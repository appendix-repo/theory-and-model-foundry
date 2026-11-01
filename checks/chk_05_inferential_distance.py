"""Check 05. Inferential distance between TCE and RD (Run 07 Section 5; appendix 3.3, 3.9, 4.3).

Recomputes, from the theory objects of Runs 01 and 02 and the pair
classifications of Run 07:
- each pair's weight: the number of `licenses` entries of its two constructs,
  with an entry that says it licenses nothing, and a scope condition, counting 0;
- the draft distance 13/17 = 0.76 and its three sensitivity variants;
- the graded distance under the proposed Stage 1 weights, 6.5/17 = 0.38;
- agreement between the pair kinds in data/run07_pairs.json and the AlignmentMap.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import DATA, theory_object, node_index, run_json, Report
from foundry.metrics import effective_licenses, inferential_distance, DRAFT_KIND_DISTANCE, GRADED_KIND_DISTANCE


def main():
    r = Report("Check 05: inferential distance, TCE reading 1 vs RD reading 1")
    spec = json.loads((DATA / "run07_pairs.json").read_text(encoding="utf-8"))
    idx = {**node_index(theory_object("tce")), **node_index(theory_object("rd"))}

    pairs = []
    for p in spec["pairs"]:
        w = len(effective_licenses(idx[p["tce"]])) + len(effective_licenses(idx[p["rd"]]))
        r.check(f"{p['link']} {p['tce']} <-> {p['rd']} ({p['kind']}): weight", w, p["stated_weight"])
        pairs.append((p["kind"], w))

    total = sum(w for _, w in pairs)
    bridge = sum(w for k, w in pairs if k == "bridge")
    r.check("total weight / bridge weight", (total, bridge), (17, 4))
    d = inferential_distance(pairs, DRAFT_KIND_DISTANCE)
    r.check("draft distance as a fraction", Fraction(total - bridge, total), Fraction(13, 17))
    r.check("draft distance (2 dp)", round(d, 2), spec["stated_results"]["distance_draft"])

    unweighted = 1 - sum(1 for k, _ in pairs if k == "bridge") / len(pairs)
    r.check("sensitivity: unweighted", unweighted, spec["stated_results"]["unweighted"])
    excl = [(k, w) for k, w in pairs if k != "none"]
    r.check("sensitivity: excluding the unaligned pair", inferential_distance(excl), spec["stated_results"]["excluding_unaligned"])
    l1_half = 1 - (bridge / 2) / total
    r.check("sensitivity: L1 at half weight (2 dp)", round(l1_half, 2), spec["stated_results"]["L1_half_weight"])

    g = inferential_distance(pairs, GRADED_KIND_DISTANCE)
    r.check("graded numerator", sum(w * GRADED_KIND_DISTANCE[k] for k, w in pairs), spec["stated_results"]["graded_numerator"])
    r.check("graded distance (2 dp)", round(g, 2), spec["stated_results"]["distance_graded"])

    am = run_json("07")[0]
    kinds_map = [l["kind"] for l in am["links"]]
    kinds_pairs = [p["kind"] for p in spec["pairs"] if p["kind"] != "none"]
    r.check("pair kinds L1..L7 agree with the AlignmentMap links, in order", kinds_pairs, kinds_map)
    for p, link in zip([p for p in spec["pairs"] if p["kind"] != "none"], am["links"]):
        primary_in_map = p["rd"] in link["constructs"] or p["tce"] in link["constructs"]
        r.check(f"{p['link']}: one of its constructs appears in the AlignmentMap link", primary_in_map, True)
    r.info("[INFO] L6's TCE side, tce:S3, is a scope condition; the AlignmentMap records the link under rd:C7, rd:C17 and tce:C9 and names tce:S3 in 'discharges'.")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
