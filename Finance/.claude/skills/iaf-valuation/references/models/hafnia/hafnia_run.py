"""Hafnia v8 (18 Nov 2026): decision figures, tables, sensitivities, attribution. Run: py hafnia_run.py
Writes results.json beside this script."""
import json
from hafnia_model import *

SC = ('Bear', 'Base', 'Bull')
ns = lambda usd: usd / SH * FX             # $m -> NOK per share
out = {}

def yr_rows(res):
    """aggregate quarterly rows into Q4-26, Q1..Q4-27, 2028, 2029 and annual 2027."""
    rs = res['rows']
    def agg(sel, lab):
        g = [r for r in rs if sel(r)]
        a = {'lab': lab}
        for k_ in ('tce', 'days', 'ebitda', 'np', 'mfcf', 'amort', 'fcf_ads', 'nb', 'opt', 'dec', 'paid', 'torm_div'):
            a[k_] = sum(r[k_] for r in g)
        a['tce_day'] = a['tce'] / a['days'] * 1000
        a['nd'] = g[-1]['nd']; a['ltv'] = g[-1]['ltv']; a['po'] = g[-1]['po']
        a['po_min'] = min(r['po'] for r in g); a['ltv_max'] = max(r['ltv'] for r in g)
        return a
    cols = [agg(lambda r: r['y'] == 2026, 'Q4-26')]
    cols += [agg(lambda r, q=q: r['y'] == 2027 and r['q'] == q, f'Q{q}-27') for q in (1, 2, 3, 4)]
    cols += [agg(lambda r: r['y'] == 2028, '2028'), agg(lambda r: r['y'] == 2029, '2029')]
    annual = {'2027': agg(lambda r: r['y'] == 2027, '2027')}
    return cols, annual

def year_path(res, path, scen):
    """year-end path: D_t paid per period (NOK/sh), V_t, r_t, IRR to t."""
    d = decision(res, path)
    ds = d['ds']
    periods = [(VAL, dt.date(2026, 12, 31)), (dt.date(2027, 1, 1), dt.date(2027, 12, 31)),
               (dt.date(2028, 1, 1), dt.date(2028, 12, 31)), (dt.date(2029, 1, 1), dt.date(2029, 12, 31))]
    Vs = [vt_interim(res, scen, i) for i in range(3)] + [res['VT']]
    Vs = [ns(v) for v in Vs]
    Dp = [sum(a for dd, a in ds if s <= dd <= e) for s, e in periods]
    rt, irrs = [], []
    prev = P_NOK
    for i in range(4):
        rt.append((Dp[i] + Vs[i] - prev) / prev)
        prev = Vs[i]
        end = periods[i][1]
        cfs = [(VAL, -P_NOK)] + [(dd, a) for dd, a in ds if dd <= end] + [(end, Vs[i])]
        irrs.append(xirr(cfs) if i > 0 else None)
    return dict(D=Dp, V=Vs, r=rt, irr=irrs)

# ---------------- decision, both paths ----------------
R = {}
for path in ('A', 'B'):
    for s in SC:
        res = run(s, path)
        d = decision(res, path)
        cols, ann = yr_rows(res)
        nav0 = nav_at_val(res, s, path)
        cum_mfcf = sum(r['mfcf'] for r in res['rows'])
        R[(path, s)] = dict(res=res, d=d, cols=cols, ann=ann, nav0=nav0)
        out[f'{path}_{s}'] = dict(irr=d['irr'], pk=d['pk'], mos=d['mos'], sumD=d['sumD'], vt=d['vt'],
                                  VT_usd=res['VT'], nd_T=res['nd'], nd_T_sh=ns(res['nd']),
                                  cap=d['sumD'] + d['vt'], cum_mfcf_sh=ns(cum_mfcf),
                                  ltv_max=max(r['ltv'] for r in res['rows'][1:]),
                                  po_min=min(r['po'] for r in res['rows'][1:]),
                                  nav0=nav0['nav'], nav0_sh=ns(nav0['nav']), tail=res['tail'])
navnow = nav_at_val(R[('A', 'Base')]['res'], 'now', 'A')
out['nav_now'] = {k_: v for k_, v in navnow.items()}
out['nav_now_sh'] = ns(navnow['nav'])
out['nav0_parts'] = {k_: v for k_, v in R[('A', 'Base')]['nav0'].items()}

print(f"P NOK {P_NOK}  FX {FX}  P$ {P_NOK/FX:.3f}  T {T:.3f}  SH {SH:.2f}")
print('NAV now parts', {k_: round(v, 1) for k_, v in navnow.items()})
print('NAV0 parts', {k_: round(v, 1) for k_, v in R[('A', 'Base')]['nav0'].items()})
print(f"NAV today $m {navnow['nav']:.0f} = NOK {ns(navnow['nav']):.1f}/sh  P/NAV {P_NOK/ns(navnow['nav']):.2f}")
for path in ('A', 'B'):
    for s in SC:
        o = out[f'{path}_{s}']
        print(f"{path} {s:4s} IRR {o['irr']*100:6.1f}%  Pk {o['pk']:6.1f}  MoS {o['mos']*100:6.1f}%  sumD {o['sumD']:5.1f}  VT {o['vt']:6.1f} (${o['VT_usd']:.0f}m)  cap {o['cap']:6.1f} ({(o['cap']/P_NOK-1)*100:+.0f}%)  cumMFCF {o['cum_mfcf_sh']:.1f}  NDT {o['nd_T_sh']:.1f}  LTVmax {o['ltv_max']:.3f} POmin {o['po_min']:.2f}  NAV0 {o['nav0_sh']:.1f} (P/NAV0 {P_NOK/o['nav0_sh']:.2f}) tail {o['tail']:.1f}")

# ---------------- period tables ----------------
print("\nPERIOD TABLES (path A)")
for s in SC:
    cols, ann = R[('A', s)]['cols'], R[('A', s)]['ann']
    print(f"-- {s}")
    for c in cols:
        print(f"  {c['lab']:6s} TCE {c['tce']:5.0f} /d {c['tce_day']:5.1f}  EBITDA {c['ebitda']:5.0f}  NP {c['np']:5.0f}  MFCF {c['mfcf']:5.0f}/{ns(c['mfcf']):5.2f}  amort {c['amort']:4.1f}  FCFads {c['fcf_ads']:5.0f}/{ns(c['fcf_ads']):5.2f}  NB {c['nb']:5.1f} opt {c['opt']:5.0f}  dec {c['dec']:5.0f}/{ns(c['dec']):5.2f}  ND {c['nd']:5.0f}/{ns(c['nd']):5.1f}  LTV {c['ltv']*100:4.0f}% po {c['po']*100:3.0f}%")
    a = ann['2027']
    print(f"  2027  TCE {a['tce']:.0f} /d {a['tce_day']:.1f} EBITDA {a['ebitda']:.0f} NP {a['np']:.0f} dec {a['dec']:.0f}/{ns(a['dec']):.2f}  MFCF {a['mfcf']:.0f}/{ns(a['mfcf']):.2f} amort {a['amort']:.1f}")
out['periods'] = {s: R[('A', s)]['cols'] for s in SC}
out['ann27'] = {s: R[('A', s)]['ann']['2027'] for s in SC}

# ---------------- year-end path ----------------
print("\nYEAR-END PATH (NOK/sh)")
YP = {}
for path in ('A', 'B'):
    for s in SC:
        yp = year_path(R[(path, s)]['res'], path, s)
        YP[(path, s)] = yp
        print(path, s, 'D', [round(x, 2) for x in yp['D']], 'V', [round(x, 1) for x in yp['V']],
              'r', [round(x * 100, 1) for x in yp['r']], 'IRR', [None if x is None else round(x * 100, 1) for x in yp['irr']])
out['yearpath'] = {f'{p}_{s}': YP[(p, s)] for p in ('A', 'B') for s in SC}

# ---------------- return split, structural ----------------
print("\nRETURN SPLIT (path A)")
for s in SC:
    d = R[('A', s)]['d']; nav0 = ns(R[('A', s)]['nav0']['nav'])
    dd = d['sumD'] / T / P_NOK
    g = (d['vt'] / P_NOK) ** (1 / T) - 1
    c = d['irr'] - dd - g
    rer = (nav0 / P_NOK) ** (1 / T) - 1
    navg = (d['vt'] / nav0) ** (1 / T) - 1
    st = run(s, 'A', struct=True)
    sd = decision(st, 'A')
    sdd = sd['sumD'] / T / P_NOK
    sg = (sd['vt'] / P_NOK) ** (1 / T) - 1
    out[f'split_{s}'] = dict(d=dd, g=g, c=c, rer=rer, navg=navg, p_nav0=P_NOK / nav0, st_irr=sd['irr'],
                            cyc=d['irr'] - sd['irr'], dd=dd - sdd, dg=g - sg, st_pk=sd['pk'])
    print(f"{s}: d {dd*100:.1f}% g {g*100:.1f}% c {c*100:+.1f}pp | rerating {rer*100:.1f}% NAVgrowth {navg*100:.1f}% (P/NAV0 {P_NOK/nav0:.2f}) | structural {sd['irr']*100:.1f}% cyclical {(d['irr']-sd['irr'])*100:+.1f}pp (dd {(dd-sdd)*100:+.1f}, dg {(g-sg)*100:+.1f})")

# ---------------- V_T bridge (Base A) ----------------
res = R[('A', 'Base')]['res']; n0 = R[('A', 'Base')]['nav0']
nd_val = n0['nd']; jvnd_val = n0['jvnd']
f0 = {s_: V_MC['Base'][seg_row(s_)] / V_ANCHOR[seg_row(s_)] for s_ in SEGS}
nb_after = sum(r['nb'] for r in res['rows']) - (1 - FRAC) * res['rows'][0]['nb']
br = dict(
    nav0=n0['nav'],
    special=-TORM_N * TORM_PX,
    nb_created=res['nb_T'] - n0['nb'] - nb_after,
    opt_age=res['opt_T'] - n0['opt_vessels'],
    own_age=res['own_T'] - n0['own'],
    jv=(res['jv_T'] - n0['jv']) + (jvnd_val - res['jv_nd']),
    prem=-n0['prem'],
    tail=res['tail'],
    retained=(nd_val - res['nd']) + nb_after + OPT_STRIKE - TORM_DIV_Q4,
)
br['tdiv_collected'] = 0.0
tot = sum(v for k_, v in br.items() if k_ != 'nav0') + br['nav0']
print("\nV_T BRIDGE Base A ($m / NOK sh):")
for k_, v in br.items():
    print(f"  {k_:12s} {v:8.1f}  {ns(v):6.2f}")
print(f"  sum {tot:.1f} vs VT {res['VT']:.1f}")
out['bridge'] = br
# retained cash check: sum MFCF after val - dividends paid (cash) - TORM div receivable
mf_after = sum(r['mfcf'] for r in res['rows']) - (1 - FRAC) * (res['rows'][0]['mfcf'] - res['rows'][0]['torm_div']) - TORM_DIV_Q4
paid_cash = sum(r['paid'] for r in res['rows'])
print(f"  check retained = sum MFCF after val {mf_after:.1f} - div paid {paid_cash:.1f} = {mf_after - paid_cash:.1f}")

# ---------------- exit asset table ----------------
print("\nEXIT ASSETS ($m)")
for s in SC:
    r_ = R[('A', s)]['res']
    print(f"  {s}: owned {r_['own_T']:.0f} options {r_['opt_T']:.0f} NB {r_['nb_T']:.0f} JV {r_['jv_T']:.0f}-{r_['jv_nd']:.0f}={r_['jv_T']-r_['jv_nd']:.0f} tail {r_['tail']:.1f} {r_['tails']} NWC {NWC} other {OTHER:.1f} ND {r_['nd']:.0f} VT {r_['VT']:.0f} = NOK {ns(r_['VT']):.1f}")
    out[f'exit_{s}'] = dict(own=r_['own_T'], opt=r_['opt_T'], nb=r_['nb_T'], jv=r_['jv_T'], jvnd=r_['jv_nd'], tail=r_['tail'], tails=r_['tails'], nd=r_['nd'], VT=r_['VT'])
# B exit TORM
for s in SC:
    print(f"  B {s}: TORM exit ${R[('B', s)]['res']['torm_T']:.0f}m (${R[('B', s)]['res']['torm_T']/TORM_N:.1f}/sh)")

# ---------------- exit-consistency: no-tail sensitivity ----------------
print("\nNO TAIL:")
for s in SC:
    d = decision(run(s, 'A', tail_on=False), 'A')
    out[f'notail_{s}'] = dict(irr=d['irr'], pk=d['pk'])
    print(f"  {s}: IRR {d['irr']*100:.1f}% Pk {d['pk']:.1f}")

# ---------------- exit cross-check ----------------
print("\nEXIT CROSS-CHECK")
for s in SC:
    r_ = R[('A', s)]['res']
    mc = {x: ROWS[s][x]['mc'] for x in ('LR2', 'LR1', 'MR')}
    days = 365 * UTIL
    tce = (6 * mc['LR2'] + 22 * mc['LR1'] + 57 * mc['MR'] + 20 * mc['MR'] * HANDY_X) * days / 1000
    tc_in = 3 * days * (mc['MR'] - 19.9) / 1000
    opex = (6 + 22 + 57 + 20) * 365 * OPEX[2029] / 1000
    ga = GA[2029] * 4; fee = FEE * 4; oth = OTH_HIRE[2029] * 4
    jv = ((2 * mc['LR2'] + 3 * mc['LR1'] + 2 * mc['MR']) * days - 7 * 365 * JV_OPEX[2029]) / 1000 - 2.0
    ebitda = tce + tc_in + fee - opex - ga - oth
    nd_T = r_['nd']; jvnd = r_['jv_nd']
    interest = R_DEBT * nd_T + FIN_FIX * 4
    mfcf = ebitda - TAX_Q * 4 - interest - MCAPEX[2029] * 4 + jv - 0.06 * jvnd
    # fleet-renewal charge: ageing at the scenario's mid-cycle marks over the window / T
    f_ = {x: V_MC[s][seg_row(x)] / V_ANCHOR[seg_row(x)] for x in SEGS}
    o0, p0, j0 = fleet_value(s, VAL, f_)
    oT, pT, jT = fleet_value(s, EXIT, f_)
    ageing = (o0 + p0 + j0) - (oT + pT + jT)
    renew = ageing / T
    fcfn = mfcf - renew
    fcfn_pre = fcfn + 15.0
    da = (DA_OWN[2029] + 3.5) * 4 + 1.9 * 10 + 14.0
    np_mc = ebitda - da - interest - TAX_Q * 4 + (jv - 0.06 * jvnd - 14)
    book = r_['book'] + r_['rows'][-1]['dec']      # Q4-29 dividend is declared after exit
    VT = r_['VT']
    assets = VT + nd_T + jvnd
    buyer = (0.08 * (r_['own_T'] + r_['opt_T'] + r_['nb_T'] + r_['jv_T']) + 0.05 * (NWC + OTHER) - 0.05 * (nd_T + jvnd)) / VT
    out[f'xc_{s}'] = dict(ebitda=ebitda, mfcf=mfcf, renew=renew, ageing=ageing, fcfn=fcfn, fcfn_pre=fcfn_pre,
                          pe_fcf=VT / fcfn_pre if fcfn_pre > 0 else None, np_mc=np_mc,
                          pe_np=VT / np_mc if np_mc > 0 else None, book=book, pb=VT / book, buyer=buyer,
                          p_fcf=P_NOK / ns(fcfn) if fcfn > 0 else None)
    print(f"  {s}: EBITDA_mc {ebitda:.0f} MFCF {mfcf:.0f} renew {renew:.0f} FCFn {fcfn:.0f} (NOK {ns(fcfn):.2f}) pre-holdco {fcfn_pre:.0f} exitPE {VT/fcfn_pre if fcfn_pre>0 else float('nan'):.1f} NPmc {np_mc:.0f} PE_np {VT/np_mc if np_mc>0 else float('nan'):.1f} book {book:.0f} P/B {VT/book:.2f} buyer {buyer*100:.1f}%  P/FCFn {P_NOK/ns(fcfn) if fcfn>0 else float('nan'):.1f} ceiling {out[f'A_{s}']['irr']/K**2:.1f}")

# re-discount exit marks at the Oslo mid-cycle return (Equity BBB 6 Nov: 8.0 / 8.9 / 9.2%)
OSLO_MC = {'Bear': 0.080, 'Base': 0.089, 'Bull': 0.092}
print("\nEXIT SENSITIVITIES")
for s in SC:
    buyer = out[f'xc_{s}']['buyer']
    idx = OSLO_MC[s]
    # marks re-discounted from 8% to the index return over ~11 years of remaining life (annuity ratio)
    ann = lambda r: (1 - (1 + r) ** -11) / r
    disc = ann(0.08 + (idx - 0.08)) / ann(0.08) if buyer < idx else 1.0
    d1 = decision(run(s, 'A', exit_disc=disc), 'A')
    ovh = 85.0 * ann(0.08)
    d2 = decision(run(s, 'A', overhead=ovh), 'A')
    out[f'xs_{s}'] = dict(disc=disc, irr_disc=d1['irr'], pk_disc=d1['pk'], ovh=ovh, irr_ovh=d2['irr'], pk_ovh=d2['pk'])
    print(f"  {s}: buyer {buyer*100:.1f}% vs Oslo {idx*100:.1f}% -> factor {disc:.3f}: IRR {d1['irr']*100:.1f}% Pk {d1['pk']:.1f} | overhead ${ovh:.0f}m (NOK {ns(ovh):.1f}): IRR {d2['irr']*100:.1f}% Pk {d2['pk']:.1f}")

# ---------------- NOK path (Equity BBB) ----------------
print("\nNOK PATH (Equity BBB): USD/NOK Bear +12% (2027) +9% (2028-29); Bull -3%")
for s, fp in (('Bear', {2027: FX * 1.12, 2028: FX * 1.09, 2029: FX * 1.09}), ('Bull', {2027: FX * 0.97, 2028: FX * 0.97, 2029: FX * 0.97})):
    d = decision(R[('A', s)]['res'], 'A', fx_path=fp)
    out[f'nok_{s}'] = dict(irr=d['irr'], pk=d['pk'])
    print(f"  {s}: IRR {d['irr']*100:.1f}% Pk {d['pk']:.1f}")

# ---------------- sensitivities (Base A) ----------------
print("\nSENSITIVITY Base A")
base = out['A_Base']
S = []
def sens(lab, **kw):
    path = kw.pop('path', 'A'); P = kw.pop('P', P_NOK); k = kw.pop('k', K); tp = kw.pop('torm_px_dec', TORM_PX)
    d = decision(run(kw.pop('scen', 'Base'), path, **kw), path, P=P, k=k, torm_px=tp)
    S.append((lab, d['irr'], d['pk']))
    print(f"  {lab:60s} IRR {d['irr']*100:6.1f}%  Pk {d['pk']:6.1f}  ({d['pk']-base['pk']:+.1f})")
sens('Cash fallback (path B: Q3 90% cash, Q4 by policy, TORM held to exit)', path='B')
sens('No reversion tail', tail_on=False)
sens('Hafnia TCE factor 0.9 on open days 2027+', fac=0.9)
sens('Hafnia TCE factor 1.1 on open days 2027+', fac=1.1)
sens('Open-day rates +12% 2027+', rate_mult=1.12)
sens('LR1 2027 at the retest level 52 (baseline flag)', lr1_2027=52)
sens('Q4-26 open days x0.8', q4fac=0.8)
sens('Q4-26 open days x1.2', q4fac=1.2)
sens('Exit fleet+NB values x0.9', val_mult=0.9)
sens('Exit fleet+NB values x1.1', val_mult=1.1)
sens('TORM price at distribution -10%', torm_px_dec=TORM_PX * 0.9)
sens('TORM price at distribution +10%', torm_px_dec=TORM_PX * 1.1)
sens('Base cash flows with Bear exit marks', exit_scen='Bear')
sens('Base cash flows with Bull exit marks', exit_scen='Bull')
sens('Payout fixed at 90%', payout_fixed=0.9)
for kk in (0.10, 0.13, 0.14):
    sens(f'k = {kk*100:.0f}%', k=kk)
out['sens'] = S
# V_T needed for 12%; break-evens
d = R[('A', 'Base')]['d']
pv_d = sum(a / (1 + K) ** ((dd - VAL).days / 365) for dd, a in d['ds'])
vt_need = (P_NOK - pv_d) * (1 + K) ** T
out['vt_need'] = vt_need
print(f"  V_T needed for 12%: NOK {vt_need:.1f} vs {d['vt']:.1f} (x {vt_need/d['vt']:.2f})")
def solve(fn, lo, hi):
    for _ in range(60):
        m = (lo + hi) / 2
        if fn(m) < K:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2
be_rate = solve(lambda m: decision(run('Base', 'A', rate_mult=m), 'A')['irr'], 1.0, 3.0)
be_val = solve(lambda m: decision(run('Base', 'A', val_mult=m), 'A')['irr'], 1.0, 2.0)
be_both = solve(lambda m: decision(run('Base', 'A', rate_mult=m, val_mult=m), 'A')['irr'], 1.0, 2.0)
out['be'] = dict(rate=be_rate, val=be_val, both=be_both)
print(f"  break-even: open-day rates 2027-29 x{be_rate:.2f}; exit values x{be_val:.2f}; both x{be_both:.2f}")
# which share of Bull is priced
bp = (P_NOK - out['A_Base']['pk']) / (out['A_Bull']['pk'] - out['A_Base']['pk'])
out['bull_priced'] = bp
print(f"  Bull priced: {bp*100:.0f}%")
# scenario-weighted reference (levels 25/50/25)
dsw = {}
for s, w in (('Bear', .25), ('Base', .5), ('Bull', .25)):
    for dd, a in R[('A', s)]['d']['ds']:
        dsw[dd] = dsw.get(dd, 0) + w * a
vtw = sum(w * R[('A', s)]['d']['vt'] for s, w in (('Bear', .25), ('Base', .5), ('Bull', .25)))
cfs = [(VAL, -P_NOK)] + sorted(dsw.items()) + [(EXIT, vtw)]
irr_w = xirr(cfs); pk_w = sum(a / 1.12 ** ((dd - VAL).days / 365) for dd, a in dsw.items()) + vtw / 1.12 ** T
out['weighted'] = dict(irr=irr_w, pk=pk_w)
print(f"  scenario-weighted reference: IRR {irr_w*100:.1f}% Pk {pk_w:.1f}")
# E/R reference (HY rule, reference only): E = Base IRR - avg 3M NIBOR (HY BBB Base 4.37%); R = Base 2027 r_t - Bear 2027 r_t
E = out['A_Base']['irr'] - 0.0437
Rr = YP[('A', 'Base')]['r'][1] - YP[('A', 'Bear')]['r'][1]
out['ER'] = dict(E=E, R=Rr, ER=E / Rr)
print(f"  E/R reference: E {E*100:.1f}pp R {Rr*100:.1f}pp E/R {E/Rr:.3f}")

# ---------------- driver breakdown (Bear, Bull) ----------------
print("\nDRIVER BREAKDOWN")
for s in ('Bear', 'Bull'):
    # step 1: sector path (rates) with Base exit marks and Base tail rule; step 2: exit marks; (path A: no company item)
    r1 = run(s, 'A', exit_scen='Base', tail_on=False)
    d1 = decision(r1, 'A')
    d2 = decision(run(s, 'A'), 'A')
    out[f'drv_{s}'] = dict(step1=d1['irr'], step1_pk=d1['pk'], step2=d2['irr'], step2_pk=d2['pk'])
    print(f"  {s}: Base {out['A_Base']['irr']*100:.1f}% -> rates {d1['irr']*100:.1f}% (Pk {d1['pk']:.1f}) -> + exit marks and tail {d2['irr']*100:.1f}% (Pk {d2['pk']:.1f})")

# ---------------- Base return bridge (NOK/sh) ----------------
b = {k_: ns(v) for k_, v in br.items()}
d = R[('A', 'Base')]['d']
cash = ns(mf_after)
rb = dict(P=P_NOK, rerating=ns(n0['nav']) - P_NOK, cash_generated=cash, nb=b['nb_created'],
          ageing=b['own_age'] + b['opt_age'] + (ns(res['jv_T'] - n0['jv'])), jv_debt=ns(jvnd_val - res['jv_nd']),
          prem=b['prem'], tail=b['tail'])
rb['sum'] = sum(v for v in rb.values())
rb['target'] = d['sumD'] + d['vt']
print("\nBASE RETURN BRIDGE (NOK/sh):", {k_: round(v, 2) for k_, v in rb.items()})
out['retbridge'] = rb

# ---------------- attribution v7 -> v8 (steps in this engine, reversed from v8) ----------------
print("\nATTRIBUTION (reverse steps from v8, Base)")
v7bv = {'LR2': 450 / 547, 'LR1': 986 / 1078, 'MR': 1582 / 1634, 'Handy': 721 / 741, 'JV': 516 / 521}
steps = [
    ('v8 decision (path A)', dict(path='A')),
    ('path B: cash dividends, TORM held to exit (30 Sep TORM marks)', dict(path='B')),
    ('+ TORM exit on 30 Jun marks', dict(path='B', torm_jun=True)),
    ('+ fleet and JV exit values on 30 Jun broker values', dict(path='B', torm_jun=True, bv_scale=v7bv)),
    ('+ Q4-26 TCE scaled to v7 ($443m)', dict(path='B', torm_jun=True, bv_scale=v7bv, q4_scale=446.9 / 525.9)),
]
for lab, kw in steps:
    path = kw.pop('path')
    d = decision(run('Base', path, **kw), path)
    d98 = decision(run('Base', path, **kw), path, P=98.0, fx=9.340)
    print(f"  {lab:62s} at 90.00/9.624: IRR {d['irr']*100:5.1f}% Pk {d['pk']:5.1f} | at 98.00/9.340: IRR {d98['irr']*100:5.1f}% Pk {d98['pk']:5.1f}")
    out.setdefault('attrib', []).append((lab, d['irr'], d['pk'], d98['irr'], d98['pk']))

json.dump(out, open('results.json', 'w'), indent=1, default=str)
