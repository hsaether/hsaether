import sys, os, copy; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idxai4 as X
M = X.M; SC = X.SC
NAV = {"W": 867.98, "C": 230.31}
FUNDS = {"DNB_N": ("W", 0.0025), "DNB_P": ("W", 0.0021), "NGI": ("C", 0.0019)}


def line(lab, o):
    E, R, ER = X.er(o)
    print(f" {lab:56s} Bear {o['Bear']['irr']*100:6.2f} Base {o['Base']['irr']*100:5.2f} Bull {o['Bull']['irr']*100:5.2f} | 27 {o['Bear']['r'][0]*100:6.1f}/{o['Base']['r'][0]*100:5.1f}/{o['Bull']['r'][0]*100:5.1f} | E/R {ER:.3f} | MoS {o['Base']['Pk']/100-1:+.1%}")


print("=== Blocks alone, before cost, NOK ===")
for which in ("W", "C"):
    print("--", which)
    _, _, bl = X.run(which)
    groups = [(n, [n]) for n in bl]+[("AI layers + co", [n for n in bl if n != "EN"]), ("REST", ["REST"]), ("EN+REST", ["EN", "REST"])]
    for lab, sel in groups:
        o, _, _ = X.run(which, only=sel); line(lab, o)
    o, _, _ = X.run(which, only=["H1", "CN"]); line("H1 + CN (all compute)", o)

print("\n=== Funds after cost ===")
for key, (w, c) in FUNDS.items():
    o, d, _ = X.run(w, cost=c); E, R, ER = X.er(o); nav = NAV[w]
    print(f"\n{key}: E {E:.2f} R {R:.1f} E/R {ER:.3f}")
    for s in SC:
        x = o[s]
        print(f" {s}: IRR {x['irr']*100:.2f} | stub {x['stub']*100:.1f} r {[round(v*100, 1) for v in x['r']]} | NAV {[round(nav*v/100, 1) for v in x['lv']]}"
              f" | Pk NAV {nav*x['Pk']/100:.1f} MoS {x['Pk']/100-1:+.1%} | kept {(x['sumD']+x['VT'])/100-1:+.1%} | sumD {x['sumD']:.1f} VT {x['VT']:.1f}"
              f" | 1m end-29 {1000*x['lv'][3]/100:.0f}k, 2027 chg {1000*(x['lv'][1]-x['lv'][0])/100:+.0f}k | d {x['d']*100:.2f} g {x['g']*100:.2f} c {(x['irr']-x['d']-x['g'])*100:.2f}"
              f" | EPS {[round(v, 3) for v in d[s]['eps']]} vm {[round(v, 2) for v in d[s]['vm']]}")
    print(" share of Bull priced", round((100-o['Base']['Pk'])/(o['Bull']['Pk']-o['Base']['Pk'])*100))
    if w == "W":
        print(" EPS growth (normalised, ann.)", [round(((d[s]['eps'][3])**(1/X.T)-1)*100, 2) for s in SC],
              " mult chg", [round(((d[s]['vm'][2]/(d[s]['P0']/d[s]['E00']))**(1/X.T)-1)*100, 2) for s in SC])
    else:
        print(" EPS growth (normalised, ann.)", [round(((d[s]['eps'][3])**(1/X.T)-1)*100, 2) for s in SC],
              " mult chg", [round(((d[s]['vm'][2]/(d[s]['P0']/d[s]['E00']))**(1/X.T)-1)*100, 2) for s in SC], "P/E now", round(d['Base']['P0']/d['Base']['E00'], 2))
print(" FX ann.", [round((X.FXMIX[s][2]**(1/X.T)-1)*100, 2) for s in SC])

print("\n=== Stress, after cost ===")
for key, (w, c) in FUNDS.items():
    ob, _, _ = X.run(w, cost=c, ai_only="Bear"); ou, _, _ = X.run(w, cost=c, ai_only="Bull")
    print(f" {key}: AI-only Bear {ob['Bear']['irr']*100:.2f} (2027 {ob['Bear']['r'][0]*100:.1f}) | AI-only Bull {ou['Bull']['irr']*100:.2f} (2027 {ou['Bull']['r'][0]*100:.1f})")

print("\n=== Attribution from the 17 Oct version (after cost) ===")
import idxai3 as OLD
def att(lab, fn):
    for key in ("DNB_N", "NGI"):
        w, c = FUNDS[key]; o = fn(w, c); line(f"{lab} [{key}]", o)
EN_NEW = M.EN
EN_OLD = (dict(Bear=tuple((x-30)/49 for x in (65, 60, 60, 60)), Base=tuple((x-30)/49 for x in (85, 77, 72, 70)),
               Bull=tuple((x-30)/49 for x in (85, 77, 72, 70))), (11, 12, 13), .55)
FX_OLD = {"Bear": [10.70/9.5555, 10.42/9.5555, 10.42/9.5555], "Base": [1, 1, 1], "Bull": [9.27/9.5555]*3}
M.EN = EN_OLD; M.FX = FX_OLD
att("0 17 Oct model (implied rest)", lambda w, c: OLD.run(w, cost=c)[0])
X.FXMIX = FX_OLD
att("1 + explicit rest (Equity BBB)", lambda w, c: X.run(w, cost=c)[0])
M.EN = (dict(Bear=EN_OLD[0]["Bear"], Base=EN_NEW[0]["Base"], Bull=EN_NEW[0]["Bull"]), EN_OLD[1], .55)
att("2 + Brent Base 2027 88", lambda w, c: X.run(w, cost=c)[0])
M.EN = EN_NEW
att("3 + energy payout 0.76", lambda w, c: X.run(w, cost=c)[0])
X.FXMIX = {s: [X.USD_SH*u+(1-X.USD_SH)*i for u, i in zip(X.USDP[s], X.I44P[s])] for s in SC}; M.FX = dict(X.FXMIX)
att("4 + 70% USD/NOK, 30% I-44 (= model)", lambda w, c: X.run(w, cost=c)[0])

print("\n=== Sensitivities ===")
REST_ALT = lambda g: dict(X.REST_EPS, Base=[.97*g**k for k in range(4)])
for key, w, c in [("NGI", "C", 0.0019), ("DNB_N", "W", 0.0025)]:
    print("--", key)
    cases = [("model", {}), ("exit P/E -1 (all blocks and rest)", dict(pex_shift=-1)), ("exit P/E +1", dict(pex_shift=1)),
             ("CY27 consensus -5%", dict(em=0.95)), ("rest growth 4.5%", dict(rest=REST_ALT(1.045))), ("rest growth 6.5%", dict(rest=REST_ALT(1.065))),
             ("NOK 10% weaker by 2029", dict(fx=dict(X.FXMIX, Base=[1.033, 1.067, 1.10]))), ("NOK 10% stronger by 2029", dict(fx=dict(X.FXMIX, Base=[0.967, 0.933, 0.90])))]
    if w == "C":
        cases += [("rest premium halves", dict(prem_mode="half")), ("rest premium gone", dict(prem_mode="gone")), ("tail x0.7", dict(tail=0.7)),
                  ("tail x1.3", dict(tail=1.3)), ("MSFT+GOOGL on E layer", dict(co_layer=("CM", "CG"))), ("NVDA on H1 layer", dict(co_layer=("CN",)))]
    for lab, kw in cases:
        o, _, _ = X.run(w, cost=c, **kw); line(lab, o)
    if w == "C":
        for lab, cc in [("hidden swap drag +0.20 (cost 0.39)", 0.0039), ("cost 0.25", 0.0025)]:
            o, _, _ = X.run(w, cost=cc); line(lab, o)
        M.PEX_OVR = {("H2", "Bear"): 4.8}; o, _, _ = X.run(w, cost=c); line("memory-stressed Bear (exit 4.8x)", o); M.PEX_OVR = {}


def solve(fn, lo=-0.6, hi=0.4):
    for _ in range(70):
        m = (lo+hi)/2
        if fn(m) > 0: lo = m
        else: hi = m
    return m


print("\n=== Triggers (NAV change from 15 Oct at unchanged earnings) ===")
for key, (w, c) in FUNDS.items():
    pe_now = 17.92*208.11/206.23 if w == "W" else 18.93*208.11/206.23*X.R_C/M.R_W
    for lab, f in [("Base = 6.2% (HY mkt after fee)", lambda o: o["Base"]["irr"]-0.062), ("Base = 6.8% (HY mkt gross)", lambda o: o["Base"]["irr"]-0.068), ("E/R = 0.196", lambda o: X.er(o)[2]-0.196),
                   ("Base = 12%", lambda o: o['Base']['irr']-0.12)]:
        m = solve(lambda x: f(X.run(w, cost=c, dp=x)[0])); o, _, _ = X.run(w, cost=c, dp=m)
        print(f" {key} {lab:30s} {m*100:6.1f}% -> NAV {NAV[w]*(1+m):7.1f}; fwd P/E {pe_now*(1+m):.1f} | Base {o['Base']['irr']*100:.1f} E/R {X.er(o)[2]:.3f}")
print(" fwd P/E now (MSCI basis, 30 Sep x URTH move): World", round(17.92*208.11/206.23, 2), " CC", round(18.93*208.11/206.23*X.R_C/M.R_W, 2))
print(" index level of the World trigger vs the Equity BBB (16 Oct, -14.1%): from 15 Oct URTH", round((206.34*(1-0.141))/208.11-1, 4))
