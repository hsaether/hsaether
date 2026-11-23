# Scatec (SCATC) — IAF analysis, stub Q4 2026 + 2027–2029

**Version 2.1 — 21 Nov 2026** (price and FX re-mark of the v2 build of 30 Oct, after the Q3 report; Step 6b added; compacted to the lean rules, 727 lines → current state only) · price **NOK 82.40** (Oslo close 20 Nov 2026) · skills: iaf-valuation **2026-11-18.1**; inputs Equity BBB 20 Nov note (NOK path, exit references), HY BBB 18 Nov (Bear refinancing spread); no sector baseline covers renewables · **verdict: clears** (Base margin of safety +22.3%).

## Summary

**Verdict**
- **Clears.** Base IRR **19.5%** against k = 12%. P_k **NOK 100.8** against **NOK 82.40**: margin of safety **+22.3%** (v2 +13%). Clears at or below NOK 98.8; fails above NOK 102.9.
- **What moved (v2 → v2.1):** price −2.7% (84.65 → 82.40) and the krone −4.8% on Scatec's revenue basket (USD/NOK 9.19 → 9.75, I-44 106.7 → 110.7). Scatec's assets and debt are foreign-currency, so the weaker krone lifts the NOK value (+1.8 pp). With FX held at 30 Oct: Base 17.7%, +16.8%. No operating input moved; no Scatec release since Q3 except the routine coupon resets.
- **Scatec is priced below its Base NAV** (P/NAV_0 ~0.98). The return is NAV growth: project debt amortisation (NOK 24 a share by exit), projects under construction reaching COD, and D&C margins that fund much of the new equity.
- **What the price needs:** Philippine EBITDA of about **NOK 320m a year** from 2028 for k (v2 ~485m; 2026 ~1,050m; the Q4 guide runs at ~1,000m). That is below our Bear (400–450).
- **Single changes no longer take it to fails:** Philippines 450 a year +5.0%; no D&C platform value +7.2%; asset rate 10% +11.5%; contracted EBITDA −NOK 150m +12.7%.
- **Bear breaks the thesis:** IRR **−16.2%**; V_T NOK 47.5 against 82.40 (~42% permanent loss); corporate net debt NOK 8.5bn by 2029 unless growth stops.
- **Bull 37.5%** (P_k NOK 156.1).

**Base in brief**
- Contracted EBITDA ~NOK 2,350m a year (Q3–Q4 run rate ~2,450 at spot); Philippines **700 / 750 / 750** after the reserve-market suspension (Q4 guide 200–300); under construction to 680; D&C 480 / 580 / 500 on the NOK 10.5bn book; growth equity NOK 1.5bn a year (target 2bn). Asset rate 9% (contracted), 11% (Philippines).
- **Where the return comes from** (NOK a share, P 82.40 → V_T 143.4): NAV_0 ~80.6 at today's FX, then ageing −8.4, under construction +9.3, growth equity at F +36.2, amortisation +25.8, corporate debt rise −3.4 `[A, v2 bridge × FX 1.048]`.
- **Break-even:** Philippines ~NOK 320m from 2028, or an asset rate above 10% together with a second hit.

**Bear in brief**
- Story: the Philippine redesign caps reserve prices and NGCP signs nothing (SNAP 400–450); Ukraine disrupted; Egypt and South Africa delays; Pakistan true-up fails; asset rate 10% (Philippines 13%); growth equity NOK 0.9bn a year at F 0.9.
- V_T NOK 47.5; corporate NIBD NOK 8.5bn by 2029 against NOK 3.9bn of liquidity; refinance Norfund (Q1 2028) and SCATC06 (Q1 2029) at Bear spreads. Survival needs growth stopped after the committed Egypt equity (then V_T ~49.9, IRR −14.9% `[A]`).

**Decision table** (NOK per share; P = NOK 82.40, 20 Nov 2026; no dividend in any scenario)

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (20 Nov 2026 → 31 Dec 2029) | −16.2% | **19.5%** | 37.5% |
| IRR_T in NOK on the Equity BBB NOK path | −14.4% | **19.5%** (spot flat) | 36.4% |
| V_T (31 Dec 2029) | 47.5 | **143.4** | 222.1 |
| P_k / margin of safety | 33.3 / −59.5% | **100.8 / +22.3%** | 156.1 / +89.4% |
| Capital preserved? (ΣD_t + V_T vs P) | **No**, −42% | Yes | Yes |
| Cumulative maintenance FCF per share (Q4-26–2029) | 28.7 | **50.2** | 61.7 |
| Net debt per share at exit: proportionate total / corporate | 141.6 / 55.8 | **127.5 / 41.6** | 125.7 / 39.9 |
| Balance-sheet line | Corp. NIBD NOK 8.5bn by 2029; growth must stop after 2027 | Corp. NIBD NOK 6.1–6.4bn while growth runs at NOK 1.5bn a year (divestments not modelled) | Corp. NIBD NOK 6.1bn |

- Per-share figures are the v2 build × the FX factor 1.0476 `[A]` (all blocks and both debt layers are foreign-currency; corporate NOK bonds are swapped to USD).

**Per-share path** (NOK per share at today's FX; proportionate; EBITDA = power + D&C − corporate)

| Base | Q4 2026 (stub) | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| EBITDA, NOK m (per share) | 965 (6.0) | 4,000 (25.0) | 4,595 (28.7) | 4,545 (28.4) |
| Maintenance FCF | 3.09 | 13.03 | 16.85 | 17.19 |
| Project debt amortisation | 3.28 | 7.54 | 7.87 | 8.19 |
| FCF after debt service | −0.19 | 5.50 | 8.99 | 9.00 |
| Growth equity invested | 2.62 | 9.84 | 9.84 | 9.84 |
| Net debt (project + corporate) | 146.4 | 144.2 | 134.8 | 127.5 |
| V_t (year end) | 86.7 | 105.6 | 124.5 | **143.4** |
| **Bear** maintenance FCF / V_t | 3.09 / 86.7 | 7.35 / 73.6 | 8.94 / 60.6 | 9.38 / **47.5** |
| **Bull** maintenance FCF / V_t | 3.09 / 86.7 | 16.12 / 131.9 | 21.02 / 176.9 | 21.48 / **222.1** |

- Interim V_t glide linearly to each scenario's V_T (path diagnostic, not used in IRR_T). D_t = 0.

Tags: `[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value · `[E]` external or secondary · `[C]` carried from an earlier version · `[A]` own assumption · `[?]` not found.

## Header

| Item | Value |
|---|---|
| Company | Scatec ASA (SCATC, Oslo); renewable IPP and EPC developer in emerging markets. Reports in NOK; revenues in USD, ZAR, PHP, EUR, BRL, MYR and others |
| Price (P) | **NOK 82.40**, Oslo close 20 Nov 2026 (Yahoo `[F]`; 30 Oct 84.65, high since then 91.30 on 10 Nov; 52-week range 76.05–137.6) |
| Valuation / exit date | 20 Nov 2026 / 31 Dec 2029, **T = 3.113 years** |
| Shares | **159.83m** `[F]` (only 2026 issue: 1.0m employee shares in Q1) |
| Market cap / net debt | NOK 13.2bn. Proportionate NIBD **NOK 22.1bn** at 30 Sep `[F]`: project 16.4bn, corporate 5.7bn (≈ NOK 23.1bn at today's FX `[A]`). Consolidated NIBD 29.3bn (IFRS) |
| Book equity attributable (30 Sep) | NOK 8,374m = NOK 52.4 a share (after the Q3 impairment); P/B 1.57 |
| **NAV_0 (Base mid-cycle marks)** | **≈ NOK 83.8** a share at today's FX (80.0 at 30 Oct FX); **P/NAV_0 ~0.98**; Bear ~25.1, Bull ~137.4 |
| FX | USD/NOK **9.7525** (Norges Bank, 20 Nov; 9.1871 on 30 Oct), I-44 **110.74** (106.66). Revenue basket 40% USD, 60% I-44 (A14): factor **1.0476** |
| Track / k | **Track B**: finite-life, project-financed assets; V_T = NAV (asset marks less proportionate debt) plus an earnings value for the D&C platform. **k = 12%**, not raised (non-recourse amortising project debt; corporate NIBD 0.45× market cap) |
| Next events | Q4 report **29 Jan 2027** `[F]`; Philippine reserve-market redesign proposal by ~12 Apr 2027 `[F]`; SCATC05 repaid in H1 2027 `[F]`; Mogobe BESS COD H1 2027; EBRD platform closing (~Q1 2027 `[A]`) |

## Scenario definitions

- **Base: the Philippines mitigates most of the hit.** Hydro to the energy spot market, BESS to existing long-term ancillary-service contracts, new NGCP contracts; a redesigned reserve market from 2028 at lower prices. Philippines 700 (2027), 750 from 2028. COD on the company schedule. Growth equity NOK 1.5bn a year. FX at spot. Asset rate 9% / 11%.
- **Bear: the redesign caps reserve prices, plus emerging-market stress.** SNAP 400–450; Ukraine 50; Mogobe and Egypt delays; no Pakistan true-up; Mendubim and South African DSCR issues hold back distributions. Asset rate 10% (13%). Growth 0.9bn a year at F 0.9; no working-capital release. HY Bear spread (+2 pp) on corporate refinancing from 2028.
- **Bull: fast redesign at old economics.** Reserve market reopens in H1 2027 on longer-term contracts: 900, then 1,000. Egypt mega projects on time with strong D&C; growth at 2bn; asset rate 8%; F 1.3.
- The scenarios are **mid-cycle shifts** (the Philippine regime and the asset rate), not a cycle: the structural IRR is within 0.4 pp of IRR_T in all three.

## Company and status

- **Q3 2026** `[F]` (30 Oct): proportionate revenues NOK 2,267m; EBITDA **NOK 1,208m** (power 1,070, D&C 168 incl. 140 Obelisk close-out, corporate −31); cash flow to equity NOK 385m; production 1,469 GWh (+22%). Impairment NOK 1,066m (Ukraine 952, Pakistan 114). Consolidated loss NOK 1,135m.
- **Power EBITDA by country, LTM to Q3** `[F]`: Philippines 1,162; South Africa 701; Egypt 368; Malaysia 334; Laos 304; Ukraine 188; Czech 126; Brazil 127; Jordan 87; Botswana 80; Pakistan 76; Honduras 44; other −253. Contracted (ex Philippines and Ukraine, ex one-offs) ~NOK 2,150m LTM; H2 2026 run rate ~2,450m.
- **Philippines** (SN Aboitiz Power, 50%; 34% of Q3 power EBITDA, 58% of power cash flow to equity) `[F]`: the ERC suspended the reserve market on 12 Oct for six months pending a redesign "to limit elevated prices"; Q4 Philippine EBITDA guided **NOK 200–300m** (impact −80m); management expects "limited long-term effects". Three BESS (3 × 40 MW at 50%) reach COD H2 2026–H1 2027 on long-term contracts. No 2027 figure `[?]`.
- **FY 2026 guidance** `[F]`: power EBITDA NOK 3,300–3,600m (cut by 300 on 21 Oct: Philippines −80, Pakistan −40, South Africa −40, Ukraine −30, FX −86, other −24); D&C remaining contract value **NOK 10.5bn** (Q2 3.8bn) at 10–12% gross margin; no 2027 guidance.
- **Strategy to 2030** `[F]`: equity investment NOK 2bn a year (was 1bn; > 60% secured); gross corporate debt down to NOK 4bn (7.1bn at 30 Sep); NOK 3.4bn of divestments; cash flow to equity > NOK 2.5bn a year from 2030; self-funded, no dividend.
- **Egypt** `[F]`: EBRD platform SPA (22 Oct): up to USD 221m for 40% of a holdco with stakes in Obelisk, Shadwan, Dandara and Energy Valley; cash to Scatec, valuation and closing not disclosed `[?]` (treated as value neutral). Shadwan (900 MW wind) in construction from 1 Oct; Dandara phase 1 loans signed 28 Oct; Egypt CODs H1 2028.
- **Problem assets** `[F]`: Ukraine (FiT expires 2029; standstill on NOK 327m of debt); Pakistan (true-up delayed to 2027); Mendubim (covenant breach, debt current, Scatec share NOK 601m); South Africa (Mogobe COD H1 2027; DSCR risk 2027); Honduras receivables.
- **Corporate debt (30 Sep)** `[F]`: SCATC05 NOK 1,453m Q1 2028 (N+425; to be repaid H1 2027), **SCATC06 1,250m Q1 2029 (N+315; coupon 7.92% for 12 Nov–12 Feb)**, **SCATC07 1,000m Q1 2030 (N+285; 7.62%)**, SCATC08 1,500m Q1 2031 (N+250); Norfund note USD 120m Q1 2028; RCF NOK 724m drawn (working-capital bridge); new USD 350m RCFs from 29 Oct. Liquidity ~NOK 3.9bn with the new RCF. Corporate NIBD NOK 5.7bn.
- **Since 30 Oct:** no Scatec release found (Newsweb via Nordic Financial, web search, 21 Nov) other than the 12 Nov coupon resets (3M NIBOR fixing 4.77%; the NOK bonds are swapped to USD, so NIBOR does not drive the model).

## Near term (Q4 2026 stub, all scenarios)

| Item | Value | Basis |
|---|---|---|
| Power EBITDA | NOK 873m (30 Oct FX) | FY guide midpoint 3,450 − YTD 2,577 `[F]`; Philippines 250 |
| D&C EBITDA / corporate | NOK 80m / −33m | 11% underlying margin `[A]`; FY guide `[F]` |
| Maintenance FCF / amortisation / growth equity | NOK 472m / 500m / 400m | `[A]` |
| Corporate NIBD at 31 Dec | NOK 6.13bn (30 Oct FX) | No working-capital release in Q4 `[A]` |

## Market input (how each block enters)

| Block (NOK m, 30 Oct FX) | Bear 27 / 28 / 29 · mid | **Base 27 / 28 / 29 · mid** | Bull 27 / 28 / 29 · mid | Life left at exit, mark (EV/EBITDA) |
|---|---|---|---|---|
| Contracted portfolio | 2,150 flat | **2,350 / 2,365 / 2,380 · 2,390** | 2,450 / 2,480 / 2,500 · 2,500 | 16-yr PPA + 14-yr tail at 45%; 7.75x / **8.36x** / 9.05x |
| Under construction (ex Shadwan, Dandara) | 180 / 500 / 600 · 600 | **270 / 640 / 680 · 680** | 300 / 680 / 720 · 720 | 18 yr; 8.0x / **8.7x** / 9.4x |
| Philippines (SNAP hydro + BESS) | 400 / 450 / 450 · 450 | **700 / 750 / 750 · 750** | 900 / 1,000 / 1,000 · 1,000 | 25-yr merchant; 6.38x / **7.33x** / 8.55x |
| Ukraine | 50 flat | **150 / 180 / 160 · 100** | 200 / 280 / 250 · 150 | FiT ends 2029; 2.0x / **3.6x** / 3.8x |
| D&C | 250 / 300 / 250 · 250 | **480 / 580 / 500 · 500** | 600 / 750 / 700 · 650 | Platform at exit: (EBITDA × 0.8 − 130) × 6 / **10** / 11.5 |
| Corporate | −130 | **−130** | −130 | In cash flows; not in NAV |

- Marks are DCF EV/EBITDA at the scenario asset rate (contracted 10 / **9** / 8%; Philippines 13 / **11** / 9%); cash conversion 0.87; contracted EBITDA +0.6% a year; Philippine merchant flat.
- **Growth equity** is valued at T at F × equity invested (0.9 / **1.1** / 1.3): development equity NOK 1.35bn plus Q4 400 and 0.9 / **1.5** / 2.0bn a year. Projects reaching COD before exit earn no EBITDA in the window (conservative).

## Common assumptions

- **Project finance:** interest 6.8% of project NIBD; repayments NOK 1.15 / 1.20 / 1.25bn in 2027–29; remaining construction draws NOK 0.8bn; all power cash flow to equity reaches the recourse group.
- **Corporate:** interest 7.5% (Bear +2 pp from 2028); D&C cash 85% of EBITDA; working capital: Base releases the NOK 0.7bn RCF bridge over 2027–28, Bear none, Bull 0.7bn in 2027; divestments (NOK 3.4bn target) at NAV marks, left out (value neutral).
- **FX:** decision at spot (Base flat). v2.1 re-marks the whole v2 build by the basket factor 1.0476 `[A]`; Bear and Bull on the Equity BBB NOK path (Bear factor 1.072 at end-2029, Bull 0.976) as memo lines.
- **No dividends**; retained cash reaches V_T through corporate net debt.
- **Model:** the v2 build was rebuilt in the 30 Oct session (`scatec_v2.py`, scratchpad; not stored). v2.1 is `.claude/skills/iaf-valuation/references/models/scatec/v21.py`: it re-marks the v2 V_T values and the v2 sensitivity and break-even grids at a new price, date and FX (it reproduces v2: Base 16.4%, P_k 95.6). The full rebuild follows at the Q4 report.

## V_T bridge (Base, NOK per share at today's FX)

| Step | Per share |
|---|---|
| NAV_0 (Base mid-cycle marks, lives at today; under-construction and development equity at cost) | 83.8 |
| − Ageing of the existing portfolio (3 years at mid-cycle marks; incl. the Ukraine FiT roll-off) | −8.4 |
| + Under construction: EV at T less debt less equity already in NAV_0 | +9.3 |
| + Growth equity at T (new equity 4,900 × 1.1 + F uplift on development equity) | +36.2 |
| + Project amortisation paid from EBITDA | +25.8 |
| − Rise in corporate NIBD after paying the growth equity | −3.4 |
| **V_T** | **143.4** |

| Exit, NOK m (today's FX) | Bear | Base | Bull |
|---|---|---|---|
| Contracted EV | 17,457 | 20,926 | 23,704 |
| Under construction EV | 5,028 | 6,198 | 7,090 |
| Philippines EV | 3,007 | 5,757 | 8,953 |
| Ukraine EV | 105 | 377 | 597 |
| − Project NIBD | −13,724 | −13,724 | −13,724 |
| + Growth equity at F | 4,196 | 7,202 | 10,555 |
| + D&C platform | 440 | 2,829 | 4,698 |
| − Corporate NIBD | −8,918 | −6,648 | −6,376 |
| **V_T (per share)** | **7,591 (47.5)** | **22,917 (143.4)** | **35,497 (222.1)** |

- **Exit consistency:** no material gap except Ukraine (Year 3 160 vs mid 100), which has a named reason (FiT expiry 2029); the tail would add NOK 0.3 a share. Backlog at exit: growth equity at F; at cost (F = 1.0) Base is 18.4% (+18.8%).
- **Exit cross-check (Equity BBB 20 Nov, Oslo):** Base exit P/E on FCF_normalised before holdco G&A 9.8 against Oslo 11.5 (10.5 / 12.5); exit P/B 1.94 against 1.78; buyer's implied return ~11.4% against Oslo's mid-cycle 8.9%: the marks are not generous. Bull exit P/E 12.9 against Oslo Bull 12.5: Bull needs the Philippines and Egypt priced as quality.

## Growth capex test

- **Amount** (Q4 2026–2029): NOK 4.9bn of new equity in Base (Bear 3.1bn, Bull 6.4bn); company target NOK 8bn over 2027–30.
- **Return evidence** `[F]`: hurdle 1.2× cost of equity (~15% project equity IRR); D&C gross margin 10–12% (11% underlying in Q3); the capital-light model funds more than half the equity from the EPC margin (~NOK 2.8bn after opex and tax on the secured portfolio). Farm-down prices (NBE, EBRD) not disclosed `[?]`.
- **Value created (Base):** (1.1 − 1) × 4.9bn on the stakes plus ~NOK 1.4bn of D&C cash; equity IRR incl. D&C ~12–14% `[A]`. **Accretive in Base, destructive in Bear** (F 0.9). No new shares beyond employee shares.

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (dated, to V_T) | −16.2% | **19.5%** | 37.5% |
| IRR_T in NOK on the Equity BBB NOK path | −14.4% | 19.5% | 36.4% |
| d / g / c | 0 / −16.2% / 0 | **0 / 19.5% / 0** | 0 / 37.5% / 0 |
| ΣD_t / V_T | 0 / 47.5 | **0 / 143.4** | 0 / 222.1 |
| P_k / margin of safety | 33.3 / −59.5% | **100.8 / +22.3%** | 156.1 / +89.4% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² (Base FCF_normalised NOK 13.7 a share `[A]`) | 11.5x vs n/a | **6.0x vs 13.5x** | 5.0x vs 26x |
| Capital preserved? | No (−42%) | Yes | Yes |
| With FX held at 30 Oct (memo) | −17.5% / 31.8 | 17.7% / 96.2 / +16.8% | 35.5% / 149.0 |

- **Share of Bull priced:** (82.40 − 100.8) / (156.1 − 100.8) = **−33%** (below the Base hurdle).
- **Scenario-weighted reference (25/50/25 on levels, convention):** V_T ~139.1, IRR ~18.3%. Not the decision.

**Sensitivity** (Base, one change at a time, at NOK 82.40 and today's FX)

| Change | V_T | IRR_T | P_k | MoS |
|---|---|---|---|---|
| Base | 143.4 | 19.5% | 100.8 | +22.3% |
| Asset rate 10% (contracted and under construction) | 130.7 | 16.0% | 91.9 | +11.5% |
| Asset rate 8% | 157.3 | 23.1% | 110.6 | +34.2% |
| Philippines 450 a year (energy and BESS only) | 123.1 | 13.8% | 86.5 | +5.0% |
| Philippines 900 / 1,000 / 1,000 | 160.2 | 23.8% | 112.6 | +36.6% |
| Philippine asset rate 13% | 138.7 | 18.2% | 97.5 | +18.3% |
| Contracted EBITDA −NOK 150m | 132.1 | 16.4% | 92.8 | +12.7% |
| No D&C platform value at exit | 125.7 | 14.5% | 88.3 | +7.2% |
| Growth equity at cost (F = 1.0) | 139.3 | 18.4% | 97.9 | +18.8% |
| No working-capital release | 138.1 | 18.0% | 97.0 | +17.7% |
| FX held at 30 Oct | 136.9 | 17.7% | 96.2 | +16.8% |
| k = 13% / 14% | 143.4 | 19.5% | 98.0 / 95.4 | +19.0% / +15.7% |

- **Break-even Philippine EBITDA** (2028–29 and mid-cycle; 2027 at 700): **~NOK 320m** a year for k (extrapolated below the 400 grid point; ~410m at 30 Oct FX). v2: ~485m at NOK 84.65.

## Price versus our call (Step 6b)

| Item | Reading (21 Nov) | Score |
|---|---|---|
| **What the price implies** | Philippines ~NOK 320m a year from 2028 for k (below our Bear 400–450), or a 10% asset rate plus a second hit (Philippines 450 and 10% together ≈ fails) | — |
| Sector turn calls | No renewables baseline. Equity BBB 20 Nov: Oslo Base 4.0%, krone weaker (Scatec's NOK value +4.8%); HY BBB: no call on spreads | +1 (FX) |
| Contract behaviour and order intake | D&C book NOK 10.5bn (Q2 3.8bn); Shadwan construction start, Dandara loans signed; three BESS on long-term ancillary contracts (30 Oct `[F]`) | +1 |
| Guidance tone vs revisions | FY2026 power EBITDA cut by NOK 300m (21 Oct); consensus FY2027 EPS cut; targets NOK 110–150 (mostly set before 21 Oct) `[E]` | −1 |
| Capital and issuance | SCATC08 at N+250, the lowest margin yet; SCATC05 to be repaid; no equity issue | +1 |
| Asset sales vs book | EBRD platform: price undisclosed `[?]` | 0 |
| Insiders and holders | DNB AM 5.03% (22 Oct); Fredly 260,000 shares (DN 27 Oct `[E]`); no primary-insider trade found since 30 Oct `[?]` | 0 |
| **Net (company and upstream)** | | **+2** |

- **Market (L5):** −2.7% since 30 Oct (OSEBX −5.0%); −40% from the 52-week high (137.6).
- **Verdict line: ahead of the price, on the positive side.** The price discounts a Philippine outcome below our Bear, or EM stress stacked on it. Our named reason: the Q4 guide (200–300 for the quarter, ~1,000m a year) and the mitigation plan (BESS on long-term contracts, NGCP contracts). What the market may see that we do not: the redesign "to limit elevated prices", Egypt FX and payment risk, and corporate debt growth with no divestments yet.
- **Scorecard:** opened 21 Nov 2026 at NOK 82.40 (+22.3%). Hit if the Q4 report (29 Jan) shows Philippine EBITDA ≥ NOK 200m and the share outperforms the OSEBX by > 10% before the redesign proposal (~Apr 2027); miss if SNAP < 200 or the redesign caps reserve prices near energy prices.

## Verdict and caveat

- **Band applied:** Base margin of safety +22.3% (clears; Summary). Bear does not survive in value (−59.5%, ~42% permanent loss).
- **What would flip it:** a Philippine outcome below ~NOK 320m a year; an asset rate of 10% together with the Philippines at 450 (≈ fails); an Egypt setback (FX convertibility, payment delays) that turns growth equity below cost; the krone back at its 30 Oct level costs 5.5 pp of margin.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation or a price target. v2.1 is a re-mark of the v2 build `[A]`: the FX factor treats all blocks and both debt layers as foreign-currency.

## Tracking

| Version | Date / price | Base IRR | P_k | MoS | What changed |
|---|---|---|---|---|---|
| v1.1 | 27 Oct / NOK 80.60 | 14.5% | 86.5 | +7% | Fredly purchase confirmed |
| v2 | 30 Oct / NOK 84.65 | 16.4% | 95.5 | +13% | Q3 report: Philippines 700 / 750 / 750, D&C book 10.5bn, corporate NIBD 5.7bn |
| **v2.1** | **20 Nov / NOK 82.40** | **19.5%** | **100.8** | **+22.3%** | Price −2.7%, krone −4.8% (basket); no operating input |

- **Against the Base path:** no quarter since Q3. Q3 was ahead on earnings (power EBITDA 1,070 against ~890 implied), behind on the balance sheet (corporate NIBD NOK 1.0bn above plan).

## Risks and signposts

| Signpost | Bear | Base | Bull | Now (21 Nov) |
|---|---|---|---|---|
| Philippine EBITDA Q4 2026 (29 Jan) | < 200 | 200–300 | > 300 | Guide 200–300 |
| NGCP long-term ancillary-service contracts for SNAP | None | Some, with tenor | Near old economics | None announced |
| ERC redesign proposal (~Apr 2027) | Price caps near energy prices | Longer-term contracts at lower prices | Old economics | Pending |
| Corporate NIBD | > NOK 6.5bn without divestments | 6.1–6.4bn | < 5.5bn | 5.7bn (30 Sep) |
| Egypt (EBRD closing, Shadwan / Dandara, EETC payments, USD convertibility) | Delays, payment arrears | On schedule | Ahead; Energy Valley close | EBRD SPA signed; closing pending |
| FX (USD/NOK; I-44) | NOK strength (< 9.2) | Spot | NOK weakness | 9.75; 110.7 |
| Problem assets (Ukraine, Mendubim, South Africa DSCR, Pakistan, Honduras) | A new impairment or a cash trap | Resolved by 2027 | — | Standstill; covenant breach (Mendubim) |
| SCATC05 repayment (H1 2027) | Delayed | Repaid from liquidity | — | Planned |

## For other modules

- **HY BBB / `hy-funds`** (Scatec bonds in Sissener Corporate Bond 0.83% and Fondsfinans High Yield 1.99%; issuer credit check): credit read unchanged since Q3 (corporate NIBD NOK 5.7bn; SCATC08 at N+250; liquidity ~NOK 3.9bn; SCATC05 repaid H1 2027). Coupon resets 12 Nov: SCATC06 7.92%, SCATC07 7.62% (3M NIBOR 4.77%). Bear: corporate NIBD NOK 8.5bn by 2029 unless growth stops; Norfund (Q1 2028) and SCATC06 (Q1 2029) refinanced at Bear spreads. A watch point, not a watchlist trigger.
- **No sector BBB change needed** (no baseline covers renewables).

## Change log

- **21 Nov 2026 — v2.1** (iaf-valuation 2026-11-18.1): re-mark at NOK 82.40 (20 Nov) and the 20 Nov FX (basket factor 1.0476); Step 6b added (ahead, positive side); compacted 727 lines → lean; model `scatec/v21.py`. Base 16.4% → **19.5%**, P_k 95.5 → **100.8**, margin +13% → **+22.3%**; Bear −17.9% → −16.2%; Bull 33.6% → 37.5%; break-even Philippines ~485m → ~320m.
- **30 Oct 2026 — v2** (iaf-valuation 2026-10-29.1): after the Q3 report; Philippines 700 / 750 / 750; D&C 480 / 580 / 500; growth equity 1.5bn; corporate NIBD 5.7bn. Base 16.4%, P_k 95.5, +13%: clears.
- **27 Oct 2026 — v1.1:** Fredly purchase confirmed (DN); price-implied Philippines ~510m; no model value changed.

## Appendix: own assumptions `[A]`

By weight on the result: (1) the Philippine EBITDA path (Bear 400 / 450; **Base 700 / 750**; Bull 900 / 1,000) and its 11% asset rate; (2) the contracted asset rate (10 / **9** / 8%) and mark structure (16-yr PPA left + 14-yr tail at 45%, +0.6% a year, conversion 0.87); (3) growth equity 0.9 / **1.5** / 2.0bn a year at F 0.9 / **1.1** / 1.3; (4) D&C path and platform multiple (6 / **10** / 11.5); (5) the FX factor (40% USD/NOK, 60% I-44) applied to all blocks and both debt layers; (6) contracted EBITDA NOK 2,350m; (7) under construction to 680 (Mogobe H1 2027); (8) Ukraine 150 / 180 / 160, mid 100; (9) project amortisation 1.15–1.25bn, interest 6.8% project / 7.5% corporate; (10) Base working-capital release NOK 0.7bn over 2027–28; (11) book equity at exit 9.6 / 11.3 / 12.4bn.

## Appendix: sources

| # | Source | Content | As of |
|---|---|---|---|
| S1 | Scatec Q3 2026 report, presentation and databook (storage.mfn.se, read 30 Oct `[C]`) | Results, country EBITDA, Philippine impact and mitigation, guidance, strategy, Egypt, problem assets, debt, liquidity | 30 Sep / 30 Oct 2026 |
| S2 | Scatec releases 21 Oct (outlook revision) and 22 Oct (EBRD platform); flagging DNB AM 5.03% `[C]` | Guidance cut, platform terms, holder | Oct 2026 |
| S3 | Stamdata / Nordic Trustee coupon notices for NO0013476101 (SCATC06) and NO0013696435 (SCATC07), via the user | Coupons 7.92% / 7.62% for 12 Nov–12 Feb | 12 Nov 2026 |
| S4 | Yahoo `SCATC.OL` chart; Norges Bank EXR (USD, I-44); Nordic Financial (Newsweb, no release after 30 Oct found); web search | Price 82.40 (20 Nov); USD/NOK 9.7525, I-44 110.74 | 20–21 Nov 2026 |
| S5 | `docs/equity-market-bbb.md` (20 Nov note), `docs/hy-market-bbb.md` (18 Nov) | Exit references, NOK path; Bear refinancing spread | 18–20 Nov 2026 |
| S6 | DN, 27 Oct 2026 (text from the user) `[E]` | Fredly purchase; Pareto and Arctic views | 27 Oct 2026 |

- **Validation:** `v21.py` reproduces v2 at 30 Oct (Base 16.4%, P_k 95.6; Bear −17.9%; Bull 33.6%). Earlier versions and the full v2 tables are in git history.
