"""Anthropic (ANT) - extras for docs/anthropic-analysis.md v1.1 (20 Nov 2026): exit cross-check, ROIC_g,
return bridge, year-end path, reverse tests, sensitivities, stakes. Imports model.py. Run: py report.py
v1.1: entry price = first close $97.17 (19 Nov); the deal ($83, 424B4) fixes shares and cash."""
from datetime import date
from model import (build, SC, E1, K, T, VAL, STUB, REV_2026, OA, TAX, USDNOK, IPO, P_CLOSE, PRICES,
                   shares_fd, shares_issued, cash_close)

P0 = P_CLOSE
BOOK0 = 128.887 + OA * IPO / 1000 + 109.742   # 424B4 pro forma as adjusted equity + option + Amazon notes as equity


def extras(r):
    s, P, rows = r["s"], r["P"], r["rows"]
    out = {}
    ni_lev = r["nopat30"] + s["r"] * r["nc_T"] * (1 - TAX)
    out["pe_equity"] = r["eq_T"] / ni_lev
    out["ev_sales30"] = r["ev"] / r["rev30"]
    book0 = BOOK0
    cash_earn = STUB["adj_oi"] + STUB["interest"] - STUB["tax"] + sum(x["adj"] + x["interest"] - x["tax"] for x in rows)
    out["book0"], out["bookT"] = book0, book0 + cash_earn
    out["pb"] = r["eq_T"] / out["bookT"]
    out["implied_ret"] = 0.7 / out["pe_equity"] + s["lr_growth"]
    inv = sum(x["compute"] - s["c_norm"] * x["rev"] for x in rows) + sum(x["capex"] for x in rows) + STUB["capex"]
    inv += sum(o[1] - o[2] for o in r["over_rows"] if o[1] > o[2])
    m = r["ebit_m"] * (1 - TAX)
    d_nopat = r["nopat30"] - REV_2026 * m
    out["inv"], out["d_nopat"] = inv, d_nopat
    out["roic_g"] = d_nopat / inv
    out["value_created"] = inv * (out["roic_g"] / K - 1)
    fd0 = r["fd0"]
    nop27 = E1["Base"][0] * SC["Base"]["share"] * (1 - SC["Base"]["c_norm"] - SC["Base"]["o_norm"] - SC["Base"]["sbc_norm"]) * (1 - TAX)
    ev0_ps = P - r["nc0"] * 1000 / fd0
    earn = r["pe0"] * (r["nopat30"] - nop27) * 1000 / fd0
    mult = (s["pe"] - r["pe0"]) * r["nopat30"] * 1000 / fd0
    over = -r["over"] * 1000 / fd0
    dil = (r["ev"] - r["over"]) * 1000 / r["sh_T"] - (r["ev"] - r["over"]) * 1000 / fd0
    cash = r["nc_T"] * 1000 / r["sh_T"] - r["nc0"] * 1000 / fd0
    out["bridge"] = dict(entry=P, ev0=ev0_ps, nc0=r["nc0"] * 1000 / fd0, earnings=earn, multiple=mult,
                         overhang=over, dilution=dil, cash=cash, VT=r["VT"],
                         check=ev0_ps + r["nc0"] * 1000 / fd0 + earn + mult + over + dil + cash)
    return out


def solve(f, lo, hi, n=80):
    for _ in range(n):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if f(m) < 0 else (lo, m)
    return m


def rd(d):
    return {k: (round(v, 3) if isinstance(v, float) else v) for k, v in d.items()}


if __name__ == "__main__":
    print(f"T {T:.3f}; FD at {P0} {shares_fd(P0):,.1f}m; issued {shares_issued():,.1f}m; cash {cash_close():.2f}bn;"
          f" mcap FD {P0*shares_fd(P0)/1000:,.0f}bn issued {P0*shares_issued()/1000:,.0f}bn;"
          f" EV {P0*shares_fd(P0)/1000-cash_close():,.0f}bn; book0 {BOOK0:.1f}")
    for name in ("Bear", "Base", "Bull"):
        r = build(name, P0)
        e = extras(r)
        print(f"\n== {name} @{P0}: IRR {r['irr']:.1%} NOK {r['irr_nok']:.1%} VT {r['VT']:.2f} Pk {r['pk']:.2f} MoS {r['mos']:+.1%}")
        print("  rows:")
        for x in r["rows"]:
            print("   ", rd(x))
        print(f"  rev30 {r['rev30']:.1f} EBIT {r['ebit_m']:.0%} NOPAT30 {r['nopat30']:.1f} EV {r['ev']:.0f} ncT {r['nc_T']:.1f}"
              f" overhang {r['over']:.1f} eqT {r['eq_T']:.0f}; shares fd0 {r['fd0']:.0f} grants {r['grants']:.0f}"
              f" match {r['match']:.0f} pbf {r['pbf']:.0f} shT {r['sh_T']:.0f}")
        print("  overhang", [tuple(round(v, 1) for v in o) for o in r["over_rows"]])
        print("  extras", rd({k: v for k, v in e.items() if k != "bridge"}))
        print("  bridge", {k: round(v, 2) for k, v in e["bridge"].items()})
        v26 = P0 + STUB["fcf"] * 1000 / r["fd0"]
        t27 = (date(2027, 12, 31) - VAL).days / 365
        t28 = (date(2028, 12, 31) - VAL).days / 365
        m27, m28 = r["marks"]
        print(f"  path: V26 {v26:.2f} V27 {m27:.1f} V28 {m28:.1f} VT {r['VT']:.1f}; r_t {m27/v26-1:+.1%} {m28/m27-1:+.1%}"
              f" {r['VT']/m28-1:+.1%}; IRR to 27 {(m27/P0)**(1/t27)-1:+.1%} to 28 {(m28/P0)**(1/t28)-1:+.1%}; pe0 {r['pe0']:.1f}")
        fd = r["fd0"] / 1000
        print("  per share: adjOI", [round(x["adj"] / fd, 2) for x in r["rows"]], "FCF", [round(x["fcf"] / fd, 2) for x in r["rows"]],
              "nc", [round(x["nc"] / fd, 2) for x in r["rows"]], "core EPS", [round(x["core"] / fd, 2) for x in r["rows"]],
              "cum FCF", round(sum(x["fcf"] for x in r["rows"]) / fd, 2), "nc26", round(r["nc26"] / fd, 2),
              "ncT/shT", round(r["nc_T"] * 1000 / r["sh_T"], 2), "min nc", round(min(r["nc_path"]), 1))
        print("  E1 share", [round(x, 3) for x in r["e1share"]], "rev", [round(x, 1) for x in r["rev"]],
              "stub FCF/sh", round(STUB["fcf"] / fd, 2))
    b = lambda **o: build("Base", P0, **o)
    print(f"\n--- reverse tests @{P0} (Base at k)")
    pe_need = solve(lambda x: b(pe=x)["irr"] - K, 5, 120)
    cn = solve(lambda x: -(b(c_norm=x)["irr"] - K), 0.05, 0.7)
    sh_need = solve(lambda x: b(share=x)["irr"] - K, 0.3, 2.0)
    r_sh = b(share=sh_need)
    print(f"exit P/E needed {pe_need:.1f}; normalised compute needed {cn:.3f} -> EBIT {1-cn-0.19-0.04:.3f};"
          f" E1 share needed {sh_need:.3f} -> rev 2029 {r_sh['rev'][2]:.1f}, 2030 {r_sh['rev30']:.1f}")
    for P in PRICES:
        print(f"  at ${P}: exit P/E needed {solve(lambda x: build('Base', P, pe=x)['irr'] - K, 5, 120):.1f};"
              f" share needed {solve(lambda x: build('Base', P, share=x)['irr'] - K, 0.3, 2.0):.3f}")
    print(f"\n--- sensitivities @{P0} Base: IRR / Pk / MoS")
    sens = [("exit P/E 21 (AI BBB E layer)", dict(pe=21)), ("exit P/E 30", dict(pe=30)),
            ("exit P/E 24 (governance -2)", dict(pe=24)),
            ("E1 share 50%", dict(share=0.50)), ("E1 share 65%", dict(share=0.65)),
            ("normalised compute 48%", dict(c_norm=0.48)), ("normalised compute 56%", dict(c_norm=0.56)),
            ("window compute +15%", dict(compute=[x * 1.15 for x in SC["Base"]["compute"]])),
            ("window compute -15%", dict(compute=[x * 0.85 for x in SC["Base"]["compute"]])),
            ("no post-IPO dilution", dict(grant=0.0, match_pa=0.0)),
            ("interest on cash 3.0%", dict(r=0.03)),
            ("no overhang tail", dict(tail_years=0)),
            ("E1 Bull revenue at 62%, Base costs and P/E", None)]
    for lab, o in sens:
        if o is None:
            r = build("Bull", P0, compute=SC["Base"]["compute"], other=SC["Base"]["other"], capex=SC["Base"]["capex"],
                      c_norm=SC["Base"]["c_norm"], o_norm=SC["Base"]["o_norm"], sbc_norm=SC["Base"]["sbc_norm"],
                      pe=SC["Base"]["pe"])
        else:
            r = b(**o)
        print(f"  {lab}: {r['irr']:.1%} / {r['pk']:.1f} / {r['mos']:+.1%}")
    # 2-year tail on the Base margin gap instead of the named reason (as in v1.0: VT minus the extra after-tax gap)
    rb = build("Base", P0)
    print(f"  tail sensitivity: VT {(rb['eq_T'] - (26.7 - 7.4)) * 1000 / rb['sh_T']:.2f}")
    vt_tail = (rb['eq_T'] - (26.7 - 7.4)) * 1000 / rb['sh_T']
    print(f"    IRR {(vt_tail/P0)**(1/T)-1:.1%} Pk {vt_tail/(1+K)**T:.1f}")
    for P in (IPO, 90, 92.60, 100, 111.50):
        r = build("Base", P)
        print(f"  entry ${P}: IRR {r['irr']:.1%}; P_k {r['pk']:.1f}; MoS {r['pk']/P-1:+.1%}; VT {r['VT']:.2f}")
    rbb = build("Bear", P0, share=0.58)
    print(f"  Bear with share 58%: {rbb['irr']:.1%} VT {rbb['VT']:.1f}")
    rb2 = build("Bear", P0, pe=21)
    print(f"  Bear at exit P/E 21: {rb2['irr']:.1%} VT {rb2['VT']:.1f}")
    vts = [build(n, P0)["VT"] for n in ("Bear", "Base", "Bull")]
    w = 0.25 * vts[0] + 0.5 * vts[1] + 0.25 * vts[2]
    print(f"scenario-weighted reference V_T {w:.1f} IRR {(w/P0)**(1/T)-1:.1%}")
    pkB, pkU = build("Base", P0)["pk"], build("Bull", P0)["pk"]
    print(f"share of Bull priced {(P0-pkB)/(pkU-pkB):.1%}")
    print("\nEntry-price table:")
    for P in PRICES:
        line = []
        for n in ("Bear", "Base", "Bull"):
            r = build(n, P)
            line.append(f"{n} {r['irr']:.1%} NOK {r['irr_nok']:.1%} VT {r['VT']:.1f} Pk {r['pk']:.1f} MoS {r['mos']:+.1%}")
        print(P, f"NOK {P*USDNOK:.0f} FD {shares_fd(P):.0f} mcapFD {P*shares_fd(P)/1000:.0f} issued {P*shares_issued()/1000:.0f}"
                 f" EV {P*shares_fd(P)/1000-cash_close():.0f}", " | ".join(line))
    print("\n--- stakes, USD bn")
    pk = build("Base", P0)["pk"]
    holders = {"Amazon": 1936.452353 + 1547.676309, "Alphabet": 1774.959745, "NVIDIA": 120.481927, "AMD": 30.120481,
               "Broadcom": 12.048192, "Micron": 12.048192, "Microsoft": 12.048192, "TSMC": 6.024096}
    for h, sh in holders.items():
        print(f"  {h} {sh:,.1f}m: at IPO {sh*IPO/1000:.2f}  at close {sh*P0/1000:.2f}  at P_k {sh*pk/1000:.2f}")
    print(f"P_k {pk:.2f}; FD equity at P_k {pk*shares_fd(P0)/1000:.0f}bn; issued {pk*shares_issued()/1000:.0f}bn; NOK prices",
          [round(P * USDNOK) for P in PRICES], "P_k NOK", round(pk * USDNOK))
