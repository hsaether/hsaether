"""DOF IAF engine (rebuilt 12 Nov 2026). Standard library only. $m unless stated.
Periods: Q4-26 (stub), Q1-27..Q4-27, 2028, 2029. Exit 31 Dec 2029.
"""
import datetime as dt, copy, json, sys

SH = 246.278655  # m shares
D = dt.date

def yf(d0, d1):
    return (d1 - d0).days / 365.0

def xnpv(r, cfs, d0):
    return sum(cf / (1 + r) ** yf(d0, d) for d, cf in cfs)

def xirr(cfs, d0, lo=-0.9, hi=2.0):
    f = lambda r: xnpv(r, cfs, d0)
    for _ in range(200):
        m = (lo + hi) / 2
        if f(m) > 0: lo = m
        else: hi = m
    return (lo + hi) / 2

PER = ["Q4-26", "Q1-27", "Q2-27", "Q3-27", "Q4-27", "2028", "2029"]
YRS = {"Q4-26": 0.25, "Q1-27": 0.25, "Q2-27": 0.25, "Q3-27": 0.25, "Q4-27": 0.25, "2028": 1.0, "2029": 1.0}
# payment dates of dividends DECLARED for a period
PAYDATE = {
    "Q3-26": D(2026, 11, 30), "Q4-26": D(2027, 3, 5), "Q1-27": D(2027, 6, 5), "Q2-27": D(2027, 9, 5),
    "Q3-27": D(2027, 11, 30), "Q4-27": D(2028, 3, 5),
}
EXIT = D(2029, 12, 31)


def run(inp, scen, structural=False, overrides=None):
    """inp: full input dict; scen: 'Bear'|'Base'|'Bull'. Returns result dict."""
    I = copy.deepcopy(inp)
    if overrides:
        for k, v in overrides.items():
            I[k] = v
    s = scen
    fx = I["fx"]
    tax = I["tax"]
    # ---------- EBITDA by period ----------
    eb = dict(I["ebitda"][s])  # period -> value (Q4-26 incl.)
    if structural:
        for p in PER[1:]:
            eb[p] = eb[p] - I["struct_delta"][s][p]
    # ---------- flows ----------
    nibd = I["nibd0"]; cash = I["cash0"]
    rows = {}
    declared = {}
    paid = {}
    # dividend declared for Q3-26 (already declared, paid in Q4-26) and Q4-26 (stub rule)
    declared["Q3-26"] = I["div_q3_26"]
    declared["Q4-26"] = I["div_q4_26"]
    lev_cap = I["lev_cap"]
    for p in PER:
        y = YRS[p]
        lease = I["lease"][p]; maint = I["maint"][p]; amort = I["amort"][p]
        gcap, gdebt = I["growth"][p]
        sale = I["sale"].get(p, 0.0)
        # dividends paid in period
        if p == "Q4-26": dpaid = declared["Q3-26"]
        elif p in ("Q1-27", "Q2-27", "Q3-27", "Q4-27"):
            prev = PER[PER.index(p) - 1]
            dpaid = declared[prev]
        else:
            dpaid = None  # annual: computed after declared
        # interest: average of start/end, iterate
        def flows(div_paid, intr):
            mf = eb[p] - tax * eb[p] - intr - lease - maint + I.get("other", {}).get(p, 0.0)
            n_end = nibd - mf + gcap + div_paid - sale
            c_end = cash + mf - gcap + gdebt - amort - div_paid + (sale - I.get('sale_repay', {}).get(p, sale))
            return mf, n_end, c_end
        def interest(n_s, c_s, n_e, c_e):
            if I["int_mode"] == "start" and y < 1:
                g, c = n_s + c_s, c_s
            else:
                g, c = (n_s + c_s + n_e + c_e) / 2, (c_s + c_e) / 2
            return (I["r_debt"] * g - I["r_cash"] * c) * y
        if p in ("2028", "2029"):
            prevq = "Q4-27" if p == "2028" else "2028"
            carry = declared[prevq] if p == "2028" else declared["2028"] * 0.25
            # uncapped declared
            intr = interest(nibd, cash, nibd, cash)
            for _ in range(30):
                mf, _, _ = flows(0, intr)
                dec = I["payout"] * (mf - (gcap - gdebt))
                dec = max(dec, 0.0)
                dp = carry + 0.75 * dec
                mf, n_end, c_end = flows(dp, intr)
                # leverage cap
                if n_end > lev_cap * eb[p]:
                    excess = n_end - lev_cap * eb[p]
                    dec = max(dec - excess / 0.75, 0.0)
                    dp = carry + 0.75 * dec
                    mf, n_end, c_end = flows(dp, intr)
                intr = interest(nibd, cash, n_end, c_end)
            declared[p] = dec
            dpaid = dp
        else:
            intr = interest(nibd, cash, nibd, cash)
            for _ in range(30):
                mf, n_end, c_end = flows(dpaid, intr)
                intr = interest(nibd, cash, n_end, c_end)
            if p != "Q4-26":
                dec = max(I["payout"] * (mf - (gcap - gdebt)), 0.0)
                declared[p] = dec
        paid[p] = dpaid
        rows[p] = dict(ebitda=eb[p], tax=tax * eb[p], interest=intr, lease=lease, maint=maint, mfcf=mf,
                       amort=amort, fcf_ads=mf - amort, gcap=gcap, gdebt=gdebt, sale=sale, div_paid=dpaid,
                       div_decl=declared.get(p, None), nibd=n_end, cash=c_end)
        nibd, cash = n_end, c_end
    # 2027 leverage cap check (annual): reduce Q4-27 declared if needed (simple)
    eb27 = sum(eb[p] for p in ["Q1-27", "Q2-27", "Q3-27", "Q4-27"])
    # ---------- dividend cash flows to shareholders (per share NOK) ----------
    divs = [(PAYDATE["Q3-26"], declared["Q3-26"])]
    divs.append((PAYDATE["Q4-26"], declared["Q4-26"]))
    for q in ["Q1-27", "Q2-27", "Q3-27", "Q4-27"]:
        divs.append((PAYDATE[q], declared[q]))
    for yname, yr in (("2028", 2028), ("2029", 2029)):
        dq = declared[yname] / 4
        divs.append((D(yr, 6, 5), dq)); divs.append((D(yr, 9, 5), dq)); divs.append((D(yr, 11, 30), dq))
        if yr == 2028:
            divs.append((D(2029, 3, 5), dq))
        # Q4-29 paid Mar 2030: after exit, stays in NIBD
    divs = [(d, v) for d, v in divs if I["val_date"] < d <= EXIT]
    # ---------- exit assets ----------
    ex = dict(I["exit"][s])
    if structural:
        ex["tail"] = 0.0
        ex["signed"] = I["signed_struct"][s]
    assets = sum(ex.values())
    VT = assets - nibd
    # FX path
    fxp = I.get("fxpath", {}).get(s) if I.get("use_fxpath") else None
    def nok(v, d):
        f = fx
        if fxp:
            f = fx * fxp.get(d.year, 1.0)
        return v * f / SH
    cfs = [(d, nok(v, d)) for d, v in divs]
    vt_nok = VT * (fx * (fxp.get(2029, 1.0) if fxp else 1.0)) / SH
    P = I["P"]
    all_cfs = [(I["val_date"], -P)] + cfs + [(EXIT, vt_nok)]
    irr = xirr(all_cfs, I["val_date"])
    k = I["k"]
    Pk = sum(v / (1 + k) ** yf(I["val_date"], d) for d, v in cfs) + vt_nok / (1 + k) ** yf(I["val_date"], EXIT)
    T = yf(I["val_date"], EXIT)
    sumD = sum(v for _, v in cfs)
    return dict(rows=rows, declared=declared, divs=divs, cfs=cfs, exit=ex, assets=assets, VT=VT, VT_nok=vt_nok,
                nibd_exit=nibd, cash_exit=cash, irr=irr, Pk=Pk, T=T, sumD=sumD, P=P, eb27=eb27)


def nokps(x, fx):
    return x * fx / SH
