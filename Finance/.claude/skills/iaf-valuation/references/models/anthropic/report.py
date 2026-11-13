"""Anthropic (ANT) - extras for docs/anthropic-analysis.md v1.0 (13 Nov 2026): exit cross-check, ROIC_g,
return bridge, year-end path, reverse tests, sensitivities, stakes. Imports model.py. Run: py report.py"""
from datetime import date
from model import (build, SC, E1, K, T, VAL, STUB, REV_2026, OA, TAX, USDNOK, shares_fd, shares_issued,
                   pk_fixed)


def extras(r):
    s, P, rows = r["s"], r["P"], r["rows"]
    out = {}
    ni_lev = r["nopat30"] + s["r"] * r["nc_T"] * (1 - TAX)
    out["pe_equity"] = r["eq_T"] / ni_lev
    out["ev_sales30"] = r["ev"] / r["rev30"]
    book0 = 108.089 + 0.793 * (P - 74) + OA * P * 0.9882 / 1000 + 110.873   # Amazon notes counted as equity
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
    for name in ("Bear", "Base", "Bull"):
        r = build(name, 74)
        e = extras(r)
        print(f"\n== {name} @74: IRR {r['irr']:.1%} NOK {r['irr_nok']:.1%} VT {r['VT']:.2f} Pk {r['pk']:.2f} MoS {r['mos']:+.1%}")
        print("  rows:")
        for x in r["rows"]:
            print("   ", rd(x))
        print(f"  rev30 {r['rev30']:.1f} EBIT {r['ebit_m']:.0%} NOPAT30 {r['nopat30']:.1f} EV {r['ev']:.0f} ncT {r['nc_T']:.1f}"
              f" overhang {r['over']:.1f} eqT {r['eq_T']:.0f}; shares fd0 {r['fd0']:.0f} grants {r['grants']:.0f}"
              f" match {r['match']:.0f} pbf {r['pbf']:.0f} shT {r['sh_T']:.0f}")
        print("  overhang", [tuple(round(v, 1) for v in o) for o in r["over_rows"]])
        print("  extras", rd({k: v for k, v in e.items() if k != "bridge"}))
        print("  bridge", {k: round(v, 2) for k, v in e["bridge"].items()})
        v26 = 74 + STUB["fcf"] * 1000 / r["fd0"]
        t27 = (date(2027, 12, 31) - VAL).days / 365
        t28 = (date(2028, 12, 31) - VAL).days / 365
        m27, m28 = r["marks"]
        print(f"  path: V26 {v26:.2f} V27 {m27:.1f} V28 {m28:.1f} VT {r['VT']:.1f}; r_t {m27/v26-1:+.1%} {m28/m27-1:+.1%}"
              f" {r['VT']/m28-1:+.1%}; IRR to 27 {(m27/74)**(1/t27)-1:+.1%} to 28 {(m28/74)**(1/t28)-1:+.1%}; pe0 {r['pe0']:.1f}")
        fd = r["fd0"] / 1000
        print("  per share: adjOI", [round(x["adj"] / fd, 2) for x in r["rows"]], "FCF", [round(x["fcf"] / fd, 2) for x in r["rows"]],
              "nc", [round(x["nc"] / fd, 2) for x in r["rows"]], "core EPS", [round(x["core"] / fd, 2) for x in r["rows"]],
              "cum FCF", round(sum(x["fcf"] for x in r["rows"]) / fd, 2), "nc26", round(r["nc26"] / fd, 2),
              "min nc", round(min(r["nc_path"]), 1))
        print("  E1 share", [round(x, 3) for x in r["e1share"]], "rev", [round(x, 1) for x in r["rev"]])
    b = lambda **o: build("Base", 74, **o)
    print("\n--- reverse tests @74 (Base at k)")
    pe_need = solve(lambda x: b(pe=x)["irr"] - K, 5, 80)
    cn = solve(lambda x: -(b(c_norm=x)["irr"] - K), 0.2, 0.7)
    sh_need = solve(lambda x: b(share=x)["irr"] - K, 0.3, 1.5)
    r_sh = b(share=sh_need)
    print(f"exit P/E needed {pe_need:.1f}; normalised compute needed {cn:.3f} -> EBIT {1-cn-0.19-0.04:.3f};"
          f" E1 share needed {sh_need:.3f} -> rev 2029 {r_sh['rev'][2]:.1f}, 2030 {r_sh['rev30']:.1f}")
    for P in (70, 78):
        print(f"  at ${P}: exit P/E needed {solve(lambda x: build('Base', P, pe=x)['irr'] - K, 5, 80):.1f};"
              f" share needed {solve(lambda x: build('Base', P, share=x)['irr'] - K, 0.3, 1.5):.3f}")
    print("\n--- sensitivities @74 Base: IRR / Pk / MoS")
    sens = [("exit P/E 21 (AI BBB E layer)", dict(pe=21)), ("exit P/E 30", dict(pe=30)),
            ("exit P/E 24 (governance -2)", dict(pe=24)),
            ("E1 share 50%", dict(share=0.50)), ("E1 share 65%", dict(share=0.65)),
            ("normalised compute 48%", dict(c_norm=0.48)), ("normalised compute 56%", dict(c_norm=0.56)),
            ("window compute +15%", dict(compute=[x * 1.15 for x in SC["Base"]["compute"]])),
            ("window compute -15%", dict(compute=[x * 0.85 for x in SC["Base"]["compute"]])),
            ("no post-IPO dilution", dict(grant=0.0, match_pa=0.0)),
            ("interest on cash 3.0%", dict(r=0.03)),
            ("no overhang tail", dict(tail_years=0)),
            ("E1 Bull revenue at 62%, Base costs and P/E", dict(share=0.62 * 1.0, g=SC["Bull"]["g"]))]
    for lab, o in sens:
        if lab.startswith("E1 Bull"):
            r = build("Base", 74, **o)
            # replace revenue with the Bull path: run as Bull with Base costs and multiple
            r = build("Bull", 74, compute=SC["Base"]["compute"], other=SC["Base"]["other"], capex=SC["Base"]["capex"],
                      c_norm=SC["Base"]["c_norm"], o_norm=SC["Base"]["o_norm"], sbc_norm=SC["Base"]["sbc_norm"],
                      pe=SC["Base"]["pe"])
        else:
            r = b(**o)
        print(f"  {lab}: {r['irr']:.1%} / {r['pk']:.1f} / {r['mos']:+.1%}")
    for P in (90, 100):
        r = build("Base", P)
        print(f"  aftermarket entry ${P}: IRR {r['irr']:.1%}; P_k {r['pk']:.1f}; MoS {r['pk']/P-1:+.1%}")
    rb = build("Bear", 74, share=0.58)
    print(f"  Bear with share 58%: {rb['irr']:.1%} VT {rb['VT']:.1f}")
    rb2 = build("Bear", 74, pe=21)
    print(f"  Bear at exit P/E 21: {rb2['irr']:.1%} VT {rb2['VT']:.1f}")
    vts = [build(n, 74)["VT"] for n in ("Bear", "Base", "Bull")]
    w = 0.25 * vts[0] + 0.5 * vts[1] + 0.25 * vts[2]
    print(f"scenario-weighted reference V_T {w:.1f} IRR {(w/74)**(1/T)-1:.1%}")
    pkB, pkU = build("Base", 74)["pk"], build("Bull", 74)["pk"]
    print(f"share of Bull priced {(74-pkB)/(pkU-pkB):.1%}")
    print("\nRange table:")
    for P in (70, 74, 78):
        line = []
        for n in ("Bear", "Base", "Bull"):
            r = build(n, P)
            line.append(f"{n} {r['irr']:.1%} NOK {r['irr_nok']:.1%} VT {r['VT']:.1f} Pk {r['pk']:.1f} MoS {r['mos']:+.1%}")
        print(P, f"FD {shares_fd(P):.0f}", " | ".join(line))
    pstar = pk_fixed("Base")
    print(f"fixed point: Base IRR = k at IPO price {pstar:.2f}; +2% margin at {pk_fixed('Base', 0.02):.2f}")
    print("\n--- stakes, USD bn")
    pk = build("Base", 74)["pk"]
    for P in (70, 74, 78):
        print(P, "AMZN", round(3484.06 * P / 1000, 1), "GOOGL", round((1654.463134 + 10000 / P) * P / 1000, 1),
              f"({1654.463134 + 10000 / P:.1f}m)", "NVDA placement shares", round(10000 / P, 1), "m")
    print(f"at P_k {pk:.2f}: AMZN {3484.06*pk/1000:.1f} GOOGL {(1654.463134+10000/74)*pk/1000:.1f} NVDA {10000/74*pk/1000:.2f}")
    print(f"FD equity at P_k {pk*shares_fd(74)/1000:.0f}bn; issued {pk*shares_issued(74)/1000:.0f}bn; NOK prices",
          [round(P * USDNOK) for P in (70, 74, 78)], "P_k NOK", round(pk * USDNOK))
