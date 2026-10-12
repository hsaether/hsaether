import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idxai as M, copy
SC = M.SC
NAV = {"W": 880.91, "C": 234.44}   # 9 Oct 2026 NAVs: DNB Global Indeks A (DNB AM), Nordnet Global Indeks (Nordnet)
COST = {"DNB_N": ("W", 0.0025), "DNB_P": ("W", 0.0021), "NGI": ("C", 0.0019)}


def subset(which, names, ai_only=None):
    """evaluate a set of blocks together (value = their weight), before cost"""
    wbl = M.blocks(M.WW)
    cbl, en_w = (wbl, M.W_EN) if which == "W" else (M.blocks(M.cc_w()), M.CC_EN)
    out = {}
    for s in SC:
        sb = s; srest = sfx = ("Base" if ai_only and s == ai_only else s)
        parts = []; w = 0
        for b in names:
            if b in cbl:
                x = cbl[b]; v, d, ds, _ = M.block_vals(b, x["e"], sb, x["pe"]); parts.append((v, d, ds)); w += x["w"]
            elif b == "EN":
                v, d, ds, _ = M.block_vals("EN", en_w/M.EN_PE, srest, M.EN_PE); parts.append((v, d, ds)); w += en_w
            elif b == "REST":
                R = M.world_rest(wbl, srest)
                if which == "W": parts.append((R["V"], R["D"], R["Dst"])); w += R["w"]
                else:
                    w_r = 100-sum(x["w"] for x in cbl.values())-en_w; e_r = 100/M.CC_PE27-sum(x["e"] for x in cbl.values())-en_w/M.EN_PE
                    pm = (w_r/e_r)/R["pe"]; pm = 1+(pm-1)/2 if srest == "Bear" else pm
                    rel = R["eps"]
                    parts.append(([R["pepath"][k]*pm*e_r*rel[k+1] for k in range(3)], [R["pay"][k]*e_r*rel[k] for k in range(3)], R["Dst"]/R["e"]*e_r)); w += w_r
        out[s] = M.evaluate(w, parts, sfx)
    return out


print("=== Blocks alone, before cost, NOK (World composition / CC composition) ===")
ALL_AI = ["E", "H1", "H2", "H3", "H4", "T"]
for which in ("W", "C"):
    print("--", which)
    for nm, names in [(b, [b]) for b in ALL_AI]+[("AI all", ALL_AI), ("Energy", ["EN"]), ("Rest", ["REST"]), ("Non-AI (EN+REST)", ["EN", "REST"])]:
        o = subset(which, names)
        print(f" {nm:18s} IRR {o['Bear']['irr']*100:6.1f} / {o['Base']['irr']*100:5.1f} / {o['Bull']['irr']*100:5.1f} | 2027 {o['Bear']['r'][0]*100:6.1f} / {o['Base']['r'][0]*100:5.1f} / {o['Bull']['r'][0]*100:5.1f}")

print("\n=== Funds after cost ===")
res = {}
for key, (which, cost) in COST.items():
    o, d = M.run_index(which, cost=cost); E, R, ER = M.er(o); res[key] = o
    nav = NAV[which]
    print(f"\n{key}: E {E:.2f} R {R:.1f} E/R {ER:.3f}")
    for s in SC:
        x = o[s]
        cum = [(x['lv'][i]/100)**(1/(M.STUB+i))-1 for i in range(1, 4)]
        print(f" {s}: IRR {x['irr']*100:.2f} | stub {x['stub']*100:.1f} r {[round(v*100, 1) for v in x['r']]} | NAV {[round(nav*v/100, 1) for v in x['lv']]} | IRR to YE {[round(v*100, 1) for v in cum]}"
              f" | Pk NAV {nav*x['Pk']/100:.1f} MoS {x['Pk']/100-1:+.1%} | kept {(x['sumD']+x['VT'])/100-1:+.1%} | 508k end-29 {508*x['lv'][3]/100:.0f}k, 2027 chg {508*(x['lv'][1]-x['lv'][0])/100:+.0f}k | d {x['d']*100:.2f} g {x['g']*100:.2f}")

print("\n=== AI-only stress (AI blocks on Bear or Bull; energy, rest and NOK on Base), after cost ===")
for key, (which, cost) in COST.items():
    ob, _ = M.run_index(which, cost=cost, ai_only="Bear"); ou, _ = M.run_index(which, cost=cost, ai_only="Bull")
    print(f" {key}: AI-only Bear IRR {ob['Bear']['irr']*100:.2f} (2027 {ob['Bear']['r'][0]*100:.1f}) | AI-only Bull IRR {ou['Bull']['irr']*100:.2f} (2027 {ou['Bull']['r'][0]*100:.1f})")

print("\n=== Sensitivities, Nordnet GI (0.19%) ===")
def line(lab, o):
    E, R, ER = M.er(o)
    print(f" {lab:48s} Bear {o['Bear']['irr']*100:5.2f} Base {o['Base']['irr']*100:5.2f} Bull {o['Bull']['irr']*100:5.2f} | 27 {o['Bear']['r'][0]*100:6.1f}/{o['Base']['r'][0]*100:5.1f} | E/R {ER:.3f} | MoS {o['Base']['Pk']/100-1:+.1%}")
for lab, kw in [("model", {}), ("rest premium halves", dict(prem_mode="half")), ("rest premium gone", dict(prem_mode="gone")),
                ("CC tail weights x0.7", dict(tail=0.7)), ("CC tail weights x1.3", dict(tail=1.3)),
                ("exit P/E -1 (all blocks)", dict(pex_shift=-1)), ("exit P/E +1", dict(pex_shift=1)),
                ("cost 0.39% (hidden swap drag 0.20)", dict(cost=0.0039)), ("cost 0.25%", dict(cost=0.0025))]:
    kw2 = dict(cost=0.0019); kw2.update(kw); o, _ = M.run_index("C", **kw2); line(lab, o)
print("=== DNB GI on Nordnet (0.25%) ===")
for lab, kw in [("model", {}), ("exit P/E -1", dict(pex_shift=-1)), ("exit P/E +1", dict(pex_shift=1))]:
    kw2 = dict(cost=0.0025); kw2.update(kw); o, _ = M.run_index("W", **kw2); line(lab, o)

# rest at trend growth instead of the implied path (check for the Equity BBB): rest EPS 0.97 x 1.055^n, implied P/E path kept
print("\n=== Check: rest of World at trend growth (0.97 then +5.5% a year) ===")
orig = M.world_rest
def rest_trend(wbl, s, pex_shift=0.0):
    R = orig(wbl, s, pex_shift)
    if s != "Base": return R
    rel = [0.97*1.055**k for k in range(4)]
    e_r = R["e"]
    R2 = dict(R); R2["eps"] = rel
    R2["V"] = [R["pepath"][k]*e_r*rel[k+1] for k in range(3)]; R2["D"] = [R["pay"][k]*e_r*rel[k] for k in range(3)]
    return R2
M.world_rest = rest_trend
for key, (which, cost) in COST.items():
    o, _ = M.run_index(which, cost=cost); print(f" {key}: Base {o['Base']['irr']*100:.2f}  2027 {o['Base']['r'][0]*100:.1f}  E/R {M.er(o)[2]:.3f}")
o, _ = M.run_index("W"); print(f" World before cost: Base {o['Base']['irr']*100:.2f}")
M.world_rest = orig
wbl = M.blocks(M.WW)
R = M.world_rest(wbl, "Base"); print(" implied rest EPS growth 2027->2030n", round(((R['eps'][3]/R['eps'][0])**(1/3)-1)*100, 2), "%/yr; from consensus", round((R['eps'][3]**(1/3)-1)*100, 2))
# AI earnings path in World (weighted)
E0 = 100/M.W_PE27
for s in SC:
    ai = [sum(wbl[b]["e"]*M.AI[b][0][s][k] for b in wbl)/sum(wbl[b]["e"] for b in wbl) for k in range(4)]
    print(f" World AI block EPS {s}: {[round(v, 3) for v in ai]}")

# triggers (NAV change at unchanged earnings) for Nordnet GI with the new model
def solve(fn, lo=-0.6, hi=0.4):
    for _ in range(70):
        m = (lo+hi)/2
        if fn(m) > 0: lo = m
        else: hi = m
    return m
print("\n=== Triggers, Nordnet GI (new model) ===")
for lab, f in [("Base = 6.9%", lambda o: o['Base']['irr']-0.069), ("E/R = 0.196", lambda o: M.er(o)[2]-0.196),
               ("E/R = 0.291", lambda o: M.er(o)[2]-0.291), ("Base = 12%", lambda o: o['Base']['irr']-0.12)]:
    m = solve(lambda x: f(M.run_index("C", cost=0.0019, P0=100*(1+x))[0]))
    o, _ = M.run_index("C", cost=0.0019, P0=100*(1+m))
    print(f" {lab:14s} {m*100:6.1f}% -> NAV {NAV['C']*(1+m):.1f}; fwd P/E {18.93*(1+m):.1f} | Base {o['Base']['irr']*100:.1f} E/R {M.er(o)[2]:.3f}")
# return split Nordnet Base
o, _ = M.run_index("C", cost=0.0019); x = o["Base"]
print("\nNGI Base split: IRR %.2f d %.2f g %.2f c %.2f sumD %.1f VT %.1f" % (x['irr']*100, x['d']*100, x['g']*100, (x['irr']-x['d']-x['g'])*100, x['sumD'], x['VT']))
for s in SC:
    x = o[s]; print(f" NGI {s}: d {x['d']*100:.2f} g {x['g']*100:.2f} c {(x['irr']-x['d']-x['g'])*100:.2f} sumD {x['sumD']:.1f} VT {x['VT']:.1f}")
