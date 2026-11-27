"""DOF inputs, 27 Nov 2026 (docs/DOF-analysis.md v-27 Nov: holder build-up news and price re-mark; skill iaf-valuation 2026-11-26.1).
Step on the 25 Nov inputs (inputs_1125, step "all" = steps 0-9), so the change can be attributed:

step 10: re-mark: P NOK 133.90 (Oslo close Thu 26 Nov 2026, Yahoo DOFG.OL; 27 Nov not yet trading at the run),
         USD/NOK 9.7658 (Norges Bank fixing 26 Nov 2026, 14:15 CET; the price-day convention of this document),
         valuation date 26 Nov 2026. Still ex the Q3 dividend (paid 30 Nov; payable in NAV_0).
         No model input other than price, FX and date moves: the holder build-up (A.P. Moller Maritime, Fredriksen)
         is a Step 6b signal and a Bull-side optionality, never a Base input.
"""
import datetime as dt
from inputs_1125 import inputs_1125

D = dt.date


def inputs_1127(step="all"):
    st = 99 if step == "all" else step
    I = inputs_1125("all" if st >= 9 else st)
    if st >= 10:
        I["val_date"] = D(2026, 11, 26); I["P"] = 133.90; I["fx"] = 9.7658
    return I


if __name__ == "__main__":
    J = inputs_1127("all")
    print(J["val_date"], J["P"], J["fx"])
