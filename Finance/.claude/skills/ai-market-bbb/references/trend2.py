import json, sys, urllib.request, http.cookiejar
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); op.addheaders=[("User-Agent","Mozilla/5.0")]
try: op.open("https://fc.yahoo.com", timeout=20)
except Exception: pass
crumb=op.open("https://query1.finance.yahoo.com/v1/test/getcrumb", timeout=20).read().decode()
g=lambda x: x.get("raw") if isinstance(x,dict) else x
for s in sys.argv[1:]:
    try:
        d=json.load(op.open(f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{s}?modules=earningsTrend&crumb={crumb}", timeout=30))
        r=d["quoteSummary"]["result"][0]
        for t in r["earningsTrend"]["trend"]:
            e=t.get("earningsEstimate",{}); v=t.get("revenueEstimate",{})
            print(f'{s:10s} {t.get("period"):4s} end {t.get("endDate")} EPS {g(e.get("avg"))} yrAgo {g(e.get("yearAgoEps"))} n {g(e.get("numberOfAnalysts"))} | Rev {g(v.get("avg"))} yrAgo {g(v.get("yearAgoRevenue"))}')
    except Exception as ex: print(s,"ERR",ex)
