---
name: oil-shipping-bbb
description: Oil Shipping BBB — the tanker-market baseline for crude tankers (VLCC, Suezmax, Aframax) and product tankers (LR2, LR1, MR). Produces Bear/Base/Bull spot TCE paths per segment on the IAF time grid (stub quarter(s) of the current year + 3 calendar years, now 2027–2029), plus mid-cycle TCE and asset values for terminal values, the period/FFA market check, fleet supply, effective tonnage, trade flows and chokepoints in sailing days, and named catalysts with signposts. Base is the decision case; Bear and Bull are catalyst-based stress tests; 25/50/25 is a labelled convention, never a probability. Reads crude and distillate prices, volumes and disruptions from docs/oil-market-bbb.md and never makes its own oil forecast. ALWAYS use when the user mentions Oil Shipping BBB / Shipping BBB / tanker BBB, asks to create, run or update ("oppdater modul") the shipping module, or asks about tanker rates, TCE, time charter or FFA rates, ton-miles, tanker fleet or orderbook, effective tonnage, shadow fleet or tanker values — even without naming the skill. Feeds iaf-valuation for tanker companies.
---

# Oil Shipping BBB

**Revision:** 2026-10-04.4 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/oil-shipping-bbb/` in the Finance folder.

A Bear/Base/Bull baseline for the tanker market. It answers one question: **what market TCE and
asset values should a tanker-company valuation use, year by year and per segment, and what named
events would move them?** It is a testable hypothesis with explicit risks, not a news summary.

It sits between [[oil-market-bbb]] and [[iaf-valuation]]. It takes oil volumes, prices,
disruptions and refining changes as given from `docs/oil-market-bbb.md` and translates them into
vessel demand. It adds the shipping side itself: fleet, effective tonnage, routes and rates.

**Scope:** spot and period TCE, FFAs, vessel values, fleet and orderbook, effective tonnage,
trade flows by route, ton-miles and ton-days, chokepoints in sailing days. **Out of scope:**
oil price, crack, supply/demand or inventory forecasts (→ [[oil-market-bbb]]; read only); rigs
(→ [[rig-market-bbb]]); company fleet, contract cover, realised TCE premiums, costs, debt and
valuation (→ [[iaf-valuation]] company analysis); dry bulk, gas carriers and chemical tankers.

## Standing parameters

- **Time grid = IAF grid:** stub (remaining quarters of the current year) + 3 full calendar years,
  now Q4 2026 + 2027–2029; Year 1 also by quarter. Roll forward with the first run each January:
  the first year becomes "realised" (forecast vs actual) and a new end year is added. Rolling is
  not a reset — overlapping years are carried over and tested.
- **Rate basis:** nominal USD/day, period average, **market spot TCE** for the segment (see
  Benchmarks). Today's spot or a crisis peak is never annualised or used as a multi-year rate.
- **Point value + range** for every scenario rate and value. IAF uses the point value; the range
  shows uncertainty inside the scenario.
- **Base = the decision case.** Bear and Bull are stress tests tied to named catalysts.
  **25/50/25** is a labelled convention for optional weighted figures — never a probability.
- **Stub has no scenario spread** (IAF rule): stub TCE is actual spot for elapsed days plus the
  FFA/forward for the rest, the same in all three scenarios. Scenarios diverge from Year 1.
- **Segments are always separate:** VLCC, Suezmax, Aframax, LR2, LR1, MR — never one blended rate.
- **Minimum change (convention):** a point value moves only if the evidence moves it by at least
  10% (annual average TCE or asset value). Smaller moves are noted, not applied.
- **Staleness:** the baseline is stale after 30 days, or earlier if a recalibration trigger fires
  or `docs/oil-market-bbb.md` gets a newer baseline date. IAF treats a stale baseline as
  provisional.
- Benchmarks below are fixed. Changing a series is a method change and goes in the change log.

## Files

- Skill: `.claude/skills/oil-shipping-bbb/SKILL.md` (this file only, no reference files).
- Input: `docs/oil-market-bbb.md` (read only).
- Output: `docs/oil-shipping-bbb.md`, one running baseline. Baseline date in the H1. Git holds the
  history, so the previous version is read from the file before it is overwritten.
- Write with Write/Edit, then **read the file back** and check every table and number. An answer
  in the conversation alone is not delivery.

## Benchmarks and units

| Segment | Size (dwt / cargo) | Spot TCE basis | Baltic route proxy | FFA |
|---|---|---|---|---|
| VLCC | ~300k / 2.0 mb crude | Segment average spot TCE, modern eco | TD3C MEG–China | TD3C (liquid) |
| Suezmax | ~150k / 1.0 mb crude | Same | TD20 WAF–Continent | TD20 |
| Aframax | ~110k / 0.7 mb crude | Same | TD25 USG–UKC; TD19 Cross-Med | TD25, TD19 |
| LR2 | ~110k coated / 75 kt clean | Same | TC1 MEG–Japan 75 kt | TC1 (thin) |
| LR1 | ~75k / 55 kt clean | Same | TC5 MEG–Japan 55 kt | TC5 (thin) |
| MR | ~50k / 37–38 kt clean | Same | TC2 + TC14 Atlantic triangulation | TC2, TC14 |

- **Spot TCE** = market average earnings for a modern (≤ 10-year) eco, non-scrubber vessel, after
  voyage costs, before opex. Use one publisher's segment average consistently (broker weighted
  average over several routes). If only Baltic route TCEs are available, use the proxy route
  and say so. Never compare a route TCE with a segment average without labelling it.
- **Period rates:** 1-year and 3-year time charter, modern eco vessel, $/day. These are the
  market's own normalised rate and the main control on the BBB paths.
- **Asset values:** newbuild contract price, 5-year-old and 10-year-old secondhand value ($m),
  scrap price ($/ldt). Same publisher where possible.
- **Demand units:** ton-miles (volume × distance) and **ton-days** (vessel days actually
  absorbed, including waiting, STS, rerouting and slow steaming). In disrupted markets ton-days
  is the better measure; always say which one is used.
- **Barrels → vessels:** vessels required = flow (mb/d) × round-trip days ÷ cargo size (mb).
  Example: 1 mb/d MEG–China (≈ 50-day round trip) ÷ 2 mb = ~25 VLCCs. State round-trip
  assumptions per route.
- **Company-specific adjustments are not made here:** scrubber and eco premiums, age discounts,
  pool fees, commissions, the 4–6 week lag between spot fixtures and reported TCE (load-to-
  discharge accounting), and booked cover all belong in the company analysis.

## Data sources

Primary data beats commentary. Every figure states source, definition, unit and both observation
and publication date. If a connector or page fails, say so and use the next source. Never fill a
gap with an invented number.

| Need | First choice | Fallback / cross-check |
|---|---|---|
| Oil volumes, prices, disruptions, refining | **`docs/oil-market-bbb.md`** (Interface + "For downstream skills") | — never a connector or own estimate |
| Spot TCE by segment, weekly | Broker weekly reports (Intermodal, Banchero Costa, Gibson, BRS, Poten, Signal Ocean) and Baltic figures quoted in Lloyd's List, TradeWinds, Splash247 | Company-reported spot TCE |
| Realised TCE, booked share of next quarter, TC fixtures | **Nordic Financial** `search_filings`/`company_research` with `ticker` + `fiscal_year` (FRO tested; HAFNI, OET, TRMD-A to test) | **FinancialFilings** for US filers (DHT, INSW, TNK, STNG, NAT): resolve id with `companies_list` |
| 1-year / 3-year TC rates | Broker weekly TC tables | Company TC fixtures in reports and announcements |
| FFAs (Q and Cal contracts) | Baltic/FIS curves quoted in press or broker reports | Company commentary — mark `[E]`, "not verified" if no dated level |
| Fleet, orderbook, deliveries, age, scrapping, contracting | Clarksons, BIMCO, Veson, Breakwave, broker reports via press | Company presentations (cite their underlying source) |
| Sanctioned / shadow fleet | Lloyd's List Intelligence, Kpler, S&P Global via press; OFAC/EU/UK designation lists | Company presentations |
| Chokepoint transits | **IMF PortWatch** API (daily, ~1 week lag) | Kpler/Vortexa via press; canal authorities (Suez, Panama) |
| Trade flows by route, floating storage | Kpler/Vortexa export and route data via press | IEA/EIA trade data (lagged) |
| Asset values, newbuild prices | VesselsValue/Veson, Clarksons, broker S&P reports via press | Company sale and purchase announcements (price, age, date) |

Connector quirks (tested 2026-10-04):

- **IMF PortWatch** (no key, query with curl): `https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query`
  with `where=portname='Strait of Hormuz'`, `outFields=date,portname,n_tanker,n_total,capacity_tanker`,
  `orderByFields=date DESC`, `f=json`; `outStatistics` gives averages for a baseline period.
  Names include Strait of Hormuz, Bab el-Mandeb Strait, Suez Canal, Panama Canal, Cape of Good
  Hope, Malacca Strait. Counts are **AIS-based**: vessels sailing dark are missed. In Sep 2026
  Hormuz showed 1–2 tankers/day (Jan 2026 average 31) while Kpler had crude near pre-war volume.
  For Hormuz and any war zone, use Kpler barrels; use PortWatch for Suez, Bab el-Mandeb, Cape and
  Panama, and as a direction signal only where vessels sail dark.
- **Nordic Financial:** always set `ticker` and `fiscal_year`. The first chunk of a quarterly
  report usually has spot TCE per segment and new TC fixtures; booked share of the current quarter
  is further down. Text excerpts only — read numbers from the text.
- **Broker weeklies as PDFs** (tested 2026-10-04): Hellenic Shipping News republishes them. Find
  the PDF link on the article page with `curl -A "Mozilla/5.0" <article> | grep -o 'https://[^"]*\.pdf'`,
  download with curl and read with `pdftotext -layout`.
  - **Xclusiv** (Mondays): segment average T/CE for VLCC, Suezmax and Aframax, route TCEs, newbuild
    prices and 5/10/15-year values. It is the primary segment-average and asset-value publisher.
    Its TC2/TC6 text has repeated TC1/TC5 numbers (template error), so do not use those two.
  - **Intermodal** (Tuesdays): 1-year and 3-year TC by segment with 2024/2025 averages, and 5-year
    values. `-layout` scrambles the TC table; rebuild each row from "this week" + "diff" = "last
    week" before use.
  - **Fearnleys** (Wednesdays): 1-year TC for eco/scrubber vessels, values and newbuild prices.
  - **Affinity** (Fridays): Baltic route TCEs for the TD and TC routes (right-hand columns; use
    `cut -c180-`).
  - The Baltic Exchange site and Seatrade/Splash247 block automated fetches (challenge page or 403).
- **FFA levels from BWET holdings:** amplifyetfs.com/bwet lists TD3C/TD20 monthly contracts with
  lots and notional market value. Price in $/t = market value ÷ (lots × 1,000 t). Convert TD3C to
  TCE with (price × 270,000 − ~$2.6m voyage costs) ÷ ~48 days. Then scale to the segment average
  with the observed segment/TD3C ratio. Mark `[A]`; contracts beyond three months are thin.
- **EODHD** `get_sanctions_vessels` returns 403 on the free plan. Not usable.
- **Yahoo** has no freight or FFA series, and the BWET price history is distorted. Use Yahoo only
  for tanker equity prices (company analysis).
- No Python on this machine. Compute PortWatch averages with PowerShell `Invoke-RestMethod`, paging
  with `resultOffset`.
- Do not use SEO "market report" pages without a traceable primary source. When sources conflict,
  give both and say which one is used and why. Tables loaded as images cannot be read: mark "not
  read" and ask the user for the figures.

## Data discipline

- Tag every number: `[F]` reported fact · `[E]` external forecast or secondary claim · `[A]` own
  assumption · `[?]` unknown. Missing new data is not evidence that nothing changed.
- For each finding: (1) the fact, (2) what it means physically (ton-days, effective vessels,
  utilisation), (3) whether it changes the model. Single fixtures, one week's rate spike or one
  diplomatic statement normally do not move BBB. They count once they produce a verified, lasting
  physical effect.
- Known weak data: shadow fleet size (estimates differ widely; give the range and the definition),
  orderbook delivery years (slippage), FFA levels quoted second-hand, company-sourced market
  estimates (restocking volumes, ton-mile claims — they talk their book), AIS counts in war zones.
- **User input is input, not a reference.** Links, numbers and drafts are assessed critically (what
  it measures, how fresh, which definition); use what holds, reject the rest, and note the
  assessment in the source appendix.

## Scenarios

There is no statistical distribution behind chokepoints, sanctions or fleet waves, so Bear and
Bull are not percentiles.

- **Base:** the most likely path, and the decision case in IAF.
- **Bear / Bull:** the worst and best reasonably foreseeable paths for tanker earnings, each tied
  to **named catalysts** with mechanism, earliest timing and **signposts**. They need not be
  symmetric, and crude and product tankers may get different catalysts.
- **Built on the oil baseline.** Each shipping scenario names the [[oil-market-bbb]] scenario it
  uses. The mapping is not one-to-one: a disruption ending is oil Bear but removes tanker
  inefficiency and can also trigger restocking demand. Choose the oil scenario that fits the
  shipping catalyst and explain the mapping. A shipping catalyst (fleet, sanctions, routing) can
  be combined with oil Base. If a scenario needs an oil path the oil baseline does not have, flag
  it for [[oil-market-bbb]] — never invent one here.
- Consider both a **demand** catalyst (volumes, distance, inefficiency) and a **supply** catalyst
  (deliveries, scrapping, sanctions, shadow fleet returning) for each tail.
- **Rates respond non-linearly to the balance:** near full utilisation small changes move rates a
  lot; in surplus rates sink towards opex-level TCE. Sustained rates above newbuild parity attract
  orders that deliver about three years later.

## Procedure

Two modes, one procedure:

- **Initiate** — "create Oil Shipping BBB", "new shipping baseline", or automatically when
  `docs/oil-shipping-bbb.md` does not exist. Full research on every step; status "Initial
  baseline"; no change log values.
- **Update** — "update Oil Shipping BBB", "oppdater modul" in a shipping context, or a
  recalibration trigger. Run every step in order; it is not a menu.

> Updating does not mean "summarise the latest shipping news". It means new, thorough research
> that tests whether the current baseline is still right. Start from the last baseline but do not
> anchor on it: every run actively tries to falsify Base. Today's extreme spot is never
> annualised. If the evidence is not strong enough to change the model, say so explicitly:
> **Oil Shipping BBB kept unchanged.**

**Step 0 — Setup.** State the revision of this skill. Note analysis date, previous baseline date
and days since. Roll the window if this is the first run in a new year. Read the previous
`docs/oil-shipping-bbb.md` and record its point values, catalysts and signposts — they become the
"previous" column in the change log. If the previous file uses another structure or other series,
migrate it and log the migration.

**Step 1 — Oil input.** Read `docs/oil-market-bbb.md`: baseline date and status, Interface table,
scenario definitions, supply/demand/stock path, disruption status in barrels, regional distillate
balances and the "For downstream skills" section. If it is stale (> 30 days) or older than the
latest material oil event, say so and get it updated **first**. Translate, do not re-analyse:

| Oil input | Shipping effect |
|---|---|
| Crude exports by region, OPEC+ output | Crude cargo volumes per route (VLCC/Suezmax demand) |
| Disruptions in barrels reaching market | Lost or rerouted cargoes; bypass routes and STS |
| Implied stock change, strategic refill | Restocking cargoes; floating storage |
| Brent curve (contango vs backwardation) | Floating storage economics |
| Regional distillate surpluses/deficits, cracks | Product arbitrage, long-haul product flows (LR/MR) |
| Refinery start-ups, closures, export bans | Shift from crude to product trade, new long-haul lanes |

**Step 2 — Spot and period market.** Per segment: latest spot TCE and quarter-to-date average,
1-year and 3-year TC, FFA for the rest of the current quarter, Year-1 quarters and the calendar
years available. Company-reported spot TCE and booked share of the current quarter as a
cross-check. Separate extreme spot (event-driven peaks) from the period market. Compare with the
previous baseline.

**Step 3 — Trade flows and demand.** Per segment, the main routes: MEG → Asia, Atlantic Basin
(US Gulf, Brazil, Guyana, WAF) → Asia and Europe, Russia (compliant and shadow trade),
India/Middle East → Europe (products), US Gulf → Europe/Latin America (products), China product
exports, floating storage and restocking. Look for changes in **both** volume and distance; more
volume on a shorter route can lower ton-miles. Express demand growth per scenario and year in
ton-days (and ton-miles where meaningful).

**Step 4 — Chokepoints.** Hormuz, Bab el-Mandeb/Red Sea, Suez/SUMED, Saudi East-West/Yanbu
outlet, Panama, Cape of Good Hope. For each: transits now vs normal (PortWatch/Kpler), extra
sailing days on the affected routes, waiting time, repositioning, and the share of each segment's
fleet absorbed — never only "open/closed" or a threat level. Barrels lost or rerouted come from
the oil baseline.

**Step 5 — Effective tonnage.** Nominal fleet minus what is not available to compliant trade:
sanctioned/shadow fleet, vessels > 15 and > 20 years old (charterer restrictions), drydock and
offhire (incl. war damage), floating storage, vessels tied up in long voyages, STS and shuttle
service, mispositioning; plus clean↔dirty switching between LR2 and Aframax (and LR1/Panamax).
Quantify per segment as a share of the fleet.

**Step 6 — Fleet supply (window + 1 year).** Per segment and year:

```
fleet start + deliveries − scrapping ± clean/dirty crossover = fleet end
effective fleet growth = change in (fleet − unavailable tonnage) / effective fleet start
```

Track orderbook/fleet, new contracting, delivery schedule and slippage, cancellations, scrapping
and the scrapping pool (≥ 20 years), yard slots (earliest delivery for a new order) and
newbuild prices. A shadow fleet returning to compliant trade or being scrapped changes effective
supply even when the nominal fleet does not.

**Step 7 — Balance check.** Per segment, scenario and year: demand growth (ton-days) − effective
fleet growth = change in tightness (percentage points). Read it against the rate path: a rising
TCE with a loosening balance, or the reverse, must be explained or adjusted. Compare with
published utilisation estimates from one named source.

**Step 8 — Asset values and anchors.** Newbuild price, 5-year and 10-year values, scrap price,
and their change since the last baseline. Compute per segment:
- **Newbuild-parity TCE:** the TCE that pays opex plus an annuity on the newbuild price over 25
  years at 8% nominal (convention), net of scrap value. Sustained rates above it attract orders.
- **Opex-level TCE / cash breakeven floor:** where rates settle in a deep surplus.
- **Asset-implied TCE:** the TCE the 5-year value capitalises (remaining life, same 8%), showing
  what the S&P market prices.

**Step 9 — Test BBB.**
- **Base:** what would have to be true for Base to be wrong, and do we see it? Is it still the
  most likely path?
- **Bear / Bull:** are the catalysts still the right ones? Has a catalyst come closer, been
  triggered, or become irrelevant? Has a signpost been crossed? Is a demand or supply catalyst
  missing? Has crude or product tanker changed more than the other?
- **Evidence threshold:** change a scenario, catalyst or path only when several independent data
  points point the same way, or one event materially changes ton-days, effective tonnage or fleet
  growth — and only by more than the minimum change.

**Step 10 — Set the paths.**
- **Spot TCE** per segment and scenario: stub, each year, 3-year average and mid-cycle, as point
  value + range ($k/day).
- **Stub:** quarter-to-date actual spot plus the FFA (or latest spot if no FFA) for the rest,
  identical across scenarios.
- **Year 1 by quarter:** shape from the FFA quarterly curve where liquid, otherwise from typical
  seasonality (strong Q1 and Q4, weaker Q2–Q3) marked `[A]`; rescaled so the four quarters average
  to the scenario's annual value.
- **Period check:** Base 3-year average vs 3-year TC, Base Year 1 vs 1-year TC and Cal FFA.
  Explain every gap above 20%. Period rates are priced on prompt tonnage and include risk premia
  in both directions; say which way the gap should close.
- **Mid-cycle** (used for IAF terminal values at exit): the normalised TCE after the window, per
  scenario. Anchor on the long-run average spot TCE for the segment (state the years, with and
  without crisis years), the newbuild-parity TCE, the 3-year TC and the fleet age profile at exit
  — never the last modelled year by default.
- **Asset values at mid-cycle** per scenario: 5-year-old and newbuild ($m), consistent with the
  mid-cycle TCE (asset-implied TCE ≈ mid-cycle TCE). The company analysis adjusts for its own
  fleet's age and specification.

**Step 11 — Write, log and check.** Write the document in the output format, with a complete
change log (new / unchanged / changed with previous → new value, reason and source; forecast vs
actual; weights kept or changed; whether IAF analyses should update). Read it back and run the
checks below.

## Recalibration triggers

A full update is due when any of these occurs:

- `docs/oil-market-bbb.md` gets a new baseline whose "For downstream skills" section flags a
  change in volumes, disruptions, regional balances or refining
- 1-year TC or the Year-1 FFA in any segment moves > 15% from the baseline value
- Transits at a chokepoint (Hormuz, Bab el-Mandeb/Suez, Panama) change > 20% and hold for two weeks
- Orderbook/fleet in a segment changes > 2 percentage points, or new contracting in a quarter
  exceeds 3% of the segment fleet
- Sanctioned/shadow fleet changes > 2% of a segment's effective fleet (designations or lifting)
- A trade rule changes a major flow (port fees, product export bans, sanctions on a route)
- A Bear or Bull catalyst is triggered or a signpost is crossed
- The baseline is older than 30 days

## Output: `docs/oil-shipping-bbb.md`

Keep the main part short per heading; series and source details go to the appendix.

```markdown
# Oil Shipping BBB — [baseline date]

## Metadata
- Analysis date, status (Initial / Final / Provisional and why), skill revision
- Previous baseline (date, days), window (stub + 2027–2029), stale after [date]
- Oil Market BBB used (baseline date, status)
- Series used (Benchmarks section of the skill); any series change since last baseline

## Conclusion
- BBB changed / kept unchanged — explicit
- Base in two sentences (crude tankers; product tankers)
- Main Bear catalyst and main Bull catalyst

## Interface — spot TCE, $k/day, period average (point values; ranges below)
| Segment Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| VLCC | | | | | |
| Suezmax | | | | | |
| Aframax | | | | | |
| LR2 | | | | | |
| LR1 | | | | | |
| MR | | | | | |

## Interface — asset values, $m
| Segment | Newbuild now | 5-yr now | 10-yr now | 5-yr mid-cycle Bear / Base / Bull | Newbuild mid-cycle Base |
|---|---|---|---|---|---|

## Scenario definitions
| Scenario | Weight (convention) | Oil BBB scenario used | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|
| Bear | 25% | | | | | |
| Base | 50% | | | | | |
| Bull | 25% | | | | | |

## Crude tankers — spot TCE $k/day, point (range)
| Scenario | Segment | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|

## Product tankers — spot TCE $k/day, point (range)
| Scenario | Segment | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|

## Year 1 by quarter ($k/day)
| Scenario | VLCC Q1–Q4 | Suezmax Q1–Q4 | Aframax Q1–Q4 | LR2 Q1–Q4 | LR1 Q1–Q4 | MR Q1–Q4 |
|---|---|---|---|---|---|---|

## Market check
| Segment | Spot latest / QTD | 1-yr TC | 3-yr TC | FFA rest-of-Q / Cal-27 / Cal-28 | Base 2027 / 3-yr avg | Gap > 20% explained |
|---|---|---|---|---|---|---|
- Anchors: long-run average TCE, newbuild-parity TCE, opex-level floor, asset-implied TCE

## Drivers
### Oil input and translation (oil scenario mapping; table of shipping effects)
### Trade flows and demand (ton-days / ton-miles per scenario and year)
### Chokepoints (transits vs normal, extra sailing days, fleet share absorbed)
### Effective tonnage (per segment, share of fleet unavailable)
### Fleet supply (fleet, orderbook %, deliveries, scrapping, effective growth per year)
### Balance check (demand − effective fleet growth, per segment, scenario and year)

## Signposts and monitoring
| Signpost | Threshold (Bear / Bull) | Now | Previous | Direction |
|---|---|---|---|---|
- What to watch before the next update

## For IAF
- What changed that tanker-company analyses must take in, or "no material change"

## Change log
- New / unchanged / changed (previous → new, reason, source)
- Forecast vs actual for the realised or partly observed year
- Weights kept or changed — explicit
- New baseline date

## Appendix: sources
| Source | Content | Observed / published |
|---|---|---|
```

## Interface to IAF

Every baseline delivers, in the fixed Interface tables and the sections behind them:

- Spot TCE point values per segment and scenario for the stub, each year and mid-cycle; Year 1
  by quarter; ranges.
- Asset values now and at mid-cycle (5-year-old and newbuild) per segment.
- The period market (1-year and 3-year TC, FFAs) with its date, and the anchors (newbuild-parity
  TCE, opex-level floor).
- Fleet supply, effective tonnage and the balance per scenario; catalysts, signposts and status.

Use in [[iaf-valuation]] (tanker companies, Track B):

- **Stub and Year-1 quarters:** market spot TCE for the company's **open** days. Booked days and
  rates come from the company's own guidance.
- **Years 2–3:** Base path as the decision case; Bear/Bull paths as the catalyst stress tests.
- **Terminal value V_T:** mid-cycle TCE × operating days − normalised costs, or NAV from the
  mid-cycle asset values, adjusted for the fleet's age at exit.
- **Growth capex (ROIC_g):** newbuild prices, yard slots, 1-year and 3-year TC and the
  newbuild-parity TCE are the evidence for returns on new vessels.
- **Mapping:** match each vessel to the right segment row (LR2 trading dirty → Aframax). The
  company's premium or discount to market TCE (scrubber, eco, age, pool, timing lag) is set and
  sourced in the company analysis.

## Checks before finishing

- Skill revision stated; window and stub correct for today's date; Oil Market BBB baseline date
  and status stated, and not stale.
- No own oil forecast: every oil figure traces to `docs/oil-market-bbb.md`.
- Every rate on the defined basis (segment average vs route proxy labelled); every number tagged
  and sourced with dates; no spot peak annualised.
- Stub identical across scenarios; Year-1 quarters average to the annual value.
- Point value and range for every scenario rate; mid-cycle TCE and asset values set and anchored.
- Gaps > 20% to the period market explained; balance check consistent with each rate path.
- Chokepoints in sailing days and fleet share, not "open/closed".
- Bear and Bull each tied to named catalysts with signposts and an oil scenario; no probability
  language.
- Change log complete (previous → new) or explicit "kept unchanged".
- File written, read back, tables render.
