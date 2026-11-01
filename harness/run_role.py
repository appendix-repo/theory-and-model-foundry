"""Re-run one Foundry role against the Claude API and save the transcript.

Usage:
    pip install -r harness/requirements.txt
    export ANTHROPIC_API_KEY=...            # or sign in with `ant auth login`
    python3 harness/run_role.py 05                      # rerun Run 05 on the stored inputs
    python3 harness/run_role.py 01 02 03 04 05 06 07 08 --chain   # the full sequence, each run fed by the reruns before it
    python3 harness/run_role.py 05 --dry-run            # print the prompt sizes and exit

Each call writes reruns/run_XX_<UTC timestamp>.md (the model's text output) and a
.json sidecar recording the model that served the request, the stop reason, token
usage, the prompt's SHA-256 and the sources the prompt was built from.

A rerun will not reproduce the stored transcript word for word: a language model
gives different output on each call, and the model version used on 10 October 2026
was not recorded (the ledger says only "Claude (Anthropic)"). What a rerun lets a
reviewer judge is whether the instruction sets reliably produce outputs of the type
and quality the appendix describes. harness/inspect_rerun.py validates a rerun's
JSON output against the schema and prints the same counts that Check 04 reports
for the stored runs, so the two can be compared.
"""
import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_prompts import build  # noqa: E402

RERUNS = ROOT / "reruns"
DEFAULT_MODEL = "claude-opus-5-5"


def call(system, user, model, effort, max_tokens, allow_fallback):
    import anthropic

    client = anthropic.Anthropic()
    kwargs = dict(model=model, max_tokens=max_tokens, system=system,
                  thinking={"type": "adaptive"}, output_config={"effort": effort},
                  messages=[{"role": "user", "content": user}])
    if allow_fallback:
        # Server-side refusal fallback: the API may finish the request on another model.
        # Off by default, because a replication record should name one model; the
        # sidecar records which model actually served the response either way.
        with client.beta.messages.stream(betas=["server-side-fallback-2026-07-01"],
                                         fallbacks="default", **kwargs) as stream:
            return stream.get_final_message()
    with client.messages.stream(**kwargs) as stream:
        return stream.get_final_message()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("runs", nargs="+", help="run ids, 01 to 08")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--max-tokens", type=int, default=64000)
    ap.add_argument("--chain", action="store_true", help="feed each run the outputs of earlier reruns")
    ap.add_argument("--allow-fallback", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    RERUNS.mkdir(exist_ok=True)
    for rid in args.runs:
        p = build(rid, chain=args.chain)
        digest = hashlib.sha256((p["system"] + "\n\x00\n" + p["user"]).encode("utf-8")).hexdigest()
        print(f"run {rid}: prompt sha256 {digest[:16]}..., sources: {'; '.join(p['sources'])}")
        if args.dry_run:
            continue
        msg = call(p["system"], p["user"], args.model, args.effort, args.max_tokens, args.allow_fallback)
        if msg.stop_reason == "refusal":
            print(f"run {rid}: the model declined the request (stop_reason=refusal); nothing saved", file=sys.stderr)
            continue
        text = "".join(b.text for b in msg.content if b.type == "text")
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        out = RERUNS / f"run_{rid}_{stamp}.md"
        out.write_text(text, encoding="utf-8")
        side = {"run": rid, "file": out.name, "requested_model": args.model, "served_model": msg.model,
                "effort": args.effort, "stop_reason": msg.stop_reason,
                "usage": {"input_tokens": msg.usage.input_tokens, "output_tokens": msg.usage.output_tokens},
                "prompt_sha256": digest, "sources": p["sources"], "chain": args.chain,
                "instruction_set": "v0.1", "utc": stamp}
        out.with_suffix(".json").write_text(json.dumps(side, indent=1) + "\n", encoding="utf-8")
        warn = " (TRUNCATED: raise --max-tokens)" if msg.stop_reason == "max_tokens" else ""
        print(f"run {rid}: saved {out.relative_to(ROOT)} [{msg.model}, {msg.usage.output_tokens} output tokens]{warn}")


if __name__ == "__main__":
    main()
