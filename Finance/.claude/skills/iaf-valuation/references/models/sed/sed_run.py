"""SED Energy Holdings (docs/SED-analysis.md) v3.0, 27 Nov 2026 (Q3 report): decision figures, tables,
structural runs, exit cross-check, sensitivities, driver breakdown, return bridge, Step 6b, attribution
from the 27 Oct build. `py sed_run.py` (all), `py sed_run.py check` (reproduction of 27 Oct only).
Writes results.json beside this file."""
import sys, json, copy
from datetime import date, timedelta
from sed_model import *

SC = ('Bear', 'Base', 'Bull')
NOKP = {'Bear': {2026: 1.0, 2027: 1.12, 2028: 1.09, 2029: 1.09},
        'Bull': {2026: 1.0, 2027: 0.97, 2028: 0.97, 2029: 0.97}}   # Equity BBB 20 Nov USD/NOK path

def pct(x): return f"{x*100:+.1f}%"

def check():
    P = OLD(); out = {}
    for s in SC:
        d = decide(P, run(P, s)); out[s] = (round(d['irr'] * 100, 2), round(d['pk'], 3), round(d['VT'], 2))
    print('Reproduction of 27 Oct (doc: Bear -30.9% / 2.29, Base 6.7% / 6.03, Bull 27.1% / 9.41):', out)
    return out

def nd_at_vdate(P):
    R = run(P, 'Base'); q4 = R['rows'][0]
    return P['debt0'] - P['cash0'] - q4['fads'] * (P['vdate'] - D(2026, 10, 1)).days / 92

def yearly(R):
    out = {}
    for r in R['rows']:
        k = 'Q4-26' if r['y'] == 2026 else r['y']
        a = out.setdefault(k, {x: 0.0 for x in ('rev', 'ebitda', 'bb', 'ebitda_ab', 'mfcf', 'am', 'fads', 'decl', 'paid')})
        for x in a:
            a[x] += r[x]
        a['nd'] = r['nd']
    return out

def paid_by_year(P, R):
    out = {}
    for pd, x, _ in R['paid']:
        if P['vdate'] < pd <= EXIT:
            out[pd.year] = out.get(pd.year, 0) + x
    return out

def path(P, R, scen):
    """Year-end path: D_t paid (NOK/share), interim marks V_t, r_t, IRR to t."""
    marks = {2027: mark(P, R, scen, D(2027, 12, 31), 1 / 3),
             2028: mark(P, R, scen, D(2028, 12, 31), 2 / 3), 2029: R['VT']}
    # end-2026 mark identical in all scenarios: Base marks and firm-today contracts only
    Pb = P; Rb = run(P, 'Base')
    marks[2026] = mark(Pb, Rb, 'Base', D(2026, 12, 31), 0.0)
    dp = paid_by_year(P, R)
    rows = []; prev = P['price']; fl = [(0.0, -P['price'])]
    for y in (2026, 2027, 2028, 2029):
        Dt = per_share(P, dp.get(y, 0.0)); Vt = per_share(P, marks[y])
        r = (Dt + Vt - prev) / prev
        for pd, x, _ in R['paid']:
            if pd.year == y and P['vdate'] < pd <= EXIT:
                fl.append((yf(P['vdate'], pd), per_share(P, x)))
        irr_t = irr(fl + [(yf(P['vdate'], D(y, 12, 31)), Vt)]) if y > 2026 else None
        rows.append(dict(y=y, D=Dt, V=Vt, r=r, irr=irr_t))
        prev = Vt
    return rows

def fcf_norm(P, scen='Base', before_holdco=True, renewal=None):
    """Normalised Maintenance FCF at the scenario mid-cycle: full fleet, 2029 opex, idle 40% of opex,
    GHTH bareboat on working days, SeaBird, SG&A (holdco, left out if before_holdco), tax, maint capex 20,
    interest income on exit net cash ($m)."""
    v = P['val']; mcu = v['mcu'][scen]; esc = (1 + P['esc']) ** 3
    tot = 0.0; rev = 0.0
    for rig, typ in TYPE.items():
        ox = P['opex26'][typ] * esc; rate = v['mc'][scen][typ]
        tot += 365 * (mcu * (rate * 0.98 - ox) - (1 - mcu) * 0.40 * ox) / 1000
        rev += 365 * mcu * rate * 0.98 / 1000
        if rig == 'GHTH':
            tot -= 365 * mcu * P['bareboat'] / 1000
    sb = {'Bear': 5.0, 'Base': 10.0, 'Bull': 18.0}[scen]
    R = run(P, scen)
    nint = -R['nd_exit'] * (P['r_cash'] if R['nd_exit'] < 0 else P['r_debt'](2029))
    sga = 0.0 if before_holdco else P['sga'](2029, 1) * 4
    return tot + sb - sga - 0.064 * rev - 20.0 + nint

def book_exit(P, R):
    """Book equity at exit: 330.1 at 30 Sep 2026 + profit - distributions paid; profit = EBITDA after
    bareboat - tax - net interest - owned-asset D&A $38m a year (9M 2026 run-rate) [A]."""
    eq = 330.141
    for r in R['rows']:
        eq += r['ebitda_ab'] - r['tax'] - r['nint'] - 38.0 / 4 - r['paid']
    return eq

def main():
    check()
    P = Q3()
    P['nd_vdate'] = nd_at_vdate(P)
    res = {}
    print(f"\n=== {P['tag']}: P {P['price']} NOK, USD/NOK {P['fx']}, shares {P['shares']:.2f}m, vdate {P['vdate']}, T {yf(P['vdate'], EXIT):.3f}")
    print(f"ND at vdate {P['nd_vdate']:.1f}; T-16 mob fee {MOB_T16:.2f}")
    Rs = {s: run(P, s) for s in SC}
    for s in SC:
        R = Rs[s]; d = decide(P, R)
        dn = decide(P, R, (lambda y, s=s: NOKP[s][y]) if s != 'Base' else None)
        n0 = nav0(P, s)
        cum_mfcf = per_share(P, sum(r['mfcf'] for r in R['rows']))
        T = yf(P['vdate'], EXIT)
        dd = (d['sumD'] / T) / P['price']; g = (d['VT'] / P['price']) ** (1 / T) - 1; c = d['irr'] - dd - g
        nav0ps = per_share(P, n0['nav'])
        rer = (nav0ps / P['price']) ** (1 / T) - 1; navg = (d['VT'] / nav0ps) ** (1 / T) - 1
        Rst = run(P, s, struct=True); dst = decide(P, Rst)
        dst_d = (dst['sumD'] / T) / P['price']; dst_g = (dst['VT'] / P['price']) ** (1 / T) - 1
        res[s] = dict(irr=d['irr'], pk=d['pk'], mos=d['mos'], VT=d['VT'], sumD=d['sumD'],
                      cap=d['sumD'] + d['VT'], irr_nok=dn['irr'], cum_mfcf=cum_mfcf,
                      nd_exit_ps=per_share(P, R['nd_exit']), nd_exit=R['nd_exit'], nav0=n0, nav0ps=nav0ps,
                      d=dd, g=g, c=c, rer=rer, navg=navg, struct=dst['irr'], cyc=d['irr'] - dst['irr'],
                      dd=dd - dst_d, dg=g - dst_g, assets=R['tot_assets'], VTm=R['VT'])
        print(f"{s}: IRR {d['irr']*100:.1f}% | NOK path {dn['irr']*100:.1f}% | P_k {d['pk']:.2f} MoS {pct(d['mos'])} | V_T {d['VT']:.2f} ({R['VT']:.1f}m) | sumD {d['sumD']:.2f} | sumD+V_T {d['sumD']+d['VT']:.2f} ({(d['sumD']+d['VT'])/P['price']-1:+.0%}) | cum MFCF/sh {cum_mfcf:.2f} | ND exit {R['nd_exit']:.1f} ({per_share(P,R['nd_exit']):.2f}/sh)")
        print(f"    d/g/c {dd*100:.1f}% / {g*100:.1f}% / {c*100:+.1f} pp | NAV0 {n0['nav']:.1f} ({nav0ps:.2f}/sh, P/NAV0 {P['price']/nav0ps:.2f}x) rigs {n0['rigs']:.1f} prem {n0['prem']:.1f} ghth {n0['ghth']:.1f} | re-rating {rer*100:.1f}% NAV growth {navg*100:.1f}%")
        print(f"    structural {dst['irr']*100:.1f}% cyclical {(d['irr']-dst['irr'])*100:+.1f} pp (dd {(dd-dst_d)*100:+.1f}, dg {(g-dst_g)*100:+.1f})")
        print('    exit assets', {r: [round(x, 1) for x in v] for r, v in R['assets'].items()}, 'GHTH', [round(x, 1) for x in R['ghth']], 'SB', R['sbv'], 'tot', round(R['tot_assets'], 1))
        fo = decide(P, run(P, s, firm_only_exit=True))
        print(f"    firm-today only at exit: IRR {fo['irr']*100:.1f}% P_k {fo['pk']:.2f} V_T {fo['VT']:.2f}")
        res[s]['firm_only'] = (fo['irr'], fo['pk'], fo['VT'])
    # periods
    print('\n--- Period tables ($m; NOK/share)')
    for s in SC:
        R = Rs[s]; print(s)
        for r in R['rows'][:5]:
            lab = f"{r['y']}Q{r['q']}"
            print(f"  {lab}: rev {r['rev']:.1f} EBITDA {r['ebitda']:.1f} after bb {r['ebitda_ab']:.1f} MFCF {r['mfcf']:.1f} ({per_share(P,r['mfcf']):.2f}) am {r['am']:.1f} FADS {r['fads']:.1f} ({per_share(P,r['fads']):.2f}) decl {r['decl']:.1f} ({per_share(P,r['decl']):.2f}) paid {r['paid']:.1f} ND {r['nd']:.1f} ({per_share(P,r['nd']):.2f}) cash {r['cash']:.1f}")
        for y, a in yearly(R).items():
            print(f"  {y}: rev {a['rev']:.1f} EBITDA {a['ebitda']:.1f} ({per_share(P,a['ebitda']):.2f}) after bb {a['ebitda_ab']:.1f} ({per_share(P,a['ebitda_ab']):.2f}) MFCF {a['mfcf']:.1f} ({per_share(P,a['mfcf']):.2f}) am {a['am']:.1f} ({per_share(P,a['am']):.2f}) FADS {a['fads']:.1f} ({per_share(P,a['fads']):.2f}) decl {a['decl']:.1f} ({per_share(P,a['decl']):.2f}) paid {a['paid']:.1f} ({per_share(P,a['paid']):.2f}) ND {a['nd']:.1f} ({per_share(P,a['nd']):.2f})")
        print('  payments', [(str(a), round(x, 1), round(b, 1)) for a, x, b in R['paid'] if a > P['vdate']])
        mincash = min(r['cash'] for r in R['rows']); peak = max(r['nd'] for r in R['rows'])
        print(f"  min cash {mincash:.1f}, peak ND {peak:.1f}")
    print('\n--- Year-end path (NOK/share)')
    for s in SC:
        rows = path(P, Rs[s], s); res[s]['path'] = rows
        parts = []
        for r in rows:
            it = 'n.m.' if r['irr'] is None else f"{r['irr']*100:+.1f}%"
            parts.append(f"{r['y']}: D {r['D']:.2f} V {r['V']:.2f} r {r['r']*100:+.1f}% IRR {it}")
        print(s, ' | '.join(parts))
    # V_T bridge Base
    print('\n--- V_T bridge, Base ($m / NOK per share)')
    R = Rs['Base']; n0 = res['Base']['nav0']
    rigsT = sum(R['assets'][r][0] for r in OWNED)
    premF_T = sum(R['assets'][r][1] for r in OWNED) + R['ghth'][0]
    premS_T = sum(R['assets'][r][2] for r in OWNED) + R['ghth'][1]
    prem0 = n0['prem'] + n0['ghth']
    mcap_ps = P['price'] * P['shares'] / P['fx']
    steps = [('P (market cap incl. options)', mcap_ps), ('Re-rating P -> NAV_0', n0['nav'] - mcap_ps),
             ('NAV_0', n0['nav']), ('Ageing of owned fleet', rigsT - n0['rigs']),
             ('Roll-off firm-today premium', premF_T - prem0), ('Premium on Base-signed backlog', premS_T),
             ('Retained cash (ND change)', n0['nd'] - R['nd_exit']), ('V_T', R['VT'])]
    for lab, x in steps:
        print(f"  {lab}: {x:.1f} / {per_share(P, x):.2f}")
    print(f"  check: NAV0 + steps = {n0['nav'] + rigsT - n0['rigs'] + premF_T - prem0 + premS_T + n0['nd'] - R['nd_exit']:.1f}")
    # Base return bridge (NOK/share): P -> sumD + V_T
    d = res['Base']
    print(f"  Return bridge: P {P['price']:.2f} -> distributions {d['sumD']:.2f} + V_T {d['VT']:.2f} = {d['sumD']+d['VT']:.2f}")
    # exit cross-check
    print('\n--- Exit cross-check')
    for s in SC:
        R = Rs[s]
        mf = fcf_norm(P, s); ageing = sum(R['assets'][r][0] for r in OWNED) - nav0(P, s)['rigs']
        fn = mf + ageing / yf(P['vdate'], EXIT)
        bk = book_exit(P, R)
        print(f"  {s}: V_T {R['VT']:.1f}; norm MFCF before holdco {mf:.1f}; FCF_norm after renewal {fn:.1f} (ageing {ageing:.1f}); exit P/E {R['VT']/fn:.1f}x ({R['VT']/mf:.1f}x); book {bk:.0f}; P/B {R['VT']/bk:.2f}")
        res[s]['xc'] = dict(mf=mf, fn=fn, pe=R['VT'] / fn, pe_m=R['VT'] / mf, book=bk, pb=R['VT'] / bk)
        rr = {'Bear': 0.080, 'Base': 0.089, 'Bull': 0.092}[s]
        dx = decide(P, run(P, s, exit_r=rr))
        print(f"     exit marks at the Oslo mid-cycle return {rr*100:.1f}%: IRR {dx['irr']*100:.1f}% P_k {dx['pk']:.2f}")
        res[s]['xc_idx'] = (dx['irr'], dx['pk'])
    # Rule 3 (Base FCF_norm after holdco and renewal)
    R = Rs['Base']
    mfa = fcf_norm(P, 'Base', before_holdco=False)
    ageing = sum(R['assets'][r][0] for r in OWNED) - nav0(P, 'Base')['rigs']
    fna = mfa + ageing / yf(P['vdate'], EXIT)
    pfcf = P['price'] / per_share(P, fna)
    print(f"\n--- Rule 3: MFCF norm (after holdco) {mfa:.1f}, renewal {ageing/yf(P['vdate'],EXIT):.1f} -> {fna:.1f} = {per_share(P,fna):.2f}/sh; P/FCF {pfcf:.1f}x; ceilings " + ', '.join(f"{s} {res[s]['irr']/K**2:.1f}x" for s in SC))
    res['rule3'] = dict(mf=mfa, renewal=ageing / yf(P['vdate'], EXIT), fn=fna, pfcf=pfcf)
    # scenario-weighted reference (levels)
    fl = {s: decide(P, Rs[s])['flows'] for s in SC}
    tmap = {}
    for s, w in (('Bear', .25), ('Base', .5), ('Bull', .25)):
        for t, x in fl[s][1:]:
            tmap[round(t, 6)] = tmap.get(round(t, 6), 0) + w * x
    wf = [(0.0, -P['price'])] + sorted(tmap.items())
    print(f"\nScenario-weighted reference: IRR {irr(wf)*100:.1f}% P_k {pv(wf[1:], K):.2f}")
    res['weighted'] = (irr(wf), pv(wf[1:], K))
    print(f"Share of Bull priced: {(P['price']-res['Base']['pk'])/(res['Bull']['pk']-res['Base']['pk']):.0%}")
    # exit consistency: earnings basis gaps (2029 revenue per calendar day vs mid-cycle x MCU x RE) and tails
    print('\n--- Exit consistency')
    for s in SC:
        R = Rs[s]; v = P['val']
        out = []
        for rig in OWNED:
            typ = TYPE[rig]; rev = 0.0
            for g in R['sched'][rig]:
                a, b = max(g['s'], D(2029, 1, 1)), min(g['e'], D(2030, 1, 1))
                if g['kind'] == 'work' and b > a:
                    rev += g['rate'] * P['re'][s](2029) * (b - a).days
            eb = (rev / 365) / (v['mc'][s][typ] * v['mcu'][s] * 0.98) - 1
            out.append(f"{rig} {eb*100:+.0f}%")
        print(' ', s, 'earnings-basis gaps:', ', '.join(out))
    def tail_extra(basis):
        def f(P, s):
            P['tail_basis'] = basis
        return f
    # rate-basis tail ($m) on open days 2030-31: (Y3 - mc) x open days x RE x weights x (1 - tax)
    Y3 = {'Bear': {'barge': 65, 'semi': 95}, 'Base': {'barge': 85, 'semi': 125}, 'Bull': {'barge': 95, 'semi': 165}}
    tails = {}
    for s in SC:
        R = Rs[s]; tot = 0.0; v = P['val']
        for rig in OWNED:
            typ = TYPE[rig]; gap = Y3[s][typ] - v['mc'][s][typ]
            for yr, w in ((2030, (2 / 3) / 1.08), (2031, (1 / 3) / 1.08 ** 2)):
                busy = 0
                for g in R['sched'][rig]:
                    if g['kind'] != 'work':
                        continue
                    e = g['e'] if g['firm'] else min(g['e'], D(2032, 1, 1))
                    a, b = max(g['s'], D(yr, 1, 1)), min(e, D(yr + 1, 1, 1))
                    if b > a:
                        busy += (b - a).days
                open_d = 365 - busy
                if s == 'Bull' and rig == 'Vencedor':
                    open_d = 0
                tot += gap * open_d * 0.98 * w * (1 - 0.064) / 1000
        tails[s] = tot
        d0 = decide(P, Rs[s]); VTt = Rs[s]['VT'] + tot
        c = d0['flows'][:-1] + [(d0['flows'][-1][0], per_share(P, VTt))]
        print(f"  {s}: rate-basis tail {tot:+.1f}m -> IRR {irr(c)*100:.1f}% P_k {pv(c[1:], K):.2f}")
        res[s]['tail'] = (tot, irr(c), pv(c[1:], K))
    # sensitivities
    print('\n--- Sensitivities (Base)')
    sens = {}
    def S(lab, R, Px=None):
        Px = Px or P; d = decide(Px, R); sens[lab] = (d['irr'], d['pk']); print(f"  {lab}: IRR {d['irr']*100:.1f}% P_k {d['pk']:.2f}")
    for m in (0.8, 0.9, 1.1, 1.2):
        S(f'exit values x{m}', run(P, 'Base', exit_mult=m))
    be = solve(lambda m: decide(P, run(P, 'Base', exit_mult=m))['irr'], K, 0.5, 2.5)
    be0 = solve(lambda m: decide(P, run(P, 'Base', exit_mult=m))['irr'], 0.0, 0.2, 2.5)
    print(f"  break-even exit values x{be:.3f} (k), x{be0:.3f} (0%)"); sens['be'] = be; sens['be0'] = be0
    S('Base CF, Bear exit values', run(P, 'Base', exit_scen='Bear'))
    S('Base CF, Bull exit values', run(P, 'Base', exit_scen='Bull'))
    def vox(m):
        def f(P, s):
            P['val']['opex'] = {k: x * m for k, x in P['val']['opex'].items()}
        return f
    S('opex -10% (ops and values)', run(P, 'Base', opex_mult=0.9, extra=vox(0.9)))
    S('opex +10% (ops and values)', run(P, 'Base', opex_mult=1.1, extra=vox(1.1)))
    S('values at the 9M 2026 actual opex (x1.035)', run(P, 'Base', extra=vox(1.035)))
    S('ops opex at the 35/40 deck figures', run(P, 'Base', opex_mult=1 / 1.035))
    S('rig life 35 years', run(P, 'Base', life=35))
    S('opex -10% and 35-year life', run(P, 'Base', opex_mult=0.9, extra=vox(0.9), life=35))
    S('exit marks at Oslo mid-cycle 8.9%', run(P, 'Base', exit_r=0.089))
    for kk in (0.10, 0.13, 0.14):
        d = decide(P, Rs['Base'], k=kk); print(f"  k={kk}: P_k {d['pk']:.2f}"); sens[f'k{kk}'] = d['pk']
    # T-16 options not exercised (Bear schedule for T-16)
    sch = copy.deepcopy(P['sched']['Base']); sch['T-16'] = copy.deepcopy(P['sched']['Bear']['T-16'])
    S('T-16 options not exercised', run(P, 'Base', sched_override=sch))
    for rr in (85, 95):
        sch = copy.deepcopy(P['sched']['Base'])
        for g in sch['T-16']:
            if g['s'] == D(2030, 1, 15): g['rate'] = rr
        S(f'T-16 option rate {rr}', run(P, 'Base', sched_override=sch))
    sch = copy.deepcopy(P['sched']['Base'])
    for g in sch['T-16']:
        if g['s'] == D(2027, 2, 1): g['e'] = D(2027, 10, 15)
        if g['s'] == D(2027, 7, 15): g['s'] = D(2027, 10, 15)
    S('T-16 Phase 7 starts 3 months late', run(P, 'Base', sched_override=sch))
    sch = copy.deepcopy(P['sched']['Base'])
    for g in sch['EDrill-1']:
        if g['s'] == D(2027, 1, 1) and g['kind'] == 'work': g['kind'] = 'idle'; g['rate'] = 0
        if g['s'] == D(2027, 3, 1) and g['kind'] == 'idle': g['s'] = D(2027, 1, 1)
    sch['EDrill-1'] = [g for g in sch['EDrill-1'] if not (g['kind'] == 'idle' and g['s'] == D(2027, 1, 1) and g['e'] == D(2027, 3, 1))]
    S('EDrill-1 not bridged (idle Jan-Jun 2027)', run(P, 'Base', sched_override=sch))
    def h2(minv, date_=None):
        def f(P, s):
            P['h2_min'] = minv
            if date_: P['h2_date'] = date_
        return f
    S('H2-26 by the 90% rule only (no $40m floor)', run(P, 'Base', extra=h2(0.0)))
    S('H2-26 $50m (guidance mid)', run(P, 'Base', extra=h2(50.0)))
    S('H2-26 paid 15 Jun 2027', run(P, 'Base', extra=h2(40.0, D(2027, 6, 15))))
    def floor_(x):
        def f(P, s): P['floor'] = x
        return f
    S('cash floor $20m', run(P, 'Base', extra=floor_(20.0)))
    def payout(x):
        def f(P, s): P['payout'] = x
        return f
    S('payout 75%', run(P, 'Base', extra=payout(0.75)))
    S('payout 100%', run(P, 'Base', extra=payout(1.0)))
    def nowc(P, s): P['wc'] = lambda y, q: 0.0
    S('no working-capital unwind', run(P, 'Base', extra=nowc))
    for pr in (6.20, 6.40, 6.80, 7.00):
        Pp = Q3(price=pr); Pp['nd_vdate'] = P['nd_vdate']
        d = decide(Pp, run(Pp, 'Base')); print(f"  price {pr}: IRR {d['irr']*100:.1f}% P_k {d['pk']:.2f}"); sens[f'p{pr}'] = (d['irr'], d['pk'])
    Pf = Q3(fx=9.7247); Pf['nd_vdate'] = P['nd_vdate']
    d = decide(Pf, run(Pf, 'Base')); print(f"  USD/NOK 9.7247 (27 Nov 07:15 UTC): IRR {d['irr']*100:.1f}% P_k {d['pk']:.2f}"); sens['fx27'] = (d['irr'], d['pk'])
    res['sens'] = sens
    # flat new-barge rate x exit values grid (EDrill-1 and T-15 new contracts and 2029 re-lets)
    print('\n--- Grid: flat rate on new barge contracts (EDrill-1, T-15) x exit values, IRR %')
    grid = {}
    for rate in (65, 70, 75, 80, 85, 90, 95, 100):
        sch = copy.deepcopy(P['sched']['Base'])
        for rig in ('EDrill-1', 'T-15'):
            for g in sch[rig]:
                if g['kind'] == 'work' and not g['firm'] and g['s'] >= D(2027, 6, 1):
                    g['rate'] = rate
        row = []
        for m in (0.6, 0.8, 1.0, 1.2, 1.4):
            row.append(round(decide(P, run(P, 'Base', sched_override=sch, exit_mult=m))['irr'] * 100, 1))
        grid[rate] = row; print(f"  ${rate}k: {row}")
    res['grid'] = grid
    # driver breakdown Bear / Bull
    print('\n--- Driver breakdown')
    for s in ('Bear', 'Bull'):
        steps = []
        sch = copy.deepcopy(P['sched']['Base'])
        for rig in ('EDrill-1', 'T-15', 'T-16', 'EDrill-2'):
            sch[rig] = copy.deepcopy(P['sched'][s][rig])
        d1 = decide(P, run(P, 'Base', sched_override=sch, re_scen=s))
        steps.append(('1 barge rates, idle and RE (sector row)', d1['irr'], d1['pk']))
        sch2 = copy.deepcopy(P['sched'][s])
        d2 = decide(P, run(P, 'Base', sched_override=sch2, re_scen=s))
        steps.append(('2 + semi-tenders (Vencedor, GHTH)', d2['irr'], d2['pk']))
        d3 = decide(P, run(P, s, sched_override=sch2, re_scen=s, sb_scen='Base', exit_scen=s, extra=lambda P, x: P.__setitem__('sbx_scen', 'Base')))
        steps.append(('3 + exit marks at the scenario mid-cycle', d3['irr'], d3['pk']))
        d4 = decide(P, Rs[s])
        steps.append(('4 + SeaBird (contribution and value)', d4['irr'], d4['pk']))
        res[s]['drivers'] = steps
        print(s, ' | '.join(f"{a}: {b*100:.1f}% / {c:.2f}" for a, b, c in steps))
    # Step 6b: price-implied exit marks
    vk = solve(lambda m: decide(P, run(P, 'Base', exit_mult=m))['irr'], K, 0.5, 2.5)
    print(f"\nStep 6b: price implies exit marks x{vk:.3f} Base mid-cycle for k")
    res['implied'] = vk
    # attribution from the 27 Oct build
    print('\n--- Attribution 27 Oct build -> 27 Nov')
    att = attribution()
    res['attr'] = att
    res['P'] = dict(price=P['price'], fx=P['fx'], shares=P['shares'], nd_vdate=P['nd_vdate'])
    json.dump(res, open('results.json', 'w'), indent=1, default=str)

def solve(fn, tgt, lo, hi):
    up = fn(hi) > fn(lo)
    for _ in range(60):
        m = (lo + hi) / 2
        if (fn(m) > tgt) == up: hi = m
        else: lo = m
    return m

def attribution():
    """Cumulative steps from the 27 Oct build to the 27 Nov build (Base IRR / P_k)."""
    out = []
    def rep(lab, P):
        P = copy.deepcopy(P)
        if P.get('nd_vdate') is None:
            P['nd_vdate'] = nd_at_vdate(P)
        d = decide(P, run(P, 'Base')); out.append((lab, d['irr'], d['pk'], d['mos']))
        print(f"  {lab}: IRR {d['irr']*100:.2f}% P_k {d['pk']:.3f} MoS {pct(d['mos'])}")
    P = OLD(); rep('27 Oct build (6.80, 9.32, 27 Oct)', P)
    P['vdate'] = D(2026, 11, 27); P['known_dist'] = [(D(2026, 8, 15), 25.0), (D(2026, 12, 11), 25.0)]
    rep('+ valuation date 27 Nov, Q2 paid 11 Dec', P)
    P['fx'] = 9.755; rep('+ USD/NOK 9.755', P)
    Q = Q3(price=6.80)
    # Q3 actual balance sheet with the old H2 schedule (Q3 at 90% of actual, Feb; Q4 May), old costs and contracts
    A = copy.deepcopy(P)
    A['start'] = Q['start']; A['debt0'] = Q['debt0']; A['cash0'] = Q['cash0']; A['q3_fads'] = Q['q3_fads']
    A['known_dist'] = [(D(2026, 12, 11), 25.0), (pay_date(2026, 3), 0.9 * Q['q3_fads'])]
    A['seabird'] = Q['seabird']; A['sched'] = sched_old(); A['nd_vdate'] = None
    rep('+ Q3 actuals (30 Sep balance sheet, Q3 cash)', A)
    B = copy.deepcopy(A)
    B['floor'] = Q['floor']; B['carry'] = True; B['h2_min'] = Q['h2_min']; B['h2_date'] = Q['h2_date']
    B['known_dist'] = [(D(2026, 12, 11), 25.0)]; B['declare'] = Q['declare']
    B['payout'] = 0.9
    rep('+ H2 distributions deferred to 15 Apr 2027 (min $40m, floor $25m)', B)
    C = copy.deepcopy(B); C['sched'] = Q['sched']; C['rev_events'] = Q['rev_events']
    rep('+ contracts (T-16 $131k to Jan, Phase 7 $90k + mob; T-15 to Feb)', C)
    E = copy.deepcopy(C); E['opex26'] = Q['opex26']; rep('+ operating opex at the 9M actual (x1.035)', E)
    F = copy.deepcopy(E); F['sga'] = Q['sga']; F['r_debt'] = Q['r_debt']; F['wc'] = Q['wc']; F['amort'] = Q['amort']
    rep('+ SG&A guidance ~$4m a quarter, SOFR, working capital, amortisation', F)
    G = copy.deepcopy(F); G['shares'] = Q['shares']; rep('+ options at NOK 3.92 strike (shares)', G)
    Hh = Q3(); rep('+ price 6.60 (27 Nov build)', Hh)
    return out

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'check':
        check()
    else:
        main()
