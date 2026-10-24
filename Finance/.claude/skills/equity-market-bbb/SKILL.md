---
name: equity-market-bbb
description: Equity Market BBB — the equity index baseline for Oslo (OSEBX) and global equities (MSCI World, in NOK unhedged and in USD). Applies the IAF method at index level (d + g + re-rating, a year-by-year IRR build, the hurdle level at k = 12%) and produces Bear/Base/Bull index total-return paths on the IAF time grid (stub of the current year + 3 calendar years, now 2027–2029), index EPS and P/E paths, the NOK scenario path, mid-cycle returns, the oil and NOK linkage (correlations, betas, the energy share of Oslo earnings), and equity triggers that mirror the HY trigger (E / R against the Nordic HY market reference, Base IRR against k and against the HY market's Base return). Oslo energy earnings follow the Brent path in docs/oil-market-bbb.md; NIBOR, Nordic GDP and the HY return come from docs/hy-market-bbb.md. Base is the decision case; Bear and Bull are catalyst-based stress tests; 25/50/25 is a labelled convention, never a probability. ALWAYS use when the user mentions Equity BBB / Equity Market BBB / aksjemarked, asks to create, run or update ("oppdater modul") the equity module, or asks about the Oslo Børs or OSEBX outlook, Oslo valuation (P/E, P/B), global equity or MSCI World expected returns, equities versus high yield, when to move from HY to equities, the oil–Oslo or oil–NOK correlation, or how Oslo compares with global equities — even without naming the skill. It estimates markets only: it never analyses a named fund, a portfolio or a single paper. It is the only place an equity index return path, an index hurdle or a NOK scenario path is set.
---

# Equity Market BBB

**Revision:** 2026-10-24.1 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/equity-market-bbb/` in the Finance folder.

An index-level baseline for Oslo and global equities. It answers one question: **what total
return can an index investor in NOK expect, year by year, from today's price, and at what index
level do equities beat the Nordic high-yield alternative on the same risk rule?** It is a
testable hypothesis with explicit risks, not a market commentary and not a price target.

Place in the chain:

- Reads `docs/oil-market-bbb.md` (Brent path and mid-cycle → Oslo energy earnings) and
  `docs/hy-market-bbb.md` (NIBOR path, Nordic GDP, HY spreads and defaults → Oslo financials and
  the Bear macro; Nordic HY expected return, the decision rule and the market reference E / R →
  the comparison). It never reads the HY fund analysis (`docs/hy-funds-analysis.md`). Defense and
  sector baselines are context only.
- Never makes its own oil, rate, GDP or credit forecast. If an upstream baseline is stale, this
  baseline is provisional.
- Gives [[iaf-valuation]] the market context for k. It never lowers k.
- **Market only.** The output is an estimate of the market. The skill never analyses a named
  fund (active, sector or index) or a single paper, and never reads or writes
  `docs/portfolio-overview.md`. It holds no portfolio figures (positions, HY book, account types,
  horizons). The HY comparison is with the Nordic HY market.

**Scope:** broad equity indices: Oslo (OSEBX), global developed (MSCI World; ACWI as
cross-check), and the NOK translation.

**Out of scope:** single stocks (→ [[iaf-valuation]]), named funds of any kind, portfolios,
sector forecasts (→ the sector BBBs), and bonds (→ [[hy-market-bbb]]). Company analyses and the
AI BBB enter only as building blocks of World's index earnings: the skill reads them and never
makes them. ETFs (OBXD, URTH, NORW, IXC) are used only as data proxies for their index.

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
  earnings. Only the P/E form is drift-free: at a fixed level the P/B falls as book grows by
  retention (~0.5% a month for Oslo).
- Never mix price and total-return series in one comparison, or USD and NOK returns.
- **Name the index behind every multiple.** Oslo has three: OSEBX (price), OBX top names (earnings
  model) and MSCI Norway (12 names; multiples). Give the bottom-up figure on the model's weights
  next to MSCI's. Historical anchors are often on yet another index (the P/B band below is OSEBX).

## Data sources

| Need | First choice | Fallback / cross-check |
|---|---|---|
| Index levels, ETF prices, FX, Brent (daily → month-end) | **Yahoo** chart API via Python (`query1.finance.yahoo.com/v8/finance/chart/<sym>?interval=1d`, User-Agent header); MCP `get_chart` for a few points | EODHD EOD prices |
| Constituent prices, market caps, forward P/E, dividend yield | **Yahoo** quote API via Python with cookie + crumb (`fc.yahoo.com` → `/v1/test/getcrumb` → `/v7/finance/quote?symbols=…&crumb=`); MCP `get_quote` (verbose) | Nordnet (read-only, Edge) |
| Consensus EPS CY / CY+1 per constituent, number of analysts | **Yahoo** `/v10/finance/quoteSummary/<sym>?modules=earningsTrend,earnings` (crumb) | Zacks for US listings and ADRs |
| ETF look-through: sector weights, top holdings, P/E, P/B | Yahoo quoteSummary `topHoldings` (OBXD.OL = DNB OBX ETF, NORW/ENOR = MSCI Norway, URTH, ACWI, SPY) | Issuer factsheets |
| Index fundamentals (P/E, fwd P/E, P/BV, yield) and top weights | **MSCI index pages** (`msci.com/indexes/index/957800` Norway, `990100` World) via WebFetch | MSCI factsheet PDFs |
| MSCI World constituent weights (World blocks) | **iShares URTH holdings CSV** (`ishares.com/us/products/239696/ishares-msci-world-etf/latest-holdings.csv`, curl; the `1467271812596.ajax` URL returns HTML) → `references/dl2/urth_ai.json` | MSCI top 10 |
| Index factsheets (fundamentals, sectors, top 10, net returns) | MSCI factsheet PDF (`msci.com/documents/10199/255599/<index-name>-usd-net.pdf`, curl, text with `pypdf` under `py -I`) | MSCI index pages |
| Bottom-up P/B, ROE, dividend yield and payout of the Oslo sample | **Yahoo** quoteSummary (`price`, `summaryDetail`, `defaultKeyStatistics`, `financialData`; `references/valq.py`), aggregated with `references/valagg.py` | MSCI Norway (index level) |
| Oslo P/B history | Nordnet blog "Hva er pris/bok på Oslo Børs" (4 Apr 2023; OSEBX, 67 names, Bloomberg, 13 years): 1.5 cheap, 2.1 expensive; 2.4–2.7 has often been followed by losses `[E]` | MSCI Norway factsheets (month-end P/BV, few points) |
| US earnings path and valuation | **FactSet Earnings Insight** PDF (weekly; WebFetch saves the PDF, read with `pypdf` under `py -I`) | Yardeni, press |
| NIBOR path, Nordic GDP, HY spreads, HY expected return | **`docs/hy-market-bbb.md`** | — never an own path |
| HY decision rule, market reference E / R, market stress loss R | **`docs/hy-market-bbb.md`** ("For other modules") | — never a fund document |
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
  fraction and is often wrong for USD reporters. Use `dividendYield`. In quoteSummary
  `summaryDetail.dividendYield` is a fraction. Both are the **latest declared dividend
  annualised**, not a forecast: one strong quarter of a variable payer (Frontline 19.9%, 16 Oct)
  shows as a yearly yield.
- Yahoo `bookValue` for NOK-listed USD reporters is usually converted to NOK, but not always: Vår
  Energi's is in USD, so its `priceToBook` reads 63.8 for a true 6.8 (16 Oct 2026). Check
  P/B = price ÷ (BVPS × FX) for every USD reporter.
- MSCI index pages give fundamentals at the last month-end and the top-10 weights; sector weights
  did not render. MSCI Norway has only 12 constituents: use it for valuation, not for weights
  below the top 10.
- No free source gives a long series of Oslo forward P/E or P/B. Historical anchors are secondary
  (`[E]`); state them as such.
- **URTH holdings CSV:** 1,251 equity rows with weights summing to 99.78% (9 Oct 2026), so
  normalise. Tickers repeat across countries (SAP = SAP SE and Saputo; 20 duplicates): match on
  ticker and country, and sum sectors from the CSV rows, not from a ticker dictionary.
- MSCI World's own factsheet shows **gross** annual returns; a renamed index can sit behind a
  plain-named URL (check the launch date and top 10).
- **Consensus EPS checks** (Oslo constituents and World block names):
  - Some Oslo-listed USD reporters have Yahoo EPS in NOK (Nordic Semiconductor); check against
    the quote's forward P/E.
  - Large one-off gains distort CY EPS (Alphabet and Amazon 2026): value on CY+1 and leave the
    distorted year out of growth.
  - Thin or inconsistent +1y estimates (few analysts): use the quote's forward P/E.
  - Fiscal years: blend June/July year-ends half and half into calendar years; map Jan–Mar
    year-ends to the calendar year they mostly cover and Sep–Oct year-ends to the same year.

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
- **Dividend and cash yields carry a label.** Report three rows, the same for Oslo and World:
  - **trailing:** dividends paid over 12 months (MSCI);
  - **forward:** the latest declared dividend annualised (Yahoo). Show it with and without
    names that pay more than 100% of trailing EPS or yield more than twice their block's average;
  - **model cash yield:** dividends plus net buybacks plus retained cash credited (Step C).
    Source the buybacks, or count none and say so.
- **P/B anchors:**
  - Name the index and the period of every historical P/B anchor.
  - Add a composition note: the names that add most to the index P/B against the anchor years
    (16 Oct 2026: Kongsberg at P/B 22.5 added ~0.19 to the Oslo sample's 2.36).
  - Record the source's loss zone (P/B 2.4–2.7) next to the band.
- **ROE carries its basis:** trailing (P/B ÷ trailing P/E) or forward (P/B ÷ forward P/E). A
  "normal" ROE built from a point P/B and an average P/E is a rule of thumb `[E/A]`, not an anchor.

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
  - Cash: payout per block (below) and cash conversion 0.80, as in Step C and as World energy.
    (The cash conversion is not the break-even c above.)
- **F block:** relative to consensus, from the NIBOR path (net interest margin) and the HY default
  path (credit losses). Bear peaks losses in the HY Bear default peak year.
- **O block:** consensus less a haircut for analyst optimism in Year 1 `[A]`, then nominal growth
  (GDP + inflation); Bear from the HY Bear GDP path.
- **Payout per block:** the latest declared dividend annualised ÷ trailing EPS from the bottom-up
  sample `[F]`.
  - Show it also without names flagged under the yield rule, and on dividends actually paid
    (Yahoo payout ratio).
  - 16 Oct 2026: E 0.76 (0.65 without Frontline's peak quarter), F 0.63, O 0.56; 0.66 weighted on
    CY+1 earnings shares. On dividends paid: 0.61 / 0.63 / 0.54.
  - Buybacks are counted only where a source gives them; energy's go through the cash
    conversion.
- **Normalised exit-year EPS** (the year after exit): energy at the scenario's **mid-cycle Brent**,
  F at mid-cycle NIBOR, O on trend. This is the V_T basis (IAF Step 3: normalised, never the last
  modelled year by default).

### Step B — World: index earnings, built from blocks (AI split; since 17 Oct 2026)

- **Earnings base = consensus CY+1 EPS = 100**, anchored on FactSet's S&P 500 CY+1 growth and the
  MSCI World trailing/forward P/E ratio (World P/E on CY+1).
- **World = company blocks + AI layer blocks + energy + rest.** The World path is the sum of the
  blocks; it is never set top-down and then backed into a rest.
  - **Company blocks:** names with their own IAF analysis (now Microsoft, Alphabet, NVIDIA) at
    index weights, with that analysis's per-share EPS, D_t and V_t per scenario.
  - **AI layer blocks:** the other AI BBB basket names in the index, at index weights, on the
    layer paths of `docs/ai-market-bbb.md` (EPS, exit P/E, payout, cash conversion c; block P/E
    from today's prices and calendarised CY+1 EPS). AI earnings paths are set only there.
  - **Energy:** the index's energy weight on the oil path (Oslo energy formula, Brent − 30), P/E
    from IXC; payout and cash conversion as Oslo energy (0.76 and 0.80; Step C).
  - **Rest** (≈ 70% of earnings): its own explicit EPS path per scenario `[A]`: Base = Year-1
    haircut on consensus (state it, now 3%), then trend nominal growth (now 5.5%); Bear and Bull
    from the [[hy-market-bbb]] recession / soft-landing catalysts. Rest P/E and payout paths
    are stated per scenario (the World multiple view without its AI and energy part).
  - Report: block weights (value and earnings), the World EPS path that results, each block's
    contribution, and the sensitivity to rest growth (± 1 pp) and to all multiples (± 10% and ± 1).
- **Retained cash:** the one rule in Step C, for World and Oslo alike.
- Scripts: `references/idxai3.py` (blocks, company and layer paths; weights in
  `references/dl2/urth_ai.json`), `references/upd.py` (World from blocks and rest) and
  `references/osl.py` (Oslo).
- Bear and Bull take the global recession / soft-landing paths that match [[hy-market-bbb]].
- **Currency:** the NOK path is set in **I-44** terms. USD earnings move with USD/NOK, other
  foreign earnings with I-44:
  - World: 70% on USD/NOK, 30% on I-44 `[A]` (the USD share of MSCI World).
  - Oslo: the energy block on USD/NOK; the foreign half of the O block on I-44; F in NOK.
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
D_t               = payout × EPS_t                      cash paid (dividends + sourced net buybacks), mid-year
V_t, V_T          + Σ (cash conversion − payout) × EPS   retained cash credited at face value (blocks with a cash conversion)
Stub              = price flat, D = cash yield × stub length (same in all scenarios)
IRR_T solves      P = Σ D_t/(1+IRR)^t + V_T/(1+IRR)^T   (XIRR on dates; T = stub + 3)
Hurdle level      P_k = Σ D_t/(1+k)^t + V_T/(1+k)^T     k = 12%;  margin of safety P_k / P − 1
Annual return r_t = (D_t + V_t − V_(t−1)) / V_(t−1)     V_stub-end = P
```

- **Exit principle (shared with [[iaf-valuation]] Step 3):** V_T is the price a market buyer pays at
  exit for a continuing index, on normalised earnings of the year after exit, at the market's
  required return at exit (the mid-cycle P/E), never at k and never at the IAF ceiling. The same
  rule sets V_T in every company analysis, so index and company exits are comparable.
- **Exit consistency per block (as IAF Step 3):** for each block and scenario,
  gap = (EPS multiplier in the exit year ÷ normalised multiplier of the year after exit) − 1.
  - Material = |gap| > 10%. Then either a **named reason** from the upstream baseline (oil BBB,
    HY BBB, AI BBB) that brings the block to its normalised level within about a year of exit, or
    a **reversion tail**: add to V_T the block's gap × EPS × payout-adjusted cash conversion,
    fading 2/3 then 1/3 over 2 years after exit, discounted at the mid-cycle return.
  - Blocks valued as P/E × EPS on trend (Oslo O, World rest) have no gap by construction; say so.
    Company and AI-layer blocks carry the test from their own documents.
  - Show one table: block, scenario, exit-year multiplier, normalised multiplier, gap, treatment.
- **P/E paths are forward 12-month P/E at each year-end.** The exit P/E is the scenario's
  **mid-cycle P/E**, anchored on long-run averages of forward P/E (state source and period) and
  cross-checked with P/B against ROE (P/B ÷ P/E = implied ROE). Never use k's ceiling as the exit
  multiple.
- **Return split (every scenario, both indices, as numbers):** d = (ΣD/T)/P; g = (V_T/P)^(1/T) − 1,
  split into normalised EPS growth (from CY+1 consensus), re-rating (value multiple at exit ÷ P/E
  now), retained cash, and FX for World in NOK; c = IRR − d − g. Never set g = IRR − d.
  - World's value multiple is V_t ÷ EPS_(t+1) of the block sum (retained cash included).
  - A rise that comes only from a cyclical block's EPS falling (memory) is not a re-rating; say so.
- **Structural run (Oslo):** EPS at the normalised level from Year 1; cyclical = IRR − structural.
  World is exempt: its blocks carry their own cyclical paths and the sum has no single normalised
  level.
- **Retained cash and payout: one rule for both indices** (counted once):
  - A block with a **cash conversion** (free cash after growth capex and dilution ÷ EPS) credits
    (conversion − payout) × EPS to V_t at face value and gets no extra growth for it. These are
    the company analyses, the AI layers, and energy in both indices (conversion 0.80 `[A]`: no
    growth to fund, sustaining capex a little above D&A).
  - A block valued as P/E × EPS (Oslo F and O, World rest) uses its retention to fund its own
    EPS growth.
  - Never credit a block's retained cash and grow its EPS from the same cash.
  - Energy has the same payout in both indices: Oslo's bottom-up figure.
- **Payout consistency, both directions:**
  - Growth must not need more than ROE × retention. If it does, cut growth or payout.
  - If ROE × retention is well above the assumed growth, state the implied return on retained
    earnings (growth ÷ retention) and the reason (dilution, field decline, low-return
    reinvestment). 18 Oct 2026: Oslo 3.4% ÷ 0.34 ≈ 10%, World 5.3% ÷ 0.51 ≈ 10%, both below k.
- **P/B–ROE check (both indices, every run):** one table with P/B now, ROE trailing and forward,
  the ROE path, normalised ROE and **exit P/B**, set against the history.
  - book_T = book_now + Σ (EPS_t − D_t), with the retained cash credit staying in book.
  - Exit P/B = V_T ÷ book_T; normalised ROE = EPS_(T+1) ÷ book_T.
  - An exit P/B outside the history band needs a stated reason, or the exit P/E is wrong.

### Step D — Mid-cycle return

Long-run expected annual return at mid-cycle earnings and P/E, no re-rating:
`cash yield (cash conversion ÷ mid-cycle P/E) + long-run nominal EPS growth`. Used for horizons
beyond the window and as the equity risk premium check against mid-cycle NIBOR.

- **Show the inputs per index and scenario** in a table: cash conversion (payout plus retained
  cash credited), mid-cycle P/E, cash yield, long-run growth and the total.
- **Long-run growth (Base) = the index's Base trend growth `[A]`:**
  - World: the rest's trend for all non-energy blocks, energy at 2% (inflation, flat volumes).
  - Oslo: block trends weighted on normalised earnings shares (energy 2%, F at nominal mainland
    GDP ~3.5%, O at its trend).
- Bear −1.5 pp, Bull +0.75 pp on long-run growth `[A]`.
- Show the implied return on retained earnings (Step C).

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
  (Year-1 stress loss). Same definitions as in [[hy-market-bbb]].
- **Attractive vs HY:** E / R ≥ the **HY market reference** (now 0.196, from
  `docs/hy-market-bbb.md`).
- **IAF test:** Base IRR vs k = 12% and the margin of safety P_k / P − 1 (clears > +2%, marginal
  ±2%, fails < −2%).
- **Triggers:** solve for the index level (price change at unchanged earnings) where
  (1) E / R = HY market reference, (2) Base IRR = k, (3) pre-alert: Base IRR = the HY market's
  Base window return (before fees, from `docs/hy-market-bbb.md`, the same basis as the equity
  Base). Report each as % from today, as the index level, and as the multiple at
  unchanged earnings (Oslo forward P/E and P/B; World forward P/E). Every row gets every column.
  - **Multiples at the triggers:** scale the MSCI month-end multiple by the index move **since
    that month-end** (OSEBX for Oslo; URTH in USD for World), never by the move since the
    previous run. Then apply the trigger's price change.
- **Long horizons:** R is a one-year stress. For horizons beyond the window also show the Bear
  window return and the mid-cycle return against HY's mid-cycle return. The allocation is not
  set here.
- **Tax note** (general, taxable accounts): equity net ≈ e − 0.3784 × (e − skjermingsrente) vs
  HY × (1 − 0.22). Tax never changes the market baseline.

## Procedure

Two modes: **Initiate** (no `docs/equity-market-bbb.md`) and **Update** ("update Equity BBB",
"oppdater modul" in an equity context, or a recalibration trigger). A request to analyse a named
fund or a single paper is not this skill's work: say so. Run every step; actively try
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
tech share). Then the block split (Step B): index weights of the company and AI names (URTH
holdings), their prices and calendarised CY+1 EPS, the energy weight, and the rest by difference.

**Step 4 — Linkage.** Step E above; compare with the previous run.

**Step 5 — Paths.** EPS (Steps A, B), P/E paths, NOK path, payout and cash conversion, per
scenario. Run the model: annual returns, window IRR, P_k, structural run (Oslo), return split, P/B–ROE
check (Step C).

Sensitivities, the same set for both indices (Base window):
- **All multiples ±10%** (values × 0.9 / 1.1), plus ±1 point.
- **NOK ±10% by the end of the window**, linear, on USD/NOK and I-44 alike.
- **Brent ±$10** on every year and mid-cycle (Oslo, and World energy).
- World only: rest growth ±1 pp.
- For the Oslo trigger, give the Brent ±$10 move two ways: Base and Bull paths only (R changes),
  and all scenarios including Bear (R unchanged).

**Step 6 — Test BBB.** What would make Base wrong (earnings revisions, P/E regime, oil and NIBOR
paths), and is it visible? Are the catalysts still right? Has a signpost been crossed?

**Step 7 — Decision rules and triggers.** E, R, E / R vs the HY references; trigger levels.

**Step 8 — Write, log and check.** Write the document in the output format; full change log
(previous → new with reason); read it back; run the checks.

## Recalibration triggers

- OSEBX or MSCI World moves more than 10% within a month, or crosses a trigger level
- The oil or HY baseline is updated with a change that reaches Oslo earnings or NIBOR
- Consensus CY+1 EPS for Oslo or the S&P 500 is revised by more than 5% since the last run
- MSCI World forward P/E leaves 15.5–19.5, or MSCI Norway P/BV leaves 1.9–2.5. Above 2.5 is a
  **valuation warning**, not a Bull sign: the P/B source's loss zone starts at 2.4. A rising P/B
  supports Bull only if earnings rise with it.
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
| Forward P/E at each year-end per scenario: Oslo index; World total value multiple (V_t ÷ EPS_t+1) and the rest |
| I-44 and USD/NOK year-end per scenario (Base = Norges Bank MPR I-44) |
| Mid-cycle inputs per index and scenario (cash conversion, P/E, cash yield, growth) |
| Exit reference per index and scenario: exit P/E, exit P/B, mid-cycle return (read by IAF's exit cross-check) |
| Exit consistency per block and scenario (exit-year vs normalised multiplier, gap, treatment) |

## Interface — hurdles and triggers
| Index | Level / date | Base IRR | P_k (k = 12%) and MoS | E | R | E / R vs HY ref | Trigger levels (%, level, P/E; Oslo also P/B) |

## Scenario definitions
## Valuation snapshot (Oslo; World; same rows for both: P/E, P/B, ROE with basis, three yield rows; yield gaps; historical anchors with index and composition note)
## Oil and NOK linkage (correlations, rolling, episodes, energy earnings share, Brent sensitivity)
## Oslo build (blocks, B_cons, paths, P/E, payout per block, cash conversion)
## World build (blocks: company, AI layers, energy, rest; weights, P/E, EPS paths; currency mix)
## Return split, structural run, P/B–ROE check and sensitivities (same table layout for both indices)
## Against high yield (decision rules, tax, long horizon)
## Signposts and monitoring
## For other modules
## Change log
## Appendix: raw values and sources
```

## Interface to other skills and documents

- **Portfolio and named funds:** none. The baseline states what each index pays per unit of the
  same stress as the HY market. It does not read, write or flag `docs/portfolio-overview.md` or
  any fund analysis; those may read the Interface tables on their own.
- **[[iaf-valuation]]:** the Oslo and World Base IRR is market context for k. A market priced below
  k does not lower k; it means few single stocks will clear it. Company analyses may cite the
  index hurdle and the energy share as context.
- **[[hy-market-bbb]]:** the equity Bear uses the same catalysts; the equity Bear 2027 drawdown is a
  cross-check of the HY Bear's spread path. No HY input is set here.
- **NOK path:** the scenario NOK path (I-44 and USD/NOK) is set only here, with Base anchored on
  Norges Bank's MPR. IAF decides at spot FX and reports Bear and Bull in NOK on this path for
  foreign-currency cash flows (IAF FX rule).
- **Exit cross-check:** company analyses set their exit P/E, exit P/B and buyer's implied return
  beside this baseline's index exit P/E, exit P/B and mid-cycle return (Interface tables). Keep
  those three figures per index and scenario in the Interface.

## Checks before finishing

- Skill revision and upstream revisions stated; window and stub right for today's date.
- Upstream Brent, NIBOR, GDP and HY figures copied from the current documents, not re-forecast.
- Every fetched value has source, as-of date, unit and currency; inverted ETF ratios and USD-EPS /
  NOK-price mismatches handled; raw values in the appendix.
- Earnings base is CY+1 consensus; block shares are earnings shares; B_cons stated.
- World EPS path is the sum of its blocks (Step B); the rest path is explicit and its growth
  stated; AI paths read from `docs/ai-market-bbb.md`, not set here.
- One retained-cash and payout rule for both indices (Step C); energy has the same payout and cash
  conversion in Oslo and World; currency on USD/NOK for USD earnings, I-44 for the rest.
- Exit-consistency table per block and scenario (gap > 10%: named reason or 2-year tail).
- Stub identical across scenarios; V_T on normalised earnings and mid-cycle P/E; g is the value
  CAGR and split into numbers for both indices; c shown; structural run shown (Oslo).
- P/B–ROE table for both indices with exit P/B; ROE basis stated; yields in three labelled rows;
  P/B anchor index named, with the composition note and the loss zone.
- Sensitivities like for like (multiples ±10%, NOK ±10%, Brent ±$10); the Brent trigger move
  given both ways; trigger multiples scaled from the month-end.
- Mid-cycle inputs shown; the implied return on retained earnings stated.
- E, R and E / R computed with the HY definitions; trigger levels given as level, % and multiple.
- Bear and Bull tied to named catalysts with signposts; the oil side case shown; no probability
  language.
- Correlation tables built from daily → month-end data; windows and dates stated.
- Change log complete or explicit "kept unchanged". File written, read back, tables render.
