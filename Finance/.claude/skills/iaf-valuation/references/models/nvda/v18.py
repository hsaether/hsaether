# NVIDIA (docs/nvda-analysis.md) -- IAF model, version 1.8, 19 Nov 2026 (price = 18 Nov close $150.96).
# Built on v17.py (v1.7, Q3 FY27). One change: the AI BBB 18 Nov turn call (ai-market-bbb 2026-11-18.1) moved the
# H1 compute Base EPS path for 2028-30 from .91/.88/.87 to .85/.82/.81 x CY27 consensus 15.21 (7 Nov basis); 2027 .92
# kept. Everything else (stub from the 25 Oct balance sheet, payout 80%, GM 72.5%, stakes, Bear, Bull) as v1.7.
# The model date stays 17 Nov (stub cash flows); the one-day shift to the 18 Nov price is below rounding.
from v17 import *
import v17 as _v
BASE = dict(_v.BASE, eps=[0.92 * CY27, 0.85 * CY27, 0.82 * CY27], eps30=0.81 * CY27)
BEAR = dict(_v.BEAR)
BULL = dict(_v.BULL)


def er(P, nibor=4.72):
    """E / R on this module's Base and Bear (v17.er reads v17's own BASE; redefined here). NIBOR window 4.72%
    (HY BBB 18 Nov market path)."""
    rb = build(BASE, P); rr = build(BEAR, P)
    V26b, Vb = interim(rb, 'Base', P); V26r, Vr = interim(rr, 'Bear', P)
    rb27 = (rb['D'][2] + Vb[0]) / V26b - 1
    rr27n = (rr['D'][2] + Vr[0]) * NOKF['Bear'][1] / V26r - 1
    basen = nok_irr(rb, 'Base', P)
    return (basen * 100 - nibor) / ((rb27 - rr27n) * 100), rb27, rr27n
