# Global index funds, 18 Oct 2026 re-run on Equity BBB Update 1 (amended 18 Oct; references/upd.py).
# World = company blocks (MSFT, GOOGL, NVDA) + AI layer blocks (AI BBB v2, retained cash) + energy + EXPLICIT rest path
#         (the Equity BBB's REST_EPS / REST_PE / REST_PAY). DNB = MSCI World on this build at the NAV-date price.
# Climate Change index (Nordnet) = the same blocks at its weights + the rest path with its rest P/E premium.
# One rule as the Equity BBB: energy payout 0.76, c 0.80, Brent Base 2027 88; 70% of earnings on USD/NOK, 30% on I-44.
# Prices: 15 Oct close = last published NAV date (16 Oct NAVs not out on 18 Oct); set DATE16=True to reproduce upd.py at 16 Oct.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idxai3 as M
SC = M.SC; STUB = M.STUB; T = M.T; nibw = M.nibw
DATE16 = "--d16" in sys.argv
B27 = 88; EN_PAY = 0.76
M.EN = (dict(Bear=tuple((x-30)/49 for x in (65, 60, 60, 60)), Base=tuple((x-30)/49 for x in (B27, 77, 72, 70)),
             Bull=tuple((x-30)/49 for x in (B27, 77, 72, 70))), (11, 12, 13), EN_PAY)
if DATE16:   # the Equity BBB's own date (check)
    EU = 1.1213
    M.P15 = {"MSFT": 529.05, "GOOGL": 340.59, "GOOG": 336.91, "AMZN": 250.00, "META": 709.33, "ORCL": 128.23, "NVDA": 214.13, "AMD": 528.75,
             "AVGO": 328.75, "MRVL": 227.83, "MU": 878.84, "ASML": 1641.52, "AMAT": 409.29, "LRCX": 263.94, "ANET": 176.98, "VRT": 206.42,
             "ETN": 391.25, "NOW": 141.97, "CRM": 240.70, "ADBE": 245.20, "PLTR": 186.03, "SAP": 199.22*EU, "INTU": 325.15, "SNOW": 306.84, "DDOG": 247.11}
    M.R_W = 206.34/209.14; M.EN_MOVE = 62.98/59.88
USDP = {"Bear": [10.70/9.5555, 10.42/9.5555, 10.42/9.5555], "Base": [1, 1, 1], "Bull": [9.27/9.5555]*3}
I44P = {"Bear": [1.08, 1.06, 1.06], "Base": [1, 1, 1], "Bull": [0.98]*3}
USD_SH = 0.70
FXMIX = {s: [USD_SH*u+(1-USD_SH)*i for u, i in zip(USDP[s], I44P[s])] for s in SC}
M.FX = dict(FXMIX)
REST_EPS = {"Bear": [.83, .87, .95, 1.02], "Base": [.97*1.055**k for k in range(4)], "Bull": [1.00, 1.07, 1.14, 1.21]}
REST_PE = {"Bear": [15.08, 14.96, 14.86], "Base": [17.17, 16.67, 16.29], "Bull": [17.78, 17.61, 17.44]}
REST_PAY = {"Bear": [.49, .47, .48], "Base": [.50, .48, .48], "Bull": [.50, .49, .49]}
NAV = {"W": (867.98, 880.91), "C": (230.31, 234.44)}
R_C = M.R_W*(NAV["C"][0]/NAV["C"][1])/(NAV["W"][0]/NAV["W"][1])
WB = M.blocks_W()
W_VR = 100*M.R_W-sum(x["v"] for x in WB.values()); W_ER = M.E0-sum(x["e"] for x in WB.values()); W_PER = W_VR/W_ER


def run(which="W", cost=0.0, tail=1.0, prem_mode="keep", pex_shift=0.0, ai_only=None, dp=0.0, em=1.0, co_layer=(), only=None,
        rest=None, fx=None):
    """dp = price change at unchanged earnings and future values; ai_only = 'Bear'/'Bull' for AI and company blocks only"""
    rest = rest or REST_EPS
    if which == "W": bl = M.blocks_W(); P0 = 100*M.R_W; E00 = M.E0
    else: bl = M.build(M.cc_w9(tail), M.CC_EN9); P0 = 100*R_C; E00 = M.E0C
    v_r = P0-sum(x["v"] for x in bl.values()); e_r = E00-sum(x["e"] for x in bl.values())
    prem = (v_r/e_r)/W_PER if which == "C" else 1.0
    pm0 = {"keep": prem, "half": 1+(prem-1)/2, "gone": 1.0}[prem_mode]
    out = {}; det = {}
    for s in SC:
        srest = "Base" if ai_only and s == ai_only else s
        parts = {}
        for n, x in bl.items():
            ss = srest if n == "EN" else s
            if n in co_layer: v, d, ds, ee = M.vals(n, dict(x, kind="layer"), ss, pex_shift, M.CO[n]["lay"])
            else: v, d, ds, ee = M.vals(n, x, ss, pex_shift)
            parts[n] = (v, d, ds, x["v"]*(1+dp), ee)
        pm = 1+(pm0-1)/2 if srest == "Bear" else pm0
        eps = rest[srest]
        parts["REST"] = ([(REST_PE[srest][k]*pm+pex_shift)*e_r*eps[k+1] for k in range(3)], [REST_PAY[srest][k]*e_r*eps[k] for k in range(3)],
                         0.025*W_VR/W_ER*e_r*STUB, v_r*(1+dp), [e_r*x for x in eps])
        sfx = srest
        if fx: M.FX = fx
        if only:
            sel = [parts[n] for n in only]; out[s] = M.evaluate(sum(p[3] for p in sel), [p[:3] for p in sel], sfx, cost, em)
        else:
            out[s] = M.evaluate(P0*(1+dp), [p[:3] for p in parts.values()], sfx, cost, em)
        M.FX = dict(FXMIX)
        E = [sum(p[4][k] for p in parts.values()) for k in range(4)]; V = [sum(p[0][k] for p in parts.values()) for k in range(3)]
        det[s] = dict(eps=[x/E00 for x in E], vm=[V[k]/E[k+1] for k in range(3)], prem=prem, pm=pm, v_r=v_r, e_r=e_r, P0=P0, E00=E00)
    return out, det, bl


def er(o):
    E = (o["Base"]["irr"]-nibw)*100; R = (o["Base"]["r"][0]-o["Bear"]["r"][0])*100; return E, R, E/R


if __name__ == "__main__":
    print(f"R_W {M.R_W:.4f} R_C {R_C:.4f}  World rest: {W_VR/M.R_W:.2f}% of value, P/E {W_PER:.2f}, {W_ER/M.E0*100:.1f}% of earnings")
    for w in ("W", "C"):
        o, d, bl = run(w)
        print(w, "no cost:", [round(o[s]['irr']*100, 2) for s in SC], "27:", [round(o[s]['r'][0]*100, 1) for s in SC], "E-0.2/R/ER",
              round(er(o)[0]-0.2, 2), round(er(o)[1], 1), round((er(o)[0]-0.2)/er(o)[1], 3), "prem", round(d['Base']['prem'], 3),
              "rest P/E", round(d['Base']['v_r']/d['Base']['e_r'], 2), "EPS Base", [round(x, 3) for x in d['Base']['eps']], "vm", [round(x, 2) for x in d['Base']['vm']])
