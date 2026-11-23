# docs/global-index-funds-analysis.md v7 (21 Nov 2026; iaf-valuation 2026-11-18.1). DNB Global Indeks A only (Nordnet Global
# Indeks dropped, user 1 Nov). DNB GI A = MSCI World on the Equity BBB World build of the 20 Nov leading-view note
# (equity-market-bbb/references/world3.py, not changed: company blocks MSFT, GOOGL, NVDA, AMZN, MU + AI layer blocks + energy +
# explicit rest), re-priced to the NAV date (19 Nov close, NAV 835.76) and run after the fund's all-in cost.
# Changes to world3's inputs here: GOOGL v2.3 (20 Nov: V_t at $265.29 with the SpaceX and Anthropic closes of 20 Nov); NVIDIA Bull
# interim V_t as v2.0 (241.0 / 319.5). Everything else as world3 (AI BBB 18 Nov rows, oil BBB 18 Nov, HY BBB 18 Nov NIBOR).
# Run from this folder: py gidx7.py            (prints all tables; writes gidx7_results.json here)
import sys, os, types, json, math
HERE = os.path.dirname(os.path.abspath(__file__))
EQ = os.path.normpath(os.path.join(HERE, "..", "..", "..", "..", "equity-market-bbb", "references"))
os.chdir(EQ); sys.path.insert(0, EQ)
NAV19 = 835.76            # DNB Global Indeks A, NAV 19 Nov 2026 (Nordnet fund page, "Siste NAV-kurs (19. nov.)") [F]
NAV18 = 846.23            # NAV 18 Nov 2026 (dnbam.com) [F]
COST = {"nordnet": 0.0025, "pension": 0.0021}
HY_REF = 0.254; HY_BASE = 0.075; HY_FEE = 0.006


def load_world(date):
    src = open("world3.py", encoding="utf-8").read()
    old = "EU5 = 1.0974539518356323; D20 = '2026-11-20'"
    assert old in src
    src = src.replace(old, f"D20 = '{date}'; EU5 = RC20['EURUSD=X'][D20]")
    mod = types.ModuleType("w3_" + date.replace("-", "")); mod.__file__ = os.path.join(EQ, "world3.py")
    exec(compile(src, mod.__file__, "exec"), mod.__dict__)
    mod.CO_SRC["CG"].update(p_an=265.29, V=dict(Bear=(159.9, 178.9, 202.4), Base=(295.8, 331.9, 371.6), Bull=(360.5, 432.7, 517.0)))
    mod.CO_SRC["CN"]["V"]["Bull"] = (241.0, 319.5, 392.6)
    return mod


W19 = load_world("2026-11-19"); W20 = load_world("2026-11-20")
M = W19.M; SC = M.SC; K = 0.12
CN_BASE = dict(V=tuple(W19.CO_SRC["CN"]["V"]["Base"]), D=tuple(W19.CO_SRC["CN"]["D"]["Base"]))
H1_BASE = M.AI["H1"]


def run_mix(W, ai="Base", en="Base", reps="Base", repe="Base", fx="Base", cost=0.0, dp=0.0, pex_shift=0.0, vm=1.0, rest=None,
            e_r=None, fxp=None, only=None):
    """one synthetic scenario: AI and company blocks on `ai`, energy on `en`, rest EPS on `reps`, rest P/E on `repe`, NOK on `fx`"""
    rest = rest or W.REST_EPS; WB = W.build(W.ALL_CO); P0 = 100.0
    v_r = P0-sum(x["v"] for x in WB.values()); e_r = e_r or W.E_R; E0 = e_r+sum(x["e"] for x in WB.values())
    parts = {}
    for n, x in WB.items():
        parts[n] = M.vals(n, x, en if n == "EN" else ai, pex_shift)
    eps = rest[reps]
    parts["REST"] = ([(W.REST_PE[repe][k]+pex_shift)*e_r*eps[k+1] for k in range(3)], [W.REST_PAY[reps][k]*e_r*eps[k] for k in range(3)],
                     0.025*v_r*W.STUB, [e_r*v for v in eps])
    fxs = (fxp or W.FXMIX)[fx]
    M.FX = {"X": fxs}
    if only:
        sel = [parts[n] for n in only]; vv = sum(WB[n]["v"] if n != "REST" else v_r for n in only)
        o = M.evaluate(vv, [([vm*v for v in p[0]], p[1], p[2]) for p in sel], "X", cost)
    else:
        o = M.evaluate(P0*(1+dp), [([vm*v for v in p[0]], p[1], p[2]) for p in parts.values()], "X", cost)
    M.FX = dict(W.FXMIX)
    E = [sum(p[3][k] for p in parts.values()) for k in range(4)]; V = [vm*sum(p[0][k] for p in parts.values()) for k in range(3)]
    D = [sum(p[1][k] for p in parts.values()) for k in range(3)]; Dst = sum(p[2] for p in parts.values())
    o["eps"] = [x/E0 for x in E]; o["vmul"] = [V[k]/E[k+1] for k in range(3)]; o["E0"] = E0; o["P0"] = P0
    o["V"] = V; o["D"] = D; o["Dst"] = Dst; o["E"] = E; o["c"] = o["irr"]-o["d"]-o["g"]
    return o


def scen(W, s, spot=False, **kw):
    return run_mix(W, ai=s, en=s, reps=s, repe=s, fx="Base" if spot else s, **kw)


def trio(W, spot=False, **kw):
    return {s: scen(W, s, spot, **kw) for s in SC}


def er(o):
    E = (o["Base"]["irr"]-W19.NIBW)*100; R = (o["Base"]["r"][0]-o["Bear"]["r"][0])*100; return E, R, E/R


def solve(fn, tgt, lo=-0.6, hi=0.6, increasing=False):
    """bisection; fn falls in m by default (price change), set increasing=True for value scalars and growth rates"""
    for _ in range(80):
        m = (lo+hi)/2
        if (fn(m) > tgt) != increasing: lo = m
        else: hi = m
    return m


def nvda_scale(target):
    """factor on NVIDIA's Base V_t and D_t so that its own IRR at $125.53 (USD) equals target [A]"""
    st = W19.STUB; T = W19.T; d = W19.CO_SRC["CN"]
    def irr_f(f):
        fl = [(0, -125.53), (st, d["stub"])]+[(st+k+0.5, f*CN_BASE["D"][k]) for k in range(3)]+[(T, f*CN_BASE["V"][2])]
        return M.irr(fl)
    lo, hi = 0.2, 1.5
    for _ in range(80):
        m = (lo+hi)/2
        if irr_f(m) > target: hi = m
        else: lo = m
    return m, irr_f(1.0)


def set_nvda(f):
    for W in (W19, W20):
        W.CO_SRC["CN"]["V"]["Base"] = tuple(f*v for v in CN_BASE["V"]); W.CO_SRC["CN"]["D"]["Base"] = tuple(f*v for v in CN_BASE["D"])


def set_h1_cut(on):
    b = H1_BASE[0]["Base"]
    M.AI["H1"] = (dict(H1_BASE[0], Base=(b[0],)+tuple(round(x*0.9, 4) for x in b[1:])) if on else H1_BASE[0],)+tuple(H1_BASE[1:])


def line(o, nav=NAV19):
    return dict(irr=o["irr"]*100, r=[x*100 for x in o["r"]], stub=o["stub"]*100, VT=o["VT"], sumD=o["sumD"], Pk=o["Pk"],
                PkNAV=nav*o["Pk"]/100, MoS=o["Pk"]/100-1, kept=(o["sumD"]+o["VT"])/100-1, navs=[nav*x/100 for x in o["lv"]],
                d=o["d"]*100, g=o["g"]*100, c=o["c"]*100, eps=o["eps"], vmul=o["vmul"])


R = {}
if __name__ == "__main__":
    W = W19; WB = W.build(W.ALL_CO); E0 = W.E_R+sum(x["e"] for x in WB.values()); v_r = 100-sum(x["v"] for x in WB.values())
    print(f"NAV date 19 Nov: URTH {W.RC20['URTH'][W.D20]:.2f} USD/NOK {W.RC20['NOK=X'][W.D20]:.4f} EUR/USD {W.EU5:.4f}; stub {W.STUB*365:.0f} d, "
          f"T {W.T:.3f}, NIBOR window {W.NIBW*100:.2f}; P/E on CY27 {100/E0:.2f}; MSCI fwd {W.FPE0:.2f}; P/B {W.PB0:.2f}")
    print(f" rest value {v_r:.1f}% earnings {W.E_R/E0*100:.1f}% P/E {v_r/W.E_R:.2f}")
    blk = {}
    for n, x in WB.items():
        print(f"  {n:3s} v {x['v']:6.2f}  e% {x['e']/E0*100:5.1f}  P/E {x['pe']:6.2f}"); blk[n] = dict(v=x["v"], e=x["e"]/E0*100, pe=x["pe"])
    co = [n for n in WB if WB[n]["kind"] == "co"]; ly = [n for n in WB if WB[n]["kind"] == "layer"]
    for lab, g in [("companies", co), ("layers", ly), ("AI+co", co+ly)]:
        v = sum(WB[n]["v"] for n in g); e = sum(WB[n]["e"] for n in g); print(f"  {lab}: value {v:.1f}%, earnings {e/E0*100:.1f}%, P/E {v/e:.1f}")
    R["blocks"] = blk
    # --- check: World at 20 Nov, no cost = Equity BBB world3 (GOOGL v2.3 and NVIDIA Bull interim moved) ---
    for lab, Wx in (("19 Nov", W19), ("20 Nov", W20)):
        o = trio(Wx); E, Rr, ER = er(o)
        print(f"World {lab} no cost (NOK path): {[round(o[s]['irr']*100, 2) for s in SC]} 27 {[round(o[s]['r'][0]*100, 1) for s in SC]} "
              f"E-0.2 {E-0.2:.2f} R {Rr:.1f} E/R(0.2 fee) {(E-0.2)/Rr:.3f}  Base Pk {o['Base']['Pk']:.1f}")
        R["world_"+lab] = {s: line(o[s]) for s in SC}; R["world_"+lab]["ER_fee20"] = (E-0.2)/Rr
    # --- fund results ---
    for plat, c in COST.items():
        for basis, spot in (("nok", False), ("spot", True)):
            o = trio(W19, spot, cost=c); E, Rr, ER = er(trio(W19, False, cost=c))
            R[f"{plat}_{basis}"] = {s: line(o[s]) for s in SC}
            print(f"\n{plat} {basis} cost {c}: " + " | ".join(f"{s} {o[s]['irr']*100:.2f} r {[round(x*100,1) for x in o[s]['r']]} stub {o[s]['stub']*100:.2f} "
                  f"VT {o[s]['VT']:.1f} sumD {o[s]['sumD']:.1f} Pk {o[s]['Pk']:.1f} ({NAV19*o[s]['Pk']/100:.0f}) MoS {o[s]['Pk']/100-1:+.1%} "
                  f"kept {(o[s]['sumD']+o[s]['VT'])/100-1:+.1%} NAVs {[round(NAV19*x/100) for x in o[s]['lv']]} d {o[s]['d']*100:.2f} g {o[s]['g']*100:.2f} c {o[s]['c']*100:.2f}"
                  for s in SC))
            if basis == "nok":
                R[f"{plat}_ER"] = dict(E=E, R=Rr, ER=ER); print(f"  E {E:.2f} R {Rr:.1f} E/R {ER:.3f}")
                for s in SC:
                    x = o[s]; T = W19.T
                    eg = x["eps"][3]**(1/T)-1; mg = (x["vmul"][2]/(100/x["E0"]))**(1/T)-1; fg = W19.FXMIX[s][2]**(1/T)-1; cg = (1-c)-1
                    print(f"   {s} split: d {x['d']*100:.2f} g {x['g']*100:.2f} = EPS {eg*100:.2f} multiple {mg*100:.2f} FX {fg*100:.2f} cost {cg*100:.2f}; c {x['c']*100:.2f};"
                          f" EPS {[round(v,3) for v in x['eps']]} vmul {[round(v,2) for v in x['vmul']]} payout {sum(x['D'])/sum(x['E'][:3]):.2f}")
                    R[f"{plat}_split_{s}"] = dict(eg=eg*100, mg=mg*100, fg=fg*100, cg=cg*100)
    oR = trio(W19, False, cost=0.0025); oS = trio(W19, True, cost=0.0025)
    print("\nR at spot (no krone cushion):", round((oS['Base']['r'][0]-oS['Bear']['r'][0])*100, 1), "E/R", round(er(oS)[0]/((oS['Base']['r'][0]-oS['Bear']['r'][0])*100), 3))
    # --- exit P/B (book rolled forward, Equity BBB method) ---
    for s in SC:
        x = oR[s]; eps = x["E"]; B = 100/W19.PB0+(x["E0"]/1.13)*W19.STUB-x["Dst"]
        for k in range(3): B += eps[k]-x["D"][k]
        print(f" exit P/B {s}: {x['V'][2]/B:.2f}  exit value multiple {x['vmul'][2]:.2f}")
    # --- 20 Nov indicative (NAV estimate) ---
    est = NAV19*(W20.RC20['URTH'][W20.D20]/W19.RC20['URTH'][W19.D20])*(W20.RC20['NOK=X'][W20.D20]/W19.RC20['NOK=X'][W19.D20])
    o20 = trio(W20, False, cost=0.0025); E, Rr, ER = er(o20)
    print(f"\n20 Nov indicative NAV {est:.1f}: Base {o20['Base']['irr']*100:.2f} Bear {o20['Bear']['irr']*100:.2f} Bull {o20['Bull']['irr']*100:.2f} "
          f"27 {[round(o20[s]['r'][0]*100,1) for s in SC]} Pk {o20['Base']['Pk']:.1f} -> NAV {est*o20['Base']['Pk']/100:.0f} MoS {o20['Base']['Pk']/100-1:+.1%} E/R {ER:.3f}")
    R["ind20"] = dict(nav=est, base=o20["Base"]["irr"]*100, bear=o20["Bear"]["irr"]*100, bull=o20["Bull"]["irr"]*100, PkNAV=est*o20["Base"]["Pk"]/100,
                      MoS=o20["Base"]["Pk"]/100-1, ER=ER, r27=[o20[s]["r"][0]*100 for s in SC])
    # --- AI-only stress and driver breakdown (cost 0.25%) ---
    print("\nDriver breakdown (cost 0.25%):")
    steps = [("Base", {}), ("AI + company blocks", dict(ai="X")), ("+ energy (oil)", dict(ai="X", en="X")),
             ("+ rest EPS", dict(ai="X", en="X", reps="X")), ("+ rest multiple (= spot FX)", dict(ai="X", en="X", reps="X", repe="X")),
             ("+ NOK path", dict(ai="X", en="X", reps="X", repe="X", fx="X"))]
    R["drivers"] = {}
    for s in ("Bear", "Bull"):
        for lab, kw in steps:
            kw2 = {k: (s if v == "X" else v) for k, v in kw.items()}
            o = run_mix(W19, cost=0.0025, **kw2)
            print(f"  {s} {lab:28s} IRR {o['irr']*100:6.2f}  2027 {o['r'][0]*100:6.1f}  Pk NAV {NAV19*o['Pk']/100:6.0f}")
            R["drivers"][f"{s}|{lab}"] = (o["irr"]*100, o["r"][0]*100, NAV19*o["Pk"]/100)
    # --- blocks alone (no cost, NOK path) ---
    print("\nBlocks alone (no cost, NOK path): Bear / Base / Bull, Bear 2027")
    R["alone"] = {}
    for n in list(WB.keys())+["REST"]:
        o = {s: scen(W19, s, only=[n]) for s in SC}
        print(f"  {n:4s} {o['Bear']['irr']*100:6.1f} / {o['Base']['irr']*100:5.1f} / {o['Bull']['irr']*100:5.1f}  Bear 2027 {o['Bear']['r'][0]*100:6.1f}")
        R["alone"][n] = [o[s]["irr"]*100 for s in SC]+[o["Bear"]["r"][0]*100]
    aico = [n for n in WB if n != "EN"]
    o = {s: scen(W19, s, only=aico) for s in SC}
    print(f"  AI+co {o['Bear']['irr']*100:6.1f} / {o['Base']['irr']*100:5.1f} / {o['Bull']['irr']*100:5.1f}  Bear 2027 {o['Bear']['r'][0]*100:6.1f} Base 2027 {o['Base']['r'][0]*100:.1f}")
    R["alone"]["AICO"] = [o[s]["irr"]*100 for s in SC]+[o["Bear"]["r"][0]*100]
    for s in ("Bear", "Bull"):
        oa = run_mix(W19, ai=s, cost=0.0025)
        print(f"  AI-only {s} (rest, energy, NOK on Base), cost 0.25%: IRR {oa['irr']*100:.2f} 2027 {oa['r'][0]*100:.1f}")
        R["aionly_"+s] = (oa["irr"]*100, oa["r"][0]*100)
    # --- sensitivities (cost 0.25%) ---
    print("\nSensitivities (cost 0.25%): Bear / Base / Bull (NOK path), Bear27 / Base27, E/R, MoS")
    R["sens"] = {}
    def sens(lab, **kw):
        o = trio(W19, False, cost=0.0025, **kw); E, Rr, ER = er(o)
        print(f"  {lab:46s} {o['Bear']['irr']*100:6.2f} {o['Base']['irr']*100:6.2f} {o['Bull']['irr']*100:6.2f} | {o['Bear']['r'][0]*100:6.1f} {o['Base']['r'][0]*100:5.1f} | {ER:6.3f} | {o['Base']['Pk']/100-1:+.1%}")
        R["sens"][lab] = (o["Bear"]["irr"]*100, o["Base"]["irr"]*100, o["Bull"]["irr"]*100, o["Bear"]["r"][0]*100, o["Base"]["r"][0]*100, ER, o["Base"]["Pk"]/100-1)
    sens("model")
    o = trio(W19, False, cost=0.0021); E, Rr, ER = er(o); R["sens"]["pension 0.21%"] = (o["Bear"]["irr"]*100, o["Base"]["irr"]*100, o["Bull"]["irr"]*100, o["Bear"]["r"][0]*100, o["Base"]["r"][0]*100, ER, o["Base"]["Pk"]/100-1)
    print(f"  {'pension 0.21%':46s} {o['Bear']['irr']*100:6.2f} {o['Base']['irr']*100:6.2f} {o['Bull']['irr']*100:6.2f} | {ER:.3f} | {o['Base']['Pk']/100-1:+.1%}")
    for sh in (-1, 1): sens(f"exit multiples {sh:+d}", pex_shift=sh)
    for m in (0.9, 1.1): sens(f"all values x{m}", vm=m)
    bvm = trio(W19, False, cost=0.0025)["Base"]["vmul"][2]
    sens(f"multiple watch: exit value multiple 15.4 (x{15.4/bvm:.3f})", vm=15.4/bvm)
    for lab, g in (("rest growth 4.5%", 1.045), ("rest growth 6.5%", 1.065)):
        rr = dict(W19.REST_EPS); rr["Base"] = [.97*g**k for k in range(4)]; sens(lab, rest=rr)
    sens("rest CY27 consensus -3%", e_r=W19.E_R*0.97)
    for lab, f in (("NOK -10% by 2029", [1.033, 1.067, 1.10]), ("NOK +10% by 2029", [0.967, 0.933, 0.90])):
        fx = dict(W19.FXMIX); fx["Base"] = f; sens(lab, fxp=fx)
    for dB in (-10, 10):
        W19.set_energy(dB=dB); sens(f"Brent {dB:+d}"); W19.set_energy()
    f_cut, chk = nvda_scale(0.167); f_wide, _ = nvda_scale(0.092)
    print(f"  NVIDIA own Base at $125.53 on these flows: {chk*100:.1f}% (analysis 20.7%); scale for 16.7% {f_cut:.3f}, for 9.2% {f_wide:.3f}")
    set_nvda(f_cut); set_h1_cut(True); sens("AI BBB order-cut watch (H1 2028-30 x0.9; NVIDIA 16.7%)")
    set_nvda(f_wide); sens("+ NVIDIA SEC probe wide (NVIDIA 9.2%)"); set_nvda(1.0); set_h1_cut(False)
    sens("check: back to model")
    # --- price-implied (Step 6b) and triggers ---
    vm_k = solve(lambda m: trio(W19, False, cost=0.0025, vm=1+m)["Base"]["irr"], 0.12, -0.5, 1.0, increasing=True)
    print(f"\nPrice-implied: Base = k needs all values x{1+vm_k:.3f}: exit value multiple {bvm*(1+vm_k):.1f} (Base {bvm:.1f})")
    def rest_g(g):
        rr = dict(W19.REST_EPS); rr["Base"] = [.97*(1+g)**k for k in range(4)]; return trio(W19, False, cost=0.0025, rest=rr)["Base"]["irr"]
    gk = solve(rest_g, 0.12, -0.2, 0.6, increasing=True)
    print(f"Price-implied: Base = k needs rest EPS growth {gk*100:.1f}% a year (Base 5.5%)")
    R["implied"] = dict(vm=1+vm_k, exit_mult=bvm*(1+vm_k), base_mult=bvm, rest_g=gk*100)
    R["trig"] = {}
    for plat, c in COST.items():
        for lab, fn, tgt in [("ER", lambda p: er(trio(W19, False, cost=c, dp=p))[2], HY_REF),
                             ("k", lambda p: trio(W19, False, cost=c, dp=p)["Base"]["irr"], K),
                             ("pre", lambda p: trio(W19, False, cost=c, dp=p)["Base"]["irr"], HY_BASE-HY_FEE),
                             ("hy75", lambda p: trio(W19, False, cost=c, dp=p)["Base"]["irr"], HY_BASE)]:
            p = solve(fn, tgt)
            print(f" trigger {plat} {lab}: dp {p*100:+.1f}% NAV {NAV19*(1+p):.0f} fwd P/E {W19.FPE0*(1+p):.1f}")
            R["trig"][f"{plat}_{lab}"] = (p*100, NAV19*(1+p), W19.FPE0*(1+p))
    # --- Base return bridge (NOK per NAV unit, Nordnet cost) and extra rows ---
    b = trio(W19, False, cost=0.0025)["Base"]; T = W19.T; P = NAV19
    fE = b["eps"][3]; fM = b["vmul"][2]/(100/b["E0"]); drag = (1-0.0025)**T
    s1 = P*(fE-1); s2 = P*fE*(fM-1); s3 = P*fE*fM*(drag-1); VT = P*fE*fM*drag; SD = P*b["sumD"]/100
    print(f"\nBridge: P {P:.2f} + EPS {s1:+.1f} + multiple {s2:+.1f} + cost on V_T {s3:+.1f} = V_T {VT:.1f} (model {P*b['VT']/100:.1f}); + dividends {SD:+.1f}"
          f" = {VT+SD:.1f}; accumulating NAV end-2029 {P*b['lv'][-1]/100:.1f}")
    R["bridge"] = dict(eps=s1, mult=s2, cost=s3, VT=VT, divs=SD, total=VT+SD, nav29=P*b["lv"][-1]/100, fE=fE, fM=fM)
    o = {s: scen(W19, s, only=["REST"]) for s in SC}
    print(f"Rest alone Base 2027 {o['Base']['r'][0]*100:.1f}, Bear 2027 {o['Bear']['r'][0]*100:.1f}; E {(o['Base']['irr']-W19.NIBW)*100:.2f}")
    o = {s: scen(W19, s, only=[n for n in WB if n != "EN"]) for s in SC}
    print(f"AI+co alone Base 2027 {o['Base']['r'][0]*100:.1f}; E {(o['Base']['irr']-W19.NIBW)*100:.2f}")
    json.dump(R, open(os.path.join(HERE, "gidx7_results.json"), "w"), indent=1, default=float)
