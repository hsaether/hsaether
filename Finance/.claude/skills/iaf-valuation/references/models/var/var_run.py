"""Vår Energi (VAR) IAF run - document figures for docs/var-analysis.md v1.0 (25 Nov 2026).
Run from this folder:  py var_run.py      (prints all tables; writes results.json beside it)
"""
import json
import var_model as vm
from var_model import (run, irr_pk, per_share_flows, xirr, VAL, EXIT, P_NOK, USDNOK, K, SHARES,
                       BLOCKS, ASSET_R, PER, BRENT, TTF, BRENT_MID, TTF_MID, EURUSD, MWH_PER_BOE)

T = (EXIT - VAL).days / 365
NOKPATH = {"Bear": lambda y: 1.12 if y <= 2027 else 1.09, "Bull": lambda y: .97,
           "Base": lambda y: 1.0}
OSLO_PE = {"Bear": 10.5, "Base": 11.5, "Bull": 12.5}


def pv(flows, r, t0=VAL):
    return sum(cf / (1 + r) ** ((d - t0).days / 365) for d, cf in flows)


R = {}
for sc in ("Bear", "Base", "Bull"):
    res = run(sc)
    irr, pk, f = irr_pk(res)
    st = run(sc, mid_from_2027=True)
    irr_s, pk_s, f_s = irr_pk(st)
    irr_nok = irr_pk(res, fx=NOKPATH[sc])[0]
    nt = run(sc, use_tail=False); irr_nt, pk_nt, _ = irr_pk(nt)
    sumD = sum(cf for d, cf in f[:-1]); VT = f[-1][1]
    d_ = sumD / T / P_NOK
    g_ = (VT / P_NOK) ** (1 / T) - 1 if VT > 0 else None
    nav0 = pv(f_s, ASSET_R)                       # NAV_0 at the scenario's mid-cycle marks
    rer = (nav0 / P_NOK) ** (1 / T) - 1
    navg = (VT / nav0) ** (1 / T) - 1 if VT > 0 else None
    sumD_s = sum(cf for d, cf in f_s[:-1]); VT_s = f_s[-1][1]
    d_s = sumD_s / T / P_NOK
    g_s = (VT_s / P_NOK) ** (1 / T) - 1 if VT_s > 0 else None
    # FCF_normalised (levered, NOK/share): sustained unlevered post-tax CF at mid-cycle (= asset rate x
    # block value, mid-year adjusted) less after-tax interest on exit NIBD and the hybrid coupon
    unlev = sum(res["nav_blocks"].values()) * ASSET_R / (1 + ASSET_R) ** .5
    fcfn = (unlev - .055 * res["N_exit"] * .78 - 105) / res["shares"] * USDNOK
    book = 157 + 1052 + 248.4 * P_NOK / USDNOK
    for r in res["rows"]:
        pbt = r["ebitdax"] - r["dda"] - r["expl"] - r["interest"]
        book += pbt - (r["tax_acc"] + r["tax_dk"]) - r["hybrid"] - r["decl"]
    R[sc] = dict(res=res, f=f, irr=irr, pk=pk, irr_nok=irr_nok, irr_s=irr_s, pk_s=pk_s, irr_nt=irr_nt,
                 pk_nt=pk_nt, sumD=sumD, VT=VT, d=d_, g=g_, nav0=nav0, rer=rer, navg=navg,
                 cyc=irr - irr_s, dd=d_ - d_s, dg=(g_ - g_s) if (g_ is not None and g_s is not None) else None,
                 fcfn=fcfn, book=book / res["shares"] * USDNOK,
                 maxlev=max(r["lev"] for r in res["rows"]), maxN=max(r["N"] for r in res["rows"]))

pc = lambda x: "n/m" if x is None else f"{x*100:.1f}%"
print(f"T = {T:.3f} y; P = NOK {P_NOK}; USD/NOK {USDNOK}; EUR/USD {EURUSD:.4f}; shares pro forma {SHARES:,.1f}m")
print("\n== Decision and results ==")
for sc in ("Bear", "Base", "Bull"):
    x = R[sc]; res = x["res"]
    ceil = x["irr"] / K ** 2
    print(f"{sc}: IRR {pc(x['irr'])} | NOK path {pc(x['irr_nok'])} | V_T {x['VT']:.2f} (equity before floor "
          f"{res['vt_raw']*USDNOK:.2f}) | P_k {x['pk']:.2f} MoS {(x['pk']/P_NOK-1)*100:+.1f}% | sumD {x['sumD']:.2f} "
          f"| sumD+VT {x['sumD']+x['VT']:.2f} ({(x['sumD']+x['VT'])/P_NOK*100-100:+.0f}%)")
    print(f"   d {pc(x['d'])} g {pc(x['g'])} c {pc(None if x['g'] is None else x['irr']-x['d']-x['g'])} | NAV0 {x['nav0']:.2f} "
          f"P/NAV0 {P_NOK/x['nav0']:.2f} re-rating {pc(x['rer'])} NAV growth {pc(x['navg'])} | structural {pc(x['irr_s'])} "
          f"(P_k {x['pk_s']:.2f}) cyclical {x['cyc']*100:+.1f}pp (dd {x['dd']*100:+.1f}, dg {('n/m' if x['dg'] is None else f'{x[chr(100)+chr(103)]*100:+.1f}')})")
    print(f"   no tail: IRR {pc(x['irr_nt'])} P_k {x['pk_nt']:.2f} | FCFn {x['fcfn']:.2f} P/FCFn {P_NOK/x['fcfn']:.1f}x vs ceiling "
          f"{'n/m' if ceil <= 0 else f'{ceil:.1f}x'} | exit P/E {x['VT']/x['fcfn']:.1f} P/B {x['VT']/x['book']:.2f} (book {x['book']:.2f}) "
          f"| max NIBD/EBITDAX {x['maxlev']:.2f}, max NIBD ${x['maxN']:,.0f}m")
    print(f"   exit: blocks {', '.join(f'{k} {v:,.0f}' for k, v in res['nav_blocks'].items())} + synergy 350 = EV {res['ev_exit']:,.0f}; "
          f"NIBD {res['N_exit']:,.0f}; hybrid {res['hybrid']:,.0f}; tax payable {res['exit_tax']:,.0f}; equity {res['eq_exit']:,.0f} $m")
nav_mkt = pv(per_share_flows(run("Base")), ASSET_R)
print(f"NAV at today's market marks (Base strip in the window, 8%): {nav_mkt:.2f} (P/NAV {P_NOK/nav_mkt:.2f})")
dates = {}
for sc, w in (("Bear", .25), ("Base", .5), ("Bull", .25)):
    for d, cf in R[sc]["f"]:
        dates[d] = dates.get(d, 0) + w * cf
print(f"Scenario-weighted reference (convention): IRR {xirr([(VAL, -P_NOK)] + sorted(dates.items()))*100:.1f}%")
print(f"Share of Bull priced: {(P_NOK - R['Base']['pk']) / (R['Bull']['pk'] - R['Base']['pk'])*100:.0f}%")

print("\n== Period tables (USD m; NOK/share at spot on pro forma shares) ==")
for sc in ("Base", "Bear", "Bull"):
    res = R[sc]["res"]; ps = USDNOK / res["shares"]
    print(sc)
    for r in res["rows"]:
        print(f" {r['lab']:6} prod {r['prod']:6.1f} Brent {r['brent']:5.1f} TTF {r['ttf']:5.1f} rev {r['rev']:6.0f} EBITDAX {r['ebitdax']:6.0f} "
              f"({r['ebitdax']*ps:5.2f}) tax paid {r['tax_nor_paid']+r['tax_dk']:6.0f} CFFO {r['cffo']:6.0f} capex+expl+abex+lease "
              f"{r['capex']+r['expl']+r['abex']+r['lease']:5.0f} MFCF {r['mfcf']:6.0f} ({r['mfcf']*ps:5.2f}) deals {r['extra']:6.0f} "
              f"decl {r['decl']:5.0f} ({r['decl']*ps:4.2f}) paid {r['div_paid']:5.0f} ({r['div_paid']*ps:4.2f}) NIBD {r['N']:6.0f} ({r['N']*ps:5.2f}) "
              f"lev {r['lev']:.2f}")
    print("  D_t:", ", ".join(f"{d.isoformat()} {cf/res['shares']*USDNOK:.2f}" for d, cf in res["divs"]))

print("\n== Year-end path (NOK/share) ==")
ends = [(2026, PER[0][2]), (2027, PER[4][2]), (2028, PER[5][2]), (2029, PER[6][2])]
for sc in ("Bear", "Base", "Bull"):
    f = R[sc]["f"]; prevV = P_NOK; line = []
    for y, e in ends:
        src = R["Base"]["f"] if y == 2026 else f
        Vt = f[-1][1] if y == 2029 else max(pv([(d, cf) for d, cf in src if d > e], ASSET_R, e), 0)
        Dy = sum(cf for d, cf in f[:-1] if d.year == y)
        rt = (Dy + Vt - prevV) / prevV
        upto = [(d, cf) for d, cf in f[:-1] if d <= e] + [(e, Vt)]
        it = xirr([(VAL, -P_NOK)] + upto) if y > 2026 else None
        line.append(f"{y}: D {Dy:.2f} V {Vt:.2f} r {rt*100:+.1f}% IRR {pc(it)}")
        prevV = Vt
    print(sc, " | ".join(line))

print("\n== Driver breakdown (one at a time from Base) ==")
for sc in ("Bear", "Bull"):
    sB, sT = dict(vm.BRENT), dict(vm.TTF)
    vm.BRENT["X"], vm.TTF["X"] = sB[sc], sT[sc]
    vm.BRENT_MID["X"], vm.TTF_MID["X"] = BRENT_MID["Base"], TTF_MID["Base"]
    i1, p1, _ = irr_pk(run("X", cop_floor=False, use_tail=False))
    vm.BRENT_MID["X"], vm.TTF_MID["X"] = BRENT_MID[sc], TTF_MID[sc]
    i2, p2, _ = irr_pk(run("X", cop_floor=False, use_tail=False))
    i3, p3, _ = irr_pk(run(sc))
    print(f" {sc}: 1 window oil and gas paths: {pc(i1)} P_k {p1:.2f} | 2 + mid-cycle marks at exit: {pc(i2)} P_k {p2:.2f} | "
          f"3 + COP floor and exit tail: {pc(i3)} P_k {p3:.2f}")

print("\n== Base return bridge (NOK/share) ==")
b = R["Base"]
print(f" P {P_NOK} -> NAV_0 {b['nav0']:.2f} (re-rating {b['nav0']-P_NOK:+.2f}); dividends {b['sumD']:.2f}; "
      f"V_T - NAV_0 {b['VT']-b['nav0']:+.2f}; sum D + V_T {b['sumD']+b['VT']:.2f}")
st = run("Base", mid_from_2027=True)
fs = irr_pk(st)[2]
print(f" structural run: sum D {sum(cf for d, cf in fs[:-1]):.2f}, V_T {fs[-1][1]:.2f}; cycle in the window adds "
      f"{b['sumD']-sum(cf for d, cf in fs[:-1]):+.2f} in D and {b['VT']-fs[-1][1]:+.2f} in V_T")

print("\n== Sensitivities (Base unless stated) ==")
sens = [("Synergies full ($850m NPV)", dict(synergy=850)), ("Synergies none", dict(synergy=0)),
        ("Exit marks at Oslo mid-cycle return 8.9%", dict(exit_r=.089)),
        ("Brent mid-cycle 75 (+5)", dict(brent_mid=75)), ("Brent mid-cycle 65 (-5)", dict(brent_mid=65)),
        ("TTF mid-cycle 33 (+5)", dict(ttf_mid=33)), ("TTF mid-cycle 23 (-5)", dict(ttf_mid=23)),
        ("Payout 40% of CFFO", dict(payout=.40)), ("Q4-26 dividend scaled for the placement ($491m)", dict(q4div=491)),
        ("COP capex x1.3", dict(cop_capex_mult=1.3)), ("BlueNord does not close", dict(bn_close=False)),
        ("Gas paths x0.8 from 2027", dict(gas_scale=.8)), ("Gas paths x1.2 from 2027", dict(gas_scale=1.2)),
        ("Run-off reserve NAV at exit (2P + 50% 2C)", dict(exit_method="runoff"))]
for lab, kw in sens:
    r = run("Base", **kw); i, p, _ = irr_pk(r)
    print(f" {lab}: IRR {pc(i)} P_k {p:.2f} MoS {(p/P_NOK-1)*100:+.1f}% V_T {r['vt_usd']*USDNOK:.2f} (before floor {r['vt_raw']*USDNOK:.2f})")
for sc in ("Bear", "Base", "Bull"):
    x = R[sc]; vt_pe = max(OSLO_PE[sc] * x["fcfn"], 0)
    f = list(x["f"][:-1]) + [(EXIT, vt_pe)]
    print(f" {sc}: exit at Equity BBB Oslo exit P/E {OSLO_PE[sc]} x FCF_norm {x['fcfn']:.2f}: V_T {vt_pe:.2f} "
          f"IRR {pc(xirr([(VAL, -P_NOK)] + f))} P_k {pv(f, K):.2f}")
# oil turn calls (oil-market-bbb 18 Nov): 2027 above the strip; 2028-29 below the strip
sB = {k: list(v) for k, v in vm.BRENT.items()}
vm.BRENT["Base"] = [sB["Base"][0]] + [x + 5 for x in sB["Base"][1:5]] + sB["Base"][5:]
i, p, _ = irr_pk(run("Base")); print(f" Turn call: Brent 2027 +$5 (no deal longer): IRR {pc(i)} P_k {p:.2f}")
vm.BRENT["Base"] = sB["Base"][:5] + [x - 5 for x in sB["Base"][5:]]
i, p, _ = irr_pk(run("Base")); print(f" Turn call: Brent 2028-29 -$5 (market-share quotas): IRR {pc(i)} P_k {p:.2f}")
vm.BRENT["Base"] = sB["Base"]

print("\n== Step 6b: what the price implies ==")
def solve(fn, lo, hi):
    for _ in range(60):
        m = (lo + hi) / 2
        if irr_pk(fn(m))[0] < K:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2
bm = solve(lambda x: run("Base", brent_mid=x), 60, 200)
bm2 = solve(lambda x: run("Base", brent_mid=x, ttf_mid=28 * x / 70), 60, 200)
tm = solve(lambda x: run("Base", ttf_mid=x), 20, 150)
print(f" Brent mid-cycle for IRR = k: ${bm:.1f} (TTF mid 28 kept); ${bm2:.1f} with TTF pro rata ({28*bm2/70:.1f}); "
      f"TTF mid alone (Brent 70): EUR {tm:.1f}/MWh")
pe_k = None
x = R["Base"]
for pe in [i / 10 for i in range(40, 400)]:
    f = list(x["f"][:-1]) + [(EXIT, pe * x["fcfn"])]
    if xirr([(VAL, -P_NOK)] + f) >= K:
        pe_k = pe; break
print(f" Exit P/E on FCF_norm at which Base returns k: {pe_k}")
for k_, p in BLOCKS.items():
    real = vm.mid_margin(k_, p, 70, 28)[0]
    q0 = p["kboe"][6] * .365
    cost = p["opex"][6] + (p["other"][6] + p["capex"][6] + p["expl"][6] + p["abex"][6] + p["lease"][6]) / q0
    print(f" {k_}: mid realised ${real:.1f}/boe, sustaining cost ${cost:.1f}/boe, post-tax ${(real-cost)*(1-p['tax']):.2f}/boe, "
          f"2029 {q0:.1f} mmboe")

print("\n== Exit consistency (Year-3 vs mid-cycle) ==")
for sc in ("Bear", "Base", "Bull"):
    gb = (BRENT[sc][6] - BRENT_MID[sc]) / BRENT_MID[sc]; gt = (TTF[sc][6] - TTF_MID[sc]) / TTF_MID[sc]
    tail = sum(vm.exit_tail(k_, p, sc, BRENT_MID[sc], TTF_MID[sc], p["kboe"][6] * .365) for k_, p in BLOCKS.items())
    print(f" {sc}: Brent {BRENT[sc][6]} vs {BRENT_MID[sc]} ({gb*100:+.1f}%); TTF {TTF[sc][6]} vs {TTF_MID[sc]} ({gt*100:+.1f}%); "
          f"tail ${tail:,.0f}m = NOK {tail/SHARES*USDNOK:.2f}/share")

print("\n== Deal tests (Base, 8%, value at 31 Dec 2026) ==")
res = R["Base"]["res"]
for name, cost in (("COP", 3900.0), ("BN", 1000 + 235 + 248.4 * P_NOK / USDNOK)):
    v = 0.0
    for r in res["rows"]:
        if name in r["blk"]:
            tt = (r["end"] - PER[0][2]).days / 365 - r["yrs"] / 2
            v += r["blk"][name]["posttax_cf"] / 1.08 ** tt
    v += res["nav_blocks"][name] / 1.08 ** ((EXIT - PER[0][2]).days / 365)
    print(f" {name}: value {v:,.0f} vs cost {cost:,.0f} -> {v/cost:.2f}x")

b = R["Base"]["res"]["rows"][0]
print(f"\nNIBD: 30 Sep 3,110; ~25 Nov {3110 + (55/92)*(-b['mfcf']) + 364:,.0f} (Q4 M-FCF pro rata + Q3 dividend 364); "
      f"31 Dec {b['N']:,.0f} (incl. placement, BlueNord, asset sales); Q4 EBITDAX {b['ebitdax']:,.0f}, revenue {b['rev']:,.0f}")
json.dump({sc: dict(irr=R[sc]["irr"], pk=R[sc]["pk"], VT=R[sc]["VT"], sumD=R[sc]["sumD"],
                    irr_nok=R[sc]["irr_nok"], nav0=R[sc]["nav0"]) for sc in R},
          open("results.json", "w"), indent=1)
