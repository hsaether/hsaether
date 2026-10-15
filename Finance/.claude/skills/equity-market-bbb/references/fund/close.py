import json,sys,urllib.request,datetime as dt
out={}
for s in sys.argv[2:]:
    u=f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.request.quote(s)}?range=1mo&interval=1d"
    r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))["chart"]["result"][0]
    off=r["meta"].get("gmtoffset",0)
    rows=[((dt.datetime.fromtimestamp(t,dt.timezone.utc)+dt.timedelta(seconds=off)).strftime("%Y-%m-%d"),c) for t,c in zip(r["timestamp"],r["indicators"]["quote"][0]["close"]) if c]
    d=dict(rows); out[s]={"14":d.get(sys.argv[1]),"9":d.get("2026-10-09") or d.get("2026-10-08"),"last":rows[-1]}
    print(f"{s:10s} {sys.argv[1]} {d.get(sys.argv[1])}  9Oct {d.get('2026-10-09')}  8Oct {d.get('2026-10-08')}  last {rows[-1]}")
json.dump(out,open("closes.json","w"),indent=1)
