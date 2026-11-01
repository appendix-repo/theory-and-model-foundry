"""Check 06. The numbers and counter-examples in Run 05 (Model Builder; appendix 3.4).

Run 05 cites an "informal numeric check, items 1-6" made with a plain-Python
script that was not kept ("scratchpad/mb/check.py, not published"). This file is
a new script, written for this repository, that recomputes every number Run 05
cites, and runs the "checker-ready statements" of Run 05 Section 7 in SymPy.

Status note. The appendix says no derivation can be marked `closed` until the
Stage 1 checking backend exists (Sections 1.4, 6). This script does not change
any status in the theory object or the appendix. It lets a reader confirm the
arithmetic and the counter-examples on which Run 05's `open` and `refuted`
statuses rest.

Inferred parameters (not stated in Run 05, recovered so that the cited numbers
come out): item 4 uses beta_X = 0.3, beta_H = 1, sigma = 1; item 5 uses the
hybrid-safeguard schedule s_X(u) = 0.3 + 0.2 u. Both are flagged in the output.
"""
import math
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import Report


def crossings(bX, bH, sX, sH):
    """Pairwise crossing points of C_g = beta_g + s_g * phi, with s_M = 1, beta_M = 0."""
    return bX / (1 - sX), (bH - bX) / (sX - sH), bH / (1 - sH)


def chosen(phi, bX, bH, sX, sH):
    costs = {"M": phi, "X": bX + sX * phi, "H": bH + sH * phi}
    return min(costs, key=costs.get)


def logistic(z):
    return 1 / (1 + math.exp(-z))


def main():
    r = Report("Check 06: Model Builder (Run 05) numbers and counter-examples")

    # ---- Item 1: D6 counter-example to closure of P3 on A8 as stated ---------------------
    phiMX, phiXH, _ = crossings(0.6, 1.0, 0.5, 0.0)
    r.check("item 1 (D6): phi_MX at s=(1,0.5,0), bH=1, bX=0.6", round(phiMX, 6), 1.2)
    r.check("item 1 (D6): phi_XH", round(phiXH, 6), 0.8)
    grid = [i / 1000 for i in range(0, 5001)]
    picks = {chosen(p, 0.6, 1.0, 0.5, 0.0) for p in grid}
    r.check("item 1 (D6): structures ever chosen on phi in [0, 5]", sorted(picks), ["H", "M"])
    a, b, _ = crossings(0.5, 1.0, 0.5, 0.0)
    r.check("item 1 (D6): bX = 0.5 is the knife edge (phi_MX == phi_XH)", math.isclose(a, b), True)
    picks_ok = {chosen(p, 0.3, 1.0, 0.5, 0.0) for p in grid}
    r.check("item 1 (D6): with A18 satisfied (bX = 0.3) all three are chosen", sorted(picks_ok), ["H", "M", "X"])

    # A18 is equivalent to the hybrid lying strictly below the market-hierarchy chord.
    bX, bH, sX, sH = sp.symbols("beta_X beta_H s_X s_H", positive=True)
    a18 = bX / (1 - sX) - (bH - bX) / (sX - sH)          # < 0  <=>  A18
    chord = bX - bH * (1 - sX) / (1 - sH)                 # < 0  <=>  below the chord
    ratio = sp.simplify(sp.together(a18) / sp.together(chord))
    r.check("A18 (symbolic): (A18 expression) / (chord expression) == (1 - s_H) / ((1 - s_X)(s_X - s_H))",
            sp.simplify(ratio - (1 - sH) / ((1 - sX) * (sX - sH))), 0)
    r.info("[INFO] Since 1 > s_X > s_H, that factor is positive, so A18 holds iff (s_X, beta_X) lies below the chord.")

    # ---- Item 2: D10 counter-example: phi2 = k + u k exp(-k) on u in [0, 7] -----------------
    k, u = sp.symbols("k u", nonnegative=True)
    phi2 = k + u * k * sp.exp(-k)
    r.check("item 2 (D10): phi2(0, u) == 0", sp.simplify(phi2.subs(k, 0)), 0)
    r.check("item 2 (D10): d phi2/du == k exp(-k) (> 0 for k > 0)", sp.simplify(sp.diff(phi2, u) - k * sp.exp(-k)), 0)
    phik = sp.diff(phi2, k)
    mink = min(float(phik.subs({k: kk / 100, u: 7})) for kk in range(0, 2001))
    r.check("item 2 (D10): min over k in [0,20] of d phi2/dk at u = 7 is > 0", mink > 0, True)
    r.check("item 2 (D10): d phi2/dk at k=2 is 1 - u e^-2, positive iff u < e^2",
            sp.simplify(phik.subs(k, 2) - (1 - u * sp.exp(-2))), 0)
    cross2 = sp.simplify(sp.diff(phi2, k, u))
    r.check("item 2 (D10): d2 phi2/dk du == (1-k) exp(-k)", sp.simplify(cross2 - (1 - k) * sp.exp(-k)), 0)
    r.check("item 2 (D10): d2 phi2/dk du at k = 2 is negative", float(cross2.subs(k, 2)) < 0, True)

    # ---- Item 3: D9 counter-example on the probability scale, phi = u k -----------------
    sH_, bH_, sig = 0.1, 1.0, 1.0
    c = (1 - sH_) / sig
    for (kk, uu, P_stated, cross_stated, bracket_stated) in [(3, 1, 0.846, -0.10, -0.87), (1, 1, 0.475, 0.23, None)]:
        z = ((1 - sH_) * uu * kk - bH_) / sig
        P = logistic(z)
        lam = P * (1 - P)
        bracket = (1 - 2 * P) * c * uu * kk + 1          # phi_k phi_u = u k, phi_ku = 1
        cross = lam * c * bracket
        r.check(f"item 3 (D9): P at (k,u)=({kk},{uu})", round(P, 3), P_stated)
        r.check(f"item 3 (D9): cross-partial at ({kk},{uu}) (2 dp)", round(cross, 2), cross_stated)
        if bracket_stated is not None:
            r.check(f"item 3 (D9): bracket at ({kk},{uu}) (2 dp)", round(bracket, 2), bracket_stated)
        h = 1e-4
        Pf = lambda k_, u_: logistic(((1 - sH_) * u_ * k_ - bH_) / sig)
        fd = (Pf(kk + h, uu + h) - Pf(kk + h, uu - h) - Pf(kk - h, uu + h) + Pf(kk - h, uu - h)) / (4 * h * h)
        r.check(f"item 3 (D9): closed form agrees with finite differences at ({kk},{uu})", abs(fd - cross) < 1e-5, True)
    # Run 05's closed form for the cross-partial, checked symbolically.
    kk_, uu_, s_h, b_h, sg = sp.symbols("k u s_H beta_H sigma", positive=True)
    phi = sp.Function("phi")(kk_, uu_)
    Pexpr = 1 / (1 + sp.exp(-((1 - s_h) * phi - b_h) / sg))
    cc = (1 - s_h) / sg
    Ps = sp.Symbol("P")
    lam_expr = Pexpr * (1 - Pexpr)
    claimed = lam_expr * cc * ((1 - 2 * Pexpr) * cc * sp.diff(phi, kk_) * sp.diff(phi, uu_) + sp.diff(phi, kk_, uu_))
    r.check("item 3 (D9, symbolic): d2P/dk du == Lambda'(z) c [(1-2P) c phi_k phi_u + phi_ku]",
            sp.simplify(sp.diff(Pexpr, kk_, uu_) - claimed), 0)

    # ---- Item 4: D8 (P5) and D13 (P7) under the multinomial logit layer -------------------
    bX4, bH4, sig4 = 0.3, 1.0, 1.0      # inferred: reproduces 0.1745
    def PH(phi_, sX_=0.4, sH4=0.1):
        cs = [phi_, bX4 + sX_ * phi_, bH4 + sH4 * phi_]
        e = [math.exp(-x / sig4) for x in cs]
        return e[2] / sum(e)
    for uu in (0.5, 2.0):
        r.check(f"item 4 (D13): Pr(H | k=0, u={uu})", round(PH(0.0 * uu), 4), 0.1745)
    r.info("[INFO] item 4 parameters beta_X=0.3, beta_H=1, sigma=1 are inferred; Run 05 does not state them.")
    ok = all(math.log(PH(uu * (kk + 0.01))) > math.log(PH(uu * kk))
             for kk in [i / 10 for i in range(0, 100)] for uu in (0.5, 1.0, 2.0))
    r.check("item 4 (D8): ln Pr(H) increases in k on a grid (phi = u k)", ok, True)

    # ---- Item 5: expansion A21, s_X(u) rising in u ---------------------------------------
    s = sp.Symbol("s")
    bXs, bHs, sHs = sp.symbols("beta_X beta_H s_H", positive=True)
    sbar_sym = sp.solve(sp.Eq(bXs / (1 - s), (bHs - bXs) / (s - sHs)), s)
    r.check("item 5 (symbolic): solving the A18 boundary for s_X gives 1 - beta_X (1 - s_H)/beta_H",
            any(sp.simplify(x - (1 - bXs * (1 - sHs) / bHs)) == 0 for x in sbar_sym), True)
    sbar = 1 - 0.3 * (1 - 0.1) / 1.0
    r.check("item 5: s_bar at beta_X=0.3, beta_H=1, s_H=0.1 (2 dp)", round(sbar, 2), 0.73)
    sX_u = lambda uu: 0.3 + 0.2 * uu     # inferred schedule
    lo, hi, _ = crossings(0.3, 1.0, sX_u(0.5), 0.1)
    r.check("item 5: hybrid band at u = 0.5 (2 dp)", (round(lo, 2), round(hi, 2)), (0.5, 2.33))
    lo2, hi2, _ = crossings(0.3, 1.0, sX_u(2.0), 0.1)
    r.check("item 5: hybrid band width at u = 2 (2 dp)", round(hi2 - lo2, 2), 0.17)
    lo3, hi3, _ = crossings(0.3, 1.0, sX_u(2.5), 0.1)
    r.check("item 5: hybrid band empty at u = 2.5", hi3 <= lo3, True)
    r.info("[INFO] item 5 schedule s_X(u) = 0.3 + 0.2u is inferred; it is a linear schedule that reproduces all three cited values.")

    # ---- Item 6: contraction, remove A1 (pi == 0) ----------------------------------------
    picks6 = {chosen(0.0, bx, 1.0, sx, 0.1) for bx in (0.1, 0.3, 0.6) for sx in (0.2, 0.5, 0.8)}
    r.check("item 6: with pi == 0 (phi == 0) the market is chosen for every parameter set tried", picks6, {"M"})

    # ---- Run 05 Section 7 checker-ready statements not covered above -------------------
    q, pi = sp.Function("q"), sp.Function("pi")
    d = sp.Symbol("d", positive=True)
    kp, up = sp.symbols("k u", positive=True)
    r.check("Section 7 D4: d/dk [pi(u) q(k)] == pi(u) q'(k)",
            sp.simplify(sp.diff(pi(up) * q(kp), kp) - pi(up) * sp.diff(q(kp), kp)), 0)
    # D12: implicit-function derivative of the threshold k*(u) on the product instance.
    K = sp.Symbol("K", positive=True)
    F = d * pi(up) * q(K) - sp.Symbol("phi_XH", positive=True)
    dkdu = sp.idiff(F, K, up)
    expected = -(d * sp.diff(pi(up), up) * q(K)) / (d * pi(up) * sp.diff(q(K), K))
    r.check("Section 7 D12: dk*/du == -phi_u / phi_k", sp.simplify(dkdu - expected), 0)
    # D13: at k = 0 every C_g is independent of u.
    sXs, sHs2, bXs2, bHs2 = sp.symbols("s_X s_H2 beta_X2 beta_H2", positive=True)
    phi0 = (d * pi(up) * q(kp)).subs(kp, 0).subs(q(0), 0)
    C = [phi0, bXs2 + sXs * phi0, bHs2 + sHs2 * phi0]
    r.check("Section 7 D13: dC_g/du at k=0, q(0)=0, is 0 for all g", [sp.simplify(sp.diff(x, up)) for x in C], [0, 0, 0])
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
