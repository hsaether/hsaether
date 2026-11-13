# Oil Market BBB — 11 November 2026

**Status:** Final · full update 11 Nov 2026 (Update mode, Steps 0–11), as of the **Tue 10 Nov** settlements · skill `oil-market-bbb` revision 2026-10-24.4 · **stale after 30 Nov 2026** · compacted 13 Nov 2026 (no value changed).

## Interface (values other documents read)

As of **11 Nov 2026** (paths) and the **10 Nov 2026 settlements** (stub, forward, long end). Nominal USD, period averages. Weights 25/50/25 are a convention, never a probability. Tags: `[F]` fact · `[E]` external forecast or secondary · `[A]` own assumption · `[?]` unknown.

**Paths and references** (point values; ranges in the sections below)

| $/bbl, period average | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| Brent Bear / Base / Bull | 97.1 / 97.1 / 97.1 | 65 / **84** / 118 | 60 / 77 / 102 | 60 / 72 / 90 | 60 / 70 / 82 |
| Brent Base 2027 by quarter (Q1 / Q2 / Q3 / Q4) | | 89 / 85 / 82 / 80 | | | |
| Diesel crack (ULSD − Brent) Bear / Base / Bull | 85.1 / 85.1 / 85.1 | 35 / 70 / 110 | 25 / 48 / 75 | 20 / 33 / 45 | 18 / 25 / 35 |
| Diesel price Base ($/bbl; $/t) | 182.2; 1,357 | 154; 1,147 | 125; 931 | 105; 782 | 95; 708 |
| Jet crack (NWE − Brent) Base | `[?]` | 60 | 40 | 28 | 22 |
| Brent–WTI Base | 7.0 | 6.0 | 5.0 | 4.5 | 4.0 |
| European diesel: gasoil crack vs ULSD crack | −9.3 | about −11 (2027–28) | about −11 | — | — |
| Forward curve, 10 Nov (Brent / diesel crack) | 97.1 / 85.1 | 81.2 / 67.8 | 73.9 / 45.2 | 71.2 / 37.7 | — |
| Long end, 10 Nov (Brent Dec contract; last column Dec-30 to Dec-34) | | Dec-27 77.64 | Dec-28 72.76 | Dec-29 70.58 | Dec-30 69.06 · Dec-31 67.70 · Dec-34 64.24 |

**Scenarios, disruption status and triggers**

| Item | State (11 Nov 2026) |
|---|---|
| Bear (25%) | Durable Iran–USA deal plus OPEC+ market-share quotas; enablers a Democratic Congress from 3 Jan 2027 and Russia–Ukraine sanctions relief. Surplus materialises, contango, crack towards its normal band. Earliest Q1 2027. **Closer, not triggered** (no signed deal) |
| Base (50%) | Armed normalisation without a deal: ME crude to market ~15–16 mb/d via bypass and escort, ME output outside Iran near pre-war by mid-2027, Iran constrained, product shortage into 2027 |
| Bull (25%) | Renewed strikes with retaliation on Gulf energy infrastructure; 3–5 mb/d lost again. Window mostly to 3 Jan 2027. **Further away** (strikes on hold since 9 Nov), tail live |
| Disruption / chokepoints | Hormuz contested, no signed deal, US blockade stays. Kpler Hormuz oil 7.82 mb/d (week to 8 Nov, ~46% of pre-war, scope not stated). ME crude incl. bypass: Kpler 16.1 (Oct; Base met), Vortexa 14.0, FGE 80–85% of pre-war. Gulf products ~3 mb/d loaded (Oct, ~half of pre-war). Attacks on ships continue; no Saudi output loss. Russian refining ~30% disrupted (runs cut up to ~1.5 mb/d) |
| Gulf export row (defense) | Gulf crude incl. pipelines 80–85% of pre-war, products 35–40% (FGE, early Nov); status unchanged: contested, no deal |
| Front 15% trigger | Re-armed on 91.49 (10 Nov): full update if F27 settles ≤ 77.8 or ≥ 105.2 to 30 Nov, then G27 ≤ 76.0 or ≥ 102.9 to 10 Dec. Not fired |
| Dec-27 15% trigger | Z27 ≤ 66.0 or ≥ 89.3 within a month of 10 Nov. Not fired (77.64) |
| 2027 strip retest band (Base 84) | Down: strip > $5 below Base (< 79) for a week without a signed deal. Up: > $6 above (> 90) with a crossed Bull flow signpost. Now 81.2: inside |
| Other triggers and signposts | M1−M4 < $5 for two weeks (now +6.70, clearly tight); agency demand revision > 0.5 mb/d for a year in the window (EIA 2027 −0.2); refining trigger > 0.5 mb/d **fired** (Russia), tested, no crack change; Hormuz < 8 mb/d for two weeks touched, not confirmed |

**Readers** (each takes the 11 Nov values at its own next run; `affects` none)

| Reader | Reads here | Note |
|---|---|---|
| shipping | Crude and product prices, volumes, disruptions | Disruption and flow rows above; ARA gasoil imports 400 kb/d (35% Saudi); Russian diesel export plan 2.15 Mt (Nov); Brent–WTI narrowing (5.45 same-month, 2027 strip 3.9) |
| rig | Brent path, long end, mid-cycle | Long end from Dec-31 flat, mid-cycle 70 unchanged: the FID logic stands |
| supply | Oil path (FID and tender logic) | As for rig; rig activity reaches it through rig |
| hy | E&P row; scenario mapping | E&P cash flow far above breakeven at Base 84; Bear 65 and mid-cycle 70; USD/NOK 9.4663 (10 Nov) |
| equity | Oslo and World energy | Base 2027 84 cuts Oslo energy E 2027 ~7% on its (Brent − 30)/50 rule: ~0.3 pp or less on the Oslo Base IRR `[A]` |
| defense | Gulf export row | Row above |
| global-index | Energy block | World energy weight ~4.2%; the 2027 Base change is < 0.05 pp `[A]` |
| sed, borr, odl, capt, hafnia, dof | Background via scenarios (rig, shipping, supply) | Nothing direct; crack paths unchanged for hafnia |
| [[iaf-valuation]] (oil producers and refiners; none in the register now) | Stub, Year-1 quarters, annual paths, mid-cycle | As in the tables above |

## Metadata

- **Analysis date:** Wed 11 Nov 2026, morning CET. Settlements from **Tue 10 Nov** (ICE Brent via NYMEX BZ and Barchart `CB*0`; NYMEX ULSD and WTI; ICE gasoil; EEX TTF). 11 Nov prints are intraday, context only (F27 ~92.0).
- **Previous baseline:** 31 Oct 2026, with a small update on 4 Nov. **Window:** stub Q4-26 + 2027–2029; no roll. BZ F27 expires 30 Nov; ICE gasoil X26 ~12 Nov.
- **Why this run:** stale after 7 Nov; the 15% front trigger fired (BZ F27 94.62 on 4 Nov vs 113.43 on 30 Oct, threshold 96.42; 91.49 on 10 Nov); the planned 7 Nov follow-up never ran.
- **Stale after 30 Nov 2026** (shorter than the 30-day rule): OPEC+ meets 29 Nov with 2027 quotas expected; F27 expires 30 Nov; the lame-duck strike window runs to 3 Jan. The OPEC MOMR (11 Nov) and IEA OMR (13 Nov) are read at that run unless one revises demand by > 0.5 mb/d for a year in the window (then a full update at once).
- **Series (skill Benchmarks), unchanged:** Brent = ICE Brent front-month futures (NYMEX BZ); diesel crack = NYMEX ULSD front × 42 − Brent front, same calendar month; jet crack = NWE jet CIF − Brent.
- **Brief input checked:** F27 4–6 Nov settlements confirmed; "~93.6 on 9 Nov" rejected (settlement 92.57, range 90.63–98.42); "2027 strip ~83 on 9 Nov" confirmed in substance (82.44); "strikes highly unlikely", "no signed deal", continuing attacks and the JPMorgan surplus confirmed; "toll demand dropped, denied by a Qatari official" partly (the official called the reported details inaccurate).
- **Data gaps `[?]`:** Kpler Hormuz week to 4 Nov, and the scope of the week-to-8-Nov figure; EIA WPSR week to 6 Nov (not out; API +9 mb from market sources); FRED Dated proxy after 3 Nov; OPEC MOMR and IEA OMR not out at writing; NWE jet crack after 16 Oct; November ARA stock levels, Singapore and China stocks; East–West throughput, Murban–Dubai, freight cost re-read; TTF quarter, season and year contracts (month averages used `[A]`), EUA price; gasoil V28 (interpolated `[A]`); the Russian diesel quota decree.
- **Oldest inputs:** IEA OMR (14 Oct); jet regrade (16 Oct); Kpler Gulf export split (data to 28 Sep).

## Conclusion

- **Oil Market BBB changed on 11 Nov: Base Brent 2027 is 84 (cut $4, −4.5%: above the $3 minimum, below the 15% recalibration trigger).** Every other Bear, Base and Bull Brent and crack path, the mid-cycle values, jet, Brent–WTI from 2027 and the weights (25/50/25, convention) stay; the stub moves mechanically.
- **Base in two sentences:** armed normalisation without a deal, with Brent **84 → 77 → 72** (mid-cycle 70), falling from ~89 in Q1-27 to ~80 in Q4-27. The ULSD crack stays at **70 → 48 → 33** (mid-cycle 25), because the product shortage outlasts the crude premium.
- **Why 84 (several independent data points, mostly physical):** the physical premium is gone (Dated proxy − front +3.4 on 3 Nov, from +20.5 on 14 Oct); supply recovers faster under the same no-deal mechanism (EIA, HSBC, JPMorgan, Vortexa); the 2027 strip repriced and held (81.2 on 10 Nov); the EIA's comparable no-deal path is $86 spot ≈ $84 futures `[A]`. Detail under Brent.
- **Why not more, and not Bear:** no deal is signed and Iran says it is not negotiating; the strait is still contested (Kpler 7.82 mb/d; ships hit 10 Nov; Houthi missiles on Riyadh 8 Nov); US commercial crude is 410 mb, the lowest end-October since 2014; the EIA raised its 2027 Brent by $2 and its 2027 diesel by 12%. The cut is front-loaded (Q1-27 89, Q4-27 80); 2028 and 2029 stay.
- **Main Bear catalyst:** a durable Iran–USA deal plus OPEC+ market-share quotas — **closer, not triggered.** Trump held off new strikes on 9 Nov after appeals from Qatar's PM and called renewed war "highly unlikely" while talks progress; a Democratic Congress sits from 3 Jan; Russia–Ukraine talks resumed in Abu Dhabi on 10 Nov (sanctions relief would add Russian barrels).
- **Main Bull catalyst:** renewed strikes with retaliation against Gulf energy infrastructure — **further away** (strikes on hold), but the tail is live: attacks on ships continue, the Houthis hit Riyadh, the blockade stays, and the window runs to 3 Jan.
- **Diesel: crack paths unchanged.** The front crack held at 82.0 (10 Nov) while Brent fell; the refining trigger fired (Russia), and the EIA expects wider 2027 cracks, but the 2027 crack forward is 67.8 and Russia plans larger diesel exports, so no path moves.

## Scenario definitions

Catalysts and mechanisms as tested on 11 Nov. Signpost status is in the monitoring table.

| Scenario | Weight (convention) | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|
| **Bear** | 25% | **Supply:** durable Iran–USA deal (blockade lifted, Iranian barrels back) and OPEC+ 2027 quotas set for market share. **Enablers:** Democratic Congress from 3 Jan 2027 presses to end the war through funding and war-powers votes; a Russia–Ukraine settlement with sanctions relief adds Russian crude and products. **Products:** Russia restores diesel exports faster than its refinery repairs suggest. **Demand:** recession after the energy shock | The agencies' 4–5 mb/d 2027 surplus materialises. Stocks rebuild quickly and the curve flips to contango. Gulf, Russian and Chinese product exports return and the crack collapses towards its normal band | Q1 2027 (a deal could be signed in Nov–Dec 2026; barrels follow after mine clearance and insurance) | Ceasefire signed and holding > 60 days · Brent M1−M4 < $2 · Dec-27 < $70 · ME refined-product exports (IEA) > 3.3 mb/d · Russian diesel exports > 0.6 mb/d · PMIs < 48 |
| **Base** | 50% | Armed normalisation: war without a deal; crude moves mostly via bypass and escort, with the Gulf and Gulf of Oman contested; product shortage persists into 2027 | ME crude to market ~15–16 mb/d (ME oil incl. bypass ~22–24 mb/d), mostly via East–West/Yanbu and escorted shuttles. Hormuz itself is volatile. ME output outside Iran back near pre-war by mid-2027 (EIA assumption, 10 Nov); Iran stays constrained. Gulf product exports are repaired gradually through 2027. China exports at or below quota; Russian exports recover only as refineries are repaired. ~1 bn bbl of restocking absorbs much of the 2027 surplus | Ongoing | ME crude incl. bypass ≥ 15 mb/d · East–West pipeline ≥ 5 mb/d · ME refined-product exports (IEA) towards ~2.6 mb/d by mid-2027 · China monthly quotas ~3.5–4 Mt · ULSD crack < $65 by mid-2027 |
| **Bull** | 25% | **Supply:** renewed US (or joint US–Israeli) strikes; Iranian/Houthi retaliation against Ras Tanura/Abqaiq/Khurais/East–West/Yanbu/Fujairah; escort and ship-to-ship system fails. **Products:** China cuts quotas again; Russian repairs fail under renewed strikes | 3–5 mb/d of crude lost again with stocks still low, so price must ration demand. Product shortage deepens; record Dated premium | Window mostly in the lame duck to 3 Jan 2027. Strikes on hold since 9 Nov (Trump, after the Qatar meeting); limited strikes without energy retaliation (Qeshm, 2 Nov) are not this catalyst | Hormuz crude < 8 mb/d for two weeks · East–West pipeline down again · ME crude incl. bypass < 13 mb/d · Saudi production or export facility hit with lasting loss · Gulf of Oman ship-to-ship/escort shuttle suspended · ULSD crack > $100 sustained · Dated–futures > $30 sustained · China monthly quota < 2 Mt |

## Brent ($/bbl) — point (range)

| Scenario | Stub | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|
| Bear | 97.1 | 65 (60–70) | 60 (55–65) | 60 (55–65) | 61.7 | 60 (55–65) |
| **Base** | **97.1** | **84 (77–91)** | **77 (70–85)** | **72 (65–80)** | **77.7** | **70 (65–75)** |
| Bull | 97.1 | 118 (105–130) | 102 (90–115) | 90 (80–100) | 103.3 | 82 (75–90) |

**Stub (10 Nov settlements), identical across scenarios:**
- **Brent 97.1:** October 108.34 (actual); November 93.55 (seven settlements 2–10 Nov: 104.77 / 103.60 / 94.62 / 98.29 / 98.32 / 92.57 / 91.49, then F27 91.49 for the remaining 14 of 21 trading days); December 89.45 (G27).
- **Crack 85.1:** October 92.85 (actual); November 82.49 (daily HO Z26 − BZ F27 80.94 / 86.69 / 82.01 / 84.49 / 83.61 / 84.45 / 82.01, then 82.01); December 79.98 (HO F27 − BZ G27).
- **Brent–WTI 7.0:** October 10.35; November 5.95 (daily BZ F27 − CL Z26, then 5.45); December 4.59 (BZ G27 − CL F27 84.86).

**Anchors:**
- **Forward (10 Nov settlements, full-year front mapping) `[F]`:** **81.2 / 73.9 / 71.2.** Base is $2.8, $3.1 and $0.8 above it; every gap is below $5. The 2027 quarters are 86.2 / 82.4 / 79.3 / 77.0, a $9.2 slope. The 2027 strip settled 82.9 / 83.6 / 85.0 / 82.4 / 81.2 on 4–10 Nov.
- **EIA STEO (10 Nov; model completed 5 Nov; spot basis) `[E]`:** 2026 $97; **2027 $86**; about $100 for November–December; below $90 in Q2-27; **$77 in Q4-27**. Base 84 is $2 below; on a futures basis the EIA path is nearer $84 `[A]`, because the EIA's spot is a Dated-type assessment that carried a premium all autumn (October spot $124 against ~$108 futures).
- **Other houses `[E]`:** JPMorgan sees a surplus since September, no new price forecast found; FGE (Fesharaki, 10 Nov) sees no deal; Goldman (17 Sep note, via search summary): 2027 about $87 in a disruption case and $64 in a peace case; older views HSBC $85 (Sep), Wood Mackenzie ~$78 (Jun), Citi $65 (undated).

**Test of Base (Step 8):**
- **Evidence for a lower Base, all seen and independent of each other (physical prices, agency, bank, futures):**
  - Dated − futures +2.6 (2 Nov) and +3.4 (3 Nov), against +20.5 on 14 Oct and +9.2 on 27 Oct `[F, FRED/EIA spot vs Yahoo]`. A Q1-27 Base of 95 needed prompt tightness the physical market no longer shows.
  - EIA (10 Nov): Middle East crude shut-ins 2.5 mb/d in October (10.9 at the May peak); Middle East output outside Iran back to pre-war by mid-2027.
  - HSBC (4 Nov): Saudi crude 8.3 mb/d in Q4-26 and 9.8 in 2027, ~10 by mid-2027 (raised by 1–2 mb/d).
  - JPMorgan (4 Nov): Middle East exports ~20.7 mb/d in October; market surplus 1.1 mb/d in September and 1.4 in October. Vortexa: Gulf product loadings ~3 mb/d in October, from ~1 in May.
  - The forward sat at or near 83 for five sessions and closed at 81.2.
- **Evidence against a lower Base (a renewed loss of barrels): not seen.** Kpler Hormuz oil 7.82 mb/d (week to 8 Nov) against 7.3 (crude, week to 28 Oct), no fall; no Saudi facility has lost output; US crude stocks low but no longer drawing (API +9 mb, unverified).
- **Size:** −$4 to 84, set in H1-27 where the premium was. A larger cut (to the strip, 81) would price part of a deal into the no-deal case. 2028 (77, forward 73.9) and 2029 (72, forward 71.2) do not move: the only evidence is the curve, and the gaps (−3.1, −0.8) are below $5.
- **Rules carried into this run:** the 31 Oct conditional up-rule (strip ≥ 93) is void; the downside retest rule (< 83 for a week without a signed deal) was not formally met (below 83 on 3 of 5 sessions, 4–10 Nov average 83.03), but the 10 Nov gap (−6.8) exceeded $5 and Base was retested in this full update; the Bear catalyst (a signed and holding deal) is not met, so Base stays the no-deal case. New retest rules are in the monitoring table.
- **Why Base sits $2.8 above the strip `[A]`:** the strip blends outcomes; with strikes on hold and Qatar mediating it prices part of a Bear outcome, which Base excludes by definition. Base 84 is in line with the EIA's comparable no-deal path.
- **Range 77–91:** a stop-start blockade with occasional hits (upper half) or quicker Gulf normalisation without a signed deal (lower half). The 10 Nov forward (81.2) is inside it.

**Mid-cycle 70 `[A]`:**
- **10 Nov settlements `[F, ICE via Barchart]`:** Dec-30 **69.06**, Dec-31 **67.70**, Dec-34 **64.24**, H35 64.05.
- The 4–10 Nov sell-off faded with maturity (Dec-27 −7.2, Dec-30 −1.6, Dec-31 −0.6 vs 3 Nov; Dec-34 +0.9): the long end did not price a structurally lower world.
- Brent's 2015–2025 median is ~$66; marginal non-OPEC full-cycle cost is $60–65 WTI `[E]`. We add a post-war structural premium (restocking, higher risk inventories).

## Year 1 by quarter ($/bbl)

Shape from the **10 Nov** forward, rescaled (multiplicatively) to each scenario's 2027 average: Brent 86.2 / 82.4 / 79.3 / 77.0; crack 76.3 / 68.9 / 65.2 / 60.7.

| Scenario | Brent Q1 / Q2 / Q3 / Q4 | Diesel crack Q1 / Q2 / Q3 / Q4 |
|---|---|---|
| Bear | 69 / 66 / 63 / 62 | 39 / 36 / 34 / 31 |
| **Base** | **89 / 85 / 82 / 80** | **79 / 71 / 67 / 63** |
| Bull | 125 / 120 / 115 / 112 | 124 / 112 / 106 / 98 |

- The quarters average to the annual values (65 / 84 / 118 and 35 / 70 / 110).

## Distillate cracks ($/bbl) — point (range)

| Scenario | Diesel (ULSD−Brent) 27 / 28 / 29 / mid-cycle | Jet (NWE−Brent) 27 / 28 / 29 |
|---|---|---|
| Bear | 35 (25–45) / 25 (18–32) / 20 (15–25) / 18 (14–22) | 30 (20–40) / 21 (15–28) / 16 (12–22) |
| **Base** | **70 (58–82) / 48 (38–58) / 33 (25–44) / 25 (20–30)** | **60 (45–75) / 40 (30–50) / 28 (20–35)** |
| Bull | 110 (90–130) / 75 (55–90) / 45 (35–55) / 35 (28–40) | 105 (80–130) / 70 (50–85) / 40 (30–50) |

- **Historical band, ULSD−Brent (quarter-end 2015–2025) `[F]`:** median $18, interquartile range $14–24; the crisis years 2022–23 averaged $47.
- **Forward vs Base (10 Nov settlements) `[F]`:** 2027 **67.8** vs 70 (−2.2; Q1 76.3 → Q4 60.7); 2028 45.2 vs 48 (−2.8); 2029 37.7 vs 33 (+4.7).
  - The 2029 HO months have zero open interest except F29 (81 lots) and Z29 (64 lots), and on 10 Nov they all moved by the same −2.86 ¢/gal: the 2029 settlement is an extrapolated mark, so the gap does not move Base. The retest signpost (OI > 1,000 lots at > $40) is not met.
  - The front crack held while crude fell: HO Z26 − BZ F27 was 82.97 on 30 Oct and **82.01** on 10 Nov.
- **Test of the crack path (Step 8):**
  - **For a higher crack:** the EIA (10 Nov) raised 2027 retail diesel from $4.49 to $5.03/gal (+12%) while raising Brent by only $2, and expects "wider product crack spreads in 2027" `[E]` — roughly +$20/bbl on its 2027 diesel margin `[A]`; Russian refining runs cut by up to ~1.5 mb/d (Refining below); Gulf product exports still ~half of normal.
  - **For a lower crack:** the traded 2027 crack fell 2.7 in the week to 10 Nov; Russia plans ~2.15 Mt of diesel exports in November (from ~0.5 Mt); ARA gasoil imports rose to 400 kb/d; the switching support faded (TTF −18%).
  - **Result:** the evidence points both ways, and the forward sits within $3 of Base for 2027–28. The crack paths are kept.
- **Gasoil cross-check (ICE gasoil, Barchart `LF*0`, settlements 10 Nov; mapping LF(m+1) ÷ 7.45 − BZ(m+2)) `[F]`:** front LFZ26 $1,227.75/t = $164.8/bbl, minus BZ F27 91.49 = **73.3**, vs ULSD 82.0 for the same month (Europe −8.7).

  | $/bbl | Nov–Dec 26 | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2027 | 2028 (Jan–Nov) |
  |---|---|---|---|---|---|---|---|
  | Gasoil − Brent | 71.7 | 65.5 | 58.1 | 52.5 | 47.1 | 55.8 | 35.6 |
  | ULSD − Brent | 81.0 | 76.3 | 68.9 | 65.2 | 60.7 | 67.8 | 45.7 |
  | Gap (Europe − US) | −9.3 | −10.8 | −10.8 | −12.7 | −13.5 | −12.0 | −10.1 |

  - **Reading `[A]`:** the US is the tighter distillate market by $9–14 through 2028. Base 70 (ULSD basis) is $2 above the ULSD curve and $14 above gasoil. Downstream analyses that price European diesel apply about −$11 to the ULSD crack for 2027–28. The 2028 gasoil months are thin; V28 is interpolated.
- **Gas-to-oil switching (context, extra support):** EEX TTF month futures, 10 Nov settlements `[F, Barchart]`: Dec-26 84.710, Jan-27 84.549, Feb 84.125, Mar 80.802, Apr 68.200, May 64.845, Jun 62.709, Jul 62.134, Aug 61.518, Sep 60.981, Oct 59.478, Nov 59.199, Dec-27 59.004 €/MWh. Q1, Summer and Cal-27 are month averages `[A]`. ICE gasoil 10 Nov `[F, Barchart]`; EUR/USD **1.1214** = EURNOK 10.6155 ÷ USDNOK 9.4663 `[F, Norges Bank, 10 Nov]`; 11.94 MWh/t; gasoil months mapped LF(m+1).

  | Period | Gasoil €/MWh | TTF €/MWh | Ratio | Band |
  |---|---|---|---|---|
  | Dec-26 (LFF27 vs TTF Dec) | 88.8 | 84.7 | **1.05** | Partial switching |
  | Q1-27 (LFG/H/J27 vs TTF Jan–Mar) | 84.4 | 83.2 | **1.02** | Partial switching |
  | Summer-27 (LFK–V27 vs TTF Apr–Sep) | 75.7 | 63.4 | 1.19 | Partial switching |
  | Cal-27 (LFG27–F28 vs TTF Jan–Dec) | 76.2 | 67.3 | 1.13 | Partial switching |

  - **Reading `[A]`:** TTF fell ~18% as the Hormuz risk to Qatari LNG eased, faster than gasoil; gas is no longer dearer than gasoil for the winter. The context signpost (ratio < 1.0) is not crossed, and the retest condition (ratio < 1.0 for two weeks while the ULSD Q1-27 forward is > 80) is not met (1.02; Q1 crack 76.3), so the H1-27 crack quarters do not lean higher. Switching volume is not quantified `[?]`; the EUA price is not sourced `[?]`.
- **Jet:** 60 / 40 / 28, low confidence. S&P Global Platts (19 Oct, via search summary, not opened) `[E]`: the European jet crack moved above the diesel crack, by up to $11.75/bbl on 16 Oct (jet FOB FARAG barge vs ULSD FOB barge). Cross-check `[A]`: the 2027 European gasoil crack is 55.8, and a positive but fading regrade puts NWE jet near 60, consistent with Base. Russian jet exports are banned to 30 Nov.

## Distillate sensitivity

**Diesel price = Brent + ULSD crack**, $/bbl ($/t at 7.45 bbl/t).

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

**Decomposition of the ULSD price change** (front month, Yahoo settlements) `[F]`:

| Period | Δ ULSD | Δ Brent | Δ Crack |
|---|---|---|---|
| Pre-war (27 Feb) → 10 Nov (front series HO Z26 / BZ F27) | +61.4 | +19.0 (31%) | +42.4 (69%) |
| 30 Oct → 10 Nov, same contracts (HO Z26 / BZ F27) | −22.9 | −21.9 | −1.0 |
| 3 Nov → 10 Nov, same contracts | −16.8 | −12.1 | −4.7 |

**Reading:** the sell-off since 30 Oct came almost entirely out of crude (Brent −21.9, crack −1.0), and crude's share of the war-time diesel rise is down to 31% (51% on 30 Oct). The market priced out the crude risk premium but not the product shortage. That fits the Russian refinery outages, half-normal Gulf product exports and the EIA's higher diesel path, and it is why the Brent path moves while the crack path stays.

## Drivers

### Crude supply (incl. disruptions in barrels reaching market)

- **Iran–USA diplomacy (Bear side) `[E]`:**
  - **9 Nov:** Trump met Qatar's PM, Sheikh Mohammed bin Abdulrahman, at the White House and afterwards said he would hold off new strikes after appeals from regional leaders. He said "I think it's going to be ending fairly soon", that Tehran is "talking very politely", and that the Gulf states "prefer the status quo", i.e. the blockade (CNBC, The National, 10 Nov). He told CNN a return to war was "highly unlikely" while talks on the nuclear file and Hormuz progress (via several reports, not opened).
  - **The blockade stays** (Trump; IG, 10 Nov).
  - **Hormuz plan:** two diplomatic sources said Iran approved a plan to reopen the strait and appeared to drop its demands to control it and to charge tolls; a Qatari official called the reported details "inaccurate" and said the US and Iran were still discussing details with mediators (9 Nov; TokenPost, 10 Nov, no wire named). Talks still rest on Iran's seven-step plan of September.
  - **Iran:** the security official Rezaei says Tehran is not negotiating with Washington and the strait stays closed unless US terms are met (search summaries); an Iranian security official told Reuters no talks were taking place (11 Nov).
  - **FGE (Fesharaki):** the gap "cannot be bridged" (CNBC, 10 Nov). **No signed deal as of 11 Nov.**
- **Attacks and escalation (Bull side) `[E]`:**
  - **10 Nov:** UKMTO reports a tanker struck north-east of Lima, Oman. The IRGC Navy says two tankers caught fire after hitting mines on an "unauthorized route"; an Iranian headline later says five tankers and a tug (unverified) (Reuters, 11 Nov).
  - **WINEP:** 37 ships attacked in October, the most of the war, and "little sign" of fewer in November.
  - **US strikes:** a further round of "minor" US strikes on air defences near the strait is reported (CNBC/CBC); whether it is the 2 Nov Qeshm strike or a new one is not clear `[?]`. No retaliation against energy infrastructure.
  - **8 Nov, Houthi missiles on Riyadh:** falling debris caused minor damage to the **Aramco Tower** (an administrative building in KAFD), no injuries (Saudi Energy Ministry); a missile toward the Eastern Province was intercepted; the coalition struck launchers in Saada; the Houthis claim six operations against Aramco facilities, Riyadh airport and military sites (CNN, Middle East Eye). **No production or export loss is reported.**
- **Flows `[E]`:**

  | Source | Scope | Value | Period |
  |---|---|---|---|
  | Kpler (The National, 10 Nov) | Hormuz oil flows excl. Iran; scope (crude only or incl. products) not stated | **7.82 mb/d**, ~46% of a pre-war 17.14 | Week to 8 Nov |
  | Kpler (CNBC, 30 Oct) | Hormuz crude | 7.3 | Week to 28 Oct |
  | Kpler | Hormuz crude | not found `[?]` | Week to 4 Nov |
  | Kpler | Gulf crude + condensate via Hormuz, Red Sea and Gulf of Oman | 16.1 (Sep 17.09) | October |
  | Vortexa | Gulf seaborne crude + condensate / products | 14.0 / 3.1 | October |
  | FGE (Bloomberg, 10 Nov) | Gulf crude incl. pipelines / products, share of pre-war | 80–85% / 35–40% | Early November |
  | EIA STEO (10 Nov) | ME crude shut-ins | 2.5 mb/d (peak 10.9 in May), flat to end-2026 | October |
  | JPMorgan (4 Nov) | ME oil exports | ~20.7 (March low 9.8) | October |

  - The 7.82 and 7.3 figures are not like-for-like: the pre-war bases differ (17.14 vs 13.5–16).
  - LSEG (10 Nov): even after a deal, flows depend on mine clearance and insurance.
- **ME crude incl. bypass (Bull < 13, Base ≥ 15) `[A]`:** Kpler October **16.1**, so Base is met on the monthly figure; Vortexa (14.0) and FGE (80–85% of a ~16.5–17 pre-war, ≈ 13–14.5) are lower. The composite is **Base on Kpler and borderline on the other trackers**; none is below the Bull line.
- **Saudi Arabia `[E]`:** HSBC (4 Nov): Aramco crude Q4-26 8.3 mb/d and 2027 9.8, ~10 by mid-2027. EIA: the East–West pipeline has restarted, and Middle East exports rose slightly in October. No East–West throughput figure since 6 Oct (5.8 mb/d) `[?]`. October exports by tracker: Kpler 5.4, Vortexa ~6.5, TankerTrackers 6.99.
- **OPEC+ `[F/E]`:** the 1 Nov meeting held per-country December targets (the seven at 31.01 mb/d). The 1.65 mb/d of 2023 voluntary cuts are fully unwound; the 2 mb/d of 2022 cuts stay to end-2026. The next meeting, **29 Nov**, is expected to set the 2027 quotas. EIA: OPEC liquids 24.5 mb/d in 2026 and 28.4 in 2027.
- **Iraq, Iran, Libya:** Basrah ~3.0 mb/d in October; Iranian oil on water outside the blockade zone is zero (Kpler, 28 Oct); Libya's Hamada–Zawiya valve shut (~31 Oct), volume not stated `[?]`.
- **Russia `[E]`:** Russia–Ukraine talks held in Abu Dhabi on 10 Nov, the first since February (Reuters); sanctions relief is a Bear enabler. A drone fire at Ust-Luga port injured three on 11 Nov; the loading effect is not stated `[?]`. Refinery outages under Refining.
- **US `[E]`:** crude production 13.9 mb/d in 2026 and a record 14.3 in 2027 (EIA, 10 Nov). The 3 Nov midterms gave Democrats the House and Senate, seated 3 Jan 2027, without a veto-proof majority; the FY27 stopgap expires 11 Dec. No law changes for oil before 3 Jan; from then, funding and war-powers pressure builds (a Bear enabler). Production policy unchanged; SPR ~282.6 mb with no refill funding.
- **For BBB `[A]`:** no barrels returned in November beyond the October levels, and none were lost. The evidence that sets Base is the outlook: a faster recovery outside Iran (EIA, HSBC) and the collapse of the physical premium. Diplomacy enters only through the Bear catalyst's timing.

### Demand

- **EIA STEO (10 Nov) `[E]`:** world consumption 102.4 mb/d in 2026 (−2.0 y/y) and **104.4** in 2027 (+2.0), the 2027 figure revised −0.2 (below the 0.5 trigger). World GDP 3.1% in 2026 and 2027.
- **JPMorgan (4 Nov):** demand −3.3 mb/d since the war began `[E]`.
- **IEA (Oct):** 102.4 (2026, −2.6) and ~104.4 (2027, +2.0). **OPEC (Oct):** 105.7 / 108.3, with 2027 growth ~2.55 mb/d. The OPEC MOMR (11 Nov) and IEA OMR (13 Nov) are to be read.
- **US:** October CPI came in hotter than expected (10 Nov, AP) and raises the chance of a Fed hike — a demand-side tail for the Bear case; no path change.
- **Price effect:** front Brent at $91–98 and diesel at ~$174–190/bbl in November still mean demand destruction in Q4-26, though less than in October ($108 Brent, ~$200 diesel).

### Inventories

- **US `[E/F]`:** EIA STEO: commercial crude **410 mb at end-October, the lowest end-October since 2014**, below the 5-year average until mid-2027. API, week to 6 Nov: crude **+9 mb** (market sources via Reuters, 11 Nov; **unverified**); the EIA WPSR for that week was not out `[?]`. Last EIA week (to 30 Oct): crude −0.87 to 409.8 mb; distillate −3.6 to 99.3 mb, ~13% below the 5-year average; utilisation 94.5%.
- **Global `[E]`:** EIA: stocks drew 1.2 mb/d in 3Q26, start to build in 4Q26, and build 3.5 mb/d in 1H27. IEA (Sep): −509 mb vs pre-war; observed −10 mb in September.
- **ARA `[E]`:** gasoil imports **400 kb/d** in November to date vs 257 kb/d in October: India 39%, Saudi Arabia 35%, Canada 12% (Vortexa via ENGINE, 6 Nov). Last stock level is the week to 15 Oct (gasoil 1,782 kt, jet 494 kt) `[?]`.
- **Singapore:** no data `[?]`. **China:** no data `[?]`; Bloomberg (10 Nov): diesel exports may stay curbed by low domestic stocks.
- **Reading `[A]`:** US crude is low but stopped drawing (API, unverified), and Europe is drawing more imports. Stocks are no longer tightening at the margin, which fits a lower H1-27 Base. The distillate stock deficit is intact, which fits an unchanged crack.

### Refining and distillate supply (incl. regional balances in mb/d)

- **Russia (refining trigger) `[E]`:** renewed Ukrainian drone strikes since late October have disrupted ~**30%** of capacity (Reuters, 10 Nov, two industry sources). Nine of 35 major refineries were hit in a week (Ryazan, Yaroslavl and Volga plants). Nameplate ~300 kt/d (**2.2 mb/d**) out of ~930 kt/d; runs were ~700 kt/d (~5.1 mb/d) at end-October; the actual processing cut is **up to 200 kt/d (~1.5 mb/d** at 7.33 bbl/t). Kirishi (the second-largest refinery) was set on fire on 9 Nov. Several regions report fuel shortages and petrol rationing. A Trump-announced energy-strike ceasefire did not take hold at end-October.
- **Russian diesel exports `[E]`:** about 2.15 Mt planned for November (~0.52 mb/d) vs ~0.51 Mt in October (Kyiv Post, citing Kpler/LSEG tanker data); Novak: up to 3.5 Mt by end-2026. Diesel tankers are dropping their US destinations (Al Jazeera, 7 Nov). The quota decree has not been seen `[?]`.
- **Barrels `[A]`:** a ~1.5 mb/d run cut at a ~35–40% diesel yield is ~0.5–0.6 mb/d less Russian diesel output while it lasts; earlier strikes were repaired in 2–6 weeks. The quota plan points the other way for exports. Russian crude that cannot be refined goes to export: crude-bearish and crack-supportive. **Trigger "refining capacity > 0.5 mb/d": fired**, tested under Distillate cracks: no path change. The Bear product signpost (Russian diesel exports > 0.6 mb/d) is **not crossed**.
- **Gulf:** no verified refinery outage. Gulf product loadings ~3 mb/d in October, half of pre-war (Vortexa) `[E]`.
- **EIA (10 Nov) `[E]`:** product markets face "continued supply constraints" through end-2027, and wider 2027 cracks should keep US refinery runs elevated. 2027 retail diesel $5.03/gal.
- **China:** third 2026 quota batch 4.55 Mt (9 Oct). The Bull signpost (< 2 Mt/month) is far away.
- **US:** utilisation 94.5%; distillate −3.6 mb (WPSR week to 30 Oct).
- **Freight and price effects** (rates are covered in [[oil-shipping-bbb]]):
  - **Brent–WTI:** November same-month **5.45** (BZ F27 − CL Z26, 10 Nov). The 2027 strip spread is **3.9** (mid-quarter shortcut: Feb 4.13, May 3.87, Aug 3.72, Nov 3.83); the freight premium in the crude spread is fading. The 2027 Base 6.0 is kept: the 2.1 gap is below the $3 minimum; retest if the strip stays below 4 at the next run.
  - No freight cost re-read (VLCC Gulf of Oman → Asia ~$21/bbl in October) `[?]`. No Murban–Dubai figure `[?]`.
- **Regional balance:** Europe imports ~1.5 mb/d of diesel (about half from the US), and the US–Europe crack gap of $9–14 keeps the transatlantic arbitrage open.

### Forward curve (M1−M4, classification, long end, Dated–futures spread)

- **Brent M1−M4 (10 Nov) `[F]`:** F27 91.49 − K27 84.79 = **+$6.70 → Clearly tight**, narrowing (daily 4–10 Nov: +7.87, +10.30, +8.88, +6.66, +6.70). With US crude stocks no longer falling (API, unverified), the reading moves from "strong physical tightness" towards "backwardation, inventories building: normalisation may be under way". A spread below $5 for two weeks would be a regime change (recalibration trigger).
- **Long end (ICE Brent via Barchart `CB*0`, 99 months to H35, 10 Nov settlements) `[F]`:**

  | Contract | 10 Nov |
  |---|---|
  | Dec-27 | 77.64 |
  | Dec-28 | 72.76 |
  | Dec-29 | 70.58 |
  | Dec-30 | 69.06 |
  | Dec-31 | 67.70 |
  | Dec-34 | 64.24 |

  - The curve flattened in the 30 Oct–10 Nov sell-off, and the long end from 2031 is unchanged or higher.
- **Overlap check:** Barchart CB 10 Nov settlements equal Yahoo BZ for every month both carry (F27–H28, Z28) `[F]`; Barchart HO equals Yahoo HO for every shared month (Z26–F28, Z28); Barchart rows still trading on 11 Nov were read as last price − change = 10 Nov settlement, and they match Yahoo.
- **WTI (Yahoo, 10 Nov):** Z26 86.04 · F27 84.86 · H27 82.03 · M27 78.48 · U27 75.52 · Z27 73.12 · Z28 68.74 · Z29 66.24.
- **Diesel crack forward (full-year front mapping) `[F]`:** stub 85.1; 2027 67.8 (Q1 76.3 → Q4 60.7); 2028 45.2 (thin but traded); 2029 37.7 (exchange mark, zero open interest).
- **Dated–futures** (Dated proxy = EIA Brent spot, FRED `DCOILBRENTEU`, minus the front future the same day) `[F]`:

  | Date | Dated proxy | Front future | Spread |
  |---|---|---|---|
  | 2 Nov | 107.39 | 104.77 (F27) | +2.6 |
  | 3 Nov | 107.03 | 103.60 (F27) | **+3.4** |

  - FRED was last updated on 4 Nov, with no value after 3 Nov. The physical premium (+20.5 on 14 Oct) is nearly gone; the Bull signpost (> $30 sustained) is far away. EIA October Brent spot average: $124 (spot basis, context).
- **USD and NOK `[F, Norges Bank]`:** USD/NOK 9.4663 (10 Nov; 9.2303 on 3 Nov): the NOK weakened 2.6% as oil fell; EUR/USD 1.1214. The dollar did not drive the oil move.

### Balance check (implied stock change per scenario and year vs IEA/EIA)

| mb/d, + = build | 2026 | 2027 | 2028 | 2029 | Comment |
|---|---|---|---|---|---|
| IEA (Oct) | −1.7 | ~+4.0 | — | — | Derived: supply 100.7 / ~108.4, demand 102.4 / ~104.4 `[E/A]`; the November OMR is due 13 Nov |
| EIA (Nov) | −0.7 | **+4.0** | — | — | Supply 101.7 / 108.4, demand 102.4 / 104.4; 1H27 +3.5 `[E]` |
| JPMorgan | Sep +1.1, Oct +1.4 | — | — | — | Monthly estimates; conflict with the IEA (Sep −0.8) `[E]` |
| OPEC (Oct) | — | — | — | — | Call on DoC crude 42.1 → 43.9 mb/d; no balance stated `[E]` |
| Base | ~−1.5 | **+1.5 to +2.5** | +0.5 to +1.0 | 0 to +0.5 | Flows incl. bypass near pre-war on monthly average; ME ex-Iran back by mid-2027; attack risk keeps restocking and risk inventories high; about half of the surplus goes to strategic refill; stocks normal by end-2028 `[A]` |
| Bear | — | +4 to +5 | +1.5 to +2.5 | ~0 | Stocks rebuilt during 2027 → contango; OPEC+ cuts in 2029 `[A]` |
| Bull | — | −1 to 0 | −0.5 to +0.5 | +0.5 | Low stocks force price rationing `[A]` |

**Reading `[A]`:**
- **Base 2027 +1.5 to +2.5 mb/d:** the faster recovery outside Iran (EIA, HSBC) adds ~0.5 mb/d of builds, ~180 mb over the year, consistent with Base 84. End-2027 stocks stay below pre-war (−509 mb hole plus ~1 bn bbl of strategic and commercial restocking), so Base keeps a backwardated, above-Bear path.
- **Base 2026 ~−1.5:** the EIA is at −0.7 and JPMorgan counts a surplus, against the IEA at −1.7.
- **EIA 2027 surplus +4.0** (cut by 1.0 mb/d in the November STEO through supply, not demand, so no trigger). The EIA's +4.0 against its own $86 shows that the agency, too, expects most of the surplus to be absorbed by restocking.

## Signposts and monitoring

| Signpost | Threshold (Bear / Bull) | Now (11 Nov) | Direction |
|---|---|---|---|
| Hormuz crude (Kpler 7d) | Bear ≥ 13 · Bull < 8 for two weeks | Kpler 7.82 (week to 8 Nov; scope not stated, pre-war base 17.14); week to 4 Nov not found; 7.3 (crude, week to 28 Oct) | Touched twice, not confirmed (series differ, a week missing); no fall in barrels |
| ME crude incl. bypass | Bull < 13 · Base ≥ 15 | Kpler October 16.1; Vortexa 14.0; FGE 80–85% of pre-war (≈ 13–14.5) | Base on Kpler; borderline on others |
| East–West pipeline / Yanbu | Bull if down again · Base ≥ 5 | Restarted (EIA); no throughput figure | Unconfirmed |
| Saudi facilities | Bull: facility hit with lasting loss | Aramco Tower (Riyadh, admin) minor debris damage 8 Nov; Eastern Province missile intercepted; no output loss | Not crossed |
| Tanker attacks / ship-to-ship shuttle | Bull: system fails | Tanker hit NE of Lima (10 Nov, UKMTO); IRGC claims two (later five) tankers mined; 37 ships hit in October (WINEP) | Not crossed; attacks continue |
| Iran–USA | Bear: ceasefire > 60 d · Bull: new strikes with retaliation on energy infrastructure | Strikes on hold (9 Nov); "highly unlikely" to return to war while talks progress; blockade stays; Qatar mediating; Iran denies talks; no signed deal | Bear closer; Bull further |
| US Congress | Bear support: Congress cuts war funding · Bull window: lame duck to 3 Jan | Democratic House and Senate seated 3 Jan; stopgap 11 Dec; no new vote | Unchanged |
| Russia–Ukraine | Bear enabler: settlement with sanctions relief | Talks in Abu Dhabi 10 Nov (first since February); refinery strikes continue | Watch |
| ME refined-product exports (IEA) | Bear > 3.3 · Base ~2.6 by mid-2027 | 1.9 (Sep, IEA); next OMR 13 Nov. Context, other scope: Vortexa Gulf product loadings ~3 (Oct) | Base |
| China product exports | Bull: monthly quota < 2 Mt | No new quota data; exports may stay curbed (low stocks); third batch 4.55 Mt | Base |
| Russian diesel | Bear: exports > 0.6 mb/d | Plan 2.15 Mt (~0.52 mb/d) in November vs 0.51 Mt in October; refining capacity −30% | Not crossed; two-way |
| Russian refining | Bull crack: outage lasts or spreads | 2.2 mb/d nameplate disrupted; runs cut up to ~1.5 mb/d; Kirishi hit 9 Nov | Supports crack |
| Brent M1−M4 | Bear < $2 (regime change < $5 for two weeks) | +6.70 (F27−K27, 10 Nov) | Clearly tight, narrowing |
| Dated–futures (EIA proxy) | Bull > $30 sustained | +3.4 (3 Nov) | Away from Bull |
| ULSD−Brent crack (front) | Bull > $100 sustained · Base < $65 by mid-2027 | 82.0 (Nov, 10 Nov) | Base |
| Gas-to-oil switching ratio | Bull crack: gasoil/TTF < 1.0 (energy basis) | Dec-26 1.05 · Q1-27 1.02 · Cal-27 1.13 | Not crossed |
| ULSD 2029 forward | Retest Base 2029 if OI > 1,000 lots at a crack > $40, or the 2028 crack > $55 | 37.7, zero OI (mark); 2028 45.2 | Base |
| Brent 2027 strip vs Base (armed on Base 84) | **Up:** retest if the strip is > $6 above Base (> 90) together with a crossed Bull flow signpost · **Down:** retest if the strip settles > $5 below Base (< 79) for a week without a signed deal | 81.2 (−2.8 vs 84) | Inside the band |
| Brent front 15% trigger (armed 11 Nov) | Full update if the front settles ≤ 77.8 or ≥ 105.2 (F27, ±15% vs 91.49 on 10 Nov) to 30 Nov, then G27 ≤ 76.0 or ≥ 102.9 to 10 Dec | 91.49 (10 Nov) | Armed |
| Dec-27 15% trigger | Full update if Z27 settles ≤ 66.0 or ≥ 89.3 within a month of 10 Nov | 77.64 (10 Nov) | Not fired |
| Brent–WTI (same month) | Stress > $12 | 5.45 (Nov, 10 Nov) | Normal |
| US export restrictions | Bull if imposed | Rejected | Unchanged |
| OPEC+ 2027 quotas | Bear: market-share quotas | No change; next 29 Nov | Open, 29 Nov |

**Watch before the next update (stale after 30 Nov):**
- **Iran–USA:** a signed MoU and the first reopening steps (Bear), or a strike with retaliation on Gulf energy infrastructure (Bull). Mine clearance and war-risk insurance are the physical gate even after a deal.
- **Flows:** Kpler weekly Hormuz figures (ask for the series and scope), the Kpler and Vortexa November monthly figures, and any East–West throughput number.
- **Agencies:** the OPEC MOMR (11 Nov) and the IEA OMR (13 Nov). A demand revision > 0.5 mb/d for a year in the window, or an IEA 2027 balance far from +4, means a full update at once.
- **US stocks:** the EIA WPSR for the weeks to 6 and 13 Nov (~12 and 18 Nov): is the API +9 mb confirmed; does distillate keep drawing?
- **Russia:** refinery repairs vs new strikes, the November diesel exports actually loaded, and the Abu Dhabi talks.
- **The curve:** M1−M4 below $5 for two weeks (regime change), the 2027 strip vs 79 / 90, and the front ±15%.

**Dated events:**
- **Before 30 Nov:** OPEC+ (29 Nov, 2027 quotas expected); BZ F27 expiry and the end of the Russian jet export ban (30 Nov); third US carrier (end of November).
- **Before 3 Jan:** EIA STEO (8 Dec); front ±15% trigger window to 10 Dec; FY27 stopgap expiry (11 Dec); OPEC MOMR (14 Dec; calendar sites, not confirmed on opec.org); Qatar LNG force majeure to end-December; the new Congress seated (3 Jan 2027).

## Change log

- **13 Nov 2026 — compacted to the lean-document rules (703 → 392 lines, Interface section first); no value changed.**
- **11 Nov 2026 — full update (skill 2026-10-24.4), BBB changed:** Base Brent 2027 88 → 84 (range 77–91; physical premium gone, faster recovery outside Iran, strip 81.2); stub 104.3 → 97.1, crack 88.1 → 85.1, Brent–WTI 8.0 → 7.0; Year-1 Base 89/85/82/80. All other paths, mid-cycle, cracks and weights kept; Russian refining trigger tested, no crack change. Changed yes, `affects` none.
- **4 Nov 2026 — small update (OPEC+ 1 Nov hold, US midterms), kept unchanged:** stub re-marked (Brent 110.4 → 104.3, crack 86.2 → 88.1); Bull window to 3 Jan; Bear enabler a Democratic Congress; new signposts (US Congress, downside retest, 15% front trigger).

## Appendix: sources

| Source | Content | Observed / published |
|---|---|---|
| Yahoo Finance connector (`get_quote`, `get_chart`): BZ F27–H28, Z28; HO Z26–F28, Z28; CL Z26, F27, H27, M27, U27, Z27, Z28, Z29; BZ=F, HO=F, CL=F daily | Daily settlements 2–10 Nov (2027 strip test), 10 Nov curve, stub, M1−M4, Brent–WTI, decomposition; 11 Nov intraday as context. 10 Nov daily volumes equal 9 Nov's for every contract (Yahoo artefact; prices match Barchart) | 2–10 Nov settlements / retrieved 11 Nov ~07:20 UTC |
| Barchart ICE Brent `CB*0`, NYMEX ULSD `HO*0`, ICE gasoil `LF*0`, EEX TTF month `GHMZ26` futures-prices grid (in-app browser, shadow-DOM read; cookie banner denied; sign-up popup closed; no sign-in) | Brent 99 months to H35 (`s` rows = 10 Nov settlements; rows trading on 11 Nov read as last − change); ULSD to F30 with OI; gasoil to Z32 (V28 not read); TTF Nov-26 to Oct-33 | Settlements 10 Nov / read 11 Nov |
| FRED `DCOILBRENTEU` | Dated proxy 26 Oct–3 Nov (no value after 3 Nov; last updated 4 Nov) | 3 Nov / retrieved 11 Nov |
| Norges Bank `get_exchange_rate` USD, EUR | USD/NOK 9.2303 (3 Nov) … 9.4663 (10 Nov); EURNOK 10.6155 (10 Nov) → EUR/USD 1.1214 | Fixings 3–10 Nov |
| EIA STEO pages (eia.gov/outlooks/steo/, report/global_oil.php) | Brent $97 (2026), $86 (2027), Q4-27 $77; balances 101.7/108.4 vs 102.4/104.4; shut-ins 2.5 mb/d; ME ex-Iran back by mid-2027; US crude 410 mb end-Oct; retail diesel 2027 $5.03; wider 2027 cracks; next STEO 8 Dec | Released 10 Nov (completed 5 Nov) |
| Bloomberg via Transport Topics | EIA raises 2027 diesel and gasoline forecasts; Brent $104 Nov / $99 Dec | 10 Nov |
| CNBC (10 Nov, oil prices) | Brent settled 91.49 (low 89.16), WTI 86.04; Trump quotes; FGE "cannot be bridged"; ING | 10 Nov |
| The National (10 Nov) | Brent < $90 intraday; Kpler Hormuz 7.82 mb/d week to 8 Nov (46% of 17.14, excl. Iran); Trump delays strikes; Russia–Ukraine talks | 10 Nov |
| Reuters via Business Recorder (11 Nov) | Tanker hit NE of Lima (UKMTO); IRGC mine claims; WINEP 37 ships in October; API +9 mb; Russian refining −30%; Ust-Luga drone fire; Abu Dhabi talks; LSEG mine-clearance note | 11 Nov |
| Reuters via gCaptain (10 Nov); Kyiv Independent, Atlantic Council, Pravda (search summaries) | Russian refining: nine refineries, 2.2 mb/d nameplate, runs cut up to 200 kt/d; Kirishi hit 9 Nov; fuel shortages | 10 Nov |
| Kyiv Post, Oil and Gas 360, Al Jazeera via Digg (search summaries, not opened) | Russian diesel exports: 2.15 Mt planned for Nov vs 0.51 Mt Oct (Kpler/LSEG); tankers drop US destinations; Novak 3.5 Mt | 5–7 Nov |
| Bloomberg via BusinessMirror (10 Nov) | Vortexa Gulf product loadings ~3 mb/d (Oct); FGE crude 80–85% / products 35–40% of pre-war; China diesel exports curbed | 10 Nov |
| Oil & Gas Journal (4 Nov) | JPMorgan surplus 1.1 / 1.4 mb/d; ME exports 20.7; demand −3.3; IEA counterview; HSBC Saudi output path | 4 Nov |
| TokenPost (10 Nov; no wire named) | Reported Hormuz plan (tolls, control dropped); Qatari official: details "inaccurate" | 9–10 Nov |
| CNN, Middle East Eye, Morocco World News (search summaries) | Houthi missiles on Riyadh; Aramco Tower debris damage; Eastern Province interception; Houthi claims | 8 Nov |
| Search summaries (Benzinga, CBC, World Today Journal; not opened) | Trump "highly unlikely" (CNN); Rezaei: no negotiations; strait closed unless terms met | 9–10 Nov |
| ENGINE (Insights Global / Vortexa) | ARA gasoil imports 400 kb/d Nov to date (India 39%, Saudi 35%, Canada 12%) | 6 Nov |
| S&P Global Platts (search summary, page 403) | European jet crack above ULSD barge crack, up to $11.75 on 16 Oct | 19 Oct |
| Trading Economics / MTS Insights calendars (search summaries) | OPEC MOMR 11 Nov and 14 Dec; IEA OMR 13 Nov | Calendars |
| Discovery Alert (aggregator, 5 Nov) | Tracker scopes (Kpler, Vortexa, IEA, EIA); no week-to-4-Nov figure | 4–5 Nov |
| Sources carried from 4 Nov (details in git): Barchart and Yahoo 3 Nov settlements; OPEC+ statement coverage; midterm coverage (AP calls); Reuters/Vortexa/Kpler October flows; Hydrocarbon Processing (Russian quotas); globaloilshock.com (UKMTO/JMIC) | OPEC+ 1 Nov hold; midterms; October flows (Kpler 16.1, Vortexa 14.0 / 3.1, Saudi exports by tracker); 3 Nov settlements (mid-cycle comparison) | 25 Oct–4 Nov |
| Sources carried from 31 Oct (details in git): Kpler via CNBC/Newsquawk; Gulf News trackers; House of Saud; Al Jazeera; IEA OMR Oct; EIA STEO Oct; Insights Global; Global Trade Alert; Mysteel | IEA October balance and demand; OPEC October demand; Kpler week to 28 Oct (7.3); ARA stocks to 15 Oct; China quota batch | Sep–Oct |

**Raw settlements 10 Nov `[F]`:**
- **Brent (Barchart CB = Yahoo BZ):** F27 91.49 · G27 89.45 · H27 87.71 · J27 86.16 · K27 84.79 · M27 83.53 · N27 82.35 · Q27 81.24 · U27 80.20 · V27 79.24 · X27 78.39 · Z27 77.64 · F28 76.95 · G28 76.33 · H28 75.79 · J28 75.32 · K28 74.94 · M28 74.60 · N28 74.26 · Q28 73.93 · U28 73.61 · V28 73.30 · X28 73.01 · Z28 72.76 · F29 72.51 · G29 72.29 · H29 72.13 · J29 71.98 · K29 71.82 · M29 71.65 · N29 71.46 · Q29 71.28 · U29 71.10 · V29 70.94 · X29 70.76 · Z29 70.58 · F30 70.39 · G30 70.25 · Z30 69.06 · Z31 67.70 · Z32 66.38 · Z33 65.13 · Z34 64.24 · H35 64.05.
- **Brent front daily (BZ F27):** 30 Oct 113.43 · 2 Nov 104.77 · 3 Nov 103.60 · 4 Nov 94.62 · 5 Nov 98.29 · 6 Nov 98.32 · 9 Nov 92.57 (range 90.63–98.42) · 10 Nov 91.49 (low 89.15).
- **2027 strip daily (full front mapping, Yahoo):** 3 Nov 89.71 · 4 Nov 82.91 · 5 Nov 83.61 · 6 Nov 84.98 · 9 Nov 82.44 · 10 Nov 81.21. M1−M4: 8.99 · 7.87 · 10.30 · 8.88 · 6.66 · 6.70. Per-contract 4–9 Nov settlements are in git.
- **ULSD ($/gal, Barchart = Yahoo):** Z26 4.1309 · F27 4.0341 · G27 3.9604 · H27 3.8744 · J27 3.7730 · K27 3.6799 · M27 3.5919 · N27 3.5333 · Q27 3.4831 · U27 3.4403 · V27 3.3993 · X27 3.3470 · Z27 3.2784 · F28 3.2061 · G28 3.1346 · H28 3.0693 · J28 2.9855 · K28 2.9208 · M28 2.8483 · N28 2.8033 · Q28 2.7558 · U28 2.7308 · V28 2.7218 · X28 2.7018 · Z28 2.6786 · F29 2.6551 · G29 2.6500 · H29 2.6393 · J29 2.6198 · K29 2.6059 · M29 2.5953 · N29 2.5974 · Q29 2.5979 · U29 2.5745 · V29 2.5737 · X29 2.5697 · Z29 2.5466 · F30 2.5535. Open interest: Z28 1,824; F29 81; G29–X29 0; Z29 64.
- **ULSD front daily (HO Z26):** 2 Nov 4.4216 · 3 Nov 4.5306 · 4 Nov 4.2055 · 5 Nov 4.3519 · 6 Nov 4.3317 · 9 Nov 4.2148 · 10 Nov 4.1309.
- **WTI (Yahoo):** Z26 86.04 (daily 2–10 Nov: 96.46 · 96.09 · 88.12 · 90.52 · 90.83 · 86.85 · 86.04) · F27 84.86 · H27 82.03 · M27 78.48 · U27 75.52 · Z27 73.12 · Z28 68.74 · Z29 66.24.
- **ICE gasoil ($/t, Barchart):** X26 1,280.75 · Z26 1,227.75 · F27 1,189.25 · G27 1,160.25 · H27 1,131.50 · J27 1,099.75 · K27 1,071.50 · M27 1,045.25 · N27 1,021.75 · Q27 1,000.25 · U27 981.00 · V27 963.75 · X27 944.00 · Z27 923.75 · F28 906.25 · G28 889.75 · H28 872.75 · J28 852.75 · K28 836.25 · M28 820.00 · N28 806.00 · Q28 793.75 · U28 786.00 · V28 780.25 `[A, interpolated]` · X28 774.50 · Z28 767.00 · F29 762.75.
- **Dated proxy (FRED `DCOILBRENTEU`, EIA spot):** 26 Oct 128.12 · 27 Oct 123.10 · 28 Oct 119.20 · 29 Oct 115.28 · 30 Oct 120.15 · 2 Nov 107.39 · 3 Nov 107.03.
- **Derived (front mapping):** Brent 2027 Q1–Q4 86.22 / 82.37 / 79.28 / 76.97, year 81.21; 2028 73.86; 2029 71.19. Crack 2027 Q1–Q4 76.29 / 68.90 / 65.24 / 60.67, year 67.77; 2028 45.16; 2029 37.74. Gasoil crack 2027 Q1–Q4 65.52 / 58.05 / 52.49 / 47.14, year 55.80; 2028 (Jan–Nov) 35.56. Brent–WTI 2027 (mid-quarter) 3.89; Nov-28 3.77; Nov-29 4.15.
