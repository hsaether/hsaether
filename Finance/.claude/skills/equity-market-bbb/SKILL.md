---
name: equity-market-bbb
description: Equity Market BBB — the equity index baseline for Oslo (OSEBX) and global equities (MSCI World, in NOK unhedged and in USD). Applies the IAF method at index level (d + g + re-rating, a year-by-year IRR build, the hurdle level at k = 12%) and produces Bear/Base/Bull index total-return paths on the IAF time grid (stub of the current year + 3 calendar years, now 2027–2029), index EPS and P/E paths, the NOK scenario path, mid-cycle returns, the oil and NOK linkage (correlations, betas, the energy share of Oslo earnings), and equity triggers that mirror the HY trigger (E / R against the Nordic HY market reference, Base IRR against k and against the HY book). Oslo energy earnings follow the Brent path in docs/oil-market-bbb.md; NIBOR, Nordic GDP and the HY return come from docs/hy-market-bbb.md. Base is the decision case; Bear and Bull are catalyst-based stress tests; 25/50/25 is a labelled convention, never a probability. ALWAYS use when the user mentions Equity BBB / Equity Market BBB / aksjemarked, asks to create, run or update ("oppdater modul") the equity module, or asks about the Oslo Børs or OSEBX outlook, Oslo valuation (P/E, P/B), global equity or MSCI World expected returns, equities versus high yield, when to move from HY to equities, the oil–Oslo or oil–NOK correlation, or whether to hold Norwegian or global equity funds — even without naming the skill. Fund mode applies the baseline to named equity funds, active (DNB Teknologi, Gambak) or index (DNB Global Indeks, Nordnet Global Indeks) — look-through, cyclical blocks or index tilts, all-in cost, alpha or tracking difference, hurdle NAV and E / R against HY; output docs/<fund>-analysis.md. ALWAYS use it when the user asks to analyse, keep or switch an equity fund. It is the only place an equity index return path, an index hurdle or a NOK scenario path is set.
---

# Equity Market BBB

**Revision:** 2026-10-12.2 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/equity-market-bbb/` in the Finance folder.

An index-level baseline for Oslo and global equities. It answers one question: **what total
return can an index investor in NOK expect, year by year, from today's price, and at what index
level do equities beat the Nordic high-yield alternative on the same risk rule?** It is a
testable hypothesis with explicit risks, not a market commentary and not a price target.

Place in the chain:

- Reads `docs/oil-market-bbb.md` (Brent path and mid-cycle → Oslo energy earnings) and
  `docs/hy-market-bbb.md` (NIBOR path, Nordic GDP, HY spreads and defaults → Oslo financials and
  the Bear macro; Nordic HY expected return → the comparison). Reads the HY decision rule and
  market reference from `docs/hy-funds-analysis.md` and the user's HY book figures from
  `docs/portfolio-overview.md`. Defense and sector baselines are context only.
- Never makes its own oil, rate, GDP or credit forecast. If an upstream baseline is stale, this
  baseline is provisional.
- Feeds the portfolio discussion (`docs/portfolio-overview.md`) and gives [[iaf-valuation]] the
  market context for k. It never lowers k.

**Scope:** broad equity indices held through index or broad funds: Oslo (OSEBX), global developed
(MSCI World; ACWI as cross-check), and the NOK translation. **Out of scope:** single stocks
(→ [[iaf-valuation]]), sector forecasts (→ the sector BBBs), bonds (→ [[hy-market-bbb]]).
**Named equity funds** (active or sector funds held by the user or proposed to them) are covered
by **Fund mode** below: they apply this baseline and never change it.

## Standing parameters

- **Time grid = IAF grid:** stub (rest of the current year) + 3 calendar years, now Q4 2026 +
  2027–2029. Exit 31 Dec of the third year. Roll forward with the first run each January.
- **Return basis:** total return in **NOK**, before fund fees and before tax, as a geometric
  annual rate. World is shown in NOK unhedged (the decision basis) and in USD (local); hedged NOK
  ≈ USD return + NIBOR − USD short rate.
- **Annual paths only.** An index has no booked days, so there is no Year-1 quarterly split.
- **Stub has no scenario spread** (IAF rule): price flat by convention, dividend accrual only,
  identical in all scenarios. Scenarios diverge from Year 1.
- **Base = the decision case.** Bear and Bull are stress tests tied to named catalysts, the same
  macro catalysts as [[hy-market-bbb]] so that equity and HY are stressed in the same world.
  **25/50/25** is a labelled convention, never a probability.
- **k = 12%** (IAF) is reported as the index hurdle. It is a single-stock hurdle; for an index the
  allocation test is the HY comparison (see Decision rules). Neither ever lowers k for IAF.
- **Minimum change (convention):** a Base window return changes only if the evidence moves it by
  at least 1.0 pp a year; a trigger level only if it moves by at least 3%. Smaller moves are noted.
- **Staleness:** stale after 30 days, after an update of the oil or HY baseline that flags a
  change, or after an index move of more than 10% within a month.

## Files

- Skill: `.claude/skills/equity-market-bbb/SKILL.md`, plus `references/` with the Python scripts
  of the last run (fetch, look-through, consensus, correlations, model, triggers) and a README.
- Output: `docs/equity-market-bbb.md`, one running baseline. Baseline date in the H1. Git holds
  history, so read the previous version before overwriting it.
- Fund mode output: `docs/<fund>-analysis.md`, one running file per fund (e.g.
  `docs/dnb-teknologi-analysis.md`). Index funds compared for the same role share one file
  (`docs/global-index-funds-analysis.md`). Fund-mode scripts are in `references/fund/`.
- Calculations run in the scratchpad (`py -I`, copies of the reference scripts) from fetched raw
  data. The document records inputs, method and results so a later run can reproduce them; copy
  changed scripts back to `references/`.
- Write with Write/Edit, then **read the file back** and check every table and number.

## Benchmarks and units

| Series | Definition | Unit | Role |
|---|---|---|---|
| Oslo | **OSEBX** (Oslo Børs Benchmark Index, gross: dividends reinvested), Yahoo `OSEBX.OL` | index points, NOK | BBB index; returns are total returns |
| Oslo valuation | **MSCI Norway** fundamentals (P/E, forward P/E, P/BV, dividend yield; month-end) | x, % | Valuation anchor (12 stocks, ~85% of float) |
| Oslo earnings base | Bottom-up consensus EPS for the current and next calendar year, top constituents covering ≥ 75% of index weight (Yahoo `earningsTrend`) | NOK per share, weighted | Index P/E on CY+1, block earnings shares |
| World | **MSCI World**; total return proxied by iShares MSCI World ETF `URTH` adjusted close (after 0.24% fee and withholding) | USD | BBB index |
| World valuation | MSCI World fundamentals (month-end); S&P 500 forward P/E, CY growth from FactSet Earnings Insight (weekly) | x, % | Valuation and earnings anchor |
| World in NOK | URTH adjusted × USD/NOK | NOK | Decision basis (unhedged) |
| **NOK (the krone itself)** | **I-44**, Norges Bank import-weighted krone index (44 trading partners; **rising = weaker NOK**), Norges Bank API `EXR/B.I44.NOK.SP` (daily fixing), `M` / `A` averages | index | NOK scenario path (Base = Norges Bank's MPR projection), NOK–oil linkage, NOK level vs history |
| NOK cross rates | USD/NOK and EUR/NOK: Norges Bank fixing `EXR/B.USD+EUR.NOK.SP` (14:15 CET) for history; Yahoo `NOK=X`, `EURNOK=X` for the latest spot | NOK per unit | USD/NOK translates World (≈ 70% USD); it is not "the NOK" |
| Brent | `BZ=F` front month, month-end from daily closes | $/bbl | Correlation series only; the price path comes from the oil baseline |

- **Month-end series are built from daily closes.** Yahoo's monthly bars carry misaligned
  timestamps for futures (collisions and missing months, tested 2026-10-11); daily → month-end
  avoids that. Returns are monthly log returns.
- OSEBX is a gross index: an index level trigger drifts up by the dividend yield (~0.45% a month)
  between runs. Give triggers both as a level on the run date and as a multiple at unchanged
  earnings.
- Never mix price and total-return series in one comparison, or USD and NOK returns.

## Data sources

| Need | First choice | Fallback / cross-check |
|---|---|---|
| Index levels, ETF prices, FX, Brent (daily → month-end) | **Yahoo** chart API via Python (`query1.finance.yahoo.com/v8/finance/chart/<sym>?interval=1d`, User-Agent header); MCP `get_chart` for a few points | EODHD EOD prices |
| Constituent prices, market caps, forward P/E, dividend yield | **Yahoo** quote API via Python with cookie + crumb (`fc.yahoo.com` → `/v1/test/getcrumb` → `/v7/finance/quote?symbols=…&crumb=`); MCP `get_quote` (verbose) | Nordnet (read-only, Edge) |
| Consensus EPS CY / CY+1 per constituent, number of analysts | **Yahoo** `/v10/finance/quoteSummary/<sym>?modules=earningsTrend,earnings` (crumb) | Zacks for US listings and ADRs |
| ETF look-through: sector weights, top holdings, P/E, P/B | Yahoo quoteSummary `topHoldings` (OBXD.OL = DNB OBX ETF, NORW/ENOR = MSCI Norway, URTH, ACWI, SPY) | Issuer factsheets |
| Index fundamentals (P/E, fwd P/E, P/BV, yield) and top weights | **MSCI index pages** (`msci.com/indexes/index/957800` Norway, `990100` World) via WebFetch | MSCI factsheet PDFs |
| US earnings path and valuation | **FactSet Earnings Insight** PDF (weekly; WebFetch saves the PDF, read with `pypdf` under `py -I`) | Yardeni, press |
| NIBOR path, Nordic GDP, HY spreads, HY expected return | **`docs/hy-market-bbb.md`** | — never an own path |
| HY decision rule, market reference E / R, HY book figures | `docs/hy-funds-analysis.md`, `docs/portfolio-overview.md` | — |
| Brent path and mid-cycle | **`docs/oil-market-bbb.md`** | — never an own path |
| US 10-year, US HY OAS (yield-gap and credit context) | **FRED** `DGS10`, `BAMLH0A0HYM2` | — |
| Norway 10-year (yield gap), zero-coupon curve | **Norges Bank API** `GOVT_GENERIC_RATES/B.10Y.GBON` (daily), `GOVT_ZEROCOUPON/B.<tenor>` | FRED `IRLTLT01NOM156N` (OECD monthly, lagged) |
| I-44, TWI, USD/NOK, EUR/NOK history (daily fixings, month-end series from 1995; monthly averages from 1990) | **Norges Bank API** `EXR` (see the iaf-valuation skill, Norges Bank paragraph) | Yahoo (cross rates only; Yahoo has no I-44) |
| NOK projection (Base anchor) | **Norges Bank MPR dataset** `data-mpr-<n>-<yy>.xlsx`: sheet **Data D** (Table 3: annual I-44 level, CPI, policy rate) and **Data E** (quarterly I-44 and 3M money-market rate) | MPR PDF Table 3 |
| Norges Bank FX purchases for the GPFG (NOK flow) | **Norges Bank API** `ANN_FX_SPU` (NOK m per day for each month; `B` = Norges Bank buys FX, i.e. sells NOK; `S` = sells FX) | Monthly press release ("Foreign exchange transactions in <month>") |
| Financial conditions (signpost) | **Norges Bank API** `FINANCIAL_INDICATORS/D.FCI_TOTAL`, `FCI_STOCK` (positive = tighter) | — |

Connector quirks (tested 2026-10-11):

- **Yahoo ETF `topHoldings` ratios are inverted:** `priceToEarnings` 0.0712 means P/E 14.0
  (earnings yield), `priceToBook` 0.403 means P/B 2.48. Invert before use.
- Yahoo `epsCurrentYear` for NOK-listed USD reporters is in USD while the price is in NOK
  (Equinor `priceEpsCurrentYear` 75 is wrong). Convert EPS with spot FX; `trailingPE` and
  `forwardPE` on the quote are already currency-consistent. Yara's consensus EPS is in NOK.
- `^OSEAX` is not on Yahoo; `OSEBX.OL` starts 5 Mar 2013, so correlation windows start Mar 2013.
- Yahoo has no I-44; take it from the Norges Bank API. Norges Bank fixings (14:15 CET) differ
  slightly from Yahoo closes (9 Oct 2026: USD/NOK 9.5623 vs 9.5555); never mix the two in one
  return series.
- Norges Bank `EXR` quirks: `UNIT_MULT` = 2 means per 100 units; holidays return blank lines;
  monthly (`M`) values are averages, so build month-end series from the daily (`B`) file.
- The `norges-bank` MCP connector gives the same values for spot checks (latest I-44, FCI,
  10-year), but the 30-year `EXR` histories and `ANN_FX_SPU` (buy/sell direction) come from the
  direct CSV API; see the iaf-valuation skill, Norges Bank paragraph.
- Yahoo quote `dividendYield` is in percent (3.54 = 3.54%); `trailingAnnualDividendYield` is a
  fraction and is often wrong for USD reporters. Use `dividendYield`.
- MSCI index pages give fundamentals at the last month-end and the top-10 weights; sector weights
  did not render. MSCI Norway has only 12 constituents: use it for valuation, not for weights
  below the top 10.
- No free source gives a long series of Oslo forward P/E or P/B. Historical anchors are secondary
  (`[E]`); state them as such.

## Data discipline

- Tag every number: `[F]` reported fact or market print · `[E]` external forecast or secondary
  claim · `[A]` own assumption · `[?]` unknown.
- **Provenance:** source, as-of date (observation date, not fetch date), unit and currency on every
  fetched value. Raw values go to the appendix before conversion.
- **Validate:** units (%, fraction, inverted ratios), currency (USD EPS vs NOK price), basis
  (price vs total return, trailing vs forward vs CY+1), staleness (prices older than 1 trading day,
  fundamentals older than the last month-end, consensus older than 1 month), plausibility (a move
  > 10% vs the previous document is confirmed in a second source), cross-source (MSCI vs ETF
  look-through vs bottom-up; explain gaps, never average them away).
- **User input is input, not a reference:** assess claims (correlations, rules of thumb, tax
  points) against data, keep what holds, and record the assessment.

## Method

### Step A — Oslo: index earnings in blocks

Split index earnings into three blocks, using the bottom-up sample (weights from the DNB OBX ETF
or MSCI Norway; GICS-like sectors from the ETF look-through):

| Block | Content | Driver (upstream) |
|---|---|---|
| **E — Oil-linked** | E&P, oil service, tankers/shipping classified as energy | Brent path and mid-cycle (`docs/oil-market-bbb.md`), × USD/NOK |
| **F — Rates and credit** | Banks, insurers | NIBOR path, defaults (`docs/hy-market-bbb.md`) |
| **O — Other** | Industrials (incl. defense), seafood, consumer, materials, telecom, tech | Nordic GDP + inflation; Bear macro from [[hy-market-bbb]]; half in foreign currency |

- **Earnings base = consensus CY+1 (now 2027) index EPS = 100.** Block shares are the shares of
  CY+1 consensus earnings, not of market cap.
- **Energy block:** `EPS_E,t / EPS_E,cons = (Brent_t − c) / (B_cons − c) × (USDNOK_t / USDNOK_0)`.
  - c = cash-cost-like break-even, **$30/bbl** `[A]` (elasticity ≈ 1.5 at $90). Gas prices,
    tanker and oil-service lags are not modelled separately; say so.
  - **B_cons** = the Brent level the consensus implies: from the largest producer's consensus EPS
    change between CY and CY+1 against the CY Brent average (same c). State it.
- **F block:** relative to consensus, from the NIBOR path (net interest margin) and the HY default
  path (credit losses). Bear peaks losses in the HY Bear default peak year.
- **O block:** consensus less a haircut for analyst optimism in Year 1 `[A]`, then nominal growth
  (GDP + inflation); Bear from the HY Bear GDP path.
- **Normalised exit-year EPS** (the year after exit): energy at the scenario's **mid-cycle Brent**,
  F at mid-cycle NIBOR, O on trend. This is the V_T basis (IAF Step 3: normalised, never the last
  modelled year by default).

### Step B — World: index earnings

- **Earnings base = consensus CY+1 EPS = 100**, anchored on FactSet's S&P 500 CY+1 growth and the
  MSCI World trailing/forward P/E ratio. Base takes a Year-1 haircut for analyst optimism `[A]`
  (state the size), then nominal growth fading toward ~5–6%.
- Bear and Bull take the global recession / soft-landing paths that match [[hy-market-bbb]].
- **Currency:** the NOK path is set in **I-44** terms and translated to USD/NOK for World (≈ 70%
  USD) and for Oslo's USD earners.
  - **Base = Norges Bank's latest MPR I-44 projection** (MPR 3/26: flat 110.0 from Q4-26 to
    2029) `[E]`, with cross rates unchanged against each other `[A]`. If the MPR level differs
    from today's fixing by more than 3%, say so and use the MPR path from Year 1.
  - **Bear:** the NOK weakens with risk-off and oil Bear. Calibrate on episodes: I-44 rose 14–18%
    in the GFC, the 2014–16 oil crash and Covid, 5% in 2022; USD/NOK rose 1.4–2.9 times as much.
  - **Bull:** the NOK firms slightly.
  - State each scenario in I-44 and in USD/NOK.

### Step C — Valuation path and IRR (IAF at index level)

```
V_t (year-end t)  = forward P/E_t × EPS_(t+1)          interim marks, path diagnostic
V_T (exit)        = mid-cycle P/E (scenario) × normalised EPS_(T+1)
D_t               = payout × EPS_t                      dividends + net buybacks, mid-year
Stub              = price flat, D = cash yield × stub length (same in all scenarios)
IRR_T solves      P = Σ D_t/(1+IRR)^t + V_T/(1+IRR)^T   (XIRR on dates; T = stub + 3)
Hurdle level      P_k = Σ D_t/(1+k)^t + V_T/(1+k)^T     k = 12%;  margin of safety P_k / P − 1
Annual return r_t = (D_t + V_t − V_(t−1)) / V_(t−1)     V_stub-end = P
```

- **P/E paths are forward 12-month P/E at each year-end.** The exit P/E is the scenario's
  **mid-cycle P/E**, anchored on long-run averages of forward P/E (state source and period) and
  cross-checked with P/B against ROE (P/B ÷ P/E = implied ROE). Never use k's ceiling as the exit
  multiple.
- **Return split (Base):** d = (ΣD/T)/P; g = (V_T/P)^(1/T) − 1, split into normalised EPS growth and
  re-rating (P/E_exit ÷ P/E_now); c = IRR − d − g. Never set g = IRR − d.
- **Structural run:** EPS at the normalised level from Year 1; cyclical = IRR − structural.
- **Payout consistency:** retained earnings (1 − payout) must fund the EPS growth assumed. If
  growth needs more than ROE × retention, cut growth or payout.

### Step D — Mid-cycle return

Long-run expected annual return at mid-cycle earnings and P/E, no re-rating:
`cash yield (payout ÷ mid-cycle P/E) + long-run nominal EPS growth`. Used for horizons beyond the
window (pension blocks) and as the equity risk premium check against mid-cycle NIBOR.

### Step E — Oil and NOK linkage (monitor, every run)

From month-end closes (Step "Benchmarks"), monthly log returns, windows: full sample, 10, 5 and 3
years, plus rolling 36-month correlations at each September:

- Correlations: OSEBX–Brent, OSEBX–World (USD and NOK), **NOK (I-44)–Brent**, NOK/USD–Brent,
  NOK/EUR–Brent, NOK (I-44)–World, World–Brent. NOK strength = −Δlog(I-44). The I-44 series runs
  from 1995 (daily), so its oil link can be measured from 2007 (Yahoo Brent) — longer than the
  OSEBX window. Betas: OSEBX to Brent; regressions OSEBX = a + b1·World(USD) + b2·Brent (R²) and
  NOK (I-44) = a + b1·World + b2·Brent.
- Volatility: OSEBX, World in USD and in NOK, Brent, I-44, USD/NOK.
- **NOK level:** I-44 today against its averages since 1990, 2000 and 2014 and its percentile;
  Norges Bank's GPFG FX flow (`ANN_FX_SPU`) for the months since the last run.
- Episodes: oil crash 2014–16, Q4-18, Covid, 2022, and the current year.
- Report the **energy share of Oslo earnings** (CY and CY+1) next to the cap weight, and the
  **Oslo IRR sensitivity to the Brent path** (± $10/bbl on every year and mid-cycle).
- Read the result: correlation measures co-movement of monthly returns; the earnings link
  (energy share × Brent path) is what moves the 3-year return.

## Scenarios

- **Base:** oil Base + HY Base (Norges Bank path) + global earnings growth slowing to trend;
  P/E drifting toward its mid-cycle level. The decision case.
- **Bear:** the [[hy-market-bbb]] Bear: oil Bear (durable Iran–USA deal + OPEC+ market share)
  together with a global recession; earnings fall, P/E compresses, NOK weakens.
- **Bull:** the [[hy-market-bbb]] Bull: soft landing, oil Base, earnings meet consensus, P/E holds.
- **Side case (not weighted):** oil Bull / stagflation (renewed war escalation): Oslo energy
  earnings jump while global equities fall. Report its Year-1 return for Oslo and World to show
  the hedge between the two. Choose Bear and Bull on what stresses an index investor most, and
  say why the side case is not the Bear.
- Each tail names catalysts, mechanism, earliest timing and signposts. No probability language.

## Decision rules (equity mirror of the HY trigger)

All per index, in NOK, before tax, after an index-fund fee of **0.20%** `[A]`:

- **E** = Base window IRR − Base NIBOR over the window − fee. **R** = Base 2027 − Bear 2027
  (Year-1 stress loss). Same definitions as the HY fund mode.
- **Attractive vs HY:** E / R ≥ the **HY market reference** (now 0.196, from
  `docs/hy-funds-analysis.md`). Compare also with the user's HY book E / R
  (`docs/portfolio-overview.md`).
- **IAF test:** Base IRR vs k = 12% and the margin of safety P_k / P − 1 (clears > +2%, marginal
  ±2%, fails < −2%).
- **Triggers:** solve for the index level (price change at unchanged earnings) where
  (1) E / R = HY market reference, (2) Base IRR = k, (3) Base IRR = the HY book's Base return,
  (4) E / R = HY book. Report each as % from today, as the index level, and as the multiple at
  unchanged earnings (Oslo forward P/E and P/B; World forward P/E).
- **Long horizons:** R is a one-year stress. For pension money with a 6–16 year horizon also show
  the Bear window return and the mid-cycle return; the allocation choice is the user's.
- **Tax note** (taxable AF accounts): equity net ≈ e − 0.3784 × (e − skjermingsrente) vs HY
  × (1 − 0.22). Inside pension wrappers the asset's tax rate does not matter. Point to the
  break-even in `docs/portfolio-overview.md`; never let tax change the market baseline.

## Procedure

Three modes: **Initiate** (no `docs/equity-market-bbb.md`), **Update** ("update Equity BBB",
"oppdater modul" in an equity context, or a recalibration trigger) and **Fund** (a named equity
fund; see Fund mode, which has its own steps). Run every step; actively try
to falsify Base. If the evidence does not move it by the minimum change, say **Equity Market BBB
kept unchanged**.

**Step 0 — Setup.** State this skill's revision and the revisions behind each upstream document.
Note dates, days since the previous baseline, and whether the oil and HY baselines are fresh. Read
the previous baseline and record its point values, triggers and signposts.

**Step 1 — Market snapshot.** OSEBX, URTH, ACWI, S&P 500, USD/NOK, EUR/NOK, Brent: last close
with time stamp. MSCI Norway and MSCI World fundamentals (month-end). US 10-year, US HY OAS,
Norway 10-year. Earnings yield gaps (forward E/P − 10-year yield) for Oslo and World.

**Step 2 — Oslo earnings base.** Bottom-up CY and CY+1 consensus for the top constituents (≥ 75%
of weight, with number of analysts): index P/E on CY and CY+1, dividend yield, block earnings
shares, B_cons. Cross-check the index P/E with MSCI Norway's forward P/E.

**Step 3 — World earnings base.** FactSet: forward P/E vs 5- and 10-year averages, trailing P/E,
CY and CY+1 growth, revisions. MSCI World P/E, forward P/E, P/BV. Sector concentration (top 10,
tech share).

**Step 4 — Linkage.** Step E above; compare with the previous run.

**Step 5 — Paths.** EPS (Steps A, B), P/E paths, NOK path, payout, per scenario. Run the model;
annual returns, window IRR, P_k, structural run, return split, sensitivities (exit P/E ± 1, Brent
± $10 for Oslo, FX for World).

**Step 6 — Test BBB.** What would make Base wrong (earnings revisions, P/E regime, oil and NIBOR
paths), and is it visible? Are the catalysts still right? Has a signpost been crossed?

**Step 7 — Decision rules and triggers.** E, R, E / R vs the HY references; trigger levels.

**Step 8 — Write, log and check.** Write the document in the output format; full change log
(previous → new with reason); read it back; run the checks.

## Fund mode

Applies the baseline to a named equity fund. It answers: **what does this fund return in NOK after
its cost, per unit of the same stress, against the HY book and against an index fund holding the
same market — and at what NAV would it clear k?** It never changes an index path, a NOK path or
a trigger in `docs/equity-market-bbb.md`. If the baseline is stale, update it first or mark the
fund analysis provisional.

First run: DNB Teknologi A, 11 Oct 2026 (`docs/dnb-teknologi-analysis.md`). Base 4.8% after
cost; P/E 15.8 on CY+1 consensus but 19.1 without memory chips. Re-run 12 Oct on the AI BBB
layer paths: Base 4.9%; 65% of NAV in AI layers; its AI holdings returned 5.2% before cost
against ~2.2% for the AI baskets on the same paths. The Samsung preference shares were found
from the gap between the country weight and the listed lines: check country and currency
weights against the holdings list. First index-fund run: DNB Global
Indeks A vs Nordnet Global Indeks, 11 Oct 2026 (`docs/global-index-funds-analysis.md`). Nordnet's
fund had switched to the MSCI World Climate Change Index (energy 0.3%, IT 37%, P/E premium
×1.056). Base 5.8% vs 6.2%, and the gap reverses if half the premium goes. Re-run 12 Oct on the AI BBB
layers: AI is 26.8% of MSCI World and 32.0% of the climate index. Nordnet's Base fell to 5.79% vs
DNB's 5.84%. The implied rest of World needs 8.8% a year of EPS growth, which is flagged to the Equity BBB.

### Fund data

| Need | First choice | Fallback / cross-check |
|---|---|---|
| NAV and date, fund size, number of holdings, top 10, sectors, countries, **currency mix**, management fee, benchmark, returns (calendar, 3/5/10 y), risk (vol, beta, tracking error, max drawdown) | Manager's fund page via WebFetch (DNB AM: `dnbam.com/en/our-funds/funds/<fund>`; the dnb.no fund-list pages return nothing) | Storebrand fund profile, Morningstar |
| **Top 25 holdings with weights**, total cost ("Total pris"), regions | **Nordnet fund page** via WebFetch (`nordnet.no/market/funds/<id>-<name>`); month-end holdings | Manager's monthly report |
| NAV history (daily) | **Yahoo** chart API on the Morningstar id (`0P00000MVB.IR` = DNB Teknologi A; find with Yahoo search `/v1/finance/search?q=<ISIN or name>`). History may start late (DNB Teknologi: Mar 2022) | Manager's calendar-year table |
| Prices and consensus EPS of the holdings | **Yahoo** quoteSummary (`earningsTrend`, `price`, `summaryDetail`, `defaultKeyStatistics`, `financialData`; script `references/fund/hold.py`) | Zacks for US listings |
| Sector earnings cycle (margins vs average, growth by industry) | **FactSet Earnings Insight** PDF; read with `pypdf` under `py -I` (WebFetch cannot decode it) | — |
| Sector ETF look-through P/E (benchmark context) | Yahoo `topHoldings` (IXN tech, IXP communication services, XLK, QQQ; ratios inverted) | — |

Quirks seen (11 Oct 2026):
- The manager's page may garble calendar-year labels. Cross-check at least three years against
  the Yahoo NAV.
- Yahoo EPS for some Oslo-listed USD reporters is in NOK (Nordic Semiconductor). Check that the
  forward P/E from the quote agrees.
- Large one-off gains distort CY EPS (Alphabet and Amazon 2026). Value on CY+1 and leave the
  distorted year out of the growth figure.
- Thin or inconsistent +1y estimates (Atlassian: 8 analysts against 30): use the quote's forward
  P/E.
- Fiscal years: blend June/July year-ends half and half into calendar years. Map Jan–Mar
  year-ends to the calendar year they mostly cover, and Sep–Oct year-ends to the same calendar
  year.

Index-fund data and quirks (11 Oct 2026):
- **Index fundamentals and weights:** the MSCI factsheet PDF of the fund's index
  (`msci.com/documents/10199/255599/<index-name>-usd-net.pdf`, curl, text with `pypdf`): P/E,
  forward P/E, P/BV, yield, sectors, top 10 next to the parent index, net returns, beta, tracking
  error, turnover. MSCI World's own factsheet shows **gross** annual returns; take net returns from
  the parent column of the tilted index's factsheet. A plain-named URL can serve a renamed index
  (World Climate Change → "Climate Change CTB"); match the launch date and top-10 weights against
  the fund's holdings list.
- **KIDs:** Nordnet's fund page links the PRIIP KID on `doc.morningstar.com`. curl it and read it
  with `pypdf` for structure, replication, counterparty, ongoing and transaction costs, and index.
- **Nordnet URLs:** `market/funds/<id>` can resolve to a sister fund (18142188 is the leveraged
  Nordnet Global Indeks 125). Use the `fond/liste/<name>-nok-<hash>` page and check the NAV.
- **dnb.no fund pages** (incl. the pension fund list) return only security.txt to WebFetch; read
  them in the in-app browser. They give the DNB platform fee and transaction costs.
- Yahoo fund ids: DNB Global Indeks A `0P0000PS3V.IR` (NAV from Mar 2022), Nordnet Global Indeks
  NOK `0P0001K6NJ.IR` (from Sep 2020); find others with Yahoo search on the ISIN. Yahoo lags the
  manager's NAV by a day or more: take the NAV of the market-price date from DNB AM or Nordnet.
- **MSCI World constituent weights:** iShares URTH holdings CSV
  (`ishares.com/us/products/239696/ishares-msci-world-etf/latest-holdings.csv`, curl; the
  `1467271812596.ajax` URL returns HTML). There are 1,251 equity rows, with weights summing to
  99.78%, so normalise. **Tickers repeat across countries** (SAP = SAP SE and Saputo; 20
  duplicates on 9 Oct): match on ticker and country, and sum sectors from the CSV rows, not
  from a ticker dictionary.

### Method

1. **Fund facts and position.** Record the NAV and date, cost, currency mix, hedging (stated, or
   inferred from the NOK-return correlation with World in NOK vs in USD, tagged `[E/A]`), size,
   number of holdings, benchmark and record. Take the user's units, value, cost and account type
   from `docs/portfolio-overview.md`.
2. **Look-through.** Use the top holdings covering **≥ 75% of NAV**. The rest is assumed to look
   like the sample `[A]`; say so. Use prices at the last close and Yahoo consensus EPS for CY and
   CY+1, calendarised. Compute the harmonic (earnings-weighted) P/E on CY+1, block by block and
   for the fund.
3. **Blocks.** Group holdings by what drives their earnings, as Step A does for Oslo, and report
   each block's **share of CY+1 earnings** next to its weight.
   - Any block whose P/E is far below the fund's (≤ half) on peak earnings is a **cyclical
     block**. It gets a mid-cycle EPS level, the way Oslo energy gets mid-cycle Brent. Example:
     memory at P/E 3.6 was 5% of DNB Teknologi's weight and 21% of its earnings.
   - Report the fund P/E with and without the cyclical block.
   - Name the evidence for the block's mid-cycle level: sector margins vs their average (FactSet),
     past peak-to-trough, how far consensus has risen. Tag it `[A]`.
4. **Scenarios = the baseline's scenarios** for the fund's market: World for global funds, Oslo
   for Norwegian funds, both weighted for mixed funds. Add a sector mechanism to each scenario
   (e.g. an AI capex cut in the Bear). Never use a separate macro world.
   - **Sector paths come from the sector baseline where one exists.**
     - Map AI-exposed holdings to the layers of `docs/ai-market-bbb.md`: E platforms, H1 compute,
       H2 memory, H3 foundry and equipment, H4 networking and DC infrastructure, T software.
       Copy the layer's EPS path, exit P/E and payout unchanged, and take the AI catalysts and
       signposts for the scenario mechanism.
     - Do the same for energy (oil BBB via the Oslo energy block) and defense
       (`docs/defense-market-bbb.md`).
     - Only blocks no baseline covers keep own `[A]` paths. Show the mapping table.
     - Report each block alone (before cost) against the matching baseline basket. That is the
       selection effect, measured without assuming alpha.
     - Report the sector-only stress: the sector blocks on Bear, the rest and the NOK on Base.
   - EPS per block per year (CY+1 consensus = 1.00) plus a normalised exit year.
   - Year-1 haircut for analyst optimism, larger for the fastest-growing blocks.
   - Exit forward P/E per block on normalised EPS, anchored on the sector's long-run multiple or
     today's level; never the IAF ceiling.
   - **Base and Bull glide** the P/E linearly to exit. **Bear de-rates at the end of Year 1**, as
     the index Bear does.
   - Cash yield = payout per block × EPS (dividends + net buybacks), reinvested inside an
     accumulating fund.
5. **NOK translation.** USD share × the baseline's USD/NOK path; other foreign currency × the
   I-44 path; NOK share flat. A hedged fund or class instead uses the local return + NIBOR − the
   foreign short rate.
6. **Cost and alpha.**
   - Deduct the **all-in cost on the platform where the fund is (or would be) held** from values
     and cash flows every year:
     - **Nordnet "Total pris"** = ongoing charges − rebate + Nordnet's platform fee. The platform
       fee is 0.29% for active equity funds, 0.19% for Nordnet's own index funds, 0.15% for
       external index funds (from 1 Apr 2025), 0.09% for money market and 0.19% for other bond
       funds. Checked on 11 Oct 2026: DNB Teknologi 0.85 + 0.29 = 1.14%; DNB Global Indeks A
       0.10 + 0.15 = 0.25%; Nordnet Global Indeks 0.00 + 0.19 = 0.19%.
     - **DNB:** ongoing charges + DNB's platform fee (0.10% for DNB Global Indeks A in the
       self-select pension account), plus the transaction costs DNB lists.
     - When only the fund's ongoing charges are known, add the platform fee and say so.
     - State which platform the figure is for. The HY fund rows in `docs/hy-funds-analysis.md` are
       before Nordnet's platform fee; keep that basis there.
   - **Manager alpha = 0 in Base** (IAF: no credit for unproven gains). Show as sensitivities:
     alpha = the cost (the manager earns its fee), and alpha = the fund's after-cost record
     against its benchmark (state the period, and the fund size then vs now).
7. **IRR build** as Step C: stub flat (cash accrual less cost, the same in all scenarios), year
   returns, XIRR, **hurdle NAV P_k** at k = 12% and the margin of safety. Show the return split
   (d, g = normalised EPS growth + P/E change + FX − cost, c), the structural run and the share of
   Bull priced.
   - A P/E "re-rating" that only comes from a cyclical block's earnings falling is not a
     re-rating. Say so, and give the P/E without that block now and at exit.
8. **Decision rules.**
   - E = Base IRR after cost − Base NIBOR over the window; R = Base Year 1 − Bear Year 1.
   - E / R vs the HY market reference, the HY book, and **an index fund on the same baseline**
     (World or Oslo after 0.20%).
   - Report the **alpha needed** to match the index fund and to match the HY book's Base.
   - IAF verdict on the margin of safety (clears > +2%, marginal ±2%, fails < −2%); whether
     capital is preserved in Bear.
9. **Triggers.** Solve the NAV change, at unchanged earnings and composition, for: Base = HY book
   Base (pre-alert), E / R = HY market reference, E / R = HY book, Base = k. Give each as %, NAV
   level and look-through P/E (with and without the cyclical block), and compare with the fund's
   NAV over the last 12 months.
10. **Linkage.** From month-end NAVs: volatility; correlation and beta with World NOK, World USD,
    the sector ETF in NOK, OSEBX, Brent and USD/NOK; max drawdown; calendar returns vs World NOK
    and the sector ETF. This states the fund's role in the user's portfolio (e.g. its oil link
    against the ~37% oil exposure of the HY book).
11. **Sensitivities:** cost at index level, alpha (two values), exit P/E ± 1, the cyclical
    block's mid-cycle level, CY+1 consensus −5%.
12. **Tax and account.** In a taxable AF account an equity fund (≥ 80% equities) is taxed like
    shares (37.84% on gains after the skjermingsfradrag). A switch realises the gain; state the
    tax brought forward. Inside ASK or a pension wrapper a switch has no tax effect.

### Index funds (variant of the method)

An index fund is the baseline index held at a cost, so steps 2–3 and 6 change:

- **Look-through = the fund's index**, from the index factsheet (fundamentals, sectors, top 10
  against the parent) and the full holdings of an ETF on the parent index, not from the fund's
  top holdings.
- **Split the baseline index into sector blocks and an implied rest** (first used 12 Oct 2026):
  - **AI blocks:** the AI BBB basket names that are in the index, at index weights, on the AI
    BBB layer paths (EPS, exit P/E, payout; block P/E from the AI BBB's prices and CY+1 EPS).
  - **Energy:** the index's energy weight on the oil path (Oslo energy block formula).
  - **Rest:** implied, so that the blocks plus the rest equal the baseline index path exactly
    (value, earnings and dividends in each year).
  - The split reproduces the baseline at zero cost. Check that, and report:
    - the rest's implied EPS growth, P/E path and payout;
    - each block's return against the matching AI BBB basket;
    - the AI-only stress.
  - If the implied rest needs growth well above trend, show "rest at trend growth" as a check
    and flag it to the next Equity BBB update. Never change the baseline path here.
  - List the names that fit a layer but are not in the AI BBB baskets (the "wider" AI share);
    they stay in the rest.
- **Plain index** (MSCI World, OSEBX): the baseline paths apply unchanged; the split is a
  look-through only.
- **Tilted index** (climate, ESG, factor, equal-weight): the same blocks at the tilted index's own
  weights.
  - Weights: top 10 via the factsheet's index/parent ratios applied to today's parent weights;
    other names from the fund's holdings list, or ×1.0 of the parent with a ×0.7 / ×1.3
    sensitivity. A large parent name missing from the fund's top 25 gets a multiplier below the
    25th weight.
  - Report the active sector and top-10 weights, and what the tilt sells and buys, with the
    earnings-weighted P/E of each side.
  - The tilted index's total P/E (factsheet forward ratio × the baseline's CY+1 P/E), less its
    blocks, gives its rest P/E. The **premium over the parent's rest** is a stated assumption:
    kept in Base and Bull, half lost in Bear. Show "premium halves" and "premium gone" as
    sensitivities, and name what drives the premium (e.g. Tesla). If the ranking between funds
    flips inside them, say the model cannot rank them on return.
  - Lesson from 11 → 12 Oct: growing a tilt "like the index ex energy" hides the AI layers' flat
    post-2027 paths. Put AI weight on the AI paths.
- **Tracking difference replaces alpha.**
  - Measure it from the manager's fund-vs-benchmark table (1/3/5/10 years) and from NAVs against
    the index. For a tilted index, compare with a plain-index fund and take out the index gap.
  - Base takes tracking beyond cost as 0. Show a drag sensitivity when the record or the
    structure (swap spread) suggests one.
- **Structure and index stability:**
  - Record physical vs synthetic replication, the swap counterparty and the UCITS 10% exposure
    cap, the domicile and base currency.
  - Record the index history: a fund that has changed index is a different exposure from its
    record.
  - For AF use, check the tax equity share of a synthetic fund, which depends on the substitute
    basket.
- **Decision rules and triggers** as steps 8–9, plus the baseline's own triggers translated into
  each fund's NAV (e.g. the World trigger as a DNB Global Indeks NAV).
- **Recommendation between funds:** cost per year in NOK on the planned amount; the model gap and
  whether it survives the premium sensitivity; Bear and side-case gaps; the size of the tilt at
  portfolio level (NOK of energy and tech moved); structure; and which fund the account can hold.

### Output: `docs/<fund>-analysis.md`

IAF document order adapted to a fund: title · skill revisions and inputs · **Summary** (verdict,
decision table: IRR, Year-1 return, NAV equivalent at exit, hurdle NAV and margin of safety,
capital preserved, position value per scenario, Year-1 stress in NOK, E / R; per-year path with
EPS, forward P/E, return and NAV equivalent) · tags · Header (fund facts, cost, currency and
hedging, position, track, k) · Scenario definitions (baseline anchor + sector mechanism; side
case) · Fund and status (holdings, sectors, record) · Near term · Market input · Look-through
valuation (blocks, references, data handling) · Common assumptions · Period table and year-end
path · Return split, structural run and sensitivities · Results · Against high yield and an index
fund (E / R table, triggers, tax) · Verdict and caveat · Risks and signposts · For other modules ·
Change log · Appendix: own assumptions · Appendix: sources (incl. raw consensus per holding and
validation notes).

- Update the fund's row in `docs/portfolio-overview.md` when the user holds the fund.
- A fund analysis is stale when the baseline is updated, after the fund's next monthly report
  shows a block weight change > 3 pp, or after a NAV move of more than 10%.

## Recalibration triggers

- OSEBX or MSCI World moves more than 10% within a month, or crosses a trigger level
- The oil or HY baseline is updated with a change that reaches Oslo earnings or NIBOR
- Consensus CY+1 EPS for Oslo or the S&P 500 is revised by more than 5% since the last run
- MSCI World forward P/E leaves 15.5–19.5, or MSCI Norway P/BV leaves 1.9–2.6
- USD/NOK moves more than 7% within a month
- A Bear or Bull signpost is crossed; the baseline is older than 30 days

## Output: `docs/equity-market-bbb.md`

```markdown
# Equity Market BBB — [baseline date]

## Metadata
- Analysis date, status, skill revision; upstream baselines (date, revision, status, stale after)
- Window, stale after; series used; FX; tags

## Conclusion
- Changed / kept unchanged — explicit
- Base in two sentences per index; main Bear and Bull catalysts; the trigger levels

## Interface — index returns (NOK total return, before fees, %)
| Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Window (ann.) | Mid-cycle |
| Oslo (OSEBX) | World (MSCI World, NOK unhedged) | World (USD, local) |

## Interface — earnings, valuation and NOK paths
| Index EPS (CY+1 consensus = 100) per scenario per year + normalised exit year |
| Forward P/E at each year-end per scenario |
| I-44 and USD/NOK year-end per scenario (Base = Norges Bank MPR I-44) |

## Interface — hurdles and triggers
| Index | Level / date | Base IRR | P_k (k = 12%) and MoS | E | R | E / R vs HY ref | Trigger levels |

## Scenario definitions
## Valuation snapshot (Oslo; World; yield gaps; historical anchors)
## Oil and NOK linkage (correlations, rolling, episodes, energy earnings share, Brent sensitivity)
## Oslo build (blocks, B_cons, paths, P/E, payout)
## World build
## Return split, structural run and sensitivities
## Against high yield (decision rules, tax, pension horizon)
## Signposts and monitoring
## For other modules
## Change log
## Appendix: raw values and sources
```

## Interface to other skills and documents

- **Portfolio discussion** (`docs/portfolio-overview.md`): the Interface tables and the trigger
  levels are the equity side of the HY-versus-equity question. This baseline does not set the
  allocation; it states what each index pays per unit of the same stress as HY.
- **[[iaf-valuation]]:** the Oslo and World Base IRR is market context for k. A market priced below
  k does not lower k; it means few single stocks will clear it. Company analyses may cite the
  index hurdle and the energy share as context.
- **[[hy-market-bbb]]:** the equity Bear uses the same catalysts; the equity Bear 2027 drawdown is a
  cross-check of the HY Bear's spread path. No HY input is set here.
- **NOK path:** the scenario NOK path (I-44 and USD/NOK) is set only here, with Base anchored on
  Norges Bank's MPR. IAF keeps spot FX at the valuation date for company figures.

## Checks before finishing

- Skill revision and upstream revisions stated; window and stub right for today's date.
- Upstream Brent, NIBOR, GDP and HY figures copied from the current documents, not re-forecast.
- Every fetched value has source, as-of date, unit and currency; inverted ETF ratios and USD-EPS /
  NOK-price mismatches handled; raw values in the appendix.
- Earnings base is CY+1 consensus; block shares are earnings shares; B_cons stated.
- Stub identical across scenarios; V_T on normalised earnings and mid-cycle P/E; g is the value
  CAGR; c shown; structural run shown.
- E, R and E / R computed with the HY definitions; trigger levels given as level, % and multiple.
- Bear and Bull tied to named catalysts with signposts; the oil side case shown; no probability
  language.
- Correlation tables built from daily → month-end data; windows and dates stated.
- Change log complete or explicit "kept unchanged". File written, read back, tables render.
- **Fund mode:** top holdings ≥ 75% of NAV, with each one's consensus validated (currency, fiscal
  year, one-offs, analyst count); block earnings shares shown, and the P/E shown with and without
  any cyclical block; scenarios and NOK paths taken from the current baseline; all-in cost for
  the named platform deducted; alpha 0 in Base, with the record as a sensitivity; E / R against
  the HY references and an index fund; hurdle NAV and triggers as NAV levels; tax on a switch
  stated; portfolio row updated.
- **Index funds:** index identified from the KID and matched to the factsheet; index history
  stated; active weights and the P/E premium of any tilt shown, with premium sensitivities;
  tracking difference measured; replication and counterparty stated; the model reproduces the
  baseline at zero cost.
