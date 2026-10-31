# Mapping of Foundry roles to Project Lakatos components

*Extracted from Section 2 of the technical appendix. The Lakatos tables it cites are in `lakatos/LAKATOS_TABLES_1-4.md`.*


The six roles are not built from scratch. Each specializes and composes prior Project Lakatos components, documented in the Lakatos outline's Appendix A and reproduced in full in Annex C:

- **Table 1:** twelve routine research agents (literature review, data interpretation and specification, modeling assistance, proof verification and synthesis, summarization);
- **Table 2:** thirteen typed cognitive operators (Represent, Explain, Justify, Extend, Corroborate, Measure, Integrate, Augment, Challenge, Refute, Reduce, Assimilate, Eliminate);
- **Table 3:** the discourse grammar for epistemological stances, logics of corroboration, ontological and modeling norms, explanatory norms, justification strategies, and logical norms of inference;
- **Table 4:** seventeen classes of scholarly-role agent, intra- and inter-disciplinary.

The Foundry draws on **seventeen scholarly-role agents, one for each Table 4 class**, specified in Section 2.1. Section 2.2 maps them, with the operators, grammar and routine agents, onto each Foundry role. Section 2.3 audits coverage in the other direction.

## 2.1 The seventeen scholarly-role agents

Each agent is specified by its scope (INTRA: within the theory's own discipline; INTER: across disciplines), function, inputs, outputs, the operators and grammar categories it uses, and the Foundry roles it feeds. The core instruction is the agent's operative directive in one sentence.

| # | Agent (scope) | Function | Inputs → outputs | Operators; grammar | Feeds |
|---|---|---|---|---|---|
| L1 | **Translator / Re-Voicer** (INTER/INTRA) | Re-voices an argument, derivation or result in the terminology, inferential logic and rhetorical conventions of another disciplinary community, to expose hidden assumptions. | Argument or construct + target discipline → re-voiced statement; list of claims that do not survive re-voicing | Represent, Reduce; ontological commitments, model classes | Integrator |
| L2 | **Challenger / Interrogator** (INTRA) | Emulates the critical stance of peer reviewers in the same field: inferential validity, effect-size reliability, replicability, generalizability, relevance, informativeness. | Theory object or paper → ranked reviewer-style challenges | Challenge, Refute; logics of corroboration, logical norms | Interlocutors (own-tradition lens) |
| L3 | **Challenger / Interrogator** (INTER) | Poses cross-disciplinary challenges to ontological choices, modeling conventions and inference schemes; exposes implicit disciplinary biases. | Theory object + rival lens → ranked cross-tradition challenges | Challenge; epistemological stances, ontological commitments, model classes | Interlocutors |
| L4 | **Deconstructor** (INTRA) | Extracts the normative and descriptive statements presupposed by an argument: the background axioms and warrants that must hold for its claims to be accepted in the field. | Text → list of presupposed axioms and warrants, each tied to the claims it supports | Justify; justification norms, logical norms | Explicator (assumption set), Argument Auditor |
| L5 | **Deconstructor** (INTER) | Reconstructs what norms, regularities or premises would have to hold for a claim in one field to persuade another; maps commensurability between paradigms. | Claim + two disciplines → conditions of cross-field persuasiveness; commensurability map | Integrate, Reduce; all Table 3 categories | Integrator, Interlocutors |
| L6 | **Arbiter** (INTRA) | Evaluates descriptive, methodological and normative claims against canonical findings and accepted background results; internal auditor of coherence and rigor. | Claims → verdicts (consistent, in tension, contradicted) with the canonical finding cited | Corroborate, Refute; logics of corroboration | Argument Auditor |
| L7 | **Referee** (INTER) | Designs or identifies crucial experiments whose results both of two competing theories' traditions would regard as binding. | Two rival theories → candidate crucial experiments, with what each side would concede | Refute, Corroborate, Measure; logics of corroboration and experimentation | Empirical Validation Designer |
| L8 | **Model Expander / Contractor** (INTRA) | For a given axiomatic system, explores the consequences of adding or removing assumptions and derives the modified theory's empirical predictions; generator and critic of extensions. | Model + assumption to add or remove → modified model; derived predictions; which results survive | Augment, Explain (deductive), Extend; commitments to model classes | Model Builder |
| L9 | **Meta-Analyzer** (INTRA) | Aggregates and weights studies by effect size, reliability, reproducibility and generalizability; identifies regularities, contradictions and boundary conditions. | Body of studies → pooled estimates, heterogeneity, boundary conditions | Corroborate, Measure; logics of corroboration | Empirical Validation Designer (effect-size priors), Interlocutors (evidence) |
| L10 | **AltGen** (INTRA) | Generates competing explanations from within the same field that yield the same predictions but rest on different assumptions or mechanisms. | Empirical result + field → rival explanations with their differing assumptions | Explain (abductive), Challenge; ontological commitments | Interlocutors (own-tradition lens) |
| L11 | **AltGenX** (INTER) | Generates alternative explanations from other disciplines that predict the same regularities but imply different theoretical or practical conclusions. | Empirical result + rival discipline → cross-field rival explanation; point of practical divergence | Explain (abductive), Challenge, Assimilate; ontological commitments | Interlocutors (accommodation test) |
| L12 | **AltGenM** (INTER) | Generates explanations that rely on different model ontologies: causal replaced by teleological or functional, process re-described in network or dynamical-systems terms. | Model + target ontology → re-specified model | Represent, Explain; commitments to model classes | Explicator (alternative readings), Model Builder |
| L13 | **PrisM** (Predictive / Reflective Implication Synthesizer) (INTRA) | Derives a theory's implications for related theories of the same phenomenon in adjacent disciplines, and anticipates the questions a researcher from another field would ask. | Theory + adjacent field → implications; anticipated cross-field questions | Extend, Explain; explanatory norms | Integrator, Empirical Validation Designer |
| L14 | **ArgMap** (Argument Mapper) (INTRA) | Reconstructs informal arguments in the claim–warrant–backing scheme (about 82 canonical forms); reveals which patterns the field treats as warrantedly assertible. | Text → argument map; form instantiated by each step | Explain, Justify; logical and meta-logical norms | Argument Auditor |
| L15 | **ArgDef** (Argument Defeater) (INTRA) | Generates prima facie defeaters for claims mapped by ArgMap, using norms warranted within the same field; internal dialectical testing. | Argument map → defeaters per warrant | Challenge, Refute; logical norms | Argument Auditor |
| L16 | **ArgDef** (Cross-Field Defeater) (INTER) | Constructs defeaters warranted in another discipline that studies similar phenomena, showing how a claim valid in one field fails another's criteria. | Argument map + rival discipline → cross-field defeaters | Challenge; epistemological stances, logics of corroboration | Interlocutors |
| L17 | **RadianX** (Reasoning and Dialogue Network) (INTER/INTRA) | Builds tree-structured records of dialogues on a shared problem, tracking each assertion, clarification, question, answer and response, and evaluates moves for validity, relevance, informativeness, coherence, consistency and responsiveness. | Dialogue → move tree with evaluations | (none directly); discursive norms | Provenance Ledger (precursor), Argument Auditor (evaluation norms) |

**Core instructions (one per agent).**
L1: "Restate X so that a member of discipline D would accept it as stated in D's terms; list every element that resists restatement." L2: "Raise the objections a demanding reviewer in X's own field would raise, ranked by how likely they are to sink the paper." L3: "Raise the objections a reviewer from discipline D would raise about X's ontology, model class and inference scheme." L4: "List every statement that must be true for X's claims to be accepted in its field, and which claim each supports." L5: "State what would have to hold for claim X to persuade discipline D, and where D's norms make that impossible." L6: "Check each claim in X against the field's canonical findings and say which it agrees with, strains against or contradicts." L7: "Design an observation whose result both T1's and T2's traditions would accept as deciding between them." L8: "Add or remove assumption A from model M; derive what changes and what survives." L9: "Pool the evidence on effect E; report the estimate, its heterogeneity and its boundary conditions." L10: "Give rival explanations of result R from within its own field that predict R equally well." L11: "Give rival explanations of R from discipline D that predict R equally well but differ in what they imply." L12: "Re-specify model M using ontology O (teleological, functional, network, dynamical) and say what changes." L13: "Derive what theory T implies for related theories of the same phenomenon in field D, and the questions D would ask." L14: "Map argument X into claim, grounds, warrant, backing, qualifier and rebuttal, naming each step's canonical form." L15: "For each warrant in map X, give the strongest defeater the field itself would accept." L16: "For each warrant in map X, give the strongest defeater discipline D would accept." L17: "Record every move in dialogue X as a tree node and score it for validity, relevance, informativeness, coherence, consistency and responsiveness."

## 2.2 Role-by-role mapping

| Foundry role | Scholarly-role agents (Table 4) | Operators (Table 2) | Grammar (Table 3) | Routine agents (Table 1) | What the composition contributes |
|---|---|---|---|---|---|
| **Explicator** | L4 Deconstructor (intra); L12 AltGenM | Represent; Measure; Justify | All categories, for the stance profile | Data Specifier: Causal; Modeling Assistant: Exploratory; Exploratory Literature Review (for the theory's own canonical statements) | Represent and Measure build the construct graph; L4 supplies the presupposed assumptions that are then partitioned core/auxiliary; L12 supplies the alternative model-ontology readings that make up the formalization ensemble |
| **Interlocutors** | L3 Challenger (inter); L2 Challenger (intra, own-tradition lens); L5 Deconstructor (inter); L10 AltGen; L11 AltGenX; L16 ArgDef (cross-field) | Challenge; Refute; Corroborate | Logics of corroboration; epistemological stances; ontological commitments | Targeted Literature Review (lens corpus) | L3 and L16 give the rival tradition's objections and defeaters; L10 and L11 produce rival explanations of the same regularity, which is how accommodations are told apart from novel facts; L5 states what would have to hold for the theory to persuade the rival tradition |
| **Integrator** | L5 Deconstructor (inter); L1 Translator/Re-Voicer; L13 PrisM | Integrate; Augment; Reduce; Assimilate; Eliminate; Extend | Justification strategies (reductive, eliminative, assimilative) | Synthetic Literature Review | L5 maps commensurability; L1 pairs constructs by inferential role rather than by name and tests whether they survive re-voicing; the five integration operators define the kinds of integration and their prices; L13 derives predictions neither theory makes alone |
| **Model Builder** | L8 Model Expander/Contractor; L12 AltGenM (alternative model classes) | Represent; Explain (deductive); Augment | Commitments to model classes; logical norms | Modeling Assistant: Exploratory and Refiner; Proof Synthesizer; Proof Verifier | L8 is the engine of minimal-auxiliary search; the proof agents construct and check derivations; the model-class commitments constrain which formalisms are admissible |
| **Argument Auditor** | L14 ArgMap; L15 ArgDef (intra); L6 Arbiter (intra); L4 Deconstructor (intra); L17 RadianX (evaluation norms) | Explain (inferential logic L); Justify | Logical and meta-logical norms of inference | (none) | L14 maps the argument, now applied to the theorist's own exposition; Explain(X,Y;L) classifies each step as deductive, inductive or abductive, which detects deductive language covering abductive moves; L15 and L6 test warrants against the field's own norms and findings |
| **Empirical Validation Designer** | L7 Referee (inter); L9 Meta-Analyzer; L13 PrisM | Measure; Corroborate; Refute | Logics of corroboration; logics of experimentation | Data Specifier: Causal; Data Interpreter: Inferential and Causal; Targeted Literature Review | L7 designs crucial experiments binding on both sides, the heart of the severity report; L9 supplies effect-size priors for power analysis; the routine data agents, redirected from analyzing existing data to designing new identified tests, supply identification strategies |
| **Provenance Ledger** | L17 RadianX | (none) | (none) | (none) | RadianX's dialogue tree is generalized to every transformation of the theory object, with human decisions and hash-chaining added |

## 2.3 Coverage audit

Every Table 4 agent class and every Table 2 operator is used by at least one Foundry role.

| Lakatos component | Used by |
|---|---|
| L1 Translator/Re-Voicer | Integrator |
| L2 Challenger (intra) | Interlocutors |
| L3 Challenger (inter) | Interlocutors |
| L4 Deconstructor (intra) | Explicator, Argument Auditor |
| L5 Deconstructor (inter) | Integrator, Interlocutors |
| L6 Arbiter | Argument Auditor |
| L7 Referee | Empirical Validation Designer |
| L8 Model Expander/Contractor | Model Builder |
| L9 Meta-Analyzer | Empirical Validation Designer |
| L10 AltGen | Interlocutors |
| L11 AltGenX | Interlocutors |
| L12 AltGenM | Explicator, Model Builder |
| L13 PrisM | Integrator, Empirical Validation Designer |
| L14 ArgMap | Argument Auditor |
| L15 ArgDef (intra) | Argument Auditor |
| L16 ArgDef (cross-field) | Interlocutors |
| L17 RadianX | Provenance Ledger, Argument Auditor |
| Represent | Explicator, Model Builder |
| Explain | Model Builder, Argument Auditor |
| Justify | Explicator, Argument Auditor |
| Extend | Integrator |
| Corroborate | Interlocutors, Empirical Validation Designer |
| Measure | Explicator, Empirical Validation Designer |
| Integrate, Reduce, Assimilate, Eliminate | Integrator |
| Augment | Integrator, Model Builder |
| Challenge, Refute | Interlocutors (Refute also Empirical Validation Designer) |

Of the twelve routine agents, ten are used inside roles. The **Summarizer/Conclusion Builder** is deliberately not used: the Foundry ends at a specified theory and its test designs, before the writing-up stage that agent serves. **Data Interpreter: Descriptive** is held in reserve for the Stage 1 validation studies rather than used inside a role.

