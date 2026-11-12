# Oil Market BBB — 11 November 2026

## Metadata

- **Analysis date:** Wed 11 Nov 2026, morning CET. Latest settlements are from **Tue 10 Nov** (ICE Brent via NYMEX BZ and Barchart `CB*0`; NYMEX ULSD and WTI; ICE gasoil; EEX TTF). Prints from 11 Nov are intraday and context only.
- **Status: Final.** Full update (Update mode, Steps 0–11). Skill `oil-market-bbb` revision **2026-10-24.4**.
- **Previous baseline:** 31 Oct 2026 (11 days), with a small update on 4 Nov. It was stale from 7 Nov; the planned 7 Nov follow-up never ran.
- **Window:** stub Q4-26 + 2027–2029. No roll this week. BZ F27 expires 30 Nov; ICE gasoil X26 expires ~12 Nov.
- **Why this run (causes from the update chain):**
  - Stale after 7 Nov.
  - The baseline's own 15% front trigger fired: BZ F27 settled **94.62 on 4 Nov**, −16.6% vs 113.43 on 30 Oct (threshold 96.42). It then settled 98.29 (5 Nov), 98.32 (6 Nov), 92.57 (9 Nov) and **91.49 (10 Nov, −19.3%)** `[F, Yahoo; = Barchart]`.
  - The planned 7 Nov follow-up (Kpler Hormuz week to 4 Nov, 4–6 Nov settlements) never ran.
- **Brief input checked (input, not reference):**
  - F27 94.62 on 4 Nov and 98.29 / 98.32 on 5–6 Nov: **confirmed** (Yahoo daily settlements; the 3 Nov value 103.60 matches the 4 Nov document).
  - "About 93.6 on 9 Nov": **not confirmed.** The 9 Nov settlement is **92.57** (range 90.63–98.42); 93.6 is probably an intraday print.
  - "2027 strip about 83 on 9 Nov": **82.44** on the full front mapping, so the rough read was close.
  - The other brief items are checked under Drivers.
- **Stale after 30 Nov 2026** (shorter than the 30-day rule). Reasons: OPEC+ meets on 29 Nov with 2027 quotas expected; BZ F27 expires on 30 Nov; the lame-duck strike window runs to 3 Jan. The IEA OMR (13 Nov) and the OPEC MOMR (11 Nov) are read at that run unless one revises demand by > 0.5 mb/d for a year in the window (then a full update is due at once).
- **Series (skill Benchmarks), unchanged:**
  - Brent = ICE Brent front-month futures (NYMEX BZ).
  - Diesel crack = NYMEX ULSD front × 42 − Brent front, same calendar month.
  - Jet crack = NWE jet CIF − Brent.
  - Nominal USD, period averages.
- **Data gaps:**
  - Kpler Hormuz week to 4 Nov: not found. Kpler week to 8 Nov found, but its scope (crude only, or crude and products) is not stated.
  - EIA WPSR for the week to 6 Nov not out at writing (Veterans Day week); the API figure (+9 mb crude) is from market sources.
  - FRED Dated proxy (`DCOILBRENTEU`) ends on 3 Nov.
  - OPEC MOMR (due 11 Nov) not out at writing; IEA OMR due 13 Nov.
  - No dated NWE jet crack after 16 Oct.
  - TTF read from month contracts only; quarter, season and year values are month averages `[A]`.
  - Barchart gasoil row V28 not read (interpolated `[A]`, 2028 cross-check only).
- **Oldest inputs:** IEA OMR (14 Oct); jet regrade (16 Oct); Kpler Gulf export split (data to 28 Sep).
- Tags: `[F]` fact · `[E]` external forecast or secondary · `[A]` own assumption · `[?]` unknown.

## Conclusion

- **Oil Market BBB changed: Base Brent 2027 88 → 84.** Every other Bear, Base and Bull Brent and crack path, the mid-cycle values, jet, Brent–WTI from 2027 and the weights (25/50/25, convention) stay. The stub moves mechanically.
- **Base in two sentences:** armed normalisation without a deal, with Brent **84 → 77 → 72** (mid-cycle 70), falling from ~89 in Q1-27 to ~80 in Q4-27. The ULSD crack stays at **70 → 48 → 33** (mid-cycle 25), because the product shortage outlasts the crude premium.
- **Size of the move:** −$4 (−4.5%) on one year. That is above the $3 minimum change but well below the 15% recalibration trigger. No Base path moves by more than the recalibration trigger; 2028, 2029 and mid-cycle do not move.
- **Why Base 2027 moves down (several independent data points, mostly physical):**
  - **The physical premium is gone.** Dated proxy − front futures was +20.5 (14 Oct) and +9.2 (27 Oct), but only **+2.6 (2 Nov) and +3.4 (3 Nov)** `[F, FRED/EIA spot vs Yahoo]`. A Q1-27 Base of 95 needed prompt tightness the physical market no longer shows.
  - **Supply recovers faster under the same no-deal mechanism `[E]`:**
    - EIA (STEO 10 Nov): Middle East crude shut-ins 2.5 mb/d in October (10.9 at the May peak), and Middle East output outside Iran back to pre-war by mid-2027.
    - HSBC (4 Nov): Saudi crude 8.3 mb/d in Q4-26 (from 6.3) and 9.8 in 2027 (from 8.8).
    - JPMorgan (4 Nov): Middle East exports ~20.7 mb/d in October, and a market surplus of 1.1 mb/d in September and 1.4 in October.
    - Vortexa: Gulf product loadings ~3 mb/d in October, from ~1 in May.
  - **The curve repriced and held there:** the 2027 strip fell from 89.7 (3 Nov) to 82.9 / 83.6 / 85.0 / 82.4 / **81.2** (4–10 Nov), and the whole 2027–2029 curve moved down.
  - **The agency's comparable path is lower:** the EIA's case (Iran constrained, the rest of the Gulf normalising) gives Brent **$86 for 2027 on a spot basis**, ≈ $84 on the futures basis `[A]`.
- **Why not more, and why not Bear:**
  - **No deal is signed**, and Iran says it is not negotiating.
  - **The strait is still contested:** Kpler counts Hormuz oil at 7.82 mb/d in the week to 8 Nov, ~46% of pre-war. Ships were hit on 10 Nov, and Houthi missiles damaged the Aramco Tower in Riyadh on 8 Nov.
  - **US stocks are low:** commercial crude was 410 mb at end-October, the lowest end-October since 2014 (EIA).
  - **The EIA raised** its 2027 Brent by $2 and its 2027 diesel price by 12%.
  - The cut is therefore front-loaded: Q1-27 95 → 89, Q4-27 82 → 80; 2028 stays 77.
- **The three rules from 31 Oct / 4 Nov:**
  - **Conditional up-rule (31 Oct): void.** It needs the 2027 strip ≥ 93, and the strip is 81.2. The Hormuz flow signpost (< 8 mb/d) was touched a second time (7.82, week to 8 Nov), but the series differs from the 28 Oct one (7.3, crude) and the week to 4 Nov is missing.
  - **Downside retest rule (< 83 for a week without a signed deal): not formally met.** The strip was below 83 on 3 of 5 sessions (4, 9, 10 Nov), with a 4–10 Nov average of 83.03. The full update tested Base anyway: the 10 Nov gap (−6.8) exceeds $5, it could not be explained away, and Base 2027 moves −4.
  - **Bear catalyst (a signed and holding deal): not met.** Base stays the no-deal case and is not re-centred to a Bear outcome. New retest rules are in the monitoring table.
- **Main Bear catalyst:** a durable Iran–USA deal plus OPEC+ market-share quotas. It is **closer, not triggered:**
  - On 9 Nov Trump held off new strikes after appeals from Qatar's PM, said the war would end "fairly soon", and called renewed war "highly unlikely" while talks progress.
  - A Democratic Congress from 3 Jan adds pressure.
  - New enabler: Russia–Ukraine talks resumed in Abu Dhabi on 10 Nov, the first since February. Sanctions relief would add Russian barrels.
- **Main Bull catalyst:** renewed strikes with retaliation against Gulf energy infrastructure. It is **further away** (strikes on hold), but the tail is live: attacks on ships continue, the Houthis hit Riyadh, the blockade stays, and the window runs to 3 Jan.
- **Diesel: crack paths unchanged.**
  - The crack held while crude fell: the front crack (same contracts) was 83.0 on 30 Oct and 82.0 on 10 Nov, while Brent fell $21.9.
  - **A refining trigger fired:** Ukrainian drones disrupted ~30% of Russian refining capacity (2.2 mb/d nameplate at nine plants; runs cut by up to ~1.5 mb/d; Reuters, 10 Nov).
  - Tested: it supports the Base and Bull crack against Bear, and the EIA now expects wider cracks in 2027. But the 2027 crack forward fell 2.7 to 67.8 and Russia plans larger diesel exports, so no path moves.

## Interface (point values; ranges in the sections below)

| $/bbl, period average | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| Brent Bear / Base / Bull | 97.1 / 97.1 / 97.1 | 65 / **84** / 118 | 60 / 77 / 102 | 60 / 72 / 90 | 60 / 70 / 82 |
| Diesel crack Bear / Base / Bull | 85.1 / 85.1 / 85.1 | 35 / 70 / 110 | 25 / 48 / 75 | 20 / 33 / 45 | 18 / 25 / 35 |
| Diesel price Base ($/bbl; $/t) | 182.2; 1,357 | 154; 1,147 | 125; 931 | 105; 782 | 95; 708 |
| Jet crack Base | `[?]` | 60 | 40 | 28 | 22 |
| Brent–WTI Base | 7.0 | 6.0 | 5.0 | 4.5 | 4.0 |
| Forward curve, 10 Nov (Brent / diesel crack) | 97.1 / 85.1 | 81.2 / 67.8 | 73.9 / 45.2 | 71.2 / 37.7 | — |

- **Changed vs 4 Nov:** Brent Base 2027 88 → **84**; stub Brent 104.3 → **97.1**, stub crack 88.1 → **85.1**, Brent–WTI stub 8.0 → **7.0**; diesel price Base stub 192.4 → 182.2 $/bbl and 2027 158 → 154 $/bbl (1,177 → 1,147 $/t).
- Forward curve on 3 Nov (previous): 104.3 / 88.1 · 89.7 / 70.5 · 79.1 / 47.2 · 74.6 / 41.5.
- 11 Nov intraday (context only, not settlements): F27 ~92.0 (+0.5); the 2027 months are +0.1 to +0.4.

**Stub (10 Nov settlements), identical across scenarios:**
- **Brent 97.1:**
  - October 108.34 (actual).
  - November 93.55: seven settlements (2–10 Nov: 104.77 / 103.60 / 94.62 / 98.29 / 98.32 / 92.57 / 91.49), then F27 91.49 for the remaining 14 of 21 trading days.
  - December 89.45 (G27).
- **Crack 85.1:**
  - October 92.85 (actual).
  - November 82.49: daily HO Z26 − BZ F27 80.94 / 86.69 / 82.01 / 84.49 / 83.61 / 84.45 / 82.01, then 82.01.
  - December 79.98 (HO F27 − BZ G27).
- **Brent–WTI 7.0:**
  - October 10.35.
  - November 5.95: daily BZ F27 − CL Z26, then 5.45.
  - December 4.59 (BZ G27 − CL F27 84.86).
- **Mechanical move:** Brent 104.3 → 97.1; crack 88.1 → 85.1; Brent–WTI 8.0 → 7.0.

## Scenario definitions

The catalysts and mechanisms are those of 24 Oct, tested again in this run. Changes on 11 Nov:
- **Bear:** a new supply enabler, Russia–Ukraine sanctions relief (talks resumed on 10 Nov).
- **Base:** the mechanism now cites the EIA's recovery timing.
- **Bull:** "Earliest" notes that strikes have been on hold since 9 Nov.

Signpost status is in the monitoring table.

| Scenario | Weight (convention) | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|
| **Bear** | 25% | **Supply:** durable Iran–USA deal (blockade lifted, Iranian barrels back) and OPEC+ 2027 quotas set for market share. **Enablers:** Democratic Congress from 3 Jan 2027 presses to end the war through funding and war-powers votes; **(11 Nov)** a Russia–Ukraine settlement with sanctions relief adds Russian crude and products. **Products:** Russia restores diesel exports faster than its refinery repairs suggest. **Demand:** recession after the energy shock | The agencies' 4–5 mb/d 2027 surplus materialises. Stocks rebuild quickly and the curve flips to contango. Gulf, Russian and Chinese product exports return and the crack collapses towards its normal band | Q1 2027 (a deal could be signed in Nov–Dec 2026; barrels follow after mine clearance and insurance) | Ceasefire signed and holding > 60 days · Brent M1−M4 < $2 · Dec-27 < $70 · ME refined-product exports (IEA) > 3.3 mb/d · Russian diesel exports > 0.6 mb/d · PMIs < 48 |
| **Base** | 50% | Armed normalisation: war without a deal; crude moves mostly via bypass and escort, with the Gulf and Gulf of Oman contested; product shortage persists into 2027 | ME crude to market ~15–16 mb/d (ME oil incl. bypass ~22–24 mb/d), mostly via East–West/Yanbu and escorted shuttles. Hormuz itself is volatile. ME output outside Iran back near pre-war by mid-2027 (EIA assumption, 10 Nov); Iran stays constrained. Gulf product exports are repaired gradually through 2027. China exports at or below quota; Russian exports recover only as refineries are repaired. ~1 bn bbl of restocking absorbs much of the 2027 surplus | Ongoing | ME crude incl. bypass ≥ 15 mb/d · East–West pipeline ≥ 5 mb/d · ME refined-product exports (IEA) towards ~2.6 mb/d by mid-2027 · China monthly quotas ~3.5–4 Mt · ULSD crack < $65 by mid-2027 |
| **Bull** | 25% | **Supply:** renewed US (or joint US–Israeli) strikes; Iranian/Houthi retaliation against Ras Tanura/Abqaiq/Khurais/East–West/Yanbu/Fujairah; escort and ship-to-ship system fails. **Products:** China cuts quotas again; Russian repairs fail under renewed strikes | 3–5 mb/d of crude lost again with stocks still low, so price must ration demand. Product shortage deepens; record Dated premium | Window mostly in the lame duck to 3 Jan 2027. Strikes on hold since 9 Nov (Trump, after the Qatar meeting); limited strikes without energy retaliation (Qeshm, 2 Nov) are not this catalyst | Hormuz crude < 8 mb/d for two weeks · East–West pipeline down again · ME crude incl. bypass < 13 mb/d · Saudi production or export facility hit with lasting loss · Gulf of Oman ship-to-ship/escort shuttle suspended · ULSD crack > $100 sustained · Dated–futures > $30 sustained · China monthly quota < 2 Mt |

## Brent ($/bbl) — point (range)

| Scenario | Stub | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|
| Bear | 97.1 | 65 (60–70) | 60 (55–65) | 60 (55–65) | 61.7 | 60 (55–65) |
| **Base** | **97.1** | **84 (77–91)** | **77 (70–85)** | **72 (65–80)** | **77.7** | **70 (65–75)** |
| Bull | 97.1 | 118 (105–130) | 102 (90–115) | 90 (80–100) | 103.3 | 82 (75–90) |

- Previous Base 2027: 88 (81–95); previous Base 3-yr average 79.0.

**Anchors (11 Nov):**
- **Forward (10 Nov settlements, full-year front mapping) `[F]`:** **81.2 / 73.9 / 71.2.** Base is $2.8, $3.1 and $0.8 above it. Every gap is below $5.
  - On 3 Nov the forward was 89.7 / 79.1 / 74.6: −8.5 / −5.3 / −3.4 in a week.
  - The 2027 quarters are 86.2 / 82.4 / 79.3 / 77.0, a $9.2 slope (was $12.6).
- **EIA STEO (10 Nov; model completed 5 Nov; spot basis) `[E]`:**
  - 2026 $97; **2027 $86** (October STEO $84); about $100 for November–December; below $90 in Q2-27; **$77 in Q4-27**.
  - Base 84 is $2 below the EIA. On a futures basis the EIA path is nearer $84 `[A]`, because the EIA's spot is a Dated-type assessment that carried a premium all autumn (October spot $124 against ~$108 futures).
- **Other houses `[E]`:**
  - JPMorgan sees a surplus since September (above); no new price forecast found.
  - FGE (Fesharaki, 10 Nov) sees no deal.
  - Goldman (17 Sep note, via search summary): 2027 about $87 in a disruption case and $64 in a peace case.
  - Older views (HSBC $85, Sep; Wood Mackenzie ~$78, Jun; Citi $65, undated) carried.

**Test of Base (Step 8):**
- **What would make Base 88 wrong, and do we see it?** A premium the physical market does not confirm, and a supply recovery faster than Base assumed. **Yes, both:**
  - Dated − futures is +3.4 (3 Nov), against +20.5 on 14 Oct.
  - EIA shut-ins are down to 2.5 mb/d, and the EIA puts Middle East output outside Iran back by mid-2027.
  - HSBC raised its Saudi output path by 1–2 mb/d.
  - JPMorgan counts a surplus.
  - The forward sat at or near 83 for five sessions and closed at 81.2.
  - These are independent of each other (physical prices, agency, bank, futures).
- **What would make a lower Base wrong?** A renewed loss of barrels. Not seen:
  - Kpler Hormuz oil is 7.82 mb/d (week to 8 Nov) against 7.3 (crude, week to 28 Oct); no fall.
  - No Saudi facility has lost output.
  - US crude stocks were low but stopped drawing (API +9 mb, unverified).
- **Size:** −$4 to 84. The cut sits in H1-27, where the premium was: Q1 95 → 89, Q4 82 → 80.
  - A larger cut (to the strip, 81) would price part of a deal into the no-deal case.
  - 2028 (77, forward 73.9) and 2029 (72, forward 71.2) do not move. The evidence for them is only the curve, and the gaps (−3.1, −0.8) are below $5.
- **Why Base sits $2.8 above the strip `[A]`:**
  - The strip blends outcomes: with strikes on hold and Qatar mediating, it prices part of a Bear outcome, which Base excludes by definition.
  - On 31 Oct the strip sat $6.3 above Base for the mirror reason (escalation premium).
  - Base 84 is now in line with the EIA's comparable no-deal path.
- **Range 77–91:** a stop-start blockade with occasional hits (upper half) or quicker Gulf normalisation without a signed deal (lower half). The 10 Nov forward (81.2) is inside it.

**Mid-cycle 70 (unchanged) `[A]`:**
- **10 Nov settlements `[F, ICE via Barchart]`:** Dec-30 **69.06**, Dec-31 **67.70**, Dec-34 **64.24**, H35 64.05.
- The sell-off faded with maturity: Dec-27 −7.2, Dec-28 −4.6, Dec-29 −2.9, Dec-30 −1.6 and Dec-31 −0.6 vs 3 Nov, while Dec-34 rose +0.9. The long end did not price a structurally lower world.
- Brent's 2015–2025 median is ~$66; marginal non-OPEC full-cycle cost is $60–65 WTI `[E]`. We add a post-war structural premium (restocking, higher risk inventories).

## Year 1 by quarter ($/bbl)

Shape from the **10 Nov** forward, rescaled (multiplicatively) to each scenario's 2027 average:
- Brent 86.2 / 82.4 / 79.3 / 77.0 (3 Nov: 96.5 / 91.3 / 87.1 / 83.9). The slope flattened from $12.6 to $9.2.
- Crack 76.3 / 68.9 / 65.2 / 60.7 (3 Nov: 80.4 / 71.6 / 67.5 / 62.5).

| Scenario | Brent Q1 / Q2 / Q3 / Q4 | Diesel crack Q1 / Q2 / Q3 / Q4 |
|---|---|---|
| Bear | 69 / 66 / 63 / 62 | 39 / 36 / 34 / 31 |
| **Base** | **89 / 85 / 82 / 80** | **79 / 71 / 67 / 63** |
| Bull | 125 / 120 / 115 / 112 | 124 / 112 / 106 / 98 |

- The quarters average to the annual values (65 / 84 / 118 and 35 / 70 / 110).
- Previous rows (3 Nov shape; Base 88), Brent: Bear 70/66/63/61, Base 95/90/85/82, Bull 127/120/115/110.
- Previous rows, crack: Bear 40/36/33/31, Base 80/71/67/62, Bull 126/112/105/97.

## Distillate cracks ($/bbl) — point (range)

| Scenario | Diesel (ULSD−Brent) 27 / 28 / 29 / mid-cycle | Jet (NWE−Brent) 27 / 28 / 29 |
|---|---|---|
| Bear | 35 (25–45) / 25 (18–32) / 20 (15–25) / 18 (14–22) | 30 (20–40) / 21 (15–28) / 16 (12–22) |
| **Base** | **70 (58–82) / 48 (38–58) / 33 (25–44) / 25 (20–30)** | **60 (45–75) / 40 (30–50) / 28 (20–35)** |
| Bull | 110 (90–130) / 75 (55–90) / 45 (35–55) / 35 (28–40) | 105 (80–130) / 70 (50–85) / 40 (30–50) |

- **Historical band, ULSD−Brent (quarter-end 2015–2025) `[F]`:** median $18, interquartile range $14–24; the crisis years 2022–23 averaged $47.
- **Forward vs Base (10 Nov settlements) `[F]`:**
  - 2027: forward **67.8** vs Base 70 (−2.2). Q1 76.3 → Q4 60.7.
  - 2028: 45.2 vs 48 (−2.8).
  - 2029: 37.7 vs 33 (+4.7).
  - Every 2029 HO month still has zero open interest (Z29 64 lots), and on 10 Nov they all moved by the same −2.86 ¢/gal. The 2029 settlement is an extrapolated mark, so the 24 Oct explanation of the gap holds. The retest signpost (OI > 1,000 lots at > $40) is not met.
  - The front crack held while crude fell: HO Z26 − BZ F27 was 82.97 on 30 Oct and **82.01** on 10 Nov.
- **Test of the crack path (Step 8):**
  - **For a higher crack:**
    - EIA (10 Nov) raised 2027 retail diesel from $4.49 to $5.03/gal (+12%) while raising Brent by only $2, and expects "wider product crack spreads in 2027" `[E]`. That is roughly +$20/bbl on its 2027 diesel margin `[A]`.
    - Russian refining was cut by up to ~1.5 mb/d of runs (Refining below).
    - Gulf product exports are still ~half of normal.
  - **For a lower crack:**
    - The traded 2027 crack fell 2.7 in a week.
    - Russia plans ~2.15 Mt of diesel exports in November (from ~0.5 Mt).
    - ARA gasoil imports rose to 400 kb/d.
    - The switching support faded (TTF −18%).
  - **Result:** the evidence points both ways, and the forward sits within $3 of Base for 2027–28. The crack paths are kept.
- **Gasoil cross-check (ICE gasoil, Barchart `LF*0`, settlements 10 Nov; mapping LF(m+1) ÷ 7.45 − BZ(m+2)) `[F]`:**
  - Front: LFZ26 $1,227.75/t = $164.8/bbl, minus BZ F27 91.49 = **73.3**, vs ULSD 82.0 for the same month (Europe −8.7).

    | $/bbl | Nov–Dec 26 | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2027 | 2028 (Jan–Nov) |
    |---|---|---|---|---|---|---|---|
    | Gasoil − Brent | 71.7 | 65.5 | 58.1 | 52.5 | 47.1 | 55.8 | 35.6 |
    | ULSD − Brent | 81.0 | 76.3 | 68.9 | 65.2 | 60.7 | 67.8 | 45.7 |
    | Gap (Europe − US) | −9.3 | −10.8 | −10.8 | −12.7 | −13.5 | −12.0 | −10.1 |

  - 30 Oct (previous): gasoil 2027 60.3 vs ULSD 72.0 (−11.7); 2028 38.7 vs 49.3 (−10.6).
  - **Reading `[A]`:** unchanged. The US is the tighter distillate market by $9–14 through 2028.
    - Base 70 (ULSD basis) is $2 above the ULSD curve and $14 above gasoil.
    - Downstream analyses that price European diesel should keep applying about −$11 to the ULSD crack for 2027–28.
    - The 2028 gasoil months are thin; V28 is interpolated.
- **Gas-to-oil switching (context, extra support):**
  - **Inputs:**
    - EEX TTF month futures, 10 Nov settlements `[F, Barchart]`: Dec-26 84.710, Jan-27 84.549, Feb 84.125, Mar 80.802, Apr 68.200, May 64.845, Jun 62.709, Jul 62.134, Aug 61.518, Sep 60.981, Oct 59.478, Nov 59.199, Dec-27 59.004 €/MWh.
    - Q1, Summer and Cal-27 are month averages `[A]` (the quarter, season and year contracts were not read).
    - ICE gasoil 10 Nov `[F, Barchart]`.
    - EUR/USD **1.1214** = EURNOK 10.6155 ÷ USDNOK 9.4663 `[F, Norges Bank, 10 Nov]`.
    - 11.94 MWh/t; gasoil months mapped LF(m+1).

    | Period | Gasoil €/MWh | TTF €/MWh | Ratio | Band | 30 Oct |
    |---|---|---|---|---|---|
    | Dec-26 (LFF27 vs TTF Dec) | 88.8 | 84.7 | **1.05** | Partial switching | 0.99 |
    | Q1-27 (LFG/H/J27 vs TTF Jan–Mar) | 84.4 | 83.2 | **1.02** | Partial switching | 0.95 |
    | Summer-27 (LFK–V27 vs TTF Apr–Sep) | 75.7 | 63.4 | 1.19 | Partial switching | 1.12 |
    | Cal-27 (LFG27–F28 vs TTF Jan–Dec) | 76.2 | 67.3 | 1.13 | Partial switching | 1.06 |

  - **Reading `[A]`:**
    - TTF fell ~18% (Dec-26 103.8 → 84.7) as the Hormuz risk to Qatari LNG eased, faster than gasoil fell. Gas is no longer dearer than gasoil for the winter.
    - The context signpost (ratio < 1.0) is **no longer crossed**.
    - The 31 Oct retest condition (ratio < 1.0 for two weeks while the ULSD Q1-27 forward is > 80) is **not met** (1.02; Q1 crack 76.3), so the H1-27 crack quarters do not lean higher.
    - Switching volume is not quantified `[?]`, and the EUA price is not sourced `[?]`.
- **Jet:** kept at 60 / 40 / 28, low confidence.
  - S&P Global Platts (19 Oct, via search summary, not opened) `[E]`: the European jet crack moved above the diesel crack, by up to $11.75/bbl on 16 Oct (jet FOB FARAG barge vs ULSD FOB barge).
  - Cross-check `[A]`: the 2027 European gasoil crack is 55.8, and a positive but fading regrade puts NWE jet near 60, consistent with Base.
  - Russian jet exports are banned to 30 Nov.

## Distillate sensitivity

**Diesel price = Brent + ULSD crack**, $/bbl ($/t at 7.45 bbl/t). The Base Brent row changes with Base 2027 = 84.

2027:

| Brent \ crack | Bear 35 | Base 70 | Bull 110 |
|---|---|---|---|
| Bear 65 | 100 (745) | 135 (1,006) — *consistent: deal restores crude, products stay short* | 175 (1,304) — *plausible: product-led shortage* |
| Base 84 | 119 (887) | **154 (1,147)** | 194 (1,445) |
| Bull 118 | 153 (1,140) — *unlikely: crude shock without product shortage* | 188 (1,401) | 228 (1,699) |

3-year average 2027–2029:

| Brent \ crack | Bear 26.7 | Base 50.3 | Bull 76.7 |
|---|---|---|---|
| Bear 61.7 | 88 (658) | 112 (834) | 138 (1,031) |
| Base 77.7 | 104 (777) | **128 (954)** | 154 (1,150) |
| Bull 103.3 | 130 (968) — *unlikely* | 154 (1,145) | 180 (1,341) |

- Previous Base rows (Base 88; 3-yr 79.0): 2027 123 (916) / 158 (1,177) / 198 (1,475); 3-yr 106 (787) / 129 (963) / 156 (1,160).

**Decomposition of the ULSD price change** (front month, Yahoo settlements) `[F]`:

| Period | Δ ULSD | Δ Brent | Δ Crack |
|---|---|---|---|
| Pre-war (27 Feb) → 10 Nov (front series HO Z26 / BZ F27) | +61.4 | +19.0 (31%) | +42.4 (69%) |
| 30 Oct → 10 Nov, same contracts (HO Z26 / BZ F27) | −22.9 | −21.9 | −1.0 |
| 3 Nov → 10 Nov, same contracts | −16.8 | −12.1 | −4.7 |
| Pre-war (27 Feb) → 3 Nov (front series HO Z26 / BZ F27) | +78.2 | +31.1 (40%) | +47.1 (60%) |
| Pre-war (27 Feb) → 30 Oct | +89.1 | +45.1 (51%) | +43.9 (49%) |

**Reading (11 Nov):**
- The sell-off since 30 Oct came almost entirely out of crude: Brent −21.9, crack −1.0.
- The crude share of the war-time diesel rise fell from 51% (30 Oct) to 31%.
- The market priced out the crude risk premium but not the product shortage. That fits the Russian refinery outages, half-normal Gulf product exports and the EIA's higher diesel path, and it is why the Brent path moves while the crack path stays.

## Drivers

### Crude supply (incl. disruptions in barrels reaching market)

**Full update 11 Nov**

- **Iran–USA diplomacy (Bear side) `[E]`:**
  - **9 Nov:** Trump met Qatar's PM, Sheikh Mohammed bin Abdulrahman, at the White House. Afterwards he said he would hold off new strikes after appeals from regional leaders.
    - Quotes: "I think it's going to be ending fairly soon" and "Iran militarily is effectively over".
    - He said Tehran is "talking very politely", and that the Gulf states "prefer the status quo", i.e. the blockade (CNBC, The National, 10 Nov).
    - He told CNN a return to war was "highly unlikely" while talks on the nuclear file and Hormuz progress (via several reports, not opened).
  - **The blockade stays** (Trump; IG, 10 Nov).
  - **Hormuz plan:**
    - Two diplomatic sources said Iran approved a plan to reopen the strait and appeared to drop its demands to control it and to charge tolls.
    - A Qatari official called the reported details "inaccurate" and said the US and Iran were still discussing details with mediators (9 Nov; TokenPost, 10 Nov, no wire named).
    - Talks still rest on Iran's seven-step plan of September.
  - **Iran:** the security official Rezaei says Tehran is not negotiating with Washington and the strait stays closed unless US terms are met (via search summaries). An Iranian security official told Reuters that no talks were taking place (11 Nov).
  - **FGE (Fesharaki):** the gap "cannot be bridged" (CNBC, 10 Nov).
  - **No signed deal as of 11 Nov.**
  - **Brief items:**
    - "Strikes highly unlikely if talks progress": **confirmed** in substance.
    - "Iran dropped its toll demand, denied by a Qatari official": **partly confirmed.** The Qatari official called the reported details inaccurate; a denial aimed at the toll element itself was not found.
    - "No signed deal as of 9 Nov": **confirmed**, and still none on 11 Nov.
- **Attacks and escalation (Bull side) `[E]`:**
  - **10 Nov:** UKMTO reports a tanker struck north-east of Lima, Oman. The IRGC Navy says two tankers caught fire after hitting mines on an "unauthorized route"; an Iranian headline later says five tankers and a tug (unverified) (Reuters, 11 Nov).
  - **WINEP:** 37 ships attacked in October, the most of the war, and "little sign" of fewer in November.
  - **US strikes:** a further round of "minor" US strikes on air defences near the strait is reported (CNBC/CBC). Whether it is the 2 Nov Qeshm strike or a new one is not clear `[?]`. There was no retaliation against energy infrastructure.
  - **8 Nov, Houthi missiles on Riyadh:**
    - Falling debris caused minor damage to the **Aramco Tower** (an administrative building in KAFD), with no injuries (Saudi Energy Ministry).
    - A missile toward the Eastern Province was intercepted. The coalition struck launchers in Saada.
    - The Houthis claim six operations against Aramco facilities, Riyadh airport and military sites (CNN, Middle East Eye).
    - **No production or export loss is reported.**
- **Flows `[E]`:**

  | Source | Scope | Value | Period |
  |---|---|---|---|
  | Kpler (The National, 10 Nov) | Hormuz oil flows excl. Iran; scope (crude only or incl. products) not stated | **7.82 mb/d**, ~46% of a pre-war 17.14 | Week to 8 Nov |
  | Kpler (CNBC, 30 Oct; carried) | Hormuz crude | 7.3 | Week to 28 Oct |
  | Kpler | Hormuz crude | not found `[?]` | Week to 4 Nov |
  | Kpler (carried) | Gulf crude + condensate via Hormuz, Red Sea and Gulf of Oman | 16.1 (Sep 17.09) | October |
  | Vortexa (carried) | Gulf seaborne crude + condensate / products | 14.0 / 3.1 | October |
  | FGE (Bloomberg, 10 Nov) | Gulf crude incl. pipelines / products, share of pre-war | 80–85% / 35–40% | Early November |
  | EIA STEO (10 Nov) | ME crude shut-ins | 2.5 mb/d (peak 10.9 in May), flat to end-2026 | October |
  | JPMorgan (4 Nov) | ME oil exports | ~20.7 (March low 9.8) | October |

  - The 7.82 and 7.3 figures are not like-for-like: the pre-war bases differ (17.14 vs 13.5–16).
  - LSEG (10 Nov): even after a deal, flows depend on mine clearance and insurance.
- **ME crude incl. bypass (Bull < 13, Base ≥ 15) `[A]`:**
  - Kpler October **16.1**, so Base is met on the monthly figure.
  - Vortexa (14.0) and FGE (80–85% of a ~16.5–17 pre-war, ≈ 13–14.5) are lower.
  - The composite is **Base on Kpler and borderline on the other trackers**. None is below the Bull line.
- **Saudi Arabia `[E]`:**
  - HSBC (4 Nov): Aramco crude Q4-26 8.3 mb/d (from 6.3) and 2027 9.8 (from 8.8), ~10 by mid-2027.
  - EIA: the East–West pipeline has restarted, and Middle East exports rose slightly in October.
  - No East–West throughput figure since 6 Oct (5.8 mb/d) `[?]`.
  - October exports by tracker (carried): Kpler 5.4, Vortexa ~6.5, TankerTrackers 6.99.
- **OPEC+ `[F/E]`:** no change since the 1 Nov hold (the seven at 31.01 mb/d for December). The next meeting, **29 Nov**, is expected to set the 2027 quotas. EIA: OPEC liquids 24.5 mb/d in 2026 (from 23.9) and 28.4 in 2027 (from 29.2).
- **Russia `[E]`:**
  - Russia–Ukraine talks were held in Abu Dhabi on 10 Nov, the first since February (Reuters). Sanctions relief is a Bear enabler (Scenario definitions).
  - A drone fire at the Ust-Luga port injured three on 11 Nov. The loading effect is not stated `[?]`.
  - The refinery outages are covered under Refining.
- **US `[E]`:** crude production 13.9 mb/d in 2026 and a record 14.3 in 2027 (EIA, 10 Nov).
- **For BBB `[A]`:**
  - No barrels returned in November beyond the October levels, and none were lost.
  - The evidence that moves Base is the outlook: a faster recovery outside Iran (EIA, HSBC) and the collapse of the physical premium. Diplomacy enters only through the Bear catalyst's timing.

**Carried from 31 Oct / 4 Nov:**
- **OPEC+ 1 Nov:** per-country December targets held. The 1.65 mb/d of 2023 voluntary cuts are fully unwound; the 2 mb/d of 2022 cuts stay to end-2026.
- **Iraq:** Basrah ~3.0 mb/d in October. **Iran:** oil on water outside the blockade zone is zero (Kpler, 28 Oct). **Libya:** the Hamada–Zawiya valve shut (~31 Oct), volume not stated `[?]`.
- **US midterms (3 Nov):**
  - Democratic House and Senate, seated on 3 Jan 2027, without a veto-proof majority. The FY27 stopgap expires on 11 Dec.
  - No law changes for oil before 3 Jan. From then, funding and war-powers pressure builds (a Bear enabler). US production policy is unchanged; SPR ~282.6 mb with no refill funding.

### Demand

- **EIA STEO (10 Nov) `[E]`:**
  - World consumption 102.4 mb/d in 2026 (−2.0 y/y) and **104.4** in 2027 (+2.0). The 2027 figure is revised −0.2 (October 104.6), below the 0.5 trigger.
  - World GDP 3.1% in 2026 and 2027.
- **JPMorgan (4 Nov):** demand −3.3 mb/d since the war began `[E]`.
- **IEA (Oct, carried):** 102.4 (2026, −2.6) and ~104.4 (2027, +2.0). **OPEC (Oct, carried):** 105.7 / 108.3, with 2027 growth ~2.55 mb/d. The OPEC MOMR is due 11 Nov and the IEA OMR on 13 Nov.
- **US:** October CPI came in hotter than expected (10 Nov, AP) and raises the chance of a Fed hike. It is a demand-side tail for the Bear case; no path change.
- **Price effect:** front Brent at $91–98 and diesel at ~$174–190/bbl in November still mean demand destruction in Q4-26, though less than in October ($108 Brent, ~$200 diesel).

### Inventories

- **US `[E/F]`:**
  - EIA STEO: commercial crude **410 mb at end-October, the lowest end-October since 2014**; it stays below the 5-year average until mid-2027.
  - API, week to 6 Nov: crude **+9 mb** (market sources via Reuters, 11 Nov; **unverified**).
  - The EIA WPSR for that week was not out at writing `[?]`.
  - Last EIA week (to 30 Oct, carried): crude −0.87 to 409.8 mb; distillate −3.6 to 99.3 mb, ~13% below the 5-year average; utilisation 94.5%.
- **Global `[E]`:**
  - EIA: stocks drew 1.2 mb/d in 3Q26, start to build in 4Q26, and build 3.5 mb/d in 1H27.
  - IEA (Sep, carried): −509 mb vs pre-war; observed −10 mb in September.
- **ARA `[E]`:**
  - Gasoil imports were **400 kb/d** in November to date vs 257 kb/d in October: India 39%, Saudi Arabia 35%, Canada 12% (Vortexa via ENGINE, 6 Nov).
  - No November stock level was found `[?]`; the last is the week to 15 Oct (gasoil 1,782 kt, jet 494 kt).
- **Singapore:** no data `[?]`.
- **China:** no data `[?]`. Bloomberg (10 Nov): diesel exports may stay curbed by low domestic stocks.
- **Reading `[A]`:** US crude is low but stopped drawing (API, unverified), and Europe is drawing more imports. Stocks are no longer tightening at the margin, which fits a lower H1-27 Base. The distillate stock deficit is intact, which fits an unchanged crack.

### Refining and distillate supply (incl. regional balances in mb/d)

- **Russia (refining trigger) `[E]`:** renewed Ukrainian drone strikes since late October have disrupted ~**30%** of capacity (Reuters, 10 Nov, two industry sources).
  - Nine of 35 major refineries were hit in a week (Ryazan, Yaroslavl and Volga plants).
  - Nameplate ~300 kt/d (**2.2 mb/d**) out of ~930 kt/d. Runs were ~700 kt/d (~5.1 mb/d) at end-October. The actual processing cut is **up to 200 kt/d (~1.5 mb/d** at 7.33 bbl/t).
  - Kirishi (the second-largest refinery) was set on fire on 9 Nov.
  - Several regions report fuel shortages and petrol rationing.
  - A Trump-announced energy-strike ceasefire did not take hold at end-October.
- **Russian diesel exports `[E]`:**
  - About 2.15 Mt is planned for November (~0.52 mb/d) vs ~0.51 Mt in October (Kyiv Post, citing Kpler/LSEG tanker data). Novak: up to 3.5 Mt by end-2026.
  - Diesel tankers are dropping their US destinations (Al Jazeera, 7 Nov).
  - The quota decree has not been seen `[?]`.
- **Barrels `[A]`:**
  - A ~1.5 mb/d run cut at a ~35–40% diesel yield is ~0.5–0.6 mb/d less Russian diesel output while it lasts. Earlier strikes were repaired in 2–6 weeks.
  - The quota plan points the other way for exports. Russian crude that cannot be refined goes to export, which is crude-bearish and crack-supportive.
  - **Trigger "refining capacity > 0.5 mb/d": fired.** Tested under Distillate cracks: no path change.
  - The Bear product signpost (Russian diesel exports > 0.6 mb/d) is **not crossed**.
- **Gulf:** no verified refinery outage. Gulf product loadings were ~3 mb/d in October, half of pre-war (Vortexa) `[E]`.
- **EIA (10 Nov) `[E]`:** product markets face "continued supply constraints" through end-2027, and wider 2027 cracks should keep US refinery runs elevated. 2027 retail diesel is $5.03/gal (from $4.49).
- **China:** third 2026 quota batch 4.55 Mt (9 Oct, carried). The Bull signpost (< 2 Mt/month) is far away.
- **US (4 Nov WPSR, carried):** utilisation 94.5%; distillate −3.6 mb.
- **Freight and price effects** (rates are covered in [[oil-shipping-bbb]]):
  - **Brent–WTI:** November same-month **5.45** (BZ F27 − CL Z26, 10 Nov), from 9.31 on 31 Oct.
  - The 2027 strip spread is **3.9** (mid-quarter shortcut: Feb 4.13, May 3.87, Aug 3.72, Nov 3.83); it was 4.85 (full year) on 3 Nov. The freight premium in the crude spread is fading.
  - No freight cost was re-read (VLCC Gulf of Oman → Asia ~$21/bbl in October, carried) `[?]`.
  - **Regional crude:** no Murban–Dubai figure `[?]`.
- **Regional balance:** unchanged. Europe imports ~1.5 mb/d of diesel (about half from the US), and the US–Europe crack gap of $9–14 keeps the transatlantic arbitrage open.

### Forward curve (M1−M4, classification, long end, Dated–futures spread)

- **Brent M1−M4 (10 Nov) `[F]`:**
  - F27 91.49 − K27 84.79 = **+$6.70 → Clearly tight.** The regime is unchanged.
  - The spread narrowed from +12.82 (30 Oct) and +8.99 (3 Nov). Daily: +7.87 (4 Nov), +10.30, +8.88, +6.66, +6.70.
  - With US crude stocks no longer falling (API, unverified), the reading moves from "strong physical tightness" towards "backwardation, inventories building: normalisation may be under way".
  - A spread below $5 for two weeks would be a regime change (recalibration trigger).
- **Long end (ICE Brent via Barchart `CB*0`, 99 months to H35, 10 Nov settlements) `[F]`:**

  | Contract | 10 Nov | 3 Nov | 30 Oct |
  |---|---|---|---|
  | Dec-27 | 77.64 | 84.88 | 88.11 |
  | Dec-28 | 72.76 | 77.38 | 78.96 |
  | Dec-29 | 70.58 | 73.49 | 74.34 |
  | Dec-30 | 69.06 | 70.65 | 71.06 |
  | Dec-31 | 67.70 | 68.27 | 68.29 |
  | Dec-34 | 64.24 | 63.34 | 62.83 |

  - Dec-27 is −11.9% vs 30 Oct (trigger 15%); Dec-28 −7.9%; Dec-29 −5.1%.
  - The curve flattened, and the long end from 2031 is unchanged or higher.
- **Overlap check:**
  - Barchart CB 10 Nov settlements equal Yahoo BZ for every month both carry (F27–H28, Z28) `[F]`.
  - Barchart HO equals Yahoo HO for every shared month (Z26–F28, Z28).
  - Barchart rows still trading on 11 Nov (F27–Z27, M28, Z28, M29, Z29) were read as last price − change = 10 Nov settlement, and they match Yahoo.
- **WTI (Yahoo, 10 Nov):** Z26 86.04 · F27 84.86 · H27 82.03 · M27 78.48 · U27 75.52 · Z27 73.12 · Z28 68.74 · Z29 66.24.
- **Diesel crack forward (full-year front mapping) `[F]`:** stub 85.1; 2027 67.8 (Q1 76.3 → Q4 60.7); 2028 45.2 (thin but traded); 2029 37.7 (exchange mark, zero open interest).
- **Dated–futures** (Dated proxy = EIA Brent spot, FRED `DCOILBRENTEU`, minus the front future the same day) `[F]`:

  | Date | Dated proxy | Front future | Spread |
  |---|---|---|---|
  | 27 Oct | 123.10 | 113.88 (Z26) | +9.2 |
  | 30 Oct | 120.15 | 117.64 (Z26, expiry) | +2.5 (+6.7 vs F27 113.43) |
  | 2 Nov | 107.39 | 104.77 (F27) | +2.6 |
  | 3 Nov | 107.03 | 103.60 (F27) | **+3.4** |

  - FRED was last updated on 4 Nov, with no value after 3 Nov.
  - The physical premium was +20.5 on 14 Oct and is nearly gone. The Bull signpost (> $30 sustained) is far away.
  - EIA October Brent spot average: $124 (spot basis, context).
- **USD and NOK `[F, Norges Bank]`:** USD/NOK 9.2303 (3 Nov) → 9.4663 (10 Nov). The NOK weakened 2.6% as oil fell; EUR/USD 1.1214. The dollar did not drive the oil move.

### Balance check (implied stock change per scenario and year vs IEA/EIA)

| mb/d, + = build | 2026 | 2027 | 2028 | 2029 | Comment |
|---|---|---|---|---|---|
| IEA (Oct) | −1.7 | ~+4.0 | — | — | Derived: supply 100.7 / ~108.4, demand 102.4 / ~104.4 `[E/A]`; the November OMR is due 13 Nov |
| EIA (Nov) | −0.7 | **+4.0** | — | — | Supply 101.7 / 108.4, demand 102.4 / 104.4; October was −1.3 / +5.0. 1H27 +3.5 `[E]` |
| JPMorgan | Sep +1.1, Oct +1.4 | — | — | — | Monthly estimates; conflict with the IEA (Sep −0.8) `[E]` |
| OPEC (Oct) | — | — | — | — | Call on DoC crude 42.1 → 43.9 mb/d; no balance stated `[E]` |
| Base | ~−1.5 | **+1.5 to +2.5** | +0.5 to +1.0 | 0 to +0.5 | Flows incl. bypass near pre-war on monthly average; ME ex-Iran back by mid-2027; attack risk keeps restocking and risk inventories high; about half of the surplus goes to strategic refill; stocks normal by end-2028 `[A]` |
| Bear | — | +4 to +5 | +1.5 to +2.5 | ~0 | Stocks rebuilt during 2027 → contango; OPEC+ cuts in 2029 `[A]` |
| Bull | — | −1 to 0 | −0.5 to +0.5 | +0.5 | Low stocks force price rationing `[A]` |

**Reading (11 Nov) `[A]`:**
- **Base 2027 moves from +1 to +2 to +1.5 to +2.5 mb/d.**
  - The faster recovery outside Iran (EIA, HSBC) adds ~0.5 mb/d of builds, ~180 mb over the year. That is consistent with a $4 lower Base.
  - End-2027 stocks stay below pre-war (−509 mb hole plus ~1 bn bbl of strategic and commercial restocking), so Base keeps a backwardated, above-Bear path.
- **Base 2026 moves from ~−2 to ~−1.5:** the EIA is at −0.7 and JPMorgan counts a surplus, against the IEA at −1.7.
- **The EIA's 2027 surplus (+4.0) shrank by 1.0 mb/d (supply −1.2)**, a supply revision, not a demand one, so no trigger. The EIA's +4.0 against its own $86 shows that the agency, too, expects most of the surplus to be absorbed by restocking.

## Signposts and monitoring

| Signpost | Threshold (Bear / Bull) | Now (11 Nov) | Previous (4 Nov) | Direction |
|---|---|---|---|---|
| Hormuz crude (Kpler 7d) | Bear ≥ 13 · Bull < 8 for two weeks | Kpler 7.82 (week to 8 Nov; scope not stated, pre-war base 17.14); week to 4 Nov not found; 7.3 (crude, week to 28 Oct) | Week to 4 Nov pending; 7.3 | Touched twice, not confirmed (series differ, a week missing); no fall in barrels |
| ME crude incl. bypass | Bull < 13 · Base ≥ 15 | Kpler October 16.1; Vortexa 14.0; FGE 80–85% of pre-war (≈ 13–14.5) | Kpler October 16.1 | Base on Kpler; borderline on others |
| East–West pipeline / Yanbu | Bull if down again · Base ≥ 5 | Restarted (EIA); no throughput figure | No figure | Unconfirmed |
| Saudi facilities | Bull: facility hit with lasting loss | Aramco Tower (Riyadh, admin) minor debris damage 8 Nov; Eastern Province missile intercepted; no output loss | Riyadh airport claim; no loss | Not crossed |
| Tanker attacks / ship-to-ship shuttle | Bull: system fails | Tanker hit NE of Lima (10 Nov, UKMTO); IRGC claims two (later five) tankers mined; 37 ships hit in October (WINEP) | Hits 30 Oct–2 Nov; transits 119 | Not crossed; attacks continue |
| Iran–USA | Bear: ceasefire > 60 d · Bull: new strikes with retaliation on energy infrastructure | Strikes on hold (9 Nov); "highly unlikely" to return to war while talks progress; blockade stays; Qatar mediating; Iran denies talks; no signed deal | Qeshm strike; draft MoU; "far from a deal" | Bear closer; Bull further |
| US Congress (new) | Bear support: Congress cuts war funding · Bull window: lame duck to 3 Jan | Seated 3 Jan; stopgap 11 Dec; no new vote | Democrats won both chambers | Unchanged |
| Russia–Ukraine (new) | Bear enabler: settlement with sanctions relief | Talks in Abu Dhabi 10 Nov (first since February); refinery strikes continue | — | Watch |
| ME refined-product exports (IEA) | Bear > 3.3 · Base ~2.6 by mid-2027 | 1.9 (Sep, IEA); next OMR 13 Nov. Context, other scope: Vortexa Gulf product loadings ~3 (Oct) | 1.9 | Base |
| China product exports | Bull: monthly quota < 2 Mt | No new quota data; exports may stay curbed (low stocks) | Third batch 4.55 Mt | Base |
| Russian diesel | Bear: exports > 0.6 mb/d | Plan 2.15 Mt (~0.52 mb/d) in November vs 0.51 Mt in October; refining capacity −30% | Quotas 2 Mt reported | Not crossed; two-way |
| Russian refining (new) | Bull crack: outage lasts or spreads | 2.2 mb/d nameplate disrupted; runs cut up to ~1.5 mb/d; Kirishi hit 9 Nov | — | Supports crack |
| Brent M1−M4 | Bear < $2 (regime change < $5 for two weeks) | +6.70 (F27−K27, 10 Nov) | +8.99 | Clearly tight, narrowing |
| Dated–futures (EIA proxy) | Bull > $30 sustained | +3.4 (3 Nov) | +9.2 (27 Oct) | Away from Bull |
| ULSD−Brent crack (front) | Bull > $100 sustained · Base < $65 by mid-2027 | 82.0 (Nov, 10 Nov) | 86.7 (3 Nov) | Base |
| Gas-to-oil switching ratio | Bull crack: gasoil/TTF < 1.0 (energy basis) | Dec-26 1.05 · Q1-27 1.02 · Cal-27 1.13 | Dec-26 0.99 · Q1-27 0.95 (30 Oct) | No longer crossed |
| ULSD 2029 forward | Retest Base 2029 if OI > 1,000 lots at a crack > $40, or the 2028 crack > $55 | 37.7, zero OI (mark); 2028 45.2 | 41.5; 47.2 | Base |
| Brent 2027 strip vs Base (re-armed 11 Nov on Base 84) | **Up:** retest if the strip is > $6 above Base (> 90) together with a crossed Bull flow signpost · **Down:** retest if the strip settles > $5 below Base (< 79) for a week without a signed deal | 81.2 (−2.8 vs 84) | 89.7 vs 88 | Inside the band |
| Brent front 15% trigger (re-armed 11 Nov) | Full update if the front settles ≤ 77.8 or ≥ 105.2 (F27, ±15% vs 91.49 on 10 Nov) to 30 Nov, then G27 ≤ 76.0 or ≥ 102.9 to 10 Dec | 91.49 (10 Nov) | Fired on 4 Nov (94.62 ≤ 96.42) | Re-armed |
| Dec-27 15% trigger | Full update if Z27 settles ≤ 66.0 or ≥ 89.3 within a month of 10 Nov | 77.64 (−11.9% vs 30 Oct) | 84.88 | Not fired |
| Brent–WTI (same month) | Stress > $12 | 5.45 (Nov, 10 Nov) | 7.5 | Normal |
| US export restrictions | Bull if imposed | Rejected | Rejected | Unchanged |
| OPEC+ 2027 quotas | Bear: market-share quotas | No change; next 29 Nov | December held | Open, 29 Nov |

**Watch before the next update (stale after 30 Nov):**
- **Iran–USA:** a signed MoU and the first reopening steps (Bear), or a strike with retaliation on Gulf energy infrastructure (Bull). Mine clearance and war-risk insurance are the physical gate even after a deal.
- **Flows:** Kpler weekly Hormuz figures (ask for the series and scope), the Kpler and Vortexa November monthly figures, and any East–West throughput number.
- **Agencies:** the OPEC MOMR (11 Nov) and the IEA OMR (13 Nov). A demand revision > 0.5 mb/d for a year in the window, or an IEA 2027 balance far from +4, means a full update at once.
- **US stocks:** the EIA WPSR for the weeks to 6 and 13 Nov (is the API +9 mb confirmed; does distillate keep drawing?).
- **Russia:** refinery repairs vs new strikes, the November diesel exports actually loaded, and the Abu Dhabi talks.
- **The curve:** M1−M4 below $5 for two weeks (regime change), the 2027 strip vs 79 / 90, and the front ±15%.

**Before 30 Nov:** OPEC+ (29 Nov, 2027 quotas expected); BZ F27 expiry and the end of the Russian jet export ban (30 Nov); third US carrier (end of November, carried).

**Before 3 Jan:** EIA STEO (8 Dec); FY27 stopgap expiry (11 Dec); Qatar LNG force majeure to end-December; the new Congress seated (3 Jan 2027).

## For downstream skills

**Full update 11 Nov.** One value that other documents read moved: **Brent Base 2027 88 → 84** (−$4, −4.5%; above the $3 minimum, below the 15% recalibration trigger).
- **Unchanged:** Base 2028 (77), Base 2029 (72), the mid-cycle values (60 / 70 / 82), every Bear and Bull path, every crack and jet path, Brent–WTI from 2027, the scenario mechanisms and the weights.
- **Re-marked (never material on their own):** the stub (Brent 104.3 → 97.1, crack 88.1 → 85.1, Brent–WTI 8.0 → 7.0) and the Year-1 quarters (Base Brent 95/90/85/82 → 89/85/82/80; crack 80/71/67/62 → 79/71/67/63).
- **Trigger-rule verdict:** no reader's path, mid-cycle or reference moved beyond the recalibration trigger. No Base IRR moves by about 1 pp, and no verdict can flip on this change, so **`affects` = none**. Each reader takes the new values at its own next update.

| Reader | What it reads here | Touched? | What to take in at its next run |
|---|---|---|---|
| **rig** | Brent path, long end, mid-cycle | No (no action now) | Base 2027 84. The long end fell (Dec-28 77.4 → 72.8, Dec-29 73.5 → 70.6, Dec-30 70.7 → 69.1), but Dec-31 onwards is flat and mid-cycle 70 is unchanged, so the FID logic stands. Its planned full update reads this baseline |
| **shipping** | Crude and product prices, volumes, disruptions | No (no action now) | Disruption status unchanged (contested, no deal). New volume data: Kpler Hormuz 7.82 mb/d (week to 8 Nov, scope unclear); FGE crude 80–85% and products 35–40% of pre-war; Vortexa Gulf product loadings ~3 mb/d (Oct); ARA gasoil imports 400 kb/d (35% Saudi). Russia: refining −30%, diesel export plan 2.15 Mt (Nov), tankers dropping US destinations. Attacks continue (tanker hit NE of Lima, 10 Nov; 37 ships in October). Brent–WTI narrowing (5.45 same-month; 2027 strip 3.9), so the US crude export arbitrage narrows |
| **supply** | Oil path (FID and tender logic), long end, mid-cycle, disruption status | No (no action now) | Long end and mid-cycle as for rig; disruption status unchanged. Rig activity still reaches it through rig |
| **hy** | E&P row and scenario mapping (Brent per scenario, mid-cycle), disruption status | No (no action now) | Base 2027 84 (E&P cash flow still far above breakeven; Bear 65 and mid-cycle 70 unchanged). The inflation channel weakens: stub 97.1, diesel ~$174–182/bbl. USD/NOK 9.47 (10 Nov) from 9.23. Bear catalyst closer (strikes on hold; Russia–Ukraine talks) |
| **equity** | Brent per scenario and mid-cycle (Oslo and World energy), Bear/Bull catalysts | No (no action now) | Base 2027 84 cuts Oslo energy E 2027 by ~7% on its (Brent − 30)/50 rule (1.16 → 1.08), one year only with mid-cycle unchanged: **~0.3 pp or less** on the Oslo Base IRR `[A]` (its own ±$10 on every year and mid-cycle is ±3.4 pp). Base is now nearer its consensus-implied 2027 Brent (~$80). Catalyst text: Bear adds Russia–Ukraine relief; Bull further (strikes on hold) |
| **borr** | Background via rig scenarios | No | Nothing direct; reaches it through rig |
| **odl** | Background via rig scenarios | No | Nothing direct; reaches it through rig |
| **dof** | Through supply only | No | Nothing direct; reaches it through supply |
| **sed** | Background | No | Nothing direct (drilling via rig) |
| **capt** | Background (crude tankers) | No | Nothing direct; flows reach it through shipping |
| **hafnia** | Background (product tankers) | No | Crack paths unchanged. Product-flow items (Russian refining, Gulf product loadings, ARA imports) reach it through shipping |
| **global-index** | Energy block | No | World energy weight ~4.2%; a one-year −$4 Base change is negligible (< 0.05 pp) `[A]` |
| **defense** (on hold) | Gulf export row | No | Disruption status unchanged |
| **[[iaf-valuation]]** (oil producers and refiners valued directly; none in the register now) | Stub, Year-1 quarters, annual paths, mid-cycle | — | Stub Brent 97.1 / crack 85.1 / Brent–WTI 7.0; Base Year-1 quarters 89/85/82/80; Base 2027 84; mid-cycle unchanged |

## Change log

### 11 Nov 2026 — full update (skill revision 2026-10-24.4)

- **Status:** **Oil Market BBB changed.** Base Brent 2027 88 → 84. New baseline date 11 Nov 2026. Weights 25/50/25 (convention) **kept**.
- **Causes:** stale after 7 Nov; the 15% front trigger fired (F27 94.62 on 4 Nov, −16.6%; 91.49 on 10 Nov, −19.3%); the 7 Nov follow-up never ran.
- **New since 4 Nov:**
  - F27 settlements 94.62 / 98.29 / 98.32 / 92.57 / 91.49 (4–10 Nov).
  - 2027 strip 89.7 → 81.2; 2028 79.1 → 73.9; 2029 74.6 → 71.2. Dec-27 84.88 → 77.64. The long end from 2031 is flat or up.
  - M1−M4 +8.99 → +6.70.
  - Dated − futures +3.4 (3 Nov), from +9.2 (27 Oct).
  - Trump held off strikes after the Qatar meeting (9 Nov); the blockade stays; Iran denies talks; the Qatari official called the reported Hormuz plan details inaccurate; no signed deal.
  - Attacks continue: tanker hit NE of Lima (10 Nov); Aramco Tower debris damage in Riyadh (8 Nov).
  - Kpler Hormuz 7.82 mb/d (week to 8 Nov). EIA shut-ins 2.5 mb/d (October).
  - EIA STEO (10 Nov): 2027 $86 (from $84), Q4-27 $77, 2027 surplus +4.0 (from +5.0), 2027 diesel +12%, wider cracks.
  - HSBC raised Saudi output; JPMorgan surplus 1.1 / 1.4 mb/d (Sep / Oct); API +9 mb (unverified).
  - Russian refining −30% (Reuters, 10 Nov); diesel export plan 2.15 Mt; Russia–Ukraine talks in Abu Dhabi (10 Nov).
  - TTF −18%; the switching ratio is back above 1.0.
- **Brief input assessed:**
  - F27 4–6 Nov settlements: confirmed.
  - "~93.6 on 9 Nov": **rejected**; the settlement was 92.57.
  - "2027 strip ~83 on 9 Nov": 82.44, confirmed in substance.
  - "Strikes highly unlikely": confirmed.
  - "Toll demand dropped, denied by a Qatari official": partly; the official called the reported details inaccurate.
  - "No signed deal": confirmed.
  - "Attacks near Hormuz and Houthi strikes on Saudi Arabia continue": confirmed (10 Nov tanker; 8 Nov Riyadh).
  - "JPMorgan sees a growing surplus": confirmed as the 4 Nov note (Sep 1.1 → Oct 1.4); no newer JPMorgan note found.
  - "EIA STEO ~10 Nov": read (10 Nov). "IEA OMR 13 Nov": not out. "OPEC+ 29 Nov": confirmed.
- **Changed (previous → new):**

| Item | Previous (31 Oct / 4 Nov) | New (11 Nov) | Reason |
|---|---|---|---|
| Brent Base 2027 (range) | 88 (81–95) | **84 (77–91)** | Physical premium gone (Dated − futures +3.4); faster recovery outside Iran (EIA, HSBC, JPMorgan); strip at or near 83 for five sessions, 81.2 on 10 Nov; EIA comparable path $86 spot ≈ $84 futures. −$4 > $3 minimum; < 15% trigger |
| Brent Base 3-yr average | 79.0 | 77.7 | Follows 2027 |
| Year-1 quarters, Brent Bear / Base / Bull | 70/66/63/61; 95/90/85/82; 127/120/115/110 | 69/66/63/62; **89/85/82/80**; 125/120/115/112 | New annual Base; 10 Nov shape (slope $12.6 → $9.2) |
| Year-1 quarters, crack Bear / Base / Bull | 40/36/33/31; 80/71/67/62; 126/112/105/97 | 39/36/34/31; 79/71/67/63; 124/112/106/98 | 10 Nov shape; annual values unchanged |
| Stub Brent / crack / Brent–WTI | 104.3 / 88.1 / 8.0 | 97.1 / 85.1 / 7.0 | Mechanical: 2–10 Nov settlements + 10 Nov forward |
| Diesel price Base stub; 2027 | 192.4 (1,433 $/t); 158 (1,177) | 182.2 (1,357); 154 (1,147) | Follows Brent and the stub |
| Forward-curve row | 3 Nov: 89.7/70.5 · 79.1/47.2 · 74.6/41.5 | 10 Nov: 81.2/67.8 · 73.9/45.2 · 71.2/37.7 | Re-marked |
| Balance, Base | 2026 ~−2; 2027 +1 to +2 | 2026 ~−1.5; 2027 +1.5 to +2.5 | Faster supply recovery; EIA, JPMorgan |
| Scenario text | — | Bear enabler: Russia–Ukraine sanctions relief. Base: EIA recovery timing. Bull: strikes on hold since 9 Nov | This run |
| Signposts | — | Retest band re-armed on Base 84 (< 79 for a week / > 90 with a Bull flow signpost); front 15% re-armed on 91.49; Dec-27 15% row; new rows Russia–Ukraine and Russian refining; switching ratio no longer crossed | This run |
| Stale after | 7 Nov | **30 Nov** | OPEC+ 29 Nov; F27 expiry 30 Nov |

- **Unchanged (tested):**
  - Bear 65 / 60 / 60 / 60. The catalyst is not triggered, and the strip (81) is far above Bear.
  - Bull 118 / 102 / 90 / 82. The catalyst is further away but live; the path is conditional on the catalyst.
  - Base 2028 77 and 2029 72: forward gaps −3.1 / −0.8, with the curve as the only evidence.
  - Mid-cycle 70: the long end is flat.
  - Diesel crack 70 / 48 / 33 / 25: evidence on both sides; forward gaps −2.2 / −2.8 / +4.7 (2029 is a mark).
  - Jet 60 / 40 / 28.
  - Brent–WTI 6.0 / 5.0 / 4.5 / 4.0: the 2027 strip at 3.9 is a gap of 2.1, below the $3 minimum. Noted, not applied; retest if it stays below 4 at the next run.
- **Rules from 31 Oct / 4 Nov:**
  - Conditional up-rule void (strip ≪ 93).
  - Downside retest rule not formally met (below 83 on 3 of 5 sessions; average 83.03), but Base was retested in this full update.
  - Bear catalyst not met.
- **Triggers:**
  - **Fired:**
    - Brent front −16.6% (4 Nov settlement), −19.3% (10 Nov). This run.
    - Refining capacity > 0.5 mb/d: Russia ~2.2 mb/d nameplate disrupted, runs cut by up to ~1.5 mb/d. Tested: no crack change.
  - **Touched, not confirmed:** the Bull flow signpost "Hormuz < 8 mb/d for two weeks" (7.3 on 28 Oct and 7.82 on 8 Nov, different series, week to 4 Nov missing).
  - **Not fired:**
    - Dec-27 −11.9% vs 30 Oct.
    - M1−M4 still clearly tight (+6.70).
    - Disrupted volumes (+7% on Kpler weekly, unlike series).
    - No OPEC+ change.
    - Front crack −1% vs 30 Oct (82.97 → 82.01).
    - EIA 2027 demand −0.2 (< 0.5).
    - No Bear signpost crossed.
- **Base paths vs recalibration trigger:** the only Base move is 2027 −$4 (−4.5%), above the $3 minimum and below the 15% recalibration trigger. **No Base path moves by more than the recalibration trigger.**
- **Forecast vs actual:** not applicable until the window rolls. For information: October realised Brent 108.34 and ULSD crack 92.85; November to date (2–10 Nov) Brent 97.7 and crack 83.5 `[F]`.
- **Downstream:** changed yes; `affects` none (see "For downstream skills").
- **New dated events:**
  - OPEC MOMR 11 Nov (watch).
  - IEA OMR 13 Nov (watch; open if a demand revision > 0.5 mb/d).
  - EIA WPSR, weeks to 6 and 13 Nov (~12 and 18 Nov).
  - Front ±15% re-armed to 10 Dec (F27 ≤ 77.8 / ≥ 105.2; then G27 ≤ 76.0 / ≥ 102.9).
  - Russian jet export ban ends 30 Nov.
  - EIA STEO 8 Dec.
  - OPEC MOMR 14 Dec (calendar sites, not confirmed on opec.org).
  - Carried: OPEC+ 29 Nov; F27 expiry 30 Nov; stopgap 11 Dec; new Congress 3 Jan 2027.

### Update 4 Nov 2026 (OPEC+ and US midterms) — condensed

- **Status:** kept unchanged; small update under 2026-10-24.4.
- **What changed:**
  - Stub Brent 110.4 → 104.3, crack 86.2 → 88.1, Brent–WTI 9.0 → 8.0 (mechanical).
  - Year-1 shape (slope $16 → $13).
  - Bull window to 3 Jan; Bear enabler: Democratic Congress from 3 Jan.
  - New signposts: US Congress, downside retest (< 83), 15% front trigger.
- **Events read:** OPEC+ held December (1 Nov); Democrats won both chambers (3 Nov); EIA WPSR (distillate −3.6 mb).
- The full 4 Nov text is in the git history.

### 31 Oct 2026 — condensed

- **Status:** kept unchanged.
- **Trigger tested:** Hormuz crude −29% week on week (10.3 → 7.3); Ras Tanura loadings −29%.
- **Why the paths stayed:** one week of data; stable bypass flows; a narrowing Dated premium; a flat long end.
- **What changed:**
  - Stub 109.2 → 110.4 Brent and 90.9 → 86.2 crack.
  - The 31 Oct conditional rule set for 7 Nov (now void).
  - The gasoil cross-check extended to 2028.
  - The switching ratio < 1.0 for Q1-27 (now un-crossed).
- The full text is in the git history.

## Appendix: sources

| Source | Content | Observed / published |
|---|---|---|
| **11 Nov:** Yahoo Finance connector (`get_quote`, `get_chart`): BZ F27–H28, Z28; HO Z26–F28, Z28; CL Z26, F27, H27, M27, U27, Z27, Z28, Z29; BZ=F, HO=F, CL=F daily | Daily settlements 2–10 Nov (2027 strip test), 10 Nov curve, stub, M1−M4, Brent–WTI, decomposition; 11 Nov intraday as context. 10 Nov daily volumes equal 9 Nov's for every contract (Yahoo artefact; prices match Barchart) | 2–10 Nov settlements / retrieved 11 Nov ~07:20 UTC |
| **11 Nov:** Barchart ICE Brent `CB*0`, NYMEX ULSD `HO*0`, ICE gasoil `LF*0`, EEX TTF month `GHMZ26` futures-prices grid (in-app browser, shadow-DOM read; cookie banner denied; sign-up popup closed with X; no sign-in) | Brent 99 months to H35 (`s` rows = 10 Nov settlements; rows trading on 11 Nov read as last − change); ULSD to F30 with OI; gasoil to Z32 (V28 not read); TTF Nov-26 to Oct-33 | Settlements 10 Nov / read 11 Nov |
| **11 Nov:** FRED `DCOILBRENTEU` | Dated proxy 26 Oct–3 Nov (no value after 3 Nov; last updated 4 Nov) | 3 Nov / retrieved 11 Nov |
| **11 Nov:** Norges Bank `get_exchange_rate` USD, EUR | USD/NOK 9.2303 (3 Nov) … 9.4663 (10 Nov); EURNOK 10.6155 (10 Nov) → EUR/USD 1.1214 | Fixings 3–10 Nov |
| **11 Nov:** EIA STEO pages (eia.gov/outlooks/steo/, report/global_oil.php) | Brent $97 (2026), $86 (2027), Q4-27 $77; balances 101.7/108.4 vs 102.4/104.4; shut-ins 2.5 mb/d; ME ex-Iran back by mid-2027; US crude 410 mb end-Oct; retail diesel 2027 $5.03; wider 2027 cracks; next STEO 8 Dec | Released 10 Nov (completed 5 Nov) |
| **11 Nov:** Bloomberg via Transport Topics | EIA raises 2027 diesel and gasoline forecasts; Brent $104 Nov / $99 Dec | 10 Nov |
| **11 Nov:** CNBC (10 Nov, oil prices) | Brent settled 91.49 (low 89.16), WTI 86.04; Trump quotes; FGE "cannot be bridged"; ING | 10 Nov |
| **11 Nov:** The National (10 Nov) | Brent < $90 intraday; Kpler Hormuz 7.82 mb/d week to 8 Nov (46% of 17.14, excl. Iran); Trump delays strikes; Russia–Ukraine talks | 10 Nov |
| **11 Nov:** Reuters via Business Recorder (11 Nov) | Tanker hit NE of Lima (UKMTO); IRGC mine claims; WINEP 37 ships in October; API +9 mb; Russian refining −30%; Ust-Luga drone fire; Abu Dhabi talks; LSEG mine-clearance note | 11 Nov |
| **11 Nov:** Reuters via gCaptain (10 Nov); Kyiv Independent, Atlantic Council, Pravda (search summaries) | Russian refining: nine refineries, 2.2 mb/d nameplate, runs cut up to 200 kt/d; Kirishi hit 9 Nov; fuel shortages | 10 Nov |
| **11 Nov:** Kyiv Post, Oil and Gas 360, Al Jazeera via Digg (search summaries, not opened) | Russian diesel exports: 2.15 Mt planned for Nov vs 0.51 Mt Oct (Kpler/LSEG); tankers drop US destinations; Novak 3.5 Mt | 5–7 Nov |
| **11 Nov:** Bloomberg via BusinessMirror (10 Nov) | Vortexa Gulf product loadings ~3 mb/d (Oct); FGE crude 80–85% / products 35–40% of pre-war; China diesel exports curbed | 10 Nov |
| **11 Nov:** Oil & Gas Journal (4 Nov) | JPMorgan surplus 1.1 / 1.4 mb/d; ME exports 20.7; demand −3.3; IEA counterview; HSBC Saudi output path | 4 Nov |
| **11 Nov:** TokenPost (10 Nov; no wire named) | Reported Hormuz plan (tolls, control dropped); Qatari official: details "inaccurate" | 9–10 Nov |
| **11 Nov:** CNN, Middle East Eye, Morocco World News (search summaries) | Houthi missiles on Riyadh; Aramco Tower debris damage; Eastern Province interception; Houthi claims | 8 Nov |
| **11 Nov:** search summaries (Benzinga, CBC, World Today Journal; not opened) | Trump "highly unlikely" (CNN); Rezaei: no negotiations; strait closed unless terms met | 9–10 Nov |
| **11 Nov:** ENGINE (Insights Global / Vortexa) | ARA gasoil imports 400 kb/d Nov to date (India 39%, Saudi 35%, Canada 12%) | 6 Nov |
| **11 Nov:** S&P Global Platts (search summary, page 403) | European jet crack above ULSD barge crack, up to $11.75 on 16 Oct | 19 Oct |
| **11 Nov:** Trading Economics / MTS Insights calendars (search summaries) | OPEC MOMR 11 Nov and 14 Dec; IEA OMR 13 Nov | Calendars |
| **11 Nov:** Discovery Alert (aggregator, 5 Nov) | Tracker scopes (Kpler, Vortexa, IEA, EIA); no week-to-4-Nov figure | 4–5 Nov |
| **4 Nov sources (carried, see git):** Barchart and Yahoo 3 Nov settlements; OPEC+ statement coverage; midterm coverage (AP calls); Reuters/Vortexa/Kpler October flows; Hydrocarbon Processing (Russian quotas); globaloilshock.com (UKMTO/JMIC) | As used in the 4 Nov update | 25 Oct–4 Nov |
| **31 Oct sources (carried, see git):** Kpler via CNBC/Newsquawk; Gulf News trackers; House of Saud; Al Jazeera; IEA OMR Oct; EIA STEO Oct; Insights Global; Global Trade Alert; Mysteel | As used on 31 Oct | Sep–Oct |

**Raw settlements 10 Nov `[F]`:**
- **Brent (Barchart CB = Yahoo BZ):** F27 91.49 · G27 89.45 · H27 87.71 · J27 86.16 · K27 84.79 · M27 83.53 · N27 82.35 · Q27 81.24 · U27 80.20 · V27 79.24 · X27 78.39 · Z27 77.64 · F28 76.95 · G28 76.33 · H28 75.79 · J28 75.32 · K28 74.94 · M28 74.60 · N28 74.26 · Q28 73.93 · U28 73.61 · V28 73.30 · X28 73.01 · Z28 72.76 · F29 72.51 · G29 72.29 · H29 72.13 · J29 71.98 · K29 71.82 · M29 71.65 · N29 71.46 · Q29 71.28 · U29 71.10 · V29 70.94 · X29 70.76 · Z29 70.58 · F30 70.39 · G30 70.25 · Z30 69.06 · Z31 67.70 · Z32 66.38 · Z33 65.13 · Z34 64.24 · H35 64.05.
- **Brent front daily (BZ F27):** 30 Oct 113.43 · 2 Nov 104.77 · 3 Nov 103.60 · 4 Nov 94.62 · 5 Nov 98.29 · 6 Nov 98.32 · 9 Nov 92.57 (range 90.63–98.42) · 10 Nov 91.49 (low 89.15). 11 Nov intraday ~92.0.
- **2027 strip daily (full front mapping, Yahoo):** 3 Nov 89.71 · 4 Nov 82.91 · 5 Nov 83.61 · 6 Nov 84.98 · 9 Nov 82.44 · 10 Nov 81.21. M1−M4: 8.99 · 7.87 · 10.30 · 8.88 · 6.66 · 6.70.
- **Brent contracts 4–9 Nov (Yahoo; H27, J27, K27, M27, N27, Q27, U27, V27, X27, Z27, F28, G28):**
  - 4 Nov: 90.05, 88.27, 86.75, 85.35, 84.04, 82.84, 81.74, 80.75, 79.89, 79.12, 78.41, 77.76.
  - 5 Nov: 92.16, 89.89, 87.99, 86.30, 84.77, 83.39, 82.15, 81.06, 80.11, 79.27, 78.49, 77.77.
  - 6 Nov: 93.30, 91.24, 89.44, 87.78, 86.26, 84.87, 83.61, 82.47, 81.48, 80.59, 79.76, 79.00.
  - 9 Nov: 88.78, 87.26, 85.91, 84.68, 83.54, 82.46, 81.46, 80.53, 79.71, 78.97, 78.28, 77.64.
- **ULSD ($/gal, Barchart = Yahoo):** Z26 4.1309 · F27 4.0341 · G27 3.9604 · H27 3.8744 · J27 3.7730 · K27 3.6799 · M27 3.5919 · N27 3.5333 · Q27 3.4831 · U27 3.4403 · V27 3.3993 · X27 3.3470 · Z27 3.2784 · F28 3.2061 · G28 3.1346 · H28 3.0693 · J28 2.9855 · K28 2.9208 · M28 2.8483 · N28 2.8033 · Q28 2.7558 · U28 2.7308 · V28 2.7218 · X28 2.7018 · Z28 2.6786 · F29 2.6551 · G29 2.6500 · H29 2.6393 · J29 2.6198 · K29 2.6059 · M29 2.5953 · N29 2.5974 · Q29 2.5979 · U29 2.5745 · V29 2.5737 · X29 2.5697 · Z29 2.5466 · F30 2.5535.
  - Open interest: Z28 1,824; F29 81; G29–X29 0; Z29 64.
- **ULSD front daily (HO Z26):** 2 Nov 4.4216 · 3 Nov 4.5306 · 4 Nov 4.2055 · 5 Nov 4.3519 · 6 Nov 4.3317 · 9 Nov 4.2148 · 10 Nov 4.1309.
- **WTI (Yahoo):** Z26 86.04 (daily 2–10 Nov: 96.46 · 96.09 · 88.12 · 90.52 · 90.83 · 86.85 · 86.04) · F27 84.86 · H27 82.03 · M27 78.48 · U27 75.52 · Z27 73.12 · Z28 68.74 · Z29 66.24.
- **ICE gasoil ($/t, Barchart):** X26 1,280.75 · Z26 1,227.75 · F27 1,189.25 · G27 1,160.25 · H27 1,131.50 · J27 1,099.75 · K27 1,071.50 · M27 1,045.25 · N27 1,021.75 · Q27 1,000.25 · U27 981.00 · V27 963.75 · X27 944.00 · Z27 923.75 · F28 906.25 · G28 889.75 · H28 872.75 · J28 852.75 · K28 836.25 · M28 820.00 · N28 806.00 · Q28 793.75 · U28 786.00 · V28 780.25 `[A, interpolated]` · X28 774.50 · Z28 767.00 · F29 762.75.
- **TTF (€/MWh, Barchart, month futures):** Dec-26 84.710 · Jan-27 84.549 · Feb 84.125 · Mar 80.802 · Apr 68.200 · May 64.845 · Jun 62.709 · Jul 62.134 · Aug 61.518 · Sep 60.981 · Oct 59.478 · Nov 59.199 · Dec-27 59.004.
- **Dated proxy (FRED `DCOILBRENTEU`, EIA spot):** 26 Oct 128.12 · 27 Oct 123.10 · 28 Oct 119.20 · 29 Oct 115.28 · 30 Oct 120.15 · 2 Nov 107.39 · 3 Nov 107.03.
- **Derived (front mapping):**
  - Brent 2027 Q1–Q4: 86.22 / 82.37 / 79.28 / 76.97, year 81.21.
  - Brent 2028: 73.86; 2029: 71.19.
  - Crack 2027 Q1–Q4: 76.29 / 68.90 / 65.24 / 60.67, year 67.77.
  - Crack 2028: 45.16; 2029: 37.74.
  - Gasoil crack 2027 Q1–Q4: 65.52 / 58.05 / 52.49 / 47.14, year 55.80; 2028 (Jan–Nov) 35.56.
  - Brent–WTI 2027 (mid-quarter): 3.89; Nov-28 3.77; Nov-29 4.15.

**Raw settlements 3 Nov `[F]` (previous run, for the change log):**
- Brent F27 103.60 · G27 100.94 · H27 98.52 · J27 96.43 · K27 94.61 · M27 92.89 · N27 91.27 · Q27 89.75 · U27 88.34 · V27 87.05 · X27 85.91 · Z27 84.88 · F28 83.91 · G28 83.00 · Z28 77.38 · Z29 73.49 · Z30 70.65 · Z31 68.27 · Z34 63.34.
- ULSD Z26 4.5306 · Z27 3.4869 · Z28 2.8264 · Z29 2.7264. WTI Z26 96.09 · Z27 79.32 · Z28 72.79 · Z29 68.73.
- Derived: Brent 2027 89.71 (Q 96.52 / 91.30 / 87.10 / 83.93), 2028 79.12, 2029 74.58; crack 2027 70.47, 2028 47.15, 2029 41.46.
- Older raw blocks (30 Oct settlements, October daily front series) are in the git history. October actuals used in the stub: Brent 108.34, ULSD crack 92.85, Brent–WTI 10.35.

**Not available on 11 Nov:**
- Kpler Hormuz week to 4 Nov; the scope of the Kpler week-to-8-Nov figure.
- EIA WPSR week to 6 Nov (not out); API figure from market sources only.
- Dated proxy after 3 Nov.
- OPEC MOMR (11 Nov, not out at writing); IEA OMR (13 Nov).
- NWE jet crack after 16 Oct.
- November ARA stock levels; Singapore and China stocks.
- East–West throughput; Murban–Dubai; freight cost re-read.
- TTF quarter, season and year contracts; EUA price.
- The Russian diesel quota decree.
