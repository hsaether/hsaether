# Storebrand ASA (STB) — IAF analysis, stub Q4 2026 + 2027–2029

**Version 24 Oct 2026**: tracking update after the Q3 2026 report (published Wed 21 Oct 2026,
07:00 CET). Previous version 19 Oct 2026. **Status: kept unchanged.** Q3 moves no decision figure
by the minimum change, so the 19 Oct build and its figures stand. The Q3 actuals, the check run
and what was tested are in **Tracking**.

Skill revisions used: **iaf-valuation 2026-10-18.2** (unchanged since 19 Oct), **equity-market-bbb
2026-10-18.6** (market context and exit references; the baseline document was produced under
2026-10-18.5). Sector inputs:
- `docs/equity-market-bbb.md`, 17 Oct 2026 (amended 18 Oct), **the same version as read on
  19 Oct**: scenarios (Bear = recession H1 2027 plus oil Bear; Base = higher-for-longer rates,
  earnings at trend; Bull = soft landing, P/E holds), Oslo block F ("rates and credit": DNB, **Storebrand**, Gjensidige), Oslo exit P/E 10.5 / 11.5 /
  12.5, exit P/B 1.48 / 1.75 / 1.97, mid-cycle return 8.2 / 9.1 / 9.4%, index Base IRRs (Oslo
  2.5%, World 5.2%), the I-44 NOK path, the HY market reference E / R 0.196. Storebrand is 4.9% of
  the OBX.
- `docs/hy-market-bbb.md`: the 19 Oct build read the 17 Oct version. **For this update the 24 Oct
  version was read** (re-run 24 Oct under hy-market-bbb 2026-10-24.1 and kept unchanged, with no
  path change). Every figure used here is unchanged: **the NIBOR path** (3M NIBOR Bear / Base /
  Bull 4.21 / 4.79 / 4.65 in 2027, 3.55 / 4.39 / 4.15 in 2028, 3.50 / 3.86 / 3.65 in 2029;
  mid-cycle 3.25 / 3.45 / 3.45), the window average 4.38%, Nordic GDP, the Nordic HY market Base
  return 6.8% and the HY market reference E / R 0.196. **Norges Bank decides on 5 Nov 2026.**
- The oil, shipping, rig, supply, defense and AI baselines are not used directly; the oil Bear
  enters through the equity and HY Bear.

## Summary

**Verdict**
- **24 Oct (Q3 report): verdict and figures unchanged.** Q3 was on the Base path:
  - group profit NOK 1,517m (model ~1.48bn), a record operating profit of NOK 1,162m (+7% y/y),
    combined ratio 87% and solvency 200%;
  - the EPS miss (2.54 against 2.81 consensus) is the 32% tax rate from SEK hedges; at 21% tax
    EPS would have been ~2.90;
  - the Board intends a dividend of ~NOK 6 for 2026 and buybacks of NOK 2bn for 2027, which is
    exactly the Base assumption.

  A check run at the 23 Oct close (NOK 188.40) with the Q3 actuals gives Base IRR 5.7% (standing
  5.3%), P_k 158.3 (156.9) and a margin of safety of −16.0% (−17.0%). That is inside the minimum
  change, so the 19 Oct figures below stand.
- **Fails.** Base IRR **5.3% a year** (NOK) against k = 12%. Hurdle price **P_k ≈ NOK 157 vs
  P NOK 189.00 (19 Oct build; 23 Oct close 188.40): margin of safety −17.0%.** Rule 3 fails (P/E
  16.6 on CY26E against a ceiling of 8.8). The Rule 1 screen passes (d + g = 3.2 + 9.4 = 12.6%)
  only because it assumes today's P/E holds.
- **A business on plan at a price that already pays for the plan.** Base meets the Capital Markets
  Day ambition (group profit ~NOK 7.1bn in 2028; ROE ~16.5–17%), and buybacks of NOK 2bn a year
  cut the share count ~2.4% a year. EPS rises ~6% a year from 2027 to 2030. But the share trades
  at **14.6x Base CY27 EPS** (13.9x consensus) and P/B 2.48, after re-rating from ~10–11x forward in
  2023–24. With the exit P/E at 13.0 the de-rating takes ~3.6% a year, and the return is a 3.2%
  dividend plus ~2% value growth.
- **Bear breaks the thesis on capital:** −7.2% a year, ΣD + V_T 20% below P. Total return is −39%
  in 2027: fees fall with markets, profit sharing collapses, and the P/E goes to 10.5 on recession
  earnings. Storebrand itself stays well capitalised (solvency 200% against a 175% buyback line);
  buybacks pause in 2027 and the NOK 6.00 dividend is held.
- **What the price needs:** an exit P/E of **~16.0** (Base 13.0; today 14.6), or operating profit
  growth of ~14% a year. Even Bull (P/E holds at 14.5, op profit +10–12% a year) clears only
  marginally (+2.4%).
- **Against the equity and HY baselines:** Base 5.3% beats Oslo (2.5%), equals World (5.2%) and is
  below the Nordic HY market (6.8%). **E / R = 0.021** against the HY reference 0.196.
  **Triggers: NOK ~157 (−17%, Base = k) and NOK ~139 (−27%, E / R = 0.196); pre-alert NOK ~181
  (−4%, Base = the HY market's 6.8%).**

**Decision table (NOK, per share)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T | −7.2% | **5.3%** | 12.9% |
| IRR_T on the Equity BBB NOK path (30% of earnings SEK/DKK on I-44) | −6.6% | 5.3% | 12.7% |
| V_T (31 Dec 2029, cum the FY29 dividend) | 133.0 | **202.0** | 253.4 |
| P_k / margin of safety | 107.7 / −43.0% | **156.9 / −17.0%** | 193.6 / +2.4% |
| Capital preserved? (ΣD + V_T vs P) | **No: −20.1%** | Yes: +17.2% | Yes: +45.0% |
| ΣD_t paid 2027–29 (cash dividends) | 18.00 | **19.44** | 20.70 |
| Buybacks 2027–29 (NOK bn) / shares at end-2029 | 2.5 / 395m | **6.0 / 386m** | 7.5 / 381m |
| BVPS end-2029 / exit P/B | 89.9 / 1.48 | **92.1 / 2.19** | 90.6 / 2.80 |
| Balance sheet | Solvency falls with equities and rates; buybacks paused in 2027, NOK 1.0–1.5bn from 2028; dividend held at 6.00 | Solvency held ~190–200% with NOK 2bn buybacks a year (total payout ~85%) | Same as Base, buybacks NOK 2.5bn a year |
| *24 Oct check run (P 188.40, Q3 actuals): IRR_T / P_k / margin of safety* | *−6.9% / 108.6 / −42.4%* | *5.7% / 158.3 / −16.0%* | *13.4% / 195.4 / +3.7%* |

**Per-share path (NOK; Track A rows; calendar years = fiscal years)**

| | CY26E (9M actual + Q4 cons.) | 2027 | 2028 | 2029 | 2030 (exit EPS) |
|---|---|---|---|---|---|
| Base group profit, NOK bn (before amortisation and tax) | 6.26 (9M 4.67 `[F]` + Q4E ~1.59); 19 Oct: 6.22 | 6.74 | 7.08 | 7.36 | 7.59 |
| Base EPS (adjusted for amortisation) | 11.18 (9M 8.07 `[F]` + Q4 cons. 3.11); 19 Oct: 11.36 | 12.94 | 13.94 | 14.87 | 15.54 |
| Base EPS growth | (−0.6% vs 11.25 in 2025; 9M tax rate 28.5%) | +15.7% (+13.9% on the 19 Oct CY26E) | +7.7% | +6.7% | +4.5% |
| Base D_t paid (~23 Apr) | — | 6.00 (FY26; Board intends ~6 `[F]`) | 6.47 | 6.97 | (7.44 FY29, in V_T) |
| Base buyback, NOK per share outstanding | ~4.8 (NOK 2bn; 1.51bn done by 30 Sep `[F]`) | 4.80 | 4.92 | 5.05 | |
| Base ROE (on opening book) / BVPS year-end | 15% LTM (Q3) / 79.6 (81.2 incl. Knif in the check run) | 15.9% / 83.8 | 16.4% / 87.8 | 16.7% / 92.1 | 16.9% |
| Base V_t (year-end) / P/E on next year | 189.0 (stub flat) | 196.1 / 14.07 | 201.3 / 13.54 | 202.0 / 13.0 | |
| Bear EPS / D_t / V_t | | 9.11 / 6.00 / 109.2 | 10.40 / 6.00 / 122.7 | 11.69 / 6.00 / 133.0 | 12.67 |
| Bull EPS / D_t / V_t | | 13.46 / 6.00 / 215.9 | 14.82 / 7.00 / 235.8 | 16.22 / 7.70 / 253.4 | 17.47 |

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value ·
`[E]` external or secondary · `[C]` carried from an earlier version · `[A]` own assumption ·
`[?]` not found or unverified.

## Header

| Item | Value |
|---|---|
| Company | Storebrand ASA, Oslo Børs: **STB**. Nordic savings, pension and insurance group: Savings (unit linked DC pensions in Norway and Sweden/SPP, Storebrand Asset Management incl. AIP and Kron, Storebrand Bank), Insurance (retail P&C ~8% Norwegian market share, health, group life, disability), Guaranteed pensions (paid-up policies and DB in long-term run-off; public-sector pensions growing), Other (company portfolios, holding) `[F]` |
| Price (P) | **NOK 189.00** (entry price of the standing build), Yahoo `STB.OL`, close 19 Oct 2026 (14:29 UTC). **23 Oct close NOK 188.40** (Yahoo, 14:25 UTC; −0.3% vs 19 Oct) `[F]`. Around the report: 20 Oct 190.60, 21 Oct 194.50 (+2.0%), 22 Oct 190.00, 23 Oct 188.40. 52-week range 155.1–208.2 `[F]`. Ex the FY25 dividend (ex-date 10 Apr 2026); cum the FY26 dividend |
| Valuation date / exit date | 19 Oct 2026 / 31 Dec 2029, **T = 3.20 years** (standing build). Check run: 24 Oct 2026, T = 3.19 |
| Shares | **418.41m outstanding** (Yahoo, 23 Oct) `[F]`. This includes the **2,746,582 new shares issued for Knif Trygghet on 16 Oct** (Q3 report, Outlook) `[F]`. Filing check: 424,763,636 shares issued less 8,676,139 own shares = **416.09m at 30 Sep** (Q3 report, Storebrand ASA equity note) `[F]`; adding Knif gives 418.83m, and the ~0.4m gap is October buybacks `[A]`. The standing build used 415.66m with ~3.0m Knif shares in Q1 2027 (416.8m into 2027). The check run has 416.3m at end-2026, −0.1% |
| Market cap | NOK 78.8bn (Yahoo, 23 Oct). Book value per share **NOK 78.10** at 30 Sep (equity NOK 33,223m less hybrid capital 353m and non-controlling interests 375m = 32,495m, on 416.09m shares; Yahoo 78.10) `[F]` → **P/B 2.41** at 188.40. On 19 Oct: 76.15 (30 Jun) and P/B 2.48 |
| P/E (at 188.40) | **16.9x** CY26E EPS 11.18 (9M actual 8.07 + Q4 consensus 3.11, 5 analysts, range 2.96–3.33). Yahoo's annual 11.63 (9 analysts) has not absorbed the Q3 tax hit `[?]`. **13.9x** CY27 consensus (13.58, 10 analysts; range 12.56–14.45); **14.6x** Base CY27 (12.94) on 189.00, 14.5x on 188.40. Trailing 18.0x (Yahoo, on IFRS EPS 10.47) |
| NAVs (Step 3) | Not applicable (insurer; Track A). Book value is the anchor: P/B 2.48 at ROE ~16–17% implies a required return of ~**9.2%** (P/B = (ROE − g)/(r − g), ROE 17%, g 4%) `[A]`; 9.4% at P/B 2.41 |
| Capital | **Solvency II ratio 200%** (30 Sep 2026; 200% at Q2, 206% at Q1). Thresholds: 175% for buybacks and special dividends, 150% for ordinary dividends `[F]`. The disclosed single stresses (rates ±100 bp, equities −25% with SA −15 pp, spreads +50 bp with VA +15 bp, property −10%) leave the ratio between **191% and 210%** `[F]`. These are chart values; which value belongs to which stress cannot be read reliably from the extracted text `[?]`. The Solvency II amendments and the new rules for guaranteed products add **more than 10 pp from Q1 2027** `[F]`, and the company states that solvency is currently not a binding constraint on capital distribution. Storebrand ASA: liquid assets NOK 5.7bn, interest-bearing debt NOK 1.0bn, unused RCF EUR 200m `[F]`. S&P 'A' (2022 upgrade) `[E]` |
| FX | NOK report and price. SPP (Sweden) and part of asset management earn in SEK/DKK: ~30% of earnings `[A]`. NOK appreciation against SEK, through the hedges, lifted the tax rate in Q1 2026 (NOK +7%, tax 36%) and in Q3 2026 (NOK +6%, tax 32%) `[F]`. FX exposure by sub-segment (Q1 2026, rounded): UL Norway 65% NOK / 35% other foreign; UL Sweden 40% SEK / 60% other; asset management 35% NOK / 20% SEK / 45% other `[F]` |
| Track | **A** (EPS, P/E, d + g) with a dated IRR to an independent exit P/E and P_k, as in the DNB and Handelsbanken analyses. Not capital-intensive in the capex sense; the cyclical drivers (markets, NIBOR, claims) are tested in Bear and the structural run |
| k | **12%**, not raised: 'A' rating, solvency 200%, liquid share (~0.5m shares, ~NOK 95m a day) |
| Horizon | Stub Q4-26 (Q3 reported 21 Oct 2026) + 2027–2029 annual; exit on 2030 EPS (at mid-cycle NIBOR). **Next report: Q4/FY26 on 10 Feb 2027** (financial calendar in the Q3 presentation) `[F]` |

**Sources (connector · document · period):**
- **Storebrand IR** (storebrand.no, quarterly reporting 2026; PDF links collected with WebFetch):
  the **Q3 2026 interim report**, 45 pages, parsed with Nordic Financial `parse_pdf_to_text`. It
  gives the group, segment and product-line tables, capital situation, outlook and dividend policy,
  and the Storebrand ASA equity note. Also the **Q3 2026 analyst presentation**, 32 pages: capital
  distribution, solvency sensitivities, Knif key figures, special items and the financial
  calendar. Both are dated 21 Oct 2026 (the Board signed on 20 Oct).
- **Nordic Financial** (`company_research`, `search_filings`; ticker STB, 2022–2026): Q3 2026
  results release (Newsweb, 21 Oct 2026 07:00 CET, English and Norwegian), Q2 2026 (15 Jul 2026),
  Q1 2026 (29 Apr 2026), Q4 2025 (11 Feb 2026), Q3 2025, Q2 2025; Knif Trygghet letter of intent
  (29 Jan 2026) and negotiated agreement (11 Jun 2026); Q2 and Q3 2026 invitations.
- **Yahoo** (23 Oct 2026 close): price and daily closes 12–23 Oct, shares 418.41m, BVPS 78.10,
  `earningsTrend` (Q4-26 3.11, 5 analysts; CY26 11.63, 9; CY27 13.58, 10), `financialData`
  (target mean NOK 206.6, median 218.5, range 143–245, 10 analysts; recommendation 1.9, "buy").
  The 19 Oct inputs: dividend history (3.25 / 3.50 / 3.70 / 4.10 / 4.70 / 5.40 for FY20–FY25) and
  month-end closes 2020–2025.
- **FinancialFilings:** not available. The monthly quota is used up (HTTP 429; it resets
  1 Nov 2026), so the `filings_list` check for share issues and insider trades could not run. It is
  covered by the Newsweb stream and the Q3 report's equity note (Knif share issue, own shares).
- **Not found `[?]`:** the full split of the financial result between company-portfolio interest
  and debt cost. Now disclosed: net profit sharing and the risk result per quarter, company
  portfolios of NOK 29.0bn, and group interest expense of NOK 187m a quarter. The mapping of the
  solvency sensitivity values to each stress (range only). The CMD 2025 presentation itself;
  targets are taken from the Q3 2026 report's Outlook section, which restates them.

## Scenario definitions (from Equity Market BBB and HY Market BBB)

| Scenario | Catalyst | What it does to Storebrand |
|---|---|---|
| **Base** (decision) | Equity Base: higher-for-longer rates, earnings at trend, World +5.2% / Oslo +2.5% a year. HY Base: NIBOR 4.79 / 4.39 / 3.86, mid-cycle 3.45 | Operating profit +9 / +8 / +7 / +6% a year (fees on AUM growth ~market + flows, insurance premiums +10% at a combined ratio ~90%, costs +5% as guided). Financial result 1.85 → 1.61bn as NIBOR falls, partly offset by profit sharing rising with the paid-up policy reform. Group profit 6.74 / 7.08 / 7.36bn (CMD: 7bn in 2028). Buybacks NOK 2bn a year; dividend 50% of adjusted EPS; exit P/E 13.0 |
| **Bear** (stress) | Equity Bear: recession H1 2027 + oil Bear; Oslo −28.5%, World −20.6% in NOK in 2027; P/E compression. HY Bear: NIBOR 4.21 / 3.55 / 3.50, mid-cycle 3.25; Nordic defaults peak 8.6% (2028) | Operating profit −12% in 2027 (AUM-linked fees fall, disability and P&C claims rise), then +6 / +9 / +8%. Profit sharing 0.10 / 0.35 / 0.50 / 0.60bn and a −0.3bn mark-to-market loss on the company portfolios in 2027. EPS 9.11 / 10.40 / 11.69 (0.67 / 0.76 / 0.86 of CY27 consensus). Buybacks paused in 2027, then NOK 1.0 / 1.5bn; dividend held at 6.00; P/E 10.5 (Oslo Bear exit) from end-2027 |
| **Bull** (stress) | Equity Bull: soft landing, first NB cut Q3-27, P/E holds; NIBOR 4.65 / 4.15 / 3.65 | Operating profit +12 / +11 / +10 / +9% (AUM +~10% a year, CR ~88%); profit sharing 0.80–0.90bn. Group profit 6.99bn in 2027 (≈ consensus), 8.44bn in 2030; ROE 18–19%. Buybacks NOK 2.5bn a year; exit P/E 14.5 (today's multiple holds) |

The stub (19 Oct–31 Dec 2026) is the same in all scenarios: quarter consensus for Q3/Q4 in the
standing build (Q3 is now actual, see Tracking), the remaining 2026 buyback (~NOK 0.35bn assumed;
NOK 486m was left at 30 Sep `[F]`), no dividend before April 2027, price flat by convention. Bear
and Bull diverge from 1 Jan 2027.

## Company and status

| Key figures `[F]` (NOK m; Q3 2026 report) | 3Q26 | 2Q26 | 1Q26 | 4Q25 | 3Q25 | FY 2025 |
|---|---|---|---|---|---|---|
| Fee and administration income | 2,139 | 2,031 | 2,097 | 2,382 | 2,124 | 8,573 |
| Insurance result (combined ratio) | 895 (87%) | 889 (87%) | 665 (93%) | 643 (93%) | 697 (89%) | 2,444 (92%) |
| Operational cost | −1,872 | −1,801 | −1,736 | −1,894 | −1,730 | −7,042 |
| **Operating profit** (cash equivalent earnings from operations) | **1,162** | **1,119** | **1,026** | **1,131** | **1,091** | **3,975** |
| Financial items and risk result (of which net profit sharing) | 355 (82) | 680 (242) | 327 (82) | 384 (157) | 495 (184) | 1,720 (599) |
| **Group profit** (before amortisation and tax) | **1,517** | **1,799** | **1,353** | **1,515** | **1,586** | **5,695** |
| Profit after tax and amortisation (effective tax rate) | 996 (32%) | 1,380 (20%) | 825 (36%) | 1,149 (20%) | 1,189 (18%) | 4,469 (16%) |
| EPS adjusted for amortisation (NOK) | 2.54 | 3.43 | 2.10 | 2.88 | 3.08 | 11.25 |
| Cash ROE, quarter annualised (LTM) | 14.4% (15%) | 20.3% (16%) | 12.3% (15%) | 17.4% | 19.0% | 18.4% |
| Solvency II | 200% | 200% | 206% | 194% | 195% | 194% |
| AUM (NOK bn) | 1,633 | 1,658 | 1,543 | 1,609 | 1,561 | 1,609 |
| Equity, total (NOK m) | 33,223 | 32,606 | 33,982 | 33,588 | 32,496 | 33,588 |

The 19 Oct table carried approximations that the Q3 report now replaces: 3Q25 operating profit
1,091 (was ~1,000 `[A]`), FY25 operating profit 3,975 (was ~3,880 `[A]`) and the 4Q25 financial
result 384 (now `[F]`). The 2Q25 column has been dropped; its figures are in source S4.

| Group profit by segment `[F]` (NOK m) | 3Q26 | 2Q26 | 1Q26 | 4Q25 | 3Q25 | 9M26 | 9M25 | FY25 |
|---|---|---|---|---|---|---|---|---|
| Savings (non-guaranteed) | 800 | 708 | 738 | 816 | 815 | 2,245 | 2,109 | 2,925 |
| Insurance | 485 | 480 | 283 | 266 | 364 | 1,247 | 796 | 1,062 |
| Guaranteed pension | 191 | 424 | 296 | 297 | 316 | 912 | 933 | 1,229 |
| Other | 41 | 187 | 37 | 136 | 91 | 265 | 343 | 479 |
| **Group** | **1,517** | **1,799** | **1,353** | **1,515** | **1,586** | **4,669** | **4,180** | **5,695** |

- **Q3 2026 by segment** `[F]`:
  - **Savings 800m (815m).** Fees +2% (+3% ex FX). Performance fees were only NOK 23m (90m), and
    asset-management fees rose 10% excluding them. Savings costs +1.6%, and asset-management costs
    fell 5%.
  - Within Savings by product line: UL Norway 208m (+17%), UL Sweden 97m (+10%), asset management
    343m (flat; it includes a NOK 54m earn-out revaluation gain on AIP), retail banking 151m
    (208m, narrower margin). Net UL inflow NOK 3.0bn in Norway and 0.8bn in Sweden. Large Norwegian
    corporate pension mandates of NOK 4.4bn were won, with assets to transfer over the coming
    quarters.
  - **Insurance 485m (364m, +33%).** Premiums f.o.a. +17%; CR 87% (89%).
    - Retail: 370m, CR 82%, premiums +19%, market share 8.3% (7.6%). A Drammen fire cost ~NOK 55m.
    - Corporate: 115m, CR 94%.
    - Portfolio premiums NOK 11.3bn (+10%). Corporate portfolio premiums were flat after a large
      outflow.
  - **Guaranteed pension 191m (316m).** Net profit sharing was 82m (184m), hit by rising interest
    rates and wider credit spreads, mostly in Sweden. Guaranteed reserves fell NOK 9bn in the
    quarter to 289bn. Buffer capital 8.6% (Norway) / 31.2% (Sweden). The excess value of bonds at
    amortised cost fell NOK 2.5bn to −14.0bn.
  - **Other 41m (91m).** The company portfolios (NOK 29.0bn) returned 1.2% in Norway and 0.3% in
    Sweden, with mark-to-market losses from rising rates. The segment also carried NOK 20m of
    one-off project costs and Knif deal costs.
- **Group** `[F]`:
  - Fee income +0.7% y/y; +6% adjusting for currency and performance fees.
  - Costs +8% y/y in the quarter. That includes NOK 20m one-off and insurance commissions on
    strong sales (+NOK 16m). Costs are +5% year to date, in line with the CMD guidance.
  - Operating profit +7% (+14% excluding performance-based income). Year to date it is NOK 3,307m,
    +16%.
  - The financial result, NOK 355m (495m), is where the rate rise in the quarter hit.
- **Tax** `[F]`: 32% in Q3 and 28.5% for 9M, against a normal 19–22%. The cause is SEK hedges as
  the NOK rose ~6% against SEK. CY26 EPS (11.18) is depressed by roughly 7% against a normal tax
  year.
- **Guaranteed pensions** are in long-term run-off and release capital. The net flow excluding
  transfers was −NOK 3.1bn in the quarter. The expected return in Norway is 5.1% against an
  average guarantee of 2.8%, i.e. +230 bp (analyst presentation) `[F]`. New paid-up policy rules
  from 1 Jul 2026 allow longer-horizon, higher-risk investment, and collective guaranteed schemes
  follow from 2027 `[F]`.
- **Targets (CMD Dec 2025, restated in the Q3 Outlook)** `[F]`:
  - Group profit **NOK 7bn and ROE 17% in 2028**.
  - Operating cost growth ~5% a year from NOK 7bn in 2025.
  - UL AUM double-digit growth a year; asset-management AUM +7–9% a year; bank loan growth > 5%.
  - Insurance premiums double-digit growth a year; combined ratio from 92% (2025) to 90% or better
    by 2028.
  - Profit sharing from ~NOK 600m in 2025 to NOK 700m in 2028. The Base path (0.65 / 0.70 / 0.75bn)
    is on this guidance.
  - **Double-digit annual DPS growth 2025–2028**, with an ordinary dividend at least the prior
    year's nominal amount.
  - Buybacks guided at NOK 1.5bn a year 2027–2030. The 2030 cumulative ambition was **lifted to
    ≥ NOK 13.5bn** (from ≥ 12bn): ~7.0bn executed 2022–2026 plus 2.0 + 1.5 + 1.5 + 1.5 planned
    (analyst presentation p. 4).
  - The CEO says Storebrand is well on track for the 2028 targets.
- **Capital return 2026–27** `[F]`:
  - Buybacks of NOK 1,514m executed in 9M (514m in Q3); NOK 486m remained at 30 Sep for the
    tranche that ends no later than 18 Dec.
  - The Board intends a dividend of **~NOK 6 for 2026** (~+10%) and **NOK 2bn of buybacks for
    2027**, up from the guided 1.5bn, subject to market conditions and approvals.
  - Total payout (LTM) 85%: dividends 51%, buybacks 34%.
  - Base has FY26 6.00 and NOK 2.0bn a year: on the announced plan for 2027, and above the 1.5bn
    guidance for 2028–29. For context, 2026 was guided at 2.0bn and is on track, and 2027 is now
    2.0bn against the 1.5bn guide.
- **Knif Trygghet** `[F]`:
  - Completed 16 Oct 2026, paid with 2,746,582 new shares (NOK 560m, ~NOK 204 a share; dilution
    0.66%). Merger with Storebrand Forsikring is expected in 2027.
  - H1 2026: profit before tax NOK 70m, gross premiums earned NOK 418m, CR 77%.
  - The standing build has the deal in Q1 2027 with ~NOK 40m a year of operating profit `[A]`; see
    Tracking for the check.
- **Regulation** `[F]`:
  - The Competition Authority decided against KLP on 25 Aug 2026 (positive for the municipal
    market). The ESA complaints are pending.
  - A revenue-sharing bill for asset managers is expected to pass this autumn.
  - From 1 Jan 2027, bonds at amortised cost are marked to market when a customer moves provider.
  - The IRRD proposal is a NOK 25bn crisis fund, 12.5bn pre-funded over 10 years (cost risk; the
    industry opposes it).
- **Market view** `[E]` (Yahoo, 23 Oct):
  - 10 analysts, mean target NOK 206.6 (+10% on 188.40), median 218.5; recommendation 1.9 ("buy").
  - Consensus EPS: CY27 13.58 (10 analysts; 13.61 on 19 Oct); Q4-26 3.11 (5; 3.02 seven days
    earlier).

## Near term: stub (all scenarios)

| NOK | Q3-26 **actual** `[F]` (19 Oct model) | Q4-26E | CY26E |
|---|---|---|---|
| EPS (adjusted) | **2.54** (cons. 2.81, 7 analysts; ~2.90 at 21% tax) | 3.11 (cons., 5 analysts; 2.96–3.33) | **11.18** (9M 8.07 + Q4 cons.); 19 Oct 11.36 |
| Operating profit NOK bn | **1.162** (~1.15 `[A]`) | ~1.18 `[A]` (+ Knif from 16 Oct) | ~4.49 (19 Oct: 4.45) |
| Group profit NOK bn | **1.517** (~1.48 `[A]`) | ~1.59 `[A]` | ~**6.26** (19 Oct: 6.22) |
| Tax rate | **32%** (21% `[A]`) | 21% `[A]` | ~27% |
| Buyback | **0.514bn** executed (~0.4bn `[A]`) | 0.486bn left at 30 Sep, to 18 Dec `[F]` | NOK 2.0bn `[F]` |
| Dividend accrued (paid ~23 Apr 2027) | | | **6.00** `[A]`; Board intends ~NOK 6 `[F]` |
| Solvency | **200%** (~200% `[A]`) | | |

- **The Q3 test set on 19 Oct, scored** `[F]`:
  - Operating profit ≥ NOK 1.10bn: **1.162, pass**.
  - Insurance CR ≤ 90%: **87%, pass**.
  - Fee income above NOK 2.05bn: **2.139, pass**.
  - Financial result ≥ NOK 0.35bn: **0.355, pass** (narrowly).
  - Solvency ≥ 195%: **200%, pass**.
  - Costs within +5% y/y: **+8% in the quarter, fail**. Year to date is +5%; the quarter includes
    NOK 20m one-off and growth-driven insurance commissions.
  - Normal tax: **32%, fail**, from the SEK hedges; non-recurring.
  - **The low-growth flag** ("a second quarter of flat fees with rising costs") **fired in its
    letter**: fees +0.7% y/y and costs +8%. **It is not adopted.** Operating profit still grew 7%
    (14% ex performance fees), and 9M operating profit is +16%, above Base 2027's +9%. The cost
    growth comes with insurance premium growth of 17%, and Savings costs grew only 1.6%. The 6%
    operating-growth sensitivity stays a sensitivity (check run: Base IRR 4.4%).
- **Book roll-forward to 31 Dec 2026:**
  - Standing build `[A]`: NOK ~32.9bn, BVPS ~79.6 on 413.8m shares, before Knif.
  - Check run: equity to shareholders NOK 32.50bn at 30 Sep `[F]` + Knif 0.56bn `[F]` + Q4 profit
    ~1.24bn − Q4 buybacks 0.49bn = **NOK ~33.8bn, BVPS ~81.2 on 416.3m shares** `[A]`.
- Dividend timing: AGM early April, ex-date ~10 April, payment ~3rd week of April `[F/A]`
  (2021–2026 ex-dates 7–14 April). The FY26 proposal and the 2027 buyback start come with the
  **Q4 report on 10 Feb 2027** `[F]`.

## Market input (Equity and HY baseline rows used and how they enter)

| Driver | Baseline row | Bear / **Base** / Bull | How it enters |
|---|---|---|---|
| Scenario frame | Equity BBB scenario definitions | Recession + oil Bear / **trend** / soft landing | Catalysts and timing (Bear from Q1 2027) |
| Equity markets → AUM, fees, profit sharing | Equity BBB: Oslo 2027 −28.5 / **0.7** / 5.2%; World NOK −20.6 / **5.6** / 13.4%; window World −1.7 / **5.2** / 10.2% | Operating profit 2027 −12 / **+9** / +12%; profit sharing 0.10 / **0.65** / 0.80bn | Fee income tracks AUM (~1,658bn, ~60% equity-linked `[A]`); profit sharing needs a customer return above the guarantee |
| **NIBOR** | HY BBB 3M NIBOR: 2027 4.21 / **4.79** / 4.65; 2028 3.55 / **4.39** / 4.15; 2029 3.50 / **3.86** / 3.65; mid-cycle 3.25 / **3.45** / 3.45; 2026 average ~4.53 | Financial result (ex profit sharing) 1.05 / **1.20** / 1.16bn in 2027 → 0.81 / **0.86** / 0.86bn in 2030 | **NOK 0.25bn pre-tax per 1 pp** `[A]`: company portfolios (mostly Norwegian and Swedish interest-bearing) net of floating-rate debt. Calibrated: 0.25 × 4.53 + profit sharing ~0.64 ≈ the 2026E financial result 1.77bn. Q3 check: company portfolios NOK 29.0bn `[F]` ≈ 0.29bn per pp before floating-rate debt, so 0.25 holds. 2026E financial items are now ~1.74bn (9M 1.362bn `[F]` + Q4 ~0.38bn) |
| Credit cycle | HY BBB Nordic FTD 5.6 / **3.0** / 2.3% (2027), Bear peak 8.6% (2028) | Bear −0.3bn MTM in 2027 | Company-portfolio credit spreads; bank losses are small (mortgage book ~NOK 95bn) |
| Exit multiple | Equity BBB Oslo exit P/E 10.5 / **11.5** / 12.5; block F P/E 12.0 on CY27 | **10.5 / 13.0 / 14.5** `[A]` | Independent of the IAF ceiling (below) |
| Index context | Equity BBB Base IRR: Oslo 2.5%, World 5.2%; HY market 6.8% | — | Context only; k is not lowered |

24 Oct: every row is unchanged. Equity BBB is the same version (17 Oct, amended 18 Oct). The HY
BBB 24 Oct re-run kept its paths: NIBOR, FTD, the HY return of 6.8% and the reference E / R of
0.196.

## Common assumptions

- **Earnings build** `[A]` on Storebrand's own "group profit" format (before amortisation of
  acquired intangibles and tax):
  - Group profit = operating profit + profit sharing + 0.25 × NIBOR (+ Bear MTM). 2026E: operating
    profit 4.45bn (H1 2.145 + Q3/Q4 ~1.15/1.18), financial result 1.77bn.
  - Knif +0.04bn operating profit from 2027.
  - Tax 21% (middle of the 19–22% guidance). EPS is "adjusted for amortisation", the company's and
    the consensus basis; amortisation (~NOK 0.25bn a year after tax) reduces book only. Hybrid
    tier 1 coupons are not modelled separately `[?]`.
  - Base CY27 group profit 6.74bn; EPS **12.94, 4.9% below consensus 13.61**. About 1.5 pp is the
    usual Year-1 haircut on consensus; the rest is the falling NIBOR (−0.25bn from 2026 by 2029)
    that consensus may not carry.
- **Capital and distributions** `[A]`:
  - Dividend FY26 NOK 6.00 (paid ~23 Apr 2027, all scenarios).
  - From FY27: Base max(prior + 0.30, 50% of EPS); Bull max(prior + 0.40, 52%); Bear held at 6.00
    (payout 66% of 2027 EPS).
  - Buybacks Base NOK 2.0bn a year, Bull 2.5bn, Bear 0 / 1.0 / 1.5bn. Bought at the start-of-year
    value path; run through the share count and EPS, not D_t.
  - Total payout Base ~85% of profit, as in 2025 (85%); funded by profit plus the run-off capital
    release. Solvency is not modelled line by line `[?]`.
  - **24 Oct, against the Q3 report** `[F]`:
    - FY26 ~6 and the 2027 NOK 2bn buyback confirm the standing assumptions.
    - The CMD guidance of double-digit DPS growth to 2028 sits above the Base rule for FY27–28:
      6.47 (+7.8%) and 6.97 (+7.7%) against ≥ 6.60 and ≥ 7.26.
    - The buyback guidance (1.5bn a year in 2028–29) sits below Base's 2.0bn.
    - The two differences pull in opposite directions: +0.05 pp and −0.4 pp on Base IRR in the
      check run (see Tracking). Both are kept as pending refinements for the next full update.
- **Exit:** V_T = exit P/E × 2030 EPS (on end-2029 shares; cum the FY29 dividend, as today's price
  is cum FY26). 2030 EPS is at each scenario's mid-cycle NIBOR. **Exit P/E Bear 10.5 / Base 13.0 /
  Bull 14.5** `[A]`:
  - **Own history:** year-end P/E on the next year's actual EPS 9.9 (2023, on 2024 underlying 9.1),
    10.8 (2024, on 2025's 11.25), 15.2 (2025, on 2026E 11.36); average **12.0** `[F/A]` (2024
    underlying = reported 11.46 less the ~2.4 a share health-insurance gain). Trailing at
    year-end: 13.3 (2024, underlying), 15.4 (2025).
  - **Equity BBB:** Oslo exit 11.5. Storebrand earns ROE ~17% at exit against the index's 15.2%
    and pays out ~85% (index 0.66), so a premium of ~1.5 points is defensible.
  - **Index-consistent check (Step D form):** at Oslo's mid-cycle return 9.1%, a sustainable payout
    of 76% (1 − 4% / 17%) and 4% long-run growth give P/E ≈ 14.9; at the index's 3.4% growth, 13.4.
    Base 13.0 sits at the low end of that range, close to the own-history average plus the ROE
    premium.
  - Bear 10.5 = the Oslo Bear exit: the premium goes in a recession that hits fees and profit
    sharing. Bull 14.5 = today's multiple on Base CY27 holds (Equity Bull "P/E holds").
  - Not used: today's 14.6 (would assume the 2025–26 re-rating is permanent), the IAF ceiling.
- **Interim V_t:** price flat at end-2026; P/E glides linearly from 14.61 (today, on Base CY27) to
  the exit P/E (Bear at 10.5 from end-2027), each on the next year's EPS.

## Period tables and year-end path

**Base** (NOK bn unless stated)

| | 2027 | 2028 | 2029 | 2030 (exit EPS) |
|---|---|---|---|---|
| 3M NIBOR (HY BBB) | 4.79 | 4.39 | 3.86 | 3.45 (mid-cycle) |
| Operating profit (incl. Knif) | 4.89 | 5.28 | 5.65 | 5.98 |
| Profit sharing / NIBOR-linked financial result | 0.65 / 1.20 | 0.70 / 1.10 | 0.75 / 0.97 | 0.75 / 0.86 |
| **Group profit** | **6.74** | **7.08** | **7.36** | **7.59** |
| Profit after 21% tax (before amortisation) | 5.32 | 5.59 | 5.81 | 6.00 |
| **EPS** NOK (vs CY27 consensus 13.61) | **12.94** (0.95) | **13.94** (1.02) | **14.87** (1.09) | **15.54** (1.14) |
| Dividend declared for the year (paid next April) | 6.47 | 6.97 | 7.44 | |
| Buyback NOK bn (NOK per share) | 2.0 (4.80) | 2.0 (4.92) | 2.0 (5.05) | |
| Shares outstanding, year-end (m) | 406.2 | 396.0 | 386.1 | |
| ROE (on opening book) / BVPS year-end | 15.9% / 83.8 | 16.4% / 87.8 | 16.7% / 92.1 | 16.9% |

**Bear** (lines that differ)

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| 3M NIBOR | 4.21 | 3.55 | 3.50 | 3.25 |
| Operating profit / profit sharing / MTM | 3.96 / 0.10 / −0.30 | 4.19 / 0.35 / 0 | 4.57 / 0.50 / 0 | 4.93 / 0.60 / 0 |
| Group profit | 4.81 | 5.43 | 5.94 | 6.34 |
| EPS | 9.11 | 10.40 | 11.69 | 12.67 |
| Dividend declared / buyback NOK bn | 6.00 / 0 | 6.00 / 1.0 | 6.00 / 1.5 | |
| ROE / BVPS | 11.3% / 82.8 | 12.4% / 86.0 | 13.4% / 89.9 | 14.1% |

**Bull** (lines that differ)

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| 3M NIBOR | 4.65 | 4.15 | 3.65 | 3.45 |
| Operating profit / profit sharing | 5.02 / 0.80 | 5.57 / 0.85 | 6.13 / 0.90 | 6.67 / 0.90 |
| Group profit | 6.99 | 7.46 | 7.94 | 8.44 |
| EPS | 13.46 | 14.82 | 16.22 | 17.47 |
| Dividend declared / buyback NOK bn | 7.00 / 2.5 | 7.70 / 2.5 | 8.43 / 2.5 | |
| ROE / BVPS | 16.5% / 83.6 | 17.5% / 86.9 | 18.4% / 90.6 | 19.3% |

**Year-end path** (D_t paid in the year; V_t at year-end; r_t in NOK)

| | End-2026 (stub) | 2027 | 2028 | 2029 (exit) |
|---|---|---|---|---|
| Bear: D / V / P/E | 0 / 189.0 / 14.61 | 6.00 / 109.2 / 10.5 | 6.00 / 122.7 / 10.5 | 6.00 / 133.0 / 10.5 |
| Bear: r_t | 0.0% | **−39.0%** | 17.8% | 13.3% |
| **Base: D / V / P/E** | 0 / 189.0 / 14.61 | 6.00 / 196.1 / 14.07 | 6.47 / 201.3 / 13.54 | 6.97 / 202.0 / 13.0 |
| **Base: r_t** | 0.0% | **7.0%** | 5.9% | 3.8% |
| Bull: D / V / P/E | 0 / 189.0 / 14.61 | 6.00 / 215.9 / 14.57 | 7.00 / 235.8 / 14.54 | 7.70 / 253.4 / 14.5 |
| Bull: r_t | 0.0% | 17.4% | 12.4% | 10.7% |

- Base returns fade from 7% to 4% a year: EPS growth slows as NIBOR falls, and the de-rating runs
  every year. No year reaches k.

## V_T bridge (Base, per share) and exit consistency

| Step | NOK/share |
|---|---|
| P (19 Oct 2026) = 14.61 × Base CY27 EPS 12.94 | 189.00 |
| EPS growth to 2030 (12.94 → 15.54; **+5.9% a year** over T), of which buybacks ~+2.4 pp a year (shares 416.8m → 386.1m after Knif, −7.4%) | +38.0 |
| De-rating 14.61 → 13.0 (−3.6% a year) | −25.0 |
| **= V_T** (13.0 × 15.54) | **202.0** |
| Book value per share at exit / P/B | 92.1 / 2.19 (from 2.48) |

- g = (202.0 / 189.0)^(1/3.20) − 1 = **2.1% a year**; d = 3.2% (cash dividends); c = +0.02 pp.
  Buybacks run through the share count and EPS, not D_t, so retained capital is counted once.
- **Exit consistency (Step 3):** the drivers that mean-revert are NIBOR and profit sharing.
  - The 2030 exit EPS uses each scenario's mid-cycle NIBOR (3.25 / 3.45 / 3.45).
  - Year 3 vs exit year (Base): NIBOR 3.86 vs 3.45 is NOK 0.08bn after tax, 1.4% of profit. Bear
    2029 vs 2030 profit sharing 0.50 vs 0.60bn, 1.6% of profit. Both are below the 10% limit.
    **No reversion tail.**
- **Exit cross-check against the equity market:**

| | Bear | **Base** | Bull | Equity BBB Oslo (Bear / Base / Bull) |
|---|---|---|---|---|
| Exit P/E (2030 EPS) | 10.5 | **13.0** | 14.5 | 10.5 / 11.5 / 12.5 |
| Exit P/B (book end-2029) | 1.48 | **2.19** | 2.80 | 1.48 / 1.75 / 1.97 |
| Normalised ROE 2030 | 14.1% | **16.9%** | 19.3% | 14.0 / 15.2 / 15.7% |
| Cash conversion (dividend + buyback ÷ EPS, 2029) | 0.83 | **0.84** | 0.91 | 0.66 |
| Buyer's implied return (cash yield + long-run growth 2.5 / 4.0 / 4.75%) | 10.4% | **10.5%** | 11.1% | 8.2 / 9.1 / 9.4% |

- The buyer's implied return at exit is ~1.4 pp above the index's mid-cycle return in Base, so the
  exit is not rich against the market rule; no re-discount sensitivity is required. Part of the
  0.84 cash conversion is run-off capital release, which fades after 2030; on a sustainable 0.76
  the Base return is 9.8%. The exit P/B 2.19 against Oslo's 1.75 follows from the higher ROE
  (earnings yield on book, ROE ÷ P/B, 7.7% against the index's 8.7%) and is below today's 2.48.

## Growth capex test (Step 4)

- An insurer's "growth capex" is the solvency capital retained to back growth. Storebrand's growth
  is capital-light (unit linked, asset management, P&C at ~8% share); retention is ~15% of profit
  in Base, against EPS growth of ~6% a year, half of which comes from buybacks. Incremental ROE on
  the retained capital is well above k on the company's own figures (P&C retail CR 80–90%) `[A]`.
- **Buybacks** at P/B 2.48 and ROE ~16.5% earn ~6.7% on the price paid (ROE ÷ P/B), below k.
  For a holder they are about equal to a dividend reinvested at the market price: per-share
  growth, not value. Below ~NOK 140 (P/B ~1.8) a buyback would earn above 9%.
- **Knif:** NOK 560m in new shares for ~NOK 800m of premiums and ~NOK 40m of operating profit
  `[A]` ≈ 14x pre-tax; value-neutral at best unless the partnership adds pension and asset
  management sales. Small (0.7% dilution).
  - **24 Oct** `[F]`: the deal closed 16 Oct with 2,746,582 shares, i.e. ~NOK 204 a share, above
    today's 188.40. Knif's H1 2026 profit before tax was NOK 70m at a CR of 77%. Normalised to
    ~NOK 80m a year `[A]` (a CR nearer 85–88%, before merger costs), the price is ~7x pre-tax and
    ~11% after tax on the price paid, just below k and better than the 14x assumed. The effect on
    Storebrand is small (Tracking sensitivity: +0.2 pp Base IRR).

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (dated, NOK) | −7.2% | **5.3%** | 12.9% |
| IRR_T on the Equity BBB NOK path (30% of earnings on I-44) | −6.6% | 5.3% | 12.7% |
| Track A screen: d + g at constant P/E (EPS CAGR CY26E 11.36 → CY29; assumes today's P/E holds) | 3.0 + 0.9 = 3.9% | **3.2 + 9.4 = 12.6% (passes the screen)** | 3.4 + 12.6 = 16.0% |
| d / g / c (dated build) | 3.0 / −10.4 / 0.2 | **3.2 / 2.1 / 0.0** | 3.4 / 9.6 / −0.1 |
| g of which buyback accretion | ~1.6 pp | **~2.4 pp** | ~2.8 pp |
| Structural / cyclical | −7.3% / +0.1 pp: a mid-cycle shift (P/E 10.5, lower earnings level), not a cycle | **5.3% / +0.0 pp** | 12.9% / +0.0 pp |
| ΣD_t / V_T | 18.00 / 133.0 | **19.44 / 202.0** | 20.70 / 253.4 |
| P_k / margin of safety | 107.7 / −43.0% | **156.9 / −17.0%** | 193.6 / +2.4% |
| Rule 3: P/E vs ceiling (d + g) / k² | 16.6 vs 2.7 | **16.6 vs 8.8 (fails)** | 16.6 vs 11.1 |
| Capital preserved? ΣD + V_T vs P | **No (−20.1%)** | Yes (+17.2%) | Yes (+45.0%) |

- **Track A screen vs dated IRR:** the screen's g (9.4%) starts from CY26E EPS, which is held down
  by a 26% tax rate, and keeps the P/E at 16.6 for ever. The dated IRR (5.3%) prices the 2027 jump
  that today's price already holds (14.6x Base CY27) and an independent exit at 13.0. The dated
  IRR decides: fails.
- **Structural run:** the same model with NIBOR at the scenario's mid-cycle and profit sharing at
  its 2030 level from 1 Jan 2027, and operating profit on a smooth path to its 2030 level (Bear's
  2027 fall removed). The cycle adds almost nothing: the exit EPS is already at mid-cycle NIBOR,
  and the Bear 2027 dip is mostly in the multiple, which the structural run keeps. Storebrand's
  return is a valuation question, not a rate-cycle question.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** 4.6%. Not a decision figure.
- **Share of Bull already priced:** (189.0 − 156.9) / (193.6 − 156.9) = **87%**.
- **Bear balance sheet:** no survival question. ROE stays at 11–14% and book value grows. Solvency
  falls with equities and lower rates; in 2020 it was 163% at Q2-20 `[F]` (the Q1-20 trough was
  not checked `[?]`), well above 100%. Buybacks stop below 175%; the NOK 6.00 dividend (66% of 2027 Bear EPS) is
  affordable. The loss comes from the multiple (14.6 → 10.5) and ~30% lower earnings in 2027.
  - **24 Oct** `[F]`: the Q3 single-stress sensitivities (191–210%) and the > 10 pp regulatory
    uplift from Q1 2027 make the Bear balance sheet stronger still.
  - The Bear buyback pause in 2027 is kept. It follows the 2020 precedent, when the proposed 2019
    dividend was cancelled (Covid-19; analyst presentation p. 4), rather than the solvency
    arithmetic.
  - Without the pause (NOK 1.5bn in 2027), Bear is −6.4% instead of −6.9% in the check run. Not
    material.
- **E / R (HY rule, NOK):** E = 5.3 − 4.38 = **0.95 pp**; R = Base 2027 (7.0%) − Bear 2027
  (−39.0%) = 46.0 pp; **E / R = 0.021**. That is a tenth of the HY market reference (0.196), below
  DNB (0.096) and about World's (0.024).
- **Sensitivities (Base IRR / P_k / margin of safety):**

| Change | IRR | P_k | MoS |
|---|---|---|---|
| Exit P/E 12.0 / 14.0 | 2.9% / 7.6% | 146.3 / 167.4 | −22.6% / −11.4% |
| Exit P/E 14.6 (today's multiple on Base CY27 holds) | 9.0% | 173.7 | −8.1% |
| **Break-even exit P/E** | **12.0% at ~16.0** | 189.0 | 0% |
| NIBOR held at 4.5% through 2030 | 6.4% | 161.6 | −14.5% |
| Operating profit +6% / +11% a year | 4.0% / 8.6% | 150.9 / 171.8 | −20.2% / −9.1% |
| Profit sharing 0.4bn a year | 3.9% | 150.4 | −20.4% |
| Buybacks at the ambition floor (1.25bn a year) / none | 4.4% / 2.9% | 152.8 / 146.3 | −19.2% / −22.6% |
| Bear with P/E 9.0 instead of 10.5 | Bear −11.1% | Bear 95.2 | Bear −49.6% |

- **The multiple decides.** One point of exit P/E moves Base by ~2.4 pp. Operating growth matters
  next (about 1 pp of IRR per pp of growth a year). Rates matter little: no cutting cycle at all adds 1.0 pp.

## Verdict and caveat

- **Fails: Base margin of safety −17.0%** (below the −2% line). Base IRR 5.3% against k = 12%.
  Unchanged on 24 Oct after Q3: the check run at 188.40 gives −16.0% and 5.7%.
- **Does not survive Bear on capital:** −7.2% a year and a 20% capital loss over the window if a
  2027 recession with falling markets cuts fees and profit sharing and the P/E falls to the Oslo
  Bear level. The company itself stays well capitalised and keeps paying NOK 6.00.
- **What would flip it:** a price near **NOK 157** (−17%: Base reaches k), or evidence that the
  re-rating is durable: an exit P/E of ~16 is needed at today's price. Operating growth of ~14% a
  year, double the CMD path, would do the same. Storebrand is executing well (record insurance
  result, costs under guidance, targets on track); the price, at P/B 2.48 and an implied required
  return of ~9.2%, already pays for that. Q3 confirms the execution. The share, at P/B 2.41 on
  23 Oct, still prices it in full.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation or a price target. Returns are
  before tax; outside ASK or a pension wrapper a Norwegian holder pays tax on dividends (37.84% on
  the grossed-up share income in 2026 `[E]`).

## Tracking

### 24 Oct 2026, after the Q3 2026 report (published 21 Oct)

**Rule applied.** iaf-valuation sets no minimum change of its own for a tracking update. This
analysis applies the convention of Equity BBB, which supplies its market references:
- a Base return moves only if the evidence moves it by ≥ 1.0 pp a year;
- a trigger level moves only if it changes by ≥ 3%;
- the verdict bands apply as usual (clears above +2%, marginal from −2% to +2%, fails below −2%).

**Actual vs model, Q3 2026** (NOK m unless stated)

| Item | Model / consensus (19 Oct) | Actual `[F]` | Gap |
|---|---|---|---|
| Operating profit | ~1,150 `[A]` | 1,162 | +1% |
| Financial items and risk result | ~330 (implied) `[A]` | 355 (profit sharing 82, risk result −7) | +8% |
| **Group profit** (before amortisation and tax) | ~1,480 `[A]` | **1,517** | **+2.5%** |
| Effective tax rate | 21% `[A]` | 32% (SEK hedges) | non-recurring |
| EPS adjusted (NOK) | 2.81 (consensus, 7) | 2.54 (~2.90 at 21% tax) | −10% (tax only) |
| Buyback in the quarter, NOK bn | ~0.4 `[A]` | 0.514 | +0.1 |
| Solvency II | ~200% `[A]` | 200% | 0 |
| FY26 dividend / 2027 buyback (Board intention) | 6.00 / 2.0bn (Base) | ~6 / 2.0bn | on Base |
| 2026E group profit / operating profit / EPS | 6.22 / 4.45bn / 11.36 | 6.26 / 4.49bn / 11.18 (9M actual + Q4E) | +0.6% / +0.8% / −1.6% (tax) |

**Check run** (scratchpad `stb_model_p.py`):
- **Changed in the run:**
  - price NOK 188.40 (23 Oct close) and valuation date 24 Oct (T 3.19);
  - 418.41m shares with the Knif shares now in (416.3m at end-2026), no new shares in 2027;
  - book at end-2026 NOK 33.8bn including Knif;
  - 2026 operating profit 4.49bn (Q3 actual);
  - CY26E EPS 11.18.
- **Unchanged:** scenarios, NIBOR paths, growth rates, profit sharing, exit P/E, the dividend rule
  and buybacks.
- **Sensitivity column:** the two pending refinements added, i.e. Knif at ~NOK 0.08bn a year
  instead of 0.04 `[A]`, and the Base and Bull dividends at ≥ 10% growth for FY27–28 (CMD
  guidance `[F]`).

| | 19 Oct standing (P 189.00) | 24 Oct check run (P 188.40) | Check + pending refinements |
|---|---|---|---|
| Base IRR_T | **5.3%** | 5.7% (+0.4 pp) | 5.9% (+0.6 pp) |
| Base P_k / margin of safety | **156.9 / −17.0%** | 158.3 (+0.9%) / −16.0% | 159.3 (+1.5%) / −15.5% |
| Bear IRR_T / P_k / capital preserved | −7.2% / 107.7 / −20.1% | −6.9% / 108.6 / −19.3% | −6.75% / 109.1 / −18.9% |
| Bull IRR_T / P_k / margin of safety | 12.9% / 193.6 / +2.4% | 13.4% / 195.4 / +3.7% | 13.5% / 196.3 / +4.2% |
| Base EPS 2027 / 2030; V_T | 12.94 / 15.54; 202.0 | 13.03 / 15.66; 203.6 | 13.11 / 15.74; 204.6 |
| E / R (HY rule) | 0.021 | 0.029 | 0.034 |
| Triggers: Base = k / E / R = 0.196 / pre-alert (Base = 6.8%) | 157 / 139 / 181 | 158 / 141 / 183 | 159 / 143 / 184 |
| Break-even exit P/E | 16.0 | 15.8 | 15.7 |
| Verdict | **fails** | fails | fails |

- **Kept unchanged.**
  - The check run moves Base by +0.4 pp, below 1.0 pp. About +0.15 pp comes from the lower price
    and the later date, +0.05 pp from the share count and Knif timing, and +0.2 pp from the higher
    2026 operating base.
  - P_k moves +0.9% and the triggers move +0.9% / +1.8% / +0.8%, all below 3%.
  - The verdict is the same.
  - The standing figures, triggers and tables stay at the 19 Oct build.
- **With the pending refinements**, Base moves +0.6 pp and P_k +1.5%. The E / R trigger moves
  +3.0% (139 → 143), right at the line. The Q3 facts alone move it +1.8%; what takes it to the
  line is an own assumption (Knif, +1.0%) and the dividend guidance (+0.3%).
  - Taking the buyback guidance as well (1.5bn in 2028–29: −0.4 pp on its own), all three
    refinements together give Base 5.5%, against the standing 5.3%.
  - None is adopted between reports. They will be settled at the Q4 update (10 Feb 2027), when the
    FY26 dividend and the 2027 plan are firm.
- **Running on the Base path:**
  - Ahead on operating profit: 9M +16% y/y, and 2026E 4.49bn against 4.45bn in the build.
  - On par on group profit (2026E 6.26bn against 6.22bn) and on capital return (dividend and the
    2027 buyback exactly as Base).
  - Behind only on EPS, through tax (11.18 against 11.36).
  - The change in Base P_k is +1.4 (156.9 → 158.3) in the check run; the standing figure is kept.
- **Market reaction:** +2.0% on the report day, given back over the next two days. At 188.40 the
  share is −0.3% against 19 Oct, so Q3 brought no re-rating.

## Risks and signposts

| Signpost | Bear / Bull threshold | Now | Source |
|---|---|---|---|
| Insurance combined ratio (segment) | > 94% two quarters / < 88% | **87% (3Q26)**, 87% (2Q26), 93% (1Q26) | Company `[F]` |
| Fee and administration income, y/y | < −3% / > +10% | **+0.7% (3Q26)**, +6% ex FX and performance fees; −1.9% (2Q26) | Company `[F]` |
| Operating cost growth | > 5% (guidance) / < 3% | **+8% y/y (3Q26; incl. NOK 20m one-off), +5% 9M** | Company `[F]` |
| Financial result, quarter | < NOK 0.2bn / > 0.6bn | **0.355bn (3Q26)**, 0.68bn (2Q26), 0.33bn (1Q26) | Company `[F]` |
| Solvency II | < 180% / > 205% | **200% (3Q26)**; single stresses 191–210%; +10 pp from Q1 2027 | Company `[F]` |
| Buyback pace 2027 | < NOK 1.5bn (guided level) / ≥ 2.5bn | **NOK 2bn intended for 2027** (2026: 2bn) | Company `[F]` |
| Group profit run-rate vs NOK 7bn in 2028 | < 6.3bn in 2027 / ≥ 7bn in 2027 | ~6.26bn (2026E: 9M 4.67bn + Q4E) | This analysis |
| 3M NIBOR / Norges Bank | NB cut before Q3-27 / no cut in 2027 | policy 4.50%; next decision 5 Nov | HY BBB |
| World / Oslo in NOK (AUM driver) | 2027 drawdown > 15% / > +10% | — | Equity BBB |
| P/E on CY27 consensus | ≤ 11.5 (≈ NOK 157) / ≥ 15 | 13.9 (188.40 / 13.58) | This analysis |
| **Price** | **≤ NOK 157 (Base = k); ≤ NOK 139 (E / R = 0.196); pre-alert ≤ 181 (Base = HY 6.8%)** | **NOK 188.40** (23 Oct close; 189.00 on 19 Oct) | Yahoo |
| Equity BBB Bear signposts | US HY OAS > 450 bp; MSCI World fwd P/E < 15.5; Nordic HY spread > 550 bp | — | `docs/equity-market-bbb.md` |

- **Other risks:**
  - Disability claims in Norway (group life, pension-related disability): reserve strengthening
    hit 2023–25 results.
  - SEK/NOK: a stronger NOK cuts SPP earnings and AUM and moves the tax rate through hedges.
  - Performance fees in asset management are volatile (reversed in Q2 2026).
  - Regulation: paid-up policy reform (upside), ESA case on public-sector pensions vs KLP (upside if
    tenders open), VAT changes from 1 Jul 2026 (cost), Solvency II reviews.
  - Guaranteed run-off: falling rates reduce profit sharing and buffer capital; very low rates
    (2020) pressured solvency.
  - Rising rates hit the quarter instead: Q3 profit sharing and company-portfolio returns fell
    on mark-to-market, and the excess value of bonds at amortised cost dropped to −NOK 14.0bn
    `[F]`. The company calls higher rates supportive for future results.
  - IRRD crisis-fund proposal (NOK 25bn for life and P&C, 12.5bn pre-funded over 10 years):
    a cost risk if adopted as proposed `[F]`.
  - Corporate insurance: portfolio premiums flat after a large outflow, and group life is only
    modestly positive `[F]`.
- **Next update:** Norges Bank (5 Nov, through HY BBB); the **Q4/FY26 report on 10 Feb 2027**
  `[F]` with the FY26 dividend proposal and the start of the 2027 buyback, when the pending
  refinements are settled; the end of the 2026 buyback tranche (by 18 Dec); and the Equity and HY
  baseline updates.

## For other modules

- **equity-market-bbb:** **difference, explained.** Block F (DNB, STB, GJF) Base is 0.98 / 0.96 /
  0.95 of CY27 consensus; Storebrand's bottom-up Base is 0.95 / 1.02 / 1.09. The gap is fee and
  insurance growth (+7–9% a year operating profit) and buybacks (~2.4% fewer shares a year),
  against the same NIBOR path; DNB's analysis found the same (1.02 / 1.07 / 1.09). Two of the
  three block F names now point above the block path from 2028. At the next update, check whether
  block F should be per share with buybacks; that would lift Oslo Base by roughly +0.1–0.2 pp a
  year. Bear 2027 is harsher here (0.67 vs 0.85): Storebrand's earnings carry equity-market beta
  through fees and profit sharing that a bank does not. No change made here.
- **hy-market-bbb:** no gap. The NIBOR path is used as set.
- **24 Oct (Q3):** no change for either module.
  - The block F note above stands. Q3 group profit was on the bottom-up path, and the 2027
    buyback (NOK 2bn) supports the per-share point.
  - Q3 also shows the rate channel working both ways: rising rates hit the quarter's
    mark-to-market and lift expected returns ahead. That is already inside the 0.25bn-per-pp
    sensitivity.

## Change log

- **19 Oct 2026 — initial analysis** (iaf-valuation 2026-10-18.2; equity-market-bbb document
  17 Oct 2026, amended 18 Oct; hy-market-bbb document 17 Oct 2026). No previous values. Made two
  days before the Q3 report; the stub uses quarter consensus.
- **24 Oct 2026 — tracking update after the Q3 2026 report (21 Oct). Kept unchanged.**
  - Skills and inputs: iaf-valuation 2026-10-18.2 and equity-market-bbb 2026-10-18.6, both
    unchanged. The equity document is the same 17/18 Oct version. The HY document's 24 Oct version
    was read and is unchanged for every figure used. Price: 23 Oct close, NOK 188.40.
  - **No decision figure moved by the minimum change.** The check run moves Base IRR 5.3 → 5.7%
    (+0.4 pp), P_k 156.9 → 158.3 (+0.9%), margin of safety −17.0 → −16.0%, Bear −7.2 → −6.9% and
    Bull 12.9 → 13.4%. Triggers moved +0.8–1.8%. Standing figures, scenarios, paths and triggers
    are kept.
  - **Updated in the text:**
    - Q3 actuals (group, segment and product-line tables);
    - share count incl. the Knif shares (filing-confirmed), BVPS 78.10 and P/B;
    - capital (solvency sensitivities, the Q1 2027 uplift, holdco liquidity);
    - capital-return facts (dividend ~6 for 2026, 2027 buyback NOK 2bn, DPS guidance, buyback
      ambition ≥ 13.5bn by 2030);
    - Knif closing and its H1 figures;
    - the Q3 test results, the new Tracking section, the signposts, and the next report date
      (10 Feb 2027).
  - **Corrected:** 3Q25 and FY25 operating profit and the 4Q25 financial result are now `[F]`
    (they were approximations).
  - **Report date:** the update register lists the Q3 event as 23 Oct. Storebrand published on
    21 Oct, as the 19 Oct version had it.
  - **Pending refinements for the next full update:** Knif contribution ~0.08bn a year; DPS at the
    double-digit guidance for FY27–28; Base buybacks against the 1.5bn guidance for 2028–29.

## Appendix: own assumptions `[A]`

| Item | Bear | Base | Bull | Basis |
|---|---|---|---|---|
| 3M NIBOR 2027 / 28 / 29 / 2030 | 4.21 / 3.55 / 3.50 / 3.25 | 4.79 / 4.39 / 3.86 / 3.45 | 4.65 / 4.15 / 3.65 / 3.45 | HY BBB (not own); 2030 = mid-cycle |
| Financial result sensitivity | NOK 0.25bn pre-tax per 1 pp | same | same | Company portfolios net of floating debt; not disclosed `[?]` |
| Operating profit growth 2027 / 28 / 29 / 30 (from 4.45bn in 2026E) | −12 / +6 / +9 / +8% | +9 / +8 / +7 / +6% | +12 / +11 / +10 / +9% | 2026 +15% y/y; CMD 7bn group profit in 2028; cost guidance +5% |
| Profit sharing, NOK bn | 0.10 / 0.35 / 0.50 / 0.60 | 0.65 / 0.70 / 0.75 / 0.75 | 0.80 / 0.85 / 0.90 / 0.90 | 2025 guaranteed Norway 0.60bn; paid-up policy reform from H2 2026 |
| Company-portfolio MTM | −0.30bn (2027) | 0 | 0 | Credit spreads in the HY Bear |
| Knif Trygghet | +3.0m shares (Q1 2027), +0.04bn op. profit | same | same | NOK 560m in new shares `[F]`; premiums ~0.8bn. Actual: 2.75m shares on 16 Oct 2026 `[F]`; the standing build is kept (check run: −0.1% shares) |
| Tax | 21% | 21% | 21% | Guidance 19–22% `[F]` |
| FY26 dividend (paid ~23 Apr 2027) | 6.00 | 6.00 | 6.00 | FY25 5.40; payout > 50% of cash result |
| Dividend rule from FY27 | held at 6.00 | max(prior + 0.30, 50% EPS) | max(prior + 0.40, 52% EPS) | 2025 payout 51% |
| Buybacks, NOK bn 2027 / 28 / 29 | 0 / 1.0 / 1.5 | 2.0 / 2.0 / 2.0 | 2.5 / 2.5 / 2.5 | ≥ 12bn by 2030, 6bn done by Q2-26 `[F]`; 2026 pace 2bn. 24 Oct: ambition lifted to ≥ 13.5bn by 2030; 2027 intended at 2bn; guidance 1.5bn a year 2028–30 `[F]` |
| Exit P/E (2030 EPS) | 10.5 (from end-2027) | 13.0 | 14.5 | Own 2023–25 forward 9.9–15.2 (avg 12.0); Oslo exit 10.5 / 11.5 / 12.5; index-consistent 13.4–14.9 |
| SEK/DKK share of earnings (NOK path) | 30% | 30% | 30% | SPP and asset management; not disclosed as a share `[?]` |
| *Pending (24 Oct; not adopted, see Tracking):* Knif operating contribution | 0.08bn | 0.08bn | 0.08bn | H1 2026 profit before tax NOK 70m, CR 77% `[F]`; normalised `[A]` |
| *Pending:* dividend FY27–28 | held | ≥ +10% a year | ≥ +10% a year | CMD guidance of double-digit DPS growth 2025–28 `[F]` |
| *Pending:* Base buybacks 2028–29 | — | 2.0bn (standing) against 1.5bn guided | — | Guidance of 1.5bn a year 2027–30, with 2027 raised to 2.0bn `[F]` |

## Appendix: sources

| # | Source | Content | As of |
|---|---|---|---|
| S1 | Storebrand Q2 2026 results release (Newsweb via Nordic Financial) | Group profit 1,799m, operating profit 1,119m, insurance 889m (CR 86.7%, retail 79.9%), fees 2,031m, financial result 680m, profit after tax 1,380m, EPS 3.43, equity 32,606m, AUM 1,658bn, ROE 16% LTM, solvency 200%, buyback tranche 15 Jul–18 Dec, NOK 6bn bought back since 2022, ambition ≥ 12bn by 2030, CMD target 7bn / 17% by 2028 `[F]` | 15 Jul 2026 |
| S2 | Storebrand Q1 2026 results release | Group profit 1,353m, operating 1,026m, insurance 665m (CR 93%), fees 2,097m, financial 327m, EPS 2.10, solvency 206%, cost guidance 5%, tax 36% (normal 19–22%), paid-up policy reform from H2 2026 `[F]` | 29 Apr 2026 |
| S3 | Storebrand Q4 2025 results release | Group profit 1,515m / FY 5,695m, operating 1,131m, EPS 2.88, ROE 16% (2025), solvency 194%, DPS 5.40 (2,289m, 51% payout), total payout 85%, NOK 2bn buybacks in 2026, guaranteed reserves 306bn, buffer capital 8.5% / 27.3% `[F]` | 11 Feb 2026 |
| S4 | Storebrand Q3 2025 and Q2 2025 releases | Q3-25 EPS 3.08, solvency 195%; Q2-25 group profit 1,427m, operating 953m, insurance 635m, EPS 2.87, CMD 10 Dec 2025 announced `[F]` | 22 Oct 2025, 11 Jul 2025 |
| S5 | Storebrand press releases: Knif Trygghet (LOI; negotiated agreement) | NOK 560m in new shares, premiums ~NOK 800m, no material effect `[F]` | 29 Jan, 11 Jun 2026 |
| S6 | Yahoo `quote_summary` (price, summaryDetail, defaultKeyStatistics, financialData, earningsTrend, calendarEvents), `get_chart` (1mo, 3mo, dividends) for STB.OL | Price 189.00, shares 415.66m, BVPS 76.15, consensus EPS, targets, next report 21 Oct 2026, dividend history, month-end closes `[F/E]` | 19 Oct 2026 |
| S7 | `docs/equity-market-bbb.md`, `docs/hy-market-bbb.md` | Scenarios, block F, exit P/E and P/B, mid-cycle returns, NOK path, index IRRs; NIBOR path, window average 4.38%, HY return 6.8%, HY reference E / R 0.196 | 17–18 Oct 2026; HY re-read in its 24 Oct version (unchanged) |
| S8 | Model script (scratchpad `stb_model.py`, `py -I`) | Earnings build, share count, book roll, XIRR, P_k, structural run, sensitivities, triggers | 19 Oct 2026 |
| S9 | Storebrand Q3 2026 interim report (PDF from storebrand.no IR, 45 pages; parsed with Nordic Financial `parse_pdf_to_text`) | Group cash-equivalent income statement (5 quarters, 9M, FY25); segment results (Savings, Insurance, Guaranteed, Other) and key figures; operating profit 1,162m, group profit 1,517m, tax 32%, EPS 2.54; profit sharing 82m; AUM 1,633bn; guaranteed reserves 289bn; buffer capital 8.6% / 31.2%; solvency 200% and the Q1 2027 uplift of more than 10 pp; buybacks 1,514m in 9M with 486m left; Outlook (targets, dividend policy, intended ~NOK 6 for 2026 and 2bn for 2027); Knif 2,746,582 shares; equity note (424,763,636 shares issued, 8,676,139 own); IFRS EPS 2.25 `[F]` | 21 Oct 2026 (Board 20 Oct) |
| S10 | Storebrand Q3 2026 analyst presentation (PDF, 32 pages) | Capital distribution chart (DPS history, buybacks 2022–2030E, ambition ≥ 13.5bn by 2030 lifted from the CMD); solvency sensitivities 191–210%; Knif H1 2026 (profit before tax 70m, GPE 418m, CR 77%); product-line profits; special items; expected return +230 bp over the guarantee; financial calendar (Q4 on 10 Feb 2027) `[F]` | 21 Oct 2026 |
| S11 | Storebrand Q3 2026 results release (Newsweb via Nordic Financial; English and Norwegian) | Headline figures, CEO quotes, dividend and buyback intention `[F]` | 21 Oct 2026, 07:00 CET |
| S12 | Yahoo `quote_summary` and `get_chart` for STB.OL | Close 188.40 (23 Oct, 14:25 UTC); daily closes 12–23 Oct; shares 418.41m; BVPS 78.10; consensus (Q4-26 3.11, CY26 11.63, CY27 13.58); targets mean 206.6, median 218.5 `[F/E]` | 23 Oct 2026 |
| S13 | Check-run script (scratchpad `stb_model_p.py`, the 19 Oct model with the inputs as parameters; reproduces the 19 Oct results exactly) | Check run and decomposition, pending-refinement sensitivity, Bear buyback and guided-buyback sensitivities | 24 Oct 2026 |

- **Quality notes:**
  - Figures come from Storebrand's own Newsweb releases (primary), not an aggregator. The full
    quarterly report PDFs (segment tables, solvency sensitivities, the financial-result split)
    were not parsed; the earnings build uses group-level lines with an own NIBOR sensitivity.
    24 Oct: the Q3 2026 interim report and analyst presentation were parsed (S9, S10).
  - Q3-25 operating profit and Q4-25 financial result are derived or approximate `[A]`; they do
    not enter the model (2026E is built from 2026 quarters). 24 Oct: replaced by the reported
    figures (S9).
  - The share count (Yahoo) is consistent with the buyback pace but not confirmed by a filing
    after July `[?]`. **24 Oct: now confirmed** by the Q3 report's equity note (416.09m
    outstanding at 30 Sep) plus the 2,746,582 Knif shares; Yahoo's 418.41m implies ~0.4m bought
    back in October `[A]`.
  - Quarter consensus is thin (4–7 analysts) and was cut in the last 30 days; annual consensus has
    9 analysts. 24 Oct: Yahoo's CY26 mean (11.63) is above 9M actual plus Q4 consensus (11.18), so
    some annual estimates have not been updated for Q3 `[?]`.
  - 24 Oct: the 19 Oct model script (S8) was copied unchanged into S13 with its inputs as
    parameters. It reproduces the 19 Oct results to the decimal before the check-run inputs are
    applied.
  - 24 Oct: FinancialFilings was unavailable (monthly quota; resets 1 Nov). The Q3 report PDFs from
    Storebrand IR are the primary source for every Q3 figure.
