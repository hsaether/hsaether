"""DOF inputs, 25 Nov 2026 (docs/DOF-analysis.md v-25 Nov: Skandi Forza sale and re-mark; skill iaf-valuation 2026-11-24.1).
Steps on the 21 Nov inputs (inputs_1121, step "all" = steps 0-7), so each step can be attributed:

step 8: re-mark: P NOK 126.00 (Oslo close Tue 24 Nov 2026), USD/NOK 9.792 (Norges Bank fixing 24 Nov 2026),
        valuation date 24 Nov 2026. Still ex the Q3 dividend (payable in NAV_0).
step 9: Skandi Forza sale (DOF release 24 Nov 2026 10:44 [F]: 2008 CSV; delivery Q4 2026; 2-year bareboat charterback;
        minority stake in the buyer retained; gain ~$35m over book at delivery; net cash ~$30m after debt repayment,
        the stake and tax; price and buyer not disclosed).
        Own assumptions [A]: price G = $62m = net cash 30 + debt repaid R 18 (~26% of price, Implementer ratio
        34/133) + stake S 9 + tax X 5; book ~$27m (G - 35). Broker mark at 30 Jun = G (sold at the mark, as the
        Implementer). Bareboat hire ~$12m a year (~$33k a day) Jan 2027 - Dec 2028, in opex (all scenarios);
        DOF keeps Forza's revenue and opex to the charter end, so its contracts and the 'Forza reversal +8' line
        stay in 2027-28 and leave with the vessel in 2029 (inside the 2029 loss below, not removed twice).
        2029 EBITDA lost = Forza at the NS CSV row x 1.0, opex $20k a day: Bear 6.0 / Base 12.6 / Bull 20.8;
        mid-cycle 6.6 / 10.2 / 14.2 (structural run and FCF_normalised).
        Cash: Q4-26 NIBD -(30 + 18) = -48, cash +30 (sale 48, repay 18). Stake at cost $9m in NAV_0 and V_T.
        Exit fleet: Forza out at its own age (25-year life, 18 years at mid-2026 -> 0.567 at exit) x the CSV
        factor 0.67 / 1.00 / 1.37 (Implementer precedent). NAV_0: fleet ex Forza, receivable G - X = 57.
"""
import datetime as dt
from inputs_1121 import inputs_1121
from inputs_new import ann8, GBPUSD

D = dt.date
FZ = dict(G=62.0, R=18.0, S=9.0, X=5.0, hire=12.0, opex=20.0)
FZ_AGE_T = ann8(25 - 18 - 3.5) / ann8(25 - 18)        # own age factor 30 Jun 2026 -> exit
CSV_FAC = {"Bear": 0.67, "Base": 1.00, "Bull": 1.37}
ROW29 = {"Bear": (38, 0.72), "Base": (50, 0.82), "Bull": (65, 0.89)}     # Supply BBB NS CSV 2029
ROWMC = {"Bear": (38, 0.75), "Base": (45, 0.80), "Bull": (52, 0.85)}     # mid-cycle


def fz_eb(rate, util):
    return rate * util * GBPUSD * 365 / 1000 - FZ["opex"] * 365 / 1000


def inputs_1125(step="all"):
    st = 99 if step == "all" else step
    I = inputs_1121("all" if st >= 7 else st)
    if st >= 8:
        I["val_date"] = D(2026, 11, 24); I["P"] = 126.00; I["fx"] = 9.792
    if st >= 9:
        I["sale"] = dict(I["sale"]); I["sale"]["Q4-26"] = FZ["G"] - FZ["S"] - FZ["X"]      # NIBD -48
        I["sale_repay"] = dict(I["sale_repay"]); I["sale_repay"]["Q4-26"] = FZ["R"]          # cash +30
        lost29 = {s: fz_eb(*ROW29[s]) for s in ROW29}
        lostmc = {s: fz_eb(*ROWMC[s]) for s in ROWMC}
        for s in ("Bear", "Base", "Bull"):
            for q in ("Q1-27", "Q2-27", "Q3-27", "Q4-27"):
                I["ebitda"][s][q] -= FZ["hire"] / 4
            I["ebitda"][s]["2028"] -= FZ["hire"]
            I["ebitda"][s]["2029"] -= lost29[s]
            I["struct_delta"][s]["2029"] += -lost29[s] + lostmc[s]
            I["exit"][s]["fleet"] -= FZ["G"] * FZ_AGE_T * CSV_FAC[s]
            I["exit"][s]["stake"] = FZ["S"]
        I["forza"] = dict(FZ, age_T=FZ_AGE_T, lost29=lost29, lostmc=lostmc,
                          exit_out={s: FZ["G"] * FZ_AGE_T * CSV_FAC[s] for s in CSV_FAC})
    return I


if __name__ == "__main__":
    J = inputs_1125("all")
    f = J["forza"]
    print("age_T", round(f["age_T"], 3), "lost29", {k: round(v, 1) for k, v in f["lost29"].items()},
          "lostmc", {k: round(v, 1) for k, v in f["lostmc"].items()}, "exit out", {k: round(v, 1) for k, v in f["exit_out"].items()})
