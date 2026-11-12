# Oil Shipping BBB — 24 October 2026

## Metadata

- Analysis date: 24 Oct 2026 (Saturday). Status: **Final**. Skill: `oil-shipping-bbb` revision **2026-10-24.1**.
- Latest inputs:
  - Baltic tanker roundup week 43 (23 Oct).
  - Gibson weekly 23 Oct (spot and Q4 FFA to 22 Oct).
  - BWET holdings (page dated 26 Oct; prices ~23 Oct).
  - Fearnleys week 43 (21 Oct).
  - Intermodal week 42 (data to 16 Oct).
  - Xclusiv 19 Oct (data to 16 Oct).
  - Compass 19 Oct.
  - IMF PortWatch to 18 Oct.
- Not yet available: Xclusiv 26 Oct. The week-of-23-Oct segment averages are therefore estimated from the Baltic routes `[A]`.
- **Oldest inputs:** the McQuilling orderbook by segment and year (Feb 2026; shape only, **stale**); the Allied fleet counts (Jul); the Frontline orderbook in vessels (11 Aug; **stale** for a count, cross-checked against the Xclusiv dwt ratios of 12 Oct and the Compass delivery counts).
- Previous baseline: 17 Oct 2026 (7 days; addenda 17 and 22 Oct without value changes). Window: stub Q4-26 + 2027–2029.
- **Stale after 23 Nov 2026**, or earlier on any of:
  - OPEC+ (1 Nov) or the US midterms (3 Nov);
  - the USTR/China port-fee deadline (9–10 Nov);
  - OFAC approvals for more than 30 sanctioned VLCCs;
  - a new Oil Market BBB.
- Oil Market BBB used: baseline **24 Oct 2026, status Final** (not stale). Its "For downstream skills" section asks for this update.
- Series (skill Benchmarks), unchanged:
  - Spot TCE = segment average for a modern vessel, $/day, nominal, period average. Primary publisher: Xclusiv "average T/CE" for VLCC, Suezmax and Aframax.
  - Product tankers use labelled Baltic route proxies: LR2 = TC1 (blended with dirty-trading LR2s), LR1 = TC5, MR = MR Atlantic/Pacific baskets.
  - Period rates: Intermodal (primary), Fearnleys and Compass (cross-checks). Asset values: Xclusiv.
- **Stub method, applied as the skill defines it (revision 2026-10-24.1):**
  - Quarter-to-date segment average, plus the rest of the quarter scaled by the paper's own path (BWET monthly contracts or Gibson Q4).
  - The shortcut used on 10 and 17 Oct (route Q4 FFA × a segment/route ratio from one day) is now a cross-check only. It broke when a route diverged from its segment: TD25 against the Aframax average this month, and TD3C against the VLCC average.
- Tags: `[F]` fact · `[E]` external forecast or secondary · `[A]` own assumption · `[?]` unknown.

## Conclusion

- **BBB changed for the stub only. VLCC 850 → 700; Aframax 245 → 305.** Suezmax (465), LR2 (220), LR1 (120) and MR (55) are kept. Unchanged:
  - 2027, 2028 and 2029 in all scenarios;
  - the Year-1 quarters;
  - mid-cycle TCE and asset values.
- **VLCC:** the segment is falling faster than TD3C.
  - In the week to 23 Oct, Baltic TD34 (Gulf of Oman–China) fell 22% to $657k, TD15 24% and TD22 19%; TD3C fell only 6% to $1.29m.
  - TD34 has tracked the segment average within 3–6%, so the segment is now ~$685k, against $937k on 9 Oct.
  - Brokers agree. Fearnleys: lists "littered with trader- and oil company relets", 105 VLCCs available in the MEG and "profit taking". Gibson: a "significant decrease" on TD34 on healthy tonnage.
  - The TD3C paper barely moved: Q4 $1.22m, Q1-27 ~$0.86m. The paper is holding the Gulf risk premium while the ships that load outside the Gulf get cheaper.
- **Aframax:** the 17 Oct mark (245) used TD25 paper on its lowest day.
  - TD25 Q4 paper has since risen 18% (to $230.5k), and the Med and North Sea held the segment well above TD25 (Baltic TD19 $383k, TD7 $482k).
  - Re-marked on the segment's own October average and the paper's path.
- **Period market now at Base in every segment.** Measured over the months a charter actually runs (from November), the period rates sit at:

| Segment | 1-yr TC, % of Base over the same 12 months | 3-yr TC, % of Base over the same 36 months |
|---|---|---|
| VLCC | 79–108% | 106% |
| Suezmax | 76–107% | 94% |
| Aframax | 89–93% | 88% |
| LR1 | 102–104% | 101% |
| MR | 97–111% | 90% |

  - On 10 Oct the 1-yr TC sat at 61–76% of Base. The shift comes from higher period rates (Intermodal VLCC 1-yr 300, 3-yr 130; Suezmax 1-yr 180) and the lower VLCC stub.
  - No gap exceeds 20%, and no segment's period market points away from Base.
- **Why 2027–29 are kept:**
  - Spot and near paper are falling (Atlantic, Gulf of Oman, TD20) while period rates rose. The two cancel.
  - The oil baseline has Middle East oil incl. bypass above pre-war (> 24 mb/d), with ~40% of Gulf crude bypassing Hormuz and > 1 mb/d moving ship to ship. More cargoes and the same inefficiency are what Base assumes for H1-27.
  - The US programme for sanctioned tankers is now policy, but analysts count only 14–24 VLCCs that could realistically return (Kpler, Braemar, Arrow). That is inside Base's < 30 cap.
- **Base, crude tankers:** the crisis structure lasts through H1-27 and unwinds in H2-27. The delivery wave (~290 VLCCs in 2027–29, ~38% of the compliant fleet) then sets 2028–29, with 2029 as the trough. **VLCC 180 → 50 → 36** (mid-cycle 44); **Suezmax 115 → 44 → 30** (mid-cycle 33).
- **Base, product tankers:** product cargo volumes are down (−10.9% y/y, Signal), but rates are set by tonnage: clean LR2 participation is −39%. Gulf product exports recover slowly. The 2028–29 delivery peak and LR2s returning to clean trade bring rates to near parity. **LR2 65 → 38 → 35; LR1 45 → 30 → 28; MR 37 → 25 → 22.**
- **Main Bear catalyst:** an Iran–USA deal plus recession; the deal is still remote. Supply leg: a wider US approval of sanctioned tonnage (> 30 VLCCs). Then the delivery wave meets slack demand.
- **Main Bull catalyst:** US strikes after 3 Nov (a second carrier is heading to the region) and retaliation against Saudi export infrastructure, which the Houthi strikes inside the kingdom have brought closer. Or suspension of the Gulf of Oman STS hub. Fleet fragmentation if the USTR/China port fees return on 10 Nov.

## Interface — spot TCE, $k/day, period average (point values; ranges below)

| Segment Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| VLCC | **700 / 700 / 700** | 70 / 180 / 480 | 26 / 50 / 150 | 24 / 36 / 90 | 36 / 44 / 55 |
| Suezmax | 465 / 465 / 465 | 50 / 115 / 300 | 27 / 44 / 108 | 25 / 30 / 70 | 27 / 33 / 41 |
| Aframax | **305 / 305 / 305** | 36 / 65 / 160 | 29 / 38 / 72 | 25 / 35 / 55 | 24 / 30 / 37 |
| LR2 | 220 / 220 / 220 | 36 / 65 / 160 | 29 / 38 / 72 | 25 / 35 / 55 | 24 / 30 / 37 |
| LR1 | 120 / 120 / 120 | 28 / 45 / 100 | 23 / 30 / 48 | 20 / 28 / 38 | 20 / 25 / 31 |
| MR | 55 / 55 / 55 | 22 / 37 / 58 | 19 / 25 / 33 | 17 / 22 / 27 | 17 / 21 / 26 |

**Stub (identical in all scenarios):** October segment average (actual weeks plus an estimate for the last week) and November–December scaled by the paper's path.

- **VLCC → 700** (range 650–780; was 850):
  - **October:** Xclusiv segment averages 786.2 (2 Oct), 936.6 (9 Oct), 883.4 (16 Oct) `[F]`.
    - 23 Oct ≈ 685 `[A]`: TD34 $656,587 × 1.03–1.055, the TD34/segment relation on 9 and 16 Oct.
    - October ≈ 800 including the last week `[A]`.
  - **Nov–Dec:** BWET TD3C Nov / Dec ≈ $1.20m / $1.14m `[A]`. That is 0.91 × TD3C spot of $1.29m (Baltic, 23 Oct), so the segment is ≈ 685 × 0.91 ≈ 620.
  - **Q4** ≈ (800 + 2 × 620) ÷ 3 = 680, rounded to 700 because the 23 Oct segment level is estimated. Xclusiv (26 Oct) will test it.
  - **Cross-checks:** the Gibson Q4 FFA ($1,222,750) × the 16 Oct Xclusiv ratio (0.637) = 778; × the 23 Oct TD34/TD3C ratio (0.51 × 1.04) = 648.
- **Suezmax kept at 465** (computed 480–515, +3–10%, at or below the minimum change):
  - October segment 619.9 / 699.9 / 700.1 `[F]`, plus ~590 `[A]` for 23 Oct: TD20 −22%, TD33 −21%, TD6 −2% (Baltic). October ≈ 650.
  - BWET TD20 Nov / Dec ≈ $365k / $249k against TD20 spot of $407k (Baltic, 23 Oct). Applied to the segment, Q4 ≈ 480–515.
  - The ratio cross-check (Gibson TD20 Q4 $366k × 1.37) gives 501.
- **Aframax → 305** (range 290–380; was 245):
  - October segment 276.9 / 384.7 / 328.3 `[F]`, plus ~315 `[A]` for 23 Oct. Baltic: TD7 $481.5k (−1%), TD19 $382.8k (+15%), TD25 $197k (−16%), TD26 $231.5k (−24%), TD9 $210k (−23%), TD28 $302k (−10%); Asia ~$229k (Gibson). October ≈ 325.
  - Nov–Dec: TD25 Q4 paper $230.5k (Gibson, 22 Oct; +18% w/w) against a TD25 October average of ~$245k gives Nov–Dec at ~0.91 × October, so the segment is ≈ 296.
  - Q4 ≈ 306 → 305. The ratio cross-check (230.5 × 1.654, 16 Oct) gives 381.
  - **Why 245 was too low:** it multiplied TD25 paper from 15 Oct ($194.75k, the low) by the 9 Oct ratio. TD25 then diverged further from the segment, which the North Sea, Med and Asia held up.
- **LR2 `[A]`, kept at 220:**
  - ~60% of LR2s trade dirty at the Aframax mark (305 → 183).
  - The clean ~40% earn: TC1 $313k and TC20 $336k (MEG); TC15 Med–East fell to $115k (Baltic, 23 Oct).
  - The clean component is scaled by the TC1/TC15 average since 10 Oct (+25%) → 50. Total ≈ 233 (+6%), below the minimum change.
- **LR1 `[A]`, kept at 120:**
  - TC5 Q4 FFA $190,250 (Gibson, 22 Oct; −3.5% w/w) × ~0.6 for West LR1 legs = 114 (−5%).
  - Spot is firmer: TC5 $229.9k (Baltic) / $244.8k (Gibson); TC8 $250.5k.
- **MR `[A]`, kept at 55:**
  - Baltic MR Atlantic basket $65.8k (23 Oct). Xclusiv MR Pacific basket $81.0k (16 Oct).
  - Q4 FFA: TC7 $51.75k, TC18 $42.75k. These are offsetting moves.
- **Confidence:** medium for VLCC (the 23 Oct segment level is estimated) and Suezmax; low for Aframax and products.
- **Data checks:**
  - Gibson's clean commentary has TC1/TC5 at "WS500/WS510" while its table has WS1,075/1,105. The Baltic agrees with the table, so the text is not used.
  - Baltic TD27 TCE "$148,500" is inconsistent with its WS740 (copy error); not used.

## Interface — asset values, $m

| Segment | Newbuild now | 5-yr now | 10-yr now | 5-yr mid-cycle Bear / Base / Bull | Newbuild mid-cycle Base |
|---|---|---|---|---|---|
| VLCC | 131.5 | 210 | 185 | 93 / 121 / 160 | 130 |
| Suezmax | 90.5 | 125 | 110 | 64 / 84 / 112 | 90 |
| Aframax | 78 | 85 | 72.5 | 54 / 75 / 100 | 77 |
| LR2 | ~80 `[A]` | 85 | 72.5 | 52 / 73 / 98 | 79 |
| LR1 | 62.5 | 68 | 48 `[E]` | 42 / 59 / 80 | 61 |
| MR | 52.5 | 52 | 42 | 32 / 46 / 64 | 51 |

- **Sources for "now":**
  - Xclusiv 19 Oct (data to 16 Oct) `[F]`. Newbuild prices are South Korean yards; secondhand values are Japanese-built.
  - LR1 5-yr: Intermodal October average (68.3) `[F]`. LR1 10-yr: KOBC (3 Sep) `[E]`. LR2 newbuild: Aframax + ~$2m `[A]`.
- **Change vs 12 Oct:** VLCC newbuild 131 → 131.5 and Suezmax 91 → 90.5; all secondhand values unchanged.
- **Cross-checks:**
  - Fearnleys (21 Oct): VLCC 205 / 180, Suezmax 125 / 105, Aframax/LR2 86 / 75.5; newbuild VLCC 130, Suezmax 87, Aframax 74, MR 49.5.
  - Intermodal October 5-yr averages: VLCC 216.7, Suezmax 135, Aframax 88.3, MR 52.7.
  - Compass (19 Oct, unchanged): VLCC 197, Suezmax 123, Aframax 91, MR 51.
- **S&P `[F]`** (Xclusiv 19 Oct):
  - Suezmaxes: *Zouzou N* (150k, 2010) $103m, a record for its age (also TradeWinds, 21 Oct); *Maran Poseidon* (158k, 2010) $98.5m.
  - Coated Aframax *Afra Mare* (105k, 2008) $59m to Chinese buyers.
  - MR2 *Prive Angel* (51k, 2008) $24.5m, prompt Fujairah delivery.
  - Old Suezmaxes are selling at ~94% of Xclusiv's 10-yr value. At $103m a buyer of the 2010 ship pays for at least Base's front-loaded earnings `[A]`.
- **Mid-cycle values (unchanged) `[A]`** = (mid-cycle TCE − opex) × 355 days, discounted over 20 years at 8%, plus the present value of scrap.
  - Opex in $k/day: VLCC 10.5, Suezmax 9.5, Aframax 9.0, LR2 9.5, LR1 8.5, MR 8.0.
  - Scrap at ~$510/ldt; Baltic recycling assessments for tankers are ~$480–530 (Compass).
- **Value risk:** the US now allows approved buyers to take over sanctioned tankers. That adds supply of old, mostly VLCC tonnage to the S&P market and can weigh on old-VLCC values.

## Scenario definitions

| Scenario | Weight (convention) | Oil BBB scenario used | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|
| **Bear** | 25% | Oil Bear, **demand variant** (Iran–USA deal + recession) | **Demand:** a deal lifts the blockade; shuttles, STS and Cape routing end; the Red Sea reopens; recession cuts cargoes. **Supply:** deliveries arrive on time, Iranian shadow VLCCs return and attacked ships come back from repair. A wide US approval programme returns sanctioned VLCCs to compliant trade even without a deal | Ton-days fall faster than volumes recover. The delivery wave meets slack demand; rates are below newbuild parity in 2028–29 | Q1 2027 (approvals: from Nov 2026) | Ceasefire > 60 days · STS/shuttle share < 2% of the VLCC fleet · STS time < 7 days · Bab el-Mandeb tankers > 18/d · VLCC 1-yr TC < $90k · TD3C Q1-27 FFA < $300k/d · PMIs < 48 · **> 30 sanctioned VLCCs approved for mainstream trade** |
| **Base** | 50% | Oil Base (armed normalisation; crude via bypass and escort; Gulf and Gulf of Oman contested) | ME oil incl. bypass ~22–24 mb/d (crude ~15–16) reaches market via East–West/Yanbu and escorted shuttles with STS. Episodic attacks, incl. on STS anchorages and in the northern Gulf; no deal. Gulf products are repaired through 2027; ~1 bn bbl of restocking; China imports recover. US approval of sanctioned tankers stays small (14–24 VLCCs on analyst counts) | Shuttle and STS inefficiency (+6% VLCCs per mb/d on MEG–Far East; ~10-day STS; ~40% of Gulf crude bypassing Hormuz) and attack downtime last through H1-27 and ease in H2-27. US→Asia long-haul is capped by freight. Restocking (~3–4% of the VLCC fleet a year) partly absorbs ~290 VLCC deliveries in 2027–29 | Ongoing | VLCC 1-yr TC below $150k by Q2-27 · TD3C Q1-27 FFA below $0.7m by end-Dec · STS time back to 5–7 days · Bab el-Mandeb tankers 8–15/d · VLCC exits from compliant trade ≥ 10 in 2028 and ≥ 25 in 2029 · LR2 dirty share < 50% during 2027 · sanctioned VLCCs approved < 30 |
| **Bull** | 25% | Oil Bull (US strikes after 3 Nov; retaliation against Saudi/Gulf export infrastructure; escort/STS system fails) | **Demand:** the escort and shuttle system fails (the Sohar/Fujairah STS hub is suspended); Gulf barrels are replaced by Atlantic long-haul; cargo splitting and STS persist. **Supply:** attacked tankers idle ~2 months each; yard slippage; USTR/China port fees return on 10 Nov and split the fleet | Ton-days rise while volumes fall, as in Mar–Oct 2026. Inefficiency absorbs the delivery wave until 2028 | Nov 2026 | Hormuz crude < 8 mb/d for two weeks · STS hub suspended · Saudi export facility hit with lasting loss · Bab el-Mandeb tankers < 5/d · VLCC 1-yr TC > $250k on all sources · TD3C Q1-27 FFA > $1m/d · USTR fees reinstated |

**Mapping note `[A]`:**
- The **oil Bear supply variant** (OPEC+ market share with contango) is a crude-tanker Bull risk inside the oil Bear. It is not used as the shipping Bear.
- **Oil Base (24 Oct)** has ME oil incl. bypass above pre-war. For tankers that means more cargoes with the same bypass and STS inefficiency, which is what Base 2027 rests on.
- **Sanctioned-tanker approvals** sit outside the oil scenarios. They are a shipping supply catalyst, combined with oil Base or oil Bear, and they add tonnage, not barrels.
- **New Bull signpost** from the oil baseline: a Saudi export facility hit with a lasting loss.

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

- Unchanged since 10 Oct. The 2028–29 crude paths rest on exits consistent with Base rates and on growth measured on the compliant fleet (see Fleet supply).
- **Segment order in 2029 Base (VLCC 36 > Aframax 35 > Suezmax 30)** is a supply effect. Aframax/LR2 has the smallest orderbook and the oldest, most sanctioned fleet (25%, Gibson). Its 2029 compliant growth is ~+3%, against ~+5.6% for Suezmax. Mid-cycle keeps the normal order.
- **Bull 2029 still flagged:** VLCC 90 / Suezmax 70 need crisis inefficiency to last through 2029.

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

- LR2 = Aframax from 2027 `[A]`. Unchanged since 10 Oct.
- **The product rally is a tonnage story** (Xclusiv/Signal, 1 Aug–15 Oct vs a year earlier) `[E]`:
  - Seaborne product shipments are −10.9% (clean −12.1%).
  - Clean-trading LR2s are −39.2% (158 ships) and clean LR1s −9.6% (208).
  - Crude-trading Aframaxes are +20.3% (858) and crude-trading Panamaxes +18.6% (134).
  - Argus counted 113 LR2s switching clean → dirty in Jan–Aug, against 67 in all of 2025.
  - Base assumes they return to clean trade in H2-27, which is the main reason product rates fall to near parity in 2028–29. Returning requires tank cleaning, so the supply response lags.
- **LR1 2029 (28 vs parity 25):** LR1 has the lightest product orderbook (~15%). Its period market is at Base (1-yr 102–104%, 3-yr 101%). Kept.

## Year 1 by quarter ($k/day)

Shape `[A]`, unchanged:
- **VLCC Q1 (Base 400):** below the Q1-27 TD3C paper (~$0.86m on TD3C). That is ≈ $455–550k segment-equivalent at a segment/TD3C ratio of 0.53 (23 Oct, TD34-based) to 0.64. BWET holds 125 lots per month. Base assumes no escalation after 3 Nov.
- **Suezmax Q1 (Base 230):** above the thin TD20 paper (Jan ~$167k on TD20; 40 lots). Supported by the period market (1-yr 165–180 = 98–107% of Base over the same months).
- **Other segments:** fade with inefficiency. MR, Aframax/LR2 and LR1 get a Q4 seasonal uptick.
- Each row averages to the scenario's 2027 value.

| Scenario | VLCC Q1 / Q2 / Q3 / Q4 | Suezmax | Aframax | LR2 | LR1 | MR |
|---|---|---|---|---|---|---|
| Bear | 150 / 60 / 40 / 30 | 90 / 45 / 35 / 30 | 55 / 35 / 28 / 26 | 55 / 35 / 28 / 26 | 38 / 28 / 24 / 22 | 28 / 21 / 19 / 20 |
| **Base** | **400 / 160 / 90 / 70** | **230 / 115 / 65 / 50** | **114 / 63 / 43 / 40** | **114 / 63 / 43 / 40** | **69 / 44 / 33 / 34** | **48 / 36 / 31 / 33** |
| Bull | 800 / 500 / 350 / 270 | 500 / 300 / 220 / 180 | 260 / 160 / 115 / 105 | 260 / 160 / 115 / 105 | 150 / 100 / 80 / 70 | 75 / 58 / 50 / 49 |

## Market check

| Segment | Spot latest / proxy | 1-yr TC | 3-yr TC | FFA Q4 / Q1-27 / Cal | Base 2027 / 3-yr avg | Gap > 20% |
|---|---|---|---|---|---|---|
| VLCC | 883 avg (16 Oct, Xclusiv); ~685 est. (23 Oct); TD3C 1,288, TD34 657 (23 Oct, Baltic) | 300 (Intermodal 16 Oct); 268.75 (Compass 19 Oct); 220 (Fearnleys 21 Oct) | 130 (Intermodal; +22%, one source) | TD3C Q4 1,223 (Gibson 22 Oct) `[F]`; Q1 ~861 `[A]`; Cal `[?]` | 180 / 88.7 | No (1) |
| Suezmax | 700 avg (16 Oct); TD20 407, TD6 871 (23 Oct) | 180 (Intermodal, +16%); 165 (Fearnleys); 128 (Compass, sticky); fixture 150 (NAT, 21 Oct) | 77.25 (Intermodal); fixtures 80 (13 Oct) | TD20 Q4 366 `[F]`; Q1 ~117 on TD20 `[A]` (thin) | 115 / 63.0 | No (1) |
| Aframax | 328 avg (16 Oct); TD25 197, TD19 383, TD7 482 (23 Oct) | 99 (Intermodal); 100 (Fearnleys); 96 (Compass) | 53 (+10%) | TD25 Q4 230.5 `[F]`; Q1 `[?]` | 65 / 46.0 | No (1) |
| LR2 | TC1 313, TC20 336, TC15 115 (23 Oct, Baltic) | — (Aframax used) | — | `[?]` | 65 / 46.0 | As Aframax |
| LR1 | TC5 230 (Baltic) / 245 (Gibson); TC8 251 | 60 (Intermodal); 61 (Compass) | 39.5 | TC5 Q4 190.25 `[F]` | 45 / 34.3 | No (1) |
| MR | Atlantic basket 65.8 (23 Oct); Pacific 81.0 (16 Oct); TC7 78, TC18 62 (Gibson) | 45 (Intermodal); 39.5 (Compass) | 26.75 | TC7 Q4 51.75; TC18 Q4 42.75 `[F]` | 37 / 28.0 | No (1) |

(1) **Period rates against Base over the months they run** (skill rule: from the delivery month, here November):
- **Nov–Dec months used `[A]`:** VLCC ~650, Suezmax ~370, Aframax ~296, LR1 ~116, MR ~55. These follow from each stub and its October average.
- **The sums:** 12 months = Nov–Dec + 2027 Q1–Q3 + Oct-27. 36 months = Nov–Dec + 2027 + 2028 + Jan–Oct 2029.

| Segment | 1-yr TC (sources) | Base Nov-26 → Oct-27 | 1-yr ÷ Base | 3-yr TC | Base Nov-26 → Oct-29 | 3-yr ÷ Base |
|---|---|---|---|---|---|---|
| VLCC | 220 / 268.75 / 300 | 277 | 79% / 97% / 108% | 130 | 123 | 106% (87% at the previous 106.25) |
| Suezmax | 128 / 150 (fixture) / 165 / 180 | 168 | 76% / 89% / 98% / 107% | 77.25; fixtures 80 | 82 | 94%; 98% |
| Aframax | 96 / 99 / 100 | 108 | 89% / 92% / 93% | 53 | 60.5 | 88% |
| LR1 | 60 / 61 | 58.6 | 102% / 104% | 39.5 | 39.2 | 101% |
| MR | 39.5 / 45 | 40.7 | 97% / 111% | 26.75 | 29.8 | 90% |

- **Reading:**
  - Every segment's period market prices the next 12 and 36 months at 76–111% of Base: at Base, with a normal risk discount at the low end and a small premium at the high end.
  - On 10 Oct the 1-yr TC sat at 61–76% of Base (different window).
  - **The period market no longer argues for cutting Suezmax 2027 or for cutting the crude late window.** It does not argue for raising any path either.
- **Trigger (Suezmax 1-yr +16%, Intermodal 155.25 → 180):**
  - Tested: it takes the Suezmax 1-yr from below Base to ~107% of Base over the same months.
  - Other sources: Fearnleys 165 (98%), NAT fixture 150 (89%), Braemar/MB assessments 180–198, Compass 128 (sticky).
  - Spot and near paper are falling (TD20 −22% in a week; Q1 TD20 paper ~$117k). Mixed evidence → Suezmax 2027 (115) kept.
- **VLCC 3-yr +22% (106.25 → 130):** above the 10% plausibility limit, and only one source. It is held as unconfirmed. At the previous 106.25 the 3-yr is 87% of Base, so the reading does not depend on it.
- **Q1-27 paper:**
  - VLCC: Base 400 is ~10–27% below the paper-equivalent (455–550). The gap narrows as the segment falls further below TD3C.
  - Suezmax: Base 230 is ~10% above the Jan TD20 paper scaled to the segment (167 × 1.37 = 229 for Jan; Q1 ~160).

**Company cross-check (DHT, 12 Oct) `[F]`:** ~50% of Q4 spot days booked at $509,100/day (discharge-to-discharge). The segment's fall since mid-October brings the market mark (700) closer to that booked level. No change to the method: company realisation stays in the company analysis.

**Cal-28 / Cal-29 FFA:** not available `[?]` (paid data). The 2028–29 market test uses the period-TC term structure below.

**Period-market term structure `[A]`** (Intermodal 16 Oct). The forward TC for Oct-27 → Sep-29 is F = (3 × TC3 − TC1) ÷ 2, compared with Base over the same two years: (Q4-27 × 0.25 + 2028 + 2029 × 0.75) ÷ 2.

| $k/day | TC1 / TC3 | Implied F | Base, same window | F ÷ Base (9 Oct) | Reading |
|---|---|---|---|---|---|
| VLCC | 300 / 130 | 45.0 | 47.3 | **0.95** (0.52) | At Base. The 3-yr rise (one source) moved F from well below Base to Base |
| Suezmax | 180 / 77.25 | 25.9 | 39.5 | 0.66 (0.85) | Below Base: the 1-yr rose more than the 3-yr |
| Aframax (LR2 proxy) | 99 / 53 | 30.0 | 37.1 | 0.81 (0.62) | Below Base, closer |
| LR1 | 60 / 39.5 | 28.25 | 29.75 | 0.95 (0.95) | At Base |
| MR | 45 / 26.75 | 17.6 | 24.9 | 0.71 (0.72) | Below Base; does not support raising MR |

- F is a direction check, not a level: the 1-yr TC is discounted against today's spike, and the 3-yr is thin and sticky.

**Anchors `[A]`** (8% nominal, 25 years, 355 days, opex as above, scrap ~$510/ldt):

| $k/day | VLCC | Suezmax | Aframax | LR2 | LR1 | MR |
|---|---|---|---|---|---|---|
| Newbuild-parity TCE | 44 | 33 | 29 | 30 | 25 | 21 |
| Asset-implied TCE (5-yr value, 20 years left) | 69 | 45 | 33 | 34 | 27 | 23 |
| 1-yr TC average 2024 / 2025 (Intermodal) `[F]` | 50.4 / 50.6 | 45.4 / 38.1 | 45.2 / 33.9 | — | 37.8 / 25.2 | 30.8 / 21.9 |
| Opex-level floor | ~10.5 | ~9.5 | ~9 | ~9.5 | ~8.5 | ~8 |

- **Asset market:** the VLCC asset-implied TCE (69) prices a longer windfall than Base; the Q4-26 and 2027 windfall explains most of it.
- **Long-run reference:** VLCC 10-year average ~$35k `[E]` (Clarksons via press). Company cash breakeven ~$24k/day (Frontline) `[F]`.

## Drivers

### Oil input and translation (oil scenario mapping; table of shipping effects)

From `docs/oil-market-bbb.md` (24 Oct, Final). All Brent and crack paths are unchanged; the stub is 109.2.

| Oil input (oil BBB, 24 Oct) | Shipping effect |
|---|---|
| Kpler (week to 18 Oct): ME oil via Hormuz plus alternative routes > 24 mb/d (pre-war 23.3); strait ~14 mb/d incl. Gulf of Oman transfers (82% of pre-war; +20% w/w). ~40% of non-Iranian Gulf crude bypassed Hormuz in September (17% pre-war). Citi: > 1 mb/d ship to ship | Volumes are back to pre-war while the inefficiency stays: bypass via Yanbu and Fujairah, shuttles, STS. That is more ton-days per barrel than pre-war, and it supports Base H1-27. Spot is falling anyway because relets and ballasters have filled the lists (supply, see Trade flows) |
| Attacks: IRGC claims four tankers hit doing STS in the northern Gulf and three on mines (22–23 Oct; unverified, Trump calls it fabricated). Two vessels struck off Saudi Arabia on 16–17 Oct, one by an RPG from a small boat (UKMTO). Kpler: ≥ 18 vessels attacked in two weeks; IMO: 120 since February | STS is now targeted inside the Gulf as well as in the Gulf of Oman. Downtime and owner reluctance persist. Not suspended |
| Houthi strikes inside Saudi Arabia (four in 48 hours); Aramco evacuated Dhahran HQ; Houthis reportedly control Bab el-Mandeb since September (Fortune) | Yanbu exports southbound to Asia face Bab el-Mandeb risk. PortWatch still shows 10 tankers/day (week to 18 Oct). New Bull signpost: a Saudi export facility hit with a lasting loss |
| East–West capacity 7 mb/d (pre-war ~2), expanding to 10 in 2–3 years; last flow 5.8 mb/d (6 Oct) | More Red Sea loadings over time: Suezmax/VLCC from Yanbu to Europe via Suez/SUMED and to Asia via Bab el-Mandeb |
| CENTCOM blockade: 138 ships redirected; Kpler: Iranian floating storage for China ran dry mid-October | Iranian shadow VLCCs idle or redeployed; they stay outside compliant supply in Base |
| ME refined-product exports 1.9 mb/d (IEA Sep; pre-war 4.7); China November quota not reported; Russian diesel: Q3 western exports 510 kt/month vs 3.27 Mt/month a year earlier, October only modestly higher (Gibson) | Product cargo volume stays weak; product rates rest on tonnage (clean LR2/LR1 participation down) |
| Implied stocks: Base 2027 +1.0 to +2.0 mb/d; ~1 bn bbl restocking; M1−M4 +12.95 (tight) | Restocking ~3.5% of the VLCC fleet a year `[A]`; no floating-storage economics |
| Freight cost: VLCC Gulf→China ≈ $35/bbl (Citi, ~22 Oct); Brent–WTI 2027 strip 5.1; Kpler: ~$20/bbl extra resale margin on Iraqi crude | Long-haul arbitrage still capped by freight; the freight shock is priced as fading |
| US approval of sanctioned-tanker sales (Wright, 19 Oct); Bloomberg Intelligence: will not solve the shortage | See Effective tonnage |
| Oil Bull: US strikes after 3 Nov, second carrier; Oil Bear: deal remote | Shipping Bull closer in timing; Bear's deal leg remote |

### Trade flows and demand (ton-days / ton-miles per scenario and year)

- **VLCC `[E]`:**
  - **Fearnleys (21 Oct):** rates shed WS100–150. Lists are "littered with trader- and oil company relets": charterers who took period cover at high rates are reletting into spot. MEG exports "surpassed prewar levels in periods". "The map is not exactly fitting the terrain… something will have to give." A rumoured WS650 Fujairah/East on a relet. 31 VLCCs were fixed in the week (−19), with 105 available in the MEG over the next 30 days (+6).
  - **Gibson (23 Oct):** Atlantic VLCC "subdued", Petrobras fixtures lower day after day, a "significant decrease" on TD34 on healthy tonnage.
  - **Reading `[A]`:** a supply-side correction, as relets and ballasters reach the lists, while cargo volumes are back to pre-war. It fits Base's Q4-26 → Q1-27 step down; it is not yet a demand loss.
- **Suezmax `[E]`:**
  - WAF softened (TD20 WS731, Baltic −22%). Gibson: "the writing on the wall that we have seen the top"; November paper expects further falls.
  - The CPC/Black Sea route stays firm (TD6 ~$871k), but the whole Black Sea is now classified as a war risk zone.
  - Fearnleys: the lack of Fujairah fixing has pushed VLCCs and Suezmaxes into the Atlantic.
- **Aframax `[E]`:**
  - The Med rebounded (TD19 +15%; Gibson "set to last for a while yet").
  - The North Sea found a floor (Fearnleys). US Gulf/Caribbean is down (TD25, TD26, TD9 −16% to −24%). Asia ~$229k (−$33k in two weeks).
- **Products `[E]`:**
  - MEG LR2/LR1 at records (TC1 $313k, TC5 $230k, TC8 $251k; Baltic 23 Oct). TC15 Med–East fell 34% to $115k.
  - MR: firmer in the UKC, Med and East (TC6 Cross-Med $110k; TC7 $78k).
  - Russian diesel to the US: 300 kt in October, then 500 kt (Nov) and 1 Mt (Dec) promised; three MRs reportedly en route. Volumes so far are small (Gibson).
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

- **Oil BBB 24 Oct test:** volumes are back to pre-war earlier than the 17 Oct oil Base implied, which supports the 2027 volume leg (+7). Bypass and STS are unchanged, so the inefficiency leg holds. Net crude Base 2027 stays at about +1 `[A]`.

### Chokepoints (transits vs normal, extra sailing days, fleet share absorbed)

IMF PortWatch, tanker transits per day (AIS), latest data 18 Oct `[F]`:

| Chokepoint | 2023 Jan–Oct | 2026 Jan–Feb (pre-war) | 5–11 Oct | 12–18 Oct | Effect |
|---|---|---|---|---|---|
| Hormuz | 57.4 | 37.0 | 0.6 | 0.6 | AIS dark: use Kpler. Strait ~14 mb/d incl. Gulf of Oman transfers (week to 18 Oct) |
| Gulf of Oman STS hub (Sohar, Fujairah) and northern Gulf STS | — | — | Attack at the Sohar anchorage (11 Oct) | IRGC claims four STS tankers hit in the northern Gulf (22–23 Oct, unverified) | ~40% bypass, > 1 mb/d STS; +6% VLCCs per mb/d (Clarksons); ~10 days per STS |
| Bab el-Mandeb | 26.2 | 12.5 | 8.6 | 10.0 (554 kt/d) | 38% of 2023. Houthis reportedly control the strait; Yanbu→Asia flows still pass |
| Suez | 25.6 | 15.9 | 17.0 (643 kt/d) | 15.9 (841 kt/d) | Steady; larger units |
| Panama | 12.9 | 12.8 | 9.4 | 13.0 (358 kt/d) | Back to normal: the dip lasted one week (no trigger). El Niño dry-season risk from late November |
| Cape of Good Hope | 9.1 (686 kt/d) | 15.1 (893 kt/d) | 17.4 (1,257 kt/d) | 19.3 (993 kt/d) | About 2× 2023: +10–15 days per westbound MEG voyage `[A]` |

### Effective tonnage (per segment, share of fleet unavailable)

| Item | VLCC | Suezmax | Aframax/LR2 | LR1/MR | Source |
|---|---|---|---|---|---|
| Attack damage and downtime | > 3% of the VLCC fleet damaged since March (cumulative). Base assumes 1–2% out at any time `[A]` | Black Sea now a war risk zone | Some | Some | Nortilus (16 Oct); Kpler ≥ 18 attacked in two weeks; IMO 120 since February `[E]` |
| Sanctioned / shadow | 164 sanctioned; 153 OFAC-only; Iran owns 38 | 116; 28 OFAC-only | 322 (25%); 42 OFAC-only | ~40 CPP MRs OFAC-only | Gibson, 16 Oct `[E]`; Xclusiv (5 Jun) cross-check |
| Realistic returns under the US approval programme | **14–24 VLCCs** (Arrow 14, Braemar 19, Kpler 24 of ~160) | None (Arrow) | None (Arrow) | Few | Splash247, 20 Oct `[E]` |
| ≥ 20 years (now → at full delivery) | 18.3% → 29.6% | 22.0% → 32.7% | 22.0% → 39.5% | Panamax/LR1 22.6%, Handy/MR1 37.3% | Frontline (28 Aug) `[F]`; Xclusiv 12 Oct `[F]` |
| Shuttle / STS / escort | Shuttle and STS (+6% per mb/d); ~40% of Gulf crude bypassing | Yanbu STS | ~14 LR2s in shuttle (Aug) | Small | Clarksons; Kpler; Citi `[E]` |
| Clean ↔ dirty | — | — | Clean LR2s −39% (158); 113 switched Jan–Aug | Clean LR1s −9.6% (208); crude-trading Panamaxes +18.6% | Xclusiv/Signal 19 Oct; Argus 15 Oct `[E]` |

**US programme for sanctioned tankers `[E/A]`:**
- **What it is** (Energy Secretary Wright, 19 Oct; Splash247, 20 Oct):
  - The administration "is authorising the sale of sanctioned oil tankers to approved investors" who refurbish them and trade only non-sanctioned oil.
  - An approval process is being developed; no general licence has been published.
  - Wright: "dozens or possibly hundreds" of a ~1,600-ship dark fleet may eventually return.
- **Analyst counts:** Kpler 24 of ~160 OFAC-sanctioned VLCCs; Braemar 19 VLCCs; Arrow Research 22 tankers incl. 14 VLCCs, none in Suezmax or Aframax.
  - BRS: 148 deepsea tankers sanctioned by the US alone (2.5% of the fleet), only 14 idle for more than three months. Most already work in grey trades, and EU/UK rules block insurance.
  - INTERTANKO opposes the programme. Arrow sees freight strength possibly through Q1-27.
- **OFAC keeps designating:** 22 vessels on 8 Oct and 9 on 21 Oct. Two were delisted after ownership changes (*Hakuna Matata*, *Pinocchio*), which shows the route back.
- **Reading `[A]`:**
  - 14–24 VLCCs is 2–3% of the compliant VLCC fleet, inside Base's < 30 cap. Most would take shuttle work and free mainstream VLCCs in H1-27, part of what the falling Gulf of Oman rates already show.
  - It is a Bear supply catalyst only above ~30 VLCCs. 30 would loosen the 2027–28 VLCC balance by ~4 pp; 100 by ~13 pp.
- **Base `[A]`, unchanged:**
  - Attack downtime (1–2%) and shuttle/STS inefficiency last through H1-27 and ease in H2-27.
  - LR2s clean up in H2-27 (+~5% clean supply).
  - Sanctioned ships beyond the approved few stay outside compliant trade.

### Fleet and orderbook register

Updated 24 Oct. The as-of date is in each cell; `[?]` = not sourced. Fleet = total fleet unless stated.

| Segment | Fleet (vessels; m dwt) | Orderbook (vessels; % fleet) | Delivered 2026 YTD | Schedule: rest-26 / 27 / 28 / 29 / 30+ | New orders: Q3-26 / Q4-26 so far | Scrapped: Q3-26 / Q4-26 so far / earlier | ≥ 20 yrs now / at full delivery | Sanctioned / outside compliant trade | Newbuild $m; earliest slot |
|---|---|---|---|---|---|---|---|---|---|
| VLCC | ~907 `[A]` (304 ÷ 33.5%); 277.1m dwt (Allied, Jul) `[F]`; Clarksons 912 (Mar) `[E]` | **304** (Frontline, 11 Aug; stale count) `[F]` = 33.5% of fleet; 32.5% by dwt (Xclusiv, 12 Oct) `[F]`; 38% (Veson, Sep) `[E]` | 31 (Xclusiv, 12 Oct) `[F]` | ~5 / 62 / 125 / 100 / 25 `[A]` (sum 317). Compass (12 and 19 Oct) 11 / 67 / 99 for rest-26 / 27 / 28; Clarksons 64 / 102; BRS 60 / 127 | ≥ 22 reported (Xclusiv); tracker YTD 164–217 `[E]` / 2 confirmed (Scorpio) + 6 unconfirmed (Hengli; not in Xclusiv 19 Oct) | 1 / none / 7 in 2022–26 (Drewry) `[E]` | 18.3% / 29.6% (Frontline, 28 Aug) `[F]` | 164 sanctioned, 153 OFAC-only (Gibson, 16 Oct) `[E]`; 14–24 realistic returns (Splash, 20 Oct) | 131.5 (Xclusiv 19 Oct, Korea); 130 (Fearnleys 21 Oct); Scorpio 135 at Hengli; China late 2028, Korea 2029–30 |
| Suezmax | ~634 `[A]` | **182** (Frontline, 11 Aug) `[F]` ≈ 28.7% `[A]`; 29.6% by dwt (Xclusiv, 12 Oct) `[F]` | 26 to mid-Jul (Xclusiv) `[F]`; since `[?]` | ~15 / 45 / 60 / 50 / 12 `[A]` (sum 182); Compass 15 / 55 / 72; + Liquimar 3 (2029–30) | ≥ 8 (+1 shuttle) / **3 confirmed (Liquimar, 157k, New Hantong, $84m each, 2029–30; Xclusiv 19 Oct)** + 2 unconfirmed (Hengli) | 0 / none / 16 in 2022–26 (Drewry) `[E]` | 22.0% / 32.7% `[F]` | 116, 28 OFAC-only (Gibson) `[E]`; none realistic under the US programme (Arrow) | 90.5 (Xclusiv 19 Oct); 87 (Fearnleys); New Hantong 84 (Liquimar) |
| Aframax/LR2 | **1,239**; 136.9m dwt (Allied, Jul) `[F]` | **221** (Frontline, 11 Aug) `[F]` ≈ 17.8% `[A]`; 20.7% by dwt (Xclusiv, 12 Oct) `[F]` | 47 to mid-Jul (Xclusiv) `[F]`; ~88 for 2026 (Breakwave) `[E]` | ~35 / 60 / 65 / 50 / 16 `[A]` (sum 226); Compass 32 / 82 / 79; McQuilling (Feb) 89 / 79 / 37+ | ≥ 22 (+2 options) / 0 confirmed + 4 LR2 unconfirmed (Hengli) | 2 / none / 23 in 2022–26 (Drewry) `[E]` | 22.0% / 39.5% `[F]` | 322 = 25%, 42 OFAC-only (Gibson) `[E]` | 78 (Xclusiv); LR2 ~80 `[A]`; China 2028–29 |
| LR1/Panamax | **438; 32.0m dwt** (McQuilling, Feb; stale) `[E]` | 13.6% (Galbraiths, Aug) `[E]` + 6 Emarat → ≈ 15% `[A]` | `[?]` | McQuilling 26 / 16 / 18+; Compass 10 / 28 / 18; + Emarat 6 (Q3 2029 per Xclusiv 19 Oct; Splash: 2 in 2029, 4 in 2030) | ≥ 6 / 6 (Emarat; Xclusiv 19 Oct) `[F]` | 0 / none / `[?]` | 22.6% (Xclusiv, 12 Oct) `[F]` / `[?]` | `[?]` | 62.5 (Xclusiv, Korea); China ~55 `[E]` |
| MR (incl. MR1) | **2,978**; 132.0m dwt (Allied, Jul) `[F]` | MR2 19.7% by dwt (Xclusiv, 12 Oct) `[F]`; MR2 304 = 15.3% by number (McQuilling, Feb; stale) `[E]` | 63 MR2 to mid-Jul (Xclusiv) `[F]` | MR2 152 / 111 / 41+ (McQuilling, Feb) + ~120 ordered since → 2028+ ~150 `[A]`; + Top Ships 4 (2029–30) | ≥ 39 (+2 options) / 4 (Top Ships, GSI Nansha; Intermodal 13 Oct) `[E]` | ~4 Handy/MR1 + 1 MR / none / `[?]` | Handy/MR1 37.3% (Xclusiv, 12 Oct) `[F]` | ~40 CPP MRs OFAC-only (Gibson) `[E]` | 52.5 (MR2, Xclusiv); 49.5 (Fearnleys) |

**Aggregates `[F/E]`:**
- **Xclusiv (12 Oct, main segments, dwt):**
  - Fleet 738.9m dwt.
  - Deliveries 32.6m dwt in 2026 to date. Scheduled 50.7m (2027), 61.2m (2028) and 67.5m (2029 and later).
  - 19.8% of the fleet ≥ 20 years.
- **All tankers > 25k dwt (Allied, Jul):** 6,302 ships / 693.05m dwt; orderbook 1,267 ships / 173.32m dwt. H1-26: 193 deliveries, 21 recyclings, 339 contracts.
- **Hafnia/Vortexa (28 Aug) `[E]`:** 161m dwt delivers in 2027–29, against 106m dwt of exits. VLCC + Suezmax deliveries 2027–29: 119m dwt. Handy–LR2/Aframax orderbook 18 / 16 / 17 / 10m dwt for 2026–29.
- **Galbraiths (10 Aug) `[E]`:** record ordering of 96.4m dwt to end-July; removals ~0.5% a year, all VLCC/Suezmax removals sanctioned ships.
- **BIMCO (Aug/Sep) `[E]`:** crude orderbook 27–28%, > 70% delivering 2028+. Product fleet +13% from end-2025 to end-2027; heaviest product tranches 2028–29.

**Schedule check `[A]`:**
- **The spread between sources:**
  - VLCC 2027 / 2028: Compass 67 / 99, Clarksons 64 / 102, BRS 60 / 127. Base 62 / 125 follows BRS. On Compass/Clarksons, 2028 is ~3 pp tighter and 2029 looser: VLCC 2028 ~+5, 2029 ~−3, average unchanged.
  - Suezmax 2027 / 2028: Compass 55 / 72 vs Base 45 / 60.
  - Aframax/LR2 2027: Compass 82 and McQuilling 79 vs Base 60.
  - The differences shift timing (earlier for Suezmax and Aframax/LR2, later for VLCC) rather than the total. No year moves by the minimum change.
- **Xclusiv dwt:** Base matches 2028 (61.2m, within ~3%) and 2029+ (67.5m, within ~4%). 2027 is ~10% light (mostly Aframax/LR2 and small tankers).
- **To do:** re-base the schedule on Frontline's Q3 orderbook count (late Nov) with the Compass, Clarksons and BRS spread.

**Contracting and demolition log, Q4-26 so far** (reported deals; a minimum count):

| Segment | Confirmed | Unconfirmed `[?]` | Demolitions |
|---|---|---|---|
| VLCC | 2 (Scorpio at Hengli, 2028, $135m) | 6 at Hengli (Dynacom among the buyers; ~$140m each). Chinese press via Greek City Times (14 Oct); not in the Xclusiv tables of 12 or 19 Oct | None |
| Suezmax | **3 (Liquimar, 157k, New Hantong, $84m each, 2029–30; Xclusiv 19 Oct)** | 2 at Hengli (same report) | None |
| Aframax/LR2 | 0 | 4 LR2 at Hengli (same report) | None |
| LR1/Panamax | 6 (Emarat, 74k, New Hantong; Xclusiv 19 Oct: Q3 2029, scrubber) | — | None |
| MR | 4 (Top Ships, 50k, GSI Nansha, 2029–30; Intermodal 13 Oct) | — | None |

- **Contracting trigger (> 3% of a segment fleet in a quarter):** not fired. VLCC 0.2% (0.9% with the unconfirmed); Suezmax 0.5% (0.8%); LR1 1.4%.
- **Orderbook trigger (> 2 pp):** not fired on the Xclusiv basis (VLCC +1.1 pp, Aframax/LR2 +0.7 pp, Jul → Oct). MR2's +3.4 pp is not on a consistent basis `[?]`; re-test with Hafnia's Q3 deck (18 Nov).
- **Slippage:** not testable yet. The 2027 schedule above is the reference for January.

### Fleet supply (fleet growth per segment and year; scrapping per scenario)

| Fleet growth, Base `[A]` | 2027 | 2028 | 2029 |
|---|---|---|---|
| VLCC deliveries / exits from compliant trade | 62 / 5 | 125 / 10 | 100 / 25 |
| VLCC growth of the compliant fleet | +7.5% (~757 → 814) | +14.1% (→ 929) | +8.1% (→ 1,004) |
| Suezmax deliveries / exits (compliant growth) | 45 / 5 (+7.4%, ~539 → 579) | 60 / 10 (+8.6%) | 50 / 15 (+5.6%) |
| Aframax/LR2 deliveries / scrapping (net) | 60 / 15 (+3.5%) | 65 / 15 (+3.8%) | 50 / 20 (+2.2%) |
| LR1/MR net growth (scrapping 1.5 / 1.0 / 1.5%) | +4% | +4% | +2% (LR1 ~+2%, MR ~+2.5%) |

Unchanged since 10 Oct. The basis:
- **Compliant-fleet basis:**
  - Growth is measured on nominal fleet minus sanctioned ships; all deliveries enter compliant trade.
  - VLCC ~757 compliant at start-2027 (917 − 160); Suezmax ~539.
  - Gibson's 16 Oct counts confirm it. The US approval programme (14–24 VLCCs realistic) would add ~2–3% to compliant VLCC supply over its first year, inside Base's < 30 assumption.
- **Exits consistent with each scenario's rates:**
  - The VLCC demolition record of 38 (2018) came at earnings near opex. Only 7 VLCCs were scrapped in 2022–26.
  - All 2026 VLCC/Suezmax removals were sanctioned ships.
  - Base exits: 5 / 10 / 25.
- **Product scrapping:** the run-rate is ~0.5–0.6% a year; sanctioned ships are hard to recycle. Base uses 1.0–1.5% (LR1/MR) and 15–20 Aframax/LR2 a year.
- **Scrapping by scenario `[A]`:** Bear VLCC 20 / 50 / 60 (near cash breakeven, as in 2018); Bull 5 / 5 / 10; Base as above.
- **New orders:** Liquimar's 3 Suezmaxes (2029–30) add ~+0.3 pp to Suezmax 2029–30 growth. The unconfirmed Hengli 6 VLCCs would add ~+0.6 pp to 2029. Both are below the minimum change.
- **Scrapping capacity is not the constraint; owners' earnings are.** The ≥ 20-year pool rises to 30–40% of each crude segment by full delivery.

### Balance check (demand − effective fleet growth, per segment, scenario and year)

Inefficiency is counted only in demand (ton-days). Unchanged since 10 Oct.

| pp change in tightness `[A]` | 2027 | 2028 | 2029 | Rate path consistent? |
|---|---|---|---|---|
| VLCC Bear (compliant basis; ~40 Iranian VLCCs back in 2027 and ~20 in 2028) | −8 − 10.8 = **−18.8** | 1 − 11.3 = **−10.3** | 2 − 4.3 = **−2.3** | Yes: 70 → 26 → 24, near Frontline's ~$24k cash breakeven, where 50–60 VLCCs scrapped a year is plausible (2018) |
| VLCC Base (compliant basis) | +1 − 7.5 = **−6.5** | 3 − 14.1 = **−11.1** | 2 − 8.1 = **−6.1** | Yes: 700 stub → 180 (Q4-27 70) → 50 → 36. 2029 is the trough at ~80% of parity, where exits of ~25 begin |
| VLCC Bull (scrapping 5 / 5 / 10) | 5 − 7.5 = **−2.5** | 0 − 14.7 = **−14.7** | 1 − 9.6 = **−8.6** | **Flagged:** 480 → 150 → 90 needs crisis inefficiency to last through 2029 |
| Suezmax Base (compliant basis) | 1 − 7.4 = **−6.4** | 3 − 8.6 = **−5.6** | 2 − 5.6 = **−3.6** | Yes: 465 stub → 115 → 44 → 30 (91% of parity) |
| Suezmax Bear | −8 − ~8.3 = **~−16** | 1 − ~6.8 = **~−6** | 2 − ~4 = **~−2** | Yes: 50 → 27 → 25 |
| Aframax/LR2 Base | 2 − 3.5 = **−1.5** | 2 − 3.8 = **−1.8** | 2 − 2.2 = **−0.2** | Yes: 305 stub → 65 (Q4-27 40) → 38 → 35. On the compliant basis 2028–29 would be ~35–36 / ~33 (−6 to −8%, below the minimum change) |
| LR1/MR Base | 4 − 4 − 3 (LR2s back to clean) = **−3** | 2 − 4 − 2 = **−4** | 2 − 2 = **0** | Yes: LR1 120 stub → 45 (Q4-27 34) → 30 → 28; MR 55 → 37 (Q4-27 33) → 25 → 22 |

**How the 2028–29 rates were set (10 Oct; re-tested today):**
- **Crude:**
  - Q4-27 exits at 70 (1.6× parity). A −11 pp year takes the 2028 average to ~50, and a further −6 pp takes 2029 to ~36 (~80% of parity).
  - In the 2010–13 and 2017–18 delivery waves, VLCC earnings fell to ~50–65% of newbuild parity `[E, background]`.
  - Base stays above that history because ~18% of the fleet is sanctioned, Cape/Red Sea routing persists and restocking runs into 2028.
- **Products:** the 2029 balance is about flat once scrapping is set at the observed run-rate. MR (22) and LR2 (35) sit at 2025 period-rate levels; LR1 (28) ~10% above.
- **Today's re-test:**
  - The period market prices 36 months from November at 88–106% of Base in every segment.
  - The VLCC forward implied by the 1- and 3-year TC (F) moved to Base (0.95, on a 3-yr TC from one source).
  - Delivery sources differ in timing, not totals.
  - The US approval programme sits inside Base.
  - **Kept.**
- **Mid-cycle kept (VLCC 44 / Suezmax 33).** 2029 is the trough, not the norm: deliveries fall to ~25 VLCCs a year from 2030 and ~30% of the fleet is ≥ 20 years old at full delivery. The exit at mid-cycle values assumes a 2030–31 recovery, and the IAF bridge should name it.

**Non-linearity:** the market starts at extreme utilisation (VLCC spot ~20× its 10-year average). On the compliant basis:
- ~6.5 pp of loosening in 2027 takes Base from 700 (stub) to an average of 180;
- ~11 pp in 2028 takes it to ~50;
- ~6 pp in 2029 takes it to ~36.

No published utilisation series was read `[?]`.

## Signposts and monitoring

| Signpost | Threshold (Bear / Bull) | Now (24 Oct) | Previous (17 Oct) | Direction |
|---|---|---|---|---|
| Hormuz flows (Kpler, via oil BBB) | Bear ≥ 13 crude without escort · Bull < 8 crude for two weeks | Strait ~14 mb/d total incl. Gulf of Oman transfers (week to 18 Oct); ME incl. alternatives > 24 | Crude ~8.5; total 11.6 | → Base (recovered) |
| Tanker attacks / STS | Bull: STS hub suspended | IRGC claims four STS tankers hit in the northern Gulf (unverified); RPG attack off Saudi Arabia (16–17 Oct); ≥ 18 attacked in two weeks (Kpler) | ≥ 10 hit 11–16 Oct; Sohar anchorage | → Bull (not suspended) |
| Saudi export infrastructure (new, from oil BBB) | Bull: a facility hit with lasting loss | Houthi strikes inside the kingdom; Aramco Dhahran evacuated; no lost barrels | — | → Bull |
| Iran–USA | Bear: deal > 60 days · Bull: new strikes | Talks stalled; second carrier; no strikes before 3 Nov | US reply "insufficient" | → Bull |
| US approval of sanctioned tankers | Bear > 30 VLCCs approved · Base < 30 | Policy announced 19 Oct; approval process in development; 14–24 VLCCs realistic (Kpler, Braemar, Arrow) | Being weighed | Base |
| Bab el-Mandeb tankers (PortWatch) | Bear > 18/d · Bull < 5/d | 10.0/d (12–18 Oct) | 8.6/d | Base |
| VLCC 1-yr TC | Bear < 90k · Bull > 250k on all sources | 300 (Intermodal 16 Oct) / 268.75 (Compass) / 220 (Fearnleys 21 Oct) | 270 / 268.75 / 225 | Crossed on two of three |
| VLCC segment average | — (info: stub) | 883 (16 Oct); ~685 est. (23 Oct, TD34-based) | 937 (9 Oct) | ↓ |
| TD3C Q1-27 FFA (TD3C TCE) | Bear < 300k · Base < 700k by end-Dec · Bull > 1m | ~861k `[A]` (125 lots per month) | ~875k | Flat |
| TD34 (Gulf of Oman–China) | — (info: segment proxy) | $657k (23 Oct; −22% w/w) | $838k (16 Oct) | ↓ |
| Suezmax 1-yr TC | Suezmax 2027 → ~100 if < ~130k on Intermodal/Fearnleys | 180 (Intermodal) / 165 (Fearnleys) / 128 (Compass, sticky); NAT fixture 150 | 155.25 / 165 | Supports Base 2027 |
| TD20 Q1-27 FFA (info; thin) | Suezmax 2027 review if it falls further | Jan ~167k, Q1 ~117k on TD20 `[A]` (40 lots) | Jan ~148k, Q1 ~111k | → |
| LR1 1-yr TC | — (info) | 60 (Intermodal) / 61 (Compass) | 56 / 61 | At Base |
| China product exports | Bull for Pacific clean if quotas rise | No November quota reported `[?]` | Below quota pace | Open |
| Russian diesel | Bear for MR if > 0.6 mb/d | Q3 western exports 510 kt/month; October only modestly higher; US schedule 0.3 → 0.5 → 1 Mt | First cargo | Small |
| USTR/China port fees | Bull: fees reinstated 10 Nov | Suspension expires 9 Nov; no notice seen | Open | Open |
| Panama tanker transits | Bull for MR/LR1 ton-miles: < 10/d for two weeks | 13.0/d (12–18 Oct) | 9.4/d | Normal |
| VLCC orderbook/fleet | Bear > 40% of total fleet | 33.5% (vessels, 11 Aug); 32.5% by dwt (12 Oct) | Same | Base |
| VLCC contracting per quarter | Bear > 3% of fleet (~27 ships) | Q4: 2 confirmed + 6 unconfirmed (0.9%) | Same | Below |
| Aframax/LR2 orderbook | Bear > 25% of fleet | 17.8% (vessels); 20.7% by dwt | Same | Base |
| VLCC exits from compliant trade | Bear ≥ 50 a year near cash breakeven · Bull ≤ 5 | None reported in Q4 | Same | Base needs 10 (2028) and 25 (2029) |
| Product and Aframax/LR2 scrapping | Bear < 0.5% a year from 2028 at parity · Bull > 3% | ~0.5–0.6% a year (2026) | Same | Base needs 1.0–1.5% / 15–20 |
| Product orderbook for 2029 | Bear > 15m dwt · Bull < 10m dwt | ~12–13m dwt `[A]` | Same | Rising |
| LR2s trading dirty | Bear for clean < 40% | Clean LR2s −39% y/y (158 ships); > 50% dirty | > 50% | → Bull (clean) |
| LR1 contracting and orderbook | Bear for LR1 > 16% or Q4 orders > 3% | ≈ 15%; Q4 orders 6 (1.4%) | Same | Watch |
| AG VLCC fixtures / list (Fearnleys) | Bull: sharp fall in liftings | 31 fixed in the week (−19); 105 available in the MEG next 30 days (+6) | 50 fixed; 99 available | → Base (supply building) |
| TD3C benchmark (info) | — | Mercuria v Baltic trial from 26 Oct; TD34 FFA liquid | Same | TD34 is the cross-check |

**Watch before the next update:**
- Xclusiv 26 Oct (the VLCC segment level behind the 700 stub).
- Whether TD3C paper follows TD34 down.
- Relets and MEG list length (Fearnleys 28 Oct).
- Attacks on STS in the Gulf and Gulf of Oman; Saudi infrastructure; US decision after 3 Nov.
- OFAC approval process: number of VLCCs, buyers.
- Intermodal and Fearnleys period rates (VLCC 3-yr confirmation).
- OPEC+ (1 Nov); USTR notice (9 Nov).
- Frontline Q3 orderbook (late Nov) and Hafnia Q3 deck (18 Nov).

## For IAF

- **Stub Q4-26 open days (market basis):**

| Segment | New | Was (17 Oct) | Change |
|---|---|---|---|
| VLCC | **700** | 850 | −150 |
| Suezmax | 465 | 465 | — |
| Aframax | **305** | 245 | +60 |
| LR2 | 220 | 220 | — |
| LR1 | 120 | 120 | — |
| MR | 55 | 55 | — |

  - **Rough effect `[A]`:** per open ship over the rest of Q4 (~68 days from 24 Oct), VLCC −$10.2m and Aframax +$4.1m. The Aframax change reverses most of the 17 Oct cut.
  - Booked days stay at booked rates; apply the company's own booked share first. Open days fall mostly in Nov–Dec, which the stub already weights at the paper's lower level.
- **2027–2029 and mid-cycle unchanged, so V_T is unchanged.** The period market now sits at Base, which supports the Base paths for valuation (no further haircut needed for "period below Base").
- **CAPT:** VLCC open Q4 days are lower and Aframax/LR2 higher; take both in at the next update. The 10 Oct note (re-run CAPT; Bear LTV) still stands.
- **Hafnia:** no change (LR2, LR1, MR stubs kept).
- **Asset-based checks:** old Suezmaxes at ~$98–103m (2010-built) and VLCC 5-yr ~$205–217m. The US approval of sanctioned-tanker sales is a downside risk to old-VLCC values.
- **Growth-capex hurdle:** unchanged. A VLCC newbuild at $131.5m needs ~$57k/day sustained to earn k = 12%; Base mid-cycle is 44.

## Change log

- **New since 17 Oct:**
  - **Oil BBB 24 Oct:** paths unchanged. ME oil incl. alternatives > 24 mb/d; strait ~14 mb/d; ~40% bypass; > 1 mb/d STS. Escalation against Saudi Arabia; the US approval of sanctioned-tanker sales.
  - **Spot:**
    - VLCC segment 937 → 883 (Xclusiv, 9 → 16 Oct).
    - Baltic 23 Oct: TD3C $1.29m (−6%), TD34 $657k (−22%), TD15 $551k (−24%), TD22 $452k (−19%), TD20 $407k (−22%), TD25 $197k (−16%), TD19 $383k (+15%), TC1 $313k, TC5 $230k, TC15 $115k (−34%).
    - Relets and ballasters fill the VLCC lists (Fearnleys).
  - **Paper:** Gibson Q4 FFA (22 Oct): TD3C 1,223 (−3%), TD20 366 (−4%), TD25 230.5 (+18%), TC5 190 (−4%), TC7 51.75 (+9%), TC18 42.75 (+3%). BWET Q1-27: TD3C ~861k, TD20 ~117k.
  - **Period (Intermodal 16 Oct):** VLCC 300 / 130; Suezmax 180 / 77.25; Aframax 99 / 53; LR1 60 / 39.5; MR 45 / 26.75. Fearnleys (21 Oct) VLCC 220, Suezmax 165, Aframax 100. Compass unchanged. NAT *Nordic Hawk* 1-yr at $150k (21 Oct).
  - **US approval of sanctioned-tanker sales** (19 Oct); analysts count 14–24 realistic VLCC returns.
  - **Orders:** Liquimar 3 Suezmax confirmed (Xclusiv 19 Oct); Emarat confirmed (Q3 2029).
  - **Values:** unchanged; S&P of 2010-built Suezmaxes at $98.5–103m.
  - **Product tonnage data** (Xclusiv/Signal): clean LR2s −39%, product shipments −10.9%.
  - **PortWatch to 18 Oct:** Panama back to 13/d; Bab el-Mandeb 10/d.
- **Triggers:**
  - **Fired:**
    - A new Oil Market BBB that asks for this update.
    - Suezmax 1-yr TC +16% (Intermodal; tested: kept).
  - **Not fired:**
    - VLCC 1-yr +11% (Intermodal); Year-1 FFAs (TD3C −2%, TD20 +5%).
    - Panama (one week only).
    - Orderbook and contracting.
    - Sanctions changes below 2% of any segment (approvals not yet granted; 31 new designations).
  - **Signposts:** the VLCC 1-yr TC Bull signpost is crossed on two of three sources. No catalyst is triggered.
- **User input assessed:** none this run (plain update request). The 17 and 22 Oct addenda (Baltic and TD34; Compass; TradeWinds NAT fixture; Dynacom sale) are carried into the sections above.
- **Changed (previous → new):**

| Item | Previous (17 Oct) | New (24 Oct) | Reason |
|---|---|---|---|
| Stub VLCC | 850 | **700** | Segment falling faster than TD3C: TD34 −22% to $657k (Baltic 23 Oct), segment est. ~685. Re-marked on the October average plus the BWET TD3C path for Nov–Dec. Cross-checks 648–778 |
| Stub Aframax | 245 | **305** | The 17 Oct mark used TD25 paper on its low day × a one-day ratio. TD25 Q4 paper +18% since; the segment held at 328 (16 Oct) on Med and North Sea strength |
| Stub method | Route Q4 FFA × one-day segment/route ratio | October segment average + paper path for Nov–Dec; ratio as cross-check | The ratio broke when routes diverged (TD25, TD3C); the skill's own definition is QTD actual + forward |
| VLCC / Suezmax newbuild now | 131 / 91 | 131.5 / 90.5 | Xclusiv 19 Oct |
| LR1 5-yr now | 67 | 68 | Intermodal October average 68.3 |
| Market check | 1-yr TC vs Base Oct-26 → Sep-27 incl. the full stub | Period vs Base over the months a charter runs (from November); table for all segments | Skill rule (2026-10-22.1) |
| Suezmax 2027 flag | "Cut to ~100 likely if primary sources fall" | **Removed** | Primary 1-yr TC rose (180) and sits at ~98–107% of Base |
| Bear signpost (supply) | OFAC licences > 30 VLCCs | > 30 sanctioned VLCCs approved for mainstream trade | Policy now announced; same threshold |
| Bull signposts | — | + Saudi export facility hit with lasting loss | Oil BBB 24 Oct |
| Contracting log | Liquimar 3 unconfirmed | Liquimar 3 confirmed ($84m, 2029–30) | Xclusiv 19 Oct table |

- **Unchanged:**
  - All 2027–2029 paths in all scenarios, the Year-1 quarters, mid-cycle TCE and asset values.
  - Suezmax, LR2, LR1 and MR stubs (computed moves +3–10%, +6%, −5% and offsetting).
  - Fleet supply, balance and demand tables; LR2 = Aframax from 2027.
  - Weights 25/50/25 (convention) kept.
- **Kept, flagged:**
  - The VLCC stub depends on an estimated 23 Oct segment level (Xclusiv 26 Oct will test it).
  - VLCC 3-yr TC +22% (one source).
  - Delivery-schedule spread (Compass/Clarksons vs BRS for VLCC 2028; Suezmax and Aframax/LR2 earlier).
  - Bull 2029.
- **Forecast vs actual:** not applicable (no realised year in the window). For information, the VLCC segment ran 786 / 937 / 883 / ~685 (est.) through October against the 10 Oct stub of 850 and the new 700.
- **Data gaps:**
  - Cal-28/29 FFA (paid data).
  - TD34 FFA levels.
  - The 23 Oct segment averages (Xclusiv 26 Oct).
  - China crude arrivals.
  - Dated demolitions by segment.
  - A published utilisation series.
- **Earlier history (in git):**
  - 10 Oct, four runs: 2027 raised; fleet register added; 2028–29 product and crude re-tests on the compliant-fleet basis.
  - 17 Oct: stub re-marked, OFAC catalyst added.
  - Addenda 17 and 22 Oct: Baltic access and TD34, Compass, NAT fixture, Dynacom sale.
- **New baseline date:** 24 Oct 2026.

## Appendix: sources

| Source | Content | Observed / published |
|---|---|---|
| `docs/oil-market-bbb.md` | Oil scenarios; Kpler flows (> 24 mb/d incl. alternatives; strait ~14); bypass and STS shares; attacks; Saudi escalation; East–West 7 mb/d; Russian/Chinese products; freight costs; sanctioned-tanker sales | 24 Oct 2026 |
| [Baltic Exchange tanker report week 43](https://www.balticexchange.com/en/data-services/WeeklyRoundup/tanker/news/2026/tanker-report-week-43.html) (in-app browser) | TD3C WS1,208.13 / $1,287,851; TD34 WS620 / $656,587; TD15 WS556.13 / $550,946; TD22 $58.22m / $451,905; TD20 WS731.11 / ~$406,769; TD27 WS740.56 (TCE "$148,500" inconsistent, not used); TD33 WS666.11 / ~$444,100; TD6 WS1,072.78 / ~$870,600; TD7 WS585.83 / ~$481,500; TD19 ~WS810 / $382,816; TD26 WS672 / ~$231,500; TD9 WS666 / ~$210,400; TD25 ~WS651 / ~$197,000; TD28 $14.26m / ~$301,900; TC1 WS1,075 / $313,200; TC20 $21.51m / $336,400; TC15 $12.00m / $115,100; TC5 WS1,105 / $229,900; TC8 $16.28m / $250,500; TC17 $113,200; TC2 $12,900; TC14 $53,900; TC21 $61,500; MR Atlantic basket $65,800; TC6 $109,600; TC23 $67,900 | 23 Oct |
| [Baltic Exchange tanker report week 42](https://www.balticexchange.com/en/data-services/WeeklyRoundup/tanker/news/2026/tanker-report-week-42.html) | Route WS/TCE 16 Oct (TD3C $1,370,193; TD34 $837,569; TD20 ~$522,600; TD25 $234,851; TC1 $285,400; TC5 $202,000; MR Atlantic basket $62,700) | 16 Oct |
| [Gibson, "Diesel, Drones and Donald"](https://www.gibsons.co.uk/report/diesel-drones-and-donald/) | Russian diesel GL 135, Graham Act waiver, export volumes (Q3 510 kt/month vs 3.27 Mt/month); regional commentary (relets, TD34 decrease, Suezmax top, Med Aframax rebound, Black Sea war risk zone). Table (eco, non-scrubber, 22 Oct): TD3C WS1,208 / $1,347,500, Q4 FFA WS1,109 / $1,222,750; TD20 WS731 / $429,250, Q4 WS646 / $366,000; TD25 WS652 / $209,250, Q4 WS728 / $230,500; TC1 WS1,075 / $329,250; TC5 WS1,105 / $244,750, Q4 $190,250; TC18 $62,000, Q4 $42,750; TC7 $78,250, Q4 $51,750. Bunkers Fujairah 967, Singapore 926, Rotterdam 747 $/t. Clean text "WS500/510" conflicts with the table (not used) | 22 Oct / 23 Oct |
| Amplify BWET holdings (in-app browser) | TD3C lots / value: Oct 242 / $61.07m; Nov 202 / $44.91m; Dec 217 / $46.05m; Jan–Mar 125 each / $21.46m, $20.33m, $19.20m → $252.4 / 222.3 / 212.2 / 171.7 / 162.6 / 153.6 per t → TCE ≈ 1.37 / 1.20 / 1.14 / 0.91 / 0.86 / 0.81m `[A]`. TD20: Oct 65 / $9.79m; Nov 50 / $5.69m; Dec 50 / $4.16m; Jan–Mar 40 each / $2.48m, $1.81m, $1.56m → $150.7 / 113.7 / 83.3 / 61.9 / 45.2 / 39.1 per t → TCE ≈ 507 / 365 / 249 / 167 / 103 / 80k `[A]` | Holdings page dated 26 Oct; read 24 Oct |
| Fearnleys Weekly wk 43 (fearnpulse.com, in-app browser) | VLCC 1-yr 220k (−5k), Suezmax 165k, Aframax 100k; spot WS (MEG/Japan 1,200, WAF/FEast 615, WAF/USAC 785, Sidi Kerir/WMed 950, Caribs/USG 665); VLCCs fixed 31, 105 available in the MEG; relets, "profit taking"; North Sea floor, Med strong; values and newbuild prices unchanged. "Brent Spot" not used | 21 Oct |
| Intermodal Weekly Market Report wk 42 (PDF via Hellenic Shipping News) | 1-yr/3-yr TC 16 Oct (rebuilt; each row checks): VLCC 300,000 / 130,000; Suezmax 180,000 / 77,250; Aframax 99,000 / 53,000; Panamax 60,000 / 39,500; MR 45,000 / 26,750; Handy 29,250 / 19,000. October 5-yr averages VLCC 216.7, Suezmax 135, Aframax 88.3, LR1 68.3, MR 52.7 | Data to 16 Oct / 20 Oct |
| Xclusiv Shipbrokers Weekly wk 42 (PDF via Hellenic Shipping News) | Segment averages VLCC $883,372, Suezmax $700,137, Aframax $328,345; routes (TD3C $1,387,683; WAF–China $711,081; USG–China $551,352; TD20 $511,221; Black Sea–Med $889,052; MEG–Med $759,554; North Sea $474,585; Kuwait–Singapore $456,238; TD25 $198,525; TC1 $284,616; TC15 $172,995; TC20 $333,985; TC5 $202,500); MR Atlantic $63,419, Pacific $81,008 (TC2/TC6/TC8 text repeats TC1/TC5/TC20, not used). Editorial: Signal data, product shipments −10.9%, clean LR2 −39.2%, crude Aframax +20.3%. Values and newbuild prices; S&P (*Zouzou N* $103m, *Maran Poseidon* $98.5m, *Afra Mare* $59m, *Prive Angel* $24.5m); newbuild orders (Liquimar 3 × 157k $84m 2029–30; Emarat 6 × 74k Q3 2029) | Data to 16 Oct / 19 Oct |
| Compass Maritime Weekly, 19 Oct (PDF) | 12-month TC unchanged (VLCC 268,750; Suezmax 128,000; Aframax 96,000; LR1 61,000; MR 39,500); deliveries rest-26 / 27 / 28 unchanged (VLCC 11 / 67 / 99; Suezmax 15 / 55 / 72; Aframax 32 / 82 / 79; Panamax 10 / 28 / 18) | 19 Oct |
| [Splash247, "US moves to legitimise shadow tanker fleet"](https://splash247.com/us-moves-to-legitimise-shadow-tanker-fleet/) (in-app browser) | Wright (19 Oct): approval process for sanctioned-tanker sales; Kpler 24 of ~160 VLCCs; Braemar 19 VLCCs; Arrow 22 tankers incl. 14 VLCCs, none Suezmax/Aframax; BRS 148 US-only (2.5%), 14 idle > 3 months; INTERTANKO opposition | 20 Oct |
| Sanctions search summaries (sanctions.com, Legal500, Energy News Beat) | OFAC designations 8 Oct (22 vessels) and 21 Oct (9 vessels); delistings after ownership change; no general licence for tanker sales published | 8–21 Oct (secondary) |
| UKMTO via search (newsonair, Seatrade) | Two vessels struck off Saudi Arabia (16–17 Oct), one by RPG from a small boat; IRGC mine claim in Hormuz | 17 Oct (secondary) |
| IMF PortWatch API | Daily tanker transits and capacity | To 18 Oct |
| [TradeWinds, NAT *Nordic Hawk*](https://www.tradewindsnews.com/tankers/nordic-american-smashes-suezmax-charter-record-in-deal-with-trafigura/2-1-2061926) (user's unlock link, 22 Oct addendum) | 1-yr $150k to Trafigura; earlier $100–110k; Braemar $198k, MB $180k | 21 Oct |
| [TradeWinds, Dynacom *Zouzou N*](https://www.tradewindsnews.com/tankers/dynacom-suezmax-said-to-break-100m-price-barrier/2-1-2061721) (lead only, 22 Oct addendum) | ~$103m, record for a 2010 Suezmax | 21 Oct |
| [Baltic Exchange press release, TD34 FFA](https://www.balticexchange.com/en/news-and-events/news/press-releases-/2026/TD34-FFA-trades-outpace-TD3C-in-debut-week-as-market-seeks-greater-Gulf-freight-cover.html) | ICE TD34 and TD15 FFAs since 5 Oct; TD34 3,837 trades vs TD3C 2,989 in the first week | Mid-Oct |
| Carried from earlier baselines (10 and 17 Oct; details in git) | Frontline Q2 release (orderbook 304 / 182 / 221; age shares); Allied (fleet counts); Hafnia Q2 deck (dwt schedule); BRS/Clarksons/Signal (VLCC schedule); BIMCO, Drewry, Galbraiths (scrapping, sanctioned shares); McQuilling via Scorpio 20-F (segment orderbook, Feb); Xclusiv 5 Jun and Gibson 16 Oct (sanctioned by segment); Xclusiv 12 Oct (dwt orderbook ratios, deliveries); DHT business update (12 Oct); DHT *Jaguar* 3-yr (Jul); TradeWinds Suezmax 3-yr fixtures (13 Oct); Clarksons shuttle model; Argus (LR2 switching); Splash on Emarat (13 Oct); Xinde (TD3C court case) | Feb–Oct 2026 |
| Rejected or not used | Gibson clean text WS500/510 (conflicts with its table and the Baltic). Baltic TD27 TCE (copy error). Xclusiv TC2/TC6/TC8 text (template error). Compass S&P and recycling tables (misaligned). Fearnleys "Brent Spot" (stale). Undated BRL/Banchero order reports from search (Laskaridis, JHI, TMS, Zodiac, Venergy; dates not confirmable). Nortilus VLCC "$800k" (basis not stated) | — |
