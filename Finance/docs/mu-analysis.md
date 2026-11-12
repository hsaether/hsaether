# Micron Technology (MU) — IAF analysis, stub Q4 2026 + 2027–2029

> **5 Nov 2026 — version 3, price re-mark (light update; the verdict flips from fails to clears).**
> Skill used: **iaf-valuation 2026-11-01.1**. Micron closed at **$656.39** on 5 Nov (Nasdaq; −17.5%
> on the day from $795.23; −23.4% from v2's $856.49; Yahoo `get_quote`, 21:00 UTC). The cause is a
> sector sell-off on fears that the Democratic sweep in the 3 Nov midterms slows the US data-center
> build (SOX −12.2% on Yahoo's close; ~−10% intraday in the AI BBB). No company news; no filing
> since 22 Oct in FinancialFilings.
> - **Upstream read:** AI Market BBB 5 Nov notes (a price event; H2 EPS path, revenue index, exit
>   P/E 8 / 10 / 11 and cash conversion unchanged; state siting policy added as a Bear signpost;
>   memory multiplier re-marked: basket 0.80×, **Micron 1.05×** Base 2028–30 for k, was 1.43×;
>   memory basket Base 19.4%). HY Market BBB 5 Nov (NIBOR path unchanged; HY Base window
>   6.8% → **7.2%**; market reference E / R 0.196 → **0.254**). Equity BBB unchanged (17/18 Oct).
> - **Model blocks kept:** no input above moves the EPS path, capex, payout, exit P/E or the NOK
>   path. Only the price, the valuation date (22 Oct → 5 Nov; T 3.19 → 3.16 years, stub 70 → 56
>   days) and the net cash at the valuation date (~$74bn → ~$79bn, two weeks of FQ1 FCF `[A]`) move.
> - **Before → after:** Base IRR **6.3% → 18.3%**; P_k **$748.3 → $751.6** (the shorter discount
>   period only); margin of safety **−12.6% → +14.5%**; verdict **fails → clears**. Bear −11.0% →
>   −1.7% (capital −26.6% → −4.3%); Bull 18.3% → 32.0%.
> - **Decision rule kept:** this analysis has not been set up cycle-first (Step 7; the AI BBB says
>   it "may" lead with the Memory cycle section). Micron is not held, so the existing rule stays:
>   Base margin of safety against k, with E / R as a reference row. The AI BBB's cycle read is
>   quoted in the Summary as context.

> **4 Nov 2026, kept unchanged (change gate):** read AI Market BBB Update 6 of 1 Nov (H2 path, exit P/E and scenarios unchanged; its new Memory cycle section prices Micron at 1.43× Base 2028–30) and the HY funds analysis of 31 Oct (HY market reference unchanged at 0.196). No figure in this analysis changes.

> **29 Oct 2026, kept unchanged (change gate):** read AI Market BBB Update 5 of 29 Oct; the H2 memory path, exit P/E and scenarios are unchanged. No figure in this analysis changes.

**Version 3 — 5 Nov 2026** (price re-mark on the 5 Nov close; iaf-valuation 2026-11-01.1; inputs
as in the note above). The build below is version 2's; every figure that depends on the price or
the valuation date is re-marked, and the rest is unchanged.

**Version 2 — 22 Oct 2026** (version 1: 16 Oct). Skill revisions used: **iaf-valuation
2026-10-18.2** (v1: 2026-10-11.3; the new exit cross-check against the equity market and the
Tracking section are added here). Trigger for this version: Micron's technology webinar of 21 Oct
2026 (user input), the AI BBB Update 3 and the new equity and HY baselines, and the price
($931.24 → $856.49). Sector inputs:
- `docs/ai-market-bbb.md`, **Update 3 of 22 Oct 2026**, produced with ai-market-bbb rev
  **2026-10-22.1**. It supplies:
  - the **H2 memory layer**: EPS path (CY27 consensus = 1.00; **unchanged since 12 Oct**), exit
    P/E reference 8 / 10 / 11, cash conversion and the Track B instruction;
  - the scenarios and catalysts (financing break and memory overshoot / contracted build then
    digestion / agentic adoption);
  - the H2 revenue index (reconciled to the EPS path on 16 Oct, used as a check), memory signposts
    (DRAM contract prices, CXMT), and the H2 basket return and P/E for comparison.

  Its note for this analysis: "no new flag". This analysis makes no memory market forecast of its
  own.
- `docs/equity-market-bbb.md` (17 Oct 2026, amended 18 Oct; produced with equity-market-bbb rev
  2026-10-18.5, skill now 2026-10-18.6; stale after 10 Nov). It supplies:
  - the macro scenarios the AI scenarios sit inside (Bear = recession H1 2027 + oil Bear; Bull =
    soft landing);
  - the USD/NOK path (**Base 9.41 flat; Bear 10.54 / 10.27 / 10.27; Bull 9.13**; NOK memo only,
    the decision is in USD at spot);
  - World Base **5.2%**, World E / R **0.024**;
  - the exit anchors for the new cross-check: World exit P/E **17** (15 / 18.5), exit P/B **3.14**
    (2.46 / 3.69), mid-cycle return **8.2%**.
- `docs/hy-market-bbb.md` (17 Oct 2026, amended 18 Oct; skill 2026-10-18.2) is read for the Base
  window NIBOR **4.38%** (E / R), the HY market Base **6.8%** a year and, via
  `docs/hy-funds-analysis.md` (18 Oct), the HY market reference E / R **0.196**. Micron is rated
  BBB+ with net cash; no refinancing test applies. The oil, rig, supply, shipping and defense
  baselines are not used.

## Summary

**Verdict (v3, 5 Nov 2026 close $656.39)**
- **Clears: the verdict flips from fails (v2) to clears.** Base IRR **18.3% a year** (USD; NOK the
  same in Base) against k = 12%. Hurdle price **P_k ≈ $752 vs P $656.39: margin of safety
  +14.5%** (v2: −12.6%).
  - The whole change is the price (−23.4% since 22 Oct, −17.5% on 5 Nov alone). P_k moves only
    with the shorter discount period ($748.3 → $751.6). No model block moved.
  - **Bear:** −1.7% a year in USD (+1.9% in NOK on the Equity BBB path); P_k (Bear) $473; capital
    is almost preserved (ΣD + V_T $628 against P $656, −4.3%). The Bear still fails k, but it no
    longer breaks the thesis in value the way it did at $856 (−26.6%).
  - **Bull:** 32.0% (P_k $992). P is below the Base hurdle, so the share of Bull priced is negative
    (−40%).
  - **What the price now allows** (Base still earns k down to any one of): an exit P/E of **8.0**
    on 2030 EPS (Base 10); **2030 EPS of ~$54**, 0.28 of CY27 consensus (Base $67, 0.35); or the
    2028–30 EPS path at **~0.85× Base** (own approximation `[A]`; the AI BBB basket method gives
    Micron 1.05× at its 5 Nov intraday prices). It returns 0% at an exit P/E of 4.8 or ~0.60× Base.
  - **Cycle context (AI BBB H2, 5 Nov; not the gate here):** late upcycle, Base turn in 2028
    kept; timing risk 1–2 quarters earlier, 2029–30 risk deeper. The memory basket now prices a
    turn ~20% below Base; Micron prices about Base. The new 2028 demand risk is state siting
    policy (a Bear signpost, no figure yet).
  - **E / R reference row:** 0.616 (E 13.9 pp over window NIBOR 4.36%; R 22.6 pp) against the
    current HY market reference **0.254** (HY BBB 5 Nov; `docs/hy-funds-analysis.md` still shows
    0.196 because the funds run is on hold). R shrinks at the lower price because the Bear's
    end-2027 mark (8 × 2028 EPS + cash) does not depend on the price.
  - **Re-mark triggers (the verdict reverts above these):** Base = k at **$752 (+14.5%)**;
    E / R = 0.254 at $770 (+17%); Base = HY market Base 7.2% at $840 (+28%). Bull hurdle $992.

*Version 2 verdict (22 Oct, $856.49), kept for the record:*
- **Fails, by less than on 16 Oct.** Base IRR **6.3% a year** (USD; NOK the same in Base) against
  k = 12%. Hurdle price **P_k ≈ $748 vs P $856.49: margin of safety −12.6%** (v1: −20.0%).
  - The whole improvement is the price (−8.0% since 15 Oct, −6.3% on 22 Oct alone). P_k is almost
    unchanged ($745 → $748).
  - **The webinar (21 Oct) changes no number in the model.** It is a technology roadmap with no
    guidance, prices, bits or capex. Its one hard supply fact cuts the other way from the bull
    case: 1δ DRAM (+mid-20s% bits per wafer) and G11 NAND (~2× bit density) both ramp in **2H
    2027**. That is more bit supply into 2028, which fits the AI BBB Base fall (see Webinar).
  - Micron is priced at **4.5× calendar-2027 consensus EPS** ($191.8; core 4.1×). The AI
    baseline's memory path takes earnings to **0.90 of that consensus in 2027, then 0.60, 0.40 and
    0.35 by 2030**. **Today's price is 12.8× the Base 2030 earnings** against an exit multiple of
    10.
- **The cash is real, but it does not reach k.** Base free cash flow is $123 / $78 / $46 a share in
  2027–29. Paid out under Micron's "return 100% of excess cash" policy, plus $35 of excess cash in
  2027, that gives ΣD ≈ $282 a share. On top, V_T ≈ $724 = 10 × $67.1 + net cash.
- **Bear breaks the thesis:** −11.0% a year in USD (−7.9% in NOK). The 2027 return is −29% (the
  price falls 42%, partly offset by the excess-cash payout), and capital is not preserved (ΣD +
  V_T is 27% below P).
  - The catalyst is the AI BBB financing break and memory overshoot inside the equity recession.
  - The balance sheet is never at risk: net cash, BBB+, and FCF positive every year (Bear
    $92 / $50 / $39bn).
- **Bull clears k:** 18.3% (P_k $988, +15.3%). 45% of the Bull hurdle is already priced (v1: 78%).
- **What the price needs** (any one of):
  - an exit P/E of **~12.3** on 2030 EPS (Base 10);
  - **2030 EPS of ~$83**, 0.43 of the CY27 consensus (Base 0.35);
  - earnings falling **only ~23% a year after 2027** (Base −27%).

  Micron's own view, "much tighter in 2027 and 2028" (EPS at consensus through 2028, 0.60 in
  2029, 0.45 in 2030), gives 18.7%: the bull case is still management's case.
- **Against World, its layer and HY:**
  - Base 6.3% is now **above MSCI World (5.2%)** but below the AI BBB memory basket (11.3% in NOK,
    21 Oct): Micron trades at 4.5× against 2.8× for SK hynix and 3.1× for Samsung.
  - **E / R = 0.069** (v1 −0.05): above World (0.024), below the HY market (0.196).
  - **Triggers:** Base = HY market Base 6.8% at **$846 (−1.2%)**; E / R = 0.196 at $792 (−7.5%);
    Base = k at **$748 (−12.6%)**, a core P/E of 3.6 on CY27 consensus, about where SK hynix and
    Samsung trade now.

**Decision table (USD, per share; v3, P = $656.39 Nasdaq close 5 Nov 2026; v2 at $856.49 in
brackets)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| Traded price (USD, Nasdaq) | $656.39 | **$656.39** | $656.39 |
| IRR_T (USD) / NOK memo | −1.7% / +1.9% (−11.0% / −7.9%) | **18.3% / 18.3%** (6.3%) | 32.0% / 30.4% (18.3% / 16.9%) |
| V_T (31 Dec 2029) | 435.9 | **723.6** | 1,001.8 |
| P_k (USD) / margin of safety | **$472.9** / −27.9% (−45.0%) | **$751.6 / +14.5%** (−12.6%) | **$992.2** / +51.2% (+15.3%) |
| Capital preserved? (ΣD + V_T vs P) | **No, just: −4.3%** (−26.6%) | Yes: +53.2% | Yes: +104.0% |
| Cumulative FCF per share 2027–29 (after growth capex) | 156.9 | **246.4** | 301.8 |
| Net cash per share at exit (ex customer deposits) | 52.2 | **52.2** | 52.2 |
| Balance sheet | Net cash $60bn; BBB+; FCF positive in every year; capex cut to $40bn / $35bn | Net cash $60bn kept, all FCF and $41bn of excess cash returned; capex $58–65bn a year | Capex $62–80bn a year still leaves FCF $68–156bn |

**Per-share path (USD; calendar years; EPS non-GAAP)**

| | Stub Q4-26 (6 Nov–31 Dec, v3) | 2027 | 2028 | 2029 | 2030 (exit-year EPS) |
|---|---|---|---|---|---|
| Base revenue ($bn) | 38.7 (CQ4 63.5 × 56/92) | 270 | 230 | 200 | (≈195) |
| Base EBITDA $bn / per share | 34.1 / 29.7 | 244 / 212 | 169 / 147 | 121 / 106 | |
| Base EPS | 24.1 (CQ4 39.62) | 172.6 | 115.1 | 76.7 | **67.1** |
| Base maintenance FCF per share (capex = D&A) | 18.6 (all FCF) | 162.9 | 120.3 | 80.6 | |
| Base growth capex per share (capex − D&A) | | 40.0 | 42.6 | 34.8 | |
| Base FCF after growth capex per share (no material debt amortisation) | 18.6 | 122.9 | 77.7 | 45.8 | |
| Base D_t (dividends + buybacks, paid) | — (ex-date 14 Oct passed) | 158.4 (incl. 35.5 excess cash) | 77.7 | 45.8 | |
| Base net cash per share (ex deposits; year-end) | 87.7 | 52.2 | 52.2 | 52.2 | |
| Base V_t (year-end; v3 interim glide) | 675.0 (price flat + stub cash) | 697.0 | 650.5 | 723.6 | |
| Bear EPS / FCF per share / V_t | | 115.1 / 79.7 / 513 | 57.5 / 43.6 / 436 | 48.0 / 33.6 / 436 | 48.0 |
| Bull EPS / FCF per share / V_t | | 191.8 / 135.6 / 928 | 153.5 / 107.3 / 934 | 105.5 / 58.9 / 1,002 | 86.3 |

The stub is shorter (56 days from the new valuation date); net cash at 31 Dec ($100.8bn,
$87.7/share) is unchanged because the FCF of 23 Oct–5 Nov now sits in the net cash at the
valuation date (~$79bn, $69.1/share `[A]`).

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value ·
`[E]` external or secondary · `[C]` carried from an earlier version · `[A]` own assumption ·
`[?]` not found or unverified.

## Header

| Item | Value |
|---|---|
| Company | Micron Technology, Inc., Nasdaq: MU. Fiscal year ends on the Thursday closest to 31 Aug (FY26 ended 3 Sep 2026, 53 weeks). FY26 revenue **$133.19bn** (+256%), non-GAAP gross margin 81.1%, non-GAAP operating income $101.2bn, non-GAAP EPS **$75.52** (GAAP $74.33) `[F]` (FQ4-26 release, 30 Sep 2026) |
| Price (P) | **$656.39**, Yahoo `get_quote` `MU`, Nasdaq close 5 Nov 2026 (regularMarketTime 21:00 UTC; −17.5% on the day from $795.23; day range $650.00–761.81; volume 75.0m against a 3-month average of 27.0m; after hours $657.11) `[F]`. Sector sell-off on the midterm result, no company news (AI BBB 5 Nov). v2: $856.49 (22 Oct); v1: $931.24. 52-week range $192.59–1,255.00 |
| Valuation date / exit date | **5 Nov 2026 (close)** / 31 Dec 2029, **T = 3.16 years** (stub 56 days). v2: 22 Oct, T = 3.19 |
| Shares | **1,149m diluted** (FQ4-26 non-GAAP; FQ1-27 guide "approximately 1.15 billion") `[F]`; 1,131.4m outstanding on 2 Oct 2026 (10-K cover; Yahoo the same on 22 Oct) `[F]`. Held flat: buybacks are counted as D_t (cash returned), not as per-share accretion (counted once). SEC EDGAR since the 10-K (9 Oct): Form 4 and Form 144 only (insiders), no 8-K, no share issue `[F]` |
| Market cap / EV | **$754bn** (diluted; v2 $984bn). **Net cash ex customer deposits ≈ $79bn at the valuation date** `[A]` ($69.1/share; v2 $74bn): $68.3bn at 3 Sep (cash and investments $73.5bn less debt $5.2bn) `[F]`, less $12.75bn of SCA customer deposits to be returned later `[F]`, plus ~9 weeks of FQ1 FCF (management: FQ1 FCF above FQ4's $33.2bn) `[A]`. **EV ≈ $675bn** |
| P/E | 5.5× CY26 EPS ($119.0: calendarised actuals + FQ1 consensus); **3.42× CY27 consensus ($191.8)** `[A]` (calendarised on 22 Oct from Yahoo FY27 $176.50 and FY28 $206.85; on 5 Nov Yahoo shows FY27 $176.50 and FY28 $207.76, which lifts CY27 by ~0.1% to ~$192.0: below rounding, not moved; the AI BBB has $192.10, see Sensitivities); core P/E (price less net cash) **3.06×** (v2 4.46× / 4.13×). Yahoo `priceEpsCurrentYear` on FY27: 3.72× (5 Nov) `[F]` |
| P/B | 5.4× (book value $138.4bn, $122.3/share, 3 Sep) `[F]`; v2 7.0× |
| NAVs (Step 3) | Not applicable (no tradeable asset marks for fabs). V_T is built on normalised EPS × an independent exit P/E + net cash (Step 3), with the exit cross-check against the equity market |
| FX | USD reporting and USD price: no conversion. NOK memo at USD/NOK **9.3094** (Yahoo `NOK=X`, 5 Nov 2026 21:05:59 UTC; user input 9.3095 at 21:05 UTC; v2 9.313 on 22 Oct), moved with the Equity BBB USD/NOK path relative to its 9.41 start (Bear +12% in 2027 and +9% after, Base flat, Bull −3%) |
| Track | **B** (cyclical, capital-intensive memory; the AI BBB's Interface to IAF: "H2 memory is Track B (cyclical; normalise to mid-cycle)"). FCF build per year, V_T on normalised mid-cycle EPS, P_k |
| k | **12%**, not raised: BBB+, net cash, very liquid. Concentration (top ten customers > half of revenue; majority of DRAM output in Taiwan) is priced in the Bear, not through k |
| Horizon | Stub CQ4-26 (6 Nov–31 Dec in v3; FQ1-27 ends ~3 Dec, report 23 Dec on Yahoo's estimate of 5 Nov, 16 Dec in the AI BBB signposts `[?]`) + 2027–2029 annual (calendar years); exit on 2030 normalised EPS |

**Sources (connector · document · period):**
- **v3 (5 Nov 2026):** Yahoo `get_quote` MU, `NOK=X`, `^SOX` (close 5 Nov; SOX 9,011.14,
  −12.2%); FinancialFilings `filings_list` (Micron id 29796, releases since 22 Oct: none; server
  date 3 Nov); `docs/ai-market-bbb.md` (5 Nov notes, Memory cycle sections 1–7);
  `docs/hy-market-bbb.md` (5 Nov change summary); `docs/equity-market-bbb.md` (17/18 Oct,
  unchanged).
- **Micron technology webinar, "Technology and products leadership for the AI era"** (IR PDF,
  21 Oct 2026, 33 slides, Scott DeBoer; text via `pypdf`) `[F]` for stated roadmaps and timing,
  which Micron calls "directional … subject to change". New in v2; see Webinar.
- **Micron FQ4-26 press release** (8-K exhibit 99.1, SEC, 30 Sep 2026, quarter ended 3 Sep 2026)
  `[F]`: revenue, margins, EPS, business units, cash flow, balance sheet, capital returns, dividend
  ($0.15, record 14 Oct, paid 29 Oct), FQ1-27 guidance.
- **Micron FQ4-26 prepared remarks** (IR PDF, 30 Sep 2026) `[F]`: DRAM / NAND, industry bit
  outlook, SCAs (26, > 35% of revenue through 2030, $32bn of customer commitments), RPO ~$150bn,
  fab timelines, capex, opex, tax, capital return from 9 Dec 2026.
- **Micron FY26 10-K** (SEC, filed 9 Oct 2026; WebFetch, partial) `[F]`: D&A $9.50bn, PP&E spend
  $30.71bn less incentives $3.32bn, customer deposits $12.75bn, equity $138.4bn, buyback
  authorization **$35.16bn** (8 Oct), shares 1,131.4m, DRAM $100.68bn / NAND $31.79bn in FY26.
- **SEC EDGAR submissions** (CIK 723125, 22 Oct): filings since 1 Oct (10-K, Forms 4 and 144).
- **Yahoo** (22 Oct 2026): price and closes 9–22 Oct, `earningsTrend`, `calendarEvents` (report
  23 Dec, estimate), `financialData` (target mean $1,560.57, 46 analysts; low $361, high $3,000).
- **Zacks:** news of 22 Oct (close $856.49; FY27 consensus $177.73, revenue $277.53bn; Rank 1; EPS
  estimate +11.6% in a month); research report of 7 Oct (ROIC 10-year median 11.1%, 5-year median
  P/S 3.25×) `[C]`.
- **FinancialFilings:** **not available** (monthly quota exhausted, 429 on 22 Oct; resets 1 Nov).
  The share-issue check was run on EDGAR instead.
- **Sector:** `docs/ai-market-bbb.md` (22 Oct 2026); `docs/equity-market-bbb.md` (17/18 Oct 2026);
  `docs/hy-market-bbb.md` and `docs/hy-funds-analysis.md` (17/18 Oct 2026).

## Scenario definitions (from AI Market BBB and Equity Market BBB)

| Scenario | Catalyst | What it does to Micron |
|---|---|---|
| **Base** (decision) | AI BBB: contracted 2027 build, then digestion; memory "2027 up on price, 2028–29 down as new capacity arrives (2017–19 analogue)". Inside the equity Base (AI boom slows to trend) | EPS on the H2 layer path × Micron's CY27 consensus ($191.8): **$173 / $115 / $77** (2027–29) and **$67** in 2030. Revenue $270 / 230 / 200bn `[A]`, net margin 73% → 44% → ~40% at mid-cycle. Capex $58 / 65 / 60bn. All FCF returned. Exit P/E 10 |
| **Bear** (stress) | AI BBB **financing break + memory overshoot 2028** (a lab misses commitments, AI credit tightens, 2028 hyperscaler capex −16%, DRAM contract prices fall) inside the equity Bear (recession H1 2027 + oil Bear). Earliest H1 2027 | EPS $115 / $58 / $48, and $48 in 2030 (layer 0.60 / 0.30 / 0.25 / 0.25). Revenue $200 / 140 / 130bn; capex cut to $52 / 40 / 35bn. Exit P/E 8, reached at end-2027 |
| **Bull** (stress) | AI BBB **agentic adoption** (lab revenue +130% in 2027, capex to $1.3–1.7tn) inside the equity Bull (soft landing). Earliest Q2 2027 | EPS at consensus in 2027 ($192), then $154 / $106, and $86 in 2030 (layer 1.00 / 0.80 / 0.55 / 0.45). Capex $62 / 75 / 80bn. Exit P/E 11 |

The stub (23 Oct–31 Dec 2026) is the same in all scenarios. It uses the FQ1-27 guidance and the
FQ2 consensus (CQ4-26 EPS $39.62 × 70/92), with price flat by convention. Bear and Bull diverge
from 1 Jan 2027.

## Company and status

- **The cycle in numbers** `[F]`:

| Fiscal year (to ~1 Sep) | FY22 | FY23 | FY24 | FY25 | **FY26** | FY27 consensus | FY28 consensus |
|---|---|---|---|---|---|---|---|
| Revenue $bn | 30.76 | 15.54 | 25.11 | 37.38 | **133.19** | 275.7 (40) | 318.7 (42) |
| Net income (GAAP) $bn | 8.69 | −5.83 | 0.78 | 8.54 | **84.97** | — | — |
| EPS (non-GAAP) $ | — | — | — | 8.29 | **75.52** | 176.50 (35) | 206.85 (36) |
| D&A $bn | 7.12 | 7.86 | 7.78 | 8.35 | **9.50** | | |
| Capex (gross PP&E) $bn | 11.18 | 7.68 | 8.39 | 15.86 | **30.71** (net 27.37) | | |

  FY22–25 from Zacks statements; FY26 from the release and 10-K; consensus from Yahoo, 22 Oct
  (analysts in brackets; FY28 EPS +1.2% since 15 Oct). Micron's ASPs have moved between about
  +200% and −50% a year over the last five years (10-K).
- **FQ4-26 (Jun–Aug 2026)** `[F]`:
  - Revenue **$54.23bn** (+31% q/q, +379% y/y).
  - **DRAM $39.8bn** (73%): prices up high-teens q/q, bits up mid-single digits.
  - **NAND $14.1bn** (26%): prices +~30%, bits +~10%; data-center SSD ~$10bn.
  - Gross margin **87.0%**, operating margin 82.3%, tax 15%, EPS $33.42.
  - OCF $44.0bn, capex $10.8bn, FCF $33.2bn; customer deposits received $12.3bn (financing, not
    FCF).
  - Inventory $10.4bn (129 days).
  - Business units: Cloud Memory $16.3bn (GM 83%, HBM-heavy), Core Data Center $18.0bn (90%),
    Mobile and Client $13.1bn (90%), Automotive and Embedded $6.8bn (84%).
  - About 60% of FY26 revenue came from data center (10-K).
- **Contracts** `[F]`:
  - **26 strategic customer agreements (SCAs)**, take-or-pay, estimated at **> 35% of revenue
    through 2030**. Three-quarters of that revenue has a defined pricing framework, mostly floor
    and ceiling bands; some agreements now extend into 2031.
  - **RPO ≈ $150bn** at committed volumes and minimum prices. "Even at floor prices, we expect
    margins meaningfully above any prior cycle peak margins."
  - Customer financial commitments **$32bn**, mostly cash deposits ($12.75bn on the balance sheet,
    returned in the latter half of each term).
  - **> 75% of 2027 output is already committed** (Zacks, from the call) `[E]`. The vast majority
    of 2027 HBM bits is contracted at significantly higher prices.
- **Market view (management, 30 Sep)** `[F]`:
  - Industry DRAM bits grow mid-20s% in CY26, then low-20s% in CY27 and CY28; NAND bits grow
    mid-20s% in CY27–28.
  - "Much tighter in calendar 2027 and 2028 than in 2026"; "we do not have line of sight to when
    supply and demand will return to balance."
  - HBM bits grow faster than conventional DRAM through 2028. Server units grow high-teens in
    CY26 and CY27.
- **Capacity** `[F]` (Micron's own additions; the AI BBB's 2028–29 fall rests on these and the
  industry's):

  | Site or node | First output |
  |---|---|
  | Singapore HBM packaging | early CY27 |
  | ID1 (Idaho) | mid-CY27 |
  | Tongluo (Taiwan) | mid-CY27 |
  | **1δ DRAM node (+mid-20s% bits per wafer vs 1γ)** | **ramp 2H CY27** (webinar) |
  | **G11 NAND node (> 400 layers, ~2× bit density vs G9)** | **volume ramp 2H CY27** (webinar) |
  | ID2 (Idaho) and Japan DRAM | late CY28 |
  | Singapore NAND | 2H CY28 |
  | New York | CY30 |

  More than $250bn is committed to US manufacturing and R&D (webinar; Zacks 9 Jul) `[F]`.
- **Capital** `[F]`:
  - Net cash $68.3bn (3 Sep) incl. $12.75bn of customer deposits; BBB+ at all three agencies.
  - Dividend $0.15 a quarter.
  - Buybacks of $650m in FY26. Authorization raised to **$35.16bn** on 8 Oct 2026.
  - "We intend to increase our capital return from Dec. 9, 2026 … Over time, we expect to return
    100% of our excess cash to shareholders."

### Webinar of 21 Oct 2026: what it says and what it changes

**What it contains** `[F]` (roadmap timing is "targeted high-volume manufacturing … directional
and subject to change"):

| Topic | Content |
|---|---|
| DRAM nodes | **1δ ramps in 2H 2027**, "fifth consecutive node of DRAM industry leadership", built in the US; **mid-20s% bit-density gain over 1γ**, "optimized cost". After it: 1ε in development, ζÅ / ηÅ pathfinding; high-NA EUV and wafer bonding; 3D DRAM in development |
| 4F² | "Not pursuing 4F² due to increased complexity/cost"; "over two decades of 4F² technology investigation, no viable scaling path" |
| NAND | **G11: > 400 layers, wafer-on-wafer bonding, ~2× bit density vs G9, volume ramp 2H 2027** |
| HBM roadmap | HBM4 (2026; 36 GB 12-high in volume since March), **HBM4E 2027, with custom base dies from HBM4E**, HBM5 2028, HBM5E 2029, HBM6 2030; vertical HBM (memory stacked on compute) and vEIM (edge inference memory) from about 2028 (illustrative); hybrid bonding and 16-high stacks |
| Customers | "Actively developing custom products with multiple CSPs"; LPDDR6 for data centers with Meta (joint white paper); 245 TB SSDs |
| Demand claims | HBM per GPU 3.6× from H100 to B300; memory per server 2× in three years; AI context length 30× a year; DRAM in an L4+ robotaxi > 10× an L2+ car |
| Productivity | AI in design: ~50–60% less time to tape-out and to customer-ready silicon (two SSD programs) |
| Long-horizon R&D | Micron Ventures $550m; $10bn on advanced lithography with Albany NanoTech / NY CREATES (5–10 years); Micron Research Labs (10+ years) |
| Financials | **None:** no guidance, pricing, bit or capex update |

**Assessment against the model** (input, not reference):
1. **No number moves the EPS path.** The deck is a technology and marketing piece. The demand
   claims are illustrative per-unit ratios, not bit or revenue forecasts. Under the AI BBB rule a
   path moves only on evidence that shifts a Base EPS point by ≥ 0.05; nothing here does.
2. **The supply facts support the Base fall in 2028 rather than management's "tight through
   2028".** Both new nodes ramp in 2H 2027: +mid-20s% bits per DRAM wafer and ~2× per NAND wafer.
   That bit growth comes without new cleanroom space, on top of ID1 and Tongluo (mid-27) and ID2,
   Japan and Singapore NAND (late 2028). Peers run similar node cadences. Management's industry
   bit outlook of 30 Sep (DRAM low-20s%, NAND mid-20s% in CY27–28) should already include this.
   The webinar does not raise it, but it shows where the 2028 supply comes from. The Base is
   kept.
3. **Cost per bit falls with 1δ.** That supports Micron's margin at mid-cycle relative to peers.
   The layer's 2030 level already implies margins above every prior peak (net ~40%), so this is
   not a sourced reason to move Micron above the layer.
4. **Custom HBM from HBM4E (2027), co-designed with several cloud providers,** makes HBM more
   contract-like and stickier. That is qualitative support for the SCA floors (> 35% of revenue
   through 2030), which already sit behind the Bear. No change.
5. **4F².** Micron says it found no viable path. That bears on the AI BBB's CXMT signpost: CXMT
   claimed a 4F² server DRAM on 13 Oct, which helped drive the memory sell-off. Micron is an
   interested party, so this is a competitor's view, not proof. The signpost stays "claim only"
   and the CXMT risk is not removed (see For other modules).
6. **R&D spend.** $10bn of lithography work over 5–10 years (~$1–2bn a year) plus the labs and
   Ventures is < 2% of Base FCF. It is taken as inside the FY27 opex step-up (+$2.5bn) and the
   capex path `[A]`; not modelled separately.

**The market's response:** the share rose 2.0% on 21 Oct and fell 6.3% on 22 Oct with the Nasdaq
(−2.6%). No company-specific cause was found (Zacks, web search), and the move fits Micron's beta
of ~2.2.

### Outlook (FQ1-27 guidance, 30 Sep 2026) `[F]`

| Item | Guidance | Consensus (Yahoo / Zacks, 22 Oct) |
|---|---|---|
| Revenue FQ1-27 (Sep–Nov 2026) | $61.5bn ± $1.5bn | $61.75bn (33) / $62.04bn |
| Gross margin (non-GAAP) | ~86.25%, "the floor for gross margins in fiscal 2027" | — |
| Opex (non-GAAP) | ~$2.06bn; FY27 opex +$2.5bn | — |
| EPS (non-GAAP) | $38.15 ± $1.00 on ~1.15bn shares | $38.28 (29) / $38.20 |
| FY27 | "another record year, with sequential revenue growth each quarter", "a more moderate rate of price increases" | FY27 EPS $176.50 (35) / $177.73 |
| Capex | FQ1 ~$11.5bn; 1H FY27 ~$25bn; higher in 2H; construction capex grows faster than equipment | — |
| Tax | ~15.5% | — |

## Near term: stub (all scenarios)

| USD | CQ4-26E (Oct–Dec; ≈ 2/3 FQ1-27 + 1/3 FQ2-27) | Stub v3 (6 Nov–31 Dec, 56/92; v2 23 Oct–31 Dec, 70/92) |
|---|---|---|
| Revenue $bn | 63.5 (FQ1 consensus 61.75, FQ2 consensus 67.12) | 38.7 (v2 48.3) |
| EPS (non-GAAP) | 39.62 | 24.1 (v2 30.1) |
| FCF $bn | ~35 `[A]` (NI 45.5 + D&A 3.0 − capex 12.2 − working capital) | 21.4 ($18.6/share; v2 26.8 / $23.3) |
| Dividend | $0.15 paid 29 Oct, **ex-date 14 Oct passed: not counted** | — |
| Net cash ex deposits, 31 Dec | ≈ $101bn `[A]` ($87.7/share) | |

- **FQ1-27 report (23 Dec, Yahoo estimate):**
  - Tests: revenue ≥ $61.5bn, gross margin ≥ 86.25%, FY27 capex, the size of the buyback from
    9 Dec, new SCAs, and DRAM / HBM pricing for 2027.
  - The model takes consensus for the stub; a beat moves the starting cash, not the path.
- **Before that:** SK hynix Q3 (28 Oct), Microsoft and Alphabet (28 Oct) and Amazon (29 Oct)
  capex, NVIDIA Q3 FY27 (17 Nov) and Q1-27 DRAM contract prices.

## Market input (AI Market BBB rows used and how they enter)

| Micron item | AI BBB row | Bear / **Base** / Bull | Company adjustment |
|---|---|---|---|
| **EPS** (calendar years; CY27 consensus = 1.00 = **$191.8**) | **H2 layer EPS path** (unchanged since 12 Oct) | 2027: .60 / **.90** / 1.00 · 2028: .30 / **.60** / .80 · 2029: .25 / **.40** / .55 · 2030 normalised: .25 / **.35** / .45 | None. The SCAs (floors on > 35% of revenue) and the webinar's custom HBM support the Bear floor but are not a sourced reason to deviate from the layer (Common assumptions; Webinar) |
| **Exit P/E** on 2030 EPS | H2 reference 8 / **10** / 11 | Used as the IAF exit multiple, anchored independently and cross-checked against World (V_T bridge) | — |
| Cash conversion (check) | H2 c, Base .70 / .65 / .60 | Micron model .71 / .67 / .60 | The AI BBB row is calibrated on this analysis |
| Scenario mechanism and signposts | Financing break, memory overshoot, CXMT, DRAM contract prices | As above | Micron SCAs, RPO and node ramps added as company signposts |
| Revenue (for working capital only) | H2 revenue index (2026 average = 100, reconciled 16 Oct): 100 / **138** / 150 · 72 / **118** / 133 · 67 / **103** / 118 | Used as a check: taken literally it gives Base 6.6% (Sensitivities) | Revenue path implied by the EPS path `[A]`: Base $270 / 230 / 200bn |
| Comparison | H2 basket (MU, SK hynix, Samsung): **Base 19.4% (NOK), P/E 2.79 on CY27 (5 Nov re-mark)**; v2 read 11.3% and 3.4 (21 Oct). Price-implied multiplier for k: basket 0.80×, Micron 1.05× Base 2028–30 (5 Nov, US intraday 19:36 UTC) | — | Micron at 3.42× CY27 (v2 4.5×) |

- **Calendar 2027 consensus.**
  - Micron's fiscal quarters end about a month before the calendar quarters, so CQ = 2/3 of the
    fiscal quarter that ends in it + 1/3 of the next. FY27 Q3/Q4 and the FY28 quarters are split
    as in v1 and scaled to the 22 Oct consensus.
  - **CY27 = $191.8** (CQ 43.7 / 47.4 / 49.9 / 50.9); CY26 = $119.0. The AI BBB has $192.10;
    on its figure Base is unchanged at 6.3%.
- **Both 16 Oct flags to the AI BBB are resolved:** the fiscal-year label error was fixed on
  16 Oct, and the reconciled H2 revenue index now fits Micron's run-rate (literal use: Base 6.6%,
  against −11.1% on the old index).
- **Equity Market BBB:**
  - The Bear is the recession world. In v2 Micron returned −28.6% in USD in 2027, about World's
    −28.4% in USD (−20.6% in NOK), with the price falling 42% ($880 → $513). **At the v3 price the
    Bear 2027 return is −7.0%** (end-2026 mark $675 → $513, −24%, plus $115 of payout): the 5 Nov
    fall has taken out more than half of the Bear's 2027 de-rating in advance.
  - The NOK memo uses the 17/18 Oct USD/NOK path.

## Common assumptions

- **EPS basis:** non-GAAP (Micron's and consensus basis; GAAP is ~1.6% lower in FY26: stock
  compensation and minor items). Tax ~15.5% inside the path.
- **Shares:** 1,149m diluted, held flat. Stock-based dilution (~$1.3bn a year) is offset by
  withholdings and buybacks, and **buybacks are D_t** (cash returned per share at today's count),
  so retained cash is counted once.
- **Payout** `[A]`:
  - Micron's stated policy, applied from 2027: dividends + buybacks = 100% of FCF.
  - Net cash ex deposits is held at **$60bn**, with the excess above it at end-2026 (~$41bn,
    $35.5/share) paid out in 2027.
  - Retaining everything instead changes Base by −1.0 pp (Sensitivities).
- **Customer deposits** ($12.75bn) are debt-like and excluded from net cash: they are returned
  toward the end of each SCA term, mostly after 2029. New deposits are financing and are not
  counted.
- **Capex (net of incentives)** `[A]` (unchanged; the webinar gives no capex figure):

  | Capex, $bn | 2027 | 2028 | 2029 | Basis |
  |---|---|---|---|---|
  | Base | 58 | 65 | 60 | FY27 guide 1H ~$25bn, higher 2H → FY27 ~$55bn; cleanroom construction for late-2028+ and the >$250bn US plan |
  | Bear | 52 | 40 | 35 | Equipment cut "appropriately with our demand"; construction continues |
  | Bull | 62 | 75 | 80 | |

  - **Maintenance capex = D&A** `[A]`: $12 / 16 / 20bn in Base, rising with the fab
    build-out. The rest is growth capex.
- **Working capital:** 15% of the revenue change `[A]` (receivables $36.2bn, inventory $10.4bn,
  payables $22.6bn at 3 Sep).
- **Revenue path** `[A]`, used only for working capital and as a margin check:
  - Base: $270bn (2027), $230bn, $200bn; ~$195bn in 2030 at a ~40% net margin.
  - Bear: $200bn, $140bn, $130bn. Bull: $293bn, $260bn, $230bn.
  - This implies a mid-cycle memory market about the size of 2026 at margins above Micron's
    prior peaks (FY18 net margin ~45%), which the SCA floors make plausible. **The 2030
    "normalised" EPS of $67 is about 8× FY25's $8.29; that is the AI BBB's structural-AI
    assumption.**
- **Exit P/E (independent of the IAF ceiling):** Base **10**, Bear **8**, Bull **11** on 2030
  normalised EPS.
  - The AI BBB memory reference is 10.
  - Mid-cycle memory has historically traded around high-single to low-double-digit earnings
    multiples, and the Korean peers trade at 2.8–3.1× peak CY27 earnings today `[A]`.
  - Cross-checks: the exit cross-check table (V_T bridge); **Zacks' 5-year median P/S of 3.25×**
    on Base 2030 revenue equals a P/E of 8.2 and gives 1.3% (Sensitivities). On that history, 10
    is not conservative.
- **Interim V_t:** P/E on next-year EPS glides linearly from today's core P/E on the scenario's
  2027 EPS to the exit P/E. v3: Base 3.40× → 5.60× (end-2027) → 7.80× (end-2028) → 10; Bull 3.06×
  → 5.71× → 8.35× → 11 (v2: Base 4.6 → 6.4 → 8.2; Bull 4.1 → 6.4 → 8.7). The Bear reaches 8 at
  end-2027. Plus net cash. This is a path diagnostic only and does not enter IRR_T.
- **NOK memo:** the Equity BBB USD/NOK path relative to its 9.41 start.

## Period tables and year-end path

**Year 1 (2027) by quarter** (EPS, USD; calendar quarters; haircut to calendarised consensus
`[A]`):

| | CQ1-27 | CQ2-27 | CQ3-27 | CQ4-27 | CY27 |
|---|---|---|---|---|---|
| Consensus (calendarised) | 43.7 | 47.4 | 49.9 | 50.9 | 191.8 |
| **Base** (0.98 / 0.93 / 0.87 / 0.83: Q1 largely contracted, prices +3–8% in Q1 per the AI BBB, then the turn) | 42.8 | 44.1 | 43.4 | 42.2 | **172.5** |
| Bear (0.85 / 0.62 / 0.50 / 0.46: recession H1-27, then the financing break) | 37.1 | 29.4 | 24.9 | 23.4 | 114.9 |
| Bull (at consensus) | 43.7 | 47.4 | 49.9 | 50.9 | 191.8 |
| Consensus revenue $bn (Base ×0.985 / 0.95 / 0.90 / 0.86) | 68.4 (67.4) | 72.6 (69.0) | 76.0 (68.4) | 77.6 (66.7) | 294.6 (271; 270 in the model) |

**Base** (USD bn unless per share):

| | Stub | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Revenue | 48.3 | 270 | 230 | 200 |
| Net income | 34.6 | 198.4 | 132.2 | 88.2 |
| EBITDA (margin) | 42.6 | 244 (90%) | 169 (74%) | 121 (61%) |
| Maintenance FCF / per share | 26.8 / 23.3 | 187.2 / 162.9 | 138.2 / 120.3 | 92.7 / 80.6 |
| Growth capex / per share | — | 46 / 40.0 | 49 / 42.6 | 40 / 34.8 |
| FCF after growth capex / per share | 26.8 / 23.3 | 141.2 / 122.9 | 89.2 / 77.7 | 52.7 / 45.8 |
| D_t paid / per share | 0 | 182.0 / 158.4 | 89.2 / 77.7 | 52.7 / 45.8 |
| Net cash ex deposits / per share | 100.8 / 87.7 | 60.0 / 52.2 | 60.0 / 52.2 | 60.0 / 52.2 |

**Bear and Bull** (lines that differ from Base):

| | Bear 2027 | 2028 | 2029 | Bull 2027 | 2028 | 2029 |
|---|---|---|---|---|---|---|
| Revenue | 200 | 140 | 130 | 293 | 260 | 230 |
| Net income | 132.2 | 66.1 | 55.1 | 220.4 | 176.3 | 121.2 |
| EBITDA (margin) | 165 (83%) | 90 (64%) | 79 (61%) | 270 (92%) | 223 (86%) | 162 (71%) |
| Capex | 52 | 40 | 35 | 62 | 75 | 80 |
| FCF after growth capex / per share | 91.6 / 79.7 | 50.1 / 43.6 | 38.6 / 33.6 | 155.8 / 135.6 | 123.3 / 107.3 | 67.7 / 58.9 |
| D_t per share | 115.2 | 43.6 | 33.6 | 171.1 | 107.3 | 58.9 |
| Net cash per share | 52.2 | 52.2 | 52.2 | 52.2 | 52.2 | 52.2 |

**Year-end path, v3** (USD per share; P $656.39 on 5 Nov; r_t from the end-2026 mark $675.0 =
price flat + stub cash $18.6; D_t at mid-quarter payment dates):

| | End-2026 | 2027 | 2028 | 2029 (exit) |
|---|---|---|---|---|
| **Base** D_t / V_t | — / 675.0 | 158.4 / 697.0 | 77.7 / 650.5 | 45.8 / **723.6** |
| Base r_t / IRR to year-end | | +26.7% / +28.6% | +4.5% / +18.0% | +18.3% / **+18.3%** |
| **Bear** D_t / V_t | — / 675.0 | 115.2 / 512.6 | 43.6 / 435.9 | 33.6 / **435.9** |
| Bear r_t / IRR to year-end | | −7.0% / −4.2% | −6.5% / −5.2% | +7.7% / **−1.7%** |
| **Bull** D_t / V_t | — / 675.0 | 171.1 / 928.4 | 107.3 / 933.5 | 58.9 / **1,001.8** |
| Bull r_t / IRR to year-end | | +62.9% / +62.4% | +12.1% / +39.4% | +13.6% / **+32.0%** |

- The Base path now rises in value while the cash comes out: the share pays ~$282 over three years
  and is worth ~$724 at exit, above today's $656. The 2027 jump is mostly the interim glide from
  today's low multiple (3.4× core) toward 10 (diagnostic only).

*v2 year-end path (22 Oct, end-2026 mark $879.8):* Base 158.4 / 787.9, 77.7 / 681.1, 45.8 / 723.6;
r_t +7.6% / −3.7% / +13.0%; IRR to year-end +9.4% / +3.7% / +6.3%. Bear r_t −28.6% / −6.5% /
+7.7%, IRR to exit −11.0%. Bull r_t +37.4% / +4.0% / +9.2%, IRR to exit 18.3%.

## V_T bridge (Base, per share) and exit checks

| Step | Per share |
|---|---|
| Price today (v3, 5 Nov) | **656.4** = core 587.3 + net cash 69.1 |
| Core at today's P/E (3.06× CY27 consensus) | 587.3 |
| − Base 2027 below consensus (×0.90) | −58.8 → 528.5 |
| − normalisation 2027 → 2030 ($172.6 → $67.1) at today's multiple | −323.0 → 205.5 |
| + multiple to the exit P/E 10 (from 3.06×) | +465.9 → **671.4** core |
| + net cash at exit (ex deposits; the excess and all FCF paid out) | +52.2 |
| **V_T** | **723.6** (unchanged) |
| Distributions over the horizon (ΣD) | 281.9 (unchanged) |

- **Reading (v3):** the peak-to-mid-cycle earnings fall (−$323 at today's multiple) is now more than
  offset by the multiple rising to the exit P/E (+$466). Today the market pays **9.8× the Base 2030
  earnings (8.8× core)**, below the exit P/E of 10 (v2: 12.8×, 11.8× core). v2 bridge: core 792.1
  → −79.2 → −435.6 → +394.2 → 671.4.

**Exit consistency** (Step 3; earnings basis = EPS):

| Row | Scenario | 2029 EPS | 2030 normalised EPS | Gap | Treatment | Tail per share |
|---|---|---|---|---|---|---|
| Micron EPS | Bear | 48.0 | 48.0 | 0% | Not material | 0 |
| | **Base** | 76.7 | 67.1 | **+14.3%** | **Named reason:** the AI BBB H2 path itself reaches 0.35 in 2030 ("2028–29 down as new capacity arrives"; Interface — EPS paths). Micron's ID2, Japan and Singapore NAND output starts late-2028 and New York in 2030 (prepared remarks); the 1δ and G11 nodes ramp from 2H 2027 (webinar). V_T is on the 2030 row | (8.7 as sensitivity) |
| | Bull | 105.5 | 86.3 | +22.2% | Named reason (same; Bull path to 0.45) | (17.3 as sensitivity) |

- With the 2-year reversion tail instead (v3): Base 18.7% (P_k $758), Bull 32.6% (P_k $1,004)
  (v2: 6.6% / $754 and 18.8% / $1,000).

**Exit cross-check against the equity market** (new in v2, iaf-valuation 2026-10-18.2; World
from `docs/equity-market-bbb.md`; Micron is not an Oslo listing):

| | Bear | **Base** | Bull | World (Bear / **Base** / Bull) |
|---|---|---|---|---|
| Exit P/E on 2030 normalised EPS | 8.0 (EPS 48.0) | **10.0** (EPS 67.1) | 11.0 (EPS 86.3) | 15 / **17** / 18.5 |
| Book at exit, $bn / per share (book + Σ (NI − D_t)) | 205 / 179 | **268 / 233** | 303 / 264 | |
| Exit P/B | 2.44 | **3.10** | 3.79 | 2.46 / **3.14** / 3.69 |
| ROE 2030 on exit book | 27% | **29%** | 33% | 16.4 / **18.5** / 19.9% |
| Buyer's implied return at exit: cash yield (c at exit ÷ P/E; c .70 / .60 / .55 from the H2 row) + long-run growth 4% `[A]` | 8.8 + 4 = **12.8%** | 6.0 + 4 = **10.0%** | 5.0 + 4 = **9.0%** | mid-cycle return **8.2%** |

- **Reading:** the exit P/E is 7–7.5 points below World's and the exit P/B is about World's, at an
  ROE ~10 points higher. A buyer at exit earns 9–13% against World's 8.2%. The exit is therefore
  not generous, and the extra return pays for memory's cyclicality (beta ~2.2). The sensitivity at
  the index return is not required (the buyer's return is above it). The 4% long-run growth is
  memory's nominal trend `[A]`; at 2% the Base buyer's return is 8.0%, about World's 8.2%.
- **P/B 3.1 at ROE 29%:** this is the AI BBB's structural mid-cycle (net margin ~40%). On
  Micron's own history (10-year median ROIC 11.1%) the same P/B would be far too high. That risk
  is the mid-cycle level, tested in the sensitivities (2030 EPS ×0.8: Base 0.7%).

## Growth capex test (Step 4)

- **Amount:**
  - Base capex 2027–29 is $183bn against D&A of $48bn, so **growth capex ≈ $135bn** (Bear
    $83bn, Bull $166bn).
  - It goes mostly to cleanroom space for output from late 2028 and HBM packaging. The 1δ and G11
    nodes add bits per wafer within the same capex.
- **ROIC_g, evidence:**
  1. **On the Base mid-cycle:** normalised net income of $77bn (2030) on invested capital of
     ~$221bn at exit (book $268bn less net cash $60bn plus deposits $12.75bn) is **~35%** after
     tax. In the Bear mid-cycle it is also ~35% ($55bn on ~$158bn: smaller earnings on a smaller
     book).
  2. **Through-cycle history:** Micron's **10-year median ROIC is 11.1%** (Zacks, 7 Oct), about
     k. Memory capacity has historically earned about its cost of capital over a cycle; today's
     58.5% is the peak.
  3. **Contracts:** SCA floors on > 35% of revenue through 2030 at margins "above any prior cycle
     peak", and $32bn of customer commitments, part-fund the build. Custom HBM from HBM4E
     (webinar) ties more of the new output to named customers.
- **Verdict:**
  - **Accretive on the AI BBB's mid-cycle** (ROIC_g ~35% > k); about value-neutral on Micron's
    own through-cycle history.
  - The test turns on whether the AI-era mid-cycle (EPS ~$67, ~8× FY25) holds. That is the AI
    BBB's assumption; it is not tested here.
  - The capacity's value is already inside the 2030 normalised EPS, so it is not added again.
- **Per share:** no new shares. Growth is funded from FCF, and buybacks continue.

## Results

**v3, P $656.39 (5 Nov 2026 close); v2 at $856.49 in brackets:**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (USD) | −1.7% (−11.0%) | **18.3%** (6.3%) | 32.0% (18.3%) |
| IRR_T in NOK (Equity BBB USD/NOK path) | +1.9% (−7.9%) | **18.3%** (6.3%) | 30.4% (16.9%) |
| d / g / c | 9.3 / −12.2 / +1.2 | **13.6 / +3.1 / +1.5** | 16.3 / +14.3 / +1.4 |
| g: earnings normalisation / multiple (no NAV; core P/E on 2030 EPS today 8.8, v2 11.8) | EPS −25% a year from 2027; exit 8 | **EPS −27% a year from 2027; exit 10** | EPS −23% a year; exit 11 |
| Structural IRR / cyclical (pp) `[A]` reconstruction | −6.0% / +4.3 (−14.2% / +3.2) | **9.0% / +9.3** (−0.6% / +6.8) | 21.3% / +10.7 (10.4% / +7.9) |
| ΣD_t / V_T | 192.4 / 435.9 | **281.9 / 723.6** | 337.3 / 1,001.8 |
| P_k (hurdle price, USD) / margin of safety | **$472.9** / −27.9% (470.9 / −45.0%) | **$751.6 / +14.5%** (748.3 / −12.6%) | **$992.2** / +51.2% (987.9 / +15.3%) |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | — | **9.8× vs 12.7×** (12.8× vs 4.4×) | — |
| Capital preserved? ΣD_t + V_T vs P | **No, −4.3%** (−26.6%) | Yes, +53.2% (+17.4%) | Yes, +104.0% (+56.3%) |

- **How v3 was computed:** the v2 cash flows (D_t by year, paid in equal parts at mid-quarter
  dates, and V_T at 31 Dec 2029) re-priced with XIRR from the new valuation date. The same script
  reproduces every v2 Results figure to 0.1 pp and $0.1 at v2's date and price, so only the price
  and the dates move.
- **Structural run:**
  - EPS is set at the scenario's own 2030 normalised level from 2027 (revenue at the 2029 level).
  - v3 re-runs it on a reconstruction `[A]`: a flat structural payout per year (plus the $35.5 of
    excess cash in 2027), solved so that v2's structural IRRs are reproduced at $856.49, then
    re-priced at $656.39.
  - **The Base cycle is worth +9.3 pp:** two more years of peak cash (2027–28) lift the Base from
    9.0% to 18.3%. **At its normalised earnings, Micron at $656 returns ~9%, below k; the pass rests
    on the 2027–28 peak cash, which is mostly contracted (> 75% of 2027 output committed).**
- **FCF_normalised (Rule 3):** Base 2030 net income $77.1bn with maintenance capex = D&A (the
  renewal charge) gives **$67.1/share**. P/FCF 9.8× against a ceiling of 12.7× now passes; the
  decision is on P_k.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** 17.6% (v2 5.8%). It never
  replaces the Base.
- **Share of Bull already priced:** (656.4 − 751.6) / (992.2 − 751.6) = **−40%**: the price is
  below the Base hurdle (v2 +45%).
- **E / R (NOK; reference row only):** E = 18.3 − 4.36 (Base window NIBOR from 5 Nov, HY BBB path
  4.80 / 4.79 / 4.39 / 3.86 time-weighted) = 13.9 pp; R = Base 2027 return (+26.7%) − Bear 2027
  return in NOK (+4.1%) = 22.6 pp; **E / R = 0.616** (v2 0.069). Against: World 0.024 (Equity BBB,
  18 Oct) and the HY market reference **0.254** (HY BBB 5 Nov; `docs/hy-funds-analysis.md` still
  carries 0.196, its run is on hold). R is small because the Bear's end-2027 mark is set by
  8 × 2028 EPS, not by the price; read the ratio with that in mind.
- **Against the layer:** Base 18.3% is close to the AI BBB memory basket (19.4% in NOK, 5 Nov
  re-mark) and far above World (5.2%). Micron trades at 3.42× CY27 against the basket's 2.79×.
- **Bear balance sheet:**
  - Net cash $60bn throughout; FCF $92 / $50 / $39bn; no debt maturities of note (debt $5.2bn,
    ~9 years average maturity); BBB+.
  - No survival question. The loss is in value: −7.0% in 2027 and −4.3% of capital at exit (v2
    −29% and −27%).
- **Market check (not an input):**
  - Yahoo average rating 1.3 (Strong Buy), 5 Nov. Brokers' mean target was $1,561 (46, Yahoo,
    22 Oct; not re-read in v3), with targets of $361–3,000.
  - They value near-peak earnings at near-peak multiples; the IAF hurdle ($752) is still far below
    the mean target. The difference is the normalisation the brokers do not price.

**Sensitivities, v3** (USD IRR and P_k; P $656.39, 5 Nov):

| Change | Bear | **Base** | Bull |
|---|---|---|---|
| Model | −1.7% (473) | **18.3% (752)** | 32.0% (992) |
| Exit P/E −2 / +2 | −8.0% / +3.8% | **12.1% / 23.8%** (657 / 845) | 25.7% / 37.7% |
| 2030 normalised EPS ×0.8 / ×1.2 | −6.7% / +2.8% | **12.1% / 23.8%** | 25.0% / 38.2% |
| CY27 consensus on the AI BBB figure ($192.10) | −1.6% | 18.4% (753) | 32.1% |
| H2 revenue index (reconciled) taken literally | not re-run (v2: +0.1 pp) | not re-run (v2: +0.3 pp, P_k +$6) | not re-run (v2: +0.2 pp) |
| Capex ×1.2 / ×0.8 | −3.0% / −0.4% | 16.5% / 20.1% (725 / 778) | 30.0% / 34.0% |
| Payout 0% (all FCF retained in net cash) `[A]` reconstruction, no interest on cash | −1.4% | 14.5% (703) | 25.3% |
| **Micron's view: tight through 2028** (EPS 1.00 / 1.00 / 0.60 / 0.45 × consensus, exit 10) | | **33.0% (996)** | |
| Exit at Zacks' 5-year median P/S 3.25× on 2030 revenue (P/E 7.7 / 8.2 / 7.0) | −2.6% | 12.7% (667) | 18.5% |
| With the 2-year reversion tail (exit consistency) | −1.7% | 18.7% (758) | 32.6% |
| **Bear exit P/E capped at v2's core P/E 4.1** (AI BBB memory diagnostic; not the rule) | −15.2% (342); 2027 −40%; capital −33% | | |
| Bear capped at today's core P/E 3.06 | −19.8% (307); 2027 −49%; capital −40% | | |

v2 sensitivities (22 Oct, $856.49), Base: exit P/E −2 / +2 0.7% / 11.3%; EPS ×0.8 / ×1.2 the same;
capex ×1.2 / ×0.8 4.9% / 7.7%; payout 0% 5.3%; Micron's view 18.7% (991); P/S exit 1.3%; tail
6.6%; Bear capped at 4.1 −23.2%.

- **What flips the verdict back to fails:** a price above $752, or (at $656) any one of an exit P/E
  below 8.0, 2030 EPS below ~$54 (0.28× CY27 consensus), or 2028–30 EPS ~15% below the Base path
  `[A]`. The deeper 2029–30 trough that the AI BBB names as its main risk is the one that would do
  it. Every row in the table keeps the Base at or above k except the Bear-side ones.

*Payout-0% and structural rows are re-run on a reconstruction that matches v2 within 0.2–0.4 pp
(v2's model added interest on retained cash); the other rows reproduce v2 to 0.1 pp.*

## Verdict and caveat

- **Verdict (v3, 5 Nov 2026): clears.** Base margin of safety **+14.5%** (Base IRR 18.3% vs k
  12%; P $656.39 vs P_k $751.6). **This flips the v2 verdict (fails, −12.6%).** Decision rule: the
  existing Base margin-of-safety rule (the analysis is not set up cycle-first; see the note at the
  top).
- **Bear:** fails k (−1.7%) but capital is nearly preserved (−4.3%). The balance sheet survives
  every scenario.
- **Why it clears:** only the price. Nothing in the AI BBB path, exit P/E, cash conversion or the
  company model changed. The market now pays 9.8× the Base 2030 earnings, below the exit P/E of 10,
  and the contracted 2027–28 peak cash does the rest.
- **What would flip it back:**
  - the price recovering above **$752**;
  - a deeper or longer trough than the Base 2029–30 (2030 EPS below ~$54, or the path ~15% below
    Base), which the AI BBB names as the main risk;
  - an exit P/E below 8 (a pre-AI memory multiple on a structural-AI mid-cycle);
  - the new state-siting signpost or the financing break turning into a 2028 capex cut (Bear).

*Version 2 verdict (22 Oct, $856.49), for the record:* fails, margin −12.6%; Bear capital −27%;
the price needed ~$748 or a path outside the AI BBB Base (exit P/E 12.3, 2030 EPS $83, or
management's tight-through-2028 view).
- **Caveat:**
  - This is a margin-of-safety screen, not an intrinsic valuation, a price target or personal
    advice.
  - The memory path is the AI BBB's.
  - The calendarisation of consensus, the capex path, the payout and the exit multiples are own
    assumptions; the sensitivities show their weight.

## Tracking

| Version | Valuation date / price | Report since | Base P_k (change) | Base IRR / margin of safety | Running vs Base path |
|---|---|---|---|---|---|
| v1 | 16 Oct 2026 / $931.24 | — | 744.9 | 2.8% / −20.0% | — |
| v2 | 22 Oct 2026 / $856.49 | None (webinar only) | 748.3 (+0.5%): CY27 consensus 191.3 → 191.8, net cash at the valuation date 72 → 74bn, stub 76 → 70 days | 6.3% / −12.6% | On path: FQ1 consensus $38.28 at the guide ($38.15 ± 1); no data on Q4 DRAM prices or FQ1 cash yet |
| **v3** (price re-mark) | **5 Nov 2026 / $656.39** | **None** (no company news; sector sell-off after the 3 Nov midterms) | **751.6 (+0.4%)**: valuation date 22 Oct → 5 Nov only (T 3.19 → 3.16); model blocks unchanged | **18.3% / +14.5%: clears** (was fails) | On path: no Micron data since v2; AI BBB paths unchanged; Yahoo FY27 consensus unchanged ($176.50), FY28 $206.85 → $207.76 |

## Risks and signposts

| Signpost | Bear / Bull threshold | Now | Source |
|---|---|---|---|
| MU price (triggers, v3) | Verdict reverts to fails above $752 (Base = k); E / R = 0.254 at $770; Base = HY market 7.2% at $840 / ≥ $992 Bull hurdle. Below: Bear P_k $473 | **$656.39 (5 Nov close)**: below all three v2 triggers ($846 / $792 / $748) | Yahoo |
| **US state data-center siting (new, from AI BBB 5 Nov)** | statewide moratorium by order or statute in Texas, Georgia or Ohio, or a hyperscaler moving or cancelling ≥ 1 GW over policy → 2028 capex cut (Bear) / pledges softened into cost rules | Texas pause on new loads ≥ 75 MW since 3 Aug; ERCOT/PUCT audit 10 Dec; governors sworn in 11–19 Jan 2027 | AI BBB (Drivers, Memory cycle section 6) |
| DRAM contract prices (incl. HBM) | fall q/q / > +10% q/q into 2027 | Q4-26 +15–20%; Q1-27 +3–8% | AI BBB (TrendForce via Goldman `[E]`) |
| FQ1-27 (23 Dec): revenue, gross margin, FY27 capex, buyback size | < $60bn and GM < 86% / > $63bn | Guide $61.5bn, 86.25% | Micron |
| Micron SCAs and RPO | RPO falls or floors renegotiated / RPO > $200bn | 26 SCAs, RPO ~$150bn, > 35% of revenue through 2030 | Micron |
| **Node ramps 1δ DRAM and G11 NAND (new)** | on time with peers on time → more 2028 bits (Base) / slips industry-wide (Bull) | Both 2H 2027 (webinar, "directional") | Micron, peers |
| **Custom HBM4E (new)** | CSP programs delayed / named custom wins with prepayments | "Multiple CSPs" in development (webinar) | Micron |
| Industry capacity: CXMT 4F² DRAM, Samsung / SK hynix capex | volume shipments with specs in 2026–27 / claim slips | Claim only (13 Oct); Micron: "no viable scaling path" for 4F² (21 Oct, interested party) | AI BBB, webinar |
| SK hynix Q3 (28 Oct), Samsung final Q3: 2027 HBM and DRAM pricing | price cuts / sold-out 2028 | 2027 sold out `[E]` | Company reports |
| Hyperscaler 2027 capex (28–29 Oct); NVIDIA Q3 FY27 (17 Nov) | flat or down / 2027 consensus > USD 1.3tn | 2027 consensus ~USD 1.1tn; Meta 2027 "continue investing" (21 Oct) | AI BBB |
| Lab and vendor financing | IPO pulled; new vendor loans or guarantees > USD 50bn in a quarter | ≥ USD 230bn of supplier loans, guarantees and equity commitments (AI BBB, 22 Oct); Micron stake in Anthropic (size `[?]`) | AI BBB |
| Micron inventory days | > 140 and rising / < 110 | 129 (FQ4-26) | Micron |
| Taiwan / export controls | escalation | Majority of DRAM output in Taiwan (10-K) | Not modelled |

## For other modules

- **`ai-market-bbb`** (input; no path set here; no path change requested):
  1. **Webinar supply facts for H2 (Hardware, memory):** Micron's 1δ DRAM (+mid-20s% bits per
     wafer) and G11 NAND (~2× density, > 400 layers) both ramp in 2H 2027. That is node-driven
     bit supply for 2028 on top of the cleanroom timeline, and evidence *for* the Base 2028 fall.
     It does not move a Base EPS point by ≥ 0.05.
  2. **CXMT signpost:** add Micron's statement of 21 Oct ("not pursuing 4F² due to increased
     complexity/cost"; "over two decades … no viable scaling path") as context. It is a
     competitor's view and does not close the signpost.
  3. **HBM roadmap and customisation:** HBM4E 2027 (custom base dies from HBM4E, "multiple CSPs"),
     HBM5 2028, HBM5E 2029, HBM6 2030; vertical HBM from ~2028. Qualitative support for contract
     depth (SCAs), not a price path.
  4. **Micron company check (v3):** at $656.39 (5 Nov close) Base is 18.3% in USD, P_k $751.6,
     margin of safety +14.5% (clears; was −12.6% at $856.49 on 22 Oct), E / R 0.616. On this
     analysis's own method (100% payout, net cash) the price earns k at ~0.85× the Base 2028–30
     path `[A]`, against the AI BBB's 1.05× for Micron on the basket method (US intraday prices);
     the difference is the method (net cash and the fast cash return), as section 5 of the Memory
     cycle expects. No path change requested. Both 16 Oct flags (CY27 label, revenue index base) are confirmed resolved: the
     AI BBB's $192.10 and the reconciled index give the same result as the EPS path (6.3% and
     6.6%).
- **`docs/global-index-funds-analysis.md`:** at the next re-run Micron can be taken as a company
  block at Base 18.3% in USD on the 5 Nov close (v2 6.3%; v1 2.8%). Micron is ~1.3% of MSCI World; the effect on either fund
  is < 0.05 pp.
- **`equity-market-bbb`:** no input.
- **`docs/portfolio-overview.md`:** not held; no change. DNB Teknologi holds no Micron
  (`docs/dnb-teknologi-analysis.md`).

## Change log

- **5 Nov 2026 — version 3, price re-mark** (iaf-valuation 2026-11-01.1; ai-market-bbb document
  5 Nov notes, skill 2026-11-01.1 / 2026-11-05.1; hy-market-bbb document 5 Nov; equity-market-bbb
  document 17/18 Oct, unchanged).
  - **Market data:** price $856.49 → **$656.39** (Nasdaq close 5 Nov, −17.5% on the day, sector
    sell-off after the 3 Nov midterms; no company news); valuation date 22 Oct → 5 Nov, T 3.19 →
    3.16, stub 70 → 56 days; net cash at the valuation date ~$74bn → ~$79bn `[A]`; USD/NOK 9.313
    → 9.3094.
  - **Upstream:** AI BBB H2 path, revenue index, exit P/E and cash conversion unchanged; state
    siting policy added as a signpost; memory multiplier for Micron 1.43× → 1.05×. HY BBB: NIBOR
    path unchanged (window NIBOR 4.38 → 4.36 on the later start); HY Base window 6.8% → 7.2%;
    market reference E / R 0.196 → 0.254 (read from the HY BBB; the funds analysis still shows
    0.196). Equity BBB unchanged.
  - **Model blocks:** none changed. Yahoo FY28 consensus $206.85 → $207.76 lifts CY27 by ~0.1%;
    not moved (the $192.10 sensitivity covers it).
  - **Result:** Base 6.3% → **18.3%**, P_k 748.3 → **751.6**, margin of safety −12.6% →
    **+14.5%**; Bear −11.0% → −1.7%; Bull 18.3% → 32.0%; E / R 0.069 → 0.616. **Verdict flips:
    fails → clears.** Decision rule kept (Base margin of safety; not set up cycle-first).
  - **Method note:** v3 re-prices the v2 cash flows with a script that reproduces v2 exactly
    (mid-quarter payment dates); the structural and payout-0% rows use a reconstruction `[A]`.
- **22 Oct 2026 — version 2** (iaf-valuation 2026-10-18.2; ai-market-bbb document Update 3 of
  22 Oct, rev 2026-10-22.1; equity-market-bbb document of 17/18 Oct, skill 2026-10-18.6;
  hy-market-bbb 17/18 Oct, skill 2026-10-18.2).
  - **Input: Micron technology webinar (21 Oct).** Read in full (33 slides). New section Webinar;
    1δ and G11 added to the capacity table, the exit-consistency reason and the signposts; custom
    HBM to the growth capex test. **No model input changed by it** (no guidance, prices, bits or
    capex; reasons in Webinar).
  - **Market data:** price $931.24 → **$856.49** (22 Oct close); consensus FQ1 38.21 → 38.28, FQ2
    41.97 → 42.30, FY27 176.55 → 176.50, FY28 204.47 → 206.85; CY27 191.3 → **191.8**; net cash at
    the valuation date 72 → 74bn; stub 76 → 70 days; USD/NOK 9.472 → 9.313.
  - **Upstream:** H2 path, exit P/E and cash conversion unchanged. New Equity BBB USD/NOK path
    (Bear 10.54 / 10.27 / 10.27, Bull 9.13, from 9.41); World 6.1% → 5.2%, E / R 0.063 → 0.024.
    The HY trigger now uses the HY market Base 6.8% (was the HY book 6.9%), as in the AI BBB.
  - **Method (iaf-valuation 2026-10-18.2):** exit cross-check against the equity market added
    (exit P/E, P/B, buyer's implied return vs World); Tracking section added; IRR in NOK moved
    into the Results table.
  - **Sensitivities:** the old "AI BBB basis $206.33" and "old revenue index" rows replaced by the
    resolved versions; the Bear capped at today's multiple added (AI BBB diagnostic).
  - **Result:** Base 2.8% → **6.3%**, P_k 744.9 → **748.3**, margin of safety −20.0% →
    **−12.6%**; Bear −13.7% → −11.0%; Bull 14.3% → 18.3%. Verdict unchanged: **fails**.
- **16 Oct 2026 — version 1** (iaf-valuation 2026-10-11.3; ai-market-bbb 2026-10-15.1;
  equity-market-bbb 2026-10-16.1, document of 11 Oct). No previous version.

## Appendix: own assumptions `[A]`

By weight on the result:
1. **Memory EPS path** = AI BBB H2 layer × Micron's calendarised CY27 consensus ($191.8); 2030
   normalised $67.1.
2. **Exit P/E 10 / 8 / 11** on 2030 EPS (the AI BBB reference, cross-checked against World's exit
   P/E, P/B and mid-cycle return, and on P/S history).
3. **Payout:** 100% of FCF from 2027, net cash ex deposits held at $60bn, $41bn of excess paid
   in 2027.
4. **Capex** $58 / 65 / 60bn (Base); maintenance capex = D&A $12 / 16 / 20bn. The webinar's R&D
   programs are taken as inside opex and capex.
5. **Revenue path** (working capital only) and working capital at 15% of the revenue change.
6. **Calendarisation:** CQ = 2/3 of the fiscal quarter ending in it + 1/3 of the next; FY27 Q3/Q4
   = 46.38 / 49.54 and FY28 quarters 50.58 / 51.39 / 52.00 / 52.88 (v1 split scaled to the 22 Oct
   consensus).
7. **Net cash at the valuation date** ≈ $74bn ex deposits (FQ1 FCF to date).
8. Year-1 quarterly haircuts (Base 0.98 / 0.93 / 0.87 / 0.83).
9. **Long-run growth 4%** in the buyer's implied return at exit (cross-check only).

## Appendix: sources

| # | Source | Content | As of |
|---|---|---|---|
| S1 | [Micron FQ4-26 press release (8-K ex. 99.1)](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000018/a2026q4ex991-pressrelease.htm) | Revenue $54,229m; GM 87.0%; non-GAAP EPS $33.42; FY26 $133,188m / $75.52; OCF, capex, FCF; balance sheet; dividend; FQ1-27 guidance | 30 Sep 2026 (quarter to 3 Sep) |
| S2 | [Micron FQ4-26 prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf) (text via `pypdf`) | DRAM/NAND, SCAs, RPO ~$150bn, market outlook, fab timelines, capex, opex, tax, capital return | 30 Sep 2026 |
| S3 | [Micron FY26 10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm) (WebFetch, partial) | D&A $9,503m; PP&E $30,712m; incentives $3,316m; deposits $12.75bn; equity $138,378m; buyback authorization $35.16bn (8 Oct); shares 1,131,423,212 (2 Oct); DRAM/NAND by year; customer and Taiwan concentration | Filed 9 Oct 2026 |
| S4 | Yahoo quoteSummary (`earningsTrend`, `price`, `financialData`, `calendarEvents`) and chart | Price $856.49 (22 Oct close; 21 Oct $913.67); FQ1 $38.28 (29), FQ2 $42.30 (28), FY27 $176.50 (35), FY28 $206.85 (36); revenue FY27 $275.7bn (40), FY28 $318.7bn (42); targets; report 23 Dec (estimate) | 22 Oct 2026 |
| S5 | [Zacks research report, MU](https://www.zacks.com/zer/report/MU) | ROIC 10-year median 11.1%; P/S history; > 75% of 2027 output committed | 7 Oct 2026 `[C]` |
| S6 | [Zacks: "Micron (MU) Falls More Steeply Than Broader Market"](https://www.zacks.com/stock/news/3013280/micron-(mu)-falls-more-steeply-than-broader-market:-what-investors-need-to-know) | Close $856.49 (−6.26%), Nasdaq −2.6%, S&P −1.21%; FY27 $177.73, revenue $277.53bn; Rank 1; estimate +11.57% in a month | 22 Oct 2026 |
| S7 | [Micron webinar "Technology and products leadership for the AI era"](https://s25.q4cdn.com/621799436/files/doc_downloads/2026/10/MU-TP-Webinar.pdf) (33 slides; text via `pypdf`) | 1δ ramp 2H-27, mid-20s% density; no 4F²; G11 > 400 layers, ~2× density, ramp 2H-27; HBM4E–HBM6 roadmap, custom HBM, vHBM, vEIM; demand ratios; R&D programs; > $250bn US commitment | 21 Oct 2026 |
| S8 | [SEC EDGAR submissions, CIK 723125](https://data.sec.gov/submissions/CIK0000723125.json) | Filings since 1 Oct: 10-K (9 Oct), Forms 4 and 144; no 8-K | 22 Oct 2026 |
| S9 | `docs/ai-market-bbb.md` (Update 3) | H2 path, exit P/E, cash conversion, index, basket, signposts, scenarios, CY27 $192.10 | 22 Oct 2026 |
| S10 | `docs/equity-market-bbb.md`, `docs/hy-market-bbb.md`, `docs/hy-funds-analysis.md` | Macro scenarios, USD/NOK path, World return, exit P/E, P/B and mid-cycle return; NIBOR; HY market Base and reference E / R | 17–18 Oct 2026 |
| S11 | Yahoo `NOK=X` | USD/NOK 9.313 | 22 Oct 2026 |
| S12 | Yahoo `get_quote` MU, `NOK=X`, `^SOX` | MU close $656.39 (prev. $795.23; −17.46%), FY27 EPS $176.50, forward $207.76, 1,131.4m shares, rating 1.3; USD/NOK 9.3094 (21:05:59 UTC); SOX 9,011.14 (−12.2%) | 5 Nov 2026 |
| S13 | `docs/ai-market-bbb.md` (5 Nov notes; Memory cycle §5 re-mark), `docs/hy-market-bbb.md` (5 Nov change summary) | Price event, paths unchanged; Micron 1.05×, basket 0.80×, basket Base 19.4%; NIBOR path unchanged, HY Base 7.2%, reference E / R 0.254 | 5 Nov 2026 |
| S14 | FinancialFilings `filings_list` (company 29796, released since 22 Oct) | No filings returned (no share issue found) | Server date 3 Nov 2026 |

- **Validation notes:**
  - **Consensus year labels:** on 22 Oct FY27 = 2027-08-31 ($176.50) with year-ago $75.52 = FY26
    actual, FY28 = 2028-08-31 ($206.85). Zacks agrees on FY27 ($177.73).
  - **CY27 check:** own calendarisation $191.8 against the AI BBB's $192.10 (−0.2%).
  - **FY26 EPS check:** quarterly 4.78 + 12.20 + 25.11 + 33.42 = 75.51 vs reported $75.52.
  - **Net cash:** the release's $68.3bn includes customer deposits ($12.75bn) that are to be
    returned, so they are excluded here.
  - **Yahoo `freeCashflow`** ($29.1bn TTM) is a levered definition; not used.
  - **FinancialFilings** was unavailable (quota until 1 Nov); EDGAR was used for the filing check.
  - The webinar has no financial figures; every roadmap date is Micron's target.
- **Scripts:** the v1 model (`mumodel.py`) and sensitivities (`musens.py`) were re-run in the
  session scratchpad with the inputs above, plus a break-even script. As for the other IAF
  analyses, they are not stored in the skill. Every input is in Common assumptions and Appendix:
  own assumptions, so the build can be reproduced.
- **v3 script:** a re-pricing script in the session scratchpad (`muremark.py`, `musens2.py`)
  takes the v2 D_t by year (paid in four equal parts on 15 Feb / May / Aug / Nov) and V_T at
  31 Dec 2029. At v2's date and price it reproduces every v2 Results figure (Base 6.28%, P_k
  748.3; Bear −11.00%, 470.9; Bull 18.30%, 987.9; NOK −7.92% / 16.93%; weighted 5.8%). No model
  script in `.claude/skills/equity-market-bbb/references/fund/` or `ai-market-bbb/references/` is
  named by this document, so none was used.
