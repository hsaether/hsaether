# Microsoft Corporation (MSFT) — IAF analysis, stub Q4 2026 + 2027–2029

> **7 Nov 2026, price re-mark at the 6 Nov close, upstream re-read** (iaf-valuation
> **2026-11-01.1**; its new rule for opportunistic cyclical positions does not apply: Microsoft is
> Track A and not rate-driven).
> - **Change gate.**
>   - The AI BBB (Update 7 of 7 Nov) moved no row this analysis reads: E2, T1, T3 and K1 are
>     unchanged, as are the E-layer path (.92 / 1.07 / 1.17 / 1.27) and its exit P/E 21.
>   - The Equity BBB of 6 Nov (Update 2) kept its scenarios and the NOK relative moves. Only its
>     spot (USD/NOK 9.29) and its comparison values moved: World Base 5.2% → 6.6%, E / R 0.024 →
>     0.080, exit P/B 3.14 → 3.17.
>   - The HY BBB of 5 Nov kept NIBOR (4.38%). It moved the HY market Base (6.8% → 7.2%) and the
>     market reference (E / R 0.196 → **0.254**; 0.216 with the Bear read as a shock), and these
>     set this analysis's E / R price trigger.
>   - So the update touches values read here. It is a re-mark; the model is unchanged.
> - **Filings since 28 Oct (EDGAR) `[F]`:**
>   - **$25.0bn of senior notes** were priced on 29 Oct and settled on 4 Nov (8-K of 4 Nov; FWP of
>     30 Oct; 424B2 of 2 Nov). Aaa / AAA, ten tranches from 2028 to 2066: fixed coupons 4.85–6.35%
>     and two $1bn floating-rate notes at SOFR + 35 / + 53 bp. Use of proceeds: "general corporate
>     purposes", which may include capex and buybacks.
>   - This is cash in and debt in, so net cash does not move. The carry (≈ $1.4bn a year of coupon
>     against interest on the cash) is ≈ −$0.04 of EPS a year, ≈ −0.02 pp: **not applied**. On the
>     28 Oct call debt was "not yet" tapped; it now is (a K3 item for the AI BBB).
>   - No share issue. The 8-K of 5 Nov is a director (Walmsley) not standing for re-election. Shares
>     7,426.2m (10-Q cover, Yahoo 7 Nov).
> - **Applied:**
>   - Price **$531.01 → $530.61** (MSFT regular close 6 Nov, Yahoo, 21:00 UTC; −0.1%). The path in
>     between: $507.12 on 2 Nov, $555.80 on 4 Nov (midterm day), $535.93 on 5 Nov.
>   - Valuation date 28 Oct → 6 Nov (T 3.18 → 3.15). Still cum-dividend: ex-date 19 Nov.
>   - USD/NOK 9.2540 → **9.4665** (Yahoo `NOK=X`, 21:00 UTC bar). Norges Bank fixing 9.4277 and I-44
>     108.79 (1.1% stronger than 110.0, so Base stays spot flat). Equity BBB NOK path of 6 Nov.
>   - HY reference 0.254 and the pre-alert at the HY market Base 7.2% (new trigger, as in
>     `docs/googl-analysis.md` and the Equity BBB).
> - **Not applied:**
>   - consensus drift (CY27 21.72 → 22.09; Q4-26 EPS 4.82 → 4.86);
>   - the bond carry (above).
>
>   The Q4-26 base stays on the guide midpoint and the consensus of 28 Oct.
> - **Result:**
>   - **Base 9.5% → 9.6%**, P_k $494.5 → **$495.9**, margin of safety −6.9% → **−6.5%: still
>     fails.**
>   - Bear −7.4% (NOK −4.8%), unchanged. Bull 19.7% → 19.9% (NOK 18.5% → 18.7%).
>   - Bridge (9.49% → 9.60%): date +0.08 pp (P_k +$1.4), price +0.03 pp.
>   - E / R 0.131 → **0.134**.
>   - **Triggers:**
>     - Base = k at **$495.9 (−6.5%)**.
>     - E / R = 0.254 at **$441.3 (−16.8%)**. It was $484.1 at 0.196 and would be $486.2 at 0.196
>       today. With the Bear read as a shock (0.216): $471.2.
>     - Pre-alert (Base = HY 7.2%) at **$568.5: crossed** (price below it).
>   - EPS, D_t and V_T are unchanged. The interim V_t of Base and Bull re-glide from the starting
>     core P/E of 24.10 (24.12 before): −$0.3.
>
> **4 Nov 2026, kept unchanged (change gate):** read AI Market BBB Update 6 of 1 Nov: the E2, T1, T3 and K1 rows are unchanged. No figure in this analysis changes.

> **29 Oct 2026, kept unchanged (change gate):** read AI Market BBB Update 5 of 29 Oct; the E2, T1, T3 and K1 rows are unchanged. No figure in this analysis changes.

**Version 3 — 28 Oct 2026, price re-mark at the 6 Nov close (7 Nov 2026; iaf-valuation
2026-11-01.1; model unchanged)** (post-report update after the Q1 FY27 report of 28 Oct, quarter to
30 Sep 2026, and its earnings call; version 2 of 15 Oct, initial version 12 Oct). Skill revisions
used: **iaf-valuation 2026-10-18.2** for v3, **2026-11-01.1** for the 7 Nov re-mark (versions 1–2:
2026-10-11.3; the method changes are listed under "Change since 15 Oct" and in the change log).
**Sector inputs read on 7 Nov:** `docs/ai-market-bbb.md` Update 7 of 7 Nov (ai-market-bbb
2026-11-06.1; rows read unchanged since 15 Oct); `docs/equity-market-bbb.md` Update 2 of 6 Nov
(equity-market-bbb 2026-10-24.1); `docs/hy-market-bbb.md` of 5 Nov (hy-market-bbb 2026-10-24.1).
The bullets below describe the inputs as read for v3; the 7 Nov changes are in the top note.
Sector inputs:
- `docs/ai-market-bbb.md`, **Update 4 of 24 Oct 2026** (ai-market-bbb rev **2026-10-24.1**, method
  v2.1; Updates 2 of 17 Oct and 3 of 22 Oct came in between; version 2 read Update 1 of 15 Oct).
  It supplies the scenarios and catalysts (financing break / contracted build then digestion /
  agentic adoption), the E2 hyperscaler cloud growth row (used for Azure), the T1 Copilot seat row
  and the T3 incumbent software row (used for Productivity and Business Processes), the K1 capex
  path and K3/K4 financing and backlog context, the E-layer EPS path and exit P/E (consistency
  check), the E basket's exit cross-check and the signposts. **The rows used here (E2, T1, T3, K1)
  are unchanged since 15 Oct**; the E-layer Bear and Bull now follow this analysis's own Bear and
  Bull (with Alphabet's and Amazon's). This analysis makes no AI market forecast of its own.
- `docs/equity-market-bbb.md`, **17 Oct 2026, amended 18 Oct** (document produced with
  equity-market-bbb 2026-10-18.5; skill now 2026-10-24.1, no value changed; version 2 read the
  11 Oct baseline). It supplies the macro scenarios the AI scenarios sit inside, the NOK path
  (Base spot flat; Bear USD/NOK +12% / +9% / +9%; Bull −3%: the same relative moves as on 11 Oct),
  World's Base IRR **5.2%** (was 6.1%) and E / R **0.024** (was 0.063), and the exit references
  for the new cross-check: World exit P/E **17** (Bear 15, Bull 18.5), exit P/B **3.14** and
  mid-cycle return **8.2%**.
- `docs/hy-market-bbb.md`, **24 Oct 2026** (hy-market-bbb 2026-10-24.1, kept unchanged): Base window
  NIBOR **4.38%** (E / R) and the HY market reference E / R **0.196**. Microsoft is AAA-rated with
  net cash; no HY refinancing test applies. The oil, rig, supply, shipping and defense baselines
  are not used.

## Summary

**Verdict**
- **Fails (re-mark 7 Nov, 6 Nov close $530.61).** Base IRR **9.6% a year** (USD; NOK the same in
  Base) against k = 12% (28 Oct: 9.5%; 15 Oct 8.8%). Hurdle price **P_k $495.9 vs P $530.61:
  margin of safety −6.5%** (28 Oct −6.9%; 15 Oct −8.9%). The price is about where it was on 28 Oct;
  the later date adds +0.08 pp, and the model is unchanged. The $25bn bond of 4 Nov leaves net cash
  unchanged.
  The Rule 1 screen at constant P/E passes only marginally (d + g = 12.6%, assumes today's P/E
  holds), and Rule 3 fails clearly (P/E 28.3 on CY26 against a ceiling of 8.7).
- **28 Oct (version 3): the report left the value about where it was; the price did the rest.** Of the +0.7 pp in
  Base, the method and the AI and Equity inputs add nothing, the report +0.0 pp (a higher 2026
  base from the Q1 beat and the Q2 guide, offset by lower net cash, finance-lease principal and a
  24% OpenAI stake instead of 26.8%), and the lower price and later valuation date +0.7 pp. The
  quarter ran **ahead on the P&L** (revenue +1.8% and EPS +3.6% above consensus, Azure +48%
  against a 44–45% guide and 49–50% guided for Q2, margin 49.8%) and **behind on backlog and
  cash** (commercial RPO flat q/q at $677bn, bookings −12% y/y; net cash $36.5bn → $29.0bn after
  $12.9bn of component prepayments; capex $45.2bn against "> $50bn" as third-party capacity
  slipped).
- **Bear still breaks the thesis for a 3-year holder:** −7.4% a year in USD (−4.8% on the Equity
  BBB NOK path). The share falls ~36% in 2027, and capital is not preserved (ΣD + V_T is 21% below P).
  The balance sheet is never at risk: AAA, net cash, and FCF rises in Bear once capex is cut. The
  10-Q now shows the Bear channel directly: **OpenAI was $10.0bn of revenue in the quarter (10.8%)**.
- **What the price needs:** an exit P/E of **~24.8** on 2030 EPS (Base 23), or EPS growth of **~14%
  a year 2028–30** (Base ~11%), or Azure 5 pp a year above the AI BBB E2 row (→ ~12.4%, margin of
  safety ~+1%, marginal; v3 12.3% / +0.7%, moved with Base).
- **Triggers (7 Nov):**
  - Base reaches k at **$495.9 (−6.5%)**.
  - E / R reaches the HY reference (now **0.254**, was 0.196) at **$441.3 (−16.8%)**. The HY market
    now pays more per unit of stress, so this trigger is deeper; it was $484 at 0.196.
  - The pre-alert (Base = the HY market's 7.2%) is at $568.5, so it is crossed at today's price.
  - On 4 Nov the share closed at $555.80. Base is 8.0% there (margin of safety −10.8%), still a
    fail.

**Decision table (USD, per share; MSFT on Nasdaq at $530.61, 6 Nov close)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (USD) / NOK path (Equity BBB) | −7.4% / −4.8% | **9.6% / 9.6%** | 19.9% / 18.7% |
| V_T (31 Dec 2029) | 404 | **692** | 921 |
| P_k (USD) / margin of safety | 294 / −44.6% | **495.9 / −6.5%** | 656 / +23.7% |
| Price triggers (USD) | | **Base = k: 495.9 · E / R = 0.254: 441.3 · pre-alert (Base 7.2%): 568.5 (crossed)** | |
| Capital preserved? (ΣD + V_T vs P) | **No: −21%** | Yes: +33% | Yes: +76% |
| Cumulative FCF 2027–29 | 33.7 | **31.1** | 24.2 |
| Net cash at exit (ex leases) | 19.7 | **11.7** | 1.3 |
| Balance sheet | AAA; net cash rises to ~$146bn as capex is cut (FCF $97–113bn a year in 2028–29) | Net cash ~$19bn at end-2026, ~$87bn at exit; finance-lease liabilities $71bn on balance sheet and $365bn of leases not yet commenced come on top | Capex $240–300bn a year absorbs OCF; ~$10bn net debt (ex leases) at end-2028 |

**Per-share path (USD; Track A rows; years are calendar years)**

| | CY26 (3 actual + 1 cons.) | 2027 | 2028 | 2029 | 2030 (exit-year EPS) |
|---|---|---|---|---|---|
| Base EPS (non-GAAP, ex OpenAI) | 18.72 | 20.77 | 23.40 | 26.11 | 28.39 |
| Base EPS growth | | +11.0% | +12.7% | +11.6% | +8.7% |
| Base D_t (dividends paid) | 0.98 (stub) | 4.01 | 4.37 | 4.76 | |
| Base FCF per share | | 6.96 | 10.24 | 13.92 | |
| Base V_t (year-end) | 530.6 (stub flat) | 585.4 | 643.1 | 692.1 | |
| Bear EPS / FCF / V_t | | 18.18 / 5.52 / 338 | 17.84 / 12.99 / 369 | 19.16 / 15.18 / 404 | 20.61 |
| Bull EPS / FCF / V_t | | 22.03 / 5.20 / 681 | 26.26 / 7.47 / 806 | 30.37 / 11.52 / 921 | 33.80 |

**Change since 15 Oct (Base, USD)**

| Step | Base IRR | P_k | MoS | What moved |
|---|---|---|---|---|
| Version 2 (15 Oct, $540.26) | 8.8% | 492.4 | −8.9% | |
| 1. Method (iaf-valuation 2026-10-11.3 → 2026-10-18.2) | +0.0 pp | 0.0 | 0.0 | Exit principle, Track A exit rule, exit cross-check, NOK path label: all already practice here; new cross-check table |
| 2. AI and Equity BBB inputs | +0.0 pp | 0.0 | 0.0 | E2, T1, T3, K1 and the NOK path's relative moves unchanged; only the comparisons move (E basket 6.9%, World 5.2%) |
| 3. Report and call (at the 15 Oct price and date) | **+0.0 pp** (8.78 → 8.79) | +0.1 | +0.1 pp | CY26 base +0.40 pp (Q1 beat; Q2 guide $96.0–97.1bn, Azure 49–50%); shares and OpenAI 24% −0.15 pp; net cash at 31 Dec (~$19bn, was $36.5bn) and finance-lease principal −0.24 pp |
| 4. Price, FX and date | **+0.7 pp** (8.8 → 9.5) | +2.0 | +1.9 pp | $540.26 → $531.01 (−1.7%); valuation date 15 → 28 Oct (T 3.21 → 3.18); USD/NOK 9.47 → 9.25 (no effect in USD or on the NOK-path IRR) |
| **Version 3 (28 Oct, $531.01)** | **9.5%** | **494.5** | **−6.9%** | |
| 5. Re-mark 7 Nov: date 28 Oct → 6 Nov (T 3.18 → 3.15) | +0.08 pp | +1.4 | +0.3 pp | Model, inputs and the rows read unchanged; the $25bn bond is cash and debt (net cash unchanged) |
| 6. Price $531.01 → $530.61 | +0.03 pp | 0.0 | +0.1 pp | |
| **Re-mark 7 Nov ($530.61, 6 Nov close)** | **9.6%** | **495.9** | **−6.5%** | |

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value ·
`[E]` external or secondary · `[C]` carried from an earlier version · `[A]` own assumption ·
`[?]` not found or unverified.

## Header

| Item | Value |
|---|---|
| Company | Microsoft Corporation, Nasdaq: MSFT. Fiscal year ends 30 June. **Q1 FY27 (quarter to 30 Sep 2026):** revenue $92.3bn (+19%), operating income $45.9bn (49.8%), non-GAAP EPS $4.89 (GAAP $4.92; OpenAI +$0.03) `[F]` (8-K Ex. 99.1 and 10-Q, 28 Oct 2026). FY26: revenue $331.8bn, operating income $155.2bn (46.8%), non-GAAP EPS $17.28 `[C]` |
| Price (P) | **Re-mark 7 Nov: $530.61**, Yahoo `MSFT`, regular close 6 Nov 2026 21:00 UTC (day range 524.47–538.33; 52-week high now 559.15 on 4 Nov) `[F]`. Version 3: **$531.01**, Yahoo `MSFT`, regular close 28 Oct 2026 20:00 UTC (previous close $531.33; the report came after the close). After hours **$544.18** (+2.5%) at 21:04 UTC, before the call `[F]`; Investing.com reports up to $554.68 (+4.5%) later `[E]`: a sensitivity, not the decision price. Version 2: $540.26 (15 Oct). 52-week range 349.20–551.15 `[F]` |
| Valuation date / exit date | **6 Nov 2026** (re-mark) / 31 Dec 2029, **T = 3.15 years** (version 3: 28 Oct, T = 3.18; version 2: 15 Oct, T = 3.21). Cum-dividend: ex-date 19 Nov |
| Shares | **7,426.2m** outstanding on 22 Oct 2026 `[F]` (10-Q cover; Yahoo 7,425.5m, Zacks 7,426.4m). Diluted weighted average Q1 FY27 7,446m `[F]`. Held flat: buybacks ($2.9bn under the programme plus $1.5bn for tax withholding in Q1) offset stock-based dilution, so buybacks are a use of cash, not a per-share return (counted once, see Common assumptions) |
| Market cap / EV | $3.94tn. **Net cash ex leases $29.0bn** ($3.91/share) at 30 Sep 2026: cash and short-term investments $64.5bn less debt $4.4bn current and $31.1bn long-term `[F]` (was $36.5bn at 30 Jun; $4.85bn of debt repaid). **$25.0bn of new notes settled 4 Nov** (2028–2066, 4.85–6.35% fixed, FRNs SOFR + 35 / + 53 bp; 8-K 4 Nov `[F]`): gross debt ≈ $60.5bn, net cash unchanged. Lease liabilities **$98.4bn** (finance $71.0bn, operating $27.5bn) `[F]`; leases not yet commenced **$364.6bn** (FY27–FY34 starts; was $329.1bn) `[F]`. **EV ≈ $4.01tn** incl. lease liabilities |
| P/E | **Re-mark 7 Nov ($530.61):** 28.3x CY26; 24.0x CY27 consensus ($22.09 = average of FY27 $20.00 and FY28 $24.18; 32 and 33 analysts, Yahoo 7 Nov); 25.5x CY27 Base; core P/E **24.10x** on Base (22.7x on consensus). Version 3 ($531.01): 28.4x CY26 (EPS $18.72: three reported quarters + Q4-26 consensus); 24.4x CY27 consensus ($21.72 = average of FY27 $19.76 and FY28 $23.69; 34 and 33 analysts, Yahoo 28 Oct, before the report); 25.6x CY27 Base ($20.77). **Core P/E** (price less the OpenAI stake and net cash, on Base CY27): **24.1x** (23.1x on consensus) |
| NAVs (Step 3) | Not applicable (no tradeable asset marks; Track A). In their place, the price split (re-mark 7 Nov): **core business $500.5 + OpenAI stake $27.5 + net cash $2.6 (31 Dec 2026E) = $530.61** (v3: $500.9 core, $531.01) |
| OpenAI stake | **~24% on an as-converted basis** `[F]` (10-Q note 1; version 2 used ~26.8% `[E]`), equity method (HLBV), carried far below market. At the $852bn valuation (Mar-2026 round, confirmed by the Aug-2026 secondary `[E]`) **≈ $204bn, $27.5/share** (was $30.75). Funding commitments $13.0bn, $12.0bn funded `[F]`. Base holds it flat to exit; Bear −50%, Bull +50% |
| FX | **Re-mark 7 Nov:** USD/NOK **9.4665** (Yahoo `NOK=X`, 15-min bar 21:00 UTC, 6 Nov; Norges Bank fixing 6 Nov 9.4277 `[F]`), on the Equity BBB NOK path of 6 Nov (spot 9.29 there; relative moves +12% / +9% / +9%, flat, −3% unchanged). I-44 **108.79** (6 Nov) is 1.1% stronger than Norges Bank's 110.0, inside the 3% tolerance: Base spot flat. Version 3: USD reporting and USD price: no conversion. NOK path (Equity BBB) at USD/NOK **9.2540** (Yahoo `NOK=X`, 15-min bar 20:00 UTC, 28 Oct; Norges Bank fixing 28 Oct 9.2944 at 14:15 CET, the gap is the intraday move; 9.4749 on 15 Oct), moved with the Equity BBB relative path (Bear +12% / +9% / +9%, Base flat, Bull −3%). I-44 107.06 (28 Oct) is 2.7% stronger than Norges Bank's 110.0, inside Equity BBB's 3% tolerance, so Base stays spot flat |
| Track | **A (EPS, PE) deciding on a dated IRR to an independent exit P/E with a hurdle price P_k**, plus an FCF cross-check (iaf-valuation Step 2A). The AI BBB puts platforms on Track A "unless capex dominates FCF (then state it)": **it does** — Q1 FY27 FCF $18.6bn (OCF $58.0bn less PP&E $39.4bn) against non-GAAP net income $36.4bn (51%), and $5.7bn after component prepayments. Earnings are not rate-driven (no mid-cycle reversion), so EPS stays the value metric; capex enters through FCF, net cash and the growth-capex test (Step 4) |
| k | **12%**, not raised: AAA, net cash, deep liquidity (~$13bn traded a day). OpenAI concentration (10.8% of revenue) is a risk priced in Bear, not through k |
| Horizon | Stub Q4-26 (= Q2 FY27; 6 Nov–31 Dec at the re-mark, 28 Oct–31 Dec in v3) + 2027–2029 annual (calendar years); exit on 2030 forward EPS |

**Sources (connector · document · period):**
- **Re-mark 7 Nov:**
  - Yahoo `get_chart` (MSFT daily 27 Oct–6 Nov; `NOK=X` 15-min bars 6 Nov) and `quote_summary`
    (earningsTrend, calendarEvents, financialData, 7 Nov: Q4-26 EPS 4.86 (24 analysts), revenue
    $96.70bn (36); FY27 20.00 (32), FY28 24.18 (33); next report 27 Jan 2027 (estimate); ex-dividend
    19 Nov, paid 10 Dec; target mean $634.1 (54)).
  - Norges Bank API (USD fixing 2–6 Nov, I-44 4–6 Nov).
  - EDGAR filing list and documents: FWP 30 Oct, 424B2 29 Oct and 2 Nov, 8-K 4 Nov (notes), 8-K
    5 Nov (director).
- **SEC EDGAR** (direct; generic user agent): **8-K Ex. 99.1** (accession 0001193125-26-436122) and
  **10-Q** (0001193125-26-436133), both 28 Oct 2026, period to 30 Sep 2026 `[F]`: income statement,
  balance sheet, cash flow, segments (Agents and Infra; Devices and Consumer), product lines (Azure
  $33.17bn), RPO, leases, OpenAI related-party note, share count. A second 8-K of the same day
  (0001193125-26-436149) carries recast statements for the new segments; not read in detail `[?]`.
  The EDGAR filing list (`filings_list` equivalent) shows no share issue since 15 Oct (8-Ks, 10-Q,
  proxy material of 21 Oct, Form 4s).
- **Microsoft IR** FY27 Q1 metrics page `[F]`: Azure growth 48% (Q4 FY26 restated 42%), Microsoft
  Cloud $63.9bn and gross margin 66%, commercial RPO $677bn (Q4 FY26 $678bn), bookings −12%, M365
  commercial seats +5%.
- **Earnings call (28 Oct, 21:30 UTC)** `[E]`: read through third-party transcripts (TradingKey
  quotes of Amy Hood; Motley Fool transcript page, 29 Oct); Microsoft's own transcript not read.
  Q2 FY27 guidance, Q1 capex $45.2bn incl. $7.4bn finance leases, calendar-2026 capex ~$170bn,
  capacity, bookings, Copilot, financing (see Outlook).
- **FinancialFilings:** not used (quota exhausted in version 1); EDGAR was read directly instead.
- **Yahoo** (28 Oct 2026): price, after-hours price, USD/NOK, `earningsTrend` (before the report:
  Q3-26 EPS 4.72 / revenue 90.74bn, 25 / 38 analysts; Q4-26 4.82 / 95.65bn, 25 / 37; FY27 19.76
  (34); FY28 23.69 (33)), `calendarEvents` (ex-dividend 19 Nov; payment 10 Dec), `financialData`
  (target mean $605.1, 53 analysts).
- **Norges Bank API** (28 Oct): USD fixing 9.2944, I-44 107.06 `[F]`.
- **Zacks** (28 Oct): fiscal-YTD cash flow (Q2 FY26 OCF $35.8bn, PP&E $29.9bn, used for the stub),
  profile (target average $597.05; ABR 1.29 from 52 brokers) `[E]`.
- **Web `[E]`:** Q1 FY27 guidance as given in July (revenue $89.85–90.95bn, Azure 44–45% cc, capex
  "> $50bn" incl. finance leases, operating margin about flat y/y; FY27 operating margin "down
  less than one point", capex to grow, FCF positive; FY26 Azure $101.94bn) — financefeeds, CFO
  Dive, MarketBeat summaries; Visible Alpha Azure estimate $32.84bn and the after-hours move
  (Investing.com/Reuters, 28 Oct); OpenAI's $852bn valuation (Aug-2026 secondary, dealroom).
- **Sector:** `docs/ai-market-bbb.md` (24 Oct 2026; re-mark: Update 7 of 7 Nov);
  `docs/equity-market-bbb.md` (17/18 Oct 2026; re-mark: Update 2 of 6 Nov); `docs/hy-market-bbb.md`
  (24 Oct 2026; re-mark: 5 Nov).

## Scenario definitions (from AI Market BBB and Equity Market BBB)

| Scenario | Catalyst | What it does to Microsoft |
|---|---|---|
| **Base** (decision) | Contracted 2027 build, then digestion; the equity Base (AI boom slows to trend) | Azure follows the E2 Base row: +38% / +25% / +18% (2027–29) from a CY26 base of $124.8bn (Q3-26 +48%, Q4-26 guided +49–50%). Productivity grows ~10% (T3 +8/7/7% plus half the Copilot seat uplift from T1: 60 / 95 / 130m seats). Operating margin 45.5% → 45% as depreciation catches up with capex. EPS +11% a year; exit P/E 23 |
| **Bear** (stress) | **Financing break** (a lab — for Microsoft, OpenAI, $10.0bn of Q1 FY27 revenue — falls short of commitments; neoclouds renegotiate; AI credit tightens) inside the equity Bear (recession H1 2027 + oil Bear). Earliest H1 2027 | Azure +25% in 2027 (contracted) then +8%; Productivity +3.5 / +1 / +3.5%; PCs and gaming −6% in 2027. Margin 43% → 41% (2028) as depreciation on 2026–27 capacity meets slower revenue. Capex cut to $150bn from 2028. OpenAI stake −50%. P/E 18 from end-2027. EPS flat 2027–29 |
| **Bull** (stress) | **Agentic adoption** (lab revenue +130% in 2027, capex to $1.3–1.7tn) inside the equity Bull (soft landing). Earliest Q2 2027 | Azure +45% / +32% / +22%; Productivity +14–15% (Copilot 80 / 140 / 200m seats); margin holds 46.5%; capex $240–300bn; OpenAI +50%. Exit P/E 26 |

The stub (28 Oct–31 Dec 2026) is the same in all scenarios: Q4-26 guidance and consensus, the
declared dividend, price flat by convention. Bear and Bull diverge from 1 Jan 2027.

## Company and status

- **New reporting structure from FY27** `[F]`: two segments, **Agents and Infra** ($76.8bn in Q1,
  +25%, operating income $40.6bn) and **Devices and Consumer** ($15.5bn, −3%, operating income
  $5.4bn); prior periods recast. Product lines Q1 FY27 (y/y) `[F]`:

| Product line | Q1 FY27 $bn | Q1 FY26 $bn | Growth |
|---|---|---|---|
| Azure | 33.17 | 22.38 | +48% (cc +48%) |
| Microsoft 365 cloud | 27.78 | 23.69 | +17% |
| Productivity and server licensing | 8.41 | 8.68 | −3% |
| Search and advertising | 6.55 | 5.94 | +10% (ex TAC +12%) |
| XBOX | 5.38 | 5.51 | −2% |
| Industry solutions | 5.34 | 4.89 | +9% (cloud +10%) |
| Windows OEM and devices | 3.55 | 4.55 | −22% (Windows OEM alone −27% `[E]`, call) |
| Frontier and support services | 2.11 | 2.02 | +4% |
| **Total** | **92.28** | **77.67** | **+19%** |

- **Q1 FY27 against the model (v2) and guidance** (this is the actual for the stub quarter Q3-26):

| | Model / guide | Actual | Gap | Tag |
|---|---|---|---|---|
| Revenue $bn | 90.69 (consensus used in v2); guide 89.85–90.95 | **92.28** | +1.8% | `[F]` |
| Azure $bn / growth | ~31.3 / ~45% cc (guide 44–45%; Visible Alpha $32.84bn) | **33.17 / +48%** (Q4 FY26 restated +42%) | +6% | `[F]` |
| Operating income / margin | margin about flat y/y (guide; Q1 FY26 48.9%) | **45.9 / 49.8%** | +0.9 pp y/y | `[F]` |
| Non-GAAP EPS (GAAP) | 4.72 (25 analysts) | **4.89** (4.92) | +3.6% | `[F]` |
| Tax rate / other income ex OpenAI | ~20% / ≈ −$0.1bn (guide) | 20.3% / −$0.23bn (OpenAI gains $0.27bn pre-tax) | in line | `[F]` |
| Capex incl. finance leases / PP&E paid | "> $50bn" incl. finance leases (guide `[E]`) | **45.2** incl. $7.4bn finance leases `[E]` (call) / **39.4** `[F]`; plus $6.5bn of operating-lease right-of-use assets `[F]` | below the guide: third-party capacity deliveries slipped into H2 | `[F]`/`[E]` |
| FCF (OCF − PP&E) | ≈ dividends + buybacks `[A]` | **18.6** (OCF 58.0); **5.7** after other investing of −$12.9bn, "primarily to facilitate the purchase of components" | | `[F]` |
| Cash returned | ≈ $11bn | $11.1bn cash (dividends 6.8, buybacks 4.4); "$10.2bn returned" on a declared basis | in line | `[F]` |
| Net cash at 30 Sep $bn | ≈ 36.5 `[A]` | **29.0** | −7.5 | `[F]` |
| Commercial RPO $bn | rising (v2 signpost) | **677** (+73% y/y; 678 at 30 Jun); ~30% within 12 months; bookings −12% y/y ("large Azure commitments in the prior year", call `[E]`) | flat q/q | `[F]` |
| Depreciation / D&A and other $bn | — | 11.1 / 11.7 (Q1 FY26 7.1 / 8.1) after the building-life change | | `[F]` |

- **AI and backlog** `[F]`: Microsoft Cloud $63.9bn (+30%), gross margin 66% ("sales mix shift to
  Azure, offset in part by product-level margin improvements, primarily in Azure"). Commercial
  RPO $677bn with a weighted average duration of ~2.3 years; total RPO $683bn. On the call
  "customer demand continues to exceed available supply", with some third-party capacity
  "delayed to H2" `[E]`. M365 commercial seats +5% (from +7%); "weaker sales execution" in M365 E3
  and stand-alone SKUs `[E]`. No new M365 Copilot seat count: premium seats (M365 Copilot, E5, E7)
  have "reached millions of paid seats" `[E]` (> 30m Copilot seats in July `[E]`).
- **OpenAI** `[F]` (10-Q): ~24% as-converted interest; **revenue from OpenAI incl. revenue-sharing
  $10.0bn in the quarter (10.8% of total)**; receivables from OpenAI $7.2bn (from $6.0bn);
  net gains $0.27bn pre-tax (excluded from non-GAAP). OpenAI's Azure commitment (Oct 2025) sits in
  RPO `[E]`. OpenAI models also entered private preview on Google Cloud (21 Oct) while Microsoft
  "remains its primary cloud partner" `[E]`. Microsoft also holds a stake in Anthropic (~$2/share
  `[?]`, not modelled).
- **Capex and leases** `[F]`: PP&E paid $39.4bn (Q1 FY26 $19.4bn); finance leases $7.4bn on the
  call's basis `[E]` ($5.2bn of finance-lease assets obtained in the 10-Q; the definitions differ
  `[?]`); operating-lease assets obtained $6.5bn; about three-quarters of capex on short-lived
  assets `[E]`; net PP&E $346.8bn (from $313.1bn). Finance-lease liabilities $71.0bn (13-year
  average term, 4.5%); principal paid $1.0bn and interest $0.8bn in the quarter. Leases not yet
  commenced **$364.6bn** (+$35.5bn q/q). Building and datacenter lives raised from 15 to 25 years
  from FY27 (more new leases classify as operating leases; "a minimal benefit" to FY27 operating
  income `[E]`). Microsoft "will access additional sources of funding when we believe it is
  attractive", leasing so far and debt "not yet" tapped `[E]`.
- **Capital returns** `[F]`: quarterly dividend **$0.98** (+7.7%), ex-date 19 Nov, paid 10 Dec
  2026 — the share is not yet ex-dividend, so it counts. $37.7bn left of the $60bn buyback
  programme.

### Outlook

| Item | Q1 FY27: guidance (29 Jul) → outcome | Q2 FY27 (= Q4-26) guidance (28 Oct call `[E]`) |
|---|---|---|
| Revenue | $89.85–90.95bn → **$92.28bn** | **$96.0–97.1bn** (+18–19%); consensus before the report $95.65bn (37 analysts). Agents and Infra $80.1–80.7bn; Devices and Consumer $15.9–16.4bn |
| Azure (cc) | 44–45% → **48%** | **49–50%** |
| Other lines | — | M365 commercial cloud ~+19% cc; Windows OEM and devices down mid-30s % |
| Operating margin | about flat y/y → 49.8% (+0.9 pp) | "down slightly year-over-year"; FY27 "down less than one point" from 46.8% (July; no update on the call) |
| Other income ex OpenAI / tax | ≈ −$0.1bn → −$0.23bn / 20.3% | ≈ −$0.3bn / ~20% |
| Capex | "> $50bn" incl. finance leases → **$45.2bn** (third-party capacity delayed) | **> $50bn**; calendar 2026 **~$170bn** (was ~$175bn) "due to the 3P capacity delays", spending accelerating in H2 |
| FCF | positive in FY27 (July) → $18.6bn in Q1 | positive in FY27 (reiterated) |
| EPS | consensus 4.72 → **4.89** | not guided; consensus before the report 4.82 (25 analysts), in line with the guide (revenue $96.6bn × ~46.7% margin) `[A]` |

## Near term: stub (all scenarios)

| USD | Q3-26 (= Q1 FY27; **actual**) | Q4-26E (= Q2 FY27) | CY26E |
|---|---|---|---|
| Revenue $bn | **92.28** (model 90.69) | **96.55** (guide midpoint) | **361.7** (v2: 359.2) |
| Azure $bn | **33.17** (model ~31.3) | ~36.3 `[A]` (guide +49–50% on ~$24.3bn) | ~124.8 (v2: 121.1) |
| EPS (non-GAAP, ex OpenAI) | **4.89** (model 4.72) | 4.82 (consensus) | **18.72** (incl. Q1-26 4.27 and Q2-26 4.74) |
| Dividend paid | 0.91 (10 Sep) | **0.98 on 10 Dec** (ex 19 Nov) | |
| Net cash, period end $bn | **29.0** (model ≈ 36.5) | ≈ **19** `[A]` | |

- **Net cash to 31 Dec** `[A]`: $29.0bn + FCF ~$3bn (OCF ~$45bn, +25% on Q2 FY26's $35.8bn, less
  PP&E ~$42bn of the "> $50bn" capex) − dividends $7.3bn − buybacks $4.4bn − finance-lease principal
  $1.1bn ≈ **$19bn** ($2.56/share). No further component prepayments are assumed; another $10bn
  quarter would take it to ~$9bn (−$1.3/share, −0.05 pp).
- **Q2 FY27 report** (late January 2027, date `[?]`): Azure against the 49–50% guide and the E2
  row's slowdown, RPO (does it grow again q/q?), capex incl. finance leases and the FY27 figure,
  OpenAI's revenue share, Copilot seats.
- Next dividend dates (assumed `[A]`): ~10 Mar, 10 Jun, 10 Sep 2027; the December dividend is raised
  each year (Base +9%).

## Market input (AI Market BBB rows used and how they enter)

| Microsoft block (CY26 $bn `[A]`, calibrated to CY26 revenue $361.7bn) | AI BBB row | Bear / **Base** / Bull 2027 · 2028 · 2029 | Company adjustment |
|---|---|---|---|
| **Azure** (124.8; Q2-26 $29.4bn, Q3-26 $33.2bn actual, Q4-26 ~$36.3bn guided) | **E2** hyperscaler cloud growth | +25 / **+38** / +45 · +8 / **+25** / +32 · +8 / **+18** / +22% (unchanged since 12 Oct) | None: Azure grows at the row. Q3-26's 48% and the Q2 guide of 49–50% (accelerating from 42%) run ahead of the row's implied slowdown, but RPO did not grow q/q, bookings fell 12% and OpenAI is ~11% of revenue: no backlog support for a premium (Google Cloud's +12 pp rests on a backlog 5.2× run-rate). Tested as a sensitivity (+5 pp → 12.3%). 2030: +8 / +12 / +15% `[A]` |
| **Productivity and Business Processes** (145.3) | **T3** incumbent software + **T1** Copilot seats | T3: +3 / **+8** / +11 · 0 / **+7** / +11 · +3 / **+7** / +10%; T1 seats 45 / **60** / 80 · 55 / **95** / 140 · 65 / **130** / 200m (unchanged) | T3 plus **half** the Copilot uplift (seat adds × ~$240 a year net price `[A]`) → **+3.5 / +10 / +14 · +1 / +10 / +15 · +3.5 / +9 / +14%**. M365 commercial cloud grew 17% (18% cc) in Q3-26 and is guided ~19% cc, on seat growth of only 5% |
| Other Intelligent Cloud (servers, services; 38.4) | — (no row) | 0 / **+3** / +4% a year `[A]` | Server products follow cloud migration (productivity and server licensing −3% in Q3-26) |
| More Personal Computing (53.2) | — (equity BBB macro) | −6 / **+2** / +4% in 2027, then 0–2 / **+2** / +4% `[A]` | Windows OEM −27% in Q3-26 and guided down mid-30s % in Q4-26 (PC demand, memory costs): +2% looks generous; the block is 13% of revenue (−1 pp on it ≈ −0.02 pp IRR) |
| **Capex** (CY26 ~170 incl. finance leases, guided `[E]`) | **K1** (5 hyperscalers 790 → 950 / **1,120** / 1,300 in 2027; unchanged) | 200 / **210** / 240 · 150 / **225** / 280 · 150 / **230** / 300 (incl. finance leases; cash capex = 85%) `[A]` | Microsoft grows capex less than K1 (Base CY27 +24% on ~170 vs K1 +42%) because new capacity moves to operating leases ($365bn not commenced) and third-party contracts; its share of K1 falls from ~22% to 19% |

- **Revenue against consensus:** Base CY27 $425.9bn vs consensus CY27 ≈ $430.1bn (−1.0%; before
  the report); Base CY28 $487.2bn. Consensus FY28 (+19.7%) needs Azure near the Bull row.
- **E-layer consistency:** on the AI BBB's E-layer EPS path (0.97 / 1.07 / 1.17 / 1.27 × CY27
  consensus 21.72) with its Base exit P/E 21 and this analysis's own net cash and dividends,
  Microsoft returns **5.7%**; at exit P/E 23 **8.6%**; this Base **9.5%**. The differences are named:
  EPS ~3% above the layer path by 2030 (0.96 / 1.08 / 1.20 / 1.31; gap −0.01 in 2027, +0.04 by
  2030, below the AI BBB's 0.05 rule) and the exit P/E premium (23 vs 21, worth +2.8 pp). On the
  AI BBB's own method (layer cash conversion −.20 / .00 / .20) Microsoft gives 3.3% at $524.51
  (23 Oct); that conversion is the basket's, and Microsoft's own is .19 / .31 / .42 in this Base.
  The E basket's Base is 6.9% (NOK, 23 Oct prices; was 6.1% at 15 Oct).

## Common assumptions

- **EPS basis:** non-GAAP, excluding OpenAI equity-method results and other investment gains; tax
  20% (Q3-26 20.3% `[F]`; Q2 guide ~20% `[E]`); other income −$1.0 / −2.0 / −2.5 / −3.0bn for
  2027–30 (finance-lease interest $0.77bn in Q3-26 `[F]`; Q2 guide −$0.3bn) `[A]`. The OpenAI stake
  is valued separately (Header).
- **Operating margin** `[A]` (unchanged): Base 45.5% (2027) → 45.0%; Bear 43 / 41 / 42 / 43%; Bull
  46.5%. Q3-26's 49.8% is the seasonal high quarter (Q1 FY26 48.9%, FY26 46.8%); Q2 is guided "down
  slightly" y/y and FY27 "down less than one point" (July), which puts FY27 near 46%, so Base 2027
  sits ~0.5–1 pp below the company and ~1–1.5 pp below consensus. D&A rises from $47bn a year
  (Q3-26 run-rate `[F]`) to $72 / 90 / 102bn in Base, which needs D&A up ~$1.5bn a quarter:
  consistent with $45–50bn of quarterly capex, three-quarters on short-lived assets `[A]`. A +1 pp
  margin every year is worth +0.8 pp (sensitivities).
- **Cash returns:** dividends paid quarterly, raised each December (Bear +5%, Base +9%, Bull +10%).
  Buybacks $10 / 22 / 30bn a year offset stock-based dilution: shares held flat, buyback cash
  deducted from net cash. **D_t = dividends only** (no double count).
- **FCF** = net income + D&A + SBC ($14–16bn) − $5bn other − cash capex (85% of capex incl. finance
  leases) − **finance-lease principal $5.0 / 6.5 / 8.0bn** (new in version 3: $1.0bn in Q3-26 on
  $71bn of liabilities `[F]`; version 2 left the 15% non-cash part of capex unpaid in the window).
  Component prepayments are timing (they turn into PP&E) and are not modelled after Q3-26.
  Retained FCF after dividends and buybacks accumulates as net cash and enters V_T once.
- **Exit:** V_T = exit P/E × 2030 EPS + OpenAI stake at the scenario mark + net cash at exit.
  **Exit P/E Bear 18 / Base 23 / Bull 26** `[A]`, set independently of the IAF ceiling (Step 2A,
  exit principle in Step 3: the market price of a continuing business at the market's return at
  exit, never k):
  - Own history: forward P/S over 5 years 6.9–14.0x, median 10.4x (Zacks 30 Sep `[C]`); at ~36% net
    margin a P/E of ~19 / 29 / 39.
  - AI BBB E layer: 17 / 21 / 23.5. Equity BBB World: 15 / 17 / 18.5.
  - Base 23 = **+35% to World's 17** and +10% to the E layer, for growth at exit (2030 EPS +8.7%
    against World's 5.3% long-run), margin (45% operating) and ROE (~23% on exit book against
    World's 18.5%); below the 5-year median because growth at exit is below 2021–26 (15–18%) and
    FCF conversion (~40–50% of net income in 2029–30) is below its history.
  - Bear 18 ≈ the low end of the 5-year range, reached at end-2027 (as in the AI BBB). Bull 26 ≈
    today's headline multiple held.
- **Interim V_t:** price flat at end-2026 (all scenarios); core P/E glides linearly from 24.1 (today,
  on Base CY27) to the exit P/E (Base 23.7 / 23.4 / 23.0; Bull 24.7 / 25.4 / 26.0; Bear at 18 from
  end-2027); the OpenAI stake glides to its exit mark.

## Period tables and year-end path

**Base** (USD bn unless stated)

| | 2027 | 2028 | 2029 | 2030 (exit EPS) |
|---|---|---|---|---|
| Azure | 172.2 | 215.2 | 254.0 | 284.4 |
| Productivity and Business Processes | 159.8 | 175.8 | 191.6 | 207.0 |
| Other Intelligent Cloud / More Personal Computing | 39.6 / 54.3 | 40.8 / 55.4 | 42.0 / 56.5 | 43.2 / 57.6 |
| **Revenue** (growth) | **425.9** (+17.7%) | **487.2** (+14.4%) | **544.1** (+11.7%) | 592.3 (+8.9%) |
| Operating income (margin) | 193.8 (45.5%) | 219.2 (45.0%) | 244.8 (45.0%) | 266.5 (45.0%) |
| Net income | 154.2 | 173.8 | 193.9 | 210.8 |
| **EPS** (vs CY27 consensus 21.72) | **20.77** (0.96) | **23.40** (1.08) | **26.11** (1.20) | **28.39** (1.31) |
| Capex incl. finance leases / cash capex | 210 / 178.5 | 225 / 191.3 | 230 / 195.5 | |
| OCF / finance-lease principal | 235.2 / 5.0 | 273.8 / 6.5 | 306.9 / 8.0 | |
| **FCF** $bn / per share | **51.7 / 6.96** | **76.0 / 10.24** | **103.4 / 13.92** | |
| Dividends paid $bn / per share | 29.8 / 4.01 | 32.4 / 4.37 | 35.4 / 4.76 | |
| Buybacks $bn | 22 | 22 | 22 | |
| **Net cash, year-end** $bn / per share | **19.0 / 2.55** | **40.6 / 5.46** | **86.6 / 11.66** | |

- Base FCF in CY27 ($52bn) is below FY26 ($67bn), while management expects FCF to stay positive
  in FY27 `[E]`. Q3-26 alone gave $18.6bn before component prepayments. The Base stays cautious
  here; FY27 FCF above $67bn remains a positive signpost.

**Bear** (lines that differ)

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Revenue (Azure) | 394.8 (156.0) | 408.8 (168.4) | 429.4 (181.9) | 452.0 (196.5) |
| Operating margin | 43.0% | 41.0% | 42.0% | 43.0% |
| EPS | 18.18 | 17.84 | 19.16 | 20.61 |
| Capex incl. finance leases / FCF $bn | 200 / 41.0 | 150 / 96.5 | 150 / 112.8 | |
| FCF / share | 5.52 | 12.99 | 15.18 | |
| Net cash $bn / share (buybacks $10bn; dividend +5%) | 20.5 / 2.77 | 76.1 / 10.24 | 146.3 / 19.71 | |

**Bull** (lines that differ)

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Revenue (Azure) | 441.9 (180.9) | 528.4 (238.8) | 611.6 (291.3) | 681.1 (335.0) |
| Operating margin | 46.5% | 46.5% | 46.5% | 46.5% |
| EPS | 22.03 | 26.26 | 30.37 | 33.80 |
| Capex incl. finance leases / FCF $bn | 240 / 38.6 | 280 / 55.5 | 300 / 85.5 | |
| FCF / share | 5.20 | 7.47 | 11.52 | |
| Net cash $bn / share (buybacks $30bn; dividend +10%) | −2.3 / −0.30 | −9.6 / −1.29 | 9.8 / 1.32 | |

**Year-end path** (D_t paid in the year; V_t at year-end; r_t in USD, NOK path in brackets;
re-mark 7 Nov at $530.61, valuation date 6 Nov; interim V_t re-glided from the core P/E of 24.10)

| | End-2026 (stub) | 2027 | 2028 | 2029 (exit) |
|---|---|---|---|---|
| Bear: D / V / core P/E | 0.98 / 530.6 / 24.1 | 3.97 / 337.7 / 18.0 | 4.17 / 368.8 / 18.0 | 4.38 / 404.5 / 18.0 |
| Bear: r_t / IRR to t | 0.2% / 1.2% | **−35.6% (NOK −27.9%)** / −31.8% | 10.5% / −14.7% | 10.9% / **−7.4%** |
| **Base: D / V / core P/E** | 0.98 / 530.6 / 24.1 | 4.01 / 585.4 / 23.7 | 4.37 / 643.1 / 23.4 | 4.76 / 692.1 / 23.0 |
| **Base: r_t / IRR to t** | 0.2% / 1.2% | **11.1%** / 9.8% | 10.6% / 10.2% | 8.4% / **9.6%** |
| Bull: D / V / core P/E | 0.98 / 530.6 / 24.1 | 4.02 / 681.3 / 24.7 | 4.42 / 805.8 / 25.4 | 4.86 / 921.4 / 26.0 |
| Bull: r_t / IRR to t | 0.2% / 1.2% | 29.2% (NOK 25.3%) / 25.2% | 18.9% / 22.2% | 15.0% / **19.9%** |

- No year in Base reaches 12%: the return is earnings growth (~10% a year) less a slow de-rating
  (−1.5% a year) plus a 0.8% dividend.

## V_T bridge (Base, per share), exit consistency and exit cross-check

| Step | $/share |
|---|---|
| P (6 Nov 2026 close; re-mark 7 Nov) | 530.61 |
| = core business (24.10 × Base CY27 EPS 20.77) | 500.52 |
| + OpenAI stake (24% × $852bn) | 27.53 |
| + net cash (31 Dec 2026E; 30 Sep actual $3.91) | 2.56 |
| Core: EPS growth to 2030 (20.77 → 28.39; **+10.4% a year** over T = 3.15) | +183.7 |
| Core: de-rating 24.10 → 23.0 (**−1.5% a year**) | −31.3 |
| = core at exit (23.0 × 28.39) | 652.9 |
| + OpenAI stake (held flat) | 27.53 |
| + net cash at exit (retained FCF after dividends, buybacks and finance-lease principal: +$67.6bn) | 11.66 |
| **= V_T** | **692.1** |

- g = (692.1 / 530.61)^(1/3.15) − 1 = **8.8% a year** = core value growth (EPS +10.4%, re-rating
  −1.5%) plus the net cash build. c = −0.0 pp. (Version 3 at $531.01 and T = 3.18: 8.7%.)
- Exit V_T: Bear 404.5 = 18 × 20.61 (371.0) + 13.8 (OpenAI −50%) + 19.7; Bull 921.4 = 26 × 33.80
  (878.8) + 41.3 + 1.3.
- **Exit consistency (Step 3):** earnings are not rate-driven, so there is no mid-cycle rate gap.
  The margin test: Year-3 margin vs the exit-year margin is 45.0 vs 45.0% (Base), 42.0 vs 43.0%
  (Bear, gap 2.4%), 46.5 vs 46.5% (Bull) — all below the 10% materiality limit. No reversion tail.
- **Backlog at exit:** not applicable as a separate line. Commercial RPO ($677bn, ~30% within 12
  months) is revenue already in the scenario paths, not a premium on asset marks.

**Exit cross-check against the equity market (Step 3; new in version 3)**

| | Bear | **Base** | Bull | World (Equity BBB) Bear / Base / Bull |
|---|---|---|---|---|
| Exit P/E on 2030 EPS: core / on all of V_T | 18.0 / 19.6 | **23.0 / 24.4** | 26.0 / 27.3 | 15.0 / **17.0** / 18.5 |
| Exit P/B (book $470.5bn at 30 Sep rolled forward with earnings less dividends and buybacks, plus SBC) | 3.6 | **5.7** | 7.3 | 2.47 / **3.17** / 3.74 (6 Nov; was 2.46 / 3.14 / 3.69) |
| ROE 2030 on exit book | 18.4% | **23.4%** | 26.7% | 16.4 / **18.5** / 19.9% |
| Cash conversion c 2029 (FCF less buybacks ÷ net income) | 0.72 | **0.42** (0.50 in 2030 at flat capex `[A]`) | 0.25 | 0.49 |
| Buyer's implied return: cash yield + World's long-run growth | 4.0 + 3.8 = **7.8%** | 2.2 + 5.3 = **7.5%** | 1.0 + 6.1 = **7.1%** | mid-cycle 7.1 / **8.2** / 8.7% |
| Same with Microsoft's own 2030 EPS growth | 4.0 + 7.6 = 11.6% | 2.2 + 8.7 = 10.9% | 1.0 + 11.3 = 12.3% | |

- **Reading:** the Bear exit gives a buyer more than World's Bear mid-cycle return (not generous).
  The Base and Bull exits give less than World's mid-cycle return on World's growth, and more on
  Microsoft's own. **The stated reason is growth** (2030 EPS +8.7% in Base, World 5.3%) with ROE
  ~23% (exit P/B 5.7 against World's 3.1; today's P/B is 8.4), the same reason the AI BBB gives for
  the E layer (buyer's return 6.3% on World's growth, 9.5% on its own).
- **Sensitivity at the index return:** an exit priced so a buyer earns World's 8.2% on World's
  growth (P/E ≈ 0.50 ÷ 2.9% ≈ 17, i.e. World's multiple) gives Base **0.3%** (P_k $376, margin of
  safety −29.2%; re-mark 7 Nov: 0.3%, $377, −29.0%). That is Microsoft priced like the average
  company in 2029; the exit P/E rows under Results bracket it.

## Growth capex test (Step 4)

| | Bear | Base | Bull |
|---|---|---|---|
| Cash capex 2027–29 $bn | 425 | 565 | 697 |
| less D&A 2027–29 (maintenance proxy) | 255 | 264 | 282 |
| **Growth capex** $bn (per share) | **170 (22.9)** | **301 (40.5)** | **415 (55.9)** |
| plus leases not yet commenced (all scenarios) | 365 | 365 | 365 |
| Operating income CY26 → 2030 $bn | 170 → 194 | 170 → 267 | 170 → 317 |
| After-tax increment $bn | +20 | +77 | +117 |
| **ROIC_g** = increment ÷ (growth capex + ~$100bn of FY26 capacity not yet earning) `[A]` | **~7%** | **~19%**; **~13%** incl. half the lease commitments | ~23%; ~17% incl. half the leases |
| vs k = 12% | **destroys value** | accretive, close to k once leases are counted | accretive |

- **Evidence for ROIC_g:** Azure growth of 48% (49–50% guided) on capacity added, group operating
  margin 49.8% in Q3-26 with depreciation +56% y/y, RPO of $677bn, demand above supply, and
  management calling returns per capex dollar "encouraging" `[E]`. Against it: RPO no longer
  growing q/q, leases not yet commenced up another $35.5bn to $365bn, $12.9bn of component
  prepayments in one quarter and OpenAI at 10.8% of revenue. **Growth is accretive in Base only if
  the leased capacity fills; in Bear the 2026–27 build earns below k.** This is the AI BBB's
  financing-break mechanism at company level.

## Results

Re-mark 7 Nov: $530.61 (6 Nov close), valuation date 6 Nov, T = 3.15. Version 3 values (28 Oct,
$531.01) are in brackets where they differ.

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (dated, USD) | −7.4% | **9.6%** (9.5%) | 19.9% (19.7%) |
| IRR_T in NOK on the Equity BBB NOK path | −4.8% | **9.6%** (9.5%) | 18.7% (18.5%) |
| Track A: Rule 1 screen d + g (EPS CAGR CY26→29; assumes today's P/E holds) | 0.8 + 0.8 = 1.6% | **0.8 + 11.7 = 12.6%** | 0.8 + 17.5 = 18.3% |
| d / g / c (dated build) | 0.8 / −8.3 / 0.1 | **0.8 / 8.8 / −0.0** | 0.8 / 19.1 / −0.1 |
| g: EPS growth / re-rating (core P/E 24.10 → exit) | −0.2% / −8.8% a year | **+10.4% / −1.5%** | +16.7% / +2.4% |
| Structural / cyclical | n/a (Track A; not rate-driven) — the split that matters is EPS growth vs re-rating above | | |
| ΣD_t / V_T | 13.49 / 404.5 | **14.12 / 692.1** | 14.28 / 921.4 |
| P_k / margin of safety | 294 / −44.6% | **495.9 / −6.5%** (494.5 / −6.9%) | 656 / +23.7% |
| Rule 3: P/E vs ceiling (d + g) / k² | 28.3 vs 1.1 | **28.3 vs 8.7 (fails)** | 28.3 vs 12.7 |
| P/FCF cross-check (CY27 / CY29 FCF) | 96.1 / 35.0 | **76.2 / 38.1** | 102.0 / 46.1 |
| Capital preserved? ΣD + V_T vs P | **No (−21%)** | Yes (+33%) | Yes (+76%) |

- **The Rule 1 screen passes only because it assumes today's P/E holds;** at 28x CY26 earnings that
  needs ~12% EPS growth for ever. With the exit P/E set independently (23), the dated IRR is 9.6%.
  Rule 3 says a 12% total return justifies a P/E below 9 over a 3-year horizon; Microsoft trades on
  a long-duration growth premium the 3-year window cannot pay for.
- **FCF:** P/FCF of 38–76x in Base. Microsoft's earnings are real, but during the build-out only
  about a fifth to two-fifths of them reach shareholders as free cash after buybacks, and Q3-26
  showed a new drain (component prepayments) on top of capex.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** 8.9% (28 Oct 8.8%). Not a
  decision figure.
- **Share of Bull already priced:** (530.6 − 495.9) / (656.4 − 495.9) = **22%** (28 Oct 23%; 15 Oct
  30%).
- **Bear balance sheet:** no survival question. Net cash rises to ~$146bn by 2029 because capex is
  cut; the dividend keeps growing (+5%). The loss is entirely multiple and earnings: the AAA
  balance sheet protects the company, not the share price.
- **E / R (HY rule, NOK; re-mark 7 Nov):**
  - E = 9.60 − 4.38 = **5.22 pp**. R = Base 2027 (11.1%) − Bear 2027 (−27.9%) = 39.0 pp.
    **E / R = 0.134** (28 Oct 0.131; 15 Oct 0.11).
  - That is above World (0.080 on 6 Nov, was 0.024) and the platforms basket (0.099, AI BBB 7 Nov).
    It is below the HY market reference, which is now **0.254** (5 Nov; 0.196 before, 0.216 with the
    Bear read as a shock).
  - **Price triggers:**
    - E / R = 0.254 at **$441.3 (−16.8%)**; at 0.216, $471.2; at 0.196, $486.2 (v3: $484.1).
    - Convention as in v3: the interim marks stay on today's glide while the trial price moves.
      Re-gliding them at each trial price instead gives $478.6 at 0.254.
    - Pre-alert (Base = the HY market's 7.2%): **$568.5 (+7.1%), crossed**. Base = k: $495.9.
- **Sensitivities (Base IRR / P_k / margin of safety):** the exit P/E rows are re-run at the
  7 Nov re-mark ($530.61, 6 Nov). The other rows are version 3 (28 Oct, $531.01). At the re-mark
  each of them moves with Base by about +0.1 pp of IRR and +$1.4 of P_k.

| Change | IRR | P_k | MoS |
|---|---|---|---|
| Exit P/E 20 | 5.2% | 436 | −17.8% |
| Exit P/E 21 (AI BBB E layer) | 6.7% | 456 | −14.0% |
| Exit P/E 26 | 13.7% | 556 | +4.7% |
| Exit P/E 29 (5-year median P/S equivalent) | 17.4% | 615 | +15.9% |
| **Break-even exit P/E** | **12.0% at ~24.8** (24.75) | 530.6 | 0% |
| Exit at a buyer's World return (P/E ≈ 17) | 0.3% | 377 | −29.0% |
| **Price $555.80** (4 Nov close, the high of the window) | 8.0% | 496 | −10.8% |
| Operating margin −1 pp / +1 pp every year | 8.7% / 10.3% | 483 / 506 | −9.0% / −4.7% |
| Azure growth −5 pp / +5 pp every year | 6.9% / 12.3% | 459 / 535 | −13.6% / +0.7% |
| OpenAI stake to zero / doubled | 8.1% / 10.8% | 475 / 514 | −10.5% / −3.3% |
| Capex +$20bn a year | 9.2% | 490 | −7.8% |
| No finance-lease principal (version 2 cash convention) | 9.6% | 496 | −6.5% |
| After-hours price $544.18 (28 Oct, 21:04 UTC, before the call; v3) | 8.6% | 494 | −9.1% |
| After-hours $554.68 (28 Oct, Investing.com, later; v3) | 8.0% | 494 | −10.8% |
| $25bn notes of 4 Nov: net carry ≈ −$0.3bn a year after tax (not applied) | ≈ −0.02 pp | ≈ −0.6 | ≈ −0.1 pp |
| AI BBB E-layer EPS path, exit P/E 21 / 23 | 5.7% / 8.6% | | |
| EPS growth 2028–30 needed for 12% (exit P/E 23) | 13.9% a year (Base 11.0%) | | |

## Verdict and caveat

- **Fails: Base margin of safety −6.5%** (below the −2% line; re-mark 7 Nov at $530.61; 28 Oct
  −6.9%). Base IRR 9.6% against k = 12%.
- **Does not survive Bear:** −7.4% a year and a 21% capital loss over the window, driven by a
  re-rating to 18x and flat EPS 2027–29 if the AI financing break hits Microsoft's OpenAI revenue
  ($10bn a quarter) and Azure growth drops to single digits.
- **What would flip it:** an exit P/E of ≥ 24.8 (the market keeps paying close to today's
  multiple), Azure holding 5 pp a year above the AI BBB E2 Base (marginal, ~+1%), or a price at
  or below **$495.9** (Base meets k). E / R meets the HY reference (now 0.254) only at
  **$441.3**. The HY reference rose, so the two triggers are now far apart ($484–494 on 28 Oct). Microsoft is the closest
  of the analysed platforms to clearing because its earnings growth is real and broad; the gap is
  the entry multiple, not the business.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation or a price target. Returns are
  before fund fees and tax; NOK returns are on the Equity BBB NOK path, beside the spot decision.

## Tracking

| Version | Date | Price | Base IRR | P_k | MoS | What changed |
|---|---|---|---|---|---|---|
| 1 | 12 Oct 2026 | $540.53 | 8.7% | 492.0 | −9.0% | Initial analysis |
| 2 | 15 Oct 2026 | $540.26 | 8.8% | 492.4 | −8.9% | AI BBB Update 1 (paths unchanged); price and valuation date; no new company report |
| **3** | **28 Oct 2026** | **$531.01** | **9.5%** | **494.5** | **−6.9%** | Q1 FY27 report and call; iaf-valuation 2026-10-18.2; AI BBB Updates 2–4 and Equity BBB 17/18 Oct (rows used unchanged); price and date |
| 3, re-mark | 7 Nov 2026 (6 Nov close) | $530.61 | **9.6%** | **495.9** | **−6.5%** | Price and date; iaf-valuation 2026-11-01.1; AI BBB Update 7, Equity BBB 6 Nov, HY BBB 5 Nov (rows used unchanged; HY reference 0.196 → 0.254 moves the E / R trigger to $441.3); $25bn notes (net cash unchanged) |

- **Actual vs model for Q3-26 (= Q1 FY27)** (table under Company and status):
  - **EPS** $4.89 vs $4.72 (+3.6%); revenue $92.3bn vs $90.7bn (+1.8%); Azure $33.2bn (+48%) vs
    ~$31.3bn.
  - **FCF** $18.6bn, but $5.7bn after $12.9bn of component prepayments; **dividend** $0.91 paid as
    modelled, $0.98 declared for December; **net cash** $29.0bn vs ≈ $36.5bn modelled (−$7.5bn,
    −$1.0/share).
  - **Backlog:** commercial RPO $677bn vs $678bn at 30 Jun (flat; v2 implied growth).
  - **Guidance:** Q2 revenue $96.0–97.1bn (midpoint $0.9bn above consensus), Azure 49–50%;
    calendar-2026 capex ~$170bn (from ~$175bn).
- **Change in Base P_k:** 492.4 → 492.5 from the report and call (at the 15 Oct price and date),
  → 494.5 at 28 Oct (the later valuation date). Split of the Base IRR change: see "Change since
  15 Oct" in the Summary.
- **Running ahead of or behind Base:** **ahead on revenue, Azure and margin; behind on backlog,
  capex delivery and cash.** For the decision the two net out (+0.0 pp). The quarter does not move
  any input row.
- **Against the AI BBB rows (for its next run, after Amazon's report on 29 Oct):**
  - **E2 (Azure): ahead.** Azure +48% in Q3-26 and **49–50% guided for Q4-26**, accelerating from
    42% (restated), with demand still above supply; CY26 Azure ~+45%. The E2 path implies a
    slowdown from ~+50% (2026 blend) to +38% (2027); Microsoft is moving the other way into 2027.
    Kept at the row here because the backlog did not grow.
  - **K4 (backlog): behind.** Commercial RPO flat q/q ($678bn → $677bn), +73% y/y (from +84%),
    bookings −12% y/y (prior-year Azure commitments), ~30% within 12 months. The K4 total (~$2.35tn)
    and the "2027 largely contracted" reading rest on growing backlogs.
  - **K1 (capex): below Microsoft's own guide, not below the row.** Q3-26 capex $45.2bn incl. $7.4bn
    finance leases against "> $50bn" guided, as third-party capacity slipped; Q4-26 "> $50bn";
    **calendar 2026 ~$170bn** (K1 assumes ~175 for Microsoft). K1 2026 (790) moves < 1%; the slip
    shifts spend into H1 2027, which supports K1 2027.
  - **K3 (financing): new items.** Leases not yet commenced $329.1bn → **$364.6bn**; finance-lease
    liabilities $71.0bn; **$12.9bn of component prepayments** (a platform pre-financing its
    suppliers, the reverse of K3's vendor financing); $4.85bn of debt repaid; Hood: Microsoft "will
    access additional sources of funding when ... attractive" (leasing so far, debt "not yet").
  - **E1 (labs) ↔ E2:** OpenAI paid Microsoft **$10.0bn in the quarter** (incl. revenue share; 10.8%
    of revenue; receivables $7.2bn) `[F]` against OpenAI's ~$50bn run-rate `[E]`: a direct measure of
    lab spending inside E2 and of the financing-break channel. Stake ~24%, not ~27%.
  - **T1 / T3:** no Copilot seat count (premium seats "millions" `[E]`); M365 commercial cloud +17%
    (18% cc), ~19% cc guided, on seat growth of 5% (from 7%) and "weaker sales execution" in E3 —
    ahead of T3's +8% in value, with the seat compression T3 describes.
- **Equity Market BBB:** World Base 5.2% (was 6.1%), E / R 0.024; NOK firmer (USD/NOK 9.25, I-44
  107.1, 2.7% from Norges Bank's 110.0): a pending input for its update (stale after 10 Nov).
  Taken in by its Update 2 of 6 Nov (World 6.6%, E / R 0.080; I-44 107.76).
- **Re-mark 7 Nov (no new report):** running on the Base path. No quarter has closed since 30 Sep.
  The share has moved in a $507–556 band (2–4 Nov), and Base IRR is 11.2–8.0% across that band.
  At the 2 Nov close ($507.12) the margin of safety was −2.2%, just outside the marginal band.
  Consensus rose after the report: CY27 21.72 → 22.09 (+1.7%), and the Base 2027 EPS (20.77) is
  now 0.94 of it. Microsoft raised $25bn of debt on 29 Oct, the day after "not yet".

## Risks and signposts

| Signpost | Bear / Bull threshold | Now | Source |
|---|---|---|---|
| Azure growth (cc), quarterly | < 30% / > 45% | **48% (Q3-26) and 49–50% guided for Q4-26: Bull side crossed**; 42% (Q2-26, restated) | Microsoft `[F]`; call `[E]` |
| Commercial RPO and bookings | falls q/q or OpenAI share rising / > $800bn | **$677bn, −$1bn q/q: Bear side touched (flat)**; +73% y/y; bookings −12% y/y | Microsoft `[F]` |
| OpenAI share of revenue (new) | > 15%, or receivables rising faster than OpenAI revenue / share falling while Azure holds > 40% | 10.8% ($10.0bn); receivables $7.2bn (from $6.0bn) | 10-Q `[F]` |
| FY27 capex guidance vs FCF | capex up while FCF falls / FCF growth with capex ≥ $175bn | CY26 capex ~$170bn (third-party delays); Q3-26 $45.2bn; FCF $18.6bn ($5.7bn after component prepayments); FCF positive in FY27 | Microsoft `[F]`; call `[E]` |
| Component prepayments (new) | another quarter ≥ $10bn with RPO flat / reversing into capex | $12.9bn other investing in Q3-26 (+$6.7bn y/y) | 10-Q `[F]` |
| M365 Copilot paid seats (AI BBB T1) | < 45m mid-2027 / > 70m | > 30m (Jul); no update on 28 Oct (premium seats "millions") | Microsoft `[E]` |
| OpenAI funding (AI BBB K3) | missed commitments, down round / IPO above $852bn | $852bn (Mar round; Aug secondary at the same mark) | `[E]` |
| Operating margin (FY27) | < 44% / ≥ 46.5% | 49.8% in Q1 FY27 (seasonal high); Q2 "down slightly" y/y; FY27 "down < 1 pt" from 46.8% | Microsoft `[F]`/`[E]` |
| Core P/E on CY27 | ≤ 21 (k trigger region) / ≥ 27 | 22.7 on consensus (22.09), 24.1 on Base (7 Nov) | This analysis |
| **Price** | **≤ $495.9 (Base = k) and ≤ $441.3 (E / R = 0.254)**; pre-alert ≤ $568.5 (Base = HY market 7.2%) | **$530.61 (6 Nov close): pre-alert crossed**; $34.7 (6.5%) above Base = k; range since 28 Oct $507.12–555.80 | Yahoo `[F]` |
| Debt financing (new, 7 Nov; AI BBB K3) | further debt raised while RPO stays flat / debt used for buybacks | **$25.0bn of notes, 29 Oct (settled 4 Nov)**, Aaa / AAA, 2028–2066; gross debt ≈ $60.5bn; net cash unchanged | 8-K 4 Nov `[F]` |
| AI BBB Bear signposts | hyperscaler guides capex flat/down; Oracle BB+; capex/OCF > 100% with debt share > 40% | Microsoft: capex ~2x y/y, delayed not cut; PP&E paid ÷ OCF 68% | `docs/ai-market-bbb.md`; 8-K `[F]` |
| Lab financing and vendor financing (AI BBB) | OpenAI raise fails or down round; Anthropic IPO pulled or below USD 965bn / IPOs above those marks | Anthropic roadshow reported from 9 Nov, listing before 26 Nov | `docs/ai-market-bbb.md` |

- **Signposts after the Q1 FY27 report:** one crossed on each side. Azure (Bull side: 48% and
  49–50% guided) and RPO (Bear side, flat q/q). Neither is a scenario change: the Bull needs Azure
  at +45% for 2027 as a whole and the Bear needs a lab to fall short. The new OpenAI-share and
  component-prepayment rows track the Bear channel directly.
- **Other risks:** regulation (EU and US antitrust on bundling Copilot and Teams), price per token
  falling faster than usage grows (Epoch −47% a quarter `[E]`), the useful-life and lease changes
  making reported capex and margins less comparable, OpenAI using other clouds (Google Cloud
  preview, 21 Oct `[E]`), Windows OEM weakness (−27%, mid-30s % decline guided).
- **Next update:** after the Q2 FY27 report (late January 2027), the next AI BBB update (after
  Amazon's report on 29 Oct; stale after 8 Dec) or the Equity BBB update (stale after 10 Nov).
  **Re-mark 7 Nov:** next re-mark points are the ex-dividend date (19 Nov; the $0.98 then leaves
  the stub), NVIDIA's Q3 (17 Nov) through the AI BBB, the Anthropic IPO pricing (~20 Nov; Microsoft
  holds a stake, not modelled) and the Q2 FY27 report (27 Jan 2027, Yahoo estimate).

## For other modules

- **Re-mark 7 Nov: no block value changed.** EPS, D_t and V_T per scenario are unchanged. The
  interim V_t of Base and Bull re-glide to the new price by the analysis's own rule, which the
  reading documents apply themselves: Base 585.4 / 643.1, Bull 681.3 / 805.8.
  - Decision figure: Base 9.5% → 9.6% (date roll), P_k $494.5 → $495.9.
  - Triggers: Base = k $495.9; E / R = 0.254 $441.3; pre-alert $568.5.
  - **ai-market-bbb:**
    - **K3: Microsoft's $25.0bn bond** (29 Oct, settled 4 Nov; Aaa / AAA; ten tranches 2028–2066,
      fixed 4.85–6.35%, FRNs SOFR + 35 / + 53 bp) is not yet in K3. The call had said debt was
      "not yet" tapped.
    - Company check: 9.6% at $530.61 (P_k $495.9). The E MSFT row's "≈ −6.9%" is now −6.5%.
    - Update 7's appendix says USD/NOK "closed ~9.30 on 6 Nov". Yahoo's 21:00 UTC bar is 9.4665
      and Norges Bank's 6 Nov fixing is 9.4277. 9.29 is the Equity BBB spot (Norges Bank 5 Nov
      fixing 9.2984). It has no effect on the NOK-path IRRs, which use relative moves.
  - **equity-market-bbb, dnb-teknologi, global-index-funds:** no input beyond the price.
- **ai-market-bbb (24 Oct):** no row changed here; the hints for its next run are under Tracking
  (E2 ahead; K4 behind; K1 below guide, CY26 ~$170bn; K3 leases $364.6bn, component prepayments
  and the funding remark; OpenAI $10.0bn of Microsoft revenue; stake ~24%). Company check: Base
  9.5% at $531.01 (8.8% at $540.26), EPS 0.96 / 1.08 / 1.20 / 1.31 of CY27 consensus (gap to the E
  path −0.01 / +0.01 / +0.03 / +0.04, below the 0.05 rule); Bear .84 / .82 / .88 / .95 and Bull
  1.01 / 1.21 / 1.40 / 1.56 of CY27 consensus (v2 Bear .83 / .81 / .87 / .94); own cash conversion
  .19 / .31 / .42 (v2 .22 / .34 / .45).
- **equity-market-bbb and global index funds (company block in World):** EPS +0.9–1.2% per year
  (higher 2026 base), V_T about unchanged (Base 692.0 → 692.1; Bear 406.9 → 404.5; Bull 919.7 →
  921.4), D_t unchanged; Base 9.5% (was 8.8%) at a 1.7% lower price. Below any minimum-change
  rule; no re-run needed on these alone.
- **DNB Teknologi (company block):** same values as above.
- **Portfolio:** no action implied. On the user's rule (each switch must beat what it replaces),
  Microsoft at $531 does not beat the HY market on E / R (0.131 vs 0.196); at ≈ $484 it would match
  the HY market reference. A watch level, not a recommendation. **Re-mark 7 Nov:** at $530.61, E / R
  0.134 against the HY reference 0.254; it would match only at ≈ $441.

## Change log

- **7 Nov 2026 — price re-mark at the 6 Nov close; upstream re-read** (iaf-valuation 2026-11-01.1;
  AI BBB Update 7 of 7 Nov, ai-market-bbb 2026-11-06.1; Equity BBB Update 2 of 6 Nov,
  equity-market-bbb 2026-10-24.1; HY BBB of 5 Nov, hy-market-bbb 2026-10-24.1).
  - **Change gate:**
    - AI: E2, T1, T3 and K1 are unchanged.
    - Equity: scenarios and NOK relative moves unchanged; spot and the comparisons moved (World
      6.6%, E / R 0.080, exit P/B 3.17).
    - HY: NIBOR 4.38% unchanged; HY market Base 6.8% → 7.2%; reference 0.196 → 0.254. These set the
      E / R trigger, so this is a re-mark.
  - **Changed (previous → new):**
    - price $531.01 → $530.61; valuation date 28 Oct → 6 Nov (T 3.18 → 3.15); USD/NOK 9.2540 →
      9.4665; I-44 107.06 → 108.79;
    - Base 9.5% → **9.6%**, P_k $494.5 → **$495.9**, MoS −6.9% → **−6.5%**; Bear −7.4% (NOK
      −4.8%), unchanged; Bull 19.7% → 19.9% (NOK 18.5% → 18.7%);
    - E / R 0.131 → **0.134**;
    - triggers: Base = k $494.5 → **$495.9**; E / R $484.1 (0.196) → **$441.3 (0.254)**; new
      pre-alert (Base = 7.2%) **$568.5, crossed**;
    - interim V_t: Base 585.8 / 643.2 → 585.4 / 643.1, Bull 681.6 / 806.0 → 681.3 / 805.8;
    - exit P/E sensitivities re-run; the other sensitivity rows are labelled as v3.
  - **Added:**
    - the $25.0bn notes of 29 Oct / 4 Nov (net cash unchanged; carry ≈ −0.02 pp, not applied);
    - a debt-financing signpost;
    - the consensus of 7 Nov (CY27 22.09);
    - Yahoo's next report date (27 Jan 2027);
    - the pre-alert trigger.
  - **Kept:** EPS, D_t, V_T, every path and assumption, and the Q4-26 base (guide midpoint).
    **Verdict unchanged (fails).**
  - Reproduction check: the v3 build re-run at 28 Oct gives 9.49%, P_k $494.5, Bear −7.36%, Bull
    19.70% and E / R 0.131, the same as v3.
- **12 Oct 2026 — initial analysis** (iaf-valuation 2026-10-11.3; ai-market-bbb document
  12 Oct 2026; equity-market-bbb document 11 Oct 2026). No previous values.
- **15 Oct 2026 — version 2: update for AI Market BBB Update 1 (rev 2026-10-15.1) and a price
  refresh.** Equity Market BBB unchanged (11 Oct document). Changed: price $540.53 → $540.26,
  USD/NOK 9.5744 → 9.4749, valuation date 12 → 15 Oct (T 3.22 → 3.21), CY27 consensus 21.72 → 21.75.
  Base IRR 8.7% → **8.8%**, P_k 492.0 → 492.4, MoS −9.0% → **−8.9%**; Bear −7.6% (unchanged), Bull
  18.7% (unchanged); E / R 0.11 (unchanged). Corrected: Azure vs the E2 2026 row (now ~+50%); E basket
  comparison 5.7% → 6.1%; AI BBB stale date 26 → 29 Nov. Added: Tracking section, Anthropic
  commitment and stake memo, lab/vendor-financing signpost. **No assumption changed; verdict
  unchanged (fails).**
- **28 Oct 2026 — version 3: post-report update (Q1 FY27, quarter to 30 Sep 2026, and the call).**
  - **Method (iaf-valuation 2026-10-11.3 → 2026-10-18.2):** exit principle (V_T = market price of a
    continuing business at the market's return at exit, never k); Track A decides on a dated IRR
    to an independent exit P/E, with Rule 1 at constant P/E as a labelled screen; exit cross-check
    table added (exit P/E, exit P/B, buyer's implied return against World 17 / 3.14 / 8.2%, with
    the index-return sensitivity); the NOK memo is now the labelled "NOK path (Equity BBB)" for
    Bear and Bull, decision at spot. Backlog at exit and holdco G&A are Track B rules (not
    applicable). **No number changed by the method.**
  - **Inputs:** AI BBB Update 4 (24 Oct; rows E2, T1, T3, K1 unchanged; E basket 6.1% → 6.9%);
    Equity BBB 17/18 Oct (World 6.1% → 5.2%, E / R 0.063 → 0.024; NOK path relative moves and
    scenarios unchanged; exit references added); HY BBB 24 Oct (NIBOR 4.38%, reference 0.196,
    unchanged). **No number changed by the inputs.**
  - **Report and call:** Q3-26 actual replaces consensus (EPS 4.72 → 4.89; revenue 90.69 → 92.28;
    Azure ~31.3 → 33.17); Q4-26 revenue on the guide midpoint ($96.55bn) and Azure on the 49–50%
    guide (~$36.3bn); CY26 base 359.2 → 361.7 (Azure 121.1 → 124.8); shares 7,425.5m → 7,426.2m;
    OpenAI stake 26.8% → 24% ($30.75 → $27.53); net cash at 31 Dec $36.5bn → ~$19bn (30 Sep actual
    $29.0bn); finance-lease principal added to FCF ($5.0 / 6.5 / 8.0bn); leases not yet commenced
    $329.1bn → $364.6bn; CY26 capex ~$175bn → ~$170bn (context; the 2027–29 path is unchanged).
    Margin, capex path, exit P/E and scenario paths unchanged. Effect +0.0 pp.
  - **Price and date:** $540.26 → $531.01; 15 → 28 Oct (T 3.21 → 3.18); USD/NOK 9.4749 → 9.2540.
    Effect +0.7 pp.
  - **Result:** Base 8.8% → **9.5%**, P_k 492.4 → **494.5**, MoS −8.9% → **−6.9%**; Bear −7.6% →
    −7.4% (NOK −5.0% → −4.8%); Bull 18.7% → 19.7% (NOK 17.6% → 18.5%); E / R 0.11 → 0.131;
    triggers ≈ $494 (k) and ≈ $484 (E / R). **Verdict unchanged (fails).**
  - **Added:** product-line table, actual-vs-model table, Q2 FY27 outlook, exit cross-check,
    OpenAI-share and component-prepayment signposts, after-hours sensitivity.

## Appendix: own assumptions `[A]`

| Item | Bear | Base | Bull | Basis |
|---|---|---|---|---|
| CY26 blocks $bn: Azure / P&BP / other IC / MPC | 124.8 / 145.3 / 38.4 / 53.2 | same | same | Azure: version 2 build with Q3-26 actual ($33.17bn) and Q4-26 ~$36.3bn (guide +49–50% on ~$24.3bn); the rest scaled to CY26 revenue $361.7bn (three actual quarters + the Q4-26 guide midpoint $96.55bn) |
| Azure growth 2027 / 28 / 29 / 30 | 25 / 8 / 8 / 8% | 38 / 25 / 18 / 12% | 45 / 32 / 22 / 15% | AI BBB E2 row; 2030 fade own |
| P&BP growth | 3.5 / 1 / 3.5 / 4% | 10 / 10 / 9 / 8% | 14 / 15 / 14 / 10% | T3 + half of T1 seat adds × $240 |
| Other IC / MPC growth | 0–2% / −6% then 0–2% | 3% / 2% | 4% / 4% | Own |
| Operating margin 2027 / 28 / 29 / 30 | 43 / 41 / 42 / 43% | 45.5 / 45 / 45 / 45% | 46.5% | FY26 46.8%; Q3-26 49.8% (seasonal high); D&A step-up |
| D&A $bn 2027–29 | 72 / 88 / 95 | 72 / 90 / 102 | 75 / 95 / 112 | Q3-26 11.7 `[F]` (47 a year) + ~1.5 a quarter |
| Capex incl. finance leases $bn 2027–29 (cash = 85%) | 200 / 150 / 150 | 210 / 225 / 230 | 240 / 280 / 300 | K1 path; lease shift (Q3-26 PP&E paid $39.4bn of $45.2bn, 87%) |
| Finance-lease principal $bn 2027–29 | 5.0 / 6.5 / 8.0 | same | same | $1.0bn in Q3-26; liabilities $71.0bn, 13-year term `[F]` |
| SBC / other OCF items $bn | 14–16 / −5 | same | same | FY26 cash flow; Q3-26 SBC 3.1 `[F]` |
| Buybacks $bn a year / dividend growth | 10 / 5% | 22 / 9% | 30 / 10% | FY26 $22.3bn; Q3-26 $4.4bn; 24 years of raises |
| Net cash 31 Dec 2026 $bn | 19 | same | same | $29.0bn at 30 Sep `[F]` + Q4 FCF ~3 − dividends 7.3 − buybacks 4.4 − lease principal 1.1 |
| OpenAI stake (24% × $852bn = $27.5/share) at exit | −50% (from end-2027) | flat | +50% | 10-Q stake; Mar-2026 round, Aug-2026 secondary |
| Exit P/E (2030 EPS) | 18 (from end-2027) | 23 | 26 | 5-year P/S range; AI E layer 17 / 21 / 23.5; World 15 / 17 / 18.5 |
| Tax / other income | 20% / −1 to −3bn | same | same | Q3-26 tax 20.3% `[F]`; Q2 guide ~20% |

## Appendix: sources

| # | Source | Content | As of |
|---|---|---|---|
| S1 | [Microsoft 8-K Ex. 99.1, Q1 FY27 release](https://www.sec.gov/Archives/edgar/data/789019/000119312526436122/msft-ex99_1.htm) | Revenue, operating income, net income, EPS GAAP/non-GAAP, OpenAI impact, segments, product lines, balance sheet, cash flow, RPO, cash returned `[F]` | 28 Oct 2026 (period to 30 Sep 2026) |
| S2 | [Microsoft 10-Q, Q1 FY27](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm) | Shares 7,426,194,552 (22 Oct); OpenAI ~24%, revenue $10.0bn, receivables $7.2bn, commitments $13.0bn; RPO $683bn total / $677bn commercial, ~30% in 12 months; leases (finance $71.0bn, operating $27.5bn, not commenced $364.6bn); depreciation $11.1bn; other investing for components; buybacks `[F]` | 28 Oct 2026 |
| S3 | [Microsoft FY27 Q1 metrics](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/metrics) | Azure growth 48% (Q4 FY26 42% restated), Microsoft Cloud $63.9bn and gross margin 66%, RPO $677bn (Q4 FY26 $678bn), bookings −12%, M365 seats +5% `[F]` | 28 Oct 2026 |
| S4 | [TradingKey: FY2027 Q1 call](https://www.tradingkey.com/news/transcripts/262249601-tradingkey), [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/) | Q2 FY27 guidance (revenue $96.0–97.1bn, Azure 49–50% cc, segments, margin, other income, tax, capex > $50bn); Q1 capex $45.2bn incl. $7.4bn finance leases; calendar 2026 ~$170bn; Windows OEM −27%; bookings; Copilot; financing `[E]` | 28–29 Oct 2026 |
| S5 | Yahoo `get_quote`, `get_chart`, `quote_summary` (earningsTrend, calendarEvents, financialData) | Close $531.01 (20:00 UTC), after hours $544.18 (21:04 UTC), USD/NOK 9.2540 (20:00 UTC bar), consensus before the report, dates, target mean $605.1 (53) `[F]` | 28 Oct 2026 |
| S6 | Norges Bank API (`EXR/B.USD.NOK.SP`, `EXR/B.I44.NOK.SP`) | USD fixing 9.2944; I-44 107.06 `[F]` | 28 Oct 2026 |
| S7 | Zacks `compare_stocks` (QCF, profile) | Fiscal-YTD cash flow (Q2 FY26 OCF 35.8, PP&E 29.9); shares 7,426.4m; target average $597.05; ABR 1.29 (52) `[E]` | 28 Oct 2026 |
| S8 | [Investing.com: Microsoft stock after hours](https://www.investing.com/news/earnings/microsoft-stock-rises-over-4-after-hours-on-quarterly-results-beat-4980704), [Reuters via Investing.com](https://www.investing.com/news/stock-market-news/microsoft-beats-quarterly-cloud-revenue-estimates-4980616), [Investing.com: why the stock is surging](https://www.investing.com/news/stock-market-news/why-is-microsoft-stock-surging-today-93CH-4980849) | Visible Alpha Azure estimate $32.84bn; after hours +2.5% to +6% (up to $554.68); "capex significantly lower than expected" (Interactive Brokers) `[E]` | 28 Oct 2026 |
| S9 | [financefeeds preview](https://financefeeds.com/microsoft-stock-before-wednesdays-results-the-45-azure-guide-and-50-billion-capex-quarter/), [CFO Dive](https://www.cfodive.com/news/microsoft-holds-line-ai-spending-plans/826648/), [MarketBeat Q4 call highlights](https://www.marketbeat.com/instant-alerts/microsoft-q4-earnings-call-highlights-2026-07-29/) | Q1 FY27 guidance (revenue, Azure 44–45%, capex > $50bn, margin about flat); FY26 Azure $101.94bn, Q4 FY26 $29.42bn; FY27 margin "down < 1 pt", capex to grow, ~$175bn, FCF positive `[E]` | 29 Jul – 28 Oct 2026 |
| S10 | [dealroom: OpenAI secondary](https://dealroom.co/news/144253-openai-closes-7b-share-sale-at-852b-valuation-ahead-of-ipo/) | $7bn secondary at $852bn (Aug 2026) `[E]` | 11 Aug 2026 |
| S11 | Version 2 sources (Q4 FY26 release, Zacks report 30 Sep, broker ratings, OpenAI recapitalisation) | FY26 figures, P/S range, broker range `[C]` | 29 Jul – 12 Oct 2026 |
| S12 | `docs/ai-market-bbb.md`, `docs/equity-market-bbb.md`, `docs/hy-market-bbb.md` | Scenario rows, E-layer path and checks, NOK path, World exit references, NIBOR, HY reference | 17–24 Oct 2026; re-read 7 Nov (AI Update 7 of 7 Nov, Equity Update 2 of 6 Nov, HY 5 Nov) |
| S13 | [Microsoft FWP, pricing term sheet](https://www.sec.gov/Archives/edgar/data/789019/000119312526439794/d799291dfwp.htm), [8-K notes](https://www.sec.gov/Archives/edgar/data/789019/000119312526447173/d178557d8k.htm), [424B2 filing fees](https://www.sec.gov/Archives/edgar/data/789019/000119312526442618/d150456dexfilingfees.htm), [8-K director](https://www.sec.gov/Archives/edgar/data/789019/000119312526448357/d177209d8k.htm) | $25.0bn notes (ten tranches 2028–2066, $24.96bn offering amount), trade 29 Oct, settlement 4 Nov, Aaa / AAA; use of proceeds; Walmsley not standing for re-election `[F]` | 29 Oct – 5 Nov 2026 |
| S14 | Yahoo `get_chart` / `quote_summary`; Norges Bank API | MSFT close $530.61 (6 Nov, 21:00 UTC); USD/NOK 9.4665 (21:00 UTC bar); consensus 7 Nov (CY27 22.09); ex-dividend 19 Nov; fixing 9.4277; I-44 108.79 `[F]` | 6–7 Nov 2026 |

- **Not found / unverified `[?]`:** Microsoft's own call transcript (call figures are from
  third-party transcripts); the finance-lease basis ($7.4bn on the call vs $5.2bn of assets obtained
  in the 10-Q); Q2 FY26 and Q3 FY26 Azure under the new definition (CY26 Azure is approximate);
  the recast 8-K (0001193125-26-436149); OpenAI's share of RPO; the value of the Anthropic stake;
  a current M365 Copilot seat count.
- **Quality notes:** the Q1 FY26 comparatives are recast for the new segments. Zacks' cash flow is
  fiscal-YTD cumulative (Q2 FY26 = H1 − Q1). After-hours prints differ by source (+2.5% to +6%);
  the decision uses the regular close. "Windows OEM and devices" fell 22% (release); Windows OEM
  alone fell 27% (call).
