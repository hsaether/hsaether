# NVIDIA (docs/nvda-analysis.md) -- v1.5 outputs, 12 Nov 2026. Run from this folder: py v15_run.py [price]
# Prints every decision figure, table and sensitivity used in the document.
import sys
from datetime import date
import v15 as m

P = float(sys.argv[1]) if len(sys.argv) > 1 else 165.82
S = {'Bear': m.BEAR, 'Base': m.BASE, 'Bull': m.BULL}
pct = lambda x: f"{x*100:.1f}%"


def res(s, P=P, **ov):
    return m.build(s, P, **ov)


print(f"P = {P}")
R = {n: res(s) for n, s in S.items()}
for n, r in R.items():
    T = r['T']; s = r['s']
    sumD = sum(r['D']); d = sumD / T / P; g = (r['VT'] / P) ** (1 / T) - 1; c = r['irr'] - d - g
    print(f"{n}: IRR {pct(r['irr'])} NOK {pct(m.nok_irr(r, n, P))} Pk {r['pk']:.1f} MoS {r['pk']/P-1:+.1%} VT {r['VT']:.1f} "
          f"sumD {sumD:.2f} D {[round(x,2) for x in r['D']]} cap {(sumD+r['VT'])/P-1:+.1%} d/g/c {d*100:.1f}/{g*100:.1f}/{c*100:+.1f}")
    print(f"   NC/sh {[round(x,2) for x in r['NC']]} ST/sh {[round(x,2) for x in r['ST']]} FCF {[round(x,1) for x in r['FCF']]} "
          f"FCF/sh {[round(x/m.SH,2) for x in r['FCF']]} NI {[round(x,1) for x in r['NI']]} REV {[round(x,1) for x in r['REV']]} "
          f"EPS {[round(x,2) for x in s['eps']]} eps30 {s['eps30']:.2f} cumFCF/sh {sum(r['FCF'])/m.SH:.1f} nc0 {r['nc0']:.3f} st0 {r['st0']:.3f} T {T:.3f}")
    V26, V = m.interim(r, n, P)
    path = [V26] + V + [r['VT']]
    Ds = r['D']
    rts = [(Ds[i + 1] + path[i + 1]) / path[i] - 1 for i in range(3)]
    stub_r = (Ds[0] + V26) / P - 1
    # IRR to each year-end
    irr_to = []
    for j in range(3):
        cf = [(0, -P)] + r['cf'][:j + 2]
        cf[-1] = (cf[-1][0], cf[-1][1])
        tY = (date(2027 + j, 12, 31) - m.VDATE).days / 365.25
        cf2 = [(0, -P)] + r['cf'][:j + 2] + [(tY, path[j + 1])]
        irr_to.append(m.irr(cf2))
    nokf = m.NOKF[n]
    rt_nok = [(Ds[1] + path[1]) * nokf[1] / path[0] - 1,
              (Ds[2] + path[2]) * nokf[2] / (path[1] * nokf[1]) - 1,
              (Ds[3] + path[3]) * nokf[3] / (path[2] * nokf[2]) - 1]
    ebitda = [ni / 0.83 + da for ni, da in zip(r['NI'], s['da'])]
    print(f"   V_t {[round(x,1) for x in path]} r_t {[pct(x) for x in rts]} stub {pct(stub_r)} IRR-to {[pct(x) for x in irr_to]} "
          f"r_t NOK {[pct(x) for x in rt_nok]} EBITDA {[round(x) for x in ebitda]} EBITDA/sh {[round(x/m.SH,1) for x in ebitda]}")
    # P/E glide
    core0 = (P - r['nc0'] - r['st0']) / m.BASE['eps'][0]
    print(f"   core0 P/E on Base27 {core0:.2f}; core P/E on 2030 EPS {(P - r['nc0'] - r['st0'])/s['eps30']:.2f}")

rb, rr, ru = R['Base'], R['Bear'], R['Bull']
# structural
print("Structural:")
for n, s in S.items():
    e30 = s['eps30']; rv = m.base_rev(s)[2]
    st = res(s, eps=[e30] * 3, rev=[rv] * 3)
    print(f"  {n}: structural {pct(st['irr'])} cyclical {(R[n]['irr']-st['irr'])*100:+.1f} pp; "
          f"dD {(sum(R[n]['D'])-sum(st['D']))/R[n]['T']/P*100:+.1f} dg {(((R[n]['VT']/P)**(1/R[n]['T'])-1)-((st['VT']/P)**(1/st['T'])-1))*100:+.1f}")
# E/R and triggers
E, r27b, r27r = m.er(P)
print(f"E/R {E:.3f} (Base r27 {pct(r27b)}, Bear r27 NOK {pct(r27r)})")
pkb = rb['pk']
print(f"Triggers: clears <= {pkb/1.02:.1f}; P_k {pkb:.1f}; fails >= {pkb/0.98:.1f}; Bull Pk {ru['pk']:.1f}; Bear Pk {rr['pk']:.1f}")
pe = m.solve(lambda x: m.er(x)[0], 0.254, 120, 260)
print(f"E/R = 0.254 at {pe:.1f}")
p72 = m.solve(lambda x: m.build(m.BASE, x)['irr'], 0.072, 150, 400)
print(f"Base = 7.2% at {p72:.1f}")
# exit P/E for k
ek = m.solve(lambda x: m.build(m.BASE, P, pe=x)['irr'], 0.12, 5, 25)
print(f"Exit P/E for k at P: {ek:.2f}")
# implied multiplier
def mult(x, pe=17):
    b = m.BASE
    return m.build(dict(b, eps=[b['eps'][0], b['eps'][1] * x, b['eps'][2] * x], eps30=b['eps30'] * x, pe=pe), P)['irr']
for pe_ in [17, 13, 15, 19]:
    mk = m.solve(lambda x: mult(x, pe_), 0.12, 0.3, 2.0)
    m0 = m.solve(lambda x: mult(x, pe_), 0.0, 0.1, 2.0) if pe_ == 17 else None
    print(f"  exit {pe_}: k at m={mk:.3f} ({[round(v*mk/m.CY27,2) for v in m.BASE['eps'][1:]]+[round(m.BASE['eps30']*mk/m.CY27,2)]})" + (f"; 0% at m={m0:.3f}" if m0 else ""))
bearpath = m.build(dict(m.BASE, eps=m.BEAR['eps'], eps30=m.BEAR['eps30'], rev=m.BEAR['rev']), P)
print(f"AI BBB Bear path at Base exit, stakes, margins: {pct(bearpath['irr'])}")
# scenario weighted
cfw = [(t, .25 * a + .5 * b + .25 * c) for (t, a), (_, b), (_, c) in zip(rr['cf'], rb['cf'], ru['cf'])]
print(f"Scenario-weighted 25/50/25 on levels: {pct(m.irr([(0,-P)]+cfw))}")
print(f"Share of Bull priced: {(P-pkb)/(ru['pk']-pkb):+.1%}")
print(f"Rule 3: P/FCF_norm {P/m.BASE['eps30']:.1f}x vs ceiling {rb['irr']/0.0144:.1f}x; Bear {P/m.BEAR['eps30']:.1f} vs n/m; Bull {P/m.BULL['eps30']:.1f} vs {ru['irr']/0.0144:.1f}")
print(f"At 11 Nov close 173.73: Base {pct(m.build(m.BASE,173.73)['irr'])}; Bear {pct(m.build(m.BEAR,173.73)['irr'])}; Bull {pct(m.build(m.BULL,173.73)['irr'])}")
