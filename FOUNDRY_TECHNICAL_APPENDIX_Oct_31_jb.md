# Technical Appendix: Theory and Model Foundry

*Supplement to the Stage 1 proposal, "Theory and Model Foundry," submitted to the Organization Science Special Issue: AI-Enabled Frontiers in Organizational Science. This appendix provides the full agent-role specifications, the seventeen scholarly-role agents from which the roles are composed and the mapping between them, the instruction sets for each role, worked transcripts demonstrating each role's current behavior, and the draft theory-object schema. It supersedes the compressed descriptions in the proposal itself, which reference this document. The accompanying repository is at https://github.com/appendix-repo/theory-and-model-foundry; file paths given in this appendix (for example `runs/` and `schema/`) are relative to it.*

**Contents**

0. Reading guide and glossary
1. Agent role specifications (1.1 to 1.7), Interlocutor lenses (1.8), the orchestration loop (1.9)
2. Foundations in Project Lakatos: the seventeen scholarly-role agents (2.1), role-by-role mapping (2.2), coverage audit (2.3)
3. Worked transcripts (runs 01 to 08 and the Provenance Ledger trace)
4. Theory-object schema (draft v0) and the measured quantities
5. Validation protocols
6. Status of components: built, specified, to be built in Stage 1

References · Annex A: full schema and JSON-LD context · Annex B: full transcripts of Runs 01 to 08, case inputs, and the Ledger trace · Annex C: Project Lakatos Tables 1 to 4

*The body (Sections 0 to 6 and References) is about 10,500 words; Annex B carries the complete, unedited transcripts and is long by design.*

---

## 0. Reading guide and glossary

The Foundry has **six agent roles** (Explicator, Interlocutors, Integrator, Model Builder, Argument Auditor, Empirical Validation Designer) and **one record-keeping component**, the Provenance Ledger, which is not an agent. Together these are the seven components of the Foundry. The roles are not new agents built from scratch: each is an instruction set that *composes* already-specified Project Lakatos components, namely the thirteen cognitive operators (Lakatos Appendix A, Table 2), the discourse grammar (Table 3), the twelve routine research agents (Table 1), and seventeen scholarly-role agents, one for each class in Table 4. All four tables are reproduced in Annex C.

| Term | Meaning in this appendix |
|---|---|
| Theory object | A typed graph of constructs, relations, mechanisms, assumptions, scope conditions, propositions and derivations, in which each construct carries an inferential role. Serialized as JSON-LD (Section 4). |
| Inferential role | Following Brandom (1994, 2000): what asserting that a construct applies *commits* the theorist to, what would *entitle* the theorist to assert it, what it *licenses* others to infer, and what it *precludes*. |
| Core and auxiliary assumptions | Following Lakatos (1970): the *hard core* whose abandonment abandons the research programme, and the *protective belt* of auxiliaries modified to absorb anomalies. |
| Novel fact and accommodation | A prediction the theory made before (or independently of) the evidence, versus a known fact the theory was fitted to (Lakatos 1970). |
| Formalization ensemble | The set of candidate theory objects the Explicator returns when the prose underdetermines a single reading, together with their dispersion. |
| Bridge, rivalry, complementarity, equivocation | The four relations the Integrator assigns between constructs of different theories: same licensed inferences; conflicting entitlements; one theory's commitment discharges another's open assumption; shared vocabulary with different roles. |
| Inferential price | What an integration requires each tradition to give up or newly assume. |
| Severity | Following Mayo (2018): a test is severe for a claim if, were the claim false, the test would very probably have produced a result that disagrees with it. |
| Lens | The profile of a rival theoretical tradition, stated in the categories of the Project Lakatos discourse grammar (Table 3: epistemological stance, logic of corroboration, ontological commitments, model class, explanatory norm, justification strategy) plus a canonical corpus, that parameterizes one Interlocutor. |

---

## 1. Agent role specifications

The Foundry is orchestrated around a human theorist who accepts, rejects, or modifies every consequential move. Each role below is specified on a common template: function; epistemological grounding; inputs and outputs, typed against the schema in Section 4; composition from Project Lakatos components; human decision points; failure modes and safeguards; and evaluation. The full instruction sets (current version v0.2) are in `instruction-sets/FOUNDRY_ROLE_INSTRUCTION_SETS.md` in the accompanying repository and are reproduced in substance here.

### 1.1 The Explicator

**Function.** Converts prose theory into a candidate theory object: typed constructs (each carrying its measurement commitments and its material-inferential role, meaning what it licenses and precludes), directed relations, proposed mechanisms, and a partition of assumptions into core and auxiliary. Because prose typically underdetermines its formalization, the Explicator returns *multiple* candidate inferential-role assignments rather than a single reading.

**Grounding.** Brandom's inferentialism (a construct's content is its inferential role) and Price's global expressivism (we ask what work a vocabulary does, not what it mirrors), which licenses representing constructs from any tradition in one format without first settling whose ontology is fundamental. The core/auxiliary partition is Lakatos's.

**Inputs.** Prose exposition (a paper, a section, a theorist's notes); optionally the theorist's own glossary.
**Outputs.** A `FormalizationEnsemble` of two or more `TheoryObject`s; a table of pivotal differences between readings; a `StanceProfile` in the Table 3 grammar; a list of open questions.

**Composition.** *Represent(X,Y)* produces the typed construct graph; *Measure(X,Y;M)* attaches measurement commitments; *Justify(X,Y)* records why each assumption is classed core or auxiliary. The **Deconstructor (intra)** extracts the presupposed background axioms and warrants that populate the assumption set. **AltGenM** generates the alternative model-ontology readings (e.g., causal versus selection-based) that become further members of the ensemble. The routine **Data Specifier: Causal** and **Modeling Assistant: Exploratory** agents supply the variable typing and relation forms. The Table 3 grammar supplies the stance-profile vocabulary.

**Human decision points.** Which reading the theorist adopts as theirs (or that several remain live); every reclassification of an assumption between core and auxiliary; acceptance of any surfaced implicit assumption. All are Ledger events.

**Failure mode and safeguard.** *Formalization degeneracy*: laundering one arbitrary reading into apparent precision. The Explicator is required to return an ensemble where the text underdetermines a reading, never to choose, and the ensemble's dispersion is reported as a quantity (Section 4.3).

**Evaluation.** Inter-team agreement on theory objects in the N ≈ 25 to 30 theory study (Section 5.2); specification completeness of the adopted reading.

### 1.2 The Interlocutors

**Function.** Adversarial agents instantiating rival theoretical lenses (transaction-cost, behavioral, institutional, evolutionary, and network), each grounded in a curated corpus and each with its own inferential commitments. Each probes the theory object for what its tradition would dispute: unentitled commitments, constructs doing tautological work, predictions that are accommodations rather than novel facts (Lakatos 1970), disputed ontology and model class, and refuting evidence.

**Grounding.** Lakatos's methodology of scientific research programmes, which judges a programme progressive only if it predicts novel facts, and his view that theories are appraised against rivals, not in isolation. The voice-of-a-tradition requirement draws on Moldoveanu and Baum's (2014) account of interactive epistemic inference within small research networks: an objection lands when it is recognizably the move a member of the rival network would make.

**Inputs.** A theory object (the adopted reading or the whole ensemble); a lens specification (Section 1.8).
**Outputs.** Per lens, a ranked list of objections, each with type, target ids, statement in the tradition's voice, strength (fatal to the core, damaging, minor) and what would answer it; the lens's rival explanation of the theory's key regularities.

**Composition.** The **Challenger/Interrogator (inter)** supplies the cross-tradition challenges to ontology, model class and inference scheme; the **Challenger/Interrogator (intra)** supplies the reviewer-style challenges on validity, replicability and generalizability when the lens is the theory's own tradition. The **Deconstructor (inter)** reconstructs what would have to hold for the claim to persuade the rival tradition. **AltGenX** and **AltGen** generate the rival explanations of the same regularity that expose accommodations. The **ArgDef (cross-field)** constructs defeaters warranted by the rival tradition's own norms. Operators: *Challenge(X,Y)*, *Refute(X,Y)*, *Corroborate(X,Y)* (to test whether the rival corroborates equally). The **Targeted Literature Review** routine agent grounds refuting evidence in the lens corpus. The Table 3 logics of corroboration set each lens's evidential standard.

**Human decision points.** Which objections the theorist accepts, rejects (with reasons) or answers by modifying the theory object; each response is linked to the objection in the Ledger.

**Failure mode and safeguard.** *Sycophancy and objection theater*: fluent but toothless critique that misses the load-bearing claims and inferential steps, or drift toward agreement. Safeguards: the instruction set forbids concession and requires ranked strength; objections must cite target ids; tournament-style selection keeps the strongest objections across repeated runs; and the retrospective-validity benchmark (Section 5.1) checks whether objections recover the real critical record.

**Evaluation.** Retrospective recovery of at least 80% of a theory's major published critiques, together with a pre-registered lens increment over the no-lens baseline (Section 5.1); discovery of substantive gaps absent from the published record, judged blind by domain experts.

### 1.3 The Integrator

**Function.** Given two or more theory objects, aligns their constructs' inferential roles and returns a map of the relations between them: where they license the same inferences (bridges), where their entitlements conflict (genuine rivalry), where one theory's commitments discharge another's open assumptions (complementarity), and where shared vocabulary hides different roles (equivocation). Proposes candidate integrated theory objects and states the inferential price each integration pays.

**Grounding.** Commensurability as a matter of degree: two theories are commensurable exactly to the extent that their constructs' inferential roles can be mapped onto each other. This replaces the Kuhnian treatment of incommensurability as a barrier with an auditable operation on inferential-role structures.

**Inputs.** Two or more theory objects.
**Outputs.** An `AlignmentMap` (Section 4), with a basis for every link; results of a substitution test on every claimed bridge; at most two candidate integrated theory objects, each with its operator and inferential price; one cross-theory prediction per integration that neither theory makes alone.

**Composition.** The integration operators *Integrate*, *Augment*, *Reduce*, *Assimilate* and *Eliminate* (and *Extend* for scope extension) define the kinds of integration on offer; the Table 3 justification strategies (reductive, eliminative, assimilative) name them in the traditions' own terms. The **Deconstructor (inter)**, whose Lakatos use case is "mapping commensurability between paradigms," does the alignment. The **Translator/Re-Voicer** restates each construct's licensed inferences in a neutral vocabulary so that constructs are paired by role, not by name, and tests whether a construct survives re-voicing into the other discipline. **PrisM** derives the cross-theory predictions.

**Human decision points.** Which bridges and conflicts the theorist accepts as real; whether to pursue a candidate integration, and at what price.

**Failure mode and safeguard.** *Spurious integration*: manufacturing bridges between theories that share only surface vocabulary. A bridge is a claim about shared inferential role and must pass the substitution test; failing pairs are reported as equivocations, not bridges. Expert adjudication of bridges as real or forced is part of validation.

**Evaluation.** In the integration demonstrations (transaction-cost and resource-dependence accounts of firm boundaries; institutional and evolutionary accounts of change), domain experts judge whether surfaced bridges and conflicts are real and previously under-articulated.

### 1.4 The Model Builder

**Function.** Translates a theory object into machine-executable form (for example agent-based simulation, structural model, or game-theoretic specification) and attempts to *derive* the theory's claimed propositions rather than assert them. Where derivations fail to close, surfaces the minimal auxiliary assumptions required, making hidden assumption load explicit.

**Grounding.** Morgan's (2012) account of models as instruments of inquiry, and the principle that a proposition is part of a theory's content only if it follows from the theory: "the language model proposes, the backend disposes."

**Inputs.** A theory object (the adopted reading).
**Outputs.** An `ExecutableModel` specification with a construct-to-variable map; a derivation table (target, premises, method, status, auxiliaries required); surfaced assumptions added to the theory object with status `surfaced`; checker-ready statements of each derivation.

**Composition.** The **Model Expander/Contractor** is the core: it adds and removes assumptions and derives the consequences, which is exactly the search for minimal auxiliaries. The routine **Modeling Assistant: Exploratory** and **Refiner** agents build and tune the model; the **Proof Synthesizer** constructs derivations or counter-examples; the **Proof Verifier** checks them. Operators: *Represent(X,Y)* into the chosen formal class, *Explain(X,Y;L)* with L deductive, *Augment(X,Y)* when auxiliaries are added. The Table 3 commitments to model classes constrain which formal class is admissible for the theory's tradition.

**Human decision points.** Choice of model class; acceptance of each surfaced auxiliary as part of the theory, or rejection (leaving the derivation open on the record).

**Failure mode and safeguard.** *Spurious derivation claims.* The Model Builder may only mark a derivation `asserted`; it becomes `closed` only when a symbolic checker or executable simulation verifies it. **The checking backend is Stage 1 work** (Section 6); in the transcripts below every derivation status is therefore `asserted` or `open`, never `closed`.

**Evaluation.** Derivational tightness and assumption load (Section 4.3) before and after the Model Builder's pass; checker agreement with its claimed derivations once the backend exists.

### 1.5 The Argument Auditor

**Function.** Maps the argumentative structure (Toulmin 1958) of the theorist's exposition (claims, grounds, warrants, backing, qualifiers and rebuttals) and identifies warrant gaps and points where deductive language covers abductive or inductive moves. Generates defeaters for each warrant from within the theorist's own field.

**Grounding.** Toulmin's argument scheme and the field-dependence of warrants: what counts as a warrant without further justification differs across disciplines, which is why the Auditor judges warrants by the theorist's own field's norms. Other argument schemes can replace Toulmin's, and schemes for classifying arguments can be added.

**Inputs.** The theorist's prose exposition and its theory object.
**Outputs.** An argument map; a list of warrant gaps with the missing warrant stated; a list of inference-mode mismatches; one intra-field defeater per warrant; claims in tension with canonical findings.

**Composition.** **ArgMap** reconstructs the arguments using its library of canonical claim–warrant–backing forms, here applied to the theorist's own exposition rather than a rival's. **ArgDef (intra)** generates the defeaters. **Arbiter (intra)** checks claims against canonical findings. **RadianX**'s discursive norms (validity, relevance, informativeness, coherence, consistency) supply the evaluation criteria. Operators: *Explain(X,Y;L)* to classify each step's inferential logic L as deductive, inductive or abductive; *Justify(X,Y)* for normative claims. The Table 3 logical and meta-logical norms set the field's standard.

**Human decision points.** Which gaps the theorist closes (by adding a warrant, which then enters the theory object as an assumption), hedges (by changing the qualifier), or contests.

**Failure mode and safeguard.** Pedantry: flagging every enthymeme as a gap. The Auditor ranks gaps by whether the missing warrant is contested in the field.

**Evaluation.** Blind expert rating of argumentative soundness in the prospective value-in-use study (Section 5.3).

### 1.6 The Empirical Validation Designer

**Function.** Extracts the theory's *risky* predictions, those on which it diverges from its rivals as represented by the Interlocutors, and maps them to feasible designs with identification strategy and power analysis, producing a severity report in Mayo's (2018) sense: which designs would discriminate this theory from its competitors, and which would merely be consistent with it.

**Grounding.** Mayo's severe-testing account, and the Lakatosian point that a test matters when the theory and its rivals predict differently.

**Inputs.** A theory object; the Interlocutors' rival explanations; any AlignmentMap rivalries.
**Outputs.** A risky-prediction table (theory prediction, rival prediction, observable); for each, a design with identification strategy, main threat to validity, and indicative power with its effect-size prior; a severity ranking; a crucial-experiment check.

**Composition.** The **Referee (inter)** designs the "crucial experiments" whose results both sides would regard as binding. The **Meta-Analyzer** supplies effect-size priors and known boundary conditions for power analysis. **PrisM** contributes predictions in adjacent disciplines that can serve as additional discriminating observables. The routine **Data Specifier: Causal**, **Data Interpreter: Inferential** and **Data Interpreter: Causal** agents, redirected from analyzing existing data to designing new identified tests, supply identification strategies; the **Targeted Literature Review** finds candidate data sources. Operators: *Measure(X,Y;M)*, *Corroborate(X,Y)*, *Refute(X,Y)*. The logics of corroboration and experimentation in Table 3 and the Lakatos synopsis (fixed and random effects; variation in stimulus as well as subjects) shape the designs.

**Human decision points.** Which designs to pursue; acceptance of measurement choices as fair to both traditions.

**Failure mode and safeguard.** Proposing designs that are merely consistent with the theory. Every design must state what a rival predicts under it; designs without a divergent rival prediction are reported as low-severity.

**Evaluation.** Blind expert rating of testability in the prospective study; expert judgment of whether the top-ranked design would in fact discriminate.

### 1.7 The Provenance Ledger

**Function.** Records every transformation, agent proposal, and human decision as an append-only, hash-chained trace, so that the human and machine division of labor in any Foundry-assisted theorizing session is a matter of inspectable record rather than a disclosure statement.

**Grounding.** The proposal's response to the call's concern with "Potemkin villages of slop" (Organization Science 2026); and the program's aim of making theory development an empirical domain, which requires that its intermediate products be recorded.

**Record.** Each `LedgerEvent` (Section 4) carries a timestamp, actor (human, agent or checker, with model and instruction-set version), action (ingest, propose, accept, reject, modify, derive, challenge, align, design, annotate), input and output node ids, the event it responds to, a rationale, and the previous event's hash.

**Composition.** **RadianX**, which builds tree-structured records of dialogues tracking each assertion, question, answer and response, is the Lakatos precursor; the Ledger generalizes RadianX's dialogue tree from conversational moves to all transformations of a theory object, and adds human decisions and hash-chaining.

**Status.** Specified (schema in Section 4); implementation is Stage 1 work. Section 3.8 gives the Ledger trace that the worked runs in this appendix would produce.

### 1.8 Interlocutor lenses

Each Interlocutor is one instance of a shared instruction set (Section 1.2) parameterized by a lens. Every lens is profiled in the six categories of the Project Lakatos discourse grammar (Table 3, reproduced in Annex C), using that grammar's own terms, and grounded in a curated corpus. The defaults are:

| Lens | Epistemological stance | Logic of corroboration | Ontological commitments | Model class | Explanatory norm | Justification strategy | Canonical corpus |
|---|---|---|---|---|---|---|---|
| Transaction-cost | Positivism (lay form) | Falsificationism (sophisticated) | Transactions; governance structures; boundedly rational, opportunistic agents | Teleological (comparative statics of discriminating alignment) | Coverage (parsimony) | Assimilative | Coase 1937; Williamson 1975, 1985, 1991; Klein, Crawford & Alchian 1978; Monteverde & Teece 1982; Masten 1984 |
| Behavioral | Positivism (lay form) | Inductivism | Boundedly rational decision makers; aspiration levels; routines; coalitions | Causal (process and simulation models) | Depth | Reductive (to decision processes) | Simon 1947, 1955; March & Simon 1958; Cyert & March 1963; Kahneman & Tversky 1979; Greve 2003 |
| Institutional | Constructivism | Inductivism (comparative-historical) | Organizational fields; institutional logics; legitimacy; taken-for-granted scripts | Functional | Coverage | Assimilative | Meyer & Rowan 1977; DiMaggio & Powell 1983; Scott 1995; Thornton, Ocasio & Lounsbury 2012 |
| Evolutionary | Realism (metaphysical form) | Falsificationism (methodological) | Routines; populations; variation, selection and retention | Causal (selection dynamics) | Coverage (parsimony) | Reductive (to selection) | Nelson & Winter 1982; Hannan & Freeman 1977, 1984; Aldrich 1999; Carroll & Hannan 2000 |
| Network | Realism (metaphysical form) | Inductivism | Networks of ties and positions; structural holes; embeddedness | Causal (relational) | Coverage | Reductive (to structure) | Granovetter 1985; Burt 1992; Gulati 1995; Uzzi 1997; Podolny 2001 |

Two lenses can share a category value and still differ: the transaction-cost and behavioral lenses are both positivist in the lay sense, and part company on corroboration logic, model class and justification strategy. The table states each lens's *default* profile; a lens's own members dispute some entries (for example, whether transaction-cost economics is better read as instrumentalist), and the theorist can override any cell.

*Version note.* Runs 03 and 04 (Section 3.2) used instruction set v0.1, whose lens table described the same profiles in looser wording ("lay positivism; comparative-institutional realism", "positivism with process realism", "structural realism", and so on) that did not keep to the Table 3 vocabulary. This table (instruction set v0.2) restates each profile in the grammar's own terms and adds the explanatory-norm and justification-strategy categories. The substance of the two lenses used in the runs is unchanged. v0.1 is preserved in the repository as `instruction-sets/FOUNDRY_ROLE_INSTRUCTION_SETS_v0.1.md`.

**Lenses are pluggable.** A new lens is admitted by filling one row of this table, supplying a curated corpus of at least ten works, and passing the retrospective-validity check (Section 5.1) on two theories its tradition has criticized in print. This is the architectural answer to the homogenization risk: the interlocutor set is a contested, extensible commons, not a canon of five.

### 1.9 The orchestration loop

The roles are bound into a loop under continuous human direction. The diagram shows the default order; the theorist can invoke any role at any point, and every arrow is a Ledger event.

```
 prose ──► [1 Explicator] ──► ensemble ──► THEORIST adopts reading(s)
                                                │
              ┌─────────────────────────────────┼──────────────────────────┐
              ▼                                 ▼                          ▼
     [2 Interlocutors ×5]              [5 Argument Auditor]        [4 Model Builder]
     objections, rival                 warrant gaps,               derivations,
     explanations                      mode mismatches             surfaced auxiliaries
              │                                 │                          │
              └──────────────► THEORIST accepts / rejects / modifies ◄─────┘
                                                │   (loop back to 1 if the
                                                │    theory object changes)
                     second theory object? ─────┤
                                                ▼
                                       [3 Integrator]
                                       alignment map, integrations
                                                │
                                                ▼
                                [6 Empirical Validation Designer]
                                risky predictions, severity report
                                                │
                                                ▼
                                THEORIST selects designs ──► [Ledger: full trace]
```

**Gates.** Three gates require an explicit human decision before the loop proceeds: adoption of a reading after the Explicator; disposition of every objection, gap and surfaced assumption ranked "fatal" or "damaging"; and selection of designs. Undecided items remain open in the theory object and are counted in its metrics.

**Status.** The roles are specified as instruction sets and exercised individually and in sequence (Section 3). The orchestration software that binds them, routes theory objects between them and writes the Ledger is Stage 1 work.


---

## 2. Foundations in Project Lakatos

The six roles are not built from scratch. Each specializes and composes prior Project Lakatos components, documented in the Lakatos outline's Appendix A and reproduced in full in Annex C:

- **Table 1:** twelve routine research agents (literature review, data interpretation and specification, modeling assistance, proof verification and synthesis, summarization);
- **Table 2:** thirteen typed cognitive operators (Represent, Explain, Justify, Extend, Corroborate, Measure, Integrate, Augment, Challenge, Refute, Reduce, Assimilate, Eliminate);
- **Table 3:** the discourse grammar for epistemological stances, logics of corroboration, ontological and modeling norms, explanatory norms, justification strategies, and logical norms of inference;
- **Table 4:** seventeen classes of scholarly-role agent, intra- and inter-disciplinary.

The Foundry draws on **seventeen scholarly-role agents, one for each Table 4 class**, specified in Section 2.1. Section 2.2 maps them, with the operators, grammar and routine agents, onto each Foundry role. Section 2.3 audits coverage in the other direction.

### 2.1 The seventeen scholarly-role agents

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

### 2.2 Role-by-role mapping

| Foundry role | Scholarly-role agents (Table 4) | Operators (Table 2) | Grammar (Table 3) | Routine agents (Table 1) | What the composition contributes |
|---|---|---|---|---|---|
| **Explicator** | L4 Deconstructor (intra); L12 AltGenM | Represent; Measure; Justify | All categories, for the stance profile | Data Specifier: Causal; Modeling Assistant: Exploratory; Exploratory Literature Review (for the theory's own canonical statements) | Represent and Measure build the construct graph; L4 supplies the presupposed assumptions that are then partitioned core/auxiliary; L12 supplies the alternative model-ontology readings that make up the formalization ensemble |
| **Interlocutors** | L3 Challenger (inter); L2 Challenger (intra, own-tradition lens); L5 Deconstructor (inter); L10 AltGen; L11 AltGenX; L16 ArgDef (cross-field) | Challenge; Refute; Corroborate | Logics of corroboration; epistemological stances; ontological commitments | Targeted Literature Review (lens corpus) | L3 and L16 give the rival tradition's objections and defeaters; L10 and L11 produce rival explanations of the same regularity, which is how accommodations are told apart from novel facts; L5 states what would have to hold for the theory to persuade the rival tradition |
| **Integrator** | L5 Deconstructor (inter); L1 Translator/Re-Voicer; L13 PrisM | Integrate; Augment; Reduce; Assimilate; Eliminate; Extend | Justification strategies (reductive, eliminative, assimilative) | Synthetic Literature Review | L5 maps commensurability; L1 pairs constructs by inferential role rather than by name and tests whether they survive re-voicing; the five integration operators define the kinds of integration and their prices; L13 derives predictions neither theory makes alone |
| **Model Builder** | L8 Model Expander/Contractor; L12 AltGenM (alternative model classes) | Represent; Explain (deductive); Augment | Commitments to model classes; logical norms | Modeling Assistant: Exploratory and Refiner; Proof Synthesizer; Proof Verifier | L8 is the engine of minimal-auxiliary search; the proof agents construct and check derivations; the model-class commitments constrain which formalisms are admissible |
| **Argument Auditor** | L14 ArgMap; L15 ArgDef (intra); L6 Arbiter (intra); L4 Deconstructor (intra); L17 RadianX (evaluation norms) | Explain (inferential logic L); Justify | Logical and meta-logical norms of inference | (none) | L14 maps the argument, now applied to the theorist's own exposition; Explain(X,Y;L) classifies each step as deductive, inductive or abductive, which detects deductive language covering abductive moves; L15 and L6 test warrants against the field's own norms and findings |
| **Empirical Validation Designer** | L7 Referee (inter); L9 Meta-Analyzer; L13 PrisM | Measure; Corroborate; Refute | Logics of corroboration; logics of experimentation | Data Specifier: Causal; Data Interpreter: Inferential and Causal; Targeted Literature Review | L7 designs crucial experiments binding on both sides, the heart of the severity report; L9 supplies effect-size priors for power analysis; the routine data agents, redirected from analyzing existing data to designing new identified tests, supply identification strategies |
| **Provenance Ledger** | L17 RadianX | (none) | (none) | (none) | RadianX's dialogue tree is generalized to every transformation of the theory object, with human decisions and hash-chaining added |

### 2.3 Coverage audit

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

---

## 3. Worked transcripts

### 3.0 How these runs were produced

The transcripts are genuine runs of the six instruction sets at version v0.1 (`instruction-sets/FOUNDRY_ROLE_INSTRUCTION_SETS_v0.1.md`), produced on 10 October 2026. The current version, v0.2, differs only in the wording of the lens table (Section 1.8). Each run was executed by a separate instance of Claude (Anthropic), given only the common preamble, its own role's instruction set, the schema, and its inputs. Runs are single and unedited; no run was repeated or selected from several. The full transcripts are reproduced in Annex B and are in the repository under `runs/`.

**The case.** The inputs are two short prose expositions written for this demonstration as faithful paraphrases of canonical statements: **Input A**, the transaction-cost theory of firm boundaries (after Williamson 1975, 1985, 1991); and **Input B**, the resource-dependence theory of organizational boundaries (after Pfeffer & Salancik 1978; Casciaro & Piskorski 2005). This is one of the standing integration problems named in Section 3 of the proposal. Both inputs are in Annex B.0.

**The sequence.** The runs follow the orchestration loop of Section 1.9:

| Run | Role | Input | Output |
|---|---|---|---|
| 01 | Explicator | Input A | TCE formalization ensemble (3 readings) |
| 02 | Explicator | Input B | RD formalization ensemble (3 readings) |
| *gate* | *Adoption of reading 1 of each* | | *see note below* |
| 03 | Interlocutor, institutional lens | TCE reading 1 | 10 ranked objections; rival explanation |
| 04 | Interlocutor, behavioral lens | TCE reading 1 | 9 ranked objections; rival explanation |
| 05 | Model Builder | TCE reading 1 | Model; 11 derivation attempts; surfaced assumptions |
| 06 | Argument Auditor | Input A + TCE reading 1 | Argument map; 11 warrant gaps |
| 07 | Integrator | TCE reading 1 + RD reading 1 | AlignmentMap; 2 candidate integrations |
| 08 | Empirical Validation Designer | TCE reading 1 + rivals from 02, 03, 04 | 7 risky predictions; 7 designs; severity ranking |
| 09 | Provenance Ledger | all of the above | 11 hash-chained events |

**Who passed the gate.** In real use every gate is a human decision. In this demonstration **no human passed the reading-adoption gate: Claude stood in for the human theorist** and adopted reading 1 of each theory so that the sequence could proceed. The Ledger records this as such (event 5, actor "demonstration operator (Claude), standing in for the human theorist"), and `adoptedReading` is left unset in both ensembles. The demonstration therefore shows the roles' behavior, not the human direction the Foundry is built around. The decisions each run returns to the theorist are reproduced in the transcripts but were not acted on.

**Limits.** No derivation is marked `closed`, because the checking backend is Stage 1 work (Section 6). Literature citations the agents were not certain of are marked "(to verify)" in the transcripts; they are left unedited there and checked in the table below. Statements of probability in the severity report (Run 08) are the agent's judgments, flagged as such.

**Citation verification.** The transcripts carry the agents' own "(to verify)" flags and are left unedited. The table below checks every work so flagged, on two counts: whether the bibliographic details are correct, and whether the work says what the transcript uses it for. **Basis:** checked by Claude (Anthropic) against the published record on 23 October 2026: bibliographic details, and each work's abstract and main findings. For the three works marked †, the publisher's abstract or a secondary summary was consulted online. A row marked *Partly* means the citation is real and relevant but the transcript overstates or simplifies it; the correction is given. Priors and magnitudes the agents *chose* (marked "(assumption)" in Run 08) are not citations and are not verified here.

| Work | Run(s) | Reference | Use in the transcript | Verdict |
|---|---|---|---|---|
| Alchian 1950 | 06 | *Journal of Political Economy* 58(3), 211–221 | Selection does not guarantee optimality | Supported |
| Alfaro, Conconi, Fadinger & Newman 2016 | 08 | *Review of Economic Studies* 83(3), 855–888 | Output prices affect integration | Supported |
| Argyres 1996 † | 04 | *Strategic Management Journal* 17(2), 129–150 | Make-or-buy driven "by relative capabilities more than by hazard" | *Partly.* Asset specificity alone was decisive in some decisions, capabilities or combinations in others; "more than" overstates |
| Baker, Gibbons & Murphy 2002 | 06 | *Quarterly Journal of Economics* 117(1), 39–84 | Relational contracts sustain cooperation without integration | Supported |
| Balakrishnan & Wernerfelt 1986 | 06 | *Strategic Management Journal* 7(4), 347–359 | Technological change lowers the attraction of integration | Supported |
| Boehm, Flaaen & Pandalai-Nayar 2019 | 08 | *Review of Economics and Statistics* 101(1), 60–75 | Supplier-link data after the 2011 Tōhoku earthquake | Supported (data are US affiliates of Japanese multinationals) |
| Carvalho, Nirei, Saito & Tahbaz-Salehi 2021 | 08 | *Quarterly Journal of Economics* 136(2), 1255–1321 | Firm-level supplier links after the 2011 earthquake | Supported |
| Casciaro & Piskorski 2005 † | 02, 07, 08 | *Administrative Science Quarterly* 50(2), 167–199 | Mutual dependence promotes, imbalance hinders, M&A; inter-industry dependence indexed with input-output data | Supported on the findings. The 0.80 rate ratio in Run 08 is the agent's assumption, not an estimate from the paper |
| Coase 2000 | 03 | *Journal of Law and Economics* 43(1), 15–31 | GM was not held up by Fisher Body; the acquisition brought the Fisher brothers into GM | Supported |
| David & Han 2004 | 04 | *Strategic Management Journal* 25(1), 39–58 | Empirical support for the uncertainty predictions is mixed | Supported |
| Dyer 1996 | 03, 08 | *Strategic Management Journal* 17(4), 271–291 | Japanese automaker supplier networks with dedicated assets under hybrid governance | Supported |
| Freeland 2000 | 03 | *Journal of Law and Economics* 43(1), 33–66 | No pre-merger hold-up; integration retained the Fishers' human capital | Supported |
| Ghoshal & Moran 1996 | 04, 06 | *Academy of Management Review* 21(1), 13–47 | Assuming opportunism and governing for it can produce it | Supported |
| Grossman & Hart 1986 | 06, 07 | *Journal of Political Economy* 94(4), 691–719 | Integration reallocates residual control rights rather than removing hold-up | Supported |
| Hsieh, Bloch & Larsen 1998 | 08 | *Statistics in Medicine* 17(14), 1623–1634 | Sample-size formula for logistic regression with variance inflation | Supported. The inflation factor is 1/(1 − ρ²); Run 08's 1/(1 − 0.30) treats 0.30 as the squared multiple correlation |
| Jensen 1986 | 06 | *American Economic Review* 76(2), 323–329 | Managers use free cash flow for empire-building | Supported |
| Joskow 1987 | 06 | *American Economic Review* 77(1), 168–185 | Contract duration rises with relationship-specific investment | Supported |
| Kahneman, Knetsch & Thaler 1986 | 04 | *American Economic Review* 76(4), 728–741 | Exploiting a shift in bargaining power is judged unfair, and punished | *Partly.* The AER paper reports fairness judgments; the punishment evidence is in the authors' companion paper (*Journal of Business* 59(4), S285–S300, 1986) |
| Klein & Leffler 1981 | 06 | *Journal of Political Economy* 89(4), 615–641 | Reputational premia assure performance | Supported |
| Klein, Crawford & Alchian 1978 | 03, 06 | *Journal of Law and Economics* 21(2), 297–326 | Appropriable quasi-rents; GM–Fisher Body as the hold-up case | Supported |
| Lafontaine & Slade 2007 | 06, 08 | *Journal of Economic Literature* 45(3), 629–685 | Positive specificity effects; endogeneity and measurement problems | Supported |
| Macaulay 1963 | 06 | *American Sociological Review* 28(1), 55–67 | Non-contractual relations in business | Supported |
| Macher & Richman 2008 | 06, 08 | *Business and Politics* 10(1), 1–63 | Review of empirical TCE: consistent positive specificity effects | Supported |
| Masten 1984 | 01 | *Journal of Law and Economics* 27(2), 403–417 | Historical priority of P5 | Supported: the test postdates Williamson (1975), consistent with P5's provisional "novel" status |
| Ménard 2004 | 06 | *Journal of Institutional and Theoretical Economics* 160(3), 345–376 | Hybrids have distinct governance mechanisms | Supported |
| Milgrom & Roberts 1988 | 06 | *American Journal of Sociology* 94 (Suppl.), S154–S179 | Influence activities as a cost of hierarchy | Supported |
| Monteverde & Teece 1982 | 01, 04, 08 | *Bell Journal of Economics* 13(1), 206–213 | Priority of P5; engineering-effort measure possibly a consequence of integration | Supported. The design is cross-sectional and does not rule out the reverse direction Run 04 raises |
| Nelson & Winter 1982 | 06 | *An Evolutionary Theory of Economic Change*, Harvard University Press | Inefficient routines can persist | Supported |
| Nunn 2007 | 08 | *Quarterly Journal of Economics* 122(2), 569–600 | Relationship-specificity index: share of inputs not exchange-traded or reference-priced | Supported |
| Pfeffer & Salancik 1978 | 02 | *The External Control of Organizations*, Harper & Row | Industry merger patterns as early evidence | Supported. The early evidence is Pfeffer (1972, *ASQ* 17(3), 382–394), which used input-output data, also answering Run 07's flag on that indicator |
| Pierce & Schott 2016 | 08 | *American Economic Review* 106(7), 1632–1662 | Normal-trade-relations gap at the 2001 grant of PNTR | Supported |
| Riordan & Williamson 1985 | 06 | *International Journal of Industrial Organization* 3(4), 365–378 | Production-cost economies traded off against governance costs | Supported |
| Shelanski & Klein 1995 | 06 | *Journal of Law, Economics, and Organization* 11(2), 335–361 | Specificity–integration link among the more robust findings; uncertainty mixed | Supported |
| Walker & Weber 1984 † | 04, 06, 08 | *Administrative Science Quarterly* 29(3), 373–391 | Comparative production costs and volume uncertainty mattered; the specificity proxy (supplier-market competition) was weak | *Partly.* Comparative production costs were the strongest predictor, but supplier-market competition also predicted make-or-buy with production costs controlled, so "weak" understates it |
| Williamson 1983 | 06 | *American Economic Review* 73(4), 519–540 | Credible commitments and hostages | Supported |
| Williamson 1991 | 05, 06 | *Administrative Science Quarterly* 36(2), 269–296 | Hybrids lose viability as the frequency of disturbances rises | Supported (page for A21's formulation not checked) |

Of 36 works, 33 are supported as used and 3 are partly supported, with the corrections shown. None was found to be misattributed or non-existent. All three *Partly* rows (Argyres; Kahneman, Knetsch & Thaler; Walker & Weber) are evidence in the behavioral run (beh:O4, O5, O7) and in two of the Auditor's defeaters; the corrections weaken those points somewhat but do not reverse them.

### 3.1 Explicator (Runs 01 and 02): multiple candidate readings

*Demonstrates: prose to theory object; constructs separated from their measurement commitments; core/auxiliary partition; multiple inferential-role assignments where the prose underdetermines one.*

Run 01 produced a theory object of 19 constructs, each with all four inferential-role fields; 13 assumptions (7 core, 6 auxiliary), each with its reason for classification; and 7 propositions with fact status (P1 marked an accommodation; P5 and P6 provisionally novel pending historical check). It returned **three readings** and identified four pivotal differences. The most consequential, D1, concerns what produces alignment:

> **D1.** What produces alignment: "It follows that transactions are aligned" (s9) vs "will be selected out by competition" (s10). Reading 1: deliberate economizing choice: A4 core, A13 auxiliary, R9 teleological. Reading 2: selection: A4.r2 and A12.r2 core, A13 removed, R9.r2 selection. *Downstream:* P3 is per-transaction in R1/R3 but population-level and scope-restricted to competitive, mature populations in R2. P4 is a backstop in R1 but carries the explanation in R2. P8 and P9 are new in R2. Under R2, misalignment in protected industries is expected; under R1 it is an anomaly. *(Run 01, §c)*

The Explicator also surfaced an assumption the prose needs but does not state: that whoever chooses governance can identify the cheapest structure (tce:A13), which sits uneasily with bounded rationality (tce:A1). Given the theory object, two later roles made A13 their central finding by different routes (Runs 04 and 06; see Section 3.7).

Run 02 did the same for resource dependence (19 constructs; 10 assumptions, 4 core; 9 propositions; three readings). Its main pivot is the meaning of "constraint" (one-way dependence or power imbalance), and it found that the four dyadic quantities the theory names (each side's dependence, mutual dependence, imbalance) have only two independent dimensions, so they cannot all carry separate effects.

### 3.2 Interlocutors (Runs 03 and 04): objections in the voice of the tradition

*Demonstrates: two lens agents probing the same theory object; objections recognizable in the voice of the invoked tradition rather than generic.*

The two lenses produced different strongest objections, each characteristic of its tradition, against different core nodes:

> **Institutional, O1 (fatal to core tce:A4).** Reading 1 explains governance through its consequences for cost. It never shows that the people who adopt a structure are responding to those consequences rather than to what their field defines as the proper way to organize. [...] A correlation between asset specificity and integration (tce:P5) is therefore no evidence for tce:A4 until the institutional route to the same outcome has been ruled out. The object contains nothing that could rule it out, because it has no construct for field, logic or legitimacy. *(Run 03, O1)*

> **Behavioral, O1 (fatal).** Reading 1 says the people who write contracts are boundedly rational (tce:A1) but assumes the people who choose governance can foresee and minimize its costs (tce:A13), and tce:A13 is the only link from economizing (tce:A4) to the discriminating-alignment prediction (tce:P3). Dropping tce:A13 leaves reading 1 with no mechanism for P3, and falling back on selection turns it into reading 2. *(Run 04, O1, summarized)*

Each lens supplied a rival explanation that reproduces the theory's headline regularities (P5, P6), which is how the Interlocutors separate accommodation from novel prediction: the institutional field-template account and the behavioral problemistic-search account both predict that integration rises with asset specificity, but diverge from transaction-cost theory elsewhere. The institutional run's sharpest divergence: in fields where the hybrid is the legitimate template, the rival predicts a *negative* specificity × uncertainty interaction where transaction-cost theory predicts a positive one everywhere. Objections are ranked (institutional: 1 fatal, 7 damaging, 2 minor; behavioral: 1 fatal, 6 damaging, 2 minor), each with what would answer it.

### 3.3 Integrator (Run 07): bridges, rivalry and the price of integration

*Demonstrates: an integration run on two theory objects, with at least one bridge and one genuine conflict.*

Run 07 paired constructs by re-voiced inferential role, not by name, and classified seven links: **1 bridge, 1 rivalry, 3 complementarities, 2 equivocations**, with one further pair (frequency against resource importance) found to have no alignment.

- **Bridge.** Asset specificity (tce:C2) to resource dependence (rd:C1). The substitution test passes on tce:P5 and tce:P2 but the reverse check fails on rd:P1. The bridge is therefore one-way: specificity behaves as a *special case* of dependence (dependence arising from a sunk relationship-specific investment), not as an equivalent.
- **Rivalry.** Comparative governance cost under economizing (tce:C15, tce:A4) against managerial autonomy goals (rd:C8, rd:A4): a clash of hard cores. The divergent observable is the incidence of common ownership in dyads with high mutual dependence but low asset specificity, where transaction-cost theory predicts market governance and a penalty for integrating, and resource dependence predicts mergers without penalty.
- **Candidate integrations.** *I1, Augment* (transaction-cost host, with resource dependence's feasibility constructs replacing a TCE scope condition). Price: TCE must treat unintegrated high-specificity dyads as predicted rather than anomalous; RD is subordinated to a cost-minimizing core that its reading 1 rejects. *I2, Integrate* (a two-criterion dyadic boundary choice over cost and autonomy). Price: TCE loses economizing as its sole positive heuristic; RD's autonomy goal moves from core to protective belt. Each comes with a prediction neither theory makes alone; for I1, integration rises less steeply with the investor's asset specificity when the investor is the weaker side of a power imbalance.
- **Inferential distance** 0.76 under the draft metric (Section 4.3), with sensitivity analysis.

The run also caught two errors in its inputs: a mis-typed cross-reference id in Run 02, and an inaccurate statement in Run 02 of what transaction-cost theory predicts. It reported both rather than silently absorbing them.

### 3.4 Model Builder (Run 05): a derivation that fails to close

*Demonstrates: a derivation attempt, including cases where a derivation fails to close and the surfaced auxiliary assumption is shown.*

Run 05 built a comparative-statics model (a fixed cost plus a share of a hold-up hazard per governance structure, a hold-up stage game for the hazard, and a logit layer for the probability statements in P5 and P6), and named property-rights theory as the alternative it set aside because it contradicts tce:A6. Of eleven derivation attempts, **5 were asserted** (pending a checker), **5 failed to close**, and **1 was refuted**.

- **Fails to close: discriminating alignment (tce:P3).** It needs three auxiliaries the theory does not state: renegotiation is inefficient, not merely a transfer (A16); the hazard actually reaches the hierarchy threshold (A17); and the hybrid is not dominated (A18). The run showed that Run 01's A8 ("hybrids are intermediate in safeguards and costs") does not deliver A18: with safeguards (1, 0.5, 0) and bureaucratic costs β_H = 1, β_X = 0.6, the hybrid is intermediate yet never chosen. It proposes splitting A8 in two.
- **Refuted as stated: P6 on the probability scale.** In a logit counter-example the specificity × uncertainty interaction turns negative once integration is already likely (at Pr ≈ 0.85 the cross-partial is about −0.10). Two restatements are offered: on the log-odds scale (fails to close without assuming the hazard is supermodular, A19, and the run gives a hazard function satisfying every stated condition with a negative interaction), and as "the specificity threshold for integration falls with uncertainty" (asserted without A19).
- **Contraction and expansion.** Removing bounded rationality (core A1) makes contracts complete and collapses P1, P2, P3, P5 and P6. Adding the auxiliary that hybrid safeguards degrade with uncertainty yields a new prediction (P10: the hybrid share falls with uncertainty) and partly rescues P6.

### 3.5 Argument Auditor (Run 06): warrant gaps in the theorist's own exposition

*Demonstrates: warrant-gap detection against a theorist's own exposition.*

Run 06 mapped Input A into eleven Toulmin steps and found **11 warrant gaps** and **5 places where deductive language covers an abductive or inductive move** ("will", "therefore", "it follows that", "will be selected out", and the prediction in s11). Two structural findings: *no step carries backing* (every warrant rests on the theorist's say-so); and the chain *splits* at steps 9 and 10, reaching alignment once by choice and once by selection without saying which carries the inference (the same underdetermination the Explicator found as D1).

> **Most serious gap (W6).** s7 claims, with no warrant, that common ownership suppresses opportunism (tce:A6). The exposition applies bounded rationality and opportunism (A1/A2) to market parties but not to people inside the hierarchy, yet P1, P3 and P5 all depend on A6. *Defeater:* property-rights theory holds that integration does not remove hold-up; it moves the residual control rights, and the incentive distortion, to the other party. *(Run 06, summarized)*

### 3.6 Empirical Validation Designer (Run 08): from rival predictions to a severity ranking

*Demonstrates: extraction of risky predictions and their mapping to identified test designs.*

Run 08 took the rivals produced by Runs 02, 03 and 04 and extracted **7 risky predictions** on which transaction-cost reading 1 diverges from at least one rival, separating them from 3 contrasts on which all theories agree (including the sign of P5 itself). It proposed 7 designs, each with identification strategy, main threat, and a power calculation with its effect-size priors marked as assumptions.

- **Most severe (D1).** Natural disasters that disrupt suppliers of *generic* inputs (e.g., the 2011 Tōhoku earthquake, the 2011 Thai floods): does insourcing persist 36 months later? Reading 1 rules out lasting insourcing while the input's attributes are unchanged; the shock is exogenous to both parties; specificity is measured beforehand; and the obvious defence (rational updating on uncertainty) is already classified as a move to reading 3, so it can be pre-registered as a loss. Indicative power: 588 per arm to detect a rise from 2% to 5%, 823 per arm after clustering.
- **Merely consistent (D6).** A cross-sectional replication of P5. All three rivals predict the same positive sign, so an agreeing result is likely whichever theory is true: low severity, though cheap.
- **Crucial-experiment check.** No design binds all three traditions. D1 could serve as a crucial experiment against the behavioral account if its parameters are agreed in advance; the institutional tradition would accept none of the designs as binding; resource dependence is bound by the trade-shock design only if it keeps its autonomy assumption in the core.
- The run flagged one of its own designs (D3) as underpowered as first specified, and proposed a fix.

### 3.7 Cross-role convergence

The Explicator surfaced tce:A13 as an unstated assumption and made it the pivot between readings. Both later runs that took up the point were given reading 1, in which A13 is already flagged as a surfaced auxiliary, so they did not discover it separately. Given the theory object, two later roles made A13 their central finding by different routes: the behavioral Interlocutor made it its fatal objection, on the ground that it contradicts bounded rationality (tce:A1); and the Argument Auditor traced it to a split in the argument's structure, where alignment is reached once by choice and once by selection, and flagged the unwarranted A6 on which the choice route rests. The Model Builder then showed that even granting A13, alignment (P3) needs three further auxiliaries. This is the pattern the Foundry is designed to produce: a load-bearing but unexamined assumption located, stated, and priced.

### 3.8 Provenance Ledger trace

The Ledger is Stage 1 work; the trace below is what it would record for Runs 01 to 08. **The trace was assembled after the runs, not written live: its timestamps are reconstructed** from the completion times of the run files, rounded to the minute, the two ingest events are dated to when the case inputs were saved, and the adoption event (ev:5), which has no file of its own, is placed between the Explicator runs and the runs that used their output. It is written in the v0 `LedgerEvent` format and hash-chained (SHA-256 over the canonical JSON of each event, including the previous hash). All eleven events validate against the schema. Range ids such as `inst:O1..O10` abbreviate lists of node ids. The full JSON is `runs/09_ledger_trace.json` and Annex B.9.

| Event | Time (UTC) | Actor | Action | Inputs → outputs | Responds to |
|---|---|---|---|---|---|
| ev:1 | 18:46 | case author | ingest | → Input A | |
| ev:2 | 18:46 | case author | ingest | → Input B | |
| ev:3 | 18:54 | Explicator | propose | Input A → tce ensemble, readings 1 to 3 | ev:1 |
| ev:4 | 18:55 | Explicator | propose | Input B → rd ensemble, readings 1 to 3 | ev:2 |
| ev:5 | 18:56 | demonstration operator (Claude), standing in for the human theorist | accept | both ensembles → tce reading 1, rd reading 1 | ev:4 |
| ev:6 | 18:57 | Interlocutor (institutional) | challenge | tce reading 1 → inst:O1..O10 | ev:5 |
| ev:7 | 18:57 | Interlocutor (behavioral) | challenge | tce reading 1 → beh:O1..O9 | ev:5 |
| ev:8 | 18:58 | Argument Auditor | annotate | Input A, tce reading 1 → W1..W11 | ev:5 |
| ev:9 | 19:00 | Model Builder | derive | tce reading 1 → D4..D13, A16..A21, P10 | ev:5 |
| ev:10 | 19:01 | Integrator | align | tce reading 1, rd reading 1 → AlignmentMap | ev:5 |
| ev:11 | 19:02 | Empirical Validation Designer | design | tce reading 1, objections, rd reading 1 → RP1..RP7, D1..D7 | ev:7 |

### 3.9 What the runs exposed about the Foundry itself

The runs were also the first test of the schema, the metrics and the instruction sets, and found four things to fix in Stage 1:

1. **Cross-run id discipline.** Run 02 referred to its rival as `tce:reading1` where Run 01 had defined `tce:reading-1`; the Integrator caught it. The orchestration layer must resolve cross-object references, not leave them to the agents.
2. **The draft inferential-distance metric is too coarse.** It scores a rivalry the same as an unrelated pair (distance 1). Run 07 shows a graded weighting by link kind (bridge < complementarity < rivalry < equivocation < unaligned) moves the TCE–RD distance from 0.76 to about 0.38. Section 4.3 notes this.
3. **Assumptions stated in words can fail to do the work assigned to them.** A8 (hybrids intermediate) did not secure the three-way prediction. The Model Builder's surfacing of A18 is exactly the role's purpose, and argues for routing every Explicator assumption through the Model Builder before it is accepted.
4. **Probability-scale propositions need a scale.** P6 as written is refuted on the probability scale and survives only when restated. The Explicator's instruction set should require each interaction claim to name its scale.

---

## 4. Theory-object schema (DRAFT v0)

> **Status: draft v0.1, 10 October 2026. Not yet implemented.** The schema below is the current specification of the theory object referenced in Section 3 of the proposal as a Stage 1 build target. It has been used as the output format for the worked runs in Section 3, which is its first test; field names and enumerations will change during Stage 1. The full JSON Schema (draft 2020-12) and the JSON-LD context are reproduced in Annex A and are in the repository as `schema/theory-object.v0.schema.json` and `schema/context.v0.jsonld`.

### 4.1 Design principles

1. **Constructs are inferential roles.** Every `Construct` must carry an `InferentialRole` with four lists (commitments, entitlements, licenses, precludes). A construct with only a definition fails validation. This is the schema-level expression of the proposal's inferentialist wager.
2. **Readings are plural until a human chooses.** `FormalizationEnsemble` holds several theory objects; its `adoptedReading` can be set only by a human `LedgerEvent`.
3. **Derivations have a status, and only a checker can close them.** `Derivation.status` is `asserted`, `open`, `closed` or `refuted`; `closed` requires a named `checker`.
4. **Assumptions are partitioned and traceable.** Every `Assumption` is `core` or `auxiliary`, and `explicit`, `implicit` or `surfaced` (with the agent or derivation that surfaced it).
5. **Everything is addressable.** Every node has an `@id`, so Ledger events, objections and alignment links can point at it. Serialization as JSON-LD lets theory objects from different users and traditions be merged and queried as one graph, the "epinet of the field's theoretical corpus" the proposal describes.
6. **The grammar is reused, not reinvented.** `StanceProfile` enumerations are the Project Lakatos Table 3 categories.

### 4.2 Node types

| Node | Required fields | Purpose |
|---|---|---|
| `TheoryObject` | id, label, constructs, relations, assumptions, propositions | One reading of one theory |
| `StanceProfile` | (all optional) | Table 3 tags: stance, corroboration logic, ontology, model classes, explanatory norms, justification strategies, inference norms |
| `Construct` | id, label, constructType, inferentialRole | Typed construct with level, measurement commitments, and alternative roles |
| `InferentialRole` | commitments, entitlements, licenses, precludes | Brandomian content of a construct |
| `Relation` | id, from, to, form | Directed relation; form is causal, teleological, functional, constitutive or selection |
| `Mechanism` | id, label, steps | Ordered chain of relations |
| `Assumption` | id, statement, status | Core or auxiliary; explicit, implicit or surfaced |
| `ScopeCondition` | id, statement | Where the theory claims to apply |
| `Proposition` | id, statement | Claim, with fact status (novel or accommodation) and rival divergence |
| `Derivation` | id, target, premises, method, status | Attempt to derive a proposition; auxiliaries required; checker |
| `ExecutableModel` | id, modelClass | Formal or simulation model with construct-to-variable map |
| `FormalizationEnsemble` | id, members | Multiple readings, pivotal differences, dispersion, adopted reading |
| `AlignmentMap` | id, theories, links | Integrator output: bridges, rivalries, complementarities, equivocations, with operator and inferential price |
| `LedgerEvent` | id, timestamp, actor, action, prevHash, hash | One append-only, hash-chained Provenance Ledger entry |

### 4.3 The measured quantities

The proposal states that once theories exist as inferential-role structures, five of their properties become quantities. The draft operational definitions are:

| Quantity | Draft definition (computed on one theory object T, or a pair) | Range |
|---|---|---|
| **Specification completeness** | Mean, over constructs, of the share of five slots filled (definition, measurement commitment, and non-empty commitments, entitlements and licenses), multiplied by the share of relations with both form and sign specified. | 0 to 1 |
| **Derivational tightness** | Over propositions claimed as derived, the mean of *s / (1 + a)*, where *s* is 1 if the derivation is `closed`, 0.5 if `asserted`, 0 if `open` or `refuted`, and *a* is the number of auxiliaries required that were not in T's stated assumptions. | 0 to 1 |
| **Falsifiability surface** | The number of propositions that are (i) marked `novel` and (ii) have at least one rival divergence with an observable, normalized by the total number of propositions. A count version is reported alongside. | 0 to 1 |
| **Assumption load** | The number of auxiliary assumptions (explicit plus surfaced) per proposition, with the share that were `surfaced` reported separately as **hidden assumption load**. | ≥ 0 |
| **Inferential distance** (between T1 and T2) | 1 minus the share of aligned construct pairs classified as bridges among all pairs that the Integrator considered, weighted by the number of licensed inferences involved. A pair with no alignment counts as distance 1. | 0 to 1 |
| **Formalization dispersion** (within an ensemble) | Mean pairwise inferential distance between members of the ensemble, computed with the same measure. | 0 to 1 |

**Revision proposed by the first run.** The Integrator's run (Run 07, §5) showed that the draft inferential distance scores a rivalry, which names a shared observable on which two theories conflict and is therefore a highly commensurable relation, the same as an unrelated pair. The proposed Stage 1 revision weights each aligned pair by link kind: bridge 0, complementarity 0.25, rivalry 0.5, equivocation 0.75, no alignment 1 (illustrative, to be calibrated against expert judgments). On the TCE–RD case this moves the distance from 0.76 to about 0.38.

These are first definitions, chosen to be computable directly from the schema. Their reliability and validity are themselves objects of the Stage 1 validation studies (Section 5.2).

---

## 5. Validation protocols

### 5.1 Retrospective validity of the Interlocutors

*Question.* Do the Interlocutors recover the documented published critiques of theories whose critical histories are well established?

*Procedure.* For each benchmark theory, two domain experts independently compile the theory's major published critiques from the literature, each reduced to one sentence and a source, and reconcile them into a reference list. The Interlocutors are run on the Explicator's theory object of the theory's founding statement, with no access to the critical literature after that statement's date (the lens corpus is filtered by date). Two further coders, blind to which objections came from which lens and to each other, match each reference critique to the Foundry objections.

*Recovery rule.* A critique counts as recovered if both coders judge that at least one Foundry objection makes the same point about the same target, even if in different words. Disagreements are resolved by a third coder and reported.

*Training-data contamination and the no-corpus baseline.* Date-filtering the lens corpus does not make the Interlocutors blind. The base language model has already read the critical literature on canonical theories, including critiques published long after a theory's founding statement; the worked runs show it (the Argument Auditor's main defeater in Run 06 is Grossman & Hart 1986, and the behavioral run draws on Ghoshal & Moran 1996, both well after Williamson 1975). A high recovery rate could therefore measure the model's memory of the critical record rather than the Interlocutors' capacity to find weaknesses. To separate the two, every benchmark theory is run under two conditions, with identical theory objects, coders and recovery rule:
- **Lens condition:** the Interlocutor instruction set with its lens specification and its date-filtered curated corpus;
- **Baseline condition:** the same base model, given the same theory object and the same generic adversarial instructions, with **no lens specification and no lens corpus**.

Recovery in the baseline condition estimates what the model already knows. The quantity of interest is the **lens increment**: recovery in the lens condition minus recovery in the baseline condition, together with the share of each condition's objections that are judged substantive but absent from the published record (Section 5.2). Coders are blind to condition.

*Bar.* Recovery of at least **80%** of a theory's major published critiques in the lens condition, as pre-specified in the proposal, **and** a lens increment above a margin fixed in the pre-registration. Recovery alone, without the increment, is not counted as evidence that the lenses track real epistemic weaknesses. Coder agreement (Cohen's κ) is reported alongside.

*Candidate benchmark theories* (to be fixed and pre-registered at the start of Stage 1): transaction-cost theory of the firm (Williamson 1975); resource-dependence theory (Pfeffer & Salancik 1978); the garbage-can model (Cohen, March & Olsen 1972); structural inertia (Hannan & Freeman 1984); institutional isomorphism (DiMaggio & Powell 1983); absorptive capacity (Cohen & Levinthal 1990); the resource-based view (Barney 1991); upper-echelons theory (Hambrick & Mason 1984). Each has an extensive and well-documented critical record.

### 5.2 Reliability and coverage at scale

Scale to **N ≈ 25 to 30** canonical and contemporary Organization Science theories, each processed by two independent human–Foundry teams. Measures: inter-team agreement on theory objects (the inferential distance between the two teams' adopted readings, Section 4.3); coverage of the published critical record (as in 5.1); and the more demanding test, whether the Foundry surfaces **substantive gaps absent from the published record**, assessed blind by domain experts who rate each Foundry objection not matched to the record as substantive, minor, or mistaken.

### 5.3 Prospective value in use

A preregistered study in which doctoral students and faculty develop early-stage theory with and without the Foundry. The resulting drafts are evaluated blind by expert raters on specification, argumentative soundness and testability (the latter two linked to the Argument Auditor and the Empirical Validation Designer respectively). The claim under test is not that the Foundry makes theorizing faster, but that it makes theories *better specified and more severely testable*. Secondary outcome: whether Foundry-assisted theories converge in style and content (lexical and structural similarity across theory objects), which tests the homogenization risk directly.

---

## 6. Status of components

| Component | Status at submission |
|---|---|
| Lakatos cognitive operators (13), discourse grammar, routine agents (12) | Built and in use in Project Lakatos |
| Seventeen scholarly-role agents (Section 2.1) | One agent per Table 4 class, specified and prototyped in Project Lakatos |
| Six Foundry role instruction sets | Specified (v0.2, repository `instruction-sets/`); v0.1 exercised in Section 3 |
| Interlocutor lens profiles (5) | Specified (Section 1.8); curated corpora to be assembled in Stage 1 |
| Theory-object schema | Draft v0 (Section 4, Annex A); used as the output format of the runs in Section 3 |
| Orchestration loop | Designed (Section 1.9); to be built in Stage 1 |
| Provenance Ledger | Schema specified (`LedgerEvent`); to be built in Stage 1 |
| Symbolic-checking and simulation backend | To be built in Stage 1. Until then no derivation can be marked `closed`; the Proof Verifier and Proof Synthesizer routine agents are the existing precursors |
| Validation studies | Designed (Section 5); to be pre-registered at the start of Stage 1 |

---

## References

Aldrich, H. E. (1999). *Organizations Evolving*. Sage.  
Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management*, 17(1), 99–120.  
Brandom, R. B. (1994). *Making It Explicit: Reasoning, Representing, and Discursive Commitment*. Harvard University Press.  
Brandom, R. B. (2000). *Articulating Reasons: An Introduction to Inferentialism*. Harvard University Press.  
Burt, R. S. (1992). *Structural Holes: The Social Structure of Competition*. Harvard University Press.  
Carroll, G. R., & Hannan, M. T. (2000). *The Demography of Corporations and Industries*. Princeton University Press.  
Casciaro, T., & Piskorski, M. J. (2005). Power imbalance, mutual dependence, and constraint absorption: A closer look at resource dependence theory. *Administrative Science Quarterly*, 50(2), 167–199.  
Coase, R. H. (1937). The nature of the firm. *Economica*, 4(16), 386–405.  
Cohen, M. D., March, J. G., & Olsen, J. P. (1972). A garbage can model of organizational choice. *Administrative Science Quarterly*, 17(1), 1–25.  
Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128–152.  
Cyert, R. M., & March, J. G. (1963). *A Behavioral Theory of the Firm*. Prentice-Hall.  
DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, 48(2), 147–160.  
Granovetter, M. (1985). Economic action and social structure: The problem of embeddedness. *American Journal of Sociology*, 91(3), 481–510.  
Greve, H. R. (2003). *Organizational Learning from Performance Feedback*. Cambridge University Press.  
Gulati, R. (1995). Social structure and alliance formation patterns: A longitudinal analysis. *Administrative Science Quarterly*, 40(4), 619–652.  
Hambrick, D. C., & Mason, P. A. (1984). Upper echelons: The organization as a reflection of its top managers. *Academy of Management Review*, 9(2), 193–206.  
Hannan, M. T., & Freeman, J. (1977). The population ecology of organizations. *American Journal of Sociology*, 82(5), 929–964.  
Hannan, M. T., & Freeman, J. (1984). Structural inertia and organizational change. *American Sociological Review*, 49(2), 149–164.  
Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263–291.  
Klein, B., Crawford, R. G., & Alchian, A. A. (1978). Vertical integration, appropriable rents, and the competitive contracting process. *Journal of Law and Economics*, 21(2), 297–326.  
Lakatos, I. (1970). Falsification and the methodology of scientific research programmes. In I. Lakatos & A. Musgrave (Eds.), *Criticism and the Growth of Knowledge* (pp. 91–196). Cambridge University Press.  
March, J. G., & Simon, H. A. (1958). *Organizations*. Wiley.  
Masten, S. E. (1984). The organization of production: Evidence from the aerospace industry. *Journal of Law and Economics*, 27(2), 403–417.  
Mayo, D. G. (2018). *Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars*. Cambridge University Press.  
Meyer, J. W., & Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. *American Journal of Sociology*, 83(2), 340–363.  
Moldoveanu, M. C., & Baum, J. A. C. (2014). *Epinets: The Epistemic Structure and Dynamics of Social Networks*. Stanford University Press.  
Monteverde, K., & Teece, D. J. (1982). Supplier switching costs and vertical integration in the automobile industry. *Bell Journal of Economics*, 13(1), 206–213.  
Morgan, M. S. (2012). *The World in the Model: How Economists Work and Think*. Cambridge University Press.  
Nelson, R. R., & Winter, S. G. (1982). *An Evolutionary Theory of Economic Change*. Harvard University Press.  
Pfeffer, J., & Salancik, G. R. (1978). *The External Control of Organizations: A Resource Dependence Perspective*. Harper & Row.  
Podolny, J. M. (2001). Networks as the pipes and prisms of the market. *American Journal of Sociology*, 107(1), 33–60.  
Organization Science (2026). Call for papers: *AI-Enabled Frontiers in Organizational Science*. Special issue; guest editors C. Gartenberg, S. Hasan, L. Pierce, C. Bail, H. Dai, O. Hauser, H. Rahman & D. Zhang.  
Price, H. (2011). *Naturalism Without Mirrors*. Oxford University Press.  
Scott, W. R. (1995). *Institutions and Organizations*. Sage.  
Simon, H. A. (1947). *Administrative Behavior*. Macmillan.  
Simon, H. A. (1955). A behavioral model of rational choice. *Quarterly Journal of Economics*, 69(1), 99–118.  
Thornton, P. H., Ocasio, W., & Lounsbury, M. (2012). *The Institutional Logics Perspective*. Oxford University Press.  
Toulmin, S. (1958). *The Uses of Argument*. Cambridge University Press.  
Uzzi, B. (1997). Social structure and competition in interfirm networks: The paradox of embeddedness. *Administrative Science Quarterly*, 42(1), 35–67.  
Williamson, O. E. (1975). *Markets and Hierarchies: Analysis and Antitrust Implications*. Free Press.  
Williamson, O. E. (1985). *The Economic Institutions of Capitalism*. Free Press.  
Williamson, O. E. (1991). Comparative economic organization: The analysis of discrete structural alternatives. *Administrative Science Quarterly*, 36(2), 269–296.  

*References cited only inside the transcripts (Annex B) are as given there. Every work the agents marked "(to verify)" is checked in the citation verification table in Section 3.0.*

---

## Annex A. Theory-object schema, draft v0 (full text)

### A.1 JSON Schema (`schema/theory-object.v0.schema.json`)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://foundry.lakatos.example/schema/theory-object/v0",
  "title": "Foundry Theory Object (DRAFT v0)",
  "description": "DRAFT v0, 10 October 2026. Not yet implemented. An inferential-role representation of a theory: constructs are positions in a web of material inferential relations (commitments, entitlements, licensed inferences, incompatibilities), not names for latent essences. Serialized as JSON-LD using context.v0.jsonld. Every identified node can be referenced by Provenance Ledger events. Field names and enumerations will change during Stage 1.",
  "type": "object",
  "required": ["@context", "@id", "@type", "label", "schemaVersion", "constructs", "relations", "assumptions", "propositions"],
  "properties": {
    "@context": { "description": "Must reference the Foundry v0 context.", "type": ["string", "object", "array"] },
    "@id": { "$ref": "#/$defs/iri" },
    "@type": { "const": "TheoryObject" },
    "schemaVersion": { "const": "0.1-draft" },
    "label": { "type": "string" },
    "tradition": { "description": "Research programme the theory belongs to, e.g. transaction-cost economics.", "type": "string" },
    "sources": { "type": "array", "items": { "$ref": "#/$defs/SourceRef" } },
    "readingOf": { "description": "When this object is one member of a formalization ensemble: the ensemble's @id.", "$ref": "#/$defs/iri" },
    "stanceProfile": { "$ref": "#/$defs/StanceProfile" },
    "scopeConditions": { "type": "array", "items": { "$ref": "#/$defs/ScopeCondition" } },
    "constructs": { "type": "array", "items": { "$ref": "#/$defs/Construct" } },
    "relations": { "type": "array", "items": { "$ref": "#/$defs/Relation" } },
    "mechanisms": { "type": "array", "items": { "$ref": "#/$defs/Mechanism" } },
    "assumptions": { "type": "array", "items": { "$ref": "#/$defs/Assumption" } },
    "propositions": { "type": "array", "items": { "$ref": "#/$defs/Proposition" } },
    "derivations": { "type": "array", "items": { "$ref": "#/$defs/Derivation" } },
    "models": { "type": "array", "items": { "$ref": "#/$defs/ExecutableModel" } },
    "openQuestions": { "description": "Points the producing agent could not settle and returned to the human theorist.", "type": "array", "items": { "type": "string" } },
    "provenance": { "$ref": "#/$defs/ProvenanceStamp" }
  },
  "$defs": {
    "iri": { "type": "string", "description": "Compact IRI or local id, e.g. 'tce:C1'." },
    "SourceRef": {
      "type": "object",
      "required": ["citation"],
      "properties": {
        "citation": { "type": "string" },
        "span": { "description": "Quoted or located passage this node was read from.", "type": "string" }
      }
    },
    "StanceProfile": {
      "description": "Tags from the Project Lakatos discourse grammar (Appendix A, Table 3).",
      "type": "object",
      "properties": {
        "epistemologicalStance": { "enum": ["positivism-strict", "positivism-lay", "realism-metaphysical", "realism-language-dependent", "instrumentalism", "constructivism", "pragmatism", "mixed", "undetermined"] },
        "corroborationLogic": { "enum": ["inductivism-bayesian", "inductivism-frequentist", "falsificationism-dogmatic", "falsificationism-naive", "falsificationism-methodological", "falsificationism-sophisticated", "mixed", "undetermined"] },
        "ontologicalCommitments": { "type": "array", "items": { "type": "string" } },
        "modelClasses": { "type": "array", "items": { "enum": ["causal", "teleological", "functional", "structural", "dynamical", "relational"] } },
        "explanatoryNorms": { "type": "array", "items": { "enum": ["depth", "coverage-parsimony"] } },
        "justificationStrategies": { "type": "array", "items": { "enum": ["reductive", "eliminative", "assimilative"] } },
        "inferenceNorms": { "type": "array", "items": { "enum": ["deductive", "inductive", "abductive"] } },
        "evidence": { "description": "Why these tags were assigned.", "type": "string" }
      }
    },
    "ScopeCondition": {
      "type": "object",
      "required": ["@id", "statement"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "statement": { "type": "string" },
        "explicitness": { "enum": ["explicit", "implicit", "surfaced"] }
      }
    },
    "InferentialRole": {
      "description": "Brandomian inferential role of a construct. Each entry is a statement-level inference, written as a short conditional, optionally pointing to propositions or other constructs.",
      "type": "object",
      "required": ["commitments", "entitlements", "licenses", "precludes"],
      "properties": {
        "commitments": { "description": "What asserting that the construct applies commits the theorist to.", "type": "array", "items": { "$ref": "#/$defs/Inference" } },
        "entitlements": { "description": "What would entitle a theorist to assert that the construct applies (its evidential or circumstantial conditions).", "type": "array", "items": { "$ref": "#/$defs/Inference" } },
        "licenses": { "description": "Downstream inferences others may draw once it is asserted.", "type": "array", "items": { "$ref": "#/$defs/Inference" } },
        "precludes": { "description": "Claims incompatible with asserting it.", "type": "array", "items": { "$ref": "#/$defs/Inference" } }
      }
    },
    "Inference": {
      "type": "object",
      "required": ["@id", "statement"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "statement": { "type": "string" },
        "refs": { "type": "array", "items": { "$ref": "#/$defs/iri" } },
        "strength": { "enum": ["strict", "defeasible"] }
      }
    },
    "MeasurementCommitment": {
      "type": "object",
      "required": ["indicator"],
      "properties": {
        "indicator": { "type": "string" },
        "level": { "enum": ["nominal", "ordinal", "interval", "ratio", "latent"] },
        "method": { "type": "string" },
        "unitOfAnalysis": { "type": "string" }
      }
    },
    "Construct": {
      "type": "object",
      "required": ["@id", "label", "constructType", "inferentialRole"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "label": { "type": "string" },
        "definition": { "type": "string" },
        "constructType": { "enum": ["entity", "attribute", "state", "process", "event", "disposition", "relation"] },
        "level": { "enum": ["individual", "dyad", "transaction", "organization", "population", "field", "multi-level"] },
        "measurementCommitments": { "type": "array", "items": { "$ref": "#/$defs/MeasurementCommitment" } },
        "inferentialRole": { "$ref": "#/$defs/InferentialRole" },
        "alternativeRoles": { "description": "Rival inferential-role assignments where the prose underdetermines one; each is a full InferentialRole with a label.", "type": "array", "items": { "allOf": [{ "$ref": "#/$defs/InferentialRole" }, { "type": "object", "properties": { "readingLabel": { "type": "string" } } }] } },
        "source": { "$ref": "#/$defs/SourceRef" }
      }
    },
    "Relation": {
      "type": "object",
      "required": ["@id", "from", "to", "form"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "from": { "$ref": "#/$defs/iri" },
        "to": { "$ref": "#/$defs/iri" },
        "form": { "enum": ["causal", "teleological", "functional", "constitutive", "selection"] },
        "sign": { "enum": ["positive", "negative", "non-monotone", "conditional", "unspecified"] },
        "moderators": { "type": "array", "items": { "$ref": "#/$defs/iri" } },
        "scope": { "type": "array", "items": { "$ref": "#/$defs/iri" } }
      }
    },
    "Mechanism": {
      "type": "object",
      "required": ["@id", "label", "steps"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "label": { "type": "string" },
        "steps": { "description": "Ordered relation ids composing the mechanism.", "type": "array", "items": { "$ref": "#/$defs/iri" } },
        "mechanismType": { "enum": ["cognitive", "strategic", "economic", "political", "social-structural", "selection", "institutional"] }
      }
    },
    "Assumption": {
      "type": "object",
      "required": ["@id", "statement", "status"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "statement": { "type": "string" },
        "status": { "description": "Core = Lakatosian hard core; auxiliary = protective belt.", "enum": ["core", "auxiliary"] },
        "explicitness": { "enum": ["explicit", "implicit", "surfaced"] },
        "surfacedBy": { "description": "Agent role or derivation that surfaced an implicit assumption.", "type": "string" },
        "supports": { "type": "array", "items": { "$ref": "#/$defs/iri" } }
      }
    },
    "Proposition": {
      "type": "object",
      "required": ["@id", "statement"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "statement": { "type": "string" },
        "claimType": { "enum": ["prediction", "explanation", "prescription", "definition"] },
        "factStatus": { "description": "Lakatos (1970): does the theory predict this as a novel fact, or accommodate a known one?", "enum": ["novel", "accommodation", "undetermined"] },
        "observables": { "type": "array", "items": { "type": "string" } },
        "rivalDivergence": { "description": "Rival theory objects that predict otherwise, with their contrary prediction.", "type": "array", "items": { "type": "object", "properties": { "rival": { "$ref": "#/$defs/iri" }, "contrary": { "type": "string" } } } }
      }
    },
    "Derivation": {
      "type": "object",
      "required": ["@id", "target", "premises", "method", "status"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "target": { "$ref": "#/$defs/iri" },
        "premises": { "type": "array", "items": { "$ref": "#/$defs/iri" } },
        "method": { "enum": ["verbal", "symbolic", "simulation", "game-theoretic"] },
        "status": { "description": "'asserted' = claimed in prose only; 'closed' = verified by a checker; 'open' = fails without further assumptions.", "enum": ["asserted", "closed", "open", "refuted"] },
        "auxiliariesRequired": { "type": "array", "items": { "$ref": "#/$defs/iri" } },
        "checker": { "description": "Symbolic or simulation backend that disposed the derivation; empty for 'asserted'.", "type": "string" },
        "notes": { "type": "string" }
      }
    },
    "ExecutableModel": {
      "type": "object",
      "required": ["@id", "modelClass"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "modelClass": { "enum": ["agent-based", "structural", "game-theoretic", "system-dynamics", "analytical"] },
        "artifact": { "description": "Path or hash of the code or formal specification.", "type": "string" },
        "mapsConstructs": { "type": "array", "items": { "type": "object", "properties": { "construct": { "$ref": "#/$defs/iri" }, "parameterOrVariable": { "type": "string" } } } }
      }
    },
    "ProvenanceStamp": {
      "type": "object",
      "properties": {
        "createdBy": { "type": "string" },
        "ledgerEvents": { "type": "array", "items": { "$ref": "#/$defs/iri" } }
      }
    },

    "FormalizationEnsemble": {
      "description": "Explicator output when prose underdetermines a reading: several theory objects plus their dispersion.",
      "type": "object",
      "required": ["@id", "@type", "members"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "@type": { "const": "FormalizationEnsemble" },
        "members": { "type": "array", "items": { "$ref": "#/$defs/iri" } },
        "pivotalDifferences": { "type": "array", "items": { "type": "string" } },
        "dispersion": { "type": "number", "minimum": 0, "maximum": 1 },
        "adoptedReading": { "description": "Set only by a human decision recorded in the Ledger.", "$ref": "#/$defs/iri" }
      }
    },
    "AlignmentMap": {
      "description": "Integrator output relating two or more theory objects.",
      "type": "object",
      "required": ["@id", "@type", "theories", "links"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "@type": { "const": "AlignmentMap" },
        "theories": { "type": "array", "items": { "$ref": "#/$defs/iri" }, "minItems": 2 },
        "links": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["kind", "constructs", "basis"],
            "properties": {
              "kind": { "enum": ["bridge", "rivalry", "complementarity", "equivocation"] },
              "constructs": { "type": "array", "items": { "$ref": "#/$defs/iri" } },
              "sharedLicenses": { "type": "array", "items": { "type": "string" } },
              "conflictingEntitlements": { "type": "array", "items": { "type": "string" } },
              "discharges": { "description": "For complementarity: which open assumption of one theory the other's commitment discharges.", "type": "string" },
              "basis": { "type": "string" },
              "operator": { "enum": ["Integrate", "Augment", "Reduce", "Assimilate", "Eliminate"] },
              "inferentialPrice": { "description": "What the integration gives up or must newly assume.", "type": "string" }
            }
          }
        }
      }
    },
    "LedgerEvent": {
      "description": "One append-only Provenance Ledger entry. Events are hash-chained.",
      "type": "object",
      "required": ["@id", "@type", "timestamp", "actor", "action", "prevHash", "hash"],
      "properties": {
        "@id": { "$ref": "#/$defs/iri" },
        "@type": { "const": "LedgerEvent" },
        "timestamp": { "type": "string", "format": "date-time" },
        "actor": { "type": "object", "required": ["kind", "name"], "properties": { "kind": { "enum": ["human", "agent", "checker"] }, "name": { "type": "string" }, "modelVersion": { "type": "string" }, "instructionSetVersion": { "type": "string" } } },
        "action": { "enum": ["ingest", "propose", "accept", "reject", "modify", "derive", "challenge", "align", "design", "annotate"] },
        "inputs": { "type": "array", "items": { "$ref": "#/$defs/iri" } },
        "outputs": { "type": "array", "items": { "$ref": "#/$defs/iri" } },
        "respondsTo": { "$ref": "#/$defs/iri" },
        "rationale": { "type": "string" },
        "prevHash": { "type": "string" },
        "hash": { "type": "string" }
      }
    }
  }
}
```

### A.2 JSON-LD context (`schema/context.v0.jsonld`)

```json
{
  "@context": {
    "@version": 1.1,
    "@vocab": "https://foundry.lakatos.example/vocab/v0#",
    "fdy": "https://foundry.lakatos.example/vocab/v0#",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "TheoryObject": "fdy:TheoryObject",
    "FormalizationEnsemble": "fdy:FormalizationEnsemble",
    "AlignmentMap": "fdy:AlignmentMap",
    "LedgerEvent": { "@id": "fdy:LedgerEvent" },
    "from": { "@id": "fdy:from", "@type": "@id" },
    "to": { "@id": "fdy:to", "@type": "@id" },
    "refs": { "@id": "fdy:refs", "@type": "@id", "@container": "@set" },
    "moderators": { "@id": "fdy:moderators", "@type": "@id", "@container": "@set" },
    "steps": { "@id": "fdy:steps", "@type": "@id", "@container": "@list" },
    "supports": { "@id": "fdy:supports", "@type": "@id", "@container": "@set" },
    "premises": { "@id": "fdy:premises", "@type": "@id", "@container": "@set" },
    "target": { "@id": "fdy:target", "@type": "@id" },
    "auxiliariesRequired": { "@id": "fdy:auxiliariesRequired", "@type": "@id", "@container": "@set" },
    "members": { "@id": "fdy:members", "@type": "@id", "@container": "@set" },
    "readingOf": { "@id": "fdy:readingOf", "@type": "@id" },
    "theories": { "@id": "fdy:theories", "@type": "@id", "@container": "@set" },
    "inputs": { "@id": "prov:used", "@type": "@id", "@container": "@set" },
    "outputs": { "@id": "prov:generated", "@type": "@id", "@container": "@set" },
    "respondsTo": { "@id": "prov:wasInformedBy", "@type": "@id" },
    "timestamp": { "@id": "prov:atTime", "@type": "xsd:dateTime" },
    "actor": { "@id": "prov:wasAssociatedWith" }
  }
}
```

---

## Annex B. Full transcripts

*Reproduced unedited from `runs/`, except that heading levels are lowered to fit this document. Section numbers inside each transcript are the run's own. The agents' "(to verify)" flags are kept as part of the record; every flagged work is checked, and any correction given, in the citation verification table in Section 3.0. The transcripts were produced with instruction set v0.1.*

### B.0 Case inputs


These two passages are the prose theory inputs for the worked transcripts. They were written for this demonstration as faithful paraphrases of the canonical statements of each theory; they are not quotations. They play the part of "a theorist's prose exposition" handed to the Foundry.

#### Input A: Transaction-cost theory of firm boundaries (after Williamson 1975, 1985, 1991)

Firms exist because some transactions are more cheaply governed inside a hierarchy than across a market. Transactions differ along three dimensions: the specificity of the assets they require, the uncertainty surrounding them, and the frequency with which they recur. Asset specificity is the decisive dimension. When one party invests in assets whose value is much higher inside this relationship than in their next-best use, such as a die built for a single customer, a plant sited next to a single buyer, or skills learned for one employer's systems, the investing party is exposed to opportunistic renegotiation once the investment is sunk. Because contracting parties are boundedly rational, they cannot write complete contracts that anticipate every contingency, and because some of them are opportunistic, gaps in contracts will be exploited. Markets therefore become hazardous as asset specificity rises. Hierarchy, meaning common ownership with authority and administrative control, suppresses opportunism and permits adaptation by fiat, but it carries bureaucratic costs and weakens high-powered incentives. Hybrids such as long-term contracts and alliances fall between the two. It follows that transactions are aligned with governance structures in a discriminating way: low specificity goes to the market, intermediate specificity to hybrids, and high specificity to hierarchy. Firms that misalign transactions and governance will incur higher costs and, over time, will be selected out by competition. Empirically, we should observe that the probability of vertical integration increases with asset specificity, and more steeply when uncertainty is high.

#### Input B: Resource-dependence theory of organizational boundaries (after Pfeffer & Salancik 1978; Casciaro & Piskorski 2005)

Organizations are not self-sufficient. They depend on their environments for critical resources, and that dependence is the source of other actors' power over them. Dependence on a supplier or buyer is greater the more important the resource is to the organization's operations and the fewer alternative sources of it there are. Organizations are run by managers who seek to reduce uncertainty and preserve the organization's autonomy, so they act to manage dependence. They may absorb the constraining actor through merger or acquisition, co-opt it through interlocking directorates or joint ventures, negotiate long-term arrangements, or diversify away from it. Which tactic is chosen depends on how much power each side holds: mergers are most likely where an organization faces high constraint from a partner, and especially where mutual dependence between the two is high, because mutual dependence makes absorption feasible and attractive to both sides. Power imbalance, by contrast, makes the weaker side want to absorb the stronger but leaves it less able to do so. Organizational boundaries therefore reflect the political management of external dependencies rather than the minimization of costs. Empirically, we should observe that mergers and other boundary-spanning ties concentrate between organizations that depend heavily on each other, and that boundaries shift when the structure of resource dependencies shifts.

---

### B.1 Run 01: Explicator on Input A (transaction-cost theory)
*Instruction set: Foundry v0.1, Role 1. Input: case_inputs.md, Input A. Single run, unedited.*

---

#### 0. Segmentation (step 1)

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

#### (a) Reading 1: JSON-LD theory object

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

#### (b) Further readings: fields that differ from reading 1

##### Reading 2: "selection equilibrium"

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

##### Reading 3: "independent dimensions"

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

##### Ensemble

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

#### (c) Pivotal differences

| # | Underdetermined point (textual basis) | Reading 1 | Reading 2 | Reading 3 | Downstream propositions that change |
|---|---|---|---|---|---|
| D1 | What produces alignment: "It follows that transactions are aligned" (s9) vs "will be selected out by competition" (s10) | Deliberate economizing choice: A4 core, A13 auxiliary, R9 teleological | Selection: A4.r2 and A12.r2 core, A13 removed, R9.r2 selection | as reading 1 | **P3** is per-transaction in R1/R3 but population-level and scope-restricted to competitive, mature populations in R2. **P4** is a backstop in R1 but carries the explanation in R2. **P8** and **P9** are new in R2. Under R2, misalignment in protected industries is expected; under R1 it is an anomaly. |
| D2 | Role of uncertainty: listed as an independent dimension (s2) but used only as a moderator (s11) | Moderator only | Moderator only | Main effect plus moderator (R14, R15, A15) | **P7** (no uncertainty effect at low asset specificity) holds in R1/R2 and is reversed in R3 (P7.r3). **P6** is unchanged in all readings. |
| D3 | Status of "asset specificity is the decisive dimension" (s3) | Core | Core | Auxiliary (A5.r3) | No proposition's content changes. What changes is where an anomaly to **P5** is directed. In R1/R2 a null effect of asset specificity is absorbed by the belt (measurement, A10 exogeneity, A12). In R3 it can be absorbed by re-weighting toward uncertainty without abandoning the programme. |
| D4 | Referent of "firm": "Firms exist because ... hierarchy" (s1) vs "Firms that misalign ... selected out" (s10) | Firm = hierarchy (C17 primary role) | Firm = portfolio of transactions and unit of selection (C17 alternative role) | as reading 1 | **P1** reads as a per-transaction cost claim in R1/R3 but as a survival claim in R2. Under R2, P4's selection pressure on a misaligned transaction is diluted by the firm's other transactions. |

Cross-cutting point not made into a separate reading: P3 is three-way, but P5 and P6 are stated for a binary outcome (vertical integration). Whether hybrids are coded as "not integrated" changes how P5 bears on P3 in every reading (Q7).

---

#### (d) Decisions for the theorist

1. **Adopt, combine or reject readings 1, 2 and 3** (D1 to D4). D1 and D2 vary independently, so a fourth combination (selection equilibrium plus an uncertainty main effect) is available if wanted. I have not chosen among them, and `adoptedReading` is unset.
2. **Decide whether A13 is acceptable** given A1. If governance choosers are themselves boundedly rational, reading 1 needs an argument for why governance is chosen more accurately than contracts are written (Q2).
3. **Classify A5 and A9** as core or auxiliary (D3, Q12). This decides which assumptions later Interlocutor objections may target without abandoning the programme.
4. **Settle frequency (C4):** drop it, or state a relation for it (Q5).
5. **Confirm or revise A8.** Say what "fall between" means for hybrids, since the three-way P3 depends on it (Q6).
6. **Choose a coding rule for hybrids** when testing P5 and P6 against a binary integration outcome (Q7).
7. **Name an independent indicator** for comparative governance cost (C15) or for hazard (C8), or accept that both are read off asset specificity (Q8).
8. **Confirm the fact-status assignments** for P5 and P6 (provisionally novel), after historical verification (Q10).
9. **Approve, edit or reject the surfaced nodes:** A8, A10, A11, A13, A14, A15, S3, S4, P7, P8 and P9. None is in the text as given.

---

### B.2 Run 02: Explicator on Input B (resource-dependence theory)
*Instruction set: Foundry v0.1, Role 1. Input: case_inputs.md, Input B. Single run, unedited.*

---

#### 1. Segmentation

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

#### 2. Output (a): Theory object, Reading 1 ("decomposition reading")

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

#### 3. Reasons for classifications (steps 4 and 5)

##### 3.1 Assumption partition (Reading 1)

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

##### 3.2 Fact status of propositions

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

#### 4. Output (b): Further readings (fields that differ from Reading 1)

##### Reading 2 ("constraint-as-imbalance reading")

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

##### Reading 3 ("complementary reading")

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

##### Ensemble

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

#### 5. Output (c): Pivotal differences

| Pivot | Text | Reading 1 | Reading 2 | Reading 3 | Downstream propositions that change |
|---|---|---|---|---|---|
| **D-2 Meaning of "constraint"** (the pivot with the most consequences) | B.6 "faces high constraint from a partner", read with B.7 | A's unilateral dependence on B. P4 is a total effect that holds only if mutual dependence outweighs imbalance (surfaced A10) | Power imbalance against A. P4 holds only when mutual dependence is high (interaction). P6's sign is left open. P10 is surfaced | as Reading 1 | rd:P4 (unconditional vs interaction), rd:P6 (net negative vs undetermined sign), rd:A10 (needed vs not), rd:P10 (absent vs present), rd:R9 sign |
| **D-3 Status of the cost-minimization contrast** | B.8 "rather than the minimization of costs" | core (eliminative); P9 excludes cost-based explanation | core | auxiliary (assimilative); P9 becomes an incremental-variance prediction | rd:P9 (exclusion vs incremental), rd:D1 (needs A4 vs does not), stance justification strategy. Decides whether the Integrator should treat this theory's relation to Input A as rivalry or complementarity |
| **D-1 Power and dependence** | B.2 "that dependence is the source of other actors' power" | constitutive identity (power = dependence) | constitutive | causal (power has other sources and need not be exercised) | rd:P2 (definition vs testable prediction), rd:C4 entitlements, rd:R3 form. In Reading 3, rd:P4 to rd:P6 need a separate indicator of power |

---

#### 6. Output (d): Decisions for the theorist

1. **D-2: What does "constraint" mean in B.6?** Choose unilateral dependence (Reading 1, which then needs surfaced assumption rd:A10) or power imbalance against the focal organization (Reading 2, which makes rd:P4 an interaction and leaves rd:P6's sign open). Or supply a third definition.
2. **Which two dyadic quantities are primitive?** A's dependence on B, B's dependence on A, mutual dependence and imbalance are not independent. Also state the aggregation rule for mutual dependence (sum, mean or minimum).
3. **D-3: Is "rather than the minimization of costs" hard core or protective belt?** This choice determines whether the Integrator approaches Input A as a rival (Readings 1, 2) or a complement (Reading 3).
4. **D-1: Is power identical to dependence, or caused by it?** If caused, name an indicator of power that does not use dependence.
5. **rd:A8 (managerial discretion):** accept it as auxiliary, or reclassify it as core.
6. **Tactic choice beyond merger:** adopt, reject or amend the surfaced proposition rd:P10, which says when non-absorption tactics are predicted.
7. **Measurement:** the text commits to no indicator of dependence (rd:C1). Choose one that is independent of the observed ties, to avoid the circularity flagged at rd:C11.e1.
8. **Whether to send rd:D1** (the "therefore" in B.8) to the Argument Auditor as a possible case of deductive language covering an abductive inference.

---

### B.3 Run 03: Interlocutor (institutional lens) on the transaction-cost theory object
*Instruction set: Foundry v0.1, Role 2, lens = institutional. Input: Run 01, reading 1. Single run, unedited.*

---

#### 0. Lens and target

**Lens (institutional row).** Stance: constructivism. Ontology: organizational fields, institutional logics, legitimacy, taken-for-granted scripts. Preferred model classes: functional and constitutive explanation. Corroboration: inductivist, comparative-historical. Canonical corpus: Meyer & Rowan 1977; DiMaggio & Powell 1983; Scott 1995; Thornton, Ocasio & Lounsbury 2012.

**Target.** `tce:reading-1` ("economizing choice"), Run 01. In this reading discriminating alignment (tce:P3) comes from parties choosing the cheapest structure (tce:A4 core, tce:A13 auxiliary), and selection (tce:A12, tce:M4) is a backstop. Readings 2 and 3 are cited only where an objection would change under them.

**My position in one paragraph.** From where I stand, the theory explains a historically specific organizational form as if it were the timeless solution to a technical problem. Firm boundaries are institutional facts. What counts as a "transaction", what counts as "core", which boundary arrangements are legitimate, and what "efficient" means are all constituted within organizational fields, and they change with law, professions and dominant conceptions of control. A cost-minimizing account can always be told after the fact. That is precisely what Meyer & Rowan (1977) mean by a rationalized myth.

Convention: "(R01: id)" cites a node of the Run 01 object. "(inferred)" marks my inference rather than the text's.

---

#### 1. Objections, ranked by strength

##### O1. Economizing is asserted, not shown, to be the mechanism of boundary choice
- **Type:** 4 (disputed ontology and model class)
- **Targets:** tce:A4 (core), tce:R9 (teleological), tce:M3, tce:C15.com1, tce:P1
- **Objection.** Reading 1 explains governance through its consequences for cost (R01: R9, "teleological"; C15.com1). It never shows that the people who adopt a structure are responding to those consequences rather than to what their field defines as the proper way to organize. Organizations adopt formal structures because those structures are legitimate in their institutional environment, and they decouple the structures from technical activity (Meyer & Rowan 1977). Fields converge on forms through coercive, mimetic and normative isomorphism whether or not those forms are efficient (DiMaggio & Powell 1983). A correlation between asset specificity and integration (tce:P5) is therefore no evidence for tce:A4 until the institutional route to the same outcome has been ruled out. The object contains nothing that could rule it out, because it has no construct for field, logic or legitimacy (ontology list, R01 stanceProfile).
- **Strength:** **fatal to a core assumption (tce:A4)**, if the comparative-historical evidence in O2 and O6 holds. A4 is the positive heuristic (R01, reason table), and the only fallback in reading 1 is selection (A12), which O8 contests.
- **What would answer it.** The theorist would need to show that the effect of asset specificity on governance survives field-by-period controls for the prevailing template, for example field × era fixed effects, diffusion through board interlocks, and the adoption share among peers. The theorist would also need process evidence that cost comparisons came before adoption and were not written up as justification afterwards.

##### O2. Firm boundaries move in historical waves that transaction attributes do not explain
- **Type:** 5 (refuting evidence)
- **Targets:** tce:P1, tce:P3, tce:P5, tce:A4, tce:A10
- **Objection.** The large shifts in American firm boundaries line up with changes in antitrust law and in the dominant "conception of control": manufacturing, then sales and marketing, then finance (Fligstein 1990). They do not line up with any recorded change in asset specificity. The conglomerate was dismantled in the 1980s through takeovers and a shift in what investors and analysts would treat as a legitimate firm (Davis, Diekmann & Tinsley 1994). Analysts discounted diversified firms that did not fit their industry categories (Zuckerman 1999), which is a categorical penalty and not a governance cost. If boundaries change across whole populations while transaction attributes stay roughly constant, then the cross-section in tce:P5 shows the template of one era. It is not a law of alignment. That transaction attributes were roughly constant over these waves is my inference and is to be checked.
- **Strength:** **damaging.** It does not refute P5 within one era, but it removes P1 and P3 from the status of general explanations. The evidence those two works use concerns diversification more than vertical integration, so the transfer to vertical boundaries is partial.
- **What would answer it.** Show that changes in measured transaction attributes account for the timing of the waves. Otherwise add a scope condition that restricts P3 and P5 to one institutional regime. That condition concedes that the regime, not the transaction, fixes the baseline.

##### O3. Governance cost and hazard are read off the outcome they explain
- **Type:** 2 (tautological constructs)
- **Targets:** tce:C15, tce:C8, tce:C16, tce:P1, tce:P2
- **Objection.** The Explicator records that comparative governance cost has "no direct measure" and is read off asset specificity and the attributes of governance (R01: C15 measurementCommitments, C15.ent1; Q8). The hold-up hazard is likewise "read off asset specificity" (R01: C8). Alignment is then defined as the match with the structure that this cost predicts (R01: C16.ent1). P1 is an accommodation by the Explicator's own tagging. Any observed boundary can be redescribed as cost-minimizing once the right unobserved costs are imputed, and an institutionalist would expect exactly that redescription, because efficiency is the legitimating vocabulary of the modern firm (Meyer & Rowan 1977).
- **Strength:** **damaging.** It does not refute the theory. It makes P1–P3 untestable as stated, so only P5 and P6, which are stated in terms of observables, carry the empirical weight.
- **What would answer it.** An ex ante indicator of governance cost or hazard that is measured independently of the governance observed, together with a statement of which observed boundary pattern would count against tce:A4.

##### O4. Boundedly rational choosers follow scripts; tce:A13 is unentitled
- **Type:** 1 (unentitled commitment)
- **Targets:** tce:A13, tce:A1, tce:R9, tce:M3
- **Objection.** The theory says contract writers cannot anticipate contingencies (tce:A1), yet assumes that the same agents can identify the cost-minimizing governance structure ahead of time (tce:A13). Run 01 already flags this tension (Q2). Our tradition says where the gap is filled: under bounded rationality and ambiguity, organizations imitate those they see as successful or legitimate (mimetic isomorphism, DiMaggio & Powell 1983), and they adopt templates that consultants, lawyers and business schools carry (normative isomorphism). The text gives no entitlement condition for A13. It is surfaced only because the reading needs it.
- **Strength:** **damaging.** A13 is auxiliary in reading 1, but dropping it moves the theory to reading 2. That makes tce:A12 core, and O8 targets A12.
- **What would answer it.** Evidence from decision processes, such as board minutes, consultant reports or make-or-buy studies, showing comparative cost calculation rather than benchmarking against peers. Or adopt reading 2 and answer O8.

##### O5. The uncertainty interaction (tce:P6) is predicted equally well by mimetic isomorphism
- **Type:** 3 (accommodation dressed as prediction; rival explanation)
- **Targets:** tce:P6, tce:P5, tce:A11, tce:D3
- **Objection.** DiMaggio & Powell (1983) predict that uncertainty increases imitation of the field's modal form. Specific-asset industries in the US mid-century record (autos, aerospace, process industries) had integration as their modal template. In such fields, the institutional account produces the same positive specificity × uncertainty interaction that tce:P6 claims. That interaction rests on the surfaced bridge tce:A11, which is not in the text (R01: D3). The "novel" tag on P5 and P6 is provisional and still to be verified (R01: Q10). As a test, P6 discriminates nothing until it is estimated where the field template is *not* integration.
- **Strength:** **damaging.** It does not falsify P6, but it removes most of P6's power to corroborate tce:A4.
- **What would answer it.** Estimate P6 in fields whose modal form for high-specificity exchange is the hybrid, such as Japanese automotive supplier networks with dedicated assets under keiretsu-type relations (Dyer 1996, to verify; Gerlach 1992). The rival predicts that under high uncertainty firms converge on the hybrid, which is a negative interaction with integration there. TCE predicts a positive interaction everywhere.

##### O6. Hold-up hazard depends on the institutional environment, and the object has no construct for it
- **Type:** 1 (unentitled commitment)
- **Targets:** tce:C8.ent1, tce:R2, tce:A2 (core), tce:A9 (core), tce:S1
- **Objection.** C8.ent1 lets the theorist assert hazard from specificity, sunk cost, incompleteness and opportunism *alone*. Whether gaps get exploited depends on the regulative, normative and cultural-cognitive pillars around the exchange: courts, trade associations, business-group norms and patterns of authority (Scott 1995; Granovetter 1985 makes the embeddedness version). Hamilton & Biggart (1988) show that similar industries are organized as chaebol, keiretsu and family-firm networks in Korea, Japan and Taiwan. They trace the difference to patterns of legitimate authority, not to differences in transactions. tce:A2 treats opportunism as a constant of human nature. Ghoshal & Moran (1996) argue that hierarchical control can produce the opportunism it is meant to suppress, which makes A2 partly endogenous to governance.
- **Strength:** **damaging.** It forces a missing moderator into the core mechanism tce:M1. If the moderator dominates, A2's status as a universal premise fails.
- **What would answer it.** Add the institutional environment as a construct that moderates R2 and R3, and show that the specificity effect holds within institutional environments and *across* them with the same sign. Or narrow S1 to one legal-normative regime.

##### O7. The transaction is not a pre-institutional unit
- **Type:** 4 (disputed ontology)
- **Targets:** tce:A3 (core), tce:C1, tce:C1.ent1
- **Objection.** The theory takes the transaction as given (tce:A3), but the Explicator found "no rule for delimiting a transaction" (R01: C1 measurementCommitments). The only entitlement offered is that an exchange *could* be governed otherwise (C1.ent1). In our view, the categories that split activity into separable transactions, such as "core competence", "non-core function" or "outsourceable service", are field-level constructions that change with institutional logics (Thornton, Ocasio & Lounsbury 2012). The unit of explanation should be the field and its logic. The transaction attributes the theory treats as exogenous (cf. tce:A10) are partly products of that logic.
- **Strength:** **damaging.** This is a dispute about ontology and does not refute anything, but it undercuts tce:A10 and therefore the causal reading of P5.
- **What would answer it.** A delimiting rule for C1 that does not use current organizational practice. Evidence that the attribute measures used for C2 are stable when the field's categories change.

##### O8. Legitimate organizations survive misalignment
- **Type:** 5 (refuting evidence)
- **Targets:** tce:P4, tce:A12, tce:C18, tce:M4; also tce:A12.r2 under reading 2
- **Objection.** Institutional theory predicts that conformity to institutional rules secures resources and survival whatever the technical efficiency (Meyer & Rowan 1977). Meyer & Zucker (1989) document organizations that persist while performing poorly. Where legitimacy, regulation or state support buffer firms (tce:S2 already concedes this), selection cannot be the backstop for tce:A4. In reading 1 the gap in the choice mechanism (O4) is then covered by nothing.
- **Strength:** **damaging.** A12 is auxiliary in reading 1, so this is damaging and not fatal. Under reading 2, where A12.r2 is core, it would be fatal.
- **What would answer it.** Exit-hazard evidence (tce:P9, reading 2) showing misaligned firms exit faster after controlling for the legitimacy of their form, for example the form's prevalence in the field and its coverage by analysts.

##### O9. The founding exemplar of hold-up is historically contested
- **Type:** 5 (refuting evidence)
- **Targets:** tce:M1, tce:A9, tce:P5 (exemplar support)
- **Objection.** The GM–Fisher Body integration, the canonical hold-up case (Klein, Crawford & Alchian 1978), has been reread from archival evidence. Coase (2000) and Freeland (2000) argue that GM was not held up and that integration served managerial control and the retention of the Fisher brothers inside GM (to verify: exact claims of each). On a comparative-historical standard, the theory's paradigm case is better explained by intra-organizational politics.
- **Strength:** **minor.** One exemplar does not refute a general proposition, but it weakens the abductive support for tce:M1.
- **What would answer it.** Show that M1 is supported by cases selected without regard to outcome, not by a small number of illustrative cases.

##### O10. Hierarchy's safeguard depends on legitimate authority, not on ownership
- **Type:** 1 (unentitled commitment)
- **Targets:** tce:C12.ent1, tce:A6 (core), tce:R5
- **Objection.** C12.ent1 lets the theorist assert hierarchy from common ownership plus authority, and A6 then gives hierarchy the power to suppress opportunism. In our view, fiat works only when it is legitimate, which means employees and managers accept it as rightful. Ownership does not guarantee that acceptance. The suppression of opportunism is a property of the normative order inside the firm, not of the ownership boundary.
- **Strength:** **minor.** It refines A6 rather than defeating it.
- **What would answer it.** An entitlement condition for "authority" that is observable separately from ownership. Evidence that integrated transactions with contested authority still show reduced hazard.

**Count by strength:** fatal 1 (O1), damaging 7 (O2–O8), minor 2 (O9, O10).

---

#### 2. Rival explanation (AltGenX): field-template account of firm boundaries

**Claim.** The boundary arrangement for a class of exchanges is the template that is legitimate in the organizational field at the time. Law, the professions and the dominant conception of control install that template, and imitation spreads it, most strongly under uncertainty. Where it is used, efficiency talk is the rationale that legitimates the template, not what causes it to be adopted (Meyer & Rowan 1977; DiMaggio & Powell 1983; Fligstein 1990; Thornton, Ocasio & Lounsbury 2012).

**Mechanism.** Changes in law or logic redefine the legitimate firm. Early adopters adopt for technical reasons. Later adopters adopt for legitimacy, a pattern documented for civil-service reform (Tolbert & Zucker 1983) and for TQM, where early adopters customized the practice and later adopters conformed (Westphal, Gulati & Shortell 1997). The template becomes taken for granted, and transaction attributes are then defined and measured within the template's categories.

**How it reproduces the TCE regularities.** P5 appears in eras and fields whose template ties dedicated assets to ownership. P6 appears because uncertainty amplifies imitation of that template (O5). P3's hybrid band appears when alliance forms become legitimate.

**Discriminating predictions (where reading 1 and the rival part company).**

| # | Observable | Reading 1 (tce:A4, A13) | Field-template rival |
|---|---|---|---|
| X1 | Same transaction attributes, different nations or eras | Same governance | Governance follows the national or era template (O2, O6) |
| X2 | Sign of specificity × uncertainty (tce:P6) in a field whose modal form is the hybrid | Positive | Negative with respect to integration; uncertainty pushes firms toward the hybrid (O5) |
| X3 | Effect of peer adoption share, controlling for attributes | None | Positive and increasing over the diffusion curve |
| X4 | Early vs late adopters of a boundary change | Attributes predict adoption equally across the curve | Attributes predict early adoption only; late adoption is predicted by field prevalence |
| X5 | Exit of misaligned firms with legitimate forms | Higher hazard (tce:P4) | No higher hazard while the form is legitimate (O8) |

---

#### 3. Additions proposed to `openQuestions`

- Q13 (O1, O3): What observable boundary pattern would the theorist accept as evidence *against* tce:A4, as distinct from a pattern explained by an unobserved cost?
- Q14 (O2, O6): Should a scope condition restrict P3, P5 and P6 to one institutional regime, or should institutional environment enter as a construct moderating tce:R2 and tce:R3?
- Q15 (O5): Has P6 been estimated in any field whose modal form for high-specificity exchange is not integration? (To verify against the literature.)
- Q16 (O7): Can C1 be delimited without using the categories current in the field being studied?

#### 4. Derivation status

I checked no derivation and mark none closed. D1–D3 remain "asserted" (R01). O3 and O5 say that the empirical support for D2 and D3 does not single out the premises of tce:A4. They do not say that the derivations are invalid.

#### 5. Decisions for the theorist

1. **Accept, contest or defer O1.** Doing so decides whether tce:A4 must be defended against the field-template rival before P5 and P6 can count as corroborating it.
2. **Choose a response to O2 and O6:** either add an institutional-environment construct, or add a regime-restricting scope condition (Q14).
3. **Decide whether to keep tce:A13** (O4), or move to reading 2 and take on O8 at full strength.
4. **Supply an independent indicator for C15 or C8,** or accept that P1–P3 are not directly testable (O3, Q13).
5. **Decide whether to commission the discriminating tests X1–X5** (Role 6), especially X2, which bears on the "novel" status of P6.
6. **Have the citations marked "to verify" checked** (Dyer 1996; the specific claims of Coase 2000 and Freeland 2000), and confirm that the diversification evidence in O2 transfers to vertical boundaries.
7. **Rule on O9 and O10** (minor): no action, or revisions to the exemplar list for tce:M1 and to the entitlement condition for tce:C12.

---

### B.4 Run 04: Interlocutor (behavioral lens) on the transaction-cost theory object
*Instruction set: Foundry v0.1, Role 2, lens = behavioral. Input: Run 01, reading 1. Single run, unedited.*

---

#### 0. Lens and target

**Lens (behavioral row).** Stance: positivism with process realism. Ontology: boundedly rational decision makers, aspiration levels, routines, coalitions. Preferred model class: process and simulation models. Corroboration: inductivist, process-tracing. Canonical corpus: Simon 1947, 1955; March & Simon 1958; Cyert & March 1963; Kahneman & Tversky 1979; Greve 2003.

**Target.** `tce:reading-1` ("economizing choice"), Run 01. Basis convention: "(R01: id)" means the claim rests on that node of the Run 01 object. "(lens)" means it is a claim of my tradition, not of the text.

**Position.** I speak for the Carnegie tradition. We do not object that transaction-cost economics borrowed bounded rationality from us. We object that it borrowed the word and dropped the theory. In reading 1, bounded rationality limits only the people who write contracts (`tce:A1`). The people who choose governance are assumed to compare the costs of three discrete structures and pick the cheapest (`tce:A4`, `tce:A13`). A behavioral model of the firm makes the opposite assumption: governance is chosen by the same limited, satisficing, coalition-bound decision makers. Most of the objections below follow from that one point.

---

#### 1. Objections, ranked by strength

| Rank | Id | Type | Targets | Strength |
|---|---|---|---|---|
| 1 | beh:O1 | 1, 4 | tce:A4, tce:A13, tce:A1, tce:R9, tce:M3, tce:P3 | **fatal to a core assumption** (tce:A4 as stated in reading 1) |
| 2 | beh:O2 | 2 | tce:C15, tce:C16, tce:C8, tce:P1, tce:P3 | damaging |
| 3 | beh:O3 | 3 | tce:P5, tce:P6 | damaging |
| 4 | beh:O4 | 5, 3 | tce:P7, tce:C3, tce:A5 | damaging |
| 5 | beh:O5 | 1, 3 | tce:A10, tce:C2, tce:R13, tce:P5 | damaging |
| 6 | beh:O6 | 4 | tce:C17, tce:C9, tce:A3, tce:R9 | damaging |
| 7 | beh:O7 | 1 | tce:C6, tce:A2, tce:C8 | damaging |
| 8 | beh:O8 | 4, 5 | tce:A12, tce:C18, tce:P4, tce:M4 | minor (in reading 1) |
| 9 | beh:O9 | 1 | tce:C4, tce:C11, tce:A8 | minor |

Count: 1 fatal, 6 damaging, 2 minor.

---

##### beh:O1. Bounded rationality applies to contracting but not to the choice of governance
- **Type:** 1 (unentitled commitment), 4 (disputed model class).
- **Targets:** tce:A4 (core), tce:A13 (auxiliary in reading 1), tce:A1 (core), tce:R9 (teleological), tce:M3, tce:P3.
- **Objection.** Reading 1 says contracting parties cannot foresee contingencies (R01: tce:A1). It also says the same parties can identify, in advance, which of three governance structures minimizes the combined costs of hazard, bureaucracy and weakened incentives over the transaction's life (R01: tce:A13, tce:C15.com1). These two claims are inconsistent. Evaluating governance costs in advance requires anticipating exactly the contingencies that `tce:A1` says cannot be anticipated. Simon's (1955) decision maker does not optimize over alternatives. She searches sequentially until an alternative meets an aspiration level and stops there. Cyert & March (1963) add that search is *problemistic*: it starts when performance falls short and looks first near the current solution. Under that model, the decision process cannot produce cost-minimizing alignment. At most it produces local, history-dependent satisficing. The Explicator raised this tension (R01: Q2; Decision 2). I hold that it removes the support reading 1 gives to `tce:A4` (core), because `tce:A4` connects cost comparisons to outcomes only through `tce:A13`.
- **Why fatal.** In reading 1, `tce:A4` is core and `tce:A13` is the only route from `tce:C15` to `tce:C9` (R01: tce:R9, tce:M3). If `tce:A13` is withdrawn to protect `tce:A1`, reading 1 has no mechanism left for `tce:P3`. Retreating to selection (`tce:A12`) changes the reading to reading 2 (R01: D1). That makes the retreat a change of programme, not an adjustment in the protective belt.
- **What would answer it.** One of the following. (a) A *procedural* account of governance choice in which satisficing searchers with aspiration feedback converge on discriminating alignment, together with conditions on search breadth, feedback lags and aspiration updating, shown in a simulation (lens). (b) An explicit argument that governance choice is an easier problem than contract writing: fewer alternatives, coarser criteria, a repeated decision with learning. This would restate `tce:A13` as a claim about the task, and it would need evidence. (c) Adopting reading 2 and accepting its scope restriction (R01: S2.r2). Williamson's own phrase, "intendedly rational, but only limitedly so" (taken from Simon 1947), does not answer the objection. It names the inconsistency without resolving it.

##### beh:O2. The governance-cost construct is inferred from the outcome it explains
- **Type:** 2 (tautological construct).
- **Targets:** tce:C15, tce:C16, tce:C8, tce:P1, tce:P3.
- **Objection.** Comparative governance cost has "no direct measure" and is "read off asset specificity and governance attributes" (R01: tce:C15 measurementCommitments, tce:C15.ent1). The hazard is likewise "read off asset specificity" (R01: tce:C8). Alignment is defined as conformity to the rule `tce:P3` states (R01: tce:C16.ent1). So when a structure is observed, the theory is entitled to say it was the cheaper one. When it is not observed, the theory calls it misalignment, a cost that is not yet visible. `tce:P1` ("firms exist because...") then explains the existence of firms by a cost advantage that is attributed because firms exist. Simon (1991, *JEP*, "Organizations and markets") made a related complaint against the new institutional economics: its efficiency stories are fitted after the fact, and an auxiliary assumption can always be found to rationalize the observed form. A process theorist asks for the cost estimate the decision makers *actually formed* and the record of the comparison they *actually made*. Reading 1 supplies neither.
- **Strength:** damaging. It does not refute any core assumption. It takes away the evidential value of `tce:P1` and `tce:P3` until `tce:C15` has a measure independent of `tce:C9` (cf. R01: Q8).
- **What would answer it.** An indicator of governance cost recorded *before* the governance outcome and independently of it: for example, measured renegotiation frequency, dispute costs, or delivery-failure rates for comparable transactions under each structure. Alternatively, process-tracing of actual make-or-buy deliberations showing that a cost comparison of the theory's kind was made.

##### beh:O3. P5 and P6 do not distinguish this theory from a behavioral rival (AltGenX)
- **Type:** 3 (accommodation presented as prediction).
- **Targets:** tce:P5 (factStatus "novel", provisional), tce:P6 (factStatus "novel", provisional).
- **Objection.** A Carnegie model predicts the same signs for a different reason. Highly specific inputs are the ones whose supply problems hurt most and are most visible: a die for one customer, a co-located plant, firm-specific skills. A shortfall from aspiration on such an input is therefore more likely and more salient. It triggers problemistic search, and local search reaches "do it ourselves" first, because that alternative is under the decision maker's own control (Cyert & March 1963). This gives `tce:P5`. Under high uncertainty, shortfalls are more frequent and the organization's standing preference for *uncertainty avoidance* through a "negotiated environment" (Cyert & March 1963) is engaged more often. This makes the response to specificity-linked shortfalls steeper, which gives `tce:P6`. Neither prediction needs opportunism or cost minimization. The provisional "novel" status (R01: tce:P5, tce:P6; Q10) should be read in the Lakatosian sense: a fact is novel for the programme only if its rivals did not equally predict it. In the cross-section, these two facts are predicted equally well by the rival.
- **Strength:** damaging. Cross-sectional confirmations of P5 and P6 (Monteverde & Teece 1982; Masten 1984) remain evidence, but they do not count as severe tests of `tce:A4` against the behavioral rival.
- **What would answer it.** Predictions on which the two accounts diverge (see Section 2): the *timing* of integration relative to performance shortfalls, the role of prior in-house routines, and a main effect of uncertainty. Then evidence on those predictions.

##### beh:O4. Uncertainty acts by itself, and P7 forbids that
- **Type:** 5 (refuting evidence), 3.
- **Targets:** tce:P7 (surfaced), tce:C3.pre1, tce:A5 (core in reading 1).
- **Objection.** Reading 1 forbids uncertainty from raising integration when asset specificity is near zero (R01: tce:P7, tce:C3.pre1). Our tradition predicts the opposite main effect. Uncertainty avoidance is a general property of organizational decision making, not a moderator of hold-up (Cyert & March 1963). Kahneman & Tversky's (1979) loss aversion also makes a supply disruption weigh more than an equal expected saving from buying. The evidence I know of points our way. Walker & Weber (1984, *ASQ*) found that volume uncertainty and comparative production costs mattered for make-or-buy, while asset-specificity measures (supplier-market competition) had weak effects (to verify: exact variables and effect sizes). David & Han (2004, *SMJ*) reviewed the empirical TCE literature and reported that support for the uncertainty predictions was mixed and inconsistent, weaker than for asset specificity (to verify: tallies). If an uncertainty main effect holds, `tce:P7` is refuted and `tce:A5` ("decisive") is under pressure. Under reading 1 that is a core assumption.
- **Strength:** damaging. It would be fatal to `tce:A5` only if the theorist keeps `tce:A5` core and the main effect survives a test with specificity held near zero.
- **What would answer it.** A test restricted to low-specificity transactions that shows no uncertainty effect. Alternatively, a move to reading 3 (R01: A5.r3, P7.r3), which admits the main effect but explains it by `tce:A15` (adaptation costs) rather than uncertainty avoidance. The theorist should then show that A15 and uncertainty avoidance can be told apart.

##### beh:O5. Asset specificity is produced by routines and integration, not given before them
- **Type:** 1 (unentitled commitment), 3.
- **Targets:** tce:A10 (surfaced auxiliary), tce:C2, tce:R13, tce:P5.
- **Objection.** `tce:A10` treats asset specificity as fixed before, and independently of, governance. Specific skills and know-how are learned in the doing, and they are learned where the activity is carried out. A component made in-house builds firm-specific routines (March & Simon 1958, on performance programs). Those routines are what a later study codes as "specific human assets". Read this way, the engineering-effort measure in Monteverde & Teece (1982) is as much a *consequence* of prior integration as a cause of it (lens; to verify whether their design rules this out). Argyres (1996, *SMJ*) reports make-or-buy decisions driven by relative capabilities more than by hazard (to verify). The arrow in `tce:R13` may run backwards, or a common cause (the firm's history of routines) may drive both sides.
- **Strength:** damaging. `tce:A10` is auxiliary, so the core survives. But the causal reading of `tce:P5` does not survive without it (R01: D2 derivation note).
- **What would answer it.** Measures of specificity taken before the governance decision (e.g. new products or new transactions where no in-house routine yet exists), or an instrument for specificity. Plus a demonstration that prior in-house production of related items does not account for the specificity-integration association.

##### beh:O6. The decision maker is a coalition, not a single economizer, and governance changes in episodes, not continuously
- **Type:** 4 (disputed ontology and model class).
- **Targets:** tce:C17, tce:C9, tce:A3, tce:R9; stanceProfile.modelClasses ("teleological", "functional").
- **Objection.** Reading 1 has "parties" choose a governance structure for each transaction, as a comparative static (R01: tce:A3, tce:C1.lic1, tce:R9). In our ontology the firm is a coalition of participants with partly conflicting goals. Conflict is settled only partly ("quasi-resolution"), through sequential attention to goals and organizational slack (Cyert & March 1963). A make-or-buy decision is a bargaining outcome among, for example, purchasing, manufacturing and engineering, each with its own aspiration levels. Governance is also *sticky*: it changes in episodes, after problems, and rarely as continuous adjustment to a transaction attribute. The right model class is a process or simulation model with attention, aspiration and search rules (lens). A transaction-by-transaction discrete-choice model is not. `tce:A3` (the transaction as the unit) is a methodological choice we reject, not a finding.
- **Strength:** damaging. It is a rival programme's hard core, so it cannot refute `tce:A3` alone. It does predict observable patterns that reading 1 does not (Section 2).
- **What would answer it.** Evidence that governance choices across a firm's transactions are independent once transaction attributes are controlled, with no clustering by decision unit, by period or by preceding performance shortfall. Alternatively, an explicit statement that reading 1 is an "as-if" model of outcomes and makes no claim about process, with the scope consequences that follow (see beh:O1).

##### beh:O7. Opportunism is assumed without evidence, and it ignores what is known about fairness and norms
- **Type:** 1.
- **Targets:** tce:C6, tce:A2 (core), tce:C8.ent1.
- **Objection.** Opportunism is "held as a maintained assumption" with no measure (R01: tce:C6). Its entitlement condition depends on an assumption that opportunists cannot be identified in advance, which the Explicator surfaced and flagged (R01: tce:C6.ent1). Behavioral evidence shows that renegotiation is limited by fairness norms. Kahneman, Knetsch & Thaler (1986, *AER*) found that people judge it unfair to exploit a shift in bargaining power, and they punish those who do. Exchange relationships also build reputational and normative constraints over time. So the size of the hazard is a variable, and it should be measured, not assumed. Ghoshal & Moran (1996, *AMR*) argue further that assuming opportunism and governing to suit it can produce the behavior it assumes (to verify their exact claim; their argument is close to the institutional lens).
- **Strength:** damaging. `tce:A2` asserts only "some" opportunism (R01: s5b), so it is hard to refute. That same weakness makes `tce:C8` impossible to estimate.
- **What would answer it.** An indicator of opportunism risk at the level of the dyad (e.g. history of disputes, renegotiation attempts, or the partner's reputation), and a test showing that it moderates the effect of specificity on integration as `tce:R3` requires.

##### beh:O8. Selection is too weak to serve as a backstop
- **Type:** 4, 5.
- **Targets:** tce:A12 (auxiliary in reading 1), tce:C18, tce:P4, tce:M4.
- **Objection.** Organizational slack absorbs inefficiency in good times (Cyert & March 1963). Aspirations adapt downward after sustained poor performance (Greve 2003). Meyer & Zucker (1989, *Permanently Failing Organizations*) document organizations that persist at low performance. A misaligned transaction inside a large firm costs too little to affect the firm's survival (cf. R01: tce:C17.r2.lic1). `tce:P4` has no observable attached (R01: tce:P4, factStatus undetermined).
- **Strength:** minor in reading 1, where `tce:A12` is a backstop. It would be **fatal** under reading 2, where `tce:A12.r2` is core.
- **What would answer it.** Exit-hazard evidence by alignment status (R01: tce:P9), with slack and firm size controlled.

##### beh:O9. Frequency plays no role, and the ordering of hybrids is assumed
- **Type:** 1.
- **Targets:** tce:C4, tce:C11, tce:A8.
- **Objection.** Frequency enters no relation (R01: Q5). Our tradition gives it the role it obviously has: recurrence is the condition for *routinization* (March & Simon 1958). Recurrent transactions get standard operating procedures, and those procedures tie the activity to whoever performs it. The theory has left out its most behavioral variable. Hybrids are placed "between" market and hierarchy by assumption (R01: tce:A8, surfaced). The ordering is never derived.
- **Strength:** minor.
- **What would answer it.** A stated relation for `tce:C4`, and an argument or evidence for `tce:A8`.

---

#### 2. Rival explanation (AltGenX): problemistic search and routine replication

**Statement.** Make-or-buy outcomes are produced by boundedly rational coalitions. When an input's performance falls short of aspiration, problemistic search begins. Search is local, so it first reaches options under the firm's own control and options that use existing in-house routines. Integration therefore follows (i) salient supply shortfalls, which are more frequent for specific and uncertain inputs, (ii) a general preference for avoiding uncertainty, and (iii) prior in-house competence. Once adopted, governance persists through routine and inertia until the next shortfall. (Basis: Simon 1955; March & Simon 1958; Cyert & March 1963; Greve 2003.)

| Observable | Reading 1 (economizing choice) | Behavioral rival |
|---|---|---|
| Cross-section: integration rises with asset specificity (tce:P5) | yes | yes (shortfalls are more salient and more frequent) |
| Steeper slope under uncertainty (tce:P6) | yes | yes (uncertainty avoidance) |
| Uncertainty effect when specificity is near zero (tce:P7) | none | **positive** |
| Timing: integration shortly after a supplier performance shortfall, given attributes | no prediction | **yes** |
| Prior in-house production of related items raises make, given specificity | no (or only via specificity) | **yes** |
| Governance changes over time | tracks attribute changes | **episodic, sticky, clustered after shortfalls** |
| Decisions cluster by decision unit or coalition within the firm, given attributes | no | **yes** |
| Misaligned firms exit faster (tce:P4) | yes (backstop) | weakly or not, because of slack and aspiration adaptation |

The rows in bold are where the two accounts diverge. I pass them to the Empirical Validation Designer (Role 6) as candidate risky predictions.

---

#### 3. Open questions added (for `openQuestions`)

- **beh:Q1.** Can `tce:A13` be restated as a claim about the task (governance choice is easier than contract completion) and given its own evidence? If not, does reading 1 hold together at all? (beh:O1)
- **beh:Q2.** Is there a measure of `tce:C15` taken before, and independently of, the governance outcome? (beh:O2; extends R01: Q8)
- **beh:Q3.** Do the cited findings bear as stated? Walker & Weber 1984, David & Han 2004, Argyres 1996, Ghoshal & Moran 1996: exact findings to verify. (beh:O4, O5, O7)
- **beh:Q4.** Is Monteverde & Teece's (1982) specificity measure measured before integration? (beh:O5)
- **beh:Q5.** I am unsure whether the inconsistency in beh:O1 is fatal or only damaging. That depends on whether the theorist reads `tce:A4` as a claim about a process or as an "as-if" claim about outcomes. I have rated it on the process reading, which is the one reading 1 states (R01: tce:R9 "teleological").

---

#### 4. Decisions for the theorist

1. **Respond to beh:O1.** Choose one: (a) give a procedural account under which satisficing choosers produce alignment; (b) restate `tce:A13` as a claim about the task, with evidence; (c) move to reading 2 and accept its scope restriction; or (d) declare reading 1 "as-if" and give up its process claims. Only you can decide whether this objection is accepted as fatal.
2. **Decide whether `tce:P5` and `tce:P6` keep "novel" status**, given that the behavioral rival predicts them equally well (beh:O3).
3. **Decide the status of `tce:A5` and `tce:P7`** in light of the predicted uncertainty main effect (beh:O4). Keeping `tce:A5` core exposes it to refutation. Moving to reading 3 absorbs the effect, at the cost of `tce:A15`.
4. **Decide how `tce:A10` will be defended** (beh:O5): pre-decision measures, an instrument, or downgrading `tce:P5` to an association.
5. **Accept or reject `tce:A3`** as against the behavioral ontology, with the decision unit (coalition) as the actor (beh:O6).
6. **Decide whether opportunism (`tce:C6`) becomes a measured variable** (beh:O7).
7. **Decide whether to forward the diverging rows of Section 2 to Role 6** as risky predictions.

---

### B.5 Run 05: Model Builder on the transaction-cost theory object
*Instruction set: Foundry v0.1, Role 4. Input: Run 01, reading 1. Single run, unedited.*

---

Input: theory object `tce:reading-1` ("economizing choice") from Run 01. Reading 1 was adopted for this demonstration only; in real use the theorist adopts it. New ids below (`tce:A16`–`tce:A21`, `tce:D4`–`tce:D12`, `tce:P6.mb1`, `tce:P6.mb2`, `tce:P10`, `tce:model-1`) are provisional, and the Provenance Ledger may renumber them.

Convention: "(stated)" means the step uses only nodes in reading 1. "(surfaced)" means it uses a node I add here. No derivation is marked `closed`, because no checker exists. A derivation that seems to follow from its premises is `asserted`. A derivation that does not follow from the stated nodes is `open`, and the auxiliaries it needs are listed. A derivation for which I give a counter-example is `refuted`. That counter-example has also not been checked.

---

#### 1. Model class (step 1)

**Chosen:** an analytical **comparative-statics model of discrete governance choice**. Governance cost for each structure is a reduced form (in the spirit of Williamson 1991). It rests on a stylized **hold-up stage game**, and a **random-cost discrete-choice layer** produces the probabilities that P5 and P6 talk about.

**Why this class.**
- The stance profile lists `teleological` and `causal` model classes. Its inference norm is `deductive` ("therefore", s6; "It follows that", s9). Reading 1 makes alignment the outcome of cost-minimizing choice (A4, A13). Minimizing over three discrete alternatives is the most direct formal match for that.
- P5 and P6 (s11) are statements about a *probability*. So the model needs an explicit stochastic layer that links the deterministic optimum to observed frequencies. That layer is where the scale problem for P6 shows up (D9).

**Alternative named: property-rights incomplete-contracting game** (Grossman & Hart 1986; Hart & Moore 1990). In that game investment is endogenous, and ownership allocates residual control. I did not use it as the primary class, for two reasons:
- In that game integration does not remove hold-up. It only moves it to the other party. That contradicts A6 ("hierarchy suppresses opportunism", s7), which reading 1 holds as core.
- It replaces haggling and maladaptation costs with under-investment. Section 5 uses it as an expansion route instead (relaxing A10).

**Not used: an agent-based or replicator model.** That is the natural class for reading 2, where selection carries the explanation. Under reading 1 selection is only a backstop, so I leave P4 open (D11).

---

#### 2. Construct-to-variable map (step 2)

| Construct | Model object | Notes |
|---|---|---|
| tce:C1 Transaction | the unit indexed by $(k,u)$; one governance choice per unit | A3 (stated) |
| tce:C2 Asset specificity | $k \ge 0$, exogenous (A10); quasi-rent at stake $q(k)$, $q(0)=0$, $q'>0$ | the definition in s4 gives $q'>0$ |
| tce:C3 Uncertainty | $u \ge 0$ | enters only through $\pi(u)$ (A11) |
| tce:C5 Bounded rationality, tce:C7 Incompleteness | $\pi(u)\in(0,1)$: the probability that an uncontracted contingency arises; $\pi'>0$ | A1 makes $\pi>0$; A11 gives $\pi'>0$ |
| tce:C6 Opportunism | when a gap opens, the quasi-rent at stake is contested | A2 |
| tce:C8 Hold-up hazard | $\varphi(k,u)$: expected *dissipated* value per transaction, before safeguards; $\varphi(0,u)=0$ | the dissipation part needs A16 (surfaced) |
| tce:C9–C12 Governance | $g\in\{M,X,H\}$ (market, hybrid, hierarchy) | C9.com1 |
| tce:C12 safeguard (A6) | hazard pass-through $s_g$: $s_M=1>s_X>s_H\ge 0$ | A6; the hybrid's place in the order comes from A8 |
| tce:C13 Bureaucratic cost + tce:C14 Incentive weakening | fixed cost $\beta_g$: $\beta_M=0<\beta_X<\beta_H$ | A7, A8. C13 and C14 are merged into one parameter, since the text gives no separate role to either. |
| tce:C15 Comparative governance cost | $C_g(k,u)=\beta_g+s_g\,\varphi(k,u)$ | |
| tce:C16 Alignment | $g^*(k,u)=\arg\min_g C_g$; misalignment cost $C_g-C_{g^*}$ | |
| tce:C19 Vertical integration | the event $g=H$; $\Pr(H\mid k,u)$ | hybrids are coded as non-integrated (Run 01, Q7) |

**Not mapped.**
- **tce:C4 Frequency.** It enters no relation in reading 1 (Q5), and I did not invent one.
- **tce:C17 Firm.** It is mapped only as "a transaction with $g=H$" (C17.com1). Its role as a portfolio of transactions belongs to reading 2.
- **tce:C18 Competitive selection.** It is outside the model class (D11).

---

#### 3. Model specification (step 3)

**Primitives.** $k\in[0,\bar k]$, $u\in[0,\bar u]$; $q(\cdot)$, $\pi(\cdot)$; $(\beta_g,s_g)$ for $g\in\{M,X,H\}$; a dissipation share $d\in(0,1]$.

**Timing (the hold-up stage game).**
1. **t0.** The parties choose $g$ jointly and incur $\beta_g$ (A4, A13).
2. **t1.** The supplier sinks a specific asset. The quasi-rent $q(k)$ is now appropriable (A9, S1).
3. **t2.** With probability $\pi(u)$, a contingency arises that the contract does not cover (A1, A11).
4. **t3.** If it arises, an opportunistic party contests $q(k)$ (A2). Under market governance a share $d$ of the contested value is dissipated in haggling and maladaptation (**A16, surfaced**). Governance $g$ scales this loss by $s_g$ (A6, A8).

**Reduced form.** $\varphi(k,u)=d\,\pi(u)\,q(k)$ in the microfounded instance. The derivations below use a general $\varphi$ that satisfies:
- $\varphi(0,u)=0$ (C8.pre1);
- $\varphi_k>0$;
- $\varphi_u>0$ for $k>0$ (from A11 and C7.lic1, reading incompleteness as a positive moderator of R2).

The product form is one instance of this general $\varphi$. It is a modelling choice, and the text does not state it.

$$C_g(k,u)=\beta_g+s_g\,\varphi(k,u).$$

**Equilibrium concept.** The parties minimize expected governance cost: $g^*(k,u)=\arg\min_g C_g(k,u)$, given the reduced-form continuation from t3. This is subgame-perfect in the reduced game. A13 is what lets the t0 choosers optimize even though the t2 contract writers are bounded. The model represents the tension in Run 01's Q2 but does not resolve it.

**Observation layer.** Realized cost is $C_g+\varepsilon_g$, where the $\varepsilon_g$ are i.i.d. type-I extreme value with scale $\sigma$ and are independent of $(k,u)$ (**A20, surfaced**). This gives multinomial logit:
$$\Pr(g\mid k,u)=\frac{e^{-C_g/\sigma}}{\sum_h e^{-C_h/\sigma}}.$$
In the binary market-versus-hierarchy case, $\Pr(H)=\Lambda(z)$ with $z=[(1-s_H)\varphi-\beta_H]/\sigma$.

---

#### 4. Derivations (step 4)

##### D4 → tce:P2 (the market hazard rises with asset specificity)
1. The appropriable quasi-rent is $q(k)$, with $q'>0$ (C2 definition, s4; A9) (stated).
2. Exposure under the market is $\pi(u)\,q(k)$, and $\partial_k[\pi q]=\pi q'>0$ because $\pi>0$ (A1) (stated).
3. So the hazard **as exposure** rises with $k$.

**Status: `asserted`.**

The cost reading of P2 (R4: hazard → C15) is different. At t3 the contested rent is a *transfer* between the parties. If renegotiation is efficient ($d=0$), then $\varphi\equiv 0$, and governance cost does not depend on $k$ at all. So the step from "exposure" to "higher governance cost" (C8.com1, R4) **fails to close** on the stated nodes. One minimal auxiliary closes it:

**tce:A16 (surfaced).** Ex post renegotiation is inefficient: it dissipates a positive share of the value at stake. Equivalently, $\varphi_k>0$ for the *cost* hazard.

The alternative closure is to drop A10 and let investment be endogenous, so that the cost appears as under-investment (Section 5b). **D5 is `open` without A16, and A16 carries every downstream derivation.**

##### D6 → tce:P3 (discriminating alignment). This derivation fails to close.
1. Each $C_g$ is affine in $\varphi$, with slopes $s_M=1>s_X>s_H$ and intercepts $0<\beta_X<\beta_H$ (A6, A7, A8 first clause) (stated).
2. The lower envelope of affine functions is concave and piecewise linear. Along it, the structure that is chosen has a steeper slope the lower $\varphi$ is. So each structure is optimal on an interval of $\varphi$, and the intervals come in the order $M$, then $X$, then $H$, **if each is non-empty**.
3. The pairwise crossings are $\varphi_{MX}=\beta_X/(1-s_X)$, $\varphi_{XH}=(\beta_H-\beta_X)/(s_X-s_H)$ and $\varphi_{MH}=\beta_H/(1-s_H)$.
4. The hybrid is optimal on some interval **if and only if** $\varphi_{MX}<\varphi_{XH}$.
5. **Counter-example to closure on A8 as stated.** Take $s=(1,\,0.5,\,0)$, $\beta_H=1$ and $\beta_X=0.6$. The hybrid is intermediate in both safeguard and cost, exactly as A8's first clause requires. Yet $\varphi_{MX}=1.2>\varphi_{XH}=0.8$, so the hybrid is never chosen, and alignment is two-way (market, then hierarchy). The same happens at $\beta_X=0.5$, which is a knife-edge case. (Informal numeric check, item 1.)
6. **Minimal auxiliary, tce:A18 (surfaced): the hybrid is not dominated.**
   $$\frac{\beta_X}{1-s_X}<\frac{\beta_H-\beta_X}{s_X-s_H}.$$
   Geometrically, in (safeguard, fixed cost) space the hybrid's point $(s_X,\beta_X)$ lies strictly below the chord that joins market $(1,0)$ and hierarchy $(s_H,\beta_H)$. In words, the hybrid buys hazard reduction at a lower average cost than going straight to hierarchy.
7. **Mapping into $k$.** Since $\varphi_k>0$ (from D4 and A16), the $\varphi$-intervals become $k$-intervals $[0,k_{MX})$, $(k_{MX},k_{XH})$, $(k_{XH},\bar k]$.
8. For the hierarchy band to be non-empty on the support, the model also needs **tce:A17 (surfaced, range):** $\varphi(\bar k,u)>\varphi_{XH}$. A17 is shared with D7.

**Status: `open`.** Auxiliaries required: A16, A17, A18. With them the derivation seems to follow, and it would then be `asserted`.

**Diagnosis.** Run 01's A8 has two clauses: "intermediate in safeguards and costs, *so* the cost curves cross in that order". The "so" does not follow from what comes before it; the second clause *is* A18. I propose splitting A8 into A8a (intermediacy: the orderings of $s_g$ and $\beta_g$) and A18 (non-dominance).

##### D7 → tce:P1 (firms exist)
1. Firms exist iff some $(k,u)$ in the support has $g^*=H$, that is, $\varphi(k,u)>\max(\varphi_{XH},\varphi_{MH})$.
2. A7 ($\beta_H>0$) and A6 ($s_H<1$) give a *finite* threshold. Nothing in the text says the hazard ever reaches it.

**Status: `open`.** Auxiliaries required: A16, A17. P1 is an existence claim, and it needs the range assumption A17.

##### D8 → tce:P5 (Pr(integration) rises with asset specificity)
1. Under the logit layer, $\partial_k \ln\Pr(H)=\tfrac{1}{\sigma}\varphi_k\sum_g \Pr(g)\,(s_g-s_H)$.
2. Every term is non-negative, and the $g=M$ term is strictly positive. So the derivative is $>0$.
3. The result does not depend on the logit form. For any shock distribution independent of $k$, the event $\{C_H+\varepsilon_H<C_g+\varepsilon_g\ \forall g\}$ grows with $k$, because $C_H-C_g$ falls with $k$ for every $g\neq H$.

**Status: `asserted`.** Premises: A1, A2, A4, A6, A9, A10, A13. Auxiliaries required: A16, A20 (shocks independent of $k$). A18 is *not* needed: P5 survives even if hybrids are never chosen. (Informal numeric check, item 4.)

##### D9 → tce:P6 (steeper in $k$ when $u$ is high), on the probability scale as s11 states it. Refuted.
In the binary case, with $c=(1-s_H)/\sigma$:
$$\partial^2_{ku}\Pr(H)=\Lambda'(z)\,c\,\big[(1-2P)\,c\,\varphi_k\varphi_u+\varphi_{ku}\big].$$

**Counter-example.** Take $\varphi=uk$, which *satisfies* every auxiliary in this run, including A19 below. Set $\beta_H=1$, $s_H=0.1$, $\sigma=1$. At $(k,u)=(3,1)$, $P=0.846$, and the bracket equals $1+(1-2P)\,0.9\cdot 3=-0.87<0$. So $\partial^2_{ku}P\approx-0.10$. At $(1,1)$, $P=0.475$ and the cross-partial is $+0.23$. (Informal numeric check, item 3.)

When integration is already likely, the probability saturates, and higher uncertainty *flattens* the slope in $k$. This is the logit/probit interaction problem of Ai & Norton (2003).

**Status: `refuted`** as a global claim about the probability scale. The counter-example is asserted and has not been checked by a Proof Verifier.

**Sufficient restriction.** If $P\le 1/2$ and A19 holds, the cross-partial is positive.

##### D10 → tce:P6.mb1 (proposed restatement: the cross-partial on the **log-odds / latent-cost** scale is positive). Fails to close.
1. $\text{logit}\Pr(H\text{ vs }M)=[(1-s_H)\varphi-\beta_H]/\sigma$, so $\partial^2_{ku}=(1-s_H)\varphi_{ku}/\sigma$.
2. The sign is therefore the sign of $\varphi_{ku}$. The same holds for $H$ versus $X$, with factor $(s_X-s_H)$.
3. **What the stated nodes give.** $\varphi(0,u)=0$ (C8.pre1, consistent with P7), $\varphi_u>0$ for $k>0$ (A11 and C7.lic1), and $\varphi_k>0$. Together these imply only $\int_0^k\varphi_{ku}\,dk'=\varphi_u(k,u)>0$: the interaction is positive *on average from zero*, not at every point.
4. **Counter-example.** $\varphi=k+u\,k\,e^{-k}$ on $u\in[0,7]$ satisfies every stated condition: $\varphi(0,u)=0$, $\varphi_u=ke^{-k}>0$, and $\varphi_k=1+ue^{-k}(1-k)>0$ for $u<e^2$. But $\varphi_{ku}=(1-k)e^{-k}<0$ for $k>1$. (Informal numeric check, item 2.)
5. **Minimal auxiliary, tce:A19 (surfaced): the hazard is supermodular in specificity and uncertainty.** $\varphi_{ku}\ge 0$ everywhere, and $>0$ somewhere. In words, uncertainty raises the hazard *per unit* of specificity, not only its level. The product form $\pi(u)q(k)$ is a sufficient instance. The relation R2 lists C7 as a moderator but gives no sign or functional form, so the text does not supply A19.

**Status: `open`.** Auxiliaries required: A11, A16, A19. With them the derivation would be `asserted`.

##### D12 → tce:P6.mb2 (alternative restatement: the specificity threshold for integration falls with uncertainty). Closes without A19.
1. Define $k^*(u)$ by $\varphi(k^*,u)=\varphi_{XH}$ (or $\varphi_{MH}$).
2. By the implicit function theorem, $dk^*/du=-\varphi_u/\varphi_k<0$, using $\varphi_u>0$ and $\varphi_k>0$.
3. Under any symmetric shock layer, $k^*(u)$ is the $k$ at which $\Pr(H)$ crosses its median.

**Status: `asserted`.** Premises: A1, A2, A4, A6, A9, A11, A13. Auxiliaries: A16, A17. **A19 is not needed.**

This "threshold" form of s11 carries less auxiliary load than either slope form. The theorist may prefer it.

##### D11 → tce:P4 (misalignment raises costs and leads to exit)
- **The cost clause.** $C_g\ge C_{g^*}$ holds by the definition of $g^*$ (A4). It is analytically true inside the model, so on reading 1 it has no empirical content. **Status: `asserted` (definitional).**
- **The exit clause.** It needs population dynamics (A12, S2) that this model class does not contain. **Status: `open`**, not attempted. I recommend a replicator or agent-based model under reading 2.

##### D13 → tce:P7 (no effect of uncertainty when specificity is near zero)
$\varphi(0,u)=0$, so $C_g(0,u)=\beta_g$ for every $g$, and $\Pr(g\mid 0,u)$ does not depend on $u$. (Informal numeric check, item 4: $\Pr(H\mid 0,u)=0.1745$ at $u=0.5$ and at $u=2$.)

**Status: `asserted`.** Premises: C8.pre1, together with reading 1's exclusion of A15. Note that this result holds *by construction*: the model contains no channel through which uncertainty affects cost when specificity is zero.

##### Derivation table

| Id | Target | Premises (stated) | Method | Status | Auxiliaries required |
|---|---|---|---|---|---|
| tce:D4 | P2 (exposure) | A1, A2, A9, C2 | symbolic | asserted | none |
| tce:D5 | P2 / R4 (cost) | A1, A2, A9 | game-theoretic | **open** | **A16** (or relax A10) |
| tce:D6 | P3 | A4, A6, A7, A8a, A13 | symbolic | **open** | A16, A17, **A18** |
| tce:D7 | P1 | A4, A6, A7, A13 | symbolic | **open** | A16, **A17** |
| tce:D8 | P5 | A1, A2, A4, A6, A9, A10, A13 | symbolic | asserted | A16, A20 |
| tce:D9 | P6 (probability scale) | as D8, plus A11 | symbolic | **refuted** (counter-example asserted) | none restores it globally; P ≤ 1/2 restriction suffices |
| tce:D10 | P6.mb1 (log-odds scale) | as D8, plus A11 | symbolic | **open** | A16, **A19**, A20 |
| tce:D12 | P6.mb2 (threshold shift) | as D8, plus A11 | symbolic | asserted | A16, A17 |
| tce:D11 | P4 | A4; A12, S2 | verbal | asserted (cost clause); open (exit clause) | dynamic model |
| tce:D13 | P7 | C8.pre1, A4 | symbolic | asserted (by construction) | A16 |

**Informal check.** sympy is not installed in this environment, and the run rules forbid installing packages. Instead I ran a plain-Python script (`scratchpad/mb/check.py`, not published). It does finite-difference and grid checks of items 1–6, which are cited above. This is *not* a checker run, and every status stays as given.

---

#### 5. Contraction and expansion (step 5)

##### (a) Contraction: remove core tce:A1 (bounded rationality, so contracts are complete)
Then $\pi\equiv 0$, so $\varphi\equiv 0$ and $C_g=\beta_g$. The market is chosen for every $(k,u)$, because $\beta_M=0$. (Numeric check, item 6.)

**What fails:** P1, P2 (cost), P3, P5 and P6.

**What survives:** P7 holds trivially, and P4 becomes vacuous.

Removing A2 (opportunism) or A6 (hierarchy safeguards, $s_H\to 1$, which makes $H$ dominated by $M$) has the same effect on P1.

**Finding.** P6 needs more than A1 holding. A1 must be **graded**: incompleteness $\pi(u)$ has to *vary* with $u$, via A11. Run 01 treats A1 as a maintained constant ("held as a maintained assumption, not a variable", C5 measurement; C5.ent1). So the interaction prediction quietly turns a hard-core *constant* into a *variable* of the belt. The theorist should decide whether that is acceptable.

##### (b) Expansion: add tce:A21 (natural auxiliary): hybrid safeguards degrade with uncertainty, $s_X'(u)>0$
A21 says hybrids adapt poorly to frequent disturbances. It is in the spirit of Williamson (1991) (to verify: exact formulation and page).

**Result 1: A18 becomes uncertainty-dependent.** The hybrid band vanishes once
$$s_X(u)\ \ge\ \bar s=1-\frac{\beta_X(1-s_H)}{\beta_H}.$$
With $\beta_X=0.3$, $\beta_H=1$, $s_H=0.1$ this gives $\bar s=0.73$. The hybrid's $\varphi$-band is $(0.50,\,2.33)$ at $u=0.5$ and has width $0.17$ at $u=2$. It is empty by $u=2.5$. (Numeric check, item 5.)

**New proposition, tce:P10 (proposed, surfaced):** at intermediate specificity, the share of hybrid governance falls with uncertainty, and at high uncertainty alignment becomes two-way (market, then hierarchy). P10 is a novel, testable consequence that reading 1 does not contain.

**Result 2: P6 is partly rescued without A19, for hierarchy versus hybrid.** $\partial^2_{ku}\,\text{logit}(H\text{ vs }X)=[s_X'(u)\varphi_k+(s_X-s_H)\varphi_{ku}]/\sigma$. The first term is positive, so a mildly negative $\varphi_{ku}$ is tolerated. The contrast of hierarchy against the *market* is unchanged and still needs A19.

**Result 3: P7 survives,** because $C_X(0,u)=\beta_X$ still does not depend on $u$.

**Alternative expansion, noted only.** Relax A10 so that specificity is chosen jointly with governance. This is the route of the Section 1 alternative model class. It could replace A16, because the cost would come from under-investment. But $k$ would then be endogenous to $g$, and the causal reading of P5 would require an instrument. That is a handoff to the Empirical Validation Designer.

---

#### 6. Surfaced assumptions

| Id | Statement | Proposed status | Needed by |
|---|---|---|---|
| tce:A16 | Ex post renegotiation over a contested quasi-rent is inefficient: it dissipates a positive share $d$ of the value at stake, through haggling or maladaptation. | auxiliary | D5–D8, D10, D12, D13 (all cost-based derivations) |
| tce:A17 | Range: at the top of the observed specificity range, the hazard exceeds the hierarchy threshold, $\varphi(\bar k,u)>\varphi_{XH}$. | auxiliary | D6, D7, D12 |
| tce:A18 | Hybrid non-dominance: $\beta_X/(1-s_X)<(\beta_H-\beta_X)/(s_X-s_H)$. This replaces the "so" clause of A8. | auxiliary | D6 |
| tce:A19 | Supermodularity: $\varphi_{ku}\ge 0$. Uncertainty raises the hazard per unit of specificity. | auxiliary | D10 |
| tce:A20 | Unobserved governance-cost shocks are independent of $(k,u)$; logit form for the closed-form results. | auxiliary (econometric) | D8–D10 |
| tce:A21 | Hybrid safeguards degrade with uncertainty, $s_X'(u)>0$. | auxiliary (expansion only; not needed by any reading-1 proposition) | P10 |

All have `explicitness: "surfaced"` and `surfacedBy: "Model Builder (Role 4), run 05"`.

---

#### 7. Checker-ready statements (step 6)

These are written for a SymPy backend (symbols positive unless noted). None has been run.

```
# common
k,u,sig,bX,bH,sX,sH,d = symbols(..., positive=True); q,pi = Function('q'), Function('pi')
phi = d*pi(u)*q(k)                       # product instance; general phi for D10
C = {M: phi, X: bX + sX*phi, H: bH + sH*phi}
assume: 1 > sX > sH >= 0, 0 < bX < bH, q(0)=0, q'(k)>0, pi'(u)>0 (A11), d>0 (A16)

D4 : prove diff(pi(u)*q(k), k) > 0
D6 : prove  [A18] => solve(C[M]-C[X]) < solve(C[X]-C[H])   (in phi);
     counterexample check: subs(sX=1/2,sH=0,bH=1,bX=3/5) => phiMX > phiXH
D8 : PH = exp(-C[H]/sig)/Sum(exp(-C[g]/sig)); prove diff(log(PH),k) > 0
D9 : P = 1/(1+exp(-((1-sH)*u*k - bH)/sig)); evaluate diff(P,k,u) at (k=3,u=1,sH=1/10,bH=1,sig=1) < 0
D10: prove diff(phi,k,u) >= 0 => diff((1-sH)*phi - bH, k, u) >= 0;
     counterexample: phi2 = k + u*k*exp(-k): check phi2(0,u)=0, diff(phi2,u)>0 (k>0),
     diff(phi2,k)>0 (u<e**2), diff(phi2,k,u) < 0 at k=2
D12: kstar defined by phi(kstar,u)=const; prove idiff(...) = -phi_u/phi_k < 0
D13: prove diff(C[g].subs(k,0), u) == 0 for all g
Exp: sbar = solve(bX/(1-s) - (bH-bX)/(s-sH), s) == 1 - bX*(1-sH)/bH
```

---

#### 8. Decisions for the theorist

1. **Model class.** Accept the comparative-statics/discrete-choice class, or require the property-rights game. The game would contradict A6 unless A6 is moved to the belt.
2. **A16 (inefficient renegotiation).** Accept it, or relax A10 instead. Without one of them, hazard is a transfer and not a cost, and P1–P6 lose their cost basis.
3. **Split A8** into A8a (intermediacy) and A18 (non-dominance), and decide whether to accept A18. Rejecting it leaves P3 `open` and makes alignment two-way.
4. **How to state P6.** Choose among three versions. The probability scale as in s11 is `refuted` globally. The log-odds scale (P6.mb1) needs A19. The threshold shift (P6.mb2) needs no A19. This choice also binds the Empirical Validation Designer.
5. **A1 as constant or graded.** Decide whether A1 may be graded via A11, which turns a core constant into a variable (Section 5a).
6. **Accept or reject A17, A19, A20,** and decide whether to adopt the expansion A21 together with its new prediction P10.
7. **P4's exit clause.** Decide whether to commission a dynamic model (replicator or agent-based) for it, which belongs to reading 2.

**openQuestions (added):**
- **MB-Q1.** Does "steeper" in s11 refer to probabilities, log-odds or thresholds? The text does not say, and the answer changes P6's status.
- **MB-Q2.** Is dissipation $d$ itself a function of governance or of uncertainty? If $d$ rises with $u$, A19 becomes easier to satisfy. The text is silent.
- **MB-Q3.** How do A13 (choosers optimize) and A1 (contract writers are bounded) coexist inside one agent? The model represents both but does not reconcile them (Run 01, Q2).
- **MB-Q4.** Frequency (C4) remains unmapped, as in Run 01 Q5.

---

### B.6 Run 06: Argument Auditor on the transaction-cost exposition
*Instruction set: Foundry v0.1, Role 5. Input: case_inputs.md Input A, anchored to Run 01 reading 1. Single run, unedited.*

---

Scope and conventions. I audit Input A as the theorist's own exposition, using Run 01's segmentation (s1 to s11, with s5 split into s5a and s5b) and the ids of reading 1 ("economizing choice"). Adopting reading 1 is the theorist's decision; I use it here only because the demonstration proceeds on it. "(text)" means the passage states it. "(inferred)" means I infer it. Every literature citation is marked "(to verify)" except Toulmin (1958) and the Williamson works named in the input's own header. No derivation (tce:D1 to tce:D3) is marked closed, because no checker has run.

---

#### 1. Argument map (ArgMap, Toulmin scheme)

The exposition has one top-level claim (tce:P1, s1) and one empirical payoff (tce:P5, tce:P6, s11). In between is a chain of eleven steps. "Stated" in the warrant column means the text gives the warrant. Otherwise the warrant is missing from the text, and the missing-warrant id (W1 to W11) points to section 2.

| Step | Claim (id) | Grounds (data) | Warrant | Backing | Qualifier | Rebuttal conditions | Argument form |
|---|---|---|---|---|---|---|---|
| AM1 (s1) | Firms exist because some transactions are governed more cheaply by hierarchy than by market (tce:P1) | Firms exist (accommodated fact, Run 01 fact status) | Structures that govern more cheaply are the ones that come to exist. This is tce:A4, unstated here (W1) | None given | None. Stated categorically | Firms that exist for reasons other than governance cost | Functional explanation; inference to the best explanation |
| AM2 (s2-s3) | Transactions vary on three dimensions (tce:A3), and asset specificity is decisive (tce:A5) | None | None (W2) | None | None | Other dimensions do as much work | Bare assertion. Its status (stipulation or empirical weighting) is unclear: see Run 01, D3 |
| AM3 (s4) | A party that has sunk a specific investment is exposed to opportunistic renegotiation (tce:R2, tce:C8) | Examples: a dedicated die, a co-located plant, firm-specific skills (tce:C2.ent1) | Quasi-rents that are sunk can be appropriated (tce:A9). The text states this, but it is not sufficient on its own (W3) | Examples only | "once the investment is sunk" (scope tce:S1) | Reciprocal specificity; ex ante pricing of the risk | Argument from mechanism |
| AM4 (s5a) | Parties cannot write complete contracts (tce:R1, tce:C7) | Parties are boundedly rational (tce:A1) | A complete contract requires anticipating every contingency (stated) | None | None | Incompleteness can also arise from unverifiability, without bounded rationality | Deduction from a definition |
| AM5 (s5b) | Gaps in contracts *will* be exploited (tce:R3) | *Some* parties are opportunistic (tce:A2) | Opportunists cannot be screened out or disciplined (W4) | None | "some" in the premise, but none in the conclusion | Reputation, repeated dealing | Generalization from a disposition |
| AM6 (s6) | *Therefore* markets become hazardous as asset specificity rises (tce:P2, tce:R4) | AM3, AM4, AM5 | Market governance has no safeguard that grows with specificity (W5) | None | "as ... rises" (comparative) | Hostages, bonds, reputation premia, courts | Mechanism aggregated to the level of the governance form |
| AM7 (s7) | Hierarchy suppresses opportunism and permits adaptation by fiat (tce:A6, tce:R5), but carries bureaucratic costs and weakens incentives (tce:A7, tce:R6, tce:R7) | A definition: common ownership plus authority (tce:C12) | Common ownership removes the incentive or the ability to hold up, and hierarchy cannot replicate market incentives at no cost (W6) | None | None | Hold-up and influence activity inside the firm | Assertion of comparative properties |
| AM8 (s8) | Hybrids fall between market and hierarchy (tce:C11) | Examples: long-term contracts, alliances | Hybrids are intermediate in *both* safeguards and costs, so the three cost curves cross in order (tce:A8, surfaced in Run 01) (W7) | None | None | Hybrids may be dominated, or ranked by uncertainty rather than by specificity | Classification by example |
| AM9 (s9) | *It follows that* governance aligns discriminatingly: low specificity with market, intermediate with hybrid, high with hierarchy (tce:P3, tce:D1) | AM6, AM7, AM8 | Choosers identify and pick the structure with the lowest cost (tce:A4, tce:A13), all three structures are feasible (tce:S3), and governance cost is the only cost that differs (W8) | None | None | Production-cost differences; boundedly rational choosers (Run 01, Q2) | Comparative-institutional inference to an optimum (teleological) |
| AM10 (s10) | Misaligners *will* incur higher costs and *will* be selected out (tce:P4, tce:R11, tce:R12) | AM9 | Selection is strong, fast and acts on the relevant unit (tce:A12, tce:S2; tce:A14 from reading 2) (W9) | None | "over time" | Weak competition; dilution across the firm's portfolio (Run 01, D4) | Argument from selection |
| AM11 (s11) | We *should observe* that Pr(integration) rises with asset specificity (tce:P5), more steeply when uncertainty is high (tce:P6) | AM9 | P5: tce:A10 exogeneity, identification of tce:C19 with tce:C12, and a coding rule for hybrids (W10). P6: uncertainty raises incompleteness (tce:A11), and hazard is supermodular in specificity and incompleteness (W11) | None | "probability" | Endogeneity of specificity; a flexibility motive under uncertainty | Hypothetico-deductive prediction |

Structural observations, inferred from the map:
- **No step carries backing.** The exposition relies on stated premises and illustrative examples. It cites no evidence and no formal result. Every warrant therefore rests on the theorist's say-so, and that is the main thing a referee would ask to be filled.
- **The chain splits at AM9/AM10.** AM9 reaches alignment by choice; AM10 reaches it by selection. In reading 1, AM10 is a backstop. The prose, however, offers both and does not say which one carries the inference (Run 01, D1).
- **The dimensions dangle.** Uncertainty (tce:C3) enters no step between s2 and s11. Frequency (tce:C4) enters no step at all. As a result, AM11's interaction claim has no grounds within the exposition.

---

#### 2. Warrant gaps

Each gap gives the step, the warrant that is missing (stated explicitly), and what depends on it. There are **11 gaps**.

| Gap | Step | Missing warrant, stated explicitly | Load-bearing for |
|---|---|---|---|
| W1 | AM1 (s1) | "If structure g governs transaction t more cheaply than the alternatives, then t comes to be governed by g, through choice (tce:A13) or selection (tce:A12)." s1 states the explanandum and the cost comparison, but not the mechanism that turns lower cost into existence. | tce:P1 |
| W2 | AM2 (s3) | Either (a) "asset specificity accounts for more of the variation in governance than uncertainty or frequency" (empirical), or (b) "we take asset specificity as the programme's organizing variable" (methodological). The text gives neither ground, and the two options give tce:A5 different statuses (Run 01, D3). | tce:A5, so tce:P3, tce:P5, tce:P7 |
| W3 | AM3 (s4) | "The counterparty is not equally locked in, and the hazard is not neutralized ex ante by price or by reciprocal commitment." Exposure needs asymmetric bargaining power after the investment is sunk. Bilateral specificity produces bilateral monopoly, not one-sided exposure. | tce:R2, tce:M1 |
| W4 | AM5 (s5b) | "Opportunistic parties cannot be identified ex ante, and reputation or repeated dealing does not deter them." Without this, "some are opportunistic" does not give "gaps *will* be exploited". Note that frequency (tce:C4), which the text introduced and then dropped, is exactly the variable that would govern this warrant. | tce:R3, tce:M1 |
| W5 | AM6 (s6) | "Market contracting has no safeguard (hostage, bond, reputation premium, court enforcement) that scales with specificity." Without this, rising specificity raises the *stakes* but not necessarily the *hazard* under the market. | tce:P2, tce:R4 |
| W6 | AM7 (s7) | "Placing both sides under common ownership removes the opportunism that tce:A2 attributes to contracting parties. Equivalently, the behavioural assumptions tce:A1 and tce:A2 bind less on employees and divisions than on independent contractors. And hierarchy cannot both replicate market incentives and add fiat (tce:C13.pre1)." The text applies bounded rationality and opportunism to market parties only and says nothing about them inside the firm. | tce:A6, so tce:P1, tce:P3, tce:P5. Core |
| W7 | AM8 (s8) | "Hybrids are intermediate in safeguards *and* in costs, so that the cost curves of market, hybrid and hierarchy each cross once, in that order, as specificity rises" (tce:A8; single crossing). | The three-way form of tce:P3 |
| W8 | AM9 (s9) | "Governance is chosen by parties who can rank structures by cost and who choose the cheapest (tce:A4, tce:A13). All three structures are feasible (tce:S3). Production costs (for example, an outside supplier's scale economies) do not differ, or do not offset governance-cost differences." The text compares only governance costs. | tce:P3, tce:D1 |
| W9 | AM10 (s10) | (i) "Alignment" is defined by cost minimization (tce:C16), so "misaligned firms incur higher costs" is close to analytic. (ii) The selection part needs this warrant: "Competition is strong enough, and the cost penalty from misaligned transactions is large enough at the level of the *firm*, to reduce survival within the observation window" (tce:A12, tce:S2, tce:A14). | tce:P4 |
| W10 | AM11 (s11), P5 | "Asset specificity is fixed before governance and independently of it (tce:A10). Vertical integration is the observable counterpart of hierarchy (tce:C19.com1). Hybrids are coded consistently (Run 01, Q7)." | tce:P5, tce:D2 |
| W11 | AM11 (s11), P6 | "Uncertainty raises contractual incompleteness (tce:A11), and the hold-up hazard rises in specificity *more* when incompleteness is greater (complementarity)." The exposition gives no step from which P6 could follow. | tce:P6, tce:D3 |

---

#### 3. Inference-mode check: deductive language covering abductive or inductive moves

| Step | Deductive marker (text) | Actual mode | Mismatch? | Why |
|---|---|---|---|---|
| AM1 (s1) | "Firms exist because" | Abductive (functional explanation) | Borderline. **Not counted** | "because" is explanatory, not inferential. It is still categorical where a qualifier ("can be explained by") would be accurate. It also inherits W1. |
| AM4 (s5a) | "cannot" | Deductive from a definition | No | Valid if "complete" means "anticipates every contingency". It is near-trivial for that reason. |
| AM5 (s5b) | "gaps in contracts **will** be exploited" | Inductive or probabilistic generalization | **Yes (MM1)** | From "some" parties, only "may be exploited, with probability depending on the share of opportunists and on screening" follows. "Will" asserts certainty. |
| AM6 (s6) | "Markets **therefore** become hazardous" | Deductive over an enthymeme whose missing premise (W5) is empirical (inductive) | **Yes (MM2)** | "Therefore" is valid only if the suppressed premise holds, and that premise is a contested empirical claim about market safeguards. |
| AM9 (s9) | "**It follows that** transactions are aligned" | Abductive or teleological. It needs unstated behavioural premises (tce:A4, tce:A13) and an unstated structural premise (tce:A8) | **Yes (MM3). The most consequential** | "It follows" presents a comparative-institutional *hypothesis* about how governance is chosen as if it were a *theorem* of s4 to s8. Even with A8, the inference to observed alignment adds an empirical behavioural claim. tce:D1 remains "asserted". |
| AM10 (s10) | "**will** incur higher costs and, over time, **will** be selected out" | First clause near-analytic (W9-i). Second clause inductive (argument from selection) | **Yes (MM4)** | Selection arguments yield tendencies under conditions (tce:S2, tce:A12, tce:A14), not certain outcomes. |
| AM11 (s11) | "we **should** observe ... and more steeply when uncertainty is high" | P5: hypothetico-deductive, given W10. P6: abductive or imported, because there is no derivation in the text | **Yes for P6 (MM5)**; no for P5 | "Should" signals a derived prediction. P5 has a derivation sketch (via P3). P6 has none, since uncertainty does no work in s4 to s10. |

Count: **5 mismatches** (MM1 to MM5), plus one borderline case that is not counted (AM1).

Pattern (inferred): the deductive vocabulary is concentrated at the joints where the exposition moves from *dyadic mechanism* to *governance-level outcome* (s6, s9, s10). Those are the places where behavioural or empirical premises are needed and not stated.

---

#### 4. Defeaters (ArgDef-INTRA): one per warrant, from within transaction-cost and organizational economics

| Warrant | Defeater (from within the field) | Effect if it holds |
|---|---|---|
| W1 | Agency and managerial-discretion arguments: managers integrate for private benefits such as empire-building or free-cash-flow use, not for governance-cost savings (Jensen 1986, to verify). | Existence of hierarchy no longer licenses the inference to lower governance cost. tce:P1 becomes one explanation among several. |
| W2 | Early make-or-buy studies found volume or technological uncertainty, or the comparison of production costs, at least as predictive as specificity in some samples (Walker & Weber 1984, to verify). | tce:A5 reads as an empirical weighting claim (reading 3, tce:A5.r3), not a hard-core postulate. |
| W3 | Credible commitments: reciprocal specific investments and hostages make exposure mutual and self-enforcing (Williamson 1983, to verify). Quasi-rent appropriation presupposes asymmetric lock-in (Klein, Crawford & Alchian 1978, to verify). | Specificity alone does not give one-sided exposure, so tce:R2 needs an asymmetry condition. |
| W4 | Reputation and relational contracting in repeated exchange sustain cooperation without integration (Baker, Gibbons & Murphy 2002, to verify; Macaulay 1963, to verify). | "Will be exploited" fails for recurrent transactions. This gives frequency (tce:C4) a negative relation to hazard, which the text omits. |
| W5 | Reputational premia (Klein & Leffler 1981, to verify). Long-term contracts whose duration rises with specificity (Joskow 1987, to verify). | Rising specificity can be met *within* contracting, so the market-to-hierarchy step in s6 and s9 is not forced. |
| W6 | Property-rights theory: integration does not abolish hold-up; it reallocates residual control rights, and with them the incentive distortion, to the other party (Grossman & Hart 1986, to verify). Influence activities inside hierarchies (Milgrom & Roberts 1988, to verify). | tce:A6 becomes a comparative empirical claim with conditions, not a property of common ownership. tce:P1 and tce:P3 then depend on *which* party's investment matters more. |
| W7 | Williamson (1991) himself argues that hybrids lose viability as the frequency of disturbances rises, so their position depends on uncertainty as well as on specificity. Later work treats hybrids as having distinct mechanisms rather than as a midpoint (Ménard 2004, to verify). | The single-crossing ordering by specificity alone (tce:A8) fails at high uncertainty, so the three-way tce:P3 needs an uncertainty condition. |
| W8 | Production-cost economies of outside suppliers, who aggregate demand, are traded off against governance costs (Riordan & Williamson 1985, to verify). Choosers are themselves boundedly rational (Run 01, Q2). | Governance-cost minimization alone does not fix the aligned structure, and tce:D1 needs a production-cost term. |
| W9 | Selection arguments yield optimality only under strong conditions, and inefficient routines can persist (Alchian 1950, to verify; Nelson & Winter 1982, to verify). | tce:P4 holds as a tendency at most. In reading 1 this weakens the backstop. In reading 2 it weakens the core (tce:A12.r2). |
| W10 | Specificity and governance are chosen jointly: integrated firms invest in more specific assets *because* they are integrated. Surveys flag endogeneity and measurement problems in the make-or-buy literature (Lafontaine & Slade 2007, to verify). | The tce:P5 coefficient is not a causal effect of specificity unless tce:A10 is defended or instrumented. |
| W11 | Under technological uncertainty, firms may prefer *not* to integrate in order to keep the flexibility to switch suppliers or technologies (Balakrishnan & Wernerfelt 1986, to verify). | The sign of the uncertainty term, and possibly of the interaction in tce:P6, is contested within the field. |

---

#### 5. Arbitration (Arbiter-INTRA): conflicts with canonical findings

1. **tce:P5: broadly consistent.** Surveys of the make-or-buy literature report that the positive association between measures of asset specificity and integration is among the more robust findings (Shelanski & Klein 1995, to verify; Macher & Richman 2008, to verify). No conflict, but see W10 on causal interpretation.
2. **tce:P6 and the role of uncertainty: mixed record.** The same surveys report that uncertainty effects are inconsistent in sign and significance (to verify). The exposition presents P6 with the same confidence as P5 ("we should observe"). The canonical record does not support that equal confidence. P6 should carry a weaker qualifier.
3. **tce:A6 and tce:P1: theoretical conflict.** Grossman and Hart (1986, to verify) is a canonical result within the field. It denies that common ownership as such suppresses hold-up, which is the claim s7 asserts. The exposition does not engage with it. This is a substantive, not a presentational, conflict.
4. **tce:P3 against tce:P5: internal tension sharpened by evidence.** Joskow (1987, to verify) finds that high specificity is often governed by long-term contracts (hybrids), not by integration. This is consistent with three-way tce:P3, but it means that a binary test of tce:P5 that codes hybrids as "not integrated" will understate the effect of specificity (Run 01, Q7).
5. **Testability (meta-logical norm).** tce:C15 (comparative governance cost) has no measure independent of the alignment it explains (Run 01, Q8). Together with W9-i, this leaves tce:P1 and tce:P3 open to the long-standing charge that transaction-cost explanations are ex post rationalizations (a critique associated with, for example, Ghoshal & Moran 1996, to verify). P5 and P6 are the exposition's only escape from that charge, and they rest on W10 and W11.

---

#### 6. Additions proposed for `openQuestions` (not adopted)

- Q13 (W6): Does the theorist hold that tce:A1 and tce:A2 apply inside hierarchies? If they do, what removes hold-up there?
- Q14 (W8): Should comparative governance cost (tce:C15) be widened to total cost (governance plus production)?
- Q15 (W4): Should frequency (tce:C4) enter as a moderator of tce:R3, with recurrence lowering the hazard through reputation?
- Q16 (MM3, MM4): Should "It follows that" (s9) and "will" (s5b, s10) be replaced with qualified language until a checker closes tce:D1?

---

#### Decisions for the theorist

1. **Accept, reject or amend each of the 11 warrant gaps** (W1 to W11). For each accepted gap, choose whether to state the missing warrant as an explicit assumption, which assumptions would be new and which are surfaced ids already, or to weaken the claim instead.
2. **Decide how to handle the five mode mismatches** (MM1 to MM5). Requalify the prose, or supply derivations to be sent to the checker (tce:D1, tce:D3 first). In particular, decide whether s9's "It follows that" is to be defended as a derivation or restated as a hypothesis.
3. **Respond to W6 and Arbitration 3** (property-rights challenge to tce:A6). The options are to restrict scope, to condition A6 on whose investment matters, or to argue that the challenge does not apply. This touches the hard core.
4. **Set the confidence level for tce:P6** relative to tce:P5, given the derivation gap (W11) and the mixed record (Arbitration 2).
5. **Decide whether to add a production-cost term** (W8) and a frequency relation (W4), which would close Run 01's Q5.
6. **Approve or reject the proposed open questions Q13 to Q16.**
7. **Verify, or have verified, every literature citation marked "(to verify)"** before any defeater or arbitration point is entered in the Provenance Ledger.

---

### B.7 Run 07: Integrator on transaction-cost and resource-dependence theory objects
*Instruction set: Foundry v0.1, Role 3. Inputs: Run 01 reading 1, Run 02 reading 1. Single run, unedited.*

---

**Inputs.** `tce:reading-1` ("economizing choice", Run 01) and `rd:reading1` ("decomposition reading", Run 02). Both are reading 1 of their ensembles. Neither reading has been adopted by a human; the demonstration proceeds on them by stipulation. Prose sources: Inputs A and B, `case_inputs.md`.

**Conventions.** "(text)" means the theory object states it, with the inference id. "(inferred)" means the inference is mine. Where a pass or fail rests on an inference that the Explicator itself marked as inferred, I say so. Operators are used in their ordinary Project Lakatos sense. *Augment* adds elements of Y to X with X's core intact. *Integrate* builds a new object whose core contains elements of both. The appendix text available to me does not give fuller operator definitions; see Decision 7.

---

#### 1. Candidate pairs, re-voiced in a neutral vocabulary (Translator/Re-Voicer)

Each construct is restated by what it licenses, using only these neutral terms: *A* and *B* are two parties to a recurrent exchange; *exit loss* is what A loses if the A–B exchange ends; *ex post leverage* is B's ability to change terms after A has committed; *common ownership* is both sides under one owner; *governance cost* is the cost of running the exchange under a given arrangement.

| # | TCE construct (licenses, re-voiced) | RD construct (licenses, re-voiced) | Why considered |
|---|---|---|---|
| 1 | **tce:C2 Asset specificity.** A has a sunk investment whose value outside A–B is much lower (C2.com1). Licenses: B's ex post leverage over A rises (C2.com2, with C6 and C7); P(common ownership) rises (C2.lic1, P5); band of the investment maps to arrangement (C2.lic2). | **rd:C1 Resource dependence (A on B)**, built from rd:C2 importance and rd:C3 alternatives. A's exit loss is high (C1.c2). Licenses: B has power over A to the same degree (C1.l1, strict); A's managers take a tactic aimed at B (C1.l2). | Both are A's exit loss in the A–B exchange, and both license "B gains ex post leverage" and "common ownership becomes more likely." |
| 2 | **tce:C15 Comparative governance cost** (with tce:A4). Licenses: the arrangement with the lowest governance cost is the one adopted (C15.com1, C15.lic1). | **rd:C8 Managerial goals** (with rd:A4, rd:C18). Licenses: the arrangement that reduces outside control and uncertainty is the one adopted (C8.l1). rd:C18.p1 *precludes* "boundary set by minimizing costs." | Both name the criterion that picks the arrangement, that is, what makes an activity fall inside or outside the boundary. |
| 3 | **tce:C6 Opportunism.** A disposition of some parties. Licenses: given gaps (C7), a party with sunk specific assets will face renegotiation (C6.lic1); unenforced promises are no safeguard (C6.pre1). | **rd:C4 Power (B over A).** A structural capacity, constituted by dependence (C4.e1). Licenses: A's autonomy is lower (C4.l1); tactic choice follows both sides' power (C4.l2). What power *does* is only inferred (C4.c1: "the text does not say"). | Both are what turns A's exposure into an actual loss for A. |
| 4 | **tce:C3 Uncertainty.** An attribute of the transaction. Raises contractual incompleteness (C3.com1, surfaced A11). Licenses only a steeper slope of integration on specificity (C3.lic1). In reading 1 it precludes a main effect at near-zero specificity (C3.pre1, P7). | **rd:C9 Uncertainty.** A state of the focal organization about the supply and terms of resources. Caused by dependence (rd:R5). Licenses: managers are more motivated to adopt a tactic (C9.l1), with no specificity condition. | The same word in both texts. |
| 5 | **tce:C12 Hierarchy** (observed as tce:C19 vertical integration). Common ownership *with authority and administrative control* (C12.pre2). Licenses: opportunism suppressed and fiat available (C12.com1); bureaucratic cost and weaker incentives (C12.com2); not aligned at low specificity (C12.pre1). | **rd:C12 Absorption.** An event: a merger or acquisition. Licenses: B's resources are internal to A and B has no external power over A (C12.e1, C12.l1). No cost commitments. Licensed whenever mutual dependence is high (rd:P5). | Both are coded from the same observable: a common-ownership event between A and B. |
| 6 | **tce:S3** (surfaced scope): all three structures are feasible for every transaction. TCE has no construct for *who can* integrate. | **rd:C7 Power imbalance, rd:C17 Feasibility of absorption.** Licenses: the weaker side wants to absorb but is less able to (C7.l1, rd:R13); infeasible absorption is unlikely even when motivated (C17.l1). | One theory assumes what the other models. |
| 7 | **tce:C11 Hybrid.** Long-term contracts and alliances. Licenses: aligned at intermediate specificity (C11.lic1); not at the extremes (C11.pre1). | **rd:C14 Negotiated long-term arrangement, rd:C13 Co-optation.** Licenses: lower supply uncertainty for the term (C14.l1); a co-opted B is less likely to use power (C13.l1). RD gives no condition under which these are chosen over absorption (Run 02, openQuestion 5). | The same observables (long-term contracts, joint ventures and alliances). |
| 8 | **tce:C4 Frequency.** Licenses nothing in the text (C4.lic1). | **rd:C2 Resource importance.** Licenses: dependence rises (C2.l1). | Considered because a recurring input might be read as an important one. Rejected: C4 has no licensed inference, so no role to compare. **No alignment.** |

Considered and set aside without a pair: tce:C18 competitive selection has no RD construct counterpart. RD's nearest node is an assumption, rd:A8 ("not only through the selection of organizations"), so the two sides do not form a construct pair. tce:C17 Firm vs rd:C18 Organizational boundary: both are entitled by ownership or administrative control (tce:C17.ent1, rd:C18.e1), and every difference in their licenses is carried by pair 2. Listing them separately would count that difference twice.

---

#### 2. Classification of each pair

**L1. Bridge (scope-restricted): tce:C2 ↔ rd:C1 (via rd:C2, rd:C3).**
- *Shared licenses* over the shared scope: (i) if X(A,B) rises, B's ex post leverage over A rises (tce:C2.com2 / tce:C6.lic1; rd:C1.l1 with rd:C4.c1); (ii) if X(A,B) rises, P(A and B under common ownership) rises (tce:C2.lic1, tce:P5; rd:C5.l1, rd:P4); (iii) if the A–B asset or resource is as good elsewhere, X is absent (tce:C2.pre1; rd:C1.p1).
- *Entitlement link, one-way.* A sunk investment worth much less outside A–B means that B's custom is important to A and that A has few alternatives for that asset. That meets rd:C1.e1, which is strict. So tce:C2 entitles rd:C1 (inferred). The converse fails. A firm buying a generic input from a monopolist has high rd:C1 (importance plus few sources) and zero tce:C2: it has no relationship-specific investment, and tce:C8.pre1 excludes a hazard.
- *Shared scope:* dyads in which A's dependence on B is created by A's sunk, relationship-specific investment, that is, tce:S1 ∩ rd:S2. Outside that scope the two come apart, and that gap generates the rivalry test in L2.

**L2. Rivalry: tce:C15 (+ tce:A4) ↔ rd:C8 (+ rd:A4, rd:C18).**
- *Conflict.* tce:C15.com1 commits to "the lowest-cost structure is the one adopted," and tce:A4 is core. rd:C18.p1 precludes "A's boundary is set by minimizing ... costs," and rd:A4 is core in reading 1. Both are hard-core, so this is a conflict between negative heuristics, not belt against belt. TCE's tce:C12.pre1 excludes hierarchy as aligned at low specificity; RD's rd:P5 and rd:C6.l1 license absorption whenever mutual dependence is high, with no specificity condition.
- *Divergent observable.* The incidence of common ownership among dyads with **high mutual dependence and low asset specificity**, for example a critical but generic input with few suppliers, where neither side has made a relationship-specific investment. TCE reading 1 predicts market governance there (tce:P3, tce:C10.lic1). Where integration does occur, TCE calls it misaligned and predicts higher cost and lower survival (tce:P4). RD reading 1 predicts elevated merger incidence (rd:P5, rd:P7) and attaches no cost or survival penalty. The measurement precondition: dependence must be indexed independently of specificity, for example by input-output transaction shares, the indicator Run 02 names (to verify that the cited literature used this), and specificity by a separate engineering or co-location measure.

**L3. Complementarity: tce:C6 + tce:C7 (tce:A2) → rd:C4.**
- *Open assumption in RD.* What power does, and when it is exercised. rd:C4.c1 is the Explicator's inference ("the text does not say what power does"). Reading 3's alternative role makes this explicit: power "need not be exercised."
- *Discharging commitment in TCE.* tce:A2 with tce:C7: leverage is exercised where contracts leave gaps and the advantaged party is opportunistic ("gaps in contracts will be exploited," s5b).
- *Why not a bridge.* Substitute power for opportunism in tce:A2: "because some parties have power, gaps in contracts will be exploited." RD reading 1 does not license "will be exploited," since it is silent on exercise. And under high mutual dependence RD licenses cooperative absorption "attractive to both sides" (rd:A6), not exploitation. The roles differ: TCE's is a behavioural disposition held everywhere, RD's a structural capacity that varies by dyad. They fit together rather than substitute.

**L4. Equivocation: tce:C3 ↔ rd:C9 ("uncertainty").**
- The same word with different inferential roles. TCE: exogenous, transaction-level, acting only through contractual incompleteness, and precluding an integration effect at near-zero specificity (tce:C3.pre1, tce:P7). RD: endogenous to dependence (rd:R5), organization-level, licensing a direct motive for any tactic (rd:C9.l1).
- Substitution shows the clash. Inserting rd:C9 into tce:P7 gives "when asset specificity is near zero, resource uncertainty does not raise integration," and RD licenses the contrary (rd:C9.l1 → rd:C11 → rd:C12). Not a bridge. A study that pools "uncertainty" measures across the two literatures would be testing two different constructs.

**L5. Equivocation: tce:C12 / tce:C19 ↔ rd:C12 (common ownership coded as "vertical integration" vs "merger/absorption").**
- The same observable with different roles. TCE hierarchy requires authority and administrative control (tce:C12.pre2), carries costs (tce:C12.com2) and is precluded at low specificity (tce:C12.pre1). RD absorption is an event that carries no cost, is licensed by mutual dependence alone, and includes horizontal and conglomerate mergers.
- Partial overlap. tce:C12.com1 ("opportunism suppressed") matches rd:C12.l1 ("B no longer has external power over A"). "Fiat," however, has no RD counterpart.
- Substitution: tce:C12.com1 → *partial pass*. tce:C12.com2 ("absorption carries bureaucratic cost") → *fail*: RD is silent, so it does not license it. tce:C12.pre1 ("absorption not aligned at low specificity") → *fail*: rd:P5 licenses the contrary. An acquired unit run as an autonomous subsidiary counts as absorption but not as hierarchy. Flagged so that no test counts one M&A event as evidence for both theories.

**L6. Complementarity: rd:C7 + rd:C17 → tce:S3.**
- *Open assumption in TCE.* tce:S3, surfaced by Run 01, says all of market, hybrid and hierarchy are feasible for every transaction. TCE has no account of who can integrate, or when integration fails although it would be cheaper.
- *Discharging commitment in RD.* rd:R13 and rd:C17.l1: the weaker side of an imbalanced dyad is less able to absorb, and infeasible absorption is unlikely whatever the motive. rd:C16.p1: a side that does not depend on the other has, within RD, no motive to absorb it.
- This turns TCE's surfaced scope assumption into a variable.

**L7. Complementarity (conditional on L1 and tce:A8): tce:C11 → rd:C13 / rd:C14.**
- *Open assumption in RD.* When co-optation or negotiated arrangements are chosen instead of absorption. Run 02 openQuestion 5 says only absorption is tied to power positions. P10 addresses this but is reading 2 only.
- *Discharging commitment in TCE.* tce:C11.lic1 aligns hybrids with intermediate specificity. Read through L1, intermediate dependence that arises from specific investment goes to long-term contracts, joint ventures or alliances.
- *Limits.* This covers only dependence inside L1's scope, and it leaves RD's fourth tactic, diversification (rd:C15), with no TCE counterpart. Its strength is borrowed from tce:A8, which is surfaced and auxiliary.

---

#### 3. Substitution test for the bridge (L1)

The test replaces the construct in two of the first theory's propositions and checks whether the second theory licenses the result.

| Test | Original (TCE) | After substitution | Does RD reading 1 license it? | Result |
|---|---|---|---|---|
| T1 | tce:P5: "The probability of vertical integration increases with asset specificity." | "The probability of vertical integration [of A and B] increases with A's dependence on B." | Yes, via rd:P4 ("holding B's dependence on A constant, P(merge) increases with A's dependence on B"). rd:D2 is asserted only and needs the surfaced rd:A10 (the mutual-dependence effect outweighs the imbalance effect). It also requires reading "vertical integration" as "merger," which is equivocation L5. | **PASS, conditional** on rd:A10 and on a common-ownership coding of the outcome |
| T2 | tce:P2: "The hazard of market governance increases with asset specificity." | "The hazard of market governance increases with A's dependence on B." | Yes. rd:C1.l1 (strict): dependence gives B power over A. rd:C4.c1: B can press demands A would otherwise refuse, which is A's ex post exposure. But rd:C4.c1 is the Explicator's inference, not B-text. | **PASS, conditional** on rd:C4.c1 |
| T3 (reverse, robustness) | rd:P1: "A's dependence on B increases with importance and decreases with alternative sources." | "A's asset specificity increases with importance and decreases with alternative sources." | TCE does not license it. Specificity is the value of A's own investment in its next-best use (tce:C2.pre1), not the number of sources of an input. | **FAIL** |
| T4 (reverse, robustness) | rd:P5: "P(merge) increases with mutual dependence, holding imbalance constant." | "P(merge) increases with bilateral asset specificity, holding asymmetry of specificity constant." | Weakly. tce:P5 licenses integration rising with either party's specificity. Reading 1 says nothing about symmetry. | **PASS (weak)** |

**Verdict.** The required test (T1, T2), run from TCE's side, passes, conditionally both times. The reverse test fails at T3. L1 is therefore a **one-directional, scope-restricted bridge**: tce:C2 behaves as a *special case* of rd:C1 (dependence created by sunk specific investment) and not as its equivalent. No other pair was a bridge candidate after re-voicing. L5 was the closest, and it fails substitution on 2 of 3 inferences (Section 2).

---

#### 4. Candidate integrations (at most two)

##### I1. Augment(TCE, RD): "feasibility-constrained alignment"
- **Operator:** Augment. TCE is the host, and its core (tce:A1–A6, A9) is unchanged.
- **Kept from TCE:** the hold-up mechanism (tce:M1), economizing (tce:A4), discriminating alignment (tce:P3), and the cost of hierarchy (tce:A7).
- **Kept from RD:** power imbalance (rd:C7) and feasibility of absorption (rd:C17, rd:R13) replacing tce:S3 (L6); power read as the locus of leverage, exercised under opportunism (L3); asset specificity as one source of dependence (L1).
- **Inferential price.** *TCE* gives up tce:S3, a surfaced auxiliary, at small cost. It must then accept **persistent misalignment that is not a cost anomaly**: a high-specificity dyad that stays unintegrated because the exposed party is too weak to integrate. Under reading 1 that is currently an anomaly for P3. TCE also newly assumes a measure of imbalance that is independent of specificity. *RD* gives up nothing in its belt, but its constructs enter only as auxiliaries of a cost-minimizing core. That is incompatible with rd:A4 as core, so RD would have to accept a role it explicitly rejects in reading 1 (D-3).
- **PrisM prediction (neither theory alone):** *The slope of P(integration) on the investing party's asset specificity is flatter when the investing party is the weaker side of a power imbalance.* This is a specificity × imbalance interaction, and the predicted response in such dyads is more hybrids and co-optation instead of ownership.
  - TCE alone predicts a slope that does not depend on imbalance (tce:P5, tce:P6).
  - RD alone has no specificity term.
  - Adjacent discipline (contract theory): the integrated model also implies lower specific investment by weak-side suppliers. This is consistent with property-rights arguments (Grossman & Hart 1986; to verify the fit) but is not derived from either input.

##### I2. Integrate(TCE, RD): "two-criterion dyadic boundary choice"
- **Operator:** Integrate. The new core contains elements of both.
- **Structure.** The boundary choice for dyad A–B weighs governance cost (tce:C15) against managerial autonomy and uncertainty reduction (rd:C8). Dependence is split into a specificity-generated part (the L1 scope) and a residual from importance and scarcity that is not specificity-based.
- **Kept from TCE:** tce:M1, tce:M2 and tce:A7 (hierarchy is costly), and competitive selection tce:C18 / tce:A12 as the force that penalizes non-cost boundaries.
- **Kept from RD:** rd:C1–rd:C7, rd:A3, and the managerial-discretion assumption rd:A8.
- **Inferential price.** *TCE* gives up tce:A4 as the **sole** positive heuristic, so economizing becomes one criterion of two (a hard-core change). It gives up tce:A3: the transaction is no longer the sole unit, since the unit becomes the dyad. *RD* gives up rd:A4 in its reading-1 form, the hard-core "rather than the minimization of costs"; this is RD reading 3, so the theorist would have to change readings (D-3). It must also newly accept that absorption is costly (tce:A7, which RD lacks). *Both* newly assume a weighting parameter and an indicator of dependence that is independent of specificity. Without that indicator the integration cannot be tested (Run 02, the circularity flag at rd:C11.e1).
- **PrisM prediction (neither theory alone):** *The effect of non-specificity dependence on integration is larger where competitive selection is weak* (regulated, protected or concentrated industries), and close to zero where it is strong. The integrated model reads this as a dependence × competitive-intensity interaction: political boundaries survive only where selection is too weak to remove their cost.
  - TCE alone predicts no effect of non-specificity dependence at any level of competition.
  - RD alone predicts an effect that does not depend on competition (rd:P5, rd:P7, and rd:S3–S4 name no competition condition).

---

#### 5. Inferential distance (draft definition, appendix D §4.3)

*Definition:* 1 minus the share of considered construct pairs classified as bridges, weighted by the number of licensed inferences involved. A pair with no alignment counts as distance 1.

*Operationalization (mine; flagged).* A pair's weight is the number of `licenses` entries of its two constructs in the input objects. An entry that says the construct licenses nothing counts 0. A scope condition counts 0.

| Pair | Kind | Licenses (TCE + RD) | Weight | Bridge weight |
|---|---|---|---|---|
| L1 tce:C2 ↔ rd:C1 | bridge | 2 (lic1, lic2) + 2 (l1, l2) | 4 | 4 |
| L2 tce:C15 ↔ rd:C8 | rivalry | 1 + 1 | 2 | 0 |
| L3 tce:C6 ↔ rd:C4 | complementarity | 1 + 2 | 3 | 0 |
| L4 tce:C3 ↔ rd:C9 | equivocation | 1 + 1 | 2 | 0 |
| L5 tce:C12 ↔ rd:C12 | equivocation | 1 + 1 | 2 | 0 |
| L6 tce:S3 ↔ rd:C17 | complementarity | 0 + 1 | 1 | 0 |
| L7 tce:C11 ↔ rd:C14 | complementarity | 1 + 1 | 2 | 0 |
| (8) tce:C4 ↔ rd:C2 | no alignment | 0 + 1 | 1 | 0 |
| **Total** | | | **17** | **4** |

**Inferential distance = 1 − 4/17 = 13/17 ≈ 0.76.**

Sensitivity:
- Unweighted: 1 − 1/8 = 0.875.
- Excluding the unaligned pair: 1 − 4/16 = 0.75.
- Counting L1 at half weight because it is one-directional: 1 − 2/17 ≈ 0.88.

**Measurement note for the schema authors.** The draft gives a rivalry, a complementarity, an equivocation and "no alignment" the same distance, 1. The rivalry in L2 is the *most* commensurable relation found here: it names a shared observable on which the two theories conflict. A distance that cannot tell it apart from an unrelated pair is likely to misstate how far apart the theories are. Suggested revision: bridge 0, complementarity 0.25, rivalry 0.5, equivocation 0.75, none 1 (illustrative weights, not calibrated). Under those weights the distance is (2·0.5 + 3·0.25 + 2·0.75 + 2·0.75 + 1·0.25 + 2·0.25 + 1·1)/17 = 6.5/17 ≈ 0.38.

---

#### 6. AlignmentMap (schema v0)

The schema has no slot for substitution results or for candidate integrations. Substitution results are therefore recorded in `basis`, and each integration's operator and price sit on the link it is built on (I1 on L6, I2 on L2). See Decision 6.

```json
{
  "@id": "align:tce-rd-run07",
  "@type": "AlignmentMap",
  "theories": ["tce:reading-1", "rd:reading1"],
  "links": [
    {
      "kind": "bridge",
      "constructs": ["tce:C2", "rd:C1", "rd:C2", "rd:C3"],
      "sharedLicenses": [
        "If X(A,B) rises, B's ex post leverage over A rises (tce:C2.com2, tce:C6.lic1; rd:C1.l1 with rd:C4.c1)",
        "If X(A,B) rises, P(A and B under common ownership) rises (tce:C2.lic1, tce:P5; rd:C5.l1, rd:P4)",
        "If the A-B asset or resource is as good elsewhere, X is absent (tce:C2.pre1; rd:C1.p1)"
      ],
      "basis": "Scope-restricted, one-directional bridge over dyads whose dependence arises from A's sunk relationship-specific investment (tce:S1 intersect rd:S2). tce:C2 entitles rd:C1 via rd:C1.e1 (inferred); the converse fails (generic input from a monopolist: high rd:C1, zero tce:C2, tce:C8.pre1). Substitution test: T1 tce:P5 -> PASS conditional on rd:A10 and common-ownership coding; T2 tce:P2 -> PASS conditional on rd:C4.c1 (Explicator inference). Reverse robustness: T3 rd:P1 -> FAIL; T4 rd:P5 -> weak PASS."
    },
    {
      "kind": "rivalry",
      "constructs": ["tce:C15", "rd:C8", "rd:C18"],
      "conflictingEntitlements": [
        "tce:C15.com1 with core tce:A4: the lowest-governance-cost structure is the one adopted",
        "rd:C18.p1 with core rd:A4: boundaries are not set by cost minimization",
        "tce:C12.pre1 excludes hierarchy at low specificity; rd:P5 / rd:C6.l1 license absorption under high mutual dependence with no specificity condition"
      ],
      "basis": "Hard-core versus hard-core conflict over the boundary criterion. Divergent observable: incidence of common ownership in dyads with high mutual dependence and low asset specificity (critical generic input, few suppliers, no specific investment). TCE: market governance; any integration is misaligned and bears a cost/survival penalty (tce:P3, tce:P4). RD: elevated merger incidence with no penalty predicted (rd:P5, rd:P7). Requires a dependence indicator independent of specificity.",
      "operator": "Integrate",
      "inferentialPrice": "I2 (two-criterion dyadic boundary choice). TCE: tce:A4 ceases to be the sole positive heuristic; the transaction (tce:A3) ceases to be the sole unit. RD: rd:A4 must move from hard core to belt (RD reading 3); must accept that absorption is costly (tce:A7). Both: a weighting parameter and a specificity-independent dependence indicator. PrisM: the effect of non-specificity dependence on integration rises as competitive selection weakens."
    },
    {
      "kind": "complementarity",
      "constructs": ["tce:C6", "tce:C7", "rd:C4"],
      "discharges": "RD leaves open what power does and when it is exercised (rd:C4.c1 is an inference; reading 3: power need not be exercised). TCE's tce:A2 with tce:C7 discharges it: leverage is exercised where contracts are incomplete and the advantaged party is opportunistic.",
      "basis": "Not a bridge: substituting power for opportunism in tce:A2 ('because some parties have power, gaps will be exploited') is not licensed by RD reading 1, and under high mutual dependence RD licenses cooperative absorption (rd:A6), not exploitation. Disposition (TCE) and structural capacity (RD) compose rather than substitute."
    },
    {
      "kind": "equivocation",
      "constructs": ["tce:C3", "rd:C9"],
      "basis": "Same word, different roles. tce:C3: exogenous transaction attribute, acts through incompleteness (tce:A11), precludes an integration effect at near-zero specificity (tce:C3.pre1, tce:P7). rd:C9: endogenous to dependence (rd:R5), organization-level, licenses a direct motive for tactics (rd:C9.l1). Substituting rd:C9 into tce:P7 yields a claim RD contradicts."
    },
    {
      "kind": "equivocation",
      "constructs": ["tce:C12", "tce:C19", "rd:C12"],
      "basis": "Same observable (a common-ownership event), different roles. tce:C12 requires authority and administrative control (pre2), carries bureaucratic cost and weaker incentives (com2), is precluded at low specificity (pre1). rd:C12 is a cost-free event licensed by mutual dependence and includes horizontal mergers. Substitution: tce:C12.com1 partial pass (rd:C12.l1; 'fiat' unmatched); tce:C12.com2 FAIL (RD silent); tce:C12.pre1 FAIL (rd:P5 contrary). Do not count one M&A event as evidence for both theories."
    },
    {
      "kind": "complementarity",
      "constructs": ["rd:C7", "rd:C17", "tce:C9"],
      "discharges": "TCE's surfaced scope condition tce:S3 (all governance structures feasible for every transaction) is discharged by rd:R13 / rd:C17.l1 (the weaker side is less able to absorb; infeasible absorption is unlikely whatever the motive) and rd:C16.p1 (no motive to absorb without dependence).",
      "basis": "TCE assumes what RD models; feasibility becomes a variable instead of a scope condition.",
      "operator": "Augment",
      "inferentialPrice": "I1 (feasibility-constrained alignment), TCE host. TCE: drops tce:S3 and must accept persistent non-integration of high-specificity dyads as predicted rather than anomalous; needs an imbalance measure independent of specificity. RD: its constructs enter as auxiliaries of a cost-minimizing core, incompatible with rd:A4 as core in reading 1. PrisM: the slope of P(integration) on the investor's asset specificity is flatter when the investor is the weaker side of a power imbalance."
    },
    {
      "kind": "complementarity",
      "constructs": ["tce:C11", "rd:C13", "rd:C14"],
      "discharges": "RD leaves open when co-optation or negotiated long-term arrangements are chosen over absorption (Run 02 openQuestion 5). TCE's tce:C11.lic1 (hybrids at intermediate specificity), read through the L1 bridge, discharges it for dependence that arises from specific investment.",
      "basis": "Conditional on the L1 bridge and on surfaced auxiliary tce:A8. Leaves diversification (rd:C15) without a counterpart, and does not cover dependence outside L1's scope."
    }
  ]
}
```

Validation: the JSON block above was extracted and validated against `$defs/AlignmentMap` in `schema/theory-object.v0.schema.json` with `python3 -I` and jsonschema 4.26.0 (Draft 2020-12). Result: the JSON parses, has 7 links, and returns **0 validation errors**.

---

#### 7. Notes for the Provenance Ledger

- **Id mismatch.** rd:P5 and rd:P9 cite their rival as `tce:reading1`, but Run 01's id is `tce:reading-1`. The links cannot resolve until one of the two is corrected.
- **rd:P5's rivalDivergence** says that for TCE, "mutual dependence without specific investment gives no prediction." The more accurate statement is that TCE predicts market governance there (tce:C12.pre1, tce:C10.lic1). That is a contrary prediction, not silence, and it is the L2 observable.
- **Reading dependence.**
  - L1's T1 pass depends on rd:A10, which exists only in RD reading 1. Under RD reading 2 ("constraint" as imbalance), a unilateral rise in A's specific investment raises merger probability only where mutual dependence is high. T1 would then fail and a second rivalry would open, over asymmetric specificity.
  - L2 is a rivalry only under RD readings 1 and 2. Under RD reading 3 it becomes a complementarity: incremental variance explained (Run 02, D-3).

---

#### Decisions for the theorist

1. **Accept, narrow or reject L1 as a bridge.** It passes only conditionally (on rd:A10 and rd:C4.c1) and in one direction. You could instead record it as "tce:C2 is a special case of rd:C1," which the schema cannot currently express.
2. **Decide whether the L2 rivalry is real or an artefact of reading 1.** It hinges on RD D-3 (whether rd:A4 is core). Under RD reading 3 it becomes a complementarity, and I2 would then cost RD nothing in its hard core.
3. **Choose at most one integration to pursue, or neither.** I1 (Augment) is cheap for TCE but subordinates RD. I2 (Integrate) changes both hard cores. I have not chosen.
4. **Approve the equivocation flags L4 and L5** before any test design. In particular, decide whether "vertical integration" (tce:C19) and "merger/absorption" (rd:C12) may be coded from the same events.
5. **Name an indicator of dependence that does not depend on specificity.** L2's test and both integrations need one; without it they cannot be tested.
6. **Schema changes.** Should AlignmentMap gain slots for substitution tests, one-directional (special-case) bridges, reading conditions on a link, and candidate integrations as first-class nodes? At present these are written into free-text fields.
7. **Inferential-distance metric.** Accept the draft's binary weighting (0.76 here) or adopt graded weights by link kind (about 0.38 with the illustrative weights). Also fix how a pair is weighted (here: count of `licenses` entries) and supply the operator definitions from Table 2, so the Augment/Integrate labels can be checked.
8. **Verify citations** marked "(to verify)": Grossman & Hart 1986 as the property-rights reference for I1's adjacent-discipline implication, and the input-output indicator of dependence attributed to the RD literature.

---

### B.8 Run 08: Empirical Validation Designer on the transaction-cost theory object
*Instruction set: Foundry v0.1, Role 6. Inputs: Run 01 reading 1; rivals from Runs 02, 03, 04. Single run, unedited.*

---

#### 0. Target, rivals and conventions

**Theory under test.** `tce:reading-1` ("economizing choice", Run 01). Parties choose the structure that governs a transaction most cheaply (tce:A4 core, via tce:A13). Asset specificity is decisive (tce:A5 core). Uncertainty only moderates (tce:P6, tce:P7). Selection is a backstop (tce:A12 auxiliary).

**Rivals.**
- **INST**: the field-template account (Run 03, §2, rows X1 to X5).
- **BEH**: problemistic search and routine replication (Run 04, §2, the rows in bold).
- **RD**: resource-dependence theory, `rd:reading1` (Run 02). Its core includes rd:A2 (power = dependence) and rd:A4 (boundaries are set by political management of dependence, not by cost minimization). Its predictions are rd:P4 to rd:P9.

**Conventions.** "(R0n: id)" cites a node or row of Run 0n. "(assumption)" marks an effect-size or base-rate prior that I chose and nobody has measured. "(to verify)" marks a citation or magnitude I am not sure of. All power calculations use two-sided α = 0.05 and power 0.80, so (z₀.₉₇₅ + z₀.₈₀)² = (1.960 + 0.842)² = 7.849. Equivalence tests (TOST) use one-sided α = 0.05 each way and power 0.80 when the true effect is zero, so (z₀.₉₅ + z₀.₉₀)² = (1.645 + 1.282)² = 8.565. I mark no derivation closed.

**Severity (Mayo 2018).** A design is severe for reading 1 if a result that agrees with reading 1 would be *improbable* were reading 1 false and the rival true. For each design I give an indicative figure, P(agreeing result | rival true). It is roughly the rival-side miss rate (1 − power, or the equivalence analogue) plus the probability that the main threat alone produces the agreeing result. These figures are judgments, not estimates.

---

#### 1. Risky-prediction table (step 1)

A prediction counts as risky only if reading 1 forbids an observable outcome that at least one rival expects. Rows N1 to N3 are included for contrast because they are **not** risky.

| # | Observable | Reading 1 (basis) | Rival prediction (basis) | Rival(s) |
|---|---|---|---|---|
| RP1 | Effect of uncertainty on integration when asset specificity is near zero | **Zero** (tce:P7, tce:C3.pre1, tce:A5) | **Positive** through uncertainty avoidance and loss aversion (R04: beh:O4) | BEH; also reading 3 (tce:P7.r3) |
| RP2 | Insourcing of a *generic* input after an exogenous supplier shortfall, and whether it persists once supply is restored | **No persistent insourcing.** Governance tracks attributes (tce:A3, tce:A4, tce:A13) and attributes are unchanged | **Insourcing that persists**: local search reaches "make", and routines then keep it in-house (R04: §2 timing and stickiness rows) | BEH. RD predicts multi-sourcing, not absorption, because dependence is low (rd:P3, rd:C3). INST predicts following peers |
| RP3 | Effect of prior in-house production of *related* items on make, given specificity | **None** except through measured specificity (tce:R13, tce:A10) | **Positive**: routine replication (R04: beh:O5, §2) | BEH |
| RP4 | Vertical integration after an exogenous rise in alternative sources for an input, with specificity unchanged | **No change** (tce:A5 decisive; hazard comes from ex post lock-in, tce:A9, not from ex ante numbers) | **Fall**: dependence falls (rd:C3.l1, rd:P4, rd:P8) | RD |
| RP5 | Asset-specificity slope on *non-market* governance (hybrid or hierarchy vs market) in a field whose template is the hybrid | **Positive** in every field (tce:P3 ordering, tce:A8) | **About zero**: governance follows the template (R03: X1, X2) | INST |
| RP6 | Attribute effect across the diffusion curve; effect of peer prevalence given attributes | Attribute effect **does not decline** with adoption order; prevalence has **no** effect (tce:A4, tce:A13) | Attribute effect **declines**; prevalence effect is **positive** (R03: X3, X4; Tolbert & Zucker 1983) | INST |
| RP7 | Exit hazard of firms whose main transactions are misaligned | **Higher** (tce:P4, tce:A12; reading 2: tce:P9) | **Not higher** while the form is legitimate (R03: X5) or slack buffers it (R04: beh:O8) | INST, BEH |
| N1 | Sign of the specificity effect on integration in the cross-section | Positive (tce:P5) | Positive, through salience (BEH, R04: beh:O3), the template (INST, R03: §2), and specific assets reducing alternatives, which raises dependence (RD, rd:P1, inferred) | None diverge |
| N2 | Sign of specificity × uncertainty | Positive (tce:P6) | Positive under BEH (R04: §2). Positive under INST where the template is integration (R03: O5) | Diverges only in hybrid-template fields; folded into RP5 |
| N3 | Which party acquires under power imbalance (rd:P6) | **No prediction**: the object has no construct for acquirer identity | Weaker side less able to absorb (rd:P6) | Not risky *for TCE*: reading 1 cannot fail on it |

**Count: 7 risky predictions (RP1 to RP7); 3 non-risky contrasts (N1 to N3).**

---

#### 2. Measurement (step 2): indicators both sides could accept

| Construct | Indicator | Source | Unit | Who might object, and why |
|---|---|---|---|---|
| tce:C2 asset specificity | (a) Ratings by engineers of how much a component's value depends on this buyer, taken **before** the governance decision; (b) the share of an industry's inputs not traded on exchanges or reference-priced (Nunn 2007, to verify) | Procurement and engineering records; I-O tables | Component (a); industry pair (b) | BEH: (a) must predate in-house routines (beh:O5). INST: categories are field-constructed (R03: O7). Mitigation: fix the coding rubric ex ante and blind coders to governance |
| tce:C3 uncertainty | Coefficient of variation of monthly demand for the downstream product, and the count of engineering change orders | Firm records | Component | None expected. This measures volume and technological uncertainty, not behavioural uncertainty |
| tce:C9 / tce:C19 governance | Three-way code: spot or short contract (market); contract of three years or more, or equity alliance (hybrid); common ownership (hierarchy). Binary "non-market" = hybrid or hierarchy | Contracts, ownership records | Transaction | Settles Run 01 Q7 for these tests only. Needs the theorist's approval |
| Supplier shortfall (BEH) | An exogenous disruption of the supplier's plant (earthquake, flood), with no fault on either side | Disaster maps linked to supplier sites | Firm × input | TCE might call a shortfall evidence of opportunism. A natural disaster rules that out by construction |
| rd:C1 dependence; rd:C3 alternatives | Purchase share from the I-O tables × concentration of the supplier industry; the count of import sources | BEA I-O tables; trade data | Directed industry pair | RD accepts this; it is close to Casciaro & Piskorski 2005 (to verify) |
| Template / prevalence (INST) | The modal governance of the same component class among the focal firm's field peers in the prior year; the cumulative adoption share | Industry surveys; firm disclosures | Field-year | TCE: prevalence may lower governance cost (thicker supplier markets). Addressed in D5 |
| tce:C16 misalignment | Observed structure ≠ the structure tce:P3 assigns to the band of indicator (a) | As above | Firm (share of its spend that is misaligned) | Inherits R03: O3 and R04: beh:O2. Bands must be fixed ex ante |

---

#### 3. Designs (steps 3 and 4)

##### D1. Persistence of insourcing after a disaster disrupts a generic input (RP2; also bears on RP1)

- **Design.** A staggered event study (difference-in-differences). Treated: firm × input pairs whose incumbent supplier plant was hit by an exogenous disaster, for example the 2011 Tōhoku earthquake or the 2011 Thai floods. Controls: the same inputs at firms whose suppliers were not hit, matched on input class and firm size. Restrict to **low-specificity inputs** (band fixed ex ante on indicator (a)) that had **at least three alternative qualified suppliers after the shock**.
- **Primary outcome.** The input is in-house at t + 36 months, after supplier capacity and prices have returned to pre-shock levels. Secondary outcome: multi-sourcing (the RD prediction).
- **Identification.** The disaster hits supplier performance but leaves the transaction's attributes unchanged (tce:C2 and tce:C3 are measured before the shock). Under reading 1, governance of a generic input stays with the market, so short-run insourcing should revert. BEH predicts lasting insourcing. Measuring at t + 36 separates a production-cost response to a temporary capacity loss, which reading 1 can accommodate, from a governance change. Reading 1 cannot accommodate a persistent change, because nothing in tce:C15 has changed.
- **Main threat.** The disruption may raise the input's *perceived* specificity or uncertainty, so reading 1 could redescribe the persistence as rational updating on tce:C3. Under reading 1, uncertainty matters only through specificity (tce:P7), so that redescription is itself a move to reading 3. Pre-register that a reading-1 defence through uncertainty counts as a reading change. Secondary threats: survivorship of firms, and insourcing for inventory or strategic-control reasons. Code the reasons from procurement minutes.
- **Data.** Procurement records from cooperating manufacturers is the only source with input-level make-or-buy. A coarse fallback is firm-level outsourcing ratios from Japanese official enterprise surveys (to verify availability). Supplier-link data used in disruption studies (e.g. Carvalho et al. 2021; Boehm, Flaaen & Pandalai-Nayar 2019, both to verify) can identify treated links.
- **Power (superiority, to detect BEH).** Base rate of persistent insourcing of a generic input over 36 months: p₁ = 0.02 (assumption). BEH smallest effect of interest: p₂ = 0.05 (assumption, to verify; no published magnitude known to me).
  - p̄ = 0.035, so 2p̄q̄ = 0.06755, √ = 0.2599, and × 1.960 = 0.5094.
  - p₁q₁ + p₂q₂ = 0.0196 + 0.0475 = 0.0671, √ = 0.2590, and × 0.842 = 0.2180.
  - n per arm = (0.5094 + 0.2180)² / (0.03)² = 0.5291 / 0.0009 = **588**.
  - Clustering of inputs within firms: m = 5 inputs per firm and ICC = 0.10 (assumptions) give a design effect of 1 + 4 × 0.10 = 1.4, so **823 per arm, about 1,650 firm × input pairs.**
- **Power (equivalence, the reading-1 side).** Margin Δ = 0.03 and true difference 0. n per arm = 8.565 × (2 × 0.0196) / 0.0009 = 8.565 × 0.0392 / 0.0009 = **373**, × 1.4 = **522**.
- **Severity.** P(agreeing result | BEH true) ≈ 0.20 (miss rate) + ≈ 0.05 (the uncertainty redescription succeeds although pre-registered), so about **0.25**. **Discriminates TCE from BEH.** It does **not** discriminate TCE from RD: both predict no persistent insourcing of low-dependence generic inputs (RD predicts multi-sourcing). It discriminates TCE from INST only if peer responses are recorded.

##### D2. Uncertainty effect within the low-specificity stratum, with prior routines (RP1, RP3)

- **Design.** A cross-section of components within firms, restricted to the lowest band of specificity indicator (a). Logit of make on standardized demand volatility, with firm fixed effects. A second regressor is an indicator for prior in-house production of a related item (RP3).
- **Identification.** Within-firm variation across components holds the firm's governance competence and template constant. The test of RP1 is an **equivalence test**, because reading 1 predicts a point null.
- **Main threat.** Measurement error in specificity. If volatile components are also somewhat more specific than indicator (a) records, a spurious uncertainty effect appears, and it biases the test *against* reading 1. A second threat is that reading 1 can retreat to reading 3 (tce:A5.r3), which is a belt move. The test therefore bears on tce:A5 *as core*, not on the programme.
- **Power.** Base rate of make in the low-specificity stratum: p = 0.20, so p(1 − p) = 0.16 (assumption). BEH smallest effect of interest: OR = 1.3 per SD of volatility, so β* = ln 1.3 = 0.2624 and β*² = 0.06883 (assumption; Walker & Weber 1984 report a volume-uncertainty effect, magnitude to verify). Using Hsieh, Bloch & Larsen (1998, to verify), n = 7.849 / (0.16 × 0.06883) = 7.849 / 0.011013 = 713. The variance inflation for correlated covariates, 1/(1 − 0.30) = 1.43, gives **1,018 components**. Equivalence with margin |ln OR| < 0.262: n = 8.565 / 0.011013 = 778, × 1.43 = **1,111 components**.
- **Severity.** P(agreeing result | BEH true) ≈ 0.20 + measurement-error risk. That risk biases toward rejecting reading 1, not toward agreeing with it, so it does not raise the figure. About **0.20 for tce:P7**. The test discriminates TCE from BEH on tce:A5's core status, but a reading-1 loss can be absorbed by a change of reading, so the severity is lower for the *programme*.

##### D3. A trade shock that adds alternative sources, with specificity fixed (RP4)

- **Design.** A continuous-treatment difference-in-differences on directed upstream → downstream industry pairs. Treatment: the exposure of the upstream industry to a fall in US tariff uncertainty on Chinese imports. Pierce & Schott (2016, to verify) use the normal-trade-relations gap at the 2001 grant of permanent normal trade relations. The treatment raises the number of alternative sources for downstream buyers (rd:C3) without changing relationship specificity (Nunn 2007 index, to verify; held fixed at its pre-period value).
- **Outcome.** Vertical M&A between domestic firms in the pair, per pair-year.
- **Predictions.** RD: integration falls in high-gap pairs (rd:P4, rd:P8). Reading 1: no change at any level of specificity (tce:A5, tce:A9). Run separately within low-specificity and high-specificity pairs. Reading 1 predicts null in both. RD predicts a fall that is larger where the domestic supplier was concentrated.
- **Main threat.** Price channels. A tariff change shifts input prices, and prices affect the value of integration (Alfaro et al. 2016, to verify). That is a fourth explanation, which neither side owns. Mitigation: control for the change in input prices, and pre-specify the sign the price channel implies.
- **Power.** Base rate: 0.005 vertical deals per pair-year (assumption, to verify). RD smallest effect of interest: rate ratio 0.80 for the top vs bottom tercile of exposure (assumption, scaled from Casciaro & Piskorski 2005, to verify).
  - Var(ln RR) ≈ 1/E₁ + 1/E₂ with E₁ = 0.8 E₂, so 2.25 / E₂ ≤ (ln 0.8)² / 7.849 = 0.04979 / 7.849 = 0.006344.
  - That requires E₂ ≥ 355 control events and E₁ ≥ 284 treated events, which is 355 / 0.005 = **71,000 pair-years per tercile**.
  - Overdispersion φ = 1.5 (assumption) raises this to 106,500 per tercile.
  - **Available** (assumption): 20,000 pairs × 8 post-years × 1/3 = 53,300 per tercile. **Underpowered for RR 0.80.** The minimum detectable effect is near RR 0.72: at RR 0.72, (ln 0.72)² = 0.1079 and 7.849 × (1/(0.72 × 177.7) + 1/177.7) = 7.849 × 0.01344 = 0.1055 ≤ 0.1079.
  - Remedy: widen the outcome to all boundary-spanning ties in rd:P7 (joint ventures, long-term contracts). That raises the base rate and is equally binding on RD.
- **Severity.** Under the remedy, P(agreeing result | RD true) ≈ 0.20 + ≈ 0.10 (a price channel masks a dependence effect), so about **0.30**. **Discriminates TCE from RD**, and is severe for rd:A4 as well as for tce:A5. Reading 1 can absorb a positive result only by adding ex ante small-numbers bargaining to the belt, which tce:A5 "decisive" does not currently allow.

##### D4. Japanese transplants vs domestic manufacturers in one host country (RP5)

- **Design.** Component-level governance (coded in three categories, then collapsed to binary non-market) for Japanese-owned and US-owned car assemblers in the US. They share one legal regime and one supplier base but have different home templates (the keiretsu-type hybrid; R03: O5; Dyer 1996, to verify).
- **Test.** The specificity slope on P(non-market) *within* the Japanese group.
- **Predictions.** Reading 1: positive, with a level difference permitted (the cost curves may differ). INST: about zero, because the hybrid template is applied whatever the attributes (R03: X1, X2).
- **Main threat.** Reading 1 can absorb a zero slope by positing that the Japanese hybrid is cheaper than the market at *every* level of specificity, which revises tce:A8 in the belt. Without an independent measure of tce:C15 (Run 01 Q8; R03: O3), that move cannot be blocked. The severity of D4 therefore depends on the theorist answering Q8.
- **Power.** Same priors as D6. OR = 1.8 per SD (assumption, to verify) and p = 0.6, so p(1 − p) = 0.24. n = 7.849 / (0.24 × 0.3455) = **95**, × 1.43 = **136 components** in the Japanese group.
- **Severity.** P(agreeing result | INST true) ≈ 0.05 (false positive) in sampling terms. But a *disagreeing* result can be absorbed in the belt with probability I put at ≈ 0.5 (judgment), so the design tests tce:A8 more than tce:A4. **Discriminates on its face; only moderately severe for the core.**

##### D5. Attribute effects by adoption order in a boundary-change diffusion (RP6)

- **Design.** An event history of a boundary change, for example outsourcing of a function. Interact specificity with the adopter's position on the diffusion curve (early half vs late half). Add lagged peer prevalence, instrumented by shocks to peers' peers (to address reflection; Manski 1993).
- **Predictions.** Reading 1: the specificity effect is constant or rising (learning). INST: the specificity effect declines and prevalence has a positive effect.
- **Main threat.** Reading 1 can treat prevalence as lowering governance cost (thicker markets for the new structure), so the prevalence coefficient does not discriminate. Only the decline in the attribute effect does.
- **Power.** Detect a fall from OR 1.8 (early) to 1.0 (late), a difference in log OR of 0.588, with p(1 − p) = 0.24 (assumptions). The difference has variance 2 / (n_h × 0.24). n_h = 2 × 7.849 / (0.24 × 0.3455) = 15.698 / 0.08292 = **190 adopters per half**, × 1.43 ≈ **543 adopters**.
- **Severity.** P(agreeing result | INST true) ≈ 0.20 + ≈ 0.20 (instrument weakness or reflection) ≈ **0.40**. **Discriminates weakly.**

##### D6. Cross-sectional replication of tce:P5 (N1): low-severity contrast

- **Design.** A logit of make on an engineering-effort specificity proxy, after Monteverde & Teece (1982), with uncertainty and the interaction term (tce:P5, tce:P6).
- **Power.** OR = 1.8 per SD (assumption; Monteverde & Teece 1982 and the reviews of Lafontaine & Slade 2007 and Macher & Richman 2008 report consistent positive effects, magnitudes to verify) and p = 0.4, so p(1 − p) = 0.24. n = 7.849 / (0.24 × 0.3455) = **95**, × 1.43 = **136 components**. The design is cheap and well powered.
- **Severity.** All three rivals predict the same sign: BEH through salience (R04: beh:O3), INST through the US template (R03: §2), and RD because specific assets reduce alternatives (inferred). P(agreeing result | any rival true) ≈ **0.8 to 0.9** (judgment). **Merely consistent.** A positive estimate adds almost nothing to the case for tce:A4 over its rivals. This bears out the Interlocutors' downgrade of the provisional "novel" status of tce:P5 (Run 01 Q10; R04: beh:O3).

##### D7. Exit hazard by alignment status (RP7): low severity for reading 1's core

- **Design.** A Cox model of firm exit on the share of spend that is misaligned, with controls for slack, size, and the legitimacy of the form (its prevalence in the field) (R03: O8; R04: beh:O8).
- **Power.** Hazard ratio 1.3 (assumption) and 30% of firms misaligned. Using Schoenfeld's formula, d = 7.849 / (0.21 × 0.06883) = 7.849 / 0.01445 = **543 exits**.
- **Severity.** It discriminates the rivals on tce:A12. But tce:A12 is **auxiliary** in reading 1, so a null leaves tce:A4 untouched. **Consistent-only for reading 1's core.** It would be the top-severity design under reading 2 (tce:A12.r2 core; tce:P9).

---

#### 4. Severity ranking (step 5)

| Rank | Design | Rival(s) discriminated | P(agreeing result \| rival true), indicative | What a reading-1 failure would hit | Verdict |
|---|---|---|---|---|---|
| 1 | D1 disaster → persistent insourcing | BEH | ≈ 0.25 | tce:A4 + tce:A13 as a process claim (tce:R9 teleological); retreat = reading 2 or "as-if" | **Discriminates** |
| 2 | D3 trade shock → alternatives | RD | ≈ 0.30 (with the widened outcome) | tce:A5 core; also severe for rd:A4 | **Discriminates** (underpowered as first specified) |
| 3 | D2 uncertainty at low specificity, plus routines | BEH, reading 3 | ≈ 0.20 for tce:P7, but absorbable by a change of reading | tce:A5 status (D3 in Run 01) | **Discriminates** a proposition; weaker for the programme |
| 4 | D4 transplants | INST | low in sampling terms; ≈ 0.5 absorbable through tce:A8 | tce:A8 (belt) unless tce:C15 is measured | **Moderately discriminating** |
| 5 | D5 diffusion order | INST | ≈ 0.40 | tce:A13 | **Weakly discriminating** |
| 6 | D7 exit hazard | INST, BEH | ≈ 0.20 on tce:A12, but A12 is auxiliary | belt only | **Consistent** (for the core) |
| 7 | D6 replication of tce:P5 | none | ≈ 0.8 to 0.9 | nothing a rival denies | **Merely consistent** |

D1 ranks first because three conditions hold together:
1. Reading 1 forbids a definite outcome: persistent insourcing of a generic input with unchanged attributes.
2. The cause is exogenous by construction, and the specificity measure predates the shock, which answers beh:O5 about tce:A10.
3. The obvious accommodation, rational updating on uncertainty, is itself classified in Run 01 as a change of reading (tce:P7 vs tce:P7.r3). It can therefore be pre-registered as a loss, not hidden in the belt.

---

#### 5. Crucial-experiment check (step 6)

**Verdict: no design is binding on all three rival traditions. D1 is a candidate crucial experiment for reading 1 vs BEH only, and only if four terms are agreed in advance.**

- **D1, TCE vs BEH.** Both sides already accept the observable: BEH forwarded the timing and stickiness rows to this role (R04: §2), and reading 1's per-transaction economizing (tce:A3, tce:A4) speaks directly to it. Binding requires agreeing ex ante on:
  1. the low-specificity band and its coding rubric;
  2. the 36-month horizon;
  3. the equivalence margin of 3 percentage points;
  4. that a defence through updated uncertainty counts as a move to reading 3.
- **What each side concedes.** If persistent insourcing exceeds the margin, the reading-1 theorist concedes that tce:A13 fails for governance choice. That forces Decision 1 in R04: move to reading 2, or declare reading 1 "as-if" and give up tce:R9's teleological form. If the TOST establishes equivalence, the BEH theorist concedes that problemistic search does not reach "make" for generic inputs. That undercuts BEH's own route to tce:P5 (R04: beh:O3), so the cross-sectional evidence of D6 counts for reading 1 again.
- **INST would not treat any design here as binding.** Its corroboration logic is comparative-historical (R03: §0), and it disputes that the specificity indicator is pre-institutional (R03: O7). D4 and D5 would shift the balance; they would not settle it.
- **RD might accept D3** if the price channel is controlled. But a null result would let RD move rd:A4 to the belt (Run 02 reading 3, pivot D-3) rather than concede. D3 is therefore binding only if the RD theorist holds rd:A4 as core.
- Following Lakatos (1970), even an agreed D1 result would be recognised as crucial only in retrospect, once one programme had stopped making progress.

---

#### 6. Additions to `openQuestions`

- **V1.** The equivalence margins (3 pp in D1; OR 1.3 in D2; RR 0.8 in D3) are what make reading 1's null predictions refutable. Who sets them, and from what? No published magnitudes are known to me (assumption).
- **V2.** D4 and D7 lose most of their severity unless tce:C15 has an independent measure (Run 01 Q8). Is a measure such as renegotiation frequency or dispute cost (R04: beh:O2) acceptable as that measure?
- **V3.** Does input-level make-or-buy data across disaster-hit suppliers exist outside cooperating firms? (To verify.)

---

#### 7. Decisions for the theorist

1. **Adopt, amend or reject the risky-prediction table** (RP1 to RP7). In particular, confirm that N3 (acquirer identity) is outside reading 1, so that it cannot count against it.
2. **Approve the measurement rules in §2**, especially the three-way governance coding (which answers Run 01 Q7 for these tests) and the ex ante specificity bands.
3. **Decide whether to pre-register that a defence of D1 through uncertainty counts as a move to reading 3.** Without that rule D1 loses most of its severity.
4. **Set or delegate the equivalence margins** (V1). They are effect-size priors, not findings.
5. **Choose which designs to commission.** D1 is the most severe but needs firm-level partners. D3 needs its outcome widened to reach adequate power. D6 is cheap but merely consistent; commission it only as a calibration check.
6. **Decide whether to answer Run 01 Q8** (an independent measure of governance cost) before running D4. The answer determines whether D4 tests the core or only tce:A8.
7. **Have the "(to verify)" citations and magnitudes checked** before any prior is used in a pre-registration. These include Walker & Weber 1984; Nunn 2007; Pierce & Schott 2016; Alfaro et al. 2016; Dyer 1996; Carvalho et al. 2021; Boehm et al. 2019; Lafontaine & Slade 2007; Macher & Richman 2008; Hsieh et al. 1998; and Casciaro & Piskorski 2005 magnitudes.

---

### B.9 Provenance Ledger trace (`runs/09_ledger_trace.json`)

```json
[
 {
  "@id": "ev:1",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T18:46:00Z",
  "actor": {
   "kind": "human",
   "name": "case author (paraphrase of Williamson 1975, 1985, 1991)"
  },
  "action": "ingest",
  "inputs": [],
  "outputs": [
   "src:InputA"
  ],
  "rationale": "Prose input A registered.",
  "prevHash": "0000000000000000000000000000000000000000000000000000000000000000",
  "hash": "a30ebfb8bec9a0e797cf3de9a89fcac1d3088e825fe26db3e4b885d8bc8c1a2a"
 },
 {
  "@id": "ev:2",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T18:46:00Z",
  "actor": {
   "kind": "human",
   "name": "case author (paraphrase of Pfeffer & Salancik 1978)"
  },
  "action": "ingest",
  "inputs": [],
  "outputs": [
   "src:InputB"
  ],
  "rationale": "Prose input B registered.",
  "prevHash": "a30ebfb8bec9a0e797cf3de9a89fcac1d3088e825fe26db3e4b885d8bc8c1a2a",
  "hash": "bad8e4ed0d48d77126b1ca48abcae8bf9043a29a0b7e3345ab87e0de20558ae0"
 },
 {
  "@id": "ev:3",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T18:54:00Z",
  "actor": {
   "kind": "agent",
   "name": "Explicator",
   "modelVersion": "Claude (Anthropic)",
   "instructionSetVersion": "Foundry v0.1"
  },
  "action": "propose",
  "inputs": [
   "src:InputA"
  ],
  "outputs": [
   "tce:ensemble-1",
   "tce:reading-1",
   "tce:reading-2",
   "tce:reading-3"
  ],
  "respondsTo": "ev:1",
  "rationale": "Run 01. Three readings; pivotal differences D1-D4.",
  "prevHash": "bad8e4ed0d48d77126b1ca48abcae8bf9043a29a0b7e3345ab87e0de20558ae0",
  "hash": "038d51dff03fc709d258c6ee7c5fd64b8208276c5e691b5ea6e7b5b17ac5aef2"
 },
 {
  "@id": "ev:4",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T18:55:00Z",
  "actor": {
   "kind": "agent",
   "name": "Explicator",
   "modelVersion": "Claude (Anthropic)",
   "instructionSetVersion": "Foundry v0.1"
  },
  "action": "propose",
  "inputs": [
   "src:InputB"
  ],
  "outputs": [
   "rd:ensemble",
   "rd:reading1",
   "rd:reading2",
   "rd:reading3"
  ],
  "respondsTo": "ev:2",
  "rationale": "Run 02. Three readings; pivot on the meaning of 'constraint'.",
  "prevHash": "038d51dff03fc709d258c6ee7c5fd64b8208276c5e691b5ea6e7b5b17ac5aef2",
  "hash": "480ab893631f820a779cb4497fe17fe40933d0f8de39b6b43307410698027c37"
 },
 {
  "@id": "ev:5",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T18:56:00Z",
  "actor": {
   "kind": "agent",
   "name": "demonstration operator (Claude), standing in for the human theorist",
   "modelVersion": "Claude (Anthropic)"
  },
  "action": "accept",
  "inputs": [
   "tce:ensemble-1",
   "rd:ensemble"
  ],
  "outputs": [
   "tce:reading-1",
   "rd:reading1"
  ],
  "respondsTo": "ev:4",
  "rationale": "Reading 1 of each adopted for demonstration only; in real use a human decision. adoptedReading left unset in the ensembles.",
  "prevHash": "480ab893631f820a779cb4497fe17fe40933d0f8de39b6b43307410698027c37",
  "hash": "b7322dacde6e1c9fb7b079c81a3801c14f86d33cefbae5a789496c5f5c001aca"
 },
 {
  "@id": "ev:6",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T18:57:00Z",
  "actor": {
   "kind": "agent",
   "name": "Interlocutor (institutional lens)",
   "modelVersion": "Claude (Anthropic)",
   "instructionSetVersion": "Foundry v0.1"
  },
  "action": "challenge",
  "inputs": [
   "tce:reading-1"
  ],
  "outputs": [
   "inst:O1..O10"
  ],
  "respondsTo": "ev:5",
  "rationale": "Run 03. 10 objections (1 fatal to tce:A4); field-template rival.",
  "prevHash": "b7322dacde6e1c9fb7b079c81a3801c14f86d33cefbae5a789496c5f5c001aca",
  "hash": "fc9c8df2c723c3b99883c6d2846ec93b7e23e124c70e22a2da5dbca3f20a8730"
 },
 {
  "@id": "ev:7",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T18:57:00Z",
  "actor": {
   "kind": "agent",
   "name": "Interlocutor (behavioral lens)",
   "modelVersion": "Claude (Anthropic)",
   "instructionSetVersion": "Foundry v0.1"
  },
  "action": "challenge",
  "inputs": [
   "tce:reading-1"
  ],
  "outputs": [
   "beh:O1..O9"
  ],
  "respondsTo": "ev:5",
  "rationale": "Run 04. 9 objections (1 fatal: tce:A13 vs tce:A1); problemistic-search rival.",
  "prevHash": "fc9c8df2c723c3b99883c6d2846ec93b7e23e124c70e22a2da5dbca3f20a8730",
  "hash": "89d8f8d7c0a85c96c2b60786557b3f8555aa33333b98bfe5cf5571da9b80147d"
 },
 {
  "@id": "ev:8",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T18:58:00Z",
  "actor": {
   "kind": "agent",
   "name": "Argument Auditor",
   "modelVersion": "Claude (Anthropic)",
   "instructionSetVersion": "Foundry v0.1"
  },
  "action": "annotate",
  "inputs": [
   "src:InputA",
   "tce:reading-1"
  ],
  "outputs": [
   "aud:W1..W11"
  ],
  "respondsTo": "ev:5",
  "rationale": "Run 06. 11 warrant gaps; 5 deductive-over-abductive mismatches.",
  "prevHash": "89d8f8d7c0a85c96c2b60786557b3f8555aa33333b98bfe5cf5571da9b80147d",
  "hash": "30777f223dbf2ba005cb0df0060b9e50a22161aaaeb1f347f98888de6acfe381"
 },
 {
  "@id": "ev:9",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T19:00:00Z",
  "actor": {
   "kind": "agent",
   "name": "Model Builder",
   "modelVersion": "Claude (Anthropic)",
   "instructionSetVersion": "Foundry v0.1"
  },
  "action": "derive",
  "inputs": [
   "tce:reading-1"
  ],
  "outputs": [
   "tce:D4..D13",
   "tce:A16..A21",
   "tce:P10"
  ],
  "respondsTo": "ev:5",
  "rationale": "Run 05. 5 asserted, 5 open, 1 refuted (P6 on probability scale); surfaced A16-A19. None closed: no checker.",
  "prevHash": "30777f223dbf2ba005cb0df0060b9e50a22161aaaeb1f347f98888de6acfe381",
  "hash": "ab53cdbd99eb3c927175f4e1bb0f90b5829697340e044b7eab122e93ab4bc29b"
 },
 {
  "@id": "ev:10",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T19:01:00Z",
  "actor": {
   "kind": "agent",
   "name": "Integrator",
   "modelVersion": "Claude (Anthropic)",
   "instructionSetVersion": "Foundry v0.1"
  },
  "action": "align",
  "inputs": [
   "tce:reading-1",
   "rd:reading1"
  ],
  "outputs": [
   "align:tce-rd"
  ],
  "respondsTo": "ev:5",
  "rationale": "Run 07. 1 bridge, 1 rivalry, 3 complementarities, 2 equivocations; integrations I1 (Augment), I2 (Integrate); distance 0.76.",
  "prevHash": "ab53cdbd99eb3c927175f4e1bb0f90b5829697340e044b7eab122e93ab4bc29b",
  "hash": "680804394283280904d4020e69387bf1adc9730e91016ff6e4694c1aedfb1932"
 },
 {
  "@id": "ev:11",
  "@type": "LedgerEvent",
  "timestamp": "2026-10-10T19:02:00Z",
  "actor": {
   "kind": "agent",
   "name": "Empirical Validation Designer",
   "modelVersion": "Claude (Anthropic)",
   "instructionSetVersion": "Foundry v0.1"
  },
  "action": "design",
  "inputs": [
   "tce:reading-1",
   "inst:O1..O10",
   "beh:O1..O9",
   "rd:reading1"
  ],
  "outputs": [
   "val:RP1..RP7",
   "val:D1..D7"
  ],
  "respondsTo": "ev:7",
  "rationale": "Run 08. 7 risky predictions; D1 ranked most severe; no design binds all three rivals.",
  "prevHash": "680804394283280904d4020e69387bf1adc9730e91016ff6e4694c1aedfb1932",
  "hash": "f78be2460d6357a9e3dce4b26ae112a0c3aee340a4e083bb075e0477740bda92"
 }
]
```

---

## Annex C. Project Lakatos component tables

*Reproduced from the Project Lakatos outline (Appendix A, Tables 1 to 4), which reviewers will not otherwise have, so that the composition in Section 2 can be checked against its sources. Text is as in the outline, with two typographical corrections; one Table 1 entry (Summarizer/Conclusion Builder), which breaks off in the source, has been completed. In Table 4, the Id column (L1 to L17) is added to match Section 2.1. The tables are also in the repository as `lakatos/LAKATOS_TABLES_1-4.md`.*

### C.1 Table 1. ‘Routine’ Agents for the Cocreation of Research Contributions

| Agent                           | Function / Description                                                                                                                                            |
|:--------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exploratory Literature Review   | Assists in the creation of an exploratory review in a specific domain or literature field.                                                                        |
| Targeted Literature Review      | Assists in the creation of a targeted literature review that aims to provide corroborating or refuting empirical arguments for a specific idea.                   |
| Synthetic Literature Review     | Assists in the creation of a synthetic synopsis of a field, based on targeted instructions.                                                                       |
| Data Interpreter: Descriptive   | Assists in the descriptive interpretation of a data set, based on specific instructions.                                                                          |
| Data Interpreter: Inferential   | Assists in performing inferential tests of one or more hypotheses based on a formatted data set.                                                                  |
| Data Interpreter: Causal        | Assists in performing tests of causal links and relationships in RCT or natural experiment data, based on a specification of one or more causal model topologies. |
| Data Specifier: Causal          | Assists in the formulation of causal models based on specific inputs that specify variable sets and available data sources.                                       |
| Modeling Assistant: Exploratory | Assists in the formulation of a model of a phenomenon or of a data set.                                                                                             |
| Modeling Assistant: Refiner     | Assists in the refinement of a model of a phenomenon or of a data set.                                                                                            |
| Proof Verifier                  | Assists in the verification of a formal proof.                                                                                                                    |
| Proof Synthesizer               | Assists in the construction of a proof or a counterexample.                                                                                                       |
| Summarizer/Conclusion Builder   | Assists in the summarization of main findings of a completed paper, or in the creation of its concluding section                                                                          |


### C.2 Table 2. Cognitive Operators for Advanced Research Assistant/Production Agents

| Operator            | Function / Description                                                                                                                                                                                                                                                                                                                                                                |
|:--------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Represent (X,Y)     | Represents natural language description X of a phenomenon in terms of a set of entities Y (concepts, variables—independent, dependent, control, moderators—and inferential links between them), where the representations (Y) include relational models (spatial, temporal, social), structural models, and dynamical models (including causal, teleological, and functional models). |
| Explain (X,Y; L)    | Constructs explanations of a natural language description X of a phenomenon in terms of a model (or representation) Y, using an inferential logic L (deductive, inductive, abductive; formal, informal).                                                                                                                                                                              |
| Justify (X,Y)       | Justifies a set of principles, injunctions, prescriptions or proscriptions (X) in terms of another set Y comprising normative and/or descriptive statements that are either general or particular, and may include empirical examples, counterexamples, competing theories, or alternative representations.                                                                           |
| Extend (X,Y)        | Extends the explanatory coverage of a set of concepts or models X into a domain of empirical support Y to which X had not previously been applied.                                                                                                                                                                                                                                    |
| Corroborate (X,Y)   | Provides corroborations for theory or model X from domain of applicability Y.                                                                                                                                                                                                                                                                                                         |
| Measure (X,Y; M)    | Derives a measure and associated measurement method M reflecting current technological capabilities for some quantity of interest X that renders it measurable via M within the variable space of some model or theory Y.                                                                                                                                                             |
| Integrate (X,Y)     | Produces an integration (logical, ontological, epistemological) of two representational entities (theories, models) X and Y.                                                                                                                                                                                                                                                          |
| Augment (X,Y)       | Augments a theory or model X by some or all of the base assumptions of another theory or model Y.                                                                                                                                                                                                                                                                                     |
| Challenge (X,Y)     | Produces a challenge to the empirical validity, coverage, coherence, or explanatory logic of theory/model X that is logically and semantically consistent with the substantive claims of theory/model Y.                                                                                                                                                                              |
| Refute (X,Y)        | Produces one or more refutations of the substantive, empirically testable claims of theory/model X from a relevant domain.                                                                                                                                                                                                                                                            |
| Reduce (X,Y; Φ)     | Produces a reduction of the explanatory apparatus of theory/model Y for phenomenon Φ to the terms (entities, variables, inferential links) of theory/model X.                                                                                                                                                                                                                         |
| Assimilate (X,Y; Φ) | Produces an assimilation (“unification”) of the empirical base associated with phenomena Φ of theory/model Y into the apparatus (entities, variables, inferential links) of theory/model X.                                                                                                                                                                                           |
| Eliminate (X,Y; Φ)  | Produces an elimination (as “epi-phenomenal”) of the theoretical apparatus of theory/model Y for the empirical base associated with phenomena Φ to the theoretical apparatus of theory/model X.                                                                                                                                                                                       |


### C.3 Table 3. Reconstructing Epistemological/Inferential Discourse: A Grammar for Patterning Agents

| Category                                    | Subcategory / Type           | Description                                                                                                                                                                                                                                                                                                                   |
|:--------------------------------------------|------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Epistemological Stances (Commitments)       | Positivism                   | In strict form, only statements referring to observable/sensible quantities “make sense” (Mach); propositions about electrons are nonsense. In “layman” form (common among social scientists), theories/models must be testable against empirical data.                                                                       |
|                                             | Realism                      | In metaphysical form: we can speak about events/objects as they are and independently of our minds because the terms of a theory correspond to the right states of affairs. In language-dependent form: multiple ways of describing the same state of affairs exist, and “truth” is always “truth-in-a-description-language.” |
|                                             | Instrumentalism              | Theories/models are instruments for making predictions; they need not be “true,” “valid,” or “representative.” Advanced by Friedman (1953) and others in quantum mechanics.                                                                                                                                                   |
|                                             | Constructivism               | Multiple forms: the “picture of reality” emerging from science results from interactions between minds/bodies and phenomena; contributions of agencies and essences are inseparable and relevant to how objects and events are constituted and labelled (cf. participatory realism in Fuchs).                                 |
|                                             | Pragmatism                   | Amplified instrumentalism: the success of a theory/model depends on the useful effects it produces (including prediction/control).                                                                                                                                                                                            |
| Logics of Corroboration (Testing)           | Inductivism                  | Theories/models receive inductive support (confirmation) from observation statements (data) consistent with them. Includes Bayesian and frequentist approaches.                                                                                                                                                               |
|                                             | Falsificationism             | Theories/models can only be refuted by observation statements, never confirmed. Variants: dogmatic, methodological, naïve, and sophisticated falsificationism (Popper, Peirce).                                                                                                                                               |
| Ontological and Modeling Norms              | Ontological Commitments      | E.g., rational expected utility-maximizing agents in economics; “waves”/“particles” in QM; networks (of interactions, information flows, trust, epistemic states) in social network science.                                                                                                                                  |
|                                             | Commitments to Model Classes | E.g., teleological models in economics; causal models in physics; functional models in sociology and anthropology.                                                                                                                                                                                                            |
| Explanatory Norms                           | Explanatory Depth            | Some disciplines value explanations with high logical depth (e.g., mathematics, theoretical physics).                                                                                                                                                                                                                         |
|                                             | Explanatory Coverage         | Some disciplines value parsimony – explaining much by little (Ockham’s Razor).                                                                                                                                                                                                                                                |
| Justification Norms and Strategies          | Reductive Approaches         | Reduce a set of facts/theories/models to a more basic core (e.g., game theory in human/animal behavior).                                                                                                                                                                                                                      |
|                                             | Eliminative Approaches       | Eliminate phenomena as epi-phenomenal (e.g., eliminativist theories of consciousness).                                                                                                                                                                                                                                        |
|                                             | Assimilative Approaches      | Assimilate facts or models from other paradigms to support one’s own approach (e.g., transaction cost economics).                                                                                                                                                                                                             |
| Logical and Meta-Logical Norms of Inference | **—**                        | Heuristics and norms constraining scientific reasoning; commitments to deductive, inductive, or abductive inference; positions on replication, reproduction, generalization, and application, ranging from “we’re done” to “we don’t know what you are referring to.”                                                         |


### C.4 Table 4. Types of Agents – A Preliminary Synopsis

| Id | Type (Intra- / Inter-Disciplinary) | Use Case / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:---|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| L1 | INTER / INTRA                      | Translator / Re-Voicer: Re-voices or reformulates an argument, derivation, or empirical result using the terminology, inferential logic, and rhetorical conventions of another disciplinary community. For example, translating a result in transaction-cost economics into neoclassical economics, or reframing an economic coordination model in the discourse of social psychology to expose hidden assumptions.                                                                   |
| L2 | INTRA                              | Challenger / Interrogator: Emulates the critical stance of peer reviewers within the same field. It raises discipline-typical questions about inferential validity, effect-size reliability, replicability, generalizability, relevance, and informativeness, helping researchers anticipate critiques likely to arise during the review process.                                                                                                                                     |
| L3 | INTER                              | Challenger / Interrogator: Operates across disciplinary boundaries, posing challenges concerning ontological choices (e.g., individual vs. systemic causation), modeling conventions (causal vs. functional explanations), or inferential schemes (frequentist vs. Bayesian reasoning). Serves as an epistemic bridge exposing implicit disciplinary biases.                                                                                                                          |
| L4 | INTRA                              | Deconstructor: Analyzes scholarly text to extract the normative and descriptive statements presupposed by its arguments, i.e., the background axioms and warrants that must hold for the claims to be accepted within the field. Reveals hidden epistemic commitments and disciplinary norms.                                                                                                                                                                                         |
| L5 | INTER                              | Deconstructor: Performs the same function across disciplines, reconstructing what norms, empirical regularities, or theoretical premises would have to hold for a claim in one field to be persuasive in another. Useful for mapping commensurability between paradigms.                                                                                                                                                                                                              |
| L6 | INTRA                              | Arbiter: Evaluates descriptive, methodological, and normative claims within a discipline, comparing them against canonical findings or accepted background results. Acts as an internal auditor of epistemic coherence and methodological rigor.                                                                                                                                                                                                                                      |
| L7 | INTER                              | Referee: Designs or identifies “crucial experiments” capable of arbitrating between competing theories from different disciplines, i.e., experiments whose results would be regarded as binding by both sides (for example, testing cognitive-economics versus behavioral-sociology explanations of cooperation).                                                                                                                                                                     |
| L8 | INTRA                              | Model Expander / Contractor: For a given axiomatic system, explores consequences of adding or removing assumptions, e.g., introducing risk aversion into the Modigliani–Miller theorem or bounded rationality into Nash bargaining. Derives empirical predictions of the modified theory, functioning both as generator and critic of extensions.                                                                                                                                     |
| L9 | INTRA                              | Meta-Analyzer: Conducts meta-analyses by aggregating and weighting existing studies according to effect size, reliability, reproducibility, and generalizability. Helps identify empirical regularities, contradictions, and potential boundary conditions.                                                                                                                                                                                                                           |
| L10 | INTRA                              | AltGen (Alternative Explanation Generator): For a given empirical result, generates one or more competing explanations from within the same field that yield identical predictions but rest on different assumptions or mechanisms—for instance, behavioral-economics findings interpreted via “irrationality” versus “contextual adaptive rationality,” or cognitive-neuroscience data explained by distinct architectural models.                                                   |
| L11 | INTER                              | AltGenX: Produces alternative explanations drawn from other disciplines that predict the same empirical regularities but imply different theoretical or practical conclusions, e.g., framing an organizational behavior result in terms of evolutionary game theory or sociotechnical systems design.                                                                                                                                                                                 |
| L12 | INTER                              | AltGenM: Generates explanations from other fields that rely on different model ontologies, for example, replacing a causal model with a teleological or functional one, or re-describing a psychological process using network or dynamical-systems language.                                                                                                                                                                                                                         |
| L13 | INTRA                              | PrisM (Predictive / Reflective Implication Synthesizer): For a given model or theory, derives implications for related theories of the same phenomenon in adjacent disciplines (e.g., computational-vision models vs. neurophysiological models of vision). It also anticipates the kinds of questions a researcher from another field would ask to reach convergent understanding.                                                                                                   |
| L14 | INTRA                              | ArgMap (Argument Mapper): Reconstructs informal arguments within a discipline using the claim–warrant–backing schema (approximately 82 canonical forms). Reveals the argumentative patterns regarded as valid or “warrantedly assertible” without further justification.                                                                                                                                                                                                              |
| L15 | INTRA                              | ArgDef (Argument Defeater): Generates prima facie defeaters – counterarguments that undermine or qualify claims identified by *ArgMap* – using norms that are themselves warranted within the same field. Provides internal dialectical testing.                                                                                                                                                                                                                                      |
| L16 | INTER                              | ArgDef (Cross-Field Defeater): Constructs defeaters or counterarguments warranted in another discipline that studies similar phenomena, illuminating how a claim valid in one field might fail under another’s epistemic criteria.                                                                                                                                                                                                                                                    |
| L17 | INTER / INTRA                      | RadianX (Reasoning and Dialogue Network): Builds structured, tree-like representations of dialogues on a shared empirical or theoretical problem, tracking each assertion, clarification, question, answer, and response. Evaluates conversational moves according to discursive norms – validity, relevance, informativeness, coherence, semantic consistency, and responsiveness – common to one or more fields. Enables transparent mapping of reasoning paths across disciplines. |
