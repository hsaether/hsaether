# Samsung Electronics (docs/samsung-analysis.md) -- IAF model, version 4.1 (23 Nov 2026 price re-mark = V41); version 4 (19 Nov 2026; V4: AI BBB 18 Nov H2 turn call,
# Base .90/.50/.32/.28, index 1.38/1.08/0.95; Seoul close 19 Nov; consensus 77,775); version 3 (16 Nov 2026).
# Rebuilt from version 2's published inputs (29 Oct 2026; the v2 scripts were not kept): with
# V2 settings it reproduces v2 (Base 23.3%, P_k 306,225). iaf-valuation 2026-11-12.1.
# Track B: memory = AI BBB H2 EPS path x memory share of CY27 consensus; non-memory own [A];
# V_T = exit P/E x 2030 core EPS + net cash at exit. KRW tn unless per share (KRW).
from datetime import date

EXIT = date(2029, 12, 31)
TAX = 0.24

MEM = {'Bear': [.60, .30, .25, .25], 'Base': [.90, .60, .40, .35], 'Bull': [1.00, .80, .55, .45]}
IDX = {'Bear': [1.00, .72, .67], 'Base': [1.38, 1.18, 1.03], 'Bull': [1.50, 1.33, 1.18]}
MEM18 = dict(MEM, Base=[.90, .50, .32, .28])     # AI BBB 18 Nov turn call (60%)
IDX18 = dict(IDX, Base=[1.38, 1.08, 0.95])
NMREV = {'Bear': [-15, -20, -15], 'Base': [0, 0, 0], 'Bull': [5, 10, 15]}
DX = {'Bear': [-2, 4, 7, 8], 'Base': [2, 7, 10, 12], 'Bull': [0, 2, 5, 8]}
SDC = {'Bear': [2, 2.5, 3, 3], 'Base': [3.5, 4, 4, 4], 'Bull': [4, 4.5, 4.5, 4.5]}
HAR = {'Bear': [1.2, 1.4, 1.6, 1.6], 'Base': [1.8, 1.9, 2.0, 2.0], 'Bull': [2.0, 2.1, 2.2, 2.2]}
LSI = {'Bear': [-3, -3, -2, -1], 'Base': [-1, .5, 2, 3], 'Bull': [0, 2, 4, 5]}
OTH = {'Bear': .8, 'Base': 1.0, 'Bull': 1.2}
CAPEX = {'Bear': [85, 65, 55], 'Base': [100, 105, 95], 'Bull': [110, 125, 125]}
DA = {'Bear': [57, 62, 65], 'Base': [58, 66, 73], 'Bull': [59, 69, 78]}
EXPE = {'Bear': 8.0, 'Base': 10.0, 'Bull': 11.0}
CBUY = {'Bear': .70, 'Base': .60, 'Bull': .55}      # H2 cash conversion used in the buyer's return
I44 = {'Bear': [1.08, 1.06, 1.06], 'Base': [1, 1, 1], 'Bull': [.98, .98, .98]}  # Equity BBB NOK path


def years():
    return [2027, 2028, 2029]


# ---------------------------------------------------------------- inputs per version
V2 = dict(P=232000.0, vdate=date(2026, 10, 29), shares=6.569, eps_basis=6.569, cons27=72281.41,
          mem26=491.3, nm26=216.8, sdc_own=0.848, rem2026=65.0, pay=0.5, floor=9.8,
          bridge='v2', nc30sep=197.6, tax_owed=24.4, bonus_owed=17.4, q3div=30.0,
          q4=dict(rev=207.4, q3rev=195.3, op=116.8, dsop=116.6, da=12.2, intr=1.5, capex=27.5),
          ltdep=0.0, prepay=0.0, opi9m=0.0, buyq4=0.0, sbp30sep=0.0, sbpq4oth=0.0, treas=0.0,
          wc=0.15, rate=0.025, capex_mult=1.0, book26=659.5, Ppref=183900.0)

V3 = dict(V2, P=196800.0, vdate=date(2026, 11, 16), shares=6.64865, eps_basis=6.5596, cons27=77323.65,
          sdc_own=0.892, bridge='v3', ltdep=34.73, prepay=10.17, opi9m=3.74, buyq4=2.47,
          sbp30sep=27.21, sbpq4oth=0.30, treas=136.722, book26=662.3, Ppref=161300.0)
# V4: Seoul close 19 Nov (common 195,000, preference 155,900); Yahoo CY27 consensus 77,774.66 (34; 19 Nov);
# AI BBB 18 Nov H2 Base path. Bridge as V3 (no new report).
V4 = dict(V3, P=195000.0, vdate=date(2026, 11, 19), cons27=77774.66, Ppref=155900.0, mem_tab=MEM18, idx_tab=IDX18)
# V4.1 (price re-mark, 23 Nov 2026): Seoul close 23 Nov (common 177,500, preference 140,900). Paths, consensus, bridge as V4.
V41 = dict(V4, P=177500.0, vdate=date(2026, 11, 23), Ppref=140900.0)
# V3 sources: DART quarterly report (filed 16 Nov 2026) for the 30 Sep balance sheet, the 2026
# long-term financial products (net 34.73), contract liabilities (24.15 vs 13.98), treasury shares
# (127.67m at 30 Sep + 9.06m bought after), the share-based payment reserve (27.21) and the
# Samsung Display stake (89.2%); Yahoo for prices (16 Nov) and CY27 consensus (77,323.65; 33).


def bridge(I):
    """Net cash (KRW tn) at the valuation date and at 31 Dec 2026, plus the parts."""
    q = I['q4']
    wc = I['wc'] * 4 * (q['rev'] - q['q3rev'])
    tax = TAX * (q['op'] + q['intr'])
    award_q4 = 0.105 * q['dsop'] if I['bridge'] == 'v3' else 0.0
    fcf_q4 = q['op'] + award_q4 + q['da'] + q['intr'] - tax - q['capex'] - wc
    vd = I['vdate']
    f = ((vd - date(2026, 10, 1)).days + 1) / 92.0   # Q4 days elapsed incl. the valuation date (v2: 29/92)
    if I['bridge'] == 'v2':
        adj = I['nc30sep'] - I['tax_owed'] - I['bonus_owed'] - I['q3div']
        nc_v = adj + f * fcf_q4
        nc_e = adj + fcf_q4
        short_v = short_e = 0.0
    else:
        adj = I['nc30sep'] + I['ltdep'] - I['tax_owed'] - I['opi9m'] - I['prepay'] - I['q3div']
        tv = I['treas'] * I['P'] / 1e6          # treasury shares held for awards, KRW tn at the price
        short_v = max(0.0, I['sbp30sep'] + f * (award_q4 + I['sbpq4oth']) - tv)
        short_e = max(0.0, I['sbp30sep'] + award_q4 + I['sbpq4oth'] - tv)
        nc_v = adj + f * fcf_q4 - I['buyq4'] - short_v
        nc_e = adj + fcf_q4 - I['buyq4'] - short_e
    return dict(nc_v=nc_v, nc_e=nc_e, fcf_q4=fcf_q4, wc_q4=wc, tax_q4=tax, award_q4=award_q4,
                adj30=adj, f=f, short_v=short_v, short_e=short_e)


def mem1(I):
    """Memory earnings = 1.00 of the H2 path: CY27 consensus NI less 10tn non-memory OP and
    10tn financial income after tax [A]."""
    return I['cons27'] * I['eps_basis'] / 1000.0 - 20 * (1 - TAX)


def nonmem(s, I, ov):
    if ov.get('nm_zero'):
        return [0.0] * 4
    k = ov.get('dx_mult', 1.0)
    return [DX[s][i] * k + SDC[s][i] * I['sdc_own'] + HAR[s][i] + LSI[s][i] + OTH[s] for i in range(4)]


def build(s, I, **ov):
    """One scenario. ov: overrides (mem, idx, pe, capex, nm, payout, cash50, tail, struct, capped,...)."""
    sh = I['shares'] / 1000.0          # bn shares / 1000: KRW tn / sh = KRW per share
    br = bridge(I)
    M1 = mem1(I) * ov.get('cons_mult', 1.0)
    mem = list(ov.get('mem', I.get('mem_tab', MEM)[s]))
    if 'mem30_mult' in ov:
        mem[3] *= ov['mem30_mult']
    if 'mem2830_mult' in ov:
        mem = [mem[0]] + [x * ov['mem2830_mult'] for x in mem[1:]]
    if 'mem_all_mult' in ov:
        mem = [x * ov['mem_all_mult'] for x in mem]
    if 'mem30' in ov:
        mem[3] = ov['mem30']
    sn = ov.get('nm_s', s)
    nm = nonmem(sn, I, ov)
    idx = ov.get('idx', I.get('idx_tab', IDX)[s])
    nmrev = NMREV[ov.get('nmrev_s', s)]
    sc = ov.get('capex_s', s)
    capex = [c * ov.get('capex_mult', 1.0) for c in CAPEX[sc]]
    da = DA[sc]
    rev = [idx[i] * I['mem26'] + I['nm26'] + nmrev[i] for i in range(3)]
    core = [mem[i] * M1 + nm[i] * (1 - TAX) for i in range(4)]   # core NI 2027..2030
    if ov.get('struct'):                                             # structural run
        core = [core[3]] * 3 + [core[3]]
        rev = [rev[2]] * 3
    nc = br['nc_e']
    q4run = 4 * I['q4']['rev']
    prev_rev = q4run
    NI, FCF, MFCF, GCX, PAID, NCs, RET, INT = [], [], [], [], [], [], [], []
    vd = I['vdate']
    dates, D = [], []
    pay = ov.get('payout', I['pay'])
    floor = 0.0 if pay == 0 else I['floor']
    rem = ov.get('rem2026', I['rem2026'])
    dates.append(date(2027, 4, 15)); D.append(rem)
    carry = 0.0
    for i, y in enumerate(years()):
        intr = nc * I['rate'] * (1 - TAX)
        ni = core[i] + intr
        dwc = I['wc'] * (rev[i] - prev_rev)
        prev_rev = rev[i]
        mfcf = ni - dwc
        gcx = capex[i] - da[i]
        fcf = mfcf - gcx
        if 'cconv' in ov:                                            # AI BBB H2 cash conversion
            fcf = ov['cconv'][i] * core[i] + intr
            mfcf = fcf + gcx
        ret = max(pay * fcf, floor) if fcf > 0 else floor
        paid = (carry if i > 0 else 0.0) + 0.3 * ret
        if i == 0:
            paid += rem
        else:
            dates.append(date(y, 4, 15)); D.append(carry)
        dates.append(date(y, 11, 15)); D.append(0.3 * ret)
        carry = 0.7 * ret
        nc = nc + fcf - paid
        NI.append(ni); FCF.append(fcf); MFCF.append(mfcf); GCX.append(gcx); PAID.append(paid)
        NCs.append(nc); RET.append(ret); INT.append(intr)
    eps = [x / sh for x in NI]
    core_eps = [x / sh for x in core]
    nc_sh = [x / sh for x in NCs]
    Dsh = [x / sh for x in D]
    pe = ov.get('pe', EXPE[s])
    P = I['P']
    nc_e_sh = br['nc_e'] / sh
    core27b = (I.get('mem_tab', MEM)['Base'][0] * M1 + nonmem('Base', I, ov)[0] * (1 - TAX)) / sh
    core_pe0 = (P - nc_e_sh) / core27b                                 # today's core P/E (Base 2027)
    cash_w = 0.5 if ov.get('cash50') else 1.0
    if ov.get('capped'):
        cap = (P - nc_e_sh) / I['cons27']
        pes = [cap, cap, cap]
    elif s == 'Bear':
        pes = [pe, pe, pe]                                             # Bear: exit P/E from end-2027
    else:
        pes = [core_pe0 + (pe - core_pe0) * (k + 1) / 3 for k in range(3)]
    tail = 0.0
    if ov.get('tail'):
        tail = (core_eps[2] - core_eps[3]) * (2 / 3 / 1.08 + 1 / 3 / 1.08 ** 2)
    VT = pes[2] * core_eps[3] + cash_w * nc_sh[2] + tail
    Vint = [pes[0] * core_eps[1] + nc_sh[0], pes[1] * core_eps[2] + nc_sh[1]]
    stub_cash = (br['nc_e'] - br['nc_v']) / sh
    V26 = P + stub_cash
    # book (controlling equity) path
    book = [I.get('book26', 0.0)]
    for i in range(3):
        book.append(book[-1] + NI[i] - PAID[i])
    if 'pb_exit' in ov:
        VT = ov['pb_exit'] * book[3] / sh
    return dict(s=s, sh=sh, br=br, M1=M1, mem=mem, nm=nm, rev=rev, core=core, NI=NI, FCF=FCF, MFCF=MFCF,
                GCX=GCX, PAID=PAID, NC=NCs, RET=RET, INT=INT, eps=eps, core_eps=core_eps, nc_sh=nc_sh,
                dates=dates, D=Dsh, VT=VT, pes=pes, core_pe0=core_pe0, Vint=Vint, V26=V26,
                stub_cash=stub_cash, P=P, vd=vd, capex=capex, da=da, book=book, tail=tail)


def yf(d, v0):
    return (d - v0).days / 365.0


def npv(r, P, dates, D, VT, vd):
    return -P + sum(x / (1 + r) ** yf(d, vd) for d, x in zip(dates, D)) + VT / (1 + r) ** yf(EXIT, vd)


def irr(P, dates, D, VT, vd, fx=None):
    if fx is not None:
        D = [x * fx[d.year - 2027] for d, x in zip(dates, D)]
        VT = VT * fx[2]
    lo, hi = -0.9, 3.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(mid, P, dates, D, VT, vd) > 0:
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
