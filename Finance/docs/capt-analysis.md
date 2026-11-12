# CAPT (Capital Tankers Corp.) — IAF analysis, 24 Oct 2026 (stub Q3–Q4 2026 + 2027–2029)

Skill revisions used: **iaf-valuation 2026-10-18.2**. Sector and market inputs (all renewed 24 Oct):
- `docs/oil-shipping-bbb.md`: baseline **24 Oct 2026** (Final, stale after 23 Nov; oil-shipping-bbb rev 2026-10-24.1).
  - The stub is re-marked on the revised stub method: VLCC 850 → 700, Aframax 245 → 305.
  - 2027–29, the Year-1 quarters, mid-cycle TCE and asset values are unchanged.
  - No own tanker forecast.
- `docs/oil-market-bbb.md`: baseline 24 Oct 2026 (Final, kept unchanged). Background only, through the shipping BBB's scenario mapping.
- `docs/equity-market-bbb.md`: baseline 17 Oct, amended 18 Oct (equity-market-bbb rev 2026-10-24.1; the 24 Oct revision changed only the source of the HY reference, no value). **Context only:**
  - Index returns and E / R.
  - Oslo's exit P/E, exit P/B and mid-cycle return (exit cross-check).
  - The NOK path (NOK-path line).
  - It never changes k.
- `docs/hy-market-bbb.md` (24 Oct, kept unchanged; rev 2026-10-24.1): Base-window NIBOR 4.38% and the HY market reference E / R 0.196, read through the equity baseline. CAPT's own debt is USD and SOFR-based.

## Summary

**Verdict: fails.**
- **Base:** IRR_T is **1.0%** against k = 12%.
  - P = NOK 194.70 against a hurdle price P_k = **NOK 148.2**: margin of safety **−23.9%**.
- **News 6 Nov (noted 8 Nov, not modelled):** Amor fixed on a 15-month TC at ~$160–180k/day ($73.1–82.2m). Worth ~+$14m in Base (≈ +NOK 1/share, ~+0.2 pp): the verdict does not change (section 3).
- **Since 20 Oct:** no other company news. Base IRR fell from 1.9% to 1.0%:
  - Price +2.7%: −1.0 pp.
  - Shipping BBB's Q4 Aframax mark 245 → 305: +0.25 pp, P_k +1.0.
  - Firmer krone: −0.2 pp, P_k −0.8.
  - The cut in the Q4 VLCC mark (850 → 700) does not reach CAPT: its only sailing VLCC is on time charter to 21 Feb 2027.
- **Bear breaks the thesis:**
  - IRR −24.2%; ΣD_t + V_T = NOK 92 against 194.70, a **permanent loss of ~53%** (~49% on the Equity BBB's Bear krone).
  - FCF after debt service is negative from 2028; LTV ~76% at end-2028.
- **Bull:** 42.7%; the price already reflects **22%** of the Base-to-Bull gap.
- **What the price needs:**
  - 2029 tanker values about **29% above Base mid-cycle** (VLCC 5-yr ≈ $156m instead of $121m).
  - Or all 2027–29 rates +20% *and* exit values +20%.
- **Against the market (context):**
  - Base 1.0% is below Oslo (2.5%), World (5.2%) and the Nordic HY market (6.8%).
  - E / R −0.07, against the HY reference 0.196.
  - **Watch levels:** ~NOK 168 (Base = HY 6.8%), **NOK 148 (Base = k)**, **~NOK 142 (E / R = HY reference; binding)**.
- **Exit cross-check:**
  - Exit P/E 10.6x (Oslo 11.5) and exit P/B 0.86x (Oslo 1.75).
  - A buyer at the exit marks earns ~8.3%, against Oslo's 9.1%. At the index return, Base is −0.8%.
- **The period market now sits at Base in every segment** (shipping BBB, 24 Oct). That removes one argument that Base was generous, but the verdict rests on 2029 asset values, which the period market does not reach.

**Decision table**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (24 Oct 2026 → 31 Dec 2029) | −24.2% | **+1.0%** | +42.7% |
| IRR_T in NOK on the Equity BBB NOK path | −21.9% | +1.0% | +40.9% |
| V_T per share (NAV at exit, incl. reversion tail) | 70.1 | **154.1** | 337.8 |
| P_k (hurdle price) / margin of safety | 69.6 / −64% | **148.2 / −23.9%** | 355.7 / +83% |
| Capital preserved? (ΣD_t + V_T vs 194.70) | **No: 91.9 (−53%)** | Yes: 199.9 (+2.7% nominal) | Yes: 480.8 |
| Cumulative maintenance FCF per share, Q4-26 to 2029 | 52.8 | **103.2** | 286.4 |
| Net debt per share at exit (negative = net cash) | 99.4 | **73.1** | −12.9 |
| Balance sheet | FCF after debt service −$54m in 2028–29; cash falls to ~$370m; LTV ~76% at end-2028, covenant terms undisclosed `[?]` | Net debt peaks $1.23bn (Q2-28); at exit gross LTV ~55%, net ~32% on Base mid-cycle values. Funding: $359m still to arrange (2028) | Net cash in most quarters from Q1-27 |

**Per-share path** (NOK per share; 134.18m shares; USD/NOK 9.3403)

| | Q3-26E (ended) | Q4-26E | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| **Base** EBITDA, $m | 147 | 415 | 636 | 382 | 259 |
| EBITDA per share | 10.25 | 28.90 | 44.25 | 26.58 | 18.04 |
| **Maintenance FCF per share** | **9.90** | **28.46** | **41.78** | **20.82** | **12.15** |
| Debt amortisation per share | 0.48 | 0.64 | 3.49 | 6.66 | 6.86 |
| FCF after debt service per share | 9.41 | 27.82 | 38.29 | 14.15 | 5.29 |
| D_t paid per share | 3.00 (Q2 dividend, paid 18 Sep, before valuation) | 4.24 | 27.59 | 8.30 | 5.67 |
| Net debt per share, period end | 21.4 | 5.7 | 58.4 | 79.5 | 73.1 |
| V_t per share, year end | — | 219.8 | 185.4 | 165.5 | **154.1** |
| **Bear** maintenance FCF per share | 9.90 | 28.46 | 14.59 | 6.00 | 3.74 |
| Bear V_t per share | — | 219.8 | 89.2 | 70.4 | 70.1 |
| **Bull** maintenance FCF per share | 9.90 | 28.46 | 129.77 | 79.68 | 48.47 |
| Bull V_t per share | — | 219.8 | 294.6 | 317.7 | 337.8 |

- **Maintenance FCF** = EBITDA − net interest − drydock, before debt amortisation. CAPT pays dividends out of FCF after debt service, so the payout is applied to that line.
- Q3-26 ended before the valuation date and sits in today's net debt; its dividend (paid ~15 Dec) is still ahead and counts.
- **V_t at end-2026** marks the fleet at today's market values glided 10% towards Base mid-cycle, identical in all scenarios.

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value · `[E]` external or secondary · `[C]` carried from an earlier version · `[A]` own assumption · `[?]` not found.

## 1. Header

| Item | Value |
|---|---|
| Company | Capital Tankers Corp. (Marshall Islands). Euronext Growth Oslo: CAPT, ISIN MHY1096C1093. Reports in USD, IFRS |
| Price (P) | **NOK 194.70**, close Fri 23 Oct 2026, 14:28 UTC (Yahoo `CAPT.OL`) `[F]`. Day range 193.00–197.20; previous close 194.80. Week: 191.64 / 189.50 / 190.50 / 194.80 / 194.70. 52-week high 215.95 (14 Oct) |
| Valuation / exit date | 24 Oct 2026 / 31 Dec 2029, **T = 3.19 years** |
| Shares | **134,177,660** (9 Sep 2026, incl. 485,067 RSU-plan shares) `[F]` |
| Market cap / EV | NOK 26.12bn = **$2.80bn**; net debt at the valuation date ≈ **$307m** (end-Q3E, model) → EV ≈ **$3.10bn** |
| NAV at today's market marks | **NOK 206.4/share (P/NAV 0.94x)**. Fleet $4,839m (Xclusiv 19 Oct, unchanged from 12 Oct): sailing VLCC 210, Suezmax 125, LR2 85, Aframax 2018–19 ~78. Newbuilds at resale, scaled `[A]`: VLCC 2027 delivery 200, 2028 delivery 188, Suezmax 2028 113. Less remaining capex $1,567m and net debt $307m |
| NAV_0 (Base mid-cycle marks, V_T method) | **NOK 108.3/share (P/NAV_0 1.80x)**. Bear NOK 50.5 (3.86x); Bull NOK 186.6 (1.04x). No contract is firm past Feb-27 |
| FX | USD/NOK **9.3403** (Yahoo `NOK=X`, 23 Oct 14:00–14:30 UTC bar, matching the price time stamp) `[F]`. Constant over the horizon (decision); the Equity BBB NOK path is reported as its own line |
| Track / k | **Track B** (spot tanker owner, fleet doubling on debt, finite-life ships). **k = 12%**, not raised: pro forma gross LTV ~46%, liquidity ~330k shares a day, no single-asset exposure |

**Sources (connector · document · as-of date):**
- **Company:**
  - Release of 20 Oct 2026 (MFN): Amor delivery and financing for 11 VLCCs `[C]`.
  - Q2 2026 earnings release and presentation, and the 9 Sep share capital notice, read 4 Oct via FinancialFilings id 51575 `[C]`.
- **Filing check, 24 Oct:**
  - MFN: nothing after the 20 Oct release.
  - FinancialFilings: still at its monthly credit limit.
  - Newsweb-only notices are not covered (flag kept).
- **Yahoo** (23 Oct close): CAPT.OL, NOK=X. NOK=X 18 Sep close 9.4174 was used for the Q2 dividend. SOFR futures as of 16 Oct `[C]`.
- **Sector and market baselines:**
  - `docs/oil-shipping-bbb.md` (24 Oct; inputs 16–23 Oct; the 23 Oct segment level is estimated from Baltic routes).
  - `docs/equity-market-bbb.md` (17/18 Oct; prices 16 Oct).
  - Oldest company input: Q2 report (period to 30 Jun 2026).

## 2. Scenarios (from Oil Shipping BBB, 24 Oct)

| Scenario | Catalyst | Shipping BBB rows used ($k/day, VLCC / Suezmax / Aframax-LR2) | What it does to CAPT |
|---|---|---|---|
| **Base** (decision) | Armed normalisation: ME oil incl. bypass ~22–24 mb/d, crude via bypass and escort, Gulf and Gulf of Oman contested. Inefficiency through H1-27, easing in H2-27; ~290 VLCC deliveries in 2027–29, 2029 the trough. US approval of sanctioned tankers stays small (14–24 VLCCs) | **2027:** 180 / 115 / 65 (Q1–Q4: VLCC 400 / 160 / 90 / 70; Suezmax 230 / 115 / 65 / 50; Aframax/LR2 114 / 63 / 43 / 40). **2028:** 50 / 44 / 38. **2029:** 36 / 30 / 35. **Mid-cycle:** 44 / 33 / 30 | Windfall in Q4-26 and H1-27, then rates at or below newbuild parity while CAPT takes 14 VLCCs |
| **Bear** (stress) | Iran–USA deal plus recession (Q1 2027); a wide US approval programme returns > 30 sanctioned VLCCs to compliant trade (from Nov 2026) | **2027:** 70 / 50 / 36 (Q1 150 / 90 / 55). **2028:** 26 / 27 / 29. **2029:** 24 / 25 / 25. **Mid-cycle:** 36 / 27 / 24 | Rates near cash breakeven in 2028–29 |
| **Bull** (stress) | US strikes after 3 Nov and retaliation against Saudi/Gulf export infrastructure (Houthi strikes inside Saudi Arabia; a second US carrier), or suspension of the Gulf of Oman STS hub; USTR/China port fees on 10 Nov | **2027:** 480 / 300 / 160 (Q1 800 / 500 / 260). **2028:** 150 / 108 / 72. **2029:** 90 / 70 / 55. **Mid-cycle:** 55 / 41 / 37 | Crisis through 2027. **Bull 2029 is flagged as high in the shipping BBB** |

- **Stub Q4-26** (identical in all scenarios): **VLCC 700**, Suezmax 465, **Aframax 305**, LR2 220. CAPT's Aframax/LR2 pool uses the blend 262.5; its VLCC is on TC.
- **End-2026 asset marks:** also identical.

## 3. Company and status

- **News of 6 Nov `[C]` (MFN 6 Nov 07:00; noted 8 Nov, not modelled):** a **15-month time charter for the Suezmax M/T Amor** (2026, dual-fuel LNG, scrubber) with "a global energy company", from November 2026 (to ~Feb 2028), subject to the charterer's vetting. Expected revenue **$73.1–82.2m**, i.e. **~$160–180k/day gross** over ~457 days (rate and options not disclosed).
  - **Against the model** (Amor open, at the scenario rows: Q4-26 stub 465 × 80%, 2027 quarters × 97%, Jan–Feb 2028 at the 2028 row): Base earns ~$62.9m over the same days (~$138k/day), Bear ~$39m, Bull ~$130m.
  - **So the charter is worth** ~**+$14m in Base** (mid-point, after ~1.25% commission) ≈ **+NOK 1.0/share**, mostly in 2027; Bear **+$36m** (≈ +NOK 2.5); Bull **−$50m** (≈ −NOK 3.5). Roughly +0.2 pp on Base IRR and +NOK 1 on P_k `[A]`: the verdict (fails, margin −23.9%) does not change. It narrows the Bear–Bull spread slightly.
  - **Market read:** a 15-month Suezmax period at ~$170k/day is above the shipping BBB's Base 2027 average (115) and well above its 2028 row (44). It is one fixture, the first year of which is mostly Q4-26/Q1-27 at windfall rates; it goes to the shipping BBB as a period-market data point (section 13).
  - **Not modelled now:** CAPT is on hold to 11 Nov (user); the Q3 report (30 Nov) brings the full update, with the charter in the model.
- **No other company release since 20 Oct** (MFN, 24 Oct).
- **News of 20 Oct `[C]`:**
  - **Amor delivered 20 Oct** (13 days early), with a $64.5m sale-and-leaseback (28 × $0.9m, $40.0m balloon Oct-2033). The sailing fleet is 17 (1 VLCC, 8 Suezmax, 4 Aframax, 4 LR2).
  - **Financing arranged for 11 VLCCs, $930.3m** (expected amounts; lenders, margins and covenants not disclosed `[?]`):

| Date | Vessels (yard, delivery) | Expected financing per vessel | Repayment | Balloon per vessel |
|---|---|---|---|---|
| 29 Sep | Alterego II, Alexandros II, Apollonas II (Hanwha, 2027) | $81.3m / $81.3m / $79.2m | 20 quarterly × $1.0m (5 years) | $60.9m / $60.9m / $59.4m |
| 9 Oct | Amfitrion II, Alexander the Great II, Anemos II (DSIC, 2027) | $90.9m / $90.9m / $89.6m | 40 quarterly × $1.1m (10 years) | $45.5m / $45.5m / $44.8m |
| 10 Oct | Akadimos, Amyntas II (DSIC, 2027–28) | $89.6m each | 40 quarterly × $1.1m | $44.8m |
| 12 Oct | Aspidoforos, Armonikos, Aftarkis (Hengli, 2027) | $79.3m each | 40 quarterly × $1.0m | $39.7m |
| **Total** | **11 VLCCs** | **$930.3m** | ~4.9–5.0% of principal a year | Hanwha balloons ~$181m in 2032 (outside the window) |

- **Still to arrange:** ~$359m `[C]` for Arkesios, Aktor, Atromitos II (VLCCs, Feb–May 2028), Akeraios and Alkaios (Suezmaxes, Feb/Mar 2028).
- **Fleet: 33 ships, ~7.1m dwt:**
  - 15 VLCC, 10 Suezmax, 4 Aframax (2018–19), 4 LR2.
  - 14 VLCCs deliver Jan 2027 – May 2028.
  - Options on 13 more crude tankers ($1,496m, exercisable to **31 Dec 2026**; broker intrinsic value $253.7m on 18 Aug `[C]`).
- **Employment:** spot and short-term charters via Heidmar (related party). Aristotelis II is on TC at $97,450/day to 21 Feb 2027 `[C]`. No other period cover.
- **Balance sheet 30 Jun 2026** `[C]`: debt $523.9m (SOFR + 1.22%), cash $356.7m, net debt $167.2m.
- **Remaining capex:** $1,567m after Q3. Funding:
  - Cash $357m.
  - Debt drawn or secured $247m (incl. Ayrton and Amor).
  - Arranged $930.3m.
  - Still to arrange $359m.
  - Excess ~$86m `[C]`.
- **Dividends:**
  - Q1 NOK 0.50; Q2 NOK 3.00 (paid 18 Sep: not counted).
  - Policy: ~30–40% of FCF to equity while building, 70–80% when fully delivered.
- **Overhead:** G&A is holding-company cost (technical management in opex, commercial management in voyage costs) `[C/A]`. It is not deducted in NAV.

| Reported $m | Q1 2026 (9 Jan–31 Mar) | Q2 2026 |
|---|---|---|
| TCE revenue | 27.6 | 114.0 |
| Adjusted EBITDA | 25.7 | 104.2 |
| Net income / EPS | 23.1 / $0.21 | 92.9 / $0.70 |
| Fleet TCE $/day | 97,309 | 116,260 |
| Opex $/day | — | 8,246 |

## 4. Near term: stub quarters (all scenarios)

| | Q3-26E (ended 30 Sep, unreported) | Q4-26E |
|---|---|---|
| Available days | 1,304 (company) | **1,545** (company 1,532 + 13 Suezmax days for Amor `[A]`) |
| Booked | 79% at $113,681 fleet (1 Sep): VLCC 100% at 97,450 (TC), Suezmax 71% at 130,239, Aframax/LR2 82% at 105,765 `[C]` | Not disclosed `[?]` |
| Open days | Suezmax $180k, Aframax/LR2 $130k `[A]` | 80% of the stub mark `[A]`: Suezmax 465 → 372, **Aframax/LR2 262.5 → 210** (was 186). VLCC on TC at 97.5 (the 700 mark does not apply) |
| Model TCE $/day | 122.8k | **278.5k** (was 267.0k) |
| TCE revenue / EBITDA ($m) | 160 / 147 | 430 / 415 |
| Maintenance FCF / FCF after debt service ($m) | 142 / 135 | 409 / 400 |
| Per share (NOK) | 9.90 / 9.41 | 28.46 / 27.82 |
| Dividend declared (45% of FCF after debt service) | $61m = **NOK 4.24**, paid ~15 Dec 2026 `[A]` | $180m = **NOK 12.52**, paid ~15 Mar 2027 `[A]` |
| Capex / new debt ($m) | 239.4 / 182.0 | 122.1 / 64.5 (Amor) |
| Net debt at quarter end ($m / NOK per share) | 307 / 21.4 | **81 / 5.7** |

- **Q4 realisation (80%):**
  - The shipping BBB's new stub method already weights Nov–Dec at the paper's lower level. 80% still covers the discharge-to-discharge lag of September fixtures, Amor's ex-yard first voyage and LR2 clean legs.
  - Q4 EBITDA moves ~$53m per 10 pp; Base IRR is −0.5% at 60% and 2.5% at 100%.
- **Consensus:** Yahoo FY26 EPS 24.17, probably NOK (≈ $2.59/share, ≈ $347m). This model gives ~$635m (H1 $116m + H2E ~$520m). Not used; the gap is flagged.
- **Net debt bridge to 31 Dec 2026 ($m):**
  - 167.2 (30 Jun) + capex 361.5 + dividends paid 103.5 − maintenance FCF Q3–Q4 551.1 = **81.1**.
  - Gross debt $754m, cash $673m.
  - **Net debt at the valuation date ≈ $307m** (end-Q3E).
- **Dates:**
  - Q3 report not announced `[?]` (late Nov/early Dec likely).
  - Mercuria v Baltic (TD3C) trial 26 Oct; OPEC+ 1 Nov; US midterms 3 Nov; Norges Bank 5 Nov; USTR/China port fees 9–10 Nov.
  - Option deadline 31 Dec.

## 5. Market input and how it enters

### Oil Shipping BBB (24 Oct)

| Input | Value used | Entry into the model |
|---|---|---|
| Stub Q4-26 spot TCE | VLCC **700** (was 850), Suezmax 465, Aframax **305** (was 245), LR2 220 | Open Q4 days at 80%; VLCC on TC, so the VLCC cut has no effect |
| Year-1 quarters 2027 | Section 2 (unchanged) | Open days × 97%; VLCC Q1 = 52 TC days + spot |
| 2028 / 2029 | Base VLCC 50 / 36, Suezmax 44 / 30, Aframax/LR2 38 / 35; Bear 26 / 24, 27 / 25, 29 / 25; Bull 150 / 90, 108 / 70, 72 / 55 (unchanged) | Flat within each year × 97% |
| Mid-cycle TCE (Bear / Base / Bull) | VLCC 36 / 44 / 55, Suezmax 27 / 33 / 41, Aframax/LR2 24 / 30 / 37 | Structural runs; FCF_normalised; exit-consistency test |
| Mid-cycle asset values, 5-yr (Bear / Base / Bull) | VLCC 93 / 121 / 160, Suezmax 64 / 84 / 112, Aframax 54 / 75 / 100, LR2 52 / 73 / 98; newbuild Base 130 / 90 / 77 / 79; 8% asset rate | V_T and NAV_0, adjusted for age |
| Asset values now (Xclusiv 19 Oct) | VLCC 210 / 185; Suezmax 125 / 110; Aframax 85 / 72.5; newbuild VLCC 131.5, Suezmax 90.5 | NAV at market marks; interim V_t glide |
| **Period market check (new reading)** | 1-yr TC at 76–108% and 3-yr TC at 88–106% of Base over the same months, in every segment | Supports Base 2027–29 for valuation; no haircut for "period below Base" |
| Recovery after the window | "the exit at mid-cycle values assumes a 2030–31 recovery" | Exit-consistency test (section 8) |
| Value risk | US approval of sanctioned-tanker sales can weigh on old-VLCC values | Risk; CAPT's fleet is young (VLCC ≤ 4 years at exit) |
| Growth capex hurdle | VLCC newbuild at $131.5m needs ~$57k/day for 12% | ROIC_g test |

### Equity Market BBB (17 Oct, amended 18 Oct; values unchanged on 24 Oct) — context

| Input | Value | How it enters |
|---|---|---|
| Index Base window IRR (NOK, before fees) | Oslo **2.5%**, World **5.2%**; Nordic HY market 6.8% | Comparison line (section 9) |
| Base-window 3M NIBOR | 4.38% | E = Base IRR − NIBOR |
| E / R convention | R = Base 2027 − Bear 2027; HY market reference **0.196** | CAPT E / R; watch prices |
| House Bear | Oil Bear plus recession H1 2027: Oslo −28.5%, World −20.6%, HY −2.2% in 2027 | Mapping check (same catalyst as CAPT's Bear) |
| Oil side case (escalation) | Oslo ≈ +15%, World ≈ −15% in 2027 | CAPT's Bull corresponds to it |
| Oslo exit P/E / exit P/B / mid-cycle return (Bear / Base / Bull) | 10.5 / 11.5 / 12.5; 1.48 / 1.75 / 1.97; 8.2 / 9.1 / 9.4% | Exit cross-check (Step 3) |
| NOK path | USD/NOK vs spot: Base flat; Bear +12% (2027), +9% (2028–29); Bull −3% | NOK-path line (FX rule) |

## 6. Common assumptions (all scenarios)

| Item | Value | Source |
|---|---|---|
| Available days 2027 / 2028 | 7,732 / 11,519, by quarter as guided | Company `[C]` |
| Available days 2029 | 11,839 | `[A]` |
| Q4-26 days | +13 Suezmax days (Amor delivered 20 Oct, not 2 Nov) | Release `[C]`, days `[A]` |
| Realised vs segment average TCE, 2027–29 | 97% | `[A]` |
| Opex per calendar day | 2026: VLCC 9.92k / Suezmax 8.85k / Aframax-LR2 7.57k; +3% a year | `[C/A]` |
| G&A (holdco) | $2.0m a quarter in 2026; 2.5 / 2.75 / 3.0 in 2027 / 28 / 29 | `[C/A]` |
| Debt cost | 5.5% (stub), 5.8% (2027), 5.9% (2028–29) = SOFR futures + 1.22% + ~0.1% fees; cash 3.8%. New-loan margins undisclosed `[?]` | `[C/A]` |
| New debt at delivery | Arranged per vessel `[C]`: Q1-27 81.3; Q2-27 251.4; Q3-27 90.9; Q4-27 417.1; Amyntas II 89.6 (Q1-28). Still to arrange $359m for 3 VLCC (~83.5 each) + 2 Suezmax (~54 each) `[A]` in Q1–Q2 2028 | Release 20 Oct; Q2 presentation |
| Amortisation | 5.3% of debt a year (new facilities ~5%) | `[C]` |
| Payout of FCF after debt service | 45% (stub, 2027), 50% (H1-28), 75% (H2-28, 2029); nil when negative | `[C/A]` |
| Dividend timing | ~2.5 months after quarter end; the Q4-29 dividend stays in V_T | `[A]` |
| Tax | Nil | `[A]` |
| Working capital, options, buybacks, new equity | None | `[A]` |

## 7. Period tables ($m, with per share in NOK)

### Base (decision case)

| | Q3-26E | Q4-26E | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|
| Available days | 1,304 | 1,545 | 1,606 | 1,814 | 2,005 | 2,307 | 11,519 | 11,839 |
| Fleet TCE $k/day | 122.8 | 278.5 | 180.3 | 99.9 | 61.7 | 52.4 | 43.8 | 32.9 |
| EBITDA | 147 | 415 | 273 | 163 | 103 | 97 | 382 | 259 |
| Maintenance FCF | 142 | 409 | 268 | 155 | 93 | 84 | 299 | 175 |
| — per share | 9.90 | 28.46 | 18.64 | 10.79 | 6.50 | 5.85 | 20.82 | 12.15 |
| Debt amortisation | 7 | 9 | 10 | 11 | 14 | 15 | 96 | 99 |
| FCF after debt service | 135 | 400 | 258 | 144 | 79 | 69 | 203 | 76 |
| — per share | 9.41 | 27.82 | 17.95 | 10.03 | 5.52 | 4.79 | 14.15 | 5.29 |
| Growth capex | 239 | 122 | 172 | 252 | 117 | 422 | 483 | 0 |
| New debt drawn | 182 | 65 | 81 | 251 | 91 | 417 | 449 | 0 |
| Dividend declared (in period earned) | 61 | 180 | 116 | 65 | 36 | 31 | 128 | 57 |
| — per share | 4.24 | 12.52 | 8.08 | 4.51 | 2.48 | 2.16 | 8.93 | 3.97 |
| Net debt, end of period | 307 | 81 | 165 | 378 | 466 | 839 | 1,143 | 1,049 |
| — per share | 21.4 | 5.7 | 11.5 | 26.3 | 32.5 | 58.4 | 79.5 | 73.1 |

### Bear

Capex, new debt and the stub equal Base.

| | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|
| Fleet TCE $k/day | 76.5 | 42.6 | 32.7 | 27.9 | 26.2 | 23.8 |
| EBITDA | 106 | 59 | 45 | 41 | 180 | 151 |
| Maintenance FCF (per share) | 101 (7.05) | 50 (3.45) | 34 (2.33) | 25 (1.76) | 86 (6.00) | 54 (3.74) |
| FCF after debt service (per share) | 91 (6.35) | 39 (2.69) | 19 (1.35) | 10 (0.71) | −9 (−0.66) | −45 (−3.13) |
| Dividend declared per share | 2.86 | 1.21 | 0.61 | 0.32 | 0 | 0 |
| Net debt (per share) | 332 (23.1) | 575 (40.0) | 676 (47.0) | 1,081 (75.2) | 1,482 (103.2) | 1,428 (99.4) |

### Bull

Capex, new debt and the stub equal Base.

| | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|
| Fleet TCE $k/day | 388.7 | 274.8 | 209.5 | 183.0 | 114.0 | 73.2 |
| EBITDA | 608 | 480 | 400 | 398 | 1,191 | 736 |
| Maintenance FCF (per share) | 603 (41.95) | 475 (33.09) | 395 (27.47) | 392 (27.25) | 1,145 (79.68) | 696 (48.47) |
| FCF after debt service (per share) | 593 (41.25) | 465 (32.33) | 381 (26.49) | 376 (26.20) | 1,049 (73.01) | 598 (41.61) |
| Dividend declared per share | 18.56 | 14.55 | 11.92 | 11.79 | 46.17 | 31.21 |
| Net debt (per share) | −170 (−11.8) | −127 (−8.8) | −195 (−13.6) | 6 (0.4) | −32 (−2.2) | −185 (−12.9) |

### Year-end path per share (NOK; D_t = dividends paid in the period)

Interim V_t marking `[A]`: today's market marks ($4,839m incl. newbuilds at resale) glide to each scenario's mid-cycle exit value. V_T includes the reversion tail. The share of the gap closed by each year end:

| Scenario | End-2026 | End-2027 | End-2028 | End-2029 |
|---|---|---|---|---|
| Base | 10% (to Base) | 55% | 85% | 100% |
| Bear | 10% (to Base) | 85% | 100% | 100% |
| Bull | 10% (to Base) | 25% | 65% | 100% |

No backlog exists at any interim date.

| | | Stub (to 31 Dec 26) | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| **Base** | D_t | 4.24 | 27.59 | 8.30 | 5.67 |
| | V_t | 219.8 | 185.4 | 165.5 | **154.1** |
| | r_t | +15.1% (not annualised) | −3.1% | −6.2% | −3.5% |
| | IRR to t | n.m. (0.19 yr) | +10.6% | +2.9% | **+1.0%** |
| **Bear** | D_t | 4.24 | 17.19 | 0.32 | 0.00 |
| | V_t | 219.8 | 89.2 | 70.4 | **70.1** |
| | r_t | +15.1% | −51.6% | −20.7% | −0.3% |
| | IRR to t | n.m. | −41.3% | −32.9% | **−24.2%** |
| **Bull** | D_t | 4.24 | 57.55 | 43.43 | 37.83 |
| | V_t | 219.8 | 294.6 | 317.7 | **337.8** |
| | r_t | +15.1% | +60.2% | +22.6% | +18.2% |
| | IRR to t | n.m. | +74.2% | +51.6% | **+42.7%** |

**Reading the path:**
- **Base:** selling at end-2027 at the then market marks would earn 10.6%, below k. After that, falling asset values outweigh the dividends.
- **Bear:** loses half its value in 2027.
- **The stub r_t (+15%)** marks today's fleet at market NAV (P/NAV 0.94); it is a mark, not a price forecast.

## 8. V_T bridge (Base), exit tests and growth capex

**Return split, Base:**
- P 194.70 → NAV_0 108.3 is a **re-rating of −16.8% a year**.
- NAV_0 → V_T 154.1 is **NAV growth of +11.7% a year**.
- Together g = −7.1% a year.

| Step (Base) | $m | NOK/share |
|---|---|---|
| NAV_0 at Base mid-cycle marks: existing 16 ships $1,340m + 17 newbuilds at mid-cycle newbuild value $2,090m − remaining capex $1,567m − net debt $307m (no firm-today premium beyond Feb-27; holdco G&A not deducted) | 1,556 | 108.3 |
| + Value created by growth capex (17 newbuilds at T $2,022m − value in NAV_0 $2,090m) | −68 | −4.7 |
| − Ageing of the existing fleet at mid-cycle marks ($1,340m → $1,266m) | −75 | −5.2 |
| ± Firm-today contract premium roll-off (Aristotelis II TC to Feb-27; ~$7m) | ~0 | ~0 |
| ± Premium on backlog signed in the scenario | 0 | 0 |
| ± Reversion tail (exit consistency; VLCC −37.8, Aframax/LR2 +12.5) | −25 | −1.8 |
| + Retained cash (Σ maintenance FCF $1,483m − D_t paid $658m; = −Δ net debt ex growth capex) | +825 | +57.4 |
| **= V_T (31 Dec 2029): fleet $3,288m + tail −$25m − net debt $1,049m** | **2,213** | **154.1** |

**Backlog at exit:** none in any scenario. Aristotelis II's TC ends 21 Feb 2027, and no scenario assumes new period cover. The firm-today-only sensitivity equals the decision figure.

**Exit-consistency test** (2029 rate vs the scenario's mid-cycle; open days = 2029 available days × 97%; tail factor 0.903; no tax; unchanged in $):

| Row | Scenario | 2029 rate | Mid-cycle | Gap | Open days a year | Treatment | Tail $m | NOK/share |
|---|---|---|---|---|---|---|---|---|
| VLCC | **Base** | 36 | 44 | **−18.2%** | 5,231 | **Tail.** The shipping BBB names the recovery cause (deliveries ~25 a year from 2030; ~30% ≥ 20 years) but times it to **2030–31**, beyond about a year after exit. The asset-implied TCE is above mid-cycle | −37.8 | −2.63 |
| Suezmax | Base | 30 | 33 | −9.1% | 3,488 | Not material | 0 | 0 |
| Aframax/LR2 | **Base** | 35 | 30 | **+16.7%** | 2,766 | **Tail.** The BBB explains why 2029 is above mid-cycle (small orderbook, old and sanctioned fleet) but names no cause that brings it down within a year | +12.5 | +0.87 |
| **Base total** | | | | | | | **−25.3** | **−1.76** |
| VLCC | Bear | 24 | 36 | −33.3% | 5,231 | Tail | −56.7 | −3.95 |
| Suezmax / Aframax-LR2 | Bear | 25 / 25 | 27 / 24 | −7.4% / +4.2% | — | Not material | 0 | 0 |
| VLCC / Suezmax / Aframax-LR2 | Bull | 90 / 70 / 55 | 55 / 41 / 37 | +64% / +71% / +49% | 5,231 / 3,488 / 2,766 | Tail. **The BBB flags Bull 2029 as high** | +165.3 / +91.3 / +45.0 | +21.00 total |

- **Decision with the tail.** Without it (the named-reason treatment): Base **1.3%, P_k 149.5**; Bear −23.0%, P_k 72.3; Bull 40.5%, P_k 341.1.
- The tail is zero in the structural runs.

**Exit cross-check against the equity market (Step 3):**

| | Bear | **Base** | Bull | Oslo index (Bear / Base / Bull) |
|---|---|---|---|---|
| V_T ($m) | 1,008 | **2,213** | 4,852 | — |
| FCF_normalised before holdco G&A, year after exit (own mid-cycle; after interest on exit debt and the fleet-renewal charge) | 121 | **209** | 352 | — |
| Holdco G&A a year (beside it) | 12 | 12 | 12 | — |
| **Exit P/E** | 8.3x | **10.6x** | 13.8x | 10.5 / **11.5** / 12.5 |
| Book equity at exit `[A]` (30 Jun $2,061m + net income − D_t paid) | 2,207 | **2,586** | 3,820 | — |
| **Exit P/B** | 0.46x | **0.86x** | 1.27x | 1.48 / **1.75** / 1.97 |
| Net debt ÷ V_T | 1.42 | 0.47 | net cash | — |
| **Buyer's implied equity return** (8% asset rate, levered at net debt cost ~7.4%) | 10.2% | **8.3%** | 7.8% | mid-cycle return 8.2 / **9.1** / 9.4% |
| Sensitivity: exit marks re-discounted to the index return | not needed (above the index) | **IRR −0.8%, P_k 141.9** (asset rate 8.55%, marks × 0.96) | IRR 39.0%, P_k 330.8 (asset rate 9.6%, marks × 0.89) | — |

- **Exit P/E (Base 10.6x)** sits just below Oslo's 11.5x: consistent.
- **Exit P/B below 1 in Bear and Base:** book carries ships bought or contracted in 2025–26 above their mid-cycle marks. In Bear that is an accounting impairment case, not a cash case.
- **Buyer's implied return below the index in Base and Bull:** CAPT has no contract cover, so no stated reason supports a buyer accepting less than Oslo's mid-cycle return. The sensitivity is shown; the decision stays at the market marks (the Track B default).

**Exit fleet value at mid-cycle, $m per ship (age at exit) `[A]`:**

| Ships | Bear | Base | Bull | Method |
|---|---|---|---|---|
| 14 VLCC newbuilds (1.75–2.6 yr) | 96.3–97.5 | 125.3–126.8 | 165.7–167.7 | Between mid-cycle newbuild (130) and 5-yr (93/121/160) |
| Aristotelis II (3.9 yr) | 94.6 | 123.1 | 162.7 | Same |
| 8 Suezmax (3.2–3.7 yr) / 2 Suezmax 2028 (1.8 yr) | 65.2–65.7 / 66.9 | 85.6–86.2 / 87.8 | 114.1–115.0 / 117.1 | Newbuild 90, 5-yr 64/84/112 |
| 4 Aframax 2018–19 (11.1 yr) | 44.6 | 61.9 | 82.5 | 5-yr × today's 10/5-yr ratio (0.85), −3% a year beyond 10 |
| 4 LR2 (4.9 / 3.5 yr) | 52.1 / 53.3 | 73.1 / 74.8 | 98.1 / 100.5 | Newbuild 79, 5-yr 52/73/98 |
| **Fleet total** | **2,493** | **3,288** | **4,366** | No dual-fuel premium or Chinese-yard discount `[A]` |
| + Reversion tail | −57 | −25 | +302 | Exit-consistency table |
| Backlog premium at exit | 0 | 0 | 0 | No contracts past Feb-27 |

**Growth capex test (Step 4):**

1. **Committed programme** (17 ships incl. Amor; remaining capex $1,567m, ~$1,353m debt-funded, of which ~$995m is secured or arranged):
   - **Horizon basis:** IRR **~32%**, NPV at 12% **+$470m** (Base EBITDA of the new ships 2026–29 ~$552m plus exit value $2,022m). At mid-cycle rates: ~26%, +$363m.
   - Accretive for a buyer today; that gain is inside NAV_0.
   - **Life-cycle basis:** a VLCC at $117–123m needs $52–54k/day for 12% (BBB anchor $57k at $131.5m). Base mid-cycle is 44, so **ROIC_g < k**.
2. **Options** (13 ships, $1,496m, deadline 31 Dec 2026), not modelled:
   - k-parity TCE is $53.5k (VLCC at $120m) and $41.7k (Suezmax at $89.5m), against Base mid-cycle 44 / 33 and Base 2029 36 / 30. **ROIC_g < k**.
   - They deliver Dec-27 to Sep-28, into the trough.

## 9. Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (dated, to the exit value) | −24.2% | **+1.0%** | +42.7% |
| IRR_T in NOK on the Equity BBB NOK path | −21.9% | +1.0% | +40.9% |
| d / g / c | 3.5% / −27.4% / −0.4 pp | **7.4% / −7.1% / +0.7 pp** | 23.0% / +18.9% / +0.8 pp |
| g: re-rating / NAV growth (P/NAV_0) | −34.5% / +10.9% (3.86x) | **−16.8% / +11.7% (1.80x)** | −1.3% / +20.5% (1.04x) |
| Structural IRR / cyclical (pp; Δd, Δg) | −22.9% / −1.3 pp (+0.3; −1.4) | **−5.8% / +6.7 pp (+2.9; +3.5)** | +10.4% / +32.3 pp (+16.8; +15.0) |
| ΣD_t / V_T (NOK) | 21.8 / 70.1 | **45.8 / 154.1** | 143.1 / 337.8 |
| P_k (hurdle price) / margin of safety | 69.6 / −64% | **148.2 / −23.9%** | 355.7 / +83% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | 14.2x vs negative | **14.2x vs 0.7x** | 14.2x vs 29.6x |
| Capital preserved? ΣD_t + V_T vs P | **No: 91.9 (−53%)** | Yes: 199.9 (+2.7% nominal) | Yes: 480.8 |

**Definitions and readings:**
- **Structural run:** every open day from 1 Jan 2027 at that scenario's own mid-cycle; stub, TC days and exit values unchanged; tail zero.
  - **Base:** a rate path around an unchanged mid-cycle.
  - **Bear:** a shift in the mid-cycle (its −1.3 pp cyclical part is the exit tail).
  - **Bull:** a higher mid-cycle plus a much stronger 2027.
- **FCF_normalised (Base):**
  - Full fleet at Base mid-cycle, 2029 costs: EBITDA $298m (after holdco G&A $12m) − net interest $78m = $220m.
  - Less the fleet-renewal charge $23m = **$197m = NOK 13.7/share**: P/FCF 14.2x.
  - With one year of ageing on the full exit fleet it is 16.8x. Either way it is far above the 0.7x ceiling.
- **Scenario-weighted reference** (convention): IRR 8.8%, P_k NOK 180. Not the decision figure.
- **Bull already priced:** (194.70 − 148.2) / (355.7 − 148.2) = **22%**.

**Bear: balance-sheet survival:**
- Maintenance FCF stays positive every quarter (lowest $11m).
- FCF after debt service is −$9m (2028) and −$45m (2029). The 2029 fleet TCE ($23.8k) is below the full-fleet cash breakeven including amortisation (~$25.6k). Dividends stop after Q4-27.
- Cash falls to ~$370m at end-2029. Gross debt peaks at $1.95bn (Q2-28) against a Bear fleet value of ~$2.5bn: **LTV ~76% at end-2028, 72% at end-2029.**
- Covenants on the new facilities are undisclosed `[?]`.
- The Hanwha loans leave ~$181m of balloons in 2032, after the window.
- **Liquidity survives; capital does not.**

### Against the equity market and HY (context, from `docs/equity-market-bbb.md`)

| Base window, NOK | Base IRR | E (pp over NIBOR 4.38%) | R (pp: Base 2027 − Bear 2027) | E / R | Bear 2027 | Bear capital kept |
|---|---|---|---|---|---|---|
| Nordic HY market (after 0.6% fee) | 6.2 | 1.82 | 9.3 | **0.196** (reference) | −2.8 | — |
| World, NOK unhedged (after 0.20% fee) | 5.0 | 0.64 | 26.3 | 0.024 | −20.8 | −5.2% |
| Oslo (OSEBX, after 0.20% fee) | 2.3 | −2.12 | 29.2 | −0.07 | −28.7 | −11.9% |
| **CAPT** (no fee) | **1.0** | **−3.40** | **48.5** (−3.1 vs −51.6) | **−0.07** | **−51.6** | **−53%** |

- **R for CAPT** uses calendar-2027 returns on the interim marks (equity BBB convention). From today's price to end-2027 it is 55 pp (Base +11.6%, Bear −43.2%). E / R is negative either way.
- **Watch prices** (unchanged paths):

| Level | CAPT price (NOK) | From 194.70 |
|---|---|---|
| Base IRR = HY market Base 6.8% (pre-alert) | ~168 | −14% |
| **Base IRR = k (P_k)** | **148** | **−24%** |
| **E / R = HY reference 0.196** (Base IRR 13.9%) | **~142** | **−27%** |

- **Scenario mapping:**
  - CAPT's Bear is the house Bear's catalyst; CAPT falls ~1.8x as far as Oslo in 2027.
  - CAPT's Bull is the equity BBB's oil side case (Oslo ≈ +15%, World ≈ −15%), the only case in which it diversifies world equities. The oil baseline says the Houthi campaign inside Saudi Arabia has moved that case closer.
- **NOK path:** the Bear krone cushions the loss from −53% to −49%. Base is unchanged; Bull is slightly lower.

**Sensitivity (Base unless stated; with tail):**

| Change | IRR_T | P_k (NOK) |
|---|---|---|
| No reversion tail (named-reason treatment) | 1.3% | 150 |
| Exit marks re-discounted to Oslo's mid-cycle return (9.1%) | −0.8% | 142 |
| Exit fleet value × 0.8 / 0.9 / 1.1 | −8.6% / −3.5% / +5.1% | 116 / 132 / 164 |
| Exit fleet value × 1.2 / 1.25 / 1.3 | +8.8% / +10.6% / +12.3% | 180 / 188 / 196 |
| **Break-even exit value for 12%** | × 1.29 (VLCC 5-yr ≈ $156m) | — |
| Base cash flows, exit at today's market marks ($5.0bn) | +19.4% | 232 |
| Base cash flows, Bull exit / Bear exit values | +13.5% / −10.5% | 202 / 111 |
| All Base rates 2027–29 × 0.8 / 0.9 / 1.1 / 1.2 | −4.5% / −1.9% / +3.7% / +5.9% | 127 / 137 / 159 / 168 |
| Rates × 1.2 and exit × 1.15 / × 1.2 | +11.5% / **+13.2%** | 192 / 200 |
| Q4-26 realisation 60% / 70% / 90% / 100% (model 80%) | −0.5% / 0.2% / 1.7% / 2.5% | 142 / 145 / 151 / 155 |
| k = 10% / 13% / 14% | — | 155 / 145 / 142 |

## 10. Verdict and caveat

- **Fails.** Base margin of safety −23.9% (below −2%); Base IRR 1.0% against k = 12%.
- **Bear breaks the thesis:** −53% of capital, no dividends after 2027, LTV ~76% in 2028.
- **Behind every market alternative on Base:** Oslo 2.5%, World 5.2%, HY 6.8%. E / R is negative.
- **This week's inputs barely move value:** the higher Aframax stub (+NOK 1.0 on P_k) and the firmer krone (−0.8) offset; the higher price lowers the IRR.
- **The decisive assumption is the 2029 asset value:** 29% above Base mid-cycle (VLCC 5-yr ≈ $156m) is needed for 12%. Rates alone (+20%) give 5.9%.
- **The exit cross-check adds no comfort:** the exit is below book (0.86x), and at the index return Base is −0.8%.

**Caveat:** this is a margin-of-safety screen, not an intrinsic valuation or a price target. P_k is the price at which the Base path returns exactly 12%.

## 11. Tracking

No new quarterly report since the previous versions (all rest on Q2 2026).

| | 4 Oct | 10 Oct (evening) | 17 Oct | 20 Oct | **24 Oct** | Main reason for the latest change |
|---|---|---|---|---|---|---|
| Price (NOK) | 184.5 | 196.64 | 195.10 | 189.50 | **194.70** | Market (+2.7%) |
| USD/NOK | 9.61 | 9.581 | 9.4434 | 9.3882 | **9.3403** | Firmer NOK |
| Shipping baseline | 4 Oct | 10 Oct, run 4 | 17 Oct | 17 Oct | **24 Oct** | Stub VLCC 850 → 700 (no effect on CAPT), Aframax 245 → 305; period market at Base |
| Method | rev 2026-10-04.12 | rev 2026-10-10.1 | rev 2026-10-11.3 | rev 2026-10-18.2 | rev 2026-10-18.2 | Unchanged |
| Company news | — | — | — | Amor; $930.3m arranged | **None** | — |
| Base IRR_T | 2.6% | 2.3% | 1.0% | 1.9% | **1.0%** | Price −1.0 pp; Aframax stub +0.25 pp; FX −0.2 pp |
| Base P_k (NOK) | 144.8 | 154.8 | 148.2 | 147.7 | **148.2** | Aframax stub +1.0; FX −0.8 |
| Margin of safety | −21.5% | −21.3% | −24.1% | −22.0% | **−23.9%** | Higher price |
| Bear IRR_T / capital | −20.9% / −49% | −21.7% / −49% | −24.3% / −53% | −23.7% / −52% | **−24.2% / −53%** | Higher price |
| Weighted reference | 7.8% | 9.2% | 8.7% | 9.8% | 8.8% | Convention only |
| NAV at market marks (NOK) | ~169 | ~210 | ~209 | ~207 | ~206 | FX |

**Ahead of or behind Base:**
- Delivery is ahead (Amor +13 days); financing is on track (11 of 14 VLCCs arranged).
- The first earnings test is the Q3 report: Q3E EBITDA $147m, FCF after debt service $135m, dividend ~NOK 4.2.

## 12. Risks and signposts

- **Asset values:** the verdict hangs on them.
  - VLCC 5-yr (210 now; Base mid-cycle 121); resale/newbuild ratio ~1.60x.
  - The US approval of sanctioned-tanker sales could weigh on old-VLCC values (CAPT's fleet is young).
- **Delivery wave vs inefficiency** (shipping BBB signposts):
  - VLCC 1-yr TC (Intermodal 300 now; Bear < $90k, Bull > $250k on all sources).
  - TD3C Q1-27 FFA (~$0.86m; Mercuria v Baltic trial from 26 Oct).
  - STS hub status.
  - **> 30 sanctioned VLCCs approved for mainstream trade** (Bear; analyst counts 14–24).
  - VLCC exits from compliant trade (Base ≥ 10 in 2028, ≥ 25 in 2029).
- **Bull signposts brought closer** (oil and shipping BBB, 24 Oct): Houthi strikes inside Saudi Arabia, Aramco's Dhahran evacuation, a second US carrier. **A Saudi export facility hit with lasting loss** is a new Bull signpost.
- **Suezmax 2027** flagged earlier in the shipping BBB (cut to ~100 possible): now supported by the period market (1-yr 165–180 = 98–107% of Base). Effect if cut: ~−0.6 pp Base IRR `[A]`.
- **Financing:** $359m still to arrange for 2028. Margins, lenders and covenants are undisclosed `[?]`. Hanwha balloons fall in 2032.
- **House Bear signposts** (equity and HY BBB): US HY OAS > 4.5%; Norges Bank FCI > +2; Nordic HY spread > 550 bp.
- **Options (31 Dec):** ROIC_g < k in Base; equity issuance is a dilution risk.
- **Related parties and control:** CMTC ~73%; Heidmar and CSM are related parties; the lock-up expires in March 2027.
- **Catalysts:**
  - Mercuria v Baltic (26 Oct); OPEC+ (1 Nov); US midterms (3 Nov); Norges Bank (5 Nov); port fees (10 Nov).
  - Q3 report (`[?]`); option decision (≤ 31 Dec); first VLCC delivery (Alterego II, 15 Jan 2027).

## 13. For other modules

- **Oil Shipping BBB (8 Nov):** period-market data point for its next run: CAPT's Amor, 2026 dual-fuel Suezmax, 15-month TC from November 2026 at ~$160–180k/day gross (revenue $73.1–82.2m; charterer "a global energy company"; subject to vetting). No change requested.
- **Oil Shipping BBB:** no change requested. Its "For IAF" note for CAPT (VLCC stub lower, Aframax/LR2 higher) is taken in. The VLCC part has no effect because CAPT's sailing VLCC is on time charter through Q4.
- **Equity Market BBB:** no input (CAPT is on Euronext Growth, outside OSEBX).
- **HY BBB:** not relevant.

## Change log

- **8 Nov 2026: news note (Amor 15-month TC, 6 Nov)**, no model change, under iaf-valuation rev 2026-10-18.2 (CAPT on hold to 11 Nov, user). Worth ~+$14m in Base vs the open-spot path (+NOK 1.0/share, ~+0.2 pp, P_k ~+1) `[A]`; Bear +$36m, Bull −$50m. Verdict unchanged (fails). Taken into the model at the Q3 report (30 Nov).
- **24 Oct 2026 (this version):** baselines of 24 Oct; no company news.
  - **Inputs:**
    - Price 194.70 (23 Oct), USD/NOK 9.3403, valuation date 24 Oct.
    - Shipping stub VLCC 850 → 700 (not applied: VLCC on TC) and Aframax 245 → 305 (Aframax/LR2 blend 232.5 → 262.5).
    - Asset values, 2027–29 and mid-cycle unchanged.
    - Oil, equity and HY baselines unchanged in value.
  - **Results:**
    - Base IRR 1.9% → 1.0%; P_k 147.7 → 148.2; margin of safety −22.0% → −23.9%.
    - Bear −23.7% → −24.2%; Bull 44.1% → 42.7%.
- **20 Oct 2026:** company news (Amor early; $930.3m financing for 11 VLCCs); iaf-valuation rev 2026-10-18.2 (exit cross-check, NOK-path line, backlog at exit, holdco G&A).
- **17 Oct 2026:** shipping BBB 17 Oct (stub cut), exit-consistency tail, equity market added as context.
- **10 Oct 2026, evening:** shipping BBB fourth run (VLCC/Suezmax 2028–29 lower).
- **10 Oct 2026, morning:** rev 2026-10-10.1 (summary first, return split, NAV_0 bridge, structural runs per scenario).
- **4 Oct 2026:** full rebuild under rev 2026-10-04.12; English.
- **28 Sep 2026 and earlier:** previous methods.

## Appendix A: own assumptions `[A]`

| Assumption | Value | Why |
|---|---|---|
| Q3 open-day TCE | Suezmax 180k, Aframax/LR2 130k | Aug–Sep fixtures, discharge-to-discharge lag |
| Q4 realisation | 80% of the stub mark | Lag of September fixtures; Amor's ex-yard voyage; LR2 clean legs |
| Amor's extra Q4 days | +13 Suezmax days | Delivery 20 Oct vs 2 Nov schedule |
| Aframax/LR2 stub blend | 262.5 = (305 + 220) / 2 | 4 Aframax + 4 LR2 |
| Realised vs segment average, 2027–29 | 97% | Ex-yard ballast, waiting, off-hire |
| Debt still to arrange | 3 VLCC ~83.5, 2 Suezmax ~54 ($m), Q1–Q2 2028 | $359m remaining per Q2 presentation |
| Payout | 45% → 50% → 75% of FCF after debt service | Policy and Q2 practice |
| Newbuild resale marks today | VLCC 2027 delivery 200, 2028 delivery 188, Suezmax 2028 113 | August resale $165m scaled to today's 5-yr marks |
| Asset value glide (interim V_t only) | 10% / 55% / 85% / 100% (Base) | End-2026 identical in all scenarios |
| Mid-cycle value by age | Linear newbuild → 5-yr; 5–10 yr by today's 10/5 ratio; −3% a year beyond 10 | The shipping BBB gives newbuild and 5-yr mid-cycle only |
| Reversion tail | Gap × 2029 open days × 0.97 × 0.903; rows with gap > 10% | iaf-valuation Step 3 |
| Book equity at exit | 30 Jun book + net income (depreciation ~$11.6k per calendar day) − dividends paid | Exit P/B |
| Buyer's implied return | 8% asset rate levered at the net debt cost (debt 5.9%, cash 3.8%) | Exit cross-check |
| R for E / R | Calendar-2027 returns on interim marks | Equity BBB convention |

## Appendix B: sources

| Source | Content | As-of / published |
|---|---|---|
| Yahoo `CAPT.OL` (daily chart) | Close 194.70; range 193.00–197.20; closes 19–23 Oct 191.64 / 189.50 / 190.50 / 194.80 / 194.70 | 23 Oct 2026 14:28 UTC |
| Yahoo `NOK=X` 30-min bars | 9.3403 (14:00–14:30 bar close); 24 Oct weekend quote 9.3162 not used | 23 Oct 2026 |
| Yahoo `NOK=X` daily | 9.4174 (Q2 dividend conversion) | 18 Sep 2026 |
| Yahoo SOFR futures SR3Z26 / Z27 / Z28 | 4.23% / 4.66% / 4.60% `[C]` | 16 Oct 2026 |
| CAPT release (MFN), 20 Oct | Amor delivery; financing for 11 VLCCs `[C]` | 20 Oct 2026 |
| CAPT Q2 2026 earnings release and presentation (FinancialFilings 59412307, 60340792) | P&L, balance sheet, debt per vessel, bookings, capex and days schedules, funding split, options `[C]` | 1 Sep 2026 (period to 30 Jun) |
| CAPT share capital notice (FinancialFilings 59696385) | 134,177,660 shares `[C]` | 9 Sep 2026 |
| MFN (mfn.se/all/a/capital-tankers) | Filing check: nothing after 20 Oct | Read 24 Oct 2026 |
| `docs/oil-shipping-bbb.md` | Stub (VLCC 700, Aframax 305), quarters, annual paths, mid-cycle TCE and values, asset values (Xclusiv 19 Oct), period market check, 2030–31 recovery note, signposts | 24 Oct 2026 |
| `docs/equity-market-bbb.md` | Index Base IRRs, E / R table, house Bear, oil side case, NOK path, Oslo exit P/E, P/B and mid-cycle return | 17 Oct 2026, amended 18 Oct (rev 2026-10-24.1; prices 16 Oct) |
| `docs/oil-market-bbb.md` | Scenario background (kept unchanged; Houthi strikes inside Saudi Arabia, second carrier) | 24 Oct 2026 |
| `docs/hy-market-bbb.md` | NIBOR window, HY reference E / R 0.196 (kept unchanged) | 24 Oct 2026 |
| Failed or limited this run | FinancialFilings (monthly credit limit); Newsweb-only notices not covered | 24 Oct 2026 |
