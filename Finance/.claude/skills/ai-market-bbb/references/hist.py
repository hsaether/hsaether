import json,sys,urllib.request,datetime
op=urllib.request.build_opener(); op.addheaders=[("User-Agent","Mozilla/5.0")]
for s in sys.argv[1:]:
    try:
        d=json.load(op.open(f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?range=3mo&interval=1d",timeout=30))["chart"]["result"][0]
        ts=d["timestamp"]; c=d["indicators"]["quote"][0]["close"]
        rows=[(datetime.datetime.utcfromtimestamp(t+d["meta"].get("gmtoffset",0)).strftime("%m-%d"),x) for t,x in zip(ts,c) if x]
        hi=max(x for _,x in rows); hd=[a for a,x in rows if x==hi][0]
        last=rows[-1][1]
        print(f"{s:10s} hi {hi:.1f} ({hd}) last {last:.1f} vs hi {last/hi*100-100:+.1f}% | "+" ".join(f"{a}:{x:.0f}" if x>100 else f"{a}:{x:.2f}" for a,x in rows[-12:]))
    except Exception as e: print(s,"ERR",e)
