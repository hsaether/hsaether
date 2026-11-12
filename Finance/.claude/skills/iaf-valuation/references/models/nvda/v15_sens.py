# NVIDIA (docs/nvda-analysis.md) -- v1.5 attribution v1.4 -> v1.5, sensitivities (a)-(d), driver breakdown,
# return bridge and exit cross-check. 12 Nov 2026. Run from this folder: py v15_sens.py [price]
import sys
from datetime import date
import v15 as m

P = float(sys.argv[1]) if len(sys.argv) > 1 else 165.82
pct = lambda x: f"{x*100:.1f}%"
OLD_B = dict(m.BASE, eps=[13.99, 14.91, 15.21], eps30=14.75, remark=0.0)
OLD_R = dict(m.BEAR, charge=[0, 5, 10], exitliab=0.0, remark=0.0)
OLD_U = dict(m.BULL, remark=0.0)


def row(label, B, R, U, P, **kw):
    b = m.build(B, P, **kw); r = m.build(R, P, **kw); u = m.build(U, P, **kw)
    print(f"{label}: Base {pct(b['irr'])} / ${b['pk']:.1f} / {b['pk']/P-1:+.1%} | Bear {pct(r['irr'])} (${r['pk']:.1f}) | Bull {pct(u['irr'])} (${u['pk']:.1f})")


print("== Attribution ==")
row("v1.4 (173.73, 11 Nov, 50 days)", OLD_B, OLD_R, OLD_U, 173.73, vdate=date(2026, 11, 11), stub_days=50)
row("1 date 12 Nov, 49 days", OLD_B, OLD_R, OLD_U, 173.73)
NEWB_paths = dict(OLD_B, eps=m.BASE['eps'], eps30=m.BASE['eps30'])
row("2 AI BBB 11 Nov Base path", NEWB_paths, OLD_R, OLD_U, 173.73)
row("3 price 165.82", NEWB_paths, OLD_R, OLD_U, P)
row("4a stakes public re-mark -6.5bn", dict(NEWB_paths, remark=m.REMARK), dict(OLD_R, remark=m.REMARK), dict(OLD_U, remark=m.REMARK), P)
row("4b Bear cross-funding rebuild (= v1.5)", m.BASE, m.BEAR, m.BULL, P)

print("== Sensitivities (Base unless stated) ==")
base = m.build(m.BASE, P)


def show(label, s, **kw):
    r = m.build(s, P, **kw)
    print(f"{label}: {pct(r['irr'])} P_k ${r['pk']:.1f} margin {r['pk']/P-1:+.1%} VT {r['VT']:.1f} 2030 EPS {r['s']['eps30']:.2f}")
    return r


show("Model", m.BASE)
# (a) stop to new discretionary funding
a_c = m.apply_loss(m.BASE, [5/610.2, 10/609.0, 10/594.3, 10/594.3]); a_c['stakes'] = [16.9, 0, 0]
show("(a) central: lost 5/10/10/10bn revenue (direct support not replaced), no new stakes", a_c)
a_w = m.apply_loss(m.BASE, [0.039, 0.078, 0.078, 0.078]); a_w['stakes'] = [16.9, 0, 0]
show("(a) wide: non-K1 -10% 2027, -20% persistent 2028+ (NVIDIA rev -3.9% / -7.8%)", a_w)
# (b) full closure of diversion channels
b_c = m.apply_loss(m.BASE, [0.015, 0.03, 0.03, 0.03])
show("(b) central: rev -1.5% 2027 (backfill), -3% 2028+", b_c)
b_w = m.apply_loss(m.BASE, [0.06, 0.06, 0.06, 0.06], extra_charge=[5, 0, 0])
show("(b) wide: rev -6% from 2027, 5bn penalty 2027", b_w)
for L in [0.10, 0.15, 0.20]:
    show(f"(b) loss {L:.0%} from 2027", m.apply_loss(m.BASE, [L] * 4))
Lk = m.solve(lambda x: m.build(m.apply_loss(m.BASE, [x] * 4), P)['irr'], 0.12, 0, 0.5)
Lf = m.solve(lambda x: m.build(m.apply_loss(m.BASE, [x] * 4), P)['pk'] / P - 1, -0.02, 0, 0.5)
print(f"(b) revenue loss for k: {Lk:.1%}; for fails (-2%): {Lf:.1%}")
# (c) CEO de-rating
for pe in [16, 15, 13, 12.75]:
    show(f"(c) exit {pe}", m.BASE, pe=pe)
c_x = dict(m.BASE, pe=15, eps=[m.BASE['eps'][0], m.BASE['eps'][1], m.BASE['eps'][2] * 0.95], eps30=m.BASE['eps30'] * 0.95)
show("(c) exit 15 and 2029-30 EPS x0.95 (customer hedging)", c_x)
ek = m.solve(lambda x: m.build(m.BASE, P, pe=x)['irr'], 0.12, 5, 25)
print(f"(c) exit P/E for k: {ek:.2f}")
for pe in [15, 13]:
    print(f"   price at which exit {pe} = k: {m.build(m.BASE, None, pe=pe)['pk']:.1f}")
# (d) all three
d_c = m.apply_loss(m.BASE, [5/610.2 + 0.015, 10/609.0 + 0.03, 10/594.3 + 0.03, 10/594.3 + 0.03]); d_c['stakes'] = [16.9, 0, 0]
show("(d) central: (a)+(b) central + exit 15", d_c, pe=15)
d_w = m.apply_loss(m.BASE, [0.039 + 0.06, 0.078 + 0.06, 0.078 + 0.06, 0.078 + 0.06], extra_charge=[5, 0, 0]); d_w['stakes'] = [16.9, 0, 0]
show("(d) wide: (a)+(b) wide + exit 13", d_w, pe=13)
print(f"   (d) central k-price {m.build(d_c, None, pe=15)['pk']:.1f}; wide k-price {m.build(d_w, None, pe=13)['pk']:.1f}")
# Other sensitivities
show("Exit -2 (15)", m.BASE, pe=15); show("Exit +2 (19)", m.BASE, pe=19)
for n, s in [('Bear', m.BEAR), ('Bull', m.BULL)]:
    for d in [-2, 2]:
        r = m.build(s, P, pe=s['pe'] + d); print(f"  {n} exit {s['pe']+d}: {pct(r['irr'])}")
show("Exit at today's core P/E (no re-rating)", m.BASE, pe=(P - base['nc0'] - base['st0']) / m.BASE['eps'][0])
r = m.build(m.BEAR, P, pe=(P - base['nc0'] - base['st0']) / m.BASE['eps'][0]); print("  Bear at today's core", pct(r['irr']))
r = m.build(m.BULL, P, pe=(P - base['nc0'] - base['st0']) / m.BASE['eps'][0]); print("  Bull at today's core", pct(r['irr']))
show("2030 EPS x0.9", m.BASE, eps30=m.BASE['eps30'] * 0.9); show("2030 EPS x1.1", m.BASE, eps30=m.BASE['eps30'] * 1.1)
for n, s in [('Bear', m.BEAR), ('Bull', m.BULL)]:
    print(f"  {n} 2030x0.9 {pct(m.build(s,P,eps30=s['eps30']*0.9)['irr'])} x1.1 {pct(m.build(s,P,eps30=s['eps30']*1.1)['irr'])}")
show("Stakes at book (no re-mark)", m.BASE, remark=0.0)
show("Stakes worth zero at exit", m.BASE, sf=0.0)
for n, s in [('Bear', m.BEAR), ('Bull', m.BULL)]:
    print(f"  {n} stakes zero {pct(m.build(s,P,sf=0.0)['irr'])}")
show("Payout 100%", m.BASE, payout=1.0); show("Payout 30%", m.BASE, payout=0.3)
print(f"  Bear payout 100/30: {pct(m.build(m.BEAR,P,payout=1.0)['irr'])} / {pct(m.build(m.BEAR,P,payout=0.3)['irr'])}; Bull {pct(m.build(m.BULL,P,payout=1.0)['irr'])} / {pct(m.build(m.BULL,P,payout=0.3)['irr'])}")
print(f"Bear: v1.4 cross-funding (charge 15, no exit liability): {pct(m.build(m.BEAR,P,charge=[0,5,10],exitliab=0.0)['irr'])}; "
      f"charges x2 and stakes 25%: {pct(m.build(m.BEAR,P,charge=[4,15,21],exitliab=40.0,sf=0.25)['irr'])}; "
      f"no charges, stakes at book: {pct(m.build(m.BEAR,P,charge=[0,0,0],exitliab=0.0,sf=1.0)['irr'])}")
show("Version 1 basis FY Jan-28 = CY27 (15.91)", m.BASE, eps=[e * 15.91 / 15.21 for e in m.BASE['eps']], eps30=m.BASE['eps30'] * 15.91 / 15.21)
mg = dict(m.BASE, eps=[15.21, 15.21 * 1.065, 15.21 * 1.087], eps30=15.21 * 1.054)
show("Management FY28 ~+70% then digestion (1.00/1.065/1.087/1.054)", mg)
show("Previous AI BBB Base path (.92/.98/1.00/.97)", m.BASE, eps=[13.99, 14.91, 15.21], eps30=14.75)

print("== Driver breakdown ==")
for n, s in [('Bear', m.BEAR), ('Bull', m.BULL)]:
    step1 = dict(m.BASE, eps=s['eps'], eps30=s['eps30'], rev=s['rev'], margin=s['margin'], capex=s['capex'])
    step2 = dict(step1, pe=s['pe'])
    step3 = dict(step2, sf=s['sf'], sfg=s['sfg'])
    step4 = dict(step3, charge=s['charge'], exitliab=s['exitliab'])
    out = [m.build(x, P)['irr'] for x in [m.BASE, step1, step2, step3, step4]]
    pks = [m.build(x, P)['pk'] for x in [m.BASE, step1, step2, step3, step4]]
    print(n, [pct(x) for x in out], [round(x, 1) for x in pks])

print("== Base return bridge ==")
b = base; s = m.BASE
core = P - b['nc0'] - b['st0']; pe0 = core / s['eps'][0]
e_growth = pe0 * s['eps30'] - core
rerate = (s['pe'] - pe0) * s['eps30']
print(f"P {P} = core {core:.2f} + net cash {b['nc0']:.2f} + stakes {b['st0']:.2f}; core P/E {pe0:.2f}")
print(f"EPS 2027->2030 at today's multiple {e_growth:+.2f}; multiple to 17 {rerate:+.2f}; net cash change {b['NC'][-1]-b['nc0']:+.2f} "
      f"(exit {b['NC'][-1]:.2f}); stakes change {b['ST'][-1]-b['st0']:+.2f} (exit {b['ST'][-1]:.2f}); VT {b['VT']:.2f}; sumD {sum(b['D']):.2f}; total {sum(b['D'])+b['VT']-P:+.2f}")

print("== Exit cross-check (book equity) ==")
for n, sc in [('Bear', m.BEAR), ('Base', m.BASE), ('Bull', m.BULL)]:
    r = m.build(sc, P)
    book = 295 + m.REMARK + sum(r['NI']) - sum(r['D'][1:]) * m.SH - sum(sc['charge']) - sc['exitliab'] + 3 * 8
    if sc['sf'] < 1:
        book -= (1 - sc['sf']) * r['ST'][-1] * m.SH
    bps = book / m.SH
    roe = sc['eps30'] * m.SH / book
    conv = r['FCF'][2] / r['NI'][2]
    print(f"{n}: book {book:.0f} / {bps:.1f}; exit P/B {r['VT']/bps:.1f}; ROE {roe:.0%}; all-in exit P/E {r['VT']/sc['eps30']:.1f}; "
          f"conv 2029 {conv:.2f}; cash yield {conv/sc['pe']:.1%}")
