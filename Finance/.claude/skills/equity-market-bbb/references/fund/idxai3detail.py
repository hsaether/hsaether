import sys, os, copy; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idxai3 as M
SC = M.SC
NAV = {"W": 867.98, "C": 230.31}   # 15 Oct 2026 NAVs (DNB AM; Nordnet)
FUNDS = {"DNB_N": ("W", 0.0025), "DNB_P": ("W", 0.0021), "NGI": ("C", 0.0019)}


def line(lab, o):
    E, R, ER = M.er(o)
    print(f" {lab:58s} Bear {o['Bear']['irr']*100:6.2f} Base {o['Base']['irr']*100:5.2f} Bull {o['Bull']['irr']*100:5.2f} | 27 {o['Bear']['r'][0]*100:6.1f}/{o['Base']['r'][0]*100:5.1f}/{o['Bull']['r'][0]*100:5.1f} | E/R {ER:.3f} | MoS {o['Base']['Pk']/100-1:+.1%}")


print("=== Company block check (USD, at the analysis price $214.13 for NVDA; stub as the analysis) ===")
for c, P in (("CN", 214.13), ("CM", 540.26), ("CG", 349.28)):
    d = M.CO[c]
    for s in SC:
        fl = [(0, -P), (M.STUB, d["stub"])]+[(M.STUB+k+0.5, d["D"][s][k]) for k in range(3)]+[(M.T, d["V"][s][2])]
        print(f" {c} {s}: {M.irr(fl)*100:.1f}%", end="")
    print()

print("\n=== Blocks alone, before cost, NOK ===")
for which in ("W", "C"):
    print("--", which)
    _, _, bl = M.run(which)
    groups = [(n, [n]) for n in bl]+[("AI layers + co", [n for n in bl if n != "EN"]), ("REST", ["REST"]), ("EN+REST", ["EN", "REST"])]
    for lab, sel in groups:
        o, _, _ = M.run(which, only=sel); line(lab, o)
    o, _, _ = M.run(which, only=["CN"], co_layer=("CN",)); line("CN on the H1 layer path", o)
    o, _, _ = M.run(which, only=["H1", "CN"]); line("H1 + CN (all compute)", o)
    o, _, _ = M.run(which, only=["CM", "CG"], co_layer=("CM", "CG")); line("CM+CG on the E layer path", o)

print("\n=== Funds after cost ===")
for key, (w, c) in FUNDS.items():
    o, d, _ = M.run(w, cost=c); E, R, ER = M.er(o); nav = NAV[w]
    print(f"\n{key}: E {E:.2f} R {R:.1f} E/R {ER:.3f}")
    for s in SC:
        x = o[s]; cum = [(x['lv'][i]/100)**(1/(M.STUB+i))-1 for i in range(1, 4)]
        print(f" {s}: IRR {x['irr']*100:.2f} | stub {x['stub']*100:.1f} r {[round(v*100, 1) for v in x['r']]} | NAV {[round(nav*v/100, 1) for v in x['lv']]} | IRR to YE {[round(v*100, 1) for v in cum]}"
              f" | Pk NAV {nav*x['Pk']/100:.1f} MoS {x['Pk']/100-1:+.1%} | kept {(x['sumD']+x['VT'])/100-1:+.1%} | sumD {x['sumD']:.1f} VT {x['VT']:.1f}"
              f" | 920k end-29 {920*x['lv'][3]/100:.0f}k, 2027 chg {920*(x['lv'][1]-x['lv'][0])/100:+.0f}k | d {x['d']*100:.2f} g {x['g']*100:.2f}")
    print(" share of Bull priced", round((100-o['Base']['Pk'])/(o['Bull']['Pk']-o['Base']['Pk'])*100))

print("\n=== Stress and checks, after cost ===")
for key, (w, c) in FUNDS.items():
    ob, _, _ = M.run(w, cost=c, ai_only="Bear"); ou, _, _ = M.run(w, cost=c, ai_only="Bull"); ot, _, _ = M.run(w, cost=c, rest_trend=True)
    print(f" {key}: AI-only Bear {ob['Bear']['irr']*100:.2f} (2027 {ob['Bear']['r'][0]*100:.1f}) | AI-only Bull {ou['Bull']['irr']*100:.2f} (2027 {ou['Bull']['r'][0]*100:.1f})"
          f" | rest at trend: Base {ot['Base']['irr']*100:.2f} E/R {M.er(ot)[2]:.3f}")
o, _, _ = M.run("W", rest_trend=True); print(" World before cost, rest at trend:", round(o['Base']['irr']*100, 2))
R = M.world_rest("Base"); print(" implied rest EPS growth 2027->2030n", round(((R['eps'][3]/R['eps'][0])**(1/3)-1)*100, 2), "%/yr; from consensus", round((R['eps'][3]**(1/3)-1)*100, 2))
WB = M.blocks_W()
for s in SC:
    ai = [n for n in WB if n != "EN"]
    e0 = sum(WB[n]["e"] for n in ai)
    path = [sum(M.vals(n, WB[n], s)[3][k] for n in ai)/e0 for k in range(4)]
    cash = sum(M.vals(n, WB[n], s)[0][2] for n in ai if WB[n]["kind"] == "layer")
    M.RET = False; nocash = sum(M.vals(n, WB[n], s)[0][2] for n in ai if WB[n]["kind"] == "layer"); M.RET = True
    print(f" World AI+co EPS {s}: {[round(v, 3) for v in path]} | layer retained cash in V_2029: {cash-nocash:.2f} (index value {100*M.R_W:.1f})")
M.RET = False
for s in SC:
    R0 = M.world_rest(s); print(f" rest without AI retained cash {s}: V/EPS {[round(x, 2) for x in R0['pepath']]}")
M.RET = True
# validation: at the 9 Oct price and zero cost the split reproduces World
rw = M.R_W; M.R_W = 1.0; o, _, _ = M.run("W"); print(" check at 9 Oct price, zero cost:", [round(o[s]['irr']*100, 2) for s in SC]); M.R_W = rw

print("\n=== Attribution from the 15 Oct version (after cost) ===")
def att(lab):
    for key in ("DNB_N", "NGI"):
        w, c = FUNDS[key]; o, _, _ = M.run(w, cost=c); line(f"{lab} [{key}]", o)
M.RET = False; M.BEAR_V1 = True; M.CONS_V1 = True; M.CN_LAYER = True
att("1 prices/NAV 15 Oct, stub 75 d (method v1)")
M.CONS_V1 = False; att("2 + calendarised consensus (AI BBB U2)")
M.BEAR_V1 = False; att("3 + v2 Bear paths (H1, H3, H4)")
M.CN_LAYER = False; att("4 + NVIDIA company block")
M.RET = True; att("5 + retained cash in layer and energy blocks (= model)")

print("\n=== Sensitivities ===")
for key, w, c in [("NGI", "C", 0.0019), ("DNB_N", "W", 0.0025)]:
    print("--", key)
    cases = [("model", {}), ("exit P/E -1", dict(pex_shift=-1)), ("exit P/E +1", dict(pex_shift=1)), ("CY27 consensus -5%", dict(em=0.95))]
    if w == "C":
        cases += [("rest premium halves", dict(prem_mode="half")), ("rest premium gone", dict(prem_mode="gone")), ("tail x0.7", dict(tail=0.7)),
                  ("tail x1.3", dict(tail=1.3)), ("MSFT+GOOGL on E layer", dict(co_layer=("CM", "CG"))), ("NVDA on H1 layer", dict(co_layer=("CN",))),
                  ("all three companies on their layers", dict(co_layer=("CM", "CG", "CN")))]
    for lab, kw in cases:
        o, _, _ = M.run(w, cost=c, **kw); line(lab, o)
    if w == "C":
        for lab, cc in [("hidden swap drag +0.20 (cost 0.39)", 0.0039), ("cost 0.25", 0.0025)]:
            o, _, _ = M.run(w, cost=cc); line(lab, o)
        cv = copy.deepcopy(M.CONV)
        M.CONV["EN"] = {s: (.55,)*3 for s in SC}; o, _, _ = M.run(w, cost=c); line("energy c = payout 0.55 (no retained cash)", o)
        M.CONV["EN"] = {s: (1.0,)*3 for s in SC}; o, _, _ = M.run(w, cost=c); line("energy c = 1.0", o)
        M.CONV = cv
        for k in ("E", "H1"):
            cv = copy.deepcopy(M.CONV); M.CONV[k] = {s: tuple(x-0.2 for x in M.CONV[k][s]) for s in SC}
            o, _, _ = M.run(w, cost=c); line(f"{k} cash conversion -0.2", o); M.CONV = cv
        M.PEX_OVR = {("H2", "Bear"): 4.8}; o, _, _ = M.run(w, cost=c); line("memory-stressed Bear (exit 4.8x = today)", o); M.PEX_OVR = {}
        c0 = copy.deepcopy(M.CO)
        M.CO["CN"]["cons"] = 15.91
        M.CO["CN"]["V"] = dict(Bear=(132.2, 156.7, 171.1), Base=(248.1, 273.5, 286.3), Bull=(302.0, 366.0, 420.7))
        M.CO["CN"]["D"] = dict(Bear=(5.47, 5.73, 6.03), Base=(6.80, 8.86, 9.22), Bull=(7.23, 10.05, 11.21))
        M.CO["CN"]["EPS"] = dict(Bear=(11.14, 9.55, 11.14, 11.93), Base=(14.64, 15.59, 15.91, 15.43), Bull=(15.92, 18.31, 19.90, 20.68))
        o, _, _ = M.run(w, cost=c); line("NVDA on its unadjusted v1 analysis (FY basis, old Bear)", o)
        M.CO = c0


def solve(fn, lo=-0.6, hi=0.4):
    for _ in range(70):
        m = (lo+hi)/2
        if fn(m) > 0: lo = m
        else: hi = m
    return m


print("\n=== Triggers (NAV change from 15 Oct at unchanged earnings) ===")
for key, (w, c) in FUNDS.items():
    pe_now = 17.92*M.R_W if w == "W" else 18.93*M.R_C
    for lab, f in [("Base = 6.9%", lambda o: o['Base']['irr']-0.069), ("E/R = 0.196", lambda o: M.er(o)[2]-0.196),
                   ("E/R = 0.291", lambda o: M.er(o)[2]-0.291), ("Base = 12%", lambda o: o['Base']['irr']-0.12)]:
        m = solve(lambda x: f(M.run(w, cost=c, dp=x)[0])); o, _, _ = M.run(w, cost=c, dp=m)
        print(f" {key} {lab:12s} {m*100:6.1f}% -> NAV {NAV[w]*(1+m):7.1f}; fwd P/E {pe_now*(1+m):.1f} | Base {o['Base']['irr']*100:.1f} E/R {M.er(o)[2]:.3f}")

print("\n=== Return split and paths ===")
for w, c in (("C", 0.0019), ("W", 0.0025)):
    o, d, bl = M.run(w, cost=c); P0 = 100*(M.R_C if w == "C" else M.R_W); E00 = M.E0C if w == "C" else M.E0
    for s in SC:
        E = d[s]["eps"]
        # value at year-ends before FX/cost: rebuild
        parts = []
        for n, x in bl.items(): parts.append(M.vals(n, x, s)[0])
        if w == "W": V = [(M.W_PE[s][k])*M.E0*M.W_EPS[s][k+1] for k in range(3)]
        else:
            R = M.world_rest(s); rr = d[s]["REST"]
            V = [sum(p[k] for p in parts)+R["pepath"][k]*rr["pm"]*rr["e"]*R["eps"][k+1] for k in range(3)]
        print(f" {w} {s}: EPS rel {[round(x/E00, 3) for x in E]} V/EPS(next) {[round(V[k]/E[k+1], 2) for k in range(3)]} | EPS g {((E[3]/E00)**(1/M.T)-1)*100:.2f}"
              f" mult chg {((V[2]/E[3]/(P0/E00))**(1/M.T)-1)*100:.2f} FX {((M.FX[s][2])**(1/M.T)-1)*100:.2f} | d {o[s]['d']*100:.2f} g {o[s]['g']*100:.2f} c {(o[s]['irr']-o[s]['d']-o[s]['g'])*100:.2f} | P/E now {P0/E00:.2f}")
