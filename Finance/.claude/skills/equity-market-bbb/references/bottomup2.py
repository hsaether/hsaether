# Equity BBB Update 2 (6 Nov 2026): Oslo bottom-up on Yahoo earningsTrend 6 Nov (CY26 / CY27), prices 5 Nov close (valq.py -> data/val.json).
# OBX sample weights: DNB OBX ETF top holdings (Yahoo look-through, unchanged since 9 Oct) repriced by each name's price move 9 Oct -> 5 Nov.
import json
q = json.load(open("data/val.json"))
FX = {"NOK": 1, "USD": 9.2944, "EUR": 10.442}         # Yahoo 5 Nov close
W9 = {"EQNR": 16.1, "DNB": 10.4, "KOG": 7.3, "NHY": 6.7, "AKRBP": 6.2, "MOWI": 5.1, "STB": 4.9, "TEL": 4.7, "SUBC": 4.3, "YAR": 4.2,
      "ORK": 3.5, "GJF": 2.5, "FRO": 2.5, "VAR": 1.5}
P9 = {"EQNR": 417.9, "AKRBP": 353.7, "VAR": 53.2, "SUBC": 338.6, "FRO": 543.6, "DNB": 302.4, "STB": 187.9, "GJF": 254.2, "KOG": 295.4,
      "NHY": 78.9, "MOWI": 203.8, "TEL": 124.5, "YAR": 413.6, "ORK": 93.05}
BLK = {"EQNR": "E", "AKRBP": "E", "VAR": "E", "SUBC": "E", "FRO": "E", "DNB": "F", "STB": "F", "GJF": "F"}
# consensus 6 Nov (Yahoo earningsTrend; 0y = CY26, +1y = CY27), currency of EPS
C = {"EQNR": (5.86759, 4.65483, "USD", 19), "AKRBP": (4.19978, 3.38032, "USD", 16), "VAR": (0.76961, 0.60791, "USD", 12),
     "SUBC": (2.63884, 2.69132, "USD", 14), "FRO": (12.49122, 7.30763, "USD", 4), "DNB": (26.64303, 28.44148, "NOK", 16),
     "STB": (11.53158, 13.52433, "NOK", 8), "GJF": (15.46425, 17.47045, "NOK", 13), "KOG": (7.31654, 11.41755, "NOK", 10),
     "NHY": (8.15768, 7.55935, "NOK", 13), "MOWI": (1.19445, 1.43753, "EUR", 11), "TEL": (11.73496, 9.19243, "NOK", 14),
     "YAR": (46.944, 40.50239, "NOK", 18), "ORK": (6.6119, 6.85612, "NOK", 8)}
C11 = {"EQNR": (5.6789, 4.42852), "AKRBP": (3.52129, 2.97614), "VAR": (0.73711, 0.48742), "SUBC": (2.57323, 2.69656), "FRO": (8.5775, 5.16),
       "DNB": (26.49917, 28.12707), "STB": (11.68615, 13.44888), "GJF": (15.30021, 17.32513), "KOG": (7.33323, 11.40049), "NHY": (8.62394, 8.25514),
       "MOWI": (1.15617, 1.40604), "TEL": (10.37406, 9.32793), "YAR": (55.48273, 46.82372), "ORK": (6.61106, 6.86423)}
P = {n: q[n+".OL"]["price"] for n in W9}
W = {n: W9[n]*P[n]/P9[n] for n in W9}; tw = sum(W.values()); tw9 = sum(W9.values())
print(f"sample weight 9 Oct {tw9:.1f}; repriced (rel.) {tw:.2f}; scale to 9-Oct sum: x{tw9/tw:.4f}")
Wn = {n: w*tw9/tw for n, w in W.items()}
tot = {b: [0, 0, 0, 0, 0] for b in "EFO"}; e26 = e27 = dy = e27o = 0
print("name  blk  wt(5Nov)  P/E26  P/E27  g27   CY27 rev vs 11 Oct  fwd div yld  analysts")
for n, (a, b, c, na) in C.items():
    pe26 = P[n]/(a*FX[c]); pe27 = P[n]/(b*FX[c]); w = Wn[n]; bl = BLK.get(n, "O"); y = q[n+".OL"]["dy"]
    rev = b/C11[n][1]-1
    print(f"{n:6s} {bl}  {w:5.2f}  {pe26:6.1f} {pe27:6.1f} {b/a-1:+6.1%}  {rev:+6.1%}  {y*100:5.2f}%  {na}")
    t = tot[bl]; t[0] += w; t[1] += w/pe26; t[2] += w/pe27; t[3] += w*y; t[4] += w/pe27/(1+rev)
    e26 += w/pe26; e27 += w/pe27; dy += w*y; e27o += w/pe27/(1+rev)
for b, (w, a, c, y, co) in tot.items():
    print(f"{b}: w {w:.1f} ({w/tw9:.0%}) P/E26 {w/a:.1f} P/E27 {w/c:.1f} EPS g {c/a-1:+.1%} share26 {a/e26:.1%} share27 {c/e27:.1%} fwd dy {y/w*100:.2f}% CY27 rev {c/co-1:+.1%}")
print(f"Index sample: P/E26 {tw9/e26:.2f} P/E27 {tw9/e27:.2f} EPS g {e27/e26-1:+.1%} fwd dy {dy/tw9*100:.2f}%  CY27 consensus revision since 11 Oct (same weights) {e27/e27o-1:+.1%}")
json.dump({"W": Wn, "P": P}, open("data/obxw.json", "w"))
# B_cons from Equinor (CY26 Brent avg 93.0: Q1-Q3 Yahoo BZ=F daily 79.1/96.5/92.0 + Q4 oil BBB stub 104.3)
B26 = (79.14+96.47+91.98+104.3)/4; r = C["EQNR"][1]/C["EQNR"][0]
print(f"B26 {B26:.2f}; Equinor CY27/CY26 {r:.4f} -> B_cons {30+r*(B26-30):.1f}; Aker BP {30+C['AKRBP'][1]/C['AKRBP'][0]*(B26-30):.1f}; Var {30+C['VAR'][1]/C['VAR'][0]*(B26-30):.1f}")
