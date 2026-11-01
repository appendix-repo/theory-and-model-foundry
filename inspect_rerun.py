"""Validate a rerun's JSON output and print its counts, for comparison with the stored run.

Usage:
    python3 harness/inspect_rerun.py reruns/run_01_20261102T101500Z.md

Every ```json block in the file is parsed. Blocks typed TheoryObject (with
constructs), FormalizationEnsemble or AlignmentMap are validated against schema
v0 and summarized: constructs, assumptions (core/auxiliary), propositions,
derivation statuses, ensemble members, link kinds. Compare with the output of
checks/chk_04_run_counts.py for the stored runs.
"""
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from foundry.io import json_blocks, read_text  # noqa: E402
from foundry.validate import errors, prose_rule_violations  # noqa: E402


def main(path):
    try:
        blocks = json_blocks(read_text(path))
    except json.JSONDecodeError as e:
        print(f"a JSON block does not parse: {e}")
        return 1
    print(f"{path}: {len(blocks)} JSON block(s)")
    status = 0
    for b in blocks:
        kind, bid = b.get("@type"), b.get("@id")
        if kind == "TheoryObject" and "constructs" in b and "differsFrom" not in b:
            errs = errors(b)
            st = Counter(a.get("status") for a in b.get("assumptions", []))
            ds = Counter(d.get("status") for d in b.get("derivations", []))
            print(f"  {bid}: schema errors {len(errs)}; constructs {len(b['constructs'])}; "
                  f"assumptions {len(b.get('assumptions', []))} (core {st['core']}, auxiliary {st['auxiliary']}); "
                  f"propositions {len(b.get('propositions', []))}; derivations {dict(ds)}; "
                  f"prose-rule violations {len(prose_rule_violations(b))}")
        elif kind in ("FormalizationEnsemble", "AlignmentMap"):
            errs = errors(b, kind)
            extra = (f"members {len(b.get('members', []))}" if kind == "FormalizationEnsemble"
                     else f"links {dict(Counter(l.get('kind') for l in b.get('links', [])))}")
            print(f"  {bid} ({kind}): schema errors {len(errs)}; {extra}")
        else:
            print(f"  {bid or '(no @id)'}: {kind or 'untyped'} block, not validated (a reading delta or other output)")
            continue
        for e in errs[:10]:
            print(f"      {e}")
        status = status or (1 if errs else 0)
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
