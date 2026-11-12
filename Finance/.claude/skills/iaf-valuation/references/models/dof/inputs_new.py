"""New inputs, 12 Nov 2026 (Q3 report). Built as old + explicit deltas so every step can be attributed."""
import datetime as dt, copy
from inputs_old import old_inputs
D = dt.date
SH = 246.278655
GBPUSD = 1.3327  # Supply BBB convention (17 Oct 1.33265; spot 12 Nov 1.326)
TAXN = 0.086

def ann8(n, r=0.08):
    return (1 - (1 + r) ** -n) / r

# --- PLSV (DOFCON) on DOF's basis ---
PLSV = dict(
    total_new=(305 + 295 + 295) / 3.0,          # Petrobras round, $k/day at 100% (charter + services)
    dof_new=550e3 / (3 * 4 * 365),               # $k/day DOF share: ">USD 500m" read as 500-600, mid 550
    dof_new_lo=500e3 / (3 * 4 * 365), dof_new_hi=600e3 / (3 * 4 * 365),
    dof_ext=135e3 / 1066,                         # Buzios/Recife extension ">USD 130m" for 516+550 days, read as 130-140
    norskan=30.0,                                 # $k/day marine operations (Norskan) inside DOF's share [A]
)
PLSV["C_new"] = (PLSV["dof_new"] - PLSV["norskan"]) * 2      # DOFCON (JV) day at 100%
PLSV["fc"] = PLSV["C_new"] / PLSV["total_new"]                # JV share of the Petrobras total
MID = {"Bear": (215, 0.82), "Base": (250, 0.88), "Bull": (300, 0.92)}  # Supply BBB 12 Nov PLSV mid-cycle (rate, MCU)
ANN2 = 1 / 1.08 + 1 / 1.08 ** 2

def dofcon_premium(s, tax=TAXN, structural=False):
    r, u = MID[s]
    Cmc = PLSV["fc"] * r
    if structural:
        prem = Cmc * (0.95 - u)
    else:
        prem = PLSV["C_new"] * 0.95 - Cmc * u
    return prem * 0.5 * 3 * 365 / 1000 * (1 - tax) * ANN2

def dofcon_struct_delta(s):
    r, u = MID[s]
    Cmc = PLSV["fc"] * r
    return (Cmc * u - PLSV["C_new"] * 0.92) * 0.5 * 3 * 365 / 1000   # $m/yr vs the signed path

def new_inputs(step="all"):
    """step controls cumulative application for attribution:
    0 old; 1 price/FX/date; 2 Q3 balance sheet + dividends + Q4 guidance; 3 subsea/core trim (+tail);
    4 tax 8.6%; 5 PLSV basis (signed terms, mobilisation, premium); 6 Implementer $133m; 7 SALT $103m;
    8 Supply BBB 12 Nov (Bull PLSV mid-cycle; broker FMV 4,081 print)."""
    I = old_inputs()
    st = 99 if step == "all" else step
    q = lambda a, b, c, d, e, f, g: {"Q4-26": a, "Q1-27": b, "Q2-27": c, "Q3-27": d, "Q4-27": e, "2028": f, "2029": g}
    def add(scen, deltas):
        for p, v in deltas.items():
            I["ebitda"][scen][p] += v
    tax_old = 0.095
    fac = {"Bear": 0.567, "Base": 0.954, "Bull": 1.420}
    fmv = 4085.0
    impl_price = 147.0
    # exit components (recomputed from parts)
    impl_factor = {"Bear": 0.67, "Base": 1.00, "Bull": 1.37}
    firm = {"Bear": 136.0, "Base": 86.0, "Bull": 54.0}
    rio = {"Bear": 11.4, "Base": 19.5, "Bull": 22.5}
    dofcon_old = {"Bear": 38.9, "Base": 35.5, "Bull": 33.0}
    tail = {"Bear": 3.4, "Base": 12.3, "Bull": 0.0}
    salt_capex = (90.25, 66.8) if st >= 7 else (71.0, 42.6)
    if st >= 1:
        I["val_date"] = D(2026, 11, 12); I["P"] = 128.6; I["fx"] = 9.552
    if st >= 2:
        I["nibd0"] = 1234.0; I["cash0"] = 488.0
        for s in I["ebitda"]: I["ebitda"][s]["Q4-26"] = 208.0
        I["div_q3_26"] = 0.40 * SH; I["div_q4_26"] = 0.40 * SH
    if st >= 3:
        for s in ("Bear", "Base", "Bull"):
            add(s, {"Q1-27": -2.5, "Q2-27": -2.5, "Q3-27": -2.5, "Q4-27": -2.5})   # core -3/yr, subsea -7 (2027)
            add(s, {"2028": -3.0, "2029": -3.0})
        for s in ("Base", "Bull"):
            add(s, {"2028": -7.0, "2029": -7.0})
        tail["Base"] = 0.0   # services gap 133 vs 125 = +6.4% < 10%
    tax = TAXN if st >= 4 else tax_old
    I["tax"] = tax
    taxadj = (1 - tax) / (1 - tax_old)
    if st >= 5:
        # signed terms in all scenarios: in-window delta vs the 28 Oct row-relative block; mobilisation
        old_blk = {"Bear": (0, -22, -25), "Base": (0, 0, 1), "Bull": (0, 18, 20)}
        for s, (a, b, c) in old_blk.items():
            add(s, {"Q1-27": -8.0})                      # Acu/Niteroi/Vitoria mobilisation & acceptance 1Q27 (chart) [A]
            add(s, {"2028": -b - 5.0, "2029": -c})        # signed flat vs current on DOF's basis; ~3 weeks acceptance Jan-28
    if st >= 6:
        impl_price = 133.0
        sc = impl_price / 147.0
        old_impl = {"Bear": (9.81, 12.0, 10.4), "Base": (14.69, 21.1, 19.6), "Bull": (18.5, 31.5, 31.0)}
        for s, (a, b, c) in old_impl.items():
            dlt = [x * (1 - sc) for x in (a, b, c)]
            add(s, {"Q2-27": dlt[0] * 0.2, "Q3-27": dlt[0] * 0.4, "Q4-27": dlt[0] * 0.4, "2028": dlt[1], "2029": dlt[2]})
        I["sale"] = {"Q2-27": impl_price}
        I["sale_repay"] = {"Q2-27": 34.0}   # Q3 bridge: minimum debt repayment ~$34m, rest kept as cash [B]
    if st >= 8:
        fmv = 4081.0
        fac["Bull"] = 1.420 + 0.15 * (512 - 470) / 496.0
    # growth capex (SALT)
    g = I["growth"]
    g["Q4-27"] = (15 + 12 + salt_capex[0], 12 + 9 + salt_capex[1])
    g["2028"] = (60 + 120 + salt_capex[0], 48 + 90 + salt_capex[1])
    # exit assets
    ex = {}
    for s in ("Bear", "Base", "Bull"):
        fleet = fmv * 0.820 * fac[s] - impl_price * 0.894 * impl_factor[s]
        dprem = dofcon_premium(s, tax) if st >= 5 else dofcon_old[s] * taxadj
        ex[s] = dict(fleet=fleet, firm=firm[s] * taxadj, signed=dprem + rio[s] * taxadj,
                     norseman={"Bear": 150, "Base": 165, "Bull": 175}[s], salt={"Bear": 148, "Base": 224, "Bull": 306}[s],
                     rsv={"Bear": 330, "Base": 386, "Bull": 400}[s], rov=135.0,
                     services={"Bear": 270, "Base": 500, "Bull": 800}[s], tail=tail[s] * taxadj)
    if st == 0:
        ex = old_inputs()["exit"]
    I["exit"] = ex
    # structural signed premium
    rio_struct = {"Bear": 12.1, "Base": 9.1, "Bull": 7.1}
    if st >= 5:
        I["signed_struct"] = {s: dofcon_premium(s, tax, structural=True) + rio_struct[s] * taxadj for s in MID}
    I["meta"] = dict(fmv=fmv, fac=fac, impl_price=impl_price, salt_capex=salt_capex, tax=tax)
    return I

# ---------- structural deltas (path - mid-cycle) per block, for the new inputs ----------
def struct_deltas(I):
    pool_vy = {"2027": 1.5, "2028": 3.5, "2029": 4.5}
    def pool_mid(s):
        r, u = {"Bear": (30, 0.52), "Base": (38, 0.60), "Bull": (50, 0.66)}[s]
        return r * GBPUSD * u * 365 / 1000 - 15 * 365 / 1000
    pool_path = {"Bear": (9, 13, 14), "Base": (26, 52, 61), "Bull": (53, 116, 133)}
    csv_path = {"Bear": (-33, -81, -121), "Base": (-6, -26, -46), "Bull": (14, 37, 46)}
    csv_rel = {"Bear": 28.5 / 49.5 - 1, "Base": 36 / 49.5 - 1, "Bull": 44.2 / 49.5 - 1}
    open_sh = (0.25, 0.45, 0.60)
    salt_path = {"Bear": (1, 14, 13), "Base": (2, 25, 27), "Bull": (2, 38, 43)}
    def salt_mid(s):
        r, u = {"Bear": (38, 0.75), "Base": (45, 0.80), "Bull": (52, 0.85)}[s]
        return r * GBPUSD * u * 365 / 1000 - 18 * 365 / 1000
    salt_vy = (0.125, 1.75, 2.0)
    braz_path = {"Bear": (0, -1, -4), "Base": (0, 1, 6), "Bull": (0, 4, 14)}
    def braz_mid(s):
        r, u = {"Bear": (55, 0.78), "Base": (62, 0.83), "Bull": (70, 0.87)}[s]
        return (r * u - 55 * 0.92) * 365 / 1000
    braz_vy = (0, 0.75, 1.75)
    serv_path = {"Bear": (108, 100, 90), "Base": (128, 138, 133), "Bull": (143, 163, 168)}
    serv_mid = {"Bear": 90, "Base": 125, "Bull": 160}
    sc = I["meta"]["impl_price"] / 147.0
    impl_path = {"Bear": (-9.81 * sc, -12.0 * sc, -10.4 * sc), "Base": (-14.69 * sc, -21.1 * sc, -19.6 * sc), "Bull": (-18.5 * sc, -31.5 * sc, -31.0 * sc)}
    impl_mid = {"Bear": -11.2 * sc, "Base": -16.3 * sc, "Bull": -21.8 * sc}
    out = {}
    for s in ("Bear", "Base", "Bull"):
        yrs = {}
        for i, y in enumerate(("2027", "2028", "2029")):
            d = 0.0
            d += pool_path[s][i] - pool_vy[y] * pool_mid(s)
            d += csv_path[s][i] - open_sh[i] * csv_rel[s] * 450
            d += salt_path[s][i] - salt_vy[i] * salt_mid(s)
            d += braz_path[s][i] - braz_vy[i] * braz_mid(s)
            d += serv_path[s][i] - serv_mid[s]
            d += impl_path[s][i] - impl_mid[s] * (0.625 if y == "2027" else 1.0)
            if y == "2028": d += -dofcon_struct_delta(s) * 11 / 12
            if y == "2029": d += -dofcon_struct_delta(s)
            yrs[y] = d
        # quarterly 2027 split: equal, except SALT (Q4) and Implementer (Q2-Q4 0.2/0.4/0.4)
        y27 = yrs["2027"]
        salt27 = salt_path[s][0] - salt_vy[0] * salt_mid(s)
        impl27 = impl_path[s][0] - impl_mid[s] * 0.625
        rest = y27 - salt27 - impl27
        out[s] = {"Q4-26": 0.0, "Q1-27": rest / 4, "Q2-27": rest / 4 + impl27 * 0.2, "Q3-27": rest / 4 + impl27 * 0.4,
                  "Q4-27": rest / 4 + impl27 * 0.4 + salt27, "2028": yrs["2028"], "2029": yrs["2029"]}
    return out
