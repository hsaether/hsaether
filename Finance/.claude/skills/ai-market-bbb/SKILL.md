---
name: ai-market-bbb
description: AI Market BBB — the baseline for the AI value chain over the IAF window (stub of the current year + 3 calendar years, now 2027–2029). Covers market growth from the money in (hyperscaler and other AI data-center capex and how it is financed) through three layers — Hardware (accelerators/GPUs and custom ASICs, memory and HBM, foundry, packaging and equipment, networking and data-center power and cooling), AI engines (frontier model labs and the AI cloud platforms that sell compute) and Tools (copilots and agents in incumbent software, AI-native tools such as coding agents, and the seat-based software they disrupt). Produces Bear/Base/Bull paths for capex, layer revenues, adoption and the monetisation ratio, layer EPS paths and exit multiples, and an index-level IAF test per layer basket (Base IRR in USD and NOK, hurdle P/E at k = 12%, E / R against the HY reference), plus catalysts and signposts. Base is the decision case; Bear and Bull are catalyst-based stress tests; 25/50/25 is a labelled convention, never a probability. Reads the equity index scenarios, NOK path and World paths from docs/equity-market-bbb.md, NIBOR from docs/hy-market-bbb.md and the IAF method from iaf-valuation; it is the only place an AI market path is set. ALWAYS use when the user mentions AI Market BBB / AI BBB / AI-markedet, asks to create, run or update ("oppdater modul") the AI module, or asks about AI capex, hyperscaler spending, GPUs, Nvidia/AMD/Broadcom/TSMC demand, HBM or memory in AI, data-center power, OpenAI/Anthropic revenue, AI adoption, copilots, AI agents, AI disruption of software, or whether AI stocks clear the required return — even without naming the skill. Feeds iaf-valuation for AI hardware, platform and software companies and equity fund analyses with AI exposure.
---

# AI Market BBB

**Revision:** 2026-10-12.2 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/ai-market-bbb/` in the Finance folder.

A Bear/Base/Bull baseline for the AI market. It answers three questions:

1. **Market:** how fast does AI spending grow, year by year, and where in the chain does the money
   land (hardware, engines, tools)?
2. **Durability:** is the end revenue catching up with the capital spent, and how is the gap
   financed? That decides whether 2028–29 is digestion or continued build-out.
3. **Price:** what return do the listed layer baskets offer at today's prices on the Base case, and
   what growth is the market already paying for (IAF at basket level)?

It is a testable hypothesis with explicit risks, not a news summary and not a stock list.

**Position in the chain.** It sits under [[equity-market-bbb]] (which sets the index paths, the
macro scenarios and the NOK path) and beside the sector BBBs. It uses [[iaf-valuation]]'s method
(d + g + re-rating, year-by-year IRR, hurdle at k = 12%). The chain it models, with the gaps where
most of the analysis sits:

**End demand (users, tasks, tokens) → engine revenue (labs, AI cloud) → compute contracts and
backlog → capex (hyperscalers, neoclouds, sovereign) → hardware orders (accelerators, memory,
foundry, network, power) → hardware revenue and margins.** Funding runs the other way: **operating
cash flow + debt + equity + vendor financing → capex.**

| Gap | Why it matters |
|---|---|
| Capex ≠ AI revenue | Capex runs years ahead of end revenue. The **monetisation ratio** (end revenue ÷ capex) is the core durability test |
| Backlog ≠ demand | RPO and cloud backlog include labs' multi-year commitments that depend on the labs' own funding |
| Capex ≠ hardware revenue | Buildings, land, power and long-lived assets vs short-lived compute; the compute share moves |
| Units ≠ value | Memory and GPU prices swing with scarcity; supply limits turn demand into prices, not volume |
| Token volume ≠ revenue | Price per token at constant capability falls by an order of magnitude a year |
| AI revenue ≠ software revenue | Agents can shrink seat-based software while total software spend grows |

**Scope:** AI data-center capex and its financing; accelerators (GPU, ASIC), memory (DRAM/HBM,
enterprise SSD as a memo), foundry and advanced packaging, semiconductor equipment, networking and
optics, data-center power and cooling; frontier model labs (OpenAI, Anthropic, Google DeepMind
as part of Alphabet, xAI, Meta, others); AI cloud (AWS, Azure, Google Cloud, OCI, neoclouds);
copilots and agents (Microsoft 365 Copilot, Salesforce, ServiceNow, SAP), AI-native tools (coding
agents and others), and incumbent application software. **Out of scope:** the oil price
([[oil-market-bbb]]); index return paths, the NOK path and macro scenarios
([[equity-market-bbb]]; read only); NIBOR ([[hy-market-bbb]]; read only); a single company's
valuation (IAF company analysis); consumer devices (AI PCs and phones) except as a memo; China's
domestic AI chain except as an export and competition row.

## Standing parameters

- **Time grid = IAF grid:** stub (rest of the current year) + 3 full calendar years, now Q4 2026
  + 2027–2029, exit 31 Dec 2029. Roll forward with the first run each January (forecast vs actual
  for the realised year; a new end year). Rolling is not a reset.
- **The current year has no scenario spread** (IAF rule): 2026 market sizes are guidance plus
  year-to-date actuals, the same in all three scenarios. Scenarios diverge from 2027.
- **Units:** USD bn nominal, calendar years. Fiscal years are calendarised and the method is
  stated (NVIDIA's FY ending January ≈ the previous calendar year; Microsoft's FY ending June =
  half of two calendar years; Oracle's FY ending May ≈ the calendar year it mostly covers).
  Where no reliable dollar series exists, the row is an **index (2026 = 100)**.
- **Returns:** basket IRR in USD and in NOK (NOK path from [[equity-market-bbb]]), before fund
  fees and tax. EPS paths are relative to **CY27 consensus = 1.00**.
- **Point value + range** for every scenario figure on core rows.
- **Base = the decision case.** Bear and Bull are stress tests tied to named catalysts.
  **25/50/25** is a labelled convention, never a probability.
- **Consistency with [[equity-market-bbb]]:** the AI Bear sits inside the equity Bear (recession
  and oil Bear) and adds the AI-specific mechanism; the AI Base sits inside the equity Base ("AI
  earnings boom slows to trend"); the AI Bull inside the equity Bull. The NOK path is never set
  here.
- **Minimum change (convention):** a point value moves only if the evidence moves it by at least
  5% (capex level), 5 pp (a layer growth rate), 10% (lab revenue level), 0.05 (EPS path point) or
  1 turn (exit P/E). Smaller moves are noted, not applied.
- **Staleness:** stale after **45 days**, after a hyperscaler capex guidance change of more than
  10% (quarterly reports: late Jan, late Apr, late Jul, late Oct), after NVIDIA's quarterly report,
  or after the equity baseline changes its scenarios. IAF treats a stale baseline as provisional.
- Rows and definitions are fixed. Changing one is a method change and goes in the change log.

## Files

- Skill: `.claude/skills/ai-market-bbb/SKILL.md`, plus `references/` with the scripts of the
  last run (`model.py` for the layer baskets and the README).
- Inputs (read only): `docs/equity-market-bbb.md` (scenarios, World paths, USD/NOK path, World
  Base IRR and E / R), `docs/hy-market-bbb.md` (NIBOR path), `docs/hy-funds-analysis.md` (HY
  market reference E / R), `.claude/skills/iaf-valuation/SKILL.md` (method, k), company and fund
  analyses with AI exposure (e.g. `docs/dnb-teknologi-analysis.md`) for consistency.
- Output: `docs/ai-market-bbb.md`, one running baseline. Baseline date in the H1. Git holds
  history; read the previous version before overwriting it.
- Calculations run in the scratchpad (`py -I`, copies of the reference scripts, Yahoo quote and
  `earningsTrend` scripts from `equity-market-bbb/references/`). Copy changed scripts back.
- Write with Write/Edit, then **read the file back** and check every table and number. An answer
  in the conversation alone is not delivery.

## Rows

### Money in

| Row | Content | Unit | Role |
|---|---|---|---|
| **K1 Hyperscaler capex** | MSFT, GOOGL, AMZN, META, ORCL; calendar year, incl. finance leases as each reports | USD bn | Core; the anchor series |
| K2 Other AI capex | Neoclouds (CoreWeave, Nebius), labs' own builds, sovereign, xAI, enterprise, China | Memo, `[?]` until a source exists | Secondary |
| **K3 Financing** | Capex ÷ operating cash flow; debt and equity raised for AI; off-balance lease commitments; vendor financing | Ratios, USD bn | Core (risk gauge) |
| **K4 Contracted backlog** | AWS backlog, Google Cloud backlog, Microsoft commercial RPO, Oracle RPO, neocloud backlog | USD bn | Core (leading indicator) |

### Hardware

| Row | Content | Listed proxies | Role |
|---|---|---|---|
| **H1 Compute** | Data-center accelerators (GPU, ASIC) and AI networking silicon | NVDA (data center), AVGO (AI semis), AMD (Instinct), MRVL (custom) | Core |
| **H2 Memory** | DRAM incl. HBM, server DRAM; enterprise SSD memo | MU, SK hynix, Samsung | Core; cyclical (Track B in IAF) |
| **H3 Foundry, packaging and equipment** | Leading-edge wafers, CoWoS, lithography, deposition and etch | TSM, ASML, AMAT, LRCX | Core |
| **H4 Networking and DC infrastructure** | Switching, optics, power distribution, cooling | ANET, VRT, ETN (GEV, optics names secondary) | Core |
| H5 Power | Grid connection, on-site generation, GW available vs needed | Utilities, turbines (memo) | Constraint row, signposts only |

### AI engines

| Row | Content | Proxies | Role |
|---|---|---|---|
| **E1 Frontier labs** | Revenue of OpenAI and Anthropic (booked, calendar year; run-rate shown separately); others memo | Private; company statements and reported figures | Core; the end-revenue anchor |
| **E2 AI cloud platforms** | AWS, Azure, Google Cloud, OCI revenue growth; neoclouds memo | MSFT, GOOGL, AMZN, ORCL, (META as an internal user) | Core |
| E3 Price of intelligence | Price per token at constant capability; usage growth | Epoch AI, provider price lists | Secondary (driver) |

### Tools

| Row | Content | Proxies | Role |
|---|---|---|---|
| **T1 Copilots and agents in suites** | Paid AI seats and consumption in incumbent suites | Microsoft 365 Copilot seats, Salesforce, ServiceNow, SAP | Core |
| **T2 AI-native tools** | Coding agents and other AI-first products | Cursor, Claude Code, GitHub Copilot (memo for private names) | Core (index) |
| **T3 Incumbent application software** | Seat-based SaaS revenue growth and margins under agent substitution | NOW, CRM, ADBE, SAP, INTU, SNOW, DDOG, PLTR | Core |
| **T4 Adoption** | Share of firms using AI (US Census BTOS) | Census | Core (driver) |

**Layer baskets for the IAF test:** H1, H2, H3, H4, E (MSFT, GOOGL, AMZN, META, ORCL) and T
(T3 names). Market-cap weighted; basket P/E = Σ mcap ÷ Σ (mcap ÷ P/E). Loss-makers (CoreWeave)
are shown as memo, not in a P/E.

## Definitions

| Term | Definition |
|---|---|
| **Monetisation ratio** | E1 frontier-lab revenue (calendar year, booked) ÷ K1 hyperscaler capex. A narrow but clean measure: lab revenue is the purest AI end revenue; the hyperscalers' own AI revenue is not separately reported. Track its direction, not its level |
| Run-rate | Latest month (or quarter) annualised. Never added to booked revenue |
| Backlog / RPO | Contracted, not yet recognised revenue. Labs' commitments in it are only as good as the labs' funding |
| Compute share | Share of capex spent on short-lived assets (servers, accelerators, network). Microsoft: about two-thirds (Q4 FY26) |
| Consensus | Yahoo `earningsTrend` mean, with the number of analysts; calendarised. Context and starting point, never the Base by default |
| Basket IRR | IAF Track-B-style build on the basket: P = today's price at CY27 P/E; cash yield = payout × EPS; exit value = exit P/E × normalised 2030 EPS; flows dated mid-year; stub 12 Oct–31 Dec price flat |
| **E / R** | As in the HY rule: E = Base NOK IRR − Base window NIBOR; R = Base 2027 − Bear 2027 return (NOK). Compared with the HY market reference and the World index |
| Implied growth | Constant annual EPS growth after 2027 (from the Base 2027 level, at the Base exit P/E) that gives 12% in NOK. It shows what the price assumes |

## Data sources

Primary beats secondary. Every figure states source, unit and as-of date. Never fill a gap with
an invented number; aggregator blogs are `[E]` at best and never the only source for a path.

| Need | First choice | Fallback / cross-check |
|---|---|---|
| Hyperscaler capex, cloud growth, backlog, RPO | Company releases and 10-Qs (investor sites; SEC EDGAR); FinancialFilings `filings_markdown_search` (500-credit monthly cap) | Earnings-call summaries `[E]`; FactSet Insight, Moody's, Goldman, Morgan Stanley consensus `[E]` |
| NVIDIA, Broadcom, AMD, Marvell, TSMC, memory results and guidance | Company releases (NVIDIA newsroom; SEC 8-K exhibits; TSMC 6-K) | Call summaries `[E]` |
| Memory prices | TrendForce releases (quoted by brokers) `[E]` | Company commentary |
| Lab revenue | Company statements, CNBC/Reuters/The Information reports of investor figures `[E]` | Epoch AI revenue dataset (`epoch.ai/data/ai_companies_revenue_reports.csv`) |
| Price of intelligence | Epoch AI data and reports | Provider price lists |
| Adoption | US Census BTOS AI supplement (census.gov) | Secondary analyses of BTOS `[E]` |
| Market totals | Gartner AI spending forecast (press release; web page returns 403 to WebFetch, use search excerpts) `[E]`; IDC | Never used as a path; cross-check only |
| Power | PJM, ERCOT, EIA; S&P Global; broker reports `[E]` | Trade press |
| Prices, market caps, P/E, consensus EPS | **Yahoo** via `equity-market-bbb/references/quotes.py` and `trend.py` | Zacks `get_wall_st_rating`, `compare_stocks` (US only) |
| FX | Yahoo (`KRW=X`, `EURUSD=X`); USD/NOK path from [[equity-market-bbb]] | AllRatesToday |

Quirks (2026-10-12 run):
- Yahoo `quote` returns no P/E or forward EPS for Korean tickers (`000660.KS`, `005930.KS`);
  `earningsTrend` does (KRW). Market caps come in KRW; convert at `KRW=X`.
- Yahoo flags TSM's `financialCurrency` as TWD, but the ADR EPS in `earningsTrend` is USD per ADR
  (forward P/E confirms).
- Alphabet's and Amazon's CY26 EPS include large equity gains, so their CY26→CY27 consensus growth
  is negative; use CY27 for P/E and leave CY26 out of growth figures.
- Microsoft changed building useful lives (15 → 25 years) and is shifting finance leases to
  operating leases in FY27: its reported capex falls without a change in spending. Track the
  lease commitments line beside capex.
- Many "AI revenue" and "ARR" figures circulate only in aggregator blogs with inconsistent dates.
  Tag them `[E]` or `[?]`, and never mix run-rate with booked revenue.
- Statista Market Insights ("Artificial Intelligence – Worldwide") sizes the market from the
  funding of AI companies, not from spending; its editions disagree with each other and the page
  shows no yearly values. Use its growth rate as a cross-check at most, never its level.

## Data discipline

- Tag every number: `[F]` reported fact · `[E]` external forecast or secondary · `[A]` own
  assumption · `[?]` unknown.
- For each finding: (1) the fact, (2) what it means for a row (USD, which years), (3) whether it
  changes the model.
- **Guidance is `[E]`.** Companies talk their book; capex guidance has been raised every quarter
  since 2024, and consensus has repeatedly lagged.
- **Never double count:** lab revenue paid to clouds appears again as cloud revenue and again as
  capex; neocloud capex financed by hyperscaler contracts is not extra demand; vendor financing
  (chip makers investing in customers) is netted in the financing row, not added to demand.
- **User input is input, not a reference:** assess, extract, note in the source appendix.
- Provenance on every fetched value (source, as-of date, unit); raw kept beside derived;
  plausibility checks: a row moved more than 15% from the previous baseline needs a second source.

## Scenarios

| Side | Catalyst | Mechanism | Rows hit first |
|---|---|---|---|
| Bear demand | **Financing break** | A frontier lab falls short of its compute commitments or cannot raise; contracts at Oracle and neoclouds are renegotiated; credit for AI capex tightens (Oracle near HY); hyperscalers with near-zero FCF cut the next year's capex | K1 (year after), H1, H4, E1, ORCL and neoclouds |
| Bear demand | **Monetisation disappointment** | Enterprise ROI stalls (Gartner places GenAI in the trough of disillusionment in 2026); lab revenue growth slows sharply while price per token keeps falling | E1, T1, then K1 |
| Bear supply | **Efficiency shock** | Algorithmic gains cut compute per task faster than usage grows; GPU rental prices fall; capex digestion | H1, H2, K1 |
| Bear supply | **Capacity overshoot (2028)** | New memory and HBM capacity meets slowing demand | H2, H3 equipment |
| Bear macro | **Equity Bear** ([[equity-market-bbb]]) | Global recession H1 2027 + oil Bear; P/E compression | All baskets |
| Bull demand | **Agentic adoption** | Adoption broadens (BTOS 20% → 40%+); tokens per user multiply; lab revenue doubles again in 2027; capex reaches the brokers' upside (~USD 1.4tn in 2027) | E1, T2, K1, H1 |
| Bull supply | — | Power, CoWoS and HBM limits cap volume: in Bull the gain shows in prices, margins and backlog length more than in units | H1, H2 margins |
| Tail (not modelled) | Taiwan conflict; export-control escalation | Supply shock; China already excluded in NVIDIA's guidance | All |

- The AI Bear needs an AI mechanism on top of the macro Bear; a recession alone slows but does not
  break contracted 2027 builds.
- Supply constraints cushion a Bear in the first year (projects stretch rather than stop) and cap
  volume in a Bull.

## Procedure

Two modes: **Initiate** (no `docs/ai-market-bbb.md`) and **Update** ("update AI Market BBB",
"oppdater modul" in an AI context, or a recalibration trigger). Every run tries to falsify Base;
if the evidence is not strong enough, say **AI Market BBB kept unchanged**.

**Step 0 — Setup.** State this skill's revision and the revisions/dates of the upstream baselines
(equity, HY). Read the previous baseline and record its values and open checkpoints.

**Step 1 — Money in (K1–K4).** Latest quarter capex per hyperscaler, full-year guidance, next-year
signals; consensus for the next two years (state source and date); capex ÷ OCF, FCF, debt and
equity raised, lease commitments; backlog and RPO per company. Output: K1 per scenario.

**Step 2 — Hardware (H1–H5).** NVIDIA data-center revenue and guidance; Broadcom AI semis and
guidance; AMD data center; TSMC growth and capex, CoWoS; memory prices (TrendForce) and sold-out
status; networking and DC infrastructure orders; power constraint evidence. Check: H1 growth vs
K1 growth (compute share), and that H1 Base ≤ supply limits stated by suppliers.

**Step 3 — Engines (E1–E3).** Lab revenue (booked and run-rate, dated), commitments and cash burn;
cloud growth and backlog; price-per-token trend. Compute the monetisation ratio per scenario.

**Step 4 — Tools (T1–T4).** Copilot seats and pricing model; AI-native tool revenue; incumbent
software growth, guidance and margins; adoption (BTOS). State winners and losers by mechanism
(seat compression vs consumption pricing).

**Step 5 — Layer baskets (IAF).** Fetch prices and consensus (CY26, CY27, analysts); basket P/E;
set EPS paths per scenario (relative to CY27 consensus) from Steps 1–4; exit P/E per scenario;
payout; run `model.py`: IRR USD and NOK, 2027 return, hurdle P/E at k = 12%, margin of safety,
E / R, implied growth. Compare with World (equity BBB) and the HY reference.

**Step 6 — Test BBB.** Pre-mortem for Base; catalysts still right; signposts crossed; consistency
with the equity baseline's scenarios and World EPS path; consistency with fund and company
analyses that use AI blocks (flag differences for re-run).

**Step 7 — Write, log and check.** Output format below; complete change log; read back; checks.

## Recalibration triggers

- A hyperscaler changes capex guidance by more than 10%, or gives a first next-year figure
- NVIDIA, Broadcom, AMD or TSMC quarterly results; memory contract-price releases
- A lab's revenue, funding round or commitment change larger than 20%
- Oracle or a neocloud downgraded, a failed financing, or a contract cancellation
- A model release that changes compute per task materially (efficiency shock)
- A Bear or Bull signpost crossed; the equity baseline changes scenarios
- The baseline is older than 45 days

## Output: `docs/ai-market-bbb.md`

```markdown
# AI Market BBB — [baseline date]

## Metadata
## Conclusion
## Interface — money in (USD bn): K1 capex, K3 financing, K4 backlog
## Interface — hardware (USD bn or index 2026 = 100)
## Interface — engines and tools
## Interface — monetisation ratio
## Interface — layer baskets (IAF): P/E, Base/Bear/Bull IRR USD and NOK, 2027, hurdle P/E, MoS, E / R, implied growth
## Interface — EPS paths and exit P/E per layer
## Scenario definitions
## Drivers (money in; hardware; engines; tools; power)
## Against World and high yield
## Signposts and monitoring
## For IAF and downstream skills
## Change log
## Appendix: market prints, consensus, sources
```

## Interface to IAF

- **Track:** H2 memory is Track B (cyclical; normalise to mid-cycle). H1 compute and H4 are Track B
  while the build-out lasts (peak margins, order-driven); E platforms and T software Track A unless
  capex dominates FCF (then state it).
- **Revenue Years 2–3:** company revenue = its layer path × share change set and sourced in the
  company analysis. Backlog (RPO) coverage shown.
- **Exit:** IAF sets the exit multiple independently; this baseline's exit P/E per layer is a
  reference, never the IAF ceiling.
- **Bear/Bull:** map the catalysts above to the company's layers.

## Checks before finishing

- Skill and upstream revisions stated; window and stub correct.
- Every number tagged and sourced with dates; run-rate never mixed with booked revenue; guidance
  tagged `[E]`.
- 2026 identical across scenarios; point + range on core rows.
- H1 growth reconciled with K1 growth and supplier limits; no double counting of lab, cloud and
  capex dollars.
- Basket IRRs reproduced by `model.py`; NOK path and NIBOR read from upstream, not set here.
- Bear and Bull tied to named catalysts with signposts; AI Bear consistent with the equity Bear.
- Change log complete or explicit "kept unchanged". File written, read back, tables render.
