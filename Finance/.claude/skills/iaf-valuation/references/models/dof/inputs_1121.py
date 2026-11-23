"""DOF inputs, 21 Nov 2026 (docs/DOF-analysis.md v-21 Nov: ex-dividend re-mark; skill iaf-valuation 2026-11-18.1).
Step on the 18 Nov inputs (inputs_1118, step "all" = steps 0-6), so the change can be attributed:

step 7: ex-dividend re-mark: P NOK 124.00 (Oslo close Fri 20 Nov 2026, the ex-date of the Q3 dividend), USD/NOK 9.750
        (Yahoo NOK=X, 20 Nov 15:00-15:30 UTC bar close 9.7505, the Oslo close; Norges Bank fixing 9.7525), valuation
        date 20 Nov 2026. The Q3-26 dividend ($0.40 = $98.5m, NOK 3.87252 paid 30 Nov) leaves D_t (q3_ex flag in
        dof_model.run); the company still pays it from cash in Q4-26, so net debt and V_t in USD are unchanged.
        NAV_0 deducts it as a payable to the old holders (div_payable, used in report.py); the V_T bridge's retained
        cash then excludes it (counted once). Supply BBB 21 Nov kept every row the 18 Nov version had: no path change.
"""
import datetime as dt
from inputs_1118 import inputs_1118

D = dt.date


def inputs_1121(step="all"):
    st = 99 if step == "all" else step
    I = inputs_1118("all" if st >= 6 else st)
    if st >= 7:
        I["val_date"] = D(2026, 11, 20); I["P"] = 124.00; I["fx"] = 9.750
        I["q3_ex"] = True
        I["div_payable"] = I["div_q3_26"]
    return I


if __name__ == "__main__":
    J = inputs_1121("all")
    print(J["val_date"], J["P"], J["fx"], J["div_payable"])
