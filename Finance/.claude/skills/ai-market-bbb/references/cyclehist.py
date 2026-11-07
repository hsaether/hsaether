# Past-cycle share prices (Yahoo chart API, daily closes): high and low with dates in a window.
# Usage: py -I cyclehist.py <ticker> <from YYYY-MM-DD> <to YYYY-MM-DD>   (Memory cycle section, table 2)
import json,sys,urllib.request,datetime
op=urllib.request.build_opener(); op.addheaders=[("User-Agent","Mozilla/5.0")]
s=sys.argv[1]; a=sys.argv[2]; b=sys.argv[3]
p1=int(datetime.datetime.fromisoformat(a).timestamp()); p2=int(datetime.datetime.fromisoformat(b).timestamp())
d=json.load(op.open(f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?period1={p1}&period2={p2}&interval=1d",timeout=30))["chart"]["result"][0]
ts=d["timestamp"]; c=d["indicators"]["quote"][0]["close"]; adj=d["indicators"].get("adjclose",[{}])[0].get("adjclose",c)
rows=[(datetime.datetime.fromtimestamp(t+d["meta"].get("gmtoffset",0), datetime.timezone.utc).strftime("%Y-%m-%d"),x,y) for t,x,y in zip(ts,c,adj) if x]
hi=max(rows,key=lambda r:r[1]); lo=min(rows,key=lambda r:r[1])
print(s,a,b,"high",hi[0],round(hi[1],2),"low",lo[0],round(lo[1],2),"first",rows[0][0],round(rows[0][1],2),"last",rows[-1][0],round(rows[-1][1],2))
