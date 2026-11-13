"""Anthropic, PBC (ANT) - IAF model behind docs/anthropic-analysis.md, version 1.0, 13 Nov 2026.

Track A with explicit compute and capex (year-by-year build): stub Q4-26 + 2027-29, exit 31 Dec 2029,
V_T = exit P/E x normalised 2030 NOPAT + net cash at exit - commitment overhang (PV of committed
compute above the normalised need after exit). No dividends (D_t = 0). USD bn unless stated.
Facts [F]: EU retail prospectus approved by Bafin 11 Nov 2026 (printed page = PDF page - 10).
E1 frontier-lab revenue paths: docs/ai-market-bbb.md (11 Nov 2026). NOK path: docs/equity-market-bbb.md.
Everything else is an own assumption [A]. Standard library only. Run: py model.py
"""
from datetime import date

K = 0.12
VAL = date(2026, 11, 20)            # closing of the global offering: the IPO price is paid
EXIT = date(2029, 12, 31)
T = (EXIT - VAL).days / 365.0
TAX = 0.21                          # normalised tax rate in exit earnings [A]
USDNOK = 9.5610                     # EODHD 12 Nov 2026 18:25 UTC via docs/nvda-analysis.md v1.5 [C]
NOKF = {"Bear": 10.14 / 9.29, "Base": 1.0, "Bull": 9.02 / 9.29}   # Equity BBB exit-year factors

# ---- share count [F] prospectus, millions --------------------------------------------------
OUT_PRE = 11966.410             # Class A 6,630.24 + Class N 5,336.17, last practicable date (incl. PBF 846.84)
PRIMARY = 801.351354            # new Class A in the global offering
OA = 123.75                     # over-allotment (assumed exercised) [A]
PLACEMENT_USD = 26000.0         # concurrent Class N placement, $m, at the IPO price
AMZN_NOTES = 1840.444962 - 276.827518   # rollover notes left after the IPO conversion (fixed price <= IPO price)
OPTIONS, OPT_K = 1774.342693, 2.91      # options outstanding 30 Sep, weighted exercise price
RSU = 1026.660010 + 47.041287           # unvested RSUs + RSUs granted after 30 Sep
MATCH = 553.441297                      # vested matching obligation (donation matching plan, maximum)
PBF = 846.840960                        # Anthropic Public Benefit Fund (inside OUT_PRE)


def shares_fd(P):
    return (OUT_PRE + PRIMARY + OA + PLACEMENT_USD / P + AMZN_NOTES
            + OPTIONS * (1 - OPT_K / P) + RSU + MATCH)


def shares_issued(P):
    return OUT_PRE + PRIMARY + OA + PLACEMENT_USD / P


def cash_close(P):
    """Net cash at closing, $bn: as further adjusted 30 Sep (at $74) +/- $0.793bn per $1, plus over-allotment."""
    return 212.684 + 0.793 * (P - 74) + OA * P * 0.9882 / 1000


# ---- stub Q4-26, identical in all scenarios [A] ---------------------------------------------
STUB = dict(rev=21.5, compute=13.0, other=5.5, capex=3.0, interest=1.5, tax=0.2)
STUB["adj_oi"] = STUB["rev"] - STUB["compute"] - STUB["other"]
STUB["fcf"] = STUB["adj_oi"] - STUB["capex"] + STUB["interest"] - STUB["tax"] + 0.0
REV_2026 = 33.242 + STUB["rev"]

E1 = {"Bear": [155, 170, 187], "Base": [190, 275, 360], "Bull": [230, 370, 515]}   # AI BBB 11 Nov
COMMITTED = {2027: 77, 2028: 125, 2029: 147, 2030: 155, 2031: 135, 2032: 120, 2033: 100,
             2034: 45, 2035: 40}   # contractual compute schedule [A] from the $900.9bn and its timing [F]

SC = {
    "Base": dict(share=0.58, g=[0.22, 0.18, 0.15, 0.12, 0.10, 0.08], compute=[77, 115, 135],
                 other=[0.25, 0.23, 0.21], capex=[20, 20, 15], r=0.0375,
                 c_norm=0.52, o_norm=0.19, sbc_norm=0.04, pe=26, takedown=0.92, resale=0.0,
                 tail_years=2, shield=TAX, match_pa=0.005, grant=0.03, lr_growth=0.07,
                 need=[0.62, 0.60, 0.57]),
    "Bear": dict(share=0.55, g=[0.08, 0.06, 0.06, 0.06, 0.06, 0.06], compute=[75, 100, 108],
                 other=[0.26, 0.25, 0.24], capex=[15, 6, 4], r=0.030,
                 c_norm=0.58, o_norm=0.21, sbc_norm=0.05, pe=15, takedown=0.80, resale=0.5,
                 tail_years=6, shield=0.0, match_pa=0.005, grant=0.03, lr_growth=0.04,
                 need=[0.68, 0.66, 0.64]),
    "Bull": dict(share=0.62, g=[0.30, 0.25, 0.20, 0.15, 0.12, 0.10], compute=[92, 145, 172],
                 other=[0.24, 0.22, 0.20], capex=[30, 35, 30], r=0.0375,
                 c_norm=0.48, o_norm=0.18, sbc_norm=0.03, pe=30, takedown=1.0, resale=0.0,
                 tail_years=2, shield=TAX, match_pa=0.005, grant=0.03, lr_growth=0.08,
                 need=[0.60, 0.57, 0.52]),
}
CASH_TAX = [0.0, 0.05, 0.12]   # on positive pre-tax cash profit, 2027-29 (RSU deductions, NOLs) [A]


def irr(flows):
    lo, hi = -0.99, 5.0
    for _ in range(200):
        m = (lo + hi) / 2
        v = sum(c / (1 + m) ** t for t, c in flows)
        lo, hi = (m, hi) if v > 0 else (lo, m)
    return m


def build(name, P, **ov):
    s = dict(SC[name], **ov)
    rev = s.get("rev") or [e * s["share"] for e in E1[name]]
    need = s.get("need", [0.62, 0.60, 0.57])          # compute ratio needed to serve revenue [A]
    comp = [max(c, n * r) for c, n, r in zip(s["compute"], need, rev)]
    nc = cash_close(P) + STUB["fcf"]
    nc_path = [nc]
    rows = []
    capex_cum = STUB["capex"]
    for i, yr in enumerate((2027, 2028, 2029)):
        adj = rev[i] - comp[i] - s["other"][i] * rev[i]
        da = capex_cum / 5.0
        interest = s["r"] * nc
        pre = adj + interest
        tax = CASH_TAX[i] * max(0.0, pre)
        fcf = adj + da - s["capex"][i] + interest - tax
        nc += fcf
        capex_cum += s["capex"][i]
        core = (adj - s["sbc_norm"] * rev[i]) * (1 - TAX)
        rows.append(dict(yr=yr, rev=rev[i], compute=comp[i], cratio=comp[i] / rev[i], adj=adj,
                         adjm=adj / rev[i], interest=interest, tax=tax, capex=s["capex"][i], da=da,
                         fcf=fcf, nc=nc, core=core))
        nc_path.append(nc)
    # normalised exit year 2030 and the overhang after exit
    revs = [rev[2]]
    for g in s["g"]:
        revs.append(revs[-1] * (1 + g))
    rev30 = revs[1]
    ebit_m = 1 - s["c_norm"] - s["o_norm"] - s["sbc_norm"]
    nopat30 = rev30 * ebit_m * (1 - TAX)
    ev = s["pe"] * nopat30
    over = 0.0
    over_rows = []
    for j in range(s["tail_years"]):
        yr = 2030 + j
        need = s["c_norm"] * revs[j + 1]
        paid = s["takedown"] * COMMITTED.get(yr, 0)
        ex = max(0.0, paid - need) * (1 - s["resale"]) * (1 - s["shield"])
        pv = ex / 1.08 ** (j + 1)
        over += pv
        over_rows.append((yr, paid, need, ex, pv))
    eq_T = ev + nc - over
    # dilution after the IPO: new grants, further donation matching, PBF milestones (iterate on price)
    fd0 = shares_fd(P)
    sh = fd0
    vt = eq_T * 1000 / sh
    for _ in range(30):
        path = [P * (vt / P) ** ((i + 1) / 3) for i in range(3)]
        grants = sum(s["grant"] * rows[i]["rev"] * 1000 / path[i] for i in range(3))
        match = s["match_pa"] * fd0 * 3
        pbf = 0.0
        base = fd0 + grants + match
        for lvl in (1.5, 2.25, 3.375):
            if max(path) >= lvl * P:
                pbf += 0.02 * (base + pbf)
        sh = base + pbf
        vt_new = eq_T * 1000 / sh
        if abs(vt_new - vt) < 1e-6:
            break
        vt = vt_new
    vt = eq_T * 1000 / sh
    res = dict(name=name, P=P, s=s, rev=rev, rows=rows, rev30=rev30, revs=revs, ebit_m=ebit_m,
               nopat30=nopat30, ev=ev, nc_T=nc, over=over, over_rows=over_rows, eq_T=eq_T,
               fd0=fd0, sh_T=sh, grants=grants, match=match, pbf=pbf, VT=vt, nc0=cash_close(P),
               nc26=nc_path[0], nc_path=nc_path)
    res["irr"] = (vt / P) ** (1 / T) - 1
    res["pk"] = vt / (1 + K) ** T
    res["mos"] = res["pk"] / P - 1
    res["irr_nok"] = (vt * NOKF[name] / P) ** (1 / T) - 1
    res["e1share"] = [r / e for r, e in zip(rev, E1[name])]
    # interim marks (diagnostic): P/E glides from the entry-implied multiple to the exit P/E
    nop_next = [rev[i] * ebit_m * (1 - TAX) for i in (1, 2)]
    ev0 = P * fd0 / 1000 - res["nc0"]
    base_rev27 = E1["Base"][0] * SC["Base"]["share"]
    base_m = 1 - SC["Base"]["c_norm"] - SC["Base"]["o_norm"] - SC["Base"]["sbc_norm"]
    pe0 = ev0 / (base_rev27 * base_m * (1 - TAX))
    marks = []
    for i, yr in enumerate((2027, 2028)):
        t_i = (date(yr, 12, 31) - VAL).days / 365.0
        pe_t = pe0 + (s["pe"] - pe0) * t_i / T
        sh_t = fd0 + (sh - fd0) * (i + 1) / 3
        marks.append((pe_t * nop_next[i] + nc_path[i + 1] - over / 1.08 ** (2 - i)) * 1000 / sh_t)
    res["marks"] = marks
    res["pe0"] = pe0
    return res


def pk_fixed(name, target=0.0, **ov):
    """IPO price at which the Base margin of safety equals target (fixed point: cash and shares move with P)."""
    lo, hi = 10.0, 300.0
    for _ in range(100):
        m = (lo + hi) / 2
        r = build(name, m, **ov)
        lo, hi = (m, hi) if r["mos"] > target else (lo, m)
    return m


def fmt(x, d=1):
    return f"{x:,.{d}f}"


if __name__ == "__main__":
    print(f"T = {T:.3f} years; valuation {VAL}, exit {EXIT}")
    for P in (70, 74, 78):
        print(f"P={P}: FD {shares_fd(P):,.1f}m, issued {shares_issued(P):,.1f}m, cash {cash_close(P):.1f}bn,"
              f" mcap FD {P*shares_fd(P)/1000:,.0f}bn, issued {P*shares_issued(P)/1000:,.0f}bn,"
              f" EV {P*shares_fd(P)/1000-cash_close(P):,.0f}bn")
    print("stub", STUB, "2026 revenue", round(REV_2026, 2))
    for name in ("Bear", "Base", "Bull"):
        r = build(name, 74)
        print(f"\n== {name} @74: IRR {r['irr']:.1%}  NOK {r['irr_nok']:.1%}  VT {r['VT']:.2f}  Pk {r['pk']:.2f}"
              f"  MoS {r['mos']:+.1%}  E1 share {[round(x,3) for x in r['e1share']]}")
        for row in r["rows"]:
            print("  ", {k: (round(v, 2) if isinstance(v, float) else v) for k, v in row.items()})
        print(f"   rev30 {r['rev30']:.1f} EBIT {r['ebit_m']:.0%} NOPAT30 {r['nopat30']:.1f} EV {r['ev']:.0f}"
              f" ncT {r['nc_T']:.1f} overhang {r['over']:.1f} eqT {r['eq_T']:.0f}")
        print(f"   shares fd0 {r['fd0']:.0f} grants {r['grants']:.0f} match {r['match']:.0f} pbf {r['pbf']:.0f}"
              f" shT {r['sh_T']:.0f}; marks {[round(m,1) for m in r['marks']]} pe0 {r['pe0']:.1f}")
        print("   overhang rows", [tuple(round(x, 1) for x in o) for o in r["over_rows"]])
    print("\nRange:")
    for P in (70, 74, 78):
        out = []
        for name in ("Bear", "Base", "Bull"):
            r = build(name, P)
            out.append(f"{name} IRR {r['irr']:.1%} Pk {r['pk']:.1f} MoS {r['mos']:+.1%} VT {r['VT']:.1f}")
        print(P, " | ".join(out))
    print("Fixed point P_k (Base, MoS 0):", round(pk_fixed("Base"), 2), " MoS +2%:", round(pk_fixed("Base", 0.02), 2))
