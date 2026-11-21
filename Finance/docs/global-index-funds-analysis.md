# DNB Global Indeks A — index fund on the Equity BBB World blocks

**Version 7 — 21 Nov 2026** · NAV **NOK 835.76** (19 Nov 2026, latest published) · skills: iaf-valuation **2026-11-18.1** (Step 6b
first used here; v6 was built under 2026-10-18.2); inputs equity-market-bbb 2026-11-18.1 (20 Nov note), ai-market-bbb 2026-11-18.1
(18 Nov rows), hy-market-bbb 2026-11-18.2, oil-market-bbb 2026-11-18.2 · **verdict: fails** (Base margin of safety −13.5%).

## Summary

**Verdict**
- **Fails.** Base IRR **6.7% a year** in NOK after the 0.25% all-in cost on Nordnet (6.7% at 0.21% on the DNB pension platform)
  against k = 12%. **Hurdle NAV P_k 723 against 835.76: margin of safety −13.5%.** Only the Bull clears k (Bull hurdle 880 at
  spot, 856 on the NOK path); 72% of the Bull's gain over Base is already in the NAV.
- **Bear loses capital:** 2027 **−24.2%** at spot FX (−16.0% on the Equity BBB NOK path, where the krone weakens), window −2.7% a
  year (−0.1%); ΣD + V_T is 7.9% below the NAV at spot (−0.4% on the NOK path). No balance-sheet question (daily-dealing UCITS, no
  leverage).
- **What the price needs for k:** an exit value multiple of **19.8** on 2030 EPS (Base 16.9; the Equity BBB Bull 18.5), or rest-of-
  World EPS growth of 13.1% a year (Base 5.5%). Neither is inside the baselines' range.
- **Against high yield:** E / R **0.081** against the HY market reference 0.254; Base 6.7% is just below the HY market after a
  typical fee (6.9%). Triggers: pre-alert NAV **830**, E / R trigger **728** (−12.8%), k at **723** (−13.5%).
- **20 Nov close** (NAV published ~23 Nov): indicative NAV ≈ **812.5** (−2.8%): Base 7.9%, margin −10.6%, E / R 0.134; the
  pre-alert is crossed there. Still fails.

**Base in brief**
- World EPS (sum of blocks) **0.96 / 0.98 / 1.02 / 1.07 × CY27 consensus** in 2027–30: below consensus in 2027 (AI and company
  blocks at 0.92, the rest at −3%), then +2.2% a year in USD to the 2030 normalised year. The AI and company part is about flat after
  2027 (NVIDIA's funding losses, the 18 Nov H1 and H2 cuts); energy falls with Brent 80 → 70; the rest grows 5.5% a year.
- **Where the return comes from** (NOK per unit, from 835.76 to ΣD + V_T 1,013.6): EPS growth **+58.5**, value multiple 16.0 →
  16.9 **+53.6**, dividends **+73.1**, cost **−7.4**; FX 0 in Base. The re-rating is new: after the AI sell-off the NAV sits below
  the Equity BBB's mid-cycle multiple (17).
- **Break-even:** exit value multiple 19.8, or the NAV at 723 (forward P/E ≈ 14.2).

**Bear in brief**
- **Story:** recession from H1 2027 with the oil Bear (Brent 65 / 60 / 60: a durable Iran–USA deal and OPEC+ market-share quotas)
  and the AI financing break inside World; USD/NOK +12%. Earliest Q1 2027.
- **Worst year:** 2027, World EPS 0.80 of CY27 consensus and the value multiple to 15.
- **What does the damage** (driver breakdown): the AI and company blocks take Base 6.7% to 2.9%, energy to 2.6%, the rest's
  recession EPS to −0.5%, the rest multiple to −2.7% (spot); the weaker krone adds back 2.6 pp (−0.1%).

**Decision table** (NOK; NAV 835.76 of 19 Nov 2026; after the 0.25% all-in cost on Nordnet; before tax)

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T to 31 Dec 2029, spot FX (decision) | −2.7% | **6.7%** | 13.9% |
| IRR_T on the Equity BBB NOK path | −0.1% | **6.7%** | 12.9% |
| 2027 return, spot / NOK path | −24.2% / −16.0% | **7.9%** | 21.4% / 18.2% |
| NAV at end-2029 (accumulating), spot / NOK path | 776 / 839 | **1,019** | 1,245 / 1,212 |
| **Hurdle NAV P_k (k = 12%) / margin of safety**, spot | 549 / −34.3% | **723 / −13.5%** | 880 / +5.2% |
| P_k on the NOK path | 594 / −28.9% | 723 | 856 / +2.4% |
| Capital preserved? (ΣD + V_T vs P), spot / NOK path | No: −7.9% / −0.4% | Yes: +21.3% | Yes: +47.9% / +43.9% |
| E / R (HY market reference 0.254) | | **0.081** | |
| NAV triggers | | **pre-alert 830 · E / R 728 · k 723** | |
| NOK 1m at end-2029 (NOK path) | 1,004k | **1,219k** | 1,450k |
| DNB pension platform (0.21%): IRR_T / P_k / margin / E / R | −2.7% (spot) | **6.7% / 723 / −13.4% / 0.083** | 14.0% (spot) |
| 20 Nov close, indicative NAV ≈ 812.5 | 1.0% (NOK path) | **7.9% / 727 / −10.6% / 0.134** | 14.2% (NOK path) |

**Per-year path** (NAV, accumulating; NOK after cost; stub one period, not annualised)

| | Now (19 Nov) | End-2026 | 2027 | 2028 | 2029 | 2030 (normalised) |
|---|---|---|---|---|---|---|
| Base EPS (World blocks, CY27 consensus = 1.00) | | — | 0.959 | 0.980 | 1.021 | 1.070 |
| Base value multiple (V ÷ next-year EPS, incl. retained cash) | 16.0 on CY27 (MSCI fwd ≈ 16.5) | — | 17.1 | 17.0 | 16.9 | |
| Base return / NAV | 835.76 | +0.2% / 838 | +7.9% / 904 | +5.9% / 957 | +6.5% / 1,019 | |
| Bear, spot: return / NAV | | +0.2% / 838 | −24.2% / 635 | +11.0% / 705 | +10.0% / 776 | EPS 0.912 |
| Bear, NOK path: return / NAV | | +0.2% / 838 | −16.0% / 703 | +8.4% / 762 | +10.0% / 839 | |
| Bull, spot: return / NAV | | +0.2% / 838 | +21.4% / 1,017 | +11.1% / 1,130 | +10.2% / 1,245 | EPS 1.199 |
| Bull, NOK path: return / NAV | | +0.2% / 838 | +18.2% / 990 | +11.1% / 1,100 | +10.2% / 1,212 | |

## Tags

`[F]` fact from a fund document, index factsheet, holdings file or market print · `[E]` external or secondary · `[C]` carried from
an earlier version · `[A]` own assumption · `[?]` not found or unverified.

## Header

| Item | DNB Global Indeks A |
|---|---|
| Legal name, ISIN | DNB Global Indeks A, **NO0010582984** (Bloomberg DNBNGBI NO); classes A–H `[F]` |
| Structure | Norwegian UCITS, DNB Asset Management; physical, full replication; accumulating `[F]` |
| Index | **MSCI World Index Net (NOK)** less DNB's exclusions (tobacco, controversial weapons, cannabis, pornography, oil sands and coal ≥ 30% of revenue, DNB's responsible-investment list); 1,240 holdings against 1,248 (holdings of 14 Oct); SFDR art. 8 `[F]` |
| NAV (price P) | **NOK 835.76, 19 Nov 2026** (Nordnet fund page, latest published on 21 Nov) `[F]`; 846.23 on 18 Nov (dnbam.com) `[F]`; one trading day old, flagged |
| Indicative NAV, 20 Nov | ≈ 812.5 = 835.76 × URTH (187.43 / 193.91) × USD/NOK (9.7568 / 9.7006), Yahoo closes `[A]`; check 18 → 19 Nov: −1.14% against the NAV's −1.24% |
| Size | NOK 160,869m in the fund (dnbam.com, 21 Nov; date not stated) `[F]` |
| Cost (all-in) | Fund 0.10% management fee + 0.01% transaction costs. **0.25% on Nordnet** (+0.15% platform fee) · **0.21% on DNB's pension platform** (+0.10% platform fee) `[C]` (8 and 11 Oct) |
| Tracking | Fund vs benchmark: YTD 3.21 vs 2.89%, 1 y 7.00 vs 6.71% (dnbam.com, 18 Nov) `[F]`; annualised 3 y −0.14, 5 y −0.11, 10 y −0.12 pp after the fee; tracking error 0.24% `[C]` (8 Oct) |
| Currency | USD 72.8%, EUR 8.2%, JPY 5.8%, CAD 3.3%, GBP 3.2%, CHF 2.4%, other 4.3% (3 Sep); **unhedged** `[C]` |
| Risk | SRI 4; 3-year volatility 13.1%; max drawdown −22.2% `[C]` |
| Valuation, exit, T | Valuation 21 Nov 2026 at the 19 Nov NAV; stub 41 days to 31 Dec; exit 31 Dec 2029; T = 3.11 years |
| Track | Index fund on the Equity BBB World build: dated IRR to an exit value multiple (the Equity BBB's mid-cycle exit), with the company, AI layer, energy and rest blocks each on their own paths. DNB GI A = MSCI World on this build |
| k | **12%**, standard (no leverage, daily liquidity) |
| FX | USD/NOK 9.7006 (Yahoo, 19 Nov close; Norges Bank fixing 9.6866) `[F]`. Base spot flat; Bear and Bull on the Equity BBB relative path: 70% of earnings on USD/NOK, 30% on I-44 (Bear × 1.108 / 1.081 / 1.081, Bull × 0.973) |
| Inputs read (versions) | `docs/equity-market-bbb.md` 20 Nov note (World re-run; `world3.py`) · `docs/ai-market-bbb.md` 18 Nov rows (the 19 and 20 Nov notes moved no row) · `docs/msft-analysis.md` v3.3 (20 Nov, $484.52) · `docs/googl-analysis.md` v2.3 (20 Nov, $265.29) · `docs/nvda-analysis.md` v2.0 (20 Nov, $125.53) · `docs/amzn-analysis.md` v2.1 (20 Nov) · `docs/mu-analysis.md` v4.1 (20 Nov) · `docs/oil-market-bbb.md` 18 Nov · `docs/hy-market-bbb.md` 18 Nov · `docs/hy-funds-analysis.md` 9 Nov (reference 0.254, from the HY BBB) |

## Scenarios

The Equity BBB's World scenarios, with the AI BBB mechanism and the company analyses inside the World blocks. 25/50/25 is a
convention only, never a probability.

| | Bear | **Base** | Bull |
|---|---|---|---|
| Story, catalyst, earliest | Recession H1 2027 + oil Bear + AI financing break (lab shortfall, neocloud credit); Q1 2027 | AI boom slows to trend (AI BBB 18 Nov rows, NVIDIA funding losses); multiple drifts to mid-cycle; ongoing | Soft landing; earnings meet consensus; agentic adoption; Q2 2027 |
| Baseline rows | Equity BBB World Bear; AI BBB Bears (H1 .68 / .50 / .53 / .57 …); Brent 65 / 60 / 60 | Equity BBB World Base; AI BBB Base (H1 .92 / .85 / .82 / .81, H4 .95 / .94 / .94 / .99, E cash conversion −.20 / .11 / .36); Brent 80 / 73 / 72, mid-cycle 70 | Equity BBB World Bull; AI BBB Bulls; Brent on the Base path |
| World EPS × CY27 consensus, 2027 / 2030 | 0.80 / 0.91 | **0.96 / 1.07** | 1.00 / 1.20 |
| Company blocks: V_T MSFT / GOOGL / NVDA / AMZN / MU (USD) | 404.3 / 202.4 / 119.9 / 144.9 / 435.8 | **692.1 / 371.6 / 196.4 / 324.3 / 589.3** | 921.4 / 517.0 / 392.6 / 442.6 / 1,001.6 |
| Rest of World (70% of earnings): EPS 2027–30 / P/E to 2029 | .83 / .87 / .95 / 1.02 · 14.9 | **.97, then +5.5% a year · 17.2 → 16.3** | 1.00 / 1.07 / 1.14 / 1.21 · 17.4 |
| Exit value multiple (V_2029 ÷ 2030 EPS) | 14.9 | **16.9** | 18.5 |
| Macro and NOK | HY Bear macro (NB to 3.50% by Q4-27); USD/NOK +12 / +9 / +9%, I-44 +8 / +6 / +6% | NIBOR market path; NOK spot flat | First NB cut Q3-27; USD/NOK −3%, I-44 −2% |
| Result: IRR_T spot / NOK path; P_k; capital | −2.7 / −0.1%; 549; No (−7.9%) | **6.7%; 723; Yes** | 13.9 / 12.9%; 880; Yes |

**Driver breakdown** (one driver at a time from Base; after the 0.25% cost; IRR_T / 2027 return / P_k NAV)

| Step | Bear | Bull |
|---|---|---|
| Base | 6.66% / 7.9% / 723 | 6.66% / 7.9% / 723 |
| 1. AI and company blocks to the scenario | 2.93% / −2.8% / 650 | 10.83% / 14.9% / 810 |
| 2. + energy on the oil path | 2.57% / −4.3% / 643 | 10.90% / 15.0% / 811 |
| 3. + rest EPS path | −0.53% / −16.2% / 587 | 12.36% / 18.6% / 844 |
| 4. + rest multiple (= the scenario at spot FX) | −2.73% / −24.2% / 549 | 13.93% / 21.4% / 880 |
| 5. + NOK path | −0.14% / −16.0% / 594 | 12.90% / 18.2% / 856 |

- Step 1 alone is the **AI-only stress** (financing break without a recession): 2027 −2.8%, window 2.9% a year; AI-only Bull 10.8%.
- The rest's recession path (step 3) does more damage than the AI blocks in 2027: the rest is 70% of earnings.

**Base return bridge** (NOK per fund unit, after cost)

| P | + EPS growth (×1.070, CY27 consensus → 2030) | + value multiple (16.0 → 16.9) | + FX | − cost | = V_T | + dividends (ΣD) | = ΣD + V_T |
|---|---|---|---|---|---|---|---|
| 835.76 | +58.5 | +53.6 | 0 | −7.4 | 940.5 | +73.1 | **1,013.6** (accumulating NAV at end-2029: 1,018.7) |

## Fund and status

- **DNB Global Indeks A** holds MSCI World less about 8 excluded names, physically; it tracks its benchmark within ~0.1 pp a year
  after its 0.10% fee over 3–10 years `[C]`. YTD to 18 Nov it is 0.32 pp ahead (3.21 vs 2.89%) `[F]`.
- Sold on Nordnet (0.25% all-in) and on DNB's pension platform (0.21%). The only fund analysed here (user decision, 1 Nov).

**Record** (NOK, %; DNB AM table, checked against Yahoo NAVs for 2023–24) `[C]`; 2026 to 18 Nov `[F]`

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 to 18 Nov |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DNB GI A | 4.16 | 15.45 | −3.43 | 29.46 | 13.64 | 25.50 | −9.05 | 27.81 | 32.75 | 6.97 | 3.21 |
| MSCI World NOK | 4.55 | 16.31 | −3.36 | 29.56 | 12.93 | 25.46 | −8.56 | 27.62 | 32.71 | 7.55 | 2.89 |

## Near term

- **Stub (21 Nov–31 Dec 2026, 41 days):** price flat by convention; dividend accrual less cost **+0.24%**, the same in all
  scenarios.
- **NAV path:** 867.98 (15 Oct, the last version's NAV) → 846.23 (18 Nov) → **835.76 (19 Nov)**: −3.7%, the AI sell-off with a
  weaker krone partly offsetting (USD/NOK 9.49 → 9.70).
- **20 Nov (not yet in a published NAV):** URTH −3.34% in USD, USD/NOK +0.58%: World in NOK ≈ −2.8%, NAV ≈ 812.5 `[A]`. NVIDIA
  −14% (SEC accounting-probe report), Micron −14%. At that price Base 7.9%, P_k 727, margin −10.6%, E / R 0.134.
- **Dated events:** NAV of 20 Nov (~23 Nov); NVIDIA 10-Q (~25 Nov); SSB Q3 national accounts (26 Nov); OPEC+ (29 Nov); MSCI
  November index review and month-end factsheet (30 Nov); Equity BBB full update with refreshed consensus (by 6 Dec); Micron FQ1-27
  (16 Dec); Norges Bank MPR 4/26 (17 Dec, new I-44 anchor); Microsoft (~27 Jan), Alphabet (~2 Feb), Amazon (~4 Feb), NVIDIA Q4
  (~24 Feb).

## Market input (how the baselines enter)

| Input | From | Used as |
|---|---|---|
| World blocks: company blocks (MSFT, GOOGL, NVDA, AMZN, MU), AI layer blocks (E rest: Meta, Oracle; H1; H3; H4; T), energy, explicit rest: EPS Bear .83 / .87 / .95 / 1.02 · Base .97 then +5.5% · Bull 1.00 / 1.07 / 1.14 / 1.21; rest P/E Base 17.17 / 16.67 / 16.29; payout ~0.48–0.50 | `docs/equity-market-bbb.md` (20 Nov; `world3.py`) | DNB GI A = World on this build |
| AI layer rows: EPS paths, exit P/E, payout, cash conversion | `docs/ai-market-bbb.md` (18 Nov rows) | Layer blocks |
| Company per-share V_t, D_t, EPS per scenario; GOOGL v2.3 V_t at $265.29 (SpaceX and Anthropic at the 20 Nov close); NVIDIA Bull interim 241.0 / 319.5 (v2.0) | The five analyses (20 Nov) | Company blocks, interim V_t re-glided to the 19 Nov closes `[A]` |
| Energy: EPS (Brent − 30) / 49, Brent Bear 65 / 60 / 60, Base 80 / 73 / 72, mid-cycle 70; payout 0.58, cash conversion 0.80 | `docs/oil-market-bbb.md` (18 Nov) via the Equity BBB | Energy block |
| FX: 70% USD/NOK, 30% I-44, relative to spot; Base flat | `docs/equity-market-bbb.md` | Whole index |
| 3M NIBOR market path 4.80 (stub), 4.79 / 4.78 / 4.58; window **4.72%** | `docs/hy-market-bbb.md` (18 Nov) | E = Base IRR − NIBOR |
| HY market reference E / R **0.254** (E 2.15 pp ÷ R 8.47 pp); HY Base 7.5% before fees, 6.9% after a typical 0.6% fee | `docs/hy-market-bbb.md` (from 5 Nov); `docs/hy-funds-analysis.md` (9 Nov) reads the same | Decision rule and triggers |
| Prices 19 Nov (block names, URTH 193.91, IXC 55.64, USD/NOK 9.7006, EUR/USD 1.0972); URTH holdings of 4 Nov for weights | Yahoo (`dl2/recent_1120.json`); `dl2/urth_ai_nov.json` | Block weights and the World price at the NAV date |
| Check: at the 20 Nov close and zero cost the build gives 1.25 / 8.15 / 14.47%, 2027 −12.9 / 10.8 / 21.2%, E / R 0.136 (after 0.20%), against the Equity BBB's 1.3 / 8.2 / 14.5, −12.9 / 10.8 / 20.6, 0.137 | `world3.py` | Differences: GOOGL v2.3 (Base −0.03 pp) and NVIDIA's v2.0 Bull interim (Bull 2027 +0.6 pp) |

**World blocks** (19 Nov close; weight in MSCI World, P/E on CY27 consensus, share of CY27 earnings; each block alone in NOK on the
NOK path, before cost: IRR Bear / **Base** / Bull · Bear 2027)

| Block | Path source | Weight / P/E / earnings | Alone |
|---|---|---|---|
| CM Microsoft | msft v3.3 | 4.15% / 22.5 / 2.9% | −3.2 / **11.9** / 21.5 · −24.0% |
| CG Alphabet A + C | googl v2.3 | 3.37% / 18.2 / 2.9% | −6.4 / **10.9** / 22.2 · −34.5% |
| CN NVIDIA | nvda v2.0 (at $145.98) | 3.96% / 9.6 / 6.6% | 1.2 / **14.6** / 42.9 · −16.1% |
| CA Amazon | amzn v2.1 | 2.94% / 24.1 / 1.9% | −14.7 / **7.7** / 18.0 · −52.9% |
| CU Micron | mu v4.1 (at $690.44) | 0.92% / 3.6 / 4.1% | −0.5 / **8.2** / 28.4 · +0.7% |
| E Meta, Oracle | AI BBB E-rest row, E cash conversion | 1.77% / 16.4 / 1.7% | 6.9 / **18.0** / 24.3 · +0.6% |
| H1 Broadcom, AMD, Marvell | AI BBB H1 | 2.94% / 20.7 / 2.3% | −21.9 / **−8.0** / 8.9 · −62.1% |
| H3 ASML, Applied, Lam | AI BBB H3 | 1.23% / 20.0 / 1.0% | −14.0 / **5.4** / 15.8 · −47.9% |
| H4 Arista, Vertiv, Eaton | AI BBB H4 | 0.47% / 25.8 / 0.3% | −21.5 / **−4.6** / 8.7 · −62.4% |
| T software (8 names) | AI BBB T | 1.29% / 20.9 / 1.0% | −3.9 / **7.9** / 16.2 · −28.8% |
| **AI layers + companies** | | **23.0% / 14.9 / 24.8%** | **−6.2 / 9.0 / 23.5 · −32.2%** |
| EN energy | Oil BBB | 4.22% / 13.8 / 4.9% | −13.5 / **−4.4** / −3.1 · −41.1% |
| **Rest** | Equity BBB rest path | **72.7% / 16.5 / 70.4%** | **2.6 / 6.8 / 10.3 · −9.2%** |
| **Index (before cost)** | | **100% / 16.0** | **0.1 / 6.9 / 13.2 · −15.8%** |

- **The AI part now returns more than the rest** (9.0% against 6.8%): the sell-off took the AI and company blocks to P/E 14.9 on CY27
  against 16.5 for the rest. NVIDIA (14.6% at $145.98) and Microsoft (11.9%) are the strongest blocks; H1 and H4 still return below
  zero in Base at P/E 21–26.
- **Meta and Oracle (E) and Micron lose only ~9% in USD in the 2027 Bear** (about 0% in NOK after the krone's +10.8%): both already
  trade at or below their Bear exit marks (E at P/E 16.4 against the AI BBB's Bear exit P/E 17; Micron at 3.6 on CY27). For E the
  layer method then gives almost no Bear de-rating (flag to the AI BBB).
- **Wider AI list left in the rest** (Cisco, CrowdStrike, Palo Alto, GE Vernova, KLA, SanDisk, Amphenol, Shopify, Advantest, Tokyo
  Electron, Dell and others, ~4% of MSCI World) `[C]`; Apple and Tesla are in no AI layer. TSMC, SK hynix and Samsung are emerging
  markets, not in MSCI World.

## Common assumptions

| Item | Value | Basis |
|---|---|---|
| Company blocks | Analyses' per-share V_t, D_t and EPS per scenario; their cash inside V_t; Base and Bull interim V_t re-glided to the 19 Nov close (core P/E glides to the exit P/E); Bear at its exit P/E from end-2027; CY27 consensus MSFT 22.11, GOOGL 14.91, NVDA 15.21, AMZN 10.66, MU 191.80 | Company analyses; Equity BBB |
| Layer blocks | AI BBB EPS paths, exit P/E, payout; Base and Bull glide from today's block P/E to exit, Bear at its exit level at end-2027; (c − payout) × EPS accumulates in V_t | AI BBB Interface |
| Energy | EPS (Brent − 30) / 49 on the 9 Oct consensus basis; P/E 13.8 → exit 11 / 12 / 13; payout 0.58, conversion 0.80 | Equity BBB |
| Rest | CY27 earnings = the 18 Oct rest × URTH unit change × 1.006 (S&P 500 CY27 revision); Equity BBB EPS, multiple and payout paths | Equity BBB `[A]` |
| Currency | 70% USD/NOK, 30% I-44, relative to the 19 Nov spot | Equity BBB |
| Cost | 0.25% (Nordnet) or 0.21% (DNB pension platform), a continuous drag on value and dividends | `[C]` |
| Tracking beyond cost | 0 (record within ~0.1 pp a year) | `[A]` |
| Triggers | NAV change at unchanged earnings and unchanged future values | Equity BBB convention |

## Exit and cross-check

| Bear / **Base** / Bull | DNB GI A (MSCI World) | Equity BBB World |
|---|---|---|
| Exit value multiple (V_2029 ÷ 2030 EPS, incl. retained cash) | 14.9 / **16.9** / 18.5 | 15.0 / **17.0** / 18.5 (mid-cycle P/E) |
| Exit P/B (book rolled forward with earnings less dividends) | 2.48 / **3.12** / 3.77 | 2.48 / **3.12** / 3.77 |
| Buyer's implied return at exit (normalised cash yield + long-run growth) | 7.1 / **8.2** / 8.7% | 7.1 / **8.2** / 8.7% |

- DNB's exit is World's by construction: an independent market multiple at the market's mid-cycle return, never k and never the
  IAF ceiling. The value multiple glides from 16.0 today to 16.9 at exit in Base (Bear at 15 from end-2027).

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (dated, to the exit value; after 0.25% cost), spot FX | −2.7% | **6.7%** | 13.9% |
| IRR_T in NOK on the Equity BBB NOK path | −0.1% | **6.7%** | 12.9% |
| Rule 1 screen d + g at today's multiple (assumes 16.0 holds) | | 2.8 + 2.2 = **5.0%** | |
| d / g / c (NOK path) | 2.58 / −2.80 / 0.08 | **2.81 / 3.87 / −0.02** | 3.04 / 9.97 / −0.12 |
| g split: EPS (USD) / value multiple / FX / cost | −2.92 / −2.11 / +2.54 / −0.25 | **2.20 / 1.89 / 0 / −0.25** | 6.00 / 4.92 / −0.87 / −0.25 |
| ΣD / V_T (P = 100; NOK path) | 8.0 / 91.5 | **8.7 / 112.5** | 9.5 / 134.4 |
| P_k (hurdle NAV) / margin of safety, spot | 549 / −34.3% | **723 / −13.5%** | 880 / +5.2% |
| Rule 3: P/E on CY27 vs ceiling (d + g) / k² | | 16.0 vs 3.5: fails | |
| Capital preserved? ΣD + V_T vs P, spot / NOK path | No: −7.9% / −0.4% | Yes: +21.3% | Yes: +47.9% / +43.9% |

- **Structural run:** not applicable; the blocks carry their own cyclical paths. The structural reference is the World mid-cycle return
  (8.2% before cost, ≈ 8.0% after it).
- **Share of Bull already priced:** (P − P_k Base) / (P_k Bull − P_k Base) = **72%** at spot (85% on the NOK path).
- **Oil side case** (oil Bull, not weighted): World ≈ −12% in 2027 (Equity BBB), the fund ≈ −12%.
- Tail risks not modelled (as in the AI BBB): a Taiwan conflict, export-control escalation.

**Sensitivities** (after the 0.25% cost; NOK path; window IRR, %)

| Change | Bear | Base | Bull | Bear 2027 / Base 2027 | E / R | Margin (Base) |
|---|---|---|---|---|---|---|
| **Model** | −0.14 | **6.66** | 12.90 | −16.0 / 7.9 | 0.081 | −13.5% |
| DNB pension platform (0.21%) | −0.10 | 6.70 | 12.94 | −16.0 / 7.9 | 0.083 | −13.4% |
| Exit multiples −1 / +1 (blocks and rest) | −1.98 / 1.63 | 4.98 / 8.28 | 11.34 / 14.40 | −20.8 / −11.3 | 0.011 / 0.149 | −17.5 / −9.6% |
| All values ×0.9 / ×1.1 | −3.32 / 2.84 | 3.25 / 9.84 | 9.29 / 16.27 | −24.2 / −7.9 | −0.068 / 0.195 | −21.5 / −5.6% |
| **Equity BBB multiple watch: exit value multiple 15.4 (×0.910)** | −2.98 | **3.62** | 9.67 | −23.3 / −1.5 | −0.051 | −20.6% |
| Rest growth 4.5% / 6.5% | | 5.97 / 7.35 | | / 7.1 / 8.6 | 0.054 / 0.107 | −15.2 / −11.9% |
| Rest CY27 consensus −3% | −0.93 | 5.88 | 12.13 | −18.0 / 5.5 | 0.049 | −15.4% |
| NOK 10% weaker / stronger by 2029 | | 10.02 / 3.07 | | / 11.4 / 4.3 | 0.193 / −0.081 | −5.2 / −21.9% |
| Brent −$10 / +$10 | | 6.39 / 6.92 | | | 0.073 / 0.089 | −14.2 / −12.9% |
| AI BBB order-cut watch (H1 2028–30 ×0.9; NVIDIA at its 16.7% case) | | 6.43 | | / 7.2 | 0.074 | −14.1% |
| + NVIDIA SEC probe wide case (NVIDIA 9.2%) | | 6.15 | | / 6.6 | 0.063 | −14.8% |

- **No single input in the baselines' range reaches k at the 19 Nov NAV.** The closest is a 10% weaker krone by 2029 (margin −5.2%).
- **The multiple is the largest risk to Base:** if the de-rating holds to exit, Base is 3.6% and E / R turns negative.
- NVIDIA's cases scale its Base V_t and D_t to its own IRR at $125.53 (16.7% order cut, 9.2% wide + order cut) `[A]`.

## Price versus our call (Step 6b)

- **What the price implies:** at NAV 835.76 the Base build returns k only with an exit value multiple of **19.8** on 2030 EPS
  (all values × 1.17; Base 16.9, Bull 18.5, MSCI World forward P/E 16.5 today), or with rest-of-World EPS growth of **13.1%** a year
  (Base 5.5%). On our Base the NAV is priced to return 6.9% before cost, below the market's own mid-cycle return (8.2%); at the
  20 Nov close (≈ 812.5) it returns 8.1% before cost, about at the mid-cycle return.
- **Sector turn calls, translated:**
  - Equity BBB **World value multiple lower** (55%, watch; L2 −1 VIX 35.9 and inverted, L3 −1 US HY OAS 3.52%, L5 −1 AI-led fall,
    against L1 +1 CY27 growth +16.2% and L4 +1 issuance open): not in Base; if applied, Base 3.6%, margin −20.6%. Moves Base on its
    confirmation (VIX > 30 for a week, US HY OAS > 4.0%, CY27 cut > 5%).
  - AI BBB **H1 2028–30 order cut by funded buyers** (45%, watch): −0.2 pp (6.4%); with NVIDIA's SEC-probe wide case −0.5 pp (6.2%).
  - AI BBB **H1 and H2 2028–30 lower** (18 Nov): in Base (the H1 layer and the NVIDIA and Micron blocks carry them).
  - H1 2027 up (55%), K1 2028 lower (50%), T software lower (50%), H3 flat: not sized by the AI BBB; at their weights in World
    (H1 layer 2.9%, T 1.3%, platforms via the company blocks) under ±0.3 pp `[A]`.
- **Fund leading signals** (scored): an index fund has no insiders, buybacks or contracts. Tracking (YTD +0.32 pp against the
  benchmark) **0**; management fee 0.10% as before **0**; fund capital NOK 160.9bn (165.0bn on 18 Oct, about the price move: no flow signal) **0**.
  Score 0. The index-level families are the Equity BBB's and are read, not re-scored.
- **Verdict line (21 Nov, NAV 835.76): with the market.** At the 20 Nov close the index is priced to return the market's mid-cycle
  8.2% on our Base (6.9% at the 19 Nov NAV): the price holds our earnings path at about a normal multiple, and nothing in our Base
  is more positive or negative than that. We would be **behind** if the de-rating holds (the multiple watch); that call moves Base
  only on its confirmation signposts.
- **Scorecard:** v6 (29 Oct, NAV 867.98) had no Step 6b line; its call was "fails, the NAV above even the Bull hurdle". Since then
  the NAV fell 3.7% (and ≈ 2.8% more on 20 Nov): toward our call. Open: this run's line.

## Against high yield

| Base window, NOK, before tax | Base return | E (pp over NIBOR 4.72%) | R (Base 2027 − Bear 2027, pp) | **E / R** | Bear 2027 |
|---|---|---|---|---|---|
| Nordic HY market (after a typical 0.6% fee) | 6.9 | 2.15 | 8.47 | **0.254** (reference) | −0.4 (before fee) |
| World (Equity BBB, 20 Nov price, after 0.20%) | 8.0 | 3.23 | 23.7 | 0.137 | −12.9 |
| World on this build at the 19 Nov price (after 0.20%) | 6.7 | 2.01 | 24.0 | 0.084 | −15.8 |
| **DNB Global Indeks A, Nordnet (0.25%)** | **6.66** | **1.94** | **23.9** | **0.081** | **−16.0** |
| **DNB Global Indeks A, DNB pension platform (0.21%)** | **6.70** | **1.98** | **23.9** | **0.083** | **−16.0** |
| AI layers + companies in World, alone (before cost) | 9.0 | 4.3 | 39.7 | 0.109 | −32.2 |
| Rest of World, alone (before cost) | 6.8 | 2.1 | 18.6 | 0.112 | −9.2 |

- R uses the NOK-path Bear, as the Equity BBB and the HY reference do. At spot FX (no krone cushion) R is 32.1 and E / R 0.060.
- **The fund is dominated by HY on the 3-year rule:** a Base a little below the HY market after fees (6.66 against 6.9%), with
  2.8× its one-year stress (R 23.9 against 8.47 pp); E / R 0.081 against 0.254.

**Triggers** (NAV change from 835.76 at unchanged earnings and future values; forward P/E = MSCI 30 Oct 17.38 × index move `[A]`)

| Trigger | Nordnet (0.25%) | DNB pension platform (0.21%) |
|---|---|---|
| Pre-alert: Base = HY market after a typical fee (6.9%) | −0.7% → **NAV 830** (fwd P/E 16.4) | −0.6% → 831 |
| Base = HY market before fees (7.5%, the Equity BBB's pre-alert) | −2.3% → 816 (16.1) | −2.2% → 817 |
| **E / R = HY reference 0.254** | **−12.8% → NAV 728** (14.4) | −12.7% → 729 |
| **Base = k = 12% (P_k)** | **−13.5% → NAV 723** (14.2) | −13.4% → 723 |

- **State:** none crossed at the 19 Nov NAV. At the 20 Nov indicative NAV (≈ 812.5) the pre-alert and the 7.5% line are crossed;
  the E / R trigger is 10.4% lower.
- The Equity BBB's World trigger 1 (−8.7% from the 20 Nov close, URTH $171.1) is ≈ 742 in NAV terms from the indicative 812.5.
  This document's 728 is a uniform move from the 19 Nov price and mix; the 20 Nov fall was concentrated in NVIDIA and Micron,
  blocks with high Base returns, so the trigger on the 20 Nov mix sits higher (P_k 727 there against 723).
- The triggers drift up about 0.2% a month with reinvested dividends and move about one for one with consensus revisions, the AI
  paths and the multiple.

## Verdict and caveat

- **Verdict:** in the Summary. Band applied: Base margin of safety P_k / P − 1 = −13.5%, **fails** (below −2%); both platforms.
- **What would flip it:** a NAV at or below ≈ **738** makes it marginal and at or below ≈ **709** it clears (P_k 723); at today's
  NAV, an exit value multiple of 19.8 or rest EPS growth of 13.1%. A 10% weaker krone by 2029 (margin −5.2%) or all values ×1.1 (−5.6%) do not.
- **Caveat:** a margin-of-safety screen on the baselines' index model, not a price target or personal advice. The AI paths are the
  AI BBB's, the company paths their analyses', the rest and NOK paths the Equity BBB's; the 20 Nov NAV is an estimate.

## Risks and signposts

| Signpost | Threshold | Now | Source |
|---|---|---|---|
| DNB GI A NAV | ≤ 830 pre-alert · **≤ 728 E / R trigger** · ≤ 723 k | 835.76 (19 Nov); ≈ 812.5 indicative (20 Nov) | Nordnet, DNB AM |
| World value multiple (Equity BBB watch, 55%) | Confirm: VIX > 30 for a week, US HY OAS > 4.0%, CY27 cut > 5% · reverse: VIX < 25 | VIX 35.9 (one close); OAS 3.52% (19 Nov); CY27 +16.2% (13 Nov) | Equity BBB |
| MSCI World forward P/E | < 15.5 / > 19.5 | ≈ 16.5 (19 Nov; 30 Oct 17.38 scaled) | MSCI factsheet, Equity BBB |
| NVIDIA 10-Q (~25 Nov), SEC probe | funded-customer stress event; probe naming customer-financed revenue | NVIDIA Base 20.7% at $125.53; wide + order cut 9.2% (fund −0.5 pp) | `docs/nvda-analysis.md`, AI BBB |
| AI BBB order-cut watch (45%) | stress event, or B200 rental −15% for a month | watch | AI BBB |
| US HY OAS | > 4.5% (Bear) | 3.52% (19 Nov) | Equity BBB (FRED) |
| USD/NOK; I-44 | > 10.5 / < 9.2; > 117 / < 107 | 9.70 (19 Nov), 9.76 (20 Nov); I-44 110.7 (20 Nov) | Yahoo; Norges Bank |
| AI share of MSCI World (strict mapping) | > 30% | 23.0% (19 Nov) | URTH weights + prices |
| Fee or index change | any announcement | 0.25% / 0.21% | Nordnet, DNB |

**Stale after 6 Dec 2026** (the Equity BBB's full update with refreshed consensus), or earlier at a NIBOR path change in the HY BBB,
a company-block re-run that moves V_T by ≥ 5%, or a NAV at or below the E / R trigger (728).

## For other modules

- **`equity-market-bbb` (for its full update by 6 Dec; no re-run on its own):** two points. (1) GOOGL v2.3 and NVIDIA's v2.0 Bull
  interim V_t are not yet in `world3.py` (Base −0.03 pp; Bull 2027 20.6 → 21.2%). (2) At the 19 Nov price World Base is 6.9%
  before fees (E / R 0.084), at the 20 Nov close 8.15%.
- **`ai-market-bbb`:** Meta and Oracle (E-rest row) at P/E 16.4 on CY27 trade below the row's Bear exit P/E (17), so the layer
  method gives them almost no Bear de-rating in 2027 (−9% in USD, +0.6% on the NOK path). Whether the E-rest Bear exit P/E should sit
  below today's multiple is the baseline's decision.
- **`kospi`, `dnbtek` (comparison rows only):** DNB GI A Base 6.7%, E 1.94 pp, R 23.9, E / R 0.081, Bear 2027 −16.0% (NOK path) at
  the 19 Nov NAV; 7.9% and 0.134 at the 20 Nov indicative NAV. No input to their own Base.
- Company analyses: used as blocks; no input back.

## Change log

- **21 Nov 2026 — v7 (update chain; iaf-valuation 2026-11-18.1, Step 6b added):** DNB Global Indeks A only (Nordnet Global Indeks
  dropped, user 1 Nov); on the Equity BBB 20 Nov World build (Amazon and Micron blocks, AI BBB 18 Nov rows, Brent 80 / 73, NIBOR
  4.72%, HY reference 0.196 → 0.254) at the 19 Nov NAV 835.76. Base 4.58 → **6.66%** (inputs +0.74 pp, NAV −3.7% +1.34 pp), margin
  −19.0 → −13.5%, E / R 0.008 → 0.081, triggers 733 / 703 → 728 / 723; compacted to the lean rules.
- **29 Oct 2026 — re-mark on inputs** (Microsoft v3, Alphabet v2, AI BBB Updates 3–5): Base 4.66 → 4.58%, E / R 0.011 → 0.008; NAV
  date kept at 15 Oct.
- **18 Oct 2026 — Equity BBB Update 1** (World from blocks with an explicit rest): Base 6.03 → 4.66%; portfolio content removed
  (user).

## Appendix: own assumptions

By weight on the result:

1. DNB GI A is MSCI World on the Equity BBB World build (DNB's exclusions and tracking beyond cost ignored; record within ~0.1 pp).
2. The rest of World (70% of earnings) follows the Equity BBB's explicit path (consensus −3% in 2027, then 5.5% a year); ±1 pp of
   rest growth moves Base by ±0.7 pp.
3. Company blocks take their analyses' per-share paths at the 19 Nov closes, interim V_t re-glided; GOOGL v2.3 and NVIDIA v2.0 Bull
   interim values replace the Equity BBB's.
4. The decision is at the published 19 Nov NAV and the 19 Nov closes (NAV-date pricing); the 20 Nov NAV ≈ 812.5 is URTH × USD/NOK
   (Yahoo), error about ±0.1–0.5% a day.
5. Equity BBB FX path (70/30) relative to the 19 Nov spot; Base spot flat.
6. Costs 0.25% and 0.21% as of 8 and 11 Oct (not re-checked: Nordnet's total price did not load on 21 Nov).
7. NVIDIA's order-cut and SEC cases scale its Base V_t and D_t to its own IRRs.

## Appendix: sources

| # | Source | Content | Observed |
|---|---|---|---|
| S1 | [Nordnet, DNB Global Index A](https://www.nordnet.no/fond/liste/dnb-global-indeks-a-nok-7b4b0894) | NAV 835.76 (19 Nov), −1.24% | 21 Nov 2026 |
| S2 | [DNB Asset Management, DNB Global Indeks](https://dnbam.com/en/our-funds/funds/dnb-global-indeks) | NAV 846.23 (18 Nov); YTD 3.21 vs 2.89%; 1 y 7.00 vs 6.71%; fund NOK 160,869m; holdings of 14 Oct | 21 Nov 2026 |
| S3 | DNB pension fund page; Nordnet fund page; Nordnet platform-fee FAQ | Cost 0.21% (DNB pension), 0.25% (Nordnet) | 8–11 Oct 2026 `[C]` |
| S4 | DNB AM record table; KID data | Annual record 2016–25, tracking, currencies, risk | 8 Oct 2026 `[C]` |
| S5 | Yahoo chart closes 18–20 Nov (`equity-market-bbb/references/dl2/recent_1120.json`) | URTH 197.72 / 193.91 / 187.43; USD/NOK 9.6237 / 9.7006 / 9.7568; EUR/USD 1.0972 (19 Nov); IXC 55.64; every block name | 20 Nov 2026 |
| S6 | Norges Bank API `EXR/B.USD.NOK.SP` | USD/NOK fixing 9.6866 (19 Nov), 9.7525 (20 Nov) | 21 Nov 2026 |
| S7 | iShares URTH holdings (`dl2/urth_ai_nov.json`) | MSCI World weights of the block names and energy | 4 Nov 2026 |
| S8 | MSCI World factsheet (via the Equity BBB) | Forward P/E 17.38, P/B 4.06 | 30 Oct 2026 |
| S9 | `docs/equity-market-bbb.md` (20 Nov note) and `references/world3.py` | World blocks, rest path, scenarios, NOK path, exit references, turn calls | 20 Nov 2026 |
| S10 | `docs/ai-market-bbb.md` | Layer paths (18 Nov), turn calls (20 Nov) | 18–20 Nov 2026 |
| S11 | `docs/msft-analysis.md` v3.3, `docs/googl-analysis.md` v2.3, `docs/nvda-analysis.md` v2.0, `docs/amzn-analysis.md` v2.1, `docs/mu-analysis.md` v4.1 | Per-share V_t, D_t, EPS per scenario | 20 Nov 2026 |
| S12 | `docs/oil-market-bbb.md`, `docs/hy-market-bbb.md` (18 Nov); `docs/hy-funds-analysis.md` (9 Nov) | Brent path; NIBOR market path, HY Base, reference E / R 0.254 | 9–18 Nov 2026 |

- **Validation:** the build at the 20 Nov close and zero cost reproduces the Equity BBB's World within 0.05 pp in Base (differences
  named under Market input); NVIDIA's flows give 20.8% at $125.53 (analysis 20.7%); the 18 → 19 Nov NAV move (−1.24%) is within
  0.1 pp of URTH × USD/NOK (−1.14%).
- **Script:** `.claude/skills/iaf-valuation/references/models/global-index/gidx7.py` (run `py gidx7.py` from its folder; it imports
  the Equity BBB's `world3.py` and `idxai3.py` unchanged and writes `gidx7_results.json`). The 11 Oct–29 Oct scripts stay in
  `equity-market-bbb/references/fund/` (`idxai3.py`–`idxai5.py`).
