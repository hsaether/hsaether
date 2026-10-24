# Equity BBB Update 1 amended 18 Oct 2026 (skill 2026-10-18.1): World = company blocks + AI layer blocks + energy + explicit rest.
# One rule with Oslo: energy payout 0.76 (Oslo energy: latest declared dividend annualised / trailing EPS) and c = 0.80 in both indices.
# Currency: 70% of World on USD/NOK, 30% on I-44. Prices: 16 Oct close.
import sys, os; sys.path.insert(0, os.getcwd())
import idxai3 as M
FEE = 0.20; NIBW = M.nibw; T = M.T
# --- 16 Oct closes ---
EU = 1.1213
P16 = {"MSFT": 529.05, "GOOGL": 340.59, "GOOG": 336.91, "AMZN": 250.00, "META": 709.33, "ORCL": 128.23, "NVDA": 214.13, "AMD": 528.75,
       "AVGO": 328.75, "MRVL": 227.83, "MU": 878.84, "ASML": 1641.52, "AMAT": 409.29, "LRCX": 263.94, "ANET": 176.98, "VRT": 206.42,
       "ETN": 391.25, "NOW": 141.97, "CRM": 240.70, "ADBE": 245.20, "PLTR": 186.03, "SAP": 199.22*EU, "INTU": 325.15, "SNOW": 306.84, "DDOG": 247.11}
M.P15 = P16; M.R_W = 206.34/209.14; M.EN_MOVE = 62.98/59.88
B27 = 88; EN_PAY = 0.76     # oil BBB 17 Oct: Base 2027 88; energy payout as Oslo energy (was 0.55)
M.EN = (dict(Bear=tuple((x-30)/49 for x in (65, 60, 60, 60)), Base=tuple((x-30)/49 for x in (B27, 77, 72, 70)),
             Bull=tuple((x-30)/49 for x in (B27, 77, 72, 70))), (11, 12, 13), EN_PAY)
# --- currency: USD share on USD/NOK, the rest on I-44 (relative to the 16 Oct spot) ---
USD_SH = 0.70
USDP = {"Bear": [10.70/9.5555, 10.42/9.5555, 10.42/9.5555], "Base": [1, 1, 1], "Bull": [9.27/9.5555]*3}
I44P = {"Bear": [1.08, 1.06, 1.06], "Base": [1, 1, 1], "Bull": [0.98]*3}
FXMIX = {s: [USD_SH*u+(1-USD_SH)*i for u, i in zip(USDP[s], I44P[s])] for s in M.SC}
M.FX = dict(FXMIX)
# --- rest of World: explicit EPS paths (rest CY27 consensus = 1); multiple and payout paths kept from the 11 Oct World view ---
REST_EPS = {"Bear": [.83, .87, .95, 1.02], "Base": [.97*1.055**k for k in range(4)], "Bull": [1.00, 1.07, 1.14, 1.21]}
REST_PE = {"Bear": [15.08, 14.96, 14.86], "Base": [17.17, 16.67, 16.29], "Bull": [17.78, 17.61, 17.44]}
REST_PAY = {"Bear": [.49, .47, .48], "Base": [.50, .48, .48], "Bull": [.50, .49, .49]}
FPE0 = 17.92*206.34/206.23; PB0 = 4.10*206.34/206.23    # MSCI World 30 Sep scaled by the URTH move since 30 Sep
def world(dp=0.0, cost=0.0, rest=None, pex_shift=0.0, vm=1.0, only_rest_old=False):
    rest = rest or REST_EPS
    WB = M.blocks_W(); P0 = 100*M.R_W
    v_r = P0-sum(x["v"] for x in WB.values()); e_r = M.E0-sum(x["e"] for x in WB.values())
    out = {}; det = {}
    for s in M.SC:
        parts = [M.vals(n, x, s, pex_shift) for n, x in WB.items()]
        if only_rest_old:
            R = M.world_rest(s, pex_shift, (), WB); parts.append((R["V"], R["D"], R["Dst"], [R["e"]*x for x in R["eps"]]))
        else:
            eps = rest[s]
            parts.append(([(REST_PE[s][k]+pex_shift)*e_r*eps[k+1] for k in range(3)], [REST_PAY[s][k]*e_r*eps[k] for k in range(3)],
                          0.025*v_r*M.STUB, [e_r*x for x in eps]))
        out[s] = M.evaluate(P0*(1+dp), [([vm*v for v in p[0]], p[1], p[2]) for p in parts], s, cost)
        det[s] = dict(eps=[sum(p[3][k] for p in parts)/M.E0 for k in range(4)], V=[vm*sum(p[0][k] for p in parts) for k in range(3)],
                      D=[sum(p[1][k] for p in parts) for k in range(3)], Dst=sum(p[2] for p in parts))
    return out, det, dict(v_r=v_r, e_r=e_r, pe_r=v_r/e_r, P0=P0, WB=WB)
def er(o): E = (o["Base"]["irr"]-NIBW)*100-FEE; R = (o["Base"]["r"][0]-o["Bear"]["r"][0])*100; return E, R, E/R
def solve(fn, tgt, lo=-0.5, hi=0.5):
    for _ in range(80):
        m = (lo+hi)/2
        if fn(m) > tgt: lo = m
        else: hi = m
    return m
if __name__ == "__main__":
    o, d, info = world(); P0 = info["P0"]; E0 = M.E0
    print(f"World 16 Oct: P0 {P0:.2f} rest share {info['v_r']/P0*100:.1f}% value, rest P/E {info['pe_r']:.2f}, rest earnings {info['e_r']/E0*100:.1f}%  P/E now {P0/E0:.2f}  MSCI fwd now {FPE0:.2f}")
    print(" FX mix:", {s: [round(x, 4) for x in FXMIX[s]] for s in M.SC})
    for s in M.SC:
        x = o[s]; eps = [E0*v for v in d[s]["eps"]]; V = d[s]["V"]
        vmul = [V[k]/eps[k+1] for k in range(3)]
        print(f" {s}: IRR {x['irr']*100:.2f} r {[round(v*100,1) for v in x['r']]} stub {x['stub']*100:.2f} EPS {[round(v,3) for v in d[s]['eps']]} VT {x['VT']:.1f} sumD {x['sumD']:.1f} "
              f"Pk {x['Pk']:.1f} MoS {x['Pk']/100-1:+.1%} d {x['d']*100:.2f} g {x['g']*100:.2f} value multiple {[round(v,2) for v in vmul]} payout {sum(d[s]['D'])/sum(eps[:3]):.2f}")
        eg = (d[s]["eps"][3])**(1/T)-1; mg = (vmul[2]/(P0/E0))**(1/T)-1; fg = M.FX[s][2]**(1/T)-1
        print(f"   split: d {x['d']*100:.2f} g {x['g']*100:.2f} = EPS (USD) {eg*100:.2f} value multiple {mg*100:.2f} FX {fg*100:.2f}; c {(x['irr']-x['d']-x['g'])*100:.2f}  capital kept {x['sumD']+x['VT']-100:+.1f}%")
        e26 = E0/1.13; B = P0/PB0 + e26*M.STUB - d[s]["Dst"]; roe = []
        for k in range(3): roe.append(eps[k]/B); B += eps[k]-d[s]["D"][k]
        print(f"   ROE path {[round(v*100,1) for v in roe]} 2030 {eps[3]/B*100:.1f}%  exit P/B {V[2]/B:.2f}  (P/B now {PB0:.2f}; trailing ROE {4.10/22.69*100:.1f}%, forward {PB0/FPE0*100:.1f}%)")
    E, R, r = er(o); print(f" E {E:.2f} R {R:.1f} E/R {r:.3f}  NIBOR window {NIBW*100:.2f}")
    o2, d2, _ = world(only_rest_old=True); print(" old World path (implied rest):", [round(o2[s]['irr']*100,2) for s in M.SC])
    for lab, f in [("Base rest 4.5%", {"Base": [.97*1.045**k for k in range(4)]}), ("Base rest 6.5%", {"Base": [.97*1.065**k for k in range(4)]}), ("Base rest no haircut 5.5%", {"Base": [1.0*1.055**k for k in range(4)]})]:
        rr = dict(REST_EPS); rr.update(f); oo, _, _ = world(rest=rr); print(f" sens {lab}: Base {oo['Base']['irr']*100:.2f}")
    for sh in (-1, 1):
        oo, _, _ = world(pex_shift=sh); print(f" sens multiples {sh:+d}: Base {oo['Base']['irr']*100:.2f}")
    for m in (0.9, 1.1):
        oo, _, _ = world(vm=m); print(f" sens all values x{m}: Base {oo['Base']['irr']*100:.2f}")
    for lab, f in [("NOK -10% by 2029", [1.033, 1.067, 1.10]), ("NOK +10% by 2029", [0.967, 0.933, 0.90])]:
        M.FX = dict(FXMIX); M.FX["Base"] = f; oo, _, _ = world(); print(f" sens FX {lab}: Base {oo['Base']['irr']*100:.2f}")
    M.FX = dict(FXMIX)
    M.FX = dict(USDP); oo, _, _ = world(); print(f" check: 100% on USD/NOK: Bear27 {oo['Bear']['r'][0]*100:.1f} IRR {[round(oo[s]['irr']*100,2) for s in M.SC]} E/R {er(oo)[2]:.3f}")
    M.FX = dict(FXMIX)
    M.EN = (M.EN[0], M.EN[1], 0.55); oo, _, _ = world(); print(f" check: energy payout 0.55: Base {oo['Base']['irr']*100:.3f}")
    M.EN = (M.EN[0], M.EN[1], EN_PAY)
    base = solve(lambda p: er(world(dp=p)[0])[2], 0.196)
    for lab, fn, tgt in [("E/R=0.196", lambda p: er(world(dp=p)[0])[2], 0.196), ("Base=12%", lambda p: world(dp=p)[0]['Base']['irr'], 0.12),
                         ("Base=6.8% (HY market Base, hy-market-bbb)", lambda p: world(dp=p)[0]['Base']['irr'], 0.068)]:
        p = solve(fn, tgt); oo = world(dp=p)[0]
        print(f" trigger {lab}: dp {p*100:+.1f}%  URTH NOK {206.34*9.4135*(1+p):.0f}  fwd P/E (MSCI basis) {FPE0*(1+p):.1f}  Base {oo['Base']['irr']*100:.1f} E/R {er(oo)[2]:.3f}")
