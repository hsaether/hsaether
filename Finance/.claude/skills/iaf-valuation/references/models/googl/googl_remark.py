"""googl_remark.py - docs/googl-analysis.md, version 2.2 (20 Nov 2026), iaf-valuation 2026-11-18.1.

Re-mark layer on version 2's published per-share streams (the period tables of the 7 Nov
re-mark): core EPS 2027-30, average and year-end shares, year-end net cash, dividends at
payment dates, equity stakes after tax, exit P/E and the interim P/E glide. The v2 segment
model (Services, Cloud, margins, capex) was not kept; the next full run (Q4 report, early
Feb 2027) rebuilds it here. Operating sensitivities are carried as the V_T change each row
had in the 7 Nov table (backed out from its IRR at the 7 Nov base).

Run from this folder (standard library):
    py googl_remark.py          20 Nov re-mark: 19 Nov close, Anthropic at ANT, placement paid
    py googl_remark.py V7NOV    reproduces the 7 Nov figures (Base 9.1%, P_k 262.3, E / R 0.103)
"""
import sys
from datetime import date

K = 0.12
EXIT = date(2029, 12, 31)
YEARS = (2027, 2028, 2029)
SH_YE = {2026: 12460, 2027: 12570, 2028: 12680, 2029: 12790}      # m, year-end
SH_AV = {2027: 12515, 2028: 12625, 2029: 12735, 2030: 12845}      # m, average
EPS7 = {'bear': [10.47, 9.83, 11.01, 12.34],                     # 2027-30, 7 Nov
        'base': [12.67, 14.29, 15.90, 17.45],
        'bull': [13.81, 16.67, 18.98, 21.40]}
NC7 = {'bear': [-48.4, -46.3, -17.0],                             # $bn year-end 2027-29
       'base': [-51.7, -101.0, -110.2],
       'bull': [-78.7, -169.5, -229.2]}
FCF7 = {'bear': [-3.25, 2.41, 4.48], 'base': [-2.85, -0.95, 2.21], 'bull': [-4.49, -3.68, -1.15]}
PE_X = {'bear': 16.0, 'base': 21.0, 'bull': 24.0}
STK_X = {'bear': 0.5, 'base': 1.0, 'bull': 1.5}                    # stake mark at exit
DIVG = {'bear': 0.0, 'base': 0.05, 'bull': 0.10}
FX = {'bear': {2026: 1.0, 2027: 10.41 / 9.29, 2028: 10.14 / 9.29, 2029: 10.14 / 9.29},
      'base': {2026: 1.0, 2027: 1.0, 2028: 1.0, 2029: 1.0},
      'bull': {2026: 1.0, 2027: 9.02 / 9.29, 2028: 9.02 / 9.29, 2029: 9.02 / 9.29}}
TAX_STK = 0.21
EX_DATE = date(2026, 12, 7)
EPS26 = 11.35                                                     # CY26 core EPS


def stakes_after_tax(spcx, ant_px, ant_sh, other=6.67, meas_alt=None, cost=33.0):
    """$bn after 21% tax on the gain over cost. SpaceX 555.04m shares; other listed 6.67;
    Anthropic either at the measurement-alternative carrying value or ant_sh x ant_px."""
    spx = 555.04356 * spcx / 1000.0
    ant = meas_alt if meas_alt is not None else ant_sh * ant_px / 1000.0
    pre = spx + other + ant
    return pre - TAX_STK * (pre - cost), pre, spx, ant


def build(cfg):
    """cfg: P, vdate, stake0 ($bn after tax), nc0 ($bn at the valuation date), dnc (dict year ->
    $bn change in year-end net cash), deps (dict year -> EPS change), pe_x/stk_x overrides."""
    out = {}
    eps_b27 = EPS7['base'][0] + cfg['deps'].get(2027, 0.0)
    core0 = cfg['P'] - cfg['stake0'] * 1000 / SH_YE[2026] - cfg['nc0'] * 1000 / SH_YE[2026]
    pe0 = core0 / eps_b27
    for s in ('bear', 'base', 'bull'):
        eps = [EPS7[s][i] + cfg['deps'].get(2027 + i, 0.0) for i in range(4)]
        nc = [NC7[s][i] + cfg['dnc'].get(2027 + i, 0.0) for i in range(3)]
        pex = cfg.get('pe_x', {}).get(s, PE_X[s])
        stx = cfg.get('stk_x', {}).get(s, STK_X[s])
        stk_exit_bn = cfg.get('stk_exit', {}).get(s, cfg['stake0'] * stx)
        # dividends at payment dates
        divs = []
        if cfg['vdate'] < EX_DATE:
            divs.append((date(2026, 12, 14), 0.22))
        q = 0.22
        for y in YEARS:
            for m in (3, 6, 9, 12):
                if m == 6:
                    q *= 1 + DIVG[s]
                divs.append((date(y, m, 15), q))
        V = {2026: cfg['P']}
        pe_path = {2026: pe0}
        for j, y in enumerate(YEARS, start=1):
            if s == 'bear':                      # Bear: exit P/E and stake mark from end-2027
                pe_t, st_m = pex, stx
            else:
                pe_t = pe0 + (pex - pe0) * j / 3
                st_m = 1 + (stx - 1) * j / 3
            stk_t = cfg['stake0'] * st_m if y < 2029 else stk_exit_bn
            V[y] = pe_t * eps[j] + stk_t * 1000 / SH_YE[y] + nc[j - 1] * 1000 / SH_YE[y]
            pe_path[y] = pe_t
        VT = V[2029]
        D = {y: sum(a for d, a in divs if d.year == y) for y in (2026,) + YEARS}
        irr = xirr(cfg['P'], cfg['vdate'], divs, VT)
        irr_nok = xirr(cfg['P'], cfg['vdate'], [(d, a * FX[s][d.year]) for d, a in divs],
                       VT * FX[s][2029])
        pk = pv(K, cfg['vdate'], divs, VT)
        T = (EXIT - cfg['vdate']).days / 365
        sumD = sum(a for _, a in divs)
        dd = sumD / T / cfg['P']
        g = (VT / cfg['P']) ** (1 / T) - 1
        r = {2026: D[2026] / cfg['P']}
        irr_t = {2026: xirr(cfg['P'], cfg['vdate'], [x for x in divs if x[0].year == 2026],
                            cfg['P'], end=date(2026, 12, 31))}
        for y in YEARS:
            r[y] = (D[y] + V[y]) / V[y - 1] - 1
            irr_t[y] = xirr(cfg['P'], cfg['vdate'], [x for x in divs if x[0].year <= y], V[y],
                            end=date(y, 12, 31))
        r27_nok = (D[2027] * FX[s][2027] + V[2027] * FX[s][2027]) / cfg['P'] - 1
        out[s] = dict(eps=eps, nc=nc, V=V, VT=VT, D=D, sumD=sumD, irr=irr, irr_nok=irr_nok,
                      pk=pk, mos=pk / cfg['P'] - 1, d=dd, g=g, c=irr - dd - g, r=r,
                      irr_t=irr_t, r27_nok=r27_nok, pe=pe_path, divs=divs, T=T,
                      stk_exit_ps=stk_exit_bn * 1000 / SH_YE[2029],
                      nc_exit_ps=nc[2] * 1000 / SH_YE[2029], pex=pex,
                      g_eps=(eps[3] / eps_b27) ** (1 / T) - 1,
                      g_rr=(pex / pe0) ** (1 / T) - 1)
    out['pe0'] = pe0
    out['core0'] = core0
    out['eps_b27'] = eps_b27
    return out


def pv(rate, vdate, divs, VT):
    T = (EXIT - vdate).days / 365
    return sum(a / (1 + rate) ** ((d - vdate).days / 365) for d, a in divs if d > vdate) \
        + VT / (1 + rate) ** T


def xirr(P, vdate, divs, V, end=EXIT):
    T = (end - vdate).days / 365

    def f(r):
        return -P + sum(a / (1 + r) ** ((d - vdate).days / 365) for d, a in divs
                        if vdate < d <= end) + V / (1 + r) ** T
    lo, hi = -0.95, 3.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def er(res, nibor):
    E = res['base']['irr_nok'] - nibor
    R = res['base']['r'][2027] - res['bear']['r27_nok']
    return E / R, E, R


# ---------------------------------------------------------------- configurations
V7 = dict(P=284.78, vdate=date(2026, 11, 6), stake0=172.3, nc0=48.6, dnc={}, deps={})


def remark_cfg(P=272.66, vdate=date(2026, 11, 19), spcx=138.43, ant=97.17,
               ant_sh=1775.0, placement=10.0, rate=0.04, tax=0.17):
    """20 Nov re-mark. The $10bn Class N placement (120.48m at $83, closing 20 Nov) moves cash
    into the stake; the lost interest (4% on net cash, 17% tax) lowers EPS and net cash."""
    s_at, pre, spx, a = stakes_after_tax(spcx, ant, ant_sh, cost=33.0 + placement)
    dnc, deps = {}, {}
    lost_stub = placement * rate * (1 - tax) * (date(2026, 12, 31) - date(2026, 11, 20)).days / 365
    prev = -placement - lost_stub
    h = rate * (1 - tax) / 2
    for y in (2027, 2028, 2029, 2030):
        cur = prev * (1 + h) / (1 - h)
        dni = cur - prev                     # $bn, negative
        deps[y] = dni * 1000 / SH_AV[y]      # $bn -> $ a share (shares in m)
        if y <= 2029:
            dnc[y] = cur
        prev = cur
    cfg = dict(P=P, vdate=vdate, stake0=s_at, nc0=48.6 - placement, dnc=dnc, deps=deps)
    meta = dict(stake_pre=pre, spx=spx, ant=a, dnc26=-placement - lost_stub, lost_stub=lost_stub)
    return cfg, meta


def solve_price(cfg, target_fn, lo=150.0, hi=450.0):
    for _ in range(80):
        mid = (lo + hi) / 2
        c = dict(cfg, P=mid)
        if target_fn(build(c)) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def report(cfg, nibor, hyb, label, meta=None):
    res = build(cfg)
    print(f'=== {label}: P {cfg["P"]}, {cfg["vdate"]}, T {res["base"]["T"]:.3f}, '
          f'stakes {cfg["stake0"]:.2f}bn after tax, nc0 {cfg["nc0"]}bn, core P/E {res["pe0"]:.3f} '
          f'(core {res["core0"]:.2f}, EPS27 {res["eps_b27"]:.3f})')
    if meta:
        print('  meta', {k: round(v, 3) for k, v in meta.items()})
        print('  dnc', {k: round(v, 3) for k, v in cfg['dnc'].items()},
              'deps', {k: round(v, 4) for k, v in cfg['deps'].items()})
    for s in ('bear', 'base', 'bull'):
        x = res[s]
        print(f'  {s:4s} IRR {x["irr"]*100:6.2f}% NOK {x["irr_nok"]*100:6.2f}% P_k {x["pk"]:7.2f} '
              f'MoS {x["mos"]*100:6.1f}% V_T {x["VT"]:6.2f} sumD {x["sumD"]:.3f} '
              f'd/g/c {x["d"]*100:.2f}/{x["g"]*100:.2f}/{x["c"]*100:.2f} '
              f'gEPS {x["g_eps"]*100:.2f} gRR {x["g_rr"]*100:.2f}')
        print('        EPS', [round(e, 3) for e in x['eps']], 'nc', [round(n, 2) for n in x['nc']],
              'nc/sh', [round(x['nc'][i] * 1000 / SH_YE[2027 + i], 2) for i in range(3)])
        print('        V_t', {y: round(v, 2) for y, v in x['V'].items()},
              'PE', {y: round(v, 2) for y, v in x['pe'].items()},
              'D', {y: round(v, 3) for y, v in x['D'].items()})
        print('        r_t', {y: round(v * 100, 1) for y, v in x['r'].items()},
              'IRR to t', {y: round(v * 100, 1) for y, v in x['irr_t'].items()},
              f'r27 NOK {x["r27_nok"]*100:.1f}', f'stk/sh exit {x["stk_exit_ps"]:.2f}',
              f'nc/sh exit {x["nc_exit_ps"]:.2f}')
        cumf = sum(FCF7[s]) + sum(cfg['deps'].get(y, 0) for y in YEARS)
        print(f'        cum FCF 27-29/sh {cumf:.2f}; FCF29/sh {FCF7[s][2]+cfg["deps"].get(2029,0):.2f}; '
              f'capital {(x["sumD"]+x["VT"])/cfg["P"]-1:+.1%}')
    e, E, R = er(res, nibor)
    print(f'  E/R {e:.3f} (E {E*100:.2f} pp, R {R*100:.1f} pp); Rule 1 screen d+g: ' +
          ', '.join(f'{s} {res[s]["d"]*100:.2f}+{((res[s]["eps"][2]/EPS26)**(1/3)-1)*100:.2f}'
                    for s in ('bear', 'base', 'bull')))
    ref = 0.254
    t_er = solve_price(cfg, lambda r: er(r, nibor)[0] - ref)
    t_er2 = solve_price(cfg, lambda r: er(r, nibor)[0] - 0.216)
    t_pre = pv(hyb, cfg['vdate'], res['base']['divs'], res['base']['VT'])
    print(f'  triggers: Base=k {res["base"]["pk"]:.2f}; E/R 0.254 {t_er:.2f}; 0.216 {t_er2:.2f}; '
          f'pre-alert (Base={hyb*100:.1f}%) {t_pre:.2f}')
    w = {'bear': .25, 'base': .5, 'bull': .25}
    divs_w = [(d, sum(w[s] * dict(res[s]['divs'])[d] for s in w)) for d, _ in res['base']['divs']]
    vt_w = sum(w[s] * res[s]['VT'] for s in w)
    print(f'  scenario-weighted reference {xirr(cfg["P"], cfg["vdate"], divs_w, vt_w)*100:.2f}%; '
          f'share of Bull priced {(cfg["P"]-res["base"]["pk"])/(res["bull"]["pk"]-res["base"]["pk"]):.1%}')
    return res


def vt_from_irr(irr, cfg, s='base'):
    """V_T that gives this IRR at the cfg price (dividends of scenario s)."""
    res = build(cfg)
    divs = res[s]['divs']
    T = res[s]['T']
    pvd = sum(a / (1 + irr) ** ((d - cfg['vdate']).days / 365) for d, a in divs if d > cfg['vdate'])
    return (cfg['P'] - pvd) * (1 + irr) ** T


def sens(cfg, meta):
    base = build(cfg)
    VTb = base['base']['VT']
    P = cfg['P']
    divs = base['base']['divs']

    def row(name, VT, divs_=divs):
        irr = xirr(P, cfg['vdate'], divs_, VT)
        pk = pv(K, cfg['vdate'], divs_, VT)
        print(f'  {name:62s} IRR {irr*100:5.1f}%  P_k {pk:6.1f}  MoS {pk/P-1:+.1%}')
    print('=== sensitivities at', P)
    eps30 = base['base']['eps'][3]
    stk = base['base']['stk_exit_ps']
    ncx = base['base']['nc_exit_ps']
    for pe in (18, 24, 26):
        row(f'exit P/E {pe}', pe * eps30 + stk + ncx)
    # break-even exit P/E
    lo, hi = 10.0, 40.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if xirr(P, cfg['vdate'], divs, mid * eps30 + stk + ncx) < K:
            lo = mid
        else:
            hi = mid
    print(f'  break-even exit P/E {mid:.2f}')
    # EPS growth 2028-30 needed for 12% at exit P/E 21
    e27 = base['base']['eps'][0]
    lo, hi = 0.0, 0.5
    for _ in range(80):
        g = (lo + hi) / 2
        if xirr(P, cfg['vdate'], divs, 21 * e27 * (1 + g) ** 3 + stk + ncx) < K:
            lo = g
        else:
            hi = g
    print(f'  EPS growth 2028-30 for 12% (exit 21): {g*100:.1f}% (Base '
          f'{((eps30/e27)**(1/3)-1)*100:.1f}%)')
    # stakes
    row('equity stakes to zero', VTb - stk)
    row('equity stakes doubled', VTb + stk)
    for lab, px in (('Anthropic at the IPO price $83', 83.0), ('Anthropic at its IAF P_k $58.91', 58.91),
                    ('ANT $50', 50.0), ('ANT $150', 150.0)):
        s_at = stakes_after_tax(138.43, px, 1775.0, cost=43.0)[0]
        row(lab, VTb - stk + s_at * 1000 / SH_YE[2029])
    s_ct = stakes_after_tax(138.43, 0, 0, meas_alt=128.2 + 10.0, cost=43.0)[0]
    row('Anthropic at the old carrying value + $10bn placement at cost', VTb - stk + s_ct * 1000 / SH_YE[2029])
    # Anthropic at its own scenario V_T, SpaceX and other at the document's marks
    print('  Anthropic at its own scenario V_T (Bear 17.7 / Base 83.9 / Bull 176.6), rest at the marks:')
    spx_other_pre = 555.04356 * 138.43 / 1000 + 6.67
    for s, antv in (('bear', 17.7), ('base', 83.9), ('bull', 176.6)):
        pre = spx_other_pre * STK_X[s] + 1775.0 * antv / 1000
        s_at = pre - TAX_STK * (pre - 43.0)
        c2 = dict(cfg, stk_exit={s: s_at})
        r2 = build(c2)[s]
        print(f'     {s}: stake at exit {s_at:.1f}bn after tax; IRR {r2["irr"]*100:.1f}%  P_k {r2["pk"]:.1f}  '
              f'MoS {r2["mos"]:+.1%}  V_T {r2["VT"]:.1f}')
    # carried operating rows: V_T change from the 7 Nov table
    b7 = build(V7)
    VT7 = b7['base']['VT']
    rows7 = [('Cloud growth -5 pp every year', 0.070), ('Cloud growth +5 pp every year', 0.114),
             ('Cloud 2027 +70% (about consensus), then Base', 0.111),
             ('Cloud on the plain E2 row', 0.071),
             ('Services growth -2 pp every year', 0.068), ('Services growth +2 pp every year', 0.114),
             ('Segment margins -1 pp every year', 0.078), ('Segment margins +1 pp every year', 0.103),
             ('Capex +$25bn a year (2027 $300bn)', 0.081), ('Core tax 15%', 0.101),
             ('Waymo at its Feb-2026 round, Other Bets out of core EPS', 0.112),
             ('Q3-call Q4 items (Services +8.5%, Cloud margin 34%)', 0.0898)]
    for lab, irr7 in rows7:
        dV = vt_from_irr(irr7, V7) - VT7
        row(lab + f' [dV_T {dV:+.1f}]', VTb + dV)
    # AI BBB E-layer path, consensus CY27 14.91
    cons = 14.91
    vt_l = 21 * 1.27 * cons
    print(f'  E-layer path .92/1.07/1.17/1.27 x {cons}: headline {xirr(P, cfg["vdate"], divs, vt_l)*100:.1f}% '
          f'with stakes and net debt {xirr(P, cfg["vdate"], divs, vt_l + stk + ncx)*100:.1f}%; '
          f'Base EPS27 / cons {e27/cons:.3f}; EPS30 / path {eps30/(1.27*cons):.3f}')
    # capex -25bn in 2028-29 (K1 2028 watch call), mirror of 2/3 of the +25bn row [A]
    dV = -(vt_from_irr(0.081, V7) - VT7) * 2 / 3
    row(f'K1 2028 watch: capex -$25bn in 2028-29 (2/3 mirror of the +25bn row) [dV_T {dV:+.1f}]', VTb + dV)
    # prices
    for lab, px in (('post-market $273.30 (20 Nov 00:59 UTC)', 273.30), ('18 Nov close $282.44', 282.44)):
        c3 = dict(cfg, P=px)
        r3 = build(c3)['base']
        print(f'  {lab:62s} IRR {r3["irr"]*100:5.1f}%  P_k {r3["pk"]:6.1f}  MoS {r3["mos"]:+.1%}')


def drivers(cfg):
    """Driver breakdown Base -> Bear / Bull, one driver at a time."""
    print('=== driver breakdown')
    for s in ('bear', 'bull'):
        steps = [('Base', {})]
        steps.append((f'{s} earnings, cash and dividends (Base exit P/E, Base stakes)',
                      {'scen': s, 'pe': PE_X['base'], 'stk': 1.0}))
        steps.append((f'+ exit P/E {PE_X[s]:.0f}', {'scen': s, 'pe': PE_X[s], 'stk': 1.0}))
        steps.append((f'+ stakes x{STK_X[s]}', {'scen': s, 'pe': PE_X[s], 'stk': STK_X[s]}))
        for lab, o in steps:
            if not o:
                r = build(cfg)['base']
            else:
                c = dict(cfg, pe_x={o['scen']: o['pe']}, stk_x={o['scen']: o['stk']})
                r = build(c)[o['scen']]
            print(f'  {lab:70s} IRR {r["irr"]*100:6.1f}%  V_T {r["VT"]:6.1f}  P_k {r["pk"]:6.1f}')


def bridge(cfg):
    res = build(cfg)
    b = res['base']
    P = cfg['P']
    st0 = cfg['stake0'] * 1000 / SH_YE[2026]
    nc0 = cfg['nc0'] * 1000 / SH_YE[2026]
    core0 = res['core0']
    pe0 = res['pe0']
    e27, e30 = b['eps'][0], b['eps'][3]
    grow = pe0 * e30 - core0
    rr = (b['pex'] - pe0) * e30
    print('=== Base return bridge (per share)')
    print(f'  P {P:.2f} = core {core0:.2f} (P/E {pe0:.2f} x {e27:.3f}) + stakes {st0:.2f} + net cash {nc0:.2f}')
    print(f'  EPS growth {grow:+.2f}; re-rating {pe0:.2f} -> {b["pex"]} {rr:+.2f}; core at exit {b["pex"]*e30:.2f}')
    print(f'  stakes {st0:.2f} -> {b["stk_exit_ps"]:.2f} ({b["stk_exit_ps"]-st0:+.2f}); net cash {nc0:.2f} -> '
          f'{b["nc_exit_ps"]:.2f} ({b["nc_exit_ps"]-nc0:+.2f}); V_T {b["VT"]:.2f}; dividends {b["sumD"]:.2f}; '
          f'total {b["VT"]+b["sumD"]:.2f} ({(b["VT"]+b["sumD"])/P-1:+.1%})')


if __name__ == '__main__':
    if 'V7NOV' in sys.argv:
        report(V7, 0.0438, 0.072, '7 Nov reproduction')
    else:
        report(V7, 0.0438, 0.072, '7 Nov reproduction (check)')
        cfg, meta = remark_cfg()
        report(cfg, 0.0472, 0.075, '20 Nov re-mark', meta)
        # attribution steps
        print('=== attribution 7 Nov -> 20 Nov (Base IRR, P_k)')
        steps = [('7 Nov', V7),
                 ('+ date 19 Nov', dict(V7, vdate=date(2026, 11, 19)))]
        s_sp = stakes_after_tax(138.43, 0, 0, meas_alt=128.2, cost=33.0)[0]
        steps.append(('+ SPCX 134.27 -> 138.43', dict(V7, vdate=date(2026, 11, 19), stake0=s_sp)))
        c_ant, _ = remark_cfg(P=284.78, placement=0.0, ant_sh=1654.463)
        steps.append(('+ Anthropic 1,654.5m at ANT 97.17', c_ant))
        c_pl, _ = remark_cfg(P=284.78)
        steps.append(('+ placement ($10bn cash -> 120.48m shares; lost interest)', c_pl))
        steps.append(('+ price 272.66', cfg))
        for lab, c in steps:
            r = build(c)['base']
            print(f'  {lab:60s} IRR {r["irr"]*100:6.2f}%  P_k {r["pk"]:7.2f}  V_T {r["VT"]:7.2f}')
        sens(cfg, meta)
        drivers(cfg)
        bridge(cfg)
