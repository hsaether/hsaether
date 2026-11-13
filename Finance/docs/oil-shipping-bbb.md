# Oil Shipping BBB — 13 November 2026

**Status: Final** (update run) · skill `oil-shipping-bbb` revision **2026-10-24.1** · as of **13 Nov 2026** (market data to 6–12 Nov) · **stale after 4 Dec 2026**

## Interface (values other documents read)

As of 13 Nov 2026. Spot TCE in $k/day, market segment average (modern eco, non-scrubber), period average; asset values in $m. Ranges in the sections below.

| Item | Stub Q4-26 (all scenarios) | 2027 Bear / Base / Bull | 2028 | 2029 | Mid-cycle | Values $m: now NB / 5-yr / 10-yr · 5-yr mid-cycle Bear / Base / Bull · NB mid-cycle Base |
|---|---|---|---|---|---|---|
| VLCC | **630** | 70 / 180 / 480 | 26 / 50 / 150 | 24 / 36 / 90 | 36 / 44 / 55 | 131.5 / 210 / 190 · 93 / 121 / 160 · 130 |
| Suezmax | **400** | 50 / 115 / 300 | 27 / 44 / 108 | 25 / 30 / 70 | 27 / 33 / 41 | 90.5 / 130 / 115 · 64 / 84 / 112 · 90 |
| Aframax | **210** | 36 / 65 / 160 | 29 / 38 / 72 | 25 / 35 / 55 | 24 / 30 / 37 | 78 / 90 / 77 · 54 / 75 / 100 · 77 |
| LR2 | **170** | 36 / 65 / 160 | 29 / 38 / 72 | 25 / 35 / 55 | 24 / 30 / 37 | ~80 `[A]` / 90 / 77 · 52 / 73 / 98 · 79 |
| LR1 | 120 | 28 / 45 / 100 | 23 / 30 / 48 | 20 / 28 / 38 | 20 / 25 / 31 | 62.5 / 68 / 48 `[E]` · 42 / 59 / 80 · 61 |
| MR | **62** | 22 / 37 / 58 | 19 / 25 / 33 | 17 / 22 / 27 | 17 / 21 / 26 | 52.5 / 53 / 43 · 32 / 46 / 64 · 51 |
| Base Year-1 quarters 2027 (Q1 / Q2 / Q3 / Q4) | VLCC 400 / 160 / 90 / 70 · Suezmax 230 / 115 / 65 / 50 · Aframax and LR2 114 / 63 / 43 / 40 · LR1 69 / 44 / 33 / 34 · MR 48 / 36 / 31 / 33 | — | — | — | — | — |
| Nov–Dec 2026 market level (open days from mid-Nov) `[A]` | VLCC ~450–520 · Suezmax ~240–250 · Aframax ~140 · LR2 ~125 · LR1 ~100–110 · MR ~56 | — | — | — | — | — |
| Period market (6–11 Nov) | 1-yr TC: VLCC 210–270, Suezmax 155–170 (Amor 15-month 160–180), Aframax 86–100, LR1 67–68.5, MR 39.5–43 · 3-yr: VLCC 125, Suezmax 77.25, Aframax 53.25, LR1 39.5, MR 27.75 | — | — | — | — | — |
| Anchors | Newbuild-parity TCE: VLCC 44, Suezmax 33, Aframax 29, LR2 30, LR1 25, MR 21 · opex floor 8–10.5 | — | — | — | — | — |
| Signpost states | TD3C Q1-27 paper ~$417k (Base signpost < $0.7m met; Bear < $300k not) · VLCC 1-yr > $250k on 2 of 3 sources · USTR/China port fees suspended to 9/10 Jan 2027 · Bab el-Mandeb 6.9 tankers/d · sanctioned-VLCC approvals: none (applications ~50 ships, all types) · Q4 VLCC contracting 2.3% of fleet (trigger 3%) | — | — | — | — | — |

- Bold = stub changed at this run. "Now" asset values re-marked to Xclusiv 9 Nov (+0–6%). 2027–2029, Year-1 quarters, mid-cycle TCE and mid-cycle values are unchanged.
- LR2 = Aframax from 2027 `[A]`. Product rows use labelled Baltic route proxies (see Metadata).

## Metadata

- **Analysis date:** Fri 13 Nov 2026. Previous baseline 24 Oct 2026 (20 days). Window: stub Q4-26 + 2027–2029 (no roll).
- **Why this run:** the USTR/China port-fee deadline (9–10 Nov) passed; open watch item CAPT *Amor* 15-month TC (6 Nov). During the run the skill's own **Year-1 FFA trigger fired** (TD3C Q1-27 paper −52%, TD20 Q1-27 −28%); it is tested in the Market check.
- **Oil Market BBB used:** baseline **11 Nov 2026, Final** (Interface and "For downstream skills" read). Base Brent 2027 84; disruption status unchanged (contested, no deal). It flags nothing for shipping. Not stale (stale after 30 Nov).
- **Latest inputs:**
  - BWET holdings (13 Nov; prices ~12 Nov).
  - Fearnleys week 46 (11 Nov).
  - Compass 9 Nov.
  - Xclusiv 9 Nov (data to 6 Nov), 2 Nov and 26 Oct.
  - Intermodal weeks 44 and 45 (data to 30 Oct and 6 Nov).
  - Baltic tanker roundup week 45 (6 Nov).
  - Gibson weekly 6 Nov (spot and Q4 FFA to 5 Nov).
  - IMF PortWatch to 8 Nov.
- **Not available at writing:** Gibson 13 Nov, Baltic week 46 and Xclusiv 16 Nov. The ~11 Nov segment levels are therefore estimated from Fearnleys route WS and the Baltic 6 Nov TCEs `[A]`.
- **Oldest inputs:** McQuilling orderbook by segment (Feb; shape only, stale); Allied fleet counts (Jul); Frontline orderbook in vessels (11 Aug; stale for a count).
- **Series (skill Benchmarks), unchanged:**
  - Spot TCE = Xclusiv "average T/CE" for VLCC, Suezmax and Aframax. The Xclusiv VLCC average is the simple mean of its MEG–China, WAF–China and USG–China routes (checked 30 Oct and 6 Nov).
  - Products use labelled proxies: LR2 = ~60% dirty at the Aframax mark + ~40% clean (TC1/TC15); LR1 = TC5 × ~0.6; MR = Atlantic/Pacific baskets and TC7/TC18 paper.
  - Period rates: Intermodal (primary; table rebuilt row by row), Fearnleys and Compass (cross-checks). Asset values: Xclusiv.
- **Stub method:** October segment average (weekly Xclusiv points 2–30 Oct) + November and December scaled by the paper's own path (BWET monthly contracts, Gibson Q4 FFA). The route-ratio method is a cross-check only.
- Tags: `[F]` fact · `[E]` external forecast or secondary · `[A]` own assumption · `[?]` unknown.

## Conclusion

- **Oil Shipping BBB: stub re-marked; all paths kept.**
  - Stub Q4-26: VLCC 630, Suezmax 400, Aframax 210, LR2 170 and MR 62 move; LR1 120 is kept.
  - Unchanged: 2027–2029 in every scenario, the Year-1 quarters, mid-cycle TCE and mid-cycle values.
  - "Now" asset values re-marked to Xclusiv 9 Nov (+0–6%).
- **USTR/China port fees: status quo, no shipping effect.**
  - USTR suspended its Section 301 port fees and crane duties for two more months (to 23:59 ET on 9 Jan 2027). China extended its suspension of special port fees on US-linked ships, its shipping probe and the Hanwha countermeasures to 10 Jan 2027.
  - No fleet split, routing change or TCE effect. Base never assumed fees. The Bull supply leg "fees return and split the fleet" moves to 10 Jan 2027.
- **The crude market corrected hard after the midterms.**
  - Segment averages, 30 Oct → 6 Nov: VLCC 829 → 731, Suezmax 570 → 340 (−40%), Aframax 303 → 176 (−42%) (Xclusiv; the Baltic confirms).
  - The fall continued to ~11 Nov. TD34 fell to WS411 (≈ $430k) and Fearnleys puts Gulf of Oman VLCC returns at $350–400k.
  - Brokers point to supply length: ballasters, relets, failed fixtures and Suezmax substitution in the Atlantic. Gibson: December paper −27% in the week after the 3 Nov midterms.
- **The Year-1 FFA trigger fired; tested, Base 2027 kept.**
  - The Q1-27 paper fell: TD3C ~$861k → ~$417k (−52%; 120–125 lots a month), TD20 ~$117k → ~$84k (−28%; 45 lots, thin).
  - The 1-yr TC barely moved on the primary series (Intermodal VLCC −10%, Suezmax −6%, Aframax +1%, MR −4%, LR1 +12%). It sits at **99–136% of Base** over the same 12 months in every segment.
  - The skill names the period market the main control on the paths, and it does not confirm the paper. The paper and the period market point in opposite directions, so no path moves.
  - **VLCC Q1-27 (Base 400)** sits 7–80% above the Q1 paper-equivalent (~$220–375k). The range depends on whether the Gulf premium in TD3C persists. **Retest rule:** if the TD3C Q1 paper stays below ~$0.5m and two of three VLCC 1-yr sources fall below $200k by the next run, cut Q1 to ~300 and Base 2027 to ~155 (−14%).
  - **No Base path moved, so none moved by more than the recalibration trigger.**
- **Amor** (CAPT; 2026 dual-fuel Suezmax; 15 months from November at ~$160–180k gross) prices at **120–136% of Base** over the months it runs. It supports Base Suezmax 2027 (115) against the thin TD20 paper.
- **Base, crude tankers:** the crisis structure lasts through H1-27 and unwinds in H2-27. The delivery wave (~290 VLCCs in 2027–29) then sets 2028–29, with 2029 the trough. **VLCC 180 → 50 → 36** (mid-cycle 44); **Suezmax 115 → 44 → 30** (mid-cycle 33).
- **Base, product tankers:** rates rest on tonnage (clean LR2 participation low); Gulf product loadings recover (~3 mb/d in October, Vortexa via oil BBB). The 2028–29 delivery peak and LR2s returning to clean trade bring rates to near parity. **LR2 65 → 38 → 35; LR1 45 → 30 → 28; MR 37 → 25 → 22.** LR1 is flagged upward: its period market sits at 133–136% of Base.
- **Main Bear catalyst (closer, not triggered):**
  - An Iran–USA deal plus recession. Strikes have been on hold since 9 Nov; the Democrats won both chambers on 3 Nov (new Congress 3 Jan); Iran denies talks.
  - Supply leg: Trafigura, Vitol, Mercuria and ADNOC have applied for US licences on ~50 sanctioned ships (none granted).
- **Main Bull catalyst (further away, tail live):**
  - US strikes before 3 Jan with retaliation against Gulf export infrastructure, or suspension of the Gulf of Oman STS hub. Attacks continue (37 ships in October; a tanker hit on 10 Nov), and the Houthis struck Riyadh on 8 Nov.
  - Port fees return on 10 Jan 2027.

## Stub Q4-26

Identical in all scenarios: October actual (Xclusiv weekly points) + November–December scaled by the paper. Weights 31 / 30 / 31 days.

- **VLCC 630** (range 590–690):
  - **October 839:** 786.2 / 936.6 / 883.4 / 761.4 / 829.4 (2–30 Oct) `[F]`.
  - **November ~595:**
    - 31 Oct–6 Nov ~780 (829 → 731.5 `[F]`); 7–13 Nov ~620; rest ~520.
    - ~11 Nov segment ≈ 565 `[A]`: MEG–China ~1.07m, WAF–China ~350k and USG–China ~275k (Fearnleys WS 11 Nov, Baltic TD22 $41.67m on 10 Nov, scaled to the Xclusiv route basis).
    - Rest of November = 0.92 × the current segment: the BWET TD3C November contract ($204.1/t ≈ $1.09m) less the ~$1.22m fixed so far, against TD3C now ~$1.07m.
  - **December ~447:** BWET TD3C December $161.7/t ≈ $0.86m, i.e. 0.79 × TD3C now.
  - **Q4 = 627 → 630.** The move is −10%, at the minimum change. The direction is confirmed: Fearnleys on 11 Nov reports "another downward rate correction".
  - **Cross-checks:**
    - BWET Q4 TD3C ≈ $1.11m × segment/TD3C 0.52–0.57 = 575–630.
    - Gibson Q4 FFA ($1,177k, 5 Nov) × 0.57 = 671.
- **Suezmax 400** (range 370–460):
  - **October 646:** 619.9 / 699.9 / 700.1 / 638.4 / 570.1 `[F]`.
  - **November ~295:** 6 Nov 339.8 `[F]`; ~11 Nov ~240 `[A]` (TD20 WS430 → WS300, TD6 below WS450, MEG "pile up").
  - **December ~250:** BWET TD20 Nov / Dec $65.5 / $60.3 per t ≈ $181k / $161k, about flat to TD20 spot (~$150–157k).
  - **Q4 = 398 → 400.**
  - **Cross-check:** TD20 Q4 paper ($283k BWET; $297k Gibson) × segment/TD20 1.37–1.64 = 388–487. The stub sits at the low end because the Atlantic led the fall.
- **Aframax 210** (range 190–260):
  - **October 326:** 276.9 / 384.7 / 328.3 / 336.1 / 303.1 `[F]`.
  - **November ~165:** 6 Nov 175.5 `[F]`; ~11 Nov ~143 `[A]` (Fearnleys UK/Cont WS250, Euromed WS270, Caribs/USG WS285; Kuwait–Singapore and Asia firmer).
  - **December ~140:** the TD25 Q4 paper ($155.25k, Gibson 5 Nov) implies Nov–Dec ≈ 0.95 × TD25 spot.
  - **Q4 = 211 → 210.**
  - **Cross-check:** TD25 Q4 × segment/TD25 1.65–2.1 = 257–328. Not used: TD25 has diverged from its segment.
- **LR2 170** `[A]` (range 150–195):
  - Dirty ~60% × 210 = 126.
  - Clean ~40% = 44.6: the 24 Oct clean component scaled by the Q4 TC1/TC15 average (−11%). Baltic 6 Nov: TC1 $292k, TC20 $297k, TC15 $79k.
  - Total 170.6 → 170.
- **LR1 kept at 120:** TC5 Q4 FFA $184.75k (Gibson 5 Nov) × ~0.6 = 111 (−7.6%, below the minimum change). Spot is still firm: TC5 $212k (Baltic) / $227k (Gibson); TC8 $224k.
- **MR 62** (range 55–70):
  - October ~73.5 (Atlantic basket ~68, Pacific basket ~79).
  - Nov–Dec ~56: TC7 Q4 FFA $70.0k and TC18 $51.0k (Gibson 5 Nov), net of their October averages.
  - Q4 ≈ 62 (+13%). The 6 Nov Atlantic basket was $72.0k (Baltic) and Pacific $85.5k (Xclusiv).
- **Confidence:** medium for VLCC and Suezmax (the ~11 Nov level is estimated); low for Aframax and products.

## Scenario definitions

| Scenario | Weight (convention) | Oil BBB scenario used | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|
| **Bear** | 25% | Oil Bear, **demand variant** (Iran–USA deal + recession) | **Demand:** a deal lifts the blockade; shuttles, STS and Cape routing end; the Red Sea reopens; recession cuts cargoes. **Supply:** deliveries on time; Iranian shadow VLCCs return; attacked ships come back from repair; a wide US licence programme returns sanctioned VLCCs to compliant trade even without a deal | Ton-days fall faster than volumes recover. The delivery wave meets slack demand; rates below newbuild parity in 2028–29 | Q1 2027 (licences: any time) | Ceasefire > 60 days · STS/shuttle share < 2% of the VLCC fleet · STS time < 7 days · Bab el-Mandeb tankers > 18/d · VLCC 1-yr TC < $90k · TD3C Q1-27 FFA < $300k/d · PMIs < 48 · **> 30 sanctioned VLCCs approved for mainstream trade** |
| **Base** | 50% | Oil Base (armed normalisation; no deal; Gulf and Gulf of Oman contested) | ME oil reaches market via East–West/Yanbu and escorted shuttles with STS; episodic attacks; no deal. ME output outside Iran back to pre-war by mid-2027 (EIA via oil BBB); Gulf products repaired through 2027; ~1 bn bbl restocking. US licences for sanctioned tankers stay small (< 30 VLCCs) | Shuttle and STS inefficiency (+6% VLCCs per mb/d on MEG–Far East; ~10-day STS) and attack downtime last through H1-27 and ease in H2-27. US→Asia long-haul capped by freight and a narrower Brent–WTI. Restocking (~3–4% of the VLCC fleet a year) partly absorbs ~290 VLCC deliveries in 2027–29 | Ongoing | VLCC 1-yr TC below $150k by Q2-27 · TD3C Q1-27 FFA below $0.7m by end-Dec (met) · STS time back to 5–7 days · Bab el-Mandeb tankers 8–15/d · VLCC exits ≥ 10 in 2028 and ≥ 25 in 2029 · LR2 dirty share < 50% during 2027 · sanctioned VLCCs approved < 30 |
| **Bull** | 25% | Oil Bull (US strikes before 3 Jan; retaliation against Saudi/Gulf export infrastructure; escort/STS system fails) | **Demand:** the escort and shuttle system fails (Sohar/Fujairah STS hub suspended); Gulf barrels replaced by Atlantic long-haul; cargo splitting and STS persist. **Supply:** attacked tankers idle ~2 months each; yard slippage; **USTR/China port fees return on 10 Jan 2027** and split the fleet | Ton-days rise while volumes fall, as in Mar–Oct 2026. Inefficiency absorbs the delivery wave until 2028 | Nov 2026 (strikes); 10 Jan 2027 (fees) | Hormuz crude < 8 mb/d for two weeks · STS hub suspended · Saudi export facility hit with lasting loss · Bab el-Mandeb tankers < 5/d · VLCC 1-yr TC > $250k on all sources · TD3C Q1-27 FFA > $1m/d · port fees reinstated |

**Mapping note `[A]`:**
- The **oil Bear supply variant** (OPEC+ market share with contango) is a crude-tanker Bull risk inside the oil Bear; it is not the shipping Bear.
- **Oil Base (11 Nov)** has faster supply recovery outside Iran under the same no-deal mechanism. For tankers that means more cargoes with the bypass and STS inefficiency intact, which is what Base 2027 rests on.
- **Sanctioned-tanker licences** sit outside the oil scenarios. They are a shipping supply catalyst that adds tonnage, not barrels.
- **Port fees** are a shipping supply catalyst (fleet fragmentation). They are combined with oil Base or Bull.

## Crude tankers — spot TCE $k/day, point (range)

| Scenario | Segment | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|
| Bear | VLCC | 70 (50–90) | 26 (21–31) | 24 (20–29) | 40.0 | 36 (32–40) |
| Bear | Suezmax | 50 (38–62) | 27 (22–32) | 25 (21–29) | 34.0 | 27 (24–30) |
| Bear | Aframax | 36 (28–44) | 29 (24–34) | 25 (21–29) | 30.0 | 24 (21–27) |
| **Base** | **VLCC** | **180 (145–230)** | **50 (40–62)** | **36 (30–44)** | **88.7** | **44 (40–50)** |
| **Base** | **Suezmax** | **115 (95–140)** | **44 (37–52)** | **30 (26–35)** | **63.0** | **33 (30–37)** |
| **Base** | **Aframax** | **65 (53–80)** | **38 (32–45)** | **35 (30–40)** | **46.0** | **30 (27–33)** |
| Bull | VLCC | 480 (350–650) | 150 (110–190) | 90 (70–110) | 240.0 | 55 (50–62) |
| Bull | Suezmax | 300 (220–400) | 108 (80–135) | 70 (55–85) | 159.3 | 41 (37–46) |
| Bull | Aframax | 160 (120–200) | 72 (58–88) | 55 (45–65) | 95.7 | 37 (33–41) |

- The 2028–29 crude paths rest on exits consistent with Base rates and on growth measured on the compliant fleet (see Fleet supply).
- **Segment order in 2029 Base (VLCC 36 > Aframax 35 > Suezmax 30)** is a supply effect. Aframax/LR2 has the smallest orderbook and the oldest, most sanctioned fleet (25%, Gibson), so its 2029 compliant growth is ~+3% against ~+5.6% for Suezmax. Mid-cycle keeps the normal order.
- **New VLCC orders** (21 in Q4 so far, mostly 2029–30 delivery) add ~+0.65 pp to 2029 fleet growth. That is ~−3% on the 2029 rate, below the minimum change; noted.
- **Bull 2029 flagged:** VLCC 90 / Suezmax 70 need crisis inefficiency to last through 2029.

## Product tankers — spot TCE $k/day, point (range)

| Scenario | Segment | 2027 | 2028 | 2029 | 3-yr avg | Mid-cycle |
|---|---|---|---|---|---|---|
| Bear | LR2 | 36 (28–44) | 29 (24–34) | 25 (21–29) | 30.0 | 24 (21–27) |
| Bear | LR1 | 28 (23–33) | 23 (19–27) | 20 (17–23) | 23.7 | 20 (17–22) |
| Bear | MR | 22 (18–26) | 19 (16–22) | 17 (15–19) | 19.3 | 17 (15–19) |
| **Base** | **LR2** | **65 (53–80)** | **38 (32–45)** | **35 (30–40)** | **46.0** | **30 (27–33)** |
| **Base** | **LR1** | **45 (38–53)** | **30 (26–35)** | **28 (24–32)** | **34.3** | **25 (22–28)** |
| **Base** | **MR** | **37 (31–43)** | **25 (22–29)** | **22 (19–25)** | **28.0** | **21 (19–24)** |
| Bull | LR2 | 160 (120–200) | 72 (58–88) | 55 (45–65) | 95.7 | 37 (33–41) |
| Bull | LR1 | 100 (75–125) | 48 (40–58) | 38 (32–44) | 62.0 | 31 (28–34) |
| Bull | MR | 58 (46–70) | 33 (28–38) | 27 (23–31) | 39.3 | 26 (23–29) |

- LR2 = Aframax from 2027 `[A]`.
- **The product rally is a tonnage story** (Xclusiv/Signal, 1 Aug–15 Oct vs a year earlier) `[E]`:
  - Seaborne product shipments −10.9%; clean-trading LR2s −39% (158 ships); clean LR1s −9.6%; crude-trading Aframaxes +20%.
  - Argus: 113 LR2s switched clean → dirty in Jan–Aug.
  - Base assumes they return to clean trade in H2-27. The Aframax correction may start that early: Gibson (6 Nov) expects condensate stems ex-NWOZ to be covered by LR2s.
- **LR1 flagged upward:**
  - The 1-yr TC rose to 67 / 68.5 (Intermodal / Compass, +12%), 133–136% of Base over the same 12 months. TC5 spot is still ~$210–230k, and the LR1 orderbook is the lightest product orderbook (~15%).
  - Kept, because the paper is flat to lower (TC5 Q4 −3%) and Gibson reports LRs softening.
  - **Retest rule:** raise LR1 2027 (45 → ~52) if the 1-yr TC holds ≥ 65 on two sources and TC5 spot stays above $150k into December.

## Year 1 by quarter ($k/day)

Shape `[A]`, unchanged; each row averages to the scenario's 2027 value.

| Scenario | VLCC Q1 / Q2 / Q3 / Q4 | Suezmax | Aframax | LR2 | LR1 | MR |
|---|---|---|---|---|---|---|
| Bear | 150 / 60 / 40 / 30 | 90 / 45 / 35 / 30 | 55 / 35 / 28 / 26 | 55 / 35 / 28 / 26 | 38 / 28 / 24 / 22 | 28 / 21 / 19 / 20 |
| **Base** | **400 / 160 / 90 / 70** | **230 / 115 / 65 / 50** | **114 / 63 / 43 / 40** | **114 / 63 / 43 / 40** | **69 / 44 / 33 / 34** | **48 / 36 / 31 / 33** |
| Bull | 800 / 500 / 350 / 270 | 500 / 300 / 220 / 180 | 260 / 160 / 115 / 105 | 260 / 160 / 115 / 105 | 150 / 100 / 80 / 70 | 75 / 58 / 50 / 49 |

- **VLCC Q1 (Base 400) against the Q1 paper:**
  - BWET TD3C Jan / Feb / Mar ≈ $476k / $399k / $376k → Q1 ≈ $417k on TD3C `[A]` (120–125 lots a month).
  - At the crisis segment/TD3C ratio (0.53–0.64) that is ~$220–270k for the segment. If the Gulf premium fades, as the paper's own 60% fall implies (ratio 0.75–0.9), it is ~$310–375k.
  - Base is 7–80% above the paper and is flagged with a retest rule (see Conclusion). The 12-month period market (99–128% of Base) does not confirm the paper.
- **Suezmax Q1 (Base 230):** BWET TD20 Jan / Feb / Mar ≈ $120k / $78k / $55k → Q1 ≈ $84k on TD20 (45 lots, thin), ~$115–140k for the segment at 1.37–1.64. Base is 65–100% above the paper, while the period market (1-yr 118–129%, *Amor* 120–136%) is above Base. Kept; this is the widest paper/period disagreement in the baseline.
- **Other segments:** fade with inefficiency; MR, Aframax/LR2 and LR1 get a Q4 seasonal uptick. No Q1 paper for TD25 or TC routes `[?]`.

## Market check

| Segment | Spot latest | 1-yr TC | 3-yr TC | FFA rest-Q4 / Q1-27 / Cal | Base 2027 / 3-yr avg | Gap > 20% |
|---|---|---|---|---|---|---|
| VLCC | Xclusiv avg 731.5 (6 Nov) `[F]`; ~565 est. (~11 Nov) `[A]`; TD3C 1,304 (Baltic 6 Nov) / 1,366 (Gibson 5 Nov); TD34 620 (6 Nov), WS411 ≈ 430 (10 Nov) `[A]` | 270 (Intermodal 6 Nov); 254.25 (Compass 9 Nov); 210 (Fearnleys 11 Nov) | 125 (Intermodal) | TD3C Q4 1,177 (Gibson 5 Nov) `[F]`; Nov / Dec 1,094 / 855 `[A]`; Q1 417 `[A]`; Cal `[?]` | 180 / 88.7 | Yes: Q1 paper (1); 1-yr at 120–128% on two sources (2) |
| Suezmax | Xclusiv avg 339.8 (6 Nov); TD20 224.5 (Baltic) / 238.75 (Gibson); TD6 513 (6 Nov); ~240 est. | 170 (Intermodal); 156.25 (Compass); 155 (Fearnleys); *Amor* 15-month 160–180 gross (6 Nov) | 77.25 | TD20 Q4 297 `[F]`; Nov / Dec 181 / 161 `[A]`; Q1 84 `[A]` (thin) | 115 / 63.0 | Yes (2) |
| Aframax | Xclusiv avg 175.5 (6 Nov); TD25 107.5 (Baltic) / 115.75 (Gibson); TD19 100.3; TD7 242.6; Asia ~175 | 100 (Intermodal); 95 (Fearnleys); 86.25 (Compass) | 53.25 | TD25 Q4 155.25 `[F]`; Q1 `[?]` | 65 / 46.0 | Yes (2) |
| LR2 | TC1 292 (Baltic) / 308 (Gibson); TC20 297; TC15 79 (6 Nov) | — (Aframax used) | — | `[?]` | 65 / 46.0 | As Aframax |
| LR1 | TC5 212 (Baltic) / 227 (Gibson); TC8 224 | 67 (Intermodal); 68.5 (Compass) | 39.5 | TC5 Q4 184.75 `[F]` | 45 / 34.3 | Yes (2) |
| MR | Atlantic basket 72.0 (Baltic) / 72.8 (Xclusiv); Pacific 85.5 (Xclusiv); TC7 71.75, TC18 70.75 (Gibson) | 43 (Intermodal); 39.5 (Compass) | 27.75 | TC7 Q4 70.0; TC18 Q4 51.0 `[F]` | 37 / 28.0 | No |

(1) See Year 1 by quarter.

(2) **Period rates against Base over the months they run** (skill rule: from the delivery month, here December; *Amor* from November):
- **Months used `[A]`:** Dec-26 at the stub's December level (VLCC ~447, Suezmax ~250, Aframax ~140, LR1 ~100, MR ~56).
- **Windows:** 12 months = Dec + 2027 Q1–Q3 + Oct–Nov 2027. 36 months = Dec + 2027 + 2028 + Jan–Nov 2029.

| Segment | 1-yr TC (sources) | Base Dec-26 → Nov-27 | 1-yr ÷ Base | 3-yr TC | Base Dec-26 → Nov-29 | 3-yr ÷ Base |
|---|---|---|---|---|---|---|
| VLCC | 210 / 254.25 / 270 | 211.4 | 99% / 120% / 128% | 125 | 100.1 | 125% |
| Suezmax | 155 / 156.25 / 170; *Amor* 160–180 (15 months: Base 131.3) | 131.7 | 118% / 119% / 129%; *Amor* 122–137% gross | 77.25 | 69.1 | 112% |
| Aframax | 86.25 / 95 / 100 | 73.3 | 118% / 130% / 136% | 53.25 | 48.9 | 109% |
| LR1 | 67 / 68.5 | 50.5 | 133% / 136% | 39.5 | 36.3 | 109% |
| MR | 39.5 / 43 | 38.9 | 102% / 111% | 27.75 | 28.9 | 96% |

- **Reading:**
  - The period market prices the next 12 months at 99–136% of Base in every segment. Spot and the Q1 paper fell 30–50% in two weeks, but the 1-yr TC moved only between −10% and +12%.
  - The gaps opened mainly because the window lost a high stub month while TC assessments held.
  - Gaps > 20% are explained by assessment lag: Intermodal was unchanged in the latest week and Compass rose $1k while spot fell. Fearnleys, the only source updated after the 9–11 Nov fall, is the lowest and sits at 99% (VLCC), 118% (Suezmax) and 130% (Aframax).
- **Which way the gaps should close:** from above, if spot stays near current levels through December. If the TC holds while spot recovers, Base 2027 (and LR1) is low. Neither direction is confirmed by two independent sources, so **no path moves**.
- **VLCC 3-yr 125%:** one source (Intermodal), sticky since its 16 Oct jump. The term structure below puts it at 1.18 × Base for 2028–29, below the 20% gap.
- **Company cross-check:** not read this run (DHT/Frontline Q3 company TCE) `[?]`.
- **MR2 resales with TC attached** (Xclusiv 9 Nov): *CS Fujairah* / *CS Rotterdam*, 12–15 months at $23.8k / $21.5k. Fixing date unknown; not used as a market mark.

**Period-market term structure `[A]`** (Intermodal 6 Nov). Forward TC for Dec-27 → Nov-29: F = (3 × TC3 − TC1) ÷ 2. Base over the same window: (Q4-27 × 1 + 2028 × 12 + 2029 × 11) ÷ 24.

| $k/day | TC1 / TC3 | Implied F | Base, same window | F ÷ Base | Reading |
|---|---|---|---|---|---|
| VLCC | 270 / 125 | 52.5 | 44.4 | 1.18 | Above Base, inside 20%; one-source 3-yr |
| Suezmax | 170 / 77.25 | 30.9 | 37.8 | 0.82 | Below Base |
| Aframax (LR2 proxy) | 100 / 53.25 | 29.9 | 36.7 | 0.81 | Below Base |
| LR1 | 67 / 39.5 | 25.75 | 29.25 | 0.88 | Slightly below |
| MR | 43 / 27.75 | 20.1 | 24.0 | 0.84 | Below Base |

- F is a direction check, not a level. Beyond Year 1 the period market sits at or below Base except VLCC. It does not support raising 2028–29.

**Anchors `[A]`** (8% nominal, 25 years, 355 days; opex VLCC 10.5, Suezmax 9.5, Aframax 9.0, LR2 9.5, LR1 8.5, MR 8.0; scrap ~$510/ldt):

| $k/day | VLCC | Suezmax | Aframax | LR2 | LR1 | MR |
|---|---|---|---|---|---|---|
| Newbuild-parity TCE | 44 | 33 | 29 | 30 | 25 | 21 |
| Asset-implied TCE (5-yr value, 20 years left) | 69 | 46 | 34 | 35 | 27 | 23 |
| 1-yr TC average 2024 / 2025 (Intermodal) `[F]` | 50.4 / 50.6 | 45.4 / 38.1 | 45.2 / 33.9 | — | 37.8 / 25.2 | 30.8 / 21.9 |
| Opex-level floor | ~10.5 | ~9.5 | ~9 | ~9.5 | ~8.5 | ~8 |

- The asset market prices a longer windfall than Base (asset-implied above parity in every crude segment), helped by ADNOC's buying.
- **Long-run reference:** VLCC 10-year average ~$35k `[E]` (Clarksons via press). Company cash breakeven ~$24k/day (Frontline) `[F]`.

**Asset values (now) `[F]`:**
- **Source:** Xclusiv 9 Nov (Korean newbuild prices; Japanese-built secondhand). LR1 5-yr: Intermodal October average. LR1 10-yr: KOBC (3 Sep) `[E]`.
- **Intermodal LR1 5-yr:** the November average is 75.0 (+10%), from one source. It is held at 68 until a second source confirms.
- **Cross-checks:**
  - Fearnleys (11 Nov): VLCC 215 / 190; Suezmax 135 / 110; Aframax/LR2 94.5 / 77; newbuild VLCC 130, Suezmax 87, Aframax 74, MR 49.5.
  - Intermodal 5-yr, November averages: VLCC 220, Suezmax 150, Aframax 95.
  - Compass (9 Nov): table misaligned in extraction; not used.
- **S&P `[F]`** (Compass 9 Nov; Xclusiv 9 Nov):
  - ADNOC L&S bought *Olympic Lady* (300k, 2017, eco) ~$185m, *Eurospirit* (320k, 2011) $153m, *Sponde* (158k, 2012) $110m and *Zouzou N* (150k, 2010) $103m. Trafigura bought *Sponde* in September for $74m.
  - *Rising Sun 1* (297k, 2005) $126m.
  - *Haima* (105k, 2009) $65m.
  - MR2 resales *CS Singapore* / *CS Houston* (50k, 2027) $55–56m each.
- **Mid-cycle values `[A]`** = (mid-cycle TCE − opex) × 355 days, discounted over 20 years at 8%, plus the present value of scrap.
- **Value risk:** US licences for sanctioned tankers would add old, mostly VLCC tonnage to the S&P market.

## Drivers

### Oil input and translation

From `docs/oil-market-bbb.md` (11 Nov, Final; Interface and "For downstream skills"). Base Brent 2027 84; stub 97.1; crack paths unchanged. The oil run judged nothing material for shipping.

| Oil input (oil BBB, 11 Nov) | Shipping effect |
|---|---|
| Disruption status unchanged: contested, no deal, blockade stays. Kpler Hormuz 7.82 mb/d (week to 8 Nov, ~46% of pre-war; scope unclear). FGE: crude 80–85% and products 35–40% of pre-war | Bypass, shuttle and STS inefficiency intact, which is Base's H1-27 assumption. No change |
| EIA (STEO 10 Nov): ME shut-ins 2.5 mb/d in October (10.9 at the May peak); ME output outside Iran back to pre-war by mid-2027. HSBC: Saudi 8.3 mb/d Q4-26, 9.8 in 2027. JPMorgan: ME exports ~20.7 mb/d in October; surplus 1.1 / 1.4 mb/d (Sep / Oct) | More crude cargoes in 2027: supports the 2027 volume leg (+7%). Normalisation of routing is the Bear risk; Base keeps it for H2-27 |
| Vortexa: Gulf product loadings ~3 mb/d in October (from ~1 in May). ARA gasoil imports 400 kb/d (35% Saudi) | Long-haul clean cargoes MEG → Europe recovering: supports LR2/LR1 (period LR1 up) |
| Russia: refining −30% (drones; up to ~1.5 mb/d of runs cut; Reuters 10 Nov); diesel export plan 2.15 Mt (Nov); tankers dropping US destinations | Fewer short-haul Russian diesel cargoes; Europe replaces from MEG/US/India. Mildly positive for MR/LR ton-miles; the US diesel deal is unlikely to move volume (Gibson) |
| Attacks continue: tanker hit 10 Nov; 37 ships attacked in October; Houthi missiles damaged the Aramco Tower in Riyadh (8 Nov) | Downtime and owner reluctance persist; Bull tail live |
| Brent–WTI narrowing (5.45 same-month; 2027 strip 3.9) | US crude export arbitrage narrows: less USG → Asia VLCC long-haul (TD22 −28% in a week) |
| Oil Bear catalyst closer (strikes on hold since 9 Nov; midterms; Russia–Ukraine talks); Bull further away | Shipping Bear closer in timing; not triggered |

### Trade flows and demand (ton-days / ton-miles per scenario and year)

- **VLCC `[E]`:**
  - **Fearnleys (11 Nov):** "another downward rate correction". A reported USG/China at $36m was later denied. TD34 WS411 and a Fujairah/Japan fixture at WS360 (on a ship discharging in Fujairah); returns $350–400k/day. 45 fixed (−5), 99 available in the MEG (+1).
  - **Gibson (6 Nov):** Gulf of Oman and east-bound fixtures below benchmarks; WAF charterers switching to Suezmaxes; the USG/Brazil market "had yet to establish a clear floor".
  - **Intermodal (10 Nov):** subdued cargo demand, mounting availability and Suezmax competition; Bahri Week reduces visible fixing.
  - **Reading `[A]`:** supply length and Atlantic weakness, with Gulf volumes intact. It fits Base's Q4-26 → Q1-27 step down; it is not yet a demand loss.
- **Suezmax `[E]`:**
  - Atlantic oversupply: TD20 −38%, TD27 −45%, TD33 −52% in the week to 6 Nov (Baltic).
  - CPC under pressure after failed fixtures (TD6 −29%).
  - Fearnleys (11 Nov): Aframaxes price Suezmaxes out of USG transatlantic, VLCCs compete for Atlantic volumes, 17 ships ETS within 5 days for TD20, and "supply side length dictates persistent softness".
- **Aframax `[E]`:**
  - The Med and North Sea collapsed (TD19 −55%, TD7 −38%; Baltic 6 Nov).
  - Fearnleys (11 Nov): the Med "bottom has been established", while the North Sea has more room to soften.
  - Asia ~$175k (Gibson); Kuwait–Singapore still ~$385k (Xclusiv).
- **Products `[E]`:**
  - MEG LR2/LR1 stable at high levels (TC1 ~$292–308k, TC5 ~$212–227k); TC15 Med–East down to $79k.
  - AG MRs tight (TC17 WS600); UKC/Med MRs past peak.
  - Gibson (6 Nov) on the midterms: tighter Russia sanctions are more likely; the US diesel deal is less likely to deliver.
- **China (crude):** no new arrivals data `[?]`.
- **Demand in ton-days, change vs prior year `[A]`** (unchanged; inefficiency counted here only):

| % y/y | 2027 | 2028 | 2029 |
|---|---|---|---|
| Crude Bear | −8 (inefficiency gone in H1) | +1 | +2 |
| Crude Base | +1 (volumes +7, inefficiency −6) | +3 | +2 |
| Crude Bull | +5 | 0 | +1 |
| Product Bear | −2 | +1 | +1 |
| Product Base | +4 | +2 | +2 |
| Product Bull | +6 | +2 | +1 |

- **Oil BBB 11 Nov test:** the faster supply recovery outside Iran supports the 2027 volume leg. Routing is unchanged, so the inefficiency leg holds; net crude Base 2027 stays at about +1.

### Trade rules: USTR/China port fees

- **Outcome `[F]`:**
  - **USTR:** the notice of 9 Nov (Federal Register 10 Nov, doc. 2026-22867) suspends the Section 301 maritime actions for two more months, effective 9 Nov to 23:59 ET on 9 Jan 2027. That covers the Annex I–III port fees on Chinese-operated or -owned and Chinese-built vessels, and the Annex V.A duties on ship-to-shore cranes and cargo-handling equipment. "To allow for further negotiation with China"; ~60 comments received. USTR "will consider before January 10, 2027" whether to continue; Holland & Knight advises treating 10 Jan as a live deadline.
  - **China:** the Ministry of Transport (9 Nov, approved by the State Council after the eighth round of consultations) extended to 10 Jan 2027 its suspension of special port fees on US-linked vessels (US-built, US-flagged or ≥ 25% US-owned) and of its shipping probe. The Hanwha Ocean countermeasures stay suspended (Maritime Executive).
- **Effect on tankers:** none on effective tonnage, routing or TCE in any segment.
  - Chinese-built, -owned or -operated tankers keep calling at US ports without fees; US-linked tankers keep calling at Chinese ports.
  - Base never assumed fees; the stub and paths are unchanged.
- **Bull leg deferred to 10 Jan 2027.** Reinstated fees would fragment the fleet again: US-linked VLCCs out of China discharges, Chinese-built and -owned tonnage out of US loadings, as in October 2025. That lowers effective supply on USG–Asia and MEG–China.
- **Signposts:** the Trump–Xi meeting (~18–19 Nov, APEC Shenzhen); a USTR notice before 9 Jan. Gibson (6 Nov): changes to Section 301 measures "look unlikely" under the new Congress because the powers sit with the White House.

### Chokepoints (transits vs normal, extra sailing days, fleet share absorbed)

IMF PortWatch, tanker transits per day (AIS), latest data 8 Nov `[F]`:

| Chokepoint | 2023 Jan–Oct | 2026 Jan–Feb (pre-war) | 12–18 Oct | 26 Oct–1 Nov | 2–8 Nov | Effect |
|---|---|---|---|---|---|---|
| Hormuz | 57.4 | 37.0 | 0.6 | 1.4 | 1.0 | AIS dark: use Kpler (7.82 mb/d, week to 8 Nov, via oil BBB) |
| Gulf of Oman STS hub (Sohar, Fujairah) and northern Gulf STS | — | — | Attacks on STS (Oct) | — | Not suspended; Fujairah fixing continues (Gibson) | ~40% bypass (Sep), > 1 mb/d STS; +6% VLCCs per mb/d (Clarksons); ~10 days per STS |
| Bab el-Mandeb | 26.2 | 12.5 | 10.0 (554 kt/d) | 8.6 (411 kt/d) | 6.9 (343 kt/d) | Falling: −31% in the latest week vs 12–18 Oct, −21% over two weeks; trigger needs > 20% held two weeks (one week so far). Bull < 5/d |
| Suez | 25.6 | 15.9 | 15.9 | 17.0 | 15.4 (780 kt/d) | Steady |
| Panama | 12.9 | 12.8 | 13.0 | 11.3 | 12.1 (329 kt/d) | Normal; El Niño dry-season risk from late November |
| Cape of Good Hope | 9.1 (686 kt/d) | 15.1 (893 kt/d) | 19.3 (993 kt/d) | 19.4 | 15.9 (956 kt/d) | Back to the pre-war 2026 level: fewer Atlantic and westbound voyages after the Atlantic correction. Still ~1.7× 2023 |

### Effective tonnage (per segment, share of fleet unavailable)

| Item | VLCC | Suezmax | Aframax/LR2 | LR1/MR | Source |
|---|---|---|---|---|---|
| Attack damage and downtime | > 3% of the VLCC fleet damaged since March (cumulative); Base 1–2% out at any time `[A]` | Black Sea war risk zone | Some | Some | Nortilus (16 Oct); oil BBB (37 ships attacked in October) `[E]` |
| Sanctioned / shadow | 164 sanctioned; 153 OFAC-only; Iran owns 38 | 116; 28 OFAC-only | 322 (25%); 42 OFAC-only | ~40 CPP MRs OFAC-only | Gibson 16 Oct `[E]`. US-sanctioned ships 1,568 incl. 462 crude tankers (4 Nov; Bloomberg via gCaptain) `[E]` |
| US licences for sanctioned tankers | Applications for ~50 ships (all types, incl. 2 mb supertankers) by Trafigura, Vitol, Mercuria, ADNOC; none granted; case by case (8 Nov). Realistic VLCC returns 14–24 (Kpler, Braemar, Arrow; 20 Oct) | None realistic (Arrow) | None realistic (Arrow) | Few | gCaptain/Bloomberg 8 Nov; Splash247 20 Oct `[E]` |
| ≥ 20 years (now → at full delivery) | 18.3% → 29.6% | 22.0% → 32.7% | 22.0% → 39.5% | Panamax/LR1 22.6%, Handy/MR1 37.3% | Frontline (28 Aug) `[F]`; Xclusiv 12 Oct `[F]` |
| Shuttle / STS / escort | Shuttle and STS (+6% per mb/d); ~40% of Gulf crude bypassing (Sep) | Yanbu STS | ~14 LR2s in shuttle (Aug) | Small | Clarksons; Kpler; Citi `[E]` |
| Clean ↔ dirty | — | — | Clean LR2s −39% (158); 113 switched Jan–Aug | Clean LR1s −9.6%; crude-trading Panamaxes +18.6% | Xclusiv/Signal 19 Oct; Argus 15 Oct `[E]` |
| Port fees | None (suspended to 9/10 Jan 2027) | None | None | None | USTR 9 Nov; China MoT 9 Nov `[F]` |

- **Reading `[A]`:**
  - The ~50 ships in licence talks span all types. If ~30 were VLCCs and all were granted, the Bear supply signpost (> 30 VLCCs) would be reached. That is not the case yet.
  - 14–24 VLCCs is 2–3% of the compliant VLCC fleet, inside Base's < 30 cap. 30 would loosen the 2027–28 VLCC balance by ~4 pp; 100 by ~13 pp.
- **Base `[A]`, unchanged:**
  - Attack downtime (1–2%) and shuttle/STS inefficiency last through H1-27 and ease in H2-27.
  - LR2s clean up in H2-27 (+~5% clean supply).
  - Sanctioned ships beyond a licensed few stay outside compliant trade.

### Fleet and orderbook register

Updated 13 Nov. As-of date in each cell; `[?]` = not sourced. Fleet = total fleet unless stated.

| Segment | Fleet (vessels; m dwt) | Orderbook (vessels; % fleet) | Delivered 2026 YTD | Schedule: rest-26 / 27 / 28 / 29 / 30+ | New orders: Q3-26 / Q4-26 so far | Scrapped: Q3-26 / Q4-26 so far / earlier | ≥ 20 yrs now / at full delivery | Sanctioned / outside compliant trade | Newbuild $m; earliest slot |
|---|---|---|---|---|---|---|---|---|---|
| VLCC | ~907 `[A]` (304 ÷ 33.5%); 277.1m dwt (Allied, Jul) `[F]` | **304** (Frontline, 11 Aug; stale) `[F]`; ~310–325 ≈ 34–36% incl. Q4 orders less deliveries `[A]`; 32.5% by dwt (Xclusiv, 12 Oct) | ~37 `[A]` (31 to 12 Oct, Xclusiv; ~6 since, Compass) | ~5 / 62 / 125 / 106 / 38 `[A]` (sum 336). Compass (9 Nov) 5 / 68 / 107; Clarksons 64 / 102; BRS 60 / 127 | ≥ 22 reported / **21 confirmed** (Scorpio 2, JP Morgan 2, Venergy 2 + 2 opt, Bahri 3 `[A]`, Stealth 2, CSET 10) + ≤ 4 unconfirmed (Hengli) | 1 / none / 7 in 2022–26 (Drewry) `[E]` | 18.3% / 29.6% (Frontline, 28 Aug) `[F]` | 164 sanctioned, 153 OFAC-only (Gibson, 16 Oct) `[E]`; licences: none granted (8 Nov) | 131.5 (Xclusiv 9 Nov, Korea); 130 (Fearnleys 11 Nov); Hanwha 133–133.5 (2030); Scorpio 135 at Hengli; China late 2028, Korea 2030 |
| Suezmax | ~634 `[A]` | **182** (Frontline, 11 Aug) `[F]` ≈ 28.7% `[A]`; 29.6% by dwt (12 Oct) | 26 to mid-Jul `[F]`; ~7 delivered 19 Oct–9 Nov (Compass) | ~8 / 45 / 60 / 50 / 15 `[A]` (incl. Liquimar 3). Compass (9 Nov) 8 / 50 / 78 | ≥ 8 (+1 shuttle) / 3 (Liquimar, New Hantong, $84m, 2029–30) + 2 unconfirmed (Hengli) | 0 / none / 16 in 2022–26 `[E]` | 22.0% / 32.7% `[F]` | 116, 28 OFAC-only `[E]`; none realistic under licences (Arrow) | 90.5 (Xclusiv); 87 (Fearnleys); New Hantong 84 |
| Aframax/LR2 | **1,239**; 136.9m dwt (Allied, Jul) `[F]` | **221** (Frontline, 11 Aug) `[F]` + 8 Q4 orders ≈ 18.5% `[A]`; 20.7% by dwt (12 Oct) | 47 to mid-Jul `[F]`; ~88 for 2026 (Breakwave) `[E]`; ~16 delivered 19 Oct–9 Nov (Compass) | ~16 / 60 / 67 / 55 / 17 `[A]`. Compass (9 Nov) 16 / 81 / 82; McQuilling (Feb) 89 / 79 / 37+ | ≥ 22 (+2 opt) / **8 confirmed** (Nanjing Tankers 4 × 114k DSIC 2029; Stealth 2 × 115k HD Hyundai $78m 2029–30; Laskaridis 2 × 114k Hengli 2028) + ≤ 4 LR2 unconfirmed (Hengli) | 2 / none / 23 in 2022–26 `[E]` | 22.0% / 39.5% `[F]` | 322 = 25%, 42 OFAC-only `[E]` | 78 (Xclusiv); LR2 ~80 `[A]`; China 2028–29 |
| LR1/Panamax | **438; 32.0m dwt** (McQuilling, Feb; stale) `[E]` | 13.6% (Galbraiths, Aug) `[E]` + 6 Emarat ≈ 15% `[A]` | `[?]` | McQuilling 26 / 16 / 18+; Compass (9 Nov) 3 / 30 / 20; + Emarat 6 (2029–30) | ≥ 6 / 6 (Emarat, New Hantong) `[F]` | 0 / none / `[?]` | 22.6% (Xclusiv, 12 Oct) `[F]` / `[?]` | `[?]` | 62.5 (Xclusiv, Korea); China ~55 `[E]` |
| MR (incl. MR1) | **2,978**; 132.0m dwt (Allied, Jul) `[F]` | MR2 19.7% by dwt (Xclusiv, 12 Oct) `[F]`; MR2 304 = 15.3% by number (McQuilling, Feb; stale) `[E]` | 63 MR2 to mid-Jul `[F]` | MR2 152 / 111 / 41+ (McQuilling, Feb) + ~135 ordered since → 2028+ ~165 `[A]` | ≥ 39 (+2 opt) / **16** (Top Ships 4; Central Mare 2; Leon 2 at $52.9m, 2029; Navios 2; TORM 2; Jiangsu Haifeng 4; sizes realigned `[A]`) + 2 × 40k MR1 | ~4 Handy/MR1 + 1 MR / none / `[?]` | Handy/MR1 37.3% (Xclusiv, 12 Oct) `[F]` | ~40 CPP MRs OFAC-only `[E]` | 52.5 (MR2, Xclusiv); 49.5 (Fearnleys) |

**Aggregates `[F/E]`:**
- **Xclusiv (12 Oct, main segments, dwt):** fleet 738.9m; deliveries 32.6m in 2026 to date; scheduled 50.7m (2027), 61.2m (2028), 67.5m (2029+); 19.8% ≥ 20 years.
- **All tankers > 25k dwt (Allied, Jul):** 6,302 ships / 693.05m dwt; orderbook 1,267 / 173.32m dwt.
- **Hafnia/Vortexa (28 Aug) `[E]`:** 161m dwt delivers in 2027–29 against 106m dwt of exits.
- **BIMCO (Aug/Sep) `[E]`:** crude orderbook 27–28%, > 70% delivering 2028+.

**Schedule check `[A]`:**
- **VLCC 2027 / 2028 by source:** Compass 68 / 107, Clarksons 64 / 102, BRS 60 / 127; Base 62 / 125 follows BRS. On Compass/Clarksons 2028 is ~2 pp tighter and 2029 looser; the average is unchanged.
- **Suezmax 2027 / 2028:** Compass 50 / 78 vs Base 45 / 60, i.e. ~+3 pp in 2028 on Compass `[A]`. Not applied: one source, timing rather than total.
- **Aframax/LR2 2027:** Compass 81 vs Base 60. This is timing.
- No year moves by the minimum change.
- **To do:** re-base the schedule on Frontline's Q3 orderbook count (late Nov) with the Compass, Clarksons and BRS spread.

**Contracting and demolition log, Q4-26 so far** (reported deals; a minimum count):

| Segment | Confirmed (broker tables) | Unconfirmed `[?]` | Demolitions |
|---|---|---|---|
| VLCC | 21: Scorpio 2 (Hengli, 2028, $135m); JP Morgan 2 (Hanwha, 320k, 2030, $133–133.5m; Intermodal wk 44 and Xclusiv 9 Nov; = "Global Meridian" in Xclusiv 2 Nov `[A]`); Venergy 2 + 2 options (Hengli, 306k, 2029); Bahri 3 (IMI; Xclusiv 2 Nov, size realigned from a misaligned table `[A]`); Stealth 2 (Hanwha, 320k, 2030, $133m); CSET 10 (6 COSCO HI Yangzhou + 4 DSIC, 309k, LNG-ready, 2029–30; Intermodal wk 45) | Up to 4 more at Hengli (Chinese press, 14 Oct; Venergy's 2 may be part of the 6 reported) | None |
| Suezmax | 3 (Liquimar, 157k, New Hantong, $84m, 2029–30) | 2 at Hengli | None |
| Aframax/LR2 | 8: Nanjing Tankers 4 (114k, DSIC, 2029); Stealth 2 (115k, HD Hyundai, $78m, 2029–30); Laskaridis 2 (114k, Hengli, 2028) | Up to 4 LR2 at Hengli | None |
| LR1/Panamax | 6 (Emarat, 74k, New Hantong, 2029–30) | — | None |
| MR | 16 (see register) + 2 × 40k (Kitanihon) | — | None |

- **Contracting trigger (> 3% of a segment fleet in a quarter, vessel count):** not fired.
  - VLCC 2.3% (2.8% with the unconfirmed); close, watch.
  - Suezmax 0.5%; Aframax/LR2 0.6%; LR1 1.4%; MR 0.5%.
- **Orderbook trigger (> 2 pp):** not testable on a consistent basis this run.
  - VLCC on a vessel count: +21 orders − ~6 deliveries since 24 Oct ≈ +1.6 pp `[A]`.
  - Re-test on Frontline's Q3 count (late Nov) and Hafnia's Q3 deck (18 Nov) for MR2.
- **Slippage:** not testable yet; the 2027 schedule above is the January reference.

### Fleet supply (fleet growth per segment and year; scrapping per scenario)

| Fleet growth, Base `[A]` | 2027 | 2028 | 2029 |
|---|---|---|---|
| VLCC deliveries / exits from compliant trade | 62 / 5 | 125 / 10 | 106 / 25 |
| VLCC growth of the compliant fleet | +7.5% (~757 → 814) | +14.1% (→ 929) | +8.7% (→ 1,010) |
| Suezmax deliveries / exits (compliant growth) | 45 / 5 (+7.4%, ~539 → 579) | 60 / 10 (+8.6%) | 50 / 15 (+5.6%) |
| Aframax/LR2 deliveries / scrapping (net) | 60 / 15 (+3.5%) | 67 / 15 (+4.0%) | 55 / 20 (+2.6%) |
| LR1/MR net growth (scrapping 1.5 / 1.0 / 1.5%) | +4% | +4% | +2% (LR1 ~+2%, MR ~+2.5%) |

- **Compliant-fleet basis:** nominal fleet minus sanctioned ships; all deliveries enter compliant trade. VLCC ~757 compliant at start-2027 (917 − 160); Suezmax ~539.
- **Exits consistent with each scenario's rates:** the VLCC demolition record of 38 (2018) came at earnings near opex; only 7 VLCCs were scrapped in 2022–26, and all 2026 VLCC/Suezmax removals were sanctioned ships. Base exits 5 / 10 / 25.
- **Product scrapping:** run-rate ~0.5–0.6% a year; Base uses 1.0–1.5% (LR1/MR) and 15–20 Aframax/LR2 a year.
- **Scrapping by scenario `[A]`:** Bear VLCC 20 / 50 / 60 (near cash breakeven, as in 2018); Bull 5 / 5 / 10; Base as above.
- **Q4 orders this run:** 2029 VLCC growth +8.1% → +8.7% (+0.65 pp), Aframax/LR2 2028–29 +0.2–0.4 pp. Both are below the minimum change on the rate.

### Balance check (demand − effective fleet growth, per segment, scenario and year)

Inefficiency is counted only in demand (ton-days).

| pp change in tightness `[A]` | 2027 | 2028 | 2029 | Rate path consistent? |
|---|---|---|---|---|
| VLCC Bear (compliant basis; ~40 Iranian VLCCs back in 2027 and ~20 in 2028) | −8 − 10.8 = **−18.8** | 1 − 11.3 = **−10.3** | 2 − 4.3 = **−2.3** | Yes: 70 → 26 → 24, near Frontline's ~$24k cash breakeven, where 50–60 VLCCs scrapped a year is plausible (2018) |
| VLCC Base (compliant basis) | +1 − 7.5 = **−6.5** | 3 − 14.1 = **−11.1** | 2 − 8.7 = **−6.7** | Yes: 630 stub → 180 (Q4-27 70) → 50 → 36. 2029 is the trough at ~80% of parity, where exits of ~25 begin |
| VLCC Bull (scrapping 5 / 5 / 10) | 5 − 7.5 = **−2.5** | 0 − 14.7 = **−14.7** | 1 − 10.2 = **−9.2** | **Flagged:** 480 → 150 → 90 needs crisis inefficiency to last through 2029 |
| Suezmax Base (compliant basis) | 1 − 7.4 = **−6.4** | 3 − 8.6 = **−5.6** | 2 − 5.6 = **−3.6** | Yes: 400 stub → 115 → 44 → 30 (91% of parity) |
| Suezmax Bear | −8 − ~8.3 = **~−16** | 1 − ~6.8 = **~−6** | 2 − ~4 = **~−2** | Yes: 50 → 27 → 25 |
| Aframax/LR2 Base | 2 − 3.5 = **−1.5** | 2 − 4.0 = **−2.0** | 2 − 2.6 = **−0.6** | Yes: 210 stub → 65 (Q4-27 40) → 38 → 35 |
| LR1/MR Base | 4 − 4 − 3 (LR2s back to clean) = **−3** | 2 − 4 − 2 = **−4** | 2 − 2 = **0** | Yes: LR1 120 stub → 45 → 30 → 28; MR 62 → 37 → 25 → 22 |

- **How 2028–29 were set:**
  - Crude: Q4-27 exits at 70 (1.6× parity). A −11 pp year takes 2028 to ~50, and a further −7 pp takes 2029 to ~36 (~80% of parity).
  - In the 2010–13 and 2017–18 delivery waves VLCC earnings fell to ~50–65% of newbuild parity `[E, background]`. Base stays above that history because ~18% of the fleet is sanctioned, Cape/Red Sea routing persists and restocking runs into 2028.
  - Products: the 2029 balance is about flat at the observed scrapping run-rate.
- **Re-test this run:**
  - The period market prices 36 months from December at 96–125% of Base. The term structure for 2028–29 sits at 0.81–1.18 × Base.
  - New orders shift 2029 by < 1 pp.
  - Licence talks remain inside Base's cap.
  - **Kept.**
- **Mid-cycle kept (VLCC 44 / Suezmax 33).** 2029 is the trough, not the norm: deliveries fall from 2030 and ~30% of the fleet is ≥ 20 years old at full delivery. The exit at mid-cycle values assumes a 2030–31 recovery; the IAF bridge should name it.
- **Non-linearity:** the market starts at extreme utilisation (VLCC spot ~15× its 10-year average even after the correction). No published utilisation series was read `[?]`.

## Signposts and monitoring

| Signpost | Threshold (Bear / Bull) | Now (13 Nov) | Direction since 24 Oct |
|---|---|---|---|
| Hormuz flows (Kpler, via oil BBB) | Bear ≥ 13 crude without escort · Bull < 8 crude for two weeks | 7.82 mb/d (week to 8 Nov; scope unclear, ~46% of pre-war); week to 4 Nov missing | Touched on an unlike series (oil BBB: not confirmed) |
| Tanker attacks / STS | Bull: STS hub suspended | 37 ships attacked in October; tanker hit 10 Nov; Fujairah fixing continues | → Bull tail live; not suspended |
| Saudi export infrastructure | Bull: facility hit with lasting loss | Houthi missiles damaged the Aramco Tower, Riyadh (8 Nov); no lost export barrels | → Bull, not crossed |
| Iran–USA | Bear: deal > 60 days · Bull: new strikes | Strikes on hold (9 Nov; "no immediate plans"); Democrats won both chambers (Congress 3 Jan); Iran denies talks; blockade stays | → Bear (closer, not triggered) |
| US licences for sanctioned tankers | Bear > 30 VLCCs approved · Base < 30 | Applications for ~50 ships of all types (Trafigura, Vitol, Mercuria, ADNOC); none granted (8 Nov) | → Bear (applications filed) |
| Bab el-Mandeb tankers (PortWatch) | Bear > 18/d · Bull < 5/d | 6.9/d (2–8 Nov) | ↓ (−3.1/d); toward Bull |
| VLCC 1-yr TC | Bear < 90k · Bull > 250k on all sources | 270 (Intermodal 6 Nov) / 254.25 (Compass 9 Nov) / 210 (Fearnleys 11 Nov) | ↓ (−4 to −10%); still above 250k on two of three |
| VLCC segment average (info: stub) | — | 731.5 (6 Nov); ~565 est. (~11 Nov) | ↓ |
| TD3C Q1-27 paper (TD3C TCE) | Bear < 300k · Base < 700k by end-Dec · Bull > 1m | ~417k `[A]` (BWET 13 Nov; 120–125 lots a month) | ↓↓ (−52%); Base signpost met early; 117k above Bear. Retest rule set |
| TD34 (Gulf of Oman–China; info) | — | WS411 ≈ $430k (10 Nov) `[A]`; WS360 fixture (Fujairah/Japan) | ↓ (−35% since 23 Oct) |
| Suezmax 1-yr TC | Suezmax 2027 → ~100 if < ~130k on Intermodal/Fearnleys | 170 (Intermodal) / 155 (Fearnleys) / 156.25 (Compass); *Amor* 15-month 160–180 | ↓ slightly; supports Base 2027 |
| TD20 Q1-27 paper (info; thin) | Suezmax 2027 review if it falls further | Jan ~120k, Q1 ~84k `[A]` (45 lots) | ↓ (−28%); reviewed: kept (period market above Base) |
| LR1 1-yr TC | Raise LR1 2027 if ≥ 65 on two sources and TC5 > 150k into December | 67 (Intermodal) / 68.5 (Compass); TC5 ~$212–227k | ↑ (+12%); watch |
| USTR/China port fees | Bull: fees reinstated | Suspended to 9 Jan (USTR, 23:59 ET) / 10 Jan 2027 (China), Hanwha countermeasures included | Deferred two months |
| China product exports | Bull for Pacific clean if quotas rise | Not read `[?]` | Open |
| Russian diesel | Bear for MR if > 0.6 mb/d | Refining −30% (drones); export plan 2.15 Mt (Nov); US destinations dropped | Lower Russian exports; mildly Bull for MR/LR ton-miles |
| Panama tanker transits | Bull for MR/LR1 ton-miles: < 10/d for two weeks | 12.1/d (2–8 Nov) | Normal |
| VLCC orderbook/fleet | Bear > 40% of total fleet | ~34–36% `[A]` (count); 32.5% by dwt (12 Oct) | ↑ |
| VLCC contracting per quarter | Bear > 3% of fleet (~27 ships) | Q4: 21 confirmed (2.3%) + ≤ 4 unconfirmed (2.8%) | ↑ close to trigger |
| Aframax/LR2 orderbook | Bear > 25% of fleet | ~18.5% (vessels) `[A]`; 20.7% by dwt (12 Oct) | Base |
| VLCC exits from compliant trade | Bear ≥ 50 a year near cash breakeven · Bull ≤ 5 | None reported in Q4 | Base needs 10 (2028) and 25 (2029) |
| Product and Aframax/LR2 scrapping | Bear < 0.5% a year from 2028 at parity · Bull > 3% | ~0.5–0.6% a year (2026); none reported in Q4 | Base needs 1.0–1.5% / 15–20 |
| Product orderbook for 2029 | Bear > 15m dwt · Bull < 10m dwt | ~13m dwt `[A]` | Rising |
| LR2s trading dirty | Bear for clean < 40% | > 50% dirty (Signal, 15 Oct); no new data `[?]` | → (Aframax correction may pull LR2s back to clean) |
| LR1 contracting and orderbook | Bear for LR1 > 16% or Q4 orders > 3% | ≈ 15%; Q4 orders 6 (1.4%) | Watch |
| AG VLCC fixtures / list (Fearnleys) | Bull: sharp fall in liftings | 45 fixed in the week (−5); 99 available in the MEG next 30 days (+1) (11 Nov) | → Base |
| Cape of Good Hope tankers (info) | — | 15.9/d (2–8 Nov) | ↓ (Atlantic correction) |

**Watch before the next update (stale after 4 Dec):**
- Xclusiv 16 and 23 Nov (the VLCC, Suezmax and Aframax levels behind the stub).
- BWET Q1 TD3C/TD20 contracts and Fearnleys/Intermodal/Compass 1-yr TC, for the two retest rules (VLCC Q1, LR1).
- US licences for sanctioned tankers (number of VLCCs).
- Trump–Xi meeting (~18–19 Nov) and any USTR notice before 9 Jan.
- Attacks on STS and Saudi infrastructure; any US decision before 3 Jan.
- Hafnia Q3 deck (18 Nov; product orderbook by year); Frontline Q3 orderbook (late Nov).
- New Oil Market BBB after OPEC+ (29 Nov).

## For IAF

- **Stub Q4-26 open days (market basis):**

| Segment | Stub Q4-26 | Δ vs 24 Oct | Nov–Dec market level `[A]` |
|---|---|---|---|
| VLCC | **630** | −70 | ~450–520 |
| Suezmax | **400** | −65 | ~240–250 |
| Aframax | **210** | −95 | ~140 |
| LR2 | **170** | −50 | ~125 |
| LR1 | 120 | — | ~100–110 |
| MR | **62** | +7 | ~56 |

  - The stub is a quarter average, and October (realised) sits well above November–December. Open days that fall from mid-November should use the Nov–Dec level, or the company's own stub factor on the quarter mark.
  - Booked days stay at booked rates.
- **2027–2029, Year-1 quarters and mid-cycle unchanged, so V_T is unchanged.** Asset values "now" rose 0–6% (Xclusiv 9 Nov).
- **Flags for valuation:**
  - VLCC Q1-27 Base (400) is above the traded Q1 paper (segment-equivalent ~$220–375k), so test the Q1 open days at ~300 as a sensitivity.
  - LR1 2027 may be raised at the next run (period at 133–136% of Base).
- **CAPT (on hold):** Suezmax and Aframax/LR2 open-day marks fell (Nov–Dec ~245 / ~140). The *Amor* TC at 120–136% of Base supports the Base Suezmax 2027. No path change.
- **Hafnia:** LR2 stub down 50, MR up 7, LR1 kept. 2027+ unchanged; LR1 upside flag.
- **Growth-capex hurdle:** unchanged. A VLCC newbuild at $131.5m needs ~$57k/day sustained to earn k = 12%; Base mid-cycle is 44. Hanwha's 2030 slots at $133m confirm the price.

## Change log

- **13 Nov 2026 (update; port-fee deadline, *Amor*):** stub re-marked after the post-midterm crude correction (VLCC 700 → 630, Suezmax 465 → 400, Aframax 305 → 210, LR2 220 → 170, MR 55 → 62; LR1 kept); "now" values re-marked; port fees suspended to 9/10 Jan 2027 (no effect). The Year-1 FFA trigger fired (TD3C Q1 −52%, TD20 −28%) and was tested: 2027–29 and mid-cycle kept because the period market (99–136% of Base) disagrees; retest rules for VLCC Q1 and LR1 set. No Base path moved.
- **24 Oct 2026 (update):** stub re-marked (VLCC 850 → 700, Aframax 245 → 305) on the new stub method (October segment average + paper path); period market tested over the months a charter runs; paths kept.
- **17 Oct 2026 (update):** stub re-marked; OFAC/sanctioned-tanker catalyst added to Bear; paths kept.

## Appendix: sources

| Source | Content (raw values) | Observed / published |
|---|---|---|
| `docs/oil-market-bbb.md` | Interface and "For downstream skills": Base Brent 2027 84; disruption status; Kpler Hormuz 7.82 mb/d; FGE; Vortexa Gulf product loadings ~3 mb/d; Russian refining −30%; attacks; Brent–WTI | 11 Nov 2026 |
| [Holland & Knight, "USTR Extends Section 301 Maritime Fee, Cargo Handling Equipment Duty Suspension to January 9"](https://www.hklaw.com/en/insights/publications/2026/11/ustr-extends-section-301-maritime-fee) | USTR proposal 23 Oct; final notice effective 9 Nov, Federal Register 10 Nov (doc. 2026-22867); suspension to 23:59 ET 9 Jan 2027 / HTS date 10 Jan 2027; Annexes I–III fees and Annex V.A duties; ~60 comments; "will consider before January 10, 2027" | Nov 2026 |
| [Shipping Telegraph, "US and China extend pause on reciprocal port fees by two months"](https://shippingtelegraph.com/port-news/us-and-china-extend-pause-on-reciprocal-port-fees-by-two-months/) | USTR (Greer) and China MoT (9 Nov, State Council, eighth round of consultations): both suspensions to 9/10 Jan 2027; China's probe suspended | 10 Nov |
| [Maritime Executive, "China follows US in continuing suspension of fees on shipping"](https://maritime-executive.com/article/china-follows-us-in-continuing-suspension-of-fees-on-shipping) (search summary) | China also extends suspension of Hanwha Ocean countermeasures and critical-mineral waivers | ~10 Nov (secondary) |
| [Gibson, "Mid Term Fallout"](https://www.gibsons.co.uk/report/mid-term-fallout/) | Midterms (Democrats both chambers); December tanker FFA −27%; regional commentary. Table (eco, non-scrubber, 5 Nov): TD3C WS1,221 / $1,366,000, Q4 FFA WS1,065 / $1,177,000; TD20 WS430 / $238,750, Q4 $297,000; TD25 WS399 / $115,750, Q4 $155,250; TC1 WS1,005 / $308,250; TC5 WS1,025 / $227,250, Q4 $184,750; TC18 $70,750, Q4 $51,000; TC7 $71,750, Q4 $70,000. Bunkers Fujairah 869, Singapore 855, Rotterdam 717 $/t. Clean text "TC1 75 × WS400 / TC5 55 × WS450" conflicts with its table (not used) | 5 Nov / 6 Nov |
| [Baltic Exchange tanker report week 45](https://www.balticexchange.com/en/data-services/WeeklyRoundup/tanker/news/2026/tanker-report-week-45.html) (in-app browser) | TD3C WS1,220.63 / $1,303,616; TD34 WS586.43 / $619,969; TD15 WS564.38 / $561,731; TD22 < $58m / ~$451,000; TD20 WS430 / ~$224,500; TD27 WS382.22 / ~$198,400; TD33 WS292.78 / ~$172,200; TD6 WS664.44 / ~$513,400; TD7 WS350 / ~$242,600; TD19 WS300 / ~$100,300; TD26 WS408 / ~$122,000; TD9 WS397 / ~$111,100; TD25 WS399 / ~$107,500; TD28 $10.15m / ~$206,200; TC1 WS1,005 / $292,000; TC20 $19.29m / $297,300; TC15 $9.25m / $79,200; TC5 WS1,025 / $212,300; TC8 $14.75m / $223,700; TC17 WS896 / $113,900; TC2 $13,600; TC14 $60,800; TC21 $60,600; MR Atlantic basket $72,000 (from $82,100); TC6 $88,100; TC23 $78,500. Week 46 not published at writing (404) | 6 Nov |
| Xclusiv Shipbrokers Weekly, 26 Oct / 2 Nov / 9 Nov (PDFs via Hellenic Shipping News) | Segment averages: VLCC 761,352 / 829,398 / 731,473; Suezmax 638,377 / 570,090 / 339,785; Aframax 336,059 / 303,147 / 175,504. VLCC routes 9 Nov: MEG–China 1,285,922, WAF–China 493,106, USG–China 415,390. Suezmax routes 9 Nov: WAF–Cont 207,106, BSea–Med 472,463, MEG–Med 672,326, Guyana–ARA 186,278. Aframax routes 9 Nov: North Sea 219,773, Kuwait–Singapore 385,505, Carib–USG 89,559, SEA–Aus 174,820, Cross-Med 92,619, USG–UKC 83,176, ECMex–USG 97,129. Products 9 Nov: TC1 294,560, TC15 73,546, TC20 292,594, TC5 212,207; MR Atlantic 72,782, Pacific 85,542. Values 9 Nov: newbuild 131.5 / 90.5 / 78 / 62.5 / 52.5; VLCC resale 230, 5-yr 210, 10-yr 190; Suezmax 150 / 130 / 115; Aframax 105 / 90 / 77; MR2 60 / 53 / 43. S&P (*Rising Sun 1* $126m, *Sponde* $110m, *Haima* $65m, MR2 resales). Newbuilding tables (sizes and buyers realigned `[A]`); no tanker demolitions | Data to 23 Oct / 30 Oct / 6 Nov |
| Intermodal Weekly Market Report weeks 44 and 45 (PDFs via Hellenic Shipping News) | 1-yr / 3-yr TC, rebuilt row by row (each row checks on its 2024/2025 averages and diff): 6 Nov VLCC 270,000 / 125,000; Suezmax 170,000 / 77,250; Aframax 100,000 (−2,500) / 53,250; Panamax/LR1 67,000 (+7,000) / 39,500; MR 43,000 (+2,000) / 27,750; Handy 31,250 / 19,000. 30 Oct: VLCC 270,000 (−25,000) / 125,000 (−4,000); Suezmax 170,000; Aframax 102,500 / 53,250; Panamax 60,000; MR 41,000 / 27,250. Newbuilding: JP Morgan 2 VLCC Hanwha $133m 2030; Venergy 2 + 2 × 306k Hengli 2029; CSET 6 + 4 VLCC (COSCO Yangzhou, DSIC) 2029–30; Stealth 2 VLCC Hanwha $133m 2030 and 2 LR2 HD Hyundai $78m 2029–30; Laskaridis 2 LR2 Hengli 2028; Leon 2 × 50k COSCO Guangdong $52.9m 2029. 5-yr values November average: VLCC 220, Suezmax 150, Aframax 95, LR1 75 | Data to 30 Oct / 6 Nov |
| Compass Maritime Weekly, 9 Nov (PDF) | 12-month TC: VLCC 254,250 (253,250 last week); Suezmax 156,250; Aframax 86,250; LR1 68,500; MR 39,500. Deliveries 2026 / 2027 / 2028: VLCC 5 / 68 / 107; Suezmax 8 / 50 / 78; Aframax 16 / 81 / 82; Panamax 3 / 30 / 20. S&P to ADNOC L&S: *Eurospirit* $153m, *Olympic Lady* ~$185m, *Sponde* $110m, *Zouzou N* $103m. Values table misaligned (not used) | 9 Nov |
| Fearnleys Weekly week 46 (fearnpulse.com, in-app browser) | VLCC commentary (TD22 $41.67m Baltic; $36m report denied; TD34 WS411; Fujairah/Japan WS360; $350–400k/day); Suezmax and Aframax commentary. Spot WS: MEG/West 625, MEG/Japan 1,025, MEG/Singapore 1,050, WAF/FEast 375, WAF/USAC 300, Sidi Kerir/WMed 390, N.Afr/Euromed 270, UK/Cont 250, Caribs/USG 285. 1-yr TC eco/scrubber: VLCC 210,000 (−10,000), Suezmax 155,000 (−10,000), Aframax 95,000 (−5,000). VLCCs fixed 45, available MEG 99. Newbuild 130 / 87 / 74 / 49.5; 5/10-yr VLCC 215 / 190, Suezmax 135 / 110, Aframax/LR2 94.5 / 77. "Brent Spot" not used | 11 Nov |
| Amplify BWET holdings (in-app browser) | TD3C lots / value: Nov 127 / $25,920,319; Dec 122 / $19,724,960; Jan 120 / $11,316,600; Feb 125 / $10,074,375; Mar 125 / $9,556,875 → $204.10 / 161.68 / 94.31 / 80.60 / 76.46 per t → TCE ≈ 1,094 / 855 / 476 / 399 / 376k `[A]` ((price × 270,000 − $2.6m) ÷ 48). TD20: Nov 45 / $2,947,995; Dec 20 / $1,205,000; Jan 45 / $2,230,245; Feb 45 / $1,729,980; Mar 45 / $1,469,745 → $65.51 / 60.25 / 49.56 / 38.44 / 32.66 per t → TCE ≈ 181 / 161 / 120 / 78 / 55k `[A]` (3.826 × price − 69.6, fitted on the 24 Oct conversions) | Holdings 13 Nov |
| IMF PortWatch API | Daily tanker transits and capacity (weekly averages above) | To 8 Nov |
| [gCaptain / Bloomberg, "Oil traders in talks with US to get sanctioned ships back to sea"](https://gcaptain.com/oil-traders-in-talks-with-us-to-get-sanctioned-ships-back-to-sea/) | Trafigura, Vitol, Mercuria, ADNOC seek licences for ~50 of ~1,600 sanctioned ships; none granted; US-sanctioned ships 1,568 incl. 462 crude tankers (4 Nov) | 8 Nov |
| CAPT announcement via `docs/capt-analysis.md` (news note 8 Nov) | *Amor* (2026 dual-fuel Suezmax) 15-month TC from Nov 2026, revenue $73.1–82.2m (~$160–180k/day gross), subject to vetting | 6 Nov |
| Carried from earlier baselines (details in git) | Frontline Q2 release (orderbook 304 / 182 / 221; age shares); Allied (fleet counts); Hafnia Q2 deck (dwt schedule); BRS/Clarksons/Signal (VLCC schedule); BIMCO, Drewry, Galbraiths (scrapping, sanctioned shares); McQuilling via Scorpio 20-F; Gibson 16 Oct (sanctioned by segment); Xclusiv 12 Oct (dwt orderbook ratios, deliveries) and 19 Oct (Signal product data, Liquimar, Emarat); Splash247 20 Oct (licence programme counts); Clarksons shuttle model; Argus (LR2 switching) | Feb–Oct 2026 |
| Rejected or not used | Gibson clean text WS400/450 (conflicts with its table and the Baltic). Compass values table (misaligned). Intermodal LR1 5-yr November average 75 (+10%, single source; held). Xclusiv TC2/TC6 text (template error). Fearnleys "Brent Spot". Clarksons "2027 USG–China FFA $213k" from search (undated) | — |
