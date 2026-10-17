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

## Fund mode — `fund/` (first run: DNB Teknologi A, 11 Oct 2026)

Copy `fund/` to the scratchpad and run there with `py -I`, in this order. The holdings, blocks,
EPS paths, exit P/Es, payouts, currency mix and baseline paths are literals for DNB Teknologi on
17 Oct 2026 (fourth run). Company blocks CM, CG, CN, CT carry the per-share V_t, D_t and EPS
paths of `docs/msft-analysis.md`, `docs/googl-analysis.md`, `docs/nvda-analysis.md` (calendarised,
revenue-consistent Bear) and `docs/tsm-analysis.md` (revenue-consistent Bear) (`COMP` in
`fundmodel.py`); re-copy them when those analyses change. Layer and own blocks count retained cash
(`CONV`, AI BBB v2; `RET` switch). AI-exposed blocks (E, H1, H2, H3, T) carry the layer paths of
`docs/ai-market-bbb.md`; re-copy them from there on every run, and keep own paths only for
non-AI blocks. Replace them for each fund and run, from the fund's own sources and the current
`docs/equity-market-bbb.md`.

| Script | Does | Run as |
|---|---|---|
| `close.py` | Daily closes on the NAV date (and 9 Oct, last) for all holdings and NOK=X → `closes.json`; `blocks.py` prices from it | `py -I close.py 2026-10-14 MSFT GOOGL … NOK=X` |
| `hold.py` | Yahoo quoteSummary per holding: price, currencies, P/E, dividend yield, consensus EPS 0y / +1y with analyst counts → `hold.json` | `py -I hold.py MSFT GOOGL … 005930.KS` |
| `blocks.py` | Holdings table (weight, block, CY / CY+1 EPS after calendarisation) → block weights, CY+1 P/E, earnings shares, growth → `blocks.json` | `py -I blocks.py` |
| `fundmodel.py` | Scenario model: block EPS paths, P/E glide (Bear de-rates in Year 1), payout, USD/NOK and I-44 paths, total cost, alpha → returns, XIRR, hurdle NAV, E / R | `py -I fundmodel.py` |
| `sens.py` | Sensitivities (cost, alpha, exit P/E, cyclical mid-cycle, consensus) and NAV triggers (imports `fundmodel.py`) | `py -I sens.py` |
| `attrib.py` | Attribution from the previous version (method v1 → v2 Bears → company blocks → retained cash) and the method sensitivities (X cash conversion, NVIDIA/TSMC variants, memory-stressed Bear) | `py -I attrib.py` |
| `aisplit.py` | Per-block IRR (each block alone, before cost) vs the AI BBB baskets; AI layers vs non-AI part; AI-only Bear and Bull (non-AI block and NOK on Base); path and exit sensitivities (imports `fundmodel.py`) | `py -I aisplit.py` |
| `detail.py` | Per-year NAV equivalents, blended forward P/E, IRR to each year-end | `py -I detail.py` |
| `link.py` | Fund NAV vs World NOK/USD, sector ETF, OSEBX, Brent, USD/NOK: volatility, correlation, beta, drawdowns, calendar returns. Needs `data/d_<sym>.json` from `../fetchd.py` (fund on its Morningstar id, e.g. `0P00000MVB.IR`) | `py -I link.py` |
| `pdf.py` | PDF → text with `pypdf` (FactSet Earnings Insight, MSCI factsheets, KIDs) | `py -I pdf.py in.pdf out.txt` |

### Index funds (first run: DNB Global Indeks A vs Nordnet Global Indeks, 11 Oct 2026)

Inputs are literals for that run: World paths from the baseline, the energy share of World
earnings (5.5%), the oil block path, the Climate Change P/E premium (18.93 / 17.92), payouts, costs
and NAVs. Refresh them from the current baseline, the index factsheets and the fund pages.

| Script | Does | Run as |
|---|---|---|
| `idxfunds.py` | Index-fund model on the World paths: World unchanged (must reproduce the baseline at zero cost); tilted index = World ex energy (energy on the oil path) with a P/E premium; all-in cost → returns, XIRR, hurdle NAV, E / R, NAV paths | `py -I idxfunds.py` |
| `idxsens.py` | Sensitivities (premium halves / gone, Tesla P/E, Bear premium, energy share, swap drag, cost, exit P/E, consensus), NAV triggers, structural run, oil side case (imports `idxfunds.py`) | `py -I idxsens.py` |
| `idxdetail.py` | Per-year paths, NAV levels, IRR to each year-end, NOK 508k outcomes, return split, share of Bull priced | `py -I idxdetail.py` |
| `idxcmp.py` | Two fund NAVs vs URTH × USD/NOK: calendar and period returns, volatility, correlations (World, OSEBX, Brent, USD/NOK), tracking between the funds before and after an index change, drawdowns. Needs `data/d_<sym>.json` from `../fetchd.py` (`0P0001K6NJ.IR`, `0P0000PS3V.IR`, URTH, NOK=X, OSEBX.OL, BZ=F) | `py -I idxcmp.py` |
| `idxtd.py` | Fund-vs-fund NAV ratio against the index-vs-index ratio from the MSCI factsheet (1 y, YTD) | `py -I idxtd.py` |

**AI split (12 Oct 2026 re-run).** Needs `dl2/urth_ai.json`: weights of the AI basket names
(ticker + country), the total of 99.78 and the energy sector weight 4.18, built from the URTH
holdings CSV (see SKILL.md, index-fund data). Literals: the AI BBB layer paths, exit P/Es and
payouts; block P/Es from the AI BBB appendix prices and CY27 EPS; Climate Change multipliers;
energy P/E 14.8; NAVs of 9 Oct.

| Script | Does | Run as |
|---|---|---|
| `idxai.py` | World = AI blocks (AI BBB paths) + energy (oil path) + implied rest, reproducing the Equity BBB World path; the climate index = the same blocks at its weights, with its rest premium; options for cost, tail weights, premium mode, exit P/E shift, AI-only stress, consensus shift (`em`), price change (`P0`) | `py -I idxai.py` |
| `idxaidetail.py` | Blocks alone vs the AI baskets, fund results after cost, AI-only stress, sensitivities, the "rest at trend growth" check, Nordnet triggers, return split (imports `idxai.py`) | `py -I idxaidetail.py` |

**15 Oct 2026 re-run (company blocks, NAV-date prices).** The same inputs as above, plus:
Microsoft and Alphabet per-share V_t, D_t and EPS per scenario from their analyses; the 9 Oct and
14 Oct prices of every block name (AI BBB appendix); the index moves since 9 Oct (URTH, and the
Climate Change index from the NAV ratio); IXC for energy; NAVs of 14 Oct. Triggers keep future
values unchanged (the Equity BBB convention); `dp` moves only today's price.

| Script | Does | Run as |
|---|---|---|
| `idxai2.py` | World = company blocks (MSFT, GOOGL) + AI layer blocks + energy + implied rest at the NAV-date prices, reproducing the Equity BBB World path at its price; the climate index = the same blocks at its weights with its rest premium; options `cost`, `tail`, `prem_mode`, `pex_shift`, `ai_only`, `dp`, `em`, `co_as_layer` (company names back on the E layer), `rest_trend`, `only` | `py -I idxai2.py` |
| `idxai2detail.py` | Blocks alone (incl. company vs layer path), fund results after cost with NAV levels and NOK 920k / 508k outcomes, AI-only stress, rest-at-trend check, sensitivities, triggers for both funds, return split | `py -I idxai2detail.py` |
| `close.py` | Closes on a given date for any Yahoo symbols (also used by the fund mode) | `py -I close.py 2026-10-14 URTH NOK=X …` |

**17 Oct 2026 re-run (AI BBB Update 2, NVIDIA as a company block).** Same data files as 15 Oct
(`dl2/urth_ai.json`). New literals: NVIDIA per-share V_t, D_t and EPS (calendarised,
revenue-consistent Bear, as in `fundmodel.py` CN); AI BBB v2 Bear paths and cash conversion `CONV`;
energy c = 0.80; calendarised CY27 consensus (`EPS27`; the old basis kept as `EPS27_V1`); 15 Oct
closes (`P15`, Alphabet C at its own price); NAVs of 15 Oct. TSMC is not in MSCI World.

| Script | Does | Run as |
|---|---|---|
| `idxai3.py` | As `idxai2.py`, plus block CN, retained cash counted once in layer and energy blocks, and switches `RET`, `BEAR_V1`, `CONS_V1`, `CN_LAYER` for the attribution; `co_layer` puts any company block back on its layer; `PEX_OVR` for the memory-stressed Bear | `py -I idxai3.py` |
| `idxai3detail.py` | Company-block check against the analyses (USD), blocks alone, fund results, AI-only stress, rest checks and the layer retained cash, attribution from the 15 Oct version, sensitivities (incl. energy c, cash conversion, NVIDIA variants), triggers, return split | `py -I idxai3detail.py` |

**17 Oct 2026 — Equity BBB Update 1 (World from the AI split; Oslo repriced).** Copy `upd.py`,
`osl.py` and `fund/idxai3.py` (+ `fund/dl2/urth_ai.json`, URTH weights of 9 Oct) into one
scratch folder and run with `py -I`.

| Script | Does | Run as |
|---|---|---|
| `upd.py` | World = company blocks + AI layer blocks + energy (imports `idxai3.py`, repriced to the 16 Oct closes, Brent Base 2027 88) + an explicit rest path per scenario (`REST_EPS`, `REST_PE`, `REST_PAY`); returns in NOK, E / R, sensitivities, triggers; `only_rest_old=True` reruns the 11 Oct top-down path | `py -I upd.py` |
| `osl.py` | Oslo on the 11 Oct block model at the 16 Oct price, Brent Base 2027 88, USD earnings at the 16 Oct NOK spot, stub 75 days; return split, sensitivities, triggers | `py -I osl.py` |
