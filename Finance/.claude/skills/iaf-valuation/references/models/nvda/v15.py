# NVIDIA (docs/nvda-analysis.md) -- IAF model, version 1.5, 12 Nov 2026.
# Built from v13.py (which reproduces v1.4 exactly: 19.76% / $212.19 at $173.73, 11 Nov, 50-day stub).
# Changes in v1.5: valuation date 12 Nov (49-day stub); AI BBB 11 Nov H1 Base path (.92/.91/.88/.87);
# public equity stakes re-marked (-6.5bn since the 26 Jul 10-Q); Bear cross-funding rebuilt
# (in-window charges 2/7.5/10.5bn and a 20bn exit liability); revenue-loss sensitivities with the
# H1 revenue-to-EPS link (1.25 in 2027-29, 1.0 in 2030). Standard library only.
from datetime import date

SH = 24.2          # diluted shares, bn (held flat; buybacks are D_t)
K = 0.12
CY27 = 15.21       # calendarised CY27 consensus (AI BBB basis)
REV0 = 411.8       # FY27 consensus revenue, working-capital base (kept from version 1)
VDATE = date(2026, 11, 12)
EXIT = date(2029, 12, 31)
STUB_DAYS = 49     # 13 Nov - 31 Dec 2026
NC26 = 41.8        # net cash 31 Dec 2026, $bn [C] (version 1 roll-forward)
ST26_BOOK = 115.0  # equity stakes 31 Dec 2026 at book, $bn [C]
REMARK = -6.5      # public stakes re-marked 26 Jul -> 12 Nov, $bn [A] (Intel -6.5, SpaceX +3.4, other L1 -0.6, Level 2 -2.7)
LINK = [1.25, 1.25, 1.25, 1.0]  # H1 revenue-to-EPS link (review-ai-h1-non-k1-funding 4.4)


def irr(cf):
    lo, hi = -0.95, 3.0
    for _ in range(300):
        m = (lo + hi) / 2
        if sum(c / (1 + m) ** t for t, c in cf) > 0:
            lo = m
        else:
            hi = m
    return m


def pvk(cf, k=K):
    return sum(c / (1 + k) ** t for t, c in cf)


BASE = dict(name='Base', eps=[0.92 * CY27, 0.91 * CY27, 0.88 * CY27], eps30=0.87 * CY27,
            margin=[.555, .55, .545], rev=None, capex=[13, 15, 17], da=[6.5, 9, 11],
            stakes=[16.9, 2, 2], charge=[0, 0, 0], exitliab=0.0, sf=1.0, sfg=[1, 1, 1],
            pe=17, payout=.6, wc=.25, remark=REMARK)
BEAR = dict(BASE, name='Bear', eps=[10.34, 7.61, 8.06], eps30=8.67, rev=[497, 404, 422],
            capex=[12, 11, 11], charge=[2.0, 7.5, 10.5], exitliab=20.0, sf=.5, sfg=[.5, .5, .5], pe=13)
BULL = dict(BASE, name='Bull', eps=[15.21, 17.49, 19.01], eps30=19.77, margin=[.56, .555, .55],
            capex=[14, 17, 19], sf=1.25, sfg=[1.08, 1.17, 1.25], pe=19)
NOKF = {'Base': [1, 1, 1, 1], 'Bear': [1, 1.12, 1.09, 1.09], 'Bull': [1, .97, .97, .97]}


def base_rev(s):
    return [s['eps'][i] * SH / s['margin'][i] for i in range(3)] if s['rev'] is None else list(s['rev'])


def apply_loss(s, loss, extra_charge=None):
    """Revenue loss fractions [2027, 2028, 2029, 2030]; EPS falls by loss x LINK."""
    rev = base_rev(s)
    t = dict(s)
    t['eps'] = [s['eps'][i] * (1 - loss[i] * LINK[i]) for i in range(3)]
    t['eps30'] = s['eps30'] * (1 - loss[3] * LINK[3])
    t['rev'] = [rev[i] * (1 - loss[i]) for i in range(3)]
    if extra_charge:
        t['charge'] = [s['charge'][i] + extra_charge[i] for i in range(3)]
    return t


def build(s, P=None, vdate=VDATE, stub_days=STUB_DAYS, **ov):
    s = dict(s, **ov)
    f = stub_days / 56
    sfcf = 22.5 * f
    sD = 0.6 * sfcf
    st26 = ST26_BOOK + s['remark']
    nc0 = NC26 - (sfcf - sD)
    st0 = st26 - 4.4 * f
    nc = NC26; st = st26; D = [sD / SH]; NC = []; ST = []; FCF = []; NI = []; REV = []; prev = REV0
    revs = base_rev(s)
    for i in range(3):
        ni = s['eps'][i] * SH
        rev = revs[i]
        wc = s['wc'] * (rev - prev); prev = rev
        fcf = ni - (s['capex'][i] - s['da'][i]) - wc - s['stakes'][i] - s['charge'][i]
        d = s['payout'] * fcf
        nc += fcf - d; st += s['stakes'][i]
        D.append(d / SH); NC.append(nc / SH); ST.append(st / SH); FCF.append(fcf); NI.append(ni); REV.append(rev)
    VT = s['pe'] * s['eps30'] + NC[-1] + s['sf'] * ST[-1] - s['exitliab'] / SH
    t = lambda d: (d - vdate).days / 365.25
    dates = [date(2026, 12, 28), date(2027, 7, 1), date(2028, 7, 1), date(2029, 7, 1)]
    cf = [(t(d), x) for d, x in zip(dates, D)] + [(t(EXIT), VT)]
    res = dict(D=D, VT=VT, NC=NC, ST=ST, FCF=FCF, NI=NI, REV=REV, cf=cf, nc0=nc0 / SH, st0=st0 / SH,
               nc26=NC26 / SH, st26=st26 / SH, s=s, T=t(EXIT), sfcf=sfcf, sD=sD)
    if P is not None:
        res['irr'] = irr([(0, -P)] + cf)
    res['pk'] = pvk(cf)
    return res


def nok_irr(r, name, P):
    f = NOKF[name]
    cf = [(t, c * f[min(i, 3)]) for i, (t, c) in enumerate(r['cf'][:4])] + [(r['cf'][4][0], r['cf'][4][1] * f[3])]
    return irr([(0, -P)] + cf)


def interim(r, name, P, base_eps27=None):
    """Year-end V_t 2027-28 (path diagnostic): core P/E on next-year EPS glides from today's
    (on Base 2027) to the exit P/E in thirds; the Bear reaches its exit P/E at end-2027."""
    s = r['s']
    if base_eps27 is None:
        base_eps27 = BASE['eps'][0]
    core0 = (P - r['nc0'] - r['st0']) / base_eps27
    V = []
    eps_next = [s['eps'][1], s['eps'][2]]
    for i in range(2):
        pe = s['pe'] if name == 'Bear' else core0 + (s['pe'] - core0) * (i + 1) / 3
        V.append(pe * eps_next[i] + r['NC'][i] + s['sfg'][i] * r['ST'][i])
    V26 = P + (r['nc26'] - r['nc0'])
    return V26, V


def er(P, nibor=4.38):
    rb = build(BASE, P); rr = build(BEAR, P)
    V26b, Vb = interim(rb, 'Base', P); V26r, Vr = interim(rr, 'Bear', P)
    rb27 = (rb['D'][1] + Vb[0]) / V26b - 1
    rr27n = (rr['D'][1] + Vr[0]) * NOKF['Bear'][1] / V26r - 1
    basen = nok_irr(rb, 'Base', P)
    return (basen * 100 - nibor) / ((rb27 - rr27n) * 100), rb27, rr27n


def solve(fn, target, lo, hi):
    for _ in range(200):
        m = (lo + hi) / 2
        if (fn(m) - target) * (fn(lo) - target) > 0:
            lo = m
        else:
            hi = m
    return m
