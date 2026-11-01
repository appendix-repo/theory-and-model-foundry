"""Check 07. Power calculations of Run 08 (Empirical Validation Designer; appendix 3.6).

Recomputes every sample size in Run 08 Section 3 from the effect-size priors the
run states. The priors are the agent's assumptions (marked "(assumption)" in the
run) and are not verified here; only the arithmetic is.

Constants. Run 08 uses (z_.975 + z_.80)^2 = 7.849 for two-sided 5% tests at 80%
power, and 8.565 = (z_.95 + z_.90)^2 for equivalence (TOST at 5%, 80% power,
true difference 0). Both are recomputed from the normal quantiles below.

Rounding. Run 08 rounds some intermediate n before multiplying by a design
effect and not others. Each figure is therefore checked to within +/- 1.5 of the
recomputed value, and the unrounded value is printed.

Known issue (appendix Section 3.0, citation table, Hsieh et al. 1998): Run 08's
variance inflation 1/(1 - 0.30) = 1.43 treats 0.30 as the squared multiple
correlation rho^2. If 0.30 were meant as rho, the factor would be 1/(1 - 0.09) = 1.10.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import Report

z = NormalDist().inv_cdf
K80 = (z(0.975) + z(0.80)) ** 2          # 7.849
KEQ = (z(0.95) + z(0.90)) ** 2           # 8.565
VIF = 1 / (1 - 0.30)                     # 1.43 as used in Run 08
TOL = 1.5


def two_prop(p1, p2):
    pbar = (p1 + p2) / 2
    a = z(0.975) * math.sqrt(2 * pbar * (1 - pbar))
    b = z(0.80) * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return (a + b) ** 2 / (p2 - p1) ** 2


def logistic_n(p, odds_ratio, k=K80):
    """Hsieh, Bloch & Larsen (1998) for one standardized continuous covariate."""
    return k / (p * (1 - p) * math.log(odds_ratio) ** 2)


def main():
    r = Report("Check 07: Run 08 power calculations")
    r.check("constant (z.975 + z.80)^2", round(K80, 3), 7.849, tol=0.001)
    r.check("constant (z.95 + z.90)^2", round(KEQ, 3), 8.565, tol=0.002)

    # D1: two proportions, 0.02 vs 0.05; design effect 1 + (m-1) ICC with m=5, ICC=0.10.
    n1 = two_prop(0.02, 0.05)
    deff = 1 + 4 * 0.10
    r.info(f"D1 superiority n per arm (unrounded) = {n1:.2f}")
    r.check("D1: n per arm", round(n1), 588, tol=TOL)
    r.check("D1: design effect", deff, 1.4, tol=1e-9)
    r.check("D1: n per arm after clustering", round(588 * deff), 823, tol=TOL)
    r.check("D1: total firm x input pairs (about)", 2 * 823, 1650, tol=5)
    neq = KEQ * (2 * 0.02 * 0.98) / 0.03 ** 2
    r.info(f"D1 equivalence n per arm (unrounded) = {neq:.2f}")
    r.check("D1: equivalence n per arm", round(neq), 373, tol=TOL)
    r.check("D1: equivalence n after clustering", round(373 * deff), 522, tol=TOL)

    # D2: logistic, p = 0.20, OR = 1.3 per SD.
    n2 = logistic_n(0.20, 1.3)
    r.info(f"D2 n (unrounded) = {n2:.2f}; with VIF = {n2 * VIF:.2f}")
    r.check("D2: n", round(n2), 713, tol=TOL)
    r.check("D2: n with variance inflation", n2 * VIF, 1018, tol=TOL)
    n2e = logistic_n(0.20, 1.3, KEQ)
    r.check("D2: equivalence n", round(n2e), 778, tol=TOL)
    r.check("D2: equivalence n with variance inflation", n2e * VIF, 1111, tol=TOL)

    # D3: Poisson rate ratio 0.80, base rate 0.005 per pair-year, overdispersion 1.5.
    bound = math.log(0.8) ** 2 / K80
    E2 = 2.25 / bound
    r.info(f"D3 (ln 0.8)^2 / 7.849 = {bound:.6f}; E2 >= {E2:.1f}")
    r.check("D3: control events E2", math.ceil(E2), 355)
    r.check("D3: treated events E1", round(0.8 * 355), 284)
    r.check("D3: pair-years per tercile", 355 / 0.005, 71000, tol=1)
    r.check("D3: with overdispersion 1.5", 71000 * 1.5, 106500, tol=1)
    avail = 20000 * 8 / 3
    r.check("D3: available pair-years per tercile (stated as 53,300)", avail, 53300, tol=40)
    E2_av = avail * 0.005 / 1.5
    r.check("D3: effective control events available", E2_av, 177.7, tol=0.2)
    lhs = K80 * (1 / (0.72 * E2_av) + 1 / E2_av)
    r.check("D3: at RR 0.72, 7.849 x (1/(0.72 E2) + 1/E2) <= (ln 0.72)^2", lhs <= math.log(0.72) ** 2, True)
    lo, hi = 0.5, 0.99
    for _ in range(60):
        mid = (lo + hi) / 2
        ok = K80 * (1 / (mid * E2_av) + 1 / E2_av) <= math.log(mid) ** 2
        lo, hi = (lo, mid) if not ok else (mid, hi)
    r.info(f"D3 minimum detectable rate ratio (solved) = {lo:.3f}")
    r.check("D3: minimum detectable RR 'near 0.72'", round(lo, 2), 0.72, tol=0.01)
    r.check("D3: underpowered for RR 0.80 (available < required)", avail < 106500, True)

    # D4 and D6: OR 1.8 per SD, p(1-p) = 0.24.
    n4 = K80 / (0.24 * math.log(1.8) ** 2)
    r.info(f"D4/D6 n (unrounded) = {n4:.2f}")
    r.check("D4/D6: n", math.ceil(n4), 95)
    r.check("D4/D6: n with variance inflation", 95 * VIF, 136, tol=TOL)
    # D5: difference in log OR of ln 1.8, two halves.
    n5 = 2 * K80 / (0.24 * math.log(1.8) ** 2)
    r.check("D5: adopters per half", math.ceil(n5), 190)
    r.check("D5: total adopters with variance inflation", 2 * 190 * VIF, 543, tol=TOL)
    # D7: Schoenfeld, HR 1.3, 30% misaligned.
    d7 = K80 / (0.3 * 0.7 * math.log(1.3) ** 2)
    r.check("D7: exits required", round(d7), 543, tol=TOL)

    r.info(f"[INFO] Variance inflation used in Run 08: 1/(1-0.30) = {VIF:.3f}. If 0.30 is rho rather than rho^2: {1 / (1 - 0.09):.3f}.")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
