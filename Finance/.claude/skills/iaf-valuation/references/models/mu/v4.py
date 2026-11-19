"""Micron (MU) IAF model, v4 (19 Nov 2026). Rebuilds the v3 document build (5 Nov) as a script.

EPS = AI BBB H2 layer path x CY27 consensus ($191.8, calendarised). Net income = EPS x 1.149bn
diluted shares (held flat; buybacks are D_t). FCF after growth = NI - working capital (15% of the
revenue change) - (capex - D&A). Payout: net cash ex customer deposits held at $60bn, the excess
at end-2026 paid in 2027, then 100% of FCF. V_T = exit P/E x 2030 EPS + net cash per share.
D_t paid in four equal parts at mid-quarter (15 Feb / May / Aug / Nov). Stub: no D_t (cash kept).
Run: py v4.py [price] [YYYY-MM-DD]  (v3 check: py v4.py 656.39 2026-11-05 v3)
"""
import sys
from datetime import date

SH = 1.149            # bn diluted shares
CY27 = 191.8          # calendarised CY27 consensus EPS
K = 0.12
REV26 = 195.3         # CY26 revenue $bn (working-capital base, implied by v3)
NC26 = 100.8          # net cash ex deposits at 31 Dec 2026, $bn
NC_HOLD = 60.0
EXIT = date(2029, 12, 31)

SCEN = {
    # layer EPS 2027-29, 2030; revenue; capex; D&A; exit P/E
    'Bear': dict(eps=[.60, .30, .25], e30=.25, rev=[200, 140, 130], capex=[52, 40, 35], da=[12, 15, 17], pe=8),
    'Base': dict(eps=[.90, .50, .32], e30=.28, rev=[270, 210, 185], capex=[58, 65, 60], da=[12, 16, 20], pe=10),
    'Bull': dict(eps=[1.00, .80, .55], e30=.45, rev=[293, 260, 230], capex=[62, 75, 80], da=[12, 17, 22], pe=11),
}
V3_BASE = dict(SCEN['Base'], eps=[.90, .60, .40], e30=.35, rev=[270, 230, 200])


def yf(d0, d):
    return (d - d0).days / 365.25


def irr(cfs):
    lo, hi = -0.9, 3.0
    for _ in range(200):
        mid = (lo + hi) / 2
        v = sum(c / (1 + mid) ** t for t, c in cfs)
        lo, hi = (mid, hi) if v > 0 else (lo, mid)
    return mid


def build(s, P, d0, **ov):
    s = dict(s, **ov)
    eps = [x * CY27 for x in s['eps']]; e30 = s['e30'] * CY27
    ni = [e * SH for e in eps]
    rev = [REV26] + s['rev']
    fcf = [ni[i] - 0.15 * (rev[i + 1] - rev[i]) - (s['capex'][i] - s['da'][i]) for i in range(3)]
    D = [fcf[0] + (NC26 - NC_HOLD)] + fcf[1:]
    if s.get('retain'):
        D = [0, 0, 0]
    nc_exit = NC26 + sum(fcf) - sum(D)
    Dps = [x / SH for x in D]
    VT = s['pe'] * e30 * s.get('e30x', 1) + nc_exit / SH
    cfs = [(0, -P)]
    for i, y in enumerate([2027, 2028, 2029]):
        for m in (2, 5, 8, 11):
            cfs.append((yf(d0, date(y, m, 15)), Dps[i] / 4))
    T = yf(d0, EXIT)
    cfs.append((T, VT))
    r = irr(cfs)
    pk = sum(c / (1 + K) ** t for t, c in cfs[1:])
    return dict(irr=r, pk=pk, VT=VT, D=Dps, sumD=sum(Dps), eps=eps, e30=e30, fcf=[f / SH for f in fcf],
                ni=ni, nc_exit=nc_exit / SH, T=T, cap=(sum(Dps) + VT) / P - 1, cfs=cfs)


def solve(f, target, lo, hi):
    flo = f(lo) - target
    for _ in range(100):
        mid = (lo + hi) / 2
        fm = f(mid) - target
        if fm * flo > 0:
            lo, flo = mid, fm
        else:
            hi = mid
    return mid


if __name__ == '__main__':
    P = float(sys.argv[1]) if len(sys.argv) > 1 else 705.27
    d0 = date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else date(2026, 11, 18)
    S = dict(SCEN)
    if len(sys.argv) > 3 and sys.argv[3] == 'v3':
        S['Base'] = V3_BASE
    pct = lambda x: f"{x*100:.1f}%"
    print(f"P {P}  date {d0}  T {yf(d0, EXIT):.3f}")
    R = {}
    for n, s in S.items():
        r = build(s, P, d0); R[n] = r
        print(f"{n}: IRR {pct(r['irr'])} P_k {r['pk']:.1f} MoS {r['pk']/P-1:+.1%} V_T {r['VT']:.1f} sumD {r['sumD']:.1f} "
              f"cap {r['cap']:+.1%} | EPS {[round(e,1) for e in r['eps']]} 2030 {r['e30']:.1f} | FCF/sh {[round(f,1) for f in r['fcf']]} "
              f"| D/sh {[round(x,1) for x in r['D']]} | cumFCF {sum(r['fcf']):.1f}")
    B = S['Base']
    pkb = R['Base']['pk']
    print(f"Triggers: clears <= {pkb/1.02:.1f}; P_k {pkb:.1f}; fails >= {pkb/0.98:.1f}")
    # price-implied multiplier on Base 2028-30
    f = lambda m: build(dict(B, eps=[B['eps'][0], B['eps'][1]*m, B['eps'][2]*m], e30=B['e30']*m), P, d0)['irr']
    mk = solve(f, K, 0.2, 3.0); m0 = solve(f, 0.0, 0.0, 3.0)
    print(f"Price implies k at m = {mk:.2f} x Base 2028-30 ({[round(x*mk,2) for x in B['eps'][1:]]+[round(B['e30']*mk,2)]}); 0% at m = {m0:.2f}")
    fpe = lambda pe: build(dict(B, pe=pe), P, d0)['irr']
    print(f"Exit P/E for k: {solve(fpe, K, 1, 30):.1f}; for 0%: {solve(fpe, 0.0, 0.1, 30):.1f}")
    fe = lambda x: build(dict(B, e30=x), P, d0)['irr']
    x = solve(fe, K, 0.01, 2); print(f"2030 EPS for k: {x:.3f} x CY27 = ${x*CY27:.1f}")
    print("== Sensitivities (Base IRR, P_k) ==")
    for lab, ov in [('exit 8', dict(pe=8)), ('exit 12', dict(pe=12)), ('2030 EPS x0.8', dict(e30x=0.8)), ('2030 EPS x1.2', dict(e30x=1.2)),
                    ('v3 path (.60/.40/.35)', dict(eps=[.90, .60, .40], e30=.35, rev=[270, 230, 200])),
                    ('2029 capex 45 (cut)', dict(capex=[58, 65, 45])), ('retain all cash', dict(retain=True)),
                    ('Bear 2028 depth with Base exit (.90/.30/.25/.25, P/E 10)', dict(eps=[.90, .30, .25], e30=.25, rev=[270, 140, 130])),
                    ('Micron "tight through 2028" (1.00/1.00/.60/.45)', dict(eps=[1.0, 1.0, .60], e30=.45, rev=[293, 293, 230]))]:
        r = build(B, P, d0, **ov)
        print(f"  {lab}: {pct(r['irr'])} P_k {r['pk']:.1f} ({r['pk']/P-1:+.1%})")
    # year-end r_t with interim glide (diagnostic)
    nc0 = 84.0 / SH
    for n in R:
        s = S[n]; r = R[n]
        core0 = (P - nc0) / r['eps'][0]
        pes = [core0 + (s['pe'] - core0) * i / 3 for i in (1, 2)] if n != 'Bear' else [s['pe'], s['pe']]
        nxt = r['eps'][1:] + [r['e30']]
        V = [P + (NC26 / SH - nc0)] + [pes[0] * nxt[0] + 60 / SH, pes[1] * nxt[1] + 60 / SH, r['VT']]
        rt = [(r['D'][i] + V[i + 1]) / V[i] - 1 for i in range(3)]
        print(f"  {n} V_t {[round(v,1) for v in V]} r_t {[pct(x) for x in rt]} core P/E0 {core0:.2f}")
    # E / R reference (NIBOR window 4.72)
    rb, rr = R['Base'], R['Bear']
    Vb = [P + (NC26 / SH - nc0)]
    print(f"Core P/E on CY27 consensus: {(P - nc0)/CY27:.2f}; on Base 2030 EPS {(P-nc0)/R['Base']['e30']:.1f}")
