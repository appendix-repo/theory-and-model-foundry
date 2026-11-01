"""Assemble the prompt for each agent run (Runs 01 to 08) from the repository files.

Usage:
    python3 harness/build_prompts.py              # writes harness/prompts/run_XX.md for all runs
    python3 harness/build_prompts.py 05           # one run
    python3 harness/build_prompts.py --chain      # use earlier reruns in reruns/ as upstream inputs

System prompt = common preamble + the role's section of instruction set v0.1
(+ the lens row for an Interlocutor). User message = the schema, then the inputs.
This is a reconstruction: the prompts of the original runs were not archived
(see harness/README.md).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from foundry.io import RUNS, RUN_FILES, APPENDIX, SCHEMA_PATH, read_text, json_blocks

CFG = json.loads((Path(__file__).parent / "runs.json").read_text(encoding="utf-8"))
OUT = Path(__file__).parent / "prompts"
RERUNS = ROOT / "reruns"


def instruction_sections():
    text = read_text(ROOT / CFG["instruction_set"])
    parts = re.split(r"(?m)^## ", text)
    sections = {p.split("\n", 1)[0].strip(): "## " + p for p in parts[1:]}
    return sections


def strip_rules(s):
    return re.sub(r"\n---\s*$", "", s.strip())


def lens_row(role_text, lens):
    header = [l for l in role_text.split("\n") if l.startswith("| Lens |")][0]
    row = [l for l in role_text.split("\n") if l.startswith(f"| {lens} |")][0]
    return f"{header}\n|---|---|---|---|---|---|\n{row}"


def case_input(letter):
    text = read_text(RUNS / RUN_FILES["00"])
    i = text.index(f"## Input {letter}:")
    j = text.find("\n## Input ", i + 5)
    return text[i:] if j < 0 else text[i:j]


def latest_rerun(run_id):
    files = sorted(RERUNS.glob(f"run_{run_id}_*.md"))
    return files[-1] if files else None


def upstream_text(run_id, chain):
    if chain and latest_rerun(run_id):
        return read_text(latest_rerun(run_id)), f"rerun {latest_rerun(run_id).name}"
    return read_text(RUNS / RUN_FILES[run_id]), f"stored runs/{RUN_FILES[run_id]}"


def resolve(item, chain):
    kind, _, key = item.partition(":")
    if kind == "input":
        return f"### Prose exposition (Input {key})\n\n{case_input(key)}", f"runs/case_inputs.md, Input {key}"
    if kind == "object":
        src = CFG["chain_sources"][item]
        text, where = upstream_text(src, chain)
        obj = json_blocks(text)[0]
        return (f"### Theory object `{obj['@id']}` (reading 1)\n\n```json\n"
                f"{json.dumps(obj, indent=1, ensure_ascii=False)}\n```"), f"first JSON block of {where}"
    if kind == "run":
        text, where = upstream_text(key, chain)
        return f"### Output of Run {key}\n\n{text}", where
    if kind == "appendix" and key == "4.3":
        app = read_text(APPENDIX)
        sec = app[app.index("### 4.3 "):app.index("**Revision proposed by the first run.**")]
        return f"### Draft definitions of the measured quantities\n\n{sec.strip()}", "appendix Section 4.3 (draft definitions only)"
    raise ValueError(item)


def build(run_id, chain=False):
    spec = CFG["runs"][run_id]
    sec = instruction_sections()
    preamble = strip_rules(sec["Common preamble (all roles)"])
    role = strip_rules(sec[spec["role"]])
    sources = [CFG["instruction_set"] + ": Common preamble, " + spec["role"]]
    if "lens" in spec:
        role = role.replace("[LENS]", spec["lens"].lower())
        role = role.split("### Lens specifications")[0].rstrip() + \
            "\n\n### Lens specification\n\n" + lens_row(sec[spec["role"]], spec["lens"])
        sources.append(f"lens row: {spec['lens']}")
    system = preamble + "\n\n---\n\n" + role
    parts = ["## Schema (draft v0)\n\n```json\n" + read_text(SCHEMA_PATH).strip() + "\n```"]
    sources.append("schema/theory-object.v0.schema.json")
    for item in spec["inputs"]:
        text, where = resolve(item, chain)
        parts.append(text)
        sources.append(where)
    user = "\n\n".join(parts) + "\n\nProduce your output as your instruction set specifies."
    return {"run": run_id, "system": system, "user": user, "sources": sources}


def main(argv):
    chain = "--chain" in argv
    ids = [a for a in argv if not a.startswith("--")] or list(CFG["runs"])
    OUT.mkdir(exist_ok=True)
    for rid in ids:
        p = build(rid, chain)
        doc = (f"# Prompt for Run {rid} (reconstructed)\n\nSources: " + "; ".join(p["sources"]) +
               "\n\n## SYSTEM\n\n" + p["system"] + "\n\n## USER\n\n" + p["user"] + "\n")
        (OUT / f"run_{rid}.md").write_text(doc, encoding="utf-8")
        print(f"run {rid}: system {len(p['system'])} chars, user {len(p['user'])} chars -> harness/prompts/run_{rid}.md")


if __name__ == "__main__":
    main(sys.argv[1:])
