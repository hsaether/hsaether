# Borr Drilling (BORR) — IAF analysis, 24 Oct 2026, news update 25 Oct 2026 (v3.1), price re-mark 7 Nov 2026 (v3.2) (stub Q4 2026 + 2027–2029)

**Version 3.2, 7 Nov 2026: price re-mark (change gate).** Skill revisions used: **iaf-valuation 2026-11-01.1** (v3.1 used 2026-10-18.2; the new revision changes no rule this Track B build uses), rig-market-bbb 2026-10-10.1, equity-market-bbb 2026-10-24.1 (read only).
- **Upstreams read:**
  - `docs/rig-market-bbb.md`, small update of 4 Nov. Only the UDW drillship stub and 2027 points moved (Base 400 → 420). The high-spec, SE Asia and Middle East jackup rates, MCU paths, mid-cycle and asset values this analysis reads are unchanged. The jackup stub MCU moved 87 → 88% (mechanical, the September count), but the stub here is built from booked days, so it does not enter. No Gulf suspension: Valaris says on 2 Nov that all its own and ARO's Middle East rigs stay under contract. Aramco extended five ARO rigs by 3 years, and KJO took Embracer for 4 years at $91.3k, in line with the Middle East Base row. **No cash flow changes.**
  - `docs/equity-market-bbb.md`, Update 2 of 6 Nov (read 18 Oct before). The Oslo exit P/E (10.5 / 11.5 / 12.5) is unchanged. The exit P/B is 1.48 / 1.74 / 1.95 (was 1.48 / 1.75 / 1.97), and the mid-cycle return is 8.0 / 8.9 / 9.2% (was 8.2 / 9.1 / 9.4%). The USD/NOK relative moves are unchanged (Bear +12 / +9 / +9%, Bull −3%); only the spot base moved. These enter the exit cross-check sensitivity and the NOK lines only, never the decision. The HY market reference (E / R 0.254) is not an input to this company screen.
  - `docs/hy-issuers.md`, 4 Nov. The 2032 and 2034 notes moved from Performing to **Watch**. They are derived at ~93 (91–96) from Heimdal's October contribution, with no observed quote. That is a credit signal only: the debt is fixed-rate with no maturity in the window, so no rate or refinancing input changes. It is consistent with the Base reading here (RCF exhausted in 2029).
- **Peers' Q3 reports (Valaris, Noble 26 Oct–2 Nov; Seadrill 3 Nov), as read by Rig BBB on 4 Nov:** they are mostly floater news. For jackups they show Gulf contract demand firming (ARO 5 × 3 years, Embracer) and no suspension. Jackup MCU was 88% in September (384 / 438). **No jackup row changed.**
- **Borr news since 25 Oct** (Newsweb and EDGAR 6-Ks of 26 Oct, 29 Oct and 2 Nov `[F]`):
  - Prospector 5: the bodies of four people have been recovered and one person is still missing.
  - A classification society has been engaged for an independent investigation. About 280 m³ of marine diesel was on board, and environmental measures are in place.
  - BW Energy's Q3 report (29 Oct, via `docs/hy-issuers.md` `[F]`): the MaBoMo Phase 2 campaign is delayed, and it is "too early to confirm when drilling will resume". No replacement Borr rig is named.
  - **Nothing on insurance, the contract, the notes or the Q3 date.** No 6-K after 2 Nov, and no Newsweb release after 2 Nov.
  - Q3 report: not announced. Yahoo gives 18 Nov (estimate); Zacks consensus is EPS −$0.11 (28 Oct).
- **What moved: the share price only.** It is **$3.24** at the NYSE close on 6 Nov (Yahoo), against $4.40 on 23 Oct: **−26%**. The path ran $3.96 on 26 Oct (the first session after the loss), $4.02 on 30 Oct, then $3.68 / $3.46 / $3.33 / $3.12 on 2–5 Nov, and back to $3.24 on 6 Nov. The 2–5 Nov slide came with the US sell-off of 5 Nov and the notes' fall to Watch. No company announcement explains it beyond the incident updates.
  - Oslo: NOK 31.29 (6 Nov, 15:25 UTC).
  - USD/NOK 9.4537 (Yahoo, last tick 7 Nov 05:21 UTC); Norges Bank fixing 9.4277 on 6 Nov `[F]`. The Yahoo bid/ask (9.19 / 9.22) is stale, so the fixing is the cross-check. P in NOK = 30.63.
  - Valuation date **7 Nov 2026**, T = **3.15 years** (1,150 days).
  - Shares: Yahoo shows 309.26m (+0.75m vs 308.51m at 30 Jun). No filing behind the change was found (probably share-based vesting `[?]`), so 308.51m is kept. The effect on Bull V_T is < $0.02.
- **Re-mark (cash flows and V_T unchanged; only P, the date and T move, and P_k moves by the date alone):**

| v3.1 → v3.2 | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T | −100% → −100% | **−100% → −100%** | 7.6% → **18.6%** |
| IRR_T in NOK on the Equity BBB NOK path | −100% | **−100%** (spot flat) | 6.5% → **17.5%** |
| P_k / margin of safety | $0 / −100% | **$0 / −100%** | $3.87 / −12.1% → **$3.88 / +19.9%** |
| Capital preserved? ($5.55 vs P) | No | **No** | Yes |
| Bull already priced, (P − P_k Base) / (P_k Bull − P_k Base) | — | — | 114% → **83%** |

- **Change gate.** No upstream value this document reads has moved, so the cash flows, V_T and every P_k are kept. The price moved by more than a fifth, so the IRRs are re-marked.
- **Verdict unchanged: fails.** The Base margin of safety stays −100% (V_T 0, P_k $0), and Bear still runs out of liquidity in 2028. **The Bull stress test flips from below k to above k** (18.6%). At $3.24 the price sits 17% below the Bull hurdle: it no longer prices the Bull case in full.
- **Other v3.2 Bull figures** `[A]`, from the v3.1 exit values at the new price and date:
  - Insurance $70m / $100m / $130m: 20.5% / 21.3% / 22.0% (P_k $4.08 / $4.16 / $4.25).
  - With the reversion tail: 19.8%. With firm-today contracts only: 17.7%.
  - Exit marks re-discounted at Oslo's Bull mid-cycle return, now 9.2% (was 9.4%): V_T ~$4.69, IRR ~12.4%, just above k.
  - Structural ~15.6%, cyclical ~+3.0 pp. Re-rating +17.0% a year (P/NAV_0 0.61x), NAV growth +1.4% a year.
  - Scenario-weighted reference (convention): IRR −23.6%, P_k $0.97.
  - EV ≈ $3.34bn (market cap $1.00bn + net debt ~$2,336m).
- **Break-even mid-cycle** (Base cash flows, 12% to 2029): about **~$139k** on Rig BBB's basis (was ~$146k), interpolated from the section 9 sensitivity `[A]`. That is still above Rig BBB Bull ($130k).
- **Stale after 18 Nov 2026** (Borr Q3 report, Yahoo estimate; not announced). Update earlier on a Borr statement on insurance or the BW contract, a Q3 invitation with an earlier date, or the full Rig BBB update due by 9 Nov if it changes the jackup rows. Sections 1–11 below are v3.1, except where marked v3.2.

> **4 Nov 2026, kept unchanged (change gate):** read Rig Market BBB small update of 4 Nov: the high-spec jackup, Middle East and SE Asia rows and rig values this analysis reads are unchanged (only the UDW drillship 2027 point moved); no Gulf suspension. No figure in this document changes.

**Version 3.1, 25 Oct 2026: news update, Prospector 5 lost.** Skill revisions used: iaf-valuation 2026-10-18.2 and rig-market-bbb 2026-10-10.1 (both unchanged since v3); no upstream document was re-read for new values.
- **Event** (BW Energy's stock-exchange release of 25 Oct `[F]`; Borr's statement of 25 Oct as carried by Reuters and Energy-Pedia, "Source: Borr Drilling" `[E]`; Borr's own release was not found on EDGAR (latest 6-K 16 Oct) or via search for Newsweb): the jackup **Prospector 5** (2014 F&G JU-2000E, owned and operated by Borr) sank on the Dussafu Marin licence offshore Gabon at about 20:37 local time on Sat 24 Oct 2026. It was jacking up ahead of BW Energy's MaBoMo Phase 2 infill campaign (four wells). Borr's preliminary information is a punch-through during preload, then loss of stability; the cause is not confirmed and is under investigation.
- **People:** 115 on board; 110 accounted for; **five people remain missing** and search and rescue was ongoing on 25 Oct. Borr's emergency response team is working with the local authorities and BW Energy. No later update was found.
- **Client:** BW Energy shut MaBoMo production as standard procedure; no damage to the facility and no discharge reported `[F]`. Neither company has said anything on the contract, a replacement rig or the rest of the campaign `[?]`. The contract was an LOA of Apr 2026: four wells, at least 320 days firm, 220 days of options `[E]`; the model had it firm to Jul 2027.
- **Insurance** `[?]`: neither statement mentions it. Borr's 20-F (FY2025) `[F]`: hull and machinery cover for the whole fleet "reflects its agreed value when the insurance is placed", subject to a deductible; P&I covers third-party liabilities including personal injury and death and wreck removal. No loss-of-hire cover is described, so none is assumed `[A]`. The agreed value of Prospector 5 is not disclosed.
- **Collateral** `[F/?]`: the 2032 and 2034 notes are "secured on a senior basis by most of the rigs" (H1 2026 report). At end-2025 all 24 rigs then owned, Prospector 5 among them, secured the old notes (20-F). So Prospector 5 is very probably note collateral `[A]`. The indenture's terms on a total loss (reinvest the proceeds or offer them to noteholders) were not found `[?]`.
- **Model change (minimum change; only the rig is removed):** fleet 29 → 28 rigs. Its backlog to Jul 2027 and its open days to 2029 are taken out of the cash flows (Base EBITDA −$4m in Q4-26, −$17m in 2027, −$15m in 2028, −$16m in 2029; with interest, Base net debt +$45m at exit). Its exit value is removed (Base $58m, Bull $121m, Bear $10m), together with its share of the backlog-at-exit premium and the reversion tail. **No insurance proceeds in the decision figures**, because no source gives a value or a timing. They are shown as a sensitivity below. Incident costs (deductible, search and rescue, legal) are not modelled `[?]`.
- **Price:** still $4.40 (Fri 23 Oct close). The market has not priced the event; it opens Mon 26 Oct. Valuation date 25 Oct, T = 3.19 years (1,163 days).

| v3 → v3.1 (no insurance) | Bear | **Base** | Bull |
|---|---|---|---|
| Equity at exit, $m | −2,817 → −2,844 | **−506 → −615** | 1,904 → 1,713 |
| V_T per share | 0 → 0 | **0 → 0** | $6.17 → **$5.55** |
| IRR_T | −100% → −100% | **−100% → −100%** | 11.2% → **7.6%** |
| P_k / margin of safety | $0 → $0 | **$0 → $0 (−100%)** | $4.30 → **$3.87 (−12.1%)** |
| Net debt at exit, $m | 3,039 → 3,056 before new money | **2,376 → 2,421** | 1,904 → 1,969 |
| Balance sheet | Liquidity still gone in 2028; funding gap $658m → ~$675m by 2029 | **RCF fully drawn in 2029, ~$40m gap** (was $245m of $250m) | Net debt $1.97bn at exit |

| Insurance sensitivity (agreed value `[?]`; received mid-2027; reduces net debt; ×1.22 at exit for interest saved at ~8.9% `[A]`) | Bull V_T / IRR_T / P_k | Base | Bear |
|---|---|---|---|
| None (decision) | $5.55 / 7.6% / $3.87 | 0 | 0; gap ~$675m |
| $70m (≈ Noble transaction level a rig) | $5.83 / 9.2% / $4.06 | 0 | 0 |
| $100m (≈ average book value a rig, $105m at 30 Jun) | $5.95 / 9.9% / $4.15 | 0 | 0; gap ~$550m if the cash is kept, unchanged if offered to noteholders |
| $130m | $6.07 / 10.6% / $4.23 | 0 | 0 |
| Needed to restore v3 Bull (11.2%) | ~$156m | Base equity needs +$615m: not reachable | — |

- **Change gate.** The verdict does not move: **fails**. Base stays at zero (V_T 0, P_k $0), and the loss widens the exit deficit by $109m. Bear stays at zero and still runs out of liquidity in 2028; with insurance cash kept, the run-out comes about a quarter later `[A]`. **Bull moves beyond the minimum change: IRR 11.2% → 7.6%, P_k $4.30 → $3.87, margin −2.3% → −12.1%** with no insurance. Even at a $130m insured value Bull stays below k (10.6%). The rig's Bull exit value plus its 2027–29 earnings ($186m) exceeds any plausible insured value.
- **Other v3.1 figures** `[A]`, scaled from the v3 build:
  - NAV_0: Base −$0.85, Bear −$5.46, Bull $5.32 (P/NAV_0 0.83x; re-rating +6.1% a year, NAV growth +1.3% a year). NAV at market marks ~$0.35, before any insurance receivable.
  - Bull: IRR in NOK on the Equity BBB path 6.5%; structural ~4.8%, cyclical ~+2.8 pp; with the reversion tail 8.6%; with firm-today contracts only 6.7%; with exit marks at Oslo's 9.4% ~1.0%.
  - Break-even mid-cycle ~$146k (Rig BBB basis; ~$145k at $100m insured), was ~$144k.
  - Scenario-weighted reference (convention): IRR −30.4%, P_k $0.97. Bull already priced: 114%.
- **Non-financial signposts** (sources only; no speculation):
  - The outcome of the search for the five missing people.
  - The investigation into the punch-through, by Borr and the Gabonese authorities.
  - BW Energy's choice for the rest of the MaBoMo Phase 2 campaign (a replacement rig, a Borr rig or another contractor), expected at the latest with its Q3 report on 29 Oct `[E]`.
  - Any client or regulatory review of Borr's preload procedures elsewhere.
  - The insurers' acceptance of a total-loss claim and its timing.
- **Stale after 9 Nov 2026** (unchanged). Update earlier on any of these: Borr's next statement on Prospector 5 (search outcome, insurance, contract), the 26 Oct opening price, BW Energy's Q3 report (29 Oct), or Borr's Q3 report (not announced; 4–18 Nov expected).

Skill revisions used (v3): **iaf-valuation 2026-10-18.2** (backlog at exit, exit-consistency test, exit cross-check against Equity BBB, Bear/Bull in NOK on the Equity BBB path, holdco G&A outside NAV), **rig-market-bbb 2026-10-10.1** (the 10 Oct baseline was built under 2026-10-08.2; small updates 13, 17 and 22 Oct under 2026-10-10.1), **equity-market-bbb 2026-10-24.1** (exit reference and NOK path read only). Sector inputs:
- `docs/rig-market-bbb.md`: baseline 10 Oct 2026 (Final, stale after 9 Nov), small updates 13, 17 and 22 Oct with paths unchanged. The jackup rows (high-spec, SE Asia, Middle East), MCU, mid-cycle, asset values and the asset-value convention are identical to the 4 Oct baseline with the 8 Oct method revision used on 8 Oct. Rows are used directly; no own rig forecast.
- `docs/oil-market-bbb.md`: baseline 24 Oct 2026 (Final, stale after 23 Nov), kept unchanged; the last value change was 17 Oct (Brent Base 2027 85 → 88, mid-cycle unchanged). Background only, through Rig BBB's scenario mapping; Rig BBB (17 Oct) asks for no rig change for oil reasons.
- `docs/equity-market-bbb.md`: 17 Oct 2026, amended 18 Oct (stale after 10 Nov). Oslo exit P/E, exit P/B and mid-cycle return for the exit cross-check, and the USD/NOK path for the Bear/Bull NOK figures. Nothing else is taken from it.
- `docs/hy-market-bbb.md`: not used for a rate path. Borr's debt is fixed-rate USD with no maturity inside the horizon except a $44m convertible in Feb 2028.
- **Stale after 9 Nov 2026** (Rig BBB stale date). Re-run earlier at the Q3 report and fleet status (not yet announced; 4–18 Nov expected), at a Rig BBB change to the jackup rows, or on a Gulf suspension notice. Oldest input: Q2 accounts (30 Jun 2026); price 23 Oct close.

**What changed vs 8 Oct (version 2.1):**
- **Change gate: nothing upstream moves a decision figure.** The jackup rows did not change after 4 Oct, and the oil change (Brent Base 2027 +$3) is background only. Rig BBB's 10 Oct note on the regional jackup reading was tested: Borr's documented premium holds and the difference is below the 5% minimum change (section 5). Cash flows, EBITDA and net debt are unchanged.
- **Price $4.635 → $4.40** (23 Oct close), valuation date 8 → 24 Oct, T 3.23 → 3.19 years.
- **Current method applied:** backlog at exit, the exit-consistency test, the exit cross-check and the NOK path. Holdco G&A was already outside NAV.
- **Result:** Base and Bear unchanged (V_T 0, IRR −100%, P_k $0). **Bull IRR 8.3% → 11.2%** (price and date +2.0 pp, backlog at exit +0.9 pp), Bull P_k $4.16 → $4.30, margin −10% → −2.3%. **Verdict unchanged: fails.**

## Summary

**Verdict: fails, and the Base case leaves no equity value.** v3.1 (25 Oct): Prospector 5 lost, fleet 28 rigs, no insurance in the figures. **v3.2 (7 Nov), price $3.24 (−26%): Base and Bear unchanged at zero; Bull 18.6% (P_k $3.88, margin +19.9%), now above k.** The bullets below are at the v3.1 price ($4.40) unless marked.
- **Base:**
  - At Rig BBB's Base mid-cycle ($110k a day for high-spec jackups, plus Borr's 8% premium) on the harmonised rig-value convention, the **28 rigs** are worth **$1.73bn at end-2029** against **$2.42bn of net debt**.
  - The backlog at exit (+$39m) and the reversion tail (+$35m) shrink the gap to −$0.62bn. Equity value is still nil: IRR_T −100% and P_k $0, against a price of $4.40.
- **Bull** (mid-cycle $130k) returns **7.6%** (v3 11.2%), below k = 12%. The price is 14% above the Bull hurdle ($3.87).
  - With $100m of insurance proceeds it is 9.9% (sensitivity); with a reversion tail on the Bull exit 8.6%.
  - The exit cross-check makes the Bull exit look generous: a buyer at NAV earns ~7.5% on the levered equity against Oslo's 9.4%. At 9.4% Bull falls to ~1%.
- **Bear:** EBITDA cannot cover the 9% coupons and the 5% amortisation, and liquidity runs out in 2028.
- **What the price needs:**
  - A through-life jackup rate of **~$146k on Rig BBB's basis** (v3 ~$144k; ≈ $158k for Borr after its premium) to earn 12% to 2029. That is above Rig BBB Bull ($130k).
  - Today's EV ($3.70bn) capitalises ~$138k (Borr pure rate, ≈ $128k on Rig BBB's basis) on the same convention (v3, 29 rigs; with 28 rigs and no insurance it is a little higher a rig, not re-run).
- **Market signals (not an IAF input; section 11):**
  - Founder and director Tor Olav Trøim has bought **~13.8m shares (~$63m) in 2026**, of which ~8.0m ($37m) between 6 and 15 Oct at $4.24–4.93.
  - Short interest rose to **34.5m shares (30 Sep; 14.5% of float)**, part of it probably hedging of the April convertible.
  - Trøim is in effect buying the Bull case, which the price already reflects.
- **Why:**
  - At Base mid-cycle a Borr rig generates ~$7m a year of rig-level free cash after idle time, tax and maintenance capex. Across 28 rigs that is ~$198m a year, against ~$195m of interest and ~$59m of G&A.
  - Base FCF is therefore about zero. Net debt never falls, and three years of ageing take $0.17bn off the fleet.

**Decision table** (v3.2 at $3.24, 7 Nov; 28 rigs, no insurance; v3.1 at $4.40 in brackets where it moved)

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (7 Nov 2026 → 31 Dec 2029) | −100% | **−100%** | **+18.6%** (7.6%) |
| IRR_T in NOK on the Equity BBB NOK path | −100% | **−100%** (spot flat) | +17.5% (6.5%) |
| V_T per share (equity at exit) | 0 (−$2.84bn before new money) | **0 (−$0.62bn)** | **$5.55** ($1.71bn; v3 $6.17) |
| P_k (hurdle price) / margin of safety | $0 / −100% | **$0 / −100%** | **$3.88 / +19.9%** ($3.87 / −12.1%) |
| Capital preserved? (ΣD_t + V_T vs $3.24) | No | **No** | Yes |
| Cumulative maintenance FCF per share, Q4-26 to 2029 | −$2.30 (−$2.25) | **−$0.25** (−$0.10) | +$1.22 (+$1.43) |
| Net debt per share at exit | $9.90 before new money | **$7.85** (7.70) | $6.38 (6.17) |
| Balance sheet | Liquidity gone in 2028; funding gap ~$675m by 2029 | **RCF fully drawn in 2029, ~$40m gap** (v3 $245m of $250m) | Net debt falls to $1.97bn |

**Per-share path** ($ per share, 308.5m shares; no distributions in any scenario; v3.1 without Prospector 5 from 24 Oct)

| | Q3-26E | Q4-26E | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| **Base** EBITDA, $m | 83.4 | 79.8 | 262.3 | 303.4 | 303.1 |
| EBITDA per share | 0.27 | 0.26 | 0.85 | 0.98 | 0.98 |
| **Maintenance FCF per share** | **0.02** | **0.01** | **−0.21** | **−0.02** | **−0.03** |
| Debt amortisation per share (incl. 2.5% premium; 2028 incl. convertible) | 0 | 0 | 0.17 | 0.48 | 0.34 |
| FCF after debt service per share | 0.02 | 0.01 | −0.38 | −0.50 | −0.37 |
| RCF drawn at period end, $m | 0 | 0 | 23 | 178 | 250 + ~40 gap |
| Net debt per share, period end | 7.58 | 7.57 | 7.79 | 7.81 | 7.85 |
| V_t per share, year end | — | 0.13 | 0 | 0 | **0** |
| **Bear** maintenance FCF per share | 0.02 | 0.01 | −0.45 | −0.83 | −1.03 |
| Bear V_t per share | — | 0.13 | 0 | 0 | 0 |
| **Bull** maintenance FCF per share | 0.02 | 0.01 | 0.08 | 0.46 | 0.67 |
| Bull V_t per share | — | 0.13 | 1.38 | 3.49 | 5.55 |

- **Maintenance FCF** = EBITDA − tax − interest − maintenance capex, before debt amortisation (Step 2B). Q3-26 ended before the valuation date and is not yet reported, so it sits in today's net debt.
- **V_t at end-2026** marks the rigs at the Noble transaction level (identical in all scenarios). At that level the equity is worth $0.13/share without an insurance receivable (v3 $0.39 with Prospector 5). Bull interim marks for 2027–28 are scaled from v3 `[A]`.

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value · `[E]` external or secondary · `[C]` carried from an earlier version or another workspace document · `[A]` own assumption · `[?]` not found.

## 1. Header

| Item | Value |
|---|---|
| Company | Borr Drilling Limited (Bermuda). Primary listing NYSE: BORR; Euronext Oslo: BORR (main market since 21 May 2026). Reports in USD, US GAAP |
| Price (P), v3.2 | **$3.24**, NYSE close 6 Nov 2026 21:00 UTC (Yahoo; previous close $3.12). Oslo NOK 31.29 (6 Nov 15:25 UTC). USD/NOK 9.4537 (Yahoo, 7 Nov 05:21 UTC); Norges Bank fixing 6 Nov 9.4277 `[F]`. Valuation date 7 Nov 2026, T = 3.15 years (1,150 days). Market cap $1.00bn; EV ≈ $3.34bn; P/NAV at market marks ~9.3x (NAV ~$0.35) |
| Price (P), v3.1 | **$4.40**, NYSE close 23 Oct 2026 20:00 UTC (Yahoo; previous close $4.08, +7.8% on the day). Oslo cross-check: NOK 39.85 (14:25 UTC) ÷ 9.331 = $4.27, before the US afternoon rally |
| FX | **USD/NOK 9.316** (Yahoo NOK=X, 23 Oct 20:00 UTC, the price time stamp). Norges Bank fixing 23 Oct 9.3509 (14:15 CET) `[F]`. P in NOK = 40.99 |
| Valuation / exit date | 25 Oct 2026 (v3.1; v3 24 Oct) / 31 Dec 2029, **T = 3.19 years** (1,163 days). The price predates the loss of Prospector 5 (markets closed until 26 Oct) |
| Shares | **308.51m** outstanding (30 Jun 2026 `[F]`; Yahoo 23 Oct 308,512,741). No share issue: the EDGAR 6-K list to 16 Oct shows none. Convertibles are out of the money and treated as debt: 2033 notes at $8.00 (37.5m shares), 2028 bonds at $6.94 (6.4m) `[F]`; conversion is modelled only where V_t > $8.00 (does not occur) |
| Market cap / EV | $1.36bn; net debt 30 Sep (model) **$2,339m** (debt principal $2,529m − cash; ~$2,337m at 24 Oct) → EV ≈ **$3.70bn**. EV / 2026E EBITDA ($300m) = 12.3x |
| NAV at today's market marks | **$0.60/share (P/NAV 7.3x)**: rigs at the rate implied by Noble's $72m sale (~$123k, convention) $2.33bn + firm-contract premium $0.16bn + JV $0.04bn − net debt `[C]`; 16 days of ageing change it by < $0.01 |
| NAV_0 (Base mid-cycle marks) | v3: **−$0.62/share** (n.m.; rigs $1,954m + firm premium $193m − net debt $2,339m); Bear −$5.42; Bull $5.78 (P/NAV_0 0.76x). **v3.1 without Prospector 5 and before any insurance receivable** `[A]`: Base −$0.85, Bear −$5.46, Bull $5.32 (0.83x); NAV at market marks ~$0.35 |
| Track / k | **Track B** (short contracts into a cyclical rate path, finite-life rigs, high leverage). **k = 12%**; a leverage add-on would not change a P_k of zero |
| Distributions | None in any scenario: last paid $0.02 in Mar 2025; the 2032/2034 note indenture restricts payments `[F]`; Base FCF leaves nothing to pay. Retained cash reaches V_t through net debt |

**Sources:**
- **SEC EDGAR 6-K filings** (FinancialFilings has used its monthly quota until 1 Nov; Nordic Financial Newsweb has no Borr announcement after 30 Sep):
  - Q2 2026 results (11 Aug) and the Fleet Status Report of 11 Aug.
  - H1 2026 interim report with notes (12 Aug) and the Q2 presentation (12 Aug).
  - Releases of 15 Sep (Mexico, Odin/Idun/Bestla) and 30 Sep (Norve/Natt/Joro).
  - Since 8 Oct: one 6-K, filed 16 Oct, dated 16 Sep (the Pareto conference investor presentation). Nothing new on contracts, fleet status or financing.
- **Alpha Vantage:** Q2 call transcript (12 Aug) `[C]`.
- **Yahoo (23 Oct):** quotes, FX, consensus, insider module, short interest (30 Sep).
- **Zacks (24 Oct):** expected report date, broker ratings and targets (market check only).
- **Norges Bank API:** USD fixing 23 Oct.
- **Workspace:** `docs/PLSV-analysis.md` for the Fontis seller-credit terms and JV rig build years `[C]`.

## 2. Scenarios (from Rig Market BBB, 10 Oct; jackup rows unchanged since 4 Oct)

| Scenario | Catalyst | Rig BBB rows used (2027 / 2028 / 2029; mid-cycle) | What it does to Borr |
|---|---|---|---|
| **Base** (decision) | NOC-led demand converts gradually; Gulf jackups return gradually | High-spec 105 / 115 / 120; mid 110. SE Asia 90 / 95 / 98. Middle East 90 / 95 / 100. MCU 89 / 91 / 91% | Rolling contracts re-price from ~$128k to $97–130k; fleet ~83% working in 2027, ~88% in 2028–29; stacked rigs back from Jul 2027 |
| **Bear** (stress) | Oil Bear (Iran–USA deal + OPEC+ share fight) and Gulf rigs idled by war move to Asia | High-spec 92 / 88 / 85; mid 92. SE Asia 72 / 70 / 70 | Re-pricing into $76–99k; fleet 67–73% working; stacked rigs stay stacked to 2029 |
| **Bull** (stress) | 2H26 FIDs and NOC programmes convert; Aramco/KJO absorb the Gulf rigs | High-spec 118 / 135 / 145; mid 130. MCU 92 / 94 / 95% | Stacked rigs back from Apr 2027; fleet ~91% working; EBITDA $479m (2028), $548m (2029) |

- The stub is identical in all scenarios.
- Middle East Bear/Bull and SE Asia Bear/Bull mid-cycle are scaled from the high-spec ratios `[A]` (Rig BBB has Base only).

## 3. Company and status

- **Fleet:** **28 wholly owned jackups** since the loss of Prospector 5 on 24 Oct 2026 (29 before), built 2008–2024 (average build year 2016), plus 50% of five ex-Fontis jackups in Mexico (BC Ventures, since 29 Jul 2026) `[F]`. Five rigs (Bestla, Joro, Sif, Forseti, Freyja) were bought from Noble for **$360m** in Jan 2026 `[F]`.
- **Q2 2026** `[F]`:
  - Revenue $232.3m; adjusted EBITDA **$43.8m** (Q1 $88.5m), hit by the Odin start-up ($22.5m), six rigs between contracts, Middle East insurance and fuel (+$7.3m) and $10.8m of credit losses.
  - Technical utilisation 98.4%, economic 96.4%. Book equity $961.6m at 30 Jun; depreciation $43.5m in Q2.
  - Q3 guidance: ~23 active rigs; adjusted EBITDA to "improve significantly" from Q2.
- **Contracting:** 2026 coverage 73% at ~$134k `[F]`. YTD: 21 commitments, ~4,350 days, $541m (**~$123k average** incl. mobilisation fees; ~207 days a commitment) `[F]`. Backlog $1.13bn (11 Aug) ÷ ~8,440 firm days → **$122–134k** `[B]`.
- **Since Q2** `[F]`:
  - Odin earning in the US Gulf from 11 Sep.
  - Idun 130-day follow-on in Vietnam.
  - Bestla: Eni option to Sep 2027 (+9 months priced option).
  - Norve LOA mid-Dec 2026 to Aug 2027 (+175 days of options).
  - Natt option exercised to Aug 2027; Joro 60 days of UK accommodation.
  - The 51% of Perfomex is being sold to the Mexican partner at book value. Galar, Gersemi and Njord move to bareboat with "largely unchanged" economics.
- **Since 8 Oct:** no contract, fleet-status or financing announcement (Newsweb, EDGAR, Zacks news to 24 Oct). Insider purchases continued (section 11). The status of the rigs rolling off in Oct–Nov (Sif, Vali, Grid, Skald, Mist) is not known until the Q3 fleet status report `[?]`.
- **Debt at 30 Jun 2026** `[F]`, principal **$2,529.2m**:
  - $1,100m 8.75% notes due Jan 2032 and $935m 9.00% notes due Jan 2034. Both amortise 5% of original principal a year ($101.75m, at 102.5%) from Jul 2027.
  - $300m 3.5% convertible notes 2033 and $44.2m 5% convertible bonds due Feb 2028.
  - $150m Noble seller's credit at 7.5%, stepping up to 15% by Feb 2031, due Jan 2032.
  - Undrawn $250m RCF to 2031. Cash $223.6m.
- **Fontis JV** `[F/C]`: $287m for five rigs (built 2007, 2007, 2008, 2013, 2014). Financed by a **$237m non-recourse seller credit** (10/12/14%, due ~Jan 2029) plus $25m equity from each partner; Borr also provides a ~$15m shareholder loan. Three of the five rigs are contracted.

### Fleet and firm cover (fleet status as of 8 Oct 2026; no update published since)

| Rig | Built | Region (Rig BBB row) | Customer / status | Firm to |
|---|---|---|---|---|
| Arabia I | 2020 | Brazil (high-spec) | Petrobras (charter) | Apr 2029 |
| Arabia II | 2019 | UAE (Middle East) | Bunduq | Jan 2027 |
| Arabia III | 2013 | Saudi (Middle East) | Saudi Aramco | Sep 2028 |
| Bestla | 2008 | Netherlands (high-spec) | Eni (Noble bareboat to Dec 2026) | Sep 2027 (+9-month option) |
| Forseti | 2013 | UAE (Middle East) | Noble bareboat | Dec 2026 |
| Galar, Gersemi | 2017, 2018 | Mexico (high-spec) | PEMEX via partner (bareboat) | May 2030 |
| Njord | 2019 | Mexico (high-spec) | PEMEX via partner | Apr 2028 |
| Gerd | 2018 | Ivory Coast (high-spec) | Foxtrot | Mar 2027 |
| Grid | 2018 | Angola (high-spec) | Halliburton | Nov 2026 (option) |
| Natt | 2018 | Nigeria (high-spec) | Shell | early Aug 2027 |
| Norve | 2011 | West Africa (high-spec) | idle Oct–mid-Dec; LOA | Aug 2027 (+175 days options) |
| Prospector 1 | 2013 | Netherlands (high-spec) | ONE-Dyas | Apr 2027 (+210 days options) |
| ~~Prospector 5~~ | 2014 | Gabon (high-spec) | BW Energy (LOA: 4 wells, ≥ 320 days, 220 days options `[E]`) | **Sank 24 Oct 2026 while preloading at Dussafu; removed from the model in v3.1** (was firm to Jul 2027) |
| Odin | 2013 | US Gulf (high-spec) | undisclosed → Cantium | Dec 2026; Feb–Jul 2027 |
| Ran | 2013 | Mexico (high-spec) | Eni contract ended Sep 2026 | open `[?]` |
| Sif | 2013 | Suriname (high-spec) | Petronas | Oct 2026 |
| Gunnlod | 2018 | Vietnam (SE Asia) | PVEP-NCS | Apr 2027 (+~110 days options) |
| Idun | 2013 | Vietnam (SE Asia) | HLHV → undisclosed | ~Mar 2027 |
| Mist | 2013 | Malaysia (SE Asia) | Sarawak Shell | Nov 2026 |
| Saga | 2018 | Brunei (SE Asia) | Brunei Shell | Apr 2027 |
| Skald | 2018 | Malaysia (SE Asia) | Vestigo | Nov 2026 (option) |
| Thor | 2019 | Vietnam (SE Asia) | PVEP-Cuulong → undisclosed | Apr 2027 |
| Vali | 2024 | Libya (Middle East) | Mellitah | Oct 2026 (option) |
| Joro | 2008 | UK (high-spec) | accommodation | mid-Dec 2026 (+56 days options) |
| Freyja, Var | 2014, 2024 | Singapore (SE Asia) | warm stacked | — |
| Groa | 2018 | UAE (Middle East) | warm stacked | — |
| Hild | 2020 | Mexico (high-spec) | warm stacked | — |

Firm (incl. LOA) share of fleet rig-days in the model: Q4-26 71% · 2027 39% · 2028 16% · 2029 8%.

## 4. Near term: stub (all scenarios)

| | Q3-26E (ended, unreported) | Q4-26E |
|---|---|---|
| Average working rigs | 22.5 (guidance ~23) | 22.8 |
| Firm share of working days | 100% | 90% (open days on Ran, Sif, Vali, Grid, Skald at 50% earning `[A]`) |
| Revenue, $m (consensus, Yahoo 23 Oct) | 254.9 (260; 6 analysts) | 248.6 (249; 5 analysts) |
| Adjusted EBITDA, $m | **83.4** (incl. Odin start-up $7.5m, Middle East insurance $2m) | **83.9** |
| Maintenance FCF, $m / per share | 6.4 / 0.02 | 7.3 / 0.02 |
| Net debt, end of quarter, $m | 2,339 | **2,332** |

- Consensus EPS is −$0.09 for Q3 (4 analysts; −$0.07 a week earlier) and −$0.08 for Q4. Q3 implies EBITDA of ~$80m `[A]`, in line with the model. FY27 EPS consensus is $0.04 (7 analysts; $0.08 a week ago, $0.32 90 days ago). Market check only.
- **Net debt bridge, $m:** 30 Jun 2,305.6 + JV equity 25 + JV loan 15 − Q3 MFCF 6.4 = 2,339.2 at 30 Sep; − Q4 MFCF 7.3 = **2,331.9 at 31 Dec**. Interest is accrued; the ~$110m coupon on 15 Jan 2027 moves cash, not this measure.
- **Dates:**
  - **Q3 report: not announced** as of 24 Oct (no invitation on Newsweb or EDGAR; the Q2 invitation came 27 days ahead). Zacks expects 4 Nov, Yahoo 18 Nov (both estimates `[E]`); Q3 2025 was reported on 5 Nov 2025 `[F]`.
  - Transocean Q3 and fleet status 2 Nov; OPEC+ 1 Nov; US midterms 3 Nov; Rig BBB stale 9 Nov; Equity BBB stale 10 Nov; Oil BBB stale 23 Nov.
  - First note amortisation 15 Jul 2027.

## 5. Market input and assumptions

**Rates for open rig-days** (Rig BBB rows × Borr premium +8%; work starting in that year):

| $k/day | Stub | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| High-spec jackups, Bear / Base / Bull | 105 | 92 / **105** / 118 | 88 / **115** / 135 | 85 / **120** / 145 | 92 / **110** / 130 |
| SE Asia jackups | 90 | 72 / **90** / 98 | 70 / **95** / 108 | 70 / **98** / 115 | 77 `[A]` / **92** / 109 `[A]` |
| Middle East jackups | 90 | 79 `[A]` / **90** / 101 `[A]` | 73 / **95** / 112 | 71 / **100** / 121 | 79 / **95** / 112 `[A]` |
| High-spec MCU % | 87 | 84 / **89** / 92 | 82 / **91** / 94 | 81 / **91** / 95 | 82 / **88** / 92 |

All rows are identical in the 10 Oct baseline and its 13, 17 and 22 Oct updates.

**Regional reading check (Rig BBB 10 Oct, "For IAF"):**
- Rig BBB says the composite high-spec row ($105k for 2027) is ~10% above the benign-region level (~$95k, Westwood 2026 YTD excluding Norway and Australia). Borr's rigs in Mexico, West Africa, the US Gulf and Suriname use the composite × 1.08 = $113k for 2027 starts. Rig BBB asks to re-check these, or to document the premium.
- **The premium is documented by Borr's own prints.** Its 2026 awards average ~$123k incl. mobilisation `[F]` and its 2026 cover runs at ~$134k `[F]`, mostly in benign regions, against the benign-region ~$94k `[E, via Rig BBB]`. That is +31% incl. mobilisation, about +15–20% ex-mobilisation `[A]`.
- $95k × 1.15 = $109k is 4% below the model's $113k, below Rig BBB's 5% minimum change. **Cash flows kept.**
- If the strict $95k × 1.08 were used, Base would not change (V_T is already nil). Bull V_T would fall by about $0.1–0.3 a share `[A]`.

| Assumption | Value | Basis |
|---|---|---|
| Borr premium on Rig BBB rows | +8% on open-day rates and exit values | YTD awards $123k vs the leading-edge median $106k (+16%), halved for mobilisation fees and the dayrate-equivalent basis `[A, anchored B]`; vs the benign-region level see the check above |
| Booked rate | ~$128k pre-August backlog; $120k post-August awards; Joro $80k | Backlog ÷ firm days `[B]`; rates not disclosed `[A]` |
| Open-day utilisation | Row MCU − 5 pp; stacked rigs from Jul 2027 (Base), Apr 2027 (Bull), Jan 2029 (Bear), $5m each to reactivate | Active-fleet coverage ~87% vs modern MCU 90–92% `[F/A]` |
| Revenue efficiency / opex | 96% / $63k per working day (2026, +3% a year; blended incl. bareboat rigs) | Q2 96.4% `[F]`; calibrated to Q1-26 accounts `[F/A]` |
| Idle cost | $30k a day warm (+3%); Bear long-stacked $12k | `[A]` |
| G&A (holding company) | $54m (2026 run-rate), $56m / $57.5m / $59m | Q1–Q2 `[F]`. One reported line, treated as holding company `[A]`: in the cash flows as paid, never in NAV. The convention's $75k rig opex is taken to include onshore rig support `[A]` |
| Tax / maintenance capex | 4.5% of revenue / $65m, $70m, $75m (2027–29) | H1 cash tax `[F]`; $2–2.5m a rig guidance `[F]` |
| Interest | Notes 8.87% on outstanding; convertibles 3.5% / 5%; Noble credit 7.5% → 10.5% (cash); RCF fee ~$3m | `[F]`; step-ups `[A]` |
| Liquidity | $100m minimum cash; RCF drawn first; any further gap shown as a funding gap | `[A]` |
| JV | Seller credit flat at $237m, refinanced at par in Base/Bull; Borr's stake = 50% × (rigs − debt) + $15m loan, floored at zero (non-recourse) | `[A]` |
| Backlog at exit (new) | Rig-days under contracts the scenario has signed: 2030 = 0.50 × and 2031 = 0.20 × the 2029 working share (Bear 39% / 16%, Base 44% / 17%, Bull 46% / 18%) of the 27 rigs not firm today, at the 2029 row rate | Shape of Borr's own book on 8 Oct (cover 39% / 16% of rig-days one and two years out at a 78.5% working share) `[B/A]`; Rig BBB gives no typical term for the row |

**Mark-to-market:** Base 2027 starts re-price at $97–113k against a ~$128k book, i.e. **−15–25% on every rolling contract**. Base 2027 EBITDA is $280m against a consensus-implied ~$450m.

## 6. Period tables ($m and per share; unchanged from 8 Oct)

**v3.1:** the tables below are the v3 build with 29 rigs. Removing Prospector 5 changes them as follows ($m; no insurance; interest at ~8% on the extra debt `[A]`). All other lines are unchanged.

| Δ v3.1 vs v3 | Q4-26E (from 24 Oct) | 2027 | 2028 | 2029 | Σ |
|---|---|---|---|---|---|
| Base EBITDA | −4.1 | −17.2 (contract to Jul at ~$128k, then open) | −14.9 | −15.8 | −52.0 |
| Base maintenance FCF (after tax, capex, interest) | −3.2 | −14.0 | −13.1 | −14.9 | −45.2 |
| Bear maintenance FCF | −3.2 | −10.8 | −2.0 | −0.7 | −16.7 |
| Bull maintenance FCF | −3.2 | −15.8 | −20.5 | −25.2 | −64.7 |

### Base (decision case)

| | Q3-26E | Q4-26E | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|
| Fleet working share | 77.7% | 78.5% | 79.8% | 76.2% | 89.1% | 88.3% | 88.3% | 87.3% |
| Revenue | 254.9 | 248.6 | 237.0 | 221.9 | 253.7 | 250.1 | 1,041.5 | 1,058.1 |
| Rig opex + idle cost | 148.5 | 149.2 | 151.5 | 149.9 | 163.3 | 162.5 | 665.8 | 680.2 |
| G&A and one-offs | 23.0 | 15.5 | 14.0 | 14.0 | 14.0 | 14.0 | 57.5 | 59.0 |
| **Adjusted EBITDA** | **83.4** | **83.9** | **71.6** | **58.0** | **76.4** | **73.5** | **318.3** | **318.9** |
| Tax | 11.5 | 11.2 | 10.7 | 10.0 | 11.4 | 11.3 | 46.9 | 47.6 |
| Interest (accrued, net) | 50.5 | 50.4 | 50.7 | 50.8 | 50.9 | 50.4 | 194.4 | 189.4 |
| Capex (incl. $20m reactivations in Q3-27) | 15.0 | 15.0 | 16.0 | 16.0 | 36.0 | 17.0 | 70.0 | 75.0 |
| **Maintenance FCF** | **6.4** | **7.3** | **−5.9** | **−18.8** | **−21.9** | **−5.1** | **7.0** | **6.9** |
| Maintenance FCF per share | 0.02 | 0.02 | −0.02 | −0.06 | −0.07 | −0.02 | 0.02 | 0.02 |
| Debt amortisation | 0 | 0 | 0 | 0 | 52.1 | 0 | 148.5 | 104.3 |
| FCF after debt service per share | 0.02 | 0.02 | −0.02 | −0.06 | −0.24 | −0.02 | −0.46 | −0.32 |
| Growth capex / distributions | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| RCF drawn, end | 0 | 0 | 0 | 0 | 1 | 6 | 148 | 245 |
| Net debt, end | 2,339 | 2,332 | 2,338 | 2,356 | 2,380 | 2,385 | 2,380 | 2,376 |
| Net debt per share | 7.58 | 7.56 | 7.58 | 7.64 | 7.71 | 7.73 | 7.72 | 7.70 |

### Bear and Bull (lines not shown follow the Base mechanics)

| | Q3-26E | Q4-26E | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|
| **Bear** fleet working share | 77.7% | 78.2% | 76.9% | 73.7% | 71.0% | 69.1% | 67.0% | 78.1% |
| Bear EBITDA | 83.4 | 83.8 | 67.4 | 47.8 | 34.1 | 25.9 | 40.7 | −0.9 |
| Bear maintenance FCF | 6.4 | 7.2 | −9.3 | −28.0 | −41.3 | −49.6 | −255.2 | −316.9 |
| Bear maintenance FCF per share | 0.02 | 0.02 | −0.03 | −0.09 | −0.13 | −0.16 | −0.83 | −1.03 |
| Bear RCF drawn / cumulative funding gap | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 33 / 0 | 83 / 0 | 250 / 237 | 250 / 658 |
| Bear net debt before new money | 2,339 | 2,332 | 2,341 | 2,369 | 2,412 | 2,461 | 2,719 | 3,039 |
| **Bull** fleet working share | 77.7% | 78.5% | 80.7% | 92.5% | 91.2% | 90.6% | 90.8% | 91.0% |
| Bull EBITDA | 83.4 | 83.9 | 80.4 | 100.8 | 97.6 | 96.6 | 479.0 | 548.1 |
| Bull maintenance FCF | 6.4 | 7.3 | 2.6 | 1.5 | 18.4 | 17.3 | 162.9 | 231.1 |
| Bull maintenance FCF per share | 0.02 | 0.02 | 0.01 | 0.00 | 0.06 | 0.06 | 0.53 | 0.75 |
| Bull net debt | 2,339 | 2,332 | 2,329 | 2,328 | 2,311 | 2,293 | 2,133 | 1,904 |

### Year-end path ($ per share; D_t = 0; P = $4.40 at 24 Oct)

End-of-stub rigs are at the Noble-implied mark, with contracts firm today only (identical in all scenarios). Interim marks glide linearly to the scenario's mid-cycle at exit; from end-2027 they also count the backlog the scenario holds on that date (2-year cap): Bull −$0.05 (end-2027) and +$0.10 (end-2028) a share.

| | Stub (31 Dec 26) | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Base V_t / r_t / IRR to t | 0.39 / −91.1% / n.m. | 0 / −100% / −100% | 0 / — / −100% | **0 / — / −100%** |
| Bear V_t / IRR to t | 0.39 / n.m. | 0 / −100% | 0 / −100% | 0 / −100% |
| Bull V_t / r_t / IRR to t | 0.39 / −91.1% / n.m. | 1.77 / +354% / −53.6% | 3.98 / +125% / −4.5% | **6.17 / +55% / +11.2%** |
| **v3.2** Bull V_t / IRR to t (28 rigs, P = $3.24 at 7 Nov) | 0.13 / n.m. | 1.38 / −52.5% | 3.49 / +3.5% | **5.55 / +18.6%** |

## 7. Exit value V_T (Rig BBB asset-value convention)

- **Method** (Rig BBB skill rev 2026-10-08.2, unchanged since):
  - Value per rig = annual rig cash flow × the 8% annuity over 30 − age years, floored at $10m.
  - Annual rig cash flow = 365 × [MCU × (rate × 96% − $75k) − (1 − MCU) × 40% × $75k] − 4.5% tax on revenue − $2.5m maintenance capex.
  - Rate = high-spec mid-cycle (92 / 110 / 130) × 1.08; MCU 82 / 88 / 92%. All rigs are valued on the global high-spec row, since rigs are mobile.
  - G&A and financing are excluded. Holding-company G&A ($54–59m a year) is in the 2026–29 cash flows as paid and never in NAV (IAF rule 2026-10-18.2).
- **New (IAF 2026-10-18.2):** V_T adds the premium on backlog the scenario holds at exit (capped at end-2031) and, where the exit-consistency test finds a material gap with no named reason, a 2-year reversion tail.

**V_T bridge, Base ($m; per share in brackets)**

| Step | $m |
|---|---|
| NAV_0 at 24 Oct 2026: rigs at Base mid-cycle by age 1,954 + firm-contract premium 193 + JV 0 − net debt 2,339 | **−192 (−$0.62)** |
| − Ageing of the owned fleet (1,954 → 1,784) | −170 (−$0.55) |
| − Firm-contract premium roll-off (193 → 6) | −187 (−$0.61) |
| + Premium on backlog signed in the Base (contracts running past T, capped at end-2031) | +42 (+$0.14) |
| + Reversion tail (exit consistency, high-spec block) | +38 (+$0.12) |
| + Value created by growth capex (none committed); JV stake stays at zero | 0 |
| + Retained cash: Σ maintenance FCF −30, amortisation premia −7 (net debt 2,339 → 2,376) | −37 (−$0.12) |
| = Equity at exit: rigs 1,784 + firm premium 6 + backlog 42 + tail 38 + JV 0 − net debt 2,376 | **−506 → V_T = 0** (limited liability) |

P/NAV_0 is not meaningful because NAV_0 is negative: at Base mid-cycle marks, the equity is under water today.

**Exit asset values ($m; age at 1 Jan 2030; each rig in brackets)**

| Rigs (age at exit) | Bear | Base | Bull |
|---|---|---|---|
| 2008 CJ50: Bestla, Joro (22) | 20 (10) | 81 (41) | 169 (84) |
| 2011: Norve (19) | 10 | 51 | 105 |
| 2013–14: 10 rigs (16–17) | 100 (10) | 564 (56–58) | 1,169 (116–121) |
| 2017–20: 14 rigs (10–13) | 140 (10) | 938 (65–70) | 1,943 (134–144) |
| 2024: Vali, Var (6) | 20 (10) | 149 (75) | 309 (154) |
| **Owned fleet (29)** | **290** | **1,784** | **3,694** |
| Firm-today premium after exit (Galar, Gersemi to May 2030) | 13 | 6 | 0 |
| Premium on backlog signed in the scenario (below) | −28 | +42 | +49 |
| Reversion tail (exit consistency, below) | −52 | +38 | 0 (named reason; +56 as sensitivity) |
| JV stake (five rigs worth $50m / $116m / $334m against $237m of debt) | 0 | 0 | 64 |
| Net debt at exit | 3,039 before new money | 2,376 | 1,904 |
| **Equity / V_T per share** | **−2,817 / 0** | **−506 / 0** | **1,904 / $6.17** |
| **v3.1 without Prospector 5:** 2013–14 block 9 rigs | 90 | 506 | 1,048 |
| v3.1 owned fleet (28) | 280 | 1,726 | 3,573 |
| v3.1 backlog premium / tail (its high-spec share removed) | −28.7 / −52 | +38.6 / +35.3 | +44.7 / 0 |
| v3.1 net debt at exit (no insurance) | 3,056 before new money | 2,421 | 1,969 |
| **v3.1 equity / V_T per share** | **−2,844 / 0** | **−615 / 0** | **1,713 / $5.55** |

**Backlog at exit** (contracts the scenario signs before exit, running into 2030–31; premium per day = contract day at the 2029 row rate × 1.08, 96% RE, $75k opex and 4.5% tax, against the convention's mid-cycle day at the scenario MCU incl. idle cost; discounted at 8%):

| Block (rigs, excl. Galar/Gersemi) | 2029 contract rate, $k (Bear / Base / Bull) | Premium per contract day, $k | Premium, $m (Bear / Base / Bull) |
|---|---|---|---|
| High-spec (14) | 91.8 / 129.6 / 156.6 | +1.4 / +17.6 / +21.6 | +3.6 / +51.7 / +66.1 |
| SE Asia (8) | 75.6 / 105.8 / 124.2 | −13.5 / −4.2 / −8.2 | −20.3 / −7.1 / −14.3 |
| Middle East (5) | 76.7 / 108.0 / 130.7 | −12.5 / −2.2 / −2.2 | −11.7 / −2.3 / −2.4 |
| **Total** | | | **−28.4 / +42.3 / +49.4** |

- Firm-today contracts (Galar, Gersemi to May 2030) count for their full term, as before.
- Most of the high-spec premium is utilisation: a contracted rig works ~96% of its days against the mid-cycle MCU of 82 / 88 / 92%. SE Asia and Middle East contracts sign below the high-spec mark, so their premium is negative.
- **Sensitivities (Bull):**
  - Contracts firm today only: V_T $6.01, IRR 10.3%, P_k $4.19.
  - Backlog at Rig BBB's market cover proxy (70% / 45%) instead of Borr's own book shape: IRR 11.9%.
  - Base and Bear stay at zero either way.

**Exit consistency (Step 3):** earnings basis = rate × MCU (Rig BBB basis); open days are those not under backlog at exit. SE Asia and the Middle East use the high-spec MCU path `[A]`: there is no SE Asia MCU series, and the Middle East row is Base-only. Galar and Gersemi are open from Jun 2030.

| Block | Scenario | Year-3 rate × MCU | Mid-cycle × MCU (the mark) | Gap | Open share 2030 / 2031 | Treatment | Tail $m (per share) |
|---|---|---|---|---|---|---|---|
| High-spec (16) | Bear | 85 × 81% = 68.9 | 92 × 82% = 75.4 | −8.7% | 61% / 84% | Not material | 0 |
| SE Asia (8) | Bear | 70 × 81% = 56.7 | 75.4 | −24.8% | 61% / 84% | Tail: Rig BBB names no recovery cause (Bear: Gulf rigs move to Asia) | −32.6 (−0.11) |
| Middle East (5) | Bear | 71 × 81% = 57.5 | 75.4 | −23.8% | 61% / 84% | Tail | −19.5 (−0.06) |
| High-spec (16) | **Base** | 120 × 91% = 109.2 | 110 × 88% = 96.8 | **+12.8%** | 56% / 83% | **Tail.** The named reason does not apply: asset-implied rates ($119–123k) are above Base mid-cycle | **+37.7 (+0.12)** |
| SE Asia (8) | Base | 98 × 91% = 89.2 | 96.8 | −7.9% | 56% / 83% | Not material | 0 |
| Middle East (5) | Base | 100 × 91% = 91.0 | 96.8 | −6.0% | 56% / 83% | Not material | 0 |
| High-spec (16) | **Bull** | 145 × 95% = 137.8 | 130 × 92% = 119.6 | **+15.2%** | 54% / 82% | **Named reason:** Rig BBB transaction check ("Interface — asset values and anchors"): the asset market prices jackups at ~$119–123k, at or below Bull mid-cycle ($130k), so a buyer at exit pays the mid-cycle mark | 0 (sensitivity +56.3, +0.18) |
| SE Asia (8) | Bull | 115 × 95% = 109.3 | 119.6 | −8.7% | 54% / 82% | Not material | 0 |
| Middle East (5) | Bull | 121 × 95% = 115.0 | 119.6 | −3.9% | 54% / 82% | Not material | 0 |

| Exit treatment | Bear IRR_T / P_k | **Base IRR_T / P_k** | Bull IRR_T / P_k |
|---|---|---|---|
| **Decision (treatments above)** | −100% / 0 | **−100% / 0** | 11.2% / 4.30 |
| Other treatment (Bear and Base without the tail; Bull with the tail) | −100% / 0 | −100% / 0 | 12.2% / 4.43 |
| 8 Oct rules (no backlog at exit, no tail) | −100% / 0 | −100% / 0 | 10.3% / 4.19 |

**Exit cross-check against the equity market (Oslo, Equity BBB 17/18 Oct)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| V_T ($m) | 0 (equity −2,817) | **0 (equity −506)** | 1,904 |
| FCF_normalised before holdco G&A ($m; after the fleet-renewal charge) | −222 | **−96** | 83 |
| Holdco G&A, not in NAV ($m a year) | 59 | **59** | 59 |
| **Exit P/E** on FCF_normalised before holdco G&A (Maintenance FCF basis in brackets) | n.m. | **n.m.** | 22.9x (9.9x) |
| Book equity at exit ($m; $961.6m at 30 Jun + net income to exit `[A]`) | −87 | **576** | 1,047 |
| **Exit P/B** | n.m. | **0** | 1.82 |
| **Buyer's implied return at exit** | n.m. (equity under water) | **n.m.** (assets $1.87bn < net debt $2.38bn); assets at 8% | ~7.5%: assets at 8%, debt at ~8.3–9.1% on net debt about equal to equity |
| Oslo index: exit P/E / exit P/B / mid-cycle return | 10.5 / 1.48 / 8.2% | **11.5 / 1.75 / 9.1%** | 12.5 / 1.97 / 9.4% |
| Sensitivity: exit marks re-discounted at the index return (IRR_T / P_k) | −100% / 0 | **−100% / 0** (rigs $1.66bn) | 4.9% / 3.57 |

- **Base and Bear:** the exit equity is negative, so the equity ratios are not meaningful. On the asset side the marks are the asset market's own (8%), the most independent exit available.
- **Bull:**
  - The exit P/B (1.82) is in line with Oslo's Bull 1.97.
  - The exit P/E on normalised equity FCF is ~23x, far above Oslo's 12.5x. The reason is leverage plus finite-life ageing: after 8.3–9.1% debt service on ~$1.9bn and a $110m-a-year fleet-renewal charge, little equity cash is left. Before the renewal charge it is 9.9x.
  - **A buyer at NAV earns ~7.5% on the levered equity**, below Oslo's Bull mid-cycle return (9.4%), and no reason (quality, growth, contract cover) is stated for accepting less.
  - P/NAV = 1 at exit stays the convention. The re-discounted case (4.9%) shows how much of the Bull return depends on it.
- **Book at exit:** net income = EBITDA − tax − interest − depreciation at the Q2 run-rate ($43.5m a quarter `[F]`) − amortisation premia, by scenario `[A]`.

**Cross-checks:**
- Book value of the rigs: $3,037m at 30 Jun ($105m a rig) `[F]`.
- Noble paid $72m a rig and Fontis $57m a rig. Base exit values are $41–75m a rig, 3.2 years older.
- On the convention, the Noble price implies ~$123k through-life (Rig BBB market check: transactions 8–12% above Base mid-cycle). At that mark, exit equity is still negative (sensitivity).

## 8. Growth capex test

- **No growth capex is committed** in the horizon. Reactivating the four stacked rigs ($20m) sits in maintenance FCF and clears k easily *if* they find work (~$13m of EBITDA a year each at Base rates).
- **Fontis JV** (Jul 2026, already sunk):
  - Borr put in $40m ($25m equity + $15m loan).
  - Stake at T: Base **$0** (five rigs worth $116m against $237m of debt), Bear $0, Bull $64m.
  - **ROIC_g < k in Base.** The non-recourse structure caps the loss at $40m.
- **Noble five rigs** ($360m, Jan 2026, sunk): Base value today $294m, market marks $350m, Bull $608m. Accretive only on Bull-level values.

## 9. Full results and sensitivity

v3.2 figures at $3.24 (7 Nov; 28 rigs, no insurance); v3.1 at $4.40 in brackets where they moved. The notes and the sensitivity table below are the v3 build with 29 rigs at $4.40, except where marked v3.1 or v3.2; the insurance sensitivity is in the v3.1 and v3.2 notes at the top.

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T | −100% | **−100%** | +18.6% (+7.6%) |
| IRR_T in NOK on the Equity BBB NOK path (USD/NOK Bear +12% / +9% / +9%, Bull −3%) | −100% | **−100%** (spot flat) | +17.5% (+6.5%) |
| d / g / c | 0.0% / −100% / 0.0 pp | **0.0% / −100% / 0.0 pp** | 0.0% / +18.6% / 0.0 pp |
| g: re-rating / NAV growth (P/NAV_0) | n.m. (NAV_0 −$5.46) | **n.m. (NAV_0 −$0.85)** | +17.0% / +1.4% (0.61x) |
| Structural IRR / cyclical | −100% / 0 | **−100% / 0** | ~+15.6% / ~+3.0 pp `[A]` (~+4.8% / ~+2.8 pp) |
| ΣD_t / V_T | 0 / 0 | **0 / 0** | 0 / $5.55 |
| P_k / margin of safety | $0 / −100% | **$0 / −100%** | $3.88 / +19.9% ($3.87 / −12.1%) |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | n.m. | **n.m. vs negative** | not re-run; above the 12.9x ceiling (v3 55x at $4.40; ~40x at $3.24 `[A]`) |
| Capital preserved? ΣD_t + V_T vs $3.24 | No (−100%) | **No (−100%)** | Yes ($5.55) |

**Notes on the results:**
- **Structural run:**
  - Every open day from 1 Jan 2027 is priced at the scenario's own mid-cycle rate and MCU. The reversion tail is zero. Backlog signed in the scenario stays at exit, re-priced to mid-cycle, so only its utilisation premium remains (Bull −$16m: SE Asia and Middle East sign below the high-spec mark).
  - Base and Bear are zero either way, so the result is set by the mid-cycle and the balance sheet, not by the cycle.
  - Bull: structural 8.3%; the cycle adds 2.9 pp, all through g.
- **FCF_normalised:**
  - Base: full fleet at Base mid-cycle (regional rows × 1.08, MCU − 5 pp) at 2029 costs gives EBITDA $213m. Less tax $42m, interest on exit net debt $197m and capex $75m: −$102m. Less the fleet-renewal charge of $53m: **−$155m = −$0.50/share**.
  - Bull: $24m ($0.08) after a $110m renewal charge `[C]`.
- **Scenario-weighted reference (convention, 25/50/25 on V_T):** $1.54 → IRR −28.0%, P_k $1.08. Not the decision figure.
- **Bull already priced:** P ($4.40) is just above the Bull P_k ($4.30), i.e. **102%** of the way from the Base to the Bull hurdle.
- **NOK path (Equity BBB):** the decision is at spot USD/NOK 9.316. Equity BBB's firmer Bull krone (−3%) trims Bull from 11.2% to 10.1% in NOK. Base is spot flat, and Bear is −100% in any currency.
- **Bear survival:**
  - Cash reaches the $100m floor in Q3-27, and the RCF is fully drawn in 2028.
  - Funding gap: $237m in 2028, $658m by end-2029. That points to a restructuring in 2028; the equity is wiped.
- **Base liquidity:**
  - The RCF is drawn to $245m of $250m by end-2029. Amortisation from 2030 ($51m a half-year) would need new money.
  - SSRCF covenants were not found `[?]`.
  - An equity issue or debt exchange is a real Base risk, and it is not in the per-share figures.

**Sensitivity** (Base unless stated; P = $4.40; backlog at exit and the exit-consistency rule applied in each case unless stated)

| Change | V_T | IRR_T | P_k |
|---|---|---|---|
| **Base** | 0 | −100% | 0 |
| Base without the tail and without scenario backlog | 0 | −100% | 0 |
| Exit at the Noble-implied rate (~$123k Borr level, 88%, no premium) | 0 | −100% | 0 |
| Exit values with Borr's own model opex ($71k in 2030) — Base / Bull | 0 / 7.38 | −100% / +17.6% | 0 / 5.14 |
| Rig life 35 years — Base / Bull | 0 / 8.01 | −100% / +20.7% | 0 / 5.58 |
| Own opex + 35-year life | 0.44 | −51.5% | 0.30 |
| Borr premium 16% (cash flows and values) — Base / Bull (8 Oct exit build, no backlog line; re-timed to 24 Oct) | 0.74 / 9.27 | −42.8% / +26.3% | 0.52 / 6.46 |
| Base mid-cycle rate for exit values $120k / $130k / $140k | 0.52 / 3.03 / 5.37 | −48.7% / −11.0% / +6.5% | 0.36 / 2.11 / 3.74 |
| **Break-even mid-cycle rate** (Base cash flows) | ≈ 6.32 | 12% at **~$144k** (8 Oct rules: ~$141k; Bull mid-cycle $130k) | ≈ 4.40 |
| Base cash flows, Bull exit values | 3.99 | −3.0% | 2.78 |
| Bull cash flows, Base exit values | 0.68 | −44.4% | 0.47 |
| Bull with the reversion tail | 6.35 | +12.2% | 4.43 |
| Bull, contracts firm today only | 6.01 | +10.3% | 4.19 |
| Bull, exit marks at Oslo's Bull mid-cycle return (9.4%) | 5.12 | +4.9% | 3.57 |

- **Exit values decide everything.** Even Bull cash flows cannot make up for Base exit values.
- At higher mid-cycle marks, Base's own 2029 rates (high-spec $120k, SE Asia $98k, Middle East $100k) fall below the mark. The backlog premium and the tail then turn negative, which is why the break-even rises from ~$141k to ~$144k under the current rules.
- Only a mid-cycle above Rig BBB Bull, or several favourable assumptions together (Bull rates + Borr's opex + 35-year life), clears 12% with margin. Bull alone now sits at k, within the uncertainty of the exit rules.

## 10. Verdict and caveat

- **Fails** (Base margin of safety −100%), **does not survive Bear**, and **Bull falls below k** after the loss of Prospector 5 (v3.1: 7.6%; 9.9% with $100m of insurance; v3 11.2%).
- **v3.2 (7 Nov, $3.24):** still **fails** in Base and Bear. **Bull is now above k** (18.6%, margin +19.9% against the Bull P_k of $3.88). The price no longer reflects the Bull case in full (83% of the way from the Base to the Bull hurdle). The upside is a stress-test outcome, not a margin of safety: Base still leaves no equity at exit.
- **What would flip it:**
  - A jackup mid-cycle of ≥ ~$139k at $3.24 (Rig BBB basis; v3.1 ~$146k at $4.40; v3 ~$144k).
  - Evidence that Borr's rigs run materially below $75k a day (sourced opex), combined with a Bull-level mid-cycle.
  - A Rig BBB mid-cycle review that moves towards the transaction-implied rates (open checkpoint 13) *and* above them.
  - Stub, payout and k do not matter.
- **Caveat:** margin-of-safety screen, not an intrinsic valuation or price target. The analysis also ignores the option value of limited liability: equity in a levered company with debt due 2032–34 can trade above a zero-NAV floor for years.

## Tracking

| | Version 1 (8 Oct) | Version 2 (8 Oct) | Version 3 (24 Oct) | Reason (v2 → v3) | Version 3.1 (25 Oct) | **Version 3.2 (7 Nov)** |
|---|---|---|---|---|---|---|
| Rig values | Gross-margin method | Harmonised convention (Rig BBB rev 2026-10-08.2) | Same convention; backlog at exit and exit-consistency added | IAF 2026-10-18.2 | Same; **28 rigs** (Prospector 5 lost) | Unchanged (Rig BBB 4 Nov: jackup rows kept) |
| Price / T | $4.635 / 3.23 | $4.635 / 3.23 | $4.40 / 3.19 | 23 Oct close | $4.40 / 3.19 (pre-incident price) | **$3.24 / 3.15** (6 Nov close) |
| Base V_T / IRR_T / P_k | $4.01 / −4.4% / $2.78 | $0 / −100% / $0 | $0 / −100% / $0 | Unchanged (exit equity −586 → −506) | $0 / −100% / $0 (exit equity −615) | **$0 / −100% / $0** |
| Bull V_T / IRR_T / P_k | $11.86 / +33.7% / $8.22 | $6.01 / +8.3% / $4.16 | $6.17 / +11.2% / $4.30 | Price +2.0 pp; backlog at exit +0.9 pp | $5.55 / +7.6% / $3.87 (no insurance) | **$5.55 / +18.6% / $3.88** (price only) |
| Break-even mid-cycle | — | ~$142k | ~$144k | Exit rules +$3.5k; lower price −$1k | ~$146k | **~$139k** `[A]` |
| NAV today at market marks | $0.89 | $0.60 | $0.60 | — | ~$0.35 before insurance | ~$0.35 (P/NAV ~9.3x) |
| Cash flows, EBITDA, net debt | — | Unchanged | Unchanged | No rig row changed; regional check within 5% | Base net debt at exit +$45m; EBITDA −$52m over 2026–29 | Unchanged |

No new quarterly report since version 1. The first test is the Q3 report (not announced as of 7 Nov; Yahoo estimate 18 Nov): EBITDA of ~$83m and ~23 working rigs (Zacks consensus EPS −$0.11, 28 Oct).

## 11. Risks and signposts

| Signpost | Bear | Base | Bull | Now |
|---|---|---|---|---|
| Borr's realised rate on 2027 starts | < $100k | $100–120k | > $130k | YTD awards ~$123k incl. mob `[F]`; no award since 30 Sep |
| Q3-26 EBITDA (report 4–18 Nov, not announced) | < $70m | $80–90m | > $95m | Consensus-implied ~$80m (EPS −$0.09, 4 analysts) |
| Working rigs Q4-26 / Q1-27 | < 21 | 22–23 | ≥ 24 | ~23 guided for Q3 |
| Stacked rigs (Freyja, Groa, Hild, Var) | Stacked through 2027 | Back by H2-27 | Back by Q2-27 | All warm stacked |
| Aramco / KJO jackup awards; Gulf operations | Suspensions after 3 Nov | Gradual | Aramco recalls 6–9 rigs | KJO 4 × 4 years; Aramco pending `[?]`. **Escalation from 22 Oct** (Oil BBB 24 Oct: Houthi strikes inside Saudi Arabia, Aramco evacuated its Dhahran HQ); no suspension notice from Borr (Arabia III, Arabia II, Forseti) as of 24 Oct. **Towards Bear** |
| High-spec MCU (Westwood) | < 84% | 88–91% | > 92% | 87% (Aug); working jackups 373 (12 Oct) |
| Jackup transaction marks | < $60m for 2013–14 HD rigs | $70–90m | > $110m | Noble $72m, Fontis $57m |
| Liquidity (cash + undrawn RCF) | < $250m | $250–350m | > $400m | $473.6m (30 Jun) |
| Fontis JV | Interest missed at the 14% step (Jan 2028) | Self-funding, refinanced Jan 2029 | 4–5 rigs working | 3 of 5 contracted |
| Insider buying (Trøim, Schorn, CEO) | Insiders sell or stop buying | Occasional buying | Continued buying ≥ $4.5 | **Bull signpost hit:** Trøim 5.25m at $4.60–4.93 on 9–15 Oct (plus 2.75m at $4.24–4.31 on 6–7 Oct) |
| Short interest (FINRA) | Rising above ~35m shares | 25–33m | Falling below 20m (or a squeeze) | **34.5m (30 Sep)**, up from 29.4m (15 Sep). Towards Bear |
| **Prospector 5 loss (v3.1)**: insurance and covenants | Claim disputed or delayed; proceeds offered to noteholders while the RCF is needed; deductible and claims beyond P&I | Total loss accepted at agreed value within ~12 months | Agreed value ≥ ~$156m and kept as liquidity | Sank 24 Oct; insured value, timing and indenture terms not disclosed `[?]`. **7 Nov:** still not stated; the notes are on Watch at ~93 derived (`docs/hy-issuers.md`, 4 Nov) |
| **Prospector 5 loss (v3.1)**: people, investigation, clients | Loss of life confirmed; findings against Borr's preload procedure; client or regulator reviews of other Borr rigs; BW Energy moves the campaign to another contractor | Investigation finds a site-specific seabed cause; no wider client action | — | Five people missing, search ongoing (25 Oct); cause preliminary (punch-through); no client or regulator statement beyond BW Energy's shut-in. **7 Nov:** four dead, one still missing (6-K 2 Nov); a class-society investigation has been engaged; BW Energy's campaign is delayed with no restart date (29 Oct); Gabon's technical investigation is `[E]` |

**Other risks:** customer credit (West Africa loss, PEMEX); start-up execution (Odin); Middle East insurance and suspensions; dilution if liquidity tightens.

### Market signals: insiders and short interest (not an IAF input)

**Insider trades 2026** (Yahoo insider module from filings `[F]`; PDMR notices `[E]`):

| Who | Trades | Shares | Value | Price range |
|---|---|---|---|---|
| Tor Olav Trøim (director, founder; via Drew Holdings) | 24 Mar, 16 Apr, 9 Jun, 13–14 Aug, 25 Aug, 18 Sep (notice), 5 Oct; **6, 7, 9, 13, 14, 15 Oct** | ~13.8m (of which 8.0m on 6–15 Oct) | ~$63m (of which $37m in Oct after the 5th) | $4.02–5.58 |
| Patrick Schorn (executive chair) | 17 Jun | 1.2m | $5.1m | $4.27 |
| Bruno Morand (CEO) | 17 Jun, 18 Sep | 0.32m | $1.4m | $4.27–4.40 |
| Jeffrey Currie (director) | 24 Mar, 13 Aug | 0.38m | $1.8m | $4.01–5.31 |
| Thiago Mordehachvili (director, indirect holding) | 9 Jun **sale** | 8.0m | $37.6m | $4.70 (same day Trøim bought 1.06m at $4.70) |
| CFO, COO, GC and two officers | 2–3 Sep **sales** | ~0.08m | ~$0.4m | $4.55–4.80 (small; possibly tax on share vesting `[?]`) |
| Harvey Snowling (COO) | 13–14 Oct: option exercise (0.15m), purchase and sale of 0.3m at $4.91 | net ~0 | — | $4.91 (likely exercise-and-sell `[?]`) |

- Trøim's indirect holding was ~32.1m shares (10.4%) before October `[F]`, so ~40m (~13%) after the 6–15 Oct buys `[A]`. In 2026 to date insiders bought ~15.7m shares and sold ~8.1m; the 8m block sale dominates the sales.
- **Short interest** (FINRA via Yahoo `[E]`):
  - 16.9m (13 Mar) → 27.8m (30 Jun) → 32.9m (14 Aug) → 29.4m (15 Sep) → **34.5m (30 Sep, the highest in the 2025–26 series)**.
  - That is 11.2% of shares outstanding, 14.5% of float, 5.9 days to cover.
- **Brokers (market check only, never an IAF input):** Yahoo 6 analysts, mean target $4.88 ($3.50–5.50); Zacks 9 brokers, average broker rating 2.11, average target $5.55. Zacks Rank 5 reflects estimate cuts (FY27 EPS $0.32 → $0.04 in 90 days).

**Reading:**
- **Not all of the short interest is a bet against Borr.** The jump from March to June coincides with the April issue of $300m 3.5% convertible notes (conversion $8.00, 37.5m shares). Convertible-arbitrage funds short the stock to hedge. At a delta of ~0.3–0.45, that is ~11–17m shares `[A]`, partly offset by the hedges that unwound when $195m of the 2028 convertible was repurchased. Only the rest is a directional bet, and the September rise is consistent with this analysis: leverage plus re-pricing.
- **Trøim's buying is the strongest bull signal available.**
  - He founded Borr, knows the tender pipeline (Aramco, KJO, PEMEX), and has now bought ~$63m in 2026 at $4.0–5.6. The 9–15 Oct buys were at $4.60–4.93, above today's price.
  - He did the same in Nov 2024 ($3.93); the share later fell to $2.44.
  - It tells us he expects a better cycle than Rig BBB Base. The price is already at the Bull hurdle ($4.30).
- **Equity in a company with debt due 2032–34 is a long-dated option on the cycle**, and this screen ignores option value. Downside per share is capped while an upcycle (rates $150k+) would multiply the equity. That can justify buying for an investor with a horizon beyond 2029 and a strong Bull view, but it is not a margin of safety at k = 12%.
- Neither signal changes P_k. Both are tracked as signposts above.

## For other modules

- **Rig Market BBB:**
  - **Regional jackup reading (10 Oct request) answered:** Borr's 2026 prints (~$123k awards incl. mobilisation, ~$134k cover) sit ~31% above the benign-region level (~$94k) for a modern high-spec fleet. A regional split of the high-spec row, or a stated premium for modern units in benign regions, would remove the `[A]` here.
  - **Gulf jackups:** the Oil BBB of 24 Oct reports escalation from 22 Oct (Houthi strikes in Saudi Arabia, Aramco HQ evacuated). Rig BBB's Bear catalyst for Gulf jackups (suspensions) has not been assessed since 22 Oct. Borr has three rigs working in the Gulf.
  - **Data gaps:** a typical contract term for the jackup rows (needed for the backlog-at-exit cap), Middle East Bear/Bull rows, an SE Asia MCU series, and jackup opex per operated rig (open checkpoint 13; Borr's blended $63k includes bareboat rigs).
  - **Borr company data** `[F]` for the jackup rows (carried): modern-jackup MCU 90.1% (30 Jun) and 91.7% (11 Aug); 11 newbuilds under construction; Borr YTD awards ~$123k; Middle East H1 awards the lowest in 25 years; PEMEX recalling rigs. The Q3 fleet status (with the Q3 report) is the next input for rig-by-rig cover (Rig BBB checkpoint 6).
- **v3.1 (25 Oct), Prospector 5 lost:**
  - **Rig BBB:** no change needed. One high-spec jackup out of ~370 working is below any minimum change. BW Energy may need a replacement jackup in West Africa (a small demand item, not yet stated).
  - **HY BBB / `docs/hy-issuers.md`:** the credit reading weakens. The note collateral very probably loses one rig (`[A]`; "most of the rigs" secure the notes). Base net debt at exit rises by $45m without insurance, and Base now exhausts the RCF in 2029 (~$40m gap). Insurance cash kept as liquidity would offset it. Track the insured value and whether the indenture requires the proceeds to be offered to noteholders `[?]`.
- **HY BBB / `docs/hy-issuers.md`:**
  - No change (v3). Borr's 8.75% 2032 and 9.00% 2034 notes amortise 5% a year at 102.5% from Jul 2027.
  - Credit reading: Base leaves no room for deleveraging (RCF nearly fully drawn by 2029); Bear cannot service the notes from 2028.
  - Both matter for the Heimdal funds' Borr positions (4.8–5.4% of NAV).
- **Oil Market BBB:** no change needed.
- **Equity BBB:** read only (exit cross-check, NOK path); no input back.
- **v3.2 (7 Nov):** no change needed for Rig BBB or Equity BBB. For `docs/hy-issuers.md`: the equity fell 26% to $3.24 (market cap $1.00bn), which shrinks the equity cushion under the notes. The credit reading of the model is unchanged (Base RCF exhausted in 2029, Bear liquidity gone in 2028). Insurance is still not stated.

## Change log

- **7 Nov 2026, version 3.2 (price re-mark, change gate):** iaf-valuation 2026-11-01.1, rig-market-bbb 2026-10-10.1, equity-market-bbb 2026-10-24.1 (read only).
  - **Read:** Rig BBB 4 Nov (only the UDW drillship 2027 point moved; jackup rows, MCU paths, mid-cycle and asset values kept). Equity BBB 6 Nov (Oslo exit P/E unchanged; exit P/B Bull 1.97 → 1.95; mid-cycle return 9.4 → 9.2% in Bull and 9.1 → 8.9% in Base; NOK relative moves unchanged). `docs/hy-issuers.md` 4 Nov (notes Performing → Watch, ~93 derived). Peers' Q3 reports via Rig BBB: no jackup change, no Gulf suspension.
  - **Borr news:** Prospector 5 updates of 29 Oct and 2 Nov (four dead, one missing; class-society investigation). Nothing on insurance, the BW contract or the notes. Q3 date not announced (Yahoo estimate 18 Nov).
  - **Moved:** price $4.40 → $3.24 (−26%), valuation date 7 Nov, T 3.15 years. **Bull IRR 7.6% → 18.6%, P_k $3.87 → $3.88, margin −12.1% → +19.9%; Bull NOK 6.5% → 17.5%; break-even mid-cycle ~$146k → ~$139k.** The Bull sensitivity with exit marks at Oslo's return is now at 9.2%: ~12.4%.
  - **Not moved:** cash flows, V_T, Base and Bear (−100%, P_k $0). **Verdict unchanged: fails.** The Bull stress test is now above k.
  - Shares: 308.51m kept. Yahoo shows 309.26m, but no filing was found `[?]`.
- **25 Oct 2026, version 3.1 (news update):** the jackup Prospector 5 sank offshore Gabon on 24 Oct during preload for BW Energy. Five of 115 people are missing and the search is ongoing. Same skill revisions (iaf-valuation 2026-10-18.2, rig-market-bbb 2026-10-10.1).
  - **Model:** fleet 29 → 28. The rig's backlog (to Jul 2027), its open days to 2029 and its exit value are removed. No insurance proceeds are counted (insured value unknown); they are shown as a sensitivity ($70m / $100m / $130m: Bull 9.2% / 9.9% / 10.6%).
  - **Result:** Base and Bear unchanged at zero; Base exit equity −506 → −615; Base RCF exhausted in 2029. **Bull IRR 11.2% → 7.6%, P_k $4.30 → $3.87, margin −2.3% → −12.1%.** Break-even mid-cycle ~$144k → ~$146k. **Verdict unchanged: fails.**
  - **Not changed:** price $4.40 (pre-incident close), market inputs, method. The period tables carry a Δ table instead of a rebuild. The v3 sensitivities in section 9 are not re-run except as marked.
- **24 Oct 2026, version 3:** re-run under iaf-valuation 2026-10-18.2. Change gate, price and method.
  - **Upstream (change gate): no decision figure moves.**
    - Rig BBB (10 Oct; updates 13, 17, 22 Oct): the jackup rows, MCU, mid-cycle and asset values are unchanged since 4 Oct.
    - The regional-reading note was tested: Borr's documented premium holds, and the difference ($109k vs $113k) is below the 5% minimum change.
    - Oil BBB (17 Oct value change, 24 Oct unchanged) is background only.
    - Cash flows are unchanged.
  - **Company data:**
    - Price $4.635 → $4.40 (23 Oct close); USD/NOK 9.316.
    - No contract, fleet or financing news since 30 Sep. The 16 Oct 6-K is the 16 Sep investor presentation.
    - Trøim bought ~8.0m shares (6–15 Oct); short interest 34.5m (30 Sep).
    - Q3 report date not announced (4–18 Nov expected).
  - **Method (IAF 2026-10-18.2):**
    - Backlog at exit added (Base +$42m, Bull +$49m, Bear −$28m).
    - Exit-consistency test added: Base high-spec +12.8% gets a tail (+$38m); Bull high-spec +15.2% has a named reason (asset-implied ≤ Bull mid-cycle), with the tail as a sensitivity (12.2%); Bear SE Asia and Middle East get negative tails.
    - Exit cross-check against Equity BBB added (Bull exit P/E ~23x, P/B 1.82, buyer's return ~7.5% vs Oslo 9.4%; at 9.4% Bull is 4.9%).
    - Bear/Bull in NOK on the Equity BBB path added (Bull 10.1%).
    - Holdco G&A was already outside NAV; this is now stated.
  - **Result:**
    - Base and Bear unchanged ($0 / −100%).
    - Bull IRR 8.3% → 11.2%, P_k $4.16 → $4.30, margin −10% → −2.3%; break-even mid-cycle ~$142k → ~$144k.
    - **Verdict unchanged: fails.**
  - **Correction:** version 2's Bear exit equity (−$2,078m) netted the $658m funding gap against net debt. Before new money it was −$2,736m, and it is −$2,817m with the new exit lines. V_T is zero on either basis.
- **8 Oct 2026, version 2.1:** added market signals (insider trades 2026, short-interest history and reading) and two signposts. No change to figures or verdict.
- **8 Oct 2026, version 2:**
  - Restructured with a Summary first: decision table and per-share path, including FCF per share per period for all scenarios.
  - Per-share lines added to the period tables (IAF rev 2026-10-08.2).
  - Exit values, NAV_0 and market marks restated on the Rig BBB asset-value convention (rev 2026-10-08.2).
  - Result: Base V_T $4.01 → $0, P_k $2.78 → $0; Bull IRR 33.7% → 8.3%. Cash flows unchanged. Verdict unchanged (fails), but now also failing in Bull.
- **8 Oct 2026, version 1:** first Borr analysis (gross-margin rig values). Base IRR −4.4%, P_k $2.78.

## Appendix: own assumptions `[A]`

| Assumption | Value | Why |
|---|---|---|
| Booked rates | $128k pre-August; $120k post-August awards; Joro $80k | Backlog ÷ firm days `[B]`; rates not disclosed |
| Borr premium | +8% on open-day rates and exit values | YTD awards vs leading edge, halved; supported against the benign-region level (+31% incl. mob, ~+15–20% ex-mob) |
| Open-day utilisation | MCU − 5 pp; stub 50% for rolling rigs in Q4-26 | Contract gaps; options on Grid, Skald, Vali |
| Stacked-rig return | Base Jul 2027, Bull Apr 2027, Bear Jan 2029; $5m each | Warm stacked |
| Opex / idle | $63k per working day (2026, +3%); idle $30k warm, $12k cold | Q1-26 calibration |
| Options | Exercised in Base and Bull (Bestla, Norve, P1, Joro); not in Bear | — |
| Noble seller's credit | 7.5% → 8.5% → 9.5% → 10.5%, cash pay | Only "rising to 15% by Feb 2031" disclosed |
| Exit values | Rig BBB convention (jackup parameters), high-spec row × 1.08, 30 years, 8%, $10m floor | Rig BBB rev 2026-10-08.2 |
| Backlog at exit | 2030 / 2031 rig-days under scenario-signed contracts = 0.50 / 0.20 × the 2029 working share, at the 2029 row rate; 27 rigs (Galar, Gersemi carry their firm contract) | Borr's 8 Oct book shape; no typical term in Rig BBB |
| Exit-consistency MCU for SE Asia and Middle East | High-spec MCU path | No SE Asia series; Middle East Base-only |
| Book equity at exit | $961.6m (30 Jun) + net income; depreciation $43.5m a quarter | Q2 run-rate `[F]` |
| Middle East / SE Asia Bear-Bull | Scaled from high-spec ratios | Rig BBB rows Base-only |
| JV | 0.9 × high-spec rate; debt flat $237m; stake floored at zero | Lower-spec units; non-recourse |
| Market marks | Convention at the Noble-implied ~$123k, 88% MCU (JV at the Fontis-implied ~$119k) | Reproduces the transaction prices |
| Liquidity floor | $100m cash before RCF draws | — |

## Appendix: sources

| Source | Date | Used for |
|---|---|---|
| [Borr Q2 2026 results, 6-K ex. 99.2](https://www.sec.gov/Archives/edgar/data/1715497/000114036126032598/ef20080031_ex99-2.htm) | 11 Aug 2026 | P&L, balance sheet (equity $961.6m, depreciation $43.5m), cash flow, debt, Fontis JV, Q3 guidance |
| [Borr Fleet Status Report, 6-K ex. 99.3](https://www.sec.gov/Archives/edgar/data/1715497/000114036126032598/ef20080031_ex99-3.htm) | 11 Aug 2026 | Rig-by-rig contracts and status |
| [Borr H1 2026 interim report with notes (6-K)](https://www.sec.gov/Archives/edgar/data/1715497/000162828026055957/borr-20260630.htm) | 12 Aug 2026 | Debt terms, conversion prices, Noble $360m, JV terms |
| [Borr Q2 2026 presentation, 6-K ex. 99.2](https://www.sec.gov/Archives/edgar/data/1715497/000114036126032660/ef20080142_ex99-2.htm) | 12 Aug 2026 | Coverage, YTD contracting statistics |
| [Borr — Streamlines Mexico operations (6-K)](https://www.sec.gov/Archives/edgar/data/1715497/000114036126036608/ef20082025_ex99-1.htm) | 15 Sep 2026 | Perfomex divestment |
| [Borr — Operational and contracting updates (6-K)](https://www.sec.gov/Archives/edgar/data/1715497/000114036126036705/ef20082084_ex99-1.htm) | 15 Sep 2026 | Odin, Idun, Bestla |
| [Borr — Contracting updates (6-K)](https://www.sec.gov/Archives/edgar/data/1715497/000114036126038129/ef20083023_ex99-1.htm) | 30 Sep 2026 | Norve, Natt, Joro |
| [Borr — Investor presentation (6-K ex. 99.1)](https://www.sec.gov/Archives/edgar/data/1715497/000114036126039844/ef20082106_ex99-1.htm) | dated 16 Sep, filed 16 Oct 2026 | No new facts (Pareto conference presentation) |
| [EDGAR 6-K list, Borr (CIK 1715497)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1715497&type=6-K) | to 16 Oct 2026 | No share issue or financing since 30 Sep |
| Nordic Financial (Newsweb stream, BORR, 2026) | to 24 Oct 2026 | No announcement after 30 Sep; Q1/Q2 invitation timing |
| [Borr Q3 2025 results (6-K ex. 99.1)](https://www.sec.gov/Archives/edgar/data/1715497/000114036125040727/ef20058406_ex99-1.htm) | 5 Nov 2025 | Prior-year Q3 report date |
| Borr Q2 2026 earnings call transcript (Alpha Vantage) | 12 Aug 2026 | Q3 guidance, Odin costs, capex, JV funding `[C]` |
| Yahoo (BORR, BORR.OL, NOK=X; quoteSummary: consensus, insiders, short interest, calendar) | 23 Oct 2026 close; short interest 30 Sep | Price, FX, shares, consensus, insider trades, short interest |
| Zacks (compare_stocks BORR/VAL; news) | 24 Oct 2026 | Expected report date 4 Nov (estimate), brokers; no Zacks articles in the last 15 days |
| Norges Bank API (EXR B.USD.NOK.SP) | 23 Oct 2026 | USD/NOK fixing 9.3509 (cross-check) |
| Borr statement on Prospector 5, via [Reuters (Internazionale)](https://www.internazionale.it/ultime-notizie-reuters/2026/10/25/borr-drilling-rig-sinks-offshore-gabon-five-personnel-missing) and [Energy-Pedia ("Source: Borr Drilling")](https://www.energy-pedia.com/news/gambia/borr-drilling-reports-prospector-5-rig-incident-205800) | 25 Oct 2026 | v3.1: time, preliminary cause, people on board, missing. No 6-K on EDGAR yet (latest 16 Oct) |
| [BW Energy: Drilling rig incident on the Dussafu licence (stock-exchange release)](https://www.investegate.co.uk/announcement/mfn/bw-energy-ltd--0abd/bw-energy-drilling-rig-incident-on-the-dussa-/9839860) | 25 Oct 2026 | v3.1: MaBoMo shut-in, no damage or discharge `[F]` |
| [Offshore Energy (user link)](https://www.offshore-energy.biz/2026/10/25/rig-incident-110-rescued-5-still-missing-after-borr-drillings-jack-up-sinks-off-gabon-coast) | 25 Oct 2026 | v3.1: secondary; consistent with the two releases `[E]` |
| [Drilling Contractor: Prospector 5 heads to Dussafu](https://drillingcontractor.org/borr-prospector-5-jackup-heads-to-dussafu-for-mabomo-phase-2-drilling-80366) | 16 Oct 2026 | v3.1: four infill wells, first well onstream early 2027 `[E]` |
| [Borr 20-F FY2025](https://www.sec.gov/Archives/edgar/data/1715497/000162828026021450/borr-20251231.htm) | 26 Mar 2026 | v3.1: insurance (H&M at agreed value, deductible, P&I, war risk; no loss of hire described); notes secured by the 24 rigs then owned |
| BW Energy Q3 2026 operational update (via search) | 15 Oct 2026 | v3.1: BW Energy Q3 report 29 Oct `[E]` |
| Yahoo (BORR, BORR.OL, NOK=X quotes; BORR daily chart 22 Oct–6 Nov) | 6 Nov 2026 close; FX 7 Nov 05:21 UTC | v3.2: price $3.24, price path, shares 309.26m (unverified), Q3 date estimate 18 Nov |
| Norges Bank API (EXR B.USD.NOK.SP) | 4–6 Nov 2026 | v3.2: USD fixing 9.4277 (6 Nov) |
| Nordic Financial Newsweb stream (BORR, 2026) and EDGAR 6-K list | to 7 Nov 2026 | v3.2: Prospector 5 updates of 29 Oct and 2 Nov; no release after 2 Nov; Q3 date not announced |
| Zacks news (BORR) | 28 Oct 2026 | v3.2: Q3 consensus EPS −$0.11, revenue $256m |
| `docs/hy-issuers.md` | 4 Nov 2026 | v3.2: notes Watch, ~93 derived; BW Energy Q3 (29 Oct) |
| `docs/rig-market-bbb.md` | 10 Oct 2026 (updates 13, 17, 22, 24, 28 Oct, 4 Nov; v3.2 read the 4 Nov update) | Rates, MCU, mid-cycle, asset-value convention, transaction check, regional reading, catalysts, signposts |
| `docs/oil-market-bbb.md` | 24 Oct 2026 (last value change 17 Oct) | Background scenario mapping; Gulf escalation from 22 Oct |
| `docs/equity-market-bbb.md` | 17 Oct 2026, amended 18 Oct; v3.2 read Update 2 of 6 Nov | Oslo exit P/E, exit P/B, mid-cycle return; USD/NOK path |
| `docs/PLSV-analysis.md` | 5 Oct 2026 | Fontis seller credit, JV rig build years `[C]` |
