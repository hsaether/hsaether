"""SPY options read for the Equity BBB leading-view note (20 Nov 2026). Uses oil-market-bbb/references/futures.py chain() and dist().
Percentiles and odds of the price change from spot to the expiry (forward with r 4%, dividend yield 1.2% [A])."""
import sys, math, datetime as dt
sys.path.insert(0, r"C:\GitWrk\hsaether\Finance\.claude\skills\oil-market-bbb\references")
import futures as F
op, crumb = F.opener()
now = dt.datetime(2026, 11, 20, 21)
res = F.chain(op, crumb, "SPY", now)
S = res[0]["S"]; print("SPY", S, "expiries", [r["exp"] for r in res])
for want in ("2027-06", "2027-12", "2028-12"):
    c = [r for r in res if r["exp"].startswith(want) and r["fit"]]
    if not c: print(want, "none"); continue
    r = max(c, key=lambda x: x["n"]); T = r["T"]; Fw = S*math.exp((0.04-0.012)*T)
    lv = [S*x for x in (0.77, 0.80, 0.90, 1.00, 1.09, 1.10, 1.22)]
    pct, pr = F.dist(Fw, T, r["fit"], lv)
    print(f"{r['exp']} T {T:.2f} n {r['n']} ATM {r['atm']*100:.1f}% skew {r['skew']*100:+.1f}pp F {Fw:.1f}")
    print("  pct (price change vs spot):", {q: f"{(v/S-1)*100:+.0f}%" for q, v in pct.items()})
    print("  P(<=):", {f"{x/S-1:+.0%}": f"{p*100:.0f}%" for x, p in pr.items()})
