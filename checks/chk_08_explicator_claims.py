"""Check 08. Two quantitative claims made by the Explicator runs.

(a) Run 02 (appendix 3.1): the four dyadic quantities resource dependence names,
    A's dependence on B, B's dependence on A, mutual dependence and imbalance,
    "have only two independent dimensions". Under the sum/difference aggregation
    Run 02 states, the 4 x 2 map from (D_AB, D_BA) has rank 2. Also checked:
    rd:D2's note that a unilateral rise in D_AB raises both mutual dependence and
    imbalance, so that rd:A6 and rd:A7 push in opposite directions.
    Under the 'mean' rule the rank is also 2; under 'minimum' the map is not linear
    but still has two degrees of freedom (it is a function of two inputs).

(b) Run 01 ensemble: dispersion 0.43, by the run's own proxy ("the share of
    reading-1 propositions that are restated, replaced or removed in at least one
    other reading", 3 of 7). Recomputed from the reading deltas. A proposition counts
    as changed if its id (or a suffixed variant such as tce:P3.r2) is replaced or
    removed, or if an added proposition says it sharpens it (tce:P9 on tce:P4).
    This proxy is not the Section 4.3 dispersion, which needs inferential distances
    between readings that the runs do not compute.
"""
import re
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import run_json, theory_object, Report


def main():
    r = Report("Check 08: Explicator claims (Runs 01 and 02)")

    # (a) Run 02 ------------------------------------------------------------------
    dab, dba = sp.symbols("D_AB D_BA", nonnegative=True)
    for rule, mutual in [("sum", dab + dba), ("mean", (dab + dba) / 2)]:
        quantities = sp.Matrix([dab, dba, mutual, dab - dba])
        J = quantities.jacobian([dab, dba])
        r.check(f"Run 02 ({rule} rule): rank of the four dyadic quantities in (D_AB, D_BA)", J.rank(), 2)
    J = sp.Matrix([dab + dba, dab - dba]).jacobian([dab, dba])
    r.check("rd:D2: d(mutual)/dD_AB and d(imbalance)/dD_AB under the sum rule", (J[0, 0], J[1, 0]), (1, 1))
    rd = theory_object("rd")
    d2 = next(d for d in rd["derivations"] if d["@id"] == "rd:D2")
    r.check("rd:D2 status recorded by Run 02", d2["status"], "asserted")
    r.check("rd:D2 auxiliary required", d2.get("auxiliariesRequired"), ["rd:A10"])
    oq = " ".join(rd.get("openQuestions", []))
    r.check("Run 02 openQuestions state the two-degrees-of-freedom point",
            "two degrees of freedom" in oq, True)

    # (b) Run 01 ------------------------------------------------------------------
    t = theory_object("tce")
    blocks = run_json("01")
    base = [p["@id"] for p in t["propositions"]]
    changed = set()
    for delta in blocks[1:3]:
        ids = [p["@id"] for p in delta.get("replace", {}).get("propositions", [])]
        ids += [x for x in delta.get("remove", []) if isinstance(x, str)]
        for i in ids:
            root = re.sub(r"\.r\d+$", "", i)
            if root in base:
                changed.add(root)
        for p in delta.get("add", {}).get("propositions", []):
            for m in re.findall(r"sharpening of (P\d+)", p.get("statement", "")):
                changed.add("tce:" + m)
    ens = blocks[3]
    r.check("Run 01: reading-1 propositions changed in another reading", sorted(changed), ["tce:P3", "tce:P4", "tce:P7"])
    r.check("Run 01: dispersion proxy (2 dp)", round(len(changed) / len(base), 2), ens["dispersion"])
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
