"""NVIDIA (docs/nvda-analysis.md) -- v2.1, 23 Nov 2026: Huang reinstated as CEO (8-K 23 Nov, board action 22 Nov).
Base is the v1.9 model unchanged (v19.py: AI BBB 18 Nov H1 path, customer funding $75bn a year 2027-29, the funded
book at half at exit, guarantees called $15bn in 2028 and 2029 + $30bn owed at exit, exit P/E 15). This script adds:
 1. the reverse test at the new price (exit P/E and EPS multiplier for k; funding level for k);
 2. the 'Huang funding regime' named case [A]: funding $100bn a year (Q3 FY27 run-rate: guarantees +9.5 and equity
    15.7 in one quarter) or $125bn (plus the OpenAI backstop restored to the $250bn proposal: ~$145bn more over ~6
    years); guarantees scaled with the funding; window-only, or permanent (the extra funding continues after exit,
    half lost each year, capitalised at the exit P/E; Base's exit 15 already carries the $75bn permanent loss);
 3. the regime x demand grid (funding 75 / 100 permanent x the AI BBB order-cut watch 2028-30 x0.9);
 4. governance exit sensitivities (14 / 16) and the SEC-probe cases (v20_probe) at the new price.
Run from this folder: py v21_huang.py [price]
"""
import sys
import v19 as m

P = float(sys.argv[1]) if len(sys.argv) > 1 else 167.01   # v2.1 price: Nasdaq 10:17 ET 23 Nov 2026 (intraday)
B, BE, BU = m.BASE, m.BEAR, m.BULL
SH = m.SH
pct = lambda x: f"{x*100:.1f}%"


def r(s, P=P):
    x = m.build(s, P)
    return f"{pct(x['irr'])} (P_k ${x['pk']:.1f}, {x['pk']/P-1:+.1%})"


def cut(s, f=0.9):
    """AI BBB order-cut watch: 2028-30 EPS x f (2027 kept)."""
    return dict(s, eps=[s['eps'][0], s['eps'][1] * f, s['eps'][2] * f], eps30=s['eps30'] * f)


def regime(X, perm=True, base=B):
    """Customer funding X $bn a year 2027-29 (Base 75), the book at half; guarantees scaled X/75;
    perm: the extra (X - 75) continues after exit, half lost a year, deducted from 2030 earnings."""
    f = X / 75.0
    s = dict(base, stakes=[X, X, X], charge=[0, 15 * f, 15 * f], exitliab=30 * f)
    if perm:
        s['eps30'] = base['eps30'] - 0.5 * (X - 75) / SH
    return s


print(f"P = {P}")
for n, s in [('Bear', BE), ('Base', B), ('Bull', BU)]:
    x = m.build(s, P)
    print(f"{n}: {r(s)}; NOK {pct(m.nok_irr(x, n, P))}; capital {(sum(x['D'])+x['VT'])/P-1:+.1%}; sumD {sum(x['D']):.2f} VT {x['VT']:.1f}")
pk = m.build(B, P)['pk']
print(f"Triggers: clears <= {pk/1.02:.1f}; P_k {pk:.1f}; fails >= {pk/0.98:.1f}")
E, rb27, rr27 = m.er(P)
print(f"E/R {E:.3f} (Base 2027 {pct(rb27)}, Bear 2027 NOK {pct(rr27)})")

print("== Reverse test ==")
ek = m.solve(lambda x: m.build(B, P, pe=x)['irr'], 0.12, 5, 30)
print(f"exit P/E for k at P (Base EPS, funding, losses): {ek:.2f}")


def mult(x, pe=15):
    return m.build(dict(B, eps=[B['eps'][0], B['eps'][1] * x, B['eps'][2] * x], eps30=B['eps30'] * x, pe=pe), P)['irr']


for pe in (15, 16, 17):
    mk = m.solve(lambda x: mult(x, pe), 0.12, 0.3, 3.0)
    print(f"  exit {pe}: k at m={mk:.3f} ({[round(v*mk/m.CY27,2) for v in B['eps'][1:]]+[round(B['eps30']*mk/m.CY27,2)]})")
m0 = m.solve(lambda x: mult(x, 15), 0.0, 0.1, 3.0)
print(f"  exit 15: 0% at m={m0:.3f}")
# funding level (permanent, half lost) for k at P
Xk = m.solve(lambda x: m.build(regime(x), P)['irr'], 0.12, 0, 300)
print(f"funding level (permanent, half lost) for k at P: {Xk:.0f}bn a year")
Xk0 = m.solve(lambda x: m.build(regime(x), 125.53)['irr'], 0.12, 0, 400)
print(f"funding level (permanent, half lost) for k at 125.53: {Xk0:.0f}bn a year")
clean = dict(B, stakes=[75, 2, 2], charge=[0, 0, 0], exitliab=0, pe=17)
print("clean stop from 2028 (exit 17):", r(clean))
print("Base at exit 16 / 17:", r(dict(B, pe=16)), "/", r(dict(B, pe=17)))

print("== Huang funding regime (named case) ==")
for X in (100, 125):
    print(f"  ${X}bn a year, window only: {r(regime(X, perm=False))}; permanent: {r(regime(X))}")
print("== Regime x demand (permanent funding; AI BBB order-cut watch x0.9) ==")
for lab, s in [("75 (Base)", B), ("100 permanent", regime(100)), ("125 permanent", regime(125))]:
    print(f"  {lab}: demand Base {r(s)} | order cut {r(cut(s))}")
print(f"  50 permanent (Kress regime, tighter): demand Base {r(regime(50))} | order cut {r(cut(regime(50)))}")
for X in (100, 125):
    # extra cost of the heavier regime vs the cost of the order cut, P_k terms
    d_reg = m.build(B, P)['pk'] - m.build(regime(X), P)['pk']
    d_cut = m.build(B, P)['pk'] - m.build(cut(B), P)['pk']
    print(f"  P_k cost: regime {X} permanent ${d_reg:.1f} vs order cut ${d_cut:.1f} -> break-even order-cut odds avoided {d_reg/d_cut:.0%}")

print("== Governance exit (c) ==")
for pe in (13, 14, 16, 17):
    print(f"  exit {pe}: {r(B if pe is None else dict(B, pe=pe))}")
print("  Huang regime 100 permanent + exit 14:", r(dict(regime(100), pe=14)))

print("== Order cut (e) and SEC probe (g) at P ==")
print("  order cut:", r(cut(B)))
TAX = 0.17


def restate(s, bn):
    d = bn * (1 - TAX) / SH
    return dict(s, eps=[e - d for e in s['eps']], eps30=s['eps30'] - d, stakes=[st - bn * (1 - TAX) for st in s['stakes']])


cc = dict(restate(B, 10), charge=[0, B['charge'][1] + 10, B['charge'][2]], pe=14)
w = dict(restate(B, 25), charge=[0, B['charge'][1] + 25, B['charge'][2]], pe=13)
w4 = dict(w, eps=[w['eps'][0], w['eps'][1] - 0.1 * B['eps'][1], w['eps'][2] - 0.1 * B['eps'][2]], eps30=w['eps30'] - 0.1 * B['eps30'])
print("  SEC central:", r(cc), "| wide:", r(w), "| wide + order cut:", r(w4))

print("== Rule 3 and return bridge ==")
x = m.build(B, P)
print(f"P/FCF_norm {P/B['eps30']:.1f}x vs ceiling {x['irr']/0.0144:.1f}x")
core = P - x['nc0'] - x['st0']; pe0 = core / B['eps'][0]
print(f"core {core:.2f} ({pe0:.2f}x Base 2027; {core/B['eps30']:.2f}x 2030); earnings at today's multiple {pe0*B['eps30']-core:+.1f}; "
      f"re-rating to 15 {(B['pe']-pe0)*B['eps30']:+.1f}; net cash {x['NC'][-1]-x['nc0']:+.2f}; sumD {sum(x['D']):.2f}; "
      f"book {x['ST'][-1]*0.5 - x['st0']:+.2f}; liab {-B['exitliab']/SH:.2f}; total {sum(x['D'])+x['VT']:.1f}")
V26, V = m.interim(x, 'Base', P)
print(f"Base V_t {round(V26,1)}, {[round(v,1) for v in V]}, {x['VT']:.1f}")
