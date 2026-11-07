# Bridge of the World Base window IRR, 18 Oct (5.22%) -> 6 Nov. Step 1 runs the 18 Oct model (upd.py) at the 5 Nov prices and stub with
# unchanged future values (price-only). The later steps use world2.py.
import sys, os, json
sys.path.insert(0, os.getcwd())
import upd
M = upd.M
o, _, _ = upd.world(); print(f"0 18 Oct model: {[round(o[s]['irr']*100, 2) for s in M.SC]} 2027 {[round(o[s]['r'][0]*100, 1) for s in M.SC]} E/R {upd.er(o)[2]:.3f}")
RC = json.load(open("dl2/recent_1105.json")); EU5 = 1.1235
P5 = {n: RC[n]["2026-11-05"] for n in M.P15 if n != "SAP"}; P5["SAP"] = 215.75*EU5
M.STUB = 55/365; M.T = M.STUB+3; upd.T = M.T
M.nibw = ((1.048)**M.STUB*1.0479*1.0439*1.0386)**(1/M.T)-1; upd.NIBW = M.nibw
o, _, _ = upd.world(); print(f"1a + stub 55 days, NIBOR window: {[round(o[s]['irr']*100, 2) for s in M.SC]} E/R {upd.er(o)[2]:.3f}")
M.P15 = P5; M.R_W = 199.63/209.14; M.EN_MOVE = 57.27/59.88
o, _, _ = upd.world(); print(f"1b + 5 Nov prices (unchanged future values): {[round(o[s]['irr']*100, 2) for s in M.SC]} 2027 {[round(o[s]['r'][0]*100, 1) for s in M.SC]} E/R {upd.er(o)[2]:.3f}")
import world2 as W
SC = W.SC
def show(lab, **kw):
    o, d, info = W.world(**kw); print(f"{lab}: {[round(o[s]['irr']*100, 2) for s in SC]} 2027 {[round(o[s]['r'][0]*100, 1) for s in SC]} E/R {W.er(o)[2]:.3f}  P/E now {100/info['E0']:.2f}")
    return o
W.set_energy(pay=0.76)
show("2 + company analyses re-marked (MSFT v3, GOOGL v2, NVDA v1.2), AI E cash conversion, 4 Nov weights, 1 Nov consensus; 17 Oct block set; rest revision 0",
     co_blocks=("CM", "CG", "CN"), e_r=4.062306*W.S_UNIT)
show("3 + rest CY27 revision +0.6%", co_blocks=("CM", "CG", "CN"))
show("4 + Amazon v2 and Micron v3 as company blocks", )
W.set_energy()
show("5 + energy payout 0.58 (= final)")
