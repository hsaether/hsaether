# DNB Bank ASA (DNB) — IAF analysis, stub Q4 2026 + 2027–2029

**Update 1 — 21 Oct 2026, after the Q3 2026 report; amended 22 Oct 2026** (Q3 Excel factbook
checked, price moved to the first post-report close). Initial analysis 12 Oct 2026.

Skill revisions used: **iaf-valuation 2026-10-18.2** (was 2026-10-11.3 at the initial run; new
since then: Track A decided on a dated IRR to an independent exit P/E, which this analysis already
did, and the **exit cross-check table** against the equity market, added below). Sector inputs:
- `docs/equity-market-bbb.md`, Update 1 of 17 Oct 2026, amended 18 Oct (equity-market-bbb rev
  2026-10-18.5; the skill is now at 2026-10-18.6). Used:
  - the scenarios (Bear = recession H1 2027 + oil Bear; Base = higher-for-longer rates, earnings
    at trend; Bull = soft landing);
  - the Oslo financials block F ("rates and credit": DNB, Storebrand, Gjensidige; unchanged
    0.98 / 0.96 / 0.95);
  - Oslo exit P/E 10.5 / 11.5 / 12.5, exit P/B 1.48 / 1.75 / 1.97, mid-cycle return 8.2 / 9.1 /
    9.4%;
  - the index Base IRRs (Oslo 2.5%, World 5.2%) and the HY reference E / R 0.196.
  - DNB is 10.4% of the OBX.
- `docs/hy-market-bbb.md` (17 Oct 2026, amended 18 Oct, no value changed; hy-market-bbb rev
  2026-10-18.1 as used there, skill now 2026-10-18.2). Used:
  - **the NIBOR path** (3M NIBOR Bear / Base / Bull 4.21 / 4.79 / 4.65 in 2027, 3.55 / 4.39 /
    4.15 in 2028, 3.50 / 3.86 / 3.65 in 2029; mid-cycle 3.25 / 3.45 / 3.45);
  - Norway mainland GDP and registered unemployment;
  - the Nordic default path (FTD 3.0 → 3.5% in Base, Bear peak 8.6% in 2028; E&P, oil service
    and shipping peaks 15 / 12 / 7%);
  - the NIBOR window average 4.38% for E / R.
- The oil, shipping, rig, supply, defense and AI baselines are not used directly (the oil Bear
  enters through the equity and HY Bear).

## Summary

**Verdict**
- **Still fails, and the post-report rally widened the gap.** The share rose 3.1% to **NOK 314.70**
  on 21 Oct. Base IRR is now **7.0% a year** (8.2% at the pre-report 305.30; 8.6% initially)
  against k = 12%.
  - Hurdle price **P_k ≈ NOK 275 vs P NOK 314.70: margin of safety −12.5%** (−9.6% at 305.30;
    −8.6% initially).
  - Track A screens fail: Rule 1 d + g = 6.0 + 4.0 = 10.0% < 12%; Rule 3 P/E 11.7 against a
    ceiling of 7.0.
- **Q3 was good and changes little.** EPS 6.57 (7.07 excluding the Luminor loss) beat consensus
  of 6.33. NII rose 2.5% q/q on the July repricing, and fees were +14.6% y/y. The losses in Q3
  are in line with the model: NOK 529m, 9 bp.
  - What lowers the result is the **credit-loss path, re-based**: the normalised exit-year loss
    rate goes from 12 bp to **15 bp**. Early-warning stage-2 volumes are rising (below), and DNB's
    realised losses over a full cycle are higher than in the benign 2023–26 run.
  - A new 0.75% buyback and higher fee growth (+7% a year) offset part of it.
- **Bear loses capital but does not break the bank:** −3.5% a year, ΣD + V_T 10% below P.
  - Total return is −36% in 2027.
  - Credit losses peak at 40 bp (NOK 8.6bn) in 2028.
  - CET1 bottoms at 16.5%, 0.2 pp above the FSA expectation (16.3%). The dividend is held at NOK
    18.50; no buybacks.
- **What the price needs:** an exit P/E of ~12.3 (Base 10.5), i.e. today's 11.1x on CY27 consensus
  rising further and holding beyond 2029.
  - Even an exit priced on Oslo's mid-cycle return (9.1%, P/E ~12.1) gives 11.4%: marginal
    (−1.6%). **At NOK 314.70 the price already assumes DNB trades like the index at exit.**
- **Against the HY rule:** E / R 0.063 (HY market reference 0.196). **Triggers: NOK ~275 (−12.5%,
  Base = k) and NOK ~261 (−17%, E / R = 0.196).**

**Credit losses: actual and expected (NOK bn; bp of customer loans)**

| | 2023 | 2024 | 2025 | 2026E (9M actual 1.51) | 2027 | 2028 | 2029 | 2030 (normalised, in V_T) |
|---|---|---|---|---|---|---|---|---|
| Actual `[F]` | 2.65 (13) | 1.21 (6) | 2.80 (12) | 2.11 (10) | | | | |
| **Base** | | | | | **2.39 (11)** | **2.92 (13)** | **3.02 (13)** | **3.61 (15)** |
| Bear | | | | | 6.36 (30) | 8.56 (40) | 4.41 (20) | 3.42 (15) |
| Bull | | | | | 1.54 (7) | 1.85 (8) | 2.19 (9) | 3.06 (12) |

- Cumulative 2027–29: Base NOK 8.3bn, Bear 19.3bn, Bull 5.6bn. After tax that is NOK 4.6, 10.6
  and 3.1 a share. Every sustained +10 bp costs ~NOK 1.3 of EPS (−4%) and ~1.8 pp of IRR.
- The Bear peak (40 bp) is below DNB's 2016 oil crisis and 2020 Covid years (~50–60 bp,
  `[?]`/derived). Pre-provision profit (~NOK 48bn in the Bear) covers losses of ~2.2% of loans
  before a loss year.

**Decision table (NOK, per share)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T | −3.5% | **7.0%** | 14.1% |
| V_T (31 Dec 2029) | 228.8 | **326.3** | 407.0 |
| P_k / margin of safety | 206.1 / −34.5% | **275.2 / −12.5%** | 332.3 / +5.6% |
| Capital preserved? (ΣD + V_T vs P) | **No: −9.7%** | Yes: +21.8% | Yes: +47.8% |
| ΣD_t paid 2027–29 (cash dividends) | 55.50 | **57.00** | 58.14 |
| Credit losses 2027–29, NOK bn (peak bp) | 19.3 (40) | **8.3 (13)** | 5.6 (9) |
| Buybacks 2027–29 (NOK bn) / shares at end-2029 | 0 / 1,401m | **18.8 / 1,342m** | 14.2 / 1,359m |
| BVPS end-2029 / exit P/B | 199.3 / 1.15 | **214.3 / 1.52** | 220.7 / 1.84 |
| Balance sheet | CET1 trough 16.5% (2028), 0.2 pp above the FSA expectation; dividend held, no buybacks | CET1 held at ~17.3% with buybacks of NOK 6–7bn a year | Same as Base; ROE ~15.5% |

**Per-share path (NOK; Track A rows; calendar years = fiscal years)**

| | CY26E (9M actual + Q4E) | 2027 | 2028 | 2029 | 2030 (exit EPS) |
|---|---|---|---|---|---|
| Base EPS | 26.41 (26.91 excl. Luminor) | 28.49 | 29.37 | 30.27 | 31.08 |
| Base EPS growth | (−7.2% vs 2025's 28.45) | +7.9% (+5.9% underlying) | +3.1% | +3.1% | +2.7% |
| Base D_t paid (~5 May) | — | 18.50 (FY26) | 19.00 | 19.50 | (20.50 FY29, in V_T) |
| Base buyback, NOK per share outstanding | ~8.5 (2.75% programmes) | 5.1 | 4.2 | 4.4 | |
| Base ROE / BVPS (year-end, incl. allocated dividend) | ~14.4% / ~189 | 14.8% / 196.5 | 14.6% / 205.2 | 14.4% / 214.3 | 14.1% |
| Base V_t (year-end) | 314.7 (stub flat) | 312.8 | 319.4 | 326.3 | |
| Bear EPS / D_t / V_t | | 21.93 / 18.50 / 184.0 | 20.44 / 18.50 / 215.0 | 23.89 / 18.50 / 228.8 | 25.42 |
| Bull EPS / D_t / V_t | | 29.75 / 18.50 / 346.7 | 31.52 / 19.25 / 375.1 | 33.35 / 20.39 / 407.0 | 35.39 |

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value ·
`[E]` external or secondary · `[C]` carried from an earlier version · `[A]` own assumption ·
`[?]` not found or unverified.

## Header

| Item | Value |
|---|---|
| Company | DNB Bank ASA, Oslo Børs: **DNB**. Norway's largest financial group: personal customers (PC), corporate customers Norway (CCN), large corporates and international (LCIC), DNB Carnegie (investment bank, Nordic), Wealth Management (asset management, DNB Livsforsikring). Owners: Norwegian state (NFD) 34%, Folketrygdfondet, DNB Savings Bank Foundation (insiders 45.6% per Yahoo) `[F/E]` |
| Price (P) | **NOK 314.70**, Yahoo `DNB.OL`, close 21 Oct 2026 (14:26 UTC), the first close after the Q3 report (+3.1% on the day, from 305.30; day range 307.4–314.7; volume 2.4m, ~1.9x average) `[F]`. 52-week range 257.4–325.8. Cum the FY26 dividend (last ex-date 22 Apr 2026) |
| Valuation date / exit date | 22 Oct 2026 / 31 Dec 2029, **T = 3.19 years** |
| Shares | **1,421.82m outstanding** at 30 Sep (factbook); 1,421.65m after programme 2 (completed 2 Oct) `[F]`. New 0.75% programme approved 20 Oct (~7.1m shares in the market, ~NOK 2.2bn `[A]`). The AGM in April 2027 cancels own shares and redeems **~13.5m** state shares (9.80m for programmes 1–2 `[F]` + ~3.7m for programme 3 `[A]`) → **~1,401m** in May 2027 |
| Market cap | NOK 447bn. Book value per share **NOK 182.50** incl. allocated dividend (30 Sep 2026) `[F]` → **P/B 1.72** |
| P/E | **11.9x** CY26E 26.41 (9M actual 19.58 + model Q4 6.83; Yahoo after Q3: CY26 26.72, 11 analysts; Q4 6.68, 4); **11.7x** excluding the Luminor loss (DNB: EPS +0.50 in Q3); **11.1x** CY27 consensus (28.27, 15 analysts, up from 28.14); **11.05x** Base CY27 (28.49) |
| NAVs (Step 3) | Not applicable (bank; Track A). Book value is the anchor: P/B 1.72 at ROE ~14.5% |
| Capital | **CET1 17.3%** (30 Sep 2026) after deducting the new 0.75% programme; **FSA expectation 16.3%** (incl. Pillar 2 guidance), **requirement 15.3%** (both 0.1 pp lower than at end-June) `[F]`. Leverage ratio 6.3%; LCR 125%, NSFR 112%. Luminor closing adds ~+20 bp `[F]`. Finanstilsynet's consultation on mortgage (25%) and CRE (35%) risk-weight floors, which expire at end-2026, "may result in some reduction" of REA `[F]` |
| FX | NOK report and price: no conversion. ~25% of income international `[E]`; no foreign-currency cash flows to the holder, so no NOK-path IRR is needed |
| Track | **A** (EPS, P/E, d + g as screens) decided on a dated IRR to an independent exit P/E and a hurdle price P_k (skill Step 2A) |
| k | **12%**, not raised: AA-class ratings, CET1 1 pp above the FSA expectation, very liquid share |
| Horizon | Stub Q4-26 + 2027–2029 annual; exit on 2030 EPS at mid-cycle NIBOR and normalised credit losses |

**Sources (connector · document · period):**
- **DNB IR (ir.dnb.no), read in the in-app browser** (PDFs fetched and parsed in the page with
  pdf.js; the Q3 Excel factbook was not yet posted):
  - Q3 2026 quarterly report (21 Oct): income statement, NII and segment tables, impairment by
    industry, notes G5–G7 (stages, allowances, loans by industry), capital, outlook;
  - Q3 2026 presentation: NII bridge, CET1 bridge, FSA expectation, buyback, DNB Carnegie macro
    view;
  - Q3 2026 factbook (PDF): stage 1–3 exposure and allowances by industry, quarterly impairment
    by segment, EAD by industry and risk class, NIBOR, shares, BVPS.
  - **Q3 2026 factbook (Excel, posted 21–22 Oct):** every figure taken from the PDFs was checked
    against it (income statement, key figures, spreads, NIBOR, shares, BVPS, stages); no
    difference. Added from it: CET1 capital NOK 205.9bn, REA NOK 1,190.9bn and **foreseeable
    dividends of NOK 17.4bn already deducted at 30 Sep** (61.7% of 9M profit); buyback table
    (18.85m own shares, 9.71m state shares at 30 Sep, average price NOK 300.61); DNB Carnegie
    macro table (mainland GDP 1.1 / 1.5 / 1.6 / 1.6%, LFS unemployment 4.7 / 4.8 / 4.7 / 4.6%,
    CPI 3.3 / 2.9 / 2.6 / 2.4% for 2026–29) `[E]`.
  - Earlier: the Q2 2026 factbook (Excel) and presentation, CMD 2024.
- **Nordic Financial:** Q2 2026 and Q4 2025 releases, Luminor divestment (20 Jul), basis-swap and
  AT1 notices, Q4 2020 release (2020 profit and pre-impairment profit, used to derive the 2020
  loss level).
- **Yahoo** (22 Oct 2026, after Q3): price and daily chart, shares, `earningsTrend` (CY26 26.72,
  11 analysts; CY27 28.27, 15; Q4-26 6.68, 4; Q1-27 6.76, 3), `financialData` (target mean
  NOK 319, median 310, range 286–390, 16 analysts; "hold").
- **Norges Bank API:** policy rate 4.50% (9 Oct).
- **FinancialFilings:** not used; DNB's own report is the primary source.

## Scenario definitions (from Equity Market BBB and HY Market BBB)

| Scenario | Catalyst | What it does to DNB |
|---|---|---|
| **Base** (decision) | Equity Base: higher-for-longer rates, earnings at trend. HY Base = Norges Bank MPR 3/26: NIBOR 4.79 / 4.39 / 3.86, mid-cycle 3.45; mainland GDP ~1%; NAV unemployment 2.3–2.4%; Nordic FTD 3.0–3.5% | NII +NOK 3.0bn per pp NIBOR: the cutting cycle costs ~NOK 4bn of NII by 2030, against loan growth of 3.5% a year (DNB ambition 3–4%). Fees +7% a year (DNB ambition > 9%). Costs +3.5% then +3%. **Credit losses 11 / 13 / 13 bp, normalised 15 bp.** Margin competition −NOK 1.0bn by 2029. EPS 28.53 → 31.19 (2030); DPS +0.50 a year; buybacks hold CET1 at ~17.3%; exit P/E 10.5 |
| **Bear** (stress) | Equity Bear: recession H1 2027 + oil Bear (durable Iran–USA deal, OPEC+ market share). HY Bear: NB cuts to 3.50% by Q4-27; NIBOR 4.21 / 3.55 / 3.50, mid-cycle 3.25; mainland −0.5% (2027); NAV unemployment 3.0% (2028); Nordic HY defaults peak at 8.6% (2028) | Loan growth 1% (2027–28); fees −8%, other income −NOK 2bn in 2027. **Credit losses 30 / 40 / 20 bp** (NOK 6.4 / 8.6 / 4.4bn: CRE, oil, gas and offshore, residential property, SMEs, consumer finance), normalised 15 bp. Risk-weight migration +4% / +3% of REA. EPS 21.93 / 20.44 / 23.89; dividend held at 18.50, buybacks paused; P/E 9.0 from end-2027 |
| **Bull** (stress) | Equity Bull: soft landing, first NB cut Q3-27; NIBOR 4.65 / 4.15 / 3.65; mainland 1.5–1.8% | Loan growth 5%; fees +10% (DNB ambition met); credit losses 7–9 bp, normalised 12 bp. EPS 29.79 → 35.50 (2030), ROE ~15.5%; exit P/E 11.5 |

The stub (22 Oct–31 Dec 2026) is the same in all scenarios: Q4 from the Q3 run-rate, no dividend
payment before May 2027, price flat by convention. Bear and Bull diverge from 1 Jan 2027.

## Company and status

| Key figures `[F]` (NOK m) | 3Q26 | 2Q26 | 1Q26 | 4Q25 | 3Q25 | 9M 2026 | FY 2025 |
|---|---|---|---|---|---|---|---|
| Net interest income | 15,504 | 15,132 | 15,299 | 16,179 | 15,990 | 45,935 | 64,731 |
| Net commissions and fees | 4,489 | 4,569 | 4,129 | 4,612 | 3,916 | 13,188 | 16,398 |
| Other income (FV, insurance, associates, other) | 1,700 | 2,622 | 2,365 | 2,764 | 2,784 | 6,686 | 9,520 |
| Total income | 21,693 | 22,323 | 21,793 | 23,555 | 22,691 | 65,809 | 90,649 |
| Operating expenses | (8,634) | (8,989) | (8,441) | (9,361) | (8,483) | (26,064) | (34,476) |
| Impairment of financial instruments (annualised % of loans) | (529) (0.09%) | (338) (0.06%) | (644) (0.11%) | (853) (0.15%) | (862) (0.15%) | (1,511) (0.09%) | (2,803) (0.12%) |
| Profit to shareholders | 9,371 | 9,404 | 9,466 | 11,193 | 10,268 | 28,241 | 41,944 |
| EPS (NOK) | 6.57 (7.07 excl. Luminor) | 6.50 | 6.50 | 7.65 | 6.98 | 19.58 | 28.45 |
| ROE / C/I | 14.5% (15.5% adj.) / 39.8% | 14.6% / 40.3% | 14.0% / 38.7% | 16.6% / 39.7% | 15.8% / 37.4% | 14.4% / 39.6% | 15.9% / 38.0% |
| CET1 | 17.3% | 17.4% | 18.1% | 17.9% | 17.9% | 17.3% | 17.9% |
| Lending / deposit / combined spread; NIM | 1.33 / 1.03 / 1.20%; 1.71% | 1.30 / 1.02 / 1.18%; 1.70% | 1.52 / 0.87 / 1.24%; 1.74% | 1.61 / 0.86 / 1.29%; 1.81% | 1.73 / 0.84 / 1.35%; 1.80% | 1.39 / 0.97 / 1.21% | 1.68 / 0.89 / 1.34%; 1.84% |
| Average 3M NIBOR | 4.62% | 4.52% | 4.18% | 4.18% | 4.28% | 4.44% | 4.39% |

- **Q3 one-offs** `[F]`: Luminor loss −NOK 704m (in associates; DNB's adjusted EPS 7.07);
  DNB Næringseiendom sale +NOK 277m; AT1 FX −NOK 534m; basis swaps +NOK 151m. Underlying other
  income ≈ NOK 2.5bn a quarter.
- **NII has turned.** +2.5% q/q on the July repricing and higher interest on equity; lending spreads
  +3 bp. Norges Bank hiked again on 24 Sep (to 4.50%). DNB reprices existing mortgages and
  deposits from 29 Nov, with full effect from Q1 2027 `[F]`. NII is still −5.4% y/y for 9M:
  lending spreads −32 bp, deposit spreads +8 bp `[F]`.
- **Fees +14.6% y/y:** investment banking +39% (ECM, DCM, M&A), asset management +13%; record
  net flow NOK 54.5bn and AUM NOK 1,849bn `[F]`.
- **Costs** −4.0% q/q (seasonal, lower pension cost); +3.8% for 9M. FTEs and consultants are down
  in LCIC `[F]`.
- **Loans** +5.0% y/y (+1.2% q/q currency-adjusted); deposits −1.9% q/q (seasonal public-sector
  outflows) `[F]`.
- **Guidance (Q3 report, "Future prospects")** `[F]`: ROE > 14% (overriding); organic loan growth
  3–4% a year over time; **net commissions and fees +9% a year or more**; C/I < 40%; tax 23% for
  2026 and going forward (22% in Q4); CET1 target = FSA expectation (16.3%) + a management buffer;
  dividend payout > 50% with an ambition to raise the nominal DPS each year, plus buybacks as the
  flexible tool.
- **Distributions 2026** `[F]`: two 1% programmes completed (19.0m shares in the market + 9.8m
  state shares for NOK 2.95bn); **a third programme of 0.75% approved 20 Oct**. That uses 2.75% of
  the 3.5% AGM authorisation.
- **Capital Markets Day 10 Nov 2026 (London)** `[F]` (DNB release 10 Nov): targets for 2027–29: ROE > 14% (overriding) for FY2027–28 and
  **> 15% towards end-2028**; cost/income < 40%, **< 38% towards end-2028**; CET1 above the FSA expectation (16.3%); payout > 50% with the
  ambition of a higher nominal DPS each year (unchanged). DNB Carnegie's macro: mainland GDP ~1.5% towards 2030; policy rate stable at
  4.00% after two cuts in H2 2027.
  - **Against Base** (ROE 14.8 / 14.6 / 14.4%): the end-2028 targets sit ~0.5 pp above Base. Neither signpost is met (Bull: ROE ≥ 16% or
    a higher distribution path; Bear: ≤ 13%). If DNB reached 15% in 2028, P_k would rise ~3–4% `[A]`: at NOK 324.3 (10 Nov) the margin
    would be about −12% instead of −15%. **Verdict unchanged (fails).** The 4.00% rate floor is above HY BBB's Base for 2029 (3.86), a
    net interest income positive if right; the NIBOR path stays HY BBB's. Noted 10 Nov; the model takes it at the next run.
- **Market view** `[E]`: 16 analysts, mean target NOK 319 (+1% from 314.70), median 310, "hold".
  After Q3: CY26 EPS 26.47 → 26.72, CY27 28.14 → 28.27; Q4 6.87 → 6.68 (4 analysts).

## Credit losses: actual and expected

**Portfolio and stage development** (maximum exposure incl. commitments, NOK bn; factbook 1.5.1
`[F]`)

| 30 Sep 2026 | Exposure | Stage 2 (Dec-25 → Sep-26) | Stage 3 (Dec-25 → Sep-26) | Allowance stage 1–3 | Impairment 9M26 (NOK m) |
|---|---|---|---|---|---|
| Personal customers | 1,369.8 | 35.2 → **49.2** | 5.4 → 4.7 | 1.16 | (216) |
| Commercial real estate | 304.4 | 25.1 → 21.9 (15.4 in Mar) | 3.2 → **4.2** | 1.01 | (198) |
| Residential property | 139.8 | 11.6 → 10.9 | 2.1 → 2.4 | 0.88 | (156) |
| Oil, gas and offshore | 125.8 | 8.8 → 4.8 | 1.15 → **0.54** | 0.32 | +116 (net reversal) |
| Shipping | 60.2 | 1.9 → 0.8 | 0.01 → 0.06 | 0.03 | in "other" |
| Power and renewables | 170.6 | 7.7 → 7.6 | 2.3 → 2.9 | 0.88 | +6 |
| Fishing, fish farming and farming | 127.5 | 6.9 → 7.2 | 0.9 → **1.7** (Q3 doubled) | 0.32 | in "other" |
| Other corporate (bank and insurance, healthcare, retail, manufacturing, TMT, services, other) | 907.7 | 54.1 → **65.3** | 9.8 → 8.9 | 3.62 | (1,063) "other" incl. Poland legacy, shipping, fishing |
| **Total** | **3,206** | **151.3 → 167.6** (5.2%) | **25.0 → 25.4** (0.8%) | **8.22** | **(1,511)** |

- **What the stages say:**
  - **Stage 3 is flat** at NOK 25.4bn, 0.86% of loans. Allowances cover 24% of it (NOK 6.2bn).
    Oil and offshore is cleaning up; CRE and fishing are rising.
  - **Stage 2 is rising**: NOK 130bn (Mar) → 154 (Jun) → 168bn (Sep). The increase is in personal
    customers (+14bn since Dec; DNB: "slightly negative customer migration"), manufacturing,
    services, retail, and bank and insurance.
  - **High-risk EAD** is NOK 126.7bn, up from 97.8bn two years ago `[F]`.
  - Stage 2 is the pipeline for 2027–28 losses, but it carries only 0.6% coverage today.
- **Losses so far are benign and idiosyncratic:** 9M26 NOK 1.51bn (9 bp). DNB: "company-specific
  events within various segments"; macro forecasts had no significant effect in Q3 `[F]`.
- **Loss history `[F]` unless tagged:**
  - 2021 −0.05% and 2022 −0.01% (net reversals);
  - 2023 0.13%, 2024 0.06%, 2025 0.12%, 9M26 0.09%;
  - 2020 ≈ 0.5–0.6% (~NOK 8–10bn, derived from 2020 pre-impairment profit NOK 33.0bn, profit
    NOK 19.8bn and ~20% tax `[A]`);
  - 2016 ≈ 0.5% (oil crisis, recollection `[?]`).
  - The 2021–25 average is ~5 bp; including 2016 and 2020, the 2015–2025 average is ~15–20 bp
    `[A]`.

**Expected losses: three anchors for the normalised (exit-year) rate**

| Anchor | Loss rate | Basis |
|---|---|---|
| Recent realised, 2023–9M26 | ~10 bp | Benign: low unemployment, oil up-cycle, CRE stress absorbed |
| Cycle average, 2015–2025 | ~15–20 bp `[A]` | Includes 2016 (oil) and 2020 (Covid) at ~50–60 bp |
| Portfolio PD × LGD (risk classes) | ~20 bp `[A]` | EAD low risk NOK 1,937bn × PD ~0.15% × LGD ~15%; medium 541bn × 1.5% × 25%; high (ex stage 3) 102bn × 6% × 30% ≈ NOK 4.3bn |

**Sector build (NOK bn; % of exposure) `[A]`**

| Segment | Base normalised (2030) | Bear peak (2028) | Driver in the baselines |
|---|---|---|---|
| Personal customers | 0.41 (0.03%) | 1.37 (0.10%) | NAV unemployment 2.4% / 3.0% |
| Commercial real estate | 0.46 (0.15%) | 2.43 (0.80%) | NIBOR, Nordic real-estate FTD 2.5% / 6.0% |
| Residential property (developers) | 0.28 (0.20%) | 0.84 (0.60%) | Housing starts low; rates |
| Oil, gas and offshore | 0.13 (0.10%) | 1.26 (1.0%) | Oil Bear: Brent 60; oil-service FTD 12% |
| Shipping | 0.06 (0.10%) | 0.30 (0.5%) | Tanker Bear; shipping FTD 7% |
| Power and renewables | 0.17 (0.10%) | 0.34 (0.20%) | Contracted cash flows |
| Fishing and farming | 0.19 (0.15%) | 0.38 (0.30%) | Salmon prices, resource tax |
| Other corporate | 1.82 (0.20%) | 1.82 (0.20%) | SMEs, retail, services, manufacturing |
| **Total** | **3.52 (~15 bp of loans)** | **8.74 (~40 bp)** | Model: Base 3.61; Bear 8.56 |

- **The Base path (11 → 13 → 13 → 15 bp) assumes the rising stage 2 turns into somewhat higher
  losses, not a cycle.** It is above the 2023–26 run-rate and at the low end of the cycle
  anchors. The Bear (40 bp peak) is a recession plus an oil collapse, about two thirds of the
  2016/2020 peaks. DNB's oil and offshore book is smaller and cleaner now, and its CRE book is
  larger.
- **Capacity:** pre-provision profit ~NOK 56–60bn a year in Base and ~48bn at the Bear trough. A
  loss year needs a ~2.2% loss rate, about 4x the 2016/2020 peaks.

## Near term: stub (all scenarios)

| NOK | Q3-26 actual | vs model (consensus 12 Oct) | Q4-26E | CY26E |
|---|---|---|---|---|
| EPS | **6.57** (7.07 excl. Luminor) | 6.33 (+0.24) | **6.83** `[A]` (consensus 6.68, 4 analysts after Q3) | **26.41** (Yahoo 26.72, 11) |
| Net interest income NOK bn | 15.50 | ~15.5 | 15.75 (July repricing in full; 29 Nov repricing one month) | 61.69 |
| Net commissions and fees | 4.49 | — | 4.70 (seasonal) | 17.89 |
| Other income | 1.70 (2.5 underlying) | — | 2.40 (Luminor gone) | 9.09 |
| Operating expenses | 8.63 | — | 9.30 (seasonal) | 35.36 |
| Impairments (bp) | 0.53 (9) | ~0.5 | 0.60 (11) | 2.11 (10) |
| Tax rate | 22% | — | 22% (guided) | 23% |
| CET1 | 17.3% | ~17.6% (before the new programme) | ~17.4% (with Luminor) | FY26 dividend 18.50 `[A]` (70% payout), paid ~5 May 2027 |

- **CET1 roll-forward to 31 Dec 2026 `[A]`:**
  - NOK 205.9bn (30 Sep, factbook) + Q4 profit 9.7 − the rest of the FY26 dividend 8.7 (NOK
    26.1bn for NOK 18.50 a share, less the 17.4bn already deducted at 30 Sep) + Luminor 2.4 =
    **NOK ~209.4bn on REA ~1,203bn → ~17.4%**.
  - That is ~NOK 1.2bn above the 17.3% working level used in the model. The first Update 1
    estimate (210.4bn) did not net the 17.4bn deduction correctly (−NOK 1bn).
  - Of the 2026 AGM authorisation, 0.75% (the remaining 3.5% − 2.75%) is unused.
- **Q4 test (report ~4 Feb 2027):**
  - NII ≥ NOK 15.7bn; lending spread ≥ 1.35%;
  - impairments ≤ 15 bp; stage 2 not above NOK 175bn;
  - C/I ≤ 41% (seasonal);
  - FY26 dividend ≥ NOK 18.25.

## Market input (Equity and HY baseline rows used and how they enter)

| Driver | Baseline row | Bear / **Base** / Bull | How it enters |
|---|---|---|---|
| Scenario frame | Equity BBB scenario definitions (17–18 Oct) | Recession + oil Bear / **trend** / soft landing | Catalysts and timing (Bear from Q1 2027) |
| **NIBOR** | HY BBB 3M NIBOR (unchanged 17 Oct): 2027 4.21 / **4.79** / 4.65; 2028 3.55 / **4.39** / 4.15; 2029 3.50 / **3.86** / 3.65; mid-cycle (2030) 3.25 / **3.45** / 3.45. 2026 average 4.53 (Q1–Q3 actual 4.18 / 4.52 / 4.62 `[F]`, Q4 4.80) | NII effect vs 2026: 2027 −1.0 / **+0.8** / +0.4bn; 2030 −3.8 / **−3.2** / −3.2bn | **NOK 3.0bn of NII per 1 pp** `[A]`. Q3 check: interest on equity +NOK 71m q/q for +0.10 pp NIBOR (≈ 2.8bn/pp annualised incl. repricing) |
| Norwegian growth, unemployment | HY BBB: mainland GDP −0.5 / **1.0** / 1.5 (2027); NAV unemployment 2.6 / **2.3** / 2.1 → 3.0 / **2.4** / 2.2 (2028) | Loan growth 1 / **3.5** / 5% | Volumes, REA growth, personal-customer losses. DNB Carnegie: mainland ~1.5% from 2027, unemployment ~2.1–2.3% `[E]` |
| Credit cycle | HY BBB Nordic FTD 5.6 / **3.0** / 2.3 (2027), 8.6 / **3.5** / 2.2 (2028); E&P, oil-service, shipping, real-estate FTD peaks 15 / 12 / 7 / 6% in Bear | Credit losses 30–40 / **11–13, normalised 15** / 7–9 bp | Sector build above |
| Bank earnings reference | Equity BBB Oslo block F: Bear 0.85 / 0.80 / 0.88, **Base 0.98 / 0.96 / 0.95**, Bull 1.00 / 1.03 / 1.05 of CY27 consensus | DNB (on CY27 consensus 28.27) Bear 0.78 / 0.72 / 0.85, **Base 1.01 / 1.04 / 1.07**, Bull 1.05 / 1.11 / 1.18 | Above block F in Base for named reasons: buybacks (~6% fewer shares by 2029), 3.5% loan growth and +7% fees |
| Exit multiple | Equity BBB: Oslo exit P/E 10.5 / **11.5** / 12.5; exit P/B 1.48 / 1.75 / 1.97; mid-cycle return 8.2 / **9.1** / 9.4% | **9.0 / 10.5 / 11.5** `[A]` | Independent of the IAF ceiling; cross-checked below |
| Index context | Equity BBB Base IRR: Oslo 2.5%, World 5.2%; HY market 6.8% (6.2% after fees) | — | Context only; k is not lowered |

## Common assumptions

- **Earnings build** `[A]`. CY26E = 9M actuals plus Q4E: NII NOK 61.69bn, fees 17.89bn, other
  9.09bn (after one-offs), costs 35.36bn, credit losses 2.11bn. From 2027:
  - NII = prior year × (1 + loan growth) + 3.0 × ΔNIBOR + margin competition (−0.4 / −0.8 /
    −1.0bn cumulative). The repricing lag of the initial run is dropped: Q3–Q4 now carry it.
  - Fees +7% (Base) against DNB's > 9% ambition. 9M26 is +11.9%, partly from a full year of
    Carnegie and a strong ECM year.
  - Other income NOK 9.4–10.0bn (Base); AT1 FX and basis swaps net to zero.
  - Costs +3.5% (2027), then +3%. Tax 23%; AT1 coupons NOK 1.63bn a year.
  - Base CY27: income NOK 92.8bn (consensus 93.3bn), C/I 39.4%, EPS **28.49 (0.8% above
    consensus 28.27)**; the gap is the buyback share count.
- **Credit losses** in bp of customer loans (NOK 2,098bn at 30 Sep, growing with loans): Base
  11 / 13 / 13 / 15; Bear 30 / 40 / 20 / 15; Bull 7 / 8 / 9 / 12. See the credit-loss section.
- **Capital model** `[A]`:
  - CET1 NOK ~209.4bn and REA ~1,203bn at 31 Dec 2026. REA grows with loans; the Bear adds +4% /
    +3% for rating migration.
  - **Buybacks return all capital above a 17.3% working CET1 level** (FSA expectation 16.3% +
    1.0 pp, the buffer DNB holds now). They are done at the start-of-year price path and include
    the state's pro-rata share.
  - Bear: no buybacks while CET1 is below 17.3%.
  - A lower risk-weight floor from 2027 (consultation) would add buyback capacity; it is not in
    Base.
- **Dividends:** FY26 NOK 18.50, paid ~5 May 2027 in all scenarios. Then Base max(prior + 0.50, 65%
  of EPS), Bull max(prior + 0.75, 65%), Bear held at 18.50 (payout 84–91% in 2027–28).
- **Exit:** V_T = exit P/E × 2030 EPS (cum the FY29 dividend). 2030 EPS is at mid-cycle NIBOR and
  normalised losses. **Exit P/E Bear 9.0 / Base 10.5 / Bull 11.5** `[A]`. Anchors: DNB's own
  year-end P/E 12.9 (2021), 9.25, 8.7, 7.7, 9.9 (2025); 12.0 at 30 Sep 2026 on the factbook's
  annualised year-to-date EPS (11.6 on trailing four quarters);
  Oslo exit 10.5 / 11.5 / 12.5. The discount to Oslo is explained in the cross-check below.
- **Interim V_t:** price flat at end-2026; P/E glides from 11.05 (today, on Base CY27) to the exit
  P/E (Bear at 9.0 from end-2027), each on the next year's EPS.

## Period tables and year-end path

**Base** (NOK bn unless stated)

| | 2027 | 2028 | 2029 | 2030 (exit EPS) |
|---|---|---|---|---|
| 3M NIBOR (HY BBB) | 4.79 | 4.39 | 3.86 | 3.45 (mid-cycle) |
| Net interest income | 64.2 | 64.9 | 65.4 | 66.4 |
| Net commissions and fees / other income | 19.1 / 9.4 | 20.5 / 9.6 | 21.9 / 9.8 | 23.5 / 10.0 |
| Total income | 92.8 | 95.0 | 97.1 | 99.9 |
| Operating expenses (C/I) | 36.6 (39.4%) | 37.7 (39.7%) | 38.8 (40.0%) | 40.0 (40.0%) |
| Credit losses (bp of loans) | 2.39 (11) | 2.92 (13) | 3.02 (13) | 3.61 (15) |
| Pre-tax profit | 53.8 | 54.3 | 55.2 | 56.3 |
| Profit to shareholders (after 23% tax and AT1) | 39.78 | 40.21 | 40.89 | 41.69 |
| **EPS** NOK (vs CY27 consensus 28.27) | **28.49** (1.01) | **29.37** (1.04) | **30.27** (1.07) | **31.08** (1.10) |
| Dividend declared for the year (paid next May) | 19.00 | 19.50 | 20.00 | 20.50 |
| Buyback NOK bn (shares, m) | 7.11 (22.6) | 5.79 (18.6) | 5.89 (18.4) | |
| Shares outstanding, year-end (m) | 1,378.5 | 1,359.9 | 1,341.5 | |
| CET1 / ROE | 17.3% / 14.8% | 17.3% / 14.6% | 17.3% / 14.4% | 17.74% / 14.1% |
| BVPS incl. allocated dividend, year-end | 196.5 | 205.2 | 214.3 | 225.4 |

**Bear** (lines that differ)

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| 3M NIBOR | 4.21 | 3.55 | 3.50 | 3.25 |
| NII / fees / other | 60.9 / 16.5 / 7.4 | 59.2 / 17.0 / 8.9 | 60.6 / 18.0 / 9.5 | 62.0 / 19.0 / 9.8 |
| Expenses (+2.5% a year) / C/I | 36.2 / 42.7% | 37.2 / 43.7% | 38.1 / 43.2% | 39.0 / 43.0% |
| Credit losses (bp) | 6.36 (30) | 8.56 (40) | 4.41 (20) | 3.42 (15) |
| EPS | 21.93 | 20.44 | 23.89 | 25.42 |
| Dividend declared | 18.50 | 18.50 | 18.50 | 18.50 |
| CET1 / ROE | 16.97% / 11.5% | **16.52%** / 10.6% | 16.60% / 12.1% | 16.73% / 12.5% |
| BVPS | 192.0 | 193.9 | 199.3 | 206.2 |

**Bull** (lines that differ)

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| 3M NIBOR | 4.65 | 4.15 | 3.65 | 3.45 |
| Total income / C/I | 94.3 / 38.8% | 98.2 / 38.6% | 102.6 / 38.2% | 108.2 / 37.5% |
| Credit losses (bp) | 1.54 (7) | 1.85 (8) | 2.19 (9) | 3.06 (12) |
| EPS | 29.75 | 31.52 | 33.35 | 35.39 |
| Dividend declared | 19.25 | 20.39 | 21.58 | 23.01 |
| Buyback NOK bn | 5.48 | 4.27 | 4.46 | |
| ROE / BVPS | 15.4% / 198.2 | 15.5% / 209.2 | 15.5% / 220.7 | 15.6% / 234.5 |

**Year-end path** (D_t paid in the year; V_t at year-end; r_t in NOK)

| | End-2026 (stub) | 2027 | 2028 | 2029 (exit) |
|---|---|---|---|---|
| Bear: D / V / P/E | 0 / 314.7 / 11.05 | 18.50 / 184.0 / 9.0 | 18.50 / 215.0 / 9.0 | 18.50 / 228.8 / 9.0 |
| Bear: r_t | 0.0% | **−35.7%** | 26.9% | 15.0% |
| **Base: D / V / P/E** | 0 / 314.7 / 11.05 | 18.50 / 312.8 / 10.65 | 19.00 / 319.4 / 10.55 | 19.50 / 326.3 / 10.5 |
| **Base: r_t** | 0.0% | **5.3%** | 8.2% | 8.3% |
| Bull: D / V / P/E | 0 / 314.7 / 11.05 | 18.50 / 346.7 / 11.0 | 19.25 / 375.1 / 11.25 | 20.39 / 407.0 / 11.5 |
| Bull: r_t | 0.0% | 16.1% | 13.7% | 13.9% |

- Base 2027 returns only 5.3%: the P/E falls from 11.05 to the 10.65 glide path. 2028–29 return
  ~8% (a ~6% dividend plus ~2–3% EPS growth, most of it from buybacks).

## V_T bridge (Base, per share), exit cross-check and exit consistency

| Step | NOK/share |
|---|---|
| P (22 Oct 2026) = 11.05 × Base CY27 EPS 28.49 | 314.70 |
| EPS growth to 2030 (28.49 → 31.08; **+2.8% a year** over T), of which buybacks ~+1.8 pp a year (shares −5.6%) | +28.6 |
| De-rating 11.05 → 10.5 (**−1.6% a year**) | −17.0 |
| **= V_T** (10.5 × 31.08) | **326.3** |
| Book value per share at exit / P/B | 214.3 / 1.52 (from 1.72) |

- g = (326.3 / 314.7)^(1/3.19) − 1 = **1.1% a year**; d = 5.7%; c = +0.1 pp. Buybacks run through
  the share count, so retained capital is counted once.

**Exit cross-check against the equity market (skill Step 3)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| Exit P/E (V_T ÷ 2030 EPS) | 9.0 | **10.5** | 11.5 |
| Exit P/B (V_T ÷ BVPS end-2029) | 1.15 | **1.52** | 1.84 |
| ROE 2030 (normalised) | 12.5% | **14.1%** | 15.6% |
| Buyer's implied return at exit (cash yield incl. buybacks at the exit P/E + retained ROE) | 11.4% | **10.2%** | 9.7% |
| Equity BBB Oslo: exit P/E / exit P/B / mid-cycle return | 10.5 / 1.48 / 8.2% | **11.5 / 1.75 / 9.1%** | 12.5 / 1.97 / 9.4% |

- **DNB's exit is priced about 1 pp a year more cheaply than the Oslo index** in every scenario.
  The stated reasons:
  - DNB's own P/E has stayed in a 7.7–12.9 band since 2021 (average 9.7 at year-ends);
  - bank earnings carry rate and credit cyclicality that the market discounts;
  - DNB's normalised ROE (14.1%) is below Oslo's (15.2%).
  - The exit P/B of 1.52 sits inside Oslo's 1.5–2.1 band.
- **Sensitivity on the cross-check:** an exit priced on Oslo's Base mid-cycle return (9.1% → P/E
  ≈ 0.85 ÷ (0.091 − 0.021) ≈ 12.1) gives **Base IRR 11.4%, P_k 309.8 (−1.6%: marginal)**. So at
  NOK 314.70 even an index-consistent exit no longer clears k. The verdict depends on accepting
  that a bank exits below the index multiple; history supports it, and this is the assumption
  that matters most.
- **Exit consistency (Step 3):** the mean-reverting drivers are NIBOR and credit losses. 2030 EPS
  is at each scenario's mid-cycle NIBOR and normalised loss rate.
  - Year 3 vs exit, Base: NIBOR 3.86 vs 3.45 = NOK 0.95bn after tax (2.3% of profit); losses 13 vs
    15 bp = −0.36bn (−0.9%).
  - Bear: losses 20 vs 15 bp = 0.76bn (2.3%).
  - All are below the 10% materiality limit. **No reversion tail.**

## Growth capex test (Step 4)

- Retained CET1 for loan growth: ~NOK 7bn a year in Base (17.3% × REA growth ~NOK 42bn) at an
  incremental ROE of ~14.5% `[A]`, above k. That is mildly value-creating, if new lending is priced
  at today's spreads. Lending spreads stabilised in Q3 (+3 bp q/q) after −40 bp y/y.
- **Buybacks** at P/B 1.72 and ROE ~14.5% earn ~8.4% on the price paid, below k. For a holder they
  are about equal to a dividend reinvested at the market price. They add per-share growth, not
  value, at this price.

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (dated, to the exit value; NOK) | −3.5% | **7.0%** | 14.1% |
| IRR_T in NOK on the Equity BBB NOK path | n/a (NOK cash flows) | n/a | n/a |
| Track A: Rule 1 screen d + g at constant P/E (assumes today's P/E holds; EPS CAGR CY26 underlying 26.91 → CY29) | 5.9 − 3.9 = 2.0% | **6.0 + 4.0 = 10.0% (fails)** | 6.2 + 7.4 = 13.6% |
| d / g / c (dated build) | 5.5 / −9.5 / 0.5 | **5.7 / 1.1 / 0.1** | 5.8 / 8.4 / −0.1 |
| g: of which buyback accretion / P/E re-rating | ~0.5 pp / −6.4 pp | **~1.8 pp / −1.6 pp** | ~1.4 pp / +1.3 pp |
| Structural IRR / cyclical | −3.5% / 0.0 pp: a mid-cycle shift (NIBOR 3.25, losses, P/E 9) | **6.3% / +0.6 pp** (NIBOR at 3.45 from 1 Jan 2027) | 13.4% / +0.6 pp |
| ΣD_t / V_T | 55.50 / 228.8 | **57.00 / 326.3** | 58.14 / 407.0 |
| P_k / margin of safety | 206.1 / −34.5% | **275.2 / −12.5%** | 332.3 / +5.6% |
| Rule 3: P/E vs ceiling (d + g) / k² | 11.7 vs 1.4 | **11.7 vs 7.0 (fails)** | 11.7 vs 9.4 |
| Capital preserved? ΣD + V_T vs P | **No (−9.7%)** | Yes (+21.8%) | Yes (+47.8%) |

- **Structural run:** NIBOR at the scenario's mid-cycle from 1 Jan 2027; Bear and Bull also at
  their normalised loss rate. The cycle adds only ~0.6 pp in Base, because exit EPS is already at
  mid-cycle.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** 6.5%. Not a decision figure.
- **Share of Bull already priced:** (314.7 − 275.2) / (332.3 − 275.2) = **69%** (51% before the
  post-report rise).
- **Bear balance sheet:** no survival question. ROE stays at 10.6–12.5% and book value keeps
  growing. CET1 bottoms at 16.5% (2028), 0.2 pp above the FSA expectation and 1.2 pp above the
  requirement. The headroom is thinner than in the initial run because the 2026 buybacks used
  more capital. A dividend cut is not needed, but a further 1 pp of REA inflation would make it
  likely.
- **E / R (HY rule, NOK):** E = 7.0 − 4.38 = **2.6 pp**; R = Base 2027 (5.3%) − Bear 2027
  (−35.7%) = 40.9 pp; **E / R = 0.063**. That is above World (0.024) and Oslo (−0.07), but a third
  of the HY market reference (0.196).
- **Sensitivities (Base IRR / P_k / margin of safety):**

| Change | IRR | P_k | MoS |
|---|---|---|---|
| Exit P/E 9.5 / 11.5 | 3.9% / 9.8% | 253.6 / 296.9 | −19.4% / −5.7% |
| **Break-even exit P/E** | **12.0% at ~12.3** | 314.7 | 0% |
| Exit on Oslo's mid-cycle return (P/E ~12.1) | 11.4% | 309.8 | −1.6% |
| **Credit losses 15 bp every year** | 6.9% | 274.5 | −12.8% |
| **Credit losses 20 bp every year** | 6.0% | 268.1 | −14.8% |
| **Credit losses 25 / 25 / 25 bp, normalised 20** | 5.8% | 266.8 | −15.2% |
| NIBOR held at ~4.5% through 2030 | 8.8% | 289.5 | −8.0% |
| Market-implied NIBOR 5.1 / 4.9 / 4.8 in 2027–29, mid-cycle unchanged | 7.3% | 277.6 | −11.8% |
| Costs +5% a year / +1.5% a year | 5.0% / 8.5% | 261.2 / 286.9 | −17.0% / −8.8% |
| Loan growth 5% a year | 8.6% | 287.7 | −8.6% |
| No buybacks (excess capital left idle and not priced) | 5.6% | 265.6 | −15.6% |

- **Ranking of what moves the result:** the exit multiple (±1 P/E ≈ ±3 pp) > costs > the NIBOR
  level at exit > credit losses (+5 bp sustained ≈ −1 pp). Credit losses matter most in the Bear,
  where they drive the 2027 drawdown together with the multiple.

## Verdict and caveat

- **Fails: Base margin of safety −12.5%** (below the −2% line). Base IRR 7.0% against k = 12%.
- **Does not survive Bear on capital:** −3.5% a year and a 10% capital loss if a 2027 recession with
  an oil collapse cuts NIBOR to 3.5% and credit losses rise to 30–40 bp, with the P/E at 9. The
  bank stays well capitalised and keeps paying NOK 18.50.
- **What would flip it:** a price near **NOK 275** (−12.5%: Base reaches k). Or one of these:
  - the market keeps pricing DNB at ~12.3x or more through 2029 (an index-consistent exit is
    now only marginal);
  - a Capital Markets Day (10 Nov) that lifts the ROE target to ~16% or frees capital through lower
    risk-weight floors;
  - Norges Bank holding ~4.5% with losses staying near 10 bp.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation or a price target. Returns are
  before tax. Outside a pension wrapper or ASK, a Norwegian holder pays tax on dividends (37.84%
  on the grossed-up share income in 2026 `[E]`), which matters when ~70% of the return is
  dividend.

## Tracking

| Date | Event | Actual vs model | Base P_k (MoS) | Ahead / behind Base |
|---|---|---|---|---|
| 12 Oct 2026 | Initial analysis | — | 277.8 (−8.6% at 304.00) | — |
| 21 Oct 2026 | **Q3 2026 report** | **EPS 6.57 vs 6.33 (+0.24; 7.07 vs ~6.8 excl. Luminor). NII 15.50 vs ~15.5 (on path). Fees 4.49 (+14.6% y/y, ahead). Impairment 0.53 vs ~0.5 (9 bp, on path). CET1 17.3% vs ~17.6% (new 0.75% programme deducted). Dividend: no change (FY26 18.50 assumed). Shares 1,421.8m (on path) + new programme** | **275.9 (−9.6% at 305.30)**: −1.9 in all. The credit-loss re-basing costs −3.6 and removing the 2027 repricing-lag add-back −3.0; fees +7% and other income add +4.7. Q3 actuals, the new buyback, price and date net to ≈ 0 | **Slightly ahead on earnings** (fees, costs), **on path on NII and losses**. The stage-2 rise is a watch item, not yet a loss trend |
| **22 Oct 2026** | **Q3 Excel factbook; first post-report close** | All figures taken from the PDFs confirmed. CET1 start corrected −NOK 1.0bn (the FY26 dividend deduction already at 30 Sep), so ~NOK 1bn fewer buybacks in 2027. Price 305.30 → 314.70 (+3.1%). Consensus CY27 28.14 → 28.27 | **275.2 (−12.5% at 314.70)**: P_k −0.7 from the capital correction; the margin of safety falls 2.9 pp because of the price | On path; the market rewarded the Q3 beat, which takes the price further above the hurdle |

## Risks and signposts

| Signpost | Bear / Bull threshold | Now | Source |
|---|---|---|---|
| 3M NIBOR / Norges Bank policy rate | NB cut before Q3-27 / no cut in 2027 | policy 4.50% (hiked 24 Sep); NIBOR 4.80% (30 Sep) | Norges Bank, factbook `[F]` |
| **Impairment, % of loans annualised** | **> 0.20% two quarters / ≤ 0.06%** | 0.09% (3Q26), 0.09% 9M | Company `[F]` |
| **Stage 2, NOK bn (loans + commitments)** | **> 185 / < 140** | 167.6 (from 130 in Mar) | Factbook `[F]` |
| Stage 3, % of loans | > 1.0% / < 0.75% | 0.86% | Company `[F]` |
| High-risk EAD, NOK bn | > 140 / < 110 | 126.7 | Factbook `[F]` |
| CRE stage 3, NOK bn | > 5.5 / < 3.0 | 4.2 (from 3.2 at Dec) | Factbook `[F]` |
| Combined customer spread | < 1.15% two quarters / > 1.35% | 1.20% (3Q26) | Company `[F]` |
| Net commissions and fees, y/y | < 0% / > +12% | +14.6% (3Q26) | Company `[F]` |
| C/I ratio (reported) | > 42% / < 38% | 39.8% (3Q26), 39.6% 9M | Company `[F]` |
| CET1 vs FSA expectation (16.3%) | headroom < 0.5 pp / > 1.3 pp | 1.0 pp (17.3%) | Company `[F]` |
| NAV registered unemployment | > 2.6% / < 2.1% | 2.1% | HY BBB; Q3 report |
| Nordic HY FTD / Stamdata distress notices | > 5% / < 2.5% | ~3.0% | HY BBB |
| Risk-weight floors (Finanstilsynet consultation) | floors kept or raised / lowered from 2027 | 25% mortgages, 35% CRE, expire end-2026 | Q3 report `[F]` |
| Capital Markets Day targets (10 Nov 2026) | ROE target ≤ 13% or a lower payout / ROE ≥ 16% or a higher distribution path | ROE > 14% | DNB |
| P/E on CY27 consensus | ≤ 9.7 (≈ NOK 275) / ≥ 11.5 | 11.1 | This analysis |
| **Price** | **≤ NOK 275 (Base = k); ≤ NOK 261 (E / R = 0.196)** | NOK 314.70 (21 Oct close) | Yahoo |
| Equity BBB Bear signposts | US HY OAS > 450 bp; Nordic HY spread > 550 bp; USD/NOK > 10.5 | — | `docs/equity-market-bbb.md` |

- **Other risks:**
  - Mortgage and SME price competition: lending spreads −40 bp y/y, stabilising in Q3.
  - The CRE book (NOK 304bn, the largest corporate exposure) with stage 3 rising.
  - Consumer-finance migration in personal customers.
  - The legacy Polish FX mortgage portfolio (provision in 2026).
  - DNB Carnegie's ECM dependence.
  - AT1 FX swings (±NOK 0.5bn a quarter).
  - Oil-related exposure in the Bear (NOK 126bn).
- **Next update:**
  - after Norges Bank (5 Nov) and the Capital Markets Day (10 Nov), if the targets change;
  - otherwise after the Q4 report (Feb 2027) or a baseline update (HY stale after 5 Nov; equity
    after its next run).

## For other modules

- **equity-market-bbb:** **difference, explained (repeated from the initial run).** Block F (DNB,
  STB, GJF) has Base EPS 0.98 / 0.96 / 0.95 of CY27 consensus; DNB's bottom-up Base is 1.01 / 1.04
  / 1.07. The Storebrand analysis flags the same. The gap is buybacks, loan and fee growth.
  - Credit losses are now also re-based in DNB (normalised 15 bp). That narrows the gap, but
    block F still looks low per share.
  - Check at the next update whether block F is per share with buybacks.
  - No change made here.
- **hy-market-bbb:** no gap; the NIBOR path is used as set. DNB's Q3 report is a data point for
  the HY baseline's Base credit view:
  - stage 2 is rising in SMEs, retail, services and manufacturing, while stage 3 is flat;
  - CRE stage 3 is +NOK 1bn since December;
  - fishing stage 3 doubled in Q3;
  - Norges Bank hiked to 4.50% on 24 Sep and signals a further hike cannot be ruled out (check
    the HY rate path at the 5 Nov decision).
- **Portfolio:** no action implied. DNB at NOK 315 does not beat the HY reference on E / R (0.063
  vs 0.196). Watch levels **NOK ~275 (Base = k)** and **~261 (E / R = HY reference)**, not a
  recommendation.

## Change log

- **10 Nov 2026 — note on the Capital Markets Day** (no model change; DNB on hold to 11 Nov): ROE > 15% and cost/income < 38%
  towards end-2028; payout and CET1 policy unchanged. About 0.5 pp above Base ROE for 2028; verdict unchanged (fails).

- **22 Oct 2026 — amendment to Update 1** (no assumption changed except the capital start).
  - Q3 Excel factbook read: every figure taken from the PDFs matches.
  - CET1 at 31 Dec 2026 corrected 210.4 → **209.4bn** (17.4%): DNB had already deducted NOK 17.4bn
    of foreseeable dividends at 30 Sep.
  - **Price 305.30 → 314.70** (first post-report close); valuation date 22 Oct, T 3.19. Consensus
    after Q3: CY26 26.72, CY27 28.27.
  - **Results:** Base IRR 8.2 → **7.0%**, P_k 275.9 → **275.2**, MoS −9.6 → **−12.5%**. Bear −2.4 →
    −3.5% (capital −6.9 → −9.7%). Bull 15.4 → 14.1%. E / R 0.089 → 0.063. Break-even exit P/E
    11.9 → 12.3. The index-consistent exit is now marginal (11.4%, −1.6%). Triggers NOK 275 and
    261.
- **21 Oct 2026 — Update 1 after the Q3 report** (iaf-valuation 2026-10-18.2; equity-market-bbb
  document 17/18 Oct; hy-market-bbb document 17/18 Oct, NIBOR path unchanged).
  - **Price** 304.00 (12 Oct) → **305.30** (20 Oct close, pre-report). Valuation date 21 Oct, T
    3.22 → 3.20.
  - **2026 base** re-set to 9M actuals + Q4E: NII 62.0 → 61.69, fees 17.7 → 17.89, other 8.1 →
    9.09, costs 35.2 → 35.36. The 2027 repricing-lag add-back (+0.5bn) is removed: the July
    repricing is now in Q3–Q4.
  - **Credit losses** Base 10 / 10 / 11 / 12 → **11 / 13 / 13 / 15 bp**; Bear normalised 12 →
    15 bp; Bull 6 / 6 / 7 / 8 → 7 / 8 / 9 / 12 bp. Reasons:
    - stage 2 up NOK 38bn since March and high-risk EAD up NOK 29bn in two years;
    - DNB's full-cycle loss rate (15–20 bp incl. 2016 and 2020) and the portfolio PD × LGD
      (~20 bp), against the benign 2023–26 run (~10 bp).
  - **Fees** Base +6 → +7%, Bull +9 → +10% (DNB's > 9% ambition; 9M +11.9%). Other income +0.1bn a
    year.
  - **Capital and shares:** FSA expectation 16.4 → 16.3%; working CET1 17.3% unchanged (1.0 pp
    buffer). A new 0.75% programme takes shares to ~1,414.6m by year-end and ~13.5m state shares
    are redeemed in 2027. CET1 end-2026 ~17.5%.
  - **Results:** Base IRR 8.6 → **8.2%**, P_k 277.8 → **275.9**, MoS −8.6 → **−9.6%**. Bear −1.7 →
    −2.4%, capital −4.8 → −6.9%. Bull 15.8 → 15.4%. E / R 0.096 → 0.089. Triggers NOK 278 → 276
    and 261 (unchanged).
  - **Method (skill 2026-10-18.2):** exit cross-check table added (exit P/E, P/B, buyer's implied
    return vs Oslo), with the index-return exit as a sensitivity. A credit-loss section was added
    on the user's request.
- **12 Oct 2026 — initial analysis** (iaf-valuation 2026-10-11.3; equity-market-bbb document
  11 Oct 2026; hy-market-bbb document 5 Oct 2026).

## Appendix: own assumptions `[A]`

| Item | Bear | Base | Bull | Basis |
|---|---|---|---|---|
| 3M NIBOR 2027 / 28 / 29 / 2030 | 4.21 / 3.55 / 3.50 / 3.25 | 4.79 / 4.39 / 3.86 / 3.45 | 4.65 / 4.15 / 3.65 / 3.45 | HY BBB (not own); 2030 = mid-cycle |
| NII sensitivity | NOK 3.0bn per 1 pp | same | same | Interest on equity + deposit margins; Q3 bridge consistent; not disclosed by DNB `[?]` |
| Margin competition (cumulative NII effect, NOK bn) | −0.4 / −0.8 / −1.0 / −1.0 | −0.4 / −0.8 / −1.0 / −1.0 | −0.2 / −0.4 / −0.4 / −0.4 | Lending spreads −40 bp y/y; +3 bp q/q in Q3 |
| Loan and REA growth | 1 / 1 / 3 / 3.5%; REA +4% / +3% extra (migration) | 3.5% | 5% | DNB ambition 3–4%; +5.0% y/y (3Q26) |
| Fee growth | −8% then +3% / +6% / +6% | +7% | +10% | DNB ambition > 9%; 9M +11.9% |
| Other income NOK bn (2027–30) | 7.4 / 8.9 / 9.5 / 9.8 | 9.4 / 9.6 / 9.8 / 10.0 | 9.7 / 10.1 / 10.5 / 10.9 | Q3 underlying ~2.5bn a quarter; Luminor gone |
| Expense growth | +2.5% | +3.5% (2027), then +3% | +3.5% | Wage growth 4.1 / 3.8 / 3.5% `[E]`; 9M +3.8% |
| **Credit losses, bp of loans** | **30 / 40 / 20 / 15** | **11 / 13 / 13 / 15** | **7 / 8 / 9 / 12** | Credit-loss section: realised ~10 bp, cycle 15–20 bp, PD × LGD ~20 bp |
| Tax / AT1 coupons | 23% / NOK 1.63bn | same | same | DNB guidance (Q3); factbook |
| FY26 dividend (paid ~5 May 2027) | 18.50 | 18.50 | 18.50 | FY25 18.00 + ambition to raise DPS |
| Dividend rule from FY27 | held at 18.50 | max(prior + 0.50, 65% EPS) | max(prior + 0.75, 65% EPS) | Policy > 50%; 2023–25 cash payout 63–65% |
| Buybacks | none while CET1 < 17.3% | all capital above CET1 17.3% | same | FSA expectation 16.3% + 1.0 pp (DNB's current buffer) |
| Q4-26 | EPS 6.83; NII 15.75; fees 4.70; other 2.40; costs 9.30; losses 0.60 | same | same | Q3 run-rate, seasonality, repricing |
| Exit P/E (2030 EPS) | 9.0 (from end-2027) | 10.5 | 11.5 | DNB 2021–26 year-end 7.7–12.9; cross-check vs Oslo above |

## Appendix: sources

| # | Source | Content | As of |
|---|---|---|---|
| S1 | DNB Q3 2026 quarterly report (ir.dnb.no `202610207179-3.pdf`) | Income statement, key figures, NII components, segments, impairment by industry, notes G5–G7 (stages, allowances, loans by industry), capital (CET1 17.3%, FSA 16.3% / 15.3%), risk-weight floor consultation, future prospects (targets, tax, loan and fee ambitions, dividend policy, 0.75% buyback) `[F]` | 30 Sep 2026, published 21 Oct 2026 |
| S2 | DNB Q3 2026 presentation (`202610207179-1.pdf`) | NII bridge, repricing from 29 Nov, CET1 bridge, impairment by segment and stage, DNB Carnegie macro view `[F/E]` | 21 Oct 2026 |
| S3 | DNB Factbook 3Q26 (PDF `202610207179-2.pdf`; Excel `Factbook_3Q_2026.xlsx`, read 22 Oct) | Stage 1–3 exposure and allowances by industry (1.5.1), quarterly impairment by segment (1.5.5), EAD by industry and risk class (1.6.1), NIBOR, shares, BVPS; own funds (CET1 205,949m, REA 1,190,857m, foreseeable dividends 17,423m), buyback table 1.7.11, DNB Carnegie macro table 3.1.7 `[F/E]` | 30 Sep 2026 |
| S4 | DNB Factbook 2Q26 (Excel) and Q2 2026 presentation | Quarterly history 2Q24–2Q26, buyback table, FSA expectation at end-June `[F]` | 30 Jun 2026 |
| S5 | DNB Capital Markets Day 2024 presentation | Targets 2025–2027, dividend policy `[F]` | 19 Nov 2024 |
| S6 | Newsweb releases via Nordic Financial | Q2 2026, Q4 2025, Q4 2020 (2020 profit and pre-impairment profit), Luminor divestment, basis-swap and AT1 notices `[F]` | 2021–2026 |
| S7 | DNB press release: buyback completed (ir.dnb.no) | Programme 2 shares and price; state redemption 9,796,520 shares, NOK 2,950m `[F]` | 2 Oct 2026 |
| S8 | Yahoo `get_quote`, `quote_summary`, `get_chart` (DNB.OL) | Price 314.70 (21 Oct close; 305.30 on 20 Oct), shares, consensus EPS/revenue after Q3, analyst targets `[F/E]` | 22 Oct 2026 |
| S9 | Norges Bank API `IR/B.KPRA.SD.R` | Policy rate 4.50% `[F]` | 9 Oct 2026 |
| S10 | `docs/equity-market-bbb.md` (17/18 Oct), `docs/hy-market-bbb.md` (17/18 Oct) | Scenarios, block F, Oslo exit P/E and P/B, mid-cycle returns, index IRRs; NIBOR path and mid-cycle, macro and default rows, HY references | 17–18 Oct 2026 |

- **Quality notes:**
  - The Q3 figures come from DNB's own report and factbook (primary). They were first read from
    the PDFs and checked against the Excel factbook on 22 Oct, with no difference.
  - The price is the first post-report close (21 Oct).
  - The 2016 and 2020 loss levels are a recollection `[?]` and an estimate derived from
    2020 profit figures `[A]`; they set the cycle anchor, not the Base path directly.
  - The PD × LGD anchor uses class mid-point PDs and own LGDs; DNB does not publish them per class.
  - Post-Q3 consensus is still thin for quarters (3–4 analysts); annual CY27 has 15.
  - The NII sensitivity to NIBOR is an own estimate.
