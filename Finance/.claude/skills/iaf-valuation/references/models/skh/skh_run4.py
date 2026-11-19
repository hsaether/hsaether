# SK hynix (docs/skhynix-analysis.md) -- version 4 outputs, 19 Nov 2026 (skh_run.py = v3).
# Run from this folder: py skh_run.py   (attribution v2 -> v3, decision figures, tables, sensitivities, ADR)
from datetime import date
import skh_model as m

I = dict(m.V4)
S = ['Bear', 'Base', 'Bull']
pct = lambda x: f"{x*100:.1f}%"
K = lambda x: f"{x:,.0f}"
FX = 1329.32            # USD/KRW, Yahoo 19 Nov 06:54 UTC
ADR = 122.47            # SKHY, Nasdaq close 18 Nov (Yahoo)
ADR13 = 122.47
PREM_BULL = ADR * 10 * FX / I['P'] - 1     # held at today's premium in Bull
PREM = dict(Bear=0.0, Base=0.15, Bull=PREM_BULL)


def R(s, I=I, **ov):
    return m.res(s, I, **ov)


def mos(r, P=None):
    return r['pk'] / (r['P'] if P is None else P) - 1


def line(tag, I, **ov):
    out = [tag]
    for s in S:
        r = R(s, I, **ov)
        out.append(f"{pct(r['irr'])} / {K(r['pk'])} / {mos(r):+.1%}")
    return " | ".join(out)


print("== Attribution v3 -> v4 (Bear | Base | Bull: IRR / P_k / margin)")
V3 = dict(m.V3)
print(line("v3 (1,120,000; 16 Nov)", V3))
A1 = dict(V3, P=1173000.0, vdate=date(2026, 11, 19), kio_px=I['kio_px'], jpykrw=I['jpykrw'])
print(line("price, date, Kioxia mark (v3 path)", A1))
print(line("+ AI BBB 18 Nov H2 Base path and index (= v4)", I))

print("\n== Bridge v4")
br = m.bridge(I)
sh = I['sh'] / 1e6
for k_, v in br.items():
    print(k_, round(v, 3))
print("nc_v/sh", K(br['nc_v'] / sh), "nc_e/sh", K(br['nc_e'] / sh), "kio tn", round(m.kio(I), 2), "kio/sh", K(m.kio(I) / sh),
      "T", round(m.yf(m.EXIT, I['vdate']), 3), "stub days", (date(2026, 12, 31) - I['vdate']).days)
P = I['P']
kio_sh = m.kio(I) / sh
print("P/E cons27", round(P / I['cons27'], 2), " core (P - NC_v - kio)/cons27", round((P - br['nc_v'] / sh - kio_sh) / I['cons27'], 2),
      " P/cons26", round(P / 360169.8, 2))

res = {s: R(s) for s in S}
print("\n== Decision")
for s in S:
    r = res[s]
    T = r['T']; sD = sum(r['D']); d = sD / T / P; g = (r['VT'] / P) ** (1 / T) - 1; c = r['irr'] - d - g
    nok = m.irr(P, r['dates'], r['D'], r['VT'], r['vd'], fx=m.I44[s])
    st = R(s, struct=True)
    sd = sum(st['D']) / T / P; sg = (st['VT'] / P) ** (1 / T) - 1
    print(f"{s}: IRR {pct(r['irr'])} NOK {pct(nok)} VT {K(r['VT'])} Pk {K(r['pk'])} MoS {mos(r):+.1%} sumD {K(sD)} "
          f"cap {(sD + r['VT'])/P-1:+.1%} d/g/c {d*100:.1f}/{g*100:.1f}/{c*100:+.1f} struct {pct(st['irr'])} "
          f"cyc {(r['irr']-st['irr'])*100:+.1f} (dd {(d-sd)*100:+.1f}, dg {(g-sg)*100:+.1f})")
    print(f"   eps {[K(x) for x in r['eps']]} rev {[round(x) for x in r['rev']]} NI {[round(x,1) for x in r['NI']]}")
    print(f"   EBITDA~ {[round(r['NI'][i]/(1-m.TAX) + r['da'][i]) for i in range(3)]} /sh {[K((r['NI'][i]/(1-m.TAX) + r['da'][i])/sh) for i in range(3)]}")
    print(f"   MFCF {[round(x,1) for x in r['MFCF']]} /sh {[K(x/sh) for x in r['MFCF']]} GCX/sh {[K(x/sh) for x in r['GCX']]} "
          f"FCF {[round(x,1) for x in r['FCF']]} /sh {[K(x/sh) for x in r['FCF']]} cumFCF/sh {K(sum(r['FCF'])/sh)}")
    print(f"   PAID {[round(x,1) for x in r['PAID']]} NC {[round(x,1) for x in r['NC']]} /sh {[K(x) for x in r['nc_sh']]} book {[round(x,1) for x in r['book']]}")
    print(f"   D {[K(x) for x in r['D']]} pes {[round(x,2) for x in r['pes']]} pe0 {r['pe0']:.2f} Vint {[K(x) for x in r['Vint']]} V26 {K(r['V26'])} kio_t {[K(x) for x in r['kio_t']]}")
    path = [r['V26']] + r['Vint'] + [r['VT']]
    Dy = [r['D'][2] + r['D'][3], r['D'][4], r['D'][5]]
    rt = [(Dy[i] + path[i + 1]) / path[i] - 1 for i in range(3)]
    cum = []
    for i in range(3):
        n = 4 + i
        cum.append(m.irr(P, r['dates'][:n], r['D'][:n], path[i + 1], r['vd'], ex=date(2027 + i, 12, 31)))
    stub_irr = m.irr(P, r['dates'][:2], r['D'][:2], r['V26'], r['vd'], ex=date(2026, 12, 31))
    print(f"   Dy {[K(x) for x in Dy]} stub D {K(r['D'][0]+r['D'][1])} r_t {[f'{x:+.1%}' for x in rt]} IRR to end-26 {pct(stub_irr)} to {[pct(x) for x in cum]}")
    print(f"   P/FCFnorm {P/r['eps'][3]:.1f}x vs ceiling {r['irr']/0.0144:.1f}x; core P/E on 2030 after NC_e {(P - br['nc_e']/sh - kio_sh)/r['eps'][3]:.1f}")

cb = R('Bear', capped=True)
print(f"\nCapped Bear: IRR {pct(cb['irr'])} Pk {K(cb['pk'])} cap {(sum(cb['D'])+cb['VT'])/P-1:+.1%} mult {cb['pes'][0]:.2f} "
      f"Vint {[K(x) for x in cb['Vint']]} VT {K(cb['VT'])} 2027 r {(cb['D'][2]+cb['D'][3]+cb['Vint'][0])/cb['V26']-1:+.1%}")
rb, re_, ru = res['Base'], res['Bear'], res['Bull']
Dw = [0.25 * a + 0.5 * b + 0.25 * c for a, b, c in zip(re_['D'], rb['D'], ru['D'])]
VTw = 0.25 * re_['VT'] + 0.5 * rb['VT'] + 0.25 * ru['VT']
print("weighted ref", pct(m.irr(P, rb['dates'], Dw, VTw, rb['vd'])), " Bull share priced", f"{(P - rb['pk'])/(ru['pk'] - rb['pk']):+.0%}")


def ret27(r):
    return (r['D'][2] + r['D'][3] + r['Vint'][0]) / r['V26'] - 1


b27 = ret27(rb); E = rb['irr'] * 100 - 4.72
for nm, x in [('decision Bear', ret27(re_)), ('capped Bear', ret27(cb))]:
    xn = (1 + x) * 1.08 - 1
    Rr = b27 * 100 - xn * 100
    print(f"E/R {nm}: E {E:.1f} Base27 {b27:+.1%} Bear27 KRW {x:+.1%} NOK {xn:+.1%} R {Rr:.1f} E/R {E/Rr:.3f}")


def solve(f, lo, hi, target):
    flo = f(lo) - target
    for _ in range(80):
        mid = (lo + hi) / 2
        fm = f(mid) - target
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


mk = solve(lambda x: R('Base', mem2830_mult=x)['irr'], -0.5, 1.5, 0.12)
m0 = solve(lambda x: R('Base', mem2830_mult=x)['irr'], -0.5, 1.5, 0.0)
pe_k = solve(lambda x: R('Base', pe=x)['irr'], 0.0, 10.0, 0.12)
m30 = solve(lambda x: R('Base', mem30=x)['irr'], -0.2, 0.35, 0.12)
mall = solve(lambda x: R('Base', mem_all_mult=x)['irr'], 0.01, 1.0, 0.12)
print(f"\nMultiplier 2028-30 for k {mk:.2f} (path {[round(x*mk,2) for x in I['mem_tab']['Base'][1:]]}); for 0% {m0:.2f} ({[round(x*m0,2) for x in I['mem_tab']['Base'][1:]]})")
r30 = R('Base', mem30=m30)
print(f"Break-evens: exit P/E {pe_k:.1f}; 2030 EPS {m30:.3f} of CY27 ({K(r30['eps'][3])}; x2025 {r30['eps'][3]/60372:.1f}); whole path x{mall:.2f} ({(mall-1)*100:.0f}%)")
print("2030 EPS vs 2025 EPS 60,372:", round(rb['eps'][3] / 60372, 1))
for nm, path in [('2019-depth (.90/.45/.30/.25)', [.90, .45, .30, .25]), ('earlier turn (.80/.45/.35/.35)', [.80, .45, .35, .35]),
                 ('later turn (.95/.85/.55/.40)', [.95, .85, .55, .40]), ('Bear path at Base P/E', [.60, .30, .25, .25])]:
    x = R('Base', mem=path)
    print(f"  path {nm}: {pct(x['irr'])} Pk {K(x['pk'])}")

for s in ['Bear', 'Bull']:
    a = R('Base', mem=m.MEM[s], idx=m.IDX[s])
    b = R('Base', mem=m.MEM[s], idx=m.IDX[s], pe=m.EXPE[s])
    if s == 'Bear':
        b = R(s, capex_s='Base', kio_m=1.0)
    else:
        b = R(s, capex_s='Base', kio_m=1.0)
    c = R(s, kio_m=1.0)
    d = R(s)
    print(f"Driver {s}: Base {pct(rb['irr'])} -> H2 path+index {pct(a['irr'])} ({K(a['pk'])}) -> + exit P/E (and Bear 8x from end-27) {pct(b['irr'])} ({K(b['pk'])}) "
          f"-> + capex {pct(c['irr'])} -> + Kioxia = {pct(d['irr'])} ({K(d['pk'])})")

nce = br['nc_e'] / sh; ncv = br['nc_v'] / sh
cons = I['cons27']
core_now = P - ncv - kio_sh
pe_now = core_now / cons
e27 = rb['eps'][0]; e30 = rb['eps'][3]
s1 = core_now * (e27 / cons) - core_now
s2 = pe_now * e30 - pe_now * e27
s3 = 10 * e30 - pe_now * e30
print(f"\nReturn bridge: P {K(P)} = core {K(core_now)} + NC_v {K(ncv)} + Kioxia {K(kio_sh)}; core P/E on cons {pe_now:.2f}; Base27 vs cons {s1:+,.0f} -> {K(core_now+s1)}; "
      f"norm 27->30 {s2:+,.0f} -> {K(core_now+s1+s2)}; multiple to 10 {s3:+,.0f} -> {K(10*e30)}; NC exit {K(rb['nc_sh'][2])} (= NC_v {K(ncv)} + stub {K(nce-ncv)} + retained {K(rb['nc_sh'][2]-nce)}); "
      f"Kioxia {K(rb['kio_t'][2])}; VT {K(rb['VT'])}; sumD {K(sum(rb['D']))}")
print(f"P after NC_e and Kioxia on Base 2030 EPS: {(P - nce - kio_sh)/e30:.1f}x")

for s in S:
    r = res[s]
    gap = r['eps'][2] / r['eps'][3] - 1
    rt = R(s, tail=True)
    core_v = r['pes'][2] * r['eps'][3]
    ncx = r['nc_sh'][2]
    bk = r['book'][3]; bks = bk / sh
    ni30 = r['eps'][3] * sh
    buyer = (core_v * (m.CBUY[s] / m.EXPE[s] + 0.04) + ncx * 0.025) / (core_v + ncx)
    print(f"Exit {s}: eps29 {K(r['eps'][2])} eps30 {K(r['eps'][3])} gap {gap:+.1%} tail/sh {K((r['eps'][2]-r['eps'][3])*(2/3/1.08+1/3/1.08**2))} -> with tail {pct(rt['irr'])} ({K(rt['pk'])}); "
          f"book {bk:,.1f} /sh {K(bks)} P/B {r['VT']/bks:.2f} ROE30 {ni30/bk:.1%} NC share of VT {ncx/r['VT']:.0%} buyer {buyer:.1%}")

print("\n== Sensitivities (Bear | Base | Bull: IRR (P_k))")
def sens(tag, **ov):
    out = []
    for s in S:
        r = R(s, **ov)
        out.append(f"{pct(r['irr'])} ({K(r['pk']/1000)})")
    print(f"{tag}: " + " | ".join(out))
sens("model")
for dpe in (-2, 2):
    out = []
    for s in S:
        r = R(s, pe=m.EXPE[s] + dpe); out.append(f"{pct(r['irr'])} ({K(r['pk']/1000)})")
    print(f"exit P/E {dpe:+d}: " + " | ".join(out))
sens("2030 EPS x0.8", mem30_mult=0.8)
sens("2030 EPS x1.2", mem30_mult=1.2)
sens("2030 EPS x0.6", mem30_mult=0.6)
sens("cons x1.05", cons_mult=1.05)
sens("cons x0.95", cons_mult=0.95)
sens("cons back to 467,761 (x0.8696)", cons_mult=467761 / 537910.7)
sens("capex x1.2", capex_mult=1.2)
sens("capex x0.8", capex_mult=0.8)
cc = {'Bear': [.70, .75, .70], 'Base': [.70, .65, .60], 'Bull': [.70, .70, .55]}
out = []
for s in S:
    r = R(s, cconv=cc[s]); out.append(f"{pct(r['irr'])} ({K(r['pk']/1000)})")
print("H2 cash conversion: " + " | ".join(out))
sens("payout 0", payout=0.0)
sens("payout 1", payout=1.0)
sens("FY2026 rest at floor 25.4", rem2026=25.36)
sens("net cash at exit 50%", cash_w=0.5)
sens("LT liquidity investments not counted", nc_add=-I['ltinv'])
sens("net cash -10", nc_add=-10.0)
sens("net cash +10", nc_add=10.0)
sens("Kioxia zero", kio_mult0=0.0)
sens("tail", tail=True)
for tag, Iq in [("Q4 prices +10%", dict(I, q4=dict(I['q4'], rev=131.2, op=105.0))),
                ("Q4 prices -10%", dict(I, q4=dict(I['q4'], rev=107.4, op=83.6)))]:
    out = []
    for s in S:
        r = m.res(s, Iq); out.append(f"{pct(r['irr'])} ({K(r['pk']/1000)})")
    print(f"{tag}: " + " | ".join(out))
pbr = R('Bear', capped=True)
print(f"Bear capped: {pct(pbr['irr'])} ({K(pbr['pk']/1000)})")
core_now_e = P - nce - kio_sh
pe_today = core_now_e / rb['eps'][3]
x = R('Base', pe=pe_today)
print(f"Base at today's core multiple on 2030 EPS ({pe_today:.1f}x): {pct(x['irr'])} ({K(x['pk']/1000)})")

print("\n== ADR line (SKHY)")
P_adr = ADR * 10 * FX
print(f"ADR {ADR} -> KRW {K(P_adr)} premium {P_adr/P-1:.1%}; 13 Nov close {ADR13} premium {ADR13*10*FX/P-1:.1%}")
for s in S:
    r = res[s]
    for prem in sorted(set([PREM[s], 0.0, 0.15, 0.30, PREM_BULL])):
        VT = r['VT'] * (1 + prem)
        i_ = m.irr(P_adr, r['dates'], r['D'], VT, r['vd'])
        pk_ = m.pk(r['dates'], r['D'], VT, r['vd'])
        nok = m.irr(P_adr, r['dates'], r['D'], VT, r['vd'], fx=m.I44[s])
        tag = '*' if abs(prem - PREM[s]) < 1e-9 else ' '
        print(f" {tag}{s} prem {prem:.0%}: IRR {pct(i_)} NOK {pct(nok)} Pk/ADR ${pk_/FX/10:.2f} MoS {pk_/P_adr-1:+.1%} cap {(sum(r['D'])+VT)/P_adr-1:+.1%}")
VTc = cb['VT']
print(f" capped Bear prem 0: IRR {pct(m.irr(P_adr, cb['dates'], cb['D'], VTc, cb['vd']))} cap {(sum(cb['D'])+VTc)/P_adr-1:+.1%}")
x = R('Base', pe=pe_today)
print(f" Base prem 15% + today's multiple held: IRR {pct(m.irr(P_adr, x['dates'], x['D'], x['VT']*1.15, x['vd']))}")
st = R('Base', struct=True)
print(f" Base structural prem 15%: IRR {pct(m.irr(P_adr, st['dates'], st['D'], st['VT']*1.15, st['vd']))}")
pn = solve(lambda p: m.irr(P_adr, rb['dates'], rb['D'], rb['VT'] * (1 + p), rb['vd']), -0.5, 1.0, 0.12)
print(f" exit premium for Base = 12%: {pn:.1%}")
