# Rig Market BBB — 12 November 2026

## Metadata

- **Analysis date:** Thu 12 Nov 2026, Europe/Oslo. **Status: Final** (full update, Update mode, Steps 0–11). Caveats: contract cover is a market proxy plus contractor cover (`[A]`); the latest Westwood monthly is September activity; Borr Q3 and SED Q3 (both ~18 Nov) are not out.
- **Skill:** `rig-market-bbb` revision **2026-10-10.1**.
- **Previous baseline:** 10 Oct 2026 (33 days), with small updates on 13, 17, 22, 24 and 28 Oct and 4 Nov. Their history is in the change log.
- **Why this run:**
  - Stale after 9 Nov (30-day rule).
  - The 4 Nov small update fired the UDW drillship trigger (Base 2027 400 → 420, Bull 430 → 450) and left the sample question to this run (checkpoint 18).
  - Oil Market BBB re-baselined on 11 Nov.
- **Window:** stub Q4-26 + 2027–2029. No roll (that is in January).
- **Stale after 12 Dec 2026** (30 days). Re-run earlier if:
  - a recalibration trigger fires;
  - the Westwood October dashboard (~27 Nov) shows drillship MCU outside 90–96% or drillship backlog below 150 rig-years;
  - the Oil BBB update after OPEC+ (29 Nov) flags a rig-relevant change;
  - Borr or SED Q3 (~18 Nov) meets the rule in checkpoint 17 or 22.
- **Oil Market BBB used:** baseline **11 Nov 2026**, Final, stale after 30 Nov.
  - Brent Bear / Base / Bull: 2027 65 / **84** / 118; 2028 60 / 77 / 102; 2029 60 / 72 / 90; mid-cycle 60 / 70 / 82.
  - Long end (10 Nov settlements): Dec-27 77.6, Dec-28 72.8, Dec-29 70.6, Dec-30 69.1, Dec-31 67.7, Dec-34 64.2.
  - Its "For downstream skills" row for rig: "No (no action now)". This run's own check agrees (Drivers).
- **Series per segment (unchanged):**
  - UDW drillships: Westwood drillship MCU (all drillships, proxy).
  - HE semis (NCS): contract cover of the named NCS fleet, with Westwood semi MCU as context.
  - Benign semis: Westwood semi MCU as an upper bound, benign set below it `[A]`.
  - High-spec jackups: Westwood jackup MCU.
  - Latest observation: September (October edition, 25/27 Oct): drillships 93%, semis 82%, jackups 88%.
  - **New context series (not a replacement):** RigLogix marketed utilization by class, as printed in Seadrill's 10-Q (as of 30 Sep 2026): benign floaters 87%, HE floaters 97%, HE jackups 95%. It is another source and definition, so it is shown beside the Westwood series and never mixed into it.
- **Leading-edge sample rule (fixed this run; closes checkpoint 18):**
  - Six months to the run date, firm term ≥ ~1 year, start within ~18 months.
  - Pure dayrate. Where only a value incl. mobilisation is known, an ex-mob estimate is used and tagged `[A]`.
  - Rates as signed; for the NCS, not the escalated fleet-status value (checkpoint 19).
  - Median, range and n. Where the sample is bimodal (NOC vs IOC work), the two groups are shown as well.
- **Method:** unchanged since 8 Oct (one asset-value convention for values, asset-implied rates and newbuild parity).
- **Westwood backlog dating:** start-of-month snapshots. Each edition restates the prior snapshot, so read changes within one edition only.
- **Oldest inputs:** Westwood leading-edge YTD via Riviera (15 Jun); Westwood monthly (Sep activity, published 25/27 Oct); Zacks RIG report (23 Oct, Aug data).
- **Not read `[?]`:** Petrodata weekly (dynamic tables); Westwood October dashboard (not out); Borr and SED Q3; per-rig dayrates for KOC/ADNOC Drilling and Beacon Pacific (not disclosed).
- **Tags:** `[F]` fact · `[E]` external forecast or secondary · `[A]` own assumption · `[?]` unknown. Fixture grades: A stated dayrate · B value ÷ days · C secondary estimate · D unknown.

## Conclusion

- **BBB changed for UDW drillships only (Bull 2027 and the stub). Everything else is kept.**
  - Drillship **Bull 2027 450 → 475** (range 430–475 → 450–500).
  - Drillship **stub rate 420 → 455**: the fixed six-month rule, mechanical, identical in all scenarios.
  - Drillship **Base 2027 stays at 420**; its range widens from 400–445 to 400–455.
  - Two secondary ranges widen, with the points kept: SE Asia jackups Base 2027 80–98 → **80–105**; Middle East jackups Base 2028 85–105 → **85–110**.
  - All other Bear, Base and Bull paths, MCU, mid-cycle values and asset values: **kept**.
- **Why drillship Base 2027 stays at $420k:**
  - The fixed sample gives **455 / 389–499 / n = 5**, but it is bimodal: NOC and Australia work at 389–406 (KG2, Skyros; n = 2) and US Gulf / SE Asia work at 455–499 (West Carina, Proteus, Conqueror; n = 3).
  - Weighting the two group medians by their count gives **~438 `[A]`, +4% vs 420**, below the 5% minimum change.
  - The balance points the other way for 2027: Base MCU 91% vs 93% today (an H1-2027 gap: Transocean UDW 22% uncommitted, Noble ~20% more contracted capacity in H2 2027 than in H1), backlog down six editions in a row (152.2 rig-years), and contracted drillships flat at 80.
  - Supply responds: six modern stacked drillships sit with one owner from ~1 Dec, and Keppel's RigCo is completing a 7G drillship on spec for 2027 delivery.
  - No new drillship term fixture since 4 Nov.
- **Why drillship Bull 2027 rises to $475k:** the Bull signpost "2027-start median > $450k" is crossed on the fixed rule (455). A Bull case at 95% MCU cannot sit below today's six-month leading edge, and the IOC prints are $465–499k.
- **Recalibration triggers:**
  - **Fired:**
    - Staleness (> 30 days).
    - A stranded unit reactivated against a contract: **Beacon Pacific** (CIMC-owned 6G HE semi; steel cut 2015, idle since build `[A]`), six firm wells for Serica in the UK from Q3 2027. It adds one HE semi to NW Europe supply from mid-2027. NCS HE paths are kept: it works in the UK, it is one unit, and NCS 2028 is ~83% covered. It is a Bear-side supply signpost for NCS 2028–29.
    - A Bull signpost crossed (drillship 2027 median): Bull 2027 raised, Base kept (above).
  - **Formally met, assessed as no point change:** NOC multi-year jackup awards. KOC gave ADNOC Drilling two jackups for 4 years from Q4 2027 (~$107k, B), and ONGC gave ADES two standard jackups for 3 years (~$54k, B, not high-spec). Both are secondary rows or outside the high-spec class.
  - **Not fired:**
    - Oil (11 Nov flags no rig change; this run agrees).
    - MCU (no new month).
    - Core term fixture > 10% from Base (no new core print).
    - Floater orders (none; the Keppel completion has no contract).
    - Ownership change at a covered contractor (Transocean–Valaris is known; it closes ~1 Dec).
    - War or force majeure (no Gulf rig suspension found).
- **Oil input:** the cut in Brent Base 2027 from 88 to 84 is not material for rigs. 2027 is mostly set by backlog (~70% covered). FIDs run on the long end and mid-cycle: mid-cycle 70 is unchanged, Dec-29 is 70.6, and Dec-31 onwards is flat or higher. Contractors report fixtures underwritten at $30–40 breakevens `[E]`. The oil Bear catalyst (a deal) is closer, and that matters more for rigs in 2028–29 than the −$4 in 2027.
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
- **Rig values:** unchanged (mid-cycle unchanged). Blackford Dolphin (1974 benign semi, $10m plus $15m contingent) is consistent with the benign-semi floor. Drillship and jackup transactions still imply 8–12% above Base mid-cycle (checkpoint 13).

## Interface — leading-edge dayrate, $k/day (point values; ranges below)

| Segment Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| UDW drillships | 455 / 455 / 455 | 380 / 420 / **475** | 375 / 455 / 500 | 360 / 470 / 540 | 320 / 360 / 420 |
| HE semis (NCS) | 430 / 430 / 430 | 410 / 425 / 445 | 400 / 450 / 500 | 380 / 470 / 540 | 350 / 400 / 460 |
| Benign semis | 350 / 350 / 350 | 310 / 340 / 370 | 290 / 355 / 405 | 280 / 365 / 430 | 260 / 300 / 340 |
| High-spec jackups | 105 / 105 / 105 | 92 / 105 / 118 | 88 / 115 / 135 | 85 / 120 / 145 | 92 / 110 / 130 |
| SE Asia jackups (secondary) | 90 / 90 / 90 | 72 / 90 / 98 | 70 / 95 / 108 | 70 / 98 / 115 | — / 92 / — |
| Tender-assist barges (secondary) | 80 / 80 / 80 | 68 / 78 / 88 | 65 / 82 / 95 | 65 / 85 / 100 | — / 80 / — |
| Middle East jackups (secondary, Base only) | 90 | 90 | 95 | 100 | 95 |

- **Stub** = six-month leading edge on the fixed sample rule, identical across scenarios.
- **Drillship stub (455) above Base 2027 (420):**
  - The six-month sample is led by US Gulf and SE Asia work (3 of 5 prints).
  - Base 2027 is the composite for all 2027 open days. Those include NOC work (~$390–405k) and an H1-2027 gap; MCU is 91% vs 93% today.
  - IAF prices open 2027 days at the regional reading where the rig's market is clear (Market check).
- **Low confidence (n < 3 term prints in six months):** benign semis, tender-assist, SE Asia and Middle East. SE Asia has two prints at $95–106k against a stub of 90 (checkpoint 22).

## Interface — MCU, % annual average

| Segment Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| UDW drillships | 93 / 93 / 93 | 88 / 91 / 95 | 86 / 95 / 97 | 83 / 94 / 97 | 82 / 88 / 92 |
| HE semis (NCS) `[A]` | 97 / 97 / 97 | 92 / 97 / 98 | 88 / 96 / 98 | 83 / 93 / 97 | 85 / 92 / 96 |
| Benign semis `[A]` | 76 / 76 / 76 | 73 / 79 / 84 | 69 / 82 / 88 | 67 / 82 / 89 | 68 / 78 / 85 |
| High-spec jackups | 88 / 88 / 88 | 84 / 89 / 92 | 82 / 91 / 94 | 81 / 91 / 95 | 82 / 88 / 92 |
| Middle East jackups (committed, Base only) `[E/A]` | ~90 | 90 | 91 | 92 | 90 |
| SE Asia jackups, tender-assist | `[?]` no series | | | | |

- Stubs are the latest observed month (Westwood, September, published 25/27 Oct):
  - drillships 80 / 86 = 93.0%;
  - jackups 384 / 438 = 87.7%;
  - semis 82% in aggregate, with HE and benign set at 97 and 76 `[A]`.
- The drillship stub is above Base 2027 (91%), consistent with an H1-2027 gap (Noble has ~20% more contracted capacity in H2 2027 than H1; Transocean's UDW fleet is 22% uncommitted for 2027).
- Cross-check (RigLogix via Seadrill 10-Q, 30 Sep):
  - HE floaters 97% (23 contracted), consistent with NCS HE 97%;
  - benign floaters 87% (107 contracted; drillships and semis together);
  - HE jackups 95% (27).
- Tender-assist (Westwood, 5 Nov): fleet utilization ~96%, heading for 100% by end-Q4 2026, excluding the cold-stacked T-9 and the newbuild Raiqa `[E]`. Not a series yet; it is context for checkpoint 17.

## Interface — asset values and anchors

| Segment | Newbuild / completion $m | Secondhand $m (age, date) | Reactivation $m, lead time | Value mid-cycle Bear / Base / Bull $m | Cash floor $k/d | Reactivation parity $k/d | Newbuild parity $k/d |
|---|---|---|---|---|---|---|---|
| UDW drillships | 850–1,000+ `[E]`; stranded 7G completion: Keppel/Seatrium package $390m for 4 units (not split) `[F]` | 300 (Deep Value Driller, 2014 7G, Feb-26) `[F]` | 85–150, 12–18 mo `[E]` | **67 / 208 / 404** (12-yr-old 7G) | 225 `[E]` | 390 (320–470) `[A]` | **~540–570** (convention); 650–720 `[E]` |
| HE semis (NCS) | `[?]` | 480 (Deepsea Bollsta, 2019, Nov-25, incl. $355m backlog) `[F]` | `[?]` (Beacon Pacific reactivation cost not disclosed) | **104 / 307 / 539** (7-yr-old) | 250 `[A]` | `[?]` | `[?]` |
| Benign semis | `[?]` | 10 + 15 contingent (Blackford Dolphin, 1974, to SPM, Oct-26) `[F]`; recycling 4–8 `[E]` | `[?]` | **10 / 10 / 132** (15-yr-old; Bear and Base at the floor) | 225 `[E]` | `[?]` | `[?]` |
| High-spec jackups | `[?]` | 72 each (5 Noble units to Borr, Jan-26); 57 each (5 Fontis units, Jul-26); 64 (Noble Resolve, closed Oct-26) `[F]` | 20–40, 6–12 mo `[E, older]` | **10 / 42 / 107** (12-yr-old; Bear at the floor) | 75 (55–90) `[A]` | 125 (95–140) `[A]` | `[?]` (newbuild price `[?]`) |
| Tender barges (secondary) | 113–135 (EDrill/T-series build cost) `[F, SED]` | ~28 each (Seadrill → Energy Drilling, 3 units incl. a semi-tender, Jun-23) `[F]` | `[?]` | **13 / 62 / 117** (15-yr-old; mid-cycle 67 / 80 / 95, MCU 65 / 80 / 90 `[A, SED]`) | 35 `[F, SED]` | `[?]` | `[?]` |

**Asset-value convention (since 8 Oct; one method for values, asset-implied rates and newbuild parity):**

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

- Margins are thin, so values are very sensitive to opex: ±$7.5k a day moves a 12-year-old jackup from $18m to $66m.
- Company analyses must source their own opex before departing from the segment parameters.

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
| **Blackford Dolphin → SPM, $10m + $15m contingent (agreed 26 Oct, closing ~5 Nov)** | 52 (beyond the 30-year life) | n/a (floor) | 300 (benign) | — | Consistent with the floor: $10m paid on delivery, $15m only on a first contract payment (India). The rig stays in the fleet |

- **Reading:** on the fully costed convention, 2025–26 buyers of drillships and jackups paid for through-life rates **8–12% above Base mid-cycle**, between Base and Bull. Old benign semis trade at the floor.
- **Mid-cycle rates are not changed.** The evidence is three competitive or exit sales plus one closing. The gap is carried as **open checkpoint 13** for the mid-cycle review with the long-run leading-edge series (checkpoint 10). Until then, IAF analyses show V_T at transaction-implied marks as a sensitivity.

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
| SE Asia jackups | Bear / **Base** / Bull | 72 (60–80) / **90 (80–105)** / 98 | 70 / **95 (85–105)** / 108 | 70 / **98 (88–108)** / 115 | Six-month term prints: NAGA 8 $95k (A, Chevron Malaysia, 547 days) and **Perseverance ~$106k incl. mob/demob (B, PHM Indonesia, 406 + 30 days, end-Dec 2026)**. Older: PV Drilling VI $97k (A), NAGA 2 ~$86k for 5 years (B). PTTEP–Foresight $60–70k (C, unconfirmed). n = 2 in six months, so the point is kept and the range widened (checkpoint 22). Bear = Gulf rigs relocate and Foresight-type pricing spreads |
| Tender-assist barges | Bear / **Base** / Bull | 68 (60–75) / **78 (70–88)** / 88 | 65 / **82 (72–92)** / 95 | 65 / **85 (75–95)** / 100 | SED contracts ($83k EDrill-2 for 5 years; older $94–121k); SED opex ~$37k a rig-day. T-16 Phase 7 (CPOC, 30 months from Q3 2027) ≈ $95k incl. mob (B), ~$89–92k ex-mob `[A]`; one print, not applied. Westwood (5 Nov): fleet utilization ~96% → 100%; four TARs above $120k, types not stated `[E]`. Semi-tenders ($127–160k, SED) are not covered. Jackups compete directly (PTTEP). Checkpoint 17 |
| Middle East jackups | **Base** | **90 (80–100)** | **95 (85–110)** | **100 (88–110)** | KJO: Arabian Drilling 4 rigs × 4 years ≈ $91k (B, Sep-26); Embracer $91.3k (A, 1,460 days from Mar 2027). **KOC: ADNOC Drilling 2 rigs × 4 years from Q4 2027, $313.6m maximum value incl. mobilisation ≈ $107k (B, upper bound)**. Aramco 3-year extensions for five ARO rigs (D). The Bear catalyst (war re-escalation) is in the scenario table; Bear/Bull figures are added when a company analysis needs them |

- **Contract cover per segment and year `[A]`.** Rig-by-rig cover is built for the main contractors in the appendix. The market proxy is Westwood backlog ÷ marketed rigs (1 Oct snapshot).
  - **Drillships:** 152.2 rig-years over 86 marketed = 1.77 years per rig, i.e. cover ~70% / 45% / 25% for 2027 / 2028 / 2029.
    - Transocean's active drillships are ~92% / 52% / 24% committed. Its UDW fleet incl. 3 stacked units is uncommitted 22% / 56% / 80% (10-Q, 2 Nov `[F]`).
    - Valaris: 3,152 contracted drillship days in 2027 ≈ 8.6 of 10 active rigs. Seadrill: > 85% of 2027 drillship days contracted. Noble: floaters 66% contracted in Q3.
  - **NCS HE semis:** ~96% / ~83% / ~50%. Transocean's NCS fleet is ~96 / 80 / 64% committed `[A]` (HE uncommitted 8 / 31 / 47% `[F]`). The market proxy for 2029 (50%) stays below Transocean's own NCS fleet.
  - **Semis aggregate:** 1.13 years per rig. **Benign semis:** ~65% / 40% / 20%.
  - **Jackups:** 1.57 years per rig, ~70% / 45% / 25%.
  - The Bear–Bull spread is narrowest in 2027 and widest in 2029 for every segment; the NCS spread is narrowest of all in 2027. The drillship 2027 spread widened with Bull (380–475) and is still the narrowest drillship year.
- **Base vs management guidance `[E]`:**
  - Transocean ("> 90% in 2027, approaching 100% by year-end"), Noble ("essentially fully contracted by late next year"; "inflection in fleet utilization … starting H2 2027") and Seadrill ("signs that point towards a market recovery in 2027") all sit above Base 2027 MCU (91%). Bull (95%) reflects the guidance case.
  - Base is lower because contracted drillships have been flat at 80 since July, backlog has fallen six editions in a row, and guidance assumes tenders convert.
  - On rates, Noble's Tier-1 leading edge ("mid-$400,000s to $500,000") matches the IOC tier and the six-month median (455). Base 2027 (420) also carries the NOC tier and the H1 gap.

## Market check

| Segment | MCU latest (month) | Leading-edge median / range / n (6 mo, term; fixed rule) | Trend 6–12 mo | Cover 2027 / 28 / 29 `[A]` | Base 2027 vs leading-edge |
|---|---|---|---|---|---|
| UDW drillships | **93% (Sep; 80 / 86)**; 90% Jun–Aug, 94% Mar–May. RigLogix benign floaters 87% (30 Sep) | **2027 starts: 455 / 389–499 / 5** (KG2 389, Skyros 406, West Carina ~455 ex-mob, Proteus 465, Conqueror 499). Groups: NOC and Australia 389–406 (n = 2); US Gulf and SE Asia 455–499 (n = 3); grouped reading ~438 `[A]`. 2028 starts: Noble Viking 460 (296 days, short of the term rule), West Polaris 438 (older). Noble Tier-1 range "mid-400s to 500" `[F, company]`. Short: Globetrotter I 400, DS-12 ~417, BlackHawk ~500. Westwood 2026 YTD (Jun): 6G/7G 388, 7G 407, 6G 371 | MCU up 3 pp on supply (−2 units; contracted flat at 80); backlog −12% since the 1 Apr snapshot (173.3, April edition → 152.2); working floaters 134 (Sep) → 137 (2 and 9 Nov); rates up for IOC / US Gulf work, NOC flat at ~$390k | ~70 / 45 / 25 (Transocean active ~92 / 52 / 24; Seadrill 2027 > 85%) | **420 vs 455 (−8%); vs grouped ~438 (−4%)** |
| HE semis (NCS) | `[?]` (Westwood semi aggregate 82%, Sep). RigLogix HE floaters 97% (30 Sep) | ~430 / 399–517 / 8 as signed (4 Nov sample less Hercules, which works in Canada; no new NCS rate print since. 2027 starts ~437: Endurance 402, GreatWhite ~432, Encourage 441, Barents 450; 2028 starts ~452: Scarabeo 8 430, Bergen ~472 incl. mob, Norge 517). Bergen signed 10 Nov (terms as the LOA); options ~$500k after FX and escalation (CEO, Q3 call `[E]`). Westwood Norway 2026 YTD 436 | Rates rising (+$50k y/y); fleet-status rates drift up with escalation and the NOK component (checkpoint 19) | ~96 / 83 / 50 | 425 vs ~437 for 2027 starts (−3%) |
| Benign semis | ~76% `[A]` (aggregate 82% incl. HE, Sep; counts 59 / 71 = 83%, flagged) | ~350 / 320–400 / term n < 3, low confidence. Westwood all-semi 2026 YTD < 340 (implies benign ~$300k if Norway is ~30% of fixtures `[A]`). Short: SSV Catarina 279 (Indonesia, 70 days). Hakuryu-5 ≤ ~280–300 all-in (C, 1977 unit, conditional) | MCU flat; backlog down; short work dominates; old units stay in the fleet (Blackford Dolphin to SPM, India) | ~65 / 40 / 20 | 340 vs ~300–350 |
| High-spec jackups | **88% (Sep; 384 / 438)**; 87% Jul–Aug, 86% Mar–Jun. RigLogix HE jackups 95% (30 Sep). Working 374–376 (Oct–9 Nov, Westwood weekly) | 4 Nov set: 126 / 91–167 / 8 (skewed to NW Europe/Australia). Added since: Embracer 91.3 (A, KJO), **KOC ~107 (B)**, **Perseverance ~106 (B)**; these pull the median towards ~115 `[A]`. Short: VALARIS 122 UK 125, VALARIS Norway ~135, 107 165, 106 ~111; Tenacious (Angola, priced 1-year option) ~142 (B). Westwood 2026 YTD excl. Norway/Australia (Jun): 94 | Firming slightly; contracted +2 in Sep; backlog −28 rig-years a month; Middle East and Africa working jackups down in October (Westwood commentary) | ~70 / 45 / 25 | 105 vs ~91–107 (benign regions) and ~115–167 (NW Europe/Australia) |

- **Jackup composite `[A]`:** Base $105k ≈ 80% benign regions at ~$96–100k + 20% NW Europe/Australia at ~$140k. Rigs in Mexico, West Africa, the Middle East and SE Asia should read ~$95–100k for 2027 (or their secondary row), not $105k. The composite is kept for global MCU and fleet-wide reads.
- **Westwood leading-edge** (via Riviera, 15 Jun 2026, YTD to mid-June; aggregate of RigLogix fixtures, treated as `[F]` for the database and `[E]` for the commentary):
  - Drillships: 6G $371k, 7G $407k, 6G/7G $388k (−7% vs 2025).
  - Semis: < $340k (−6%); Norway $436k (+$50k).
  - Jackups: ~$94k excl. Norway/Australia (−6% vs 2025, −24% vs 2024's $123k).
  - Westwood averages for reference: 2023 jackups $118k, semis $368k, drillships $419k.
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
| Brent Base **84** / 77 / 72 (2027 was 88), mid-cycle 70; long end Dec-27 77.6, Dec-28 72.8, Dec-29 70.6, Dec-30 69.1, Dec-31 67.7, Dec-34 64.2 | 2027 is ~70% covered, so the −$4 reaches rig demand mainly through 2027 exploration budgets, set in this budget season. That is small against $30–40 project breakevens `[E]` and NOC programmes that are not price-led. FIDs run on the long end and mid-cycle: Dec-29 ≈ mid-cycle 70, and Dec-31 onwards is flat or higher. **No rig change** (own check; it agrees with the oil baseline's "no action") |
| Bear 65 / 60 / 60 (durable Iran–USA deal plus OPEC+ market share; new enabler: Russia–Ukraine sanctions relief). Status: **closer** (strikes on hold since 9 Nov; talks) | Exploration and marginal deepwater FIDs (US Gulf independents, Namibia) are deferred with a 6–18 month lag, so the hit lands in 2028–29. This is the main oil risk for the floater paths |
| Bull 118 / 102 / 90 (renewed strikes with retaliation against Gulf energy infrastructure). Status: further away, tail live | Cash flow lifts floater demand with a 12–36 month lag. Operationally, Gulf jackups face suspension and evacuation again — **two separate lines** |
| Strategic restocking (~1 bn bbl), energy security | Supports NOC programmes (Aramco, ADNOC, KOC, KJO, Petronas, PTTEP gas, Equinor) |

**Operational geopolitics (status 12 Nov):**
- **Middle East jackups:**
  - **History:** working utilization fell from 83% to ~69% (Feb → late Apr) while committed held ~90% `[E, Westwood May]`. The Arabian Gulf is ~36% of global jackup supply `[E]`. The war suspensions of March 2026 were reversed by mid-August (ADES 11 Aug, Arabian Drilling 12 Aug, VALARIS 110 and 250, Borr) `[F]`. Precedent: a drone hit a KOC offshore drilling platform on 12 Jul `[F]`.
  - **Since the late-October escalation:** attacks are onshore and coastal, plus on ships. They include Dammam airport and Shaybah (21 Oct), the evacuation of Aramco's Dhahran HQ (22 Oct), a claimed Ras Tanura hit (27 Oct, unconfirmed), and Houthi missiles damaging the Aramco Tower in Riyadh (8 Nov, per Oil BBB). Ships were hit on 10 Nov. The IRGC declared Hormuz closed (~26 Oct).
  - **Not found `[?]` (searches 4 and 12 Nov):** any suspension, evacuation, down-manning or force majeure for a Gulf offshore rig, or a contractor notice. Valaris (2 Nov, primary): "All Valaris and ARO rigs operating in the Middle East remain under contract." Westwood says Middle East working jackups fell in October, without a count.
  - **Contract demand firm:** Aramco gave five ARO rigs 3-year extensions, KJO awarded 4-year terms, and KOC gave ADNOC Drilling 2 × 4 years.
  - **Reading:** the oil-price line has no rig effect. The operational line is high risk but has lost no rig-days so far. If rigs are suspended, committed MCU (the Middle East row basis) holds, as in March–April, while working utilization and contractor revenue fall at once.
- **Red Sea / Egypt / East Med:** Valaris DS-12 works for BP in Egypt to Apr 2027 (+60 days late 2027); Transocean Asgard is in the East Med to Dec 2027. Flag on escalation.
- Floaters outside the region are not affected operationally.

### Operator demand

- **Brazil (Westwood, 1 Nov):**
  - 47 rigs operating and 35 drilling, both flat vs 1 Oct: 25 drillships, 9 semis, 10 platform rigs and 3 jackups. Petrobras has 34.
  - Outstanding minimum requirements: 2027 **210** rig-days (360 on 1 Oct), 2028 **1,185** (1,035; 570 in tenders) and 2029 780. That is small against the fleet, and the 2028 rise is ~0.4 rig-years.
  - Petrobras concluded a $3.6bn cycle in March–April (Búzios, Mero, Renecon), with 6G long terms at $360–430k. Corcovado and Orion run to 2030 at $392k, and Aquila to Jun 2028 at $442k. Further Búzios drillship awards are pending `[?]`.
  - IOC work: Valaris DS-8 moves to Shell Brazil from Mar 2027 (~800 days), and DS-17 works for Equinor Brazil to Jan 2028.
  - Petrobras is ~20% of global deepwater demand, a concentration risk. Transocean expects Brazil to sustain 30–33 rigs over five years `[E]`.
- **India:** ONGC took KG2 Feb 2027–Feb 2029 at $389k (binding LOA), and Reliance has KG1 to Mar 2028 at $410k. ONGC also gave ADES two standard jackups (Key Singapore, Admarine 10) for 3 years from ~Q1 2027 at $117.2m incl. mobilisation ≈ **$54k** (B). These are standard units, outside the high-spec class.
- **NCS:**
  - Equinor's 7 rig-years are firm: Endurance returns from Australia in Q2 2027; Enabler and Encourage run from 2028 at $402k (escalated), with Encourage bridging at $441k from May 2027.
  - Transocean Barents (from Romania) works for Vår Jun 2027–Jun 2030 at $470k ($450k as signed).
  - **Hercules** (SFL, Odfjell-managed) leaves Norway for Canada for ≥ 400 days from Q1 2027 (correction: it is not NCS demand in 2027).
  - **Deepsea Bergen: Vår contract signed on 10 Nov** (LOA 10 Sep): 3 years from early 2028 plus four 1-year priced options to 2035; ~$472k incl. mobilisation (B). The CEO puts option economics near $500k after FX and escalation `[E]`.
  - Transocean Norge: Harbour Jan–Oct 2028 at $517k, priced options to Mar 2029, then Shell Mar–Jul 2029.
  - Spitsbergen is firm with Equinor to Dec 2027 ($519k from Apr 2027), then open. Deepsea Atlantic is firm to late Q4 2027, with two more priced wells and three ~1-year periods at rates to be agreed. Deepsea Nordkapp is firm to end-2028 (rate set at market by end-2026). Deepsea Aberdeen works for Equinor to Q1 2029. Noble GreatWhite works for Aker BP from Q2 2027 for 3 years (~$432k, B), and Scarabeo 8 for Aker BP from Jan 2028 (366 days, $430k).
  - **NCS HE availability:** booked through 2027 (~96%) and ~83% of 2028. Open rig-days in 2028: Spitsbergen (from Jan 2028) and Atlantic (after two priced wells), plus Scarabeo 8 from 2029. Transocean expects Norway HE utilization near 100% from 2028 `[E]`, and Odfjell calls most marketable Tier-1 HE rigs fully booked for 2027 `[E]`.
  - Jackups: Noble Interceptor drills a DNO well in Q3 2027, then 670 days of ConocoPhillips Ekofisk P&A. Noble Intrepid moves from BP UK ($150k to Sep 2027) to ORLEN (1 well, Q3 2027).
- **UK:**
  - **Beacon Pacific** (CIMC-owned 6G HE semi, managed by Odfjell): Serica, six firm wells from Q3 2027 (Bruce infill first, then possibly Kyla and Greater Laggan west of Shetland, and P&A), with options. Reactivation and transit from Asia have begun. The rate is not disclosed (D).
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
  - **KOC: ADNOC Drilling, two jackups for 4 years firm (incl. mobilisation) plus 1 option year, from Q4 2027, $313.6m maximum (KWD 96.6m) ≈ $107k (B, upper bound)**. One rig is ADNOC Drilling's own and one bareboat-chartered (source `[?]`). It is ADNOC Drilling's first offshore work outside the UAE, under an LOA subject to formalities.
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
  - Westwood restates earlier snapshots upwards as late awards are booked (1 Sep: jackups 687.8 → 725.8, semis 81.7 → 90.4, drillships 155.7 → 157.6). The semi restatement probably carries Equinor's 7 rig-years `[A]`.
  - Awards are not yet replacing burn. This is the main falsification signal against Base 2027–28. The next reading is the October edition (~27 Nov), which should include Proteus and Conqueror (~3.2 rig-years).

### Supply

- **Drillships** (Westwood, Sep): marketed 86 (80 contracted + 6 available), cold-stacked 9, total 95 (97 in Aug: two units left the fleet, names `[?]`).
  - No newbuild orders.
  - **Stranded completion (new):** Keppel RigCo will fund Seatrium to complete a 7G drillship for 2027 delivery "positioned for charters", with no contract `[F]`. It is a funded plan, so it is probable supply from 2027–28. It becomes competitive supply once contracted.
  - The stacked pool in Transocean–Valaris is six modern units, in one owner's hands from ~1 Dec. Reactivation costs $85–150m and takes 12–18 months, and none has been announced.
  - Ownership: Deep Value Driller passed to Eldorado ($300m), and Noble's Globetrotter II sale ($38m) is pending. Neither creates a rig.
  - Net effective change 2026 → 2029: Base 0 to +1 (Keppel); Bull +1–3 from 2028 (reactivations, Keppel); Bear −1–2 (older 6G retirements), with the Keppel unit uncontracted.
- **Semis** (Westwood, Sep): marketed 71 (59 + 12), cold-stacked 7, total 78 (80 in Aug).
  - Retirements: Valaris DPS-1 and MS-1, Noble Ocean Apex.
  - **Beacon Pacific (new):** a CIMC-owned 6G HE semi, steel cut at Yantai in 2015 and idle since build `[A]`, enters the NW Europe HE fleet from Q3 2027 against the Serica contract. That is +1 competitive HE semi in the UK. Whether it can later take NCS work (consent) is `[?]` (checkpoint 20).
  - Keppel's two mid-water HE semis for NW Europe: completion is "under assessment", so they are not supply yet (checkpoint 21).
  - Old units stay: Blackford Dolphin (1974) was sold to SPM for marketing in India, and Hakuryu-5 (1977) has a conditional Timor contract. That slows benign retirements.
  - Relocations: Hercules (Norway → Canada, Q1 2027 start; correction 12 Nov), Endurance (Australia → NCS, Q2 2027), Barents (Romania → NCS, Jun 2027), Deepsea Mira (→ Trinidad, Apr 2027). No global change. Net NCS HE semi count 2027 vs 2026: −1 + 2 = +1.
  - Net effective change by 2029: benign −1 to −3 (Base); NW Europe HE +1.
  - Counts: the reported 82% does not reconcile with 59 / 71 = 83.1%; the gap is flagged, not corrected.
- **Jackups** (Westwood, Sep): marketed 438 (384 + 54), cold-stacked 51, total 489.
  - Ownership: Borr bought 5 from Noble (Jan) and 5 Fontis units in a 50/50 JV (Jul). Noble Resolve went to Ocean Oilfield (now Ocean MVM, Tunisia work). VALARIS 111 was sold for MOPU conversion and leaves the fleet. Valaris has three benign units stacked (148, 147, 143) plus VALARIS Viking (HE). Seven units are leased to ARO.
  - Loss: Borr's Prospector 5 (2014 JU-2000E) sank off Gabon on 24 Oct: −1 high-spec unit, ~0.2 pp of MCU.
  - **Stranded completion (new):** Keppel's N-class HE jackup (500-ft class) for 2028 delivery, no contract.
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
| Middle East jackups | Committed ~90%; no suspension found to 12 Nov; ME working jackups down in Oct (Westwood) | KJO ~$91k (B, Arabian ×4) and $91.3k (A, Embracer); **KOC ~$107k (B, 2 × 4 years from Q4 2027)**; Aramco 5 × 3-year extensions (D) | Contract demand firm; operational risk high | Low price / very high geopolitical | Medium |
| SE Asia floaters | Rising (Seadrill: "increasing activity in Southeast Asia") | West Carina ~$477k incl. mob (B); West Capella options ~$442k (B); Noble Viking $460k (2028) | Up | Low–medium (NOC) | Medium |
| Timor Sea benign semis | Hakuryu-5 for Finder KTJ from Dec 2027 (conditional on FID 30 Nov) | ≤ ~$280–300k all-in (C, upper bound) | Small-operator work | Medium | Low |
| SE Asia jackups | `[?]` | **Perseverance ~$106k incl. mob (B)**; NAGA 8 $95k (A); NAGA 2 ~$86k (B); Foresight $60–70k (C) | Mixed: PHM/Chevron firm, PTTEP aggressive | Low–medium (NOC gas) | Low–medium |
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
| 2027-start drillship term fixtures (fixed rule) | < $380k / > $450k (median) | **455 / 389–499 / 5; Bull threshold crossed** (no new print since 4 Nov) | ~$420k (13 Oct sample) / 455–465 (strict) | Towards Bull; Bull 2027 raised |
| 2028-start drillship term fixtures | < $400k / > $500k; Base cut test < $440k | No new print; Noble Viking $460k (short), West Polaris $438k (older); 2027-start terms running through 2028 at $465–499k | Same | Neutral, firm |
| Westwood drillship backlog (rig-years) | < 150 / two rises in a row | 152.2 (1 Oct); 6 falls in a row; next ~27 Nov | Same | Towards Bear (not crossed) |
| NCS HE availability | Open rig-days in 2028 / fully booked 2029 | 2027 ~96%; 2028 ~83% (Bergen signed 10 Nov); open in 2028: Spitsbergen, Atlantic beyond two priced wells | Same | Towards Bull |
| NW Europe HE supply (new) | A stranded HE unit gets NCS work, or a second one is completed / — | Beacon Pacific to the UK (Serica, Q3 2027); Keppel's two mid-water HE semis "under assessment" | — | Towards Bear (supply), not crossed |
| Petrobras | Further deferrals / Búzios awards | No new awards; Brazil count flat (47 / 35); 2028 outstanding rig-days 1,035 → 1,185 | No awards | Neutral |
| West Africa FIDs | Venus FID slips to 2027+ / Venus FID taken | Not taken; fiscal talks open (15 Oct); deadline "before 2027" | Not taken | Towards Bear (deadline near) |
| Saudi / Gulf jackups | Renewed suspensions / Aramco recalls 6–9 rigs | No suspension found (12 Nov). Contract demand firm: Aramco 5 × 3-year extensions, KJO 4-year terms, **KOC 2 × 4 years** (Q4 2027). Onshore attacks continue (Aramco Tower, 8 Nov) | No suspension; Aramco, KJO | **Mixed:** contracts towards Bull; operational risk towards Bear |
| APAC jackup / tender pricing | Confirmed term fixtures < $80k / > $100k | **Perseverance ~$106k incl. mob (B)**; NAGA 8 $95k; Foresight $60–70k (C, unconfirmed); T-16 barge ~$95k (B); Westwood: four TARs > $120k, fleet ~96% (5 Nov) | Foresight; $86–97k; T-16 | Towards Bull for Indonesia and tender-assist; PTTEP jackups still towards Bear |
| Reactivations | ≥ 2 cold-stacked drillships reactivated without long contracts / none | None for drillships. HE semi: Beacon Pacific reactivated **against a contract** (trigger, assessed) | None | Neutral (drillships) |
| Stranded completions (new) | A stranded floater delivered without a contract / delivered against a term contract | Keppel 7G drillship (2027) and N-class HE jackup (2028) being completed with no contract | — | Towards Bear (supply), not crossed |
| Retirements | — / ≥ 2 floaters retired a quarter | Q3: drillship fleet 97 → 95, semis 80 → 78 (MS-1, Sagar Vijay, others `[?]`). Q4 so far: none found; Blackford Dolphin stays marketed (SPM) | Crossed (Q3) | Q3 crossed; Q4 open |
| Newbuild orders | Any floater order / none | None | None | Towards Bull (supply) |

**Open checkpoints** (closed this run: 6 and 18; earlier closures are in the change log):

1. **PTTEP/Foresight actual rates:** carried. Still unconfirmed; three secondary sources say $60–70k (C). Reflected in the SE Asia and tender-assist Bear.
2. **Gulf operations:** carried. Re-assess the Middle East row (Bear) on any of these:
   - a suspension, evacuation or force majeure notice for a Gulf offshore rig (Aramco, QatarEnergy, ADNOC, KOC/KJO);
   - an attack on an offshore installation or support base;
   - a Westwood weekly with working jackups down ≥ 5 and the Middle East cited (March precedent: −13 in a month).
   - Status 12 Nov: none of the three is met. Next reads: Westwood weeklies, Borr Q3 (~18 Nov), and ADES and Arabian Drilling releases.
3. **Transocean–Valaris closing:** carried. Shareholder votes 24 Nov, court 26 Nov, closing ~1 Dec. Close this checkpoint on the completion 8-K, then count the combined stacked pool as one owner's.
4. **2H26 FIDs and budgets:** carried. Venus FID is not taken (deadline "before 2027"); Mopane FID 2028; Westwood's 30 FIDs outstanding; Finder KTJ FID by 30 Nov (Hakuryu-5).
5b. **Westwood October dashboard (~27 Nov):** test drillship MCU (Base 2027 91%; today 93%) and backlog (Bear signpost < 150; Proteus and Conqueror should add ~3.2 rig-years). Re-run early if MCU is outside 90–96% or backlog is < 150.
8. **Noble Faye Kozack (Ghana) rate:** carried, low priority (D).
10. **Long-run leading-edge series per segment** (2010–2026, with and without the 2014 peak and the 2016–2021 trough): carried. Partial: Westwood averages for 2023 (jackups $118k, semis $368k, drillships $419k), 2024 (jackups $123k), 2025 (implied: drillships ~$417k, jackups ~$100k) and 2026 YTD.
11. **Jackup and HE semi newbuild prices, HE semi reactivation cost, NCS opex:** carried, all `[?]`. New partial: Keppel's remaining completion cost for four stranded units is ~$390m in total (not split). Beacon Pacific's reactivation cost is not disclosed. Cross-check: Transocean 2026 O&M $2.33–2.40bn ÷ 27 rigs ≈ $236–244k a rig-day `[B]`.
12. **+9 marketed jackups in August:** carried, low priority. The September fleet was flat at 438.
13. **Mid-cycle vs transaction-implied rates:** carried. Drillships ~$394k and jackups ~$119–123k, 8–12% above Base mid-cycle; Westwood's 2023–26 drillship averages ($388–419k) sit at or above Base mid-cycle ($360k) without trough years. Odfjell's price implies ~$413k through-life on its own economics (+3% vs HE Base mid-cycle). Globetrotter II (~$298k) is not comparable. Blackford Dolphin is at the floor (benign). Review with checkpoint 10.
14. **Benign-semi rate path:** carried. Westwood's all-semi 2026 YTD implies benign ~$300k `[A]` vs Base 2027 $340k. Low prints so far are old or short units (Hakuryu-5, SSV Catarina), and old units now stay in the fleet (Blackford Dolphin). No term benign fixture in the Q3 reports. Cut Base 2027 to ~$310–320k if a term benign fixture for a high-spec unit prints ≤ $320k.
15. **Jackup composite weighting** (80/20 benign vs NW Europe/Australia `[A]`): carried. RigLogix HE jackup MCU 95% (Seadrill 10-Q) supports the NW Europe premium.
17. **Tender-assist row vs T-16:** carried.
    - **Rule:** if a second SE Asia tender-barge term fixture for a 2027–28 start prints ≥ ~$86k at grade A/B, raise Base 2027–28 by at least 5% and widen the 2027 range (top 88). If instead the next EDrill-1 / T-15 awards come in at ≤ $80k, T-16 stands as a client-specific outlier.
    - **New evidence (Westwood, 5 Nov `[E]`):** fleet utilization ~96%, heading for 100% by end-Q4; four TARs "securing" > $120k, types not stated. Semi-tenders are not covered by the row, so this is not a barge fixture.
    - Next read: SED Q3 (18 Nov).
19. **NOK and escalation drift in NCS fleet-status rates:** carried. Compare leading-edge on rates as signed; IAF uses current USD values for booked days. Odfjell's CEO puts Bergen's option economics near $500k after FX and escalation.
20. **New: Beacon Pacific.** Rate, reactivation cost and NCS consent `[?]`. Watch:
    - the Serica term length (six wells ≈ 1 year `[A]`) and the options;
    - whether the rig bids for NCS work in 2028–29 (Bear supply for NCS HE).
    - Sources: Odfjell or CIMC disclosures, and Westwood.
21. **New: Keppel stranded completions.**
    - The 7G drillship (2027) and N-class HE jackup (2028): contract or charter status.
    - The two mid-water HE semis: completion decision.
    - A 7G drillship delivered without work is a Bear supply signpost. One delivered against a term contract at ≥ $450k is Bull pricing evidence.
22. **New: SE Asia jackup point and Borr Q3 (~18 Nov).** Two six-month term prints at $95–106k vs Base 2027 $90k. **Rule:** if a third grade A/B term print ≥ $95k appears (Borr Q3, Velesto, ADES), raise SE Asia Base 2027–28 by ≥ 5%. Also read Borr's contract cover and average dayrates, and its Gulf, Mexico and West Africa statements, for the jackup row.
23. **New: KOC per-rig rate.** $313.6m is a maximum value incl. mobilisation for two rigs. Read the per-rig dayrate when ADNOC Drilling or the Kuwaiti gazette publishes it, and test the Middle East 2028 Base (95).

## For IAF

- **What changed:** UDW drillships Bull 2027 450 → 475 and the drillship stub 420 → 455. No IAF analysis uses the drillship row today. Every row read by an existing analysis (HE NCS, jackups, SE Asia, Middle East, tender-assist) keeps its points, MCU, mid-cycle and asset values. **No re-run is needed for rig reasons.**
- **Odfjell (`docs/odl-analysis.md`): HE semis (NCS) row.**
  - Unchanged: Base 425 / 450 / 470 at 97 / 96 / 93%, mid-cycle 400 at 92%, a 7-year-old HE semi worth $307m at Base.
  - The Bergen signing (10 Nov) confirms backlog already counted (~$472k incl. mob from 2028, +5% vs Base 2028). Norge ($517k) and Barents ($470k) remain the comparables.
  - Nordkapp 2028 and Atlantic's open 2028 days stay at Base 2028 ($450k) until set. The Nordkapp rate is set by two brokers by end-2026.
  - Beacon Pacific earns Odfjell management fees only: a company item, not a market row.
- **Borr (`docs/borr-analysis.md`, on hold):** jackup, SE Asia and Middle East rows, by rig location.
  - Points are unchanged: composite 105 / 115 / 120; SE Asia 90 / 95 / 98 (2027 range now 80–105); Middle East 90 / 95 / 100 (2028 range now 85–110). A 12-year-old jackup is worth $42m at Base.
  - Rigs in Mexico, West Africa, the Middle East and SE Asia read ~$95–100k for 2027, not the $105k composite.
  - New regional prints (KOC ~$107k, Perseverance ~$106k) are mildly positive for Borr's Gulf and Asia re-lets. The fleet's ~$134k average still marks negative on rolling contracts.
  - No Gulf suspension. Borr Q3 (~18 Nov) is checkpoint 22.
- **SED (`docs/SED-analysis.md`): tender-assist row.**
  - Unchanged: Base 78 / 82 / 85, Bear 68 / 65 / 65, Bull 88 / 95 / 100, mid-cycle 80. A 15-year-old barge is worth $62m at Base.
  - Westwood's 5 Nov reading (utilization ~96% → 100%, four TARs above $120k) is Bull-side evidence, but it is not a barge fixture. SED Q3 (18 Nov) applies checkpoint 17.
- **Transocean, Valaris, Noble, Seadrill (no IAF analysis):** UDW drillships row.
  - Price open 2027 days at the regional reading: NOC, Brazil and India ~$390–405k; US Gulf, IOC West Africa and SE Asia ~$455–500k. The global Base ($420k) is for rigs without a clear market.
  - Mid-cycle Base is $360k, and a 12-year-old 7G is worth $208m on the convention.
  - Stacked units: Keppel's speculative 7G completion and the six-unit stacked pool cap the Bull case from 2028.
- **Method (since 8 Oct):** V_T, NAV_0 and market marks use the asset-value convention (values-by-age table or the same formula). Transaction-implied marks (+8–12% on rate) are a sensitivity (checkpoint 13).

## For downstream skills

**Full update 12 Nov.** The values that moved are UDW drillships Bull 2027 (450 → 475) and the drillship stub (420 → 455), plus two secondary ranges (SE Asia Base 2027 80–105, Middle East Base 2028 85–110; points kept). Against the recalibration trigger (10% on a rate, 3 pp on MCU): Bull 2027 +5.6% and the stub +8.3%, both below it; no MCU moved. No reader reads a value that moved materially: no Base or Bear path, MCU, mid-cycle or asset value moved, the stub is a mechanical re-mark, and a range is not a point. **`affects` = none.** Each reader takes the notes below at its own next run.

| Reader | What it reads here | Touched? | What to take in at its next run |
|---|---|---|---|
| **supply** | Rig activity for OSV demand: NCS, UK, Brazil, Guyana/Suriname (working rigs, rig-years, moored semis vs DP drillships, P&A rigs, Petrobras plan) | No (no action now) | **UK:** +1 HE semi from Q3 2027, Beacon Pacific (Serica, six firm wells, options incl. P&A). Supply flagged it from Seabreeze; it is now confirmed from the Odfjell and Serica releases. It is likely moored like its sister Deepsea Yantai `[A]`, so it needs AHTS for rig moves. **NCS:** Bergen's signing is a continuation, and Endurance (Q2 2027) and Barents (Jun 2027) were already noted. **Correction:** Hercules (SFL, Odfjell-managed) leaves Norway for Canada (≥ 400 days from Q1 2027, announced Mar 2026); earlier rig notes tagged its Suncor work as NCS. Net NCS HE semis 2027 vs 2026: −1 + 2 = +1. **Brazil (1 Nov):** 47 operating / 35 drilling, flat; outstanding rig-days 2027 210 (360), 2028 1,185 (1,035), 2029 780; Petrobras plan unchanged. **Guyana/Suriname:** DS-18 with Petronas to May 2027, then to the US Gulf for Occidental (−1 drillship in Suriname from mid-2027). Drillship rate changes do not change OSV demand |
| **hy** | Oil Service row: drillship Base and Bear, NCS HE | No | Base unchanged: drillships 420 / 455 / 470 at 91 / 95 / 94%; NCS HE 425 / 450 / 470. Bear unchanged: 380 / 375 / 360 at 88 / 86 / 83%. Bull 2027 475 is not read there. Text note: HY's Oil Service paragraph quotes the drillship Bear as "400 → 360k"; the Bear 2027 point has been 380 since 10 Oct |
| **odl** | HE semis (NCS) row: rates, MCU, mid-cycle, asset convention, fixtures | No | Row unchanged. Bergen signed 10 Nov (terms as LOA; options ~$500k per the CEO `[E]`). Beacon Pacific is a managed rig (fees), UK. RigLogix HE floater MCU 97% |
| **sed** | Tender-assist row, rig values | No | Row unchanged. Westwood (5 Nov): TAR utilization ~96% → 100%, four TARs > $120k (types `[?]`). Checkpoint 17 rule at SED Q3 (18 Nov) |
| **borr** (on hold) | Jackup rates, MCU, rig values; SE Asia and Middle East rows | No | Points unchanged; ranges widened. New prints: KOC ~$107k (B, 2 × 4 years from Q4 2027), Perseverance ~$106k (B, Indonesia), Tenacious ~$142k (B, Angola option). Keppel N-class HE jackup (2028, spec). Checkpoint 22 at Borr Q3 |

## Change log

- **12 Nov 2026 — full update (re-baseline; skill 2026-10-10.1; new baseline date 12 Nov):**
  - **Inputs read:**
    - Oil Market BBB 11 Nov (full update).
    - Westwood weekly counts for 26 Oct, 2 Nov and 9 Nov, with the October month commentary. Westwood dashboard: still the October edition (Sep activity). Westwood Brazil count of 1 Nov.
    - Transocean (fleet status 2 Nov, 10-Q 3 Nov; no 8-K since), Valaris (10-Q 3 Nov; no 8-K since), Noble (8-K of 4 Nov is a management item only) and Seadrill (10-Q 4 Nov, with a RigLogix utilization table).
    - Odfjell: Q3 (3 Nov), Beacon Pacific (2 Nov) and the Deepsea Bergen signing (10 Nov). Serica (2 Nov) and Offshore mag (3 Nov) for Beacon Pacific.
    - Borr 6-Ks to 2 Nov (no contract news since 30 Sep). ADES: Perseverance and Tenacious (3 Nov) and ONGC (9–11 Nov). ADNOC Drilling / KOC (9–10 Nov). Velesto NAGA 3 (4 Nov). Ocean MVM Tunisia (Nov).
    - Keppel RigCo / Seatrium completion deal (26–28 Oct). Dolphin Drilling's Blackford Dolphin sale (26 Oct). Westwood on tender-assist rigs (5 Nov). Venus status (15 Oct). Transocean–Valaris timetable. Zacks RIG report (23 Oct).
  - **Oil input:** Base Brent 2027 88 → 84. 2028–29 (77 / 72), mid-cycle (60 / 70 / 82), Bear and Bull are unchanged. The long end fell to 2030 (Dec-28 77.4 → 72.8, Dec-29 73.5 → 70.6, Dec-30 70.7 → 69.1) and is flat or higher from 2031. **Judged not material for rigs** (own check, agreeing with the oil agent): 2027 is ~70% covered, FIDs use the long end and mid-cycle, and Dec-29 ≈ mid-cycle 70. No own oil view.
  - **Changed (previous → new):**
    - UDW drillships **Bull 2027 450 (430–475) → 475 (450–500)**. Bull 3-year average 497 → 505.
    - UDW drillships **stub rate 420 → 455** (all scenarios).
    - UDW drillships Base 2027 range 400–445 → **400–455** (point 420 kept).
    - SE Asia jackups Base 2027 range 80–98 → **80–105** (point 90 kept).
    - Middle East jackups Base 2028 range 85–105 → **85–110** (point 95 kept).
    - **Reasons:**
      - Checkpoint 18 is closed with a fixed sample rule (Metadata). 2027-start term fixtures in the six months to 12 Nov: KG2 389 (A), Skyros 406 (A), West Carina ~455 ex-mob (B / `[A]`), Proteus 465 (A), Conqueror 499 (A). That gives **455 / 389–499 / n = 5**.
      - The stub is the six-month leading edge by rule, so it moves to 455.
      - Bull: its signpost (median > $450k) is crossed, and a Bull at 95% MCU must sit above today's leading edge.
      - Base: the grouped reading (~438 `[A]`, +4%) is below the 5% minimum. The 2027 balance (MCU 91% vs 93% now, H1-2027 gap, backlog −6 editions) and the supply response (six modern stacked units, Keppel 7G on spec) do not support a rise without a new print.
      - Secondary ranges: the new prints sit above the old range tops. Perseverance ~$106k incl. mob/demob (B, PHM Indonesia, 406 + 30 days, from end-Dec 2026). KOC ~$107k (B, maximum value incl. mobilisation, 2 × 4 years from Q4 2027). The points are kept: n < 3 term prints in six months on each row, and checkpoint 1 (Foresight $60–70k) is unresolved.
    - Size against the recalibration trigger (10% on a rate, 3 pp on MCU): Bull 2027 +5.6%, stub +8.3%, ranges only on the secondary rows. Nothing moved beyond the trigger.
    - Sources: Transocean fleet status 2 Nov; Seadrill and Noble Q3 releases; ADES and ADNOC Drilling releases via OE Digital / World Oil; Westwood weekly.
  - **Unchanged (tested):**
    - **UDW drillships:** Base 2027 420 / 91%, Base 2028 455 / 95%, Base 2029 470 / 94%, Bear 380 / 375 / 360, Bull 2028–29 500 / 540, mid-cycle 320 / 360 / 420, MCU stub 93.
      - The 2028 cut test from 4 Nov (cut if a 2028-start term fixture prints < $440k or backlog < 150) is **not met**: no new 2028-start print, and the latest backlog is 152.2.
    - **NCS HE semis:** all paths. Bergen's signing (10 Nov) converts the September LOA with the same terms. The CEO puts option economics near $500k after FX and escalation `[E]`. Beacon Pacific goes to the UK, not the NCS. RigLogix HE floater MCU is 97% (30 Sep), consistent with Base 2027 97%. Cover is 96 / 83 / 50.
    - **Benign semis:** all paths (checkpoint 14 carried). No benign term fixture was found. Blackford Dolphin (1974) was sold for $10m + $15m contingent and is marketed in India by SPM, so it stays in the fleet.
    - **High-spec jackups:** all paths. The new benign-region prints ($106–107k, B) sit at the composite (105), and the NW Europe premium holds (RigLogix HE jackup MCU 95%).
    - **Tender-assist row:** kept (checkpoint 17). Westwood (5 Nov) reports fleet utilization of ~96%, heading for 100% by end-Q4, and four TARs above $120k a day. The types are not stated; semi-tenders are not covered by the row. That is not a named barge fixture, so the change rule is not met. SED Q3 (18 Nov) decides.
    - **Middle East and SE Asia points**, all MCU paths, contract cover, mid-cycle rates and asset values.
  - **Recalibration triggers checked:**
    - **Fired:**
      - Staleness.
      - Stranded unit reactivated against a contract: Beacon Pacific, Serica UK, six wells from Q3 2027. Assessed: +1 NW Europe HE semi from mid-2027; NCS paths kept; new checkpoint 20.
      - Bull signpost crossed: drillship 2027-start median 455 > 450. Bull 2027 changed.
    - **Formally met, no point change:** NOC multi-year awards (KOC 2 × 4 years; ONGC 2 × 3 years standard jackups; Aramco 5 × 3-year extensions from the 4 Nov run). They add cover, not rigs: ADNOC Drilling uses one own rig and one bareboat-chartered rig `[F]`.
    - **Not fired:**
      - Oil (11 Nov "no action" for rig; own check agrees).
      - MCU > 3 pp (no new monthly).
      - Core term fixture > 10% (no new core print since 4 Nov).
      - ≥ 2 floater orders (none). Keppel's completion of a 7G drillship and an N-class HE jackup is speculative (no contract), so it is logged as supply.
      - M&A at a covered contractor (Transocean–Valaris already logged; shareholder votes 24 Nov, court 26 Nov, close ~1 Dec).
      - War or force majeure (no Gulf rig suspension found; Westwood says Middle East working jackups fell in October, with no count given).
  - **New supply items:**
    - Keppel RigCo will fund the completion of four stranded rigs at Seatrium (~S$500m / $390m in total; not split by rig): a 7G drillship for 2027 delivery and an N-class HE jackup for 2028, both "positioned for charters" (no contract). Two mid-water HE semis for NW Europe are still "under assessment".
    - Beacon Pacific (above).
    - Dolphin Drilling: Blackford Dolphin sold to SPM (closing ~5 Nov), with management by Dolphin and marketing in India. This is an ownership change, not a new rig.
  - **Data correction:** Hercules (SFL-owned, Odfjell-managed HE semi) works in **Canada** from Q1 2027 (≥ 400 days, ~$170m ≈ $425k, B; SFL release Mar 2026), not on the NCS. It was tagged NCS in the fixture log and the NCS sample since 4 Oct. Without it the NCS 2027-start median is ~437 (n = 4), so Base 2027 (425) is −3%, inside the minimum. Net NCS HE semis 2027 vs 2026: −1 (Hercules) + 2 (Endurance, Barents) = +1.
  - **Layout:** the body now carries current values only. The dated small-update narratives (13 Oct–4 Nov) were removed from Metadata, Conclusion, Drivers and For IAF; each stays in its own change-log entry below. The day-by-day Gulf log is condensed to its status. The rig-by-rig appendix was rebuilt from the Q3 fleet status reports.
  - **Checkpoints:**
    - Closed: 6 (Q3 fleet status reports; Borr moves to checkpoint 22) and 18 (sample rule).
    - Carried: 1, 2, 3, 4, 5b, 8, 10, 11, 12, 13, 14, 15, 17 and 19.
    - New: 20 (Beacon Pacific), 21 (Keppel stranded completions), 22 (SE Asia jackup point and Borr Q3) and 23 (KOC per-rig rate).
  - **Forecast vs actual:** no realised window year. For 2026 (reference), Westwood drillship MCU was 90–94% from January to September vs its late-2025 forecast of 94%.
  - **Weights:** 25/50/25 kept as a convention.
  - **IAF:** no existing analysis reads a changed value. Odfjell (HE NCS), Borr (jackups, SE Asia and Middle East points), SED (tender-assist) and HY (drillship Base and Bear) are unchanged. See "For downstream skills".
  - **Input assessed:**
    - The brief's "11 Nov formal signing" of Deepsea Bergen: Odfjell's release is dated **10 Nov** (Newsweb, 06:06 UTC). The terms are as in the September LOA.
    - The oil agent's "not material for rigs": verified against the rig rules.
    - Supply BBB's Beacon Pacific flag (Seabreeze): verified from the Odfjell and Serica releases and now taken in.
  - **New dated events:**
    - Transocean and Valaris shareholder votes on 24 Nov; Bermuda court on 26 Nov.
    - Venus FID ("before 2027") by 31 Dec.
    - Finder KTJ FID (Hakuryu-5) on 30 Nov.
    - Beacon Pacific starts for Serica in Q3 2027.
    - KOC jackups (ADNOC Drilling) start in Q4 2027.
    - Keppel 7G drillship delivery in 2027.
    - Contractor Q4 fleet status reports in mid-Feb 2027.
    - SED Q3 on 18 Nov should also name rig (checkpoint 17).
  - **Baseline date:** 12 Nov 2026. Stale after 12 Dec 2026.

- **4 Nov 2026 — small update (orchestrator request after the Q3 reports; skill 2026-10-10.1; UDW drillships 2027 changed, everything else kept):**
  - **Inputs read:**
    - Transocean fleet status and 8-K (2 Nov) and 10-Q (3 Nov).
    - Valaris Q3 release and fleet status (2 Nov).
    - Noble Q3 release (26 Oct) and 10-Q (27 Oct).
    - Seadrill Q3 release (3 Nov).
    - Westwood dashboard, October edition (Sep activity; published 25 Oct, updated 27 Oct).
    - Borr 6-Ks (26 Oct–2 Nov).
    - `docs/odl-analysis.md` v2 (4 Nov; Odfjell Q3 of 3 Nov).
    - Oil Market BBB 31 Oct.
  - **Not read `[?]`:** the Westwood weekly counts of 26 Oct and 2 Nov (not posted on Westwood's page as of 4 Nov), the Seadrill fleet status PDF (the release was used), and Borr Q3 (~18 Nov).
  - **Oil input:** Oil Market BBB 31 Oct (Final, stale after 7 Nov). Paths and mid-cycle are unchanged, and it says "no change" for rigs. No own oil view.
  - **Recalibration triggers checked:**
    - **Fired — core term fixture > 10% from Base (UDW drillships, 2027 starts):**
      - Deepwater Proteus: US Gulf, 10 wells, Feb 2027–Jan 2029, **$465k** (A; +16% vs Base 2027 $400k).
      - Deepwater Conqueror: US Gulf, 5 wells, Aug 2027–Nov 2028, **$499k** (A; +25%).
      - Both are new in Transocean's fleet status of 2 Nov.
    - **Signposts:**
      - Bull "2027-start median > $450k": crossed on the strict six-month window (~$455–465k, n = 5); not crossed on the 13 Oct sample (~$420k, n = 7).
      - Bull supply signpost "≥ 2 floaters retired a quarter": crossed (Q3: Sagar Vijay, MS-1 and two more drillships plus one semi out of Westwood's fleet; names `[?]`).
    - **Formally met, assessed as no change:**
      - Middle East operator awards: Aramco gave 3-year extensions to five ARO rigs, and KJO took Embracer for 4 years at $91.3k. These are continuations that add cover, not rigs, and sit on the Middle East row at Base (90).
      - Embracer is −13% vs the jackup composite ($105k) but +1% on its own (Middle East) row, as with KJO in September.
      - NCS: Barents $470k (FSR) is +10.6% vs Base 2027, but it was signed in April at ~$450k (+6%). The rise is escalation and the NOK component, and it is ~+3% vs the term-weighted Base (~$456k over Jun 2027–Jun 2030). It is not a new print.
      - Norge Harbour 2028 is $517k (+15% vs Base 2028), but it is a ~9-month contract from 2025 already in the 2028-start median, which is unchanged (~$452k).
      - Spitsbergen Apr–Dec 2027 at $519k is a priced extension (~8 months), not a term fixture.
    - **Not fired:**
      - MCU > 3 pp: drillships +3 pp on rounding (90 → 93) and +2.1 pp on counts (90.9 → 93.0); jackups +1; semis 0.
      - ≥ 2 floater orders or a reactivation: none.
      - Gulf war or force majeure: no suspension found (Valaris 2 Nov: all its own and ARO's Middle East rigs remain under contract).
      - Oil baseline flags a rig change: no.
  - **Changed, UDW drillships 2027:**
    - Base rate **400 → 420** (range 385–420 → 400–445).
    - Bull rate **430 → 450** (410–450 → 430–475).
    - Stub rate 400 → 420 (all scenarios; six-month 2027-start median).
    - Stub MCU 90 → 93 (latest observed month, mechanical).
    - 3-year averages: Base 442 → 448; Bull 490 → 497.
    - **Reason (several independent data points, ≥ the 5% minimum):**
      - Two A-grade Transocean US Gulf fixtures ($465k, $499k).
      - Noble's Tier-1 leading edge "mid-$400,000s to $500,000" on ~44 months of new floater backlog (26 Oct).
      - Seadrill West Carina (~$477k, B; in the median since 13 Oct).
      - Westwood drillship MCU 93% (Sep).
      - Valaris: "day rates are moving higher".
      - 2027-start term median 406 → **420** on the 13 Oct sample (n = 7; +5.0% vs Base). The strict six-month window gives ~$455–465k (n = 5).
    - **Why not more:**
      - Backlog fell for a sixth month: 152.2 rig-years on 1 Oct (−5.4 within the edition).
      - Contracted drillships have been flat at 80 since July, and the MCU rise comes from two units leaving the fleet.
      - NOC term work prices at ~$390k: KG2 $389k (A; Westwood had $395k) and Petrobras $392k.
      - The minimum the evidence supports is applied, and the sample question is left to the full update (checkpoint 18).
    - **Kept:** Base 2027 MCU 91% (89–93). One month, supply-driven; ~78 of 86 contracted implies an H1-2027 gap, consistent with Noble's H1/H2 profile. Bear 2027 (380, 88%) is also kept, as are all of 2028–29 and mid-cycle.
    - **Previous → new, Base 2027 vs leading-edge:** 400 vs 406 (−1.5%) → 420 vs 420.
    - Sources: Transocean fleet status (2 Nov) and 10-Q (3 Nov); Noble Q3 release (26 Oct); Valaris Q3 release (2 Nov); Westwood dashboard, October edition.
  - **Changed, high-spec jackups:** stub MCU 87 → 88 (latest observed, mechanical; 384 / 438 = 87.7%). Paths are unchanged.
  - **Unchanged (tested):**
    - **NCS HE semis:**
      - 2027-start median ~$430k vs Base $425k; 2028-start median ~$452k vs Base $450k.
      - Equinor package $402k (A, escalated); Barents $470k (A; $450k as signed); Norge $517k (A); Spitsbergen $519k (short).
      - Cover 2028 ~80% → ~83% `[A]` (Nordkapp firm to end-2028). Transocean HE uncommitted 8 / 31 / 47%; its NCS fleet is ~96 / 80 / 64% committed `[A]`.
      - Transocean HE average daily revenue Q3 $504.3k (backlog average, not leading-edge).
    - **Benign semis:** semi MCU 82% (flat; counts give 83.1%, flagged); SSV Catarina $279k (short). Checkpoint 14 carried.
    - **High-spec jackups:** MCU 88% (+1); backlog 697.3 (1 Oct, −28.4). Valaris short NW Europe work at $125–135k; Valaris jackup backlog average 2027 $130k. The composite is kept.
    - **Secondary rows** (SE Asia, tender-assist, Middle East), mid-cycle rates and asset values: unchanged.
  - **New market-check row:** Noble Globetrotter II, $38m (closing Q4-26). It implies ~$298k on the convention, −17% vs Base mid-cycle. It is not comparable (non-Tier-1 unit, impaired seller).
  - **Data corrections:**
    - The Transocean–Valaris stacked drillship pool is 6 modern units (Ocean Rig Apollo, Athena, Mylos; VALARIS DS-11, DS-13, DS-14), not "9, mostly 6G".
    - VALARIS 111 was sold for MOPU conversion, not recycling.
    - Westwood restated the 1 Sep backlog upwards (jackups 687.8 → 725.8; semis 81.7 → 90.4; drillships 155.7 → 157.6).
    - KG2 is $389k (Transocean fleet status), not $395k.
    - Corcovado is $392k (A), not ~$385k (B).
    - The Norge conflict is resolved at $517k (checkpoint 9 closed).
  - **Ownership:** Transocean–Valaris has all approvals and closes on or about 1 Dec 2026 (Valaris, 2 Nov). Noble Resolve closed 9 Oct, and the Globetrotter II sale is pending.
  - **Checkpoints:**
    - Closed: 5 (September dashboard) and 9 (Norge rate).
    - Updated: 2, 3, 6 (Base 2028 cut condition met on its wording but overridden; new test set), 8, 12, 13, 14 and 17.
    - New: 18 (drillship 2027 regional split and sample rule) and 19 (NOK and escalation drift in NCS fleet-status rates).
  - **User and agent input assessed:** the orchestrator's list of prints (from the Odfjell update) was verified against the primary filings. Barents $470k, Norge $517k, Spitsbergen $519k, the Equinor package $402k, HE uncommitted 8 / 31 / 47%, HE Q3 average daily revenue $504k, the 1 Dec close and Valaris Q3 adjusted EBITDA $151m (incl. ~$24m of Middle East impact) all match. One caveat: Barents was signed at ~$450k (Apr 2026), and $470k is the escalated fleet-status value.
  - **Weights:** 25/50/25 kept as a convention.
  - **IAF:** no existing analysis uses the drillship row. Odfjell, Borr, SED and Paratus: no change (see For IAF).
  - **Supply BBB:** no material change; the NCS rig-count note adds Barents from Jun 2027.
  - **HY BBB (Oil Service row):** its text quotes drillships at $400k / 91% for 2027, which is now $420k / 91%. The direction is mildly positive for drillers; no FTD change is implied.
  - **New dated events:**
    - Transocean–Valaris closing ~1 Dec 2026.
    - Deepsea Nordkapp 2028 rate set by end-2026.
    - Barents mobilisation Feb–Jun 2027 and Vår start Jun 2027.
    - Proteus US Gulf term from Feb 2027; Conqueror US Gulf term from Aug 2027.
    - Westwood dashboard (Oct activity) ~late Nov.
    - Borr Q3 and SED Q3 ~18 Nov.
    - Noble Globetrotter II sale closing Q4 2026.
  - **Baseline date:** stays 10 Oct 2026, with paths changed on 4 Nov (drillships 2027). Stale after 9 Nov 2026 (unchanged). A full update is due because a trigger fired; run it after the Oil BBB follow-up of 7 Nov.

- **28 Oct 2026 — small update (orchestrator request: Westwood weekly of 26 Oct and the T-16 award of 27 Oct; skill 2026-10-10.1; Rig Market BBB kept unchanged):**
  - **Oil input:** Oil Market BBB 24 Oct is still the latest (Final, stale after 23 Nov). No new read; no own oil view.
  - **Westwood weekly of 26 Oct:** **not published** on Westwood's weekly page as of 28 Oct (latest week 43, 19 Oct: 376 jackups / 135 floaters). A search found no press coverage of it. Held `[?]`; it is not evidence of an unchanged count.
  - **Gulf status since 24 Oct (substitute):**
    - No offshore rig suspension, evacuation, force majeure or contractor notice found.
    - New: 26 Oct Houthi claims on the East-West pumping stations and Riyadh airport (unconfirmed). 27 Oct claimed Ras Tanura refinery and terminal hit; a fire near the terminal was contained (Bloomberg source), not confirmed by Saudi Arabia, no output effect `[E]`.
    - Checkpoint 2 triggers: not met.
  - **New fixture: T-16 Phase 7** (Energy Drilling / SED; 2013 tender barge; CPOC, Malaysia–Thailand JDA). Letter of award on 27 Oct 07:00 (MFN, primary): 30 months firm from early Q3 2027, up to 15 months of options, ~USD 87m firm including an undisclosed mobilisation fee. No dayrate is stated.
    - **Rate:** 87 ÷ ~915 days ≈ **$95.1k** (B). If mobilisation is $3–6m, the ex-mob figure is ~$89–92k `[A]`.
    - **Same rig, same client:** Phase 6 at $131k (firm to Dec 2026; campaign ends Q1 2027) re-prices to ~$95k (−27%). Between the phases the rig is demobilised to Singapore with reduced crew for ~5 months `[F]`. Over the gap plus the firm term the contractor earns ~$82k per calendar day.
    - **Physical meaning:** +2.5 rig-years of firm tender-assist demand from mid-2027. It is a continuation of an existing campaign, so the net demand change is ~0 beyond the gap. SED's 2027 firm cover rises from 44% to 52% (SED analysis).
  - **Skill thresholds checked (tender-assist row):**
    - Against Base: +22% vs Base 2027 (78) and +15% vs the term-weighted Base (Jul 2027–Jan 2030: 78 / 82 / 85 ≈ $82.5k). Ex-mob +14–18% vs 78 and +8–11% vs the term-weighted Base. It is above the 2027 range (70–88), at about the term-weighted Bull (~$96k).
    - Recalibration trigger "term fixture > 10% from Base": defined for **core segments**, and tender-assist is a **secondary row**, so **not fired**. Applied by analogy it would exceed 10% on the headline, but the evidence threshold is not met. It is one fixture (n = 1 term print in six months, so low confidence and a range, not a point). It is grade B with mobilisation included, from an incumbent rig in campaign continuity, and it came with an idle gap the contractor accepted.
    - Plausibility (> 15% from the last comparable fixture: EDrill-2 $83k, +15%; T-16 Phase 6 $131k, −27%): the value is confirmed in the primary release, so it is held as B, not `[?]`.
    - **Decision: tender-assist row kept** (2027 / 2028 / 2029 Base 78 / 82 / 85, ranges, Bear, Bull and stub 80 unchanged). Open checkpoint 17 sets the rule for a change.
  - **Other SE Asia tender-assist fixtures since 10 Oct:** none found. Older items, not in the six-month window or not covered by the row: Vantris (ex-Sapura) Sapura Esperanza (PCSB assignment) and Sapura Jaya (Vestigo), semi-tenders, Q3 2026 starts, 4–5 Aug 2026, rates not disclosed (D); Sapura T-17 / T-18 for PTTEP, 5 years from Q2 2026 (awarded Feb 2025).
  - **Other item:** Borr Prospector 5 (2014 JU-2000E) sank off Gabon on 24 Oct (punch-through during preload; five personnel unaccounted for on 25 Oct). That is −1 marketed high-spec jackup, ~0.2 pp of MCU: no change.
  - **Signposts:** "Saudi / UAE jackups" not crossed (re-read 28 Oct). "APAC jackup / tender pricing" now carries T-16 inside the $80–100k band.
  - **Unchanged (tested):** all paths, scenarios, stub, MCU, contract cover, mid-cycle rates and asset values. No row moved.
  - **Weights:** 25/50/25 kept as a convention. **IAF:** no change (SED already has T-16 as a company contract; Borr has Prospector 5). **Supply BBB:** no change (no covered region). **HY BBB (Oil Service row):** no change.
  - **New dated events:** T-16 Phase 6 ends Q1 2027 and Phase 7 starts early Q3 2027. Westwood weekly 26 Oct / 2 Nov (pending). SED Q3 on 18 Nov (EDrill-1 / T-15 follow-on awards; checkpoint 17). Borr's Prospector 5 investigation and its Q3 (date not announced).
  - **Baseline date:** stays 10 Oct 2026; stale after 9 Nov 2026.

- **24 Oct 2026 — small update (Gulf escalation since 22 Oct; orchestrator request; skill 2026-10-10.1; Rig Market BBB kept unchanged):**
  - **Oil input:** Oil Market BBB 24 Oct (Final, stale after 23 Nov).
    - Brent paths and mid-cycle are unchanged (Base 88 / 77 / 72, mid-cycle 70). The front rose to 116.72 (M1−M4 +12.95): a near-term risk premium, not lost barrels.
    - Long end: Dec-27 86.7, Dec-28 78.8, Dec-29 74.8.
    - Its "For downstream skills" says no change for rigs. **Oil-driven demand is not a channel**; no own oil view is taken.
  - **Gulf operational line, new since 22 Oct (facts):**
    - 21 Oct: Dammam airport attack. A drone aimed at an Aramco facility at Shaybah (onshore) was intercepted, and the energy ministry reports 2 killed. The US ordered non-emergency staff out of Saudi Arabia.
    - 22 Oct: Aramco evacuated its Dhahran HQ; cause and duration unknown.
    - 20–21 Oct: UKMTO tanker strikes off Al Faw and Bukha (Jubail on 16 Oct, by small boat).
  - **Claims:** Houthi strikes on Yanbu, Riyadh and Abha; IRGC seven-tanker claim (unverified).
  - **Not found `[?]`:**
    - No offshore rig suspension, evacuation, down-manning, force majeure or contract suspension (Aramco, QatarEnergy, ADNOC, KOC, KJO, Iranian side).
    - No contractor notice (Borr, ADES/Shelf, Valaris/ARO, Noble, Arabian Drilling).
    - No change in offshore war-risk insurance.
  - **Correction (older facts found this run):**
    - The war-suspended Saudi offshore rigs had all resumed by mid-August (ADES 11 Aug; Arabian Drilling 12 Aug, offshore utilization 100% by end-Q3 expected).
    - VALARIS 110 (Qatar) resumed in late May.
    - The "Aramco recalls `[?]`" reading therefore applies only to the 2024 demand-driven suspensions.
    - Precedent: a KOC offshore drilling platform was hit by a drone on 12 Jul.
  - **Skill thresholds checked:**
    - Gulf-jackup Bear catalyst / signpost "Gulf rigs suspended again": **not reached**.
    - Trigger "a war or force majeure puts a region's rigs offhire or suspended": **not fired**.
    - Trigger "oil baseline flags a rig-relevant change": **not fired**.
    - MCU and fixture triggers: no new data. Westwood weekly 19 Oct: 376 jackups / 135 floaters (+3 / +1), pre-escalation.
    - Signpost "Saudi / UAE jackups" re-read: **Mixed** (contracts towards Bull; operational risk towards Bear). Checkpoint 2 now names measurable re-assessment triggers.
  - **Other item:** Noble Resolve (CJ50 HE jackup) has passed to Ocean Oilfield (Abu Dhabi) for $64m (agreed Dec 2025; closed, rig in Malta 13 Oct). It is an ownership change, not a new rig. It implies ~$122k on the convention (+11% vs Base mid-cycle; added to the market check, checkpoint 13). No value change.
  - **Unchanged (tested):** all paths, scenarios, stub, MCU, contract cover, mid-cycle rates and asset values; the Middle East secondary row (Base only) and its catalyst text. No row moved.
  - **Weights:** 25/50/25 kept as a convention. **IAF:** no change (Borr: no suspension notice; see For IAF). **Supply BBB:** no change. **HY BBB (Oil Service row):** no change.
  - **Baseline date:** stays 10 Oct 2026; stale after 9 Nov 2026.

- **22 Oct 2026 — small update (user link: OE Digital, 20 Oct; skill 2026-10-10.1; Rig Market BBB kept unchanged):**
  - **New fixture (conditional):** Hakuryu-5 (ENEOS Drilling, ex-Japan Drilling; 1977 moored semi, max ~500 m water depth) for Finder Energy's KTJ development, Timor-Leste (PSC 19-11). Terms:
    - 3 firm wells from 1 Dec 2027 (window to 15 Mar 2028), ~150 days, minimum 140 days, plus 2 option wells.
    - Estimated gross JV cost $42.3m, "dependent on actual duration and contractual rates" (OE Digital). The basis is unclear, probably including mobilisation and spread costs.
    - It is conditional: ENEOS approvals by 16 Nov 2026; joint venture, government and Finder board approvals by 31 Dec 2026; FID targeted 30 Nov 2026.
    - Checked against Finder's release (via energy-pedia, 19 Oct). The value figure is only in the trade press (OE Digital, Offshore mag).
  - **Rate:** $42.3m ÷ 150 days ≈ $282k (÷ 140 ≈ $302k) all-in, so the dayrate is at most that (C, upper bound). It is not a leading-edge print for the benign row: a 49-year-old mid-water unit is not comparable to the high-spec benign fixtures ($375–400k). It points the same way as checkpoint 14 (benign ~$300k), but one old-spec, conditional fixture is not evidence for a change.
  - **Physical meaning:** ~0.4 rig-years of demand, mostly H1 2028, if FID is taken. That is < 1 pp of benign-semi MCU. Supply: a 1977 unit staying in the marketed fleet weakens the retirement story slightly, but it is one unit.
  - **Tested against Base:** no change to the benign-semi paths, MCU or catalysts. Small positive for the Bull signpost "Asia FIDs convert", if the 30 Nov FID happens.
  - **Other checks:** the Westwood dashboard still shows the August-activity edition (25/30 Sep); September data are not out. Transocean reports Q3 and its fleet status on 2 Nov (checkpoint 6). No recalibration trigger fired.
  - **User input assessed:** the OE Digital article (20 Oct) is a secondary summary of Finder's ASX release of 15/19 Oct. Its terms match the release and Offshore mag. The $42.3m is a cost estimate, not a contract value, so it is graded C.
  - **Weights:** 25/50/25 kept as a convention. **IAF:** no change. **Supply BBB:** not a covered region (Timor-Leste); no change.
  - **Baseline date:** stays 10 Oct 2026; stale after 9 Nov 2026.

- **17 Oct 2026 — small update (user link: Splash247, 16 Oct; skill 2026-10-10.1; Rig Market BBB kept unchanged):**
  - **New fixture:** Deepsea Atlantic (Odfjell, 2009 6G HE semi, DP, NCS): Equinor exercised two priced well options, firm end-Q2 2027 → late Q4 2027, at original contract pricing (D). Verified against Odfjell's release of 16 Oct (primary).
  - **Physical meaning:** +~0.45 rig-years of firm NCS HE demand in H2 2027 and no change in supply. NCS HE 2027 cover ~95% → ~96% `[A]`, below the 2 pp minimum. Base 2027 MCU of 97% is confirmed, not changed.
  - **Rate:** not a leading-edge print. The options were priced in 2023/2025: the Jan 2025 extension implies ~$464k (B) and the 2023 23-month contract ~$414k (B, older). The six-month NCS median ($430k) is unchanged.
  - **Tested against Base:** consistent. Equinor is converting priced NCS options, so the Bear signpost (open 2028 rig-days) does not move. Atlantic's 2028 is open beyond two priced wells and re-prices at market.
  - **Other checks this run:**
    - Westwood weekly 12 Oct: working jackups 373 (−1), floaters 134 (flat). Within noise.
    - No new Westwood dashboard: the August-activity edition (25/30 Sep) is still the latest.
    - Oil Market BBB 17 Oct: Brent Base 2027 85 → 88; long end Dec-27 86.7, Dec-28 78.0, Dec-29 ~73.8; mid-cycle and Bear/Bull unchanged. FID and tender logic runs on the long end and mid-cycle, so there is no rig change. Oil reference updated; the Bull catalyst (US strikes after 3 Nov) is closer, so the Gulf jackup operational line stays the main Bear risk for jackups.
  - **Not done this run (no trigger):** full re-research of all segments. The Q3 fleet status reports and the September dashboard (late Oct) are still pending, so checkpoints 5 and 6 are carried.
  - **User input assessed:** the Splash247 article is a secondary summary of Odfjell's release. Its facts match the primary source, and the rate is not disclosed in either. Offshore Energy (16 Oct) adds the 106-day off-hire after the April BOP drop.
  - **Weights:** 25/50/25 kept as a convention. **IAF:** no change. **Supply BBB:** no change in NCS rig count; the Viking Avant PSV extension is noted for it.
  - **Baseline date:** stays 10 Oct 2026; stale after 9 Nov 2026.

- **13 Oct 2026 — small update (user links: three Splash247 articles, read via Edge; paths unchanged):**
  - **New fixtures:**
    - West Carina (7G, Indonesia, H1 2027, 880 days, $420m incl. mob ≈ $477k, B).
    - West Capella options (~$342k priced, ~$442k unpriced at market; PTTEP to Feb 2028).
    - Sonangol Libongos (Angola, to Jan 2030); Sevan Louisiana (Kosmos, 25 days); DS-18 next goes to Occidental for 914 days.
  - **Recalibration trigger assessed** (core term fixture > 10% from Base): West Carina is +19% vs Base 2027 ($400k), or ~+13% ex-mob `[A]`. The 2027-start median moves ~$400k → ~$406k (n = 5), +1.5%, below the 5% minimum change. **UDW drillship paths kept.**
  - Direction: SE Asia floater demand is firming. It is the first Bull-side 2027 print and partly offsets the falling backlog, so the 2027 cut stands but is not extended to 2028.
  - Seadrill > 85% of 2027 drillship days contracted `[E]`, consistent with the cover proxy (~70% market, Transocean 81%).
  - **Norge:** Splash247 gives Harbour 2028 at $513k (current term $472k); checkpoint 9 reopened, $497k kept.
  - Transocean and Valaris articles: no new facts beyond the primary releases already used.
  - **IAF:** no change. Supply BBB: no change (Angola and SE Asia only).

- **10 Oct 2026 — update (skill 2026-10-08.2; user request with two links):**
  - **Changed, UDW drillships 2027:**
    - Base rate 425 → **400**, MCU 93 → **91**.
    - Bear 400 → 380 (MCU 89 → 88). Bull 450 → 430 (MCU 95 kept).
    - Bear 2028 385 → 375 (path shape after the lower 2027 start).
    - Stub 406 → 400 (six-month median, mechanical).
    - 3-year averages: Base 450 → 442; Bear 382 → 372; Bull 497 → 490.
    - Reason, several independent data points: 2027-start term fixtures median ~$400k (n = 4); Westwood 2026 leading-edge 7G $407k, 6G $371k (−7% y/y); MCU flat at 90% (Jun–Aug); drillship backlog down five editions in a row (−10%, Bear signpost crossed); working floaters 138 → 134 in September.
    - Sources: Westwood dashboard (25/30 Sep), Westwood weekly (5 Oct), Westwood via Riviera (15 Jun), fixture log.
    - Affects new analyses of Transocean, Valaris, Noble and Seadrill; no existing IAF document.
  - **Unchanged (tested):**
    - NCS HE semis: Equinor firm; Norway $436k YTD; Norge $497k (Harbour) and ~$517k (Shell, B). Supports Base 2028 at $450k; 2028 cover 75% → 80%.
    - Benign semis: Westwood-implied ~$300k is a single derived point, so it is carried as checkpoint 14.
    - High-spec jackups: the composite is explained (80/20 weighting `[A]`), with a regional reading for IAF.
    - Secondary rows, mid-cycle rates and asset values: no change.
  - **Data corrections:**
    - Westwood backlog figures are start-of-month snapshots: 687.8 / 81.7 / 155.7 is 1 Sep, not "August". Westwood restates the prior snapshot between editions.
    - The Norge rate conflict is resolved at $497k.
  - **Closed checkpoints:** 7 (Equinor approval), 9 (Norge rate), 16 (Nordnet link, read via Edge). **New:** 14 (benign-semi rate), 15 (jackup composite weighting).
  - **User input assessed:**
    - Drilling Contractor (9 Oct): used, verified against Transocean's 8-K of 9 Oct (primary); adds the Norge–Shell fixture and the Equinor approval.
    - Nordnet (TDN Finans, 7 Oct): a secondary summary of Valaris's 7 Oct release, which was already used from the primary PDF. All figures match; no change.
  - **Forecast vs actual:** no realised window year yet. For 2026 (reference), Westwood drillship MCU of 90–94% (Jan–Aug) remains below its late-2025 forecast of 94%, and Westwood's 2026 leading-edge is −6 to −7% y/y for every class except Norway semis.
  - **Weights:** 25/50/25 kept as a convention.
  - **IAF:** Borr should check the regional jackup reading (see For IAF). Supply BBB: no material change. Oil: no change needed.
  - **New baseline date:** 10 Oct 2026.

- **8 Oct 2026 — method revision (skill 2026-10-08.2); no path change:**
  - **Asset values harmonised** on one fully costed convention: rig-level free cash flow after idle cost (40% of opex), maintenance capex, revenue efficiency and tax, before G&A and financing; 30 years, 8%, $10m floor.
  - Mid-cycle values (Bear / Base / Bull, $m), previous → new:
    - 12-year-old 7G drillship 270 / 400 / 610 → **67 / 208 / 404**.
    - 7-year-old HE semi 320 / 520 / 760 → **104 / 307 / 539**.
    - 15-year-old benign semi 75 / 185 / 305 → **10 / 10 / 132**.
    - 12-year-old jackup 48 / 105 / 175 → **10 / 42 / 107**.
    - New: tender barge row 13 / 62 / 117 (15-year-old).
  - Asset-implied rates restated: Deep Value Driller ~$325k → ~$394k; Noble jackups ~$100k → ~$123k; Fontis ~$94–99k → ~$119k. Drillship newbuild parity ~$465–490k → ~$540–570k.
  - Added: parameter table with sources, values by age, sensitivities (opex ±10%, 35-year life), and a transaction market check.
  - Reason: Borr (gross method) and SED (fully costed) used different value methods on the same baseline, and the gross method overstated values 2–2.5x at Base mid-cycle.
  - Sources: Transocean 2026 capex guidance ($150m); Borr Q2 2026 (economic utilisation, capex guidance, cash tax, Odin opex); SED (tender opex and tax).
  - Unchanged: all rate and MCU paths, mid-cycle rates, cash floors, reactivation parity, catalysts and signposts.
  - **IAF:** Borr must re-run; Paratus should update the seller-credit collateral reading; SED re-run optional (see For IAF).

- **4 Oct 2026 — update and migration** (the entries below belong to this baseline):
- **Method:**
  - Migrated to skill revision 2026-10-04.3: English, new structure.
  - Probability matrix and indicator score removed; weights are a convention only.
  - Stub, ranges, mid-cycle, asset values and anchors added.
  - Secondary rows added: Middle East jackups, SE Asia jackups, tender-assist (requested by the SED analysis).
- **Changed:** benign-semi MCU −3 pp in all scenarios and years:
  - Bear 76 / 72 / 70 → 73 / 69 / 67.
  - Base 82 / 85 / 85 → 79 / 82 / 82.
  - Bull 87 / 91 / 92 → 84 / 88 / 89.
  - Reason: Westwood semi MCU 84% → 82% (Aug), semi backlog 88.4 → 81.7 rig-years, marketed available 11 → 13. With NCS HE near full, implied benign MCU is ~79% → ~76% `[A]`.
  - Source: Westwood dashboard 25 Sep. Affects Noble, Transocean (benign semis) and benign APAC units.
- **Unchanged (evidence within the minimum change):**
  - **UDW drillships:** 2027-start fixtures median ~$400k vs Base $425k. That is −6% of evidence, above the 5% minimum, but the n = 4 sample is NOC long-term (term discount) and short programmes price higher (Conqueror ~$471k/day of value). Held, flagged as under pressure: if Q3 fleet status reports show no 2027 term fixture ≥ $425k, cut 2027 to ~$405k next run.
  - **HE semis (NCS):** confirmed by the 2027-start median ~$420k and the 2028-start median ~$452k.
  - **High-spec jackups:** six-month median $106k vs Base 2027 $105k.
- **Data corrections:**
  - The August dashboard was available at the previous run.
  - Backlog figures restated: July 712.2 / 88.4 / 160.5; August 687.8 / 81.7 / 155.7.
  - Jackup MCU now reconciles; the July "47 available" was probably the source's or our misreading.
- **Forecast vs actual (2026, outside the window; reference only):**
  - Westwood (late 2025) forecast 2026 drillship MCU 94% → actual 90–94% (Jan–Aug).
  - Semis 88% → actual 78–86%.
  - Middle East jackups 96% → revised to 89–91% (war).
  - The miss on the downside again calls for caution on management and agency forecasts.
- **Weights:** 25/50/25 kept as a convention.
- **IAF:** SED should update (new tender-assist row). Other driller analyses: no existing IAF documents.
- **New baseline date:** 4 Oct 2026.

---

## Appendix

### Fixture log (selection; term fixtures from Apr 2026 plus key earlier ones)

| Rig | Class | Region | Operator | Start | Term | Rate $k/day | Grade | Source |
|---|---|---|---|---|---|---|---|---|
| Dhirubhai Deepwater KG2 | DS | India | ONGC | Jan 2027 | 730 days | 395 | A | Westwood dashboard (Aug data, 25 Sep) |
| Deepwater Conqueror | 7G DS | Equatorial Guinea | undisclosed | 2027 | ~170 days, 2 wells | ~471 (value $80m ÷ 170 days, excl. mob) | B, short | Transocean PR 15 Sep |
| Deepwater Asgard | 7G DS | East Med | — | 4Q26 | — | 405 | C | Deepwater Insight 18 Apr |
| Deepwater Atlas | 8G DS (20k psi) | US Gulf | BP | Jun 2028 | — | 635 (excluded: not comparable) | C | Deepwater Insight 18 Apr |
| Noble Viking | 7G DS | Brunei | Petronas Carigali | Jan 2028 | 296 days | 460 | A | Westwood; Noble Jul |
| Seadrill West Polaris | UDW DS | Brazil | Petrobras | Feb 2028 | 1,095 days | 438 | A | Westwood; DC |
| Valaris DS-4 | DS | Brazil | Petrobras | Nov 2027 | 1,064 days | ~420 ($447m) | B | World Oil 6 Apr |
| Deepwater Corcovado | DS | Brazil | Petrobras | Sep 2027 | 1,156 days | ~385 ($445m) | B | World Oil 14 Apr |
| Deepwater Skyros | DS | Australia | Chevron | Mar 2027 | 320 days | 406 | A | Westwood |
| Valaris DS-7 | 7G DS | Angola | Azule | Oct 2026 | 325 days | 385 | A | Westwood |
| Foresea ODN I | UDW DS | Brazil | Petrobras | early 2027 | 1,443 days | ~322 ($465m) | B | World Oil 25 Mar |
| Deepsea Bergen (ex-Bollsta) | HE semi | NCS | Vår Energi | early 2028 | 3 years | ~473 ($518m incl. mob) | B | OE Digital 10 Sep |
| Transocean Norge | 6G HE semi | NCS | Harbour | Jan 2028 | 5 wells + 3 options | 497 (Hartl: 513) | A (conflict) | Westwood; Transocean 8-K |
| Enabler / Encourage / Endurance | HE semi (Cat D) | NCS | Equinor (conditional) | Q2 2027 / Q1 2028 | 7 rig-years | 399 base, > 400 effective | A | Transocean 30 Jun |
| Scarabeo 8 | HE semi | NCS | Aker BP | Jan 2028 | 366 days | 430 | A | Westwood |
| Odfjell Hercules | HE semi (2008; SFL-owned, Odfjell-managed) | **Canada** (correction 12 Nov: not NCS) | Suncor (Westwood); undisclosed (SFL) | Q1 2027 | 400 days minimum | 425 (SFL: ~$170m ÷ 400 days ≈ 425, B) | A | Westwood; SFL release Mar 2026 (via OE Digital, Baird) |
| Transocean Encourage | HE semi | NCS | Equinor | Mar 2027 | 365 days | 416 | A | Westwood |
| Noble GreatWhite | HE semi | NCS | Aker BP | Q2 2027 | 3 years | ~430 | B | DC Mar |
| Deepsea Mira | 7G HE semi | Trinidad | Shell | Apr 2027 | ~150 days | ~467 ($70m incl. mob/demob); option ~427 | B, short | Splash247 (date `[?]`, Sep/Oct) |
| Noble Developer | 6G semi | Trinidad | BP | 2026/27 | 240 days | 375 | A | Westwood |
| Transocean Equinox | 6G semi | Australia | Santos | Q2 2027 | 90 days + 5 options | ~400 | B, short | Transocean 8-K |
| Noble Claus Bachmann | 6G semi | UK | BP | Mar 2027 | 150–210 days | ~320 | C | Hartl |
| Borgland Dolphin | semi | Spain | Repsol | Apr 2027 | 90 days | — | D | Westwood (Aug) |
| Arabian Drilling × 4 | jackups | Saudi/Kuwait (KJO) | KJO | end Q4 2026 | 4 years | ~91 (SAR 2bn ÷ 5,840 rig-days) | B | DC 28 Sep |
| Valaris 248 | HE jackup | UK | NEO NEXT+ | Apr 2027 | 1,080 days (41-well P&A) | ~130 ($140m) | B | Westwood; Valaris FSR 5 Aug |
| Valaris 123 | jackup | Poland | — | — | 1 well + option | 135 | A | Valaris FSR 5 Aug |
| Valaris 122 | jackup | UK | INEOS | Sep 2026 | 162 days | 115 | A | Valaris FSR |
| Valaris 107 | jackup | Australia | Golden Beach | Oct 2026 | 150 days | 163 | A | Valaris FSR |
| ADES Main Pass IV | jackup | Nigeria | Belbop | Jul 2026 | 365 days | 132 | A | Westwood |
| Velesto NAGA 2 | jackup | Malaysia | PCSB | Feb 2026 | ~5 years | ~86 ($157m) | B | Velesto / Bursa |
| Velesto NAGA 8 | jackup | Malaysia | Chevron (Hess) | Aug 2026 | 547 days | 95 | A | Westwood |
| PV Drilling VI | jackup | Malaysia | Dialog | Mar 2026 | 180 days | 97 | A | Westwood |
| Foresight Aryabhatt 1 / Vivekanand 1 | 350 ft jackups | Thailand | PTTEP | Feb/Apr 2027 | 5 years + 3 options | 60–70 | C | Splash247; SED analysis |
| Borr Norve | jackup | West Africa | undisclosed | Dec 2026 | 245 days + 175 options | — | D | Borr 30 Sep |
| Borr Natt | jackup | Nigeria | Shell | to Aug 2027 | 1-well option | — | D | Borr 30 Sep |
| Borr Joro | jackup (accommodation) | UK | undisclosed | Oct 2026 | 60 days + 56 options | — | D | Borr 30 Sep |
| Valaris DS-16 / DS-18 | 7G DS | US Gulf | Occidental | Jun / Nov 2026 | to Dec 2028 / Dec 2029 (~$760m combined) | — | D | Valaris FSR 5 Aug |
| **New since 4 Oct:** | | | | | | | | |
| Transocean Norge | 6G HE semi | NCS | A/S Norske Shell | after Harbour (≈ late 2028) | ~120 days, 2 wells + 1 option | ~517 ($62m excl. services) | B, short | Transocean 8-K 9 Oct; Drilling Contractor 9 Oct |
| Transocean Norge (check) | 6G HE semi | NCS | Harbour | Q1 2028 | 5 wells (~300 days) | ~497 ($149m) — confirms 497 | B | Transocean via Zacks 22 Sep |
| Enabler / Encourage / Endurance | HE semi (Cat D) | NCS | Equinor (now firm) | Q2 2027 / Q1 2028 | 7 rig-years ($1.0bn) | 399 base, > 400 effective | A | Transocean 8-K 9 Oct |
| Valaris DS-18 | 7G DS | Suriname | Petronas | Q4 2026 | 2 wells, up to 7 months | — | D | Valaris PR 7 Oct |
| Valaris 107 | jackup | Australia | — | after current work | ~300 days + priced options | ~167 ($50m excl. mob) | B | Valaris PR 7 Oct |
| Valaris (fleet award) | jackup | UK Southern North Sea | — (P&A) | window to Dec 2030 | 341 days + 19-day option | ~122 ($41.5m) | B | Valaris PR 7 Oct |
| Valaris 122 | jackup | Denmark | INEOS | Feb 2027 | 126 days + options 699 days | 115 | A | Valaris PR 7 Oct |
| Valaris 121 / 72 | jackups | UK (East Irish Sea) | Eni | Nov 2026 | ~8.5 months moved to 121; +$17m backlog | — | D | Valaris PR 7 Oct |
| Noble Interceptor | CJ70 HE jackup | NCS | ConocoPhillips (Ekofisk P&A) | Q3 2027 | 670 days | — | D | Offshore mag / OE Digital (Sep) |
| Noble Intrepid | CJ70 HE jackup | NCS | ORLEN Upstream Norge | Q3 2027 | 1 well, 40–60 days | — (BP UK to Sep 2027 at 150) | D (A for BP) | Offshore Energy / Ocean News (Sep) |
| Borr Mist | jackup | Malaysia | Sarawak Shell | Oct 2026 | ~45 days | — | D | Borr (via search) |
| **New 13 Oct:** | | | | | | | | |
| Seadrill West Carina | 7G DS (2015) | Indonesia | undisclosed | H1 2027 | 880 days + 880 days priced options | ~477 ($420m incl. mob, excl. services); ~450–460 ex-mob `[A]` | B | Splash247 13 Oct (Seadrill release) |
| Seadrill West Capella (priced options) | 6G DS (2008) | Malaysia | PTTEP | 2027 | 120 days | ~342 ($41m) | B, short | Splash247 13 Oct |
| Seadrill West Capella (unpriced options) | 6G DS (2008) | Malaysia | PTTEP | to Feb 2028 | 120 days | ~442 ($53m; set at market) | B, short | Splash247 13 Oct |
| Sonangol Libongos | 7G DS (2019) | Angola | undisclosed (Sonadrill JV) | 2027 | ~3 years, to Jan 2030 | — | D | Splash247 13 Oct |
| Sevan Louisiana | semi (circular, 2013) | US Gulf | Kosmos | Nov 2026 | 25 days | — | D | Splash247 13 Oct |
| Transocean Norge (current) | 6G HE semi | NCS | Harbour/OMV | Jun 2026 | to Jan 2028 | 472 | C | Splash247 12 Oct |
| Valaris DS-18 (next) | 7G DS | US Gulf | Occidental | after Suriname (~mid-2027) | 914 days + 2 × 1-year options | — | D | Splash247 8 Oct |
| **New 17 Oct:** | | | | | | | | |
| Odfjell Deepsea Atlantic (options) | 6G HE semi (2009, GVA 7500, DP) | NCS | Equinor | end Q2 2027 (direct continuation) | 2 wells, to late Q4 2027; 2 more priced wells + 3 × ~1-year periods (rate to be agreed) | — (original contract pricing; not a leading-edge print) | D | Odfjell release 16 Oct; Splash247 16 Oct |
| Odfjell Deepsea Atlantic (reference) | 6G HE semi | NCS | Equinor | mid-Q3 2026 | to end Q2 2027 (~319 days) | ~464 ($148m, excl. escalation, services, bonus) | B, signed Jan 2025 | Odfjell disclosure 29 Jan 2025 |
| **New 22 Oct:** | | | | | | | | |
| ENEOS Hakuryu-5 | Benign semi (1977, moored, ≤ ~500 m) | Timor-Leste (KTJ, PSC 19-11) | Finder Energy (JV with TIMOR GAP) | 1 Dec 2027 (window to 15 Mar 2028) | 3 wells, ~150 days (minimum 140) + 2 option wells; conditional on FID (30 Nov 2026) and approvals | ≤ ~282–302 all-in ($42.3m estimated gross JV cost) | C (upper bound) | Finder release 19 Oct (via energy-pedia); OE Digital 20 Oct; Offshore mag |
| **New 28 Oct:** | | | | | | | | |
| Energy Drilling T-16 (Phase 7) | Tender barge (2013, COSCO Nantong) | Malaysia–Thailand JDA | CPOC (Carigali-PTTEPI) | early Q3 2027 (after ~5 months idle in Singapore) | 30 months firm + up to 15 months options | ~95.1 (USD 87m firm incl. undisclosed mobilisation ÷ ~915 days); ~89–92 ex-mob `[A]` | B | SED/Energy Holdings release (MFN) 27 Oct 07:00 |
| Energy Drilling T-16 (Phase 6, reference) | Tender barge | Malaysia–Thailand JDA | CPOC | Nov 2024 | firm to Dec 2026; campaign to Q1 2027 on options | 131 (options 124) | A (company) | `docs/SED-analysis.md` (Pareto 17 Sep); MFN 27 Oct |
| Sapura Esperanza / Sapura Jaya (reference) | Semi-tenders (2013 / 2011) | Malaysia | PCSB (assignment) / Vestigo | Q3 2026 | — | — (not covered by the row) | D | Drilling Contractor 5 Aug 2026; The Star 4 Aug 2026 |
| **New 4 Nov:** | | | | | | | | |
| Deepwater Proteus | 7G DS (2016) | US Gulf | undisclosed | Feb 2027 | 10 wells, to Jan 2029 (~23 months) | **465** | A | Transocean fleet status 2 Nov |
| Deepwater Conqueror | 7G DS (2016) | US Gulf | undisclosed | Aug 2027 | 5 wells, to Nov 2028 (~15 months) | **499** | A | Transocean fleet status 2 Nov |
| Deepwater Conqueror (check) | 7G DS | Equatorial Guinea | Chevron (Westwood) | Jan 2027 | 2 wells, to Jul 2027 | 465 (Westwood $470,588); replaces ~471 (B) | A, short | Transocean fleet status 2 Nov; Westwood October edition |
| Dhirubhai Deepwater KG2 (check) | DS (2010) | India | ONGC | Feb 2027 | to Feb 2029 + priced options to Feb 2031 | **389** (replaces 395) | A | Transocean fleet status 2 Nov (binding LOA) |
| Deepwater Corcovado / Orion (check) | DS (2011) | Brazil | Petrobras | Jan 2027 | to Nov 2030 / Mar 2030 | 392 / 392 (Corcovado replaces ~385 B) | A | Transocean fleet status 2 Nov (awarded H1 2026) |
| Deepwater Aquila (reference) | 8G DS (2024) | Brazil | Petrobras | Jan 2027 | to Jun 2028 | 442 | A | Transocean fleet status 2 Nov (older award) |
| Noble Globetrotter I | DS (2011, non-Tier-1) | Peru | Occidental | Q2 2027 | 2 wells; then TotalEnergies West Africa 3-year light-well-intervention capacity reservation (≥ 150 days a year) | 400 (+ mob fee) | A, short | Noble Q3 release 26 Oct |
| Noble BlackHawk | 7G DS | Uruguay | Apache | Q4 2027 | 1 well, ~50 days | ~500 (~$25m excl. mob/demob) | B, short | Noble Q3 release 26 Oct |
| Noble BlackRhino / Faye Kozack | 7G DS | Nigeria / Ghana | TotalEnergies / Tullow | Q4 2026 / mid-2027 | 4 wells ~150 days + 6 options / 5 wells ~250 days + 5 options | — | D | Noble Q3 release 26 Oct |
| Noble (range statement) | Tier-1 DS | various | various | 2027 | ~44 months of new floater backlog since Q2 | "mid-400s to 500" | A (company range, n `[?]`) | Noble Q3 release 26 Oct |
| VALARIS DS-12 (extension) | DS (2013) | Egypt | BP | late 2027 / early 2028 | 60 days (priced) | ~417 (~$25m) | B, short | Valaris fleet status 2 Nov |
| Transocean Barents | HE semi (2009) | NCS (from Romania) | Vår Energi | Jun 2027 (after 145 days of mobilisation and preparation) | to Jun 2030 + priced options to Jun 2034 | **470** (FSR, escalated; ~450 at signing, ~$490m ÷ 1,095 days) | A | Transocean fleet status 2 Nov; Transocean release 8–9 Apr 2026 (via OGJ, OE Digital) |
| Transocean Norge (primary) | 6G HE semi | NCS | Harbour Energy | Jan 2028 | to Oct 2028 (5 wells) + priced options to Mar 2029 | **517** (replaces 497 / 513) | A | Transocean fleet status 2 Nov |
| Transocean Norge (primary) | 6G HE semi | NCS | A/S Norske Shell | Mar 2029 | to Jul 2029 + priced option to Aug 2029 | 517 | A, short | Transocean fleet status 2 Nov |
| Transocean Spitsbergen | HE semi (2010) | NCS | Equinor | Apr 2027 | to Dec 2027 (priced extension) | 519 (May FSR: 503 for Jan–Oct 2027) | A, short | Transocean fleet status 2 Nov |
| Transocean Enabler / Encourage / Endurance (primary) | HE semis (Cat D) | NCS | Equinor | Apr 2028 / May 2028 / Jun 2027 | 3 / 2 / 2 years | 402 (escalated from 399) | A | Transocean fleet status 2 Nov |
| Transocean Encourage (bridge) | HE semi | NCS | Equinor | May 2027 | to May 2028 | 441 (Westwood had 416 for a Mar 2027 start) | A | Transocean fleet status 2 Nov |
| Transocean Equinox | HE semi (2015) | Australia | Santos | Apr 2027 | ~2 months + priced options to Oct 2027 | 395 | A, short | Transocean fleet status 2 Nov |
| Deepsea Nordkapp (extension) | HE semi (2019) | NCS | Aker BP | Jan 2028 | to end-2028 | — (set at market by two brokers by end-2026) | D | `docs/odl-analysis.md` v2 (Newsweb 17 Jul 2026) |
| Ventura SSV Catarina | semi | Indonesia | Searah JV (Eni / Petronas) | Oct 2026 | 70 days | 278.9 | A, short | Westwood October edition |
| Northern Offshore Embracer | jackup | Saudi–Kuwait Neutral Zone | KJO | Mar 2027 | 1,460 days | 91.3 | A | Westwood October edition |
| ARO-owned jackups × 5 | jackups | Saudi Arabia | Saudi Aramco | Oct 2026 (continuation) | 3-year extensions | — | D | Valaris fleet status 2 Nov |
| VALARIS 122 | jackup (2014) | UK | INEOS | Jul 2027 | 158 days + 541 days of options (UK/Denmark) | 125 | A, short | Valaris fleet status 2 Nov |
| VALARIS Norway | HE jackup (2011) | UK | Ithaca Energy | Q2 2027 | ~200 days + 163 days priced options | ~135 ($27m) | B, short | Valaris fleet status 2 Nov |
| VALARIS 107 | jackup (2006) | Australia | Emperor Energy | Q2 2027 | 1 well, ≥ 30 days | 165 | A, short | Valaris fleet status 2 Nov |
| VALARIS 106 (extension) | jackup (2005) | Indonesia | BP | Q4 2028 | 1 well, ~90 days + 3 options | ~111 ($10m) | B, short | Valaris fleet status 2 Nov |
| Seadrill Sevan Louisiana | semi (2013) | US Gulf | LLOG | after Kosmos (Dec 2026) | ~60 days | — | D | Seadrill Q3 release 3 Nov |
| **New 12 Nov:** | | | | | | | | |
| Beacon Pacific | 6G HE semi (CIMC Yantai, steel cut 2015; idle since build `[A]`; managed by Odfjell) | UK (Bruce; possibly Kyla and Greater Laggan) | Serica Energy | Q3 2027 | 6 firm wells + options (incl. P&A) | — (not disclosed) | D | Odfjell release 2 Nov (Newsweb); Serica via energy-pedia 2 Nov; Offshore mag 3 Nov |
| Deepsea Bergen (contract signed) | HE semi (2019, CS60E) | NCS | Vår Energi | early 2028 | 3 years + four 1-year priced options to 2035 | ~472 ($518m incl. mob ÷ ~1,095 days; LOA terms); options ~500 after FX and escalation (CEO `[E]`) | B | Odfjell release 10 Nov (Newsweb 06:06 UTC); Discovery Alert 10 Nov |
| ADNOC Drilling × 2 | high-spec jackups (1 owned, 1 bareboat-chartered) | Kuwait | KOC | Q4 2027 | 4 years firm incl. mob + 1-year option each | ~107 ($313.6m maximum ÷ 2,920 rig-days, incl. mob; upper bound) | B | World Oil 9 Nov; OE Digital; The National 10 Nov |
| Shelf Perseverance (ADES) | JU-2000E, 400 ft | Indonesia | Pertamina Hulu Mahakam | end-Dec 2026 | 406 days + 30-day option | ~106 ($46.17m firm + option incl. mob/demob ÷ 436 days); ex-mob ~100–104 `[A]` | B | OE Digital 3 Nov (ADES release) |
| Shelf Tenacious (ADES) | jackup, BMC Pacific 375 (2007) | Angola | (Chevron CABGOC on the prior extension) | Q1 2027 (continuation) | 1 year (priced option exercised) | ~142 ($52m ÷ 365) | B (option; not a new print) | OE Digital 3 Nov (ADES 27 Oct) |
| ADES Key Singapore / Admarine 10 | standard jackups | India | ONGC | ~Q1 2027 | 3 years each | ~54 ($117.2m for two incl. mob ÷ 2,190 days) | B (not high-spec) | OE Digital; Saudi Gulf Projects (Nov) |
| Velesto NAGA 3 | jackup | Malaysia | Petronas Carigali | Nov 2026 | 1 well + 1 option | — | D | Drilling Contractor 4 Nov |
| Ocean MVM (ex-Noble Resolve) | CJ50 HE jackup | Tunisia | Tende Energy | `[?]` | Abiod well | — | D | AllAfrica (French), Nov 2026 |

### Rig-by-rig availability and cover (main contractors; as of the Q3 fleet status reports, 26 Oct–4 Nov, plus releases to 12 Nov)

- **Transocean** (27 rigs: 20 UDW, 7 HE; fleet status 2 Nov, 10-Q 3 Nov):
  - Backlog **$7,966m** (UDW $5,189m, HE $2,777m). $2.0bn was added since August at a weighted ~$423k.
  - Uncommitted fleet rate (excl. priced options), rest-2026 / 2027 / 28 / 29 / 30: UDW 15% / 22% / 56% / 80% / 93%; HE 0% / 8% / 31% / 47% / 74%.
  - Q3 utilization: UDW 67.6% (3 rigs idle or preparing), HE 95.1%. Average daily revenue: UDW $442.1k, HE $504.3k. Revenue efficiency: 96.4% / 97.7%.
  - Average contract dayrates: UDW Q4-26 $454k → Q3-27 $443k; HE $478k → $465k.
  - Stacked: Ocean Rig Apollo, Athena and Mylos (since 2016–17).
  - **UDW:**
    - Proteus: US Gulf, Feb 2027–Jan 2029, $465k.
    - Conqueror: Equatorial Guinea Jan–Jul 2027 ($465k), then US Gulf Aug 2027–Nov 2028 ($499k).
    - Asgard: East Med, Dec 2026–Dec 2027, $405k.
    - Skyros: Chevron Australia, Mar 2027–Feb 2028 (rate not disclosed in the FSR; $406k per Westwood); priced options to Jul 2030.
    - KG2: ONGC, Feb 2027–Feb 2029, $389k, with priced options to Feb 2031. KG1: Reliance to Mar 2028, $410k.
    - Petrobras 10000: to Aug 2029 ($428k → $454k in steps).
    - Corcovado and Orion: Petrobras to Nov 2030 / Mar 2030, $392k. Aquila: Petrobras to Jun 2028, $442k.
    - Atlas: available early 2027, then bp from Jun 2028 ($635k, 8G).
  - **HE:**
    - Norge: Harbour/OMV to Jan 2028 ($476k / $558k), Harbour Jan–Oct 2028 ($517k) + priced options to Mar 2029, Shell Mar–Jul 2029 ($517k).
    - Spitsbergen: Equinor to Dec 2027 ($417k → $519k from Apr 2027), then open.
    - Barents: Romania to Jan 2027 ($498k), yard Feb–Jun 2027, Vår Jun 2027–Jun 2030 ($470k).
    - Enabler to Apr 2031, Encourage to May 2030 (bridge from May 2027 at $441k), Endurance Jun 2027–Jun 2029 (Equinor, $402k in the package terms).
    - Equinox: Santos, Australia, Apr–Jun 2027 ($395k) + options to Oct 2027.
- **Valaris** (fleet status 2 Nov; 10-Q 3 Nov):
  - Backlog ~$4.75bn (+~$600m since 5 Aug). Drillship contracted days: 3,152 in 2027 (≈ 8.6 rig-years of 10 active drillships) at a backlog average of $432k (2028+: $417k). Jackup backlog average 2027: $130k.
  - Drillships:
    - Brazil: DS-4 to Oct 2030; DS-8 to Shell Brazil from Mar 2027 (~800 days); DS-17 with Equinor Brazil to Jan 2028.
    - Angola and Nigeria: DS-7 Angola to Sep 2027; DS-9 Angola to Jul 2028; DS-10 Nigeria to Jul 2028.
    - DS-12: BP Egypt to Apr 2027, plus 60 days in late 2027 / early 2028.
    - DS-15: Spain / Côte d'Ivoire to May 2027.
    - US Gulf: DS-16 to Dec 2028. DS-18 works for Petronas in Suriname Nov 2026–May 2027, then 914 days for Occidental in the US Gulf.
  - Stacked: DS-11, DS-13 and DS-14 (Spain); jackups 148, 147 and 143 (UAE) and Viking (UK).
  - Jackups:
    - 248: UK P&A to Mar 2030.
    - 115 Brunei to Apr 2029; 110 Qatar to Oct 2029.
    - 122: Denmark to ~Jun 2027, then UK from Jul 2027 ($125k).
    - 107: Australia. VALARIS Norway: Ithaca from Q2 2027.
    - 121: East Irish Sea from Nov 2026. 72 finishes Mar 2027.
    - VALARIS 111 was sold for MOPU conversion. Seven units are leased to ARO.
  - Middle East: all Valaris and ARO rigs under contract; five ARO-owned rigs have 3-year Aramco extensions. Merger closing ~1 Dec 2026.
- **Odfjell** (Q3 of 3 Nov; firm backlog $2.5bn; Q3 financial utilization 89%, September 98%):
  - Deepsea Bergen: Equinor to Q1 2028, then **Vår 3 years to Q1 2031 (contract signed 10 Nov)** plus four 1-year priced options to 2035.
  - Deepsea Nordkapp: Aker BP, firm to end-2028; the rate is set at market by two brokers by end-2026.
  - Deepsea Aberdeen: Equinor to Q1 2029. Deepsea Stavanger: Aker BP to ~Q1 2030.
  - Deepsea Atlantic: Equinor, firm to late Q4 2027, then two priced wells and three ~1-year periods as options. Off hire 106 days Apr–Aug 2026 (BOP incident; a company issue).
  - Hercules (SFL-owned, managed by Odfjell): leaves Norway for **Canada**, ≥ 400 days from Q1 2027 (~$170m ≈ $425k, B). It is not an NCS rig in 2027 (correction 12 Nov).
  - **Beacon Pacific** (owned by a CIMC affiliate, managed by Odfjell, the ninth HE rig in its managed and owned fleet): Serica UK from Q3 2027, six firm wells.
- **Seadrill** (Q3 release 3 Nov; 10-Q 4 Nov):
  - Backlog $2,813m; drilling contracts $2,577m, of which $1,207m in 2027 and $614m in 2028. More than 85% of available 2027 drillship days are contracted.
  - West Neptune: LLOG, 365 days from Sep 2026. West Vela: 270 days from Aug 2026.
  - West Polaris: Petrobras to Jan 2028, then 1,095 days. West Capella: PTTEP, Malaysia, to Feb 2028.
  - West Carina (2015 7G): Indonesia, H1 2027, 880 days firm + 880 days priced options. Sonangol Libongos: Angola to Jan 2030.
  - Sevan Louisiana: Kosmos (25 days, Nov 2026), then ~60 days for LLOG.
  - West Vela, West Elara and Sevan Louisiana had time between contracts in Q3. The fleet status PDF was not read.
- **Noble** (Q3 release 26 Oct; 23 marketed floaters 66% contracted in Q3; 5 marketed UHE jackups 86%; backlog $6.7bn; "~20% more contracted capacity in H2 2027 than H1 2027"):
  - Viking: Brunei from Jan 2028, $460k.
  - Faye Kozack: Petrobras to Jan 2027, then Tullow Ghana from mid-2027.
  - BlackRhino: TotalEnergies Nigeria from Q4 2026. BlackHawk: Apache Uruguay, Q4 2027.
  - Globetrotter I: Occidental Peru from Q2 2027 ($400k), then a TotalEnergies intervention capacity reservation. Globetrotter II: sale ($38m) pending.
  - GreatWhite: Aker BP from Q2 2027, 3 years. Claus Bachmann: BP UK from Mar 2027.
  - Interceptor: DNO, then ConocoPhillips Ekofisk P&A from Q3 2027 (670 days). Intrepid: BP UK to Sep 2027 ($150k), then ORLEN Norway in Q3 2027.
- **Borr** (no release since 30 Sep apart from the Prospector 5 updates; Q3 ~18 Nov):
  - 2026 cover 73% at ~$134k (Q2 report, 11 Aug; 70% in April).
  - Norve: West Africa, Dec 2026–Aug 2027. Natt: Shell Nigeria to Aug 2027. Joro: UK accommodation to Dec 2026.
  - Odin: US from 11 Sep. Idun: Vietnam, Q4 2026. Bestla: ENI to Sep 2027.
  - Perfomex divested; Borr keeps the Mexico rigs on bareboat economics.
  - Fontis JV: 3 of 5 contracted (Aug). Prospector 5 lost (24 Oct).
- **ADES / Shelf:**
  - Perseverance: PHM Indonesia from end-Dec 2026 (406 days).
  - Tenacious: Angola, +1 year from Q1 2027.
  - Key Singapore and Admarine 10: ONGC, 3 years from ~Q1 2027.
  - Saudi offshore rigs all resumed since Aug.
- **Cold-stacked drillships (9, Westwood):** six in Transocean–Valaris (Ocean Rig Apollo 2015, Athena 2014, Mylos 2013; VALARIS DS-11 2013, DS-13 2023, DS-14 2023); three with other owners `[?]`. No reactivation without a long contract.
- **Stranded units:**
  - Keppel RigCo at Seatrium: a 7G drillship (delivery 2027) and an N-class HE jackup (2028), being completed with no contract; two mid-water HE semis for NW Europe, completion under assessment.
  - CIMC: Beacon Pacific, to the UK for Serica (Q3 2027).

### Sources

| Source | Content | Definition | Observed / published |
|---|---|---|---|
| [Westwood Offshore Energy Data Dashboard](https://www.westwoodenergy.com/news/infographics/offshore-energy-data-dashboard) | MCU, total utilization, committed, available, cold-stacked, backlog, fixtures; month-by-month backlog tables Feb–Aug editions | MCU = contracted ÷ marketed; backlog in rig-years, **start-of-month snapshots**, prior month restated per edition | Aug activity / published 25 Sep, updated 30 Sep 2026; read 10 Oct |
| [Westwood weekly global rig count](https://www.westwoodenergy.com/news/infographics/weekly-global-offshore-rig-count) | Working jackups 376, floaters 135 (19 Oct, read 24 Oct; October weeks have no regional split); 373 / 134 (12 Oct, read 17 Oct); 374 / 134 (5 Oct); Sep weekly 374–377 / 134–137; Aug month-end 372 / 138 | Working, not utilization; the page's month-end commentary (+5 / −1) does not match its own table (+4 / −4); table used | 12 Oct 2026 (latest); 5 Oct 2026 |
| [Westwood Brazil offshore rig count](https://www.westwoodenergy.com/news/infographics/brazil-offshore-rig-count) | 47 operating, 35 drilling; by type and operator; outstanding rig-days 2027–29 | Operating vs drilling; the type table's drilling column sums to 37 (inconsistent) | Data 1 Oct 2026 |
| [Rigzone/Bloomberg — Saudi Aramco evacuates HQ](https://www.rigzone.com/news/saudi_aramco_evacuates_hq-22-oct-2026-184909-article) | Dhahran HQ evacuated after an alarm; staff remote; cause and duration unknown; Shaybah and Dammam attacks; US staff drawdown | Secondary (unnamed sources); Aramco no comment | 22 Oct 2026 |
| [Reuters via Al-Monitor — US orders departure of diplomats from Saudi Arabia](https://www.al-monitor.com/originals/2026/10/us-orders-departure-diplomats-saudi-arabia-amid-houthi-strikes) | Ordered departure (Saudi Arabia only); Dammam airport 1 killed, 8 injured; Shaybah drone intercepted, 2 killed (energy ministry) | Wire report; casualty counts differ between outlets | 21 Oct 2026 |
| [Transocean fleet status report, 2 Nov 2026](https://www.deepwater.com/documents/FleetStatusReport/2026/November%202026%20Fleet%20Status%20Report.pdf) (8-K exhibit; PDF read via text extraction) | Rig-by-rig customer, dates and dayrates; updates (Conqueror, Proteus, KG2, Norge–Shell, Equinox); average contract dayrates by quarter; backlog ~$8.0bn | Full contractual operating dayrate; excludes mobilisation; NCS rates include a non-USD component and escalation (footnotes 1, 2) | As of 2 Nov 2026; read 4 Nov |
| Transocean 10-Q Q3 2026 (FinancialFilings 75463011) | Uncommitted fleet rates 2026–30; backlog by class; average daily revenue; revenue efficiency; utilization; outlook | Uncommitted = idle or stacked days ÷ calendar days, excluding priced options | Q3 2026 / filed 3 Nov 2026 |
| Valaris Q3 release and fleet status (FinancialFilings 75379362, 75382064) | Q3 results (adjusted EBITDA $151m; ~$24m Middle East impact); merger close ~1 Dec; new awards; contracted days and average rates by class; Middle East status; ARO extensions | Backlog excludes lump-sum mobilisation | As of 2 Nov 2026 |
| Noble Q3 release (FinancialFilings 74765190) and 10-Q (74797448) | Floater 66% contracted, UHE jackups 86%; Tier-1 leading edge "mid-$400,000s to $500,000"; UHE jackups $230–300k; new awards; Resolve / Globetrotter II sales | Company statements; backlog excludes mobilisation | 26 / 27 Oct 2026 |
| Seadrill Q3 release (FinancialFilings 75462278) | Awards since August (~$800m TCV); > 85% of 2027 drillship days contracted; backlog ~$3.3bn | TCV includes mobilisation | 3 Nov 2026 |
| Westwood dashboard, October edition (same URL as above) | Sep activity: MCU drillships 93% / semis 82% / jackups 88%; committed 80 / 59 / 384; available 6 / 12 / 54; cold-stacked 9 / 7 / 51; backlog 1 Sep (restated) → 1 Oct; fixtures (Embracer $91,267; Catarina $278,888; Conqueror $470,588) | As above; total fleet derived from the counts | Sep activity / published 25 Oct, updated 27 Oct 2026; read 4 Nov |
| Westwood weekly (same URL as above), re-read 4 Nov | Latest is still week 43 (19 Oct: 376 / 135); 26 Oct and 2 Nov not posted | Working counts | Read 4 Nov 2026 |
| Borr 6-Ks 29 Oct and 2 Nov (FinancialFilings 75118812, 75346449) | Prospector 5 updates (4 dead, 1 missing; independent investigation); no Gulf notice | Company releases | 29 Oct / 2 Nov 2026 |
| OGJ / OE Digital (Apr 2026) | Transocean Barents–Vår Energi 1,095 days from mid-2027 at ~$450k, ~$490m (signing value) | Secondary, matches the Transocean release | 8–9 Apr 2026; found 4 Nov |
| `docs/odl-analysis.md` v2 (4 Nov) | Odfjell Q3 (3 Nov): Bergen options to 2035, Nordkapp to end-2028, Atlantic to late Q4 2027, price-implied ~$413k through-life | Company analysis in this workspace (read only) | 4 Nov 2026 |
| [The National — Houthis launch another wave of attacks](https://thenationalnews.com/business/energy/2026/10/23/oil-prices-rise-as-houthis-launch-another-wave-of-attacks-on-saudi-arabia) | Houthi claims (Defence Ministry Riyadh, Dammam, Yanbu, Abha); no production loss reported; no offshore mention | Trade press; claims `[E]` | 23 Oct 2026 |
| [gCaptain — two more tankers struck](https://gcaptain.com/two-more-tankers-struck-as-maritime-attacks-spread-across-persian-gulf/) | UKMTO: Al Faw (20 Oct), Bukha (21 Oct); Jubail tankers 16 Oct (RPG, small boat); JMIC: 17 Oct mine claims unsubstantiated; no rigs or platforms mentioned | Trade press citing UKMTO/JMIC | 21 Oct 2026 |
| [Drilling Contractor — ADES resumes all suspended offshore rigs in Saudi Arabia](https://drillingcontractor.org/ades-resumes-all-suspended-offshore-rigs-in-saudi-arabia-79312); [AGBI](https://www.agbi.com/oil-and-gas/2026/08/ades-confirms-all-offshore-rigs-in-saudi-arabia-are-operational/) | All suspended Saudi offshore rigs resumed; Qatar rigs resumed earlier; CEO: 10 Gulf rigs halted in March | Company disclosure via trade press | 11–12 Aug 2026 |
| [Arabian Drilling — Tadawul disclosure](https://www.saudiexchange.sa/Resources/fsPdf/28194_3703_2026-08-12_08-33-13_en.pdf) | Remaining suspended offshore rigs resume; offshore utilization 100% by end-Q3 expected | Primary filing; PDF returned 403, content via search summary | 12 Aug 2026 |
| [Westwood Insight — Middle East conflict reverberates through jackup market](https://www.westwoodenergy.com/news/westwood-insight/westwood-insight-middle-east-conflict-reverberates-through-jackup-market) | Arabian Gulf ~36% of global jackup supply; working 83% → ~69%, committed ~90%; 2026 committed 89–91%; Aramco, KOC, KJO tenders (~56 rig-years) | Westwood commentary `[E]` | 13 May 2026 (page dated 17 Aug) |
| [Khaleej Times — Kuwait drone attack on offshore oil platform](https://www.khaleejtimes.com/world/gulf/kuwait-drone-attack-offshore-oil-platform-injures-worker?amp=1) | KOC offshore drilling platform hit, one worker injured | Kuwait MoD via press | 12 Jul 2026 |
| [OE Digital — Ocean Oilfield brings Noble jackup into its fleet](https://www.oedigital.com/news/543761-ocean-oilfield-brings-noble-corporation-s-jack-up-rig-into-its-fleet); [Noble — planned divestment of six jackups](https://s201.q4cdn.com/439848451/files/doc_news/2025/12/Noble-announces-planned-divestment-of-six-jackups.pdf) | Noble Resolve → Ocean MVM, $64m cash, CJ50-X100 MC, in Malta 13 Oct, marketed worldwide | Transaction price (agreed Dec 2025); build year not confirmed `[?]` | 15/19 Oct 2026; 11 Dec 2025 |
| [Valaris — Q3 2026 earnings date](https://s23.q4cdn.com/956522167/files/doc_news/2026/10/10-14-2026-Valaris-Schedules-Third-Quarter-2026-Earnings-Release.pdf) | Q3 release after close 2 Nov; no call (pending combination) | Company notice | 14 Oct 2026 |
| [OE Digital — Finder Energy selects ENEOS rig for drilling job off Timor-Leste](https://www.oedigital.com/news/543783-finder-energy-selects-eneos-rig-for-drilling-job-off-timor-leste) (user input) | Hakuryu-5, KTJ 3 wells, Dec 2027, ~150 days, $42.3m estimated gross JV cost, conditions | Secondary; cost estimate, not contract value | 20 Oct 2026 |
| [energy-pedia — Finder Energy secures drilling rig for KTJ development](https://www.energy-pedia.com/news/timor-leste/finder-energy-secures-drilling-rig-secured-for-ktj-development-205713) | Finder release: contract executed, conditional, start 1 Dec 2027, 3 firm + 2 option wells | Company release (ASX) reproduced; annexure with rig terms not shown | 19 Oct 2026 |
| [Offshore mag — Finder selects Hakuryu-5](https://www.offshore-mag.com/drilling-completion/news/55412349/finder-selects-hakuryu-5-rig-for-ktj-development-drilling-offshore-timor-leste) | Same terms; subject to approvals | Trade press | Oct 2026 |
| [Splash247 — Japan Drilling awarded semisub contract by Inpex](https://splash247.com/japan-drilling-awarded-semisub-contract-by-inpex/); [Offshore Energy — Petronas hires Japan's rig owner](https://offshore-energy.biz/?p=558331) | Hakuryu-5: 1977 Mitsubishi build, max 1,640 ft (option 1,970 ft); Inpex Japan 2022, Petronas Sarawak 2022 | Rig spec and history | 2022 |
| [Splash247 — Equinor keeps Odfjell Drilling semisub busy into late 2027](https://splash247.com/equinor-keeps-odfjell-drilling-semisub-busy-into-late-2027/) (user input) | Deepsea Atlantic: two priced wells, firm to late Q4 2027; rate not disclosed; Jan 2025 background ($148m) | Secondary (Odfjell release); fetched directly this time | 16 Oct 2026 |
| [Odfjell Drilling — Equinor exercises options for two additional wells for Deepsea Atlantic](https://www.inderes.fi/en/releases/odfjell-drilling-ltd-equinor-exercises-options-for-two-additional-wells-for-deepsea-atlantic) | Two wells in direct continuation; firm to late Q4 2027; original contract pricing; two further priced wells | Primary (Oslo Børs disclosure, via Inderes) | 16 Oct 2026, 11:35 |
| [Odfjell Drilling — Extension of Deepsea Atlantic contract](https://www.odfjelldrilling.com/disclosure/odfjell-drilling-ltd-extension-of-deepsea-atlantic-contract/) | Mid-Q3 2026 → end Q2 2027, ~$148m; four priced wells and three ~1-year periods as options | Value excl. escalation, services, bonus, fuel incentives; ÷ ~319 days = ~$464k `[B]` | 29 Jan 2025 |
| [Offshore Energy — Equinor employs 2009-built Odfjell rig for additional wells](https://www.offshore-energy.biz/2026/10/16/equinor-employs-2009-built-odfjell-drilling-rig-for-additional-wells) | Rig spec; BOP dropped in April, 106 days off hire, back in August; Viking Avant PSV extension to end-2027 | Trade press | 16 Oct 2026 |
| [Splash247 — Indonesia award leads new batch of Seadrill contracts](https://splash247.com/indonesia-award-leads-new-batch-of-seadrill-contracts/) (user input) | West Carina $420m / 880 days; West Capella options $41m + $53m; Libongos to Jan 2030; Sevan Louisiana; > 85% of 2027 days contracted | Values incl. mob, excl. services; secondary (Seadrill release); read via Edge (site blocks fetch) | 13 Oct 2026 |
| [Splash247 — Transocean books new Shell work and firms up $1bn Equinor deal](https://splash247.com/transocean-books-new-shell-work-and-firms-up-1bn-equinor-deal/) (user input) | Norge current $472k; Harbour 2028 $513k; Equinor firm | Secondary; read via Edge | 12 Oct 2026 |
| [Splash247 — Valaris adds $220m of new contracts and extensions](https://splash247.com/valaris-adds-220m-of-new-contracts-and-extensions/) (user input) | Same as the Valaris 7 Oct release; plus DS-18 → Occidental 914 days | Secondary; read via Edge | 8 Oct 2026 |
| [Riviera — Westwood: rig dayrates (mostly) continue to fall in 2026](https://www.rivieramm.com/news-content-hub/news-content-hub/westwood-offshore-rig-dayrates-mostly-continue-to-fall-in-2026-89065) | Leading-edge 2026 YTD: drillships 6G 371 / 7G 407 / avg 388; semis < 340, Norway 436; jackups ~94 excl. Norway/Australia; utilization mid-June | RigLogix leading-edge averages (Teresa Wilkie, Westwood) | YTD to mid-June / 15 Jun 2026 |
| [Transocean 8-K — Equinor approval and Norge–Shell](https://www.sec.gov/Archives/edgar/data/0001451505/000145150526000072/rig-ex99d1.htm) | Equinor $1.0bn firm (approval late Sep); Norge Shell 2 wells, ~120 days, $62m | Backlog excl. additional services | 9 Oct 2026 |
| [Drilling Contractor — Transocean Norge wins two-well Norske Shell contract](https://drillingcontractor.org/transocean-norge-wins-two-well-norske-shell-contract-in-norway-80313) (user input) | Same facts as the 8-K | Secondary; verified against the 8-K | 9 Oct 2026 |
| [Valaris PR — contract awards and fleet status updates](https://s23.q4cdn.com/956522167/files/content_files/10-7-2026-Valaris-Announces-Contract-Awards-and-Fleet-Status-Updates.pdf) | DS-18 Suriname; 107 Australia $50m; SNS P&A $41.5m; 122 $115k; 121/72 Eni; MS-1 and 111 recycled | Backlog excl. lump sums | 7 Oct 2026 |
| [Zacks analyst report — RIG](https://www.zacks.com/zer/report/RIG) | Management view: > 90% high-spec 2027; ~100 rig-years H1; ~40 tenders (75–80 rig-years); Brazil 30–33 rigs; Africa 20–25; drillship coverage 81% (2027); Norge Harbour $149m; O&M guidance; reactivation $100–150m | Contractor commentary relayed `[E]`, grade C | 22 Sep 2026 |
| [Ocean News — Noble Intrepid/ORLEN](https://oceannews.com/news/energy/noble-intrepid-jackup-rig-tapped-for-orlen-exploration-drilling-offshore-norway/); [OE Digital — Noble Interceptor/ConocoPhillips](https://www.oedigital.com/news/541887-conocophillips-hire-noble-corporation-s-jack-up-for-ekofisk-p-a-work) | NCS jackup work Q3 2027; Intrepid BP $150k | Trade press | Sep 2026 |
| [Offshore mag — Venus fiscal accord](https://www.offshore-mag.com/field-development/news/55398042/totalenergies-awaits-fiscal-accord-before-venus-fid-offshore-namibia); [The Namibian — "before 2027"](https://www.namibian.com.na/venus-decision-must-come-before-2027-totalenergies/) | Venus FID status | Trade press | 2026 |
| [Nordnet / TDN Finans — "Valaris: kontrakter og forlengelser på rundt 220M USD"](https://www.nordnet.no/market/news/b1dc57a8-41cb-4bdb-8824-bdc3d186cd43) (user input) | Summary of Valaris's 7 Oct release; matches the primary PDF | Secondary; read via the Edge connection (needs a logged-in session) | 7 Oct 2026, 13:20 |
| [Transocean PR — Deepwater Conqueror](https://www.globenewswire.com/news-release/2026/09/15/3361834/0/en/transocean-ltd-announces-80-million-contract-for-ultra-deepwater-drillship.html) | EG 2 wells, ~170 days, $80m | Value excl. mob and services | 15 Sep 2026 |
| [Transocean quarterly fleet status (PR)](https://www.globenewswire.com/news-release/2026/08/05/3339805/0/en/transocean-ltd-provides-quarterly-fleet-status-report.html) | $292m new backlog; $6.7bn backlog; Equinor $1.0bn excluded | — | 5 Aug 2026 |
| [World Oil — Transocean/Equinor](https://www.worldoil.com/news/2026/6/30/transocean-lands-seven-year-1-billion-equinor-rig-deal/) | 7 rig-years, $399k base | Conditional on licence approval | 30 Jun 2026 |
| [Valaris fleet status report (8-K)](https://www.sec.gov/Archives/edgar/data/0000314808/000031480826000139/fsrex99_1august2026.htm) | Rig-by-rig contracts, stacked, sold rigs, backlog $4.6bn | As-of 5 Aug | 5 Aug 2026 |
| [Borr contracting update](https://finance.yahoo.com/energy/articles/borr-drilling-limited-contracting-updates-203900488.html) | Norve, Natt, Joro | — | 30 Sep 2026 |
| [Borr Q2 2026 (6-K)](https://www.sec.gov/Archives/edgar/data/0001715497/000114036126032598/ef20080031_ex99-1.htm) | Cover 73% at ~$134k; Fontis JV $287m; Middle East costs | — | 11 Aug 2026 |
| [OE Digital — Deepsea Bergen/Vår](https://www.oedigital.com/amp/news/542860-v-r-energi-picks-odfjell-drilling-s-deepsea-bergen-for-multi-year-drilling-ops) | 3 years from 2028, $518m | Incl. mob; excl. escalation, services, bonus | 10 Sep 2026 |
| [Shipping Telegraph — Bollsta sale](https://shippingtelegraph.com/offshore-news/odfjell-drilling-acquires-semi-sub-rig-from-northern-ocean-for-480m/) | $480m, $355m backlog | Transaction price | 17 Nov 2025 |
| [Drilling Contractor — KJO award](https://drillingcontractor.org/arabian-drilling-wins-four-jackup-offshore-contract-from-kjo-80162) | 4 jackups, 4 years, SAR 2bn | Contract value | 28 Sep 2026 |
| [Splash247 — Deepsea Mira/Shell](https://splash247.com/northern-ocean-scores-70m-shell-semisub-deal) | 150 days, $70m incl. mob; option to $226m | Value; page blocked (403), figures via search summary `[E]` | Sep/Oct 2026 |
| [Splash247 — Valaris awards](https://splash247.com/valaris-secures-nearly-900m-in-new-rig-awards-and-extensions/) | DS-16/18, 248, 122 | — | 2026 |
| [Offshore Energy — Deep Value Driller sale](https://www.offshore-energy.biz/saipem-loses-drillship-deal-to-higher-bidder/) | $300m to Eldorado (Saipem bid $272.5m) | Transaction price, 2014 7G | Feb 2026 |
| [Deepwater Insight — 7G market update](https://deepwaterinsight.com/7g-drillship-market-update/) | 7G MCU low 80s → ~89% by early 2027; Asgard $405k; Atlas $635k | Secondary `[E]` | 18 Apr 2026 |
| [Hartl — Offshore Drillers Q2 2026](https://arminhartl.substack.com/p/offshore-drillers-2026-q2-review) | Management guidance; rates incl. Norge $513k | Secondary `[E]`, grade C | 10 Aug 2026 |
| [Hartl — Offshore Supply Unpacked](https://arminhartl.substack.com/p/offshore-supply-unpacked) | Opex floaters ~$225k, jackups ~$90k; reactivation $85–150m, 12–18 months; recycling values | Secondary `[E]` | 14 Jan 2026 |
| [Westwood Insight (via Hellenic) — newbuild orders](https://www.hellenicshippingnews.com/1001334-2/); [Energy Intel](https://www.energyintel.com/0000017b-a7d8-de4c-a17b-e7dad29d0000) | Newbuild $850m–1bn+, required $650–720k | Secondary `[E]` | 2024–2025 |
| [Transocean 8-K — 2026 outlook](https://www.sec.gov/Archives/edgar/data/0001451505/000145150526000041/rig-20260504xex99d1.htm) | 2026 capex $150m (raised from $130m) | Total capex, no maintenance split; ÷ 27 floaters = $5.6m a rig `[B]` | 4 May 2026 |
| [Valaris 8-K — Q4 2025 results](https://www.sec.gov/Archives/edgar/data/314808/000031480826000025/a12312025ex991pressrelease.htm) | 2026 capex $425–475m, of which ~$260m maintenance and upgrades (incl. deferred drillship maintenance, jackup SPS) | Mixed fleet; not used for a per-rig figure | Feb 2026 |
| [Borr Q2 2026 results and call](https://www.sec.gov/Archives/edgar/data/1715497/000114036126032598/ef20080031_ex99-2.htm) | Economic utilisation 96.4%; capex $2–2.5m a rig a year; H1 cash tax 4.5% of revenue; Odin opex mid-$70k | Asset-value convention parameters (jackups) | 11–12 Aug 2026 |
| [Offshore mag — jackups and the 25-year life](https://offshore-mag.com/drilling-completion/article/16763186/jackups-new-market-niches-for-aging-drilling-equipment); Transocean 10-K (jackup non-operating life 30 years) | Economic-life conventions | Industry rule of thumb / accounting life `[E]` | older |
| [Splash247/Westwood — Middle East jackups](https://splash247.com/middle-east-conflict-derails-jackup-market-recovery/) | Working 83% → ~69%; committed ~90% | Westwood utilization | 14 May 2026 |
| [World Oil — Velesto/Chevron](https://worldoil.com/news/2026/7/22/velesto-secures-51-million-chevron-malaysia-drilling-contract/); Velesto/Bursa (NAGA 2) | NAGA 8 Chevron; NAGA 2 PCSB $157m 2026–2030 | Value | Jul / Mar 2026 |
| [World Oil — TotalEnergies Mopane](https://worldoil.com/news/2026/9/3/totalenergies-completes-entry-into-giant-mopane-discovery-offshore-namibia/); [Offshore mag](https://www.offshore-mag.com/field-development/news/55403205/totalenergies-totalenergies-takes-operatorship-of-namibias-mopane-discovery-targets-2028-fid) | Mopane FID 2028; Venus FID targeted 2026 | — | 3 Sep 2026 |
| [Offshore mag — Transocean–Valaris DOJ](https://www.offshore-mag.com/business-briefs/company-news/news/55406763/transocean-valaris-merger-reports-indicate-doj-may-clear-deal-early) | DOJ early clearance expected; CFIUS cleared 29 Jun | — | ~22 Sep 2026 |
| [World Oil — Petrobras extensions](https://worldoil.com/news/2026/4/14/transocean-adds-445-million-backlog-with-petrobras-drillship-extension/); [Deepwater Insight — Petrobras round](https://deepwaterinsight.com/petrobras-rig-tender-results-3-6-billion-in-deepwater-contracts-across-buzios-mero-and-renecon/) | $3.6bn cycle; Corcovado, DS-4 | Value ÷ days | Apr 2026 |
| [MFN — Energy Drilling receives letter of award for 30-month drilling campaign for T-16](https://mfn.se/a/energy-holdings/energy-holdings-energy-drilling-receives-letter-of-award-for-30-month-drilling-campaign-for-t-16) | T-16 Phase 7: CPOC, 30 months from early Q3 2027, options up to 15 months, ~USD 87m firm incl. mobilisation; Phase 6 firm to Dec 2026, ends Q1 2027; rig demobilised to Singapore in between | Primary (company release); no dayrate; value ÷ days `[B]` | 27 Oct 2026, 07:00 |
| [Offshore Energy — EDrill T-16 rig (CPOC campaign)](https://www.offshore-energy.biz/?p=781086) | T-16: 2013 build, JENGKA campaign for CPOC; history (Chevron 2013 at $115.5k) | Trade press | older |
| [Westwood weekly global rig count](https://www.westwoodenergy.com/news/infographics/weekly-global-offshore-rig-count) (re-checked 28 Oct) | Latest still week 43 (19 Oct): 376 / 135; **week 44 (26 Oct) not posted**; no October regional commentary | Working rigs | Checked 28 Oct 2026 |
| [MarineLink (Bloomberg) — Houthi missile strikes Saudi oil refinery](https://www.marinelink.com/news/houthi-missile-strikes-saudi-oil-refinery-543943) | Houthi claim: Ras Tanura refinery hit, fire; Bloomberg source: fire near the terminal contained; Saudi did not confirm; no offshore mention | Wire/trade press; claim `[E]` | 27 Oct 2026 |
| Detroit News (AP), 26 Oct; houseofsaud.com, 27 Oct (via search summaries; the first is paywalled) | Houthi claims on East-West pumping stations and Riyadh airport; coalition interceptions towards the Eastern Region | `[E]`, unconfirmed | 26–27 Oct 2026 |
| [The National — Aramco building attacked](https://www.thenationalnews.com/news/gulf/2026/10/14/aramco-building-on-fire-after-saudi-led-coalition-hits-houthi-site/) | Dhahran administrative building hit 13 Oct, fire, no casualties | Trade press, via search summary `[E]` | 14 Oct 2026 |
| [Offshore Energy — Borr jackup sinks off Gabon](https://www.offshore-energy.biz/2026/10/25/rig-incident-110-rescued-5-still-missing-after-borr-drillings-jack-up-sinks-off-gabon-coast) | Prospector 5 (2014 JU-2000E) sank 24 Oct 20:37 during preload (punch-through, preliminary); BW Energy Dussafu; 110 of 115 accounted for | Trade press citing Borr and BW Energy | 25 Oct 2026 |
| [Drilling Contractor — Vantris tender-assist contracts in Malaysia](https://drillingcontractor.org/vantris-secures-new-tender-assisted-drilling-rig-contracts-in-malaysia-79273) | Sapura Esperanza (PCSB assignment), Sapura Jaya (Vestigo), Q3 2026; no values per rig | Trade press | 5 Aug 2026 |
| [Westwood weekly global rig count](https://www.westwoodenergy.com/news/infographics/weekly-global-offshore-rig-count) (read 12 Nov) | Working jackups / floaters: 376 / 136 (26 Oct), 374 / 137 (2 Nov), 376 / 137 (9 Nov); October commentary: jackups up in South America, North America, Europe and Asia, down in the Middle East and Africa; floaters up in North and South America | Working rigs (RigLogix), Monday counts; the monthly narrative does not always match the table (table used) | 26 Oct–9 Nov 2026 |
| [Westwood dashboard](https://www.westwoodenergy.com/news/infographics/offshore-energy-data-dashboard) (re-read 12 Nov) | Still the October edition (Sep activity); no newer edition | As above | Published 25 Oct, updated 27 Oct 2026 |
| [Westwood Brazil offshore rig count](https://www.westwoodenergy.com/news/infographics/brazil-offshore-rig-count) (read 12 Nov) | 47 rigs, 35 drilling; 25 DS, 9 semis, 10 platform, 3 jackups; Petrobras 34; outstanding minimum rig-days 2027 210 / 2028 1,185 / 2029 780 | Operating vs drilling; prospects + tenders | Data 1 Nov 2026 |
| Seadrill 10-Q Q3 2026 (FinancialFilings 75612466) | RigLogix contracted rigs and marketed utilization (30 Sep): benign floaters 107 / 87%, HE floaters 23 / 97%, HE jackups 27 / 95%; backlog $2,813m by year; "signs that point towards a market recovery in 2027" | RigLogix series, a different source from the Westwood dashboard (context only) | Filed 4 Nov 2026 |
| Odfjell — Contract signed for Deepsea Bergen (Newsweb, via the Nordic Financial connector) | Vår contract formally signed; 3 years from early 2028; four 1-year priced options; booked to early 2031, options to early 2035 | Primary (Oslo Børs disclosure) | 10 Nov 2026, 06:06 UTC |
| [Odfjell — New management agreement and contract award for Beacon Pacific](https://www.inderes.dk/en/releases/odl-odfjell-drilling-ltd-new-management-agreement-and-contract-award-for-beacon-pacific) (Newsweb, via the Nordic Financial connector) | Serica contract with Beacon Pacific Offshore; six firm wells from Q3 2027; Odfjell manages; reactivation partly begun; similar to Deepsea Yantai | Primary; no rate | 2 Nov 2026 |
| [energy-pedia — Serica secures rig](https://www.energy-pedia.com/news/united-kingdom/serica-energy-secures-rig-for-multi-well-ukcs-drilling-programme-205915); [Offshore mag — North Sea roundup](https://www.offshore-mag.com/regional-reports/north-sea-europe/news/55416436/north-sea-roundup-serica-drilling-campaign-lyra-contract-award-lead-latest-activity); [OE Digital — Odfjell adds rig](https://www.oedigital.com/news/544051-odfjell-drilling-adds-new-rig-to-fleet-ahead-of-serica-s-uk-drilling-campaign) | Beacon Pacific: 6G semi upgraded to 620 m; owner Beacon Pacific Offshore (CIMC affiliate); Bruce infill first; P&A use; options | Company release reproduced; trade press | 2–3 Nov 2026 |
| [Upstream — CIMC cuts steel on Beacon Pacific](https://www.upstreamonline.com/online/cimc-cuts-steel-on-beacon-pacific/1-1-1166912); portnews / China Daily (2015) | Built by CIMC Raffles Yantai for Beacon (steel cut June 2015, delivery planned end-2017) | Build history; idle since build `[A]` | 2015 |
| [Discovery Alert — Deepsea Bergen into 2031](https://discoveryalert.com/news/deepsea-bergen-rig-contract-odfjell-var-energi-november-2026/) | Bergen ~$472k arithmetic; CEO on the Q3 call: options near $500k after FX and escalation; "37 of 38 marketed HE semis committed" (unverified industry estimate, not used) | Secondary `[E]` | 10 Nov 2026 |
| [Offshore mag — RigCo to complete four rigs with Seatrium](https://www.offshore-mag.com/rigs/news/55415204/seatrium-rigco-to-invest-over-s500-million-to-complete-four-offshore-drilling-rigs-with-seatrium); [Baird Maritime](https://www.bairdmaritime.com/offshore/vessels-rigs/seatrium-to-complete-keppel-rigs) | 7G drillship (2027), N-class HE jackup (2028), two mid-water HE semis (under assessment); > S$500m (~$390m); positioned for charters; no contracts | Company deal via trade press | 26–28 Oct 2026 |
| [World Oil — ADNOC Drilling enters offshore Kuwait](https://worldoil.com/news/2026/11/9/adnoc-drilling-enters-offshore-kuwait-with-two-jackup-rig-contracts-from-koc/); [The National](https://thenationalnews.com/business/energy/2026/11/10/abu-dhabis-adnoc-drilling-wins-contracts-worth-314m-from-kuwait-oil-company) | KOC: 2 jackups, 4 years firm incl. mob + 1 option year, Q4 2027, $313.6m maximum (KWD 96.6m); 1 owned, 1 bareboat-chartered; LOA | Contract value (maximum) ÷ days `[B]` | 9–10 Nov 2026 |
| [OE Digital — ADES lands Angola and Indonesia deals](https://www.oedigital.com/amp/news/544092-ades-lands-new-offshore-drilling-rig-deals-in-angola-and-indonesia) | Tenacious +1 year (~$52m); Perseverance PHM 406 + 30 days ($46.17m incl. mob/demob) | Values ÷ days `[B]` | 3 Nov 2026 (Angola announced 27 Oct) |
| [OE Digital — ADES lands $117m ONGC contracts](https://www.oedigital.com/news/544212-ades-lands-117m-ongc-drilling-contracts-for-two-jack-ups) | Key Singapore and Admarine 10, 3 years each, $117.2m incl. mob | Value ÷ days `[B]`; standard units | 9–11 Nov 2026 |
| [OE Digital — Tender-assist rigs head for full utilization (Westwood, P. Ezekiel)](https://www.oedigital.com/news/544178-tender-assist-rigs-southeast-asia-s-quiet-workhorses-head-for-full-utilization) | 29 TARs (16 active, 6 warm, 6 cold, 1 under construction); utilization ~96% → 100% by end-Q4; four TARs > $120k; 2027 semi-tender campaigns; PTTEP TAR vs jackup choice | Westwood commentary `[E]` | 5 Nov 2026 |
| [OE Digital — Dolphin sells Blackford Dolphin](https://www.oedigital.com/news/543921-dolphin-drilling-sells-blackford-dolphin-semi-sub-forges-new-rig-partnership); [Baird Maritime](https://www.bairdmaritime.com/offshore/drilling-production/blackford-dolphin-sale-to-spm) | $10m on delivery + $15m on first contract payment; SPM markets in India; Dolphin manages; built 1974, upgraded 2008 | Transaction price | 26 Oct 2026 |
| [Drilling Contractor (home page)](https://drillingcontractor.org/) | Headlines 4–11 Nov: Bergen formalised; ADNOC Kuwait; Ocean MVM Tunisia; ADES ONGC; Velesto NAGA 3; Valaris extensions (4 Nov, from its 2 Nov FSR); US Gulf demand outlook (27 Oct) | Index page | Read 12 Nov 2026 |
| [AllAfrica — Tunisia: drilling off Hammamet](https://fr.allafrica.com/stories/202611070164.html) | Ocean MVM for Tende Energy, Abiod well (Maâmoura permit) | Trade press (French) | Nov 2026 |
| [World Oil — Venus terms still under negotiation](https://www.worldoil.com/news/2026/10/15/totalenergies-namibia-still-negotiating-venus-terms-as-2026-fid-target-nears/) | Venus FID not taken; fiscal terms open | Bloomberg via trade press | 15 Oct 2026 |
| [Baird Maritime — Transocean–Valaris approvals](https://www.bairdmaritime.com/offshore/drilling-production/transocean-valaris-merger-regulatory-approvals) | All approvals (DOJ, CADE, unconditional); shareholder votes 24 Nov; Bermuda court 26 Nov; close ~1 Dec | Trade press citing the companies | Nov 2026 |
| [Zacks analyst report — RIG](https://www.zacks.com/zer/report/RIG) | Same management view as 22 Sep (> 90% in 2027, ~100 rig-years H1, ~40 tenders); Proteus/Conqueror $550m (19 Oct) | Relayed commentary `[E]`, grade C | 23 Oct 2026 |
| `docs/oil-market-bbb.md` | Brent paths, mid-cycle, long end, catalysts | Front-month futures basis | **11 Nov 2026 (full update; Base 2027 84; paths and mid-cycle otherwise unchanged; "no action" for rig)**; earlier reads 10, 17, 24 and 31 Oct |
| `docs/SED-analysis.md` | Tender-assist contracts, opex, PTTEP–Foresight evidence | Company analysis `[C]` items as tagged there | 3 Oct 2026 |

**User and secondary input assessed:**
- Hartl and Deepwater Insight are used only as `[E]`/grade C, never as sole evidence for a Base rate.
- The Norge rate conflict ($513k vs $497k) is closed at $497k (10 Oct): $149m ÷ ~300 days.
- 10 Oct user links: the Drilling Contractor article was used and verified against the primary 8-K. The Nordnet item (TDN Finans) repeats Valaris's 7 Oct release, which was already used from the primary source.
- Westwood via Riviera (15 Jun): RigLogix aggregates are used as evidence for the drillship cut together with own fixtures. It is a mid-year snapshot, so it is never the sole basis.
- The Splash247 Deepsea Mira page returned 403; its figures come from the search summary and are tagged B/`[E]`.
- 24 Oct, input assessed:
  - The orchestrator's summary of Oil BBB (24 Oct) matches the oil document.
  - Houthi and IRGC claims are kept as `[E]`/`[?]`, and only wire-confirmed items are `[F]`. Casualty counts differ between outlets; this is not material for rigs.
  - The Westwood dashboard was re-checked on 24 Oct: still the August-activity edition (labelled "September 2026", same figures).
  - Searches for offshore suspensions and evacuations returned only pre-baseline events (March–August). The absence of a report is held as `[?]`, not as evidence of normal operations.
- 28 Oct, input assessed:
  - The orchestrator's T-16 summary (30 months, ~USD 87m incl. mobilisation, ~$95k/day B, ~5-month idle gap) matches the MFN release.
  - The ~915-day divisor is an assumption (30 months); the mobilisation amount is `[?]`.
  - A Shelf Drilling "suspension effective October" item in the search results is from 2020 (High Island IV) and was rejected.
  - Ras Tanura and the pumping-station claims are `[E]`, since Saudi Arabia has not confirmed them.
- 12 Nov, input assessed:
  - The brief's "11 Nov formal signing" of Deepsea Bergen: Odfjell's Newsweb release is dated 10 Nov (06:06 UTC). The terms are as in the September LOA. Used with the primary date.
  - The oil agent's verdict ("not material for rigs") was checked against the rig rules (cover, lags, long end and mid-cycle) and holds.
  - Supply BBB's Beacon Pacific flag (from Seabreeze) was verified against the primary Odfjell and Serica releases and taken in.
  - Discovery Alert's "37 of 38 marketed HE semis committed" is an unverified industry estimate: not used. The RigLogix HE floater figure (97%, Seadrill 10-Q) is used as context instead.
  - KOC's $313.6m is a maximum value incl. mobilisation, so the derived ~$107k is an upper bound (B). The ADES values include mobilisation and options where stated, and the derived rates are tagged B with ex-mob estimates `[A]`.
  - A search result calling Transocean's $550m Proteus/Conqueror award "October" is consistent with the 19 Oct release; no new drillship award after 4 Nov was found.
