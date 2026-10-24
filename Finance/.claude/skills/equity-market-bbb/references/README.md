# Equity Market BBB — scripts (market only; initial run 11 Oct 2026)

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

**17 Oct 2026 — Equity BBB Update 1 (World from the AI split; Oslo repriced).** Copy `upd.py`,
`osl.py` and `idxai3.py` (+ `dl2/urth_ai.json`, URTH weights of 9 Oct) into one scratch
folder and run with `py -I`.

| Script | Does | Run as |
|---|---|---|
| `upd.py` | World = company blocks + AI layer blocks + energy (imports `idxai3.py`, repriced to the 16 Oct closes, Brent Base 2027 88) + an explicit rest path per scenario (`REST_EPS`, `REST_PE`, `REST_PAY`); returns in NOK, E / R, sensitivities, triggers; `only_rest_old=True` reruns the 11 Oct top-down path | `py -I upd.py` |
| `osl.py` | Oslo on the 11 Oct block model at the 16 Oct price, Brent Base 2027 88, USD earnings at the 16 Oct NOK spot, stub 75 days; return split, sensitivities, triggers | `py -I osl.py` |

**18 Oct 2026 — amendment (skill 2026-10-18.1: one retained-cash and payout rule, currency mix).**
`osl.py` and `upd.py` above were replaced; the 17 Oct versions are in git history. Run from one
scratch folder with `idxai3.py` and `dl2/urth_ai.json` next to them.

| Script | Does | Run as |
|---|---|---|
| `osl.py` | Oslo: payout per block (E 0.76, F 0.63, O 0.56), energy cash conversion 0.80 credited to V_t, energy on USD/NOK and the O block's foreign half on I-44. Prints returns, return split (EPS, re-rating, retained cash), structural run, sensitivities (Brent, multiples ±10% and ±1, NOK ±10%, energy cash conversion), triggers with P/B and P/E (MSCI scaled from 30 Sep), the Brent trigger move both ways, and the exit P/B–ROE check | `py -I osl.py` |
| `upd.py` | World: as 17 Oct, plus energy payout 0.76 (as Oslo), 70% USD/NOK and 30% I-44, the value-multiple path, numeric return split (EPS, value multiple, FX), exit P/B–ROE, sensitivities (multiples ±10% and ±1, NOK ±10%, rest growth), checks against the 17 Oct currency and payout, triggers with the forward P/E scaled from 30 Sep | `py -I upd.py` |
| `valq.py` | Yahoo quoteSummary per name: price, currencies, BVPS, P/B, ROE, dividend yield (latest declared, annualised), trailing dividend rate, P/E, payout → JSON | `py -I valq.py data/val.json EQNR.OL DNB.OL KOG.OL NHY.OL AKRBP.OL MOWI.OL STB.OL TEL.OL SUBC.OL YAR.OL ORK.OL GJF.OL FRO.OL VAR.OL` |
| `valagg.py` | P/B (harmonic), P/E, ROE trailing / forward / Yahoo, forward dividend yield and dividend run rate ÷ trailing EPS for the Oslo sample on OBX weights, MSCI Norway weights and market cap; per block; without Frontline, without Kongsberg (and Gjensidige, Vår). Fixes USD book values (Vår) | `py -I valagg.py data/val.json 9.41` |

**World block model.** `idxai3.py` (company blocks, AI layer blocks, energy; switches for the
attribution) and `dl2/urth_ai.json` (MSCI World weights of the AI basket names from the URTH
holdings CSV, total 99.78, energy weight 4.18) were moved here from `fund/` on 18 Oct 2026. Its
Climate Change index parts are unused by the baseline.

**`fund/`** holds the scripts of the former fund mode. Fund mode was removed from this skill on
18 Oct 2026 (revision 2026-10-18.5): the skill estimates markets only and never analyses a named
fund or a single paper. The folder is not part of this skill.
