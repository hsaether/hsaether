import json
q = json.load(open("data/val.json")); W = json.load(open("data/obxw.json"))["W"]
BLK = {"EQNR": "E", "AKRBP": "E", "VAR": "E", "SUBC": "E", "FRO": "E", "DNB": "F", "STB": "F", "GJF": "F"}
FX = {"NOK": 1, "USD": 9.2944, "EUR": 10.442}
C27 = {"EQNR": (4.65483, "USD"), "AKRBP": (3.38032, "USD"), "VAR": (0.60791, "USD"), "SUBC": (2.69132, "USD"), "FRO": (7.30763, "USD"), "DNB": (28.44148, "NOK"),
       "STB": (13.52433, "NOK"), "GJF": (17.47045, "NOK"), "KOG": (11.41755, "NOK"), "NHY": (7.55935, "NOK"), "MOWI": (1.43753, "EUR"), "TEL": (9.19243, "NOK"),
       "YAR": (40.50239, "NOK"), "ORK": (6.85612, "NOK")}
def blk(ex=()):
    out = {}
    for b in "EFO":
        ns = [n for n in W if BLK.get(n, "O") == b and n not in ex]
        g = lambda n, k: q[n+".OL"][k]
        et = sum(W[n]/g(n, "tpe") for n in ns); e27 = sum(W[n]*C27[n][0]*FX[C27[n][1]]/g(n, "price") for n in ns); dv = sum(W[n]*g(n, "dy") for n in ns)
        paid = sum(W[n]/g(n, "tpe")*g(n, "payout") for n in ns)
        out[b] = (dv/et, paid/et, dv/e27)
    return out
for lab, ex in [("all", ()), ("without FRO", ("FRO",)), ("without TEL", ("TEL",)), ("without FRO, TEL", ("FRO", "TEL"))]:
    o = blk(ex); print(lab, {b: tuple(round(x, 2) for x in v) for b, v in o.items()}, "(run rate / trailing EPS, Yahoo paid payout, run rate / CY27 consensus)")
