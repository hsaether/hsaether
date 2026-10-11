import json, sys, urllib.request, time, datetime as dt
for s in sys.argv[1:]:
    url = "https://query1.finance.yahoo.com/v8/finance/chart/" + urllib.request.quote(s) + "?period1=1356998400&period2=" + str(int(time.time())) + "&interval=1d&events=div"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=60))
    r = d["chart"]["result"][0]
    q = r["indicators"]["quote"][0]["close"]; adj = r["indicators"].get("adjclose",[{}])[0].get("adjclose", q)
    me = {}; daily=[]
    for t,c,a in zip(r["timestamp"], q, adj):
        if c is None: continue
        x = dt.datetime.fromtimestamp(t, dt.timezone.utc) + dt.timedelta(hours=r["meta"].get("gmtoffset",0)/3600)
        me[(x.year,x.month)] = (c,a); daily.append((x.strftime("%Y-%m-%d"),c,a))
    json.dump({"sym":s,"me":{f"{y}-{m:02d}":v for (y,m),v in me.items()},"daily":daily,"div":r.get("events",{}).get("dividends",{})}, open("data/d_"+s.replace("^","_").replace("=","_")+".json","w"))
    print(s, len(me), daily[0], daily[-1])
