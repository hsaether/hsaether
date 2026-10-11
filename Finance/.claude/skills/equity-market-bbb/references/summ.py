import json, sys, urllib.request, http.cookiejar
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); op.addheaders=[("User-Agent","Mozilla/5.0")]
try: op.open("https://fc.yahoo.com", timeout=20)
except Exception: pass
crumb=op.open("https://query1.finance.yahoo.com/v1/test/getcrumb", timeout=20).read().decode()
for s in sys.argv[1:]:
    try:
        d=json.load(op.open(f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{s}?modules=topHoldings,fundProfile,summaryDetail,defaultKeyStatistics&crumb={crumb}", timeout=30))
        r=d["quoteSummary"]["result"][0]; th=r.get("topHoldings",{})
        eq=th.get("equityHoldings",{}); g=lambda x: x.get("raw") if isinstance(x,dict) else x
        print("\n==",s, "PE",g(eq.get("priceToEarnings")),"PB",g(eq.get("priceToBook")),"PS",g(eq.get("priceToSales")),"PCF",g(eq.get("priceToCashflow")),"3yEPSgr",g(eq.get("threeYearEarningsGrowth")))
        sd=r.get("summaryDetail",{}); print(" yield",g(sd.get("yield")),"trailPE",g(sd.get("trailingPE")),"navPrice",g(sd.get("navPrice")))
        print(" sectors:", {k:round(g(v)*100,1) for w in th.get("sectorWeightings",[]) for k,v in w.items() if g(v)})
        print(" top:", [(h.get("symbol"),round(g(h.get("holdingPercent"))*100,1)) for h in th.get("holdings",[])])
    except Exception as e: print(s,"ERR",e)
