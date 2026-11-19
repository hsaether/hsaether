"""NVIDIA v1.9 extras: driver breakdown with the funding step, price-implied path at exit 15, funding variants,
order-cut call (AI BBB), corrected return bridge. Run: py v19_extra.py [price]"""
import sys
import v19 as m
P = float(sys.argv[1]) if len(sys.argv) > 1 else 150.96
B, BE, BU = m.BASE, m.BEAR, m.BULL
pct = lambda x: f"{x*100:.1f}%"
def r(s): x = m.build(s, P); return f"{pct(x['irr'])} (${x['pk']:.1f}, {x['pk']/P-1:+.1%})"
print("Driver Bear:")
s = dict(B, eps=BE['eps'], eps30=BE['eps30'], rev=BE['rev'], capex=BE['capex']); print(" 1 path, revenue, capex", r(s))
s = dict(s, pe=13); print(" 2 + exit 13", r(s))
s = dict(s, stakes=BE['stakes'], charge=BE['charge'], exitliab=BE['exitliab'], sfg=BE['sfg']); print(" 3 + funding stops (financing break), Bear costs = Bear", r(s), "| Bear", r(BE))
print("Driver Bull:")
s = dict(B, eps=BU['eps'], eps30=BU['eps30'], capex=BU['capex']); print(" 1 path, capex", r(s))
s = dict(s, pe=19); print(" 2 + exit 19", r(s))
s = dict(s, stakes=BU['stakes'], charge=BU['charge'], exitliab=BU['exitliab'], sf=BU['sf'], sfg=BU['sfg']); print(" 3 + funding at the Bull's own pace, no losses, stakes 1.25", r(s), "| Bull", r(BU))
print("Base build-up from v1.8:")
v = m.V18BASE; print(" v1.8", r(v))
s = dict(v, stakes=[75, 75, 75]); print(" + funding 75/yr", r(s))
s = dict(s, sf=.5, sfg=B['sfg']); print(" + stakes 50%", r(s))
s = dict(s, charge=[0, 15, 15], exitliab=30); print(" + guarantees", r(s))
s = dict(s, pe=15); print(" + exit 15 (= v1.9)", r(s), "| v1.9", r(B))
def mult(x, pe=15):
    return m.build(dict(B, eps=[B['eps'][0], B['eps'][1] * x, B['eps'][2] * x], eps30=B['eps30'] * x, pe=pe), P)['irr']
mk = m.solve(lambda x: mult(x), 0.12, 0.3, 2.0); m0 = m.solve(lambda x: mult(x), 0.0, 0.1, 2.0)
c = m.CY27
print(f"Price-implied at exit 15: k at m={mk:.3f} ({[round(v_*mk/c,2) for v_ in B['eps'][1:]]+[round(B['eps30']*mk/c,2)]}); 0% at m={m0:.3f}")
cut = dict(B, eps=[B['eps'][0], B['eps'][1] * .9, B['eps'][2] * .9], eps30=B['eps30'] * .9)
print("Order cut x0.9 (AI BBB watch):", r(cut))
print("Funding 100/yr:", r(dict(B, stakes=[100, 100, 100])), "| 50/yr:", r(dict(B, stakes=[50, 50, 50])))
print("Funding stops from 2028 (clean, no losses beyond 2027's):", r(dict(B, stakes=[75, 2, 2], charge=[0, 0, 0], exitliab=0, pe=17)))
print("Funding book at 25% / at book:", r(dict(B, sf=.25, sfg=[.75, .5, .25])), "/", r(dict(B, sf=1, sfg=[1, 1, 1])))
x = m.build(B, P)
st_exit = B['sf'] * x['ST'][-1]; liab = B['exitliab'] / m.SH; core_exit = B['pe'] * B['eps30']
print(f"Bridge: core 145.52 -> EPS -17.40 -> 128.12 -> multiple to 15 {core_exit - 128.12:+.2f} -> core {core_exit:.2f}; net cash 0.99 -> {x['NC'][-1]:.2f}; "
      f"stakes 4.45 -> {st_exit:.2f} (book {x['ST'][-1]:.2f}); exit liability -{liab:.2f}; VT {x['VT']:.2f}; sumD {sum(x['D']):.2f}; total {x['VT']+sum(x['D']):.2f}")
print("Stakes book $bn", [round(v_*m.SH, 1) for v_ in x['ST']], "D $bn", [round(d*m.SH, 1) for d in x['D'][2:]])
