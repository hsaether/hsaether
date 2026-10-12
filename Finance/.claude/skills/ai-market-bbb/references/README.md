# AI Market BBB — scripts (initial run 12 Oct 2026)

Copy to the scratchpad, create `data/`, and run with `py -I` from there.

| Step | Script | Does |
|---|---|---|
| 1 | `../../equity-market-bbb/references/quotes.py data/q.json <tickers>` | Yahoo prices, market caps, P/E (basket tickers listed in `model.py`) |
| 2 | `../../equity-market-bbb/references/quotes.py data/fx.json KRW=X EURUSD=X NOK=X` | FX for Korean and European market caps |
| 3 | `../../equity-market-bbb/references/trend.py <tickers>` | Consensus EPS CY / CY+1 and analyst counts; paste CY27 (calendarised) into `eps27`, CY26 into `eps26` |
| 4 | `model.py` | Layer baskets: P/E on CY27, IRR USD and NOK per scenario, 2027 return, hurdle P/E at k = 12%, MoS, E / R, implied EPS growth 2028–30 for 12% |

Inputs to refresh in `model.py` each run: KRW and EUR FX, `eps27`/`eps26`, EPS paths and exit
P/E per layer (from the baseline's Steps 1–4), USD/NOK path (`FX`, from equity-market-bbb),
window NIBOR (`NIB`, from hy-market-bbb), stub length (`T0`).
