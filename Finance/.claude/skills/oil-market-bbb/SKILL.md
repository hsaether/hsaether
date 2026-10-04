---
name: oil-market-bbb
description: Oil Market BBB — the price baseline for crude oil and distillates at the top of the analysis chain. Produces Bear/Base/Bull price paths for Brent and distillate cracks (diesel/ULSD, jet) on the IAF time grid (stub quarter(s) of the current year + 3 calendar years, now 2027–2029), plus mid-cycle prices for terminal values, the forward curve, the supply/demand/inventory balance and named catalysts with signposts. Base is the decision case; Bear and Bull are catalyst-based stress tests; 25/50/25 is a labelled convention, never a probability. Covers prices and their physical drivers only — no shipping (rates, tonnage, ton-mile, routes) and no rigs. ALWAYS use when the user mentions Oil Market BBB / oil BBB, asks to create, run or update ("oppdater modul") the oil module, or asks about the Brent outlook, oil price scenarios, diesel or jet cracks, distillate prices, the oil forward curve or oil inventories — even without naming the skill. Feeds oil-shipping-bbb, rig-market-bbb, supply-market-bbb and iaf-valuation; it is the only place an oil price forecast is made.
---

# Oil Market BBB

**Revision:** 2026-10-04.6 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/oil-market-bbb/` in the Finance folder.

A Bear/Base/Bull price baseline for crude oil and distillates. It answers one question: **what
Brent and distillate prices should the downstream analyses use, year by year, and what named
events would move them?** It is a testable hypothesis with explicit risks, not a news summary.

This skill is the top of the chain. [[oil-shipping-bbb]], [[rig-market-bbb]],
[[supply-market-bbb]] and [[iaf-valuation]] read `docs/oil-market-bbb.md` and never make their own oil forecast, so the
output must keep the fixed interface defined under Output.

**Scope:** crude and distillate prices and the physical drivers behind them (supply, demand,
inventories, refining, disruptions measured in barrels). **Out of scope:** freight rates, vessels,
tonnage, ton-mile, sailing routes and transit days (→ [[oil-shipping-bbb]]); rigs and E&P capex
(→ [[rig-market-bbb]]); company figures (→ [[iaf-valuation]]); gasoline and other non-distillate
products.

## Standing parameters

- **Time grid = IAF grid:** stub (remaining quarters of the current year) + 3 full calendar years,
  now Q4 2026 + 2027–2029. Roll forward with the first run each January: the first year becomes
  "realised" (used for forecast vs actual) and a new end year is added. Rolling is not a reset —
  overlapping years are carried over and tested.
- **Price basis:** nominal USD, average over the period, **front-month futures basis** (see
  Benchmarks). Today's spot or a crisis peak is never used as a multi-year assumption.
- **Point value + range** for every scenario price. Downstream skills and IAF use the point value;
  the range shows uncertainty inside the scenario.
- **Base = the decision case.** Bear and Bull are stress tests tied to named catalysts.
  **25/50/25** is a labelled convention for optional weighted figures — never a probability.
- **Stub has no scenario spread** (IAF rule): the stub price is actuals for elapsed days plus the
  forward curve for the rest, the same in all three scenarios. Scenarios diverge from Year 1.
- **Minimum change (convention):** a point value moves only if the evidence moves it by at least
  USD 3/bbl (Brent or crack, annual average). Smaller moves are noted, not applied.
- **Staleness:** the baseline is stale after 30 days, or earlier if a recalibration trigger fires.
  Downstream skills treat a stale baseline as provisional.
- Benchmarks below are fixed. Changing a series is a method change and goes in the change log.

## Files

- Skill: `.claude/skills/oil-market-bbb/SKILL.md` (this file only, no reference files).
- Output: `docs/oil-market-bbb.md`, one running baseline. Baseline date in the H1. Git holds the
  history, so the previous version is read from the file before it is overwritten.
- Write with Write/Edit, then **read the file back** and check every table and number. An answer
  in the conversation alone is not delivery.

## Benchmarks and units

| Series | Definition | Unit | Role |
|---|---|---|---|
| Brent | ICE Brent front-month futures (read as NYMEX BZ, which settles on ICE Brent) | $/bbl | BBB price |
| Diesel crack | NYMEX ULSD front (HO, $/gal × 42) − Brent front, same calendar month | $/bbl | BBB crack |
| Diesel price | Brent + diesel crack; also in $/t (× 7.45 bbl/t) | $/bbl, $/t | Derived |
| Jet crack | NWE jet CIF − Brent (press/agency data) | $/bbl | BBB crack, lower confidence |
| Brent–WTI | Brent front − NYMEX WTI front, same calendar month | $/bbl | For US-priced producers |
| Gasoil crack (Europe) | ICE low-sulphur gasoil ($/t ÷ 7.45) − Brent | $/bbl | Cross-check only |
| Brent curve signal | M1 − M4 (front vs fourth contract) | $/bbl | Tightness signal |
| Long end | Brent December contract for each year in the window | $/bbl | Market's view of the path |
| Dated–futures spread | Dated Brent − front-month futures | $/bbl | Physical tightness signal |

- **Front-month mapping (forward periods):** the front contract in calendar month m is Brent
  m+2 and ULSD/WTI m+1 (Brent expires about two months before delivery, ULSD and WTI about one).
  The forward value of a period is the average over its calendar months of those contracts, e.g.
  Q1-27: Brent H27/J27/K27, ULSD and WTI G27/H27/J27. The crack for month m is HO(m+1) × 42 −
  BZ(m+2). For a whole year, the four mid-quarter months (Feb, May, Aug, Nov) are an acceptable
  shortcut; say so when it is used.
- **Why ULSD − Brent for diesel:** it is the only distillate crack with a full, fetchable forward
  curve (contracts to end-2029 on Yahoo), so actuals, forwards and scenarios are on one basis.
  The European gasoil crack is the reference for European import pricing and is tracked as a
  cross-check from press data; report the gap between the two when both are available.
- **Never mix series** in one comparison (e.g. ULSD−WTI vs ULSD−Brent, single crack vs 3-2-1,
  intraday high vs settlement, Dated vs futures). Label any context-only series as such.
- **Conversions:** diesel/gasoil 7.45 bbl/t, jet/kerosene 7.9 bbl/t; $/gal × 42 = $/bbl.
- **Dated vs futures:** producers realise prices closer to Dated. The company-specific discount or
  premium belongs in the company analysis; this baseline reports the market spread as a signal.

## Data sources

Primary data beats commentary. Every figure states source, definition, unit and both observation
and publication date. If a connector fails or returns nothing, say so and use the next source.
Never fill a gap with an invented number.

| Need | First choice | Fallback / cross-check |
|---|---|---|
| Brent, WTI, ULSD front and every contract month | **Yahoo** `get_quote`: `BZ=F`, `CL=F`, `HO=F`; months as `BZZ27.NYM`, `CLZ29.NYM`, `HOZ28.NYM` (F,G,H,J,K,M,N,Q,U,V,X,Z) | EODHD EOD prices; press settlement reports |
| Monthly / annual actuals (forecast vs actual) | **Yahoo** `get_chart` on `BZ=F`, `HO=F` (monthly) | **Alpha Vantage** `BRENT`, `WTI` (EIA spot monthly averages, ~1 month lag; spot basis, so label it) |
| US inventories, refinery runs, product supplied | EIA Weekly Petroleum Status Report (Wednesdays) | Press summaries citing EIA |
| Global balance, demand, supply forecasts | IEA Oil Market Report, EIA STEO, OPEC MOMR (monthly) — tag `[E]`, note revisions | JODI (country data, lagged) |
| OPEC+ quotas and actual output | OPEC statements; MOMR secondary-source table | Agency surveys via press |
| European / Asian product stocks | Insights Global ARA (Thursdays), Enterprise Singapore (weekly) via press | — |
| Gasoil crack, jet crack, Dated Brent | Argus/Platts/ICE figures quoted in Reuters/Bloomberg | Agency reports |
| Disruptions (barrels reaching market) | Kpler/Vortexa export data via press; IEA/EIA; company statements | Other tracking firms — state the spread between estimates |
| Realised producer prices (cross-check only) | **Nordic Financial** `search_filings`/`company_research` with `ticker` + `fiscal_year` (e.g. EQNR, AKRBP) | Company reports |

Connector quirks (tested 2026-10-04):

- **Yahoo back months print stale.** Check `regularMarketTime` on every contract. Prints older
  than ~5 trading days (common for BZ 2028–2029) are flagged with their date; use the bid/ask
  midpoint only if both sides are present and plausible, otherwise cross-check with the liquid WTI
  contract of the same month plus the Brent–WTI spread from the nearest liquid month, and mark
  `[A]`.
- Yahoo drops unknown tickers silently — check that every requested ticker came back. ICE gasoil
  is **not** available on Yahoo.
- Alpha Vantage: 25 calls/day, 1 call/second, call sequentially.
- Nordic Financial has no oil-price series; `macro_summary` does not cover oil.
- Do not use SEO "market report" pages without a traceable primary source. When sources conflict,
  give both and say which one is used and why. Tables loaded as images cannot be read: mark "not
  read" and ask the user for the figures.

## Data discipline

- Tag every number: `[F]` reported fact · `[E]` external forecast or secondary claim · `[A]` own
  assumption · `[?]` unknown. Missing new data is not evidence that nothing changed.
- For each finding: (1) the fact, (2) what it means physically (barrels, stocks, refinery output),
  (3) whether it changes the model. Single news items normally do not move BBB. Diplomatic signals
  count only once they produce a verified, lasting physical effect.
- Known weak data: China's stocks (estimates only, sources disagree), Russian exports (tracking
  estimates), agency forecasts (revised hard in crises — always give the report date), long-dated
  futures (thin, stale prints).
- **User input is input, not a reference.** Links, numbers and drafts are assessed critically (what
  it measures, how fresh, which definition); use what holds, reject the rest, and note the
  assessment in the source appendix.

## Scenarios

There is no statistical distribution behind geopolitical and structural oil events, so Bear and
Bull are not percentiles.

- **Base:** the most likely path, and the decision case downstream.
- **Bear / Bull:** the worst and best reasonably foreseeable paths, each tied to **named
  catalysts** with mechanism, earliest timing and **signposts** (observable thresholds showing the
  market moving there). They need not be symmetric.
- Consider both a **supply** and a **demand** catalyst for each tail (e.g. Bear: disruption ends and
  OPEC+ fights for market share, or a global recession; Bull: a new supply outage on top of low
  stocks, or a strong demand rebound). Choose the catalyst or combination that gives the most
  relevant stress and say why.
- **Crude and distillates are linked but partly decoupled.** Cracks are driven by refining capacity
  and outages, product export policy, product stocks and season, and can move against Brent. Build
  the Brent path and the crack path separately:

```
Product price ($/bbl) = Brent + crack
Δ product price       = Δ Brent + Δ crack
```

## Procedure

Two modes, one procedure:

- **Initiate** — "create Oil Market BBB", "new baseline", or automatically when
  `docs/oil-market-bbb.md` does not exist. Full research on every step; status "Initial baseline";
  no change log values.
- **Update** — "update Oil Market BBB", "oppdater modul" in an oil context, or a recalibration
  trigger. Run every step in order; it is not a menu.

> Updating does not mean "summarise the latest oil news". It means new, thorough research that
> tests whether the current baseline is still right. Start from the last baseline but do not
> anchor on it: every run actively tries to falsify Base. If the evidence is not strong enough to
> change the model, say so explicitly: **Oil Market BBB kept unchanged.**

**Step 0 — Setup.** State the revision of this skill. Note analysis date, previous baseline date
and days since. Roll the window if this is the first run in a new year. Read the previous
`docs/oil-market-bbb.md` and record its point values, catalysts and signposts — they become the
"previous" column in the change log. If the previous file uses another structure or other series,
migrate it and log the migration.

**Step 1 — Market snapshot.** From the connectors: Brent, WTI and ULSD front month; the contract
strip for the stub, every quarter of Year 1 and each December to the end of the window; M1−M4;
diesel crack per contract month; Brent–WTI. Check the time stamp of every print. Add the Dated–
futures spread, the European gasoil crack and the jet crack from the latest reliable report.

**Step 2 — Crude supply.** OPEC+ quotas, compliance, actual exports and spare capacity, and whether
that spare capacity can physically reach the market. Non-OPEC growth (US, Brazil, Guyana, Canada,
Norway). Russia: crude exports, sanctions and their enforcement. **Disruptions** (Hormuz, Bab
el-Mandeb, Suez/SUMED, pipelines and bypass routes, attacks on export terminals): express each as
barrels per day of crude and products reaching the market versus before the disruption, never only
as "open/closed". How the barrels are shipped is out of scope.

**Step 3 — Demand.** Global and US, China, Europe, India; diesel/gasoil and jet separately.
Separate structural change, demand destruction (price or shortage) and rebound. Record agency
revisions since the last baseline.

**Step 4 — Inventories.** US crude, Cushing, SPR and distillate; OECD/Europe; ARA gasoil and jet;
Singapore middle distillates; China (estimates — name the method). Level versus the 5-year average
for the same week (state the years), draws/builds versus the seasonal norm, days of cover.
Strategic stock releases and refill needs.

**Step 5 — Refining and distillate supply.** Utilisation and outages by region (US, Europe, Middle
East, Russia, China, India, Africa/Dangote, Korea/Japan); new capacity and permanent closures;
product export policy (China quotas, Russian export bans, any US restrictions); regional
surpluses and deficits in mb/d (who exports distillates, who imports). This step drives the crack
path; stocks, season and the curve confirm it.

**Step 6 — Forward curve.** Classify Brent M1−M4 with the fixed table and read it together with the
inventory direction. If a spread cannot be sourced with a date, mark `[?]` and do not classify.

| Brent M1−M4 | Signal |
|---|---|
| Backwardation > USD 5/bbl | Clearly tight |
| Backwardation USD 2–5/bbl | Moderately tight |
| Backwardation USD 0–2/bbl | Roughly balanced |
| Contango USD 0–2/bbl | Slightly loose |
| Contango > USD 2/bbl | Clearly loose |

| Curve | Inventories | Reading |
|---|---|---|
| Backwardation | Falling | Strong physical tightness |
| Backwardation | Building | Normalisation may be under way |
| Contango | Falling | Curve lagging, or risk premium priced out — check |
| Contango | Building | Clear loose signal |

**Step 7 — Balance check.** Supply − demand = implied stock change (mb/d) per scenario and year.
A Brent path that needs a stock path the market cannot deliver must be adjusted. Compare with the
IEA and EIA balances and explain gaps.

**Step 8 — Test BBB.**
- **Base:** what would have to be true for Base to be wrong, and do we see it? Is it still the
  most likely path?
- **Bear / Bull:** are the catalysts still the right ones? Has a catalyst come closer, been
  triggered, or become irrelevant? Has a signpost been crossed? Is a supply or demand catalyst
  missing?
- **Evidence threshold:** change a scenario, catalyst or path only when several independent data
  points point the same way, or one event materially changes physical supply, refining or the
  stock path — and only by more than the minimum change.

**Step 9 — Set the paths.**
- **Brent and diesel crack** per scenario: stub, each year, 3-year average and mid-cycle, as point
  value + range. Anchor against the forward curve and agency forecasts, and explain every gap
  larger than USD 5/bbl.
- **Year 1 by quarter:** quarterly shape from the forward curve, rescaled so that the four quarters
  average to the scenario's annual value.
- **Jet crack** per scenario and year (annual only): from the jet market data, cross-checked as
  diesel crack + jet/diesel regrade. Mark confidence.
- **Brent–WTI** Base spread per year.
- **Mid-cycle** (used for IAF terminal values at exit): the normalised price after the window, per
  scenario. Anchor on the longest liquid futures, the full-cycle cost of marginal non-OPEC supply
  and the historical cycle range — never the last modelled year by default. Crack mid-cycle
  relative to its own historical normal band.
- **Each crack** is judged against its own historical normal band, not only against Brent.

**Step 10 — Distillate sensitivity.** Matrix of Brent scenario × diesel crack scenario for Year 1
and for the 3-year average, giving the diesel price in $/bbl and $/t. Mark combinations as
consistent or unlikely (e.g. Bear Brent + Bull crack needs refining or export loss without crude
shortage). Decompose the latest period's diesel price change into a Brent part and a crack part.

**Step 11 — Write, log and check.** Write the document in the output format, with a complete
change log (new / unchanged / changed with previous → new value, reason and source; forecast vs
actual; weights kept or changed; whether downstream skills should update). Read it back and run
the checks below.

## Recalibration triggers

A full update is due when any of these occurs:

- Brent front month or a December contract in the window moves > 15% within a month
- Brent M1−M4 changes regime in the classification table and stays there for two weeks
- Crude or product volumes reaching the market from a disrupted area change > 20%
- OPEC+ decision or actual production change > 0.5 mb/d
- Refining or product export capacity changes > 0.5 mb/d (outage, start-up, closure, export ban)
- Diesel crack moves > 25% within a month
- IEA, EIA or OPEC revise global demand > 0.5 mb/d for a year in the window
- A Bear or Bull catalyst is triggered or a signpost is crossed
- The baseline is older than 30 days

## Output: `docs/oil-market-bbb.md`

Keep the main part short per heading; series and source details go to the appendix.

```markdown
# Oil Market BBB — [baseline date]

## Metadata
- Analysis date, status (Initial / Final / Provisional and why), skill revision
- Previous baseline (date, days), window (stub + 2027–2029), stale after [date]
- Series used (Benchmarks section of the skill); any series change since last baseline

## Conclusion
- BBB changed / kept unchanged — explicit
- Base in two sentences (Brent path + diesel crack path)
- Main Bear catalyst and main Bull catalyst

## Interface (point values; ranges in the sections below)
| $/bbl, period average | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| Brent Bear / Base / Bull | | | | | |
| Diesel crack Bear / Base / Bull | | | | | |
| Diesel price Base ($/bbl and $/t) | | | | | |
| Jet crack Base | | | | | |
| Brent–WTI Base | | | | | |
| Forward curve (Brent / diesel crack, date) | | | | | — |

## Scenario definitions
| Scenario | Weight (convention) | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|
| Bear | 25% | | | | |
| Base | 50% | | | | |
| Bull | 25% | | | | |

## Brent ($/bbl) — point (range)
| Scenario | Stub | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|

## Year 1 by quarter ($/bbl)
| Scenario | Brent Q1 / Q2 / Q3 / Q4 | Diesel crack Q1 / Q2 / Q3 / Q4 |
|---|---|---|

## Distillate cracks ($/bbl) — point (range)
| Scenario | Diesel 27 / 28 / 29 / mid-cycle | Jet 27 / 28 / 29 |
|---|---|---|
- Historical normal band per crack; gasoil (Europe) cross-check vs ULSD

## Distillate sensitivity
- Brent × diesel crack matrix (Year 1 and 3-yr average; $/bbl and $/t), consistency marked
- Decomposition of the latest diesel price change (Brent part vs crack part)

## Drivers
### Crude supply (incl. disruptions in barrels reaching market)
### Demand
### Inventories
### Refining and distillate supply (incl. regional balances in mb/d)
### Forward curve (M1−M4, classification, long end, Dated–futures spread)
### Balance check (implied stock change per scenario and year vs IEA/EIA)

## Signposts and monitoring
| Signpost | Threshold (Bear / Bull) | Now | Previous | Direction |
|---|---|---|---|---|
- What to watch before the next update

## For downstream skills
- What changed that [[oil-shipping-bbb]] / [[rig-market-bbb]] / [[supply-market-bbb]] / IAF must take in, or "no material change"

## Change log
- New / unchanged / changed (previous → new, reason, source)
- Forecast vs actual for the realised or partly observed year
- Weights kept or changed — explicit
- New baseline date

## Appendix: sources
| Source | Content | Observed / published |
|---|---|---|
```

## Interface to downstream skills and IAF

Every baseline delivers, in the fixed Interface table and the sections behind it:

- Brent and diesel crack point values per scenario for the stub, each year and mid-cycle; Year 1
  by quarter; jet crack; Brent–WTI.
- The forward curve on the same basis (December contracts and Year-1 quarters) with its date.
- Supply, demand and the implied stock path per scenario; regional distillate surpluses and
  deficits in mb/d; disruption status in barrels reaching the market.
- Catalysts, signposts and their status.

Use by skill:

- **[[iaf-valuation]]** (oil producers, refiners): stub price for the stub quarters, Year-1
  quarters, annual Base path as the decision case, Bear/Bull paths as the catalyst stress tests,
  and the **mid-cycle** column for the terminal value V_T. Company-specific realised price
  differentials are set in the company analysis.
- **[[rig-market-bbb]]**: Brent path per scenario and the long end of the curve (E&P cash flow and
  FID logic).
- **[[supply-market-bbb]]**: Brent long end and mid-cycle (FID, tender and Petrobras capex logic)
  and disruption status; drilling activity reaches it through [[rig-market-bbb]].
- **[[oil-shipping-bbb]]**: crude and product volumes, regional balances, refining changes and
  disruption status, translated there into shipping effects. Shipping, rig and OSV companies do not take
  this baseline directly into IAF; it reaches them through their sector skill.

## Checks before finishing

- Skill revision stated; window and stub correct for today's date.
- Every price on the defined series and basis; no mixed series; every number tagged and sourced
  with dates; stale futures prints flagged.
- Stub identical across scenarios; Year-1 quarters average to the annual value.
- Point value and range for every scenario price; mid-cycle set and justified.
- Gaps > USD 5/bbl to the forward curve and agency forecasts explained.
- Balance check consistent with each Brent path.
- Bear and Bull each tied to named catalysts with signposts; no probability language.
- No shipping or rig content.
- Change log complete (previous → new) or explicit "kept unchanged".
- File written, read back, tables render.
