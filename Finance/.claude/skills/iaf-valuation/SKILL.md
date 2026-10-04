---
name: iaf-valuation
description: Investment Analysis Framework (IAF) — the standing valuation method for this workspace. A forward-looking required-return test (d + g versus k, k = 12%), a PE or P/FCF ceiling, a year-by-year IRR build with a hurdle price for cyclical and capital-intensive companies (shipping, offshore, rigs), growth treated as a capital-allocation decision (ROIC on growth capex versus k), and Bear/Base/Bull where Base is the decision case and Bear/Bull are catalyst-based stress tests. ALWAYS use this skill when the user asks to value, screen or analyse a company, mentions IAF, "the framework", d+g, k, hurdle, PE ceiling, P/FCF, IRR, growth capex, ROIC, BBB or Bear/Base/Bull, or asks whether a stock clears the required return — even without naming IAF.
---

# Investment Analysis Framework (IAF)

**Revision:** 2026-10-04.13 — bump on every change (date.counter). This file is the master and the
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
| Nordic listed company: quarterly figures, guidance, booked days/rates, backlog, dividend policy, CEO outlook | **Nordic Financial** (`search_filings`, `company_research`) | FinancialFilings, issuer IR / Newsweb |
| Structured IS/BS/CF line items, any listed company (Nordic, EU, US, SG) | **FinancialFilings** (`companies_financials_retrieve`) | Nordic Financial text, issuer report |
| Filing list: new reports, share issues, insider trades, prospectuses | **FinancialFilings** (`filings_list`, newest first) | Nordic Financial `report_type="press_release"` |
| Share price, spot FX, futures, Oslo tickers, market cap | **Yahoo** (`get_quote`, `get_chart`, `quote_summary`) | EODHD EOD prices; AllRatesToday for spot FX |
| FX at a past moment (balance-sheet date, ex-date, payment date), several pairs at once; official central-bank rates | **AllRatesToday** (`get_rates_authenticated` with `time`, `get_official_rates`) | Yahoo `get_chart` |
| Price history (EOD) as a cross-check | **EODHD** | Yahoo `get_chart` |
| US company ratios, Brent/WTI monthly history | **Alpha Vantage** (`COMPANY_OVERVIEW`, `BRENT`, `WTI`) | FinancialFilings, Yahoo |
| Norwegian macro (policy rate, CPI, NOK FX), Nordic power price | **Nordic Financial** (`report_type="macro_summary"`, `get_current_power_price`) | — |

**Nordic Financial** (aidatanorge Nordic MCP server): about 1,500 companies listed in Oslo,
Stockholm, Helsinki and Copenhagen, plus First North, from 2020 onwards. Covers annual and
quarterly reports, Newsweb/exchange announcements, press releases and quarterly macro summaries.
- **Always set `fiscal_year`** and `ticker`. Without them, old reports (e.g. 2020) outrank the
  latest quarter.
- Use `company_research` with one section per IAF need (results, guidance/coverage, fleet and
  capex, dividend and capital allocation, debt), each with `ticker` set.
- Results are text excerpts, not tables. Read the numbers from the text and use
  `parse_pdf_to_text` for the full report when needed.
- `analyze_company` writes a synthesised answer. Use it only for orientation and never as a figure
  source.
- `get_company_info` works for the NO/DK/FI registries, not for Sweden.
- No oil-price series (`macro_summary` does not cover oil). Realised oil and gas prices appear in
  producers' quarterly reports (e.g. Equinor) and serve as a cross-check of the oil baseline only.

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

**Not used for IAF:** sector or oil forecasts from any connector. These always come from `docs/oil-market-bbb.md` and the sector BBB documents.

## Definitions

| Symbol | Meaning |
|---|---|
| P | Current share price (entry price) |
| E / FCF | Earnings, or free cash flow to equity. Use FCF for capital-intensive and cyclical sectors |
| D_t | Cash returned to shareholders in period t per share (dividends + buybacks), placed at its payment date |
| d | Annualised distribution yield on entry price: (Σ D over the horizon ÷ T) ÷ P |
| V_t | Value per share at end of year t (see Terminal value) — V_0 = P |
| g | Per-share growth in value/earning power. An output of the build, not a free input |
| IRR | Return that equates P with the D_t stream plus V_T. Equivalent to d + g |
| P_k | Hurdle price: the most you can pay and still earn exactly k |
| ROIC_g | Return on growth capex (new capital deployed) |

## Step 1 — Choose the track

- **Track A (steady):** stable earnings, low capex volatility. Use E, PE and a growth rate.
- **Track B (cyclical / capital-intensive):** shipping, offshore, rigs, commodities, or any company
  where capex, D&A or rates swing earnings. Use FCF, the year-by-year IRR build and P_k.
- State which track and why. When in doubt, use Track B.

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
rate. Cross-check: sustainable g ≈ ROIC × reinvestment rate. If the forecast g needs more
reinvestment than the payout leaves, d and g are inconsistent — fix one of them.

Rule 3 combines a total-return hurdle with a no-growth earnings-yield anchor. It is a heuristic for
how much premium is defensible, not a value from a cash-flow model.

## Step 2B — Track B: year-by-year IRR build

For each period (stub quarters, Year 1 quarters, Years 2–3), build per share:

| Line | Content |
|---|---|
| Maintenance FCF | Cash generated before growth spending (after interest, tax, maintenance capex, drydock) |
| Growth capex | Capital spent to expand the earning base (new vessels, rigs, projects), net of new debt raised for it |
| Retained cash | Maintenance FCF − growth capex − D_t (goes into V_t via net debt / cash) |
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
Implied split     d = (Σ D_j / T) / P,   g = IRR_T − d
```
- Retained cash must be counted exactly once: either paid out in D_t or added to V_t, never both,
  never neither.
- r_t and IRR-to-each-year are a path diagnostic, not a per-year pass/fail. A weak middle year is
  not a failure, but it must be visible.
- Rule 3 cross-check: P/FCF_normalized < IRR_T / k². Report it, but decide on P vs P_k (the
  ceiling uses an IRR that itself depends on P).

Worked example: P = 100, D = 8 / 8 / 8, V_3 = 110, k = 12% → IRR ≈ 11.0% (d = 8.0%, g = 3.0%),
P_k ≈ 97.5. Fails the hurdle by ~2.5%: no margin of safety.

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
- **Exit multiple must be stated and independent.** Never use the IAF ceiling as the exit multiple
  (circular). For finite-life assets (ships, rigs), prefer NAV over a perpetuity multiple.
- **Roll the capital base forward**: V_T includes the value of growth capex deployed during the
  horizon (Step 4) and the change in net debt / retained cash.
- Show V_T as a bridge: starting value → + value of growth capex → ± net debt change → ± cycle
  normalization → V_T.

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
  reactivation parity and secondhand values in `docs/supply-market-bbb.md`). State the source. For
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
5. Cyclicals: rate-driven earnings mean-revert and do not compound. Split g into **structural**
   (growth capex at ROIC_g, NAV change) and **cyclical** (rates vs mid-cycle), and report both.
6. Flag growth quality: share issuance, asset-sale gains, dependence on the cycle turning.

## Step 6 — Bear / Base / Bull

There is no statistical distribution behind sector events, so Bear and Bull are not percentiles.

- **Base**: the most likely path, from the central view of the relevant sector skill (Oil Market
  BBB, Oil Shipping BBB, Rig Market BBB, Supply Market BBB). It carries the decision: IRR_T vs k and P vs P_k.
- **Bear**: a stress test anchored to a named catalyst from the sector skill (e.g. chokepoint
  reopening, fleet oversupply, demand shock). Report:
  - Bear IRR_T and P_k (Bear),
  - capital preservation: does ΣD_t + V_T (Bear) cover P? If not, size the permanent loss,
  - balance-sheet survival: liquidity, covenants, refinancing in the Bear path.
  If Bear breaks the thesis, say so plainly.
- **Bull**: anchored to a named upside catalyst. Report Bull IRR_T and how much of it the current
  price already reflects.
- **Stub period**: most days are already booked, so scenarios differ only on open days and spot
  exposure. Do not create an artificial spread in the stub; Bear and Bull diverge from Year 1.
- Scenarios need not be symmetric. Bear is the worst reasonably foreseeable case, Bull the best.
- Optional reference figure: weight the scenario **levels** (D_t and V_T, not growth rates or IRRs)
  25/50/25 and compute one IRR. Label it "scenario-weighted reference (convention)". It never
  replaces Base as the decision figure.

## Step 7 — Output

1. **Header**: company, ticker, price, valuation date, exit date and T in years, track (A or B)
   and why, k used and why, sources per the Data sources section (connector, document and
   period for each key figure; price source and time stamp; sector outputs from
   `docs/oil-market-bbb.md`, `docs/oil-shipping-bbb.md`, `docs/rig-market-bbb.md`,
   `docs/supply-market-bbb.md`).
2. **Scenario definitions**: one line each for Base, Bear, Bull with the named catalyst.
3. **Near-term section**: table for the stub quarters (e.g. Q3E, Q4E) with booked share of days,
   TCE or day rate, EBITDA, FCF and dividend per share, versus consensus where available; next
   report and dividend dates (ex-date, payment date); net debt bridge to 31 Dec.
4. **Period table** per scenario: stub quarters, Year 1 quarters, Years 2–3 (Track B lines above).
   Track A: E, EPS growth, D_t per period.
5. **V_T bridge** for Base, starting from net debt at 31 Dec of the current year.
6. **Growth capex test**: amount, ROIC_g with source, value created vs k.
7. **Results table**:

| | Bear | Base | Bull |
|---|---|---|---|
| IRR_T (or d+g) | | | |
| d / g split (g: structural / cyclical) | | | |
| P_k (hurdle price) / margin of safety | | | |
| PE or P/FCF ceiling (Rule 3) vs actual | | | |
| Capital preserved? (Bear) | | | |

8. **Verdict**: clears / marginal (within ±2% of k) / fails, based on Base; whether it survives
   Bear; key assumptions that would flip the verdict.
9. **Caveat**: margin-of-safety screen, not an intrinsic valuation or price target.

**Tracking (after each quarterly report)**: replace the estimate with the actual, move the
valuation date forward, and add a line: actual vs model for the quarter (FCF, dividend, net debt),
change in Base P_k, and whether the company is running ahead of or behind the Base path.

## Checks before finishing

- k ≥ 10%, all figures per share and forward-looking.
- Every key figure has a source and period. Price and figures are in the same currency.
  `filings_list` was checked for share issues and new reports since the last analysis.
- Stub included, cash flows at payment dates, stub figures not annualised, ex-dividend status
  checked, net debt rolled forward to 31 Dec.
- Retained cash counted once; dilution included.
- V_T built from normalized economics, exit multiple independent of the IAF ceiling.
- ROIC_g sourced, not assumed.
- Bear and Bull each tied to a named catalyst; no probability language.
- Base verdict uses P vs P_k (Track B) or Rules 1 and 3 (Track A).
