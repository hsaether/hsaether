# Odfjell Drilling (ODL) — IAF analysis, 4 Nov 2026 (v2) (stub Q4 2026 + 2027–2029)

> **4 Nov 2026, kept unchanged (change gate):** read Rig Market BBB small update of 4 Nov: the NCS HE semi row is unchanged (Barents signed at ~$450k; Norge 2028 $517k; medians at Base); only the UDW drillship 2027 point moved. No figure in this document changes.

**Version 2, 4 Nov 2026: update after the Q3 report (3 Nov) and Transocean's Q3 fleet status
(2 Nov).** Skill revisions used:
- **iaf-valuation 2026-11-01.1** (v1 used 2026-10-18.2; the new cycle-first rule for cyclical
  equities is applied in the Summary).
- **rig-market-bbb 2026-10-10.1** (the document was read; no rig forecast is made here).
- **oil-market-bbb 2026-10-24.4**: read only through Rig BBB's scenario mapping.
- **equity-market-bbb 2026-10-24.1** (exit cross-check and NOK path only).

Sector inputs:
- `docs/rig-market-bbb.md`: baseline 10 Oct 2026 (Final, stale after 9 Nov), with small updates on
  13, 17, 22, 24 and 28 Oct and paths unchanged. Uses the **HE semis (NCS) row**: leading edge,
  MCU, mid-cycle, the asset-value convention, the fixture log and the Bollsta transaction anchor.
  Rig BBB has not yet read the Q3 fleet status reports (its checkpoint 6). The Transocean
  read-across below is input for its re-run, not a change made here. No own rig forecast is made.
- `docs/oil-market-bbb.md`: 31 Oct 2026 (Final, stale after 7 Nov). Paths and mid-cycle are
  unchanged (Brent Base 88 / 77 / 72, mid-cycle 70), and it says "no change" for rigs. Background
  only, through Rig BBB's scenario mapping (Rig BBB last read the 24 Oct oil document).
- `docs/equity-market-bbb.md`: 17 Oct 2026, amended 18 Oct (stale after 10 Nov). Oslo exit P/E,
  exit P/B and mid-cycle return; USD/NOK path for the Bear/Bull NOK figures. Nothing else is taken
  from it.
- `docs/hy-market-bbb.md`: not used for a rate path. ODL's debt is a fixed 7.25% USD bond (due
  Mar 2031) plus SOFR bank facilities, with no maturity inside the horizon.
- **Stale after 4 Dec 2026** (30 days). A Rig BBB change to the HE semis row (re-run due by
  9 Nov) reaches this document through the register's input check. Also update on:
  - the Nordkapp 2028 rate (set by end-2026);
  - an exercise or lapse of the remaining Deepsea Atlantic priced options;
  - the Q4 report (date not announced; ~late Feb 2027 `[A]`).
- Oldest input: Q3 accounts (30 Sep 2026). Price: 3 Nov close.

## Summary

**Cycle first** (from Rig BBB, HE semis NCS row; no own rig forecast):
- **Where the cycle is: tight and firming.**
  - NCS HE cover is ~96% for 2027 and ~80% for 2028. Leading edge is $430–517k, and Westwood has
    Norway at $436k for 2026 YTD (+$50k y/y).
  - Odfjell says most marketable Tier-1 HE rigs are booked for 2027 and many into 2028, and it
    sees newbuilds as unlikely.
  - Transocean's fleet status of 2 Nov adds NCS prints for 2027–29 starts. Single rigs fix at
    $441–519k. Equinor's multi-year package is at $402k, i.e. at Base mid-cycle.
- **What can turn it:** demand, not supply. Supply is consent-gated and no newbuilds are coming.
  - The Bear catalyst is oil Bear: an Iran–USA deal plus an OPEC+ market-share fight (Brent
    65 / 60 / 60).
  - It works through FID deferrals and NCS programmes cut to minimum. The hit lands in 2028–29:
    MCU 88% → 83%, leading edge $400k → $380k.
- **How likely and when:** Bear is a stress test, not a probability. Its earliest date is Q1 2027
  (FIDs). ODL's 2027 is fully booked, so the scenarios part mainly from 2028.
- **What the price implies:** a through-life NCS HE rate of **~$413k** on Odfjell's own economics.
  - Base mid-cycle is $400k. A 12% return needs **~$425k**, about 6% above Base.
  - The price therefore assumes that today's tightness lasts beyond 2029.
  - The only HE transaction, the Bollsta purchase, implies ~$332k on the same economics.

**Verdict: fails.**
- **Base IRR ~8%** against k = 12%. The hurdle price is **$10.21 (NOK 94.9)** against
  **$11.23 (NOK 104.40)**: a margin of safety of **−9%**. v1 had −13% at an IRR of 6.3%.
- **Change since 26 Oct** (Base IRR +1.8 pp; P_k +$0.05):
  - **Method +0.4 pp** (P_k +$0.09). The rebuilt model replicates v1 at 6.4% (+0.1 pp). The cost
    calibration returns to the stated $231k a rig-day (v1 ran at ~$234k; Q3 confirms $229k):
    +0.3 pp. The skill revision 2026-11-01.1 changes presentation only.
  - **Report −0.3 pp** (P_k −$0.07). Net debt was $52m above the model at 30 Sep (−0.55 pp); the
    managed fleet and the raised dividend ($0.27) offset part of it.
  - **Price/FX +1.7 pp** (P_k +$0.03, from the later valuation date). The NOK price is −4.2%
    (104.40 vs 109.00; −4.6% on the report day): +1.7 pp. The firmer krone (9.2934 vs 9.31445):
    −0.1 pp. The valuation date (4 Nov): +0.1 pp.
- **Bear** (oil Bear; NCS MCU 83% by 2029; mid-cycle $350k): IRR ~−12%.
  - Capital is not preserved: $8.06 against $11.23, a ~28% permanent loss.
  - The balance sheet holds: net debt 1.1x EBITDA at exit and no maturity before Mar 2031.
- **Bull** (mid-cycle $460k; NCS leading edge $540k by 2029): IRR ~22%, hurdle $14.15 (NOK 131.5).
  The price reflects **26%** of the Base→Bull hurdle gap.
- **Price triggers (Oslo, NOK, at USD/NOK 9.2934):**
  - Base = k at **NOK 94.9** cum dividend. After the 12 Nov ex-date the $0.27 drops out:
    **~NOK 92.4**.
  - Bear preserves capital at **≤ NOK ~75** ($8.06). Bull's hurdle is NOK 131.5.
- **Why it still fails at Base:**
  - The cash yield is high (d 9.7%; $0.27 a quarter, raised).
  - But the fleet ages (−$283m), and the above-market firm contracts roll off (−$359m).
  - The price sits 1.07x Base NAV_0. Per-share value falls 2.4% a year while cash is paid out.
- **Robustness:** the verdict holds on every exit basis.
  - Rig BBB's convention marks give Base IRR ~−12%.
  - Exit marks re-discounted at Oslo's mid-cycle return give 6.1%.
  - The decision basis (Odfjell's realised margins) is the generous one.

**Decision table** (USD per share; P = $11.23 = NOK 104.40 at USD/NOK 9.2934)

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T | ~−12% | **~8%** | ~22% |
| V_T per share | $5.14 | **$10.42** | $15.78 |
| P_k (USD / NOK) / margin of safety | $6.13 / NOK 57.0 / −45% | **$10.21 / NOK 94.9 / −9%** | $14.15 / NOK 131.5 / +26% |
| Capital preserved? (ΣD_t + V_T vs P) | No: $8.06 (−28%) | **Yes: $13.88** | Yes: $19.50 |
| Cumulative Maintenance FCF per share, Q4-26 to 2029 | $4.72 | **$5.65** | $6.23 |
| Net debt per share at exit (31 Dec 2029) | $1.77 | **$1.39** | $1.06 |
| Balance sheet | ND/EBITDA 1.1x at exit; 2029 dividend cut to ~$0.45 | **ND/EBITDA 0.6x; bond balloon $564.5m in 2031, after exit** | ND/EBITDA 0.4x |
| E / R (HY rule; reference only, not the gate) | — | 0.69 in NOK (0.22 at spot FX) vs HY reference 0.196 | — |

The E / R row is a reference under the cycle-first rule; no switch rows against HY funds. It reads
high because 2027 is booked and the Bear loss lands in 2028–29, outside R (section 9).

**Per-share path** ($ per share; USD; Q3-26 is now reported, the stub is Q4-26)

| Base | Q4-26E | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| EBITDA, $m | 157 | 616 | 588 | 569 |
| EBITDA | 0.65 | 2.57 | 2.45 | 2.37 |
| Maintenance FCF | 0.61 (incl. $0.16 tax refund) | 1.88 | 1.67 | 1.49 |
| Debt amortisation | 0.05 | 0.37 | 0.37 | 0.37 |
| FCF after debt service | 0.56 | 1.51 | 1.30 | 1.12 |
| D_t paid | 0.27 (Q3 div., 25 Nov) | 1.13 | 1.17 | 0.89 |
| Net debt, period end | 3.24 | 2.48 | 1.99 | 1.39 |
| V_t (year end) | 10.35 | 10.24 | 10.17 | 10.42 |
| **Bear** Maintenance FCF / V_t | 0.61 / 10.35 | 1.88 / 8.52 | 1.44 / 6.72 | 0.79 / 5.14 |
| **Bull** Maintenance FCF / V_t | 0.61 / 10.35 | 1.88 / 11.86 | 1.80 / 13.61 | 1.94 / 15.78 |

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value or
reported figures · `[E]` external or secondary · `[A]` own assumption · `[?]` not found.

## 1. Header

| Item | Value |
|---|---|
| Company | Odfjell Drilling Ltd (Bermuda; UK tax resident; reports in USD), ticker **ODL** (Oslo Børs) |
| Price | **NOK 104.40**, close Tue 3 Nov 2026 (Yahoo `ODL.OL`, 15:29 UTC, 15-min delayed) `[F]`. −4.6% on the report day (prior close 109.40). 52-week range 76.2–112.0 |
| FX | USD/NOK **9.2934** (Yahoo `NOK=X`, 3 Nov, 15:15–15:30 UTC bar) `[F]` → **P = $11.23** (11.234) |
| Valuation date / exit / T | 4 Nov 2026 / 31 Dec 2029 / **3.16 years** (1,153 days) |
| Shares | **239,807,088** (Q3 note 13) `[F]`. 1,413,408 options outstanding (0.6%); July exercises were cash-settled, so basic shares are used `[A]`. No share issue or own-share purchase in 2026 (note 13; FinancialFilings `filings_list` since 15 Aug: no share issue, no insider trade) |
| Market cap / EV | $2,694m (NOK 25.0bn) / **$3,516m**: net interest-bearing debt ~$777m at the valuation date (30 Sep $857m less the $39m tax refund of 6 Oct and pro-rata Q4 cash flow `[A]`) plus leases $45m |
| NAV_0 (Base mid-cycle marks, Odfjell economics, incl. premium on firm-today contracts) | **$10.48 a share; P/NAV_0 1.07** (Bear $6.38 / 1.76; Bull $14.86 / 0.76) |
| NAV at market marks | **$6.51 a share; P/NAV 1.73**. Marks at the through-life rate implied by the only transaction, the Bollsta purchase ($480m incl. $355m backlog, Nov 2025): ~$332k on Odfjell economics |
| Track | **B**: rigs, capital-intensive, dayrate-driven cyclical |
| k | **12%**. Not raised: leverage is low (1.6x on the covenant definition at 30 Sep) and falling. Concentration (five rigs in one basin, three clients) is noted as a risk, not priced into k |
| Primary sources | Q3 2026 report and presentation (3 Nov; parsed in full, 30 + 19 pages), Q2 2026 report (balance sheet check), Newsweb (Nordic Financial `search_filings`, 2026), Transocean 8-K of 2 Nov (results and fleet status, SEC EDGAR), Rig BBB fixture log |

## 2. Scenarios (from Rig Market BBB, 10 Oct; HE semis (NCS) row; unchanged)

| Scenario | Catalyst (Rig BBB) | NCS HE leading edge 2027 / 28 / 29, $k | MCU 2027 / 28 / 29 | Mid-cycle rate / MCU |
|---|---|---|---|---|
| **Bear** | Oil Bear (Iran–USA deal plus an OPEC+ market-share fight; Brent 65 / 60 / 60), FID deferrals; NCS programmes cut to minimum | 410 / 400 / 380 | 92 / 88 / 83% | $350k / 85% |
| **Base** | Armed normalisation (Brent 88 / 77 / 72); NOC-led floater demand; NCS booked through 2027 and largely 2028 | 425 / 450 / 470 | 97 / 96 / 93% | **$400k / 92%** |
| **Bull** | 2H26 FIDs and NOC programmes lock long terms; no reactivations before 2028 | 445 / 500 / 540 | 98 / 98 / 97% | $460k / 96% |

The stub (Q4-26) is identical in all scenarios; Bear and Bull diverge from 1 Jan 2027. ODL's 2027 is
~100% firm, so the scenarios differ mainly from 2028.

## 3. Company and status

- **Business.** Own Fleet: five 6G harsh-environment semis on the NCS/UKCS (Q3 own-fleet revenue
  $235m, EBITDA $127m incl. +$11m other income). External Fleet: management of Deepsea Yantai,
  Deepsea Mira, Hercules and, from 2 Nov, Beacon Pacific (Q3 EBITDA $6m). Corporate: −$3.2m in Q3.
- **Owner.** Helene Odfjell controls Odfjell Partners Holding with **49.85%** `[F]`.
- **Q3 2026** `[F]`:
  - Revenue $265m, EBITDA $130m (incl. +$10.7m other income, mainly insurance), net profit $56m
    (incl. $4.7m interest on the tax refund, shown as discontinued operations).
  - FU 89%: Deepsea Atlantic 55.8%, the other four 97% (Aberdeen 94.5% and Bergen 94.0% after a
    labour dispute at a third-party supplier). FU was 98% in September.
  - Net debt **$857m** (gross $901.9m, cash $45.2m), liquidity $261m (RCF $216m undrawn).
    Leverage 1.6x on the covenant definition; equity ratio 56%; covenants met.
  - Firm backlog **$2.5bn** (Q2: $2.1bn), after the Vår Energi contract and the Nordkapp extension.
- **Deepsea Atlantic incident** (18 Apr): the BOP and 400 m of riser were dropped at 1,100 m.
  - **Off-hire:** 106 days in total (73 in Q2, 33 in Q3); back on rate 2 Aug, with minor restart
    issues resolved by mid-August.
  - **Insurance:** $93.7m recognised; $50m paid on account in Q3; **$43.7m receivable** still to
    come. The excess claim is a contingent asset `[F]`.
  - The company says the incident's total net cash impact is fully in the Q3 liquidity. Remaining
    capex payments are expected to be offset by the remaining insurance proceeds, so it is modelled
    as **net zero from Q4** `[F/A]`.
- **Tax case:** **$39m received on 6 Oct** (NOK 352m = NOK 307m repayment plus NOK 45m interest)
  `[F]`.
- **Debt.**
  - Bonds: $650m 7.25% senior secured (ODRG02), issued Dec 2025, due **Mar 2031** `[F]`. The
    coupon is paid in March and September: Q3 cash interest was $29.2m, against ~$17m accrued.
  - Banks: $550m of facilities ($300m RCF) at SOFR + ~288 bp average margin `[F]`.
  - Contractual debt $909.5m at 30 Sep. Repayments: Q4-26 $10.8m, then $33.3 / 10.8 / 33.3 / 10.8m
    a quarter ($88.3m a year), $80.0m in the fourth year and **$564.5m in the fifth (2031)** `[F]`.
- **Dividend:** raised to **$0.27** for Q3 ($64.7m; the sixth rise since Q4 2024, from $0.125)
  `[F]`.
  - Ex-date 12 Nov, payment 25 Nov 2026. It is after the valuation date, so it counts as D_t.
  - Criteria: leverage, cash position, covenants, 12-month cash forecast, backlog, market position.
- **Managed fleet (new):**
  - Beacon Pacific (6G semi, owner Beacon Pacific Offshore Ltd): management agreement, 2 Nov. The
    rig is being reactivated for Serica (UK, six firm wells, Q3 2027 to Q4 2028, options after).
  - Deepsea Yantai: two Okea wells (~80 days), firm to Q4 2027.
  - Deepsea Mira: Shell Trinidad from Apr 2027.
  - Hercules: Suncor (Canada) from Q1 2027.
  - Fees are not disclosed `[?]`.
- **Next report:** Q4 2026, date not announced (Q4 2025 was 25 Feb 2026) `[?]`.

### Fleet and firm cover (as of 4 Nov 2026; unchanged from v1)

| Rig (built) | Client / contract | Firm to | Basis rate used, $k/day | Source / tag |
|---|---|---|---|---|
| **Deepsea Atlantic** (2009, DP, UK/NCS) | Equinor/Adura. The Jan 2025 extension (mid-Q3 2026 → end Q2 2027, $148m) plus 2 priced wells exercised 16 Oct | **late Q4 2027** (15 Dec assumed). Then 2 priced wells and unpriced options extending beyond 2030 | 478 (2026) / 492 (2027). The $148m ÷ ~319 days gives ~$464k `[B]`, escalated `[A]` | Newsweb 16 Oct; Q3 report |
| **Deepsea Stavanger** (2010) | Aker BP, 5-year firm from early 2025. Base value $620–730m; rate set annually by two brokers within a collar (floor/ceiling $340/400k, ceiling inflation-adjusted from Jun 2023) | **~Q1 2030** | 437 (2026), 435 (2027). 2028–29 = clamp(market, floor, ceiling) with index 3% a year: Bear 400 / 406, Base 450 / 470, Bull 464 / 478 | Newsweb 24 Aug 2022 `[F]`; index `[A]` |
| **Deepsea Aberdeen** (2014) | Equinor: new contract (interim, then Fram Sør) from Q4 2026, **$373m** | **Q1 2029** (15 Feb assumed) | 470 to Oct 2026 `[A]`; 446 from 1 Nov 2026 ($373m ÷ ~837 days `[B]`), escalated 3% a year | Newsweb 19 Dec 2025 |
| **Deepsea Nordkapp** (2019) | Aker BP (semi-alliance); one-year extensions | **end 2028**, then unpriced Aker BP options | 460 (2026) / 440 (2027) `[A]`. 2028: rate set by end-2026 at market by two brokers, so **450 in all scenarios** `[A]`. SPS late 2028, ~20 days and $35m `[A]` | Newsweb 17 Jul 2026; Q3 presentation |
| **Deepsea Bergen** (ex-Bollsta, 2019) | Equinor (Johan Sverdrup Ph. III) to early 2028, then **Vår Energi, 3 years**, plus four 1-year priced options to early 2035 | **Q1 2031** | Equinor 465, escalated; Vår ~$473k from Apr 2028 ($518m incl. mobilisation `[B]`), escalated from 2029 | Newsweb 10 Sep 2026; Q3 report |

- **Firm backlog** `[F]`: $2.5bn at Q3, excluding Atlantic's 2 wells exercised after the period.
- **Model cross-check:** the model's firm days at basis rates (incl. 3% escalation, Atlantic to
  end-Q2 2027) sum to ~$2.25bn. That is ~10% below the reported figure; the gap is unexplained
  `[?]`.
  - The 2027 slice reconciles: the model has $752m against the company's $754m (Q4-25 backlog by
    year).
  - The gap therefore sits in 2028+. Candidates are the Stavanger collar, the company's estimate
    for Nordkapp 2028 and the Vår mobilisation fee.
  - It matters for U. If the basis rates were higher, U would be lower, and so would the exit
    marks (section 9).
- **Open rig-days in the window:**
  - Atlantic from mid-Dec 2027;
  - Nordkapp from 2029;
  - Aberdeen from mid-Feb 2029.
  - That is ~25% of 2029 rig-days and ~20% of 2028 (Atlantic only).
  - Stavanger is firm, but its rate resets inside the collar every year.

## 4. Near term: Q3 actual and the Q4 stub (all scenarios)

| | Q3-26 actual | Q4-26E |
|---|---|---|
| Booked share of own-fleet days | 100% (Atlantic off hire 1 Jul–2 Aug) | 100% |
| Own-fleet FU | 89% (Atlantic 55.8%; others 97%) `[F]` | 97% (10-year average; September 98%) |
| Average basis dayrate, own fleet | ~$461k (model) | ~$459k (Aberdeen re-priced to 446 from 1 Nov) |
| Rig-days on hire | 408 | 446 |
| Revenue / EBITDA, $m | 265.4 / 130.3 (incl. +10.7 other income) `[F]` | 290 / 157 |
| Maintenance FCF, $m (per share) | ~52 ($0.22) `[B]`: CFO 94.3 − capex 39.1 + other investments 0.9 − lease principal 3.7 | 146 ($0.61), incl. +39 tax refund; incident cash net 0 |
| Dividend declared, per share | **$0.27** (ex 12 Nov, paid 25 Nov) `[F]` | $0.27 (paid ~19 Mar 2027 `[A]`) |
| Consensus | — | Yahoo FY2026 EPS $1.21 (n `[?]`) `[E]`. It implies Q4 ~$0.43 against 9M actual $0.78 and model Q4 ~$0.32; inconsistent with the run-rate, unverified |

- **Net debt bridge:**
  - 30 Sep **$857m** `[F]`.
  - Less the tax refund $39m (6 Oct) and pro-rata Q4 cash flow → **~$777m at 4 Nov** `[A]`.
  - Less the rest of Q4 Maintenance FCF (total $146m incl. the refund), plus the Q3 dividend
    $64.7m (25 Nov) → **$776m at 31 Dec 2026**.
- **Interest timing.** The model accrues interest (7.6% on net debt + $60m minimum cash). The bond
  coupon falls in March and September, so cash net debt at 31 Dec should be ~$12m lower than the
  model; the difference reverses in Q1 2027.
- **Unmodelled upside:** trade receivables rose $33m in Q3 (113 → 146) as the fleet came back on
  full hire. A return to the ~45-day norm would release ~$13m `[A]`.
- Amortisation ($10.8m in Q4) moves gross debt and cash equally and does not change net debt.
- **Calibration (Q3):**
  - Own-fleet EBITDA excluding incident items: ~$129m. The incident items net −$2m: +$11.1m
    insurance and ~$13m claim costs in opex (derived from YTD $64m less the Q2 $50.5m) `[B]`.
  - That gives a cash cost of **$229k a calendar rig-day** (Q1: $231k) `[B]`.
  - Revenue ÷ basis revenue at actual FU by rig = **U 1.25** (Q1 fleet 1.29; Q2 Bergen 1.25)
    `[B]`. Aberdeen had a lower bonus in Q3 `[F]`.
  - Revenue per on-hire day was ~$575k. Transocean's HE fleet earned $504k per operating day in Q3
    at 97.7% revenue efficiency `[F]`.

## 5. Market input and assumptions

**Rig BBB rows used (HE semis, NCS; unchanged since v1):**
- Open days earn the leading edge of their calendar year × the scenario's MCU. Idle days cost
  40% of the cash cost.
- Mid-cycle and MCU feed the exit marks.
- Nordkapp's 2028 rate is set in the stub at Base 2028 ($450k).
- Stavanger's 2028–29 rate is the scenario's market rate inside the contract collar.

**Transocean Q3 and fleet status, 2 Nov (read-across; SEC 8-K ex. 99.1 and 99.2)** `[F]`:

| Rig (built) | Client | Term | Dayrate $k | Reading for ODL |
|---|---|---|---|---|
| Transocean Barents (2009) | Vår Energi | Jun 2027–Jun 2030, firm; priced options to Jun 2034 | **470** | Same vintage as Deepsea Atlantic. A 3-year NCS term at the Base 2029 rate, above the $450k used for Atlantic's 2028 re-pricing |
| Transocean Norge (2019) | Harbour | Jan–Oct 2028 | **517** | Resolves Rig BBB checkpoint 9 at $517k (not $497k) |
| Transocean Norge | A/S Norske Shell | Mar–Jul 2029, firm; option to Aug 2029 | **517** | First firm 2029-start NCS print; above Base 2029 ($470k) |
| Transocean Spitsbergen (2010) | Equinor | Apr–Dec 2027 | **519** | 2027 print above Base 2027 ($425k); ODL's 2027 is already booked |
| Transocean Enabler / Encourage | Equinor | Dec 2026–Apr 2028 / May 2027–May 2028 | 480 / 441 | Bridging terms |
| Enabler / Encourage / Endurance | Equinor | 2027–2031 multi-year package | **402** | Long-term package rate ≈ Base mid-cycle ($400k) |

- **Transocean fleet data:**
  - HE fleet in Q3: average daily revenue $504k, revenue efficiency 97.7%, utilisation 95.1%.
  - HE estimated average contract dayrates: Q4-26 $478k, Q3-27 $465k.
  - Fleet-wide 2027 coverage ~95%. Valaris closing is expected on 1 Dec 2026, with all approvals in
    hand.
- **Reading:**
  - NCS prints for 2027–29 starts run from $402k (Equinor's multi-year package) to $517–519k
    (single rigs, shorter terms).
  - The 3-year 2009-vintage term at $470k sits at Rig BBB Base 2029. It supports the Base path
    ($450k / $470k) and the Nordkapp 2028 assumption ($450k).
  - It says nothing new about mid-cycle, which drives the verdict. The $402k package for 2028–31 is
    the closest long-term print, and it sits at Base mid-cycle.
  - No change is made here; the fixtures go to Rig BBB (For other modules).

**Company economics (decision basis; departs from Rig BBB's convention, sourced):**

| Parameter | ODL value | Rig BBB convention | Source |
|---|---|---|---|
| Revenue per working day | basis dayrate × FU 97% × **U 1.27** | rate × RE 96% | U: Q1-26 fleet 1.29, Q3-26 fleet 1.25 (mean 1.27), Q2-26 Bergen 1.25 `[B]`. Bonuses, fuel incentives, escalation, integrated services and FX on NOK-denominated rate parts, all excluded from the disclosed dayrates and backlog. FU = 10-year average `[F]` |
| Cash cost per rig-day | **$231k** (2026), +3% a year; $250k in the marks | $250k | (Revenue − EBITDA) ÷ calendar rig-days, own fleet: Q1-26 $231k, Q3-26 $229k ex incident items `[B]`. v1's tables ran at ~$234k (the $231k escalated half a year); corrected |
| Cash tax | **3% of revenue** | 5% | FY2025 tax $24m ÷ revenue $901m = 2.7% `[B]` |
| Maintenance capex | **$12m/rig/yr** in marks; window: Q4-26 $20m `[A]` (YTD ex-incident run-rate ~$19m a quarter), then $14m a quarter, +3% a year from 2028, plus SPS (Nordkapp Q4-28 $35m; Atlantic Q2-29 $35m; Bergen Q3-29 $30m `[A]`) | $6m | 9M-26 PPE purchases $74m incl. ~$18m Atlantic incident in Q3; commitments $40.5m at 30 Sep `[F]` |
| Idle cost / life / asset rate | 40% / 30 years / 8% | same | Rig BBB |

- **Why depart from the convention.**
  - At a $450k basis rate ODL earns ~$320k a working day; the convention earns $182k.
  - The Bollsta EBITDA (~$100m a year at ~$450k, company guidance `[F]`) and the Q1 and Q3
    margins show this is realised, not projected.
  - The skill allows company opex "where sourced in the company analysis".
- **The asset market does not capitalise these margins at 8%:**
  - On ODL economics, Bollsta at Base mid-cycle would have been worth **$709m**, against the
    **$480m** ODL paid.
  - The Bollsta price implies ~$332k on ODL economics and ~$448k on the convention.
  - The decision basis is therefore the favourable one; both alternatives are shown as
    sensitivities (section 9).
- **Interest:** 7.6% on net debt plus a $60m minimum cash balance; 2% on cash; accrual basis
  `[B]`. Q3 other interest was $17.1m on ~$905m gross debt (7.6%). Leases $4.3m a quarter `[F]`.
- **External fleet:** EBITDA $6m in Q4-26 (Q3: $6.1m), $6.5m a quarter in H1-27 (Hercules, Mira)
  and $7m from Q3-27 (Beacon Pacific) `[A]`. Valued at 3x the exit run-rate ($84m) in NAV and V_T
  `[A]`.
- **Holdco G&A:** corporate −$12m a year (9M-26: −$9.6m excluding a $2.0m sublease gain `[B]`;
  v1 had −$9m). It is in the cash flows and **not deducted in NAV**. Onshore operations are in the
  rig cash cost.
- **Dividends** `[A]`:
  - $0.27 for Q4 2026 (the new level).
  - From Q1 2027: 75% of the quarter's FCF after debt service, with a **$0.27 floor** while that
    FCF covers it, and the full FCF after debt service below the floor.
  - Paid on 1 Jun / 17 Sep / 25 Nov / 19 Mar.
  - Retained cash reduces net debt and reaches V_T. A 100% payout changes Base IRR by < 0.1 pp.
  - Q4-29's dividend is paid in Mar 2030, after exit, so it sits in V_T as lower net debt.

## 6. Period tables ($m and per share; USD)

### Base (decision case)

| | Q4-26E | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|
| Rig-days on hire | 446 | 437 | 441 | 446 | 446 | 1770 | 1741 | 1666 |
| Revenue, $m | 290 | 286 | 288 | 291 | 290 | 1155 | 1138 | 1123 |
| EBITDA, $m | 157 | 152 | 154 | 156 | 154 | 616 | 588 | 569 |
| EBITDA, $/sh | 0.65 | 0.63 | 0.64 | 0.65 | 0.64 | 2.57 | 2.45 | 2.37 |
| Net interest (accrual), $m | 17 | 16 | 15 | 14 | 13 | 57 | 44 | 36 |
| Cash tax, $m | 9 | 9 | 9 | 9 | 9 | 35 | 34 | 34 |
| Leases, $m | 4 | 4 | 4 | 4 | 4 | 17 | 17 | 17 |
| Capex (maintenance + SPS), $m | 20 | 14 | 14 | 14 | 14 | 56 | 93 | 124 |
| Other cash (tax refund), $m | 39 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Maintenance FCF, $m** | 146 | 110 | 112 | 115 | 114 | 451 | 400 | 358 |
| **Maintenance FCF, $/sh** | 0.61 | 0.46 | 0.47 | 0.48 | 0.48 | 1.88 | 1.67 | 1.49 |
| Debt amortisation, $m | 11 | 33 | 11 | 33 | 11 | 88 | 88 | 88 |
| **FCF after debt service, $m** | 135 | 76 | 101 | 82 | 103 | 363 | 312 | 270 |
| **FCF after debt service, $/sh** | 0.56 | 0.32 | 0.42 | 0.34 | 0.43 | 1.51 | 1.30 | 1.12 |
| Dividend declared (period earned), $/sh | 0.270 | 0.270 | 0.316 | 0.270 | 0.324 | 1.180 | 1.083 | 0.971 |
| Dividends paid in period, $m | 65 | 65 | 65 | 76 | 65 | 270 | 281 | 213 |
| Growth capex | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Net debt, period end, $m** | 776 | 731 | 684 | 645 | 595 | 595 | 477 | 332 |
| **Net debt, $/sh** | 3.24 | 3.05 | 2.85 | 2.69 | 2.48 | 2.48 | 1.99 | 1.39 |

- **2028–29 EBITDA falls although market rates rise**, for three reasons:
  - costs inflate 3% a year;
  - Atlantic re-prices from $492k to a Base $450k (2028) and $470k at 93% MCU (2029);
  - SPS off-hire in 2028–29.
- The dividend oscillates ($0.27 / $0.32) because amortisation is paid unevenly by quarter. In the
  SPS quarters (Q4-28, Q2–Q3-29) FCF after debt service falls below the floor, and the dividend
  drops to $0.16–0.23.

### Bear and Bull (lines not shown follow the Base mechanics; 2027 is almost fully booked, so Bear and Bull equal Base until 2028)

| | Bear 2027 | Bear 2028 | Bear 2029 | Bull 2027 | Bull 2028 | Bull 2029 |
|---|---|---|---|---|---|---|
| Revenue, $m | 1154 | 1080 | 940 | 1156 | 1171 | 1237 |
| EBITDA, $m | 615 | 534 | 402 | 616 | 619 | 677 |
| Maintenance FCF, $m ($/sh) | 450 (1.88) | 346 (1.44) | 190 (0.79) | 451 (1.88) | 431 (1.80) | 465 (1.94) |
| FCF after debt service, $m ($/sh) | 362 (1.51) | 258 (1.07) | 102 (0.43) | 363 (1.51) | 343 (1.43) | 377 (1.57) |
| Dividend declared, $/sh | 1.178 | 0.987 | 0.448 | 1.181 | 1.141 | 1.258 |
| Net debt, year end, $m ($/sh) | 596 (2.48) | 521 (2.17) | 425 (1.77) | 595 (2.48) | 451 (1.88) | 254 (1.06) |

### Year-end path ($ per share; P = $11.23 at 4 Nov)

| | Stub (to 31 Dec 2026) | 2027 | 2028 | 2029 (exit) |
|---|---|---|---|---|
| **Base** D_t paid / V_t / r_t / IRR to t | 0.27 / 10.35 / −5.5% (not annualised) / — | 1.13 / 10.24 / +9.8% / 3.3% | 1.17 / 10.17 / +10.8% / 6.7% | 0.89 / 10.42 / +11.1% / **8.1%** |
| Bear | 0.27 / 10.35 / −5.5% / — | 1.13 / 8.52 / −6.8% / −10.9% | 1.13 / 6.72 / −7.8% / −9.8% | 0.39 / 5.14 / −17.8% / **−12.3%** |
| Bull | 0.27 / 10.35 / −5.5% / — | 1.13 / 11.86 / +25.5% / 16.3% | 1.20 / 13.61 / +24.9% / 20.5% | 1.12 / 15.78 / +24.2% / **21.8%** |

- **Interim V_t marks** glide linearly from the Base mid-cycle marks at the end of the stub
  (identical in all scenarios, firm-today premium only) to each scenario's exit marks. The 2027 and
  2028 marks include the scenario's signed backlog on rigs that re-price within six months.
- **The stub loss (−5.5%) is the price-to-NAV gap.** Once the price is marked to NAV, Base earns
  ~10–11% a year, still below k.

## 7. Exit value V_T (Rig BBB asset-value formula, ODL parameters)

**Exit asset table** ($m; mid-cycle rate / MCU; ages at 31 Dec 2029; convention values in
brackets; rig rows unchanged from v1)

| Rig (age at exit) | Bear (350 / 85%) | **Base (400 / 92%)** | Bull (460 / 96%) |
|---|---|---|---|
| Atlantic (20.5) | 225 (65) | **400** (192) | 593 (337) |
| Stavanger (19.5) | 241 (69) | **427** (205) | 634 (360) |
| Aberdeen (15.5) | 292 (84) | **518** (249) | 769 (437) |
| Nordkapp (10.7) | 336 (97) | **596** (287) | 885 (502) |
| Bergen (10.7) | 336 (97) | **596** (287) | 885 (502) |
| **Fleet** | 1,429 | **2,537** (1,220) | 3,768 |
| Firm-today backlog premium (Bergen/Vår to Q1 2031, Stavanger to ~Feb 2030) | +103 | **+71** | +33 |
| Scenario-signed backlog premium (Atlantic, Aberdeen and Nordkapp on rolling ~1-year terms: 0.5 year average at the 2029 rate, capped well inside 2 years) | +41 | **+59** | +60 |
| Reversion tail (exit consistency) | 0 (gap < 10%) | **+80** | +96 |
| Management business (3x exit EBITDA) `[A]` | +84 | **+84** | +84 |
| Net debt at exit (leases fully repaid) | −425 | **−332** | −254 |
| **Equity value / per share** | 1,232 / **$5.14** | **2,498 / $10.42** | 3,785 / **$15.78** |

Per contracted day vs the average mid-cycle day: Base $312k vs $202k (Bear $204k vs $128k; Bull
$395k vs $284k), both after cash tax.

**V_T bridge, Base** ($m; per share in brackets). The re-rating P → NAV_0 sits above it: P $11.23
→ NAV_0 $10.48, i.e. −2.2% a year assumed at exit.

| Step | $m | $/sh |
|---|---|---|
| NAV_0 at Base mid-cycle marks (fleet $2,820m + firm premium $430m + management $84m − net debt $777m − leases $45m) | 2,512 | 10.48 |
| + value created by growth capex | 0 | 0 |
| − ageing of the fleet at Base mid-cycle marks (2,820 → 2,537) | −283 | −1.18 |
| − roll-off of the firm-today premium (430 → 71) | −359 | −1.50 |
| + premium on backlog signed in the scenario | +59 | +0.25 |
| + reversion tail | +80 | +0.33 |
| + retained cash (Σ Maintenance FCF − D_t paid; net debt and leases 822 → 332) | +490 | +2.04 |
| **= V_T** | **2,498** | **10.42** |

NAV_0 counts the Nordkapp 2028 extension at no premium, because its rate is not yet set (as in v1).

**Exit consistency** (HE semis row; open days after exit only; unchanged)

| Scenario | Year-3 rate | Mid-cycle | Gap | Open days in the 2 years after exit | Treatment | Tail $m ($/sh) |
|---|---|---|---|---|---|---|
| Bear | 380 | 350 | +8.6% | — | Not material | 0 |
| **Base** | 470 | 400 | **+17.5%** | 3 open rigs (half of year 1 under scenario-signed backlog), Stavanger after Feb 2030, Bergen after Mar 2031 | **Reversion tail.** Rig BBB names no reason for a return to mid-cycle within a year of exit. The asset market prices above mid-cycle on the convention (Bollsta ~$448k, Rig BBB anchors) | **+80 (0.33)** |
| Bull | 540 | 460 | +17.4% | as Base | Reversion tail | +96 (0.40) |

- Without the tail: Base IRR 7.1%, P_k $9.98; Bull 20.9% / $13.87.
- Without the scenario-signed premium (firm-today contracts only): Base 7.4% / $10.04; Bear
  −13.0% / $6.01; Bull 21.2% / $13.98.

**Exit cross-check against the equity market** (Oslo; Equity BBB 17/18 Oct)

| | Bear | **Base** | Bull |
|---|---|---|---|
| FCF_normalised, after the fleet-renewal charge and before holdco G&A ($12m a year), $m ($/sh) | 98 (0.41) | **201 (0.84)** | 312 (1.30) |
| Exit P/E (V_T ÷ FCF_norm) | 12.6 | **12.5** | 12.1 |
| Book equity at exit, $m / exit P/B | 1,476 / 0.83 | **1,569 / 1.59** | 1,647 / 2.30 |
| Buyer's implied return (asset rate 8%, adjusted for net debt) | 8.1% | **8.1%** | 8.0% |
| Oslo index: exit P/E / exit P/B / mid-cycle return | 10.5 / 1.48 / 8.2% | **11.5 / 1.75 / 9.1%** | 12.5 / 1.97 / 9.4% |
| IRR_T / P_k with exit marks re-discounted at the Oslo return | −12.6% / $6.07 | **6.1% / $9.74** | 19.0% / $13.27 |

- **The exit P/E is close to the index** (Base 12.5 vs 11.5). The buyer's return is ~1 pp below
  Oslo's, with no stated quality reason, so the re-discounted figures above are the sensitivity.
- **Bull's exit P/B (2.30) is above the Oslo band (1.5–2.1).** The rigs are carried at
  depreciated 2009–2019 cost while Bull marks them at a $460k mid-cycle.

## 8. Growth capex test

- **None in the horizon.** No newbuild, acquisition or reactivation of an owned rig is announced,
  and none is modelled.
- **Beacon Pacific** is a management agreement on a third-party rig: no ODL capital.
- **The Bollsta acquisition** (Dec 2025, $480m, fully debt-financed) is sunk and sits in NAV_0.
- **Ex-post it is accretive:**
  - ~$100m EBITDA a year at ~$450k (company `[F]`; Q3 Bergen at 94% FU) gives ~$85m of rig-level
    cash after tax and capex, ~18% on the price.
  - On Base mid-cycle marks with ODL economics, Bergen is worth ~$634m plus its Vår premium today,
    against $480m paid. ROIC_g > k.
- **A future fleet addition must be tested against** Rig BBB's HE newbuild/reactivation parity
  (both `[?]` in Rig BBB) and the contract rate secured.

## 9. Full results and sensitivity

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (dated, to the exit value) | −12.3% | **8.1%** | 21.8% |
| IRR_T in NOK on the Equity BBB NOK path (USD/NOK Bear +12% / +9% / +9%; Bull −3%) | −9.2% | 8.1% (spot flat) | 20.4% |
| d / g / c | 8.2% / −21.9% / +1.5 pp | **9.7% / −2.4% / +0.7 pp** | 10.5% / +11.4% / −0.1 pp |
| g: re-rating / NAV growth (P/NAV_0) | −16.4% / −6.6% (1.76) | **−2.2% / −0.2% (1.07)** | +9.3% / +1.9% (0.76) |
| Structural IRR / cyclical (pp; Δd, Δg) | −14.4% / +2.1 (+0.8, +1.1) | **4.3% / +3.8 (+1.2, +2.6)** | 19.3% / +2.5 (+0.6, +2.1) |
| ΣD_t / V_T | $2.92 / $5.14 | **$3.46 / $10.42** | $3.71 / $15.78 |
| P_k / margin of safety | $6.13 / −45.5% | **$10.21 / −9.1%** | $14.15 / +26.0% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | 27.4x vs n/a (IRR < 0) | **13.4x vs 5.6x** | 8.6x vs 15.1x |
| Capital preserved? ΣD_t + V_T vs P | **No**: $8.06 (−28%) | Yes: $13.88 | Yes: $19.50 |

- **Structural and cyclical runs:**
  - From 1 Jan 2027 every open or re-priced day is at the scenario's own mid-cycle rate. That
    covers Atlantic after Dec 2027, Nordkapp's 2028 rate, the Stavanger collar from 2028, and
    Aberdeen and Nordkapp in 2029.
  - The tail is zero, and scenario-signed backlog is re-priced at mid-cycle.
- **Reading:**
  - Base is mostly structural: 4.3% even at a flat $400k. The 2027–29 rate path above mid-cycle
    adds 3.8 pp.
  - **Bear and Bull are mainly mid-cycle shifts:**
    - the structural IRR moves −18.7 pp (Bear) and +15.0 pp (Bull) against Base;
    - the rate path around each scenario's own mid-cycle adds only +2.1 / +2.5 pp.
  - The price is therefore a bet on the NCS HE mid-cycle, not on the next three years, which are
    already booked.
- **FCF_normalised (Base):**
  - Five rigs at Base mid-cycle give $61.6m each of rig-level cash after idle time, tax and
    capex, so $308m; plus management $28m.
  - Less interest on the exit net debt ($29m), leases ($17m) and the fleet-renewal charge (ageing
    $283m ÷ T = $90m) → **$201m**, $0.84 a share.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** IRR 7.9%, P_k $10.18.
- **Share of Bull already priced:** (11.23 − 10.21) ÷ (14.15 − 10.21) = **26%** (v1: 39%).
- **E / R (HY rule, NOK; reference only under the cycle-first rule, not the gate):**
  - E = Base IRR 8.1% − Base window NIBOR 4.38% = 3.7 pp.
  - R = Base 2027 (+9.8%) − Bear 2027 in NOK (+4.4%: −6.8% in USD, with USD/NOK +12% on the Equity
    BBB path) = 5.4 pp. E / R = **0.69** (0.22 at spot FX, R 16.6 pp). HY market reference: 0.196.
  - It overstates ODL: 2027 is booked, so the Bear loss (window IRR −12%) lands in 2028–29,
    outside R. No switch rows against HY funds.
- **Bear balance-sheet survival:**
  - EBITDA falls to $402m in 2029. Net debt falls to $425m (1.1x).
  - The dividend drops to ~$0.45 for 2029. Amortisation ($88m a year) is covered.
  - Bear HY refinancing is not needed: the bond matures Mar 2031 and the exit net debt is well
    below the bond.
  - Survival is not in question; the Bear loss is valuation, not solvency.

**Sensitivities (Base unless stated)**

| Change | IRR_T | P_k | Margin |
|---|---|---|---|
| Decision | 8.1% | $10.21 | −9.1% |
| Revenue uplift U 1.20 / 1.25 / 1.35 (vs 1.27; window and marks) | 0.9% / 6.1% / 15.3% | $8.52 / $9.73 / $12.15 | −24% / −13% / +8% |
| Cash cost +10% / −10% (window only) | 6.2% / 9.9% | $9.73 / $10.69 | −13% / −5% |
| Cash cost +10% / −10% (window and marks opex) | 1.6% / 13.8% | $8.69 / $11.74 | −23% / +4% |
| v1 cost level ($234k) and Q3's U 1.25 | 5.8% | $9.66 | −14% |
| Base mid-cycle $350k / $375k / $425k / $450k | −1.1% / 3.7% / 12.1% / 15.5% | $8.13 / $9.17 / $11.25 / $12.22 | −28% / −18% / 0% / +9% |
| **Rig BBB convention marks** (opex 250, RE 96%, no uplift, tax 5%, capex $6m) | **−11.9%** (V_T $4.70) | $6.22 | −45% |
| Convention marks, Bear / Bull | −43.8% / 4.1% | $3.04 / $9.27 | — |
| Exit marks at Oslo's mid-cycle return (9.1%) | 6.1% | $9.74 | −13% |
| No reversion tail | 7.1% | $9.98 | −11% |
| Firm-today backlog only | 7.4% | $10.04 | −11% |
| Payout 100% of FCF after debt service | 8.1% | $10.24 | −9% |
| **Break-even Base mid-cycle for 12%** | ODL economics **~$425k**; convention ~$558k | | |
| **Price-implied through-life rate** (NAV_0 = P, MCU 92%) | ODL economics ~$413k; convention ~$565k | | |
| Bollsta-implied through-life rate (transaction, Nov 2025) | ODL economics ~$332k; convention ~$448k | | |

- **The one input that could flip Base is U**, the bonus/incentive uplift. U ≥ ~1.31 clears.
  - Observed: Q3 fleet 1.25, Q2 Bergen 1.25, Q1 fleet 1.29. Part of it is FX on NOK-denominated
    rate components at today's strong krone.
  - A U above 1.30 is not evidenced. The Q3 reading (1.25) and the backlog gap (section 3) both
    point the other way.

## 10. Verdict and caveat

- **Fails.** The Base margin of safety is **−9.1%** (P_k $10.21 / NOK 94.9 vs P $11.23 / NOK
  104.40; below the −2% threshold). v1: −13.2%.
- **It does not survive Bear:** IRR −12.3% and a ~28% permanent loss, though the balance sheet is
  never at risk.
- **What would flip the verdict:**
  - a through-life NCS HE rate of ~$425k (Base mid-cycle $400k; Rig BBB Bull $460k);
  - or a sustained revenue uplift ≥ 1.31 on basis dayrates;
  - or a price ≤ NOK ~95 ($10.21).
- **What does not flip it:** the Q3 report and the next three years. They are almost fully booked,
  and the cash yield (~10%) is real and rising.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation or price target.

## 11. Tracking

| Quarter | Item | Model (v1) | Actual | Gap and cause |
|---|---|---|---|---|
| Q3-26 | Revenue / EBITDA, $m | 272 / 138 | 265.4 / 130.3 | EBITDA −8: FU 89% vs ~90% effective (third-party labour dispute on Aberdeen and Bergen); EBITDA includes +$10.7m other income against ~$13m claim costs |
| Q3-26 | Maintenance FCF, $m | 118 | ~52 `[B]` | −66: EBITDA −8; interest timing −12 (September bond coupon); capex −13 (Atlantic incident $18m, to be covered by the insurance receivable); working capital −2 vs +35 modelled, so −37 (the $50m insurance receipt was offset by trade receivables +$33m and other items); tax paid $0.1m vs ~$8m, +8 (timing); other non-cash items −5 |
| Q3-26 | Net debt 30 Sep, $m | 805 | 857 | +52 |
| Q3-26 | Dividend declared | $0.25 | **$0.27** | Raised |
| Q4-26 | Tax refund / incident cash | +37 / −10 | +39 received 6 Oct / net 0 (company) | +12 |
| 31 Dec 2026 | Net debt, $m | 738 | 776 (model v2) | +38 ($0.16 a share) |
| — | Base P_k | $10.16 | **$10.21** | +$0.05 |

- **Against the Base path:** behind on cash and EBITDA in Q3 (incident restart, labour dispute,
  receivables). Ahead on the dividend and on contracts: Atlantic's two wells were exercised, and
  Bergen's Vår term now has four priced option years to 2035. The underlying run-rate from
  September (FU 98%) is in line with Base.
- **Base IRR 6.3% → 8.1%; P_k $10.16 → $10.21:**
  - **Method +0.4 pp / +$0.09:** the rebuilt model replicates v1 at 6.4% (+0.1 pp against the
    published 6.3%); cost recalibration to $231k +0.3 pp.
  - **Report −0.3 pp / −$0.07:** Q3 actual and Q4 cash −0.55 pp; managed fleet, corporate cost
    and management value +0.25 pp; dividend floor about 0.
  - **Price/FX +1.7 pp / +$0.03:** NOK price −4.2% +1.7 pp; firmer krone −0.1 pp; valuation date
    4 Nov +0.1 pp (the P_k change is the date).
  - Bear −13.3% → −12.3% (method +0.5, report −0.7, price/FX +1.2 pp).
  - Bull 19.6% → 21.8% (method +0.3, report −0.2, price/FX +2.0 pp).

## 12. Risks and signposts

- **Nordkapp 2028 rate (by end-2026, two brokers).**
  - It is a clean NCS market print for 2028 work.
  - Above $470k → Bull side; below $430k → Bear side. The model holds $450k.
  - Transocean's 2028 prints span $441–517k for single rigs.
- **Deepsea Atlantic (2009).**
  - Signposts: Equinor's remaining two priced wells and the unpriced options beyond. A lapse
    leaves the oldest rig open into 2028 against the Bear MCU.
  - Transocean Barents (same vintage) took a 3-year Vår term at $470k from mid-2027: a supportive
    comparable.
  - Concentration risk is shown by 2026: one incident cost 106 days.
- **Cash items to come:** the $43.7m insurance receivable (offsets the remaining incident capex);
  any recognised excess claim (a contingent asset, upside); and the unwind of trade receivables
  ($146m).
- **Q3 dividend:** ex-date 12 Nov (the price drops by ~NOK 2.5); paid 25 Nov.
- **Stavanger collar.** The ceiling caps the Bull upside to $464–478k; the floor protects Bear at
  ~$400k. The index formula is `[?]` (3% a year assumed).
- **Mid-cycle anchors.**
  - Rig BBB open checkpoint 13: transactions imply 8–12% above Base mid-cycle.
  - Westwood's long-run Norway series (checkpoint 10).
  - Any HE semi sale price (incl. backlog split).
  - Long-term NCS packages ($402k, Equinor 2028–31) sit at Base mid-cycle.
- **HE supply:** Beacon Pacific's reactivation (UK, Q3 2027) shows that idle 6G semis return when
  term work is offered. Rig BBB to assess.
- **FX.** Part of revenue and most costs are in NOK. A weaker krone lowers USD costs and the NOK
  part of rates together; the net effect is not split out `[?]`.
- **Ownership.** 49.85% Odfjell family control; free float ~50%; average daily volume ~315k
  shares (~NOK 33m).

## For other modules

- **Rig Market BBB (input for the re-run due by 9 Nov; no change requested by this document):**
  - **Transocean fleet status 2 Nov (primary, SEC 8-K ex. 99.2):**
    - Not in the fixture log: Barents (2009) Vår Energi Jun 2027–Jun 2030 **$470k** firm, priced
      options to Jun 2034.
    - Norge Harbour Jan–Oct 2028 **$517k**. This resolves checkpoint 9: the log's $497k should read
      $517k.
    - Norge Shell firm Mar–Jul 2029 at **$517k** (grade A; the log has ~$517k B, "late 2028").
    - Spitsbergen Equinor Apr–Dec 2027 $519k; Enabler Dec 2026–Apr 2028 $480k; Encourage May 2027–
      May 2028 $441k.
    - Equinor package (Enabler Apr 2028–Apr 2031, Encourage May 2028–May 2030, Endurance Jun 2027–
      Jun 2029) at **$402k**.
    - HE fleet in Q3: average daily revenue $504k, revenue efficiency 97.7%, utilisation 95.1%.
      Transocean 2027 coverage ~95%. Valaris closing 1 Dec 2026, all approvals in hand
      (checkpoint 3).
  - **Odfjell Q3:**
    - Tier-1 HE booked for 2027, many into 2028; newbuilds unlikely (company view `[E]`).
    - Beacon Pacific (6G semi) is being reactivated for Serica (UK, six wells, Q3 2027–Q4 2028)
      under ODL management: a UK semi supply addition.
    - Deepsea Yantai (managed) has Okea for 2 wells (~80 days), firm to Q4 2027.
    - Deepsea Bergen Vår term: four 1-year priced options to early 2035.
  - **HE semi asset convention vs realised NCS margins** (carried from v1):
    - ODL earns ~$320k a working day at a ~$450k basis rate. Q3 calibration: U 1.25, cash cost
      $229k.
    - The convention gives $182k. Bollsta ($480m with $355m backlog) sits between: ~$448k on the
      convention, ~$332k on ODL economics.
    - Suggest a review with checkpoints 11 and 13.
- **Nordic HY BBB / hy-issuers:** ODRG02 (Odfjell Rig III, $650m 7.25%, Mar 2031).
  - Net debt $857m at 30 Sep; leverage 1.6x on the covenant definition; liquidity $261m;
    covenants met.
  - Net debt/EBITDA is 0.6x in Base and 1.1x in Bear at exit. The amortising structure leaves no
    refinancing risk inside the window in any scenario.
  - Not on any watchlist; no change requested.
- **Equity BBB:** read only (exit cross-check, NOK path); no input back.

## Change log

- **2026-11-04 (v2): Q3 update.**
  - **Actuals in:** Q3 actuals replace the estimate. The stub is now Q4-26 only. Net debt at
    30 Sep is $857m (model $805m).
  - **Dividend:** $0.27 declared (ex 12 Nov, paid 25 Nov); the floor is raised to $0.27.
  - **Q4 cash:** tax refund $39m received 6 Oct; incident cash net zero from Q4; Q4 capex $20m.
  - **Cost calibration:** $231k a rig-day, confirmed by Q3 ($229k). v1's tables ran at ~$234k.
  - **Other inputs:** managed fleet $6–7m EBITDA a quarter (Beacon Pacific) and management value
    $84m; corporate −$12m a year; leases $45m.
  - **Price:** NOK 104.40 at USD/NOK 9.2934 ($11.23), valuation 4 Nov.
  - **Transocean Q3 fleet status:** read across. It supports the Base path but leaves mid-cycle
    unchanged; it goes to Rig BBB. Rig BBB paths and mid-cycle are unchanged.
  - **Model rebuilt:** the v1 scripts were not retrievable. The model was rebuilt from v1's stated
    parameters and replicates v1 within 0.1 pp (6.4% vs 6.3%; V_T $10.60 vs $10.59; P_k $10.18 vs
    $10.16).
  - **Result:** Base IRR 6.3% → **8.1%**; P_k $10.16 → **$10.21**; margin of safety −13.2% →
    **−9.1%**. Bear −13.3% → −12.3%; Bull 19.6% → 21.8%. **Verdict unchanged: fails.**
  - **Split:** method +0.4 pp, report −0.3 pp, price/FX +1.7 pp (Summary and Tracking).
  - **Added:** price triggers in NOK (incl. ex-dividend) and the E / R reference row
    (cycle-first rule; reference only).
  - **Cross-check:** a second, independent rebuild with slightly different managed-fleet and
    corporate inputs (management value $65m, corporate −$10m a year, Beacon Pacific +$1.5m a
    quarter to Q4-28) gave Base 7.9% / P_k $10.17 / V_T $10.35, Bear −12.5%, Bull 21.6%. Same
    verdict; the v2 tables reproduce exactly on the stated inputs.
  - **Stale after:** 9 Nov → 4 Dec 2026.
- **2026-10-26 (v1):** first analysis.
  - Decision basis: ODL's realised economics for both the window and the exit marks.
  - Rig BBB convention and the Bollsta-implied marks shown as sensitivities.
  - **Verdict: fails (Base −13.2%).**

## Appendix: own assumptions `[A]`

| Assumption | Value | Why |
|---|---|---|
| Revenue uplift U | 1.27 | Mean of the fleet calibrations, Q1-26 (1.29) and Q3-26 (1.25); Q2-26 Bergen 1.25 |
| Cash cost | $231k a calendar rig-day (2026), +3% a year | Q1-26 $231k, Q3-26 $229k ex incident items |
| Basis rates without a disclosed value | Atlantic 478 (2026) / 492 (2027); Aberdeen 470 (to Oct 2026); Nordkapp 460 (2026) / 440 (2027); Stavanger 437 / 435 | Calibrated so the Q1-26 fleet average (~$456k) and margin reconcile within 2.4%; 2027 slice matches the company's backlog by year ($752m vs $754m) |
| Escalation on in-place contracts | 3% a year from 2027 | Contracts carry yearly escalation excluded from the backlog (Aberdeen release) |
| Stavanger collar index | 3% a year from Jun 2023 | Formula not disclosed |
| Nordkapp 2028 rate | $450k in all scenarios | Set by end-2026 at the then market (Rig BBB 2028-start median ~$452k; Transocean 2028 prints $441–517k) |
| Contract ends | Atlantic 15 Dec 2027; Aberdeen 15 Feb 2029; Bergen Equinor to 31 Mar 2028, Vår to 31 Mar 2031; Stavanger ~15 Feb 2030 | Company quarters given; mid-points assumed |
| SPS | Nordkapp Q4-28 (20 days, $35m); Atlantic Q2-29 (20 days, $35m); Bergen Q3-29 (15 days, $30m) | Nordkapp `[F]`; others on a 5-year cycle |
| Q4-26 cash items | +$39m tax refund `[F]`; incident capex offset by the $43.7m insurance receivable (net 0); capex $20m | Company statement; 9M run-rate ex incident |
| Net debt at valuation date | $777m | 30 Sep $857m less the refund and pro-rata Q4 cash flow |
| Interest | 7.6% on net debt + $60m cash; 2% on cash; accrual basis | Q3 other interest $17.1m (7.6%); bond coupon in March and September (cash timing not modelled) |
| Open-rig contracting | Rolling ~1-year terms at the year's leading edge; 0.5 year of scenario-signed backlog at exit | NCS options are typically wells or ~1-year periods |
| External fleet | EBITDA $6.0m (Q4-26), $6.5m (H1-27), $7.0m a quarter from Q3-27 | Q3 $6.1m; Hercules (Q1-27), Mira (Apr-27), Beacon Pacific (Q3-27) |
| Management business value | 3x exit EBITDA ($84m) | Third-party contracts can end |
| Corporate cost | −$12m a year | 9M-26 −$9.6m ex the sublease gain |
| Dividend rule | 75% of FCF after debt service, floor $0.27 while covered, the full FCF after debt service below it | Board raised to $0.27; policy criteria are qualitative |
| D&A for book equity | $54.2m a quarter | Q3 actual |

## Appendix: sources

| Source | Content | As of |
|---|---|---|
| [ODL Q3 2026 report (PDF)](https://www.odfjelldrilling.com/wp-content/uploads/2026/11/odl-report-for-the-3rd-quarter-of-2026-202611021913-1.pdf) | Statements, segments, FU by rig, cash flow, debt note and repayment schedule, insurance (note 4), commitments (note 11), tax case (notes 12, 16), shares and dividends (note 13), ownership (note 15), leverage calculation | 30 Sep 2026, published 3 Nov |
| [ODL Q3 2026 presentation (PDF)](https://www.odfjelldrilling.com/wp-content/uploads/2026/11/odfjell-drilling-ltd-presentation-for-the-third-quarter-of-2026-2.pdf) | Contract awards (Bergen options to 2035, Yantai, Mira, Beacon Pacific), market outlook, cash-flow bridge, dividend history | 3 Nov 2026 |
| [ODL Q2 2026 report (PDF)](https://www.odfjelldrilling.com/wp-content/uploads/2026/08/odl-report-for-the-2nd-quarter-of-2026-202608172140-3.pdf) | 30 Jun balance sheet (receivables $113.3m, leases $43.6m) for the Q3 working-capital bridge | 30 Jun 2026 |
| Newsweb via Nordic Financial `search_filings` (ODL, 2026) | Q3 announcement and dividend key information (3 Nov), Atlantic options (16 Oct), Vår LoA (10 Sep), tax ruling (2 Sep), Nordkapp extension (17 Jul) | as dated |
| [ODL — Beacon Pacific management agreement](https://cdn.financialreports.eu/financialreports/media/filings/9909/2026/RNS/9909_rns_2026-11-02_c64799c9-807b-4c6a-9f07-b17f2144ce37.html) (via FinancialFilings) | 6G semi, owner Beacon Pacific Offshore Ltd; Serica UK, six wells from Q3 2027; fees not disclosed | 2 Nov 2026 |
| FinancialFilings `filings_list` (company 9909) | No share issue or insider trade since 15 Aug | 3 Nov 2026 |
| [Transocean 8-K, 2 Nov 2026 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/1451505/000145150526000083/) | Ex. 99.1 Q3 results (HE average daily revenue $504k, RE 97.7%, utilisation 95.1%; 2027 coverage ~95%; Valaris closing 1 Dec); ex. 99.2 fleet status (HE semi contracts and dayrates) | 2 Nov 2026 |
| [ODL bond pricing, 21 Nov 2025](https://www.odfjelldrilling.com/disclosure/odl-successful-pricing-of-senior-secured-first-lien-bonds/) | $650m 7.25%, semi-annual coupon, maturity Mar 2031 | 21 Nov 2025 |
| [ODL Q4 2025 presentation (PDF)](https://www.odfjelldrilling.com/wp-content/uploads/2026/02/odl-q4-2025-presentation-2.pdf) | Backlog by year (2027E $754m), Bollsta ~$100m EBITDA | 25 Feb 2026 |
| Yahoo `ODL.OL`, `NOK=X` | Price NOK 104.40 (3 Nov close); USD/NOK 9.2934 (3 Nov 15:15–15:30 UTC); shares; FY2026 EPS consensus $1.21 | 3 Nov 2026 |
| `docs/rig-market-bbb.md` | HE semis (NCS) row, MCU, mid-cycle, asset convention, fixture log | 10 Oct 2026 (+ small updates to 28 Oct) |
| `docs/oil-market-bbb.md` | Scenario background | 31 Oct 2026 |
| `docs/equity-market-bbb.md` | Oslo exit P/E, P/B, mid-cycle return; USD/NOK path | 17/18 Oct 2026 |
| Model scripts (scratchpad, not part of the workspace) | Rebuilt daily rig-day model, quarterly cash flows, marks, XIRR, v1 replication and bridge | 4 Nov 2026 |

Data gaps:
- The v1 model scripts were not retrievable; the model was rebuilt from the stated parameters
  (replication within 0.1 pp).
- Contract dayrates for Nordkapp, Stavanger (current year) and Aberdeen (to Oct 2026) are not
  disclosed and are calibrated `[A]`.
- The model's firm backlog ($2.25bn) is ~10% below the reported $2.5bn; not resolved `[?]`.
- Managed-fleet fees (Beacon Pacific, Yantai, Mira) are not disclosed.
- The Q4 report date is not announced. Consensus by quarter was not found; the Yahoo FY figure
  looks inconsistent.
- The Q3 webcast was not reviewed (no transcript found).
