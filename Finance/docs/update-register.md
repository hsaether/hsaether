# Update register

The bookkeeping for the update chain: which document reads which, which version of each
input it was built on, when it goes stale, and which planned events should trigger a re-run.
Kept by the `update-chain` skill; checked by
`.claude/skills/update-chain/references/update_check.py`.

- **First fill:** 24 Oct 2026, from the metadata of each document. The dates are as each header
  states them. Where a header was unclear, the note column says so.
- **Rules:**
  - Dates are ISO (YYYY-MM-DD). `-` means none. `?` means not recorded.
  - Update the Documents and Inputs rows with the script's `record` command, not by hand.
  - Edit the Events table by hand (add new events; mark done with `event-done`).

## How to read the columns

- **as of:** the date of the latest run of the document, including a run that kept everything
  unchanged.
- **last change:** the date of the latest run that moved a value other documents read (a path,
  a scenario, a mid-cycle value, a verdict, a stub). A run that kept the document unchanged
  leaves this date alone. Downstream documents are flagged for update only when this date is
  newer than the version they read; a newer "as of" alone only asks for a header note.
- **affects** (from 7 Nov 2026): the downstream documents for which the last change moved a
  value they read materially (the trigger rule in the `update-chain` skill), set by `record
  --affects`. Only these are flagged; `none` flags no one; `all` is the old behaviour (every
  downstream). Others see the change under "no action" and read it at their own next update.
- **note:** a note starting `HOLD (user` keeps the document out of the run list until the date
  it names, or until the user lifts it.
- **stale after:** from the document's own header. Company analyses and funds without one get
  30 days after "as of".
- **rev used:** the skill revision of the latest run. The script compares it with the current
  `**Revision:**` line in the skill.
- **link** (Inputs): `main` sets the update order. `loop` marks a back-reference: for example,
  Equity BBB reads the AI baseline and three company blocks, while those read Equity BBB. A loop
  input is checked once and never restarts the chain.

## Documents

| id | file | skill | type | as of | last change | affects | stale after | rev used | note |
|---|---|---|---|---|---|---|---|---|---|
| oil | docs/oil-market-bbb.md | oil-market-bbb | market | 2026-11-11 | 2026-11-11 | none | 2026-11-30 | 2026-10-24.4 | 11 Nov full update (15% front trigger fired 4 Nov; stale): Base Brent 2027 88 → 84 (physical premium gone, faster recovery outside Iran, strip 81.2); 2028/29, mid-cycle, Bear/Bull and cracks unchanged; stub 104.3 → 97.1, crack 88.1 → 85.1; Russian refining trigger tested, no crack change |
| shipping | docs/oil-shipping-bbb.md | oil-shipping-bbb | market | 2026-10-24 | 2026-10-24 | all | 2026-11-23 | 2026-10-24.1 | 24 Oct re-marked the stub (VLCC 850 → 700, Aframax 245 → 305); paths unchanged |
| rig | docs/rig-market-bbb.md | rig-market-bbb | market | 2026-11-12 | 2026-11-12 | none | 2026-12-12 | 2026-10-10.1 | 12 Nov full update: drillship Bull 2027 450→475, stub 420→455 (six-month rule 455 / 389–499 / 5 fixtures); Base 2027 420 kept (grouped ~438, +4% < 5%); all other paths, MCU, mid-cycle and values kept; SE Asia / ME ranges widened; triggers: stale, Beacon Pacific (stranded HE semi, Serica UK Q3-27), Bull signpost; oil 84 not material; Hercules corrected to Canada |
| supply | docs/supply-market-bbb.md | supply-market-bbb | market | 2026-11-12 | 2026-11-12 | none | 2026-12-12 | 2026-11-12.1 | 12 Nov full update: NS PSV spot Base 2027 £16.5k→£18.5k (75%); PLSV Bear 2028–29 255/250→270/265, Bull mid-cycle 285→300 (2028 round $295–309k confirms Base 295/300); AHTS £75k kept, cut to ~£60–65k if Nov Seabreeze <£50k; Paratus not tracked; affects none |
| hy | docs/hy-market-bbb.md | hy-market-bbb | market | 2026-11-11 | 2026-11-05 | hy-issuers, global-index | 2026-12-05 | 2026-11-08.1 | 11 Nov note: Taptravel vote approved (re-default, no new FTD; longstop 31 Mar 2027); Oct CPI 3.6 / CPI-ATE 2.7 vs MPR 3.8 / 2.7; Riksbank minutes confirm ~2 more hikes; oil Base 2027 84 not material for E&P; DNB CMD noted ([E]); market path +0.17/+0.33/+0.69; all paths and E / R 0.254 kept |
| equity | docs/equity-market-bbb.md | equity-market-bbb | market | 2026-11-06 | 2026-11-06 | global-index | 2026-12-06 | 2026-10-24.1 | Update 2 (6 Nov): full update on 5 Nov closes after HY 5 Nov, midterms and Q3. World Base 5.2% → 6.6% (mostly the ~4% price fall; Amazon and Micron now company blocks), Oslo 2.5% → 2.6% (re-marked). E / R World 0.024 → 0.080, Oslo −0.06 vs HY ref 0.254. Trigger 1 World −14.3% (URTH NOK ≈ 1,590), Oslo 1,492. World 1.6% above its pre-alert (1,827). NOK Base spot flat at I-44 107.8 / USD/NOK 9.29 |
| ai | docs/ai-market-bbb.md | ai-market-bbb | market | 2026-11-12 | 2026-11-11 | amzn, dnbtek, equity, global-index, googl, msft, nvda | 2026-11-17 | 2026-11-11.2 | 11 Nov re-run (skill 2026-11-11.2), Option D of review-ai-k1: K1 capex cycle section; K1 Base 1,170 / 1,170 (was 1,250 / 1,300); H1 750 / 745, EPS .91 / .88 / .87; H4 129 / 130; E cash conversion −.20 / .11 / .36; ratio 0.24 / 0.31; H2, H3, E1, E2, T kept; no re-mark; all six 10.0% → 9.2%, H1 11.2% → 7.5% |
| defense | docs/defense-market-bbb.md | defense-market-bbb | market | 2026-10-31 | 2026-10-07 | all | 2027-01-04 | 2026-10-10.1 | **HOLD (user): no update until the user lifts it.** Initial baseline |
| hy-issuers | docs/hy-issuers.md | hy-market-bbb | book | 2026-11-11 | 2026-11-09 | hy-funds | 2026-11-18 | 2026-11-08.1 | 9 Nov short update on Fondsfinans' October report and 31 Oct holdings: Sigma 79.2 Distressed, Foxway 93.7, Magnolia 88.0, Heimstaden hybrid new (84.7), Varel out [A], Hofseth ~72 confirmed; named loss HH 2.15, HH+ 2.06, FF 0.34, FFK 0.09, SIS 1.10; Stamdata screen not re-run |
| hy-funds | docs/hy-funds-analysis.md | hy-market-bbb | book | 2026-11-09 | 2026-11-09 | none | 2026-12-05 | 2026-11-08.1 | 9 Nov full re-run on the October reports and 5 Nov HY BBB: all five Attractive; E / R FFK 0.520, FF 0.491, HH+ 0.422, SIS 0.343, HH N 0.340 (134% of 0.254; rests on the NOK report yield, 0.267 on the box yield); 6 Nov Marginal reading withdrawn; oil follow-up pending; Arctic Return L rerun (October report): E / R 0.119 → 0.109, 43% of 0.254, not graded |
| dof | docs/DOF-analysis.md | iaf-valuation | company | 2026-11-12 | 2026-11-12 | none | 2026-12-12 | 2026-11-10.1 | 12 Nov full update after Q3 (iaf 2026-11-10.1 layout): Base 11.8%, P_k NOK 127.9 at NOK 128.60 / USD/NOK 9.552, margin −0.6% → marginal (was 9.0%, fails); PLSV $295–305k are Petrobras totals (charter + services), DOF basis flat (> $500m over 4,380 days ≈ extension level), no hidden upside; Implementer ~$133m and SALT ~$103m each from the Q3 chart; FX-sensitive (fails at 9.29, clears at 9.80) |
| plsv | docs/PLSV-analysis.md | - | static | - | - | - | - | - | No longer tracked (user, 25 Oct 2026). Last version 19 Oct; kept as a source (Fontis seller credit, Seagems fleet data cited by borr, rig and supply) |
| sed | docs/SED-analysis.md | iaf-valuation | company | 2026-11-04 | 2026-10-18 | all | 2026-11-17 | 2026-11-01.1 | 27 Oct news update: T-16 award (Base 8.3% → 6.7%, still fails) |
| borr | docs/borr-analysis.md | iaf-valuation | company | 2026-11-07 | 2026-11-07 | all | 2026-11-18 | 2026-11-01.1 | **HOLD (user, 7 Nov): only on request. Not interesting as an equity; its value is the credit read for the Borr bonds in hy-issuers.** v3 24 Oct: Base unchanged (no equity value), Bull 8.3% → 11.2%; Q3 date not announced (4–18 Nov expected) |
| odl | docs/odl-analysis.md | iaf-valuation | company | 2026-11-13 | 2026-11-13 | none | 2026-12-13 | 2026-11-12.1 | v2.1 13 Nov (ex-dividend re-mark, compacted 721 → 450 lines): Base 8.1% → 9.0%, P_k $9.97 (NOK 95.5) vs $10.74 (NOK 102.80), margin −7%, fails; Deepsea Bergen contract signed 10 Nov (already firm in the model) |
| scatec | docs/scatec-analysis.md | iaf-valuation | company | 2026-10-30 | 2026-10-30 | all | 2027-02-28 | 2026-10-29.1 | v2 30 Oct after Q3: clears (Base IRR 16.4%, P_k NOK 95.5 vs 84.65, +13%); Bear −17.9%, Bear corp. NIBD NOK 8.5bn by 2029; Q4 report 29 Jan 2027 |
| capt | docs/capt-analysis.md | iaf-valuation | company | 2026-11-08 | 2026-10-24 | all | 2026-11-23 | 2026-10-18.2 | HOLD (user, 9 Nov): only on request. Position sold. 8 Nov news note: Amor 15-month TC (~$160–180k/day, $73.1–82.2m), ~+$14m in Base (+NOK 1/share), not modelled, verdict unchanged (fails); model on the 24 Oct inputs |
| hafnia | docs/hafnia-analysis.md | iaf-valuation | company | 2026-11-05 | 2026-10-24 | all | 2026-11-18 | 2026-11-01.1 | v6 exit check on the v5 model of 17 Oct |
| kog | docs/kongsberg-analysis.md | iaf-valuation | company | 2026-10-29 | 2026-10-29 | all | 2026-11-28 | 2026-10-18.2 | **HOLD (user): no update until the user lifts it.** Version 2 (29 Oct, Q3 report, method 2026-10-18.2): Base −19.9% → −16.2%, fails; record backlog NOK 174bn |
| rhm | docs/rheinmetall-analysis.md | iaf-valuation | company | 2026-10-07 | 2026-10-07 | all | 2026-11-06 | 2026-10-07.1 | **HOLD (user): no update until the user lifts it.** |
| amzn | docs/amzn-analysis.md | iaf-valuation | company | 2026-11-11 | 2026-11-11 | ai, dnbtek, equity | 2026-11-20 | 2026-11-10.1 | Version 2 (30 Oct, Q3 report): Base 6.8% → 9.2%, P_k $221.5 vs $240.35, fails; OpenAI $50bn preferred added (missing in v1) |
| dnb | docs/dnb-analysis.md | iaf-valuation | company | 2026-11-10 | 2026-10-22 | all | 2026-11-21 | 2026-10-18.2 | Update 1 after Q3, amended 22 Oct; 10 Nov note: CMD targets (ROE > 15% and C/I < 38% towards end-2028; payout and CET1 unchanged), ~0.5 pp above Base ROE 2028, verdict unchanged |
| googl | docs/googl-analysis.md | iaf-valuation | company | 2026-11-11 | 2026-10-28 | all | 2026-11-20 | 2026-11-10.1 | Version 2 (28 Oct) + price re-mark 1 Nov at the 30 Oct close $279.84: Base 4.6% → 9.6%, P_k $261.6 (−6.5%), fails; E / R 0.116; triggers: k $261.6, HY E / R $256.1 |
| shb | docs/handelsbanken-analysis.md | iaf-valuation | company | 2026-10-24 | 2026-10-24 | all | 2026-11-23 | 2026-10-18.2 | HOLD (user, 12 Nov): no update until 3 Feb 2027 (year-end report). Version 2 |
| msft | docs/msft-analysis.md | iaf-valuation | company | 2026-11-07 | 2026-10-28 | all | 2026-11-20 | 2026-11-01.1 | Version 3 (28 Oct, Q1 FY27 report and call): Base 8.8% → 9.5%, fails |
| mu | docs/mu-analysis.md | iaf-valuation | company | 2026-11-05 | 2026-11-05 | none | 2026-11-17 | 2026-11-01.1 | v3 5 Nov price re-mark on the 5 Nov sell-off close $656.39 (was $856.49): Base 6.3% → 18.3%, P_k $751.6, margin −12.6% → +14.5%, fails → clears; Bear −1.7%, Bull 32.0%; E / R 0.616 vs HY BBB reference 0.254; model blocks kept; existing margin rule (not cycle-first); AI BBB layer method prices Micron at 1.05× Base 2028–30 (method gap) |
| nvda | docs/nvda-analysis.md | iaf-valuation | company | 2026-11-12 | 2026-11-12 | ai, dnbtek, equity, global-index | 2026-11-17 | 2026-11-12.1 | v1.5 12 Nov news update at $165.82 (13:25 ET): Huang resigned (8-K), Kress interim CEO, Jones first chair; AI BBB 11 Nov path taken in: Base 17.8%, P_k $192.5, +16.1%, clears (≤ $188.7, fails ≥ $196.4); Bear −5.4% (cross-funding costs), Bull 37.2%; E / R 0.289; cross-funding is equity plus contingent credit, NVIDIA money ~3–5% of DC revenue; sensitivities: funding stop 17.1%, diversion closure 16.6%, CEO de-rating exit 15 13.8% / 13 9.5%, all three 12.1% marginal; Step 7 layout, 107 → 51 KB |
| skh | docs/skhynix-analysis.md | iaf-valuation | company | 2026-11-04 | 2026-10-28 | all | 2026-11-20 | 2026-11-01.1 | Version 2 (28 Oct, Q3 report): Seoul Base 21.1%, clears; ADR marginal at the post-report price; Seoul line and SKHY ADR line |
| smsn | docs/samsung-analysis.md | iaf-valuation | company | 2026-11-04 | 2026-10-29 | all | 2026-11-28 | 2026-11-01.1 | Version 2 (29 Oct, Q3 report): common Base 26.9% → 23.3%, preference 29.5% → 25.6%, both clear; common, preference and GDR lines |
| kospi | docs/kospi-analysis.md | iaf-valuation | fund | 2026-11-06 | 2026-11-06 | all | 2026-11-17 | 2026-11-01.1 | Version 1.8 (6 Nov): price re-mark on the 6 Nov Seoul close after the 5–6 Nov chip sell-off (look-through −10.5% in KRW; IQQK EUR 99.2 → 88.6); paths and company blocks unchanged; HY reference now from HY BBB (0.254); price implies 0.61× Base 2028–30 for k (0.80×); Base ~21% (16%), P_k ~EUR 110 (unchanged), margin +25% (+11%); capped Bear −8%/yr, 2027 −39%; E / R 0.249 vs 0.254 (reference only); neither reads nor writes the portfolio |
| stb | docs/storebrand-analysis.md | iaf-valuation | company | 2026-10-24 | 2026-10-19 | all | 2026-11-23 | 2026-10-18.2 | Date from the file |
| tsm | docs/tsm-analysis.md | iaf-valuation | company | 2026-11-11 | 2026-11-11 | none | 2026-11-17 | 2026-11-10.1 | v1.2 11 Nov (daily run): October revenue +59.7% y/y (above the +45% signpost, not crossed: set into 2027) and November board; re-mark at $396.48 (10 Nov close): Base 13.7% → 9.5%, P_k $369.8, margin −6.7%, clears → fails on price |
| global-index | docs/global-index-funds-analysis.md | iaf-valuation | fund | 2026-11-01 | 2026-10-29 | all | 2026-11-17 | 2026-10-29.1 | Re-mark 29 Oct (MSFT v3, GOOGL v2, AI Update 5): Base −0.08 pp (DNB Global Indeks A 4.58%, Nordnet Global Indeks 4.73%), both fail; NAV date kept at 15 Oct; AI E-layer .92 not stacked on the company blocks; from the next run DNB Global Indeks A only (Nordnet Global Indeks dropped, user 1 Nov) |
| dnbtek | docs/dnb-teknologi-analysis.md | iaf-valuation | fund | 2026-11-06 | 2026-11-06 | none | 2026-11-17 | 2026-11-01.1 | 6 Nov re-run (NAV 7,381.56 on 4 Nov; 5 Nov est. ≈ 7,145): Base 8.6% (10.0% at 5 Nov est.), P_k NAV 6,721, margin −8.9% (−5.4%), fails; E / R 0.113 vs new HY ref 0.254 (trigger NAV 6,399); 30 Sep holdings (ASML in); NVDA v1.2, TSM v1.1, GOOGL re-mark |
| iaf-notes | docs/iaf-reference-notes.md | - | static | - | - | - | - | - | Background, not updated |
| review-2029 | docs/review-2029-step-down.md | - | static | - | - | - | - | - | Review, not updated |
| review-equity | docs/review-equity-market-bbb.md | - | static | - | - | - | - | - | Review, not updated |
| review-hy | docs/review-hy-funds-and-defaults.md | - | static | - | - | - | - | - | Review, not updated |
| review-iaf-exit | docs/review-iaf-exit.md | - | static | - | - | - | - | - | Review, not updated |
| review-kospi | docs/review-kospi-analysis.md | - | static | - | - | - | - | - | Review, not updated (1 Nov 2026: quality and risk of kospi-analysis v1.6 for an IQQK position) |
| review-ai-debt | docs/review-ai-debt-and-market-power.md | - | static | - | - | - | - | - | Review, not updated (5 Nov 2026: debt-funded AI expansion, data-centre multiples and market power). Not adopted (user, 6 Nov): its skill additions (2026-11-05.1) and baseline changes reverted; a dated record, not an input |
| review-ai-h1 | docs/review-ai-h1-non-k1-funding.md | - | static | - | - | - | - | - | Review, not updated (11 Nov 2026: AI BBB checkpoint 10, H1 compute bought outside K1 and its funding; Option A+ adopted by the user and applied 11 Nov (ai-market-bbb 2026-11-11.1)) |
| review-ai-k1 | docs/review-ai-k1-sustainability.md | - | static | - | - | - | - | - | Review, not updated (11 Nov 2026: is K1 Base the most likely path or the companies' plan; return gap; recommends Option D, a cycle-first K1 section with K1 Base 790 / 1,120 / 1,170 / 1,170; Option D adopted by the user and applied 11 Nov (ai-market-bbb 2026-11-11.2)) |
| weekly | docs/weekly-update.md | update-chain | static | - | - | - | - | - | Running report of the weekly run and the midweek check; read by no document |

## Inputs

| document | reads | input as of | link | reads what |
|---|---|---|---|---|
| shipping | oil | 2026-10-24 | main | Crude and product prices, volumes, disruptions |
| rig | oil | 2026-11-11 | main | Brent path, long end, mid-cycle |
| supply | oil | 2026-11-11 | main | Oil path (FID and tender logic) |
| supply | rig | 2026-11-12 | main | Rig activity for OSV demand |
| hy | oil | 2026-11-11 | main | E&P row; scenario mapping |
| hy | rig | 2026-11-04 | main | Oil Service row (drillers) |
| hy | supply | 2026-11-04 | main | Oil Service row (OSV, subsea) |
| hy | shipping | 2026-10-24 | main | Shipping row (tankers) |
| equity | oil | 2026-11-04 | main | Oslo and World energy |
| equity | hy | 2026-11-05 | main | NIBOR path, Bear macro, HY return, reference E / R |
| equity | ai | 2026-11-05 | loop | AI layer paths in World |
| equity | msft | 2026-11-04 | loop | Company block in World |
| equity | googl | 2026-11-04 | loop | Company block in World |
| equity | nvda | 2026-11-05 | loop | Company block in World |
| equity | amzn | 2026-11-04 | loop | Company block in World (from 6 Nov) |
| equity | mu | 2026-11-05 | loop | Company block in World (from 6 Nov) |
| ai | equity | 2026-11-06 | main | Scenarios, NOK path, World |
| ai | hy | 2026-11-11 | main | NIBOR, HY reference E / R |
| ai | mu | 2026-11-05 | loop | Company check |
| ai | amzn | 2026-11-11 | loop | Company check |
| ai | nvda | 2026-11-11 | loop | Company check |
| ai | tsm | 2026-11-11 | loop | Company check |
| ai | msft | 2026-11-07 | loop | Company check |
| ai | googl | 2026-11-11 | loop | Company check |
| ai | skh | 2026-11-04 | loop | Company check (layer method only until 24 Oct; not yet read) |
| ai | smsn | 2026-11-04 | loop | Company check (layer method only until 24 Oct; not yet read) |
| defense | hy | 2026-10-24 | main | Nordic GDP |
| defense | oil | 2026-10-24 | main | Gulf export row |
| hy-issuers | hy | 2026-11-05 | main | Bear default rates, status scale |
| hy-funds | hy | 2026-11-05 | main | Market paths, NIBOR, reference E / R |
| hy-funds | hy-issuers | 2026-11-09 | main | Named bond losses per fund |
| hy-funds | scatec | 2026-10-30 | loop | Scatec bond holdings (Sissener Corporate Bond, Fondsfinans High Yield): issuer credit check (Bear corporate NIBD, 2028 refinancing); not yet read |
| dof | supply | 2026-11-12 | main | NS and Brazil rows, anchors, economic life |
| dof | equity | 2026-11-06 | main | Exit cross-check, NOK path |
| dof | hy | 2026-11-11 | main | Bear HY spread (2030 refinancing) |
| sed | rig | 2026-11-04 | main | Tender-assist row, rig values |
| sed | oil | 2026-10-24 | main | Background |
| sed | equity | 2026-10-18 | main | Exit cross-check, NOK path |
| borr | rig | 2026-11-04 | main | Jackup rates, MCU, rig values |
| borr | oil | 2026-11-04 | main | Background via rig scenarios |
| borr | equity | 2026-11-06 | main | Exit cross-check, NOK path |
| odl | rig | 2026-11-12 | main | HE semis (NCS) row: rates, MCU, mid-cycle, asset convention, fixtures |
| odl | oil | 2026-11-11 | main | Background via rig scenarios |
| odl | equity | 2026-11-06 | main | Exit cross-check, NOK path |
| scatec | equity | 2026-10-18 | main | Exit cross-check, NOK path |
| scatec | hy | 2026-10-24 | main | Bear refinancing spread (corporate bonds from 2028) |
| capt | shipping | 2026-10-24 | main | VLCC and Aframax rows, stub, values |
| capt | oil | 2026-10-24 | main | Background |
| capt | equity | 2026-10-18 | main | Exit cross-check, NOK path |
| capt | hy | 2026-10-24 | main | NIBOR, reference E / R (via equity) |
| hafnia | shipping | 2026-10-24 | main | LR2, LR1, MR rows, stub, values |
| hafnia | oil | 2026-11-04 | main | Background |
| hafnia | equity | 2026-10-18 | main | Exit cross-check, NOK path |
| kog | defense | 2026-10-07 | main | Segment order and revenue paths |
| kog | hy | 2026-10-24 | main | NIBOR on cash |
| kog | equity | 2026-10-18 | main | Exit references (Oslo exit P/E, P/B, mid-cycle return) |
| rhm | defense | 2026-10-07 | main | Segment order and revenue paths |
| amzn | ai | 2026-11-07 | main | E2 cloud row, K1 capex, E-layer EPS and exit P/E |
| amzn | equity | 2026-11-06 | main | Macro scenarios, NOK path |
| amzn | hy | 2026-11-05 | main | NIBOR (E / R) |
| dnb | equity | 2026-10-18 | main | Scenarios, Oslo financials block |
| dnb | hy | 2026-10-17 | main | NIBOR path |
| dnbtek | ai | 2026-11-05 | main | Layer EPS paths, exit P/Es |
| dnbtek | equity | 2026-11-06 | main | World scenarios, NOK path |
| dnbtek | amzn | 2026-11-04 | main | Company block CA |
| dnbtek | nvda | 2026-11-05 | main | Company block CN |
| dnbtek | tsm | 2026-11-05 | main | Company block CT |
| dnbtek | msft | 2026-11-04 | main | Company block CM |
| dnbtek | googl | 2026-11-04 | main | Company block CG |
| dnbtek | mu | 2026-11-05 | loop | Memory evidence (the fund holds no Micron) |
| dnbtek | skh | 2026-11-04 | main | SK hynix company block (from 31 Oct; layer path only until 22 Oct) |
| dnbtek | smsn | 2026-11-04 | main | Samsung company blocks, common and preference (from 31 Oct; layer path only until 22 Oct) |
| googl | ai | 2026-11-07 | main | E2 cloud row, K1 capex, E-layer EPS |
| googl | equity | 2026-11-06 | main | Macro scenarios, NOK path |
| googl | hy | 2026-11-05 | main | NIBOR (E / R) |
| shb | equity | 2026-10-18 | main | Scenarios, Oslo financials block, NOK path |
| shb | hy | 2026-10-24 | main | Sweden GDP, Riksbank, NIBOR |
| msft | ai | 2026-11-07 | main | E2, T1, T3 rows, K1 capex |
| msft | equity | 2026-11-06 | main | Macro scenarios, NOK path |
| mu | ai | 2026-11-05 | main | H2 memory layer |
| mu | equity | 2026-10-18 | main | Scenarios, exit cross-check |
| mu | hy | 2026-11-05 | main | NIBOR (E / R) |
| mu | skh | 2026-10-22 | loop | Peer comparison (from the SK hynix analysis, not only market multiples; not yet read) |
| mu | smsn | 2026-10-22 | loop | Peer comparison (from the Samsung analysis, not only market multiples; not yet read) |
| nvda | ai | 2026-11-11 | main | H1 compute layer (11 Nov re-run held to the 17 Nov run, deferral rule) |
| nvda | equity | 2026-11-06 | main | Scenarios, NOK path |
| nvda | hy | 2026-11-11 | main | NIBOR (E / R) |
| skh | ai | 2026-11-01 | main | H2 memory layer: EPS path, exit P/E, scenarios |
| skh | equity | 2026-10-18 | main | Scenarios, I-44 path (NOK memo), exit cross-check |
| skh | hy | 2026-10-24 | main | NIBOR (E / R), HY reference E / R |
| skh | nvda | 2026-11-02 | main | NVIDIA as main HBM customer, supply commitments |
| skh | mu | 2026-10-22 | main | Peer on the same H2 path |
| skh | smsn | 2026-10-25 | loop | Peer comparison (Samsung analysis; not yet read) |
| smsn | ai | 2026-11-01 | main | H2 memory layer: EPS path, exit P/E, revenue index, scenarios |
| smsn | equity | 2026-10-18 | main | Scenarios, I-44 path (NOK memo), exit cross-check |
| smsn | hy | 2026-10-24 | main | NIBOR (E / R), HY reference E / R |
| smsn | nvda | 2026-11-02 | main | NVIDIA as main HBM customer, supply commitments |
| smsn | mu | 2026-10-22 | main | Peer on the same H2 path |
| smsn | skh | 2026-10-28 | main | Peer on the same H2 path; template for the build |
| kospi | smsn | 2026-11-04 | main | Company blocks: Samsung common and preference (D_t, V_t, capped Bear) |
| kospi | skh | 2026-11-04 | main | Company block: SK hynix, also driving the SK holdcos block |
| kospi | ai | 2026-11-05 | main | H2 memory scenarios and catalysts, capped-Bear diagnostic, memory basket row |
| kospi | equity | 2026-11-06 | main | I-44 path for KRW, World return and exit references |
| kospi | hy | 2026-11-05 | main | NIBOR window (E / R), HY market reference E / R (0.254 from 6 Nov) |
| kospi | hy-funds | 2026-11-01 | main | HY Base after fee, Bear 2027 (the HY market reference comes from hy from 6 Nov) |
| kospi | nvda | 2026-11-05 | loop | Memory evidence only (HBM demand; no company block) |
| kospi | mu | 2026-11-05 | loop | Memory evidence only (no company block) |
| kospi | global-index | 2026-11-01 | main | World index-fund comparison row |
| kospi | dnbtek | 2026-11-06 | main | DNB Teknologi comparison row |
| stb | equity | 2026-10-18 | main | Scenarios, Oslo block F, exit references |
| stb | hy | 2026-10-24 | main | NIBOR path, GDP, HY return |
| tsm | ai | 2026-11-07 | main | H3 foundry layer |
| tsm | nvda | 2026-11-05 | main | NVIDIA as TSMC's main customer |
| tsm | equity | 2026-11-06 | main | Scenarios, NOK path |
| tsm | hy | 2026-11-05 | main | NIBOR (E / R) |
| global-index | equity | 2026-10-18 | main | World blocks, scenarios, NOK path |
| global-index | ai | 2026-10-29 | main | Layer paths |
| global-index | msft | 2026-10-29 | main | Company block |
| global-index | googl | 2026-10-29 | main | Company block |
| global-index | nvda | 2026-10-17 | main | Company block |
| global-index | oil | 2026-10-24 | main | Energy block |
| global-index | hy | 2026-10-24 | main | NIBOR (E / R) |
| dnbtek | hy | 2026-11-05 | main | NIBOR (Base window 4.38%), HY market reference E / R (0.254 from 6 Nov) |
| dnbtek | hy-funds | 2026-11-01 | main | Sissener R and E / R (the HY market reference comes from hy from 6 Nov) |
| dnbtek | global-index | 2026-10-29 | main | DNB Global Indeks A as the World index-fund row |
| equity | global-index | 2026-11-01 | loop | AI-split flags used for the 17 Oct World rebuild |
| global-index | hy-funds | 2026-10-24 | main | HY market reference E / R 0.196 |
| hy | hy-issuers | 2026-11-09 | loop | Held-company news screen behind the default log |
| mu | hy-funds | 2026-11-01 | main | HY market reference E / R 0.196 |
| msft | hy | 2026-11-05 | main | NIBOR (E / R) |

## Not links

Pairs where a document's header names another document, but it is not an input. The lint
(`update_check.py lint`) skips these. Add a row here only after judging that the reference is
not an input; otherwise add an Inputs row.

| document | names | why |
|---|---|---|
| ai | dnbtek | Update 6 cites DNB Teknologi's E-layer blend (≈ .91) only as a cross-check; dnbtek reads ai, not the reverse |
| dof | oil | Used only through Supply BBB (scenario mapping) |
| dof | rig | Used only through Supply BBB (scenario mapping) |
| global-index | tsm | TSMC is not in MSCI World or the Climate Change index |
| hy | hy-funds | Context only: the 11 Nov note cites the October spread read from Fondsfinans' report in hy-funds; hy-funds reads hy |
| hy-issuers | hy-funds | Downstream: hy-funds charges the watchlist's losses (hy-funds reads hy-issuers) |
| defense | kog | Downstream: kog reads defense; defense quotes Kongsberg's reported orders only as evidence via the Kongsberg report events (weekly run 31 Oct) |
| odl | hy | Header states HY BBB is not used: fixed-rate USD bond, no maturity inside the horizon |
| borr | hy-issuers | Credit signal only (Watch status, derived ~93): no figure in the IAF build reads it (7 Nov, weekly run) |
| msft | googl | Method precedent for the re-mark layout only, no value read (7 Nov, weekly run) |

## Events

Planned events that should trigger a re-run. "firm" is `yes` for an announced date, `approx`
when the header gives only a period.

- **status `open`:** a re-run trigger. Once it has passed and is still `open`, the check flags its
  documents for update.
- **status `watch`:** a data release or a decision where no change is expected. It shows in the
  upcoming events and is read at the documents' next run, but it never flags an update on its own.
- **`done` / `dropped`:** dealt with, or no longer relevant.

If a `watch` event surprises (for example, a central bank moves when a hold was expected), change
it to `open`.

| date | firm | event | affects | status |
|---|---|---|---|---|
| 2026-10-21 | yes | Handelsbanken Q3 report | shb | done |
| 2026-10-21 | yes | Storebrand Q3 report | stb | done |
| 2026-10-23 | yes | DOF sells Skandi Implementer (2018 CSV), delivery Q2 2027, price not disclosed; "material reduction" in net debt (Newsweb 23 Oct; daily news 26 Oct) | dof | done |
| 2026-11-05 | yes | DOF: Petrobras extends DOFCON PLSV Skandi Olinda 304 days, Apr 2027 → Jan 2028 (rate undisclosed); Buzios, Olinda and Recife now all end Jan 2028 (dof news note 6 Nov) | dof | done |
| 2026-11-09 | yes | DOF: option declared on the AHTS Skandi Mariner, firm from Q2 2027 to Q3 2028, value Significant ($15–25m) (dof news note 9 Nov; place in the model at Q3) | dof | done |
| 2026-11-09 | yes | Petrobras PLSV tender final results (Fearnley via TDN, 9 Nov): DOFCON Buzios $305k, Recife and Olinda $295k/day; Paratus Sapura Jade $309k; 4 years from 1 Jan 2028; signatures remain (dof news note 10 Nov) | dof | done |
| 2026-11-09 | yes | Brazil PLSV data point for the supply BBB's next run: four vessels at $295–309k/day from 2028 (Base row 2028 295, 2029 300) | supply | done |
| 2026-11-08 | yes | NVIDIA board opens an independent probe into the CEO (reported intelligence link); no timeline; stock −4.3% 9 Nov, −6.1% 10 Nov. Read at the Q3 run (17 Nov) | nvda, ai | watch |
| 2026-11-10 | approx | Possible new US export controls on NVIDIA AI chips to China (The Information, 10 Nov) and congressional briefing requests; China already excluded from NVIDIA Base | nvda, ai | watch |
| 2026-11-06 | yes | CAPT: 15-month TC for the Suezmax Amor from Nov 2026, revenue $73.1–82.2m (~$160–180k/day gross), subject to vetting (capt news note 8 Nov) | capt | done |
| 2026-11-06 | yes | Period-market data point: CAPT Amor (2026 dual-fuel Suezmax) 15-month TC at ~$160–180k/day gross; read at the shipping BBB's next run | shipping | watch |
| 2026-10-23 | yes | Intrum Q3 report: net loss SEK 1.49bn incl. SEK 1.52bn goodwill impairment (Germany); shares −39% intraday; servicing leverage 4.5x; bond price not found (daily news 26 Oct) (hy-issuers read 31 Oct) | hy-funds | done |
| 2026-10-25 | yes | Brazil presidential runoff | supply | done |
| 2026-10-26 | yes | Westwood weekly rig count, first after the Gulf escalation (not public by 28 Oct; the 2 Nov count covers it) | rig, borr | done |
| 2026-10-26 | yes | First Borr bond (2032/2034) and share prices after the Prospector 5 loss; Borr's own statement (insurance, BW Energy) | hy-issuers, borr | done |
| 2026-10-27 | yes | Heimdal Høyrente N NAV for 26 Oct: indirect signal for Borr's 2032/2034 notes (no bond price found on 26 Oct). Outcome: superseded by the manager's mark decomposition read into hy-issuers 31 Oct; Borr signal now the October report (~6 Nov) (weekly run 31 Oct) | hy-issuers | done |
| 2026-10-27 | yes | SED (Energy Holdings): CPOC letter of award for T-16, Phase 7, 30 months firm from early Q3 2027 + up to 15 months options, ~USD 87m firm incl. mobilisation; Phase 6 ends Q1 2027, rig idle in Singapore at reduced cost until Phase 7 (mfn 27 Oct; daily news 27 Oct). Tender-assist market print | rig | done |
| 2026-10-28 | yes | Microsoft Q3 report (FY27 Q1) (msft read 28 Oct, v3; Azure +48%, guided 49–50%; RPO flat q/q) | ai | done |
| 2026-10-28 | yes | FOMC decision (DNB Carnegie: hold at 3.75–4.00%, hike in Dec; hawkish dissents possible). Outcome: hold at 3.75–4.00%, 10–2 vote; Dec hike priced (weekly run 31 Oct) [E] | equity, ai | done |
| 2026-10-28 | yes | UK Budget (Chancellor) — UK defence spending | defense | done |
| 2026-10-28 | yes | Norway retail sales Sep (DNB Carnegie: +0.5% M/M) | hy | watch |
| 2026-10-28 | yes | Alphabet Q3 report (googl read 28 Oct, v2; Cloud +103%, far above E2) | ai | done |
| 2026-10-28 | yes | SK hynix Q3 report and further shareholder returns (skh read 28 Oct, v2; kospi read v2 28 Oct) | ai, smsn | done |
| 2026-10-29 | approx | Alphabet Q3 call transcript re-check: 2026/2027 capex guide, Cloud backlog, TPU, buybacks (call not read in v2) | googl | done |
| 2026-10-29 | yes | Amazon Q3 report (amzn read 30 Oct, v2; AWS +39%, 'over 40%' in 2027–28 per Jassy; backlog $578bn) | ai | done |
| 2026-10-29 | yes | BW Energy Q3 report (Dussafu campaign and the Prospector 5 contract) | borr | done |
| 2026-10-29 | yes | ECB decision (DNB Carnegie: hold at 2.50%; hikes in Dec and Mar). Outcome: hold at 2.50%; Sep HICP 3.8%; Dec hike still priced; Lagarde to step down in Feb 2027 (weekly run 31 Oct) [E] | equity, hy | done |
| 2026-10-29 | yes | US Q3 GDP (DNB Carnegie 3.2% ann.) and Sep PCE (core +0.3% M/M). Outcome: GDP +3.4% ann. (BEA advance), Q3 PCE prices +2.1% ann.; no surprise (weekly run 31 Oct) [F] | equity | done |
| 2026-10-29 | yes | Sweden GDP indicator Q3 (DNB Carnegie +0.5% Q/Q) | hy, shb | watch |
| 2026-10-30 | yes | Norway registered unemployment Oct (DNB Carnegie 2.1%); Norges Bank FX purchases for Nov (a clearly larger daily NOK sale than Oct = the oil-tax tailwind to NOK fades from Nov) | hy, equity | watch |
| 2026-10-30 | yes | Euro-area and France Q3 GDP (advance), France Oct CPI | equity, defense | watch |
| 2026-10-30 | yes | Scatec Q3 report (Philippine reserve-market impact on Q4 and 2027, net debt at 30 Sep, EBRD Egypt platform terms) | scatec | done |
| 2026-10-29 | yes | Samsung Electronics Q3 report (HBM4, 2027 memory pricing, DX loss, 2027 capex) and the board's Q3 dividend (~KRW 30tn, late Oct) (smsn read 29 Oct, v2); ai read 29 Oct (Update 5) | kospi | done |
| 2026-10-29 | yes | Kongsberg Q3 report (kog read 29 Oct, v2) | defense | done |
| 2026-10-29 | yes | Heimdal Høyrente NAV −1.4% over the week to 29 Oct (user). 27 Oct −0.74%, decomposed by the manager (Nordnet forum, Heimdal Erik, 28 Oct; user paste) [E]: Intrum bond marked 80 → 73.75 after Q3 (trades 75–77), −0.26%, now 2.87% of NAV (Heimdal added); HX old 2030 loan 25 → 12.5 after a small trade, −0.36%, now 0.34% of NAV, the rest of the HX exposure is in debt moved up the capital structure; swing pricing triggered (technical, normally temporary). Fund yield 8.73% local / 9.77% in NOK after fee. Trustly (TRUSTLY 001, NO0013646943; HH ~3.3%, HH+ 3.36%, SIS 1.84%): fund prices it at 79 (manager, forum ~30 Oct [E]); bid of size 76/77 not filled, one offer 400k at 80.375; watchlist assumed ~95, so a mark-down of ~16 points (~−0.5% of HH NAV) is the likely rest of the week. Heimdal Martin (~30 Oct [E]): yield 9.6% in NOK (8.9% end-Aug); bought more Intrum; EUR/USD bonds are fixed-rate (gain if rates fall), NOK bonds floating. October report (~6 Nov) (hy-issuers read 31 Oct) | hy-funds | done |
| 2026-10-31 | approx | France PLF 2027 (October) | defense | done |
| 2026-10-31 | approx | Westwood September rig dashboard (late Oct) | rig | done |
| 2026-11-01 | yes | OPEC+ meeting | oil | done |
| 2026-11-02 | yes | Transocean Q3 report and fleet status | rig, odl | done |
| 2026-11-02 | yes | Westwood weekly rig count; Valaris Q3 (after close) | rig, borr | done |
| 2026-11-03 | yes | US midterm elections (Democrats won House and Senate; oil read 4 Nov, kept; equity read 6 Nov) | defense | open |
| 2026-11-20 | approx | Equinor AHTS term tender: bids were due 3 Nov, no award announced by 4 Nov (supply checkpoint 13); award expected later | supply | open |
| 2026-11-03 | yes | Odfjell Drilling Q3 report and Q3 dividend (insurance and tax-refund cash, net debt) | odl | done |
| 2026-11-04 | yes | Riksbank rate decision: hiked to 2.00% from 11 Nov, more hikes likely (hy read 5 Nov) | shb | done |
| 2026-11-05 | yes | Norges Bank rate decision | hy | done |
| 2026-11-05 | yes | Rheinmetall Q3 report (also Hensoldt and Renk Q3) | rhm, defense | open |
| 2026-11-04 | yes | TORM Q3 report (signpost and stake for Hafnia) | hafnia | done |
| 2026-11-05 | approx | Valaris, Noble, Seadrill and Borr Q3 reports and fleet status (to early Nov) (rig read Valaris, Noble, Seadrill 4 Nov; Borr ~18 Nov) | borr | done |
| 2026-11-05 | approx | Alphabet Q3 10-Q (early Nov): Cloud backlog, equity-securities split | googl | done |
| 2026-11-06 | approx | October Nordic HY anchor spread (early Nov) | hy | done |
| 2026-11-06 | approx | Seabreeze October report (early Nov) | supply | done |
| 2026-11-06 | approx | Heimdal October monthly reports: Borr's contribution (first price signal for the 2032/2034 notes after the Prospector 5 loss); also confirms the Intrum (73.75), Trustly (79) and HX (12.5 old loan) marks and gives the HH+ figures; and gives the October yield in NOK (basis settled 1 Nov: report yields are NOK) and the size of October's rise | hy-issuers, hy-funds | done |
| 2026-11-06 | yes | Pentagon Europe force-posture recommendation to Hegseth (date firm per defense 31 Oct; NDAA floor 76,000 US troops in Europe) | defense | open |
| 2026-11-09 | yes | Tidewater Q3 report (after the US close; call 10 Nov) | supply | done |
| 2026-11-07 | yes | Hofseth: value-adjusted equity ratio covenant on the EUR 300m bond tightens 25% → 27.5% (26.5% at 30 Jun); bond ~72 (Finansavisen via Salmon Business, 12 Oct [E]); NOK 600m equity raise still not closed (daily news 28 Oct) | hy-issuers, hy-funds | done |
| 2026-11-09 | yes | USTR/China port-fee deadline (9–10 Nov) | shipping | open |
| 2026-11-09 | yes | Taptravel bondholder vote: both procedures approved; effective only when a SEK 50m share issue closes (hy and hy-issuers notes 11 Nov) | hy-issuers, hy | done |
| 2026-11-10 | yes | DNB Capital Markets Day (London): update on financial targets (Newsweb 23 Oct) | dnb | done |
| 2026-11-10 | approx | Fondsfinans October reports (Sissener's read 6 Nov): trigger for the full hy-funds re-run, with Heimdal's NOK report yields | hy-funds, hy-issuers | done |
| 2026-12-08 | approx | Sissener November monthly report | hy-funds | open |
| 2026-12-08 | approx | Fondsfinans November report and holdings: confirms whether Varel has left FF HY and Kreditt | hy-issuers, hy-funds | watch |
| 2027-02-15 | approx | Cegal bond repaid from new NOK 1.8bn bank financing (FF HY position) | hy-issuers | watch |
| 2026-11-10 | yes | SSB October CPI (Norway): CPI 3.6%, CPI-ATE 2.7% vs MPR 3.8 / 2.7 (hy 11 Nov) | hy | done |
| 2026-11-10 | yes | CoreWeave Q3 report and call (5 pm ET): neocloud-funding signpost | ai | done |
| 2026-11-10 | approx | Anthropic roadshow launch; amended S-1 with price range expected first (googl 7 Nov [E]) | googl, ai, amzn | done |
| 2026-11-19 | yes | MSFT ex-dividend $0.98 (paid 10 Dec): re-mark point | msft | open |
| 2026-11-10 | yes | Riksbank minutes (4 Nov decision): unanimous, ~2 more hikes expected (hy read 11 Nov, path kept) | shb | done |
| 2026-11-10 | approx | TSMC October revenue (monthly 6-K, ~10th; date not confirmed): signpost y/y < +25% / > +45% (Sep +54.6%) | tsm, ai | done |
| 2026-11-12 | yes | Bundestag budget committee final session on the 2027 budget (Bereinigungssitzung) | defense, rhm | open |
| 2026-11-16 | approx | US-brokered Russia–Ukraine talks (mid-Nov) | defense | open |
| 2026-11-12 | approx | MSCI November index review announced (effective ~1 Dec): IQQK re-capped (Samsung ~31%, SK hynix ~19%) | kospi | watch |
| 2026-11-12 | yes | DOF Q3 report (supply read it 12 Nov) | dof | done |
| 2026-11-16 | approx | SK hynix Q3 business report (6-K/DART): tax payable and bonus accrual at 30 Sep | skh, ai, kospi | open |
| 2026-11-14 | approx | Samsung Q3 quarterly report on DART: LTA price ranges or floors | smsn, ai, kospi | open |
| 2026-11-17 | yes | NVIDIA Q3 FY27 report. The full re-run also restructures the report to the iaf-valuation 2026-11-10.1 layout (structure review 10 Nov: scenario table, Bear driver breakdown, Base return bridge, history to the change log; fix the 30 Oct multiples left in the exit-anchor text and in For other modules) | nvda, ai, skh, smsn, kospi | open |
| 2026-11-16 | approx | NVIDIA Q3 13F (public stakes at 30 Sep) | nvda, ai | watch |
| 2026-11-18 | approx | Anthropic IPO pricing: marks NVIDIA's stake and its $10bn placement | nvda, ai | watch |
| 2026-12-15 | approx | NDAA final text (AI Overwatch, Chip Security, MATCH Acts) | nvda, ai | watch |
| 2027-02-28 | approx | NVIDIA permanent CEO named (3–4-month search) | nvda, ai | open |
| 2026-11-18 | yes | House closed briefing on NVIDIA requested for 18 Nov (committee chairs Mast, Moolenaar, Crawford; letter 4 Nov); 11 Nov: House Republicans press Huang to testify, subpoena floated (daily news 12 Nov) | nvda, ai | watch |
| 2026-11-12 | approx | NVIDIA board decision on CEO: Huang resigned as CEO and director (8-K 12 Nov, effective 11 Nov); Colette Kress interim CEO and CFO; Harvey Jones first Chair; internal and external search | nvda, ai | done |
| 2026-11-30 | approx | BIS rule blocking Chinese remote access to advanced AI chips via data centres abroad, seven more countries incl. Malaysia, Singapore, Thailand (The Information 11 Nov `[E]`; "could be announced this month") | nvda, ai | open |
| 2026-11-18 | approx | Trump–Xi meeting (18–19 Nov): export policy for AI chips | nvda, ai | watch |
| 2027-02-25 | approx | CoreWeave Q4 2026 report (date not announced): ~$9bn of prepayments received, financing; neocloud-funding signpost | ai | open |
| 2026-11-20 | yes | DOF Q3 dividend $0.40 goes ex (paid 30 Nov); duplicate of the open row "DOF Q3 dividend USD 0.40 goes ex" (13 Nov) | dof | dropped |
| 2027-02-18 | yes | DOF Q4 2026 report and Q4 dividend (paid ~5 Mar) | dof | open |
| 2027-04-07 | yes | DOF annual report, with new broker fleet values | dof | open |
| 2027-02-25 | approx | Tidewater Q4 2026 report (day rates, utilisation by region) | supply | open |
| 2026-12-01 | approx | Silicon Data GPU rental indices (H100, B200), monthly: K1 capex cycle signpost (B200 −20% from its 2026 high for three months, or rising with the curve in contango) | ai | watch |
| 2027-01-31 | approx | AI BBB January roll-forward: re-run the K1 return gauge (k1ret.py) and the K1 cycle judgement on the hyperscalers' first 2027 capex figures; re-set K1 2025 / 2026 to filings (~450 / ~815) | ai | open |
| 2027-01-15 | approx | New Senate: Warren chairs Senate Banking; possible subpoena on NVIDIA's China exposure | nvda | watch |
| 2027-03-15 | approx | Trial of the Supermicro co-founder (chip diversion case) | nvda | watch |
| 2026-11-07 | approx | DNB Teknologi 5 Nov NAV published (first NAV with the 5 Nov sell-off; estimate ≈ 7,145): check against the estimate | dnbtek | watch |
| 2026-11-15 | approx | DNB AM October monthly report for DNB Teknologi with 31 Oct holdings | dnbtek | open |
| 2026-11-19 | yes | SK hynix buyback window ends (24.07m shares for cancellation); finished early on 21 Oct (23.69m shares, KRW 40.0tn; Q3 report) | skh | done |
| 2026-11-18 | yes | Hafnia Q3 report | hafnia | open |
| 2026-11-16 | yes | TORM Q3 dividend USD 1.35 goes ex (Copenhagen 16 Nov, New York 17 Nov; paid 2 Dec) | hafnia | open |
| 2026-11-17 | yes | Petrobras PSV 4500 (5 lots) and PSV 3000 (2 lots) tender proposals open: 4-year firm from Jun–Oct 2027 | supply, dof | open |
| 2026-11-18 | yes | SED Q3 report | sed, rig | open |
| 2026-11-12 | yes | SeaBird (SED) Fulmar Explorer OBN source contract, West Africa, ~6 months from Dec 2026 (supports the SeaBird Base 2027 contribution; read at the SED Q3 run) | sed | watch |
| 2026-11-18 | approx | Borr Q3 report (Investing.com date `[E]`, not yet announced by Borr): first figures after the Prospector 5 loss, insurance position | borr, hy-issuers, rig | open |
| 2026-11-18 | approx | Anthropic IPO pricing (S-1/A of 10 Nov: range $70–78; pricing 18 Nov and first trade ~19 Nov press-reported `[E]`); the $26bn Class N placement closes right after (Google, NVIDIA, AMD, Broadcom, Micron, Microsoft, TSMC): value of Amazon's and Alphabet's stakes, E1 lab revenue; re-mark only if priced outside the range | ai, amzn, googl, msft | open |
| 2026-11-10 | yes | TSMC November board (6-K 10 Nov): 3Q26 dividend NT$9.0 (model NT$8.0), capital appropriations $40.93bn, up to $0.5bn each of Anthropic common (IPO price) and OpenAI preferred | tsm, ai | done |
| 2026-12-10 | approx | TSMC November revenue (monthly 6-K, ~10th; date not confirmed): signpost y/y < +25% / > +45% (Oct +59.7%) | tsm, ai | open |
| 2026-12-10 | yes | TSMC 2Q26 dividend NT$7.0 goes ex (paid 7 Jan 2027) | tsm | watch |
| 2027-03-11 | yes | TSMC 3Q26 dividend NT$9.0 goes ex (paid 8 Apr 2027) | tsm | watch |
| 2026-11-27 | yes | Paratus Q3 report | plsv | dropped |
| 2026-11-27 | yes | German 2027 budget adopted (Bundestag plenary 24–27 Nov; draft defence EUR 139.6bn, procurement > EUR 60bn) | defense, rhm | open |
| 2026-11-27 | approx | Petrobras business plan 2027–31 (late Nov; date not announced). The decisive Brazil signpost after Lula's re-election (E&P vs refining split) | supply | open |
| 2026-11-25 | yes | Trustly Q3 report (and the >USD 40m equity injection closing in November) | hy-issuers, hy-funds | open |
| 2026-11-25 | approx | Norse Atlantic Q3 report (financial calendar, date estimated `[E]`; daily news 2 Nov); held issuer on the watchlist (HH 0.76, HH+ 2.27), status Watch | hy-issuers, hy-funds | open |
| 2026-11-30 | approx | DRAM/NAND monthly contract price print (November) — memory cycle signpost | ai, skh, smsn, kospi | open |
| 2026-11-13 | yes | IEA Oil Market Report (open the oil update if 2027 demand is revised by more than 0.5 mb/d) | oil | watch |
| 2026-12-10 | approx | Brent front ±15% trigger re-armed on the 10 Nov settlement 91.49: F27 ≤ 77.8 or ≥ 105.2 (then G27 ≤ 76.0 or ≥ 102.9), to 10 Dec | oil | watch |
| 2026-11-27 | approx | Westwood October rig dashboard: re-run Rig BBB early if drillship MCU is outside 90–96% or backlog below 150 rig-years | rig | watch |
| 2026-11-30 | approx | Finder KTJ FID for Hakuryu-5 (rig demand) | rig | watch |
| 2026-11-30 | yes | Russian jet fuel export ban ends | oil | watch |
| 2026-12-08 | yes | EIA STEO (December) | oil | watch |
| 2026-12-15 | approx | Signatures of the 2028 Petrobras PLSV round (Buzios, Recife, Olinda, Jade; 4 years from 1 Jan 2028) | supply, dof | watch |
| 2026-12-10 | yes | SSB November CPI (Norway) | hy | watch |
| 2027-03-31 | yes | Taptravel longstop: SEK 50m share issue (Ridge Capital) must close, or event of default | hy, hy-issuers | open |
| 2026-11-29 | yes | OPEC+ meeting (2027 quotas expected) | oil | open |
| 2026-11-30 | approx | Brent F27 15% front-month trigger: a settlement ≤ 96.42 by 30 Nov makes the oil follow-up a full update | oil | done |
| 2026-11-27 | approx | Westwood October rig dashboard (late Nov); duplicate of the watch row with the re-run test (MCU 90–96%, backlog 150 rig-years) (13 Nov) | rig | dropped |
| 2026-11-30 | yes | CAPT Q3 report | capt | open |
| 2026-11-30 | yes | SK hynix Q3 dividend record date (KRW 20,000: 10,000 regular + 10,000 special) | skh, kospi | open |
| 2026-12-11 | approx | FTSE December review (effective mid/late Dec): FLXK re-capped; FLXK no longer followed (no KID at Nordnet, 29 Oct) | kospi | dropped |
| 2026-12-04 | approx | Seabreeze November report: completes the Q4 North Sea spot test (AHTS Bear signpost month 2) | supply | open |
| 2026-12-04 | approx | Heimdal November reports and holdings: second price signal for Borr and the HX super senior bonds; weights after the October outflow | hy-issuers, hy-funds, hy | open |
| 2026-12-10 | approx | Oracle Q2 FY27 report (backlog, cloud infrastructure, capex) (mid-Dec) | ai | open |
| 2026-12-04 | yes | Polish Sejm third reading of the 2027 budget (second reading 2 Dec, Senate 8 Dec) | defense | open |
| 2026-12-09 | approx | Bundestag decision on Arminius (Boxer order, ~EUR 12.4bn for Rheinmetall; secondary source) | rhm, defense | open |
| 2026-12-15 | approx | Storting adopts Norway's 2027 defence budget | defense, kog | open |
| 2026-12-31 | approx | SAFE round 2 allocations (EUR 21.3bn opened 29 Oct; within the existing envelope) and the French 2027 budget final vote | defense | open |
| 2026-12-16 | yes | Micron Q1 FY27 report | mu, ai, skh, smsn, kospi | open |
| 2026-12-31 | yes | Hofseth: first test of the 27.5% value-adjusted equity ratio covenant (EUR 300m bond); breach likely without the NOK 600m equity raise `[E]` | hy-issuers, hy-funds | open |
| 2026-12-31 | approx | Deepsea Nordkapp 2028 rate set by two independent brokers (Aker BP; by end-2026): NCS HE market print for 2028 | odl, rig | open |
| 2026-11-12 | yes | ODL Q3 dividend USD 0.27 goes ex (paid 25 Nov) | odl | done |
| 2026-11-20 | yes | DOF Q3 dividend USD 0.40 goes ex (paid 30 Nov; Q3 report 12 Nov, daily news 12 Nov) | dof | open |
| 2026-11-26 | yes | SSB Q3 national accounts (Norway mainland GDP) | hy | open |
| 2026-11-30 | yes | Dooba and Point Properties deadlines | hy-issuers, hy | open |
| 2026-11-30 | approx | MSCI November month-end fundamentals: MSCI Norway P/BV against the 2.5 warning (2.46 on 30 Oct), MSCI World forward P/E | equity | watch |
| 2026-11-30 | approx | Norges Bank FX purchases for December (November NOK sale unchanged at NOK 176m a day) | hy, equity | open |
| 2026-12-01 | yes | Transocean–Valaris closing expected (all approvals in hand) | rig | open |
| 2026-12-01 | yes | Booster standstill ends | hy-issuers, hy | open |
| 2026-12-10 | approx | ERCOT data-center (large-load) audit due: Texas siting policy, AI BBB state-siting signpost (ai 5 Nov) | ai, kospi | open |
| 2027-02-24 | approx | ODL Q4 2026 report and Q4 dividend (date not announced; Q4 2025 was 25 Feb) | odl | open |
| 2026-12-31 | approx | DRAM/NAND monthly contract price print (December) and TrendForce Q1-27 outlook — memory cycle signpost | ai, skh, smsn, kospi | open |
| 2026-12-11 | yes | US FY27 stopgap expires (lame-duck Congress; war funding) | oil, equity, defense, ai | watch |
| 2026-12-16 | yes | Riksbank rate decision and MPR | hy, shb | open |
| 2026-12-17 | yes | Norges Bank rate decision and MPR 4/26: re-test the NIBOR Base (market path +0.17 / +0.33 / +0.71 pp above Base, 4 Nov); new I-44 projection for the equity Base NOK anchor (spot 2.0% stronger than 110.0; switch at 3%) | hy, equity | open |
| 2026-12-31 | yes | Achilles EUR 100m amortisation | hy-issuers, hy | open |
| 2027-01-03 | yes | New US Congress seated (Democratic House and Senate): war funding and war-powers votes, sanctions | oil, equity, defense, ai | open |
| 2027-01-07 | approx | Samsung Q4 preliminary results (early Jan) | smsn, ai, kospi | open |
| 2027-01-11 | approx | Ohio and Georgia governors sworn in (data-center pause pledges; AI BBB state-siting signpost) | ai, kospi | open |
| 2027-01-12 | approx | HX: company certificate on whether the new super senior bond top-up is needed | hy-issuers, hy-funds | open |
| 2027-01-12 | yes | Texas Legislature convenes: data-center siting and grid-cost bills (AI BBB state-siting signpost) | ai, kospi | open |
| 2027-01-14 | yes | TSMC Q4 report | tsm, ai | open |
| 2027-01-19 | yes | Texas governor sworn in (data-center pause pledge; Abbott's own pause on new loads ≥ 75 MW since 3 Aug) | ai, kospi | open |
| 2027-01-28 | approx | SK hynix Q4 report and the rest of the FY2026 return (~KRW 35tn: year-end dividend and Q4 buyback) (late Jan) | skh, ai, kospi | open |
| 2027-01-27 | approx | Microsoft Q2 FY27 report (late Jan; Yahoo estimate) | msft, ai | open |
| 2027-01-28 | approx | Meta Q4 report and first 2027 capex figure (late Jan; none given on 21 Oct): K1 2027 against 1,120 and the E-rest row | ai | open |
| 2027-01-29 | approx | Samsung Q4 report and board decision on the rest of the 2026 return (KRW 60–80tn) and any 2027+ policy (late Jan) | smsn, ai, kospi | open |
| 2027-01-29 | yes | Scatec Q4 report (first quarter without the Philippine reserve market against the 200–300 guide, any NGCP contract, 2027 guidance, net debt at 31 Dec) (Scatec financial calendar) | scatec | open |
| 2027-02-02 | approx | Alphabet Q4 report and 2027 capex guide (early Feb) | googl, ai | open |
| 2027-02-04 | approx | Amazon Q4 report and first 2027 capex figure (early Feb) | amzn, ai | open |
| 2027-02-04 | yes | Intrum Q4 report | hy-issuers, hy-funds | open |
| 2027-02-03 | yes | Handelsbanken year-end report 2026 | shb | open |
| 2027-02-04 | yes | DNB Q4 2026 report (DNB financial calendar) | dnb | open |
| 2027-02-10 | yes | Storebrand Q4 report | stb | open |
| 2027-02-11 | yes | Kongsberg Q4 report | kog, defense | open |
| 2027-02-11 | approx | HX February coupon: cash, tap or PIK (decides the HX carry basis in Heimdal) | hy-issuers, hy-funds | open |
| 2027-02-15 | approx | Nordic Trustee annual default report (sets the 2027 allowance for unseen defaults) | hy, hy-funds | open |
| 2027-03-31 | approx | SED T-16 Phase 6 ends (Q1 2027, on options after Dec); rig to Singapore, idle until Phase 7; also the Ventura closing long-stop | sed | open |
| 2027-03-31 | approx | Scatec–EBRD Egypt platform closing (SPA signed 22 Oct 2026; closing date and cash to Scatec not disclosed; date assumed) | scatec | open |
| 2027-04-12 | approx | Philippine reserve-market redesign proposal to the ERC (NGCP, PEMC, IEMOP; due within 6 months of the 12 Oct 2026 suspension) | scatec | open |
| 2027-04-15 | approx | French presidential election (April–May 2027): defence budget path after the LPM | defense | open |
| 2027-06-30 | approx | DOF: Skandi Implementer delivered to its buyer (Q2 2027); proceeds repay debt | dof | open |
| 2027-06-30 | approx | Scatec repays SCATC05 (NOK 1,453m, due Q1 2028) in H1 2027 per the Q3 presentation | scatec, hy-funds | open |
| 2027-06-30 | approx | UK 2027 Spending Review (date not set): funds or not the path to 3% / 3.5% of GDP | defense | open |
| 2027-07-01 | approx | SED T-16 Phase 7 (CPOC, 30 months firm) starts (early Q3 2027) | sed | open |

## Change log

Kept in `docs/log/register-log.md` (moved 12 Nov 2026).
