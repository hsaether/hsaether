# Review: Equity Market BBB, skill and report — 18 Oct 2026

Skill revision behind this review: **equity-market-bbb 2026-10-17.3** (the revision the report was
written under). Upstream skills: iaf-valuation 2026-10-11.3, ai-market-bbb 2026-10-17.1,
oil-market-bbb 2026-10-11.1, hy-market-bbb 2026-10-18.1.

**Questions (user):** review the Equity Market BBB skill and `docs/equity-market-bbb.md` (17 Oct,
Update 1); check that Oslo and World are reported the same way; check the quality of P/B, ROE and
dividend yield.

**What was done:**
- Re-ran `references/osl.py` and `references/upd.py` (with `fund/idxai3.py`) in the scratchpad.
- Re-read the MSCI Norway and MSCI World index pages (data as of 30 Sep 2026).
- Fetched Yahoo fundamentals for the 14 Oslo sample names (close 16 Oct 2026).
- Re-read the source of the P/B band (Nordnet blog, 4 Apr 2023).

Numbers tagged `[A]` are my own arithmetic. No change was made to the skill or the report.

## Answer in brief

- **The numbers reproduce.** Every Oslo and World figure in the Interface tables comes out of the
  scripts unchanged: returns, IRR, P_k, E / R and all eight trigger levels. The one exception is
  the Brent sensitivity of the Oslo trigger (section 4, item 2).
- **The headline measures hold:**
  - Oslo P/B 2.34, trailing P/E 13.34 and dividend yield 4.80% match MSCI's page.
  - Rebuilt from the 14 names at 16 Oct prices: P/B **2.36**, P/E 13.3, implied ROE **17.7%**
    (the report has 17.5%).
  - World P/B 4.10, P/E 22.69 / 17.92 and yield 1.52% match MSCI.
- **Oslo and World are built under different rules.** World got the new block method on 17 Oct;
  Oslo kept the 11 Oct model. Six differences matter:
  1. Retained cash is credited in World but not in Oslo. Oslo energy at World's rule (c = 0.80):
     Oslo Base **2.3% → 2.8%**.
  2. Payout is set per block in World and is one flat 66% in Oslo.
  3. P/B and ROE are cross-checked for Oslo only.
  4. World's total P/E path is not shown.
  5. World's return split and structural run are incomplete.
  6. The sensitivities are not like for like, and World has **no FX sensitivity**. NOK ±10% by
     2029 moves World Base to **1.8% / 8.4%**, its largest single sensitivity.
- **P/B is right, but it is read against a history that does not fit:**
  - The 1.5–2.1 band is from OSEBX (67 names, 2010–2023). The 2.34 is MSCI Norway (12 names).
  - Kongsberg alone (P/B 22.5) adds ~0.19 to today's P/B. It was a small weight during the band
    years. Without it the sample P/B is 2.17.
  - The source also says P/B 2.4–2.7 has often been followed by losses. The report leaves that
    out, and its signposts treat P/B > 2.6 as a **Bull** sign.
- **ROE needs a stated basis and an exit check:**
  - 17.5% is the trailing figure; on forward earnings it is ~20%. The "normal ~13%" divides a
    single P/B reading (Apr 2023) by a 10-year P/E average from another source.
  - The exit check the skill asks for is missing. Run here `[A]`: Oslo's Base exit implies P/B
    **1.74** at ROE 15%, inside the band, which supports the 11.5 exit P/E. World's Base exit
    implies P/B **3.1** at ROE 18%, with no history in the report to judge it against.
- **The dividend yield is mostly peak-cycle prints:**
  - The bottom-up 5.0% includes Frontline at 19.9%, which adds 0.5 pp on a 2.5% weight. It also
    includes Aker BP, Subsea7 and Vår paying 90–113% of trailing earnings.
  - The cash yield of ~5.6% assumes ~0.7% buybacks with no source.
  - World shows only the 1.52% dividend yield. The model's 2.6% cash yield (payout 45%) is not
    reported.
- **Three small errors:**
  1. World forward P/E today is ~17.9, not 17.7: the report scaled from 9 Oct, not from 30 Sep.
     World trigger P/Es are therefore ~0.2 too low.
  2. Oslo's "±11% trigger per $10 Brent" cannot be reproduced with the stored script, which gives
     ±4%.
  3. The claim that the P/B form of a trigger does not drift is wrong. Book grows ~0.5% a month.
- **None of this changes the stance.** Both indices stay well below HY on E / R. Oslo at c = 0.80
  has E / R ≈ −0.06 against −0.08 `[A]`.

## 1. Reproduction check

| Item | Report | Re-run (scripts in `references/`) |
|---|---|---|
| Oslo Bear / Base / Bull window | −4.1 / 2.3 / 6.0 | −4.09 / 2.29 / 5.95 |
| Oslo E, R, E / R | −2.29, 28.6, −0.08 | −2.29, 28.6, −0.080 |
| Oslo triggers | 1,622 / 1,615 / 1,848 / 1,433 | same |
| World NOK Bear / Base / Bull window | −1.5 / 5.2 / 10.1 | −1.45 / 5.21 / 10.10 |
| World E, R, E / R | 0.63, 25.4, 0.025 | same |
| World triggers | −13.6 / −17.5 / −4.8 / −22.0% | same |
| Oslo trigger 1 at Brent ∓$10 | 1,448 / 1,796 (±11%) | `osl.py`: **1,558 / 1,683 (±4%)**. The report's figures come back only if the Bear path moves too (section 4, item 2) |

## 2. Oslo against World: consistency

| # | Item | Oslo | World | Problem | Fix |
|---|---|---|---|---|---|
| C1 | Retained cash | None. Payout 66%; the 34% retained is assumed to go to field decline and O growth (Base EPS still falls 2.1% a year) and adds nothing to V_T | AI layers and energy credit (c − payout) × EPS in V_t; energy c = 0.80 | The same energy business is valued on two rules. Oslo energy at c = 0.80: Base **2.29 → 2.76%**, Bear −3.71, Bull 6.37. At c = 1.0: Base 3.41 `[A]` | One rule for both indices in Step C. Oslo energy gets c (0.80 as in World) or a stated reason why not |
| C2 | Payout | 66% for every block | Per block: energy 55%, rest ~49%, AI layers 15–45%, companies from their analyses | Oslo energy's latest declared dividends come to 76% of trailing EPS (61% on dividends actually paid; bottom-up). World energy is set at 55% | Payout per block for Oslo (E / F / O). Use the same energy payout in both, or explain the gap |
| C3 | Valuation anchor vs model index | Multiples: MSCI Norway (12 names, DNB 19%). Earnings: OBX top-14 (DNB 10%). Price: OSEBX | MSCI World, URTH weights and URTH price: one index | P/B agrees (2.28–2.36). Dividend yield does not: 4.43% on MSCI weights vs 4.93% on OBX weights | State the index behind each multiple; give the bottom-up figure on the model's weights next to MSCI's |
| C4 | P/B and ROE | P/B with a history band; implied ROE 17.5% (basis not stated); P/B in the triggers | P/B 4.10 shown, nothing else. No ROE (trailing 18.1%, forward ~23% `[A]`) | Same trailing ROE (17.5 vs 18.1%) but P/B 2.34 vs 4.10. The World premium is a P/E (growth) premium, not a profitability premium. The report cannot say this | One P/B–ROE table for both indices: today (trailing and forward), exit (section 3.3), history |
| C5 | Cash yield | Dividend 4.80% (MSCI), 5.0% (bottom-up), cash yield ~5.6% `[A]` | Dividend 1.52% only; the model's d = 2.6% (payout 45%, ~1% buybacks) is not shown | Not comparable as shown | Same three rows for both: trailing dividend, forward dividend, model cash yield with buybacks |
| C6 | Forward P/E path | Index path 12.0 → 11.7 / 11.6 / 11.5 | Only the rest (17.0 → 17.2 / 16.7 / 16.3) and the layer exit P/Es | World's total value multiple (V_t / EPS_t+1) is Base **17.1 → 17.6 / 17.3 / 17.0**, Bear 15.0, Bull 18.2–18.6 `[A]`. That is a +3% re-rating in 2027, partly memory's P/E rising as its EPS falls. It sits at the top of the stated 16.5–17 anchor | Add the World total row. Note when a block's P/E rise comes only from falling earnings (the fund-mode rule) |
| C7 | Return split | g split into EPS growth −2.1% and re-rating −1.4%; structural run 2.0% | EPS growth +2.7%; re-rating "by block"; structural run "not run" | World's split can be computed: re-rating ≈ 0 (17.07 → 17.0 including retained cash) `[A]`. The "small de-rating" in the text is the rest's only | Report World's split as numbers; run a structural case on blocks, or exempt World in the skill's checklist |
| C8 | Multiple sensitivity | ±1 on 11.5 (±8.7%): −0.3 / 4.7 | ±1 on ~17 (±5.9%): 3.6 / 6.8 | Uneven shocks. At ±8.7% World gives **2.8 / 7.5** `[A]`, as large as Oslo. The text says "World's risk is the multiple", but the table makes it look smaller | Shock both by ±10% (or show both) |
| C9 | FX sensitivity | Not shown (only the 1.5% move since 9 Oct: 2.59 vs 2.29) | Not shown, although the skill asks for it | NOK −10% / +10% by 2029: World Base **8.4% / 1.8%** `[A]`, larger than any sensitivity reported | Add for both indices |
| C10 | FX translation | Energy and half of O on USD/NOK; Mowi (EUR) and other EUR earners also on USD/NOK | 100% of World on USD/NOK; the skill says "≈ 70% USD" | With 30% on I-44 (Bear +8 / +6 / +6%): World Bear 2027 −20.6% (vs −19.8%), E / R 0.024 (vs 0.025) `[A]`. Small | USD share on USD/NOK, the rest on I-44, as fund mode step 5 already does |
| C11 | Trigger multiples | Trigger 1: P/B and P/E; trigger 2: none; pre-alert and HY book: P/B only | Forward P/E on every row | Uneven rows | Every row: level, %, forward P/E; plus P/B for Oslo |
| C12 | Mid-cycle return | 9.0% = cash yield 5.7% (0.66 / 11.5) + growth 3.3% (implied, not stated) | 7.5% = 2.6% (0.45 / 17) + 4.9% (implied); not re-derived after the rest got 5.5% trend growth | The pension conclusion "Oslo 9.0% > World 7.5%" rests on growth figures nobody stated. ROE × retention gives ~5.1% (Oslo) and ~10% (World), so both assume retained earnings earn well below ROE `[A]` | State payout, P/E and growth per index; say why growth is below ROE × retention (dilution, field decline) |
| C13 | Refresh in Update 1 | Norway 10-year and the Oslo yield gap still 8 Oct; I-44 110.56 (9 Oct) in the NOK section vs 109.52 in Metadata | US 10-year refreshed in signposts (+0.6 pp) but the snapshot keeps +0.4 pp | Two values for one measure in one file | Mark not-refreshed sections in their headings, or refresh both indices the same way |

Also noted, minor:
- World energy uses Oslo's B_cons ($79, from Equinor's consensus) for a sector that includes
  refiners and midstream.
- Oslo Bull EPS in 2027 (104.7) is below Base (105.2). Bull keeps oil on Base and firms the NOK.
  That is correct, but say it, because a reader expects Bull ≥ Base.
- The upstream table lists HY BBB as "5 Oct (amended 11 and 15 Oct)"; it is now the 17 Oct
  baseline. The values used are unchanged: NIBOR 4.79 / 4.39 / 3.86, reference 0.196, HY book
  0.291.

## 3. Key measures

### 3.1 Values against sources

| Measure | Report | Check (MSCI page 30 Sep; Yahoo 16 Oct close) | Verdict |
|---|---|---|---|
| Oslo P/B | 2.34 (MSCI Norway) | MSCI 2.34 ✓. Bottom-up: 2.36 (OBX weights), 2.28 (MSCI top-10 weights), 2.53 (market cap), **2.17 without Kongsberg**, 2.09 also without Gjensidige and Vår | Correct; composition-driven (section 3.2) |
| Oslo P/E trailing / forward | 13.34 / 11.91 | 13.30 / 12.03 bottom-up | Correct |
| Oslo implied ROE | 17.5% | 17.7% (P/B ÷ P/E); Yahoo ROE, book-weighted, 17.6%; on forward P/E 19.6%. Blocks: E 20.7%, F 16.2%, O 16.2% | Correct; basis (trailing) not stated |
| Oslo dividend yield | 4.80% (MSCI); 5.0% bottom-up forward | MSCI 4.80% ✓ (trailing 12 months). Bottom-up 4.93%; **4.45% without Frontline**; 4.43% on MSCI weights | Correct as prints; not a sustainable yield (section 3.4) |
| World P/B, P/E, yield | 4.10; 22.69 / 17.92; 1.52% | MSCI ✓ | Correct |
| World ROE | — | 18.1% trailing, ~23% forward `[A]` | Missing |
| World forward P/E today | ≈ 17.7 | URTH 30 Sep 206.23 → 16 Oct 206.34 (+0.05%): **≈ 17.9** | Error (section 4, item 1) |

### 3.2 P/B

- **The level is solid.** Four bottom-up weightings land at 2.17–2.53 around MSCI's 2.34.
- **The history it is read against is weak and not like for like:**
  - The 1.5–2.1 band comes from one blog post (Nordnet, Apr 2023): OSEBX, 67 names, Bloomberg,
    13 years. It is a rule of thumb from three named analysts, not a measured distribution.
  - Index composition has changed since the band years:
    - Kongsberg is now 7–10% of the index at P/B 22.5 (a defense re-rating on a small book, NOK 14
      a share). It was a much smaller weight in the band years. It adds ~0.19 to the index P/B.
    - Gjensidige (6.1) and Vår (6.8) add more.
    - Equinor's weight has fallen from about a third (2023) to 16–20%.
  - On a 2023-like mix Oslo is at ~2.1–2.2: the top of the band, not 0.25 above it.
- **The source's own warning is left out.** It says buying at 2.4–2.7× book has often been
  followed by losses. The report's signpost and recalibration band (1.9–2.6) calls > 2.6 a
  **Bull** threshold. A rising P/B is a valuation warning; it confirms Bull only if earnings
  rise with it.
- **The P/B form of a trigger drifts.** Book grows by retention, ~34% × ~20% ROE ≈ 0.5% a month
  `[A]`. At a fixed index level the P/B falls about that much each month. Only the P/E form at
  unchanged earnings is drift-free. The report says neither form drifts.
- **World P/B is shown but never used.** No history, no exit check, no trigger.

### 3.3 ROE and the exit check

- **The basis must be stated.** P/B ÷ trailing P/E = 17.5%; P/B ÷ forward P/E ≈ 19.6%. The report
  gives 17.5% unlabelled, and "ROE ~15–17%" in the payout check without a derivation.
- **The "normal ~13%" is weak.** It is 1.8 (OSEBX P/B on one day, Apr 2023) ÷ 13.5 (a 10-year
  trailing P/E for "Norway" from an undated Swedish article). That is two indices and a point
  value against an average. Keep it only as a rule of thumb `[E/A]`.
- **The exit check the skill asks for** (Step C: cross-check the exit P/E with P/B against ROE).
  Book_T = book today + Σ (EPS − payout); exit P/B = V_T / book_T `[A]`:

| Base (Bear / Bull) | Oslo | World |
|---|---|---|
| P/B at 16 Oct | 2.37 | 4.10 |
| ROE on 2027 EPS (opening book) | 20.4% | ~23% |
| ROE in 2030 (normalised EPS) | **15.2%** (14.2 / 15.7) | **18.4%** (16.7 / 19.7) |
| Exit P/E (value multiple for World) | 11.5 (10.5 / 12.5) | 17.0 (15.0 / 18.6) |
| **Exit P/B** | **1.74** (1.49 / 1.96) | **3.13** (2.51 / 3.65) |
| Against history | Inside the 1.5–2.1 band: the exit P/E 11.5 is consistent | No history in the report. 3.1 means ROE stays ~18%, the "structurally high" World assumption, made explicit |

  World figures take CY26 EPS as CY27 ÷ 1.13 for the stub `[A]`; the exit P/B moves < 0.05 with it.

- **The payout check runs one way only.** The skill flags growth above ROE × retention, but not
  the reverse:
  - Oslo retains 34% while Base EPS falls, so ROE goes from 20% to 15%. The report calls that
    "consistent" without showing it.
  - It is the normalisation, and it lands inside the P/B band. The skill should make this
    visible instead of the bare word "consistent".

### 3.4 Dividend yield and cash yield

- **Three different measures sit side by side, unlabelled:**
  - MSCI's trailing 12-month yield (4.80%).
  - Yahoo's `dividendYield`: the latest declared dividend annualised (5.0%).
  - The model's cash yield, dividends plus net buybacks (stub 5.6%, 2027 5.8%, window d 5.4%).
- **The forward print is peak-cycle:**
  - Frontline's 19.9% is one strong tanker quarter annualised. On a 2.5% weight that is itself an
    assumption, it adds 0.48 pp.
  - Aker BP pays 113% of trailing EPS, Subsea7 94% and Vår 90%.
  - The energy block's 6.1–6.3% is not what the Base energy path (−27% by 2030) can carry. The
    model is right to pay 66% of modelled EPS rather than the printed yield. But the snapshot's
    "5.0%" reads as a sustainable yield.
- **Buybacks have no source.** The 66% payout is the same as the sample's dividend run rate ÷
  trailing EPS. On CY27 consensus, dividends are ~58% of EPS, so the model assumes ~0.7% buybacks.
  There is no source for that.
- **Known quirk confirmed.** Yahoo `trailingAnnualDividendYield` is wrong for USD reporters
  (Equinor 0.36%). The skill already says so.
- **World:** 1.52% trailing dividend yield against a model payout of 45% (cash yield 2.6%)
  implies ~1% net buybacks `[A]`. Reasonable, but not stated.

## 4. Errors and smaller points

1. **World forward P/E scaling.** The report takes MSCI's 30 Sep 17.92 × the URTH move since
   9 Oct (17.7). The move since 30 Sep is +0.05%, so today ≈ **17.9**.
   - The World trigger P/Es become **15.5 / 14.8 / 17.1 / 14.0**, against 15.3 / 14.6 / 16.8 /
     13.8 in the report.
   - The US yield gap becomes 5.58 − 5.10 = **+0.5 pp** (report: +0.6).
   - Trigger levels in % and NOK are unaffected.
2. **Brent sensitivity of the Oslo trigger.** The report gives ±11% (1,448 / 1,796). That happens
   when the Bear path moves too, which leaves R unchanged. `osl.py` moves only Base and Bull and
   gives 1,558 / 1,683 (±4%). Say which one is meant, and make the script and the document agree.
   The Base IRR sensitivity (−0.9 / 5.3%) moves Base only.
3. **New Yahoo quirk.** Vår Energi `bookValue` is in USD while the price is in NOK, so Yahoo's
   P/B is 63.8 where it should be 6.8. Equinor, Aker BP, Subsea7, Frontline and Yara were
   converted correctly. Check P/B = price ÷ (BVPS × FX) for USD reporters.
4. **The skill master carries run history.** Fund mode, lines 340–360, records past results
   ("Base 4.8%…", "Nordnet 6.32% vs DNB 6.16%…"). Results belong in the fund documents. The skill
   should keep only the lessons.

## 5. Proposed changes

**Skill (`equity-market-bbb`):**

| # | Change | Effect |
|---|---|---|
| S1 | Step C: one retained-cash rule for both indices. Oslo energy c = 0.80 (as World energy), or a stated reason for c = payout | Oslo Base +0.5 pp (below the 1.0 pp minimum change, so note it, or adopt it with the method) |
| S2 | Payout per block for Oslo; the same energy payout in both indices | Small |
| S3 | Step C: require a **P/B–ROE table for both indices** (today trailing and forward, exit P/B = V_T / book_T, normalised ROE, history), with the basis stated. Payout check in both directions: state g ÷ retention as the implied return on retained earnings | Exit checks become visible (section 3.3) |
| S4 | Data discipline: label dividend yields (trailing / forward-annualised / cash yield). Report the bottom-up yield with and without names paying > 100% of EPS or with a yield > 2× the block's. Source buybacks or tag them `[A]` | Snapshot yield ~4.4–4.9% instead of "5.0%" |
| S5 | P/B history: name the index of each anchor, add a composition note (largest P/B contributors), and record the source's 2.4–2.7 loss zone. Recalibration band and signpost: P/B > 2.5 is a **valuation warning**, not Bull | Correct reading of P/B |
| S6 | Output template: World total value-multiple path; numeric World return split; like-for-like sensitivities (multiples ±10%, FX ±10% for both indices); mid-cycle inputs (payout, P/E, growth) per index | Fills C6–C9, C12 |
| S7 | World currency: USD share on USD/NOK, the rest on I-44 | Bear 2027 −0.8 pp |
| S8 | Trigger multiples: scale month-end multiples by the index move **since that month-end** | Fixes section 4, item 1 |
| S9 | Quirks: Vår `bookValue` in USD | — |
| S10 | Move fund-mode run history to the fund documents | Shorter skill |

**Report (`docs/equity-market-bbb.md`)**, at the next update or now as a correction:
- Fix the World P/E, the trigger P/Es and the yield gap (section 4, item 1).
- Clarify the Brent trigger sensitivity (section 4, item 2).
- Correct the P/B drift sentence.
- Add the exit P/B–ROE table, the World total P/E path, the FX sensitivity and the mid-cycle
  inputs.
- Update the HY upstream line.

**Stance:** unchanged. Oslo E / R stays negative with S1; World stays at ~0.025 against the HY
reference 0.196.

## Appendix: bottom-up data (Yahoo quoteSummary, close 16 Oct 2026) `[F]`

| Name | OBX wt % | P/B | P/E trailing | P/E fwd | ROE (Yahoo) | Fwd div. yield | Payout ratio, trailing (Yahoo) |
|---|---|---|---|---|---|---|---|
| Equinor | 16.1 | 2.59 | 12.0 | 10.2 | 21.3% | 3.36% | 40% |
| DNB | 10.4 | 1.74 | 11.1 | 10.9 | 15.1% | 5.87% | 65% |
| Kongsberg | 7.3 | **22.48** | 46.3 | 27.9 | 32.6% | 0.70% | 32% |
| Norsk Hydro | 6.7 | 1.46 | 15.5 | 9.2 | 9.4% | 3.90% | 60% |
| Aker BP | 6.2 | 2.14 | 16.9 | 12.9 | 12.1% | 6.91% | **113%** |
| Mowi | 5.1 | 2.43 | 14.9 | 13.9 | 15.5% | 3.69% | 48% |
| Storebrand | 4.9 | 2.50 | 16.7 | 14.1 | 15.2% | 2.83% | 48% |
| Telenor | 4.7 | 2.74 | 10.7 | 13.6 | 25.0% | 7.69% | 81% |
| Subsea7 | 4.3 | 2.43 | 16.6 | 13.3 | 14.2% | 5.80% | 94% |
| Yara | 4.2 | 1.23 | 7.0 | 8.8 | 17.9% | 5.34% | 37% |
| Orkla | 3.5 | 2.20 | 14.4 | 13.8 | 15.1% | 4.24% | 61% |
| Gjensidige | 2.5 | 6.15 | 20.6 | 15.2 | 27.2% | 3.79% | 78% |
| Frontline | 2.5 | 3.73 | 7.6 | 10.3 | 53.9% | **19.93%** | 47% |
| Vår Energi | 1.5 | 6.78 (Yahoo: 63.8) | 10.7 | 11.9 | 94.0% | 9.72% | 90% |

- Aggregates are harmonic: P/B = Σw ÷ Σ(w / P/B). ROE = earnings ÷ book. Yield is
  weight-averaged.
- Scripts: scratchpad `eqrev/fund.py`, `agg.py`, `chk.py`, `wchk.py`. They are not copied to
  `references/` because they are review checks, not part of a run.
- Sources: [MSCI Norway](https://www.msci.com/indexes/index/957800/msci-norway-index) and
  [MSCI World](https://www.msci.com/indexes/index/990100/msci-world-index) (30 Sep 2026); Yahoo
  quoteSummary and chart API (16 Oct 2026 close); [Nordnet blog, P/B on Oslo Børs](https://www.nordnet.no/blogg/hva-er-pris-bok-pa-oslo-bors-na-og-historisk)
  (4 Apr 2023).
