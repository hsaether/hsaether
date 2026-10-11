import json, sys, urllib.request, http.cookiejar
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); op.addheaders=[("User-Agent","Mozilla/5.0")]
try: op.open("https://fc.yahoo.com", timeout=20)
except Exception: pass
crumb=op.open("https://query1.finance.yahoo.com/v1/test/getcrumb", timeout=20).read().decode()
g=lambda x: x.get("raw") if isinstance(x,dict) else x
for s in sys.argv[1:]:
    try:
        d=json.load(op.open(f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{s}?modules=earningsTrend,earnings,price&crumb={crumb}", timeout=30))
        r=d["quoteSummary"]["result"][0]
        rows=[(t.get("period"),t.get("endDate"),g(t.get("earningsEstimate",{}).get("avg")),g(t.get("earningsEstimate",{}).get("yearAgoEps")),g(t.get("earningsEstimate",{}).get("numberOfAnalysts")),g(t.get("growth"))) for t in r.get("earningsTrend",{}).get("trend",[]) if t.get("period") in ("0y","+1y")]
        ann=[(y.get("date"),g(y.get("earnings"))) for y in r.get("earnings",{}).get("financialsChart",{}).get("yearly",[])]
        print(s, r.get("earnings",{}).get("financialCurrency"), rows, "annual earnings:", ann)
    except Exception as e: print(s,"ERR",e)
