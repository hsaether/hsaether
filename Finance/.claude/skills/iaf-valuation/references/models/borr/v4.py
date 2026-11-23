"""Borr Drilling v4 (21 Nov 2026): Q3 update as an adjustment layer on the v3.1 build (28 rigs, no insurance; equity at exit
Bear -2,844 / Base -615 / Bull +1,713 $m; docs/borr-analysis.md v3.1). The v3 rig-by-rig model was not kept as a script.
Adjustments ($m at exit, all scenarios) [A]:
  insurance  +200  Prospector 5 hull value recommended for payment, due 24 Nov 2026 (Q3 release); applied to debt
  interest    +58  8.9% note interest saved on the 200, Dec 2026 - Dec 2029, compounded (kept as cash at 4%: +25)
  Q3/Q4       -5   Q3 EBITDA 78.9 vs model 83.4; Q4 guided 'broadly in line with Q3' (~79) vs model 79.8
  contracts   +8   Ran (Eni, firm to Dec 2027), Hild (Nigeria, 365 days from late Q1 2027), Vali (to Sep 2027), Skald option
No distributions in any scenario, so IRR = (V_T/P)^(1/T) - 1 and P_k = V_T / 1.12^T.
Run: py v4.py [price USD] [YYYY-MM-DD]
"""
import sys
from datetime import date

K = 0.12; EXIT = date(2029, 12, 31); SH = 309.11      # m shares outstanding 30 Sep 2026
EQ31 = {'Bear': -2844.0, 'Base': -615.0, 'Bull': 1713.0}
ADJ = dict(insurance=200.0, interest=58.0, q3q4=-5.0, contracts=8.0)
P = float(sys.argv[1]) if len(sys.argv) > 1 else 3.41
d0 = date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else date(2026, 11, 20)
T = (EXIT - d0).days / 365.25


def res(eq, p=P):
    vt = max(eq, 0.0) / SH
    irr = (vt / p) ** (1 / T) - 1 if vt > 0 else -1.0
    return vt, irr, vt / (1 + K) ** T


print(f"P ${P} {d0} T {T:.3f}; adjustments {ADJ} = {sum(ADJ.values()):+.0f}")
for n, e in EQ31.items():
    eq = e + sum(ADJ.values()); vt, irr, pk = res(eq)
    nok = ((vt * (0.97 if n == 'Bull' else 1.09)) / P) ** (1 / T) - 1 if vt > 0 else -1.0
    print(f"{n}: equity at exit {eq:,.0f}  V_T {vt:.2f}  IRR {irr*100:.1f}% (NOK path {nok*100:.1f}%)  P_k {pk:.2f}  MoS {pk/P-1:+.1%}" if vt > 0
          else f"{n}: equity at exit {eq:,.0f}  V_T 0  IRR -100%  P_k 0")
b = EQ31['Bull'] + sum(ADJ.values())
for lab, de in [('insurance kept as cash at 4%', -33), ('reversion tail on the Bull exit (v3 +0.18/sh)', 56),
                ('contracts firm today only (v3 -0.16/sh)', -49), ('exit marks at Oslo Bull mid-cycle return (v3 -0.43/sh)', -133),
                ('no insurance (v3.2 basis)', -258)]:
    vt, irr, pk = res(b + de); print(f"  Bull {lab}: V_T {vt:.2f} IRR {irr*100:.1f}% P_k {pk:.2f}")
# Base cash flows, exit values at a higher Base mid-cycle (v3 table at $4.40: equity at exit per share 0.52 / 3.03 / 5.37 at $120k / $130k / $140k
# on 308.5m shares), plus this version's adjustments
for r, v3 in ((120, 0.52), (130, 3.03), (140, 5.37)):
    vt, irr, pk = res(v3 * 308.5 + sum(ADJ.values())); print(f"  Base cash flows, exit mid-cycle ${r}k: V_T {vt:.2f} IRR {irr*100:.1f}% P_k {pk:.2f}")
