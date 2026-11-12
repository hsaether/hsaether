# TSMC (NYSE: TSM ADS / TWSE: 2330) — IAF analysis, stub Q4 2026 + 2027–2029

**Version 1.2 — signpost update and price re-mark, 11 Nov 2026** (price: NYSE regular close Tue
10 Nov 2026, **$396.48 per ADS**). Skill revision used: **iaf-valuation 2026-11-10.1** (1.1:
2026-11-01.1). **Verdict: fails** (Base 9.5%, P_k $369.8, margin of safety −6.7%). Cause: TSMC's
October revenue (6-K, 10 Nov: NT$586.89bn, +59.7% y/y) and, the same day, the November board
(3Q26 dividend NT$9.0, capital appropriations $40.9bn). Neither moves a path; the verdict flips on
the price (+12.6% since 5 Nov). The 1.1 → 1.2 walk is in the Change log. The 2026-11-10 layout
rules (current state only in the body) are not applied in full: this run keeps the document's
version-by-version layout; the Q4 report (~14 Jan 2027) brings the full re-run. Inputs read for
1.2:
- `docs/ai-market-bbb.md` (**ai**), Update 7 of 7 Nov (ai-market-bbb 2026-11-06.1): **no path,
  index, exit P/E or scenario moved**; the H3 rows used here are as in 1.1.
- `docs/equity-market-bbb.md` (**equity**), **Update 2 of 6 Nov** (1.1 read 17/18 Oct): World Base
  5.2% → **6.6%**, Bear 2027 −20.6% → **−18.3%** (NOK), E / R 0.024 → **0.080**; World exit P/E 17.0
  (15.0 / 18.5), P/B **3.17** (2.47 / 3.74), mid-cycle return 8.2% (7.1 / 8.7); NOK path relative
  moves unchanged (Bear +12% / +9% / +9%, Base flat, Bull −3%). Comparators and the exit
  cross-check only; no TSMC value moves.
- `docs/hy-market-bbb.md` (**hy**), 5 Nov, as in 1.1: NIBOR window 4.38%, HY reference E / R 0.254.
- `docs/nvda-analysis.md` not re-read (no NVIDIA report before 17 Nov).

Version 1.1 — light update 5 Nov 2026 (price: NYSE regular close Thu 5 Nov 2026). Version 1:
17 Oct 2026 (close Fri 16 Oct). Skill revisions used for 1.1: iaf-valuation 2026-11-01.1 (version 1:
2026-10-11.3; the newer Step 7 Summary rules are applied: traded price and P_k in USD per ADS for
each scenario, trigger prices, the cycle lead, the exit cross-check). Inputs read for 1.1:
- `docs/ai-market-bbb.md` (**ai**): Updates 2–6 (17 Oct–1 Nov) and the **5 Nov note** (US midterms
  and the 4–5 Nov chip sell-off), produced with ai-market-bbb rev **2026-11-01.1**. What moved the foundry layer since
  version 1: **only the H3 Bear EPS path** (Update 2, 17 Oct: .80 / .75 / .85 / .92 → **.76 / .63 /
  .67 / .71**, TSMC's own revenue-consistent Bear). K1 capex (790 / 1,120 / 1,250 / 1,300), the H3
  revenue index (Base 125 / 140 / 151), the H3 Base and Bull EPS paths and the exit P/E (14 / 18 /
  21) are unchanged. 5 Nov verdict: a price event; state siting policy added as a Bear signpost.
- `docs/nvda-analysis.md` (**nvda**), version 1.1 of 2 Nov (price 30 Oct): demand signal unchanged
  (supply commitments $279bn, $87–88bn a year in FY28–29; Q3 FY27 on 17 Nov). No value enters TSMC;
  the comparison row is updated.
- `docs/hy-market-bbb.md` (**hy**), 5 Nov: NIBOR path unchanged (Base 4.80 / 4.79 / 4.39 / 3.86;
  window **4.38%**); **HY market reference E / R 0.196 → 0.254** (Base 7.2% before fees, 6.6% after
  the 0.6% fee convention; Bear 2027 −0.4% before fees).
- `docs/equity-market-bbb.md` (**equity**), 17 Oct amended 18 Oct (read on 11 Oct in version 1): NOK
  path relative moves unchanged (Bear +12% / +9% / +9%, Base flat, Bull −3%); World Base 6.1% →
  **5.2%**, Bear 2027 −18.2% → **−20.6%** (NOK), E / R 0.063 → **0.024**; exit references World P/E
  17 (15 / 18.5), P/B 3.14 (2.46 / 3.69), mid-cycle return 8.2% (7.1 / 8.7). Nothing in it moves a
  TSMC value; the comparators and the exit cross-check use it.

Version 1 inputs (kept below for the build):
- `docs/ai-market-bbb.md`, **Update 1 of 15 Oct 2026, amended 16 Oct**, produced with ai-market-bbb rev
  **2026-10-16.1**. It supplies:
  - the **H3 foundry, packaging and equipment layer**: EPS path (CY27 consensus = 1.00), exit P/E
    reference, revenue index;
  - the scenarios and catalysts (financing break and capacity overshoot 2028 / contracted build then
    digestion / agentic adoption);
  - the H3 basket return and P/E for comparison, and the signposts.

  This analysis makes no AI market forecast of its own.
- `docs/nvda-analysis.md` (**version 1, 17 Oct 2026**, iaf-valuation 2026-10-11.3): NVIDIA is the
  largest buyer of TSMC's AI capacity. Used for its H1 path reading, its supply commitments, its
  Bear and its result as the comparison inside the same AI baseline (section NVIDIA as input).
- `docs/equity-market-bbb.md` (11 Oct 2026, produced with equity-market-bbb rev 2026-10-11.2; the
  skill is now 2026-10-16.1; the document is not stale until 10 Nov). It supplies:
  - the macro scenarios the AI scenarios sit inside (Bear = recession H1 2027 + oil Bear; Bull =
    soft landing);
  - the USD/NOK path (NOK memo only; the decision is in USD at spot, as the IAF skill requires);
  - World Base 6.1% (6.4% at the 14 Oct prices), World E / R 0.063, and the HY market reference
    E / R 0.196.
- `docs/hy-market-bbb.md` (hy-market-bbb rev 2026-10-15.1) is read only for the Base window NIBOR
  **4.38%** (E / R). TSMC has net cash; no refinancing test applies. The oil, rig, supply, shipping
  and defense baselines are not used.

## Change note, 5 Nov 2026 (version 1.1, light update; superseded by 1.2 of 11 Nov, see Change log)

**Cause:** the ADS fell **11.0% on 5 Nov** ($395.75 → **$352.03**; −14.7% from version 1's $412.61)
in a sector sell-off (SOX ~−10%) on fears that the Democratic sweep in the 3 Nov midterms slows the
AI data-center buildout. **No company news** (EDGAR: no 6-K with results or revenue since 15 Oct).
The AI BBB reads it as a price event: all paths unchanged.

| Step (in order) | Base IRR / P_k / margin of safety | Bear IRR (P_k) | Bull IRR (P_k) |
|---|---|---|---|
| Version 1 (17 Oct; $412.61; CY27 basis $23.11; old H3 Bear) | 7.4% / $362.1 / −12.2% | −6.3% ($236) | 18.8% ($497) |
| Method (iaf-valuation 2026-10-11.3 → 2026-11-01.1): Summary in USD per ADS per scenario, triggers as prices, cycle lead, exit cross-check, NOK label | no value change | — | — |
| **ai** Update 2 (17 Oct): H3 Bear .80 / .75 / .85 / .92 → **.76 / .63 / .67 / .71** (version 1's own revenue-consistent Bear, adopted by the layer). Updates 3–6 and the 5 Nov note: no H3, K1 or exit P/E row moved | unchanged | **−13.2% ($186)** | unchanged |
| **nvda** 1.1 (2 Nov): demand signal unchanged | no value change | — | — |
| **equity** 17/18 Oct: NOK path relative moves unchanged; World and the exit references moved | no value change (comparators only) | — | — |
| **hy** 5 Nov: NIBOR unchanged; HY reference E / R 0.196 → 0.254 | no IRR change; E / R trigger moves | — | — |
| Consensus (Yahoo `earningsTrend`, 5 Nov): CY27 ADS EPS $23.11 → **$23.43** (14 analysts; the AI BBB's own source, 23.39 on 1 Nov) | 7.9% / $367.0 / −11.0% | −12.8% ($189) | 19.3% ($504) |
| **Price, date and FX:** $412.61 → **$352.03**; valuation date 17 Oct → 5 Nov (T 3.21 → 3.16); USD/TWD 32.428 → 33.027 (dividends and net cash in USD); USD/NOK 9.4135 → 9.3105 | **13.7% / $368.9 / +4.8%** | **−8.5% ($190)** | **26.0% ($507)** |

- **Verdict flips: fails (−12.2%) → clears (+4.8%).** It is the price alone: the inputs moved Base by
  +0.5 pp (the consensus basis), and the Bear got worse (the reconciled H3 Bear). The margin is
  thin: **it clears below $361.7, is marginal up to $376.4 and fails above $376.4** (+6.9%).
- **What did not change:** the AI BBB's view of the foundry layer (contracted 2027, digestion
  2028–29), TSMC's guidance and the exit multiple. The 5 Nov fall is a de-rating of the capex
  receivers on policy risk to 2028 siting, which the AI BBB sizes at ~3–4% of K1 2028 (below its 5%
  rule) and has added as a second route to the Bear.

## Summary

**The AI foundry cycle** (read from the AI BBB's K1 and H3 rows, scenarios and signposts; no own
forecast). TSMC is not held; a purchase would be an opportunistic single-stock position in a
Track B layer, so the Summary leads with the cycle (iaf-valuation rule of 1 Nov, kept in
2026-11-10.1).
- **Where:** in the build-out. Hyperscaler capex (K1) ~$790bn in 2026, **$1,120bn in 2027
  (+42%, contracted and under construction), then +12% and +4%**. H3 revenue index 125 / 140 / 151;
  TSMC's Base EPS +27% in 2027, then ~7% a year. Unchanged through seven AI BBB updates (Update 7,
  7 Nov: no path moved).
- **What can turn it:** financing, and US state siting policy. The financing signposts sit on the
  Bear side: platform equity funding crossed (Update 5, 29 Oct); capex ÷ OCF ~116% for the five
  in Q3, read as touched (Update 6); CoreWeave's new 2026 low on 5 Nov, the neocloud signpost's
  first leg, read as touched (5 Nov note). Siting (Texas, Georgia, Ohio governors from 11–19 Jan;
  ERCOT/PUCT audit 10 Dec) is a second route to the Bear's 2028 capex cut. **TSMC's own 10 Nov
  prints point the other way:** October revenue **+59.7% y/y** (second month above the +45%
  Bull-side level), the 3Q26 dividend raised to **NT$9.0** (from NT$7.0) and capital
  appropriations of **$40.9bn** (August $29.4bn). No hyperscaler, NVIDIA or TSMC has cut guidance.
- **What the price implies:** at $396.48 TSMC earns k only if 2028–30 EPS is **1.07× the AI BBB
  Base**, and 0% at **0.76×**. The AI BBB Bear (≈ 0.61× Base from 2028) gives −12.0% a year. **The
  price now discounts a little more than the Base: it prices out the 2028–29 digestion the AI BBB
  expects.**
- **Next:** NVIDIA Q3 FY27 (17 Nov), the Anthropic IPO pricing (~18 Nov), November revenue
  (~10 Dec), the 2Q26 dividend ex-date (10 Dec), the Q4 report with the 2027 revenue and capex guide
  (~14 Jan 2027).

**Verdict**
- **Fails.** Base IRR **9.5% a year** (USD; NOK the same in Base) against k = 12%. Hurdle price
  **P_k $369.8 vs P $396.48 (ADS, NYSE close 10 Nov): margin of safety −6.7%.**
  - TSMC trades at **16.9× calendar-2027 consensus EPS** ($23.43 per ADS kept; Yahoo 10/11 Nov
    $23.39, 13 analysts) and **15.0× Base 2030 core earnings** after net cash.
  - The Base return is **earnings growth and retained cash**; the re-rating (core P/E 17.6 on Base
    2027 to the layer's exit 18) adds only $9. At today's multiple Base is **8.9%**.
  - Bands: **clears below $362.6 · marginal $362.6–377.4 · fails above $377.4.** Post-market
    $402.59 and Taipei's 11 Nov close (NT$2,395, +4.8%) both sit above the fail line.
- **What moved it:** the price alone (+12.6% from the 5 Nov sell-off close; +2.0% on 10 Nov after
  the releases). October revenue tracks the upper half of the Q4 guide, not above it, so the stub
  is kept; the NT$9.0 dividend raises D_t and lowers retained cash by the same amount (Base +0.0 pp
  at the 1.1 price).
- **What would make it clear k:** the price below $362.6 (−8.5%), or evidence for more than the
  Base: management's own path (12.3%, P_k $400: marginal), an exit P/E of 20 (12.8%), 2030 EPS 10%
  above Base (12.7%), the ADR premium back to its 2-year mean (12.0%). Worse: an exit P/E of 16
  (6.0%), margins toward the 56% floor (3.5%).
- **Bear breaks the thesis in value, not the balance sheet:** −12.0% a year in USD (−9.5% on the
  Equity BBB NOK path). The ADS falls **~44% in 2027** (−37% in NOK) as EPS drops to .63 of CY27
  consensus in 2028 and the P/E to 14; capital is not preserved (ΣD + V_T is 32.3% below P). Net
  cash still grows every year ($99bn at end-2026 → $201bn at exit).
- **Bull: 21.3%** (P_k $507.5). The price is 19% of the way from the Base to the Bull hurdle.
- **E / R 0.106** against the HY market reference 0.254: a reference row, not the gate. It reaches
  0.254 at **$335.9 (−15.3%)**.
- **ADR premium:** close-on-close the ADS is **13.8% above** Taipei (NT$2,285 at 32.789; Taipei
  closed before the 10 Nov releases). At the modelled 10.6% the ADS implies Taipei NT$2,351; Taipei
  printed NT$2,395 on 11 Nov (ADS-equivalent ~$403 at 10.6%).

**Decision table (USD per ADS = 5 shares; traded line NYSE: TSM)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| Price P (USD, NYSE close 10 Nov) | 396.48 | **396.48** | 396.48 |
| IRR_T (USD) / NOK path (Equity BBB) | −12.0% / −9.5% | **9.5% / 9.5%** | 21.3% / 20.1% |
| V_T (31 Dec 2029) | 250.9 | **504.4** | 698.9 |
| **P_k (USD) / margin of safety** | **190.2** / −52.0% | **369.8 / −6.7%** | **507.5** / +28.0% |
| Capital preserved? (ΣD + V_T vs P) | **No: −32.3%** | Yes: +32.3% | Yes: +81.8% |
| Cumulative FCF per ADS 2027–29 (after growth capex) | 37.1 | **49.8** | 50.6 |
| Net cash per ADS at exit | 38.7 | **48.9** | 47.8 |
| Balance sheet | Net cash grows every year (FCF $58–74bn); capex cut from $70bn to $55bn | Net cash $253bn at exit; capex $76–85bn paid from cash flow | Capex $82–105bn, net cash still $248bn |

**Trigger prices (USD per ADS; unchanged earnings and paths):** clears below **$362.6** · marginal
$362.6–377.4 · fails above **$377.4** · Base = k at **$369.8** · E / R = HY reference 0.254 at
**$335.9** · Base = HY market 7.2% at $423.2 · Bull hurdle $507.5 · Bear hurdle $190.2. Taipei
equivalent at the modelled 10.6% premium and USD/TWD 32.789: P_k **NT$2,193**, clears below
NT$2,150, fails above NT$2,238 (Taipei closed NT$2,285 on 10 Nov and NT$2,395 on 11 Nov).

**Per-share path (USD per ADS; calendar years; EPS as reported, incl. net interest income)**

| | Stub Q4-26 (10 Nov–31 Dec) | 2027 | 2028 | 2029 | 2030 (exit-year EPS) |
|---|---|---|---|---|---|
| Base revenue ($bn) | 29.5 | 220 | 247 | 266 | |
| Base EBITDA $bn / per ADS | 21.0 / 4.06 | 168 / 32.4 | 185 / 35.7 | 201 / 38.8 | |
| Base EPS = maintenance FCF per ADS (maintenance capex = D&A) | 2.86 | 22.26 | 24.14 | 25.78 | **27.18** (core 25.31) |
| Base growth capex (capex − D&A) per ADS | 1.47 | 8.10 | 7.91 | 6.94 | |
| Base FCF after growth per ADS (no debt amortisation of note) | 1.40 | 14.09 | 16.49 | 19.23 | |
| Base D_t (dividends paid; NT$35 / 44 / 52 a share) | 0 (2Q26 NT$7.0 ex 10 Dec, paid 7 Jan: in 2027) | 5.34 | 6.71 | 7.93 | |
| Base net cash per ADS (year-end) | 19.02 | 27.77 | 37.55 | 48.86 | |
| Base V_t (year-end) | 397.9 (price flat + stub cash) | 436.8 | 472.0 | 504.4 | |
| Bear EPS / FCF per ADS / V_t | | 17.81 / 11.10 / 218.2 | 14.76 / 11.85 / 233.9 | 15.70 / 14.18 / 250.9 | 16.64 |
| Bull EPS / FCF per ADS / V_t | | 23.43 / 13.86 / 477.2 | 26.95 / 16.68 / 585.1 | 30.00 / 20.10 / 698.9 | 32.81 |

### Version 1 summary (17 Oct 2026, $412.61; superseded, kept for the record)

**Verdict**
- **Fails.** Base IRR **7.4% a year** (USD; NOK the same in Base) against k = 12%. Hurdle price
  **P_k ≈ $362.1 vs P $412.61: margin of safety −12.2%.**
  - TSMC trades at **17.85× calendar-2027 consensus EPS** ($23.11 per ADS) and **15.8× Base 2030
    earnings** after net cash and the interest it earns.
  - On the AI baseline's H3 path, earnings rise **+27% in 2027** ($21.95) and then about **7% a
    year** ($23.80 / $25.42; $26.80 in 2030). The exit P/E (18) is about today's multiple, so the
    return is earnings growth, retained cash and a 1.4% dividend yield: **about 7%**.
  - **The verdict does not depend on the AI baseline being cautious.** On consensus for 2027 plus
    management's own long-term target (revenue ~25% a year 2024–29), Base is **10.2%** (P_k $392,
    −5%): still fails.
- **What the price needs** (any one of): an exit P/E of **≥ 20.9** on Base 2030 earnings (today
  18.7 on 2027); **2030 EPS ≥ $30.84** (1.335× CY27 consensus; Base 1.16, Bull 1.40). Bull earnings
  at the Base multiple give 13.8%; Base earnings at the Bull multiple give 12.1%.
- **Bear breaks the thesis in value, not the balance sheet:** −6.3% a year in USD (−3.7% in NOK).
  The ADS falls **~38% in 2027** (−30% in NOK) as the P/E goes from ~18.7 to 14, and capital is not
  preserved (ΣD + V_T is 18.5% below P).
  - The catalyst is the AI BBB financing break and the 2028 capacity overshoot inside the equity
    recession.
  - The layer's Bear EPS path implies TSMC's net margin *rising* to 56% while revenue falls. A
    revenue-consistent Bear gives **−13.2%** (see For other modules).
  - Net cash grows every year in every scenario (from $89bn today to $248–257bn at exit).
- **Bull: 18.8%** (P_k $497). The price already holds **37% of the way** from the Base hurdle to
  the Bull hurdle.
- **Against NVIDIA, its layer, World and HY:**
  - Base 7.4% is above the H3 basket (1.1%) and World (6.1–6.4%), level with the HY book (6.9%),
    and well below **NVIDIA (13.0%)** on the same AI baseline.
  - **E / R is 0.079**, far below the HY market reference (0.196), the HY book (0.291) and NVIDIA
    (0.184). The Bear 2027 loss (−30% in NOK) is ten times HY's.
  - **Triggers:** Base = k at **$362 (−12%)**; E / R = 0.196 at **$348 (−16%)**; E / R = HY book
    0.291 at **$286 (−31%)**. Above **$419 (+1.6%)** the HY book beats TSMC on Base return alone.
- **ADR premium:** the ADS trades **10.6% above** the Taipei share (2-year average 19.5%, low 6.9%).
  The model holds it constant. A return to the 2-year average adds 2.6 pp (10.0%); parity with
  Taipei costs 3.2 pp (4.2%). Neither changes the verdict.

**Decision table (USD, per ADS = 5 shares)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (USD) / NOK memo | −6.3% / −3.7% | **7.4% / 7.4%** | 18.8% / 17.7% |
| V_T (31 Dec 2029) | 320.4 | **499.0** | 690.0 |
| P_k / margin of safety | 235.7 / −42.9% | **362.1 / −12.2%** | 497.1 / +20.5% |
| Capital preserved? (ΣD + V_T vs P) | **No: −18.5%** | Yes: +25.4% | Yes: +72.4% |
| Cumulative FCF per ADS 2027–29 (after growth capex) | 44.3 | **48.8** | 49.5 |
| Net cash per ADS at exit | 47.8 | **49.5** | 47.5 |
| Balance sheet | Net cash grows every year (FCF $61–94bn); capex cut from $70bn to $55bn | Net cash $257bn at exit; capex $76–85bn paid from cash flow | Capex $82–105bn, net cash still $246bn |

**Per-share path (USD per ADS; calendar years; EPS as reported, incl. net interest income)**

| | Stub Q4-26 (17 Oct–31 Dec) | 2027 | 2028 | 2029 | 2030 (exit-year EPS) |
|---|---|---|---|---|---|
| Base revenue ($bn) | 44.0 | 220 | 247 | 266 | |
| Base EBITDA $bn / per ADS | 31.4 / 6.05 | 166 / 32.1 | 183 / 35.3 | 199 / 38.3 | |
| Base EPS = maintenance FCF per ADS (maintenance capex = D&A) | 4.26 | 21.95 | 23.80 | 25.42 | **26.80** (core 24.97) |
| Base growth capex (capex − D&A) per ADS | 2.19 | 8.10 | 7.91 | 6.94 | |
| Base FCF after growth per ADS (no debt amortisation of note) | 2.11 | 13.78 | 16.16 | 18.87 | |
| Base D_t (dividends paid) | 0 (1Q26 dividend paid 8 Oct, before the valuation date) | 4.93 | 6.17 | 7.40 | |
| Base net cash per ADS (year-end) | 19.23 | 28.07 | 38.06 | 49.53 | |
| Base V_t (year-end) | 414.7 (price flat + stub cash) | 447.1 | 474.9 | 499.0 | |
| Bear EPS / FCF per ADS / V_t | | 18.49 / 11.78 / 254.6 | 17.33 / 14.43 / 291.2 | 19.64 / 18.12 / 320.4 | 21.26 |
| Bull EPS / FCF per ADS / V_t | | 23.11 / 13.54 / 523.8 | 26.57 / 16.31 / 606.7 | 29.58 / 19.68 / 690.0 | 32.35 |

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value ·
`[E]` external or secondary · `[C]` carried from an earlier version · `[A]` own assumption ·
`[?]` not found or unverified.

## Header

| Item | Value |
|---|---|
| Company | Taiwan Semiconductor Manufacturing Company Ltd. TWSE: 2330; NYSE: TSM (1 ADS = 5 common shares). Calendar fiscal year; reports in NT$. 2025 revenue **NT$3,809bn = $122.4bn** (+36% in USD), EPS NT$66.25 ($10.65 per ADS) `[F]` (Yahoo, Zacks). **Q3 2026** (to 30 Sep): revenue **NT$1,494.24bn = $46.72bn** (+41.2% y/y in USD), gross margin 66.4%, operating margin 58.7%, net income NT$763.06bn, EPS **NT$29.43 = $4.60 per ADS**, ROE 45.5% `[F]` (management report and call, 15 Oct 2026) |
| Price (P), version 1.2 | **$396.48 per ADS**, Yahoo `TSM` `get_quote` and `get_chart`, NYSE regular close **Tue 10 Nov 2026** (regularMarketTime 21:00:02 UTC; previous close $388.62, +2.0%; day range $387.20–400.21; volume 14.3m vs 11.3m 3-month average; post-market $402.59 at 00:59 UTC 11 Nov, not used). Closes since 1.1: 5 Nov $353.10 (settled close; 1.1 used the $352.03 regular-market print), 6 Nov $375.44, 9 Nov $388.62 `[F]`. Taipei **NT$2,285**, close 10 Nov 05:30 UTC (before the 10 Nov releases); **NT$2,395** on 11 Nov (+4.8%) `[F]`. Market cap $2,056bn (Yahoo) |
| Valuation date, version 1.2 | **10 Nov 2026** / exit 31 Dec 2029, **T = 3.14 years** |
| Check 10 Nov (EDGAR, CIK 0001046179) | Since 5 Nov: **6-K October revenue** and **6-K board resolutions**, both 10 Nov, plus Forms 4 (award filings); no share issue. Yahoo shares outstanding 5,186.47m ADS equivalents, unchanged `[F]` |
| P/E, version 1.2 | **16.92× CY27 ADS consensus $23.43** (kept; Yahoo `earningsTrend` 11 Nov: **$23.39**, 13 analysts, −0.2%, noise; Q4-26 $5.16 (8) unchanged; CY26 $17.50 (11)). **Core P/E 17.64× Base 2027, 15.0× Base 2030.** Net cash at the valuation date **$91.4bn** ($17.61 per ADS): NT$2,985.4bn − 181.5 + 41/92 of Q4 FCF (NT$430bn) = NT$2,996bn at 32.789 `[A]`; end-2026 NT$3,234bn = $98.6bn ($19.02) |
| ADR premium, 10 Nov | **+13.8%** close-on-close ($396.48 vs 5 × NT$2,285 ÷ 32.789 = $348.4); Taipei closed before the releases, the ADS traded after them. At the modelled 10.6% the ADS implies Taipei NT$2,351; Taipei closed NT$2,395 on 11 Nov. Model premium kept at 10.6% |
| FX, version 1.2 | USD/TWD **32.789** (Yahoo `TWD=X` daily close 10 Nov; 32.832 at 07:19 UTC 11 Nov). USD/NOK **9.4010** (Yahoo `NOK=X` daily close 10 Nov; 9.4954 at 07:19 UTC 11 Nov). NOK path (Equity BBB 6 Nov): relative moves unchanged |
| Price (P), version 1.1 | **$352.03 per ADS**, Yahoo `TSM` `get_quote`, NYSE regular close **5 Nov 2026** (regularMarketTime 20:59:59 UTC; previous close $395.75, −11.0%; day range $351.19–380.78; volume 39.2m vs 10.5m 3-month average; post-market $355.87 at 21:08 UTC, not used) `[F]`. Taipei **NT$2,240**, close 5 Nov 05:30 UTC (−0.9%), before the US sell-off `[F]`. Market cap $1,826bn (Yahoo) |
| Price (P), version 1 | **$412.61 per ADS**, Yahoo `TSM`, close 16 Oct 2026 (15 Oct $422.25; 14 Oct $430.00; 5 Oct high $485.8, so −15.1%; 52-week range $266.82–487.47 per Zacks) `[F]`. Taipei: **NT$2,420**, close 16 Oct (−6.4% from NT$2,585 on 6 Oct) `[F]` |
| Valuation date / exit date | **5 Nov 2026** / 31 Dec 2029, **T = 3.16 years** (version 1: 17 Oct, T = 3.21) |
| Shares | **25,932m** diluted (Q3 weighted average) `[F]` = **5,186.5m ADS equivalents** (Zacks 5,186.5) `[F]`. Held flat: TSMC does not buy back stock; restricted stock awards are tiny. EDGAR list since 1 Jul 2026: 14 Forms 6-K and 153 Forms 4 (insider award filings); no share issue. **Check 5 Nov:** since 15 Oct only a 6-K of 22 Oct (September monthly report: insider holdings, pledges, asset deals, appropriations, bonds, share cancellations), a Schedule 13G (27 Oct) and a Form 4 (3 Nov); no share issue, no revenue release. Yahoo shares outstanding 5,186.47m ADS equivalents (25,932.37m shares) `[F]` |
| Market cap / EV | **$2,140bn** at the ADS price (Yahoo $2,140bn); $1,935bn at the Taipei price (NT$62.76tn at 32.428). **Net cash ≈ $88.9bn at the valuation date** `[A]` ($17.14 per ADS): NT$2,985.4bn on 30 Sep `[F]`, less the 1Q26 dividend paid 8 Oct (NT$181.5bn) `[F]`, plus 17 days of Q4 free cash flow. **EV ≈ $2.05tn** |
| P/E, version 1.1 | **15.02× CY27 ADS consensus $23.43** (Yahoo `earningsTrend`, 14 analysts, 5 Nov; 30 days ago $21.92; Q4-26 $5.16 (8), Q1-27 $5.19 (10), CY26 $17.49 (12)); Taipei forward EPS NT$149.53. **Core P/E 15.58× Base 2027, 13.2× Base 2030.** Net cash at the valuation date **$90.0bn** ($17.35 per ADS): NT$2,985.4bn − 181.5 + 36/92 of Q4 FCF (NT$430bn) = NT$2,972bn at 33.027 `[A]`; end-2026 NT$3,234bn = $97.9bn ($18.88) |
| P/E, version 1 | **17.85× CY27 ADS consensus $23.11** (Yahoo, 14 analysts, 17 Oct); 23.8× CY26 ($17.31, 12). Taipei 16.3× CY27 NT$148.61 (36). **Core P/E** (price less net cash, EPS less net interest): **18.7× Base 2027, 15.8× Base 2030**. Zacks F1/F2 $16.65 / $21.50 (9 each; most recent $16.92 / $22.26): lags the post-Q3 revisions, not used |
| P/B | 11.7× (Taipei line, Yahoo `2330.TW`) `[F]`. Yahoo's ADS P/B (64.7) mixes currencies and is not used |
| ADR premium, 5 Nov | **+3.8%** close-on-close ($352.03 vs 5 × NT$2,240 ÷ 33.027 = $339.1), **not simultaneous**: Taipei closed ~15 hours before the US sell-off. 4 Nov: +14.9% ($395.75 vs NT$2,260 at 32.818). At the modelled 10.6% the ADS implies Taipei NT$2,102 (−6.2%) `[A]`. Model premium kept at 10.6% (version 1). **Memo 6 Nov:** Taipei had not yet traded on 6 Nov when checked (Yahoo `2330.TW` still the 5 Nov close NT$2,240, market state pre-open; USD/TWD 33.125 at 00:23 UTC); read the 6 Nov close before judging the premium. The valuation price stays the 5 Nov ADS close |
| ADR premium, version 1 | **+10.6%** (16 Oct closes: $412.61 vs 5 × NT$2,420 ÷ 32.428 = $373.1) `[F]`; 2-year mean 19.5% (median 19.8%, range 6.9–33.8%), 6-month mean 13.8% `[A]` (Yahoo daily closes). Held constant to exit |
| NAVs (Step 3) | Not applicable (no asset marks). V_T = exit P/E × normalised 2030 core EPS + net cash at exit |
| FX, version 1.1 | USD/TWD **33.027** (Yahoo `TWD=X`, 5 Nov 21:09 UTC; NT$ 1.8% weaker than on 16 Oct and 3.9% weaker than the Q4 guide's 31.8: a gross-margin tailwind of roughly 1.5 pp by TSMC's rule of thumb `[E]`, not modelled; consensus carries it). USD/NOK **9.3105** (Yahoo `NOK=X`, 5 Nov 21:09 UTC; 9.3095 quoted with the task). NOK path (Equity BBB): relative moves Bear +12% in 2027, +9% in 2028–29, Base flat, Bull −3% |
| FX, version 1 | USD/TWD **32.428** (Yahoo `TWD=X`, 16 Oct close); used to convert NT$ balance-sheet and cash-flow items at spot. TSMC's Q4 guide assumes 31.8. NOK memo at USD/NOK **9.4135** (Yahoo `NOK=X`, 17 Oct 2026), moved with the Equity BBB USD/NOK path relative to spot (Bear +12% in 2027, +9% in 2028–29; Base flat; Bull −3%) |
| Track | **B.** Capex is 35% of revenue in 2026 and free cash flow is 40–75% of net income (2026 quarters 41–62%; model years 63–74%); the AI BBB's Bear is a capacity overshoot (H3 index −10% in 2028). FCF build per year, V_T on normalised 2030 EPS, P_k |
| k | **12%**, not raised: net cash, very liquid (~10.5m ADS a day, ~$4.3bn, Zacks 20-day average). The concentration of production in Taiwan is not one of the skill's reasons to raise k and is a tail the AI BBB does not model; P_k at 13% and 14% is shown ($352 / $343). Raising k only widens the fail |
| Horizon | 1.2: stub **10 Nov**–31 Dec 2026 (51/92 of Q4 left). 1.1: stub 5 Nov–31 Dec 2026 (Q4 guide; 56/92 of Q4 left; Q4 report **~14 Jan 2027**, Yahoo `calendarEvents`, an estimate; Zacks had 21 Jan) + 2027–2029 annual; exit on 2030 normalised EPS |

**Sources (connector · document · period):**
- **TSMC 3Q26 Management Report** (investor.tsmc.com, 15 Oct 2026, quarter to 30 Sep) `[F]`: income
  statement, platform, node and region mix, balance sheet, net cash reserves, cash flow, capex,
  free cash flow, the 2Q26 dividend dates.
- **TSMC 3Q26 earnings call transcript** (LSEG StreetEvents via tsmc.com, 15 Oct 2026) `[F]`: 2026
  growth ~44%, capex $60–64bn, 2026–28 capex well above 2023–25, overseas dilution, AI accelerator
  CAGR, N2, N3 and A14 capacity, pricing, Q&A on demand, power and funding.
- **TSMC Q3 release** (pr.tsmc.com/english/news/3346) `[F]`; **6-K of 11 Aug 2026** (board:
  NT$7.0 dividend for 2Q26, ex 10 Dec 2026, paid 7 Jan 2027; capital appropriations $29.4bn) and
  **6-K of 8 Oct 2026** (September revenue) `[F]`; 6-K on the 1Q26 dividend (NT$7.0, paid 8 Oct
  2026) `[F]`. EDGAR submissions list (CIK 0001046179) for the filing check.
- **Yahoo** (16–17 Oct 2026): prices (TSM, 2330.TW), `earningsTrend` (ADS and Taipei), dividends,
  2-year daily closes (ADR premium), 6-year monthly closes, USD/TWD, USD/NOK.
- **Zacks** (16–17 Oct 2026): EDT estimates, broker ratings (60 days), profile (Rank, targets,
  dividend net of withholding), three news items of 15–16 Oct. No full Zacks research report
  exists for TSM.
- **KGI research note** on TSMC's January 2026 guidance `[E]`: 2024–29 revenue CAGR ~25%, AI
  accelerators mid-to-high 50s, long-term gross margin 56% and higher.
- **Workspace:** `docs/ai-market-bbb.md` (15/16 Oct); `docs/nvda-analysis.md` (17 Oct);
  `docs/equity-market-bbb.md` (11 Oct); `docs/hy-market-bbb.md` (NIBOR);
  `docs/portfolio-overview.md` (HY book); `docs/dnb-teknologi-analysis.md` (TSM weight).

## Scenario definitions (from AI Market BBB and Equity Market BBB)

| Scenario | Catalyst | What it does to TSMC |
|---|---|---|
| **Base** (decision) | AI BBB: contracted 2027 build (hyperscaler capex +42%, H1 compute +55%), then digestion (H1 +10% in 2028, +3% in 2029); H3 index 125 / 140 / 151. Inside the equity Base (AI boom slows to trend) | **1.1:** EPS = H3 layer path × CY27 consensus (**$23.43**): **$22.26 / $24.14 / $25.78** and **$27.18** in 2030. Version 1 ($23.11): $21.95 / $23.80 / $25.42 (2027–29) and $26.80 in 2030. Revenue $220 / 247 / 266bn `[A]`. Capex $76 / 82 / 85bn. Exit P/E 18 |
| **Bear** (stress) | AI BBB **financing break** (a lab misses commitments, AI credit tightens, 2028 hyperscaler capex −16%) plus the **capacity overshoot in 2028** (H3 index 110 / 99 / 104), inside the equity Bear (recession H1 2027 + oil Bear). Since 5 Nov the AI BBB names **US state siting policy** as a second route to the 2028 capex cut. Earliest H1 2027 | **1.1:** EPS $17.81 / $14.76 / $15.70, and $16.64 in 2030 (layer **.76 / .63 / .67 / .71**, the reconciled H3 Bear; net margin 47.6 / 44.0 / 44.5%). Version 1: $18.49 / $17.33 / $19.64 / $21.26 (.80 / .75 / .85 / .92). Exit P/E 14, reached at end-2027. Capex cut to $70 / 60 / 55bn; dividend steps halved |
| **Bull** (stress) | AI BBB **agentic adoption** (lab revenue +130% in 2027, capex $1.3–1.7tn), inside the equity Bull (soft landing). Earliest Q2 2027 | **1.1:** EPS at consensus in 2027 ($23.43), then $26.95 / $30.00, and $32.81 in 2030 (layer 1.00 / 1.15 / 1.28 / 1.40). Exit P/E 21. Capex $82 / 95 / 105bn |

The stub (17 Oct–31 Dec 2026) is the same in all scenarios: TSMC's Q4 guide and the Q4 consensus,
day-weighted, with the price flat by convention. Bear and Bull diverge from 1 Jan 2027.

## Company and status

- **Q3 2026 in numbers** `[F]` (management report, 15 Oct 2026; NT$bn unless stated):

| | 3Q25 | 2Q26 | **3Q26** | 4Q26 guide |
|---|---|---|---|---|
| Revenue US$bn | 33.10 | 40.20 | **46.72** | 52.3–54.3 (+14% q/q, +58% y/y at the midpoint) |
| Revenue | 989.92 | 1,270.38 | **1,494.24** | at 31.8 NT$/US$ |
| Gross margin | 59.5% | 67.7% | **66.4%** | 65–67% |
| Operating margin | 50.6% | 60.3% | **58.7%** | 56.5–58.5% |
| Net income | 452.30 | 706.56 (incl. VIS disposal gains) | **763.06** | |
| EPS NT$ / US$ per ADS | 17.44 / 2.92 | 27.25 / 4.31 | **29.43 / 4.60** | consensus NT$32.96 (22) / $5.16 (8) |
| Wafer shipments (k 12-inch eq.) | 4,085 | 4,336 | **4,476** (+9.6% y/y) | |
| Average NT$ per US$ | 29.91 | 31.60 | 31.98 | 31.8 |

  - Revenue grew 41% in USD on 9.6% more wafers: **growth is price and mix** (2 nm 8% and 3 nm 33%
    of wafer revenue; 7 nm and below 79%).
  - Platforms: **HPC 68%** of revenue (+22% q/q; 57% a year ago), smartphone 21%, IoT 4%,
    automotive 4%. Customers in North America 79%, China 5%.
  - Nine months: NT$3,898.7bn (+41.1%) `[F]` (6-K, 8 Oct). Management now expects **2026 revenue
    growth of about 44% in USD** (~$176bn) `[F]`.
- **Margins** `[F]` (call):
  - Q4 gross margin down 0.4 pp at the midpoint: N2 ramp and overseas fabs, partly offset by cost
    work.
  - Overseas fab dilution about 2 pp in 2026, **widening to 3–4 pp** in the later years of the
    five-year plan as more US fabs ramp.
  - Long-term gross margin target **56% and higher** through the cycle (January 2026) `[E]`; the
    actual is 10 pp above it. The CEO says profitability has no ceiling but will not jump.
  - Rule of thumb: 1% move in NT$/US$ ≈ 0.4 pp of gross margin `[E]`. Spot 32.43 is 2% weaker NT$
    than the Q4 guide's 31.8: a small tailwind.
- **Capacity and capex** `[F]` (call, 6-K):
  - 2026 capex **$60–64bn** reiterated (nine months $40.64bn); capex for **2026–28 to be well above
    the previous three years** ($101bn in 2023–25); revenue should keep growing faster than capex.
    The August board approved **$29.4bn** of capital appropriations; the **November board (10 Nov)
    approved $40.93bn** (advanced and packaging capacity, fab construction, 2027 R&D and sustaining
    capex) `[F]`. The same board approved up to $0.5bn each for **Anthropic common shares at the IPO
    price**, **OpenAI preferred stock** and a new strategic investment company `[F]`: ≤ $1.5bn in
    all ($0.29 per ADS, cash into stakes at cost), immaterial; not modelled.
  - Nearly 20 fabs in progress: 13 leading-edge and advanced-packaging fabs in Taiwan and five to
    six abroad. **N2 capacity more than doubles in 2027**; A14 in volume from 2028 (more customer
    activity than N2 had). Two new N3 fabs in Tainan (volume 1H27 and 1H28); **Arizona fab 2 in
    volume Q3 2027** (ahead of plan); Japan fab 2 on N3 in 2028; Texas and a customer's "Terafab"
    under evaluation.
  - Management says **demand is still well above what TSMC can supply** and that it checks
    customers' customers, data-center build-outs and US power before adding capacity. It plans
    2027 **prudently for consumer and price-sensitive segments** hit by rising component (memory)
    prices.
  - AI accelerators (narrow definition) were guided to grow at a **mid-to-high 50s% CAGR 2024–29**;
    the CEO said it will "probably be higher". AI CPUs and networking come on top.
  - Pricing: set by segment, node and location; US-made wafers priced differently. Reports of price
    increases were not confirmed in numbers `[?]`.
- **Balance sheet and cash** `[F]` (30 Sep 2026):
  - Cash and marketable securities NT$4,016.98bn ($124bn at spot); interest-bearing debt
    NT$1,031.58bn (current portion NT$213.20bn); **net cash NT$2,985.40bn** (+NT$499bn in the
    quarter).
  - Q3 operating cash flow NT$919.77bn (after NT$197.55bn of tax paid); capex NT$443.21bn
    ($13.84bn); other investing **+NT$198.74bn, mainly US Treasury investment tax credits**; free
    cash flow **NT$476.56bn**. Net interest income NT$31.66bn in the quarter.
  - Days of receivables 28, inventory 82. Dividends payable NT$363.05bn (1Q26 and 2Q26 declared).
- **Dividends** `[F]`: quarterly, raised each year (NT$4.5 → 5.0 in 2025; 6.0 → 7.0 in 2026).
  1Q26 NT$7.0 paid 8 Oct 2026; **2Q26 NT$7.0: ex 10 Dec 2026 (shares and ADS), paid 7 Jan 2027.**
  **3Q26 NT$9.0** (board, 10 Nov 2026; +NT$2.0, the largest step so far): ex **11 Mar 2027** (shares
  and ADS), record 17 Mar, paid **8 Apr 2027** `[F]` (6-K, 10 Nov).
  Policy: sustainable and steadily rising dividend per share, annual and quarterly. Taiwan
  withholds **21%** on dividends to non-residents (Zacks shows $0.87 per ADS net against $1.107
  gross for the September ex-date) `[E]`.

## Near term: stub (all scenarios)

| USD | Q3-26 actual | Q4-26 guide | Q4-26 consensus | Stub (17 Oct–31 Dec; 76/92 of Q4) |
|---|---|---|---|---|
| Revenue $bn | 46.72 | 52.3–54.3 | 53.5 (Zacks) | 44.0 |
| Gross / operating margin | 66.4% / 58.7% | 65–67% / 56.5–58.5% | | |
| EPS per ADS | 4.60 | ≈ 5.0–5.1 implied `[A]` | **5.16** (8, Yahoo); NT$32.96 (22); Zacks 4.74 (5, stale) | **4.26** |
| Capex $bn | 13.84 | 19.4–23.4 implied by $60–64bn for 2026 | | 17.4 (Q4 at $21.4bn) |
| Free cash flow | NT$476.6bn | ≈ NT$430bn `[A]` (net income 855 + D&A 240 − capex 685 + credits 20) | | NT$355bn = $11.0bn ($2.11 per ADS) |
| Dividend | 4Q25 NT$6.0 paid in Q3 | 1Q26 NT$7.0 paid 8 Oct: **before the valuation date, not counted** | 2Q26 NT$7.0, ex 10 Dec, paid 7 Jan 2027: counted in 2027 D_t ($1.08 per ADS gross) | — |
| Net cash, 31 Dec | NT$2,985.4bn (30 Sep) | | | ≈ NT$3,234bn = **$99.7bn** ($19.23 per ADS) `[A]` |

- **1.2 (11 Nov): October revenue, the Q4 check.** October **NT$586.89bn** (+14.7% m/m, **+59.7%
  y/y**); January–October NT$4,485.62bn (+43.3%) `[F]` (6-K, 10 Nov).
  - In USD: **$17.9bn** at today's 32.789 (~$18.2bn at October's average of ~32.3 `[A]`, Yahoo
    month open 31.87, close 32.61). One third of the guide is $17.4–18.1bn: October runs at
    **~$53.7bn a quarter at spot**, the upper half of the $52.3–54.3bn guide, not above its top.
  - In NT$ (TSMC's own reporting): October × 3 = NT$1,761bn against the guide's NT$1,663–1,727bn at
    31.8; the excess is the weaker NT$ (32.3–32.8), which the guide's USD range already absorbs.
  - Seasonality cuts the other way: October 2025 was **35.1%** of Q4-25 (NT$367.47bn of
    NT$1,046.09bn) `[F]`; on that share Q4-26 is ~NT$1,672bn, in line with the consensus NT$1,708bn
    (26 analysts).
  - **Reading: Q4 tracks the guide, at most its upper half. Not clearly above, so the stub is kept**
    at the Q4 consensus (EPS $5.16, 8 analysts, unchanged), now 51/92 of the quarter (revenue
    $29.5bn, EPS $2.86, FCF after growth $1.40 per ADS). The y/y rate (+59.7%) sits above the +45%
    Bull-side signpost for the second month; the Q4 guide already implied +58% in USD, so it
    confirms the guide rather than beating it.
  - The November board (10 Nov) set the **3Q26 dividend at NT$9.0** (model NT$8.0): it replaces the
    assumption for the April 2027 payment (Common assumptions). Appropriations $40.9bn support the
    January capex signpost (≥ $75bn); not modelled.
  - Next monthly print: **November revenue ~10 Dec** (date not confirmed).
- **1.1 (5 Nov):** the stub now runs 5 Nov–31 Dec (56/92 of Q4: revenue $32.4bn, EPS $3.14 per
  ADS, FCF after growth $1.53 per ADS). The Q4 consensus is unchanged ($5.16 per ADS, 8 analysts;
  revenue NT$1,708bn, 26). **October revenue is not out** (EDGAR and TSMC newsroom checked 5 Nov;
  the last monthly release is September, 8 Oct); expected **~10 Nov** (TSMC's usual ~10th; date not
  confirmed). The hyperscalers' Q3 reports (28–30 Oct) left K1 2027 at $1,120bn (AI BBB).
- **Before the Q4 report:** October revenue (~10 Nov), the November board (3Q26 dividend, new
  appropriations; date not verified), the hyperscalers' first 2027 capex signals (27–30 Oct), NVIDIA's Q3 FY27
  (17 Nov). **Q4 report (mid-January 2027):** the first 2027 revenue and capex guide, the test of
  the Base 2027 step.
- The model takes consensus for the stub; a beat moves the starting cash, not the path.

## Market input (AI Market BBB rows used and how they enter)

| TSMC item | AI BBB row | Bear / **Base** / Bull | Company adjustment |
|---|---|---|---|
| **EPS** (calendar years; CY27 consensus = 1.00 = **$23.43**, 5 Nov; version 1 $23.11) | **H3 layer EPS path** | 2027: **.76** / **.95** / 1.00 · 2028: **.63** / **1.03** / 1.15 · 2029: **.67** / **1.10** / 1.28 · 2030 normalised: **.71** / **1.16** / 1.40 (Bear reconciled in AI BBB Update 2, 17 Oct; version 1 .80 / .75 / .85 / .92) | None (tests below) |
| **Exit P/E** on 2030 EPS | H3 reference 14 / **18** / 21 | Used as the IAF exit multiple, with independent cross-checks (Common assumptions) | Applied to core EPS (net interest removed) because net cash is added at face |
| Revenue | H3 index 2026 = 100: Bear 110 / 99 / 104; **Base 125 / 140 / 151**; Bull 132 / 156 / 175 | × TSMC 2026 revenue ~$176.1bn | Working capital only |
| Scenario mechanism and signposts | Financing break, capacity overshoot, agentic adoption; capex guidance, NVIDIA Q3 | As above | TSMC monthly revenue, gross margin, dividend and the ADR premium added |
| Comparison | H3 basket (TSM, ASML, AMAT, LRCX): Base 1.1% (NOK), P/E 21.5 on CY27, hurdle P/E 15.7 (14/15 Oct prices) | — | TSMC at 17.85× CY27 |

- **CY27 consensus anchor.** Yahoo's ADS consensus rose from $22.32 (15 Oct, used in the AI BBB) to
  **$23.11** after the Q3 beat (+3.5%). The Taipei consensus (NT$148.61, 36 analysts) gives $22.91
  at spot (−0.9%): the two agree. Zacks ($21.50, 9) has not caught up. Yahoo's ADS figure is the AI
  BBB's own source and is used; Zacks is a sensitivity (5.1%).
- **Tests of the H3 Base path against TSMC's own data:**
  1. **Management's long-term target.** Base revenue of $266bn in 2029 is a **24% CAGR from 2024**
     ($90.1bn), about management's ~25% target for 2024–29 `[E]`. The Base path is not a bear view
     of TSMC; it is management's long-term rate with the AI BBB's shape (fast 2027, slow 2028–29).
  2. **Bottom-up 2027 via the H1 path** `[A]`: if HPC (about 66% of 2026 revenue) grows ~40% (less
     than H1's +55% in dollars, which carries HBM costs and NVIDIA's margin) and the rest ~5%
     (consumer pressure), TSMC grows ~28% in 2027. Base 2027 is +25%; consensus is ~+36%.
  3. **Q4-26 run-rate (flag).** The Q4 guide annualised is ~$213bn, 121% of the 2026 average. Base
     2027 revenue ($220bn) is only 3% above that run-rate, and Base 2027 EPS ($21.95) only 6% above
     the Q4 consensus annualised ($20.64). That leaves little for N2 doubling, two new N3 fabs and
     Arizona fab 2 in 2027. It is the same base effect found in the H2 memory index (see For other
     modules). It is not changed here because consensus 2027 is the Bull row and the management
     path is a sensitivity (10.2%), which still fails.
  4. **Margins.** The Base EPS on the H3 revenue index implies a net margin of ~50% (gross margin
     ~64–66%) through 2029, i.e. no reversion to the 56% long-term floor. A reversion toward it
     (2030 EPS ×0.83) gives **1.7%**: margin is the larger downside risk in the Base, not volume.
- **1.1 (5 Nov): the flag below is closed.** The AI BBB adopted TSMC's revenue-consistent Bear as the
  H3 Bear in Update 2 (17 Oct), so it is now the Bear decision row (−8.5% at $352.03). The old path
  is a sensitivity (−1.1%). The base-effect flag (point 3 above) stays open: the AI BBB kept the
  index and added a run-rate memo.
- **Version 1: the H3 Bear EPS path does not fit TSMC.** On the layer's Bear revenue (index 110 / 99 / 104),
  TSMC's net margin must rise from 49.5% to 51.6% and 55.6% while revenue falls 10% in 2028 and
  depreciation rises. In 2023 (revenue −9% in USD) TSMC's net margin fell from 45% to 39% `[E]`. At net
  margins of 47 / 43 / 44 / 45%, TSMC's Bear EPS is about **.76 / .63 / .67 / .71** `[A]`. The
  layer path is the Bear decision row (the rule); the revenue-consistent Bear (−13.2%) is reported
  beside it and flagged.
- **Equity Market BBB (17/18 Oct, read in 1.1):** same scenarios and NOK path relative moves. In
  the Bear TSMC falls 37% in USD in 2027 (−29% in NOK) against World's −28.4% in USD (−20.6% in
  NOK). World Base is 5.2%. TSMC's Base exit P/E 18 is one turn above World's 17; its Bear 14 is
  below World's Bear 15 (exit cross-check under the V_T bridge).
- **Version 1 (Equity BBB of 11 Oct):** the Bear is the recession world; there TSMC falls 38% in USD in 2027
  against World's −27% (−18% in NOK). Zacks beta 1.37. The hot US CPI and rate move (14 Oct) acts on
  the exit multiple; the ±2 P/E sensitivity covers it. TSMC is in MSCI Emerging Markets, not in
  MSCI World, so it is not in the global index funds.

### NVIDIA as input (`docs/nvda-analysis.md`, version 1.1 of 2 Nov; version 1 of 17 Oct below)

- **1.1 (2 Nov, price 30 Oct): the demand signal TSMC reads is unchanged.** No NVIDIA report or
  filing since version 1; supply and capacity commitments still **$279bn** ($92bn rest of FY27,
  $87bn FY28, $88bn FY29, primarily memory and manufacturing): flat after the 2027 step, as in the
  Base. NVIDIA's Q3 FY27 on **17 Nov** (Q4 guide, supply commitments) is the next read. NVIDIA now
  leads with the cycle and puts the CY27 basis on calendar quarters ($15.21); its Bear is the
  reconciled H1 path (.68 / .50 / .53 / .57).

| 1.1 | NVIDIA (2 Nov, $204.64) | **TSMC (5 Nov, $352.03)** |
|---|---|---|
| P/E on CY27 consensus | 13.45 (calendarised $15.21) | **15.02** ($23.43) |
| Layer EPS path Base (2027 / 2030) | .92 / .97 (H1) | **.95 / 1.16** (H3) |
| Layer Bear path (2027 / 2028 / 2030) | .68 / .50 / .57 | **.76 / .63 / .71** |
| Exit P/E Bear / Base / Bull | 13 / 17 / 19 | **14 / 18 / 21** |
| Base IRR (USD) / margin of safety | 13.3% / +3.5% | **13.7% / +4.8%** |
| Bear IRR / 2027 in USD | −11.4% / ~−45% | **−8.5% / −37%** |
| E / R (reference) | 0.154 (against 0.196) | **0.206** (against 0.254) |
| Price implies (k) | 0.96× Base 2028–30 | **0.95× Base 2028–30** |

  - On 5 Nov NVIDIA traded at ~$183 intraday (AI BBB market-mood table, −8.5% on the day), well below
    its own P_k ($211.7); its document has not been re-marked. On their own builds both now clear;
    TSMC has the steadier earnings and the smaller Bear loss, NVIDIA the cheaper multiple.

**Version 1 (17 Oct):**

- **NVIDIA's path is TSMC's largest growth driver.** Both analyses sit on the same AI BBB: H1 +55%
  in 2027, then +10% and +3%. NVIDIA's management expects FY28 supply-limited "through at least the
  end of that year"; the supply is TSMC's CoWoS and N3, plus HBM. TSMC says the same from the other
  side (demand above supply).
- **NVIDIA's supply commitments support the Base shape.** NVIDIA's $279bn of supply and capacity
  commitments (primarily memory and manufacturing) run $92bn for the rest of FY27, **$87bn in FY28
  and $88bn in FY29**: flat after the 2027 step. Weak evidence (commitments are added every quarter;
  $119bn → $279bn in one quarter), but it matches a contracted 2027 followed by a plateau.
- **Custom silicon is NVIDIA's risk, not TSMC's.** Broadcom's AI chips, Google's TPUs, AMD's MI450
  and Marvell are all made at TSMC. A shift within H1 moves share between TSMC's customers. TSMC's
  competitive risks are Intel Foundry (14A, EMIB-T packaging) and an IDM customer insourcing,
  which the CEO did not rule out but says are in its plan `[F]`.
- **Rubin raises silicon per gigawatt** ($40bn of NVIDIA revenue per GW vs $25bn for Blackwell
  `[E]`); larger packages (TSMC is in volume on 5× reticle CoWoS, working on 9× and 14×) mean
  more TSMC content per system.
- **Side by side on the same baseline:**

| | NVIDIA | **TSMC** |
|---|---|---|
| P/E on CY27 consensus | 13.46 | **17.85** |
| Layer EPS path Base (2027 / 2030) | .92 / .97 (H1) | **.95 / 1.16** (H3) |
| Layer Bear path (2027 / 2028 / 2030) | .70 / .60 / .75 | **.80 / .75 / .92** |
| Exit P/E Bear / Base / Bull | 13 / 17 / 19 | **14 / 18 / 21** |
| Base IRR (USD) / margin of safety | 13.0% / +2.8% | **7.4% / −12.2%** |
| Bear IRR / 2027 in USD | −4.0% / −36% | **−6.3% / −38%** |
| Revenue-consistent Bear | −11.3% | **−13.2%** |
| E / R | 0.184 | **0.079** |
| Where the Base return comes from | Re-rating 13.5 → 17 on flat earnings | Earnings growth at an unchanged multiple |

  - TSMC's earnings are steadier in every scenario, but the market already pays for that: its
    multiple is a third higher, and in the Bear the multiple has further to fall (18.7 → 14).
    **NVIDIA is the cheaper way into the same AI path.**

## Common assumptions

- **EPS basis:** as reported (TSMC has no adjusted EPS), per ADS in USD = 5 × NT$ EPS ÷ NT$/US$.
  Consensus is on that basis. The path's EPS includes net interest income (Q3: NT$31.66bn, about
  $0.16 per ADS a quarter).
- **Shares:** 25,932m, flat (no buybacks; restricted stock awards immaterial). Retained cash builds
  net cash, which enters V_T at face value (counted once).
- **Net interest and V_T** `[A]`: because net cash is added at face, the exit P/E is applied to
  **core EPS** = EPS less after-tax net interest on net cash (4.0% pre-tax, 17% tax = 3.3%; Q3
  actual 4.6% annualised). Otherwise the cash would be counted twice (once in EPS × P/E, once at
  face). 2030 core EPS: Base $24.97 (EPS $26.80). Without the strip, Base is 9.6% (sensitivity).
- **1.2 changes to the common assumptions** (everything else as 1.1):
  - **Dividends:** the declared 3Q26 NT$9.0 (paid 8 Apr 2027) replaces the model's NT$8.0 in all
    scenarios. TSMC has not cut a dividend, so each ladder keeps its pace from the new level: Base
    +NT$1.0 every half-year, paid 2027 7 / 9 / 9 / 10 = **NT$35**, 2028 **NT$44**, 2029 **NT$52**
    ($5.34 / 6.71 / 7.93 per ADS); Bear held at 9 for a year, then +0.5 (NT$34 / 38 / 42); Bull
    +1.5 (NT$35.5 / 49.5 / 60). The extra payout leaves net cash (counted once): Base net cash at
    exit $50.53 → **$48.86** per ADS, Bear $38.76, Bull $47.78. Second-order interest on the
    lower cash is ignored (< $0.05 per ADS).
  - NT$ items at USD/TWD 32.789 (dividends per ADS +0.7% in USD); net cash $91.4bn at 10 Nov (41/92
    of Q4 FCF elapsed), $98.6bn at 31 Dec. EPS anchor $23.43 kept (Yahoo 11 Nov $23.39, −0.2%).
  - Interim V_t: core P/E glides from today's **17.64** to 18.0 (17.76 / 17.88 / 18.0 at end-2027 /
    2028 / 2029); Bear at 14 from end-2027, Bull to 21 as 1.1.
  - Rebuilt in the session scratchpad from this document's inputs; it reproduces 1.1 exactly (Base
    13.71% / $368.9, Bear −8.47% / $189.6, Bull 25.95% / $506.5, weighted 12.7%).
- **1.1 changes to the common assumptions** (everything else below is unchanged):
  - EPS anchor $23.43 (Yahoo, 5 Nov); Bear path .76 / .63 / .67 / .71. Free cash flow moves with net
    income one-for-one (capex, D&A, credits and working capital as version 1).
  - NT$ items at USD/TWD 33.027: dividends per ADS fall ~1.8% in USD (Base $4.84 / 6.06 / 7.27);
    net cash $90.0bn at 5 Nov (36/92 of Q4 FCF elapsed), $97.9bn at 31 Dec.
  - Interim V_t: core P/E glides from today's **15.58** (Base 2027 core EPS $21.48) to the exit P/E
    (Base 16.39 / 17.19 / 18.0 at end-2027 / 2028 / 2029; Bull to 21; the Bear at 14 from end-2027).
  - Interest strip: 3.32% after tax on average net cash (2030 core EPS Base $25.31, Bear $15.15,
    Bull $31.01).
  - The model was rebuilt in the session scratchpad from the inputs in this document and reproduces
    version 1 exactly (Base 7.45% / $362.1; Bear −6.32% / $235.8; Bull 18.82% / $497.1;
    revenue-consistent Bear −13.20% / $186.3).
- **Net cash at the valuation date (version 1)** `[A]`: NT$2,985.4bn on 30 Sep less the 1Q26 dividend
  (NT$181.5bn, paid 8 Oct) plus 17/92 of Q4 free cash flow (NT$430bn) = NT$2,883bn = $88.9bn.
  Converted at spot 32.428 (30 Sep: 31.85); if part of the cash is held in USD, the figure is up to
  ~$1bn higher; not material.
- **Revenue** (working capital only) = H3 index × 2026 revenue ~$176.1bn (nine months $122.8bn + Q4
  guide midpoint $53.3bn). Working capital = 10% of the revenue change `[A]` (receivables 28 days,
  inventory 82 days of cost, less payables).
- **Capex, D&A and credits** `[A]`:

  | $bn | 2026 | 2027 | 2028 | 2029 | Basis |
  |---|---|---|---|---|---|
  | Capex Base | 62 | **76** | **82** | **85** | Guide $60–64bn; 2026–28 well above 2023–25 (call); revenue to grow faster than capex (capital intensity 35% → 32%) |
  | Capex Bear / Bull | | 70 / 82 | 60 / 95 | 55 / 105 | Bear: 2027 tools already appropriated, then cuts; Bull: intensity held ~34–35% |
  | D&A (= maintenance capex) Base | ~26 | 34 | 41 | 49 | 85% of the previous five years' capex over five years (fits 2026's ~$26bn); Bear 34 / 40 / 45, Bull 34 / 42 / 53 |
  | US investment tax credits | ~8 | 4 | 4 | 4 | Q3 NT$198.7bn (~$6.2bn), Q2 NT$40.2bn; Bear $3bn |

- **Dividends** `[A]` (NT$ per share, paid in the year; ADS paid ~1 week after Taipei):
  Base raises the quarterly dividend NT$1.0 every half-year, the 2026 pace: 2027 7 / 8 / 8 / 9 =
  **NT$32** ($4.93 per ADS); 2028 NT$40 ($6.17); 2029 NT$48 ($7.40). Payout of EPS rises from 22% to
  29%. Bear raises by NT$0.5 every half-year (NT$30 / 34 / 38); Bull by NT$1.5 (NT$34 / 46 / 58).
  The rest is retained as net cash. Before Taiwan's 21% withholding (memo −0.2 pp).
- **Exit P/E (independent of the IAF ceiling):** Base **18**, Bear **14**, Bull **21** on 2030 core
  EPS (the AI BBB H3 reference). Cross-checks:
  - TSM's year-end ADS price over the next year's realised EPS, 2021–25: **18.3 / 14.4 / 14.8 /
    18.5 / 17.3** (mean 16.7) `[A]` (Yahoo month-end closes; EPS NT$ ÷ average FX). Those years
    carried an ADR premium of 15–25%; today's is 10.6%.
  - Today: 17.85× CY27 consensus; core 18.7× Base 2027 and 15.8× Base 2030.
  - **18 is not conservative for TSMC:** it is the top of its own five-year range on realised
    earnings, for earnings growing ~6% a year by 2030. 16.7 (the five-year mean) gives 5.3%.
- **ADR premium** `[A]`: held at 10.6% to exit (the exit P/E is on the ADS). Sensitivities: the
  2-year mean (19.5%), the 2-year low (6.9%) and parity. The premium persists because shares cannot
  freely be converted into ADSs `[E]`.
- **Interim V_t:** core P/E on next-year core EPS glides from today's 18.68 to the exit P/E (Base
  18.46 / 18.23 / 18.0 at end-2027 / 2028 / 2029); the Bear reaches 14 at end-2027. Plus net cash.
  Path diagnostic only.
- **Debt:** NT$1,031.6bn of bonds and loans, rolled or repaid from cash; net cash unchanged by
  maturities, so there is no amortisation line.
- **NOK memo:** the Equity BBB USD/NOK path relative to spot.

## Period tables and year-end path

### Version 1.2 (10 Nov 2026, $396.48)

Revenue, net income, EBITDA, EPS and FCF after growth are as in the 1.1 table below (no path moved).
What differs is the dividend ladder and, through it, net cash:

| | Base 2027 | 2028 | 2029 | Bear 2027 | 2028 | 2029 | Bull 2027 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|---|
| D_t paid, NT$ per share / per ADS | 35 / 5.34 | 44 / 6.71 | 52 / 7.93 | 34 / 5.18 | 38 / 5.79 | 42 / 6.40 | 35.5 / 5.41 | 49.5 / 7.32 | 60 / 9.15 |
| Net cash per ADS (year-end; 19.02 at end-2026) | 27.77 | 37.55 | 48.86 | 24.93 | 31.00 | 38.76 | 27.46 | 36.82 | 47.78 |

**Year 1 (2027) dividends paid, Base:** NT$7 / 9 / 9 / 10 = $1.07 / 1.37 / 1.37 / 1.53 per ADS at
32.789 (Jan, Apr, Jul, Oct).

**Year-end path, 1.2** (USD per ADS; r_t from the end-2026 mark $397.9 = price flat + stub cash):

| | End-2026 | 2027 | 2028 | 2029 (exit) |
|---|---|---|---|---|
| **Base** D_t / V_t | 0 / 397.9 | 5.34 / 436.8 | 6.71 / 472.0 | 7.93 / **504.4** |
| Base r_t / IRR to year-end | +0.4% (stub) | +11.1% / +10.1% | +9.6% / +9.9% | +8.5% / **+9.5%** |
| **Bear** D_t / V_t | 0 / 397.9 | 5.18 / 218.2 | 5.79 / 233.9 | 6.40 / **250.9** |
| Bear r_t / IRR to year-end | +0.4% | −43.9% / −39.9% | +9.9% / −20.5% | +10.0% / **−12.0%** |
| **Bull** D_t / V_t | 0 / 397.9 | 5.41 / 477.2 | 7.32 / 585.1 | 9.15 / **698.9** |
| Bull r_t / IRR to year-end | +0.4% | +21.3% / +18.9% | +24.2% / +21.4% | +21.0% / **+21.3%** |

- No year pays k in Base: at 17.6× Base 2027 core earnings the re-rating to 18 is small, so the
  return is the earnings path plus cash. In NOK the Bear 2027 is **−37.1%** (USD/NOK +12%).

### Version 1.1 (5 Nov 2026, $352.03)

**Base, Bear and Bull** (USD bn unless per ADS; capex, D&A, credits and working capital as version
1; revenue on the unchanged H3 index):

| | Base 2027 | 2028 | 2029 | Bear 2027 | 2028 | 2029 | Bull 2027 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|---|
| Revenue | 220 | 247 | 266 | 194 | 174 | 183 | 232 | 275 | 308 |
| Net income (= maintenance FCF) | 115.5 | 125.2 | 133.7 | 92.4 | 76.6 | 81.4 | 121.5 | 139.8 | 155.6 |
| Implied net margin | 52.5% | 50.7% | 50.3% | 47.6% | 44.0% | 44.5% | 52.4% | 50.8% | 50.5% |
| EBITDA (version 1 + Δ net income ÷ 0.83) | 168 | 185 | 201 | 141 | 126 | 134 | 176 | 203 | 232 |
| EPS per ADS | 22.26 | 24.14 | 25.78 | 17.81 | 14.76 | 15.70 | 23.43 | 26.95 | 30.00 |
| FCF after growth / per ADS | 73.1 / 14.09 | 85.5 / 16.49 | 99.7 / 19.23 | 57.6 / 11.10 | 61.5 / 11.85 | 73.6 / 14.18 | 71.9 / 13.86 | 86.5 / 16.68 | 104.3 / 20.10 |
| D_t paid / per ADS | 25.1 / 4.84 | 31.4 / 6.06 | 37.7 / 7.27 | 23.6 / 4.54 | 26.7 / 5.15 | 29.8 / 5.75 | 26.7 / 5.15 | 36.1 / 6.96 | 45.5 / 8.78 |
| Net cash (year-end; 97.9 / 18.88 at end-2026) / per ADS | 145.9 / 28.13 | 200.0 / 38.56 | 262.1 / 50.53 | 131.9 / 25.44 | 166.7 / 32.15 | 210.4 / 40.57 | 143.1 / 27.59 | 193.5 / 37.31 | 252.2 / 48.63 |

**Year 1 (2027) by quarter, 1.1** (consensus scaled to $23.43): consensus 5.26 / 5.63 / 6.05 / 6.49;
Base (same haircuts) 5.21 / 5.40 / 5.69 / 5.97 = $22.27; dividends paid NT$7 / 8 / 8 / 9 = $1.06 /
1.21 / 1.21 / 1.36 per ADS at 33.027.

**Year-end path, 1.1** (USD per ADS; r_t from the end-2026 mark $353.6 = price flat + stub cash):

| | End-2026 | 2027 | 2028 | 2029 (exit) |
|---|---|---|---|---|
| **Base** D_t / V_t | 0 / 353.6 | 4.84 / 405.5 | 6.06 / 456.3 | 7.27 / **506.1** |
| Base r_t / IRR to year-end | +0.4% (stub) | +16.1% / +14.3% | +14.0% / +14.2% | +12.5% / **+13.7%** |
| **Bear** D_t / V_t | 0 / 353.6 | 4.54 / 218.7 | 5.15 / 235.1 | 5.75 / **252.7** |
| Bear r_t / IRR to year-end | +0.4% | −36.8% / −32.8% | +9.8% / −15.8% | +9.9% / **−8.5%** |
| **Bull** D_t / V_t | 0 / 353.6 | 5.15 / 477.3 | 6.96 / 585.6 | 8.78 / **699.7** |
| Bull r_t / IRR to year-end | +0.4% | +36.5% / +31.6% | +24.1% / +28.2% | +21.0% / **+25.9%** |

- Base 2027 (+16.1%) carries a third of the re-rating from core P/E 15.6 to 18 (the glide); it is a
  path diagnostic, not an extra source of return. In NOK the Bear 2027 is **−29.2%** (USD/NOK +12%).

### Version 1 (17 Oct 2026, $412.61)

**Year 1 (2027) by quarter** (EPS per ADS; CQ1 consensus $5.19 (Yahoo, 10); CQ2–4 split at ~+7%
q/q to the CY27 total `[A]`):

| | CQ1-27 | CQ2-27 | CQ3-27 | CQ4-27 | CY27 |
|---|---|---|---|---|---|
| Consensus | 5.19 | 5.55 | 5.97 | 6.40 | 23.11 |
| **Base** (0.99 / 0.96 / 0.94 / 0.92: committed H1, digestion from H2) | 5.14 | 5.33 | 5.61 | 5.88 | **21.96** (path 21.95) |
| Bear (0.97 / 0.82 / 0.74 / 0.70: recession H1-27, then the financing break) | 5.04 | 4.55 | 4.41 | 4.48 | 18.48 |
| Bull (at consensus) | 5.19 | 5.55 | 5.97 | 6.40 | 23.11 |
| Dividend paid, Base (NT$ / $ per ADS gross) | 7.0 / 1.08 (Jan) | 8.0 / 1.23 (Apr) | 8.0 / 1.23 (Jul) | 9.0 / 1.39 (Oct) | 32.0 / 4.93 |

- Base 2028 ($23.80) is 1% above the Base CQ4-27 run-rate ($23.52): the plateau.

**Base** (USD bn unless per ADS):

| | Stub | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Revenue | 44.0 | 220 | 247 | 266 |
| Net income | 22.1 | 113.9 | 123.4 | 131.8 |
| of which after-tax net interest | | 4.1 | 5.7 | 7.5 |
| EBITDA (operating income + D&A) | 31.4 | 166 | 183 | 199 |
| Maintenance FCF (= net income; maintenance capex = D&A) / per ADS | 22.1 / 4.26 | 113.9 / 21.95 | 123.4 / 23.80 | 131.8 / 25.42 |
| Capex / D&A | 17.4 / 6.1 | 76 / 34 | 82 / 41 | 85 / 49 |
| Growth capex (capex − D&A) / per ADS | 11.3 / 2.19 | 42 / 8.10 | 41 / 7.91 | 36 / 6.94 |
| Working capital increase | in OCF | 4.4 | 2.6 | 1.9 |
| US investment tax credits | 0.5 | 4 | 4 | 4 |
| Debt amortisation | — | — | — | — |
| FCF after growth / per ADS | 11.0 / 2.11 | 71.5 / 13.78 | 83.8 / 16.16 | 97.9 / 18.87 |
| D_t paid / per ADS | 0 | 25.6 / 4.93 | 32.0 / 6.17 | 38.4 / 7.40 |
| Net cash (year-end) / per ADS | 99.7 / 19.23 | 145.6 / 28.07 | 197.4 / 38.06 | 256.9 / 49.53 |

**Bear and Bull** (lines that differ from Base; stub and starting balances as Base):

| | Bear 2027 | 2028 | 2029 | Bull 2027 | 2028 | 2029 |
|---|---|---|---|---|---|---|
| Revenue | 194 | 174 | 183 | 232 | 275 | 308 |
| Net income | 95.9 | 89.9 | 101.9 | 119.8 | 137.8 | 153.4 |
| Implied net margin | 49.5% | 51.6% | 55.6% | 51.6% | 50.2% | 49.8% |
| EBITDA | 145 | 142 | 159 | 174 | 201 | 229 |
| Capex / D&A | 70 / 34 | 60 / 40 | 55 / 45 | 82 / 34 | 95 / 42 | 105 / 53 |
| Working capital increase | 1.8 | −1.9 | 0.9 | 5.6 | 4.2 | 3.3 |
| US investment tax credits | 3 | 3 | 3 | 4 | 4 | 4 |
| FCF after growth / per ADS | 61.1 / 11.78 | 74.8 / 14.43 | 94.0 / 18.12 | 70.2 / 13.54 | 84.6 / 16.31 | 102.1 / 19.68 |
| D_t per ADS | 4.63 | 5.24 | 5.86 | 5.24 | 7.09 | 8.94 |
| Net cash $bn / per ADS | 136.8 / 26.39 | 184.5 / 35.57 | 248.1 / 47.83 | 142.7 / 27.52 | 190.6 / 36.74 | 246.2 / 47.48 |

- The Bear's free cash flow is close to the Base's because capex falls with demand: the cost of the
  Bear shows up in value (P/E and earnings), not in cash.

**Year-end path** (USD per ADS; r_t from the end-2026 mark $414.7):

| | End-2026 | 2027 | 2028 | 2029 (exit) |
|---|---|---|---|---|
| **Base** D_t / V_t | 0 / 414.7 | 4.93 / 447.1 | 6.17 / 474.9 | 7.40 / **499.0** |
| Base r_t / IRR to year-end | +0.5% (stub) | +9.0% / +7.9% | +7.6% / +7.8% | +6.6% / **+7.4%** |
| **Bear** D_t / V_t | 0 / 414.7 | 4.63 / 254.6 | 5.24 / 291.2 | 5.86 / **320.4** |
| Bear r_t / IRR to year-end | +0.5% | −37.5% / −32.2% | +16.4% / −13.5% | +12.0% / **−6.3%** |
| **Bull** D_t / V_t | 0 / 414.7 | 5.24 / 523.8 | 7.09 / 606.7 | 8.94 / **690.0** |
| Bull r_t / IRR to year-end | +0.5% | +27.6% / +23.0% | +17.2% / +20.4% | +15.2% / **+18.8%** |

- The Base return is even (7–9% a year): no re-rating to wait for, and no year that pays k. In NOK
  the Bear 2027 is −30.0% (USD/NOK +12%).

## V_T bridge (Base, per ADS) and exit consistency

**1.2 (10 Nov, $396.48):**

| Step | Per ADS |
|---|---|
| Price today | **396.48** = core 378.87 + net cash 17.61 |
| Core at today's core P/E (17.64× Base 2027 core EPS $21.48) | 378.87 |
| + core EPS 2027 → 2030 ($21.48 → $25.31, +5.6% a year) at today's multiple | +67.6 → 446.5 |
| + multiple to the exit P/E 18 (from 17.64) | +9.1 → **455.6** core |
| + net cash at exit (dividends paid, the rest retained) | +48.86 |
| **V_T** | **504.4** |
| Distributions over the horizon (ΣD) | 20.0 |

- **Reading:** of the $108 gain from P to V_T, **$68 is earnings growth, $9 the re-rating** and
  $31 retained cash. The Base again rests on the earnings path, as in version 1.
- **Exit consistency, 1.2:** unchanged from 1.1 (EPS gaps −5.2% / −5.6% / −8.6%; no tail).
- **Exit cross-check, 1.2** (World references now from Equity BBB **6 Nov**): exit P/E 14.0 / **18.0**
  / 21.0 on core EPS against World 15.0 / **17.0** / 18.5; book equity at exit ~76 / **~97** / ~104
  per ADS (the higher dividends take ~$1–2 off book), exit P/B ~3.3 / **~5.2** / ~6.7 against World
  2.47 / **3.17** / 3.74; buyer's implied return ~8.3% / **~9.1%** / ~10.5% against World's mid-cycle
  7.1% / **8.2%** / 8.7%. The reading of 1.1 holds: the buyer at exit earns more than World's
  mid-cycle return in every scenario; the high P/B rests on an exit ROE of ~27%.

**1.1 (5 Nov, $352.03):**

| Step | Per ADS |
|---|---|
| Price today | **352.03** = core 334.68 + net cash 17.35 |
| Core at today's core P/E (15.58× Base 2027 core EPS $21.48) | 334.68 |
| + core EPS 2027 → 2030 ($21.48 → $25.31, +5.6% a year) at today's multiple | +59.7 → 394.3 |
| + multiple to the exit P/E 18 (from 15.58) | +61.2 → **455.6** core |
| + net cash at exit (dividends paid, the rest retained) | +50.53 |
| **V_T** | **506.1** |
| Distributions over the horizon (ΣD) | 18.2 |

- **Reading:** of the $154 gain from P to V_T, **$60 is earnings growth, $61 is the re-rating** back
  to the layer's exit P/E and $33 is retained cash. In version 1 the multiple took $17 away. The
  Base now rests half on the exit multiple, as NVIDIA's does: **at today's multiple Base is 9.3%**.

**Exit consistency, 1.1** (earnings basis = EPS): Base 2029 $25.78 vs 2030 $27.18 (gap −5.2%); Bear
$15.70 vs $16.64 (−5.6%); Bull $30.00 vs $32.81 (−8.6%). None above 10%: no reversion tail.

**Exit cross-check against the equity market (new in 1.1; World references from Equity BBB 17/18
Oct, since TSMC is a non-Oslo name):**

| | Bear | **Base** | Bull |
|---|---|---|---|
| Exit P/E on 2030 core EPS (on reported EPS incl. interest) | 14.0 (15.2) | **18.0 (18.6)** | 21.0 (21.3) |
| World exit P/E (Equity BBB) | 15.0 | **17.0** | 18.5 |
| Book equity per ADS at exit `[A]` (≈ $45.2 at end-2026 + EPS − D_t) | ~78 | **~99** | ~105 |
| Exit P/B | ~3.2 | **~5.1** | ~6.7 |
| World exit P/B | 2.46 | **3.14** | 3.69 |
| Buyer's implied return at exit `[A]` (cash yield c ÷ P/E with c = 0.74, the AI BBB's TSMC 2029 cash conversion, + long-run growth 3 / 5 / 7%) | ~8.3% | **~9.1%** | ~10.5% |
| World mid-cycle return | 7.1% | **8.2%** | 8.7% |

- Book now: Yahoo 2330.TW book value NT$271.60 per share (latest quarter) = $41.12 per ADS at 33.027,
  plus Q4 EPS, less the 3Q26 dividend to be declared in November `[A]`.
- **Reading:** the buyer at exit earns more than World's mid-cycle return in every scenario, so no
  re-discounting sensitivity is needed. The P/B is high (5.1 against 3.14) because the exit ROE is
  ~27% (Base 2030 EPS ÷ exit book), against ~18% for World `[A]`: a stated reason. The Base exit P/E
  is one turn above World's on earnings growing ~5% a year at exit, and at the top of TSMC's own
  2021–25 range (14.4–18.5 on realised next-year EPS): it is not conservative (see the exit P/E −2
  sensitivity).

**Version 1 (17 Oct, $412.61):**

| Step | Per ADS |
|---|---|
| Price today | **412.61** = core 395.47 + net cash 17.14 |
| Core at today's core P/E (18.68× Base 2027 core EPS $21.17) | 395.47 |
| + core EPS 2027 → 2030 ($21.17 → $24.97, +5.6% a year) at today's multiple | +71.0 → 466.5 |
| + multiple to the exit P/E 18 (from 18.68) | −17.1 → **449.5** core |
| + net cash at exit (dividends paid, the rest retained) | +49.53 |
| **V_T** | **499.0** |
| Distributions over the horizon (ΣD) | 18.5 |

- **Reading:** of the $86 gain from P to V_T, **$71 is earnings growth**, $32 is retained cash and
  −$17 is a slightly lower multiple. Against NVIDIA ($43 of $72 from the multiple), TSMC's Base
  rests on its earnings path, which is why the result moves one-for-one with 2030 EPS.

**Exit consistency** (Step 3; earnings basis = EPS):

| Row | Scenario | 2029 EPS | 2030 normalised EPS | Gap | Treatment | Tail per ADS |
|---|---|---|---|---|---|---|
| TSMC EPS | Bear | 19.64 | 21.26 | −7.6% | Not material | 0 |
| | **Base** | 25.42 | 26.80 | **−5.2%** | Not material | 0 |
| | Bull | 29.58 | 32.35 | −8.6% | Not material | 0 |

- No row is above the 10% threshold, so there is no reversion tail and no other treatment to show.

## Growth capex test (Step 4)

- **Amount (Base, 2027–29):** capex $243bn, of which growth (capex − D&A) **$119bn ($22.9 per
  ADS)**, on top of ~$36bn in 2026 and $11bn in the stub. Funded from cash flow; net cash still
  rises by $157bn.
- **ROIC_g, evidence:**
  1. **Average return:** ROE 45.5% in Q3 (CFO) `[F]`; net margin 51%; free cash flow after all
     capex NT$1.48tn in the four quarters to Q3 (4Q25 368.6 + 1Q26 348.2 + 2Q26 287.4 + 3Q26
     476.6) `[F]`.
  2. **Incremental, on the AI BBB paths** `[A]`: Base core net income rises from ~$91bn (2026) to
     $129.5bn (2030) on ~$155bn of growth capex in 2026–29: **~25% after tax**. Bull: +$68bn on
     ~$189bn (~36%). Bear: +$10bn on ~$102bn (**~10%, below k**).
  3. **Overseas fabs** earn less (dilution 2% → 3–4 pp of group gross margin) `[F]`, partly offset
     by US investment tax credits (NT$198.7bn received in Q3) `[F]` and location-based pricing.
- **Verdict:** growth capex is accretive in Base and Bull (ROIC_g 25–36% vs k 12%) and its value is
  already inside the EPS path. In the Bear, the capacity built for 2027–28 earns ~10%: that is the
  overbuild the Citi analyst asked about on the call; TSMC's answer is its demand checks (customers,
  their customers, data centers, power) `[F]`, not a number.
- **Per share:** no new shares.
- **1.1:** with the reconciled Bear (.71 of CY27 consensus in 2030), Bear core net income in 2030 is
  ~$79bn, **below 2026's ~$91bn** after ~$102bn of growth capex: ROIC_g is **negative** in the Bear
  (version 1: ~10%). Base (~25%) and Bull (~36%) are unchanged at the path's precision.
- **1.2:** unchanged. The November appropriations ($40.9bn, after $29.4bn in August) fit the Base
  2027 capex of $76bn; they are approvals, not a 2027 capex number (that comes with the January
  guide).

## Results

**1.2 (10 Nov 2026; P $396.48 per ADS)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (USD, dated, to the exit value) | −12.0% | **9.5%** | 21.3% |
| IRR_T in NOK on the Equity BBB NOK path | −9.5% | **9.5%** | 20.1% |
| d / g / c | 1.4 / −13.6 / +0.2 | **1.6 / 8.0 / −0.1** | 1.8 / 19.8 / −0.2 |
| g: core P/E on 2030 core EPS today → exit (a year) / net cash (no NAV) | 25.0 → 14 (−16.9%) / $17.6 → $38.8 | **15.0 → 18 (+6.0%) / $17.6 → $48.9** | 12.2 → 21 (+18.9%) / $17.6 → $47.8 |
| Structural IRR / cyclical (pp; Δd, Δg) | −11.9% / −0.1 (0.0, −0.1) | **9.7% / −0.2 (0.0, −0.2)** | 21.6% / −0.2 (0.0, −0.2) |
| ΣD_t / V_T | 17.4 / 250.9 | **20.0 / 504.4** | 21.9 / 698.9 |
| P_k (hurdle price, USD per ADS) / margin of safety | 190.2 / −52.0% | **369.8 / −6.7%** | 507.5 / +28.0% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | 23.8× vs n/m | **14.6× vs 6.6×** | 12.1× vs 14.8× |
| Capital preserved? ΣD_t + V_T vs P | **No, −32.3%** | Yes, +32.3% | Yes, +81.8% |

- Structural run and FCF_normalised as version 1 (below); the structural offsets are carried from
  1.1 (the paths did not move). FCF_normalised = Base 2030 EPS $27.18; Rule 3 fails (14.6× vs
  6.6×); the decision is on P_k.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** 8.5%. It never replaces the Base.
- **Share of Bull already priced:** (396.48 − 369.8) / (507.5 − 369.8) = **19%**.
- **Bear balance sheet:** net cash $98.6bn (end-2026) → $201bn (2029); FCF after growth $58–74bn a
  year. No survival question. The loss is in value: −44% in 2027, −32.3% of capital at exit.
- **Market check (not an input):** Yahoo average analyst rating 1.3 (Strong Buy), 11 Nov. Broker
  targets not re-read.

**Sensitivities, 1.2** (USD IRR and P_k at $396.48; each sensitivity's V_T taken from the 1.1 run
and moved by the 1.2 dividend change):

| Change | Bear | **Base** | Bull |
|---|---|---|---|
| Model | −12.0% (190) | **9.5% (370)** | 21.3% (508) |
| Exit P/E −2 / +2 | −15.4% / −8.8% | **6.0% / 12.8%** (334 / 405) | 17.9% / 24.6% |
| Exit P/E 16.7 (TSM 2021–25 mean on realised next-year EPS) | | **7.2% (347)** | |
| Exit P/E at today's core 17.64 (no re-rating) | | **8.9% (363)** | |
| 2030 normalised EPS ×0.9 / ×1.1 | −14.7% / −9.5% | **6.1% / 12.7%** (336 / 404) | 17.5% / 25.0% |
| **Management path** (consensus 2027, then ~25% revenue CAGR 2024–29; EPS 1.00 / 1.08 / 1.165 / 1.26) | | **12.3% (400)** | |
| **Gross margin toward the 56% floor** (EPS ×0.94 / 0.89 / 0.83 in 2028–30) | | **3.5% (311)** | |
| **ADR premium at exit:** 2-year mean 19.5% / 2-year low 6.9% / 3.8% / parity | −10.2% / −12.8% / −13.4% / −14.3% | **12.0% / 8.4% / 7.5% / 6.4%** (396 / 359 / 350 / 339) | 24.1% / 20.1% / 19.2% / 17.9% |
| Version 1 H3 Bear path (.80 / .75 / .85 / .92) | −4.9% | | |
| P_k at k = 13% / 14% (a Taiwan premium on k) | | 360 / 350 (−9.2% / −11.6%) | |
| Bull EPS at the Base exit P/E 18 / Base EPS at the Bull exit P/E 21 | | 16.1% / 14.3% | |

- **What flips the verdict back to clear:** the price below $362.6 (−8.5%), or a path above the
  Base: management's own path (12.3%, P_k $400, +0.9%: marginal), an exit P/E of 20, 2030 EPS +10%,
  or the ADR premium back at its 2-year mean (each ~12–13%, P_k $396–405: marginal to just
  clearing). None of these is what the AI BBB expects.
- **What makes it worse:** an exit P/E of 16 (6.0%), margins toward the 56% floor (3.5%), ADR parity
  (6.4%).

**1.1 (5 Nov 2026; P $352.03 per ADS)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (USD, dated, to the exit value) | −8.5% | **13.7%** | 26.0% |
| IRR_T in NOK on the Equity BBB NOK path | −5.9% | **13.7%** | 24.7% |
| d / g / c | 1.4 / −10.0 / +0.1 | **1.6 / 12.2 / −0.1** | 1.9 / 24.3 / −0.3 |
| g: core P/E on 2030 core EPS today → exit (a year) / net cash (no NAV) | 22.1 → 14 (−13.5%) / $17.4 → $40.6 | **13.2 → 18 (+10.3%) / $17.4 → $50.5** | 10.8 → 21 (+23.5%) / $17.4 → $48.6 |
| Structural IRR / cyclical (pp; Δd, Δg) | −8.4% / −0.1 (0.0, −0.1) | **13.9% / −0.2 (0.0, −0.2)** | 26.2% / −0.3 (0.0, −0.3) |
| ΣD_t / V_T | 15.4 / 252.7 | **18.2 / 506.1** | 20.9 / 699.7 |
| P_k (hurdle price, USD per ADS) / margin of safety | 189.6 / −46.2% | **368.9 / +4.8%** | 506.5 / +43.9% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | 21.2× vs n/m | **13.0× vs 9.5×** | 10.7× vs 18.0× |
| Capital preserved? ΣD_t + V_T vs P | **No, −23.8%** | Yes, +48.9% | Yes, +104.7% |

- Structural run and FCF_normalised as version 1 (below). FCF_normalised = Base 2030 EPS $27.18.
  Rule 3 fails (13.0× vs 9.5×); the decision is on P_k.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** 12.7%. It never replaces the Base.
- **Share of Bull already priced:** (352.03 − 368.9) / (506.5 − 368.9) = **−12%**: the price is below
  the Base hurdle, so none of the Bull is priced.
- **Bear balance sheet:** net cash $97.9bn (end-2026) → $210bn (2029); FCF after growth $58–74bn a
  year. No survival question. The loss is in value: −37% in 2027, −23.8% of capital at exit.
- **Market check (not an input):** Yahoo average analyst rating 1.4 (Strong Buy), 5 Nov. The broker
  targets were not re-read; in version 1 the Zacks average target was $523, now 49% above the price.

**Sensitivities, 1.1** (USD IRR and P_k at $352.03):

| Change | Bear | **Base** | Bull |
|---|---|---|---|
| Model | −8.5% (190) | **13.7% (369)** | 26.0% (507) |
| Exit P/E −2 / +2 | −12.0% / −5.2% | **10.1% / 17.1%** (334 / 404) | 22.4% / 29.3% |
| Exit P/E 16.7 (TSM 2021–25 mean on realised next-year EPS) | | **11.4% (346)** | |
| Exit P/E at today's core 15.58 (no re-rating) | | **9.3% (326)** | |
| 2030 normalised EPS ×0.9 / ×1.1 | −11.2% / −5.9% | **10.2% / 17.0%** (335 / 403) | 22.0% / 29.7% |
| **Management path** (consensus 2027, then ~25% revenue CAGR 2024–29; EPS 1.00 / 1.08 / 1.165 / 1.26) | | **16.6% (399)** | |
| **Gross margin toward the 56% floor** (EPS ×0.94 / 0.89 / 0.83 in 2028–30) | | **7.5% (310)** | |
| CY27 anchor: version 1 $23.11 / Zacks $21.50 (not re-read) | −8.9% (187) / — | 13.2% (364) / 10.7% (339) | 25.4% (500) / — |
| **ADR premium at exit:** 2-year mean 19.5% / 2-year low 6.9% / today's close-on-close 3.8% / parity | −6.6% / −9.3% / −9.9% / −10.8% | **16.2% / 12.6% / 11.7% / 10.6%** (395 / 358 / 349 / 338) | 28.8% / 24.7% / 23.7% / 22.4% |
| Version 1 H3 Bear path (.80 / .75 / .85 / .92) | −1.1% (240) | | |
| P_k at k = 13% / 14% (a Taiwan premium on k) | | 359 / 349 (+2.0% / −0.8%) | |
| Bull EPS at the Base exit P/E 18 / Base EPS at the Bull exit P/E 21 | | 20.5% / 18.7% | |

- Not re-run (each moved the Base by < 0.3 pp in version 1): capex ×1.2, dividends net of the 21%
  Taiwan withholding. The no-interest-strip run added ~2 pp in version 1.
- **What flips the verdict back:** the price above $376.4 (+6.9%); an exit P/E of 16 (10.1%, P_k $334: fails) or the 2021–25
  mean (16.7: 11.4%, P_k $346, −1.7%: marginal); 2030 EPS 10% below Base; margins toward the 56% floor; a
  Taiwan premium of 2 pp on k; or the ADR premium staying near today's close-on-close level.
- **What strengthens it:** management's own path (16.6%); the ADR premium back toward its 2-year mean
  (16.2%); a January 2027 guide of +30% or more with capex ≥ $75bn.

**Version 1 (17 Oct 2026; P $412.61)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T | −6.3% | **7.4%** | 18.8% |
| d / g / c | 1.2 / −7.6 / +0.1 | **1.4 / 6.1 / −0.1** | 1.6 / 17.4 / −0.2 |
| g: core P/E on 2030 core EPS today → exit (a year) / net cash (no NAV) | 20.3 → 14 (−11.0%) / $17.1 → $47.8 | **15.8 → 18 (+4.1%) / $17.1 → $49.5** | 12.9 → 21 (+16.3%) / $17.1 → $47.5 |
| Structural IRR / cyclical (pp; Δd, Δg) | −6.0% / −0.4 (0.0, −0.4) | **7.7% / −0.2 (0.0, −0.2)** | 19.0% / −0.2 (0.0, −0.2) |
| ΣD_t / V_T | 15.7 / 320.4 | **18.5 / 499.0** | 21.3 / 690.0 |
| P_k (hurdle price) / margin of safety | 235.7 / −42.9% | **362.1 / −12.2%** | 497.1 / +20.5% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | 19.4× vs n/m | **15.4× vs 5.2×** | 12.8× vs 13.1× |
| Capital preserved? ΣD_t + V_T vs P | **No, −18.5%** | Yes, +25.4% | Yes, +72.4% |

- **Structural run:**
  - EPS is set at the scenario's own 2030 normalised level from 2027 (revenue at the scenario's
    2029 level); capex, dividends and the exit as in the path.
  - **The Base has no cycle in the window** (−0.2 pp): its earnings rise steadily to the 2030
    level. Bear and Bull are **shifts of the mid-cycle itself** (Bear structural −6.0% against Base
    7.7%), not rate paths around it. For TSMC the question is the level AI silicon earnings settle
    at, and the margin TSMC keeps on it.
- **FCF_normalised (Rule 3):** 2030 normalised EPS with maintenance capex = D&A (the renewal charge)
  and no working-capital growth = **$26.80 per ADS**. P/FCF 15.4× against a ceiling of 5.2× fails;
  the decision is on P_k.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** 7.7%. It never replaces the
  Base.
- **Share of Bull already priced:** (412.61 − 362.1) / (497.1 − 362.1) = **37%**.
- **Bear balance sheet:** net cash $99.7bn (end-2026) → $248bn (2029); FCF after growth $61–94bn a
  year. No survival question. The loss is in value: −38% in 2027, −18.5% of capital at exit.
- **Market check (not an input):**
  - Zacks average broker target **$523** (Zacks own target $508); ABR 1.21 (18 of 19 at Buy or
    Strong Buy). In the last 60 days: Barclays Strong Buy, target $665 (6 Oct); Citi Strong Buy, no
    target (7 Oct). Zacks Rank 1 (Strong Buy) from 17 Oct: estimate momentum, not an IAF input.
    Zacks long-term EPS growth 29%.
  - Brokers price growth well beyond the AI BBB's. **The IAF hurdle ($362) is 31% below the
    average target**; the gap is the digestion after 2027 that the brokers do not price, and an
    exit multiple above TSMC's own five-year range.

**Sensitivities** (USD IRR and P_k):

| Change | Bear | **Base** | Bull |
|---|---|---|---|
| Model | −6.3% (236) | **7.4% (362)** | 18.8% (497) |
| Exit P/E −2 / +2 | −9.9% / −3.0% | **4.0% / 10.6%** (327 / 397) | 15.5% / 21.9% |
| Exit P/E 16.7 (TSM 2021–25 mean on realised next-year EPS) | | **5.3% (340)** | |
| Exit P/E at today's core 18.68 | | 8.6% (374) | |
| 2030 normalised EPS ×0.9 / ×1.1 | −9.1% / −3.7% | **4.2% / 10.5%** (329 / 396) | 15.1% / 22.3% |
| **Management path:** consensus 2027, then ~25% revenue CAGR 2024–29 (EPS 1.00 / 1.08 / 1.165 / 1.26) | | **10.2% (392)** | |
| **Gross margin toward the 56% floor** (EPS ×0.94 / 0.89 / 0.83 in 2028–30) | | **1.7% (304)** | |
| CY27 anchor: Zacks $21.50 / Taipei consensus $22.91 | −8.4% / −6.6% | 5.1% / 7.2% | 16.2% / 18.5% |
| No interest strip (EPS × P/E + cash at face) | −4.1% | 9.6% (385) | 20.7% |
| **ADR premium at exit:** 2-year mean 19.5% / 2-year low 6.9% / parity | −4.1% / −7.3% / −9.1% | **10.0% / 6.3% / 4.2%** | 21.7% / 17.6% / 15.2% |
| **Revenue-consistent Bear** (EPS .76 / .63 / .67 / .71) | **−13.2% (186)** | | |
| Capex ×1.2 | −6.6% | 7.3% | 18.7% |
| Dividends net of 21% Taiwan withholding (memo) | −6.5% | 7.2% | 18.5% |
| P_k at k = 13% / 14% (a Taiwan premium on k) | | 352 / 343 (−14.7% / −17.0%) | 483 / 470 |
| Bull EPS at the Base exit P/E 18 / Base EPS at the Bull exit P/E 21 | | 13.8% / 12.1% | |

- **What flips the verdict:**
  - Up: an exit multiple ≥ 20.9 on Base earnings, or 2030 EPS ≥ $30.84 (close to Bull), or the
    price falling 12% to $362. Management's own path alone does not do it (10.2%).
  - Down (worse): margins reverting toward the long-term floor (1.7%), a lower exit multiple
    (5.3% at the five-year mean), or ADR parity (4.2%).
- **The result is about the 2030 earnings level and the multiple;** capex, dividends and working
  capital move it by less than 0.3 pp. The ADR premium is the one TSMC-specific item that moves it
  by ±3 pp.

## Against World, layer, NVIDIA and HY

**1.2 (10 Nov).** E / R is a reference row, not the gate (cycle-lead rule); TSMC is not held. The
HY book and DNB Teknologi rows of 1.1 came from `docs/portfolio-overview.md`, retired on 9 Nov; they
are dropped here.

| NOK, before fees | Base window return | Bear 2027 | E / R |
|---|---|---|---|
| Nordic HY market reference (`docs/hy-market-bbb.md`, 5 Nov) | 7.2% (6.6% after the 0.6% fee) | −0.4% (−1.0% after fee) | **0.254** |
| MSCI World (Equity BBB **6 Nov**, 5 Nov prices) | 6.6% | −18.3% | 0.080 |
| AI H3 foundry and equipment basket (AI BBB Update 7, 6 Nov prices) | see `docs/ai-market-bbb.md` | — | — |
| **TSMC (this analysis, $396.48)** | **9.5%** | **−37.1%** | **0.106** |

- **E / R** = (Base NOK 9.5% − NIBOR 4.38%) ÷ (Base 2027 +11.1% − Bear 2027 −37.1%) = 5.1 ÷ 48.2.
- **Reading:** TSMC still beats World and the HY market on Base return, but by less, and its Bear
  2027 loss is larger from the higher price: per unit of that stress it pays well under half of
  the HY market (0.106 vs 0.254). No portfolio change follows from this document.

**Trigger prices, 1.2** (USD per ADS; unchanged earnings and paths; P vs the 10 Nov close):

| Trigger | Price | Move | Base IRR there |
|---|---|---|---|
| Clears (margin of safety > +2%) below | **$362.6** | −8.5% | 12.7% |
| Base = k (12%) | **$369.8** | −6.7% | 12.0% |
| Fails (margin < −2%) above | **$377.4** | −4.8% | 11.3% |
| E / R = HY market reference 0.254 | **$335.9** | −15.3% | 15.6% |
| Base = HY market 7.2% (before fees) | $423.2 | +6.7% | 7.2% |
| Bull hurdle / Bear hurdle | $507.5 / $190.2 | +28.0% / −52.0% | — |

**1.1 (5 Nov).** E / R is a reference row here, not the gate (cycle-lead rule, iaf-valuation
2026-11-01.1); TSMC is not held.

| NOK, before fees | Base window return | Bear 2027 | E / R |
|---|---|---|---|
| Nordic HY market reference (`docs/hy-market-bbb.md`, 5 Nov) | 7.2% (6.6% after the 0.6% fee) | −0.4% (−1.0% after fee) | **0.254** |
| HY book (`docs/portfolio-overview.md`; not re-read, predates the 5 Nov HY re-mark) `[C]` | 6.9% | — | 0.291 |
| MSCI World (Equity BBB 17/18 Oct) | 5.2% | −20.6% | 0.024 |
| AI H3 foundry and equipment basket (AI BBB, 5 Nov prices) | 11.7% (margin of safety −0.8%) | — | — |
| NVIDIA (`docs/nvda-analysis.md` 1.1, $204.64 on 30 Oct) | 13.3% | ~−39% | 0.154 |
| DNB Teknologi (fund; `docs/portfolio-overview.md`, 22 Oct) `[C]` | 7.2% (after 1.14% cost) | −30.8% | 0.074 |
| **TSMC (this analysis, $352.03)** | **13.7%** | **−29.2%** | **0.206** |

- **E / R** = (Base NOK 13.7% − NIBOR 4.38%) ÷ (Base 2027 +16.1% − Bear 2027 −29.2%) = 9.3 ÷ 45.3.
  Version 1: 0.079 on the old Bear; 0.062 on the reconciled Bear at $412.61.
- **Reading:** TSMC now beats World, the HY market and the HY book on Base return, but carries a Bear
  2027 loss of −29% in NOK against −0.4% for HY: per unit of that stress it pays less than the HY
  market (0.206 vs 0.254). It is not held directly (in DNB Teknologi, not in MSCI World); **no
  portfolio change follows from this document.**

**Trigger prices, 1.1** (USD per ADS; unchanged earnings and paths; P vs the 5 Nov close):

| Trigger | Price | Move | Base IRR there |
|---|---|---|---|
| Clears (margin of safety > +2%) below | **$361.7** | +2.7% | 12.7% |
| Base = k (12%) | **$368.9** | +4.8% | 12.0% |
| Fails (margin < −2%) above | **$376.4** | +6.9% | 11.3% |
| E / R = HY market reference 0.254 | **$334.9** | −4.9% | 15.6% |
| E / R = HY book 0.291 `[C]` | $323.2 | −8.2% | 16.9% |
| Base = HY market 7.2% (before fees) | $422.5 | +20.0% | 7.2% |
| Base = HY book 6.9% `[C]` | $426.2 | +21.1% | 6.9% |
| Bull hurdle / Bear hurdle | $506.5 / $189.6 | +43.9% / −46.2% | — |

**Version 1 (17 Oct):**

| NOK, before fees | Base window return | Bear 2027 | E / R |
|---|---|---|---|
| Nordic HY market reference | 6.2% (after 0.6% fee) | −2.8% | 0.196 |
| HY book (`docs/portfolio-overview.md`) | 6.9% | — | 0.291 |
| MSCI World (Equity BBB) | 6.1% (6.4% at 14 Oct) | −18.2% | 0.063 |
| AI H3 foundry and equipment basket (AI BBB, 14/15 Oct) | 1.1% | −43.5% | −0.077 |
| NVIDIA (`docs/nvda-analysis.md`) | 13.0% | −28.2% | 0.184 |
| DNB Teknologi (fund, after 1.14% cost) | 5.6% | −29.4% | 0.037 |
| **TSMC (this analysis)** | **7.4%** | **−30.0%** | **0.079** |

- **E / R** = (Base NOK 7.4% − NIBOR 4.38%) ÷ (Base 2027 +9.0% − Bear 2027 −30.0%) = 3.1 ÷ 39.0.
  With the revenue-consistent Bear (2027 −40.4% in NOK) it is 0.062.
- **Head-to-head on the agreed rule:** TSMC barely beats the HY book on Base return (7.4% vs 6.9%)
  and loses on E / R (0.079 vs 0.291) and on Bear 2027 (−30% vs HY's −3%). It also loses to NVIDIA
  on both. It is not held directly (1.97% of DNB Teknologi; not in MSCI World), so **no portfolio
  change follows.** It becomes a candidate on the rule only at a trigger.
- **Triggers** (at unchanged earnings and paths; P vs the 16 Oct close):

| Trigger | Price | Move | Base IRR there |
|---|---|---|---|
| Base = HY book 6.9% (above this, HY wins on return alone) | $419.3 | +1.6% | 6.9% |
| Base = k (12%) | **$362.1** | −12.2% | 12.0% |
| E / R = HY market reference 0.196 | **$347.9** | −15.7% | 13.4% |
| E / R = HY book 0.291 | **$286.3** | −30.6% | 20.7% |

## Verdict and caveat

**1.2 (11 Nov 2026, $396.48 per ADS; the verdict is in the Summary):**
- **Band applied:** Base margin of safety P_k / P − 1 = 369.8 / 396.48 − 1 = **−6.7%**, below −2%:
  the fail band. Clears below $362.6, marginal to $377.4.
- **What would flip it:** the price (−8.5% to clear); or a Base above the AI BBB's (management's
  path, an exit P/E of 20, 2030 EPS +10%, the ADR premium at its 2-year mean: each only reaches
  marginal or just clears). The 10 Nov prints (October +59.7% y/y, NT$9.0, $40.9bn) are on the
  Bull side but move no path; the January guide (+30% or more with capex ≥ $75bn) is the print that
  could.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation, a price target or personal
  advice. The EPS paths and the scenarios are the AI BBB's; the exit multiples, the interest strip,
  capex, dividends and the ADR premium are own assumptions.

**1.1 (5 Nov 2026, $352.03 per ADS):**
- **Verdict: clears, narrowly.** Base margin of safety **+4.8%** (Base IRR 13.7% vs k 12%; P_k
  $368.9). **The verdict flips from fail (−12.2%) on price alone**; the inputs since 17 Oct moved
  Base by +0.5 pp and made the Bear worse.
- It does **not survive Bear** in value: −8.5% a year, capital −23.8% at exit, −37% in 2027 (−29% in
  NOK). The balance sheet survives every scenario with net cash rising.
- **Why it clears now:** the 5 Nov sell-off took the ADS to 15.0× CY27 consensus and a core 13.2× Base
  2030 earnings. On the AI BBB's unchanged paths, the return to the layer's exit P/E of 18 is ~14%.
  Half of the gain is that re-rating; at today's multiple the Base is 9.3%.
- **How firm:** thin. Marginal from $361.7, fails above $376.4; an exit P/E of 16, margins toward the
  56% floor, a 2 pp Taiwan premium on k or the ADR premium staying near 4% each takes it back to
  marginal or fail. The price implies 0.95× Base 2028–30 earnings.
- **What would confirm it:** October revenue (~10 Nov) still above +45% y/y; NVIDIA's Q3 (17 Nov)
  without a supply-commitment cut; a January guide of +30% or more with capex ≥ $75bn.
- **What would break it:** the AI BBB moving K1 2028 (state siting or financing), margins toward
  the floor, a digestion that starts in 2027, or a Taiwan event (not modelled).
- **E / R 0.206** against the HY reference 0.254: a reference row. TSMC pays more than HY in Base but
  less per unit of Bear stress.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation, a price target or personal
  advice. The EPS paths and the scenarios are the AI BBB's; the exit multiples, the interest strip,
  capex, dividends and the ADR premium are own assumptions.

**Version 1 (17 Oct 2026, $412.61):**
- **Verdict: fails.** Base margin of safety **−12.2%** (Base IRR 7.4% vs k 12%). It does **not
  survive Bear** in value: capital −18.5% at exit, −38% in 2027 (−13% a year on the
  revenue-consistent Bear). The balance sheet survives every scenario with net cash rising.
- **Why:** TSMC is the highest-quality business in the AI hardware chain (record margins, net
  cash, every AI chip designer as a customer, demand above supply), and the price says so. At
  17.85× 2027 consensus, the AI baseline's path pays about 7%: management's long-term growth rate
  with digestion after 2027, at an exit multiple equal to today's.
- **What would make it clear k:**
  - evidence that 2028–29 growth runs well above the H3 Base (a 2027 revenue guide in January of
    +30% or more with capex ≥ $75bn and gross margin held near 65%; NVIDIA and the hyperscalers
    guiding 2028 up);
  - or the price falling to ~$362 (Base = k) or ~$348 (E / R = HY reference).
- **What would make it worse:** margins reverting toward the 56% floor (overseas fabs, N2/A14
  ramps, pricing), a digestion that starts in 2027 (consumer weakness plus a financing break), the
  ADR premium collapsing, or a Taiwan event (not modelled).
- **On the HY rule it does not qualify:** E / R 0.079 against 0.196 (HY reference) and 0.291 (HY
  book). On the same AI baseline NVIDIA is the better candidate (13.0%, E / R 0.184).
- **Caveat:**
  - This is a margin-of-safety screen, not an intrinsic valuation, a price target or personal
    advice.
  - The EPS path and the scenarios are the AI BBB's.
  - The exit multiples, the interest strip, capex, dividends and the ADR premium are own
    assumptions; the sensitivities show their weight.

## Risks and signposts

| Signpost | Bear / Bull threshold | Now | Source |
|---|---|---|---|
| TSM price (triggers, 1.2) | > $377.4 fails; $362.6–377.4 marginal / < $362.6 clears; ≤ $335.9 E / R = 0.254 | **$396.48 (10 Nov close)**: fails (5 Nov $352.03 cleared) | Yahoo |
| Monthly revenue (~10th of each month; November on ~10 Dec, date not confirmed) | y/y growth < +25% for two months in H1-27 / > +45% into 2027 | **October NT$586.89bn, +59.7% y/y** (+14.7% m/m; Jan–Oct +43.3%), the second month above +45% (September +54.6%); Q4 tracks the upper half of the guide (Near term). **11 Nov: signpost Bull-side level hit; kept** (the threshold reads into 2027; the guide already implied +58%) | TSMC 6-K, 10 Nov |
| US state siting policy (new 5 Nov, from the AI BBB) | Texas pause extended into 2027 or a statutory moratorium; a hyperscaler moves or cancels ≥ 1 GW / pause lifted with cost rules | ERCOT/PUCT audit 10 Dec; governors 11–19 Jan; Texas Legislature from 12 Jan | AI BBB |
| Q4 report (mid-Jan 2027): 2027 revenue and capex guide | 2027 growth < +20% in USD or capex flat / ≥ +30% with capex ≥ $75bn | 2026 ~+44%; capex $60–64bn | TSMC |
| Gross margin guide | < 60% (overseas, N2, pricing) / ≥ 66% held through 2027 | Q4 guide 65–67% | TSMC |
| Board: quarterly dividend and appropriations (next: February 2027, 4Q26 dividend; date not verified) | dividend held / raised by ≥ NT$1.0; appropriations cut / raised | **10 Nov: 3Q26 NT$9.0 (from 7.0) and $40.93bn (August $29.4bn): Bull side on both**; dividend replaces the model's NT$8.0, appropriations not modelled | TSMC 6-K, 10 Nov |
| Hyperscaler 2027 capex (27–30 Oct; next figures late Jan–early Feb) | flat or down / 2027 consensus > USD 1.3tn | Q3 reports guided 2027 up; K1 2027 kept at USD 1,120bn (AI BBB, 1 and 5 Nov) | AI BBB |
| NVIDIA Q3 FY27 (17 Nov) and supply commitments | Q4 guide below Q3, commitments cut / Q4 guide > ~$124bn, commitments raised | Q3 guide $108bn; commitments $279bn (unchanged, 2 Nov) | `docs/nvda-analysis.md` |
| Lab financing and AI credit (Anthropic IPO, OpenAI raises, neoclouds) | IPO pulled or below marks; a lab misses commitments / above marks | Platform equity funding crossed (29 Oct); capex ÷ OCF ~116% touched (1 Nov); CoreWeave new 2026 low on 5 Nov, neocloud first leg touched; Anthropic IPO pricing ~18 Nov (range $70–78 `[E]`); TSMC's board approved up to $0.5bn of Anthropic at the IPO price and $0.5bn of OpenAI preferred (10 Nov `[F]`; immaterial to TSMC) | AI BBB; TSMC 6-K |
| Consumer demand (memory-cost squeeze on phones and PCs) | smartphone revenue down y/y / N2 smartphone ramp on plan | Smartphone +10% q/q in Q3; management "prudent" for 2027 | TSMC |
| ADR premium | < 5% / > 20% | 13.8% close-on-close on 10 Nov (Taipei before the releases); the 5 Nov 3.8% was a timing gap, not a crossing | Yahoo |
| NT$/US$ | < 30 (NT$ +7%: gross margin about −3 pp) / > 33 | 32.79 (10 Nov; 33.11 on 6 Nov): back below the Bull-side level | Yahoo, TSMC rule of thumb `[E]` |
| Foundry competition (Intel 14A and EMIB-T, an IDM customer insourcing) | a large AI customer moves leading-edge wafers or packaging away / A14 larger than N2 confirmed | CEO: A14 interest above N2 at the same stage | Call |
| Taiwan Strait, export controls, US tariffs on chips | escalation | Not modelled (AI BBB tail) | — |

## For other modules

**1.2 (11 Nov):**
- **`ai-market-bbb`** (no path set here; nothing it reads as a row moved):
  1. Company check: TSM at **$396.48** (10 Nov close); Base **9.5%**, P_k **$369.8**, margin
     **−6.7%** (fails; 1.1 +4.8% at $352.03). Bear −12.0%, Bull 21.3%. Price implied: 1.07× Base
     2028–30 for k (0.76× for 0%).
  2. Signposts for H3 and K1 (TSMC 6-Ks, 10 Nov `[F]`): October revenue NT$586.89bn, +59.7% y/y
     (second month above +45%; Q4 on the upper half of the guide, not above it); 3Q26 dividend
     NT$9.0; **capital appropriations $40.93bn** (August $29.4bn); TSMC to buy up to $0.5bn of
     Anthropic at the IPO price and $0.5bn of OpenAI preferred (confirms the press report of the
     Class N placement buyer from TSMC's side).
  3. The base-effect flag (Q4-26 run-rate ~121 on the H3 index) stays open; October supports it.
- **`docs/dnb-teknologi-analysis.md`** (TSMC ADS block): Base 13.7% → 9.5% at $396.48 (fails);
  read at its next re-run, at its own price date. A price re-mark: no path it reads moved.
- **`docs/global-index-funds-analysis.md`, `equity-market-bbb`, `kospi`:** no input.

**1.1 (5 Nov):**
- **`ai-market-bbb`** (no path set here; nothing it reads as a row moved):
  1. Company check: TSM at **$352.03** (5 Nov close), CY27 consensus **$23.43** (14); on its own build
     Base **13.7%**, P_k **$368.9**, margin **+4.8%** (clears; version 1 7.4% / −12.2%). Bear −8.5%,
     Bull 26.0%.
  2. The H3 Bear adoption (Update 2) is confirmed from the TSMC side; the base-effect flag (Q4-26
     run-rate ~121) stays open.
  3. Price implied for the foundry leader: 0.95× Base 2028–30 for k (0.66× for 0%), beside NVIDIA's
     0.96× at $204.64.
  4. ADR premium close-on-close 3.8% on 5 Nov (non-simultaneous; 14.9% on 4 Nov); NT$/US$ 33.03.
- **`docs/dnb-teknologi-analysis.md`** (TSMC ADS block): Base 7.4% → 13.7% at $352.03; read at its next
  re-run, at its own price date.
- **`docs/global-index-funds-analysis.md`, `equity-market-bbb`:** no input.
- **`docs/portfolio-overview.md`:** not held directly; no change.

**Version 1 (17 Oct):**
- **`ai-market-bbb`** (input; no path set here):
  1. **H3 Bear: EPS path and revenue index are inconsistent** (as found for H1 and H2). On the
     layer's Bear revenue TSMC's net margin must rise from 49.5% to 55.6% while revenue falls 10% in
     2028 and depreciation rises. A revenue-consistent TSMC Bear is ~.76 / .63 / .67 / .71
     (−13.2% instead of −6.3%). Suggest reconciling the H3 Bear EPS path to its revenue index (or
     the index to the path).
  2. **H3 revenue index base effect** (as fixed for H2 on 16 Oct): 2026 = 100 is the calendar-year
     average, but TSMC exits 2026 at ~121 (Q4 guide annualised). Base 2027 at 125 means TSMC revenue
     only ~3% above its Q4-26 run-rate for the whole of 2027, against N2 capacity doubling and two
     new N3 fabs. Suggest adding a Q4 run-rate memo to H3 and testing the 2027 Base step against it.
  3. **The open item "TSMC Q4 guide and 2027 capex comment (call 15 Oct, not yet read)" is now
     read** (management report and transcript): Q4 guide $52.3–54.3bn (+14% q/q), gross margin
     65–67%; 2026 ~+44% in USD; 2026 capex $60–64bn; 2026–28 capex well above 2023–25 (no 2027
     number); overseas dilution 2% → 3–4 pp; AI accelerator CAGR "probably higher" than mid-to-high
     50s; N2 capacity more than doubles in 2027; A14 volume 2028; demand above supply; prudent on
     consumer for 2027; August appropriations $29.4bn. All support H3 Base 2027; nothing moves 2028–29.
  4. **TSM prints for the basket:** price $430.00 → **$412.61** (16 Oct); CY26 / CY27 consensus
     $17.05 / $22.32 → **$17.31 / $23.11** (12 / 14). TSM's P/E falls from 19.3 to 17.85; with ASML,
     AMAT and LRCX at 16 Oct prices the H3 basket P/E is ~20.1 (from 21.5) and its Base return
     roughly 3% `[A]` (not re-run).
  5. **New signpost suggestion:** TSMC monthly revenue (the only monthly hard print in the chain)
     and the ADR premium as a mood gauge for Asian AI hardware.
- **`docs/dnb-teknologi-analysis.md`** (TSMC ADS 1.97% of NAV, valued on the H3 layer): TSMC can
  enter as a company block at the next re-run (Base 7.4% against ~1% on the layer method). Rough
  effect ≈ +0.1 pp on the fund's Base `[A]`.
- **`docs/global-index-funds-analysis.md`:** no input (TSMC is not in MSCI World).
- **`equity-market-bbb`:** no input.
- **`docs/portfolio-overview.md`:** not held directly; no change (see Against World, layer, NVIDIA
  and HY).

## Change log

- **17 Oct 2026 — version 1** (iaf-valuation 2026-10-11.3; ai-market-bbb 2026-10-16.1;
  equity-market-bbb 2026-10-16.1, document of 11 Oct; NVIDIA analysis version 1 of the same day).
  No previous version.
- **5 Nov 2026 — version 1.1, light update** (iaf-valuation **2026-11-01.1**; ai-market-bbb
  2026-11-01.1, document of 1 Nov (Update 6) with the 5 Nov note; NVIDIA 1.1 of 2 Nov; HY
  BBB 5 Nov; Equity BBB 17/18 Oct). No company report.
  - Inputs: H3 Bear reconciled to .76 / .63 / .67 / .71 (Bear −6.3% → −13.2% at the old price); CY27
    consensus $23.11 → $23.43 (Base 7.4% → 7.9%); HY reference E / R 0.196 → 0.254 and NIBOR
    unchanged; Equity BBB and NVIDIA: comparators only.
  - Price: $412.61 → $352.03 (5 Nov close, −11.0% on the day, sector sell-off after the midterms; no
    company news); valuation date 17 Oct → 5 Nov; USD/TWD 32.428 → 33.027; USD/NOK 9.4135 → 9.3105.
  - Result: Base **13.7%**, P_k **$368.9**, margin **+4.8%: fails → clears**. Bear −8.5% (P_k $189.6),
    Bull 26.0% (P_k $506.5). E / R 0.079 → 0.206 (reference 0.254).
  - Method items added: Summary in USD per ADS per scenario with trigger prices and Taipei
    equivalents, the cycle lead and the price-implied multiplier, the exit cross-check against World,
    the NOK path label. The model was rebuilt from this document's inputs and reproduces version 1
    exactly.
  - Not done (light update): the broker targets, Zacks estimates and the ADR premium history were not
    re-read; the HY book and DNB Teknologi rows are carried from `docs/portfolio-overview.md`.
- **11 Nov 2026 — version 1.2, signpost update and price re-mark** (iaf-valuation **2026-11-10.1**;
  ai-market-bbb document Update 7 of 7 Nov, skill 2026-11-06.1; Equity BBB **6 Nov** (Update 2; 1.1
  read 17/18 Oct); HY BBB 5 Nov; NVIDIA not re-read). Cause: the register event "TSMC October
  revenue (monthly 6-K, ~10th)".
  - **11 Nov: October revenue NT$586.89bn, +59.7% y/y: signpost Bull-side level hit; kept** (Q4 on
    the upper half of the guide, not above it: stub unchanged). The same day's board: 3Q26 dividend
    NT$9.0 (replaces the model's NT$8.0; ladders re-based, retained cash lower by the same amount),
    appropriations $40.93bn (not modelled), ≤ $1.5bn of AI-lab and strategic stakes (immaterial).

  | Step (in order) | Base IRR / P_k / margin of safety | Bear IRR (P_k) | Bull IRR (P_k) |
  |---|---|---|---|
  | 1.1 (5 Nov; $352.03) | 13.7% / $368.9 / +4.8% | −8.5% ($189.6) | 26.0% ($506.5) |
  | Inputs: ai Update 7 (no path), equity 6 Nov (comparators and exit references only), hy unchanged, consensus $23.43 kept ($23.39, −0.2%) | no value change | — | — |
  | October revenue (stub check: Q4 tracks the guide) | no value change | — | — |
  | Dividend NT$9.0 and re-based ladders (net cash at exit Base −$1.67, Bear −$1.82, Bull −$0.83 per ADS) | 13.7% / $369.2 / +4.9% | −8.5% ($189.8) | 26.0% ($506.6) |
  | **Price, date and FX:** $352.03 → **$396.48**; 5 Nov → 10 Nov (T 3.16 → 3.14); USD/TWD 33.027 → 32.789; USD/NOK 9.3105 → 9.4010 | **9.5% / $369.8 / −6.7%** | **−12.0% ($190.2)** | **21.3% ($507.5)** |

  - **Verdict flips: clears (+4.8%) → fails (−6.7%)**, on the price alone (+12.6% from the 5 Nov
    sell-off close). E / R 0.206 → 0.106 (reference 0.254). Price implied: 0.95× → 1.07× Base
    2028–30 (0% at 0.76× on the rebuilt model; 1.1 stated 0.66×, the rebuild gives 0.68× at the
    1.1 price).
  - The Summary, decision table, triggers, per-share path, results, sensitivities, V_T bridge, exit
    cross-check, E / R table and signposts carry 1.2; the 1.1 and version 1 blocks below them stay
    as the record. The HY book and DNB Teknologi comparator rows are dropped (portfolio document
    retired 9 Nov).
  - Not done: broker targets, Zacks estimates and the ADR premium history not re-read; NVIDIA not
    re-read (Q3 on 17 Nov).

## Appendix: own assumptions `[A]`

By weight on the result:
1. **EPS path** = AI BBB H3 layer × CY27 consensus $23.11 (Yahoo ADS, 14); 2030 normalised $26.80,
   core $24.97.
2. **Exit P/E 14 / 18 / 21** on 2030 core EPS (the AI BBB reference; cross-checked against TSM's
   2021–25 year-end P/E on realised next-year EPS, 14.4–18.5, and today's 17.85).
3. **Interest strip:** net interest 4.0% pre-tax, 17% tax, on net cash; removed from the exit EPS
   because net cash is added at face.
4. **ADR premium** held at 10.6% to exit.
5. **Net cash at the valuation date** $88.9bn; at 31 Dec 2026 $99.7bn (Q4 free cash flow NT$430bn:
   net income at consensus, D&A NT$240bn, capex $21.4bn, credits NT$20bn).
6. **Capex** Base $76 / 82 / 85bn (Bear 70 / 60 / 55; Bull 82 / 95 / 105); D&A from five-year
   lagged capex; US investment tax credits $4bn a year (Bear $3bn).
7. **Dividends** stepping up NT$1.0 every half-year in Base (NT$32 / 40 / 48 a share paid), NT$0.5
   in Bear, NT$1.5 in Bull; ADS paid about a week after Taipei. **1.2:** re-based on the declared
   3Q26 NT$9.0 (Base NT$35 / 44 / 52; Bear 34 / 38 / 42; Bull 35.5 / 49.5 / 60).
8. **Revenue** = H3 index × $176.1bn, for working capital at 10% of the change.
9. **Stub:** Q4 consensus EPS $5.16, 76/92 of the quarter; price flat.
10. Year-1 quarterly split (~+7% q/q) and haircuts (Base 0.99 / 0.96 / 0.94 / 0.92).
11. Revenue-consistent Bear net margins 47 / 43 / 44 / 45%; management-path EPS 1.00 / 1.08 /
    1.165 / 1.26; margin-reversion factors 0.94 / 0.89 / 0.83.
12. Shares 25,932m, flat; tax 17% for the EBITDA display only.

## Appendix: sources

| # | Source | Content | As of |
|---|---|---|---|
| S1 | [TSMC 3Q26 Management Report](https://investor.tsmc.com/english/quarterly-results/2026/q3) (PDF, investor.tsmc.com) | Income statement (revenue NT$1,494.24bn, GP 992.38, OI 876.45, NI 763.06, EPS 29.43 / $4.60); mix by node, platform, region; balance sheet (cash and securities 4,016.98, debt 1,031.58, net cash 2,985.40, dividends payable 363.05); cash flow (OCF 919.77, D&A 220.20, capex 443.21, other investing 198.74, dividends 155.59, FCF 476.56; Q2 FCF 287.36, Q1 348.21, 4Q25 368.60); capex $13.84bn (YTD 40.64); diluted shares 25,932m; 2Q26 dividend dates | 15 Oct 2026 (quarter to 30 Sep) |
| S2 | [TSMC 3Q26 earnings call transcript](https://investor.tsmc.com/english/quarterly-results/2026/q3) (LSEG StreetEvents, PDF) | Q4 guide; 2026 ~+44%; capex $60–64bn and 2026–28 outlook; overseas dilution 2% → 3–4 pp; AI accelerator CAGR; N2, N3, A14, Arizona, Japan, Texas; ROE 45.5%; Q&A on demand, power, funding, pricing, competition | 15 Oct 2026 |
| S3 | [TSMC Q3 2026 release](https://pr.tsmc.com/english/news/3346) | Headline results, Q4 guidance, FX assumption 31.8 | 15 Oct 2026 |
| S4 | TSMC Form 6-K, board resolutions ([EDGAR](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000536/tsm-boardx20260811.htm)) | 2Q26 dividend NT$7.0, ex 10 Dec 2026 (shares and ADS), record 16 Dec, paid 7 Jan 2027; capital appropriations $29,442.5m; Sony JV | 11 Aug 2026 |
| S5 | TSMC Form 6-K, September revenue ([EDGAR](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000680/tsm-revenue20261008.htm)) | September NT$511.86bn (+54.6% y/y); nine months NT$3,898.73bn (+41.1%) | 8 Oct 2026 |
| S6 | TSMC Form 6-K, 1Q26 dividend adjustment (EDGAR) | 1Q26 dividend NT$181,526,590,469 (NT$7.0), paid 8 Oct 2026 | 2026 |
| S7 | SEC EDGAR submissions (`data.sec.gov`, CIK 0001046179) | Filings since 1 Jul 2026: 14 Forms 6-K, 153 Forms 4; no share issue | 15 Oct 2026 (latest) |
| S8 | Yahoo quote, `earningsTrend`, chart and dividend events (TSM, 2330.TW, TWD=X, NOK=X) | **TSM $412.61 (16 Oct close)**, mcap $2,140bn; 2330.TW NT$2,420; ADS consensus Q4-26 $5.16 (8), Q1-27 $5.19 (10), CY26 $17.31 (12), CY27 $23.11 (14); Taipei consensus Q4-26 NT$32.96 (22), CY26 NT$110.13 (35), CY27 NT$148.61 (36); revenue CY26 NT$5,561bn, CY27 NT$7,647bn; dividends (2330.TW NT$ and TSM $ per ex-month); 2-year daily closes for the ADR premium; 6-year monthly closes; USD/TWD 32.428; USD/NOK 9.4135 | 16–17 Oct 2026 |
| S9 | [Zacks TSM quote](https://www.zacks.com/stock/quote/TSM): profile, EDT estimates, broker ratings (60 days) | Rank 1 (from 17 Oct); ABR 1.21 (19); average target $523, Zacks target $508; F1 $16.65 / F2 $21.50 (9 each); Q4-26 $4.74 (5); LTG 29.2%; dividend $0.87 net, last ex 16 Sep; beta 1.37; Barclays $665 (6 Oct), Citi Strong Buy (7 Oct) | 16–17 Oct 2026 `[E]` |
| S10 | Zacks news: [Q3 earnings article](https://www.zacks.com/stock/news/3008590/taiwan-semiconductor-q3-earnings-&-revenues-top-estimates,-margins-up) (15 Oct 09:18 ET), [ETF article](https://www.zacks.com/stock/news/3009915/tsmc's-record-q3-earnings-&-upbeat-outlook-put-these-etfs-in-focus-) (16 Oct 10:00 ET), [commentary](https://www.zacks.com/commentary/3010184/taiwan-semiconductor-posts-record-q3-results:-time-to-buy-the-dip?) (16 Oct 18:36 ET) | Cross-check of Q3 figures, guidance, 2026 growth, dividend; Zacks consensus before the report ($4.45 EPS, $45.61–45.62bn revenue) | 15–16 Oct 2026 `[E]` |
| S11 | [KGI research note on TSMC's January 2026 guidance](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_15012026e.pdf); [VanEck on the Q1 2026 call](https://www.vaneck.com/pe/en/news-and-insights/blogs/thematic-investing/tsmc-q1-earnings-call-what-it-means-for-smh/) | 2024–29 revenue CAGR ~25%, AI accelerators mid-to-high 50s, long-term gross margin 56% and higher | 15 Jan / Apr 2026 `[E]` |
| S12 | `docs/ai-market-bbb.md` (Update 1, amended 16 Oct) and `references/model.py` | H3 path, exit P/E, revenue index, basket, scenarios, signposts | 15–16 Oct 2026 |
| S13 | `docs/nvda-analysis.md` (version 1) | NVIDIA path, supply commitments, Bear, result and E / R | 17 Oct 2026 |
| S14 | `docs/equity-market-bbb.md`, `docs/hy-market-bbb.md`, `docs/portfolio-overview.md`, `docs/global-index-funds-analysis.md`, `docs/dnb-teknologi-analysis.md` | Macro scenarios, USD/NOK path, World return, HY reference and book, NIBOR, fund weights | 5–15 Oct 2026 |
| S15 (1.1) | Yahoo `get_quote` (TSM, 2330.TW, NOK=X, TWD=X) and `quoteSummary` (`earningsTrend`, `calendarEvents`) for TSM | **TSM $352.03, NYSE regular close 5 Nov 2026** (20:59:59 UTC; previous close $395.75; post-market $355.87); 2330.TW NT$2,240 (5 Nov 05:30 UTC; previous NT$2,260); USD/TWD 33.027 and USD/NOK 9.3105 (21:09 UTC); CY27 $23.43 (14; 7 days ago 23.39, 30 days ago 21.92), CY26 $17.49 (12), Q4-26 $5.16 (8), Q1-27 $5.19 (10); Q4 report 14 Jan 2027 (estimate); ex-dividend 10 Dec, paid 7 Jan | 5 Nov 2026 |
| S16 (1.1) | SEC EDGAR submissions (CIK 0001046179); 6-K of 22 Oct (September monthly report); web search for October revenue | No filing with revenue or results since 15 Oct; no share issue; October revenue not yet released | Checked 5 Nov 2026 |
| S17 (1.1) | `docs/ai-market-bbb.md` (Updates 2–6 and the 5 Nov note on the midterms and the chip sell-off), `docs/nvda-analysis.md` 1.1, `docs/hy-market-bbb.md` (5 Nov), `docs/equity-market-bbb.md` (17/18 Oct) | H3 paths, K1, signposts, 5 Nov market table; NVIDIA demand signal and result; NIBOR and HY reference E / R 0.254; World, NOK path and exit references | 17 Oct–5 Nov 2026 |
| S18 (1.2) | TSMC Form 6-K, October revenue ([EDGAR](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000796/tsm-revenue20261110.htm)); TSMC Form 6-K, board resolutions ([EDGAR](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000797/tsm-boardx202611xx.htm)); EDGAR submissions (CIK 0001046179) | October NT$586,890m (+14.7% m/m, +59.7% y/y; October 2025 NT$367,473m); Jan–Oct NT$4,485,617m (+43.3%). Board: Q3 statements approved; **3Q26 dividend NT$9.0**, ex 11 Mar 2027, record 17 Mar, paid 8 Apr 2027 (ADS ex and record 11 Mar); **capital appropriations US$40,926.70m**; up to $0.5bn each for an investment company, Anthropic common shares at the IPO price and OpenAI preferred. No share issue | 10 Nov 2026 |
| S19 (1.2) | Yahoo `get_quote`, `get_chart` (TSM, 2330.TW, TWD=X, NOK=X) and `quoteSummary` (`earningsTrend`, `calendarEvents`) | **TSM $396.48, NYSE regular close 10 Nov 2026** (21:00:02 UTC; previous $388.62; post-market $402.59); closes 5 / 6 / 9 Nov $353.10 / 375.44 / 388.62; 2330.TW NT$2,285 (10 Nov) and NT$2,395 (11 Nov 05:30 UTC); USD/TWD 32.789 (10 Nov daily close; October month open 31.87, close 32.61) and USD/NOK 9.4010 (10 Nov daily close); CY27 $23.39 (13), CY26 $17.50 (11), Q4-26 $5.16 (8), Q4 revenue NT$1,708bn (26), Q4-25 revenue NT$1,046.09bn; Q4 report 14 Jan 2027 (estimate); ex-dividend 10 Dec, paid 7 Jan | 10–11 Nov 2026 |
| S20 (1.2) | `docs/ai-market-bbb.md` (Update 7, 7 Nov), `docs/equity-market-bbb.md` (Update 2, 6 Nov), `docs/hy-market-bbb.md` (5 Nov) | H3 paths unchanged; World 6.6% / −18.3% / 0.080, exit references 17.0 / 3.17 / 8.2%, NOK relative path unchanged; NIBOR 4.38%, HY reference 0.254 | 5–7 Nov 2026 |

- **Validation notes (1.2):**
  - **Price:** the 10 Nov close is the latest regular-session print (the analysis runs before the
    11 Nov US open). The 5 Nov settled close is $353.10 against the $352.03 regular-market print 1.1
    used (0.3%); 1.1 is not restated.
  - **October revenue:** +59.7% y/y, consistent with the Q4 guide's +58% y/y in USD and inside the
    guide's USD range: plausible, from the primary 6-K (which gives no breakdown). The NT$ figure gains from the
    weaker NT$ (October ~32.3 against the guide's 31.8).
  - **Consensus:** CY27 $23.39 (13) vs $23.43 (14) on 5 Nov: −0.2%, noise; the anchor is kept.
    Yahoo's "7 days ago" value ($22.30) does not match the 5 Nov print ($23.43): a Yahoo trend quirk,
    not used.
  - **USD/NOK:** the 11 Nov quote's bid/ask (9.389 / 9.392) is inconsistent with its price (9.4954);
    the 10 Nov daily close 9.4010 is used. NOK is a memo only (Base NOK = USD).
  - **Dividend:** NT$9.0 is a step of NT$2.0 against TSMC's usual NT$0.5–1.0; confirmed in the
    primary 6-K; Yahoo still shows the 2Q26 NT$7.0 (ex 10 Dec) as the next event, consistent.
- **Validation notes (1.1):**
  - **Price:** the 5 Nov close is the latest print (same day). The 11.0% fall has a named cause
    (sector sell-off, SOX ~−10%; AI BBB market table) and no company news; it is a market print, not
    a data error.
  - **ADR premium:** 3.8% close-on-close is not a valid level: Taipei closed before the US move.
    Unverified until the 6 Nov Taipei close.
  - **Consensus:** CY27 +1.4% since 17 Oct (23.39 on 1 Nov in the AI BBB): consistent with the
    post-Q3 revisions; the Taipei forward EPS NT$149.53 at 33.027 is $22.64 per ADS (−3.4%), partly
    the weaker NT$ and a different period basis; the ADS figure is the AI BBB's source and is used.
  - **USD/NOK:** Yahoo 9.3105 vs 9.3095 given with the task; NOK is a memo only.
- **Validation notes (version 1):**
  - **Price staleness:** the 16 Oct close is the latest (valuation date is a Saturday).
  - **Consensus cross-check:** Yahoo ADS CY27 $23.11 (14) vs Taipei NT$148.61 (36) = $22.91 at spot
    (−0.9%, noise). Zacks $21.50 (9) is 7% lower; its "most recent" figure ($22.26) shows it lags the
    post-Q3 revisions; used only as a sensitivity. Yahoo's CY26 ADS consensus ($17.31) is below nine
    months' actuals plus Q4 consensus ($17.56): some estimates are not yet updated.
  - **Q4 consensus vs guide:** consensus $5.16 per ADS ≈ the guide-implied ~$5.0–5.1 at spot FX;
    Zacks' $4.74 (5) predates the guide.
  - **Yahoo ADS P/B (64.7)** mixes a USD price with NT$ book value; not used (Taipei 11.7×).
  - **Dividend per ADS:** Yahoo $1.107 (gross) vs Zacks $0.87 (net of 21% Taiwan withholding);
    both consistent with NT$7.0 × 5 ÷ ~31.6.
  - **ADR premium** uses same-date closes that are not simultaneous (Taipei closes ~05:30 UTC, New
    York 20:00 UTC); on a volatile day the gap is a few points of noise (16 Oct: ADS −2.3% after
    Taipei's close).
  - **Plausibility:** Q3 other investing (+NT$198.7bn) is far above Q2 (+NT$40.2bn); the management
    report attributes it to US Treasury investment tax credits, confirmed. Modelled at $3–4bn a
    year, not at the Q3 rate. Q2 net income includes VIS disposal and mark-to-market gains
    (non-operating NT$67.4bn); the path uses consensus, which excludes nothing, so no adjustment.
  - **Net cash** is NT$, converted at spot; 30 Sep FX 31.85 would give $93.7bn instead of $92.1bn
    for the 30 Sep figure.
  - **FinancialFilings** was not used; the filing check and statements come from EDGAR and TSMC's
    own documents (primary sources).
- **Scripts:** the model (`tsmmodel.py`), sensitivities (`tsmsens.py`), tables (`tsmtab.py`) and
  the ADR premium (`prem.py`) were run in the session scratchpad. As for the other IAF analyses,
  they are not stored in the skill. Every input is in Common assumptions and Appendix: own
  assumptions, so the build can be reproduced.
