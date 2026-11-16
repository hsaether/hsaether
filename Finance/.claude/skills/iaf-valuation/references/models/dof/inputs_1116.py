"""DOF inputs, 16 Nov 2026 (docs/dof-analysis.md, upstream update: Supply BBB 16 Nov AHTS rule; re-mark; skill 2026-11-12.1).
Built as the 12 Nov inputs (inputs_new.py, step "all") plus explicit deltas, so each step can be attributed.

step 0: 12 Nov inputs (reproduces the 12 Nov full update: Base 11.76%, P_k 127.9)
step 1: re-mark: P NOK 127.10 (Oslo close 13 Nov 2026, 16:20 CET), USD/NOK 9.550, valuation date 16 Nov 2026
step 2: Supply BBB 16 Nov: NS AHTS spot (> 22k bhp) Base Year-1 quarters 72.0 / 84.8 / 61.5 / 81.8 ->
        57.6 / 67.8 / 49.2 / 65.4 GBP k at utilisation 60 / 66 / 60 / 62% (kept), on DOF's spot pool of
        1.5 vessel-years in 2027 (even spread, 1.5 vessels a quarter). The structural run is unchanged
        (the pool sits at mid-cycle there), so the struct delta moves with the path.
step 3: iaf-valuation 2026-11-12.1 rule "awarded, not yet signed": the DOFCON 2028 PLSV terms (tender result,
        signatures left) count as firm today: exit premium for the full term (to ~Jan 2032, not capped),
        in NAV_0 and the end-of-stub mark (Base mid-cycle basis, as the other firm-today premiums), and not
        re-priced in the structural run (firm days unchanged; full premium kept).
The stub Q4-26 (66 -> 43) does not reach the model: Q4-26 EBITDA is DOF's 12 Nov guidance mid-point and the
non-crane spot pool (Minder, Saltfjord) is on firm cover Nov 2026 - Feb 2027 (Q3 chart). 2028-29, mid-cycle,
Bear and Bull rows are unchanged upstream.
"""
import copy, datetime as dt
from inputs_new import new_inputs, struct_deltas, GBPUSD, dofcon_premium, dofcon_struct_delta, ANN2, ann8

D = dt.date
POOL_VY_2027 = 1.5
AHTS_OLD = (72.0, 84.8, 61.5, 81.8)
AHTS_NEW = (57.6, 67.8, 49.2, 65.4)
AHTS_UTIL = (0.60, 0.66, 0.60, 0.62)
QDAYS = 365 / 4.0
Q27 = ("Q1-27", "Q2-27", "Q3-27", "Q4-27")


def ahts_delta(old=AHTS_OLD, new=AHTS_NEW, util=AHTS_UTIL, vy=POOL_VY_2027):
    """$m EBITDA per 2027 quarter from the NS AHTS spot row change (opex unchanged)."""
    return {q: (n - o) * u * GBPUSD * QDAYS * vy / 1000 for q, o, n, u in zip(Q27, old, new, util)}


def inputs_1116(step="all"):
    st = 99 if step == "all" else step
    I = new_inputs("all")
    I["struct_delta"] = struct_deltas(I)
    if st >= 1:
        I["val_date"] = D(2026, 11, 16); I["P"] = 127.10; I["fx"] = 9.550
    if st >= 2:
        dq = ahts_delta()
        for q, v in dq.items():
            I["ebitda"]["Base"][q] += v
            I["struct_delta"]["Base"][q] += v   # structural run: pool at mid-cycle, unchanged
        I["ahts_delta"] = dq
    I["prem0_add"] = {"Bear": 0.0, "Base": 0.0, "Bull": 0.0}; I["stub_prem_add"] = 0.0
    if st >= 3:
        ann_full = ANN2 + (1 / 12) / 1.08 ** (2 + 1 / 12)          # Jan 2030 - Jan 2032 after exit
        start = D(2028, 2, 1)
        for sc in ("Bear", "Base", "Bull"):
            tax = I["tax"]
            dp = dofcon_premium(sc, tax)                            # capped 2-year premium (in "signed")
            dps = dofcon_premium(sc, tax, structural=True)
            yearly = dp / ANN2                                      # after-tax premium a year, DOF share
            ex = I["exit"][sc]
            ex["signed"] -= dp
            ex["firm"] += yearly * ann_full
            I["signed_struct"][sc] -= dps                           # Rio/Botafogo only in the structural run
            dsd = dofcon_struct_delta(sc)
            I["struct_delta"][sc]["2028"] += dsd * 11 / 12          # undo the mid-cycle re-pricing of the PLSV days
            I["struct_delta"][sc]["2029"] += dsd
            I["prem0_add"][sc] = yearly * ann8(4) / 1.08 ** ((start - I["val_date"]).days / 365)
        yb = dofcon_premium("Base", I["tax"]) / ANN2
        I["stub_prem_add"] = yb * ann8(4) / 1.08 ** ((start - D(2026, 12, 31)).days / 365)
        I["plsv_firm"] = {sc: dofcon_premium(sc, I["tax"]) / ANN2 * ann_full for sc in ("Bear", "Base", "Bull")}
    return I


if __name__ == "__main__":
    J = inputs_1116("all")
    print("PLSV firm premium at exit", {k: round(v, 1) for k, v in J["plsv_firm"].items()}, "NAV_0 add", {k: round(v, 1) for k, v in J["prem0_add"].items()}, "stub add", round(J["stub_prem_add"], 1))
    print("exit firm/signed", {k: (round(v["firm"], 1), round(v["signed"], 1)) for k, v in J["exit"].items()}, "signed_struct", {k: round(v, 1) for k, v in J["signed_struct"].items()})
    dq = ahts_delta()
    print({k: round(v, 2) for k, v in dq.items()}, "total", round(sum(dq.values()), 2))
    # Bear and Bull: same pool at their own (unchanged) rows; a vessel-year of crane AHTS on spot in 2027:
    print("per vessel-year 2027 (Base)", round(sum(dq.values()) / POOL_VY_2027, 2))
