# Scatec (SCATC) — IAF analysis, 30 Oct 2026 (v2) (stub Q4 2026 + 2027–2029)

**Version 2, 30 Oct 2026**, after the Q3 2026 report (published 30 Oct 07:00 CET). It replaces
v1.1 of 27 Oct. Q3 actuals replace the estimates, the valuation date moves to 30 Oct, and a
Tracking section is added. Skill revisions used:
- **iaf-valuation 2026-10-29.1** (v1 used 2026-10-18.2).
- **equity-market-bbb 2026-10-24.1**: used for the exit cross-check and the NOK path only.
- **hy-market-bbb 2026-10-24.1**: used for the Bear refinancing spread only.

Sector inputs:
- **No sector baseline covers renewable power** (solar, wind, BESS, hydro in emerging markets).
  - The asset marks, the Philippine view and the project paths are own assumptions `[A]`, built
    from Scatec's own reports and guidance. Each one is named in the appendix.
  - No oil, rig, shipping or defense input is used. Scatec's earnings do not follow Brent.
- `docs/equity-market-bbb.md`: 17 Oct 2026, amended 18 Oct (stale after 10 Nov). Oslo exit P/E
  11.5, exit P/B 1.75 and mid-cycle return 9.1% for the exit cross-check; USD/NOK and I-44 paths for
  the Bear/Bull NOK figures. Nothing else is taken from it.
- `docs/hy-market-bbb.md`: 24 Oct 2026. Bear new-issue spread (about +2 pp on corporate
  refinancing from 2028). Scatec's NOK bonds are swapped to USD, so the NIBOR path does not drive
  its interest cost.

Update triggers and dates:
- **Next update at the Q4 report on 29 Jan 2027** `[F]` (Scatec financial calendar). It brings
  the first quarter without the Philippine reserve market, 2027 guidance and net debt at 31 Dec.
- **Stale after 28 Feb 2027.** Also update on the Philippine reserve-market redesign proposal
  (due by ~12 Apr 2027), any NGCP long-term ancillary-service contract for SNAP, the EBRD platform
  closing, and the Pakistan true-up decision (expected 2027).
- **Oldest input:** Q3 accounts (30 Sep 2026). Price: 30 Oct close.

## Summary

**Verdict: clears.** Base IRR **16.4%** against k = 12%. The hurdle price is **NOK 95.5**
against **NOK 84.65**, a margin of safety of **+13%** (v1.1: +7%).
- **What changed:** the Philippine hit is much smaller than v1 feared.
  - Scatec guides Q4 Philippine EBITDA at **NOK 200–300m** after the reserve-market suspension.
    The impact is about −80m in Q4, and management expects "limited long-term effects". v1 had
    ~NOK 120m in Q4.
  - Base Philippines is raised to **700 / 750 / 750** (v1 550 / 650 / 650). That alone adds ~6
    points to the margin of safety.
  - The D&C contract book rose to NOK 10.5bn (from 3.8bn), and Scatec doubled its equity growth
    target to NOK 2bn a year.
  - Against that: corporate net debt at 30 Sep is NOK 5.7bn, NOK 1.0bn above v1's estimate
    (working capital and Egypt investments). Ukraine and Pakistan were impaired by NOK 1.07bn.
- **Scatec is priced at about its Base NAV** (P/NAV_0 1.06). The return comes from NAV growth:
  - project debt amortisation (NOK 25 a share by exit);
  - projects under construction reaching COD;
  - D&C margins that fund much of the new equity.
- **What the price needs:** Philippine EBITDA of about **NOK 485m a year** from 2028
  (break-even at k). That compares with ~NOK 1,050m in 2026 and NOK 540–890m a year in 2022–23,
  before the reserve market opened. The Q4 guide alone runs at ~NOK 1,000m a year.
- **The margin is still not wide.** Each single change below takes it to +4% or less:
  - Philippines 450 a year: −3%;
  - no D&C platform value at exit: −1%;
  - asset rate 10% instead of 9%: +3%;
  - NOK 150m less contracted EBITDA: +4%.
- **Bear** (the redesign caps reserve prices and no NGCP contracts; Egypt and South Africa
  delays; 10% asset rate): **IRR −17.9%**.
  - Capital is not preserved: V_T NOK 45.3 against 84.65, a ~46% permanent loss.
  - Corporate net debt would reach NOK 8.5bn by 2029 at NOK 0.9bn a year of growth. Liquidity is
    NOK 3.9bn. Survival needs growth stopped after the committed Egypt equity. Bear breaks the
    thesis.
- **Bull** (the reserve market reopens in H1 2027 near old economics; Egypt on time; 8% asset
  rate): **IRR 33.6%**, hurdle NOK 148.0. The price is below the Base hurdle, so it reflects none
  of the Base→Bull gap (−21%).

**Decision table** (NOK per share; P = NOK 84.65; no dividend in any scenario)

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T | −17.9% | **16.4%** | 33.6% |
| V_T (31 Dec 2029) | 45.3 | **136.9** | 212.0 |
| P_k / margin of safety | 31.6 / −63% | **95.5 / +13%** | 148.0 / +75% |
| Capital preserved? (ΣD_t + V_T vs P) | **No**, −46% | Yes | Yes |
| Cumulative Maintenance FCF per share (Q4-26–2029) | 27.4 | **47.9** | 58.9 |
| Net debt per share at exit: proportionate total / corporate | 135.2 / 53.3 | **121.7 / 39.7** | 120.0 / 38.1 |
| Balance-sheet line | Corp. NIBD NOK 8.5bn by 2029 against NOK 3.9bn liquidity; growth must stop after 2027; refinance Norfund (Q1 2028) and SCATC06 (Q1 2029) at Bear spreads | Corp. NIBD NOK 6.1–6.4bn while growth runs at NOK 1.5bn a year (divestments not modelled) | Corp. NIBD NOK 6.1bn |

**Per-share path** (NOK per share; proportionate; EBITDA = power + D&C − corporate)

| Base | Q4 2026 (stub) | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| EBITDA, NOK m (per share) | 920 (5.8) | 3,820 (23.9) | 4,385 (27.4) | 4,340 (27.2) |
| Maintenance FCF | 2.95 | 12.44 | 16.08 | 16.41 |
| Project debt amortisation | 3.13 | 7.20 | 7.51 | 7.82 |
| FCF after debt service | −0.18 | 5.25 | 8.58 | 8.59 |
| Growth equity invested | 2.50 | 9.39 | 9.39 | 9.39 |
| D_t paid | 0 | 0 | 0 | 0 |
| Net debt (project + corporate) | 139.7 | 137.6 | 128.7 | 121.7 |
| V_t | 82.8 | 100.8 | 118.8 | **136.9** |
| **Bear** Maintenance FCF / V_t | 2.95 / 82.8 | 7.02 / 70.3 | 8.53 / 57.8 | 8.95 / **45.3** |
| **Bull** Maintenance FCF / V_t | 2.95 / 82.8 | 15.39 / 125.9 | 20.06 / 168.9 | 20.50 / **212.0** |

**Practical reading** (portfolio ~85% Nordic HY, stocks opportunistic):
- On investment value, the share now clears with a real margin in Base. It still fits only the
  opportunistic sleeve: Bear loses about half, and the Philippine redesign is not yet known.
- The next hard test is the Q4 report (29 Jan 2027): actual Philippine EBITDA without the reserve
  market, and any NGCP contract.

## Tags

`[F]` fact from a filing or market print · `[B]` derived from a disclosed contract value · `[E]`
external or secondary · `[C]` carried from an earlier version · `[A]` own assumption · `[?]` not
found.

## Header

| Item | Value |
|---|---|
| Company | Scatec ASA (SCATC, Oslo); renewable IPP and EPC developer in emerging markets |
| Price | **NOK 84.65** `[F]` (Yahoo `SCATC.OL`, close 30 Oct 2026 15:29 UTC; day range 84.05–88.50 on the report; 52-week range 76.05–137.6) |
| Valuation date / exit / T | 30 Oct 2026 / 31 Dec 2029 / **3.17 years** |
| Shares | **159.83m** `[F]` (Yahoo; Q3 report: average 159.8m; the only 2026 issue was 1.0m employee shares in Q1; no change in Q3) |
| Market cap | NOK 13.53bn |
| Proportionate net interest-bearing debt (30 Sep 2026) | **NOK 22.1bn** `[F]`: project level 16.4bn (operation 14.2, under construction 2.2; incl. SPV cash 3.0), group (corporate) level 5.7bn |
| Proportionate EV | ~NOK 35.7bn at the valuation-date estimates (project 16.3bn, corporate 5.8bn `[A]`) |
| Consolidated NIBD (30 Sep) | NOK 29.3bn `[F]` (IFRS; includes partners' shares of consolidated projects) |
| Book equity attributable (30 Sep) | NOK 8,374m `[F]` = NOK 52.4 a share (after the Q3 impairment of NOK 1.0bn attributable and FX); P/B 1.62 |
| NAV at today's market marks | Omitted: no market mark exists for the portfolio (no broker or transaction NAV) |
| **NAV_0 (Base mid-cycle marks)** | **NOK 80.0** a share; **P/NAV_0 1.06** (Bear 24.0, Bull 131.2 at their own marks) |
| FX | Reports in NOK. USD/NOK **9.1871**, EUR/NOK 10.268 `[F]` (Yahoo, 30 Oct 21:01 / 21:28 UTC). NOK 1.4% firmer against USD than in v1 (9.3165). Revenues are in USD, ZAR, PHP, EUR, BRL, MYR and others; corporate NOK bonds are swapped to USD |
| Track | **B**: a capital-intensive owner of finite-life, project-financed assets. V_T = NAV (asset marks less proportionate debt), plus an earnings value for the D&C platform as a continuing business |
| k | **12%**, not raised. The project debt is non-recourse and amortising. Corporate leverage is moderate (corp. NIBD 0.42x market cap). Shown at 13% and 14% in the sensitivity: still +10% and +7% |
| Next events | Q4 2026 report **29 Jan 2027** (07:00 CET) `[F]`; Philippine reserve-market redesign proposal due by ~12 Apr 2027 `[F]`; SCATC05 to be repaid in H1 2027 `[F]` (presentation); Mogobe BESS COD H1 2027 `[F]` |

Sources for key figures: Q3 2026 report, presentation and databook (MFN storage links in the
appendix); Scatec financial calendar; Yahoo for price, FX and consensus. The Newsweb results text
was not read: the Nordic Financial connector was not available in this run, so the full report was
used instead.

## Scenario definitions

- **Base: the Philippines mitigates most of the hit.** In the interim, Scatec moves hydro capacity
  to the energy spot market, BESS to existing long-term ancillary-service contracts, and signs new
  contracts with NGCP (the ERC told NGCP to seek longer-term contracts). A redesigned reserve market
  comes from 2028 at lower prices.
  - Philippine EBITDA: NOK 700m in 2027 (dry season H1 without a market), 750m from 2028.
  - Projects under construction reach COD on the company schedule (Mogobe H1 2027). Growth equity
    runs at NOK 1.5bn a year (company target 2bn). FX holds at spot. Asset rate 9% (contracted)
    and 11% (Philippine merchant hydro).
- **Bear: the redesign caps reserve prices, plus emerging-market stress.** Bear catalysts:
  - The redesign caps reserve prices and NGCP signs no new contracts, so SNAP earns mostly energy
    plus BESS contracts: NOK 400–450m.
  - Ukraine stays disrupted (NOK 50m).
  - Further delays at Mogobe and in Egypt; Pakistan's true-up does not come; Mendubim's and the
    South African DSCR issues hold back distributions.
  - Asset rate 10% (Philippines 13%). Growth equity NOK 0.9bn a year (committed Egypt equity).
    Value factor on new equity 0.9x. No working-capital release.
- **Bull: fast redesign at old economics.** Bull catalysts:
  - The reserve market reopens in H1 2027 on longer-term contracts near old economics:
    NOK 900m, then 1,000m.
  - The Egypt mega projects (Shadwan, Dandara, Energy Valley) proceed on time with strong D&C.
    Growth at the NOK 2bn target. Asset rate 8%. Value factor on new equity 1.3x.
- The scenarios are **mid-cycle shifts**, not rate paths around one mid-cycle: the structural IRR
  is within 0.4 pp of IRR_T in all three (Results).

## Company and status

- **Portfolio (Q3 report, at publication)** `[F]`:
  - In operation: 6.1 GW generation and storage, 47% average economic interest, across 14
    countries plus Release.
  - Under construction: 2.3 GW generation and 0.68 GWh storage (66%). New in Q3–Q4: Shadwan
    (900 MW wind, construction from 1 Oct) and Dandara phase 1 (569 MW solar + 50 MW / 100 MWh,
    loans signed 28 Oct).
  - Backlog: 4.3 GW and 4.7 GWh (70%), led by Energy Valley (1,950 MW solar + 842 MW / 3,935 MWh).
  - Pipeline: 6.2 GW and 8.3 GWh.
- **Q3 2026 proportionate results** `[F]`:
  - Revenues NOK 2,267m; EBITDA **NOK 1,208m** (Q3 2025: 1,063): power 1,070, D&C 168,
    corporate −31.
  - Cash flow to equity **NOK 385m** (Q3 2025: 538, which included 253 of Philippine refinancing
    proceeds): power 442, D&C 138, corporate −195.
  - Production 1,469 GWh (+22%, new assets).
  - D&C gross margin 26%, of which NOK 140m Obelisk close-out (incl. NOK 100m contingency
    release); the underlying margin was 11%.
  - Impairment NOK 1,066m proportionate (Ukraine 952, Pakistan 114). Consolidated loss NOK 1,135m;
    EPS −6.27.

Q3 2026 power EBITDA by country (databook, NOK m) `[F]`:

| Country | Q3 26 | Q2 26 | Q1 26 | Q4 25 | Q3 25 | LTM |
|---|---|---|---|---|---|---|
| **Philippines** | **367** | 201 | 231 | 363 | 332 | **1,162** |
| South Africa | 180 | 134 | 191 | 196 | 158 | 701 |
| Egypt | 139 | 99 | 77 | 53 | 76 | 368 |
| Laos | 90 | 72 | 68 | 74 | 88 | 304 |
| Malaysia | 78 | 85 | 90 | 81 | 81 | 334 |
| **Ukraine** | **78** | 74 | 18 | 18 | 130 | **188** |
| Czech Republic | 48 | 49 | 19 | 10 | 44 | 126 |
| Brazil | 35 | 34 | 15 | 43 | 26 | 127 |
| Jordan | 26 | 27 | 18 | 16 | 27 | 87 |
| Botswana | 22 | 18 | 22 | 18 | 10 | 80 |
| Pakistan | 20 | 24 | 17 | 15 | 17 | 76 |
| Honduras | 13 | 16 | 20 | −5 | 4 | 44 |
| Tunisia | 8 | 5 | – | – | – | 13 |
| Other (incl. Release, Romania, Colombia, cost allocations; Vietnam −56 in Q1) | −32 | −32 | −83 | −106 | −36 | −253 |
| **Power total** | **1,070** | 805 | 702 | 775 | 955 | **3,352** |
| Contracted (total less Philippines and Ukraine) | 625 | 530 | 453 | 394 | 493 | 2,002 |

- Contracted ex the one-offs (Vietnam −56 in Q1, Other −106 in Q4 2025) runs at ~NOK 2,150m
  LTM. With the Q4 guide (contracted ~NOK 600m) the H2 2026 run rate is ~NOK 2,450m a year,
  including Obelisk phase 2 and Rio Urucuia in full.
- **Philippines** (SN Aboitiz Power, 50%): Q3 EBITDA 367 (net revenue 411, of which ~235 at an
  effective ancillary-service price of 3.8 PHP/kWh) `[F]`. 34% of power EBITDA and 58% of power
  cash flow to equity in Q3 (CFE 257 of 442).
- **What replaces the suspended reserve market** (ERC order of 12 Oct 2026; suspension for six
  months pending a redesign) `[F]`:
  - Scatec's mitigation: reallocate hydro capacity to the energy spot market; reallocate BESS
    capacity to existing long-term ancillary-service (AS) contracts; enter new AS contracts with
    NGCP; arbitrage trading in the spot market.
  - The ERC asked the market operator to propose a redesign "to limit elevated prices" within six
    months and, meanwhile, to seek longer-term contracts for AS demand. No ASPA prices or
    must-run cost recovery were quantified `[?]`.
  - Scatec says the suspension was triggered by high prices in the Visayas, where it does not
    operate, and expects continued strong AS demand.
  - **Size of the hit:** Q4 2026 Philippine EBITDA guided at **NOK 200–300m** (midpoint 250),
    with an estimated impact of **−NOK 80m** (Q4 net revenue 296 against 376 before). Management:
    "limited long-term effects". No 2027 figure was given `[?]`.
  - BESS: Binga, Binga 2 and Ambuklao (3 × 40 MW / 40 MWh at 50%) are under construction, COD H2
    2026 to H1 2027. They go to long-term AS contracts, not held back.
- **FY 2026 guidance** (30 Oct) `[F]`:
  - Power EBITDA **NOK 3,300–3,600m** (midpoint 3,450; unchanged from 21 Oct). The −300m bridge:
    Philippines −80, Pakistan −40, South Africa −40, Ukraine −30, FX −86, other −24. Implied Q4
    power EBITDA ~NOK 873m.
  - Production 4,950–5,150 GWh (Q4 1,300–1,400).
  - D&C remaining contract value **NOK 10.5bn** (Q2: 3.8bn) at 10–12% gross margin.
  - Corporate EBITDA −110 to −120 (raised by 15).
  - No 2027 guidance.
- **Strategy update to 2030** `[F]`:
  - average equity investment of **NOK 2bn a year** (was 1bn; NOK 8bn over 2027–2030, >60%
    secured in backlog and under construction);
  - gross corporate debt down to NOK 4bn (7.1bn at 30 Sep, incl. the 0.7bn RCF draw);
  - NOK 3.4bn of divestments;
  - cash flow to equity >NOK 2.5bn a year from 2030 (run rate);
  - self-funded, with no dividend (last paid Apr 2023).
- **Egypt** `[F]`:
  - **EBRD platform** (SPA signed 22 Oct): EBRD commits up to USD 221m (~USD 170m equity, the rest
    project-level guarantees) for 40% of a holdco that takes 40% of Obelisk, 51% of Shadwan and
    ~60% of Dandara and Energy Valley. Scatec holds 60%. **Cash to Scatec, the implied valuation
    and the closing date are not disclosed** `[?]`. Still treated as value neutral and as funding
    for the Egypt equity.
  - **Shadwan** (900 MW wind, EDF partner): construction started 1 Oct. USD 50m TAEF equity
    bridge loan.
  - **Dandara / Egypt Aluminium phase 1**: USD 217m non-recourse loans (EBRD, AfDB, EIB) signed
    28 Oct, construction starting. NBE takes 20%; Scatec ends at 56% (36% via the platform, 20%
    direct).
  - **Energy Valley**: still backlog; USD 100m TAEF EBL secured. Egypt CODs H1 2028.
  - Obelisk completed early, below budget.
- **Problem assets** `[F]`:
  - **Ukraine:** impairment NOK 952m proportionate (after-tax discount rate 24%). Most plants run
    on 10-year feed-in tariffs that **expire in 2029** (v1 said 2030). The plant damaged in 2025
    is assumed back from Jan 2028. Non-recourse debt NOK 327m in breach under a standstill.
  - **Pakistan:** the true-up is delayed, with final approval expected in 2027; impairment
    NOK 114m proportionate. The interim 2025–26 true-up cash is still in the company's cash flow
    projections.
  - **Mendubim** (Brazil, 30%): in breach of covenants at 30 Sep; debt classified as current;
    Scatec's share NOK 601m.
  - **South Africa:** Mogobe BESS COD moved to H1 2027 (Eskom grid works). Grootfontein and Mogobe
    risk missing DSCR tests in 2027.
  - **Honduras:** receivables NOK 60m, of which 36m overdue; lower performance ratios under review.
- **Corporate debt (30 Sep)** `[F]`:
  - Bonds: SCATC05 NOK 1,453m Q1 2028 (N+425, NOK 297m bought back; to be repaid in H1 2027),
    SCATC06 1,250m Q1 2029 (N+315), SCATC07 1,000m Q1 2030 (N+285), **SCATC08 1,500m Q1 2031
    (N+250, new)**. SCATC04 fully redeemed.
  - Norfund vendor note USD 120m, due Q1 2028 (USD 20m repaid in Q3).
  - RCF: NOK 724m drawn on the old USD 230m facility (a short-term working-capital bridge). The
    new USD 350m RCFs became effective 29 Oct.
  - Free cash NOK 1,203m; available liquidity NOK 2,736m at 30 Sep and ~NOK 3.9bn including the
    new RCF capacity.
  - Equity bridge loans NOK 1,152m (Egypt), guaranteed 84% by Scatec ASA (they sit in project
    debt).
  - Gross corporate debt NOK 7.1bn; corporate NIBD **NOK 5.7bn** (Q2: 4.6bn). Q3 used ~NOK 1.1bn:
    working capital −746 (Egypt and South Africa construction), investments −687 (under
    construction 304, development 383), interest −147.
- **Shareholders:** DNB AM at 5.03% (22 Oct). Fredly (Apollo Asset) 260,000 shares (DN, 27 Oct)
  `[E]`. Neither is an IAF input.

## Near term

| Q4 2026 (stub) | Value | Basis |
|---|---|---|
| Power EBITDA (ops) | NOK 873m `[F]` | FY guide midpoint 3,450 − YTD 2,577; Philippines 250 (guide 200–300), contracted ~600, Ukraine ~20 `[A]` |
| D&C EBITDA | NOK 80m `[A]` | ~NOK 1.4bn revenue at the 11% underlying margin, less ~NOK 75m opex (Q3 underlying ~30) |
| Corporate EBITDA | −NOK 33m `[F]` | FY guide −115 − YTD −82 |
| Maintenance FCF | NOK 472m (2.95 a share) | after project interest, tax, corporate interest and opex |
| Project amortisation | NOK 500m `[A]` | Semi-annual payments fall in Q4; normalised 292 a quarter (Q3) |
| Growth equity | NOK 400m `[A]` | Shadwan and Dandara starts; most Shadwan/Energy Valley equity goes through the TAEF EBL |
| Dividend | none | No declared dividend; nothing goes ex in the stub |
| Corporate NIBD | 5.70bn (30 Sep) → 5.84bn at the valuation date `[A]` → **6.13bn at 31 Dec** | No working-capital release assumed in Q4 |
| Project NIBD | 16.40bn (30 Sep) → 16.33bn `[A]` → 16.20bn at 31 Dec | Repayments 0.5bn, construction draws 0.3bn |

- **Consensus** (Yahoo, consolidated basis, not the proportionate basis used here) `[E]`:
  - Q4 EPS NOK 1.05 (2 estimates, cut from 1.51 a week ago).
  - FY 2026 EPS 0.96 (6 estimates; before the Q3 loss of −6.27 a share was fully reflected).
  - FY 2027 EPS 7.67 (5 estimates, range 1.35–11.5).
  - Targets NOK 110–150, mean 128.5 (8 analysts, mostly set before 21 Oct).
  - Consolidated EPS includes D&C profit on 100%-consolidated Egypt projects, so it is not
    comparable with the IAF path.

## Market input (how each block enters)

Proportionate EBITDA, NOK m `[A]` except history `[F]`. Changes from v1.1 are tagged `(v2)`.

| Block | LTM to Q3 26 `[F]` | Bear 27 / 28 / 29 · mid | **Base 27 / 28 / 29 · mid** | Bull 27 / 28 / 29 · mid | Life left at exit, mark |
|---|---|---|---|---|---|
| Contracted portfolio (all operating except the Philippines and Ukraine) | ~2,150 ex one-offs | 2,150 flat · 2,150 | **2,350 / 2,365 / 2,380 · 2,390** | 2,450 / 2,480 / 2,500 · 2,500 | 16 yr PPA + 14 yr tail at 45%; 7.75x / **8.36x** / 9.05x |
| Under construction (COD 2026–28; ex Shadwan and Dandara) | – | 180 / 500 / 600 · 600 (v2) | **270 / 640 / 680 · 680** (v2: Mogobe H1 2027) | 300 / 680 / 720 · 720 (v2) | 18 yr; 8.0x / **8.7x** / 9.4x |
| Philippines (SNAP hydro + BESS) | 1,162 | 400 / 450 / 450 · 450 | **700 / 750 / 750 · 750** (v2) | 900 / 1,000 / 1,000 · 1,000 (v2) | 25 yr merchant; 6.38x / **7.33x** / 8.55x |
| Ukraine | 188 | 50 / 50 / 50 · 50 | **150 / 180 / 160 · 100** (v2) | 200 / 280 / 250 · 150 (v2) | FiT ends 2029, then merchant; 2.0x / **3.6x** / 3.8x |
| D&C | 753 (incl. 340 contingency releases) | 250 / 300 / 250 · 250 | **480 / 580 / 500 · 500** (v2) | 600 / 750 / 700 · 650 (v2) | Platform value at exit (below) |
| Corporate | −110 | −130 a year | **−130** | −130 | In cash flows; not in NAV (Step 3) |

- Marks are EV/EBITDA from a DCF of each block at the scenario's asset rate. Cash conversion is
  0.87 (cash tax ~5–6% of EBITDA, plus maintenance and inverter replacement). Contracted EBITDA
  grows 0.6% a year (partial CPI indexation less degradation); Philippine merchant EBITDA is held
  flat. Asset rates:
  - contracted: Bear 10% / Base 9% / Bull 8%;
  - Philippines: 13% / 11% / 9%.
- **Contracted (unchanged):** the Q3 and Q4 run rate (~NOK 2,450m a year at spot FX) supports the
  Base 2,350. The NOK has firmed 1.4% since v1, and Mendubim, Honduras and Pakistan are weak; these
  are held inside the Base rather than added on.
- **Philippines (v2):** the Q4 guide of 250 runs at ~NOK 1,000m a year. Base 2027 is lower (700)
  for three reasons:
  - Q1–Q2 are dry-season quarters that leaned most on reserve revenue (Q2 2026: AS 199 of 244 net
    revenue);
  - the redesign is only due by ~Apr 2027;
  - spot prices (6.3 PHP/kWh in Q3) may normalise.
  - 2028 (750) adds the redesigned market and the three new BESS on long-term AS contracts.
- **Ukraine (v2):** LTM 188. The FiT expires in 2029 and the damaged plant is back in 2028
  (Note 5), so 2028–29 are above mid-cycle (100, merchant).
- **D&C (v2):** the remaining contract value of NOK 10.5bn at 11% gives ~NOK 1.15bn gross profit,
  mostly in 2027–28, less ~NOK 300m opex a year. Backlog projects add from H2 2027 (Energy Valley,
  Dandara phase 2, Kroonstad).
- **Growth equity** (Shadwan, Dandara, backlog and development) is valued at T at **F × equity
  invested**: Bear 0.9 / Base 1.1 / Bull 1.3. The base is NOK 1.35bn in development at the
  valuation date `[A]` plus the new equity: Q4 400, then 0.9 / **1.5** / 2.0bn a year (v2; v1
  0.7 / 1.0 / 1.2). Projects reaching COD before exit (Shadwan, Dandara in H1 2028) earn no
  EBITDA in the window under this convention. That is conservative.
- **D&C platform** (a continuing business at exit): (D&C EBITDA × 0.8 after tax − corporate cost
  130) × multiple. Multiples are 6 / 10 / 11.5 (Oslo exit P/E), giving NOK 0.42 / **2.70** /
  4.49bn (v1 0.42 / 2.30 / 4.03). The corporate cost is charged here because this overhead runs
  the platform.

## Common assumptions

- **Project finance** (proportionate):
  - interest 6.8% of project NIBD (Q3 2026: NOK 283m on 16.4bn);
  - normalised repayments of NOK 1.15 / 1.20 / 1.25bn in 2027–29 (v2; Q3 normalised 292 a
    quarter; v1 1.05–1.15);
  - remaining construction draws for the under-construction block NOK 0.8bn (Q4 0.3, 2027 0.5;
    v2: NOK 1.0bn drawn in Q3, more than v1 assumed). Shadwan and Dandara debt is not in the
    model: these projects are valued as equity at F;
  - all power cash flow to equity reaches the recourse group (counted once; SPV cash builds are
    ignored).
- **Corporate:**
  - interest 7.5% of corporate NIBD (v2; Q3 net interest 131 incl. a 25m buy-back premium, ~8% on
    the average; SCATC08 at N+250 lowers the cost). Bear +2 pp from 2028;
  - D&C cash at 85% of EBITDA (Q3: 82%);
  - **working capital** (v2): Base releases the NOK 0.7bn RCF-funded bridge over 2027–28 (0.35bn a
    year; Scatec calls it a short-term working-capital bridge; 2025 released 1.7bn after Obelisk).
    The rest of the 2026 build (~NOK 1.0bn) stays tied up while the 10.5bn book is built. Bear
    releases nothing; Bull releases 0.7bn in 2027;
  - divestments (NOK 3.4bn target, incl. the EBRD platform) are assumed at NAV marks and left out
    (value neutral). So the modelled corporate NIBD stays above the company's NOK 4bn target.
- **No dividends** in any scenario. Retained cash reaches V_T through corporate net debt.

## Period tables and year-end path

Base, NOK m (per share in brackets):

| Base | Q4 26 | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Power EBITDA (ops) | 873 | 3,470 | 3,935 | 3,970 |
| D&C EBITDA | 80 | 480 | 580 | 500 |
| Project interest | −277 | −1,080 | −1,017 | −933 |
| Tax (power) | −52 | −208 | −236 | −238 |
| Corporate interest + opex (D&C cash adjustment in the total) | −140 | −601 | −605 | −601 |
| **Maintenance FCF** | **472 (2.95)** | **1,989 (12.44)** | **2,571 (16.08)** | **2,622 (16.41)** |
| Project amortisation | −500 (3.13) | −1,150 (7.20) | −1,200 (7.51) | −1,250 (7.82) |
| **FCF after debt service** | **−28 (−0.18)** | **839 (5.25)** | **1,371 (8.58)** | **1,372 (8.59)** |
| Growth equity | −400 | −1,500 | −1,500 | −1,500 |
| Working-capital release | 0 | +350 | +350 | 0 |
| Corporate NIBD, end | 6,128 (38.3) | 6,439 (40.3) | 6,219 (38.9) | 6,346 (39.7) |
| Project NIBD, end | 16,200 (101.4) | 15,550 (97.3) | 14,350 (89.8) | 13,100 (82.0) |

- Maintenance FCF = power EBITDA − project interest − power tax + 0.85 × D&C EBITDA + corporate
  EBITDA − corporate interest.
- Bear: Maintenance FCF 472 / 1,122 / 1,364 / 1,430; growth equity 900 a year; corporate NIBD
  6,128 / 7,057 / 7,793 / 8,513.
- Bull: Maintenance FCF 472 / 2,460 / 3,206 / 3,276; growth equity 2,000 a year; corporate NIBD
  6,128 / 6,118 / 6,112 / 6,086.
- Project NIBD is the same in all three (same schedule; Bear delays show as lower EBITDA).

Year-end path (NOK per share):

| | End-2026 | End-2027 | End-2028 | Exit end-2029 |
|---|---|---|---|---|
| V_t Bear / **Base** / Bull | 82.8 (all) | 70.3 / **100.8** / 125.9 | 57.8 / **118.8** / 168.9 | 45.3 / **136.9** / 212.0 |
| r_t Base | −2.2% (stub, not annualised) | +21.8% | +17.9% | +15.2% |
| IRR to t: Bear / **Base** / Bull | −12.1% annualised (all; −2.2% over the stub) | −14.7% / **16.1%** / 40.4% | −16.1% / **16.9%** / 37.4% | −17.9% / **16.4%** / 33.6% |

- End-2026 V_t is NAV at Base marks at 31 Dec, the same in all scenarios. It is below P because
  Q4 FCF after debt service is negative and NOK 400m goes into growth equity at cost.
- Later V_t glide linearly to each scenario's V_T `[A]`: a path diagnostic, not used in IRR_T.
- D_t = 0, so r_t is the change in V_t.

## V_T bridge (Base, from NAV_0)

Re-rating P → NAV_0: NOK 84.65 → 80.0, −1.8% a year (P/NAV_0 1.06, just outside 0.95–1.05: the
price is slightly above Base NAV, so part of NAV growth is used to close that premium).

| Step | NOK m | per share |
|---|---|---|
| NAV_0 (Base mid-cycle marks, lives at today; UC and development equity at cost) | 12,788 | 80.0 |
| − Ageing of the existing portfolio (3 years of life at mid-cycle marks; incl. Ukraine FiT roll-off) | −1,283 | −8.0 |
| + Under construction: EV at T 5,916 − debt 3,000 − equity already in NAV_0 1,500 | +1,416 | +8.9 |
| + Growth equity at T: new equity 4,900 × 1.1 + F uplift on development equity 1,350 × 0.1 | +5,525 | +34.6 |
| + Project amortisation paid from EBITDA (after the valuation date) | +3,933 | +24.6 |
| − Rise in corporate NIBD (5,843 → 6,346), after paying 4,900 growth equity | −504 | −3.2 |
| ± Contract premium | 0 | 0 |
| ± Reversion tail | 0 | 0 |
| **V_T** | **21,875** | **136.9** |

- The contract premium needs no line: contracted blocks are valued over their remaining PPA life,
  so the premium is inside the mark.
- The reversion tail is zero: the only material gap (Ukraine) has a named reason (below).

Exit asset table (NOK m at T):

| | Bear | Base | Bull |
|---|---|---|---|
| Contracted EV | 16,664 | 19,975 | 22,627 |
| Under construction EV | 4,800 | 5,916 | 6,768 |
| Philippines EV | 2,870 | 5,495 | 8,546 |
| Ukraine EV | 100 | 360 | 570 |
| − Project NIBD | −13,100 | −13,100 | −13,100 |
| + Growth equity at F (development equity at 30 Oct + new equity) | 4,005 | 6,875 | 10,075 |
| + D&C platform | 420 | 2,700 | 4,485 |
| − Corporate NIBD | −8,513 | −6,346 | −6,086 |
| **V_T (per share)** | **7,246 (45.3)** | **21,875 (136.9)** | **33,884 (212.0)** |

**Backlog at exit:**
- Firm-today contracts are in the contracted and under-construction marks for their full term.
- Scenario-signed backlog is the growth equity at F. Valued at cost (F = 1.0, no premium), Base
  becomes **IRR 15.3%, P_k NOK 92.8 (+10%)**.

**Exit consistency** (Year 3 vs mid-cycle, open earnings):

| Row | Scenario | Year 3 | Mid-cycle | Gap | Treatment |
|---|---|---|---|---|---|
| Contracted | all | 2,150 / 2,380 / 2,500 | 2,150 / 2,390 / 2,500 | 0% | none needed |
| Under construction | all | 600 / 680 / 720 | same | 0% | none needed |
| Philippines | all | 450 / 750 / 1,000 | same | 0% | none needed |
| Ukraine | Base | 160 | 100 | +60% | **Named reason:** the 10-year feed-in tariffs expire in 2029, then merchant (Q3 report, Note 5). The tail would add NOK 0.3 a share (Base IRR +0.0 pp, P_k 95.7) |
| Ukraine | Bull | 250 | 150 | +67% | Same reason. Tail +NOK 0.5 a share (P_k 148.3) |
| D&C | all | 250 / 500 / 700 | 250 / 500 / 650 | 0% / 0% / +8% | below 10%: none needed |

**Exit cross-check** (against Equity BBB, Oslo):

| | Bear | Base | Bull | Oslo index |
|---|---|---|---|---|
| Exit P/E (V_T ÷ FCF_normalised before holdco G&A) | 6.0 | **9.8** | 12.9 | 11.5 (10.5 / 12.5) |
| Exit P/B (book NOK 60 / 71 / 78 a share at exit `[A]`) | 0.75 | **1.94** | 2.73 | 1.75 |
| Buyer's implied return | ~17.8% | **~11.4%** | ~8.9% | Mid-cycle 9.1% |

- FCF_normalised before holdco G&A is NOK 1,217 / 2,221 / 2,625m. Holdco G&A is NOK 130m a year.
- Buyer's implied return = asset rate (EV-weighted: 10.4 / 9.4 / 8.2%), levered by project and
  corporate debt at ~7.0% (Base D/E 0.89; Bear 2.98).
- The Base buyer earns more than the Oslo index, so the marks are not generous.
- Base exit P/B 1.94 is above Oslo's 1.75. The reason is that book carries the Q3 impairments and
  accounting depreciation on D&C-inflated costs, while the marks value contracted cash flows. The
  Bull exit P/E of 12.9 is above the Oslo Bull 12.5: Bull needs the Philippines and Egypt to be
  priced as quality.

## Growth capex test

- **Amount** (Q4 2026–2029): NOK 4.9bn of new equity in Base (Bear 3.1bn, Bull 6.4bn). The
  company target is NOK 8bn over 2027–2030. Under construction needs ~NOK 0.8bn more project
  debt; its equity is mostly paid in.
- **Return evidence:**
  - Scatec's stated hurdle is 1.2× cost of equity, about a 15% project equity IRR and cash yield
    `[F]` (presentation).
  - D&C gross margin is 10–12% guided, 11% underlying in Q3 `[F]`.
  - Scatec's funding illustration for the secured portfolio `[F]`: ~NOK 54bn capex, ~80%
    non-recourse debt, Scatec equity ~NOK 5bn, D&C gross profit ~NOK 4.2bn. The capital-light model
    funds more than half of Scatec's equity from the EPC margin (after D&C opex and 22% tax:
    ~NOK 2.8bn).
  - Priced farm-downs: NBE paid NOK 233m for 20% of Obelisk (Q2) and joins Dandara at 20%; EBRD
    takes 40% of the Egypt platform. Prices against cost are not disclosed `[?]`, so no premium is
    visible.
- **Value created** (Base): (1.1 − 1) × NOK 4.9bn = NOK 0.5bn on the stakes, plus D&C cash of
  ~NOK 1.4bn over the horizon. The equity IRR including D&C is ~12–14% `[A]`, above k but not by
  much.
  - The faster pace barely moves value in this model. At NOK 1.0bn a year instead of 1.5bn, Base
    P_k is 95.7: the 0.1 uplift on F is eaten by the 7.5% corporate funding cost while no project
    EBITDA is counted before exit.
- **Accretive in Base, destructive in Bear** (F 0.9: Egypt FX and payment risk, delays).
- **Growth quality:**
  - No new shares beyond 1.0m employee shares in Q1 2026.
  - Growth depends on Egypt (now ~56–80% stakes before the EBRD platform) and on farm-downs at or
    above cost.
  - It also raises corporate NIBD unless the NOK 3.4bn of divestments come through.

## Results

| | Bear | Base | Bull |
|---|---|---|---|
| IRR_T (dated, to V_T) | −17.9% | **16.4%** | 33.6% |
| IRR_T in NOK on the Equity BBB NOK path | −16.0% | 16.4% (spot flat) | 32.5% |
| d / g / c | 0 / −17.9% / 0 | **0 / 16.4% / 0** | 0 / 33.6% / 0 |
| g: re-rating / NAV growth (P/NAV_0) | −32.8% / +22.2% (3.53) | **−1.8% / +18.4% (1.06)** | +14.8% / +16.3% (0.65) |
| Structural IRR / cyclical | −17.8% / −0.0 pp | **16.0% / +0.3 pp** (Δd 0, Δg +0.3) | 33.2% / +0.3 pp |
| ΣD_t / V_T | 0 / 45.3 | **0 / 136.9** | 0 / 212.0 |
| P_k / margin of safety | 31.6 / −63% | **95.5 / +13%** | 148.0 / +75% |
| Rule 3: P/FCF normalised vs ceiling IRR_T/k² | 12.4x vs n/a (IRR < 0) | **6.5x vs 11.4x** | 5.4x vs 23.3x |
| Capital preserved? ΣD_t + V_T vs P | No (−46%) | Yes | Yes |

Notes:
- **NOK path:** cash flows are about 40% USD-linked and 60% other currencies, so V_T is scaled by
  0.4 × USD/NOK + 0.6 × I-44. The Bear factor is 1.072 at end-2029, the Bull factor 0.976.
  Corporate NOK bonds are swapped to USD, so they scale too.
- **Structural run:** every open day from 1 Jan 2027 at the scenario's own mid-cycle (Philippines,
  Ukraine and D&C at mid; contracted and under-construction rows already are). The paths are close
  to mid-cycle, so the cyclical part is small (+0.3 pp in Base, from Ukraine's FiT years and D&C
  above mid in 2028). **The scenarios are mid-cycle shifts:** the regime for the Philippine reserve
  market and the asset rate, not a cycle.
- **FCF_normalised** (Base, for Rule 3): mid-cycle power EBITDA 3,920 − tax and maintenance 9% +
  D&C 500 × 0.85 − project interest on exit NIBD 891 − corporate interest 476 − holdco 130 −
  renewal charge 404 (the ageing line ÷ T) = **NOK 2,091m = 13.1 a share**.
- **Scenario-weighted reference (convention, 25/50/25 on levels):** V_T 132.8, IRR 15.2%. Not the
  decision.
- **Share of Bull priced:** (84.65 − 95.5) / (148.0 − 95.5) = −21%. The price is below the Base
  hurdle.
- **Bear balance-sheet survival:**
  - Corporate NIBD rises from NOK 5.7bn (30 Sep) to **8.5bn by 2029** at NOK 0.9bn a year of
    growth, because FCF after debt service is ~0 in Bear.
  - Liquidity is NOK 3.9bn (free cash 1.2bn, undrawn old RCF 1.5bn, new USD 350m RCF capacity).
  - Maturities: SCATC05 NOK 1.45bn (Scatec plans to repay it in H1 2027 from liquidity), the RCF,
    the Norfund note USD 120m (Q1 2028) and SCATC06 NOK 1.25bn (Q1 2029). These would be refinanced
    in a Bear HY market (~+200 bp).
  - If growth stops after 2027 (only the committed Egypt equity), corporate NIBD peaks at ~NOK 7.1bn
    in 2027 and falls to 6.5bn. Bear then gives V_T 47.6 (IRR −16.6%).
  - Corporate bond covenants were not read `[?]`.
  - Likely outcome: survival with growth stopped, asset sales below marks, or an equity issue. Bear
    breaks the thesis.

**Sensitivity** (Base, one change at a time):

| Change | V_T | IRR_T | P_k | MoS |
|---|---|---|---|---|
| Base | 136.9 | 16.4% | 95.5 | +13% |
| Asset rate 10% (contracted and under construction) | 124.8 | 13.0% | 87.1 | +3% |
| Asset rate 8% | 150.2 | 19.8% | 104.8 | +24% |
| Philippines 450 a year (energy and BESS contracts only) | 117.5 | 10.9% | 82.0 | −3% |
| Philippines at the v1 Base (550 / 650 / 650) | 129.9 | 14.5% | 90.7 | +7% |
| Philippines 900 / 1,000 / 1,000 | 152.9 | 20.5% | 106.7 | +26% |
| Philippine asset rate 13% | 132.4 | 15.1% | 92.4 | +9% |
| Contracted EBITDA −NOK 150m (FX, Mendubim, Honduras, Pakistan) | 126.1 | 13.4% | 88.0 | +4% |
| No D&C platform value at exit | 120.0 | 11.6% | 83.7 | −1% |
| D&C at the v1 path (450 / 500 / 450) | 133.4 | 15.4% | 93.1 | +10% |
| Growth equity at cost (F = 1.0) | 133.0 | 15.3% | 92.8 | +10% |
| Growth equity NOK 1.0bn a year (v1 pace) | 137.1 | 16.4% | 95.7 | +13% |
| No working-capital release | 131.8 | 15.0% | 92.0 | +9% |
| k = 13% / 14% | 136.9 | 16.4% | 92.9 / 90.3 | +10% / +7% |

**Break-even Philippine EBITDA** (2028–29 and mid-cycle, 2027 at Base 700, all else Base): NOK
**~485m** for IRR = 12% (with 2027 at the same level: ~505m). NOK 400m gives 10.6%; 500m gives
12.3%; 600m gives 13.9%; 750m gives 16.4%.

## Verdict and caveat

- **Clears (Base margin of safety +13%). It does not survive Bear** (−63%, ~46% permanent loss).
- The Base verdict holds if all of the following hold:
  - the Philippines settles above ~NOK 485m a year once the market is redesigned;
  - buyers price contracted emerging-market renewables at ~10% or less;
  - the D&C/development platform keeps a value at exit.
- **Assumptions that would flip it:**
  - a redesign plus NGCP contracts that leave SNAP near energy-only (NOK 450m: −3%);
  - no value for the D&C platform (−1%);
  - an asset rate of 10% together with any second hit;
  - an Egypt setback (FX convertibility, payment delays) that turns growth equity below cost.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation or a price target.

## Tracking

**Q3 2026 (report 30 Oct 2026) against v1.1** (v1 had no full Q3 model; Q3 was implied from the
FY guide, and net debt was estimated at the 27 Oct valuation date):

| Item | v1.1 model | Q3 actual / new | Difference |
|---|---|---|---|
| Power EBITDA Q3 | ~890 (implied) | **1,070** `[F]` | +180 |
| Philippines EBITDA Q3 | inside guide 320–420 | **367** `[F]` | in range |
| Total proportionate EBITDA Q3 | not modelled | 1,208 `[F]` (D&C 168 incl. 140 one-off) | – |
| Cash flow to equity Q3 | not modelled | 385 `[F]` (power 442, D&C 138, corporate −195) | – |
| Power EBITDA H2 2026 (Q3 + Q4) | 890 + 1,050 = 1,940 | 1,070 + 873 = 1,943 | in line |
| Philippines EBITDA Q4 | ~120 | **250** (guide 200–300) | +130 |
| Corporate NIBD | 4.7bn (27 Oct est.) | **5.7bn** (30 Sep) | +1.0bn worse (working capital −0.75bn, investments −0.69bn) |
| Project NIBD | 16.7bn (27 Oct est.) | **16.4bn** (30 Sep) | −0.3bn (FX) |
| Total proportionate NIBD | 21.4bn | **22.1bn** | +0.7bn worse |
| Impairment | none | NOK 1,066m (Ukraine 952, Pakistan 114) | Ukraine value cut |

- **Base P_k: NOK 86.5 → 95.5 (+9.0, +10%)**; margin of safety +7% → +13% at a higher price
  (80.60 → 84.65). Bear P_k 34.0 → 31.6; Bull P_k 135.2 → 148.0.
  - Moved up by the Philippines (+5 on P_k), the D&C book and platform (+2), and the new
    development equity counted at F.
  - Moved down by the higher corporate NIBD, Ukraine (FiT to 2029, lower mid) and the stub's
    negative FCF.
- **Ahead of the Base path on earnings, behind on the balance sheet.**
  - Ahead: Q3 EBITDA beat the implied figure, and the Philippine suspension costs far less than v1
    assumed.
  - Behind: corporate NIBD is NOK 1.0bn above plan. Ukraine and Pakistan were impaired, and
    Mogobe slipped to H1 2027.

## Risks and signposts

- **Philippines (largest):**
  - Q4 report (29 Jan 2027): actual SNAP EBITDA against the 200–300 guide. Below 200 would point
    to Bear.
  - Any NGCP long-term AS contract for SNAP hydro or BESS, with price and tenor.
  - ERC redesign proposal (by ~12 Apr 2027): price caps against a longer-term contracted reserve
    market. A cap near energy prices moves Base towards the 485 break-even.
  - Q1–Q2 2027 (dry season): the first quarters where reserve revenue mattered most.
- **FX:** NOK strength (USD/NOK 9.19 against 10.39 on the 2025 average `[F]`) hits EBITDA in NOK
  directly; FY 2026 already −86m.
- **Egypt:**
  - EBRD platform closing and terms (cash to Scatec);
  - Shadwan and Dandara construction (COD H1 2028); Energy Valley financial close;
  - USD convertibility and timely payments from EETC; working capital in Egypt.
- **Corporate financing:** repayment of SCATC05 in H1 2027; release of the NOK 0.7bn RCF bridge;
  divestment proceeds towards the NOK 4bn gross debt target. Corporate NIBD above NOK 6.5bn
  without divestments would be a warning sign.
- **Problem assets:** Ukraine (standstill, further damage), Mendubim (covenant breach, debt
  current), South African DSCR tests in 2027 (Grootfontein, Mogobe), the Pakistan true-up (NEPRA,
  2027), Honduras receivables and performance.
- **Flagging and shareholder lists:** DNB AM at 5.03% (22 Oct). Fredly (Apollo Asset) 260,000
  shares (0.16%, DN 27 Oct). A flagging notice would come only above 5%.

## For other modules

- **No sector BBB change needed.** No baseline covers renewables.
- **HY BBB (information only; `hy-funds` reads this as an issuer credit check, loop):**
  - Scatec bonds sit in Sissener Corporate Bond (0.83%) and Fondsfinans High Yield (1.99%).
  - Credit read after Q3:
    - corporate NIBD NOK 5.7bn (up 1.1bn in Q3; 0.7bn of it a working-capital RCF bridge);
    - new SCATC08 at N+250 (the lowest margin yet);
    - liquidity NOK 3.9bn with the new RCF;
    - SCATC05 to be repaid in H1 2027.
  - Bear: corporate NIBD up to NOK 8.5bn by 2029 unless growth stops. Refinancing of Norfund
    (Q1 2028) and SCATC06 (Q1 2029) at Bear spreads.
  - These are a watch point, not a watchlist trigger. No bond price was checked. Whether to watch
    is for the HY skill to judge.

## Change log

- **2026-10-27 (v1):** first analysis. Base clears thinly (IRR 14.5%, P_k NOK 86.5 vs 80.6,
  +7%); Bear −14.7% (capital not preserved); Bull 31.8%. Built before the Q3 report (30 Oct).
  Fredly's buying could not be confirmed.
- **2026-10-27 (v1.1):** DN confirms the Fredly purchase: Apollo Asset holds 260,000 shares
  (0.16%, ~NOK 21m), most likely bought after 22 Oct. Pareto and Arctic views added. The price
  implies Philippine EBITDA of ~NOK 510m. No model value changed.
- **2026-10-30 (v2):** update after the Q3 2026 report. Price NOK 84.65; valuation date 30 Oct;
  iaf-valuation 2026-10-29.1. Base **clears** (IRR 16.4%, P_k NOK 95.5, +13%); Bear −17.9%
  (capital not preserved, ~46% loss); Bull 33.6%.
  - Changes, each tagged (v2) in Market input and the appendix:
    - Q4 stub from the FY guide (power 873, Philippines 250);
    - net debt from 30 Sep (corporate 5.7bn, project 16.4bn);
    - Philippines 700 / 750 / 750 (Q4 guide 200–300, mitigation plan);
    - D&C 480 / 580 / 500 (contract value NOK 10.5bn);
    - growth equity 1.5bn a year (target doubled to 2bn);
    - Ukraine lower after the impairment (FiT to 2029);
    - Mogobe in 2027;
    - corporate interest 7.5%;
    - amortisation 1.15–1.25bn;
    - Base working-capital release of NOK 0.7bn.
  - Tracking section added; the Fredly section is folded into Company and status.

## Appendix: own assumptions

| # | Assumption | Value | Why |
|---|---|---|---|
| A1 | Contracted asset rate | 10 / **9** / 8% | Emerging-market contracted solar/wind; USD-equivalent unlevered return for infrastructure buyers. Unchanged |
| A2 | Philippine asset rate | 13 / **11** / 9% | Merchant hydro with a regulatory reset. Unchanged |
| A3 | Mark structure | Contracted 16 yr PPA left at exit + 14 yr tail at 45%, +0.6% a year; Philippines 25 yr merchant, flat; conversion 0.87 | Factsheet PPA tenors and COD years; normalised cash tax 5% of EBITDA (FY 2025). Unchanged |
| A4 | Philippine EBITDA path (v2) | Bear 400 / 450 / 450; **Base 700 / 750 / 750**; Bull 900 / 1,000 / 1,000 | Q4 2026 guide 200–300 after the suspension (−80m impact) `[F]`; management "limited long-term effects" `[F]`; dry-season reliance on AS (Q2 2026: AS 199 of 244) `[F]`; redesign due ~Apr 2027 `[F]`; 3 new BESS on long-term AS contracts `[F]`. v1: 550 / 650 / 650 |
| A5 | Contracted EBITDA run rate | 2,350 Base | Q3 2026 ex Philippines and Ukraine NOK 625m, Q4 implied ~600 `[F]`; held below the H2 run rate for FX, Mendubim, Honduras and Pakistan. Unchanged |
| A6 | Under-construction EBITDA (v2) | 680 at maturity; 2027 270 (Base) | 12% EBITDA yield on ~USD 610m proportionate capex `[B]`; Mogobe COD H1 2027 `[F]` (v1: 300 in 2027) |
| A7 | Growth equity and value factor F (v2) | 0.9 / **1.5** / 2.0bn a year; 0.9 / **1.1** / 1.3; development equity at 30 Oct NOK 1.35bn | Company target NOK 2bn a year, >60% secured `[F]`; hurdle 1.2× CoE, ~15% project IRR `[F]`; NBE/EBRD entries, prices undisclosed `[?]`; Q3 development injections 383 `[F]`. v1: 0.7 / 1.0 / 1.2bn; development equity 1.0bn |
| A8 | D&C EBITDA and platform multiple (v2) | Base 480 / 580 / 500, mid 500; Bull 600 / 750 / 700, mid 650; multiples 6 / **10** / 11.5 | Remaining contract value NOK 10.5bn at 10–12% `[F]`; D&C opex ~NOK 275–300m a year `[F]`; Oslo exit P/E 11.5 (Equity BBB) as the Bull cap. v1: 450 / 500 / 450 |
| A9 | Q4 2026 stub (v2) | Power EBITDA 873; D&C 80; corporate −33; growth equity 400; amortisation 500 | FY guide midpoint 3,450 less YTD 2,577 `[F]`; Philippines guide 200–300 `[F]`; Q3 underlying D&C margin 11% `[F]` |
| A10 | Net debt at the valuation date (v2) | Corporate 5.84bn, project 16.33bn | 30 Sep actuals `[F]` rolled one month into Q4 |
| A11 | Interest (v2) | Project 6.8%; corporate 7.5% (+2 pp Bear from 2028) | Q3 2026 actuals `[F]`; SCATC08 at N+250 `[F]`; HY BBB Bear spread |
| A12 | No dividend | 0 in all scenarios | Self-funded growth and deleveraging strategy `[F]` |
| A13 | Book equity at exit (v2) | 9.6 / 11.3 / 12.4bn | Book 8,374 at 30 Sep `[F]` + the same attributable earnings as v1 |
| A14 | NOK path weights | 40% USD/NOK, 60% I-44 | Revenue currency mix from the factsheet (USD: Egypt, Pakistan, Jordan, Honduras, Laos, Release) |
| A15 | Working capital (v2, new) | Base +0.35bn in 2027 and 2028; Bear 0; Bull +0.7bn in 2027 | NOK 724m RCF draw called a short-term working-capital bridge `[F]`; 2025 release +1.7bn `[F]` |
| A16 | Ukraine path and today's value (v2, new) | Base 150 / 180 / 160, mid 100; EV today = mid × 3.6 + FiT years above mid (NOK ~500m) | Note 5: FiT expiry 2029, damaged plant back Jan 2028, 24% discount rate; recoverable amount NOK 1,011m consolidated `[F]` |
| A17 | Project amortisation and draws (v2, new) | 1.15 / 1.20 / 1.25bn; remaining draws 0.8bn | Q3 normalised repayments 292 a quarter `[F]`; NOK 1.0bn drawn in Q3 `[F]` |

## Appendix: sources

| Item | Source | As of |
|---|---|---|
| Price NOK 84.65, shares 159.83m, market cap, consensus, targets | Yahoo `SCATC.OL` (`get_quote`, `quote_summary`) | Close 30 Oct 2026 15:29 UTC |
| USD/NOK 9.1871, EUR/NOK 10.268 | Yahoo `NOK=X`, `EURNOK=X` | 30 Oct 2026 21:01 / 21:28 UTC |
| Q3 2026 report (key figures, segments, outlook, cash flow, notes 2–10, APMs, CFE breakdown) | `storage.mfn.se/c22a164a-0df7-4b00-835d-f49ee6658eb9/scatec-q3-2026-report.pdf` (33 pages; text extracted locally with pypdf, because Nordic Financial `parse_pdf_to_text` was not available) | 30 Sep 2026 (published 30 Oct) |
| Q3 2026 presentation (Philippine impact and mitigation, NIBD split and bridge, guidance bridge, strategy 2030, funding illustration, portfolio) | `storage.mfn.se/a/scatec/b1cf5e1e-c4f7-49d9-a39c-eb2e441f3dcc/scatec-q3-2026-presentation.pdf` (32 pages) | 30 Sep 2026 |
| Country EBITDA, CFE and debt, Q2 2025–Q3 2026 | Q3 2026 databook (`storage.mfn.se/19b73e98-de88-4052-b61d-e1b83bc3c710/scatec-q3-2026-databook.xlsx`, read with openpyxl) | 30 Sep 2026 |
| Newsweb results announcement | Not read: Nordic Financial connector not available in this run `[?]`; the full report covers it | 30 Oct 2026 |
| Q4 report date 29 Jan 2027 | scatec.com financial calendar | read 30 Oct 2026 |
| Q2 2026 report, presentation, databook (history, v1 inputs) | MFN storage links in v1.1 `[C]` | 30 Jun 2026 |
| Outlook revision; EBRD Egypt platform | MFN releases `[C]`; confirmed in Q3 report notes 10 and outlook | 21 and 22 Oct 2026 |
| Flagging: DNB AM 4.76% → 5.03% | MFN / Oslo Børs flagging notices `[C]` | 9 Oct and 23 Oct 2026 |
| ERC reserve-market suspension | BusinessWorld, Philstar `[C]`; Q3 report note 10 `[F]` | Press release 12 Oct 2026 |
| Fredly purchase; Pareto and Arctic views | DN, 27 Oct 2026 (text from the user) `[E]` `[C]` | 27 Oct 2026 |
| Oslo exit P/E, P/B, mid-cycle return; NOK path | `docs/equity-market-bbb.md` | 17–18 Oct 2026 |
| Bear refinancing spread | `docs/hy-market-bbb.md` | 24 Oct 2026 |
| USD/NOK 2025 average 10.3912 | Norges Bank EXR annual average (iaf-valuation skill text) | 2025 |

Validation flags:
- The consolidated Yahoo EPS and EV/EBITDA (19.0x) mix the consolidated and proportionate bases.
  They are not used.
- The Q3 D&C EBITDA (168) includes NOK 140m of Obelisk close-out; the underlying 11% margin is
  used for the stub.
- The presentation's "available liquidity NOK 3.9bn" includes the new RCF capacity effective
  29 Oct. The report's 30 Sep figure is NOK 2.7bn. Both are shown.
- The Philippine Q4 figure is guidance, not an actual. 2027 is an own assumption: no 2027
  Philippine guidance was given.
- Model: `scatec_v2.py` (scratchpad), rebuilt from the v1 description; contracted and Philippine
  marks reproduce v1 (8.36x and 7.33x at Base rates).
