# Hafnia Limited (HAFNI / HAFN) — IAF analysis, stub Q3–Q4 2026 + 2027–2029

**Note 5 Nov 2026: kept unchanged; read TORM Q3 of 4 Nov.** No new version: every value below is v7 of 24 Oct. Skill used for this note: iaf-valuation **2026-11-01.1** (the v7 model was built under 2026-10-18.2). The 2026-11-01.1 change (the summary of an opportunistic cyclical equity position leads with the cycle) is not applied in this note; it comes with the full update at Hafnia's Q3 report (18 Nov).
- **TORM Q3 2026** (4 Nov; Nasdaq Copenhagen release via Nordic Financial, PR Newswire) `[F]`: TCE $353m ($40,102/day; LR2 52,575, LR1 38,667, MR 36,137), EBITDA $274m, net profit $199m. FY26 guidance narrowed up: TCE $1,750–1,900m (was 1,700–1,900), EBITDA $1,350–1,500m (was 1,300–1,500), so Q4 EBITDA $459–609m against Q3 $274m. **Q4 cover (28 Oct) 53% at $78,419/day** (LR2 68% at 112,150, LR1 38% at 106,271, MR 49% at 59,722). Dividend **$1.35** (ex 16 Nov Copenhagen / 17 Nov New York, paid 2 Dec). Fleet value 30 Sep $4,333m (30 Jun 4,056), NAV $4,062m = $39.60/share (30 Jun 36.50). New: 8 LR2 newbuilds in a 50/50 JV (2029–30), 2 more MR options. Nothing on Hafnia's stake (still ~19.85%, 20.38m shares) and no transaction. TRMD $37.64 at the 4 Nov close (−6.5% on the day; Yahoo).
- **Change gate: what the model reads moves by less than the minimum change, and the verdict cannot flip.**
  - TORM Q4 dividend $1.35 against the modelled $1.12 (DPS rule): +$4.7m Q4 income, P_k +NOK 0.07.
  - TORM exit value: TORM's 30 Sep marks are higher (fleet +6.8%, net debt ~$319m → ~$271m), but Hafnia's own fleet is still on 30 Jun broker values. Both are re-based together on 30 Sep values at Hafnia's Q3 report. TORM alone on 30 Sep values would add about NOK 0.6 to Base P_k `[A]`, not adopted.
  - TRMD $39.89 → $37.64: stake $813m → $767m, NAV today −NOK 0.8/share. NAV today is not a decision figure.
  - Q4 stub (the validation flag in Near term): TORM's Q4 cover and implied Q4 TCE ($599–749m, 1.7–2.1× Q3) support the modelled Hafnia Q4 (1.51× Q3, $50.4k/day) and argue against the lower consensus ($378m). TORM's booked MR $59.7k and LR1 $106k are above Hafnia's modelled open-day 44 and 96 (LR2 112 is below 176, but Hafnia's LR2s are mostly on TC-out). That points to upside in the Q4 stub (stub factor 1.0: P_k +1.9), not adopted before Hafnia's own Q4 cover on 18 Nov. The stub rows are set in Oil Shipping BBB.
  - Indicative market re-mark, not adopted: at the 4 Nov close **NOK 93.05** (Yahoo `HAFNI.OL`, −5.1% vs 98.00) and USD/NOK 9.290 (Yahoo `NOK=X`, 5 Nov 07:06 UTC), Base IRR ≈ +1.4% (v7 −0.5%), P_k ≈ NOK 72.5, margin of safety ≈ −22%. **Still fails.**
- **Hafnia news 23 Oct – 5 Nov: none.** Newsweb API (issuer HAFNI; filter checked on 5–12 Oct) shows no message, and a web search found no news. Hafnia's Q3 report is on **18 Nov 2026** (Yahoo, not an estimate). TORM's FY26 report is not yet dated (2026 calendar: 26 Feb; expected late Feb – early Mar 2027 `[E]`).

Version 7, 24 Oct 2026: re-mark after Oil Shipping BBB of 24 Oct (valuation date 24 Oct; price and FX at the Friday 23 Oct close). Earlier: v6 19 Oct (exit-criteria check), v5 17 Oct, v2–v4 10 Oct, v1 5 Oct. Skill revisions used: **iaf-valuation 2026-10-18.2** (unchanged since v6). Baselines read: **oil-shipping-bbb 2026-10-24.1** (24 Oct baseline), oil-market-bbb 24 Oct baseline (header rev 2026-10-11.1), `docs/equity-market-bbb.md` (17 Oct, amended 18 Oct; not re-run since) for the exit cross-check and the NOK path. Sector inputs:
- `docs/oil-shipping-bbb.md`, baseline **24 Oct 2026** (Final, rev 2026-10-24.1; stale after 23 Nov, or earlier on OPEC+ 1 Nov, the US midterms 3 Nov, the USTR/China port-fee deadline 9–10 Nov, > 30 sanctioned VLCCs approved, or a new Oil Market BBB). Read: Conclusion, both Interface tables, For IAF and the change log since 17 Oct.
  - **New stub method:** October segment average plus Nov–Dec on the paper's own path; the route-ratio shortcut is now a cross-check only. It re-marked VLCC (850 → 700) and Aframax (245 → 305) only.
  - **Product rows used by Hafnia are unchanged:** LR2 220, LR1 120 and MR 55 stubs kept (computed +6%, −5% and offsetting moves, within the baseline's minimum change); 2027–29, the Year-1 quarters, mid-cycle TCE and mid-cycle values unchanged in all scenarios. Its For IAF section: "Hafnia: no change (LR2, LR1, MR stubs kept)".
  - The only product value that moved is the **LR1 5-yr mark now, 67 → 68** (Intermodal October average). It enters today's NAV and the interim marks, not V_T or NAV_0.
- `docs/oil-market-bbb.md`, baseline **24 Oct 2026** (Final), re-run and **kept unchanged** (all paths and mid-cycle values). Used only through Oil Shipping BBB; no own oil view.
- `docs/hy-market-bbb.md` is not used: Hafnia's debt is USD bank debt on SOFR with no NOK bonds. `docs/equity-market-bbb.md` (17 Oct, amended 18 Oct) is context only and does not move k; its NOK path (USD/NOK Bear +12% / +9% / +9%, Bull −3%, Base spot flat) is applied as moves from today's spot. Rig, supply, defense and AI baselines are not used.
- **Change gate (v7): nothing that moved in the 24 Oct shipping baseline moves a Hafnia decision figure.** The decision figures move only with the market re-mark: price NOK 94.85 → **98.00** (+3.3%), USD/NOK 9.443 → **9.340** (−1.1%), valuation date 17 → 24 Oct. USD cash flows, USD V_T and the model are unchanged from v5/v6. Base IRR +1.2% → **−0.5%**, P_k NOK 73.2 → **72.6** (FX −0.8, one week less discounting +0.2), margin of safety −22.8% → **−25.9%**. The verdict (**fails**) is unchanged.
- **Method (since v5, iaf-valuation 2026-10-11.3):** exit-consistency test (Step 3). Base and Bull LR2 and LR1 end 2029 more than 10% above mid-cycle with no named reason in the baseline, so a **2-year reversion tail** is added to V_T (Base +NOK 0.60/share, Bull +NOK 1.68). See the exit-consistency table.
- **Oldest inputs:** Hafnia's balance sheet, broker values and segment data are at 30 Jun 2026 (Q2, the latest reported quarter; Q3 is due 18 Nov). Cover is at 17 Aug. Consensus is now Yahoo's (seen 24 Oct): 1 EPS estimate and 3–4 revenue estimates, so thin. Price and FX are the 23 Oct close (1 trading day; valuation date Saturday 24 Oct). FinancialFilings is at its monthly credit limit (resets 1 Nov); SEC filings were checked through Yahoo's filing list instead (last 6-K 13 Oct).

## Summary

**Verdict**
- **Fails, by a little more than in v6.** Base IRR_T is **−0.5%** against k = 12%. The hurdle price is **NOK 72.6** vs P = NOK 98.00, a **margin of safety of −25.9%** (v6: −22.8%). The share rose 3.3% in the week (NOK 94.85 → 98.00) and the krone firmed 1.1% (USD/NOK 9.443 → 9.340), which, net of one week less discounting, takes NOK 0.6 off P_k. Nothing in the 24 Oct shipping baseline moves a Hafnia input: the LR2, LR1 and MR stubs, rows, Year-1 quarters and mid-cycle values are all unchanged.
- **Bear breaks the thesis:** IRR −19.4%, about 44% of capital lost. The balance sheet survives (fully committed LTV ~30%).
- **Bull** returns ~22% a year (P_k NOK 120.7). The price reflects 53% of the way from the Base to the Bull hurdle (v6: 45%).
- **Exit criteria (v6 check, IAF 2026-10-18.2; re-marked): the exit is generous, not harsh.** No backlog runs past exit, so the reversion tail stands as built. The exit P/B (1.40 Base) is inside the Oslo band, but the exit P/E on Hafnia's own mid-cycle earnings is ~39x (accounting) against Oslo's 11.5x. The buyer's implied return at the NAV exit (8.6%) is below Oslo's mid-cycle return (9.1%). Re-discounting the exit marks at 9.1% gives Base IRR −1.0% (P_k 71.6); deducting capitalised operating overhead gives −4.8% (P_k 65.3). Every exit check points the same way: the NAV exit flatters Hafnia rather than penalising it.
- **What the price needs:** an exit value of ~NOK 106.1/share against the Base NOK 69.6 (× 1.52). **Base cash flows with Bull exit values no longer clear at NOK 98.00: 10.9% (P_k 95.5).** No single input in the sensitivity table now closes the gap; the price needs Bull-type asset values at exit and more.

**Decision table**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (exit 31 Dec 2029) | −19.4% | **−0.5%** | +22.3% |
| V_T per share (NOK) | 42.0 | **69.6** | 105.7 |
| P_k / margin of safety (P = 98.00) | 41.2 / −58% | **72.6 / −25.9%** | 120.7 / +23.1% |
| Capital preserved? ΣD_t + V_T vs P | No: 54.7 (−44%) | **No: 96.8 (−1% nominal)** | Yes: 160.0 (+63%) |
| Cumulative Maintenance FCF per share, Q4-26 to 2029 (NOK) | 15.9 | **32.4** | 61.6 |
| Net debt per share at exit (NOK; incl. leases and pool facility) | 15.4 | **13.3** | 11.2 |
| Balance-sheet line | Fully committed LTV ~30% in 2029; net loss in 2029 stops dividends; liquidity covers the $490m newbuild bill | LTV ≤ 19%, 90% payout throughout | LTV 10–13% |

**Per-share path (NOK per share; 542.2m shares, USD/NOK 9.340)**

| Base | Q3-26 (ended) | Q4-26 | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| Adj. EBITDA, $m | 232 | 371 | 974 | 504 | 410 |
| Adj. EBITDA per share | 4.00 | 6.38 | 16.78 | 8.67 | 7.06 |
| Maintenance FCF per share | 3.38 | 5.81 | 14.89 | 6.69 | 5.02 |
| Debt amortisation per share | 0.21 | 0.21 | 0.58 | 0.32 | 0.29 |
| FCF after debt service per share | 3.17 | 5.60 | 14.31 | 6.37 | 4.73 |
| D_t paid per share | — (Q2 dividend paid 23 Sep, before the valuation date) | 2.97 | 15.19 | 5.49 | 3.54 |
| Net debt per share, end of period | 10.6 | 8.1 | 10.1 | 10.8 | 13.3 |
| V_t per share | — | 90.3 | 82.0 | 75.4 | **69.6** |
| **Bear:** Maintenance FCF / V_t per share | 3.38 / — | 5.81 / 90.3 | 6.42 / 71.8 | 2.62 / 57.5 | 1.09 / **42.0** |
| **Bull:** Maintenance FCF / V_t per share | 3.38 / — | 5.81 / 90.3 | 31.91 / 96.8 | 14.04 / 99.9 | 9.88 / **105.7** |

Q3-26 has ended and its cash is already in net debt at the valuation date; it is shown for tracking.

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value · `[E]` external or secondary · `[C]` carried from an earlier version · `[A]` own assumption · `[?]` not found.

## Header

| Item | Value |
|---|---|
| Company | Hafnia Limited (Singapore; BW Group controlled). Product and chemical tankers: LR2, LR1, MR (incl. IMO II), Handy (IMO II). Listed on Euronext Oslo (HAFNI) and NYSE (HAFN). Reports in USD |
| Price (P) | **NOK 98.00**, Oslo close Fri 23 Oct 2026 (session end 14:20 UTC, last print 14:28 UTC; Yahoo `HAFNI.OL`; day range 95.85–99.60; previous close 96.45; 52-week 51.7–106.0) `[F]`. Cross-check: NYSE HAFN $10.50 at 20:00 UTC × 9.324 (20:00 bar) = NOK 97.9, consistent |
| Valuation date / exit date | 24 Oct 2026 / 31 Dec 2029, **T = 3.19 years** |
| Shares | **535.33m** issued (registered 5 Oct `[F]`; Yahoo 535,331,154 on 23 Oct), **542.2m** used per share (+6.85m option dilution = diluted − basic at 30 Jun `[F]`). No share issue since (no Newsweb notice 16–23 Oct; last 6-K 13 Oct) |
| FX | USD/NOK **9.340** (Yahoo `NOK=X` 15-min bar 14:15 UTC on 23 Oct, close 9.34025, matching the Oslo close) `[F]`. Cross-check: Norges Bank fixing 23 Oct 9.3509 (14:15 CET; the krone firmed into the afternoon). P = **$10.49**. Held constant |
| Market cap / EV | NOK 52.5bn = **$5.62bn** (535.3m shares). Net debt incl. leases and the pool borrowing-base facility ≈ $614m at 30 Sep `[A, Q3E]` → EV ≈ **$6.2bn**; EV / 2027E Base EBITDA 6.4x. EV includes the TORM stake ($813m) and JV equity ($337m) |
| NAV today (market marks) | Owned fleet $3,963m + JV $337m + TORM stake $813m (20.38m shares × $39.89, 23 Oct) + TC-in purchase options $220m + newbuild instalments $30m + other $13m + net working capital $404m − net debt $614m = **$5,165m = NOK 89.0/share → P/NAV 1.10**. Product marks from the 24 Oct baseline: LR1 5-yr 67 → 68; LR2 and MR unchanged |
| NAV_0 (Base mid-cycle marks) | **$4,353m = NOK 75.0/share → P/NAV_0 1.31** (Bear NOK 49.2 → 1.99; Bull NOK 107.5 → 0.91) |
| Track | **B** (tanker owner, ~83% of 2027 days open, finite-life vessels, newbuild programme). FCF basis, year-by-year IRR, P vs P_k |
| k | **12%**, not raised. Net LTV 13% (30 Jun), 87 owned vessels plus 14 JV units, two liquid listings (~1.4m shares a day in Oslo, ~2.1m in New York). BW Group control and related-party funding are a governance flag, not priced through k |
| Horizon | Stub Q3-26 (ended, unreported) + Q4-26; 2027 by quarter; 2028–2029 annual (modelled quarterly, reported annually) |
| Basis | IFRS as reported. Adj. EBITDA includes TORM dividend income and the fee-based businesses; JVs equity-accounted |

**Sources (connector · document · period):**
- **FinancialFilings** (company id 9980, Hafnia Limited, SG, USD), read on 5 Oct: Q2 2026 interim report (57967361, period ended 30 Jun 2026), Q2 presentation (59231672), 424B5 prospectus supplement (62394258, 25 Sep), placement and share-capital announcements (23 Sep – 5 Oct), TORM purchases (16 and 24 Sep). The connector is at its monthly credit limit (HTTP 429 again on 24 Oct; resets 1 Nov). **SEC filings were checked through Yahoo's `secFilings` list (24 Oct): the last 6-K is dated 13 Oct** (the CFO trade notice), so nothing new was filed with the SEC after 13 Oct.
- **Newsweb, 24 Oct sweep** (Oslo Børs API via the in-app browser; 559 messages 16–23 Oct, filter checked on the 12 Oct Hafnia and TORM notices): **no Hafnia and no TORM message from 16 to 23 Oct.** No fleet deal, charter, dividend, share or insider notice.
- **Newsweb** (earlier sweep), all Hafnia and TORM messages 5–17 Oct:
  - Hafnia 6 Oct: borrowed placement shares redelivered to BW Group (no share-count change).
  - **Hafnia 12 Oct: CFO Perry Van Echtelt sold 50,000 shares at NOK 101.52 on 9 Oct;** he holds 563,544 shares and options. Insider sale near the 52-week high.
  - TORM 5–9 Oct: Oaktree sold its last 6.33m TORM shares (~$40.05) and exited; its board member stepped down. Hafnia stays at ~19.85%.
  - **TORM 12 Oct: FY26 guidance raised** to TCE $1.7–1.9bn and EBITDA $1.3–1.5bn (from $1.4–1.6bn and $1.0–1.2bn), "based on current coverage and expectations for continued market strength during the remainder of the fourth quarter". TORM's Q3 report is due 4 Nov.
  - TORM Q2 2026 report (26 Aug): dividend $2.40/share, fleet value $4,056m, NAV $36.50/share at 30 Jun.
- **Yahoo** (24 Oct): HAFNI.OL and HAFN (23 Oct close), NOK=X (intraday 23 Oct), TRMD ($39.89, 102.71m shares), consensus `[E]` (`earningsTrend`: Q3-26 EPS $0.30 and Q4-26 $0.30, 1 estimate each, both raised from $0.26 in the last 7 days; FY26 $1.37 and FY27 $0.71, 1 estimate; revenue Q3 $298m (274–316) and Q4 $378m (330–425), 3 estimates; mean target $11.5, 2 analysts), Q3 report 18 Nov 2026 (`isEarningsDateEstimate` false).
- **Zacks** (HAFN, 24 Oct): BTIG Strong Buy, target $12 (14 Sep, reiterated); DNB Carnegie Hold (12 Mar); Clarksons Platou Strong Buy (9 Feb); Fearnley target $6.71 (Dec 2025, stale). No Zacks news on HAFN or TRMD in the last 15 days.
- **Sector:** rows, mid-cycle values, anchors, catalysts and signposts from `docs/oil-shipping-bbb.md` (24 Oct); scenario mapping from `docs/oil-market-bbb.md` (24 Oct). No own oil or tanker forecast is made here.

## Scenario definitions (from Oil Shipping BBB, 24 Oct; product rows unchanged since 10 Oct)

| Scenario | Catalyst | What it does to Hafnia |
|---|---|---|
| **Base** (decision) | Oil Base (armed normalisation; crude via bypass and escort; Gulf and Gulf of Oman contested; ME oil incl. bypass above pre-war). Product cargo volumes are down, but rates are set by tonnage: LR2s keep trading dirty, Gulf product exports recover slowly; the 2028–29 delivery peak and LR2s returning to clean trade in H2-27 bring rates near parity. Rows 2027 / 2028 / 2029: **LR2 65 / 38 / 35, LR1 45 / 30 / 28, MR 37 / 25 / 22** ($k/day) | 2027 fleet TCE **$36.7k/day**, EBITDA **$974m**, net profit $777m, dividends declared NOK 12.0/share. 2028 $26.2k/day (EBITDA $504m); 2029 $23.6k/day (EBITDA $410m) |
| **Bear** (stress) | Iran–USA deal plus recession (still remote; talks stalled). **Supply leg:** a wide US approval of sanctioned tankers for mainstream trade (> 30 VLCCs; policy announced 19 Oct, analysts count 14–24 realistic). Shuttles, STS and Cape routing end in H1-27, LR2s return to clean trade, the delivery wave meets slack demand. Rows: **LR2 36 / 29 / 25, LR1 28 / 23 / 20, MR 22 / 19 / 17**; mid-cycle values ~30% below Base | 2027 $23.8k/day, EBITDA $488m; net loss in 2029 (−$43m), no dividend from Q1-29. Fully committed LTV ~30%, payout 80% |
| **Bull** (stress) | US strikes after 3 Nov (a second carrier is heading to the region) and retaliation against Saudi export infrastructure, or suspension of the Gulf of Oman STS hub; USTR/China port fees return on 10 Nov. New signpost: a Saudi export facility hit with a lasting loss. Rows: **LR2 160 / 72 / 55, LR1 100 / 48 / 38, MR 58 / 33 / 27** | 2027 $62.6k/day, EBITDA $1,951m, dividends declared NOK 28.2/share in 2027 (29% yield) |

The stub (Q3–Q4 2026) is identical in all three scenarios: Q3 is 80% booked and has ended; Q4 uses the baseline stub (no scenario spread). Scenarios diverge from 1 Jan 2027.

## Company and status

- **Fleet (30 Jun 2026)** `[F]`: 103 owned vessels incl. JV units and bareboats, plus 9 time-chartered in. LR2 10 (4 in the Vista JV), LR1 28 (6 Vista JV, 2 bareboat-in, 2 TC-in), MR 54 (13 IMO II; 4 Ecomar JV, 2 H&A JV sold in July, 7 TC-in), Handy 20 (18 IMO II, 1 bareboat-in). **Average age of owned vessels 9.7 years.** Consolidated owned fleet (excl. JV): LR2 6, LR1 20, MR 41, Handy 20 = 87.
- **Broker values (30 Jun)** `[F]`: $4,255m, of which **$3,739m 100%-owned** and $516m JV share (Vista $353m, Ecomar $121m, H&A $42m committed sale). Segment values incl. JV: LR2 $697m, LR1 $1,092m, MR $1,745m, Handy $721m.
- **Segment TCE ($/day, incl. TC-out)** `[F]`:

| | Q3-25 | Q4-25 | Q1-26 | Q2-26 | Q3-26 booked (17 Aug) |
|---|---|---|---|---|---|
| LR2 | 36,527 | 33,163 | 35,316 | 46,855 (spot 131,160) | 93% at 39,169 |
| LR1 | 29,229 | 30,986 | 38,194 | 52,057 | 75% at 35,908 |
| MR | 24,785 | 26,307 | 27,958 | 43,767 | 77% at 29,614 |
| Handy | 22,648 | 24,006 | 25,589 | 35,866 | 89% at 25,596 |
| Fleet | | | | **44,093** | **80% at 30,716** |

- **Cover (17 Aug)** `[F]`: H2-26 53% at $28,917; **2027 17% at $25,742** (LR2 74% at $30,726, LR1 3% at $27,989, MR 17% at $23,895, Handy 14% at $22,533, all TC-out). JV 2027: 62% at $25,103. Pool earnings week of 17 Aug: LR1 $74,446, MR $27,833, Handy $27,009.
- **Results** `[F]`: Q2-26 TCE income $372.9m, Adj. EBITDA $287.3m, net profit $277.8m (incl. $39.3m sale gains). H1-26 net profit $457.5m. Opex incl. technical management $8,981/calendar day (Q2). G&A $23.0m a quarter. Fee-based businesses $8.8m a quarter. TORM dividend income $9.9m in Q2.
- **Balance sheet (30 Jun)** `[F]`: borrowings $885.4m (bank $808.3m incl. the $90.5m pool borrowing-base facility; sale-leaseback $34.3m; other leases $42.7m); cash at bank $271.0m (plus $82.2m pool cash and $20m restricted). Net LTV **13.0%** on Hafnia's definition. Bank debt 4.8% average. Liquidity $631m plus the new **$330m RCF** (Aug, matures 2033, undrawn). Maturities: $100m RCF 2027, $84m facility 2029, RCFs 2032.
- **Capital events Jul–Oct 2026** `[F]`:
  - **TORM:** stake **~19.85% ≈ 20.38m shares** (bought 4.5m at $32.25 on 16 Sep and 1.7m at $34.00 on 24 Sep), worth **$813m** at $39.89 (23 Oct). Oaktree exited on 6 Oct; Hafnia is TORM's largest shareholder. TORM raised its FY26 guidance on 12 Oct; its Q3 report is on 4 Nov.
  - **16–23 Oct:** no Hafnia or TORM announcement (Newsweb sweep, 24 Oct) and no new SEC filing (last 6-K 13 Oct). No fleet deal, charter, dividend or insider notice since v5.
  - **Placement 24 Sep:** 35.49m shares at NOK 80.00, net $288.6m.
  - **Insider:** CFO sold 50,000 shares at NOK 101.52 (9 Oct).
  - **H&A JV:** two MRs sold in July, $13.3m gain to Hafnia; JV to be liquidated.
  - **CEO:** Søren Steenberg Jensen replaced Mikael Skov on 1 Sep; strategy and payout policy unchanged.
- **Newbuilds** `[F]`: 10 MRs ordered in 2026, delivery 2028–29; $503.6m contracted after 30 Jun. Capex profile read as Q3-26 30, Q4-26 50, 2027 100, 2028 110, 2029 230 = $520m `[E/A]` (≈ $52m a vessel; MR newbuild $52.5m in the baseline).
- **TC-in purchase options** `[F]`: 7 MRs (option ~$29.1m) and 2 LR1s (~$38.3m); in-the-money value $191m at 30 Jun.
- **Dividend policy** `[F]`: quarterly payout of net profit by net LTV: > 40% → 50%, 30–40% → 60%, 20–30% → 80%, **≤ 20% → 90%**; from 2027 on a **fully committed basis**. Q2-26 dividend $0.5003, paid 23 Sep — already paid, not counted.

## Near term: stub quarters (all scenarios)

| | Q3-26E (ended 30 Sep, unreported) | Q4-26E |
|---|---|---|
| Booked share / rate | 80% at $30,716 (17 Aug) `[F]` | **26% at ~$25.2k** (Q3 vs H2 cover, by segment `[B]`) |
| Open-day rate, $k/day | LR2 100, LR1 70, MR 35, Handy 30 `[A]` (September fixtures; pool levels mid-Aug; load-to-discharge lag) | 0.8 × Oil Shipping BBB stub (LR2 220, **LR1 120**, MR 55): **LR2 176, LR1 96, MR 44, Handy 39.6** `[A]` |
| Operating days (consolidated, excl. JV) | 8,705 `[F]` | 8,793 (214 drydock days `[F]`) |
| Fleet TCE | **$33.7k/day**, $293m | **$50.4k/day**, $443m |
| Adj. EBITDA (incl. TORM dividends $34.1m / $22.8m) | **232** | **371** |
| Net profit (incl. JV; Q3 incl. $13.3m H&A gain) | 191 | 329 |
| Maintenance FCF ($m / NOK per share) | 196 / 3.38 | 337 / 5.81 |
| Dividend declared (90%) | **$172m = NOK 2.97/share**, paid ~15 Dec 2026 `[A]` | **$296m = NOK 5.10/share**, paid ~20 Mar 2027 `[A]` |
| Net debt end of quarter ($m / NOK per share) | 614 / 10.6 | **470 / 8.1** |

- **Validation flag (Q4):** the modelled Q4 TCE is 50% above Q3 (> 30%). Named cause: the baseline's Q4 stub (LR2 220, LR1 120, MR 55; kept on 24 Oct under the new stub method: LR1 from TC5 Q4 paper $190k × ~0.6 = 114, MR from offsetting TC7/TC18 paper). **Second source, partial:** TORM's 12 Oct guidance upgrade (FY26 EBITDA +$300m at the midpoint, mostly H2) cites Q4 coverage and continued strength in the product market. Hafnia's own Q4 cover at the Q3 report (18 Nov) is the check.
- **The new stub method and the stub factor 0.8:** the baseline's Q4 value is a quarter average (October actual plus Nov–Dec on the paper), and it notes that company open days fall mostly in Nov–Dec. The Hafnia factor 0.8 `[A]` carries that, plus pool realisation and the load-to-discharge lag; kept. The range 0.6–1.0 moves P_k by −1.9 / +1.9 (sensitivity table).
- **Cross-check of H2 with TORM:** TORM's new EBITDA midpoint ($1.4bn) implies H2 about 1.27× its H1. The model has Hafnia's H2 EBITDA ($603m) at 1.24× H1 ($486m), consistent.
- **Consensus** (Yahoo `earningsTrend`, seen 24 Oct `[E]`; replaces the stale Bloomberg 24 Aug figures): Q3 revenue $298m (3 estimates, 274–316) against the model's Q3 TCE $293m, in line. **Q4 revenue $378m (3 estimates, 330–425) against the model's $443m, above the high end**; it sits between stub factor 0.6 ($346m) and 0.8. EPS: Q3 $0.30 and Q4 $0.30 (1 estimate each) against the model's $0.36 and $0.61 per basic share; FY26 $1.37 (1 estimate) against $1.83. **Thin (one EPS estimate), so not the market's view; not used for the decision.** It strengthens the Q4 flag: Q4 at the consensus TCE (stub factor ~0.67) gives Base IRR −1.0% and P_k NOK 71.3 (−1.3).
- **Net debt bridge** ($m; borrowings incl. leases and pool facility − cash at bank):
  - 30 Jun: 885.4 − 271.0 = **614.4**.
  - Q3: − EBITDA 232 + tax 1.5 + net finance 9.7 + maintenance capex 25 + newbuild 30 + Q2 dividend 250 + TORM shares 203.7 − placement 288.6 + RSU 0.3 = **614** at 30 Sep (≈ valuation date). Hafnia definition (excl. pool facility): ~$524m.
  - Q4: − 371 + 1.5 + 9.7 + 22 + 50 + Q3 dividend 172 − H&A distribution 28.3 = **470** at 31 Dec (Hafnia definition ~$379m; LTV 9%).
- **Dates:** OPEC+ 1 Nov; US midterms 3 Nov; TORM Q3 report 4 Nov (Yahoo, confirmed); USTR/China port-fee suspension expiry 9–10 Nov; **Hafnia Q3 report 18 Nov 2026** (Yahoo, not an estimate); Q3 dividend ex ~early Dec, paid ~mid-Dec. No new date found since v6.

## Market input

**Oil Shipping BBB rows used** (24 Oct; all product values below unchanged from 17 Oct; $k/day; booked days at booked rates, open days at the segment row × Hafnia factor):

| Row (Bear / Base / Bull) | Stub Q4-26 | 2027 (Base Q1 / Q2 / Q3 / Q4) | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| LR2 | 220 | 36 / **65** / 160 (114 / 63 / 43 / 40) | 29 / **38** / 72 | 25 / **35** / 55 | 24 / **30** / 37 |
| LR1 | **120** (since 17 Oct; was 150) | 28 / **45** / 100 (69 / 44 / 33 / 34) | 23 / **30** / 48 | 20 / **28** / 38 | 20 / **25** / 31 |
| MR | 55 | 22 / **37** / 58 (48 / 36 / 31 / 33) | 19 / **25** / 33 | 17 / **22** / 27 | 17 / **21** / 26 |
| Handy `[A]` = 0.90 × MR | 49.5 | 19.8 / **33.3** / 52.2 | 17.1 / **22.5** / 29.7 | 15.3 / **19.8** / 24.3 | 15.3 / **18.9** / 23.4 |

Bear 2027 quarters: LR2 55 / 35 / 28 / 26, LR1 38 / 28 / 24 / 22, MR 28 / 21 / 19 / 20. Bull 2027 quarters: LR2 260 / 160 / 115 / 105, LR1 150 / 100 / 80 / 70, MR 75 / 58 / 50 / 49. All unchanged since 10 Oct (stub since 17 Oct).

| Asset values, $m (Oil Shipping BBB) | 5-yr anchor (28 Sep) | 5-yr now (Xclusiv 19 Oct; LR1 Intermodal Oct average 68.3) | 5-yr mid-cycle Bear / Base / Bull | Factor vs anchor: now; Bear / Base / Bull mid-cycle | Asset-implied TCE vs mid-cycle TCE (Base) |
|---|---|---|---|---|---|
| LR2 | 85 | 85 | 52 / 73 / 98 | 1.00; 0.61 / 0.86 / 1.15 | 34 vs 30 |
| LR1 | 60 | **68** (was 67) | 42 / 59 / 80 | 1.13; 0.70 / 0.98 / 1.33 | 27 vs 25 |
| MR (and Handy `[A]`) | 50 | 52 | 32 / 46 / 64 | 1.04; 0.64 / 0.92 / 1.28 | 23 vs 21 |
| MR newbuild | 52 | 52.5 | Base mid-cycle 51 | — | — |

- **How the rows enter:**
  - **Handy** has no row in the baseline. Derived as 0.90 × MR `[A]` (Hafnia's realised Handy/MR TCE 0.91 in Q3-25 to Q1-26; 0.82 in Q2-26). IMO II MRs use the MR row; chemical premiums ignored.
  - **LR2:** Hafnia's 6 owned LR2s are on TC-out (74% of 2027 at $30.7k; half of that cover assumed to run into 2028 `[A]`). The JV's 4 LNG dual-fuel LR2s are on TC at $25.9k through 2027, then on the row.
  - **Hafnia factor vs market, 2027+: 1.00** `[A]` (older, partly non-eco fleet vs pool scale and IMO II flexibility). Sensitivity ±10%.
  - **Stub factor 0.80** `[A]` on Q4 open days (reporting lag; pool levels; the baseline itself says Hafnia's open days fall mostly in Nov–Dec, where the paper is below the Q4 average). Sensitivity 0.6–1.0.
- **Exit and NAV marks:** Hafnia's 30 Jun broker values by segment × (mark ÷ 28 Sep anchor) × an age factor `[A]`, gliding from today's values at 31 Dec 2026 to the scenario's mid-cycle at exit. Age factor (relative to a 5-yr-old): 1.10 − 0.02a below 5 years; 1 − 0.04(a − 5) from 5 to 15; 0.60 − 0.05(a − 15) above 15, floor 0.15. Value-weighted ages at 30 Jun: LR2 7.0, LR1 9.8, MR 10.8, Handy 11.0 `[A]`.
- **What changed in the 24 Oct baseline that touches Hafnia (v7):**
  - **Nothing in the rows.** The new stub method re-marked VLCC (850 → 700) and Aframax (245 → 305); Hafnia owns neither. The LR2 stub would compute at ~233 with the higher Aframax mark (60% of LR2s trade dirty) and the clean TC1/TC15 legs, +6%, so it is kept at 220; LR1 computes at 114 (−5%), kept at 120; MR moves offset, kept at 55.
  - **LR1 5-yr now 67 → 68:** today's NAV +$17m (owned), +$3m (JV) and +$2m (purchase options), interim marks slightly higher; V_T and NAV_0 unchanged; no payout threshold crossed in any scenario.
  - **Period market at Base:** LR1 1-yr TC 60 (Intermodal) / 61 (Compass) = 102–104% of Base over the months a charter runs; MR 39.5–45 = 97–111%. The v6 signpost "a second source at $56k would lift LR1 2027" is answered: two sources now quote ≥ $56k, but measured over the same months they sit at Base, so the baseline keeps LR1 2027 at 45. The baseline says the period market supports the Base paths for valuation.
  - **Bear supply leg:** the US approval of sanctioned-tanker sales is now policy (19 Oct); 14–24 VLCCs are realistic on analyst counts, inside Base's < 30 cap. Mainly old VLCCs; small product effect.
  - **Bull:** a new signpost (a Saudi export facility hit with a lasting loss); Houthi strikes inside the kingdom; ≥ 18 tankers attacked in two weeks (Kpler); the STS hub is not suspended.
- **What changed in the 17 Oct baseline that touched Hafnia (v5):**
  - **LR1 stub 150 → 120:** the TC5 Q4 FFA fell 19% (to $197k), while MEG LR1 spot hit records; the stub follows the paper. Effect: −$43m Q4 TCE.
  - **LR1 2029 premium (28 vs parity 25) weakened:** the orderbook leg is now ~15% after the Emarat order (13 Oct), and the paper market is about at Base (forward ÷ Base 0.95, from 1.08). Kept by the baseline; it matters for the exit-consistency test below.
  - **LR1 2027 may rise** if a second source confirms the 1-yr TC at $56k (+16%, one source).
  - **LR2s keep moving dirty:** 113 LR2s switched from clean to dirty in Jan–Aug 2026 against 67 in all of 2025 (Argus, 15 Oct).
  - **New Bear supply leg:** OFAC licences for sanctioned tankers (mainly old VLCCs East of Suez; small product effect).
- **Fleet register (baseline, carried from 10 Oct):** Aframax/LR2 orderbook 17.8% with 22% of the fleet ≥ 20 years; LR1 orderbook ~15%; MR2 ~15% plus ~120 MR2 ordered since Feb, including **Hafnia's own 10**; product orderbook > 50% delivering 2028 or later; MR newbuild $52.5m with 2028–29 slots open.
- **Oil Market BBB** (through the shipping baseline only): 24 Oct re-run kept every path and mid-cycle value unchanged (Brent Base 2027 88; diesel crack 70 / 48 / 33). New in the picture: ME oil incl. alternatives > 24 mb/d, the strait ~14 mb/d incl. Gulf of Oman transfers, ~40% of Gulf crude bypassing Hormuz, escalation against Saudi Arabia. Carried from 17 Oct: ME products 1.9 mb/d vs 4.7 pre-war (IEA Sep); Russian diesel exports restarted; China's product loadings slowing.

## Common assumptions (all scenarios)

| Item | Value | Source |
|---|---|---|
| Fleet days | Owned 87 + TC-in (LR1 2 to Jul-27; MR 8.1 / 8.9 in H2-26, 5.8 avg 2027, 2 in 2028, 1 in 2029) + newbuilds (2 in Q3-28, 2 in Q4-28, 6 through 2029); utilisation 97% from 2027 | Coverage table and TC-in days `[F]`; schedule `[A]` |
| Opex incl. technical management | $9.0k/calendar day (2026), +3% a year → $9.83k (2029) | Q2 $8,981 `[F]`; inflation `[A]` |
| G&A / fee business / charter hire (non-lease) | $23.0m a quarter +3% a year / +$8.8m a quarter / $35m (2026) → $25m (2027) → $11m a year | Q2 `[F]`; TC-in expiries `[F/A]` |
| TORM dividends | Q3-26 $34.1m (14.2m shares × $2.40 `[F]`); then DPS = 0.008 × Hafnia's own quarterly net profit (prior quarter) × 20.38m shares | Ratio fitted to Q1–Q2 2026 `[A]` |
| D&A | $47m a quarter (2026), $182m (2027), $172m (2028), $164m (2029), plus $1.9m a year per newbuild | Q2 $47.2m `[F]`; ROU roll-off `[A]` |
| Net finance cost | 5.0% on average net debt + $8m a year | Q2 $11.8m `[F]`; 4.8% bank rate `[F]` |
| Tax | $6m a year (Singapore tonnage regime; no rate-linked cash tax, so the reversion tail is taken pre-tax) | Q2 $1.4m `[F]` |
| Maintenance capex (drydock, upgrades) | Q3 $25m, Q4 $22m, then $70m a year | H1-26 PP&E purchases $41.3m with 571 off-hire days `[F]` |
| Debt amortisation | Q3/Q4-26 $12.2m each, 2027 $33.6m, 2028 $18.6m, 2029 $16.6m; bullets refinanced. Net-debt neutral; the payout policy is on net profit, not FCF after debt service | Note 7 `[F]`; split `[A]` |
| Newbuild capex | $520m: Q3-26 30, Q4-26 50, 2027 100, 2028 110, 2029 230; funded from cash and RCFs | Q2 deck `[E/A]`; commitments $503.6m `[F]` |
| JV (50% share) | Vista: 2 LR2-eq on TC $25.9k to end-2027, 3 LR1-eq mostly open; Ecomar: 2 MR-eq on TC $24.5k to 2029 `[A]`; JV opex $9.5k; JV debt share $194m at 6%; JV cash retained to repay JV debt | Coverage table, note 7 `[F]`; terms `[A]` |
| Dividend | Payout by Hafnia's LTV rule on quarterly net profit; from 2027 LTV on the fully committed basis (TORM at the lower of cost $514m and market); paid the quarter after | Policy `[F]` |
| Net working capital (incl. pool cash) | $404m, held constant | 30 Jun balance sheet `[F]`; constant `[A]` |
| Shares | 542.2m; no buybacks or further issues | `[F]` / `[A]` |

## Period tables ($m unless stated; NOK per share at 542.2m shares and USD/NOK 9.340)

### Base (decision case)

| | Q3-26 | Q4-26 | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|
| TCE income | 293 | 443 | 414 | 302 | 250 | 256 | 839 | 795 |
| TCE $/day (k) | 33.7 | 50.4 | 49.1 | 35.9 | 30.2 | 31.5 | 26.2 | 23.6 |
| Booked share | 80% | 26% | 17% | 17% | 17% | 17% | 2% | 0% |
| Adj. EBITDA | 232 | 371 | 366 | 250 | 180 | 178 | 504 | 410 |
| Net profit | 191 | 329 | 322 | 201 | 127 | 125 | 306 | 203 |
| Maintenance FCF ($m / NOK/share) | 196 / 3.38 | 337 / 5.81 | 339 / 5.84 | 224 / 3.85 | 152 / 2.62 | 150 / 2.58 | 389 / 6.69 | 291 / 5.02 |
| Debt amortisation ($m) | 12.2 | 12.2 | 8.4 | 8.4 | 8.4 | 8.4 | 18.6 | 16.6 |
| FCF after debt service ($m / NOK/share) | 184 / 3.17 | 325 / 5.60 | 331 / 5.70 | 215 / 3.71 | 144 / 2.47 | 141 / 2.43 | 370 / 6.37 | 275 / 4.73 |
| Newbuild capex (growth) | 30 | 50 | 25 | 25 | 25 | 25 | 110 | 230 |
| Dividend declared ($m / NOK/share) | 172 / 2.97 | 296 / 5.10 | 290 / 5.00 | 181 / 3.12 | 115 / 1.98 | 113 / 1.94 | 275 / 4.74 | 183 / 3.14 |
| Net debt end ($m / NOK/share) | 614 / 10.6 | 470 / 8.1 | 452 / 7.8 | 543 / 9.4 | 598 / 10.3 | 588 / 10.1 | 628 / 10.8 | 772 / 13.3 |
| Net LTV (Hafnia definition) / payout | 12% / 90% | 9% / 90% | 16% / 90% | 18% / 90% | 19% / 90% | 18% / 90% | 18% / 90% | 18% / 90% |

2027 full year: TCE $36.7k/day, EBITDA $974m, net profit $777m (EPS $1.43, P/E 7.3x), dividends declared NOK 12.04/share (12.3% yield). The fleet then earns $26.2k/day in 2028 and $23.6k/day in 2029.

### Bear

Booked share, debt amortisation and newbuild capex equal Base and are not repeated.

| | Q3-26 | Q4-26 | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|
| TCE $/day (k) | 33.7 | 50.4 | 29.8 | 23.2 | 21.0 | 21.1 | 20.2 | 17.8 |
| Adj. EBITDA | 232 | 371 | 203 | 117 | 86 | 81 | 272 | 186 |
| Net profit | 191 | 329 | 152 | 62 | 30 | 24 | 54 | −43 |
| Maintenance FCF ($m / NOK/share) | 196 / 3.38 | 337 / 5.81 | 176 / 3.03 | 88 / 1.52 | 57 / 0.98 | 51 / 0.89 | 152 / 2.62 | 63 / 1.09 |
| FCF after debt service ($m / NOK/share) | 184 / 3.17 | 325 / 5.60 | 168 / 2.89 | 80 / 1.38 | 48 / 0.83 | 43 / 0.74 | 133 / 2.30 | 47 / 0.80 |
| Dividend declared ($m / NOK/share) | 172 / 2.97 | 296 / 5.10 | 137 / 2.36 | 50 / 0.86 | 24 / 0.41 | 19 / 0.33 | 43 / 0.75 | 0 / 0.00 |
| Net debt end ($m / NOK/share) | 614 / 10.6 | 470 / 8.1 | 615 / 10.6 | 689 / 11.9 | 706 / 12.2 | 704 / 12.1 | 713 / 12.3 | 891 / 15.4 |
| Net LTV / payout | 12% / 90% | 9% / 90% | 20% / 90% | 22% / 80% | 22% / 80% | 23% / 80% | 24% / 80% | 30% / 80% (loss: 0) |

### Bull

Booked share, debt amortisation and newbuild capex equal Base and are not repeated.

| | Q3-26 | Q4-26 | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|
| TCE $/day (k) | 33.7 | 50.4 | 85.0 | 62.6 | 52.6 | 49.5 | 37.2 | 30.5 |
| Adj. EBITDA | 232 | 371 | 668 | 525 | 402 | 356 | 921 | 686 |
| Net profit | 191 | 329 | 644 | 494 | 365 | 316 | 780 | 517 |
| Maintenance FCF ($m / NOK/share) | 196 / 3.38 | 337 / 5.81 | 641 / 11.05 | 502 / 8.65 | 378 / 6.51 | 331 / 5.69 | 815 / 14.04 | 574 / 9.88 |
| FCF after debt service ($m / NOK/share) | 184 / 3.17 | 325 / 5.60 | 633 / 10.90 | 494 / 8.51 | 370 / 6.37 | 322 / 5.55 | 796 / 13.72 | 557 / 9.59 |
| Dividend declared ($m / NOK/share) | 172 / 2.97 | 296 / 5.10 | 579 / 9.98 | 444 / 7.65 | 329 / 5.66 | 284 / 4.90 | 702 / 12.09 | 465 / 8.01 |
| Net debt end ($m / NOK/share) | 614 / 10.6 | 470 / 8.1 | 150 / 2.6 | 252 / 4.3 | 343 / 5.9 | 366 / 6.3 | 471 / 8.1 | 651 / 11.2 |
| Net LTV / payout | 12% / 90% | 9% / 90% | 10% / 90% | 11% / 90% | 13% / 90% | 12% / 90% | 12% / 90% | 11% / 90% |

### Year-end path per share (NOK; D_t = dividends paid in the period)

V_t is NAV: owned fleet and JV vessels at Hafnia's broker marks, aged, gliding linearly from today's market marks at 31 Dec 2026 (identical in all scenarios) to the scenario's mid-cycle marks at exit, plus the reversion tail at T; newbuilds at cost until delivery; TORM stake gliding from today's price to its scenario exit value; less net debt.

| | | Stub (to 31 Dec 26) | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| **Base** | D_t | 2.97 | 15.19 | 5.49 | 3.54 |
| | V_t | 90.3 | 82.0 | 75.4 | **69.6** |
| | r_t | −4.8% (mark vs price, not annualised) | +7.6% | −1.3% | −3.0% |
| | IRR to t | n.m. (0.19 yr) | +2.1% | +0.6% | **−0.5%** |
| **Bear** | D_t | 2.97 | 8.72 | 0.88 | 0.20 |
| | V_t | 90.3 | 71.8 | 57.5 | **42.0** |
| | r_t | −4.8% | −10.9% | −18.6% | −26.7% |
| | IRR to t | n.m. | −13.7% | −15.9% | **−19.4%** |
| **Bull** | D_t | 2.97 | 28.39 | 13.95 | 9.01 |
| | V_t | 90.3 | 96.8 | 99.9 | **105.7** |
| | r_t | −4.8% | +38.5% | +17.7% | +14.9% |
| | IRR to t | n.m. | +28.7% | +24.7% | **+22.3%** |

Reading:
- **Base:** the price is now 10% above today's market NAV (NOK 89.0). 2027's dividends (NOK 15.2 paid, incl. the large Q4-26 dividend in March) give one good year (r_t +7.6%), but from NOK 98.00 the IRR to end-2027 is only +2.1%. After that, ageing (~NOK 3 a year) and the fade to mid-cycle marks eat the yield.
- **Bear:** the loss is spread over the glide to Bear mid-cycle values and dividends that dry up.
- **Bull:** the yield carries the return; values rise towards Bull mid-cycle marks.

## V_T bridge, Base ($m and NOK/share)

| Step | $m | NOK/share |
|---|---|---|
| P → NAV_0 (re-rating needed: P/NAV_0 1.31) | — | 98.00 → 75.0 |
| **NAV_0** at Base mid-cycle marks (ages at 24 Oct): owned fleet 3,419 + newbuild instalments 30 + JV 267 + TORM 674 + options 160 + other 13 + NWC 404 − net debt 614 | **4,353** | **75.0** |
| + Value created by growth capex (newbuilds worth 497 at T − 30 in NAV_0 − 490 paid in the horizon) | −23 | −0.4 |
| − Ageing of the owned fleet at mid-cycle marks (3,419 → 2,859) | −560 | −9.6 |
| − Purchase options (in-the-money amount at aged marks, 160 → 106) | −55 | −0.9 |
| ± JV (vessel ageing −43, JV net debt paid down from retained JV cash +162, H&A cash moved to Hafnia −28) | +91 | +1.6 |
| − TORM stake (TORM fleet ageing at mid-cycle, 674 → 542) | −133 | −2.3 |
| ± Firm-contract premium roll-off | ~0 | ~0 |
| **+ Reversion tail (exit consistency; LR2 and LR1 end 2029 above mid-cycle)** | **+35** | **+0.6** |
| + Retained cash (Σ Maintenance FCF − dividends paid + H&A, = −Δ net debt excl. newbuild capex) | +332 | +5.7 |
| **= V_T (31 Dec 2029): assets 4,812 − net debt 772** | **4,040** | **69.6** |

**Exit asset values ($m) `[A]`:**

| Asset | Bear | Base | Bull | Method |
|---|---|---|---|---|
| Owned fleet (87 vessels) | 2,008 | 2,859 | 3,934 | Broker $3,739m by segment × mid-cycle factor × age factor |
| 10 MR newbuilds | 346 | 497 | 691 | 5-yr mid-cycle MR × 1.08 (age ~1) |
| JV, net of JV debt | 194 | 358 | 631 | JV vessels by the same method − JV net debt |
| TORM stake (20.38m shares) | 361 | 542 | 768 | TORM fleet $4,056m (30 Jun) × mid-cycle factor × ageing 0.82 − TORM net debt $319m, on 102.4m shares → $17.7 / $26.6 / $37.7 vs $39.89 today (23 Oct) |
| TC-in purchase options | 2 | 106 | 249 | (aged vessel value at marks − strike) for 7 MR + 2 LR1 |
| Reversion tail | 0 | 35 | 98 | Exit-consistency table below |
| Other investments / NWC | 13 / 404 | 13 / 404 | 13 / 404 | Held |
| Net debt at exit | −891 | −772 | −651 | Model |
| **V_T ($m / NOK per share)** | **2,436 / 42.0** | **4,040 / 69.6** | **6,136 / 105.7** | |

**Exit-consistency table (Step 3).** Gap = (2029 rate − mid-cycle rate) ÷ mid-cycle rate, on the scenario's own values; open days are Hafnia's consolidated plus JV share as in 2029 (97% utilisation, Hafnia factor 1.0, no firm cover after 2029). Material = |gap| > 10%. Tail = gap × open days × 0.903 (2/3 ÷ 1.08 + 1/3 ÷ 1.08²), pre-tax (tonnage tax).

| Row | Scenario | 2029 rate ($k) | Mid-cycle ($k) | Gap | Open days a year | Treatment | Tail ($m / NOK per share) |
|---|---|---|---|---|---|---|---|
| LR2 (6 owned + 2 JV-eq) | Bear | 25 | 24 | +4% | 2,832 | Not material | 0 / 0 |
| LR2 | **Base** | 35 | 30 | **+17%** | 2,832 | **Reversion tail** | **12.8 / 0.22** |
| LR2 | Bull | 55 | 37 | **+49%** | 2,832 | **Reversion tail** | **46.0 / 0.79** |
| LR1 (20 owned + 3 JV-eq) | Bear | 20 | 20 | 0% | 8,143 | Not material | 0 / 0 |
| LR1 | **Base** | 28 | 25 | **+12%** | 8,143 | **Reversion tail** | **22.1 / 0.38** |
| LR1 | Bull | 38 | 31 | **+23%** | 8,143 | **Reversion tail** | **51.5 / 0.89** |
| MR (41 owned + 9.25 newbuild-eq + 1 TC-in, Q4-29 run-rate) | Bear / Base / Bull | 17 / 22 / 27 | 17 / 21 / 26 | 0% / +5% / +4% | 18,145 | Not material | 0 |
| Handy (20) | Bear / Base / Bull | 15.3 / 19.8 / 24.3 | 15.3 / 18.9 / 23.4 | 0% / +5% / +4% | 7,081 | Not material | 0 |
| **Total** | Bear / **Base** / Bull | | | | | | 0 / **34.9 / 0.60** / 97.5 / 1.68 |

- **Why the tail and not a named reason:** the baseline names no cause that brings LR2 or LR1 down to mid-cycle within a year of exit.
  - The asset market prices both above mid-cycle (asset-implied TCE LR2 34 vs 30, LR1 27 vs 25; Market check anchors). A buyer at exit would not pay only the mid-cycle mark, so the market-consistency reason fails.
  - The Aframax/LR2 deliveries after the window are small (~16 vessels for 2030+ in the register), which argues for the 2029 level holding rather than falling.
  - For LR1, the baseline says the 2029 premium "weakened slightly" (orderbook ~15%, paper about at Base) but keeps the row. That is a reason to watch the row, not a sourced reversion cause.
- **The other treatment as a sensitivity (no tail, i.e. assume an immediate fall to mid-cycle):** Base IRR −0.7%, P_k 72.2 (−0.4); Bull 21.8%, P_k 119.5. Bear unchanged.
- The 24 Oct baseline gives no 2030 view for the product rows either, so the treatment stands.
- The tail is zero in the structural runs (2029 at mid-cycle there), so it sits in the cyclical part of IRR_T.
- **No exit multiple** is used; the IAF ceiling is not used as an exit. Cross-check: Base exit fleet value (owned + newbuilds + options ≈ $3.46bn) is ~10x Base mid-cycle EBITDA ex-TORM of $330m, generous rather than harsh, because Hafnia's costs (opex $9.8k + G&A ~$2.9k a day) are above the baseline's parity costs.

### Exit criteria check (iaf-valuation 2026-10-18.2; v6 19 Oct, NOK figures re-marked 24 Oct)

The skill now states one exit principle (V_T = what a market buyer pays for a continuing business, on mid-cycle earnings, at the market's required return), adds backlog-at-exit rules, an exit cross-check against Equity BBB and a NOK path for Bear and Bull. Hafnia was checked item by item on the v5 model (v6); the USD ratios are unchanged in v7, and the NOK figures below are at the 23 Oct price and FX.

| Criterion (Step 3 / FX rule) | Hafnia | Result |
|---|---|---|
| **Backlog at exit** (firm today: full term; signed in the scenario: ≤ 2 years after exit, at most the BBB's typical term) | No contract runs past 31 Dec 2029. Owned LR2 TC-outs (74% of 2027 at $30.7k) are assumed to run into mid-2028 `[A]`; JV LR2 TCs end in 2027; Ecomar MR TCs are assumed to end in 2029 `[A]`. No scenario signs new term cover | **No contract premium** in V_T or NAV_0. If the Ecomar TCs run past 2029, the premium ($24.5k vs MR mid-cycle $21k on 2 MR-equivalents ≈ $2.3m a year) is < NOK 0.1/share |
| **Exit consistency on open days after exit** (tail only on days not under backlog) | All LR2 and LR1 days are open in 2030–31, so the tail runs on the full 2029 open days | **Tail unchanged in $:** Base +NOK 0.60, Bull +NOK 1.68, Bear 0 |
| **Holding-company G&A not deducted in NAV** | NAV_0, interim V_t and V_T are marks less net debt; no G&A is deducted. Within the window all G&A ($92–100m a year) is in the cash flows. Split: holdco ~$15m a year `[A]` (board, listing, corporate finance); the rest runs the platform (commercial, technical, pools) | **Complies.** The operating part is not in the market marks either (see the overhead sensitivity below) |
| **Exit cross-check vs Equity BBB (Oslo)** | Table below | **P/B inside the Oslo band; P/E far above; buyer's return below the index** (Base and Bull) |
| **NOK path for Bear and Bull** (USD/NOK on the Equity BBB path) | Bear USD/NOK +12% (2027), +9% (2028–29); Bull −3%; applied as moves from today's spot | Bear IRR −16.8% (P_k 45.0) vs −19.4% at spot; Bull 20.7% (P_k 117.2) vs 22.3%. A weaker krone cushions Bear by ~2.6 pp; the decision stays at spot |

**Exit cross-check (V_T against the equity market).** Exit P/E uses FCF_normalised before holdco G&A (the NAV basis) and, as a second read, mid-cycle accounting net profit. Book is rolled forward from 30 Jun ($2,650m + placement $289m − Q2 dividend $250m + Σ net profit − Σ dividends declared to Q3-29, TORM at its exit value). Buyer's implied return = 8% asset rate on the marked assets less 5% on net debt, on equity at P/NAV = 1.

| | Bear | **Base** | Bull | Oslo (Equity BBB) Bear / Base / Bull |
|---|---|---|---|---|
| V_T ($m / NOK per share) | 2,436 / 42.0 | **4,040 / 69.6** | 6,136 / 105.7 | — |
| FCF_normalised before holdco G&A ($m) | −63 | **47** | 191 | — |
| Exit P/E on FCF_normalised (pre-holdco) | negative | **~87x** | ~32x | 10.5 / 11.5 / 12.5 |
| Exit P/E on mid-cycle accounting net profit ($m: −63 / 104 / 319) | negative | **~39x** | ~19x | 10.5 / 11.5 / 12.5 |
| Book equity at exit ($m) / exit P/B | 2,535 / 0.96 | **2,885 / 1.40** | 3,365 / 1.82 | 1.48 / 1.75 / 1.97 (band 1.5–2.1) |
| Buyer's implied return at exit (equity) | 9.1% | **8.6%** | 8.3% | Mid-cycle return 8.2 / 9.1 / 9.4% |

- **Reading:**
  - **P/B is fine:** 1.40 in Base, below the Oslo exit P/B. Hafnia's book carries ships at depreciated cost ($2.25bn against $3.7bn broker value at 30 Jun), so a P/B above 1 is normal for a tanker owner at NAV.
  - **P/E is far outside the index**, and it needs a stated reason (skill). The reason: at mid-cycle the baseline's rates sit at about newbuild parity, which pays the market's 8% only before a full owner's overhead. Hafnia's opex incl. technical management ($9.8k/day in 2029) is above the baseline's value opex (MR $8.0k, LR1 $8.5k, LR2 $9.5k), and it carries ~$85m a year of operating G&A. So its own mid-cycle earnings are thin, while the marks are market prices any buyer of a ship pays. The NAV exit is still the IAF default for Track B, because the marks are the most independent exit. Listed product-tanker owners trade near NAV (TORM ~1.05x its updated NAV; Hafnia 1.10x today), so a market buyer of the share does pay NAV today. **But the P/E says the exit is generous to Hafnia, not conservative.**
  - **Buyer's return:** in Base (8.6% vs 9.1%) and Bull (8.3% vs 9.4%) the buyer's implied return is below Oslo's mid-cycle return with no stated quality or contract reason. So the skill's sensitivity applies: re-discount the exit marks at the index return (asset rate 8.44% Base, 8.98% Bull over ~11 years of remaining life → marks × 0.979 / 0.954). In Bear it is above the index (9.1% vs 8.2%), so no sensitivity is needed.

| Exit sensitivity (decision unchanged) | Bear | **Base** | Bull |
|---|---|---|---|
| Decision (NAV exit at 8% marks, with tail) | −19.4% / 41.2 | **−0.5% / 72.6** | +22.3% / 120.7 |
| Exit marks re-discounted at the Oslo mid-cycle return | n/a (buyer's return above index) | **−1.0% / 71.6** | +21.0% / 117.7 |
| Exit NAV less capitalised operating overhead ($85m a year over 11 years at 8% = $607m, NOK 10.5/share) `[A]` | −26.1% / 33.9 | **−4.8% / 65.3** | +19.2% / 113.4 |
| NOK path (Equity BBB), reported beside spot | −16.8% / 45.0 | = spot (Base path is flat) | +20.7% / 117.2 |

- The overhead line is a bound, not the method: market marks embed some owner cost, and the skill keeps holdco G&A out of NAV. It shows how much the NAV convention could flatter a high-overhead owner: ~NOK 7 on P_k.
- **Conclusion of the check:** every exit criterion is met or flagged with its sensitivity. None of them would move the verdict towards a pass. The most generous reading (decision case) already fails by 26%.

## Growth capex test (Step 4)

| Item | Capex in horizon | Evidence for ROIC_g | ROIC_g (pre-tax, unlevered) | vs k = 12% | Value at T vs capex |
|---|---|---|---|---|---|
| **10 MR newbuilds** (2028–29) | $490m after 30 Sep (of $520m) | No charters attached. Base mid-cycle MR $21k + $1.5k eco premium − $8.5k opex `[A]` → ~$5.0m EBITDA a year on $52m. Oil Shipping BBB: MR newbuild parity $21k at 8%; at 12% a newbuild needs ~$27–28k. Fleet register: price $52.5m with 2028–29 slots still open, so the order is at market; > 50% of the product orderbook delivers 2028 or later; MR2 contracting is the heaviest of the product segments (~120 since Feb, Hafnia's 10 among them). MR is the one product row with no exit gap (2029 22 vs mid-cycle 21) | **~9.6%** (Bull mid-cycle $26k → ~13%) | **Below k** in Base; ≈ k only in Bull | NAV at T $497m vs $520m paid: **−$23m** (perpetuity formula ≈ **−$104m**). Today's NAV impact ≈ 0 (contract ≈ market price) |
| **TORM shares** (6.2m bought in Sep for $203m, funded by the $289m placement) | Before the valuation date | Bought at $32.25/$34.00, marked at $39.89 today (23 Oct). TORM NAV $36.50 (30 Jun); TORM raised FY26 guidance on 12 Oct. Base exit $26.6/share plus dividends | Base: below k | **Below k** in Base; Bull ≈ k | Strategic (consolidation) value not modelled. Hafnia is now TORM's largest holder |
| **Placement** (35.5m new shares at NOK 80) | — | Issued at ~0.90× today's market NAV/share (NOK 89.0) | — | — | **≈ −NOK 0.6/share** dilution of NAV `[A]` |
| **TC-in purchase options** (exercise) | Strike only, if exercised | Strike $29.1m (MR) / $38.3m (LR1) vs today's values | In the money ($191m at 30 Jun `[F]`; ~$220m at today's marks `[A]`) | Above k (discounted entry) | Kept as an option value line |

- **Funding:** newbuilds and TORM come from cash, RCFs and the placement; dividends are on net profit, so growth is funded by the 10% retention, RCF draws and new shares.
- **Per share:** 7.1% dilution in Sep funded a financial stake whose Base return is below k. It does not pass the per-share test unless a TORM transaction creates value that is not in this model.
- **Reading:** growth spending in this window is **not accretive in Base**; the newbuilds are ordered at market prices into the 2028–29 product delivery peak, where the baseline keeps MR rates at newbuild parity.
- **Fleet renewal:** Hafnia's owned fleet averages 9.7 years; its oldest ships (three 2010 LR1s) turn 20 in 2030, just after exit. The age factor (floor 0.15) and the fleet-renewal charge in Rule 3 carry the wear.

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (exit 31 Dec 2029) | −19.4% | **−0.5%** | +22.3% |
| d / g / c | 4.1% / −23.4% / −0.1 pp | **8.7% / −10.2% / +1.0 pp** | 17.4% / +2.4% / +2.5 pp |
| g: re-rating / NAV growth (P/NAV_0) | −19.4% / −4.9% (1.99) | **−8.0% / −2.3% (1.31)** | +2.9% / −0.5% (0.91) |
| Structural IRR / cyclical (pp; Δd, Δg) | −21.6% / +2.2 (+1.2, +0.8) | **−6.1% / +5.7 (+4.1, +0.8)** | +8.4% / +13.9 (+10.0, +1.8) |
| ΣD_t / V_T (NOK) | 12.8 / 42.0 | **27.2 / 69.6** | 54.3 / 105.7 |
| **P_k (hurdle price) / margin of safety** | 41.2 / −58% | **72.6 / −25.9%** | 120.7 / +23.1% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | negative FCF vs negative | **176x vs −0.3x** (25.6x before the renewal charge) | 32.3x vs 15.5x |
| Capital preserved? ΣD_t + V_T vs P = 98.00 | **No: 54.7, −44%** | **No: 96.8, −1% nominal over 3.2 years** | Yes: 160.0, +63% |

**Notes on the results:**
- **Structural and cyclical:** each scenario is re-run with every open day from 1 Jan 2027 (Hafnia, JV LR1s, JV LR2s from 2028) at that scenario's own mid-cycle rate. The stub, the 2027 TC-out days and exit asset values are unchanged; the reversion tail is zero; dividends and net debt follow the cash flows.
  - Base: the cycle above mid-cycle adds +5.7 pp, mostly through d (2027 dividends); +0.2 pp of it is the tail (NOK 0.6/share; v6 wrote "+0.6 pp", which was the per-share amount).
  - Bear and Bull are mainly **mid-cycle shifts**: Bear structural −21.6% vs Base structural −6.1% (−15.5 pp); Bull +8.4% (+14.5 pp). The Bull rate path adds a further +13.9 pp.
- **FCF_normalised (Base):**
  - Full fleet incl. the 10 newbuilds at Base mid-cycle rates gives TCE $754m.
  - Less opex $348m, G&A $100m and charter hire $11m, plus fees $35m and TORM dividends $15m → EBITDA $345m.
  - Less interest $47m (on exit net debt), tax $6m and maintenance capex $70m → maintenance FCF $222m (NOK 3.82/share).
  - Less the fleet-renewal charge $190m (ageing of owned and JV vessels at mid-cycle, $607m ÷ T) → **$32m = NOK 0.56/share → 176x**.
  - The same build at Bear marks is negative; Bull gives NOK 3.03 → 32x.
  - The Base ceiling is negative because Base IRR_T is now below zero.
- **Scenario-weighted reference (convention, 25/50/25 on the levels D_t and V_T):** IRR 1.6%, P_k NOK 76.8. Not the decision figure.
- **Bull already priced:** (98.00 − 72.6) / (120.7 − 72.6) = **53%**.
- **NOK path (Equity BBB), beside spot:** Bear −16.8% (P_k 45.0), Bull +20.7% (P_k 117.2). Base equals spot (flat path). The decision stays at spot FX.
- **Market check (not an input):** BTIG target $12 (14 Sep, reiterated; Zacks 24 Oct) ≈ NOK 112 at today's FX; Yahoo mean target $11.5 (2 analysts, $11–12) ≈ NOK 107. Both sit between the Base and Bull hurdles.

**Bear — balance-sheet survival:**
- EBITDA falls to $186m in 2029 and net profit turns negative (−$43m); dividends stop from Q1-29.
- Net debt rises from $470m (end-2026) to $891m, mainly from newbuild capex ($490m). Fully committed LTV reaches ~30% at Bear values.
- Liquidity ($631m at 30 Jun plus the undrawn $330m facility) covers the newbuild bill. Maturities are 2027 ($100m RCF, refinanced), 2029 and 2032–33. Covenant levels were not read `[?]`; at ~30% LTV the headroom against typical tanker value covenants is wide.
- The Bear supply leg (US approval of sanctioned tankers for mainstream trade, policy since 19 Oct) mainly hits old VLCCs and crude values; for product tankers its effect is small (baseline).
- **Survivable; the loss is capital (−44% over 3.2 years), not solvency.**

### Sensitivity (Base, unless stated)

| Change | IRR_T | P_k (NOK) |
|---|---|---|
| **No reversion tail (immediate fall to mid-cycle at exit)** | **−0.7%** | **72.2** |
| Exit marks re-discounted at the Oslo mid-cycle return (9.1%; v6 exit cross-check) | −1.0% | 71.6 |
| Exit NAV less capitalised operating overhead (−NOK 10.5/share; v6, a bound) | −4.8% | 65.3 |
| Hafnia TCE factor 0.9 / 1.1 on open days 2027+ | −2.7% / +1.8% | 68.1 / 77.1 |
| Open-day rates +12% (≈ +$3k/day) 2027+ | +2.2% | 78.0 |
| Stub factor 0.6 / 1.0 (Q4-26 open days) | −1.3% / +0.3% | 70.7 / 74.5 |
| Q4-26 at the Yahoo consensus TCE ($378m; stub factor ~0.67) | −1.0% | 71.3 |
| Exit fleet + newbuild values × 0.8 / 0.9 | −5.3% / −2.8% | 64.5 / 68.6 |
| Exit fleet + newbuild values × 1.1 / 1.2 | +1.8% / +3.9% | 76.6 / 80.6 |
| TORM stake at today's price at exit ($39.89; no mid-cycle re-mark) | +1.3% | 75.8 |
| Base cash flows with Bear / Bull exit marks | −11.8% / **+10.9%** | 55.2 / **95.5** |
| Payout fixed at 90% | −0.5% | 72.6 |
| k = 10% / 13% / 14% | — | 75.9 / 71.0 / 69.5 |
| **V_T needed for IRR 12%** | NOK 106.1 vs 69.6 (× 1.52) | — |

- Each 10% on exit asset values moves the IRR by ~2.3 pp; each 10% on open-day rates by ~2.3 pp.
- **No single input now closes the gap.** At NOK 94.85 (v6) the Bull exit marks did on their own (12.7%); at NOK 98.00 they give 10.9% and P_k 95.5, just below P. Every other single input leaves Base well below k.

## Verdict

- **Fails.** Base IRR_T is **−0.5%** against k = 12%. P = NOK 98.00 is 35% above P_k = NOK 72.6, so the **margin of safety is −25.9%**. Rule 3 fails too (176x vs a negative ceiling; 25.6x even before the renewal charge). Base no longer returns the entry price in nominal terms (ΣD_t + V_T = NOK 96.8).
- **Bear breaks the thesis:** about 44% of capital is lost (IRR −19.4%). The balance sheet survives comfortably.
- **Bull** returns ~22% a year (P_k NOK 120.7); the price reflects 53% of the way from Base to Bull.
- **Why Base fails:**
  - **The price is above every Base NAV:** P/NAV 1.10 on today's marks and 1.31 on Base mid-cycle marks. Base needs a −8.0% a year re-rating to reach NAV_0.
  - **Cash returns are front-loaded and short:** NOK 27.2 of dividends to 2029 (d = 8.7%), of which NOK 18.2 come by end-2027. After 2027 the Base rows fall to or near newbuild parity, and Hafnia earns $306m in 2028 and $203m in 2029.
  - **The NAV erodes:** ageing ~NOK 10/share, TORM ~NOK 2, options ~NOK 1; the newbuilds add nothing at Base returns. Retained cash (+NOK 5.7) and the tail (+NOK 0.6) only partly offset this.
  - **Growth spending is below k:** MR newbuilds at ~9.6% ROIC, and the TORM stake funded by a 7% share issue.
- **What would flip the verdict:**
  - Up: Bull-type mid-cycle values at exit together with something more (on their own 10.9% at NOK 98.00, P_k 95.5); a durable Bull rate path; a TORM merger at terms that create value per Hafnia share; or buybacks below NAV instead of newbuilds.
  - Down: Bear catalysts (Iran–USA deal plus recession; a wide US approval of sanctioned tankers adding supply; LR2s cleaning up faster; on-time 2028–29 deliveries); Q4 cover on 18 Nov at the sell side's level (P_k −1.3).
  - The stub, the payout ratio, the tail and the Hafnia premium each move the result by ≤ 2.3 pp.

**Caveat:** this is a margin-of-safety screen, not an intrinsic valuation or a price target. P_k is the price at which the Base path returns exactly 12%.

## Tracking

| Version | Valuation date / price | What changed | Base IRR / P_k / MoS | Bear / Bull P_k |
|---|---|---|---|---|
| v1 | 5 Oct 2026 / NOK 96.70 | First analysis (Oil Shipping BBB 4 Oct) | −0.5% / 70.5 / −27.1% | 40.4 / 115.6 |
| v2 | 10 Oct 2026 / NOK 103.30 | Oil Shipping BBB 10 Oct (stub and 2027 higher); price +6.8%; TORM re-based on its reported NAV; LR1/MR values up | −1.3% / 74.7 / −27.7% | 43.0 / 123.0 |
| v3 | 10 Oct 2026 / NOK 103.30 | Fleet register: LR2 Base 2029 31 → 35 | −1.3% / 74.9 / −27.5% | 43.0 / 123.0 |
| v4 | 10 Oct 2026 / NOK 103.30 | Product re-test: LR2 2028 44 → 38; LR1 2028 33 → 30, 2029 25 → 28; seasonal Q4-27 | −1.4% / 74.6 / −27.8% | 43.0 / 123.0 |
| v5 | 17 Oct 2026 / NOK 94.85 | No new quarter reported. Price −8.2%; USD/NOK 9.581 → 9.443; TRMD $39.94 → $38.20; Oil Shipping BBB 17 Oct (LR1 stub 150 → 120; nothing else for Hafnia); IAF exit-consistency test (reversion tail Base +NOK 0.61, Bull +NOK 1.70) | +1.2% / 73.2 / −22.8% | 41.6 / 121.7 |
| v6 | 17 Oct 2026 / NOK 94.85 (check on 19 Oct) | Exit criteria under IAF 2026-10-18.2: no backlog at exit, tail unchanged, holdco G&A not in NAV, exit cross-check vs Oslo (P/B 1.40 inside the band; P/E ~39x far above; buyer's return 8.6% < 9.1%), NOK path for Bear/Bull. Decision figures unchanged | +1.2% / 73.2 / −22.8% (re-discounted at 9.1%: 0.6% / 72.2) | 41.6 / 121.7 |
| **v7** | **24 Oct 2026 / NOK 98.00** | No new quarter and no company news. Oil Shipping BBB 24 Oct: nothing for Hafnia (product stubs, rows, mid-cycle unchanged; LR1 5-yr mark now 67 → 68, NAV today only). Market re-mark: price +3.3%, USD/NOK 9.443 → 9.340, TRMD $38.20 → $39.89, valuation date +7 days | **−0.5% / 72.6 / −25.9%** | 41.2 / 120.7 |

- **v7 vs v6, Base:**
  - USD cash flows, USD V_T ($4,040m) and the model are unchanged; the shipping baseline moved nothing Hafnia reads into the decision.
  - P_k NOK 73.2 → 72.6: FX −0.8 (every NOK figure −1.1%), one week less discounting +0.2.
  - IRR +1.2% → −0.5%: the price in USD rose 4.5% ($10.04 → $10.49) against unchanged USD cash flows.
  - **The margin of safety falls from −22.8% to −25.9%, all from the market (price up, krone firmer).** Base capital preservation tips from +3% to −1% nominal, and the Bull-exit sensitivity no longer clears.
- **v5 vs v4, Base:**
  - Q4-26 EBITDA $413m → $371m (LR1 open Q4 days 0.8 × 150 → 0.8 × 120).
  - 2027–29 USD cash flows unchanged except the JV's Q4 LR1 days; FX cuts every NOK figure by 1.4%.
  - V_T NOK 70.9 → 70.4: FX −1.0, lower Q4 cash net of the lower dividend −0.1, reversion tail +0.6.
  - **P_k NOK 74.6 → 73.2 (−1.4), while the price fell NOK 8.45. The margin of safety improves from −27.8% to −22.8%, all from the price.**
- **Running ahead of or behind the Base path:** no actuals yet. TORM's guidance upgrade supports the modelled H2 (Hafnia H2/H1 EBITDA 1.24× vs TORM's implied 1.27×). The sell side (Yahoo, thin) is in line on Q3 revenue ($298m vs model $293m) but below on Q4 ($378m vs $443m). The Q3 report on 18 Nov (Q3 TCE vs $33.7k/day; Q4 cover vs $50.4k/day) is the first real test.
- Earlier version notes (v2–v4) are in the change log.

## Risks and signposts

| Signpost | Bear | Base | Bull | Now |
|---|---|---|---|---|
| Q3 report (18 Nov): Q3 TCE and Q4 cover | Q3 < $31k/day; Q4 booked < $38k | Q3 ~$33–34k; Q4 booked $42–55k | Q4 booked > $60k | Q3 80% at $30.7k (17 Aug); consensus Q4 revenue $378m vs model $443m (Yahoo, 3 estimates) |
| TORM Q3 report (4 Nov) and Q4 cover | Guidance cut | Guidance held ($1.3–1.5bn EBITDA) | Raised again | Raised on 12 Oct; no TORM news 16–23 Oct; TRMD $39.89 |
| MR 1-yr TC (Intermodal) | < $25k | $30–45k | > $50k | $45k (Intermodal 16 Oct) / $39.5k (Compass); 97–111% of Base over the charter's months |
| LR1 1-yr TC | < $30k | $35–61k | > $65k | $60k (Intermodal) / $61k (Compass): two sources ≥ $56k, but 102–104% of Base over the charter's months, so LR1 2027 stays 45 (baseline 24 Oct) |
| LR2s trading dirty (Oil Shipping BBB) | < 40% by mid-2027 (clean supply returns) | Falls below 50% during H2-27 | Stays > 60% | > 50% dirty; clean-trading LR2s −39% y/y (158 ships, Signal) |
| Gulf of Oman STS / Iran–USA after 3 Nov | Deal holding > 60 days | Contested armed normalisation | STS hub suspended, US strikes, or a Saudi export facility hit with lasting loss | ≥ 18 tankers attacked in two weeks (Kpler); IRGC claims four STS tankers hit (unverified); talks stalled; second US carrier; hub not suspended |
| US approval of sanctioned tankers (was "OFAC licences") | > 30 sanctioned VLCCs approved for mainstream trade | < 30; little product effect | — | Policy announced 19 Oct; process in development; 14–24 VLCCs realistic (Kpler, Braemar, Arrow) |
| USTR/China port fees | — | Suspension extended | Fees reinstated 10 Nov | Suspension expires 9 Nov; no notice seen (24 Oct) |
| TORM | Stake value falls with rates | Held; dividends | Transaction at value-creating terms | 19.85%, $813m; Oaktree out |
| Insider dealing | Further sales by management | — | Insider buying | CFO sold 50,000 at NOK 101.52 (9 Oct); none since (Newsweb to 23 Oct) |
| Fully committed LTV / payout | > 20% → 80% payout | 16–19% (90%) | < 13% | 13% (30 Jun, old basis) |
| Capital allocation | More newbuilds or acquisitions at market prices | 10 MRs only | Buybacks below NAV | Placement for "strategic opportunities" |

**Other risks:**
- **Governance:** BW Group control, related-party funding and a non-pre-emptive placement; the ex-CEO sits on the board with accelerated options.
- **Accounting:** the payout is on net profit including sale gains and TORM dividends; a large TORM transaction could change the LTV basis and the payout.
- **Regulation:** USTR/China port fees (9–10 Nov), IMO Net-Zero Framework, sanctions policy (US approval of sanctioned-tanker sales, 19 Oct).
- **Costs:** opex inflation above 3% a year.

## For other modules

- **Oil Shipping BBB:**
  1. **Exit consistency for products:** Base LR2 (35 vs 30) and LR1 (28 vs 25) end 2029 more than 10% above mid-cycle, and the baseline gives no reason why they fall to mid-cycle in 2030 (asset-implied TCE is above mid-cycle for both, and 2030+ Aframax/LR2 deliveries are small). IAF now adds a reversion tail. A sourced 2030 view for the product rows (deliveries, scrapping, LR2 clean/dirty) would either remove the tail or confirm it.
  2. **TORM's 12 Oct guidance upgrade** (FY26 TCE $1.7–1.9bn, EBITDA $1.3–1.5bn, citing Q4 coverage) is a product-market data point for the Q4 stub.
  3. **Handy row** still missing (convention Handy = 0.90 × MR). Open since v1.
  4. **Register gaps:** Hafnia's Q3 deck (18 Nov) normally updates the Handy–LR2/Aframax orderbook bars and the sanctioned/aged exit pool.
  5. **Product stub vs sell side (new, 24 Oct):** Yahoo consensus for Hafnia's Q4 revenue is $378m (3 estimates, $330–425m), below the $443m that the baseline stub (LR2 220, LR1 120, MR 55) gives at Hafnia's 0.8 factor. Thin data, but it points the same way as the falling TC5 Q4 paper ($190k, −3.5% w/w). Hafnia's Q4 cover on 18 Nov tests the product stub directly.
- **Oil Market BBB:** no change needed.

## Change log

- **24 Oct 2026 (v7):** update after Oil Shipping BBB 24 Oct (rev 2026-10-24.1), under iaf-valuation rev 2026-10-18.2.
  - **Change gate:** the 24 Oct baseline changed the stub method and re-marked VLCC and Aframax stubs only. LR2 220, LR1 120, MR 55, the 2027–29 rows, the Year-1 quarters, mid-cycle TCE and mid-cycle values are unchanged, so **no Hafnia input that enters IRR_T or P_k moved**. The LR1 5-yr mark now (67 → 68) moves today's NAV (+$17m owned, +$3m JV, +$2m options) and the interim marks only.
  - **Market re-mark:** price NOK 94.85 → 98.00 (23 Oct close); USD/NOK 9.443 → 9.340; TRMD $38.20 → $39.89 (NAV today only; the TORM exit value is on mid-cycle marks); valuation date 17 → 24 Oct (T 3.21 → 3.19). Every NOK per-share figure re-translated at 9.340; $m figures unchanged.
  - **Company data:** no Hafnia or TORM announcement on Newsweb 16–23 Oct; no 6-K after 13 Oct; no fleet deal, charter, dividend or insider trade. Consensus replaced: Yahoo (24 Oct) instead of the stale Bloomberg (24 Aug); thin (1 EPS estimate), below the model on Q4. Zacks ratings unchanged (BTIG $12).
  - **Result:** **fails**, unchanged. Base IRR +1.2% → −0.5%, P_k NOK 73.2 → 72.6, margin of safety −22.8% → −25.9%; Bear P_k 41.6 → 41.2; Bull P_k 121.7 → 120.7. Base capital preservation +3% → −1% nominal; Base cash flows with Bull exit marks 12.7% → 10.9% (no longer clears).
  - **Correction:** the v6 note "+0.6 pp of it is the tail" was the per-share amount (NOK 0.6); the tail adds +0.2 pp to the Base IRR.
- **19 Oct 2026 (v6):** exit-criteria check under iaf-valuation rev 2026-10-18.2 on the v5 model; no input or decision change.
  - Backlog at exit: none (no contract past 2029), so no contract premium; the reversion tail runs on all open days as before.
  - Holdco G&A: not deducted in NAV (complies); split holdco ~$15m / operating ~$85m a year `[A]`.
  - Exit cross-check vs Equity BBB (Oslo): exit P/B 0.96 / 1.40 / 1.82 (Oslo 1.48 / 1.75 / 1.97); exit P/E on FCF_normalised pre-holdco ~87x Base and on mid-cycle net profit ~39x (Oslo 11.5x), reason stated (Hafnia's cost base above the baseline's value opex; market marks independent); buyer's implied return 9.1 / 8.6 / 8.3% vs Oslo mid-cycle 8.2 / 9.1 / 9.4%.
  - Sensitivities added: marks re-discounted at the Oslo return (Base 0.6%, P_k 72.2; Bull 23.1%, 118.7); exit NAV less capitalised operating overhead (Base −3.2%, P_k 65.9).
  - NOK path (Equity BBB): Bear −15.4% (P_k 45.4), Bull 22.8% (P_k 118.2).
  - Result: **fails**, unchanged (Base IRR +1.2%, P_k NOK 73.2, margin of safety −22.8%).
- **17 Oct 2026 (v5):** update under iaf-valuation rev 2026-10-11.3 with Oil Shipping BBB and Oil Market BBB (17 Oct).
  - **New inputs:** price NOK 94.85 and USD/NOK 9.443 (16 Oct close); TRMD $38.20; LR1 stub 120; Hafnia CFO share sale (12 Oct notice); TORM guidance upgrade (12 Oct).
  - **Method:** exit-consistency test (IAF Step 3). Material gaps in Base and Bull LR2 and LR1 with no named reason in the baseline → 2-year reversion tail in V_T (Base $35m = NOK 0.61; Bull $98m = NOK 1.70); the no-tail case is a sensitivity. MR and Handy gaps are below 10%; Bear has none.
  - **Result:** **fails** (Base IRR +1.2%, P_k NOK 73.2, margin of safety −22.8%). The improvement from v4 (−27.8%) comes from the lower price.
  - **Unchanged:** company inputs (no new report), 2027–29 rows, mid-cycle TCE and values, asset values for products, the MR newbuild verdict.
  - **Data access:** FinancialFilings still at its monthly limit (not re-queried); new filings checked on Newsweb (5–17 Oct).
- **10 Oct 2026 (v4):** product re-test from the Oil Shipping BBB third run (LR2 2028 44 → 38; LR1 2028 33 → 30, 2029 25 → 28; seasonal Q4-27). Result: fails (Base IRR −1.4%, P_k NOK 74.6, −27.8%).
- **10 Oct 2026 (v3):** fleet and orderbook register (LR2 2029 31 → 35; register evidence in the growth capex test). Result: fails (−1.3%, P_k NOK 74.9, −27.5%).
- **10 Oct 2026 (v2):** Oil Shipping BBB 10 Oct (stub and 2027 higher), price NOK 103.30, new IAF output layout (Summary first, per-share tables, debt amortisation line), market marks split from the 28 Sep anchor, TORM exit from its reported NAV, provenance flags. Result: fails (−1.3%, P_k NOK 74.7, −27.7%).
- **5 Oct 2026 (v1):** first Hafnia analysis, under iaf-valuation rev 2026-10-05.2 with the 4 Oct baselines. Result: fails (Base IRR −0.5%, P_k NOK 70.5, −27%).

## Appendix: own assumptions `[A]`

| Assumption | Value | Why |
|---|---|---|
| Q3-26 open-day rates | LR2 100, LR1 70, MR 35, Handy 30 ($k) | September fixtures; pool earnings mid-Aug; load-to-discharge lag |
| Q4-26 cover by segment | LR2 83% at 30.8k, LR1 10% at 27.7k, MR 27% at 23.0k, Handy 23% at 24.2k | Derived from Q3 vs H2 cover and rates |
| Stub factor | 0.8 × baseline stub on Q4 open days | Reporting lag; pool levels; open days mostly in Nov–Dec |
| Hafnia TCE factor 2027+ | 1.00 × rows | Older, partly non-eco fleet vs pool scale and IMO II; no calibration series |
| Handy row | 0.90 × MR row (incl. mid-cycle and values) | Hafnia's realised ratio |
| Segment split of owned broker value | LR2 450, LR1 986, MR 1,582, Handy 721 ($m) | Hafnia segment values less the JV share |
| Value anchor | 28 Sep 5-yr values (LR2 85, LR1 60, MR 50) ≈ Hafnia's 30 Jun broker level; today's marks LR2 85, LR1 68, MR 52 | v1 fit of 10-yr/5-yr ratios; baseline 24 Oct |
| Ages (value-weighted, 30 Jun) | LR2 7.0, LR1 9.8, MR 10.8, Handy 11.0 | Fleet list |
| Age factor | 1.10 − 0.02a (< 5 years); 1 − 0.04(a − 5) (5–15); 0.60 − 0.05(a − 15) (> 15), floor 0.15 | Fits 10-yr/5-yr ratios of ~0.80 |
| Glide | Today's marks to 31 Dec 2026, then linear to the scenario mid-cycle at exit | IAF Step 3 |
| Reversion tail | 2-year linear fade at 8%, pre-tax; open days = consolidated + JV share as in 2029 at 97% utilisation | IAF Step 3; tonnage tax |
| TORM | DPS = 0.008 × Hafnia own net profit; exit = (fleet $4,056m × mid-cycle factor × 0.82 − net debt $319m) ÷ 102.4m shares | TORM Q2 release; fitted ratios |
| TC-in purchase options | MR vessel value $51.6m at the anchor, LR1 $55.0m; strikes decline $0.38m / $0.25m a year | Fitted to the $191m in-the-money value at 30 Jun |
| Newbuild schedule | 2 in Q3-28, 2 in Q4-28, 6 through 2029; depreciation $1.9m a year each | "Delivery 2028–2029"; capex chart |
| JV terms | Vista LR2 TC to end-2027; Ecomar TC to 2029; JV cash retained | Coverage table; French tax-lease structure |
| H&A distribution | $28.3m in Q4-26 | Carrying $15.0m + gain $13.3m |
| Debt amortisation split | $12.2m a quarter (H2-26), $33.6m (2027), $18.6m (2028), $16.6m (2029) | Note 7 schedule and lease run-off |
| Net working capital | $404m constant | 30 Jun balance sheet |
| Payment dates | Q3 → 15 Dec; Q4 → 20 Mar; Q1 → 18 Jun; Q2 → 23 Sep | 2025–26 ex/pay pattern |
| Shares | 542.2m incl. option dilution | Diluted − basic at 30 Jun |

## Appendix: sources

Raw values as fetched (converted values are in the sections above).

| Source | As-of | Raw value / content | Used for |
|---|---|---|---|
| Yahoo `HAFNI.OL` | 23 Oct 2026 close (last print 14:28:39 UTC) | NOK 98.00 (prev. 96.45; day 95.85–99.60; volume 1.22m; 52-week 51.7–106.0); 535,331,154 shares. Daily closes 16–23 Oct: 94.85, 94.75, 95.00, 97.20, 96.45, 98.00 | P, shares |
| Yahoo `HAFN` | 23 Oct 2026 20:00 UTC | $10.50 (prev. 10.33) | Cross-check of P |
| Yahoo `NOK=X` 15-min bars | 23 Oct 2026 14:15 UTC | close 9.34025 (14:00 bar 9.33748; 14:30 bar 9.33553; 20:00 bar 9.32385) | FX at the price time stamp |
| Norges Bank `EXR/B.USD.NOK.SP` (MCP `norges-bank`) | 16–23 Oct 2026 fixings | 9.441, 9.4036, 9.3843, 9.3573, 9.3601, **9.3509** (23 Oct) | FX cross-check |
| AllRatesToday `get_rates_authenticated` (time 23 Oct 14:20 UTC) | 24 Oct 2026 | 403: dated rates need a paid plan | Not used |
| Yahoo `TRMD` | 23 Oct 2026 20:00 UTC | $39.89; 102,711,882 shares; Q3 report 4 Nov | TORM stake value (NAV today) |
| Yahoo `HAFN` `earningsTrend`, `financialData`, `secFilings` | seen 24 Oct 2026 | Q3-26 EPS $0.30 (1 est.; 7 days ago 0.26), Q4-26 $0.30 (1); FY26 $1.37 (1), FY27 $0.71 (1); revenue Q3 $298.1m (3; 274–316), Q4 $377.6m (3; 330–425), FY26 $1,355m (3), FY27 $1,201m (4); target mean $11.5 (2; 11–12); last 6-K 13 Oct; Q3 report 18 Nov | Consensus `[E]`, filing check |
| Zacks `get_wall_st_rating` / `get_real_time_news` (HAFN, TRMD) | 24 Oct 2026 | BTIG Strong Buy $12 (14 Sep); DNB Carnegie Hold (12 Mar); Clarksons Platou Strong Buy (9 Feb); Fearnley $6.71 (2 Dec 2025); no articles in 15 days | Market check only |
| Newsweb API (`api3.oslo.oslobors.no/v1/newsreader/list`, in-app browser) | 16–23 Oct 2026 | 559 messages; no HAFNI or TORM issuer message (filter verified on 683904 and 683944 of 12 Oct) | Company news check |
| FinancialFilings `filings_list` (company 9980) | 24 Oct 2026 | HTTP 429, monthly credit limit; resets 1 Nov | Not available |
| Nordic Financial `search_filings` (HAFNI, newsweb, 2026) | 24 Oct 2026 | Latest Hafnia item indexed 3 Sep (accelerated vesting); nothing after | Not current; Newsweb API used |
| Newsweb: Hafnia 683904 | 12 Oct 2026 | CFO sold 50,000 shares at NOK 101.5203 on 9 Oct; holds 563,544 shares and options | Insider signpost |
| Newsweb: TORM 683944 | 12 Oct 2026 | FY26 guidance TCE $1.7–1.9bn (was $1.4–1.6bn), EBITDA $1.3–1.5bn (was $1.0–1.2bn); Q3 report 4 Nov | Q4 cross-check |
| Newsweb: Hafnia 683621; TORM 683606, 683643, 683731, 683841, 683859 | 5–9 Oct 2026 | Share redelivery; Oaktree's exit from TORM | Carried from v2 |
| Newsweb: TORM Q2 2026 results (680798) | 30 Jun 2026; published 26 Aug | Dividend $2.40, fleet value $4,056m, NAV $36.50/share | TORM dividends and exit value |
| Hafnia Q2 2026 interim report (FinancialFilings 57967361) | 30 Jun 2026; published 28 Aug | Accounts, borrowings $885.4m, cash $271.0m, cover, TC-in options, fleet list | Balance sheet, fleet, cover |
| Hafnia Q2 2026 presentation (59231672) | 28 Aug 2026 | Dividend policy, net LTV 13.0%, newbuild capex chart, drydock 214 days in Q4, Bloomberg consensus (24 Aug) | Policy, capex, consensus |
| Hafnia 424B5 prospectus supplement (62394258) | 25 Sep 2026 | $330m RCF, BW loan, capitalisation | Debt, liquidity |
| Placement and TORM purchase announcements | 16 Sep – 5 Oct 2026 | 35,488,875 shares at NOK 80; 535,331,154 shares; TORM 4.5m at $32.25, 1.7m at $34.00 | Shares, TORM stake |
| `docs/oil-shipping-bbb.md` | 24 Oct 2026 (rev 2026-10-24.1) | New stub method; VLCC 850 → 700, Aframax 245 → 305; LR2 220, LR1 120, MR 55 kept; 2027–29, Year-1 quarters, mid-cycle TCE and values unchanged; LR1 5-yr now 68 (Intermodal Oct avg 68.3); period market at Base (LR1 1-yr 60/61, MR 45/39.5); For IAF: "Hafnia: no change" | Market input, exit consistency |
| `docs/oil-shipping-bbb.md` | 17 Oct 2026 | Rows (LR1 stub 120), asset values (Xclusiv 12 Oct), asset-implied TCE anchors, register, catalysts | Carried (v5) |
| `docs/oil-market-bbb.md` | 24 Oct 2026 | Re-run, kept unchanged (paths and mid-cycle) | Through the shipping baseline |
| `docs/equity-market-bbb.md` | 17 Oct 2026, amended 18 Oct | Oslo exit P/E 10.5 / 11.5 / 12.5, exit P/B 1.48 / 1.75 / 1.97, mid-cycle return 8.2 / 9.1 / 9.4%; USD/NOK path Bear +12% / +9% / +9%, Bull −3%, Base flat | Exit cross-check, NOK path |
| Model | `py` scripts (scratchpad), quarterly engine with reversion tail; v7 run reproduces v6 exactly at the v6 inputs before the re-mark | — | All `[A]` derivations |
