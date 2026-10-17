# Equity BBB Update 1 (17 Oct 2026): World split into company blocks + AI layers + energy + explicit rest; Oslo repriced
import sys, os; sys.path.insert(0, os.getcwd())
import idxai3 as M
FEE = 0.20; NIBW = M.nibw
# --- 16 Oct closes ---
EU = 1.1213
P16 = {"MSFT": 529.05, "GOOGL": 340.59, "GOOG": 336.91, "AMZN": 250.00, "META": 709.33, "ORCL": 128.23, "NVDA": 214.13, "AMD": 528.75,
       "AVGO": 328.75, "MRVL": 227.83, "MU": 878.84, "ASML": 1641.52, "AMAT": 409.29, "LRCX": 263.94, "ANET": 176.98, "VRT": 206.42,
       "ETN": 391.25, "NOW": 141.97, "CRM": 240.70, "ADBE": 245.20, "PLTR": 186.03, "SAP": 199.22*EU, "INTU": 325.15, "SNOW": 306.84, "DDOG": 247.11}
M.P15 = P16; M.R_W = 206.34/209.14; M.EN_MOVE = 62.98/59.88
B27 = 88   # oil BBB 17 Oct: Base 2027 85 -> 88
M.EN = (dict(Bear=tuple((x-30)/49 for x in (65, 60, 60, 60)), Base=tuple((x-30)/49 for x in (B27, 77, 72, 70)),
             Bull=tuple((x-30)/49 for x in (B27, 77, 72, 70))), (11, 12, 13), .55)
# --- rest of World: explicit EPS paths (rest CY27 consensus = 1); multiple and payout paths kept from the 11 Oct World view ---
REST_EPS = {"Bear": [.83, .87, .95, 1.02], "Base": [.97*1.055**k for k in range(4)], "Bull": [1.00, 1.07, 1.14, 1.21]}
REST_PE = {"Bear": [15.08, 14.96, 14.86], "Base": [17.17, 16.67, 16.29], "Bull": [17.78, 17.61, 17.44]}
REST_PAY = {"Bear": [.49, .47, .48], "Base": [.50, .48, .48], "Bull": [.50, .49, .49]}
def world(dp=0.0, cost=0.0, rest=None, pex_shift=0.0, only_rest_old=False):
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
        out[s] = M.evaluate(P0*(1+dp), [p[:3] for p in parts], s, cost)
        det[s] = dict(eps=[sum(p[3][k] for p in parts)/M.E0 for k in range(4)], V=[sum(p[0][k] for p in parts) for k in range(3)])
    return out, det, dict(v_r=v_r, e_r=e_r, pe_r=v_r/e_r, P0=P0, WB=WB)
def er(o): E = (o["Base"]["irr"]-NIBW)*100-FEE; R = (o["Base"]["r"][0]-o["Bear"]["r"][0])*100; return E, R, E/R
def solve(fn, tgt, lo=-0.5, hi=0.5):
    for _ in range(80):
        m = (lo+hi)/2
        if fn(m) > tgt: lo = m
        else: hi = m
    return m
if __name__ == "__main__":
    o, d, info = world()
    print(f"World 16 Oct: P0 {info['P0']:.2f} rest share {info['v_r']/info['P0']*100:.1f}% value, rest P/E {info['pe_r']:.2f}, rest earnings {info['e_r']/M.E0*100:.1f}%")
    blk = info['WB']; ai = [n for n in blk if n != 'EN']
    print(f" AI+co value {sum(blk[n]['v'] for n in ai)/info['P0']*100:.1f}% P/E {sum(blk[n]['v'] for n in ai)/sum(blk[n]['e'] for n in ai):.1f}; energy {blk['EN']['v']/info['P0']*100:.2f}%")
    for s in M.SC:
        x = o[s]; print(f" {s}: IRR {x['irr']*100:.2f} r {[round(v*100,1) for v in x['r']]} stub {x['stub']*100:.1f} EPS {[round(v,3) for v in d[s]['eps']]} VT {x['VT']:.1f} sumD {x['sumD']:.1f} Pk {x['Pk']:.1f} d {x['d']*100:.2f} g {x['g']*100:.2f}")
    E, R, r = er(o); print(f" E {E:.2f} R {R:.1f} E/R {r:.3f}  NIBOR window {NIBW*100:.2f}")
    o2, d2, _ = world(only_rest_old=True); print(" old World path at 16 Oct prices (implied rest):", [round(o2[s]['irr']*100,2) for s in M.SC], [round(o2[s]['r'][0]*100,1) for s in M.SC], 'E/R', round(er(o2)[2],3))
    # AI/company blocks alone
    for lab, f in [("Base rest 4.5%", {"Base": [.97*1.045**k for k in range(4)]}), ("Base rest 6.5%", {"Base": [.97*1.065**k for k in range(4)]}), ("Base rest no haircut 5.5%", {"Base": [1.0*1.055**k for k in range(4)]})]:
        rr = dict(REST_EPS); rr.update(f); oo, _, _ = world(rest=rr); print(f" sens {lab}: Base {oo['Base']['irr']*100:.2f}")
    for sh in (-1, 1):
        oo, _, _ = world(pex_shift=sh); print(f" sens exit/multiple {sh:+d}: Base {oo['Base']['irr']*100:.2f}")
    # triggers (price change at unchanged earnings and future values)
    for lab, fn, tgt in [("E/R=0.196", lambda p: er(world(dp=p)[0])[2], 0.196), ("Base=12%", lambda p: world(dp=p)[0]['Base']['irr'], 0.12),
                         ("Base=6.9%", lambda p: world(dp=p)[0]['Base']['irr'], 0.069), ("E/R=0.291", lambda p: er(world(dp=p)[0])[2], 0.291)]:
        p = solve(fn, tgt); oo = world(dp=p)[0]; print(f" trigger {lab}: dp {p*100:+.1f}%  Base {oo['Base']['irr']*100:.1f} E/R {er(oo)[2]:.3f}")
