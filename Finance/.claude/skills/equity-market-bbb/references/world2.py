# Equity BBB Update 2 (6 Nov 2026; skill 2026-10-24.1): World = company blocks + AI layer blocks + energy + explicit rest.
# Prices: 5 Nov 2026 close (Yahoo). Weights: URTH holdings of 4 Nov 2026 (dl2/urth_ai_nov.json) repriced to 5 Nov. World value 5 Nov = 100.
# Company blocks (own IAF analyses): Microsoft v3 (28 Oct, $531.01), Alphabet v2 re-mark (30 Oct, $279.84), NVIDIA v1.2 (5 Nov, $181.60),
#   Amazon v2 (30 Oct, $240.35), Micron v3 (5 Nov, $656.39). Interim V_t of Base and Bull re-glided to the 5 Nov price (the analyses' rule:
#   core P/E glides linearly from today's to the exit P/E; Bear at its exit P/E from end-2027); V_T, D_t and EPS are the analyses' figures.
# AI layer blocks (docs/ai-market-bbb.md, Update 6 of 1 Nov, kept 5 Nov): E rest (Meta, Oracle) on the "E rest" row; H1 (AMD, Broadcom,
#   Marvell); H3 (ASML, Applied, Lam); H4 (Arista, Vertiv, Eaton); T (8 software names). CY27 EPS calendarised (AI BBB, 1 Nov).
# Energy: URTH energy weight on the oil path ((Brent - 30)/49: the 9 Oct consensus basis, P/E from IXC scaled by price), payout as Oslo energy.
# Rest: CY27 earnings = 18 Oct rest x the URTH unit change x (1 + 0.6% S&P 500 CY27 revision, FactSet 30 Oct vs 9 Oct) [A].
# Needs idxai3.py, dl2/urth_ai_nov.json (urthparse.py) and dl2/recent_1105.json (recent.py, 5 Nov closes) in the working folder. Run: py -I world2.py
import sys, os, json, copy
sys.path.insert(0, os.getcwd())
import idxai3 as M
SC = M.SC; K = 0.12; FEE = 0.20
M.STUB = STUB = 55/365; M.T = T = STUB+3
NIB = (4.80, 4.79, 4.39, 3.86)
M.nibw = NIBW = ((1+NIB[0]/100)**STUB*(1+NIB[1]/100)*(1+NIB[2]/100)*(1+NIB[3]/100))**(1/T)-1
UA = json.load(open("dl2/urth_ai_nov.json")); RC = json.load(open("dl2/recent_1105.json"))
EU5 = 1.1235
P5 = {n: RC[n]["2026-11-05"] for n in ["MSFT", "GOOGL", "GOOG", "NVDA", "AMZN", "META", "ORCL", "AMD", "AVGO", "MRVL", "MU", "ASML", "AMAT", "LRCX",
                                        "ANET", "VRT", "ETN", "NOW", "CRM", "ADBE", "PLTR", "INTU", "SNOW", "DDOG"]}
P5["SAP"] = 215.75*EU5
MOVE = {n: P5[n]/RC[n]["2026-11-04"] for n in P5 if n != "SAP"}
MOVE["SAP"] = (215.75/214.30)*(EU5/1.1207)
R_URTH = RC["URTH"]["2026-11-05"]/RC["URTH"]["2026-11-04"]
W5 = {n: UA["w"][n]/UA["total"]*100*MOVE[n]/R_URTH for n in MOVE}
EN_V = UA["energy"]/UA["total"]*100*(RC["IXC"]["2026-11-05"]/RC["IXC"]["2026-11-04"])/R_URTH
EN_PE = 14.8*RC["IXC"]["2026-11-05"]/59.88
EPS27 = {"META": 33.93, "ORCL": 9.83, "AMD": 15.94, "AVGO": 19.47, "MRVL": 7.07, "ASML": 62.45, "AMAT": 18.55, "LRCX": 10.94, "ANET": 5.22,
         "VRT": 9.74, "ETN": 16.30, "NOW": 4.80, "CRM": 16.08, "ADBE": 27.51, "PLTR": 2.35, "SAP": 8.48*EU5, "INTU": 25.12, "SNOW": 2.96, "DDOG": 2.98}
LAY = {"E": ["META", "ORCL"], "H1": ["AMD", "AVGO", "MRVL"], "H3": ["ASML", "AMAT", "LRCX"], "H4": ["ANET", "VRT", "ETN"],
       "T": ["NOW", "CRM", "ADBE", "PLTR", "SAP", "INTU", "SNOW", "DDOG"]}
# AI BBB (1 Nov): E rest row for Meta/Oracle; E cash conversion -.20/.00/.20 (Bear -.10/.30/.50; Bull -.30/-.20/.00); others unchanged
M.AI["E"] = (dict(Bear=(.88, .88, .97, 1.05), Base=(.97, 1.07, 1.17, 1.27), Bull=(1.0, 1.13, 1.27, 1.41)), (17, 21, 23.5), .34)
M.CONV["E"] = dict(Bear=(-.10, .30, .50), Base=(-.20, .00, .20), Bull=(-.30, -.20, .00))
B_EN = 49.0
EN_PAY = 0.58          # Oslo energy payout (latest declared dividend annualised / trailing EPS, 5 Nov); cash conversion 0.80


def set_energy(b27=88, dB=0, dB_bear=0, bc=B_EN, pay=None):
    Bb = [b27+dB, 77+dB, 72+dB, 70+dB]
    M.EN = (dict(Bear=tuple((x+dB_bear-30)/bc for x in (65, 60, 60, 60)), Base=tuple((x-30)/bc for x in Bb),
                 Bull=tuple((x-30)/bc for x in Bb)), (11, 12, 13), pay or EN_PAY)


set_energy()


def reglide(V, EPS, p_now, p_an, eps27):
    dpe = (p_now-p_an)/eps27
    return (V[0]+dpe*2/3*EPS[1], V[1]+dpe*1/3*EPS[2], V[2])


CO_SRC = {
 "CM": dict(names=["MSFT"], cons=22.08, stub=0.98, p_an=531.01, e27=20.77,
            V=dict(Bear=(337.7, 368.8, 404.5), Base=(585.8, 643.2, 692.1), Bull=(681.6, 806.0, 921.4)),
            D=dict(Bear=(3.97, 4.17, 4.38), Base=(4.01, 4.37, 4.76), Bull=(4.02, 4.42, 4.86)),
            EPS=dict(Bear=(18.18, 17.84, 19.16, 20.61), Base=(20.77, 23.40, 26.11, 28.39), Bull=(22.03, 26.26, 30.37, 33.80))),
 "CG": dict(names=["GOOGL", "GOOG"], cons=14.84, stub=0.22, p_an=279.84, e27=12.66,
            V=dict(Bear=(160.1, 179.0, 202.6), Base=(306.6, 337.9, 371.1), Bull=(373.0, 439.3, 515.9)),
            D=dict(Bear=(0.88, 0.88, 0.88), Base=(0.91, 0.96, 1.01), Bull=(0.95, 1.04, 1.14)),
            EPS=dict(Bear=(10.46, 9.82, 11.00, 12.33), Base=(12.66, 14.28, 15.89, 17.44), Bull=(13.80, 16.66, 18.97, 21.39))),
 "CN": dict(names=["NVDA"], cons=15.21, stub=0.56, p_an=181.60, e27=13.99,
            V=dict(Bear=(106.7, 116.0, 126.9), Base=(220.8, 253.3, 274.1), Bull=(269.5, 339.6, 402.6)),
            D=dict(Bear=(5.12, 4.92, 4.43), Base=(6.59, 8.46, 8.81), Bull=(7.00, 9.59, 10.70)),
            EPS=dict(Bear=(10.34, 7.61, 8.06, 8.67), Base=(13.99, 14.91, 15.21, 14.75), Bull=(15.21, 17.49, 19.01, 19.77))),
 "CA": dict(names=["AMZN"], cons=10.65, stub=0.0, p_an=240.35, e27=9.69,
            V=dict(Bear=(105.9, 119.6, 141.4), Base=(267.2, 292.0, 317.3), Bull=(316.9, 371.0, 432.1)),
            D=dict(Bear=(0, 0, 0), Base=(0, 0, 0), Bull=(0, 0, 0)),
            EPS=dict(Bear=(7.54, 6.23, 7.05, 8.22), Base=(9.69, 11.28, 12.68, 14.00), Bull=(10.51, 13.07, 15.35, 17.73))),
 "CU": dict(names=["MU"], cons=191.80, stub=0.0, p_an=656.39, e27=172.6,
            V=dict(Bear=(512.6, 435.9, 435.9), Base=(697.0, 650.5, 723.6), Bull=(928.4, 933.5, 1001.8)),
            D=dict(Bear=(115.2, 43.6, 33.6), Base=(158.4, 77.7, 45.8), Bull=(171.1, 107.3, 58.9)),
            EPS=dict(Bear=(115.1, 57.5, 48.0, 48.0), Base=(172.6, 115.1, 76.7, 67.1), Bull=(191.8, 153.4, 105.5, 86.3)))}
ALL_CO = ("CM", "CG", "CN", "CA", "CU")


def setup_co(cos):
    M.CO = {}
    for c in cos:
        d = copy.deepcopy(CO_SRC[c]); p = P5[d["names"][0]]
        d["V"] = {s: (reglide(d["V"][s], d["EPS"][s], p, d["p_an"], d["e27"]) if s != "Bear" else d["V"][s]) for s in SC}
        M.CO[c] = d


def build(co_blocks=ALL_CO):
    setup_co(co_blocks); lay = {k: list(v) for k, v in LAY.items()}
    eps = dict(EPS27)
    if "CA" not in co_blocks: lay["E"] = ["AMZN"]+lay["E"]; eps["AMZN"] = 10.65
    if "CU" not in co_blocks: lay["H2"] = ["MU"]; eps["MU"] = 191.80
    b = {}
    for L, ns in lay.items():
        v = sum(W5[n] for n in ns); e = sum(W5[n]*eps[n]/P5[n] for n in ns); b[L] = dict(kind="layer", v=v, e=e, pe=v/e)
    for c, d in M.CO.items():
        v = sum(W5[n] for n in d["names"]); sh = sum(W5[n]/P5[n] for n in d["names"])
        b[c] = dict(kind="co", v=v, e=sh*d["cons"], pe=v/(sh*d["cons"]), sh=sh)
    b["EN"] = dict(kind="en", v=EN_V, e=EN_V/EN_PE, pe=EN_PE)
    return b


S_UNIT = 209.14/199.63                                  # 9-Oct value units -> 5-Nov units (URTH)
E_R = 4.062306*S_UNIT*1.006                             # rest CY27 earnings (18 Oct model 4.0623 in 9-Oct units) x S&P CY27 revision
USD_SH = 0.70
USDP = {"Bear": [10.70/9.5555, 10.42/9.5555, 10.42/9.5555], "Base": [1, 1, 1], "Bull": [9.27/9.5555]*3}
I44P = {"Bear": [1.08, 1.06, 1.06], "Base": [1, 1, 1], "Bull": [0.98]*3}
FXMIX = {s: [USD_SH*u+(1-USD_SH)*i for u, i in zip(USDP[s], I44P[s])] for s in SC}
M.FX = dict(FXMIX)
REST_EPS = {"Bear": [.83, .87, .95, 1.02], "Base": [.97*1.055**k for k in range(4)], "Bull": [1.00, 1.07, 1.14, 1.21]}
REST_PE = {"Bear": [15.08, 14.96, 14.86], "Base": [17.17, 16.67, 16.29], "Bull": [17.78, 17.61, 17.44]}
REST_PAY = {"Bear": [.49, .47, .48], "Base": [.50, .48, .48], "Bull": [.50, .49, .49]}
FPE0 = 17.38*199.63/204.64; PB0 = 4.06*199.63/204.64    # MSCI World 30 Oct scaled by the URTH move since 30 Oct


def world(dp=0.0, rest=None, pex_shift=0.0, vm=1.0, co_blocks=ALL_CO, e_r=None):
    rest = rest or REST_EPS; WB = build(co_blocks); P0 = 100.0
    v_r = P0-sum(x["v"] for x in WB.values()); e_r = e_r or E_R; E0 = e_r+sum(x["e"] for x in WB.values())
    out = {}; det = {}
    for s in SC:
        parts = [M.vals(n, x, s, pex_shift) for n, x in WB.items()]
        eps = rest[s]
        parts.append(([(REST_PE[s][k]+pex_shift)*e_r*eps[k+1] for k in range(3)], [REST_PAY[s][k]*e_r*eps[k] for k in range(3)],
                      0.025*v_r*STUB, [e_r*x for x in eps]))
        out[s] = M.evaluate(P0*(1+dp), [([vm*v for v in p[0]], p[1], p[2]) for p in parts], s)
        det[s] = dict(eps=[sum(p[3][k] for p in parts)/E0 for k in range(4)], V=[vm*sum(p[0][k] for p in parts) for k in range(3)],
                      D=[sum(p[1][k] for p in parts) for k in range(3)], Dst=sum(p[2] for p in parts),
                      blk={n: [p[3][k]/x["e"] for k in range(4)] for (n, x), p in zip(WB.items(), parts)})
    return out, det, dict(v_r=v_r, e_r=e_r, pe_r=v_r/e_r, P0=P0, WB=WB, E0=E0)


def er(o):
    E = (o["Base"]["irr"]-NIBW)*100-FEE; R = (o["Base"]["r"][0]-o["Bear"]["r"][0])*100; return E, R, E/R


def solve(fn, tgt, lo=-0.5, hi=0.5):
    for _ in range(80):
        m = (lo+hi)/2
        if fn(m) > tgt: lo = m
        else: hi = m
    return m


URTH_NOK = 199.63*9.2944

if __name__ == "__main__":
    o, d, info = world(); P0 = info["P0"]; E0 = info["E0"]; WB = info["WB"]
    print(f"World 5 Nov: stub {STUB*365:.0f} d, T {T:.3f}, NIBOR window {NIBW*100:.2f}; P/E now on CY27 {P0/E0:.2f}; MSCI fwd now {FPE0:.2f}; P/B now {PB0:.2f}")
    print(f" rest: value {info['v_r']:.1f}%  earnings {info['e_r']/E0*100:.1f}%  P/E {info['pe_r']:.2f};  energy v {EN_V:.2f} P/E {EN_PE:.2f}")
    for n, x in WB.items(): print(f"  {n:3s} v {x['v']:6.2f}  e% {x['e']/E0*100:5.1f}  P/E {x['pe']:6.2f}")
    co = [n for n in WB if WB[n]["kind"] == "co"]; ly = [n for n in WB if WB[n]["kind"] == "layer"]
    for lab, g in [("companies", co), ("layers", ly), ("AI+co", co+ly)]:
        v = sum(WB[n]["v"] for n in g); e = sum(WB[n]["e"] for n in g); print(f"  {lab}: value {v:.1f}%, earnings {e/E0*100:.1f}%, P/E {v/e:.1f}")
    for s in SC:
        x = o[s]; eps = [E0*v for v in d[s]["eps"]]; V = d[s]["V"]; vmul = [V[k]/eps[k+1] for k in range(3)]
        print(f" {s}: IRR {x['irr']*100:.2f} r {[round(v*100,1) for v in x['r']]} stub {x['stub']*100:.2f} EPS {[round(v,3) for v in d[s]['eps']]} VT {x['VT']:.1f} sumD {x['sumD']:.1f} "
              f"Pk {x['Pk']:.1f} MoS {x['Pk']/100-1:+.1%} value multiple {[round(v,2) for v in vmul]} payout {sum(d[s]['D'])/sum(eps[:3]):.2f}")
        eg = (d[s]["eps"][3])**(1/T)-1; mg = (vmul[2]/(P0/E0))**(1/T)-1; fg = M.FX[s][2]**(1/T)-1
        print(f"   split: d {x['d']*100:.2f} g {x['g']*100:.2f} = EPS (USD) {eg*100:.2f} value multiple {mg*100:.2f} FX {fg*100:.2f}; c {(x['irr']-x['d']-x['g'])*100:.2f}  capital kept {x['sumD']+x['VT']-100:+.1f}%")
        e26 = E0/1.13; B = P0/PB0 + e26*STUB - d[s]["Dst"]; roe = []
        for k in range(3): roe.append(eps[k]/B); B += eps[k]-d[s]["D"][k]
        print(f"   ROE path {[round(v*100,1) for v in roe]} 2030 {eps[3]/B*100:.1f}%  exit P/B {V[2]/B:.2f}  (trailing ROE {4.06/22.29*100:.1f}%, forward {PB0/FPE0*100:.1f}%)")
        ai = [n for n in WB if n != "EN"]; eAI = sum(WB[n]["e"] for n in ai)
        print("   AI+co EPS (own CY27=1):", [round(sum(WB[n]['e']*d[s]['blk'][n][k] for n in ai)/eAI, 3) for k in range(4)],
              " energy:", [round(d[s]['blk']['EN'][k], 3) for k in range(4)])
    M.FX = {s: [1, 1, 1] for s in SC}; ou, _, _ = world(); M.FX = dict(FXMIX)
    print(" USD:", {s: (round(ou[s]['irr']*100, 2), [round(v*100, 1) for v in ou[s]['r']]) for s in SC})
    E, R, r = er(o); print(f" E {E:.2f} R {R:.1f} E/R {r:.3f}")
    oo, _, _ = world(co_blocks=("CM", "CG", "CN"))
    print(" 17 Oct block set (Amazon on the E rest row, Micron on H2):", [round(oo[s]['irr']*100, 2) for s in SC], [round(oo[s]['r'][0]*100, 1) for s in SC], "E/R", round(er(oo)[2], 3))
    for lab, f in [("rest 4.5%", {"Base": [.97*1.045**k for k in range(4)]}), ("rest 6.5%", {"Base": [.97*1.065**k for k in range(4)]})]:
        rr = dict(REST_EPS); rr.update(f); print(f" sens {lab}: Base {world(rest=rr)[0]['Base']['irr']*100:.2f}")
    for sh in (-1, 1): print(f" sens multiples {sh:+d}: Base {world(pex_shift=sh)[0]['Base']['irr']*100:.2f}")
    for m in (0.9, 1.1): print(f" sens all values x{m}: Base {world(vm=m)[0]['Base']['irr']*100:.2f}")
    for lab, f in [("NOK -10% by 2029", [1.033, 1.067, 1.10]), ("NOK +10% by 2029", [0.967, 0.933, 0.90])]:
        M.FX = dict(FXMIX); M.FX["Base"] = f; print(f" sens FX {lab}: Base {world()[0]['Base']['irr']*100:.2f}")
    M.FX = dict(FXMIX)
    for dB in (-10, 10):
        set_energy(dB=dB); print(f" sens Brent {dB:+d}: Base {world()[0]['Base']['irr']*100:.2f}")
    set_energy()
    for lab, ef in [("rest CY27 revision 0%", 4.062306*S_UNIT), ("rest CY27 revision -3%", 4.062306*S_UNIT*0.97)]:
        print(f" sens {lab}: Base {world(e_r=ef)[0]['Base']['irr']*100:.2f}")
    set_energy(pay=0.76); print(f" check: energy payout 0.76 (18 Oct): Base {world()[0]['Base']['irr']*100:.3f}"); set_energy()
    for lab, fn, tgt in [("E/R=0.254", lambda p: er(world(dp=p)[0])[2], 0.254), ("E/R=0.216 (Bear as shock)", lambda p: er(world(dp=p)[0])[2], 0.216),
                         ("Base=12%", lambda p: world(dp=p)[0]['Base']['irr'], 0.12), ("Base=7.2% (HY market Base)", lambda p: world(dp=p)[0]['Base']['irr'], 0.072)]:
        p = solve(fn, tgt); oo = world(dp=p)[0]
        print(f" trigger {lab}: dp {p*100:+.1f}%  URTH NOK {URTH_NOK*(1+p):.0f}  URTH USD {199.63*(1+p):.1f}  fwd P/E (MSCI basis) {FPE0*(1+p):.1f}  Base {oo['Base']['irr']*100:.1f} E/R {er(oo)[2]:.3f}")
