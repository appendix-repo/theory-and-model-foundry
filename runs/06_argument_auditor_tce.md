# Run 06: Argument Auditor on the transaction-cost exposition
*Instruction set: Foundry v0.1, Role 5. Input: case_inputs.md Input A, anchored to Run 01 reading 1. Single run, unedited.*

---

Scope and conventions. I audit Input A as the theorist's own exposition, using Run 01's segmentation (s1 to s11, with s5 split into s5a and s5b) and the ids of reading 1 ("economizing choice"). Adopting reading 1 is the theorist's decision; I use it here only because the demonstration proceeds on it. "(text)" means the passage states it. "(inferred)" means I infer it. Every literature citation is marked "(to verify)" except Toulmin (1958) and the Williamson works named in the input's own header. No derivation (tce:D1 to tce:D3) is marked closed, because no checker has run.

---

## 1. Argument map (ArgMap, Toulmin scheme)

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

## 2. Warrant gaps

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

## 3. Inference-mode check: deductive language covering abductive or inductive moves

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

## 4. Defeaters (ArgDef-INTRA): one per warrant, from within transaction-cost and organizational economics

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

## 5. Arbitration (Arbiter-INTRA): conflicts with canonical findings

1. **tce:P5: broadly consistent.** Surveys of the make-or-buy literature report that the positive association between measures of asset specificity and integration is among the more robust findings (Shelanski & Klein 1995, to verify; Macher & Richman 2008, to verify). No conflict, but see W10 on causal interpretation.
2. **tce:P6 and the role of uncertainty: mixed record.** The same surveys report that uncertainty effects are inconsistent in sign and significance (to verify). The exposition presents P6 with the same confidence as P5 ("we should observe"). The canonical record does not support that equal confidence. P6 should carry a weaker qualifier.
3. **tce:A6 and tce:P1: theoretical conflict.** Grossman and Hart (1986, to verify) is a canonical result within the field. It denies that common ownership as such suppresses hold-up, which is the claim s7 asserts. The exposition does not engage with it. This is a substantive, not a presentational, conflict.
4. **tce:P3 against tce:P5: internal tension sharpened by evidence.** Joskow (1987, to verify) finds that high specificity is often governed by long-term contracts (hybrids), not by integration. This is consistent with three-way tce:P3, but it means that a binary test of tce:P5 that codes hybrids as "not integrated" will understate the effect of specificity (Run 01, Q7).
5. **Testability (meta-logical norm).** tce:C15 (comparative governance cost) has no measure independent of the alignment it explains (Run 01, Q8). Together with W9-i, this leaves tce:P1 and tce:P3 open to the long-standing charge that transaction-cost explanations are ex post rationalizations (a critique associated with, for example, Ghoshal & Moran 1996, to verify). P5 and P6 are the exposition's only escape from that charge, and they rest on W10 and W11.

---

## 6. Additions proposed for `openQuestions` (not adopted)

- Q13 (W6): Does the theorist hold that tce:A1 and tce:A2 apply inside hierarchies? If they do, what removes hold-up there?
- Q14 (W8): Should comparative governance cost (tce:C15) be widened to total cost (governance plus production)?
- Q15 (W4): Should frequency (tce:C4) enter as a moderator of tce:R3, with recurrence lowering the hazard through reputation?
- Q16 (MM3, MM4): Should "It follows that" (s9) and "will" (s5b, s10) be replaced with qualified language until a checker closes tce:D1?

---

## Decisions for the theorist

1. **Accept, reject or amend each of the 11 warrant gaps** (W1 to W11). For each accepted gap, choose whether to state the missing warrant as an explicit assumption, which assumptions would be new and which are surfaced ids already, or to weaken the claim instead.
2. **Decide how to handle the five mode mismatches** (MM1 to MM5). Requalify the prose, or supply derivations to be sent to the checker (tce:D1, tce:D3 first). In particular, decide whether s9's "It follows that" is to be defended as a derivation or restated as a hypothesis.
3. **Respond to W6 and Arbitration 3** (property-rights challenge to tce:A6). The options are to restrict scope, to condition A6 on whose investment matters, or to argue that the challenge does not apply. This touches the hard core.
4. **Set the confidence level for tce:P6** relative to tce:P5, given the derivation gap (W11) and the mixed record (Arbitration 2).
5. **Decide whether to add a production-cost term** (W8) and a frequency relation (W4), which would close Run 01's Q5.
6. **Approve or reject the proposed open questions Q13 to Q16.**
7. **Verify, or have verified, every literature citation marked "(to verify)"** before any defeater or arbitration point is entered in the Provenance Ledger.
