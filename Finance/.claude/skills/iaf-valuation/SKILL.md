---
name: iaf-valuation
description: Investment Analysis Framework (IAF) — the standing valuation method for this workspace. A forward-looking required-return test (d + g versus k, k = 12%), a PE or P/FCF ceiling, a year-by-year IRR build with a hurdle price for cyclical and capital-intensive companies (shipping, offshore, rigs), growth treated as a capital-allocation decision (ROIC on growth capex versus k), and Bear/Base/Bull where Base is the decision case and Bear/Bull are catalyst-based stress tests. ALWAYS use this skill when the user asks to value, screen or analyse a company, mentions IAF, "the framework", d+g, k, hurdle, PE ceiling, P/FCF, IRR, growth capex, ROIC, BBB or Bear/Base/Bull, or asks whether a stock clears the required return — even without naming IAF.
---

# Investment Analysis Framework (IAF)

**Revision:** 2026-10-08.2 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/iaf-valuation/` in the Finance folder.

A forward-looking test of whether today's price is defensible given the return it can deliver over
the rest of the current year plus 3 calendar years. It answers one question: **does the expected
return clear k, and by how much margin?**
It is a margin-of-safety screen. Never present its output as a price target.

## Standing parameters

- **k = 12%** baseline required return. **Never below 10%.** k may be raised (not lowered) for high
  leverage, single-asset or single-contract exposure, or poor liquidity; state the reason.
- **Horizon = stub period + 3 full calendar years** (the rest of the current year, then the next
  three calendar years). Up to 5 years only for steady compounders; state which. Roll the window
  forward each January. See Step 1b.
- **Base case = the decision.** Bear and Bull are stress tests (see BBB).
- **25/50/25** is only a labelled convention for an optional reference figure — never a probability.
- Everything per share, forward-looking, same currency and same basis (no trailing/forward mixing).

## Data sources (MCP connectors)

Use the connectors in this order. Primary documents beat aggregated data. Every figure states its
source, its fiscal period with period-end date, and its currency. If a connector fails or returns
nothing, say so and fall back to the next one. Never fill a gap with an invented number.

| Need | First choice | Fallback |
|---|---|---|
| Nordic listed company: quarterly figures, guidance, booked days/rates, backlog, dividend policy, CEO outlook | **Nordic Financial** (`search_filings`, `company_research`); full report via `parse_pdf_to_text` on the IR PDF | FinancialFilings, issuer IR / Newsweb |
| Contract awards, fixtures, newbuild orders, results dates since the last report (backlog tracking) | **Nordic Financial** `search_filings` with `source="newsweb"` + `ticker` + `fiscal_year`, `limit` 10–20 | FinancialFilings `filings_list` |
| Structured IS/BS/CF line items, any listed company (Nordic, EU, US, SG) | **FinancialFilings** (`companies_financials_retrieve`) | Nordic Financial text, issuer report |
| Filing list: new reports, share issues, insider trades, prospectuses | **FinancialFilings** (`filings_list`, newest first) | Nordic Financial `report_type="press_release"` |
| Share price, spot FX, futures, Oslo tickers, market cap | **Yahoo** (`get_quote`, `get_chart`, `quote_summary`) | EODHD EOD prices; AllRatesToday for spot FX |
| FX at a past moment (balance-sheet date, ex-date, payment date), several pairs at once; official central-bank rates | **AllRatesToday** (`get_rates_authenticated` with `time`, `get_official_rates`) | Yahoo `get_chart` |
| Price history (EOD) as a cross-check | **EODHD** | Yahoo `get_chart` |
| US company ratios | **Zacks** (`compare_stocks`, `get_zacks_metrics`) | Alpha Vantage (`COMPANY_OVERVIEW`), FinancialFilings, Yahoo |
| Market check on the hurdle price (US listings and US ADRs): broker ratings and price targets per firm, consensus EPS/sales with number of estimates, next report date | **Zacks** (`get_wall_st_rating`, `compare_stocks` with `section="EDT"`) | Yahoo `quote_summary` |
| Analyst digest of results, guidance, backlog and management market commentary (US listings) | **Zacks** `get_zacks_research` (dated report), `get_zacks_commentary` | Issuer report via FinancialFilings |
| Brent/WTI/diesel spot history (cross-check of realised prices against the oil baseline) | **FRED** (`DCOILBRENTEU`, `DCOILWTICO`, `DDFUELNYH`, averaged server-side per quarter) | Alpha Vantage (`BRENT`, `WTI`) |
| NIBOR path per scenario (NOK floating-rate debt service), Nordic HY spread and new-issue spreads (refinancing in Bear), HY watchlist (distress signal for an analysed issuer) | **`docs/hy-market-bbb.md`** (Interface tables, watchlist) | FRED and Norges Bank API for current levels only — never an own rate path |
| Defense companies: defense spending per country, equipment and addressable spending, segment order and revenue growth per scenario, long end and steady-state margins, capacity balance | **`docs/defense-market-bbb.md`** (Interface tables, "For IAF") | — never an own defense spending or defense market forecast |
| Rate and credit context: US 10-year, US high-yield spread, Norwegian 10-year and 3-month | **FRED** (`DGS10`, `BAMLH0A0HYM2`, `IRLTLT01NOM156N`, `IR3TIB01NOM156N`) | AllRatesToday `get_official_rates` (Norges Bank) |
| Norwegian macro (policy rate, NOK FX) | **FRED** for rates; **Yahoo** / **AllRatesToday** for NOK FX | Norges Bank website |
| Nordic power price (today/tomorrow, hourly, EUR/kWh) | **Nordic Financial** `get_current_power_price` (zones NO1–NO5, SE1–SE4, DK1, DK2, FI) | — |

**Nordic Financial** (aidatanorge Nordic MCP server): about 1,500 companies listed in Oslo,
Stockholm, Helsinki and Copenhagen, plus First North, from 2020 onwards. Covers annual and
quarterly reports, Newsweb/exchange announcements and press releases (the advertised macro
summaries returned nothing in testing, see below), plus Nordic power prices and PDF extraction.
- **Always set `fiscal_year`** and `ticker`. Without them, old reports (e.g. 2020) outrank the
  latest quarter.
- Use `company_research` with one section per IAF need (results, guidance/coverage, fleet and
  capex, dividend and capital allocation, debt), each with `ticker` set.
- Results are text excerpts, not tables. For 2026, `report_type="quarterly_report"` holds only the
  Newsweb results announcement (about 3 chunks: headline figures, backlog, dividend), not the full
  report. Segment TCE/rates, coverage, the statements and the notes need the full report.
- **Full report:** `parse_pdf_to_text(pdf_url)` on the issuer's IR PDF (tested 2026-10-05 on Hafnia
  Q2 2026: 34 pages, about 106k characters). IR pages often build their links with JavaScript,
  so WebFetch sees no PDF. Get the URL in the in-app browser by collecting `a[href$=".pdf"]`
  (Hafnia: `s201.q4cdn.com/891122012/files/doc_financials/<year>/q<n>/…`). The output is too
  large for the conversation and is saved to a file: read it with `py`, split on
  `--- Page N ---`. Tables come out one cell per line in column order (current quarter, prior-year
  quarter, YTD, prior YTD); map the columns from the header lines before reading figures.
- **Newsweb stream:** `source="newsweb"` + `ticker` + `fiscal_year` returns dated announcements
  (contract awards with the issuer's size class, newbuilds, results dates). It is the quickest way
  to update backlog after the last report.
- Do not use the `sector` filter: company documents carry `sector = null`, so a sector filter
  returns nothing. `macro_summary` returned nothing for any country or year (tested 2026-10-05),
  and no freight or commodity series were found despite the server's documentation.
- `analyze_company` writes a synthesised answer. Use it only for orientation and never as a figure
  source or a complete list (tested 2026-10-05: it missed 2 of 6 DOF contract awards in
  July–August that `search_filings` found).
- `get_company_info` works for the NO/DK/FI registries, not for Sweden.
- Oil prices: only daily `BZ=F` closes copied from Yahoo (`report_type="macro"`), found by
  semantic search as scattered single days; `macro_summary` does not cover oil. Use Yahoo or FRED
  instead. Realised oil and gas prices appear in producers' quarterly reports (e.g. Equinor) and
  serve as a cross-check of the oil baseline only.

**FinancialFilings** (official filings from SEC, ESMA, Oslo and other regulators):
- Resolve the company first with `companies_list(search=…)` and confirm name and country, then
  use the internal id. Example: Hafnia = id 9980, registered in SG and reporting in USD.
- `companies_financials_retrieve` returns standardised line items per period with
  `source_filing` and `viewer_url`. Interims often come back as cumulative periods (H1, 9M).
  Derive a discrete quarter as H1 − Q1, for example, and never mix the two.
- Read the extraction notes. Lines marked PARTIAL AGGREGATE or ASSUMED ZERO (often net debt and
  total debt) must be checked against the report before use.
- `filings_list(company=id, ordering="-release_datetime")` is the check for new events before
  each analysis or tracking update: share issues (CAP/424B5), insider trades (DIRS) and new
  reports. A share issue changes the share count used in the per-share figures.

**Yahoo**: no quota. Best source for prices, spot FX, futures and Oslo tickers (`.OL`).
- Multiples are wrong for NOK-listed companies that report in USD, because currencies get mixed
  (e.g. Hafnia EV/EBITDA 67x). Compute multiples yourself from price × shares and the reported
  figures.
- An unknown ticker is dropped silently, so check that every ticker came back.

**FX rule**: convert reported figures (often USD) to the share-price currency (often NOK) at the
rate matching the price time stamp. Use Yahoo for that market rate (AllRatesToday
`get_exchange_rate` as cross-check; they agreed to the 4th decimal when tested). State pair, rate,
source and time stamp in the header.

Historical FX (quarter-end, year-end, ex-date, payment date) comes from AllRatesToday
`get_rates_authenticated` with `time` set to the moment (e.g. `2025-12-31T16:00:00Z`); give several
targets comma-separated in one call. Fall back to Yahoo `get_chart`.

**AllRatesToday** (free API key): live interbank mid-market rates for 160+ currencies.
- `get_rates_authenticated` with `time`: one point per pair at any past datetime. `group` with
  `time` still returns one point, not a series.
- `get_historical_rates`: fixed windows ending now only (`30d` daily, `1y` weekly). Use Yahoo
  `get_chart` for longer or custom-window series.
- `get_official_rates`: the latest published central-bank table (Norges Bank = `norges`, ECB =
  `ecb`, Fed = `fed`, BoE = `boe`; other codes via `list_central_banks`, whose output is large).
  Dated official rates need a paid plan (403). Use the Norges Bank rate when a company or a tax
  rule names it; otherwise use the market rate.
- Always cite the returned `time` or `rate_date`.

**EODHD** (free plan): 20 calls per day, EOD prices only. Fundamentals and live data return 403.
Tickers are `.OL` for Oslo and `.US` for the US. One bad ticker in a batch gives a 404 for the
whole batch. Use it only as a price cross-check.

**Alpha Vantage** (free key): 25 calls per day and at most 1 call per second, so call
sequentially. `COMPANY_OVERVIEW` gives usable ratios for US companies. `BRENT`/`WTI` are EIA
monthly averages from 1987 and lag about a month. An unknown ticker returns `{}`.

**Zacks** (Zacks Investment Research; tested 2026-10-08, no quota met): US listings and US OTC
ADRs only (e.g. TDW, RIG, VAL, NE, BORR, FRO, HAFN; BAESY, RNMBY, SAABY). Oslo-only names are not
covered (DOFG returned an error).
- `get_wall_st_rating`: one row per broker with rating, target, previous target and date,
  including Nordic brokers (DNB Carnegie, Fearnley, Clarksons Platou on TDW). Use it as a market
  check beside the hurdle price; a broker target is never an IAF input.
- `get_zacks_research`: a dated analyst report (only names with a full Zacks report; e.g. RIG,
  22 Sep 2026). It digests results, guidance, backlog, coverage and management's market
  commentary. Quote it as Zacks' view with its publish date, tag `[E]`, and check figures against
  the issuer report before use.
- `compare_stocks`: up to 5 tickers side by side; the `section` parameter picks the detail block
  (`EDT` estimates with high/low and count, `SEH` surprise history, `PEERS`, `CFIN` ratios). An
  unknown ticker is dropped silently, so check that every ticker came back.
- Consensus is thin: 1–2 estimates for TDW, VAL and BORR, none for FRO. Always state the number
  of estimates; never call it "the market's view" on one or two estimates.
- Statement quirks: FRO EBITDA equals EBIT (D&A missing from the income statement, present in the
  cash flow); the capex sign is inconsistent (FRO 2025 +24.6). FinancialFilings stays the source
  for statements; Zacks is a cross-check. ADR figures are per ADR in USD, not per local share.
- Zacks Rank and the style scores measure short-term estimate-revision momentum. They are not an
  IAF input and never move k or the hurdle.

**FRED** (St. Louis Fed; tested 2026-10-05, no quota met): official US and OECD time series.
- Find a series with `fred-search-series`, fetch with `fred-get-series-observations`. Set
  `frequency_aggregation` (`m`, `q`, `a`) with `aggregation_method="avg"` to get period averages
  in one call; `eop` for period-end values.
- Lags: `DGS10` and `BAMLH0A0HYM2` about 1 trading day; EIA oil spot about 1 week; OECD Norwegian
  rates are monthly averages about 1 month behind; `DEXNOUS` (USD/NOK) about 1 week, so keep Yahoo
  for spot FX. Cite the last observation date.
- Oil series are EIA spot (Dated proxy), not the futures basis of the oil baseline — label them.
- Rates and spreads are context for k only: they can support raising k (e.g. wide high-yield
  spreads for a leveraged name) and never lower it below the standing rule.
- No company data, rig counts, tanker or OSV rates, or futures curves.

**Not used for IAF:** sector or oil forecasts from any connector. These always come from `docs/oil-market-bbb.md` and the sector BBB documents.

## Definitions

| Symbol | Meaning |
|---|---|
| P | Current share price (entry price) |
| E / FCF | Earnings, or free cash flow to equity. Use FCF for capital-intensive and cyclical sectors |
| D_t | Cash returned to shareholders in period t per share (dividends + buybacks), placed at its payment date |
| d | Cash yield on entry: (Σ D over the horizon ÷ T) ÷ P. Simple and undiscounted |
| V_t | Value per share at end of year t (see Terminal value) — V_0 = P |
| NAV_0 | NAV per share at the valuation date by the V_T method, at the scenario's mid-cycle marks, less net debt at the valuation date |
| g | Per-share value growth. Track A: EPS CAGR (value growth at a constant PE). Track B: (V_T / P)^(1/T) − 1. An output of the build, not a free input |
| IRR | Return that equates P with the D_t stream plus V_T. Track A: ≈ d + g. Track B: IRR_T = d + g + c, c = timing term (Step 2B) |
| P_k | Hurdle price: the most you can pay and still earn exactly k |
| ROIC_g | Return on growth capex (new capital deployed) |

## Step 1 — Choose the track

- **Track A (steady):** stable earnings, low capex volatility. Use E, PE and a growth rate.
- **Track B (cyclical / capital-intensive):** shipping, offshore, rigs, commodities, or any company
  where capex, D&A or rates swing earnings. Use FCF, the year-by-year IRR build and P_k.
- State which track and why. When in doubt, use Track B.
- Defense companies are normally Track A (backlog-driven growth, moderate capital intensity). Use
  Track B, or Track A with explicit capex, when a capacity build-out makes FCF swing (new
  ammunition or missile plants); state which.

## Step 1b — Time grid: stub period + 3 calendar years

- **Valuation date = today. Exit date = 31 Dec of the third full calendar year.** Example:
  valuation 4 Oct 2026 → exit 31 Dec 2029, T ≈ 3.24 years. Calendar years match company reporting
  and the sector BBB skills.

| Period | Content | Granularity |
|---|---|---|
| Stub | Remaining quarters of the current year, including a quarter that has ended but is not yet reported | Quarterly |
| Year 1 | Next calendar year (contract cover, drydocks, deliveries, debt instalments fall in specific quarters) | Quarterly |
| Years 2–3 | Following two calendar years | Annual |

- **Stub quarters are modelled from locked-in information**: booked days and rates from the latest
  guidance, actual spot rates for elapsed open days, current spot/forward for remaining open days,
  known opex, drydock days, debt instalments and deliveries. An ended-but-unreported quarter is the
  highest-confidence estimate in the model. Oil prices for the stub and Year-1 quarters come from
  the Stub and Year 1 by quarter tables in `docs/oil-market-bbb.md`. Tanker spot TCE for open days
  comes from the same tables in `docs/oil-shipping-bbb.md` (market basis; the company's own
  premium or discount to market is set and sourced in the company analysis). For drilling
  contractors, booked rig-days and rates come from the fleet status; open rig-days use the
  leading-edge dayrate for the rig's segment row in `docs/rig-market-bbb.md`, with idle time
  informed by the segment utilization. A rig earns its backlog rate until expiry, then the
  leading-edge rate for that year. For OSV and subsea-vessel owners, booked days and rates come
  from the company's contract lists; open days use the vessel's row in `docs/supply-market-bbb.md`
  (North Sea spot by quarter × the row's utilization for spot-exposed vessels; leading-edge term or
  Petrobras rate otherwise). A vessel earns its contract rate until expiry, then the row's rate.
  For defense companies, stub and Year-1 revenue comes from the company's firm backlog, delivery
  schedule and guidance; the market check in `docs/defense-market-bbb.md` (segment book-to-bill,
  capacity) tests that guidance. Years 2–3 apply the baseline's segment revenue growth paths to
  the company's segment and regional mix, ± a named and sourced share change, and show backlog
  coverage of each year.
- **Starting balance sheet**: roll the last reported balance sheet forward through the stub to net
  debt at 31 Dec (the start of Year 1). Also state net debt at the valuation date.
- **Dividends at payment dates.** A declared dividend counts only if the share has not yet gone
  ex-dividend on the valuation date.
- **Never annualise stub figures.** Show them as quarters.
- In IRR terms the stub is small. Its main value is the starting point (net debt), near-term
  catalysts, and tracking actuals against the model.

## Step 2A — Track A: the core rules

```
Rule 1  (hurdle)     d + g > k            ⇔  (d + g) / k > 1
Rule 2  (anchor)     PE = 1 / k           (zero-growth stock priced to return k)
Rule 3  (ceiling)    PE < (d + g) / k²
```
At k = 12% (k² = 0.0144): d = 1%, g = 20% → PE < 14.6; d = 1%, g = 30% → PE < 21.5.

g = forward per-share EPS CAGR over the horizon, built from drivers, fading toward a sustainable
rate. For defense companies the fade follows the long-end CAGR and steady state, and normalised
margins follow the steady-state segment margins, in `docs/defense-market-bbb.md`.
Cross-check: sustainable g ≈ ROIC × reinvestment rate. If the forecast g needs more reinvestment
than the payout leaves, d and g are inconsistent — fix one of them.

Rule 3 combines a total-return hurdle with a no-growth earnings-yield anchor. It is a heuristic for
how much premium is defensible, not a value from a cash-flow model.

## Step 2B — Track B: year-by-year IRR build

For each period (stub quarters, Year 1 quarters, Years 2–3), build per share:

| Line | Content |
|---|---|
| Maintenance FCF | EBITDA − tax − net interest − lease payments − maintenance capex and drydock: cash generated before growth spending. **Before scheduled debt amortisation**, which moves cash and debt equally and leaves net debt unchanged |
| Debt amortisation | Own line. If the payout policy is set on FCF after debt service, apply the payout to Maintenance FCF − amortisation and say so |
| Growth capex | Capital spent to expand the earning base (new vessels, rigs, projects), gross. Show the new debt raised for it on its own line |
| Retained cash / net debt | Retained cash = Maintenance FCF − growth capex − D_t paid (+ new equity). Net debt falls by retained cash; show net debt at each period end. This is how retained cash reaches V_t |
| D_t | Actual dividends + buybacks |
| V_t | Value at year end (see Terminal value) |
| r_t | Period return = (D_t + V_t − V_(t−1)) / V_(t−1), shown per year-end (stub not annualised) |
| IRR to t | Cumulative IRR if exiting at each year-end, including the end of the stub |

Then:
```
t_j = (payment date of D_j − valuation date) / 365;   T = (exit date − valuation date) / 365
IRR_T solves      P = Σ_j D_j/(1+IRR)^(t_j) + V_T/(1+IRR)^T        (XIRR on dates)
Hurdle price      P_k = Σ_j D_j/(1+k)^(t_j) + V_T/(1+k)^T
Rule 1 (Track B)  IRR_T > k   ⇔   P < P_k
Margin of safety  P_k / P − 1
```
- Retained cash must be counted exactly once: either paid out in D_t or added to V_t, never both,
  never neither.
- r_t and IRR-to-each-year are a path diagnostic, not a per-year pass/fail. A weak middle year is
  not a failure, but it must be visible. Interim V_t follows the marking convention in Step 3.
- Rule 3 cross-check: P/FCF_normalised < IRR_T / k². Report it as "P/FCF x vs ceiling y" (always in
  that order), but decide on P vs P_k (the ceiling uses an IRR that itself depends on P).
  - **FCF_normalised** = Maintenance FCF at Base mid-cycle (full fleet, exit-year costs, interest on
    exit net debt) **less a fleet-renewal charge**: one year of mid-cycle ageing on the V_T method
    (the ageing line of the V_T bridge ÷ T). Debt amortisation is not deducted; it is
    financing, and the renewal charge carries the asset wear.
  - Why: Track A's E is after depreciation. Without the renewal charge, P/FCF flatters ageing
    fleets (DOF 8.1x without it, 17.2x with it, against a 7.8x ceiling).

**Return split (reporting only; the decision is IRR_T and P_k):**
```
d           = (Σ_j D_j / T) / P               cash yield on entry
g           = (V_T / P)^(1/T) − 1             per-share value growth, P to V_T
  re-rating = (NAV_0 / P)^(1/T) − 1           price-to-NAV gap closing by exit
  NAV growth= (V_T / NAV_0)^(1/T) − 1         (1 + g) = (1 + re-rating) × (1 + NAV growth)
c           = IRR_T − d − g                   timing and compounding term
```
- **Never set g = IRR_T − d.** That plug puts c into g, so g stops being value growth. In the CAPT,
  SED and DOF Base cases the plug differed from the value CAGR by 0.6–1.9 pp, and it flatters g
  whenever value falls.
- c is usually within ±2 pp. A larger |c| means front-loaded distributions or a large value change;
  check the dividend dates. Do not interpret c as a source of return.
- **Re-rating** is the part of g that exists only because V_T is a NAV and P is a market price. It
  assumes the share trades at NAV at exit. Name it whenever P/NAV_0 is outside 0.95–1.05: a flat g
  can be a falling NAV plus a discount assumed to close (DOF Base: re-rating +4.6% a year, NAV
  growth −5.4% a year, g −1.1%).

Worked example: P = 100, D = 8 / 8 / 8, V_3 = 110, k = 12% → IRR ≈ 11.0% (d = 8.0%, g = 3.2%,
c = −0.2 pp), P_k ≈ 97.5. Margin of safety −2.5%: fails, no margin of safety.

## Step 3 — Terminal value (V_T)

V_T drives most of the result, so build it, never assume it.

- **Base it on normalized, mid-cycle economics**, not the last modelled year: mid-cycle rates ×
  operating days − normalized costs, or NAV (vessel/rig values at mid-cycle prices) less net debt.
  For oil-price-driven companies, take mid-cycle Brent and cracks from the Mid-cycle column of
  `docs/oil-market-bbb.md`. For tanker companies, take mid-cycle TCE and mid-cycle asset values
  from `docs/oil-shipping-bbb.md`, adjusted for the fleet's age at exit. For drilling
  contractors, take mid-cycle dayrate, utilization and rig values from `docs/rig-market-bbb.md`,
  adjusted for each rig's age and spec at exit. For OSV owners, take mid-cycle rate, utilization
  and vessel values from `docs/supply-market-bbb.md`, adjusted for each vessel's age and spec.
  For defense companies on Track B, normalised earnings at exit use the steady-state segment
  margins and long-end growth from `docs/defense-market-bbb.md`; its sector multiples are
  context only and never the exit multiple.
  If the sector BBB gives no Bear/Bull mid-cycle for a row, derive it from the nearest row's
  Bear/Base/Bull mid-cycle ratios and tag it `[A]`.
- **Exit multiple must be stated and independent.** Never use the IAF ceiling as the exit multiple
  (circular). For finite-life assets (ships, rigs), prefer NAV over a perpetuity multiple.
- **Roll the capital base forward**: V_T includes the value of growth capex deployed during the
  horizon (Step 4) and the change in net debt / retained cash.
- **Two NAVs at the valuation date** (both per share, less net debt at the valuation date), in the
  header with P/NAV for each:
  - NAV at **today's market marks** (broker or secondhand values). Omit if no current mark exists.
  - **NAV_0** at the **Base mid-cycle marks** (the V_T method, incl. firm-contract premium). It
    anchors the re-rating in Step 2B. Bear and Bull compute their own NAV_0 at their own marks.
- **V_T bridge (Base), from NAV_0**, in $m and per share, with the re-rating P → NAV_0 shown above
  it so the whole of g is explained:
  NAV_0 → + value created by growth capex (value at T − value in NAV_0 − capex paid in the horizon)
  → − ageing of the existing fleet at mid-cycle marks → ± firm-contract premium roll-off →
  + retained cash (Σ Maintenance FCF − D_t paid; = −Δ net debt excluding growth capex) → V_T.
  There is no separate cycle-normalisation step: with NAV_0 at mid-cycle marks it sits in the
  re-rating.
- **Interim V_t** (end of stub, Years 1–2) is a path diagnostic and does not enter IRR_T. Use the
  V_T method with asset marks gliding from today's market marks (Base mid-cycle where no market
  mark exists) to the scenario's mid-cycle value at exit; state the glide. End-of-stub marks are
  identical in all scenarios (Step 6). Marking straight to each scenario's mid-cycle at the end of
  the stub creates a spread the stub does not have, and makes "IRR to Year 1" look like a pass
  whenever P is below mid-cycle NAV.

## Step 4 — Growth as a capital-allocation decision

Growth capex lowers cash returned now and raises earning power later. Both effects must run through
the same IRR, otherwise growth only shows up as a cost.

```
Value of growth capex at T  ≈  Growth capex × ROIC_g / k
Value created               ≈  Growth capex × (ROIC_g / k − 1)
```
Example at k = 12%: 20 invested at ROIC_g 15% → worth 25 (+5). At ROIC_g 9% → worth 15 (−5).

- **ROIC_g must come from evidence**: contracted charters or day rates on the new capacity, realised
  returns on past newbuilds or projects, current newbuild price vs secondhand value (for tankers:
  newbuild prices, period rates and newbuild-parity TCE in `docs/oil-shipping-bbb.md`; for rigs:
  reactivation parity, secondhand rig prices and the contract rate secured, from
  `docs/rig-market-bbb.md` and the company's own announcements; for OSVs: newbuild and
  reactivation parity and secondhand values in `docs/supply-market-bbb.md`; for defense capacity
  such as new plants: the segment capacity balance per scenario in `docs/defense-market-bbb.md`
  — a plant needed only in Bull, or coming on line into a surplus, earns less). State the source. For
  finite-life assets, use NAV of the asset at T instead of the perpetuity formula.
- **Test ROIC_g vs k separately from Rule 1.** ROIC_g > k: growth is accretive even though D_t falls.
  ROIC_g ≤ k: growth destroys value even if revenue, earnings or FCF rise.
- **Per share**: growth funded by new shares only counts if ROIC_g > k after dilution.
- g is the result of this build. Never forecast g separately and then add it on top.

## Step 5 — Growth hygiene (both tracks)

1. Match the metric to the multiple: EPS for PE, FCF/share for P/FCF. Revenue is a driver, never g.
2. Geometric (compound) growth, never averages of annual rates. No above-k growth in perpetuity.
3. Never compute a growth rate from a base near zero or negative — work with levels.
4. Strip non-repeatable items: one-offs, asset-sale gains, M&A, FX.
5. Cyclicals: rate-driven earnings mean-revert and do not compound. Split **IRR_T** (not g alone)
   into structural and cyclical, for each scenario:
   - **Structural IRR**: the same model with every open or re-priced day from 1 Jan of Year 1 at
     **that scenario's own mid-cycle rate**. The stub, firm contract days and exit asset values are
     unchanged; unexercised options count as open days; dividends and net debt follow the cash
     flows.
   - **Cyclical = IRR_T − structural IRR** (pp), shown as Δd and Δg. For high-payout companies the
     cycle shows up mostly in d (DOF Base: +1.8 pp, all of it through d), so a g-only split misses it.
   - The gap between a scenario's structural IRR and the Base structural IRR is a **mid-cycle
     shift**, not the cycle. Using the Base structural run for Bear and Bull labels that shift
     "cyclical" (SED Bear: −31.9 pp reported as cyclical, +2.6 pp on its own mid-cycle).
6. Flag growth quality: share issuance, asset-sale gains, dependence on the cycle turning.

## Step 6 — Bear / Base / Bull

There is no statistical distribution behind sector events, so Bear and Bull are not percentiles.

- **Base**: the most likely path, from the central view of the relevant sector skill (Oil Market
  BBB, Oil Shipping BBB, Rig Market BBB, Supply Market BBB, Defense Market BBB). It carries the
  decision: IRR_T vs k and P vs P_k (Track A: Rules 1 and 3).
- **Bear**: a stress test anchored to a named catalyst from the sector skill (e.g. chokepoint
  reopening, fleet oversupply, demand shock). Report:
  - Bear IRR_T and P_k (Bear),
  - capital preservation: does ΣD_t + V_T (Bear) cover P? If not, size the permanent loss,
  - balance-sheet survival: liquidity, covenants, refinancing in the Bear path (Bear NIBOR and
    HY spread from `docs/hy-market-bbb.md` for bond refinancing).
  If Bear breaks the thesis, say so plainly.
- **Bull**: anchored to a named upside catalyst. Report Bull IRR_T and how much of it the current
  price already reflects: (P − P_k Base) / (P_k Bull − P_k Base). Negative means P is below the
  Base hurdle.
- **Stub period**: most days are already booked, so scenarios differ only on open days and spot
  exposure. Do not create an artificial spread in the stub, including in the end-of-stub asset
  marks used for interim V_t; Bear and Bull diverge from Year 1.
- **Read the structural IRRs** (Step 5) to say what kind of stress test each scenario is: a rate
  path around an unchanged mid-cycle, or a shift in the mid-cycle itself.
- Scenarios need not be symmetric. Bear is the worst reasonably foreseeable case, Bull the best.
- Optional reference figure: weight the scenario **levels** (D_t and V_T, not growth rates or IRRs)
  25/50/25 and compute one IRR. Label it "scenario-weighted reference (convention)". It never
  replaces Base as the decision figure.

## Step 7 — Output

0. **Summary** (first section, readable on its own; everything after it is the supporting build):
   - **Verdict** in 2–4 bullets: clears / marginal / fails, the Base margin of safety, Bear outcome,
     and what the price needs (the break-even assumption).
   - **Decision table** (Bear / Base / Bull): IRR_T; V_T per share; P_k and margin of safety;
     capital preserved?; cumulative Maintenance FCF per share over the horizon; net debt (or net
     cash) per share at exit; the one balance-sheet line that matters (liquidity, covenant or
     refinancing outcome).
   - **Per-share path** (Track B): columns = stub quarters (or the stub as one column), Year 1, Years
     2–3; rows for Base = EBITDA ($m and per share), Maintenance FCF per share, debt amortisation per
     share, FCF after debt service per share, D_t per share, net debt per share, V_t per share; then
     Maintenance FCF per share and V_t per share for Bear and Bull. Track A: EPS, D_t and FCF per
     share per year.
   - Keep the summary short: no method text, no sources; those stay in the sections below.
1. **Header**: company, ticker, price, valuation date, exit date and T in years, shares, market cap
   and EV, the two NAVs with P/NAV (Step 3), FX, track (A or B) and why, k used and why, sources
   per the Data sources section (connector, document and period for each key figure; price source
   and time stamp; sector outputs from `docs/oil-market-bbb.md`, `docs/oil-shipping-bbb.md`,
   `docs/rig-market-bbb.md`, `docs/supply-market-bbb.md`, `docs/defense-market-bbb.md`).
2. **Scenario definitions**: one line each for Base, Bear, Bull with the named catalyst.
3. **Near-term section**: table for the stub quarters (e.g. Q3E, Q4E) with booked share of days,
   TCE or day rate, EBITDA, FCF and dividend per share, versus consensus where available; next
   report and dividend dates (ex-date, payment date); net debt bridge to 31 Dec and net debt at the
   valuation date.
4. **Period table** per scenario: stub quarters, Year 1 quarters, Years 2–3 (Track B lines above;
   Bear and Bull may drop lines that equal Base, saying so). Show $m **and** per share for
   Maintenance FCF, FCF after debt service and net debt; a table in $m only does not meet Step 2B. Dividends are shown declared, in the
   period earned; D_t in the year-end path is paid. Then the **year-end path** (D_t, V_t, r_t, IRR
   to t) for all three scenarios. Track A: E, EPS growth, D_t per period.
5. **V_T bridge** for Base, from NAV_0 (Step 3), plus the exit asset table for all three scenarios.
6. **Growth capex test**: amount, ROIC_g with source, value created vs k.
7. **Results table** (rows in this order):

| | Bear | Base | Bull |
|---|---|---|---|
| IRR_T (Track A: d + g) | | | |
| d / g / c | | | |
| g: re-rating / NAV growth (P/NAV_0) | | | |
| Structural IRR / cyclical (pp; Δd, Δg) | | | |
| ΣD_t / V_T | | | |
| P_k (hurdle price) / margin of safety | | | |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² (Track A: PE vs ceiling) | | | |
| Capital preserved? ΣD_t + V_T vs P | | | |

   Below the table: how the structural and cyclical runs were defined, the FCF_normalised build,
   the optional scenario-weighted reference, the share of Bull already priced, Bear balance-sheet
   survival and the sensitivity table.
8. **Verdict** on the Base margin of safety (P_k / P − 1): **clears** above +2%, **marginal**
   from −2% to +2%, **fails** below −2%. Then whether it survives Bear, and the key assumptions
   that would flip the verdict.
9. **Caveat**: margin-of-safety screen, not an intrinsic valuation or price target.

**Document order** (`docs/<company>-analysis.md`): title · skill revisions and sector inputs used
· **Summary** (verdict, decision table, per-share path) · tags · Header · Scenario definitions · Company and status · Near term · Market input (sector rows
used and how they enter) · Common assumptions · Period tables and year-end path · V_T bridge ·
Growth capex test · Results · Verdict and caveat · Tracking (from the second version) · Risks and
signposts · For other modules (input for the sector BBB skills, or "no change needed") · Change
log · Appendix: own assumptions · Appendix: sources.

**Tags** on figures: `[F]` fact from a filing or market print · `[B]` derived from a disclosed
contract value · `[E]` external or secondary · `[C]` secondary source carried from an earlier
version · `[A]` own assumption · `[?]` not found.

**Tracking (after each quarterly report)**: replace the estimate with the actual, move the
valuation date forward, and add a line: actual vs model for the quarter (FCF, dividend, net debt),
change in Base P_k, and whether the company is running ahead of or behind the Base path.

## Checks before finishing

- k ≥ 10%, all figures per share and forward-looking.
- Summary first, with the decision table and the per-share path (FCF per share per period for all
  three scenarios).
- Every key figure has a source and period. Price and figures are in the same currency.
  `filings_list` was checked for share issues and new reports since the last analysis.
- Stub included, cash flows at payment dates, stub figures not annualised, ex-dividend status
  checked, net debt rolled forward to 31 Dec.
- Retained cash counted once; dilution included. Maintenance FCF is before debt amortisation.
- V_T built from normalized economics, exit multiple independent of the IAF ceiling. V_T bridge
  starts from NAV_0; end-of-stub marks are the same in all scenarios.
- g is the value CAGR (V_T vs P), never IRR − d; c is shown; the re-rating is named when P/NAV_0
  is outside 0.95–1.05.
- Structural IRR per scenario on that scenario's own mid-cycle; cyclical measured on IRR.
- FCF_normalised for Rule 3 is after the fleet-renewal charge.
- ROIC_g sourced, not assumed.
- Bear and Bull each tied to a named catalyst; no probability language.
- Base verdict uses the margin of safety P_k / P − 1 (Track B) or Rules 1 and 3 (Track A).
