# Oslo sample: aggregate P/B, P/E, ROE, dividend yield and payout under several weightings (Equity BBB skill 2026-10-18.1)
# Input: JSON from valq.py. Literals: OBX sample weights (11 Oct baseline), MSCI Norway top-10 weights (30 Sep 2026), blocks.
# Run: py -I valagg.py data/val.json 9.41      (second argument: USD/NOK on the price date)
import json, sys
q = json.load(open(sys.argv[1])); FX = float(sys.argv[2]) if len(sys.argv) > 2 else 9.41
OBX = {"EQNR": 16.1, "DNB": 10.4, "KOG": 7.3, "NHY": 6.7, "AKRBP": 6.2, "MOWI": 5.1, "STB": 4.9, "TEL": 4.7, "SUBC": 4.3, "YAR": 4.2,
       "ORK": 3.5, "GJF": 2.5, "FRO": 2.5, "VAR": 1.5}
MSCI = {"EQNR": 20.21, "DNB": 19.26, "KOG": 10.29, "AKRBP": 8.28, "NHY": 8.18, "MOWI": 6.81, "TEL": 6.08, "YAR": 5.17, "ORK": 5.10, "GJF": 3.98}
BLK = {"EQNR": "E", "AKRBP": "E", "VAR": "E", "SUBC": "E", "FRO": "E", "DNB": "F", "STB": "F", "GJF": "F"}   # the rest: O
# P/B quirk: Yahoo bookValue of a USD reporter may be in USD while the price is in NOK (Var Energi, 16 Oct 2026).
# Take the reading (price / BVPS or price / (BVPS x FX)) whose implied ROE (P/B / trailing P/E) is closer to Yahoo's ROE.
for s, o in q.items():
    a = o["price"]/o["bvps"]; b = o["price"]/(o["bvps"]*FX)
    o["pb_fix"] = a if (o["fccy"] != "USD" or abs(a/o["tpe"]-o["roe"]) <= abs(b/o["tpe"]-o["roe"])) else b
    if abs(o["pb_fix"]-o["pb"]) > 0.01: print(f"P/B fixed for {s}: Yahoo {o['pb']:.2f} -> {o['pb_fix']:.2f}")
def agg(W, lab):
    tw = sum(W.values()); g = lambda n, k: q[n+".OL"][k]
    book = sum(w/g(n, "pb_fix") for n, w in W.items()); earn = sum(w/g(n, "tpe") for n, w in W.items())
    fearn = sum(w/g(n, "fpe") for n, w in W.items()); roe_y = sum(w/g(n, "pb_fix")*g(n, "roe") for n, w in W.items())/book
    dy = sum(w*g(n, "dy") for n, w in W.items())/tw
    print(f"{lab:34s} cover {tw:6.1f}  P/B {tw/book:5.2f}  P/E trailing {tw/earn:5.2f} fwd {tw/fearn:5.2f}  ROE trailing {earn/book:6.1%}"
          f" fwd {fearn/book:6.1%} (Yahoo {roe_y:5.1%})  fwd div. yield {dy:6.2%}  dividend run rate / trailing EPS {dy/(earn/tw):5.0%}")
print("Per name:")
for n in OBX:
    o = q[n+".OL"]
    print(f" {n:6s} P/B {o['pb_fix']:6.2f}  P/E {o['tpe']:6.1f} / {o['fpe']:5.1f}  ROE {o['roe']:6.1%}  fwd div. yield {o['dy']:6.2%}  payout {o['payout']:5.0%}")
agg(OBX, "OBX sample weights (model)")
agg(MSCI, "MSCI Norway top-10 weights")
agg({n: q[n+".OL"]["mcap"]/1e9 for n in OBX}, "Market cap (14 names)")
for b in "EFO": agg({n: w for n, w in OBX.items() if BLK.get(n, "O") == b}, f"Block {b}")
agg({n: w for n, w in OBX.items() if n != "FRO"}, "Without Frontline")
agg({n: w for n, w in OBX.items() if n != "KOG"}, "Without Kongsberg")
agg({n: w for n, w in OBX.items() if n not in ("KOG", "GJF", "VAR")}, "Without Kongsberg, Gjensidige, Var")
