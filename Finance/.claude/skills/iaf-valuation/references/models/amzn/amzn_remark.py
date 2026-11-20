"""docs/amzn-analysis.md -- re-mark layer on the v2 build (Q3 2026 report, 30 Oct 2026).

Version 2.1, 20 Nov 2026 (iaf-valuation 2026-11-18.1). The v2 EPS / FCF / net-debt build was not kept
as a script; this layer starts from v2's published per-share streams (period tables of the document)
and re-marks price, valuation date and the AI stakes. Standard library only.

Run:  py amzn_remark.py            -> 20 Nov version (19 Nov close, Anthropic at market $97.17)
      py amzn_remark.py OLD        -> reproduces the 11 Nov figures (10 Nov close, carrying value)
      py amzn_remark.py DRIVERS    -> driver breakdown (Bear, Bull)
      py amzn_remark.py PATH       -> year-end path (V_t, core P/E, r_t, IRR to t)
"""
import math, sys
from datetime import date

K = 0.12
EXIT = date(2029, 12, 31)

# v2 build, per share (USD); year-end shares (bn) end-2026..2029
SH_YE = {2026: 10.950, 2027: 11.045, 2028: 11.140, 2029: 11.235}
SH_OUT = 10.813                                  # 10-Q cover, used for today's stake per share
ND_2026 = 6.20                                   # net debt per share end-2026 (all scenarios)
EPS_B27 = 9.69                                   # Base CY27 core EPS (today's core P/E basis)
SCN = {  # EPS 2028, 2029, 2030; net debt per share end-2027, -28, -29; exit P/E; stake factor at exit
    'Bear': dict(eps=[6.23, 7.05, 8.22], nd=[10.96, 11.10, 9.13], pe=17.0, sf=0.5),
    'Base': dict(eps=[11.28, 12.68, 14.00], nd=[11.25, 13.39, 12.29], pe=22.0, sf=1.0),
    'Bull': dict(eps=[13.07, 15.35, 17.73], nd=[14.64, 21.96, 25.82], pe=24.0, sf=1.5),
}
NOK_EXIT = {'Bear': 1.091, 'Base': 1.0, 'Bull': 0.971}     # Equity BBB 6 Nov relative moves
NOK_2027 = {'Bear': 1.121, 'Base': 1.0, 'Bull': 0.971}

ANT_COST, TAX, OPENAI = 18.0, 0.21, 50.0                    # $bn


def ant_after_tax(pre):
    return pre - TAX * (pre - ANT_COST)


def setup(old):
    if old:
        return dict(P=270.87, vd=date(2026, 11, 10), ant_pre=238.7, nibor=4.38, hy=7.2)
    return dict(P=257.37, vd=date(2026, 11, 19), ant_pre=3484.1 * 97.17 / 1000, nibor=4.72, hy=7.5)


def build(P, vd, ant_pre, stakes_override=None, pe_override=None, vt_add=0.0):
    T = (EXIT - vd).days / 365
    stakes_bn = ant_after_tax(ant_pre) + OPENAI if stakes_override is None else stakes_override
    st_today = stakes_bn / SH_OUT
    pe0 = (P - st_today + ND_2026) / EPS_B27
    out = {'T': T, 'pe0': pe0, 'st_today': st_today, 'stakes_bn': stakes_bn}
    for s, d in SCN.items():
        pe_x = d['pe'] if pe_override is None or s != 'Base' else pe_override
        path = []
        for i, yr in enumerate([2027, 2028, 2029]):
            st = stakes_bn / SH_YE[yr]
            if s == 'Bear':      # P/E 17 and stakes -50% from end-2027
                pe, sf = pe_x, d['sf']
            else:                # linear glide from today's core P/E and mark
                w = (i + 1) / 3
                pe = pe0 + (pe_x - pe0) * w
                sf = 1 + (d['sf'] - 1) * w
            path.append(pe * d['eps'][i] + st * sf - d['nd'][i])
        path[-1] += vt_add if s == 'Base' else 0.0
        vt = path[-1]
        irr = (vt / P) ** (1 / T) - 1
        pk = vt / (1 + K) ** T
        irr_nok = (vt * NOK_EXIT[s] / P) ** (1 / T) - 1
        r27 = path[0] / P - 1
        r27n = path[0] * NOK_2027[s] / P - 1
        out[s] = dict(path=path, vt=vt, irr=irr, pk=pk, mos=pk / P - 1, irr_nok=irr_nok,
                      r27=r27, r27n=r27n, cap=vt / P - 1)
    return out


def er(o, nibor):
    E = o['Base']['irr'] * 100 - nibor
    R = (o['Base']['r27'] - o['Bear']['r27n']) * 100
    return E, R, E / R


def solve(f, lo, hi):
    for _ in range(80):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def main():
    old = len(sys.argv) > 1 and sys.argv[1] == 'OLD'
    c = setup(old)
    P, vd, ap = c['P'], c['vd'], c['ant_pre']
    o = build(P, vd, ap)
    print(f"P {P}  date {vd}  T {o['T']:.3f}  core P/E today {o['pe0']:.2f}  stakes today/sh {o['st_today']:.2f}"
          f"  stakes after tax $bn {o['stakes_bn']:.1f}  Anthropic pre-tax {ap:.1f}")
    for s in ('Bear', 'Base', 'Bull'):
        x = o[s]
        print(f"{s}: V_t {[round(v, 1) for v in x['path']]}  IRR {x['irr']*100:.2f}%  NOK {x['irr_nok']*100:.1f}%"
              f"  P_k {x['pk']:.1f}  MoS {x['mos']*100:.1f}%  cap {x['cap']*100:+.1f}%  r27 {x['r27']*100:.1f}% (NOK {x['r27n']*100:.1f}%)")
    E, R, ratio = er(o, c['nibor'])
    print(f"E/R: E {E:.2f} pp  R {R:.1f} pp  ratio {ratio:.3f}  (NIBOR {c['nibor']})")
    T = o['T']
    # 25/50/25 on levels
    vw = 0.25 * o['Bear']['vt'] + 0.5 * o['Base']['vt'] + 0.25 * o['Bull']['vt']
    print(f"weighted ref {((vw / P) ** (1 / T) - 1)*100:.1f}%   Bull priced {(P - o['Base']['pk'])/(o['Bull']['pk'] - o['Base']['pk'])*100:.0f}%")
    # triggers
    for ref in (0.254, 0.216):
        p = solve(lambda q: er(build(q, vd, ap), c['nibor'])[2] - ref, 120, P * 1.2)
        print(f"price at E/R {ref}: {p:.1f} ({p/P-1:+.1%})")
    p = solve(lambda q: build(q, vd, ap)['Base']['irr'] * 100 - c['hy'], 150, 400)
    print(f"pre-alert (Base = HY {c['hy']}%): {p:.1f} ({p/P-1:+.1%})")
    # break-even exit P/E and EPS growth
    need = P * (1 + K) ** T
    st_x = o['stakes_bn'] / SH_YE[2029]
    pe_be = (need - st_x + SCN['Base']['nd'][2]) / SCN['Base']['eps'][2]
    eps_need = (need - st_x + SCN['Base']['nd'][2]) / SCN['Base']['pe']
    g_need = (eps_need / EPS_B27) ** (1 / 3) - 1
    print(f"break-even exit P/E {pe_be:.2f}; 2030 EPS needed at 22x {eps_need:.2f} ({eps_need/10.6575:.3f}x CY27 cons.), growth 2028-30 {g_need*100:.1f}%")
    # Base return bridge
    core0 = o['pe0'] * EPS_B27
    print(f"bridge: core {core0:.2f} + stakes {o['st_today']:.2f} - nd {ND_2026}; EPS growth {(14.00-EPS_B27)*o['pe0']:+.1f};"
          f" re-rating {(22-o['pe0'])*14.00:+.1f}; stakes at exit {st_x:.2f} ({st_x-o['st_today']:+.2f}); nd exit -12.29 ({-12.29+ND_2026:+.2f})")
    print(f"g: EPS {((14.00/EPS_B27)**(1/T)-1)*100:.1f}%  re-rating {((22/o['pe0'])**(1/T)-1)*100:.1f}%;"
          f" Bear EPS {((8.22/EPS_B27)**(1/T)-1)*100:.1f}% rr {((17/o['pe0'])**(1/T)-1)*100:.1f}%;"
          f" Bull EPS {((17.73/EPS_B27)**(1/T)-1)*100:.1f}% rr {((24/o['pe0'])**(1/T)-1)*100:.1f}%")
    if old:
        return
    # attribution 11 Nov -> 20 Nov
    co = setup(True)
    a0 = build(co['P'], co['vd'], co['ant_pre'])['Base']
    a1 = build(co['P'], co['vd'], ap)['Base']
    a2 = build(co['P'], vd, ap)['Base']
    a3 = o['Base']
    print(f"attrib: 11 Nov {a0['irr']*100:.2f}% P_k {a0['pk']:.1f} | stake {a1['irr']*100:.2f}% P_k {a1['pk']:.1f}"
          f" | date {a2['irr']*100:.2f}% P_k {a2['pk']:.1f} | price {a3['irr']*100:.2f}% P_k {a3['pk']:.1f}")
    # stake sensitivities (Base)
    def st(ant_pre=None, openai=OPENAI, mult=1.0):
        bn = (ant_after_tax(ant_pre if ant_pre is not None else ap) + openai) * mult
        return build(P, vd, ap, stakes_override=bn)['Base']
    rows = [('Anthropic at the $83 IPO price', st(3484.1 * 83 / 1000)),
            ('Anthropic at its own Base V_T $83.9', st(3484.1 * 83.9 / 1000)),
            ('Anthropic at its own P_k $58.91', st(3484.1 * 58.91 / 1000)),
            ('Anthropic at the 30 Sep carrying value $238.7bn', st(238.7)),
            ('Anthropic post-market $92.60', st(3484.1 * 92.60 / 1000)),
            ('Anthropic to zero', build(P, vd, ap, stakes_override=OPENAI)['Base']),
            ('Both stakes to zero', build(P, vd, ap, stakes_override=0.0)['Base']),
            ('Both stakes doubled', st(mult=2.0)),
            ('+ public equities and warrants ~$9bn', build(P, vd, ap, vt_add=9.0 / SH_YE[2029])['Base'])]
    for n, r in rows:
        print(f"  {n}: {r['irr']*100:.1f}%  P_k {r['pk']:.1f}  MoS {r['mos']*100:.1f}%")
    # Anthropic on its own scenario V_T in every scenario (Bear 17.7 / Base 83.9 / Bull 176.6)
    for s, v in (('Bear', 17.7), ('Base', 83.9), ('Bull', 176.6)):
        bn = ant_after_tax(3484.1 * v / 1000) + OPENAI * SCN[s]['sf']
        vt = SCN[s]['pe'] * SCN[s]['eps'][2] + bn / SH_YE[2029] - SCN[s]['nd'][2]
        print(f"  own-path {s}: V_T {vt:.1f}  IRR {((vt/P)**(1/T)-1)*100:.1f}%")
    # exit P/E rows
    for pe in (19, 21, 23, 25, 27):
        r = build(P, vd, ap, pe_override=pe)['Base']
        print(f"  exit P/E {pe}: {r['irr']*100:.1f}%  P_k {r['pk']:.1f}  MoS {r['mos']*100:.1f}%")
    # operating sensitivities: V_T backed out of the 11 Nov IRRs, plus the stake re-mark
    dst = (o['stakes_bn'] - (ant_after_tax(238.7) + OPENAI)) / SH_YE[2029]
    print(f"stake delta at exit {dst:.2f}/sh")
    ops = [('AWS growth -5 pp', 1.6), ('AWS growth +5 pp', 8.9), ('AWS on E2 Bull row', 9.3),
           ('AWS on management +40%/+40%', 8.3), ('same with more capex', 7.3),
           ('AWS margin -2 pp', 3.6), ('AWS margin +2 pp', 6.7), ('AWS margin held 37%', 8.5),
           ('Retail margin -1 pp', 3.4), ('Retail margin +1 pp', 6.8), ('Retail growth -2 pp', 4.2),
           ('Retail growth +2 pp', 6.1), ('Capex +$30bn a year', 3.6), ('Q4 capex at Q3 pace', 4.7),
           ('Core tax 21%', 6.1), ('Core tax 25%', 4.2)]
    for n, irr_old in ops:
        v_old = co['P'] * (1 + irr_old / 100) ** ((EXIT - co['vd']).days / 365)
        v = v_old + dst
        print(f"  {n}: {((v/P)**(1/T)-1)*100:.1f}%  P_k {v/(1+K)**T:.0f}  MoS {(v/(1+K)**T/P-1)*100:.1f}%")
    # post-market
    pm = 256.37
    r = build(pm, vd, ap)['Base']
    print(f"  post-market AMZN {pm}: {r['irr']*100:.1f}%  P_k {r['pk']:.1f}  MoS {r['mos']*100:.1f}%")
    # exit P/B and ROE (book per share at exit from v2: V_T / P/B, plus the after-tax stake re-mark)
    for s, pb_old, vt_old in (('Bear', 1.94, 141.4), ('Base', 3.26, 317.3), ('Bull', 3.78, 432.1)):
        bk = vt_old / pb_old + dst * SCN[s]['sf']
        print(f"  {s} book/sh {bk:.1f}  P/B {o[s]['vt']/bk:.2f}  ROE 2030 {SCN[s]['eps'][2]/bk*100:.1f}%")
    # E-layer consistency (AI BBB .92/1.07/1.17/1.27 x consensus 10.6575, exit P/E 21)
    v = 21 * 1.27 * 10.6575
    print(f"  E-layer: headline {((v/P)**(1/T)-1)*100:.1f}%  with stakes and net debt {(((v+o['stakes_bn']/SH_YE[2029]-12.29)/P)**(1/T)-1)*100:.1f}%")


if __name__ == '__main__' and not (len(sys.argv) > 1 and sys.argv[1] in ('DRIVERS', 'PATH')):
    main()


def drivers():
    """Driver breakdown (one driver at a time, Base -> scenario), on the exit value; approximate:
    2030 EPS = (AWS OI + retail OI - net interest) x 0.77 / 11.285bn, Base net interest 6.2 held in step 1."""
    c = setup(False)
    o = build(c['P'], c['vd'], c['ant_pre'])
    T, P = o['T'], c['P']
    st = o['stakes_bn'] / SH_YE[2029]
    irr = lambda v: ((v / P) ** (1 / T) - 1) * 100
    base = 22 * 14.00 + st - 12.29
    print(f"Base V_T {base:.1f} IRR {irr(base):.1f}%")
    for s, aws, eps, nd, pe, sf in (('Bear', 72.7, 8.22, 9.13, 17, 0.5), ('Bull', 172.9, 17.73, 25.82, 24, 1.5)):
        e1 = (aws + 82.0 - 6.2) * 0.77 / 11.285
        v1 = 22 * e1 + st - 12.29
        v2 = 22 * eps + st - nd
        v3 = pe * eps + st - nd
        v4 = pe * eps + st * sf - nd
        print(f"{s}: AWS EPS {e1:.2f} V {v1:.1f} {irr(v1):.1f}% | retail+capex V {v2:.1f} {irr(v2):.1f}% |"
              f" exit P/E V {v3:.1f} {irr(v3):.1f}% | stakes V {v4:.1f} {irr(v4):.1f}%")


if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'DRIVERS':
    drivers()


def year_end_path():
    """Year-end path: V_t, core P/E, r_t (USD; 2027 also NOK), IRR to each year-end."""
    c = setup(False)
    o = build(c['P'], c['vd'], c['ant_pre'])
    P, vd = c['P'], c['vd']
    ends = [date(2027, 12, 31), date(2028, 12, 31), date(2029, 12, 31)]
    for s in ('Bear', 'Base', 'Bull'):
        d = SCN[s]
        path = o[s]['path']
        pes = []
        for i in range(3):
            st = o['stakes_bn'] / SH_YE[2027 + i]
            sf = d['sf'] if s == 'Bear' else 1 + (d['sf'] - 1) * (i + 1) / 3
            pes.append((path[i] - st * sf + d['nd'][i]) / d['eps'][i])
        prev = P
        row = []
        for i, v in enumerate(path):
            t = (ends[i] - vd).days / 365
            row.append(f"{v:.1f} / P/E {pes[i]:.1f} / r {(v/prev-1)*100:.1f}% / IRR {((v/P)**(1/t)-1)*100:.1f}%")
            prev = v
        print(s, ' | '.join(row))


if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'PATH':
    year_end_path()
