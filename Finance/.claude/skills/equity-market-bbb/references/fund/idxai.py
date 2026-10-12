# Global index funds on the Equity BBB World paths, with the AI Market BBB layers (12 Oct 2026)
# World = AI blocks (AI BBB paths) + energy (oil BBB) + rest (implied, so that World = the Equity BBB path exactly)
# Climate Change index = the same blocks at its own weights; its rest carries the non-AI tilt premium
import json
STUB = 80/365; T = STUB+3; K = 0.12
NIB = {"stub": 4.80, "2027": 4.79, "2028": 4.39, "2029": 3.86}
nibw = ((1+NIB["stub"]/100)**STUB*(1+NIB["2027"]/100)*(1+NIB["2028"]/100)*(1+NIB["2029"]/100))**(1/T)-1
SC = ["Bear", "Base", "Bull"]
FX = {"Bear": [10.70/9.5555, 10.42/9.5555, 10.42/9.5555], "Base": [1, 1, 1], "Bull": [9.27/9.5555]*3}
# --- Equity BBB World (unchanged) ---
W_EPS = {"Bear": [.75, .82, .90, .97], "Base": [.95, 1.0165, 1.0775, 1.137], "Bull": [1.00, 1.09, 1.17, 1.25]}
W_PE = {"Bear": [15.0, 15.0, 15.0], "Base": [17.6, 17.3, 17.0], "Bull": [18.2, 18.4, 18.5]}
W_PE27 = 17.3; W_PAY = 0.45; W_Y = 0.025
# --- AI BBB layers (docs/ai-market-bbb.md, 12 Oct 2026): EPS 2027, 28, 29, 2030n; exit P/E Bear/Base/Bull; payout ---
AI = {"E":  (dict(Bear=(.88, .88, .97, 1.05), Base=(.97, 1.07, 1.17, 1.27), Bull=(1.0, 1.13, 1.27, 1.41)), (17, 21, 23.5), .34),
      "H1": (dict(Bear=(.70, .60, .70, .75), Base=(.92, .98, 1.00, .97), Bull=(1.0, 1.15, 1.25, 1.30)), (13, 17, 19), .25),
      "H2": (dict(Bear=(.60, .30, .25, .25), Base=(.90, .60, .40, .35), Bull=(1.0, .80, .55, .45)), (8, 10, 11), .15),
      "H3": (dict(Bear=(.80, .75, .85, .92), Base=(.95, 1.03, 1.10, 1.16), Bull=(1.0, 1.15, 1.28, 1.40)), (14, 18, 21), .45),
      "H4": (dict(Bear=(.75, .65, .75, .85), Base=(.95, 1.02, 1.07, 1.11), Bull=(1.0, 1.12, 1.22, 1.30)), (15, 20, 24), .35),
      "T":  (dict(Bear=(.88, .85, .93, 1.00), Base=(.95, 1.03, 1.11, 1.19), Bull=(1.0, 1.10, 1.20, 1.30)), (15, 20, 24), .45)}
# energy block: oil BBB through the Oslo block formula (Brent - 30) / (79 - 30) [A]; exit P/E 11/12/13, payout 55% [A]
EN = (dict(Bear=tuple((x-30)/49 for x in (65, 60, 60, 60)), Base=tuple((x-30)/49 for x in (85, 77, 72, 70)),
           Bull=tuple((x-30)/49 for x in (85, 77, 72, 70))), (11, 12, 13), .55)
EN_PE = 14.8   # CY27 P/E of energy (XOM as proxy) [A]
# --- names: P/E on CY27 consensus (AI BBB appendix prices of 9 Oct / AI BBB CY27 EPS) ---
PE = {"MSFT": 535.07/((19.76867+23.67732)/2), "GOOGL": 351.66/14.97242, "GOOG": 351.66/14.97242, "AMZN": 262.43/10.5269,
      "META": 718.67/34.07467, "ORCL": 141.40/((8.14059+10.99899)/2),
      "NVDA": 229.28/15.9146, "AMD": 608.10/15.72189, "AVGO": 361.54/19.39382, "MRVL": 275.28/7.28277, "MU": 1029.0/206.33243,
      "ASML": 1780.34/58.475166, "AMAT": 507.03/18.47894, "LRCX": 318.84/11.76415,
      "ANET": 216.74/5.21686, "VRT": 242.78/9.18451, "ETN": 429.65/16.2461,
      "NOW": 140.86/5.00551, "CRM": 229.13/16.0207, "ADBE": 242.27/27.67328, "PLTR": 209.05/2.35154, "SAP": 191.46/8.36656,
      "INTU": 302.75/27.07543, "SNOW": 368.89/3.0052, "DDOG": 293.26/2.97446}
BLK = {"E": ["MSFT", "GOOGL", "GOOG", "AMZN", "META", "ORCL"], "H1": ["NVDA", "AMD", "AVGO", "MRVL"], "H2": ["MU"],
       "H3": ["ASML", "AMAT", "LRCX"], "H4": ["ANET", "VRT", "ETN"], "T": ["NOW", "CRM", "ADBE", "PLTR", "SAP", "INTU", "SNOW", "DDOG"]}
UA = json.load(open("dl2/urth_ai.json")); NORM = UA["total"]/100   # URTH equity weights sum to 99.78 (9 Oct)
WW = {n: UA["w"][n]/NORM for b in BLK.values() for n in b}  # MSCI World weights, URTH 9 Oct 2026 (ticker + country), normalised to 100
W_EN = UA["energy"]/NORM                                    # URTH energy sector weight, 9 Oct (4.18%)
# CC weights: top 10 via MSCI factsheet multipliers (30 Sep) on today's World weights; MU via Nordnet 31 Aug vs DNB 31 Aug;
# MRVL at Nordnet's 0.47 (31 Aug); ASML x0.55 (absent from the CC top 25 at 0.43); others x tail (1.0) [A]
MULT = {"MSFT": 5.88/4.00, "NVDA": 5.78/5.81, "AMZN": 3.79/2.67, "AMD": 2.48/1.10, "AVGO": 2.37/1.76, "GOOGL": 2.23/2.23,
        "META": 1.77/1.76, "GOOG": 1.75/1.76, "MU": 1.43/1.18, "ASML": 0.55}
CC_EN = 0.30; CC_PE27 = W_PE27*18.93/17.92


def cc_w(tail=1.0):
    w = {}
    for n, v in WW.items():
        if n == "MRVL": w[n] = 0.47
        elif n in MULT: w[n] = v*MULT[n]
        else: w[n] = v*tail
    return w


def blocks(wts):
    out = {}
    for b, names in BLK.items():
        w = sum(wts[n] for n in names); e = sum(wts[n]/PE[n] for n in names)
        out[b] = dict(w=w, e=e, pe=w/e)
    return out


def block_vals(b, e, s, pe0, pex_shift=0.0):
    """year-end values V (end-27/28/29), dividends D (2027-29), stub D and EPS for a block with CY27 consensus earnings e"""
    if b == "EN": eps, pex, pay = EN[0][s], EN[1][SC.index(s)], EN[2]
    else: eps, pex, pay = AI[b][0][s], AI[b][1][SC.index(s)], AI[b][2]
    pex += pex_shift
    path = [pex]*3 if s == "Bear" else [pe0+(pex-pe0)*(k+1)/3 for k in range(3)]
    V = [path[k]*e*eps[k+1] for k in range(3)]; D = [pay*e*eps[k] for k in range(3)]; Dst = pay*e*STUB
    return V, D, Dst, [e*x for x in eps]


def world_rest(wbl, s, pex_shift=0.0):
    """rest of World for scenario s, implied so that the sum of blocks equals the Equity BBB World path"""
    E0 = 100/W_PE27
    V = [(W_PE[s][k]+pex_shift)*E0*W_EPS[s][k+1] for k in range(3)]; D = [W_PAY*E0*W_EPS[s][k] for k in range(3)]
    Dst = 100*W_Y*STUB; Er = [E0*x for x in W_EPS[s]]
    w_r = 100-sum(x["w"] for x in wbl.values())-W_EN; e_r = E0-sum(x["e"] for x in wbl.values())-W_EN/EN_PE
    for b, x in list(wbl.items())+[("EN", dict(w=W_EN, e=W_EN/EN_PE, pe=EN_PE))]:
        v, d, ds, ee = block_vals(b, x["e"], s, x["pe"], pex_shift)
        V = [V[k]-v[k] for k in range(3)]; D = [D[k]-d[k] for k in range(3)]; Dst -= ds; Er = [Er[k]-ee[k] for k in range(4)]
    return dict(w=w_r, e=e_r, pe=w_r/e_r, V=V, D=D, Dst=Dst, eps=[x/e_r for x in Er],
                pepath=[V[k]/Er[k+1] for k in range(3)], pay=[D[k]/Er[k] for k in range(3)])


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
    return dict(irr=I, r=r, Pk=Pk, stub=(Dst+Vst)/P0-1, VT=V[2], sumD=Dst+sum(D), lv=lv, d=(Dst+sum(D))/T/P0,
                g=(V[2]/P0)**(1/T)-1)


def er(o):
    E = (o["Base"]["irr"]-nibw)*100; R = (o["Base"]["r"][0]-o["Bear"]["r"][0])*100; return E, R, E/R


def run_index(which="W", cost=0.0, tail=1.0, prem_mode="keep", pex_shift=0.0, ai_only=None, P0=100.0, only=None, em=1.0):
    """which W (MSCI World, DNB) or C (Climate Change, Nordnet). ai_only='Bear'/'Bull': AI blocks on that scenario,
    energy, rest and NOK on Base. only=block name: evaluate that block alone (value = its weight)."""
    wbl = blocks(WW)
    cbl, en_w = (wbl, W_EN) if which == "W" else (blocks(cc_w(tail)), CC_EN)
    sc_p = P0/100   # price change at unchanged earnings: values now scale, earnings do not
    out = {}; det = {}
    for s in SC:
        sb = srest = sfx = s
        if ai_only and s == ai_only: srest = sfx = "Base"
        parts = {}
        for b, x in cbl.items():
            v, d, ds, _ = block_vals(b, x["e"], sb, x["pe"]*sc_p, pex_shift); parts[b] = (v, d, ds, x["w"]*sc_p)
        v, d, ds, _ = block_vals("EN", en_w/EN_PE, srest, EN_PE*sc_p, pex_shift); parts["EN"] = (v, d, ds, en_w*sc_p)
        R = world_rest(wbl, srest, pex_shift)
        if which == "W":
            # at a different P0 the rest's start value scales; its path stays the implied one (start P/E changes only)
            parts["REST"] = (R["V"], R["D"], R["Dst"], R["w"]*sc_p); det[s] = dict(REST=R)
        else:
            w_r = 100-sum(x["w"] for x in cbl.values())-en_w; e_r = 100/CC_PE27-sum(x["e"] for x in cbl.values())-en_w/EN_PE
            prem = (w_r/e_r)/R["pe"]
            pm = {"keep": prem, "half": 1+(prem-1)/2, "gone": 1.0}[prem_mode]
            if srest == "Bear": pm = 1+(pm-1)/2
            rel = R["eps"]
            V = [R["pepath"][k]*pm*e_r*rel[k+1] for k in range(3)]; D = [R["pay"][k]*e_r*rel[k] for k in range(3)]
            Dst = R["Dst"]/R["e"]*e_r
            parts["REST"] = (V, D, Dst, w_r*sc_p); det[s] = dict(REST=dict(w=w_r, e=e_r, pe=w_r/e_r, prem=prem, pm=pm))
        if only:
            p = parts[only]; out[s] = evaluate(p[3], [p[:3]], sfx, cost)
        else:
            out[s] = evaluate(P0, [p[:3] for p in parts.values()], sfx, cost, em)
    return out, det


if __name__ == "__main__":
    print(f"NIBOR window {nibw*100:.2f}%  STUB {STUB*365:.0f} days")
    wbl = blocks(WW); ccb = blocks(cc_w()); E0 = 100/W_PE27; E0c = 100/CC_PE27
    print("\nBlock  World w / P/E / earn share    CC w / P/E / earn share")
    for b in BLK:
        x = wbl[b]; y = ccb[b]
        print(f"{b:3s} {x['w']:6.2f} {x['pe']:6.1f} {x['e']/E0*100:6.1f}%    {y['w']:6.2f} {y['pe']:6.1f} {y['e']/E0c*100:6.1f}%")
    aiw = sum(x["w"] for x in wbl.values()); aie = sum(x["e"] for x in wbl.values())
    ciw = sum(x["w"] for x in ccb.values()); cie = sum(x["e"] for x in ccb.values())
    print(f"AI  World {aiw:.2f}% P/E {aiw/aie:.1f} earn {aie/E0*100:.1f}%  | CC {ciw:.2f}% P/E {ciw/cie:.1f} earn {cie/E0c*100:.1f}%")
    print(f"EN  World {W_EN:.2f}% earn {W_EN/EN_PE/E0*100:.1f}% | CC {CC_EN}% earn {CC_EN/EN_PE/E0c*100:.1f}%")
    for s in SC:
        R = world_rest(wbl, s)
        print(f"World rest {s}: w {R['w']:.2f} P/E now {R['pe']:.2f} EPS {[round(v, 3) for v in R['eps']]} "
              f"P/E path {[round(v, 2) for v in R['pepath']]} payout {[round(v, 2) for v in R['pay']]} stub y {R['Dst']/R['w']/STUB*100:.2f}%")
    o, d = run_index("W")
    print("\nWorld check (equity BBB -0.2/6.1/11.0; 2027 -18.2/5.9/13.8):", [round(o[s]['irr']*100, 2) for s in SC],
          [round(o[s]['r'][0]*100, 1) for s in SC], "E/R at 0.20%", round(er(run_index('W', cost=0.002)[0])[2], 3))
    o, d = run_index("C")
    print("CC no cost:", [round(o[s]['irr']*100, 2) for s in SC], [round(o[s]['r'][0]*100, 1) for s in SC],
          " rest premium", round(d['Base']['REST']['prem'], 3), "CC rest P/E", round(d['Base']['REST']['pe'], 2))
