import copy
from dof_model import *
from inputs_new import *

BASE = new_inputs("all")
BASE["struct_delta"] = struct_deltas(BASE)
P = BASE["P"]

def res(I, s="Base", **kw):
    r = run(I, s, **kw)
    return r["irr"] * 100, r["Pk"], r["VT_nok"]

def show(lab, I, s="Base"):
    i, pk, vt = res(I, s)
    print(f"{lab:62s} IRR {i:6.2f}  Pk {pk:6.1f}  MoS {(pk/P-1)*100:6.1f}%  VT {vt:6.1f}")
    return i, pk

print("Base:", res(BASE))
# --- PLSV basis range ---
def plsv(dof_new):
    I = copy.deepcopy(BASE)
    dd = (dof_new - PLSV["dof_ext"]) * 0.92 * 3 * 365 / 1000
    I["ebitda"]["Base"]["2028"] += dd * 11 / 12; I["ebitda"]["Base"]["2029"] += dd
    I["exit"]["Base"]["signed"] += (dof_new - PLSV["dof_new"]) * 0.95 * 3 * 365 / 1000 * (1 - 0.086) * ANN2
    return I, dd
for lab, v in (("PLSV DOF share $114k/day (>USD 500m at its floor)", PLSV["dof_new_lo"]),
               ("PLSV DOF share $137k/day (USD 600m)", PLSV["dof_new_hi"]),
               ("PLSV DOF share $149k/day (50% of the Petrobras total, ~USD 650m)", 653e3 / 4380)):
    I, dd = plsv(v); show(f"{lab} [{dd:+.1f}/yr]", I)
I = copy.deepcopy(BASE)
I["ebitda"]["Base"]["2028"] += 60 * 11 / 12; I["ebitda"]["Base"]["2029"] += 60
show("Earlier hypothesis: +$60m a year 2028-29 (rates vs JV revenue)", I)
# Implementer $147m
I = copy.deepcopy(BASE)
I["sale"] = {"Q2-27": 147.0}
sc = 147 / 133.0
for s, (a, b, c) in {"Base": (14.69, 21.1, 19.6)}.items():
    f = 133 / 147.0
    dlt = [x * f * (1 - sc) for x in (a, b, c)]
    for p, w in (("Q2-27", 0.2), ("Q3-27", 0.4), ("Q4-27", 0.4)): I["ebitda"][s][p] += dlt[0] * w
    I["ebitda"][s]["2028"] += dlt[1]; I["ebitda"][s]["2029"] += dlt[2]
I["exit"]["Base"]["fleet"] -= 14 * 0.894
show("Skandi Implementer at $147m (TradeWinds headline)", I)
# SALT $83m
I = copy.deepcopy(BASE)
I["growth"]["Q4-27"] = (15 + 12 + 71.0, 12 + 9 + 42.6); I["growth"]["2028"] = (60 + 120 + 71.0, 48 + 90 + 42.6)
show("SALT 310 CSVs at ~$83m each (28 Oct inference) instead of ~$103m", I)
# services trim reversed
I = copy.deepcopy(BASE)
for p in ("Q1-27", "Q2-27", "Q3-27", "Q4-27"): I["ebitda"]["Base"][p] += 7 / 4
I["ebitda"]["Base"]["2028"] += 7; I["ebitda"]["Base"]["2029"] += 7
I["exit"]["Base"]["tail"] = 12.3 * (1 - 0.086) / (1 - 0.095)
show("Subsea services path not trimmed (135/145/140; tail back)", I)
# mobilisation not counted
I = copy.deepcopy(BASE)
I["ebitda"]["Base"]["Q1-27"] += 8; I["ebitda"]["Base"]["2028"] += 5
show("PLSV mobilisation/acceptance gaps not counted (+8 Q1-27, +5 2028)", I)
# tax 9.5%
I = copy.deepcopy(BASE); I["tax"] = 0.095
show("Tax payable 9.5% of EBITDA (previous guide) instead of 8.6%", I)
# FX 9.29
I = copy.deepcopy(BASE); I["fx"] = 9.2944
show("USD/NOK 9.29 (Equity BBB spot, 5 Nov) instead of 9.552", I)
I = copy.deepcopy(BASE); I["fx"] = 9.80
show("USD/NOK 9.80", I)
# exit fleet
for f in (0.8, 0.9, 1.1, 1.2):
    I = copy.deepcopy(BASE); I["exit"]["Base"]["fleet"] *= f
    show(f"Exit fleet value x {f}", I)
for lab, f in (("Economic life 27.5 years", (ann8(12) / ann8(15.5)) / 0.820), ("Economic life 30 years", (ann8(14.5) / ann8(18)) / 0.820)):
    I = copy.deepcopy(BASE); I["exit"]["Base"]["fleet"] *= f
    show(f"{lab} (fleet x {f:.3f})", I)
# life x factor grid
print("grid fleet factor x life")
for ff in (0.8, 0.9, 1.0, 1.1):
    row = []
    for lf in (1.0, (ann8(12) / ann8(15.5)) / 0.820, (ann8(14.5) / ann8(18)) / 0.820):
        I = copy.deepcopy(BASE); I["exit"]["Base"]["fleet"] *= ff * lf
        row.append(round(res(I)[0], 1))
    print(ff, row)
# re-discount at Oslo mid-cycle 8.9%
def rd(n, r):
    return ann8(n, r) / ann8(n, 0.08)
I = copy.deepcopy(BASE)
e = I["exit"]["Base"]
e["fleet"] *= rd(9.5, 0.089); e["salt"] *= rd(23, 0.089); e["norseman"] *= rd(12, 0.089)
show("Exit marks re-discounted at Oslo mid-cycle return 8.9%", I)
r = run(I, "Base"); print("   buyer return check", (0.089 * r["assets"] - (0.063 * r["nibd_exit"] + 13.2)) / r["VT"])
# without signed premium
I = copy.deepcopy(BASE); I["exit"]["Base"]["signed"] = 0
show("Without the premium on backlog signed in the scenario", I)
for s in ("Bear", "Bull"):
    J = copy.deepcopy(BASE); J["exit"][s]["signed"] = 0
    show(f"   {s} without signed premium", J, s)
# tails
I = copy.deepcopy(BASE); I["exit"]["Base"]["tail"] = (29.0 + 26.2) * (1 - 0.086) / (1 - 0.095)
show("Tails on every material row (AHTS +29, CSV +26)", I)
# DOFCON at 100% in FMV
I = copy.deepcopy(BASE); I["exit"]["Base"]["fleet"] -= 300 * 0.82 * 0.954
show("DOFCON PLSVs in the broker FMV at 100% (anchor -$300m)", I)
# AHTS mid-cycle 32k
I = copy.deepcopy(BASE); I["exit"]["Base"]["fleet"] -= 4081 * 0.82 * 0.22 * (1 - (32 * 1.3327 * 0.6 * 0.365 - 5.475) / (38 * 1.3327 * 0.6 * 0.365 - 5.475))
show("NS AHTS mid-cycle GBP 32k (asset-implied)", I)
# services multiple
for m in (0, 6):
    I = copy.deepcopy(BASE); I["exit"]["Base"]["services"] = 125 * m
    show(f"Subsea services valued at {m}x", I)
# AHTS pool +1 vessel-year 2028
for s, dd in (("Base", 20.2 - 10.8 - 5.4 * 0), ("Bear", 3.8 - 10.8)):
    I = copy.deepcopy(BASE)
    if s == "Base": dd = (65 * 1.3327 * 0.64 * 0.365 - 5.475) - (47 * 0.95 * 0.365 - 5.475)
    else: dd = (38 * 1.3327 * 0.50 * 0.365 - 5.475) - (47 * 0.95 * 0.365 - 5.475)
    I["ebitda"][s]["2028"] += dd
    show(f"AHTS spot pool +1 vessel-year in 2028 ({s}, {dd:+.1f})", I, s)
# RSV
def rsv(c, off=False):
    I = copy.deepcopy(BASE)
    old = (48, 120, 120)
    new = (0, 0, 0) if off else (0.4 * c, c, c)
    keys = ("2027", "2028", "2029")
    for k_, o, n in zip(keys, old, new):
        if k_ == "2027":
            for q in ("Q1-27", "Q2-27", "Q3-27", "Q4-27"):
                g, d_ = I["growth"][q]; I["growth"][q] = (g + (n - o) / 4, d_ + 0.75 * (n - o) / 4)
        else:
            g, d_ = I["growth"][k_]; I["growth"][k_] = (g + n - o, d_ + 0.75 * (n - o))
    I["exit"]["Base"]["rsv"] = 0 if off else 549 - 1.6 * c * 0.85
    return I
show("RSV cost $100m each", rsv(100)); show("RSV cost $140m each", rsv(140)); show("RSVs moved off DOF's balance sheet", rsv(0, True))
# payout
for po in (0.75, 1.0):
    I = copy.deepcopy(BASE); I["payout"] = po
    show(f"Payout {int(po*100)}%", I)
# Base cash flows with Bear / Bull exit
for s in ("Bear", "Bull"):
    I = copy.deepcopy(BASE); I["exit"]["Base"] = copy.deepcopy(BASE["exit"][s])
    show(f"Base cash flows with {s} exit", I)
# k
for k in (0.10, 0.13, 0.14):
    I = copy.deepcopy(BASE); I["k"] = k
    print(f"k {k}: Pk {run(I,'Base')['Pk']:.1f}")
# price break-evens
r = run(BASE, "Base")
print(f"P clears <= {r['Pk']/1.02:.1f}; fails > {r['Pk']/0.98:.1f}")
# exit fleet factor for P_k = P*1.02 and P_k = P
for target, lab in ((P, "k at today's price"), (P * 1.02, "clears")):
    lo, hi = 0.9, 1.2
    for _ in range(50):
        m = (lo + hi) / 2
        I = copy.deepcopy(BASE); I["exit"]["Base"]["fleet"] *= m
        if run(I, "Base")["Pk"] < target: lo = m
        else: hi = m
    print(f"fleet factor for {lab}: {m:.3f}")

print("\n=== Driver breakdown ===")
for s in ("Bear", "Bull"):
    steps = []
    I = copy.deepcopy(BASE); I["ebitda"]["Base"] = copy.deepcopy(BASE["ebitda"][s])
    steps.append(("sector paths in the window (EBITDA)", res(I)))
    I["exit"]["Base"]["fleet"] = BASE["exit"][s]["fleet"]
    steps.append(("+ exit fleet marks", res(I)))
    for kk in ("norseman", "salt", "rsv", "services"): I["exit"]["Base"][kk] = BASE["exit"][s][kk]
    steps.append(("+ newbuild and services values", res(I)))
    for kk in ("firm", "signed", "tail"): I["exit"]["Base"][kk] = BASE["exit"][s][kk]
    steps.append(("+ backlog premiums and tail", res(I)))
    print(s)
    for lab, (i, pk, vt) in steps:
        print(f"   {lab:40s} IRR {i:6.2f} Pk {pk:6.1f} VT {vt:6.1f}")
