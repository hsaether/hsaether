# Rheinmetall AG (RHM) — IAF analysis, stub Q3–Q4 2026 + 2027–2029

Skill revisions used: **iaf-valuation 2026-10-07.1**. Sector inputs:
- `docs/defense-market-bbb.md`, initial baseline 7 Oct 2026, produced with defense-market-bbb rev
  **2026-10-07.3**. Supplies the segment order and revenue paths per scenario, the long-end CAGRs
  2030–35, the steady-state margins and the capacity balance. No own defense market forecast is made
  here.
- `docs/hy-market-bbb.md` is not used: Rheinmetall has no Nordic HY bonds, and it needs no
  refinancing in Bear (see Bear balance-sheet survival). Oil, rig, supply and shipping baselines are
  not used.

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value ·
`[E]` external or secondary · `[A]` own assumption · `[?]` not found.

## Header

| Item | Value |
|---|---|
| Company | Rheinmetall AG (Düsseldorf), Xetra: RHM, ISIN DE0007030009. Pure defense group from 2026: the civil business (Power Systems) is a discontinued operation, sale to AEQUITA signed June 2026, closing expected Q4 2026 `[F]` |
| Price (P) | **€926.20**, Xetra close 7 Oct 2026 (Yahoo `RHM.DE`, last trade 15:38 UTC). 52-week range €923.30–1,966; at its 52-week low |
| Valuation date / exit date | 7 Oct 2026 / 31 Dec 2029, **T = 3.24 years** |
| Shares | **46,789,567** issued after the last convertible conversion (early July 2026) `[F]` (H1 report, note 13). Treasury shares (€4m at cost) ignored. No convertible left; no buyback programme |
| Market cap / EV | €43.3bn. EV ≈ €47.2bn: plus net financial debt ≈ €3.05bn at the valuation date `[A, end-Q3E]` and minorities at book €0.80bn `[F]`. Pensions net out against plan surpluses (provisions €295m vs net plan assets €302m) `[F]` |
| P/E | 28.5x on Base 2026E adjusted EPS €32.5; 24.9x on consensus €37.25 (19 analysts); 17.4x on consensus 2027 €53.2 (Yahoo `earningsTrend`) |
| NAVs (Step 3) | **NAV at today's market marks: not applicable.** Rheinmetall has no tradeable asset marks. **NAV_0 (Base) €154/share** = the 2026 business at Base steady-state segment margins, valued by the V_T method, less net debt at the valuation date. **P/NAV_0 = 6.0x.** Bear €86, Bull €224 |
| FX | All figures in EUR, the reporting and trading currency. No conversion needed |
| Track | **B** (dated IRR, P vs P_k). Defense is normally Track A, but the skill's exception applies: H1 operating FCF was −€1.6bn on a working-capital build, capex runs at 8–9% of sales during the capacity build (new ammunition, powder and rocket-motor plants), and a €3.7bn Arminius advance arrives in 2027. Track A rules are reported as a cross-check |
| k | **12%**, not raised. Leverage is low (net financial debt peaks around €3bn, about 1x operating result). Liquidity is high (192k shares a day ≈ €180m). The backlog is spread over five segments and many countries. Concentration on the German customer (38% of H1 sales) is flagged as a risk, not priced through k |
| Horizon | Stub Q3-26 (ended, unreported; report 5 Nov) + Q4-26; 2027 by quarter; 2028–2029 annual |

**Sources (connector · document · period):**
- **FinancialFilings** (company id 356):
  - Half-yearly financial report 2026 (filing 49986481, published 6 Aug 2026), period ended 30 Jun
    2026: segment figures, backlog, guidance, balance sheet, cash flow, NVL purchase price
    allocation, discontinued operations, events after the reporting date (F126 write-off €2,153m,
    last conversion, RAST buy-out €81m, Aschau €350m).
  - Structured FY2025 and FY2024 line items (`companies_financials_retrieve`): FY2025 sales €9,935m,
    operating result €1,840m, earnings from continuing operations €1,176m, NCI ≈ €139m.
  - `filings_list` checked on 7 Oct 2026. Newest filings are directors' dealings: CEO Papperger
    buy ≈ €0.5m (29 Sep) and Georgi foundation buy ≈ €0.24m (2 Oct). No share issue after the July
    conversion and no new report since 6 Aug.
- **Yahoo:** price, 52-week range, shares, consensus (`earningsTrend`: Q3-26 revenue €3.16bn from 3
  analysts; Q4-26 €5.56bn from 2; FY26 EPS €37.25 and revenue €13.92bn; FY27 EPS €53.2 and revenue
  €18.54bn), and the next report date of 5 Nov 2026.
- **Web (company call and press, `[E]`):**
  - Investing.com transcript of the Q2 call (6 Aug): capex 8–9% of sales; firm share of backlog
    70%; year-end backlog target €100–120bn; Naval 2030 ambition €5bn at ≈15%; plant start dates.
  - Arminius coverage (boerse-express, defence-industry.eu, calibredefence): Rheinmetall share of
    the firm order ≈ €12.4bn; 30% advance (> €3bn); Bundestag decision 9 Dec 2026.
  - CMD 18 Nov 2025 (Bloomberg, Börsen-Zeitung): 2030 ambition of ≈ €50bn sales, operating margin
    > 20%, cash conversion > 50%.
  - ad-hoc-news (Sep–Oct 2026): insider buying, Deutsche Bank target €1,800.
- **Sector:** `docs/defense-market-bbb.md` (7 Oct 2026): segment Bear/Base/Bull paths, long-end
  CAGRs, steady-state margins, capacity balance, signposts.

## Scenario definitions (from Defense Market BBB, 7 Oct 2026)

| Scenario | Catalyst | What it does to Rheinmetall |
|---|---|---|
| **Base** (decision) | Funded national plans executed with haircuts (Germany 95%, France slips a year; Italy, Spain and the UK stay below their pledges). The war continues or freezes; the US partly draws down | Market segments grow per the Base row (land 18/14/10%, ammunition 15/5/0%, air defense 25/18/14%, C4ISR 14/12/10%, naval 9/10/10%) plus named, backlog-backed share gains for Rheinmetall. Ammunition scarcity margins fade from 29.5% to 21% by 2029 and 16% at steady state. Group sales €22.1bn in 2029 (CAGR 16.6%) |
| **Bear** (stress) | Ukraine ceasefire plus fiscal stress (OAT–Bund > 120 bp, gilts > 5.5%), US "buy American" pressure, execution failures of the F126 type; ammunition overcapacity. Earliest: 2027 budgets | Ammunition revenue falls 10–15% a year from 2028, land flattens, margins drop 2–4 pp. Half of the Base share gains survive (firm backlog). Group sales peak at €16.2bn in 2028 |
| **Bull** (stress) | US drawdown ≥ 25,000 troops (Pentagon recommendation early Nov 2026) plus Russian escalation on NATO territory; SAFE 2 or defense Eurobonds | Faster ramp-up, Europe replaces US enablers; capacity caps volume, so margins hold longer (ammunition 24% in 2029, 20% steady state). Group sales €25.2bn in 2029 |

The stub (Q3–Q4 2026) is the same in all scenarios: it rests on H1 actuals, firm backlog and
guidance. Bear and Bull diverge from 1 Jan 2027. The Arminius contract and its advance are in all
three scenarios. The award is due on 9 Dec, before any Bear catalyst can act, and is funded from the
debt-brake exemption.

## Company and status

- **Segments since 1 Jan 2026** `[F]`: Vehicle Systems, Weapon and Ammunition, Air Defence and
  Digital Systems (the last two split out of Electronic Solutions), plus Naval Systems since NVL was
  acquired (27 Feb 2026; price €1.52bn, goodwill €820m).
- **Corporate changes 2026** `[F]`:
  - The civil business is held for sale. The provisional price is €350m; a further €212m impairment
    was booked in June; closing is expected in Q4 2026.
  - Majority stake in DOK-ING (unmanned ground vehicles, 51%), end-June; consolidated from July. 100% of RAST (Saudi
    simulation) for €81m cash, July.
  - The 2030 convertible was fully converted (+787k shares). A €500m bond (2031, 3.375%) was
    issued, and a €1.0bn club loan (12-month tenor) refinanced NVL.
- **F126:** Germany cancelled the frigate programme at the end of June. Rheinmetall's subcontract
  was terminated in mid-July and **€2,153m of Naval order backlog was written off** `[F]`. 2026 sales
  guidance was cut by €0.3bn, and the Naval margin guidance to 10–11%.
- **Dividend:** €11.50 for FY2025 (≈ 47% of adjusted EPS), paid 15 May 2026, so already paid and
  not counted. The payout is modelled at 40% of adjusted attributable EPS `[A]` (history 39–47%).

### H1 2026 by segment (€m, continuing operations) `[F]`

| Segment | Sales H1-26 | Growth y/y | Operating result | Margin | Nomination H1 | Backlog 30/6 (firm / frame) | OFCF H1 |
|---|---|---|---|---|---|---|---|
| Vehicle Systems | 2,431 | +28% | 275 | 11.3% | 6,691 | 28,829 (24,729 / 4,090) | −557 |
| Weapon and Ammunition | 1,757 | +33% | 417 | 23.7% | 3,097 | 25,274 (13,932 / 11,342) | −370 |
| Air Defence | 478 | +62% | 76 | 16.0% | 1,534 | 4,218 (4,218 / –) | −408 |
| Digital Systems | 820 | +24% | 63 | 7.7% | 4,702 | 20,646 (11,951 / 8,694) | −105 |
| Naval Systems (Mar–Jun) | 334 | n.a. | 33 | 9.8% | 1,004 | 6,255 (6,255 / –); **4,102 after the F126 write-off** | −166 |
| Others / consolidation | −592 | | −77 | | | | −10 |
| **Group** | **5,227** | **+39%** (organic +30%) | **786** | **15.0%** | **16,238** | **80,467 (56,343 firm / 24,124 frame)** | **−1,616** |

- Q2 alone: sales €3,289m (+69%), operating result €562m (17.1%).
- Group backlog is about 70% firm `[F/E]`. After the F126 write-off it is ≈ €78.3bn, of which
  ≈ €54.2bn firm `[B]`.
- Backlog with NATO members and partners is 94.9% `[F]`.
- **Balance sheet 30 Jun 2026** `[F]`:
  - Net financial debt (continuing, including leases) **€2,722m**, against net cash of €369m at
    31 Dec 2025.
  - Debt: club loan €999m, term loans €550m, bond €496m, Schuldschein €328m (a further €129m
    repaid in July), CP €30m, other €192m, plus leases.
  - Inventories €6.25bn (from €4.72bn); contract liabilities (advances) €6.27bn.
  - Equity €5.77bn, of which minorities €0.80bn.
- **Working capital** (inventories + contract assets + receivables − payables − contract
  liabilities) rose from €0.76bn (7.6% of sales, YE2025) to €2.27bn (≈ 20% of LTM sales) at
  30 June. That build is the −€1.6bn H1 OFCF.
- **Minorities:** 18.5% of H1 continuing earnings (€84m of €455m) and ≈ 12% in FY2025. The JVs
  (RBSL, Rheinmetall MAN, Hungary, ammunition JVs) are material. **15% is modelled `[A]`.**

### Guidance 2026 (H1 report, 6 Aug) `[F]`

| | Sales | Operating margin |
|---|---|---|
| Group | €13.7–14.2bn (organic +28–31%) | ≈ 19% |
| Vehicle Systems | €5.9–6.0bn | 12–13% |
| Weapon and Ammunition | €4.9–5.0bn | 29–30% |
| Air Defence | €0.9–1.0bn | ≈ 19% |
| Digital Systems | €2.2–2.3bn | ≈ 12% |
| Naval Systems | €1.0–1.2bn (cut from €1.3bn) | 10–11% (cut from 11–13%) |
| Cash conversion | 100% of operating result | |

- The guidance is heavily H2-weighted. It implies H2 sales of €8.7bn and an operating result of
  €1.87bn (21.4%), and Weapon and Ammunition must run at ≈ 32% in H2.
- 100% cash conversion implies H2 OFCF of ≈ +€4.3bn. That is reachable only if the Arminius
  advance (≥ €3bn) lands in December.

## Near term: stub quarters (all scenarios)

| €bn | Q3-26E (ended, unreported) | Q4-26E | FY2026E | Consensus |
|---|---|---|---|---|
| Sales | 3.15 | 5.57 | 13.95 (guide midpoint) | Q3 3.16; Q4 5.56; FY 13.92 |
| Operating result (margin) | 0.58 (18.4%) | 1.28 (23.0%) | 2.65 (19.0%) | — |
| Operating FCF | −0.25 | +1.90 | +0.03 (H1 −1.62) | — |
| Arminius advance | — | 0 in Base (timing: assumed Jan 2027) | — | Management: "end-2026 / early 2027" |
| Civil business sale | — | +0.30 `[A]` (€350m provisional, less adjustments) | | |
| Net financial debt at period end | **3.05** (incl. RAST −0.08) | **0.85** | | |
| Adjusted EPS | — | — | **€32.5** | €37.25 |

- Q3 and Q4 sales follow the consensus split. The margin uses guidance; OFCF is `[A]`. The H2
  working-capital release assumes YE2026 working capital at 10% of sales (YE2025: 7.6%).
- **Without the Arminius advance, FY2026 cash conversion is about 0%, against 100% guided.** This
  is the near-term test on 5 Nov (Q3) and in the FY report (March 2027). If the advance arrives
  before 31 Dec, YE net debt is ≈ −€2.9bn (net cash). That is timing only and leaves the IRR
  unchanged.
- Base EPS (€32.5) is below consensus (€37.25) mainly because of minorities (15% vs ≈ 10%
  implied) and interest on the higher net debt.
- **Dates:** Q3 report 5 Nov 2026. Bundestag Arminius decision 9 Dec. FY2026 report around
  mid-March 2027. AGM around 12 May 2027, dividend paid ≈ 15 May 2027 (ex-date one business day
  after the AGM) `[A]`.
- **Net debt at the valuation date ≈ €3.05bn `[A]`;** at 31 Dec 2026 €0.85bn (Base, all
  scenarios).

### Year 1 by quarter (Base, €bn) `[A]`

| | Q1-27 | Q2-27 | Q3-27 | Q4-27 | 2027 |
|---|---|---|---|---|---|
| Sales (seasonality 16/23/24/37%) | 2.77 | 3.98 | 4.15 | 6.40 | 17.29 |
| Operating result | 0.39 | 0.68 | 0.75 | 1.31 | 3.13 |
| Operating FCF (incl. Arminius advance €3.72bn in Q1) | +2.72 | −0.80 | −0.22 | +3.30 | 5.00 |
| Dividend to RHM shareholders (€13.00/share, 15 May) | — | 0.61 | — | — | 0.61 |
| Distributions to minorities | — | 0.17 | 0.17 | — | 0.34 |
| Net financial debt, period end | −1.87 | −0.29 | 0.10 | −3.20 | −3.20 |

Bear and Bull change 2027 only through sales growth and margins (period tables below); the
quarterly pattern is the same.

## Market input (Defense Market BBB rows used and how they enter)

| Rheinmetall segment | Baseline row | Market revenue growth 2027 / 28 / 29, Bear · Base · Bull | Rheinmetall share gain, pp (Base and Bull full, Bear half) | Basis for the share gain | Steady-state margin: baseline row → Rheinmetall (Bear / Base / Bull) |
|---|---|---|---|---|---|
| Vehicle Systems | Land systems | 12/5/−2 · 18/14/10 · 22/18/14 | +10 / +8 / +6 | Arminius (€12.4bn firm Rheinmetall share, Bundestag 9 Dec; ramp toward ≈ 1,000 Boxers a year), Puma 200 (€2bn, deliveries from mid-2028), Romania 298 Lynx (SAFE), Hungary and Italy Lynx; firm VS backlog €24.7bn = 4.2 years | 8/10/12 → **9 / 11 / 13** (+1 pp: scale in Boxer/Lynx, vertical integration) |
| Weapon and Ammunition | Ammunition and energetics | 5/−10/−15 · 15/5/0 · 22/15/8 | +7 / +1 / 0 | New capacity on line in 2027 (Unterlüß 155 mm, Lithuania 100k rounds Q2-27, Albacete > 1m medium-calibre mid-27, Aschau powder 4,500 t Q3-27) `[E]`; German frame contracts; frame backlog €11.3bn | 10/14/18 → **12 / 16 / 20** (+2 pp: own powder and energetics) |
| Air Defence | Air and missile defense | 15/8/4 · 25/18/14 · 30/25/20 | +15 / +10 / +6 | Skyranger/Skynex demand (counter-drone; H1 +62%, nomination ×6); backlog €4.2bn = 4.4 years | 12/15/17 → **13 / 16 / 18** |
| Digital Systems | C4ISR, electronics and space | 8/4/2 · 14/12/10 · 18/16/13 | +4 / +3 / +2 | TaWAN and IdZ-ES frame call-offs (frame €8.7bn), FV-014 loitering munitions, SATCOMBw/SAR satellites, UK collective training (≈ €1bn, July) | 10/12/13 → **9 / 11 / 12** (−1 pp: H1 7.7%, history below peers) |
| Naval Systems | Naval | 6/5/4 · 9/10/10 · 10/12/13 | 0 | F126 lost; the €5bn 2030 ambition is not in Base (it needs unnamed new programmes) | 5/7/8 → **7 / 9 / 10** (+2 pp: NVL ran ≈ 10%) |

- **Long end 2030–35** (baseline segment CAGRs, Bear / Base / Bull): land 1/3/4%, ammunition
  −3/−2/0%, air defense 3/6/8%, C4ISR 3/5/6%, naval 4/7/8%. Terminal growth after 2035 is
  1.5/2/2.5% `[A]`.
- **Margin glide to the steady state** (Base): ammunition 29.5% (2026) → 28 / 25 / 21% → 16%.
  Firm W&A backlog of 2.8 years locks in much of the 2027–28 pricing; surplus risk starts around
  2028 per the baseline.
- **Market check, Base revenue against company views:**
  - Base group growth is +24% / +16% / +11% (2027–29), against consensus 2027 +33% and the
    company's "30% or more a year" to 2030.
  - The CMD ambition (≈ €50bn in 2030) would be ≈ 27% of the baseline's Base European addressable
    spending in 2030 (€183bn), against ≈ 9% (€14bn of €128bn) in 2026. Base therefore does not
    contain it; it is tested as an overlay (Results, sensitivity).
- **Backlog coverage (Base):**
  - Firm backlog at YE2026E ≈ €64bn `[A]`: €54.2bn after F126, − H2 sales €8.7bn, + Arminius
    €12.4bn, + other H2 intake ≈ €6bn.
  - That is 3.7x Base 2027 sales, and Base 2027–29 cumulative sales of €59bn are 93% of it.
  - Delivery profiles are long (Arminius to ≈ 2035, Puma from mid-2028, naval into the 2030s), so
    about half of the firm backlog falls in 2027–29 `[A]`. The remainder of Base needs frame
    call-offs (€24bn frame backlog) and new orders.
  - **Base sales look well covered in 2027 and less so in 2029.**

## Common assumptions (all scenarios) `[A]`

| Item | Value | Basis |
|---|---|---|
| Group sales | 91.8% of the segment sum | 2026 guidance midpoint vs segment midpoints (internal sales) |
| Holding and other | −1.2% of group sales (2026: −1.3%) | H1 −€77m (−1.5%) |
| Tax | 27% of EBT (cash tax after the PPA deduction) | H1 26.4%; FY2025 25% |
| Minorities | 15% of earnings, fully distributed each year | H1 18.5%, FY2025 ≈ 12% |
| Payout | 40% of prior-year adjusted attributable EPS, paid 15 May | History 39–47% |
| Interest | 3.8% on net financial debt; 2% on net cash; + €20m other | H1 net interest −€46m |
| D&A (ex PPA) | 3.0% → 3.4% of sales; normalised 3.5% | H1 incl. PPA 4.5% |
| Capex | 2026 8.5%; 2027 7.0% (Bear 7.0, Bull 7.5); 2028 5.5% (4.5, 6.5); 2029 4.5% (4.0, 5.0); normalised 4.0% | Guidance 8–9% for 2026; ammunition and digitalisation build "finalised in 2027" (CMD) |
| Working capital (ex Arminius) | 10% of sales Base (Bear 12%, Bull 9%); YE2026 10% | YE2025 7.6%; 30 Jun 2026 ≈ 20% of LTM |
| Arminius advance | €3.72bn in Q1 2027 (30% × €12.4bn) `[B]`; unwinds €0.53bn a year 2028–34; the €2.66bn still outstanding at exit is deducted from V_T as debt-like | Avoids counting customer funding as value |
| Exit value V_T | 2030–35 unlevered FCF at each scenario's steady-state margins and long-end growth, plus a Gordon terminal value, discounted at k; × (1 − 15% minorities) − net debt − Arminius advance outstanding | The skill's Track B defense rule: steady-state margins and long-end growth from the baseline; sector multiples are context only |

## Period tables (€bn unless stated)

### Base (decision case)

| €bn | 2026E | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Vehicle Systems sales | 5.95 | 7.62 | 9.29 | 10.78 |
| Weapon and Ammunition sales | 4.95 | 6.04 | 6.40 | 6.40 |
| Air Defence sales | 0.95 | 1.33 | 1.70 | 2.04 |
| Digital Systems sales | 2.25 | 2.65 | 3.05 | 3.42 |
| Naval Systems sales | 1.10 | 1.20 | 1.32 | 1.45 |
| **Group sales** | **13.95** | **17.29** | **19.98** | **22.11** |
| Growth % | +40.4 | +23.9 | +15.5 | +10.7 |
| Vehicle Systems margin % | 12.5 | 12.5 | 12.0 | 11.5 |
| Weapon and Ammunition margin % | 29.5 | 28.0 | 25.0 | 21.0 |
| Air Defence margin % | 19.0 | 18.5 | 17.5 | 16.5 |
| Digital Systems margin % | 12.0 | 12.0 | 11.5 | 11.0 |
| Naval Systems margin % | 10.5 | 10.5 | 10.0 | 9.5 |
| **Operating result** | **2.65** | **3.13** | **3.26** | **3.17** |
| Margin % | 19.0 | 18.1 | 16.3 | 14.3 |
| Adjusted EPS (€) | 32.5 | 40.8 | 43.8 | 42.6 |
| Capex | 1.19 | 1.21 | 1.10 | 1.00 |
| of which growth (above 3.5% of sales) | 0.70 | 0.61 | 0.40 | 0.22 |
| Δ working capital (ex Arminius) | 0.64 | 0.33 | 0.27 | 0.21 |
| Arminius advance in / (unwind) | — | +3.72 | −0.53 | −0.53 |
| Operating FCF after tax and interest | 0.03 | 5.00 | 1.21 | 1.39 |
| Dividend paid to RHM shareholders (May) | (0.54) | 0.61 | 0.76 | 0.82 |
| D_t per share paid (€) | (11.50 paid 15 May 2026, not counted) | 13.00 | 16.31 | 17.51 |
| Distributions to minorities | — | 0.34 | 0.36 | 0.35 |
| Net financial debt, 31 Dec | 0.85 | −3.21 | −3.29 | −3.51 |
| Arminius advance outstanding | — | 3.72 | 3.19 | 2.66 |

The 2026E column combines H1 actuals with the stub. Group operating margin falls from 19% to 14.3%
by 2029: ammunition normalises while vehicles (lower margin) grow fastest. EPS peaks in 2028.

### Bear

| €bn | 2026E | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Vehicle Systems sales | 5.95 | 6.96 | 7.59 | 7.66 |
| Weapon and Ammunition sales | 4.95 | 5.37 | 4.86 | 4.13 |
| Air Defence sales | 0.95 | 1.16 | 1.32 | 1.41 |
| Digital Systems sales | 2.25 | 2.48 | 2.61 | 2.69 |
| Naval Systems sales | 1.10 | 1.17 | 1.22 | 1.27 |
| **Group sales** | **13.95** | **15.73** | **16.15** | **15.75** |
| Growth % | +40.4 | +12.7 | +2.7 | −2.5 |
| Margins % (VS / WA / AD / DS / NS) | 12.5 / 29.5 / 19 / 12 / 10.5 | 11.5 / 26 / 17 / 11 / 9 | 10.5 / 20 / 15 / 10 / 8 | 9.5 / 15 / 13 / 9.5 / 7 |
| **Operating result** | **2.65** | **2.58** | **2.13** | **1.69** |
| Margin % | 19.0 | 16.4 | 13.2 | 10.7 |
| Adjusted EPS (€) | 32.5 | 33.6 | 28.7 | 22.8 |
| Capex | 1.19 | 1.10 | 0.73 | 0.63 |
| Δ working capital (ex Arminius) | 0.64 | 0.49 | 0.05 | −0.05 |
| Operating FCF after tax and interest | 0.03 | 4.51 | 0.84 | 0.71 |
| D_t per share paid (€) | — | 13.00 | 13.43 | 11.49 |
| Net financial debt, 31 Dec | 0.85 | −2.77 | −2.75 | −2.74 |

The Arminius advance and its unwind are the same as Base.

### Bull

| €bn | 2026E | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Vehicle Systems sales | 5.95 | 7.85 | 9.90 | 11.88 |
| Weapon and Ammunition sales | 4.95 | 6.39 | 7.41 | 8.00 |
| Air Defence sales | 0.95 | 1.38 | 1.86 | 2.34 |
| Digital Systems sales | 2.25 | 2.75 | 3.27 | 3.76 |
| Naval Systems sales | 1.10 | 1.21 | 1.36 | 1.53 |
| **Group sales** | **13.95** | **17.96** | **21.83** | **25.24** |
| Growth % | +40.4 | +28.8 | +21.5 | +15.6 |
| Margins % (VS / WA / AD / DS / NS) | 12.5 / 29.5 / 19 / 12 / 10.5 | 13 / 30 / 19 / 12.5 / 10.5 | 13 / 28 / 19 / 12.5 / 10.5 | 13 / 24 / 18 / 12 / 10 |
| **Operating result** | **2.65** | **3.45** | **4.00** | **4.19** |
| Margin % | 19.0 | 19.2 | 18.3 | 16.6 |
| Adjusted EPS (€) | 32.5 | 45.1 | 53.7 | 56.2 |
| Capex | 1.19 | 1.35 | 1.42 | 1.26 |
| Δ working capital (ex Arminius) | 0.64 | 0.22 | 0.35 | 0.31 |
| Operating FCF after tax and interest | 0.03 | 5.24 | 1.42 | 1.88 |
| D_t per share paid (€) | — | 13.00 | 18.04 | 21.49 |
| Net financial debt, 31 Dec | 0.85 | −3.41 | −3.54 | −3.95 |

Even Bull 2029 EPS (€56) is close to consensus 2027 (€53). The consensus path is above Bull.

### Year-end path per share (€; D_t = dividends paid in the year)

Interim V_t are a path diagnostic only. They glide geometrically from P to each scenario's V_T, and
the end-of-stub mark (€867) is the same in all scenarios (Base glide).

| Scenario | Year-end | D_t | V_t | r_t | IRR to t |
|---|---|---|---|---|---|
| All | 2026 (stub) | 0 | 867 | −6.4% | −24.8% |
| **Base** | 2027 | 13.00 | 651 | −23.3% | −23.8% |
| | 2028 | 16.31 | 489 | −22.4% | −23.3% |
| | 2029 (exit) | 17.51 | **368** | −21.3% | **−22.9%** |
| **Bear** | 2027 | 13.00 | 504 | −40.4% | −38.0% |
| | 2028 | 13.43 | 292 | −39.3% | −38.9% |
| | 2029 (exit) | 11.49 | **170** | −37.9% | **−38.9%** |
| **Bull** | 2027 | 13.00 | 751 | −11.8% | −14.6% |
| | 2028 | 18.04 | 651 | −11.0% | −13.0% |
| | 2029 (exit) | 21.49 | **564** | −10.0% | **−12.2%** |

## V_T build and bridge

**Exit value per scenario (€bn unless stated)**

| | Bear | Base | Bull |
|---|---|---|---|
| 2030 sales (normalised) | 15.9 | 22.7 | 26.2 |
| Steady-state operating margin | 9.6% | 12.5% | 15.2% |
| NOPAT 2030 | 1.11 | 2.07 | 2.91 |
| Unlevered FCF 2030 (capex 4%, D&A 3.5%, working capital on growth) | 1.01 | 1.90 | 2.70 |
| Growth 2030–35 (mix of segment long-end CAGRs) / terminal | ≈ 0.9% / 1.5% | ≈ 2.7% / 2.0% | ≈ 3.9% / 2.5% |
| PV 2030–35 + PV terminal at k = EV_T | 4.21 + 5.05 = **9.26** | 8.18 + 11.05 = **19.23** | 11.92 + 17.61 = **29.53** |
| EV_T / NOPAT 2030 | 8.4x | 9.3x | 10.1x |
| × (1 − 15% minorities) | 7.87 | 16.35 | 25.10 |
| + net cash at exit | +2.74 | +3.51 | +3.95 |
| − Arminius advance outstanding | −2.66 | −2.66 | −2.66 |
| **Equity at exit** | **7.95** | **17.20** | **26.39** |
| **V_T per share (€)** | **170** | **368** | **564** |
| Implied P/E on normalised 2030 earnings | 8.4x | 9.8x | 10.7x |

**Why the exit multiple is low.** At k = 12% and 2–4% long-end growth, a capital-light business
converting about 92% of NOPAT to FCF is worth about 9–10x earnings. That is the price at which a
buyer in 2029 earns k thereafter. The method is independent of the IAF ceiling. Today's sector
P/E of 15–18x (baseline market check) is context only: it embeds a lower discount rate or faster
growth after 2030. See the exit P/E sensitivity.

**V_T bridge, Base (€/share):**

| Step | €/share | Comment |
|---|---|---|
| P | 926 | |
| Re-rating P → NAV_0 | −772 | NAV_0 = 2026 business (€13.95bn sales) at Base steady-state margins (operating result €1.77bn), valued by the V_T method, less net debt €3.05bn. **Re-rating −42.6% a year** |
| NAV_0 | **154** | |
| + Scale-up 2026 → 2030 at steady-state margins (after minorities) | +130 | Sales €13.95bn → €22.7bn (Base growth + share gains); attributable EV €10.2bn → €16.4bn |
| + Cash retained, valuation date → exit | +140 | Net debt €3.05bn → net cash €3.51bn (OFCF incl. the Arminius advance, less dividends and minority distributions) |
| − Arminius advance still outstanding at exit | −57 | €2.66bn of deliveries already paid for |
| **V_T** | **368** | NAV growth +30.9% a year. (1 + g) = 0.574 × 1.309 = 0.752, so **g = −24.8% a year** |

Growth is strong (NAV ×2.4) but cannot offset a price that is 6x the normalised value of today's
business.

## Growth capex test (Step 4)

| | Bear | Base | Bull |
|---|---|---|---|
| Growth capex 2026–29 (above 3.5% of sales) + working-capital build | 2.62 | 3.38 | 3.96 |
| ΔNOPAT at steady state, 2030 vs 2026 scale | 0.11 | 0.77 | 1.35 |
| **ROIC_g** | **≈ 4%** | **≈ 23%** | **≈ 34%** |
| vs k = 12% | Destroys value | Accretive | Accretive |

- **Ammunition capacity** (≈ half of 2026 capex: Unterlüß, Lithuania, Albacete, Aschau €350m):
  - Base: W&A revenue is flat at €6.4bn in 2028–29 while the margin falls to 16%. The new plants come
    on line in 2027 into the baseline's surplus window (≈ 2m shells a year in Europe by 2027), so
    ROIC_g on ammunition capacity is about k at best.
  - Bear: W&A revenue falls to €4.1bn by 2029, so the plants are stranded and ROIC_g is negative.
  - Bull is the only case where this capacity earns well above k.
- **Air defense capacity:** shortage through the window (baseline). Revenue ×2.1 by 2029 on little
  capex, so ROIC_g is far above k.
- Group ROIC_g of 23% in Base is evidence that the business itself is good. The verdict below fails
  on price, not on business quality.

## Results

| | Bear | Base | Bull |
|---|---|---|---|
| IRR_T | **−38.9%** | **−22.9%** | **−12.2%** |
| d / g / c | 1.3% / −40.8% / +0.6 pp | 1.6% / −24.8% / +0.4 pp | 1.8% / −14.2% / +0.2 pp |
| g: re-rating / NAV growth (P/NAV_0) | −52.0% / +23.4% (10.8x) | −42.6% / +30.9% (6.0x) | −35.5% / +33.0% (4.1x) |
| Structural IRR / cyclical (pp; Δd, Δg) | −41.1% / +2.2 (+0.3, +1.7) | −24.4% / +1.5 (+0.3, +1.2) | −13.2% / +1.0 (+0.3, +0.7) |
| ΣD_t / V_T (€) | 37.9 / 170 | 46.8 / 368 | 52.5 / 564 |
| P_k (hurdle price) / margin of safety | €150 / −84% | **€294 / −68%** | €434 / −53% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | 50.3x vs n.m. (IRR < 0) | 26.8x vs n.m. (IRR < 0) | 18.9x vs n.m. (IRR < 0) |
| Capital preserved? ΣD_t + V_T vs P | No: €208 vs €926 (−78%) | No: €415 vs €926 (−55%) | No: €617 vs €926 (−33%) |

**Notes to the results table**
- **Structural run:** every segment at the scenario's own steady-state margin from 1 Jan 2027 (no
  ammunition scarcity margin). The stub, revenue, exit value method and long end are unchanged.
  "Cyclical" is therefore the scarcity-margin windfall 2027–29: worth only 1–2 pp of IRR, because
  the decision is driven by the exit value, not the near-term earnings.
- **FCF_normalised** = Base 2030 unlevered FCF €1.90bn × 85% = €1.62bn = €34.5 per share (Bear
  €18.4, Bull €49.0). Normalised capex (4% of sales) exceeds D&A (3.5%), so no separate renewal
  charge is added. With IRR_T < 0 the Rule 3 ceiling is not meaningful. At IRR = k the ceiling is
  1/k = 8.3x, against 26.8x.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** IRR −22.9%, V_T €367. It never
  replaces Base.
- **Share of Bull already priced:** (P − P_k Base) / (P_k Bull − P_k Base) = (926 − 294) /
  (434 − 294) = **4.5**. The price is above even the Bull hurdle (€434), so it discounts more than
  the Bull case.
- **Track A cross-check** (constant-PE growth, the method most favourable to the price):
  - Base: EPS €32.5 (2026E) → €42.6 (2029), so g = 9.5% and d = 1.6%. d + g = **11.0% < 12%**:
    fails Rule 1. Rule 3: P/E 28.5x (2026E) or 22.7x (2027E) vs ceiling (d + g)/k² = **7.7x**:
    fails.
  - On consensus (2026 €37.25, 2027 €53.2, then +25% / +20% `[A]`): g ≈ 28.9%, ceiling 21.1x vs
    P/E 24.9x on 2026 consensus. That fails narrowly; on 2027 consensus (17.4x) it passes, but that
    mixes years. The constant-PE assumption also breaks once growth fades to 2–6% after 2030.
- **Bear balance-sheet survival:** no issue.
  - Net debt peaks at ≈ €3.05bn (Q3-26, about 1x operating result), then turns to net cash in all
    scenarios on the Arminius advance and lower capex.
  - The €1bn club loan matures by ≈ Mar 2027 and is refinanced from Q4 inflows and the advance.
    The bond is due 2031.
  - The Bear risk is a permanent loss of capital through valuation, not insolvency.

### Sensitivity (Base unless stated)

| Change | IRR_T | P_k |
|---|---|---|
| **Base** | **−22.9%** | **€294** |
| Ammunition steady-state margin 12% / 20% / 24% (Base 16%) | −24.7% / −21.1% / −19.5% | €274 / €313 / €333 |
| Terminal growth 1% / 3% / 4% (Base 2%) | −24.0% / −21.5% / −20.0% | €281 / €309 / €328 |
| Working capital 8% / 12% / 14% of sales (Base 10%) | −22.3% / −23.5% / −24.1% | €300 / €287 / €280 |
| Exit P/E 10x / 14x / 18x / 22x / 26x on normalised 2030 earnings (instead of the k-based exit) | −21.3% / −13.4% / −6.8% / −1.2% / +3.8% | €312 / €416 / €520 / €624 / €729 |
| **Company-plan overlay:** sales €18.5 / 25 / 32 / 40bn (2027–30), margin ≈ 20%; exit at 15% steady state (Bull method) | −1.2% | €624 |
| Same, 20% margin held as the steady state | +7.3% | €810 |
| CMD ambition in full: €50bn in 2030, 20–21% margin held | **+14.8%** | **€1,000** |
| CMD ambition in full, exit EV/NOPAT 12x | +20.7% | €1,175 |

**Reverse test: what does €926 require?**
- At the Base exit method (9.3x EV/NOPAT), an IRR of k needs V_T ≈ €1,281/share. That is equity of
  ≈ €60bn, EV ≈ €69.5bn and 2030 NOPAT of ≈ €7.5bn, i.e. a steady-state operating result of
  ≈ €10.2bn.
- Sales needed in 2030: **€82bn at the Base steady-state margin (12.5%), €68bn at 15%, €51bn at
  20%.**
- So the price clears k only if the CMD plan (≈ €50bn) is delivered in full **and** a 20% margin is
  the permanent steady state, not a scarcity peak.

## Verdict

- **Base fails: margin of safety −68%** (P_k €294 vs P €926; IRR_T −22.9% vs k = 12%). This is not
  marginal. Every sensitivity inside the defense baseline fails.
- **Bear does not survive:** IRR −38.9%, and ΣD + V_T covers 22% of the price. That is a permanent
  loss of capital, though with no solvency risk.
- **Bull also fails** (IRR −12.2%, P_k €434). The price sits above the Bull hurdle.
- **Why the price and the IAF diverge:**
  - The defense baseline has European addressable spending growing 10.7% a year to 2029 and then
    2.8% a year. Rheinmetall's CMD plan (≈ €50bn sales in 2030, > 20% margin) needs about 27% of
    Europe's 2030 addressable spending plus exports, and margins that the baseline treats as
    scarcity margins.
  - At k = 12%, €926 needs that plan delivered in full and the 20% margin held for good.
  - The business is good (ROIC_g 23%, a 3.7x firm backlog, a strong position in land and air
    defense); the price already embeds the company's own plan.
- **What would flip the verdict:**
  1. Evidence that 20% is a durable steady-state margin (ammunition pricing holding after the
     2027–28 capacity wave; land and air defense margins rising, not falling).
  2. Orders and revenue tracking the CMD path rather than Base: 2027 sales ≥ €18.5bn and backlog
     ≥ €100bn at YE2026 while ammunition pricing holds.
  3. A price near P_k: €294 Base, €434 Bull. Even a halving from here would only reach Bull.
- **Caveat:** this is a margin-of-safety screen at k = 12%, not an intrinsic valuation or price
  target. A lower discount rate (defense primes have trading betas around 0.5) would raise all
  values, but the skill does not allow k below 10%. At the floor of k = 10% (shown only as a
  sensitivity), Base V_T rises to €456, but IRR is still −17.8% and the hurdle price is €375, so it
  still fails by a wide margin.

## Risks and signposts

| Signpost | Bear threshold | Bull threshold | Now | Date |
|---|---|---|---|---|
| Q3 OFCF and working capital | OFCF < −€0.5bn in Q3; FY guidance cut | Q3 OFCF positive; 100% conversion confirmed ex-Arminius | H1 −€1.6bn; inventories €6.25bn | 5 Nov 2026 |
| Arminius (Boxer) | Bundestag delay or volume cut | Signed in Dec with the advance before 31 Dec; options (€12–14bn) exercised early | Final negotiations; Bundestag 9 Dec | Dec 2026 |
| W&A margin | Price cuts or idle lines (baseline Bear signpost) | > 28% held into 2028 | H1 23.7%; FY guide 29–30% (H2 ≈ 32%) | Each quarter |
| Backlog | Firm backlog falls; book-to-bill < 1 for 2 quarters | YE2026 ≥ €120bn (top of target) | €80.5bn (F126 −€2.15bn after) | FY report, Mar 2027 |
| US posture (baseline Bull catalyst) | — | ≥ 25k troops withdrawn | Review; recommendation early Nov | Nov 2026 |
| German 2027 budget (EP14) | < €100bn | > €115bn | Draft €109.7bn | Late Nov 2026 |
| Ukraine ceasefire + fiscal stress (baseline Bear catalyst) | Ceasefire signed; OAT–Bund > 120 bp | EU-financed rebuild of Ukraine's army | Talks paused; OAT–Bund 82 bp | Ongoing |
| Naval follow-up | No replacement for F126 | New frigate or corvette programme for NVL | MEKO A-200 went to TKMS | 2026–27 |
| Supply chain | China dual-use export stop bites (rare earths, chemicals) | — | Stop on Rheinmetall and 13 European firms, end-July; "not material" (several years of stock) | 2027 |
| Civil business sale | Price adjustment, or closing slips into 2027 | — | €350m provisional | Q4 2026 |

**Other risks:**
- Customer concentration: Germany is 38% of sales and 40% of H1 nomination.
- Fixed-price execution on new programmes (NVL, Arminius, Lithuania).
- Minorities taking a rising share of profits.
- IFRS 18 from 2027 changes the operating result definition, so comparability breaks.
- Key-person risk (CEO).

## For other modules

Input for `defense-market-bbb` at its next run. Nothing here changes the current baseline:
1. **Award log:**
   - Arminius: Rheinmetall's share of the firm order ≈ €12.4bn, 30% advance, Bundestag 9 Dec 2026
     `[E]`.
   - Romania SAFE package, 29 May 2026: €5.7bn nomination for Rheinmetall (Lynx, air defense,
     ammunition, 4 vessels €0.92bn) `[F]`.
   - Puma +200 (€3.5bn total, €2bn Rheinmetall) `[F]`.
   - FV-014 loitering munition frame contract (low single-digit €bn) `[F]`.
   - UK ACTS training (≈ €1bn Rheinmetall share, 15 years) `[F]`.
   - F126 subcontract: −€2.15bn Naval backlog written off, July `[F]`.
2. **Capacity table:**
   - Aschau powder: 4,500 t a year, €350m, start Q3 2027.
   - Lithuania 155 mm: 100k rounds a year, Q2 2027.
   - Albacete medium calibre: > 1m rounds a year, mid-2027.
   - Unterlüß rocket motors: Q1 2027. All `[E]`.
3. **Market signal:**
   - The CMD ambition of €50bn in 2030 sits far above the baseline Base for one supplier. Record
     it as a company view, not an input.
   - Consensus 2027 growth for Rheinmetall is +33%, against the baseline land row at +18%.
4. **Supply chain:** the China dual-use export stop on Rheinmetall and 13 other European defense
   companies (end-July 2026) is a candidate bottleneck row (rare earths, chemicals).

## Change log

- **Initial analysis (7 Oct 2026).** No previous version.
- **Method notes:**
  - Track B is used for a defense company because of the working-capital swing, the 2026–27
    capacity capex and the Arminius advance; Track A is reported as a cross-check.
  - NAV_0 for a company without asset marks is defined as the 2026 business at the scenario's
    steady-state margins, valued by the V_T method, less net debt at the valuation date.
  - The Arminius advance is treated as debt-like at exit, so customer funding is not counted as
    value.
  - Candidates for the IAF skill at its next revision.

## Appendix: own assumptions `[A]`

1. 2026: guidance midpoints for sales (€13.95bn) and margin (19%). H2 OFCF +€1.65bn ex-Arminius
   (Q3 −€0.25bn, Q4 +€1.90bn). Civil sale +€0.30bn in Q4.
2. The Arminius advance (€3.72bn) arrives in Q1 2027, the same in all scenarios. It unwinds
   linearly 2028–34.
3. Share gains over market growth per segment (see Market input), at half size in Bear.
4. Company steady-state margins = baseline steady state + a company premium (VS +1, WA +2, AD +1,
   DS −1, NS +2 pp), applied the same way to Bear and Bull.
5. Margin glide 2027–29 per the period tables. W&A Base 28/25/21%: firm W&A backlog of 2.8 years
   locks in part of the scarcity pricing.
6. Minorities 15%, fully distributed. Tax 27%. Payout 40%. Interest 3.8% on net debt.
7. Capex and working capital per Common assumptions. Normalised capex 4% vs D&A 3.5%.
8. Exit: 2030–35 explicit at steady state with the baseline long-end CAGRs; terminal growth
   1.5/2/2.5%; discounted at k = 12%.
9. Group sales = 91.8% of the segment sum; holding −1.2% of sales.
10. Year-1 quarterly seasonality 16/23/24/37%.
11. The company-plan overlay path (€18.5 / 25 / 32 / 40–50bn) is an illustration of the CMD
    ambition, not a forecast.

## Appendix: sources

| Source | Content | Period / date |
|---|---|---|
| FinancialFilings 49986481 — Rheinmetall half-yearly financial report 2026 | Segments, backlog, guidance, balance sheet, cash flow, notes 5, 6, 8, 10 and 13 | H1 2026 / 6 Aug 2026 |
| FinancialFilings `companies_financials_retrieve` (id 356) | FY2025 and FY2024 line items | FY2024–25 |
| FinancialFilings `filings_list` (id 356) | Directors' dealings 29 Sep and 2 Oct; F126 release 2 Jul; civil sale 3 Jun; no new share issues | to 7 Oct 2026 |
| Yahoo `RHM.DE` (`get_quote`, `quote_summary`) | Price, range, shares, consensus, report date | 7 Oct 2026 |
| Investing.com — Q2 2026 call transcript | Capex 8–9%, firm share 70%, backlog target, plant timings, Naval 2030 | 6 Aug 2026 `[E]` |
| boerse-express / defence-industry.eu / calibredefence | Arminius €12.4bn, advance, Bundestag 9 Dec | Sep 2026 `[E]` |
| Bloomberg / Börsen-Zeitung / Baird Maritime — CMD | €50bn 2030, > 20% margin, > 50% cash conversion, Naval €5bn | 18 Nov 2025 `[E]` |
| ad-hoc-news | Insider buys, Deutsche Bank €1,800, Arminius review | Sep–Oct 2026 `[E]` |
| `docs/defense-market-bbb.md` | Segment paths, long end, steady-state margins, capacity, signposts, peer valuation context | 7 Oct 2026 |
