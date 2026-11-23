"""TSMC (TSM ADS) IAF model, v1.3 (20 Nov 2026): rebuilt from docs/tsm-analysis.md v1.2 (11 Nov) inputs as a cash-flow script.

v1.2 values per ADS (USD at USD/TWD 32.789): D_t 2027-29 (quarterly NT$ ladder, ADS paid ~1 week after Taipei: 14 Jan, 15 Apr,
15 Jul, 15 Oct), V_T = exit P/E x 2030 core EPS + net cash at exit (Bear 14, Base 18, Bull 21; ADR premium 10.6% held), interim V_t
(core P/E glide). No path moved since v1.2 (AI BBB H3 kept on 18 and 20 Nov), so a re-mark scales the NT$ items by the USD/TWD
change and re-solves IRR and P_k at the new price and date.
Run: py v13.py [price] [YYYY-MM-DD] [USD/TWD]   (v1.2 check: py v13.py 396.48 2026-11-10 32.789)
"""
import sys
from datetime import date

K = 0.12
FX0 = 32.789
EXIT = date(2029, 12, 31)
QD = [(1, 14), (4, 15), (7, 15), (10, 15)]
# quarterly NT$ dividends per share paid in the year (v1.2 ladders); per ADS USD = 5 x NT$ / FX
LAD = {'Bear': [[7, 9, 9, 9], [9, 9.5, 9.5, 10], [10, 10.5, 10.5, 11]],
       'Base': [[7, 9, 9, 10], [10, 11, 11, 12], [12, 13, 13, 14]],
       'Bull': [[7, 9, 9, 10.5], [10.5, 12, 12, 13.5], [13.5, 15, 15, 16.5]]}   # 35.5 / 48 / 60 (v1.2 per-ADS 5.41 / 7.32 / 9.15)
VT = {'Bear': 250.9, 'Base': 504.4, 'Bull': 698.9}                      # v1.2, USD at 32.789
VINT = {'Bear': [218.2, 233.9], 'Base': [436.8, 472.0], 'Bull': [477.2, 585.1]}   # v1.2 interim V_t end-2027 / 2028
EPS = {'Bear': [17.81, 14.76, 15.70, 16.64], 'Base': [22.26, 24.14, 25.78, 27.18], 'Bull': [23.43, 26.95, 30.00, 32.81]}
CORE30 = {'Bear': 15.15, 'Base': 25.31, 'Bull': 31.01}; NC30 = {'Bear': 38.76, 'Base': 48.86, 'Bull': 47.78}
NC26 = 19.02; STUB_CASH = 1.40/51; CY27 = 23.43; PE_EXIT = {"Bear": 14, "Base": 18, "Bull": 21}   # STUB_CASH: v1.2 stub FCF per ADS per day (10 Nov-31 Dec: 1.40)


def yf(d0, d): return (d - d0).days / 365.25


def irr(cfs):
    lo, hi = -0.9, 2.0
    for _ in range(200):
        m = (lo + hi) / 2; v = sum(c / (1 + m) ** t for t, c in cfs)
        lo, hi = (m, hi) if v > 0 else (lo, m)
    return m


def build(n, P, d0, fx=FX0, vt_x=1.0, dshift=0.0):
    f = FX0 / fx
    cfs = [(0, -P)]
    for i, y in enumerate((2027, 2028, 2029)):
        for (m, dd), nt in zip(QD, LAD[n][i]):
            cfs.append((yf(d0, date(y, m, dd)), 5 * nt / FX0 * f))
    T = yf(d0, EXIT); vt = (VT[n] * vt_x + dshift) * f
    cfs.append((T, vt))
    D = [sum(5 * x / FX0 * f for x in LAD[n][i]) for i in range(3)]
    r = irr(cfs); pk = sum(c / (1 + K) ** t for t, c in cfs[1:])
    return dict(irr=r, pk=pk, VT=vt, D=D, sumD=sum(D), cap=(sum(D) + vt) / P - 1, T=T, cfs=cfs, f=f)


def solve(fn, tgt, lo, hi):
    """bisection on fn(x) = tgt, either direction"""
    up = fn(hi) > fn(lo)
    for _ in range(100):
        m = (lo + hi) / 2
        if (fn(m) > tgt) == up: hi = m
        else: lo = m
    return m


if __name__ == '__main__':
    P = float(sys.argv[1]) if len(sys.argv) > 1 else 318.71
    d0 = date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else date(2026, 11, 20)
    fx = float(sys.argv[3]) if len(sys.argv) > 3 else 32.958
    pct = lambda x: f"{x*100:.1f}%"
    print(f"P {P} date {d0} USD/TWD {fx} T {yf(d0, EXIT):.3f}")
    R = {}
    for n in ('Bear', 'Base', 'Bull'):
        r = build(n, P, d0, fx); R[n] = r
        print(f"{n}: IRR {pct(r['irr'])} P_k {r['pk']:.1f} MoS {r['pk']/P-1:+.1%} V_T {r['VT']:.1f} D {[round(x,2) for x in r['D']]} sumD {r['sumD']:.1f} cap {r['cap']:+.1%}")
    pk = R['Base']['pk']
    print(f"Triggers: clears <= {pk/1.02:.1f}; P_k {pk:.1f}; fails > {pk/0.98:.1f}")
    # year-end path: V_t interim (v1.2 values x f) with end-2026 mark = price flat + stub cash (no stub dividend)
    for n in R:
        f = R[n]['f']; V = [P + STUB_CASH * (date(2026, 12, 31) - d0).days * f] + [v * f for v in VINT[n]] + [R[n]['VT']]
        rt = [(R[n]['D'][i] + V[i + 1]) / V[i] - 1 for i in range(3)]
        print(f"  {n} V_t {[round(v,1) for v in V]} r_t {[pct(x) for x in rt]}")
    # NOK (Equity BBB path: Bear +12% 2027, +9% after; Bull -3%)
    F = {'Bear': [1.12, 1.09, 1.09], 'Base': [1, 1, 1], 'Bull': [.97, .97, .97]}
    for n, r in R.items():
        cf = [r['cfs'][0]] + [(t, c * F[n][i // 4]) for i, (t, c) in enumerate(r['cfs'][1:-1])] + [(r['cfs'][-1][0], r['cfs'][-1][1] * F[n][2])]
        print(f"  {n} NOK IRR {pct(irr(cf))}")
    # price-implied: multiplier m on Base 2028-30 (scales core EPS 2030 in V_T; interim and D held) [A]
    f = R['Base']['f']
    def base_m(m):
        dv = (m - 1) * PE_EXIT['Base'] * CORE30['Base']
        return build('Base', P, d0, fx, dshift=dv)['irr']
    print(f"Price implies k at m = {solve(base_m, K, 0.3, 2.0):.2f} x Base 2030 core EPS; 0% at m = {solve(base_m, 0.0, 0.1, 2.0):.2f}")
    def pe_x(pe): return build('Base', P, d0, fx, dshift=(pe - 18) * CORE30['Base'])['irr']
    print(f"Exit P/E for k: {solve(pe_x, K, 5, 40):.1f}")
    for lab, pe in (("exit 16", 16), ("exit 16.7 (5-yr mean)", 16.7), ("exit 20", 20)):
        r = build('Base', P, d0, fx, dshift=(pe - 18) * CORE30['Base']); print(f"  sens {lab}: {pct(r['irr'])} P_k {r['pk']:.1f} ({r['pk']/P-1:+.1%})")
    for lab, x in (("2030 EPS x0.9", 0.9), ("2030 EPS x1.1", 1.1)):
        r = build('Base', P, d0, fx, dshift=(x - 1) * 18 * CORE30['Base']); print(f"  sens {lab}: {pct(r['irr'])} P_k {r['pk']:.1f} ({r['pk']/P-1:+.1%})")
    # E / R vs NIBOR window
    nib = 4.72; m26 = P + STUB_CASH * (date(2026, 12, 31) - d0).days * f
    b27 = (R['Base']['D'][0] + VINT['Base'][0] * f) / m26 - 1
    bear27n = ((R['Bear']['D'][0] + VINT['Bear'][0] * f) * 1.12) / m26 - 1
    E = R['Base']['irr'] * 100 - nib; Rr = (b27 - bear27n) * 100
    print(f"E/R: E {E:.2f} R {Rr:.1f} (Base 2027 {b27*100:.1f}%, Bear 2027 NOK {bear27n*100:.1f}%) E/R {E/Rr:.3f}")
    def er_p(p):
        rb = build('Base', p, d0, fx); mm = p + STUB_CASH * (date(2026, 12, 31) - d0).days * f
        b = (rb['D'][0] + VINT['Base'][0] * f) / mm - 1; be = ((R['Bear']['D'][0] + VINT['Bear'][0] * f) * 1.12) / mm - 1
        return (rb['irr'] * 100 - nib) / ((b - be) * 100)
    print(f"E/R = 0.254 at ${solve(er_p, 0.254, 150, 600):.1f}")
    print(f"Base = HY market 7.5% at ${solve(lambda p: build('Base', p, d0, fx)['irr'], 0.075, 150, 800):.1f}")
    print(f"Core P/E on Base 2030: {(P - NC26 * f) / (CORE30['Base'] * f):.1f}; P/E CY27 consensus {P/(CY27*f):.1f}")
