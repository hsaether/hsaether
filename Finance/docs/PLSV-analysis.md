# Paratus Energy Services (PLSV) — IAF analysis, 19 Oct 2026 (stub Q4 2026 + 2027–2029)

> **No longer tracked (25 Oct 2026, user decision).** This version of 19 Oct is the last one. It
> is not updated by the update chain and its figures will go stale. It stays in the folder as a
> source: the Borr, Rig and Supply baselines cite it for the Fontis seller credit and the Seagems
> fleet data.

Skill revisions used: **iaf-valuation 2026-10-18.2** (backlog at exit with a 2-year cap, exit-consistency test, exit cross-check against Equity BBB, Bear/Bull in NOK on the Equity BBB path, holdco G&A outside NAV), **equity-market-bbb 2026-10-18.6** (exit reference and NOK path read only). Sector inputs:
- `docs/supply-market-bbb.md`: baseline **17 Oct 2026** (Final, stale after 9 Nov), supply-market-bbb rev 2026-10-10.3. The **Brazil PLSV row is now on a 100% basis** (corrected from the 5 Oct row after this analysis flagged it) and is used directly. Its **mid-cycle was re-anchored to 215 / 250 / 285** (was the equivalent of 244 / 285 / 326). Also used: 25-year economic life, the value convention and the scenario catalysts.
- `docs/rig-market-bbb.md`: baseline 10 Oct 2026 (Final, stale after 9 Nov), rig-market-bbb rev 2026-10-08.2, small updates 13 and 17 Oct (rev 2026-10-10.1, paths unchanged). High-spec jackup rates, MCU and the **new fully costed asset-value convention** are used for the seller credit (collateral ~$155m at maturity at Base mid-cycle against a $237m credit). No own rig view.
- `docs/oil-market-bbb.md`: baseline 17 Oct 2026 (Final, stale after 16 Nov), rev 2026-10-11.1. Brent Base 88 / 77 / 72 (2027 raised from 85), Bear 65 / 60 / 60, Bull 118 / 102 / 90. Used only through the Supply and Rig scenarios.
- `docs/hy-market-bbb.md` (17 Oct, data 18 Oct), rev 2026-10-18.2: Bear Nordic HY spread for the June 2029 bond refinancing. Paratus is not on its watchlist.
- `docs/equity-market-bbb.md` (17 Oct, amended 18 Oct): Oslo exit P/E, exit P/B and mid-cycle return for the exit cross-check; USD/NOK path for the Bear/Bull NOK figures. Nothing else is taken from it.
- oil-shipping-bbb, defense-market-bbb and ai-market-bbb are not used.

## Summary

**Verdict: fails, clearly.**
- **Base:** IRR_T is **0.6%** against k = 12%. The hurdle price P_k is **NOK 37.45** against a price of **NOK 47.75**, so the **margin of safety is −21.6%** (5 Oct: −10.4%).
  - The cash yield is high (d = 17.6%), but about a third of the dividend is borrowed. Value per share falls from the price to V_T NOK 21.6 by 2029: the share trades at **1.39x NAV_0**, and NAV falls 13.5% a year as the fleet ages and today's contract premium runs off.
- **Bear breaks the thesis outright:** the equity is worth nothing at exit. Net debt ($577m) exceeds asset value ($504m). IRR is −66%, and ~71% of the capital is lost even after the dividends received. The June 2029 bond maturity falls at ~5.5x EBITDA after a seller-credit default.
- **Bull:** IRR 16.0%, P_k NOK 52.1. The price already reflects ~70% of the Bull upside.
- **What the price needs:** no single assumption clears 12%. Today's $285k as the permanent mid-cycle gives 7.4%; a 30-year life 9.0%; the management case 8.5%. Life 30 years plus exit fleet values 10% above the mark gives 12.4%. Or a price at or below **~NOK 37**.
- **Change since 5 Oct (6.9% → 0.6%):**
  - Supply BBB cut the PLSV Base mid-cycle from $285k to $250k: **−6.8 pp**.
  - The price rose 1.7%, and the NOK firmed 2.0% against the USD: −1.7 pp.
  - Holding-company G&A is no longer deducted in NAV (IAF 2026-10-18.2): +2.0 pp.
  - The other method changes (backlog cap, third-party vessel out of NAV_0) net to about zero.
- **Exit cross-check:** V_T is 14.8x normalised FCF (after the fleet-renewal charge, before holdco G&A) against Oslo's 11.5x, and 0.54x book against the index's 1.75x. The high P/E comes from the renewal charge on a mid-life fleet, not from a generous mark. At the Oslo mid-cycle return (9.1%) instead of the 8% asset rate, Base is −1.2%.

**Decision table**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (19 Oct 2026 → 31 Dec 2029) | −65.7% | **+0.6%** | +16.0% |
| IRR_T in NOK on the Equity BBB NOK path | −63.4% | +0.6% (spot flat) | +14.7% |
| V_T per share (NOK) | **0.00** (assets $504m < net debt $577m) | **21.55** | 42.12 |
| P_k (hurdle price) / margin of safety | 12.45 / −73.9% | **37.45 / −21.6%** | 52.12 / +9.1% |
| Capital preserved? ΣD_t + V_T vs P = 47.75 | **No: 13.8 (−71%)** | Barely: 48.5 (+1.5% nominal over 3.2 years) | Yes: 69.5 (+46%) |
| Cumulative Maintenance FCF per share, Q4-26 to 2029 (NOK) | 10.86 | **20.33** | 25.33 |
| Net debt per share at exit (NOK; excl. seller credit) | 33.36 | **23.33** | 19.10 |
| Balance-sheet line | Seller credit defaults after Jan-28 (recovery $50m). The June 2029 maturity needs the full $250m tap plus $149m at 11% at 5.5x EBITDA: **restructuring risk** | Leverage 1.6x → **2.3x** (net of the seller credit); $221m of the 2031 tap used at the 2029 maturity | Seller credit repaid Jan-28 and used to call 2029 bonds; leverage 1.45x |

**Per-share path** (NOK per share; 162.735m shares; USD/NOK 9.4078)

| | Stub Q4-26 | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| **Base** EBITDA, $m (NOK/share) | 45.4 (2.62) | 170.2 (9.84) | 175.1 (10.12) | 176.2 (10.19) |
| Base Maintenance FCF | 1.53 | 6.23 | 6.75 | 5.82 |
| Base debt amortisation (Seagems, 50%) | 0.19 | 0.75 | 0.49 | 0.17 |
| Base FCF after debt service | 1.34 | 5.47 | 6.26 | 5.65 |
| Base D_t (paid) | 2.07 | 8.28 | 8.28 | 8.28 |
| Base net debt, excl. seller credit (net of it) | 30.99 (17.29) | 33.04 (19.34) | 34.58 (20.88) | 23.33 (23.33) |
| Base V_t | 32.83 | 26.07 | 26.44 | **21.55** |
| Bear Maintenance FCF / V_t | 1.53 / 32.83 | 5.69 / 9.00 | 2.46 / 0.84 | 1.18 / **0.00** |
| Bull Maintenance FCF / V_t | 1.53 / 32.83 | 6.69 / 32.06 | 8.09 / 41.18 | 9.00 / **42.12** |

- Maintenance FCF = EBITDA − tax − net interest (incl. seller-credit income) − maintenance capex, before Seagems debt amortisation.
- End-of-stub marks are identical in all scenarios (Base mid-cycle; no PLSV market mark exists). V_t then glides to each scenario's mid-cycle at exit.
- **Base FCF after debt service (NOK 5.5–6.3 a year) does not cover the NOK 8.28 dividend.** The gap is borrowed.

---

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value · `[E]` external or secondary · `[C]` carried from the 5 Oct version · `[A]` own assumption · `[?]` not found.

## Header

| Item | Value |
|---|---|
| Company | Paratus Energy Services Ltd. (Bermuda), Euronext Oslo: **PLSV**, ISIN BMG6904D1083. Holding company owning **50% of Seagems** (six PLSVs on Petrobras contracts in Brazil; JV partner Sapura Energy). Fontis (five jackups, Mexico) sold to a Borr Drilling/CME JV, closed 29 Jul 2026; Archer stake sold Sep 2025 |
| Price (P) | **NOK 47.75**, close 19 Oct 2026, 14:25 UTC (Yahoo `PLSV.OL`; previous close 48.50; 52-week range 38.10–52.50) |
| Valuation date / exit date | **19 Oct 2026** / 31 Dec 2029, **T = 3.20 years** |
| Shares | **162.735m** outstanding (169.55m issued less 6.815m treasury) `[F]` (Q2 note 10; Yahoo `sharesOutstanding` 162,735,049 on 19 Oct, unchanged). No dilutive options. $75m buyback authority unused; no buybacks assumed |
| FX | USD/NOK **9.4078** (Yahoo `NOK=X`, 15-min bar 14:15–14:30 UTC 19 Oct, at the price time stamp). Cross-check: Norges Bank fixing 19 Oct **9.4036** (−0.04%). P = **$5.076**. Held constant (decision at spot) |
| Market cap / EV | NOK 7.77bn = **$826m**. Net debt (Paratus + 50% Seagems) **$527m excl. the seller credit, $290m net of it** at 30 Sep `[C, A: Q3E]`; taken as net debt at the valuation date (19 days of Q4 cash flow, ~$5m, ignored). EV ≈ **$1,116m** with the seller credit netted → EV / 2026E EBITDA ($178m) **6.3x**; EV / 2027E Base ($170m) 6.6x |
| NAV at today's market marks | Omitted: no secondhand PLSV sale exists `[?]`. Book cross-check: Seagems PP&E $1,120m at 100% ($187m a vessel) `[F]` |
| **NAV_0** (Base mid-cycle marks, firm-today contracts only) | Fleet at Base mid-cycle $809m + firm-contract premium $74m + seller credit $237m − net debt $527m = **$594m = NOK 34.31 → P/NAV_0 1.39**. Bear NOK 18.62 (2.56); Bull NOK 49.47 (0.97). Holdco G&A is not deducted (IAF rule); the third-party vessel is not firm and not in NAV_0 |
| Track | **B**: finite-life vessels, contract roll-over in 2027–28, a secured credit on drilling rigs, leverage. FCF basis, year-by-year IRR, P vs P_k |
| k | **12%**, not raised. One customer (Petrobras), one asset class and a 50/50 JV without control would justify 13%. That is shown in the sensitivity (P_k −0.7 NOK) and not built in, because the verdict does not depend on it. Liquidity ~0.23m shares a day (~NOK 11m) is adequate |
| Horizon | Stub Q4-26 (Q3-26 ended before the valuation date, unreported, and is in the 30 Sep net debt); 2027 by quarter; 2028–2029 annual |
| Basis | **Management reporting**: 50% of Seagems proportionally consolidated plus the Paratus holdco. US GAAP books Seagems under the equity method; the dividend capacity is Seagems' distributions (it "distributes all excess cash" `[F]`) |

**Sources (connector · document · period):**
- **FinancialFilings** (company id 6589), read 5 Oct `[C]`: Q2 2026 interim report (61117358) and presentation (57967166); Q1 2026 presentation (47877277, FY2026 guidance); Fontis sale announcement and deck (33016728, 59255648); bond call and redemption notices (59414601, 59976693); Petrobras tender update 18 Sep (60329825); Q2 dividend notice (57967180); board change (61117360); 2024 annual report (5877807, fleet table).
- **New-event check on 19 Oct:** FinancialFilings `filings_list` failed (429, monthly credit limit used up). Fallbacks:
  - Nordic Financial Newsweb stream (`source="newsweb"`, ticker PLSV, 2026): newest item still the 23 Sep re-upload of the Q2 report. No award, share issue or new report since.
  - Yahoo share count unchanged (162,735,049).
- **Nordic Financial** (Newsweb): Q2-26 and Q1-26 releases (Seagems dayrates $281k Q1-26, $278k Q4-25; backlog; EDD to age 20; distributions $41.3m / $30.2m to Paratus in Q1 / Q2).
- **Yahoo:** PLSV.OL quote (19 Oct, 14:25 UTC), NOK=X 15-min bars, BORR ($4.36, −4.0% on 19 Oct). Q3 report date **27 Nov 2026** (not an estimate). Yahoo's PE and EPS fields mix USD and NOK and are not used.
- **Norges Bank API:** USD/NOK fixing 15, 16 and 19 Oct.
- **Web** `[C]`: Upstream (IHC Merwede pipelayer orders), Seabras' three 550 t PLSVs ~$800m (~$267m each).
- **Sector:** supply (17 Oct), rig (10 Oct, updated 17 Oct), oil (17 Oct), HY (17/18 Oct) and equity (17/18 Oct) baselines. No own oil, rig, PLSV or rate forecast is made here.

**Validation (skill: provenance and validation):**
- *Staleness:* price and FX are same-day. Financials are Q2 2026, the latest reported quarter (Q3 due 27 Nov). The 30 Sep net debt is an estimate carried from 5 Oct `[C, A]`. **Oldest input:** the Seagems vessel and debt data from the Q2 deck (28 Aug).
- *Units/basis:* USD reporting against a NOK price, converted at the price time stamp. Paratus basis = 50% of Seagems + holdco. Supply BBB PLSV row at 100%, applied ×50%.
- *Correction found in the 5 Oct model:* the Seagems debt amortisation (13 / 26 / 17 / 6) is at **100%**, but was applied as Paratus' 50% share (79.2 at 100% less those amounts leaves the ~$17m at end-2029 that the maturity chart shows). It is now applied at 50% (6.5 / 13 / 8.5 / 3). Amortisation moves cash and debt equally, so net debt and IRR are unaffected; only the "FCF after debt service" line changes.
- *Cross-source:* FX Yahoo vs Norges Bank −0.04%. Book equity (Yahoo `bookValue` $5.50/share, basis not verified against the Q2 balance sheet) is used only for the exit P/B and is low-confidence `[E]`.
- *Failed/limited:* FinancialFilings filing check (quota); Q3 actuals not yet out; Petrobras 2028 tender results and rates `[?]`.

## Scenario definitions

| Scenario | Catalyst (sector skill) | What it does to Paratus |
|---|---|---|
| **Base** (decision) | Supply Base: the PLSV 2028 roll at today's level (2028 $295k, 2029 $300k; utilisation 92% / 91%); **mid-cycle $250k at 88%** (between newbuild parity $205–226k and today's $285k). Oil Base (Brent 88 / 77 / 72, mid-cycle 70). Rig Base for the seller credit (jackups $105k → $115k → $120k, MCU 89–91%) | Jade bridges Aug-27 to Mar-28 at half utilisation. Then all six vessels sit on four-year contracts at $295k. The third-party PLSV adds a small margin from Apr-28. Borr/CME refinance and repay the seller credit at maturity (29 Jan 2029). DPS $0.22 a quarter is held, funded partly by debt |
| **Bear** (stress) | Supply Bear: the Brazil government transition (runoff 25 Oct, new government 1 Jan 2027) and oil Bear (Iran–USA deal + OPEC+ market share; Brent 65 / 60 / 60) cut Petrobras activity; PLSVs re-contract ~10% lower in 2028 (Jade idle); mid-cycle $215k at 82%. Rig Bear for jackups ($92k → $88k → $85k; MCU 82%) | Jade idle Aug-27 to Mar-28. PLSVs re-price at $255k with 82% / 80% utilisation. The third-party contract is not signed. The Borr/CME rig JV cannot carry 14% on $237m at Bear jackup rates: it defaults after the Jan-28 payment, and Paratus recovers **$50m** at exit (Rig BBB Bear values at the $10m floor per rig). Dividend cut to 50% of FCF after debt service from 2028 |
| **Bull** (stress) | Supply Bull: Petrobras PN 2027–31 confirms more subsea capacity; no PLSV newbuilds; 2028 roll at $335k, utilisation 96% / 95%; mid-cycle $285k at 92% (today's level holds). Rig Bull for jackups ($118k → $135k → $145k) | Jade bridged at 90% and re-contracted. Seller credit repaid early at the 14% step-up (29 Jan 2028); proceeds call $237m of the 2029 bonds at 101.9%. Dividend the higher of $0.22 and 100% of FCF after debt service |

The stub (Q4-26) is identical in all three scenarios: all six vessels are on firm Petrobras contracts and the seller credit is performing. Bear and Bull diverge from 1 Jan 2027, and in practice from Jade's expiry on 31 Jul 2027.

## Company and status

- **What Paratus is now:** a holding company whose operating asset is 50% of Seagems. Seagems owns six 550 t-class PLSVs built at IHC in 2014–2016, all on Petrobras contracts `[F]`. Paratus calls itself "the world's only pure-play PLSV company of scale". Three players manage 19 of the 20 high-spec PLSVs in Brazil, and no PLSV newbuilds are on order `[F, company]`.
- **Fleet and contracts** (2024 annual report fleet table; dayrates from the Q2-26 presentation) `[F]`:

| Vessel | Built | Current Petrobras contract | Contract end | Contractual dayrate (100%) |
|---|---|---|---|---|
| Diamante | 2014 | Apr 2025 – | **Apr 2028** | $289k |
| Topazio | 2014 | Apr 2025 – | **Apr 2028** | $289k |
| Esmeralda | 2015 | May 2025 – | **May 2028** | $269k |
| Onix | 2015 | Sep 2025 – | **Sep 2028** | $289k |
| Jade | 2015 | Jul 2024 – | **Jul 2027** | $287k |
| Rubi | 2016 | May 2025 – | **May 2028** | $287k |

  - Check: these end dates at the listed rates give ~$1.13bn of backlog at 30 Jun 2026, against the reported "~$1.1bn" `[B]`. Unexercised options, if any, are not in backlog `[?]`.
  - Dayrates include a BRL component and can move with cost escalation `[F]`. Realised average: $281k (Q1-26), $278k (Q4-25). The previous contract round averaged **$200.8k** (Q2-24) `[F]`.
- **Petrobras PLSV tender for 2028 starts** (5 lots, four-year terms): Seagems bid **Jade** and a **third-party vessel** (exclusive access, MOU with purchase option). Partial results (18 Sep) accept the third-party bid, subject to award and contracts. **Jade is not mentioned** `[F]`. No further release by 19 Oct.
- **Seagems quarterly (100%):**
  - Revenue $150m / $142m, EBITDA $96m / $87m, distributions $83m / $60m, capex $6m / $6m in Q1 / Q2-26.
  - Technical utilisation 98.3% / 93%. Q2 was hit by maintenance and incidents on Esmeralda and Jade, which are completed `[F]`.
  - Opex at 100% ≈ $72k / $77k per vessel-day `[B]`.
  - **Extended Dry-Docking** approved to age 20 for the five Panama-flagged 550 t vessels (one fewer SPS each); approval for Esmeralda is pending `[F]`. This lowers capex and docking days; it does not extend economic life (Supply BBB, life table).
- **Paratus segment figures (50% + holdco):** revenue $74.9m / $71.0m; adjusted EBITDA $45.6m / $41.5m (Q1 / Q2-26). **FY2026 guidance: revenue $285–300m, EBITDA $175–190m, capex $15–25m** `[F]`.
- **Fontis sale** (closed 29 Jul 2026) `[F]`:
  - Price $400m = $148m cash + $15m deferred (paid at closing) + a **$237m 2.5-year non-recourse seller credit** to the Borr/CME rig-owning JV.
  - The credit has a **first lien on all five rigs** and is ring-fenced. Interest 10% (months 1–12), 12% (13–18), 14% (19–30); maturity ~29 Jan 2029.
  - Plus $20m reimbursement of interim funding. Net disposal proceeds of $158.2m went to a partial call of the 2029 bonds on 16 Sep.
- **Debt after the call** `[F]`:
  - 2029 bonds **$353.5m** at 9.5%, due 27 Jun 2029.
  - 2031 bonds **$250m** at 8.125%, due 22 May 2031 (framework $500m, so **$250m of tap capacity**).
  - Seagems debt $79.2m at 100% (Paratus share $39.6m at 30 Jun), amortising to ~$17m at 100% by end-2029.
- **Distributions:** $0.22 a quarter every quarter since the 2024 IPO. Management states "a credible path to sustaining" it. Its own illustration: at $285k, 98% utilisation, opex $70–75k and ~8.5% funding, normalised FCFE is $130m = **$0.20** a quarter; a ~4% higher dayrate gives $0.22 `[F]`.
- **Management:** CFO Baton Haxhimehmedi is also interim CEO; the CEO role is open `[F]`.

## Near term: stub quarters (all scenarios)

| | Q3-26E (ended 30 Sep, unreported) `[C]` | Q4-26E |
|---|---|---|
| Firm cover | 6 of 6 vessels on Petrobras contracts (100% of days) | same |
| Dayrate / technical utilisation | $285k contractual, ~$282k realised / 97% `[A]` (Q2 93%, Q1 98.3%) | same |
| Revenue (50%) / EBITDA (incl. holdco G&A), $m | 75.5 / 45.4 | 75.5 / 45.4 |
| Tax / net interest (of which seller-credit income) / maintenance capex, $m | 4.8 / 12.7 (−4.2) / 7.0 | 4.8 / 7.1 (−5.9) / 7.0 |
| Maintenance FCF, $m (NOK/share) | 20.9 (1.21) | 26.5 (1.53) |
| Dividend declared | **$0.22 = NOK 2.07**, paid ~11 Dec 2026 `[A]` | **$0.22 = NOK 2.07**, paid ~10 Mar 2027 `[A]` |
| Net debt end of quarter, excl. / net of seller credit, $m | 527 / 290 | 536 / 299 |

- **2026E EBITDA $178m** (H1 actual 87.0 + H2 90.8) sits in the lower half of the $175–190m guidance. Opex is set at $76k a vessel-day (Q2 level) and utilisation at 97%. Consensus is not used (Yahoo fields mix currencies).
- **Net debt bridge, 30 Jun → 31 Dec 2026** ($m, Paratus + 50% Seagems, notional, Fontis excluded):
  - 30 Jun: debt 829.2 (2029 bonds 500, 2031 bonds 250, Seagems 79.2) − cash 147.7 = **681.5** `[F]`.
  - Less the Fontis cash proceeds net of costs 178.2; plus the make-whole premium 8.7; less Q3 maintenance FCF 20.9; plus the Q2 dividend 35.8 (11 Sep) → **30 Sep 526.8** (seller credit 237 → **289.8** net) `[C]`.
  - Less Q4 maintenance FCF 26.5; plus the Q3 dividend 35.8 → **31 Dec 536.1** (**299.1** net of the seller credit). Seagems amortisation (3.25 a quarter at 50%) moves debt and cash equally.
- **Dates:**
  - Brazil presidential runoff 25 Oct (Supply BBB Bear catalyst); OPEC+ 1 Nov and US midterms 3 Nov (oil and rig Bull/Bear catalysts).
  - Borr Q3 (~18 Nov, Yahoo estimate): first read on the rig JV behind the seller credit.
  - **Q3 report and Q3 dividend: 27 Nov 2026**; payment ~2 weeks later.
  - Petrobras Strategic Plan 2027–31: late Nov (Supply BBB Bull/Bear marker).
  - Formal Petrobras award for the third-party vessel and the remaining 2028 lots (Jade): pending.
  - Seller credit: rate steps to 12% on 29 Jul 2027 and 14% on 29 Jan 2028; maturity ~29 Jan 2029.
  - Jade's contract ends **31 Jul 2027**; Diamante/Topazio Apr-28, Esmeralda/Rubi May-28, Onix Sep-28.
  - 2029 bonds mature **27 Jun 2029**.

## Market input

**Supply BBB — Brazil PLSV row (17 Oct, 100% basis, used directly).** Rule: booked days at contract rates; re-priced days at the row.

| PLSV row, Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| Rate, $k/day (100%) | 285 | 275 / 285 / 295 | **255 / 295 / 335** | 250 / 300 / 345 | **215 / 250 / 285** |
| Utilisation, % | 95 | 92 / 95 / 96 | **82 / 92 / 96** | **80 / 91 / 95** | **82 / 88 / 92** |

- **Changes since 5 Oct:**
  - The row is restated to 100% (the 5 Oct row was half the real level; this analysis used it as ratios). The paths are almost the same as the 5 Oct ratio-adjusted values (2028: 255 / 295 / 335 against 254 / 295 / 336).
  - **The mid-cycle is re-anchored** from today's level to **$250k** (Base). Bear $215k ≈ newbuild parity at today's cost and the previous round plus inflation; Bull $285k = today's level. Supply BBB's reasons: the previous round averaged $200.8k; convention newbuild parity is $205–226k; no newbuild is on order because four-year terms do not finance a $350–425m vessel.
  - Supply BBB names $285k (today) and $205k (parity / previous cycle) as the alternative anchors for this analysis. Both are in the sensitivity.
- **How the row enters the model** `[A]`:
  - Vessels re-contract on four-year terms at the **2028** rate from each expiry. 2029 re-priced days stay at the 2028 rate. Utilisation follows the row each year: it carries cover gaps, and on contract days it is below Seagems' 97% technical history (a conservative reading, kept from 5 Oct).
  - Jade's open days Aug-27 to Mar-28 are priced at the 2027 row rate with a bridge utilisation of 0% / 50% / 90%. The tender update names only the third-party vessel.
- **Value convention:** Supply BBB values an 11-year-old PLSV at **$343m** at Base mid-cycle (opex $90k incl. G&A, no taxes, 8% over 14 years left). This analysis uses the same method on **Seagems' own cost and tax basis**: 99% realisation, 4.5% Brazilian revenue taxes, opex $76k plus Seagems G&A $4.7m a vessel, 10% income tax, $5.8m capex. That gives **$275m**. The company basis is sourced (Q2-26 actuals) and is the decision basis; the convention is a sensitivity (8.5%).

**Rig BBB — used for the seller credit (10 Oct baseline, fully costed asset convention since 8 Oct).** The credit is secured on Defender (2007), Courageous (2007), Intrepid (2008), Oberon (2013) and Titania FE (2014) `[F]`.

| Rig BBB input | Bear / Base / Bull | Use |
|---|---|---|
| High-spec jackup rate 2027 / 2028 / 2029, $k | 92 / 105 / 118; 88 / 115 / 135; 85 / 120 / 145 | Debt-service capacity of the Borr/CME JV. 14% on $237m = $33m a year ≈ $18k per rig-day |
| High-spec jackup MCU 2028 / mid-cycle | 82 / 91 / 94%; 82 / 88 / 92% | Same |
| Value of a 12-year-old high-spec jackup at mid-cycle, $m | **10 / 42 / 107** (was 48 / 105 / 175 on the withdrawn gross-margin method) | Collateral |
| Rig BBB reading for Paratus | The five rigs are worth **~$181m today and ~$155m at maturity (Jan 2029) at Base mid-cycle** (Bear $50m, Bull $396–462m), against $285m paid. "Collateral cover is below 1x at Base marks" | Seller-credit risk |
| Transaction check | The Fontis price ($57m a rig, Jul-26) implies **~$119k** through-life on the convention, 8% above Base mid-cycle ($110k) | Buyers price between Base and Bull |

**Seller-credit reading (updated):**
- **Debt service:** at Base 2028 conditions ($115k, 91% MCU) a rig earns ~$18k per calendar day after opex, idle cost, tax and capex on the Rig BBB parameters `[A]`. That just covers the 14% coupon. At Bear rates ($85–92k) it does not.
- **Repayment at maturity:**
  - At Base mid-cycle marks the collateral (~$155m) covers only 65% of the $237m credit.
  - At Base 2029 conditions ($120k, 91%) the same convention values the five rigs at **~$280m** `[A]` (85% LTV), close to what the JV paid.
  - **Base keeps repayment at par in Jan 2029**: Base jackup rates are above mid-cycle through 2029, and the transaction-implied rate (~$119k) says buyers pay at that level. It is no longer a comfortable assumption.
  - The two downside cases are sensitivities: repayment of only $155m (Base IRR −4.1%), and default with the Bear recovery of $50m (−14.5%).
- **Counterparty:** the JV is ring-fenced and non-recourse. Borr itself is stretched (the Borr analysis of 8 Oct gives a Base equity value of nil on the Rig BBB convention), which limits support beyond the JV.
- **Bear:** default after the Jan-28 payment. Recovery **$50m** at exit (Rig BBB Bear values at the $10m floor for each of the five rigs), against $150m on 5 Oct.

**Oil BBB:** Brent Base 88 / 77 / 72 (mid-cycle 70) supports Petrobras' pipelay plan; Bear 65 / 60 / 60 maps to Petrobras cost control (Supply Bear). Oil enters only through the Supply and Rig scenarios.

**HY BBB (Bear refinancing):** Bear Nordic HY year-end spreads are 650 bp (2028) and 520 bp (2029). With Norway +35 bp and the energy multiplier (×1.15), a June 2029 refinancing costs ~640–780 bp over a ~4% USD base, i.e. **~10.5–11.5%**. That supports the 11% used for funding beyond the 2031 tap `[A]`.

## Common assumptions (all scenarios)

| Item | Value | Source |
|---|---|---|
| Realised vs contractual rate | 99% (BRL component) | Q1-26 $281k vs list $285k `[F]` |
| Technical utilisation on firm days | 97% | 2025 ~99%, H1-26 95.7% `[F]`; `[A]` |
| Revenue taxes | 4.5% of contract revenue | Q2-26: 3.2 / 71.0 `[F]` |
| Opex | $76k per vessel-day (100%) on all days, flat in real terms; rates carry cost escalation | H1-26 $74.4k, Q2 $76.6k `[B]`; management $70–75k `[F]` |
| Seagems G&A / Paratus holdco G&A | $28m a year (100%) / $9m a year | Q1–Q2 run-rate; management ~$29m `[F]` |
| Seagems income tax | 10% of Seagems EBITDA | H1-26: 9.7 / 91.7 `[F]` |
| Maintenance capex | $17.5m a year (50%); Q4-26 $7m | Management normalised $35m (100%); 2026 guidance $15–25m `[F]` |
| Seagems debt (50%) | 7%; amortisation 6.5 (H2-26) / 13 / 8.5 / 3 | Q2 maturity chart at 100% (13 / 26 / 17 / 6), corrected to 50% `[F/B]`; rate `[A]` |
| Bonds | 2029: $353.5m at 9.5%, repaid 27 Jun 2029. 2031: $250m at 8.125%. Shortfalls funded by tapping the 2031 bonds (up to $250m) at 8.125%; beyond that at 11% (HY BBB Bear check above) | `[F]`; funding `[A]` |
| Cash | Paratus minimum $50m + Seagems cash $25.8m (50%) held; interest income 3.5% | `[A]` |
| Seller credit | Accrued at 10 / 12 / 14%. Base repaid 29 Jan 2029; Bull 29 Jan 2028; Bear defaults after the Jan-28 payment, $50m recovered at exit | Terms `[F]`; outcomes `[A]` from Rig BBB |
| Third-party PLSV | Base/Bull: $9m a year margin at 100% ($4.5m to Paratus) from Apr-28 for four years, no capex. Bear: not signed | Bid accepted `[F]`; terms `[?]`, margin `[A]` |
| Dividend | $0.22 a quarter to Q4-27 in all scenarios. From Q1-28: Base $0.22; Bear 50% of (maintenance FCF − Seagems amortisation); Bull the higher of $0.22 and 100% of it. Declared with the quarterly report, paid ~2 weeks later (Mar, Jun, Sep, Dec). The Q4-29 dividend is paid after exit and stays in V_T | Track record `[F]`; rule `[A]` |
| Interest basis | Accrual | `[A]` |

## Period tables ($m unless stated; Paratus basis; per share in NOK at 9.4078)

### Base (decision case)

| | Q4-26E | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|---|---|---|
| Revenue (50%) | 75.5 | 73.9 | 74.7 | 71.4 | 69.3 | 291.2 | 291.0 |
| EBITDA | 45.4 | 44.3 | 44.9 | 41.5 | 39.5 | 175.1 | 176.2 |
| Tax | 4.8 | 4.7 | 4.7 | 4.4 | 4.2 | 18.4 | 18.5 |
| Net interest (seller-credit income) | 7.1 (5.9) | 7.2 (5.9) | 7.2 (5.9) | 6.4 (6.7) | 6.2 (7.1) | 22.4 (32.8) | 39.5 (2.8) |
| Maintenance capex | 7.0 | 4.4 | 4.4 | 4.4 | 4.4 | 17.5 | 17.5 |
| **Maintenance FCF** ($m; NOK/share) | **26.5; 1.53** | **28.1; 1.62** | **28.6; 1.65** | **26.3; 1.52** | **24.7; 1.43** | **116.7; 6.75** | **100.7; 5.82** |
| Seagems debt amortisation (50%) | 3.25 | 3.25 | 3.25 | 3.25 | 3.25 | 8.5 | 3.0 |
| FCF after debt service ($m; NOK/share) | 23.3; 1.34 | 24.8; 1.44 | 25.4; 1.47 | 23.0; 1.33 | 21.5; 1.24 | 108.2; 6.26 | 97.7; 5.65 |
| Growth capex | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Dividend declared ($m; NOK/share) | 35.8; 2.07 | 35.8; 2.07 | 35.8; 2.07 | 35.8; 2.07 | 35.8; 2.07 | 143.2; 8.28 | 143.2; 8.28 |
| Net debt excl. seller credit, end ($m; NOK/share) | 536; 30.99 | 544; 31.44 | 551; 31.85 | 561; 32.40 | 572; 33.04 | 598; 34.58 | 404; 23.33 |
| Seller credit outstanding | 237 | 237 | 237 | 237 | 237 | 237 | 0 |
| Net debt net of seller credit | 299 | 307 | 314 | 324 | 335 | 361 | 404 |

- 2027: EBITDA $170m (Jade at half utilisation from Aug). Maintenance FCF $108m = **NOK 6.23 a share against NOK 8.28 paid**.
- 2028–29: re-contracting at $295k and 92% / 91% holds EBITDA at ~$175m. The seller credit adds $33m of income in 2028 and then ends.
- **The $0.22 dividend is not covered in Base.** FCF after debt service is $98–108m a year against $143m of dividends. Net debt net of the seller credit rises from $290m to $404m; leverage from 1.6x to **2.3x** EBITDA, and $221m of the 2031 tap is used at the 2029 maturity.

### Bear (lines equal to Base through Q2-27 are not repeated)

| | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|
| Revenue (50%) | 67.1 | 62.9 | 245.2 | 221.1 |
| EBITDA | 37.4 | 33.3 | 127.7 | 105.0 |
| Net interest (seller-credit income) | 6.4 (6.7) | 6.3 (7.1) | 54.0 (2.4) | 55.6 (0) |
| **Maintenance FCF** ($m; NOK/share) | **22.6; 1.31** | **19.1; 1.10** | **42.6; 2.46** | **20.4; 1.18** |
| FCF after debt service ($m; NOK/share) | 19.4; 1.12 | 15.9; 0.92 | 34.1; 1.97 | 17.4; 1.01 |
| Dividend declared ($m; NOK/share) | 35.8; 2.07 | 35.8; 2.07 | 17.0; 0.98 | 8.7; 0.50 |
| Seller credit | performing | performing | defaults after the Jan-28 payment; marked at $50m | $50m recovered at exit |
| Net debt excl. seller credit, end ($m; NOK/share) | 564; 32.62 | 581; 33.58 | 589; 34.06 | 577; 33.36 |
| Funding | — | tap $33m | tap $58m | tap $250m (full) + **$149m at 11%** |

### Bull (lines equal to Base through Q2-27 are not repeated)

| | Q3-27 | Q4-27 | 2028 | 2029 |
|---|---|---|---|---|
| Revenue (50%) | 75.1 | 75.0 | 328.7 | 345.0 |
| EBITDA | 45.0 | 44.9 | 210.8 | 227.8 |
| **Maintenance FCF** ($m; NOK/share) | **29.5; 1.71** | **29.6; 1.71** | **140.0; 8.09** | **155.7; 9.00** |
| FCF after debt service ($m; NOK/share) | 26.3; 1.52 | 26.4; 1.53 | 131.5; 7.60 | 152.7; 8.83 |
| Dividend declared ($m; NOK/share) | 35.8; 2.07 | 35.8; 2.07 | 145.5; 8.41 | 152.7; 8.83 |
| Other | — | — | −4.5 (call premium, $237m of 2029 bonds at 101.9%) | — |
| Net debt (seller credit repaid Jan-28), end ($m; NOK/share) | 557; 32.22 | 564; 32.58 | 335; 19.34 | 330; 19.10 |

### Year-end path per share (NOK; D_t = dividends paid in the period)

V_t is NAV by the V_T method: the Seagems fleet (50%) at mid-cycle marks for its age, plus the contract premium (firm-today contracts; from end-2028 also the scenario's new four-year contracts, capped at 2 years after the date), the third-party contract once started, the seller credit, less net debt. Holdco G&A is not deducted. Marks glide from the Base mid-cycle at end-2026 (no market mark exists) to each scenario's mid-cycle at exit, by thirds. End-of-stub marks are the same in all scenarios. Negative equity is shown as 0 (limited liability).

| | | Stub (to 31 Dec 26) | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| **Base** | D_t | 2.07 | 8.28 | 8.28 | 8.28 |
| | V_t | 32.83 | 26.07 | 26.44 | **21.55** |
| | r_t | −26.9% (mark vs price, not annualised) | +4.6% | +33.2% | +12.9% |
| | IRR to t | n.m. (0.20 yr) | −22.7% | −3.2% | **+0.6%** |
| **Bear** | D_t | 2.07 | 8.28 | 2.93 | 0.49 |
| | V_t | 32.83 | 9.00 | 0.84 | **0.00** |
| | r_t | −26.9% | −47.4% | −58.1% | −42.1% |
| | IRR to t | n.m. | −60.9% | −66.3% | **−65.7%** |
| **Bull** | D_t | 2.07 | 8.28 | 8.30 | 8.77 |
| | V_t | 32.83 | 32.06 | 41.18 | **42.12** |
| | r_t | −26.9% | +22.9% | +54.3% | +23.6% |
| | IRR to t | n.m. | −10.5% | +13.0% | **+16.0%** |

- **Base:** the end-2026 mark is 31% below the price: the share prices the fleet near today's $285k, the mark uses the $250k mid-cycle. The 17% cash yield is then eaten by ageing and by dividends paid out of the balance sheet. 2028 looks strong only because the new four-year contracts enter the premium when they start.
- **Bear:** the loss builds through 2027–28: lower mid-cycle marks, the seller-credit default and rising leverage. By end-2028 equity is almost gone.
- **Bull:** mostly a re-mark of fleet values; cash returns are steady.

## V_T bridge, Base ($m and NOK/share)

| Step | $m | NOK/share |
|---|---|---|
| Price P | 826.0 | 47.75 |
| Re-rating P → NAV_0 (P/NAV_0 1.39; the price assumed to fall to NAV by exit, −9.8% a year) | −232.5 | −13.44 |
| **NAV_0 (19 Oct 2026)**: fleet at Base mid-cycle 809.0 + firm-contract premium 74.4 + seller credit 237.0 − net debt 526.8 | **593.5** | **34.31** |
| + Value created by growth capex | 0 | 0 |
| − Ageing of the fleet at Base mid-cycle marks (809.0 → 685.5) | −123.5 | −7.14 |
| − Firm-contract premium roll-off (all current contracts end by Sep-28: 74.4 → 0) | −74.4 | −4.30 |
| + Scenario-signed backlog at exit: new four-year contracts (2028 signings at $295k), capped at end-2031 | +83.7 | +4.84 |
| + Scenario-signed backlog at exit: third-party PLSV margin, capped at end-2031 | +7.2 | +0.42 |
| ± Reversion tail (exit consistency) | 0 | 0 |
| + Retained cash: Σ maintenance FCF 351.6 − Σ dividends paid 465.4 (= −Δ net debt net of the seller credit, 289.8 → 403.6) | −113.8 | −6.58 |
| **= V_T (31 Dec 2029): assets 776.4 − net debt 403.6** | **372.8** | **21.55** |

The bridge closes exactly (model check = 0). The seller credit is repaid in Jan 2029, so it moves from an asset to cash inside net debt. Ageing, premium roll-off and the borrowed part of the dividend (−NOK 18.0) outweigh the new contracts (+NOK 5.3).

**Exit asset values ($m, Paratus 50%) `[A]`:**

| Asset | Bear | Base | Bull | Method |
|---|---|---|---|---|
| Seagems fleet (6 PLSVs, ages 13.5–15.5) | 406.6 | 685.5 | 954.8 | Per vessel: (mid-cycle rate × 99% × utilisation × 365 × (1 − 4.5%) − opex $76k × 365 − Seagems G&A $4.7m) × (1 − 10% tax) − capex $5.8m, × 8% annuity over the life left to 25 years (Supply BBB convention) |
| Firm-today contract premium after 2029 | 0 | 0 | 0 | All current contracts end by Sep-28 |
| Scenario-signed backlog premium (new four-year contracts, cap end-2031) | 47.8 | 83.7 | 96.8 | (2028 rate × 99% × 2029 row utilisation − mid-cycle rate × 99% × mid-cycle utilisation) × (1 − 4.5%) × (1 − 10%), 6 vessels, 2 years, PV 8% |
| Third-party PLSV contract (cap end-2031) | 0 | 7.2 | 7.2 | $4.5m a year after 10% tax, 2 years, PV 8% (not signed in Bear) |
| Seller credit (Bear: recovery in cash at exit) | 50.0 | 0 (repaid Jan-29) | 0 (repaid Jan-28) | Rig BBB Bear values at the floor |
| Reversion tail | 0 | 0 | 0 | No test: all days under backlog to the cap (table below) |
| **Total assets** | **504.4** | **776.4** | **1,058.8** | |
| Net debt at exit (excl. seller credit) | 577.1 | 403.6 | 330.3 | Model |
| **V_T ($m / NOK per share)** | **−72.6 → 0 / 0.00** | **372.8 / 21.55** | **728.5 / 42.12** | |

- **Per vessel (100%):** annual cash flow at mid-cycle $19.8m (Bear) / **$33.4m (Base)** / $46.5m (Bull). Base value **$275m at age 11 (14 years left)** and ~$228m on average at exit. At today's $285k the same vessel is worth $354m.
- **Replacement-cost check:** Seabras ordered its first three 550 t PLSVs for ~$267m each (2012) `[E]`; Supply BBB puts today's cost at ~$346–425m `[A]`. The Base mark of $275m for an 11-year-old vessel is ~1.5x Seagems' book value ($187m) and close to 2012 cost. **The market price implies ~$347m a vessel** (market cap + net debt net of the seller credit − firm premium = $1,041m, ÷ 3 vessel-equivalents at 50%), against the Base mark of ~$270m. That is about the value at today's $285k ($354m at age 11): the share prices today's rate as if it were the mid-cycle, or a longer life.
- No exit multiple is used, and the IAF ceiling is not used as an exit.

**Backlog at exit (IAF Step 3):**
- *Firm today:* none runs past exit (Onix, the last, ends Sep-28).
- *Signed in the scenario:* the six four-year contracts from the 2028 roll (Apr–Sep 2028 to Apr–Sep 2032) and the third-party vessel (Apr-28 to Mar-32). They are counted for **2 years after exit (to end-2031)**, at the scenario's 2028 signing rate. Beyond the cap the days are open at mid-cycle.
- The premium is mostly **rate** in this case (295 vs 250 in Base); utilisation is held at the row's 2029 level (91%) against the 88% mid-cycle, a conservative reading for contracted vessels `[A]`.
- **Sensitivity, firm-today contracts only (no scenario-signed backlog):** IRR_T Bear −65.7% / **Base −4.3%** / Bull 12.2%; P_k 12.45 / **33.79** / 47.93.

**Exit consistency (Year-3 vs mid-cycle, open days after T):**

| Row | Scenario | Year 3 (2029): rate; rate × utilisation | Mid-cycle: rate; rate × utilisation | Gap (rate; earnings) | Open days 2030–31 | Treatment |
|---|---|---|---|---|---|---|
| Brazil PLSV (6 Seagems vessels) | Bear | 255 (2028 signing); 204 | 215; 176 | +19%; +16% | **none**: all six on four-year contracts to Apr–Sep 2032 | **No test** (under backlog to the cap) |
| | **Base** | 295; 268 | 250; 220 | +18%; +22% | none | **No test** |
| | Bull | 335; 318 | 285; 262 | +18%; +21% | none | **No test** |

- **No reversion tail** in any scenario. The gaps are carried by the capped backlog premium instead; after end-2031 the vessels earn mid-cycle. Without the scenario-signed backlog, the open-day gaps would be material in all three scenarios and need a tail of about the same size: a tail and the premium are two routes to the same value, so the firm-today-only sensitivity above is the relevant other treatment.

**Exit cross-check against the equity market (Step 3):**

| | Bear | **Base** | Bull |
|---|---|---|---|
| V_T ($m) | 0 (−72.6 before the floor) | **372.8** | 728.5 |
| Normalised Maintenance FCF at the scenario mid-cycle, before holdco G&A ($m) | 4.3 | **63.8** | 109.0 |
| FCF_normalised (after the fleet-renewal charge), before holdco G&A ($m) | −18.6 | **25.2** | 55.3 |
| Holdco G&A, not in NAV (IAF rule) ($m a year) | 9 | **9** | 9 |
| **Exit P/E** on FCF_normalised before holdco G&A (Maintenance FCF basis in brackets) | n.m. | **14.8x (5.8x)** | 13.2x (6.7x) |
| Book equity at exit ($m; $895m at 30 Jun `[E, Yahoo]` + earnings − dividends; D&A $41m a year `[A]`) | 566 | **689** | 762 |
| **Exit P/B** | 0.00 | **0.54** | 0.96 |
| **Buyer's implied return at exit** (Supply BBB asset rate on the marks; equity return higher at ~52% net debt to assets in Base) | ~8% (equity wiped) | **~8%** | ~8% |
| Oslo index (Equity BBB): exit P/E / exit P/B / mid-cycle return | 10.5 / 1.48 / 8.2% | **11.5 / 1.75 / 9.1%** | 12.5 / 1.97 / 9.4% |
| Sensitivity: exit marks at the index mid-cycle return instead of 8% (IRR_T / P_k) | −65.7% / 12.45 | **−1.2% / 36.06** | 13.8% / 49.69 |

- **Exit P/E above the index (14.8x vs 11.5x) is not a generous mark.** Normalised FCF carries a renewal charge of $38.5m a year (one year of Base ageing). On maintenance FCF before that charge the exit is 5.8x. A mid-life fleet valued above book wears out fast in cash terms; the index's P/E is on earnings after depreciation of mostly younger, longer-lived assets.
- **Exit P/B 0.54** is far below the index (1.75): the Base marks put the fleet below its 2029 book. The book figure is low-confidence (Yahoo basis unverified; Fontis sale result not checked).
- **The buyer's return (8%) is below the Oslo mid-cycle return (9.1%)**, so the exit is a little generous against the stock market. At 9.1% Base falls to −1.2%.

## Growth capex test (Step 4)

| Item | Capex in horizon | Evidence for ROIC_g | ROIC_g | vs k | Value at T vs capex |
|---|---|---|---|---|---|
| Third-party PLSV (chartered in, Petrobras 2028 lot) | 0 (charter; purchase option not modelled) | Bid accepted, terms not disclosed `[?]` | n.a. (no capital) | — | +$7m at T (not in NAV_0: not firm) |
| Use of Fontis proceeds | $158m to redeem 2029 bonds at 105.9% | Saves the 9.5% coupon | ~9.5% before the premium | **< k** (deleveraging, not growth) | Neutral to NAV |

- There is **no growth capex** in the horizon. Management is exploring PLSV/subsea acquisitions, third-party charters and partnerships `[F]`. None is modelled; any one would need ROIC_g > 12% after dilution to help.
- The Fontis sale crystallised $400m but left $237m (59%) as a credit to a highly levered buyer group. On the Rig BBB convention the collateral is worth ~$155–181m at Base mid-cycle, against $237m. That is the main capital-allocation risk in the structure.

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (exit 31 Dec 2029) | −65.7% | **+0.6%** | +16.0% |
| IRR_T in NOK on the Equity BBB NOK path (USD/NOK Bear +12% / +9% / +9%, Bull −3%) | −63.4% | +0.6% | +14.7% |
| d / g / c | 9.0% / n.m. (V_T = 0) / n.m. | **17.6% / −22.0% / +5.0 pp** | 17.9% / −3.8% / +2.0 pp |
| g: re-rating / NAV growth (P/NAV_0) | −25.5% / n.m. (2.56) | **−9.8% / −13.5% (1.39)** | +1.1% / −4.9% (0.97) |
| Structural IRR / cyclical (pp; Δd, Δg) | −74.3% / +8.6 (+0.5, 0.0) | **−8.9% / +9.5 (0.0, +12.9)** | 8.8% / +7.2 (+0.3, +8.1) |
| ΣD_t / V_T (NOK) | 13.8 / 0.0 | **26.9 / 21.6** | 27.4 / 42.1 |
| **P_k (hurdle price) / margin of safety** | 12.45 / −73.9% | **37.45 / −21.6%** | 52.12 / +9.1% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | n.m. (FCF_normalised negative) vs negative | **50.9x vs 0.4x** | 17.8x vs 11.1x |
| Capital preserved? ΣD_t + V_T vs P = 47.75 | **No: 13.8, −71%** | Barely: 48.5 (+1.5% nominal over 3.2 years) | Yes: 69.5 (+46%) |

**Notes on the results:**
- **Structural runs:** every re-priced day from 1 Jan 2027 (Jade from Aug-27, the rest from their 2028 expiries) is set at the scenario's own mid-cycle rate and utilisation. Firm days, the stub, the seller credit and the exit fleet marks are unchanged. The scenario-signed backlog at exit is re-priced to mid-cycle, so its premium falls to zero; the reversion tail is zero.
  - **Base: the cycle is worth +9.5 pp, all through g.** The 2028 roll at $295k is 18% above the Base mid-cycle, and the contracts carry that premium past exit. The dividend is fixed, so Δd is nil.
  - **Bear and Bull are mostly mid-cycle shifts:** their structural IRRs differ from Base structural by −65 pp and +18 pp. Bear's cyclical part is n.m. (V_T is zero in both runs).
- **c = +5.0 pp in Base** is outside the usual ±2 pp. A high cash yield is paid early while value falls 22% a year, so the simple d + g understates the compounded return. The dividend dates were checked; c is timing, not a source of return.
- **Re-rating:** P/NAV_0 is 1.39, outside 0.95–1.05. Of g (−22.0% a year), −9.8% is the price assumed to fall to NAV by exit and −13.5% is NAV decline.
- **FCF_normalised (Base):** mid-cycle Seagems EBITDA $130.5m (six vessels at $250k × 88%, opex $76k, Seagems G&A) − holdco G&A 9 − tax 13.1 − interest on exit net debt 36.2 − maintenance capex 17.5 = $54.8m, less a renewal charge of **$38.5m** (ageing $123.5m ÷ 3.20) = **$16.2m = $0.10/share → 50.9x** against a 0.4x ceiling. Without the renewal charge it is 15.1x.
- **Scenario-weighted reference (convention, 25/50/25 on the levels D_t and V_T):** IRR −2.4%, P_k NOK 34.9. Not the decision figure.
- **Bull priced:** (47.75 − 37.45) / (52.12 − 37.45) = **70%**. The price already pays for most of the Bull case.
- **NOK path (Equity BBB):** decision at spot USD/NOK 9.41. On the Equity BBB path a weaker krone lifts the NOK value of Bear dividends (−65.7% → −63.4%; V_T is zero either way). A firmer krone trims Bull (16.0% → 14.7%). Base is the same (spot flat).

**Bear — balance-sheet survival:**
- EBITDA falls to $128m (2028) and $105m (2029). The seller credit stops paying after Jan-28. Net debt stays at ~$580–590m excl. the credit, **4.6x (2028) and 5.5x (2029) EBITDA**.
- **The 27 Jun 2029 maturity ($353.5m)** needs the full $250m tap plus **$149m of new debt** (11%, consistent with HY BBB Bear spreads of 520–650 bp, Norway and energy adjusted). There are no seller-credit proceeds; only the $50m recovery, later.
- At 5.5x EBITDA and Bear fleet marks of ~$407m against ~$577m of net debt, that refinancing is unlikely on market terms. **A restructuring (bondholders taking the Seagems stake, or a deeply dilutive equity raise) is the realistic outcome.**
- Dividends fall to NOK ~1.0 a share in 2028 and ~0.5 in 2029.
- **Bear breaks the thesis: the equity is worth nothing at exit; ~71% of capital is lost** after NOK 13.8 of dividends (~68% in NOK on the Equity BBB path).

### Sensitivity (Base, unless stated)

| Change | IRR_T | P_k (NOK) |
|---|---|---|
| Base | 0.6% | 37.45 |
| Exit fleet value × 0.8 / 0.9 | −7.1% / −3.0% | 31.93 / 34.69 |
| Exit fleet value × 1.1 / 1.2 | +4.0% / +7.1% | 40.20 / 42.96 |
| **Vessel life 30 years** (instead of 25) | **+9.0%** | **44.71** |
| Mid-cycle utilisation 95% (Seagems' contracted history, instead of 88%) | +4.6% | 40.72 |
| **Mid-cycle $285k** (today's level; Supply BBB alternative anchor) | **+7.4%** | **43.21** |
| Mid-cycle $205k (newbuild parity / previous cycle; Supply BBB alternative anchor) | −10.3% | 30.04 |
| Supply BBB value convention ($90k opex incl. G&A, no revenue or income tax) | +8.5% | 44.30 |
| **Management case** (98% technical utilisation, opex $72.5k, +4% on re-pricing, Jade bridged at 90%, 95% utilisation on re-priced days and at mid-cycle) | **+8.5%** | **44.32** |
| Jade idle Aug-27 to Mar-28 | −0.3% | 36.75 |
| No third-party vessel contract | −0.1% | 36.85 |
| **Seller credit repaid only $155m at maturity** (Rig BBB Base collateral) | **−4.1%** | **33.94** |
| **Seller credit defaults inside Base** (Bear recovery $50m) | **−14.5%** | **27.76** |
| Backlog at exit: firm-today contracts only | −4.3% | 33.79 |
| Exit marks at the Oslo mid-cycle return (9.1%) | −1.2% | 36.06 |
| k = 10% / 13% / 14% | — | 38.98 / 36.72 / 36.02 |

**Exit fleet value × economic life, Base IRR_T %:**

| Fleet factor \ life | 25 years (Base) | 27.5 years | 30 years |
|---|---|---|---|
| × 0.8 | −7.1 | −2.5 | 1.0 |
| × 0.9 | −3.0 | 1.7 | 5.2 |
| × 1.0 | **0.6** | 5.4 | 9.0 |
| × 1.1 | 4.0 | 8.8 | **12.4** |

- **The mid-cycle rate and vessel life decide the verdict; nothing on its own clears 12%.** Each $10k on the mid-cycle moves the IRR ~2 pp; each 2.5 years of life ~4 pp; 10% on the exit fleet ~3.5 pp.
- **The seller credit is now the largest single downside inside Base**: a partial repayment at the Rig BBB collateral value costs ~5 pp, a default ~15 pp.
- The dividend policy barely moves the IRR (cash paid or retained is counted once); it moves leverage.

## Verdict

- **Fails (margin of safety −21.6%, threshold −2%).** Base IRR_T is **0.6%** against k = 12%; P = NOK 47.75 against P_k = **NOK 37.45**. Rule 3 fails by a wide margin (50.9x vs 0.4x).
- **Bear breaks the thesis outright.** The equity is worth nothing at exit (IRR −66%, ~71% of capital lost after dividends). Lower PLSV re-contracting meets a seller-credit default ($50m recovery) and the June 2029 bond maturity at ~5.5x leverage.
- **Bull** returns 16% a year; the price already reflects ~70% of it.
- **Why Base fails despite a 17% dividend yield:**
  - **The yield is not covered.** Base FCF after debt service is NOK 5.5–6.3 a share a year against NOK 8.28 paid; the gap is borrowed (net debt net of the seller credit $290m → $404m).
  - **The share trades at 1.39x NAV_0.** The price values the fleet near today's $285k as if it were permanent (~$347m a vessel). Supply BBB now puts the mid-cycle at $250k, between newbuild parity and today.
  - **The fleet ages and today's premium runs off.** NAV falls 13.5% a year: ageing −NOK 7.1, premium roll-off −NOK 4.3, partly offset by the 2028 roll above mid-cycle (+NOK 5.3).
  - **The seller credit** (29% of market cap) is secured on rigs worth ~$155–181m at Base mid-cycle. Repayment at par is the Base, but it no longer has collateral cover at mid-cycle marks.
- **What would flip the verdict:**
  - Up: evidence that $285k is the mid-cycle (the 2028 roll at or above $300k with a firm Petrobras PN 2027–31; Bull); evidence that PLSVs earn to 30 years (Petrobras accepting 20+-year-old units on four-year terms); together these give ~12–16%. Or the price at or below **~NOK 37**.
  - Down: Jade not re-contracted; any sign of stress in the Borr/CME rig JV (missed interest, jackup MCU < 88%, Mexico payment delays); the dividend held at $0.22 while leverage passes 2.5x.

**Caveat:** this is a margin-of-safety screen, not an intrinsic valuation or a price target. P_k is the price at which the Base path returns exactly 12%.

## Tracking

| Date | Event | Actual vs model | Base P_k (NOK) | Margin of safety | Ahead / behind Base |
|---|---|---|---|---|---|
| 5 Oct 2026 | First analysis (iaf-valuation 2026-10-05.1) | — | 42.0 | −10.4% (P 46.95) | — |
| 19 Oct 2026 | Re-run: IAF 2026-10-18.2, Supply BBB 17 Oct (PLSV row at 100%, mid-cycle $250k), Rig BBB convention for the collateral. No company news since 23 Sep; Q3 not yet reported | No quarter reported since 5 Oct | **37.45** | **−21.6%** (P 47.75) | On path (no data) |

**P_k bridge, 5 Oct → 19 Oct (NOK):**

| Step | Base IRR_T | P_k |
|---|---|---|
| 5 Oct (as published) | 6.9% | 42.0 |
| Rebuilt model at 5 Oct price, FX and mid-cycle ($285k), with the 2-year backlog cap, third-party out of NAV_0 and the Seagems amortisation corrected | 7.1% | 42.3 |
| Price 46.95 → 47.75 and USD/NOK 9.604 → 9.408 (USD flows worth 2.0% less in NOK) | 5.4% | 41.4 |
| Holdco G&A no longer deducted in NAV (+$45m at exit) | 7.4% | 43.2 |
| **Supply BBB mid-cycle $285k → $250k** (fleet marks −$196m at exit; larger backlog premium +$54m) | **0.6%** | **37.45** |

The seller-credit reading changed in Bear only (recovery $150m → $50m); the Base still assumes repayment at par.

## Risks and signposts

| Signpost | Bear | Base | Bull | Now |
|---|---|---|---|---|
| Petrobras 2028 PLSV tender: Jade | Jade not awarded; no extension | Bridge/extension, four-year contract from 2028 | Jade awarded or extended at ≥ $285k | Third-party vessel accepted (18 Sep); Jade not mentioned; nothing new by 19 Oct |
| Re-contracting rates (Diamante, Topazio, Esmeralda, Rubi Apr–May 2028; Onix Sep 2028), 100% | < $255k | $270–310k (Supply BBB Base signpost) | > $310k | Current $269–289k |
| PLSV mid-cycle evidence | Next round below $250k; any PLSV newbuild order at ≤ $350m | Roll at ~$295k, no newbuilds | Roll ≥ $330k and no newbuilds | Supply BBB mid-cycle $250k (17 Oct) |
| Seagems technical utilisation (quarterly) | < 93% | 95–97% | ≥ 98% | Q2 93%, Q1 98.3% |
| Q3 report (27 Nov): EBITDA (50% + holdco) / dividend | < $43m / DPS cut | $44–47m / $0.22 | > $48m / $0.22 + buyback | Q2 $41.5m |
| Seller credit: Borr/CME rig JV (Borr Q3 ~18 Nov; Rig BBB jackup MCU and Mexico cell) | Missed interest at the 14% step (Jan-28); MCU < 88%; Borr stress | Interest paid; refinanced by Jan-29 | Early repayment at the Jan-28 step-up | 3 of 5 rigs contracted (Jul); Mexico improving; BORR $4.36 (−4% on 19 Oct) |
| Brazil transition and Petrobras PN 2027–31 (runoff 25 Oct; plan late Nov) | New board re-scopes; E&P/subsea capex cut > 10% | Plan holds | More subsea capacity and PLSV demand | PN 2026–30 |
| Oil (Oil BBB) | Iran–USA deal + OPEC+ market share (Brent < $70 on Dec-27) | Armed normalisation | Renewed strikes after 3 Nov | Brent front ~$110 (17 Oct) |
| Leverage and 2029 refinancing | > 3x and no seller-credit proceeds | ~2.0–2.3x, tap used | < 1.6x | 1.6x (net of the seller credit) |
| CEO appointment / capital allocation | Value-destructive M&A or newbuild order | Steady-state payout | Accretive charter-in growth | CFO is interim CEO |

**Other risks:**
- Petrobras concentration (100% of revenue), Brazilian revenue taxes and BRL indexation.
- JV governance: 50/50 with Sapura Energy, which went through restructuring `[?]`; distributions require JV agreement (current policy: all excess cash).
- Vessel age limits in future Petrobras tenders `[?]`; EDD approval for Esmeralda pending.
- Holding-company structure: Paratus' only cash sources are Seagems distributions and seller-credit interest.

## For other modules

- **Supply Market BBB:**
  1. The 17 Oct row restatement (100% basis) and the Seagems vessel table are adopted here; **no correction needed** to the paths.
  2. **PLSV value convention:** the row's convention ($90k opex incl. G&A, no taxes) gives $343m for an 11-year-old vessel. Seagems' own basis adds 4.5% Brazilian revenue taxes, 10% income tax and 99% realisation, and gives $275m. Brazil revenue taxes are a cash cost for every Petrobras charter. Consider adding them to the PLSV (and Brazil OSV) value convention, or stating that the convention is pre-tax.
  3. PLSV utilisation on contract: the row's 91–92% for 2028–29 sits below Seagems' 97% technical history for fully contracted vessels. A note on what the row's utilisation includes (cover gaps vs technical downtime) would help company analyses.
- **Rig Market BBB:** the collateral reading requested on 10 Oct is done (Base repayment at par kept, with partial repayment and default as sensitivities; Bear recovery $50m). No change needed.
- **HY Market BBB:** Paratus is not on the watchlist. Candidate: Paratus 2029 bonds ($353.5m, 9.5%, due Jun 2029) and 2031 bonds ($250m, 8.125%). In Bear the 2029 maturity falls at ~5.5x EBITDA after a seller-credit default (energy / oil-service row).
- **Oil Market BBB / Equity BBB:** no change needed.

## Change log

- **19 Oct 2026:** re-run under **iaf-valuation 2026-10-18.2**, with Supply BBB (17 Oct), Rig BBB (10 Oct, updated 17 Oct), Oil BBB (17 Oct), HY BBB (17/18 Oct) and Equity BBB (17/18 Oct). Price NOK 47.75 and USD/NOK 9.4078 (19 Oct). Result: **fails** (Base IRR 0.6%, P_k NOK 37.45, margin of safety −21.6%).
  - **Method (IAF):** Summary first; holdco G&A outside NAV (+$45m at exit); third-party vessel out of NAV_0 (not firm); scenario-signed backlog capped at 2 years after exit (the 5 Oct version counted the new contracts to 2032); exit-consistency table (no test: all days under backlog); exit cross-check against Equity BBB; Bear/Bull IRR in NOK on the Equity BBB path; per-share lines in the period tables.
  - **Inputs:** Supply BBB PLSV row used directly at 100%; **mid-cycle $285k → $250k** (Bear 244 → 215, Bull 326 → 285); Rig BBB fully costed jackup values, so the Bear seller-credit recovery is $150m → $50m and the Base collateral reading is weaker; HY BBB Bear spreads support the 11% refinancing rate.
  - **Model correction:** Seagems amortisation applied at 50% (it was the 100% figure); no effect on net debt or IRR.
  - **Bear:** equity now worth nothing at exit (−37% → −66% IRR).
- **5 Oct 2026:** first Paratus analysis, under iaf-valuation rev 2026-10-05.1 with Oil BBB (4 Oct), Rig BBB (4 Oct) and Supply BBB (5 Oct, PLSV row used as ratios because of the level error). Result: **fails** (Base IRR 6.9%, P_k NOK 42.0, margin of safety −10.4%).

## Appendix: own assumptions `[A]`

| Assumption | Value | Why |
|---|---|---|
| Q3/Q4-26 EBITDA | $45.4m each | 97% utilisation at $282k realised, opex $76k; FY2026 $178m vs guidance $175–190m |
| Net debt 30 Sep | $526.8m ($289.8m net of the seller credit) | 5 Oct bridge `[C]`; Q3 not yet reported |
| Re-contracting | Four-year terms at the 2028 row rate from each expiry; utilisation per row year | Petrobras tender format (5 lots, 4 years) |
| Jade bridge | 0 / 50 / 90% utilisation Aug-27 to Mar-28, at the 2027 row rate | Contract ends Jul-27; tender update silent on Jade |
| Opex | $76k a vessel-day flat (real), on all days | H1-26 actual; rates carry cost escalation |
| Tax / capex / G&A | 10% of Seagems EBITDA / $17.5m a year / $28m (100%) + $9m holdco | H1-26 actuals, management normalisation |
| Seller credit outcomes | Base repaid at par Jan-29; Bull Jan-28; Bear default after the Jan-28 payment, $50m recovered at exit | Rig BBB rates, MCU and convention values (collateral ~$155m Base mid-cycle, ~$280m at Base 2029 conditions, $50m Bear) |
| Third-party PLSV margin | $9m a year at 100% from Apr-28 | Charter-in spread; terms not disclosed |
| Funding | Tap of the 2031 bonds at 8.125% up to $250m; beyond at 11% | Framework $500m; HY BBB Bear spreads |
| Dividend rule | $0.22 to Q4-27; then Base $0.22, Bear 50% of FCF after amortisation, Bull max($0.22, 100%) | Policy is a stated DPS, not a ratio |
| Fleet value | 25-year life, 8% annuity on mid-cycle cash flow per vessel, Seagems cost and tax basis | Supply BBB convention, company basis |
| Backlog premium at exit | 2028 signing rate at the 2029 row utilisation vs mid-cycle, 2 years, PV 8% | IAF Step 3 cap |
| Interim marks | Base mid-cycle at end-2026, gliding by thirds to the scenario mid-cycle at exit; negative equity shown as 0 | No PLSV market mark |
| Book equity for the exit P/B | $895m at 30 Jun (Yahoo), D&A $41m a year (50%) | Low confidence; cross-check only |

## Appendix: sources

| Source | Date | Used for |
|---|---|---|
| Paratus Q2 2026 interim report (FinancialFilings 61117358; first release 57967161) `[C]` | 28 Aug / 23 Sep 2026 | Segment P&L, balance sheet, debt, Fontis, Seagems balance sheet, shares, APM net debt |
| Paratus Q2 2026 presentation (57967166) `[C]` | 28 Aug 2026 | Seagems 100% figures, dayrates per vessel, capitalisation, maturities |
| Paratus Q1 2026 presentation (47877277) `[C]` | 29 May 2026 | FY2026 guidance |
| Fontis sale announcement and deck (33016728, 59255648) `[C]` | 23–24 Mar 2026 | Buyer, consideration, seller-credit terms and security, management's DPS illustration |
| 2029 bond call and redemption notices (59414601, 59976693) `[C]` | 1 and 14 Sep 2026 | $146.46m redeemed at 105.947%, $353.5m outstanding |
| Petrobras tender update (60329825) `[C]` | 18 Sep 2026 | Third-party vessel accepted; MOU with purchase option |
| Paratus 2024 annual report (5877807) `[C]` | 30 Apr 2025 | Fleet table: build years, contract periods |
| Nordic Financial, Newsweb stream (PLSV, 2026), checked 19 Oct | to 23 Sep 2026 | No new releases; Q1/Q2 release text (EDD, distributions, dayrates) |
| FinancialFilings `filings_list` | 19 Oct 2026 | **Failed** (429, monthly credit limit) |
| Yahoo (PLSV.OL 14:25 UTC, NOK=X 15-min bars, BORR) | 19 Oct 2026 | Price, FX at the price time stamp, share count, report date, book value |
| Norges Bank API (EXR B.USD.NOK.SP) | 15–19 Oct 2026 | USD/NOK fixing 9.4036 (cross-check) |
| [Upstream — IHC Merwede pipelayer orders](https://www.upstreamonline.com/epaper/1143388/ihc-merwede-confirms-usd-13bn-pipelayer-orders) `[C]` | 2012 | PLSV newbuild cost anchor `[E]` |
| `docs/supply-market-bbb.md` | 17 Oct 2026 | PLSV row (100%), mid-cycle and anchors, value convention, life, scenarios |
| `docs/rig-market-bbb.md` | 10 Oct 2026 (updated 17 Oct) | Jackup rates, MCU, convention values, collateral reading |
| `docs/oil-market-bbb.md` | 17 Oct 2026 | Scenario mapping |
| `docs/hy-market-bbb.md` | 17 Oct 2026 (data 18 Oct) | Bear spreads for the 2029 refinancing |
| `docs/equity-market-bbb.md` | 17 Oct 2026 (amended 18 Oct) | Oslo exit P/E, P/B, mid-cycle return; USD/NOK path |
