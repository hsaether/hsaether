import json, sys, urllib.request, time, datetime as dt
for s in sys.argv[1:]:
    url = "https://query1.finance.yahoo.com/v8/finance/chart/" + urllib.request.quote(s) + "?period1=946684800&period2=" + str(int(time.time())) + "&interval=1d"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=60))
    r = d["chart"]["result"][0]
    q = r["indicators"]["quote"][0]["close"]; adj = r["indicators"].get("adjclose",[{}])[0].get("adjclose", q)
    me = {}
    for t,c,a in zip(r["timestamp"], q, adj):
        if c is None: continue
        x = dt.datetime.fromtimestamp(t, dt.timezone.utc) + dt.timedelta(hours=r["meta"].get("gmtoffset",0)/3600)
        me[f"{x.year}-{x.month:02d}"] = (c,a)
    json.dump(me, open("data/long_"+s.replace("^","_").replace("=","_")+".json","w")); print(s, min(me), max(me), len(me))
