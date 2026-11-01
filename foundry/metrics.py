"""The measured quantities of appendix Section 4.3, as reference code.

Section 4.3 gives draft definitions. Where a definition leaves a choice open,
the choice made here is written next to the code, and the same choice is
used everywhere. Two of these quantities are reported numerically in the
appendix (inferential distance in Run 07 and Section 3.3; the Explicator's
dispersion proxy in Run 01); the others are computed here for the first
time and are labelled as such in the check output.
"""
import re

# An inference entry whose text says the construct licenses nothing counts 0
# (the rule Run 07, Section 5 states for its weights). In the two theory
# objects only tce:C4.lic1 has this form.
_LICENSES_NOTHING = re.compile(r"licen[sc]es no\b|licen[sc]es nothing", re.I)

DRAFT_KIND_DISTANCE = {"bridge": 0.0, "rivalry": 1.0, "complementarity": 1.0,
                       "equivocation": 1.0, "none": 1.0}
# Proposed Stage 1 revision (appendix 4.3, Run 07 Section 5). Illustrative.
GRADED_KIND_DISTANCE = {"bridge": 0.0, "complementarity": 0.25, "rivalry": 0.5,
                        "equivocation": 0.75, "none": 1.0}


def effective_licenses(node):
    """Licensed inferences of a construct; scope conditions and other nodes count 0."""
    role = node.get("inferentialRole")
    if not role:
        return []
    return [x for x in role.get("licenses", []) if not _LICENSES_NOTHING.search(x.get("statement", ""))]


def _committed(mc_list):
    return any(not str(m.get("indicator", "")).lower().startswith("uncommitted") for m in mc_list or [])


def specification_completeness(obj):
    """Mean share of five construct slots filled, times share of relations with form and sign.

    Slots: definition; a measurement commitment whose indicator is not
    'uncommitted'; non-empty commitments, entitlements and (effective) licenses.
    """
    shares = []
    for c in obj["constructs"]:
        role = c["inferentialRole"]
        slots = [bool(c.get("definition")), _committed(c.get("measurementCommitments")),
                 bool(role.get("commitments")), bool(role.get("entitlements")),
                 bool(effective_licenses(c))]
        shares.append(sum(slots) / 5)
    rel = obj.get("relations", [])
    rel_share = sum(1 for r in rel if r.get("form") and r.get("sign")) / len(rel) if rel else 0.0
    return (sum(shares) / len(shares)) * rel_share, sum(shares) / len(shares), rel_share


def derivational_tightness(obj, derivations=None):
    """Mean of s/(1+a) over derivations; s = 1 closed, 0.5 asserted, 0 open/refuted.

    a = number of auxiliaries required that are not among the object's stated
    assumptions. Note: when an auxiliary was surfaced into the object by the
    same run (as tce:A8, A10, A11 were), it counts as stated.
    """
    derivations = obj.get("derivations", []) if derivations is None else derivations
    stated = {a["@id"] for a in obj.get("assumptions", [])}
    score = {"closed": 1.0, "asserted": 0.5, "open": 0.0, "refuted": 0.0}
    vals = []
    for d in derivations:
        a = sum(1 for x in d.get("auxiliariesRequired", []) if x not in stated)
        vals.append(score[d["status"]] / (1 + a))
    return sum(vals) / len(vals) if vals else None


def falsifiability_surface(obj):
    """Share of propositions marked novel with at least one rival divergence."""
    props = obj.get("propositions", [])
    n = sum(1 for p in props if p.get("factStatus") == "novel" and p.get("rivalDivergence"))
    return (n / len(props) if props else 0.0), n


def assumption_load(obj):
    """Auxiliary assumptions per proposition; hidden load = share of auxiliaries surfaced."""
    aux = [a for a in obj["assumptions"] if a["status"] == "auxiliary"]
    props = obj.get("propositions", [])
    surfaced = sum(1 for a in aux if a.get("explicitness") == "surfaced")
    return (len(aux) / len(props) if props else None), (surfaced / len(aux) if aux else 0.0), len(aux), surfaced


def inferential_distance(pairs, kind_distance=DRAFT_KIND_DISTANCE):
    """Weighted mean distance over considered pairs, given as (kind, weight) tuples.

    With the draft weights (bridge 0, everything else 1) this is
    1 - (weight of bridges / total weight), the Section 4.3 definition.
    """
    total = sum(w for _, w in pairs)
    return sum(w * kind_distance[k] for k, w in pairs) / total
