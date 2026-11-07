import json,sys,urllib.request,datetime as dt
out={}
D0,_,DL=sys.argv[1].partition(",")   # "<NAV date>[,<last date>]": the last close is taken on DL if given (v7)
for s in sys.argv[2:]:
    u=f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.request.quote(s)}?range=1mo&interval=1d"
    r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))["chart"]["result"][0]
    off=r["meta"].get("gmtoffset",0)
    rows=[((dt.datetime.fromtimestamp(t,dt.timezone.utc)+dt.timedelta(seconds=off)).strftime("%Y-%m-%d"),c) for t,c in zip(r["timestamp"],r["indicators"]["quote"][0]["close"]) if c]
    mt=r["meta"].get("regularMarketTime"); md=(dt.datetime.fromtimestamp(mt,dt.timezone.utc)+dt.timedelta(seconds=off)).strftime("%Y-%m-%d") if mt else None
    if DL and md==DL and not any(x[0]==DL for x in rows): rows.append((DL,r["meta"]["regularMarketPrice"]))   # bar still empty: the session's regular-market price (v7)
    d=dict(rows); lr=[r for r in rows if r[0]<=DL][-1] if DL else rows[-1]; out[s]={"14":d.get(D0),"9":d.get("2026-10-09") or d.get("2026-10-08"),"last":lr}
    print(f"{s:10s} {D0} {d.get(D0)}  9Oct {d.get('2026-10-09')}  8Oct {d.get('2026-10-08')}  last {lr}")
json.dump(out,open("closes.json","w"),indent=1)
