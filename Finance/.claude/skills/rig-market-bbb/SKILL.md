---
name: rig-market-bbb
description: Rig Market BBB — the offshore drilling-rig market baseline for drillships, semisubmersibles and jackups (plus tender-assist where a company analysis needs it). Produces Bear/Base/Bull leading-edge dayrate and marketed utilization paths per segment on the IAF time grid (stub quarter(s) of the current year + 3 calendar years, now 2027–2029), plus mid-cycle dayrates and rig asset values for terminal values, reactivation and newbuild parity, contract cover, operator demand in rig-years, fleet supply (stacked, reactivations, newbuilds, retirements) and named catalysts with signposts. Base is the decision case; Bear and Bull are catalyst-based stress tests; 25/50/25 is a labelled convention, never a probability. Reads the Brent path, long end and mid-cycle from docs/oil-market-bbb.md and never makes its own oil forecast. ALWAYS use when the user mentions Rig Market BBB / Riggmarked BBB / rig BBB, asks to create, run or update ("oppdater modul") the rig module, or asks about rig dayrates, utilization, contract cover, rig availability, stacked or reactivated rigs, rig newbuilds or rig values for drillships, semisubs or jackups (incl. NCS harsh environment) — even without naming the skill. Feeds iaf-valuation for drilling contractors and supply-market-bbb (rig activity for OSV demand).
---

# Rig Market BBB

**Revision:** 2026-10-08.2 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/rig-market-bbb/` in the Finance folder.

A Bear/Base/Bull baseline for the offshore rig market. It answers one question: **what market
dayrates, utilization and rig values should a drilling-contractor valuation use, year by year and
per segment, and what named events would move them?** It is a testable hypothesis with explicit
risks, not a news summary.

It sits between [[oil-market-bbb]] and [[iaf-valuation]]. It takes the oil price path as given from
`docs/oil-market-bbb.md` and translates it into rig demand through this chain:

**Brent path and long end → E&P cash flow → offshore capex and FIDs → rig demand (rig-years) →
utilization → leading-edge dayrate**, modified by **effective rig supply** (stacked, reactivations,
newbuilds, retirements) and **contract cover** (how much of each year is already locked).

**Scope:** leading-edge dayrates, marketed utilization, contract cover at market level, operator
demand, fleet supply, rig values, reactivation and newbuild economics. **Out of scope:** oil price,
supply/demand or inventory forecasts (→ [[oil-market-bbb]]; read only); tankers (→
[[oil-shipping-bbb]]); a company's own backlog, realised rate, revenue efficiency, costs, capex,
debt and valuation (→ [[iaf-valuation]] company analysis); OSVs (→ [[supply-market-bbb]], which
reads this baseline); onshore rigs, liftboats and seismic.

## Standing parameters

- **Time grid = IAF grid:** stub (remaining quarters of the current year) + 3 full calendar years,
  now Q4 2026 + 2027–2029. Roll forward with the first run each January: the first year becomes
  "realised" (forecast vs actual) and a new end year is added. Rolling is not a reset —
  overlapping years are carried over and tested.
- **No Year-1 quarterly shape.** Rig rates are set by term contracts, not a seasonal spot market.
  IAF prices open days in each Year-1 quarter at the Year-1 annual value. Add a quarterly split
  only for a documented seasonal segment (e.g. a winter-restricted region) and mark it `[A]`.
- **Rate basis:** nominal USD k/day, **leading-edge pure dayrate** for a term contract (≥ ~1 year)
  on a comparable rig, starting in the period (see Definitions). Today's crisis-level oil price
  or a single headline fixture is never used as a multi-year assumption.
- **Utilization basis:** **marketed committed utilization (MCU)**, annual average, on one named
  source series per segment (see Definitions and Data sources).
- **Point value + range** for every scenario rate, utilization and value. IAF uses the point value;
  the range shows uncertainty inside the scenario.
- **Base = the decision case.** Bear and Bull are stress tests tied to named catalysts.
  **25/50/25** is a labelled convention for optional weighted figures — never a probability.
- **Stub has no scenario spread** (IAF rule): stub MCU is the latest observed month and the stub
  rate is the leading-edge from the last six months of fixtures, the same in all three scenarios.
  Scenarios diverge from Year 1.
- **Contract cover sets the spread:** Bear–Bull spread is narrow where the year is highly covered
  (normally 2027) and widens towards the end of the window. A spread that does not follow cover
  must be explained.
- **Segments and regions are always separate** — never one blended global rate.
- **Minimum change (convention):** a point value moves only if the evidence moves it by at least
  5% (annual leading-edge rate or asset value) or 2 percentage points (annual MCU). Smaller moves
  are noted, not applied.
- **Staleness:** the baseline is stale after 30 days, or earlier if a recalibration trigger fires
  or `docs/oil-market-bbb.md` gets a newer baseline date whose "For downstream skills" section
  flags a rig-relevant change. IAF treats a stale baseline as provisional.
- Segments, definitions and source series below are fixed. Changing one is a method change and
  goes in the change log.

## Files

- Skill: `.claude/skills/rig-market-bbb/SKILL.md` (this file only, no reference files).
- Input: `docs/oil-market-bbb.md` (read only).
- Output: `docs/rig-market-bbb.md`, one running baseline. Baseline date in the H1. Git holds the
  history, so the previous version is read from the file before it is overwritten.
- Write with Write/Edit, then **read the file back** and check every table and number. An answer
  in the conversation alone is not delivery.

## Segments and regions

| Row | Definition | Utilization series | Role |
|---|---|---|---|
| **UDW drillships** | High-spec 6th/7th-generation drillships (source's Tier-1 / high-spec class) | Westwood drillship MCU (all drillships — proxy; mark it) | Core BBB |
| **HE semis (NCS)** | Harsh-environment semis able to work on the Norwegian shelf (Cat D and equivalent, NCS consent) | No public series: contract cover of the named NCS fleet + Westwood semi MCU as context | Core BBB |
| **Benign semis** | Mid-water and deepwater semis outside harsh environment | Westwood semi MCU is an upper bound (includes HE); set benign below it `[A]` | Core BBB |
| **High-spec jackups** | Modern/premium jackups per source class (typically ≥ 350 ft, built after ~2000) | Westwood jackup MCU + contractor-reported modern-fleet utilization | Core BBB (global composite) |
| Middle East jackups | High-spec jackups working in the Gulf states | Westwood regional committed/working utilization when published | Secondary |
| SE Asia shallow water | High-spec jackups in Malaysia, Indonesia, Thailand, Vietnam, Brunei | Company fleet status | Secondary |
| Tender-assist | Tender barges and semi-tenders (mainly SE Asia, West Africa) | Company fleet status only | Secondary |
| Other | Standard jackups, NCS HE jackups, Tier-2 drillships, UK HE semis | — | Only when a company analysis needs it |

- **Core rows** get full Bear/Base/Bull for MCU and dayrate, ranges and mid-cycle.
- **Secondary rows** get a Base point + range for dayrate (and MCU where a series exists); Bear and
  Bull only when a company analysis uses the row. Confidence is stated on each.
- Add a row when an IAF company analysis needs it and records the gap (e.g. tender-assist for SED,
  SE Asia jackups for Borr). Log the addition as a method change.
- Never transfer a global high-spec jackup rate to standard jackups, tender-assist or NCS HE
  jackups, and never a global HE rate to the NCS. Spec can gate a region (NCS consent and emissions
  rules, NOC requirements in the Middle East): record it when it limits which rigs compete.

**Regions** (one rig = one region, by current or contracted work area; a rig moves when it starts
the new contract): Norway (NCS) · UK and other NW Europe · Mediterranean/North Africa · Middle East
· India · SE Asia · Australia · West Africa · East Africa · Brazil · Other South America (Guyana,
Suriname, Argentina) · US Gulf · Mexico.

Source regions are coarser (Petrodata "NW Europe", "South America"; Baker Hughes "Europe",
"Latin America", "Asia Pacific"). Map them before adding up. Where a region cannot be split, say so
and never construct NCS/UK or Brazil/Guyana figures.

## Definitions and units

| Term | Definition |
|---|---|
| Total fleet | All existing rigs including stacked; excludes units under construction |
| Marketed fleet | Total fleet minus cold-stacked and rigs not offered for work |
| Competitive fleet | Marketed fleet adjusted for spec, regional access and long idle periods |
| Contracted | Rig with a contract in place (incl. mobilising, contracted yard stay, suspended) |
| Working | Actually on hire and operating (Westwood weekly "working") |
| Contracted, not working | Contracted − working: suspensions, force majeure, war-related offhire |
| **MCU** | Contracted ÷ marketed fleet |
| Total utilization | Contracted ÷ total fleet |
| Friction ceiling | Practical maximum MCU (yard stays, SPS, mobilisation, gaps between contracts), below 100%. Tightness shows in rates before MCU reaches it |
| Rig-year | 365 rig-days. Demand in rig-years = wells × days per well ÷ 365, plus mobilisation and gaps |
| **Contract cover** | Firm contracted rig-days ÷ available rig-days of the marketed fleet, per segment and year. Options are counted with a stated exercise probability, never 0/100 by default |
| Dayrate | Pure operating dayrate, excluding mobilisation, services, bonus |
| Contract value per day | Total contract value ÷ firm days; may include mobilisation and services |
| **Leading-edge rate** | Comparable recent term fixtures (same class/spec and region, start within ~12–18 months, firm term ≥ ~1 year): median, range and n |
| Fleet-average backlog rate | Average rate in a contractor's or segment's backlog |
| Mark-to-market gap | Leading-edge − fleet-average backlog rate; the bridge into the company analysis |

- Short (well-to-well, < ~6 months) and term contracts are reported separately: the term premium
  or discount is itself a signal.
- Utilization reconciliation from counts (Westwood): MCU ≈ contracted ÷ (contracted + marketed
  available); total ≈ contracted ÷ (marketed + cold-stacked). A difference is flagged, not
  corrected.
- Growth rates use the same fleet definition in numerator and denominator.

**Fixture rate confidence:**

| Grade | Meaning |
|---|---|
| A | Dayrate stated by operator, contractor, exchange filing or primary database |
| B | Derived from contract value ÷ firm days (mobilisation or services may distort) |
| C | Estimate from trade press, analyst or other secondary source |
| D | Unknown — tag `[?]`, never guessed |

## Data sources

Primary data beats commentary. Every figure states source, definition, unit and both observation
and publication date. If a connector or page fails, say so and use the next source. Never fill a
gap with an invented number.

| Need | First choice | Fallback / cross-check |
|---|---|---|
| Brent path, long end, mid-cycle, disruptions | **`docs/oil-market-bbb.md`** (Interface + "For downstream skills") | — never a connector or own estimate |
| MCU, total utilization, marketed available, cold-stacked, backlog in rig-years, monthly fixtures | **Westwood Offshore Energy Data Dashboard** (monthly, RigLogix extract) | Contractor fleet-utilization statements `[E]` |
| Working rig count (weekly trend) | Westwood Weekly Global Offshore Rig Count | Baker Hughes Worldwide Rig Count (direction by country only) |
| Contracted rigs by region and type (weekly) | S&P Global Petrodata Weekly Offshore Rig Count | — |
| Brazil demand | Westwood Brazil Offshore Rig Count (monthly; operating rigs, outstanding rig-days) | Petrobras plans and tender results |
| Fixtures, rig-by-rig contracts, cover by year | Contractor **fleet status reports** and contract announcements | Westwood dashboard fixtures; trade press `[E]`, grade C |
| Contractor filings — US filers (RIG, VAL, NE, SDRL, BORR) | **FinancialFilings** (`companies_list` → id; `filings_list` newest first; 8-K/6-K exhibits) | SEC EDGAR, company IR |
| Contractor market commentary digest — US listings (RIG, VAL, NE, BORR): utilization outlook, rig-years awarded, open tenders, cover by year, average dayrates, backlog | **Zacks** `get_zacks_research` (dated analyst report), `get_zacks_commentary` | Contractor results release and call transcript |
| Contractor filings — Oslo/Nordic (ODL, ENH, BORR, SHLF and similar) | **Nordic Financial** `search_filings`/`company_research` with `ticker` + `fiscal_year` | FinancialFilings, company IR |
| Operator plans, tenders, FIDs, consents | Operators (Petrobras, Equinor, Aker BP, Aramco, ADNOC, PTTEP, Petronas, ONGC, majors); Sokkeldirektoratet/Havtil; ANP | Trade press |
| Offshore capex / EPC and FID pipeline | Westwood, Rystad, company capex guidance `[E]` | Trade press |
| Rig values, reactivation and newbuild cost | Rig sale and purchase announcements (price, age, spec, date); contractor reactivation guidance | Esgian/Bassoe/VesselsValue via press `[E]` |
| Trade press | Offshore mag, Offshore Energy, Splash247, Drilling Contractor, Upstream, World Oil, Deepwater Insight, Reuters | Analyst newsletters — `[E]`, grade C, never sole evidence for a rate |

Quirks (observed in the 2026-09-29 run):

- **Westwood dashboard** lags 4–8 weeks (July data published 25 Aug). It has no regional split and
  no Tier-1/HE/benign split. The backlog series broke in Jan 2026 (Dec → Jan values inconsistent):
  check for series breaks before reading month-on-month changes. Jackup MCU did not reconcile with
  the counts (381/(381+47) = 89% vs 87% reported); floater figures did.
- **Westwood weekly** counts working rigs, not utilization; regional charts are images.
- **Petrodata weekly** tables load dynamically and did not come through a fetch: mark "not read"
  and ask the user for a screenshot or the figures. Counts only, coarse regions, its own series.
- **Baker Hughes** "active" is narrower (drilling most of the week) and excludes Russia, Caspian,
  Iran and onshore China; Saudi method change Jan 2024. Its offshore level (~230–240) is less than
  half of Westwood working (~510): **levels are not comparable**, use direction only.
- **Fleet status reports** are as-of a date that can lag a quarter, and many contracts are
  announced without a rate. Selective disclosure means known rates are not a representative sample.
- **Zacks** (tested 2026-10-08): a full analyst report exists only for some names (RIG yes;
  VAL, NE and BORR have only quantitative reports). The RIG report of 22 Sep 2026 carried
  management's view (high-spec utilization >90% in 2027; ~100 rig-years awarded in H1 2026; ~40
  open tenders for 75–80 rig-years; Brazil 30–33 rigs; Africa 20–25). That is contractor
  commentary relayed by Zacks: tag `[E]`, grade C, cite the publish date, use it for signposts and
  cross-checks, never as sole evidence for MCU or a rate. Its consensus has 1–6 estimates per
  name and is not a market check on the rig paths.
- Paid databases (RigLogix, Petrodata Rigs, Clarksons, Bassoe) are not assumed available.
- Expect 20+ searches and fetches for a full run: monthly and weekly dashboards first, then
  contractors, then operators.
- Do not use SEO "market report" pages without a traceable primary source (rejected example:
  $180–220k for HE jackups with no source). When sources conflict, give both and say which one is
  used and why.

## Data discipline

- Tag every number: `[F]` reported fact · `[E]` external forecast or secondary claim · `[A]` own
  assumption · `[?]` unknown. Missing new fixtures or data are not evidence that nothing changed.
- For each finding: (1) the fact, (2) what it means physically (rig-years of demand, rigs added to
  or removed from the competitive fleet, cover), (3) whether it changes the model. One regional
  contract or one tender does not move the global model without a stated reason.
- **One series = one source.** Westwood MCU, Petrodata "marketed contracted" and Baker Hughes
  "active" measure different things: never mix them in a series or use one to correct another.
  If a source changes, document it and show both values for one overlapping date.
- **Never double count:** a rig is not a newbuild, a reactivation and part of the marketed fleet at
  once. Relocation adds to one region and subtracts from another. Mergers and ownership changes
  create no rigs.
- **Activity ≠ pricing power:** utilization can rise while aggressive bids hold rates down (e.g.
  jackups replacing tender-assist in Thailand).
- **Management guidance is `[E]`.** Contractors talk their book; Base is set from cover, tenders and
  fixtures, and the gap to guidance is stated.
- n < 3 comparable term fixtures in six months → give a range and "low confidence", not a point.
- Known weak data: NCS HE and NCS HE jackups (few fixtures a year), segment splits (no public
  Tier-1/HE/benign series), contract cover (built by hand), stranded newbuilds (dated census data),
  contracted-but-suspended rigs hiding lower real activity.
- **User input is input, not a reference.** Links, numbers and drafts are assessed critically (what
  it measures, how fresh, which definition); use what holds, reject the rest, and note the
  assessment in the source appendix.

## Scenarios

There is no statistical distribution behind FIDs, wars or reactivation waves, so Bear and Bull are
not percentiles.

- **Base:** the most likely path, and the decision case in IAF.
- **Bear / Bull:** the worst and best reasonably foreseeable paths for rig earnings, each tied to
  **named catalysts** with mechanism, earliest timing and **signposts**. They need not be
  symmetric, and floaters and jackups may get different catalysts.
- **Built on the oil baseline.** Each rig scenario names the [[oil-market-bbb]] scenario it uses.
  The mapping is not one-to-one:
  - **Lags.** Rig demand follows expected and mid-cycle oil prices, not spot, with 6–18 months
    (exploration) to 1–3 years (deepwater development). Year 1 is mostly set by backlog; the last
    year depends on FIDs taken now.
  - **Price sensitivity differs.** Sanctioned developments and NOC programmes (Aramco, ADNOC,
    QatarEnergy, Petrobras, PTTEP) are policy-driven and less price-sensitive; future FIDs and
    exploration are price-sensitive.
  - **Supply response caps the upside:** high rates bring reactivations and, later, newbuilds, so
    high oil does not automatically give rig Bull.
  - **Operational geopolitics is separate:** high oil can coincide with evacuation, force majeure,
    suspension and offhire in a region (Middle East). Assess the oil-price effect and the
    operational effect as two lines.
  - A rig catalyst (reactivation wave, consolidation, a programme cancelled) can be combined with
    oil Base. If a scenario needs an oil path the oil baseline does not have, flag it for
    [[oil-market-bbb]] — never invent one here.
- Consider both a **demand** catalyst (FIDs, tenders, NOC programmes, P&A) and a **supply**
  catalyst (reactivations, stranded newbuilds delivered, rigs relocating from a weak region,
  retirements) for each tail.
- **Rates respond non-linearly:** near the friction ceiling small demand changes move rates a lot;
  in surplus rates sink towards cash breakeven. Reactivation parity is the practical ceiling while
  cold-stacked rigs exist; newbuild parity only once they are gone.

## Procedure

Two modes, one procedure:

- **Initiate** — "create Rig Market BBB", "new rig baseline", or automatically when
  `docs/rig-market-bbb.md` does not exist. Full research on every step; status "Initial baseline";
  no change log values.
- **Update** — "update Rig Market BBB", "oppdater modul" in a rig context, or a recalibration
  trigger. Run every step in order; it is not a menu.

> Updating does not mean "summarise the latest rig news". It means new, thorough research that
> tests whether the current baseline is still right. Start from the last baseline but do not
> anchor on it: every run actively tries to falsify Base. If the evidence is not strong enough to
> change the model, say so explicitly: **Rig Market BBB kept unchanged.**

**Step 0 — Setup.** State the revision of this skill. Note analysis date, previous baseline date
and days since. Roll the window if this is the first run in a new year. Read the previous
`docs/rig-market-bbb.md` and record its point values, catalysts, signposts and open checkpoints —
they become the "previous" column in the change log, and every open checkpoint is closed or
carried with a new status. If the previous file uses another structure, language or series,
migrate it and log the migration. Check **current rig ownership** (mergers, acquisitions, renames,
rigs sold, recycled or converted) before using any fleet list.

**Step 1 — Oil input.** Read `docs/oil-market-bbb.md`: baseline date, status and "stale after"
date, Interface table (Brent per scenario and year, mid-cycle, forward curve), scenario
definitions, disruption status and "For downstream skills". If it is stale or older than the latest
material oil event, say so, mark this baseline **Provisional**, and get the oil baseline updated
**first**. Translate, do not re-analyse:

| Oil input | Rig effect |
|---|---|
| Brent path per scenario, long end, mid-cycle | E&P cash flow and FID economics vs project breakevens (use long end and mid-cycle, not spot) |
| Bear/Bull catalysts and timing | Which FIDs and exploration campaigns move, and with what lag |
| Disruptions and war zones | Operational line per region: suspensions, force majeure, evacuation, tenders deferred |
| Energy-security policy (strategic stocks, domestic gas) | NOC programmes and gas developments (SE Asia, Middle East, Norway) |

**Step 2 — Utilization and fleet status.** From the Westwood dashboard (latest complete month,
anchor), the weekly counts (fresh trend) and Petrodata (regional contracted counts): per class,
total fleet, marketed, contracted, working, contracted-not-working, marketed available,
warm/cold-stacked, under construction, backlog in rig-years. Reproduce MCU from the counts and
flag differences. Check for series breaks. Note the friction ceiling. Compare with the previous
baseline.

**Step 3 — Fixtures and leading-edge.** Log every new fixture: rig, class/spec, region, operator,
announcement date, start, firm term, options, rate, source, grade A–D. Mark short vs term. Per core
and secondary row: leading-edge median, range and n over six months, and the 6–12 month trend.
Selective and late publication means no new fixtures is not "unchanged".

**Step 4 — Contract cover.** From fleet status reports of the main contractors (Transocean,
Valaris, Noble, Seadrill, Odfjell, Borr, ADES/Shelf, Saipem and regional owners — ownership as
checked in Step 0), build rig-by-rig availability for each window year: contract expiries, options (with
exercise probability), idle gaps, yard stays (SPS, upgrades), mobilisation, relocation. Aggregate
to cover per segment and year. Where cover cannot be built, say so: the spread is then judgement
and is labelled `[A]`.

**Step 5 — Operator demand.** Per region, separate **prospects → tenders → awards → work under
way**, and decompose into development/infill (sanctioned), exploration, NOC programmes and plug &
abandonment. Convert to rig-years where possible (assumptions explicit); a discovery or a new well
count is not automatically a rig contract. Note concentration (e.g. Petrobras as the dominant
drillship buyer) and counterparty risk (e.g. Pemex payments).

**Step 6 — Supply.** Per segment and year: **nominal → probable → competitive**.

```
marketed fleet start + reactivations + newbuild/stranded deliveries − retirements ± relocations = marketed fleet end
net effective change = change in competitive fleet / competitive fleet start
```

Assess each candidate unit (financing, spec and regional access, completion or reactivation cost,
contract in hand, time to start). Cold-stacked or unfinished units are not supply until they have
a contract or a funded plan. Test both directions: does today's rate trigger reactivations or
orders, and would a fall trigger retirements?

**Step 7 — Balance check.** Per segment, scenario and year: demand (rig-years) vs competitive
supply → implied MCU, compared with cover from Step 4. Reconcile: Σ regional fleets = global fleet
per segment at start and end; relocations net to zero; Σ regional demand ≤ global competitive
capacity. A rising rate with a loosening balance, or the reverse, must be explained or adjusted.
Build the region × segment matrix for material cells only; mark the rest "not assessed".

**Step 8 — Anchors and asset values.** Per core segment:
- **Cash breakeven floor:** rig opex per day (from contractor reports) — where rates settle in a
  deep surplus; below it rigs are stacked.
- **Reactivation parity:** the rate that pays opex plus the reactivation cost over the typical
  first firm term at 8% nominal (convention; state cost, term and lead time). It caps the rate
  while cold-stacked units of the class exist.
- **Newbuild parity:** the dayrate at which a newbuild (or stranded-unit completion) is worth its
  price on the asset-value convention below, age 0, at 92% MCU. Test whether an order placed now
  could deliver inside the window.
- **Asset values:** newbuild/completion price, recent secondhand transactions ($m per rig, age,
  spec, date, buyer), reactivation cost, recycling value. **Asset-implied rate:** the dayrate at
  which the convention below reproduces a transaction price (same age and MCU).

**Asset-value convention (one method).** Every rig value in this baseline uses it: mid-cycle
values, values by age, asset-implied rates and newbuild parity. Every IAF drilling-contractor
analysis uses it for V_T, NAV_0 and market marks. It values the rig as a buyer would: rig-level
free cash flow before corporate G&A and financing.

```
Annual cash flow = 365 × [ MCU × (rate × RE − opex) − (1 − MCU) × idle × opex ]
                   − tax × (rate × RE × 365 × MCU) − maintenance capex
Value            = annual cash flow × annuity(8%, 30 − age), floored at the recycling/stacking value
```

- **rate, MCU:** the scenario's mid-cycle (or the rate being tested), flat in nominal terms; MCU is
  used as the working share.
- **Parameters per segment** (RE = revenue efficiency; idle = idle-day cost as a share of opex;
  maintenance capex includes SPS, annualised). Keep them in the document's parameter table with
  sources; change them only with evidence, logged as a method change:

| Segment | Opex $k/d | RE | Idle | Maint. capex $m/yr | Tax % revenue | Floor $m |
|---|---|---|---|---|---|---|
| Floaters (drillships, semis) | segment cash floor (225; HE 250) | 95% (HE 96%) | 40% | 6 (benign semis 5) | 5% | 10 |
| High-spec jackups | 75 | 96% | 40% | 2.5 | 4.5% | 10 |
| Tender barges / semi-tenders | 35 / 40 | 98% | 40% | 3.0 / 3.5 | 6.4% | 10 |

- **Life 30 years, discount 8% nominal** (unchanged conventions). Show 35-year life and opex ±10%
  as sensitivities for each core segment: margins are thin, so values are very sensitive to opex.
- **Excluded:** corporate G&A, financing, working capital. The company analysis carries these in
  its cash flows; it may show capitalised G&A as a sensitivity on V_T, never in the base figure.
- **Company adjustments** (IAF): age always; a spec premium or discount on the rate, or own opex,
  maintenance capex or tax, only where sourced in the company analysis. Never mix this convention
  with a gross-margin capitalisation ((rate − opex) × 365 × MCU × annuity), which ignores idle
  cost, maintenance capex and tax and overstates values by ~1.5–2.5x at Base mid-cycle.
- **Market check (required):** the asset-implied rate of each recent transaction against the
  segment's Base mid-cycle rate. A gap > 10% is stated in the Market check and carried as an open
  checkpoint; it is evidence for the next mid-cycle review, not an automatic change. IAF analyses
  then show V_T at transaction-implied marks as a sensitivity.

**Step 9 — Test BBB.**
- **Base:** what would have to be true for Base to be wrong, and do we see it? Search actively for
  exactly that (pre-mortem). Is it still the most likely path? Where Base differs from management
  guidance, state why.
- **Bear / Bull:** are the catalysts still the right ones? Has one come closer, been triggered, or
  become irrelevant? Has a signpost been crossed? Is a demand or supply catalyst missing? Have
  floaters and jackups diverged?
- **Evidence threshold:** change a scenario, catalyst or path only when several independent data
  points point the same way, or one event materially changes demand in rig-years, competitive
  supply or cover — and only by more than the minimum change.

**Step 10 — Set the paths.**
- **MCU and leading-edge rate** per core segment and scenario: stub, each year, 3-year average and
  mid-cycle, as point value + range. Build each in three layers: (a) contract cover as the anchor,
  (b) the balance for the uncovered share, (c) the rate as a function of tightness, bounded by the
  cash breakeven floor and reactivation (or newbuild) parity, and checked against the latest
  fixtures.
- **Stub:** latest observed MCU and the six-month leading-edge, identical across scenarios.
- **Secondary rows:** Base point + range (Bear/Bull when used by a company analysis), with
  confidence.
- **Mid-cycle** (used for IAF terminal values at exit): the normalised rate and MCU after the
  window, per scenario. Anchor on the long-run leading-edge for the segment (state the years, with
  and without the 2014 peak and the 2016–2021 trough), the cash floor and reactivation parity, and
  the fleet age at exit — never the last modelled year by default.
- **Asset values at mid-cycle** per scenario on the asset-value convention (Step 8): a rig of
  typical age for the segment, plus a values-by-age table (5, 10, 12, 15, 20 years) for each core
  segment so IAF can read values for its own fleet. Compare with newbuild/replacement cost and the
  transaction market check. The company analysis adjusts for its own rigs' age and spec.

**Step 11 — Write, log and check.** Write the document in the output format, with a complete
change log (new / unchanged / changed with previous → new value, reason and source; forecast vs
actual; weights kept or changed; whether IAF analyses should update). Read it back and run the
checks below.

## Recalibration triggers

A full update is due when any of these occurs:

- `docs/oil-market-bbb.md` gets a new baseline whose "For downstream skills" section flags a
  rig-relevant change (Brent path, long end, mid-cycle, disruptions)
- MCU of a core segment moves > 3 percentage points from the baseline's latest observation
- A term fixture in a core segment is > 10% away from the Base rate for its start year
- ≥ 2 high-spec floater orders, or a cold-stacked or stranded unit reactivated against a contract
- An operator defers or cancels a multi-year programme, or awards one (Petrobras, Aramco, Equinor,
  ADNOC, PTTEP and similar)
- A merger or acquisition changes rig ownership for a covered contractor
- A war or force majeure puts a region's rigs offhire or suspended
- A Bear or Bull catalyst is triggered or a signpost is crossed
- The baseline is older than 30 days

## Output: `docs/rig-market-bbb.md`

Keep the main part short per heading; fixtures, rig-by-rig cover and source details go to the
appendix.

```markdown
# Rig Market BBB — [baseline date]

## Metadata
- Analysis date, status (Initial / Final / Provisional and why), skill revision
- Previous baseline (date, days), window (stub + 2027–2029), stale after [date]
- Oil Market BBB used (baseline date, status, stale-after date)
- Series used per segment (Segments section of the skill); any series change since last baseline

## Conclusion
- BBB changed / kept unchanged — explicit
- Base in two sentences (floaters; jackups)
- Segment ranking (strongest → weakest) with the main reason
- Main Bear catalyst and main Bull catalyst

## Interface — leading-edge dayrate, $k/day (point values; ranges below)
| Segment Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| UDW drillships | | | | | |
| HE semis (NCS) | | | | | |
| Benign semis | | | | | |
| High-spec jackups | | | | | |
| Secondary rows (Base, or B/B/B where used) | | | | | |

## Interface — MCU, % annual average
| Segment Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|

## Interface — asset values and anchors
| Segment | Newbuild / completion $m | Secondhand $m (age, date) | Reactivation $m, lead time | Value mid-cycle Bear / Base / Bull $m | Cash floor $k/d | Reactivation parity $k/d | Newbuild parity $k/d |
|---|---|---|---|---|---|---|---|
- Asset-value convention: parameter table (with sources), values by age per core segment and
  scenario, sensitivities (35-year life, opex ±10%), transaction market check (asset-implied rate
  vs Base mid-cycle)

## Scenario definitions
| Scenario | Weight (convention) | Oil BBB scenario used | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|
| Bear | 25% | | | | | |
| Base | 50% | | | | | |
| Bull | 25% | | | | | |

## Paths per segment — MCU % / rate $k/day, point (range)
| Scenario | Segment | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|
- Contract cover per segment and year (the reason for the spread)
- Base vs management guidance

## Market check
| Segment | MCU latest (month) | Leading-edge median / range / n (6 mo) | Trend 6–12 mo | Cover 2027 / 28 / 29 | Base 2027 vs leading-edge |
|---|---|---|---|---|---|
- Anchors: cash floor, reactivation parity, newbuild parity, asset-implied rate

## Drivers
### Oil input and translation (oil scenario mapping; operational geopolitics per region)
### Operator demand (prospects → tenders → awards; rig-years per region)
### Supply (reactivations, stranded and newbuild deliveries, retirements, net effective change)
### Region × segment matrix (material cells)
### Balance check (demand vs competitive supply vs cover, per segment, scenario and year)

## Signposts and monitoring
| Signpost | Threshold (Bear / Bull) | Now | Previous | Direction |
|---|---|---|---|---|
- Open checkpoints (carried / closed) and what to watch before the next update

## For IAF
- What changed that drilling-contractor analyses must take in, or "no material change"
- Per covered contractor: rows to use, mark-to-market gap where data exists

## For downstream skills
- [[supply-market-bbb]]: changes in rig activity in Norway (NCS), UK, Brazil and Guyana/Suriname
  (working rigs, rig-years, moored semis vs DP drillships, P&A rigs, Petrobras drilling plan), or
  "no material change"

## Change log
- New / unchanged / changed (previous → new, reason, source)
- Forecast vs actual for the realised or partly observed year
- Weights kept or changed — explicit
- New baseline date

## Appendix
### Fixture log (rig, class, region, operator, start, term, rate, grade, source)
### Rig-by-rig availability and cover
### Sources
| Source | Content | Definition | Observed / published |
|---|---|---|---|
```

## Interface to IAF

Every baseline delivers, in the fixed Interface tables and the sections behind them:

- Leading-edge dayrate and MCU point values per segment and scenario for the stub, each year and
  mid-cycle; ranges; secondary rows with confidence.
- Asset values now and at mid-cycle, and the anchors (cash floor, reactivation parity, newbuild
  parity).
- Contract cover, operator demand, supply and the balance per scenario; catalysts, signposts and
  status.

Use in [[iaf-valuation]] (drilling contractors, Track B):

- **Stub and Year-1 quarters:** booked days and rates come from the company's own fleet status.
  Only **open** rig-days are priced at the market: leading-edge rate for the rig's row and region,
  with idle time between contracts informed by the segment MCU (the company sets the probability
  for each named rig).
- **Years 2–3:** Base path as the decision case; Bear/Bull paths as the catalyst stress tests.
  Re-pricing follows the company's contract expiries: a rig earns its backlog rate until expiry,
  then the leading-edge rate for that year.
- **Terminal value V_T:** NAV of the fleet from mid-cycle asset values on the asset-value
  convention (Step 8), read from the values-by-age table or recomputed with the same formula and
  parameters for each rig's age and sourced spec at exit. No other value method is used for V_T,
  NAV_0 or market marks; transaction-implied marks are a sensitivity.
- **Growth capex (ROIC_g):** reactivations and rig acquisitions are tested against reactivation
  parity, recent secondhand prices and the contract rate actually secured.
- **Mapping:** match each rig to the right row (class, spec, region). The company's revenue
  efficiency, mobilisation fees, escalation clauses and premium or discount to leading-edge are
  set and sourced in the company analysis.

## Checks before finishing

- Skill revision stated; window and stub correct for today's date; Oil Market BBB baseline date
  and status stated, and not stale (or this baseline marked Provisional).
- No own oil forecast: every oil figure traces to `docs/oil-market-bbb.md`.
- Every utilization figure on its named series and definition; every rate a pure dayrate or
  labelled otherwise; every number tagged, graded where a fixture, and sourced with dates.
- Stub identical across scenarios; spread follows contract cover.
- Point value and range for every core-segment scenario figure; mid-cycle rate, MCU and asset
  values set and anchored; rates inside the floor–parity band or the exception explained.
- Every rig value, asset-implied rate and newbuild parity on the asset-value convention, with the
  parameter table, values by age, sensitivities and the transaction market check shown.
- Fleet reconciliation holds (regions sum to global, no double counting); balance check consistent
  with each path.
- Bear and Bull each tied to named catalysts with signposts and an oil scenario; no probability
  language.
- Change log complete (previous → new) or explicit "kept unchanged".
- File written, read back, tables render.
