---
name: oil-shipping-bbb
description: Oil Shipping BBB — the tanker-market baseline for crude tankers (VLCC, Suezmax, Aframax) and product tankers (LR2, LR1, MR). Produces Bear/Base/Bull spot TCE paths per segment on the IAF time grid (stub quarter(s) of the current year + 3 calendar years, now 2027–2029), plus mid-cycle TCE and asset values for terminal values, the period/FFA market check, fleet supply, effective tonnage, trade flows and chokepoints in sailing days, and named catalysts with signposts. Base is the decision case; Bear and Bull are catalyst-based stress tests; 25/50/25 is a labelled convention, never a probability. Reads crude and distillate prices, volumes and disruptions from docs/oil-market-bbb.md and never makes its own oil forecast. ALWAYS use when the user mentions Oil Shipping BBB / Shipping BBB / tanker BBB, asks to create, run or update ("oppdater modul") the shipping module, or asks about tanker rates, TCE, time charter or FFA rates, ton-miles, tanker fleet or orderbook, effective tonnage, shadow fleet or tanker values — even without naming the skill. Feeds iaf-valuation for tanker companies.
---

# Oil Shipping BBB

**Revision:** 2026-10-24.1 — bump on every change (date.counter). This file is the master and the
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
| Realised TCE, booked share of next quarter, TC fixtures | **Nordic Financial** `search_filings`/`company_research` with `ticker` + `fiscal_year` (FRO and HAFNI tested; OET, TRMD-A to test); full report via `parse_pdf_to_text` on the IR PDF. **DHT business updates** (GlobeNewswire, ~2 weeks after quarter end: last quarter's spot/TC TCE and the booked share of the current quarter, discharge-to-discharge) | **FinancialFilings** for US filers (DHT, INSW, TNK, STNG, NAT): resolve id with `companies_list`; SEC 6-K usually a day or more later |
| VLCC fixture count and daily TD3C/TD15 marks | **Infront TDN Direkt via Nordnet** ("TANK: N VLCC-slutninger …", from the Fearnleys fixture list): fixtures per day, WS and TCE, and the AG VLCC fixture count by loading month (a volume signpost) | Baltic weekly roundup (direct; see quirks); Affinity; Fearnleys weekly |
| 1-year / 3-year TC rates | Broker weekly TC tables | Company TC fixtures in reports and announcements |
| FFAs (Q and Cal contracts) | **Gibson weekly** (current-quarter FFA in TCE); BWET holdings for the next months (derived `[A]`); Baltic/FIS curves quoted in press | Company commentary — mark `[E]`, "not verified" if no dated level |
| Orderbook in vessels (VLCC, Suezmax, Aframax/LR2) and share of fleet ≥ 20 years | **Frontline quarterly release** (industry sources; SEC 6-K exhibit or GlobeNewswire), "orderbook" paragraph | Company presentations quoting Clarksons (cite the underlying source) |
| Fleet count and dwt per segment; half-year deliveries, recycling, contracting, cancellations | **Allied QuantumSea research** in the Allied weekly (semi-annual tanker fleet issue) | Breakwave, BIMCO |
| Orderbook/fleet ratio per segment incl. LR1/Panamax, MR2, Handy/MR1 | **Xclusiv** orderbook issue (periodic, e.g. 13 Jul 2026) | BIMCO (crude vs product %) |
| Delivery schedule by year | VLCC: BRS weekly (via press), Clarksons via Frontline presentations, Signal Ocean quarterly crude schedule (via press). Products: Hafnia quarterly presentation (orderbook by year in m dwt, Handy–LR2/Aframax) | BIMCO outlook (share of orderbook delivering 2028+) |
| Weekly new orders and demolition sales | **Xclusiv weekly** "NEWBUILDING ORDERS" and "DEMO SALES" tables (reported deals only = a minimum count) | Allied weekly newbuilding table; Signal/MSI/Allied year-to-date order counts via press |
| Sanctioned share of the old fleet | BIMCO outlook; Clarksons tallies via press | Frontline management comments |
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
  is further down. Text excerpts only — read numbers from the text. For 2026 the database holds
  only the Newsweb results announcement. Hafnia's announcement (2026-10-05 test) gives fleet TCE
  and coverage but not TCE per segment (LR2/LR1/MR/Handy), so read those from the full report:
  `parse_pdf_to_text` on the IR PDF (Hafnia: `s201.q4cdn.com/891122012/files/doc_financials/<year>/q<n>/`;
  get the link in the in-app browser, since the IR page builds it with JavaScript). The large
  output is saved to a file: read it with `py`. For new TC fixtures and newbuild orders, use
  `source="newsweb"` + `ticker` + `fiscal_year`. See the iaf-valuation skill for details.
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
    Read it directly at **fearnpulse.com** in the in-app browser: navigate, wait ~5 s (the page is
    a JavaScript app and shows a spinner first), then `get_page_text`. It is available on the
    publication day, before the Hellenic Shipping News PDF (tested 2026-10-15). Its "Brent Spot"
    figure was stale ($83.97 vs a $105.88 front-month) and is not used.
  - **Baltic Exchange weekly tanker roundup** (Fridays, published the same day; tested 2026-10-17):
    `balticexchange.com/en/data-services/WeeklyRoundup/tanker/news/<yyyy>/tanker-report-week-<n>.html`.
    It reads in the in-app browser: navigate, wait ~3 s, then read `document.body.innerText` with
    `javascript_tool` (`get_page_text` returns only a sidebar headline). It gives WS and Baltic
    round-trip TCE for every TD and TC route, the MR Atlantic Triangulation Basket and the BDTI.
    It is the first choice for Baltic route TCEs; Affinity and Cyprus Shipping News republish it
    later. Copy errors occur (week 41 gave TD19 the TD25 TCE), so check each TCE against its WS
    move. Baltic TCEs are a standard-vessel basis, ~4–6% below Gibson's eco basis.
  - **TD34** (Gulf of Oman/Mina al Fahal → Ningbo, 270 kt; live June 2026; ICE FFA since 5 Oct
    2026, alongside TD15) is the VLCC that loads after the shuttles and STS. It tracked the Xclusiv
    VLCC segment average within 3% on 9 Oct 2026. Use TD34 ÷ TD3C as a second estimate of the
    segment/TD3C ratio for the stub. No public TD34 FFA levels; BWET holds only TD3C and TD20.
  - **Affinity** (Fridays): Baltic route TCEs for the TD and TC routes (right-hand columns; use
    `cut -c180-`). Fallback to the Baltic roundup above.
  - **Compass Maritime weekly** (Mondays; tested 2026-10-17): curl and `pdftotext -layout` work on
    `compassmar.com/wp-content/uploads/<yyyy>/<mm>/Compass-Weekly-Report-<Mon>-<dd>-<yy>.pdf`
    (e.g. `Oct-12-26`). It gives:
    - 12-month TC for VLCC, Suezmax, Aframax, LR1 (80k) and MR (47k), current and last week. It is
      the third TC source and the second free LR1 source besides Intermodal. Its Suezmax TC can stay
      unchanged for weeks, so check whether it moved.
    - "Newbuilding statistics": deliveries in vessels per segment for the rest of the year and the
      next two years. Use them for the delivery-schedule spread.
    - Values (newbuild / resale / 5-yr / 10-yr). In the text the rows shift one line down; realign
      before use.
    - The S&P and recycling-statistics tables extract misaligned; do not use them.
  - **Xclusiv NEWBUILDING ORDERS / DEMO SALES tables** (tested 2026-10-10): extract with
    `awk '/NEWBUILDING ORDERS/{p=1} /Sale & Purchase|SECONDHAND PRICES/{p=0} p' file.txt | grep "^ *TANKER"`
    (demolitions: from `DEMO SALES` to `Commodities`). Units and dwt per line are reliable; the
    yard, buyer, price and delivery columns are often misaligned, so read those with care. Issues are
    weekly at `wp-content/uploads/<yyyy>/<mm>/xclusiv-<yyyy>_<mm>_<dd>.pdf` (Mondays).
  - **Allied weekly** PDFs are on cyprusshippingnews.com (`wp-content/uploads/<yyyy>/<mm>/ALLIED-Weekly-Market-Report-Week-<n>.pdf`).
    The "Market Snapshot" table extracts with values shifted one row down; realign before use.
  - The Baltic Exchange site and Seatrade/Splash247 block WebFetch and curl (challenge page or 403).
    The Baltic weekly roundup and press releases read in the in-app browser (see above).
    Splash247 articles read fine in the in-app browser (`mcp__Claude_Browser__navigate`, then
    `get_page_text`; tested 2026-10-13). Splash often names the yard, price comparables and S&P
    deals, which is enough to confirm an aggregator report.
  - **TradeWinds** is paywalled, but a share link from the user (`…?lid=…&unlockToken=…`) reads in
    full in the in-app browser (navigate, wait ~4 s, `get_page_text`; tested 2026-10-15). Its
    period-fixture reports (named ship, term, rate, charterer, broker 1- and 3-year assessments) feed
    the period-market check. Test a 3-year fixture against Base over the same 36 months **including
    the stub**, not against the 2027–29 average. Test any period fixture over the months it actually
    runs, **from its delivery month**. A one-year deal delivering in November covers Nov–Dec at the
    late-quarter paper level, not the stub average, so scale those months with the monthly FFA shape
    (BWET or Gibson). Fixtures and broker assessments are cross-checks; the 15% trigger is tested
    only on the baseline's own TC series (Intermodal, then Fearnleys).
    Without an unlock link, the user's DN Media login (logged-in Edge, `mcp__edge__browser_navigate`
    + `browser_evaluate` over the `<article>` paragraphs) shows only the lead paragraphs. The rest
    sits behind a TradeWinds paywall (tested 2026-10-22). Use the lead for the headline fact. The
    user has no TradeWinds subscription: unlock links come only when the user happens to receive
    one, so do not ask for them. Look for the same fact in a free source instead (Splash247,
    broker weeklies). The "Read more" list on each article is
    a free headline feed for leads.
- **Company updates and Nordnet news** (tested 2026-10-12):
  - GlobeNewswire blocks WebFetch (403). The search page and releases read fine through the Edge
    connection (`mcp__edge__browser_navigate`, then `browser_evaluate` with `innerText`).
  - Nordnet news links (`nordnet.no/market/news/<uuid>`) load only in the user's logged-in Edge.
    Wait ~2 s after navigating before reading `innerText`, or the result is empty.
  - Nordnet items are TDN summaries: use the primary release, and the TDN text as a cross-check.
  - TDN bunker prices differed from Gibson/Xclusiv by ~$100/t on the same day (Oct 2026). Do not
    use them.
  - **Newbuilding news from aggregators** (e.g. maritimebriefs.com) often lacks yard, price or
    primary reference, and can mix up sizes (LR1 vs LR2). Log it as unconfirmed `[?]` in the
    contracting log and register, outside the delivery schedule, until a broker table (Xclusiv,
    Allied), the yard, the buyer or TradeWinds confirms it. Size the effect (orderbook %, quarter
    contracting %, deliveries per window year) even when unconfirmed.
  - **Company realised TCE is a lagging cross-check, never a market mark.** A discharge-to-discharge
    reporter's booked share of the current quarter reflects fixtures made 4–6 weeks earlier. In a
    fast market, compare it with the segment average of the fixing period, not with the stub.
- **Frontline release on SEC** (tested 2026-10-10): `curl -A "<name> <email>"` on the 6-K exhibit
  (sec.gov requires a user agent), strip tags, and grep "order book". It gives the orderbook in
  vessels for VLCC, Suezmax and Aframax/LR2 and the ≥ 20-year shares now and at full delivery.
- **Hafnia investor presentation** (tested 2026-10-10): `s201.q4cdn.com/891122012/files/doc_financials/<yyyy>/q<n>/Hafnia-Limited-Q<n>-<yyyy>-Investor-Presentation-vF.pdf`
  (Q1 2026 used `-vF2`). The "Orderbook, Scrap & Sanctioned Landscape" slide extracts as bar labels:
  the four orderbook bars (2026–2029, m dwt) sum to the stated total, which confirms the reading.
  Company view: tag `[E]`.
- **FFA levels from BWET holdings:** amplifyetfs.com/bwet lists TD3C/TD20 monthly contracts with
  lots and notional market value. Price in $/t = market value ÷ (lots × 1,000 t). Convert TD3C to
  TCE with (price × 270,000 − ~USD 2.6m voyage costs) ÷ ~48 days. Then scale to the segment
  average with the observed segment/TD3C ratio. Mark `[A]`. Check the lot count per month: Q1
  contracts became usable in Oct 2026 (110 lots/month); 5 lots is too thin to use. Tested
  2026-10-10: derived Q4 TD3C USD 1.38m/day vs Gibson's quoted USD 1.40m/day.
- **Gibson weekly report** (gibsons.co.uk/report/<slug>, Fridays; the Hellenic Shipping News copy
  is only an excerpt): route WS and TCE tables with a **quoted Q4 FFA in TCE** for TD3C, TD20, TD25,
  TC5, TC7 and TC18, plus attack and downtime counts. It is the first-choice FFA source for the
  rest of the current quarter.
- **EODHD** `get_sanctions_vessels` returns 403 on the free plan. Not usable.
- **Yahoo** has no freight or FFA series, and the BWET price history is distorted. Use Yahoo only
  for tanker equity prices (company analysis).
- Python runs as `py` (not `python`). PortWatch averages also work in PowerShell with
  `Invoke-RestMethod`, paging with `resultOffset` (tested 2026-10-10).
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
- **Provenance on every fetched value.** Record the source (connector or publisher plus series,
  ticker or document), the **as-of date** (observation or report date, not the fetch date) and the
  unit and currency. A value without an as-of date is `[?]`. Show the as-of date in every table
  that carries market data, and the oldest input date in the Metadata section.
- **Raw → checked → derived.** Keep the value as fetched in the source appendix before it is
  converted, averaged or adjusted. A derived value names its conversion. A correction never
  overwrites the raw value: record both and say why.
- **Validate before use.** Run these checks on every fetched value. A failed check is flagged in
  the text ("stale", "unverified", "unit check failed"), never silently fixed or dropped:
  - *Units and scale:* $/day vs $k/day, Worldscale points vs TCE, dwt vs vessel count, ton-miles vs
    ton-days.
  - *Basis and period:* spot vs 1-year TC vs FFA, eco/scrubber vs standard TCE, route vs segment
    average, weekly vs period average.
  - *Staleness:* spot TCE older than 1 week; TC and FFA quotes older than 2 weeks; asset values and
    fleet/orderbook counts older than 1 month. Older inputs are used only with the flag and their
    age.
  - *Plausibility:* a spot move of more than 25% in a week, or a TC/asset-value move of more than
    10% vs the current document. Such a jump is confirmed in a second source or the primary document
    before it moves the model. Otherwise it is held as `[?]`.
  - *Cross-source:* where two sources cover the same item, compare them. A gap beyond normal noise
    is explained, never averaged away.

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

A shadow fleet returning to compliant trade or being scrapped changes effective supply even when
the nominal fleet does not.

**Fleet and orderbook register (every run).** Keep the fixed register table in the output (see
Output) for all six segments and update every cell, with source and as-of date:

- **Fleet** (vessels, m dwt), **orderbook** (vessels, % of fleet; say whether the fleet is the
  total or the commercially traded fleet), **deliveries year-to-date**, **delivery schedule** for
  the rest of the current year and each year of the window plus the year after, **new orders**
  (current quarter and year-to-date), **scrapping** (current quarter and year-to-date),
  **share ≥ 20 years** (now and at full delivery where published), **sanctioned/outside compliant
  trade**, **newbuild price** and **earliest yard slot** (by yard country).
- **Delivery schedule rules:** use published schedules first and show the spread between
  sources. Where only the total orderbook is known, allocate it by year using the closest
  published shape (e.g. Signal Ocean's crude schedule, Hafnia's dwt by year), mark `[A]`, and make
  the years sum to the orderbook. Cross-check against any published dwt total (e.g. VLCC +
  Suezmax deliveries over the window).
- **Contracting and demolition log:** each run adds the reported orders and demolitions since the
  last run (Xclusiv weekly tables) to the quarter's log, per segment. Reported deals are a minimum
  count; compare with tracker totals (Signal, MSI, Allied, BIMCO) and state the gap.
- **Slippage:** once a year's actual deliveries are known, compare them with the schedule recorded
  at the start of that year and log the difference.
- **Scrapping assumption:** state per segment and year in Base, Bear and Bull, against the
  ≥ 20-year pool, the sanctioned share (sanctioned ships are hard to sell for recycling) and the
  rate level in that scenario. Scrapping is a scenario variable, not a constant.
- **Triggers:** test the orderbook (> 2 pp) and quarterly contracting (> 3% of fleet) triggers
  on one consistent basis each run, and say which source the test uses.
- A cell that cannot be sourced is `[?]`, never filled from an older run without its date.

**Step 7 — Balance check.** Per segment, scenario and year: demand growth (ton-days) − effective
fleet growth = change in tightness (percentage points). Count inefficiency (waiting, STS, shuttles,
rerouting) **once**, in ton-days demand. Effective fleet growth covers only fleet changes
(deliveries, scrapping, damage and repair, sanctions, clean/dirty crossover). Read it against the rate path: a rising
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
  identical across scenarios. Build it on the segment itself:
  - Take the quarter-to-date segment average (weekly Xclusiv; estimate the latest unpublished week
    from the Baltic routes, TD34 for VLCC, and mark it `[A]`).
  - Scale the remaining months by the paper's own path (BWET monthly contracts, or the Gibson
    quarter FFA against the route's quarter-to-date average).
  - Use "route quarter FFA × one-day segment/route ratio" only as a cross-check. It fails when the
    route diverges from its segment (Oct 2026: TD25 vs the Aframax average, TD3C vs the VLCC
    average).
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
### Fleet and orderbook register
| Segment | Fleet (vessels; m dwt) | Orderbook (vessels; % fleet) | Delivered YTD | Schedule: rest of year / Y1 / Y2 / Y3 / later | New orders: quarter / YTD | Scrapped: quarter / YTD | ≥ 20 yrs now / at full delivery | Sanctioned / outside compliant trade | Newbuild $m; earliest slot |
|---|---|---|---|---|---|---|---|---|---|
| VLCC | | | | | | | | | |
| Suezmax | | | | | | | | | |
| Aframax/LR2 | | | | | | | | | |
| LR1/Panamax | | | | | | | | | |
| MR | | | | | | | | | |
- One row per segment; source and as-of date in every cell (or `[?]`)
- Contracting and demolition log for the quarter (reported deals per segment vs tracker totals)
- Delivery schedule spread between sources; slippage vs the schedule recorded at the start of the year
### Fleet supply (fleet growth per segment and year; scrapping per scenario)
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
- Fleet and orderbook register complete for all six segments, every cell sourced and dated or
  `[?]`; delivery schedule sums to the orderbook; contracting/demolition log updated; orderbook and
  contracting triggers tested on a stated basis.
- Bear and Bull each tied to named catalysts with signposts and an oil scenario; no probability
  language.
- Change log complete (previous → new) or explicit "kept unchanged".
- Every fetched value has source, as-of date and unit; raw kept beside derived; validation
  checks run and failures flagged in the text.
- File written, read back, tables render.
