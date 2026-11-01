"""Check 09. Coverage audit of the Project Lakatos components (appendix Sections 2.1 to 2.3).

Parses the role-by-role mapping table (Section 2.2) from the appendix and the
component tables (lakatos/LAKATOS_TABLES_1-4.md), and checks:
- every one of the 17 scholarly-role agents (L1 to L17) is used by at least one role;
- every one of the 13 cognitive operators (Table 2) is used by at least one role;
- 10 of the 12 routine agents (Table 1) are used, the unused two being
  Summarizer/Conclusion Builder and Data Interpreter: Descriptive;
- the Section 2.3 "Used by" column equals what the Section 2.2 table implies;
- the Section 2.1 "Feeds" column names the same roles as Section 2.2.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import APPENDIX, ROOT, read_text, Report

ROLES = ["Explicator", "Interlocutors", "Integrator", "Model Builder", "Argument Auditor",
         "Empirical Validation Designer", "Provenance Ledger"]
OPERATORS = ["Represent", "Explain", "Justify", "Extend", "Corroborate", "Measure", "Integrate",
             "Augment", "Challenge", "Refute", "Reduce", "Assimilate", "Eliminate"]


def rows(block):
    out = []
    for line in block.split("\n"):
        if line.startswith("|") and not re.match(r"^\|\s*:?-", line):
            out.append([c.strip() for c in line.strip().strip("|").split("|")])
    return out[1:]


def role_of(cell):
    return next(r for r in ROLES if r in cell.replace("*", ""))


def main():
    r = Report("Check 09: coverage audit of Lakatos components")
    app = read_text(APPENDIX)
    t22 = rows(app[app.index("### 2.2 "):app.index("### 2.3 ")])
    t23 = rows(app[app.index("### 2.3 "):app.index("Of the twelve routine agents")])
    t21 = rows(app[app.index("### 2.1 "):app.index("**Core instructions")])

    agents, ops, routine = {}, {}, {}
    for row in t22:
        role = role_of(row[0])
        agents[role] = set(re.findall(r"\bL(\d+)\b", row[1]))
        ops[role] = {o for o in OPERATORS if re.search(rf"\b{o}\b", row[2])}
        routine[role] = row[4]

    used_L = set().union(*agents.values())
    r.check("scholarly-role agents used (of L1..L17)", sorted(map(int, used_L)), list(range(1, 18)))
    used_ops = set().union(*ops.values())
    r.check("operators used (of 13)", sorted(used_ops), sorted(OPERATORS))

    tables = read_text(ROOT / "lakatos" / "LAKATOS_TABLES_1-4.md")
    t1 = tables[tables.index("Table 1."):tables.index("Table 2.")]
    names = [c[0] for c in rows(t1) if c and c[0]]
    r.check("Table 1 routine agents", len(names), 12)
    text = " ".join(routine.values())
    text = text.replace("Data Interpreter: Inferential and Causal", "Data Interpreter: Inferential; Data Interpreter: Causal")
    text = text.replace("Modeling Assistant: Exploratory and Refiner", "Modeling Assistant: Exploratory; Modeling Assistant: Refiner")
    used_routine = [n for n in names if n in text]
    unused = [n for n in names if n not in used_routine]
    r.check("routine agents used inside roles", len(used_routine), 10)
    r.check("routine agents not used", sorted(unused), sorted(["Summarizer/Conclusion Builder", "Data Interpreter: Descriptive"]))

    # Section 2.3 versus Section 2.2
    for row in t23:
        comp, used_by = row[0], row[1]
        stated = {x for x in ROLES if x in used_by}
        m = re.match(r"L(\d+)\b", comp)
        if m:
            implied = {role for role, s in agents.items() if m.group(1) in s}
        else:
            comp_ops = [o for o in OPERATORS if re.search(rf"\b{o}\b", comp)]
            implied = set().union(*[{role for role, s in ops.items() if o in s} for o in comp_ops])
        r.check(f"2.3 '{comp}' used by == 2.2 implies", sorted(stated), sorted(implied))

    # Section 2.1 Feeds versus Section 2.2
    for row in t21:
        m = re.match(r"L(\d+)", row[0])
        if not m:
            continue
        feeds = {x for x in ROLES if x in row[-1]}
        implied = {role for role, s in agents.items() if m.group(1) in s}
        if m.group(1) == "9":
            r.known(f"2.1 L9 feeds == 2.2 implies", sorted(feeds), sorted(implied),
                    "Section 2.1 says the Meta-Analyzer also feeds the Interlocutors (evidence), "
                    "but Sections 2.2 and 2.3 list it only under the Empirical Validation Designer. "
                    "This is an inconsistency in the appendix text, reported in README 'Discrepancies'.")
            continue
        r.check(f"2.1 L{m.group(1)} feeds == 2.2 implies", sorted(feeds), sorted(implied))
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
