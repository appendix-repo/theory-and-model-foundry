"""Check 01. The appendix reproduces the repository files without edits.

Appendix claims checked:
- Annex B: transcripts "reproduced unedited from `runs/`, except that heading
  levels are lowered" (B.0 to B.8).
- Annex B.9 is `runs/09_ledger_trace.json`.
- Annex A.1 and A.2 are `schema/theory-object.v0.schema.json` and
  `schema/context.v0.jsonld`.
- Section 1.8 lens table is the v0.2 instruction-set lens table.

Comparison rule for transcripts: heading markers (#, ##, ...) are normalized,
horizontal rules and blank lines are ignored, and the run file's own title
line (which the appendix replaces with its B.n heading) is dropped. Every other
line must match exactly and in order.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import APPENDIX, RUNS, RUN_FILES, SCHEMA_PATH, CONTEXT_PATH, LEDGER_PATH, ROOT, read_text, Report

ANNEX = {"B.0": "00", "B.1": "01", "B.2": "02", "B.3": "03", "B.4": "04",
         "B.5": "05", "B.6": "06", "B.7": "07", "B.8": "08"}


def norm(lines):
    out = []
    for line in lines:
        s = line.rstrip()
        if not s.strip() or s.strip() == "---":
            continue
        out.append(re.sub(r"^#+\s*", "#", s))
    return out


def first_json_after(text, marker):
    i = text.index(marker)
    j = text.index("```json", i)
    j = text.index("\n", j) + 1
    k = text.index("\n```", j)
    return json.loads(text[j:k])


def main():
    r = Report("Check 01: appendix matches repository files")
    app = read_text(APPENDIX)
    lines = app.split("\n")
    starts = {}
    for i, line in enumerate(lines):
        m = re.match(r"^### (B\.\d) ", line)
        if m:
            starts[m.group(1)] = i
        if line.startswith("## Annex C"):
            starts["end"] = i
    order = sorted(k for k in starts if k != "end") + ["end"]
    for n, key in enumerate(order[:-1]):
        if key not in ANNEX:
            continue
        section = norm(lines[starts[key] + 1:starts[order[n + 1]]])
        run_lines = norm(read_text(RUNS / RUN_FILES[ANNEX[key]]).split("\n"))[1:]  # drop title
        r.check(f"Annex {key} == runs/{RUN_FILES[ANNEX[key]]} ({len(run_lines)} lines)", section == run_lines, True)

    r.check("Annex B.9 == runs/09_ledger_trace.json",
            first_json_after(app, "### B.9 ") == json.loads(read_text(LEDGER_PATH)), True)
    r.check("Annex A.1 == schema/theory-object.v0.schema.json",
            first_json_after(app, "### A.1 ") == json.loads(read_text(SCHEMA_PATH)), True)
    r.check("Annex A.2 == schema/context.v0.jsonld",
            first_json_after(app, "### A.2 ") == json.loads(read_text(CONTEXT_PATH)), True)

    def lens_rows(text):
        return [l.strip() for l in text.split("\n")
                if re.match(r"^\| (Transaction-cost|Behavioral|Institutional|Evolutionary|Network) \|", l)]
    v02 = read_text(ROOT / "instruction-sets" / "FOUNDRY_ROLE_INSTRUCTION_SETS.md")
    sec18 = app[app.index("### 1.8 "):app.index("### 1.9 ")]
    r.check("Section 1.8 lens table == instruction-sets v0.2 lens table", lens_rows(sec18) == lens_rows(v02), True)

    v01 = read_text(ROOT / "instruction-sets" / "FOUNDRY_ROLE_INSTRUCTION_SETS_v0.1.md")
    strip = lambda t: [l for l in t.split("\n")[1:] if not l.startswith("*v0.2 changes")]
    d01 = [l for l in strip(v01) if not re.match(r"^\|( (Lens|Transaction-cost|Behavioral|Institutional|Evolutionary|Network)|---)", l)]
    d02 = [l for l in strip(v02) if not re.match(r"^\|( (Lens|Transaction-cost|Behavioral|Institutional|Evolutionary|Network)|---)", l)]
    r.check("v0.1 and v0.2 differ only in the lens table (Section 3.0, 1.8)",
            [l for l in d01 if l.strip()] == [l for l in d02 if l.strip()], True)

    body = app[:app.index("## Annex A.")]
    no_refs = body[:body.index("## References")]
    r.info(f"[INFO] Word count (whitespace tokens): Sections 0 to 6 = {len(no_refs.split())}; "
           f"with References = {len(body.split())}. The appendix front matter says 'about 10,500'. Informational only.")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
