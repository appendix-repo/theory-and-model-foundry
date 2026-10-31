# Run 01: Explicator on Input A (transaction-cost theory)
*Instruction set: Foundry v0.1, Role 1. Input: case_inputs.md, Input A. Single run, unedited.*

---

## 0. Segmentation (step 1)

The input has eleven sentences. Sentence 5 joins two independent clauses, so it is split into s5a and s5b. Every sentence does at least one of the five things step 1 lists, so none was left out.

| Seg. | Text (abridged) | Function | Nodes produced |
|---|---|---|---|
| s1 | "Firms exist because some transactions are more cheaply governed inside a hierarchy than across a market." | explanation; introduces constructs | tce:C17, tce:C1, tce:C12, tce:C10, tce:C15; tce:P1; tce:A4 |
| s2 | "Transactions differ along three dimensions: ... specificity ..., uncertainty ..., frequency ..." | introduces constructs | tce:C1, tce:C2, tce:C3, tce:C4; tce:A3 |
| s3 | "Asset specificity is the decisive dimension." | assumption (weighting) | tce:A5 |
| s4 | "When one party invests in assets whose value is much higher inside this relationship than in their next-best use ... exposed to opportunistic renegotiation once the investment is sunk." | defines construct; posits mechanism; scope | tce:C2, tce:C8; tce:R2; tce:A9; tce:S1 |
| s5a | "Because contracting parties are boundedly rational, they cannot write complete contracts ..." | assumption + relation | tce:C5, tce:C7; tce:A1; tce:R1 |
| s5b | "... because some of them are opportunistic, gaps in contracts will be exploited." | assumption + relation | tce:C6; tce:A2; tce:R3 |
| s6 | "Markets therefore become hazardous as asset specificity rises." | relation (presented as derived) | tce:R4; tce:P2 |
| s7 | "Hierarchy, meaning common ownership with authority and administrative control, suppresses opportunism and permits adaptation by fiat, but it carries bureaucratic costs and weakens high-powered incentives." | defines construct; relations | tce:C12, tce:C13, tce:C14; tce:R5, tce:R6, tce:R7; tce:A6, tce:A7 |
| s8 | "Hybrids such as long-term contracts and alliances fall between the two." | introduces construct; ordering | tce:C11; tce:A8 |
| s9 | "It follows that transactions are aligned with governance structures in a discriminating way: low ... market, intermediate ... hybrids, high ... hierarchy." | prediction (derivation asserted in prose) | tce:C9, tce:C16; tce:R9, tce:R10; tce:P3 |
| s10 | "Firms that misalign transactions and governance will incur higher costs and, over time, will be selected out by competition." | mechanism (selection) + prediction | tce:C16, tce:C18; tce:R11, tce:R12; tce:P4; tce:A12; tce:S2 |
| s11 | "Empirically, we should observe that the probability of vertical integration increases with asset specificity, and more steeply when uncertainty is high." | prediction | tce:C19; tce:R13; tce:P5, tce:P6 |

Convention used throughout: each inference ends with its basis. "(s4)" means the text states it in that segment. "(inferred)" means I inferred it and the text does not state it. "(surfaced)" means it is an implicit premise that the argument needs.

---

## (a) Reading 1: JSON-LD theory object

Reading 1, labelled **"economizing choice"**, takes the alignment in s9 to be produced by parties choosing governance to minimize governance cost. On this reading the competitive selection in s10 is a backstop. Uncertainty acts only as a moderator of asset specificity, and asset specificity is in the hard core.

```json
{
  "@context": ["../schema/context.v0.jsonld", {"tce": "https://foundry.lakatos.example/theory/tce#"}],
  "@id": "tce:reading-1",
  "@type": "TheoryObject",
  "schemaVersion": "0.1-draft",
  "label": "Transaction-cost theory of firm boundaries, reading 1 (economizing choice)",
  "tradition": "transaction-cost economics",
  "readingOf": "tce:ensemble-1",
  "sources": [{"citation": "case_inputs.md, Input A: paraphrase after Williamson 1975, 1985, 1991", "span": "s1-s11"}],
  "stanceProfile": {
    "epistemologicalStance": "positivism-lay",
    "corroborationLogic": "falsificationism-methodological",
    "ontologicalCommitments": ["transactions (C1) as the basic unit", "governance structures as discrete alternatives (C9-C12)", "boundedly rational agents (C5)", "opportunistic agents, at least some (C6)", "relationship-specific assets (C2)", "firms (C17)", "a competitive environment that selects (C18)"],
    "modelClasses": ["causal", "functional", "teleological"],
    "explanatoryNorms": ["coverage-parsimony", "depth"],
    "justificationStrategies": ["reductive"],
    "inferenceNorms": ["deductive", "abductive"],
    "evidence": "positivism-lay: the text ends in an observable, probabilistic implication ('Empirically, we should observe that the probability of vertical integration increases...', s11) and reads unobservables (opportunism, hazard) through their observable consequences, but it does not state a formal theory of evidence. falsificationism-methodological: it states a refutable comparative-static implication with a sign and an interaction (s11). The text alone cannot show the programme-level appraisal by novel facts that 'sophisticated' requires, so I put that question in openQuestions. Ontology: entities named in s1-s2, s4-s5b, s7-s8 and s10. Model classes: causal (s4-s6: specificity raises hazard); functional (governance is explained by its cost consequences, s1, s9); teleological (s1 'more cheaply governed' read as a choice criterion; this is the Reading-1 interpretation, see pivotal difference D1). Explanatory norms: coverage-parsimony (three dimensions, one 'decisive', s2-s3, cover the whole make-or-buy range); depth (a micro-mechanism of hold-up is given, s4-s5b). Justification: reductive, because firm boundaries are explained by transaction-level attributes and individual behavioural assumptions (s1-s5b). Inference norms: deductive language ('therefore' s6, 'It follows that' s9) and an abductive explanatory claim ('Firms exist because', s1)."
  },
  "scopeConditions": [
    {"@id": "tce:S1", "statement": "The theory applies to transactions where at least one party makes an investment that becomes sunk before all terms of exchange are settled ('once the investment is sunk', s4).", "explicitness": "explicit"},
    {"@id": "tce:S2", "statement": "The selection claim (P4) applies only where firms face competition strong enough to affect survival ('selected out by competition', s10).", "explicitness": "implicit"},
    {"@id": "tce:S3", "statement": "For each transaction, market, hybrid and hierarchy are all legally and technologically feasible alternatives; the comparison is among feasible structures (surfaced: needed for s9 to assign any level of specificity to any structure).", "explicitness": "surfaced"},
    {"@id": "tce:S4", "statement": "The governing parties are firms whose governance choices respond to cost (s1, s10); bureaus and non-profits are not obviously covered (surfaced).", "explicitness": "surfaced"}
  ],
  "constructs": [
    {
      "@id": "tce:C1", "label": "Transaction", "constructType": "entity", "level": "transaction",
      "definition": "The exchange that is 'governed' by a market, hybrid or hierarchy (s1) and that 'differ[s] along three dimensions' (s2). The text does not define where one transaction ends and another begins.",
      "measurementCommitments": [{"indicator": "uncommitted (no rule for delimiting a transaction)", "unitOfAnalysis": "transaction"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C1.com1", "statement": "If X is a transaction, then X takes a value on asset specificity, uncertainty and frequency (s2).", "refs": ["tce:C2", "tce:C3", "tce:C4"], "strength": "strict"},
          {"@id": "tce:C1.com2", "statement": "If X is a transaction, then X is governed by exactly one of market, hybrid or hierarchy at a given time (inferred from s9).", "refs": ["tce:C9"], "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C1.ent1", "statement": "If an exchange could in principle be governed by an alternative structure, one is entitled to treat it as a transaction (inferred; the text gives no criterion).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C1.lic1", "statement": "If X is a transaction, others may pose the governance question for X separately from the firm's other transactions (inferred from s9).", "refs": ["tce:A3"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C1.pre1", "statement": "If governance is assigned per transaction, then it is excluded that one firm-wide choice fixes governance whatever the transactions' attributes are (inferred from s9).", "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s1, s2"}
    },
    {
      "@id": "tce:C2", "label": "Asset specificity", "constructType": "attribute", "level": "transaction",
      "definition": "The degree to which an investment supporting the transaction has 'value ... much higher inside this relationship than in [its] next-best use' (s4).",
      "measurementCommitments": [
        {"indicator": "gap between an asset's value inside the relationship and its value in its next-best use", "level": "ordinal", "method": "the text names three bands (low, intermediate, high; s9) but gives no scale", "unitOfAnalysis": "transaction"},
        {"indicator": "type of specific asset, by example: a die built for one customer (physical), a plant sited next to one buyer (site), skills learned for one employer's systems (human)", "level": "nominal", "unitOfAnalysis": "transaction"}
      ],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C2.com1", "statement": "If a transaction has high asset specificity, then some party holds an investment that loses much of its value if redeployed (s4).", "strength": "strict"},
          {"@id": "tce:C2.com2", "statement": "If asset specificity is high and the investment is sunk, then the investing party is exposed to opportunistic renegotiation, given incomplete contracts and some opportunism (s4, s5a, s5b).", "refs": ["tce:C6", "tce:C7", "tce:C8"], "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C2.ent1", "statement": "If a transaction is supported by a dedicated tool, a co-located plant or relationship-specific skills, one is entitled to assert positive asset specificity (s4, by example).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C2.lic1", "statement": "If asset specificity rises, others may infer that market governance becomes more hazardous (s6) and that vertical integration becomes more probable (s11).", "refs": ["tce:P2", "tce:P5"], "strength": "defeasible"},
          {"@id": "tce:C2.lic2", "statement": "If asset specificity is in the low, intermediate or high band, others may infer that the aligned structure is market, hybrid or hierarchy respectively (s9).", "refs": ["tce:P3"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C2.pre1", "statement": "If an asset is as valuable in its next-best use as in the relationship, it cannot count as specific (s4).", "strength": "strict"},
          {"@id": "tce:C2.pre2", "statement": "If asset specificity is the decisive dimension, then governance cannot be insensitive to it while being driven by uncertainty or frequency (s3).", "refs": ["tce:A5"], "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s2, s3, s4"}
    },
    {
      "@id": "tce:C3", "label": "Uncertainty", "constructType": "attribute", "level": "transaction",
      "definition": "'The uncertainty surrounding' the transaction (s2). The text does not say whether its source is environmental, behavioural or technological.",
      "measurementCommitments": [{"indicator": "uncommitted (s11 implies at least a high/low contrast)", "level": "ordinal", "unitOfAnalysis": "transaction"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C3.com1", "statement": "If uncertainty is high, then more contingencies go unanticipated in the contract (surfaced; the text does not state this, and it is needed for P6).", "refs": ["tce:A11", "tce:C7"], "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C3.ent1", "statement": "The text gives no entitlement condition. A candidate is that a transaction is highly uncertain if its specifications, volumes or technology change unpredictably during its life (inferred; flagged).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C3.lic1", "statement": "If uncertainty is high, others may infer that the slope of integration probability on asset specificity is steeper (s11).", "refs": ["tce:P6"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C3.pre1", "statement": "Reading 1: if asset specificity is near zero, then high uncertainty does not by itself raise the probability of integration (inferred from s3 together with the interaction-only wording of s11).", "refs": ["tce:P7"], "strength": "defeasible"}
        ]
      },
      "alternativeRoles": [
        {
          "readingLabel": "reading-3 (independent dimensions)",
          "commitments": [{"@id": "tce:C3.r3.com1", "statement": "If uncertainty is high, then market governance is costlier whatever the level of asset specificity, because adaptation needs grow (inferred from s2 listing uncertainty as a dimension of its own).", "strength": "defeasible"}],
          "entitlements": [{"@id": "tce:C3.r3.ent1", "statement": "As in reading 1 (no condition stated in the text).", "strength": "defeasible"}],
          "licenses": [{"@id": "tce:C3.r3.lic1", "statement": "If uncertainty is high, others may infer a higher probability of integration even at low asset specificity, and a steeper slope on asset specificity (s11 plus a main effect).", "refs": ["tce:P7.r3"], "strength": "defeasible"}],
          "precludes": [{"@id": "tce:C3.r3.pre1", "statement": "Excludes that uncertainty matters only through its interaction with asset specificity.", "strength": "defeasible"}]
        }
      ],
      "source": {"citation": "Input A", "span": "s2, s11"}
    },
    {
      "@id": "tce:C4", "label": "Frequency", "constructType": "attribute", "level": "transaction",
      "definition": "'The frequency with which [transactions] recur' (s2).",
      "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "transaction"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C4.com1", "statement": "If frequency is a dimension on which transactions differ, then two transactions that differ only in frequency can in principle differ in governance (s2). The text states no relation that would realize this.", "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C4.ent1", "statement": "If the same exchange between the same parties recurs often, one is entitled to assert high frequency (inferred from 'recur', s2).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C4.lic1", "statement": "The passage licenses no downstream inference from frequency. A candidate from outside the passage is that recurrent transactions more readily recover the set-up cost of specialized governance (inferred; not licensed by the text; flagged).", "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C4.pre1", "statement": "If asset specificity is decisive (s3), then frequency cannot by itself determine the governance structure.", "refs": ["tce:A5"], "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s2"}
    },
    {
      "@id": "tce:C5", "label": "Bounded rationality", "constructType": "disposition", "level": "individual",
      "definition": "Contracting parties 'cannot write complete contracts that anticipate every contingency' (s5a).",
      "measurementCommitments": [{"indicator": "uncommitted (held as a maintained assumption, not a variable)", "unitOfAnalysis": "contracting party"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C5.com1", "statement": "If parties are boundedly rational, then contracts for non-trivial transactions are incomplete (s5a).", "refs": ["tce:C7"], "strength": "strict"}
        ],
        "entitlements": [
          {"@id": "tce:C5.ent1", "statement": "It is asserted of all contracting parties as a general premise (s5a). The text asks for no transaction-specific evidence.", "strength": "strict"}
        ],
        "licenses": [
          {"@id": "tce:C5.lic1", "statement": "If parties are boundedly rational, others may infer that contracts have gaps which, given opportunism, can be exploited ex post (s5a, s5b).", "refs": ["tce:C6", "tce:C8"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C5.pre1", "statement": "Excludes that hold-up is removed by comprehensive ex ante contracting (s5a).", "strength": "strict"}
        ]
      },
      "source": {"citation": "Input A", "span": "s5a"}
    },
    {
      "@id": "tce:C6", "label": "Opportunism", "constructType": "disposition", "level": "individual",
      "definition": "The disposition of 'some' contracting parties to exploit gaps in contracts (s5b).",
      "measurementCommitments": [{"indicator": "uncommitted (held as a maintained assumption)", "unitOfAnalysis": "contracting party"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C6.com1", "statement": "If some parties are opportunistic, then gaps in contracts will be exploited (s5b).", "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C6.ent1", "statement": "The text requires only that 'some' parties be opportunistic. I infer that this suffices for the hazard only if opportunistic parties cannot be identified ex ante (inferred; flagged).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C6.lic1", "statement": "If opportunism is present, others may infer that a party holding sunk specific investments faces a risk of renegotiation (s4, s5b).", "refs": ["tce:C8"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C6.pre1", "statement": "Excludes that unenforced promises are a sufficient safeguard for highly specific investments (inferred from s5b).", "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s5b"}
    },
    {
      "@id": "tce:C7", "label": "Contractual incompleteness", "constructType": "state", "level": "dyad",
      "definition": "Contracts that do not 'anticipate every contingency' (s5a).",
      "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "contract / dyad"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C7.com1", "statement": "If a contract is incomplete, then some contingencies will call for adaptation or renegotiation after the contract is signed (inferred from s5a-s5b).", "strength": "strict"}
        ],
        "entitlements": [
          {"@id": "tce:C7.ent1", "statement": "Bounded rationality entitles one to assert incompleteness (s5a).", "refs": ["tce:C5"], "strength": "strict"},
          {"@id": "tce:C7.ent2", "statement": "High uncertainty entitles one to assert greater incompleteness (surfaced).", "refs": ["tce:C3", "tce:A11"], "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C7.lic1", "statement": "If a contract is incomplete and some party is opportunistic and asset specificity is high, others may infer a hold-up hazard (s4-s5b).", "refs": ["tce:C8", "tce:M1"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C7.pre1", "statement": "Excludes that the transaction is fully governed by a court-enforced complete contingent contract (s5a).", "strength": "strict"}
        ]
      },
      "source": {"citation": "Input A", "span": "s5a"}
    },
    {
      "@id": "tce:C8", "label": "Contractual (hold-up) hazard", "constructType": "state", "level": "dyad",
      "definition": "The exposure of the investing party 'to opportunistic renegotiation once the investment is sunk' (s4). The text aggregates it as markets being 'hazardous' (s6).",
      "measurementCommitments": [{"indicator": "uncommitted (not observed directly; read off asset specificity)", "unitOfAnalysis": "dyad / transaction"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C8.com1", "statement": "If the hazard is high under market governance, then market governance of that transaction is costlier (s6, s9).", "refs": ["tce:C15"], "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C8.ent1", "statement": "If asset specificity is high and the investment is sunk and the contract is incomplete and some party is opportunistic, one is entitled to assert the hazard (s4-s6).", "refs": ["tce:C2", "tce:C5", "tce:C6", "tce:C7"], "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C8.lic1", "statement": "If the hazard is high, others may infer that a structure that suppresses opportunism (hierarchy) becomes comparatively more attractive (s7).", "refs": ["tce:C12"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C8.pre1", "statement": "Excludes a material hazard when asset specificity is near zero, since there is then little to appropriate (inferred from s4).", "strength": "defeasible"},
          {"@id": "tce:C8.pre2", "statement": "Excludes that the hazard is as high under hierarchy as under market for the same transaction (s7).", "refs": ["tce:A6"], "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s4, s6"}
    },
    {
      "@id": "tce:C9", "label": "Governance structure", "constructType": "entity", "level": "transaction",
      "definition": "The structure within which a transaction is governed, one of market, hybrid or hierarchy, ordered with hybrid 'between the two' (s1, s7-s9).",
      "measurementCommitments": [{"indicator": "observed structure: spot or arm's-length exchange / long-term contract or alliance / common ownership", "level": "ordinal", "method": "ordering taken from s8", "unitOfAnalysis": "transaction"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C9.com1", "statement": "If a governance structure is assigned to a transaction, then it is one of three discrete alternatives ordered market < hybrid < hierarchy (s8, s9).", "strength": "strict"}
        ],
        "entitlements": [
          {"@id": "tce:C9.ent1", "statement": "Observed ownership and contract form entitle one to classify a transaction's governance: common ownership with authority means hierarchy (s7), a long-term contract or alliance means hybrid (s8), and anything else means market (inferred).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C9.lic1", "statement": "If governance structures are distinguished, others may infer that each has a cost profile that varies with asset specificity (s6-s9).", "refs": ["tce:C15"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C9.pre1", "statement": "Excludes that all three structures are equally costly at every level of asset specificity, since otherwise no alignment would be discriminating (s9).", "strength": "strict"}
        ]
      },
      "source": {"citation": "Input A", "span": "s1, s7, s8, s9"}
    },
    {
      "@id": "tce:C10", "label": "Market governance", "constructType": "entity", "level": "transaction",
      "definition": "Governance 'across a market' (s1), set against common ownership (s7). By contrast it involves separately owned parties without authority.",
      "measurementCommitments": [{"indicator": "separate ownership and no long-term contract or alliance (inferred by contrast with s7, s8)", "level": "nominal", "unitOfAnalysis": "transaction"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C10.com1", "statement": "If a transaction is market-governed, then adaptation needs agreement between separately owned parties, not fiat (inferred by contrast with s7).", "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C10.ent1", "statement": "Exchange between separately owned parties without a long-term contract or alliance entitles one to assert market governance (inferred).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C10.lic1", "statement": "If a transaction is market-governed, others may infer that its hazard rises with asset specificity (s6) and that it is aligned only if asset specificity is low (s9).", "refs": ["tce:P2", "tce:P3"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C10.pre1", "statement": "Excludes adaptation by fiat (s7, by contrast).", "strength": "strict"},
          {"@id": "tce:C10.pre2", "statement": "Excludes that market governance is aligned when asset specificity is high (s9).", "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s1, s6, s9"}
    },
    {
      "@id": "tce:C11", "label": "Hybrid governance", "constructType": "entity", "level": "dyad",
      "definition": "'Hybrids such as long-term contracts and alliances' that 'fall between' market and hierarchy (s8). The text does not say in what respect they fall between.",
      "measurementCommitments": [{"indicator": "presence of a long-term contract or alliance between separately owned parties (by example, s8)", "level": "nominal", "unitOfAnalysis": "transaction"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C11.com1", "statement": "If a transaction is governed by a hybrid, then its governance properties are intermediate between market and hierarchy (s8). Which properties are intermediate is unspecified; I read it as both safeguards and costs (surfaced as A8).", "refs": ["tce:A8"], "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C11.ent1", "statement": "A long-term contract or alliance between separately owned parties entitles one to assert hybrid governance (s8).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C11.lic1", "statement": "If asset specificity is intermediate, others may infer that the hybrid is the aligned structure (s9).", "refs": ["tce:P3"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C11.pre1", "statement": "Excludes that the hybrid is the aligned structure at either extreme of asset specificity (s9).", "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s8, s9"}
    },
    {
      "@id": "tce:C12", "label": "Hierarchy", "constructType": "entity", "level": "organization",
      "definition": "'Common ownership with authority and administrative control' (s7).",
      "measurementCommitments": [{"indicator": "common ownership of both sides of the transaction (vertical integration, s11)", "level": "nominal", "unitOfAnalysis": "transaction"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C12.com1", "statement": "If a transaction is governed by hierarchy, then opportunism in it is suppressed and adaptation by fiat is available (s7).", "refs": ["tce:A6"], "strength": "defeasible"},
          {"@id": "tce:C12.com2", "statement": "If a transaction is governed by hierarchy, then it bears bureaucratic costs and weaker incentives than under the market (s7).", "refs": ["tce:C13", "tce:C14", "tce:A7"], "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C12.ent1", "statement": "Common ownership of both sides together with an authority relation and administrative control entitles one to assert hierarchy (s7).", "strength": "strict"}
        ],
        "licenses": [
          {"@id": "tce:C12.lic1", "statement": "If asset specificity is high, others may infer that hierarchy is the aligned structure (s9) and that firms exist for such transactions (s1).", "refs": ["tce:P1", "tce:P3"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C12.pre1", "statement": "Excludes that hierarchy is the aligned structure for low-specificity transactions (s7, s9).", "strength": "defeasible"},
          {"@id": "tce:C12.pre2", "statement": "Excludes counting common ownership without authority and administrative control as hierarchy (s7, definitional).", "strength": "strict"}
        ]
      },
      "source": {"citation": "Input A", "span": "s1, s7"}
    },
    {
      "@id": "tce:C13", "label": "Bureaucratic cost", "constructType": "attribute", "level": "organization",
      "definition": "The costs that hierarchy 'carries' (s7). Their content is unspecified.",
      "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "organization"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C13.com1", "statement": "If a transaction is moved into hierarchy, then it incurs positive bureaucratic cost (s7).", "strength": "strict"}
        ],
        "entitlements": [
          {"@id": "tce:C13.ent1", "statement": "The text gives no entitlement condition. Bureaucratic cost is asserted as a maintained property of hierarchy (s7; flagged).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C13.lic1", "statement": "If hierarchy carries bureaucratic cost, others may infer that hierarchy is not universally cost-minimizing, so there is a range of asset specificity where the market is cheaper (s9).", "refs": ["tce:P3"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C13.pre1", "statement": "Excludes that a hierarchy can replicate market governance and add fiat at no extra cost (inferred; the passage does not state this argument).", "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s7"}
    },
    {
      "@id": "tce:C14", "label": "Incentive intensity", "constructType": "attribute", "level": "transaction",
      "definition": "How 'high-powered' the parties' incentives are. Hierarchy 'weakens' them (s7).",
      "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "transaction / organization"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C14.com1", "statement": "If a transaction is moved from market to hierarchy, then incentive intensity falls (s7).", "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C14.ent1", "statement": "If a party's reward is less closely tied to its own output, one is entitled to assert lower incentive intensity (inferred; the text names no indicator).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C14.lic1", "statement": "If incentives are weakened, others may infer a cost of hierarchy that offsets its safeguards (s7, s9).", "refs": ["tce:C15"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C14.pre1", "statement": "Excludes a hierarchy that keeps full market-strength incentives (s7).", "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s7"}
    },
    {
      "@id": "tce:C15", "label": "Comparative governance cost", "constructType": "attribute", "level": "transaction",
      "definition": "The cost of governing a given transaction under a given structure, compared across structures ('more cheaply governed', s1; 'higher costs', s10).",
      "measurementCommitments": [{"indicator": "uncommitted (no direct measure; the text reads it off asset specificity and governance attributes)", "unitOfAnalysis": "transaction x governance structure"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C15.com1", "statement": "Reading 1: if structure g has the lowest governance cost for transaction t, then t comes to be governed by g (s1, s9, via A4 and A13).", "refs": ["tce:A4", "tce:A13"], "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C15.ent1", "statement": "Rising hazard under the market (C8), and bureaucratic cost and weakened incentives under hierarchy (C13, C14), entitle one to rank the structures' costs at a given level of asset specificity (s6, s7). No independent measure is given.", "refs": ["tce:C8", "tce:C13", "tce:C14"], "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C15.lic1", "statement": "If costs cross in the order market, hybrid, hierarchy as asset specificity rises, others may infer discriminating alignment (s9).", "refs": ["tce:P3", "tce:A8"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C15.pre1", "statement": "Excludes a governance assignment that is invariant to differences in governance cost (s1, s9).", "refs": ["tce:A4"], "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s1, s9, s10"}
    },
    {
      "@id": "tce:C16", "label": "Alignment (and misalignment)", "constructType": "relation", "level": "transaction",
      "definition": "The match between a transaction's attributes and its governance structure as assigned by the discriminating rule (s9). Misalignment is a mismatch (s10).",
      "measurementCommitments": [{"indicator": "whether the observed governance structure equals the structure s9 assigns to the transaction's asset-specificity band", "level": "nominal", "unitOfAnalysis": "transaction"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C16.com1", "statement": "If a transaction is misaligned, then it is governed at a higher cost than an available alternative would impose (s10).", "refs": ["tce:C15"], "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C16.ent1", "statement": "Comparing observed governance with the structure s9 assigns to the transaction's band of asset specificity entitles one to assert alignment or misalignment (inferred from s9-s10).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C16.lic1", "statement": "If a firm misaligns, others may infer higher costs and a lower survival probability for it (s10).", "refs": ["tce:P4"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C16.pre1", "statement": "Excludes the long-run persistence of misaligned firms under competition (s10).", "refs": ["tce:S2"], "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s9, s10"}
    },
    {
      "@id": "tce:C17", "label": "Firm", "constructType": "entity", "level": "organization",
      "definition": "In s1 the firm exists because hierarchy is cheaper for some transactions, so the firm is the locus of hierarchical governance. In s10 the firm is the agent that aligns or misaligns transactions and that competition selects. The text does not reconcile the two uses (see D4).",
      "measurementCommitments": [{"indicator": "uncommitted", "unitOfAnalysis": "organization"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C17.com1", "statement": "Reading 1: if a firm exists, then at least one transaction is governed more cheaply by hierarchy than by market (s1).", "refs": ["tce:P1"], "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C17.ent1", "statement": "Common ownership plus authority over a set of transactions entitles one to assert a firm (s7; inferred identification of firm with hierarchy).", "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C17.lic1", "statement": "If a firm exists, others may infer that its boundary is the set of transactions it governs by hierarchy (inferred).", "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C17.pre1", "statement": "Excludes explaining the firm's existence without reference to comparative governance cost (s1 'because').", "strength": "defeasible"}
        ]
      },
      "alternativeRoles": [
        {
          "readingLabel": "reading-2 (selection equilibrium)",
          "commitments": [{"@id": "tce:C17.r2.com1", "statement": "If X is a firm, then X holds a portfolio of transactions, some possibly misaligned, and is the unit on which competitive selection acts (s10).", "strength": "defeasible"}],
          "entitlements": [{"@id": "tce:C17.r2.ent1", "statement": "A separately surviving or exiting organization under common ownership entitles one to assert a firm (inferred from s10).", "strength": "defeasible"}],
          "licenses": [{"@id": "tce:C17.r2.lic1", "statement": "Others may infer that selection pressure on a misaligned transaction is diluted by the firm's other transactions (inferred).", "strength": "defeasible"}],
          "precludes": [{"@id": "tce:C17.r2.pre1", "statement": "Excludes reading the governance of each individual transaction as itself optimized.", "strength": "defeasible"}]
        }
      ],
      "source": {"citation": "Input A", "span": "s1, s10"}
    },
    {
      "@id": "tce:C18", "label": "Competitive selection", "constructType": "process", "level": "population",
      "definition": "The process by which firms that misalign 'over time, will be selected out by competition' (s10).",
      "measurementCommitments": [{"indicator": "uncommitted (s10 implies firm survival or exit over time as the observable)", "unitOfAnalysis": "firm-year within a population"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C18.com1", "statement": "If competition operates, then misaligned firms have a lower survival probability than aligned ones (s10).", "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C18.ent1", "statement": "If firms compete in the same markets and cost differences affect survival, one is entitled to assert selection (inferred; the text gives no condition).", "refs": ["tce:S2"], "strength": "defeasible"}
        ],
        "licenses": [
          {"@id": "tce:C18.lic1", "statement": "If selection operates and has had time to act, others may infer that observed governance approximates aligned governance (inferred from s10).", "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C18.pre1", "statement": "Excludes the long-run coexistence of aligned and misaligned firms under the same competitive pressure (s10).", "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s10"}
    },
    {
      "@id": "tce:C19", "label": "Vertical integration", "constructType": "state", "level": "transaction",
      "definition": "The observable whose 'probability' is predicted (s11). I take it as the empirical counterpart of hierarchy (C12) for a vertical transaction.",
      "measurementCommitments": [{"indicator": "make (common ownership) vs buy for the transaction", "level": "nominal", "method": "binary outcome modelled as a probability (s11), e.g. a discrete-choice model; the method is my inference", "unitOfAnalysis": "transaction"}],
      "inferentialRole": {
        "commitments": [
          {"@id": "tce:C19.com1", "statement": "If a transaction is vertically integrated, then it is governed by hierarchy (inferred identification with C12).", "refs": ["tce:C12"], "strength": "defeasible"}
        ],
        "entitlements": [
          {"@id": "tce:C19.ent1", "statement": "Common ownership of both stages of the transaction entitles one to assert vertical integration (s7, s11).", "strength": "strict"}
        ],
        "licenses": [
          {"@id": "tce:C19.lic1", "statement": "If vertical integration is observed across transactions that vary in asset specificity and uncertainty, others may use it to test P5 and P6 (s11).", "refs": ["tce:P5", "tce:P6"], "strength": "defeasible"}
        ],
        "precludes": [
          {"@id": "tce:C19.pre1", "statement": "Excludes counting hybrid governance as integration (inferred). The binary coding therefore merges hybrid with market; see openQuestions.", "strength": "defeasible"}
        ]
      },
      "source": {"citation": "Input A", "span": "s11"}
    }
  ],
  "relations": [
    {"@id": "tce:R1", "from": "tce:C5", "to": "tce:C7", "form": "causal", "sign": "positive"},
    {"@id": "tce:R2", "from": "tce:C2", "to": "tce:C8", "form": "causal", "sign": "positive", "moderators": ["tce:C6", "tce:C7"], "scope": ["tce:S1"]},
    {"@id": "tce:R3", "from": "tce:C6", "to": "tce:C8", "form": "causal", "sign": "positive", "moderators": ["tce:C7"]},
    {"@id": "tce:R4", "from": "tce:C8", "to": "tce:C15", "form": "causal", "sign": "positive", "moderators": ["tce:C10"]},
    {"@id": "tce:R5", "from": "tce:C12", "to": "tce:C8", "form": "causal", "sign": "negative"},
    {"@id": "tce:R6", "from": "tce:C12", "to": "tce:C13", "form": "causal", "sign": "positive"},
    {"@id": "tce:R7", "from": "tce:C12", "to": "tce:C14", "form": "causal", "sign": "negative"},
    {"@id": "tce:R8", "from": "tce:C3", "to": "tce:C7", "form": "causal", "sign": "positive"},
    {"@id": "tce:R9", "from": "tce:C15", "to": "tce:C9", "form": "teleological", "sign": "conditional", "scope": ["tce:S3"]},
    {"@id": "tce:R10", "from": "tce:C2", "to": "tce:C9", "form": "causal", "sign": "positive", "moderators": ["tce:C3"], "scope": ["tce:S3"]},
    {"@id": "tce:R11", "from": "tce:C16", "to": "tce:C15", "form": "causal", "sign": "negative"},
    {"@id": "tce:R12", "from": "tce:C16", "to": "tce:C17", "form": "selection", "sign": "positive", "moderators": ["tce:C18"], "scope": ["tce:S2"]},
    {"@id": "tce:R13", "from": "tce:C2", "to": "tce:C19", "form": "causal", "sign": "positive", "moderators": ["tce:C3"]}
  ],
  "mechanisms": [
    {"@id": "tce:M1", "label": "Hold-up: bounded rationality leaves gaps, opportunism exploits them, sunk specific assets make the exploitation costly under the market", "steps": ["tce:R1", "tce:R3", "tce:R2", "tce:R4"], "mechanismType": "strategic"},
    {"@id": "tce:M2", "label": "Hierarchical safeguard trade-off: hierarchy suppresses the hazard but adds bureaucratic cost and weakens incentives", "steps": ["tce:R5", "tce:R6", "tce:R7"], "mechanismType": "economic"},
    {"@id": "tce:M3", "label": "Discriminating alignment by economizing choice (reading 1)", "steps": ["tce:R4", "tce:R6", "tce:R7", "tce:R9", "tce:R10"], "mechanismType": "economic"},
    {"@id": "tce:M4", "label": "Selection backstop: misalignment raises cost and lowers survival", "steps": ["tce:R11", "tce:R12"], "mechanismType": "selection"}
  ],
  "assumptions": [
    {"@id": "tce:A1", "statement": "Contracting parties are boundedly rational and cannot write complete contracts (s5a).", "status": "core", "explicitness": "explicit", "supports": ["tce:R1", "tce:M1", "tce:P2", "tce:P3"]},
    {"@id": "tce:A2", "statement": "Some contracting parties are opportunistic and will exploit contractual gaps (s5b).", "status": "core", "explicitness": "explicit", "supports": ["tce:R3", "tce:M1", "tce:P2", "tce:P3"]},
    {"@id": "tce:A3", "statement": "The transaction is the unit of analysis, and governance is assigned transaction by transaction according to the transaction's attributes (s2, s9).", "status": "core", "explicitness": "implicit", "supports": ["tce:P3", "tce:P5"]},
    {"@id": "tce:A4", "statement": "Economizing: transactions come to be governed by the structure that governs them most cheaply (s1 'more cheaply governed'; s9 'It follows that').", "status": "core", "explicitness": "implicit", "supports": ["tce:R9", "tce:M3", "tce:P1", "tce:P3"]},
    {"@id": "tce:A5", "statement": "Asset specificity is the decisive dimension of transactions (s3).", "status": "core", "explicitness": "explicit", "supports": ["tce:R10", "tce:R13", "tce:P3", "tce:P5", "tce:P7"]},
    {"@id": "tce:A6", "statement": "Hierarchy suppresses opportunism and permits adaptation by fiat (s7).", "status": "core", "explicitness": "explicit", "supports": ["tce:R5", "tce:M2", "tce:P1", "tce:P3"]},
    {"@id": "tce:A7", "statement": "Hierarchy carries bureaucratic costs and weakens high-powered incentives (s7).", "status": "auxiliary", "explicitness": "explicit", "supports": ["tce:R6", "tce:R7", "tce:M2", "tce:P3"]},
    {"@id": "tce:A8", "statement": "Hybrids are intermediate in both safeguards and costs, so the cost curves of market, hybrid and hierarchy cross in that order as asset specificity rises (s8 'fall between'; ordering surfaced).", "status": "auxiliary", "explicitness": "surfaced", "surfacedBy": "Explicator (Role 1), run 01", "supports": ["tce:P3"]},
    {"@id": "tce:A9", "statement": "Specific investments are sunk before the terms of exchange are fully settled, so the quasi-rents they create can be appropriated in renegotiation (s4 'once the investment is sunk').", "status": "core", "explicitness": "explicit", "supports": ["tce:R2", "tce:M1"]},
    {"@id": "tce:A10", "statement": "Asset specificity is determined prior to, and independently of, the governance choice, so it can be treated as exogenous in P5 (surfaced).", "status": "auxiliary", "explicitness": "surfaced", "surfacedBy": "Explicator (Role 1), run 01", "supports": ["tce:R13", "tce:P5"]},
    {"@id": "tce:A11", "statement": "Higher uncertainty increases contractual incompleteness, that is, the number of unanticipated contingencies (surfaced; needed for P6).", "status": "auxiliary", "explicitness": "surfaced", "surfacedBy": "Explicator (Role 1), run 01", "supports": ["tce:R8", "tce:P6"]},
    {"@id": "tce:A12", "statement": "Competitive selection is strong and fast enough to eliminate firms that misalign (s10).", "status": "auxiliary", "explicitness": "explicit", "supports": ["tce:R12", "tce:M4", "tce:P4"]},
    {"@id": "tce:A13", "statement": "The parties who choose governance can identify the cost-minimizing structure ex ante and choose it (surfaced; needed for the economizing-choice reading of s9).", "status": "auxiliary", "explicitness": "surfaced", "surfacedBy": "Explicator (Role 1), run 01", "supports": ["tce:R9", "tce:M3", "tce:P3"]}
  ],
  "propositions": [
    {"@id": "tce:P1", "statement": "Firms exist because some transactions are more cheaply governed inside a hierarchy than across a market (s1).", "claimType": "explanation", "factStatus": "accommodation", "observables": ["existence of firms (hierarchically governed transactions)"]},
    {"@id": "tce:P2", "statement": "The hazard of market governance increases with asset specificity (s6).", "claimType": "explanation", "factStatus": "undetermined", "observables": []},
    {"@id": "tce:P3", "statement": "Transactions are aligned with governance in a discriminating way: low asset specificity with market, intermediate with hybrid, high with hierarchy (s9).", "claimType": "prediction", "factStatus": "undetermined", "observables": ["asset-specificity band of each transaction", "governance structure of each transaction"]},
    {"@id": "tce:P4", "statement": "Firms that misalign transactions and governance incur higher costs and, over time, are selected out by competition (s10).", "claimType": "prediction", "factStatus": "undetermined", "observables": ["costs of misaligned vs aligned firms", "survival or exit of misaligned vs aligned firms over time"]},
    {"@id": "tce:P5", "statement": "The probability of vertical integration increases with asset specificity (s11).", "claimType": "prediction", "factStatus": "novel", "observables": ["make-or-buy outcome per transaction", "asset-specificity indicators per transaction"]},
    {"@id": "tce:P6", "statement": "The increase in the probability of vertical integration with asset specificity is steeper when uncertainty is high (s11).", "claimType": "prediction", "factStatus": "novel", "observables": ["make-or-buy outcome", "asset specificity", "uncertainty", "their interaction"]},
    {"@id": "tce:P7", "statement": "When asset specificity is near zero, uncertainty does not raise the probability of vertical integration (surfaced from s3 and the interaction-only wording of s11).", "claimType": "prediction", "factStatus": "undetermined", "observables": ["make-or-buy outcome for low-specificity transactions across levels of uncertainty"]}
  ],
  "derivations": [
    {"@id": "tce:D1", "target": "tce:P3", "premises": ["tce:A1", "tce:A2", "tce:A4", "tce:A6", "tce:A7", "tce:A9", "tce:A13"], "method": "verbal", "status": "asserted", "auxiliariesRequired": ["tce:A8"], "notes": "Asserted in prose ('It follows that', s9). The three-way ordering seems to need A8, which the text does not state. Not checked."},
    {"@id": "tce:D2", "target": "tce:P5", "premises": ["tce:P3", "tce:A3", "tce:A5"], "method": "verbal", "status": "asserted", "auxiliariesRequired": ["tce:A10"], "notes": "The text does not state the derivation; it reads as the binary (make/buy) projection of P3. It seems to need A10 for a causal reading and the identification of C19 with C12. Not checked."},
    {"@id": "tce:D3", "target": "tce:P6", "premises": ["tce:P5", "tce:R8"], "method": "verbal", "status": "asserted", "auxiliariesRequired": ["tce:A11"], "notes": "The text gives no derivation. P6 seems to follow only if uncertainty enlarges the hold-up hazard (A11) and the hazard interacts multiplicatively with asset specificity. Not checked."}
  ],
  "openQuestions": [
    "Q1 (D1): Is alignment in s9 produced by deliberate economizing choice (A4 + A13) or by competitive selection (A12, s10)? The text uses both 'It follows that' and 'selected out by competition'.",
    "Q2: A13 (parties identify the cost-minimizing structure) sits in tension with A1 (bounded rationality). Is the theorist willing to assume governance choosers are less bounded than contract writers?",
    "Q3 (D2): Does uncertainty have an effect of its own on integration (main effect) or only a moderating one? s2 lists it as a dimension; s11 mentions it only as a moderator.",
    "Q4 (D3): Is 'asset specificity is the decisive dimension' (A5) hard core or protective belt? I could not settle this from the text.",
    "Q5: Frequency (C4) is introduced in s2 but enters no relation or proposition. Should it be dropped, or given a relation (e.g. as a condition for specialized governance)?",
    "Q6: 'Fall between the two' (s8): between on which dimension(s)? A8 reads it as both safeguards and costs. Without that, P3's three-way ordering seems not to follow.",
    "Q7: P3 predicts three categories, but P5 uses a binary outcome (vertical integration). How should hybrids be coded when testing P5?",
    "Q8: Comparative governance cost (C15) has no measure independent of asset specificity and governance attributes. Is there an indicator that would let P3 be tested without reading costs off the alignment it predicts?",
    "Q9 (D4): Is the firm the governance structure (s1) or the organization that holds many transactions and is selected (s10)?",
    "Q10: The fact status of P5 and P6 is marked 'novel' provisionally, on the textual ground that they are derived consequences framed as predictions. Whether they preceded the empirical record (e.g. Monteverde & Teece 1982; Masten 1984) is a historical question to verify.",
    "Q11: The corroboration logic is tagged 'falsificationism-methodological'. 'Sophisticated' needs evidence of programme-level appraisal by novel facts, which this passage does not provide.",
    "Q12: A9 (sunk investment and appropriable quasi-rents) is classified as core because M1 depends on it. A reader could treat it as part of the belt that elaborates A5."
  ],
  "provenance": {"createdBy": "Foundry Explicator (Role 1, instruction set v0.1), model claude-opus-5-5, run 01", "ledgerEvents": []}
}
```

**Classification reasons for assumptions (step 4).** All classifications are proposals for the theorist to decide.

| Id | Status | Reason |
|---|---|---|
| tce:A1 | core | Without bounded rationality, complete contracts would remove the hold-up hazard (s5a), and the explanation of firms in s1 would have nothing to work on. Giving it up abandons the programme. |
| tce:A2 | core | Without opportunism, contractual gaps would not be exploited (s5b), and the market would not become hazardous (s6). |
| tce:A3 | core | Treating transactions as the unit (s2) defines what the programme explains. Replacing it with a different unit, such as resources or dependencies, would make a different programme. |
| tce:A4 | core | Economizing is the positive heuristic that turns cost comparisons into governance outcomes (s1, s9). |
| tce:A5 | core (reading 1) | The text calls asset specificity "decisive" (s3), and every prediction runs through it (s9, s11). Contested: see D3 and reading 3. |
| tce:A6 | core | Hierarchy's ability to suppress opportunism is the only comparative advantage the text gives it (s7). Without it, s1 has no explanation. |
| tce:A7 | auxiliary | Some offsetting cost of hierarchy is needed for P3. Which cost it is (bureaucracy, weakened incentives) could be revised without abandoning the programme. |
| tce:A8 | auxiliary | Needed only for the three-way ordering. If hybrids were dominated over some range, a two-way market/hierarchy version would survive. |
| tce:A9 | core | M1 needs sunk, appropriable quasi-rents to link asset specificity to hazard (s4). Contestable: see Q12. |
| tce:A10 | auxiliary | Exogeneity of asset specificity is a modelling convenience for P5. It can be relaxed (joint choice of investment and governance) while the programme stays intact. |
| tce:A11 | auxiliary | A bridge assumption needed only for the interaction in P6. It can be replaced by another reason why uncertainty amplifies hazard. |
| tce:A12 | auxiliary (reading 1) | In reading 1 selection is a backstop for deliberate choice, so it can be weakened (slow selection) without losing P3. In reading 2 it becomes core. |
| tce:A13 | auxiliary (reading 1) | Needed only for the choice reading of alignment. It can be dropped in favour of selection (reading 2). |

**Fact-status reasons (step 5).**
- **tce:P1, accommodation.** The existence of firms is the explanandum (s1). The theory is fitted to explain a fact already known, not one it predicted.
- **tce:P2, undetermined.** The hazard has no observable in the text, so novelty cannot be assessed.
- **tce:P3, undetermined.** The text does not say whether the three-way pattern was known before the theory. The hybrid band also depends on A8.
- **tce:P4, undetermined.** It is stated as a consequence, with no observable or test attached.
- **tce:P5, novel (provisional).** It is framed as a derived consequence ("we should observe", s11), not as a fitted known regularity. Historical priority is to verify (Q10).
- **tce:P6, novel (provisional).** It is a specific interaction implication, not a general stylized fact, and it rests on the surfaced A11. Historical priority is to verify.
- **tce:P7, undetermined.** It is surfaced by me, not stated in the text, and it is reading-dependent.

---

## (b) Further readings: fields that differ from reading 1

### Reading 2: "selection equilibrium"

This reading takes s10 as the operative mechanism. Discriminating alignment (s9) is a population-level regularity produced by competition eliminating misaligned firms. It is not a rule that parties apply to each transaction. The textual grounds are "over time, will be selected out by competition" (s10), and the fact that s1 says firms exist *because* hierarchy is cheaper, which states a functional explanation without naming a decision maker.

```json
{
  "@id": "tce:reading-2",
  "@type": "TheoryObject",
  "readingOf": "tce:ensemble-1",
  "label": "Transaction-cost theory of firm boundaries, reading 2 (selection equilibrium)",
  "differsFrom": "tce:reading-1",
  "replace": {
    "stanceProfile.modelClasses": ["causal", "functional", "dynamical"],
    "stanceProfile.evidence (model classes)": "functional explanation backed by selection (s10), not teleological choice; dynamical because alignment is reached 'over time' (s10).",
    "relations": [
      {"@id": "tce:R9.r2", "from": "tce:C15", "to": "tce:C9", "form": "selection", "sign": "conditional", "moderators": ["tce:C18"], "scope": ["tce:S2", "tce:S3"]}
    ],
    "mechanisms": [
      {"@id": "tce:M3.r2", "label": "Discriminating alignment as a selection equilibrium: governance varies, misaligned firms bear higher cost and exit, survivors are aligned", "steps": ["tce:R4", "tce:R6", "tce:R7", "tce:R11", "tce:R12", "tce:R9.r2"], "mechanismType": "selection"}
    ],
    "assumptions": [
      {"@id": "tce:A4.r2", "statement": "Economizing is a property of the surviving population: governance structures that are more costly for a transaction do not persist in competitive populations (s1, s10).", "status": "core", "explicitness": "implicit"},
      {"@id": "tce:A12.r2", "statement": "Competitive selection is strong and fast enough to eliminate firms that misalign (s10).", "status": "core", "explicitness": "explicit", "supports": ["tce:R9.r2", "tce:M3.r2", "tce:P3.r2", "tce:P4"]},
      {"@id": "tce:A14", "statement": "Governance arrangements vary across firms, for example through trial, imitation or error, so that selection has variation to act on (surfaced).", "status": "auxiliary", "explicitness": "surfaced", "surfacedBy": "Explicator (Role 1), run 01"}
    ],
    "propositions": [
      {"@id": "tce:P3.r2", "statement": "In competitive populations that have had time to be selected, the distribution of governance across transactions approximates discriminating alignment: low asset specificity with market, intermediate with hybrid, high with hierarchy. Individual transactions may be misaligned.", "claimType": "prediction", "factStatus": "undetermined", "observables": ["share of aligned transactions by industry", "industry age", "competitive intensity"]}
    ],
    "constructs (inferentialRole switches to alternativeRoles 'reading-2')": ["tce:C17"],
    "tce:C15.inferentialRole.commitments": [
      {"@id": "tce:C15.r2.com1", "statement": "If structure g has the lowest governance cost for transaction t, then firms governing t by structures other than g have a lower expected survival (s10).", "strength": "defeasible"}
    ]
  },
  "add": {
    "propositions": [
      {"@id": "tce:P8", "statement": "The prevalence of misaligned transactions decreases with competitive intensity and with the time a population has been exposed to competition (surfaced from s10 under reading 2).", "claimType": "prediction", "factStatus": "novel", "observables": ["misalignment share", "competitive intensity (e.g. concentration, import penetration)", "industry or firm age"]},
      {"@id": "tce:P9", "statement": "Among firms of the same age in the same market, misaligned firms have a higher exit hazard than aligned ones (sharpening of P4 under reading 2).", "claimType": "prediction", "factStatus": "undetermined", "observables": ["firm exit", "alignment status of the firm's main transactions"]}
    ],
    "scopeConditions": [
      {"@id": "tce:S2.r2", "statement": "P3 itself (not only P4) holds only in competitive populations observed after selection has had time to act.", "explicitness": "surfaced"}
    ]
  },
  "remove": ["tce:A4", "tce:A12", "tce:A13", "tce:R9", "tce:M3", "tce:P3"],
  "openQuestions (added)": [
    "Under reading 2, P3 does not hold in protected, regulated or young industries. Does the theorist accept that restriction of scope?",
    "Selection acts on firms but alignment is defined per transaction (C16 vs C17.r2). How much misalignment can a firm with many aligned transactions carry before selection bites?"
  ]
}
```

### Reading 3: "independent dimensions"

This reading takes s2 at its word. Asset specificity, uncertainty and frequency are three dimensions on which transactions differ, and uncertainty has an effect of its own on governance. "Decisive" (s3) is read as a claim about relative weight, open to empirical revision, not as a methodological decision. Asset specificity therefore moves to the protective belt. Reading 3 keeps reading 1's choice mechanism (A4, A13), so it differs from reading 1 only on D2 and D3.

```json
{
  "@id": "tce:reading-3",
  "@type": "TheoryObject",
  "readingOf": "tce:ensemble-1",
  "label": "Transaction-cost theory of firm boundaries, reading 3 (independent dimensions)",
  "differsFrom": "tce:reading-1",
  "replace": {
    "assumptions": [
      {"@id": "tce:A5.r3", "statement": "Asset specificity is the empirically most important of the three dimensions (s3), a weighting claim revisable in the light of evidence.", "status": "auxiliary", "explicitness": "explicit"}
    ],
    "constructs (inferentialRole switches to alternativeRoles 'reading-3')": ["tce:C3"],
    "propositions": [
      {"@id": "tce:P7.r3", "statement": "Holding asset specificity constant, including near zero, higher uncertainty raises the probability of vertical integration; the effect of asset specificity is also steeper when uncertainty is high.", "claimType": "prediction", "factStatus": "undetermined", "observables": ["make-or-buy outcome", "uncertainty main effect", "asset specificity x uncertainty interaction"]}
    ]
  },
  "add": {
    "relations": [
      {"@id": "tce:R14", "from": "tce:C3", "to": "tce:C19", "form": "causal", "sign": "positive"},
      {"@id": "tce:R15", "from": "tce:C3", "to": "tce:C15", "form": "causal", "sign": "positive", "moderators": ["tce:C10"]}
    ],
    "assumptions": [
      {"@id": "tce:A15", "statement": "Uncertainty raises the cost of market governance through adaptation needs even when no specific assets are at stake (surfaced; needed for R15).", "status": "auxiliary", "explicitness": "surfaced", "surfacedBy": "Explicator (Role 1), run 01"}
    ]
  },
  "remove": ["tce:A5", "tce:P7"],
  "note": "Frequency (tce:C4) still enters no relation in this reading. The text gives no basis for one, and I did not invent one (see Q5)."
}
```

### Ensemble

```json
{
  "@id": "tce:ensemble-1",
  "@type": "FormalizationEnsemble",
  "members": ["tce:reading-1", "tce:reading-2", "tce:reading-3"],
  "pivotalDifferences": [
    "D1: mechanism producing alignment (s9 vs s10): teleological economizing choice (readings 1, 3) vs selection equilibrium (reading 2).",
    "D2: role of uncertainty (s2 vs s11): moderator only (readings 1, 2) vs main effect plus moderator (reading 3).",
    "D3: status of 'asset specificity is decisive' (s3): core (readings 1, 2) vs auxiliary (reading 3).",
    "D4: referent of 'firm' (s1 vs s10): the hierarchy itself (readings 1, 3) vs the organization holding a portfolio of transactions, which is the unit of selection (reading 2)."
  ],
  "dispersion": 0.43,
  "dispersionBasis": "Proposed metric, not a Foundry standard: the share of reading-1 propositions that are restated, replaced or removed in at least one other reading. P3 and P4 change in reading 2 (P3 restated as P3.r2; P4 sharpened by P9); P7 is replaced in reading 3. That is 3 of 7, about 0.43."
}
```

---

## (c) Pivotal differences

| # | Underdetermined point (textual basis) | Reading 1 | Reading 2 | Reading 3 | Downstream propositions that change |
|---|---|---|---|---|---|
| D1 | What produces alignment: "It follows that transactions are aligned" (s9) vs "will be selected out by competition" (s10) | Deliberate economizing choice: A4 core, A13 auxiliary, R9 teleological | Selection: A4.r2 and A12.r2 core, A13 removed, R9.r2 selection | as reading 1 | **P3** is per-transaction in R1/R3 but population-level and scope-restricted to competitive, mature populations in R2. **P4** is a backstop in R1 but carries the explanation in R2. **P8** and **P9** are new in R2. Under R2, misalignment in protected industries is expected; under R1 it is an anomaly. |
| D2 | Role of uncertainty: listed as an independent dimension (s2) but used only as a moderator (s11) | Moderator only | Moderator only | Main effect plus moderator (R14, R15, A15) | **P7** (no uncertainty effect at low asset specificity) holds in R1/R2 and is reversed in R3 (P7.r3). **P6** is unchanged in all readings. |
| D3 | Status of "asset specificity is the decisive dimension" (s3) | Core | Core | Auxiliary (A5.r3) | No proposition's content changes. What changes is where an anomaly to **P5** is directed. In R1/R2 a null effect of asset specificity is absorbed by the belt (measurement, A10 exogeneity, A12). In R3 it can be absorbed by re-weighting toward uncertainty without abandoning the programme. |
| D4 | Referent of "firm": "Firms exist because ... hierarchy" (s1) vs "Firms that misalign ... selected out" (s10) | Firm = hierarchy (C17 primary role) | Firm = portfolio of transactions and unit of selection (C17 alternative role) | as reading 1 | **P1** reads as a per-transaction cost claim in R1/R3 but as a survival claim in R2. Under R2, P4's selection pressure on a misaligned transaction is diluted by the firm's other transactions. |

Cross-cutting point not made into a separate reading: P3 is three-way, but P5 and P6 are stated for a binary outcome (vertical integration). Whether hybrids are coded as "not integrated" changes how P5 bears on P3 in every reading (Q7).

---

## (d) Decisions for the theorist

1. **Adopt, combine or reject readings 1, 2 and 3** (D1 to D4). D1 and D2 vary independently, so a fourth combination (selection equilibrium plus an uncertainty main effect) is available if wanted. I have not chosen among them, and `adoptedReading` is unset.
2. **Decide whether A13 is acceptable** given A1. If governance choosers are themselves boundedly rational, reading 1 needs an argument for why governance is chosen more accurately than contracts are written (Q2).
3. **Classify A5 and A9** as core or auxiliary (D3, Q12). This decides which assumptions later Interlocutor objections may target without abandoning the programme.
4. **Settle frequency (C4):** drop it, or state a relation for it (Q5).
5. **Confirm or revise A8.** Say what "fall between" means for hybrids, since the three-way P3 depends on it (Q6).
6. **Choose a coding rule for hybrids** when testing P5 and P6 against a binary integration outcome (Q7).
7. **Name an independent indicator** for comparative governance cost (C15) or for hazard (C8), or accept that both are read off asset specificity (Q8).
8. **Confirm the fact-status assignments** for P5 and P6 (provisionally novel), after historical verification (Q10).
9. **Approve, edit or reject the surfaced nodes:** A8, A10, A11, A13, A14, A15, S3, S4, P7, P8 and P9. None is in the text as given.
