# Equity Market BBB — scripts (initial run 11 Oct 2026)

Copy the scripts to the scratchpad, create a `data/` folder there, and run them with `py -I`
from that folder (never from inside a download folder). They hold the 11 Oct 2026 inputs as
literals; update the inputs from the current upstream documents before each run.

| Script | Does | Run as |
|---|---|---|
| `fetchd.py` | Yahoo daily closes → month-end series in `data/d_<sym>.json` | `py -I fetchd.py OSEBX.OL BZ=F NOK=X EURNOK=X URTH ACWI ^GSPC` |
| `quotes.py` | Yahoo quote API with cookie + crumb (price, market cap, P/E, P/B, yield) | `py -I quotes.py data/q.json EQNR.OL DNB.OL …` |
| `trend.py` | Consensus EPS CY / CY+1 and analyst count (`earningsTrend`) | `py -I trend.py EQNR.OL …` |
| `summ.py` | ETF look-through: sector weights, top holdings, inverted P/E and P/B | `py -I summ.py OBXD.OL NORW URTH ACWI` |
| `corr2.py` | Correlations, betas, regressions, rolling 36-month, episodes, annual returns | `py -I corr2.py` |
| `bottomup.py` | Oslo block P/E (CY, CY+1), earnings shares, dividend yield | `py -I bottomup.py` (weights and consensus as literals) |
| `i44.py` | I-44 / USD / EUR (Norges Bank daily fixings → month-end) vs Brent and World: correlations, regressions, rolling, I-44 levels and episodes. Needs `nb/exr_daily.csv` and `nb/exr_monthly.csv` from the Norges Bank API (`EXR/B.USD+EUR+I44+TWI.NOK.SP?format=csv&startPeriod=1995-01-01&locale=en`, and `EXR/M.I44+USD+EUR.NOK.SP` from 1990) and Yahoo long series in `data/long_*.json` | `py -I i44.py` |
| `model.py` | Scenario model: EPS, P/E, FX paths → annual returns, window IRR, P_k, E / R | `py -I model.py` |
| `triggers.py` | Solves the trigger levels and runs the sensitivities (imports `model.py`) | `py -I triggers.py` |

Model inputs to refresh each run (all in `model.py`): stub length, NIBOR path (HY BBB), Brent
path and mid-cycle (oil BBB), B_cons and block shares (bottom-up), P/E paths, payout, USD/NOK
path, World EPS path.
