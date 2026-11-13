# Equity Market BBB — 6 November 2026

**Status: Update 2 (full update, Step 0–8); Equity Market BBB changed (World; triggers)** · skill
`equity-market-bbb` revision 2026-10-24.1 · as of **6 Nov 2026** (prices: close Thu 5 Nov 2026) ·
**stale after 6 Dec 2026** · compacted 13 Nov 2026 (no value changed)

## Interface (values other documents read)

As of **6 Nov 2026**, prices at the 5 Nov close. NOK total return before fund fees. Cells
Bear / **Base** / Bull. The stub is identical across scenarios. Weights 25/50/25 are a convention,
never a probability. Market only: no named fund or single paper is analysed here.

**Index returns, % (stub one period, not annualised; window = IRR over 3.15 years)**

| Bear / Base / Bull | Stub Q4-26 (period) | 2027 | 2028 | 2029 | Window (ann.) | Mid-cycle (ann.) |
|---|---|---|---|---|---|---|
| **Oslo (OSEBX)** | 0.8 / 0.8 / 0.8 | −27.8 / **2.2** / 6.6 | 12.0 / **1.7** / 6.3 | 9.5 / **3.4** / 5.7 | −4.2 / **2.6** / 6.3 | 8.0 / **8.9** / 9.2 |
| **World (MSCI World, NOK unhedged)** | 0.3 / 0.3 / 0.3 | −18.3 / **7.7** / 15.8 | 8.6 / **6.2** / 10.9 | 10.3 / **6.5** / 10.2 | −0.8 / **6.6** / 11.9 | 7.1 / **8.2** / 8.7 |
| World (USD, local) | 0.3 / 0.3 / 0.3 | −26.2 / **7.7** / 19.0 | 11.3 / **6.2** / 10.9 | 10.3 / **6.5** / 10.2 | −3.3 / **6.6** / 13.0 | 7.1 / **8.2** / 8.7 |
| *Reference: Nordic HY (hy-market-bbb, 5 Nov)* | *1.1* | *−0.4 / 8.0 / 10.7* | *10.8 / 7.2 / 7.1* | *8.2 / 6.8 / 6.1* | *6.0 / 7.2 / 7.7* | *5.7 / 6.3 / 6.5* |
| *Reference: 3M NIBOR (hy-market-bbb)* | *4.80 (ann.)* | *4.21 / 4.79 / 4.65* | *3.55 / 4.39 / 4.15* | *3.50 / 3.86 / 3.65* | *— / 4.37 / —* | *3.25 / 3.45 / 3.45* |

**Earnings, multiple and NOK paths** (EPS: annual; P/E and FX: year-end; the 2029 year-end P/E is the
exit multiple)

| Path, Bear / Base / Bull | Now (5 Nov) | 2027 | 2028 | 2029 | 2030 (normalised exit year) |
|---|---|---|---|---|---|
| **Oslo index EPS** (CY27 consensus of 6 Nov = 100, NOK at the 5 Nov spot) | — | 83.2 / **105.6** / 105.2 | 76.1 / **97.2** / 99.1 | 80.7 / **94.2** / 97.6 | 83.6 / **93.0** / 96.6 |
| Oslo block E, oil-linked (block CY27 consensus = 1.00, before FX) | — | 0.70 / **1.16** / 1.16 | 0.60 / **0.94** / 0.94 | 0.60 / **0.84** / 0.84 | 0.60 / **0.80** / 0.80 |
| Oslo block F, rates and credit (DNB, STB, GJF) | — | 0.85 / **0.98** / 1.00 | 0.80 / **0.96** / 1.03 | 0.88 / **0.95** / 1.05 | 0.90 / **0.93** / 1.02 |
| Oslo block O, other | — | 0.85 / **0.97** / 1.00 | 0.85 / **1.02** / 1.08 | 0.93 / **1.07** / 1.15 | 1.00 / **1.10** / 1.19 |
| **World index EPS** (CY27 consensus = 100, USD; sum of blocks) | — | 79.6 / **96.7** / 100.7 | 78.5 / **100.0** / 107.1 | 85.0 / **104.1** / 113.3 | 91.2 / **108.8** / 119.9 |
| — AI + companies (own CY27 consensus = 100; 24.7% of earnings) | — | 71.5 / **91.7** / 99.0 | 57.6 / **94.2** / 109.6 | 61.2 / **96.7** / 116.8 | 66.4 / **99.5** / 124.4 |
| — energy (4.9%) | — | 71.4 / **118.4** / 118.4 | 61.2 / **95.9** / 95.9 | 61.2 / **85.7** / 85.7 | 61.2 / **81.6** / 81.6 |
| — rest (70.4%) | — | 83 / **97.0** / 100 | 87 / **102.3** / 107 | 95 / **108.0** / 114 | 102 / **113.9** / 121 |
| Oslo forward P/E | 11.8 on CY27 | 10.5 / **11.7** / 12.0 | 10.5 / **11.6** / 12.3 | 10.5 / **11.5** / 12.5 | — |
| **World total value multiple** (V_t ÷ EPS_t+1, USD) | 16.4 on CY27 (MSCI basis ≈ 16.95) | 15.0 / **17.2** / 17.8 | 15.0 / **17.1** / 18.2 | 15.0 / **17.0** / 18.6 | — |
| World rest P/E | 16.9 on CY27 | 15.1 / **17.2** / 17.8 | 15.0 / **16.7** / 17.6 | 14.9 / **16.3** / 17.4 | — |
| **I-44** (Base = spot flat; Norges Bank MPR 3/26: 110.0) | 107.8 | ~116.4 (+8%) / **107.8** / ~105.6 (−2%) | ~114.2 (+6%) / **107.8** / ~105.6 | ~114.2 (+6%) / **107.8** / ~105.6 | — |
| **USD/NOK** | 9.29 | 10.41 (+12%) / **9.29** / 9.02 (−3%) | 10.14 (+9%) / **9.29** / 9.02 | 10.14 (+9%) / **9.29** / 9.02 | — |

**Hurdles, triggers, exit references and blocks**

| Item | Oslo (OSEBX) | World (MSCI World, NOK unhedged) |
|---|---|---|
| Level, 5 Nov 2026 | 2,080.59 `[F]`; MSCI Norway P/B ≈ 2.39, forward P/E ≈ 12.1 (30 Oct × OSEBX move since 30 Oct, −3.0%) | URTH 199.63 USD × 9.2944 = 1,855.4 NOK `[F]`; MSCI World forward P/E ≈ 16.95 (30 Oct 17.38 × URTH move since 30 Oct, −2.4%) |
| Base window IRR | **2.6%** | **6.6%** |
| P_k at k = 12% (hurdle level) / margin of safety | 1,617 / **−22.3% (fails)** | 1,601 / **−13.7% (fails)** |
| E: Base excess over NIBOR after 0.20% fee | −1.92 pp | 2.08 pp |
| R: Base 2027 − Bear 2027 | 29.9 pp | 25.9 pp |
| **E / R** (HY market reference **0.254**) | **−0.06** | **0.080** |
| Bear: capital kept (ΣD + V_T vs P) | −11.8% | −2.4% |
| **Trigger 1:** E / R = 0.254 | **−28.3% → 1,492**; P/B ≈ 1.71, fwd P/E ≈ 8.7 | **−14.3% → 1,590** (URTH 171.1 USD); fwd P/E ≈ 14.5 |
| Trigger 1, sensitivity: E / R = 0.216 (HY Bear read as a shock) | −24.5% → 1,570; P/B ≈ 1.80, fwd P/E ≈ 9.2 | −11.0% → 1,651 (177.6 USD); fwd P/E ≈ 15.1 |
| **Trigger 2:** Base IRR = 12% (k) | −22.3% → 1,617; P/B ≈ 1.85, fwd P/E ≈ 9.4 | −13.7% → 1,601 (172.2 USD); fwd P/E ≈ 14.6 |
| Pre-alert: Base IRR = HY market Base **7.2%** | −11.8% → 1,834; P/B ≈ 2.10, fwd P/E ≈ 10.7 | **−1.6% → 1,827** (196.5 USD); fwd P/E ≈ 16.7 |
| Trigger state | None crossed | None crossed; 1.6% above the pre-alert |
| **Exit P/E** Bear / Base / Bull (World: mid-cycle P/E) | 10.5 / **11.5** / 12.5 | 15.0 / **17.0** / 18.5 |
| **Exit P/B** Bear / Base / Bull | 1.48 / **1.74** / 1.95 | 2.47 / **3.17** / 3.74 |
| **Mid-cycle return** Bear / Base / Bull | 8.0 / **8.9** / 9.2 | 7.1 / **8.2** / 8.7 |
| Blocks: share of CY27 earnings; P/E on CY27 | E 44%, 9.5 · **F 22%, 12.8** · O 34%, 14.2 | Companies (MSFT, GOOGL, NVDA, AMZN, MU) 18.5%, 14.4 · AI layers 6.3%, 18.7 · energy 4.9%, 14.2 · rest 70.4%, 16.9 |
| Block F detail (rates and credit) | Weight in sample 24%; P/E CY26 14.1; consensus EPS CY27 vs CY26 +9.8%; forward dividend yield 4.5%; payout 0.65; P/B 2.21 / ROE 15.2% (trailing); path NIBOR 4.79 → 3.86 → mid-cycle 3.45 compresses margins, Bear losses peak in 2028 with HY defaults | — |
| Payout and cash conversion | Payout per block E 0.58, F 0.65, O 0.49 (0.565 weighted); energy cash conversion 0.80, (0.80 − 0.58) × EPS credited to V_t | Payout 0.46 plus 0.03 credited (AI layers, energy 0.58 with conversion 0.80; rest ~0.49) |
| Currency rule | USD/NOK on all of E; I-44 on the foreign half of O | 70% on USD/NOK, 30% on I-44 (Bear factor 1.108 / 1.081 / 1.081 against spot, Bull 0.973) |

- **Scenarios** (catalysts with signposts under "Scenario definitions"):
  - **Bear (25%):** oil Bear (Brent 65 / 60 / 60; mid-cycle 60; durable Iran–USA deal + OPEC+
    market-share quotas) with a global recession in H1 2027 (HY Bear macro: NB cuts to 3.50% by
    Q4-27, mainland GDP −0.5% in 2027, Nordic spread YE-27 850 bp), and the AI BBB Bear inside
    World; NOK weaker. Earliest Q1 2027.
  - **Base (50%):** oil Base (88 / 77 / 72; mid-cycle 70); Norges Bank on the MPR 3/26 path;
    mainland GDP ~1%; the AI earnings boom slows to trend; P/E drifts to its mid-cycle level; NOK
    spot flat.
  - **Bull (25%):** oil Base; soft landing (first NB cut Q3-27); earnings meet consensus; Oslo P/E
    to 12.5, World rest ~17.5; NOK firms. Earliest Q2 2027.
  - Oil side case (oil Bull, not weighted): Oslo ≈ +15%, World ≈ −12% in 2027.
- **HY market reference** (`docs/hy-market-bbb.md`, 5 Nov): E / R **0.254** (E 2.15 pp after a 0.6%
  fee, R 8.47 pp; 0.216 with Bear read as a shock); HY market Base window 7.2% before fees.
- **NOK anchor and switch:** Base = spot flat while spot is within 3% of Norges Bank's I-44
  projection (110.0; spot 107.76 is 2.0% stronger). Below ~106.7, Base follows the MPR path from
  Year 1. MPR 4/26 (17 Dec) gives a new projection. Bear and Bull are relative moves (USD/NOK +12% /
  +9% / +9% and −3%; I-44 +8% / +6% / +6% and −2%): readers apply them to the spot of their own
  analysis date.
- **Signpost states:** no signpost crossed and held. I-44 Bull level (< 107) touched 30 Oct and
  3 Nov, not held; MSCI Norway P/BV 2.46 at end-Oct, close to the 2.5 valuation warning; World
  1.6% above its pre-alert.
- **Dated events:** listed under "Signposts and monitoring" (next: NVIDIA Q3, 17 Nov; MPR 4/26,
  17 Dec).
- **Readers:** company analyses (iaf-valuation) read market context only (both Base IRRs below
  k = 12%; k not changed) and the exit references above. ai-market-bbb reads World's paths,
  scenarios and NOK path; World carries Amazon and Micron as company blocks and keeps the AI BBB's
  E rest row for Meta and Oracle only. hy-market-bbb: no input to its paths; the equity Bear (−18%
  to −28% in 2027) is consistent with the HY Bear's spread path (Nordic 850 bp at end-2027).

## Metadata

- **Analysis date:** Fri 6 Nov 2026 (morning), Europe/Oslo. Prices: last close Thu 5 Nov 2026 (Oslo
  and US). Full update (Step 0–8) after the Q3 reports, OPEC+ (1 Nov) and Norges Bank (5 Nov).
- **Trigger for this run:** user request, on the register's flags: the HY BBB update of 5 Nov
  (reference E / R and HY market return moved; the equity triggers mirror the HY rule); the US
  midterms (3 Nov) and the 5 Nov tech and chip sell-off; the Q3 reports, OPEC+ and Norges Bank.
- **Skill revisions:** `equity-market-bbb` **2026-10-24.1**. Upstream, read only: `oil-market-bbb`
  2026-10-24.4; `hy-market-bbb` 2026-10-24.1; `ai-market-bbb` 2026-11-06.1 (its Update 6 and 5 Nov
  check were run under 2026-11-01.1; the text is the same); `iaf-valuation` 2026-11-01.1 (company
  blocks: Microsoft v3 and Alphabet v2 under 2026-10-18.2, the Alphabet re-mark and Amazon v2
  under 2026-10-29.1, NVIDIA v1.2 and Micron v3 under 2026-11-01.1).
- **Upstream baselines and inputs:**

| Input | Date | Revision / status | Stale after | Used for |
|---|---|---|---|---|
| Oil Market BBB | 31 Oct 2026, update 4 Nov (kept unchanged) | Final (skill 2026-10-24.4) | 7 Nov 2026 (follow-up planned) | Brent Bear 65 / 60 / 60, **Base 88 / 77 / 72**, Bull 118 / 102 / 90; mid-cycle 60 / **70** / 82 → Oslo and World energy. Stub 104.3. Midterm read (4 Nov): Bear catalyst closer, Bull window mainly to 3 Jan |
| Nordic HY Market BBB | 5 Nov 2026 | Final (skill 2026-10-24.1) | 5 Dec 2026 | NIBOR path 4.80 / 4.79 / 4.39 / 3.86, Nordic GDP and the Bear macro; HY market Base window 7.2%; market reference **E / R 0.254** (E 2.15 pp after a 0.6% fee, R 8.47 pp; 0.216 with Bear read as a shock) |
| AI Market BBB | Update 6 of 1 Nov 2026; 5 Nov check (kept unchanged) | skill 2026-11-06.1 | 16 Dec 2026, or NVIDIA Q3 (17 Nov) | Layer EPS paths, exit P/E, payout, cash conversion (E layer **−.20 / .00 / .20**); calendarised CY27 consensus (1 Nov) |
| Company analyses (World company blocks) | Microsoft v3 (28 Oct); Alphabet v2 with its re-mark (30 Oct close); NVIDIA v1.2 (5 Nov close); Amazon v2 (30 Oct); Micron v3 (5 Nov close) | iaf-valuation (see above) | — | Per-share EPS, D_t and V_t per scenario; interim V_t of Base and Bull re-glided to the 5 Nov price |
| URTH holdings (MSCI World weights) | 4 Nov 2026 | iShares holdings CSV `[F]` | — | Block weights (`references/dl2/urth_ai_nov.json`), repriced to the 5 Nov close |

- **Window:** stub 6 Nov–31 Dec 2026 (55 days) + 2027–2029; exit 31 Dec 2029, T = 3.15 years.
  **Stale after 6 Dec 2026** (30 days), or earlier at an oil follow-up (7 Nov) or full update that
  flags a change for equity; an AI BBB update after NVIDIA's Q3 (17 Nov) that moves a path; an
  index move of more than 10% within a month, or a trigger crossed (World is 1.6% above its
  pre-alert). Norges Bank's MPR 4/26 (17 Dec) comes after; it gives a new I-44 projection for the
  Base NOK anchor.
- **Prices (Yahoo, 5 Nov close; all prints in the Appendix):** OSEBX **2,080.59** (−1.0% on the
  day); URTH **199.63 USD** (−4.0%); S&P 500 −4.4%. USD/NOK **9.2944** (Norges Bank fixing 9.2984);
  Norges Bank fixing **I-44 107.76** `[F]`. URTH in NOK = 199.63 × 9.2944 = **1,855.4**.
- **Rates:** US 10-year **4.90%** (FRED `DGS10`, 4 Nov); US HY OAS **3.32%** (`BAMLH0A0HYM2`,
  4 Nov); Norway 10-year **4.37%** (Norges Bank, 4 Nov).
- **Tags:** `[F]` fact or market print · `[E]` external forecast or secondary · `[A]` own
  assumption · `[?]` unknown.
- **Market only:** no named fund, single paper or portfolio is analysed, and
  `docs/portfolio-overview.md` is neither read nor written. Company analyses and the AI BBB enter
  only as building blocks of World's index earnings.

## Conclusion

- **Changed at this run: World and the triggers.** World's Base window moved by more than the
  1.0 pp minimum, mostly from the lower price at about unchanged index earnings; Oslo's was
  re-marked below the minimum (view unchanged). The triggers moved with the HY market reference
  (0.254). Kept: scenarios, catalysts, P/E paths, the rest path, Oslo block paths relative to
  consensus and the NOK relative moves.
- **World (MSCI World, NOK unhedged): Base 6.6%**; Bear −0.8% (2027 −18.3% in NOK, −26.2% in
  USD); Bull 11.9%. E / R **0.080** against the HY reference 0.254. The cash yield (2.8%), the
  rest's 5.5% growth and a value multiple that starts below its exit (16.4 on CY27 against 17.0)
  carry the Base.
- **Oslo (OSEBX): Base 2.6%**; Bear −4.2%; Bull 6.3%; E / R −0.06. The return is the
  normalisation: today's price capitalises energy earnings the oil baseline expects to fall, and
  the dividend yield carries it. Payout per block is on post-Q3 trailing EPS (Equinor, Hydro,
  Telenor's gain); energy's total cash stays 0.80 (paid plus credited).
- **US midterms (3 Nov) and the 5 Nov sell-off: a price event, read through the upstream
  documents.** Democrats won both chambers; nothing changes in law before 3 Jan 2027, and there is
  no veto-proof majority. Oil kept its paths (4 Nov), the AI BBB kept its paths (5 Nov: a
  de-rating of the capex receivers, not a fundamental change), and HY kept NIBOR and GDP. The rest
  of World (70% of its earnings) has no fiscal or tax change in law to model, so its path is kept
  `[A]`. 5 Nov: S&P 500 −4.4%, URTH −4.0%, SOX about −10 to −12% `[E]`, OSEBX −1.0%.
- **Q3 reports:** S&P 500 Q3 blended earnings +30.2% (82% beat, 60% reported), CY27 growth
  **+16.3%** (FactSet, 30 Oct); the "Magnificent 7" missed in aggregate (−14.7%) and the other 493
  beat; the rest's CY27 base is raised 0.6% (S&P 500 proxy) `[A]`. Oslo CY27 consensus **+2.5%**
  since 11 Oct (energy +9.9% with the higher strip, financials +1.0%, other −4.9%: Yara −13.5%,
  Hydro −8.4%), below the 5% recalibration trigger.
- **Both indices stay below HY and far below k = 12%.** The Nordic HY market's Base is 7.2% before
  fees and pays 0.254 per unit of the same stress; World pays 0.080 and Oslo nothing.
- **Triggers (mirror of the HY trigger; levels, P/E and P/B in the Interface):** none crossed.
  World trigger 1 −14.3% (URTH in NOK ≈ 1,590), pre-alert −1.6% (≈ 1,827): World is close to it.
  Oslo trigger 1 ≈ 1,492 (−28.3%), Base = k at 1,617 (−22.3%).
- **Valuation (30 Oct month-end, scaled to 5 Nov):** Oslo MSCI Norway P/BV 2.46 (≈ 2.39), close to
  the 2.5 valuation warning; bottom-up 2.27, 2.06 without Kongsberg. World forward P/E 17.38
  (≈ 16.95), P/BV 4.06 (≈ 3.96). Exit P/B: Oslo 1.74 at a normalised ROE of 14.7%, inside the
  band; World 3.17 at ROE 18.6%.
- **NOK:** I-44 107.76, 2.0% stronger than Norges Bank's 110.0 projection, inside the 3% tolerance:
  Base stays spot flat. The I-44 Bull signpost (< 107) was touched on 30 Oct and 3 Nov (106.7) and
  not held.
- **Main Bear catalyst:** the HY Bear: oil Bear (a durable Iran–USA deal plus OPEC+ market-share
  quotas; closer after the midterms per the oil baseline) together with a global recession in H1
  2027, with the AI BBB Bear inside World (financing break, also state siting policy).
- **Main Bull catalyst:** soft landing, oil on Base, AI earnings on the AI BBB Bull.
- **Oil side case (not weighted):** Oslo ≈ +15%, World ≈ −12% in 2027.

## Path and trigger notes, mid-cycle inputs and exit consistency

- **Stub:** one period (55 days), not annualised: price flat by convention, cash accrual only,
  identical in all scenarios `[A]`. The NIBOR window (4.37%) uses the 55-day stub; the HY BBB's
  4.38% uses its own stub from 1 Oct. The HY row is the HY BBB's own window (from 1 Oct, 3.24
  years, with October's −0.2% in its stub); the decision rule compares like with like (E and R),
  so the two windows are used as published.
- World hedged to NOK ≈ the USD row + NIBOR − USD short rate (4.80 − SOFR 3.94 ≈ +0.9 pp a year,
  HY BBB 5 Nov) `[A]`: Base ≈ 7.5%, but Bear 2027 ≈ −25.3% because the NOK cushion is lost.
- Oslo Bull EPS in 2027 (105.2) is below Base (105.6): Bull keeps oil on Base and firms the NOK,
  so USD earnings are worth less in NOK.
- **World's value multiple** includes the retained cash credited in the blocks. It starts below
  its exit level (16.4 against 17.0): most AI names fell from mid-October (Marvell −41%, Lam −30%,
  Micron −25%, AMD −24%, Alphabet −17%, NVIDIA −15% since 16 Oct; Microsoft and Amazon rose) while
  the rest's P/E stayed at 16.9. Part of the Base rise in 2027 (16.4 → 17.2) is Micron's P/E
  rising as its EPS falls (3.4 now, towards 10 on the AI BBB H2 path), not a market re-rating. The
  rest's multiple path is the 11 Oct World view without its AI and energy part. The World exit
  reference (mid-cycle P/E) is 15.0 / 17.0 / 18.5; the value multiple at the 2029 year-end is
  15.0 / 17.0 / 18.6.
- World blocks' multiples: AI + companies 15.5 on CY27 (companies 14.4, layers 18.7); energy 14.2.
  Exits: AI BBB layer exit P/E (E 21, H1 17, H3 18, H4 20, T 20 in Base) and the company analyses'
  V_t.
- **NOK:** Norges Bank called the krone "stronger than assumed" on 5 Nov (HY BBB); Bear and Bull
  relative moves are applied to the 5 Nov spot `[A]`.
- **Triggers:** at unchanged earnings and future values; they move with consensus revisions, the
  oil and AI paths, NIBOR and the HY reference.
  - Oslo's trigger 1 lies below k: Oslo's R is large (29.9 pp), so at k its E / R is only ≈ 0.19.
    World's E / R at k is ≈ 0.25, just under the reference.
  - **Brent and Oslo's trigger 1:** ±$10 on the Base and Bull paths only moves it −2.1% / +1.6%
    (1,461 / 1,516; R changes with Base 2027). ±$10 on all scenarios, the Bear included, moves it
    ±13% (1,300 / 1,683; R unchanged): the "whole oil world shifts" case.
  - **Drift:** OSEBX is a gross index, so its levels drift up ~0.45% a month with reinvested
    dividends. At a fixed level P/B falls ~0.5% a month as book grows by retention. Only the P/E
    form at unchanged earnings stays put.
  - **A stronger NOK does not reach the World trigger while Base is spot flat:** the NOK price and
    the future NOK values fall together. It counts only if spot moves more than 3% from Norges
    Bank's projection, when Base follows the MPR path.
  - **Multiples at the triggers:** the MSCI month-end figure (30 Oct) × the index move since that
    month-end × the trigger's change `[A]`.
- Sensitivities (multiples, NOK, Brent, rest growth) are in "Return split" below.

**Mid-cycle inputs** (cash yield at mid-cycle P/E + long-run nominal EPS growth, no re-rating;
`[A]` except where tagged):

| Index | Scenario | Cash conversion | Mid-cycle P/E | Cash yield | Long-run EPS growth | Mid-cycle return |
|---|---|---|---|---|---|---|
| Oslo | Bear / **Base** / Bull | 0.64 | 10.5 / **11.5** / 12.5 | 6.1 / **5.6** / 5.1 | 1.8 / **3.3** / 4.1 | 8.0 / **8.9** / 9.2 |
| World | Bear / **Base** / Bull | 0.49 | 15.0 / **17.0** / 18.5 | 3.3 / **2.9** / 2.6 | 3.8 / **5.3** / 6.1 | 7.1 / **8.2** / 8.7 |

- **Base growth:** Oslo on block trends and normalised earnings shares: energy 2% (inflation, flat
  volumes) × 38%, F 3.5% (nominal mainland GDP) × 22%, O 4.5% × 40%; cash conversion on the same
  shares energy 0.80, F 0.65, O 0.49. World: the rest's 5.5% trend on all non-energy blocks, and
  energy 2% × 4.9%. Bear is 1.5 pp lower and Bull 0.75 pp higher.
- **Implied return on retained earnings:** Oslo 3.3% ÷ 0.36 ≈ 9%, World 5.3% ÷ 0.51 ≈ 10%. Both
  are below ROE (15% and 19% at exit) and below k: dilution (new issues, share-based pay), field
  decline in Oslo energy, and low-return reinvestment. Oslo's higher mid-cycle return comes from
  its cash yield (5.6% against 2.9%), not from growth.

**Exit consistency per block** (gap = EPS multiplier in 2029 ÷ normalised multiplier of 2030 − 1;
material if |gap| > 10%):

| Block | Gap Bear / Base / Bull | Treatment |
|---|---|---|
| Oslo E, World energy (Brent − 30) | 0 / +5% / +5% | Not material (Brent 72 in 2029 against mid-cycle 70) |
| Oslo F | −2% / +2% / +3% | Not material |
| Oslo O, World rest (P/E × EPS on trend) | — | No gap by construction |
| E rest (Meta, Oracle) | −8% / −8% / −10% | Not material; continuing growth priced on 2030 EPS |
| H1 compute | −7% / +3% / −4% | Not material |
| H3 foundry and equipment | −6% / −5% / −9% | Not material |
| H4 networking and DC infra | **−14%** / −4% / −6% | Bear material. Named reason in the AI BBB: revenue −20% in 2028, flat in 2029, and 2030 recovers part of the way. A 2-year tail would move World Bear by < 0.01 pp; not applied |
| T software | −7% / −7% / −8% | Not material |
| Microsoft | −7% / −8% / −10% | Carried from its analysis (growth; V_T on 2030 EPS) |
| Alphabet | **−11%** / −9% / **−11%** | Carried from its analysis: Bear is the recovery from the 2028 trough, Bull continuing growth |
| NVIDIA | −7% / +3% / −4% | Carried from its analysis |
| Amazon | **−14%** / −9% / **−13%** | Carried from its analysis: as Alphabet |
| Micron | 0 / **+14%** / **+22%** | Named reason in the AI BBB: the H2 memory path turns in 2028 and is normalised in 2030, the year after exit; V_T is on the 2030 normalised EPS. A tail would add < 0.01 pp |

- The tails would move every World IRR by less than 0.05 pp in total, so no tail is applied.

## Scenario definitions

Catalysts and mechanisms; the midterm timing is taken from the oil and AI baselines.

| Scenario | Weight (convention) | Oil BBB | HY BBB macro | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|---|
| **Bear** | 25% | **Bear** (Brent 65 / 60 / 60; mid-cycle 60) | Bear: NB cuts to 3.50% by Q4-27; mainland GDP −0.5% (2027); defaults peak 8.6% (2028); Nordic spread YE-27 850 bp | Durable Iran–USA deal + OPEC+ market-share quotas (closer after the midterms: a Democratic Congress presses to end the war from 3 Jan); global recession H1 2027 after the energy shock; inside World the AI BBB Bear (financing break; state siting policy as a second route to the 2028 capex cut) | Oslo energy EPS −30% vs consensus 2027 in USD (partly offset in NOK); bank losses; World EPS 0.80 of CY27 consensus in 2027 (AI + companies 0.72 on the AI BBB and company Bears, rest 0.83); P/E to 10.5 (Oslo) and ~15 (World rest); NOK weakens (USD/NOK +12%, I-44 +8%) | Q1 2027 | Oil Bear signposts (Dec-27 Brent < $70, ceasefire > 60 days) · US HY OAS > 450 bp · S&P CY27 growth consensus < +8% · MSCI World fwd P/E < 15.5 · USD/NOK > 10.5 · Nordic HY spread > 550 bp · AI BBB Bear signposts |
| **Base** | 50% | **Base** (88 / 77 / 72; mid-cycle 70) | Base: NB MPR 3/26 path (held 4.50% on 5 Nov); mainland GDP ~1% | Armed normalisation in oil; higher-for-longer rates; the AI earnings boom slows to trend; Congress changes no law before 3 Jan | Oslo normalised exit-year EPS 7% below the 2027 consensus (energy −31% vs 2027 Base; the rest grows); World EPS = sum of blocks: AI + companies ~flat after 2027 (AI BBB Base and the company analyses), rest −3% then +5.5% a year → 1.088 of CY27 consensus by 2030 (+2.7% a year); P/E drifts to its mid-cycle level | Ongoing | Brent within the oil Base band · MSCI World fwd P/E 16–19 · CY27 consensus revisions within ±5% · NB on path (17 Dec MPR 4/26) |
| **Bull** | 25% | **Base** | Bull: first NB cut Q3-27; soft landing | Inflation falls faster; earnings meet consensus; risk appetite holds | World EPS 1.01 → 1.20 (AI BBB Bull and the company Bulls; rest +6.6% a year); rest P/E ~17.5; Oslo P/E to 12.5; NOK firms (USD/NOK −3%, I-44 −2%) | Q2 2027 | S&P CY27 consensus holds ≥ +15% through the Q4 reports · US HY OAS < 300 bp · CPI-ATE < 2.5% by mid-2027 · Nordic HY spread < 400 bp |

- **Why the Bear is recession + oil Bear, not stagflation:** the oil Bull (renewed US or Israeli
  strikes with retaliation against Gulf export infrastructure; its window runs mainly to 3 Jan,
  oil BBB 4 Nov; Brent 118 in 2027) lifts Oslo energy earnings ~76% above consensus 2027 and hits
  world equities. On the model: **Oslo ≈ +15%, World ≈ −12% (USD and NOK) in 2027** `[A]` (Oslo:
  O block −7%, P/E 11.0; World EPS −10% and value multiple 15.5 from today's 16.4; NOK assumed
  flat, since in 2026 a +93% Brent move strengthened the NOK only 8% against USD). For an investor
  holding both, or holding Nordic HY with its oil-linked issuers, the recession + oil collapse
  case is the worse one. Kept as the side case.
- 25/50/25 is a labelled convention; no scenario-weighted figure is computed.

## Valuation snapshot

MSCI figures are at month-end (30 Oct), scaled to 5 Nov where stated. The bottom-up P/B, ROE and
yields are at the 5 Nov close; the consensus is Yahoo's of 6 Nov.

| Measure | Oslo | Source / date | Reference |
|---|---|---|---|
| P/E trailing | 13.85 | MSCI Norway, 30 Oct 2026 `[F]`; bottom-up **11.48** (5 Nov) | Norway ~13.5 over the last 10 years (Affärsvärlden, c. 2023) `[E]`. The bottom-up trailing EPS already holds Q3 (Equinor P/E 8.6, Hydro 10.4, Telenor's gain); MSCI's month-end figure lags it |
| P/E forward | 12.51 (30 Oct); ≈ 12.1 at 5 Nov | MSCI Norway `[F]`; bottom-up 11.77 (Yahoo forward, 5 Nov); 10.7 on CY26, **11.8 on CY27** (80% of the OBX, Yahoo consensus 6 Nov) `[F/A]` | ~11–12 over the long run `[A]` |
| P/B | **2.46** (30 Oct); ≈ 2.39 at 5 Nov | MSCI Norway `[F]`. Bottom-up 5 Nov: **2.27** on OBX weights, 2.22 on MSCI weights, 2.39 on market cap; **2.06 without Kongsberg**. DNB OBX ETF 2.48, NORW 2.19 (Yahoo look-through) | Band 1.5 (cheap) – 2.1 (expensive): OSEBX, 67 names, Bloomberg, 13 years to Apr 2023 (Nordnet blog) `[E]`. The same source: P/B 2.4–2.7 has often been followed by losses `[E]`. MSCI's 2.46 on 30 Oct sat just under the 2.5 valuation warning |
| ROE | Trailing **17.8%** (MSCI: P/B ÷ trailing P/E); forward ~19.7% | Bottom-up 19.8% / 19.3%; Yahoo ROE book-weighted 19.7% (5 Nov) | Blocks (trailing): E 25.5%, F 15.2%, O 17.7%. "Normal" ~13% (1.8 ÷ 13.5) is a rule of thumb only: a point P/B over an average P/E `[E/A]` |
| Dividend yield, trailing | 4.54% | MSCI Norway, dividends paid over 12 months, 30 Oct `[F]` | |
| Dividend yield, forward | 4.89% (OBX weights); **4.44% without Frontline**; 4.72% on MSCI weights | Yahoo, latest declared dividend annualised, 5 Nov `[F]` | Frontline 22.4% is one strong quarter annualised. Subsea7 (94%) and Vår (86%) pay close to all trailing EPS |
| Model cash yield | Stub 5.6%; 5.1% in 2027 (Base, cash paid); window d 4.8% | Dividends at block payouts 0.58 / 0.65 / 0.49 plus energy's cash credit; no buybacks counted (no source) `[A]` | |
| Energy weight | 33–35% of cap | DNB OBX ETF 33.0%, NORW 32.9% (Yahoo look-through); 35% of the repriced sample `[F]` | **51% of CY26 and 44% of CY27 consensus earnings** (bottom-up) |
| Consensus EPS CY26 → CY27 | **−9.7%** (energy −21.5%, financials +9.8%, other −1.6%) | Yahoo `earningsTrend`, 6 Nov `[F]` | Equinor −21%, Vår −21%, Frontline −42%, Telenor −22%, Kongsberg +56% |
| Consensus CY27 revision since 11 Oct | **+2.5%** (energy +9.9%, financials +1.0%, other −4.9%) | Same weights, 6 Nov vs 11 Oct `[F]` | Below the 5% recalibration trigger |
| Forward E/P − Norway 10-year | 8.2% − 4.37% = **+3.9 pp** | Norges Bank `GOVT_GENERIC_RATES/B.10Y.GBON`, 4 Nov `[F]` | On normalised EPS ~+3.5 pp |

- **P/B and composition `[A]`:** Kongsberg (P/B 22.4, 8–11% of the index, a much smaller weight
  in the band years) adds ~0.21 to the sample's 2.27; Gjensidige (6.2) and Vår (9.2; Yahoo's book
  in USD, fixed) add more. Equinor's weight has fallen from about a third (2023) to 16–22%. On a
  mix like 2023's, Oslo is at ~2.0–2.1: the top of the band, not above it. The bottom-up P/B
  (2.27) is below MSCI's (2.46 at 30 Oct; ≈ 2.39 at 5 Nov) because Yahoo's book values already
  hold Q3 retention, and the weights differ; the two are not averaged. The band is a rule of thumb
  from three named analysts, not a measured distribution.

| Measure | World | Source / date | Reference |
|---|---|---|---|
| P/E trailing / forward | 22.29 / **17.38** (30 Oct); forward ≈ 16.95 at 5 Nov | MSCI World `[F]`; URTH −2.4% since 30 Oct | ~16.5–17 forward over 10 years `[A]`. Model: 16.4 on calendarised CY27 consensus |
| P/B | 4.06 (30 Oct); ≈ 3.96 at 5 Nov | MSCI World `[F]` | No long series in this baseline `[?]` |
| ROE | Trailing **18.2%** (P/B ÷ trailing P/E); forward 23.4% | Derived | About the same trailing ROE as Oslo (17.8%). World's higher P/B is a P/E (growth) premium, not a profitability premium |
| Dividend yield, trailing | 1.54% | MSCI World, 30 Oct `[F]` | URTH distribution yield 1.39% (Yahoo) |
| Dividend yield, forward | — | Not fetched `[?]` | |
| Model cash yield | Stub 2.3% a year; window d 2.8% (Base) | Payout 0.46 plus 0.03 retained cash credited (AI layers, energy). Implies ~1% net buybacks `[A]` | |
| S&P 500 forward P/E | **18.7** on 29 Oct (5-y avg 19.8, 10-y avg 19.1); ≈ 17.8 at 5 Nov; trailing 25.9 (10-y avg 23.7) | FactSet Earnings Insight, 30 Oct `[F]`; S&P 500 −4.7% since 29 Oct | Below both averages |
| S&P 500 EPS growth | CY26 **+32.9%**, CY27 **+16.3%** (revenue +9.6%); Q3-26 +30.2% blended (60% reported; 82% beat) | FactSet, 30 Oct `[E]` | "Magnificent 7" Q3 −14.7% vs estimates in aggregate (GAAP; Alphabet's equity-securities loss, Meta's litigation charge) |
| S&P 500 bottom-up target | 9,327.80, +20.8% from 7,720.39 (29 Oct) | FactSet, 30 Oct `[E]` | +26.8% from the 5 Nov close |
| Concentration | Top 10 = 26.6%; information technology 29.1% (URTH holdings, 4 Nov) | MSCI 30 Oct; iShares `[F]` | |
| Forward E/P − US 10-year | 5.90% − **4.90%** = **+1.0 pp** | MSCI forward scaled to 5 Nov; FRED `DGS10`, 4 Nov `[F]` | |
| US HY OAS | 3.32% | FRED `BAMLH0A0HYM2`, 4 Nov `[F]` | Bear signpost > 4.5% |

- **Reading:** Oslo is priced on cyclically high earnings, World on structurally high earnings
  expectations. Oslo's risk is earnings (oil, banks); World's risk is the multiple. At equal
  shocks (±10%) the multiple moves World's Base by ±3.3 pp and Oslo's by ±3.0 pp.

## Oil and NOK linkage

Monthly log returns from month-end closes (Yahoo daily, re-fetched 6 Nov), Mar 2013–Oct 2026 `[F]`;
derived. Windows end at the October month-end.

| Correlation (beta) | 13.6 years | 10 years | 5 years | 3 years |
|---|---|---|---|---|
| OSEBX ~ Brent (USD) | **0.58** (0.20) | **0.62** (0.21) | 0.40 (0.16) | 0.56 (0.17) |
| OSEBX ~ Brent (NOK) | 0.50 | 0.52 | 0.25 | 0.49 |
| OSEBX ~ World (USD) | 0.64 | 0.63 | 0.40 | −0.09 |
| OSEBX ~ World (NOK) | **0.32** (0.37) | 0.29 (0.34) | 0.03 (0.03) | −0.33 (−0.30) |
| **NOK (I-44) ~ Brent** | **0.55** (0.116) | **0.54** (0.113) | 0.43 (0.113) | **0.44** (0.087) |
| NOK (I-44) ~ World (USD) | 0.51 | 0.54 | 0.45 | 0.25 |
| NOK/USD ~ Brent | **0.51** (0.148) | 0.48 (0.138) | 0.32 (0.111) | **0.26** (0.075) |
| NOK/EUR ~ Brent | 0.59 (0.128) | 0.61 (0.129) | 0.47 (0.120) | 0.49 (0.103) |
| NOK/USD ~ World (USD) | **0.61** | 0.64 | 0.58 | 0.36 |
| World (USD) ~ Brent | 0.34 | 0.35 | −0.10 | −0.19 |

| Regression | 13.6 years | 10 years | 5 years | 3 years |
|---|---|---|---|---|
| OSEBX = b1·World(USD) + b2·Brent (R²) | 0.47 / 0.14 (0.55) | 0.44 / 0.16 (0.58) | 0.39 / 0.17 (0.35) | 0.02 / 0.18 (0.31) |
| NOK/USD = b1·World(USD) + b2·Brent (R²) | 0.39 / 0.099 (0.47) | 0.42 / 0.085 (0.49) | 0.49 / 0.133 (0.48) | 0.41 / 0.099 (0.24) |
| NOK (I-44) = b1·World(USD) + b2·Brent (R²) | 0.21 / 0.090 (0.42) | 0.23 / 0.084 (0.44) | 0.29 / 0.125 (0.42) | 0.22 / 0.101 (0.31) |

- NOK strength = −Δlog(I-44); I-44 from Norges Bank daily fixings (month-end). With Brent from
  Aug 2007 the I-44 ~ Brent correlation is **0.54** (230 months).
- **Data note `[?]`:** the short windows are source-sensitive. Yahoo's `BZ=F` futures front month
  and FRED's Dated Brent (`DCOILBRENTEU`, month-end) diverged by up to $25 in 2026 (March
  month-end 101 against 127). On Dated Brent, Oct-23–Oct-26 gives I-44 ~ Brent 0.19 and
  NOK/USD ~ Brent −0.02; on the futures (Sep-23–Sep-26) 0.44 and 0.22. The 10- and 13-year values
  differ by 0.01–0.04 only. The reading below holds on either series.

| Volatility, ann. (13.6 y) | OSEBX 13.2% | World USD 14.0% | **World NOK 11.4%** | Brent 38.4% | USD/NOK 11.2% | I-44 8.1% |
|---|---|---|---|---|---|---|

Rolling 36-month correlation (at September; the last column ends in October 2026):

| Year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | Oct-26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OSEBX ~ Brent | 0.42 | 0.49 | 0.50 | 0.71 | 0.78 | 0.79 | 0.64 | 0.43 | 0.15 | 0.32 | 0.56 | 0.56 |
| **NOK (I-44) ~ Brent** | 0.63 | 0.66 | 0.37 | 0.44 | 0.75 | 0.73 | 0.62 | 0.40 | 0.36 | 0.35 | 0.44 | 0.44 |
| NOK/USD ~ Brent | 0.67 | 0.62 | 0.22 | 0.31 | 0.70 | 0.74 | 0.66 | 0.48 | 0.28 | 0.08 | 0.26 | 0.26 |
| NOK/EUR ~ Brent | 0.57 | 0.63 | 0.40 | 0.45 | 0.79 | 0.81 | 0.72 | 0.48 | 0.37 | 0.39 | 0.48 | 0.49 |
| OSEBX ~ World (NOK) | 0.48 | 0.43 | 0.54 | 0.52 | 0.66 | 0.66 | 0.62 | 0.42 | 0.33 | 0.11 | −0.31 | −0.33 |

Episodes (month-end to month-end, %):

| Episode | OSEBX | Brent | USD/NOK | I-44 (+ = weaker NOK) | World USD | World NOK |
|---|---|---|---|---|---|---|
| GFC, Jul → Dec-08 | — | −63.3 | +36.2 | +18.3 | — | — |
| Oil crash, Jun-14 → Jan-16 | −9.2 | −69.1 | +40.5 | +14.5 | −7.5 | +30.0 |
| Q4-18 sell-off, Sep → Dec-18 | −14.8 | −36.7 | +6.9 | +5.5 | −13.3 | −7.3 |
| Covid, Dec-19 → Mar-20 | −24.1 | −62.5 | +18.1 | +13.8 | −21.1 | −6.8 |
| Rates shock, May → Sep-22 | −14.3 | −24.4 | +14.2 | +5.3 | −14.5 | −2.4 |
| 2026 to date, Dec-25 → Oct-26 | +27.1 | +93.3 | −8.0 | −11.0 | +10.9 | +2.0 |

USD/NOK in this table is Yahoo (as in the model; GFC row from Norges Bank fixings); I-44 is the
Norges Bank fixing `[F]`. Brent is the Yahoo front month (see the data note). The October
month-end Brent (117.64) is the expiring Z26 contract.

Annual total returns (%; 2026 to 30 Oct):

| Year | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OSEBX | 5.0 | 5.9 | 12.1 | 19.1 | −1.8 | 16.5 | 4.6 | 23.4 | −1.0 | 9.9 | 9.1 | 18.4 | 27.1 |
| World NOK | 27.5 | 17.7 | 4.9 | 18.1 | −3.5 | 29.7 | 12.0 | 26.2 | −7.9 | 27.7 | 32.0 | 7.7 | 2.0 |
| Brent (price) | −48.3 | −35.0 | 50.6 | 18.7 | −19.2 | 22.7 | −21.5 | 50.2 | 10.5 | −10.3 | −3.1 | −18.5 | 93.3 |

CAGR Mar-13 → Oct-26: OSEBX 11.8%, World NOK 15.2% (World USD 11.4%, USD/NOK +3.4% a year)
`[F]`. Max drawdown OSEBX: −24.6% month-end, −32.8% daily (23 Mar 2020) `[F]`. Since 30 Oct:
OSEBX −3.0%, URTH −2.4% in USD (−1.9% in NOK).

**User input assessed** (`[A]`; 11 Oct statements, checked on the current data):

| User statement | Check | Reading |
|---|---|---|
| Oslo correlates with the oil price (many oil companies) | Monthly correlation 0.40–0.62 across windows; beta 0.16–0.21; Brent explains about a third of OSEBX's monthly variance; 44–51% of index earnings are energy | **Correct, and the earnings link is stronger than the price correlation.** The 3-year return moves ~3.4 pp a year per $10/bbl on the Brent path. But global equities still move OSEBX more than Brent over 10+ years (b1 0.4–0.5 vs b2 0.14–0.17); over 3 years the World link has gone (b1 0.02) |
| The NOK correlates with oil, for the same reason and through tax income from oil companies | Trade-weighted (**I-44**): 0.54–0.55 since 2007 and over 10–13.6 years, **0.43–0.44 over 3–5 years** on futures (0.19 over 3 years on Dated Brent). Against USD 0.26 (3 y; −0.02 on Dated), against EUR 0.49. I-44 ~ World 0.25–0.54: across windows global risk explains about as much of the NOK as oil does (b1 0.21–0.29 on World vs b2 0.08–0.13 on Brent, which is ~2.7 times as volatile). 2026: Brent +93% Dec–Oct, I-44 −11.0% (NOK stronger) | **Correct in the long run, weaker now, most clearly against USD.** The tax channel is largely sterilised by design: petroleum revenue saved in the GPFG is converted to foreign currency. Norges Bank buys FX for the government worth **NOK 300m a day in Nov 2026** (net NOK 176m after transfers; also 300m in Sep and Oct) `[F]`, and the state's direct cash flow (SDFI) never enters NOK. What is left works through activity, Norges Bank's rate path and terms of trade |

**What follows for a NOK investor `[A]`:**
- The NOK weakens in risk-off, so **global equities held unhedged lose less in NOK** (World NOK
  volatility 11.4% vs 14.0% in USD; Covid −6.8% vs −21.1%; 2022 −2.4% vs −14.5%). Unhedged is the
  natural choice for a NOK investor; hedging adds ~0.9 pp a year of carry but removes the cushion.
  In 2026 the cushion ran the other way: the NOK firmed 8% against USD, so World returned +10.9% in
  USD but +2.0% in NOK to October.
- OSEBX vs World in NOK correlates only 0.29–0.32 over 10+ years (negative in the last 3): the
  two are good diversifiers. Oslo adds the same oil and Norway risk that the Nordic HY market
  carries through its oil service, E&P and shipping issuers (`docs/hy-market-bbb.md`).

### NOK level and flows (Norges Bank API)

| Measure | Value | Source / date |
|---|---|---|
| I-44 now | **107.76** (5 Nov); 106.66 (30 Oct) | `EXR/B.I44.NOK.SP` `[F]` |
| I-44 annual average | 2012 87.0 · 2016 105.4 · 2020 115.0 · 2022 110.0 · 2023 119.4 · 2024 120.3 · 2025 119.6 · 2026 YTD 112.7 | `EXR/M` `[F]` |
| Average / range since 1990 | 101.1 / 85.0–123.3; today weaker than 81% of months | derived |
| Average since 2016 | 111.6 (range 101.5–123.3); today stronger than 65% of months | derived |
| Norges Bank MPR 3/26 projection | 110.0 flat, Q4-26 to 2029; spot 2.0% stronger | MPR dataset Data D/E `[E]` |
| Norges Bank FX for the GPFG (NOK m per day; buy = Norges Bank sells NOK) | 2025: buy 50–400 (Jan–Jun), sell 150 (Jul–Oct), buy 150 (Nov–Dec) · **2026: sell 650 / 600 / 600 (Jan–Mar), sell 50–400 (Apr–Aug), buy 300 (Sep, Oct, Nov)** | `ANN_FX_SPU` `[F]` |
| Financial Conditions Index (positive = tighter) | **−1.65** (29 Oct); stock-market part −0.30; mean +0.5 since 2007; 2008 +7, Mar 2020 +4 | `FINANCIAL_INDICATORS/D.FCI_TOTAL` `[F]` |

- **Reading `[A]`:** the NOK is on the strong side of its last ten years; Norges Bank noted the
  krone is "stronger than assumed" (5 Nov) but made no new projection, so Base follows spot while
  the gap to 110.0 is inside 3%. The government's FX flow worked *for* the NOK in Jan–Aug 2026 and
  against it from September (Norges Bank buying FX worth NOK 300m a day as petroleum tax rises
  with the oil price); the November amount equals October's, so the flow did not grow with
  October's higher oil price. Financial conditions are loose (FCI −1.65, below its average): no
  stress signal for equities or HY; a move above +2 would be an early Bear signpost.

## Oslo build

- **Sample:** 14 largest names, 79.9% of the DNB OBX ETF weight. OBX ETF top 10 (Yahoo
  look-through of 9 Oct): EQNR 16.1, DNB 10.4, KOG 7.3, NHY 6.7, AKRBP 6.2, MOWI 5.1, STB 4.9, TEL
  4.7, SUBC 4.3, YAR 4.2 `[F]`; ORK 3.5, GJF 2.5, FRO 2.5, VAR 1.5 `[A]`, from market cap × free
  float. Repriced to 5 Nov by each name's price move since 9 Oct (the look-through has not been
  refreshed; repriced weights in the Appendix) `[A]`. Prices 5 Nov; consensus Yahoo 6 Nov (4–19
  analysts per name). P/B, ROE and payout at the 5 Nov close.

| Block | Weight in sample | P/E CY26 | P/E CY27 | Consensus EPS CY27 vs CY26 | Share of CY27 earnings | Forward dividend yield (5 Nov) | Dividend run rate ÷ trailing EPS (5 Nov) | P/B / ROE trailing (5 Nov) |
|---|---|---|---|---|---|---|---|---|
| E — Oil-linked (EQNR, AKRBP, VAR, SUBC, FRO) | 35% | 7.5 | 9.5 | −21.5% | **44%** | 6.5% | 58% | 2.29 / 25.5% |
| F — Rates and credit (DNB, STB, GJF) | 24% | 14.1 | 12.8 | +9.8% | 22% | 4.5% | 65% | 2.21 / 15.2% |
| O — Other (KOG, NHY, MOWI, TEL, YAR, ORK) | 41% | 13.9 | 14.2 | −1.6% | 34% | 3.8% | 49% | 2.30 / 17.7% |
| **Index (sample)** | 100% | **10.7** | **11.8** | **−9.7%** | 100% | **4.9%** | **56%** | **2.27 / 19.8%** |

- **B_cons (Brent the consensus implies for 2027) ≈ $80** `[A]`.
  - Equinor's consensus EPS falls 20.7% from 2026 (5.87 → 4.65 USD), against a Brent 2026
    average of ≈ $93.0 (Q1–Q3 79.1 / 96.5 / 92.0 from Yahoo daily, Q4 the oil BBB stub 104.3):
    (80 − 30) / (93 − 30) = 0.79. Aker BP gives 80.7, Vår 79.7.
  - The oil Base for 2027 ($88) is above it, so Base 2027 energy earnings are 16% above consensus.
  - Energy consensus rose 9.9% since 11 Oct (Equinor +5%, Aker BP +14%, Vår +25%, Frontline +42%),
    with the 2027 strip at 90–94 in late October. The energy EPS per Brent dollar is anchored on
    CY26 consensus and the CY26 Brent average, so it moves little with consensus.
- **Block paths** (EPS, block consensus CY27 = 1.00, before FX; values in the Interface). In NOK
  the USD/NOK path applies to all of E and the I-44 path to the foreign half of O. Basis: E =
  (Brent − 30) / 50 on the oil paths (Bear 65 / 60 / 60 / 60; Base and Bull 88 / 77 / 72 /
  mid-cycle 70). F: NIBOR 4.79 → 3.86 → mid-cycle 3.45 compresses margins; Bear losses peak in
  2028 with HY defaults `[A]`. O: Base 3% Year-1 haircut, then ~4.5% nominal growth; half the block
  in foreign currency `[A]`.
- **Exit P/E 11.5 (Base mid-cycle)** `[A]`: forward P/E averages ~11–12 for Oslo (10-year
  trailing ~13.5 `[E]`), a little below today's 11.8 on CY27. Bear 10.5, Bull 12.5. The exit P/B
  (1.74; Bear 1.48, Bull 1.95) is inside the OSEBX band (table under "Return split").
- **Cash and payout (one rule with World):**
  - Payout per block = latest declared dividend annualised ÷ trailing EPS `[F]`: **E 0.58, F 0.65,
    O 0.49** (0.565 weighted on CY27 earnings shares). Trailing EPS holds Q3: Equinor's trailing
    P/E is 8.6, Hydro's 10.4, Telenor's 8.2 (a gain in its trailing EPS). Cross-checks: on
    dividends actually paid (Yahoo payout ratio) 0.50 / 0.64 / 0.48; on the run rate ÷ CY27
    consensus 0.62 / 0.57 / 0.54; without Frontline E is 0.48, without Telenor O 0.46. The rule's
    figures are used.
  - Energy has a cash conversion of 0.80, as World energy, so (0.80 − 0.58) × energy EPS is
    credited to V_t: 2.4% of the price by 2029. Energy's total cash is 0.80 either way; the split
    moves only timing. F and O are valued as P/E × EPS; their retention funds their growth. No
    buybacks are counted (no source) `[A]`. Stub cash yield 5.6% ≈ 0.66 × CY27 E/P 8.5% `[A]`.
- **Payout consistency (both directions):** retaining ~36% (after energy's credit) at ROE 15–21%
  would fund 5–7% growth; the Base EPS falls 2.3% a year instead (the normalisation): ROE goes
  from 21.0% (2027) to 14.7% (2030). The long-run growth of 3.3% implies ~9% on retained earnings
  (field decline, dilution), below k, consistent with the exit P/B inside the band.

## World build

**Blocks at the 5 Nov close** (MSCI World weights from the URTH holdings of 4 Nov, repriced to
5 Nov; CY27 consensus calendarised as in the AI BBB Update 6 of 1 Nov) `[F/A]`:

| Block | Names | Share of value | P/E on CY27 | Share of CY27 earnings | Path source |
|---|---|---|---|---|---|
| Company blocks | Microsoft, Alphabet (A+C), NVIDIA, Amazon, Micron | 16.2% | 14.4 (MSFT 24.3, GOOGL 19.0, NVDA 11.9, AMZN 24.4, MU 3.4) | 18.5% | `docs/msft-analysis.md` v3, `docs/googl-analysis.md` v2, `docs/nvda-analysis.md` v1.2, `docs/amzn-analysis.md` v2, `docs/mu-analysis.md` v3 (V_t, D_t, EPS per scenario) |
| AI layer blocks | E rest (Meta, Oracle), H1 (AMD, Broadcom, Marvell), H3 (ASML, Applied, Lam), H4 (Arista, Vertiv, Eaton), T (8 software names) | 7.1% | 18.7 (E 16.7, H1 17.4, H3 19.2, H4 23.4, T 23.0) | 6.3% | `docs/ai-market-bbb.md` layer paths, exit P/E, payout, cash conversion (E rest on the "E rest" row) |
| Energy | MSCI World energy weight (4.15% on 4 Nov) | 4.2% | 14.2 | 4.9% | Oil BBB (Brent − 30) / 49 on the 9 Oct consensus basis; payout 0.58 (as Oslo energy); cash conversion 0.80 |
| **Rest** | everything else | **72.4%** | **16.9** | **70.4%** | Explicit path (below) `[A]` |
| **World** | | 100% | **16.4** | 100% | Sum |

- **Company blocks:** the skill takes company blocks from every name with its own IAF analysis;
  the AI BBB keeps the E rest row for Meta and Oracle only, and H2 has no name left in World.
  - Block inputs: Microsoft v3 (Base EPS 2027 20.77, V_T 692.1), Alphabet v2 (its re-mark at the
    30 Oct close: Base EPS 2027 12.66, V_T 371.1), NVIDIA v1.2 (5 Nov close: V_t 220.8 / 253.3 /
    274.1), Amazon v2 (Base EPS 9.69, V_T 317.3; no dividend), Micron v3 (5 Nov close; D_t 158.4 /
    77.7 / 45.8, V_T 723.6).
  - Interim V_t of Base and Bull are re-glided to the 5 Nov price with the analyses' own rule (core
    P/E glides linearly from today's to the exit P/E; Bear at its exit P/E from end-2027):
    Microsoft $535.93, Alphabet $282.57, Amazon $260.21. NVIDIA and Micron are already at the
    5 Nov close. V_T, D_t and EPS are the analyses' figures.
- **AI layer blocks:** AI BBB paths; E-layer cash conversion Base −.20 / .00 / .20, Bear −.10 /
  .30 / .50, Bull −.30 / −.20 / .00. The E-layer Base 2027 (.92) comes from Microsoft's and
  Alphabet's own EPS, which the company blocks carry, so it is not stacked on the E rest row.
- **Rest paths** `[A]`: Base = CY27 consensus less 3% (Year-1 analyst optimism), then 5.5% a
  year (nominal trend). Bear = recession 0.83 / 0.87 / 0.95 / 1.02 (the HY Bear; −17% vs
  consensus in 2027, recovered by 2030). Bull = 1.00 / 1.07 / 1.14 / 1.21. Rest P/E (paths in the
  Interface) and payout (~0.48–0.50) are the 11 Oct World view without its AI and energy part.
  The rest's CY27 earnings are the 18 Oct figure carried into today's value units, raised 0.6%
  (FactSet S&P 500 CY27 EPS revision 9 → 30 Oct, as the proxy; CY26 +32.9%, CY27 +16.3%) `[A]`.
- **Retained cash and payout (one rule with Oslo):** blocks with a cash conversion (AI layers,
  energy) credit (conversion − payout) × EPS to V_t at face value and get no extra growth for it:
  0.49 index points by 2029 in Base, 2.7% of window earnings. The company analyses carry their own
  net cash in V_t. The rest is valued as P/E × EPS, so its retention (~51%) funds its 5.5% growth.
  Energy's payout follows Oslo's (0.58, conversion 0.80).
- **Currency:** 70% of World on USD/NOK, 30% on I-44 `[A]` (USD earnings on USD/NOK, other foreign
  earnings on I-44; Oslo the same rule).
- **Market check:** FactSet's bottom-up 12-month S&P 500 target (30 Oct) is 9,327.80, **+26.8%**
  from the 5 Nov close `[E]`; the Bull 2027 in USD is +19.0%. The S&P 500's CY27 consensus
  growth (+16.3%) is mostly AI; the split puts that growth through the AI BBB paths and the
  company analyses instead of the index average.

## Return split, structural run, P/B–ROE check and sensitivities

| Window, % a year | Oslo Bear / Base / Bull | World NOK Bear / Base / Bull |
|---|---|---|
| IRR_T | −4.2 / **2.6** / 6.3 | −0.8 / **6.6** / 11.9 |
| d (cash yield) | 3.9 / **4.8** / 4.8 | 2.5 / **2.8** / 2.9 |
| g (value growth, P → V_T) | −8.4 / **−2.3** / 1.4 | −3.4 / **3.9** / 9.2 |
| — normalised EPS growth (from CY27 consensus) | −5.5 / **−2.3** / −1.1 (NOK) | −2.9 / **2.7** / 5.9 (USD) |
| — re-rating | −3.7 / **−0.9** / 1.8 (P/E 11.8 → 10.5 / 11.5 / 12.5) | −2.9 / **+1.2** / 3.9 (value multiple 16.4 → 15.0 / 17.0 / 18.6) |
| — retained cash credited | 0.7 / **0.8** / 0.7 | inside the value multiple |
| — FX | inside EPS | 2.5 / **0.0** / −0.9 |
| c (timing) | 0.3 / **0.2** / 0.1 | 0.1 / **0.0** / −0.1 |
| ΣD / V_T (P = 100) | 12.3 / 75.9 · **15.0 / 92.9** · 15.2 / 104.5 | 7.8 / 89.8 · **8.8 / 112.7** · 9.1 / 131.8 |
| Structural IRR (EPS at the normalised level from 2027) | −4.1 / **2.2** / 6.0 | exempt: the blocks carry their own cyclical paths |
| Cyclical (IRR − structural, pp) | −0.1 / **+0.5** / +0.4 | — |

- Oslo's d (4.8%) and its retained cash (0.8) reflect energy paying 0.58 and crediting 0.22.
- World's Base re-rating is positive: the index starts at 16.4 on CY27, below the 17.0 exit. Part
  of it is Micron's P/E rising as its EPS falls (not a market re-rating) and the blocks' retained
  cash.

**P/B against ROE** (book_T = book now + Σ (EPS − cash paid); exit P/B = V_T ÷ book_T) `[A]`:

| Base (Bear / Bull) | Oslo | World |
|---|---|---|
| P/B at 5 Nov | 2.39 (MSCI 2.46 × OSEBX move since 30 Oct) | 3.96 (MSCI 4.06 × URTH move since 30 Oct) |
| ROE trailing / forward | 17.8% / ~19.7% (bottom-up 19.8% / 19.3%) | 18.2% / 23.4% |
| ROE 2027 / 2028 / 2029 (on opening book) | 21.0 / 17.7 / 16.0% | 22.9 / 21.1 / 19.7% |
| ROE 2030 (normalised) | **14.7%** (13.8 / 15.2) | **18.6%** (16.5 / 20.1) |
| Exit P/E (World: value multiple) | 11.5 (10.5 / 12.5) | 17.0 (15.0 / 18.6) |
| **Exit P/B** | **1.74** (1.48 / 1.95) | **3.17** (2.47 / 3.74) |
| Reading | Inside the OSEBX band 1.5–2.1: the exit P/E 11.5 is consistent with ROE normalising to ~15% | 3.2 assumes World keeps an ROE of ~18–19%; there is no P/B history in this baseline to test it `[?]` |

World takes CY26 EPS as CY27 ÷ 1.13 for the stub `[A]`; the exit P/B moves < 0.05 with it. Oslo
takes CY26 as CY27 ÷ (1 − 0.097), the sample's consensus step.

**Sensitivities (Base window IRR, %; the same shocks for both indices):**

| Shock | Oslo | World NOK |
|---|---|---|
| Base | 2.6 | 6.6 |
| All multiples −10% / +10% | −0.5 / 5.6 | 3.3 / 9.8 |
| All multiples −1 / +1 point | 0.0 / 5.1 | 5.0 / 8.2 |
| NOK 10% weaker / stronger by end-2029 (USD/NOK and I-44) | 4.6 / 0.7 | 10.0 / 3.1 |
| Brent path −$10 / +$10 (Base, every year and mid-cycle) | −0.8 / 5.9 | 6.4 / 6.9 |
| Energy cash conversion = payout / 1.0 | 1.9 / 3.4 | 6.6 / 6.7 |
| Rest growth 4.5% / 6.5% | — | 6.0 / 7.3 |
| Rest CY27 revision 0% / −3% (instead of +0.6%) | — | 6.5 / 5.8 |
| Payout per block 0.76 / 0.63 / 0.56 (pre-Q3 trailing EPS) | 2.9 | 6.7 |
| Amazon on the AI BBB E rest row and Micron on H2 (no company blocks for them) | — | 6.5 |

- **Oslo's low Base is the normalisation:** today's price capitalises earnings that the oil
  baseline expects to fall (energy −31% from 2027 Base to the 2030 normalised level), on a P/E
  (11.8 on CY27) above its mid-cycle 11.5. Its energy cash conversion (0.80) matters: at the
  rule's 0.58 payout it moves Base by −0.8 / +0.7 pp between "conversion = payout" and 1.0.
- **World's Base is mostly the rest and the lower price:** AI and company earnings add little
  after 2027 in Base (0.92 → 1.00 of their CY27 consensus). For World the NOK is the largest
  single sensitivity (±3.4 pp for ±10% by 2029), about as large as the multiple (±3.3 pp); for
  Oslo it is ±2.0 pp, through energy and the O block's foreign half.

## Against high yield

| Base window, NOK, before tax | Return | E (pp) | R (pp) | E / R | Bear 2027 |
|---|---|---|---|---|---|
| Nordic HY market (after 0.6% typical fee; HY BBB 5 Nov) | 6.6 | 2.15 | 8.47 | **0.254** | −1.0 |
| Oslo (OSEBX, after 0.20% fee) | 2.4 | −1.92 | 29.9 | −0.06 | −28.0 |
| World NOK unhedged (after 0.20% fee) | 6.4 | 2.08 | 25.9 | 0.080 | −18.5 |
| World NOK hedged (approx.) | ~7.3 | ~3.0 | ~34 | ~0.09 | ~−25.5 |

- **Reading `[A]`:**
  - On the 3-year window and the one-year stress, HY wins clearly. With Nordic spreads at 490 bp
    (end-Oct) HY pays 0.254 per unit of stress against World's 0.080. World unhedged is within
    1.6% of its pre-alert: below ~1,827 (URTH in NOK) its Base equals the HY market's 7.2% before
    fees, but its stress (R ~26 pp) is about 3 times HY's, so E / R is only ~0.10 there.
  - **Tax (general, taxable accounts):** equity is taxed 37.84% on returns above the
    skjermingsrente, HY interest at 22% (formula in the skill). Tax does not change this baseline.
  - **Long horizons:** on mid-cycle returns equities beat HY (Oslo 8.9%, World 8.2% against the HY
    market's 6.3% before fees); Oslo's lead is its cash yield, and both assume ~9–10% on retained
    earnings. The Bear window is −0.8% a year for World in NOK and −4.2% for Oslo (HY 6.0%). The
    entry price decides the first three years; the horizon decides whether a one-year drawdown
    matters. The allocation is not set here.
  - **The HY trigger and the equity trigger together:** if Nordic spreads tighten and the HY
    reference falls to 0.196, the equity triggers move up to −9.4% (World, URTH in NOK ≈ 1,682;
    fwd P/E 15.4) and −22.6% (Oslo ≈ 1,610; fwd P/E 9.4); at 0.17 to −7.2% (≈ 1,722) and −20.2%
    (≈ 1,661). For World to qualify at today's price on HY alone, the HY reference would have to
    fall to 0.080: HY's excess after fees ~0.7 pp over NIBOR (2.15 pp now). In practice the switch
    comes from equity prices falling, or from equity falling while HY spreads tighten.

## Signposts and monitoring

| Signpost | Threshold (Bear / Bull) | Now | Direction |
|---|---|---|---|
| OSEBX level (trigger) | ≤ 1,492 (trigger 1) / ≥ 2,250 | 2,080.59 (5 Nov); 2,144.97 (30 Oct) | down |
| MSCI Norway P/BV | < 1.9 (de-rating under way) / > 2.5 (**valuation warning**, not Bull) | 2.46 (30 Oct); ≈ 2.39 (5 Nov); bottom-up 2.27 | up to the edge of the warning at month-end |
| MSCI World forward P/E | < 15.5 / > 19.5 | 17.38 (30 Oct); ≈ 16.95 (5 Nov) | down |
| URTH in NOK (World trigger) | ≤ 1,590 (trigger 1); pre-alert 1,827 / ≥ 2,200 | 1,855 (5 Nov) | down; 1.6% above the pre-alert |
| S&P 500 CY27 EPS growth consensus | < +8% / ≥ +15% held | +16.3% (FactSet 30 Oct) | firmer |
| Oslo CY27 consensus EPS (Equinor CY27) | −10% / +10% vs this run | $4.65 (19 analysts); sample +2.5% since 11 Oct | up (energy +9.9%, other −4.9%) |
| Brent Dec-27 contract | < $70 / > $95 | 84.88 (3 Nov settlement, oil BBB) | down |
| US HY OAS | > 4.5% / < 3.0% | 3.32% (4 Nov) | slightly wider (3.44% on 30 Oct) |
| US 10-year vs World forward E/P | gap < 0 / > 1.5 pp | +1.0 pp (5.90% − 4.90%) | wider |
| USD/NOK | > 10.5 / < 9.2 | 9.29 (5 Nov) | NOK firmer; close to the Bull level |
| I-44 (Norges Bank) | > 117 / < 107 | 107.76 (5 Nov) | NOK firmer; **Bull level touched** on 30 Oct (106.66) and 3 Nov (106.65), not held |
| Norges Bank FCI | > +2 / < −2.5 | −1.65 (29 Oct) | slightly looser |
| Nordic HY spread | > 550 bp / < 400 bp | 490 bp (end-Oct, HY BBB) | wider |
| AI + companies EPS vs the AI BBB Base (World block) | < 0.85 / > 1.05 of CY27 by 2028 | AI BBB and company Base 0.94 (2028) | — |
| Rest-of-World CY27 consensus revisions | −5% / +5% vs this run | +0.6% (S&P 500 proxy, 9 → 30 Oct) | slightly up |

- **Crossed?** No signpost is crossed and held. The I-44 Bull level was touched twice and the
  NOK is back at 107.8; it is read as touched, not as a Bull signal for the scenario weights.
  MSCI Norway's P/BV reached 2.46 at the October month-end, close to the 2.5 warning.
- **Recalibration triggers checked:** no index moved > 10% within a month (OSEBX −3.0%, URTH −2.4%
  since 30 Oct); consensus revisions +2.5% (Oslo) and +0.6% (S&P 500), below 5%; MSCI World
  forward P/E 16.95 inside 15.5–19.5; MSCI Norway P/BV 2.46 inside 1.9–2.5; USD/NOK −2.7% since
  9 Oct (limit 7% within a month).

**Before the next update:** oil BBB follow-up (7 Nov); SSB CPI (10 Nov); Fondsfinans HY October
report (~10 Nov, DNB Carnegie's October spread); NVIDIA Q3 FY27 (17 Nov) and the AI BBB after it;
SSB Q3 national accounts (26 Nov); OPEC+ (29 Nov); MSCI November month-end fundamentals (30 Nov);
US FY27 stopgap (11 Dec); Micron FQ1-27 (16 Dec); Norges Bank MPR 4/26 (17 Dec; new I-44
projection); the new US Congress (3 Jan 2027).

## Change log

- **13 Nov 2026 — compacted to the lean-document rules (1,069 → 775 lines, Interface section
  first); no value changed.**
- **6 Nov 2026 — Update 2 (full update, Step 0–8; skill 2026-10-24.1; 5 Nov close).** World Base
  window 5.2 → 6.6% (mostly price), Oslo 2.5 → 2.6% (re-mark); triggers moved with the HY
  reference 0.196 → 0.254; Oslo payouts re-set on post-Q3 EPS; Amazon and Micron became company
  blocks. Scenarios, P/E and rest paths and NOK relative moves kept.
- **24 Oct 2026 — source of the HY reference** (skill 2026-10-24.1): read from
  `docs/hy-market-bbb.md` instead of the HY fund analysis; no number changed.

## Appendix: raw values and sources

### Prints (Yahoo, close 5 Nov 2026 unless stated) `[F]`

| Item | Value |
|---|---|
| OSEBX.OL / OBX.OL / URTH / ACWI / ^GSPC / IXC | 2,080.59 / 1,994.48 / 199.63 / 152.43 / 7,353.73 / 57.27 |
| Month-end 30 Oct: OSEBX / URTH / ^GSPC / IXC | 2,144.97 / 204.64 / 7,580.07 / 64.19 |
| BZ=F (front F27) | 98.29 (5 Nov); 99.76 (6 Nov, intraday); 117.64 (30 Oct, expiring Z26) |
| NOK=X / EURNOK=X / EURUSD=X (5 Nov) | 9.2944 / 10.442 / 1.1235 (30 Oct: 9.2459 / 10.3393 / 1.1183) |
| Norges Bank fixings 5 Nov | USD/NOK 9.2984 · EUR/NOK 10.4365 · I-44 107.76 · TWI 119.46 (30 Oct: I-44 106.66) |
| FRED (4 Nov) | DGS10 4.90% · BAMLH0A0HYM2 3.32% (3.44% on 30 Oct) |
| Norges Bank (4 Nov / 29 Oct) | 10-year 4.367% · FCI −1.65 (stock part −0.30) |
| Company names (USD) | MSFT 535.93 · GOOGL 282.57 · GOOG 281.74 · NVDA 181.60 · AMZN 260.21 · MU 656.39 |
| AI layer names (USD; SAP in EUR) | META 605.08 · ORCL 115.16 · AMD 404.40 · AVGO 291.53 · MRVL 133.55 · ASML 1,356.65 (ADR) · AMAT 319.25 · LRCX 185.20 · ANET 159.16 · VRT 176.73 · ETN 327.02 · NOW 102.36 · CRM 222.41 · ADBE 246.44 · PLTR 154.99 · SAP 215.75 EUR · INTU 354.84 · SNOW 269.54 · DDOG 174.60 |

**URTH holdings, 4 Nov 2026** (iShares CSV; 1,250 equity rows, weights summing to 99.92%,
normalised; matched on ticker and country) `[F]`: NVDA 5.06 · MSFT 4.31 · AMZN 2.83 · GOOGL 1.86 ·
AVGO 1.62 · META 1.52 · GOOG 1.47 · MU 0.99 · AMD 0.88 · ASML 0.64 · PLTR 0.41 · AMAT 0.32 · LRCX
0.30 · SAP 0.27 · ORCL 0.24 · ANET 0.21 · CRM 0.20 · MRVL 0.15 · ETN 0.15 · NOW 0.12 · ADBE 0.11 ·
INTU 0.11 · SNOW 0.10 · VRT 0.08 · DDOG 0.07. Energy 4.15%; information technology 29.06%; top 10
26.77% (Apple 5.64, Lilly 1.25 and Tesla 1.21 sit in the rest). Repriced to 5 Nov by each name's
move against URTH's (−3.96% on the day).

CY27 EPS of the layer names: AI BBB Update 6 (1 Nov, calendarised; ASML in USD, SAP EUR 8.48).
Company consensus CY27: Microsoft 22.08, Alphabet 14.84, NVIDIA 15.21, Amazon 10.65, Micron 191.80.

### Bottom-up valuation of the Oslo sample (Yahoo quoteSummary, close 5 Nov 2026) `[F]`

| Name | OBX wt % (repriced) | P/B | P/E trailing / fwd | ROE (Yahoo) | Fwd div. yield (latest declared, annualised) | Payout ratio, trailing (Yahoo) |
|---|---|---|---|---|---|---|
| Equinor | 15.5 | 2.29 | 8.6 / 9.3 | 27.6% | 3.58% | 31% |
| DNB | 11.1 | 1.80 | 12.2 / 11.5 | 14.4% | 5.51% | 66% |
| Kongsberg | 8.3 | **22.44** | 49.5 / 29.7 | 32.7% | 0.65% | 33% |
| Norsk Hydro | 5.8 | 1.27 | 10.4 / 9.1 | 12.0% | 4.36% | 46% |
| Aker BP | 5.5 | 1.76 | 8.8 / 10.1 | 17.7% | 7.70% | 77% |
| Mowi | 5.4 | 2.50 | 14.4 / 14.5 | 16.9% | 3.46% | 49% |
| Storebrand | 5.2 | 2.59 | 19.4 / 15.0 | 13.7% | 2.67% | 52% |
| Telenor | 5.1 | 2.61 | 8.2 / 14.8 | 32.9% | 7.11% | 57% |
| Subsea7 | 3.9 | 2.26 | 14.8 / 12.3 | 14.2% | 6.27% | **94%** |
| Yara | 4.0 | 1.17 | 7.7 / 9.9 | 15.9% | 5.49% | 40% |
| Orkla | 3.8 | 2.37 | 15.8 / 14.9 | 15.1% | 3.93% | 61% |
| Gjensidige | 2.7 | 6.17 | 20.6 / 16.0 | 27.2% | 3.58% | 72% |
| Frontline | 2.0 | 3.34 | 6.5 / 6.5 | 53.9% | **22.44%** | 47% |
| Vår Energi | 1.4 | 9.24 (Yahoo 85.9: book in USD) | 8.6 / 8.9 | 112% | 10.80% | 86% |

| Weighting | P/B | P/E trailing / fwd | ROE trailing / fwd | Fwd div. yield | Dividend run rate ÷ trailing EPS |
|---|---|---|---|---|---|
| OBX sample weights, repriced (model) | **2.27** | 11.48 / 11.77 | **19.8%** / 19.3% | 4.89% | 56% |
| MSCI Norway top-10 weights (30 Oct) | 2.22 | 10.99 / 11.58 | 20.2% / 19.2% | 4.72% | 52% |
| Market cap (14 names) | 2.39 | 10.76 / 11.19 | 22.2% / 21.4% | 5.12% | 55% |
| Without Frontline | 2.26 | 11.71 / 12.03 | 19.3% / 18.8% | 4.44% | 52% |
| Without Kongsberg | 2.06 | 10.54 / 11.00 | 19.5% / 18.7% | 5.39% | 57% |
| Without Kongsberg, Gjensidige, Vår | 1.97 | 10.39 / 10.92 | 19.0% / 18.1% | 5.35% | 56% |

Aggregates are harmonic: P/B = Σw ÷ Σ(w / P/B); ROE = earnings ÷ book; yields are
weight-averaged. MSCI Norway top-10 weights on 30 Oct: Equinor 21.62, DNB 18.71, Kongsberg 10.92,
Aker BP 9.11, Mowi 6.96, Hydro 6.25, Telenor 5.96, Orkla 5.14, Yara 4.61, Vår 4.07 (Gjensidige
out, Vår in).

### Constituent consensus (Yahoo `earningsTrend`, 6 Nov 2026) `[F]`

| Ticker | Price NOK (5 Nov) | EPS CY26 | EPS CY27 | Ccy | Analysts (CY27) | Fwd div. yield | CY27 vs 11 Oct |
|---|---|---|---|---|---|---|---|
| EQNR | 405.4 | 5.868 | 4.655 | USD | 19 | 3.58% | +5.1% |
| AKRBP | 319.3 | 4.200 | 3.380 | USD | 16 | 7.70% | +13.6% |
| VAR | 50.66 | 0.770 | 0.608 | USD | 12 | 10.80% | +24.7% |
| SUBC | 311.0 | 2.639 | 2.691 | USD | 14 | 6.27% | −0.2% |
| FRO | 443.3 | 12.491 | 7.308 | USD | 4 | 22.44% | +41.6% |
| DNB | 326.7 | 26.64 | 28.44 | NOK | 16 | 5.51% | +1.1% |
| STB | 202.6 | 11.53 | 13.52 | NOK | 8 | 2.67% | +0.6% |
| GJF | 279.6 | 15.46 | 17.47 | NOK | 13 | 3.58% | +0.8% |
| KOG | 339.4 | 7.317 | 11.418 | NOK | 10 | 0.65% | +0.1% |
| NHY | 68.76 | 8.158 | 7.559 | NOK | 13 | 4.36% | −8.4% |
| MOWI | 219.4 | 1.194 | 1.438 | EUR | 11 | 3.46% | +2.2% |
| TEL | 136.5 | 11.735 | 9.192 | NOK | 14 | 7.11% | −1.5% |
| YAR | 400.9 | 46.94 | 40.50 | NOK (EPS; reports in USD) | 18 | 5.49% | −13.5% |
| ORK | 101.9 | 6.612 | 6.856 | NOK | 8 | 3.93% | −0.1% |

- Checks: Yara's EPS is in NOK (P/E 9.9 against the quote's forward P/E 9.9). USD EPS converted
  at 9.2944, EUR at 10.442 (Yahoo, 5 Nov). The OBX ETF look-through (Yahoo) still shows the 9 Oct
  weights and sectors (energy 33.0, financials 20.3); NORW: energy 32.9, financials 23.0, P/E 13.1
  (E/P 0.0761), P/B 2.19 (0.4562).

### Sources

| # | Source | Content | Observed / published |
|---|---|---|---|
| S1 | Yahoo Finance chart API (daily) | OSEBX, URTH, ACWI, ^GSPC, IXC, BZ=F, NOK=X, EURNOK=X, EURUSD=X; month-end series Jan 2013–Oct 2026 (Brent from Jul 2007); 5 Nov closes | 6 Nov 2026 |
| S2 | Yahoo quote / quoteSummary API (crumb) | Constituent prices, consensus EPS (6 Nov), P/B, ROE, yields, ETF look-through | 6 Nov 2026 |
| S3 | [MSCI Norway Index](https://www.msci.com/indexes/index/957800/msci-norway-index) | Div. yield 4.54%, P/E 13.85, fwd 12.51, P/BV 2.46; top-10 weights (Equinor 21.62, DNB 18.71, Kongsberg 10.92 …) | 30 Oct 2026 (read 6 Nov) |
| S4 | [MSCI World Index](https://www.msci.com/indexes/index/990100/msci-world-index) | Div. yield 1.54%, P/E 22.29, fwd 17.38, P/BV 4.06; top 10 (Apple 5.65, NVIDIA 5.25, Microsoft 4.11 …); st. dev. 11.63 / 14.93 / 14.86% (3 / 5 / 10 y) | 30 Oct 2026 (read 6 Nov) |
| S5 | [FactSet Earnings Insight](https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_103026.pdf) | S&P 500 fwd P/E 18.7 (5-y 19.8, 10-y 19.1), trailing 25.9 (10-y 23.7); CY26 +32.9%, CY27 +16.3%; Q3 +30.2% blended; target 9,327.80; "Magnificent 7" Q3 −14.7% vs estimates | 30 Oct 2026 (data 29 Oct) |
| S6 | FRED `DGS10`, `BAMLH0A0HYM2`, `DCOILBRENTEU` | US 10-y 4.90%, US HY OAS 3.32% (4 Nov); Dated Brent month-ends Aug 2023–Oct 2026 (data note) | 4 Nov 2026 |
| S7 | Norges Bank API `ANN_FX_SPU`; HY BBB 5 Nov | FX purchases for the government NOK 300m/day in Nov (Sep and Oct also 300); net 176m/day after transfers | 30 Oct 2026 |
| S8 | [Nordnet blog, "Hva er pris/bok på Oslo Børs nå og historisk?"](https://www.nordnet.no/blogg/hva-er-pris-bok-pa-oslo-bors-na-og-historisk) | OSEBX (67 names), Bloomberg, 13 years: P/B 1.5 cheap, 2.1 expensive (thresholds from three named analysts); 1.8 in Apr 2023; buying at 2.4–2.7 has often been followed by losses | 4 Apr 2023 — old, rule of thumb `[E]` |
| S9 | [Affärsvärlden](https://www.affarsvarlden.se/artikel/genomgang-sa-dyr-och-billig-ar-stockholmsborsen-jamfort-med-andra-marknader) | Norway ~P/E 13.5 over the last 10 years | c. 2023, undated `[E]` |
| S10 | MSCI Norway factsheets (search summary) | 30 Apr: P/BV 2.24, fwd P/E 12.84; 30 Jun: P/BV 2.11, fwd 10.53 | Apr / Jun 2026 `[E]` |
| S11 | `docs/oil-market-bbb.md` (31 Oct, update 4 Nov), `docs/hy-market-bbb.md` (5 Nov), `docs/ai-market-bbb.md` (Update 6, 1 Nov; 5 Nov check), `docs/msft-analysis.md` v3, `docs/googl-analysis.md` v2, `docs/nvda-analysis.md` v1.2, `docs/amzn-analysis.md` v2, `docs/mu-analysis.md` v3 | Upstream paths, the HY market reference and the company blocks | 28 Oct–5 Nov 2026 |
| S12 | Norges Bank API (`data.norges-bank.no/api`) | `EXR` daily fixings USD, EUR, I-44, TWI from 1995 (to 5 Nov) and monthly averages from 1990; `GOVT_GENERIC_RATES` 10Y 4.367 (4 Nov); `FINANCIAL_INDICATORS` FCI −1.65 (29 Oct); `ANN_FX_SPU` 2026 | 6 Nov 2026 |
| S13 | [Norges Bank MPR 3/26 dataset](https://www.norges-bank.no/contentassets/1462461ecf6a423eb7bc3e89c1cb0d2b/data-mpr-3-26.xlsx) | Data D Table 3: I-44 119.6 / 112.3 / 110.0 / 110.0 / 110.0 (2025–29), CPI 3.0 / 3.3 / 2.6 / 2.3 / 2.1, policy rate 4.3 / 4.2 / 4.6 / 4.2 / 3.7; Data E quarterly I-44 110 from Q4-26 | 24 Sep 2026 |
| S14 | iShares URTH holdings CSV (`ishares.com/us/products/239696/ishares-msci-world-etf/latest-holdings.csv`) | MSCI World weights of the block names, energy and sector weights | 4 Nov 2026 |

- **Scripts** (scratchpad copies run with `py -I`; copied to `references/`): `osl2.py` (Oslo),
  `world2.py` (World; imports `idxai3.py`), `bridge.py` (World bridge; imports `upd.py`),
  `bottomup2.py`, `payout2.py`, `valagg2.py`, `urthparse.py` (holdings → `dl2/urth_ai_nov.json`),
  `recent.py` (5 Nov closes → `dl2/recent_1105.json`), `corr3.py`, `i44b.py`, `i44c.py`,
  `fetchlong.py`. The README in `references/` has no 6 Nov section yet (skill text left as is).
- **Not found `[?]`:** a long series of Oslo forward P/E or P/B (the historical anchors are
  secondary); MSCI World forward P/E 10-year average (≈ 16.5–17 is an assumption); free-float
  weights below the OBX top 10, and a fresh OBX ETF look-through (still 9 Oct); a P/B history for
  MSCI World (the exit P/B of 3.2 cannot be tested); the CY27 consensus revision of World energy
  (its P/E is scaled by price only).
- **Quality notes:** URTH is a total-return proxy after its 0.24% fee and withholding tax, so World
  history is slightly understated. OSEBX starts Mar 2013 on Yahoo. Correlations of monthly returns
  say nothing about the level of earnings; the oil link to the 3-year return runs through the
  energy earnings share. Yahoo's Brent front-month history changed between the 11 Oct and 6 Nov
  fetches (see the data note under the linkage tables).
