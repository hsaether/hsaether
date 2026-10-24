# Oslo, Update 1 amended 18 Oct 2026 (skill 2026-10-18.1): price 16 Oct, Brent Base 2027 88, stub 75 d.
# One rule with World: energy block cash conversion c = 0.80 (retained (c - payout) x EPS goes into V_t at face value);
# F and O on P/E x EPS (retention funds their growth). Payout per block = latest declared dividend annualised / trailing EPS (bottom-up 16 Oct).
# Currency: energy on USD/NOK, half of O on I-44 (trade-weighted), F in NOK.
STUB = 75/365; T = STUB+3; FEE = 0.20; K = 0.12
NIB = (4.80, 4.79, 4.39, 3.86)
nibw = ((1+NIB[0]/100)**STUB*(1+NIB[1]/100)*(1+NIB[2]/100)*(1+NIB[3]/100))**(1/T)-1
SC = ["Bear", "Base", "Bull"]
LEV = 2101.65                                   # OSEBX 16 Oct close
PE27 = 11.84; E27 = 100/PE27; P0 = 100*LEV/2068.38   # CY27 consensus P/E at 9 Oct prices and FX; P0 = 16 Oct price (9 Oct = 100)
USD_NOW = 9.4135/9.5555; I44_NOW = 109.52/110.56     # FX since the 9 Oct consensus
w = {"E": 0.42, "F": 0.22, "O": 0.36}                 # shares of CY27 consensus earnings
PAY = {"E": 0.76, "F": 0.63, "O": 0.56}               # trailing dividend payout per block [F] (weighted 0.66 at CY27 shares)
C_E = 0.80                                            # energy cash conversion [A], as World energy
STUB_Y = 0.056                                        # stub cash yield: ~0.68 cash conversion x CY27 E/P 8.3% [A]
def irr(fl):
    lo, hi = -0.9, 1.0
    for _ in range(200):
        m = (lo+hi)/2; v = sum(c/(1+m)**t for t, c in fl); lo, hi = (m, hi) if v > 0 else (lo, m)
    return m
def blocks(b27=88, dB=0, dB_bear=0):
    Bb = [b27+dB, 77+dB, 72+dB, 70+dB]
    return {"Bear": {"E": [(x+dB_bear-30)/49 for x in (65, 60, 60, 60)], "F": [.85, .80, .88, .90], "O": [.85, .85, .93, 1.00]},
            "Base": {"E": [(x-30)/49 for x in Bb], "F": [.98, .96, .95, .93], "O": [.97, 1.02, 1.07, 1.10]},
            "Bull": {"E": [(x-30)/49 for x in Bb], "F": [1.00, 1.03, 1.05, 1.02], "O": [1.00, 1.08, 1.15, 1.19]}}
USDP = {"Bear": [1.12, 1.09, 1.09, 1.09], "Base": [1, 1, 1, 1], "Bull": [0.97]*4}   # USD/NOK relative to spot
I44P = {"Bear": [1.08, 1.06, 1.06, 1.06], "Base": [1, 1, 1, 1], "Bull": [0.98]*4}   # I-44 relative to spot (+ = weaker NOK)
PE = {"Bear": [10.5]*3, "Base": [11.7, 11.6, 11.5], "Bull": [12.0, 12.3, 12.5]}
def run(dp=0.0, b27=88, dB=0, dB_bear=0, vm=1.0, fxs=None, c_e=C_E, pay=None, struct=False):
    """dp: price change at unchanged earnings and future values; vm: all year-end values x vm (multiples +-10%);
    fxs: Base FX path override (same factor on USD/NOK and I-44), e.g. [1.033, 1.067, 1.10, 1.10]"""
    bl = blocks(b27, dB, dB_bear); pay = pay or PAY; out = {}
    if struct: bl = {s: {b: [v[3]]*4 for b, v in x.items()} for s, x in bl.items()}   # EPS at the normalised level from 2027
    for s in SC:
        up = fxs if (fxs and s == "Base") else USDP[s]; ip = fxs if (fxs and s == "Base") else I44P[s]
        fx = {"E": [USD_NOW*up[i] for i in range(4)], "F": [1]*4, "O": [0.5+0.5*I44_NOW*ip[i] for i in range(4)]}
        eb = {b: [w[b]*bl[s][b][i]*fx[b][i]*E27 for i in range(4)] for b in w}     # block EPS in index units, NOK
        eps = [sum(eb[b][i] for b in w) for i in range(4)]
        D = [sum(pay[b]*eb[b][k] for b in w) for k in range(3)]
        cum = 0.0; V = []
        for k in range(3):
            cum += (c_e-pay["E"])*eb["E"][k]
            V.append(vm*(PE[s][k]*eps[k+1]+cum))
        P = P0*(1+dp); Dst = P0*STUB_Y*STUB
        r = []; prev = P
        for k in range(3): r.append((D[k]+V[k])/prev-1); prev = V[k]
        fl = [(0, -P), (STUB, Dst)]+[(STUB+k+0.5, D[k]) for k in range(3)]+[(T, V[2])]
        out[s] = dict(irr=irr(fl), r=r, stub=Dst/P, V=V, D=D, Dst=Dst, VT=V[2], cash=cum*vm, sumD=Dst+sum(D),
                      Pk=sum(c/(1+K)**t for t, c in fl[1:]), eps=[e/E27*100 for e in eps], epsu=eps, P=P)
    return out
def er(o): E = (o["Base"]["irr"]-nibw)*100-FEE; R = (o["Base"]["r"][0]-o["Bear"]["r"][0])*100; return E, R, E/R
def solve(fn, tgt, lo=-0.6, hi=0.6):
    for _ in range(80):
        m = (lo+hi)/2
        if fn(m) > tgt: lo = m
        else: hi = m
    return m
PB0 = 2.34*LEV/2075.18; FPE0 = 11.91*LEV/2075.18     # MSCI Norway 30 Sep scaled by the OSEBX move since 30 Sep
if __name__ == "__main__":
    o = run()
    for s in SC:
        x = o[s]; P = x["P"]
        print(f"{s}: IRR {x['irr']*100:.2f} r {[round(v*100,1) for v in x['r']]} stub {x['stub']*100:.1f} EPS {[round(v,1) for v in x['eps']]} "
              f"sumD {x['sumD']/P*100:.1f} VT {x['VT']/P*100:.1f} (cash {x['cash']/P*100:.1f}) Pk {x['Pk']:.1f} MoS {x['Pk']/P-1:+.1%} kept {(x['sumD']+x['VT'])/P-1:+.1%} "
              f"payout27 {x['D'][0]/x['epsu'][0]:.3f} cash yld27 {x['D'][0]/P*100:.2f}")
        g = (x["VT"]/P)**(1/T)-1; d = x["sumD"]/T/P
        eg = (x["eps"][3]/100)**(1/T)-1; rr = (PE[s][2]/(P/E27))**(1/T)-1; cg = (x["VT"]/(PE[s][2]*x["epsu"][3]))**(1/T)-1
        print(f"   split: d {d*100:.2f} g {g*100:.2f} = EPS {eg*100:.2f} re-rating {rr*100:.2f} retained cash {cg*100:.2f}; c {(x['irr']-d-g)*100:.2f}")
    E, R, r = er(o); print(f"E {E:.2f} R {R:.1f} E/R {r:.3f} nibw {nibw*100:.2f}  P/E now on CY27 {P0/E27:.2f}  P/B now {PB0:.3f}  MSCI fwd now {FPE0:.2f}")
    st = run(struct=True); print("structural IRR:", {s: round(st[s]['irr']*100, 2) for s in SC}, " cyclical:", {s: round((o[s]['irr']-st[s]['irr'])*100, 2) for s in SC})
    print("sens Brent -10/+10 (Base, Bull):", [round(run(dB=d)['Base']['irr']*100, 2) for d in (-10, 10)])
    print("sens all values x0.9 / x1.1 (multiples +-10%):", [round(run(vm=m)['Base']['irr']*100, 2) for m in (0.9, 1.1)])
    print("sens P/E path -1/+1:", end=" ")
    sv = dict(PE)
    for d in (-1, 1):
        for s in SC: PE[s] = [x+d for x in sv[s]]
        print(round(run()['Base']['irr']*100, 2), end=" ")
    for s in SC: PE[s] = sv[s]
    print()
    print("sens NOK -10% / +10% by 2029 (Base):", [round(run(fxs=f)['Base']['irr']*100, 2) for f in ([1.033, 1.067, 1.10, 1.10], [0.967, 0.933, 0.90, 0.90])])
    print("energy c = payout (old rule, payouts per block):", round(run(c_e=PAY['E'])['Base']['irr']*100, 2), " c = 1.0:", round(run(c_e=1.0)['Base']['irr']*100, 2))
    # the 17 Oct model (66% flat payout, no energy cash credit, O foreign half on USD/NOK) is in git history
    for lab, fn, tgt in [("E/R=0.196", lambda p: er(run(dp=p))[2], 0.196), ("Base=12%", lambda p: run(dp=p)['Base']['irr'], 0.12),
                         ("Base=6.8% (HY market Base, hy-market-bbb)", lambda p: run(dp=p)['Base']['irr'], 0.068)]:
        p = solve(fn, tgt); print(f"trigger {lab}: {p*100:+.1f}% -> {LEV*(1+p):.0f}  P/B {PB0*(1+p):.2f}  fwd P/E (MSCI basis) {FPE0*(1+p):.1f}")
    for d in (-10, 10):
        p1 = solve(lambda q: er(run(dp=q, dB=d))[2], 0.196); p2 = solve(lambda q: er(run(dp=q, dB=d, dB_bear=d))[2], 0.196)
        print(f" trigger1 at Brent {d:+d}: Base+Bull only {LEV*(1+p1):.0f} ({(1+p1)/(1+solve(lambda q: er(run(dp=q))[2], 0.196))-1:+.1%}); all scenarios {LEV*(1+p2):.0f} ({(1+p2)/(1+solve(lambda q: er(run(dp=q))[2], 0.196))-1:+.1%})")
    # exit P/B and ROE: book_T = book now + stub retention + sum(EPS - cash paid)
    for s in SC:
        x = o[s]; e26 = E27/(1-0.083); B = x["P"]/PB0 + e26*STUB - x["Dst"]; roe = []
        for k in range(3): roe.append(x["epsu"][k]/B); B += x["epsu"][k]-x["D"][k]
        print(f" {s}: P/B now {PB0:.2f} ROE path {[round(v*100,1) for v in roe]} 2030 ROE {x['epsu'][3]/B*100:.1f}% exit P/B {x['VT']/B:.2f}  exit P/E {PE[s][2]}")
