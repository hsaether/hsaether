# Global index funds, 29 Oct 2026 re-mark (inputs only; prices, NAVs and stub kept at the 15 Oct NAV date).
# On top of idxai4.py (18 Oct, Equity BBB Update 1 World build), replaces:
#   CM Microsoft  <- docs/msft-analysis.md v3 (28 Oct, Q1 FY27)
#   CG Alphabet   <- docs/googl-analysis.md v2 (28 Oct, Q3)
#   E cash conversion -.10/.10/.30 -> -.20/.00/.20 (docs/ai-market-bbb.md Update 3, 22 Oct; kept in Updates 4-5)
# The E block (Amazon, Meta, Oracle) keeps the E-rest EPS path (.97 / 1.07 / 1.17 / 1.27 Base): the Update 5 move of the
# E layer to .92 in 2027 comes from Alphabet's and Microsoft's own EPS, which this build already carries in CG and CM
# (sensitivity E92 below). Interim V_t (end-2027, end-2028) of CM and CG are re-glided to the 15 Oct block price with
# the analyses' own rule (core P/E glides linearly from today's to the exit P/E; Bear at exit from end-2027); V_T,
# D_t and EPS are the analyses' figures. Consensus basis (block CY27 earnings) kept at the Equity BBB's 17 Oct values.
import sys, os, copy; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idxai4 as X
M = X.M; SC = X.SC

CO_18 = copy.deepcopy(M.CO); CONV_E_18 = copy.deepcopy(M.CONV["E"]); AI_E_18 = copy.deepcopy(M.AI["E"])


def reglide(V, EPS, p_block, p_an, eps27, glide=True):
    """shift interim V by the change in today's core P/E (price difference / Base CY27 EPS), fading to 0 at exit"""
    if not glide: return tuple(V)
    dpe = (p_block-p_an)/eps27
    return (V[0]+dpe*2/3*EPS[1], V[1]+dpe*1/3*EPS[2], V[2])


MSFT_P, MSFT_E27 = 531.01, 20.77       # msft v3 run price (28 Oct) and Base CY27 EPS
GOOGL_P, GOOGL_E27 = 324.89, 12.66     # googl v2 run price (28 Oct) and Base CY27 core EPS
MS = dict(V=dict(Bear=(337.7, 368.8, 404.5), Base=(585.8, 643.2, 692.1), Bull=(681.6, 806.0, 921.4)),
          D=dict(Bear=(3.97, 4.17, 4.38), Base=(4.01, 4.37, 4.76), Bull=(4.02, 4.42, 4.86)),
          EPS=dict(Bear=(18.18, 17.84, 19.16, 20.61), Base=(20.77, 23.40, 26.11, 28.39), Bull=(22.03, 26.26, 30.37, 33.80)), stub=0.98)
GO = dict(V=dict(Bear=(160.1, 179.0, 202.6), Base=(340.4, 356.8, 371.1), Bull=(412.5, 461.8, 515.9)),
          D=dict(Bear=(0.88, 0.88, 0.88), Base=(0.91, 0.96, 1.01), Bull=(0.95, 1.04, 1.14)),
          EPS=dict(Bear=(10.46, 9.82, 11.00, 12.33), Base=(12.66, 14.28, 15.89, 17.44), Bull=(13.80, 16.66, 18.97, 21.39)), stub=0.22)


def co_block(src, p_block, p_an, eps27, glide=True):
    return dict(V={s: reglide(src["V"][s], src["EPS"][s], p_block, p_an, eps27, glide and s != "Bear") for s in SC},
                D=dict(src["D"]), EPS=dict(src["EPS"]), stub=src["stub"])


def setup(msft=True, googl=True, conv=True, e92=False, glide=True):
    M.CO = copy.deepcopy(CO_18); M.CONV["E"] = copy.deepcopy(CONV_E_18); M.AI["E"] = copy.deepcopy(AI_E_18)
    if msft: M.CO["CM"].update(co_block(MS, M.P15["MSFT"], MSFT_P, MSFT_E27, glide))
    if googl: M.CO["CG"].update(co_block(GO, M.P15["GOOGL"], GOOGL_P, GOOGL_E27, glide))
    if conv: M.CONV["E"] = dict(Bear=(-.10, .30, .50), Base=(-.20, .00, .20), Bull=(-.30, -.20, .00))
    if e92:
        e = M.AI["E"]; M.AI["E"] = (dict(e[0], Base=(.92,)+tuple(e[0]["Base"][1:])), e[1], e[2])


setup()

if __name__ == "__main__":
    for s in SC: print("CM", s, [round(v, 1) for v in M.CO["CM"]["V"][s]], " CG", s, [round(v, 1) for v in M.CO["CG"]["V"][s]])
    steps = [("18 Oct model", dict(msft=False, googl=False, conv=False)), ("+ Microsoft v3", dict(googl=False, conv=False)),
             ("+ Alphabet v2", dict(conv=False)), ("+ E cash conversion (= model)", {}), ("sens: + E Base 2027 .92", dict(e92=True)),
             ("sens: model without re-glide", dict(glide=False))]
    for lab, kw in steps:
        setup(**kw)
        for w, c in (("W", 0.0025), ("C", 0.0019), ("W", 0.0)):
            o, d, _ = X.run(w, cost=c); E, R, ER = X.er(o)
            print(f"{lab:32s} {w} cost {c:.4f}: Bear {o['Bear']['irr']*100:6.2f} Base {o['Base']['irr']*100:5.2f} Bull {o['Bull']['irr']*100:5.2f}"
                  f" | 27 {o['Bear']['r'][0]*100:6.1f}/{o['Base']['r'][0]*100:5.1f}/{o['Bull']['r'][0]*100:5.1f} | E {E:.2f} R {R:.1f} E/R {ER:.3f}"
                  f" | MoS {o['Base']['Pk']/100-1:+.1%} | EPS {[round(v, 3) for v in d['Base']['eps']]}")
    setup()
