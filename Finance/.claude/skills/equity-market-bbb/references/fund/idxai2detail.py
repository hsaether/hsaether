import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idxai2 as M
SC = M.SC
NAV = {"W": 870.97, "C": 230.85}   # 14 Oct 2026 NAVs (DNB AM; Nordnet)
FUNDS = {"DNB_N": ("W", 0.0025), "DNB_P": ("W", 0.0021), "NGI": ("C", 0.0019)}


def line(lab, o):
    E, R, ER = M.er(o)
    print(f" {lab:46s} Bear {o['Bear']['irr']*100:6.2f} Base {o['Base']['irr']*100:5.2f} Bull {o['Bull']['irr']*100:5.2f} | 27 {o['Bear']['r'][0]*100:6.1f}/{o['Base']['r'][0]*100:5.1f}/{o['Bull']['r'][0]*100:5.1f} | E/R {ER:.3f} | MoS {o['Base']['Pk']/100-1:+.1%}")


print("=== Blocks alone, before cost, NOK ===")
for which in ("W", "C"):
    print("--", which)
    _, _, bl = M.run(which)
    groups = [(n, [n]) for n in bl]+[("AI layers + co", [n for n in bl if n != "EN"]), ("REST", ["REST"]), ("EN+REST", ["EN", "REST"])]
    for lab, sel in groups:
        o, _, _ = M.run(which, only=sel); line(lab, o)
    o, _, _ = M.run(which, only=["CM", "CG"], co_as_layer=True); line("CM+CG on the E layer path", o)
    o, _, _ = M.run(which, only=["CM", "CG"]); line("CM+CG on company paths", o)

print("\n=== Funds after cost ===")
for key, (w, c) in FUNDS.items():
    o, d, _ = M.run(w, cost=c); E, R, ER = M.er(o); nav = NAV[w]
    print(f"\n{key}: E {E:.2f} R {R:.1f} E/R {ER:.3f}")
    for s in SC:
        x = o[s]; cum = [(x['lv'][i]/100)**(1/(M.STUB+i))-1 for i in range(1, 4)]
        print(f" {s}: IRR {x['irr']*100:.2f} | stub {x['stub']*100:.1f} r {[round(v*100, 1) for v in x['r']]} | NAV {[round(nav*v/100, 1) for v in x['lv']]} | IRR to YE {[round(v*100, 1) for v in cum]}"
              f" | Pk NAV {nav*x['Pk']/100:.1f} MoS {x['Pk']/100-1:+.1%} | kept {(x['sumD']+x['VT'])/100-1:+.1%} | sumD {x['sumD']:.1f} VT {x['VT']:.1f}"
              f" | 920k end-29 {920*x['lv'][3]/100:.0f}k, 2027 chg {920*(x['lv'][1]-x['lv'][0])/100:+.0f}k | 508k end-29 {508*x['lv'][3]/100:.0f}k, 2027 chg {508*(x['lv'][1]-x['lv'][0])/100:+.0f}k | d {x['d']*100:.2f} g {x['g']*100:.2f}")
    print(" share of Bull priced", round((100-o['Base']['Pk'])/(o['Bull']['Pk']-o['Base']['Pk'])*100))

print("\n=== Stress and checks, after cost ===")
for key, (w, c) in FUNDS.items():
    ob, _, _ = M.run(w, cost=c, ai_only="Bear"); ou, _, _ = M.run(w, cost=c, ai_only="Bull"); ot, _, _ = M.run(w, cost=c, rest_trend=True)
    ol, _, _ = M.run(w, cost=c, co_as_layer=True)
    print(f" {key}: AI-only Bear {ob['Bear']['irr']*100:.2f} (2027 {ob['Bear']['r'][0]*100:.1f}) | AI-only Bull {ou['Bull']['irr']*100:.2f} (2027 {ou['Bull']['r'][0]*100:.1f})"
          f" | rest at trend: Base {ot['Base']['irr']*100:.2f} E/R {M.er(ot)[2]:.3f} | MSFT+GOOGL on E layer: Base {ol['Base']['irr']*100:.2f} Bear {ol['Bear']['irr']*100:.2f} E/R {M.er(ol)[2]:.3f}")
o, _, _ = M.run("W", rest_trend=True); print(" World before cost, rest at trend:", round(o['Base']['irr']*100, 2))
R = M.world_rest("Base"); print(" implied rest EPS growth 2027->2030n", round(((R['eps'][3]/R['eps'][0])**(1/3)-1)*100, 2), "%/yr; from consensus", round((R['eps'][3]**(1/3)-1)*100, 2))
for s in SC:
    ai = [n for n in M.WB if n != "EN"]
    e0 = sum(M.WB[n]["e"] for n in ai)
    path = [sum(M.vals(n, M.WB[n], s)[3][k] for n in ai)/e0 for k in range(4)]
    print(f" World AI+co EPS {s}: {[round(v, 3) for v in path]}")

print("\n=== Sensitivities ===")
for key, w, c in [("NGI", "C", 0.0019), ("DNB_N", "W", 0.0025)]:
    print("--", key)
    cases = [("model", {}), ("exit P/E -1", dict(pex_shift=-1)), ("exit P/E +1", dict(pex_shift=1)), ("CY27 consensus -5%", dict(em=0.95))]
    if w == "C":
        cases += [("rest premium halves", dict(prem_mode="half")), ("rest premium gone", dict(prem_mode="gone")), ("tail x0.7", dict(tail=0.7)),
                  ("tail x1.3", dict(tail=1.3)), ("MSFT+GOOGL on E layer", dict(co_as_layer=True))]
    for lab, kw in cases:
        o, _, _ = M.run(w, cost=c, **kw); line(lab, o)
    if w == "C":
        for lab, cc in [("hidden swap drag +0.20 (cost 0.39)", 0.0039), ("cost 0.25", 0.0025)]:
            o, _, _ = M.run(w, cost=cc); line(lab, o)


def solve(fn, lo=-0.6, hi=0.4):
    for _ in range(70):
        m = (lo+hi)/2
        if fn(m) > 0: lo = m
        else: hi = m
    return m


print("\n=== Triggers (NAV change from 14 Oct at unchanged earnings) ===")
for key, (w, c) in FUNDS.items():
    pe_now = 17.92*M.R_W if w == "W" else 18.93*M.R_C
    for lab, f in [("Base = 6.9%", lambda o: o['Base']['irr']-0.069), ("E/R = 0.196", lambda o: M.er(o)[2]-0.196),
                   ("E/R = 0.291", lambda o: M.er(o)[2]-0.291), ("Base = 12%", lambda o: o['Base']['irr']-0.12)]:
        m = solve(lambda x: f(M.run(w, cost=c, dp=x)[0])); o, _, _ = M.run(w, cost=c, dp=m)
        print(f" {key} {lab:12s} {m*100:6.1f}% -> NAV {NAV[w]*(1+m):7.1f}; fwd P/E {pe_now*(1+m):.1f} | Base {o['Base']['irr']*100:.1f} E/R {M.er(o)[2]:.3f}")

print("\n=== Return split (EPS growth, re-rating) ===")
o, d, bl = M.run("C", cost=0.0019)
for s in SC:
    R = M.world_rest(s)
    v_r = 100*M.R_C-sum(x["v"] for x in bl.values()); e_r = M.E0C-sum(x["e"] for x in bl.values())
    prem = (v_r/e_r)/M.world_rest("Base")["pe"]; pm = prem if s != "Bear" else 1+(prem-1)/2
    E = [e_r*R["eps"][k] for k in range(4)]; V = [R["pepath"][k]*pm*e_r*R["eps"][k+1] for k in range(3)]
    for n, x in bl.items():
        v, dd, ds, ee = M.vals(n, x, s); V = [V[k]+v[k] for k in range(3)]; E = [E[k]+ee[k] for k in range(4)]
    print(f" CC {s}: EPS rel {[round(x/M.E0C, 3) for x in E]} fwd P/E {[round(V[k]/E[k+1], 2) for k in range(3)]} | EPS g {((E[3]/M.E0C)**(1/M.T)-1)*100:.2f} rerate {((V[2]/E[3]/(100*M.R_C/M.E0C))**(1/M.T)-1)*100:.2f} | d {o[s]['d']*100:.2f} g {o[s]['g']*100:.2f} c {(o[s]['irr']-o[s]['d']-o[s]['g'])*100:.2f}")
o, _, _ = M.run("W", cost=0.0025)
for s in SC:
    print(f" W {s}: EPS g {((M.W_EPS[s][3])**(1/M.T)-1)*100:.2f} rerate {((M.W_PE[s][2]/(M.W_PE27*M.R_W))**(1/M.T)-1)*100:.2f} | d {o[s]['d']*100:.2f} g {o[s]['g']*100:.2f} c {(o[s]['irr']-o[s]['d']-o[s]['g'])*100:.2f}")
