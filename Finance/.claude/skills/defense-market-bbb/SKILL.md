---
name: defense-market-bbb
description: Defense Market BBB — the European defense market baseline used to value European defense companies (Rheinmetall, Kongsberg, Saab, Thales, Leonardo, BAE Systems, Hensoldt, Renk, TKMS, CSG, Nammo and others). Tracks defense spending per European country against NATO targets (3.5% core + 1.5% related by 2035), enacted budgets and multi-year plans. Produces Bear/Base/Bull paths on the IAF time grid (current year + 3 calendar years, now 2027–2029, plus a long end to 2035) for core defense spending, equipment spending, the share open to European industry, and order intake and revenue growth per capability segment (land systems, ammunition, air and missile defense and missiles, combat air, naval, C4ISR; drones/counter-drone and services secondary). Also covers industry capacity, margins, a contract award log, and named catalysts with signposts. Base is the decision case; Bear and Bull are catalyst-based stress tests; 25/50/25 is a labelled convention, never a probability. It is the only place a defense spending or defense market forecast is made. ALWAYS use when the user mentions Defense BBB / Defense Market BBB / forsvarsmarked, asks to create, run or update ("oppdater modul") the defense module, or asks about European defense budgets or spending, NATO spending targets, ReArm Europe, SAFE, EDIP, defense procurement, ammunition or missile production capacity, defense order books or the defense sector outlook — even without naming the skill. Feeds iaf-valuation for defense companies.
---

# Defense Market BBB

**Revision:** 2026-10-07.3 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/defense-market-bbb/` in the Finance folder.

A Bear/Base/Bull baseline for the European defense market. It answers one question: **how much
will European states spend on defense equipment, per country and per capability segment, year
by year; how much of it reaches European industry as orders and revenue, at what margins; and
what named events would move it?** It is a testable hypothesis with explicit risks, not a news
summary.

It sits at the top of its own chain, beside [[oil-market-bbb]], and feeds [[iaf-valuation]]
for defense companies. The chain it models has several gaps, and most of the analysis sits in
those gaps:

**Threat and politics → targets (NATO, national law) → budgets (enacted, draft, medium-term
plans) → fiscal capacity → outturn → equipment spending → share to European suppliers →
contract awards (orders) → industry capacity → deliveries (revenue) → margins.**

| Gap | Why it matters |
|---|---|
| Target ≠ budget | The NATO 3.5% target for 2035 is a pledge. Only funded plans count in Base |
| Budget ≠ outturn | Underspending is common (slow procurement, delayed special-fund outflows) |
| Spending ≠ equipment | Personnel, pensions, operations and infrastructure take most of the budget. The equipment share is itself cyclical |
| Equipment ≠ European revenue | US, Korean and Israeli systems take a large share (F-35, Patriot, K2/K9, Arrow) |
| Orders ≠ revenue | Lead times run from months (drones, ammunition once capacity exists) to 5–10 years (naval) |
| Revenue ≠ profit | Fixed-price contracts, ramp-up costs and inflation clauses decide the margin |

**Scope:** defense spending of European NATO allies (excl. Türkiye, shown as a memo) and of
non-NATO EU states (memo); equipment and R&D spending; EU-level instruments (SAFE, EDIP, EDF,
MFF); demand from Ukraine; the share that goes to European suppliers; capability segments; market
order intake, revenue, backlog and margins of the peer group; industry capacity; export markets
outside Europe where covered companies are exposed. **Out of scope:** oil price
([[oil-market-bbb]]; read only, and only for the Gulf export row); Nordic GDP and NIBOR
([[hy-market-bbb]]; read only); one company's own backlog, share, costs, capex, debt and
valuation ([[iaf-valuation]] company analysis); civil aerospace; internal security and police;
the US defense market except as an export row.

## Standing parameters

- **Time grid = IAF grid:** current year + 3 full calendar years, now 2026 + 2027–2029. Roll
  forward with the first run each January: the first year becomes "realised" (forecast vs actual)
  and a new end year is added. Rolling is not a reset.
- **Long end:** 2030 and 2035 points (NATO's target year is 2035), plus a **steady state** after
  the build-up (see Step 10). IAF needs the long end for the growth fade after the window and for
  5-year horizons on steady compounders.
- **The current year has no scenario spread** (IAF rule). For 2026: enacted budgets and the NATO
  2026e estimate; segment orders and revenue from year-to-date actuals plus guidance; the same in
  all three scenarios. Scenarios diverge from 2027.
- **Annual granularity.** Budgets are annual. There is no quarterly shape. Company quarters belong
  to the company analysis.
- **Spending basis:** NATO **core defence expenditure** (the 3.5% guideline definition; payment
  basis). It is converted from national currency to **EUR bn at a fixed reference FX** (ECB rate on
  the baseline date, held for the whole window). Real growth uses NATO's real change. Paths use
  **nominal % of GDP** (NATO T2 current ÷ T5), the measure national plans and budgets use. NATO's
  headline T3 (share of real GDP at 2021 prices) is shown where it differs. FX moves are logged,
  not modelled. The 1.5% "defence and security-related"
  spending is a separate memo line and is never added to core.
- **Equipment basis:** NATO **equipment expenditure** (major equipment + R&D devoted to major
  equipment) = core × NATO equipment share. This is the market the industry sells into.
- **Addressable basis:** equipment spending × **European-supplier share** (Definitions).
- **Segment basis:** market **order intake** and **revenue** per segment, nominal EUR. Shown as
  growth rates and as an index (2026 = 100), never as a company's figure.
- **Point value + range** for every scenario figure. IAF uses the point value; the range shows the
  uncertainty inside the scenario.
- **Base = the decision case.** Bear and Bull are stress tests tied to named catalysts.
  **25/50/25** is a labelled convention for optional weighted figures, never a probability.
- **Spending growth is not revenue growth.** A company's growth is never set equal to a spending
  growth rate. It goes through the equipment share, the European share, the segment allocation,
  lead times and capacity.
- **Minimum change (convention):** a point value moves only if the evidence moves it by at least
  3% (a country's annual spending in EUR) or 0.1 pp of GDP, 2 pp (equipment share), 5 pp
  (European-supplier share), 2 pp (segment growth rate) or 1 pp (segment steady-state margin).
  Smaller moves are noted, not applied.
- **Staleness:** the baseline is stale after **90 days**. Defense demand moves through annual
  budget cycles, but a recalibration trigger (below) makes it stale at once. IAF treats a stale
  baseline as provisional.
- Rows, definitions and source series below are fixed. Changing one is a method change and goes in
  the change log.

## Files

- Skill: `.claude/skills/defense-market-bbb/SKILL.md` (this file only, no reference files).
- Inputs (read only): `docs/hy-market-bbb.md` (Nordic GDP and inflation, for the Nordic % of GDP
  conversions); `docs/oil-market-bbb.md` (only for the Gulf export row); existing defense company
  analyses `docs/*-analysis.md` (company segment mapping and market-share evidence fed back).
- Output: `docs/defense-market-bbb.md`, one running baseline including the **spending tracker**
  per country. The baseline date goes in the H1. Git holds the history, so the previous version is
  read from the file before it is overwritten.
- Write with Write/Edit, then **read the file back** and check every table and number. An answer
  in the conversation alone is not delivery.

## Rows

### Countries (spending tracker)

| Row | Countries | Why | Role |
|---|---|---|---|
| **Germany** | DE | Largest budget; debt-brake exemption; home market of Rheinmetall, Hensoldt, Renk, TKMS, KNDS (DE side) | Core |
| **France** | FR | LPM 2024–2030 (updated 2026); Thales, Dassault, Safran, KNDS (FR side), Naval Group, MBDA | Core |
| **United Kingdom** | UK | Defence Investment Plan (June 2026); BAE, Babcock, QinetiQ, Chemring | Core |
| **Italy** | IT | Leonardo, Fincantieri; fiscal constraint | Core |
| **Poland** | PL | Highest equipment share; large buyer from the US and Korea; SAFE's largest borrower | Core |
| **Spain** | ES | Declined the 5% target; Indra, Navantia | Core |
| **Netherlands** | NL | Large % GDP increase; Damen, Thales NL | Core |
| **Norway** | NO | Long-term plan 2025–2036; Kongsberg and Nammo home market | Core |
| **Sweden** | SE | Saab home market | Core |
| **Denmark** | DK | Acceleration fund; fast ramp-up | Core |
| **Finland** | FI | Patria, Nammo (shared with NO) | Core |
| Baltics | EE, LV, LT (sum of three) | Highest % GDP; ammunition and air defense | Secondary |
| Rest of NATO Europe | BE, CZ, RO, GR, PT, SK, HU, BG, HR, SI, AL, MK, ME, LU (sum) | Remaining European allies | Secondary |
| Türkiye | TR | Mostly domestic industry and a competitor | Memo, outside the European total |
| Non-NATO EU | AT, IE, CY, MT | EDA data only | Memo |
| **Ukraine** | UA | Own budget plus foreign-funded procurement | Separate demand row (see double counting) |
| Export markets | US; Gulf; Asia-Pacific; other | Only for covered companies with exposure (NASAMS, NSM/JSM, Gripen, Rafale, BAE Inc., Rheinmetall US) | Secondary, Base only |

**Europe total** = the core rows + Baltics + Rest of NATO Europe (European allies excl. Türkiye and
Iceland). Never mix it with "NATO Europe and Canada" or with the EDA EU27 total; say which one a
figure is.

### Capability segments

| Row | Content | Order → revenue lag | European suppliers (listed / private) | Main non-European competitors | Role |
|---|---|---|---|---|---|
| **Land systems** | MBT, IFV, wheeled vehicles, self-propelled artillery, trucks, turrets, drivetrains | 2–4 yr | Rheinmetall, BAE (Hägglunds), CSG, Renk, Leonardo (Iveco DV) / KNDS, Patria | Hanwha, Hyundai Rotem, GDLS | Core |
| **Ammunition and energetics** | Artillery, tank, medium-calibre, mortar and small-arms ammunition; propellants, explosives | 0.5–2 yr once capacity exists | Rheinmetall, CSG, Chemring / Nammo, KNDS Ammo, Eurenco, Diehl | Hanwha, Poongsan, US and Turkish producers | Core |
| **Air and missile defense and missiles** | Ground-based air defense, interceptors, cruise and anti-ship missiles, long-range fires | 2–4 yr | Kongsberg, Saab, Thales, Rheinmetall (Skyranger), Hensoldt / MBDA, Diehl | RTX, Lockheed Martin (Patriot, PAC-3, HIMARS, PrSM), IAI/Rafael, Hanwha | Core |
| **Combat air and aerostructures** | Fighters, helicopters, transport and tanker aircraft, F-35 work share, engines | 3–8 yr | Saab, Dassault, Airbus D&S, BAE, Leonardo, Safran, Kongsberg and Rheinmetall (F-35 parts) | Lockheed Martin (F-35), Boeing | Core |
| **Naval** | Submarines, frigates, corvettes, naval systems | 4–10 yr | TKMS, Fincantieri, BAE, Babcock, Saab (Kockums), Kongsberg (naval systems and strike) / Naval Group, Damen, Navantia | Hanwha Ocean, HD HHI | Core |
| **C4ISR, electronics and space** | Radars, sensors, EW, communications, command systems, optronics, satellites | 1–3 yr | Thales, Hensoldt, Leonardo, Saab, Kongsberg, Indra, Theon, Exail, Airbus | L3Harris, Elbit | Core |
| Uncrewed systems and counter-drone | Drones, loitering munitions, C-UAS | 0.25–1 yr | Rheinmetall, Kongsberg, Saab, Thales / Helsing, Quantum Systems, Stark, Tekever | Anduril, Baykar, Ukrainian and Israeli makers | Secondary; watched as a disruptor of other rows |
| Services, MRO and training | Sustainment, maintenance, training, base services | Contract term | Babcock, Leonardo, QinetiQ, Kongsberg, Patria | US primes in Europe | Secondary |

- **Core rows** get full Bear/Base/Bull for order intake and revenue growth, ranges and long end.
  **Secondary rows** get a Base point + range. Bear and Bull are added only when a company
  analysis uses the row. Confidence is stated on each.
- Tier-2 suppliers (Kitron, Renk, Theon, Exail and similar) map to the segments they serve. The
  mapping is shown in the company analysis.
- Add a row when an IAF company analysis needs it and records the gap. Log the addition as a
  method change.
- Never move a country's spending growth straight onto a segment, and never use total spending
  growth as equipment growth. A segment path is always built through Step 5.

## Definitions and units

| Term | Definition |
|---|---|
| **Core defence expenditure** | NATO's definition: payments by national governments to meet the needs of armed forces, incl. pensions and military aid to other countries (Ukraine), per the definition note of each edition. The basis of the 3.5% guideline |
| Defence and security-related spending | The 1.5% guideline: infrastructure, resilience, cyber, civil preparedness, industrial base. Not in NATO's tables (2026 edition). Memo only, never added to core |
| **Equipment expenditure** | NATO Table 8a: major equipment + R&D devoted to major equipment, as a share of core. Payment basis |
| Defence investment (EDA) | Equipment procurement + R&D (EU27). Close to NATO equipment, but its own definition |
| COFOG GF02 (Eurostat) | Defence function in government accounts (ESA 2010, accrual). Weapon systems are recorded **at delivery**, not at payment |
| Prepayment gap | NATO equipment (paid) − COFOG equipment (delivered). A growing gap means advances to industry and a delivery backlog |
| SIPRI military expenditure | SIPRI's own definition, constant 2024 USD. Comparable across countries and over time. Not NATO's definition |
| Target / plan / budget / outturn | Pledge (e.g. 3.5% by 2035) / funded multi-year plan / enacted annual appropriation / money actually spent. Each is its own column, never merged |
| Commitment appropriation | Authority to sign multi-year contracts (Germany: *Verpflichtungsermächtigungen*). A leading indicator for orders |
| **European-supplier share** | Share of equipment spending awarded to suppliers headquartered in Europe (EU, EEA, UK, CH, UA). A US-designed system built in Europe counts only its stated European work share |
| Plan credibility (A–D) | A: law or funded multi-year plan with an exemption or a fund in place. B: funded first years, later years political. C: target without a funded plan. D: opposed, opted out or unfunded |
| **Market order intake** | Firm contract awards to European suppliers in the segment. Frame contracts count only at call-off; the open frame potential is tracked on its own line with an exercise probability |
| Market revenue | Revenue of the segment's European suppliers (peer group) from European and export customers |
| Book-to-bill | Order intake ÷ revenue. Backlog coverage = backlog ÷ next year's revenue |
| Lead time | Months from award to revenue recognition (percentage-of-completion vs delivery) |
| Capacity | Output limit per year in physical units where meaningful (155 mm shells, rockets, missiles, vehicles) |

**Units:** EUR bn nominal at the fixed reference FX; % of GDP on NATO's basis; real growth on
NATO's deflators; segment growth in % per year and as an index (2026 = 100); margins as EBIT % of
revenue.

**Contract grade** (award log):

| Grade | Meaning |
|---|---|
| A | Value stated by the buyer, the supplier or an exchange filing |
| B | Derived (frame ceiling, budget line, value of a 25-Mio-Vorlage) |
| C | Trade press or analyst estimate |
| D | Unknown; tagged `[?]` and never guessed |

## Data sources

Primary data beats commentary. Every figure states source, definition, unit, and both observation
and publication date. If a source fails, say so and use the next one. Never fill a gap with an
invented number.

| Need | First choice | Fallback / cross-check |
|---|---|---|
| Core spending per ally, % GDP, real change, equipment share (**anchor series**) | **NATO "Defence Expenditure of NATO Countries (2014–2026)"**, Excel: `https://www.nato.int/content/dam/nato/webready/documents/finance/def-exp-2026-en.xlsx` (annual, June/July; the year in the file name changes) | NATO press release; ICDS "Defence spending: who is doing what?" for plan context `[E]` |
| Long history, all countries, one definition | **SIPRI Military Expenditure Database** (April; free Excel at sipri.org/databases/milex) | SIPRI fact sheet |
| EU27 investment split: procurement, R&D, collaborative share | **EDA Defence Data** (annual; "Defence Data 2025–2026" published 16 Jul 2026, PDF) | Council "EU defence in numbers" page |
| Delivery basis (government accounts) | **Eurostat COFOG** API, dataset `gov_10a_exp`, `cofog99=GF02`, `na_item=TE`, `sector=S13`, `unit=PC_GDP` or `MIO_EUR` (JSON, no key) | OECD COFOG |
| National budgets, medium- and long-term plans | Finance ministries and MoDs: DE bundeshaushalt.de (Einzelplan 14, Sondervermögen Bundeswehr, Finanzplan); FR PLF + LPM; UK MOD (Defence Investment Plan, annual report) and HM Treasury; IT DPP Difesa; PL budget act + FWSZ; ES PGE; NL Defensie (Prinsjesdag); NO Prop. 1 S Forsvarsdepartementet + long-term plan; SE budget bill; DK finance act + acceleration fund; FI budget | esut.de, hartpunkt, defence24, Altinget, High North News `[E]` |
| Germany procurement pipeline | Bundestag Haushaltsausschuss agendas (`bundestag.de/resource/blob/…/to_NN-sitzung_….pdf`) and *hib* notices: 25-Mio-Vorlagen approved (count, EUR) | esut.de lists of planned Vorlagen `[E]` |
| EU instruments: SAFE, EDIP, EDF, MFF, escape clause | Council policy pages (consilium.europa.eu/en/policies/safe), Commission DG DEFIS (defence-industry-space.ec.europa.eu) | Eunews, Defence Industry Europe `[E]` |
| Ukraine demand and aid | **Kiel Institute Ukraine Support Tracker** (about every two months; Excel) | Ukraine state budget; NATO/PURL and UDCG (Ramstein) statements |
| Import share, European content | **SIPRI Arms Transfers Database** (March; TIV) + **DSCA** major arms sales notifications to European buyers (dsca.mil) | MoD announcements of US/Korean/Israeli buys |
| Arms revenue by company | **SIPRI Top 100** (December) | Company reports |
| Contract awards | Company announcements: FinancialFilings `filings_list` (EU, UK), Nordic Financial `search_filings` with `source="newsweb"` (Oslo, Stockholm); procurement agencies (BAAINBw, DGA, DE&S, Agencja Uzbrojenia, FMA, FMV, FMI, NSPA, OCCAR) | TED notices (not tested); trade press `[E]`, grade C |
| Peer-group orders, revenue, backlog, margins | Quarterly reports via **FinancialFilings** (`companies_list` → id; Rheinmetall = 356, Kongsberg Gruppen = 3649) and **Nordic Financial** (Nordic names); full PDF via `parse_pdf_to_text` | Company IR |
| Share prices, market cap, multiples (context only) | **Yahoo** `get_quote` | EODHD EOD prices |
| FX | **AllRatesToday** `get_official_rates` (`ecb`) | Yahoo |
| Fiscal capacity: GDP, debt, deficit, yields | EC forecast (spring/autumn); IMF WEO (April/October); Eurostat EDP notifications (April/October); FRED OECD 10-year yields (`IRLTLT01<CC>M156N`, e.g. DE, FR, IT, GB, ES, BE) | Nordic GDP only from `docs/hy-market-bbb.md` |
| Industry capacity | Company capacity statements (plants, units per year, start dates); Commission (ASAP, EDIP) | Bruegel, Kiel, IISS analyses `[E]` |
| Trade press | esut.de, hartpunkt, defence24, Defense News, Breaking Defense, EDR Magazine, Euro-sd, Janes free items, Forsvarets Forum, Altinget | `[E]`, never the only evidence for a path |

Quirks (observed in the source test on 2026-10-07):

- **NATO Excel** has 9 sheets: T1 core in national currency; T2 core in USD (two blocks: current
  prices, then 2021 prices); T3 share of real GDP (2021 prices) and annual real change (two
  blocks); T4 real change 2014–2026e; T5 GDP; T6 per capita; T7 personnel; T8a equipment share;
  T8b infrastructure share. The **PDF is image-based** and cannot be read as text, so use the
  Excel (read with `py` + openpyxl). The 2026 edition reports **core** defence (3.5% guideline);
  the 1.5% part is not tabulated. The current and previous year are estimates and are revised in
  the next edition.
- **NATO USD totals:** the press-quoted total (European allies and Canada 2026e "about USD 634bn")
  is in **2021 prices**; current prices give USD 777bn. Always state which. USD totals move with
  EUR/USD, so build the series from T1 (national currency) and convert at the fixed reference FX.
- **NATO equipment shares are lumpy:** NO 26.8% (2025e) → 17.9% (2026e), BE 13.4% → 27.1%,
  ES 44.0% → 34.0%. Large deliveries and budget classification move them. Use a 3-year average
  for the path and log the reason for any jump.
- **NATO % of GDP:** T3 is a share of *real* GDP (2021 prices). It equals the nominal ratio (T2
  current ÷ T5) for every row except the Netherlands (2026e: 2.58% T3 vs 2.29% nominal; the Dutch
  government quotes 2.2%). Paths use the nominal ratio.
- **SIPRI ≠ NATO:** SIPRI 2025 (published 27 Apr 2026): European NATO members USD 559bn, Germany
  USD 114bn (2.3% of GDP). These are close to NATO's figures this year but not on the same
  definition, and gaps above 10% occur (2025: Italy −10%, Sweden −14% vs NATO). Never mix the two
  in one series.
- **SIPRI files:** the database Excel
  (`https://www.sipri.org/sites/default/files/SIPRI-Milex-data-1949-<year>.xlsx`) reads with
  openpyxl (sheets: Regional totals, Constant (2024) US$, Current US$, Share of GDP and others).
  The fact-sheet PDFs are image-based and cannot be read.
- **ICDS tracker** pages fetch only as a summary; the per-country table did not come through.
- **EDA** covers the EU27 only (no UK or Norway) and includes Austria, Ireland, Cyprus and Malta.
  PDF only. Its "€547bn by 2029 on current trends" is a projection `[E]`, not a plan.
- **Eurostat COFOG** lags: in September 2026 the latest year is 2024 (updated 16 Sep 2026). It is
  on a delivery basis, so levels differ from NATO (DE 2024: COFOG 1.4% vs NATO 2.00% of GDP). Use
  the gap trend, never the level, against NATO.
- **Press budget totals do not always add up.** Example: esut.de on the German 2027 draft gives
  EP14 €109.7bn + Sondervermögen €27.5bn and then a total of €133.3bn. Always rebuild the total
  from the budget documents. Poland's 2027 draft appears as both PLN 191.5bn and PLN 198.1bn
  ("4.5% of GDP") depending on which budget sections and FWSZ items are included. State the
  definition used.
- **Norway** presents the budget in early October (2027 budget on 7 Oct 2026). The regjeringen.no
  announcement page has no figures, so use Prop. 1 S from Forsvarsdepartementet.
- **Company backlog definitions differ.** Rheinmetall "Backlog" (€80.5bn, 30 Jun 2026) includes
  frame-contract potential, and "Nomination" (€16.2bn H1 2026) includes new frame agreements.
  Kongsberg reports a firm backlog (NOK 158bn, Q2 2026). The market series uses firm orders only;
  frames go on their own line.
- **Company structure changes:** Kongsberg Maritime was demerged and listed on 23 Apr 2026, so
  Kongsberg Gruppen now reports Defence Systems, Missiles & Aerostructures and Discovery. TKMS was
  spun off from thyssenkrupp; CSG listed in Amsterdam. Check the current structure before reading
  any history.
- **Yahoo** returned 17 of 18 defense tickers (RHM.DE, KOG.OL, SAAB-B.ST, HO.PA, LDO.MI, BA.L,
  HAG.DE, R3NK.DE, TKMS.DE, CSG.AS, AM.PA, KIT.OL, THEON.AS, CHG.L, FCT.MI, IDR.MC, EXA.PA). An
  unknown ticker (MAR.OL) was dropped silently. Yahoo PE values are context only, and some are
  wrong (Saab forward PE 59.5 on 7 Oct 2026).
- **Kiel tracker** counts allocations, not deliveries. It lags about six weeks (data to June 2026
  published 13 Aug 2026). European purchases of US weapons for Ukraine (PURL) are leakage to US
  industry.
- Paid databases (IISS Military Balance+, Janes, Forecast International, GlobalData, Shephard) are
  not assumed available. SEO "market size" reports with no traceable primary source are rejected.
- Expect 30+ searches and fetches for a full run: NATO/SIPRI/EDA first, then budgets for the core
  countries, then EU instruments and Ukraine, then companies and the award log.

## Data discipline

- Tag every number: `[F]` reported fact · `[E]` external forecast or secondary claim · `[A]` own
  assumption · `[?]` unknown. Missing news is not evidence that nothing changed.
- For each finding: (1) the fact, (2) what it means in money (EUR bn per year, which segment,
  which years, European share), (3) whether it changes the model. One contract or one speech does
  not move a country path without a stated reason.
- **One series = one source.** NATO, SIPRI, EDA, COFOG and national budgets measure different
  things. Never mix them in one series or use one to correct another. If the anchor source
  changes its definition (as NATO did with "core" in 2026), document it and show both values for
  one overlapping year.
- **Never double count:**
  - NATO counts military aid to Ukraine in the donor's spending. The Ukraine row therefore shows
    only Ukraine's own budget and non-NATO funding (EU-level loans, frozen-asset revenue). The aid
    inside donor figures is shown as a memo.
  - **SAFE loans are financing, not extra demand.** They fund national spending that is already in
    the national figures. Only the part that raises a country's spending above its plan is
    additional.
  - Headline envelopes (ReArm Europe €800bn, multi-year "packages") are converted into annual
    outlays and tested for additionality before use.
  - EU-budget programmes (EDF, EDIP) are not in national figures. They go on their own small
    EU-level line.
- **Targets are not budgets.** A target enters Base only through a funded plan and the
  credibility grade.
- **Management guidance and ambitions are `[E]`** (e.g. Kongsberg's NOK 100bn revenue ambition
  for 2029). Companies talk their book. Base is set from budgets, awards and capacity, and the gap
  to guidance is stated.
- **Frame contracts** are probability-weighted, never 0% or 100% by default.
- Known weak data: the segment split of equipment spending (no official series; built by hand),
  the European-supplier share (TIV is not money), private companies (KNDS, MBDA, Naval Group,
  Nammo, Diehl report annually or not at all), and contract values not disclosed.
- **User input is input, not a reference.** Links, numbers and drafts are assessed critically
  (what it measures, how fresh, which definition). Use what holds, reject the rest, and note the
  assessment in the source appendix.

## Scenarios

There is no statistical distribution behind wars, elections or fiscal crises, so Bear and Bull
are not percentiles.

- **Base:** the most likely path, and the decision case in IAF.
- **Bear / Bull:** the worst and best reasonably foreseeable paths for the European defense
  industry's orders and revenue. Each is tied to **named catalysts** with mechanism, earliest
  timing and **signposts**. They need not be symmetric, and segments may get different catalysts.
- Consider both a **demand** catalyst and a **supply** catalyst for each tail.

Candidate catalysts for the first run (test them; do not adopt them unchanged):

| Side | Catalyst | Mechanism | Segments hit first |
|---|---|---|---|
| Bear demand | **Ukraine ceasefire together with fiscal stress** | Urgency fades while bond markets punish deficits (FR, IT, UK, BE). Later plan years are cut or stretched; Ukraine aid falls | Ammunition, Ukraine row, then naval and combat air (long programmes stretched) |
| Bear demand | **US trade pressure to "buy American"** | European share falls (F-35, Patriot, HIMARS as part of trade deals) | Air and missile defense, combat air |
| Bear demand | **Execution failure** | Underspending, programme cancellations (F126 frigate, 2026), procurement bottlenecks | Naval, land |
| Bear supply | **Capacity overshoot** | European 155 mm output near 2m shells/yr by 2027 `[E]` meets lower demand after a ceasefire, so prices and margins fall | Ammunition |
| Bear supply | **New entrants** | Cheap drones and Korean/Turkish suppliers take share; legacy systems are cannibalised | Land, C4ISR, ammunition |
| Bull demand | **Russian challenge to NATO territory** | Emergency budgets, faster ramp-up, front-loaded orders | All; air defense and ammunition first |
| Bull demand | **US drawdown from Europe** | Europe replaces US enablers (ISR, air defense, deep strike, lift). Both spending and the European share rise | Air and missile defense, C4ISR, combat air |
| Bull demand | **More common EU financing** | SAFE 2, defense Eurobonds, MFF 2028–34 defence and space window (€131bn proposed) | Collaborative programmes, Rest of NATO Europe |
| Bull demand | **Ukraine rebuilds its army after a ceasefire, financed by the EU** | A ceasefire can be a demand catalyst: a large standing army to equip and a long border to deter | Land, ammunition, air defense |
| Bull supply | — | Capacity limits cap the volume upside. In Bull the gain shows in prices, margins and backlog length rather than revenue | All |
| Long end | **Procurement holiday after the build-up** | The equipment share mean-reverts once fleets are recapitalised, even at a stable % of GDP. NATO reviews the trajectory in 2029 | All, after 2030 |

- **A ceasefire is not a peace dividend by default.** European plans rest on the assessed Russian
  threat (reconstitution within a few years), not on the war itself. A Bear case needs a second
  mechanism (fiscal stress, US pressure, political change), and the skill must say which one.
- **Spending scenarios do not map one-to-one to revenue.** Lags and capacity mean a spending Bull
  raises backlog and margins before revenue, and a spending Bear hits orders years before revenue.
  Show orders and revenue as separate paths.

## Procedure

Two modes, one procedure:

- **Initiate:** "create Defense Market BBB", "new defense baseline", or automatically when
  `docs/defense-market-bbb.md` does not exist. Full research on every step; status "Initial
  baseline"; no change-log values.
- **Update:** "update Defense Market BBB", "oppdater modul" in a defense context, or a
  recalibration trigger. Run every step in order; it is not a menu.

> Updating does not mean "summarise the latest defense news". It means new, thorough research
> that tests whether the current baseline is still right. Start from the last baseline but do
> not anchor on it: every run actively tries to falsify Base. If the evidence is not strong enough
> to change the model, say so explicitly: **Defense Market BBB kept unchanged.**

**Step 0 — Setup.** State the revision of this skill. Note the analysis date, the previous
baseline date and the days since. Roll the window if this is the first run in a new year. Read the
previous `docs/defense-market-bbb.md` and record its point values, catalysts, signposts and open
checkpoints. They become the "previous" column in the change log, and every open checkpoint is
closed or carried with a new status. Check **current company structures** (demergers, IPOs,
acquisitions, renamed segments) before using any company history. Set the reference FX (ECB, date).

**Step 1 — Threat and policy regime.** Record the state of: the war in Ukraine (front, talks,
ceasefire terms); Russian activity against NATO territory; the US posture (troop levels in Europe,
NATO commitment, FMS and trade policy); NATO decisions (targets, capability targets, the 2029
review); EU instruments (SAFE allocations and disbursements, EDIP, EDF, MFF negotiation, national
escape clauses). Output: the policy regime per scenario, in one line each.

**Step 2 — Spending actuals (the tracker).** From the NATO Excel: per country, core spending in
national currency and EUR, % of GDP, real change, equipment share and equipment spending for the
last realised year, the current-year estimate and the year before. Cross-check with SIPRI (latest
year), EDA (EU27 investment, collaborative share) and COFOG (prepayment gap). Flag any source
difference above 10% and explain it (definition, timing, FX). Compare with the previous baseline
and record forecast vs actual.

**Step 3 — Budgets, plans and credibility.** Per core country: target (% of GDP and year), enacted
budget for the current year, draft budget for next year, medium-term plan (Finanzplan, LPM, DIP,
long-term plan, FWSZ), commitment appropriations, and the implied path in EUR. Grade plan
credibility A–D. Check fiscal capacity: debt/GDP, deficit vs EU rules, use of the escape clause,
10-year spread to the Bund, SAFE take-up, upcoming elections. Check past execution (outturn vs
budget, special-fund outflow). Base path = plan × credibility, with any haircut stated `[A]`.
Secondary rows: sum of national targets and plans, Base + range.

**Step 4 — Equipment spending and the European share.** Per country and year: equipment share
(3-year NATO average as the anchor, adjusted for funded plans) → equipment spending. The
European-supplier share comes from: big-ticket non-European buys in the award log (F-35, Patriot,
HIMARS, K2/K9, Arrow and similar, with payment profiles), DSCA notifications to European buyers,
SIPRI import trends (direction only), SAFE content rules, and national "buy European" statements.
Output: addressable equipment spending per country, scenario and year.

**Step 5 — Segment allocation and award log.** Keep the **contract award log** for every award of
€100m or more, or that is material for a covered company: date, buyer, segment, prime and key
subcontractors, value, firm or frame, funding (national, SAFE, EU, Ukraine aid), delivery period
and grade. Allocate each country's addressable spending to segments from its plans (Germany's
25-Mio-Vorlagen by category, Poland's awards, the Nordic long-term plans, the UK DIP, the French
LPM priorities) and check against 12 months of awards by value. Leading indicators: commitment
appropriations, 25-Mio-Vorlagen approved, frame call-offs, joint procurement via NSPA, OCCAR,
EDIP and SAFE.

**Step 6 — Industry supply and capacity.** Per core segment: capacity now and planned (units per
year where meaningful), new plants with start dates, bottlenecks (energetics, rocket motors,
microelectronics, skilled labour, test ranges), and gains by non-European competitors and new
entrants. Compare capacity with demand per year. A **shortage** means pricing power, longer lead
times and more imports. A **surplus** means price pressure and margin risk. Test both directions.

**Step 7 — Orders to revenue (market level).** Build the peer-group order intake, revenue, firm
backlog and book-to-bill per segment, mapping each company's reported segments to the rows above
(the mapping goes in the appendix). Then model market revenue from orders with the segment lead
time and the capacity ceiling. Check consistency: peer revenue from Europe ≤ addressable spending
for the segment; the peer share and its trend; a falling book-to-bill while spending rises (or the
reverse) is explained.

**Step 8 — Pricing and margins.** Per core segment: peer EBIT margin (last four quarters and
3-year history, pre-2022 average), contract types (fixed price with escalation, cost-plus, frame
with price adjustment), inflation pass-through, ramp-up costs, and the cash profile (customer
advances). Set a **steady-state margin** per segment and say how margins behave in shortage and in
surplus.

**Step 9 — Test BBB.**
- **Base:** what would have to be true for Base to be wrong, and do we see it? Search actively for
  exactly that (pre-mortem). Is it still the most likely path? Where Base differs from company
  guidance or consensus, state why.
- **Bear / Bull:** are the catalysts still the right ones? Has one come closer, been triggered, or
  become irrelevant? Has a signpost been crossed? Is a demand or supply catalyst missing? Have
  segments diverged?
- **Evidence threshold:** change a scenario, catalyst or path only when several independent data
  points point the same way, or one event materially changes a country's funded plan, the European
  share or a segment's capacity balance, and only by more than the minimum change.

**Step 10 — Set the paths.**
- **Spending:** core spending (EUR bn and % of GDP) per core country, secondary aggregate and the
  Europe total, per scenario: 2026 (no spread), 2027–2029, 2030, 2035. Point + range.
- **Equipment and addressable:** equipment spending and addressable spending for the Europe total
  per scenario and year; equipment share and European share as separate lines.
- **Segments:** order intake growth and revenue growth per core segment and scenario, 2027–2029
  and the 3-year CAGR, plus the index (2026 = 100). Built in three layers: (a) backlog already
  booked sets the floor for revenue in the next years, (b) allocated addressable spending sets
  orders, (c) the capacity ceiling and lead time set revenue.
- **Long end and steady state:** spending % of GDP in 2030 and 2035 and the plateau after the
  build-up; the equipment share at steady state; segment revenue CAGR 2030–2035; growth after
  2035 (≈ nominal GDP growth ± a stated adjustment); the steady-state margin per segment. Use
  historical analogues for the fall-back after a build-up (the 1980s build-up followed by the
  1990s procurement drop; Europe after 1990), quantified from SIPRI history in the first run.
  Never assume build-up growth rates continue indefinitely.

**Step 11 — Write, log and check.** Write the document in the output format, with a complete
change log (new / unchanged / changed with previous → new value, reason and source; forecast vs
actual; weights kept or changed; whether IAF analyses should update). Read it back and run the
checks below.

## Recalibration triggers

A full update is due when any of these occurs:

- NATO, SIPRI, EDA or Eurostat publish their annual data (NATO June/July, SIPRI April and March
  (transfers) and December (Top 100), EDA July, COFOG February)
- A core country presents or enacts a budget, a medium-term plan or a long-term plan (budget
  season: DE July draft / November–December enactment, PL August, SE and NL September, NO, FR
  and others October; UK fiscal events and spending reviews)
- A ceasefire in Ukraine is agreed or collapses, or a military incident involves a NATO member's
  territory
- A US decision on troop levels in Europe, the NATO commitment, or FMS and trade policy; or a
  European buy of a US system above €5bn
- An EU decision on new common defense financing (SAFE follow-up, Eurobonds, MFF defence window)
- Fiscal stress: a core country's 10-year spread to the Bund widens by more than 50 bp in a month,
  a downgrade, or the end of the escape clause
- A programme award or cancellation above €5bn in a core segment
- Evidence of capacity surplus (price cuts, idle lines) or a binding bottleneck
- Peer-group book-to-bill below 1.0 for two consecutive quarters
- A Bear or Bull catalyst is triggered or a signpost is crossed
- The baseline is older than 90 days

## Output: `docs/defense-market-bbb.md`

Keep the main part short per heading. The award log, country plan details, company mapping and
source details go to the appendix.

```markdown
# Defense Market BBB — [baseline date]

## Metadata
- Analysis date, status (Initial / Final / Provisional and why), skill revision
- Previous baseline (date, days), window (2026 + 2027–2029, long end 2030/2035), stale after [date]
- Reference FX (ECB, date); NATO edition used; Nordic GDP source (HY BBB baseline date)

## Conclusion
- BBB changed / kept unchanged — explicit
- Base in two sentences (spending; industry orders and revenue)
- Segment ranking (strongest → weakest) with the main reason
- Main Bear catalyst and main Bull catalyst

## Interface — core defense spending, Europe total and core countries (EUR bn; % GDP)
| Row Bear / Base / Bull | 2026 | 2027 | 2028 | 2029 | 2030 | 2035 | Target (year) |
|---|---|---|---|---|---|---|---|

## Interface — equipment and addressable spending, Europe total (EUR bn)
| Line Bear / Base / Bull | 2026 | 2027 | 2028 | 2029 | 2030 | 2035 |
|---|---|---|---|---|---|---|
| Equipment share % | | | | | | |
| Equipment spending | | | | | | |
| European-supplier share % | | | | | | |
| Addressable spending | | | | | | |

## Interface — segments (growth % per year; index 2026 = 100)
| Segment Bear / Base / Bull | Orders 2027 / 28 / 29 | Revenue 2027 / 28 / 29 | Revenue CAGR 26–29 | CAGR 30–35 | Steady-state EBIT % |
|---|---|---|---|---|---|

## Scenario definitions
| Scenario | Weight (convention) | Policy regime | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|
| Bear | 25% | | | | | |
| Base | 50% | | | | | |
| Bull | 25% | | | | | |

## Spending tracker
| Country | Target (% GDP, year) | NATO 2025e / 2026e % GDP | Equipment share 3-yr | Budget 2026 | Draft 2027 | Plan to [year] | Credibility | Base 2029 | Change vs previous |
|---|---|---|---|---|---|---|---|---|---|
- Source cross-check (NATO vs SIPRI vs EDA vs COFOG): differences above 10% and why
- Forecast vs actual for the realised year

## Market check
| Segment | Peer order intake LTM | Book-to-bill | Firm backlog / revenue | Revenue growth LTM | EBIT % LTM | Capacity balance |
|---|---|---|---|---|---|---|
- Valuation context (sector multiples; context only, never an IAF input)

## Drivers
### Threat and policy regime
### Fiscal capacity
### Equipment share and European share
### Segment allocation and leading indicators
### Industry supply and capacity
### Orders to revenue
### Pricing and margins
### Ukraine and export markets

## Signposts and monitoring
| Signpost | Threshold (Bear / Bull) | Now | Previous | Direction |
|---|---|---|---|---|
- Open checkpoints (carried / closed) and the budget and data calendar until the next update

## For IAF
- What changed that defense company analyses must take in, or "no material change"
- Per covered company: segments and regions to use, backlog coverage vs the market path

## For downstream skills
- [[hy-market-bbb]]: defense issuers in Nordic HY, if any, or "none"

## Change log
- New / unchanged / changed (previous → new, reason, source)
- Forecast vs actual for the realised year
- Weights kept or changed — explicit
- New baseline date

## Appendix
### Contract award log (date, buyer, segment, supplier, value, firm/frame, funding, delivery, grade, source)
### Country plans (target, budgets, plans, credibility, fiscal indicators)
### Company segment mapping (company segment → rows; share of revenue from Europe)
### Sources
| Source | Content | Definition | Observed / published |
|---|---|---|---|
```

## Interface to IAF

Every baseline delivers, in the fixed Interface tables and the sections behind them: spending,
equipment and addressable paths; segment order and revenue growth per scenario; the long end and
steady state; steady-state margins; capacity balance; catalysts, signposts and status.

Use in [[iaf-valuation]] (defense companies):

- **Track:** IAF decides. Most defense companies are Track A (backlog-driven growth, moderate
  capital intensity). A company in a heavy capacity build-out with volatile FCF (new ammunition or
  missile plants) may need Track B or Track A with explicit capex; state which and why.
- **Current year and Year 1:** the company's own firm backlog, delivery schedule and guidance carry
  revenue. This baseline is the market check (segment growth, book-to-bill, capacity).
- **Years 2–3:** company revenue = Σ over its segments and regions of revenue × the market segment
  growth path from this baseline, ± a named and sourced share change set in the company analysis.
  Show backlog coverage of each year.
- **After the window:** the growth fade comes from the long-end CAGR and the steady state; the
  normalised margin from the steady-state segment margin. The exit multiple stays independent
  (IAF rule). Sector multiples in the Market check are context only.
- **Bear / Bull:** use this baseline's catalysts and map each to the company's segments (e.g. a
  ceasefire with fiscal stress hits ammunition and Ukraine exposure first and naval later).
- **Growth capex (ROIC_g):** capacity expansions are tested against the segment capacity balance
  per scenario. A plant that is only needed in Bull, or that comes on line into a surplus, has a
  lower ROIC_g.
- **Mapping:** match each company segment to the right rows (see the appendix mapping). Company
  market share, pricing and contract specifics are set and sourced in the company analysis.

## Checks before finishing

- Skill revision stated; window correct for today's date; reference FX and NATO edition stated.
- Every spending figure on its named source and definition (NATO core as the anchor); targets,
  plans, budgets and outturn kept apart; no mixing of NATO, SIPRI, EDA and COFOG in one series.
- No double counting: Ukraine aid, SAFE loans and EU-level programmes handled as in Data
  discipline.
- Every number tagged and sourced with dates; award log graded A–D.
- 2026 identical across scenarios; point value and range for every core figure.
- Segment paths built through equipment share → European share → allocation → lead time and
  capacity, never copied from total spending growth.
- Peer revenue from Europe ≤ addressable spending per segment; orders and revenue shown separately.
- Long end and steady state set and anchored; no indefinite build-up growth.
- Bear and Bull each tied to named catalysts with signposts; no probability language.
- Change log complete (previous → new) or explicit "kept unchanged".
- File written, read back, tables render.
