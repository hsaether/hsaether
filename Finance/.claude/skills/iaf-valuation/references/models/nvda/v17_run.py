# NVIDIA (docs/nvda-analysis.md) -- v1.7 outputs, 18 Nov 2026 (price = 17 Nov close $155.46).
# Run from this folder: py v17_run.py [price]. Prints every decision figure, table, sensitivity, the driver
# breakdown, the Base return bridge, the exit cross-check and the attribution v1.6 -> v1.7.
import sys
from datetime import date
import v17 as m
import v15

P = float(sys.argv[1]) if len(sys.argv) > 1 else 155.46
S = {'Bear': m.BEAR, 'Base': m.BASE, 'Bull': m.BULL}
pct = lambda x: f"{x*100:.1f}%"
B = m.BASE


def res(s, P=P, **ov):
    return m.build(s, P, **ov)


print(f"P = {P}; T {m.build(B, P)['T']:.3f}")
R = {n: res(s) for n, s in S.items()}
for n, r in R.items():
    T = r['T']; s = r['s']
    sumD = sum(r['D']); d = sumD / T / P; g = (r['VT'] / P) ** (1 / T) - 1; c = r['irr'] - d - g
    print(f"{n}: IRR {pct(r['irr'])} NOK {pct(m.nok_irr(r, n, P))} Pk {r['pk']:.1f} MoS {r['pk']/P-1:+.1%} VT {r['VT']:.1f} "
          f"sumD {sumD:.2f} Dyear {[round(x,2) for x in m.Dyear(r)]} cap {(sumD+r['VT'])/P-1:+.1%} d/g/c {d*100:.1f}/{g*100:.1f}/{c*100:+.1f}")
    print(f"   NC/sh {[round(x,2) for x in r['NC']]} NC $bn {[round(x*m.SH,1) for x in r['NC']]} ST/sh {[round(x,2) for x in r['ST']]} "
          f"FCF {[round(x,1) for x in r['FCF']]} FCF/sh {[round(x/m.SH,2) for x in r['FCF']]} NI {[round(x,1) for x in r['NI']]} "
          f"REV {[round(x,1) for x in r['REV']]} EPS {[round(x,2) for x in s['eps']]} eps30 {s['eps30']:.2f} cumFCF/sh {sum(r['FCF'])/m.SH:.1f} "
          f"nc0 {r['nc0']:.3f} st0 {r['st0']:.3f}")
    V26, V = m.interim(r, n, P)
    path = [V26] + V + [r['VT']]
    Dy = m.Dyear(r)
    rts = [(Dy[i + 1] + path[i + 1]) / path[i] - 1 for i in range(3)]
    stub_r = (Dy[0] + V26) / P - 1
    irr_to = []
    for j in range(3):
        tY = (date(2027 + j, 12, 31) - m.VDATE).days / 365.25
        cf2 = [(0, -P)] + r['cf'][:j + 3] + [(tY, path[j + 1])]
        irr_to.append(m.irr(cf2))
    nokf = m.NOKF[n]
    rt_nok = [(Dy[1] + path[1]) * nokf[1] / path[0] - 1,
              (Dy[2] + path[2]) * nokf[2] / (path[1] * nokf[1]) - 1,
              (Dy[3] + path[3]) * nokf[3] / (path[2] * nokf[2]) - 1]
    ebitda = [ni / (1 - m.TAX) + da for ni, da in zip(r['NI'], s['da'])]
    print(f"   V_t {[round(x,1) for x in path]} r_t {[pct(x) for x in rts]} stub {pct(stub_r)} IRR-to {[pct(x) for x in irr_to]} "
          f"r_t NOK {[pct(x) for x in rt_nok]} EBITDA {[round(x) for x in ebitda]} EBITDA/sh {[round(x/m.SH,1) for x in ebitda]}")
    core0 = (P - r['nc0'] - r['st0']) / B['eps'][0]
    print(f"   core0 P/E on Base27 {core0:.2f}; core P/E on 2030 EPS {(P - r['nc0'] - r['st0'])/s['eps30']:.2f}; "
          f"growth spend {[round(s['capex'][i]-s['da'][i] + s['stakes'][i],1) for i in range(3)]}")

rb, rr, ru = R['Base'], R['Bear'], R['Bull']
print(f"Stub: EPS {m.STUB_EPS:.2f} rev {130*44/98:.1f} FCF {m.STUB_FCF:.1f} ({m.STUB_FCF/m.SH:.2f}/sh) D {m.STUB_BB+m.STUB_DIV:.1f} "
      f"({(m.STUB_BB+m.STUB_DIV)/m.SH:.2f}/sh; div {m.STUB_DIV/m.SH:.2f}) NC0 {m.NC0:.1f} ({m.NC0/m.SH:.2f}) NC26 {m.NC26:.1f} ({m.NC26/m.SH:.2f}) "
      f"ST0 {m.ST0:.1f} ({m.ST0/m.SH:.2f}) ST26 {m.ST26:.1f} ({m.ST26/m.SH:.2f}); Q4 EPS {m.Q4_EPS:.2f}")
print("Structural:")
for n, s in S.items():
    e30 = s['eps30']; rv = m.base_rev(s)[2]
    st = res(s, eps=[e30] * 3, rev=[rv] * 3)
    print(f"  {n}: structural {pct(st['irr'])} cyclical {(R[n]['irr']-st['irr'])*100:+.1f} pp; "
          f"dD {(sum(R[n]['D'])-sum(st['D']))/R[n]['T']/P*100:+.1f} dg {(((R[n]['VT']/P)**(1/R[n]['T'])-1)-((st['VT']/P)**(1/st['T'])-1))*100:+.1f}")
E, r27b, r27r = m.er(P)
print(f"E/R {E:.3f} (Base r27 {pct(r27b)}, Bear r27 NOK {pct(r27r)}; Base NOK {pct(m.nok_irr(rb,'Base',P))})")
pkb = rb['pk']
print(f"Triggers: clears <= {pkb/1.02:.1f}; P_k {pkb:.1f}; fails >= {pkb/0.98:.1f}; Bull Pk {ru['pk']:.1f}; Bear Pk {rr['pk']:.1f}")
print(f"E/R = 0.254 at {m.solve(lambda x: m.er(x)[0], 0.254, 120, 260):.1f}; Base = 7.2% at {m.solve(lambda x: m.build(B, x)['irr'], 0.072, 150, 400):.1f}")
ek = m.solve(lambda x: m.build(B, P, pe=x)['irr'], 0.12, 5, 25)
print(f"Exit P/E for k at P: {ek:.2f}")


def mult(x, pe=17):
    return m.build(dict(B, eps=[B['eps'][0], B['eps'][1] * x, B['eps'][2] * x], eps30=B['eps30'] * x, pe=pe), P)['irr']


for pe_ in [17, 13, 15, 19]:
    mk = m.solve(lambda x: mult(x, pe_), 0.12, 0.3, 2.0)
    m0 = m.solve(lambda x: mult(x, pe_), 0.0, 0.1, 2.0) if pe_ == 17 else None
    print(f"  exit {pe_}: k at m={mk:.3f} ({[round(v*mk/m.CY27,2) for v in B['eps'][1:]]+[round(B['eps30']*mk/m.CY27,2)]})" + (f"; 0% at m={m0:.3f}" if m0 else ""))
bearpath = m.build(dict(B, eps=m.BEAR['eps'], eps30=m.BEAR['eps30'], rev=m.BEAR['rev']), P)
print(f"AI BBB Bear path at Base exit, stakes, costs: {pct(bearpath['irr'])}")
# management FY28 ~+75% (FY27 423.7 -> 741.5), GM 72.5%, opex 46; then the AI BBB digestion ratios
mg27 = (423.7 * 1.75 * 0.725 - 46) * (1 - m.TAX) / m.SH
mgx = [mg27, mg27 * .91 / .92, mg27 * .88 / .92]
mg = dict(B, eps=mgx, eps30=mg27 * .87 / .92)
r = m.build(mg, P)
print(f"Management FY28 +75% then AI BBB digestion: EPS {[round(x,2) for x in mgx]} ({[round(x/m.CY27,3) for x in mgx]+[round(mg['eps30']/m.CY27,3)]}) "
      f"rev {[round(x) for x in m.base_rev(mg)]}: {pct(r['irr'])} P_k {r['pk']:.1f}")
cfw = [(t, .25 * a + .5 * b + .25 * c) for (t, a), (_, b), (_, c) in zip(rr['cf'], rb['cf'], ru['cf'])]
print(f"Scenario-weighted 25/50/25 on levels: {pct(m.irr([(0,-P)]+cfw))}; share of Bull priced {(P-pkb)/(ru['pk']-pkb):+.1%}")
print(f"Rule 3: P/FCF_norm {P/B['eps30']:.1f}x vs ceiling {rb['irr']/0.0144:.1f}x; Bear {P/m.BEAR['eps30']:.1f}; Bull {P/m.BULL['eps30']:.1f} vs {ru['irr']/0.0144:.1f}")
print(f"After-hours ~162.0: Base {pct(m.build(B,162.0)['irr'])} MoS {pkb/162.0-1:+.1%}; Bear {pct(m.build(m.BEAR,162.0)['irr'])}; Bull {pct(m.build(m.BULL,162.0)['irr'])}")

print("== Sensitivities ==")


def show(label, s, **kw):
    r = m.build(s, P, **kw)
    print(f"{label}: {pct(r['irr'])} P_k ${r['pk']:.1f} margin {r['pk']/P-1:+.1%} VT {r['VT']:.1f}")
    return r


R0 = m.base_rev(B)
a_c = m.apply_loss(B, [5 / R0[0], 10 / R0[1], 10 / R0[2], 10 / R0[2]]); a_c['stakes'] = [B['stakes'][0], 0, 0]
show("(a) central: lost 5/10/10/10bn revenue, no new stakes", a_c)
a_w = m.apply_loss(B, [0.039, 0.078, 0.078, 0.078]); a_w['stakes'] = [B['stakes'][0], 0, 0]
show("(a) wide", a_w)
b_c = m.apply_loss(B, [0.015, 0.03, 0.03, 0.03]); show("(b) central", b_c)
b_w = m.apply_loss(B, [0.06] * 4, extra_charge=[5, 0, 0]); show("(b) wide", b_w)
Lk = m.solve(lambda x: m.build(m.apply_loss(B, [x] * 4), P)['irr'], 0.12, 0, 0.5)
Lf = m.solve(lambda x: m.build(m.apply_loss(B, [x] * 4), P)['pk'] / P - 1, -0.02, 0, 0.5)
print(f"(b) revenue loss for k: {Lk:.1%}; for fails (-2%): {Lf:.1%}")
for pe in [16, 15, 13]:
    show(f"(c) exit {pe}", B, pe=pe)
c_x = dict(B, pe=15, eps=[B['eps'][0], B['eps'][1], B['eps'][2] * 0.95], eps30=B['eps30'] * 0.95)
show("(c) exit 15 and 2029-30 EPS x0.95", c_x)
for pe in [15, 13]:
    print(f"   price at which exit {pe} = k: {m.build(B, None, pe=pe)['pk']:.1f}")
d_c = m.apply_loss(B, [5 / R0[0] + 0.015, 10 / R0[1] + 0.03, 10 / R0[2] + 0.03, 10 / R0[2] + 0.03]); d_c['stakes'] = [B['stakes'][0], 0, 0]
r = show("(d) central + exit 15", d_c, pe=15)
d_w = m.apply_loss(B, [0.039 + 0.06, 0.078 + 0.06, 0.078 + 0.06, 0.078 + 0.06], extra_charge=[5, 0, 0]); d_w['stakes'] = [B['stakes'][0], 0, 0]
show("(d) wide + exit 13", d_w, pe=13)
print(f"   (d) central k-price {m.build(d_c, None, pe=15)['pk']:.1f}; wide {m.build(d_w, None, pe=13)['pk']:.1f}")
for n, s in S.items():
    print(f"  {n} exit -2 / +2: {pct(m.build(s,P,pe=s['pe']-2)['irr'])} / {pct(m.build(s,P,pe=s['pe']+2)['irr'])}; "
          f"2030 x0.9 / x1.1: {pct(m.build(s,P,eps30=s['eps30']*0.9)['irr'])} / {pct(m.build(s,P,eps30=s['eps30']*1.1)['irr'])}; "
          f"payout 100% / 60%: {pct(m.build(s,P,payout=1.0)['irr'])} / {pct(m.build(s,P,payout=0.6)['irr'])}; stakes zero {pct(m.build(s,P,sf=0.0)['irr'])}")
core = (P - rb['nc0'] - rb['st0']) / B['eps'][0]
for n, s in S.items():
    print(f"  {n} exit at today's core {core:.2f}: {pct(m.build(s,P,pe=core)['irr'])}" + (f" P_k {m.build(s,P,pe=core)['pk']:.1f}" if n == 'Base' else ''))
print(f"  Bear costs: none, stakes at book {pct(m.build(m.BEAR,P,charge=[0,0,0],exitliab=0.0,sf=1.0)['irr'])}; doubled, stakes 25% "
      f"{pct(m.build(m.BEAR,P,charge=[3.6,22.2,22.2],exitliab=44.4,sf=0.25)['irr'])}; all 74 leases at risk "
      f"{pct(m.build(m.BEAR,P,charge=[1.8,12.1,12.6],exitliab=22.2+10.2)['irr'])}")
show("Base GM 75% basis (v1.6 revenue)", B, rev=[B['eps'][i] * m.SH / [.555, .55, .545][i] for i in range(3)])
show("Payout 60% (v1.6)", B, payout=0.6)

print("== Driver breakdown ==")
for n, s in [('Bear', m.BEAR), ('Bull', m.BULL)]:
    st1 = dict(B, eps=s['eps'], eps30=s['eps30'], rev=s['rev'], capex=s['capex'])
    st2 = dict(st1, pe=s['pe'])
    st3 = dict(st2, sf=s['sf'], sfg=s['sfg'])
    st4 = dict(st3, charge=s['charge'], exitliab=s['exitliab'])
    xs = [B, st1, st2, st3, st4]
    print(n, [pct(m.build(x, P)['irr']) for x in xs], [round(m.build(x, P)['pk'], 1) for x in xs])

print("== Base return bridge ==")
b = rb; s = B
core = P - b['nc0'] - b['st0']; pe0 = core / s['eps'][0]
print(f"P {P} = core {core:.2f} + net cash {b['nc0']:.2f} + stakes {b['st0']:.2f}; core P/E {pe0:.2f}")
print(f"EPS 2027->2030 at today's multiple {pe0*s['eps30']-core:+.2f}; multiple to 17 {(s['pe']-pe0)*s['eps30']:+.2f}; "
      f"net cash {b['nc0']:.2f} -> {b['NC'][-1]:.2f} ({b['NC'][-1]-b['nc0']:+.2f}); stakes {b['st0']:.2f} -> {b['ST'][-1]:.2f} ({b['ST'][-1]-b['st0']:+.2f}); "
      f"sumD {sum(b['D']):.2f}; VT {b['VT']:.2f}; total {sum(b['D'])+b['VT']:.2f}; core at exit {s['pe']*s['eps30']:.1f}")

print("== Exit cross-check (book equity) ==")
BOOK26 = 282.0   # 31 Dec 2026 [A]: 266.7 (25 Oct [F]) + NI 46.8 - buybacks 20.5 - dividend 6.05 - re-mark 6.15 + SBC 1.5
for n, sc in S.items():
    r = R[n]
    book = BOOK26 + sum(r['NI']) - sum(r['D'][2:]) * m.SH - sum(sc['charge']) - sc['exitliab'] + 3 * 8
    if sc['sf'] < 1:
        book -= (1 - sc['sf']) * r['ST'][-1] * m.SH
    bps = book / m.SH
    conv = r['FCF'][2] / r['NI'][2]
    print(f"{n}: book {book:.0f} / {bps:.1f}; exit P/B {r['VT']/bps:.1f}; ROE {sc['eps30']*m.SH/book:.0%}; all-in P/E {r['VT']/sc['eps30']:.1f}; "
          f"conv 2029 {conv:.2f}; cash yield {conv/sc['pe']:.1%}")

print("== Attribution v1.6 -> v1.7 ==")
o = v15.build(v15.BASE, 166.19); print(f"v1.6 at 166.19: {pct(o['irr'])} P_k {o['pk']:.1f}")
o = v15.build(v15.BASE, P); print(f"1 price 155.46 on the v1.6 model: {pct(o['irr'])} P_k {o['pk']:.1f}")
step2 = dict(B, payout=0.6, capex=[13, 15, 17], da=[6.5, 9, 11], stakes=[16.9, 2, 2],
             rev=[B['eps'][i] * m.SH / [.555, .55, .545][i] for i in range(3)])
o = m.build(step2, P); print(f"2 date 17 Nov, stub from the Q3 balance sheet, stakes re-marked: {pct(o['irr'])} P_k {o['pk']:.1f}")
step3 = dict(step2, rev=None); o = m.build(step3, P); print(f"3 revenue on GM 72.5% (working capital): {pct(o['irr'])} P_k {o['pk']:.1f}")
step4 = dict(step3, capex=B['capex'], da=B['da'], stakes=B['stakes']); o = m.build(step4, P); print(f"4 capex, D&A, stakes: {pct(o['irr'])} P_k {o['pk']:.1f}")
o = m.build(B, P); print(f"5 payout 80%: {pct(o['irr'])} P_k {o['pk']:.1f}")
o = v15.build(v15.BEAR, P); print(f"Bear v1.6 at P: {pct(o['irr'])}; v1.7 {pct(rr['irr'])}; Bull v1.6 at P {pct(v15.build(v15.BULL, P)['irr'])}; v1.7 {pct(ru['irr'])}")
