"""Check 04. The counts reported in appendix Sections 3.0 to 3.6 are the counts in the runs.

Each count is recomputed from the run file itself: from the JSON theory objects
where there is one, and otherwise from the tables and headings of the transcript.
The parsing rule for each count is stated next to it.
"""
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import run_text, run_json, theory_object, Report


def section(text, start, end=None):
    i = text.index(start)
    j = text.index(end, i) if end else len(text)
    return text[i:j]


def table_rows(text, first_cell):
    """Rows of a markdown table whose first cell matches the regex first_cell."""
    rows = []
    for line in text.split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and re.fullmatch(first_cell, cells[0]):
                rows.append(cells)
    return rows


def main():
    r = Report("Check 04: counts reported for Runs 01 to 08")

    # --- Run 01 (Section 3.1) -------------------------------------------------
    t = theory_object("tce")
    r.check("Run 01: constructs", len(t["constructs"]), 19)
    four = all(all(c["inferentialRole"].get(k) for k in ("commitments", "entitlements", "licenses", "precludes"))
               for c in t["constructs"])
    r.check("Run 01: every construct has all four inferential-role fields non-empty", four, True)
    st = Counter(a["status"] for a in t["assumptions"])
    r.check("Run 01: assumptions", len(t["assumptions"]), 13)
    r.check("Run 01: core / auxiliary", (st["core"], st["auxiliary"]), (7, 6))
    r.check("Run 01: propositions", len(t["propositions"]), 7)
    fs = {p["@id"]: p.get("factStatus") for p in t["propositions"]}
    r.check("Run 01: P1 fact status", fs["tce:P1"], "accommodation")
    r.check("Run 01: P5, P6 fact status", (fs["tce:P5"], fs["tce:P6"]), ("novel", "novel"))
    ens = run_json("01")[3]
    r.check("Run 01: readings in the ensemble", len(ens["members"]), 3)
    r.check("Run 01: pivotal differences", len(ens["pivotalDifferences"]), 4)
    a13 = next(a for a in t["assumptions"] if a["@id"] == "tce:A13")
    r.check("Run 01: tce:A13 is a surfaced auxiliary (Section 3.1, 3.7)",
            (a13["status"], a13["explicitness"]), ("auxiliary", "surfaced"))

    # --- Run 02 (Section 3.1) -------------------------------------------------
    d = theory_object("rd")
    r.check("Run 02: constructs", len(d["constructs"]), 19)
    r.check("Run 02: assumptions", len(d["assumptions"]), 10)
    r.check("Run 02: core assumptions", sum(a["status"] == "core" for a in d["assumptions"]), 4)
    r.check("Run 02: propositions", len(d["propositions"]), 9)
    r.check("Run 02: readings in the ensemble", len(run_json("02")[3]["members"]), 3)

    # --- Run 03 (Section 3.2): '### On.' headings, then the bold word after 'Strength:'
    s3 = run_text("03")
    objs = re.findall(r"^### (O\d+)\.", s3, re.M)
    strengths = [m.lower() for m in re.findall(r"^- \*\*Strength:\*\* \*\*(fatal|damaging|minor)", s3, re.M)]
    r.check("Run 03: objections", len(objs), 10)
    r.check("Run 03: fatal / damaging / minor",
            tuple(Counter(strengths)[k] for k in ("fatal", "damaging", "minor")), (1, 7, 2))

    # --- Run 04 (Section 3.2): ranked objection table, Strength column
    s4 = section(run_text("04"), "## 1. Objections")
    rows = table_rows(s4, r"\d+")
    kinds = [re.search(r"fatal|damaging|minor", row[4]).group(0) for row in rows]
    r.check("Run 04: objections", len(rows), 9)
    r.check("Run 04: fatal / damaging / minor",
            tuple(Counter(kinds)[k] for k in ("fatal", "damaging", "minor")), (1, 6, 2))

    # --- Run 05 (Section 3.4): derivation table; D11 counts as two attempts (cost and exit clauses)
    s5 = section(run_text("05"), "### Derivation table", "## 5.")
    rows = table_rows(s5, r"tce:D\d+")
    statuses = []
    for row in rows:
        st5 = row[4].replace("*", "")
        if row[0] == "tce:D11":
            statuses += ["asserted", "open"]
        else:
            statuses.append(re.match(r"(asserted|open|refuted|closed)", st5).group(1))
    c5 = Counter(statuses)
    r.check("Run 05: derivation attempts", len(statuses), 11)
    r.check("Run 05: asserted / open / refuted",
            (c5["asserted"], c5["open"], c5["refuted"]), (5, 5, 1))
    r.check("Run 05: closed", c5["closed"], 0)
    surfaced = table_rows(section(run_text("05"), "## 6. Surfaced assumptions", "## 7."), r"tce:A\d+")
    r.check("Run 05: surfaced assumptions", [x[0] for x in surfaced],
            ["tce:A16", "tce:A17", "tce:A18", "tce:A19", "tce:A20", "tce:A21"])

    # --- Run 06 (Section 3.5)
    s6 = run_text("06")
    am = table_rows(section(s6, "## 1. Argument map", "## 2."), r"AM\d+ \(.*\)")
    r.check("Run 06: Toulmin steps", len(am), 11)
    # Backing column: 'None', 'None given', or 'Examples only' (AM3). The run itself says
    # the exposition "relies on stated premises and illustrative examples" and cites no
    # evidence, so 'Examples only' is counted as no backing.
    r.check("Run 06: steps with backing (Backing column other than None / Examples only)",
            sum(1 for row in am if not re.match(r"(none|examples only)", row[4].lower())), 0)
    gaps = table_rows(section(s6, "## 2. Warrant gaps", "## 3."), r"W\d+")
    r.check("Run 06: warrant gaps", len(gaps), 11)
    mm = sorted(set(re.findall(r"\(MM(\d)\)", section(s6, "## 3.", "## 4."))))
    r.check("Run 06: inference-mode mismatches", len(mm), 5)
    dfs = table_rows(section(s6, "## 4.", "## 5."), r"W\d+")
    r.check("Run 06: defeaters (one per warrant)", len(dfs), 11)

    # --- Run 07 (Section 3.3): AlignmentMap link kinds
    links = Counter(l["kind"] for l in run_json("07")[0]["links"])
    r.check("Run 07: bridge / rivalry / complementarity / equivocation",
            (links["bridge"], links["rivalry"], links["complementarity"], links["equivocation"]), (1, 1, 3, 2))
    r.check("Run 07: pairs with no alignment (Section 1 table, '**No alignment.**')",
            run_text("07").count("**No alignment.**"), 1)

    # --- Run 08 (Section 3.6)
    s8 = run_text("08")
    rp = table_rows(section(s8, "## 1.", "## 2."), r"RP\d+")
    nn = table_rows(section(s8, "## 1.", "## 2."), r"N\d+")
    designs = re.findall(r"^### (D\d)\.", s8, re.M)
    rank = table_rows(section(s8, "## 4. Severity ranking", "## 5."), r"\d+")
    r.check("Run 08: risky predictions", len(rp), 7)
    r.check("Run 08: contrasts on which all theories agree", len(nn), 3)
    r.check("Run 08: designs", len(designs), 7)
    r.check("Run 08: severity ranking rows", len(rank), 7)
    r.check("Run 08: top-ranked design", rank[0][1].split()[0], "D1")
    r.check("Run 08: lowest-ranked design", rank[-1][1].split()[0], "D6")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
