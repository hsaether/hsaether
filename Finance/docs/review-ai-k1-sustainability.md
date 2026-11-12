# Review: is the K1 Base path the most likely one, or the companies' plan? — 11 Nov 2026

**Reviewed:** `docs/ai-market-bbb.md` (1 Nov baseline, Update 7 of 7 Nov, note of 11 Nov): K1, K3, K4,
E1, E2, T1, the monetisation ratio, the scenarios, the signposts and the Memory cycle section.

**Skill revisions:**
- `ai-market-bbb` **2026-11-06.1** (method; not changed here);
- `iaf-valuation` **2026-11-10.1**, through the company analyses read: `docs/msft-analysis.md` v3,
  `docs/googl-analysis.md` v2 (re-mark 7 Nov), `docs/amzn-analysis.md` v2 (re-run 11 Nov),
  `docs/nvda-analysis.md` v1.3, `docs/tsm-analysis.md` v1.2; `docs/mu-analysis.md` v3 through
  `docs/review-ai-h1-non-k1-funding.md`.

**Status:** a proposal for the user's decision. Nothing in the baseline, the skills, the company
analyses or the register is changed. `docs/review-ai-debt-and-market-power.md` (not adopted) was read
only to see what was rejected; none of its tests or figures is reused.

**Tags:** `[F]` reported fact (filing, release, official statistic) · `[E]` guidance, consensus,
call transcript, press or secondary · `[A]` my own assumption or calculation, with its reasoning ·
`[?]` not found.

**Calculations** (scratchpad, `py -I`): `cy.py` calendarises the five companies' filed cash flows;
`ret.py` and `ret2.py` are the return arithmetic (a monthly vintage model of the AI asset base);
`effects.py` and `comp.py` pass K1 paths through the `model.py` v2.1 build at the Update 7 inputs.
The build reproduces the baseline: H1 basket P/E 13.71, Base 11.2%, hurdle P/E 13.40; E basket 8.1%
(baseline 8.2%, rounding), hurdle P/E 18.8.

## 1. Question

The user's challenge: funding and budgets are not enough. Spending at the planned pace needs a
sustainable return, and Base must be the most likely path, not guidance and consensus without
qualification. So:
- Is K1 Base (MSFT, GOOGL, AMZN, META, ORCL: ~435 in 2025, 790 in 2026, 1,120 / 1,250 / 1,300 in
  2027–29) the most likely path, or a guidance-and-consensus path that assumes the spending earns a
  sustainable return?
- If the latter, how should Base be set instead?

## 2. Short answer

- **How K1 Base is set today.** 2026 is guidance. 2027 sits between consensus (+39%) and Goldman
  (+54%), justified as "largely contracted". 2028–29 (+12%, +4%) is an unquantified `[A]` taper
  ("growth falls to the pace of end revenue plus replacement").
  - The only durability qualification is the monetisation ratio (lab revenue ÷ K1). The baseline
    reads it "for direction, not level", and it rises in every scenario, so it cannot tell a
    sustainable path from an unsustainable one.
  - There is no return test. **In practice Base 2026–27 is the companies' and the Street's plan,
    and 2028–29 is an untested taper.**
- **The return case fails inside the window on the AI BBB's own paths** `[A]`:
  - Today the AI build earns well: AWS 38.7% operating margin `[F]`, and about 12% pre-tax on the
    incremental AI asset base in 2026.
  - On Base K1 and the Base E-paths the pre-tax return falls to **~6% in 2027, ~2% in 2028 and ~0%
    in 2029**, because depreciation of the 2026–27 build arrives while E2 growth slows.
  - Revenue needed for 10% pre-tax: **~880bn in 2028 and ~1,230bn in 2029**. The E-paths deliver
    ~600bn and ~740bn on a generous attribution: coverage **69% and 60%** (49–71% across the
    sensitivities).
- **The gap is mostly locked in by the 2026–27 build.** Even K1 at 650 in 2028–29 only holds the
  2027 coverage. A strictly return-constrained Base would sit below the financing-break Bear (800).
- **History.** Returns lagged spending for years before capex turned: 4–5 years in telecom and a
  decade of negative free cash flow in shale.
  - The turn came from a demand, price or credit signal, not from the accounting return.
  - Both earlier hyperscaler surges ended in a flat year: +4% in 2019, −2% in 2023 `[F]`.
  - Base calls 2028–29 "digestion" but has +12% in 2028.
- **Recommendation: Option D**, a cycle-first K1 section like the memory section, with the return gap
  as its durability gauge. It sets **Base K1 790 / 1,120 / 1,170 / 1,170** (2026–29; 2028 +4.5%,
  2029 flat) in place of 790 / 1,120 / 1,250 / 1,300. Bear and Bull are unchanged.
- **Effect** `[A]`:
  - H1 basket 11.2% → **7.6%**.
  - NVIDIA 20.9% → **17.0%** (P_k $212 → $192; still clears at $168.89).
  - TSMC 9.5% → 8.2–8.6%; Micron 18.3% → 17.0–17.5% (an upper bound).
  - E basket 8.1% → 8.5–9.7%; Microsoft, Alphabet and Amazon +0.2 to +1.5 pp.
  - All six −0.4 to −1.3 pp. **No verdict flips.**

## 3. Findings with sources

### 3.1 How K1 Base is set today (S1, S2)

| Year | Base | How it is set | Qualification applied | Reading |
|---|---|---|---|---|
| 2026 | 790 `[E]` | Guidance after Q3 (Amazon ~220, Alphabet 195–205, Microsoft ~170, Meta 135–145, Oracle 60–70 `[A]`) | None needed: current year, no spread (skill rule) | The plan, now mostly spent: the five's cash capex was **560bn in nine months** `[F]` (S3) |
| 2027 | 1,120 (+42%) `[A]` | Between consensus (~1,100, +39%) and Goldman (1,200, +54%) `[E]`; "largely contracted" (backlog ~2,480bn; "increase significantly", "meaningfully increase") `[E]` | Backlog and supply limits, stated, not sized | Consensus-plus. The only Base year with a contract argument |
| 2028 | 1,250 (+12%) `[A]` | "Growth falls to the pace of end revenue plus replacement" | None quantified. Below brokers (Goldman 1,400 `[E]`) | Called "digestion", but +12% is above both earlier hyperscaler digestion years (+4%, −2%) |
| 2029 | 1,300 (+4%) `[A]` | Same rule | None quantified | A taper |
| All years | — | Monetisation ratio E1 ÷ K1: 0.13 → 0.17 / 0.22 / 0.28 (Base) `[A]` | "Track its direction, not its level"; it rises in Bear, Base and Bull alike | It cannot discriminate. It is a flow ratio, so it misses the depreciation of the capital stock |

**Internal consistency check (company analyses, S10)** `[A]`:
- The three analysed platforms set their own Base capex as a share of K1, with named reasons:
  - Microsoft shifts capacity to operating leases;
  - Alphabet sells TPU systems into customers' data centres;
  - Amazon's share falls.
- Together they take **69% / 67% / 66%** of K1 in 2027–29:
  - Microsoft 210 / 225 / 230;
  - Alphabet 275 / 300 / 305;
  - Amazon 290 / 310 / 320.
- **K1 Base therefore needs Meta and Oracle at 345 / 415 / 445.** That is +53% in 2027 on
  ~225 in 2026 (Meta ~140, Oracle ~85 on calendarised filings), and +20% in 2028. Meta and Oracle are
  the two names with no company analysis and the weakest return evidence (3.4).
- If Meta and Oracle grew like the three (+30% in 2027, then +8% and +2%), K1 would be
  ~1,065 / 1,150 / 1,175. The check is circular in part, because the shares are themselves set
  against K1. It is evidence that **the K1 growth after 2027 rests on the residual names, not on a
  bottom-up view**.

**K1 history from filings** (S3, S18):

| USD bn | 2022 | 2023 | 2024 | 2025 | 9M 2026 |
|---|---|---|---|---|---|
| Cash capex of the five (PP&E purchases, calendarised) `[F]` | 158.0 | 154.4 | 239.1 | 411.5 | 560.4 |
| Growth `[F]` | +21% | −2% | +55% | +72% | — |
| Incl. finance leases (four-company 251 / 416 `[E]` + Oracle `[F]`) | ~165 | ~165 | ~262 | **~450** | — |
| 2026 on 9M actuals + Q4 guides: Microsoft ~170, Alphabet ~200, Amazon ~220, Meta ~140, Oracle ~85 `[F]`/`[E]`/`[A]` | | | | | **~815** |

- K1 2025 is ~450 by filings against the baseline's ~435 `[A]`. K1 2026 is ~815 against 790,
  because Oracle's calendar 2026 is ~85, not 60–70. Both gaps are below the 5% rule; they are noted,
  not used to move anything here.

### 3.2 AI-related revenue now

| Company | AI-related revenue (dated) | Cloud segment (Q3-26) | Tag |
|---|---|---|---|
| Microsoft | AI business run-rate **> $37bn** (Mar 2026, +123% y/y); OpenAI paid **$10.0bn** in Q1 FY27 (10.8% of revenue, incl. revenue share); Copilot > 20m paid seats (Apr) | Azure **$33.17bn** (+48%); Intelligent Cloud gross margin 66.1% (FY24) → 62.2% (FY25) → **58.0%** (FY26) | `[E]` run-rate (S16); `[F]` OpenAI (S10), Azure, segment (S7) |
| Amazon | AWS AI run-rate **> $25bn** (Q2 2026, "triple digits"); custom chips > $25bn | AWS **$45.98bn** (+39%), operating income **$17.77bn (38.7%)**, D&A $9.23bn (+63%) | `[E]` (S16, search excerpt); `[F]` (S4) |
| Alphabet | Generative-AI product revenue "nearly 800%" y/y (Q1 2026); no dollar figure `[?]` | Google Cloud **$30.71bn** (+103%), operating margin 36.2% | `[E]`; `[F]` (S10) |
| Oracle | OCI ~$7.4bn in the Jun–Aug quarter (+121%); RPO 664bn | — | `[E]` (S1) |
| Meta | No AI revenue line. The return is ad performance: revenue +26% (impressions +10%, price per ad +14%) | Operating margin 35% before the $9.9bn legal charge (40% a year earlier) | `[F]` (S8; ad metrics via S1) |
| Labs (E1) | Lab revenue 2026 ~94–100bn; Anthropic Q3 $16.96bn booked. The labs' compute spending sits in E2 | — | `[A]`/`[F]` (S1) |

- Disclosed AI run-rates (Microsoft ≥ 37, AWS ≥ 25, OCI ~30 annualised, Google not given) sum to
  ~100–150bn by mid-2026 `[E]`/`[A]`. That is against K1 2026 of 790–815bn.
- The return arithmetic below attributes ~290bn to AI in 2026, about **twice** the disclosed
  figures. It is deliberately generous to Base.

### 3.3 Capex, depreciation and useful lives

| Item | Filed policy or fact | Source |
|---|---|---|
| Amazon servers and networking | "Five to six years". A subset was **shortened from six to five years from 1 Jan 2025**; servers were lengthened from five to six from 1 Jan 2024. Heavy equipment (data-centre infrastructure) **lengthened from 10 to 10–13 years** in 2025 `[F]`. Expected 2025 effect of the shortening ~$0.7bn `[E]` | S5 (10-K 2025, R23); S20 |
| Alphabet | Servers and network equipment "generally over a period of six years"; buildings 7–40 years `[F]`. The 2023 change from four to six years cut 2023 depreciation by $3.9bn `[F]` | S6; S20 |
| Microsoft | Computer equipment 2–6 years; buildings 5–15 years (FY26) `[F]`; building lives 15 → 25 years from FY27 `[F]`/`[E]` | S7; S1 |
| Meta | Servers and network assets 5.5 years from 1 Jan 2025; expected 2025 depreciation saving ~$2.9bn `[E]` | S20 |
| Compute share of capex | Alphabet Q3: 65% servers and networking, 35% data centres `[E]` (call); Microsoft about two-thirds to three-quarters short-lived `[E]`; Microsoft's gross PP&E: servers, network and software $215.9bn of $431.8bn `[F]` | S1; S7 |
| Assets not yet in service | Alphabet: $78.6bn of $345.1bn gross at end-2025 (23%, ~0.8 years of capex) `[F]` | S6 |
| GPU economic life (market evidence) | H100 (launched 2022–23) still rents at **$2.57–2.79 an hour** (neocloud index, May–Jul 2026); B200 **$5.62** (1 Sep, +27.6% year to date); the B200 term curve is backwardated (3-month 5.73, 12-month 5.39) `[E]` | S15 |

**Reading:**
- The filed lives (5–6 years) are supported by today's rental market: a three-year-old H100 still
  earns.
- The life extensions of 2022–24 (Alphabet $3.9bn in 2023 alone) lifted reported earnings at the
  start of the AI build. Amazon's 2025 shortening is the first move back.
- An economic life of four years is the sensitivity that matters (4.3).

### 3.4 Returns now: filed

**AWS, the cleanest series** (S4, S5) `[F]` unless tagged:

| AWS, USD bn | 2022 | 2023 | 2024 | 2025 | TTM Q3-26 |
|---|---|---|---|---|---|
| Revenue | 80.10 | 90.76 | 107.56 | 128.73 | 161.38 `[A]` (sum of filed periods) |
| Operating income | 22.84 | 24.63 | 39.83 | 45.61 | 61.02 `[A]` |
| D&A | 9.88 | 12.53 | 13.32 | 21.45 | 31.15 `[A]` |
| Margin before D&A | 40.8% `[A]` | 40.9% `[A]` | 49.4% `[A]` | 52.1% `[A]` | 58.7% (Q3) `[A]` |
| D&A ÷ revenue | 12.3% `[A]` | 13.8% `[A]` | 12.4% `[A]` | 16.7% `[A]` | 20.1% (Q3) `[A]` |
| Property and equipment additions | 27.76 | 24.84 | 53.27 | 96.50 | 147.24 (9M) |
| Net property and equipment, year-end | 60.32 | 72.70 | 110.68 | 190.06 | 313.01 (30 Sep) |
| Operating income ÷ average net PP&E `[A]` | — | 37% | 43% | 30% | ~26% (9M annualised) |
| Net PP&E ÷ revenue (run-rate) `[A]` | 0.75 | 0.80 | 1.03 | 1.48 | 1.70 |

- **Incremental return, 2023 → TTM Q3-26** `[A]`: operating income +36.4bn on net PP&E +240.3bn is
  **15% pre-tax**. On gross additions since 2024 (297bn) it is **12%**.
- Pre-AI (2023–24) AWS earned 37–43% on its net PP&E. The capital needed per dollar of revenue has
  doubled since 2023, and the cash margin rose from 41% to 59%. That is why the return is still
  positive.

**Pure-play AI cloud (CoreWeave, Q3 2026, S9)** `[F]`:
- revenue $3.66bn;
- adjusted EBITDA margin 62%, so cash costs are ~38% of revenue;
- D&A **$1.89bn = 52% of revenue**;
- operating income $0.21bn (5.7%), on net PP&E of $56.8bn: ~1.5% annualised `[A]`;
- net loss $0.71bn after $0.85bn of interest.

**The five, cash** (S3) `[F]`; ratios `[A]`:

| | Microsoft | Alphabet | Amazon | Meta | Oracle (to 31 Aug) | Five |
|---|---|---|---|---|---|---|
| Capex ÷ OCF, Q3-26 | 68% | 121% | 182% | 104% | 123% | **116%** |
| Capex ÷ OCF, TTM | 69% | 89% | 128% | 78% | 161% | **95%** |
| FCF TTM, USD bn | 60.0 | 19.7 | −46.9 | 28.6 | −28.7 | **32.7** |
| Dividends + buybacks TTM, USD bn | 48.0 | 31.3 | 0 | 14.1 | 6.0 | 99.4 |
| **FCF after shareholder returns, TTM, USD bn** | 11.9 | −11.5 | −46.9 | 14.6 | −34.8 | **−66.7** |
| Same, Q3-26 alone, USD bn | | | | | | **−48.8** |
| Depreciation growth y/y, Q3 | +56% (10-Q, S10) | +49% | AWS +63% | +44% | +90% | — |
| Revenue growth y/y, Q3 | +19% | +25% | AWS +39% | +26% | +30% | — |

**Cost of capital** (for the yardstick):
- 10-year Treasury **4.88%** (9 Nov) `[F]` (S12); IG corporate OAS **0.91%** `[F]` (S12);
- Alphabet's Q3 USD notes, weighted coupon 5.55% (15 years) `[F]` (S10); CoreWeave's cost of debt
  7.9% `[E]` (S1);
- equity k = 12% (IAF).

An after-tax WACC of ~9–10% is ~11–12.5% pre-tax `[A]`, so the user's 10% pre-tax is a floor below
the cost of capital, not above it.

**Management language on returns:**
- Zuckerberg (Sep 2025) said misspending "a couple of hundred billion" would be unfortunate, but the
  risk is "higher on the other side" `[E]` (S17).
- Pichai: the risk of underinvesting is "dramatically greater" than overinvesting `[E]` (S17).
- Amazon: servers "break even in under three years" (as quoted in `docs/amzn-analysis.md`) `[E]`.
- **No hyperscaler states a return hurdle for AI capex** `[?]`. The stated logic is strategic
  (capacity, share, asymmetric risk). The plan is therefore not return-gated, which is the user's
  point.

## 4. Return arithmetic

### 4.1 Method and parameters

The **AI asset base** is K1 above a non-AI baseline. Each month's spend is depreciated from when it
is placed in service. Net assets include construction in progress: the capital is invested even
before it earns.
- **Required revenue** = (r × average net AI assets + AI depreciation) ÷ (1 − cash cost ratio).
- **Supply** = the AI revenue that the baseline's own Base paths deliver.

| Parameter | Value | Basis |
|---|---|---|
| K1 2022–25 | 165 / 165 / 262 / 450 | 3.1 `[F]`/`[E]` |
| K1 2026–29 | Base 790 / 1,120 / 1,250 / 1,300; flat after 2029 | Baseline `[A]`; the post-2029 level only carries depreciation |
| Non-AI capex | 140 in 2023, +5% a year | `[A]`, calibrated (next row) |
| Calibration | Model AI depreciation: TTM 71bn, Q3-26 annualised 98bn. Observed: the five's D&A rose ~112bn annualised from Q3-23 to Q3-26 (Q3-26 run-rate 206 `[F]`), of which ~96 is above a 5% non-AI trend `[A]` | S3 |
| Short-lived share / life / in-service lag | 65% / 5.5 years / 2 months | 3.3 `[F]`; the lag `[A]` |
| Long-lived share / life / lag / land | 35% / 20 years / 12 months / 5% of it | 3.3 `[F]` (Alphabet not-in-service 23% of gross) / `[A]` |
| Cash cost ratio of AI revenue | 40% | AWS 41% (Q3), CoreWeave 38% `[F]` |
| Required pre-tax return r | 10% on average net AI assets | The user's yardstick; below WACC (3.4) |
| Supply: cloud | E2 four clouds 440 (2026) at +38% / +25% / +18%, then +12% / +10% (2030–31) `[A]`. The AI part is the revenue above a 10% a year trend from 2023's ~180 (AWS 90.8 + Google Cloud 33.1 `[F]`, Azure ~50, OCI ~6 `[A]`) | Baseline E2; the trend `[A]` |
| Supply: Copilot (T1) | 10 / 14 / 23 / 31bn (2026–29): Base seats × ~$240 a year | Baseline T1; price from `docs/msft-analysis.md` `[A]` |
| Supply: Meta | Revenue above a 10% a year trend from 2023 (134.9 `[F]`), 2026 ~256 `[A]`, then +13% a year `[A]`: 76 → 130bn by 2029 | Upper bound: all of Meta's above-trend growth is credited to AI |

### 4.2 Base K1 on the Base E-paths

| USD bn `[A]` | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---|---|---|---|---|---|---|
| K1 | 450 | 790 | 1,120 | 1,250 | 1,300 | 1,300 | 1,300 |
| AI capex | 296 | 628 | 950 | 1,071 | 1,112 | 1,103 | 1,093 |
| Cumulative AI capex | 461 | 1,089 | 2,038 | 3,110 | 4,222 | 5,325 | 6,418 |
| AI depreciation | 35 | 88 | 184 | 313 | 454 | 590 | 705 |
| Average net AI assets | 292 | 708 | 1,374 | 2,137 | 2,842 | 3,420 | 3,863 |
| **Revenue needed, r = 10%** | 106 | 265 | 536 | **877** | **1,230** | 1,554 | 1,819 |
| Revenue needed, r = 0% | 58 | 147 | 307 | 521 | 757 | 984 | 1,175 |
| **Supply** (cloud / Copilot / Meta) | 111 (68 / 5 / 38) | 287 (200 / 10 / 76) | 449 (344 / 14 / 92) | **602** (469 / 23 / 110) | **738** (577 / 31 / 130) | 845 | 944 |
| **Coverage of the 10% need** | 104% | 108% | 84% | **69%** | **60%** | 54% | 52% |
| Gap to 10%, revenue | — | — | −87 | **−275** | **−492** | −709 | −875 |
| **Pre-tax return on AI net assets** | 10.9% | 11.9% | 6.2% | **2.3%** | **−0.4%** | −2.4% | −3.6% |
| Five-company D&A (non-AI 93.5 in 2023 + 5% a year, plus AI) | 138 | 196 | 298 | 432 | 579 | 722 | — |

- Cross-check: the three analysed companies' own D&A paths sum to 239 / 313 / 374 in 2027–29:
  Microsoft 72 / 90 / 102, Alphabet 52 / 75 / 95, Amazon 115 / 148 / 177 on a cash-flow basis
  (S10). With Meta and Oracle at ~65 / 100 / 130 `[A]`, the totals (304 / 413 / 504) are within
  2–13% of the model, which is the higher of the two in 2028–29.

### 4.3 Sensitivities (Base K1)

| Case | Coverage 2028 / 2029 | Revenue needed 2029 | Supply 2029 | Pre-tax return 2028 / 2029 |
|---|---|---|---|---|
| **Central** | **69% / 60%** | **1,230** | **738** | **2.3% / −0.4%** |
| r = 8% / 12% | 75% / 65%; 63% / 56% | 1,136 / 1,325 | 738 | unchanged |
| Cash cost 35% / 45% | 74% / 65%; 63% / 55% | 1,136 / 1,342 | 738 | 3.7% / 0.9%; 0.9% / −1.7% |
| Short life 6.0 years | 71% / 62% | 1,188 | 738 | 3.3% / 0.7% |
| **Short life 4.0 years (economic)** | 60% / 53% | 1,382 | 738 | −2.4% / −5.0% |
| Short-lived share 75% | 65% / 57% | 1,298 | 738 | 0.6% / −2.3% |
| **Strict: no Meta uplift** | 56% / 49% | 1,230 | 608 | −0.8% / −3.1% |
| **E2 at the Bull row** (+45% / +32% / +22%) | 78% / 71% | 1,230 | 870 | 4.6% / 2.4% |

### 4.4 Other K1 paths (supply held at the Base E-paths)

| K1 2027 / 2028 / 2029 | Coverage 2027 / 2028 / 2029 / 2030 | Pre-tax return 2028 / 2029 / 2030 |
|---|---|---|
| Base 1,120 / 1,250 / 1,300 | 84 / 69 / 60 / 54% | 2.3 / −0.4 / −2.4% |
| **Plateau 1,120 / 1,170 / 1,170 (recommended Base)** | 84 / 70 / 63 / 58% | 2.5 / 0.2 / −1.6% |
| Flat 1,120 / 1,120 / 1,120 | 84 / 70 / 64 / 60% | 2.6 / 0.5 / −1.1% |
| **1,120 / 650 / 650: holds the 2027 coverage by 2029** | 84 / 77 / 81 / 84% | 4.2 / 4.8 / 5.3% |
| Bear 950 / 800 / 820 | 88 / 81 / 79 / 78% | 5.2 / 4.4 / 3.6% |

### 4.5 What the arithmetic says

- **The gap is revenue, and it is large.**
  - At 10% pre-tax the AI build needs ~880bn of AI revenue in 2028 and ~1,230bn in 2029.
  - The baseline's own E-paths give ~600bn and ~740bn on a generous attribution, about twice the
    disclosed AI run-rates (3.2). Coverage is 60–69% (49–71% across the sensitivities). No case
    reaches 10% inside the window, not even the E2 Bull.
- **When it has to show: in 2027–28 reports.**
  - Coverage falls below 100% in 2027.
  - The five's D&A rises ~+50% a year in 2027–28 (196 → 298 → 432), against revenue growth of ~13%
    `[A]`.
  - The 2026–27 vintage (~1,580bn of AI capex) depreciates through 2031–33. Its return has to arrive
    by 2029–30, or it will not arrive at all.
- **The gap is mostly locked in by the 2026–27 build.** K1 after 2027 barely moves 2028–29 returns:
  the plateau adds 0.2–0.6 pp. Holding the 2027 coverage would need K1 at ~650 in 2028–29, below the
  Bear.
  - So a return constraint cannot set the 2028 level without putting Base under the Bear.
  - The gap measures how much of the build is vulnerable, and so the depth of the eventual
    digestion. It is not a timer.
- **Base K1 assumes the return arrives after 2029.** Base K1 is consistent with the E-paths only if
  AI revenue keeps growing well above +12% a year after 2029, or if the companies accept returns
  below the cost of capital. That is the qualification the baseline does not state today.

## 5. History: capex driven by guidance and funding when returns lag

| Episode | Run-up | Returns while spending ran ahead | Funding | What turned it | Lag from signal to capex turn | Fall |
|---|---|---|---|---|---|---|
| **US telecom and fibre, 1996–2002** | Real communications-equipment investment $62bn (Q1 1996) → $135bn (Q4 2000), ~18% a year `[E]` (S13); nominal 70.8 (1996) → 123.3 (2000) `[F]`; fibre deployment more than fourfold `[E]` | The industry lost ~$20bn in 2001; long-distance prices fell; forecast traffic growth did not come `[E]` | New entrants' equity and debt (CLEC market value $3bn → $86bn, 1996–99) `[E]` | Equity first (Nasdaq telecom peak 10 Mar 2000, −62% by year-end), then visible overcapacity and falling capacity prices (early 2001), recession, regulation `[E]` | ~3 quarters from the equity peak to the capex peak (Q4 2000) | Real −31% y/y by Q4 2001 `[E]`; nominal 123.3 → 83.7 (2002, −32%) and 82.2 (2003) `[F]`; the 2000 level not regained by 2007 (106.2) `[F]` |
| **US shale, 2010–2016** | Oil and gas well investment 86.6 (2010) → 169.8 (2014) `[F]` | **Negative free cash flow every year 2010–2019**, ~$189bn for 34 producers `[E]` | High-yield debt and equity `[E]` | Price: Brent fell by more than half from mid-2014, with high-yield energy credit closing `[E]` | 2–3 quarters (cuts in early 2015) | 169.8 → 118.7 (2015, −30%) → 63.8 (2016, **−62%**) `[F]` |
| **Hyperscalers, 2017–2019** | Five's capex 42.6 → 68.2 (2018, **+60%**) `[F]` | High (operating income +16% in 2019) `[F]` | Operating cash flow | Digestion of the 2018 build; memory down-cycle; trade war `[E]` (memory section, S1) | ~1 year | +60% → **+4%** (2019); no absolute fall `[F]` |
| **Hyperscalers, 2020–2023** | 97.0 → 130.6 → 158.0 (+37%, +35%, +21%) `[F]` | Meta operating income −38% in 2022 (46.8 → 28.9) `[F]`; AWS growth 37% (2021) → 13% (2023) `[F]` | Operating cash flow | Revenue growth slowed (cloud "optimisation", Meta ads), share prices fell; Meta cut its 2023 guide from $34–37bn to an actual $28.1bn `[E]`/`[F]` | Same year as the revenue slowdown | **−2%** (2023; Amazon −17%, Meta −13%) `[F]` |
| **AI build, 2024–** | ~165 (2023) → ~262 → ~450 → ~815 (2026E) `[F]`/`[A]`: +59% / +72% / +81% | Segment margins up today; on the Base paths the AI base earns ~0% by 2029 (4.2) `[A]` | OCF, then debt (Alphabet, Amazon, Meta, Oracle), equity (Alphabet's $49.6bn and $12.4bn ATM; Oracle's $20bn), leases (Microsoft $364.6bn not commenced), vendor financing ≥ $270bn `[F]`/`[E]` (S1) | — | — | — |

**What the analogues say:**
- **Spending ran ahead of returns for years:** 4–5 in telecom, a decade in shale. Funding kept it
  going. The user is right that funding is no evidence of a sustainable return. History adds that
  funding can delay the turn for a long time.
- **The turn came from a signal outside the accounts:**
  - telecom: equity, then prices;
  - shale: price, then credit;
  - cloud 2023: revenue growth.

  None of the four turned on a computed return.
- **Hyperscaler surges ended in a flat year, not a collapse:** +4% in 2019 and −2% in 2023, after
  1–3 years of +21% to +60%. The AI build is in its fourth year in 2027 at Base +42%.

**Where today differs:**

| Differs | Evidence | Direction |
|---|---|---|
| The issuers are cash-rich and investment-grade | OCF TTM $724bn `[F]`; IG OAS 0.91% `[F]` | Later, shallower than telecom or shale |
| Contracted backlog | K4 ~2,480bn; Google Cloud 55% within 24 months; AWS 6.1 years `[F]` (S1) | Supports 2027. Two labs are ≥ ~17% of it on filed figures (AWS 248, Google ≥ 121, Microsoft–Anthropic ~47 `[F]`), ≥ ~30% with Oracle's OpenAI share `[E]` `[A]` |
| Prices rise, not fall | H100 and B200 rental indices up in 2026 `[E]` (S15). In telecom, capacity prices fell before capex peaked | No turn signal yet |
| The customer layer is equity-funded and loss-making | Labs, neoclouds (CoreWeave: no unsecured debt at current yields) `[E]` (S1) | Like the CLECs of 2000 |
| Assets wear out in 5–6 years, not 20+ | 3.3 | Unlike fibre, idle capacity cannot wait a decade for demand; the return has to come within the asset life |

## 6. Turn signals: where they stand now

| Signal | Now (dated) | Reading | Source |
|---|---|---|---|
| Capex ÷ OCF | Five 116% in Q3-26, 95% TTM; Amazon 182%, Oracle 123%, Alphabet 121% (Q3) `[F]` | Spending exceeds internal cash: the plan depends on markets | S3 |
| FCF after dividends and buybacks | Five −66.7bn TTM, **−48.8bn in Q3-26 alone** `[F]`/`[A]` | Funding need ~$200bn a year at the Q3 pace `[A]` | S3 |
| Debt and equity raised | Long-term debt, end-2025 → 30 Sep 2026: Alphabet 46.5 → 125.1 `[F]`; Amazon 68.8 → 180.9 (face) `[F]`; Meta 58.7 → 80.9 `[F]`. Oracle 100.0 (Nov-25) → 117.7 (Aug-26) `[F]`, BBB− `[E]`, FCF FY26 −23.7bn and Q1 FY27 −5.4bn `[F]`. Microsoft 35.4 → 31.1 `[F]` but leases not commenced $364.6bn `[F]`. Equity: Alphabet $49.6bn + $12.4bn ATM, Oracle $20bn `[F]`/`[E]` | Four of five fund externally. Oracle is the weakest | S3, S8, S10, S1 |
| D&A growth against revenue growth | Q3 y/y: AWS D&A +63% vs revenue +39%; Alphabet +49% vs +25%; Microsoft +56% vs +19%; Meta +44% vs +26%; Oracle +90% vs +30% `[F]` | The depreciation wave has started; 4.2 has it at ~+50% a year in 2027–28 | S3, S4, S10 |
| Margins | Microsoft Intelligent Cloud gross margin 66% → 62% → 58% (FY24–26); Meta 35% (ex charge) vs 40% `[F]`; AWS 38.7% `[F]`, up | Mixed: the fastest builders' margins are falling; AWS is not yet | S7, S8, S4 |
| Utilisation and pricing | H100 $2.75 (27 Jul), B200 $5.62 (1 Sep, +27.6% year to date); B200 curve backwardated `[E]`; all four clouds "supply constrained" `[E]` | **No turn signal.** The curve expects lower prices next year | S15, S1 |
| Customer concentration | OpenAI 10.8% of Microsoft's revenue `[F]`; OpenAI 138 + Anthropic ≥ 110 ≈ 43% of AWS backlog `[F]`/`[A]`; Anthropic ≥ 121.3bn ≈ 22% of Google Cloud's backlog `[F]`/`[A]`; more than half of Oracle's RPO is OpenAI `[E]` | High. The return rests on two equity-funded labs | S1, S10 |
| Backlog momentum | K4 +3% q/q; Microsoft flat; AWS +16.5%; Google +9% `[F]` | Slowing at Microsoft | S1 |
| Management language | Asymmetric-risk framing, no stated hurdle `[E]` | The plan is not return-gated | S17 |
| Suppliers | NVIDIA supply commitments flat at ~$87–88bn a year in FY28–29 after the FY27 step `[F]` | A plateau after 2027 is what the largest supplier has contracted for | S1 |

**Summary:** the funding and depreciation signals are on the Bear side and the pricing signals on the
Bull side. Backlog is mixed. Nothing yet turns 2027. The question is 2028–29.

## 7. Options compared

Effects are on the Base decision figures (Update 7 inputs; NVIDIA at $168.89, TSMC at $396.48,
Micron at $656.39, as in the company analyses). The H1 shock follows the method of
`docs/review-ai-h1-non-k1-funding.md`, with the H1/K1 ratio held. TSMC passes through 20–30% of the
H1 change and Micron 30–50%. The E basket and the company analyses gain the capex saving
(after-tax 0.86×). The upper bound adds lower 2030 D&A with revenue held on E2.

| Criterion | **A.** Keep guidance and consensus; add a return check and a signpost | **B.** Return-constrained Base after 2027 | **C.** Haircut by the guidance gap and digestion base rates | **D.** Cycle-first K1 section, with the return gap as its gauge (recommended) |
|---|---|---|---|---|
| Fidelity to "most likely" | Low for 2028: keeps +12% in a year it calls digestion | Low: holding the 2027 coverage needs K1 ~650 in 2028–29, below the Bear; none of the four past turns came from a computed return (5) | Low. The guidance gap depends on the regime (−21% in digestion years, +10–22% in boom years; table below). Applied unconditionally it is noise; conditionally it is a cycle call | High: 2027 on contracts; 2028–29 on the cycle evidence (5, 6) and the return gauge |
| Evidence and measurability | Filed inputs for the check; the path itself is unchanged | `[A]`-heavy (AI attribution, cash cost, lives); the path moves mechanically | n = 2 digestion years; guidance history from the press `[E]` | Filed history, filed turn signals, the sized return gauge; a judgement with evidence for and against, as in the memory section |
| Double counting with the financing-break Bear | None | **High:** Base would sit under the Bear (650 against 800) | Low | None: the plateau is digestion without a break; the Bear (950 / 800 / 820) stays the break |
| One-place rule | Kept | Kept | Kept | Kept: the judgement is made only in the AI BBB |
| K1 2027 / 2028 / 2029 | 1,120 / 1,250 / 1,300 | 1,120 / 650 / 650 | 1,120 / 1,190 / 1,240 (50/50 Base and a 2019/2023-type year) | **1,120 / 1,170 / 1,170** |
| H1 2028 / 2029 (Base 800 / 825) | 800 / 825 | 416 / 412 | 762 / 787 | **749 / 742** |
| H1 basket Base (11.2%); hurdle P/E (13.40) | 11.2%; 13.40 | −10.9%; 6.80 | 9.5%; 12.79 | **7.6%; 12.10** (margin of safety −11.7%) |
| NVIDIA Base 20.9%, P_k $212.1 | unchanged | −2.9%, $107 (fails) | 19.1%, $202 | **17.0%, $192 (+13.4%: clears)** |
| TSMC Base 9.5%, P_k $369.8 | unchanged | 2.5–4.9%, $303–325 | 8.9–9.1%, $364–366 | **8.2–8.6%, $357–361** (fails more) |
| Micron Base 18.3%, P_k $751.6 | unchanged | 10.9–14.0%, $610–667 | 17.6–17.9%, $738–744 | **17.0–17.5%, $725–735** (upper bound: H2 already assumes the 2028 digestion) |
| H3 / H2 / H4 baskets (10.2 / 21.6 / 0.9%) | unchanged | — | — | **9.0–9.4 / 20.1–20.7 / −2.6%** |
| E basket 8.1% (cash only / with lower D&A) | unchanged | not meaningful (revenue would not hold at 650) | 8.3% / 9.0% | **8.5% / 9.7%** |
| Microsoft 9.6% / Alphabet 9.1% / Amazon 5.2% (capex = share of K1) | unchanged | — | — | **9.8–10.4% / 9.4–10.3% / 5.6–6.7%**; P_k +$3–11 / +$2–9 / +$3–10; all still fail k |
| All six, cap-weighted (10.0%) | 10.0% | — | — | **~8.7–9.6%** |
| Maintenance per update | Lowest: one line | High: re-run each quarter; `[A]` inputs move the path | Medium: classify the regime each time | Medium once (a new section); then the indicator table at the hyperscalers' quarterly reports, which are already register events; the gauge annually or when K1 moves. No new update events |

**The guidance gap, which C would use** (initial guide → realised):

| Year | Company | Initial guide | Realised | Gap |
|---|---|---|---|---|
| 2019 | Facebook | $18–20bn `[E]` | $15.1bn `[F]` | −21% |
| 2023 | Meta | $34–37bn (Q3-22) `[E]` | $28.1bn `[F]`/`[E]` | −21% |
| 2024 | Meta | $30–37bn `[E]` | $39.2bn `[F]` | +17% |
| 2025 | Alphabet / Meta / Microsoft (FY25) | $75bn / $60–65bn / $80bn `[E]` | $91.4bn / $72.2bn / ~$88bn incl. finance leases `[F]`/`[E]` | +22% / +16% / +10% |
| 2026 | Amazon / Alphabet / Meta / Microsoft | $200bn / $180bn / $125bn / "$140bn+" `[E]` (S18) | ~$220bn / $195–205bn / $135–145bn / ~$170bn (guides after Q3) `[E]` | +10% / +11% / +12% / +21% |

The initial guides are as reported at the time `[E]` and were not re-read in filings here.

## 8. Recommendation

**Option D: a cycle-first K1 section, built like the H2 Memory cycle section, with the return gap as
its standing durability gauge.** On today's evidence it sets the Base as below.

| K1, USD bn | 2025 | 2026 | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| Bear | — | 790 | 950 | 800 | 820 |
| **Base, proposed** | ~435 | 790 | **1,120** | **1,170** | **1,170** |
| Base, today | ~435 | 790 | 1,120 | 1,250 | 1,300 |
| Change | — | — | 0 | **−80 (−6.4%)** | **−130 (−10.0%)** |
| Growth, proposed (today) | | | +42% (+42%) | **+4.5%** (+12%) | **0%** (+4%) |
| Base range, proposed | | 770–810 | 1,050–1,200 | **1,000–1,350** | **950–1,400** |
| Bull | — | 790 | 1,300 | 1,550 | 1,700 |

**Why it beats the alternatives:**
- **Against A:** A keeps a +12% "digestion" year without a test. Both earlier hyperscaler surges
  ended in a flat year. The Base's own E2 slows by 25–28 pp from 2026 to 2028, about as much as
  AWS's 24 pp slowdown of 2021–23 (+37% → +13% `[F]`) that came with the 2023 cut. And on the Base
  paths the AI base earns ~2% pre-tax in 2028.
- **Against B:** a return constraint would put Base below the Bear. It would mechanise an
  `[A]`-heavy calculation, and history says capex does not turn on computed returns.
- **Against C:** the guidance gap changes sign with the regime, so C hides a cycle call. A 50/50
  mixture is not a path anyone expects.
- **D answers the user's point directly.** Base becomes the most likely path:
  - contracted where contracts exist (2027);
  - judged on the cycle and the return gauge beyond that (2028–29);
  - with the evidence for and against shown, and the price-implied path beside it.

  It is the same form the user set for memory on 1 Nov.

**Why 1,170 and flat, and not lower:**
- 2028 +4.5% is at the top of the two earlier digestion years (+4%, −2%). The top, because:
  the backlog due in 2028 (Google Cloud 55% within 24 months; AWS 6.1 years) and NVIDIA's flat but
  not falling FY28–29 supply commitments support growth above zero.
- 2029 is flat: no backlog evidence reaches it, and the return gap is at its widest.
- The plateau is close to the bottom-up implied by the three analysed platforms with Meta and Oracle
  at the same growth (~1,150 / 1,175; 3.1).
- An absolute cut is the Bear's mechanism (financing break), and nothing signals it yet: prices are
  rising, IG spreads are 0.91% and the labs are funded through 2027.

**What stays:**
- 2026 and 2027: contracted.
- Bear 950 / 800 / 820: the break.
- Bull 1,300 / 1,550 / 1,700.
- E1, E2 and T1: the plateau is digestion of capacity, not a demand shortfall.

**Knock-on rows, set by the update run itself** (expected sizes from section 7; this baseline is the
only place they are set):

| Row | Today | Expected | Note |
|---|---|---|---|
| H1 2028 / 2029 (USD bn) | 800 / 825 | ~750 / ~745 | H1/K1 ratio held (0.640 / 0.635) |
| H1 EPS 2028 / 29 / 2030 | .98 / 1.00 / .97 | ~.91 / .88 / .87 | Revenue-mapped, as in the H1 review; above the 0.05 rule |
| H3 index 2028 / 2029 | 140 / 151 | ~138 / ~147 | 20–30% pass-through; below the rule for the EPS path (re-test) |
| H4 index 2028 / 2029 | 138 / 144 | ~129–134 / ~130–137 | Data-centre infrastructure follows long-lived capex; H4 is 2% of the six |
| E cash conversion 2028 / 2029 | .00 / .20 | ~.11 / ~.36 | Capex saving after tax; recalibrate on the company analyses |
| Monetisation ratio 2028 / 2029 | 0.22 / 0.28 | 0.24 / 0.31 | Same E1, lower K1 |
| H2 | — | Unchanged | The Memory cycle Base already assumes AI capex digestion in 2028; the K1 plateau is that digestion, so H2 moves only on its own evidence |

**Downstream, for the register when applied:**
- `--changed yes`; `--affects` nvda, tsm, msft, googl, amzn, dnb-teknologi,
  global-index-funds and the equity loop.
- The memory analyses (mu, skhynix, samsung, kospi) read K1 only as context, and H2 does not move.
- The register itself is not edited here.

**Evidence that would change the recommendation:**

| Evidence | Would point to |
|---|---|
| First 2027 capex figures (late Jan–early Feb 2027) summing to > 1,250, or a first 2028 view of "continued strong growth" from three of five | Later digestion: back toward 1,250 / 1,300 |
| GPU rental indices still rising through mid-2027, the B200 curve flipping to contango, and K4 backlog growing > 10% q/q | Later digestion |
| AI revenue disclosures that lift the attributed supply above ~800bn for 2028 (coverage > 90%) | The gauge no longer argues for a plateau |
| A platform guiding next-year capex flat or down, or Meta or Oracle cutting | Earlier or deeper: toward 1,120 flat, or the Bear if funding breaks |
| B200 index −20% from its 2026 high for three months, with FCF after returns below −$50bn a quarter twice | Earlier digestion, deeper 2029 |
| The Anthropic IPO pulled or below the Series H; OpenAI unable to raise for 2028 | The Bear (financing break), not the Base |

## 9. Proposed text (not applied)

### 9a. `.claude/skills/ai-market-bbb/SKILL.md` (revision 2026-11-DD.1)

**(1) Change note (after the revision line):**

```markdown
Change note 2026-11-DD.1: **K1 capex cycle** section and **K1 return gauge** added (Step 1b, Output,
Checks; `references/k1ret.py`), from `docs/review-ai-k1-sustainability.md` Option D. K1 Base is the
most likely path, not guidance or consensus by default: guidance sets the current year, contracts
the next, and the cycle judgement the years after. No row, scenario or basket-method change.
```

**(2) Rows, Money in, K1, column "Role":** replace "Core; the anchor series" with:

```markdown
Core; the anchor series. Base = the most likely path (Step 1b): current year on guidance, next year
on contracts, later years on the K1 cycle judgement; never guidance or consensus by default
```

**(3) Definitions: add two rows:**

```markdown
| **K1 return gauge** | Pre-tax return on the AI asset base (K1 above a non-AI baseline, by monthly vintage, including construction in progress), and the coverage of the AI revenue needed for 10% pre-tax, on the Base E-paths (E2 above a 10% trend from 2023, T1 seats, Meta above-trend revenue as an upper bound). Parameters from filings: short-lived share and lives, cash cost ratio (AWS, CoreWeave). `references/k1ret.py`. A durability gauge for the judgement, never a path-setter |
| Digestion (K1) | A year of capex growth between −5% and +5% after a surge without a financing break (2019 +4%, 2023 −2%). An absolute cut beyond that is the Bear's financing break |
```

**(4) Data discipline: add after "Guidance is `[E]`":**

```markdown
- **K1 years after the current one** state the contracted share (backlog due within 24 months,
  supplier and lease commitments) apart from the plan; beyond the contracted year the Base comes from
  the K1 cycle judgement (Step 1b).
```

**(5) Procedure: add after Step 1:**

```markdown
**Step 1b — K1 capex cycle, every full update.** The K1 Base beyond the contracted year is a judgement,
not a plan. Answer, with dated and tagged evidence:
1. **Where is the cycle?** One table: capex growth and capex ÷ OCF; FCF after dividends and buybacks;
   debt, equity and leases raised; D&A growth against revenue growth (AWS and the five); cloud and
   segment margins; GPU rental indices (Silicon Data H100, B200) and their term curve; K4 backlog
   q/q; customer concentration (labs in backlog); management language on returns; suppliers'
   commitments.
2. **Past cycles:** telecom 1996–2002, shale 2010–16, hyperscalers 2017–19 and 2020–23. Run-up, what
   turned it, lag and fall, against the current cycle.
3. **The return gauge** (`k1ret.py`): coverage and pre-tax return for 2027–29 on Base, with the
   sensitivities (r 8/12%, cash cost 35/45%, life 4/6 years, strict attribution, E2 Bull).
4. **Judgement against Base** for the year after the contracted one and the last window year:
   timing (earlier or later digestion) and depth, with evidence for and against. A point moves only
   by the minimum change (5% of the capex level). 25/50/25 stays a convention.
5. **What the price implies:** the H1 and E basket multipliers on Base 2028–30 for k, and NVIDIA's
   and TSMC's from their analyses.
6. **Signposts with dates.**
```

**(6) Output template: add after "Interface — money in":**

```markdown
## K1 capex cycle (five lines; where; past cycles; return gauge; judgement; price-implied; dated signposts)
```

**(7) Checks before finishing: add:**

```markdown
- K1 capex cycle updated: indicator table dated, the return gauge re-run when K1 or E2 moved, a
  judgement for the years after the contracted one, signposts with dates.
```

**(8) Files:** add `k1ret.py` (the return gauge; this review's `ret.py` + `ret2.py`) to the
references list and the README.

### 9b. `docs/ai-market-bbb.md`

**(1) Interface — money in: replace the K1, growth and range rows with:**

```markdown
| **K1 Hyperscaler capex** (MSFT, GOOGL, AMZN, META, ORCL) | ~435 `[A]` | **790** `[E]` | 950 / **1,120** / 1,300 | 800 / **1,170** / 1,550 | 820 / **1,170** / 1,700 |
| Growth y/y | ~+84% → 2026 | | +20% / **+42%** / +65% | −16% / **+4.5%** / +19% | +3% / **0%** / +10% |
| Base range | | 770–810 | 1,050–1,200 | 1,000–1,350 | 950–1,400 |
```

**(2) Replace the bullet "2028–29 Base slowdown" with:**

```markdown
- **2028–29 Base: a digestion plateau (K1 capex cycle section).** The 2027 build is contracted. After
  it, Base holds K1 at ~1,170 (2028 +4.5%, 2029 flat) `[A]`:
  - both earlier hyperscaler surges ended in a flat year (2019 +4%, 2023 −2%) `[F]`;
  - E2 slows by 25–28 pp from 2026 to 2028 on its own Base, about as much as AWS before the 2023
    cut;
  - on the Base E-paths the AI asset base earns ~2% pre-tax in 2028 and ~0% in 2029 (return gauge;
    coverage of the 10% need 69–70% and 60–63%);
  - NVIDIA's supply commitments are flat in FY28–29 `[F]`.
  An absolute cut is the Bear (financing break). Was 1,250 / 1,300 until DD Nov 2026
  (`docs/review-ai-k1-sustainability.md`).
```

**(3) New section after "Interface — money in":**

```markdown
## K1 capex cycle (DD Nov 2026)

**The cycle in five lines:**
1. **Where:** the fourth year of the build (five's capex ~165 → ~262 → ~450 → ~815, 2023–26).
   Capex is 116% of OCF (Q3-26); FCF after dividends and buybacks −48.8bn in Q3. D&A grows 44–90%
   y/y against revenue 19–39%. GPU rental prices still rise (B200 +27.6% year to date), the term
   curve is backwardated. Backlog +3% q/q (Microsoft flat).
2. **Return gauge:** on Base K1 and the Base E-paths the AI asset base earns ~12% pre-tax in 2026,
   ~6% in 2027, ~2% in 2028, ~0% in 2029. Revenue needed for 10%: ~880bn (2028), ~1,230bn (2029)
   against ~600bn and ~740bn delivered (coverage 69% / 60%; 49–71% across sensitivities). The gap is
   locked in by the 2026–27 build; it sets the depth of the eventual digestion, not its date.
3. **Past cycles:** returns lagged spending for 4–5 years (telecom) and 10 (shale); capex turned on
   equity, price, credit or revenue growth, in none of the four on a computed return. Hyperscaler surges ended in a
   flat year (2019 +4%, 2023 −2%).
4. **Judgement against Base:** 2027 contracted (1,120). 2028–29 a plateau (1,170 / 1,170). Risk
   later (AWS "over 40%" in 2027–28, rising rental prices, guidance beats of +10–22% in boom years)
   and deeper (funding of two labs, Meta and Oracle carrying the growth, siting).
5. **Price:** the H1 basket needs 1.02× Base 2028–30 for k; NVIDIA 0.78× (its analysis); TSMC 1.07×;
   the E basket 1.11×.

[Tables: where (section 6 of the review), past cycles (section 5), return gauge (4.2–4.4),
judgement, dated signposts.]
```

**(4) Monetisation ratio, Base:** 2028 **0.24** (was 0.22), 2029 **0.31** (was 0.28).

**(5) Scenario definitions, Base row, "Mechanism":**

```markdown
2027 capex +42% on backlog and supply limits; 2028–29 a digestion plateau (+4.5%, 0%) while the
2026–27 build earns in; lab revenue ~3.6× by 2029; memory normalises
```

**(6) Signposts and monitoring: add rows:**

```markdown
| **K1 2027 first figures** (late Jan–early Feb 2027) | < 1,000 (Bear) / > 1,300 (Bull); 1,050–1,250 confirms Base | Five not yet guided; 2026 ~815 on actuals and Q4 guides | Company reports |
| **K1 return gauge** (at the January roll-forward, and when K1 or E2 moves) | Coverage of the 10% need in 2028 < 60% / > 90% | 69% (2028), 60% (2029) on Base K1; 70% / 63% on the plateau | This baseline (`k1ret.py`) |
| **GPU rental indices** (Silicon Data H100, B200; monthly) | B200 −20% from its 2026 high for three months / still rising with the curve in contango into mid-2027 | B200 $5.62 (1 Sep, +27.6% year to date; 12-month 5.39); H100 $2.75 (27 Jul) | Silicon Data `[E]` |
| **FCF after shareholder returns (five)** | < −50bn a quarter for two quarters with E2 growth slowing / positive | −48.8bn (Q3-26); −66.7bn TTM | Filings `[F]` |
```

**(7) Change log entry:**

```markdown
- **DD Nov 2026 — K1 Base 2028–29 re-set (method: K1 capex cycle, skill 2026-11-DD.1).** K1 Base
  1,250 / 1,300 → **1,170 / 1,170** (digestion plateau); 2026–27, Bear and Bull unchanged. Evidence
  and arithmetic in `docs/review-ai-k1-sustainability.md`. Knock-on: H1 2028–29, H1 EPS 2028–30,
  H3 and H4 indices, E cash conversion, monetisation ratio (re-set in this update). H2 unchanged.
```

## 10. Open data gaps

| Gap | Why it matters | When it may close |
|---|---|---|
| AI revenue by company, consistently defined `[?]`: Microsoft last gave $37bn (Mar 2026), AWS "> $25bn" (Jun 2026), Google no dollar figure | The supply side of the gauge is an attribution, about twice the disclosed run-rates | Q4 calls (late Jan–early Feb 2027) |
| The return on internal AI use (Meta's ranking, Google's Search and Gemini, training runs) `[?]` | It decides how much of the gap is real. Meta is counted as an upper bound, Google not at all | Not disclosed; Meta's ad pricing and impressions are the proxy |
| Short-lived share and in-service lag per company `[E]`/`[A]` | Life and share move the 2029 coverage by −7 to +2 pp | Alphabet calls quarterly; Microsoft and Amazon partial |
| Economic life of accelerators `[E]` | Four years against 5.5 moves the 2029 return from ~0% to −5% | The rental indices only start in 2025–26; Amazon's 6 → 5 shortening is the only filed move back |
| Meta and Oracle 2027 capex `[?]`; no company analyses | They carry the K1 growth after 2027 (3.1) | Q4 calls; a Meta analysis (open checkpoint 9) |
| The guidance history (initial guide → realised) is from press reports of the calls `[E]` | Option C rests on it; D uses it only as context | Re-read in the filings if C is ever reconsidered |
| Cash cost ratio of AI revenue: only AWS and CoreWeave `[F]` | ±5 pp moves coverage by ±5 pp | Oracle OCI and Microsoft segment disclosure |
| Lab share of backlog: Microsoft's OpenAI share not given `[?]` | Concentration of the return | Microsoft 10-K |

## Sources

| # | Source | Used for |
|---|---|---|
| S1 | `docs/ai-market-bbb.md` (1 Nov baseline; Update 7, 7 Nov; note of 11 Nov) | K1–K4, E1, E2, T1, ratio, scenarios, signposts, K3 funding facts, NVIDIA supply commitments, Memory cycle |
| S2 | `.claude/skills/ai-market-bbb/SKILL.md` (2026-11-06.1) | How K1 Base is set; rules (minimum change, one place, Bear) |
| S3 | Alpha Vantage `CASH_FLOW`, `INCOME_STATEMENT` (quarterly and annual, filings-normalised), MSFT, GOOGL, AMZN, META, ORCL, fetched 11 Nov 2026 | Capex, D&A, OCF, dividends, buybacks, revenue, operating income 2016–Q3 2026; debt from `BALANCE_SHEET` `[F]` (Microsoft's quarterly D&A in this feed includes "other" and is not used) |
| S4 | Amazon 10-Q Q3 2026, R53, R56, R57, R58: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/R53.htm | AWS segment revenue, operating income, PP&E, additions, D&A `[F]` |
| S5 | Amazon 10-K 2025 (R23, R87, R91, R92, R93): https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/R87.htm; 10-K 2023 (R84, R88, R89, R90): https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/R88.htm | AWS history 2021–2025; useful-life policy and changes `[F]` |
| S6 | Alphabet 10-K 2025 (R31, R70, R90): https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R90.htm | Segment results 2023–25; lives; PP&E components, assets not yet in service `[F]` |
| S7 | Microsoft 10-K FY2026 (R46, R61, R62, R107): https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R107.htm | Segment results FY24–26; lives; PP&E; depreciation $15.2 / 22.0 / 34.3bn `[F]` |
| S8 | Meta 8-K Ex. 99.1, Q3 2026: https://www.sec.gov/Archives/edgar/data/0001326801/000162828026066700/meta-09302026xexhibit991.htm | Margins, legal charge, capex, FCF, D&A, debt, outlook `[F]` |
| S9 | CoreWeave 8-K Ex. 99.1, Q3 2026: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000461/coreweave3q26earningspress.htm | Pure-play AI cloud cost structure `[F]` |
| S10 | `docs/msft-analysis.md` v3, `docs/googl-analysis.md` v2 (7 Nov), `docs/amzn-analysis.md` v2 (11 Nov), `docs/nvda-analysis.md` v1.3, `docs/tsm-analysis.md` v1.2 | Company capex paths and K1 shares, D&A paths, Base IRR, V_T, P_k, exit P/E, shares; Microsoft depreciation 11.1 vs 7.1; OpenAI 10.8%; Alphabet notes 5.55%; price-implied multipliers |
| S11 | `docs/review-ai-h1-non-k1-funding.md` and its scripts | Shock method; NVIDIA, TSMC, Micron bases and pass-through |
| S12 | FRED: `C275RC1A027NBEA`, `C319RC1A027NBEA`, `DGS10`, `BAMLC0A0CM` | Telecom and shale investment `[F]`; 10-year 4.88%, IG OAS 0.91% (9 Nov) `[F]` |
| S13 | Couper, Hejkal and Wolman, "Boom and Bust in Telecommunications", Richmond Fed Economic Quarterly 89/4 (2003): https://www.richmondfed.org/-/media/richmondfedorg/publications/research/economic_quarterly/2003/fall/pdf/wolman.pdf | Telecom run-up, losses, turn, timing `[E]` |
| S14 | IEEFA on shale free cash flow (search excerpt; report not read in full): https://ieefa.org/media/327/download | Negative FCF every year 2010–19, ~$189bn for 34 producers `[E]` |
| S15 | Silicon Data: https://www.silicondata.com/blog/b200-rental-price-august-2026-update; https://www.silicondata.com/blog/h200-vs-h100-rental-prices-may-july-2026 | B200, H100, H200 rental indices and term curve `[E]` |
| S16 | Microsoft FY26 Q3 release coverage: https://news.microsoft.com/source/2026/04/29/microsoft-cloud-and-ai-strength-fuels-third-quarter-results/ (via search); Amazon Q2 2026 call: https://www.fool.com/earnings/call-transcripts/2026/08/07/amazon-amzn-q2-2026-earnings-call-transcript/ (search excerpt, not read) | AI run-rates `[E]` |
| S17 | Fortune on Zuckerberg (19 Sep 2025): https://dc.fortune.com/2025/09/19/zuckerberg-ai-bubble-definitely-possibility-sam-altman-collapse; CNBC via NBC DFW on Pichai: https://nbcdfw.com/news/business/money-report/techs-splurge-on-ai-chips-has-companies-in-arms-race-thats-forcing-more-spending/3601313 | Management language `[E]` |
| S18 | Platformonomics, "Follow the CAPEX 2025 Retrospective": https://platformonomics.com/?p=34926 | 2025 capex incl. finance leases (four 416bn; 2024 251bn); 2026 initial guides `[E]` |
| S19 | Meta Q4 2022 8-K: https://www.sec.gov/Archives/edgar/data/1326801/000132680123000008/meta-12312022xexhibit991.htm; Converge Digest: https://convergedigest.com/meta-trims-capex-plans/ | Meta's 2023 guidance path `[F]`/`[E]` |
| S20 | Alphabet 10-K FY2023: https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm; Deep Quarry on Amazon's server lives: https://deepquarry.substack.com/p/amazon-revises-server-lifespan-amid | The $3.9bn effect `[F]`; Meta and Amazon effects `[E]` |
