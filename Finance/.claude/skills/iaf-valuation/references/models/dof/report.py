import copy, json
from dof_model import *
from inputs_new import *

I = new_inputs("all")
I["struct_delta"] = struct_deltas(I)
FX = I["fx"]; P = I["P"]; V0 = I["val_date"]
nk = lambda x: x * FX / SH
R = {s: run(I, s) for s in ("Bear", "Base", "Bull")}
S = {s: run(I, s, structural=True) for s in ("Bear", "Base", "Bull")}
out = {}

def pr(*a):
    print(*a)

pr("=== Period tables ===")
for s in ("Base", "Bear", "Bull"):
    r = R[s]
    pr(f"--- {s}")
    hdr = ["Q4-26", "Q1-27", "Q2-27", "Q3-27", "Q4-27", "2028", "2029"]
    for key in ("ebitda", "tax", "interest", "mfcf", "amort", "fcf_ads", "gcap", "gdebt", "sale", "div_decl", "div_paid", "nibd", "cash"):
        vals = [r["rows"][p][key] for p in hdr]
        pr(f"{key:9s} " + " ".join(f"{(v if v is not None else float('nan')):8.1f}" for v in vals))
    for key in ("ebitda", "mfcf", "amort", "fcf_ads", "div_decl", "div_paid", "nibd"):
        vals = [r["rows"][p][key] for p in hdr]
        pr(f"{key+'_nok':13s} " + " ".join(f"{nk(v):7.2f}" for v in vals))
    eb27 = sum(r["rows"][p]["ebitda"] for p in hdr[1:5]); mf27 = sum(r["rows"][p]["mfcf"] for p in hdr[1:5])
    dd27 = sum(r["rows"][p]["div_decl"] for p in hdr[1:5]); am27 = sum(r["rows"][p]["amort"] for p in hdr[1:5])
    pr(f"2027 EBITDA {eb27:.1f} MFCF {mf27:.1f} ({nk(mf27):.2f}) decl {dd27:.1f} ({nk(dd27):.2f}, ${dd27/SH:.2f}/sh) amort {am27:.1f} fcfads {nk(mf27-am27):.2f}")
    lev = [r["rows"]["Q4-27"]["nibd"] / eb27, r["rows"]["2028"]["nibd"] / r["rows"]["2028"]["ebitda"], r["rows"]["2029"]["nibd"] / r["rows"]["2029"]["ebitda"]]
    pr("leverage 27/28/29", [round(x, 2) for x in lev])
    sumMF = r["rows"]["Q4-26"]["mfcf"] + mf27 + r["rows"]["2028"]["mfcf"] + r["rows"]["2029"]["mfcf"]
    sumDP = sum(r["rows"][p]["div_paid"] for p in hdr)
    sumG = sum(r["rows"][p]["gcap"] for p in hdr)
    pr(f"sum MFCF {sumMF:.1f} ({nk(sumMF):.2f}) sum div paid {sumDP:.1f} sum growth {sumG:.1f}")
    out[s] = dict(sumMF=sumMF, sumDP=sumDP, sumG=sumG, eb27=eb27, mf27=mf27, dd27=dd27)

pr("\n=== Results ===")
T = R["Base"]["T"]
for s in ("Bear", "Base", "Bull"):
    r = R[s]
    d = (r["sumD"] / T) / P
    g = (r["VT_nok"] / P) ** (1 / T) - 1
    c = r["irr"] - d - g
    pr(f"{s}: IRR {r['irr']*100:.2f} Pk {r['Pk']:.1f} MoS {(r['Pk']/P-1)*100:.1f}% VT {r['VT_nok']:.1f} ({r['VT']:.0f}) sumD {r['sumD']:.2f} D+V {r['sumD']+r['VT_nok']:.1f} ({(r['sumD']+r['VT_nok'])/P-1:+.1%}) NIBDx {r['nibd_exit']:.0f} ({nk(r['nibd_exit']):.2f}) cash {r['cash_exit']:.0f}")
    pr(f"   d {d*100:.1f} g {g*100:.1f} c {c*100:.1f}; assets {r['assets']:.0f}", {k: round(v, 1) for k, v in r['exit'].items()})
    st = S[s]
    ds = (st["sumD"] / T) / P; gs = (st["VT_nok"] / P) ** (1 / T) - 1
    pr(f"   structural IRR {st['irr']*100:.2f} cyclical {(r['irr']-st['irr'])*100:+.1f} pp (dd {(d-ds)*100:+.1f}, dg {(g-gs)*100:+.1f}); struct VT {st['VT_nok']:.1f} sumD {st['sumD']:.2f}")
    out[s].update(irr=r["irr"], Pk=r["Pk"], VT=r["VT_nok"], sumD=r["sumD"], d=d, g=g, c=c, sirr=st["irr"], VTusd=r["VT"], nibdx=r["nibd_exit"], cashx=r["cash_exit"], assets=r["assets"])

# NOK path
I2 = copy.deepcopy(I); I2["use_fxpath"] = True
I2["fxpath"] = {"Bear": {2026: 1.0, 2027: 10.41 / 9.29, 2028: 10.14 / 9.29, 2029: 10.14 / 9.29}, "Bull": {2026: 1.0, 2027: 9.02 / 9.29, 2028: 9.02 / 9.29, 2029: 9.02 / 9.29}, "Base": {}}
for s in ("Bear", "Bull"):
    r = run(I2, s)
    pr(f"NOK path {s}: IRR {r['irr']*100:.2f}  D+V {r['sumD']+r['VT_nok']:.1f}")

# NAV_0 and today's-market NAV
age0 = ann8(12.63) / ann8(13)
mid0 = {}
prem0 = {"Bear": 559.0, "Base": 404.0, "Bull": 245.0}
fac = I["meta"]["fac"]; fmv = I["meta"]["fmv"]; ip = I["meta"]["impl_price"]
for s in ("Bear", "Base", "Bull"):
    fleet0 = (fmv - ip) * fac[s] * age0
    nav0 = fleet0 + ip + prem0[s] + 155 + {"Bear": 270, "Base": 500, "Bull": 800}[s] - I["nibd0"]
    mid0[s] = dict(fleet0=fleet0, nav0=nav0, nav0_nok=nk(nav0))
    pr(f"NAV_0 {s}: fleet {fleet0:.0f} NAV {nav0:.0f} NOK {nk(nav0):.1f} P/NAV {P/nk(nav0):.2f}")
navmkt = (fmv - ip) * age0 + ip + 404 + 155 + 500 - I["nibd0"]
pr(f"NAV market marks: {navmkt:.0f} NOK {nk(navmkt):.1f} P/NAV {P/nk(navmkt):.2f}; age0 {age0:.4f}")
for s in ("Bear", "Base", "Bull"):
    r = R[s]
    rr = (mid0[s]["nav0_nok"] / P) ** (1 / T) - 1
    ng = (r["VT_nok"] / mid0[s]["nav0_nok"]) ** (1 / T) - 1
    pr(f"{s}: re-rating {rr*100:.1f} NAV growth {ng*100:.1f}")
    out[s].update(nav0=mid0[s]["nav0_nok"], rerate=rr, navg=ng)

# V_T bridge Base
b = R["Base"]; ex = b["exit"]
nav0 = mid0["Base"]["nav0"]
nb_T = ex["norseman"] + ex["salt"] + ex["rsv"] + ex["rov"]
vc = nb_T - 155 - out["Base"]["sumG"]
ageing = ex["fleet"] - mid0["Base"]["fleet0"]
roll = ex["firm"] - prem0["Base"]
ret = out["Base"]["sumMF"] - out["Base"]["sumDP"]
pr("\n=== V_T bridge Base ===")
mc = P * SH / FX
for lab, v in (("P", mc), ("rerate", nav0 - mc), ("NAV0", nav0), ("value created", vc), ("ageing", ageing), ("roll-off", roll), ("signed", ex["signed"]), ("tail", ex["tail"]), ("retained", ret)):
    pr(f"{lab:14s} {v:8.1f} {nk(v):7.2f}")
chk = nav0 + vc + ageing + roll + ex["signed"] + ex["tail"] + ret - ip
pr(f"sum (less Implementer receivable {ip}) {chk:.1f} vs VT {b['VT']:.1f}  diff {chk-b['VT']:.2f}")
pr(f"newbuild value at T {nb_T:.0f}; capex in horizon {out['Base']['sumG']:.1f}")
out["bridge"] = dict(mc=mc, nav0=nav0, vc=vc, ageing=ageing, roll=roll, signed=ex["signed"], tail=ex["tail"], ret=ret, chk=chk - b["VT"])

# FCF normalised and Rule 3, exit cross-check
mid_eb = {"Bear": 549 - 3 + 11.2 * (1 - ip / 147), "Base": 742 - 3 + 16.3 * (1 - ip / 147), "Bull": 952 - 3 + 21.8 * (1 - ip / 147) + 0.15 * 0 + (PLSV["fc"] * 15 * 0.92) * 0.5 * 6 * 365 / 1000}
pr("\n=== FCF normalised / cross-check ===")
book0 = 2131.0
da = {"Q4-26": 61.0, "Q1-27": 75, "Q2-27": 75, "Q3-27": 75, "Q4-27": 75, "2028": 310.0, "2029": 315.0}
for s in ("Bear", "Base", "Bull"):
    r = R[s]
    ageing_s = mid0[s]["fleet0"] - r["exit"]["fleet"]
    renew = ageing_s / T
    intx = 0.063 * r["nibd_exit"] + 13.2
    fcfn = mid_eb[s] - 0.086 * mid_eb[s] - intx - 145 - 45 - renew
    pfcf = (P * SH / FX) / fcfn
    ceil = r["irr"] / 0.0144
    exit_pe = r["VT"] / (fcfn + 5)
    ni_mc = mid_eb[s] - 309 - intx - 0.086 * mid_eb[s]
    acc_pe = r["VT"] / ni_mc
    ni = sum(r["rows"][p]["ebitda"] - da[p] - r["rows"][p]["interest"] - r["rows"][p]["tax"] for p in r["rows"])
    book = book0 + ni - out[s]["sumDP"]
    pb = r["VT"] / book
    buyer = (0.08 * r["assets"] - intx) / r["VT"]
    pr(f"{s}: midEB {mid_eb[s]:.1f} renew {renew:.1f} intx {intx:.1f} FCFn {fcfn:.1f} ({nk(fcfn):.2f}) P/FCF {pfcf:.1f} ceil {ceil:.1f} exitPE {exit_pe:.1f} accPE {acc_pe:.1f} book {book:.0f} PB {pb:.2f} buyer {buyer*100:.1f}")
    out[s].update(mid_eb=mid_eb[s], fcfn=fcfn, pfcf=pfcf, ceil=ceil, exit_pe=exit_pe, acc_pe=acc_pe, book=book, pb=pb, buyer=buyer, renew=renew)

# weighted reference
def weighted():
    from collections import defaultdict
    w = {"Bear": 0.25, "Base": 0.5, "Bull": 0.25}
    agg = defaultdict(float)
    for s in w:
        for d0, v in R[s]["cfs"]:
            agg[d0] += w[s] * v
    vt = sum(w[s] * R[s]["VT_nok"] for s in w)
    cfs = [(V0, -P)] + sorted(agg.items()) + [(EXIT, vt)]
    irr = xirr(cfs, V0)
    pk = sum(v / 1.12 ** yf(V0, d0) for d0, v in agg.items()) + vt / 1.12 ** yf(V0, EXIT)
    return irr, pk
wi, wp = weighted()
pr(f"weighted ref IRR {wi*100:.2f} Pk {wp:.1f}")
pr(f"Bull priced {(P-R['Base']['Pk'])/(R['Bull']['Pk']-R['Base']['Pk'])*100:.0f}%")
out["weighted"] = (wi, wp)

# year-end path with interim glide
pr("\n=== Year-end path ===")
age_e26 = ann8(12.5) / ann8(13)
stub_assets = (fmv - ip) * age_e26 + ip + 390 + 170 + 500
for s in ("Base", "Bear", "Bull"):
    r = R[s]
    exA = r["assets"] - r["exit"]["signed"] - r["exit"]["tail"]
    sa = stub_assets - ip
    V = {}
    V[2026] = stub_assets - r["rows"]["Q4-26"]["nibd"]
    V[2027] = sa + (exA - sa) / 3 - r["rows"]["Q4-27"]["nibd"]
    V[2028] = sa + (exA - sa) * 2 / 3 + r["exit"]["signed"] - r["rows"]["2028"]["nibd"]
    V[2029] = r["VT"]
    Dy = {2026: 0, 2027: 0, 2028: 0, 2029: 0}
    for d0, v in r["divs"]:
        Dy[d0.year] += v
    prevV = P
    line = []
    for y in (2026, 2027, 2028, 2029):
        Vn = nk(V[y]); Dn = nk(Dy[y])
        rt = (Dn + Vn - prevV) / prevV
        cfs = [(V0, -P)] + [(d0, nk(v)) for d0, v in r["divs"] if d0.year <= y] + [(D(y, 12, 31), Vn)]
        irr_t = xirr(cfs, V0) if y > 2026 else float("nan")
        line.append((y, round(Dn, 2), round(Vn, 1), round(rt * 100, 1), round(irr_t * 100, 1)))
        prevV = Vn
    pr(s, line)
    out[s]["path"] = line
json.dump(out, open("results.json", "w"), default=str, indent=1)
