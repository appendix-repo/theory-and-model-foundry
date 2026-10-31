# Run 04: Interlocutor (behavioral lens) on the transaction-cost theory object
*Instruction set: Foundry v0.1, Role 2, lens = behavioral. Input: Run 01, reading 1. Single run, unedited.*

---

## 0. Lens and target

**Lens (behavioral row).** Stance: positivism with process realism. Ontology: boundedly rational decision makers, aspiration levels, routines, coalitions. Preferred model class: process and simulation models. Corroboration: inductivist, process-tracing. Canonical corpus: Simon 1947, 1955; March & Simon 1958; Cyert & March 1963; Kahneman & Tversky 1979; Greve 2003.

**Target.** `tce:reading-1` ("economizing choice"), Run 01. Basis convention: "(R01: id)" means the claim rests on that node of the Run 01 object. "(lens)" means it is a claim of my tradition, not of the text.

**Position.** I speak for the Carnegie tradition. We do not object that transaction-cost economics borrowed bounded rationality from us. We object that it borrowed the word and dropped the theory. In reading 1, bounded rationality limits only the people who write contracts (`tce:A1`). The people who choose governance are assumed to compare the costs of three discrete structures and pick the cheapest (`tce:A4`, `tce:A13`). A behavioral model of the firm makes the opposite assumption: governance is chosen by the same limited, satisficing, coalition-bound decision makers. Most of the objections below follow from that one point.

---

## 1. Objections, ranked by strength

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

### beh:O1. Bounded rationality applies to contracting but not to the choice of governance
- **Type:** 1 (unentitled commitment), 4 (disputed model class).
- **Targets:** tce:A4 (core), tce:A13 (auxiliary in reading 1), tce:A1 (core), tce:R9 (teleological), tce:M3, tce:P3.
- **Objection.** Reading 1 says contracting parties cannot foresee contingencies (R01: tce:A1). It also says the same parties can identify, in advance, which of three governance structures minimizes the combined costs of hazard, bureaucracy and weakened incentives over the transaction's life (R01: tce:A13, tce:C15.com1). These two claims are inconsistent. Evaluating governance costs in advance requires anticipating exactly the contingencies that `tce:A1` says cannot be anticipated. Simon's (1955) decision maker does not optimize over alternatives. She searches sequentially until an alternative meets an aspiration level and stops there. Cyert & March (1963) add that search is *problemistic*: it starts when performance falls short and looks first near the current solution. Under that model, the decision process cannot produce cost-minimizing alignment. At most it produces local, history-dependent satisficing. The Explicator raised this tension (R01: Q2; Decision 2). I hold that it removes the support reading 1 gives to `tce:A4` (core), because `tce:A4` connects cost comparisons to outcomes only through `tce:A13`.
- **Why fatal.** In reading 1, `tce:A4` is core and `tce:A13` is the only route from `tce:C15` to `tce:C9` (R01: tce:R9, tce:M3). If `tce:A13` is withdrawn to protect `tce:A1`, reading 1 has no mechanism left for `tce:P3`. Retreating to selection (`tce:A12`) changes the reading to reading 2 (R01: D1). That makes the retreat a change of programme, not an adjustment in the protective belt.
- **What would answer it.** One of the following. (a) A *procedural* account of governance choice in which satisficing searchers with aspiration feedback converge on discriminating alignment, together with conditions on search breadth, feedback lags and aspiration updating, shown in a simulation (lens). (b) An explicit argument that governance choice is an easier problem than contract writing: fewer alternatives, coarser criteria, a repeated decision with learning. This would restate `tce:A13` as a claim about the task, and it would need evidence. (c) Adopting reading 2 and accepting its scope restriction (R01: S2.r2). Williamson's own phrase, "intendedly rational, but only limitedly so" (taken from Simon 1947), does not answer the objection. It names the inconsistency without resolving it.

### beh:O2. The governance-cost construct is inferred from the outcome it explains
- **Type:** 2 (tautological construct).
- **Targets:** tce:C15, tce:C16, tce:C8, tce:P1, tce:P3.
- **Objection.** Comparative governance cost has "no direct measure" and is "read off asset specificity and governance attributes" (R01: tce:C15 measurementCommitments, tce:C15.ent1). The hazard is likewise "read off asset specificity" (R01: tce:C8). Alignment is defined as conformity to the rule `tce:P3` states (R01: tce:C16.ent1). So when a structure is observed, the theory is entitled to say it was the cheaper one. When it is not observed, the theory calls it misalignment, a cost that is not yet visible. `tce:P1` ("firms exist because...") then explains the existence of firms by a cost advantage that is attributed because firms exist. Simon (1991, *JEP*, "Organizations and markets") made a related complaint against the new institutional economics: its efficiency stories are fitted after the fact, and an auxiliary assumption can always be found to rationalize the observed form. A process theorist asks for the cost estimate the decision makers *actually formed* and the record of the comparison they *actually made*. Reading 1 supplies neither.
- **Strength:** damaging. It does not refute any core assumption. It takes away the evidential value of `tce:P1` and `tce:P3` until `tce:C15` has a measure independent of `tce:C9` (cf. R01: Q8).
- **What would answer it.** An indicator of governance cost recorded *before* the governance outcome and independently of it: for example, measured renegotiation frequency, dispute costs, or delivery-failure rates for comparable transactions under each structure. Alternatively, process-tracing of actual make-or-buy deliberations showing that a cost comparison of the theory's kind was made.

### beh:O3. P5 and P6 do not distinguish this theory from a behavioral rival (AltGenX)
- **Type:** 3 (accommodation presented as prediction).
- **Targets:** tce:P5 (factStatus "novel", provisional), tce:P6 (factStatus "novel", provisional).
- **Objection.** A Carnegie model predicts the same signs for a different reason. Highly specific inputs are the ones whose supply problems hurt most and are most visible: a die for one customer, a co-located plant, firm-specific skills. A shortfall from aspiration on such an input is therefore more likely and more salient. It triggers problemistic search, and local search reaches "do it ourselves" first, because that alternative is under the decision maker's own control (Cyert & March 1963). This gives `tce:P5`. Under high uncertainty, shortfalls are more frequent and the organization's standing preference for *uncertainty avoidance* through a "negotiated environment" (Cyert & March 1963) is engaged more often. This makes the response to specificity-linked shortfalls steeper, which gives `tce:P6`. Neither prediction needs opportunism or cost minimization. The provisional "novel" status (R01: tce:P5, tce:P6; Q10) should be read in the Lakatosian sense: a fact is novel for the programme only if its rivals did not equally predict it. In the cross-section, these two facts are predicted equally well by the rival.
- **Strength:** damaging. Cross-sectional confirmations of P5 and P6 (Monteverde & Teece 1982; Masten 1984) remain evidence, but they do not count as severe tests of `tce:A4` against the behavioral rival.
- **What would answer it.** Predictions on which the two accounts diverge (see Section 2): the *timing* of integration relative to performance shortfalls, the role of prior in-house routines, and a main effect of uncertainty. Then evidence on those predictions.

### beh:O4. Uncertainty acts by itself, and P7 forbids that
- **Type:** 5 (refuting evidence), 3.
- **Targets:** tce:P7 (surfaced), tce:C3.pre1, tce:A5 (core in reading 1).
- **Objection.** Reading 1 forbids uncertainty from raising integration when asset specificity is near zero (R01: tce:P7, tce:C3.pre1). Our tradition predicts the opposite main effect. Uncertainty avoidance is a general property of organizational decision making, not a moderator of hold-up (Cyert & March 1963). Kahneman & Tversky's (1979) loss aversion also makes a supply disruption weigh more than an equal expected saving from buying. The evidence I know of points our way. Walker & Weber (1984, *ASQ*) found that volume uncertainty and comparative production costs mattered for make-or-buy, while asset-specificity measures (supplier-market competition) had weak effects (to verify: exact variables and effect sizes). David & Han (2004, *SMJ*) reviewed the empirical TCE literature and reported that support for the uncertainty predictions was mixed and inconsistent, weaker than for asset specificity (to verify: tallies). If an uncertainty main effect holds, `tce:P7` is refuted and `tce:A5` ("decisive") is under pressure. Under reading 1 that is a core assumption.
- **Strength:** damaging. It would be fatal to `tce:A5` only if the theorist keeps `tce:A5` core and the main effect survives a test with specificity held near zero.
- **What would answer it.** A test restricted to low-specificity transactions that shows no uncertainty effect. Alternatively, a move to reading 3 (R01: A5.r3, P7.r3), which admits the main effect but explains it by `tce:A15` (adaptation costs) rather than uncertainty avoidance. The theorist should then show that A15 and uncertainty avoidance can be told apart.

### beh:O5. Asset specificity is produced by routines and integration, not given before them
- **Type:** 1 (unentitled commitment), 3.
- **Targets:** tce:A10 (surfaced auxiliary), tce:C2, tce:R13, tce:P5.
- **Objection.** `tce:A10` treats asset specificity as fixed before, and independently of, governance. Specific skills and know-how are learned in the doing, and they are learned where the activity is carried out. A component made in-house builds firm-specific routines (March & Simon 1958, on performance programs). Those routines are what a later study codes as "specific human assets". Read this way, the engineering-effort measure in Monteverde & Teece (1982) is as much a *consequence* of prior integration as a cause of it (lens; to verify whether their design rules this out). Argyres (1996, *SMJ*) reports make-or-buy decisions driven by relative capabilities more than by hazard (to verify). The arrow in `tce:R13` may run backwards, or a common cause (the firm's history of routines) may drive both sides.
- **Strength:** damaging. `tce:A10` is auxiliary, so the core survives. But the causal reading of `tce:P5` does not survive without it (R01: D2 derivation note).
- **What would answer it.** Measures of specificity taken before the governance decision (e.g. new products or new transactions where no in-house routine yet exists), or an instrument for specificity. Plus a demonstration that prior in-house production of related items does not account for the specificity-integration association.

### beh:O6. The decision maker is a coalition, not a single economizer, and governance changes in episodes, not continuously
- **Type:** 4 (disputed ontology and model class).
- **Targets:** tce:C17, tce:C9, tce:A3, tce:R9; stanceProfile.modelClasses ("teleological", "functional").
- **Objection.** Reading 1 has "parties" choose a governance structure for each transaction, as a comparative static (R01: tce:A3, tce:C1.lic1, tce:R9). In our ontology the firm is a coalition of participants with partly conflicting goals. Conflict is settled only partly ("quasi-resolution"), through sequential attention to goals and organizational slack (Cyert & March 1963). A make-or-buy decision is a bargaining outcome among, for example, purchasing, manufacturing and engineering, each with its own aspiration levels. Governance is also *sticky*: it changes in episodes, after problems, and rarely as continuous adjustment to a transaction attribute. The right model class is a process or simulation model with attention, aspiration and search rules (lens). A transaction-by-transaction discrete-choice model is not. `tce:A3` (the transaction as the unit) is a methodological choice we reject, not a finding.
- **Strength:** damaging. It is a rival programme's hard core, so it cannot refute `tce:A3` alone. It does predict observable patterns that reading 1 does not (Section 2).
- **What would answer it.** Evidence that governance choices across a firm's transactions are independent once transaction attributes are controlled, with no clustering by decision unit, by period or by preceding performance shortfall. Alternatively, an explicit statement that reading 1 is an "as-if" model of outcomes and makes no claim about process, with the scope consequences that follow (see beh:O1).

### beh:O7. Opportunism is assumed without evidence, and it ignores what is known about fairness and norms
- **Type:** 1.
- **Targets:** tce:C6, tce:A2 (core), tce:C8.ent1.
- **Objection.** Opportunism is "held as a maintained assumption" with no measure (R01: tce:C6). Its entitlement condition depends on an assumption that opportunists cannot be identified in advance, which the Explicator surfaced and flagged (R01: tce:C6.ent1). Behavioral evidence shows that renegotiation is limited by fairness norms. Kahneman, Knetsch & Thaler (1986, *AER*) found that people judge it unfair to exploit a shift in bargaining power, and they punish those who do. Exchange relationships also build reputational and normative constraints over time. So the size of the hazard is a variable, and it should be measured, not assumed. Ghoshal & Moran (1996, *AMR*) argue further that assuming opportunism and governing to suit it can produce the behavior it assumes (to verify their exact claim; their argument is close to the institutional lens).
- **Strength:** damaging. `tce:A2` asserts only "some" opportunism (R01: s5b), so it is hard to refute. That same weakness makes `tce:C8` impossible to estimate.
- **What would answer it.** An indicator of opportunism risk at the level of the dyad (e.g. history of disputes, renegotiation attempts, or the partner's reputation), and a test showing that it moderates the effect of specificity on integration as `tce:R3` requires.

### beh:O8. Selection is too weak to serve as a backstop
- **Type:** 4, 5.
- **Targets:** tce:A12 (auxiliary in reading 1), tce:C18, tce:P4, tce:M4.
- **Objection.** Organizational slack absorbs inefficiency in good times (Cyert & March 1963). Aspirations adapt downward after sustained poor performance (Greve 2003). Meyer & Zucker (1989, *Permanently Failing Organizations*) document organizations that persist at low performance. A misaligned transaction inside a large firm costs too little to affect the firm's survival (cf. R01: tce:C17.r2.lic1). `tce:P4` has no observable attached (R01: tce:P4, factStatus undetermined).
- **Strength:** minor in reading 1, where `tce:A12` is a backstop. It would be **fatal** under reading 2, where `tce:A12.r2` is core.
- **What would answer it.** Exit-hazard evidence by alignment status (R01: tce:P9), with slack and firm size controlled.

### beh:O9. Frequency plays no role, and the ordering of hybrids is assumed
- **Type:** 1.
- **Targets:** tce:C4, tce:C11, tce:A8.
- **Objection.** Frequency enters no relation (R01: Q5). Our tradition gives it the role it obviously has: recurrence is the condition for *routinization* (March & Simon 1958). Recurrent transactions get standard operating procedures, and those procedures tie the activity to whoever performs it. The theory has left out its most behavioral variable. Hybrids are placed "between" market and hierarchy by assumption (R01: tce:A8, surfaced). The ordering is never derived.
- **Strength:** minor.
- **What would answer it.** A stated relation for `tce:C4`, and an argument or evidence for `tce:A8`.

---

## 2. Rival explanation (AltGenX): problemistic search and routine replication

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

## 3. Open questions added (for `openQuestions`)

- **beh:Q1.** Can `tce:A13` be restated as a claim about the task (governance choice is easier than contract completion) and given its own evidence? If not, does reading 1 hold together at all? (beh:O1)
- **beh:Q2.** Is there a measure of `tce:C15` taken before, and independently of, the governance outcome? (beh:O2; extends R01: Q8)
- **beh:Q3.** Do the cited findings bear as stated? Walker & Weber 1984, David & Han 2004, Argyres 1996, Ghoshal & Moran 1996: exact findings to verify. (beh:O4, O5, O7)
- **beh:Q4.** Is Monteverde & Teece's (1982) specificity measure measured before integration? (beh:O5)
- **beh:Q5.** I am unsure whether the inconsistency in beh:O1 is fatal or only damaging. That depends on whether the theorist reads `tce:A4` as a claim about a process or as an "as-if" claim about outcomes. I have rated it on the process reading, which is the one reading 1 states (R01: tce:R9 "teleological").

---

## 4. Decisions for the theorist

1. **Respond to beh:O1.** Choose one: (a) give a procedural account under which satisficing choosers produce alignment; (b) restate `tce:A13` as a claim about the task, with evidence; (c) move to reading 2 and accept its scope restriction; or (d) declare reading 1 "as-if" and give up its process claims. Only you can decide whether this objection is accepted as fatal.
2. **Decide whether `tce:P5` and `tce:P6` keep "novel" status**, given that the behavioral rival predicts them equally well (beh:O3).
3. **Decide the status of `tce:A5` and `tce:P7`** in light of the predicted uncertainty main effect (beh:O4). Keeping `tce:A5` core exposes it to refutation. Moving to reading 3 absorbs the effect, at the cost of `tce:A15`.
4. **Decide how `tce:A10` will be defended** (beh:O5): pre-decision measures, an instrument, or downgrading `tce:P5` to an association.
5. **Accept or reject `tce:A3`** as against the behavioral ontology, with the decision unit (coalition) as the actor (beh:O6).
6. **Decide whether opportunism (`tce:C6`) becomes a measured variable** (beh:O7).
7. **Decide whether to forward the diverging rows of Section 2 to Role 6** as risky predictions.
