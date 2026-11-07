# Parse iShares URTH holdings CSV -> dl2/urth_ai_nov.json (weights of the AI basket names, energy weight, total, prices)
import csv, json, sys
rows = list(csv.reader(open(sys.argv[1], encoding="utf-8-sig")))
hdr_i = next(i for i, r in enumerate(rows) if r and r[0] == "Ticker"); hdr = rows[hdr_i]
asof = [r for r in rows[:hdr_i] if r and r[0].startswith("Fund Holdings")][0][1]
num = lambda s: float(s.replace(",", "")) if s not in ("-", "") else 0.0
eq = [dict(zip(hdr, r)) for r in rows[hdr_i+1:] if len(r) == len(hdr) and r[3] == "Equity"]
tot = sum(num(r["Weight (%)"]) for r in eq)
want = {"NVDA": "United States", "MSFT": "United States", "AMZN": "United States", "GOOGL": "United States", "AVGO": "United States", "GOOG": "United States",
        "META": "United States", "MU": "United States", "TSLA": "United States", "AMD": "United States", "ASML": "Netherlands", "PLTR": "United States",
        "AMAT": "United States", "LRCX": "United States", "ORCL": "United States", "MRVL": "United States", "ANET": "United States", "SAP": "Germany",
        "CRM": "United States", "ETN": "United States", "NOW": "United States", "SNOW": "United States", "ADBE": "United States", "DDOG": "United States",
        "VRT": "United States", "INTU": "United States", "AAPL": "United States"}
w = {}; px = {}
for r in eq:
    t = r["Ticker"]
    if t in want and r["Location"] == want[t]:
        w[t] = w.get(t, 0) + num(r["Weight (%)"]); px[t] = num(r["Price"])
en = sum(num(r["Weight (%)"]) for r in eq if r["Sector"] == "Energy")
sec = {}
for r in eq: sec[r["Sector"]] = sec.get(r["Sector"], 0) + num(r["Weight (%)"])
top10 = sorted(((num(r["Weight (%)"]), r["Ticker"], r["Location"]) for r in eq), reverse=True)[:10]
print("as of", asof, "equity rows", len(eq), "total", round(tot, 2), "energy", round(en, 2))
print("missing:", [t for t in want if t not in w])
print({k: round(v, 3) for k, v in sorted(w.items(), key=lambda x: -x[1])})
print("sectors:", {k: round(v, 2) for k, v in sorted(sec.items(), key=lambda x: -x[1])})
print("top10:", [(t, round(x, 2)) for x, t, l in top10], "sum", round(sum(x for x, _, _ in top10), 2))
json.dump({"asof": asof, "w": w, "px": px, "total": round(tot, 4), "energy": round(en, 4), "sectors": sec}, open(sys.argv[2], "w"), indent=1)
