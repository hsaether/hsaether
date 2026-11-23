# Samsung Electronics (docs/samsung-analysis.md) -- version 4.1 outputs, 23 Nov 2026 price re-mark (smsn_run4.py = v4).
# Run from this folder: py smsn_run.py   (prints every decision figure, table and sensitivity)
from datetime import date
import smsn_model as m

I = dict(m.V41)
S = ['Bear', 'Base', 'Bull']
pct = lambda x: f"{x*100:.1f}%"
K = lambda x: f"{x:,.0f}"
DISC = dict(Bear=0.30, Base=None, Bull=0.15)   # preference exit discount; Base = today's held
FX = 1346.23                                     # USD/KRW, Yahoo 23 Nov 11:29 UTC
SMSN, SMSD = 3352.0, 2675.0                      # London, 23 Nov 12:14 UTC (Yahoo)
NOKPS = 9.7525                                   # USD/NOK, Norges Bank 20 Nov (23 Nov fixing not yet out)


def R(s, I=I, **ov):
    return m.res(s, I, **ov)


def mos(r, P=None):
    P = r['P'] if P is None else P
    return r['pk'] / P - 1


def pref(r, I, disc_exit, P=None):
    P = I['Ppref'] if P is None else P
    VT = r['VT'] * (1 - disc_exit)
    return m.irr(P, r['dates'], r['D'], VT, r['vd']), m.pk(r['dates'], r['D'], VT, r['vd'])


def line(tag, I, **ov):
    out = [tag]
    for s in S:
        r = R(s, I, **ov)
        out.append(f"{pct(r['irr'])} / {K(r['pk'])} / {mos(r):+.1%}")
    rb = R('Base', I, **ov)
    d0 = 1 - I['Ppref'] / I['P']
    pi, pp = pref(rb, I, d0)
    out.append(f"{pct(pi)} / {K(pp)} / {pp/I['Ppref']-1:+.1%}")
    return " | ".join(out)


print("== Attribution v4 -> v4.1 (Bear | Base | Bull | preference Base)")
V4 = dict(m.V4)
print(line("v4 (195,000; 19 Nov)", V4))
print(line("price and date (= v4.1)", I))

print("\n== Bridge v4.1")
br = m.bridge(I)
for k_, v in br.items():
    print(k_, round(v, 3) if isinstance(v, float) else v)
sh = I['shares'] / 1000
print("nc_v/sh", round(br['nc_v'] / sh), "nc_e/sh", round(br['nc_e'] / sh), "M1", round(m.mem1(I), 2),
      "T", round(m.yf(m.EXIT, I['vdate']), 3), "stub days", (date(2026, 12, 31) - I['vdate']).days)
P = I['P']
print("core P/E today (P - NC_v)/cons27:", round((P - br['nc_v'] / sh) / I['cons27'], 2),
      " P/cons27:", round(P / I['cons27'], 2), " P/cons26:", round(P / 47638.7, 2))

res = {s: R(s) for s in S}
print("\n== Decision")
for s in S:
    r = res[s]
    T = r['T']
    sD = sum(r['D'])
    d = sD / T / P
    g = (r['VT'] / P) ** (1 / T) - 1
    c = r['irr'] - d - g
    nok = m.irr(P, r['dates'], r['D'], r['VT'], r['vd'], fx=m.I44[s])
    st = R(s, struct=True)
    print(f"{s}: IRR {pct(r['irr'])} NOK {pct(nok)} VT {K(r['VT'])} Pk {K(r['pk'])} MoS {mos(r):+.1%} "
          f"sumD {K(sD)} cap {(sD + r['VT'])/P-1:+.1%} d/g/c {d*100:.1f}/{g*100:.1f}/{c*100:+.1f} "
          f"struct {pct(st['irr'])} cyc {(r['irr']-st['irr'])*100:+.1f}")
    sd = sum(st['D']); sdd = sd / T / P; sg = (st['VT'] / P) ** (1 / T) - 1
    print(f"   struct d/g {sdd*100:.1f}/{sg*100:.1f}  -> dd {(d-sdd)*100:+.1f} dg {(g-sg)*100:+.1f}")
    print(f"   rev {[round(x) for x in r['rev']]} NI {[round(x,1) for x in r['NI']]} core {[round(x,1) for x in r['core']]} "
          f"nm {[round(x,1) for x in r['nm']]} INT {[round(x,1) for x in r['INT']]}")
    print(f"   EBITDA {[round(r['core'][i]/0.76 + r['da'][i]) for i in range(3)]} EPS {[K(x) for x in r['eps']]} "
          f"core_eps {[K(x) for x in r['core_eps']]}")
    print(f"   MFCF {[round(x,1) for x in r['MFCF']]} /sh {[K(x/sh) for x in r['MFCF']]} GCX {[round(x,1) for x in r['GCX']]} "
          f"/sh {[K(x/sh) for x in r['GCX']]} FCF {[round(x,1) for x in r['FCF']]} /sh {[K(x/sh) for x in r['FCF']]} cumFCF/sh {K(sum(r['FCF'])/sh)}")
    print(f"   RET {[round(x,1) for x in r['RET']]} PAID {[round(x,1) for x in r['PAID']]} paid/sh {[K(x/sh) for x in r['PAID']]} "
          f"NC {[round(x,1) for x in r['NC']]} /sh {[K(x) for x in r['nc_sh']]} book {[round(x,1) for x in r['book']]}")
    print(f"   dated D {[K(x) for x in r['D']]} pes {[round(x,2) for x in r['pes']]} Vint {[K(x) for x in r['Vint']]} V26 {K(r['V26'])}")
    path = [r['V26']] + r['Vint'] + [r['VT']]
    Dy = [r['D'][0] + r['D'][1], r['D'][2] + r['D'][3], r['D'][4] + r['D'][5]]
    rt = [(Dy[i] + path[i + 1]) / path[i] - 1 for i in range(3)]
    stub_r = path[0] / P - 1
    cum = []
    for i in range(3):
        n = 2 + 2 * i
        VTi = path[i + 1]
        dts = r['dates'][:n]
        ex = date(2027 + i, 12, 31)
        lo, hi = -0.9, 3.0
        for _ in range(200):
            mid = (lo + hi) / 2
            v = -P + sum(x / (1 + mid) ** m.yf(dd, r['vd']) for dd, x in zip(dts, r['D'][:n])) + VTi / (1 + mid) ** m.yf(ex, r['vd'])
            lo, hi = (mid, hi) if v > 0 else (lo, mid)
        cum.append(lo)
    print(f"   Dy {[K(x) for x in Dy]} r_t stub {stub_r:+.1%} {[f'{x:+.1%}' for x in rt]} IRR to {[pct(x) for x in cum]}")
    print(f"   P/FCFnorm {P/r['core_eps'][3]:.1f}x vs ceiling {r['irr']/0.0144:.1f}x; core P/E on 2030 after NC_e {(P - br['nc_e']/sh)/r['core_eps'][3]:.1f}")

# capped Bear
cb = R('Bear', capped=True)
sD = sum(cb['D'])
print(f"\nCapped Bear: IRR {pct(cb['irr'])} Pk {K(cb['pk'])} cap {(sD+cb['VT'])/P-1:+.1%} mult {cb['pes'][0]:.2f} Vint {[K(x) for x in cb['Vint']]} VT {K(cb['VT'])} "
      f"2027 r {(cb['D'][0]+cb['D'][1]+cb['Vint'][0])/res['Bear']['V26']-1:+.1%}")
# Bear P/B 1
pb = R('Bear', pb_exit=1.0)
print(f"Bear P/B 1.0: IRR {pct(pb['irr'])} Pk {K(pb['pk'])} cap {(sum(pb['D'])+pb['VT'])/P-1:+.1%}")

# scenario-weighted reference
rb, re_, ru = res['Base'], res['Bear'], res['Bull']
Dw = [0.25 * a + 0.5 * b + 0.25 * c for a, b, c in zip(re_['D'], rb['D'], ru['D'])]
VTw = 0.25 * re_['VT'] + 0.5 * rb['VT'] + 0.25 * ru['VT']
print("weighted ref", pct(m.irr(P, rb['dates'], Dw, VTw, rb['vd'])))
print("Bull share priced", f"{(P - rb['pk'])/(ru['pk'] - rb['pk']):+.0%}")

# E / R in NOK (Base 2027 return - Bear 2027 return on the I-44 path), NIBOR 4.72, HY ref 0.254
def ret27(r, Vy1):
    return (r['D'][0] + r['D'][1] + Vy1) / r['V26'] - 1
b27 = ret27(rb, rb['Vint'][0]); e27 = ret27(re_, re_['Vint'][0]); c27 = ret27(cb, cb['Vint'][0])
E = rb['irr'] * 100 - 4.72
for nm, x in [('decision Bear', e27), ('capped Bear', c27)]:
    xn = (1 + x) * 1.08 - 1
    Rr = b27 * 100 - xn * 100
    print(f"E/R {nm}: E {E:.1f} Base27 {b27:+.1%} Bear27 KRW {x:+.1%} NOK {xn:+.1%} R {Rr:.1f} E/R {E/Rr:.3f}")

# multipliers on Base 2028-30 (2027 at Base) for k and 0%
def solve(f, lo, hi, target):
    for _ in range(80):
        mid = (lo + hi) / 2
        if (f(mid) - target) * (f(hi) - target) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2
mk = solve(lambda x: R('Base', mem2830_mult=x)['irr'], 0.05, 1.5, 0.12)
m0 = solve(lambda x: R('Base', mem2830_mult=x)['irr'], 0.0, 1.5, 0.0)
pe_k = solve(lambda x: R('Base', pe=x)['irr'], 1.0, 10.0, 0.12)
m30 = solve(lambda x: R('Base', mem30=x)['irr'], 0.0, 0.35, 0.12)
mall = solve(lambda x: R('Base', mem_all_mult=x)['irr'], 0.2, 1.0, 0.12)
print(f"\nMultiplier for k {mk:.2f} (path {[round(x*mk,2) for x in I['mem_tab']['Base'][1:]]}); for 0% {m0:.2f} ({[round(x*m0,2) for x in I['mem_tab']['Base'][1:]]})")
r30 = R('Base', mem30=m30)
print(f"Break-evens: exit P/E {pe_k:.1f}; 2030 memory {m30:.2f} (core EPS {K(r30['core_eps'][3])}); whole path x{mall:.2f} ({(mall-1)*100:.0f}%)")
print("2030 core EPS vs 2025 EPS 6,605:", round(rb['core_eps'][3] / 6605, 1))

# driver breakdown (Bear, Bull): sector path -> exit P/E -> company items
for s in ['Bear', 'Bull']:
    a = R('Base', mem=m.MEM[s], idx=m.IDX[s])
    b = R(s, nm_s='Base', capex_s='Base', nmrev_s='Base')
    c = R(s, capex_s='Base')
    d = R(s)
    print(f"Driver {s}: Base {pct(rb['irr'])} -> H2 path+index {pct(a['irr'])} ({K(a['pk'])}) -> + exit P/E {pct(b['irr'])} ({K(b['pk'])}) "
          f"-> + non-memory {pct(c['irr'])} -> + capex = {pct(d['irr'])} ({K(d['pk'])})")

# return bridge (Base, per share)
nce = br['nc_e'] / sh; ncv = br['nc_v'] / sh
cons = I['cons27']
core_now = P - ncv
pe_now = core_now / cons
c27 = rb['core_eps'][0]; c30 = rb['core_eps'][3]
s1 = core_now * (c27 / cons) - core_now
s2 = pe_now * c30 - pe_now * c27
s3 = 10 * c30 - pe_now * c30
print(f"\nReturn bridge: P {K(P)} = core {K(core_now)} + NC_v {K(ncv)}; core P/E on cons {pe_now:.2f}; Base27 vs cons {s1:+,.0f} -> {K(core_now+s1)}; "
      f"normalisation 27->30 {s2:+,.0f} -> {K(core_now+s1+s2)}; multiple to 10 {s3:+,.0f} -> {K(10*c30)}; NC exit {K(rb['nc_sh'][2])} (= NC_v {K(ncv)} + stub {K(nce-ncv)} + retained {K(rb['nc_sh'][2]-nce)}); VT {K(rb['VT'])}; sumD {K(sum(rb['D']))}")
print(f"core P/E on Base 2030 after NC_e {(P-nce)/c30:.1f}; after NC_v {(P-ncv)/c30:.1f}")

# exit consistency and cross-check
for s in S:
    r = res[s]
    gap = r['core_eps'][2] / r['core_eps'][3] - 1
    tail = (r['core_eps'][2] - r['core_eps'][3]) * (2 / 3 / 1.08 + 1 / 3 / 1.08 ** 2)
    rt = R(s, tail=True)
    core_v = r['pes'][2] * r['core_eps'][3]
    ncx = r['nc_sh'][2]
    bk = r['book'][3]; bks = bk / sh
    ni30 = r['core'][3] + r['NC'][2] * I['rate'] * (1 - m.TAX)
    buyer = (core_v * (m.CBUY[s] / m.EXPE[s] + 0.04) + ncx * 0.025) / r['VT']
    print(f"Exit {s}: core29 {K(r['core_eps'][2])} core30 {K(r['core_eps'][3])} gap {gap:+.1%} tail {K(tail)} -> with tail {pct(rt['irr'])} ({K(rt['pk'])}); "
          f"book {bk:,.1f} /sh {K(bks)} P/B {r['VT']/bks:.2f} ROE30 {ni30/bk:.1%} NC share of VT {ncx/r['VT']:.0%} buyer {buyer:.1%}")
# re-discount at World's mid-cycle return 8.2%: exit P/E where buyer's return = 8.2%
def buyer_pe(pe):
    r = R('Base', pe=pe)
    core_v = pe * r['core_eps'][3]
    return (core_v * (0.60 / pe + 0.04) + r['nc_sh'][2] * 0.025) / r['VT']
pew = solve(buyer_pe, 6.0, 14.0, 0.082)
rw = R('Base', pe=pew)
print(f"World mid-cycle return exit P/E {pew:.1f}: {pct(rw['irr'])} ({K(rw['pk'])})")

# sensitivities
print("\n== Sensitivities (Bear | Base (Pk) | Bull)")
def sens(tag, **ov):
    o = []
    for s in S:
        r = R(s, **ov)
        o.append(f"{pct(r['irr'])}" + (f" ({r['pk']/1000:.0f})" if s == 'Base' else ""))
    print(tag, " | ".join(o))
sens("model")
for dpe in (-2, 2):
    o = [pct(R(s, pe=m.EXPE[s] + dpe)['irr']) + (f" ({R(s, pe=m.EXPE[s]+dpe)['pk']/1000:.0f})" if s == 'Base' else '') for s in S]
    print(f"exit P/E {dpe:+d}", " | ".join(o))
for k_ in (0.8, 1.2, 0.6, 0.5):
    sens(f"2030 memory x{k_}", mem30_mult=k_)
pe_today = (P - nce) / rb['core_eps'][3]
o = [pct(R(s, pe=(P - nce) / R(s)['core_eps'][3])['irr']) for s in S]
print(f"exit at today's core multiple (Base {pe_today:.1f}x)", " | ".join(o), f"Base Pk {R('Base', pe=pe_today)['pk']/1000:.0f}")
for k_ in (0.95, 1.05):
    sens(f"memory consensus x{k_}", cons_mult=k_)
for k_ in (1.2, 0.8):
    sens(f"capex x{k_}", capex_mult=k_)
cc = {'Bear': [.70, .75, .70], 'Base': [.70, .65, .60], 'Bull': [.70, .70, .55]}
o = [pct(R(s, cconv=cc[s])['irr']) + (f" ({R(s, cconv=cc[s])['pk']/1000:.0f})" if s == 'Base' else '') for s in S]
print("AI BBB H2 cash conversion", " | ".join(o))
sens("payout 0%", payout=0.0)
sens("payout 100%", payout=1.0)
sens("net cash at exit at 50%", cash50=True)
sens("payout 0% + cash 50%", payout=0.0, cash50=True)
for qq in (1.10, 0.90):
    q = dict(I['q4']); d_ = 155.0 * (qq - 1)
    q['rev'] += d_; q['op'] += d_ * 0.88; q['dsop'] += d_ * 0.88
    o = []
    for s in S:
        r = m.res(s, dict(I, q4=q))
        o.append(pct(r['irr']))
    print(f"Q4 memory prices x{qq}", " | ".join(o))
for rem in (55.0, 75.0):
    sens(f"2026 remainder {rem}", rem2026=rem)
for tag, Ix in [("long-term deposits not counted", dict(I, ltdep=0.0)), ("prepayments not deducted", dict(I, prepay=0.0)),
                ("award shortfall not deducted", dict(I, sbp30sep=0.0, sbpq4oth=0.0)),
                ("treasury shares cancelled (6,511m; awards bought in full)", dict(I, shares=6.51193, treas=0.0))]:
    o = []
    for s in S:
        r = m.res(s, Ix)
        o.append(pct(r['irr']) + (f" ({r['pk']/1000:.0f})" if s == 'Base' else ''))
    print(tag, " | ".join(o))
sens("non-memory zero", nm_zero=True)
sens("DX x1.25", dx_mult=1.25)
sens("reversion tail", tail=True)

# preference line
print(f"\n== Preference ({K(I['Ppref'])}; discount today {1-I['Ppref']/P:.1%})")
d0 = 1 - I['Ppref'] / P
for s, dd in [('Base', d0), ('Base', 0.15), ('Base', 0.30), ('Bear', 0.30), ('Bear', d0), ('Bull', 0.15), ('Bull', d0)]:
    pi, pp = pref(res[s], I, dd)
    print(f"{s} disc {dd:.1%}: {pct(pi)} Pk {K(pp)} MoS {pp/I['Ppref']-1:+.1%}")
pi, pp = pref(cb, I, 0.30)
print(f"capped Bear disc 30%: {pct(pi)} Pk {K(pp)} cap {(sum(cb['D'])+cb['VT']*0.7)/I['Ppref']-1:+.1%}")
for s in S:
    dd = DISC[s] if DISC[s] is not None else d0
    r = res[s]
    print(f"pref NOK {s}: {pct(m.irr(I['Ppref'], r['dates'], r['D'], r['VT']*(1-dd), r['vd'], fx=m.I44[s]))}")
# preference V_t path (Base held; Bear 30% from end-2027; Bull linear to 15%)
for s in S:
    r = res[s]
    if s == 'Base':
        ds = [d0, d0, d0]
    elif s == 'Bear':
        ds = [0.30, 0.30, 0.30]
    else:
        ds = [d0 + (0.15 - d0) * (k + 1) / 3 for k in range(3)]
    vp = [r['Vint'][0] * (1 - ds[0]), r['Vint'][1] * (1 - ds[1]), r['VT'] * (1 - ds[2])]
    print(f"pref V_t {s}: {[K(x) for x in vp]}")
print("pref capped V_t:", [K(x * 0.7) for x in cb['Vint'] + [cb['VT']]], "pref end-2026 mark", K(res['Base']['V26'] * (1 - d0)))

# GDRs
print("\n== GDR")
for nm, px, base, s_ in [('SMSN', SMSN, P, 'c'), ('SMSD', SMSD, I['Ppref'], 'p')]:
    krw = px * FX / 25
    print(f"{nm}: ${px} = KRW {K(krw)} per share; premium {krw/base-1:+.1%}; NOK per GDR {px*NOKPS:,.0f}")
    for s in S:
        r = res[s]
        if s_ == 'c':
            VT = r['VT']
        else:
            VT = r['VT'] * (1 - (DISC[s] if DISC[s] is not None else d0))
        ii = m.irr(krw, r['dates'], r['D'], VT, r['vd']); pkk = m.pk(r['dates'], r['D'], VT, r['vd'])
        print(f"   {s}: IRR {pct(ii)} Pk/GDR ${pkk*25/FX:,.0f} MoS {pkk/krw-1:+.1%}")
print("NOK per common share", round(P / FX * NOKPS, 1))

# HY / World trigger prices (Base IRR = 7.2% HY Base, 6.6% World)
for tag, k_ in [('HY 7.5%', 0.075), ('World 6.4%', 0.064)]:
    print(tag, K(m.pk(rb['dates'], rb['D'], rb['VT'], rb['vd'], k=k_)))
# Year 1 by quarter (Base, EPS split of CY27 consensus x haircut, as v2)
split = [16500, 17700, 18600, 19500]; f_ = I['cons27'] / sum(split)
hc = [0.98, 0.93, 0.87, 0.83]
print("Q split cons", [K(x * f_) for x in split], "Base", [K(x * f_ * h) for x, h in zip(split, hc)], K(sum(x * f_ * h for x, h in zip(split, hc))))
# stub per share
q = I['q4']; fr = 38 / 92
print("stub: rev", round(q['rev'] * fr, 1), "EBITDA", round((q['op'] + br['award_q4'] + q['da']) * fr, 1),
      "EPS", K((q['op'] + q['intr']) * 0.76 * fr / sh), "Q4E EPS", K((q['op'] + q['intr']) * 0.76 / sh),
      "stub cash/sh", K(res['Base']['stub_cash']))

# cycle paths (AI BBB H2 Memory cycle, section 5) through the company build, exit P/E 10 and 8
print("\n== Cycle paths (company build)")
paths = [("Base: turn in 2028", [.90, .60, .40, .35]), ("Earlier turn (2H-27)", [.80, .45, .35, .35]),
         ("Later turn (2029)", [.95, .85, .55, .40]), ("Shallower (LTA floors hold)", [.90, .70, .55, .45]),
         ("Deeper: 2019 depth", [.90, .45, .30, .25]), ("Bear path", [.60, .30, .25, .25])]
for tag, p in paths:
    a = R('Base', mem=p); b = R('Base', mem=p, pe=8.0)
    print(f"{tag} {p}: exit 10 {pct(a['irr'])} ({a['pk']/1000:.0f}) | exit 8 {pct(b['irr'])} ({b['pk']/1000:.0f})")
