import json, sys, urllib.request, http.cookiejar
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); op.addheaders=[("User-Agent","Mozilla/5.0")]
try: op.open("https://fc.yahoo.com", timeout=20)
except Exception: pass
crumb=op.open("https://query1.finance.yahoo.com/v1/test/getcrumb", timeout=20).read().decode()
g=lambda x: x.get("raw") if isinstance(x,dict) else x
out={}
for s in sys.argv[1:]:
    try:
        d=json.load(op.open(f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{s}?modules=earningsTrend,price,summaryDetail,defaultKeyStatistics,financialData&crumb={crumb}", timeout=30))
        r=d["quoteSummary"]["result"][0]
        tr={t.get("period"):dict(end=t.get("endDate"),eps=g(t.get("earningsEstimate",{}).get("avg")),ya=g(t.get("earningsEstimate",{}).get("yearAgoEps")),n=g(t.get("earningsEstimate",{}).get("numberOfAnalysts")),gr=g(t.get("growth"))) for t in r.get("earningsTrend",{}).get("trend",[])}
        pr=r.get("price",{}); sd=r.get("summaryDetail",{}); ks=r.get("defaultKeyStatistics",{}); fd=r.get("financialData",{})
        o=dict(px=g(pr.get("regularMarketPrice")),ccy=pr.get("currency"),fccy=fd.get("financialCurrency"),t=g(pr.get("regularMarketTime")),mcap=g(pr.get("marketCap")),
               tpe=g(sd.get("trailingPE")),fpe=g(sd.get("forwardPE")) or g(ks.get("forwardPE")),dy=g(sd.get("dividendYield")),pb=g(ks.get("priceToBook")),
               fye=g(ks.get("lastFiscalYearEnd")),roe=g(fd.get("returnOnEquity")),fcf=g(fd.get("freeCashflow")),pm=g(fd.get("profitMargins")),tr=tr)
        out[s]=o
        y0=tr.get("0y",{}); y1=tr.get("+1y",{}); l5=tr.get("+5y",{}) or tr.get("LTG",{})
        print(f"{s:10s} {o['ccy']}/{o['fccy']} px {o['px']} tPE {o['tpe']} fPE {o['fpe']} dy {o['dy']} | 0y {y0.get('end')} {y0.get('eps')} (ya {y0.get('ya')}, n{y0.get('n')}) +1y {y1.get('end')} {y1.get('eps')} (n{y1.get('n')}) | +5y {l5.get('gr')}")
    except Exception as e: print(s,"ERR",e)
json.dump(out,open("hold.json","w"),indent=1)
