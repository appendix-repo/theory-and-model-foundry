"""Check 02. Every machine-readable output of the runs validates against schema v0.

Appendix claims checked:
- Section 4: the schema "has been used as the output format for the worked runs".
- Run 07, Section 6: the AlignmentMap "returns 0 validation errors".
- Section 3.8: "All eleven events validate against the schema."
- Section 3.0: `adoptedReading` is left unset in both ensembles.
- Section 4.1 design principles: which of them the v0 JSON Schema enforces by itself
  (tested with deliberately broken copies), and which are prose rules checked in code.

The JSON blocks are extracted from the transcripts by `foundry.io.json_blocks` and
also written to `extracted/` so they can be inspected or reused.
"""
import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import ROOT, run_json, load_ledger, Report
from foundry.validate import errors, prose_rule_violations

OUT = ROOT / "extracted"


def main():
    r = Report("Check 02: schema validation of run outputs")
    OUT.mkdir(exist_ok=True)
    t = run_json("01")
    d = run_json("02")
    a = run_json("07")
    full = [("Run 01 reading 1 (tce:reading-1)", t[0], None, "tce_reading-1.json"),
            ("Run 02 reading 1 (rd:reading1)", d[0], None, "rd_reading1.json"),
            ("Run 01 ensemble (tce:ensemble-1)", t[3], "FormalizationEnsemble", "tce_ensemble-1.json"),
            ("Run 02 ensemble (rd:ensemble)", d[3], "FormalizationEnsemble", "rd_ensemble.json"),
            ("Run 07 AlignmentMap", a[0], "AlignmentMap", "align_tce-rd-run07.json")]
    for label, obj, def_name, fname in full:
        errs = errors(obj, def_name)
        r.check(f"{label}: JSON Schema errors", len(errs), 0)
        for e in errs[:5]:
            r.info(f"    {e}")
        (OUT / fname).write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    # Readings 2 and 3 are returned as deltas against reading 1 (instruction set, Role 1,
    # output (b): "for each further reading, the fields that differ"). They are not full
    # theory objects, so they are saved but not validated as TheoryObjects.
    for obj, fname in [(t[1], "tce_reading-2_delta.json"), (t[2], "tce_reading-3_delta.json"),
                       (d[1], "rd_reading2_delta.json"), (d[2], "rd_reading3_delta.json")]:
        (OUT / fname).write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    r.info("[INFO] Readings 2 and 3 of each theory are deltas against reading 1 and are saved to extracted/ without validation.")

    r.check("Run 07 AlignmentMap: number of links", len(a[0]["links"]), 7)

    ledger = load_ledger()
    bad = [(ev["@id"], errors(ev, "LedgerEvent")) for ev in ledger]
    r.check("Ledger: events", len(ledger), 11)
    r.check("Ledger: events with schema errors", sum(1 for _, e in bad if e), 0)

    r.check("tce ensemble: adoptedReading unset", "adoptedReading" in t[3], False)
    r.check("rd ensemble: adoptedReading unset", "adoptedReading" in d[3], False)

    for label, obj in [("tce:reading-1", t[0]), ("rd:reading1", d[0])]:
        v = prose_rule_violations(obj)
        r.check(f"{label}: violations of Section 4.1 prose rules", len(v), 0)
        for x in v:
            r.info(f"    {x}")
        closed = [x["@id"] for x in obj.get("derivations", []) if x["status"] == "closed"]
        r.check(f"{label}: derivations marked closed (no checker exists)", closed, [])

    # Which Section 4.1 principles does the v0 JSON Schema enforce by itself?
    base = t[0]
    probes = []
    p1 = copy.deepcopy(base); del p1["constructs"][0]["inferentialRole"]
    probes.append(("P1 a construct with only a definition fails validation", p1))
    p3 = copy.deepcopy(base); p3["derivations"][0]["status"] = "closed"; p3["derivations"][0].pop("checker", None)
    probes.append(("P3 a 'closed' derivation without a checker fails validation", p3))
    p4 = copy.deepcopy(base); p4["assumptions"][0]["status"] = "maybe"
    probes.append(("P4 an assumption that is neither core nor auxiliary fails validation", p4))
    p5 = copy.deepcopy(base); del p5["constructs"][0]["@id"]
    probes.append(("P5 a construct without an @id fails validation", p5))
    for label, obj in probes:
        rejected = len(errors(obj)) > 0
        r.info(f"[INFO] {label}: schema {'ENFORCES' if rejected else 'does NOT enforce'} this"
               + ("" if rejected else " (checked in code by foundry.validate.prose_rule_violations)" if label.startswith("P3") else ""))
    r.info("[INFO] P2 (adoptedReading set only by a human LedgerEvent) is a rule about the Ledger and cannot be expressed in JSON Schema.")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
