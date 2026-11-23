# SK hynix (docs/skhynix-analysis.md) -- IAF model, version 4.1 (23 Nov 2026 price re-mark = V41); version 4 (19 Nov 2026; V4: AI BBB 18 Nov H2 turn call, Base
# .90/.50/.32/.28, index 1.38/1.08/0.95; Seoul close 19 Nov); version 3 (16 Nov 2026). iaf-valuation 2026-11-18.1.
# Rebuilt from version 2's published inputs (28 Oct 2026; the v2 scripts were not kept): with V2 it
# reproduces v2 (Base 21.1%, P_k 1,835,729; Bear 2.4% / 1,169,283; Bull 33.7% / 2,416,951).
# Track B: EPS = AI BBB H2 path x CY27 consensus EPS; FCF = NI - dWC - (capex - D&A);
# V_T = exit P/E x 2030 EPS + net cash at exit + Kioxia stake after deferred tax. KRW tn unless per share.
from datetime import date

EXIT = date(2029, 12, 31)
TAX = 0.23
MEM = {'Bear': [.60, .30, .25, .25], 'Base': [.90, .60, .40, .35], 'Bull': [1.00, .80, .55, .45]}
IDX = {'Bear': [1.00, .72, .67], 'Base': [1.38, 1.18, 1.03], 'Bull': [1.50, 1.33, 1.18]}
CAPEX = {'Bear': [60, 50, 40], 'Base': [70, 85, 85], 'Bull': [80, 100, 110]}
DA = {'Bear': [20, 25, 27], 'Base': [21, 28, 35], 'Bull': [22, 30, 38]}
EXPE = {'Bear': 8.0, 'Base': 10.0, 'Bull': 11.0}
KIOM = {'Bear': 0.5, 'Base': 1.0, 'Bull': 1.2}       # Kioxia stake multiplier at exit (linear glide)
CBUY = {'Bear': .70, 'Base': .60, 'Bull': .55}       # H2 cash conversion 2029, buyer's return check
MEM18 = dict(MEM, Base=[.90, .50, .32, .28])     # AI BBB 18 Nov turn call (60%; L2, L4, L5)
IDX18 = dict(IDX, Base=[1.38, 1.08, 0.95])
I44 = {'Bear': [1.08, 1.06, 1.06], 'Base': [1, 1, 1], 'Bull': [.98, .98, .98]}   # Equity BBB NOK path

# ------------------------------------------------------------------ inputs per version
V2 = dict(P=1487000.0, vdate=date(2026, 10, 28), sh=705.173324, cons27=467761.0, rev26=355.8,
          q4=dict(rev=119.3, q3rev=104.62, op=94.3, da=4.6, intr=1.0, capex=16.0),
          bridge='v2', nc30=98.70, ltdep=7.10, ltinv=0.0, tax_owed=17.64, comp_owed=18.15,
          octset=11.17, other_out=0.0, q3div=20000.0, buy_cancel=10.0,
          d_buy=date(2026, 11, 30), d_div=date(2026, 12, 20), d_rem=date(2027, 4, 1),
          rem2026=35.36, pay=0.5, kio=22.0, wc=0.15, book26=347.0)

# V3: DART/6-K quarterly report to 30 Sep 2026 (filed 16 Nov): cash 38.324 + ST financial instruments
# 37.925 + ST investment assets 38.210 = 114.460; borrowings 4.555 + 11.244 = 15.800; LT investment
# assets 83.998 = Level 2 80.653 (of which the Kioxia-related asset transferred from Level 3, 36.266)
# + Level 3 3.346; non-current other financial assets at amortised cost (deposits) 3.516; current tax
# liabilities 27.571 - current tax assets 0.025; employee-benefit payables in other non-trade payables
# 17.551 - 1.819 = 15.731; equity-settled share compensation accrued in 2026 3.589 less 1,625,769
# treasury shares held for compensation at the price; Penguin Solutions preferred bought 29 Oct
# (USD 377.2m = 0.50). Kioxia: 30 Sep carrying 36.266 at JPY 18,095 and JPY/KRW 8.611, marked to
# JPY 8,392 and 8.349 (16 Nov), x 0.81 deferred tax. Prices: Seoul close 16 Nov; Yahoo CY27 EPS 16 Nov.
V3 = dict(V2, P=1120000.0, vdate=date(2026, 11, 16), cons27=537910.7, bridge='v3',
          nc30=114.460 - 15.800, ltdep=3.516, ltinv=80.653 - 36.266, tax_owed=27.571 - 0.025,
          comp_liab=15.731, comp_eq=3.589, treas_comp=1.625769, other_out=0.50,
          d_buy=date(2026, 12, 13), kio_carry=36.266, kio_px=(8392.0, 18095.0), jpykrw=(8.349, 8.611),
          book26=333.0)

# V4: Seoul close 19 Nov 1,173,000; Kioxia JPY 8,271, JPY/KRW 8.310 (19 Nov); CY27 consensus 537,911 (unchanged);
# AI BBB 18 Nov H2 Base path. Bridge as V3 (no new report).
V4 = dict(V3, P=1173000.0, vdate=date(2026, 11, 19), kio_px=(8271.0, 18095.0), jpykrw=(8.310, 8.611),
          mem_tab=MEM18, idx_tab=IDX18)
# V4.1 (price re-mark, 23 Nov 2026): Seoul close 23 Nov 1,085,000; Kioxia JPY 7,307 (20 Nov close; Tokyo shut 23 Nov),
# JPY/KRW 8.439 (Yahoo 23 Nov 11:27 UTC). Every path, consensus and bridge item as V4.
V41 = dict(V4, P=1085000.0, vdate=date(2026, 11, 23), kio_px=(7307.0, 18095.0), jpykrw=(8.439, 8.611))


def kio(I):
    if I['bridge'] == 'v2':
        return I['kio']
    a, b = I['kio_px']; c, d = I['jpykrw']
    return I['kio_carry'] * a / b * c / d * 0.81


def comp_owed(I):
    if I['bridge'] == 'v2':
        return I['comp_owed']
    return I['comp_liab'] + max(0.0, I['comp_eq'] - I['treas_comp'] * I['P'] / 1e6)


def bridge(I):
    q = I['q4']
    wc = I['wc'] * 4 * (q['rev'] - q['q3rev'])
    tax = TAX * (q['op'] + q['intr'])
    fcf_q4 = q['op'] + q['da'] + q['intr'] - tax - q['capex'] - wc
    f = ((I['vdate'] - date(2026, 10, 1)).days + 1) / 92.0
    nc30 = I['nc30'] + I['ltdep'] + I['ltinv'] - I['tax_owed'] - comp_owed(I)
    pre = nc30 - I['octset'] - I['other_out']
    nc_v = pre + f * fcf_q4
    div = I['q3div'] * I['sh'] / 1e6
    nc_e = pre + fcf_q4 - div - I['buy_cancel']
    return dict(nc30=nc30, nc_v=nc_v, nc_e=nc_e, fcf_q4=fcf_q4, wc_q4=wc, tax_q4=tax, f=f,
                comp=comp_owed(I), div=div)


def build(s, I, **ov):
    sh = I['sh'] / 1e6                       # m shares / 1e6: KRW tn / sh = KRW per share
    br = bridge(I)
    c27 = I['cons27'] * ov.get('cons_mult', 1.0)
    mem = list(ov.get('mem', I.get('mem_tab', MEM)[s]))
    if 'mem30_mult' in ov:
        mem[3] *= ov['mem30_mult']
    if 'mem2830_mult' in ov:
        mem = [mem[0]] + [x * ov['mem2830_mult'] for x in mem[1:]]
    if 'mem_all_mult' in ov:
        mem = [x * ov['mem_all_mult'] for x in mem]
    if 'mem30' in ov:
        mem[3] = ov['mem30']
    eps = [m * c27 for m in mem]             # 2027..2030
    idx = ov.get('idx', I.get('idx_tab', IDX)[s])
    rev = [x * I['rev26'] for x in idx]
    if ov.get('struct'):
        eps = [eps[3]] * 4
        rev = [rev[2]] * 3
    sc = ov.get('capex_s', s)
    capex = [c * ov.get('capex_mult', 1.0) for c in CAPEX[sc]]
    da = DA[sc]
    NI = [e * sh for e in eps[:3]]
    prev = 4 * I['q4']['rev']
    nc = br['nc_e'] + ov.get('nc_add', 0.0)
    pay = ov.get('payout', I['pay'])
    rem = ov.get('rem2026', I['rem2026'])
    dates = [I['d_buy'], I['d_div'], I['d_rem']]
    D = [I['buy_cancel'] / sh, I['q3div'], rem / sh]
    FCF, MFCF, GCX, PAID, NCs = [], [], [], [], []
    for i in range(3):
        dwc = I['wc'] * (rev[i] - prev)
        prev = rev[i]
        mfcf = NI[i] - dwc
        gcx = capex[i] - da[i]
        fcf = mfcf - gcx
        if 'cconv' in ov:
            fcf = ov['cconv'][i] * NI[i]
            mfcf = fcf + gcx
        ret = max(pay * fcf, 0.0)
        paid = ret + (rem if i == 0 else 0.0)
        dates.append(date(2027 + i, 7, 1)); D.append(ret / sh)
        nc = nc + fcf - paid
        FCF.append(fcf); MFCF.append(mfcf); GCX.append(gcx); PAID.append(paid); NCs.append(nc)
    nc_sh = [x / sh for x in NCs]
    P = I['P']
    k0 = kio(I) * ov.get('kio_mult0', 1.0)
    km = ov.get('kio_m', KIOM[s])
    kio_t = [k0 / sh * (1 + (km - 1) * (j + 1) / 3) for j in range(3)]
    nce = (br['nc_e'] + ov.get('nc_add', 0.0)) / sh
    pe0 = (P - nce - k0 / sh) / eps[0]
    pe = ov.get('pe', EXPE[s])
    cw = ov.get('cash_w', 1.0)
    if ov.get('capped'):
        cap = (P - nce - k0 / sh) / I['cons27']
        pes = [cap] * 3
    elif s == 'Bear' and not ov.get('glide'):
        pes = [pe] * 3
    else:
        pes = [pe0 + (pe - pe0) * (j + 1) / 3 for j in range(3)]
    tail = (eps[2] - eps[3]) * (2 / 3 / 1.08 + 1 / 3 / 1.08 ** 2) if ov.get('tail') else 0.0
    VT = pes[2] * eps[3] + cw * nc_sh[2] + kio_t[2] + tail
    Vint = [pes[j] * eps[j + 1] + nc_sh[j] + kio_t[j] for j in range(2)]
    V26 = P + (br['nc_e'] - br['nc_v']) / sh
    book = [I['book26']]
    for i in range(3):
        book.append(book[-1] + NI[i] - PAID[i])
    return dict(s=s, sh=sh, br=br, eps=eps, rev=rev, NI=NI, FCF=FCF, MFCF=MFCF, GCX=GCX, PAID=PAID,
                NC=NCs, nc_sh=nc_sh, dates=dates, D=D, VT=VT, pes=pes, pe0=pe0, Vint=Vint, V26=V26,
                kio_t=kio_t, k0=k0, P=P, vd=I['vdate'], capex=capex, da=da, book=book, tail=tail)


def yf(d, v0):
    return (d - v0).days / 365.0


def npv(r, P, dates, D, VT, vd, ex=EXIT):
    return -P + sum(x / (1 + r) ** yf(d, vd) for d, x in zip(dates, D)) + VT / (1 + r) ** yf(ex, vd)


def irr(P, dates, D, VT, vd, fx=None, ex=EXIT):
    if fx is not None:
        D = [x * (fx[d.year - 2027] if d.year >= 2027 else 1.0) for d, x in zip(dates, D)]
        VT = VT * fx[2]
    lo, hi = -0.95, 5.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(mid, P, dates, D, VT, vd, ex) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def pk(dates, D, VT, vd, k=0.12):
    return sum(x / (1 + k) ** yf(d, vd) for d, x in zip(dates, D)) + VT / (1 + k) ** yf(EXIT, vd)


def res(s, I, P=None, **ov):
    r = build(s, I, **ov)
    P = r['P'] if P is None else P
    r['irr'] = irr(P, r['dates'], r['D'], r['VT'], r['vd'])
    r['pk'] = pk(r['dates'], r['D'], r['VT'], r['vd'])
    r['T'] = yf(EXIT, r['vd'])
    return r
