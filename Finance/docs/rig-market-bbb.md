# Rig Market BBB — 12 November 2026

**Status: Final** (full update) · skill `rig-market-bbb` revision **2026-10-10.1** · as of **12 Nov 2026** · **stale after 12 Dec 2026** · compacted 13 Nov 2026 (no value changed)

## Interface (values other documents read)

As of **12 Nov 2026**. Oil input: Oil Market BBB 11 Nov. Cells Bear / **Base (Base range)** / Bull. The stub is the six-month leading edge (fixed sample rule, Metadata) and the latest observed MCU month, identical in all scenarios. Tags: `[F]` fact · `[E]` external forecast or secondary · `[A]` own assumption · `[?]` unknown.

**Leading-edge dayrate, $k/day**

| Segment | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| UDW drillships | 455 | 380 / **420 (400–455)** / 475 | 375 / **455 (425–480)** / 500 | 360 / **470 (430–500)** / 540 | 320 / **360** / 420 |
| HE semis (NCS) | 430 | 410 / **425 (410–440)** / 445 | 400 / **450 (425–475)** / 500 | 380 / **470 (440–500)** / 540 | 350 / **400** / 460 |
| Benign semis | 350 | 310 / **340 (315–365)** / 370 | 290 / **355 (325–385)** / 405 | 280 / **365 (330–400)** / 430 | 260 / **300** / 340 |
| High-spec jackups (composite) | 105 | 92 / **105 (98–112)** / 118 | 88 / **115 (105–125)** / 135 | 85 / **120 (108–132)** / 145 | 92 / **110** / 130 |
| SE Asia jackups (secondary) | 90 | 72 / **90 (80–105)** / 98 | 70 / **95 (85–105)** / 108 | 70 / **98 (88–108)** / 115 | — / **92** / — |
| Tender-assist barges (secondary) | 80 | 68 / **78 (70–88)** / 88 | 65 / **82 (72–92)** / 95 | 65 / **85 (75–95)** / 100 | — / **80** / — |
| Middle East jackups (secondary, Base only) | 90 | **90 (80–100)** | **95 (85–110)** | **100 (88–110)** | **95** |

**MCU, % annual average, and contract cover**

| Segment | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle | Cover 2027 / 28 / 29 `[A]` |
|---|---|---|---|---|---|---|
| UDW drillships | 93 | 88 / **91 (89–93)** / 95 | 86 / **95 (92–97)** / 97 | 83 / **94 (90–97)** / 97 | 82 / **88** / 92 | ~70 / 45 / 25 |
| HE semis (NCS) `[A]` | 97 | 92 / **97 (95–98)** / 98 | 88 / **96 (93–98)** / 98 | 83 / **93 (89–96)** / 97 | 85 / **92** / 96 | ~96 / ~83 / ~50 |
| Benign semis `[A]` | 76 | 73 / **79 (76–82)** / 84 | 69 / **82 (78–86)** / 88 | 67 / **82 (77–86)** / 89 | 68 / **78** / 85 | ~65 / 40 / 20 |
| High-spec jackups | 88 | 84 / **89 (87–91)** / 92 | 82 / **91 (88–93)** / 94 | 81 / **91 (88–94)** / 95 | 82 / **88** / 92 | ~70 / 45 / 25 |
| Middle East jackups (committed, Base only) `[E/A]` | ~90 | 90 | 91 | 92 | 90 | — |
| SE Asia jackups, tender-assist | `[?]` no series | — | — | — | — | — |

**Values, anchors, activity and signposts**

| Item | Value |
|---|---|
| Asset value at mid-cycle, Bear / Base / Bull $m | 12-yr-old 7G drillship **67 / 208 / 404** · 7-yr-old HE semi (NCS) **104 / 307 / 539** · 15-yr-old benign semi **10 / 10 / 132** · 12-yr-old high-spec jackup **10 / 42 / 107** · 15-yr-old tender barge **13 / 62 / 117** (tender mid-cycle 67 / 80 / 95, MCU 65 / 80 / 90 `[A, SED]`). Other ages: values-by-age table (Asset values and anchors) or the formula |
| Asset-value convention | Annual cash flow = 365 × [MCU × (rate × RE − opex) − (1 − MCU) × idle × opex] − tax × revenue − maintenance capex; value = annual cash flow × annuity(8%, 30 − age), floored at $10m. Rate and MCU = the scenario's mid-cycle, flat nominal; G&A, financing and working capital excluded |
| Convention parameters (opex $k/d · RE · idle share of opex · maint. capex $m/yr · tax % revenue) | Drillships 225 · 95% · 40% · 6 · 5% · HE semis (NCS) 250 · 96% · 40% · 6 · 5% · benign semis 225 · 95% · 40% · 5 · 5% · high-spec jackups 75 · 96% · 40% · 2.5 · 4.5% · tender barges / semi-tenders 35 / 40 · 98% · 40% · 3.0 / 3.5 · 6.4% |
| Cash floor · reactivation parity · newbuild parity, $k/d | Drillships 225 · 390 (320–470) `[A]` · ~540–570 on the convention (industry hurdle 650–720 `[E]`) · HE semis 250 · `[?]` · `[?]` · benign semis 225 · `[?]` · `[?]` · jackups 75 (55–90) · 125 (95–140) · `[?]` · tender barges 35 · `[?]` · `[?]` |
| Transaction marks (checkpoint 13) | Asset-implied rates sit 8–12% above Base mid-cycle: drillships ~394 (Deep Value Driller), jackups ~119–123. Used as a V_T sensitivity only |
| Leading edge, six months to 12 Nov (fixed rule) | Drillship 2027 starts **455 / 389–499 / n = 5**: NOC and Australia 389–406 (n = 2), US Gulf and SE Asia 455–499 (n = 3), grouped ~438 `[A]`. NCS HE ~430 / 399–517 / 8 as signed (2027 starts ~437, 2028 starts ~452). Jackups: 4 Nov set 126 / 91–167 / 8 plus 91.3 (A), ~107 (B), ~106 (B); median towards ~115 `[A]` |
| Regional reading, 2027 open days | Drillships: NOC, Brazil and India ~390–405; Australia ~400–410; US Gulf, IOC West Africa and SE Asia ~455–500; the global Base (420) only where the rig's market is not clear. Jackups: Mexico, West Africa, the Middle East and SE Asia ~95–100 (or their secondary row), not the 105 composite (80% benign regions at ~96–100 + 20% NW Europe/Australia at ~140 `[A]`) |
| NCS HE semis (odl) | Booked through 2027 (~96%), ~83% of 2028. Open 2028 rig-days: Spitsbergen (from Jan 2028), Atlantic (after two priced wells); Scarabeo 8 from 2029. Prints: Equinor package 402 (escalated; 399 as signed), Encourage bridge 441, GreatWhite ~432 (B), Barents 470 (450 as signed), Scarabeo 8 430, Bergen ~472 incl. mob (B; signed 10 Nov; options ~500 after FX and escalation `[E]`), Norge 517, Spitsbergen 519 (priced extension). Nordkapp 2028 and Atlantic's open 2028 days at Base 2028 (450) until set. Leading edge compared on rates as signed (checkpoint 19) |
| Fleet and activity (Westwood, Sep activity) | Drillships 80 / 86 contracted / marketed (93.0%), 9 cold-stacked, total 95. Semis 59 / 71 (reported 82%), 7 cold-stacked, total 78. Jackups 384 / 438 (87.7%), 51 cold-stacked, total 489. Working floaters 137, working jackups 374–376 (Westwood weekly to 9 Nov). Drillship backlog 152.2 rig-years (1 Oct; six falls in a row). Open floater tenders ~40 (75–80 rig-years) `[E]` |
| Rig activity for OSV demand (supply) | **NCS:** net HE semis 2027 vs 2026 +1 (Hercules to Canada from Q1 2027 −1; Endurance Q2 2027 and Barents Jun 2027 +2); Equinor 7 rig-years firm; jackups Interceptor (ConocoPhillips Ekofisk P&A, 670 days from Q3 2027) and Intrepid (ORLEN, Q3 2027). **UK:** +1 HE semi from Q3 2027, Beacon Pacific (Serica, six firm wells, options incl. P&A; likely moored `[A]`); P&A jackups Valaris 248 (41 wells from Apr 2027), Southern North Sea P&A (341 days), VALARIS 121 (Eni, from Nov 2026). **Brazil (1 Nov):** 47 operating / 35 drilling (25 drillships, 9 semis, 10 platform rigs, 3 jackups; Petrobras 34); outstanding minimum rig-days 2027 210, 2028 1,185, 2029 780; Transocean expects 30–33 rigs over five years `[E]`. **Guyana/Suriname:** DS-18 with Petronas in Suriname to May 2027, then US Gulf (−1 drillship in Suriname from mid-2027) |
| Scenarios (25/50/25 is a convention) | **Bear:** oil Bear (Brent 65 / 60 / 60) defers late-window FIDs (2028–29 drillship demand −8–10 rig-years); reactivations and stranded completions add supply; rates slide towards reactivation parity. **Base:** NOC-led floater demand converts gradually alongside IOC work; an H1-2027 MCU dip, then rates firm to 455–470 in 2028–29, capped by the stacked pool and stranded completions; jackups flat to firmer. **Bull:** 2H26 FIDs and NOC programmes lock long terms; drillship MCU 97% by 2028; > 500 for 2028 starts; reactivations answer only from 2028–29 |
| Recalibration triggers (12 Nov) | **Fired:** staleness; a stranded unit reactivated against a contract (Beacon Pacific, assessed: NCS paths kept); a Bull signpost crossed (drillship 2027 median, Bull 2027 set at 475). **Formally met, no point change:** NOC multi-year jackup awards (KOC, ONGC). **Not fired:** oil, MCU (3 pp), core term fixture (10%), floater orders, ownership change, war or force majeure |
| Signpost states (12 Nov) | Drillship MCU 93% (Bear < 88 / Bull > 94) · working floaters 137 (< 130 / > 140) · 2027-start drillship median 455 (Bull > 450 **crossed**) · 2028-start Base cut test < 440 (no new print) · drillship backlog 152.2 (Bear < 150, not crossed) · Venus FID not taken (towards Bear) · Gulf: no offshore rig suspension found; operational risk high · Keppel 7G drillship (2027) and N-class HE jackup (2028) completing without contract · no floater orders · no drillship reactivation |
| Next readings | Borr and SED Q3 ~18 Nov (checkpoints 22 and 17); Transocean–Valaris votes 24 Nov, closing ~1 Dec; Westwood October dashboard ~27 Nov (re-run early if drillship MCU is outside 90–96% or backlog < 150) |

## Metadata

- **Analysis date:** Thu 12 Nov 2026, Europe/Oslo. **Status: Final** (full update, Update mode, Steps 0–11). Skill `rig-market-bbb` revision **2026-10-10.1**. Compacted 13 Nov 2026; no value changed.
- **Caveats:** contract cover is a market proxy plus contractor cover (`[A]`); the latest Westwood monthly is September activity; Borr Q3 and SED Q3 (both ~18 Nov) are not out.
- **Previous baseline:** 10 Oct 2026 (33 days), with small updates to 4 Nov. **Window:** stub Q4-26 + 2027–2029; no roll (that is in January).
- **Why this run:** stale after 9 Nov (30-day rule); the 4 Nov small update fired the UDW drillship trigger and left the sample question to this run (checkpoint 18); Oil Market BBB re-baselined on 11 Nov.
- **Stale after 12 Dec 2026** (30 days). Re-run earlier if:
  - a recalibration trigger fires;
  - the Westwood October dashboard (~27 Nov) shows drillship MCU outside 90–96% or drillship backlog below 150 rig-years;
  - the Oil BBB update after OPEC+ (29 Nov) flags a rig-relevant change;
  - Borr or SED Q3 (~18 Nov) meets the rule in checkpoint 17 or 22.
- **Oil Market BBB used:** baseline **11 Nov 2026**, Final, stale after 30 Nov.
  - Brent Bear / Base / Bull: 2027 65 / **84** / 118; 2028 60 / 77 / 102; 2029 60 / 72 / 90; mid-cycle 60 / 70 / 82.
  - Long end (10 Nov settlements): Dec-27 77.6, Dec-28 72.8, Dec-29 70.6, Dec-30 69.1, Dec-31 67.7, Dec-34 64.2.
  - Its "For downstream skills" row for rig: "No (no action now)". This run's own check agrees (Drivers).
- **Series per segment:**
  - UDW drillships: Westwood drillship MCU (all drillships, proxy).
  - HE semis (NCS): contract cover of the named NCS fleet, with Westwood semi MCU as context.
  - Benign semis: Westwood semi MCU as an upper bound, benign set below it `[A]`.
  - High-spec jackups: Westwood jackup MCU.
  - Latest observation: September (October edition, 25/27 Oct): drillships 93%, semis 82%, jackups 88%.
  - Context series (not a replacement): RigLogix marketed utilization by class, as printed in Seadrill's 10-Q (as of 30 Sep 2026): benign floaters 87%, HE floaters 97%, HE jackups 95%. It is another source and definition, so it is shown beside the Westwood series and never mixed into it.
- **Leading-edge sample rule (fixed 12 Nov; checkpoint 18 closed):**
  - Six months to the run date, firm term ≥ ~1 year, start within ~18 months.
  - Pure dayrate. Where only a value incl. mobilisation is known, an ex-mob estimate is used and tagged `[A]`.
  - Rates as signed; for the NCS, not the escalated fleet-status value (checkpoint 19).
  - Median, range and n. Where the sample is bimodal (NOC vs IOC work), the two groups are shown as well.
- **Method:** one asset-value convention (since 8 Oct) for values, asset-implied rates and newbuild parity.
- **Westwood backlog dating:** start-of-month snapshots. Each edition restates the prior snapshot, so read changes within one edition only.
- **Oldest inputs:** Westwood leading-edge YTD via Riviera (15 Jun); Westwood monthly (Sep activity, published 25/27 Oct); Zacks RIG report (23 Oct, Aug data).
- **Not read `[?]`:** Petrodata weekly (dynamic tables); Westwood October dashboard (not out); Borr and SED Q3; per-rig dayrates for KOC/ADNOC Drilling and Beacon Pacific (not disclosed).
- **Tags:** `[F]` fact · `[E]` external forecast or secondary · `[A]` own assumption · `[?]` unknown. Fixture grades: A stated dayrate · B value ÷ days · C secondary estimate · D unknown.

## Conclusion

- **The 12 Nov run changed UDW drillships only (Bull 2027 and the stub); everything else is kept.** Drillship Bull 2027 is **475** (450–500). The drillship stub is **455**, the fixed six-month rule, mechanical and identical in all scenarios. Drillship Base 2027 stays at **420** (400–455). Two secondary ranges were widened with the points kept: SE Asia jackups Base 2027 **80–105**; Middle East jackups Base 2028 **85–110**.
- **Why drillship Base 2027 is $420k:**
  - The fixed sample gives **455 / 389–499 / n = 5**, but it is bimodal: NOC and Australia work at 389–406 (KG2, Skyros; n = 2) and US Gulf / SE Asia work at 455–499 (West Carina, Proteus, Conqueror; n = 3).
  - Weighting the two group medians by their count gives **~438 `[A]`, +4% vs 420**, below the 5% minimum change.
  - The balance points the other way for 2027: Base MCU 91% vs 93% today (an H1-2027 gap: Transocean UDW 22% uncommitted, Noble ~20% more contracted capacity in H2 2027 than in H1), backlog down six editions in a row (152.2 rig-years), and contracted drillships flat at 80.
  - Supply responds: six modern stacked drillships sit with one owner from ~1 Dec, and Keppel's RigCo is completing a 7G drillship on spec for 2027 delivery.
- **Why drillship Bull 2027 is $475k:** the Bull signpost "2027-start median > $450k" is crossed on the fixed rule (455). A Bull case at 95% MCU cannot sit below today's six-month leading edge, and the IOC prints are $465–499k.
- **Triggers assessed:** Beacon Pacific (CIMC-owned 6G HE semi; steel cut 2015, idle since build `[A]`) is reactivated for six firm Serica wells in the UK from Q3 2027. It adds one HE semi to NW Europe supply from mid-2027; NCS HE paths are kept (UK work, one unit, NCS 2028 ~83% covered) and it is a Bear-side supply signpost for NCS 2028–29. The NOC jackup awards are secondary rows or outside the high-spec class: KOC gave ADNOC Drilling two jackups for 4 years from Q4 2027 (~$107k, B), and ONGC gave ADES two standard jackups for 3 years (~$54k, B).
- **Oil input:** the $4 cut in Brent Base 2027 (to 84) is not material for rigs. 2027 is mostly set by backlog (~70% covered). FIDs run on the long end and mid-cycle: mid-cycle 70 is unchanged, Dec-29 is 70.6, and Dec-31 onwards is flat or higher. Contractors report fixtures underwritten at $30–40 breakevens `[E]`. The oil Bear catalyst (a deal) is closer, and that matters more for rigs in 2028–29 than the −$4 in 2027.
- **Base in two sentences:**
  - **Floaters:** drillships at ~$420k for 2027 open days, priced in two tiers (NOC ~$390–405k; US Gulf, IOC and SE Asia ~$455–500k). They firm to $455–470k for 2028–29 as tenders for 2028 starts convert, capped by the stacked pool and stranded completions. NCS HE is booked through 2027 and ~83% of 2028 at $430–517k.
  - **Jackups:** flat to firmer. Global MCU is 88% and the composite is ~$105k. New NOC term prints sit at ~$106–107k in the Middle East and Indonesia, and NW Europe and Australia fix at $115–167k.
- **Segment ranking (strongest → weakest):**
  1. NCS HE semis: booked through 2027, ~83% of 2028, $430–517k. Beacon Pacific (UK) is the first stranded HE unit to come out in this cycle `[A]`.
  2. UDW drillships: today's leading edge is $455k, but 2027 has an H1 gap and backlog is still falling.
  3. High-spec jackups: regional split; the Gulf is the swing factor (contract demand firm, operational risk high).
  4. Benign semis: utilization flat, few term fixtures, and old units stay in the fleet (Blackford Dolphin to SPM, Hakuryu-5).
- **Main Bear catalysts:**
  - Floaters: oil Bear (an Iran–USA deal plus OPEC+ market share, Brent 65 / 60 / 60) cuts exploration and late-window FIDs, with Venus slipping. Stranded completions (Keppel 7G 2027) and reactivations add supply. **Status: closer** (oil: strikes on hold since 9 Nov, talks; Venus not taken, the year-end target at risk).
  - Gulf jackups: suspension of rigs if the war re-escalates. **Status: not triggered.** No offshore rig suspension has been found since March–April, and KOC and KJO award 4-year terms.
- **Main Bull catalyst:** 2H26 budget FIDs and NOC programmes convert to term contracts, taking drillship MCU to ~97% by 2028 before reactivations respond. **Status:** the 2027-start median is above $450k on the fixed rule; Seadrill sees "signs that point towards a market recovery in 2027"; working floaters rose from 134 (Sep) to 137 (9 Nov).
- **Rig values:** mid-cycle and values are kept. Blackford Dolphin (1974 benign semi, $10m plus $15m contingent) is consistent with the benign-semi floor. Drillship and jackup transactions imply 8–12% above Base mid-cycle (checkpoint 13).
- **Low confidence (n < 3 term prints in six months):** benign semis, tender-assist, SE Asia and Middle East. SE Asia has two prints at $95–106k against a stub of 90 (checkpoint 22).

## Asset values and anchors

| Segment | Newbuild / completion $m | Secondhand $m (age, date) | Reactivation $m, lead time | Value mid-cycle Bear / Base / Bull $m | Cash floor $k/d | Reactivation parity $k/d | Newbuild parity $k/d |
|---|---|---|---|---|---|---|---|
| UDW drillships | 850–1,000+ `[E]`; stranded 7G completion: Keppel/Seatrium package $390m for 4 units (not split) `[F]` | 300 (Deep Value Driller, 2014 7G, Feb-26) `[F]` | 85–150, 12–18 mo `[E]` | **67 / 208 / 404** (12-yr-old 7G) | 225 `[E]` | 390 (320–470) `[A]` | **~540–570** (convention); 650–720 `[E]` |
| HE semis (NCS) | `[?]` | 480 (Deepsea Bollsta, 2019, Nov-25, incl. $355m backlog) `[F]` | `[?]` (Beacon Pacific reactivation cost not disclosed) | **104 / 307 / 539** (7-yr-old) | 250 `[A]` | `[?]` | `[?]` |
| Benign semis | `[?]` | 10 + 15 contingent (Blackford Dolphin, 1974, to SPM, Oct-26) `[F]`; recycling 4–8 `[E]` | `[?]` | **10 / 10 / 132** (15-yr-old; Bear and Base at the floor) | 225 `[E]` | `[?]` | `[?]` |
| High-spec jackups | `[?]` | 72 each (5 Noble units to Borr, Jan-26); 57 each (5 Fontis units, Jul-26); 64 (Noble Resolve, closed Oct-26) `[F]` | 20–40, 6–12 mo `[E, older]` | **10 / 42 / 107** (12-yr-old; Bear at the floor) | 75 (55–90) `[A]` | 125 (95–140) `[A]` | `[?]` (newbuild price `[?]`) |
| Tender barges (secondary) | 113–135 (EDrill/T-series build cost) `[F, SED]` | ~28 each (Seadrill → Energy Drilling, 3 units incl. a semi-tender, Jun-23) `[F]` | `[?]` | **13 / 62 / 117** (15-yr-old; mid-cycle 67 / 80 / 95, MCU 65 / 80 / 90 `[A, SED]`) | 35 `[F, SED]` | `[?]` | `[?]` |

**Asset-value convention (one method for values, asset-implied rates and newbuild parity):**

```
Annual cash flow = 365 × [ MCU × (rate × RE − opex) − (1 − MCU) × idle × opex ] − tax × revenue − maintenance capex
Value            = annual cash flow × annuity(8%, 30 − age), floored at $10m
```

Rate and MCU are the scenario's mid-cycle, flat nominal. G&A, financing and working capital are excluded; they belong in the company analysis.

| Segment | Opex $k/d | RE | Idle cost (share of opex) | Maint. capex $m/yr | Tax % revenue | Floor $m | Sources |
|---|---|---|---|---|---|---|---|
| UDW drillships | 225 | 95% | 40% | 6 | 5% | 10 | Opex = cash floor `[E]`; capex ≈ Transocean 2026 capex $150m ÷ 27 floaters = $5.6m `[F/B]`; RE, tax `[A]` |
| HE semis (NCS) | 250 | 96% | 40% | 6 | 5% | 10 | Opex `[A]`; capex as drillships `[B]` |
| Benign semis | 225 | 95% | 40% | 5 | 5% | 10 | Opex `[E]`; capex `[A]` |
| High-spec jackups | 75 | 96% | 40% | 2.5 | 4.5% | 10 | Opex = cash floor `[A]` (Borr Odin "mid-$70k" `[F]`); RE = Borr economic utilisation 96.4% `[F]`; capex Borr guidance $2–2.5m a rig `[F]`; tax Borr H1 cash tax 4.5% of revenue `[F]`; idle = Borr warm-stacked ~$30k ÷ $75k `[A]` |
| Tender barges / semi-tenders | 35 / 40 | 98% | 40% | 3.0 / 3.5 | 6.4% | 10 | SED opex and tax `[F]`; capex `[A, SED]` |

- **Life 30 years, discount 8% nominal.** Accounting lives for jackups are ~30 years when non-operating (Transocean `[F]`); the industry rule of thumb is ~25 years `[E]`; some units work into their late 30s (and Blackford Dolphin, 52, and Hakuryu-5, 49, are still marketed). 35 years is a sensitivity only.
- **Reactivation parity:** opex + reactivation cost repaid over a 2-year firm term at 8%, 95% revenue efficiency. It is a cash test on the reactivation spend, not a rig value.
- **Newbuild parity** = the rate at which a newbuild is worth its price on the convention (age 0, 92% MCU). Drillships at $900m–1bn give **~$540–570k**; the industry hurdle (12–15%, 5-year contract) gives $650–720k `[E]`. No order can deliver inside the window (≥ 3–5 years lead time). Stranded completions (Keppel 7G, 2027) are the supply that answers before newbuilds.

**Values by age ($m; Bear / Base / Bull mid-cycle; values at or below the $10m floor shown as 10):**

| Segment | 5 yr | 10 yr | 12 yr | 15 yr | 20 yr |
|---|---|---|---|---|---|
| UDW drillships (320 / 360 / 420; MCU 82 / 88 / 92) | 77 / 236 / 460 | 71 / 217 / 423 | 67 / 208 / 404 | 61 / 190 / 369 | 48 / 149 / 289 |
| HE semis (350 / 400 / 460; MCU 85 / 92 / 96) | — / 316 / — | — / 291 / — | — | — / 254 / — | — |
| High-spec jackups (92 / 110 / 130; MCU 82 / 88 / 92) | 10 / 48 / 122 | 10 / 44 / 113 | 10 / 42 / 107 | 10 / 38 / 98 | 10 / 30 / 77 |

18-year-old jackup: 10 / 34 / 86; 22-year-old: 10 / 26 / 66. Values for other ages, or with a sourced company spec or opex, are recomputed with the same formula.

**Sensitivities (Base, typical age):**

| Segment | Base value | Opex −10% / +10% | 35-year life | Annual cash flow (≈ $k per calendar day) |
|---|---|---|---|---|
| UDW drillships (12 yr) | 208 | 279 / 136 | 230 | $22.1m (61) |
| HE semis (7 yr) | 307 | 397 / 217 | 327 | $29.6m (81) |
| Benign semis (15 yr) | 10 | 68 / 10 | 10 | $0.8m (2) |
| High-spec jackups (12 yr) | 42 | 66 / 18 | 47 | $4.5m (12) |
| Tender barges (15 yr) | 62 | 71 / 52 | 71 | $7.2m (20) |

- Margins are thin, so values are very sensitive to opex: ±$7.5k a day moves a 12-year-old jackup from $18m to $66m. Company analyses must source their own opex before departing from the segment parameters.

**Transaction market check (asset-implied rate on the convention vs Base mid-cycle):**

| Transaction | Age, MCU used | Asset-implied rate $k/d | Base mid-cycle | Gap | Note |
|---|---|---|---|---|---|
| Deep Value Driller, $300m (Feb-26) | 12, 88% | **~394** (35-yr life ~383) | 360 | **+9%** | Competitive sale (Saipem outbid) |
| Noble → Borr, 5 jackups at $72m (Jan-26) | 12–18, 88% | **~123** (35-yr ~120) | 110 | **+12%** | Seller exiting jackups |
| Fontis → Borr/CME JV, 5 jackups at $57m (Jul-26) | 12–19, 88% | **~119** (35-yr ~115) | 110 | **+8%** | Seller exiting |
| Noble Resolve → Ocean Oilfield, $64m (agreed Dec-25, closed Oct-26) | ~17 (build year `[?]`), 88% | **~122** (age 16–18: 121–124) | 110 | +11% | HE CJ50: compare with NW Europe fixtures ($115–167k), not the composite. Now has a Tunisia contract (Tende Energy, Abiod well; terms `[?]`) |
| Deepsea Bollsta, $480m incl. $355m backlog (Nov-25) | 6, 92% | ~452 (overstated: backlog premium not split out) | 400 | +13% (upper bound) | — |
| Seadrill → Energy Drilling, 2 barges + 1 semi-tender, $85m (Jun-23) | 10–14, 80% | ~58 (barge; semi at 1.5x) | 80 | −27% | Distressed 2023 sale |
| Noble Globetrotter II, $38m (closing Q4-26; buyer `[?]`) | ~13 (2013 `[A]`), 88%, drillship parameters | ~298 | 360 | −17% | Not comparable: not Tier-1; impaired seller |
| Blackford Dolphin → SPM, $10m + $15m contingent (agreed 26 Oct, closing ~5 Nov) | 52 (beyond the 30-year life) | n/a (floor) | 300 (benign) | — | Consistent with the floor: $10m paid on delivery, $15m only on a first contract payment (India). The rig stays in the fleet |

- **Reading:** on the fully costed convention, 2025–26 buyers of drillships and jackups paid for through-life rates **8–12% above Base mid-cycle**, between Base and Bull. Old benign semis trade at the floor.
- **Mid-cycle rates are kept.** The evidence is three competitive or exit sales plus one closing. The gap is carried as **open checkpoint 13** for the mid-cycle review with the long-run leading-edge series (checkpoint 10). Until then, IAF analyses show V_T at transaction-implied marks as a sensitivity.

## Scenario definitions

| Scenario | Weight (convention) | Oil BBB scenario used | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|
| **Bear** | 25% | Bear (Brent 65 / 60 / 60); Gulf jackups also stressed under oil Bull's war escalation (operational line) | **Demand:** oil Bear (Iran–USA deal plus OPEC+ market share) and FID deferrals (Búzios, Namibia Venus, US Gulf independents); programmes cut to minimum. **Supply:** Transocean–Valaris reactivates cold-stacked drillships against short work; stranded units complete without contracts (Keppel 7G drillship 2027, N-class HE jackup 2028; Beacon Pacific competes in NW Europe after Serica); Gulf jackups idled by war move to Asia | Late-window FIDs fail, so 2028–29 drillship demand falls 8–10 rig-years. Rates slide to near reactivation parity, then towards the cash floor for benign semis. Jackup oversupply spreads from SE Asia | Q1 2027 (FIDs); any time (Gulf) | Drillship MCU < 88% · 2027-start term fixtures < $380k · drillship backlog < 150 rig-years (Westwood, start-of-month) · Venus FID slips to 2027+ · ≥ 2 cold-stacked drillship reactivations without long contracts · a stranded floater delivered without a contract · Gulf rigs suspended again |
| **Base** | 50% | Base (armed normalisation, Brent 84 / 77 / 72; mid-cycle 70) | NOC-led floater demand converts gradually (Petrobras, ONGC, Equinor, Vår, Petronas/PTTEP) alongside IOC work in the US Gulf, West Africa and SE Asia; Gulf jackups keep working; no newbuild orders | Drillship rates ~$420k for 2027 open days in two tiers: NOC ~$390–405k; US Gulf, IOC and SE Asia ~$455–500k (six-month leading edge $455k). Floater MCU dips in H1 2027, then rises to near the friction ceiling in 2028 as tenders for 2028 starts convert. Rates firm to $455–470k, capped by the consolidated stacked pool and stranded completions. Jackups flat to firmer, with regional divergence | Ongoing | Drillship MCU 90–94% in Q1 2027 (Sep: 93%) · 2027-start term fixtures $400–455k (fixed-rule median 455) · 2028-start fixtures ≥ $440k · drillship backlog stops falling · Aramco recalls suspended rigs |
| **Bull** | 25% | Base or Bull (Brent 84–118 in 2027; cash-flow lag 12–36 months) | **Demand:** 2H26 budget FIDs (Venus, Brazil, West Africa, Asia gas) plus NOC energy-security programmes lock long terms. **Supply:** no reactivations before 2028, no orders, stranded completions absorbed by contracts | Drillship MCU 97% by 2028; 2027-start terms ~$475k; rates break $500k for 2028 starts; reactivation economics answer only from 2028–29 (12–18 months lead time). Jackups: Aramco and KJO/KOC-type awards absorb the Gulf rigs | Q1 2027 | Drillship MCU > 94% · term fixtures > $450k for 2027 starts (**crossed**, fixed rule 455) · > $500k for 2028 starts · Petrobras Búzios awards · Venus FID taken · Aramco calls back 6–9 suspended rigs · working floaters > 140 |

## Paths per segment — MCU % / rate $k/day, point (range)

| Scenario | Segment | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|
| Bear | UDW drillships | 88 (86–90) / 380 (360–395) | 86 (83–89) / 375 (350–395) | 83 (79–87) / 360 (330–390) | 86 / 372 | 82 / 320 |
| **Base** | **UDW drillships** | **91 (89–93) / 420 (400–455)** | **95 (92–97) / 455 (425–480)** | **94 (90–97) / 470 (430–500)** | **93 / 448** | **88 / 360** |
| Bull | UDW drillships | 95 (93–96) / **475 (450–500)** | 97 (95–98) / 500 (470–530) | 97 (95–98) / 540 (500–570) | 96 / 505 | 92 / 420 |
| Bear | HE semis (NCS) | 92 (90–94) / 410 (395–425) | 88 (84–91) / 400 (375–420) | 83 (78–87) / 380 (350–405) | 88 / 397 | 85 / 350 |
| **Base** | **HE semis (NCS)** | **97 (95–98) / 425 (410–440)** | **96 (93–98) / 450 (425–475)** | **93 (89–96) / 470 (440–500)** | **95 / 448** | **92 / 400** |
| Bull | HE semis (NCS) | 98 (97–99) / 445 (430–460) | 98 (97–99) / 500 (475–525) | 97 (95–99) / 540 (500–570) | 98 / 495 | 96 / 460 |
| Bear | Benign semis | 73 (70–76) / 310 (290–330) | 69 (65–73) / 290 (265–315) | 67 (62–72) / 280 (250–310) | 70 / 293 | 68 / 260 |
| **Base** | **Benign semis** | **79 (76–82) / 340 (315–365)** | **82 (78–86) / 355 (325–385)** | **82 (77–86) / 365 (330–400)** | **81 / 353** | **78 / 300** |
| Bull | Benign semis | 84 (81–87) / 370 (350–390) | 88 (85–91) / 405 (380–430) | 89 (86–92) / 430 (400–460) | 87 / 402 | 85 / 340 |
| Bear | High-spec jackups | 84 (82–86) / 92 (85–98) | 82 (79–85) / 88 (80–95) | 81 (77–84) / 85 (75–92) | 82 / 88 | 82 / 92 |
| **Base** | **High-spec jackups** | **89 (87–91) / 105 (98–112)** | **91 (88–93) / 115 (105–125)** | **91 (88–94) / 120 (108–132)** | **90 / 113** | **88 / 110** |
| Bull | High-spec jackups | 92 (90–94) / 118 (110–125) | 94 (92–96) / 135 (125–145) | 95 (93–97) / 145 (130–155) | 94 / 133 | 92 / 130 |

**Secondary rows (rate $k/day, point (range); low confidence):**

| Row | Scenario | 2027 | 2028 | 2029 | Basis |
|---|---|---|---|---|---|
| SE Asia jackups | Bear / **Base** / Bull | 72 (60–80) / **90 (80–105)** / 98 | 70 / **95 (85–105)** / 108 | 70 / **98 (88–108)** / 115 | Six-month term prints: NAGA 8 $95k (A, Chevron Malaysia, 547 days) and Perseverance ~$106k incl. mob/demob (B, PHM Indonesia, 406 + 30 days, end-Dec 2026). Older: PV Drilling VI $97k (A), NAGA 2 ~$86k for 5 years (B). PTTEP–Foresight $60–70k (C, unconfirmed). n = 2 in six months, so the point is kept and the range widened (checkpoint 22). Bear = Gulf rigs relocate and Foresight-type pricing spreads |
| Tender-assist barges | Bear / **Base** / Bull | 68 (60–75) / **78 (70–88)** / 88 | 65 / **82 (72–92)** / 95 | 65 / **85 (75–95)** / 100 | SED contracts ($83k EDrill-2 for 5 years; older $94–121k); SED opex ~$37k a rig-day. T-16 Phase 7 (CPOC, 30 months from Q3 2027) ≈ $95k incl. mob (B), ~$89–92k ex-mob `[A]`; one print, not applied. Westwood (5 Nov): fleet utilization ~96% → 100%; four TARs above $120k, types not stated `[E]`. Semi-tenders ($127–160k, SED) are not covered. Jackups compete directly (PTTEP). Checkpoint 17 |
| Middle East jackups | **Base** | **90 (80–100)** | **95 (85–110)** | **100 (88–110)** | KJO: Arabian Drilling 4 rigs × 4 years ≈ $91k (B, Sep-26); Embracer $91.3k (A, 1,460 days from Mar 2027). KOC: ADNOC Drilling 2 rigs × 4 years from Q4 2027, $313.6m maximum value incl. mobilisation ≈ $107k (B, upper bound). Aramco 3-year extensions for five ARO rigs (D). The Bear catalyst (war re-escalation) is in the scenario table; Bear/Bull figures are added when a company analysis needs them |

- **Contract cover per segment and year `[A]`.** Rig-by-rig cover is built for the main contractors in the appendix. The market proxy is Westwood backlog ÷ marketed rigs (1 Oct snapshot).
  - **Drillships:** 152.2 rig-years over 86 marketed = 1.77 years per rig, i.e. cover ~70% / 45% / 25% for 2027 / 2028 / 2029.
    - Transocean's active drillships are ~92% / 52% / 24% committed. Its UDW fleet incl. 3 stacked units is uncommitted 22% / 56% / 80% (10-Q, 2 Nov `[F]`).
    - Valaris: 3,152 contracted drillship days in 2027 ≈ 8.6 of 10 active rigs. Seadrill: > 85% of 2027 drillship days contracted. Noble: floaters 66% contracted in Q3.
  - **NCS HE semis:** ~96% / ~83% / ~50%. Transocean's NCS fleet is ~96 / 80 / 64% committed `[A]` (HE uncommitted 8 / 31 / 47% `[F]`). The market proxy for 2029 (50%) stays below Transocean's own NCS fleet.
  - **Semis aggregate:** 1.13 years per rig. **Benign semis:** ~65% / 40% / 20%.
  - **Jackups:** 1.57 years per rig, ~70% / 45% / 25%.
  - The Bear–Bull spread is narrowest in 2027 and widest in 2029 for every segment; the NCS spread is narrowest of all in 2027. The drillship 2027 spread (380–475) is still the narrowest drillship year.
- **Base vs management guidance `[E]`:**
  - Transocean ("> 90% in 2027, approaching 100% by year-end"), Noble ("essentially fully contracted by late next year"; "inflection in fleet utilization … starting H2 2027") and Seadrill ("signs that point towards a market recovery in 2027") all sit above Base 2027 MCU (91%). Bull (95%) reflects the guidance case.
  - Base is lower because contracted drillships have been flat at 80 since July, backlog has fallen six editions in a row, and guidance assumes tenders convert.
  - On rates, Noble's Tier-1 leading edge ("mid-$400,000s to $500,000") matches the IOC tier and the six-month median (455). Base 2027 (420) also carries the NOC tier and the H1 gap.

## Market check

| Segment | MCU latest (month) | Leading-edge median / range / n (6 mo, term; fixed rule) | Trend 6–12 mo | Cover 2027 / 28 / 29 `[A]` | Base 2027 vs leading-edge |
|---|---|---|---|---|---|
| UDW drillships | **93% (Sep; 80 / 86)**; 90% Jun–Aug, 94% Mar–May. RigLogix benign floaters 87% (30 Sep) | **2027 starts: 455 / 389–499 / 5** (KG2 389, Skyros 406, West Carina ~455 ex-mob, Proteus 465, Conqueror 499). Groups: NOC and Australia 389–406 (n = 2); US Gulf and SE Asia 455–499 (n = 3); grouped reading ~438 `[A]`. 2028 starts: Noble Viking 460 (296 days, short of the term rule), West Polaris 438 (older). Noble Tier-1 range "mid-400s to 500" `[F, company]`. Short: Globetrotter I 400, DS-12 ~417, BlackHawk ~500. Westwood 2026 YTD (Jun): 6G/7G 388, 7G 407, 6G 371 | MCU up 3 pp on supply (−2 units; contracted flat at 80); backlog −12% since the 1 Apr snapshot (173.3, April edition) to 152.2; working floaters 134 (Sep) → 137 (2 and 9 Nov); rates up for IOC / US Gulf work, NOC flat at ~$390k | ~70 / 45 / 25 (Transocean active ~92 / 52 / 24; Seadrill 2027 > 85%) | **420 vs 455 (−8%); vs grouped ~438 (−4%)** |
| HE semis (NCS) | `[?]` (Westwood semi aggregate 82%, Sep). RigLogix HE floaters 97% (30 Sep) | ~430 / 399–517 / 8 as signed (Hercules excluded: it works in Canada). 2027 starts ~437: Endurance 402, GreatWhite ~432, Encourage 441, Barents 450; 2028 starts ~452: Scarabeo 8 430, Bergen ~472 incl. mob, Norge 517. Bergen signed 10 Nov (terms as the LOA); options ~$500k after FX and escalation (CEO, Q3 call `[E]`). Westwood Norway 2026 YTD 436 | Rates rising (+$50k y/y); fleet-status rates drift up with escalation and the NOK component (checkpoint 19) | ~96 / 83 / 50 | 425 vs ~437 for 2027 starts (−3%) |
| Benign semis | ~76% `[A]` (aggregate 82% incl. HE, Sep; counts 59 / 71 = 83%, flagged) | ~350 / 320–400 / term n < 3, low confidence. Westwood all-semi 2026 YTD < 340 (implies benign ~$300k if Norway is ~30% of fixtures `[A]`). Short: SSV Catarina 279 (Indonesia, 70 days). Hakuryu-5 ≤ ~280–300 all-in (C, 1977 unit, conditional) | MCU flat; backlog down; short work dominates; old units stay in the fleet (Blackford Dolphin to SPM, India) | ~65 / 40 / 20 | 340 vs ~300–350 |
| High-spec jackups | **88% (Sep; 384 / 438)**; 87% Jul–Aug, 86% Mar–Jun. RigLogix HE jackups 95% (30 Sep). Working 374–376 (Oct–9 Nov, Westwood weekly) | 4 Nov set: 126 / 91–167 / 8 (skewed to NW Europe/Australia). Added since: Embracer 91.3 (A, KJO), KOC ~107 (B), Perseverance ~106 (B); these pull the median towards ~115 `[A]`. Short: VALARIS 122 UK 125, VALARIS Norway ~135, 107 165, 106 ~111; Tenacious (Angola, priced 1-year option) ~142 (B). Westwood 2026 YTD excl. Norway/Australia (Jun): 94 | Firming slightly; contracted +2 in Sep; backlog −28 rig-years a month; Middle East and Africa working jackups down in October (Westwood commentary) | ~70 / 45 / 25 | 105 vs ~91–107 (benign regions) and ~115–167 (NW Europe/Australia) |

- **Stub and MCU notes:** the drillship stub (455) is above Base 2027 (420) because the six-month sample is led by US Gulf and SE Asia work (3 of 5 prints), while Base 2027 is the composite for all 2027 open days, including NOC work (~$390–405k) and an H1-2027 gap. MCU stubs are the latest observed month (Westwood, September): drillships 80 / 86 = 93.0%; jackups 384 / 438 = 87.7%; semis 82% in aggregate, with HE and benign set at 97 and 76 `[A]`. RigLogix cross-check (Seadrill 10-Q, 30 Sep): HE floaters 97% (23 contracted), benign floaters 87% (107 contracted; drillships and semis together), HE jackups 95% (27). Tender-assist (Westwood, 5 Nov): fleet utilization ~96%, heading for 100% by end-Q4 2026, excluding the cold-stacked T-9 and the newbuild Raiqa `[E]`; context for checkpoint 17, not a series.
- **Jackup composite `[A]`:** Base $105k ≈ 80% benign regions at ~$96–100k + 20% NW Europe/Australia at ~$140k. Rigs in Mexico, West Africa, the Middle East and SE Asia should read ~$95–100k for 2027 (or their secondary row), not $105k. The composite is kept for global MCU and fleet-wide reads.
- **Westwood leading-edge** (via Riviera, 15 Jun 2026, YTD to mid-June; aggregate of RigLogix fixtures, treated as `[F]` for the database and `[E]` for the commentary): drillships 6G $371k, 7G $407k, 6G/7G $388k (−7% vs 2025); semis < $340k (−6%), Norway $436k (+$50k); jackups ~$94k excl. Norway/Australia (−6% vs 2025, −24% vs 2024's $123k). Westwood 2023 averages: jackups $118k, semis $368k, drillships $419k.
- **Regional reading for IAF (drillships, 2027 open days):** NOC, Brazil and India ~$390–405k; Australia ~$400–410k; US Gulf, IOC West Africa and SE Asia ~$455–500k. Use the global Base ($420k) only where the rig's market is not clear.

**Anchors:**
- **UDW drillships:**
  - Base 2027 ($420k) is above the central reactivation parity ($390k; range 320–470), and the six-month leading edge ($455k) is near the top of that range.
  - The reactivation ceiling works with a lag: a reactivation takes 12–18 months and $100–150m (Transocean via Zacks `[E]`), and owners want long terms (the 2023 trigger was DS-7 at $428k for 850 days `[E]`).
  - **Stacked pool:** six modern drillships in Transocean–Valaris (Ocean Rig Apollo 2015, Athena 2014 and Mylos 2013; VALARIS DS-11 2013, DS-13 2023 and DS-14 2023), in one owner's hands from ~1 Dec. The other three of Westwood's nine cold-stacked drillships have other owners `[?]`. No reactivation is announced.
  - **Stranded completion:** Keppel's RigCo will complete a 7G drillship at Seatrium for 2027 delivery without a contract. It is the first speculative floater completion of this cycle `[A]`: an owner betting on rates at or above completion parity.
  - Newbuild parity (~$540–570k on the convention, $650–720k at the industry hurdle) cannot deliver inside the window.
  - Asset-implied rate: Deep Value Driller ($300m) capitalises **~$394k** at 8% and 88% MCU, 9% above Base mid-cycle ($360k) and inside the 2027–29 Base paths ($420–470k).
- **HE semis:** Deepsea Bollsta ($480m with backlog) implies ≤ ~$452k at 92% MCU with $250k opex `[A]`, an upper bound because the backlog premium is not split out. Beacon Pacific (stranded CIMC unit, UK from Q3 2027) is the first stranded HE semi to come out against a contract in this cycle `[A]`; its rate and reactivation cost are undisclosed.
- **High-spec jackups:** the $57–72m transactions imply ~$119–123k on the convention, above Base mid-cycle ($110k) and just below reactivation parity (~$125k). The 51 cold-stacked jackups are mostly older and standard, so the competitive pool is smaller than the headline. Keppel's N-class HE jackup (2028) adds one premium unit for NW Europe or the Middle East `[A]`.

## Drivers

### Oil input and translation

| Oil input (Oil Market BBB, 11 Nov) | Rig effect |
|---|---|
| Brent Base **84** / 77 / 72, mid-cycle 70; long end Dec-27 77.6, Dec-28 72.8, Dec-29 70.6, Dec-30 69.1, Dec-31 67.7, Dec-34 64.2 | 2027 is ~70% covered, so the −$4 in Base 2027 reaches rig demand mainly through 2027 exploration budgets, set in this budget season. That is small against $30–40 project breakevens `[E]` and NOC programmes that are not price-led. FIDs run on the long end and mid-cycle: Dec-29 ≈ mid-cycle 70, and Dec-31 onwards is flat or higher. **No rig change** (own check; it agrees with the oil baseline's "no action") |
| Bear 65 / 60 / 60 (durable Iran–USA deal plus OPEC+ market share; new enabler: Russia–Ukraine sanctions relief). Status: **closer** (strikes on hold since 9 Nov; talks) | Exploration and marginal deepwater FIDs (US Gulf independents, Namibia) are deferred with a 6–18 month lag, so the hit lands in 2028–29. This is the main oil risk for the floater paths |
| Bull 118 / 102 / 90 (renewed strikes with retaliation against Gulf energy infrastructure). Status: further away, tail live | Cash flow lifts floater demand with a 12–36 month lag. Operationally, Gulf jackups face suspension and evacuation again — **two separate lines** |
| Strategic restocking (~1 bn bbl), energy security | Supports NOC programmes (Aramco, ADNOC, KOC, KJO, Petronas, PTTEP gas, Equinor) |

**Operational geopolitics (status 12 Nov):**
- **Middle East jackups:**
  - **Precedent:** working utilization fell from 83% to ~69% (Feb → late Apr) while committed held ~90% `[E, Westwood May]`. The Arabian Gulf is ~36% of global jackup supply `[E]`. The war suspensions of March 2026 were reversed by mid-August (ADES 11 Aug, Arabian Drilling 12 Aug, VALARIS 110 and 250, Borr) `[F]`. A drone hit a KOC offshore drilling platform on 12 Jul `[F]`.
  - **Since the late-October escalation:** attacks are onshore and coastal, plus on ships (Dammam airport and Shaybah 21 Oct, the evacuation of Aramco's Dhahran HQ 22 Oct, a claimed Ras Tanura hit 27 Oct (unconfirmed), Houthi missiles damaging the Aramco Tower in Riyadh 8 Nov per Oil BBB; ships hit on 10 Nov). The IRGC declared Hormuz closed (~26 Oct).
  - **Not found `[?]` (searches 4 and 12 Nov):** any suspension, evacuation, down-manning or force majeure for a Gulf offshore rig, or a contractor notice. Valaris (2 Nov, primary): "All Valaris and ARO rigs operating in the Middle East remain under contract." Westwood says Middle East working jackups fell in October, without a count.
  - **Contract demand firm:** Aramco gave five ARO rigs 3-year extensions, KJO awarded 4-year terms, and KOC gave ADNOC Drilling 2 × 4 years.
  - **Reading:** the oil-price line has no rig effect. The operational line is high risk but has lost no rig-days so far. If rigs are suspended, committed MCU (the Middle East row basis) holds, as in March–April, while working utilization and contractor revenue fall at once.
- **Red Sea / Egypt / East Med:** Valaris DS-12 works for BP in Egypt to Apr 2027 (+60 days late 2027); Transocean Asgard is in the East Med to Dec 2027. Flag on escalation. Floaters outside the region are not affected operationally.

### Operator demand

- **Brazil (Westwood, 1 Nov):**
  - 47 rigs operating and 35 drilling, both flat vs 1 Oct: 25 drillships, 9 semis, 10 platform rigs and 3 jackups. Petrobras has 34.
  - Outstanding minimum requirements: 2027 **210** rig-days, 2028 **1,185** and 2029 780. That is small against the fleet; the 2028 rise is ~0.4 rig-years.
  - Petrobras concluded a $3.6bn cycle in March–April (Búzios, Mero, Renecon), with 6G long terms at $360–430k. Corcovado and Orion run to 2030 at $392k, and Aquila to Jun 2028 at $442k. Further Búzios drillship awards are pending `[?]`.
  - IOC work: Valaris DS-8 moves to Shell Brazil from Mar 2027 (~800 days), and DS-17 works for Equinor Brazil to Jan 2028.
  - Petrobras is ~20% of global deepwater demand, a concentration risk. Transocean expects Brazil to sustain 30–33 rigs over five years `[E]`.
- **India:** ONGC took KG2 Feb 2027–Feb 2029 at $389k (binding LOA), and Reliance has KG1 to Mar 2028 at $410k. ONGC also gave ADES two standard jackups (Key Singapore, Admarine 10) for 3 years from ~Q1 2027 at $117.2m incl. mobilisation ≈ **$54k** (B), outside the high-spec class.
- **NCS:**
  - Equinor's 7 rig-years are firm: Endurance returns from Australia in Q2 2027; Enabler and Encourage run from 2028 at $402k (escalated), with Encourage bridging at $441k from May 2027.
  - Transocean Barents (from Romania) works for Vår Jun 2027–Jun 2030 at $470k ($450k as signed).
  - Hercules (SFL, Odfjell-managed) leaves Norway for Canada for ≥ 400 days from Q1 2027; it is not NCS demand in 2027.
  - Deepsea Bergen: Vår contract signed on 10 Nov (LOA 10 Sep): 3 years from early 2028 plus four 1-year priced options to 2035; ~$472k incl. mobilisation (B). The CEO puts option economics near $500k after FX and escalation `[E]`.
  - Transocean Norge: Harbour Jan–Oct 2028 at $517k, priced options to Mar 2029, then Shell Mar–Jul 2029.
  - Spitsbergen is firm with Equinor to Dec 2027 ($519k from Apr 2027), then open. Deepsea Atlantic is firm to late Q4 2027, with two more priced wells and three ~1-year periods at rates to be agreed. Deepsea Nordkapp is firm to end-2028 (rate set at market by end-2026). Deepsea Aberdeen works for Equinor to Q1 2029. Noble GreatWhite works for Aker BP from Q2 2027 for 3 years (~$432k, B), and Scarabeo 8 for Aker BP from Jan 2028 (366 days, $430k).
  - **NCS HE availability:** booked through 2027 (~96%) and ~83% of 2028. Open rig-days in 2028: Spitsbergen (from Jan 2028) and Atlantic (after two priced wells), plus Scarabeo 8 from 2029. Transocean expects Norway HE utilization near 100% from 2028 `[E]`, and Odfjell calls most marketable Tier-1 HE rigs fully booked for 2027 `[E]`.
  - Jackups: Noble Interceptor drills a DNO well in Q3 2027, then 670 days of ConocoPhillips Ekofisk P&A. Noble Intrepid moves from BP UK ($150k to Sep 2027) to ORLEN (1 well, Q3 2027).
- **UK:**
  - **Beacon Pacific** (CIMC-owned 6G HE semi, managed by Odfjell): Serica, six firm wells from Q3 2027 (Bruce infill first, then possibly Kyla and Greater Laggan west of Shetland, and P&A), with options. Reactivation and transit from Asia have begun. The rate is not disclosed (D). Likely moored like its sister Deepsea Yantai `[A]`, so it needs AHTS for rig moves.
  - P&A demand is firm: Valaris 248 (41-well P&A from Apr 2027, ~$130k), the Southern North Sea P&A fleet award (341 days, ~$122k, window to 2030), and VALARIS 121 for Eni from Nov 2026.
  - VALARIS Norway works for Ithaca from Q2 2027 (~200 days, ~$135k), VALARIS 122 for INEOS in the UK from Jul 2027 ($125k), and Claus Bachmann for BP UK from Mar 2027. Intrepid leaves the UK for Norway in Q3 2027.
- **West Africa:**
  - Venus (TotalEnergies): **FID not taken**. Fiscal terms were still being negotiated (Bloomberg, 15 Oct); "must come before 2027". It would need 2–3 rigs for development drilling `[E]`. Mopane FID is targeted for 2028.
  - Contracts: Conqueror in Equatorial Guinea Jan–Jul 2027; DS-7 in Angola to Sep 2027; Sonangol Libongos to Jan 2030; BlackRhino (TotalEnergies Nigeria) from Q4 2026; Faye Kozack (Tullow Ghana) from mid-2027.
  - Globetrotter I takes a 3-year TotalEnergies light-well-intervention capacity reservation (≥ 150 days a year).
  - Jackups: Borr Norve (245 days) and Natt (to Aug 2027). Shelf Tenacious (Angola) has a priced 1-year option exercised, ~$52m ≈ $142k (B). BW Energy may need a jackup to replace Prospector 5 (lost 24 Oct) `[?]`.
- **US Gulf:** Proteus (Feb 2027–Jan 2029, $465k) and Conqueror (Aug 2027–Nov 2028, $499k) are new term work. Also DS-16 and DS-18 (Occidental), West Neptune and West Vela (LLOG) and Sevan Louisiana (LLOG). Operator confidence "set to push rig demand modestly higher in US Gulf, mostly in shallow water" (Drilling Contractor, 27 Oct `[E]`). Transocean expects some US Gulf high-spec drillships to move to West Africa, the Mediterranean, SE Asia and India.
- **Suriname / other South America:** DS-18 works for Petronas in Suriname Nov 2026–May 2027, then 914 days for Occidental in the US Gulf. Noble BlackHawk drills 1 well for Apache in Uruguay in Q4 2027, and Globetrotter I 2 wells for Occidental in Peru from Q2 2027 ($400k).
- **Asia Pacific:**
  - Floaters: West Carina (Indonesia, H1 2027, 880 days), West Capella (PTTEP to Feb 2028), Noble Viking (Brunei, 2028, $460k), Skyros (Chevron Australia, Mar 2027, $406k), Equinox (Santos, Apr 2027, $395k). Hakuryu-5 (Finder KTJ, Timor-Leste, Dec 2027) is conditional on FID by 30 Nov.
  - Jackups: Perseverance (PHM, Indonesia, ~$106k incl. mob, B), NAGA 8 (Chevron, $95k), NAGA 2 (PCSB, 5 years), NAGA 3 (Petronas, 1 well + 1 option, Nov 2026; D), PTTEP 5 + 3 years (Foresight, 2027, $60–70k C).
  - Tender-assist (Westwood, 5 Nov `[E]`): 29 TARs (16 active, 6 warm and 6 cold-stacked, 1 under construction). PTTEP has 8 TARs + 2 semi-tenders, Petronas Carigali 3. Malaysian semi-tender campaigns start from Mar 2027 (Shell Malikai Phase 3, PTTEP Kikeh Phase 3, ConocoPhillips Kebabangan), and Vietnam's Bien Dong from Q1 2028. PTTEP increasingly chooses between TARs and jackups by programme.
- **Middle East:**
  - KJO: Arabian Drilling 4 jackups × 4 years (SAR 2bn ≈ $91k) and Embracer for 4 years from Mar 2027 ($91.3k).
  - KOC: ADNOC Drilling, two jackups for 4 years firm (incl. mobilisation) plus 1 option year, from Q4 2027, $313.6m maximum (KWD 96.6m) ≈ $107k (B, upper bound). One rig is ADNOC Drilling's own and one bareboat-chartered (source `[?]`). It is ADNOC Drilling's first offshore work outside the UAE, under an LOA subject to formalities.
  - Aramco: 3-year extensions for five ARO rigs (Oct 2026). The recall of the 2024 demand-driven suspensions is `[?]`.
- **Mediterranean:** Ocean MVM (ex-Noble Resolve, CJ50 HE jackup) for Tende Energy's Abiod well off Hammamet, Tunisia (terms `[?]`).
- **Pipeline `[E]`:**
  - ~100 floater rig-years were awarded in H1 2026, and there are ~40 open tenders (75–80 rig-years) (Transocean management, via Zacks).
  - Africa could rise to 20–25 floaters within 18 months. Countries drilling at least one exploration well: 35 (2025) → 51 (2028).
  - Westwood: 2026 EPC $84.5bn vs ~$46bn in 2025, with 30 FIDs (~$46bn EPC) still to come. Wood Mackenzie: rig demand +8.5% in 2027.
- **Backlog trend `[F]`** (Westwood, start-of-month snapshots; differences within one edition):

| Edition (activity month) | Jackups Δ | Semis Δ | Drillships Δ | Drillship level after |
|---|---|---|---|---|
| Feb | −28.4 | −2.4 | −3.9 | 149.5 |
| Mar | −29.1 | +7.5 | +12.1 | 169.0 |
| Apr | −23.1 | −3.6 | −5.6 | 167.7 |
| May | −20.3 | +1.0 | −6.0 | 161.5 |
| Jun | −24.8 | −4.2 | −1.7 | 160.5 |
| Jul | −14.2 | −4.0 | −2.2 | 158.0 |
| Aug | −28.9 | −4.4 | −5.3 | 155.7 |
| Sep (Oct edition, 25/27 Oct) | −28.4 | −4.2 | −5.4 | 152.2 |

  - Drillship backlog has fallen **six editions in a row** (Apr–Sep), −12% from the 1 Apr snapshot (173.3 as restated in the April edition) to 152.2. Jackup backlog has fallen in every edition this year, and semis in the last four.
  - Westwood restates earlier snapshots upwards as late awards are booked (the 1 Sep snapshot was restated to jackups 725.8, semis 90.4, drillships 157.6). The semi restatement probably carries Equinor's 7 rig-years `[A]`.
  - Awards are not yet replacing burn. This is the main falsification signal against Base 2027–28. The next reading is the October edition (~27 Nov), which should include Proteus and Conqueror (~3.2 rig-years).

### Supply

- **Drillships** (Westwood, Sep): marketed 86 (80 contracted + 6 available), cold-stacked 9, total 95 (two units left the fleet in September, names `[?]`).
  - No newbuild orders.
  - **Stranded completion:** Keppel RigCo will fund Seatrium to complete a 7G drillship for 2027 delivery "positioned for charters", with no contract `[F]`. It is a funded plan, so it is probable supply from 2027–28. It becomes competitive supply once contracted.
  - The stacked pool in Transocean–Valaris is six modern units, in one owner's hands from ~1 Dec. Reactivation costs $85–150m and takes 12–18 months, and none has been announced.
  - Ownership: Deep Value Driller passed to Eldorado ($300m), and Noble's Globetrotter II sale ($38m) is pending. Neither creates a rig.
  - Net effective change 2026 → 2029: Base 0 to +1 (Keppel); Bull +1–3 from 2028 (reactivations, Keppel); Bear −1–2 (older 6G retirements), with the Keppel unit uncontracted.
- **Semis** (Westwood, Sep): marketed 71 (59 + 12), cold-stacked 7, total 78 (−2 in September).
  - Retirements: Valaris DPS-1 and MS-1, Noble Ocean Apex.
  - **Beacon Pacific:** a CIMC-owned 6G HE semi, steel cut at Yantai in 2015 and idle since build `[A]`, enters the NW Europe HE fleet from Q3 2027 against the Serica contract. That is +1 competitive HE semi in the UK. Whether it can later take NCS work (consent) is `[?]` (checkpoint 20).
  - Keppel's two mid-water HE semis for NW Europe: completion is "under assessment", so they are not supply yet (checkpoint 21).
  - Old units stay: Blackford Dolphin (1974) was sold to SPM for marketing in India, and Hakuryu-5 (1977) has a conditional Timor contract. That slows benign retirements.
  - Relocations: Hercules (Norway → Canada, Q1 2027 start), Endurance (Australia → NCS, Q2 2027), Barents (Romania → NCS, Jun 2027), Deepsea Mira (→ Trinidad, Apr 2027). No global change. Net NCS HE semi count 2027 vs 2026: −1 + 2 = +1.
  - Net effective change by 2029: benign −1 to −3 (Base); NW Europe HE +1.
  - Counts: the reported 82% does not reconcile with 59 / 71 = 83.1%; the gap is flagged, not corrected.
- **Jackups** (Westwood, Sep): marketed 438 (384 + 54), cold-stacked 51, total 489.
  - Ownership: Borr bought 5 from Noble (Jan) and 5 Fontis units in a 50/50 JV (Jul). Noble Resolve went to Ocean Oilfield (now Ocean MVM, Tunisia work). VALARIS 111 was sold for MOPU conversion and leaves the fleet. Valaris has three benign units stacked (148, 147, 143) plus VALARIS Viking (HE). Seven units are leased to ARO.
  - Loss: Borr's Prospector 5 (2014 JU-2000E) sank off Gabon on 24 Oct: −1 high-spec unit, ~0.2 pp of MCU.
  - **Stranded completion:** Keppel's N-class HE jackup (500-ft class) for 2028 delivery, no contract.
  - Working jackups 374–376 through October and to 9 Nov (Westwood weekly).
  - Newbuild deliveries from Chinese and Middle East yards (ARO) are `[?]`. Net effective change: slightly positive `[A]`.
- **Ownership (Step 0):**
  - Transocean–Valaris has all regulatory approvals (incl. DOJ and CADE, without conditions). Shareholder votes are on **24 Nov**, Bermuda court approval on **26 Nov**, and closing on or about **1 Dec 2026**. Until then the fleets are counted separately; the merger creates no rigs.
  - ADES owns Shelf (since Nov 2025). Eldorado–Vantage closed in June 2026. Odfjell owns Deepsea Bergen (ex-Bollsta) and manages Beacon Pacific (owned by a CIMC affiliate). Keppel RigCo owns the stranded Seatrium units. Blackford Dolphin moves from Dolphin to SPM (Dolphin manages it).

### Region × segment matrix (material cells)

| Region × type | MCU / status | Leading-edge / recent fixtures | Trend | Oil sensitivity | Confidence |
|---|---|---|---|---|---|
| Global drillships | 93% MCU / 84% total (Sep; 80 / 86, 80 / 95); working floaters 137 (9 Nov) | Six-month 2027-start term 455 / 389–499 / 5; Westwood 7G $407k / 6G $371k (YTD Jun) | Rates up for IOC work; backlog still falling (152.2) | Low–medium | High (data) |
| Brazil drillships | 47 operating, 35 drilling (1 Nov, flat); 25 drillships, 9 semis | ODN I ~$322k (B); Corcovado and Orion $392k to 2030 (A); Aquila $442k to Jun 2028 (A); DS-4 ~$420k (B); West Polaris $438k (from 2028) | Long terms at modest rates; IOC work (Shell, Equinor) at higher rates | Low (NOC) | Medium |
| India floaters | — | KG2 $389k (A); KG1 Reliance $410k | New NOC term | Low | Medium |
| US Gulf drillships | `[?]` | Proteus $465k (A); Conqueror $499k (A); West Vela ~$440k (C) | New term work at a premium; some rigs expected to leave | Medium | Medium |
| West Africa floaters | `[?]` | DS-7 $385k (A); Conqueror EG $465k (A, short); DS-15 CNR ~$135m for 250 days incl. upgrades (B) | Active; Venus FID pending | Medium–high | Low–medium |
| NCS HE semis | Booked 2027 (~96%), ~83% 2028; RigLogix HE floaters 97% | $402–519k; 2028 starts ~$452k; Bergen ~$472k (signed 10 Nov); Westwood Norway YTD $436k | Up | Low | Medium (thin) |
| UK / NW Europe | Beacon Pacific joins from Q3 2027 (Serica, 6 wells) | Beacon Pacific (D); Claus Bachmann ~$320k (C); jackups: Valaris 122 $115–125k (A), VALARIS Norway ~$135k (B), 248 P&A ~$130k (B), SNS P&A ~$122k (B), Intrepid $150k (A); RigLogix HE jackups 95% | First stranded HE semi to work `[A]`; P&A demand | Medium | Low |
| NCS jackups | P&A and exploration from Q3 2027 (Interceptor, Intrepid) | `[?]` (rates undisclosed) | Firm | Low | Low |
| Caribbean (Trinidad) semis | — | Developer $375k (A); Deepsea Mira ~$467k value/day, 150 days incl. mob (B) | Short work | Medium | Low |
| Australia | — | Skyros $406k (A); Equinox $395k (A, short); Valaris 107 $163–167k | Stable; Endurance leaves Q2 2027 | Medium | Medium |
| Suriname / other South America floaters | — | DS-18 Petronas (D); Globetrotter I Peru $400k (A, short); BlackHawk Uruguay ~$500k (B, short) | Exploration | Medium | Low |
| Middle East jackups | Committed ~90%; no suspension found to 12 Nov; ME working jackups down in Oct (Westwood) | KJO ~$91k (B, Arabian ×4) and $91.3k (A, Embracer); KOC ~$107k (B, 2 × 4 years from Q4 2027); Aramco 5 × 3-year extensions (D) | Contract demand firm; operational risk high | Low price / very high geopolitical | Medium |
| SE Asia floaters | Rising (Seadrill: "increasing activity in Southeast Asia") | West Carina ~$477k incl. mob (B); West Capella options ~$442k (B); Noble Viking $460k (2028) | Up | Low–medium (NOC) | Medium |
| Timor Sea benign semis | Hakuryu-5 for Finder KTJ from Dec 2027 (conditional on FID 30 Nov) | ≤ ~$280–300k all-in (C, upper bound) | Small-operator work | Medium | Low |
| SE Asia jackups | `[?]` | Perseverance ~$106k incl. mob (B); NAGA 8 $95k (A); NAGA 2 ~$86k (B); Foresight $60–70k (C) | Mixed: PHM/Chevron firm, PTTEP aggressive | Low–medium (NOC gas) | Low–medium |
| SE Asia tender-assist | Westwood ~96% fleet utilization → 100% by end-Q4 (5 Nov `[E]`); SED 2027 firm cover 52% | T-16 Phase 7 ~$95k incl. mob (B); Phase 6 $131k; EDrill-2 $83k; "four TARs > $120k" (types `[?]`) | Utilization tight; barge renewals re-price in the $80–95k zone | Low (NOC/JDA) | Low (n = 1) |
| West Africa jackups | Borr Norve, Natt; Prospector 5 lost | Tenacious ~$142k (B, priced option); ADES Main Pass IV $132k (A) | Firm | Medium | Low |
| Mexico jackups | Rigs back to work (Aug); Perfomex divested (Borr keeps bareboat economics) | Borr fleet ~$134k average (mixed) | Improving; Pemex payments | Medium | Medium |

Not assessed: East Africa, Canada, Caspian.

### Balance check

- **Drillships:**
  - With 86 marketed, Base 2027 at 91% means ~78 contracted, two fewer than today's 80. That is an H1-2027 gap, consistent with the falling backlog and Noble's H1/H2 profile, before tenders for 2028 starts convert.
  - Base 2028–29 (95% / 94%) needs ~82–83 contracted out of 86–87 (87 if the Keppel unit is marketed), i.e. +2–3 rigs from the 75–80 rig-years in open tenders. That is consistent with rates firming to $455–470k, above reactivation parity, with the supply response capping them.
  - The rate stays at $420k in 2027 while today's leading edge is $455k. That is consistent with an MCU dip to 91% and a mix with more NOC and gap-filler work in the open 2027 days.
  - Bear (MCU down to 83%, rate down to $360k) is consistent with the backlog continuing to fall and the Keppel unit coming without work. Bull at 97% needs ~85 contracted plus reactivations from 2028, which caps 2029 at $540k.
- **HE NCS:** supply is fixed (consent-gated) and demand is booked. A rate rise with a stable balance is consistent. Beacon Pacific adds supply in the UK, not the NCS. It loosens the NW Europe balance for 2028–29 at the margin, a Bear-side point that is not applied (one unit, NCS 2028 ~83% covered).
- **Benign semis:** utilization falls while rates are held flat. The few term fixtures are high-spec units in benign regions ($375–400k), while older units compete for short work. Base MCU recovers +6 pp by 2028 on retirements and spill-over from fully booked drillships. That is plausible but unproven: September semi MCU was flat at 82% with the fleet −2, and old units now stay marketed (Blackford Dolphin, Hakuryu-5).
- **Jackups:** Base MCU +2–4 pp by 2028 needs ~10–15 more contracted rigs (Gulf recalls, Mexico, KJO, KOC from Q4 2027). The marketed pool grew by 9 in August, so supply absorbs part of the recovery, and the rate path stays modest ($105k → $120k).
- **Fleet reconciliation:**
  - The Westwood class totals are global, and no regional fleet split is available, so Σ regions = global cannot be shown `[?]`. No rig is counted twice: Keppel's units are not in the marketed fleet until delivered and marketed, and Beacon Pacific counts from its contract start.
  - September counts: MCU drillships 80 / 86 = 93.0% (reported 93); semis 59 / 71 = 83.1% (reported 82, a 1 pp gap, flagged); jackups 384 / 438 = 87.7% (88). Totals: 80 / 95 = 84.2% (84); 59 / 78 = 75.6% (75); 384 / 489 = 78.5% (78).

## Signposts and monitoring

| Signpost | Threshold (Bear / Bull) | Now (12 Nov) | Previous (4 Nov) | Direction |
|---|---|---|---|---|
| Drillship MCU (Westwood) | < 88% / > 94% | 93% (Sep; 80 / 86, from −2 marketed); October edition ~27 Nov | 93% (Sep) | Towards Bull (supply-driven) |
| Working floaters (Westwood weekly) | < 130 / > 140 | **137** (2 and 9 Nov); 136 (26 Oct) | 135 (19 Oct) | Towards Bull |
| 2027-start drillship term fixtures (fixed rule) | < $380k / > $450k (median) | **455 / 389–499 / 5; Bull threshold crossed** (no new print since 4 Nov) | ~$420k (13 Oct sample) / 455–465 (strict) | Towards Bull |
| 2028-start drillship term fixtures | < $400k / > $500k; Base cut test < $440k | No new print; Noble Viking $460k (short), West Polaris $438k (older); 2027-start terms running through 2028 at $465–499k | Same | Neutral, firm |
| Westwood drillship backlog (rig-years) | < 150 / two rises in a row | 152.2 (1 Oct); 6 falls in a row; next ~27 Nov | Same | Towards Bear (not crossed) |
| NCS HE availability | Open rig-days in 2028 / fully booked 2029 | 2027 ~96%; 2028 ~83% (Bergen signed 10 Nov); open in 2028: Spitsbergen, Atlantic beyond two priced wells | Same | Towards Bull |
| NW Europe HE supply | A stranded HE unit gets NCS work, or a second one is completed / — | Beacon Pacific to the UK (Serica, Q3 2027); Keppel's two mid-water HE semis "under assessment" | — | Towards Bear (supply), not crossed |
| Petrobras | Further deferrals / Búzios awards | No new awards; Brazil count flat (47 / 35); 2028 outstanding rig-days 1,185 | No awards | Neutral |
| West Africa FIDs | Venus FID slips to 2027+ / Venus FID taken | Not taken; fiscal talks open (15 Oct); deadline "before 2027" | Not taken | Towards Bear (deadline near) |
| Saudi / Gulf jackups | Renewed suspensions / Aramco recalls 6–9 rigs | No suspension found (12 Nov). Contract demand firm: Aramco 5 × 3-year extensions, KJO 4-year terms, KOC 2 × 4 years (Q4 2027). Onshore attacks continue (Aramco Tower, 8 Nov) | No suspension; Aramco, KJO | **Mixed:** contracts towards Bull; operational risk towards Bear |
| APAC jackup / tender pricing | Confirmed term fixtures < $80k / > $100k | Perseverance ~$106k incl. mob (B); NAGA 8 $95k; Foresight $60–70k (C, unconfirmed); T-16 barge ~$95k (B); Westwood: four TARs > $120k, fleet ~96% (5 Nov) | Foresight; $86–97k; T-16 | Towards Bull for Indonesia and tender-assist; PTTEP jackups still towards Bear |
| Reactivations | ≥ 2 cold-stacked drillships reactivated without long contracts / none | None for drillships. HE semi: Beacon Pacific reactivated **against a contract** (trigger, assessed) | None | Neutral (drillships) |
| Stranded completions | A stranded floater delivered without a contract / delivered against a term contract | Keppel 7G drillship (2027) and N-class HE jackup (2028) being completed with no contract | — | Towards Bear (supply), not crossed |
| Retirements | — / ≥ 2 floaters retired a quarter | Q3: drillship fleet 97 → 95, semis 80 → 78 (MS-1, Sagar Vijay, others `[?]`). Q4 so far: none found; Blackford Dolphin stays marketed (SPM) | Crossed (Q3) | Q3 crossed; Q4 open |
| Newbuild orders | Any floater order / none | None | None | Towards Bull (supply) |

**Open checkpoints:**

1. **PTTEP/Foresight actual rates:** still unconfirmed; three secondary sources say $60–70k (C). Reflected in the SE Asia and tender-assist Bear.
2. **Gulf operations:** re-assess the Middle East row (Bear) on any of: a suspension, evacuation or force majeure notice for a Gulf offshore rig (Aramco, QatarEnergy, ADNOC, KOC/KJO); an attack on an offshore installation or support base; a Westwood weekly with working jackups down ≥ 5 and the Middle East cited (March precedent: −13 in a month). Status 12 Nov: none met. Next reads: Westwood weeklies, Borr Q3 (~18 Nov), ADES and Arabian Drilling releases.
3. **Transocean–Valaris closing:** shareholder votes 24 Nov, court 26 Nov, closing ~1 Dec. Close on the completion 8-K, then count the combined stacked pool as one owner's.
4. **2H26 FIDs and budgets:** Venus FID not taken (deadline "before 2027"); Mopane FID 2028; Westwood's 30 FIDs outstanding; Finder KTJ FID by 30 Nov (Hakuryu-5).
5b. **Westwood October dashboard (~27 Nov):** test drillship MCU (Base 2027 91%; today 93%) and backlog (Bear signpost < 150; Proteus and Conqueror should add ~3.2 rig-years). Re-run early if MCU is outside 90–96% or backlog is < 150.
8. **Noble Faye Kozack (Ghana) rate:** low priority (D).
10. **Long-run leading-edge series per segment** (2010–2026, with and without the 2014 peak and the 2016–2021 trough). Partial: Westwood averages for 2023 (jackups $118k, semis $368k, drillships $419k), 2024 (jackups $123k), 2025 (implied: drillships ~$417k, jackups ~$100k) and 2026 YTD.
11. **Jackup and HE semi newbuild prices, HE semi reactivation cost, NCS opex:** all `[?]`. Partial: Keppel's remaining completion cost for four stranded units is ~$390m in total (not split). Beacon Pacific's reactivation cost is not disclosed. Cross-check: Transocean 2026 O&M $2.33–2.40bn ÷ 27 rigs ≈ $236–244k a rig-day `[B]`.
12. **+9 marketed jackups in August:** low priority. The September fleet was flat at 438.
13. **Mid-cycle vs transaction-implied rates:** drillships ~$394k and jackups ~$119–123k, 8–12% above Base mid-cycle; Westwood's 2023–26 drillship averages ($388–419k) sit at or above Base mid-cycle ($360k) without trough years. Odfjell's price implies ~$413k through-life on its own economics (+3% vs HE Base mid-cycle). Globetrotter II (~$298k) is not comparable. Blackford Dolphin is at the floor (benign). Review with checkpoint 10.
14. **Benign-semi rate path:** Westwood's all-semi 2026 YTD implies benign ~$300k `[A]` vs Base 2027 $340k. Low prints so far are old or short units (Hakuryu-5, SSV Catarina), and old units now stay in the fleet (Blackford Dolphin). No term benign fixture in the Q3 reports. Cut Base 2027 to ~$310–320k if a term benign fixture for a high-spec unit prints ≤ $320k.
15. **Jackup composite weighting** (80/20 benign vs NW Europe/Australia `[A]`): RigLogix HE jackup MCU 95% (Seadrill 10-Q) supports the NW Europe premium.
17. **Tender-assist row vs T-16:**
    - **Rule:** if a second SE Asia tender-barge term fixture for a 2027–28 start prints ≥ ~$86k at grade A/B, raise Base 2027–28 by at least 5% and widen the 2027 range (top 88). If instead the next EDrill-1 / T-15 awards come in at ≤ $80k, T-16 stands as a client-specific outlier.
    - Evidence (Westwood, 5 Nov `[E]`): fleet utilization ~96%, heading for 100% by end-Q4; four TARs "securing" > $120k, types not stated. Semi-tenders are not covered by the row, so this is not a barge fixture.
    - Next read: SED Q3 (18 Nov).
19. **NOK and escalation drift in NCS fleet-status rates:** compare leading-edge on rates as signed; IAF uses current USD values for booked days. Odfjell's CEO puts Bergen's option economics near $500k after FX and escalation.
20. **Beacon Pacific:** rate, reactivation cost and NCS consent `[?]`. Watch the Serica term length (six wells ≈ 1 year `[A]`) and the options, and whether the rig bids for NCS work in 2028–29 (Bear supply for NCS HE). Sources: Odfjell or CIMC disclosures, and Westwood.
21. **Keppel stranded completions:** the 7G drillship (2027) and N-class HE jackup (2028): contract or charter status; the two mid-water HE semis: completion decision. A 7G drillship delivered without work is a Bear supply signpost; one delivered against a term contract at ≥ $450k is Bull pricing evidence.
22. **SE Asia jackup point and Borr Q3 (~18 Nov):** two six-month term prints at $95–106k vs Base 2027 $90k. **Rule:** if a third grade A/B term print ≥ $95k appears (Borr Q3, Velesto, ADES), raise SE Asia Base 2027–28 by ≥ 5%. Also read Borr's contract cover and average dayrates, and its Gulf, Mexico and West Africa statements, for the jackup row.
23. **KOC per-rig rate:** $313.6m is a maximum value incl. mobilisation for two rigs. Read the per-rig dayrate when ADNOC Drilling or the Kuwaiti gazette publishes it, and test the Middle East 2028 Base (95).

## For IAF

- **12 Nov run:** only UDW drillships Bull 2027 and the drillship stub moved. No IAF analysis uses the drillship row today. Every row read by an existing analysis (HE NCS, jackups, SE Asia, Middle East, tender-assist) keeps its points, MCU, mid-cycle and asset values. **No re-run is needed for rig reasons.** Values: Interface; V_T, NAV_0 and market marks use the asset-value convention (values-by-age table or the same formula), with transaction-implied marks (+8–12% on rate) as a sensitivity (checkpoint 13).
- **Odfjell (`docs/odl-analysis.md`): HE semis (NCS) row.** The Bergen signing (10 Nov) confirms backlog already counted (~$472k incl. mob from 2028, +5% vs Base 2028). Norge ($517k) and Barents ($470k) remain the comparables. Nordkapp 2028 and Atlantic's open 2028 days stay at Base 2028 ($450k) until set; the Nordkapp rate is set by two brokers by end-2026. Beacon Pacific earns Odfjell management fees only: a company item, not a market row.
- **Borr (`docs/borr-analysis.md`, on hold):** jackup, SE Asia and Middle East rows, by rig location. Rigs in Mexico, West Africa, the Middle East and SE Asia read ~$95–100k for 2027, not the $105k composite. New regional prints (KOC ~$107k, Perseverance ~$106k) are mildly positive for Borr's Gulf and Asia re-lets. The fleet's ~$134k average still marks negative on rolling contracts. No Gulf suspension. Borr Q3 (~18 Nov) is checkpoint 22.
- **SED (`docs/SED-analysis.md`): tender-assist row.** Westwood's 5 Nov reading (utilization ~96% → 100%, four TARs above $120k) is Bull-side evidence, but it is not a barge fixture. SED Q3 (18 Nov) applies checkpoint 17.
- **Transocean, Valaris, Noble, Seadrill (no IAF analysis):** UDW drillships row at the regional reading (Interface). Keppel's speculative 7G completion and the six-unit stacked pool cap the Bull case from 2028.

## For downstream skills

`affects` = none at the 12 Nov run: no Base or Bear path, MCU, mid-cycle or asset value moved; the stub is a mechanical re-mark (+8.3%) and Bull 2027 moved +5.6%, both below the 10% trigger; ranges are not points. Each reader takes the notes below at its own next run; values are in the Interface.

| Reader | What it reads here | What to take in at its next run |
|---|---|---|
| **supply** | Rig activity for OSV demand: NCS, UK, Brazil, Guyana/Suriname | Interface row "Rig activity for OSV demand". New: Beacon Pacific (UK, from Q3 2027), confirmed from the Odfjell and Serica releases; Hercules works in Canada (≥ 400 days from Q1 2027, announced Mar 2026), not on the NCS. Drillship rate changes do not change OSV demand |
| **hy** | Oil Service row: drillship Base and Bear, NCS HE | Base drillships 420 / 455 / 470 at 91 / 95 / 94%; NCS HE 425 / 450 / 470; Bear drillships 380 / 375 / 360 at 88 / 86 / 83%. Bull 2027 475 is not read there. Text note: HY's Oil Service paragraph quotes the drillship Bear as "400 → 360k"; the Bear 2027 point is 380 |
| **odl** | HE semis (NCS) row: rates, MCU, mid-cycle, asset convention, fixtures | Row unchanged. Bergen signed 10 Nov (terms as LOA; options ~$500k per the CEO `[E]`). Beacon Pacific is a managed rig (fees), UK. RigLogix HE floater MCU 97% |
| **sed** | Tender-assist row, rig values | Row unchanged. Westwood (5 Nov): TAR utilization ~96% → 100%, four TARs > $120k (types `[?]`). Checkpoint 17 rule at SED Q3 (18 Nov) |
| **borr** (on hold) | Jackup rates, MCU, rig values; SE Asia and Middle East rows | Points unchanged; SE Asia 2027 and Middle East 2028 ranges widened. Prints: KOC ~$107k (B, 2 × 4 years from Q4 2027), Perseverance ~$106k (B, Indonesia), Tenacious ~$142k (B, Angola option). Keppel N-class HE jackup (2028, spec). Checkpoint 22 at Borr Q3 |

## Change log

- **13 Nov 2026 — compacted to the lean-document rules (1,143 → 634 lines, Interface section first); no value changed.**
- **12 Nov 2026 — full update (re-baseline; skill 2026-10-10.1):** fixed six-month leading-edge sample rule (checkpoint 18 closed); drillship Bull 2027 450 → 475 (450–500) and stub 420 → 455; Base 2027 kept at 420 (range 400–445 → 400–455); SE Asia Base 2027 range → 80–105, Middle East Base 2028 range → 85–110 (points kept). Beacon Pacific and Keppel stranded completions logged as supply; Hercules corrected to Canada; oil (Base 2027 88 → 84) not material. `affects` = none. Stale after 12 Dec 2026.
- **4 Nov 2026 — small update (Q3 fleet status reports):** UDW drillships Base 2027 400 → 420, Bull 2027 430 → 450, stub 400 → 420, stub MCU 90 → 93 (Proteus $465k and Conqueror $499k, Noble Tier-1 range); jackup stub MCU 87 → 88. KG2 corrected to $389k, Corcovado to $392k, Norge to $517k. Everything else kept.

## Appendix

### Fixture log (fixtures behind the current leading edge and secondary rows)

| Rig | Class | Region | Operator | Start | Term | Rate $k/day | Grade | Source |
|---|---|---|---|---|---|---|---|---|
| Deepwater Proteus | 7G DS (2016) | US Gulf | undisclosed | Feb 2027 | 10 wells, to Jan 2029 (~23 months) | **465** | A | Transocean fleet status 2 Nov |
| Deepwater Conqueror | 7G DS (2016) | US Gulf | undisclosed | Aug 2027 | 5 wells, to Nov 2028 (~15 months) | **499** | A | Transocean fleet status 2 Nov |
| Deepwater Conqueror | 7G DS | Equatorial Guinea | Chevron (Westwood) | Jan 2027 | 2 wells, to Jul 2027 | 465 (Westwood $470,588) | A, short | Transocean fleet status 2 Nov; Westwood October edition |
| Seadrill West Carina | 7G DS (2015) | Indonesia | undisclosed | H1 2027 | 880 days + 880 days priced options | ~477 ($420m incl. mob, excl. services); ~450–460 ex-mob `[A]` | B | Splash247 13 Oct (Seadrill release) |
| Dhirubhai Deepwater KG2 | DS (2010) | India | ONGC | Feb 2027 | to Feb 2029 + priced options to Feb 2031 | **389** | A | Transocean fleet status 2 Nov (binding LOA) |
| Deepwater Skyros | DS | Australia | Chevron | Mar 2027 | 320 days | 406 | A | Westwood |
| Noble Viking | 7G DS | Brunei | Petronas Carigali | Jan 2028 | 296 days | 460 | A | Westwood; Noble Jul |
| Seadrill West Polaris | UDW DS | Brazil | Petrobras | Feb 2028 | 1,095 days | 438 | A | Westwood; DC |
| Deepwater Corcovado / Orion | DS (2011) | Brazil | Petrobras | Jan 2027 | to Nov 2030 / Mar 2030 | 392 / 392 | A | Transocean fleet status 2 Nov (awarded H1 2026) |
| Deepwater Aquila | 8G DS (2024) | Brazil | Petrobras | Jan 2027 | to Jun 2028 | 442 | A | Transocean fleet status 2 Nov (older award) |
| Valaris DS-4 | DS | Brazil | Petrobras | Nov 2027 | 1,064 days | ~420 ($447m) | B | World Oil 6 Apr |
| Foresea ODN I | UDW DS | Brazil | Petrobras | early 2027 | 1,443 days | ~322 ($465m) | B | World Oil 25 Mar |
| Valaris DS-7 | 7G DS | Angola | Azule | Oct 2026 | 325 days | 385 | A | Westwood |
| Noble Globetrotter I | DS (2011, non-Tier-1) | Peru | Occidental | Q2 2027 | 2 wells; then TotalEnergies West Africa 3-year light-well-intervention capacity reservation (≥ 150 days a year) | 400 (+ mob fee) | A, short | Noble Q3 release 26 Oct |
| Noble BlackHawk | 7G DS | Uruguay | Apache | Q4 2027 | 1 well, ~50 days | ~500 (~$25m excl. mob/demob) | B, short | Noble Q3 release 26 Oct |
| Noble (range statement) | Tier-1 DS | various | various | 2027 | ~44 months of new floater backlog since Q2 | "mid-400s to 500" | A (company range, n `[?]`) | Noble Q3 release 26 Oct |
| VALARIS DS-12 (extension) | DS (2013) | Egypt | BP | late 2027 / early 2028 | 60 days (priced) | ~417 (~$25m) | B, short | Valaris fleet status 2 Nov |
| Seadrill West Capella (priced options) | 6G DS (2008) | Malaysia | PTTEP | 2027 | 120 days | ~342 ($41m) | B, short | Splash247 13 Oct |
| Seadrill West Capella (unpriced options) | 6G DS (2008) | Malaysia | PTTEP | to Feb 2028 | 120 days | ~442 ($53m; set at market) | B, short | Splash247 13 Oct |
| Deepsea Bergen (contract signed) | HE semi (2019, CS60E) | NCS | Vår Energi | early 2028 | 3 years + four 1-year priced options to 2035 | ~472 ($518m incl. mob ÷ ~1,095 days; LOA terms); options ~500 after FX and escalation (CEO `[E]`) | B | Odfjell release 10 Nov (Newsweb 06:06 UTC); OE Digital 10 Sep |
| Transocean Norge | 6G HE semi | NCS | Harbour Energy | Jan 2028 | to Oct 2028 (5 wells) + priced options to Mar 2029 | **517** | A | Transocean fleet status 2 Nov |
| Transocean Norge | 6G HE semi | NCS | A/S Norske Shell | Mar 2029 | to Jul 2029 + priced option to Aug 2029 | 517 | A, short | Transocean fleet status 2 Nov |
| Transocean Spitsbergen | HE semi (2010) | NCS | Equinor | Apr 2027 | to Dec 2027 (priced extension) | 519 | A, short | Transocean fleet status 2 Nov |
| Transocean Enabler / Encourage / Endurance | HE semis (Cat D) | NCS | Equinor | Apr 2028 / May 2028 / Jun 2027 | 3 / 2 / 2 years (7 rig-years, $1.0bn) | 402 (escalated; 399 as signed) | A | Transocean fleet status 2 Nov; 8-K 9 Oct |
| Transocean Encourage (bridge) | HE semi | NCS | Equinor | May 2027 | to May 2028 | 441 | A | Transocean fleet status 2 Nov |
| Transocean Barents | HE semi (2009) | NCS (from Romania) | Vår Energi | Jun 2027 (after 145 days of mobilisation and preparation) | to Jun 2030 + priced options to Jun 2034 | **470** (FSR, escalated; ~450 at signing, ~$490m ÷ 1,095 days) | A | Transocean fleet status 2 Nov; Transocean release 8–9 Apr 2026 (via OGJ, OE Digital) |
| Scarabeo 8 | HE semi | NCS | Aker BP | Jan 2028 | 366 days | 430 | A | Westwood |
| Noble GreatWhite | HE semi | NCS | Aker BP | Q2 2027 | 3 years | ~432 | B | DC Mar |
| Deepsea Nordkapp (extension) | HE semi (2019) | NCS | Aker BP | Jan 2028 | to end-2028 | — (set at market by two brokers by end-2026) | D | `docs/odl-analysis.md` v2 (Newsweb 17 Jul 2026) |
| Odfjell Deepsea Atlantic (reference) | 6G HE semi | NCS | Equinor | mid-Q3 2026 | to end Q2 2027 (~319 days); options to late Q4 2027 at original pricing | ~464 ($148m, excl. escalation, services, bonus) | B, signed Jan 2025 | Odfjell disclosure 29 Jan 2025; release 16 Oct 2026 |
| Beacon Pacific | 6G HE semi (CIMC Yantai, steel cut 2015; idle since build `[A]`; managed by Odfjell) | UK (Bruce; possibly Kyla and Greater Laggan) | Serica Energy | Q3 2027 | 6 firm wells + options (incl. P&A) | — (not disclosed) | D | Odfjell release 2 Nov (Newsweb); Serica via energy-pedia 2 Nov; Offshore mag 3 Nov |
| Odfjell Hercules | HE semi (2008; SFL-owned, Odfjell-managed) | Canada | Suncor (Westwood); undisclosed (SFL) | Q1 2027 | 400 days minimum | 425 (SFL: ~$170m ÷ 400 days ≈ 425, B) | A | Westwood; SFL release Mar 2026 (via OE Digital, Baird) |
| Transocean Equinox | HE semi (2015) | Australia | Santos | Apr 2027 | ~2 months + priced options to Oct 2027 | 395 | A, short | Transocean fleet status 2 Nov |
| Deepsea Mira | 7G HE semi | Trinidad | Shell | Apr 2027 | ~150 days | ~467 ($70m incl. mob/demob); option ~427 | B, short | Splash247 (date `[?]`, Sep/Oct) |
| Noble Developer | 6G semi | Trinidad | BP | 2026/27 | 240 days | 375 | A | Westwood |
| Noble Claus Bachmann | 6G semi | UK | BP | Mar 2027 | 150–210 days | ~320 | C | Hartl |
| ENEOS Hakuryu-5 | Benign semi (1977, moored, ≤ ~500 m) | Timor-Leste (KTJ, PSC 19-11) | Finder Energy (JV with TIMOR GAP) | 1 Dec 2027 (window to 15 Mar 2028) | 3 wells, ~150 days (minimum 140) + 2 option wells; conditional on FID (30 Nov 2026) and approvals | ≤ ~282–302 all-in ($42.3m estimated gross JV cost) | C (upper bound) | Finder release 19 Oct (via energy-pedia); OE Digital 20 Oct; Offshore mag |
| Ventura SSV Catarina | semi | Indonesia | Searah JV (Eni / Petronas) | Oct 2026 | 70 days | 278.9 | A, short | Westwood October edition |
| Arabian Drilling × 4 | jackups | Saudi/Kuwait (KJO) | KJO | end Q4 2026 | 4 years | ~91 (SAR 2bn ÷ 5,840 rig-days) | B | DC 28 Sep |
| Northern Offshore Embracer | jackup | Saudi–Kuwait Neutral Zone | KJO | Mar 2027 | 1,460 days | 91.3 | A | Westwood October edition |
| ADNOC Drilling × 2 | high-spec jackups (1 owned, 1 bareboat-chartered) | Kuwait | KOC | Q4 2027 | 4 years firm incl. mob + 1-year option each | ~107 ($313.6m maximum ÷ 2,920 rig-days, incl. mob; upper bound) | B | World Oil 9 Nov; OE Digital; The National 10 Nov |
| ARO-owned jackups × 5 | jackups | Saudi Arabia | Saudi Aramco | Oct 2026 (continuation) | 3-year extensions | — | D | Valaris fleet status 2 Nov |
| Shelf Perseverance (ADES) | JU-2000E, 400 ft | Indonesia | Pertamina Hulu Mahakam | end-Dec 2026 | 406 days + 30-day option | ~106 ($46.17m firm + option incl. mob/demob ÷ 436 days); ex-mob ~100–104 `[A]` | B | OE Digital 3 Nov (ADES release) |
| Velesto NAGA 8 | jackup | Malaysia | Chevron (Hess) | Aug 2026 | 547 days | 95 | A | Westwood |
| PV Drilling VI | jackup | Malaysia | Dialog | Mar 2026 | 180 days | 97 | A | Westwood |
| Velesto NAGA 2 | jackup | Malaysia | PCSB | Feb 2026 | ~5 years | ~86 ($157m) | B | Velesto / Bursa |
| Foresight Aryabhatt 1 / Vivekanand 1 | 350 ft jackups | Thailand | PTTEP | Feb/Apr 2027 | 5 years + 3 options | 60–70 | C | Splash247; SED analysis |
| ADES Key Singapore / Admarine 10 | standard jackups | India | ONGC | ~Q1 2027 | 3 years each | ~54 ($117.2m for two incl. mob ÷ 2,190 days) | B (not high-spec) | OE Digital; Saudi Gulf Projects (Nov) |
| Shelf Tenacious (ADES) | jackup, BMC Pacific 375 (2007) | Angola | (Chevron CABGOC on the prior extension) | Q1 2027 (continuation) | 1 year (priced option exercised) | ~142 ($52m ÷ 365) | B (option; not a new print) | OE Digital 3 Nov (ADES 27 Oct) |
| ADES Main Pass IV | jackup | Nigeria | Belbop | Jul 2026 | 365 days | 132 | A | Westwood |
| Valaris 248 | HE jackup | UK | NEO NEXT+ | Apr 2027 | 1,080 days (41-well P&A) | ~130 ($140m) | B | Westwood; Valaris FSR 5 Aug |
| Valaris (fleet award) | jackup | UK Southern North Sea | — (P&A) | window to Dec 2030 | 341 days + 19-day option | ~122 ($41.5m) | B | Valaris PR 7 Oct |
| Valaris 122 | jackup | Denmark | INEOS | Feb 2027 | 126 days + options 699 days | 115 | A | Valaris PR 7 Oct |
| VALARIS 122 | jackup (2014) | UK | INEOS | Jul 2027 | 158 days + 541 days of options (UK/Denmark) | 125 | A, short | Valaris fleet status 2 Nov |
| VALARIS Norway | HE jackup (2011) | UK | Ithaca Energy | Q2 2027 | ~200 days + 163 days priced options | ~135 ($27m) | B, short | Valaris fleet status 2 Nov |
| Valaris 123 | jackup | Poland | — | — | 1 well + option | 135 | A | Valaris FSR 5 Aug |
| Noble Intrepid | CJ70 HE jackup | UK, then NCS | BP UK, then ORLEN Upstream Norge | to Sep 2027; Q3 2027 | 1 well, 40–60 days (ORLEN) | 150 (BP UK) | A for BP; D for ORLEN | Offshore Energy / Ocean News (Sep) |
| Valaris 107 | jackup | Australia | Golden Beach | Oct 2026 | 150 days | 163 | A | Valaris FSR |
| Valaris 107 | jackup | Australia | — | after current work | ~300 days + priced options | ~167 ($50m excl. mob) | B | Valaris PR 7 Oct |
| VALARIS 107 | jackup (2006) | Australia | Emperor Energy | Q2 2027 | 1 well, ≥ 30 days | 165 | A, short | Valaris fleet status 2 Nov |
| VALARIS 106 (extension) | jackup (2005) | Indonesia | BP | Q4 2028 | 1 well, ~90 days + 3 options | ~111 ($10m) | B, short | Valaris fleet status 2 Nov |
| Energy Drilling T-16 (Phase 7) | Tender barge (2013, COSCO Nantong) | Malaysia–Thailand JDA | CPOC (Carigali-PTTEPI) | early Q3 2027 (after ~5 months idle in Singapore) | 30 months firm + up to 15 months options | ~95.1 (USD 87m firm incl. undisclosed mobilisation ÷ ~915 days); ~89–92 ex-mob `[A]` | B | SED/Energy Holdings release (MFN) 27 Oct 07:00 |
| Energy Drilling T-16 (Phase 6, reference) | Tender barge | Malaysia–Thailand JDA | CPOC | Nov 2024 | firm to Dec 2026; campaign to Q1 2027 on options | 131 (options 124) | A (company) | `docs/SED-analysis.md` (Pareto 17 Sep); MFN 27 Oct |

### Rig-by-rig availability and cover (main contractors; Q3 fleet status reports, 26 Oct–4 Nov, plus releases to 12 Nov)

- **Transocean** (27 rigs: 20 UDW, 7 HE; fleet status 2 Nov, 10-Q 3 Nov):
  - Backlog **$7,966m** (UDW $5,189m, HE $2,777m). $2.0bn was added since August at a weighted ~$423k.
  - Uncommitted fleet rate (excl. priced options), rest-2026 / 2027 / 28 / 29 / 30: UDW 15% / 22% / 56% / 80% / 93%; HE 0% / 8% / 31% / 47% / 74%.
  - Q3 utilization: UDW 67.6% (3 rigs idle or preparing), HE 95.1%. Average daily revenue: UDW $442.1k, HE $504.3k. Revenue efficiency: 96.4% / 97.7%.
  - Average contract dayrates: UDW Q4-26 $454k → Q3-27 $443k; HE $478k → $465k.
  - Stacked: Ocean Rig Apollo, Athena and Mylos (since 2016–17).
  - **UDW:** Proteus US Gulf Feb 2027–Jan 2029, $465k. Conqueror Equatorial Guinea Jan–Jul 2027 ($465k), then US Gulf Aug 2027–Nov 2028 ($499k). Asgard East Med Dec 2026–Dec 2027, $405k. Skyros Chevron Australia Mar 2027–Feb 2028 ($406k per Westwood), priced options to Jul 2030. KG2 ONGC Feb 2027–Feb 2029, $389k, priced options to Feb 2031; KG1 Reliance to Mar 2028, $410k. Petrobras 10000 to Aug 2029 ($428k → $454k in steps). Corcovado and Orion Petrobras to Nov 2030 / Mar 2030, $392k; Aquila Petrobras to Jun 2028, $442k. Atlas available early 2027, then bp from Jun 2028 ($635k, 8G; not comparable).
  - **HE:** Norge Harbour/OMV to Jan 2028 ($476k / $558k), Harbour Jan–Oct 2028 ($517k) + priced options to Mar 2029, Shell Mar–Jul 2029 ($517k). Spitsbergen Equinor to Dec 2027 ($417k → $519k from Apr 2027), then open. Barents Romania to Jan 2027 ($498k), yard Feb–Jun 2027, Vår Jun 2027–Jun 2030 ($470k). Enabler to Apr 2031, Encourage to May 2030 (bridge from May 2027 at $441k), Endurance Jun 2027–Jun 2029 (Equinor, $402k in the package terms). Equinox Santos, Australia, Apr–Jun 2027 ($395k) + options to Oct 2027.
- **Valaris** (fleet status 2 Nov; 10-Q 3 Nov):
  - Backlog ~$4.75bn (+~$600m since 5 Aug). Drillship contracted days: 3,152 in 2027 (≈ 8.6 rig-years of 10 active drillships) at a backlog average of $432k (2028+: $417k). Jackup backlog average 2027: $130k.
  - Drillships: Brazil DS-4 to Oct 2030, DS-8 to Shell Brazil from Mar 2027 (~800 days), DS-17 Equinor Brazil to Jan 2028. Angola and Nigeria: DS-7 Angola to Sep 2027, DS-9 Angola to Jul 2028, DS-10 Nigeria to Jul 2028. DS-12 BP Egypt to Apr 2027, plus 60 days in late 2027 / early 2028. DS-15 Spain / Côte d'Ivoire to May 2027. US Gulf: DS-16 to Dec 2028; DS-18 Petronas Suriname Nov 2026–May 2027, then 914 days for Occidental in the US Gulf.
  - Stacked: DS-11, DS-13 and DS-14 (Spain); jackups 148, 147 and 143 (UAE) and Viking (UK).
  - Jackups: 248 UK P&A to Mar 2030; 115 Brunei to Apr 2029; 110 Qatar to Oct 2029; 122 Denmark to ~Jun 2027, then UK from Jul 2027 ($125k); 107 Australia; VALARIS Norway Ithaca from Q2 2027; 121 East Irish Sea from Nov 2026; 72 finishes Mar 2027. VALARIS 111 was sold for MOPU conversion. Seven units are leased to ARO.
  - Middle East: all Valaris and ARO rigs under contract; five ARO-owned rigs have 3-year Aramco extensions. Merger closing ~1 Dec 2026.
- **Odfjell** (Q3 of 3 Nov; firm backlog $2.5bn; Q3 financial utilization 89%, September 98%):
  - Deepsea Bergen: Equinor to Q1 2028, then Vår 3 years to Q1 2031 (contract signed 10 Nov) plus four 1-year priced options to 2035.
  - Deepsea Nordkapp: Aker BP, firm to end-2028; the rate is set at market by two brokers by end-2026.
  - Deepsea Aberdeen: Equinor to Q1 2029. Deepsea Stavanger: Aker BP to ~Q1 2030.
  - Deepsea Atlantic: Equinor, firm to late Q4 2027, then two priced wells and three ~1-year periods as options. Off hire 106 days Apr–Aug 2026 (BOP incident; a company issue).
  - Hercules (SFL-owned, managed by Odfjell): Canada, ≥ 400 days from Q1 2027 (~$170m ≈ $425k, B); not an NCS rig in 2027.
  - Beacon Pacific (owned by a CIMC affiliate, managed by Odfjell, the ninth HE rig in its managed and owned fleet): Serica UK from Q3 2027, six firm wells.
- **Seadrill** (Q3 release 3 Nov; 10-Q 4 Nov):
  - Backlog $2,813m; drilling contracts $2,577m, of which $1,207m in 2027 and $614m in 2028. More than 85% of available 2027 drillship days are contracted.
  - West Neptune: LLOG, 365 days from Sep 2026. West Vela: 270 days from Aug 2026. West Polaris: Petrobras to Jan 2028, then 1,095 days. West Capella: PTTEP, Malaysia, to Feb 2028. West Carina (2015 7G): Indonesia, H1 2027, 880 days firm + 880 days priced options. Sonangol Libongos: Angola to Jan 2030. Sevan Louisiana: Kosmos (25 days, Nov 2026), then ~60 days for LLOG.
  - West Vela, West Elara and Sevan Louisiana had time between contracts in Q3. The fleet status PDF was not read.
- **Noble** (Q3 release 26 Oct; 23 marketed floaters 66% contracted in Q3; 5 marketed UHE jackups 86%; backlog $6.7bn; "~20% more contracted capacity in H2 2027 than H1 2027"):
  - Viking: Brunei from Jan 2028, $460k. Faye Kozack: Petrobras to Jan 2027, then Tullow Ghana from mid-2027. BlackRhino: TotalEnergies Nigeria from Q4 2026. BlackHawk: Apache Uruguay, Q4 2027.
  - Globetrotter I: Occidental Peru from Q2 2027 ($400k), then a TotalEnergies intervention capacity reservation. Globetrotter II: sale ($38m) pending.
  - GreatWhite: Aker BP from Q2 2027, 3 years. Claus Bachmann: BP UK from Mar 2027.
  - Interceptor: DNO, then ConocoPhillips Ekofisk P&A from Q3 2027 (670 days). Intrepid: BP UK to Sep 2027 ($150k), then ORLEN Norway in Q3 2027.
- **Borr** (no release since 30 Sep apart from the Prospector 5 updates; Q3 ~18 Nov):
  - 2026 cover 73% at ~$134k (Q2 report, 11 Aug).
  - Norve: West Africa, Dec 2026–Aug 2027. Natt: Shell Nigeria to Aug 2027. Joro: UK accommodation to Dec 2026. Odin: US from 11 Sep. Idun: Vietnam, Q4 2026. Bestla: ENI to Sep 2027.
  - Perfomex divested; Borr keeps the Mexico rigs on bareboat economics. Fontis JV: 3 of 5 contracted (Aug). Prospector 5 lost (24 Oct).
- **ADES / Shelf:** Perseverance PHM Indonesia from end-Dec 2026 (406 days); Tenacious Angola, +1 year from Q1 2027; Key Singapore and Admarine 10 ONGC, 3 years from ~Q1 2027. Saudi offshore rigs all resumed since Aug.
- **Cold-stacked drillships (9, Westwood):** six in Transocean–Valaris (Ocean Rig Apollo 2015, Athena 2014, Mylos 2013; VALARIS DS-11 2013, DS-13 2023, DS-14 2023); three with other owners `[?]`. No reactivation without a long contract.
- **Stranded units:** Keppel RigCo at Seatrium: a 7G drillship (delivery 2027) and an N-class HE jackup (2028), being completed with no contract; two mid-water HE semis for NW Europe, completion under assessment. CIMC: Beacon Pacific, to the UK for Serica (Q3 2027).

### Sources

| Source | Content | Definition | Observed / published |
|---|---|---|---|
| [Westwood Offshore Energy Data Dashboard](https://www.westwoodenergy.com/news/infographics/offshore-energy-data-dashboard), October edition (re-read 12 Nov: no newer edition) | Sep activity: MCU drillships 93% / semis 82% / jackups 88%; committed 80 / 59 / 384; available 6 / 12 / 54; cold-stacked 9 / 7 / 51; backlog 1 Sep (restated) → 1 Oct; month-by-month backlog Feb–Sep editions; fixtures (Embracer $91,267; Catarina $278,888; Conqueror $470,588) | MCU = contracted ÷ marketed; backlog in rig-years, **start-of-month snapshots**, prior month restated per edition; total fleet derived from the counts | Sep activity / published 25 Oct, updated 27 Oct 2026 |
| [Westwood weekly global rig count](https://www.westwoodenergy.com/news/infographics/weekly-global-offshore-rig-count) (read 12 Nov) | Working jackups / floaters: 376 / 136 (26 Oct), 374 / 137 (2 Nov), 376 / 137 (9 Nov); October commentary: jackups up in South America, North America, Europe and Asia, down in the Middle East and Africa; floaters up in North and South America | Working rigs (RigLogix), Monday counts; the monthly narrative does not always match the table (table used) | 26 Oct–9 Nov 2026 |
| [Westwood Brazil offshore rig count](https://www.westwoodenergy.com/news/infographics/brazil-offshore-rig-count) (read 12 Nov) | 47 rigs, 35 drilling; 25 DS, 9 semis, 10 platform, 3 jackups; Petrobras 34; outstanding minimum rig-days 2027 210 / 2028 1,185 / 2029 780 | Operating vs drilling; prospects + tenders | Data 1 Nov 2026 |
| [Riviera — Westwood: rig dayrates (mostly) continue to fall in 2026](https://www.rivieramm.com/news-content-hub/news-content-hub/westwood-offshore-rig-dayrates-mostly-continue-to-fall-in-2026-89065) | Leading-edge 2026 YTD: drillships 6G 371 / 7G 407 / avg 388; semis < 340, Norway 436; jackups ~94 excl. Norway/Australia; utilization mid-June | RigLogix leading-edge averages (Teresa Wilkie, Westwood) | YTD to mid-June / 15 Jun 2026 |
| [Transocean fleet status report, 2 Nov 2026](https://www.deepwater.com/documents/FleetStatusReport/2026/November%202026%20Fleet%20Status%20Report.pdf) (8-K exhibit; PDF read via text extraction) | Rig-by-rig customer, dates and dayrates; updates (Conqueror, Proteus, KG2, Norge–Shell, Equinox); average contract dayrates by quarter; backlog ~$8.0bn | Full contractual operating dayrate; excludes mobilisation; NCS rates include a non-USD component and escalation (footnotes 1, 2) | As of 2 Nov 2026; read 4 Nov |
| Transocean 10-Q Q3 2026 (FinancialFilings 75463011) | Uncommitted fleet rates 2026–30; backlog by class; average daily revenue; revenue efficiency; utilization; outlook | Uncommitted = idle or stacked days ÷ calendar days, excluding priced options | Q3 2026 / filed 3 Nov 2026 |
| [Transocean 8-K — Equinor approval and Norge–Shell](https://www.sec.gov/Archives/edgar/data/0001451505/000145150526000072/rig-ex99d1.htm); [World Oil — Transocean/Equinor](https://worldoil.com/news/2026/6/30/transocean-lands-seven-year-1-billion-equinor-rig-deal/) | Equinor $1.0bn firm, 7 rig-years, $399k base (approval late Sep); Norge Shell 2 wells, ~120 days, $62m | Backlog excl. additional services | 9 Oct 2026; 30 Jun 2026 |
| [Transocean 8-K — 2026 outlook](https://www.sec.gov/Archives/edgar/data/0001451505/000145150526000041/rig-20260504xex99d1.htm) | 2026 capex $150m | Total capex, no maintenance split; ÷ 27 floaters = $5.6m a rig `[B]` | 4 May 2026 |
| [Zacks analyst report — RIG](https://www.zacks.com/zer/report/RIG) | Management view: > 90% high-spec 2027; ~100 rig-years H1; ~40 tenders (75–80 rig-years); Brazil 30–33 rigs; Africa 20–25; O&M guidance; reactivation $100–150m; Proteus/Conqueror $550m (19 Oct) | Contractor commentary relayed `[E]`, grade C | 22 Sep and 23 Oct 2026 |
| Valaris Q3 release and fleet status (FinancialFilings 75379362, 75382064) | Q3 results (adjusted EBITDA $151m; ~$24m Middle East impact); merger close ~1 Dec; new awards; contracted days and average rates by class; Middle East status; ARO extensions | Backlog excludes lump-sum mobilisation | As of 2 Nov 2026 |
| [Valaris PR — contract awards and fleet status updates](https://s23.q4cdn.com/956522167/files/content_files/10-7-2026-Valaris-Announces-Contract-Awards-and-Fleet-Status-Updates.pdf) | DS-18 Suriname; 107 Australia $50m; SNS P&A $41.5m; 122 $115k; 121/72 Eni; MS-1 and 111 retired/sold | Backlog excl. lump sums | 7 Oct 2026 |
| [Valaris fleet status report (8-K)](https://www.sec.gov/Archives/edgar/data/0000314808/000031480826000139/fsrex99_1august2026.htm) | 248 P&A ($140m), 123 Poland $135k, 122 and 107 prior contracts, DS-16/18 Occidental | As-of 5 Aug | 5 Aug 2026 |
| Noble Q3 release (FinancialFilings 74765190) and 10-Q (74797448) | Floater 66% contracted, UHE jackups 86%; Tier-1 leading edge "mid-$400,000s to $500,000"; UHE jackups $230–300k; new awards; Resolve / Globetrotter II sales | Company statements; backlog excludes mobilisation | 26 / 27 Oct 2026 |
| Seadrill Q3 release (FinancialFilings 75462278) and 10-Q Q3 2026 (FinancialFilings 75612466) | Awards since August (~$800m TCV); > 85% of 2027 drillship days contracted; backlog $2,813m by year; RigLogix contracted rigs and marketed utilization (30 Sep): benign floaters 107 / 87%, HE floaters 23 / 97%, HE jackups 27 / 95%; "signs that point towards a market recovery in 2027" | TCV includes mobilisation; RigLogix series is a different source from the Westwood dashboard (context only) | 3 Nov / filed 4 Nov 2026 |
| [Splash247 — Indonesia award leads new batch of Seadrill contracts](https://splash247.com/indonesia-award-leads-new-batch-of-seadrill-contracts/) (user input) | West Carina $420m / 880 days; West Capella options $41m + $53m; Libongos to Jan 2030; Sevan Louisiana | Values incl. mob, excl. services; secondary (Seadrill release) | 13 Oct 2026 |
| Odfjell — Contract signed for Deepsea Bergen (Newsweb); [OE Digital — Deepsea Bergen/Vår](https://www.oedigital.com/amp/news/542860-v-r-energi-picks-odfjell-drilling-s-deepsea-bergen-for-multi-year-drilling-ops); [Discovery Alert](https://discoveryalert.com/news/deepsea-bergen-rig-contract-odfjell-var-energi-november-2026/) | Vår contract signed; 3 years from early 2028, $518m incl. mob; four 1-year priced options to early 2035; CEO on the Q3 call: options near $500k after FX and escalation | Primary (Oslo Børs) plus secondary `[E]`; value excl. escalation, services, bonus | 10 Nov 2026, 06:06 UTC; 10 Sep 2026 |
| [Odfjell — New management agreement and contract award for Beacon Pacific](https://www.inderes.dk/en/releases/odl-odfjell-drilling-ltd-new-management-agreement-and-contract-award-for-beacon-pacific); [energy-pedia — Serica secures rig](https://www.energy-pedia.com/news/united-kingdom/serica-energy-secures-rig-for-multi-well-ukcs-drilling-programme-205915); [OE Digital — Odfjell adds rig](https://www.oedigital.com/news/544051-odfjell-drilling-adds-new-rig-to-fleet-ahead-of-serica-s-uk-drilling-campaign); [Upstream — CIMC cuts steel on Beacon Pacific](https://www.upstreamonline.com/online/cimc-cuts-steel-on-beacon-pacific/1-1-1166912) | Serica contract with Beacon Pacific Offshore (CIMC affiliate); six firm wells from Q3 2027; Odfjell manages; reactivation partly begun; similar to Deepsea Yantai; 6G semi upgraded to 620 m; steel cut June 2015 | Primary (no rate); trade press; build history (idle since build `[A]`) | 2–3 Nov 2026; 2015 |
| [Odfjell — Equinor exercises options for Deepsea Atlantic](https://www.inderes.fi/en/releases/odfjell-drilling-ltd-equinor-exercises-options-for-two-additional-wells-for-deepsea-atlantic); [Odfjell — Extension of Deepsea Atlantic contract](https://www.odfjelldrilling.com/disclosure/odfjell-drilling-ltd-extension-of-deepsea-atlantic-contract/); [Offshore Energy — BOP incident](https://www.offshore-energy.biz/2026/10/16/equinor-employs-2009-built-odfjell-drilling-rig-for-additional-wells) | Two wells in direct continuation, firm to late Q4 2027, original contract pricing, two further priced wells; Jan 2025 extension ~$148m (÷ ~319 days ≈ $464k `[B]`); 106 days off hire | Primary (Oslo Børs) and trade press | 16 Oct 2026; 29 Jan 2025 |
| `docs/odl-analysis.md` v2 (4 Nov) | Odfjell Q3 (3 Nov): Bergen options to 2035, Nordkapp to end-2028, Atlantic to late Q4 2027, price-implied ~$413k through-life | Company analysis in this workspace (read only) | 4 Nov 2026 |
| OGJ / OE Digital (Apr 2026) | Transocean Barents–Vår Energi 1,095 days from mid-2027 at ~$450k, ~$490m (signing value) | Secondary, matches the Transocean release | 8–9 Apr 2026 |
| [Shipping Telegraph — Bollsta sale](https://shippingtelegraph.com/offshore-news/odfjell-drilling-acquires-semi-sub-rig-from-northern-ocean-for-480m/) | $480m, $355m backlog | Transaction price | 17 Nov 2025 |
| [Offshore Energy — Deep Value Driller sale](https://www.offshore-energy.biz/saipem-loses-drillship-deal-to-higher-bidder/) | $300m to Eldorado (Saipem bid $272.5m) | Transaction price, 2014 7G | Feb 2026 |
| [OE Digital — Ocean Oilfield brings Noble jackup into its fleet](https://www.oedigital.com/news/543761-ocean-oilfield-brings-noble-corporation-s-jack-up-rig-into-its-fleet); [Noble — planned divestment of six jackups](https://s201.q4cdn.com/439848451/files/doc_news/2025/12/Noble-announces-planned-divestment-of-six-jackups.pdf); [AllAfrica — Tunisia: drilling off Hammamet](https://fr.allafrica.com/stories/202611070164.html) | Noble Resolve → Ocean MVM, $64m cash, CJ50-X100 MC; Tende Energy Abiod well (Maâmoura permit) | Transaction price (agreed Dec 2025); build year not confirmed `[?]`; trade press (French) | 15/19 Oct 2026; 11 Dec 2025; Nov 2026 |
| [OE Digital — Dolphin sells Blackford Dolphin](https://www.oedigital.com/news/543921-dolphin-drilling-sells-blackford-dolphin-semi-sub-forges-new-rig-partnership); [Baird Maritime](https://www.bairdmaritime.com/offshore/drilling-production/blackford-dolphin-sale-to-spm) | $10m on delivery + $15m on first contract payment; SPM markets in India; Dolphin manages; built 1974, upgraded 2008 | Transaction price | 26 Oct 2026 |
| [Offshore mag — RigCo to complete four rigs with Seatrium](https://www.offshore-mag.com/rigs/news/55415204/seatrium-rigco-to-invest-over-s500-million-to-complete-four-offshore-drilling-rigs-with-seatrium); [Baird Maritime](https://www.bairdmaritime.com/offshore/vessels-rigs/seatrium-to-complete-keppel-rigs) | 7G drillship (2027), N-class HE jackup (2028), two mid-water HE semis (under assessment); > S$500m (~$390m); positioned for charters; no contracts | Company deal via trade press | 26–28 Oct 2026 |
| [Baird Maritime — Transocean–Valaris approvals](https://www.bairdmaritime.com/offshore/drilling-production/transocean-valaris-merger-regulatory-approvals) | All approvals (DOJ, CADE, unconditional); shareholder votes 24 Nov; Bermuda court 26 Nov; close ~1 Dec | Trade press citing the companies | Nov 2026 |
| [World Oil — ADNOC Drilling enters offshore Kuwait](https://worldoil.com/news/2026/11/9/adnoc-drilling-enters-offshore-kuwait-with-two-jackup-rig-contracts-from-koc/); [The National](https://thenationalnews.com/business/energy/2026/11/10/abu-dhabis-adnoc-drilling-wins-contracts-worth-314m-from-kuwait-oil-company) | KOC: 2 jackups, 4 years firm incl. mob + 1 option year, Q4 2027, $313.6m maximum (KWD 96.6m); 1 owned, 1 bareboat-chartered; LOA | Contract value (maximum) ÷ days `[B]` | 9–10 Nov 2026 |
| [OE Digital — ADES lands Angola and Indonesia deals](https://www.oedigital.com/amp/news/544092-ades-lands-new-offshore-drilling-rig-deals-in-angola-and-indonesia); [OE Digital — ADES lands $117m ONGC contracts](https://www.oedigital.com/news/544212-ades-lands-117m-ongc-drilling-contracts-for-two-jack-ups) | Tenacious +1 year (~$52m); Perseverance PHM 406 + 30 days ($46.17m incl. mob/demob); Key Singapore and Admarine 10, 3 years each, $117.2m incl. mob | Values ÷ days `[B]`; ONGC units standard | 3 Nov and 9–11 Nov 2026 |
| [Drilling Contractor — KJO award](https://drillingcontractor.org/arabian-drilling-wins-four-jackup-offshore-contract-from-kjo-80162) | 4 jackups, 4 years, SAR 2bn | Contract value | 28 Sep 2026 |
| [World Oil — Velesto/Chevron](https://worldoil.com/news/2026/7/22/velesto-secures-51-million-chevron-malaysia-drilling-contract/); Velesto/Bursa (NAGA 2) | NAGA 8 Chevron; NAGA 2 PCSB $157m 2026–2030 | Value | Jul / Mar 2026 |
| [OE Digital — Tender-assist rigs head for full utilization (Westwood, P. Ezekiel)](https://www.oedigital.com/news/544178-tender-assist-rigs-southeast-asia-s-quiet-workhorses-head-for-full-utilization) | 29 TARs (16 active, 6 warm, 6 cold, 1 under construction); utilization ~96% → 100% by end-Q4; four TARs > $120k; 2027 semi-tender campaigns; PTTEP TAR vs jackup choice | Westwood commentary `[E]` | 5 Nov 2026 |
| [MFN — Energy Drilling receives letter of award for T-16](https://mfn.se/a/energy-holdings/energy-holdings-energy-drilling-receives-letter-of-award-for-30-month-drilling-campaign-for-t-16) | T-16 Phase 7: CPOC, 30 months from early Q3 2027, options up to 15 months, ~USD 87m firm incl. mobilisation; Phase 6 firm to Dec 2026, ends Q1 2027 | Primary (company release); no dayrate; value ÷ days `[B]`; ~915-day divisor `[A]` | 27 Oct 2026, 07:00 |
| [OE Digital — Finder Energy selects ENEOS rig](https://www.oedigital.com/news/543783-finder-energy-selects-eneos-rig-for-drilling-job-off-timor-leste) (user input); [energy-pedia — Finder secures rig](https://www.energy-pedia.com/news/timor-leste/finder-energy-secures-drilling-rig-secured-for-ktj-development-205713); [Offshore mag](https://www.offshore-mag.com/drilling-completion/news/55412349/finder-selects-hakuryu-5-rig-for-ktj-development-drilling-offshore-timor-leste); [Splash247 — Hakuryu-5 history](https://splash247.com/japan-drilling-awarded-semisub-contract-by-inpex/) | Hakuryu-5 (1977 Mitsubishi build), KTJ 3 firm + 2 option wells, start 1 Dec 2027, ~150 days, $42.3m estimated gross JV cost, conditional on FID and approvals | Company release reproduced; cost estimate, not contract value | 19–20 Oct 2026 |
| [Splash247 — Deepsea Mira/Shell](https://splash247.com/northern-ocean-scores-70m-shell-semisub-deal) | 150 days, $70m incl. mob; option to $226m | Value; page blocked (403), figures via search summary `[E]` | Sep/Oct 2026 |
| [Ocean News — Noble Intrepid/ORLEN](https://oceannews.com/news/energy/noble-intrepid-jackup-rig-tapped-for-orlen-exploration-drilling-offshore-norway/); [OE Digital — Noble Interceptor/ConocoPhillips](https://www.oedigital.com/news/541887-conocophillips-hire-noble-corporation-s-jack-up-for-ekofisk-p-a-work) | NCS jackup work Q3 2027; Intrepid BP $150k | Trade press | Sep 2026 |
| [Borr Q2 2026 (6-K)](https://www.sec.gov/Archives/edgar/data/0001715497/000114036126032598/ef20080031_ex99-1.htm) and [results call](https://www.sec.gov/Archives/edgar/data/1715497/000114036126032598/ef20080031_ex99-2.htm) | Cover 73% at ~$134k; Fontis JV $287m; economic utilisation 96.4%; capex $2–2.5m a rig a year; H1 cash tax 4.5% of revenue; Odin opex mid-$70k | Asset-value convention parameters (jackups) | 11–12 Aug 2026 |
| [Borr contracting update](https://finance.yahoo.com/energy/articles/borr-drilling-limited-contracting-updates-203900488.html); Borr 6-Ks 29 Oct and 2 Nov (FinancialFilings 75118812, 75346449); [Offshore Energy — Borr jackup sinks off Gabon](https://www.offshore-energy.biz/2026/10/25/rig-incident-110-rescued-5-still-missing-after-borr-drillings-jack-up-sinks-off-gabon-coast) | Norve, Natt, Joro; Prospector 5 (2014 JU-2000E) sank 24 Oct during preload; no Gulf notice | Company releases; trade press | 30 Sep; 24 Oct–2 Nov 2026 |
| [Westwood Insight — Middle East conflict reverberates through jackup market](https://www.westwoodenergy.com/news/westwood-insight/westwood-insight-middle-east-conflict-reverberates-through-jackup-market) | Arabian Gulf ~36% of global jackup supply; working 83% → ~69%, committed ~90%; Aramco, KOC, KJO tenders (~56 rig-years) | Westwood commentary `[E]` | 13 May 2026 |
| [Drilling Contractor — ADES resumes all suspended offshore rigs in Saudi Arabia](https://drillingcontractor.org/ades-resumes-all-suspended-offshore-rigs-in-saudi-arabia-79312); [AGBI](https://www.agbi.com/oil-and-gas/2026/08/ades-confirms-all-offshore-rigs-in-saudi-arabia-are-operational/); [Arabian Drilling — Tadawul disclosure](https://www.saudiexchange.sa/Resources/fsPdf/28194_3703_2026-08-12_08-33-13_en.pdf); [Khaleej Times — Kuwait drone attack](https://www.khaleejtimes.com/world/gulf/kuwait-drone-attack-offshore-oil-platform-injures-worker?amp=1) | All suspended Saudi offshore rigs resumed (CEO: 10 Gulf rigs halted in March); KOC offshore drilling platform hit 12 Jul | Company disclosures via trade press; Kuwait MoD via press | 12 Jul; 11–12 Aug 2026 |
| Gulf escalation reports: [Rigzone/Bloomberg](https://www.rigzone.com/news/saudi_aramco_evacuates_hq-22-oct-2026-184909-article), [Reuters via Al-Monitor](https://www.al-monitor.com/originals/2026/10/us-orders-departure-diplomats-saudi-arabia-amid-houthi-strikes), [The National](https://thenationalnews.com/business/energy/2026/10/23/oil-prices-rise-as-houthis-launch-another-wave-of-attacks-on-saudi-arabia), [gCaptain](https://gcaptain.com/two-more-tankers-struck-as-maritime-attacks-spread-across-persian-gulf/), [MarineLink](https://www.marinelink.com/news/houthi-missile-strikes-saudi-oil-refinery-543943) | Dhahran HQ evacuation; Dammam airport and Shaybah attacks; tanker strikes; Ras Tanura claim; no offshore rig or platform mentioned | Wire and trade press; claims `[E]` | 21–27 Oct 2026 |
| [Drilling Contractor (home page)](https://drillingcontractor.org/) | Headlines 4–11 Nov: Bergen formalised; ADNOC Kuwait; Ocean MVM Tunisia; ADES ONGC; Velesto NAGA 3; US Gulf demand outlook (27 Oct) | Index page | Read 12 Nov 2026 |
| [World Oil — Venus terms still under negotiation](https://www.worldoil.com/news/2026/10/15/totalenergies-namibia-still-negotiating-venus-terms-as-2026-fid-target-nears/); [Offshore mag — Venus fiscal accord](https://www.offshore-mag.com/field-development/news/55398042/totalenergies-awaits-fiscal-accord-before-venus-fid-offshore-namibia); [The Namibian — "before 2027"](https://www.namibian.com.na/venus-decision-must-come-before-2027-totalenergies/); [World Oil — Mopane](https://worldoil.com/news/2026/9/3/totalenergies-completes-entry-into-giant-mopane-discovery-offshore-namibia/) | Venus FID not taken, fiscal terms open; Mopane FID 2028 | Bloomberg via trade press | 15 Oct 2026; 3 Sep 2026 |
| [World Oil — Petrobras extensions](https://worldoil.com/news/2026/4/14/transocean-adds-445-million-backlog-with-petrobras-drillship-extension/); [Deepwater Insight — Petrobras round](https://deepwaterinsight.com/petrobras-rig-tender-results-3-6-billion-in-deepwater-contracts-across-buzios-mero-and-renecon/) | $3.6bn cycle; DS-4, ODN I | Value ÷ days | Mar–Apr 2026 |
| [Deepwater Insight — 7G market update](https://deepwaterinsight.com/7g-drillship-market-update/) | 7G MCU low 80s → ~89% by early 2027; Asgard $405k; Atlas $635k | Secondary `[E]` | 18 Apr 2026 |
| [Hartl — Offshore Drillers Q2 2026](https://arminhartl.substack.com/p/offshore-drillers-2026-q2-review); [Hartl — Offshore Supply Unpacked](https://arminhartl.substack.com/p/offshore-supply-unpacked) | Management guidance; Claus Bachmann ~$320k; opex floaters ~$225k, jackups ~$90k; reactivation $85–150m, 12–18 months; recycling values | Secondary `[E]`, grade C | 10 Aug 2026; 14 Jan 2026 |
| [Westwood Insight (via Hellenic) — newbuild orders](https://www.hellenicshippingnews.com/1001334-2/); [Energy Intel](https://www.energyintel.com/0000017b-a7d8-de4c-a17b-e7dad29d0000) | Newbuild $850m–1bn+, required $650–720k | Secondary `[E]` | 2024–2025 |
| [Offshore mag — jackups and the 25-year life](https://offshore-mag.com/drilling-completion/article/16763186/jackups-new-market-niches-for-aging-drilling-equipment); Transocean 10-K (jackup non-operating life 30 years) | Economic-life conventions | Industry rule of thumb / accounting life `[E]` | older |
| `docs/oil-market-bbb.md` | Brent paths, mid-cycle, long end, catalysts | Front-month futures basis | 11 Nov 2026 (full update; "no action" for rig) |
| `docs/SED-analysis.md` | Tender-assist contracts, opex, PTTEP–Foresight evidence | Company analysis `[C]` items as tagged there | 3 Oct 2026 |

**Input rules:**
- Hartl and Deepwater Insight are used only as `[E]`/grade C, never as sole evidence for a Base rate.
- Westwood via Riviera (15 Jun) is a mid-year snapshot of RigLogix aggregates, never the sole basis for a rate.
- Houthi and IRGC claims are kept as `[E]`/`[?]`, and only wire-confirmed items are `[F]`. The absence of a report of an offshore suspension is held as `[?]`, not as evidence of normal operations.
- Deepsea Bergen's signing is dated 10 Nov (Odfjell's Newsweb release, 06:06 UTC), with terms as in the September LOA.
- Discovery Alert's "37 of 38 marketed HE semis committed" is an unverified industry estimate and not used; the RigLogix HE floater figure (97%, Seadrill 10-Q) is used as context instead.
- KOC's $313.6m is a maximum value incl. mobilisation, so the derived ~$107k is an upper bound (B). ADES values include mobilisation and options where stated; derived rates are tagged B with ex-mob estimates `[A]`.
