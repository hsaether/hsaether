"""Oil Market BBB — what the futures and options markets say (skill 2026-11-18.2, Step 1c).

Standard library only. Run: py -I futures.py [out.json] [--bear 65,60,60] [--base 84,77,72] [--bull 118,102,90]
                                             [--crack 70,48,33]

1. Strips (Yahoo, NYMEX BZ = ICE Brent, CL = WTI, HO = ULSD), every listed month to Dec 2030 where quoted:
   annual averages per window year, December contracts, M1-M4 and M1-M12, Dec-Dec spreads,
   ULSD crack (HO x 42 - BZ, same month) per year, Brent-WTI per year. Months whose last trade is
   older than 5 days are flagged stale and left out of the averages (the skill's Barchart route
   fills them; pass them in by hand if needed).
2. Options on the Brent ETF (BNO) and the WTI ETF (USO): own Black-Scholes implied vol from mid
   prices per strike, a quadratic smile in log-moneyness per expiry, and from it the market-implied
   (risk-neutral) distribution of Brent at each expiry, applied to the Brent contract for that month
   (same log-moneyness and vol as the ETF, an approximation [A]): percentiles 10/25/50/75/90 and the
   probability of ending at or below the Bear level / at or above the Bull level of that year.
   Point-in-time prices are wider than annual averages: read the percentiles as the outer bound of
   what an annual average can do.
3. Skew: 25-delta-style put vol (k = -0.2) minus call vol (k = +0.2) per expiry: which tail the
   market pays for.
4. OVX (CBOE crude oil vol index, 30-day WTI) for the front-end vol regime.
Outputs a JSON with all raw and derived values and prints the tables used in the baseline.
"""
import json, math, sys, urllib.request, http.cookiejar, datetime as dt

MONTHS = 'FGHJKMNQUVXZ'
YEARS = (2026, 2027, 2028, 2029, 2030)
WINDOW = (2027, 2028, 2029)
R = 0.04  # USD rate for option pricing [A]

def opener():
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    op.addheaders = [("User-Agent", "Mozilla/5.0")]
    try: op.open("https://fc.yahoo.com", timeout=20)
    except Exception: pass
    crumb = op.open("https://query1.finance.yahoo.com/v1/test/getcrumb", timeout=20).read().decode()
    return op, crumb

def quotes(op, crumb, syms):
    out = {}
    for i in range(0, len(syms), 40):
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=" + ",".join(syms[i:i+40]) + "&crumb=" + crumb
        for r in json.load(op.open(url, timeout=30))["quoteResponse"]["result"]:
            out[r["symbol"]] = r
    return out

def strip(q, root, now):
    rows = []
    for y in YEARS:
        for m, c in enumerate(MONTHS, 1):
            s = f"{root}{c}{str(y)[2:]}.NYM"
            r = q.get(s)
            if not r or r.get("regularMarketPrice") is None: continue
            t = dt.datetime.utcfromtimestamp(r.get("regularMarketTime", 0))
            p = r["regularMarketPrice"] * (42 if root == "HO" else 1)
            rows.append(dict(sym=s, year=y, month=m, price=p, time=t.strftime("%Y-%m-%d %H:%M"),
                             stale=(now - t).days > 5, oi=r.get("openInterest")))
    return rows

def ncdf(x): return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def bs(S, K, T, s, call=True):
    if s <= 0 or T <= 0: return max(0.0, (S - K) if call else (K - S))
    d1 = (math.log(S / K) + (R + s * s / 2) * T) / (s * math.sqrt(T)); d2 = d1 - s * math.sqrt(T)
    return S * ncdf(d1) - K * math.exp(-R * T) * ncdf(d2) if call else K * math.exp(-R * T) * ncdf(-d2) - S * ncdf(-d1)

def iv(S, K, T, price, call):
    lo, hi = 0.01, 3.0
    if price <= max(0.0, (S - K * math.exp(-R * T)) if call else (K * math.exp(-R * T) - S)) + 1e-6: return None
    for _ in range(100):
        m = (lo + hi) / 2
        if bs(S, K, T, m, call) < price: lo = m
        else: hi = m
    return m

def fitq(xs, ys):  # least squares y = a + b x + c x^2
    n = len(xs)
    if n < 3: return None
    S = [[sum(x ** (i + j) for x in xs) for j in range(3)] for i in range(3)]
    b = [sum(y * x ** i for x, y in zip(xs, ys)) for i in range(3)]
    for i in range(3):  # Gauss
        p = S[i][i]
        if abs(p) < 1e-12: return None
        for j in range(i + 1, 3):
            f = S[j][i] / p
            for k in range(3): S[j][k] -= f * S[i][k]
            b[j] -= f * b[i]
    c = [0, 0, 0]
    for i in (2, 1, 0):
        c[i] = (b[i] - sum(S[i][k] * c[k] for k in range(i + 1, 3))) / S[i][i]
    return c

def chain(op, crumb, sym, now):
    base = f"https://query2.finance.yahoo.com/v7/finance/options/{sym}?crumb={crumb}"
    d = json.load(op.open(base, timeout=30))["optionChain"]["result"][0]
    S = d["quote"]["regularMarketPrice"]
    res = []
    for e in d.get("expirationDates", []):
        T = (dt.datetime.utcfromtimestamp(e) - now).days / 365
        if T < 0.15: continue
        c = json.load(op.open(base + f"&date={e}", timeout=30))["optionChain"]["result"][0]["options"][0]
        pts = []
        for typ, call in (("calls", True), ("puts", False)):
            for o in c.get(typ, []):
                K = o["strike"]; bid, ask = o.get("bid") or 0, o.get("ask") or 0
                if bid <= 0 or ask <= 0 or ask < bid: continue
                k = math.log(K / (S * math.exp(R * T)))
                if (call and k < -0.05) or ((not call) and k > 0.05): continue  # OTM side only
                v = iv(S, K, T, (bid + ask) / 2, call)
                if v and 0.05 < v < 2.0 and abs(k) < 0.8: pts.append((k, v, K, o.get("openInterest") or 0))
        fit = fitq([p[0] for p in pts], [p[1] for p in pts])
        res.append(dict(exp=dt.datetime.utcfromtimestamp(e).strftime("%Y-%m-%d"), T=T, S=S, n=len(pts), fit=fit,
                        atm=None if not fit else fit[0], skew=None if not fit else (fit[0] - .2*fit[1] + .04*fit[2]) - (fit[0] + .2*fit[1] + .04*fit[2])))
    return res

def dist(F, T, fit, levels):
    """Risk-neutral P(F_T <= L) from the smile, by finite difference of undiscounted call prices."""
    def sig(K):
        k = math.log(K / F); return max(0.05, fit[0] + fit[1] * k + fit[2] * k * k)
    def C(K):
        s = sig(K); d1 = (math.log(F / K) + s * s * T / 2) / (s * math.sqrt(T)); d2 = d1 - s * math.sqrt(T)
        return F * ncdf(d1) - K * ncdf(d2)
    def P(K, h=0.01):
        h = K * h; return 1 + (C(K + h) - C(K - h)) / (2 * h)
    pct = {}
    for q in (0.10, 0.25, 0.50, 0.75, 0.90):
        lo, hi = F * 0.2, F * 4
        for _ in range(80):
            m = (lo + hi) / 2
            if P(m) < q: lo = m
            else: hi = m
        pct[q] = m
    return pct, {L: P(L) for L in levels}

def main():
    args = sys.argv[1:]
    out_path = args[0] if args and not args[0].startswith('--') else 'futures_out.json'
    def opt(name, default):
        if name in args: return [float(x) for x in args[args.index(name) + 1].split(',')]
        return default
    bear, base, bull = opt('--bear', [65, 60, 60]), opt('--base', [84, 77, 72]), opt('--bull', [118, 102, 90])
    crack_base = opt('--crack', [70, 48, 33])
    now = dt.datetime.utcnow()
    op, crumb = opener()
    syms = [f"{r}{c}{str(y)[2:]}.NYM" for r in ("BZ", "CL", "HO") for y in YEARS for c in MONTHS] + ["^OVX", "BNO", "USO"]
    q = quotes(op, crumb, syms)
    S = {r: strip(q, r, now) for r in ("BZ", "CL", "HO")}
    def get(root, y, m):
        for r in S[root]:
            if r["year"] == y and r["month"] == m and not r["stale"]: return r["price"]
    out = dict(asof=now.strftime("%Y-%m-%d %H:%M UTC"), strips=S, ovx=q.get("^OVX", {}).get("regularMarketPrice"))
    live = [r for r in S["BZ"] if not r["stale"]]
    m1 = live[0]["price"] if live else None
    out["m1"] = live[0]["sym"] if live else None
    out["m1_m4"] = m1 - live[3]["price"] if len(live) > 3 else None
    out["m1_m12"] = m1 - live[11]["price"] if len(live) > 11 else None
    # Monthly series per root with gaps (stale or outlier prints) filled by linear interpolation
    # between live contracts [A]; an outlier is a live print > 3% off the line through its live
    # neighbours (thin deferred months on Yahoo, e.g. BZV27 on 18 Nov).
    def series(root):
        keep = sorted(((r["year"] * 12 + r["month"] - 1), r["price"]) for r in S[root] if not r["stale"])
        while len(keep) > 2:  # drop the worst outlier, then re-test
            dev = []
            for i in range(1, len(keep) - 1):
                (t0, p0), (t, p), (t1, p1) = keep[i - 1], keep[i], keep[i + 1]
                dev.append((abs(p / (p0 + (p1 - p0) * (t - t0) / (t1 - t0)) - 1), i))
            worst = max(dev) if dev else (0, None)
            if worst[0] <= 0.03: break
            t, p = keep.pop(worst[1]); out.setdefault("outliers", []).append((root, t // 12, t % 12 + 1, p))
        def at(t):
            for (a, pa), (b, pb) in zip(keep, keep[1:]):
                if a <= t <= b: return pa + (pb - pa) * (t - a) / (b - a)
            return None
        return at, keep
    ser = {r: series(r) for r in ("BZ", "CL", "HO")}
    ann = {}
    for y in WINDOW + (2030,):
        # front-month basis (SKILL Benchmarks): calendar month m reads Brent m+2, ULSD and WTI m+1
        b = [ser["BZ"][0](y * 12 + m + 2) for m in range(12)]
        h = [ser["HO"][0](y * 12 + m + 1) for m in range(12)]
        w = [ser["CL"][0](y * 12 + m + 1) for m in range(12)]
        ok = all(x is not None for x in b)
        live = sum(1 for m in range(12) if any(t == y * 12 + m + 2 for t, _ in ser["BZ"][1]))
        cr = [hh - bz for hh, bz in zip(h, b) if hh is not None and bz is not None]
        bw = [bz - ww for bz, ww in zip(b, w) if bz is not None and ww is not None]
        ann[y] = dict(brent=sum(b) / 12 if ok else None, n=live, dec=get("BZ", y, 12),
                      crack=sum(cr) / len(cr) if len(cr) == 12 else None, n_crack=len(cr),
                      brent_wti=sum(bw) / len(bw) if len(bw) == 12 else None,
                      quarters=[sum(b[q*3:q*3+3]) / 3 for q in range(4)] if ok else None)
    out["annual"] = ann
    print("outliers dropped:", out.get("outliers", []))
    out["dec_dec"] = {f"{y}-{y+1}": (ann[y]["dec"] - ann[y + 1]["dec"]) if ann[y]["dec"] and ann.get(y + 1, {}).get("dec") else None for y in (2027, 2028, 2029)}
    print(f"as of {out['asof']}; front {out['m1']} {m1:.2f}; M1-M4 {out['m1_m4']:+.2f}; M1-M12 {out['m1_m12']:+.2f}; OVX {out['ovx']}")
    print("year | Brent avg (n) | Base | gap | Dec | ULSD crack avg (n) | crack Base | gap | Brent-WTI")
    for i, y in enumerate(WINDOW):
        a = ann[y]
        fb = f"{a['brent']:.2f} ({a['n']})" if a['brent'] else "n/a"
        fc = f"{a['crack']:.2f} ({a['n_crack']})" if a['crack'] else "n/a"
        gb = f"{base[i] - a['brent']:+.1f}" if a['brent'] else "-"
        gc = f"{crack_base[i] - a['crack']:+.1f}" if a['crack'] else "-"
        print(f"{y} | {fb} | {base[i]} | {gb} | {a['dec']} | {fc} | {crack_base[i]} | {gc} | {a['brent_wti']}")
    print("Dec-Dec spreads:", {k: (round(v, 2) if v else None) for k, v in out["dec_dec"].items()})
    stale = [r["sym"] for r in S["BZ"] + S["HO"] if r["stale"] and r["year"] <= 2029]
    print("stale months (left out):", stale)
    # options
    out["options"] = {}
    for etf in ("BNO", "USO"):
        try: ch = chain(op, crumb, etf, now)
        except Exception as e: print(etf, "options failed", e); continue
        out["options"][etf] = ch
        print(f"{etf} options: expiry | T | n | ATM vol | skew (put - call vol at k=-/+0.2)")
        for c in ch:
            print(f"  {c['exp']} | {c['T']:.2f} | {c['n']} | {c['atm'] if c['atm'] is None else round(c['atm']*100,1)}% | {c['skew'] if c['skew'] is None else round(c['skew']*100,1)} pp")
    # Brent distributions from BNO: apply each long expiry to the Brent contract of that month
    out["implied"] = []
    for c in out["options"].get("BNO", []):
        if not c["fit"] or c["T"] < 0.3: continue
        e = dt.datetime.strptime(c["exp"], "%Y-%m-%d")
        y, m = e.year, e.month
        F = get("BZ", y, m) or get("BZ", y - 1, 12)
        if not F: continue
        yi = (y - 1) - 2027 if m <= 2 else y - 2027  # a Jan expiry reads the year just ended
        if not 0 <= yi < 3: continue
        lv = [bear[yi], base[yi], bull[yi]]
        pct, pr = dist(F, c["T"], c["fit"], lv)
        row = dict(exp=c["exp"], F=F, T=c["T"], reads_year=2027 + yi, pct={str(k): v for k, v in pct.items()},
                   p_le_bear=pr[bear[yi]], p_le_base=pr[base[yi]], p_ge_bull=1 - pr[bull[yi]])
        out["implied"].append(row)
        print(f"Brent at {c['exp']} (F {F:.2f}, reads {2027 + yi}): p10 {pct[.1]:.0f} p25 {pct[.25]:.0f} p50 {pct[.5]:.0f} p75 {pct[.75]:.0f} p90 {pct[.9]:.0f} | "
              f"P(<= Bear {bear[yi]}) {pr[bear[yi]]*100:.0f}% | P(<= Base {base[yi]}) {pr[base[yi]]*100:.0f}% | P(>= Bull {bull[yi]}) {(1-pr[bull[yi]])*100:.0f}%")
    json.dump(out, open(out_path, "w"), default=str, indent=1)

def black76(F, K, T, s, call):
    d1 = (math.log(F / K) + s * s * T / 2) / (s * math.sqrt(T)); d2 = d1 - s * math.sqrt(T)
    df = math.exp(-R * T)
    return df * (F * ncdf(d1) - K * ncdf(d2)) if call else df * (K * ncdf(-d2) - F * ncdf(-d1))

def iv76(F, K, T, p, call):
    lo, hi = 0.02, 3.0
    if p <= max(0.0, math.exp(-R * T) * ((F - K) if call else (K - F))) + 1e-6: return None
    for _ in range(100):
        m = (lo + hi) / 2
        if black76(F, K, T, m, call) < p: lo = m
        else: hi = m
    return m

def chains_main(path, today, levels):
    """Barchart ICE Brent futures options (the preferred source: options on the contract itself, no ETF
    roll or Samuelson distortion). Input lines 'CODE|F|days|expiry|BarchartIV|PutCallPremiumRatio|<K><C|P><price> ...'
    as returned by the extractor in SKILL Data sources. levels: {code: (bear, base, bull)}.
    Prints per contract: ATM vol, skew (vol at K = 0.8F minus 1.2F), percentiles and the implied odds."""
    res = []
    for line in open(path, encoding='utf-8'):
        if not line.strip() or line.startswith('#'): continue
        code, F, days, exp, bciv, pcr, rows = line.strip().split('|')
        F = float(F); T = (dt.datetime.strptime(exp, "%m/%d/%y") - today).days / 365
        pts = []
        for tok in rows.split():
            typ = 'C' if 'C' in tok else 'P'; K, p = tok.split(typ); K, p = float(K), float(p)
            v = iv76(F, K, T, p, typ == 'C')
            if v and 0.05 < v < 1.5: pts.append((math.log(K / F), v))
        fit = fitq([x for x, _ in pts], [y for _, y in pts])
        sig = lambda k: fit[0] + fit[1] * k + fit[2] * k * k
        skew = sig(math.log(0.8)) - sig(math.log(1.2))
        lv = levels.get(code, ())
        pct, pr = dist(F, T, fit, lv)
        row = dict(code=code, F=F, T=T, expiry=exp, barchart_iv=float(bciv), put_call_premium=float(pcr), n=len(pts),
                   atm=fit[0], skew=skew, pct={str(k): v for k, v in pct.items()}, p={str(L): v for L, v in pr.items()})
        res.append(row)
        print(f"{code} F {F:.2f} exp {exp} (T {T:.2f}) n {len(pts)} | ATM {fit[0]*100:.1f}% (Barchart {bciv}%) | skew 0.8F-1.2F {skew*100:+.1f} pp | P/C premium {pcr}")
        print(f"   p10 {pct[.1]:.1f} p25 {pct[.25]:.1f} p50 {pct[.5]:.1f} p75 {pct[.75]:.1f} p90 {pct[.9]:.1f}"
              + ''.join(f" | P(<= {L}) {pr[L]*100:.0f}%" for L in lv))
    return res

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == '--chains':
        # py -I futures.py --chains chains.txt YYYY-MM-DD CODE:bear,base,bull ...
        today = dt.datetime.strptime(sys.argv[3], "%Y-%m-%d")
        lv = {a.split(':')[0]: tuple(float(x) for x in a.split(':')[1].split(',')) for a in sys.argv[4:]}
        out = chains_main(sys.argv[2], today, lv)
        json.dump(out, open(sys.argv[2] + '.json', 'w'), indent=1)
    else:
        main()
