# AI Market BBB — scripts (initial run 12 Oct 2026; updates 15, 16, 17, 22, 24 and 29 Oct, 1, 5, 7 and 11 Nov 2026)

Copy to the scratchpad, create `data/`, and run with `py -I` from there. The stored `model.py` and
`impl.py` carry the inputs of the 11 Nov run (Update 7 prices of 6 Nov, consensus 7 Nov, K1 re-set).

| Step | Script | Does |
|---|---|---|
| 1 | `../../equity-market-bbb/references/quotes.py data/q.json <tickers>` | Yahoo prices, market caps, P/E (basket tickers listed in `model.py`) |
| 2 | `../../equity-market-bbb/references/quotes.py data/fx.json KRW=X EURUSD=X NOK=X` | FX for Korean and European market caps |
| 3 | `../../equity-market-bbb/references/trend.py <tickers>` | Consensus EPS CY / CY+1 and analyst counts; paste CY27 (calendarised) into `eps27`, CY26 into `eps26` |
| 3b | `trend2.py <tickers>` | earningsTrend with endDate, yearAgoEps and revenue estimates: use it to check fiscal-year labels before calendarising (SKILL quirk, 16 Oct) |
| 3c | `k1ret.py [path ...]` (new 11 Nov) | **K1 return gauge** (Step 1b; standard library, no data files). No argument: the table on the current Base K1 (K1, AI capex, cumulative AI capex, AI depreciation, average net AI assets, revenue needed at 10% and 0%, supply split cloud / Copilot / Meta, coverage, gap, pre-tax return, the five's D&A, 2025–31), the sensitivities (r 8/12%, cash cost 35/45%, short life 6/4 years, short-lived share 75%, strict attribution, E2 Bull) and the other K1 paths. With path names (`base`, `taper`, `flat`, `hold`, `bear`, `bull`): the full table for each. `taper` reproduces table 4.2 of `docs/review-ai-k1-sustainability.md`. Update `PATHS['base']` when K1 Base moves, and the E2 / T1 / Meta supply inputs when those Base rows move |
| 4 | `model.py [CAL RET PATH AMZN U5 K1D \| NONE \| BEARCAP]` | Layer baskets (version 2.1, 22 Oct; `AMZN` = E layer on Microsoft, Alphabet and Amazon; `U5` = E Base 2027 .92 from the 29 Oct company check; `K1D` = the 11 Nov K1 re-set: H1 and H4 Base 2028–30 and the E Base cash conversion, published values with their derivation printed beside them; `BEARCAP` = all on plus the Bear capped at today's P/E; prints the exit cross-check): P/E on CY27, IRR USD and NOK per scenario, 2027 return, hurdle P/E at k = 12%, MoS, E / R, implied EPS growth 2028–30 for 12%. Retained cash counted once via cash conversion `CONV`. Switches for attribution: `CAL` calendarised consensus, `RET` retained cash, `PATH` version-2 paths; no argument = all on; `NONE` = version-1 method. For a price-then-consensus attribution, run a copy with the previous run's `cal` values first |
| 4b | `members.py` | Each name on its layer path and method (Base, Bear, E / R) for the company check, plus memory sensitivities. For the per-name capped Bear, exec it with `BEARCAP = True` set before calling `one()` |
| 4c | `impl.py [layer]` (new 1 Nov; layer argument 11 Nov) | **Price-implied path.** No argument = H2 (Memory cycle): for the basket and each name, the uniform multiplier on Base 2028–30 (2027 at Base) at which the price returns k = 12% and 0%; the same on all years; the flat 2028–30 level; IRR of named turn-date and depth paths at exit P/E 10 and 8; the basket multiplier at exit P/E 8 / 10 / 11. `impl.py H1` / `impl.py E` (any layer key): the same multipliers for that basket and its names on the layer's Base method (K1 capex cycle, Step 1b item 5) |
| 5 | `hist.py <tickers>` | Yahoo chart API, 3-month daily closes: last 12 closes, high and date, change from the high (market-mood table). Indices: `^IXIC ^NDX ^SOX ^GSPC ^KS11 ^N225 ^TWII ^HSI`; Asia names: `2330.TW 6857.T 9984.T 8035.T 285A.T` |
| 5b | `cyclehist.py <ticker> <from> <to>` (new 1 Nov) | Yahoo daily closes: high and low with dates in a window, for the past-cycle table of the Memory cycle section (MU, `000660.KS`, `005930.KS`, `^KS11`; windows 2017-01-01 to 2019-06-30, 2018-06-01 to 2019-12-31, 2020-06-01 to 2021-12-31, 2021-06-01 to 2023-06-30, and the current cycle) |

Inputs to refresh in `model.py` each run: KRW and EUR FX (Korea: previous close when Seoul is open), `cal`/`eps26` (calendarised, ASML EUR → USD), `CONV`, EPS paths and exit
P/E per layer (from the baseline's Steps 1–4), USD/NOK path (`FX`, from equity-market-bbb),
window NIBOR (`NIB`, from hy-market-bbb), stub length (`T0`). `impl.py` reads the same inputs.
When K1 Base moves again, set `K1_OLD` / `K1_NEW` and the published `K1D_SET` values in
`model.py` (or fold the `K1D` paths into `P1`/`CONV` and start a new switch).
Micron's past quarterly figures for the cycle table come from Alpha Vantage `INCOME_STATEMENT`
(MU, quarterly reports).
