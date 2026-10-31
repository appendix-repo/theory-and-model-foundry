# Run 05: Model Builder on the transaction-cost theory object
*Instruction set: Foundry v0.1, Role 4. Input: Run 01, reading 1. Single run, unedited.*

---

Input: theory object `tce:reading-1` ("economizing choice") from Run 01. Reading 1 was adopted for this demonstration only; in real use the theorist adopts it. New ids below (`tce:A16`–`tce:A21`, `tce:D4`–`tce:D12`, `tce:P6.mb1`, `tce:P6.mb2`, `tce:P10`, `tce:model-1`) are provisional, and the Provenance Ledger may renumber them.

Convention: "(stated)" means the step uses only nodes in reading 1. "(surfaced)" means it uses a node I add here. No derivation is marked `closed`, because no checker exists. A derivation that seems to follow from its premises is `asserted`. A derivation that does not follow from the stated nodes is `open`, and the auxiliaries it needs are listed. A derivation for which I give a counter-example is `refuted`. That counter-example has also not been checked.

---

## 1. Model class (step 1)

**Chosen:** an analytical **comparative-statics model of discrete governance choice**. Governance cost for each structure is a reduced form (in the spirit of Williamson 1991). It rests on a stylized **hold-up stage game**, and a **random-cost discrete-choice layer** produces the probabilities that P5 and P6 talk about.

**Why this class.**
- The stance profile lists `teleological` and `causal` model classes. Its inference norm is `deductive` ("therefore", s6; "It follows that", s9). Reading 1 makes alignment the outcome of cost-minimizing choice (A4, A13). Minimizing over three discrete alternatives is the most direct formal match for that.
- P5 and P6 (s11) are statements about a *probability*. So the model needs an explicit stochastic layer that links the deterministic optimum to observed frequencies. That layer is where the scale problem for P6 shows up (D9).

**Alternative named: property-rights incomplete-contracting game** (Grossman & Hart 1986; Hart & Moore 1990). In that game investment is endogenous, and ownership allocates residual control. I did not use it as the primary class, for two reasons:
- In that game integration does not remove hold-up. It only moves it to the other party. That contradicts A6 ("hierarchy suppresses opportunism", s7), which reading 1 holds as core.
- It replaces haggling and maladaptation costs with under-investment. Section 5 uses it as an expansion route instead (relaxing A10).

**Not used: an agent-based or replicator model.** That is the natural class for reading 2, where selection carries the explanation. Under reading 1 selection is only a backstop, so I leave P4 open (D11).

---

## 2. Construct-to-variable map (step 2)

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

## 3. Model specification (step 3)

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

## 4. Derivations (step 4)

### D4 → tce:P2 (the market hazard rises with asset specificity)
1. The appropriable quasi-rent is $q(k)$, with $q'>0$ (C2 definition, s4; A9) (stated).
2. Exposure under the market is $\pi(u)\,q(k)$, and $\partial_k[\pi q]=\pi q'>0$ because $\pi>0$ (A1) (stated).
3. So the hazard **as exposure** rises with $k$.

**Status: `asserted`.**

The cost reading of P2 (R4: hazard → C15) is different. At t3 the contested rent is a *transfer* between the parties. If renegotiation is efficient ($d=0$), then $\varphi\equiv 0$, and governance cost does not depend on $k$ at all. So the step from "exposure" to "higher governance cost" (C8.com1, R4) **fails to close** on the stated nodes. One minimal auxiliary closes it:

**tce:A16 (surfaced).** Ex post renegotiation is inefficient: it dissipates a positive share of the value at stake. Equivalently, $\varphi_k>0$ for the *cost* hazard.

The alternative closure is to drop A10 and let investment be endogenous, so that the cost appears as under-investment (Section 5b). **D5 is `open` without A16, and A16 carries every downstream derivation.**

### D6 → tce:P3 (discriminating alignment). This derivation fails to close.
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

### D7 → tce:P1 (firms exist)
1. Firms exist iff some $(k,u)$ in the support has $g^*=H$, that is, $\varphi(k,u)>\max(\varphi_{XH},\varphi_{MH})$.
2. A7 ($\beta_H>0$) and A6 ($s_H<1$) give a *finite* threshold. Nothing in the text says the hazard ever reaches it.

**Status: `open`.** Auxiliaries required: A16, A17. P1 is an existence claim, and it needs the range assumption A17.

### D8 → tce:P5 (Pr(integration) rises with asset specificity)
1. Under the logit layer, $\partial_k \ln\Pr(H)=\tfrac{1}{\sigma}\varphi_k\sum_g \Pr(g)\,(s_g-s_H)$.
2. Every term is non-negative, and the $g=M$ term is strictly positive. So the derivative is $>0$.
3. The result does not depend on the logit form. For any shock distribution independent of $k$, the event $\{C_H+\varepsilon_H<C_g+\varepsilon_g\ \forall g\}$ grows with $k$, because $C_H-C_g$ falls with $k$ for every $g\neq H$.

**Status: `asserted`.** Premises: A1, A2, A4, A6, A9, A10, A13. Auxiliaries required: A16, A20 (shocks independent of $k$). A18 is *not* needed: P5 survives even if hybrids are never chosen. (Informal numeric check, item 4.)

### D9 → tce:P6 (steeper in $k$ when $u$ is high), on the probability scale as s11 states it. Refuted.
In the binary case, with $c=(1-s_H)/\sigma$:
$$\partial^2_{ku}\Pr(H)=\Lambda'(z)\,c\,\big[(1-2P)\,c\,\varphi_k\varphi_u+\varphi_{ku}\big].$$

**Counter-example.** Take $\varphi=uk$, which *satisfies* every auxiliary in this run, including A19 below. Set $\beta_H=1$, $s_H=0.1$, $\sigma=1$. At $(k,u)=(3,1)$, $P=0.846$, and the bracket equals $1+(1-2P)\,0.9\cdot 3=-0.87<0$. So $\partial^2_{ku}P\approx-0.10$. At $(1,1)$, $P=0.475$ and the cross-partial is $+0.23$. (Informal numeric check, item 3.)

When integration is already likely, the probability saturates, and higher uncertainty *flattens* the slope in $k$. This is the logit/probit interaction problem of Ai & Norton (2003).

**Status: `refuted`** as a global claim about the probability scale. The counter-example is asserted and has not been checked by a Proof Verifier.

**Sufficient restriction.** If $P\le 1/2$ and A19 holds, the cross-partial is positive.

### D10 → tce:P6.mb1 (proposed restatement: the cross-partial on the **log-odds / latent-cost** scale is positive). Fails to close.
1. $\text{logit}\Pr(H\text{ vs }M)=[(1-s_H)\varphi-\beta_H]/\sigma$, so $\partial^2_{ku}=(1-s_H)\varphi_{ku}/\sigma$.
2. The sign is therefore the sign of $\varphi_{ku}$. The same holds for $H$ versus $X$, with factor $(s_X-s_H)$.
3. **What the stated nodes give.** $\varphi(0,u)=0$ (C8.pre1, consistent with P7), $\varphi_u>0$ for $k>0$ (A11 and C7.lic1), and $\varphi_k>0$. Together these imply only $\int_0^k\varphi_{ku}\,dk'=\varphi_u(k,u)>0$: the interaction is positive *on average from zero*, not at every point.
4. **Counter-example.** $\varphi=k+u\,k\,e^{-k}$ on $u\in[0,7]$ satisfies every stated condition: $\varphi(0,u)=0$, $\varphi_u=ke^{-k}>0$, and $\varphi_k=1+ue^{-k}(1-k)>0$ for $u<e^2$. But $\varphi_{ku}=(1-k)e^{-k}<0$ for $k>1$. (Informal numeric check, item 2.)
5. **Minimal auxiliary, tce:A19 (surfaced): the hazard is supermodular in specificity and uncertainty.** $\varphi_{ku}\ge 0$ everywhere, and $>0$ somewhere. In words, uncertainty raises the hazard *per unit* of specificity, not only its level. The product form $\pi(u)q(k)$ is a sufficient instance. The relation R2 lists C7 as a moderator but gives no sign or functional form, so the text does not supply A19.

**Status: `open`.** Auxiliaries required: A11, A16, A19. With them the derivation would be `asserted`.

### D12 → tce:P6.mb2 (alternative restatement: the specificity threshold for integration falls with uncertainty). Closes without A19.
1. Define $k^*(u)$ by $\varphi(k^*,u)=\varphi_{XH}$ (or $\varphi_{MH}$).
2. By the implicit function theorem, $dk^*/du=-\varphi_u/\varphi_k<0$, using $\varphi_u>0$ and $\varphi_k>0$.
3. Under any symmetric shock layer, $k^*(u)$ is the $k$ at which $\Pr(H)$ crosses its median.

**Status: `asserted`.** Premises: A1, A2, A4, A6, A9, A11, A13. Auxiliaries: A16, A17. **A19 is not needed.**

This "threshold" form of s11 carries less auxiliary load than either slope form. The theorist may prefer it.

### D11 → tce:P4 (misalignment raises costs and leads to exit)
- **The cost clause.** $C_g\ge C_{g^*}$ holds by the definition of $g^*$ (A4). It is analytically true inside the model, so on reading 1 it has no empirical content. **Status: `asserted` (definitional).**
- **The exit clause.** It needs population dynamics (A12, S2) that this model class does not contain. **Status: `open`**, not attempted. I recommend a replicator or agent-based model under reading 2.

### D13 → tce:P7 (no effect of uncertainty when specificity is near zero)
$\varphi(0,u)=0$, so $C_g(0,u)=\beta_g$ for every $g$, and $\Pr(g\mid 0,u)$ does not depend on $u$. (Informal numeric check, item 4: $\Pr(H\mid 0,u)=0.1745$ at $u=0.5$ and at $u=2$.)

**Status: `asserted`.** Premises: C8.pre1, together with reading 1's exclusion of A15. Note that this result holds *by construction*: the model contains no channel through which uncertainty affects cost when specificity is zero.

### Derivation table

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

## 5. Contraction and expansion (step 5)

### (a) Contraction: remove core tce:A1 (bounded rationality, so contracts are complete)
Then $\pi\equiv 0$, so $\varphi\equiv 0$ and $C_g=\beta_g$. The market is chosen for every $(k,u)$, because $\beta_M=0$. (Numeric check, item 6.)

**What fails:** P1, P2 (cost), P3, P5 and P6.

**What survives:** P7 holds trivially, and P4 becomes vacuous.

Removing A2 (opportunism) or A6 (hierarchy safeguards, $s_H\to 1$, which makes $H$ dominated by $M$) has the same effect on P1.

**Finding.** P6 needs more than A1 holding. A1 must be **graded**: incompleteness $\pi(u)$ has to *vary* with $u$, via A11. Run 01 treats A1 as a maintained constant ("held as a maintained assumption, not a variable", C5 measurement; C5.ent1). So the interaction prediction quietly turns a hard-core *constant* into a *variable* of the belt. The theorist should decide whether that is acceptable.

### (b) Expansion: add tce:A21 (natural auxiliary): hybrid safeguards degrade with uncertainty, $s_X'(u)>0$
A21 says hybrids adapt poorly to frequent disturbances. It is in the spirit of Williamson (1991) (to verify: exact formulation and page).

**Result 1: A18 becomes uncertainty-dependent.** The hybrid band vanishes once
$$s_X(u)\ \ge\ \bar s=1-\frac{\beta_X(1-s_H)}{\beta_H}.$$
With $\beta_X=0.3$, $\beta_H=1$, $s_H=0.1$ this gives $\bar s=0.73$. The hybrid's $\varphi$-band is $(0.50,\,2.33)$ at $u=0.5$ and has width $0.17$ at $u=2$. It is empty by $u=2.5$. (Numeric check, item 5.)

**New proposition, tce:P10 (proposed, surfaced):** at intermediate specificity, the share of hybrid governance falls with uncertainty, and at high uncertainty alignment becomes two-way (market, then hierarchy). P10 is a novel, testable consequence that reading 1 does not contain.

**Result 2: P6 is partly rescued without A19, for hierarchy versus hybrid.** $\partial^2_{ku}\,\text{logit}(H\text{ vs }X)=[s_X'(u)\varphi_k+(s_X-s_H)\varphi_{ku}]/\sigma$. The first term is positive, so a mildly negative $\varphi_{ku}$ is tolerated. The contrast of hierarchy against the *market* is unchanged and still needs A19.

**Result 3: P7 survives,** because $C_X(0,u)=\beta_X$ still does not depend on $u$.

**Alternative expansion, noted only.** Relax A10 so that specificity is chosen jointly with governance. This is the route of the Section 1 alternative model class. It could replace A16, because the cost would come from under-investment. But $k$ would then be endogenous to $g$, and the causal reading of P5 would require an instrument. That is a handoff to the Empirical Validation Designer.

---

## 6. Surfaced assumptions

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

## 7. Checker-ready statements (step 6)

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

## 8. Decisions for the theorist

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
