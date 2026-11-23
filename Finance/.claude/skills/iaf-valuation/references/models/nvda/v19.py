# NVIDIA (docs/nvda-analysis.md) -- IAF model, version 1.9, 19 Nov 2026 (price = 18 Nov close $150.96).
# Built on v18.py (v1.8). One change, a company-level turn call in Base (Leading view; user 19 Nov; families L4 capital
# allocation -1, L3 customer credit -1, L5 market pricing -1 against L1 guidance +1; ~65%): customer funding continues
# at the 2026 pace, $75bn a year 2027-29 into stakes, loans and support (Q3 FY27: equity purchases 58.1bn in 9M,
# guarantees +9.5bn); the funded book is junk-rated and worth half at exit (stake factor 0.5, glided in V_t);
# guarantees called $15bn in 2028 and 2029 and $30bn owed at exit; the market prices recurring vendor-financing
# losses with exit P/E 15 (AI BBB H1 reference 17). The order cut by funded buyers is a demand call for the AI BBB
# (not here). Bear (financing break: funding stops) and Bull as v1.8.
from v18 import *
import v18 as _v
BASE = dict(_v.BASE, stakes=[75, 75, 75], sf=0.5, sfg=[5 / 6, 2 / 3, 0.5], charge=[0, 15, 15], exitliab=30, pe=15)
BEAR = dict(_v.BEAR)
BULL = dict(_v.BULL)
V18BASE = dict(_v.BASE)


def er(P, nibor=4.72):
    """E / R on this module's Base and Bear (NIBOR window 4.72%)."""
    rb = build(BASE, P); rr = build(BEAR, P)
    V26b, Vb = interim(rb, 'Base', P); V26r, Vr = interim(rr, 'Bear', P)
    rb27 = (rb['D'][2] + Vb[0]) / V26b - 1
    rr27n = (rr['D'][2] + Vr[0]) * NOKF['Bear'][1] / V26r - 1
    basen = nok_irr(rb, 'Base', P)
    return (basen * 100 - nibor) / ((rb27 - rr27n) * 100), rb27, rr27n
