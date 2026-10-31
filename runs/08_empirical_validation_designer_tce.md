# Run 08: Empirical Validation Designer on the transaction-cost theory object
*Instruction set: Foundry v0.1, Role 6. Inputs: Run 01 reading 1; rivals from Runs 02, 03, 04. Single run, unedited.*

---

## 0. Target, rivals and conventions

**Theory under test.** `tce:reading-1` ("economizing choice", Run 01). Parties choose the structure that governs a transaction most cheaply (tce:A4 core, via tce:A13). Asset specificity is decisive (tce:A5 core). Uncertainty only moderates (tce:P6, tce:P7). Selection is a backstop (tce:A12 auxiliary).

**Rivals.**
- **INST**: the field-template account (Run 03, §2, rows X1 to X5).
- **BEH**: problemistic search and routine replication (Run 04, §2, the rows in bold).
- **RD**: resource-dependence theory, `rd:reading1` (Run 02). Its core includes rd:A2 (power = dependence) and rd:A4 (boundaries are set by political management of dependence, not by cost minimization). Its predictions are rd:P4 to rd:P9.

**Conventions.** "(R0n: id)" cites a node or row of Run 0n. "(assumption)" marks an effect-size or base-rate prior that I chose and nobody has measured. "(to verify)" marks a citation or magnitude I am not sure of. All power calculations use two-sided α = 0.05 and power 0.80, so (z₀.₉₇₅ + z₀.₈₀)² = (1.960 + 0.842)² = 7.849. Equivalence tests (TOST) use one-sided α = 0.05 each way and power 0.80 when the true effect is zero, so (z₀.₉₅ + z₀.₉₀)² = (1.645 + 1.282)² = 8.565. I mark no derivation closed.

**Severity (Mayo 2018).** A design is severe for reading 1 if a result that agrees with reading 1 would be *improbable* were reading 1 false and the rival true. For each design I give an indicative figure, P(agreeing result | rival true). It is roughly the rival-side miss rate (1 − power, or the equivalence analogue) plus the probability that the main threat alone produces the agreeing result. These figures are judgments, not estimates.

---

## 1. Risky-prediction table (step 1)

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

## 2. Measurement (step 2): indicators both sides could accept

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

## 3. Designs (steps 3 and 4)

### D1. Persistence of insourcing after a disaster disrupts a generic input (RP2; also bears on RP1)

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

### D2. Uncertainty effect within the low-specificity stratum, with prior routines (RP1, RP3)

- **Design.** A cross-section of components within firms, restricted to the lowest band of specificity indicator (a). Logit of make on standardized demand volatility, with firm fixed effects. A second regressor is an indicator for prior in-house production of a related item (RP3).
- **Identification.** Within-firm variation across components holds the firm's governance competence and template constant. The test of RP1 is an **equivalence test**, because reading 1 predicts a point null.
- **Main threat.** Measurement error in specificity. If volatile components are also somewhat more specific than indicator (a) records, a spurious uncertainty effect appears, and it biases the test *against* reading 1. A second threat is that reading 1 can retreat to reading 3 (tce:A5.r3), which is a belt move. The test therefore bears on tce:A5 *as core*, not on the programme.
- **Power.** Base rate of make in the low-specificity stratum: p = 0.20, so p(1 − p) = 0.16 (assumption). BEH smallest effect of interest: OR = 1.3 per SD of volatility, so β* = ln 1.3 = 0.2624 and β*² = 0.06883 (assumption; Walker & Weber 1984 report a volume-uncertainty effect, magnitude to verify). Using Hsieh, Bloch & Larsen (1998, to verify), n = 7.849 / (0.16 × 0.06883) = 7.849 / 0.011013 = 713. The variance inflation for correlated covariates, 1/(1 − 0.30) = 1.43, gives **1,018 components**. Equivalence with margin |ln OR| < 0.262: n = 8.565 / 0.011013 = 778, × 1.43 = **1,111 components**.
- **Severity.** P(agreeing result | BEH true) ≈ 0.20 + measurement-error risk. That risk biases toward rejecting reading 1, not toward agreeing with it, so it does not raise the figure. About **0.20 for tce:P7**. The test discriminates TCE from BEH on tce:A5's core status, but a reading-1 loss can be absorbed by a change of reading, so the severity is lower for the *programme*.

### D3. A trade shock that adds alternative sources, with specificity fixed (RP4)

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

### D4. Japanese transplants vs domestic manufacturers in one host country (RP5)

- **Design.** Component-level governance (coded in three categories, then collapsed to binary non-market) for Japanese-owned and US-owned car assemblers in the US. They share one legal regime and one supplier base but have different home templates (the keiretsu-type hybrid; R03: O5; Dyer 1996, to verify).
- **Test.** The specificity slope on P(non-market) *within* the Japanese group.
- **Predictions.** Reading 1: positive, with a level difference permitted (the cost curves may differ). INST: about zero, because the hybrid template is applied whatever the attributes (R03: X1, X2).
- **Main threat.** Reading 1 can absorb a zero slope by positing that the Japanese hybrid is cheaper than the market at *every* level of specificity, which revises tce:A8 in the belt. Without an independent measure of tce:C15 (Run 01 Q8; R03: O3), that move cannot be blocked. The severity of D4 therefore depends on the theorist answering Q8.
- **Power.** Same priors as D6. OR = 1.8 per SD (assumption, to verify) and p = 0.6, so p(1 − p) = 0.24. n = 7.849 / (0.24 × 0.3455) = **95**, × 1.43 = **136 components** in the Japanese group.
- **Severity.** P(agreeing result | INST true) ≈ 0.05 (false positive) in sampling terms. But a *disagreeing* result can be absorbed in the belt with probability I put at ≈ 0.5 (judgment), so the design tests tce:A8 more than tce:A4. **Discriminates on its face; only moderately severe for the core.**

### D5. Attribute effects by adoption order in a boundary-change diffusion (RP6)

- **Design.** An event history of a boundary change, for example outsourcing of a function. Interact specificity with the adopter's position on the diffusion curve (early half vs late half). Add lagged peer prevalence, instrumented by shocks to peers' peers (to address reflection; Manski 1993).
- **Predictions.** Reading 1: the specificity effect is constant or rising (learning). INST: the specificity effect declines and prevalence has a positive effect.
- **Main threat.** Reading 1 can treat prevalence as lowering governance cost (thicker markets for the new structure), so the prevalence coefficient does not discriminate. Only the decline in the attribute effect does.
- **Power.** Detect a fall from OR 1.8 (early) to 1.0 (late), a difference in log OR of 0.588, with p(1 − p) = 0.24 (assumptions). The difference has variance 2 / (n_h × 0.24). n_h = 2 × 7.849 / (0.24 × 0.3455) = 15.698 / 0.08292 = **190 adopters per half**, × 1.43 ≈ **543 adopters**.
- **Severity.** P(agreeing result | INST true) ≈ 0.20 + ≈ 0.20 (instrument weakness or reflection) ≈ **0.40**. **Discriminates weakly.**

### D6. Cross-sectional replication of tce:P5 (N1): low-severity contrast

- **Design.** A logit of make on an engineering-effort specificity proxy, after Monteverde & Teece (1982), with uncertainty and the interaction term (tce:P5, tce:P6).
- **Power.** OR = 1.8 per SD (assumption; Monteverde & Teece 1982 and the reviews of Lafontaine & Slade 2007 and Macher & Richman 2008 report consistent positive effects, magnitudes to verify) and p = 0.4, so p(1 − p) = 0.24. n = 7.849 / (0.24 × 0.3455) = **95**, × 1.43 = **136 components**. The design is cheap and well powered.
- **Severity.** All three rivals predict the same sign: BEH through salience (R04: beh:O3), INST through the US template (R03: §2), and RD because specific assets reduce alternatives (inferred). P(agreeing result | any rival true) ≈ **0.8 to 0.9** (judgment). **Merely consistent.** A positive estimate adds almost nothing to the case for tce:A4 over its rivals. This bears out the Interlocutors' downgrade of the provisional "novel" status of tce:P5 (Run 01 Q10; R04: beh:O3).

### D7. Exit hazard by alignment status (RP7): low severity for reading 1's core

- **Design.** A Cox model of firm exit on the share of spend that is misaligned, with controls for slack, size, and the legitimacy of the form (its prevalence in the field) (R03: O8; R04: beh:O8).
- **Power.** Hazard ratio 1.3 (assumption) and 30% of firms misaligned. Using Schoenfeld's formula, d = 7.849 / (0.21 × 0.06883) = 7.849 / 0.01445 = **543 exits**.
- **Severity.** It discriminates the rivals on tce:A12. But tce:A12 is **auxiliary** in reading 1, so a null leaves tce:A4 untouched. **Consistent-only for reading 1's core.** It would be the top-severity design under reading 2 (tce:A12.r2 core; tce:P9).

---

## 4. Severity ranking (step 5)

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

## 5. Crucial-experiment check (step 6)

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

## 6. Additions to `openQuestions`

- **V1.** The equivalence margins (3 pp in D1; OR 1.3 in D2; RR 0.8 in D3) are what make reading 1's null predictions refutable. Who sets them, and from what? No published magnitudes are known to me (assumption).
- **V2.** D4 and D7 lose most of their severity unless tce:C15 has an independent measure (Run 01 Q8). Is a measure such as renegotiation frequency or dispute cost (R04: beh:O2) acceptable as that measure?
- **V3.** Does input-level make-or-buy data across disaster-hit suppliers exist outside cooperating firms? (To verify.)

---

## 7. Decisions for the theorist

1. **Adopt, amend or reject the risky-prediction table** (RP1 to RP7). In particular, confirm that N3 (acquirer identity) is outside reading 1, so that it cannot count against it.
2. **Approve the measurement rules in §2**, especially the three-way governance coding (which answers Run 01 Q7 for these tests) and the ex ante specificity bands.
3. **Decide whether to pre-register that a defence of D1 through uncertainty counts as a move to reading 3.** Without that rule D1 loses most of its severity.
4. **Set or delegate the equivalence margins** (V1). They are effect-size priors, not findings.
5. **Choose which designs to commission.** D1 is the most severe but needs firm-level partners. D3 needs its outcome widened to reach adequate power. D6 is cheap but merely consistent; commission it only as a calibration check.
6. **Decide whether to answer Run 01 Q8** (an independent measure of governance cost) before running D4. The answer determines whether D4 tests the core or only tce:A8.
7. **Have the "(to verify)" citations and magnitudes checked** before any prior is used in a pre-registration. These include Walker & Weber 1984; Nunn 2007; Pierce & Schott 2016; Alfaro et al. 2016; Dyer 1996; Carvalho et al. 2021; Boehm et al. 2019; Lafontaine & Slade 2007; Macher & Richman 2008; Hsieh et al. 1998; and Casciaro & Piskorski 2005 magnitudes.
