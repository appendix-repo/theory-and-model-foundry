"""Check 11. Reference computation of the Section 4.3 quantities (demonstration).

The appendix defines six measured quantities (Section 4.3) and reports values for
only two of them (inferential distance, Check 05; the Explicator's dispersion
proxy, Check 08). This script computes the other four on the two reading-1
theory objects, using foundry/metrics.py, to show that they are computable
directly from the schema as Section 4.3 says.

THE NUMBERS PRINTED HERE ARE NOT REPORTED IN THE APPENDIX OR THE PROPOSAL.
They depend on operational choices documented in foundry/metrics.py, and their
reliability and validity are objects of the Stage 1 studies (Section 5.2). The
only pass/fail conditions are that each value is in its stated range.

The "after the Model Builder" figures treat Run 05's derivation table as the
derivations of reading 1 and its surfaced assumptions (A16 to A21) as auxiliaries
not stated in reading 1. Section 1.4 names exactly this before/after comparison
as the Model Builder's evaluation.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import run_text, theory_object, Report
from foundry.metrics import (specification_completeness, derivational_tightness,
                             falsifiability_surface, assumption_load)


def run05_derivations():
    text = run_text("05")
    block = text[text.index("### Derivation table"):text.index("## 5.")]
    out = []
    for line in block.split("\n"):
        if not line.startswith("| tce:D"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        aux = ["tce:" + a for a in re.findall(r"\b(A\d+)\b", c[5])]
        status = c[4].replace("*", "")
        if c[0] == "tce:D11":
            out.append({"@id": "tce:D11-cost", "status": "asserted", "auxiliariesRequired": []})
            out.append({"@id": "tce:D11-exit", "status": "open", "auxiliariesRequired": []})
            continue
        out.append({"@id": c[0], "status": re.match(r"(asserted|open|refuted|closed)", status).group(1),
                    "auxiliariesRequired": aux})
    return out


def main():
    r = Report("Check 11: Section 4.3 quantities on the reading-1 objects (demonstration only)")
    for label, obj in [("tce:reading-1", theory_object("tce")), ("rd:reading1", theory_object("rd"))]:
        sc, cons, rel = specification_completeness(obj)
        dt = derivational_tightness(obj)
        fs, fs_n = falsifiability_surface(obj)
        al, hidden, n_aux, n_surf = assumption_load(obj)
        r.info(f"{label}: specification completeness = {sc:.3f} (construct slots {cons:.3f} x relations with form and sign {rel:.3f})")
        r.info(f"{label}: derivational tightness = {dt:.3f} over {len(obj.get('derivations', []))} derivations")
        r.info(f"{label}: falsifiability surface = {fs:.3f} ({fs_n} propositions novel with a rival divergence;"
               " no rival divergences are recorded in reading 1, because rivals come later in the loop)")
        r.info(f"{label}: assumption load = {al:.3f} auxiliaries per proposition ({n_aux} auxiliaries); hidden share = {hidden:.3f} ({n_surf} surfaced)")
        for name, v in [("specification completeness", sc), ("derivational tightness", dt),
                        ("falsifiability surface", fs), ("hidden assumption share", hidden)]:
            r.check(f"{label}: {name} in [0, 1]", 0 <= v <= 1, True)

    tce = theory_object("tce")
    after = run05_derivations()
    dt_after = derivational_tightness(tce, after)
    r.info(f"tce:reading-1 after the Model Builder: derivational tightness = {dt_after:.3f} over {len(after)} attempts "
           f"(before: {derivational_tightness(tce):.3f} over 3 asserted derivations)")
    _, _, n_aux, n_surf = assumption_load(tce)
    text5 = run_text("05")
    new_aux = re.findall(r"^\| (tce:A\d+) \|", text5[text5.index("## 6. Surfaced"):text5.index("## 7.")], re.M)
    aux_after = n_aux + len(new_aux)
    n_props = len(tce["propositions"])
    r.info(f"tce:reading-1 after the Model Builder: assumption load = {aux_after / n_props:.3f} "
           f"({n_aux} stated + {len(new_aux)} surfaced auxiliaries, {n_props} propositions); "
           f"hidden share = {(n_surf + len(new_aux)) / aux_after:.3f}")
    r.check("after-pass derivational tightness in [0, 1]", 0 <= dt_after <= 1, True)
    r.check("Run 05 derivation attempts parsed", len(after), 11)
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
