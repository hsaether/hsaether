---
name: supply-market-bbb
description: Supply Market BBB (Supply BBB) — the offshore supply vessel (OSV) market baseline with main focus on the North Sea (NCS and UK) and South America (Brazil first, then Guyana/Suriname). Covers PSV, AHTS, subsea/CSV/IMR, Brazil RSV (vessel + ROV) and Brazil PLSV. Produces Bear/Base/Bull rate and utilization paths per segment on the IAF time grid (stub quarter(s) of the current year + 3 calendar years, now 2027–2029), North Sea spot by quarter for Year 1, mid-cycle rates and vessel values for terminal values, newbuild and reactivation parity, demand in vessel-days, fleet supply (orderbook, laid-up, attrition, migration between regions) and named catalysts with signposts. Base is the decision case; Bear and Bull are catalyst-based stress tests; 25/50/25 is a labelled convention, never a probability. Reads the oil path from docs/oil-market-bbb.md and rig activity from docs/rig-market-bbb.md and never makes its own oil or rig forecast. ALWAYS use when the user mentions Supply BBB / Supply Market BBB / OSV BBB, asks to create, run or update ("oppdater modul") the supply module, or asks about PSV or AHTS rates, North Sea spot, OSV utilization, Petrobras vessel tenders, RSV or PLSV rates, OSV fleet, newbuilds, laid-up vessels or OSV values — even without naming the skill. Feeds iaf-valuation for OSV and subsea-vessel owners (e.g. DOF, Solstad, Tidewater, Paratus/Seagems).
---

# Supply Market BBB

**Revision:** 2026-10-05.2 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/supply-market-bbb/` in the Finance folder.

A Bear/Base/Bull baseline for the offshore supply vessel market. It answers one question: **what
market rates, paid days and vessel values should an OSV-owner valuation use, year by year, per
segment and region, and what named events would move them?** It is a testable hypothesis with
explicit risks, not a news summary.

It sits below [[oil-market-bbb]] and [[rig-market-bbb]] and feeds [[iaf-valuation]]. It takes the
oil price path and rig activity as given and translates them into vessel demand through this chain:

**Oil path (via rig activity, FIDs and producing assets) → offshore activity per region → demand in
qualified vessel-days → effective supply of qualified vessel-days → utilization → rate**, modified
by **contract cover** (days already locked) and **fleet mobility** (vessels moving between regions
and into offshore wind).

**Focus:** the North Sea (Norway/NCS and UK/UKCS) and South America (Brazil, Guyana/Suriname). Other
regions appear only as a **global context** block: they are the source and sink of vessels that
move in or out of the focus regions, and they set the global orderbook and asset values.

**Scope:** spot and term rates, Petrobras contract rates, utilization, contract cover at market
level, demand in vessel-days, fleet and orderbook, laid-up and reactivation, attrition, migration,
vessel values, newbuild and reactivation economics. **Out of scope:** oil price and oil balance (→
[[oil-market-bbb]]; read only); rig demand, rig counts and dayrates (→ [[rig-market-bbb]]; read
only); tankers (→ [[oil-shipping-bbb]]); a company's own backlog, realised rates, opex, capex, debt,
JV structures and valuation (→ [[iaf-valuation]] company analysis); seismic, liftboats, crew boats
and offshore wind service vessels (SOV/CSOV/CTV) as markets of their own — offshore wind enters
only as demand that competes for CSVs, PSVs and AHTS.

## Standing parameters

- **Time grid = IAF grid:** stub (remaining quarters of the current year) + 3 full calendar years,
  now Q4 2026 + 2027–2029. Roll forward with the first run each January: the first year becomes
  "realised" (forecast vs actual) and a new end year is added. Rolling is not a reset —
  overlapping years are carried over and tested.
- **Year-1 quarterly shape for North Sea spot only.** The North Sea spot market is seasonal (weak
  winter, strong summer construction and rig-move season), so the North Sea spot rows get a Year-1
  by-quarter table. Term, Petrobras and PLSV/RSV rows are contract-driven and have no quarterly
  shape. Seasonal factors are `[A]`, derived from named historical years, and must average to the
  annual value (time-weighted).
- **Rate basis and currency:** nominal, in the market's own currency, k/day:
  - North Sea: **GBP k/day** (spot is quoted in GBP; NOK or USD term fixtures are converted at the
    FX on the fixture date and tagged).
  - Brazil, Guyana/Suriname and global context: **USD k/day** (a Petrobras BRL portion is
    converted at the FX on the bid or award date and stated).
  - Never average across currencies, segments or service scopes. IAF converts to the company's
    reporting currency under its own FX rule.
- **Utilization basis:** one named source series per row (see Segments). Spot utilization, active-
  fleet utilization, total-fleet utilization and a company's fleet utilization are different
  measures and stay separate.
- **Point value + range** for every scenario rate, utilization and value. IAF uses the point value;
  the range shows uncertainty inside the scenario.
- **Base = the decision case.** Bear and Bull are stress tests tied to named catalysts.
  **25/50/25** is a labelled convention for optional weighted figures — never a probability.
- **Stub has no scenario spread** (IAF rule): the same value in all three scenarios. North Sea spot
  stub = quarter-to-date average plus the seasonal-normal rest of the quarter `[A]`; term and
  contract rows = the six-month leading-edge. Scenarios diverge from Year 1.
- **Contract cover sets the spread:** the Bear–Bull spread is narrow where the year is highly
  covered (Brazil long-term contracts, PLSV) and wide where exposure is open (North Sea spot). A
  spread that does not follow cover must be explained.
- **Paid days and rate stay separate.** Annual revenue is rate × paid days, never a spot rate × all
  calendar days. A rate per available calendar day already contains the utilization effect.
- **Minimum change (convention):** a point value moves only if the evidence moves it by at least
  10% (North Sea spot annual average), 5% (term, contract or PLSV/RSV rate, vessel value) or
  2 percentage points (utilization; 3 pp for spot utilization). Smaller moves are noted, not applied.
- **Staleness:** the baseline is stale after 30 days, or earlier if a recalibration trigger fires,
  or `docs/oil-market-bbb.md` or `docs/rig-market-bbb.md` gets a newer baseline date whose
  downstream section flags a supply-relevant change. IAF treats a stale baseline as provisional.
- Segments, regions, definitions and source series below are fixed. Changing one is a method change
  and goes in the change log.

## Files

- Skill: `.claude/skills/supply-market-bbb/SKILL.md` (this file only, no reference files).
- Inputs (read only): `docs/oil-market-bbb.md`, `docs/rig-market-bbb.md`, and the IAF skill
  `.claude/skills/iaf-valuation/SKILL.md` for the time grid, scenario convention and how the
  output is used.
- Output: `docs/supply-market-bbb.md`, one running baseline. Baseline date in the H1. Git holds the
  history, so the previous version is read from the file before it is overwritten.
- Write with Write/Edit, then **read the file back** and check every table and number. An answer
  in the conversation alone is not delivery.

## Segments and regions

| Row | Definition | Rate series | Utilization / cover series | Role |
|---|---|---|---|---|
| **NS large PSV — spot** | North Sea PSV, Seabrokers class "PSVs > 900 m²" | Seabrokers *Seabreeze* monthly spot average, GBP/day | Seabrokers spot average utilisation (large PSV); active and laid-up counts | Core BBB, with Year-1 quarters |
| **NS large PSV — term** | Same class, firm term ≥ ~6 months, NCS and UK fixtures logged separately | Leading-edge term fixtures, GBP/day | Term cover of the named North Sea PSV fleet | Core BBB |
| **NS AHTS — spot** | North Sea AHTS, Seabrokers class "AHTS > 22,000 bhp"; high-end subset noted | Seabrokers *Seabreeze* monthly spot average, GBP/day | Seabrokers spot average utilisation (large AHTS) | Core BBB, with Year-1 quarters |
| **NS subsea / CSV-IMR** | Construction support and IMR vessels (crane, deck, ROV hangar, accommodation) in the North Sea, vessel-only basis | Leading-edge term or seasonal vessel charters, GBP/day (USD/EUR converted) | Cover of the named North Sea CSV fleet; offshore wind share recorded | Core BBB |
| **Brazil PSV** | PSVs on Petrobras or IOC contracts in Brazil, by Petrobras class (e.g. PSV 3000 / 4500); Brazilian vs foreign flag noted | Petrobras tender/award leading-edge, USD/day | Vessels contracted ÷ vessels available in Brazil (proxy; named source) | Core BBB |
| **Brazil AHTS** | AHTS on Petrobras or IOC contracts, by Petrobras BHP class; flag noted | Petrobras tender/award leading-edge, USD/day | As Brazil PSV | Core BBB |
| **Brazil RSV** | ROV support vessels on Petrobras contracts, **vessel + ROV package** | Petrobras award leading-edge, USD/day, package basis | Cover of the named Brazil RSV fleet | Core BBB |
| **Brazil PLSV** | Flexible pipe-lay support vessels for Petrobras (tension, carousel capacity, water depth, Petrobras qualification) | Petrobras award leading-edge, USD/day (vessel + crew; services stated) | Cover of the named PLSV fleet (closed set, rig-by-rig style) | Core BBB |
| NS medium PSV | Below the large-PSV boundary; mostly older tonnage | Broker spot average where published | Broker counts | Secondary (attrition and migration signal) |
| NS AHTS — term | Large/high-end AHTS on term (mooring campaigns, floating wind, FPSO hook-up) | Term fixtures | Named-fleet cover | Secondary |
| Guyana/Suriname PSV & AHTS | Vessels supporting Stabroek and Suriname developments | Contract announcements; company regional averages `[E]` | Company fleet status | Secondary |
| Brazil OSRV | Oil spill response vessels on Petrobras contracts | Petrobras awards | Named-fleet cover | Secondary |
| Other South America | Argentina, Trinidad, Colombia, Falklands | — | — | Only when a company analysis needs it |
| Global context | West Africa, Mediterranean, US Gulf/Mexico, Middle East, India, SE Asia, Australia | Company regional average dayrates (e.g. Tidewater) as reference only `[E]` | Global active/laid-up counts, orderbook | Context block, no BBB rows |

- **Core rows** get full Bear/Base/Bull for rate and utilization (or cover), ranges and mid-cycle.
- **Secondary rows** get a Base point + range; Bear and Bull only when a company analysis uses the
  row. Confidence is stated on each.
- Add a row when an IAF company analysis needs it and records the gap. Log it as a method change.

**Technical classification.** Classify from verified specifications, never from price or from the
owner's other vessels. Record the source's class boundary and keep it:

- **PSV:** deck area (m²) and DWT, plus liquid-mud/brine capacity and DP class where relevant.
- **AHTS:** BHP and bollard pull (BP) together with winch, deck, DP and design. Working bands:
  < 12k BHP · 12–16k · ~16–20k · > 20k BHP. Around 180–210 t BP is a large-AHTS control point;
  **true high-end is normally > 220 t BP** with matching winch and deck — > 200 t BP alone does not
  make a vessel high-end. Place boundary vessels explicitly. Source thresholds (e.g. 18k, 20k or
  22k BHP) are kept as published when sources are compared.
- **CSV / IMR / RSV:** crane (t, active heave compensation), deck area, ROV systems, accommodation
  and the actual service scope. An RSV rate with ROVs is not comparable to a vessel-only CSV rate.
- **PLSV:** top tension (t), carousel/storage capacity, water-depth rating, flag and Petrobras
  qualification. PLSV is its own market; never proxy it with PSV/AHTS or global OSV utilization.
- Specialist vessels count in PSV/AHTS totals only with an explicit reconciliation of the fleet
  universe.

**Regions** (one vessel = one region, by current or contracted work area; a vessel moves when it
starts the new contract): **Norway (NCS) · UK (UKCS) · other North Sea (DK/NL sectors) · Brazil ·
Guyana/Suriname · Other South America**, plus the global-context regions above.

- **North Sea spot is one pool** (vessels trade between UK and Norwegian sectors), so spot rows are
  North Sea-wide. **Demand and term are split NCS vs UK**: NCS is driven by Equinor/Aker BP
  developments, frame agreements and a stable tax regime; UK by declining drilling, a heavier tax
  burden, spot exposure and decommissioning. Never construct an NCS or UK spot rate from the pool.
- **Brazil access is gated.** Brazilian-flag and Brazilian-built vessels have priority, and a
  foreign-flag vessel needs authorisation when no Brazilian-flag vessel is available (Lei 9.432/97
  and Antaq rules). Record flag status per vessel: Brazilian-flag and foreign-flag vessels are
  separate competitive pools and can price differently.
- NCS gates (operator qualification, emissions or crewing requirements) are recorded when they
  limit which vessels compete.

## Definitions and units

| Term | Definition |
|---|---|
| Total fleet | All existing vessels of the class, incl. laid-up; excludes vessels under construction |
| Laid-up (warm / cold) | Warm: crewed or quickly reactivated (weeks); cold: unmanned, needs reactivation capex and months |
| Active fleet | Total fleet − laid-up − vessels permanently out of oil and gas (converted, sold for other use) |
| Spot pool | Vessels of the class trading the North Sea spot market in the period (broker definition) |
| Qualified fleet | Active fleet in the region that meets class, spec, flag and operator requirements |
| **Spot utilization** | Vessel-days on hire in the spot pool ÷ vessel-days available in the spot pool (broker definition; state it) |
| Active utilization | Vessel-days on hire ÷ active-fleet vessel-days |
| Contract cover | Firm contracted vessel-days ÷ available vessel-days of the named fleet, per row and year. Options carry a stated exercise probability, never 0/100 by default |
| Vessel-day | One vessel on hire for one day. Demand in vessel-days = activity × documented ratio (see Procedure, Step 5) |
| Effective capacity | Qualified fleet × days − drydock/SPS, mobilisation, transit and offhire days |
| Friction ceiling | Practical maximum utilization (drydocks, transits, gaps between jobs), below 100%. Rates react before it is reached |
| **Spot average** | Monthly average of spot fixtures for the class, as published by the named broker. **Quarterly and annual values = arithmetic mean of the monthly averages.** Seabrokers' own annual figure is fixture-weighted (~11% lower in 2025); show it as a cross-check only |
| **Leading-edge term rate** | Comparable recent term fixtures (same class/spec and region, start within ~12 months, firm ≥ ~6 months): median, range and n |
| **Petrobras leading-edge** | Rates in the latest Petrobras tender results or awards for the class (start within ~18 months, firm term stated): median, range, n |
| Realised rate | Rate a company reports for its fleet (blended regions, spot/term, services) — never a clean market index |
| Contract value per day | Total contract value ÷ (vessels × firm calendar days, stated date convention); may include mobilisation, ROVs, crew, services, escalation |
| Mark-to-market gap | Leading-edge − a fleet's backlog rate; the bridge into the company analysis |

- Spot and term are always reported separately: the term premium or discount to spot is a signal.
- State for every rate: currency, nominal, day count, and whether it includes crew, fuel,
  mobilisation, ROV/AUV, project work or other services. North Sea spot rates are time-charter
  style (charterer pays fuel); say so if a source differs.
- A contract value per day is a comparison point, not a rate per paid day. Missing service split
  limits how far it can be used.
- Growth rates and utilization use the same fleet definition in numerator and denominator.

**Fixture rate confidence:**

| Grade | Meaning |
|---|---|
| A | Rate stated by charterer, owner, exchange filing, Petrobras result or broker report with vessel named |
| B | Derived from contract value ÷ firm days (mobilisation, ROVs or services may distort) |
| C | Estimate from trade press, analyst or other secondary source |
| D | Unknown — tag `[?]`, never guessed |

## Data sources

Primary data beats commentary. Every figure states source, definition, unit and both observation
and publication date. If a connector or page fails, say so and use the next source. Never fill a
gap with an invented number.

| Need | First choice | Fallback / cross-check |
|---|---|---|
| Brent path, long end, mid-cycle, disruptions | **`docs/oil-market-bbb.md`** (Interface + "For downstream skills") | — never a connector or own estimate |
| Rig activity, rig-years, NCS/UK/Brazil/Guyana rig status, Petrobras drilling, rig moves | **`docs/rig-market-bbb.md`** (Interface, region × segment matrix, operator demand) | — never an own rig forecast; flag gaps to [[rig-market-bbb]] |
| North Sea spot rates, spot utilization, fixtures, vessels in/out of the North Sea | Broker market reports: **Westshore, Seabrokers, Fearnley Offshore Supply (FOSLive), Braemar** | [Hagland](https://hagland.market/) spot listings and monthly reports (sample, not total market) |
| North Sea term fixtures, contract awards by owner | Owner announcements: **Nordic Financial** `search_filings` with `source="newsweb"` + `ticker` + `fiscal_year`, `limit` 10–20 (dated, with the owner's size class); broker reports | Trade press `[E]`, grade C |
| NCS / UK activity | Sokkeldirektoratet (wells, field developments, production), Havtil consents, NSTA (UK wells, decommissioning), OEUK reports | Operator plans (Equinor, Aker BP, Vår Energi, Harbour, others) |
| Brazil demand and contracts | **Petrobras** (Strategic Plan, usually late Nov; FPSO start-ups, wells to connect; Petronect tenders and results) | Owner announcements; ANP (production, wells); trade press |
| Brazil fleet by flag and type | ABEAM fleet statistics; Antaq authorisations | Owner fleet lists (DOF, Solstad, OceanPact, CBO, Tidewater, Bram) |
| Guyana/Suriname | ExxonMobil and TotalEnergies project schedules (FPSO sequence, drilling) | Company fleet status (e.g. Tidewater Americas) |
| Global fleet, orderbook, laid-up, global utilization | Westwood public publications; Clarksons/Esgian via press `[E]` | Tidewater quarterly (utilization and dayrate by region and class) |
| Owner filings — Oslo/Nordic (DOF, Solstad, Havila, Eidesvik, Paratus, others) | **Nordic Financial** `search_filings` / `company_research` with `ticker` + `fiscal_year`; 2026 holds only the results announcement, so read the full report with `parse_pdf_to_text` on the IR PDF | FinancialFilings, Newsweb, company IR |
| Owner filings — US and other (Tidewater, OceanPact) | **FinancialFilings** (`companies_list` → id; `filings_list` newest first) | SEC EDGAR, CVM/B3, company IR |
| Offshore wind demand competing for CSV/PSV/AHTS | Developer and contractor announcements (construction schedules, W2W and cable campaigns, floating-wind mooring) | Trade press `[E]` |
| Vessel values, newbuild prices and lead times, reactivation cost | Sale and purchase announcements (price, age, spec, date, buyer); newbuild orders with price; owner reactivation guidance | VesselsValue/Clarksons values via press `[E]` |
| FX for currency conversion | **AllRatesToday** (`get_rates_authenticated` with `time`) per the IAF FX rule | Yahoo `get_chart` |
| Trade press | Offshore Energy, Offshore mag, Splash247, TradeWinds, Upstream, Brasil Energia, Petronotícias | Analyst notes — `[E]`, grade C, never sole evidence for a rate |

Quirks (observed in the 2026-10-05 initial run):

- **Seabrokers *Seabreeze*** is the anchor series for the North Sea spot rows:
  - `seabrokers.no/chartering/seabreeze` serves the latest monthly report as a PDF. Older months
    are at `seabrokers.no/chartering/seabreeze/markedsrapport-<month>-<year>` (Norwegian month
    names), and some at `wp-content/uploads/...`.
  - WebFetch cannot parse the PDF but saves it to `tool-results/`. Convert with
    `pdftotext -table <file> -` (available in Git Bash). `-layout` misaligns the utilisation table;
    `-table` gives clean columns. pdftoppm is not installed, so pages cannot be read as images.
  - Each report gives:
    - the monthly averages for the current and previous year per class;
    - the month's average, minimum and maximum rate;
    - six months of spot utilisation;
    - named arrivals and departures, excluding term/layup.
  - December reports give the annual averages. The daily availability chart is not extractable.
- **SSY Offshore Spot Market Update** (cms.ssyglobal.com PDFs, weekly) splits Norway (NOK) and UK
  (GBP) PSV spot and lists fixtures. Use it for the NCS–UK two-tier check, not as the anchor series.
- **Hagland spot list** loads dynamically and returns no content via fetch: mark "not read".
- **Tidewater results PDF** (q4cdn) parses with `pdftotext -table`. It gives day rate,
  utilization, vessel counts and vessel opex by region and class. That is the best public
  cross-check (Europe/Med for the North Sea; Americas blends Brazil, Guyana and others).
- **Petrobras rates:**
  - Brasil Energia, Seatrade, Marinelog, BNamericas and Splash247 return 403. Award rates often
    survive only in search snippets (grade C) or as owner contract values (grade B).
  - Reference rates in tender documents (e.g. PSV 4500 $40,670.51, Apr 2025) are a cap, not an award.
  - Portuguese searches ("licitação", "taxa diária") find more than English ones.
- **Owner announcements** state contract value and duration but rarely the scope split (ROV,
  services). Show the value per day as grade B with the scope stated.
- SEO "market report" pages without a traceable primary source are rejected (e.g.
  offshoreindustry.co.uk). Check the date of every press snippet: old Prorefam bids (2013) and
  2025 market reports surface in searches for 2026.
- Company regional averages (Tidewater "Europe/Mediterranean", "Americas") blend regions, classes
  and contract types. Use them as context and cross-check, never as a regional index.
- Paid databases (Clarksons, Westwood MarineLogix, Esgian, VesselsValue) are not available.
  Westwood public "Insight" notes give global fleet, laid-up, orderbook and utilization.
- Expect 50+ searches and fetches for a full run: Seabreeze first, then Tidewater/owners, then
  Petrobras (Portuguese), then activity sources.

## Data discipline

- Tag every number: `[F]` reported fact · `[E]` external forecast or secondary claim · `[A]` own
  assumption · `[?]` unknown. Missing new fixtures or data are not evidence that nothing changed.
- For each finding: (1) the fact, (2) what it means physically (vessel-days of demand, qualified
  vessels added or removed, cover), (3) whether it changes the model. One fixture or one tender does
  not move a row without a stated reason. Several reports of the same announcement are one
  observation.
- **One series = one source.** Two brokers' spot averages or utilization figures measure different
  pools: never mix them in one series. If a source changes, document it and show both values for
  one overlapping date.
- **Never double count:** a vessel is not a newbuild, a reactivation and part of the active fleet at
  once. A delivered newbuild moves from the orderbook to the fleet. A reactivation adds to active
  capacity only if the vessel was excluded at the start; the total fleet does not grow. Migration
  adds to one region and subtracts from another (net zero globally). Mergers, refinancing and
  ownership changes create no vessels. The same campaign is not counted twice in demand.
- **Activity ≠ pricing power:** utilization can rise while rates lag (long contracts, aggressive
  bids, Petrobras price caps), and spot rates can spike on a few days of tightness without lifting
  the annual average.
- **Management guidance is `[E]`.** Owners talk their book; Base is set from cover, tenders,
  fixtures and the balance, and the gap to guidance is stated.
- n < 3 comparable fixtures in six months → a range and "low confidence", not a point.
- Known weak data: North Sea term rates (few published), Brazil rates (selective publication),
  vessel-per-rig ratios (calibrated, not observed), offshore wind demand for oil-and-gas tonnage,
  cold-stacked vessel condition, vessel values (few transactions).
- **User input is input, not a reference.** Links, numbers and drafts are assessed critically (what
  it measures, how fresh, which definition); use what holds, reject the rest, and note the
  assessment in the source appendix.

## Scenarios

There is no statistical distribution behind FIDs, Petrobras budgets or fleet migration, so Bear and
Bull are not percentiles.

- **Base:** the most likely path, and the decision case in IAF.
- **Bear / Bull:** the worst and best reasonably foreseeable paths for OSV earnings, each tied to
  **named catalysts** with mechanism, earliest timing and **signposts**. They need not be symmetric,
  and the North Sea and Brazil may get different catalysts.
- **Built on the oil and rig baselines.** Each scenario names the [[oil-market-bbb]] scenario and
  the [[rig-market-bbb]] scenario it uses. The mapping is not one-to-one:
  - **Two demand legs with different sensitivity.** Drilling support (PSV, AHTS rig moves) follows
    rig activity; production support (PSV, IMR, RSV) follows producing installations and is sticky.
    Development work (AHTS mooring, CSV, PLSV, RSV) follows FIDs and start-ups with 1–3 years' lag.
  - **Lags.** Year 1 is mostly set by cover and sanctioned projects; the last year depends on FIDs
    and tenders decided now. A short oil price shock does not create a multi-year rate path.
  - **Policy-driven demand.** Petrobras plans and NCS sanctioned projects are less price-sensitive
    than UK activity, exploration and new FIDs.
  - **Supply response caps the upside:** high rates bring reactivations, migration into the region
    and, with 2–3 years' lag, newbuilds. Test the response from low/mid-spec tonnage up to high-end.
  - **Operational events are separate:** strikes, weather, regulatory or force-majeure stops are
    assessed as their own line, not inferred from the oil price.
  - A supply catalyst (newbuild wave, migration, wind demand shift) can be combined with oil and rig
    Base. If a scenario needs an oil or rig path the input baselines do not have, flag it for
    [[oil-market-bbb]] or [[rig-market-bbb]] — never invent one here.
- Consider both a **demand** catalyst (Petrobras plan, NCS/UK activity, FIDs, decommissioning, wind
  construction) and a **supply** catalyst (newbuild orders and deliveries, reactivations, migration,
  conversions to wind, attrition of old tonnage) for each tail.
- Test relevant mixed paths: high oil with an operational stop; strong rig demand with PSV newbuilds;
  tight high-end AHTS with moderate total days; dearer financing that delays new capacity; wind
  construction pulling CSVs out of oil and gas or releasing them.
- **Rates respond non-linearly:** near the friction ceiling a few vessels move spot rates a lot (the
  North Sea spot pool is small); in surplus rates sink towards cash breakeven. Reactivation parity
  is the practical ceiling while laid-up qualified tonnage exists; newbuild parity once it is gone.
- **High-end AHTS:** a rig move or mooring job needing several qualified vessels at once can give
  extreme spot rates for a few days. Keep the paid rate and the paid days apart; the annual average
  is what IAF uses.

## Procedure

Two modes, one procedure:

- **Initiate** — "create Supply BBB", "new supply baseline", or automatically when
  `docs/supply-market-bbb.md` does not exist. Full research on every step; status "Initial
  baseline"; no change log values.
- **Update** — "update Supply BBB", "oppdater modul" in a supply/OSV context, or a recalibration
  trigger. Run every step in order; it is not a menu.

> Updating does not mean "summarise the latest OSV news". It means new, thorough research that
> tests whether the current baseline is still right. Start from the last baseline but do not
> anchor on it: every run actively tries to falsify Base. If the evidence is not strong enough to
> change the model, say so explicitly: **Supply Market BBB kept unchanged.**

**Step 0 — Setup.** State the revision of this skill and of [[iaf-valuation]]. Note analysis date
(Europe/Oslo), information cut-off, previous baseline date and days since. Roll the window if this
is the first run in a new year. Read the previous `docs/supply-market-bbb.md` and record its point
values, catalysts, signposts and open checkpoints — they become the "previous" column in the change
log, and every open checkpoint is closed or carried with a new status. Check **current vessel
ownership** (mergers, fleet sales, renames, vessels converted, sold out of oil and gas or recycled)
before using any fleet list.

**Step 1 — Oil and rig input.** Read `docs/oil-market-bbb.md` and `docs/rig-market-bbb.md`:
baseline dates, status, "stale after" dates, Interface tables, scenario definitions and downstream
sections. If either is stale or older than the latest material event, say so, mark this baseline
**Provisional**, and get the input baseline updated **first** when the supply conclusion depends on
it. Translate, do not re-analyse:

| Input | Supply effect |
|---|---|
| Brent path per scenario, long end, mid-cycle | FID and tender economics; UK activity; Petrobras capex envelope (use long end and mid-cycle, not spot) |
| Rig activity per region (NCS, UK, Brazil, Guyana): working rigs, rig-years, moored semis vs DP drillships, P&A rigs | PSV drilling-support days; AHTS rig-move and mooring days |
| Rig operator demand (prospects → tenders → awards) and Petrobras drilling plan | Timing of new vessel demand and tenders |
| Oil/rig catalysts and timing | Which campaigns and FIDs move, and with what lag |
| Disruptions and war zones | Operational line per region; vessel migration away from or towards affected regions |

**Step 2 — Market observation.** Latest complete month as anchor, latest weekly data as trend:
- **North Sea:** spot average and spot utilization per class (named broker series), number of
  vessels in the spot pool, laid-up, arrivals and departures, term fixtures. Compare with the same
  month in prior years (seasonality) and with the previous baseline.
- **Brazil:** Petrobras tenders open and closed, awards (vessel, class, flag, term, rate, start),
  vessels under contract per type, vessels idle or leaving, Brazilian vs foreign flag.
- **Guyana/Suriname:** vessels on contract, new awards, FPSO and drilling schedule.
- **Global context:** active and laid-up fleet, orderbook, global utilization and regional
  averages (e.g. Tidewater), migration flows into or out of the focus regions.

**Step 3 — Fixtures and leading-edge.** Log every new fixture or award: vessel, class/spec, region,
charterer, announcement date, start, firm term, options, rate and currency, scope, source, grade
A–D. Mark spot vs term. For converted contract values, show vessels, firm calendar days, date
convention, options, escalation and services. Per row: leading-edge median, range and n over six
months, and the 6–12 month trend. Selective and late publication means no new fixtures is not
"unchanged".

**Step 4 — Contract cover.** From owner fleet lists and announcements (DOF, Solstad, Tidewater,
Havila, Eidesvik, OceanPact, CBO, Paratus/Seagems and other owners — ownership as checked in
Step 0), build vessel-by-vessel availability per window year for the term, Brazil, RSV, PLSV and
CSV rows: expiries, options (with exercise probability), idle gaps, drydock/SPS, mobilisation,
migration. Aggregate to cover per row and year. For the North Sea spot rows, record the spot-pool
size and how much of the class is on term. Where cover cannot be built, say so: the spread is
then judgement and labelled `[A]`.

**Step 5 — Demand in vessel-days.** Per region and year, separate **prospect → tender → award →
binding contract → start-up**, and split secured, open and unsanctioned demand. Build demand legs:
- **PSV:** rig-days (from the rig baseline) × documented PSVs per rig for that region and rig type,
  plus production support (installations/FPSOs × documented ratio), plus decommissioning and other
  supply work. Confirm rig-days vs rig-years before converting.
- **AHTS:** rig moves of moored units (number × qualified vessels × days), FPSO and floating-wind
  mooring campaigns, towing and project work. AHTS demand is not a constant factor per working rig;
  DP drillships need little AHTS support.
- **CSV/IMR, RSV, PLSV:** project and service days from subsea awards, IMR frame agreements, well
  hook-ups (Petrobras flexible-line connections per FPSO), decommissioning, and offshore wind
  campaigns that compete for the same vessels.
- Every ratio (vessels per rig, per FPSO, per rig move) is calibrated from observed regional data,
  sourced and tagged; recalibrate when the input mix changes. The same campaign is counted once.

**Step 6 — Supply.** One fleet register per row and region with vessel ID, class/spec, owner, flag,
age, status (working, idle, warm/cold laid-up, under construction), contract, operational date and
source. Per row and year: **nominal → probable → qualified/effective**.

```
qualified fleet start + newbuild deliveries + reactivations − attrition (scrapping, sold out of oil & gas)
  ± conversions (to/from wind, other use) + arrivals − departures = qualified fleet end
effective capacity = qualified fleet × days − drydock/SPS − mobilisation/transit − partial-year effects
```

- For each material newbuild or reactivation: **cost and payment timing → financing (secured or
  assumed) and yard work → delivery and mobilisation → qualified capacity from a stated date**.
  Options and pipeline orders are separate conditional additions to the firm delivery schedule.
  Split Brazil programmes by actual vessel type and reconcile programme totals with single
  contracts.
- **Capital cycle:** secondhand values → newbuild parity → available capital → newbuild economics →
  actual orders. State which project economics were tested (price, term, rate, financing) and
  whether today's rates and contract lengths trigger orders or reactivations; test the reverse
  (would a fall trigger lay-ups and scrapping?).
- Attrition matters: an ageing fleet with a small orderbook shrinks unless rates justify
  replacement. State the age profile (e.g. share > 20 years) per core row.
- Migration is the fastest supply response for the North Sea spot pool: track vessels moving to and
  from Brazil, West Africa, the Mediterranean, the Middle East and offshore wind.

**Step 7 — Balance check.** Per row, scenario and year: demand (vessel-days) vs effective capacity →
implied utilization, compared with cover from Step 4 and with the observed series. Reconcile: Σ
regional fleets = global fleet per class at start and end where the data allows; migration nets to
zero; no delivery or reactivation counted twice. A rising rate with a loosening balance, or the
reverse, must be explained or adjusted. Build the region × segment matrix for material cells only;
mark the rest "not assessed".

**Step 8 — Anchors and asset values.** Per core row:
- **Cash breakeven floor:** vessel opex per day for the class and region (owner reports; Brazilian
  and Norwegian crewing differ) — where rates settle in deep surplus; below it vessels lay up.
- **Reactivation parity:** the rate that pays opex plus reactivation cost (incl. SPS) over the
  typical first firm term at 8% nominal (convention; state cost, term and lead time). It caps the
  rate while laid-up qualified tonnage of the class exists.
- **Newbuild parity:** the rate that pays opex plus an annuity on the newbuild price over 25 years
  at 8% nominal (convention), net of scrap, at a stated utilization. Test whether an order placed now
  could deliver inside the window, and whether Brazilian-built or flag requirements change it.
- **Asset values:** newbuild price and lead time, recent secondhand transactions (price, age, spec,
  date, buyer), reactivation cost, scrap value. **Asset-implied rate:** the rate a recent
  transaction capitalises over the vessel's remaining life at the same 8% and a stated utilization.

**Step 9 — Test BBB.**
- **Base:** what would have to be true for Base to be wrong, and do we see it? Search actively for
  exactly that (pre-mortem). Is it still the most likely path? Where Base differs from owner
  guidance, state why.
- **Bear / Bull:** are the catalysts still the right ones? Has one come closer, been triggered, or
  become irrelevant? Has a signpost been crossed? Is a demand or supply catalyst missing? Have the
  North Sea and Brazil diverged?
- **Evidence threshold:** change a scenario, catalyst or path only when several independent data
  points point the same way, or one event materially changes vessel-day demand, effective supply or
  cover — and only by more than the minimum change.
- Record market event, re-publication of an older observation, correction and method change
  separately. Explain unchanged load-bearing assumptions and persistent data gaps.

**Step 10 — Set the paths.**
- **Rate and utilization (or cover)** per core row and scenario: stub, each year, 3-year average and
  mid-cycle, as point value + range. Build each in three layers: (a) contract cover as the anchor,
  (b) the balance for the uncovered share, (c) the rate as a function of tightness, bounded by the
  cash floor and reactivation (or newbuild) parity, and checked against the latest fixtures. Show the
  bridge from the dated anchor fixture to the estimate (currency/scope adjustment, spec premium or
  discount, spot/term mix, supply response, chosen term). No standing premium and no automatic annual
  rate growth.
- **North Sea spot rows:** annual time-weighted average plus the Year-1 by-quarter table; state the
  seasonal factors and the years they come from.
- **Stub:** identical across scenarios (see Standing parameters).
- **Secondary rows:** Base point + range (Bear/Bull when used by a company analysis), with confidence.
- **Mid-cycle** (for IAF terminal values at exit) is set separately from the annual path: the
  normalised rate and utilization after the window, per scenario. Anchor on the long-run average for
  the row (state the years, with and without the 2012–2014 peak and the 2015–2021 trough), the cash
  floor, reactivation parity and newbuild parity, and the fleet age at exit. A complete monthly
  report or a chosen Base rate alone does not establish a through-cycle level. Show an alternative
  anchor when the choice is decisive for the receiving company analysis.
- **Asset values at mid-cycle** per scenario (vessel of typical age for the row and newbuild/
  replacement cost), consistent with the mid-cycle rate (asset-implied rate ≈ mid-cycle rate). The
  company analysis adjusts for its own vessels' age and spec.

**Step 11 — Write, log and check.** Write the document in the output format, with a complete
change log (new / unchanged / changed with previous → new value, reason and source; forecast vs
actual; weights kept or changed; whether IAF analyses should update). Read it back and run the
checks below.

## Recalibration triggers

A full update is due when any of these occurs:

- `docs/oil-market-bbb.md` or `docs/rig-market-bbb.md` gets a new baseline whose downstream section
  flags a supply-relevant change (Brent long end or mid-cycle, rig activity in NCS/UK/Brazil/Guyana,
  Petrobras drilling plan, disruptions)
- A North Sea spot quarter averages > 15% away from the Base quarter, or spot utilization > 5 pp away
- A term fixture or Petrobras award in a core row is > 10% away from the Base rate for its start year
- A Petrobras Strategic Plan or a large Petrobras tender (PSV, AHTS, RSV, PLSV, OSRV) is published,
  awarded, cancelled or re-scoped
- ≥ 3 newbuild orders in a core class, or a laid-up group reactivated against contracts
- A net move of ≥ 3 large PSVs or AHTS into or out of the North Sea spot pool within a quarter
- A merger or fleet sale changes ownership for a covered owner
- A strike, force majeure or regulatory stop takes vessels off hire in a focus region
- A Bear or Bull catalyst is triggered or a signpost is crossed
- The baseline is older than 30 days

## Output: `docs/supply-market-bbb.md`

Keep the main part short per heading; fixtures, fleet registers, cover and source details go to the
appendix.

```markdown
# Supply Market BBB — [baseline date]

## Metadata
- Analysis date (Europe/Oslo), information cut-off, status (Initial / Final / Provisional and why)
- Skill revisions used (supply-market-bbb, iaf-valuation)
- Previous baseline (date, days), window (stub + 2027–2029), stale after [date]
- Oil Market BBB and Rig Market BBB used (baseline date, status, stale-after date)
- Series used per row (broker, Petrobras, named-fleet cover); any series change since last baseline
- FX rates used for conversions (pair, rate, source, time)

## Conclusion
- BBB changed / kept unchanged — explicit
- Base in two sentences (North Sea; South America)
- Row ranking (strongest → weakest) with the main reason
- Main Bear catalyst and main Bull catalyst

## Interface — rates, k/day (point values; ranges below). North Sea GBP, South America USD
| Row Bear / Base / Bull | Currency | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|---|
| NS large PSV — spot | GBP | | | | | |
| NS large PSV — term | GBP | | | | | |
| NS AHTS — spot | GBP | | | | | |
| NS subsea / CSV-IMR (vessel only) | GBP | | | | | |
| Brazil PSV | USD | | | | | |
| Brazil AHTS | USD | | | | | |
| Brazil RSV (vessel + ROV) | USD | | | | | |
| Brazil PLSV | USD | | | | | |
| Secondary rows (Base, or B/B/B where used) | | | | | | |

## Interface — utilization / cover, % annual average
| Row Bear / Base / Bull | Series | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|---|

## Year 1 by quarter — North Sea spot (GBP k/day; utilization %)
| Row | Scenario | Q1-27 | Q2-27 | Q3-27 | Q4-27 | Year avg | Seasonal factors (years used) |
|---|---|---|---|---|---|---|---|

## Interface — asset values and anchors
| Row | Newbuild $m, lead time | Secondhand $m (age, date) | Reactivation $m, lead time | Value mid-cycle Bear / Base / Bull $m | Cash floor k/d | Reactivation parity k/d | Newbuild parity k/d |
|---|---|---|---|---|---|---|---|

## Scenario definitions
| Scenario | Weight (convention) | Oil BBB scenario | Rig BBB scenario | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|---|
| Bear | 25% | | | | | | |
| Base | 50% | | | | | | |
| Bull | 25% | | | | | | |

## Paths per row — utilization % / rate k/day, point (range)
| Scenario | Row | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|
- Contract cover per row and year (the reason for the spread)
- Anchor-to-estimate rate bridge per core row
- Base vs owner guidance

## Market check
| Row | Utilization latest (month, series) | Leading-edge median / range / n (6 mo) | Trend 6–12 mo | Cover 2027 / 28 / 29 | Base 2027 vs leading-edge |
|---|---|---|---|---|---|
- Anchors: cash floor, reactivation parity, newbuild parity, asset-implied rate

## Drivers
### Oil and rig input and translation (scenario mapping; operational line per region)
### Demand in vessel-days (North Sea: NCS / UK; Brazil; Guyana/Suriname; secured / open / unsanctioned)
### Supply (fleet bridge per row: deliveries, reactivations, attrition, conversions, migration; age profile)
### Capital cycle (secondhand → newbuild parity → capital → orders)
### Region × segment matrix (material cells)
### Global context (migration source/sink, orderbook, regional averages)
### Balance check (demand vs effective capacity vs cover, per row, scenario and year)

## Signposts and monitoring
| Signpost | Threshold (Bear / Bull) | Now | Previous | Direction |
|---|---|---|---|---|
- Open checkpoints and data gaps (carried / closed) and the next decisive observation

## For IAF
- What changed that OSV-owner analyses must take in, or "no material change"
- Per covered owner: rows to use, mark-to-market gap where data exists

## Change log
- New / unchanged / changed (previous → new, reason, source)
- Forecast vs actual for the realised or partly observed year
- Weights kept or changed — explicit
- New baseline date

## Appendix
### Fixture and award log (vessel, class, region, charterer, start, term, rate, currency, scope, grade, source)
### Fleet register, newbuilds and reactivations (vessel ID, class, owner, flag, status, date, source)
### Vessel-by-vessel availability and cover
### Sources
| ID | Source | Content | Definition / universe | Observed / published |
|---|---|---|---|---|
```

## Interface to IAF

Every baseline delivers, in the fixed Interface tables and the sections behind them:

- Rate and utilization (or cover) point values per row and scenario for the stub, each year and
  mid-cycle; ranges; North Sea spot by quarter for Year 1; secondary rows with confidence.
- Vessel values now and at mid-cycle, and the anchors (cash floor, reactivation parity, newbuild
  parity).
- Demand, supply, cover and the balance per scenario; catalysts, signposts and status.

Use in [[iaf-valuation]] (OSV and subsea-vessel owners, Track B):

**Vessel/spec → region and qualification → contract and service scope → exposed period → relevant
rate and payable days → cost and capacity risk.**

- **Stub and Year-1 quarters:** booked days and rates come from the company's own fleet and contract
  lists. Only **open** days are priced at the market: North Sea spot-exposed vessels at the quarterly
  spot path × the row's utilization (paid days), term-exposed vessels at the leading-edge term rate,
  with idle time between contracts set per vessel by the company analysis.
- **Years 2–3:** Base path as the decision case; Bear/Bull paths as the catalyst stress tests.
  Re-pricing follows contract expiries: a vessel earns its contract rate until expiry, then the
  row's rate for that year. Start-up, gaps, mobilisation, escalation and technical offhire are dated
  so paid days and service content are counted once.
- **Terminal value V_T:** NAV of the fleet from mid-cycle vessel values, adjusted for each vessel's
  age and spec at exit, or mid-cycle rate × mid-cycle utilization × days − normalised opex.
- **Growth capex (ROIC_g):** newbuilds, reactivations and acquisitions are tested against newbuild
  and reactivation parity, recent secondhand prices and the contract rate actually secured.
- **Company notes:**
  - **DOF:** separate PSV/AHTS, CSV and integrated subsea/RSV/EPCI packages. A gross project value
    is not a vessel rate. Newbuild payments and start-ups are delivered even beyond the window.
  - **Paratus (Seagems):** use the Brazil PLSV row with comparable technical spec and Petrobras
    tender scope. PSV/AHTS or global OSV utilization never replace the PLSV rate or cover. JV
    ownership and cash to holding are handled in the company analysis.
  - **Solstad, Tidewater and other owners:** map each vessel to the row by class, spec, region and
    flag; Tidewater's regional averages are context, not a substitute for the rows.
- Company-specific growth, economic life and replacement, financing, liquidity, JV/leases,
  ownership share and return follow IAF. Market development alone does not establish them.

## Checks before finishing

- Skill revisions stated; window and stub correct for today's date; Oil and Rig Market BBB baseline
  dates and status stated and not stale (or this baseline marked Provisional).
- No own oil or rig forecast: every oil figure traces to `docs/oil-market-bbb.md`, every rig figure
  to `docs/rig-market-bbb.md`.
- Every utilization figure on its named series and definition; every rate with currency, scope and
  day convention; every number tagged, graded where a fixture, and sourced with dates.
- Stub identical across scenarios; spread follows cover; North Sea Year-1 quarters average to the
  annual value.
- Point value and range for every core-row scenario figure; mid-cycle rate, utilization and vessel
  values set and anchored separately from the annual path; rates inside the floor–parity band or
  the exception explained.
- Fleet bridge holds (deliveries, reactivations, attrition, conversions, migration; migration nets
  to zero; no double counting); balance check consistent with each path.
- Paid days and rates kept apart; no average across currencies, classes or service scopes.
- Bear and Bull each tied to named catalysts with signposts and oil and rig scenarios; no
  probability language.
- Change log complete (previous → new) or explicit "kept unchanged".
- File written, read back, tables render.
