# Run 02: Explicator on Input B (resource-dependence theory)
*Instruction set: Foundry v0.1, Role 1. Input: case_inputs.md, Input B. Single run, unedited.*

---

## 1. Segmentation

The input has nine sentences. I number them B.1 to B.9 and cite them by these numbers throughout. "Text" means what the sentence says. "Inferred" means my reading, which the theorist should check.

| # | Sentence (abridged) | Introduces | Ids |
|---|---|---|---|
| B.1 | "Organizations are not self-sufficient." | assumption, scope | rd:A1, rd:S1 |
| B.2 | "They depend on their environments for critical resources, and that dependence is the source of other actors' power over them." | constructs, relation, assumption | rd:C1, rd:C4, rd:R3, rd:A2 |
| B.3 | "Dependence on a supplier or buyer is greater the more important the resource is ... and the fewer alternative sources ..." | constructs, relations, scope | rd:C2, rd:C3, rd:R1, rd:R2, rd:A5, rd:S2, rd:P1 |
| B.4 | "Organizations are run by managers who seek to reduce uncertainty and preserve the organization's autonomy, so they act to manage dependence." | constructs, mechanism, assumption | rd:C8, rd:C9, rd:C10, rd:R6, rd:A3 |
| B.5 | "They may absorb ... co-opt ... negotiate long-term arrangements, or diversify away ..." | constructs (tactics) | rd:C11 to rd:C15, rd:P3 |
| B.6 | "Which tactic is chosen depends on how much power each side holds: mergers are most likely where an organization faces high constraint from a partner, and especially where mutual dependence ... is high, because mutual dependence makes absorption feasible and attractive to both sides." | constructs, relations, mechanism, predictions | rd:C5, rd:C6, rd:C16, rd:C17, rd:R9 to rd:R11, rd:R14, rd:R15, rd:A6, rd:P4, rd:P5 |
| B.7 | "Power imbalance, by contrast, makes the weaker side want to absorb the stronger but leaves it less able to do so." | construct, relations, mechanism | rd:C7, rd:R12, rd:R13, rd:A7, rd:P6 |
| B.8 | "Organizational boundaries therefore reflect the political management of external dependencies rather than the minimization of costs." | construct, explanatory claim, contrast with rival | rd:C18, rd:A4, rd:P9 |
| B.9 | "Empirically, we should observe that mergers and other boundary-spanning ties concentrate between organizations that depend heavily on each other, and that boundaries shift when the structure of resource dependencies shifts." | construct, predictions | rd:C19, rd:R17, rd:P7, rd:P8 |

The text has no explicit scope sentence. B.1 and B.3 set the scope implicitly (rd:S1, rd:S2). The other scope conditions are inferred or surfaced (Section 3).

---

## 2. Output (a): Theory object, Reading 1 ("decomposition reading")

Reading 1 settles the three underdetermined points (Section 5) as follows. Power is *constituted* by dependence (B.2 "source" read as Emerson-style identity). "Constraint" in B.6 is the focal organization's unilateral dependence on the partner. The cost-minimization contrast in B.8 is part of the hard core.

```json
{
  "@context": ["https://foundry.lakatos.example/schema/context.v0.jsonld", {"rd": "https://foundry.lakatos.example/theory/resource-dependence#"}],
  "@id": "rd:reading1",
  "@type": "TheoryObject",
  "schemaVersion": "0.1-draft",
  "label": "Resource-dependence theory of organizational boundaries, Reading 1 (decomposition reading)",
  "tradition": "resource-dependence theory",
  "readingOf": "rd:ensemble",
  "sources": [{"citation": "Foundry demonstration case inputs, Input B (paraphrase after Pfeffer & Salancik 1978; Casciaro & Piskorski 2005)", "span": "B.1-B.9"}],
  "stanceProfile": {
    "epistemologicalStance": "positivism-lay",
    "corroborationLogic": "inductivism-frequentist",
    "ontologicalCommitments": ["organizations as actors with interests", "external actors that control resources", "dependence and power as directed dyadic relations", "managers with goals (uncertainty reduction, autonomy)", "inter-organizational ties (mergers, interlocks, joint ventures, contracts)", "organizational boundaries"],
    "modelClasses": ["relational", "causal", "teleological"],
    "explanatoryNorms": ["coverage-parsimony"],
    "justificationStrategies": ["eliminative"],
    "inferenceNorms": ["abductive", "deductive"],
    "evidence": "positivism-lay: B.9 'Empirically, we should observe' states observable regularities without a measurement theory. inductivism-frequentist (tentative): predictions are distributional tendencies ('most likely' B.6, 'concentrate' B.9) and no refutation condition is stated. relational: the main constructs are dyadic relations (B.2, B.3, B.6, B.7). teleological: managers 'act to manage dependence' (B.4). causal: 'makes absorption feasible' (B.6), 'leaves it less able' (B.7). coverage-parsimony: one principle (dependence management) accounts for four tactics (B.5) and for boundaries (B.8). eliminative: 'rather than the minimization of costs' (B.8) sets the account against a cost-based rival. abductive with deductive language: 'therefore' (B.8) presents an inference to the best explanation as if it followed from B.1-B.7 (see rd:D1)."
  },
  "scopeConditions": [
    {"@id": "rd:S1", "statement": "Organizations that need critical resources controlled by other actors in their environment.", "explicitness": "explicit"},
    {"@id": "rd:S2", "statement": "The unit is the directed dyad between a focal organization and a supplier or buyer; dependence is assessed dyad by dyad.", "explicitness": "explicit"},
    {"@id": "rd:S3", "statement": "Managers have enough discretion to choose and carry out a tactic.", "explicitness": "implicit"},
    {"@id": "rd:S4", "statement": "Merger and acquisition are legally and financially open to the dyad (no regulatory bar, transferable ownership). Without this, rd:P4-rd:P7 do not apply; rd:P1-rd:P3 still apply to organizations of any legal form.", "explicitness": "surfaced"}
  ],
  "constructs": [
    {"@id": "rd:C1", "label": "Resource dependence (of A on B)", "definition": "The extent to which focal organization A relies on actor B for a resource A needs; greater the more important the resource and the fewer the alternative sources (B.2, B.3).", "constructType": "relation", "level": "dyad",
     "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "directed dyad: focal organization and a supplier or buyer (B.3)"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C1.c1", "statement": "If A depends on B, then B controls a resource A uses in its operations.", "refs": ["rd:A1"], "strength": "strict"},
                       {"@id": "rd:C1.c2", "statement": "If A depends heavily on B, then A's operations would suffer if B withheld the resource, because A could not quickly replace it.", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C1.e1", "statement": "If B's resource is important to A's operations and A has few alternative sources, one is entitled to assert that A depends heavily on B.", "refs": ["rd:C2", "rd:C3", "rd:P1"], "strength": "strict"}],
       "licenses": [{"@id": "rd:C1.l1", "statement": "If A depends on B to degree d, infer that B has power over A to degree d.", "refs": ["rd:C4", "rd:P2"], "strength": "strict"},
                    {"@id": "rd:C1.l2", "statement": "If A depends heavily on B, infer that A's managers will take some tactic aimed at B.", "refs": ["rd:C11", "rd:A3"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C1.p1", "statement": "A depends heavily on B although the resource is peripheral to A and many equivalent sources exist.", "refs": ["rd:P1"], "strength": "strict"}]
     }},
    {"@id": "rd:C2", "label": "Resource importance", "definition": "How important the resource is to the organization's operations (B.3).", "constructType": "attribute", "level": "dyad",
     "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "resource flow within a dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C2.c1", "statement": "If a resource is important to A, then losing it would substantially disrupt A's operations.", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C2.e1", "statement": "If A's operations would fall substantially if the resource were withdrawn, one is entitled to assert high importance (inferred criterion; the text names none).", "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C2.l1", "statement": "If importance rises and alternatives stay the same, infer that A's dependence on the supplier rises.", "refs": ["rd:R1", "rd:P1"], "strength": "strict"}],
       "precludes": [{"@id": "rd:C2.p1", "statement": "A resource is highly important to A, yet losing it leaves A's operations unaffected.", "strength": "strict"}]
     }},
    {"@id": "rd:C3", "label": "Availability of alternative sources", "definition": "The number of sources other than B from which A could obtain the resource (or, for a buyer, to which A could sell) (B.3).", "constructType": "attribute", "level": "dyad",
     "measurementCommitments": [{"indicator": "uncommitted (the text implies a count of alternative suppliers or buyers but gives no indicator)", "unitOfAnalysis": "directed dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C3.c1", "statement": "If A has alternative sources, then A could obtain the resource from actors other than B on terms not much worse (the 'comparable terms' qualifier is inferred).", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C3.e1", "statement": "If several other actors can supply the resource to A or buy A's output, one is entitled to assert that alternatives are available.", "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C3.l1", "statement": "If alternatives fall and importance stays the same, infer that A's dependence on B rises.", "refs": ["rd:R2", "rd:P1"], "strength": "strict"},
                    {"@id": "rd:C3.l2", "statement": "If A gains alternatives, infer that B's power over A falls.", "refs": ["rd:C4"], "strength": "strict"}],
       "precludes": [{"@id": "rd:C3.p1", "statement": "A has many ready alternatives, yet B can withhold the resource and A suffers as if B were the only source.", "strength": "strict"}]
     }},
    {"@id": "rd:C4", "label": "Power (of B over A)", "definition": "Other actors' power over the organization, which the organization's dependence on them gives rise to (B.2).", "constructType": "relation", "level": "dyad",
     "measurementCommitments": [{"indicator": "uncommitted (in Reading 1, measured through rd:C1; no separate indicator)", "unitOfAnalysis": "directed dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C4.c1", "statement": "If B has power over A, then B can restrict A's choices or press demands that A would otherwise refuse (inferred; the text does not say what power does).", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C4.e1", "statement": "If A depends on B to degree d, one is entitled to assert that B has power over A to degree d, with no further evidence needed.", "refs": ["rd:C1", "rd:A2"], "strength": "strict"}],
       "licenses": [{"@id": "rd:C4.l1", "statement": "If B has power over A, infer that A's autonomy is lower than it would otherwise be.", "refs": ["rd:C10", "rd:R4"], "strength": "defeasible"},
                    {"@id": "rd:C4.l2", "statement": "If both sides' power is known, infer which tactic A will choose toward B.", "refs": ["rd:C11", "rd:P4", "rd:P5", "rd:P6"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C4.p1", "statement": "B has power over A although A depends on B for nothing.", "refs": ["rd:A2"], "strength": "strict"}]
     },
     "alternativeRoles": [{"readingLabel": "Reading 3: power caused by, not constituted by, dependence",
       "commitments": [{"@id": "rd:C4.r3c1", "statement": "If B has power over A, then B can restrict A's choices; whether B uses this capacity is a separate question.", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C4.r3e1", "statement": "If A depends on B and there is independent evidence that B shapes A's decisions (for example, terms imposed on A), one is entitled to assert B's power over A.", "refs": ["rd:C1"], "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C4.r3l1", "statement": "If A's dependence on B rises, infer that B's power over A probably rises.", "refs": ["rd:P2"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C4.r3p1", "statement": "B's power over A is high and stays high after A's dependence on B is removed, with nothing else changing.", "strength": "defeasible"}]}]},
    {"@id": "rd:C5", "label": "Constraint (from a partner)", "definition": "The constraint an organization faces from a partner (B.6). The text does not define it. Reading 1 takes it as A's unilateral dependence on B.", "constructType": "relation", "level": "dyad",
     "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "directed dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C5.c1", "statement": "If A faces high constraint from B, then A depends heavily on B; B's dependence on A may be high or low.", "refs": ["rd:C1"], "strength": "strict"}],
       "entitlements": [{"@id": "rd:C5.e1", "statement": "If A's dependence on B is high, one is entitled to assert high constraint from B.", "refs": ["rd:C1"], "strength": "strict"}],
       "licenses": [{"@id": "rd:C5.l1", "statement": "If A faces high constraint from B and B's dependence on A stays the same, infer a higher probability that A and B merge.", "refs": ["rd:P4", "rd:A10"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C5.p1", "statement": "A faces high constraint from B although A does not depend on B.", "strength": "strict"}]
     },
     "alternativeRoles": [{"readingLabel": "Reading 2: constraint as power imbalance against A",
       "commitments": [{"@id": "rd:C5.r2c1", "statement": "If A faces high constraint from B, then A depends on B more than B depends on A.", "refs": ["rd:C7"], "strength": "strict"}],
       "entitlements": [{"@id": "rd:C5.r2e1", "statement": "If A's dependence on B is much higher than B's dependence on A, one is entitled to assert high constraint from B.", "refs": ["rd:C1", "rd:C7"], "strength": "strict"}],
       "licenses": [{"@id": "rd:C5.r2l1", "statement": "If A faces high constraint from B, infer that A wants to absorb B; infer a higher merger probability only if mutual dependence is also high.", "refs": ["rd:C16", "rd:C6", "rd:P4"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C5.r2p1", "statement": "A faces high constraint from B while A and B depend on each other equally.", "strength": "strict"}]}]},
    {"@id": "rd:C6", "label": "Mutual dependence", "definition": "The extent to which two organizations depend on each other (B.6, B.9 'depend heavily on each other'). The text gives no rule for combining the two directed dependences (sum, mean, minimum).", "constructType": "relation", "level": "dyad",
     "measurementCommitments": [{"indicator": "uncommitted (aggregation rule not stated)", "unitOfAnalysis": "undirected dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C6.c1", "statement": "If A and B are highly mutually dependent, then each depends substantially on the other.", "refs": ["rd:C1"], "strength": "strict"}],
       "entitlements": [{"@id": "rd:C6.e1", "statement": "If A's dependence on B and B's dependence on A are both high, one is entitled to assert high mutual dependence.", "refs": ["rd:C1"], "strength": "strict"}],
       "licenses": [{"@id": "rd:C6.l1", "statement": "If mutual dependence is high, infer that absorption is feasible and attractive to both sides, so merger is more likely.", "refs": ["rd:C16", "rd:C17", "rd:P5"], "strength": "defeasible"},
                    {"@id": "rd:C6.l2", "statement": "If mutual dependence is high, infer that boundary-spanning ties between the two are more likely.", "refs": ["rd:P7"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C6.p1", "statement": "Mutual dependence is high while one party does not depend on the other.", "strength": "strict"},
                     {"@id": "rd:C6.p2", "statement": "Mutual dependence can be read off from power imbalance (low imbalance implies high mutual dependence). B.6-B.7 treat them as separate dimensions.", "refs": ["rd:C7"], "strength": "strict"}]
     }},
    {"@id": "rd:C7", "label": "Power imbalance", "definition": "Asymmetry between the two organizations' power over each other, with a weaker and a stronger side (B.7). Inferred: the difference between A's dependence on B and B's dependence on A.", "constructType": "relation", "level": "dyad",
     "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "directed dyad (which side is weaker)"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C7.c1", "statement": "If power between A and B is imbalanced in B's favor, then A depends on B more than B depends on A.", "refs": ["rd:A2"], "strength": "strict"}],
       "entitlements": [{"@id": "rd:C7.e1", "statement": "If the two directed dependences differ greatly, one is entitled to assert power imbalance, with the more dependent side as the weaker.", "refs": ["rd:C1"], "strength": "strict"}],
       "licenses": [{"@id": "rd:C7.l1", "statement": "If imbalance favors B, infer that A wants to absorb B but is less able to.", "refs": ["rd:C16", "rd:C17", "rd:R12", "rd:R13"], "strength": "defeasible"},
                    {"@id": "rd:C7.l2", "statement": "If imbalance rises and mutual dependence stays the same, infer a lower probability that the weaker side absorbs the stronger.", "refs": ["rd:P6"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C7.p1", "statement": "Power is highly imbalanced although each side depends on the other to the same degree.", "strength": "strict"}]
     }},
    {"@id": "rd:C8", "label": "Managerial goals: uncertainty reduction and autonomy", "definition": "Managers' aim to reduce uncertainty and preserve the organization's autonomy (B.4).", "constructType": "disposition", "level": "multi-level",
     "measurementCommitments": [{"indicator": "uncommitted (asserted of managers in general, not measured)", "unitOfAnalysis": "managers of the focal organization"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C8.c1", "statement": "If managers hold these goals, then, other things equal, they prefer arrangements that make resource flows more predictable and leave fewer decisions to outside actors.", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C8.e1", "statement": "If an organization is run by managers, one is entitled to attribute these goals to them; the text asks for no further evidence.", "refs": ["rd:A3"], "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C8.l1", "statement": "If an organization depends heavily on an external actor, infer that its managers will act to manage that dependence.", "refs": ["rd:R6", "rd:P3"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C8.p1", "statement": "Managers accept a large, lasting rise in outside control over their organization's critical resources without trying to offset it, when a tactic is available to them.", "strength": "defeasible"}]
     }},
    {"@id": "rd:C9", "label": "Uncertainty", "definition": "The uncertainty managers seek to reduce (B.4). The text does not define it. Inferred: uncertainty about whether, when and on what terms critical resources will arrive.", "constructType": "state", "level": "organization",
     "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "focal organization"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C9.c1", "statement": "If A faces high resource uncertainty, then A cannot reliably predict the supply or terms of a critical resource.", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C9.e1", "statement": "If A depends on an actor whose behavior A does not control, one is entitled to assert some uncertainty (inferred link; the text does not connect dependence and uncertainty).", "refs": ["rd:R5"], "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C9.l1", "statement": "If resource uncertainty is high, infer that managers are more motivated to adopt a tactic.", "refs": ["rd:C8", "rd:C11"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C9.p1", "statement": "A faces high uncertainty about a resource it fully controls internally.", "strength": "defeasible"}]
     }},
    {"@id": "rd:C10", "label": "Organizational autonomy", "definition": "The organization's freedom from control by external actors, which managers seek to preserve (B.4).", "constructType": "state", "level": "organization",
     "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "focal organization"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C10.c1", "statement": "If A is autonomous with respect to B, then A's decisions are not subject to B's demands.", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C10.e1", "statement": "If no external actor has substantial power over A, one is entitled to assert that A is autonomous.", "refs": ["rd:C4"], "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C10.l1", "statement": "If A's autonomy is threatened, infer that A's managers will act to restore it.", "refs": ["rd:C8", "rd:C11"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C10.p1", "statement": "A is fully autonomous although it depends heavily on a single powerful actor.", "refs": ["rd:C1", "rd:C4"], "strength": "strict"}]
     }},
    {"@id": "rd:C11", "label": "Dependence-management tactic", "definition": "An action by which an organization manages its dependence on a constraining actor. Kinds: absorption (rd:C12), co-optation (rd:C13), negotiated long-term arrangement (rd:C14), diversification (rd:C15) (B.4, B.5).", "constructType": "process", "level": "dyad",
     "measurementCommitments": [{"indicator": "occurrence of one of the four named kinds directed at a specific actor", "level": "nominal", "unitOfAnalysis": "dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C11.c1", "statement": "If an action is a dependence-management tactic, then it is directed at a specific actor on which the organization depends, or at the dependence itself.", "strength": "strict"}],
       "entitlements": [{"@id": "rd:C11.e1", "statement": "If A merges with, co-opts, contracts long-term with, or diversifies away from an actor on which A depends, one is entitled to class the action as a tactic. (Risk: if dependence is then inferred from the tactic, the entitlement is circular; see openQuestions.)", "refs": ["rd:C1"], "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C11.l1", "statement": "If A has adopted a tactic toward B, infer that A's dependence on B, or B's power over A, is lower than it would otherwise be.", "refs": ["rd:R7", "rd:A9"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C11.p1", "statement": "The choice of tactic is unrelated to the power each side holds.", "refs": ["rd:P4", "rd:P5", "rd:P6"], "strength": "strict"}]
     }},
    {"@id": "rd:C12", "label": "Absorption (merger or acquisition)", "definition": "Absorbing the constraining actor through merger or acquisition (B.5).", "constructType": "event", "level": "dyad",
     "measurementCommitments": [{"indicator": "a merger or acquisition between the two organizations (B.5, B.6)", "level": "nominal", "unitOfAnalysis": "dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C12.c1", "statement": "If A absorbs B, then B's resources come under A's ownership and the A-B dependence becomes internal to A.", "strength": "strict"}],
       "entitlements": [{"@id": "rd:C12.e1", "statement": "If a merger or acquisition between A and B is completed, one is entitled to assert absorption.", "strength": "strict"}],
       "licenses": [{"@id": "rd:C12.l1", "statement": "If A has absorbed B, infer that A's boundary now includes B's activities and that B no longer has external power over A.", "refs": ["rd:R16", "rd:C18"], "strength": "strict"}],
       "precludes": [{"@id": "rd:C12.p1", "statement": "A has absorbed B, yet B remains an independent actor able to withhold the resource from A.", "strength": "strict"}]
     }},
    {"@id": "rd:C13", "label": "Co-optation", "definition": "Co-opting the constraining actor through interlocking directorates or joint ventures (B.5).", "constructType": "process", "level": "dyad",
     "measurementCommitments": [{"indicator": "a shared director (interlock) or a joint venture between the two organizations (B.5)", "level": "nominal", "unitOfAnalysis": "dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C13.c1", "statement": "If A co-opts B, then B is brought into A's governance or a jointly governed venture, without A taking ownership of B.", "strength": "strict"}],
       "entitlements": [{"@id": "rd:C13.e1", "statement": "If A and B share a director or form a joint venture, one is entitled to assert co-optation (subject to the circularity caution at rd:C11.e1).", "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C13.l1", "statement": "If A has co-opted B, infer that B is less likely to use its power against A.", "refs": ["rd:C4"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C13.p1", "statement": "Co-optation transfers full ownership of B to A (that would be absorption).", "refs": ["rd:C12"], "strength": "strict"}]
     }},
    {"@id": "rd:C14", "label": "Negotiated long-term arrangement", "definition": "Long-term arrangements negotiated with the constraining actor (B.5).", "constructType": "process", "level": "dyad",
     "measurementCommitments": [{"indicator": "a long-term agreement between the two organizations; the duration threshold is uncommitted", "level": "nominal", "unitOfAnalysis": "dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C14.c1", "statement": "If A and B have a negotiated long-term arrangement, then the terms of their exchange are fixed in advance for an extended period.", "strength": "strict"}],
       "entitlements": [{"@id": "rd:C14.e1", "statement": "If A and B have signed a multi-year supply or purchase agreement, one is entitled to assert this tactic.", "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C14.l1", "statement": "If A has such an arrangement with B, infer that A's uncertainty about the resource's supply and terms is lower for the agreement's term.", "refs": ["rd:C9"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C14.p1", "statement": "The arrangement leaves the terms of future exchange wholly open.", "strength": "strict"}]
     }},
    {"@id": "rd:C15", "label": "Diversification away from the constraining actor", "definition": "Diversifying away from the constraining actor (B.5).", "constructType": "process", "level": "organization",
     "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "focal organization"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C15.c1", "statement": "If A diversifies away from B, then A reduces how much of its operations need B's resource, or adds other sources or buyers.", "strength": "strict"}],
       "entitlements": [{"@id": "rd:C15.e1", "statement": "If A enters activities or develops sources that lower the importance of B's resource or add alternatives to B, one is entitled to assert diversification away from B.", "refs": ["rd:C2", "rd:C3"], "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C15.l1", "statement": "If A has diversified away from B, infer that A's dependence on B is lower.", "refs": ["rd:C1", "rd:P1"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C15.p1", "statement": "A diversifies away from B while making more of its operations need B's resource.", "strength": "strict"}]
     }},
    {"@id": "rd:C16", "label": "Motivation to absorb", "definition": "One side's wanting to absorb the other: present for both sides under mutual dependence (B.6, 'attractive to both sides') and for the weaker side under imbalance (B.7).", "constructType": "disposition", "level": "organization",
     "measurementCommitments": [{"indicator": "uncommitted (not directly observed in the text; inferred from structural position)", "unitOfAnalysis": "organization within a dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C16.c1", "statement": "If A is motivated to absorb B, then A's managers prefer owning B to the current arrangement.", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C16.e1", "statement": "If A is the weaker side of an imbalanced dyad, or A and B are highly mutually dependent, one is entitled to assert A's motivation to absorb B.", "refs": ["rd:R11", "rd:R12"], "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C16.l1", "statement": "If A is motivated to absorb B and absorption is feasible, infer a high probability that A absorbs B.", "refs": ["rd:C17", "rd:R14"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C16.p1", "statement": "Within this theory: A is motivated to absorb B although A does not depend on B (other motives are outside the theory, not ruled out in the world).", "strength": "defeasible"}]
     }},
    {"@id": "rd:C17", "label": "Feasibility of absorption", "definition": "Whether one side is able to absorb the other: raised by mutual dependence (B.6) and lowered for the weaker side by imbalance (B.7).", "constructType": "attribute", "level": "dyad",
     "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "dyad"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C17.c1", "statement": "If A's absorption of B is feasible, then A has the means and B's owners can be brought to accept the deal.", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C17.e1", "statement": "If A and B are highly mutually dependent, one is entitled to assert that absorption is feasible; if A is the much weaker side, that entitlement weakens.", "refs": ["rd:R10", "rd:R13"], "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C17.l1", "statement": "If absorption is infeasible, infer that it is unlikely even when motivation is high.", "refs": ["rd:R15"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C17.p1", "statement": "Absorption is feasible although the target is much stronger and has no interest in being absorbed.", "strength": "defeasible"}]
     }},
    {"@id": "rd:C18", "label": "Organizational boundary", "definition": "The line between what lies inside the organization and what lies outside it; boundaries 'reflect the political management of external dependencies' (B.8). Inferred: the set of activities and resources under the organization's ownership or administrative control.", "constructType": "attribute", "level": "organization",
     "measurementCommitments": [{"indicator": "uncommitted (B.9 implies observing boundary shifts over time)", "method": "longitudinal observation implied by B.9", "unitOfAnalysis": "organization"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C18.c1", "statement": "If an activity lies within A's boundary, then A owns it or controls it administratively.", "strength": "defeasible"}],
       "entitlements": [{"@id": "rd:C18.e1", "statement": "If A owns or administratively controls an activity, one is entitled to place it inside A's boundary.", "strength": "defeasible"}],
       "licenses": [{"@id": "rd:C18.l1", "statement": "If A's boundary has shifted, infer a prior change in A's dependence structure or in the power positions in its dyads (an abductive inference).", "refs": ["rd:C19", "rd:P8", "rd:P9"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C18.p1", "statement": "A's boundary is set by minimizing the sum of production and governance costs.", "refs": ["rd:A4", "rd:P9"], "strength": "strict"}]
     }},
    {"@id": "rd:C19", "label": "Structure of resource dependencies", "definition": "The pattern of dependence relations between the organization and the actors in its environment (B.9).", "constructType": "relation", "level": "field",
     "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "focal organization's set of dyads (ego network)"}],
     "inferentialRole": {
       "commitments": [{"@id": "rd:C19.c1", "statement": "If an organization's dependence structure is specified, then for each relevant partner the direction and strength of dependence are fixed.", "refs": ["rd:C1", "rd:S2"], "strength": "strict"}],
       "entitlements": [{"@id": "rd:C19.e1", "statement": "If one has the directed dependence of the organization on each supplier and buyer, and theirs on it, one is entitled to assert its dependence structure.", "refs": ["rd:C1"], "strength": "strict"}],
       "licenses": [{"@id": "rd:C19.l1", "statement": "If the dependence structure changes (a resource becomes more important, a new source enters), infer that the organization's boundary will change afterwards.", "refs": ["rd:P8"], "strength": "defeasible"}],
       "precludes": [{"@id": "rd:C19.p1", "statement": "Boundaries stay unchanged through a large, lasting shift in the dependence structure, with scope condition rd:S4 met.", "refs": ["rd:P8"], "strength": "defeasible"}]
     }}
  ],
  "relations": [
    {"@id": "rd:R1", "from": "rd:C2", "to": "rd:C1", "form": "constitutive", "sign": "positive", "scope": ["rd:S2"]},
    {"@id": "rd:R2", "from": "rd:C3", "to": "rd:C1", "form": "constitutive", "sign": "negative", "scope": ["rd:S2"]},
    {"@id": "rd:R3", "from": "rd:C1", "to": "rd:C4", "form": "constitutive", "sign": "positive"},
    {"@id": "rd:R4", "from": "rd:C4", "to": "rd:C10", "form": "causal", "sign": "negative"},
    {"@id": "rd:R5", "from": "rd:C1", "to": "rd:C9", "form": "causal", "sign": "positive"},
    {"@id": "rd:R6", "from": "rd:C8", "to": "rd:C11", "form": "teleological", "sign": "conditional", "moderators": ["rd:C1", "rd:C4"], "scope": ["rd:S3"]},
    {"@id": "rd:R7", "from": "rd:C11", "to": "rd:C1", "form": "teleological", "sign": "negative"},
    {"@id": "rd:R8", "from": "rd:C11", "to": "rd:C10", "form": "teleological", "sign": "positive"},
    {"@id": "rd:R9", "from": "rd:C5", "to": "rd:C12", "form": "causal", "sign": "positive", "moderators": ["rd:C6"], "scope": ["rd:S4"]},
    {"@id": "rd:R10", "from": "rd:C6", "to": "rd:C17", "form": "causal", "sign": "positive"},
    {"@id": "rd:R11", "from": "rd:C6", "to": "rd:C16", "form": "causal", "sign": "positive"},
    {"@id": "rd:R12", "from": "rd:C7", "to": "rd:C16", "form": "causal", "sign": "positive"},
    {"@id": "rd:R13", "from": "rd:C7", "to": "rd:C17", "form": "causal", "sign": "negative"},
    {"@id": "rd:R14", "from": "rd:C16", "to": "rd:C12", "form": "causal", "sign": "conditional", "moderators": ["rd:C17"], "scope": ["rd:S4"]},
    {"@id": "rd:R15", "from": "rd:C17", "to": "rd:C12", "form": "causal", "sign": "conditional", "moderators": ["rd:C16"], "scope": ["rd:S4"]},
    {"@id": "rd:R16", "from": "rd:C12", "to": "rd:C18", "form": "constitutive", "sign": "positive"},
    {"@id": "rd:R17", "from": "rd:C19", "to": "rd:C18", "form": "causal", "sign": "unspecified", "scope": ["rd:S3", "rd:S4"]},
    {"@id": "rd:R18", "from": "rd:C19", "to": "rd:C1", "form": "constitutive", "sign": "unspecified"}
  ],
  "mechanisms": [
    {"@id": "rd:M1", "label": "Dependence confers power and threatens autonomy", "steps": ["rd:R1", "rd:R2", "rd:R3", "rd:R4", "rd:R5"], "mechanismType": "political"},
    {"@id": "rd:M2", "label": "Absorption under mutual dependence", "steps": ["rd:R10", "rd:R11", "rd:R14", "rd:R15", "rd:R16"], "mechanismType": "strategic"},
    {"@id": "rd:M3", "label": "Absorption blocked by power imbalance", "steps": ["rd:R12", "rd:R13", "rd:R14", "rd:R15"], "mechanismType": "political"},
    {"@id": "rd:M4", "label": "Boundary adjustment to a change in dependence structure", "steps": ["rd:R18", "rd:R3", "rd:R4", "rd:R6", "rd:R8", "rd:R16"], "mechanismType": "political"}
  ],
  "assumptions": [
    {"@id": "rd:A1", "statement": "Organizations are not self-sufficient: they need critical resources that other actors in their environment control.", "status": "core", "explicitness": "explicit", "supports": ["rd:C1", "rd:P3"]},
    {"@id": "rd:A2", "statement": "An organization's dependence on another actor is the source of that actor's power over it; in Reading 1, B's power over A is A's dependence on B (power-dependence identity).", "status": "core", "explicitness": "explicit", "supports": ["rd:P2", "rd:P4", "rd:P5", "rd:P6"]},
    {"@id": "rd:A3", "statement": "Organizations are run by managers who seek to reduce uncertainty and preserve autonomy, and who therefore act to manage dependence.", "status": "core", "explicitness": "explicit", "supports": ["rd:P3", "rd:P8"]},
    {"@id": "rd:A4", "statement": "Organizational boundaries are set by the political management of external dependencies, not by cost minimization.", "status": "core", "explicitness": "explicit", "supports": ["rd:P9"]},
    {"@id": "rd:A5", "statement": "Dependence increases with the resource's importance and decreases with the availability of alternative sources; no other determinants are named.", "status": "auxiliary", "explicitness": "explicit", "supports": ["rd:P1"]},
    {"@id": "rd:A6", "statement": "Mutual dependence makes absorption both feasible and attractive to both sides.", "status": "auxiliary", "explicitness": "explicit", "supports": ["rd:P5", "rd:P7"]},
    {"@id": "rd:A7", "statement": "Under power imbalance, the weaker side wants to absorb the stronger but is less able to.", "status": "auxiliary", "explicitness": "explicit", "supports": ["rd:P6"]},
    {"@id": "rd:A8", "statement": "Managers have the discretion and means to choose among tactics and carry them out; boundaries change through managerial action, not only through the selection of organizations.", "status": "auxiliary", "explicitness": "implicit", "surfacedBy": "Explicator (Deconstructor-INTRA)", "supports": ["rd:P3", "rd:P8"]},
    {"@id": "rd:A9", "statement": "The tactics do reduce the dependence or uncertainty they target, or managers believe they do.", "status": "auxiliary", "explicitness": "implicit", "surfacedBy": "Explicator (Deconstructor-INTRA)", "supports": ["rd:P3", "rd:P9"]},
    {"@id": "rd:A10", "statement": "The positive effect of mutual dependence on absorption is larger in magnitude than the negative effect of power imbalance. So when A's dependence on B rises with B's dependence on A unchanged (which raises both mutual dependence and imbalance), the probability of merger rises.", "status": "auxiliary", "explicitness": "surfaced", "surfacedBy": "Explicator (Deconstructor-INTRA), reconciling B.6 with B.7 under Reading 1", "supports": ["rd:P4"]}
  ],
  "propositions": [
    {"@id": "rd:P1", "statement": "A's dependence on B increases with the importance of B's resource to A's operations and decreases with the number of alternative sources available to A.", "claimType": "definition", "factStatus": "undetermined", "observables": ["resource importance", "number of alternative suppliers or buyers"]},
    {"@id": "rd:P2", "statement": "The more A depends on B, the more power B has over A (Reading 1: by definition).", "claimType": "definition", "factStatus": "undetermined", "observables": []},
    {"@id": "rd:P3", "statement": "Organizations that depend heavily on an external actor manage that dependence by absorbing, co-opting, negotiating long-term arrangements with, or diversifying away from that actor.", "claimType": "explanation", "factStatus": "accommodation", "observables": ["mergers and acquisitions", "interlocking directorates", "joint ventures", "long-term contracts", "diversification moves"]},
    {"@id": "rd:P4", "statement": "Holding B's dependence on A constant, the probability that A and B merge increases with A's dependence on (constraint from) B.", "claimType": "prediction", "factStatus": "undetermined", "observables": ["dyadic merger or acquisition events", "directed dependence in each direction"]},
    {"@id": "rd:P5", "statement": "Holding power imbalance constant, the probability that A and B merge increases with their mutual dependence.", "claimType": "prediction", "factStatus": "undetermined", "observables": ["dyadic merger or acquisition events", "mutual dependence"],
     "rivalDivergence": [{"rival": "tce:reading1", "contrary": "Integration probability rises with asset specificity, not with mutual dependence as such; mutual dependence without specific investment gives no prediction (comparison inferred, to be checked by the Integrator)."}]},
    {"@id": "rd:P6", "statement": "Holding mutual dependence constant, the probability that the weaker side absorbs the stronger decreases as power imbalance rises.", "claimType": "prediction", "factStatus": "undetermined", "observables": ["dyadic merger or acquisition events", "power imbalance", "identity of the acquirer"]},
    {"@id": "rd:P7", "statement": "Mergers and other boundary-spanning ties (interlocks, joint ventures, long-term arrangements) occur more often between organizations that depend heavily on each other.", "claimType": "prediction", "factStatus": "undetermined", "observables": ["incidence of boundary-spanning ties across dyads", "mutual dependence"]},
    {"@id": "rd:P8", "statement": "When the structure of an organization's resource dependencies shifts, its boundaries shift afterwards.", "claimType": "prediction", "factStatus": "novel", "observables": ["timing of changes in dependence structure", "timing of later boundary changes"]},
    {"@id": "rd:P9", "statement": "Organizational boundaries are explained by the political management of external dependencies and not by cost minimization.", "claimType": "explanation", "factStatus": "undetermined", "observables": ["boundary changes that reduce dependence without reducing cost, or that raise cost"],
     "rivalDivergence": [{"rival": "tce:reading1", "contrary": "Boundaries are set by economizing on production and transaction costs; a boundary change that raises total cost should be selected against (Input A)."}]}
  ],
  "derivations": [
    {"@id": "rd:D1", "target": "rd:P9", "premises": ["rd:A1", "rd:A2", "rd:A3"], "method": "verbal", "status": "asserted", "auxiliariesRequired": ["rd:A4"], "notes": "B.8 presents P9 with 'therefore' as following from B.1-B.7. A1-A3 seem to show only that boundaries are used to manage dependence. They do not exclude cost minimization as a joint or dominant determinant. The 'rather than' clause seems to need A4 as a premise, which makes the step close to restating A4. Left asserted; flagged for the Argument Auditor."},
    {"@id": "rd:D2", "target": "rd:P4", "premises": ["rd:A2", "rd:A6", "rd:A7"], "method": "verbal", "status": "asserted", "auxiliariesRequired": ["rd:A10"], "notes": "If mutual dependence and imbalance are the sum and difference of the two directed dependences, a unilateral rise in A's dependence on B raises both. A6 pushes merger probability up and A7 pushes it down. P4 seems to follow only if A10 holds. Under other aggregation rules the result may differ. Not checked."},
    {"@id": "rd:D3", "target": "rd:P5", "premises": ["rd:A2", "rd:A6"], "method": "verbal", "status": "asserted", "auxiliariesRequired": [], "notes": "B.6 'because' gives A6 as the warrant. P5 seems to follow from A6, with R14 and R15 read as jointly sufficient for absorption. Not checked."}
  ],
  "openQuestions": [
    "B.6 'constraint' is undefined. Is it A's unilateral dependence on B (Reading 1) or power imbalance against A (Reading 2)? See pivot D-2.",
    "Under a sum/difference aggregation, A's dependence on B, B's dependence on A, mutual dependence and imbalance are linearly related (two degrees of freedom, four names). So 'constraint', 'mutual dependence' and 'imbalance' cannot all have independent effects. Which two does the theorist treat as primitive?",
    "The text gives no aggregation rule for mutual dependence (sum, mean, minimum, product). The sign in rd:P4 can depend on this choice (rd:D2).",
    "B.7 says the weaker side is 'less able', not 'less likely', to absorb. Reading 1's net-negative rd:P6 is an inference from 'by contrast'.",
    "B.6 says the choice of tactic depends on power, but only absorption is tied to power positions. When does the theory predict co-optation, negotiation or diversification instead of absorption?",
    "Is the actor in B.4 the manager (individual interests, which may diverge from owners') or the organization? This matters for whether dependence-reducing but value-destroying mergers are predicted.",
    "Circularity risk (rd:C11.e1, rd:C13.e1): if dependence is inferred from observed ties, rd:P7 becomes tautological. An independent indicator of dependence is needed. Candidates used in this literature (e.g., inter-industry transaction shares from input-output tables) are for the Data Specifier to check; the text commits to none.",
    "rd:C3 (few alternative sources) overlaps with the small-numbers condition that asset specificity creates in Input A. A test separating rd:P9 from the transaction-cost rival must vary dependence while holding asset specificity fixed, or the reverse. Is that possible?",
    "Fact status: P8 is marked novel on internal grounds (it commits to a temporal ordering the cross-sectional claims do not). Whether P5 and P7 were predicted before or fitted to known merger patterns is a historical question the text does not settle (to verify against Pfeffer & Salancik 1978 and Casciaro & Piskorski 2005)."
  ],
  "provenance": {"createdBy": "Foundry Explicator (Role 1), instruction set v0.1", "ledgerEvents": []}
}
```

---

## 3. Reasons for classifications (steps 4 and 5)

### 3.1 Assumption partition (Reading 1)

| Id | Status | Explicitness | Reason for classification |
|---|---|---|---|
| rd:A1 | core | explicit (B.1, B.2) | This is the programme's starting point. A theory without external dependence has nothing to explain. |
| rd:A2 | core | explicit (B.2) | Every prediction about tactic choice (B.6, B.7) runs through power. Without it, "how much power each side holds" has no content. Whether the link is identity or causation is underdetermined (pivot D-1); that it holds is core in every reading. |
| rd:A3 | core | explicit (B.4) | This is the motivational premise that turns dependence into action. Without it, the theory would describe dependence but not predict tactics. |
| rd:A4 | core (Reading 1) / auxiliary (Reading 3) | explicit (B.8) | In Reading 1 the "rather than" clause defines the programme against its rival, which makes it a negative heuristic. In Reading 3 it is a claim about relative explanatory weight that could be relaxed to absorb cost-related anomalies (pivot D-3). |
| rd:A5 | auxiliary | explicit (B.3) | This specifies how dependence is determined. Other determinants (for example, discretion over the resource's allocation) could be added without abandoning A1 or A2. |
| rd:A6 | auxiliary | explicit (B.6) | This is a specific claim about when absorption is feasible and attractive. It can be revised (for example, made conditional on regulatory context) and the core survives. |
| rd:A7 | auxiliary | explicit (B.7) | Same reason as A6. It refines how power positions translate into tactics. |
| rd:A8 | auxiliary | implicit | B.4 to B.6 presuppose managerial discretion. The concentration prediction (P7) could survive a reading in which ties result from selection rather than choice, so giving up A8 changes the mechanism but does not abandon the programme. **Uncertain:** a theorist who treats managerial agency as constitutive of the theory would class it as core. |
| rd:A9 | auxiliary | implicit | Teleological explanation needs only that managers *believe* tactics work. Whether tactics actually work can be adjusted. |
| rd:A10 | auxiliary | surfaced | This is needed only to reconcile B.6 with B.7 under Reading 1 (rd:D2). It concerns magnitudes, which belong to the protective belt. |

Counts. Reading 1: 4 core, 6 auxiliary. Reading 2: 4 core, 5 auxiliary (A10 not needed). Reading 3: 3 core, 7 auxiliary (A4 moves to auxiliary).

### 3.2 Fact status of propositions

| Id | Status | Reason |
|---|---|---|
| rd:P1 | undetermined | It acts as a rule for measuring dependence (claimType definition), not as an empirical claim. Novelty does not apply. |
| rd:P2 | undetermined | Definitional in Readings 1 and 2. In Reading 3 it becomes testable, but nothing in the text says whether it was predicted or fitted. |
| rd:P3 | accommodation | B.5 presents the four tactics as a list ("They may ..."), with no derivation of why these four and not others. On its face, the list catalogues known practices. (Inferred from the form of the sentence.) |
| rd:P4 | undetermined | This is a directional prediction. The text gives no basis for judging whether it was formed before the facts it covers. |
| rd:P5 | undetermined | Separating mutual dependence from imbalance is a refinement. It counts as novel if it was put forward before the data that tested it, and as an accommodation if it was introduced to absorb inconsistent earlier findings. The text does not say which (to verify, Casciaro & Piskorski 2005). |
| rd:P6 | undetermined | Same as P5. In addition, the net sign is inferred (see openQuestions). |
| rd:P7 | undetermined | Industry-level merger patterns were part of the early evidence for this programme (to verify, Pfeffer & Salancik 1978 and earlier work by Pfeffer). If the proposition was built from those patterns, it is an accommodation. The text does not settle this. |
| rd:P8 | novel (tentative) | It commits to a temporal ordering (dependence change, then boundary change) that is not needed to fit any cross-sectional pattern in B.9's first clause. This is a judgment on internal grounds only, not on the theory's history. |
| rd:P9 | undetermined | This is an explanatory contrast with a rival, not a prediction. Its testable content depends on pivot D-3. |

---

## 4. Output (b): Further readings (fields that differ from Reading 1)

### Reading 2 ("constraint-as-imbalance reading")

This reading takes "constraint" in B.6 as the partner's power advantage over the focal organization. B.6 then says that high imbalance against A raises merger probability, and B.7 says imbalance leaves the weaker side less able to absorb. The two statements conflict head-on unless the B.6 effect holds only where mutual dependence is high ("and especially where ..."). This reading resolves the conflict with an interaction term, and it does not need A10.

```json
{
  "@id": "rd:reading2",
  "readingOf": "rd:ensemble",
  "label": "Resource-dependence theory of organizational boundaries, Reading 2 (constraint-as-imbalance reading)",
  "constructs": [{"@id": "rd:C5", "definition": "The partner's power advantage over the focal organization: power imbalance in B's favor (B.6 read with B.7).", "inferentialRole": "replaced by the 'Reading 2' alternativeRole of rd:C5 in Reading 1"}],
  "relations": [
    {"@id": "rd:R9", "from": "rd:C5", "to": "rd:C12", "form": "causal", "sign": "conditional", "moderators": ["rd:C6"], "scope": ["rd:S4"]},
    {"@id": "rd:R19", "from": "rd:C5", "to": "rd:C16", "form": "causal", "sign": "positive"}
  ],
  "assumptions": [{"@id": "rd:A10", "removed": true}],
  "propositions": [
    {"@id": "rd:P4", "statement": "Constraint (imbalance in B's favor) raises the probability that A and B merge only where their mutual dependence is high; where mutual dependence is low, constraint has no positive effect on merger.", "claimType": "prediction", "factStatus": "undetermined"},
    {"@id": "rd:P6", "statement": "Power imbalance raises the weaker side's motivation to absorb the stronger and lowers its ability to. Its net effect on absorption is conditional on mutual dependence, and the text does not fix its sign.", "claimType": "prediction", "factStatus": "undetermined"},
    {"@id": "rd:P10", "statement": "[Surfaced, not in text] Where A faces high constraint from B and mutual dependence is low, A turns to co-optation, negotiated arrangements or diversification rather than absorption.", "claimType": "prediction", "factStatus": "undetermined"}
  ],
  "derivations": [{"@id": "rd:D2", "target": "rd:P4", "premises": ["rd:A2", "rd:A6", "rd:A7"], "method": "verbal", "status": "asserted", "auxiliariesRequired": [], "notes": "P4 in this reading seems to follow from A6 and A7 once the interaction is written in. A10 is not needed. P10 is needed for B.6's 'which tactic is chosen' to say anything about tactics other than merger."}]
}
```

### Reading 3 ("complementary reading")

This reading treats B.2's "source" as causal: dependence produces power but does not exhaust it. It also treats B.8's "rather than the minimization of costs" as a claim of explanatory emphasis that belongs to the protective belt, not as a hard-core exclusion. On this reading the theory accounts for boundary variation that cost minimization leaves unexplained. It does not deny cost minimization.

```json
{
  "@id": "rd:reading3",
  "readingOf": "rd:ensemble",
  "label": "Resource-dependence theory of organizational boundaries, Reading 3 (complementary reading)",
  "stanceProfile": {"justificationStrategies": ["assimilative"], "evidence": "B.8 'rather than' read as a contrast of emphasis: the account adds political management of dependence to, but does not replace, cost-based explanation."},
  "constructs": [{"@id": "rd:C4", "inferentialRole": "replaced by the 'Reading 3' alternativeRole of rd:C4 in Reading 1", "measurementCommitments": [{"indicator": "uncommitted (needs an indicator independent of rd:C1)", "unitOfAnalysis": "directed dyad"}]}],
  "relations": [{"@id": "rd:R3", "from": "rd:C1", "to": "rd:C4", "form": "causal", "sign": "positive"}],
  "assumptions": [
    {"@id": "rd:A2", "statement": "An organization's dependence on another actor is the principal source of that actor's power over it; power may also have other sources and need not be exercised.", "status": "core", "explicitness": "explicit"},
    {"@id": "rd:A4", "statement": "Political management of external dependencies is a major determinant of organizational boundaries, alongside cost considerations.", "status": "auxiliary", "explicitness": "explicit"}
  ],
  "propositions": [
    {"@id": "rd:P2", "statement": "The more A depends on B, the more power B has over A.", "claimType": "prediction", "factStatus": "undetermined"},
    {"@id": "rd:P9", "statement": "Holding cost-relevant transaction attributes constant, the dependence structure explains additional variation in organizational boundaries.", "claimType": "prediction", "factStatus": "undetermined",
     "rivalDivergence": [{"rival": "tce:reading1", "contrary": "Once asset specificity, uncertainty and frequency are controlled for, dependence adds no explanatory power (inferred rival position)."}]}
  ],
  "derivations": [{"@id": "rd:D1", "target": "rd:P9", "premises": ["rd:A1", "rd:A2", "rd:A3", "rd:A8", "rd:A9"], "method": "verbal", "status": "asserted", "auxiliariesRequired": [], "notes": "The weaker, incremental P9 seems to follow from managerial action on dependence (A3, A8, A9) without A4 as a premise. Not checked."}],
  "openQuestions": ["Reading 3: with power partly independent of dependence, what is the independent indicator of power (rd:C4)?"]
}
```

### Ensemble

```json
{
  "@id": "rd:ensemble",
  "@type": "FormalizationEnsemble",
  "members": ["rd:reading1", "rd:reading2", "rd:reading3"],
  "pivotalDifferences": [
    "D-1: B.2 'source': power constituted by dependence (Readings 1, 2) vs caused by it (Reading 3). Changes rd:R3, rd:P2, rd:C4.",
    "D-2: B.6 'constraint': A's unilateral dependence on B (Readings 1, 3) vs imbalance in B's favor (Reading 2). Changes rd:R9, rd:P4, rd:P6, rd:A10, adds rd:P10.",
    "D-3: B.8 'rather than the minimization of costs': hard-core exclusion (Readings 1, 2) vs protective-belt emphasis (Reading 3). Changes rd:A4 status, rd:P9, justification strategy, rd:D1."
  ]
}
```

`dispersion` is left unset. The appendix defines it as mean pairwise inferential distance, which needs the Integrator's alignment of the members. As a rough proxy only: across the 10 proposition ids in the union (P1 to P10), 5 differ in statement, claim type or presence in at least one reading (P2, P4, P6, P9, P10), a share of 0.5.

The three pivots are logically independent, so 2 x 2 x 2 = 8 readings are possible. The three shown here change one cluster at a time against Reading 1, except Reading 3, which bundles D-1 with D-3. They are bundled only to keep the ensemble small; they do not depend on each other.

---

## 5. Output (c): Pivotal differences

| Pivot | Text | Reading 1 | Reading 2 | Reading 3 | Downstream propositions that change |
|---|---|---|---|---|---|
| **D-2 Meaning of "constraint"** (the pivot with the most consequences) | B.6 "faces high constraint from a partner", read with B.7 | A's unilateral dependence on B. P4 is a total effect that holds only if mutual dependence outweighs imbalance (surfaced A10) | Power imbalance against A. P4 holds only when mutual dependence is high (interaction). P6's sign is left open. P10 is surfaced | as Reading 1 | rd:P4 (unconditional vs interaction), rd:P6 (net negative vs undetermined sign), rd:A10 (needed vs not), rd:P10 (absent vs present), rd:R9 sign |
| **D-3 Status of the cost-minimization contrast** | B.8 "rather than the minimization of costs" | core (eliminative); P9 excludes cost-based explanation | core | auxiliary (assimilative); P9 becomes an incremental-variance prediction | rd:P9 (exclusion vs incremental), rd:D1 (needs A4 vs does not), stance justification strategy. Decides whether the Integrator should treat this theory's relation to Input A as rivalry or complementarity |
| **D-1 Power and dependence** | B.2 "that dependence is the source of other actors' power" | constitutive identity (power = dependence) | constitutive | causal (power has other sources and need not be exercised) | rd:P2 (definition vs testable prediction), rd:C4 entitlements, rd:R3 form. In Reading 3, rd:P4 to rd:P6 need a separate indicator of power |

---

## 6. Output (d): Decisions for the theorist

1. **D-2: What does "constraint" mean in B.6?** Choose unilateral dependence (Reading 1, which then needs surfaced assumption rd:A10) or power imbalance against the focal organization (Reading 2, which makes rd:P4 an interaction and leaves rd:P6's sign open). Or supply a third definition.
2. **Which two dyadic quantities are primitive?** A's dependence on B, B's dependence on A, mutual dependence and imbalance are not independent. Also state the aggregation rule for mutual dependence (sum, mean or minimum).
3. **D-3: Is "rather than the minimization of costs" hard core or protective belt?** This choice determines whether the Integrator approaches Input A as a rival (Readings 1, 2) or a complement (Reading 3).
4. **D-1: Is power identical to dependence, or caused by it?** If caused, name an indicator of power that does not use dependence.
5. **rd:A8 (managerial discretion):** accept it as auxiliary, or reclassify it as core.
6. **Tactic choice beyond merger:** adopt, reject or amend the surfaced proposition rd:P10, which says when non-absorption tactics are predicted.
7. **Measurement:** the text commits to no indicator of dependence (rd:C1). Choose one that is independent of the observed ties, to avoid the circularity flagged at rd:C11.e1.
8. **Whether to send rd:D1** (the "therefore" in B.8) to the Argument Auditor as a possible case of deductive language covering an abductive inference.
