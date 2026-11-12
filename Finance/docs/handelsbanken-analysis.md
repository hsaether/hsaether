# Svenska Handelsbanken (SHB A) — IAF analysis, stub Q4 2026 + 2027–2029

**Version 3 — 24 Oct 2026**, after the Q3 2026 report (21 Oct) and the Equity Market BBB's
Update 1. Version 2: 15 Oct 2026; initial version 12 Oct.

Skill revisions used: **iaf-valuation 2026-10-18.2**. Versions 1 and 2 were built under
2026-10-11.3. What is new since then, and how it is applied here:
- Track A is decided on a dated IRR to an independent exit P/E. This analysis already did that.
- An **exit cross-check against the equity market** is added (exit P/E, exit P/B, the buyer's
  implied return, against Oslo).
- Bear and Bull are shown **in NOK on the Equity BBB path**. SEK is an "other currency", so it
  moves with I-44. Version 2 used its own SEK/NOK assumption, which is now a sensitivity.
- Backlog at exit, the reversion tail and holdco G&A do not apply to a bank on Track A.

Sector inputs:
- `docs/equity-market-bbb.md`: Update 1 of 17 Oct 2026, amended 18 Oct, read 24 Oct. Its 24 Oct
  change-log note only moves the source of the HY reference to `docs/hy-market-bbb.md`; no number
  changed. Version 2 read the initial baseline of 11 Oct.
  - Unchanged since 11 Oct:
    - the scenarios (Bear = recession H1 2027 + oil Bear; Base = higher-for-longer rates, earnings
      at trend; Bull = soft landing);
    - the Oslo financials block F ("rates and credit": DNB, Storebrand, Gjensidige), 0.98 / 0.96 /
      0.95 in Base;
    - the Oslo exit P/E (10.5 / 11.5 / 12.5);
    - the HY market reference E / R 0.196.
  - New or changed:
    - Oslo exit P/B 1.48 / 1.75 / 1.97 and mid-cycle return 8.2 / 9.1 / 9.4%;
    - index Base IRRs: Oslo 3.1 → 2.5%, World 6.1 → 5.2%;
    - I-44 spot 109.5 (relative Bear and Bull moves as before).
  - The HY book's E / R (0.291) is no longer in the equity baseline and is dropped here.
- `docs/hy-market-bbb.md`, version of 24 Oct 2026 (re-run on 17 and 24 Oct and kept unchanged;
  values as of 5 Oct). Used:
  - Sweden GDP 0.0 / 2.4 / 2.8 (2027) and LFS unemployment;
  - the Riksbank context: 1.75% held in September, hikes to ~2.4% signalled by Q3-27, **next
    decision 4 Nov**;
  - 3M NIBOR, window average 4.38%;
  - Swedish real-estate default context.
  No Riksbank or STIBOR path is set in any baseline, so the Swedish rate effect is still an own
  assumption `[A]`.
- The oil, shipping, rig, supply, defense and AI baselines are not used.

**Change gate.** The equity update alone moves no decision figure. Its scenarios, block F, Oslo
exit P/E and Base NOK path are unchanged. It adds the cross-check inputs, and the I-44 rule moves
only the Bear and Bull NOK figures.

The Q3 report does move the Base decision figures, through the capital return:
- the 9M anticipated dividend is SEK 8.02, 92% of profit (Q3 alone 113%);
- a new household PD model releases ~SEK 3bn of capital in Q4.

Result: Base IRR 8.1 → **8.9%**, P_k 136.7 → **138.3** (+1.2%), margin of safety −9.7 → **−7.7%**.
**The verdict (fails) and the trigger region (SEK 136–138) are unchanged.**

## Summary

**Verdict**
- **Fails (unchanged).** Base IRR **8.9% a year** in SEK against k = 12% (NOK the same in Base).
  - Hurdle price **P_k ≈ SEK 138 vs P SEK 149.85 (23 Oct close): margin of safety −7.7%** (−9.7%
    in version 2).
  - Track A screens fail: Rule 1 d + g = 7.3 + 4.5 = 11.8% < 12% (this assumes today's P/E
    holds); Rule 3 P/E 13.4 on CY26 excluding the VAT refund, against a ceiling of 8.2.
- **Q3 raised the capital return, not the earnings.**
  - The FY26 dividend is now modelled at **SEK ~12.05** (was 9.61): 9M accrual 8.02 `[F]`, 85% of
    Q4E profit, and SEK 1.52 a share from the PD-model release `[A]`.
  - Rebasing to actuals takes the EPS path down ~1.3%. Version 2 carried the one-off Q1 VAT refund
    in its "other income" base.
  - Q3 EPS was 2.87, 2.4% below consensus, and NII missed by 1.2%. The bank puts the q/q margin
    drop down to higher funding costs as Swedish market rates rose. The share fell 3.0% on the
    day.
- **The return is still almost all dividend:** cash yield 6.8% a year, value growth 1.7% a year.
  EPS grows ~3–4% a year after 2027. The price pays P/B 1.58 (on shareholders' equity) for an
  ROE of ~12.5–13%.
- **Bear breaks the thesis for a 3-year holder.** −5.4% a year in SEK, −3.4% in NOK on the
  Equity BBB I-44 path. The share falls ~33% in 2027 and capital is not preserved (ΣD + V_T is
  15% below P).
  - The bank itself is not at risk: CET1 17.0%, 2.5 pp above a requirement just lowered to
    14.5%. It still earns a ~9–10% ROE in Bear.
- **What the price needs** (any one of):
  - an exit P/E of **~13.3** (Base 12);
  - loan growth of ~4.8% a year (Q3 runs at ~2% annualised in local currencies);
  - costs held flat in nominal terms for three years.
- **Against the equity and HY baselines.** Base 8.9% beats World (5.2%), Oslo (2.5%) and the
  Nordic HY market (6.8% before fees) on return.
  - Its **E / R of 0.117** is well below the HY reference (0.196).
  - **Both triggers sit at ≈ SEK 136–138** (−8 to −9%): E / R reaches 0.196 at SEK 136, and
    Base reaches k at SEK 138.
- **Exit cross-check.** The Base exit (P/E 12, P/B 1.55) gives a buyer a return of 9.0%, level
  with Oslo's mid-cycle 9.1%. An exit priced on the index return (P/E 11.85) gives 8.5%.

**Decision table (SEK, per share)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (SEK) / NOK on the Equity BBB path | −5.4% / −3.4% | **8.9% / 8.9%** | 18.3% / 17.3% |
| V_T (31 Dec 2029) | 102.9 | **158.2** | 209.0 |
| P_k / margin of safety | 93.7 / −37.5% | **138.3 / −7.7%** | 175.2 / +16.9% |
| Capital preserved? (ΣD + V_T vs P) | **No: −15%** | Yes: +27% | Yes: +63% |
| ΣD_t paid 2027–29 | 25.07 | **32.68** | 34.66 |
| Book value per share at exit / P/B at exit | 101.2 / 1.02 | **102.4 / 1.55** | 104.9 / 1.99 |
| Balance sheet | CET1 within target (payout cut to 70%); ROE 9–10% | CET1 held ~2.5 pp above requirement at an 85% payout | Same; more room for extra distributions |

**Per-share path (SEK; Track A rows; calendar years = fiscal years)**

| | CY26 (9M actual + Q4E) | 2027 | 2028 | 2029 | 2030 (exit EPS) |
|---|---|---|---|---|---|
| Base EPS | 11.63 reported (**11.19** excl. VAT refund) | 11.89 | 12.38 | 12.77 | 13.19 |
| Base EPS growth | (−2.9% vs 2025 reported 11.98) | +6.3% (vs 11.19) | +4.1% | +3.2% | +3.3% |
| Base D_t (paid ~1 Apr) | — | 12.05 (FY26) | 10.11 | 10.52 | |
| Base ROE (on opening book) | 13.3% (9M, company) | 12.1% | 12.7% | 12.8% | 12.9% |
| Base V_t (year-end) | 149.9 (stub flat) | 153.5 | 155.8 | 158.2 | |
| Bear EPS / D_t / V_t | | 9.73 / 12.05 / 88.7 | 8.87 / 6.81 / 96.7 | 9.67 / 6.21 / 102.9 | 10.29 |
| Bull EPS / D_t / V_t | | 12.67 / 12.05 / 176.9 | 13.93 / 10.77 / 192.1 | 14.95 / 11.84 / 209.0 | 16.08 |

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value ·
`[E]` external or secondary · `[C]` carried from an earlier version · `[A]` own assumption ·
`[?]` not found or unverified.

## Header

| Item | Value |
|---|---|
| Company | Svenska Handelsbanken AB (publ), Nasdaq Stockholm: **SHB A** (and SHB B, 1.8% of shares). Decentralised branch bank; home markets Sweden, UK, Norway and the Netherlands. Largest owners include Industrivärden and the Oktogonen profit-sharing foundation (insiders 26% per Yahoo) `[E]` |
| Price (P) | **SEK 149.85** (SHB A), Yahoo `SHB-A.ST`, close Fri 23 Oct 2026 (15:29 UTC; +1.5% on the day) `[F]`. 20 Oct (before the report) 153.70; 21 Oct **149.05 (−3.0%)**; 22 Oct 147.70. Version 2: 151.35 (15 Oct). 52-week range 116.80–157.90 `[F]`. The B share closed at SEK 232.20 on thin volume (not used) |
| Valuation date / exit date | 24 Oct 2026 / 31 Dec 2029, **T = 3.19 years** (version 2: 15 Oct, T = 3.21) |
| Shares | **1,980.03m** (A 1,944.78m + B 35.25m); unchanged, no repurchases (Q3 report, key metrics `[F]`). Repurchase authorisation for up to 120m shares from the 2026 AGM `[F]`; no buybacks modelled |
| Market cap | SEK 299.6bn at class prices (NOK 281.9bn) |
| Book value | **Shareholders' equity SEK 188.2bn = SEK 95.06 a share** (30 Sep 2026 `[F]`); total equity SEK 194.2bn includes SEK 6.0bn of AT1 issued in 2026. Company "adjusted equity per share" 97.99. **P/B 1.58** on shareholders' equity (Yahoo's 1.53 divides total equity incl. AT1) |
| P/E | **12.9x** CY26 reported (11.63 = 9M 8.68 + Q4 consensus 2.95), **13.4x** excluding the VAT refund (11.19); **12.3x** CY27 consensus (SEK 12.19, 12 analysts); 12.6x Base CY27 (11.89) |
| NAVs (Step 3) | Not applicable (bank; Track A). Book value is the anchor: P/B 1.58 at an ROE of ~13% |
| Capital | **CET1 17.0%** (30 Sep), **2.5 pp above the requirement**. The requirement was cut from 14.7% to **14.5%** after SREP (Pillar 2 1.5 → 1.2 pp) `[F]` |
| Capital (cont.) | Target 1–3 pp above. Total capital 22.1%; Tier 1 18.9% after a SEK 6bn AT1 `[F]` |
| Capital (cont.) | Anticipated dividends 9M **SEK 15.9bn = 8.02 a share = 92% of profit** `[F]` |
| Capital (cont.) | Household PD model approved after the period. It is implemented in Q4: REA +SEK 1bn, CET1 requirement **−SEK 3bn net** `[F]` |
| Capital (cont.) | LCR 172%, NSFR 119%. Ratings S&P AA−, Fitch AA+, Moody's Aa2 (BCA A1) `[F]` |
| FX | SEK report and price: no conversion. NOK memo at SEK/NOK **0.9409** (Yahoo `SEKNOK=X`, 23 Oct daily close) `[F]` |
| FX (cont.) | Cross-check: Norges Bank fixing 23 Oct **0.9403** (94.03 per 100 SEK) `[F]`, 0.06% apart |
| FX (cont.) | The Yahoo weekend print of 0.9384 (24 Oct, bid/ask 0.951) is not used |
| FX (cont.) | 52-week range 0.938–1.101: the krona is at its weakest against the krone in a year |
| Track | **A** (EPS, P/E, d + g) with a dated IRR build to an exit P/E and a hurdle price P_k. Banks are not capital-intensive in the capex sense; earnings move with rates and credit losses, so a structural/cyclical check is shown |
| k | **12%**, not raised: AA-class ratings, CET1 surplus, liquid share (~SEK 600m traded a day, 3-month average) |
| Horizon | Stub Q4-26 (Q3 now reported) + 2027–2029 annual; exit on 2030 EPS. Next report: **year-end highlights 3 Feb 2027** `[F]` |

**Sources (connector · document · period):**
- **Handelsbanken interim report January–September 2026** (21 Oct 2026), full PDF from Cision
  (`mb.cision.com/Main/3555/4412599/4328910.pdf`), extracted with Nordic Financial
  `parse_pdf_to_text` (67 pages). Read:
  - pages 1–9 (overview, income, capital), 10 (Handelsbanken Sweden) and 20 (key metrics);
  - pages 24–25 (balance sheet, changes in equity) and 65 (share information);
  - the headline lines of the UK, Norway, Netherlands and Markets segments.
  - Not read: notes 2–25 (credit-risk stages, loans by sector, liquidity detail).
- **Nordic Financial** (`search_filings`, STHY Newsweb stream and nasdaq_se, 2026): Q3 headline
  release (21 Oct); earlier interim reports Q1 (22 Apr) and Q2 (15 Jul); press releases to
  19 Oct (no share issue, no buyback).
- **Yahoo** (23–24 Oct): price, daily chart 14–23 Oct, SEK/NOK, `earningsTrend` and
  `financialData`:
  - Q4-26 EPS 2.95 (2 analysts), CY26 11.47 (8, mixed basis, see Appendix), CY27 12.19 (12),
    Q1-27 3.04 (2);
  - target mean SEK 142.9, median 143, range 127–176 (16 analysts); recommendation mean 3.9
    ("underperform").
- **Placera / Modular Finance** (21 Oct) `[E]`: Q3 consensus for operating profit, NII, fees,
  costs and credit losses. SB1 Markets' estimate of SEK 67bn of distributions over three years.
- **Norges Bank API** (`norges-bank` connector): SEK/NOK fixing 14–23 Oct 2026.
- **FinancialFilings:** not available (monthly quota exhausted, HTTP 429, resets 1 Nov), so
  `filings_list` was not run. The share count is from the Q3 report and is unchanged.

## Scenario definitions (from Equity Market BBB and HY Market BBB; unchanged)

| Scenario | Catalyst | What it does to Handelsbanken |
|---|---|---|
| **Base** (decision) | Equity Base: higher-for-longer rates, earnings at trend. Sweden GDP 2.4% (2027), 1.3%, 1.6%; unemployment falling to 7.4%; the Riksbank hikes from 1.75% to ~2.4% by Q3-27 (as signalled) | Swedish deposit margins widen with the hikes (+SEK 1.2bn NII in 2027, +0.6bn in 2028); Norway's NII shrinks as NIBOR falls (in the net figure); loans +3% a year; fees +4%; costs +2.5%; credit losses normalise to ~5 bp. EPS 11.89 → 13.19; payout 85%; exit P/E 12 |
| **Bear** (stress) | Equity Bear: recession H1 2027 + oil Bear. Sweden GDP 0.0% (2027), unemployment 9.4% (2028); the Riksbank cuts instead of hiking (~1.25%) `[A]`; Nordic HY defaults peak at 8.6% (2028) with Swedish real estate exposed | NII −SEK 1.5bn (2027) and −1.0bn (2028) on rates; volumes flat; fees −5%; credit losses 5 / 10 / 5 bp (SEK 1.2 / 2.4 / 1.2bn). EPS 0.80 / 0.73 / 0.79 of CY27 consensus (Oslo block F: 0.85 / 0.80 / 0.88). Payout cut to 70%. P/E 10 from end-2027 |
| **Bull** (stress) | Equity Bull: soft landing; Sweden 2.8% in 2027; the Riksbank hikes further `[A]` | NII +SEK 1.8bn / +0.9bn on rates; loans +5%; fees +7%; credit losses 1–3 bp. EPS to 14.95 in 2029 (ROE ~15%). Exit P/E 13 |

The stub (24 Oct–31 Dec 2026) is the same in all scenarios: Q4 at consensus, the FY26 dividend
(earned and accrued in the stub, paid 1 Apr 2027) the same in all three, no payment before
April 2027, price flat by convention. Bear and Bull diverge from 1 Jan 2027.

## Company and status

| Key figures `[F]` (SEK m unless stated) | Q3 2026 | Q2 2026 | Q1 2026 | 9M 2026 | 9M 2025 |
|---|---|---|---|---|---|
| Net interest income | 10,051 | 10,008 | 10,016 | 30,075 | 32,902 |
| Net fee and commission income | 3,330 | 3,135 | 3,073 | 9,538 | 8,755 |
| Total income | 13,959 | 13,456 | 14,778 (incl. VAT refund 1,127) | 42,193 | 42,938 |
| Expenses (excl. regulatory fees) | −5,910 | −5,963 | −5,838 | −17,711 | −18,172 |
| Regulatory fees | −691 | −788 | −712 | −2,191 | −2,116 |
| Net credit losses | −5 | −30 | −35 | −70 | +278 |
| Operating profit | 7,353 | 6,678 | 8,195 | 22,226 | 22,933 |
| EPS SEK | 2.87 | 2.60 | 3.21 | 8.68 | 8.97 |
| Return on equity | 13.5% | 12.8% | 13.6% | 13.3% | 13.0% |
| C/I ratio | 42.3% | 44.3% | 39.5% | 42.0% | 42.3% |
| CET1 ratio | 17.0% | 17.2% | 17.2% | 17.0% | 18.2% |
| Anticipated dividend, SEK / share (share of profit) | 3.25 (113%) | 1.84 (71%) | 2.93 (91%) | **8.02 (92%)** | — |
| Loans to the public, period end, SEK bn | 2,393 | 2,347 | | | 2,288 |

The Q1, Q2 and Q3 dividend splits are derived from the cumulative figures (2.93, 4.77, 8.02).

- **Q3 2026 commentary** `[F]`:
  - Operating profit +10% q/q, up in every home market. Income +4%, expenses −1% (−3%
    adjusted), credit losses SEK 5m.
  - **NII +SEK 43m**, but −SEK 100m (−1%) after FX (+112m) and day (+31m) effects. Volumes added
    87m. **Margins and funding costs took −194m, "due to higher funding costs in the quarter
    resulting from higher market rates".**
  - Fees +6% (funds +10%); assets under management at a record SEK 1,508bn (+23% y/y).
- **Against consensus** `[E]` (Modular Finance via Placera):

  | Item | Actual | Consensus | Gap |
  |---|---|---|---|
  | Operating profit | 7,353 | 7,369 | −0.2% |
  | NII | 10,051 | 10,178 | −1.2% |
  | Fees | 3,330 | 3,214 | +3.6% |
  | Costs | −5,910 | −5,878 | +0.5% |
  | Credit losses | −5 | −107 | |
  | EPS | 2.87 | 2.94 (Yahoo, 4 analysts) | −2.4% |

  The share fell 3.0% on the day (153.70 → 149.05).
- **Volumes** `[F]`:
  - In local currencies, home-market loans grew **0.5% q/q** (~2% annualised). Group average
    loans rose 0.7% y/y in 9M.
  - Sweden was flat: average loans SEK 1,598bn, 0% q/q and 0% y/y. Swedish NII was 5,865,
    −0.4% q/q and −6% y/y.
  - UK +2% q/q (+8% y/y) and the Netherlands +2% (+10% y/y). Norway was 0% q/q (−5% y/y).
  - Deposits +2% q/q.
- **Capital and distribution** `[F]`:
  - The 0.2 pp cut in the requirement (SREP) went straight into the Q3 accrual: 113% of Q3
    profit, with the surplus held at 2.5 pp.
  - The household PD model (Q4) lowers the requirement by a further ~SEK 3bn.
  - Q1–Q3 2026 show the bank holding the surplus at 2.5 pp and distributing the rest.
  - SB1 Markets estimates SEK 67bn of distributions over three years `[E]`. The Base here pays
    SEK 64.7bn over its three payments.
- **Rate history** `[F]`:
  - NII 9M −9% y/y (margins −SEK 2.7bn on lower rates). The NII trough is behind: Q2 and Q3 are
    flat to up.
  - The first effect of rising Swedish market rates is negative (funding costs before deposit
    repricing).
- **Mix** `[F/A]`:
  - Handelsbanken Sweden earned SEK 15.6bn of the group's 22.2bn operating profit in 9M (70%).
  - UK 2.7bn, Norway 2.0bn, the Netherlands 0.6bn.
  - Norway's mortgage risk-weight floor rose from 20% to 25% at end-2025 `[F]`.
- **Dividends** `[F]`: FY2025 SEK 17.50 (ordinary 8.00 + special 9.50; ex 26 Mar, paid 1 Apr
  2026). Policy: ordinary dividend plus distribution of capital above the 1–3 pp target range
  `[E]`.
- **Outlook:** the bank gives no numerical guidance. The report gives no change in strategy or
  targets.
- **Market view** `[E]`: 16 analysts, mean target SEK 143 (−5%), recommendation mean 3.9
  ("underperform"). CY27 consensus 12.19 (12 analysts), unchanged through the report (12.23 a
  week earlier).

## Near term: stub (all scenarios)

| SEK | Q3-26 model (v2) | **Q3-26 actual** | Q4-26E | CY26E |
|---|---|---|---|---|
| EPS | 2.94 (cons.) | **2.87** `[F]` | 2.95 (cons., 2 analysts) | **11.63** reported; 11.19 excl. VAT refund (0.44) |
| Total income SEK bn | 14.08 (cons.) | **13.96** | ~14.1 `[A]` | ~56.2 |
| NII SEK bn | ~10.0 | **10.05** | ~10.1 `[A]` | ~40.2 |
| Dividend accrued (paid ~1 Apr 2027) | ~2.4 | **3.25** | 2.51 (85% of Q4E) + **1.52 PD release** `[A]` | **12.05** `[A]` (9M 8.02 `[F]`) |
| CET1 surplus vs requirement | ~2.5 pp | **2.5 pp** (17.0 vs 14.5%) | ~2.5 pp after the PD release | within the 1–3 pp target |

**Q3 test set in version 2:**

| Test | Result |
|---|---|
| EPS ≥ 2.9 | 2.87, just missed |
| NII up q/q | Yes (+0.4%), but −1% adjusted |
| C/I ≤ 44% | 42.3%, passed |
| Credit losses ~0 | Passed |
| CET1 surplus 2–3 pp | 2.5 pp, passed |
| Anticipated dividend ≥ 80% of profit | 92% for 9M, passed |

**Q4 test (3 Feb 2027):**
- the FY26 dividend proposal is ≥ SEK 12 (the Base carries the PD release); below SEK 10.5
  means the release was held back;
- NII ≥ SEK 10.0bn after the 4 Nov Riksbank decision;
- credit losses ≤ 2 bp.

**Dividend timing:** AGM in late March, ex-date late March, paid about 1 April (2026 pattern
`[F]`). The AGM date for 2027 is not yet published `[?]`.

## Market input (Equity and HY baseline rows used and how they enter)

| Driver | Baseline row | Bear / **Base** / Bull | How it enters |
|---|---|---|---|
| Scenario frame | Equity BBB scenario definitions (unchanged in Update 1) | Recession + oil Bear / **trend** / soft landing | Defines the catalysts and timing (Bear from Q1 2027) |
| Swedish growth, unemployment | HY BBB Sweden rows: GDP 0.0 / **2.4** / 2.8 (2027), 1.0 / **1.3** / 2.0, 2.0 / **1.6** / 1.8; unemployment 9.2 / **8.1** / 7.9 → 8.9 / **7.4** / 7.2 (Sep 2026 LFS 8.7% SA `[F]`) | Loan growth 0–2 / **3** / 5%; fees −5 then +3–4 / **+4** / +7% | Sets volumes, fees and the credit-loss path (Bear peaks at 10 bp in 2028 with unemployment) |
| Swedish policy rate | HY BBB text: Riksbank 1.75%, signals ~2.4% by Q3-27 `[E]`; **no path in any baseline**; next decision 4 Nov | Cuts to ~1.25% / **hikes to ~2.4%** / ~2.75% `[A]` | NII effect −1.5 / **+1.2** / +1.8bn (2027), −1.0 / **+0.6** / +0.9bn (2028) at ~SEK 3bn of NII per 1 pp `[A]` |
| Norwegian rates | HY BBB 3M NIBOR 4.21 / **4.79** / 4.65 → 3.50 / **3.86** / 3.65 (2029) (unchanged) | Norway segment NII shrinks as NIBOR falls (−SEK 0.2bn in Base 2030) | Netted in the rate effect |
| Bank earnings reference | Equity BBB Oslo block F (DNB, Storebrand, Gjensidige; unchanged): Bear 0.85 / 0.80 / 0.88, **Base 0.98 / 0.96 / 0.95**, Bull 1.00 / 1.03 / 1.05 of CY27 consensus | Handelsbanken Bear 0.80 / 0.73 / 0.79, **Base 0.98 / 1.02 / 1.05**, Bull 1.04 / 1.14 / 1.23 | Base is above block F for a named reason: the Riksbank is hiking while Norges Bank cuts. Bear is a little harsher (Swedish property exposure) |
| Exit multiple and cross-check | Equity BBB Oslo: exit P/E 10.5 / **11.5** / 12.5, exit P/B 1.48 / **1.75** / 1.97, mid-cycle return 8.2 / **9.1** / 9.4% | **10 / 12 / 13** `[A]` | Independent of the IAF ceiling; tested in the exit cross-check below |
| NOK | Equity BBB I-44: 109.5 spot; Bear ~118 (+8%) 2027, ~116 (+6%) 2028–29; **Base flat**; Bull ~107 (−2%). No SEK/NOK path | SEK cash flows on I-44 (skill rule) | Bear and Bull NOK figures only. Version 2's own SEK/NOK view (Bear +5% in 2027 and +4% after, Base flat, Bull −2%) is kept as a sensitivity: the SEK also weakens in a global recession |
| Index and HY context | Equity BBB Base window: Oslo **2.5%** (was 3.1%), World **5.2%** (was 6.1%); Nordic HY 6.8% before fees; HY market reference E / R **0.196** | — | Context only; a market priced below k never lowers k |

## Common assumptions

- **Earnings build** `[A]`, rebased in version 3 to the Q3 2026 run rate:
  - NII SEK **40.2bn** (4 × Q3), fees **13.3bn** (4 × Q3).
  - Other income (net gains on financial transactions plus other) **1.95bn** a year: the 9M
    recurring run rate, excluding the Q1 VAT refund of 1.127bn. Version 2 carried 3.3bn, which
    included the refund.
  - Expenses including regulatory fees and the risk tax **26.6bn** (CY26E: 9M 19.9bn + Q4 6.7bn).
    The model's C/I includes regulatory fees; the reported C/I excludes them.
  - Profit for EPS (after tax and AT1 coupons) = **0.772 × operating profit** (9M 2026; Q3 0.773).
  - Base costs grow 2.5% a year. Base CY27 EPS 11.89 is 2.4% below consensus (12.19); version 2
    had 12.05.
- **Credit losses** in SEK bn on loans of **SEK 2,393bn** (30 Sep `[F]`; was an assumed ~2,400):
  - Base 0.5 / 1.0 / 1.2 / 1.2 (2 → 5 bp); Bear 1.2 / 2.4 / 1.2 / 0.8 (5 / 10 / 5 / 3 bp); Bull
    0.3–0.6.
  - Handelsbanken's losses stayed near zero through the 2023 Swedish property stress, and were
    0.00% in 2026 `[F]`. The Bear is a recession with rising unemployment, not that case.
- **Dividends:**
  - **FY26 SEK 12.05, paid 1 Apr 2027, in all scenarios** `[A]`. This is 9M 8.02 `[F]`, plus 85%
    of Q4E EPS 2.95 (2.51), plus the PD-model release of ~SEK 3bn ÷ 1,980m shares = 1.52 at an
    unchanged 2.5 pp surplus.
  - The cash paid out no longer earns interest: −SEK 0.12bn a year pre-tax from 2027 `[A]`.
  - From FY27: 85% of prior-year EPS (Base, Bull) or 70% (Bear), paid each 1 April. 85% is close
    to the 9M ratio excluding the SREP release (83%) and keeps CET1 stable at ~3% loan growth.
  - No buybacks.
- **Exit:** V_T = exit P/E × 2030 EPS, cum the FY29 dividend (as today's price is cum the FY26
  dividend). **Exit P/E Bear 10 / Base 12 / Bull 13** `[A]`, unchanged:
  - Base 12: today's 12.6 on Base CY27 less a small fade, level with block F on CY27 (12.0) and
    above Oslo's exit (11.5). Base exit P/B 1.55 at an ROE of 12.9%.
  - Bear 10: Nordic bank troughs (2020, 2022), reached at end-2027. Exit P/B 1.0.
  - Bull 13: P/B 1.99 at an ROE of 15%.
  - The independent check is the exit cross-check below. The IAF anchor (P/B = (ROE − g) / (k − g)
    ≈ 1.1, P/E ≈ 8.5) shows the market prices this bank at ~9%, not 12%.
- **Interim V_t:** price flat at end-2026. The P/E glides from 12.6 (today, on Base CY27) to the
  exit P/E; Bear is at 10 from end-2027.

## Period tables and year-end path

**Base** (SEK bn unless stated)

| | 2027 | 2028 | 2029 | 2030 (exit EPS) |
|---|---|---|---|---|
| Total income (growth vs Q3 run rate 55.45) | 58.39 (+5.3%) | 60.82 (+4.2%) | 62.73 (+3.1%) | 64.50 (+2.8%) |
| — NII / net fees / other | 42.61 / 13.83 / 1.95 | 44.48 / 14.39 / 1.95 | 45.82 / 14.96 / 1.95 | 46.99 / 15.56 / 1.95 |
| Expenses incl. regulatory fees (C/I) | 27.27 (46.7%) | 27.95 (46.0%) | 28.65 (45.7%) | 29.36 (45.5%) |
| Credit losses (bp) | 0.5 (2) | 1.0 (4) | 1.2 (5) | 1.2 (5) |
| Interest forgone on FY26 distribution | −0.12 | −0.12 | −0.12 | −0.12 |
| Operating profit | 30.50 | 31.75 | 32.76 | 33.82 |
| Profit for EPS | 23.55 | 24.51 | 25.29 | 26.11 |
| **EPS** SEK (vs CY27 consensus 12.19) | **11.89** (0.98) | **12.38** (1.02) | **12.77** (1.05) | **13.19** (1.08) |
| Dividend paid in year, SEK / share (SEK bn) | 12.05 (23.9) | 10.11 (20.0) | 10.52 (20.8) | |
| Book value per share, year-end (end-2026: 98.01) | 97.85 | 100.12 | 102.37 | |
| ROE (on opening book) | 12.1% | 12.7% | 12.8% | 12.9% |

**Bear** (lines that differ)

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Total income | 53.29 | 52.66 | 53.94 | 55.55 |
| Expenses (+1.5% a year) / C/I | 27.00 / 50.7% | 27.40 / 52.0% | 27.82 / 51.6% | 28.23 / 50.8% |
| Credit losses (bp) | 1.2 (5) | 2.4 (10) | 1.2 (5) | 0.8 (3) |
| EPS | 9.73 | 8.87 | 9.67 | 10.29 |
| Dividend paid in year | 12.05 | 6.81 | 6.21 | |
| BVPS / ROE | 95.69 / 9.9% | 97.74 / 9.3% | 101.21 / 9.9% | — / 10.2% |

**Bull** (lines that differ)

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Total income | 60.19 | 64.29 | 67.71 | 71.32 |
| C/I | 45.3% | 43.5% | 42.3% | 41.2% |
| EPS | 12.67 | 13.93 | 14.95 | 16.08 |
| Dividend paid in year | 12.05 | 10.77 | 11.84 | |
| BVPS / ROE | 98.63 / 12.9% | 101.79 / 14.1% | 104.90 / 14.7% | — / 15.3% |

**Year-end path** (D_t paid in the year; V_t at year-end; r_t in SEK, NOK on the Equity BBB I-44
path in brackets)

| | End-2026 (stub) | 2027 | 2028 | 2029 (exit) |
|---|---|---|---|---|
| Bear: D / V / P/E | 0 / 149.9 / 12.6 | 12.05 / 88.7 / 10.0 | 6.81 / 96.7 / 10.0 | 6.21 / 102.9 / 10.0 |
| Bear: r_t | 0.0% | **−32.8% (NOK −27.6%)** | 16.8% (14.8%) | 12.8% (12.8%) |
| **Base: D / V / P/E** | 0 / 149.9 / 12.6 | 12.05 / 153.5 / 12.4 | 10.11 / 155.8 / 12.2 | 10.52 / 158.2 / 12.0 |
| **Base: r_t** | 0.0% | **10.5%** | 8.1% | 8.3% |
| Bull: D / V / P/E | 0 / 149.9 / 12.6 | 12.05 / 176.9 / 12.7 | 10.77 / 192.1 / 12.85 | 11.84 / 209.0 / 13.0 |
| Bull: r_t | 0.0% | 26.1% (NOK 23.2%) | 14.7% (14.7%) | 15.0% (15.0%) |

- Base pays 8–10% a year, almost all of it dividend. No year reaches 12%. 2027 is the best year
  only because the FY26 payment carries the capital release.

## V_T bridge (Base, per share), exit cross-check and exit consistency

| Step | SEK/share |
|---|---|
| P (24 Oct 2026) = 12.60 × Base CY27 EPS 11.89 | 149.85 |
| EPS growth to 2030 (11.89 → 13.19; **+3.3% a year** over T) | +16.4 |
| De-rating 12.60 → 12.0 (**−1.5% a year**) | −7.9 |
| **= V_T** (12.0 × 13.19) | **158.2** |
| Book value per share at exit / P/B | 102.4 / 1.55 (from 1.58 on 30 Sep book; 1.53 on end-2026 book) |

- g = (158.2 / 149.85)^(1/3.19) − 1 = **1.7% a year**; d = 6.8%; c = +0.3 pp. Retained earnings
  sit in book value and are carried by EPS growth (counted once). The extra FY26 distribution is
  paid in D_t, and its lost interest is taken out of EPS.

**Exit cross-check against the equity market (skill Step 3)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| Exit P/E (V_T ÷ 2030 EPS) | 10.0 | **12.0** | 13.0 |
| Exit P/B (V_T ÷ BVPS end-2029) | 1.02 | **1.55** | 1.99 |
| ROE 2030 (normalised, on opening book) | 10.2% | **12.9%** | 15.3% |
| Buyer's implied return at exit (payout ÷ exit P/E + retained share × ROE) | 10.0% (7.0 + 3.0) | **9.0% (7.1 + 1.9)** | 8.8% (6.5 + 2.3) |
| Equity BBB Oslo: exit P/E / exit P/B / mid-cycle return | 10.5 / 1.48 / 8.2% | **11.5 / 1.75 / 9.1%** | 12.5 / 1.97 / 9.4% |

- **Base is priced level with Oslo on return (9.0 vs 9.1%)**, at a higher P/E and a lower P/B. The
  stated reasons:
  - Handelsbanken pays out 85%, against block F's 63%;
  - its ROE (12.9%) is below Oslo's normalised 15.2%;
  - it has the lowest loss history and ratings among Nordic banks (beta 0.49).
  - The exit P/B of 1.55 sits inside Oslo's 1.5–2.1 band.
- **Bull** gives a buyer 0.6 pp less than Oslo's Bull (8.8 vs 9.4%). The reason is the same: the
  low-risk premium. **Bear** is priced more cheaply than Oslo's Bear (10.0 vs 8.2%), which is
  conservative.
- **Sensitivity on the cross-check:** an exit priced on Oslo's Base mid-cycle return (9.1% → P/E
  ≈ 0.85 ÷ (0.091 − 0.019) ≈ 11.85) gives **Base IRR 8.5%, P_k 137.0 (−8.6%)**. The verdict does
  not depend on the exit being cheaper or dearer than the index; it would need P/E ~13.3.
- **Exit consistency (Step 3):** the mean-reverting drivers are the policy rate and credit
  losses. 2030 EPS is at each scenario's normalised level.
  - Base: Year 3 vs exit, rate effect −SEK 0.2bn (0.6% of operating profit); credit losses equal.
  - Bear: credit losses 1.2 vs 0.8bn (1.6%), rate +0.3bn (1.2%).
  - Bull: no gap.
  - All are below the 10% materiality limit. **No reversion tail.**

## Growth capex test (Step 4)

- A bank's "growth capex" is retained equity backing loan growth. Base retains ~15% of earnings
  (~SEK 1.8 a share a year) to fund ~3% loan growth at an incremental ROE of ~12–13% `[A]`. That
  is about k, so growth creates little value, and the market pays for the dividend rather than
  the growth.
- **Q3 evidence:** home-market loans grow ~2% a year in local currencies, and Sweden is flat. The
  capital that growth does not need goes out as dividends (113% of Q3 profit). That is the right
  use while growth earns only ~k.
- **Buybacks** (authorisation up to 120m shares): at P/B 1.58 and ROE ~12.8%, a buyback earns
  ~8.1% on the price paid, below k. Paying surplus capital as dividends is the better use at this
  price.

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (dated, to the exit value; SEK) | −5.4% | **8.9%** | 18.3% |
| IRR_T in NOK on the Equity BBB NOK path (I-44) | −3.4% | **8.9%** | 17.3% |
| Track A: Rule 1 screen d + g (EPS CAGR CY26 excl. VAT → 2029; assumes today's P/E holds) | 5.6 − 4.7 = 0.8% | **7.3 + 4.5 = 11.8% (fails)** | 7.7 + 10.1 = 17.8% |
| d / g / c (dated build) | 5.3 / −11.1 / 0.4 | **6.8 / 1.7 / 0.3** | 7.3 / 11.0 / 0.0 |
| g: re-rating / NAV growth (P/NAV_0) | n/a (Track A; P/B 1.58 → 1.02) | **n/a (P/B 1.58 → 1.55)** | n/a (1.58 → 1.99) |
| Structural IRR / cyclical (pp; Δd, Δg) | −5.3% / −0.1 (−0.1, 0.0) | **8.8% / +0.05 (+0.05, 0.0)** | 18.4% / −0.1 (0.0, 0.0) |
| ΣD_t / V_T | 25.07 / 102.9 | **32.68 / 158.2** | 34.66 / 209.0 |
| P_k (hurdle price) / margin of safety | 93.7 / −37.5% | **138.3 / −7.7%** | 175.2 / +16.9% |
| Rule 3: P/E (CY26 excl. VAT) vs ceiling (d + g) / k² | 13.4 vs 0.6 | **13.4 vs 8.2 (fails)** | 13.4 vs 12.4 |
| Capital preserved? ΣD + V_T vs P | **No (−14.6%)** | Yes (+27.4%) | Yes (+62.6%) |

- **Structural run:** each scenario's own normalised (2030) rate effect and credit-loss level from
  1 Jan 2027, with volumes, fees and the exit unchanged.
  - The cycle inside each scenario is small (≤ 0.1 pp).
  - **Bear is a shift in the mid-cycle itself.** Its structural IRR is −5.3% against Base's
    +8.8%, a shift of −14.1 pp. That shift comes from a lasting lower rate level (~1.25%), flat
    volumes and a P/E of 10, not from the 2028 credit-loss spike.
  - Bull is a +9.6 pp shift (volumes, fees, P/E 13).
- **FCF_normalised (Track B) does not apply.** Rule 3 uses P/E on CY26 excluding the VAT refund.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** 8.3%. Not a decision figure.
- **Share of Bull already priced:** (149.85 − 138.3) / (175.2 − 138.3) = **31%** (was 40%).
- **Bear balance sheet:** no survival question.
  - ROE stays at 9–10%, book value recovers from 2028, and the payout cut to 70% keeps CET1
    inside the target band.
  - The loss is the multiple (12.6 → 10) and ~20% lower earnings.
  - If a board facing a Q1 2027 recession holds back the PD release (FY26 10.53), Bear is −5.7%.
- **NOK:** on version 2's own SEK/NOK view (+5% in 2027, +4% after), Bear is −4.1% in NOK and
  2027 is −29.4%. The I-44 rule gives a larger krone cushion than a krona that also weakens in a
  recession would.
- **E / R (HY rule, NOK):** E = 8.85 − 4.38 = **4.47 pp**. R = Base 2027 (10.5%) − Bear 2027
  (−27.6%) = 38.1 pp. **E / R = 0.117** (was 0.095).
  - That is above World (0.024) and Oslo (−0.07), and well below the HY market reference (0.196).
- **Sensitivities (Base IRR / P_k / margin of safety):**

| Change | IRR | P_k | MoS |
|---|---|---|---|
| Exit P/E 10.5 / 13.5 | 4.8% / 12.6% | 124.5 / 152.1 | −16.9% / +1.5% |
| **Break-even exit P/E** | **12.0% at ~13.3** | 149.85 | 0% |
| Exit at Oslo's mid-cycle return 9.1% (P/E 11.85) | 8.5% | 137.0 | −8.6% |
| Riksbank does not hike (rate effect zero) | 7.0% | 131.8 | −12.1% |
| Credit losses doubled | 7.6% | 134.0 | −10.6% |
| Costs +3.5% a year / flat | 7.7% / 11.5% | 134.3 / 147.8 | −10.4% / −1.4% |
| Payout 70% from FY27 | 8.1% | 135.4 | −9.7% |
| Loan growth 5% a year / **2% (the Q3 run rate)** | 12.3% / **7.1%** | 151.1 / 132.2 | +0.8% / −11.8% |
| No PD release (FY26 dividend 10.53) | 8.6% | 137.1 | −8.5% |

**Bridge from version 2 (Base IRR / P_k):**

| Step | Base IRR | P_k |
|---|---|---|
| Version 2 | 8.1% | 136.7 |
| Price 151.35 → 149.85 and valuation date 15 → 24 Oct | 8.6% | 137.1 |
| Rebase to the Q3 run rate (EPS path −1.3%) | 8.4% | 136.4 |
| FY26 dividend from the 9M accrual (10.53) | 8.6% | 137.1 |
| PD release (FY26 12.05) | **8.9%** | **138.3** |

## Verdict and caveat

- **Fails: Base margin of safety −7.7%** (below the −2% line). Base IRR 8.9% against k = 12%.
- **Does not survive Bear:** −5.4% a year in SEK (−3.4% in NOK), and a 15% capital loss over the
  window. That happens if a 2027 recession turns the Riksbank to cuts and credit losses rise to
  ~10 bp, with the P/E at 10.
- **What would flip it:**
  - a price near **SEK 136–138** (−8 to −9%): Base reaches k and E / R reaches the HY reference;
  - or loan growth of ~5% together with the Riksbank hikes. Q3 shows ~2%, so the volume line runs
    behind Base, not ahead of it.
  - The business is very safe, and the price already pays for that safety (P/B 1.58, an implied
    required return of ~9%).
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation or a price target. Returns are
  before tax. Swedish withholding tax applies to dividends paid to a Norwegian holder (15% under
  the treaty `[E]`). That matters for a stock where the dividend is ~80% of the return.

## Tracking

| Version | Date | Price SEK | Base IRR | P_k | MoS | What changed |
|---|---|---|---|---|---|---|
| 1 | 12 Oct 2026 | 152.10 | 7.9% | 136.6 | −10.2% | Initial analysis |
| 2 | 15 Oct 2026 | 151.35 | 8.1% | 136.7 | −9.7% | Price and valuation date only |
| **3** | **24 Oct 2026** | **149.85** | **8.9%** | **138.3** | **−7.7%** | Q3 actual; FY26 dividend from the 9M accrual plus the PD release; base rebased to Q3; Equity BBB Update 1 (exit cross-check, I-44 NOK rule) |

- **Q3 actual vs model:**
  - EPS 2.87 vs 2.94 (−2.4%); operating profit 7,353 vs 7,369 consensus (−0.2%).
  - Dividend accrued 3.25 vs ~2.4 modelled (**+0.85**); CET1 surplus 2.5 pp as modelled.
  - Change in Base P_k: **+1.6** (136.7 → 138.3).
- **Running ahead of or behind Base:**
  - **Ahead** on capital return and costs (9M expenses −3% y/y).
  - **Behind** on volume: ~2% annualised against Base 3%, with Sweden flat.
  - **Behind** on the NII margin: rising Swedish market rates first raised funding costs (−SEK
    194m in Q3).
  - Credit losses on track (0.00%). Net: on track, with a better mix of cash and a weaker volume
    line.
- **Equity Market BBB Update 1:** no decision effect (see the change gate). Index returns fell
  (Oslo 2.5%, World 5.2%), which widens Handelsbanken's lead on return but not on E / R.
- **Market:** SHB A −1.0% since 15 Oct (153.70 before the report, −3.0% on 21 Oct). SEK/NOK 0.951
  → 0.941: the krona is at a new 52-week low against the krone.

## Risks and signposts

| Signpost | Bear / Bull threshold | Now | Source |
|---|---|---|---|
| Riksbank policy rate | cut below 1.75% / hikes above 2.4% | 1.75% (Sep 2026), hikes signalled; **decision 4 Nov** | HY BBB `[E]` |
| Swedish unemployment (LFS) | > 9.2% / < 8.0% | 8.7% SA (Sep, SCB) | HY BBB `[F]` |
| Handelsbanken NII q/q | falls two quarters / > +3% q/q | +0.4% in Q3 (−1% adjusted; funding costs −194m) | Company `[F]` |
| Loan growth, local currencies (new) | < 0% a year / > 4% a year | ~2% annualised (Q3 +0.5% q/q); Sweden 0% y/y | Company `[F]` |
| C/I ratio (reported) | > 46% / < 40% | 42.3% (Q3), 42.0% (9M) | Company `[F]` |
| Credit loss ratio | > 0.08% / ≤ 0.02% | 0.00% (Q3, 9M) | Company `[F]` |
| CET1 surplus vs requirement | < 1.5 pp / > 3 pp (extra distributions) | 2.5 pp (17.0 vs 14.5%) | Company `[F]` |
| FY26 dividend proposal (3 Feb 2027) (new) | < SEK 10.5 (release held back) / > 12.5 | Base 12.05; 9M accrual 8.02 | Company / this analysis |
| Swedish real-estate distress (HY BBB log) | Swedish FTD > 6% / < 2% | 3.0% (2025) | HY BBB |
| P/E on CY27 consensus | ≤ 11.2 (trigger region) / ≥ 13.5 | 12.3 | This analysis |
| **Price** | **≤ SEK 136–138 (E / R = 0.196; Base = k)** | SEK 149.85 (23 Oct) | Yahoo |
| Equity BBB Bear signposts | US HY OAS > 450 bp; MSCI World fwd P/E < 15.5; Nordic HY spread > 550 bp; USD/NOK > 10.5 | US HY OAS 3.23% (15 Oct) | `docs/equity-market-bbb.md` |

- **Other risks:**
  - competition for Swedish mortgages (margin pressure, as in 2025; Swedish lending flat in 2026);
  - the UK and Netherlands growth strategy (low market share, higher cost to win; a UK CEO-elect
    since 1 Oct, pending regulatory approval);
  - regulatory change (risk-weight floors, the Riksbank's interest-free deposit requirement at SEK
    123m a year `[F]`);
  - SEK appreciation lowers translated UK and Norway earnings. In 2026 the weaker SEK added SEK
    4.3bn of OCI `[F]`.
- **Next update:**
  - the Riksbank decision on 4 Nov, the Equity BBB full update (stale after 10 Nov) and the HY
    baseline (stale after 5 Nov);
  - then the year-end report on **3 Feb 2027**, which carries the FY26 dividend proposal.

## For other modules

- **hy-market-bbb:** **gap (unchanged).** No Riksbank or STIBOR path is set anywhere, but Swedish
  banks and SEK bonds need one.
  - Suggest a Swedish policy-rate row (Bear / Base / Bull) beside the NIBOR row at the update
    after 4 Nov.
  - Q3 evidence for it: higher Swedish market rates already raised Handelsbanken's funding costs
    before any hike (−SEK 194m q/q).
- **equity-market-bbb:** **gap (unchanged):** no SEK/NOK path. This analysis now applies the I-44
  rule.
  - The Nordic bank reference is consistent with block F: Handelsbanken's Base 0.98 / 1.02 / 1.05
    against block F's 0.98 / 0.96 / 0.95. That is a named rate-path difference, not a conflict.
  - Handelsbanken's payout (85–92%) is well above block F's 0.63.
- **Portfolio:** no action implied. Handelsbanken at SEK 150 does not reach the HY market
  reference on E / R (0.117 vs 0.196). Watch level ~SEK 136–138, unchanged; not a
  recommendation.

## Change log

- **12 Oct 2026 — initial analysis** (iaf-valuation 2026-10-11.3; equity-market-bbb document
  11 Oct 2026; hy-market-bbb document 5 Oct 2026). No previous values.
- **15 Oct 2026 — version 2: price refresh** on the user's request to update for the Equity and
  AI baselines.
  - Equity Market BBB unchanged (11 Oct document). AI Market BBB Update 1 read for macro context
    only (not an input).
  - Changed: price SEK 152.10 → 151.35, SEK/NOK 0.953 → 0.9514, valuation date 12 → 15 Oct
    (T 3.22 → 3.21).
  - Results: Base IRR 7.9% → **8.1%**, P_k 136.6 → 136.7, MoS −10.2% → **−9.7%**; Bear −6.0% →
    −5.8%; Bull 17.1% → 17.3%; E / R 0.09 → 0.095; break-even exit P/E 13.7 → 13.6.
  - Added: Tracking section. **No assumption changed; verdict unchanged (fails).**
- **24 Oct 2026 — version 3: Q3 report and Equity BBB Update 1** (iaf-valuation 2026-10-18.2;
  update-chain causes: equity changed 2026-10-18, event passed 2026-10-21).
  - **Inputs read:**
    - Equity BBB Update 1 (17 Oct, amended 18 Oct; 24 Oct note);
    - HY BBB of 24 Oct (kept unchanged, values as 5 Oct);
    - the Q3 interim report (full PDF, sections listed in the Header);
    - price and FX at the 23 Oct close.
  - **Company facts:**
    - Q3 EPS 2.87 (9M 8.68); NII 10,051m; costs −5,910m; credit losses −5m;
    - CET1 17.0%, 2.5 pp above a requirement cut to 14.5%;
    - 9M anticipated dividend 8.02 (92%); household PD model releases ~SEK 3bn in Q4;
    - loans SEK 2,393bn; shares unchanged.
  - **Model:**
    - 2026 base rebased to the Q3 run rate: other income 3.32 → 1.95bn (the VAT refund removed),
      costs 27.12 → 26.6bn, NII 40.0 → 40.2bn, fees 13.0 → 13.3bn, EPS ratio 0.771 → 0.772;
    - FY26 dividend 9.61 → **12.05**, with interest forgone −0.12bn a year;
    - Base EPS 2027–30: 12.05 / 12.52 / 12.90 / 13.30 → 11.89 / 12.38 / 12.77 / 13.19.
  - **Results:**
    - Base IRR 8.1 → **8.9%**, P_k 136.7 → **138.3**, MoS −9.7 → **−7.7%**;
    - Bear −5.8 → −5.4% (NOK −4.5 → −3.4% on the new I-44 rule); Bull 17.3 → 18.3% (NOK 17.3%);
    - E / R 0.095 → 0.117; break-even exit P/E 13.6 → 13.3; triggers SEK 136 / 138.
  - **Method (skill 2026-10-18.2):**
    - exit cross-check table added (exit P/E, P/B, buyer's implied return vs Oslo), with the
      index-return exit as a sensitivity;
    - Bear and Bull in NOK on the Equity BBB I-44 path (version 2's SEK/NOK view kept as a
      sensitivity);
    - structural run defined per scenario on its own normalised rate and loss level.
  - **Corrections:**
    - Book value now excludes the SEK 6bn AT1 in equity. Version 2's 93.13 (30 Jun) included it,
      so its P/B of 1.63 should have read 1.68. No decision effect: V_T is P/E-based.
    - Yahoo's CY26 consensus mixes bases; the stub now uses 9M actual + Q4 consensus.
  - **Kept unchanged:** scenarios, drivers (volume 3%, rate effect, fees, cost growth, credit-loss
    path, payout 85% / 70%), exit P/E 10 / 12 / 13 and k.
  - **Verdict unchanged (fails).**

## Appendix: own assumptions `[A]`

| Item | Bear | Base | Bull | Basis |
|---|---|---|---|---|
| Swedish policy rate | ~1.25% (cuts 2027) | ~2.4% by Q3-27 | ~2.75% | Riksbank signal via HY BBB `[E]`; decision 4 Nov |
| Rate effect on income, SEK bn 2027 / 28 / 29 / 30 | −1.5 / −1.0 / 0 / +0.3 | +1.2 / +0.6 / 0 / −0.2 | +1.8 / +0.9 / 0 / 0 | ~SEK 3bn per 1 pp on deposit margins, net of Norway; Q3 shows the funding-cost lag first |
| Starting levels, SEK bn (NII / fees / other / costs incl. regulatory fees) | same | 40.2 / 13.3 / 1.95 / 26.6 | same | Q3 2026 run rate; other excl. VAT refund; costs CY26E `[F/A]` |
| Loan (NII volume) growth | 0 / 0 / 2 / 2% | 3% | 5% | GDP rows; Q3 runs at ~2% (flagged; sensitivity 7.1%) |
| Fee growth | −5% then +3–4% | +4% | +7% | AUM at a record, 9M fees +9% y/y |
| Expense growth | +1.5% | +2.5% | +2.5% | Wage inflation, IT investment; 9M 2026 costs −3% y/y |
| Credit losses SEK bn | 1.2 / 2.4 / 1.2 / 0.8 | 0.5 / 1.0 / 1.2 / 1.2 | 0.3 / 0.5 / 0.6 / 0.6 | Loans SEK 2,393bn `[F]` |
| Profit for EPS / operating profit | 0.772 | 0.772 | 0.772 | 9M 2026, after tax and AT1 coupons |
| Q4-26 EPS (stub) | 2.95 | 2.95 | 2.95 | Yahoo consensus, 2 analysts (thin) |
| FY26 dividend (paid 1 Apr 2027) | 12.05 | 12.05 | 12.05 | 9M 8.02 `[F]` + 85% of Q4E + PD release 1.52 (SEK 3bn `[F]` ÷ 1,980m) |
| Interest forgone on the FY26 distribution | −0.12bn a year | same | same | SEK 4.8bn paid out above version 2's 9.61 a share, at ~2.5% a year |
| Payout (from FY27) | 70% | 85% | 85% | 9M 2026 accrual 83% excluding the SREP release; CET1 surplus 2.5 pp |
| Exit P/E (2030 EPS) | 10 (from end-2027) | 12 | 13 | Block F 12.0; Nordic bank troughs; cross-checked against Oslo |
| NOK path | I-44 +7.8% (2027), +5.9% after | flat | −2.3% | Equity BBB I-44 path (skill rule); own SEK/NOK view as a sensitivity |

## Appendix: sources

| # | Source | Content | As of |
|---|---|---|---|
| S1 | Handelsbanken interim report Jan–Jun 2026 (Newsweb via Nordic Financial, STHY stream) | Q2 and H1 key figures, commentary, anticipated dividend 4.77 (82%), CET1 2.50 pp above requirement, target 1–3 pp `[F]` | 15 Jul 2026 |
| S2 | Handelsbanken interim report Jan–Mar 2026 (same) | Q1 key figures, VAT refund SEK 1,127m, anticipated dividend 2.93 (91%), commentary on margins `[F]` | 22 Apr 2026 |
| S3 | Handelsbanken year-end report 2025 (mfn_nordics / nasdaq_se) | Dividend 17.50 (8.00 ordinary), buyback authorisation 120m shares, AT1 authorisation, segment text `[F]` | 4 Feb 2026 |
| S4 | Handelsbanken interim report Jan–Sep 2025 | Handelsbanken Sweden 9M operating profit 17,194m, NII −11% on margins; Norwegian risk-weight floor; Riksbank interest-free deposits `[F]` | 22 Oct 2025 |
| S5 | Stadshypotek interim report Jan–Jun 2026 | Mortgage book SEK 1,572bn; NII −12% y/y; Norway branch NII `[F]` | 15 Jul 2026 |
| S6 | Handelsbanken press releases (Newsweb) | Q3 report on 21 Oct (7 and 19 Oct); executive team changes (1 Oct); no share issue or buyback | 1–19 Oct 2026 |
| S7 | Yahoo `get_quote`, `get_chart`, `quote_summary` (SHB-A.ST, SHB-B.ST, SEKNOK=X, ^OMX) | Price 149.85 and daily closes 14–23 Oct, SEK/NOK 0.9409 (23 Oct close), consensus EPS/revenue, analyst targets, dividend dates `[F]` | 23–24 Oct 2026 |
| S8 | Norges Bank API `EXR/B.SEK.NOK.SP` (`norges-bank` connector) | 95.31 (15 Oct) … 94.03 (23 Oct) per 100 SEK `[F]` | 23 Oct 2026 |
| S9 | `docs/equity-market-bbb.md` (Update 1, 17 Oct, amended 18 Oct, note 24 Oct); `docs/hy-market-bbb.md` (24 Oct, values as 5 Oct) | Scenarios, block F, Oslo exit P/E, P/B and mid-cycle return, index IRRs, I-44 path, HY reference; Sweden macro rows, Riksbank context, NIBOR | 17–24 Oct 2026 |
| S10 | **Handelsbanken interim report Jan–Sep 2026**, full PDF (Cision `mb.cision.com/Main/3555/4412599/4328910.pdf`) via `parse_pdf_to_text` | Q3 and 9M income statement, NII bridge (margins −194m), costs, credit losses, regulatory fees, volumes, segments, capital (CET1 17.0%, requirement 14.5%, PD models, AT1 6bn), equity statement, shares, anticipated dividends 8.02 (92%), next report 3 Feb 2027 `[F]` | 21 Oct 2026 |
| S11 | Handelsbanken Q3 headline release (Newsweb STHY; nasdaq_se) | Same headline figures; cross-check of S10 `[F]` | 21 Oct 2026 |
| S12 | Placera, Modular Finance consensus and SB1 Markets comment | Q3 consensus: operating profit 7,369, NII 10,178, fees 3,214, costs −5,878, credit losses −107; SEK 67bn of distributions over three years `[E]` | 19–21 Oct 2026 |

- **Quality notes:**
  - The Q3 PDF was read in its overview, capital, Sweden segment, key-metric and equity-statement
    pages. Notes 2–25 were not read. The figures match the Newsweb headline release.
  - Consensus is thin for quarters (2 analysts for Q4) and moderate for years (12 for CY27).
  - **Yahoo's CY26 consensus (11.47, 8 analysts) mixes reported and adjusted EPS.** 9M actual
    8.68 + Q4 2.95 = 11.63 reported, or 11.19 excluding the VAT refund. The model uses those two
    figures.
  - **Book value, raw and checked:**
    - raw: Yahoo 98.09 (total equity incl. AT1 ÷ shares);
    - checked: shareholders' equity SEK 188,216m ÷ 1,980.03m = **95.06**;
    - the company APM "adjusted equity per share" is 97.99;
    - version 2's 93.13 (30 Jun) included the AT1 (shareholders' 90.10).
  - The Yahoo SEK/NOK quote of 24 Oct (0.9384) is a weekend print with an inconsistent bid/ask.
    The 23 Oct close (0.9409) and the Norges Bank fixing (0.9403) are used.
  - FinancialFilings was unavailable (quota), so the share count rests on the Q3 report alone.
