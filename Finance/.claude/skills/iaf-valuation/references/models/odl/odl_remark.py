"""ODL (docs/odl-analysis.md) re-mark layer, v2.1, 13 Nov 2026.

The v2 full rig-day model (4 Nov 2026) was kept only in a scratchpad and is not in the
workspace. This script re-marks v2's published results to a new price and valuation date:
- it rebuilds each scenario's dated D_t stream from v2's published dividend tables
  (declared by quarter, paid 19 Mar / 1 Jun / 17 Sep / 25 Nov) and V_T;
- the Q3-26 dividend ($0.27, ex 12 Nov, paid 25 Nov 2026) is dropped from the buyer's stream;
- the net-debt path, V_t and V_T are unchanged (the company still pays the dividend);
- P_k re-marks exactly: P_k_new = (P_k_old - PV(0.27)) * 1.12^(days/365);
- IRR moves are computed on the rebuilt streams and added to v2's published IRR (delta method),
  so rounding in the rebuilt streams cancels;
- sensitivity rows: D scale and V_T fitted to v2's published IRR and P_k, then re-marked.
Standard library only. Run: py odl_remark.py
"""
from datetime import date

K = 0.12
OLD_VAL = date(2026, 11, 4)
OLD_P = 104.40 / 9.2934          # 11.234
NEW_VAL = date(2026, 11, 13)
NEW_P_NOK = 102.80               # Oslo close 12 Nov 2026 (ex the $0.27 since 12 Nov)
FX = 9.5743                      # Yahoo NOK=X 12 Nov 15:15-15:30 UTC bar close
NEW_P = NEW_P_NOK / FX
EXIT = date(2029, 12, 31)
Q3DIV = (date(2026, 11, 25), 0.27)


def pay_dates(y):
    return [date(y, 3, 19), date(y, 6, 1), date(y, 9, 17), date(y, 11, 25)]


def stream(q4_26, y27, y28, y29):
    """y27..y29 = (Q1, Q2, Q3) declared in that year, plus Q4 declared paid next March."""
    s = [Q3DIV, (date(2027, 3, 19), q4_26)]
    s += list(zip(pay_dates(2027)[1:], y27[:3]))
    s += [(date(2028, 3, 19), y27[3])]
    s += list(zip(pay_dates(2028)[1:], y28[:3]))
    s += [(date(2029, 3, 19), y28[3])]
    s += list(zip(pay_dates(2029)[1:], y29[:3]))
    return s  # Q4-29 is paid Mar 2030, inside V_T as lower net debt


# Declared dividends by quarter, rebuilt from v2 tables (year totals exact; split [A])
BASE = stream(0.27, (0.27, 0.316, 0.27, 0.324), (0.27, 0.306, 0.27, 0.237), (0.27, 0.20, 0.183))
BEAR = stream(0.27, (0.27, 0.32, 0.27, 0.318), (0.27, 0.272, 0.27, 0.175), (0.11, 0.05, 0.055))
BULL = stream(0.27, (0.27, 0.32, 0.27, 0.321), (0.27, 0.339, 0.27, 0.262), (0.27, 0.318, 0.27))
SC = {
    "Bear": dict(s=BEAR, vt=5.14, irr=-0.123, pk=6.13, v=(10.35, 8.52, 6.72), irr_t=(-0.109, -0.098)),
    "Base": dict(s=BASE, vt=10.42, irr=0.081, pk=10.21, v=(10.35, 10.24, 10.17), irr_t=(0.033, 0.067)),
    "Bull": dict(s=BULL, vt=15.78, irr=0.218, pk=14.15, v=(10.35, 11.86, 13.61), irr_t=(0.163, 0.205)),
}
NOK_FAC = {"Bear": {2026: 1.0, 2027: 1.12, 2028: 1.09, 2029: 1.09, 2030: 1.09},
           "Bull": {2026: 1.0, 2027: 0.97, 2028: 0.97, 2029: 0.97, 2030: 0.97}}
OLD_NOK = {"Bear": -0.092, "Bull": 0.204}


def yf(d, v0):
    return (d - v0).days / 365


def pv(flows, v0, r):
    return sum(a / (1 + r) ** yf(d, v0) for d, a in flows if d > v0)


def xirr(p, flows, v0):
    lo, hi = -0.9, 2.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(flows, v0, mid) > p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def flows_to(s, vt, end, ex_q3=False):
    f = [(d, a) for d, a in s if d <= end and not (ex_q3 and (d, a) == Q3DIV)]
    return f + [(end, vt)]


def pk_remark(pk_old):
    return (pk_old - Q3DIV[1] / (1 + K) ** yf(Q3DIV[0], OLD_VAL)) * (1 + K) ** ((NEW_VAL - OLD_VAL).days / 365)


def remark_irr(s, vt, irr_old, end=EXIT, fac=None):
    def conv(fl):
        return [(d, a * fac[d.year]) for d, a in fl] if fac else fl
    m_old = xirr(OLD_P, conv(flows_to(s, vt, end)), OLD_VAL)
    m_new = xirr(NEW_P, conv(flows_to(s, vt, end, ex_q3=True)), NEW_VAL)
    return irr_old + (m_new - m_old), m_old, m_new


def fit(s, irr_old, pk_old):
    """Scale later D_t and V_T so the stream returns v2's IRR at P_old and P_k at k."""
    best = None
    for i in range(0, 101):  # scale 0.5-1.5 (a near-k row is otherwise degenerate)
        sc = 0.5 + i * 0.01
        s2 = [Q3DIV] + [(d, a * sc) for d, a in s[1:]]
        # V_T from P_k
        rest = pv(s2, OLD_VAL, K)
        vt = (pk_old - rest) * (1 + K) ** yf(EXIT, OLD_VAL)
        irr = xirr(OLD_P, s2 + [(EXIT, vt)], OLD_VAL)
        err = abs(irr - irr_old)
        if best is None or err < best[0]:
            best = (err, sc, vt, s2)
    return best


def main():
    T_old = (EXIT - OLD_VAL).days / 365
    T = (EXIT - NEW_VAL).days / 365
    print(f"P_new ${NEW_P:.4f} (NOK {NEW_P_NOK} / {FX}); T {T:.3f} y ({(EXIT - NEW_VAL).days} d); T_old {T_old:.3f}")
    nav0 = {"Bear": 6.38 - 0.229, "Base": 10.48 - 0.229, "Bull": 14.86 - 0.229}
    res = {}
    for n, c in SC.items():
        irr, mo, mn = remark_irr(c["s"], c["vt"], c["irr"])
        pk = pk_remark(c["pk"])
        sd = sum(a for d, a in c["s"] if d > NEW_VAL and d <= EXIT and (d, a) != Q3DIV)
        d_ = sd / T / NEW_P
        g = (c["vt"] / NEW_P) ** (1 / T) - 1
        rr = (nav0[n] / NEW_P) ** (1 / T) - 1
        ng = (c["vt"] / nav0[n]) ** (1 / T) - 1
        pk_chk = pv(flows_to(c["s"], c["vt"], EXIT), OLD_VAL, K)
        res[n] = (irr, pk)
        print(f"{n}: model old IRR {mo:.4f} (pub {c['irr']}), P_k chk {pk_chk:.3f} (pub {c['pk']})")
        print(f"   IRR new {irr:.4f}; P_k new {pk:.3f} = NOK {pk * FX:.1f}; MoS {pk / NEW_P - 1:+.3f}")
        print(f"   SumD {sd:.3f}; SumD+VT {sd + c['vt']:.2f} (NOK {(sd + c['vt']) * FX:.1f}) vs P {NEW_P:.3f}: {(sd + c['vt']) / NEW_P - 1:+.3f}")
        print(f"   d {d_:.4f} g {g:.4f} c {irr - d_ - g:+.4f}; rerating {rr:.4f} NAVg {ng:.4f} P/NAV0 {NEW_P / nav0[n]:.2f} NAV0 {nav0[n]:.2f}")
        # path IRR to 2027, 2028
        for j, (yr, old) in enumerate(zip((2027, 2028), c["irr_t"])):
            end = date(yr, 12, 31)
            ir, _, _ = remark_irr(c["s"], c["v"][j + 1], old, end=end)
            print(f"   IRR to {yr}: {ir:.4f} (old {old})")
        print(f"   stub r_t {(c['v'][0] - NEW_P) / NEW_P:+.4f}")
        if n in NOK_FAC:
            fac = NOK_FAC[n]
            ir, mo2, _ = remark_irr(c["s"], c["vt"], OLD_NOK[n], fac=fac)
            print(f"   NOK path IRR new {ir:.4f} (model old {mo2:.4f}, pub {OLD_NOK[n]})")
    b, bb, bu = res["Base"][1], res["Bear"][1], res["Bull"][1]
    print(f"Bull share priced {(NEW_P - b) / (bu - b):.3f}")
    print(f"Rule3: Base {NEW_P / 0.84:.1f}x vs {res['Base'][0] / 0.0144:.1f}x; Bear {NEW_P / 0.41:.1f}x; Bull {NEW_P / 1.30:.1f}x vs {res['Bull'][0] / 0.0144:.1f}x")
    print(f"E = {res['Base'][0] - 0.0438:.4f}; E/R NOK {(res['Base'][0] - 0.0438) / 0.054:.2f}; spot {(res['Base'][0] - 0.0438) / 0.166:.2f}")

    # Driver breakdown, window-only step: scenario D_t and exit net debt, Base exit marks
    for n, vt in (("Bear", 10.42 - (1.77 - 1.39)), ("Bull", 10.42 + (1.39 - 1.06))):
        ir = xirr(NEW_P, flows_to(SC[n]["s"], vt, EXIT, ex_q3=True), NEW_VAL)
        print(f"window-only {n}: V_T {vt:.2f} -> IRR {ir:.4f}")
    # Sensitivity rows: (label, scenario shape, irr_old, pk_old)
    rows = [
        ("U 1.20", "Base", 0.009, 8.52), ("U 1.25", "Base", 0.061, 9.73), ("U 1.35", "Base", 0.153, 12.15),
        ("cost +10% window", "Base", 0.062, 9.73), ("cost -10% window", "Base", 0.099, 10.69),
        ("cost +10% all", "Base", 0.016, 8.69), ("cost -10% all", "Base", 0.138, 11.74),
        ("v1 cost + U1.25", "Base", 0.058, 9.66),
        ("mc 350", "Base", -0.011, 8.13), ("mc 375", "Base", 0.037, 9.17),
        ("mc 425", "Base", 0.121, 11.25), ("mc 450", "Base", 0.155, 12.22),
        ("convention", "Base", -0.119, 6.22), ("conv Bear", "Bear", -0.438, 3.04), ("conv Bull", "Bull", 0.041, 9.27),
        ("Oslo redisc Base", "Base", 0.061, 9.74), ("Oslo redisc Bear", "Bear", -0.126, 6.07),
        ("Oslo redisc Bull", "Bull", 0.190, 13.27),
        ("no tail Base", "Base", 0.071, 9.98), ("no tail Bull", "Bull", 0.209, 13.87),
        ("firm only Base", "Base", 0.074, 10.04), ("firm only Bear", "Bear", -0.130, 6.01),
        ("firm only Bull", "Bull", 0.212, 13.98),
        ("payout 100%", "Base", 0.081, 10.24), ("weighted ref", "Base", 0.079, 10.18),
    ]
    for lab, shp, io, po in rows:
        err, sc, vt, s2 = fit(SC[shp]["s"], io, po)
        ir, _, _ = remark_irr(s2, vt, io)
        pk = pk_remark(po)
        print(f"{lab:18s} fit err {err * 100:.2f}pp scale {sc:.2f} VT {vt:.2f} -> IRR {ir * 100:.1f}% P_k {pk:.2f} MoS {pk / NEW_P - 1:+.1%}")
    # structural runs: d_s = d - dd, g_s = g - dg on v2's P and T
    for n, irr_s, dd, dg, d_old, g_old in (("Bear", -0.144, 0.008, 0.011, 0.082, -0.219),
                                           ("Base", 0.043, 0.012, 0.026, 0.097, -0.024),
                                           ("Bull", 0.193, 0.006, 0.021, 0.105, 0.114)):
        sd_s = (d_old - dd) * T_old * OLD_P
        vt_s = OLD_P * (1 + g_old - dg) ** T_old
        s = SC[n]["s"]
        later = sum(a for d, a in s[1:] if d <= EXIT)
        s2 = [Q3DIV] + [(d, a * (sd_s - 0.27) / later) for d, a in s[1:]]
        ir, mo, mn = remark_irr(s2, vt_s, irr_s)
        print(f"structural {n}: model old {mo:.4f} (pub {irr_s}) -> new {ir:.4f}; cyclical {res[n][0] - ir:+.4f}")


if __name__ == "__main__":
    main()
