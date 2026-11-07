import json, sys, urllib.request, datetime as dt
out = {}
for s in sys.argv[2:]:
    url = "https://query1.finance.yahoo.com/v8/finance/chart/" + urllib.request.quote(s) + "?range=1mo&interval=1d"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60))
    r = d["chart"]["result"][0]; off = r["meta"].get("gmtoffset", 0)
    rows = [((dt.datetime.fromtimestamp(t, dt.timezone.utc)+dt.timedelta(seconds=off)).strftime("%Y-%m-%d"), c) for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c is not None]
    out[s] = dict(rows); print(s, rows[-3:], "regularMarketTime", dt.datetime.fromtimestamp(r["meta"]["regularMarketTime"], dt.timezone.utc))
json.dump(out, open(sys.argv[1], "w"), indent=0)
