# SED Energy Holdings (ENH) — IAF analysis, 17 Oct 2026, method re-run 18 Oct, market check 20 Oct, news update 27 Oct: T-16 award (stub Q3–Q4 2026 + 2027–2029)

> **4 Nov 2026, kept unchanged (change gate):** read Rig Market BBB small updates of 28 Oct and 4 Nov: the tender-assist row and rig values are unchanged (T-16 logged as one fixture, checkpoint 17 open); only the UDW drillship 2027 point moved. No figure in this document changes.

Skill revisions used: **iaf-valuation 2026-10-18.2** (backlog at exit, exit cross-check, NOK path in Bear/Bull, holdco G&A outside NAV), **equity-market-bbb 2026-10-18.6** (exit reference read only; the skill is now at 2026-10-24.1, but `docs/equity-market-bbb.md` has not been re-run since 17/18 Oct, so the values read are the same). Sector inputs:
- `docs/rig-market-bbb.md`: baseline 10 Oct 2026 (Final, stale after 9 Nov), produced with rig-market-bbb rev 2026-10-08.2. It had small updates on 13, 17, 22 and 24 Oct (rev 2026-10-10.1) with **paths unchanged**.
  - The tender-assist row is used directly and has not changed since 4 Oct.
  - Rig values use the Rig BBB asset-value convention.
  - No own rig forecast.
- `docs/oil-market-bbb.md`: baseline 17 Oct 2026 (Final, stale after 16 Nov), produced with oil-market-bbb rev 2026-10-11.1. Background only: Brent Base 2027 rose from 85 to 88, mid-cycle unchanged. SE Asia NOC gas work has low oil sensitivity, and Rig BBB asks for no change. A newer baseline (24 Oct) has the Brent paths and mid-cycle unchanged; nothing here changes.
- `docs/hy-market-bbb.md`: not used. SED has no bonds; its only debt is a SOFR-based USD bank loan.
- `docs/equity-market-bbb.md` (17 Oct, amended 18 Oct): Oslo exit P/E, exit P/B and mid-cycle return for the exit cross-check, and the USD/NOK path for the Bear/Bull NOK figures. Nothing else is taken from it.
- **18 Oct:** method only; price, FX, company data and valuation date (17 Oct) unchanged.
- **20 Oct:** Fearnley's sector report (via TDN Finans) is added as a **market check only**. A broker target is never an IAF input. No new company information; the decision figures are unchanged.
- **27 Oct, news update: T-16 award.** CPOC's letter of award for T-16 Phase 7 (MFN, 27 Oct 07:00) replaces the T-16 assumption in all three scenarios. Price, FX and valuation date are rolled to 26/27 Oct. No market input changes: the Rig BBB tender-assist row and the Equity BBB exit references and NOK path are as before.

## Summary

**Verdict: fails.**
- **Base:**
  - IRR_T is **6.7%** against k = 12%. The hurdle price P_k is **NOK 6.03** against a price of **NOK 6.80**, so the **margin of safety is −11.3%**.
  - The cash yield is high (d = 12.0%). But the 2026 contracts at $94–160k/day roll off by end-2027 into Rig BBB's tender-assist Base of $78–85k. T-16 is now the exception: ~$95k/day firm from Jul 2027 to Jan 2030. Value falls from NAV_0 (NOK 6.23) to V_T (NOK 5.43) as the fleet ages and today's firm contracts expire, partly offset by the contracts the Base signs in 2028–29 that run past exit.
- **Bear breaks the thesis:** IRR −31%, and ~58% of the capital is lost. The balance sheet survives (peak net debt ~$33m); distributions shrink to ~$14m in 2028 and ~$6m in 2029.
- **Bull:** IRR 27.1%, P_k NOK 9.41. The price already reflects ~23% of the Bull upside.
- **What the price needs:**
  - exit asset values ~21% above Base mid-cycle (≈ $500m, 4.9x 2029 EBITDA); or
  - two levers together, e.g. opex 10% lower and a 35-year rig life (15.9%), or $90k/day on the new barge contracts plus exit values 20% higher (12.9%). No single operating lever is enough now: opex −10% gives 11.4%, a 35-year life 11.0%.
- **The exit cross-check is consistent with the market:** V_T is 10.3x normalised asset-level FCF against Oslo's exit P/E of 11.5, and the exit P/B (1.20) is below the index's 1.75. The buyer's return (8%) is a little below Oslo's 9.1%; at 9.1% Base is 5.5%.
- **Change since 20 Oct** (Base 8.3% → 6.7%; P_k 6.02 → 6.03; margin of safety −8.0% → −11.3%):
  - **Contract (T-16 award): +0.5 pp, P_k +0.07** (8.8%, P_k 6.09, at the old price, FX and date). ~$95k/day for 30 months instead of the Base's $80k from Jan 2027, but with a ~5-month idle gap in 2027 and options assumed at $90k after the firm term. Bear gains (+2.2 pp) and Bull loses (−0.5 pp): the award sits between the old Base and Bull assumptions.
  - **FX and valuation date: −0.5 pp, P_k −0.05.** USD/NOK 9.44 → 9.32 lowers the NOK value of USD cash and assets (−0.6 pp); ten days of roll-forward add +0.1 pp.
  - **Price: −1.6 pp, P_k −0.01** (option dilution). NOK 6.55 → 6.80, the 26 Oct close, before the 07:00 release. Each NOK 0.10 on the price moves IRR_T by ~0.6 pp.
  - The verdict is unchanged: **fails**. The award is a Bull-band rate, but it covers one barge of six for 30 months and does not move the exit value, which still decides the verdict.
- **Change 17 → 18 Oct** (6.0% → 8.3%), method only (iaf-valuation 2026-10-18.1):
  - **Backlog at exit (+2.3 pp).** On 31 Dec 2029 the Base has signed contracts running into 2030–31 (all five rigs and GHTH). A buyer pays for them, so they now count in V_T, capped at 2 years after exit. The 17 Oct rule (contracts firm today only) is kept as a sensitivity: 6.0%.
  - The verdict is unchanged: **fails**.
- **Market check, 20 Oct (not an IAF input):**
  - **Fearnley upgraded SED from Hold to Buy, with a target of NOK 8.0** (unchanged).
  - The target sits 33% above Base P_k (6.03 on 27 Oct) and about 58% of the way to Bull P_k (9.41).
  - At k = 12% it needs exit values ~1.5x Base mid-cycle, against × 1.21 to clear the hurdle at NOK 6.80.
  - The report summary gives no SED-specific reason, and nothing in it changes a Rig BBB input for tender rigs.
  - The price was unchanged at NOK 6.55 on 20 Oct; it closed at 6.80 on 26 Oct (used from 27 Oct).

**Decision table**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (27 Oct 2026 → 31 Dec 2029) | −30.9% | **+6.7%** | +27.1% |
| IRR_T in NOK on the Equity BBB NOK path | −28.7% | +6.7% (spot flat) | +25.8% |
| V_T per share (NOK) | 1.59 | **5.43** | 9.35 |
| P_k (hurdle price) / margin of safety | 2.29 / −66.4% | **6.03 / −11.3%** | 9.41 / +38.4% |
| Capital preserved? (ΣD_t + V_T vs 6.80) | **No: 2.85 (−58%)** | Yes: 8.02 | Yes: 12.76 |
| Cumulative Maintenance FCF per share, Q4-26 to 2029 (NOK) | 1.14 | **2.83** | 3.98 |
| Net debt per share at exit (NOK; negative = net cash) | 0.16 | **−0.20** | −0.54 |
| Balance sheet | Distributions cut to ~$14m (2028) and ~$6m (2029) by the cash floor; cash ≥ ~$19m; ~$45m refinancing in Q1 2028 against EBITDA ~$53m | **Net cash or low debt throughout (peak $22m, Q2-27)** | Net cash $43m at exit |

**Per-share path** (NOK per share; 737.3m shares; USD/NOK 9.32)

| | Q3-26E | Q4-26E | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| **Base** EBITDA after GHTH bareboat, $m | 39.0 | 40.3 | 100.3 | 107.7 | 93.3 |
| EBITDA per share | 0.49 | 0.51 | 1.27 | 1.36 | 1.18 |
| **Maintenance FCF per share** | **0.37** | **0.39** | **0.82** | **0.98** | **0.65** |
| Debt amortisation per share | 0.03 | 0.03 | 0.10 | 0.10 | 0.10 |
| FCF after debt service per share | 0.34 | 0.36 | 0.72 | 0.87 | 0.54 |
| D_t paid per share | — (Q1 paid Aug) | 0.32 (Q2, 13 Nov) | 0.89 | 0.82 | 0.57 |
| Net debt per share, period end | 0.04 | −0.03 | 0.04 | −0.13 | −0.20 |
| V_t per share, year end | — | 6.08 | 5.69 | 5.64 | **5.43** |
| **Bear** Maintenance FCF per share | 0.37 | 0.39 | 0.36 | 0.33 | 0.06 |
| Bear V_t per share | — | 6.08 | 4.14 | 2.93 | 1.59 |
| **Bull** Maintenance FCF per share | 0.37 | 0.39 | 1.13 | 1.25 | 1.22 |
| Bull V_t per share | — | 6.08 | 7.01 | 8.54 | 9.35 |

- Maintenance FCF = EBITDA after bareboat − tax − net interest − maintenance capex, before debt amortisation.
- Q3-26 ended before the valuation date, so its cash is already in today's net debt.
- The end-2026 V_t is identical in all scenarios. It now includes the T-16 Phase 7 contract, which is firm today in every scenario.

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value · `[E]` external or secondary · `[C]` secondary source carried from an earlier version · `[A]` own assumption · `[?]` not found.

## Header

| Item | Value |
|---|---|
| Company | SED Energy Holdings Plc (Cyprus), Euronext Oslo: ENH, ISIN CY0101162119. Holding company for Energy Drilling (tender rigs, Singapore) and SeaBird Exploration (seismic source vessels, Bergen). Reports in USD |
| Price (P) | **NOK 6.80**, close 26 Oct 2026, last trade 15:25 UTC (Yahoo `ENH.OL`; day range 6.76–6.88, volume 1.87m). This is the **last close before the T-16 release** (27 Oct 07:00 CET; Oslo opens 09:00), so the market's reaction is not in it. Not ex-dividend: the Q2 distribution goes ex on 9 Nov. Previous versions: NOK 6.55 (16 and 20 Oct) |
| Valuation date / exit date | 27 Oct 2026 / 31 Dec 2029, **T = 3.18 years** (17 Oct up to the 20 Oct version) |
| Shares | 731.25m outstanding (incl. 108.1m non-voting B shares) `[F]` + 18.1m options at NOK 4.53 average strike `[F, Q2 report]` → **737.3m** by the treasury method at NOK 6.80 |
| Market cap / EV | NOK 5.01bn = **$538m**. Financial net debt ≈ $3m at 30 Sep `[A, Q3E]` → EV ≈ $541m; ≈ $549m including the GHTH lease (~$7.5m `[A]`). EV / LTM adj. EBITDA ($135.6m `[F]`) ≈ 4.0x |
| NAV at today's market marks | **Omitted: no current mark.** The only transaction for these rigs is Seadrill's 2023 sale (~$85m for T-15, T-16 and West Vencedor), which is over three years old and was distressed. It is shown as a sensitivity |
| **NAV_0** (scenario mid-cycle marks + contracts firm today − net debt) | **Base NOK 6.23 (P/NAV_0 1.09x)**; Bear 3.10 (2.19x); Bull 9.64 (0.71x). Includes T-16 Phase 7, firm today though it starts in Jul 2027 |
| FX | USD/NOK **9.32** (Yahoo `NOK=X` 30-minute bar 15:00–15:30 UTC on 26 Oct, close 9.3244, matching the price time stamp; Norges Bank fixing 26 Oct 9.3444). Held constant. Previous versions: 9.44 |
| Track | **B** (offshore drilling with contract roll-over and idle risk; finite-life assets). FCF basis, year-by-year IRR, P vs P_k |
| k | **12%**, not raised. SED has net cash and a liquid share (~1–3m shares a day). Customer concentration (PTTEP/Thailand 53% of H1 revenue) and short contract cover are handled in the scenarios, not through k. At k = 13% / 14%, P_k is 5.90 / 5.78 |
| Horizon | Stub Q3-26 (ended, unreported) + Q4-26; 2027 by quarter; 2028–2029 annual |

**Sources, and the check for new events since 10 Oct:**
- **27 Oct:** the MFN release list shows **"Energy Drilling receives letter of award for 30-month drilling campaign for T-16"** (27 Oct 07:00), the first SED release since 25 Sep. Terms are read from the release page (primary; see Contracts). Nordic Financial's Newsweb stream did not have it yet at ~07:30 UTC.
- **Nordic Financial** (back online), `search_filings` with `source="newsweb"`, ticker ENH, 2026: the newest SED announcement is still from September. There is no contract award.
- **MFN** (`mfn.se/a/energy-holdings`, read 17 Oct):
  - The newest release is **25 Sep (board change)**.
  - Calendar: **ex-date 9 Nov; Q3 report 18 Nov 2026 at 06:00** `[F]`.
- **FinancialFilings:** not re-run. The monthly quota was used up on 10 Oct. Share issues are checked through MFN/Newsweb instead: none.
- **Company documents** (read 4 Oct, unchanged):
  - Q2 2026 report and presentation (26 Aug, period to 30 Jun 2026).
  - Pareto company presentation (17 Sep).
  - Ventura transaction presentation (11 Sep).
  - Q2 distribution notice (4 Sep), EGM minutes (22 Sep), board change (25 Sep).
- **Yahoo:** ENH.OL, VTURA.OL, NOK=X (16 Oct; 26 Oct for the 27 Oct update). Norges Bank USD/NOK fixing (26 Oct) as a check.
- **Web:** Offshore Magazine / Hellenic Shipping News — Seadrill's sale of three tender units to Energy Drilling for ~$85m (Jun 2023).

## Scenario definitions (from Rig Market BBB, 10 Oct; tender-assist row unchanged since 4 Oct)

| Scenario | Catalyst | What it does to SED |
|---|---|---|
| **Base** (decision) | NOC-led demand converts gradually (Petronas, PTTEP, CPOC). Gulf jackups come back gradually, so SE Asia stays priced low but not at Foresight levels. Tender-assist **78 / 82 / 85** ($k/day, 2027–29), mid-cycle 80 | T-16: CPOC Phase 7 award (all scenarios), ~$95k from mid-Jul 2027 to mid-Jan 2030 after ~5 months idle; options exercised at $90k `[A]` to Apr 2031. EDrill-1 and T-15 bridged to Foresight's start, idle ~4 months, then re-let at $78k. Semi-tender options exercised (Vencedor $123k, GHTH $147k) |
| **Bear** (stress) | Gulf jackups idled by a war re-escalation after the 3 Nov midterms relocate to Asia, and Foresight-type pricing ($60–70k) spreads. Tender-assist **68 / 65 / 65**, mid-cycle 67 | T-16 award as Base; options not exercised (open from Jan 2030). EDrill-1 and T-15 idle 8–9 months, then $68k/$65k. GHTH returned in Jul 2027. Vencedor idle 4 months, then $95k |
| **Bull** (stress) | 2H26 budget FIDs and NOC energy-security programmes (Malaysia/Indonesia fiscal changes from 2028); Aramco/KJO absorb the Gulf jackups. Tender-assist **88 / 95 / 100**, mid-cycle 95 | T-16 award as Base; options exercised at $90k `[A]`. EDrill-1/T-15 idle ~1 month, then $88k and $95k from late 2028. Semis $150–165k from 2028–29 |

- The stub (Q3–Q4 2026) and the end-2026 asset marks are identical in all scenarios. Bear and Bull diverge from 1 Jan 2027.
- **What kind of stress test each is** (structural IRRs, see Results):
  - Bear and Bull are **shifts in the mid-cycle**: Bear structural −30.1%, Bull 26.2%, against Base 4.9%.
  - They are not rate paths around an unchanged mid-cycle: within each scenario the 2027–29 rate path moves IRR by only −0.8 to +1.8 pp.
  - Since 27 Oct the scenarios no longer differ on T-16's firm term and rate (fact in all three); they differ only on its options and on the market after Jan 2030.

## Company and status

- Formed 26 May 2025 by the reverse acquisition of SeaBird Exploration by Energy Drilling.
- Largest owner: Pioneer Logistics Holdings, 40.1% of capital and 29.7% of votes. CEO Kurt Waldeland. Chair Kjell E. Jacobsen since 25 Sep, after Alf C. Thorkildsen (HitecVision) retired `[F]`.
- **Energy Drilling** claims ~38% of the world's actively marketed tender rigs `[F]`.

**Fleet** (Pareto, 17 Sep; table read from extracted PDF text with a garbled layout, so the SPS years are `[F/?]`):

| Rig | Type | Built / yard | Build cost | Last / next SPS | Age at exit |
|---|---|---|---|---|---|
| EDrill-1 | Tender barge | 2014 / COSCO Guangdong | $135m | 2022 / **2027** | 15.5 |
| EDrill-2 | Tender barge | 2014 / COSCO Guangdong | $135m | 2024 / 2029 | 15.5 |
| T-15 | Tender barge | 2012 / COSCO Nantong | $113m | 2024 / 2029 | 17.5 |
| T-16 | Tender barge | 2013 / COSCO Nantong | $113m | 2024 / 2029 | 16.5 |
| ED Vencedor | Semi-tender | 2009 / Keppel FELS | $201m | 2024 / 2029 | 20.5 |
| GHTH | Semi-tender, chartered in (back-to-back bareboat) | 2021 / COSCO Guangdong | $220m | — / 2026 | — |

- **SeaBird:** Eagle Explorer (2D, India, Sep 2026 – May 2027) and Fulmar Explorer (OBN source, West Africa, Sep – Nov 2026, then marketed). Firm backlog $24m `[F]`.
- **Tax:** Singapore MSI-AIS exemption; tax is paid in the operating countries. Q2: $4.4m, 6.4% of contract revenue `[F]`.
- **Balance sheet 30 Jun 2026** `[F]`:
  - Bank debt $61.1m ($75m facility, SOFR + 350 bp, maturity Q1 2028; amortisation $8.1m a year since Feb 2026).
  - Lease liability (GHTH) $10.1m. Cash $39.4m plus $14.2m restricted.
  - Net interest-bearing debt incl. lease $17.6m (0.1x LTM adj. EBITDA). Equity $334.1m (71%).
  - PP&E $319.2m including the vessels (~$40m).
  - Three rigs and two vessels are unencumbered. Covenants were met at 30 Jun; their terms are `[?]`.
- **Distribution policy:** distribute excess liquidity quarterly; 2026 guidance **$90–110m** `[F]`.
  - **Q2 2026: $25.0m (USD 0.0342/share), approved at the EGM on 22 Sep. Ex-date 9 Nov, paid ~13 Nov `[F]`. Not yet ex, so it counts** (NOK 0.319 at 9.32; the NOK amount is fixed on 9 Nov; the company estimated NOK 0.32).
  - Payment pattern: about 4.5 months after quarter end (Q1 paid in August, Q2 in November) `[F]`.

### Contracts (Pareto 17 Sep; backlog as of 30 Jun; T-16 award 27 Oct)

| Rig | Client / area | Firm period | Rate $k/day | Option rate | Status |
|---|---|---|---|---|---|
| EDrill-1 | PTTEP, Thailand | Oct 2023 – **Dec 2026** | 94 | 94 | Follow-on tender lost to Foresight (start Feb 2027) `[E]` |
| EDrill-2 | PTTEP, Thailand | Oct 2025 – Oct 2030 | 83 (average incl. full index) | — | Firm 5 years: with T-16 Phase 7 (to Jan 2030), one of two firm contracts running past the exit |
| T-15 | PTTEP, Thailand | Mar 2026 – Jan 2027 | 121 | none shown | Follow-on lost to Foresight (start Apr 2027) `[E]` |
| T-16 | CPOC, Malaysia/JDA (Phase 6) | Nov 2024 – **Dec 2026** firm `[F, 27 Oct release]`; campaign expected to end in **Q1 2027** on extension options `[F]` | 131 | 124 | December and the Q1-27 extension modelled at $124k, ending mid-Feb 2027 `[A]` |
| T-16 | CPOC, Malaysia/JDA (**Phase 7**, letter of award 27 Oct) | **30 months from early Q3 2027** `[F]`; modelled 15 Jul 2027 – 15 Jan 2030 `[A]` | **~95.1** effective: **USD 87m firm incl. mobilisation fees** `[F]` ÷ 915 days `[B]`; mobilisation amount not disclosed `[?]` | Up to 15 months `[F]`; rate not disclosed `[?]`, $90k assumed `[A]` | Between the phases the rig is demobilised to Singapore with reduced crewing and costs `[F]`; idle length and cost not quantified `[?]` |
| ED Vencedor | PTTEP (Arthit), Thailand | Nov 2024 – Dec 2027 | 127 | 123 | |
| GHTH | Myanmar | Nov 2025 – Jul 2027 | 160 | 147 | Bareboat in ~$27k/day (H1 lease payments $4.86m) `[F/A]` |

- The option rates come from the garbled table; their assignment to rigs is my reading `[F/?]`.
- **Firm cover for 2027 is 52% of fleet rig-days** (44% before the T-16 award; 55% with the expected Q1-27 Phase 6 extension).
- The release states no dayrate. The ~$95k is the firm value spread over the firm days, so it includes the mobilisation fee.
- **PTTEP–Foresight** (23 Sep): two 350 ft jackups, 5 years + 3 options, rate not published. Three secondary sources say $60–70k; still unconfirmed `[C]`.

### Latest reported quarters ($m)

| | Q1 2026 | Q2 2026 |
|---|---|---|
| Revenue (Energy Drilling / SeaBird) | 69.8 (62.0 / 8.0) | 71.5 (64.4 / 7.3) |
| Adj. EBITDA (ED / SeaBird) | 39.0 | 42.6 (41.6 / 1.6) |
| ED opex | ~20 | 20.0 (= $36.6k per rig-day) |
| Profit | 21.8 | 25.6 |
| Net debt incl. lease | 30.5 | 17.6 |
| Distribution (declared) | 25.0 | 25.0 |
| ED utilisation, technical / economic | 98% / 98% | 98% / 99% |

H1 2026: operating cash flow $80.6m, capex $8.1m, distributions paid $42.5m `[F]`.

## Near term: stub quarters (all scenarios)

| | Q3-26E (ended 30 Sep, unreported) | Q4-26E |
|---|---|---|
| Rig-days / firm share | 552 / 100% | 552 / 100% (T-16 firm through December `[F]`; the December rate is assumed at its $124k option rate `[A]`) |
| Average dayrate | $119.3k | $118.9k |
| Drilling revenue ($m) | 64.6 | 64.3 |
| EBITDA, company basis (IFRS 16) / after bareboat | 41.5 / 39.0 | 42.8 / 40.3 |
| Maintenance FCF ($m / NOK per share) | 29.2 / 0.37 | 30.6 / 0.39 |
| FCF after debt service ($m) | 27.2 | 28.5 |
| Distribution declared (90% of FCF after debt service) | $24.5m = **NOK 0.31**, paid ~15 Feb 2027 `[A]` | $25.7m = **NOK 0.32**, paid ~15 May 2027 `[A]` |
| Financial net debt, end of quarter ($m; excl. lease) | 3.3 | **−2.2** (net cash) |

- **2026 distributions** in the model: $100m (H1 $50m + H2 $50m), in the middle of the $90–110m guidance.
- **Consensus** (Yahoo, as-of date not shown and probably from before the PTTEP loss, so stale `[?]`): FY26 EPS ~NOK 1.17, FY27 ~NOK 0.80. Model (20 Oct version, at 9.44; not recomputed for the T-16 award, which lowers 2027 slightly and lifts 2028–29): FY26 ~NOK 1.3; FY27 Base ~0.71, Bear ~0.09, Bull ~1.06. Not used for the decision.
- **Net debt bridge to 31 Dec 2026** ($m, financial debt only):
  - 30 Jun: 7.5 (debt 61.1 − cash 53.6).
  - Plus distributions paid 50.0 (Q1 $25m in Aug, Q2 $25m on ~13 Nov).
  - Less FCF after debt service 55.7 (Maintenance FCF 59.8 − amortisation 4.1).
  - = **−2.2** (net cash).
- **Net debt at the valuation date** (≈ 30 Sep): **$3.3m** (NOK 0.04/share). The GHTH lease is paid through FCF as bareboat and is not counted again in net debt.
- **Q3 distribution timing:** the Ventura LOI provides for the Q2 distribution to be paid before closing. Later distributions may wait for closing or lapse (long-stop 31 Mar 2027) `[C]`. The standalone model keeps the normal schedule; a few months' delay changes IRR by < 0.1 pp.
- **Dates:**
  - Ex-date 9 Nov, paid ~13 Nov.
  - **Q3 report 18 Nov, 06:00** `[F, MFN calendar]`.
  - US midterms 3 Nov.
  - Ventura Q3 and capex guidance: late Nov.
  - EDrill-1 firm end: Dec 2026; T-15 firm end: Jan 2027.
  - T-16: Phase 6 ends in Q1 2027; Phase 7 starts early in Q3 2027 `[F]`.
  - Ventura long-stop: 31 Mar 2027.
- **Not modelled:** GHTH's first special survey is listed for 2026 `[F/?]`. If it falls in Q4 with off-hire, every 20 days cost ~$3m of revenue.

## Market input

**Rig Market BBB (10 Oct, paths unchanged on 13, 17, 22 and 24 Oct) — rows used directly.** Open rig-days use the leading-edge rate for the rig's segment row; the rates apply to term work starting in the year.

| $k/day | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| Tender-assist barges Bear / Base / Bull | 80 / 80 / 80 | 68 / **78** / 88 | 65 / **82** / 95 | 65 / **85** / 100 | 67 / **80** / 95 |
| SE Asia jackups (context) Bear / Base / Bull | 90 | 72 / 90 / 98 | 70 / 95 / 108 | 70 / 98 / 115 | — / 92 / — |

- **Tender-assist mid-cycle Bear/Bull (67 / 95) and MCU (65 / 80 / 90%)** come from the Rig BBB asset table, which took them from this analysis `[A, SED]`. They were derived by scaling Base 80 with the high-spec jackup mid-cycle ratios (92 / 110 / 130).
- **Rig BBB has no utilisation path for tender-assist** (MCU `[?]`, no series). The exit-consistency test is therefore on the rate basis, with an earnings-basis variant shown.
- **Semi-tenders** are not covered by Rig BBB. Company-anchored `[A]`:
  - Bear 100 / 95 / 95, Base 120 / 120 / 125, Bull 135 / 150 / 165; mid-cycle 100 / 120 / 140.
  - Anchors: current contracts $127–160k; option rates $123k (Vencedor) and $147k (GHTH); company scenario tables pair barge $70–80k with semi $100–120k, and barge $150k with semi $180k.
- **Rig values: Rig BBB asset-value convention:**
  - Annual cash flow = 365 × [MCU × (rate × RE − opex) − (1 − MCU) × idle × opex] − tax × revenue − maintenance capex.
  - Value = annual cash flow × annuity(8%, 30 − age), floored at $10m.
  - Tender parameters: opex $35k / $40k (company), RE 98%, idle 40% of opex, maintenance capex $3.0m / $3.5m, tax 6.4% of revenue, flat nominal.
  - Check: a 15-year-old barge at Base is $62m in Rig BBB; this model gives EDrill-1/2 (15.5 years at exit) $60.4m.
- **Transaction check (Rig BBB):** Seadrill → Energy Drilling, two barges + one semi-tender, $85m (Jun 2023), implies ~$58k/day for a barge on the convention. That is 27% below Base mid-cycle, from a distressed 2023 sale. Drillship and jackup transactions in 2025–26 imply 8–12% *above* Base mid-cycle.
- **Market data from the company** (Pareto 17 Sep, Aug-26 data) `[E]`:
  - SE Asia rig count 80 (21% tender rigs).
  - Tender-assist fleet utilisation "up to 88%".
  - 23 tenders ongoing, 9 prospects, 28 pre-tender projects.
  - Tendering "delayed … as operators reassess timing and risk".
- **Oil Market BBB (17 Oct):** Brent Base 88 / 77 / 72 (2027 raised from 85), mid-cycle 70 unchanged. The geopolitical channel matters more than the oil price: Gulf jackups idled by war move to Asia (Bear for SED), while energy security supports NOC gas programmes (Bull).

## Common assumptions (all scenarios)

| Item | Value | Source |
|---|---|---|
| Opex per rig-day, operations | Barge $35k, semi-tender $40k in 2026; +3% a year from 2027 | Company (Ventura deck, slide 14 footnote) `[F]`. Check: 4 × 35 + 2 × 40 = $220k/day × 91 = $20.0m = reported Q2 ED opex. Escalation `[A]` |
| Opex in rig values | Flat nominal $35k / $40k, like the mid-cycle rates | Rig BBB convention |
| Idle cost, operations | 65% of opex for the first 90 days (warm), then 35% (cold) | `[A]` (the values use the convention's 40%). T-16's Feb–Jul 2027 gap in Singapore uses the same rule: the release says "reduced crewing and operating costs" without a figure. De- and remobilisation costs are not modelled separately |
| Technical utilisation on contract | 98% (Bear 96% from 2027) | Q2 98% `[F]` |
| Special surveys | EDrill-1 2027, inside its idle period (cost in capex). EDrill-2, T-15, T-16 and Vencedor in 2029: 15 days off-hire each | SPS years `[F/?]`, days `[A]` |
| SeaBird contribution (revenue − opex, before SG&A) | Q3-26 $1.5m, Q4-26 $3.0m; 2027–29 Bear 5 / Base 10 / Bull 18 $m a year | Q2 actual $2.6m `[F]`; rest `[A]` |
| SG&A (group) | $4.3m a quarter in 2026; 17.0 / 17.5 / 18.0 in 2027–29 | Q2 $4.27m `[F]` |
| Maintenance capex | Q3-26 5, Q4-26 5; 2027 20; 2028 15; 2029 28 (four SPS) | 2026 guide ~$18m, H1 $8.1m `[F]`; rest `[A]` |
| Tax | 6.4% of revenue | Q2 `[F]` |
| Debt | $61.1m at SOFR + 350 bp: 7.7% (2026), 8.3% (2027–29). Amortisation $8.1m a year. Q1-2028 maturity refinanced on the same terms. Cash earns 3.5% | Q2 report `[F]`; SOFR futures Z26 4.23%, Z27 4.81% (2 Oct, `docs/capt-analysis.md`) `[C]`, 25 days old at 27 Oct; refinancing `[A]` |
| GHTH bareboat | $27k/day while GHTH works; ends with its contract (back-to-back) | Lease payments `[F]`; rate derived `[A]` |
| Payout | **90% of FCF after debt service** (Maintenance FCF − amortisation), paid ~4.5 months after quarter end. Minimum cash $20m (incl. $14.2m restricted), applied at payment | Policy "distribute excess liquidity" `[F]`; ratio and floor `[A]`. Payout 75% / 100% gives IRR 6.6% / 6.8% |
| Working capital | Ignored (receivables $39.3m at 30 Jun) | `[A]` |
| Shares | 737.3m; no new shares, buybacks or acquisitions; **Ventura excluded** | `[A]` |

### Rig-by-rig assumptions per scenario (after the common stub)

| Rig | Bear | Base | Bull |
|---|---|---|---|
| EDrill-1 | Ends Dec 2026. Idle Jan–Aug 2027. $68k from Sep 2027 (18 months). Idle 3 months. $65k from Jun 2029 | Bridged to end-Feb 2027 at the $94k option. Idle Mar–Jun. $78k from Jul 2027 (18 months). Idle Jan 2029. $85k from Feb 2029 | Bridged to end-Mar 2027 (Foresight slips). Idle Apr. $88k from May 2027. $95k from Nov 2028 |
| EDrill-2 | $83k to Oct 2030 | same | same |
| T-15 | Ends Jan 2027. Idle Feb–Oct 2027. $68k from Nov 2027. Idle 3 months. $65k from Aug 2029 | Bridged to end-Mar 2027 at $121k (well-in-progress; no priced option `[A]`). Idle Apr–Jul. $78k from Aug 2027. Idle Feb 2029. $85k from Mar 2029 | Bridged to end-Apr 2027. Idle May. $88k from Jun 2027. $95k from Dec 2028 |
| T-16 | Phase 6 to mid-Feb 2027 at $124k. Idle in Singapore to mid-Jul. **Phase 7 ~$95k, mid-Jul 2027 – mid-Jan 2030** (awarded 27 Oct). Options not exercised; open from Jan 2030 | As Bear to Jan 2030. **Options exercised: $90k to mid-Apr 2031** `[A]` | As Base (the $90k options are below the Bull market rate) |
| ED Vencedor | $127k to Dec 2027. Idle Jan–Apr 2028. $95k from May 2028 | $127k to Dec 2027. Option $123k through 2028. Idle Jan 2029. $125k from Feb 2029 | $127k to Dec 2027. Option $123k through 2028. $165k from Jan 2029 |
| GHTH | $160k to Jul 2027, then redelivered (bareboat ends) | Option $147k Aug 2027 – Jul 2028. Idle 1.5 months. $120k from mid-Sep 2028 | Option $147k to Jul 2028. $150k from Aug 2028 |

**Backlog at exit (iaf-valuation Step 3):** contracts running on 31 Dec 2029 are backlog in that scenario, and a buyer pays for them. Contracts firm today count for their full term (EDrill-2 to Oct 2030; T-16 Phase 7 to Jan 2030, firm today though it starts in Jul 2027). Contracts the scenario signs, and options it exercises (T-16 from Jan 2030 in Base and Bull), count for at most 2 years after exit (to end-2031), at the rate signed. In practice only Bull Vencedor (to Jan 2032) is cut by the cap. After the backlog ends, the days are open at mid-cycle.

## Period tables ($m, with NOK per share in brackets where Step 2B requires it)

### Base (decision case)

| | Q3-26E | Q4-26E | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|---|
| Drilling revenue | 64.6 | 64.3 | 54.2 | 33.0 | 51.5 | 54.8 | 207.3 | 197.7 |
| EBITDA, company basis | 41.5 | 42.8 | 33.0 | 14.9 | 30.0 | 32.2 | 116.3 | 103.2 |
| EBITDA after bareboat | 39.0 | 40.3 | 30.6 | 12.5 | 27.5 | 29.7 | 107.7 | 93.3 |
| Maintenance FCF (NOK/share) | 29.2 (0.37) | 30.6 (0.39) | 21.5 (0.27) | 4.7 (0.06) | 18.4 (0.23) | 20.4 (0.26) | 77.3 (0.98) | 51.1 (0.65) |
| Debt amortisation | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 8.1 | 8.1 |
| FCF after debt service (NOK/share) | 27.2 (0.34) | 28.5 (0.36) | 19.4 (0.25) | 2.7 (0.03) | 16.4 (0.21) | 18.4 (0.23) | 69.2 (0.87) | 43.0 (0.54) |
| Growth capex | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Distribution declared (NOK/share) | 24.5 (0.31) | 25.7 (0.32) | 17.5 (0.22) | 2.4 (0.03) | 14.7 (0.19) | 16.6 (0.21) | 62.3 (0.79) | 38.7 (0.49) |
| Net debt, end of period (NOK/share) | 3.3 (0.04) | −2.2 (−0.03) | 0.7 (0.01) | 21.7 (0.27) | 20.8 (0.26) | 2.8 (0.04) | −9.9 (−0.13) | −16.2 (−0.20) |

- 2027 full year: EBITDA $110.2m on the company basis ($100.3m after bareboat); Maintenance FCF $65.0m (NOK 0.82/share).
- Q2-27 is the trough: EDrill-1, T-15 and T-16 are all idle. From 2028 the T-16 award lifts cash against the old Base ($95k against $80k).

### Bear (stub as Base)

| | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|
| Drilling revenue | 40.9 | 32.3 | 32.4 | 36.9 | 132.7 | 125.4 |
| EBITDA, company basis | 20.0 | 14.3 | 15.0 | 17.6 | 52.5 | 43.2 |
| Maintenance FCF (NOK/share) | 9.3 (0.12) | 4.0 (0.05) | 6.2 (0.08) | 9.4 (0.12) | 26.0 (0.33) | 4.8 (0.06) |
| FCF after debt service (NOK/share) | 7.2 (0.09) | 2.0 (0.02) | 4.1 (0.05) | 7.3 (0.09) | 17.9 (0.23) | −3.3 (−0.04) |
| Distribution declared (NOK/share) | 0.08 | 0.02 | 0.05 | 0.08 | 0.20 (partly withheld by the cash floor) | 0.01 |
| Net debt (NOK/share) | 12.9 (0.16) | 33.0 (0.42) | 31.0 (0.39) | 23.4 (0.30) | 11.8 (0.15) | 12.9 (0.16) |

### Bull (stub as Base)

| | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|
| Drilling revenue | 57.1 | 44.4 | 55.7 | 56.6 | 224.9 | 237.8 |
| EBITDA, company basis | 37.5 | 26.4 | 35.4 | 36.0 | 140.0 | 150.0 |
| Maintenance FCF (NOK/share) | 25.7 (0.33) | 15.5 (0.20) | 23.7 (0.30) | 24.3 (0.31) | 99.0 (1.25) | 96.3 (1.22) |
| FCF after debt service (NOK/share) | 23.7 (0.30) | 13.5 (0.17) | 21.7 (0.27) | 22.2 (0.28) | 90.9 (1.15) | 88.2 (1.11) |
| Distribution declared (NOK/share) | 0.27 | 0.15 | 0.25 | 0.25 | 1.03 | 1.00 |
| Net debt (NOK/share) | −3.5 (−0.04) | 6.6 (0.08) | 4.3 (0.05) | −7.9 (−0.10) | −27.3 (−0.35) | −42.7 (−0.54) |

### Year-end path per share (NOK; D_t = distributions paid in the period)

**Interim marks:**
- At end-2026, all scenarios use Base mid-cycle marks plus contracts firm today, because no current market mark exists.
- The marks then glide linearly (one third a year) to each scenario's own mid-cycle at exit. From end-2027 each mark also counts the backlog the scenario holds on that date (2-year cap).

| | | Stub (to 31 Dec 26) | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| **Base** | D_t | 0.32 | 0.89 | 0.82 | 0.57 |
| | V_t | 6.08 | 5.69 | 5.64 | **5.43** |
| | r_t | −5.9% (not annualised) | +8.0% | +13.6% | +6.3% |
| | IRR to t | n.m. (0.18 yr) | +1.3% | +6.7% | **+6.7%** |
| **Bear** | D_t | 0.32 | 0.69 | 0.18 | 0.08 |
| | V_t | 6.08 | 4.14 | 2.93 | **1.59** |
| | r_t | −5.9% | −20.7% | −24.7% | −43.2% |
| | IRR to t | n.m. | −23.7% | −24.4% | **−30.9%** |
| **Bull** | D_t | 0.32 | 1.06 | 1.01 | 1.02 |
| | V_t | 6.08 | 7.01 | 8.54 | **9.35** |
| | r_t | −5.9% | +32.7% | +36.2% | +21.4% |
| | IRR to t | n.m. | +22.0% | +28.8% | **+27.1%** |

The path is a diagnostic, not a per-year pass or fail:
- **Base:** 2027 is the weakest full year in cash (three barges idle in Q2), but the end-2027 mark carries the contracts signed in 2027 (+8.0%). 2028 is the best year (+13.6%), on cash and stable marks.
- **Bear:** loses value every year as the marks glide down to Bear mid-cycle, where the barges are near the $10m floor.
- **Bull:** value rises as the marks glide up to Bull mid-cycle, plus ~15% a year in cash.

## V_T bridge, Base ($m and NOK/share)

| Step | $m | NOK/share |
|---|---|---|
| P (market capitalisation incl. options, at 9.32) | 537.9 | 6.80 |
| Re-rating P → NAV_0 (P/NAV_0 1.09x, outside the 0.95–1.05 band: the price is 9% above NAV_0; −2.7% a year) | −45.2 | −0.57 |
| **NAV_0:** owned rigs at Base mid-cycle by age 384.3 + contracts firm today, premium vs mid-cycle 76.7 (T-16 Phase 7 adds ~$18m) + SeaBird 35.0 − net debt 3.3 | **492.7** | **6.23** |
| + Value created by growth capex (none committed) | 0 | 0 |
| − Ageing of the owned fleet at mid-cycle (384.3 → 336.5) | −47.8 | −0.60 |
| − Roll-off of the firm-today premium (76.7 → 4.3; EDrill-2 and two weeks of T-16 Phase 7 run past T) | −72.4 | −0.92 |
| + Premium on backlog signed in the Base (contracts and exercised options running past T, capped at end-2031; below) | +37.6 | +0.48 |
| ± Reversion tail (exit consistency; no material gap on open days, see below) | 0 | 0 |
| + Retained cash (net debt 3.3 → −16.2; includes the Q3/Q4-29 distributions payable after exit) | +19.5 | +0.25 |
| **= V_T (31 Dec 2029): assets 413.4 + net cash 16.2** | **429.5** | **5.43** |

g = (5.43 / 6.80)^(1/3.18) − 1 = **−6.8% a year**: re-rating −2.7% and NAV growth −4.2% a year.

**Exit asset values** ($m; scenario mid-cycle on the Rig BBB convention, age at exit, plus the contract premium on backlog at exit) `[A]`:

| Asset (age at exit) | Bear | Base | Bull |
|---|---|---|---|
| EDrill-1 (15.5) | 12.5 + 4.3 = 16.8 | 60.4 + 5.3 = 65.7 | 114.4 + 2.3 = 116.7 |
| EDrill-2 (15.5; firm today, $83k to Oct 2030) | 12.5 + 8.5 = 21.0 | 60.4 + 3.9 = 64.3 | 114.4 − 1.3 = 113.1 |
| T-15 (17.5) | 11.5 + 4.3 = 15.8 | 55.5 + 5.3 = 60.8 | 105.1 + 2.3 = 107.4 |
| T-16 (16.5; Phase 7 firm today to Jan 2030) | 12.0 + 0.6 = 12.6 | 58.0 + 8.9 = 66.9 | 109.9 + 1.0 = 110.9 |
| ED Vencedor (20.5) | 43.6 + 8.8 = 52.4 | 102.3 + 7.7 = 110.0 | 161.7 + 22.6 = 184.2 |
| GHTH (chartered in: value = contract margin after bareboat while its contract runs; nothing after) | 0 (redelivered Jul 2027) | 10.8 (to Sep 2030) | 14.7 (to Aug 2030) |
| SeaBird (2 vessels; book $40.3m at 30 Jun `[F]`) | 20 | 35 | 50 |
| Reversion tail | 0 | 0 | 0 |
| **Total assets** | **138.7** | **413.4** | **697.1** |
| of which: premium on contracts firm today / on backlog signed in the scenario | 9.1 / 17.5 | 4.3 / 37.6 | −1.2 / 42.8 |
| Net debt at exit | 12.9 | −16.2 | −42.7 |
| **V_T ($m / NOK per share)** | **125.8 / 1.59** | **429.5 / 5.43** | **739.8 / 9.35** |
| Assets / 2029 EBITDA (company basis), cross-check only | 3.2x | 4.0x | 4.6x |

**Backlog at exit, per contract** (scenario-signed unless stated; premium per day = contract day at 98% RE against the convention's mid-cycle day at the scenario MCU, incl. idle cost; discounted at 8%):

| Rig | Bear | Base | Bull |
|---|---|---|---|
| EDrill-1 | $65k, Jun 2029 – Jan 2031 | $85k, Feb 2029 – Jan 2031 | $95k, Nov 2028 – Jan 2031 |
| EDrill-2 | $83k firm today to Oct 2030 | same | same |
| T-15 | $65k, Aug 2029 – Jan 2031 | $85k, Mar 2029 – Jan 2031 | $95k, Dec 2028 – Jan 2031 |
| T-16 | $95k firm today to Jan 2030; options not exercised | $95k firm today to Jan 2030, then options at $90k to Apr 2031 | As Base |
| Vencedor | $95k, May 2028 – May 2031 | $125k, Feb 2029 – Jan 2031 | $165k, Jan 2029 – Jan 2032, **capped at end-2031** |
| GHTH | — | $120k, Sep 2028 – Sep 2030 | $150k, Aug 2028 – Aug 2030 |

- Most of the premium is utilisation, not rate: a contracted rig works ~98% of the days against the mid-cycle MCU of 65 / 80 / 90%. Base T-16 options: $90k × 98% ≈ $88k a day earned against $80k × 80% × 98% ≈ $63k at mid-cycle.
- **Sensitivity, contracts firm today only (the 17 Oct rule; T-16 Phase 7 counts, its options do not):** V_T Bear 1.37 / Base 4.95 / Bull 8.81; IRR_T −33.8% / **4.2%** / 25.2%; P_k 2.13 / 5.70 / 9.04.

- **Annual rig-level cash flow at mid-cycle:** barge $1.5m / $7.2m / $13.6m; semi-tender $6.7m / $15.8m / $25.0m. Bear barges sit near the $10m floor.
- **No exit multiple** is used, and the IAF ceiling is not used as an exit.
- **Cross-checks:**
  - Today's EV / LTM adj. EBITDA is ~4.0x; Base exit assets are 4.0x 2029 EBITDA.
  - Book value of the rigs ~$279m (30 Jun 2026).
  - At the 2023 transaction-implied rates ($58k barge, $87k semi, at 80% MCU), Base IRR falls to −10.4%.

### Exit consistency (Step 3)

The test runs on the **open days in the 2 years after exit** (2030–31). Days under backlog at exit are left out, because the contract premium carries them. In every scenario the owned rigs are under backlog through 2030 (EDrill-2 to Oct 2030), so the test covers 2031 (and the last two months of 2030 for EDrill-2). The exceptions are T-16, open from Apr 2031 in Base and Bull and from mid-Jan 2030 in Bear. EDrill-2's and T-16's open days are tested against the barge row's Year-3 market rate, not their own contract rates. GHTH has no value after its contract.

Rig BBB gives no utilisation path for tender rigs, so the **rate basis** decides. The **earnings basis** (the model's 2029 revenue per calendar day against mid-cycle rate × MCU × RE) is shown as a check.

| Rig | Scenario | Open share 2030 / 2031 | Year-3 rate | Mid-cycle | Gap (rate basis) | Gap (earnings basis) | Treatment |
|---|---|---|---|---|---|---|---|
| EDrill-1, T-15 | Bear | 0 / 100% | 65 | 67 | −3.0% | +10% / +7% | Not material |
| EDrill-2 (barge row) | Bear | 17% / 100% | 65 | 67 | −3.0% | +10% | Not material |
| T-16 (barge row) | Bear | 96% / 100% | 65 | 67 | −3.0% | +10% | Not material |
| Vencedor | Bear | 0 / 67% | 95 | 100 | −5.0% | +37% | Not material |
| EDrill-1, EDrill-2, T-15, T-16 | Base | 0–17% / 72–100% | 85 | 80 | +6.2% | +17–22% | Not material |
| Vencedor | Base | 0 / 100% | 125 | 120 | +4.2% | +14% | Not material |
| EDrill-1, EDrill-2, T-15, T-16 | Bull | 0–17% / 72–100% | 95 | 95 | 0% | +7–11% | Not material |
| Vencedor | Bull | 0 / 0 | 165 | 140 | +17.9% | +25% | **No test: under backlog to the cap (end-2031)** |

- **No reversion tail is applied** in any scenario. The 17 Oct named reason for Bull Vencedor is no longer needed: its contract carries the rig to the cap.
- **Earnings-basis gaps stay material in most rows** (+7% to +37%): the model's 2029 utilisation on contract (90–98%) is far above the mid-cycle MCU. That is a Rig BBB data gap (no tender-assist MCU path), carried to For other modules.
- **Sensitivity:**

| Exit treatment | Bear IRR_T / P_k | **Base IRR_T / P_k** | Bull IRR_T / P_k |
|---|---|---|---|
| **No tail (decision)** | −30.9% / 2.29 | **6.7% / 6.03** | 27.1% / 9.41 |
| Reversion tail on open days, rate basis (Base +$2.4m) | −31.1% / 2.27 | 6.9% / 6.05 | 27.1% / 9.41 |
| Reversion tail on open days, earnings basis (Base +$6.4m, NOK 0.08/share) | −30.2% / 2.32 | 7.1% / 6.09 | 27.3% / 9.44 |
| Contracts firm today only (17 Oct rule) | −33.8% / 2.13 | 4.2% / 5.70 | 25.2% / 9.04 |

### Exit cross-check against the equity market (Step 3)

| | Bear | **Base** | Bull |
|---|---|---|---|
| V_T ($m) | 125.8 | **429.5** | 739.8 |
| Normalised Maintenance FCF at the scenario mid-cycle, before holdco G&A ($m) | 12.3 | **56.7** | 107.7 |
| FCF_normalised (after the fleet-renewal charge), before holdco G&A ($m) | 7.7 | **41.7** | 81.2 |
| Holdco G&A, not in NAV (IAF rule) ($m a year) | 18 | **18** | 18 |
| **Exit P/E** on FCF_normalised before holdco G&A (Maintenance FCF basis in brackets) | 16.2x (10.2x) | **10.3x (7.6x)** | 9.1x (6.9x) |
| Book equity at exit ($m; 334.1 at 30 Jun + retained cash to exit `[A]`) | 329 | **358** | 384 |
| **Exit P/B** | 0.38 | **1.20** | 1.93 |
| **Buyer's implied return at exit** (Rig BBB asset rate; net cash in Base and Bull) | ~8% | **~8%** | ~8% |
| Oslo index (Equity BBB): exit P/E / exit P/B / mid-cycle return | 10.5 / 1.48 / 8.2% | **11.5 / 1.75 / 9.1%** | 12.5 / 1.97 / 9.4% |
| Sensitivity: exit marks at the index mid-cycle return instead of 8% (IRR_T / P_k) | −31.0% / 2.28 | **5.5% / 5.86** | 25.2% / 9.03 |

- **Exit P/B** is below the index in Base (1.20 vs 1.75): SED's normalised return on book (~11%) is below the index's ~15%. Consistent.
- **The buyer's return (8%) is below the Oslo mid-cycle return (9.1%)**, so the exit is a little generous against the stock market. At 9.1% Base falls to 5.5% (sensitivity above).
- **Exit P/E** on the NAV's own basis (asset-level, before holdco G&A) is 10.3x in Base against the index's 11.5x: consistent. Bear's 16.2x reflects mid-cycle cash near the $10m value floor, not a generous mark.
- **Holdco G&A ($18m a year) is outside NAV by the IAF rule** (2026-10-18.2): the holding company finances and sets strategy but does not operate the rigs. It is in the 2026–29 cash flows as paid. SED reports one group SG&A line; treating all of it as holding company is `[A]`. Any onshore operating support inside it would belong in rig opex.
- **Book equity is approximate:** no D&A figure was available (FinancialFilings quota used up on 18 Oct; Nordic Financial returned only the results announcement). Book at exit assumes maintenance capex ≈ D&A over the window `[A]`.

## Growth capex test (Step 4)

- **No growth capex is committed.** The capex in the model is maintenance and special surveys, so g is the change in value per share: ageing, contract roll-off and retained cash.
- **The growth decision is Ventura**, funded with 605m new shares (45% of the combined company). Under Step 4 it counts only if ROIC_g > k after dilution. It is not in the decision figure; see the overlay.
- **Rig purchases** (the company names consolidation and "new verticals") would be tested against the 2023 price (~$28m a rig) and the convention value (~$55–60m for a 15–18-year-old barge at Base). Nothing has been announced.

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T | −30.9% | **+6.7%** | +27.1% |
| IRR_T in NOK on the Equity BBB NOK path (USD/NOK Bear +12% / +9% / +9%, Bull −3%) | −28.7% | +6.7% | +25.8% |
| d / g / c | 5.8% / −36.7% / 0.0 pp | **12.0% / −6.8% / +1.6 pp** | 15.7% / +10.5% / +0.9 pp |
| g: re-rating / NAV growth (P/NAV_0) | −21.8% / −19.0% (2.19x) | **−2.7% / −4.2% (1.09x)** | +11.6% / −1.0% (0.71x) |
| Structural IRR / cyclical (pp; Δd, Δg) | −30.1% / −0.8 (+0.1, −0.9) | **4.9% / +1.8 (+0.8, +0.9)** | 26.2% / +0.9 (0.0, +1.0) |
| ΣD_t / V_T (NOK) | 1.26 / 1.59 | **2.59 / 5.43** | 3.40 / 9.35 |
| **P_k (hurdle price) / margin of safety** | 2.29 / −66.4% | **6.03 / −11.3%** | 9.41 / +38.4% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | 22.7x vs negative | **22.7x vs 4.7x** | 22.7x vs 18.8x |
| Capital preserved? ΣD_t + V_T vs P = 6.80 | **No: 2.85, −58%** | Yes: 8.02 (+18% nominal over 3.2 yr) | Yes: 12.76 |

**Notes on the results:**
- **Structural IRR:**
  - The same model with every open or re-priced day from 1 Jan 2027 at that scenario's own mid-cycle rate. Open days include the option and bridge periods and all new contracts: barge 67 / 80 / 95, semi 100 / 120 / 140. T-16 Phase 7 is firm today and keeps its rate.
  - The stub, firm-today contract days, idle gaps and exit asset values are unchanged; the reversion tail is zero. Backlog signed in the scenario stays at exit, re-priced to the mid-cycle rate, so only its utilisation premium remains.
  - Cyclical = IRR_T − structural.
  - Reading: the cycle adds little within each scenario (−0.8 to +1.8 pp). Bear (−35 pp) and Bull (+21 pp) against Base structural are **mid-cycle shifts**, driven by asset values.
- **FCF_normalised** (Rule 3):
  - Full fleet at Base mid-cycle (barge $80k, semi $120k, 80% MCU, RE 98%), 2029 opex, idle at 40% of opex, GHTH bareboat on working days, SeaBird $10m, SG&A $18m, tax 6.4%, maintenance capex $20m, interest income on exit net cash.
  - Maintenance FCF $38.7m, less a **fleet-renewal charge of $15.0m** (Base ageing −47.8 ÷ T) = **$23.7m = NOK 0.30/share → P/FCF 22.7x**.
- **Scenario-weighted reference (convention, 25/50/25 on levels D_t and V_T):** IRR 6.1%, P_k NOK 5.94. Not the decision figure.
- **Share of Bull already priced:** (6.80 − 6.03) / (9.41 − 6.03) = **23%**.
- **NOK path (Equity BBB):** decision at spot USD/NOK 9.32. On the Equity BBB path (same percentage moves as before) a weaker krone lifts the NOK value of SED's USD distributions and exit value in Bear (−30.9% → −28.7%); a firmer krone trims Bull (27.1% → 25.8%). Base is the same (spot flat).

**Bear — balance-sheet survival:**
- Net debt peaks at ~$33m (Q2-27). Bear EBITDA is $67m (2027), $53m (2028) and $43m (2029), so leverage stays below 1x. T-16's firm contract at ~$95k carries ~$20m a year of it from 2028.
- 2029 FCF after debt service is −$3m (the SPS year). The $20m cash floor (including $14.2m restricted) cuts distributions to ~$14m in 2028 and ~$6m in 2029, and cash bottoms at ~$19m.
- The bank loan matures in Q1 2028: ~$45m to refinance against Bear EBITDA of ~$53m. That is feasible, and T-16's contract to Jan 2030 helps, but lender appetite for tender rigs in a downturn is the risk. Covenant terms are not disclosed `[?]`.
- **Survivable, but with a permanent loss of ~58% of capital** (~55% in NOK on the Equity BBB path).

### Sensitivity (Base, unless stated)

| Change | IRR_T | P_k (NOK) |
|---|---|---|
| Exit asset values × 0.8 / 0.9 / 1.1 / 1.2 | +1.0% / +4.0% / +9.3% / +11.7% | 5.30 / 5.67 / 6.40 / 6.76 |
| **Break-even:** exit values × 1.21 (≈ $500m, 4.9x 2029 EBITDA) | 12.0% | ≈ 6.80 |
| Base cash flows with Bear / Bull exit values | −11.5% / +20.5% | 4.02 / 8.23 |
| Base cash flows, exit at 2023 transaction-implied rates ($58k / $87k) | −10.4% | 4.12 |
| Opex −10% / +10% ($31.5k / $38.5k barge; operations and values) | +11.4% / +1.6% | 6.71 / 5.35 |
| Rig life 35 years instead of 30 | +11.0% | 6.65 |
| Opex −10% and a 35-year rig life together | +15.9% | 7.41 |
| Reversion tail on open days, rate / earnings basis | +6.9% / +7.1% | 6.05 / 6.09 |
| Contracts firm today only at exit (17 Oct rule) | +4.2% | 5.70 |
| Exit marks at the Oslo mid-cycle return (9.1%) instead of 8% | +5.5% | 5.86 |
| k = 10% / 13% / 14% | — | 6.30 / 5.90 / 5.78 |
| Payout 75% / 100% of FCF after debt service | +6.6% / +6.8% | — |
| T-16 options not exercised in Base (open from Jan 2030) | +6.2% | 5.96 |
| T-16 option rate $85k / $95k instead of $90k | +6.6% / +6.8% | 6.01 / 6.05 |
| T-16: $4m of the $87m only covers mobilisation cost (effective $90.7k) | +6.5% | 6.00 |
| T-16 Phase 7 starts 3 months late (mid-Oct 2027) | +6.3% | 5.97 |
| Price NOK 6.70 / 6.90 / 7.00 (P_k unchanged) | +7.3% / +6.1% / +5.5% | 6.03 |

**Flat rate on all new barge contracts (EDrill-1, T-15 and the 2029 re-lets; T-16 is now fixed) × exit asset values (Base semis), IRR_T %:**

| Barge rate \ exit values | × 0.6 | × 0.8 | × 1.0 | × 1.2 | × 1.4 |
|---|---|---|---|---|---|
| $65k | −8.4 | −1.7 | 4.1 | 9.3 | 13.9 |
| $70k (Foresight level) | −7.5 | −0.8 | 4.9 | 10.0 | 14.6 |
| $75k | −6.7 | 0.0 | 5.7 | 10.7 | 15.3 |
| $80k | −5.8 | 0.8 | 6.4 | 11.5 | 16.0 |
| $85k | −5.0 | 1.5 | 7.2 | 12.2 | 16.7 |
| $90k | −4.2 | 2.3 | 7.9 | 12.9 | 17.4 |
| $95k | −3.3 | 3.1 | 8.7 | 13.7 | 18.1 |
| $100k | −2.5 | 3.9 | 9.4 | 14.4 | 18.8 |

- Each $5k/day on new barge contracts moves IRR by ~0.8 pp (less than before: T-16 is fixed, so only EDrill-1 and T-15 carry the lever). No realistic barge rate on its own clears the hurdle (break-even ~$118k). Each 0.2 step in exit values moves IRR by ~5 pp. Opex ±10% moves it by ~5 pp.
- The verdict still hinges on asset value at exit: opex, rig life and the mid-cycle rate. The 2027–29 rate path matters less.

### Market check: broker view (20 Oct; not an IAF input)

**Source:** TDN Finans / Infront summary on Nordnet (20 Oct, 08:57) of a Fearnley Securities offshore-drilling sector report of the same day `[E]`. The report itself was not read; only the summary was.

| | Fearnley (20 Oct) | This analysis (18 Oct method) |
|---|---|---|
| SED rating / target | **Buy (from Hold), NOK 8.0** (unchanged) | Fails; Base P_k **6.02**, Bull P_k 9.59 |
| Target vs price 6.55 | +22% (before ~NOK 1.2 of distributions over 12 months in the Base path) | Base IRR 8.3% a year to 2029 |
| Ventura | Buy, NOK 40 (from 37) | Overlay only |
| Jackups | Trend "sideways to falling"; Middle East normalisation should support demand | Rig BBB: jackups flat; SE Asia/tender priced low (the Base for SED) |
| Floaters | 7G drillships ~$500k/day, harsh-environment ~$520k/day; little idle high-spec capacity | Not an SED input |
| Oil | $75/bbl from 2027; risk skewed upwards | Oil BBB Base 88 / 77 / 72 (background) |

**Reading:**
- **The target needs Bull-leaning exit values.** P_k rises ~0.37 for each 0.1x step in exit values (sensitivity table), so NOK 8.0 at k = 12% needs exit values ~1.5x Base mid-cycle. That is roughly a 16–18-year-old barge at ~$85–90m, against Rig BBB's Base mid-cycle convention value of ~$56–60m and the 2023 sale at ~$28m. A 12-month broker target and a 3-year hurdle at k = 12% are different measures, so this is a scale check, not a reconciliation.
- **The upgrade is probably about price and Ventura, not new tender data.** The share has fallen ~13% since 17 Sep (7.55 → 6.55). Fearnley also raised Ventura (Buy, NOK 37 → 40). At its targets, 5.5 × (8.0 − 0.32 Q2 distribution) = 42.2 against Ventura's 40 is a ~5% gap: it prices the deal close to the exchange ratio.
- **Nothing here is an input.** The jackup view is in line with Rig BBB, and the tender-assist row is unchanged. The decision stays on P vs P_k: P 6.55 > P_k 6.02 → **fails**.
- **27 Oct:** after the T-16 award and with the price at 6.80, Base P_k is 6.03 and Bull 9.41. NOK 8.0 still needs exit values ~1.5x Base mid-cycle (1.54x).

## Verdict

- **Fails.** The Base margin of safety is −11.3% (P_k NOK 6.03 vs P 6.80; IRR_T 6.7% vs k = 12%).
- **Bear breaks the thesis.** ~58% of the capital is lost. The balance sheet survives; distributions shrink to ~$14m in 2028 and ~$6m in 2029.
- **Bull** returns 27.1% a year, and the price already reflects ~23% of it.
- **Why Base fails:**
  - Cash returns are strong: ~NOK 2.6/share of distributions to 2029, d = 12.0%.
  - But firm cover for 2027 is only 52% of rig-days, and the $94–160k contracts re-price into $78–85k. T-16's ~$95k award is the exception, and it comes after a ~5-month gap.
  - At exit the fleet is worth Base mid-cycle plus about a year of backlog at $85–90k/$125k (4.0x 2029 EBITDA), and value falls 4.2% a year from NAV_0.
  - The price is also 9% above NAV_0.
  - The exit cross-check finds the exit consistent with the stock market (10.3x vs the index's 11.5x); only the buyer's return (8% vs 9.1%) is a little generous.
- **What would flip it to a pass:**
  - exit values ≥ 21% above Base mid-cycle: barges at ~$67–73m at 16–18 years, against the 2023 sale at ~$28m; or
  - two levers together: opex 10% lower and a 35-year rig life (15.9%), or $90k on the new barge contracts plus exit values 20% higher (12.9%); or
  - a price at or below Base P_k, ~NOK 6.0.
- **Hard data points:** the CPOC award for T-16 is in (Bull-band rate; +0.5 pp in Base). Next: the Q3 report (18 Nov) and the EDrill-1 / T-15 follow-on awards.

**Caveat:** this is a margin-of-safety screen, not an intrinsic valuation or a price target. P_k is the price at which the Base path returns exactly 12%.

## Ventura LOI — overlay (not in the decision figure)

**Terms (11 Sep transaction presentation and press release, primary) `[F]`:**
- SED acquires 100% of Ventura Offshore for 605m new SED shares (45% of the combined company, fully diluted), an exchange ratio of 5.50x. The Ventura reference equity value is based on SED's 5-day VWAP to 10 Sep. It is reduced by:
  - a **Rig Cost Adjustment** for capex overruns on SSV Victoria and DS Carolina (above a >$20m buffer over the midpoint of the 2 Apr guidance); and
  - a **Delay Adjustment** of **$145k/day per rig** from 1 Mar 2027 until Petrobras acceptance.
- SED's Q2 distribution is paid before closing.
- Closing is expected in Q1 2027, subject to a definitive agreement, due diligence, **commencement of new contracts for certain of the parties' rigs**, approvals and consents. **Either party may withdraw if the conditions are not met by 31 Mar 2027.**
- Secondary detail: four of SED's six rigs on firm contract plus both Brazilian rigs accepted `[C]`.
- Financing: DNB $250m bridge plus extension of the $30m RCF; non-amortising debt targeted.
- Governance: Gunnar W. Eliassen nominated chair.

**Ventura (30 Jun) `[F]`:** firm backlog $978m.
- DS Carolina $403m and SSV Victoria $482m (Petrobras).
- SSV Catarina $39m (Eni; no follow-on).
- Zonda $49m and DVD $5m (managed).
- Pro forma backlog ~$1.3bn firm, $2.2bn including options.

**Company illustration (slide 14):** pro forma FCF per share of **NOK 1.4 / 1.7 / 2.6**, at:
- tender barge $70k / $90k / $150k;
- semi-tender $100k / $120k / $180k;
- 6G semi $250k / $300k / $350k.

The figures are before amortisation, with Ventura's contracted rigs at long-term cash rates.

**Reading:**
1. **On the company's own numbers the deal is accretive per share even at Bear-level tender rates.** The low case gives NOK 1.4, against SED standalone Base Maintenance FCF of ~NOK 0.8–1.0/share in 2027–28.
2. **The cost:**
   - pro forma debt (~$200–250m `[C]`);
   - Petrobras concentration;
   - Catarina re-contracting;
   - yard and acceptance risk on Victoria and Carolina;
   - SED owners' tender exposure diluted to 55%.
3. **SED's own tenders decide whether the deal happens.** T-16 and the two PTTEP barges must be on firm contracts by 31 Mar 2027 for the reported condition to be met. T-16 now has an award (27 Oct), but Phase 7 only **commences** in early Q3 2027, after the 31 Mar 2027 long-stop. If the condition means commencement rather than signing, T-16 cannot meet it in time. Whether T-16 is one of the named rigs is `[?]` (secondary source).
4. **Market take (price data, Yahoo daily closes; read 20 Oct, 26 Oct row added 27 Oct):**
   - **Day 1 (11 Sep):**
     - ENH −1.1% (7.34 → 7.26; it opened +3%) on 14.5m shares, ~5x normal volume.
     - VTURA +7.9% (34.2 → 36.9; intraday +14%), after already rising 14% in the four trading days before the announcement (30.0 on 4 Sep → 34.2).
     - Reading: Ventura holders liked the deal, while SED holders were neutral to slightly negative on the dilution.
   - **Deal spread** = 1 − VTURA ÷ (5.5 × ENH). The Q2 distribution (~NOK 0.32) goes to SED holders only, before closing, so it is deducted from ENH in the adjusted column:

     | Date | ENH | VTURA | Raw spread | Spread ex Q2 distribution |
     |---|---|---|---|---|
     | 11 Sep | 7.26 | 36.9 | 7.6% | 3.3% |
     | 21 Sep | 7.39 | 35.7 | 12.1% | 8.2% |
     | 2 Oct | 6.45 | 31.6 | 10.9% | 6.2% |
     | 16 Oct | 6.55 | 33.3 | 7.6% | 2.9% |
     | 20 Oct | 6.55 | 33.9 | 5.9% | 1.2% |
     | 26 Oct (before the T-16 release) | 6.80 | 32.9 | 12.0% | **7.7%** |

   - **Reading:**
     - The spread widened after the PTTEP loss (22 Sep: ENH −12.7%, VTURA −8.4%), when SED's own tender risk, and with it the closing condition, came into focus.
     - It narrowed to ~1% by 20 Oct, with ~5 months to the Q1-2027 closing and the exchange ratio still exposed to Ventura's cost and delay adjustments. By 26 Oct it had widened again to ~8% (ENH +4%, VTURA −3%).
     - **The market prices the deal as likely to close.** The earlier reading here ("the market doubts completion") overlooked the distribution and is withdrawn.
     - A narrow spread also means Ventura's standalone value is close to the deal value, so it is not proof of a high completion probability on its own.
   - **Broker:** Fearnley rates both Buy (20 Oct): Ventura NOK 40 (from 37), SED NOK 8.0. 5.5 × (8.0 − 0.32) = 42.2 against 40 is a ~5% gap at the targets.
5. **Next step:** a full pro forma IAF when the definitive agreement is signed and Ventura's Q3 capex guidance is out (late Nov). No completion probability is given.

## Tracking

**27 Oct (news update: T-16 award), vs 20 Oct.** Steps in order; each column adds one change.

| | 20 Oct | + T-16 contract | + FX and date | 27 Oct (+ price) |
|---|---|---|---|---|
| Price / USD/NOK / valuation date | 6.55 / 9.44 / 17 Oct | 6.55 / 9.44 / 17 Oct | 6.55 / 9.32 / 27 Oct | **6.80** / 9.32 / 27 Oct |
| Base IRR_T | 8.3% | 8.8% | 8.3% | **6.7%** |
| Base P_k / margin of safety | 6.02 / −8.0% | 6.09 / −7.0% | 6.04 / −7.8% | **6.03 / −11.3%** |
| Base V_T / NAV_0 (NOK) | 5.43 / 6.08 | 5.50 / 6.35 | 5.43 / 6.23 | 5.43 / 6.23 |
| Bear IRR_T / P_k | −31.4% / 2.13 | −29.2% / 2.31 | −29.8% / 2.29 | −30.9% / 2.29 |
| Bull IRR_T / P_k | 29.9% / 9.59 | 29.4% / 9.51 | 29.1% / 9.42 | 27.1% / 9.41 |
| Break-even exit values (Base) | × 1.14 | × 1.12 | × 1.14 | × 1.21 |
| Verdict | Fails | Fails | Fails | **Fails** |

- **Contract (Base +0.5 pp):** ~$95k for 30 months against the Base's $80k from Jan 2027 with no gap. The ~5-month idle gap in 2027 costs most of the first-year gain; the rest comes from 2028–29 cash and the backlog at exit (Phase 7 to Jan 2030, then options at $90k).
- **Bear +2.2 pp:** T-16 at $95k from Jul 2027 instead of $68k from Apr 2027. **Bull −0.5 pp:** Bull had $88k from Jan 2027 with no gap and $100k from Jul 2029.
- **FX and date (Base −0.5 pp):** krone 1.3% stronger (−0.6 pp); ten days of roll-forward (+0.1 pp).
- **Price (Base −1.6 pp):** NOK 6.55 → 6.80, the last close before the release.
- No market input changed. Rig BBB (updates 22 and 24 Oct) and Oil BBB (24 Oct) have newer dates, with paths unchanged.

**20 Oct (market check, no re-run):**
- Fearnley upgraded SED to Buy, target NOK 8.0. The reading is in "Market check: broker view".
- Price 6.55 (unchanged); USD/NOK 9.40; VTURA 33.9.
- No SED release since 25 Sep (MFN, read 20 Oct). Decision figures unchanged.

**18 Oct:** method only; no new company information, inputs unchanged.

| | 17 Oct | 18 Oct | Main reason |
|---|---|---|---|
| Base IRR_T | 6.0% | **8.3%** | Backlog at exit (iaf-valuation 2026-10-18.1) |
| Base P_k / margin of safety | 5.72 / −12.7% | **6.02 / −8.0%** | Same |
| Base V_T | NOK 4.99 | 5.43 | Scenario-signed backlog premium +$34.4m |
| Bear / Bull IRR_T | −35.3% / 27.8% | −31.4% / 29.9% | Same |
| Verdict | Fails | **Fails** | |
| Break-even exit values | × 1.25 | × 1.14 | |

### Tracking (17 Oct vs 10 Oct 2026)

No new quarterly report and no company release since the previous version. Both rest on Q2 2026.

| | 10 Oct | 17 Oct | Main reason |
|---|---|---|---|
| Price / FX | NOK 6.42 / 9.58 | NOK 6.55 / 9.44 | Market |
| Base IRR_T | +9.7% | **+6.0%** | Exit-consistency rule; price and FX |
| Base P_k / margin of safety | 6.10 / −4.9% | **5.72 / −12.7%** | Same |
| Verdict | Fails (close to marginal) | **Fails** | |
| Base V_T | NOK 5.51 | 4.99 | Assumed post-T contracts no longer count as premium (−$34m); FX |
| NAV_0 / P/NAV_0 | 6.20 / 1.04x | 6.08 / 1.08x | FX, price |
| Break-even exit values | × 1.09 | × 1.25 | |

**Attribution of the Base IRR change (9.7% → 6.0%):**
- **Price +2.0%, FX −1.5%, valuation date: 8.3% (−1.4 pp).**
- **Exit consistency (iaf-valuation 2026-10-11.3): 6.0% (−2.3 pp).**
  - The 10 Oct version counted the contracts it assumed for 2029–30 as firm-contract premium at exit, at Year-3 rates and full utilisation. That carried the scenario's rate path past exit.
  - Now only EDrill-2 (firm today to Oct 2030) carries a premium, and the other days after T are open days at mid-cycle.
  - On the rate basis no gap is material in Base. GHTH has no value at exit without a firm contract.

**Running ahead or behind Base:** first test in. T-16's award (~$95k, Bull band on rate) is ahead of Base on rate, but it brings a ~5-month gap the Base did not assume; net +0.5 pp. Next: the Q3 report (18 Nov) and any EDrill-1/T-15 award before their contracts end.

## Risks and signposts

| Signpost | Bear | Base | Bull | Now (27 Oct) |
|---|---|---|---|---|
| **T-16 (CPOC) award** | No award by Dec or < $70k | $75–85k | ≥ $88k | **Resolved 27 Oct: Bull band.** ~$95k effective incl. mobilisation, 30 months from early Q3 2027 `[F/B]`; still ≥ $88k unless the mobilisation fee exceeds ~$6m. Offset: ~5 months idle in 2027 |
| EDrill-1 / T-15 follow-on | Idle > 6 months, ≤ $70k | Award by mid-2027 at ~$78k | Award by Q2-27 at ≥ $88k | None |
| Foresight start for PTTEP (Feb/Apr 2027) | On time | On time, short bridge | Delayed (longer bridge at $94–121k) | Rigs must move from the Middle East `[C]` |
| PTTEP–Foresight rate | Confirmed ≤ $70k and copied elsewhere | Seen as a one-off | Higher rates in other NOC awards | Unconfirmed, $60–70k `[C]` |
| SE Asia / tender pricing (Rig BBB) | Term fixtures < $80k | $80–100k | > $100k | Mixed: T-16 ~$95k (30 months, CPOC) is in the Base band; PTTEP–Foresight $60–70k (unconfirmed) towards Bear |
| Gulf jackups after 3 Nov | Renewed suspensions, rigs to Asia | Gradual return | Aramco/KJO absorb the rigs | KJO 4 × 4-year awards |
| Tender-rig asset transactions | Near the 2023 level (~$28m) | ~$55–65m for a 15–18-year-old barge | > $100m | None since 2023 |
| Contracts running past 2029 | Re-let at ≤ $65k | Re-let at ~$85k into 2031 (in V_T as backlog, capped at end-2031) | Multi-year awards above mid-cycle | EDrill-2 (to Oct 2030) and T-16 (to Jan 2030, options to Apr 2031) firm today |
| Semi-tender options (GHTH Jul 2027 at $147k; Vencedor 2028 at $123k) | Not exercised | Exercised | Exercised, then > $150k | — |
| Ventura | Lapses on 31 Mar 2027 | Definitive agreement and conditions met | — | LOI; spread ~8% ex Q2 distribution (26 Oct). T-16 commences after the long-stop |

**Other risks:**
- Concentration: Thailand is 53% of H1 revenue.
- Owner structure: Pioneer 40.1% of capital; B shares without votes.
- Distributions are booked as a return of paid-in capital; tax treatment depends on the shareholder's country.
- Currency: USD earnings, NOK share price (the krone strengthened 1.3% from 16 to 26 Oct).
- GHTH: the 2026 SPS and renewal of the back-to-back bareboat.
- Refinancing in Q1 2028.
- T-16: ~5 months idle in Singapore in 2027, with de- and remobilisation (costs not disclosed). Each 3 months' delay to the Phase 7 start costs ~0.4 pp in Base.

## For other modules

- **Rig Market BBB:**
  1. **Add an MCU path (Bear / Base / Bull by year) to the tender-assist row.** Without one, the exit-consistency test can only run on the rate basis. On the earnings basis SED's Year-3 utilisation (90–98%) is far above the mid-cycle MCU (80%), and the gaps are material in every scenario. The MCU also sets most of the backlog premium at exit (utilisation, not rate). Company data point: fleet utilisation "up to 88%" (Aug-26).
  2. Any tender-rig transaction or broker value would firm up the exit marks; the only one is a distressed 2023 sale. (The named reason built on it is no longer used.)
  3. Add a **semi-tender** row. Anchors: SED contracts $127–160k; options $123k (Vencedor) and $147k (GHTH); company scenarios $100–180k.
  4. Correct EDrill-1's firm end to **Dec 2026** and add the option rates (carried request).
  5. Carried from 10 Oct: state whether flat nominal opex in values means real terms (it moves SED's Base by ~4 pp).
  6. New 20 Oct, for review: Fearnley's sector summary `[E]` quotes 7G drillships at ~$500k/day and harsh-environment floaters at ~$520k/day, against Rig BBB 2027 Base $400k / $425k (2028 $455k / $450k). It calls the jackup trend "sideways to falling". Check against fixtures before any change; nothing in it concerns tender rigs.
  7. New 27 Oct, for review: **T-16 Phase 7 term fixture** (CPOC, Malaysia/JDA, letter of award 27 Oct `[F]`): USD 87m firm incl. mobilisation for 30 months from early Q3 2027, ≈ $95k/day `[B]` (mobilisation not split out). It is a 2027-start tender-assist fixture ~22% above the Base row's 78 (range 70–88) and above Bull's 88. For the recalibration rule; this analysis changes no Rig BBB input.
- **Oil Market BBB / HY BBB / Equity BBB:** no change needed.
- **IAF (method):** none. Holdco G&A is now outside NAV by rule (2026-10-18.2); PLSV still deducts it and needs a re-run.

## Change log

- **27 Oct 2026: news update, T-16 award.** CPOC letter of award for T-16 Phase 7 (MFN release, 27 Oct 07:00, primary): 30 months firm from early Q3 2027, options for up to 15 months, ~USD 87m firm incl. mobilisation fees. Phase 6 is firm through Dec 2026 and ends in Q1 2027; the rig waits in Singapore in between.
  - T-16 replaced in all scenarios: firm in all three; options exercised in Base and Bull at an assumed $90k, not in Bear.
  - Price 6.55 → 6.80 (26 Oct close, before the release), USD/NOK 9.44 → 9.32, valuation date 27 Oct. Market inputs unchanged.
  - Model: the firm-today rule now also covers a signed contract that starts later (T-16 Phase 7, in NAV_0 and all marks), and an option period that directly follows a counted contract counts as scenario backlog at exit.
  - **Result:** Base 8.3% → **6.7%** (contract +0.5 pp, FX and date −0.5 pp, price −1.6 pp), P_k 6.02 → **6.03**, margin of safety −8.0% → **−11.3%**; Bear −31.4% → −30.9%; Bull 29.9% → 27.1%. The verdict is still **fails**.
- **20 Oct 2026 (later): Ventura market take.** Price reaction and deal spread table added to the overlay. The spread, adjusted for the Q2 distribution that only SED holders receive, is ~1%, so the earlier "market doubts completion" reading is withdrawn.
- **20 Oct 2026: market check only.** Fearnley upgrade (Buy, NOK 8.0) read via TDN Finans on Nordnet (Edge connection) and set against P_k. Price unchanged (6.55); USD/NOK 9.40; no new SED release. Decision figures unchanged.
- **18 Oct 2026: method re-run under iaf-valuation rev 2026-10-18.1, then 18.2** (from `docs/review-iaf-exit.md`). Inputs unchanged (price, FX, valuation date 17 Oct, company data, sector paths).
  - **Backlog at exit:** contracts the scenario signs before exit now count in V_T, capped at 2 years after exit, on the asset convention's earnings basis; firm-today contracts as before. NAV_0 and end-of-stub marks unchanged (firm today only); later interim marks count the scenario's backlog.
  - **Exit consistency** on open days after exit only; no tail in any scenario; the Bull Vencedor named reason is no longer needed.
  - **New:** exit cross-check against Equity BBB (exit P/E, exit P/B, buyer's return), and Bear/Bull IRR in NOK on the Equity BBB NOK path.
  - **Holdco G&A (iaf-valuation 2026-10-18.2, same day):** not deducted in NAV, by rule; the G&A sensitivity is removed and the cross-check's exit P/E is on asset-level earnings. No change to the decision figures.
  - Structural run keeps scenario backlog at exit at the mid-cycle rate.
  - **Result:** Base 6.0% → **8.3%**, P_k 5.72 → **6.02**, margin of safety −12.7% → **−8.0%**; Bear −35.3% → −31.4%; Bull 27.8% → 29.9%. The verdict is still **fails**.
- **17 Oct 2026:** re-run under iaf-valuation rev 2026-10-11.3. Rig BBB paths unchanged; Oil BBB 17 Oct (background). No new company information.
  - **Method:**
    - Exit-consistency test added (rate basis, earnings basis shown); the Bull Vencedor gap uses a named reason, with tails as sensitivities.
    - Firm-contract premium in V_T, NAV_0 and interim marks is now only for contracts firm today. Scenario-assumed contracts are open days after T.
    - GHTH has no value at exit.
  - **Inputs:**
    - Price NOK 6.55 and FX 9.44 (16 Oct).
    - New-events check via Nordic Financial (Newsweb) and MFN: no release since 25 Sep; Q3 report 18 Nov at 06:00.
  - **Result:** Base 9.7% → **6.0%**, P_k 6.10 → **5.72**, margin of safety −4.9% → **−12.7%**. The verdict is still **fails**.
- **10 Oct 2026:** re-run under iaf-valuation rev 2026-10-10.1. Rig BBB asset-value convention; summary first; g as value CAGR; structural IRR per scenario; renewal charge in FCF_normalised. Base 9.7%, fails.
- **4 Oct 2026:** full rebuild under iaf-valuation rev 2026-10-04.12; migrated to English; Rig BBB tender row used directly; NAV exit. Base 5.3%, fails.
- **3 Oct 2026:** first SED analysis (Norwegian). Exit at 3.5 / 4.0 / 5.0x EBITDA; rates derived from Rig BBB high-spec jackups. Base 14.5%, marginal pass.

## Appendix: own assumptions `[A]`

| Assumption | Value | Why |
|---|---|---|
| T-16 Phase 6, Dec 2026 – mid-Feb 2027 | $124k (option rate) in all scenarios; end mid-Feb 2027 | Release: firm through Dec 2026, campaign ends in Q1 2027 `[F]`; rate and end day `[A]` |
| T-16 Phase 7 | 15 Jul 2027 – 15 Jan 2030 at $95.1k (USD 87m ÷ 915 days); 98% revenue efficiency applied (Bear 96%), so the model books ~$85m of the $87m | Release: 30 months from "early Q3 2027", USD 87m incl. mobilisation `[F]`; start day and spreading the mobilisation fee over the term `[A]` |
| T-16 options | Base and Bull: 15 months at $90k to mid-Apr 2031, scenario backlog at exit; Bear: not exercised | Option rate not disclosed `[?]`; ~$90k is the firm value less a few $m of mobilisation; Base/Bull exercise and Bear does not, as for the semi-tender options |
| T-16 idle gap | Mid-Feb – mid-Jul 2027 in Singapore, at the idle-cost rule (65%, then 35% of opex) | Release: "reduced crewing and operating costs", not quantified `[?]` |
| PTTEP bridging (Base) | EDrill-1 to end-Feb 2027 at $94k (option); T-15 to end-Mar 2027 at $121k | Foresight starts Feb/Apr 2027; T-15 has no priced option disclosed |
| Idle periods | Base ~4 months, Bear 8–9, Bull ~1 for the PTTEP barges | Six tenders open with none awarded at the Q2 call `[C]`; delayed tendering |
| Semi-tender rates | 100 / 95 / 95 · 120 / 120 / 125 · 135 / 150 / 165; mid-cycle 100 / 120 / 140 | Not in Rig BBB; option rates and company scenarios |
| Option exercise | Base and Bull: GHTH 12 months at $147k; Vencedor 2028 at $123k; T-16 2030–31 at $90k | Base and Bull exercise priced options, Bear does not (GHTH's $147k is above the Base semi rate and still exercised) |
| Opex escalation (operations only) | +3% a year from 2027 | Values use flat nominal opex (Rig BBB) |
| Payout / cash floor | 90% of FCF after debt service; $20m minimum cash incl. restricted | Policy; H1 payout ~100% |
| Interim marks | End-2026 at Base mid-cycle + contracts firm today (all scenarios), linear glide to scenario mid-cycle at exit; from end-2027 plus the scenario's backlog on that date (2-year cap) | No current market mark; IAF Step 3 |
| Exit premium | Contracts firm today (EDrill-2; T-16 Phase 7) in full; scenario-signed contracts and exercised options running past T, capped at end-2031 | IAF Step 3 backlog rule (2026-10-18.1) |
| Book equity at exit | $334.1m at 30 Jun + retained cash to exit (maintenance capex ≈ D&A) | No D&A figure available; for the exit P/B only |
| Holdco G&A | Group SG&A ($18m a year from 2029) treated as holding company: in the cash flows as paid, not in NAV | IAF rule 2026-10-18.2; no split of SG&A reported |
| SeaBird | Contribution 5 / 10 / 18 $m a year; exit value 20 / 35 / 50 | Q2 contribution $2.6m; book $40.3m |
| 2029 special surveys | 15 days off-hire for each of four rigs; capex $28m | Pareto SPS schedule |
| Net debt at 30 Sep | $3.3m (Q3E) | Q3 not reported |

## Appendix: sources and provenance

**Raw → derived (key market inputs):**

| Item | Raw value (source, as-of) | Derived / used | Check |
|---|---|---|---|
| Share price | Yahoo ENH.OL 26 Oct: O 6.76 / H 6.88 / L 6.76, last 6.80 at 15:25:06 UTC, volume 1.87m (16 Oct: C 6.55) | P = NOK 6.80 | Close inside the day range. Pre-release (27 Oct 07:00). Accepted |
| USD/NOK | Yahoo NOK=X 30-minute bar 15:00 UTC 26 Oct, close 9.32443 (16 Oct: 9.44342) | 9.32 | Matches the price time stamp. Norges Bank fixing 26 Oct 9.3444 (taken earlier in the day), consistent |
| Shares | 731,252,967 (Yahoo impliedSharesOutstanding, 9 Oct; Q2 report ~731m); options 18.1m at NOK 4.53 `[F, Q2 report]` | 737.29m (treasury method at 6.80) | No share issue on MFN/Newsweb since 10 Mar |
| Q2 distribution | USD 0.0342/share, USD 25.0m (notice 4 Sep) | NOK 0.319 at 9.32, paid 13 Nov | The company's estimate was NOK 0.32 at 9.31; the NOK amount is fixed 9 Nov |
| VTURA | Yahoo VTURA.OL 33.3 (16 Oct 14:25 UTC) | Spread vs 5.5 × 6.55 = 36.0: 7.6% | — |
| Q3 report date | MFN calendar 2026-11-18 06:00 (read 17 Oct) | 18 Nov | Unchanged |
| T-16 award | MFN release page, 27 Oct 07:00 (primary): 30 months firm from early Q3 2027; options up to 15 months; ~USD 87m firm incl. mobilisation fees; Phase 6 firm through Dec 2026, ends Q1 2027; rig waits in Singapore with reduced crew and costs | $95.1k/day effective `[B]` | No dayrate, mobilisation amount, idle cost or option rate stated `[?]`. Nordic Financial (Newsweb) did not have it yet at ~07:30 UTC |
| New announcements | Nordic Financial `search_filings` (newsweb, ENH, 2026) and the MFN list, 17 Oct | None since 25 Sep | FinancialFilings not available (quota) |
| Consensus | Yahoo epsCurrentYear 1.17, epsForward 0.80 (as-of date not shown) | Context only | Stale `[?]`; not used |
| SOFR path | SR3Z26 95.77, SR3Z27 95.195 (2 Oct, via `docs/capt-analysis.md`) | 4.23% / 4.81% → 7.7% / 8.3% all-in | 25 days old at 27 Oct, not refreshed (effect on SED < 0.1 pp) |

**Oldest inputs:** Q2 2026 accounts (period ended 30 Jun 2026, published 26 Aug). The 2023 Seadrill transaction is used as a sensitivity only.

| Source | Date | Used for |
|---|---|---|
| SED Q2 2026 report (FinancialFilings 57589577) | 26 Aug 2026 | Accounts, balance sheet, cash flow, segments, debt |
| SED Q2 2026 presentation (57589578) | 26 Aug 2026 | Contracts, backlog |
| SED company presentation, Pareto conference (60293174) | 17 Sep 2026 | Fleet, build years, SPS, firm ends, option rates, tender market |
| SED/Ventura transaction presentation (60323742) | 11 Sep 2026 | Terms, adjustments, pro forma illustration, opex |
| Q2 distribution notice (59472184) | 4 Sep 2026 | Ex-date 9 Nov, payment ~13 Nov |
| EGM minutes (60646254); board change (62019849) | 22 / 25 Sep 2026 | Resolutions; chair change |
| [MFN — SED Energy Holdings release list and calendar](https://mfn.se/a/energy-holdings) | Read 17 Oct 2026; re-read 27 Oct | No release from 25 Sep to 27 Oct; Q3 report 18 Nov |
| [MFN — Energy Drilling receives letter of award for 30-month drilling campaign for T-16](https://mfn.se/a/energy-holdings/energy-holdings-energy-drilling-receives-letter-of-award-for-30-month-drilling-campaign-for-t-16) | 27 Oct 2026, 07:00 | T-16 Phase 7 terms, Phase 6 end, idle period |
| Nordic Financial (Newsweb stream, ENH) | Read 17 Oct 2026; 27 Oct | No new announcement on 17 Oct; the T-16 release not yet in the stream on 27 Oct |
| [Nordnet / TDN Finans — "Rigg: Fearnley venter at begrenset kapasitet gir positive markedsutsikter"](https://www.nordnet.no/market/news/c16de1cb-1ea8-4800-8860-eb1089b03a90) `[E]` | 20 Oct 2026, 08:57 | Fearnley ratings and targets (SED Buy, NOK 8.0); sector view. Market check only |
| MFN release list (re-read) and Yahoo (ENH.OL 6.55, VTURA.OL 33.9, NOK=X 9.40) | 20 Oct 2026 | No new release; market check |
| [Offshore Magazine — Seadrill selling three tender-assist rigs](https://www.offshore-mag.com/rigs/article/14295397/seadrill-selling-three-tenderassist-rigs); [Hellenic Shipping News](https://www.hellenicshippingnews.com/?p=989461) | Jun 2023 | ~$85m for T-15, T-16, West Vencedor |
| Splash247 / IndexBox; Freight & Barrels; Undervalued & Undercovered; Norwaystocks `[C]` | Sep–Oct 2026 | PTTEP–Foresight, call notes, closing condition (carried) |
| Yahoo (ENH.OL, VTURA.OL, NOK=X) | 16 Oct 2026 | Price, FX, shares, consensus fields |
| Yahoo (ENH.OL 6.80, VTURA.OL 32.9, NOK=X 9.32); Norges Bank USD/NOK fixing | 26 Oct 2026 | Price, FX, deal spread (27 Oct update) |
| `docs/rig-market-bbb.md` | 10 Oct 2026 (updates 13, 17, 22 and 24 Oct) | Tender-assist and SE Asia rows, asset-value convention, transaction check, catalysts |
| `docs/oil-market-bbb.md` | 17 Oct 2026 (24 Oct baseline checked: paths unchanged) | Background |
