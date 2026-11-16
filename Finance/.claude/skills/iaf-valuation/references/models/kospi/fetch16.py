# IQQK / Korea (docs/kospi-analysis.md), version 1.9 (16 Nov 2026): Yahoo daily closes 9-16 Nov for the 47 Korean shares, the
# indices and IQQK.DE, plus 15-minute FX bars. Adds "closes_yahoo" dates and "index_fx_yahoo_16nov" to korea_prices.json.
# Usage: py fetch16.py   (run from this folder after the Seoul close)
import json, os, urllib.request, datetime as dt
HERE=os.path.dirname(os.path.abspath(__file__)); FN=os.path.join(HERE,"korea_prices.json")
X=json.load(open(FN))
def chart(s,rng="1mo",iv="1d"):
    u=f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.request.quote(s)}?range={rng}&interval={iv}"
    r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))["chart"]["result"][0]
    return r
def daily(s):
    r=chart(s); off=r["meta"].get("gmtoffset",0); q=r["indicators"]["quote"][0]
    rows={}
    for i,t in enumerate(r["timestamp"]):
        d=(dt.datetime.fromtimestamp(t,dt.timezone.utc)+dt.timedelta(seconds=off)).strftime("%Y-%m-%d")
        rows[d]=dict(o=q["open"][i],h=q["high"][i],l=q["low"][i],c=q["close"][i],v=q["volume"][i])
    m=r["meta"]; mt=m.get("regularMarketTime")
    meta=dict(price=m.get("regularMarketPrice"),time=dt.datetime.fromtimestamp(mt,dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC") if mt else None,
              prev=m.get("chartPreviousClose"),ccy=m.get("currency"))
    return rows,meta
NEW=["2026-11-09","2026-11-10","2026-11-11","2026-11-12","2026-11-13","2026-11-16"]
miss=[]
for s in X["closes_yahoo"]:
    try:
        rows,meta=daily(s)
        for d in NEW:
            if d in rows and rows[d]["c"]: X["closes_yahoo"][s][d]=rows[d]["c"]
            elif d=="2026-11-16" and meta["time"] and meta["time"].startswith("2026-11-16"): X["closes_yahoo"][s][d]=meta["price"]
        if "2026-11-16" not in X["closes_yahoo"][s]: miss.append(s)
        print(f"{s:10s} " + " ".join(f"{d[5:]} {X['closes_yahoo'][s].get(d)}" for d in NEW) + f" | meta {meta['price']} {meta['time']}")
    except Exception as e: print(s,"ERR",e); miss.append(s)
out={}
for s in ("^KS11","^KS200","IQQK.DE"):
    rows,meta=daily(s); out[s]={d:rows[d] for d in rows if d>="2026-11-04"}; out[s+"_meta"]=meta
    print(s, {d:(round(v['c'],2) if v['c'] else None) for d,v in out[s].items()}, meta)
fx={}
for s in ("KRW=X","NOK=X","EURKRW=X","EURNOK=X","EURUSD=X"):
    r=chart(s,"5d","15m"); q=r["indicators"]["quote"][0]["close"]
    bars={dt.datetime.fromtimestamp(t,dt.timezone.utc).strftime("%Y-%m-%d %H:%M"):c for t,c in zip(r["timestamp"],q) if c}
    keep={k:v for k,v in bars.items() if k[11:] in ("06:30","06:45","16:00") or k==max(bars)}
    fx[s]=keep; m=r["meta"]
    print(s, {k:round(v,4) for k,v in keep.items()}, "last", m.get("regularMarketPrice"))
out["fx_15m_utc"]=fx
out["note"]=("Seoul closes 15:30 KST of 9-16 Nov (Yahoo chart API, fetched 16 Nov after the Seoul close, "+dt.datetime.now(dt.timezone.utc).strftime("%H:%M UTC")+"). "
             "IQQK.DE daily bars (Xetra). FX: Yahoo 15-minute bars (UTC).")
X["index_fx_yahoo_16nov"]=out
json.dump(X,open(FN,"w"),indent=1)
print("missing 16 Nov:",miss)
