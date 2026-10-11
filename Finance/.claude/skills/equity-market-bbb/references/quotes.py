import json, sys, urllib.request, http.cookiejar
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); op.addheaders=[("User-Agent","Mozilla/5.0")]
try: op.open("https://fc.yahoo.com", timeout=20)
except Exception as e: pass
crumb=op.open("https://query1.finance.yahoo.com/v1/test/getcrumb", timeout=20).read().decode()
syms=sys.argv[2:]
fields="symbol,shortName,marketCap,regularMarketPrice,trailingPE,forwardPE,priceToBook,dividendYield,trailingAnnualDividendYield,epsTrailingTwelveMonths,epsForward,bookValue,currency,financialCurrency,regularMarketTime"
url="https://query1.finance.yahoo.com/v7/finance/quote?symbols="+",".join(syms)+"&crumb="+crumb
d=json.load(op.open(url, timeout=30))
res=d["quoteResponse"]["result"]
json.dump(res, open(sys.argv[1],"w"))
got={r["symbol"] for r in res}; print("missing:", [s for s in syms if s not in got])
for r in res:
    print(f'{r["symbol"]:10s} {r.get("shortName","")[:22]:22s} mcap {r.get("marketCap",0)/1e9:8.1f} {r.get("currency")}/{r.get("financialCurrency")} P {r.get("regularMarketPrice")} tPE {r.get("trailingPE")} fPE {r.get("forwardPE")} PB {r.get("priceToBook")} dy {r.get("dividendYield")} tdy {r.get("trailingAnnualDividendYield")}')
