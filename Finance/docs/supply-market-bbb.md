# Supply Market BBB — 12 November 2026

## Metadata

- **Analysis date:** Thu 12 Nov 2026, Europe/Oslo. Information cut-off 12 Nov 2026 12:00 (DOF's Q3 report was published this morning). **Status: Final** (full update, Update mode, Steps 0–11). Caveats are in the open checkpoints:
  - there is no North Sea spot data after October (the November *Seabreeze* is due early December);
  - the Equinor AHTS term award is not announced;
  - contract cover outside Seagems, DOFCON and DOF's AHTS table is `[A]`.
- **Skill revisions:** `supply-market-bbb` **2026-11-12.1** (Paratus no longer tracked; no row, path or method change); `iaf-valuation` **2026-11-10.1**.
- **Why this run:**
  - Stale after 9 Nov.
  - Two recalibration triggers fired on 4 Nov: the Petrobras PSV 4500 / PSV 3000 tenders were published, and the NS AHTS Q4 spot quarter is set to miss Base by > 15%.
  - A third has fired since: **the Petrobras PLSV tender for 2028 starts has final results** (9 Nov).
  - Passed events: Tidewater Q3 (9 Nov, call 10 Nov); DOF Q3 (12 Nov); Equinor AHTS term tender bids (3 Nov).
  - New inputs: Oil Market BBB 11 Nov and Rig Market BBB 12 Nov (re-baselined before this run).
- **Previous baseline:** 17 Oct 2026 (26 days), with small updates on 28 Oct and 4 Nov. Their history is in the change log. **Window:** stub Q4-26 + 2027–2029; no roll (that is in January).
- **Stale after 12 Dec 2026** (30 days; the same date as the rig baseline). Each of these planned checks can force a small update earlier:
  - Petrobras PSV 4500 / PSV 3000 proposal opening, **17 Nov** (the first Brazil PSV rate print since Apr-25);
  - the Equinor AHTS term award (bids were due 3 Nov; nothing announced by 12 Nov);
  - Petrobras PN 2027–31 (late Nov by the 2025 pattern; date not announced);
  - the November *Seabreeze* (~4 Dec): month 2 of the AHTS test (rule under Conclusion) and the Q4 spot test;
  - signature of the 2028 PLSV contracts.
- **Inputs (read only; no own oil or rig view):**
  - **Oil Market BBB, 11 Nov 2026** (Final, stale after 30 Nov).
    - Brent Bear / Base / Bull: 2027 65 / **84** / 118 (Base was 88); 2028 60 / 77 / 102; 2029 60 / 72 / 90; mid-cycle 60 / 70 / 82, unchanged.
    - Long end (10 Nov settlements): Dec-27 77.6, Dec-28 72.8, Dec-29 70.6, Dec-30 69.1.
    - Its downstream row for supply: "No (no action now)". **Checked here and agreed** (Drivers). FID and tender economics run on the long end and mid-cycle. The long end sits at Petrobras' own planning price ($70 for 2027–30 in PN 2026–30 `[E]`) and far above offshore breakevens. Only spot-exposed UK activity is marginally weaker.
  - **Rig Market BBB, 12 Nov 2026** (Final, re-baseline, stale after 12 Dec).
    - Only drillship Bull 2027 (450 → 475), the drillship stub (420 → 455) and two secondary ranges moved. Every Base path, MCU and mid-cycle is kept.
    - Its note for this baseline:
      - Beacon Pacific (a stranded HE semi, moored type `[A]`) starts six wells for Serica in the UK from Q3 2027.
      - **Hercules leaves Norway for Canada in Q1 2027** (earlier rig notes tagged it NCS). NCS HE semis are therefore net +1 in 2027 vs 2026: Endurance from Q2 and Barents from Jun in, Hercules out.
      - Brazil is flat at 47 operating / 35 drilling. Outstanding Petrobras rig-days: 2027 210, 2028 1,185, 2029 780.
      - DS-18 leaves Suriname after May 2027.
    - All of it is assessed under Drivers and is below the minimum change.
- **Series per row:** unchanged. The PLSV utilisation series stays Seagems' vessel-by-vessel cover now that Paratus is not tracked: it is still the only public vessel-level PLSV series (checkpoint 3).

| Row | Rate series | Utilization / cover series |
|---|---|---|
| NS large PSV — spot | Seabrokers *Seabreeze* monthly average, "PSVs > 900 m²", GBP/day | Seabrokers North Sea spot average utilisation, large PSV |
| NS large PSV — term | Leading-edge NCS/UK term fixtures, GBP/day (NOK/USD converted at fixture-date FX); cross-check: Golden Energy (GEOS) fleet dayrate | Tidewater Europe/Med PSV > 900 m² active utilisation (proxy `[E]`) |
| NS AHTS — spot | Seabrokers monthly average, "AHTS > 22,000 bhp", GBP/day | Seabrokers spot utilisation, large AHTS |
| NS subsea / CSV-IMR | Vessel-only term/seasonal charters, GBP/day | Westwood global ROVSV utilisation (proxy `[E]`) + owner fleet status |
| Brazil PSV | Petrobras PSV 4500-class tender/award leading edge, USD/day | Spinergie South America PSV/AHTS utilisation (proxy `[E]`) |
| Brazil AHTS | Petrobras 15–18k bhp AHTS, vessel basis, USD/day | As Brazil PSV |
| Brazil RSV | Petrobras RSV, vessel + 2 WROV package, USD/day | Named-fleet cover `[A]` |
| Brazil PLSV | Petrobras PLSV, 550 t class, vessel + crew (services stated), USD/day at 100% vessel basis | Seagems vessel-by-vessel cover + technical utilisation |

- **Annual spot convention (unchanged):** the annual value is the **arithmetic mean of the 12 Seabrokers monthly averages**. Seabrokers' own annual figure is fixture-weighted and runs ~11% lower; IAF must use the convention stated here.
- **FX** (AllRatesToday, **12 Nov 2026 07:48 UTC**): **GBP/USD 1.32675 · GBP/NOK 12.6808 · GBP/BRL 7.41381** (USD/BRL 5.588; USD/NOK 9.558).
  - BRL is ~4% weaker than on 28 Oct (5.35) and ~10% weaker than on 17 Oct (5.064). That lowers the USD cost of Brazilian crew; rows are quoted in USD, so no rate moves.
  - No row is re-converted. Figures converted earlier keep their stated FX (17 Oct GBP/USD 1.33265; 10 Oct 1.3235; fixture dates as logged).
- **Oldest load-bearing inputs:** *Seabreeze* October 2026 (observed Oct, published early Nov; a monthly series, so the "> 1 week" staleness flag applies until the November report); the Fearnleys CSV orderbook (Dec 2025, stale); the Westwood global fleet count (Q4-25).
- **Not read `[?]`:** North Sea spot for November (no broker month yet, and no public weekly series since SSY's PDFs went private); the Tidewater call transcript (10 Nov; the release and its fleet tables were read); Solstad Maritime's Q3 segment utilisation (release summary only); Newsweb via Edge (not used; owner releases came from Nordic Financial's Newsweb source).
- **Tags:** `[F]` fact · `[E]` external forecast or secondary · `[A]` own assumption · `[?]` unknown. Fixture grades: A stated rate · B value ÷ days · C secondary · D unknown.

## Conclusion

**Supply Market BBB changed in two rows; every other path is kept.**

1. **NS large PSV spot, Base 2027: £16.5k → £18.5k (+12%); utilisation 72 → 75%.** Several independent points agree:
   - *Seabreeze* Jul–Oct: £15.3k / 21.4k / 22.3k / 19.5k at 62–82% utilisation `[F]`. The de-seasonalised H2-26 run-rate is ~£18–21k `[A]` (Jul–Oct ~£20.9k; May–Oct ~£17.8k on the 2023–25 factors), against a 2026 full-year mean of ~£17k.
   - Tidewater Europe/Med PSV > 900 m² (42 vessels, mostly North Sea): $24.9k at 92.6% in Q3, up from $23.8k at 88.5% in Q2 `[F]`. Tidewater's worldwide leading-edge term rate is $27.4k, +12.5% q/q `[F]`.
   - Term absorption takes PSVs out of the 2027 spot pool: Ross Offshore/Harbour's three PSVs from Jan 2027, seven Equinor extensions, and the NEO NEXT+ and EnQuest UK terms.
   - Rig input: NW Europe moored semis are up ~1 rig-year in 2027 vs 2026 (Endurance, Barents and Beacon Pacific in; Hercules out).
   - 2028–29 stay at £16.5k. The evidence concerns 2027. The fade comes from supply (Capital Offshore's 9 PSV deliveries in 2027, migration) and rig MCU easing (NCS HE 93% by 2029). Nothing moves 2028–29 by 10%.
   - Against the trigger: +12% on the annual average. That meets the 10% minimum change and stays below the 15% quarter trigger.
2. **Brazil PLSV, recalibrated on the 2028 tender round** (trigger fired: a large Petrobras tender awarded).
   - **Base 2028 295 and 2029 300 are kept; the round confirms them.**
   - Bear 2028 255 → **270** and Bear 2029 250 → **265**; Bear utilisation 82 → **86** and 80 → **84**.
   - Bull mid-cycle 285 → **300**; stub 285 → **300** (six-month leading edge, mechanical).
   - Detail under "PLSV read" below.

**Kept after testing (explicitly):**
- **NS AHTS spot, Base 2027 £75k.**
  - October (£43.8k at 42%) is still the only month since the supply arrived; November is not published.
  - Other evidence points the other way or takes AHTS out of the spot pool:
    - DOF reports "very strong" AHTS contract coverage for 2027–28, two term awards from Q1-27, and Skandi Mariner extended to Q3 2028.
    - Solstad Maritime's record Q3 was driven by its North Sea AHTS spot/project fleet.
    - The rig input has three moored semi arrivals and one departure in NW Europe in 2027.
  - The evidence threshold for a cut is not met.
  - **Pre-set rule for the November *Seabreeze* (~4 Dec):** a large-AHTS average below £50k (month 2 of the Bear signpost) cuts Base 2027 to ~£60–65k at once, by small update. At £75k or above, the Q4 miss is October only and Base stands.
- **NS PSV term, £19.5k:** no priced term print since 17 Oct. Two benchmarks sit at the row:
  - Tidewater's realised Europe/Med rate, ≈ £18.8k;
  - two GEOS PSV sales at $27.25m and $28m, which capitalise ~£19.3k per paid day.
- **Also kept:**
  - the NS CSV, Brazil PSV (bids open 17 Nov), Brazil AHTS, Brazil RSV and secondary rows;
  - every mid-cycle value except PLSV Bull;
  - economic life (25 years), the Year-1 AHTS quarters and the 25/50/25 convention weights.

**PLSV read (the 2028 round):**
- **Final results** (Fearnley Securities via Infront TDN, 9 Nov; user input, `[E]`; Petrobras' own publication not seen). Four years from 1 Jan 2028; negotiated down 10–15% from the first published levels; signatures remain.
  - DOFCON: **Skandi Buzios $305k**, **Skandi Recife and Skandi Olinda $295k**.
  - Seagems: **Sapura Jade $309k**.
- **Partly corroborated** by DOF's Q3 report (12 Nov) `[F]`:
  - the three DOFCON vessels "qualified for new 4-year contracts", planned start Jan 2028, subject to final award;
  - they add > $500m to DOF's backlog (its 50% plus Norskan's marine management). At 100% the quoted rates give ~$1.31bn for the three, ~$650m at 50%: consistent with "> $500m".
- **Comparable to the row basis (550 t, vessel + crew, 100%)?** Partly.
  - **Jade ($309k) is the direct comparable:** a 550 t Seagems vessel, priced per vessel (100%, no JV share), in the same Petrobras scope as the 2024 round (charter plus services, vessel and crew). It is +4.7% vs Base 2028 (295), below the 5% minimum change and the 10% trigger.
  - **The DOFCON prints are other classes.** Buzios is 650 t (sister of Açu) at $305k. Recife (340 t system) and Olinda (300 t contracted) are at $295k. Petrobras paid within $14k across 300–650 t, so the class premium is small. The round's median, $300k (n = 4), is +1.7% vs Base 2028.
  - Basis caveats: the BRL share of the rate and its FX date are `[?]`. The fifth lot (Seagems' third-party vessel, accepted in September) has no published rate.
- **Verdict: the round confirms the Brazil PLSV Base row** (2028 295, 2029 300), and the signpost "PLSV 2028 lots at $270–310k" is met.
  - It raises the floor for re-pricing (Bear). It re-anchors "today's level" (Bull mid-cycle and stub) from ~$285k to ~$300k.
  - The rest of the 2028 roll still needs a later tender: five Seagems vessels (Apr–Sep 2028) and Subsea7's 2025 contracts.

**Base in two sentences:**
- **North Sea:** large PSV spot ~£18.5k in 2027, fading to £16.5k as supply responds, and term ~£19–19.5k on NCS well and P&A work. Large AHTS normalises from 2026 (~£100k) toward £60–75k as the arrived supply is absorbed; October is the warning month.
- **South America:** Brazil PSV/AHTS hold a 2027 plateau with Petrobras tendering restarted (PSV bids 17 Nov), then recover in 2028–29 with FPSO start-ups. RSV (~$105k) and PLSV (~$285–300k) are long-contract markets, and PLSV's 2028 re-pricing has started at ~$300k.

**Row ranking (strongest → weakest):**
1. **Brazil PLSV / RSV:** the 2028 round at $295–309k for 4 years; no PLSV newbuilds.
2. **NS PSV term and spot:** tight H2-26 and term absorption into 2027 (up from 3rd–4th).
3. **NS AHTS:** scarce high-end tonnage, but October showed the arrived supply (down from 2nd).
4. **Brazil PSV/AHTS:** plateau and local newbuilds; tenders restarted.
5. **NS CSV:** ~30 speculative newbuild CSVs (150–250 t AHC crane, global, mostly China) deliver H2-26 to 2028, with a record year in 2027 (Fearnley Offshore Supply).

**Main catalysts:**
- **Bear:** oil Bear (an Iran–USA deal plus an OPEC+ market-share fight; closer, per the oil baseline), with the arrived AHTS supply staying in the North Sea, CSV newbuild deliveries, and a PN 2027–31 that moves Petrobras capital toward refining.
- **Bull:** PN 2027–31 confirms ~200 OSVs and newbuild tenders. North Sea tonnage is pulled to Brazil (the PSV 4500/3000 tenders admit vessels up to 20 years old), Guyana and West Africa. The fleet attrits and nothing is ordered.

**Recalibration triggers this run:**
- **Fired:**
  - The PLSV tender was awarded (assessed above).
  - Petrobras PSV tenders: bids open 17 Nov, rates `[?]`.
  - The NS AHTS Q4 spot miss: kept, with the rule above.
  - Staleness.
- **Not fired:**
  - NS PSV Q4: it needs a Nov–Dec average above £15.25k, and there is no data yet.
  - Net spot-pool moves: −2 in October.
  - Newbuild orders: none ≥ 3 in a core class.
  - Ownership changes at covered owners: DOF's Implementer sale is known; Solstad's Normand Tonjer sale is ownership only.
  - Strikes or force majeure: none.
  - Oil and rig baselines: neither flags a supply change; checked here.

## Interface — rates, k/day (point values; ranges below). North Sea GBP, South America USD

| Row Bear / Base / Bull | Currency | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|---|
| NS large PSV — spot | GBP | **16.4 / 16.4 / 16.4** | 11.0 / **18.5** / 21.0 | 10.0 / 16.5 / 23.0 | 10.0 / 16.5 / 22.0 | 11.0 / 14.0 / 17.0 |
| NS large PSV — term | GBP | 18.3 / 18.3 / 18.3 | 16.5 / 19.5 / 21.0 | 15.0 / 19.0 / 22.0 | 14.5 / 19.5 / 23.0 | 14.5 / 17.0 / 19.5 |
| NS AHTS — spot (> 22k bhp) | GBP | 66 / 66 / 66 | 45 / 75 / 120 | 38 / 65 / 110 | 35 / 60 / 100 | 30 / 38 / 50 |
| NS subsea / CSV-IMR (vessel only) | GBP | 55 / 55 / 55 | 45 / 55 / 62 | 40 / 52 / 65 | 38 / 50 / 65 | 38 / 45 / 52 |
| Brazil PSV (PSV 4500 class) | USD | 40 / 40 / 40 | 33 / 38 / 42 | 31 / 38 / 45 | 31 / 40 / 47 | 31 / 36 / 41 |
| Brazil AHTS (15–18k bhp, vessel basis) | USD | 72 / 72 / 72 | 58 / 70 / 78 | 55 / 70 / 82 | 55 / 72 / 85 | 55 / 62 / 70 |
| Brazil RSV (vessel + ROV) | USD | 105 / 105 / 105 | 95 / 105 / 112 | 92 / 107 / 118 | 92 / 110 / 122 | 90 / 100 / 110 |
| **Brazil PLSV (550 t, 100% basis)** | USD | **300 / 300 / 300** | 275 / 285 / 295 | **270** / 295 / 335 | **265** / 300 / 345 | 215 / 250 / **300** |
| NS medium PSV — spot (secondary, Base) | GBP | 13.0 | 13.0 | 13.0 | 13.0 | 11.0 |
| Guyana/Suriname large PSV (secondary, Base) | USD | 36 | 36 | 37 | 38 | 34 |
| NS AHTS — term; Brazil OSRV (secondary) | — | not set `[?]`: no fixtures with rates | | | | |

Bold values (not row labels) = changed this run; the previous values are in the change log.

- **Stub:** identical across scenarios.
  - **NS spot rows:** October actual (*Seabreeze*) plus Nov–Dec at the Base winter level `[A]`, i.e. the mean of Base Q4-27 and Q1-27.
    - PSV: (19.52 + 2 × 14.8) / 3 = **16.4**. The winter level is 14.8 (it was 13.2), because Base 2027 moved.
    - AHTS: (43.79 + 2 × 76.9) / 3 = **66**, unchanged.
    - Cross-checks: October × the 2025 Nov/Oct and Dec/Oct ratios (n = 1) give PSV 16.4 and AHTS 49. Nov–Dec at the previous Base winter level (13.2) give PSV 15.3. Stub ranges: PSV 15.3–16.4; AHTS 49–85. The November *Seabreeze* replaces the November estimate.
  - **PLSV: 300** = the six-month Petrobras leading edge: the 2028 round's median, n = 4 ($295–309k; start Jan 2028, inside the ~18-month window). Mechanical; no Q4-26 PLSV day is open.
    - The stub sits above Base 2027 (285) for a reason: 2027 has no new-start contracts.
    - Open 2027 PLSV days are bridges, such as Jade's gap from Jul 2027 to its new contract in Jan 2028. Petrobras has priced such bridges as extensions at in-force levels (Buzios, Recife and Olinda were extended to Jan 2028; rates undisclosed).
  - **NS PSV term: 18.3**, unchanged. No priced term print since 17 Oct; the six-month median is still £18.4k.
- **Low confidence:** NS CSV; Brazil AHTS; PLSV Bull 2028–29 (the rest of the 2028 roll is not tendered).

## Interface — utilization / cover, % annual average

| Row Bear / Base / Bull | Series | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|---|
| NS large PSV — spot | Seabrokers spot utilisation | **75 / 75 / 75** | 62 / **75** / 78 | 58 / 74 / 80 | 58 / 74 / 80 | 62 / 70 / 76 |
| NS large PSV — term | Tidewater Europe/Med PSV > 900 active `[E]` | **93 / 93 / 93** | 84 / 88 / 91 | 82 / 89 / 92 | 80 / 89 / 92 | 83 / 87 / 90 |
| NS AHTS — spot | Seabrokers spot utilisation | 55 / 55 / 55 | 52 / 62 / 70 | 50 / 64 / 72 | 50 / 65 / 72 | 52 / 60 / 66 |
| NS subsea / CSV-IMR | Westwood ROVSV `[E]` + owner status `[A]` | 90 / 90 / 90 | 78 / 85 / 90 | 74 / 83 / 90 | 72 / 82 / 89 | 75 / 80 / 85 |
| Brazil PSV | Spinergie S. America `[E]` | 84 / 84 / 84 | 80 / 84 / 87 | 77 / 83 / 89 | 77 / 85 / 90 | 78 / 83 / 87 |
| Brazil AHTS | Spinergie S. America `[E]` | 84 / 84 / 84 | 80 / 84 / 87 | 78 / 84 / 88 | 78 / 85 / 89 | 78 / 83 / 87 |
| Brazil RSV | Named-fleet cover/utilization `[A]` | 92 / 92 / 92 | 88 / 92 / 94 | 85 / 91 / 94 | 83 / 90 / 94 | 85 / 89 / 92 |
| Brazil PLSV | Seagems cover (vessel by vessel) + technical utilization | 95 / 95 / 95 | 92 / 95 / 96 | **86** / 92 / 96 | **84** / 91 / 95 | 82 / 88 / 92 |

- **Stubs:**
  - NS spot: October actual plus Nov–Dec at the Base winter level. PSV (82 + 2 × 72) / 3 = **75**; AHTS (42 + 2 × 61) / 3 = 55.
  - NS PSV term: the latest observed quarter, Tidewater Q3 92.6% `[F]` (it was Q2's 88.5%). Q3 is the seasonal high; Q4-25 was 87.7%.
- **PLSV:**
  - 2027: Seagems firm cover is ~92%, because Jade's contract ends in Jul 2027. Base 95% assumes Jade is bridged at least half the gap, as Petrobras did for DOFCON; Bear has Jade idle.
  - 2028–29: **Jade is now booked from Jan 2028 for 4 years** (subject to signature), so the Bear "Jade idle" element falls away. Bear keeps signature and mobilisation risk and the five Seagems re-contracts (Apr–Sep 2028) with gaps.

## Year 1 by quarter — North Sea spot (GBP k/day; utilization %)

| Row | Scenario | Q1-27 | Q2-27 | Q3-27 | Q4-27 | Year avg | Seasonal factors (years used) |
|---|---|---|---|---|---|---|---|
| NS large PSV — rate | Bear | 7.3 | 16.1 | 10.3 | 10.3 | 11.0 | 0.66 / 1.46 / 0.94 / 0.94 (2023–2025) |
| NS large PSV — rate | **Base** | **12.2** | **27.0** | **17.4** | **17.4** | **18.5** | same |
| NS large PSV — rate | Bull | 13.9 | 30.7 | 19.7 | 19.7 | 21.0 | same |
| NS large PSV — utilization | Base | **69** | **81** | **75** | **75** | **75** | `[A]`, from the 2026 monthly pattern |
| NS AHTS — rate | Bear | 43.2 | 50.9 | 36.9 | 49.1 | 45.0 | 0.96 / 1.13 / 0.82 / 1.09 (2023–2025) |
| NS AHTS — rate | Base | 72.0 | 84.8 | 61.5 | 81.8 | 75.0 | same |
| NS AHTS — rate | Bull | 115.2 | 135.6 | 98.4 | 130.8 | 120.0 | same |
| NS AHTS — utilization | Base | 60 | 66 | 60 | 62 | 62 | `[A]` |

- **Factors:** the quarterly mean of the Seabrokers monthly averages ÷ the annual mean, averaged over 2023–2025 (unchanged).
- **PSV seasonality** is strong and stable: Q2 peaked in all three years. In 2026 the shape was flatter (Q2/annual ~1.28, H2 firmer). If 2026's shape repeats, Base Q2-27 is ~£24k and H2 is higher, with the same annual mean.
- **AHTS seasonality** is weak and noisy, so the AHTS quarters carry low confidence.

## Interface — asset values and anchors

| Row | Newbuild $m, lead time | Secondhand $m (age, date) | Reactivation $m, lead time | Value mid-cycle Bear / Base / Bull $m | Cash floor k/d | Reactivation parity k/d | Newbuild parity k/d |
|---|---|---|---|---|---|---|---|
| NS large PSV | 40–41 (China, SEACOR/Capital orders) `[F/E]`; ~2–3 yrs | 19.0–23.6 (Bourbon Calm/Clear/Front 2012, Rainbow 2014; 2026 auctions) `[F]`. **Added:** GEOS Energy Partner 27.25 and Energy Passion 28.0 (large PSVs, Passion a PX121; build years `[?]`, ~2013–14 `[A]`), MPSV Energy Empress 30.0; gross prices, closed Dec-25 to Mar-26 `[F]` | `[?]` (laid-up fleet "scrapped in place" `[E]`) | 11 / 19 / 27 (12-yr-old) | £9.2 ($12.2) `[A]` | `[?]` | £20.2 convention `[A]`; £23–25 (Tidewater "low 30s" $) `[E]` |
| NS large AHTS | `[?]` (no > 300 t BP orders; ~90 assumed `[A]`) | 27.1 avg (15 large AHTS to 2020 Bulkers, $406m, Sep-26) `[F]`. Medium-large (200 t BP / 16k bhp, < 22k bhp class): Skandi Atlantic ~23 (Jan-26), Skandi Emerald 23 (2011, Jun-26), Skandi Peregrino 21.6 (2010, 16,315 bhp, 2 Oct 26) `[F]` | `[?]` | 14 / 37 / 70 (15-yr-old) | £11.4 ($15.0) `[A]` | `[?]` | £46.5 spot-avg equivalent at 62% util `[A]` |
| NS CSV (vessel only) | `[?]` (DOF SALT 310 pair, price not disclosed); CSOV €65m `[F]` (wind) | 46.5–60.4 (Bourbon Evolution 805/806/808, 2014, 150 t crane, Aug–Sep 26) `[F]`. High-end, outside the row: Normand Maximus (900 t / 550 t VLS) $125m intra-group strike for Oct-27, fixed Oct-22 `[F]`, not a market price; Skandi Implementer (400 t, 2018) sold, price `[?]` | — | 54 / 81 / 111 (12-yr-old; low confidence) | £13.6 ($18.0) `[A]` | — | `[?]` |
| Brazil PSV (Brazilian flag) | 85–90 (Brazil/US-built 5,500 dwt) `[E]`; 4–5 yrs `[E]` | 34.6 avg EV (Tidewater–WSUT, 22 PSVs incl. backlog, Feb-26) `[F]` | — | 31 / 46 / 62 (12-yr-old) | $13.0 `[A]` (Tidewater Americas opex $12.0 `[F]`); lower in USD with the weaker BRL (5.59) | — | $41.7 Brazil-built `[A]`; $27.7 foreign-built `[A]`; implied Petrobras 12-yr newbuild charter $52–60 `[B]` |
| **Brazil PLSV (550 t, 100%)** | 267 (Seabras/IHC, 2012) and ~317 (Subsea7, 2012) `[E]`; today ~346–425 `[A]` (cost inflation); ~3 yrs | none found `[?]`; Seagems book PP&E $187m a vessel `[F]` | — | 212 / 343 / **512** (11-yr-old, 14 yrs left) `[A]`, model only | **$90 incl. G&A; opex $77** (Seagems Q2-26, 100%) `[B]`; BRL-linked crew cost lower in USD | — | **$205–226** at $346–425m `[A]` |
| Brazil RSV | `[?]` (DOF 4 at Navship; DOF analysis assumes ~$120m incl. 2 WROV `[A]`) | `[?]` | — | `[?]` | `[?]` | — | `[?]` |
| Fleet cross-check | — | DOF broker average **$4,081m for 57 owned vessels** (30 Jun 2026, as printed in the Q3 report; $4,085m in the Q2 material; ≈ $71.6m a vessel, mixed CSV/AHTS/PLSV at 50%) `[F]` | — | — | — | — | — |

Changed this run: the PLSV Bull mid-cycle value 470 → **512** (it follows the Bull mid-cycle rate, 285 → 300), and the GEOS PSV sales are added. Other bold text marks key figures, not changes.

**Method `[A]`** (conventions from the skill):
- **Value** = (rate × utilization × 365 − opex × 365 [− capex for PLSV, $5.8m/yr]) × PV annuity at 8% over the remaining life. A 25-year life gives 12 years left at age 13 (PSV, CSV), 10 years for the AHTS and 14 years for an 11-year-old PLSV.
  - PLSV Bull: 300 × 92% × 365 = $100.7m − $32.9m opex − $5.8m capex = $62.1m × 8.244 = **$512m**.
- **Newbuild parity** = opex + 25-year annuity at 8% on the price, at 85% utilization (AHTS: per spot-paid day at 62%; PLSV: 95% and incl. $5.8m capex).
- **Opex:** PSV $12.2k/day (Tidewater Europe/Med vessel opex $10.8k in Q3 `[F]` ($56.2m ÷ 5,220 available days) + drydock ~$1.5k `[A]`); AHTS $15k and CSV $18k `[A]`; Brazil PSV $13k `[A]`; PLSV $90k incl. G&A `[B]`.
- **Asset-implied rates:**
  - A 2013 PSV at $21m (Bourbon auctions) capitalises **~£17.7k** per paid day.
  - **Added:** the GEOS PSVs at $27.25–28m (avg $27.6m, ~13 years left) capitalise **~£19.3k** per paid day at 85% ($25.6k). That equals the NS term Base (£19.5k): buyers priced today's term level, not mid-cycle.
  - The 2020 Bulkers average ($27.1m) capitalises **~£32k** spot-average-equivalent for large AHTS, the alternative mid-cycle anchor.
    - The three DDW sales (200 t class, 15–16 years, $21.6–23m) were **flat through 2026** while spot set records. Buyers do not price 2026 as permanent.
  - A Bourbon 2014 CSV at $55m capitalises **~£33k**, vessel only.
- **PLSV:** values above the 2012 newbuild price reflect today's tight market at an 8% discount rate. No PLSV transaction exists to test them, so they are model-only and sensitive to life and rate.

**Economic life per row** `[A]` (8% annuity method):

| Row | Life (years) | Evidence | Test against transactions | Alternative / what would move it |
|---|---|---|---|---|
| NS large PSV | **25** | MSI: vessels older than 15 years struggle for work in Northern Europe and migrate to the Middle East/Asia `[E]` (S38). Operator caps: ADNOC 20, ONGC 21, Aramco 23 `[E]`; Petronas 20 (raised from 15 in 2022). Petrobras' PSV 4500/3000 tenders cap age at 20 years `[F]`. The second life abroad is inside the 25 years | A 2013 PSV at $21m capitalises ~£17.7k over 12 years left, about the term mid-cycle (£17k × 87%), so 25 years is consistent. The GEOS sales ($27–28m) sit above the mid-cycle model value ($19m), but they capitalise today's term level (~£19.3k), not a longer life | None; shorter for UK spot-only tonnage |
| NS AHTS (large) | **25** | As PSV. Scrap value is negligible (MSI: ~$0.5m per OSV), so exit is by uncompetitiveness, not scrapping | DDW 200 t units (15–16 yrs, $21.6–23m) already imply ~£31k at 25 years, against a £38k mid-cycle. **At 30 years the same prices imply ~£28k** `[A]`. Buyers do not pay for a longer life | None |
| NS CSV (150–250 t) | **25** | No age cap found. High-end CSVs get mid-life upgrades | Bourbon Evolution 805/806/808 (2014, 150 t) at $46.5–60.4m vs a model value of ~$85m at 25 years (13 left, mid-cycle £45k × 80%) and ~$101m at 30 years `[A]`. The market is below even the 25-year value | 30 years only with transactions at or above the 25-year model value |
| Brazil PSV / AHTS | **25** | Petrobras prefers newbuilds for fleet renewal; the new PSV tenders cap age at 20 years `[F]` | Tidewater–WSUT ($34.6m average EV per PSV incl. backlog) cannot isolate life | None |
| Brazil RSV | **25** | No evidence either way | No transaction | `[?]` |
| Brazil PLSV | **25** | Seagems' Extended Dry-Docking (EDD) programme is approved up to 20 years of age for its five 550 t Panama-flagged PLSVs (primary text now read, S60): one fewer SPS docking in each vessel's life. It lowers docking capex and supports working to the end of 25 years, not a longer life | Model value at 25 years is already ~30% above the 2012 newbuild price; 30 years would add ~$60m a vessel | 30 years only if a class extension beyond 25 years is approved **and** Petrobras accepts the vessels on post-2032 contracts |

- **Reading for IAF:**
  - **25 years is not a conservative convention for this market.** Where transactions exist (PSV, AHTS, CSV), buyers pay at or below the 25-year model value at mid-cycle rates. The GEOS PSV sales are the exception, and they price today's term rate.
  - A 30-year life would push model values further above what the market pays, unless mid-cycle rates were cut at the same time.
  - DOF's 27.5–30-year cases therefore stay sensitivities, not Base. No open route to a longer life is left: the Seagems EDD approval lowers docking capex, not life.

## Scenario definitions

| Scenario | Weight (convention) | Oil BBB scenario | Rig BBB scenario | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|---|
| **Bear** | 25% | Bear (Brent 65 / 60 / 60; mid-cycle 60) | Bear (FID deferrals; NCS HE MCU 92 / 88 / 83%; drillships 380 / 375 / 360) | **Demand:** oil Bear cuts UK drilling and late-window FIDs. PN 2027–31 moves capital toward refining and diesel self-sufficiency, so Petrobras OSV tendering thins out after the current PSV round (AHTS, RSV, OSRV), and the rest of the 2028 PLSV roll re-prices ~10% below the 2028 round. **Supply:** the AHTS tonnage that arrived in Jun–Sep 2026 stays in the North Sea; 12 Brazilian-built PSVs (local-content priority) displace foreign vessels back to the North Sea; ~30 CSV newbuilds deliver in 2027–28 | NS PSV spot back to the 2024–25 band (£10–11k); AHTS ~£35–45k (October 2026 is the template); CSV rates fall toward asset-implied levels; Brazil PSV/AHTS slip 10–20% on re-tenders; the rest of the PLSV roll at ~$270k | Q1 2027 (AHTS: under way) | Large AHTS monthly avg < £50k for 3 months (Oct = month 1) · NS large PSV spot < £12k in Q2/Q3 · ≥ 3 large PSVs return from Brazil in a quarter · PN 2027–31 postponed or E&P capex cut > 10% · no Petrobras OSV tender beyond the PSV round by Q2-27 · NCS HE rig MCU < 92% · rest of the PLSV roll < $270k |
| **Base** | 50% | Base (84 / 77 / 72; mid-cycle 70) | Base (NCS HE 97 / 96 / 93%; Brazil flat at 35 drilling; drillships 420 / 455 / 470) | NCS well campaigns, Equinor/Aker BP/Vår term demand and Harbour's Norge campaign absorb PSVs into 2027; the UK is spot-heavy with rising P&A and its first multi-year terms. AHTS supply has answered the 2026 scarcity: rates normalise but stay above 2022–25. Petrobras has restarted OSV tendering (PSV 4500/3000, bids 17 Nov), with a 2027 plateau and 2028–29 FPSO recovery. The 2028 PLSV round prices at ~$300k | PSV spot ~£18.5k in 2027, then £16.5k; term ~£19–19.5k; AHTS £75k → £60k; Brazil PSV ~$38–40k; RSV/PLSV contracted | Ongoing | Q2-27 PSV spot avg £20–28k · H1-27 large AHTS avg £60–90k · NCS term PSV NOK 230–265k for 2027 starts · Petrobras PSV bids (17 Nov) at $36–42k · PN 2027–31 keeps E&P capex within ±10% |
| **Bull** | 25% | Base or Bull (2027 84–118) | Bull (drillships 475 in 2027, MCU 97% by 2028; FIDs) | **Demand:** PN 2027–31 confirms ~200 OSVs and 52 newbuild tenders `[E]` and pushes Equatorial Margin exploration; Guyana/Suriname and West Africa grow; NCS well campaigns, rig moves and floating-wind mooring. **Supply:** no orders; attrition (fleet > 20 yrs from 25% to 31% of tonnage `[E]`); net departures from the North Sea, as the PSV 4500/3000 4-year terms pull PSVs to Brazil; no PLSV newbuilds | NS PSV spot toward newbuild parity (£21–23k); term £21–23k; AHTS stays > £100k; Brazil PSV $42–47k; the rest of the PLSV roll at ≥ $330k (the level of the 2028 round's first published bids) | Q1 2027 | PN 2027–31 confirms the OSV target · net departures ≥ 3 large PSVs per quarter · large AHTS > £100k through H1-27 · NCS term PSV > NOK 275k · rest of the PLSV roll > $320k · Petrobras PSV bids > $42k · first large AHTS or PSV order at > $45m by a North Sea owner |

## Paths per row — utilization % / rate k/day, point (range)

| Scenario | Row | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|
| Bear | NS large PSV — spot (£) | 62 (58–66) / 11.0 (9.0–13.0) | 58 (54–62) / 10.0 (8.0–12.0) | 58 (54–62) / 10.0 (8.0–12.0) | 59 / 10.3 | 62 / 11.0 |
| **Base** | **NS large PSV — spot (£)** | **75 (71–79) / 18.5 (15.5–21.5)** | **74 (70–78) / 16.5 (13.0–20.0)** | **74 (70–78) / 16.5 (13.0–20.0)** | **74 / 17.2** | **70 / 14.0** |
| Bull | NS large PSV — spot (£) | 78 (75–82) / 21.0 (18.0–24.0) | 80 (77–84) / 23.0 (19.5–26.0) | 80 (77–84) / 22.0 (19.0–25.0) | 79 / 22.0 | 76 / 17.0 |
| Bear | NS large PSV — term (£) | 84 (82–86) / 16.5 (15.5–17.5) | 82 (79–85) / 15.0 (14.0–16.5) | 80 (77–83) / 14.5 (13.0–16.0) | 82 / 15.3 | 83 / 14.5 |
| **Base** | **NS large PSV — term (£)** | **88 (86–90) / 19.5 (18.0–21.0)** | **89 (86–91) / 19.0 (17.5–20.5)** | **89 (86–92) / 19.5 (17.5–21.5)** | **89 / 19.3** | **87 / 17.0** |
| Bull | NS large PSV — term (£) | 91 (89–93) / 21.0 (20.0–22.0) | 92 (90–94) / 22.0 (20.5–23.5) | 92 (90–94) / 23.0 (21.0–25.0) | 92 / 22.0 | 90 / 19.5 |
| Bear | NS AHTS — spot (£) | 52 (47–57) / 45 (35–55) | 50 (45–55) / 38 (30–46) | 50 (45–55) / 35 (28–42) | 51 / 39 | 52 / 30 |
| **Base** | **NS AHTS — spot (£)** | **62 (57–67) / 75 (55–95)** | **64 (59–69) / 65 (48–82)** | **65 (60–70) / 60 (45–75)** | **64 / 67** | **60 / 38** |
| Bull | NS AHTS — spot (£) | 70 (65–75) / 120 (100–145) | 72 (67–77) / 110 (90–135) | 72 (67–77) / 100 (80–125) | 71 / 110 | 66 / 50 |
| Bear | NS CSV — vessel only (£) | 78 (74–82) / 45 (40–50) | 74 (70–78) / 40 (35–45) | 72 (68–76) / 38 (33–43) | 75 / 41 | 75 / 38 |
| **Base** | **NS CSV — vessel only (£)** | **85 (82–88) / 55 (48–62)** | **83 (80–86) / 52 (45–59)** | **82 (78–86) / 50 (43–57)** | **83 / 52** | **80 / 45** |
| Bull | NS CSV — vessel only (£) | 90 (88–92) / 62 (57–67) | 90 (87–93) / 65 (59–71) | 89 (86–92) / 65 (59–71) | 90 / 64 | 85 / 52 |
| Bear | Brazil PSV ($) | 80 (78–82) / 33 (31–35) | 77 (74–80) / 31 (28–34) | 77 (74–80) / 31 (28–34) | 78 / 31.7 | 78 / 31 |
| **Base** | **Brazil PSV ($)** | **84 (82–86) / 38 (35–41)** | **83 (80–86) / 38 (35–42)** | **85 (82–88) / 40 (36–44)** | **84 / 38.7** | **83 / 36** |
| Bull | Brazil PSV ($) | 87 (85–89) / 42 (40–44) | 89 (87–91) / 45 (42–48) | 90 (88–92) / 47 (43–51) | 89 / 44.7 | 87 / 41 |
| Bear | Brazil AHTS ($) | 80 (78–82) / 58 (52–64) | 78 (75–81) / 55 (48–62) | 78 (75–81) / 55 (48–62) | 79 / 56 | 78 / 55 |
| **Base** | **Brazil AHTS ($)** | **84 (82–86) / 70 (62–78)** | **84 (81–87) / 70 (62–80)** | **85 (82–88) / 72 (63–82)** | **84 / 71** | **83 / 62** |
| Bull | Brazil AHTS ($) | 87 (85–89) / 78 (72–84) | 88 (86–90) / 82 (75–90) | 89 (87–91) / 85 (77–93) | 88 / 82 | 87 / 70 |
| Bear | Brazil RSV ($) | 88 (86–90) / 95 (90–100) | 85 (82–88) / 92 (85–98) | 83 (80–86) / 92 (85–98) | 85 / 93 | 85 / 90 |
| **Base** | **Brazil RSV ($)** | **92 (90–94) / 105 (100–110)** | **91 (89–93) / 107 (100–115)** | **90 (87–93) / 110 (102–118)** | **91 / 107** | **89 / 100** |
| Bull | Brazil RSV ($) | 94 (92–96) / 112 (107–117) | 94 (92–96) / 118 (110–125) | 94 (92–96) / 122 (113–130) | 94 / 117 | 92 / 110 |
| Bear | Brazil PLSV ($, 100%) | 92 (90–94) / 275 (265–285) | 86 (82–90) / 270 (255–285) | 84 (80–88) / 265 (245–285) | 87 / 270 | 82 / 215 |
| **Base** | **Brazil PLSV ($, 100%)** | **95 (93–97) / 285 (275–295)** | **92 (88–95) / 295 (280–325)** | **91 (87–95) / 300 (280–335)** | **93 / 293** | **88 / 250** |
| Bull | Brazil PLSV ($, 100%) | 96 (94–98) / 295 (285–305) | 96 (93–98) / 335 (305–365) | 95 (92–97) / 345 (305–385) | 96 / 325 | 92 / 300 |

Changed this run: Base NS PSV spot 2027 (point, range, 3-yr avg); Bear PLSV 2028–29 (rate, utilisation, ranges, 3-yr avg); Bull PLSV mid-cycle; the Base PLSV 2028–29 ranges narrow on the downside (lower bound 265 → 280), because the round printed at $295–309k. Previous values are in the change log.

**Secondary rows (Base, point (range), low confidence):**
- **NS medium PSV spot:** £13.0k (10–16) each year. 2026 Jan–Oct monthly mean ~£15k; October £17.4k at 78% `[F]`.
- **Guyana/Suriname large PSV:** $36k (32–40) / $37k / $38k.
  - Tidewater Americas PSV > 900 m² realised $34.2k at 81.1% active utilisation in Q3 `[F]`. From Q3 that region includes WSUT (Brazil), so it is more Brazil-weighted.
  - Demand is still adding up (the fifth Stabroek FPSO, Errea Wittu, first oil guided Q4-26). DS-18 leaves Suriname after May 2027 (rig baseline), a small offset in H2-27.
  - DOF has two AHTS on Caribbean project work, 150 days combined, $15–25m (≈ $50–83k per vessel-day, project scope) `[F]`. This is context for a Guyana/Suriname AHTS row, which is not set.

**Contract cover per row and year `[A]` unless stated** (this is why the spreads differ):
- **NS PSV spot pool:** no cover. The spread is wide from 2027.
- **NS PSV term fleet:** ~71 / 50 / 35%.
  - Five-year Equinor terms: North Barents, Sygna Tide, Polaryssel.
  - 2027 one-well terms: Energy Swan, Viking Queen and Aurora Galaxy (Ross Offshore for Harbour's Norge campaign, ~265–290 days from Jan 2027).
  - Equinor extensions into 2027–28: Viking Avant, Havila Charisma, Havila Foresight, Skandi Flora, Skandi Mongstad, Island Crusader, Kongsborg, Edda Fram.
  - UK: Falcon Tide and Forth Tide (EnQuest) to Sep/Oct 2027; the medium PSVs Havila Fanø and Herøy (NEO NEXT+) to Sep 2029, outside the large-PSV fleet.
- **NS AHTS:** mostly spot.
  - DOF's AHTS fleet has "very strong" cover for 2027–28: 11 AHTS on contracts beyond mid-2029 (Brazil and international); Skandi Vega (Equinor) to Q3 2029; Skandi Mariner to Q3 2028; two AHTS on > 1-year terms from Q1-27 `[F]` (S59, S60).
  - The Equinor AHTS term tender (1/3/5 years) is not yet awarded.
- **NS CSV:** ~70 / 45 / 25%.
  - Firm work: Normand Sentinel to end-2027; Navigator 450 days from Q2-26; DOF's I-class LOI for H1-28 (award due mid-Nov); DOF's Q1-27 decommissioning campaign; Skandi Nomad to Nov 2027.
  - New this run: Skandi Constructor firm to Apr 2028 (region `[?]`) and a 7-year contract for one smaller DOF CSV (below the row class). Both are below the 2 pp minimum.
- **Brazil PSV/AHTS:** ~75 / 55 / 35%. DOF starts 5 AHTS on new 4-year Petrobras contracts in 1Q27 "at better terms" `[F]`.
- **Brazil RSV:** ~85 / 70 / 55% (DOF: 3 more RSVs on 4-year contracts from 1Q27 `[F]`).
- **Brazil PLSV, vessel by vessel:**
  - **Seagems `[F]`:** contract ends Jade Jul-27 (new 4-year contract from Jan 2028 at $309k, subject to signature); Diamante and Topazio Apr-28; Esmeralda and Rubi May-28; Onix Sep-28.
    - Cover: **~92% in 2027, ~53% in 2028, ~17% in 2029** (was 93 / 36 / 0).
  - **DOFCON `[F]`:**
    - Buzios, Recife and Olinda are extended to Jan 2028, then on new 4-year contracts (subject to signature).
    - Açu is on its 2024 contract to mid-2029.
    - Vitória and Niterói are on 3-year contracts from 1Q27.
    - Cover: ~97 / 100 / 92%.
  - **Subsea7 (4) `[A]`:** three 3-year and one 4-year contract from 2025, so ~100 / 60 / 15%.
  - **Fleet level (16 named high-spec PLSVs) `[A]`:** **~95 / 73 / 44%** (was ~93 / 45 / 25% on ~20 units). Seagems' third-party vessel (lot 5) would add one unit from 2028 if new to Brazil `[?]`.
  - **The rest of the 2028 roll is the PLSV swing point:** five Seagems vessels (Apr–Sep 2028) and Subsea7's three 3-year contracts. Petrobras has not yet tendered them.

**Anchor-to-estimate rate bridges (Base 2027):**
- **NS PSV spot (changed):**
  - Anchor: *Seabreeze* Jul–Oct mean £19.6k at 76% `[F]`; de-seasonalised ~£20.9k (Q3/Q4 factor 0.94), or ~£17.8k on May–Oct (the Q2 factor 1.46 pulls May–Jun down) `[A]`.
  - 2026 full year ~£16.8–17.1k, with Nov–Dec at £13.2–15.0k: the weak Q1-26 (£10.5k) holds it down.
  - Supply: Capital Offshore's 9 PSV deliveries in 2027 (global, not assigned to the North Sea); Aurora Galaxy arrives on term (supply and demand together). Demand: NW Europe moored semis +~1 rig-year; term absorption takes ≥ 3 PSVs out of the spot pool.
  - Partial persistence of the H2-26 tightness gives **£18.5k** (range 15.5–21.5), against 2026's ~£17k.
- **NS PSV term:** unchanged at **£19.5k**.
  - 2027-start leading edge: Energy Swan ~£20.6k ($27.2k, NOK 262k; $8.7m firm over ~320 days incl. a one-month October charter, B). If the October month earned ~$35k, the 290-day NCS leg is ~£20.0k.
  - The five-year Equinor terms, at NOK 230–240k (£18.0–18.8k), carry a duration discount.
  - Cross-checks: Tidewater Europe/Med PSV > 900 realised $24.9k ≈ £18.8k in Q3 (fleet average incl. older contracts); GEOS PSV sales capitalise ~£19.3k.
  - Weighting 2027 starts over five-year terms gives **£19.5k**.
- **NS AHTS spot:** unchanged at **£75k**.
  - 2026 Jan–Oct mean £106.6k, inflated by the Rosebank hook-up and the Q1 rig-move cluster. October £43.8k at 42%.
  - 2027 demand: three moored-semi arrivals (Endurance Q2, Barents Jun, Beacon Pacific Q3, ~3 AHTS × 3–5 days each), the Hercules tow-out (Q1) and well-to-well moves.
  - Supply: the 9 Jun–Sep arrivals, partly offset by term lock-ups (DOF; Equinor tender pending).
  - Result: **£75k**, the test case of this baseline (rule under Conclusion).
- **NS CSV:** unchanged. **£55k ($73k)**, low confidence.
- **Brazil PSV:** unchanged at **$38k**. Petrobras reference $40.7k (Apr-25); Tidewater "> $42k" medium `[E]`. The 17 Nov bid opening is the first print.
- **Brazil AHTS:** unchanged at **$70k**. DOF $82.2k blended incl. ROV; the Petrobras AHTS newbuild tender was cancelled 19 Jun 2026 `[F]`, so there is no new Brazilian-built AHTS supply.
- **Brazil RSV:** unchanged at **$105k**.
- **Brazil PLSV:** Base 2027 **$285k** = in-force contracts.
  - Seagems contractual $269–289k (avg ~$285k, n = 6); realised $278–281k `[F/B]`.
  - The 2024 tender gave ~$274k (six 3-year contracts, ~$1.8bn) `[B]`. Subsea7's 2025-start awards (~$263k incl. services) are comparable. DOFCON earns ~$180–245k at 100% until Jan 2028 (smaller/older lay systems `[B]`).
  - **2028 round (new):** Jade $309k (550 t), Buzios $305k (650 t), Recife and Olinda $295k (300–340 t); median $300k, n = 4 (C, corroborated by DOF, B). Base 2028 $295k and 2029 $300k stand (+1.7% / 0% vs the median; Jade +4.7%).

**PLSV mid-cycle:**
- Anchors: the previous contract round averaged $200.8k (Q2-24). Convention newbuild parity at today's cost is $205–226k. The 2024 round was ~$274k. **Today's level is ~$300k (2028 round; was ~$285k).**
- No PLSV newbuild is on order. Four-year Petrobras terms do not finance a $350–425m vessel with a ~3-year lead time, so supply cannot respond inside the window.
- **Base $250k** sits between parity and today. The midpoint moved by ~3%, below the 5% minimum, so it is kept.
- **Bear $215k** ≈ parity and the previous round + inflation (kept).
- **Bull $300k** = today's level holds (285 → 300; +5.3%).
- **Alternative anchors for IAF:** $300k (today) and $205k (parity / previous cycle).

**Base vs owner guidance:**
- **Tidewater:** guides 2027 revenue $1.70–1.75bn (2026: $1.43–1.44bn, incl. WSUT for a full year) and 51–53% gross margin. Its worldwide leading-edge term rate is $27.4k (+12.5% q/q), and its earlier path was +$3–4k/day a year in 2027–28 `[E]`. Base sits below that globally; the NS PSV rows are now close to it.
- **DOF:** "the market environment remains supportive". Its firm 2027 backlog equals 72% of the mid-point of its 2026 revenue guidance `[E]`.
- **Solstad Maritime:** "well positioned for 2027" `[E]`.
- Base is set from cover, tenders and fixtures, not from guidance.

## Market check

| Row | Utilization latest (month, series) | Leading-edge median / range / n (6 mo) | Trend 6–12 mo | Cover 2027 / 28 / 29 | Base 2027 vs leading-edge |
|---|---|---|---|---|---|
| NS large PSV — spot | **82% (Oct)**; Sep 80, Aug 79, Jul 62, Jun 65, May 68 (Seabrokers) | Monthly avgs May–Oct: median £20.0k; Oct £19.5k (fixtures £11.9–41.3k); Sep £22.3k | 2026 Jan–Oct mean £17.5k, +56% vs 2025 same months; H2 firmer than Q2 | spot pool — | **18.5** vs Jan–Oct mean 17.5 (+6%); vs Jul–Oct 19.6 (−6%) |
| NS large PSV — term | Tidewater Eur/Med PSV > 900: **92.6% (Q3)**, 88.5% (Q2); GEOS fleet 94.3% (Sep) | 2027 starts: £20.6k (n = 1, B); all terms: median £18.4k / £18.0–20.6k / n = 3. No priced print since 17 Oct (extensions all D). Tidewater Eur/Med realised $24.9k ≈ £18.8k (Q3) | Firming; one-well 2027 terms on the NCS; first multi-year UK terms | 71 / 50 / 35 `[A]` | 19.5 vs 20.6 (−5%) |
| NS AHTS — spot | **42% (Oct)**; Sep 61, Aug 73, Jul 55, Jun 80, May 53 | Monthly avgs May–Oct: median £106.4k; Oct £43.8k (fixtures £21.9–71.6k), lowest since Sep 2025. Term context (D/B): DOF AHTS > 1-year terms from Q1-27 at ~$41–68k; Skandi Mariner ~$33–55k (Q2-27 to Q3-28) | Record H1; sharp break in Oct as arrivals land; Nov `[?]` | ~0 (DOF's AHTS mostly termed out) | 75 vs Jan–Oct 106.6 (−30%); vs Oct 43.8 (+71%) |
| NS CSV | Sea1 subsea 100% (Q2); Westwood ROVSV 75% (2025); DOF fleet 86% (Q3, all segments) | No 2026 NS vessel-only fixture with a disclosed rate (n = 0). H1-25 class levels (Fearnley Offshore Supply) `[E]`: 150 t AHC often > $60k (≈ £45k), 250 t AHC often > $80k (≈ £60k) | Softening into the newbuild wave; high-end employed (Normand Maximus with Saipem from Mar 2027) | 70 / 45 / 25 `[A]` | 55 vs ~45–60 (grade C): inside the band |
| Brazil PSV | Low-to-mid 80s `[E]` | Ref. $40.7k (Apr-25); Tidewater > $42k (medium) `[E]`; n < 3. **Bids open 17 Nov** | Plateau; tenders restarted (PSV 4500 × 5 lots, PSV 3000 × 2) | 75 / 55 / 35 `[A]` | 38 vs ~40 (−5%) |
| Brazil AHTS | Low-to-mid 80s `[E]` | $82.2k blended incl. WROV (May-25 `[B]`); Westhon $49.5k / $65.1k (`[C]`, undated) | Firm; DOF's 5 new 4-year contracts from 1Q27 "at better terms" | 75 / 55 / 35 `[A]` | 70 vs ~75 vessel-equivalent |
| Brazil RSV | `[A]` ~92% | ~$108k / $102–127k / 4 | Firm; 12-year newbuild terms | 85 / 70 / 55 `[A]` | 105 vs 108 (−3%) |
| Brazil PLSV (100%) | Seagems 93% (Q2), 98.3% (Q1) | **2028 round: $300k / $295–309k / 4** (Jade 550 t $309k; C, corroborated by DOF, B). In force: Seagems contractual avg ~$285k / $269–289k / 6 | +42% from $201k (Q2-24) in the 2024 round; a further +5% in the 2028 round | Seagems **92 / 53 / 17** `[F]`; fleet ~95 / 73 / 44 `[A]` | 285 vs 300 (−5%; 2027 has no new starts); Base 2028 295 vs 300 (−1.7%) |

**Anchors:**
- **NS PSV:** floor £9.2k; newbuild parity £20.2k (convention) / £23–25k (Tidewater); asset-implied £17.7k (Bourbon auctions) and **£19.3k (GEOS sales)**. The Base term (£19.5k) and the Base 2027 spot (£18.5k) sit just below convention parity, so there is no newbuild trigger yet.
- **NS AHTS:** floor £11.4k; newbuild parity ~£46.5k (at an assumed $90m); asset-implied ~£32k (the alternative mid-cycle). 2026 values were flat at $21.6–23m for 200 t-class units.
- **Brazil PSV:** foreign-built parity $27.7k < Base $38k < Brazil-built parity $41.7k < implied Petrobras newbuild charter $52–60k.
- **Brazil PLSV:** floor $90k < newbuild parity $205–226k (today's cost `[A]`) < Base mid-cycle $250k < today's $300k. Today is above parity, but no supply can respond inside the window.

## Drivers

### Oil and rig input and translation

| Input (Oil BBB 11 Nov; Rig BBB 12 Nov) | Supply effect |
|---|---|
| Brent Base **84** / 77 / 72 (2027 was 88); mid-cycle 70 unchanged; long end Dec-28 72.8, Dec-29 70.6, Dec-30 69.1 (was 77.4 / 73.5 / 70.7 on 3 Nov) | FIDs and tenders run on the long end and mid-cycle. The long end fell ~$3–5 but sits at Petrobras' own planning price ($70 for 2027–30, PN 2026–30 `[E]`) and far above offshore breakevens (contractors cite $30–40 `[E]`, rig baseline). NCS sanctioned projects and Petrobras capex are protected. Only spot-exposed UK activity is marginally weaker. **Not material: agrees with the oil baseline's "no action"** |
| Brent Bear 65 / 60 / 60; Bull 118 / 102 / 90 (unchanged) | Bear: UK drilling and exploration fall with a 6–18 month lag; Petrobras' capex envelope tightens; hits 2028–29. Bull: cash flow lifts tenders with a lag. The Bear catalyst (a deal) is closer per the oil baseline |
| Diesel crack 70 / 48 / 33 (unchanged) | Fuel is paid by charterers on North Sea time charters and supplied by Petrobras in Brazil. No rate effect |
| **NCS HE semis: net +1 in 2027 vs 2026.** In: Transocean Endurance (Equinor, Q2-27), Transocean Barents (Vår, Jun 2027–Jun 2030). Out: **Hercules to Canada in Q1-27** (correction; earlier notes counted it NCS). Deepsea Atlantic and Spitsbergen to Dec 2027; Nordkapp to end-2028; Norge (Harbour) to Oct 2028, options to Mar 2029, then Shell Mar–Jul 2029. NCS HE MCU 97 / 96 / 93% | **PSV:** 2–3 PSVs per semi campaign (DNO/Yantai 3; Ross/Harbour for Norge 3) `[F]`; NCS PSVs are often shared, so 2–3 `[A]`. Net 2027 vs 2026: Endurance ~0.75 + Barents ~0.6 − Hercules ~0.85 ≈ +0.5 rig-years, i.e. ~+1–1.5 PSV-years. That is less than the +2 semis assumed on 4 Nov (Hercules was missing). **AHTS:** two arrival hook-ups plus one tow-out in 2027 (~3 AHTS × 3–5 days each) and ~3–5 moored well-to-well moves a year per semi `[A]` |
| **UK: Beacon Pacific** (stranded CIMC 6G HE semi, likely moored `[A]`), six firm wells for Serica from Q3 2027, options incl. P&A; VALARIS Norway (Ithaca, Q2-27, ~200 days); VALARIS 122 (INEOS, DK from Feb 2027, UK from Jul 2027); Valaris 248 P&A (41 wells from Apr-27) and the SNS P&A award; Intrepid moves UK → NO in Q3-27 | **PSV:** +~1–1.5 PSV-years in H2-27 (Beacon Pacific); jackup campaigns ~1 PSV each. Together with the NCS line, NW Europe moored semis are +~1 rig-year in 2027 vs 2026 (≈ +2–3 PSV-years; ~2 pp of a 100+ vessel large-PSV fleet `[A]`). **AHTS:** one more arrival positioning (Q3-27) and rig moves. Supportive; below the 2 pp / 5% minimums on its own |
| NCS jackup P&A from Q3-27 (Noble Interceptor, Ekofisk, 670 days; a DNO well first) | P&A supply and standby PSV demand; shifts some UK work toward the NCS in H2-27 |
| Brazil: 47 operating / 35 drilling (1 Nov), flat; outstanding Petrobras rig-days 2027 210, 2028 1,185, 2029 780; plan unchanged; DS-8 to Shell Brazil (Mar 2027); DS-17 Equinor to Jan 2028 | Flat drilling-support PSV demand; AHTS demand stays FPSO/mooring-driven. Drillship rate changes (stub 455; Bull 2027 475) do not change OSV demand |
| Guyana/Suriname: DS-18 (Petronas) to May 2027, then to the US Gulf | −1 drillship in Suriname from mid-2027: a small PSV demand offset (~1–2 PSVs `[A]`) for the secondary row; not material |

**Political line (Brazil):** Lula was re-elected on 25 Oct (51.79%) `[F]`, so management and policy continue: CEO Chambriard stays and local content is kept. No measure has been taken since: no board change, capex revision or tender cancellation. The open question is how PN 2027–31 splits capital between E&P and refining/diesel self-sufficiency. BRL keeps weakening (USD/BRL 5.05 on 23 Oct → 5.59 on 12 Nov), which lowers the USD cost of Brazilian crew. There is no rate effect.

**Operational line:** no war or force-majeure impact in the focus regions. Tidewater books Middle East conflict costs (~$19.8m in 2026) outside the focus regions.

### Demand in vessel-days

- **North Sea — NCS:**
  - Secured: Equinor/Aker BP/Vår term demand (5-year PSV terms; Aker BP's 4-year PSV frame).
  - **Harbour's Transocean Norge campaign** takes three PSVs via Ross Offshore (Energy Swan, Viking Queen, Aurora Galaxy; ~265–290 days from early Jan 2027) `[F]`. That is ~800–870 PSV-days of well support, and the second 3-PSVs-per-semi calibration point after DNO/Yantai.
  - Equinor keeps extending incumbents (Viking Avant, Havila Charisma, Havila Foresight, Skandi Flora, Skandi Mongstad, Island Crusader, Kongsborg, Edda Fram) into 2027–28: term demand rolled, not added.
  - Rig changes: Endurance and Barents in, Hercules out (see the table): net +~0.5 rig-years in 2027 and +~1 in 2028.
  - Norway spot runs above the UK (Feb NOK 168k ≈ £13.2k vs UK ~£10.8k, SSY `[F]`).
- **North Sea — UK:** declining exploration drilling, rising P&A, and term appetite.
  - P&A: Valaris 248 from Apr-27; NEO NEXT+ riserless P&A (Hornbeck) from Q2-27. Beacon Pacific (Serica) from Q3-27.
  - Terms: NEO NEXT+ moved Havila Fanø and Herøy to 3-year terms to Sep 2029 (~730 PSV-days a year now secured); EnQuest extended Falcon Tide and Forth Tide to Sep/Oct 2027; Peterson extended Havila Borg (SNS) to Sep 2027 `[F]`.
  - Jackdaw has production approval; the Rosebank decision is expected by end-2026 `[E]`.
- **AHTS (North Sea):** lumpy (rig moves, hook-ups).
  - 2027 rig moves: Hercules tow-out (Q1), Endurance (Q2), Barents (Jun) and Beacon Pacific (Q3), plus moored well-to-well moves.
  - Equinor's AHTS term tender (1/3/5 years, start Jan-27 or Q3/Q4-27) had bids due 3 Nov; nothing was awarded by 12 Nov. An award of several vessels would take high-end units out of the spot pool and is the main near-term support for the spot row.
  - DOF has locked AHTS into term: Skandi Mariner to Q3 2028; two AHTS > 1 year from Q1-27; Skandi Vega to Q3 2029 `[F]`. Solstad Maritime's Q3 record came from its NS AHTS spot/project fleet `[F]`, i.e. from the strong Jul–Sep spot months.
- **Subsea/CSV:**
  - DOF: LOI for an I-class vessel in H1-28 ($50–100m incl. project services; full award due mid-Nov); North Sea decommissioning campaign in Q1-27 on one CSV ($15–25m integrated); Skandi Nomad to Nov 2027; **Skandi Constructor to Apr 2028 ($25–50m; region `[?]`)**; **a 7-year contract for one smaller CSV incl. ROV (~$110m ≈ $43k/day over 7 years, below the row class)** `[F]`.
  - Normand Maximus is firm with Saipem from Mar 2027 to May 2029 (+11 months option), after a Jan–Feb 2027 class docking `[F]`.
  - 2028 subsea demand is being booked; integrated project values are not vessel rates.
- **Offshore wind:** competes for CSVs and W2W capacity; the European CSOV market is near full employment at €50–75k for premium units (Sea1, Q2) `[E]`.
- **Brazil:**
  - 346 OSVs operating (Mar-26 `[E]`); PSV demand ~132 vessel-years `[E]`.
  - FPSO start-ups in 2027 (P-82, P-83, Albacora) and 2028 (Barracuda/Caratinga, SEAP I/II) `[F]`. At 7–8 vessels per FPSO for 12–15 months `[E]`, that is ~25 vessel-years of hook-up demand in 2027–28 `[A]`.
  - **PSV tenders** `[F]` (S53, S54): PSV 4500 (notice 7004675762, lots A–E) and PSV 3000 (notice 7004654576, lots A–B), at least one vessel per lot, so ≥ 7 vessels.
    - Four-year firm terms, start Jun–Oct 2027, 20-year age limit; proposals open 17 Nov 2026.
    - That is ≥ 28 PSV-years from H2-27. Whether it is replacement of expiring contracts or added demand is `[?]`.
  - **PLSV 2028 round:** four vessels at $295–309k for 4 years from Jan 2028, plus Seagems' third-party vessel (lot 5). This is mostly replacement demand: three DOFCON vessels and Jade re-contract. The third-party vessel is net +1 if it is new to Brazil `[?]`.
  - OSRV renewal continues (Oceanity's FOSRV Purity, 4 years, 30 Oct; no rate).
  - Exploration: Morpho (Equatorial Margin) and BP's Tupinambá find. These are long-dated, Bull-side signals for PN 2027–31, with no window demand.
  - A Brasil Energia headline (up to 20 PSVs, 12 OSRVs and 1 AHTS) **cannot be dated** and is not used (checkpoint 8).
- **Guyana/Suriname:** Errea Wittu (fifth Stabroek FPSO, 250 kb/d) arrived 21 Aug; first oil guided Q4-26 `[F]`. ExxonMobil vessel RFIs. DS-18 leaves Suriname after May 2027. DOF has two AHTS on a 150-day Caribbean project. Steady growth.

### Supply

- **North Sea PSV:**
  - Capital Offshore's 12 China newbuilds (2 more in 2026, 9 in 2027; global) `[F]`; Union Vega's 2 firm + 4 option PSVs from 2028 (West Africa/South America) `[F]`.
  - DOF's four older PSVs (Skandi Mongstad, Flora, Feistein, Kvitsøy) were delivered to their buyer in Q3 and stay on their contracts (DOF keeps management and a minority stake) `[F]`: ownership only.
  - GEOS sold Energy Partner, Energy Passion and Energy Empress (Dec-25 to Mar-26) `[F]`. The buyers and the vessels' regions after the sales are `[?]`.
  - October spot moves: Sar Brage in; Island Challenger, Skandi Caledonia and Sea Evertsen (AHTS) out; net −2. Aurora Galaxy (from Egypt) joins on term in Jan 2027: supply and demand together.
  - MH Monsoon to Guyana (Nov-26). Migration pull: the Petrobras PSV 4500/3000 tenders (4-year terms from mid-2027, vessels up to 20 years old) can draw North Sea PSVs to Brazil.
- **North Sea AHTS:**
  - Arrivals Jun–Sep: 9 vessels (Aurora Challenger, Bear, Boka Fulmar, Boulder, Fram Prince, Olympic Zeus, Sea Banckert, Sea Evertsen, Skandi Laser); departures 3 in Sep and 1 in Oct (Sea Evertsen) `[F]`.
  - October spot utilisation fell to 42% at £43.8k; Seabrokers cites "a long list" of arrivals after project charters elsewhere ended.
  - Ownership consolidation only, no new capacity: 2020 Bulkers (15 large AHTS); DDW Offshore's exit.
  - No AHTS newbuild for the North Sea; nobody builds > 300 t BP units ("prohibitive newbuilding costs", DOF).
- **CSV:**
  - **Fearnley Offshore Supply (30 Dec 2025) `[E]`:** ~30 firm newbuilds with 150 t and 250 t AHC cranes, > 20% of the active fleet, mostly China and almost all speculative; deliveries H2-26 to 2028, with 2027 a likely record (Fearnleys, Oct 2025). The figure is broker-sourced but **9–12 months old (stale)** and global. It includes DOF's two SALT 310s (Q4-27/Q1-28).
  - What it means: ~30 vessels against an active fleet of ~150 in this class. They arrive in 2027–28, which supports the Base fade (55 → 52 → 50) and the Bear. Where they work is open: Brazil, West Africa and wind compete with the North Sea.
  - Committed tonnage, capacity and demand together: REM Ocean (250 t, 2027, 8-year DeepOcean/Equinor IMR) and its sister REM Pioneer (2026); a Solstad Offshore newbuild CSV for H1-2029 on a long-term contract (Q2 report) `[F]`.
  - High-end, ownership only: Normand Maximus moves from Solstad Maritime to Solstad Offshore in Oct 2027; Skandi Implementer (400 t) is sold for delivery in Q2-27.
- **Brazil:**
  - 12 Brazilian-built hybrid PSVs (Starnav 6, first delivered Sep-26; Bram 6) have priority; DOF has 4 RSV newbuilds from 2030.
  - The Petrobras AHTS newbuild tender was cancelled (19 Jun 2026) `[F]`, so Brazil AHTS supply grows only by migration. Skandi Amazonas was lost (CTL, May-26).
  - PLSV: no newbuild; Seagems' third-party PLSV (MOU with purchase option) is +1 from 2028 if it is new to Brazil `[?]`.
- **Global context:** operational fleet 3,209 and laid-up 377 (Q4-25); orderbook 216 (~4% of fleet); share of tonnage > 20 years rising from 25% to 31%; marketed utilization 76% → 77% → > 79% `[E]`.

### Capital cycle (secondhand → newbuild parity → capital → orders)

- **Large PSV:** China newbuild $40–41m at £20–25k parity.
  - The NCS 2027-start term (~£20.6k) and the GEOS sale prices (asset-implied ~£19.3k) sit at convention parity.
  - **Watch for orders.** A second 2027–28 term at ≥ £21k on multi-year tenor, or a PSV order by a North Sea owner, would mark the turn; delivery would be 2029+. The orders so far are by non-North Sea owners (Capital Offshore, Union Vega).
- **Large AHTS:** values flat at $21.6–23m (200 t class, 15–16 yrs) and $27.1m average (2020 Bulkers), against record 2026 spot. Capital goes into consolidation and term lock-ups, not newbuilds.
- **Brazil:** capital enters via Petrobras-backed 12-year newbuild charters (implied $52–60k/day) and M&A (Tidewater–WSUT; OceanPact–CBO). Local content is kept.
- **CSV:** the speculative orders have already happened, and 2027–28 deliveries are the Bear catalyst. Owners keep high-end CSVs in-house: Solstad Offshore buys Normand Maximus at a 2022 strike, and DOF sells Implementer.
- **PLSV:** today's rate (~$300k, 2028 round) is above parity at today's cost ($205–226k `[A]`), yet nothing is ordered. Four-year terms, a ~3-year lead time and ~20 high-spec units held by three players `[F, company]` mean supply cannot respond inside the window.

### Region × segment matrix (material cells)

| Region × type | Utilization / status | Rate level / recent fixtures | Trend | Oil sensitivity | Confidence |
|---|---|---|---|---|---|
| NCS PSV | Term-heavy; one-well 2027 terms (Harbour/Norge ×3); GEOS fleet 94% (Sep) | 2027 starts ~£20.6k (Energy Swan); 5-yr Equinor NOK 230–240k; well option ~£25k (100 days) | Firming; the net semi count is +1 in 2027 (Hercules out) | Low (sanctioned) | Medium |
| UK PSV | Spot-heavy but with term appetite (NEO NEXT+ 3 yrs; EnQuest 1 yr) | Rates `[?]` (all D) | Up in 2026; P&A growth; Beacon Pacific from Q3-27 | Medium–high | Medium |
| North Sea PSV (pool) | Spot 82% (Oct); Tidewater Eur/Med PSV > 900 92.6% (Q3) | £19.5k (Oct); Tidewater realised $24.9k (Q3) | Tight H2-26 | Low–medium | Medium–high (data) |
| North Sea AHTS | 42% spot (Oct) | £43.8k (Oct), after £110.7k (Sep); term ~$41–68k (DOF, B/D) | Broke in Oct as arrivals landed; Nov `[?]`; Equinor term tender pending | Low (rig/FPSO-driven) | High (data), low (direction) |
| North Sea CSV | High (Sea1 100%, Q2) | Solstad 3 CSVs ~$143k incl. services (Dec-25/Jan-26) | Softening; high-end employed | Medium | Low |
| Brazil PSV | Low-to-mid 80s `[E]` | Ref. $40.7k; > $42k medium (Tidewater); bids open 17 Nov | Plateau; tenders restarted | Low (policy) | Medium–low |
| Brazil AHTS | Low-to-mid 80s `[E]` | DOF $82k blended; 5 DOF AHTS start 1Q27 "at better terms" | Firm; no Brazilian-built additions | Low | Low |
| Brazil RSV | High | $102–127k | Firm | Low | Medium |
| Brazil PLSV | 93–98% (Seagems) | 2028 round $295–309k (n = 4); in force $269–289k (Seagems), ~$263k (Subsea7), ~$180–245k (DOFCON to Jan 2028) | Re-pricing up at the 2028 roll | Low | Medium |
| Brazil CSV (not a row) | — | Solstad $74–85k (2026 starts) | Firm | Low | Medium |
| Guyana/Suriname PSV | Tidewater Americas PSV > 900 active 81.1% (Q3; incl. WSUT Brazil from Q3) | $34.2k realised (Americas, Q3) | Growing (fifth FPSO); DS-18 leaves mid-2027 | Low | Low |

Not assessed: other North Sea (DK/NL), Argentina, Trinidad, Colombia, Falklands.

### Global context

- **Tidewater Q3-26 `[F]`** (8-K, 9 Nov; vessel revenue ÷ days worked):

| Region / class | Day rate Q3-26 | Q2-26 | Active utilisation Q3-26 | Q2-26 |
|---|---|---|---|---|
| Europe/Med PSV > 900 m² (42 vessels) | $24,905 | $23,760 | 92.6% | 88.5% |
| Europe/Med AHTS > 16k bhp (3) | $55,455 | $44,502 | 75.1% | 80.5% |
| Americas PSV > 900 m² (12) | $34,153 | $35,554 | 81.1% | 71.4% |
| Worldwide fleet (212) | $23,775 | $22,938 | 79.2% | 81.4% |

- Worldwide weighted leading-edge term rate **$27,373** (+$3,033, +12.5% q/q). Europe/Med vessel opex ~$10.8k per available day.
- Guidance: 2027 revenue $1.70–1.75bn (2026: $1.43–1.44bn); management cites "a tight offshore vessel supply backdrop" `[E]`.
- WSUT (22 PSVs, Brazil) closed in Q3, so the Americas average now blends in Brazil.
- **Golden Energy** (North Sea cross-check): fleet working dayrate $21.0k (Aug) and $24.5k (Sep) at 93.7–94.3% `[F]`. No later monthly update was found.
- **DOF Q3 `[F]`:** fleet utilisation 86% (Q3-25: 87%). Shipowning EBITDA was up 26% y/y "primarily driven by new contracts at better terms and good spot market earnings". Backlog is $7.0bn incl. post-quarter additions.

### Balance check

- **NS large PSV:**
  - Base spot 2027 rises to £18.5k at 75% and term stays £19.5k. **Consistent:** term absorption (three Norge PSVs, Equinor extensions, UK terms) shrinks the spot pool in 2027. Demand rises a little (NW Europe moored semis +~1 rig-year), and supply adds mainly global newbuilds not assigned to the North Sea.
  - Spot fades to £16.5k at 74% in 2028–29 while term holds at £19.0–19.5k. **Explained:** the spot average includes the winter trough (Q1 factor 0.66), and newbuild deliveries and possible returns from Brazil loosen the spot pool first. A term premium over the annual spot mean is normal.
- **NS AHTS:**
  - Base holds utilisation ~62–65% while the rate falls ~20% from 2027 to 2029. The rate is set by peak-day scarcity; more vessels remove the extreme days.
  - October (42%, £43.8k) is the first month where supply clearly exceeded spot demand: the Base mechanism, but faster and deeper.
  - Base 2027 (62%, £75k) now needs the winter rig moves, the 2027 semi arrivals and departures, and term lock-ups (DOF; the Equinor tender) to absorb the arrived tonnage.
  - **One month is not enough to move 2027; the November report decides** (rule under Conclusion).
- **Brazil PSV:** flat demand + 12 newbuilds − foreign departures ≈ flat utilisation in 2027–28. The PSV tenders (≥ 7 vessels from mid-2027) are mostly renewal `[?]`. Base unchanged.
- **PLSV:**
  - 2027 is ~92–95% covered (Jade's bridge is the gap).
  - 2028: four of the ~9 roll vessels are re-priced at $295–309k for 4 years; Seagems' five (Apr–Sep 2028) and Subsea7's three still roll. The third-party vessel may add one unit.
  - Base 2028 (295) needs Petrobras to keep ~20 high-spec PLSVs employed at about today's level, and the round just did that for four.
  - Bear (270) now carries only the rest of the roll at ~10% below the round, plus signature risk.
- **Fleet reconciliation:** no regional census is available (`[?]`). No vessel is counted twice. 2020 Bulkers, DDW, WSUT, OceanPact–CBO, Normand Maximus, the DOF PSV sale and the GEOS sales are ownership changes only. North Sea arrivals and departures are listed by name.

## Signposts and monitoring

| Signpost | Threshold (Bear / Bull) | Now (12 Nov) | Previous (17 Oct baseline, 4 Nov update) | Direction |
|---|---|---|---|---|
| NS large PSV spot, quarterly avg | Q2/Q3 < £12k / > £22k | Q3-26 £19.7k; Oct £19.5k at 82%; Tidewater Eur/Med PSV > 900 92.6% (Q3) | Q3-26 £19.7k; Oct £19.5k (4 Nov) | Firm; Base 2027 raised to £18.5k |
| NS PSV Q4-26 spot test | Q4 > 15% from the 17 Oct Base quarter (£14.5k) | Fires if the Nov–Dec average > £15.25k; no November data | Same | Pending (Nov *Seabreeze* ~4 Dec) |
| NS large AHTS spot, monthly avg | < £50k for 3 months / > £100k through H1-27 | **Oct £43.8k at 42%: month 1 of 3**; Nov `[?]` | Same (4 Nov) | **Toward Bear**; November decides (rule under Conclusion) |
| NCS term PSV rate (2027 starts) | < NOK 215k / > NOK 275k | ~NOK 262k (Energy Swan, n = 1); no priced print since; GEOS sales capitalise ~£19.3k | ~NOK 262k | Up; no new print |
| UK PSV term appetite | UK operators back to spot only / multi-year UK terms spread to large PSVs | NEO NEXT+ 3-year terms (Havila Fanø, Herøy; medium); EnQuest 1-year (Falcon Tide, Forth Tide; large); Serica's Beacon Pacific campaign from Q3-27 | Same (4 Nov) | Towards Bull; not crossed |
| Equinor AHTS term tender | No award / 5-year award above Base 2027 spot | Bids were due 3 Nov; **no award announced by 12 Nov** (Nordic Financial Newsweb source, web) | No outcome (4 Nov) | Pending; the main near-term AHTS support |
| Net large PSV/AHTS moves into the NS spot pool | ≥ +3 per quarter / ≤ −3 per quarter | AHTS ~+6 net (Jun–Sep); Oct net −2 (classes partly `[?]`); Aurora Galaxy (PSV) arrives Jan 2027 on term | Same | AHTS supply arrived; Q4 so far −2 |
| Petrobras Strategic Plan 2027–31 (late Nov) | E&P capex cut > 10% or OSV target cut / ~200 OSVs and newbuild tenders confirmed | Date and figures not announced; PN 2026–30 plans at $70 Brent for 2027–30 `[E]`; Lula re-elected (continuity) | Same | Pending; the decisive Brazil signpost |
| Petrobras OSV tenders | None beyond the PSV round by Q2-27 / ≥ 2 large tenders by Q1-27 | PSV 4500 (5 lots) and PSV 3000 (2 lots) out; proposals open **17 Nov**; PLSV 2028 round concluded | PSV tenders out (4 Nov) | Base met; Bull half-met (2 PSV tenders, ~7 vessels) |
| PLSV 2028 round (5 lots, 4 yrs) | < $255k / > $310k (100% basis) | **Concluded at $295–309k** (Jade $309k; Buzios $305k; Recife, Olinda $295k); signatures remain; lot 5 rate `[?]` | Pending | **Base (closed).** Replaced by the next row |
| Rest of the 2028 PLSV roll (Seagems ×5 Apr–Sep 2028; Subsea7 ×3) | < $270k / > $320k | Not tendered `[?]` | — (new) | Pending |
| CSV newbuild deliveries | ≥ 10 delivered by end-2027 without contracts / slip | ~30 on order `[E]` (stale count); REM Ocean (committed) in outfitting; Solstad newbuild CSV H1-2029 (committed) | ~30 on order | Building |
| First large PSV/AHTS order by a North Sea owner | — / order at ≥ $45m (PSV) | None by a North Sea owner (Union Vega 2 + 4 options, Capital Offshore 12: non-NS owners) | None | Global PSV supply growing from 2027–28 |

**Open checkpoints and data gaps** (status this run):
1. **Seabrokers pre-2020 annual series** (2012–2019) for the mid-cycle. *Carried.*
2. **Petrobras PSV award rates:** the 17 Nov PSV 4500/3000 bid opening (bid rates by lot, bidders' flags, replacement vs added demand) and the Apr-25 18-PSV awards; the ABEAM fleet by flag. *Carried; 17 Nov is the first print.*
3. **PLSV:** signatures of the 2028 round; the lot-5 rate (Seagems' third-party vessel) and whether it is new to Brazil; the BRL share of the rates; the timing of the tender for the rest of the 2028 roll. **New (method):** a fleet-level PLSV cover series in place of Seagems' vessel table, now that Paratus is not tracked (skill question). *Partly closed* (round concluded).
4. **North Sea spot-pool size and laid-up counts.** *Carried* (the availability chart is not extractable).
5. **Large AHTS newbuild price; AHTS/CSV opex.** *Carried.*
6. **NS CSV vessel-only fixtures with rates.** *Carried* (Normand Maximus/Saipem: no rate; Skandi Constructor: value range only, region `[?]`).
7. **Vessel-per-rig and vessel-per-FPSO ratios.** *Carried*; two NCS points of 3 PSVs per semi campaign (DNO/Yantai; Ross/Harbour for Norge).
8. **Westhon AHTS result date; Brazil OSRV rates; date of the Brasil Energia "33 vessels" round.** *Carried.*
9. **Second broker series** (Hagland, Fearnley, Westshore). *Carried*; no public North Sea weekly series since SSY went private.
10. **Vessel-by-vessel cover.** *Partly closed:* Seagems and DOFCON done; DOF's AHTS table (S59) is a Gantt chart: only the 11 end dates beyond mid-2029 are readable as text, and the 2027–28 bars are not. NS term fleet, Brazil PSV/RSV and CSV still `[A]`.
11. **Energy Swan spec and leg split; the Viking Queen, Aurora Galaxy and Viking Avant rates.** *Carried.*
12. **PN 2027–31** (E&P capex vs PN 2026–30, OSV target, local-content terms, capital shift to refining). *Carried*; date not announced.
13. **Equinor AHTS term tender** (award, vessels, tenor, rate). *Carried*; nothing announced by 12 Nov. Watch DOF, Solstad, Siem, Island, Aurora and 2020 Bulkers releases and the November *Seabreeze*.
14. **Havila Fanø/Herøy spec and term rate.** *Carried.*
15. **DOF Q3 (12 Nov).** *Closed.* Read as market evidence: utilisation 86%; AHTS "very strong" cover for 2027–28; PLSV qualification; CSV awards. Skandi Nomad's crane class and region are still `[?]`.
16. **Newsweb via Edge** was not used in this run; owner releases came from Nordic Financial (Newsweb source). *Carried as a method note.*
17. **Post-election Petrobras measures** (CEO/board change, fuel-price intervention, dividend policy). *Carried*; none found to 12 Nov.
18. **Skandi Implementer buyer and price** (a 400 t CSV value point, above the row class). *Carried*; the DOF Q3 report gives no price. The Union Vega PSV price and option declarations: *carried*.
19. **Q4 NS spot test:** the November *Seabreeze* (~4 Dec) replaces the November estimate in the stubs and is month 2 of the AHTS Bear signpost. *Carried; the decisive observation for NS AHTS.*
20. **Classes of the October spot movers** (Sar Brage, Island Challenger, Skandi Caledonia). *Carried.*
21. **Beacon Pacific.** *Closed:* confirmed by the rig baseline (12 Nov) from the Odfjell and Serica releases.
22. **New: Skandi Mariner's region and spec** (OE Digital tags "Europe"; a 2017 Salt 200 design is reported but unverified). It decides whether the ~$44k/day option is a North Sea AHTS term print.
23. **New: the GEOS PSV sales** (Energy Partner, Energy Passion): build years and buyers' regions, to place them as North Sea value points.
24. **New: the Tidewater call (10 Nov)** for North Sea and Brazil commentary; transcript not found.

## For IAF

- **This update (12 Nov): changed values** (all below each reader's materiality test; see the change log):
  - **NS large PSV spot, Base 2027:** £16.5k → **£18.5k**, utilisation 72 → 75%. Q4-26 stub 15.3 → 16.4 (75%). Year-1 Base quarters 12.2 / 27.0 / 17.4 / 17.4.
  - **NS large PSV term:** utilisation stub 88 → 93% (latest observed quarter). Rates unchanged.
  - **Brazil PLSV:** stub 285 → 300 (leading edge); Bear 2028–29 255 / 250 → **270 / 265** (utilisation 82 / 80 → 86 / 84); Base 2028–29 ranges narrowed to 280–325 / 280–335; Bull mid-cycle 285 → **300** and Bull mid-cycle value $470m → **$512m**.
  - **Unchanged:** every other Base path and mid-cycle, all NS AHTS, CSV and Brazil PSV/AHTS/RSV values, anchors (newbuild parity, floors) and economic life (25 years).
- **Owners and rows to use:**
  - **DOF (`docs/DOF-analysis.md`):**
    - The rows DOF reads did not move in Base: NS AHTS spot, NS CSV, Brazil AHTS, Brazil RSV, the PLSV Base path and mid-cycle, anchors and economic life.
    - Company items from this run (its own update follows):
      - the DOFCON PLSV 2028 round, priced at the vessels' own rates ($305k / $295k / $295k at 100%, 4 years from Jan 2028), no longer at a relative change of the row;
      - Skandi Mariner firm to Q3 2028 ($15–25m);
      - the 7-year smaller-CSV contract (~$110m) and Skandi Constructor to Apr 2028 ($25–50m);
      - the AHTS cover table;
      - Q3 utilisation 86%.
    - These are backlog, not market rates. The NS AHTS spot pool is the row to watch: the November *Seabreeze* rule can cut Base 2027.
  - **Solstad (Offshore and Maritime; no analysis):** NS AHTS spot (Solstad Maritime's Q3 record came from it); Brazil CSV terms ($74–85k). Normand Maximus enters Solstad Offshore in Oct 2027 at $125m, debt-financed; it is firm with Saipem from Mar 2027 to May 2029. Treat it as growth capex at a 2022 strike, tested against its charter, not against the NS CSV row.
  - **Tidewater (no analysis):** Europe/Med PSV realised $24.9k (Q3) vs NS term Base 2027 £19.5k ($25.9k): a small positive mark-to-market. In Brazil (WSUT), use the Brazil PSV row and the 17 Nov bids.
  - **Golden Energy / Eidesvik / Havila (no analyses):** NS PSV term row; GEOS fleet dayrate as a monthly check; the GEOS sales as value points.
  - **Seagems (Brazil PLSV market data only; the owner is not tracked):** its public Petrobras prints (contractual $269–289k; Jade $309k from 2028) feed the PLSV row.
- **HY BBB (Oil Service row, OSV and subsea):** the direction is unchanged or firmer. NS PSV is firmer (spot Base 2027 up). NS AHTS is kept but under test, with October at Bear. Brazil PLSV is re-priced up for four vessels to 2031. Nothing points to higher OSV default risk in Base.
- **Spot convention reminder:** the NS spot rows are the mean of Seabrokers monthly averages.
- **Alternative PLSV mid-cycle anchors for any PLSV exposure:** $300k (today) and $205k (parity / previous cycle).

## Change log

- **12 Nov 2026 — full update (skill 2026-11-12.1; iaf-valuation 2026-11-10.1): Supply Market BBB changed in two rows (NS large PSV spot 2027; Brazil PLSV Bear and Bull); new baseline date 12 Nov (previous 17 Oct, 26 days).**
  - **Causes:**
    - stale after 9 Nov;
    - the triggers fired on 4 Nov (Petrobras PSV tenders; NS AHTS Q4 spot miss), plus the PLSV 2028 round results (9 Nov);
    - passed events: Tidewater Q3 (9 Nov), DOF Q3 (12 Nov), Equinor AHTS bids (3 Nov);
    - new oil (11 Nov) and rig (12 Nov) baselines.
  - **Changed (previous → new):**

| Item | Previous (17 Oct / 4 Nov) | New (12 Nov) | Reason | vs recalibration trigger |
|---|---|---|---|---|
| NS large PSV spot, Base 2027 rate (range) | 16.5 (13.5–19.5) | **18.5 (15.5–21.5)** | Several independent points: *Seabreeze* Jul–Oct £19.6k at 76% (de-seasonalised ~£18–21k); Tidewater Eur/Med PSV > 900 $24.9k at 92.6% (Q3, +4.8% / +4.1 pp q/q); term absorption into 2027; NW Europe moored semis +~1 rig-year | +12%: above the 10% minimum, below the 15% quarter trigger |
| NS large PSV spot, Base 2027 utilisation (range) | 72 (68–76) | **75 (71–79)** | Aug–Oct 79–82%; 2026 Jan–Oct mean 73% | +3 pp = the spot minimum |
| NS large PSV spot, Base 3-yr avg | 73 / 16.5 | 74 / 17.2 | Follows 2027 | — |
| NS large PSV spot, Base Year-1 quarters (rate; utilisation) | 10.9 / 24.1 / 15.5 / 15.5; 66 / 78 / 72 / 72 | **12.2 / 27.0 / 17.4 / 17.4; 69 / 81 / 75 / 75** | Same factors (2023–25) on the new annual value | — |
| NS large PSV spot, stub (rate; utilisation) | 15.3; 73 | **16.4; 75** | Mechanical: October + Nov–Dec at the new Base winter level (14.8; 72%) | Stub: never material |
| NS large PSV term, utilisation stub | 88 | **93** | Mechanical: latest observed quarter (Tidewater Q3 92.6%) | Stub |
| Brazil PLSV stub | 285 | **300** | Six-month leading edge = the 2028 round's median ($295–309k, n = 4) | Stub (mechanical) |
| Brazil PLSV Bear 2028 rate (range); utilisation (range) | 255 (235–275); 82 (76–88) | **270 (255–285); 86 (82–90)** | Four 2028 starts priced at $295–309k for 4 years; Jade booked from Jan 2028, so the "Jade idle" element falls away; the Bear now re-prices the rest of the roll ~10% below the round | +5.9%; +4 pp: below the 10% trigger |
| Brazil PLSV Bear 2029 rate (range); utilisation (range) | 250 (225–275); 80 (74–86) | **265 (245–285); 84 (80–88)** | As 2028 (Jade booked to 2031) | +6.0%; +4 pp |
| Brazil PLSV Bear 3-yr avg | 85 / 260 | 87 / 270 | Follows | — |
| Brazil PLSV Base 2028 / 2029 ranges | 265–325 / 265–335 | **280–325 / 280–335** | The round printed at $295–309k; points kept (295 / 300) | Range only |
| Brazil PLSV Bull mid-cycle | 285 | **300** | Anchor "today's level holds" moves from ~$285k to ~$300k (2028 round) | +5.3% |
| Brazil PLSV Bull mid-cycle value (11-yr-old) | $470m | **$512m** | Follows the Bull mid-cycle rate (same method) | — |
| Fleet-level PLSV cover 2027 / 28 / 29 `[A]` | ~93 / 45 / 25% | **~95 / 73 / 44%** (16 named units); Seagems 93 / 36 / 0 → **92 / 53 / 17** `[F]` | The 2028 round; DOFCON extensions to Jan 2028 | Cover |
| Asset anchors (added) | — | GEOS PSV sales $27.25–28m (asset-implied ~£19.3k); Tidewater Eur/Med opex $10.8k (Q3) | New/missed value points; the PSV opex convention $12.2k is kept | — |
| Stale after | 9 Nov | **12 Dec 2026** | 30 days; the same date as the rig baseline; events (17 Nov, PN, Nov *Seabreeze*) can force a small update | — |

  - **Kept after testing (explicitly):**
    - NS AHTS spot (all scenarios, stub 66). October is one month, and term lock-ups, rig moves and owner reports point the other way. A pre-set rule is attached to the November *Seabreeze*.
    - NS PSV term rates (no priced print; the GEOS sales and Tidewater confirm the level).
    - NS PSV spot 2028–29 and all Bear/Bull PSV values.
    - NS CSV, Brazil PSV (bids 17 Nov), Brazil AHTS, Brazil RSV.
    - PLSV Base 2027–29 (the round confirms 295 / 300), Base and Bear mid-cycle.
    - Secondary rows, every other mid-cycle and vessel value, the floors and parities, economic life (25 years), the Year-1 AHTS quarters.
  - **Weights:** 25/50/25 convention kept; never a probability.
  - **Inputs:**
    - **Oil 11 Nov:** Base 2027 88 → 84; long end ~$3–5 lower; mid-cycle unchanged. Checked: not material for supply (long end at Petrobras' $70 planning price, far above breakevens). Agrees with the oil baseline's "no action".
    - **Rig 12 Nov:** Base paths kept. Correction: Hercules leaves the NCS in Q1-27, so the net NCS semi gain in 2027 is +1, not +2. Beacon Pacific UK from Q3-27; DS-18 leaves Suriname after May 2027. Net NW Europe +~1 moored semi-year in 2027; below the minimums on its own; used as one supporting point for the PSV spot change.
  - **PLSV round assessed:** the user input (Fearnley/Infront TDN, 9 Nov) is partly corroborated by DOF's Q3 report (qualified for 4-year contracts from Jan 2028; > $500m backlog addition at DOF's share). Jade ($309k, 550 t, 100%) is the row-class comparable; the DOFCON prints are 300–650 t at $295–305k. The round confirms the Base row (detail under Conclusion).
  - **Other new evidence:**
    - DOF Q3 (utilisation 86%; AHTS cover; CSV awards; Skandi Mariner to Q3 2028, ~$33–55k/day, region `[?]`).
    - Tidewater Q3 (regional table; leading edge $27.4k, +12.5%; 2027 guidance).
    - Solstad Maritime and Solstad Offshore Q3 (4 Nov: record AHTS-driven quarter; Normand Maximus firm with Saipem Mar 2027–May 2029).
    - Seagems' EDD approval, primary text read (lowers docking capex, not life).
    - BRL 5.59 (weaker).
    - No Equinor AHTS award; no November spot data; no ≥ 3 core-class newbuild orders.
  - **Recalibration triggers:**
    - **Fired:** the PLSV tender awarded; the Petrobras PSV tenders (bids 17 Nov); the NS AHTS Q4 spot miss (kept with a rule); staleness.
    - **Pending:** the NS PSV Q4 test.
    - **Not fired:** net spot-pool moves (−2), newbuild orders, ownership changes at covered owners (Normand Tonjer sale: ownership only), strikes or force majeure.
  - **Forecast vs actual (2026, partly observed):** large PSV Jan–Oct mean £17.5k; with Nov–Dec at the new winter level (14.8) the year is ~£17.1k (17 Oct estimate ~£16.6k). Large AHTS Jan–Oct mean £106.6k; ~£101.7k for the year with Nov–Dec at £76.9k (with Nov–Dec at the 2025 Nov/Oct and Dec/Oct ratios on October, ~£97.5k).
  - **Skill revision 2026-11-12.1:** Paratus is no longer tracked. Paratus-specific guidance is removed from the body (For IAF, mid-cycle anchors, economic life). Seagems' Petrobras prints stay as PLSV market data.
  - **Layout:** dated history is removed from Metadata, Conclusion, Drivers, Signposts and For IAF. The per-run detail of 17 Oct, 28 Oct and 4 Nov stays in the entries below and in the appendix.
  - **IAF / downstream:** no reader's value moved by more than the recalibration trigger, and no Base IRR moves by ~1 pp (detail under For IAF).

- **4 Nov 2026 — small update (orchestrator request; skill 2026-10-10.3): no annual path, mid-cycle, value or weight changed; Q4-26 NS spot stubs re-marked; two recalibration triggers fired, so a full update is due. Baseline date stays 17 Oct.**
  - **Passed event: Equinor AHTS term tender, 3 Nov.** No award, rate, tenor or vessel announced (Nordic Financial/Newsweb to 4 Nov, web search, October Seabreeze). Treated as a bid deadline `[A]`; still pending.
  - **Changed (stub rule, mechanical):**

| Stub Q4-26 (all scenarios) | Previous (17 Oct) | New (4 Nov) | Basis |
|---|---|---|---|
| NS large PSV spot, £k/day | 14.5 | **15.3** | Oct £19.52k + Nov–Dec at Base winter level £13.2k |
| NS large AHTS spot, £k/day | 105 | **66** | Oct £43.79k + Nov–Dec at Base winter level £76.9k |
| NS large PSV spot utilisation, % | 68 | **73** | Oct 82% + Nov–Dec 69% |
| NS large AHTS spot utilisation, % | 62 | **55** | Oct 42% + Nov–Dec 61% |

  - The "seasonal-normal rest of quarter" is set at the mean of Base Q4-27 and Q1-27 (the Base path with the arrived supply). Two cross-checks give PSV 16.2–16.4 and AHTS 49–85 (stub note under the rate Interface).
  - **Unchanged (explicitly):** every annual rate, utilization and value path for 2027–29, mid-cycle, Year-1 quarters, secondary rows, economic life, cover figures, scenario weights (25/50/25 convention).
    - **NS AHTS 2027 (Base £75k) kept.** October (£43.8k, 42%) sits at Bear 2027. But it is one month from one series, AHTS seasonality is noisy (the Q4/Q1 rig-move season is ahead), and the Equinor term award is pending. The evidence threshold (several independent points, ≥ 10% on the annual average) is not met yet. It is the first test of the full update.
    - **NS PSV spot 2027 (Base £16.5k) kept.** October £19.5k at 82% and term absorption lean toward Bull, below the 10% minimum.
    - **Brazil PSV kept:** tenders without rates; bids open 17 Nov.
  - **Rig input (4 Nov):** Transocean Barents +1 NCS HE semi from Jun 2027 adds ~2–3 PSVs and ~30–75 AHTS-days a year `[A]`, below the 2 pp / 5% minimums. Deepsea Nordkapp and Norge are continuations. Drillship rate change: no OSV effect. Nothing else taken; Beacon Pacific (Seabreeze) flagged to rig-market-bbb.
  - **Oil input (31 Oct, update 4 Nov):** kept unchanged; stub 104.3; long end slightly lower; Bear deal catalyst closer. No supply effect; nothing taken.
  - **Text changed:** Metadata bullet and stale-after list; Conclusion; rate and utilisation stub cells and notes; Scenario definitions (Base Brazil tender note; Bear tender-gap note); Market check (PSV and AHTS spot rows); Drivers (rig table rows; NCS, UK, AHTS, Brazil demand; PSV and AHTS supply; balance check); signposts; checkpoints 4, 7, 11, 13 updated, 20–24 added; For IAF; fixture log; fleet register; spot history; sources S53–S57.
  - **Recalibration triggers:**
    - **Fired:** Petrobras PSV 4500 + PSV 3000 tenders published (≥ 7 vessels, 4-year, bids 17 Nov).
    - **Fired in substance:** NS AHTS Q4 spot quarter > 15% from Base (October −58% vs the £105k stub; utilisation −20 pp vs 62%). Q4 can only stay inside 15% with a Nov–Dec average ≥ £112k.
    - **Pending:** NS PSV Q4 (fires if Nov–Dec average > £15.25k).
    - **Not fired:** net spot-pool moves −2 (< 3), no ≥ 3 core-class newbuild orders, no ownership change at a covered owner, no strike or force majeure, no Petrobras plan. Baseline age 18 days.
  - **Forecast vs actual (2026, partly observed):** large PSV Jan–Oct mean £17.5k; with Nov–Dec at £13.2k the 2026 year is ~£16.8k (17 Oct estimate ~£16.6k). Large AHTS Jan–Oct mean £106.6k; ~£101.7k for the year with Nov–Dec at £76.9k.
  - **IAF / downstream:** DOF: Q4-26 AHTS spot stub only; no annual row. HY BBB: no row change (direction noted in For IAF).
  - **Suggested stale-after:** keep **9 Nov 2026**. The full update follows the full rig update (by 9 Nov) and Tidewater Q3 (9 Nov after the US close); DOF Q3 (12 Nov) and the Petrobras PSV bid opening (17 Nov) follow shortly after.

- **28 Oct 2026 — small update (orchestrator request; skill 2026-10-10.3): Supply Market BBB kept unchanged, paths unchanged, baseline date stays 17 Oct.**
  - **Passed event: Brazil runoff, 25 Oct.**
    - Facts: Lula re-elected, 51.79% to 48.21% (TSE). PBR −14.0% on 26 Oct. USD/BRL 5.05 → 5.35.
    - Statements: Chambriard calls the fall "speculative" and Petrobras "solid"; the programme keeps local content; PN 2027–31 is being prepared (board round 23 Oct, not approval).
    - Measures: none found (no CEO or board change, capex figure, tender or award).
    - Reading: the transition-delay channel is removed. The Base tender resumption (H1-27) is kept until a tender is seen. Brazil rows unchanged.
  - **Changed (text only, no value):**
    - Scenario definitions: the Bear and Bull Brazil catalysts are narrowed (transition and new-board variants removed); one Bear signpost is reworded; the Base note is added.
    - Conclusion catalyst lines.
    - Political line in Drivers.
    - Signposts: runoff resolved; PN and OSV tender rows updated; Union Vega order added.
    - Checkpoint 12 partly closed; checkpoints 17–19 added.
    - Fleet register: Skandi Implementer and Union Vega added. Fixture log: Skandi Acergy added.
    - Sources S46–S52.
    - Correction: the Oil BBB Base column in Scenario definitions still showed 85 / 77 / 72. It is set to 88 / 77 / 72, the 17 Oct oil input already recorded in Metadata. This is text only; no supply value depended on it.
  - **Inputs read, nothing taken:**
    - Rig Market BBB small updates of 22, 24 and 28 Oct, paths unchanged (Prospector 5 is in Gabon; T-16 in Malaysia/JDA).
    - Oil Market BBB of 24 Oct: paths and mid-cycle unchanged; Dec-28 78.8, Dec-29 74.8.
  - **Recalibration triggers:**
    - Ownership change at a covered owner (DOF, Skandi Implementer): met in form. Assessed: one 400 t CSV in the Gulf of Mexico, outside the row class and region, no price. No change.
    - Newbuild orders: Union Vega has 2 firm, below the ≥ 3 threshold.
    - No priced NS term fixture or Petrobras award; no Petrobras plan or large tender; no spot quarter newly complete.
    - Baseline age 11 days.
  - **Unchanged (explicitly):** every rate, utilization and value path, mid-cycle, Year-1 quarters, secondary rows, economic life, cover figures and the 25/50/25 convention weights.
  - **Forecast vs actual:** nothing new (October Seabreeze due early Nov).
  - **IAF / downstream:** DOF (NS and Brazil rows, anchors, economic life) and HY BBB (OSV rows): no change.

- **17 Oct 2026 (skill 2026-10-10.3): Supply Market BBB kept unchanged.**
  - **New baseline date:** 17 Oct 2026 (previous 10 Oct 2026).
  - **Unchanged (explicitly):** every rate, utilization and value path, every mid-cycle figure, the Year-1 quarters, the secondary rows, the scenario definitions and the 25/50/25 convention weights.
  - **Why nothing moved:**
    - No new Seabrokers month (October due early Nov).
    - No term fixture or Petrobras award with a rate (Viking Avant, Havila Fanø/Herøy and Skandi Nomad are all grade D).
    - The Brent Base 2027 +3 does not move FID or tender logic (oil baseline, 17 Oct).
    - The rig input is unchanged for OSV demand.
  - **Recalibration triggers checked; none fired:**
    - No North Sea spot quarter is newly complete.
    - No priced fixture is > 10% from Base.
    - No Petrobras plan or large OSV tender has been published.
    - There are no new newbuild orders in a core class: REM Ocean is an existing, committed order.
    - The two Havila medium PSVs leaving the spot pool are below the 3-vessel threshold and not large class.
    - No ownership change at a covered owner. No strike or force majeure.
    - Baseline age was 7 days.
  - **Changed (`[A]` cover and text only):**
    - NS PSV term cover 2027 ~70% → ~71% (Viking Avant).
    - NS CSV cover notes added.
    - Oil input reference updated to the 17 Oct baseline (Brent Base 2027 88).
    - New signpost: UK PSV term appetite.
    - Checkpoints 14–16 added.
    - FX refreshed (17 Oct).
    - A duplicated Normand Maximus line in Drivers was removed.
  - **Forecast vs actual:** nothing new to test (October Seabreeze pending).
  - **Weights:** 25/50/25 convention kept; never a probability.

- **Second run, 10 Oct evening (skill 2026-10-10.3), targeted:**
  - **Checked: the "~30 CSV newbuilds" figure.**
    - Source: Fearnley Offshore Supply, 30 Dec 2025 (S23 restated; S36).
    - ~30 firm 150–250 t AHC units, > 20% of the active fleet, almost all speculative, mostly China. Deliveries H2-26 to 2028, 2027 a likely record (Fearnleys, Oct 2025, S37).
    - Kept, flagged stale (9–12 months) and global.
  - **Searched: vessel-only CSV fixtures.**
    - None with a disclosed rate in 2026 (n = 0): Normand Navigator LOI (450 days from Q2-26), Normand Maximus (Q1-27 to Q1-29), Normand Subsea (2 years from Jan-26) and the Seven Viking IMR extension all have confidential terms.
    - Class levels for H1-25 (150 t > $60k, 250 t > $80k) added to the market check as grade C.
    - NS CSV row unchanged (55 / 52 / 50; mid-cycle 45), still low confidence.
  - **Added: economic life per row with evidence** (asset table). Every row stays at 25 years. Transactions for PSV, AHTS and CSV do not support a longer life. PLSV: the Seagems extended-docking programme is noted as the open route to a longer life (`[?]` primary).
  - **Unchanged:** all rates, utilizations, values, scenarios and signposts.
- **New baseline date:** 10 Oct 2026 (previous 5 Oct 2026, initial).
- **Changed — Brazil PLSV (correction of a basis error),** Bear / Base / Bull, USD k/day:

| Brazil PLSV | Stub | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| Previous (wrong basis) | 140 | 135 / 140 / 145 | 125 / 145 / 165 | 122 / 148 / 170 | 120 / 140 / 160 |
| New | 285 | 275 / 285 / 295 | 255 / 295 / 335 | 250 / 300 / 345 | 215 / 250 / 285 |

- **PLSV details:**
  - 2027–29 are a restatement (× 2.036, ratios kept).
  - **Mid-cycle is also re-anchored:** restated 245 / 285 / 325 → 215 / 250 / 285. The previous mid-cycle simply equalled today's level; it is now anchored on the previous round, parity and today.
  - Related corrections: PLSV opex $38.3k / $44.5k → **$77k / $90k**; Seagems backlog 3.6 → **1.9 years**; PLSV cover 95 / 70 / 55 → Seagems **93 / 36 / 0** (fleet ~93 / 45 / 25 `[A]`); Subsea7 awards "not comparable" → **comparable**; PLSV newbuild cell filled ($267–317m, 2012 `[E]`).
  - Source: `docs/PLSV-analysis.md`, `docs/DOF-analysis.md` (Paratus Q2-26 deck at 100%).
- **Changed — other rows and text:**
  - **NS large PSV term:** Base 2027 18.5 (17.5–19.5) → **19.5 (18.0–21.0)**; Bull 2027 20.0 → **21.0**; 3-yr avg Base 19.0 → 19.3, Bull 21.7 → 22.0. Reason: Energy Swan, Viking Queen, Energy Paradise, the GEOS fleet trend and rig-baseline NCS additions (see Conclusion). 2028–29 unchanged (< 5% minimum change).
  - **Scenario text:** Brazil transition added to Bear and Bull. Base tender resumption moved Q1-27 → H1-27. Signposts restated for PLSV (100% basis) and NCS term (NOK 230–265k). Equinor AHTS tender and Brazil runoff added.
- **Unchanged (explicitly):**
  - NS PSV spot, NS AHTS spot, NS CSV, Brazil PSV, Brazil AHTS, Brazil RSV, all utilization paths, the Year-1 quarters and the secondary rows.
  - Reason: no new Seabrokers month (October due early Nov); Brazil evidence is political/timing, not rates; DDW AHTS sales confirm the asset-implied anchor rather than move it.
- **User input assessed:** the Nordnet item is a copy of the SOFF/SOMA Newsweb release (6 Oct). Intra-group option at a 2022 strike; no capacity, no rate; high-end class outside the CSV row. Logged as an ownership change and an asset reference, not a market price.
- **Forecast vs actual:** nothing new (October Seabreeze pending).
- **Weights:** 25/50/25 convention kept; never a probability.
- **Method (skill revision 2026-10-10.1):**
  - Newsweb sweep via the Edge connection added as a source.
  - New rule: convert JV-share figures to a 100% vessel basis before computing rates.
  - PLSV row basis stated (550 t, 100%).
  - Quirks added: SSY weekly no longer public; Nordnet via Edge; GEOS monthly cross-check.

## Appendix

### Fixture and award log (selection; new entries this run first)

| Vessel | Class | Region | Charterer | Start | Firm term | Rate | Scope | Grade | Source |
|---|---|---|---|---|---|---|---|---|---|
| **Skandi Buzios** (new 12 Nov; 2017, 650 t lay system, sister of Açu) | PLSV | Brazil | Petrobras | 1 Jan 2028 (or 360 days after signing) | 4 yrs | **$305k** (100%) | Charter + services (vessel + crew) | C (corroborated by DOF, B) | S58, S59 |
| **Skandi Recife / Skandi Olinda** (new 12 Nov; 340 t system / 300 t contracted) | PLSV | Brazil | Petrobras | 1 Jan 2028 | 4 yrs | **$295k** each (100%) | As above | C (corroborated by DOF, B) | S58, S59 |
| **Sapura Jade** (new 12 Nov; Seagems, 550 t) | PLSV (row class) | Brazil | Petrobras | Jan 2028 | 4 yrs | **$309k** (100%) | As above | C | S58 |
| Seagems third-party vessel (lot 5) (new 12 Nov) | PLSV (spec `[?]`) | Brazil | Petrobras | 2028 | 4 yrs | `[?]` | — | D | S8, S58 |
| **Skandi Olinda** extension (new 12 Nov; announced 5 Nov) | PLSV | Brazil | Petrobras | Apr 2027 → Jan 2028 | +304 days | `[?]` | — | D | S59 |
| **Skandi Mariner** (new 12 Nov; option declared 9 Nov) | AHTS (spec `[?]`; reported 2017, Salt 200, unverified) | `[?]` ("Europe" tag) | `[?]` | Q2 2027 → Q3 2028 | ~15 months (~455 days `[A]`) | $15–25m ("Significant") ≈ $33–55k/day (mid ~$44k) | TC | D (range) | S60 |
| **Two DOF AHTS** (new 12 Nov; announced 30 Jul) | AHTS (`[?]`) | `[?]` | `[?]` | Q1 2027 | > 1 year each | $15–25m each ≈ $41–68k/day at 365 days | TC | D (range) | S60 |
| **Two DOF AHTS, Caribbean** (new 12 Nov) | AHTS | Caribbean | `[?]` | 2026–27 `[?]` | 150 days combined | $15–25m ≈ $50–83k per vessel-day | Project | D (project value) | S59 |
| **Skandi Constructor** extension (new 12 Nov; 11 Nov) | CSV (`[?]` class) | `[?]` | `[?]` | to Apr 2028 | extension | $25–50m ("Substantial") | `[?]` | D | S60 |
| **DOF smaller CSV, 7-year contract** (new 12 Nov; 11 Nov) | Small CSV (below the row class) | `[?]` | `[?]` | `[?]` | 7 yrs | ~$110m ≈ $43k/day over 7 years | Vessel + ROV | B (value ÷ days, full-year hire assumed) | S60 |
| **Normand Maximus** firm (new 12 Nov) | High-end CSV (900 t) | Worldwide | Saipem | Mar 2027 (after a Jan–Feb 2027 class docking) | to May 2029 (26 months) + 11 months option | `[?]` | Vessel (+ services per LOI) | D | S62 |
| **Aurora Galaxy / Energy Swan / Viking Queen** (new 4 Nov) | PSV (Aurora Galaxy class `[?]`; Energy Swan large) | NCS | Ross Offshore for Harbour Energy (Transocean Norge campaign) | early Jan 2027 | ~265–290 days | `[?]` (Energy Swan ~£20.6k, B, from the 2 Oct release) | TC | D (Swan B) | S53 |
| **Havila Charisma / Havila Foresight** (new 4 Nov) | PSV (Havyard 833L / MT 6010 MkII) | NCS | Equinor | direct continuation | 1-year options to Dec 2027 / Jan 2028 | `[?]` | TC | D | S53 |
| **Skandi Flora, Skandi Mongstad, Island Crusader, Kongsborg** (new 4 Nov) | PSV | NCS | Equinor | direct continuation | 1-year extensions | `[?]` | TC | D | S53 |
| **Edda Fram** (new 4 Nov) | PSV | NCS | Equinor | direct continuation | 6 months to Apr 2027 | `[?]` | TC | D | S53 |
| **Havila Borg** (new 4 Nov; 2009, Havyard 832) | PSV (medium `[?]`) | SNS (NL) | Peterson Den Helder | direct continuation | option to Sep 2027 (+15 months options) | `[?]` | TC | D | S53 |
| **Falcon Tide / Forth Tide** (new 4 Nov; 2013, Ulstein PX105) | Large PSV | UK | EnQuest | direct continuation | 1 year to Sep / Oct 2027 (+12 months options) | `[?]` | TC | D | S53 |
| **Siem Opal** (new 4 Nov) | AHTS on supply duties | NCS | Equinor | Oct 2026 | spot | `[?]` | Supply duties (PSV shortage) | D | S53 |
| **Large PSV spot (Oct avg)** (new 4 Nov) | > 900 m² | North Sea | various | Oct 2026 | spot | **£19,519 (11,926–41,337)** | TC | A (broker avg) | S53 |
| **Large AHTS spot (Oct avg)** (new 4 Nov) | > 22k bhp | North Sea | various | Oct 2026 | spot | **£43,794 (21,864–71,555)** | TC | A (broker avg) | S53 |
| **FOSRV Purity** (new 4 Nov) | OSRV (fast) | Brazil | Petrobras | `[?]` | 4 yrs firm | `[?]` | TC | D | S56 |
| **Petrobras PSV 4500 (lots A–E) / PSV 3000 (lots A–B) tenders** (new 4 Nov) | PSV 4500 / PSV 3000 | Brazil | Petrobras | Jun–Oct 2027 | 4 yrs | `[?]` (proposals open 17 Nov 2026); 20-year age limit | TC | — (tender, no award) | S53, S54 |
| **Skandi Acergy** (new 28 Oct; announced 22 Oct) | CSV | Africa (outside focus regions) | undisclosed | early Q1 2027 | ~100 days | $15–25m ("Significant") | Integrated subsea installation (PM, engineering, vessel) | D (project value, not a vessel rate) | S51 |
| **Viking Avant** (new 17 Oct; 2004, LNG) | PSV (large `[?]`, spec not re-verified) | NCS | Equinor | direct continuation | to end-2027 (+ option) | "current market terms" `[?]` | TC | D | S40 |
| **Havila Fanø / Havila Herøy** (new 17 Oct) | Medium PSV `[?]` (spec to confirm) | UK | NEO NEXT+ Energy E&P UK | direct continuation of spot work (Oct 2026) | 3 yrs to Sep 2029 (+ 3 × 1 yr) | "market terms" `[?]` | TC | D | S40 |
| **Skandi Nomad** (new 17 Oct) | CSV (crane class `[?]`) | `[?]` | `[?]` | Nov 2026 | 12-month option declared; firm to Nov 2027 | < $15m ("Limited") → < ~$41k/day at full-year hire | `[?]` | D (upper bound) | S40 |
| **DOF CSV, North Sea decommissioning** (new 17 Oct) | CSV | North Sea | North Sea operator (unnamed) | Q1 2027 | one campaign | $15–25m ("Significant") | Integrated: PM, engineering, ROV, survey, removal, disposal | D (project value, not a vessel rate) | S40, S41 |
| **Energy Swan** | Large PSV | NCS (+1 month undisclosed region) | two international charterers | Oct 2026 / Jan 2027 | ~1 month + ~290 days (+ ~500 days options) | $8.7m firm ≈ $27.2k ≈ **£20.6k / NOK 262k** (2 Oct FX) | TC | B | S28 |
| **Energy Paradise** | PSV | North Sea (Peterson) | Peterson | mid-Oct 2026 | well option ~100 days | $3.4m ≈ $34.0k ≈ £25.1k (10 Sep FX) | TC | B | S28 |
| **Viking Queen** | PSV | NCS (implied) | undisclosed | early 2027 | one well ~290 days + options | `[?]` | TC | D | S28 |
| **DOF I-class vessel** | Subsea/CSV | `[?]` | undisclosed | H1 2028 | LOI, "Large" ($50–100m) | `[?]` | incl. project management, engineering, logistics | D | S28 |
| **Normand Maximus** | High-end CSV (900 t / 550 t VLS) | Worldwide | international subsea contractor | Q1 2027 | to Q1 2029 (+ option to Q1 2030) | `[?]` | Vessel + 2 WROV + tooling + survey | D | S28 |
| Normand Scorpion / Saracen | AHTS | APAC | undisclosed | Q2/Q3 2027 | 475 days (+ 400 options) | $10–30m combined, upper end | Drilling support | B (range) | S28 |
| Sygna Tide (2014, VARD 1 07) | Large PSV | NCS | Equinor | ~late Oct 2026 | 5 yrs + 5×1 | `[?]` | TC | D | S1 |
| North Barents (2017, ST-216) | Large PSV | NCS | Equinor | 2026 | 5 yrs | `[?]` | TC | D | S1 |
| Polaryssel | Large PSV | NCS | Equinor | 1 Jan 2026 | 5-yr extension | NOK 233k (£18.3k) | TC | C | S20 |
| Kongsborg | Large PSV | NCS | Equinor | 2026 | term | NOK 230–240k | TC | C | S20 |
| Sjøborg (2012) | PSV | NCS | Equinor | Oct 2026 | +1 yr | `[?]` | TC | D | S1 |
| Havila Fanø / Herøy | Medium PSV | UK | NEO NEXT+ | Sep 2026 | 45 days each | `[?]` | TC | D | S1 |
| Viking Prince | PSV | NCS | Aker BP | 2026 | 3 yrs (4-yr frame) | `[?]` | TC | D | S21 |
| MH Monsoon | PSV | Guyana | Saipem | ~Nov 2026 | 250 days + 100 | `[?]` | TC | D | S1 |
| Pacific Discovery / Duchess | D-class AHTS | Spain | Repsol | Nov 2026 | ≥ 220 days | `[?]` | P&A support | D | S1 |
| Large AHTS spot (Sep avg) | > 22k bhp | North Sea | various | Sep 2026 | spot | £110.7k (70–145k) | TC | A (broker avg) | S1 |
| Aurora Saltfjord | Large AHTS | NCS | Equinor | Feb 2026 | rig move | NOK 3.0m | TC | A | S19 |
| Skandi Iguaçu, Angra, Paraty, Urca | Large AHTS (260–350 t BP) | Brazil | Petrobras | Jan/Feb 2026 | 4 yrs | $82.2k blended (3 with WROV) | TC + ROV | B | S10 |
| DOF 5 AHTS + 3 RSV (new 4-yr contracts) | AHTS / RSV | Brazil | Petrobras | 1Q 2027 | 4 yrs | > $950m per fleet incl. extensions; per-vessel `[?]` | — | D | S35 |
| Skandi Commander | RSV | Brazil | Petrobras | Jan 2027 | 4 yrs | $102.7k | Vessel + ROV | B | S9 |
| 4 × DOF RSV newbuilds | RSV | Brazil | Petrobras | 2030 | 12 yrs | ~$114k | Vessel + 2 WROV | B | S9 |
| OceanPact RSVs (A3 / A4) | RSV | Brazil | Petrobras | 2025 | `[?]` | bids $127k / $102k | Vessel + ROV | A (bids) | S11 |
| Normand Commander / Flower / Valiant | CSV | Brazil | Petrobras | Q1-26 / Jan-26 / Q4-26 | 4 / 4 / 2 yrs | $74.0k / $78.8k / $84.9k | excl. ROV (Commander) | B | S12 |
| Normand Navigator / Cutter / Jarstein | CSV | Brazil / NCS | subsea contractor | Dec-25/Jan-26 | 175 days total | $142.9k | incl. ROV/survey | B | S12 |
| **Seagems: Diamante / Topazio / Esmeralda / Onix / Jade / Rubi** (restated) | PLSV 550 t | Brazil | Petrobras | 2024–25 | to Apr-28 / Apr-28 / May-28 / Sep-28 / Jul-27 / May-28 | $289k / $289k / $269k / $289k / $287k / $287k (100%) | Vessel + crew; BRL component | A (company) | S35 |
| Seagems fleet realised | PLSV | Brazil | Petrobras | — | — | $278k (Q4-25), $281k (Q1-26), ~$280k per working day (Q2-26, 100%) | contract revenue | A/B | S8, S35 |
| 2024 Petrobras PLSV round (Seagems) | PLSV | Brazil | Petrobras | 2025 | 6 × 3 yrs | ~$1.8bn ≈ $274k | — | B | S35 |
| Seven Rio / Cruzeiro / Sun / Waves | PLSV | Brazil | Petrobras | 2025 | 3/3/3/4 yrs | ~$263k (comparable) | incl. services | B | S13 |
| DOFCON (Açu, Niterói, Vitória; Buzios, Recife) | PLSV | Brazil | Petrobras | 1Q27 / to Jan-28 | 3 yrs / extensions | ~$180–245k (100%) | — | B | S35 |
| Petrobras PSV 4500 (tender, Apr-25) | PSV | Brazil | Petrobras | 2026 | 4 yrs | reference $40,670.51 | TC | A (reference) | S14 |
| 12 × hybrid newbuild PSVs (Bram 6, Starnav 6) | PSV 5,500 dwt | Brazil | Petrobras | 2026–28 | 12 yrs | R$16.5bn total ≈ $52–60k/day | incl. newbuild capital | B | S15 |
| Petrobras PSV 3000 bareboat | PSV | Brazil | Petrobras | `[?]` | bareboat + technical management | `[?]` (bids closed 28 Aug 2026) | BBC | D | S32 |
| Theseus Z / Apollo Z | AHTS / AHTS-R | Brazil | Petrobras | `[?]` | `[?]` | $49.5k / $65.1k | TC | C (undated) | S16 |
| Normand Vibran / Trym | PSV | Brazil | Petrobras | 2024–25 `[?]` | 4 yrs 4 mo | ~$27.6k (NOK 500m total) | TC | B | S17 |

### Fleet register, newbuilds and reactivations (material items)

| Vessel / group | Class | Owner | Status / date | Effect | Source |
|---|---|---|---|---|---|
| **Energy Partner / Energy Passion / Energy Empress** (new 12 Nov) | PSV / PSV (PX121) / MPSV | GEOS → undisclosed buyers | Sold at $27.25m / $28.0m / $30.0m gross; closed Dec-25 to Mar-26 | Ownership only; PSV value points (asset-implied ~£19.3k) | S60 |
| **Four DOF PSVs** (Skandi Mongstad, Flora, Feistein, Kvitsøy) (updated 12 Nov) | PSV (2008–12) | DOF → buyer with DOF minority stake | Delivered in Q3-26; stay on current contracts; DOF manages | Ownership only | S18, S59 |
| **Skandi Connector** (new 12 Nov) | Cable layer | DOF → buyer `[?]` | Delivered Q3-26 | Outside the rows | S59 |
| **Normand Tonjer** (new 12 Nov) | `[?]` | Solstad Offshore (56%) → buyer `[?]` | Sold in Q3-26 ($24m accounting gain) | Ownership only | S62 |
| **Solstad Offshore newbuild CSV** (new 12 Nov) | CSV (spec `[?]`) | Solstad Offshore | Contracted Q2-26 for delivery H1-2029, backed by a long-term contract | Committed CSV supply and demand together, after the window | S62 |
| **Hercules** (rig; new 12 Nov) | HE semi (SFL, Odfjell-managed) | — | Leaves Norway for Canada (≥ 400 days from Q1 2027) | NCS PSV/AHTS demand −1 semi from Q1-27 (rig baseline correction) | S65 |
| **Beacon Pacific** (rig; new 12 Nov) | Stranded 6G HE semi (CIMC) | — | Six firm wells for Serica, UK, from Q3 2027 | UK PSV/AHTS demand +1 semi from Q3-27 | S65 |
| **NS spot movers, Oct 2026** (new 4 Nov) | Arrival Sar Brage; departures Island Challenger, Skandi Caledonia, Sea Evertsen (AHTS) | various | Oct 2026 (Seabreeze; excludes term/layup moves) | Net −2 for the spot pool; classes `[?]` except Sea Evertsen | S53 |
| **Aurora Galaxy** (new 4 Nov) | PSV | Aurora Offshore | From Egypt to the NCS, on hire early Jan 2027 (Harbour/Norge) | NS PSV +1 on term: supply and demand added together | S53 |
| **Vortex Victory + 3** (new 4 Nov) | Small AHTS (62.8 m, 80 t BP) | Vortex Offshore (Kotug majority) | Launched at Guangzhou Shunhai; deliveries 2027 (2) and 2028 (2) | Outside the large-AHTS class and the focus regions | S53 |
| **Horizon Maritime** (new 4 Nov) | AHTS, PSV, icebreaker, tugs (Canada) | → Chouest Group | Acquisition announced Oct 2026 | Ownership only; outside the focus regions | S53 |
| **Skandi Implementer** (new 28 Oct) | High-end CSV (2018, 137.6 m, 400 t crane rated to 3,000 m, 129 berths) | DOF → undisclosed buyer | Sale agreed 23 Oct 2026; delivery Q2 2027; price not disclosed | Ownership only. Gulf of Mexico, outside the NS CSV row class (150–250 t) and the focus regions. DOF: "material reduction" in net debt | S51 |
| **Union Vega Offshore PSVs** (new 28 Oct) | PSV, 84 m, 900 m² deck, battery-hybrid (Breeze design) | Union Vega Offshore (UK-based JV formed Apr 2026) | Ordered at Fujian Mawei: 2 firm + 4 options; first delivery 2028; price not disclosed (Baird, 19 Oct 2026) | Global PSV +2 firm from 2028, aimed at West Africa/South America. Below the ≥ 3-order trigger | S51 |
| **REM Ocean** (new 17 Oct) | CSV/ESCV, 250 t crane, methanol-ready | Rem Offshore | Hull delivered by Song Cam (Vietnam) 15 Jun 2026; arrived at Myklebust (Norway) for outfitting; delivery 2027 | NS CSV +1 in 2027, committed (8-yr DeepOcean/Equinor IMR to 2035): capacity and demand added together. Sister REM Pioneer due 2026 | S41 |
| **Normand Maximus** | High-end CSV (900 t, 550 t VLS, 178 m) | Solstad Maritime → Solstad Offshore | Option declared 6 Oct 2026; delivery Oct 2027; $125m, debt-financed | Ownership only | S28, S29, S33 |
| **Skandi Atlantic / Emerald / Peregrino** | AHTS (200 t BP / 16,315 bhp) | DDW Offshore (Akastor) → unnamed buyers | Sold Jan / Jun / Oct 2026 at ~$23m / $23m / $21.6m | Ownership only; DDW has no vessels left | S28, S34 |
| Petrobras AHTS newbuild tender | AHTS | — | Cancelled 19 Jun 2026 | No Brazilian-built AHTS additions | S35 |
| Third-party PLSV | PLSV | Seagems (MOU, purchase option) | Bid accepted 18 Sep 2026; formal award pending | +1 PLSV from 2028 if new to Brazil `[?]` | S8 |
| ACE Aristotelis + 11 sisters | PSV (8) / MPSV (4) | Capital Offshore (UOS Capital) | 1 delivered Sep-26; 2 more 2026; 9 in 2027 | Global supply +12 (not assigned to the NS) | S1 |
| Starnav Elektra + 5; Bram 6 | PSV (Brazil-built) | Starnav / Bram | First delivered Sep-26; rest 2026–28 | Brazil +12 Brazilian-flag, priority | S1, S15 |
| 15 large AHTS | AHTS | AHTS AS → 2020 Bulkers | SPA Sep-26 | Ownership only | S1 |
| 4 PSVs (Skandi Mongstad, Flora, Feistein, Kvitsøy) | PSV (2008–12) | DOF → `[?]` | Sale, delivery Q3-26 | NS supply `[?]` (depends on buyer) | S18 |
| 2 × SALT 310 CSVs | CSV 250 t | DOF (from Geveran affiliate) | Q4-27 / Q1-28 | NS/global CSV +2 | S18 |
| Sea1 Peridot / Diamond + 2 | CSV | Sea1 Offshore | 2027–28 | CSV +4 | S22 |
| Skandi Amazonas | AHTS | DOF | CTL May-26 | Brazil AHTS −1 | S18 |
| WSUT (22 PSVs) | PSV | Wilson Sons → Tidewater | Closed ~Sep-26 | Ownership only | S1, S6 |
| CBO | PSV/OSV | → OceanPact (70 vessels) | Closed (CADE) | Ownership only | S1 |
| 9 AHTS arrivals / 3 departures | AHTS | various | Jun–Sep 2026 | NS AHTS supply up (net ~ +6) | S1 |
| Global orderbook | 216 OSVs | — | Q4-25 | ~4% of fleet | S5 |

### Vessel-by-vessel availability and cover

- **Built:** Seagems PLSVs (92 / 53 / 17% for 2027 / 28 / 29 after the 2028 round; Jade booked from Jan 2028) and DOFCON PLSVs (~97 / 100 / 92%). Fleet level, 16 named units: ~95 / 73 / 44% `[A]` (Paths section).
- **Not yet built:** NS term fleet, Brazil PSV/AHTS/RSV, CSV (checkpoint 10). DOF's AHTS table (Q3 report) gives end dates for 11 AHTS beyond mid-2029 (Hera Q4-30; Vega Q3-29; Mover Q3-30; Iguaçu, Angra, Urca, Paraty, Fluminense Q4-30; Botafogo Q2-29; Lifter, Logger Q1-30) and "very strong" 2027–28 cover; the 2027–28 bars are not readable as text.

### North Sea spot history (Seabrokers, GBP/day; annual = mean of monthly averages)

| Year | Large PSV (> 900 m²) | Large AHTS (> 22k bhp) | Seabrokers own annual (PSV / AHTS) |
|---|---|---|---|
| 2020 | 5,838 | 16,687 | — |
| 2021 | 9,413 | 20,379 | — |
| 2022 | 13,227 | 38,170 | — |
| 2023 | 15,947 | 35,612 | 13,696 / 36,320 |
| 2024 | 12,346 | 39,691 | 11,570 / 39,956 |
| 2025 | 10,691 | 49,820 | 9,567 / 44,526 |
| 2026 Jan–Sep | 17,326 | 113,614 | 15,637 / 114,945 (YTD) |
| **2026 Jan–Oct** (4 Nov) | **17,546** | **106,632** | 15,954 / 106,574 (YTD) |

Monthly 2026, large PSV: 5,691 · 12,221 · 13,625 · 25,392 · 20,040 · 19,970 · 15,278 · 21,445 · 22,275 · **19,519 (Oct)**.
Monthly 2026, large AHTS: 90,283 · 127,966 · 91,116 · 117,150 · 131,234 · 155,875 · 102,188 · 96,015 · 110,702 · **43,794 (Oct)**.
Spot utilisation 2026 (Jan–Sep), large PSV: 61 · 76 · 67 · 89 · 68 · 65 · 62 · 79 · 79%; large AHTS: 57 · 69 · 37 · 63 · 53 · 80 · 55 · 73 · 61%.
4 Nov (October report): large PSV Oct **82%** (Sep restated 79 → 80%); large AHTS Oct **42%**. Medium PSV Oct £17,355 at 78%; medium AHTS Oct £41,455 at 34%. Monthly 2025 Nov–Dec (for the stub cross-check): large PSV 7,964 · 7,775; large AHTS 80,726 · 98,383.

### Sources

| ID | Source | Content | Definition / universe | Observed / published |
|---|---|---|---|---|
| S1 | Seabrokers *Seabreeze* Monthly Market Report, September 2026 (PDF via seabrokers.no/chartering/seabreeze) | NS average spot rates, utilisation, arrivals/departures, fixtures, S&P, newbuilds | North Sea spot market; Seabrokers classes; arrivals/departures exclude term/layup | Sep 2026 / early Oct 2026 |
| S2 | Seabrokers *Seabreeze* March 2026, Dec 2025, Dec 2024, Nov–Dec 2023, Dec 2021 (PDFs) | Monthly spot averages 2020–2025, utilisation, own annual averages | Same | 2021–2026 |
| S3 | SSY Offshore Spot Market Update, 22 Feb 2026 (PDF) | Norway (NOK) vs UK (GBP) PSV spot | Broker fixture lists (samples) | 22 Feb 2026 |
| S4 | Tidewater Q2 2026 results release (PDF) and earnings call | Day rates, utilization, opex by region and class; guidance | Company fleet, blended regions | Q2-26 / 3–4 Aug 2026 |
| S5 | Westwood Insight (10 Mar 2026; 21 May 2026) | Global OSV fleet, laid-up, orderbook, utilization; ROVSV/pipelay utilization | Westwood MarineLogix | Q4-25 / Mar–May 2026 |
| S6 | Tidewater 8-K exhibit (SEC), 22 Feb 2026 | WSUT acquisition | Company | Feb 2026 |
| S7 | Riviera (OSJ, Arctic Offshore, 25 Mar 2026); Rystad; Spinergie | Brazil OSV count, FPSO vessel needs, PSV demand, utilization | Broker/analyst `[E]` | 2025–2026 |
| S8 | Paratus Energy Services: Q2 2026 results (11 Sep 2026); tender update (18 Sep 2026) | Seagems (Paratus reports a **50% share**; restated to 100% this run), PLSV 2028 tender | Company | Sep 2026 |
| S9 | World Oil (11 May 2026); Baird/Nasdaq (Skandi Commander) | DOF RSV newbuilds and Skandi Commander | Company announcements | 2025–2026 |
| S10 | World Oil / DOF (21 May 2025) | 4 large AHTS, 4 yrs, ~$480m | Company | May 2025 |
| S11 | InfoMoney (23 Jan 2025) | Petrobras RSV tender bids | Tender result (bids) | Jan 2025 |
| S12 | Shipping Telegraph / OE Digital / Riviera (Solstad CSV awards) | Petrobras CSV contracts; 3-CSV package | Company | Dec 2025–2026 |
| S13 | GlobeNewswire (Subsea7, 1 Jun 2024) | 4 PLSV contracts > $1.25bn | Company | Jun 2024 |
| S14 | Offshore Magazine (3 May 2025); SINAVAL | Petrobras 18-PSV tender, PSV 4500 reference rate | Tender documents via press | Apr–May 2025 |
| S15 | Agência Petrobras / InfoMoney / Eixos (12 Dec 2024) / Seabreeze | 12 hybrid newbuild PSVs, R$16.5bn, 12-yr contracts | Petrobras | Dec 2024–2026 |
| S16 | Westhon news page | Petrobras AHTS tender results | Undated `[?]` | `[?]` |
| S17 | Seatrade/energy-pedia (snippets) | Solstad Normand Vibran/Trym | Company | 2024–25 `[?]` |
| S18 | DOF Group releases (30 Jul 2026) and Q2 2026 summaries | PSV sales, SALT 310 CSVs, Skandi Amazonas CTL | Company | Jul–Aug 2026 |
| S19 | Riviera (31 Mar 2026; Jun–Jul 2026 rate articles incl. Hagland Norway averages) | NS AHTS NOK rates, peaks, Rosebank hook-up | Broker-based press `[E]` | Mar–Aug 2026 |
| S20 | Search snippets (Bower/Remøy news, broker commentary) | Polaryssel NOK 233k; Kongsborg NOK 230–240k | Secondary, grade C | 2025–2026 |
| S21 | Baird Maritime (Eidesvik Q2 2026) | Aker BP 4-yr frame; Viking Prince 3 yrs | Company | Aug 2026 |
| S22 | Baird Maritime (Sea1 Offshore Q2 2026) | Segment utilization, newbuild CSVs | Company | Aug 2026 |
| S23 | OE Digital (subsea vessel outlook 2026) | CSV rates, ~30 newbuild CSVs | Analyst `[E]` | 30 Dec 2025 (dated in the second run; see S36) |
| S36 | [OE Digital — "Subsea Vessel Market Outlook 'Robust' for 2026" (J. Skjong, Fearnley Offshore Supply)](https://www.oedigital.com/news/533915-subsea-vessel-market-outlook-robust-for-2026) | ~30 firm 150/250 t AHC CSV newbuilds, > 20% of the active fleet, mostly China, almost all speculative; H1-25 rates 150 t > $60k, 250 t > $80k; fixtures ~4× spread | Broker `[E]` | 30 Dec 2025 |
| S37 | [Riviera — "Speculative ordering behind record CSV deliveries" (Fearnleys)](https://www.rivieramm.com/news-content-hub/news-content-hub/speculative-ordering-behind-record-csv-deliveries-86209) | > 25 CSVs (150–250 t), deliveries H2-26 to 2028, 2027 a likely record; Salt 150 t series, DEME OCV 2028, Purus Salt 311 × 2; softening demand | Broker `[E]` | 2 Oct 2025 |
| S38 | [Offshore Engineer — "Why don't OSVs get scrapped?" (MSI)](https://www.oedigital.com/news/485621-market-why-don-t-osvs-get-scrapped) | Northern Europe vessels > 15 years struggle for work; scrap value ~$0.5m per OSV; operator age caps ADNOC 20, ONGC 21, Aramco 23 | Analyst `[E]` | 1 Mar 2021 (old; structural) |
| S39 | Search summaries: Solstad (Normand Navigator LOI, Feb 2026; Normand Maximus LOI, May 2026), Subsea7 (Normand Subsea; Seven Viking), Petronas age cap 20 years (Edge Malaysia, Dec 2022), Paratus extended dry-docking (briefglance, 2026) | Fixture search (no rates disclosed); age caps; PLSV docking | Company / press `[E]`, grade C | 2022–2026 |
| S24 | AllRatesToday `get_rates_authenticated` | GBP/USD, GBP/NOK, GBP/BRL at 10 Oct 11:40 UTC, 2 Oct 05:59 UTC, 10 Sep 10:59 UTC, 5 Oct 05:37 UTC; USD/BRL 20 Dec 2024 | Mid-market | 5–10 Oct 2026 |
| S25 | Pulse2 / 2020 Bulkers LOI | 15 large AHTS, $406m; "~40% discount to newbuild parity" | Company `[E]` for the parity claim | Sep 2026 |
| S26 | Oilnow.gy / OGJ / Guyana DPI | Errea Wittu arrival 21 Aug, first oil Q4 guided; ExxonMobil vessel RFIs | Press / government | 2026 |
| S27 | `docs/oil-market-bbb.md` (10 Oct), `docs/rig-market-bbb.md` (10 Oct) | Oil and rig inputs | Workspace baselines | 10 Oct 2026 |
| S28 | **Newsweb backend via the Edge connection** (api3.oslo.oslobors.no newsreader): SOFF/SOMA 6 Oct (683645/6); GEOS 2 Oct (683466) and 10 Sep (681967); EIOF 7 Oct (683713); DOFG 2 Oct (683479); AKAST 2 Oct (683483); SOMA 30 Sep (683290); SOFF 7 May (Normand Maximus LOI) | Primary owner releases | Exchange releases `[F]` | 7 May – 7 Oct 2026 |
| S29 | Nordnet news item c71330e0… (user input, read via Edge) | Copy of the SOFF Normand Maximus release | Secondary copy of S28 | 6 Oct 2026 |
| S30 | Yahoo `get_chart` PBR | Petrobras ADR closes 28 Sep – 9 Oct 2026 | NYSE, USD | 9 Oct 2026 |
| S31 | MercoPress, Euronews, LBC (5 Oct 2026) | Brazil first-round result | Press (TSE counts) | 5 Oct 2026 |
| S32 | Lefosse newsletters (24 Aug, 14 Sep 2026) | Petrobras opportunities: PSV 3000 bareboat; P-91 FPSO deadline | Law-firm digest of Petrobras notices | Aug–Sep 2026 |
| S33 | OE Digital (6 Oct 2026), Offshore Source (7 Oct 2026) | Normand Maximus specs and option | Press | Oct 2026 |
| S34 | Placera (Akastor, 4 Jun 2026); Riviera (28 Apr 2026); TradeWinds snippet | DDW sales of Skandi Atlantic, Emerald, Peregrino; Peregrino 2010, 16,315 bhp | Company / press | 2026 |
| S35 | `docs/PLSV-analysis.md` (Paratus Q2-26 deck at 100%, vessel table, 2024 tender) and `docs/DOF-analysis.md` (DOF CMD 15 Sep 2026: Brazil contracts, DOFCON, broker values, Petrobras AHTS tender cancellation) | Company figures compiled by the IAF analyses | Company `[F]`/`[B]` as tagged there | 5 Oct 2026 |
| S40 | **Newsweb backend via the Edge connection**, sweep 9–17 Oct 2026: HAVI 16 Oct (684238), EIOF 16 Oct (684224), DOFG 14 Oct (684066) and 12 Oct (683962); also screened ODL 16 Oct (684219, rig), AKRBP/VAR/DNO Q3 trading updates (titles only), SOMA financial calendar | Primary owner releases | Exchange releases `[F]` | 12–16 Oct 2026 |
| S41 | [Offshore Energy — REM Ocean arrives in Norway (16 Oct 2026)](https://www.offshore-energy.biz/2026/10/16/methanol-ready-energy-subsea-construction-vessel-arrives-in-norway-for-completion); [Offshore Energy — DOF decommissioning (13 Oct 2026)](https://www.offshore-energy.biz/2026/10/13/north-sea-operator-appoints-dof-for-subsea-decommissioning) | CSV newbuild status; DOF award (copy of S40) | Press | 13–16 Oct 2026 |
| S42 | [Transporte Moderno (22 Sep 2026)](https://transportemoderno.com.br/2026/09/22/navio-hibrido-abre-renovacao-da-frota-offshore-da-petrobras/) | Starnav Elektra (first PSV of the 12); Starnav BNDES financing (4 PSV + 4 OSRV, 5,500 dwt); Petrobras plan for 40 new support vessels by 2030 (12 PSV, 10 OSRV, 16 RSV, 2 AHTS; US$2bn); "48 contracted by end-2026, 96 in 2027 incl. barges and tugs" (CEO via BNDES) | Press `[E]`; the counts do not reconcile (40 vs 48), so the figures are context only | 22 Sep 2026 |
| S43 | Search summaries: Petrobras director R. Baruzzi at ROG.e 2026 on PN 2027–31; PN 2026–30 approved 27 Nov 2025; Datafolha/Quaest/BTG runoff polls (Sep 2026) | Petrobras plan timing; runoff polling | Press `[E]`, grade C | Sep 2026 |
| S44 | AllRatesToday `get_rates_authenticated` | GBP/USD 1.33265, GBP/NOK 12.5557, GBP/BRL 6.74794 | Mid-market | 17 Oct 2026 14:03 UTC |
| S45 | `docs/oil-market-bbb.md` (17 Oct), `docs/rig-market-bbb.md` (10 Oct with 13 and 17 Oct small updates) | Oil and rig inputs | Workspace baselines | 17 Oct 2026 |
| S46 | [TSE — Presidente do TSE anuncia reeleição de Lula (Oct 2026)](https://www.tse.jus.br/comunicacao/noticias/2026/Outubro/presidente-do-tse-anuncia-reeleicao-de-lula-e-faz-balanco-do-2o-turno-das-eleicoes-2026); [CNBC — Lula wins historic fourth term (26 Oct)](https://www.cnbc.com/2026/10/26/brazil-lula-win-presidential-election-runoff-vote.html); ITV (4 Oct) for the 5 Jan start of the term | Runoff result: Lula 64,256,232 votes (51.79%), F. Bolsonaro 59,826,041 (48.21%); turnout 128.2m of 158m | Electoral court `[F]`; press `[E]` | 25–26 Oct 2026 |
| S47 | [InfoMoney/Reuters — CEO da Petrobras vê queda das ações após vitória de Lula como especulativa (26 Oct)](https://www.infomoney.com.br/mercados/ceo-da-petrobras-petr4-ve-queda-das-acoes-apos-vitoria-de-lula-como-especulativa/); [CNN Brasil, same Reuters item](https://www.cnnbrasil.com.br/economia/money/negocios/ceo-da-petrobras-ve-queda-das-acoes-apos-vitoria-de-lula-como-especulativa/) | Chambriard statement; B3 PETR −~10%; Ibovespa circuit breaker | Press (Reuters) `[E]`; statement, not a measure | 26 Oct 2026 |
| S48 | Forbes Brasil "O que Lula quer manter e mudar na economia em um novo mandato" (Oct 2026; 403, search summary only); Eixos / Chambriard on the next plan (diesel self-sufficiency, Sep 2026) | Programme keeps local content in Petrobras contracting; 44 of 48 ships contracted at Brazilian yards (Chambriard) | Press `[E]`, grade C (summary only) | Sep–Oct 2026 |
| S49 | [BM&C News — Petrobras prepara Plano de Negócios 2027-2031 (23 Oct)](https://bmcnews.com.br/empresas-e-negocios/petrobras-prepara-plano-de-negocios-2027-2031-para-novo-ciclo-quinquenal/) | Board round 23 Oct, "não representa a aprovação definitiva"; no date, no figures; PN 2026–30 stays the reference | Press `[E]` | 23 Oct 2026 |
| S50 | Yahoo `get_chart` PBR and BRL=X | PBR closes: 23 Oct 26.16, 26 Oct 22.50, 27 Oct 22.30; USD/BRL 23 Oct 5.050, 27 Oct 5.373, 28 Oct 5.351 (the 26 Oct daily close of 4.96 is inconsistent with the 5.46 high; not used) | NYSE USD; FX mid | 23–28 Oct 2026 |
| S51 | [Baird Maritime — DOF sells Skandi Implementer](https://www.bairdmaritime.com/offshore/exploration-development/offshore-construction/dof-sells-skandi-implementer-vessel) and OE Digital (23 Oct); [World Oil — DOF wins deepwater subsea installation contract in Africa (22 Oct)](https://www.worldoil.com/news/2026/10/22/dof-wins-deepwater-subsea-installation-contract-in-africa); [Baird Maritime — Union Vega orders hybrid PSVs (19 Oct)](https://www.bairdmaritime.com/offshore/vessels-rigs/psvs/union-vega-orders-hybrid-vessels) | DOF vessel sale and Africa award; PSV newbuild order | Press copies of company releases `[F]` | 19–23 Oct 2026 |
| S52 | `docs/oil-market-bbb.md` (24 Oct); `docs/rig-market-bbb.md` (10 Oct with 22, 24 and 28 Oct small updates) | Oil and rig inputs read 28 Oct; nothing taken | Workspace baselines | 24–28 Oct 2026 |
| S53 | Seabrokers *Seabreeze* Monthly Market Report, **October 2026** (PDF via seabrokers.no/chartering/seabreeze; `pdftotext -raw/-table`) | NS average spot rates and utilisation (Oct), arrivals/departures, term fixtures (Ross/Harbour, Equinor, EnQuest, Peterson, NEO NEXT+), Siem Opal, Petrobras PSV 4500/3000 tenders, Morpho, S&P (Bourbon auctions), newbuilds, rigs (Barents not mentioned; Beacon Pacific/Serica) | North Sea spot market; Seabrokers classes; arrivals/departures exclude term/layup | Oct 2026 / early Nov 2026 |
| S54 | alertalicitacao.com.br copies of DOU notices **7004675762** (PSV 4500, lots A–E) and **7004654576** (PSV 3000, lots A–B), Petronect | "At least one vessel" per lot; republished after a change to the edital; proposals open 17 Nov 2026 12:00. Term and start from S53 | Third-party copy of the official notice `[F]`; vessel count per lot `[?]` | Undated republication / read 4 Nov 2026 |
| S55 | StockTitan copy of the Tidewater release "Tidewater Announces Earnings Release and Conference Call" | Q3-26 results 9 Nov 2026 after the close; call 10 Nov 8:00 CT | Company `[F]` | 3 Nov 2026 |
| S56 | Nordic Financial `search_filings` (source newsweb, 2026): CMMB/Oceanity 30 Oct (FOSRV Purity, 4-year Petrobras); DOFG, GEOS, EQNR releases to 4 Nov (no Equinor AHTS award) | Owner releases | Exchange releases `[F]` | to 4 Nov 2026 |
| S57 | `docs/oil-market-bbb.md` (31 Oct, update 4 Nov); `docs/rig-market-bbb.md` (10 Oct with the 4 Nov small update) | Oil and rig inputs read 4 Nov; Barents note assessed; nothing else taken | Workspace baselines | 31 Oct – 4 Nov 2026 |
| S58 | Fearnley Securities note via Infront TDN (user input, 9–10 Nov 2026); Petrobras' own publication not seen | PLSV 2028 round final results: Skandi Buzios $305k, Skandi Recife and Olinda $295k, Sapura Jade $309k; 4 years from 1 Jan 2028; negotiated down 10–15% from first published levels; signatures remain | Broker note `[E]`, grade C; partly corroborated by S59 | 9 Nov 2026 |
| S59 | [DOF Group ASA, Q3 2026 Financial Report (PDF)](https://cdn.prod.website-files.com/629f1b36bee3b058907852a0/6af558ea5b8d71d3def35728_DOF%20Group%20ASA%20Financial%20Report%20Q3%202026.pdf) and the dof.com release | Utilisation 86% (87%); backlog $7.0bn incl. additions; PLSV qualification (> $500m backlog addition, subject to award); AHTS capacity table; contract list since Q3; Shipowning EBITDA +26% on better terms and spot; outlook "supportive"; broker FMV $4,081m (57 vessels, 30 Jun) | Company `[F]` (management reporting, DOFCON at 50%) | Q3-26 / dated 11 Nov, published 12 Nov 2026 |
| S60 | Nordic Financial `search_filings` (source newsweb): DOFG 9 Nov (Skandi Mariner), 11 Nov (7-year small CSV; Skandi Constructor), 30 Jul (two AHTS > 1 year from Q1-27), 3 Jul (Skandi Vega to Q3 2029); Paratus Q2-26 report (28 Aug: EDD up to 20 years for five 550 t Panama-flagged PLSVs); GEOS Q4-25 report (26 Mar 2026: Energy Partner $27.25m, Energy Passion $28m, Energy Empress $30m) and H1-26 report | Owner releases and reports | Exchange releases `[F]` | Jul–Nov 2026 |
| S61 | Tidewater 8-K, Exhibit 99.1 (9 Nov 2026), via FinancialFilings (filing 76076473) | Q3-26 day rates, utilisation, available days and vessel opex by region and class; leading-edge $27,373; 2026 and 2027 guidance; WSUT closed | Company `[F]`; regional averages blend classes and contract types | Q3-26 / 9 Nov 2026 |
| S62 | [Inderes copy of Solstad Maritime Q3 2026 release](https://www.inderes.fi/releases/solstad-maritime-asa-presentation-of-third-quarter-2026-results) (4 Nov); [Baird Maritime on Solstad Offshore Q3 2026](https://www.bairdmaritime.com/offshore/offshore-support-maintenance/solstad-offshore-earnings-saipem-contract) (4 Nov); Nordic Financial: SOFF Q2-26 release (15 Jul; newbuild CSV H1-2029) | SOMA record adjusted EBITDA $117m driven by the NS AHTS spot/project fleet; SOFF utilisation 92%, Normand Tonjer sold, Normand Maximus firm with Saipem Mar 2027–May 2029 | Company `[F]` via copies; segment utilisation not read `[?]` | 15 Jul – 4 Nov 2026 |
| S63 | Vessel specs: OilfieldTechnology (20 Apr 2017: Skandi Búzios delivered, sister of Skandi Açu, 650 t), Vard references and OilfieldTechnology (19 Feb 2019) for Skandi Recife (340 t Huisman system) and Skandi Olinda (300 t contracted) | PLSV lay-system classes for the comparability test | Press/yard `[E]`; contracted vs design capacity may differ | 2017–2019 |
| S64 | AllRatesToday `get_rates_authenticated` | GBP/USD 1.32675, GBP/NOK 12.6808, GBP/BRL 7.41381 | Mid-market | 12 Nov 2026 07:48 UTC |
| S65 | `docs/oil-market-bbb.md` (11 Nov 2026); `docs/rig-market-bbb.md` (12 Nov 2026) | Oil and rig inputs (downstream rows for supply; Hercules, Beacon Pacific, DS-18, Brazil counts) | Workspace baselines | 11–12 Nov 2026 |
| S66 | Search summaries (Safras; Nord Investimentos) on PN 2026–30 | Petrobras plans with Brent $70 for 2027–30; capex $109bn | Press `[E]`, grade C | Nov 2025 (PN 2026–30) |

**Assessed and rejected / limited:**
- **12 Nov full update:**
  - **PLSV round (user input):** used as `[E]`, grade C. DOF's Q3 report corroborates the three DOFCON qualifications, the Jan 2028 start and a backlog addition consistent with the rates, but not the rates themselves. The lot-5 rate is not in the input.
  - **Tidewater Q3:** an aggregator page (Panabee) gave the same headline figures with internal inconsistencies (13% vs 12.5%; a 226-vessel fleet). It is rejected in favour of the 8-K tables. Q3-2025 Tidewater items surfaced again and were rejected as the wrong year.
  - **November North Sea spot:** no public source found (Seabrokers still shows October; Riviera, Baird and SSY gave nothing dated November). The stubs keep the Base winter estimate for Nov–Dec.
  - **Skandi Mariner spec** (2017, Salt 200, 95 m, from an OE Digital page tagged "Europe"): unverified, and the region is not stated. The value is used as a D-grade range only.
  - **Equinor AHTS tender:** web results were 2019–2022 Solstad/Equinor items. Nothing from Nov 2026 was found.
  - **Solstad Q3 segment utilisation:** a Quartr summary gave Q2 AHTS utilisation (63% → 88%) but no Q3 figure. Not used.
- **4 Nov small update:**
  - Equinor AHTS tender: web results returned only 2018–2024 Equinor AHTS awards (Skandi Iceman, Skandi Vega, Normand Ferking) and the Skandi Vega option (Jul 2026). None is the 3 Nov tender. offshoreindustry.co.uk was rejected again.
  - Brasil Energia "Petrobras deve contratar sete novos PSVs 4500" returned 403 (undated). Not used for facts; whether its seven PSV 4500s relate to the five-lot tender is `[?]`.
  - Tidewater Q3 2025 figures surfaced in Q3 2026 searches and were rejected as the wrong year.
- **28 Oct small update:**
  - Press figures for the PBR fall vary (−10% to −21.7%, mixing B3, premarket and intraday). The NYSE close-to-close of −14.0% (Yahoo) is used.
  - Benzinga, GuruFocus and Forbes Brasil returned 403, so only search summaries were seen, and they are not used for facts. Energy Intelligence covers the share move only.
  - "Lula chama presidente da Petrobras de 'magnata do petróleo'" is a related-link headline only, undated. Not used (checkpoint 17).
  - No Lefosse Petrobras-opportunity newsletter for October was found (404). The October Petrobras OSV tender status rests on search.
- **17 Oct run:**
  - Eixos "Petrobras contrata dez barcos de apoio" is from **9 Oct 2024** (8 RSV + 2 AHTS, 40% local content, operations 2029–30). Old; already in the RSV/AHTS programme.
  - Offshore Industry (offshoreindustry.co.uk) 2026 OSV pages: rejected again (no traceable source; its rate ranges contradict the broker series).
  - An Offshore Energy item, "€5.6 million … PSV … 319 days … off UK": the page did not render and the item could not be dated. Not used.
  - Tidewater Q3 date: not yet announced (Q2 was announced 28 Jul for 3 Aug).
  - Errea Wittu first oil: no confirmation found after the August arrival. Still "guided Q4".
- **Nordnet link (user input):** a copy of the Newsweb release (S28). Used for the ownership change and as an asset reference. Rejected as a market valuation: the strike was fixed in 2022 and the deal is intra-group.
- **Eixos "Petrobras contrata embarcações…":** from 12 Dec 2024. Old news (12 PSVs; Oct-2024 RSV/AHTS round). Not a new event.
- **Brasil Energia "afretar até 33 embarcações"** (20 PSV, 12 OSRV, 1 AHTS; bids 10 Oct): paywalled and undated. Not used (checkpoint 8).
- **"Petrobras +13.7%" (ratings-service alert):** verified with Yahoo as +11.5% on 5 Oct and +16.9% on the week.
- **offshoreindustry.co.uk:** rejected (no traceable source). **Oceana 2013 AHTS bids:** rejected as stale. **Riviera July 2025 article:** history only. **Hagland spot list:** not read (dynamic). **SSY weekly** after Feb 2026: not available.
- **Brasil Energia, Seatrade, Marinelog, BNamericas, Splash247:** 403; search snippets only (grade C).
