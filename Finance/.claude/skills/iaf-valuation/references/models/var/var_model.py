"""Vår Energi (VAR) IAF model - engine and inputs.
Document: docs/var-analysis.md, version 1.0, 25 Nov 2026 (skill iaf-valuation 2026-11-24.1).
Track B: E&P with explicit capex, Norwegian 78% tax modelled on a cash-flow basis.
Standard library only. Run var_run.py for the document's figures.

Simplifications (stated in the document):
- Norwegian tax = 78% x (EBITDAX - dev capex - exploration - abex) - 22% x net interest - shield
  (special tax expenses capex at once since 2022; CIT 6-year depreciation treated as expensed;
  'shield' = remaining pre-2022 depreciation and uplift, calibrated to 9M-2026 current tax).
  Paid 1/6 Q3, 2/6 Q4 of the income year and 1/6 Q1, 2/6 Q2 of the next year.
- Danish (BlueNord) tax 64% of (EBITDAX - capex - abex), paid in-year.
- Working capital zero; hedges ignored except the COP gas floor (Bear).
"""
import datetime as dt
import math

D = dt.date
VAL = D(2026, 11, 25)          # valuation date (price = Oslo close Tue 24 Nov 2026)
EXIT = D(2029, 12, 31)
P_NOK = 44.65                   # [F] Yahoo VAR.OL close 24 Nov 2026
USDNOK = 9.792                  # [F] Norges Bank fixing 24 Nov 2026
EURUSD = 10.735 / 9.792         # [F] Norges Bank EUR 10.735 / USD 9.792 = 1.0963
K = 0.12
ASSET_R = 0.08                  # asset rate: Vår impairment test and deal NPVs (8% post-tax nominal)
MWH_PER_BOE = 1.70              # 5.8 MMBtu/boe / 3.412 MMBtu/MWh

SH_OLD = 2496.406               # [F] Q3 note 17, m shares
SH_PP = 249.0                   # [F] placement 24 Nov 2026, NOK 42
SH_BN = 248.4                   # [F] BlueNord merger consideration
SHARES = SH_OLD + SH_PP + SH_BN  # from BlueNord closing (assumed 31 Dec 2026)

# periods: (label, years, end date, days)
PER = [("Q4-26", .25, D(2026, 12, 31), 92), ("Q1-27", .25, D(2027, 3, 31), 90),
       ("Q2-27", .25, D(2027, 6, 30), 91), ("Q3-27", .25, D(2027, 9, 30), 92),
       ("Q4-27", .25, D(2027, 12, 31), 92), ("2028", 1., D(2028, 12, 31), 366),
       ("2029", 1., D(2029, 12, 31), 365)]

# ---- scenario prices ---------------------------------------------------------
# Brent: docs/oil-market-bbb.md Interface (18 Nov 2026). Bear/Bull 2027 flat by quarter [A].
BRENT = {
    "Base": [97.1, 85, 82, 77, 76, 73, 72], "Bear": [97.1, 65, 65, 65, 65, 60, 60],
    "Bull": [97.1, 118, 118, 118, 118, 102, 90]}
BRENT_MID = {"Base": 70, "Bear": 60, "Bull": 82}
# TTF EUR/MWh. Base = ICE Endex settlements 24 Nov 2026 (Barchart grid) [E]; Q4-26 93 [E/A].
TTF = {
    "Base": [93, 90.0, 68.9, 63.4, 59.9, 39.6, 28.7],
    "Bear": [93, 75, 45, 40, 38, 28, 24], "Bull": [93, 110, 95, 90, 90, 60, 40]}
TTF_MID = {"Base": 28, "Bear": 22, "Bull": 36}

# ---- blocks -------------------------------------------------------------------
BLOCKS = {
    # Vår standalone (after Goliat 20% / Fenja 25% / Fram 5% exits); production from guidance
    # (Q4 implied by FY ~390) and the impairment-test profile (note 12: 438 mmboe Q4-26..2029).
    "VAR": dict(start=0, kboe=[410, 375, 375, 375, 375, 365, 357], mix=(.63, .32, .05),
                opex=[11.0, 11.5, 11.5, 11.5, 11.5, 12.0, 12.3], other=[75, 80, 80, 80, 80, 320, 320],
                capex=[750, 650, 650, 650, 650, 2500, 2300], expl=[90, 70, 70, 70, 65, 275, 275],
                abex=[100, 50, 50, 50, 50, 200, 200], lease=[34, 34, 34, 34, 34, 136, 136],
                shield=[175, 150, 150, 150, 150, 450, 300], tax=.78, nor=True,
                R_exit_2p=807, R_exit_2c=855 * .5, opex_post=14.0, capex_post=10.0,
                aro_after=0.22 * 3840, dda=24.0),
    # ConocoPhillips Norway, economic consolidation from 1 Apr 2027 (Q1-27 inside the $2.5bn).
    "COP": dict(start=2, kboe=[0, 0, 115, 115, 115, 113, 108], mix=(.47, .48, .05),
                opex=[15] * 7, other=[0] * 7, capex=[0, 0, 212, 213, 212, 850, 850],
                expl=[0] * 7, abex=[0, 0, 25, 25, 25, 100, 100], lease=[0] * 7, shield=[0] * 7,
                tax=.78, nor=True, R_exit_2p=414 - 42 - 42 - 41.4 - 39.4, R_exit_2c=101 * .5,
                opex_post=17.0, capex_post=10.0, aro_after=0.22 * 2500, dda=18.0),
    # BlueNord (DUC 36.8%), from 1 Jan 2027 (closing assumed 31 Dec 2026).
    "BN": dict(start=1, kboe=[0, 45, 45, 45, 45, 43, 40], mix=(.50, .50, 0),
               opex=[14] * 7, other=[0] * 7, capex=[0, 50, 50, 50, 50, 200, 200],
               expl=[0] * 7, abex=[0, 10, 10, 10, 10, 40, 40], lease=[0] * 7, shield=[0] * 7,
               tax=.64, nor=False, R_exit_2p=150 - 15.5 - 16.4 - 15.7 - 14.6, R_exit_2c=45 * .5,
               opex_post=16.0, capex_post=6.0, aro_after=0.36 * 600, dda=20.0),
}


def realised(blk, i, sc, brent=None, ttf=None):
    b = brent if brent is not None else BRENT[sc][i]
    t = ttf if ttf is not None else TTF[sc][i]
    ttf_usd = t * MWH_PER_BOE * EURUSD
    oil = b + (2 if i == 0 else 1)
    if blk == "VAR" and i <= 1:      # ~30% of gas sold fixed/year-ahead at ~$82/boe (Q4-26, Q1-27) [F]
        gas = .3 * 82 + .7 * .95 * ttf_usd
    else:
        gas = .95 * ttf_usd
    ngl = .6 * b
    return oil, gas, ngl


def run(sc, mid_from_2027=False, payout=.275, synergy=350.0, exit_r=ASSET_R, brent_mid=None,
        ttf_mid=None, q4div=450.0, r_mult=1.0, cop_capex_mult=1.0, bn_close=True,
        use_tail=True, cop_floor=True, gas_scale=None, exit_method="cont"):
    """Return dict with cash flows (USD m), per-share D_t (dated), V_T, path."""
    bm = brent_mid if brent_mid is not None else BRENT_MID[sc]
    tm = ttf_mid if ttf_mid is not None else TTF_MID[sc]
    blocks = dict(BLOCKS)
    if not bn_close:
        blocks.pop("BN")
    shares = SHARES if bn_close else SH_OLD + SH_PP
    rows = []
    # opening (30 Sep 2026)
    N = 3110.0                              # [F] NIBD 30 Sep 2026
    tax_payable = 3313.0                    # [F] Norwegian tax payable 30 Sep 2026
    acc = {2026: 0.0, 2027: 0.0, 2028: 0.0, 2029: 0.0}
    acc_q27 = []
    divs = []                               # (date, USD m total)
    decl = []                               # declared per period
    ebitdax_hist = []
    for i, (lab, yrs, end, days) in enumerate(PER):
        year = end.year
        use_mid = mid_from_2027 and i >= 1
        b = bm if use_mid else BRENT[sc][i]
        t = tm if use_mid else TTF[sc][i]
        if gas_scale is not None and i >= 1:
            t = t * gas_scale
        ebitdax = 0.0; capex = 0.0; abex = 0.0; expl = 0.0; lease = 0.0
        tax_nor_acc = 0.0; tax_dk = 0.0; prod = 0.0; rev = 0.0; dda = 0.0; blk = {}
        for name, p in blocks.items():
            if i < p["start"]:
                continue
            q = p["kboe"][i] * days / 1000.0
            oil, gas, ngl = realised(name, i, sc, b, t)
            if name == "COP" and sc == "Bear" and cop_floor and not use_mid and i in (2, 3, 4, 5):
                share = .8 if i < 5 else .8 * .25
                gas = share * max(gas, 110) + (1 - share) * gas      # floor ~$110/boe [F]
            mo, mg, mn = p["mix"]
            r = q * (mo * oil + mg * gas + mn * ngl)
            cx = p["capex"][i] * (cop_capex_mult if name == "COP" else 1)
            e = r - q * p["opex"][i] - p["other"][i]
            prod += q; rev += r; ebitdax += e
            capex += cx; abex += p["abex"][i]; expl += p["expl"][i]; lease += p["lease"][i]
            dda += q * p["dda"]
            base = e - cx - p["abex"][i] - p["expl"][i]
            blk[name] = dict(q=q, rev=r, ebitdax=e, pretax_cf=base, posttax_cf=(1 - p["tax"]) * base)
            if p["nor"]:
                tax_nor_acc += p["tax"] * base - p["shield"][i]
            else:
                tax_dk += p["tax"] * base
        # interest (net, cash) on average net debt; carry on gross bonds
        rN = .055 + (.01 if (sc == "Bear" and year >= 2028) else 0)
        interest = (rN * max(N, 0) + .02 * 7900) * yrs * r_mult
        hybrid = 105.0 * yrs
        tax_nor_acc -= .22 * interest
        acc[year] += tax_nor_acc
        # Norwegian tax paid
        if lab == "Q4-26":
            paid = 1700.0                                   # [F] company Q4-26 cash tax estimate
            tax_payable = tax_payable + tax_nor_acc - paid
            pay26 = tax_payable
        elif lab == "Q1-27":
            paid = pay26 / 3
        elif lab == "Q2-27":
            paid = pay26 * 2 / 3
        elif lab in ("Q3-27", "Q4-27"):
            paid = None                                     # set after 2027 accrual is known
        elif lab == "2028":
            paid = .5 * acc[2027] + .5 * acc[2028]
        else:
            paid = .5 * acc[2028] + .5 * acc[2029]
        cffo_pre = ebitdax - interest - hybrid - tax_dk
        rows.append(dict(lab=lab, end=end, yrs=yrs, prod=prod, rev=rev, ebitdax=ebitdax,
                         capex=capex, abex=abex, expl=expl, lease=lease, interest=interest,
                         hybrid=hybrid, tax_dk=tax_dk, tax_nor_paid=paid, tax_acc=tax_nor_acc,
                         cffo_pre=cffo_pre, brent=b, ttf=t, dda=dda, blk=blk))
    # 2027 Norwegian tax: Q3 1/6, Q4 2/6 of the 2027 accrual
    rows[3]["tax_nor_paid"] = acc[2027] / 6
    rows[4]["tax_nor_paid"] = acc[2027] * 2 / 6
    # second pass: net debt, dividends
    N = 3110.0
    out_div = []
    pending = q4div                                      # Q4-26 dividend, paid 25 Feb 2027
    pay_dates = {"Q4-26": D(2027, 2, 25), "Q1-27": D(2027, 5, 25), "Q2-27": D(2027, 8, 25),
                 "Q3-27": D(2027, 11, 25), "Q4-27": D(2028, 2, 25)}
    ltm = []
    for i, r in enumerate(rows):
        lab = r["lab"]
        tax_paid = r["tax_nor_paid"] + r["tax_dk"]
        cffo = r["ebitdax"] - r["interest"] - r["hybrid"] - tax_paid
        mfcf = cffo - r["capex"] - r["abex"] - r["expl"] - r["lease"]
        extra = 0.0
        if lab == "Q4-26":
            extra += 364.0                                 # Q3-26 dividend paid 25 Nov to VAR holders [B]
            extra -= 300.0                                 # Goliat/Fenja sale proceeds [A] ("up to $350m")
            extra -= SH_PP * 42 / USDNOK * .985            # placement, net of ~1.5% fees [A]
            if bn_close:
                extra += 1000.0 + 235.0                    # BlueNord NIBD assumed [A] + cash consideration [F]
        if lab == "Q1-27":
            extra += 2500.0                                # COP cash at completion [F]
        if lab == "Q2-27":
            extra += 1400.0                                # COP 2026 tax liability paid H1-27 [F]
        # dividends paid in period
        paid_div = 0.0
        if lab == "Q1-27":
            paid_div += pending; out_div.append((D(2027, 2, 25), pending))
        if lab in ("Q2-27", "Q3-27", "Q4-27"):
            prev = rows[i - 1]["decl"]
            paid_div += prev; out_div.append((pay_dates[rows[i - 1]["lab"]], prev))
        ltm.append(r["ebitdax"] / r["yrs"])
        lev = N / (ltm[-1]) if ltm[-1] > 0 else 9
        po = payout * (.5 if lev > 1.3 else 1.0)
        if lab == "2028":
            q4 = rows[i - 1]["decl"]
            dec = po * cffo
            paid_div += q4 + .75 * dec
            out_div.append((D(2028, 2, 25), q4))
            for m in (5, 8, 11):
                out_div.append((D(2028, m, 25), dec / 4))
        if lab == "2029":
            q4 = rows[i - 1]["decl"] / 4
            dec = po * cffo
            paid_div += q4 + .75 * dec
            out_div.append((D(2029, 2, 25), q4))
            for m in (5, 8, 11):
                out_div.append((D(2029, m, 25), dec / 4))
        if lab in ("Q1-27", "Q2-27", "Q3-27", "Q4-27"):
            dec = po * cffo
        if lab == "Q4-26":
            dec = q4div
        r["decl"] = dec
        r["cffo"] = cffo; r["mfcf"] = mfcf; r["div_paid"] = paid_div; r["extra"] = extra
        N = N - mfcf + paid_div + extra
        r["N"] = N
        r["lev"] = N / (r["ebitdax"] / r["yrs"]) if r["ebitdax"] > 0 else 99
    # exit
    exit_tax = .5 * acc[2029]
    nav_blocks = {}
    for name, p in blocks.items():
        nav_blocks[name] = block_nav(name, p, bm, tm, exit_r, sc, use_tail and not mid_from_2027,
                                     exit_method)
    hybrid_notional = 1500 * EURUSD
    ev_exit = sum(nav_blocks.values()) + synergy
    eq_exit = ev_exit - N - hybrid_notional - exit_tax
    vt_raw = eq_exit / shares
    vt_usd = max(vt_raw, 0.0)          # limited liability: a share is never worth less than zero
    return dict(sc=sc, rows=rows, divs=out_div, shares=shares, N_exit=N, exit_tax=exit_tax,
                nav_blocks=nav_blocks, ev_exit=ev_exit, eq_exit=eq_exit, vt_usd=vt_usd, vt_raw=vt_raw,
                acc=acc, hybrid=hybrid_notional, bm=bm, tm=tm)


def mid_margin(name, p, bm, tm):
    oil = bm + 1
    gas = .95 * tm * MWH_PER_BOE * EURUSD
    ngl = .6 * bm
    mo, mg, mn = p["mix"]
    real = mo * oil + mg * gas + mn * ngl
    pre = real - p["opex_post"] - p["capex_post"]
    return real, pre


def block_nav(name, p, bm, tm, rr, sc, tail=True, method="cont"):
    """V_T asset value at exit, mid-cycle prices.
    cont   (Base method): continuing producer - production held at the 2029 rate, every 2029 cost line
           per boe (opex, other, dev capex, exploration, abex, leases) kept as the replacement cost,
           post-tax cash flow capitalised at the asset rate, zero growth (mid-year).
    runoff (floor): exponential decline from the 2029 rate over R = 2P + 50% 2C, run-off costs, less
           after-tax ARO."""
    q0 = p["kboe"][6] * 365 / 1000.0
    if method == "cont":
        real = mid_margin(name, p, bm, tm)[0]
        cost = (p["opex"][6] + (p["other"][6] + p["capex"][6] + p["expl"][6] + p["abex"][6]
                + p["lease"][6]) / q0)
        pre = real - cost
        cf = q0 * ((1 - p["tax"]) * pre if pre > 0 else pre)
        pv = cf / rr * (1 + rr) ** .5
        if tail:
            pv += exit_tail(name, p, sc, bm, tm, q0)
        return pv
    R = p["R_exit_2p"] + p["R_exit_2c"]
    d = q0 / R
    real, pre = mid_margin(name, p, bm, tm)
    m = (1 - p["tax"]) * pre if pre > 0 else pre
    pv = 0.0
    for t in range(1, 60):
        q = R * d * (1 - d) ** (t - 1)
        pv += q * m / (1 + rr) ** (t - .5)
    pv -= p["aro_after"]
    if tail:
        pv += exit_tail(name, p, sc, bm, tm, q0)
    return pv


def exit_tail(name, p, sc, bm, tm, q0):
    """Reversion tail (skill Step 3) where |Year-3 - mid| / mid > 10%, per commodity."""
    t = 0.0
    w = 2 / 3 / 1.08 + 1 / 3 / 1.08 ** 2
    mo, mg, mn = p["mix"]
    b3, g3 = BRENT[sc][6], TTF[sc][6]
    if abs(b3 - bm) / bm > .10:
        t += (b3 - bm) * (mo + .6 * mn) * q0 * w * (1 - p["tax"])
    if abs(g3 - tm) / tm > .10:
        t += (g3 - tm) * MWH_PER_BOE * EURUSD * .95 * mg * q0 * w * (1 - p["tax"])
    return t


def xirr(flows):
    def npv(r):
        return sum(cf / (1 + r) ** ((d - flows[0][0]).days / 365) for d, cf in flows)
    lo, hi = -0.95, 3.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def per_share_flows(res, fx=None):
    """Dated per-share flows in NOK for the buyer of one share at P (spot FX unless fx given)."""
    f = []
    for d, amt in res["divs"]:
        fac = fx(d.year) if fx else 1.0
        f.append((d, amt / res["shares"] * USDNOK * fac))
    fac = fx(2029) if fx else 1.0
    f.append((EXIT, res["vt_usd"] * USDNOK * fac))
    return f


def irr_pk(res, fx=None, p=P_NOK):
    f = per_share_flows(res, fx)
    irr = xirr([(VAL, -p)] + f)
    pk = sum(cf / (1 + K) ** ((d - VAL).days / 365) for d, cf in f)
    return irr, pk, f
