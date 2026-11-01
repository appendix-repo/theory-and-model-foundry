"""Check 10. The citation-verification table (appendix Section 3.0).

The verification itself (checking each work against the published record) was a
manual step and cannot be re-run by code. What this check does:
- extracts the table to data/citation_verification.csv;
- recomputes the summary line "Of 36 works, 33 are supported as used and 3 are
  partly supported", and that the three partly supported works are Argyres 1996;
  Kahneman, Knetsch & Thaler 1986; and Walker & Weber 1984;
- confirms that each work is in fact cited in every run the table lists for it
  (first author's surname and year both occur in the run file);
- lists citations that the transcripts flag "to verify" and that the table does
  not cover, if any.
"""
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import APPENDIX, DATA, RUN_FILES, read_text, run_text, Report


def main():
    r = Report("Check 10: citation verification table")
    app = read_text(APPENDIX)
    block = app[app.index("| Work | Run(s) |"):app.index("Of 36 works")]
    rows = []
    for line in block.split("\n")[2:]:
        if line.startswith("|"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            rows.append({"work": c[0], "runs": c[1], "reference": c[2], "use": c[3], "verdict": c[4]})
    with open(DATA / "citation_verification.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["work", "runs", "reference", "use", "verdict"])
        w.writeheader()
        w.writerows(rows)

    partly = [x["work"] for x in rows if x["verdict"].startswith("*Partly")]
    supported = [x for x in rows if x["verdict"].startswith("Supported")]
    r.check("works in the table", len(rows), 36)
    r.check("supported", len(supported), 33)
    r.check("partly supported", len(partly), 3)
    r.check("the partly supported works", [re.sub(r" †$", "", p) for p in partly],
            ["Argyres 1996", "Kahneman, Knetsch & Thaler 1986", "Walker & Weber 1984"])
    r.check("works marked † (publisher abstract or secondary summary consulted)",
            sum(1 for x in rows if "†" in x["work"]), 3)

    missing = []
    for x in rows:
        name = x["work"].replace("†", "").strip()
        year = re.search(r"(\d{4})$", name).group(1)
        surname = re.split(r"[ ,&]", name)[0]
        for run in re.findall(r"\d{2}", x["runs"]):
            txt = run_text(run)
            if not (surname in txt and year in txt):
                missing.append(f"{name} not found in Run {run}")
    # Run 07 refers to Casciaro & Piskorski 2005 only indirectly ("the indicator Run 02
    # names (to verify that the cited literature used this)"), so its name is not in Run 07.
    indirect = ["Casciaro & Piskorski 2005 not found in Run 07"]
    r.check("table rows whose listed runs do not cite the work (excluding the known indirect case)",
            [m for m in missing if m not in indirect], [])
    r.known("Casciaro & Piskorski 2005 is named in Run 07", [m for m in missing if m in indirect], [],
            "Run 07 refers to this work only through Run 02 ('the indicator Run 02 names'); the table's run list includes 07 on that basis.")

    # Citations flagged "to verify" in the transcripts that the table does not list.
    listed = {(re.split(r"[ ,&]", x["work"].replace("†", "").strip())[0], re.search(r"(\d{4})", x["work"]).group(1))
              for x in rows}
    flagged = set()
    for rid in ("01", "02", "03", "04", "05", "06", "07", "08"):
        for m in re.finditer(r"([A-Z][A-Za-zé\-]+)(?:,? (?:et al\.|& [A-Z][A-Za-z\-]+|[A-Z][A-Za-z\-]+,? (?:& )?[A-Z][A-Za-z\-]+)*)? ?\(?(\d{4})[a-z]?\)?,? (?:[^()]{0,40})?to verify", run_text(rid)):
            flagged.add((m.group(1), m.group(2), rid))
    works = [x["work"] for x in rows]
    uncovered = sorted({f"{a} {y} (Run {rid})" for a, y, rid in flagged
                        if not any(a in w and y in w for w in works)})
    r.info(f"[INFO] 'to verify' citations found by pattern: {len(flagged)}; not in the table: {uncovered or 'none'}")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
