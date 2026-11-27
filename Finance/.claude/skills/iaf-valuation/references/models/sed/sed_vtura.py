"""SED + Ventura Offshore pro forma (docs/SED-analysis.md v3.1, 27 Nov 2026).

Base = the combination closes (LOI 11 Sep: 605m new SED shares for 100% of Ventura; SED holders ~55%
fully diluted). SED's own flows come from the stored v3.0 engine (sed_model.Q3); Ventura is a rig-day
build on its Q3 2026 report (27 Nov) and contract announcements. Per original SED share: SED
distributions paid before closing in full; everything after closing (SED + Ventura distributions,
both V_T) at the combined share count. Standard library only: `py sed_vtura.py`.
Tags in comments: [F] filing, [E] press, [A] own assumption.
"""
import copy, json
from datetime import date as D, timedelta
from sed_model import (Q3, run, decide, yf, irr, pv, annuity, quarters, pay_date, EXIT, K, opt_shares)
from sed_run import nd_at_vdate

SC = ('Bear', 'Base', 'Bull')
CLOSE = D(2027, 3, 1)                 # LOI: closing Q1 2027 [A: 1 Mar]
NEW_SH = 605.0                        # LOI [F]; overrun/delay adjustments in sensitivities
END = D(2033, 1, 1)

def seg(s, e, kind, rate=0.0, firm=False):
    return dict(s=s, e=e, kind=kind, rate=rate, firm=firm)

# ---------------------------------------------------------------- Ventura rigs
BUILT = {'Carolina': 2011.5, 'Victoria': 2009.5, 'Catarina': 2011.5}   # [E/A] third-party data, to verify
KIND = {'Carolina': 'ds', 'Victoria': 'semi', 'Catarina': 'semi'}
J27 = D(2027, 1, 15)                                   # Petrobras start, "January 2027" [F]
C_END = J27 + timedelta(days=910)                      # DS Carolina firm 910 days [F] -> 13 Jul 2029
C_OPT = C_END + timedelta(days=305)                    # option 305 days, $113m [F]
V_END = J27 + timedelta(days=1455)                     # SSV Victoria 1,455 days [F]; Petrobras may end from day 910
V_910 = J27 + timedelta(days=910)

def sched(scen, start=J27):
    S = {}
    c_end = start + timedelta(days=910); c_opt = c_end + timedelta(days=305)
    v_end = start + timedelta(days=1455); v_910 = start + timedelta(days=910)
    pre = [seg(D(2026, 10, 1), start, 'project')]
    # DS Carolina: $363m incl. $26m mob over 910 days -> ~$370k [F/A]
    if scen == 'Bear':
        S['Carolina'] = pre + [seg(start, c_end, 'work', 370, True), seg(c_end, D(2030, 1, 1), 'idle'),
                               seg(D(2030, 1, 1), END, 'work', None)]
        S['Victoria'] = pre + [seg(start, v_910, 'work', 320, True), seg(v_910, D(2030, 3, 1), 'idle'),
                               seg(D(2030, 3, 1), END, 'work', None)]
        S['Catarina'] = [seg(D(2026, 10, 1), D(2026, 12, 15), 'work', 230, True),
                         seg(D(2026, 12, 15), D(2027, 9, 1), 'idle'),
                         seg(D(2027, 9, 1), D(2028, 9, 1), 'work', 205),
                         seg(D(2028, 9, 1), D(2029, 1, 1), 'idle'),
                         seg(D(2029, 1, 1), END, 'work', 205)]
    elif scen == 'Base':
        S['Carolina'] = pre + [seg(start, c_end, 'work', 370, True), seg(c_end, c_opt, 'work', 370),
                               seg(c_opt, END, 'work', None)]
        S['Victoria'] = pre + [seg(start, v_end, 'work', 320, True), seg(v_end, END, 'work', None)]
        S['Catarina'] = [seg(D(2026, 10, 1), D(2026, 12, 15), 'work', 230, True),
                         seg(D(2026, 12, 15), D(2027, 3, 1), 'idle'),
                         seg(D(2027, 3, 1), D(2028, 3, 1), 'work', 235),       # Eni tender 6+6 months [F/A]
                         seg(D(2028, 3, 1), D(2028, 6, 1), 'idle'),
                         seg(D(2028, 6, 1), D(2030, 6, 1), 'work', 245),
                         seg(D(2030, 6, 1), END, 'work', None)]
    else:
        S['Carolina'] = pre + [seg(start, c_end, 'work', 370, True), seg(c_end, c_opt, 'work', 370),
                               seg(c_opt, D(2032, 6, 1), 'work', 420)]
        S['Victoria'] = pre + [seg(start, v_end, 'work', 320, True), seg(v_end, END, 'work', None)]
        S['Catarina'] = [seg(D(2026, 10, 1), D(2026, 12, 15), 'work', 230, True),
                         seg(D(2026, 12, 15), D(2027, 2, 1), 'idle'),
                         seg(D(2027, 2, 1), D(2028, 2, 1), 'work', 250),
                         seg(D(2028, 2, 1), D(2031, 2, 1), 'work', 275)]
    return S

def VP(scen='Base'):
    """Ventura parameters ($m, $k/day)."""
    P = dict(
        opex=114.8,          # Q2 2026: $31.33m / 273 rig-days, all three working [F]
        esc=0.03, re=0.95,   # financial uptime 93.9% Q3 [F]; 95% convention
        idle_warm=0.65, idle_cold=0.35, project=0.40,   # project phase: crew and holding cost outside the capex budget [A]
        mgmt={'Bear': 12.0, 'Base': 16.0, 'Bull': 18.0}[scen],   # net management fees, Q3 run-rate 4.4/q [F]
        ga=26.0,             # G&A 6.6/q [F]
        tax=0.05,            # % of revenue [A] (effective 19% of pre-tax 9M [F]; Indonesia deemed profit)
        mcap={'ds': 6.0, 'semi': 5.0},   # in-horizon maintenance (SPS done in 2026; next ~2031) [A]
        mcap_exit={'ds': 14.0, 'semi': 12.0},   # normalised incl. 5-yearly SPS: 2026 project $168m for two rigs,
                                              # about half recurring [A]; Rig BBB convention 6 / 5 is for younger units
        proj_capex=[(D(2026, 12, 15), 95.0), (D(2027, 1, 31), 39.0)],   # $153m x 1.10 [F] less 34.2 paid [F]
        mob=[(J27, 26.0)],   # Carolina mobilisation fee [F]
        cash0=91.5 + 53.0,   # 30 Sep free cash [F] + bridge net of bond repayment and fees [F]
        debt0=250.0,         # bridge from 22 Oct 2026, bullet Sep 2027 [F]
        r_bridge=lambda d: 0.045 + 0.05 + 0.005 * sum(d >= x for x in (D(2027, 3, 1), D(2027, 5, 1), D(2027, 7, 1))),
        refi=D(2027, 7, 1), r_refi=0.090, amort=40.0,   # refinanced after commencement [F intent; A terms]
        r_cash=0.035, floor=30.0, payout=0.90,
        # mid-cycle at exit [A]: Rig BBB UDW 320 / 360 / 420 x ~0.86 (6th-gen, Brazil NOC market);
        # benign semi 260 / 300 / 340 x ~0.9 (2009-11 units, Brazil); Catarina on its SE Asia market
        # (Eni work at ~$232k in 2026 [A, derived from Q2/Q3 revenue])
        val=dict(mc={'Bear': {'ds': 275, 'semi': 230, 'cat': 200},
                     'Base': {'ds': 310, 'semi': 270, 'cat': 235},
                     'Bull': {'ds': 365, 'semi': 315, 'cat': 270}},
                 mcu={'Bear': {'ds': 0.82, 'semi': 0.68}, 'Base': {'ds': 0.88, 'semi': 0.78},
                      'Bull': {'ds': 0.92, 'semi': 0.85}},
                 r=0.08, life=30, floor=10.0, idle=0.40),
    )
    return P

def mc_key(rig):
    return 'cat' if rig == 'Catarina' else KIND[rig]

def mc_day(P, scen, rig, ox):
    v = P['val']; rate = v['mc'][scen][mc_key(rig)]; mcu = v['mcu'][scen][KIND[rig]]
    return mcu * (rate * P['re'] - ox) - (1 - mcu) * v['idle'] * ox - P['tax'] * mcu * rate * P['re']

def mc_value(P, scen, rig, a, ox, mult=1.0):
    v = P['val']; cf = 365 * mc_day(P, scen, rig, ox) / 1000 - P['mcap_exit'][KIND[rig]]
    n = v['life'] - a
    return max(v['floor'], cf * annuity(v['r'], n)) * mult if n > 0 else v['floor']

def age(rig, d):
    return d.year + (d.timetuple().tm_yday - 1) / 365.0 - BUILT[rig]

def run_v(scen, opex_mult=1.0, exit_mult=1.0, exit_scen=None, start=J27, extra=None, firm_only=False):
    P = VP(scen)
    if extra:
        extra(P)
    exit_scen = exit_scen or scen
    S = sched(scen, start)
    if extra and 'sched' in P:
        S = P['sched'](S)
    debt, cash = P['debt0'], P['cash0']
    rows, paid, pend = [], [], []
    for (y, q, s, e) in quarters(D(2026, 10, 1)):
        nd = (e - s).days
        ox = P['opex'] * opex_mult * (1 + P['esc']) ** (y - 2026)
        rev = opex = 0.0
        for rig, segs in S.items():
            for g in segs:
                a, b = max(g['s'], s), min(g['e'], e)
                if b <= a:
                    continue
                n = (b - a).days
                if g['kind'] == 'work':
                    rate = g['rate'] if g['rate'] is not None else P['val']['mc'][scen][mc_key(rig)]
                    util = 1.0 if g['rate'] is not None else P['val']['mcu'][scen][KIND[rig]] / 0.95 * 0.95
                    if g['rate'] is None:       # open market after the contract: mid-cycle rate at mid-cycle MCU
                        mcu = P['val']['mcu'][scen][KIND[rig]]
                        rev += rate * P['re'] * mcu * n
                        opex += ox * (mcu + (1 - mcu) * P['val']['idle']) * n
                    else:
                        rev += rate * P['re'] * n; opex += ox * n
                elif g['kind'] == 'project':
                    opex += ox * P['project'] * n
                elif g['kind'] == 'idle':
                    for i in range(n):
                        k = (a - g['s']).days + i
                        opex += ox * (P['idle_warm'] if k < 90 else P['idle_cold'])
        rev /= 1000; opex /= 1000
        mg = P['mgmt'] / 4 if y >= 2027 else 4.4
        ebitda = rev - opex + mg - P['ga'] / 4
        tax = P['tax'] * rev
        r = P['r_bridge'](s) if s < P['refi'] else P['r_refi']
        nint = debt * r * nd / 365 - cash * P['r_cash'] * nd / 365
        capex = sum(x for dd, x in P['proj_capex'] if s <= dd < e) + (sum(P['mcap'].values()) + 5.0) / 4 * (y >= 2027)
        mob = sum(x for dd, x in P['mob'] if s <= dd < e)
        am = P['amort'] / 4 if (y >= 2028) else 0.0
        fads = ebitda - tax - nint - capex + mob - am
        # distributions: 90% of FADS from Q2 2027 (after refinancing), lagged as SED's policy
        pay = 0.0
        for (pd, amt) in sorted([p for p in pend if s <= p[0] < e]):
            frac = (pd - s).days / nd
            x = max(0.0, min(amt, cash + fads * frac - pay - P['floor']))
            pay += x; paid.append((pd, x))
        pend = [p for p in pend if not (s <= p[0] < e)]
        if (y, q) >= (2027, 2):
            pend.append((pay_date(y, q), P['payout'] * max(0.0, fads)))
        cash += fads - pay; debt -= am
        rows.append(dict(y=y, q=q, rev=rev, opex=opex, ebitda=ebitda, tax=tax, nint=nint, capex=capex,
                         fads=fads, paid=pay, cash=cash, debt=debt, nd=debt - cash))
    nd_exit = debt - cash
    ox29 = P['opex'] * opex_mult * (1 + P['esc']) ** 3
    assets = {}
    for rig, segs in S.items():
        base = mc_value(P, exit_scen, rig, age(rig, EXIT), ox29, exit_mult)
        prem = 0.0
        for g in segs:
            if g['kind'] != 'work' or g['rate'] is None or g['e'] <= EXIT:
                continue
            if firm_only and not g['firm']:
                continue
            e2 = g['e'] if g['firm'] else min(g['e'], D(EXIT.year + 2, 12, 31))
            s2 = max(g['s'], EXIT); n = (e2 - s2).days
            day = (g['rate'] * P['re'] - ox29 - P['tax'] * g['rate'] * P['re']) - mc_day(P, exit_scen, rig, ox29)
            prem += day * sum((1 + P['val']['r']) ** -((s2 - EXIT).days / 365 + i / 365) for i in range(n)) / 1000
        assets[rig] = (base, prem)
    VT = sum(a + b for a, b in assets.values()) - nd_exit
    return dict(rows=rows, paid=paid, nd_exit=nd_exit, assets=assets, VT=VT, S=S, P=P)

# ---------------------------------------------------------------- combination per SED share
def combine(Ps, Rs, Rv, new_sh=NEW_SH, h2_to_sed=False):
    """Per original SED share (NOK): before CLOSE, SED distributions / SED diluted shares; after,
    (SED + Ventura) / (SED diluted + new shares). Ventura's own distributions before CLOSE stay with
    Ventura holders; its cash at CLOSE is inside Ventura's net debt path."""
    n0 = Ps['shares']; n1 = n0 + new_sh; fx = Ps['fx']
    c = [(0.0, -Ps['price'])]
    for (pd, x, _) in Rs['paid']:
        if Ps['vdate'] < pd <= EXIT:
            pre = pd < CLOSE or (h2_to_sed and pd == Ps.get('h2_date'))
            c.append((yf(Ps['vdate'], pd), x * fx / (n0 if pre else n1)))
    pre_v = sum(x for pd, x in Rv['paid'] if pd < CLOSE)
    for (pd, x) in Rv['paid']:
        if CLOSE <= pd <= EXIT:
            c.append((yf(Ps['vdate'], pd), x * fx / n1))
    VT = (Rs['VT'] + Rv['VT'] - pre_v * 0) * fx / n1
    c.append((yf(Ps['vdate'], EXIT), VT))
    c.sort()
    r = irr(c); pk = pv(c[1:], K)
    return dict(irr=r, pk=pk, mos=pk / Ps['price'] - 1, sumD=sum(x for _, x in c[1:-1]), VT=VT,
                share=n0 / n1, flows=c)

def ventura_alone(Rv, price_nok=30.9, fx=9.755, sh=105.935, vdate=D(2026, 11, 27)):
    """Ventura standalone at its own price: IRR and P_k per VTURA share (NOK)."""
    c = [(0.0, -price_nok)] + [(yf(vdate, pd), x * fx / sh) for pd, x in Rv['paid'] if vdate < pd <= EXIT]
    c.append((yf(vdate, EXIT), Rv['VT'] * fx / sh))
    return dict(irr=irr(c), pk=pv(c[1:], K))

def main():
    import sys
    price = float(sys.argv[1]) if len(sys.argv) > 1 else 6.58     # Oslo close 27 Nov (after the Q3 release)
    Ps = Q3(price=price); P0 = Q3(); Ps['nd_vdate'] = nd_at_vdate(P0)
    out = {'price': price}
    Rs = {s: run(Ps, s) for s in SC}
    Rv = {s: run_v(s) for s in SC}
    print(f"SED diluted shares {Ps['shares']:.1f}m + {NEW_SH}m new -> SED holders {Ps['shares']/(Ps['shares']+NEW_SH)*100:.1f}%")
    for s in SC:
        sa = decide(Ps, Rs[s]); cb = combine(Ps, Rs[s], Rv[s], h2_to_sed=(s == 'Bull'))
        va = ventura_alone(Rv[s])
        yr = {}
        for r in Rv[s]['rows']:
            d = yr.setdefault(r['y'], dict(rev=0, ebitda=0, fads=0, paid=0))
            for k_ in ('rev', 'ebitda', 'fads', 'paid'):
                d[k_] += r[k_]
            d['nd'] = r['nd']
        out[s] = dict(standalone=(sa['irr'], sa['pk'], sa['mos']), combined=(cb['irr'], cb['pk'], cb['mos']),
                      sumD=cb['sumD'], VT=cb['VT'], v_VT=Rv[s]['VT'], v_nd=Rv[s]['nd_exit'],
                      v_assets={k_: tuple(round(x, 1) for x in v) for k_, v in Rv[s]['assets'].items()},
                      s_VT=Rs[s]['VT'], v_years={y: {k_: round(v, 1) for k_, v in d.items()} for y, d in yr.items()},
                      vtura=(va['irr'], va['pk']))
        print(f"\n{s}: standalone IRR {sa['irr']*100:.1f}% P_k {sa['pk']:.2f} ({sa['mos']*100:+.1f}%) | "
              f"combined IRR {cb['irr']*100:.1f}% P_k {cb['pk']:.2f} ({cb['mos']*100:+.1f}%) sumD {cb['sumD']:.2f} VT {cb['VT']:.2f}")
        print(f"  Ventura V_T {Rv[s]['VT']:.0f} (assets {Rv[s]['assets']}, ND exit {Rv[s]['nd_exit']:.0f}); SED V_T {Rs[s]['VT']:.0f}")
        print(f"  Ventura alone at NOK 30.9: IRR {va['irr']*100:.1f}% P_k NOK {va['pk']:.1f}")
        for y, d in yr.items():
            print(f"   {y}: rev {d['rev']:.0f} EBITDA {d['ebitda']:.0f} FADS {d['fads']:.0f} paid {d['paid']:.0f} ND {d['nd']:.0f}")
    # sensitivities (Base combined)
    sens = {}
    def S(lab, Rv_=None, Rs_=None, **kw):
        cb = combine(Ps, Rs_ or Rs['Base'], Rv_ or Rv['Base'], **kw)
        sens[lab] = (round(cb['irr'] * 100, 1), round(cb['pk'], 2), round(cb['mos'] * 100, 1))
        print(f"  {lab}: IRR {cb['irr']*100:.1f}% P_k {cb['pk']:.2f} ({cb['mos']*100:+.1f}%)")
    print("\nSensitivities (Base, combined):")
    S('H2-26 to SED holders only', h2_to_sed=True)
    S('Ventura opex +20%', run_v('Base', opex_mult=1.2))
    S('Ventura opex +40%', run_v('Base', opex_mult=1.4))
    S('Ventura exit values x0.7', run_v('Base', exit_mult=0.7))
    S('Ventura exit values x0.5', run_v('Base', exit_mult=0.5))
    S('Ventura exit at Bear marks', run_v('Base', exit_scen='Bear'))
    def vict(P):
        P['sched'] = lambda S_: dict(S_, Victoria=[g for g in S_['Victoria'] if g['e'] <= V_910 or g['kind'] == 'project']
                                     + [seg(V_910, D(2030, 3, 1), 'idle'), seg(D(2030, 3, 1), END, 'work', None)])
    S('Petrobras ends Victoria at day 910', run_v('Base', extra=vict))
    S('Brazil starts 1 Apr 2027 (no share adjustment)', run_v('Base', start=D(2027, 4, 1)))
    S('Brazil starts 1 Apr 2027, shares cut for the delay', run_v('Base', start=D(2027, 4, 1)),
      new_sh=NEW_SH - 2 * 0.145 * 31 / (price / 9.755))
    S('Capex overrun adjustment (-$15m -> fewer shares)', new_sh=NEW_SH - 15.0 / (price / 9.755))
    gs = run_v('Base'); gs['VT'] -= (26.0 - 16.0) * 6
    S('Ventura net G&A x6 off V_T', gs)
    S('Bear SED + Base Ventura', Rs_=Rs['Bear'])
    S('Base SED + Bear Ventura', Rv['Bear'])
    out['sens'] = sens
    # price at which Base combined clears / fails
    lo, hi = 3.0, 15.0
    for _ in range(60):
        m = (lo + hi) / 2; P2 = Q3(price=m); P2['nd_vdate'] = Ps['nd_vdate']
        lo, hi = (m, hi) if combine(P2, run(P2, 'Base'), Rv['Base'])['irr'] > K else (lo, m)
    out['pk_price'] = m
    print(f'Base combined IRR = k at NOK {m:.2f}')
    def solve(f, t, lo, hi):
        for _ in range(50):
            mm = (lo + hi) / 2
            if (f(mm) - t) * (f(lo) - t) > 0: lo = mm
            else: hi = mm
        return mm
    be = dict(exit=solve(lambda x: combine(Ps, Rs['Base'], run_v('Base', exit_mult=x))['irr'], K, 0.2, 1.5),
              opex=solve(lambda x: combine(Ps, Rs['Base'], run_v('Base', opex_mult=x))['irr'], K, 0.8, 1.6),
              v_exit=solve(lambda x: ventura_alone(run_v('Base', exit_mult=x))['irr'], K, 0.05, 1.5),
              v_opex=solve(lambda x: ventura_alone(run_v('Base', opex_mult=x))['irr'], K, 0.8, 2.0))
    out['breakeven'] = be
    print('break-evens', {k_: round(v, 3) for k_, v in be.items()})
    json.dump(out, open('vtura_results.json', 'w'), indent=1, default=str)

if __name__ == '__main__':
    main()
