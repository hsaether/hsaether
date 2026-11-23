# Borr Drilling (BORR) — IAF analysis, stub Q4 2026 + 2027–2029

**Version 4 — 21 Nov 2026** (Q3 report of 18 Nov; Prospector 5 insurance; compacted to the lean rules, 724 lines → current state only) · price **$3.41** (NYSE close 20 Nov 2026; Oslo NOK 34.24) · skills: iaf-valuation **2026-11-18.1** (Step 6b); inputs Rig BBB 12 Nov interface with the 18–19 Nov turn calls and Borr Q3 note (rig-market-bbb 2026-11-18.1), Equity BBB 20 Nov note, HY BBB 18 Nov · **verdict: fails** (Base leaves no equity value; Bull 22.3%). **Hold (user, 7 Nov): updated on request; its value is the credit read for the Borr notes in `docs/hy-issuers.md`.**

## Summary

**Verdict**
- **Fails: the Base case still leaves no equity value.** At Rig BBB's Base mid-cycle ($110k a day for high-spec jackups, plus Borr's 8% premium) the 28 rigs are worth $1.73bn at end-2029 against **$2.16bn of net debt**: exit equity **−$0.35bn**, V_T $0, IRR_T −100%, P_k $0 against $3.41.
- **What changed (v3.2 → v4):** the Q3 report. The $200m hull value of Prospector 5 is recommended for payment (due 24 Nov) and goes to debt (+$258m at exit with the interest saved); Q3 EBITDA $78.9m was $4.5m below the model; four contract awards (Ran, Hild, Vali, Skald) add ~$8m `[A]`. Base exit equity −$615m → −$354m: still under water.
- **Bull 22.3%** (P_k $4.49, margin +31.6%; v3.2 18.6%): the insurance (+5.4 pp) more than offsets the higher price ($3.24 → $3.41, −1.7 pp).
- **Bear:** EBITDA cannot carry the ~9% coupons and the 5% amortisation from Jul 2027; liquidity runs out in 2028 and the funding gap reaches ~$400m by 2029 (v3.2 ~$660m): a restructuring case.
- **What the price needs:** a through-life jackup mid-cycle of **~$135k on Rig BBB's basis** for k (0% at ~$129k), above Rig BBB Bull ($130k); v3.2 ~$139k, v3.1 ~$146k. Today's EV ($3.19bn after the insurance) capitalises **~$122.5k**, about the transaction level ($119–123k).

**Base in brief**
- Rolling contracts re-price from Borr's ~$128k book to $97–113k for 2027 starts (Rig BBB rows × 1.08): about −15–25% on each. Base 2027 EBITDA **~$270m** against management's "broadly in line with 2026" (~$290m).
- **Where the value goes:** at Base mid-cycle a rig earns ~$7m a year of rig-level free cash; 28 rigs ~$198m a year against ~$180m of interest (after the insurance repayment) and ~$58m of G&A. Net debt barely moves (2,134 at end-2026 → 2,160 at exit), and three years of ageing take ~$0.17bn off the fleet.
- **Break-even:** a mid-cycle ~$135k (Rig BBB basis) with Base cash flows.

**Bear in brief**
- Story: oil Bear (Iran–USA deal plus an OPEC+ share fight) with Gulf rigs idled and moving to Asia; high-spec 92 / 88 / 85, SE Asia 72 / 70 / 70. Earliest H1 2027.
- Cash at the $100m floor in 2027, RCF fully drawn in 2028, gap ~$400m by 2029 even with the insurance. Equity wiped in a restructuring.

**Decision table** (USD per share; NYSE: BORR at $3.41, 20 Nov 2026; 309.1m shares)

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (20 Nov 2026 → 31 Dec 2029) | −100% | **−100%** | **+22.3%** |
| IRR_T in NOK on the Equity BBB NOK path | −100% | **−100%** (spot flat) | +21.1% |
| V_T per share (equity at exit) | 0 (−$2.58bn before new money) | **0 (−$0.35bn)** | **$6.39** ($1.97bn) |
| P_k (hurdle price) / margin of safety | $0 / −100% | **$0 / −100%** | **$4.49 / +31.6%** |
| Capital preserved? (ΣD_t + V_T vs $3.41) | No | **No** | Yes |
| Cumulative maintenance FCF per share, Q4-26 to 2029 | −$2.03 | **−$0.05** | +$1.46 |
| Net debt per share at exit | $9.04 before new money | **$6.99** | $5.53 |
| Balance sheet | Liquidity gone in 2028; gap ~$400m by 2029 | **No funding gap in the window: RCF ~$25m drawn at end-2029** (v3.2: $250m drawn + ~$40m gap) | Net debt falls to ~$1.71bn |

**Per-share path** ($ per share; no distributions in any scenario; v3.1 build plus the v4 adjustments `[A]`)

| | Q4-26E | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| **Base** EBITDA, $m | ~79 | ~270 | ~303 | ~303 |
| **Base** maintenance FCF per share | 0.01 | −0.13 | 0.04 | 0.03 |
| Debt amortisation per share (5% a year at 102.5% from Jul 2027; 2028 incl. the 2028 convertible) | 0 | 0.17 | 0.48 | 0.34 |
| Net debt per share, period end (insurance received 24 Nov) | 6.90 | 7.05 | 7.01 | **6.99** |
| V_t per share, year end (Base / Bull) | ~1.0 / ~1.0 (Noble-implied marks) | 0 / ~2.2 | 0 / ~4.3 | **0 / 6.39** |
| **Bear** maintenance FCF per share | 0.01 | −0.37 | −0.77 | −0.97 |
| **Bull** maintenance FCF per share | 0.01 | 0.16 | 0.52 | 0.73 |

- Maintenance FCF = EBITDA − tax − interest − maintenance capex, before debt amortisation (Step 2B). Interim V_t: rigs at the Noble-implied mark at end-2026 in every scenario, gliding to each scenario's mid-cycle at exit (Bull interim scaled from v3 `[A]`).

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value · `[E]` external or secondary · `[C]` carried from an earlier version or another workspace document · `[A]` own assumption · `[?]` not found.

## Header

| Item | Value |
|---|---|
| Company | Borr Drilling Limited (Bermuda). NYSE: BORR (primary); Euronext Oslo: BORR. Reports in USD, US GAAP. 28 wholly owned jackups (built 2008–2024) plus 50% of five ex-Fontis jackups in Mexico (BC Ventures) |
| Price (P) | **$3.41**, NYSE close 20 Nov 2026 (Yahoo `[F]`; 19 Nov $3.27, 18 Nov $3.24, the Q3 day). Oslo NOK 34.24 (20 Nov). USD/NOK 9.7525 (Norges Bank, 20 Nov) |
| Valuation / exit date | 20 Nov 2026 / 31 Dec 2029, **T = 3.113 years** |
| Shares | **309.11m** outstanding (30 Sep 2026 `[F]`; 315.4m issued). Convertibles out of the money, treated as debt: 2033 notes at $8.00 (37.5m shares), 2028 bonds at $6.94 (6.4m) `[F]` |
| Market cap / EV | **$1.05bn**. Debt principal **$2,534.4m** at 30 Sep `[F]`; cash $203.5m incl. restricted → net debt **$2,331m** `[B]`; **$2,131m pro forma** for the $200m insurance (24 Nov). EV ≈ **$3.19bn**; EV / 2026E EBITDA (~$290m) ≈ 11.0x |
| NAV at today's market marks | ~$1.0/share (rigs at the Noble-implied ~$123k on the convention, $2.33bn + firm premium ~$0.15bn + JV ~$0.04bn − pro forma net debt) `[A]` |
| NAV_0 (Base mid-cycle marks) | **Base ≈ −$0.20/share** (n.m.); Bear −$4.8; Bull ~$6.0 (P/NAV_0 ~0.6x) `[A]` (v3.1 −$0.85 / −$5.46 / $5.32 plus the insurance) |
| Track / k | **Track B** (short contracts into a cyclical rate path, finite-life rigs, high leverage). **k = 12%**; a leverage add-on would not change a P_k of zero |
| Distributions | None: last $0.02 in Mar 2025; the 2032/2034 note indenture restricts payments `[F]`; no buybacks or issuance in Q3 `[F]` |
| Horizon | Stub 21 Nov–31 Dec 2026 + 2027–2029; exit on normalised 2030 fleet values. Q4 report **17 Feb 2027** (Rig BBB) |

## Scenarios (from Rig Market BBB; jackup rows unchanged since 4 Oct, interface 12 Nov)

| | Bear | **Base** | Bull |
|---|---|---|---|
| Catalyst; earliest | Oil Bear (Iran–USA deal + OPEC+ share fight); Gulf rigs idled and moving to Asia. H1 2027 | NOC-led demand converts gradually; Gulf jackups return gradually | 2H26 FIDs and NOC programmes convert; Aramco/KJO absorb the Gulf rigs. Q2 2027 |
| High-spec $k 2027 / 2028 / 2029; mid-cycle (Borr × 1.08) | 92 / 88 / 85; 92 | **105 / 115 / 120; 110** | 118 / 135 / 145; 130 |
| SE Asia / Middle East 2027 | 72 / 79 `[A]` | **90 / 90** | 98 / 101 `[A]` |
| High-spec MCU 2027 / 2028 / 2029; mid-cycle | 84 / 82 / 81%; 82% | **89 / 91 / 91%; 88%** | 92 / 94 / 95%; 92% |
| Fleet working; stacked rigs | 67–73%; stay stacked to 2029 | **~83% in 2027, ~88% in 2028–29; back from Jul 2027** | ~91%; back from Apr 2027 |
| **Result: IRR_T / P_k / V_T** | **−100% / $0 / 0** | **−100% / $0 / 0** | **+22.3% / $4.49 / $6.39** |

- The stub is identical in all scenarios. Middle East and SE Asia Bear/Bull mid-cycle are scaled from the high-spec ratios `[A]` (Rig BBB has Base only).

## Company and status

- **Q3 2026** `[F]` (release 18 Nov; 6-K on EDGAR 20 Nov): revenue **$263.1m** (+13% q/q; dayrate $216.8m, bareboat $36.4m, management contracts $9.9m); adjusted EBITDA **$78.9m** (Q2 $43.8m); net loss $38.7m. Technical utilisation 98.0%, economic 97.3%; **22.9 rigs operating** on average.
- **Guidance** `[F]`: Q4 adjusted EBITDA "broadly in line with Q3, despite the Prospector 5 impact"; **FY2027 adjusted EBITDA "broadly in line with full-year 2026"** (~$290m on Q1–Q3 actuals plus Q4 ≈ Q3 `[A]`), Q1-27 sequentially lower, a strong ramp-up in Q4-27.
- **Contracting** `[F]`: coverage **79% for 2026, 52% for 2027** (no average rate given). Dayrate-equivalent backlog **$1.13bn** at the report date. YTD 30 commitments, ~6,300 days, $810m (~$129k a day `[B]`). Since Q2: nine commitments, ~$269m, > 1,950 days (~$138k `[B]`). 25 of 28 rigs contracted or committed.
  - **Ran:** 15-month extension with Eni in Mexico, committed to Dec 2027. **Hild** (warm stacked): binding LOA in Nigeria, 365 days firm from late Q1 2027, plus a 12-month option. **Vali:** Mellitah (Libya) to Sep 2027, plus 2 × 45 days. **Skald:** Vestigo option, Malaysia, into Jan 2027.
- **Prospector 5** (sank 24 Oct, Gabon; five people died) `[F]`: declared a total loss; hull and machinery insured value **$200m**; the claims leader **recommended payment of the insured value, due 24 Nov 2026**; net book value $94.8m at 30 Sep. No loss-of-hire cover; the BW Energy contract (~$45m firm) ended. Proceeds go "per the debt instruments" (debt repayment, capex or investments). DNV investigates; cause not established.
- **Balance sheet at 30 Sep** `[F]`: cash $202.6m + restricted $0.9m; $250m RCF undrawn → **liquidity $452.6m**. Debt principal $2,534.4m: $1,100m 8.75% notes 2032, $935m 9.00% notes 2034 (both amortise 5% a year at 102.5% from Jul 2027), $300m 3.5% convertible 2033, $44.2m 5% convertible 2028, $155.2m Noble seller's credit 2032. RCF covenants loosened to 31 Mar 2028 (interest cover 1.2×, net leverage 8.0×).
- **Mexico:** 51% of Perfomex sold (18 Sep); Galar, Gersemi, Njord on bareboat to PEMEX. Fontis JV: $287m for five rigs (Jul 2026), $237m non-recourse seller credit (10/12/14%, ~Jan 2029); Borr's exposure $40m.
- **Market (CEO, 18 Nov)** `[F]`: "an increasing number of opportunities in Southeast Asia and West Africa"; marketed utilisation for modern jackups ~93% (90% nine months ago); priority "maximizing fleet utilization" with discipline on longer commitments.

## Market input and common assumptions

| Item | Value | Basis |
|---|---|---|
| Open-day rates | Rig BBB rows × 1.08 (Borr premium) for work starting in that year | Borr's awards (~$123–138k incl. mobilisation) vs the leading-edge median; halved for mobilisation fees `[A, anchored B]` |
| Booked rates | ~$128k on the pre-August book; ~$120k on later awards; Joro $80k | Backlog ÷ firm days `[B]` |
| Open-day utilisation | Row MCU − 5 pp; stacked rigs back Jul 2027 (Base), Apr 2027 (Bull), Jan 2029 (Bear), $5m each | `[A]` |
| Revenue efficiency / opex | 96% / $63k per working day (2026, +3% a year; blended incl. bareboat rigs); idle $30k warm, $12k cold | Q3 economic utilisation 97.3% `[F]`; Q1-26 calibration `[A]` |
| G&A / tax / maintenance capex | $56m / $57.5m / $59m (2027–29); 4.5% of revenue; $65m / $70m / $75m | `[F/A]` |
| Interest | Notes 8.87% on outstanding; convertibles 3.5% / 5%; Noble credit 7.5% → 10.5%; RCF fee ~$3m | `[F/A]` |
| **Insurance (v4)** | $200m received 24 Nov, applied to debt; interest saved at 8.9% (+$58m to exit); kept as cash at 4% is a sensitivity (+$25m) | Q3 release `[F]`; use `[A]` |
| **Q3 awards (v4)** | Ran firm to Dec 2027; Hild from late Q1 2027 instead of a Jul 2027 reactivation; Vali to Sep 2027; Skald to Jan 2027: ~+$8m to exit `[A]` | Q3 release `[F]` (rates not disclosed) |
| Liquidity | $100m minimum cash; RCF drawn first; any further gap shown as a funding gap | `[A]` |
| Exit values | Rig BBB convention: value per rig = annual rig cash flow × 8% annuity over 30 − age, $10m floor; rate = high-spec mid-cycle × 1.08, MCU 82 / 88 / 92%; G&A and financing excluded | Rig BBB rev 2026-10-08.2 |
| Backlog at exit | 2030 / 2031 rig-days under scenario-signed contracts = 0.50 / 0.20 × the 2029 working share, at the 2029 row rate | Borr's book shape `[B/A]` |
| JV | Stake = 50% × (rigs − $237m debt) + $15m loan, floored at zero | `[A]` |

- **Model:** `.claude/skills/iaf-valuation/references/models/borr/v4.py`, an adjustment layer on the v3.1 rig-by-rig build (equity at exit Bear −2,844 / Base −615 / Bull +1,713 $m), which was not kept as a script. The full rebuild follows at the next run that needs it (Q4, 17 Feb 2027, if the hold is lifted).

## Exit value V_T

**V_T bridge, Base ($m)**

| Step | $m |
|---|---|
| Rigs at Base mid-cycle at exit (28 rigs, ages 6–22) | 1,726 |
| + firm-today premium after exit (Galar, Gersemi to May 2030) + premium on backlog signed in the Base + reversion tail (high-spec gap +12.8%, no named reason) | +6 +39 +35 |
| + JV stake (five rigs worth ~$116m against $237m of debt) | 0 |
| − net debt at exit (v3.1 2,421 − insurance 200 − interest saved 58 + Q3/Q4 5 − contracts 8) | −2,160 |
| **= equity at exit** | **−354 → V_T 0** (limited liability) |

| Exit, $m | Bear | **Base** | Bull |
|---|---|---|---|
| Owned fleet (28) | 280 | **1,726** | 3,573 |
| Backlog premium / tail / firm premium / JV | −29 / −52 / 13 / 0 | **+39 / +35 / 6 / 0** | +45 / 0 / 0 / 64 |
| Net debt at exit | 2,795 before new money | **2,160** | 1,708 |
| **Equity / V_T per share** | **−2,583 / 0** | **−354 / 0** | **1,974 / $6.39** |

- **Exit consistency:** the Base high-spec block's year-3 earnings (120 × 91%) are 12.8% above the mark (110 × 88%) with no named recovery reason: a reversion tail (+$35m). Bull high-spec (+15.2%) has a named reason (Rig BBB: the asset market prices jackups at ~$119–123k, at or below Bull mid-cycle), tail as a sensitivity. Bear SE Asia and Middle East carry negative tails.
- **Exit cross-check (Equity BBB 20 Nov, Oslo):** Base and Bear equity is negative, so the ratios are not meaningful. Bull exit P/B ~1.8 against Oslo's Bull 2.00; a buyer at NAV earns ~7.5% on the levered equity against Oslo's Bull mid-cycle return 9.2% (re-discounted Bull: 19.6%).
- **Cross-checks:** book value of the rigs $105m a rig (30 Jun) `[F]`; Noble paid $72m a rig, Fontis $57m; Base exit values $41–75m a rig, 3 years older. Prospector 5's insured value ($200m, 2014 build) is ~2.8× the Noble price per rig: hull cover, not a market mark.

## Growth capex test

- **No growth capex committed.** Reactivating the four stacked rigs ($20m) sits in maintenance FCF and clears k if they find work (~$13m of EBITDA a year each at Base rates); Hild's Nigeria award is the first.
- **Fontis JV** (sunk, $40m): stake at exit Base $0, Bull $64m; non-recourse caps the loss. **Noble five rigs** ($360m, Jan 2026, sunk): accretive only on Bull-level values.

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (USD) / NOK path | −100% / −100% | **−100% / −100%** | +22.3% / +21.1% |
| d / g / c | 0 / −100% / 0 | **0 / −100% / 0** | 0 / +22.3% / 0 |
| ΣD_t / V_T | 0 / 0 | **0 / 0** | 0 / $6.39 |
| P_k / margin of safety | $0 / −100% | **$0 / −100%** | $4.49 / +31.6% |
| Rule 3: P/FCF normalised vs ceiling | n.m. | **n.m. (FCF_normalised negative: −$0.44/share after the renewal charge `[A]`)** | above the ceiling |
| Capital preserved? | No | **No** | Yes |

- **Share of Bull already priced:** (3.41 − 0) / (4.49 − 0) = **76%** (v3.2 83%).
- **Base liquidity:** with the insurance applied to debt, the RCF is ~$25m drawn at end-2029 and there is no funding gap in the window (v3.2: fully drawn plus ~$40m). Amortisation continues from 2030 ($51m a half-year).
- **Bear survival:** RCF fully drawn in 2028; gap ~$400m by 2029: a restructuring.

**Sensitivities** (USD; at $3.41)

| Change | V_T | IRR_T | P_k |
|---|---|---|---|
| **Base** | 0 | −100% | 0 |
| Base cash flows, exit mid-cycle $120k / $130k / $140k (Rig BBB basis) | 1.36 / 3.87 / 6.20 | −25.5% / +4.1% / +21.2% | 0.96 / 2.72 / 4.36 |
| **Break-even exit mid-cycle** (Base cash flows) | | 12% at **~$135k**; 0% at ~$129k | |
| Management's FY2027 EBITDA (~$290m vs ~$270m) in Base | 0 (equity −$0.33bn) | −100% | 0 |
| Bull, insurance kept as cash at 4% | 6.28 | +21.7% | 4.41 |
| Bull with the reversion tail | 6.57 | +23.4% | 4.61 |
| Bull, contracts firm today only | 6.23 | +21.3% | 4.38 |
| Bull, exit marks at Oslo's Bull mid-cycle return (9.2%) | 5.96 | +19.6% | 4.19 |
| Bull without the insurance (v3.2 basis) | 5.55 | +16.9% | 3.90 |

- **Exit values decide everything.** Bull cash flows cannot make up for Base exit values; only a mid-cycle above Rig BBB Bull, or several favourable assumptions together (Bull rates + Borr's own opex + a 35-year rig life), clears 12% with margin.

## Price versus our call (Step 6b)

| Item | Reading (21 Nov) | Score |
|---|---|---|
| **What the price implies** | EV $3.19bn capitalises a through-life ~$122.5k (Rig BBB basis): the transaction level; k needs ~$135k to exit | — |
| Sector turn calls (Rig BBB 18–19 Nov) | High-spec jackups 2027–28 **lower** (50%, watch; L5 only): would cut Bull 2027–28 cash, not Base (already zero); the Q3 read "neither confirms nor reverses" | −1 |
| Contract behaviour | Ran 15-month Eni extension, Hild 365-day Nigeria award for a stacked rig, Vali and Skald extensions (18 Nov `[F]`); nine awards since Q2 at ~$138k `[B]` | +1 |
| Order intake and backlog | Backlog $1.13bn; 2027 cover 52% | 0 |
| Guidance vs consensus | FY2027 EBITDA ≈ FY2026 (~$290m) against our Base ~$270m; Q4 ≈ Q3 | +1 |
| Asset sale vs book | Prospector 5: $200m insured value recommended against a $94.8m book value | +1 |
| Insiders and issuance | Trøim bought ~13.8m shares (~$63m) in 2026, 8.0m on 6–15 Oct at $4.24–4.93 `[F]`; none checked since Q3 `[?]`; no issuance | +1 |
| **Net (company)** | | **+4** |

- **Verdict line: ahead of the price, on the negative side.** The market capitalises the rigs at the transaction level (~$122.5k), the price that buyers paid for similar rigs; our Base uses Rig BBB's mid-cycle ($110k), 8–12% below the transactions, and at that level the levered equity is under water. The company's own signals point the other way (awards, guidance, insurance), but a company signal does not move the sector row. The dispute is Rig BBB's mid-cycle (open checkpoint 13), not Borr.
- **Scorecard:** opened 21 Nov 2026 at $3.41 (Base $0). Hit if 2027 jackup fixtures print below ~$110k or Borr falls toward its NAV at market marks (~$1.0); miss if 2027 fixtures hold ≥ $125k and Borr's 2027 EBITDA meets the guide (Q4 report, 17 Feb 2027).

## Verdict and caveat

- **Band applied:** Base margin of safety −100%: fails (Summary). Bull is above k, as a stress-test outcome, not a margin of safety.
- **What would flip it:** a Rig BBB mid-cycle review toward the transaction-implied rates *and* above them (≥ ~$135k); sourced rig opex materially below $75k a day together with a Bull-level mid-cycle. Stub, payout and k do not matter.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation or a price target. It ignores the option value of limited liability: equity in a levered company with debt due 2032–34 can trade above a zero-NAV floor for years. The v4 adjustments sit on the v3.1 rig-by-rig build `[A]`.

## Tracking

| Version | Date / price | Base V_T / IRR | Bull IRR / P_k | Break-even mid-cycle | What changed |
|---|---|---|---|---|---|
| v3.1 | 25 Oct / $4.40 | 0 / −100% (equity −615) | 7.6% / $3.87 | ~$146k | Prospector 5 lost, no insurance |
| v3.2 | 7 Nov / $3.24 | 0 / −100% | 18.6% / $3.88 | ~$139k | Price −26% |
| **v4** | **20 Nov / $3.41** | **0 / −100% (equity −354)** | **22.3% / $4.49** | **~$135k** | Q3: insurance $200m, EBITDA $78.9m (model $83.4m), four awards |

- **Q3 against the model:** EBITDA −$4.5m (Odin and transitions behind); rigs operating 22.9 against ~22.5 modelled; liquidity $452.6m against ~$450m. Behind on EBITDA, ahead on contracts and cash (insurance): net +$0.26bn of exit equity.

## Risks and signposts

| Signpost | Bear | Base | Bull | Now (21 Nov) |
|---|---|---|---|---|
| Borr's realised rate on 2027 starts | < $100k | $100–120k | > $130k | Awards since Q2 ~$138k incl. mob `[B]` |
| Q4-26 EBITDA (17 Feb 2027) | < $70m | ~$79m (guide ≈ Q3) | > $90m | Q3 $78.9m |
| FY2027 EBITDA guide | < $250m | ~$270m | > $320m | "Broadly in line with 2026" (~$290m) |
| Working rigs | < 21 | 22–23 | ≥ 24 | 22.9 (Q3) |
| Stacked rigs (Freyja, Groa, Var; Hild from late Q1 2027) | Stacked through 2027 | Back by H2-27 | Back by Q2-27 | Hild awarded; three stacked |
| High-spec MCU (Westwood / Borr) | < 84% | 88–91% | > 92% | Borr: modern ~93% |
| Jackup transaction marks | < $60m for 2013–14 rigs | $70–90m | > $110m | Noble $72m, Fontis $57m |
| Liquidity (cash + undrawn RCF) | < $250m | $250–450m | > $500m | $452.6m (30 Sep) + $200m insurance (24 Nov) |
| Prospector 5 insurance | Payment disputed or delayed | Paid 24 Nov | — | Recommended; due 24 Nov |
| Gulf operations | Suspension notices | Gradual return | Aramco recalls 6–9 rigs | No suspension (Arabia II, III, Forseti) |
| Insider buying | Insiders sell | Occasional | Continued buying | Trøim 8.0m in Oct; none checked since |
| Short interest (FINRA) | > 35m shares | 25–33m | < 20m | 34.5m (30 Sep; partly convertible hedging) |

- **Other risks:** customer credit (West Africa, PEMEX); Middle East insurance and fuel costs; the Prospector 5 investigation (client reviews of preload procedures); dilution if liquidity tightens in the Bear.

## For other modules

- **`docs/hy-issuers.md` (the reason this analysis is kept):** credit-positive versus v3.2. The $200m insurance goes to debt (net debt $2.33bn → $2.13bn pro forma) and Base no longer exhausts the RCF in the window (~$25m drawn at end-2029); covenants loosened to Mar 2028. Bear still cannot service the notes from 2028 (gap ~$400m by 2029). Status Watch is consistent with this; the 2032 / 2034 notes amortise 5% a year at 102.5% from Jul 2027. Read at its next price round (~4 Dec).
- **Rig Market BBB:** Q3 company data (marketed utilisation for modern jackups ~93%; nine awards ~$138k incl. mobilisation; Hild's Nigeria award; SE Asia and West Africa "increasing opportunities") are Bull-side for the jackup watch call; a typical contract term and jackup opex per operated rig remain open (checkpoint 13).
- **Equity BBB, Oil BBB:** read only; no input back.

## Change log

- **21 Nov 2026 — v4 (on request; iaf-valuation 2026-11-18.1):** Q3 report (EBITDA $78.9m; FY2027 ≈ FY2026), Prospector 5 insurance $200m recommended (to debt, +$258m with interest), four awards (+$8m `[A]`); price $3.24 → $3.41 (20 Nov). Base still zero (exit equity −$615m → −$354m; no funding gap in the window); **Bull 18.6% → 22.3%, P_k $3.88 → $4.49**; break-even mid-cycle ~$139k → ~$135k. Step 6b added (ahead, negative side). Compacted 724 lines → lean; adjustment model `borr/v4.py`.
- **7 Nov 2026 — v3.2 (price re-mark):** $4.40 → $3.24; Bull 7.6% → 18.6%, P_k $3.88; Base and Bear zero.
- **25 Oct 2026 — v3.1:** Prospector 5 sank 24 Oct; fleet 29 → 28, no insurance counted; Base exit equity −$506m → −$615m; Bull 11.2% → 7.6%.

## Appendix: own assumptions `[A]`

By weight on the result: (1) the Rig BBB high-spec mid-cycle × 1.08 for exit values; (2) the asset-value convention ($75k opex, 30-year life, 8%, $10m floor); (3) booked rates on the pre-August book (~$128k) and later awards (~$120k); (4) open-day utilisation MCU − 5 pp and the stacked-rig return dates; (5) the insurance applied to debt at 8.9%; (6) the Q3-award adjustment (+$8m) and the Q3/Q4 EBITDA adjustment (−$5m) on the v3.1 build; (7) backlog at exit (0.50 / 0.20 × the 2029 working share); (8) the JV at 0.9 × the high-spec rate with debt flat; (9) Middle East and SE Asia Bear/Bull scaled from high-spec ratios.

## Appendix: sources

| # | Source | Content | As of |
|---|---|---|---|
| S1 | [Borr Q3 2026 release (6-K ex. 99.1)](https://www.sec.gov/Archives/edgar/data/1715497/000114036126044994/ef20085971_ex99-1.htm) and [ex. 99.2](https://www.sec.gov/Archives/edgar/data/1715497/000114036126044994/ef20085971_ex99-2.htm) | Q3 results, guidance, coverage, backlog, liquidity, debt, Prospector 5 insurance, awards, CEO comments | 18 Nov 2026 (filed 20 Nov) |
| S2 | [Borr Q3 interim financial report (6-K)](https://www.sec.gov/Archives/edgar/data/1715497/000162828026074853/q320266-k.htm) | MD&A; Prospector 5 book value $94.8m; covenants | 18 Nov 2026 |
| S3 | Borr Q2 2026 release, interim report and presentation; releases of 15 and 30 Sep; Prospector 5 releases 24 Oct–2 Nov (EDGAR, Newsweb) `[C]` | Q2 baseline, fleet, debt terms, incident | Aug–Nov 2026 |
| S4 | Yahoo (BORR, BORR.OL; insider module, short interest); Norges Bank EXR | Prices to 20 Nov; insider trades; short interest 30 Sep; USD/NOK 9.7525 | 20 Nov 2026 |
| S5 | `docs/rig-market-bbb.md` (12 Nov interface; 18–19 Nov turn calls and Borr Q3 note), `docs/equity-market-bbb.md` (20 Nov note), `docs/hy-market-bbb.md` (18 Nov), `docs/hy-issuers.md` (19 Nov) | Jackup rows, MCU, asset values, watch call; exit references, NOK path; credit status | 12–20 Nov 2026 |

- **Validation:** the v4 adjustments are added to the v3.1 equity at exit (Bear −2,844 / Base −615 / Bull +1,713 $m) in `borr/v4.py`; with no adjustments it gives the v3.1/v3.2 Bull V_T $5.55 (16.9% at $3.41; 18.6% at $3.24 on 7 Nov). Earlier versions and their full tables are in git history.
