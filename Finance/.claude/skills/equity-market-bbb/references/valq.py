# Bottom-up fundamentals per name (Yahoo quoteSummary with crumb): price, currencies, book value per share, P/B, ROE,
# dividend yield (latest declared, annualised; a fraction here), trailing dividend rate, P/E, payout. Output JSON for valagg.py.
# Run: py -I valq.py data/val.json EQNR.OL DNB.OL ...   (Equity BBB skill 2026-10-18.1)
import json, sys, urllib.request, http.cookiejar
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); op.addheaders=[("User-Agent","Mozilla/5.0")]
try: op.open("https://fc.yahoo.com", timeout=20)
except Exception: pass
crumb=op.open("https://query1.finance.yahoo.com/v1/test/getcrumb", timeout=20).read().decode()
g=lambda x: x.get("raw") if isinstance(x,dict) else x
out={}
for s in sys.argv[2:]:
    try:
        d=json.load(op.open(f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{s}?modules=price,summaryDetail,defaultKeyStatistics,financialData&crumb={crumb}", timeout=30))
        r=d["quoteSummary"]["result"][0]
        pr,sd,ks,fd=r.get("price",{}),r.get("summaryDetail",{}),r.get("defaultKeyStatistics",{}),r.get("financialData",{})
        o=dict(price=g(pr.get("regularMarketPrice")),ccy=pr.get("currency"),fccy=fd.get("financialCurrency"),mcap=g(pr.get("marketCap")),
               bvps=g(ks.get("bookValue")),pb=g(ks.get("priceToBook")),roe=g(fd.get("returnOnEquity")),
               dy=g(sd.get("dividendYield")),dr=g(sd.get("dividendRate")),tdr=g(sd.get("trailingAnnualDividendRate")),tdy=g(sd.get("trailingAnnualDividendYield")),
               t5dy=g(sd.get("fiveYearAvgDividendYield")),tpe=g(sd.get("trailingPE")),fpe=g(sd.get("forwardPE")),
               eps_ttm=g(ks.get("trailingEps")),payout=g(sd.get("payoutRatio")),shares=g(ks.get("sharesOutstanding")),ni=g(ks.get("netIncomeToCommon")),
               mrq=g(ks.get("mostRecentQuarter")),time=g(pr.get("regularMarketTime")))
        out[s]=o
        print(s, {k:v for k,v in o.items()})
    except Exception as e: print(s,"ERR",e)
json.dump(out, open(sys.argv[1],"w"), indent=1)
