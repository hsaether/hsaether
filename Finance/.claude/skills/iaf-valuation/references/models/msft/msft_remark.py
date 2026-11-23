"""msft_remark.py - docs/msft-analysis.md, version 3.2 (20 Nov 2026), iaf-valuation 2026-11-18.1.

Re-mark layer on version 3's published per-share streams (the period tables of the 28 Oct build,
re-marked 7 Nov): EPS 2027-30, year-end net cash, dividends at payment dates, the AI-lab stakes,
the exit P/E and the interim P/E glide. Shares are held flat at 7,426.2m (buybacks offset SBC).
The v3 segment build (Azure, P&BP, margins, capex, FCF) was not kept as a script; the next full
run (Q2 FY27 report, ~27 Jan 2027) rebuilds it here. Operating sensitivities are carried as the
V_T change each row had in the v3 table (backed out from its IRR at the v3 base, 28 Oct).

Run from this folder (standard library):
    py msft_remark.py          20 Nov re-mark: 19 Nov close (ex-dividend), Anthropic placement,
                               HY NIBOR window 4.72%, pre-alert at the HY market Base 7.5%
    py msft_remark.py V7NOV    reproduces the 7 Nov re-mark (Base 9.6%, P_k 495.9, E / R 0.134)
"""
import sys
from datetime import date

K = 0.12
EXIT = date(2029, 12, 31)
YEARS = (2027, 2028, 2029)
SH = 7426.2                                                        # m, flat
EPS3 = {'bear': [18.18, 17.84, 19.16, 20.61],                     # 2027-30, v3
        'base': [20.77, 23.40, 26.11, 28.39],
        'bull': [22.03, 26.26, 30.37, 33.80]}
NC3 = {'bear': [20.5, 76.1, 146.3],                                # $bn year-end 2027-29
       'base': [19.0, 40.6, 86.6],
       'bull': [-2.3, -9.6, 9.8]}
FCF3 = {'bear': [5.52, 12.99, 15.18], 'base': [6.96, 10.24, 13.92], 'bull': [5.20, 7.47, 11.52]}
REV3 = {'base': [425.9, 487.2, 544.1, 592.3]}
PBP3 = [159.8, 175.8, 191.6, 207.0]                               # Base P&BP 2027-30 $bn
PE_X = {'bear': 18.0, 'base': 23.0, 'bull': 26.0}
STK_X = {'bear': 0.5, 'base': 1.0, 'bull': 1.5}                    # lab-stake mark at exit
DIVG = {'bear': 0.05, 'base': 0.09, 'bull': 0.10}                  # raised each December
FX = {'bear': {2026: 1.0, 2027: 1.12, 2028: 1.09, 2029: 1.09},     # Equity BBB NOK path (relative)
      'base': {2026: 1.0, 2027: 1.0, 2028: 1.0, 2029: 1.0},
      'bull': {2026: 1.0, 2027: 0.97, 2028: 0.97, 2029: 0.97}}
EX_DATE = date(2026, 11, 19)                                      # $0.98 paid 10 Dec 2026
EPS26 = 18.72
OPENAI = 0.24 * 852.0                                             # $bn, 24% x $852bn
CONS27 = 22.11                                                    # CY27 consensus, Yahoo 20 Nov


def build(cfg):
    """cfg: P, vdate, stake0 ($bn labs at the valuation date), nc0 ($bn at 31 Dec 2026), dnc
    (year -> $bn change in year-end net cash), deps (year -> EPS change), optional pe_x / stk_x /
    pe0_fix (keep today's glide while P moves) / dvt (scenario -> V_T change, $ a share)."""
    out = {}
    eps_b27 = EPS3['base'][0] + cfg['deps'].get(2027, 0.0)
    core0 = cfg['P'] - cfg['stake0'] * 1000 / SH - cfg['nc0'] * 1000 / SH
    pe0 = cfg.get('pe0_fix') or core0 / eps_b27
    for s in ('bear', 'base', 'bull'):
        eps = [EPS3[s][i] + cfg['deps'].get(2027 + i, 0.0) for i in range(4)]
        eps = [e + cfg.get('deps_s', {}).get(s, {}).get(2027 + i, 0.0) for i, e in enumerate(eps)]
        nc = [NC3[s][i] + cfg['dnc'].get(2027 + i, 0.0)
              + cfg.get('dnc_s', {}).get(s, {}).get(2027 + i, 0.0) for i in range(3)]
        pex = cfg.get('pe_x', {}).get(s, PE_X[s])
        stx = cfg.get('stk_x', {}).get(s, STK_X[s])
        divs = []
        if cfg['vdate'] < EX_DATE:
            divs.append((date(2026, 12, 10), 0.98))
        q = 0.98
        for y in YEARS:
            for m in (3, 6, 9, 12):
                if m == 12:
                    q *= 1 + DIVG[s]
                divs.append((date(y, m, 10), q))
        V = {2026: cfg['P']}
        pe_path = {2026: pe0}
        for j, y in enumerate(YEARS, start=1):
            if s == 'bear':                      # Bear: exit P/E and stake mark from end-2027
                pe_t, st_m = pex, stx
            else:
                pe_t = pe0 + (pex - pe0) * j / 3
                st_m = 1 + (stx - 1) * j / 3
            V[y] = pe_t * eps[j] + cfg['stake0'] * st_m * 1000 / SH + nc[j - 1] * 1000 / SH
            pe_path[y] = pe_t
        V[2029] += cfg.get('dvt', {}).get(s, 0.0)
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
        r27_nok = (D[2027] + V[2027]) * FX[s][2027] / cfg['P'] - 1
        out[s] = dict(eps=eps, nc=nc, V=V, VT=VT, D=D, sumD=sumD, irr=irr, irr_nok=irr_nok,
                      pk=pk, mos=pk / cfg['P'] - 1, d=dd, g=g, c=irr - dd - g, r=r,
                      irr_t=irr_t, r27_nok=r27_nok, pe=pe_path, divs=divs, T=T,
                      stk_exit_ps=cfg['stake0'] * stx * 1000 / SH,
                      nc_exit_ps=nc[2] * 1000 / SH, pex=pex,
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
V3 = dict(P=531.01, vdate=date(2026, 10, 28), stake0=OPENAI, nc0=19.0, dnc={}, deps={})
V7 = dict(P=530.61, vdate=date(2026, 11, 6), stake0=OPENAI, nc0=19.0, dnc={}, deps={})


def remark_cfg(P=498.30, vdate=date(2026, 11, 19), ant_px=97.17, ant_sh=12.05,
               placement=1.0, rate=0.04, tax=0.20, openai=OPENAI):
    """20 Nov re-mark. Microsoft's Anthropic placement (12.05m Class N at $83 = $1.0bn, closing
    20 Nov) moves cash into a stake marked at ANT; lost interest (4% on cash, 20% tax) lowers EPS
    and net cash. Stakes pre-tax, as for OpenAI."""
    ant = ant_sh * ant_px / 1000.0
    dnc, deps = {}, {}
    lost_stub = placement * rate * (1 - tax) * (date(2026, 12, 31) - date(2026, 11, 20)).days / 365
    prev = -placement - lost_stub
    h = rate * (1 - tax) / 2
    for y in (2027, 2028, 2029, 2030):
        cur = prev * (1 + h) / (1 - h)
        deps[y] = (cur - prev) * 1000 / SH
        if y <= 2029:
            dnc[y] = cur
        prev = cur
    cfg = dict(P=P, vdate=vdate, stake0=openai + ant, nc0=19.0 - placement - lost_stub,
               dnc=dnc, deps=deps)
    meta = dict(ant_bn=ant, ant_ps=ant * 1000 / SH, openai_ps=openai * 1000 / SH,
                nc0=19.0 - placement - lost_stub, lost_stub=lost_stub)
    return cfg, meta


def solve_price(cfg, target_fn, lo=300.0, hi=700.0, fix=True):
    pe0 = build(cfg)['pe0'] if fix else None
    for _ in range(80):
        mid = (lo + hi) / 2
        c = dict(cfg, P=mid)
        if fix:
            c['pe0_fix'] = pe0
        if target_fn(build(c)) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def report(cfg, nibor, hyb, label, meta=None):
    res = build(cfg)
    P = cfg['P']
    print(f'=== {label}: P {P}, {cfg["vdate"]}, T {res["base"]["T"]:.3f}, stakes {cfg["stake0"]:.2f}bn, '
          f'nc0 {cfg["nc0"]:.3f}bn, core {res["core0"]:.2f}, core P/E {res["pe0"]:.3f} (EPS27 {res["eps_b27"]:.4f})')
    if meta:
        print('  meta', {k: round(v, 4) for k, v in meta.items()})
    for s in ('bear', 'base', 'bull'):
        x = res[s]
        print(f'  {s:4s} IRR {x["irr"]*100:6.2f}% NOK {x["irr_nok"]*100:6.2f}% P_k {x["pk"]:7.2f} '
              f'MoS {x["mos"]*100:6.2f}% V_T {x["VT"]:6.2f} sumD {x["sumD"]:.3f} '
              f'd/g/c {x["d"]*100:.2f}/{x["g"]*100:.2f}/{x["c"]*100:.2f} '
              f'gEPS {x["g_eps"]*100:.2f} gRR {x["g_rr"]*100:.2f}')
        print('        EPS', [round(e, 3) for e in x['eps']], 'nc', [round(n, 2) for n in x['nc']],
              'nc/sh', [round(x['nc'][i] * 1000 / SH, 2) for i in range(3)])
        print('        V_t', {y: round(v, 1) for y, v in x['V'].items()},
              'PE', {y: round(v, 2) for y, v in x['pe'].items()},
              'D', {y: round(v, 3) for y, v in x['D'].items()})
        print('        r_t', {y: round(v * 100, 1) for y, v in x['r'].items()},
              'IRR to t', {y: round(v * 100, 1) for y, v in x['irr_t'].items()},
              f'r27 NOK {x["r27_nok"]*100:.1f}', f'stk/sh exit {x["stk_exit_ps"]:.2f}',
              f'nc/sh exit {x["nc_exit_ps"]:.2f}', f'capital {(x["sumD"]+x["VT"])/P-1:+.1%}')
        print(f'        FCF/sh {FCF3[s]} cum {sum(FCF3[s]):.2f}; P/FCF 27/29 {P/FCF3[s][0]:.1f} / {P/FCF3[s][2]:.1f}; '
              f'Rule 1 d+g {x["d"]*100:.1f}+{((x["eps"][2]/EPS26)**(1/3)-1)*100:.1f}; '
              f'Rule 3 ceiling {(x["d"]+((x["eps"][2]/EPS26)**(1/3)-1))/K**2*100/100:.1f}')
    e, E, R = er(res, nibor)
    print(f'  E/R {e:.3f} (E {E*100:.2f} pp, R {R*100:.1f} pp); P/E CY26 {P/EPS26:.1f}; CY27 cons {P/CONS27:.1f}; '
          f'core P/E on cons {res["core0"]/CONS27:.2f}')
    t_er = solve_price(cfg, lambda r: er(r, nibor)[0] - 0.254)
    t_er2 = solve_price(cfg, lambda r: er(r, nibor)[0] - 0.216)
    t_er3 = solve_price(cfg, lambda r: er(r, nibor)[0] - 0.254, fix=False)
    t_pre = pv(hyb, cfg['vdate'], res['base']['divs'], res['base']['VT'])
    print(f'  triggers: Base=k {res["base"]["pk"]:.2f}; E/R 0.254 {t_er:.2f} (re-glided {t_er3:.2f}); '
          f'0.216 {t_er2:.2f}; pre-alert (Base={hyb*100:.1f}%) {t_pre:.2f}')
    w = {'bear': .25, 'base': .5, 'bull': .25}
    divs_w = [(d, sum(w[s] * dict(res[s]['divs'])[d] for s in w)) for d, _ in res['base']['divs']]
    vt_w = sum(w[s] * res[s]['VT'] for s in w)
    print(f'  scenario-weighted reference {xirr(P, cfg["vdate"], divs_w, vt_w)*100:.2f}%; '
          f'share of Bull priced {(P-res["base"]["pk"])/(res["bull"]["pk"]-res["base"]["pk"]):.1%}')
    return res


def vt_from_irr(irr, cfg, s='base'):
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
        print(f'  {name:66s} IRR {irr*100:5.1f}%  P_k {pk:6.1f}  MoS {pk/P-1:+.1%}')
    print('=== sensitivities at', P)
    eps30 = base['base']['eps'][3]
    stk = base['base']['stk_exit_ps']
    ncx = base['base']['nc_exit_ps']
    for pe in (17, 20, 21, 26, 29):
        row(f'exit P/E {pe}', pe * eps30 + stk + ncx)
    lo, hi = 10.0, 40.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if xirr(P, cfg['vdate'], divs, mid * eps30 + stk + ncx) < K:
            lo = mid
        else:
            hi = mid
    print(f'  break-even exit P/E {mid:.2f}')
    e27 = base['base']['eps'][0]
    lo, hi = -0.2, 0.5
    for _ in range(80):
        g = (lo + hi) / 2
        if xirr(P, cfg['vdate'], divs, 23 * e27 * (1 + g) ** 3 + stk + ncx) < K:
            lo = g
        else:
            hi = g
    print(f'  EPS growth 2028-30 for 12% (exit 23): {g*100:.1f}% (Base {((eps30/e27)**(1/3)-1)*100:.1f}%)')
    # price-implied multiple of Base EPS 2028-30 at exit 23 (2027 kept)
    lo, hi = 0.5, 1.5
    for _ in range(80):
        m = (lo + hi) / 2
        c = dict(cfg, deps_s={'base': {y: (m - 1) * EPS3['base'][i] for i, y in ((1, 2028), (2, 2029), (3, 2030))}})
        if build(c)['base']['irr'] < K:
            lo = m
        else:
            hi = m
    print(f'  price-implied Base EPS 2028-30 multiple at exit 23: {m:.3f}x')
    oa = OPENAI * 1000 / SH
    row('OpenAI stake to zero', VTb - oa)
    row('OpenAI stake doubled', VTb + oa)
    oa125 = 0.24 * 1250 * 1000 / SH
    row('OpenAI at the reported $1.25tn first close (24%, undiluted) [E]', VTb - oa + oa125)
    row('OpenAI at $1.25tn diluted by a $20bn round (23.6%) [E]', VTb - oa + 0.24 * (1250 - 20) / 1250 * 1250 * 1000 / SH)
    ant = meta['ant_ps']
    row('Anthropic placement at the IPO price $83', VTb - ant + 12.05 * 83 / SH)
    row('Anthropic placement at its IAF P_k $58.91', VTb - ant + 12.05 * 58.91 / SH)
    # carried operating rows: V_T change from the v3 table (28 Oct base)
    b3 = build(V3)
    VT3 = b3['base']['VT']
    rows3 = [('Operating margin -1 pp every year', 0.087), ('Operating margin +1 pp every year', 0.103),
             ('Azure growth -5 pp every year', 0.069), ('Azure growth +5 pp every year', 0.123),
             ('Capex +$20bn a year 2027-29', 0.092), ('No finance-lease principal', 0.096)]
    for lab, irr3 in rows3:
        dV = vt_from_irr(irr3, V3) - VT3
        row(lab + f' [dV_T {dV:+.1f}]', VTb + dV)
    dV = -(vt_from_irr(0.092, V3) - VT3) * 2 / 3
    row(f'K1 2028 watch: capex -$20bn a year 2028-29, capex only [dV_T {dV:+.1f}]', VTb + dV)
    # T software watch: P&BP growth -3 pp a year 2028-30, group margin 45%, tax 20%
    p = [PBP3[0]]
    gr = [PBP3[i] / PBP3[i - 1] - 1 for i in (1, 2, 3)]
    for i in range(3):
        p.append(p[-1] * (1 + gr[i] - 0.03))
    dni = [(p[i] - PBP3[i]) * 0.45 * 0.8 for i in range(4)]
    deps = {2027 + i: dni[i] * 1000 / SH for i in range(4)}
    dnc = {2028: dni[1], 2029: dni[1] + dni[2]}
    c = dict(cfg, deps_s={'base': deps}, dnc_s={'base': dnc})
    rb = build(c)['base']
    lab = f'T watch: P&BP growth -3 pp a year 2028-30, 45 pct margin [dEPS30 {deps[2030]:+.2f}]'
    print(f'  {lab:66s} IRR {rb["irr"]*100:5.1f}%  P_k {rb["pk"]:6.1f}  MoS {rb["mos"]:+.1%}  V_T {rb["VT"]:.1f}')
    # AI BBB E-layer path x CY27 consensus
    for pe in (21, 23):
        vt_l = pe * 1.27 * CONS27 + stk + ncx
        print(f'  E-layer path .92/1.07/1.17/1.27 x {CONS27}, exit {pe}: {xirr(P, cfg["vdate"], divs, vt_l)*100:.1f}%')
    print('  Base EPS / CY27 cons', [round(e / CONS27, 3) for e in base['base']['eps']],
          'Bear', [round(e / CONS27, 2) for e in base['bear']['eps']],
          'Bull', [round(e / CONS27, 2) for e in base['bull']['eps']])
    for lab, px, vd in (('post-market $494.85 (20 Nov 00:59 UTC)', 494.85, cfg['vdate']),
                        ('18 Nov close $508.29 (cum-dividend)', 508.29, date(2026, 11, 18)),
                        ('19 Nov intraday high $526.49', 526.49, cfg['vdate'])):
        c3, _ = remark_cfg(P=px, vdate=vd)
        r3 = build(c3)['base']
        print(f'  {lab:66s} IRR {r3["irr"]*100:5.1f}%  P_k {r3["pk"]:6.1f}  MoS {r3["mos"]:+.1%}')


def drivers(cfg):
    print('=== driver breakdown')
    for s in ('bear', 'bull'):
        steps = [('Base', None),
                 (f'{s} earnings, cash and dividends (Base exit P/E, Base stake marks)',
                  {'pe': PE_X['base'], 'stk': 1.0}),
                 (f'+ exit P/E {PE_X[s]:.0f}', {'pe': PE_X[s], 'stk': 1.0}),
                 (f'+ stake marks x{STK_X[s]}', {'pe': PE_X[s], 'stk': STK_X[s]})]
        for lab, o in steps:
            if o is None:
                r = build(cfg)['base']
            else:
                r = build(dict(cfg, pe_x={s: o['pe']}, stk_x={s: o['stk']}))[s]
            print(f'  {lab:70s} IRR {r["irr"]*100:6.1f}%  V_T {r["VT"]:6.1f}  P_k {r["pk"]:6.1f}')


def bridge(cfg):
    res = build(cfg)
    b = res['base']
    P = cfg['P']
    st0 = cfg['stake0'] * 1000 / SH
    nc0 = cfg['nc0'] * 1000 / SH
    core0, pe0 = res['core0'], res['pe0']
    e27, e30 = b['eps'][0], b['eps'][3]
    grow = pe0 * e30 - core0
    rr = (b['pex'] - pe0) * e30
    print('=== Base return bridge (per share)')
    print(f'  P {P:.2f} = core {core0:.2f} (P/E {pe0:.3f} x {e27:.4f}) + stakes {st0:.2f} + net cash {nc0:.2f}')
    print(f'  EPS growth {grow:+.2f}; re-rating {pe0:.2f} -> {b["pex"]} {rr:+.2f}; core at exit {b["pex"]*e30:.2f}')
    print(f'  stakes {st0:.2f} -> {b["stk_exit_ps"]:.2f}; net cash {nc0:.2f} -> {b["nc_exit_ps"]:.2f} '
          f'({b["nc_exit_ps"]-nc0:+.2f}); V_T {b["VT"]:.2f}; dividends {b["sumD"]:.2f}; '
          f'total {b["VT"]+b["sumD"]:.2f} ({(b["VT"]+b["sumD"])/P-1:+.1%})')


if __name__ == '__main__':
    if 'V7NOV' in sys.argv:
        report(V7, 0.0438, 0.072, '7 Nov reproduction')
        report(V3, 0.0438, 0.072, 'v3 28 Oct reproduction')
    else:
        report(V7, 0.0438, 0.072, '7 Nov reproduction (check)')
        cfg, meta = remark_cfg()
        report(cfg, 0.0472, 0.075, '20 Nov re-mark', meta)
        print('=== attribution 7 Nov -> 20 Nov (Base IRR, P_k, MoS at each step\'s price)')
        steps = [('7 Nov', V7),
                 ('+ date 19 Nov, ex-dividend (the $0.98 leaves the stream), price 530.61',
                  dict(V7, vdate=date(2026, 11, 19)))]
        c_ant, _ = remark_cfg(P=530.61)
        steps.append(('+ Anthropic placement (stake at ANT 97.17, cash -1.0bn)', c_ant))
        steps.append(('+ price 498.30', cfg))
        for lab, c in steps:
            r = build(c)['base']
            print(f'  {lab:72s} IRR {r["irr"]*100:6.2f}%  P_k {r["pk"]:7.2f}  MoS {r["mos"]*100:6.2f}%  V_T {r["VT"]:7.2f}')
        r7 = build(V7)
        print(f'  E/R 7 Nov at NIBOR 4.72: {er(r7, 0.0472)[0]:.3f}')
        sens(cfg, meta)
        drivers(cfg)
        bridge(cfg)
