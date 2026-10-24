# AI Market BBB — scripts (initial run 12 Oct 2026; updates 15, 16, 17, 22 and 24 Oct 2026)

Copy to the scratchpad, create `data/`, and run with `py -I` from there.

| Step | Script | Does |
|---|---|---|
| 1 | `../../equity-market-bbb/references/quotes.py data/q.json <tickers>` | Yahoo prices, market caps, P/E (basket tickers listed in `model.py`) |
| 2 | `../../equity-market-bbb/references/quotes.py data/fx.json KRW=X EURUSD=X NOK=X` | FX for Korean and European market caps |
| 3 | `../../equity-market-bbb/references/trend.py <tickers>` | Consensus EPS CY / CY+1 and analyst counts; paste CY27 (calendarised) into `eps27`, CY26 into `eps26` |
| 3b | `trend2.py <tickers>` | earningsTrend with endDate, yearAgoEps and revenue estimates: use it to check fiscal-year labels before calendarising (SKILL quirk, 16 Oct) |
| 4 | `model.py [CAL RET PATH AMZN \| NONE \| BEARCAP]` | Layer baskets (version 2.1, 22 Oct; `AMZN` = E layer on Microsoft, Alphabet and Amazon; `BEARCAP` = all on plus the Bear capped at today's P/E; prints the exit cross-check): P/E on CY27, IRR USD and NOK per scenario, 2027 return, hurdle P/E at k = 12%, MoS, E / R, implied EPS growth 2028–30 for 12%. Retained cash counted once via cash conversion `CONV`. Switches for attribution: `CAL` calendarised consensus, `RET` retained cash, `PATH` version-2 paths; no argument = all on; `NONE` = version-1 method |
| 4b | `members.py` | Each name on its layer path and method (Base, Bear, E / R) for the company check, plus memory sensitivities |
| 5 | `hist.py <tickers>` | Yahoo chart API, 3-month daily closes: last 12 closes, high and date, change from the high (market-mood table). Indices: `^IXIC ^NDX ^SOX ^GSPC ^KS11 ^N225 ^TWII ^HSI`; Asia names: `2330.TW 6857.T 9984.T 8035.T 285A.T` |

Inputs to refresh in `model.py` each run: KRW and EUR FX (Korea: previous close when Seoul is open), `cal`/`eps26` (calendarised, ASML EUR → USD), `CONV`, EPS paths and exit
P/E per layer (from the baseline's Steps 1–4), USD/NOK path (`FX`, from equity-market-bbb),
window NIBOR (`NIB`, from hy-market-bbb), stub length (`T0`).
