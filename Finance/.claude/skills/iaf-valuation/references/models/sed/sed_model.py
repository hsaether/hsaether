"""SED Energy Holdings (docs/SED-analysis.md) - IAF Track B rig-day engine.

v3.0, 27 Nov 2026 (Q3 2026 report run). The 27 Oct rig-day build was not kept (only sed6b.py, a
re-mark layer), so this engine is rebuilt from the 27 Oct document's published inputs; `OLD`
reproduces the 27 Oct decision figures (see sed_run.py `check`). `Q3` is the 27 Nov build.
Standard library only. Run from this folder: `py sed_run.py`.
"""
from datetime import date, timedelta
import copy

D = date
EXIT = D(2029, 12, 31)
K = 0.12

# ---------------------------------------------------------------- helpers
def yf(a, b):
    return (b - a).days / 365.0

def add_months(d, m):
    y = d.year + (d.month - 1 + m) // 12
    mo = (d.month - 1 + m) % 12 + 1
    return D(y, mo, min(d.day, 28) if d.day > 28 else d.day)

def quarters(start, end_year=2029):
    qs = []
    y, q = start.year, (start.month - 1) // 3 + 1
    while y <= end_year:
        s = D(y, 3 * (q - 1) + 1, 1)
        e = D(y + (q == 4), (3 * q) % 12 + 1, 1)
        qs.append((y, q, s, e))
        q += 1
        if q == 5:
            q, y = 1, y + 1
    return qs

def annuity(r, n):
    return (1 - (1 + r) ** -n) / r if n > 0 else 0.0

def irr(flows):
    lo, hi = -0.95, 3.0
    for _ in range(200):
        m = (lo + hi) / 2
        v = sum(x / (1 + m) ** t for t, x in flows)
        lo, hi = (m, hi) if v > 0 else (lo, m)
    return m

def pv(flows, r):
    return sum(x / (1 + r) ** t for t, x in flows)

# ---------------------------------------------------------------- rig sets
TYPE = {'EDrill-1': 'barge', 'EDrill-2': 'barge', 'T-15': 'barge', 'T-16': 'barge',
        'Vencedor': 'semi', 'GHTH': 'semi'}
BUILT = {'EDrill-1': 2014.5, 'EDrill-2': 2014.5, 'T-15': 2012.5, 'T-16': 2013.5,
         'Vencedor': 2009.5}          # mid-year build convention: EDrill-1 is 15.5 at exit
OWNED = ['EDrill-1', 'EDrill-2', 'T-15', 'T-16', 'Vencedor']

def seg(s, e, kind, rate=0.0, firm=False):
    """Working ('work'), idle ('idle'), off-hire ('sps') or redelivered ('gone') from s to e (excl.).
    firm=True: contract signed on the valuation date (firm today)."""
    return dict(s=s, e=e, kind=kind, rate=rate, firm=firm)

# ---------------------------------------------------------------- engine
def age(rig, d):
    return d.year + (d.timetuple().tm_yday - 1) / 365.0 - BUILT[rig]

def mc_day(P, scen, typ):
    """Mid-cycle day on the Rig BBB asset convention ($k/day), before maintenance capex."""
    v = P['val']
    rate = v['mc'][scen][typ]; mcu = v['mcu'][scen]; ox = v['opex'][typ]
    return mcu * (rate * v['re'] - ox) - (1 - mcu) * v['idle'] * ox - v['tax'] * mcu * rate * v['re']

def mc_value(P, scen, typ, a, mult=1.0):
    v = P['val']
    cf = 365 * mc_day(P, scen, typ) / 1000 - v['mcap'][typ]
    life = v.get('life', 30)
    return max(v['floor'], cf * annuity(v['r'], life - a)) * mult if life - a > 0 else v['floor']

def contract_day(P, typ, rate, bareboat=0.0):
    v = P['val']
    return rate * v['re'] - v['opex'][typ] - v['tax'] * rate * v['re'] - bareboat

def backlog_value(P, rig, segs, d0, scen_mc, cap_scen, struct=False, scen=None, mcday=None):
    """PV at d0 ($m) of contract margin over the mid-cycle day on work segments running at d0.
    Firm-today segments in full; scenario-signed ones to d0 + 2 years. GHTH (chartered): full
    margin after bareboat, no mid-cycle deduction."""
    v = P['val']; typ = TYPE[rig]; tot = 0.0
    cap = D(d0.year + 2, d0.month, d0.day) if cap_scen else None
    base_day = mcday if mcday is not None else mc_day(P, scen_mc, typ)
    for sg in segs:
        if sg['kind'] != 'work' or sg['e'] <= d0:
            continue
        s = max(sg['s'], d0); e = sg['e']
        if not sg['firm'] and cap is not None:
            e = min(e, cap)
        if e <= s:
            continue
        rate = sg['rate']
        if struct and not sg['firm']:
            rate = v['mc'][scen][typ]
        if rig == 'GHTH':
            pday = contract_day(P, typ, rate, P['bareboat'])
        else:
            pday = contract_day(P, typ, rate) - base_day
        # daily discounting at the asset rate
        n = (e - s).days; t0 = yf(d0, s)
        disc = sum((1 + v['r']) ** -(t0 + i / 365.0) for i in range(n))
        tot += pday * disc / 1000
    return tot

def run(P, scen, struct=False, opex_mult=1.0, exit_mult=1.0, exit_scen=None, life=None,
        firm_only_exit=False, exit_r=None, sched_override=None, extra=None, re_scen=None,
        sb_scen=None):
    """Quarterly cash flows Q(start) .. Q4-29, D_t at payment dates, V_T and marks ($m)."""
    P = copy.deepcopy(P)
    if life:
        P['val']['life'] = life
    if exit_r:
        P['val']['r'] = exit_r
    if extra:
        extra(P, scen)
    sched = sched_override or P['sched'][scen]
    exit_scen = exit_scen or scen
    re_scen = re_scen or scen
    sb_scen = sb_scen or scen
    qs = quarters(P['start'])
    debt, cash = P['debt0'], P['cash0']
    rows = []
    pend = list(P['known_dist'])                     # (pay date, $m) already declared
    paid_list = []
    carry = []
    ox26 = {k: x * opex_mult for k, x in P['opex26'].items()}
    for (y, q, s, e) in qs:
        nd = (e - s).days
        esc = (1 + P['esc']) ** (y - 2026)
        rev = opex = bb = 0.0
        for rig, segs in sched.items():
            typ = TYPE[rig]; oxd = ox26[typ] * esc
            for sg in segs:
                a, b = max(sg['s'], s), min(sg['e'], e)
                if b <= a:
                    continue
                n = (b - a).days
                if sg['kind'] == 'work':
                    rate = sg['rate']
                    if struct and not sg['firm'] and a >= D(2027, 1, 1):
                        rate = P['val']['mc'][scen][typ]
                    re = P['re'][re_scen](y)
                    rev += rate * re * n
                    opex += oxd * n
                    if rig == 'GHTH':
                        bb += P['bareboat'] * n
                elif sg['kind'] == 'sps':
                    opex += oxd * n
                elif sg['kind'] == 'idle' and not (rig == 'GHTH' and not P.get('ghth_idle_cost', False)):
                    # warm 90 days from the spell start, then cold (GHTH: chartered in, no idle cost [A])
                    for i in range(n):
                        k = (a - sg['s']).days + i
                        opex += oxd * (P['idle_warm'] if k < 90 else P['idle_cold'])
        rev /= 1000; opex /= 1000; bb /= 1000
        rev += sum(x for dd, x in P['rev_events'].get(scen, []) if s <= dd < e)
        sb = P['seabird'][sb_scen](y, q)
        sga = P['sga'](y, q)
        ebitda = rev - opex + sb - sga
        ebitda_ab = ebitda - bb
        tax = P['tax'] * rev
        nint = debt * P['r_debt'](y) * nd / 365 - cash * P['r_cash'] * nd / 365
        mcap = P['mcap'](y, q)
        wc = P['wc'](y, q)
        mfcf = ebitda_ab - tax - nint - mcap - wc
        am = P['amort'](y, q)
        fads = mfcf - am
        # distributions paid in the quarter (cash floor at payment)
        paid = 0.0
        for (pd, amt) in sorted([p for p in pend if s <= p[0] < e]):
            frac = (pd - s).days / nd
            avail = cash + fads * frac - paid - P['floor']
            x = max(0.0, min(amt, avail))
            paid += x
            paid_list.append((pd, x, amt))
            if P.get('carry') and amt - x > 1e-9:          # withheld part paid with the next distribution
                carry.append(amt - x)
        pend = [p for p in pend if not (s <= p[0] < e)]
        decl = P['declare'](P, y, q, fads, scen)
        for i, (pd, amt) in enumerate(decl):
            if i == 0 and carry:
                amt += sum(carry); carry.clear()
            pend.append((pd, amt))
        cash = cash + fads - paid
        debt = debt - am
        rows.append(dict(y=y, q=q, rev=rev, opex=opex, sb=sb, sga=sga, ebitda=ebitda, bb=bb,
                         ebitda_ab=ebitda_ab, tax=tax, nint=nint, mcap=mcap, wc=wc, mfcf=mfcf,
                         am=am, fads=fads, decl=sum(a for _, a in decl), paid=paid,
                         nd=debt - cash, cash=cash, debt=debt))
    nd_exit = debt - cash
    # ---- exit value
    assets = {}
    for rig in OWNED:
        typ = TYPE[rig]
        base = mc_value(P, exit_scen, typ, age(rig, EXIT), exit_mult)
        prem_f = backlog_value(P, rig, [g for g in sched[rig] if g['firm']], EXIT, exit_scen, False,
                               struct, scen)
        prem_s = 0.0 if firm_only_exit else backlog_value(
            P, rig, [g for g in sched[rig] if not g['firm']], EXIT, exit_scen, True, struct, scen)
        assets[rig] = (base, prem_f, prem_s)
    gh_f = backlog_value(P, 'GHTH', [g for g in sched['GHTH'] if g['firm']], EXIT, exit_scen, False, struct, scen)
    gh_s = 0.0 if firm_only_exit else backlog_value(
        P, 'GHTH', [g for g in sched['GHTH'] if not g['firm']], EXIT, exit_scen, True, struct, scen)
    sbv = P['seabird_exit'][P.get('sbx_scen') or exit_scen]
    tot_assets = sum(sum(v) for v in assets.values()) + gh_f + gh_s + sbv
    VT = tot_assets - nd_exit
    return dict(rows=rows, paid=paid_list, nd_exit=nd_exit, assets=assets, ghth=(gh_f, gh_s),
                sbv=sbv, tot_assets=tot_assets, VT=VT, P=P, sched=sched)

def per_share(P, x):
    return x * P['fx'] / P['shares']

def flows(P, R, fx_path=None):
    """Per-share NOK flows from the valuation date: D_t at payment dates (only after the valuation
    date), V_T at exit. fx_path(year) multiplies spot."""
    f = (lambda yr: 1.0) if fx_path is None else fx_path
    c = [(0.0, -P['price'])]
    for (pd, x, _) in R['paid']:
        if pd > P['vdate'] and pd <= EXIT:
            c.append((yf(P['vdate'], pd), per_share(P, x) * f(pd.year)))
    c.append((yf(P['vdate'], EXIT), per_share(P, R['VT']) * f(2029)))
    return c

def decide(P, R, fx_path=None, k=K):
    c = flows(P, R, fx_path)
    r = irr(c); pk = pv(c[1:], k)
    sd = sum(x for _, x in c[1:-1]); vt = c[-1][1]
    return dict(irr=r, pk=pk, mos=pk / P['price'] - 1, sumD=sd, VT=vt, flows=c)

def nav0(P, scen='Base', vdate=None, nd=None):
    """NAV at the valuation date: owned rigs at the scenario mid-cycle by age + firm-today premium
    + GHTH firm margin + SeaBird - net debt at the valuation date ($m)."""
    vdate = vdate or P['vdate']; sched = P['sched'][scen]
    rigs = sum(mc_value(P, scen, TYPE[r], age(r, vdate)) for r in OWNED)
    prem = sum(backlog_value(P, r, [g for g in sched[r] if g['firm']], vdate, scen, False) for r in OWNED)
    gh = backlog_value(P, 'GHTH', [g for g in sched['GHTH'] if g['firm']], vdate, scen, False)
    sb = P['seabird_exit']['Base'] if scen == 'Base' else P['seabird_exit'][scen]
    nd = P['nd_vdate'] if nd is None else nd
    return dict(rigs=rigs, prem=prem, ghth=gh, sb=sb, nd=nd, nav=rigs + prem + gh + sb - nd)

def mark(P, R, scen, d, w):
    """Interim mark at date d ($m): owned rigs at a blend (1-w) Base + w scenario mid-cycle by age;
    backlog premium (firm today in full, scenario-signed capped 2 years) against the blended day;
    GHTH margin; SeaBird blend; less net debt at d."""
    sched = R['sched']; tot = 0.0
    for rig in OWNED:
        typ = TYPE[rig]
        val = (1 - w) * mc_value(P, 'Base', typ, age(rig, d)) + w * mc_value(P, scen, typ, age(rig, d))
        day = (1 - w) * mc_day(P, 'Base', typ) + w * mc_day(P, scen, typ)
        segs = [g for g in sched[rig] if (g['firm'] or w > 0)]
        prem = backlog_value(P, rig, [g for g in segs if g['firm']], d, scen, False, mcday=day) + \
            backlog_value(P, rig, [g for g in segs if not g['firm']], d, scen, True, mcday=day)
        tot += val + prem
    segs = [g for g in sched['GHTH'] if (g['firm'] or w > 0)]
    tot += backlog_value(P, 'GHTH', [g for g in segs if g['firm']], d, scen, False) + \
        backlog_value(P, 'GHTH', [g for g in segs if not g['firm']], d, scen, True)
    tot += (1 - w) * P['seabird_exit']['Base'] + w * P['seabird_exit'][scen]
    nd = [r for r in R['rows'] if D(r['y'], 3 * r['q'], 1) <= d][-1]['nd']
    return tot - nd

# ---------------------------------------------------------------- common pieces
def val_block():
    return dict(mc={'Bear': {'barge': 67, 'semi': 100}, 'Base': {'barge': 80, 'semi': 120},
                    'Bull': {'barge': 95, 'semi': 140}},
                mcu={'Bear': 0.65, 'Base': 0.80, 'Bull': 0.90},
                opex={'barge': 35.0, 'semi': 40.0}, re=0.98, idle=0.40,
                mcap={'barge': 3.0, 'semi': 3.5}, tax=0.064, r=0.08, floor=10.0, life=30)

def pay_date(y, q):
    """Distribution for quarter q paid ~4.5 months after quarter end."""
    return {1: D(y, 8, 15), 2: D(y, 11, 15), 3: D(y + 1, 2, 15), 4: D(y + 1, 5, 15)}[q]

def sps_2029(segs, start=D(2029, 10, 1), n=15):
    """15 days off-hire in October 2029 on a working segment (four rigs, 2029 special surveys)."""
    out = []
    for g in segs:
        if g['kind'] == 'work' and g['s'] <= start and g['e'] >= start + timedelta(days=n):
            out.append(dict(g, e=start))
            out.append(seg(start, start + timedelta(days=n), 'sps'))
            out.append(dict(g, s=start + timedelta(days=n)))
        else:
            out.append(g)
    return out

END = D(2033, 1, 1)

# ---------------------------------------------------------------- 27 Oct build (OLD)
def sched_old():
    S = {}
    # Base
    b = {}
    b['EDrill-1'] = [seg(D(2026, 7, 1), D(2027, 1, 1), 'work', 94, True),
                     seg(D(2027, 1, 1), D(2027, 3, 1), 'work', 94),
                     seg(D(2027, 3, 1), D(2027, 7, 1), 'idle'),
                     seg(D(2027, 7, 1), D(2029, 1, 1), 'work', 78),
                     seg(D(2029, 1, 1), D(2029, 2, 1), 'idle'),
                     seg(D(2029, 2, 1), D(2031, 1, 1), 'work', 85),
                     seg(D(2031, 1, 1), END, 'idle')]
    b['EDrill-2'] = sps_2029([seg(D(2026, 7, 1), D(2030, 11, 1), 'work', 83, True),
                              seg(D(2030, 11, 1), END, 'idle')])
    b['T-15'] = sps_2029([seg(D(2026, 7, 1), D(2027, 2, 1), 'work', 121, True),
                          seg(D(2027, 2, 1), D(2027, 4, 1), 'work', 121),
                          seg(D(2027, 4, 1), D(2027, 8, 1), 'idle'),
                          seg(D(2027, 8, 1), D(2029, 2, 1), 'work', 78),
                          seg(D(2029, 2, 1), D(2029, 3, 1), 'idle'),
                          seg(D(2029, 3, 1), D(2031, 1, 1), 'work', 85),
                          seg(D(2031, 1, 1), END, 'idle')])
    b['T-16'] = sps_2029([seg(D(2026, 7, 1), D(2026, 12, 1), 'work', 131, True),
                          seg(D(2026, 12, 1), D(2027, 2, 15), 'work', 124),
                          seg(D(2027, 2, 15), D(2027, 7, 15), 'idle'),
                          seg(D(2027, 7, 15), D(2030, 1, 15), 'work', 95.1, True),
                          seg(D(2030, 1, 15), D(2031, 4, 15), 'work', 90),
                          seg(D(2031, 4, 15), END, 'idle')])
    b['Vencedor'] = sps_2029([seg(D(2026, 7, 1), D(2028, 1, 1), 'work', 127, True),
                              seg(D(2028, 1, 1), D(2029, 1, 1), 'work', 123),
                              seg(D(2029, 1, 1), D(2029, 2, 1), 'idle'),
                              seg(D(2029, 2, 1), D(2031, 1, 1), 'work', 125),
                              seg(D(2031, 1, 1), END, 'idle')])
    b['GHTH'] = [seg(D(2026, 7, 1), D(2027, 8, 1), 'work', 160, True),
                 seg(D(2027, 8, 1), D(2028, 8, 1), 'work', 147),
                 seg(D(2028, 8, 1), D(2028, 9, 15), 'idle'),
                 seg(D(2028, 9, 15), D(2030, 9, 15), 'work', 120),
                 seg(D(2030, 9, 15), END, 'gone')]
    S['Base'] = b
    # Bear
    r = {}
    r['EDrill-1'] = [seg(D(2026, 7, 1), D(2027, 1, 1), 'work', 94, True),
                     seg(D(2027, 1, 1), D(2027, 9, 1), 'idle'),
                     seg(D(2027, 9, 1), D(2029, 3, 1), 'work', 68),
                     seg(D(2029, 3, 1), D(2029, 6, 1), 'idle'),
                     seg(D(2029, 6, 1), D(2031, 1, 1), 'work', 65),
                     seg(D(2031, 1, 1), END, 'idle')]
    r['EDrill-2'] = b['EDrill-2']
    r['T-15'] = sps_2029([seg(D(2026, 7, 1), D(2027, 2, 1), 'work', 121, True),
                          seg(D(2027, 2, 1), D(2027, 11, 1), 'idle'),
                          seg(D(2027, 11, 1), D(2029, 5, 1), 'work', 68),
                          seg(D(2029, 5, 1), D(2029, 8, 1), 'idle'),
                          seg(D(2029, 8, 1), D(2031, 1, 1), 'work', 65),
                          seg(D(2031, 1, 1), END, 'idle')])
    r['T-16'] = sps_2029([seg(D(2026, 7, 1), D(2026, 12, 1), 'work', 131, True),
                          seg(D(2026, 12, 1), D(2027, 2, 15), 'work', 124),
                          seg(D(2027, 2, 15), D(2027, 7, 15), 'idle'),
                          seg(D(2027, 7, 15), D(2030, 1, 15), 'work', 95.1, True),
                          seg(D(2030, 1, 15), END, 'idle')])
    r['Vencedor'] = [seg(D(2026, 7, 1), D(2028, 1, 1), 'work', 127, True),
                     seg(D(2028, 1, 1), D(2028, 5, 1), 'idle'),
                     seg(D(2028, 5, 1), D(2031, 5, 1), 'work', 95),
                     seg(D(2031, 5, 1), END, 'idle')]
    r['Vencedor'] = sps_2029(r['Vencedor'])
    r['GHTH'] = [seg(D(2026, 7, 1), D(2027, 8, 1), 'work', 160, True),
                 seg(D(2027, 8, 1), END, 'gone')]
    S['Bear'] = r
    # Bull
    u = {}
    u['EDrill-1'] = [seg(D(2026, 7, 1), D(2027, 1, 1), 'work', 94, True),
                     seg(D(2027, 1, 1), D(2027, 4, 1), 'work', 94),
                     seg(D(2027, 4, 1), D(2027, 5, 1), 'idle'),
                     seg(D(2027, 5, 1), D(2028, 11, 1), 'work', 88),
                     seg(D(2028, 11, 1), D(2031, 1, 1), 'work', 95),
                     seg(D(2031, 1, 1), END, 'idle')]
    u['EDrill-2'] = b['EDrill-2']
    u['T-15'] = sps_2029([seg(D(2026, 7, 1), D(2027, 2, 1), 'work', 121, True),
                          seg(D(2027, 2, 1), D(2027, 5, 1), 'work', 121),
                          seg(D(2027, 5, 1), D(2027, 6, 1), 'idle'),
                          seg(D(2027, 6, 1), D(2028, 12, 1), 'work', 88),
                          seg(D(2028, 12, 1), D(2031, 1, 1), 'work', 95),
                          seg(D(2031, 1, 1), END, 'idle')])
    u['T-16'] = b['T-16']
    u['Vencedor'] = sps_2029([seg(D(2026, 7, 1), D(2028, 1, 1), 'work', 127, True),
                              seg(D(2028, 1, 1), D(2029, 1, 1), 'work', 123),
                              seg(D(2029, 1, 1), D(2032, 1, 1), 'work', 165),
                              seg(D(2032, 1, 1), END, 'idle')])
    u['GHTH'] = [seg(D(2026, 7, 1), D(2027, 8, 1), 'work', 160, True),
                 seg(D(2027, 8, 1), D(2028, 8, 1), 'work', 147),
                 seg(D(2028, 8, 1), D(2030, 8, 1), 'work', 150),
                 seg(D(2030, 8, 1), END, 'gone')]
    S['Bull'] = u
    return S

def opt_shares(out, n, strike, price):
    return out + n * max(0.0, 1 - strike / price)

def OLD():
    P = {}
    P['tag'] = '27 Oct build'
    P['vdate'] = D(2026, 10, 27); P['price'] = 6.80; P['fx'] = 9.32
    P['shares'] = 737.3
    P['start'] = D(2026, 7, 1); P['debt0'] = 61.1; P['cash0'] = 53.6
    P['known_dist'] = [(D(2026, 8, 15), 25.0), (D(2026, 11, 13), 25.0)]
    P['opex26'] = {'barge': 35.0, 'semi': 40.0}; P['esc'] = 0.03
    P['idle_warm'] = 0.65; P['idle_cold'] = 0.35
    P['bareboat'] = 27.0
    P['re'] = {'Base': lambda y: 0.98, 'Bull': lambda y: 0.98,
               'Bear': lambda y: 0.98 if y == 2026 else 0.96}
    sbq = {'Bear': 5.0, 'Base': 10.0, 'Bull': 18.0}
    def sb(scen):
        return lambda y, q: (1.5 if q == 3 else 3.0) if y == 2026 else sbq[scen] / 4
    P['seabird'] = {s: sb(s) for s in sbq}
    P['seabird_exit'] = {'Bear': 20.0, 'Base': 35.0, 'Bull': 50.0}
    P['sga'] = lambda y, q: 4.3 if y == 2026 else {2027: 17.0, 2028: 17.5, 2029: 18.0}[y] / 4
    P['mcap'] = lambda y, q: 5.0 if y == 2026 else {2027: 20.0, 2028: 15.0, 2029: 28.0}[y] / 4
    P['wc'] = lambda y, q: 0.0
    P['amort'] = lambda y, q: 2.0 if y <= 2027 else 8.1 / 4
    P['r_debt'] = lambda y: 0.077 if y == 2026 else 0.083
    P['r_cash'] = 0.035
    P['tax'] = 0.064
    P['floor'] = 20.0
    P['payout'] = 0.90
    P['declare'] = lambda P, y, q, fads, scen: [(pay_date(y, q), P['payout'] * max(0.0, fads))]
    P['rev_events'] = {}
    P['sched'] = sched_old()
    P['val'] = val_block()
    P['nd_vdate'] = 3.3
    return P

# ---------------------------------------------------------------- 27 Nov build (Q3 report)
def sched_q3():
    """Q3 report changes: T-16 Phase 6 firm to end-Jan 2027 at $131k [F]; Phase 7 dayrate $90k
    [F] plus mobilisation fees (USD 87m firm incl. mob: ~$4.6m [B]); T-15 firm to end-Feb 2027 [F]."""
    S = sched_old()
    for sc in S:
        t16 = [g for g in S[sc]['T-16']]
        new = [seg(D(2026, 7, 1), D(2027, 2, 1), 'work', 131, True),
               seg(D(2027, 2, 1), D(2027, 7, 15), 'idle')]
        for g in t16:
            if g['s'] >= D(2027, 7, 15):
                g = dict(g)
                if g['firm']:
                    g['rate'] = 90.0
                new.append(g)
        S[sc]['T-16'] = new
        t15 = S[sc]['T-15']
        out = []
        for g in t15:
            g = dict(g)
            if g['firm'] and g['s'] == D(2026, 7, 1):
                g['e'] = D(2027, 3, 1)
            elif g['s'] == D(2027, 2, 1) and g['kind'] == 'work':   # Base/Bull bridge after the firm term
                g['s'] = D(2027, 3, 1)
            elif g['s'] == D(2027, 2, 1) and g['kind'] == 'idle':   # Bear: idle after the firm term
                g['s'] = D(2027, 3, 1)
            out.append(g)
        S[sc]['T-15'] = out
    return S

MOB_T16 = 87.0 - 90.0 * (D(2030, 1, 15) - D(2027, 7, 15)).days / 1000   # ~$4.6m [B]

def Q3(price=6.60, fx=9.755, vdate=D(2026, 11, 27)):
    P = OLD()
    P['tag'] = '27 Nov build (Q3 report)'
    P['vdate'] = vdate; P['price'] = price; P['fx'] = fx
    P['shares_out'] = 731.253; P['opt_n'] = 18.128; P['opt_k'] = 3.92
    P['shares'] = opt_shares(731.253, 18.128, 3.92, price)
    # 30 Sep 2026 actual balance sheet [F]: bank loan 58.995 + other 0.083; cash 26.340 + restricted 17.627
    P['start'] = D(2026, 10, 1); P['debt0'] = 59.078; P['cash0'] = 43.967
    P['q3_fads'] = 15.29     # Q3 actual FCF after debt service: cash -9.63 + distribution 25.0 - other financing 0.08
    P['known_dist'] = [(D(2026, 12, 11), 25.0)]
    # ED opex 9M 2026 $62.2m / 1,638 rig-days = $38.0k vs $36.7k on the 35/40 mix: x1.035 [F]
    P['opex26'] = {'barge': 35.0 * 1.035, 'semi': 40.0 * 1.035}
    P['sga'] = lambda y, q: 4.0 if y == 2026 else {2027: 16.0, 2028: 16.5, 2029: 17.0}[y] / 4
    P['mcap'] = lambda y, q: 5.0 if y == 2026 else {2027: 20.0, 2028: 15.0, 2029: 28.0}[y] / 4
    # contract balances unwind (liabilities 6.86 less capitalised mob cost 2.80 = 4.1, non-cash revenue) [B/A]
    P['wc'] = lambda y, q: 1.0 if (y, q) in ((2026, 4), (2027, 1), (2027, 2), (2027, 3)) else 0.0
    P['amort'] = lambda y, q: 2.0 if y == 2026 else 8.1 / 4
    P['r_debt'] = lambda y: 0.077 if y == 2026 else 0.080   # SOFR Z27 4.54% (27 Nov) + 350 bp
    P['floor'] = 25.0                                    # restricted 17.6 + ~7 operating cash [A]
    P['carry'] = True                                    # withheld part paid with the next distribution [A]
    P['h2_min'] = 40.0                                   # guidance $90-110m less H1 $50m [F]
    P['h2_date'] = D(2027, 4, 15)                        # after closing or the 31 Mar long-stop [A]
    def declare(P, y, q, fads, scen):
        if (y, q) == (2026, 4):
            amt = max(P['payout'] * max(0.0, P['q3_fads'] + fads), P['h2_min'])
            return [(P['h2_date'], amt)]
        return [(pay_date(y, q), P['payout'] * max(0.0, fads))]
    P['declare'] = declare
    sbq = {'Bear': 5.0, 'Base': 10.0, 'Bull': 18.0}
    def sb(scen):
        return lambda y, q: 3.0 if y == 2026 else sbq[scen] / 4
    P['seabird'] = {s: sb(s) for s in sbq}
    P['sched'] = sched_q3()
    P['rev_events'] = {s: [(D(2027, 7, 15), MOB_T16)] for s in ('Bear', 'Base', 'Bull')}
    P['nd_vdate'] = None      # set in sed_run from the Q4 path (30 Sep actual rolled 58 days)
    return P
