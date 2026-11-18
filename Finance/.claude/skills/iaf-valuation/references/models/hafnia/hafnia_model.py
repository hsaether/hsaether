"""Hafnia IAF model (docs/hafnia-analysis.md), v8 of 18 Nov 2026.

Rebuilt in this run: the v1-v7 scripts were kept only in a scratchpad and are lost. Built from v7's
published method and inputs, re-based on the Q3 2026 report (30 Sep balance sheet, broker values,
Q4 and 2027 cover, TC-in purchase options) and Oil Shipping BBB of 13 Nov 2026.

Engine: quarterly Q4-26 to Q4-29, consolidated fleet by segment (LR2, LR1, MR, Handy), JV share,
cash flows to net debt, dividends by Hafnia's LTV payout rule, NAV marks, V_T, reversion tail.
Paths: 'A' = TORM shares distributed as the special dividend (replaces Q3 and Q4 2026 cash
dividends; the board's preference); 'B' = cash fallback (Q3 90% cash, Q4 by policy, TORM held).
Standard library only. Run from this folder: py hafnia_run.py
"""
import datetime as dt

VAL = dt.date(2026, 11, 18)          # valuation date
EXIT = dt.date(2029, 12, 31)
T = (EXIT - VAL).days / 365.0
P_NOK = 90.00                         # HAFNI.OL close 17 Nov 2026 (Yahoo; last print 15:27 UTC)
FX = 9.6243                           # USD/NOK, Yahoo NOK=X 15-min bar 15:15 UTC 17 Nov (Norges Bank fixing 9.6237)
SH = 535.331154 + 6.549              # issued 535.33m + option dilution (diluted - basic, Q3 weighted)
SH_ISSUED = 535.331154
K = 0.12

# ---------------- quarter grid ----------------
QS = []
for y in (2026, 2027, 2028, 2029):
    for q in (1, 2, 3, 4):
        if y == 2026 and q < 4:
            continue
        s = dt.date(y, 3 * q - 2, 1)
        e = dt.date(y + (q == 4), 1 if q == 4 else 3 * q + 1, 1) - dt.timedelta(days=1)
        QS.append(dict(y=y, q=q, lab=f"Q{q}-{str(y)[2:]}", s=s, e=e, d=(e - s).days + 1))

def qidx(y, q):
    for i, x in enumerate(QS):
        if x['y'] == y and x['q'] == q:
            return i

# ---------------- sector rows (Oil Shipping BBB 13 Nov 2026; $k/day) ----------------
ROWS = {
    'Base': {'LR2': {2027: [114, 63, 43, 40], 2028: 38, 2029: 35, 'mc': 30},
             'LR1': {2027: [69, 44, 33, 34], 2028: 30, 2029: 28, 'mc': 25},
             'MR':  {2027: [48, 36, 31, 33], 2028: 25, 2029: 22, 'mc': 21}},
    'Bear': {'LR2': {2027: [55, 35, 28, 26], 2028: 29, 2029: 25, 'mc': 24},
             'LR1': {2027: [38, 28, 24, 22], 2028: 23, 2029: 20, 'mc': 20},
             'MR':  {2027: [28, 21, 19, 20], 2028: 19, 2029: 17, 'mc': 17}},
    'Bull': {'LR2': {2027: [260, 160, 115, 105], 2028: 72, 2029: 55, 'mc': 37},
             'LR1': {2027: [150, 100, 80, 70], 2028: 48, 2029: 38, 'mc': 31},
             'MR':  {2027: [75, 58, 50, 49], 2028: 33, 2029: 27, 'mc': 26}},
}
HANDY_X = 0.90                         # Handy = 0.90 x MR [A]
Q4_OPEN = {'LR2': 125.0, 'LR1': 105.0, 'MR': 56.0}   # baseline Nov-Dec market level, open days from mid-Nov
# 5-yr values $m: anchor 28 Sep (= Hafnia 30 Sep broker date), now (Xclusiv 9 Nov; LR1 Intermodal Oct), mid-cycle
V_ANCHOR = {'LR2': 85.0, 'LR1': 60.0, 'MR': 50.0}
V_NOW = {'LR2': 90.0, 'LR1': 68.0, 'MR': 53.0}
V_MC = {'Bear': {'LR2': 52.0, 'LR1': 42.0, 'MR': 32.0},
        'Base': {'LR2': 73.0, 'LR1': 59.0, 'MR': 46.0},
        'Bull': {'LR2': 98.0, 'LR1': 80.0, 'MR': 64.0}}

def seg_row(seg):
    return 'MR' if seg == 'Handy' else seg

def rate(scen, seg, y, q, struct=False, fac=1.0, lr1_2027=None):
    r = ROWS[scen][seg_row(seg)]
    if struct and y >= 2027:
        v = r['mc']
    elif y == 2027:
        v = r[2027][q - 1]
        if lr1_2027 and seg_row(seg) == 'LR1':
            v *= lr1_2027 / 45.0
    else:
        v = r[y]
    if seg == 'Handy':
        v *= HANDY_X
    return v * (fac if y >= 2027 else 1.0)

def age_factor(a):
    if a < 5:
        return 1.10 - 0.02 * a
    if a <= 15:
        return 1 - 0.04 * (a - 5)
    return max(0.15, 0.60 - 0.05 * (a - 15))

# ---------------- company inputs (Q3 2026 report unless stated) ----------------
SEGS = ['LR2', 'LR1', 'MR', 'Handy']
BV30 = {'LR2': 547.0, 'LR1': 1078.0, 'MR': 1634.0, 'Handy': 741.0}   # owned 100%, $4,000m [F]; LR2/LR1 split of Vista [A]
AGE30 = {'LR2': 7.25, 'LR1': 10.05, 'MR': 11.05, 'Handy': 11.25}     # value-weighted ages at 30 Sep [A]
JV_BV = {'LR2': 204.0, 'LR1': 192.0, 'MR': 125.0}                    # JV share $521m [F]; Vista split [A]
JV_AGE = {'LR2': 3.3, 'LR1': 7.1, 'MR': 1.0}
JV_N = {'LR2': 2.0, 'LR1': 3.0, 'MR': 2.0}                           # Hafnia 50% share, vessel-equivalents
OPT_V30 = {'LR1': 2 * 54.7, 'MR': 6 * 44.0}                         # 8 option vessels at 30 Sep marks [A]
OPT_AGE = {'LR1': 7.2, 'MR': 8.0}
OPT_STRIKE = 235.0                                                   # [F] approx. total
OPT_ITM_ALL = 161.0                                                  # [F] exercisable options, 11 vessels, 30 Sep
OPT_Q = (2027, 2)                                                    # exercised end Q2-27 [A]
ND30 = 862.387 + 32.913 + 3.4 - 299.481                              # bank + SLB + office leases - cash at bank [F]
POOL_FAC = 90.5
TC_LEASE = 75.6
NWC = 383.7                                                          # incl. pool cash, restricted cash [F]
OTHER = 12.6 + 7.9 + 9.7                                             # unquoted inv., Complexio loan, net derivatives [F]
JV_ND30 = 202.65 - 15.0                                              # Hafnia share of JV debt [F] less JV cash [A]
BOOK30 = 3071.711
TORM_N = 20.356061
TORM_PX = 33.73                                                      # 17 Nov close, ex the $1.35 dividend
TORM_FV30 = 774.837
TORM_COST = 515.4                                                    # Q3 deck p.26 [F]
TORM_DIV_Q4 = 1.35 * TORM_N                                          # ex 16/17 Nov, paid 2 Dec: Hafnia receives it
TORM_SH = 102.71
TORM_FLEET30, TORM_ND30 = 4333.0, 271.0                              # TORM Q3 (30 Sep) [F]
TORM_FAC = {'Bear': 0.64, 'Base': 0.92, 'Bull': 1.25}                # TORM fleet mid-cycle factor vs 30 Sep [A]
NB_COST = 503.6
NB_PAID30 = 100.72
NB_CAPEX = {'Q4-26': 50.0, 'Q1-27': 7.75, 'Q2-27': 7.75, 'Q3-27': 7.75, 'Q4-27': 7.75,
            'Q1-28': 54.75, 'Q2-28': 54.75, 'Q3-28': 54.75, 'Q4-28': 54.75,
            'Q1-29': 25.5, 'Q2-29': 25.5, 'Q3-29': 25.5, 'Q4-29': 25.5}   # Q3 deck p.26: Q4-26 50, 2027 31, 2028 219, 2029 102 [F]
NB_DELIV = {'Q3-28': (2, 47), 'Q4-28': (2, 47), 'Q1-29': (2, 44), 'Q2-29': (2, 47), 'Q3-29': (2, 47)}

# Q4-26 company data [F]: earning days and cover by segment (Hafnia fleet), 13 Nov
Q4_DAYS = {'LR2': 548.0, 'LR1': 1962.0, 'MR': 4577.0, 'Handy': 1839.0}
Q4_COV = {'LR2': (1.00, 34.000), 'LR1': (0.64, 97.841), 'MR': (0.71, 49.678), 'Handy': (0.85, 38.753)}
JV_Q4 = {'LR2': (184.0, 1.00, 25.875), 'LR1': (267.6, 0.76, 79.111), 'MR': (183.0, 1.00, 24.5)}
COV27 = {'LR2': (0.90, 34.288), 'LR1': (0.03, 27.988), 'MR': (0.21, 24.813), 'Handy': (0.15, 23.469)}
JV_COV27 = {'LR2': (1.00, 25.875), 'LR1': (0.17, 24.0), 'MR': (1.00, 24.5)}

UTIL = 0.97
OPEX = {2026: 9.0, 2027: 9.27, 2028: 9.55, 2029: 9.83}
JV_OPEX = {2026: 9.5, 2027: 9.8, 2028: 10.1, 2029: 10.4}
TCIN = {'LR1': {2026: 19.6, 2027: 19.8}, 'MR': {2026: 18.0, 2027: 18.2, 2028: 19.4, 2029: 19.9}}
GA = {2026: 24.0, 2027: 24.0, 2028: 24.7, 2029: 25.5}                # $m a quarter
FEE = 7.0
OTH_HIRE = {2026: 3.0, 2027: 3.0, 2028: 1.5, 2029: 1.5}
DA_OWN = {2026: 40.0, 2027: 39.5, 2028: 38.0, 2029: 36.5}
MCAPEX = {2026: 12.0, 2027: 17.5, 2028: 17.5, 2029: 17.5}
AMORT = {2026: 3.6, 2027: 3.55, 2028: 3.5, 2029: 3.5}               # scheduled ($84m facility + SLB), a quarter
TAX_Q = 1.25
R_DEBT, FIN_FIX = 0.05, 2.0
PAYDATE = {1: (6, 18), 2: (9, 23), 3: (12, 15), 4: (3, 20)}
SPECIAL_DATE = dt.date(2026, 12, 15)                                 # [A]


def payout_rule(ltv, y, q, new_from=(2027, 1)):   # Q3 deck p.6: from Q1 2027, fully committed LTV [F]
    if (y, q) >= new_from and ltv < 0.10:
        return 1.00
    if ltv <= 0.20:
        return 0.90
    if ltv <= 0.30:
        return 0.80
    if ltv <= 0.40:
        return 0.60
    return 0.50


def glide(scen, t_idx, seg):
    """value index vs anchor at year-end t_idx (0 = YE26 ... 3 = YE29)."""
    s = seg_row(seg)
    f0 = V_NOW[s] / V_ANCHOR[s]
    f1 = V_MC[scen][s] / V_ANCHOR[s]
    return f0 + (f1 - f0) * t_idx / 3.0


def yrs_from_30sep(d):
    return (d - dt.date(2026, 9, 30)).days / 365.0


def fleet_value(scen, d, f_by_seg, n_nb_deliv=0):
    """owned fleet + option vessels + JV vessels at value index f_by_seg (dict) and date d."""
    a = yrs_from_30sep(d)
    own = sum(BV30[s] * f_by_seg[s] * age_factor(AGE30[s] + a) / age_factor(AGE30[s]) for s in SEGS)
    opt = sum(OPT_V30[s] * f_by_seg[s] * age_factor(OPT_AGE[s] + a) / age_factor(OPT_AGE[s]) for s in OPT_V30)
    jv = sum(JV_BV[s] * f_by_seg[s] * age_factor(JV_AGE[s] + a) / age_factor(JV_AGE[s]) for s in JV_BV)
    return own, opt, jv


def run(scen='Base', path='A', struct=False, fac=1.0, q4fac=1.0, tail_on=True, val_mult=1.0,
        exit_scen=None, payout_fixed=None, torm_px=TORM_PX, lr1_2027=None, rate_mult=1.0,
        exit_disc=None, overhead=0.0, fx_path=None, q4_scale=1.0, bv_scale=None, torm_jun=False):
    """Return dict with quarterly rows, dividends (date, $m), V_T etc. Prices of the paths in $m."""
    xs = exit_scen or scen
    rows = []
    nd = ND30
    jv_nd = JV_ND30
    nb_paid = NB_PAID30
    prev_np = 170.765
    divs = []          # (date, $m, label)
    torm_held = True
    book = BOOK30
    cum = dict(mfcf=0.0, divpaid=0.0, ret=0.0, nb=0.0, opt=0.0, torm_div=0.0)
    for i, Q in enumerate(QS):
        y, q, d = Q['y'], Q['q'], Q['d']
        r = {'lab': Q['lab'], 'y': y, 'q': q}
        # fleet counts
        lr1_tc = 2.0 if (y, q) <= OPT_Q else 0.0
        mr_tc = 9.0 if (y, q) <= OPT_Q else 3.0
        lr1_own = 20.0 + (2.0 if (y, q) > OPT_Q else 0.0)
        mr_own = 41.0 + (6.0 if (y, q) > OPT_Q else 0.0)
        nb_avg = 0.0
        delivered = 0
        for lab, (n, dd) in NB_DELIV.items():
            j = [k for k, x in enumerate(QS) if x['lab'] == lab][0]
            if j < i:
                delivered += n
            elif j == i:
                delivered += n
                nb_avg -= n * (1 - dd / d)
        nb_avg += delivered
        cnt_own = {'LR2': 6.0, 'LR1': lr1_own, 'MR': mr_own + nb_avg, 'Handy': 20.0}
        cnt_tc = {'LR2': 0.0, 'LR1': lr1_tc, 'MR': mr_tc, 'Handy': 0.0}
        tce = 0.0
        tce_seg = {}
        days_tot = 0.0
        for s in SEGS:
            if y == 2026:
                ed = Q4_DAYS[s]
                c, cr = Q4_COV[s]
                op = Q4_OPEN[seg_row(s)] * (HANDY_X if s == 'Handy' else 1.0) * q4fac
                v = ed * c * cr + ed * (1 - c) * op
            else:
                ed = (cnt_own[s] + cnt_tc[s]) * d * UTIL
                if y == 2027:
                    c, cr = COV27[s]
                elif y == 2028 and q <= 3 and s == 'LR2':
                    c, cr = 0.90, 34.288
                else:
                    c, cr = 0.0, 0.0
                op = rate(scen, s, y, q, struct, fac, lr1_2027) * rate_mult
                v = ed * c * cr + ed * (1 - c) * op
            tce += v / 1000.0
            tce_seg[s] = v / 1000.0
            days_tot += ed
        if y == 2026:
            tce = tce * q4_scale - 3.9                   # Oct FFA losses [F]
        own_cal = (6 + lr1_own + mr_own + nb_avg + 20) * d
        opex = own_cal * OPEX[y] / 1000.0
        tc_hire = (cnt_tc['LR1'] * d * TCIN['LR1'].get(y, 0) + cnt_tc['MR'] * d * TCIN['MR'][y]) / 1000.0
        lease = 0.5 * tc_hire
        ch_ebitda = 0.5 * tc_hire + OTH_HIRE[y]
        torm_div = 0.0
        if y == 2026:
            torm_div = TORM_DIV_Q4
        elif path == 'B' and torm_held:
            torm_div = 0.008 * prev_np * TORM_N
        ebitda = tce + FEE + torm_div - opex - ch_ebitda - GA[y]
        # JV (Hafnia share)
        jv_tce = 0.0
        for s in ('LR2', 'LR1', 'MR'):
            if y == 2026:
                ed, c, cr = JV_Q4[s]
                op = Q4_OPEN[s] * q4fac
            else:
                ed = JV_N[s] * d * UTIL
                if y == 2027:
                    c, cr = JV_COV27[s]
                elif s == 'MR':
                    c, cr = 1.0, 24.5                     # Ecomar TC assumed to 2029 [A]
                else:
                    c, cr = 0.0, 0.0
                op = rate(scen, s, y, q, struct, fac, lr1_2027) * rate_mult
            jv_tce += (ed * c * cr + ed * (1 - c) * op) / 1000.0
        jv_ebitda = jv_tce - sum(JV_N.values()) * d * JV_OPEX[y] / 1000.0 - 0.5
        jv_int = 0.06 * jv_nd / 4
        jv_np = jv_ebitda - 3.5 - jv_int
        jv_nd -= (jv_ebitda - jv_int - 0.5)
        # holdco
        nb_cap = NB_CAPEX[Q['lab']]
        opt_cap = OPT_STRIKE if (y, q) == OPT_Q else 0.0
        interest = R_DEBT * nd / 4 + FIN_FIX
        tax = 1.2 if y == 2026 else TAX_Q
        mcap = MCAPEX[y]
        da = DA_OWN[y] + (3.5 if (y, q) > OPT_Q else 0.0) + 1.9 / 4 * nb_avg
        np_ = ebitda - lease - da - interest + jv_np - tax          # lease proxy = ROU dep + lease interest
        mfcf = ebitda - tax - interest - lease - mcap
        # cash paid in this quarter: dividends whose pay date falls inside the quarter
        paid = 0.0
        if y == 2026 and path == 'B':
            divs.append((dt.date(2026, 12, 15), 0.9 * 170.765, 'Q3-26 cash'))
            paid += 0.9 * 170.765
        for (pd_, amt, lab) in list(divs):
            if Q['s'] <= pd_ <= Q['e'] and lab != 'Q3-26 cash':
                paid += amt
        # special dividend (path A) in Q4-26: TORM out, non-cash
        if y == 2026 and path == 'A':
            torm_held = False
            book -= TORM_N * torm_px
        retained = mfcf - nb_cap - opt_cap - paid
        nd -= retained
        nb_paid += nb_cap
        # dividend declared for the quarter: payout by net LTV at quarter end (fully committed from 2027)
        nb_rem = NB_COST - nb_paid
        t_c = max(0.0, (Q['e'] - dt.date(2026, 12, 31)).days / 365.0)
        f_idx = {s: glide(xs, t_c, s) for s in SEGS}                  # scenario value glide for LTV [A]
        own_v, opt_v, _ = fleet_value(scen, Q['e'], f_idx)
        torm_v = min(TORM_COST, TORM_N * torm_px) if torm_held and path == 'B' else 0.0
        r_debt = nd - POOL_FAC + (TC_LEASE if (y, q) <= OPT_Q else 35.0)
        if y >= 2027:
            ltv = (r_debt + nb_rem) / (own_v + (opt_v if (y, q) > OPT_Q else 0) + NB_COST + torm_v)
        else:
            ltv = r_debt / (own_v + nb_paid + torm_v)
        if payout_fixed is not None:
            po = payout_fixed
        else:
            po = payout_rule(ltv, y, q)
        if np_ <= 0:
            po = 0.0
        dec = po * max(np_, 0.0)
        if y == 2026:
            dec = 0.0 if path == 'A' else dec
        m, dday = PAYDATE[q]
        pay = dt.date(y + (q == 4), m, dday)
        if dec > 0:
            divs.append((pay, dec, Q['lab']))
        book += np_ - dec
        cum['mfcf'] += mfcf; cum['divpaid'] += paid; cum['ret'] += retained
        cum['nb'] += nb_cap; cum['opt'] += opt_cap; cum['torm_div'] += torm_div
        r.update(tce=tce, days=days_tot, tce_day=tce / days_tot * 1000 if days_tot else 0, ebitda=ebitda,
                 np=np_, mfcf=mfcf, amort=AMORT[y], fcf_ads=mfcf - AMORT[y], nb=nb_cap, opt=opt_cap,
                 dec=dec, paid=paid, nd=nd, ltv=ltv, po=po, jv_np=jv_np, jv_nd=jv_nd, lease=lease,
                 torm_div=torm_div, tce_seg=tce_seg, opex=opex, interest=interest, da=da)
        rows.append(r)
        prev_np = np_ - (torm_div if path == 'B' else 0)               # TORM DPS rule on Hafnia own profit
    # Q4-29 dividend is declared after exit: it stays in V_T as cash (nd already excludes it)
    divs_in = [(d_, a, l) for (d_, a, l) in divs if d_ <= EXIT]
    # ---------------- V_T ----------------
    f_T = {s: V_MC[xs][seg_row(s)] / V_ANCHOR[seg_row(s)] * val_mult for s in SEGS}
    own_T, opt_T, jv_T = fleet_value(xs, EXIT, f_T)
    if bv_scale:
        own_T = sum(BV30[s_] * bv_scale[s_] * f_T[s_] * age_factor(AGE30[s_] + T + 0.13) / age_factor(AGE30[s_]) for s_ in SEGS)
        jv_T *= bv_scale['JV']
    nb_T = 10 * V_MC[xs]['MR'] * 1.08 * val_mult
    if exit_disc:
        own_T *= exit_disc; opt_T *= exit_disc; jv_T *= exit_disc; nb_T *= exit_disc
    torm_T = 0.0
    if path == 'B':
        torm_T = TORM_N * (TORM_FLEET30 * TORM_FAC[xs] * 0.82 - TORM_ND30) / TORM_SH
        if torm_jun:
            torm_T = TORM_N * (4056.0 * TORM_FAC[xs] * 0.82 - 319.0) / 102.4
    tail = 0.0
    tails = {}
    if tail_on and not struct:
        open_days = {'LR2': (6 + 2) * 365 * UTIL, 'LR1': (22 + 3) * 365 * UTIL}
        for s in ('LR2', 'LR1'):
            g = ROWS[scen][s][2029] - ROWS[scen][s]['mc']
            if abs(g) / ROWS[scen][s]['mc'] > 0.10:
                tails[s] = g * open_days[s] * (2 / 3 / 1.08 + 1 / 3 / 1.08 ** 2) / 1000.0
        tail = sum(tails.values())
    VT = own_T + opt_T + nb_T + jv_T - jv_nd + torm_T + NWC + OTHER - nd + tail - overhead
    return dict(rows=rows, divs=divs_in, divs_all=divs, nd=nd, jv_nd=jv_nd, VT=VT, own_T=own_T, opt_T=opt_T,
                nb_T=nb_T, jv_T=jv_T, torm_T=torm_T, tail=tail, tails=tails, book=book, cum=cum,
                path=path, scen=scen)


FRAC = (dt.date(2026, 12, 31) - VAL).days / 92.0          # share of Q4 after the valuation date (44/92)


def nd_at_val(res):
    """net debt at the valuation date: 30 Sep + the share of Q4 cash flow to 18 Nov (TORM dividend excluded)."""
    q4 = res['rows'][0]
    flow = q4['mfcf'] - q4['torm_div'] - q4['nb']
    return ND30 - (1 - FRAC) * flow


def jvnd_at_val(res):
    return JV_ND30 + (1 - FRAC) * (res['rows'][0]['jv_nd'] - JV_ND30)


def firm_premium(scen='Base', at=VAL):
    """PV at 8% of covered days x (covered rate - scenario mid-cycle day at 97%) after `at`, $m."""
    tot = 0.0
    for Q in QS:
        if Q['e'] <= at:
            continue
        y, q = Q['y'], Q['q']
        fr = FRAC if y == 2026 else 1.0
        tm = ((Q['s'] - at).days + Q['d'] / 2) / 365.0 if y > 2026 else 22 / 365.0
        for s in SEGS:
            mcd = ROWS[scen][seg_row(s)]['mc'] * (HANDY_X if s == 'Handy' else 1.0) * UTIL
            if y == 2026:
                c, cr = Q4_COV[s]
                days = Q4_DAYS[s] * c * fr
            elif y == 2027:
                c, cr = COV27[s]
                n = {'LR2': 6, 'LR1': 21.2, 'MR': 47.6, 'Handy': 20}[s]
                days = n * Q['d'] * UTIL * c
            elif y == 2028 and q <= 3 and s == 'LR2':
                cr, days = 34.288, 6 * Q['d'] * UTIL * 0.9
            else:
                continue
            tot += days * (cr - mcd) / 1000.0 / 1.08 ** tm
        for s in ('LR2', 'LR1', 'MR'):
            mcd = ROWS[scen][s]['mc'] * UTIL
            if y == 2026:
                ed, c, cr = JV_Q4[s]
                days = ed * c * fr
            elif y == 2027:
                c, cr = JV_COV27[s]
                days = JV_N[s] * Q['d'] * UTIL * c
            else:
                continue
            tot += days * (cr - mcd) / 1000.0 / 1.08 ** tm
    return tot


def nav_at_val(res, marks='Base', path='A', torm_px=TORM_PX):
    """NAV at the valuation date. marks: 'now' (market) or a scenario name (mid-cycle marks)."""
    if marks == 'now':
        f = {s: V_NOW[seg_row(s)] / V_ANCHOR[seg_row(s)] for s in SEGS}
    else:
        f = {s: V_MC[marks][seg_row(s)] / V_ANCHOR[seg_row(s)] for s in SEGS}
    own, opt, jv = fleet_value(marks, VAL, f)
    nb_paid = NB_PAID30 + (1 - FRAC) * res['rows'][0]['nb']
    if marks == 'now':
        nb = 10 * 52.5 - (NB_COST - nb_paid)
        opt_line = opt - OPT_STRIKE + (OPT_ITM_ALL - (sum(OPT_V30.values()) - OPT_STRIKE)) * f['MR']
        prem = 0.0
        torm = TORM_N * torm_px
    else:
        nb = nb_paid
        opt_line = opt - OPT_STRIKE
        prem = firm_premium(marks)
        if path == 'A':
            torm = TORM_N * torm_px
        else:
            torm = TORM_N * (TORM_FLEET30 * TORM_FAC[marks] - TORM_ND30) / TORM_SH
    jvnd = jvnd_at_val(res)
    nd = nd_at_val(res)
    tot = own + opt_line + nb + jv - jvnd + torm + TORM_DIV_Q4 + NWC + OTHER - nd + prem
    return dict(own=own, opt=opt_line, nb=nb, jv=jv, jvnd=jvnd, torm=torm, tdiv=TORM_DIV_Q4, nwc=NWC,
                other=OTHER, nd=nd, prem=prem, nav=tot, opt_vessels=opt, nb_paid=nb_paid)


def vt_interim(res, scen, yi):
    """V_t at year-end yi (0 = YE26, 1 = YE27, 2 = YE28), $m; glide from today's marks to mid-cycle."""
    d = dt.date(2026 + yi, 12, 31)
    f = {s: glide(scen, yi, s) for s in SEGS}
    own, opt, jv = fleet_value(scen, d, f)
    row = res['rows'][[i for i, r in enumerate(res['rows']) if r['y'] == 2026 + yi and r['q'] == 4][0]]
    nb_paid = NB_PAID30 + sum(r['nb'] for r in res['rows'] if r['y'] <= 2026 + yi)
    opt_line = opt - (OPT_STRIKE if yi == 0 else 0.0)
    torm = 0.0
    if res['path'] == 'B':
        t_exit = TORM_N * (TORM_FLEET30 * TORM_FAC[scen] * 0.82 - TORM_ND30) / TORM_SH
        torm = TORM_N * TORM_PX + (t_exit - TORM_N * TORM_PX) * yi / 3.0
    prem = firm_premium('Base', d) if yi == 0 else firm_premium(scen, d)
    return own + opt_line + nb_paid + jv - row['jv_nd'] + torm + NWC + OTHER - row['nd'] + prem


def xnpv(rate_, cfs):
    return sum(a / (1 + rate_) ** ((d - VAL).days / 365.0) for d, a in cfs)


def xirr(cfs):
    lo, hi = -0.9, 3.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if xnpv(mid, cfs) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def per_share_flows(res, path, fx=FX, torm_px=TORM_PX, fx_path=None):
    """NOK per share: D_t list (date, NOK) and V_T NOK. fx_path: {year: fx} for NOK path."""
    def f(d):
        if fx_path is None:
            return fx
        return fx_path.get(d.year, fx)
    ds = []
    if path == 'A':
        ds.append((SPECIAL_DATE, TORM_N * torm_px / SH_ISSUED * f(SPECIAL_DATE)))
    for d_, a, l in res['divs']:
        ds.append((d_, a / SH * f(d_)))
    vt = res['VT'] / SH * f(EXIT)
    return ds, vt


def decision(res, path, P=P_NOK, k=K, fx=FX, torm_px=TORM_PX, fx_path=None):
    ds, vt = per_share_flows(res, path, fx, torm_px, fx_path)
    cfs = [(VAL, -P)] + ds + [(EXIT, vt)]
    irr = xirr(cfs)
    pk = sum(a / (1 + k) ** ((d - VAL).days / 365.0) for d, a in ds) + vt / (1 + k) ** T
    return dict(irr=irr, pk=pk, mos=pk / P - 1, sumD=sum(a for _, a in ds), vt=vt, ds=ds)
