"""Micron v4 extras: NOK IRR (Equity BBB path: Bear +12% 2027, +9% after; Bull -3%), E / R, book at exit, Rule 3."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v4
from datetime import date
P = float(sys.argv[1]) if len(sys.argv) > 1 else 705.27
d0 = date(2026, 11, 18)
F = {'Bear': [1.12, 1.09, 1.09], 'Base': [1, 1, 1], 'Bull': [0.97, 0.97, 0.97]}
R = {n: v4.build(s, P, d0) for n, s in v4.SCEN.items()}
for n, r in R.items():
    cf = [r['cfs'][0]]
    for i, (t, c) in enumerate(r['cfs'][1:-1]):
        cf.append((t, c * F[n][i // 4]))
    cf.append((r['cfs'][-1][0], r['cfs'][-1][1] * F[n][2]))
    print(n, 'NOK IRR', f"{v4.irr(cf)*100:.1f}%")
nc0 = 84.0 / v4.SH
V0 = P + (v4.NC26 / v4.SH - nc0)
def r27(n, s):
    r = R[n]; core0 = (P - nc0) / r['eps'][0]
    pe = s['pe'] if n == 'Bear' else core0 + (s['pe'] - core0) / 3
    return (r['D'][0] + pe * r['eps'][1] + 60 / v4.SH) / V0 - 1
b27 = r27('Base', v4.SCEN['Base']); be27 = (1 + r27('Bear', v4.SCEN['Bear'])) * 1.12 - 1
E = R['Base']['irr'] * 100 - 4.72; Rr = (b27 - be27) * 100
print(f"E/R: E {E:.1f} pp, R {Rr:.1f} pp (Base 2027 {b27*100:.1f}%, Bear 2027 NOK {be27*100:.1f}%), E/R {E/Rr:.3f}")
# book at exit: v3 Base 268bn on old NI and D; adjust
old = v4.build(v4.V3_BASE, P, d0)
for n, r in R.items():
    base_old = {'Bear': 205, 'Base': 268, 'Bull': 303}[n]
    ref = old if n == 'Base' else r
    bk = base_old + (sum(r['ni']) - sum(ref['ni'])) - (r['sumD'] - ref['sumD']) * v4.SH
    s = v4.SCEN[n]; mcap = r['VT'] * v4.SH
    print(f"{n}: book exit {bk:.0f}bn / {bk/v4.SH:.0f} per sh; P/B {mcap/bk:.2f}; ROE30 {r['e30']*v4.SH/bk*100:.0f}%")
rb = R['Base']
print(f"Rule 3: P/FCF_norm {P/rb['e30']:.1f}x vs ceiling {rb['irr']/0.0144:.1f}x")
w = 0.25 * R['Bear']['irr'] + 0.5 * rb['irr'] + 0.25 * R['Bull']['irr']
print(f"Share of Bull priced {(P-rb['pk'])/(R['Bull']['pk']-rb['pk']):+.0%}")
# price at which E/R = 0.254 and Base = HY 7.5%
f = lambda p: v4.build(v4.SCEN['Base'], p, d0)['irr']
print(f"Base = HY market 7.5% at ${v4.solve(f, 0.075, 300, 1500):.0f}")
