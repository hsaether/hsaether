# Global index funds, 17 Oct 2026 analysis (prices at the 15 Oct close = NAV date); AI BBB Update 2 (method v2)
# World = company blocks (MSFT, GOOGL, NVDA from their IAF analyses) + AI layer blocks (AI BBB v2 paths, retained cash
#         counted once through the cash conversion c) + energy (oil BBB) + rest, implied so that World equals the
#         Equity BBB World path exactly. TSMC is MSCI Emerging Markets: not in either index.
# Climate Change index = the same blocks at its own weights; its rest carries the non-AI tilt premium
# Switches for the attribution: RET (retained cash), BEAR_V1 (12 Oct Bear paths), CONS_V1 (uncalendarised consensus),
#                               CN_LAYER (NVIDIA on the H1 layer instead of its company block)
import json
RET = True; BEAR_V1 = False; CONS_V1 = False; CN_LAYER = False
STUB = 75/365; T = STUB+3; K = 0.12                # 17 Oct -> 31 Dec 2026
NIB = {"stub": 4.80, "2027": 4.79, "2028": 4.39, "2029": 3.86}
nibw = ((1+NIB["stub"]/100)**STUB*(1+NIB["2027"]/100)*(1+NIB["2028"]/100)*(1+NIB["2029"]/100))**(1/T)-1
SC = ["Bear", "Base", "Bull"]
FX = {"Bear": [10.70/9.5555, 10.42/9.5555, 10.42/9.5555], "Base": [1, 1, 1], "Bull": [9.27/9.5555]*3}   # relative to spot
# --- Equity BBB World (11 Oct baseline, unchanged); value 100 = 9 Oct close ---
W_EPS = {"Bear": [.75, .82, .90, .97], "Base": [.95, 1.0165, 1.0775, 1.137], "Bull": [1.00, 1.09, 1.17, 1.25]}
W_PE = {"Bear": [15.0, 15.0, 15.0], "Base": [17.6, 17.3, 17.0], "Bull": [18.2, 18.4, 18.5]}
W_PE27 = 17.3; W_PAY = 0.45; W_Y = 0.025; E0 = 100/W_PE27
NAV = {"W": (867.98, 880.91), "C": (230.31, 234.44)}      # 15 Oct / 9 Oct NAVs (DNB AM; Nordnet)
R_W = 208.11/209.14            # URTH 15 Oct / 9 Oct (USD): World price at unchanged earnings
R_C = R_W*(NAV["C"][0]/NAV["C"][1])/(NAV["W"][0]/NAV["W"][1])   # Climate Change: Nordnet NAV move relative to DNB's
# --- AI BBB layer paths (docs/ai-market-bbb.md Update 2, 17 Oct): EPS (CY27 cons = 1) 2027-30, exit P/E Bear/Base/Bull, payout
AI = {"E":  (dict(Bear=(.88, .88, .97, 1.05), Base=(.97, 1.07, 1.17, 1.27), Bull=(1.0, 1.13, 1.27, 1.41)), (17, 21, 23.5), .34),  # rest of E (AMZN, META, ORCL)
      "H1": (dict(Bear=(.68, .50, .53, .57), Base=(.92, .98, 1.00, .97), Bull=(1.0, 1.15, 1.25, 1.30)), (13, 17, 19), .25),
      "H2": (dict(Bear=(.60, .30, .25, .25), Base=(.90, .60, .40, .35), Bull=(1.0, .80, .55, .45)), (8, 10, 11), .15),
      "H3": (dict(Bear=(.76, .63, .67, .71), Base=(.95, 1.03, 1.10, 1.16), Bull=(1.0, 1.15, 1.28, 1.40)), (14, 18, 21), .45),
      "H4": (dict(Bear=(.75, .54, .56, .65), Base=(.95, 1.02, 1.07, 1.11), Bull=(1.0, 1.12, 1.22, 1.30)), (15, 20, 24), .35),
      "T":  (dict(Bear=(.88, .85, .93, 1.00), Base=(.95, 1.03, 1.11, 1.19), Bull=(1.0, 1.10, 1.20, 1.30)), (15, 20, 24), .45)}
BEAR1 = {"H1": (.70, .60, .70, .75), "H3": (.80, .75, .85, .92), "H4": (.75, .65, .75, .85)}   # 12 Oct Bears (method v1)
# cash conversion c 2027/28/29 (AI BBB v2): free cash after growth capex and dilution offsets / EPS
CONV = {"E":  dict(Bear=(.00, .40, .60), Base=(-.10, .10, .30), Bull=(-.20, -.10, .10)),
        "H1": dict(Bear=(.85, .95, .95), Base=(.80, .90, .90), Bull=(.75, .85, .90)),
        "H2": dict(Bear=(.70, .75, .70), Base=(.70, .65, .60), Bull=(.70, .70, .55)),
        "H3": dict(Bear=(.75, .90, .95), Base=(.75, .80, .82), Bull=(.70, .72, .78)),
        "H4": {s: (.90,)*3 for s in SC}, "T": {s: (.80,)*3 for s in SC},
        "EN": {s: (.80,)*3 for s in SC}}      # energy [A]: no growth to fund; sustaining capex a little above D&A
EN = (dict(Bear=tuple((x-30)/49 for x in (65, 60, 60, 60)), Base=tuple((x-30)/49 for x in (85, 77, 72, 70)),
           Bull=tuple((x-30)/49 for x in (85, 77, 72, 70))), (11, 12, 13), .55)
EN_PE9 = 14.8; EN_MOVE = 61.38/59.88          # IXC 15 Oct / 9 Oct
# --- company analyses (USD per share; V end-2027/28/29, D 2027-29, stub dividend, EPS 2027-30, CY27 consensus) ---
CO = {"CM": dict(names=["MSFT"], cons=21.75, stub=0.98, lay="E",                     # docs/msft-analysis.md v2 (15 Oct)
                 V=dict(Bear=(339.1, 370.7, 406.9), Base=(592.3, 646.5, 692.0), Bull=(688.1, 808.8, 919.7)),
                 D=dict(Bear=(3.97, 4.17, 4.38), Base=(4.01, 4.37, 4.76), Bull=(4.02, 4.42, 4.86)),
                 EPS=dict(Bear=(18.02, 17.67, 18.97, 20.41), Base=(20.58, 23.16, 25.81, 28.06), Bull=(21.83, 25.98, 30.02, 33.39))),
      "CG": dict(names=["GOOGL", "GOOG"], cons=15.05, stub=0.22, lay="E",             # docs/googl-analysis.md (15 Oct)
                 V=dict(Bear=(170.8, 190.4, 215.1), Base=(361.5, 377.1, 390.1), Bull=(434.2, 484.2, 537.5)),
                 D=dict(Bear=(0.88, 0.88, 0.88), Base=(0.91, 0.96, 1.01), Bull=(0.95, 1.04, 1.14)),
                 EPS=dict(Bear=(11.12, 10.48, 11.66, 13.02), Base=(13.45, 15.04, 16.70, 18.27), Bull=(14.60, 17.40, 19.79, 22.24))),
      # docs/nvda-analysis.md v1 (17 Oct), calendarised (x 15.21/15.91) with the revenue-consistent Bear .68/.50/.53/.57,
      # as that analysis quantifies and the AI BBB adopted; rebuilt for docs/dnb-teknologi-analysis.md (17 Oct) [A]
      "CN": dict(names=["NVDA"], cons=15.21, stub=0.75, lay="H1",
                 V=dict(Bear=(106.7, 115.7, 126.4), Base=(237.5, 261.8, 273.9), Bull=(289.0, 350.2, 402.5)),
                 D=dict(Bear=(4.99, 4.57, 4.18), Base=(6.41, 8.45, 8.80), Bull=(6.81, 9.56, 10.68)),
                 EPS=dict(Bear=(10.34, 7.61, 8.06, 8.67), Base=(13.99, 14.91, 15.21, 14.75), Bull=(15.21, 17.49, 19.01, 19.77)))}
# --- prices 9 Oct and 15 Oct (Yahoo closes, close.py), CY27 EPS calendarised (AI BBB Update 2, 17 Oct) ---
EU9, EU15 = 1.1213, 1.1195
P9 = {"MSFT": 535.07, "GOOGL": 351.66, "GOOG": 347.86, "AMZN": 262.43, "META": 718.67, "ORCL": 141.40, "NVDA": 229.28, "AMD": 608.10,
      "AVGO": 361.54, "MRVL": 275.28, "MU": 1029.0, "ASML": 1780.34, "AMAT": 507.03, "LRCX": 318.84, "ANET": 216.74, "VRT": 242.78,
      "ETN": 429.65, "NOW": 140.86, "CRM": 229.13, "ADBE": 242.27, "PLTR": 209.05, "SAP": 191.46*EU9, "INTU": 302.75, "SNOW": 368.89, "DDOG": 293.26}
P15 = {"MSFT": 539.44, "GOOGL": 349.22, "GOOG": 344.91, "AMZN": 254.76, "META": 736.72, "ORCL": 134.47, "NVDA": 217.23, "AMD": 562.23,
       "AVGO": 344.33, "MRVL": 241.24, "MU": 931.24, "ASML": 1657.44, "AMAT": 430.01, "LRCX": 277.46, "ANET": 185.58, "VRT": 214.75,
       "ETN": 402.48, "NOW": 148.57, "CRM": 246.74, "ADBE": 251.67, "PLTR": 200.50, "SAP": 201.25*EU15, "INTU": 330.17, "SNOW": 335.07, "DDOG": 266.25}
EPS27 = {"AMZN": 10.55, "META": 33.92, "ORCL": 9.80, "NVDA": 15.21, "AMD": 15.76, "AVGO": 19.40, "MRVL": 7.04,
         "MU": 192.10, "ASML": 55.93*EU15, "AMAT": 18.46, "LRCX": 10.62, "ANET": 5.22, "VRT": 9.19, "ETN": 16.29,
         "NOW": 5.01, "CRM": 16.08, "ADBE": 27.51, "PLTR": 2.35, "SAP": 8.38*EU15, "INTU": 25.12, "SNOW": 2.94, "DDOG": 2.97}
EPS27_V1 = {"AMZN": 10.5269, "META": 34.07467, "ORCL": (8.14059+10.99899)/2, "NVDA": 15.9146, "AMD": 15.72189, "AVGO": 19.39382, "MRVL": 7.28277,
            "MU": 206.33243, "ASML": 58.475166, "AMAT": 18.47894, "LRCX": 11.76415, "ANET": 5.21686, "VRT": 9.18451, "ETN": 16.2461,
            "NOW": 5.00551, "CRM": 16.0207, "ADBE": 27.67328, "PLTR": 2.35154, "SAP": 8.36656*1.1210, "INTU": 27.07543, "SNOW": 3.0052, "DDOG": 2.97446}
LAY = {"E": ["AMZN", "META", "ORCL"], "H1": ["AMD", "AVGO", "MRVL"], "H2": ["MU"], "H3": ["ASML", "AMAT", "LRCX"],
       "H4": ["ANET", "VRT", "ETN"], "T": ["NOW", "CRM", "ADBE", "PLTR", "SAP", "INTU", "SNOW", "DDOG"]}
UA = json.load(open("dl2/urth_ai.json")); NORM = UA["total"]/100
ALLN = [n for v in LAY.values() for n in v]+["MSFT", "GOOGL", "GOOG", "NVDA"]
WW9 = {n: UA["w"][n]/NORM for n in ALLN}                     # MSCI World weights 9 Oct (URTH), normalised
W_EN9 = UA["energy"]/NORM
MULT = {"MSFT": 5.88/4.00, "NVDA": 5.78/5.81, "AMZN": 3.79/2.67, "AMD": 2.48/1.10, "AVGO": 2.37/1.76, "GOOGL": 2.23/2.23,
        "META": 1.77/1.76, "GOOG": 1.75/1.76, "MU": 1.43/1.18, "ASML": 0.55}
CC_EN9 = 0.30; CC_PE27 = W_PE27*18.93/17.92; E0C = 100/CC_PE27
PEX_OVR = {}      # e.g. {("H2","Bear"): 4.8} for the memory-stressed Bear


def cc_w9(tail=1.0):
    return {n: (0.47 if n == "MRVL" else v*MULT[n] if n in MULT else v*tail) for n, v in WW9.items()}


def build(w9, en9):
    """blocks at the 15 Oct close in 9-Oct value units: value, CY27 earnings, P/E"""
    eps = EPS27_V1 if CONS_V1 else EPS27
    lay = {k: list(v) for k, v in LAY.items()}
    co = dict(CO)
    if CN_LAYER: lay["H1"] = ["NVDA"]+lay["H1"]; co.pop("CN")
    b = {}
    for L, names in lay.items():
        v = sum(w9[n]*P15[n]/P9[n] for n in names); e = sum(w9[n]/(P9[n]/eps[n]) for n in names)
        b[L] = dict(kind="layer", v=v, e=e, pe=v/e)
    for c, d in co.items():
        v = sum(w9[n]*P15[n]/P9[n] for n in d["names"]); sh = sum(w9[n]/P9[n] for n in d["names"])   # shares (9-Oct units)
        b[c] = dict(kind="co", v=v, e=sh*d["cons"], pe=v/(sh*d["cons"]), sh=sh)
    b["EN"] = dict(kind="en", v=en9*EN_MOVE, e=en9/EN_PE9, pe=EN_PE9*EN_MOVE)
    return b


def lpath(lay, s):
    if BEAR_V1 and s == "Bear" and lay in BEAR1: return BEAR1[lay]
    return AI[lay][0][s]


def vals(name, x, s, pex_shift=0.0, layer_override=None):
    """V (end-27/28/29, incl. retained cash), D (2027-29), stub D, EPS (2027-30) for block x under scenario s"""
    if x["kind"] == "co":
        d = CO[name]; sh = x["sh"]
        return [sh*v for v in d["V"][s]], [sh*v for v in d["D"][s]], sh*d["stub"], [sh*v for v in d["EPS"][s]]
    if x["kind"] == "en": lay = "EN"; eps, pex, pay = EN[0][s], EN[1][SC.index(s)], EN[2]
    else:
        lay = layer_override or name
        eps, pex, pay = lpath(lay, s), AI[lay][1][SC.index(s)], AI[lay][2]
        pex = PEX_OVR.get((lay, s), pex)
    pex += pex_shift; e = x["e"]; pe0 = x["pe"]
    path = [pex]*3 if s == "Bear" else [pe0+(pex-pe0)*(k+1)/3 for k in range(3)]
    V = []; cum = 0.0
    for k in range(3):
        if RET: cum += (CONV[lay][s][k]-pay)*e*eps[k]
        V.append(path[k]*e*eps[k+1]+cum)
    return V, [pay*e*eps[k] for k in range(3)], pay*e*STUB, [e*v for v in eps]


def blocks_W(): return build(WW9, W_EN9)


def world_rest(s, pex_shift=0.0, co_layer=(), WB=None):
    WB = WB or blocks_W()
    V = [(W_PE[s][k]+pex_shift)*E0*W_EPS[s][k+1] for k in range(3)]; D = [W_PAY*E0*W_EPS[s][k] for k in range(3)]
    Dst = 100*W_Y*STUB; Er = [E0*x for x in W_EPS[s]]
    v_r = 100*R_W; e_r = E0
    for n, x in WB.items():
        if n in co_layer: v, d, ds, ee = vals(n, dict(x, kind="layer"), s, pex_shift, CO[n]["lay"])
        else: v, d, ds, ee = vals(n, x, s, pex_shift)
        V = [V[k]-v[k] for k in range(3)]; D = [D[k]-d[k] for k in range(3)]; Dst -= ds; Er = [Er[k]-ee[k] for k in range(4)]
        v_r -= x["v"]; e_r -= x["e"]
    return dict(v=v_r, e=e_r, pe=v_r/e_r, V=V, D=D, Dst=Dst, eps=[x/e_r for x in Er], pepath=[V[k]/Er[k+1] for k in range(3)],
                pay=[D[k]/Er[k] for k in range(3)])


def irr(fl):
    lo, hi = -0.95, 2.0
    for _ in range(200):
        m = (lo+hi)/2; v = sum(c/(1+m)**t for t, c in fl)
        lo, hi = (m, hi) if v > 0 else (lo, m)
    return m


def evaluate(P0, parts, s, cost=0.0, em=1.0):
    V = [em*sum(p[0][k] for p in parts) for k in range(3)]; D = [em*sum(p[1][k] for p in parts) for k in range(3)]
    Dst = em*sum(p[2] for p in parts); f = FX[s]; drag = lambda t: (1-cost)**t
    V = [V[k]*f[k]*drag(STUB+k+1) for k in range(3)]; D = [D[k]*f[k]*drag(STUB+k+0.5) for k in range(3)]
    Dst = Dst*drag(STUB/2); Vst = P0*drag(STUB)
    r = []; prev = Vst
    for k in range(3): r.append((D[k]+V[k])/prev-1); prev = V[k]
    fl = [(0, -P0), (STUB, Dst)]+[(STUB+k+0.5, D[k]) for k in range(3)]+[(T, V[2])]
    I = irr(fl); Pk = sum(c/(1+K)**t for t, c in fl[1:])
    lv = [Vst+Dst]
    for x in r: lv.append(lv[-1]*(1+x))
    return dict(irr=I, r=r, Pk=Pk/P0*100, stub=(Dst+Vst)/P0-1, VT=V[2]/P0*100, sumD=(Dst+sum(D))/P0*100, lv=[v/P0*100 for v in lv],
                d=(Dst+sum(D))/T/P0, g=(V[2]/P0)**(1/T)-1)


def er(o):
    E = (o["Base"]["irr"]-nibw)*100; R = (o["Base"]["r"][0]-o["Bear"]["r"][0])*100; return E, R, E/R


def run(which="W", cost=0.0, tail=1.0, prem_mode="keep", pex_shift=0.0, ai_only=None, dp=0.0, em=1.0, co_layer=(), only=None, rest_trend=False):
    """dp = price change from the 15 Oct close at unchanged earnings and future values; ai_only = 'Bear'/'Bull' for AI and company
    blocks only; co_layer = company blocks put back on their layer path"""
    WB = blocks_W()
    if which == "W": bl = WB; P0 = 100*R_W
    else: bl = build(cc_w9(tail), CC_EN9); P0 = 100*R_C
    sc = 1+dp; out = {}; det = {}
    for s in SC:
        sx = s; srest = sfx = ("Base" if ai_only and s == ai_only else s)
        parts = {}
        for n, x in bl.items():
            ss = srest if n == "EN" else sx
            if n in co_layer: v, d, ds, ee = vals(n, dict(x, kind="layer"), ss, pex_shift, CO[n]["lay"])
            else: v, d, ds, ee = vals(n, x, ss, pex_shift)
            parts[n] = (v, d, ds, x["v"]*sc, ee)
        R = world_rest(srest, pex_shift, co_layer, WB)
        if rest_trend and srest == "Base":
            rel = [0.97*1.055**k for k in range(4)]
            R = dict(R, eps=rel, V=[R["pepath"][k]*R["e"]*rel[k+1] for k in range(3)], D=[R["pay"][k]*R["e"]*rel[k] for k in range(3)])
        if which == "W":
            parts["REST"] = (R["V"], R["D"], R["Dst"], R["v"]*sc, [R["e"]*x for x in R["eps"]]); det[s] = dict(REST=R)
        else:
            v_r = P0-sum(x["v"] for x in bl.values()); e_r = E0C-sum(x["e"] for x in bl.values())
            prem = (v_r/e_r)/R["pe"]; pm = {"keep": prem, "half": 1+(prem-1)/2, "gone": 1.0}[prem_mode]
            if srest == "Bear": pm = 1+(pm-1)/2
            rel = R["eps"]
            parts["REST"] = ([R["pepath"][k]*pm*e_r*rel[k+1] for k in range(3)], [R["pay"][k]*e_r*rel[k] for k in range(3)],
                             R["Dst"]/R["e"]*e_r, v_r*sc, [e_r*x for x in rel])
            det[s] = dict(REST=dict(v=v_r, e=e_r, pe=v_r/e_r, prem=prem, pm=pm))
        det[s]["eps"] = [sum(p[4][k] for p in parts.values()) for k in range(4)]
        if only:
            sel = [parts[n] for n in only]; out[s] = evaluate(sum(p[3] for p in sel), [p[:3] for p in sel], sfx, cost, em)
        else:
            out[s] = evaluate(P0*sc, [p[:3] for p in parts.values()], sfx, cost, em)
    return out, det, bl


if __name__ == "__main__":
    print(f"NIBOR window {nibw*100:.2f}%  STUB {STUB*365:.0f}d  R_W {R_W:.4f}  R_C {R_C:.4f}")
    WB = blocks_W(); cb = build(cc_w9(), CC_EN9)
    print("Block   World w15 / P/E / earn%      CC w15 / P/E / earn%")
    for n in WB:
        x = WB[n]; y = cb[n]
        print(f"{n:3s} {x['v']/R_W:6.2f} {x['pe']:6.1f} {x['e']/E0*100:5.1f}%   {y['v']/R_C:6.2f} {y['pe']:6.1f} {y['e']/E0C*100:5.1f}%")
    ai = [n for n in WB if n != "EN"]
    for lab, bl, P0, EE in [("World", WB, 100*R_W, E0), ("CC", cb, 100*R_C, E0C)]:
        v = sum(bl[n]["v"] for n in ai); e = sum(bl[n]["e"] for n in ai)
        print(f"{lab}: AI+co {v/P0*100:.2f}% of value, P/E {v/e:.1f}, {e/EE*100:.1f}% of earnings; energy {bl['EN']['v']/P0*100:.2f}% ({bl['EN']['e']/EE*100:.1f}% of earnings)")
    for s in SC:
        R = world_rest(s); print(f"World rest {s}: w {R['v']/R_W:.2f} P/E {R['pe']:.2f} EPS {[round(x, 3) for x in R['eps']]} V/EPS path {[round(x, 2) for x in R['pepath']]} payout {[round(x, 2) for x in R['pay']]}")
    o, d, _ = run("W"); print("World (no cost):", [round(o[s]['irr']*100, 2) for s in SC], [round(o[s]['r'][0]*100, 1) for s in SC])
    o, d, _ = run("C"); print("CC (no cost):", [round(o[s]['irr']*100, 2) for s in SC], [round(o[s]['r'][0]*100, 1) for s in SC], "rest prem", round(d['Base']['REST']['prem'], 3), "CC rest P/E", round(d['Base']['REST']['pe'], 2))
