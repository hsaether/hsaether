"""DOF inputs, 18 Nov 2026 (docs/DOF-analysis.md v-18 Nov: Supply BBB leading-view update; skill iaf-valuation 2026-11-18.1).
Steps on the 16 Nov inputs (inputs_1116, step "all" = steps 0-3), so each step can be attributed:

step 4: re-mark: P NOK 128.30 (Oslo close 18 Nov 2026), USD/NOK 9.705 (Yahoo NOK=X, 18 Nov 15:00-15:30 UTC bar,
        the Oslo close), valuation date 18 Nov 2026.
step 5: Supply BBB 18 Nov turn call: NS AHTS spot Base Year-1 quarters 57.6 / 67.8 / 49.2 / 65.4 ->
        49.9 / 58.8 / 42.6 / 56.7 GBP k (utilisation kept), on the 1.5 vessel-year 2027 spot pool. Structural run
        unchanged (pool at mid-cycle), so the struct delta moves with the path (as step 2).
step 6: company contracts after the 16 Nov run (Newsweb): Skandi Seven, "Very Large" ($100-200m) 3-year integrated
        FSV contract in Africa (16 Nov 13:21); Skandi Africa, "Very Large" re-contract with TechnipFMC in direct
        continuation (17 Nov). Vessel revenue moved from the open CSV share to firm at today's level: CSV_FIRM
        $70m a year [A] (Skandi Africa ~$50m vessel charter at the $150m mid-point over an assumed 3 years; Skandi
        Seven ~$20m vessel share, the services part sits in the Base services path). Removes that revenue's
        re-pricing in 2027-29 in every scenario (path) and at mid-cycle (structural), and adds the after-tax premium
        over the scenario's mid-cycle for 2027-29 to NAV_0 and the end-of-stub mark. No exit premium (terms end
        ~Q1 2030 [A]).
"""
import datetime as dt
from inputs_1116 import inputs_1116, ahts_delta, AHTS_UTIL, POOL_VY_2027, Q27
from inputs_new import ann8

D = dt.date
AHTS_1116 = (57.6, 67.8, 49.2, 65.4)
AHTS_1118 = (49.9, 58.8, 42.6, 56.7)
CSV_FIRM = 70.0                                     # $m vessel revenue a year moved to firm [A]
OPEN_REV = (0.25 * 450, 0.45 * 450, 0.60 * 450)     # open CSV revenue 2027-29 ($m), skill inputs (inputs_new)
CSV_PATH = {"Bear": (-33, -81, -121), "Base": (-6, -26, -46), "Bull": (14, 37, 46)}
CSV_REL_MID = {"Bear": 28.5 / 49.5 - 1, "Base": 36 / 49.5 - 1, "Bull": 44.2 / 49.5 - 1}


def csv_firm_effect(s):
    """($m EBITDA path delta per year 2027-29, $m struct-run delta per year) for moving CSV_FIRM from open to firm."""
    path = [-CSV_FIRM * CSV_PATH[s][i] / OPEN_REV[i] for i in range(3)]   # re-pricing avoided on the path
    struct = [-CSV_FIRM * CSV_REL_MID[s]] * 3                            # re-pricing to mid-cycle avoided
    return path, struct


def inputs_1118(step="all"):
    st = 99 if step == "all" else step
    I = inputs_1116("all" if st >= 3 else st)
    if st >= 4:
        I["val_date"] = D(2026, 11, 18); I["P"] = 128.30; I["fx"] = 9.705
    if st >= 5:
        dq = ahts_delta(old=AHTS_1116, new=AHTS_1118)
        for q, v in dq.items():
            I["ebitda"]["Base"][q] += v
            I["struct_delta"]["Base"][q] += v
        I["ahts_delta_1118"] = dq
    if st >= 6:
        I["csv_firm"] = {}
        for s in ("Bear", "Base", "Bull"):
            path, struct = csv_firm_effect(s)
            for q in Q27:
                I["ebitda"][s][q] += path[0] / 4
                # structural EBITDA = path - struct_delta; structural gain is struct[0], so delta += path - struct
                I["struct_delta"][s][q] += (path[0] - struct[0]) / 4
            for i, y in ((1, "2028"), (2, "2029")):
                I["ebitda"][s][y] += path[i]
                I["struct_delta"][s][y] += path[i] - struct[i]
            yearly = -CSV_FIRM * CSV_REL_MID[s] * (1 - I["tax"])        # after-tax premium over mid-cycle a year
            pv = yearly * ann8(3) / 1.08 ** ((D(2027, 1, 1) - I["val_date"]).days / 365)
            I["prem0_add"][s] += pv
            if s == "Base":
                I["stub_prem_add"] += yearly * ann8(3)
            I["csv_firm"][s] = dict(path=[round(x, 1) for x in path], struct=[round(x, 1) for x in struct], prem0=round(pv, 1))
    return I


if __name__ == "__main__":
    J = inputs_1118("all")
    print("AHTS delta 18 Nov", {k: round(v, 2) for k, v in J["ahts_delta_1118"].items()}, "total", round(sum(J["ahts_delta_1118"].values()), 2))
    print("CSV firm", J["csv_firm"])
    print("prem0_add", {k: round(v, 1) for k, v in J["prem0_add"].items()}, "stub add", round(J["stub_prem_add"], 1))
