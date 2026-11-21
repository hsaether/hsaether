"""Scatec v2.1 (21 Nov 2026): re-mark of the v2 build (30 Oct, NOK 84.65) at a new price, date and FX.
No dividends, so IRR = (V_T / P)^(1/T) - 1 and P_k = V_T / 1.12^T. V_T (NOK) of v2: Bear 45.3 / Base 136.9 / Bull 212.0 at
USD/NOK 9.1871 and I-44 106.66 (30 Oct). FX at spot (Base rule): all blocks, project and corporate debt (NOK bonds swapped to USD)
are foreign-currency, so V_T scales with the revenue basket 0.4 x USD/NOK + 0.6 x I-44 (A14) [A].
Run: py v21.py [price] [YYYY-MM-DD] [USD/NOK] [I-44]
"""
import sys, math
from datetime import date

K = 0.12; EXIT = date(2029, 12, 31)
V2 = {'Bear': 45.3, 'Base': 136.9, 'Bull': 212.0}; P2, D2 = 84.65, date(2026, 10, 30)
NOKPATH = {'Bear': 1.072, 'Base': 1.0, 'Bull': 0.976}
# v2 sensitivity table (V_T at 30 Oct FX) and the Philippine break-even grid (IRR at 84.65 -> V_T)
SENS = {'Asset rate 10%': 124.8, 'Asset rate 8%': 150.2, 'Philippines 450 a year': 117.5, 'Philippines 900 / 1,000 / 1,000': 152.9,
        'Philippine asset rate 13%': 132.4, 'Contracted EBITDA -NOK 150m': 126.1, 'No D&C platform value at exit': 120.0,
        'Growth equity at cost (F = 1.0)': 133.0, 'No working-capital release': 131.8}
PHIL = {400: 0.106, 500: 0.123, 600: 0.139, 750: 0.164}

P = float(sys.argv[1]) if len(sys.argv) > 1 else 82.40
d0 = date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else date(2026, 11, 20)
usd = float(sys.argv[3]) if len(sys.argv) > 3 else 9.7525
i44 = float(sys.argv[4]) if len(sys.argv) > 4 else 110.74
T = (EXIT - d0).days / 365.25; T2 = (EXIT - D2).days / 365.25
f = 0.4 * usd / 9.1871 + 0.6 * i44 / 106.66
irr = lambda v, p=P: (v / p) ** (1 / T) - 1
pk = lambda v: v / (1 + K) ** T
print(f"P {P} {d0} T {T:.3f}; FX factor {f:.4f} (USD/NOK {usd}, I-44 {i44}); v2 check Base {(136.9/P2)**(1/T2)-1:.3%}")
for n, v in V2.items():
    vt = v * f; vn = vt * NOKPATH[n]
    print(f"{n}: V_T {vt:.1f} IRR {irr(vt):.1%} (NOK path {irr(vn):.1%}) P_k {pk(vt):.1f} MoS {pk(vt)/P-1:+.1%} | FX held at 30 Oct: IRR {irr(v):.1%} P_k {pk(v):.1f} MoS {pk(v)/P-1:+.1%}")
for lab, v in SENS.items():
    vt = v * f; print(f"  {lab}: V_T {vt:.1f} IRR {irr(vt):.1%} P_k {pk(vt):.1f} MoS {pk(vt)/P-1:+.1%}")
for k_ in (0.13, 0.14):
    print(f"  k {k_:.0%}: P_k {V2['Base']*f/(1+k_)**T:.1f} ({V2['Base']*f/(1+k_)**T/P-1:+.1%})")
grid = sorted((ph, P2 * (1 + r) ** T2 * f) for ph, r in PHIL.items())
def phil_for(target_v):
    for (a, va), (b, vb) in zip(grid, grid[1:]):
        if va <= target_v <= vb: return a + (b - a) * (target_v - va) / (vb - va)
    (a, va), (b, vb) = (grid[0], grid[1]) if target_v < grid[0][1] else (grid[-2], grid[-1])
    return a + (b - a) * (target_v - va) / (vb - va)
print(f"Philippine EBITDA (2028-29 and mid) for k: ~NOK {phil_for(P*(1+K)**T):.0f}m; for 0%: ~NOK {phil_for(P):.0f}m")
f0 = 1.0; grid0 = sorted((ph, P2 * (1 + r) ** T2) for ph, r in PHIL.items())
grid, g_ = grid0, grid
print(f"  at 30 Oct FX: for k ~NOK {phil_for(P*(1+K)**T):.0f}m")
