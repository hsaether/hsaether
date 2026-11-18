# NVIDIA (docs/nvda-analysis.md) -- IAF model, version 1.7, 18 Nov 2026 (run date; price = 17 Nov close).
# Built from v15.py (v1.5/v1.6 model; v15.py with its own constants reproduces v1.6: 17.7% / $192.5 at $166.19).
# Changes in v1.7 (Q3 FY27 report, 17 Nov; 8-K Ex. 99.1 and CFO commentary [F], call [E]):
#  - valuation date 17 Nov 2026 (the close), stub 18 Nov - 31 Dec (44 days), built explicitly from the
#    25 Oct balance sheet [F]: net cash 21.1bn (cash 29.1 + marketable debt 24.4 - LT debt 32.4), stakes
#    marketable 44.2 + non-marketable 65.5 + equity-method 3.3 [C]; public stakes re-marked 23 Oct -> 17 Nov
#    on the 30 Sep 13F counts (-6.15bn); Q4 FY27 cash flows from the guide (revenue 130, GM 71.5%, opex 10.7):
#    FCF 45bn, buybacks 30bn, dividend 6.05bn on 23 Dec, Anthropic Class N placement 10bn at cost + 3bn other.
#  - payout 80% of FCF after growth and stakes (buyback authorisation 227.3bn to be executed by end FY28 [F]).
#  - revenue (working capital and cascade basis) from Base GM 72.5% (FY28 guide 72-73% [F]) and an opex path,
#    not from fixed net margins; REV0 = FY27 revenue 423.7bn (9M 293.7 [F] + Q4 guide 130 [F]).
#  - capex at the Q3 run-rate (4.4bn a quarter [F]): 18/20/22, D&A 8/10/12 (Base).
#  - Bear cross-funding costs rebuilt on the Q3 inventory (neocloud 32, guarantees 118 incl. power and systems
#    9.5 new, data-center leases 74 not yet commenced).
# The EPS paths are the AI BBB's (11 Nov, unchanged): H1 .92/.91/.88/.87 x CY27 consensus 15.21 (7 Nov basis).
# Standard library only. Run from this folder.
from datetime import date

SH = 24.19         # diluted shares, bn (Q3 FY27 non-GAAP diluted 24,186m [F]); held flat (buybacks are D_t)
K = 0.12
CY27 = 15.21       # calendarised CY27 consensus of 7 Nov (AI BBB basis)
REV0 = 423.7       # FY27 revenue: 9M 293.7 [F] + Q4 guide 130.0 [F]; working-capital base
VDATE = date(2026, 11, 17)
EXIT = date(2029, 12, 31)
TAX = 0.17
GM = 0.725         # Base and Bull gross margin 2027-30 [A] (FY28 guide 72-73% [F]; Q4 71-72% "the bottom")
OPEX = [46.0, 52.0, 56.0, 58.0]   # non-GAAP opex net of other income 2027-30, $bn [A] (Q4 guide 10.7 for 14 weeks)
LINK = [1.25, 1.25, 1.25, 1.0]    # H1 revenue-to-EPS link (review-ai-h1-non-k1-funding 4.4)

# ---- stub (identical in all scenarios), $bn [A] unless noted ----
NC_Q3 = 29.089 + 24.423 - 32.371      # net cash 25 Oct [F] = 21.141
ST_Q3 = 44.219 + 65.528 + 3.3          # stakes 25 Oct: marketable [F] + non-marketable [F] + equity-method [C]
REMARK = -6.15                         # public stakes 23 Oct -> 17 Nov close on 30 Sep 13F counts [A]
Q4 = dict(fcf=45.0, bb=30.0, div=0.25 * SH, eq_pre=0.7, eq_stub=13.0, days=98, pre=23, stub=44)
f_pre, f_stub = Q4['pre'] / Q4['days'], Q4['stub'] / Q4['days']
NC0 = NC_Q3 + Q4['fcf'] * f_pre - Q4['bb'] * f_pre - Q4['eq_pre']          # net cash at the valuation date
ST0 = ST_Q3 + REMARK + Q4['eq_pre']                                        # stakes at the valuation date
STUB_FCF = Q4['fcf'] * f_stub
STUB_BB = Q4['bb'] * f_stub
STUB_DIV = Q4['div']
NC26 = NC0 + STUB_FCF - STUB_BB - STUB_DIV - Q4['eq_stub']                 # net cash 31 Dec 2026
ST26 = ST0 + Q4['eq_stub']                                                 # stakes at book 31 Dec 2026
Q4_EPS = (130.0 * 0.715 - 10.7 + 0.25) * (1 - TAX) / SH                    # Q4 FY27 non-GAAP EPS from the guide [A]
STUB_EPS = Q4_EPS * f_stub


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


def rev_from_eps(eps, i, gm=GM):
    return (eps * SH / (1 - TAX) + OPEX[i]) / gm


BASE = dict(name='Base', eps=[0.92 * CY27, 0.91 * CY27, 0.88 * CY27], eps30=0.87 * CY27,
            rev=None, capex=[18, 20, 22], da=[8, 10, 12],
            stakes=[11.9 + 7.0, 2, 2], charge=[0, 0, 0], exitliab=0.0, sf=1.0, sfg=[1, 1, 1],
            pe=17, payout=.8, wc=.25, remark=0.0)
BEAR = dict(BASE, name='Bear', eps=[0.68 * CY27, 0.50 * CY27, 0.53 * CY27], eps30=0.57 * CY27, rev=[497, 404, 422],
            capex=[16, 15, 15], charge=[1.8, 11.1, 11.1], exitliab=22.2, sf=.5, sfg=[.5, .5, .5], pe=13)
BULL = dict(BASE, name='Bull', eps=[1.00 * CY27, 1.15 * CY27, 1.25 * CY27], eps30=1.30 * CY27,
            capex=[20, 23, 26], sf=1.25, sfg=[1.08, 1.17, 1.25], pe=19)
NOKF = {'Base': [1, 1, 1, 1], 'Bear': [1, 1.12, 1.09, 1.09], 'Bull': [1, .97, .97, .97]}
# Bear cross-funding costs [A], $bn: 2027 / 2028 / 2029 / at exit
BEAR_CF = {
    'Neocloud buy-backs (32), net of own use': [1.8, 4.4, 3.6, 8.0],
    'SB Energy guaranty (OpenAI default; 1-2 phases, half re-let)': [0, 0, 5.0, 6.0],
    'Land, power, shell 3.5 + power and systems 9.5 (half called)': [0, 5.1, 0, 0],
    'Data-center leases at risk (~33 of 74), not reassigned': [0, 1.6, 2.5, 8.2],
}


def base_rev(s):
    return [rev_from_eps(s['eps'][i], i) for i in range(3)] if s['rev'] is None else list(s['rev'])


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


def build(s, P=None, vdate=VDATE, **ov):
    s = dict(s, **ov)
    st26 = ST26 + s['remark']
    nc = NC26; st = st26; NC = []; ST = []; FCF = []; NI = []; REV = []; prev = REV0
    D = [STUB_BB / SH, STUB_DIV / SH]
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
    dates = [date(2026, 12, 9), date(2026, 12, 23), date(2027, 7, 1), date(2028, 7, 1), date(2029, 7, 1)]
    cf = [(t(d), x) for d, x in zip(dates, D)] + [(t(EXIT), VT)]
    res = dict(D=D, VT=VT, NC=NC, ST=ST, FCF=FCF, NI=NI, REV=REV, cf=cf, nc0=NC0 / SH, st0=(ST0 + s['remark']) / SH,
               nc26=NC26 / SH, st26=st26 / SH, s=s, T=t(EXIT))
    if P is not None:
        res['irr'] = irr([(0, -P)] + cf)
    res['pk'] = pvk(cf)
    return res


def Dyear(r):
    """D_t per calendar year: stub (buybacks + dividend), 2027, 2028, 2029."""
    return [r['D'][0] + r['D'][1]] + r['D'][2:]


def nok_irr(r, name, P):
    f = NOKF[name]
    idx = [0, 0, 1, 2, 3]
    cf = [(t, c * f[idx[i]]) for i, (t, c) in enumerate(r['cf'][:5])] + [(r['cf'][5][0], r['cf'][5][1] * f[3])]
    return irr([(0, -P)] + cf)


def interim(r, name, P):
    """Year-end V_t 2027-28 (path diagnostic): core P/E on next-year EPS glides from today's
    (on Base 2027) to the exit P/E in thirds; the Bear reaches its exit P/E at end-2027.
    End-2026 mark: P plus the stub's retained cash and stake purchases (same in all scenarios)."""
    s = r['s']
    core0 = (P - r['nc0'] - r['st0']) / BASE['eps'][0]
    V = []
    eps_next = [s['eps'][1], s['eps'][2]]
    for i in range(2):
        pe = s['pe'] if name == 'Bear' else core0 + (s['pe'] - core0) * (i + 1) / 3
        V.append(pe * eps_next[i] + r['NC'][i] + s['sfg'][i] * r['ST'][i])
    V26 = P + (r['nc26'] - r['nc0']) + (r['st26'] - r['st0'])
    return V26, V


def er(P, nibor=4.38):
    rb = build(BASE, P); rr = build(BEAR, P)
    V26b, Vb = interim(rb, 'Base', P); V26r, Vr = interim(rr, 'Bear', P)
    rb27 = (rb['D'][2] + Vb[0]) / V26b - 1
    rr27n = (rr['D'][2] + Vr[0]) * NOKF['Bear'][1] / V26r - 1
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


if __name__ == '__main__':
    print(f"NC_Q3 {NC_Q3:.2f} ST_Q3 {ST_Q3:.2f} NC0 {NC0:.2f} ST0 {ST0:.2f} NC26 {NC26:.2f} ST26 {ST26:.2f} "
          f"stub FCF {STUB_FCF:.2f} BB {STUB_BB:.2f} DIV {STUB_DIV:.2f}; Q4 EPS {Q4_EPS:.3f} stub EPS {STUB_EPS:.3f}")
    print('Base rev', [round(x, 1) for x in base_rev(BASE)], 'Bull rev', [round(x, 1) for x in base_rev(BULL)])
    print('Bear charges', [round(sum(v[i] for v in BEAR_CF.values()), 1) for i in range(4)])
