# Global index funds — DNB Global Indeks A and Nordnet Global Indeks on the Equity BBB World blocks — 29 October 2026 (re-mark 29 Oct of the 18 Oct version)

> **Scope change from the next run (user, 1 Nov 2026):** Nordnet Global Indeks (Nordnet Indeksfond Global ESG) is no longer analysed. The next run covers DNB Global Indeks A only (on Nordnet and on the DNB pension platform) and drops the Nordnet fund's columns, triggers and the head-to-head. Its figures below are kept as of 29 Oct.

**Skill revisions used:**
- `iaf-valuation` **2026-10-18.2** (this run; the 18 Oct version used 2026-10-11.3): k = 12%,
  hurdle and margin-of-safety rules, exit principle and exit cross-check. **Method changes since
  2026-10-11.3, where they touch this document:**
  - *Exit principle* (V_T = the market price of a continuing business at the market's return at
    exit, never k): already practice here (World and block exit multiples from the Equity BBB and
    the AI BBB). No number changes.
  - *Exit cross-check against the equity market* (exit P/E, exit P/B, buyer's implied return):
    added as a short table under Return split. No number changes.
  - *NOK path label* (Bear and Bull in NOK on the Equity BBB path, decision at spot): already the
    form here (Base is spot flat). Track A dated IRR, backlog at exit and holdco G&A: not
    applicable to an index fund.
- Method of the index-fund build: as on 18 Oct, set by the then `equity-market-bbb` fund mode
  (**2026-10-18.4**; the World blocks at each index's weights, company analyses as own blocks,
  retained cash counted once, NAV-date pricing, World scenarios, NOK path, E / R decision rule,
  trigger convention). That skill is now **2026-10-24.1** and market only; this document runs under
  `iaf-valuation` and reads the Equity BBB document as an input. **Market only:** it neither reads
  nor writes `docs/portfolio-overview.md`.
- `ai-market-bbb`: document Update 5 (rev **2026-10-29.1**, method v2.1; read Update 2, rev
  2026-10-17.1, on 18 Oct).

**Inputs:**
- **`docs/equity-market-bbb.md` (17 Oct, amended 18 Oct twice; Update 1; unchanged since read):**
  World built from blocks with an **explicit rest at trend growth**: Microsoft, Alphabet and NVIDIA
  on their analyses, the other AI names on the AI BBB layers, energy on the oil path, and the rest
  (70% of earnings) at consensus −3%, then 5.5% a year. **World Base 5.2%** before fees at the
  16 Oct price; Bear −1.7%, Bull 10.2%; E / R 0.024. Energy payout 0.76, cash conversion 0.80;
  70% of World's earnings on USD/NOK and 30% on I-44. Exit references: World exit P/E 17
  (15 / 18.5), exit P/B 3.14 (2.46 / 3.69), mid-cycle return 8.2% (7.1 / 8.7).
- **`docs/ai-market-bbb.md` (Update 5, 29 Oct; read Update 2 of 17 Oct, so Updates 3 of 22 Oct
  and 4 of 24 Oct are also taken here):**
  - Update 3: **E-layer cash conversion −.10 / .10 / .30 → −.20 / .00 / .20** (taken: the E block
    reads it); E-layer Bear and Bull moved to the Microsoft, Alphabet and Amazon blend, with the old
    path kept as the "E rest" row for the unanalysed names (Meta, Oracle).
  - Update 4: kept unchanged.
  - Update 5: **E-layer Base 2027 .97 → .92** from the company check (Alphabet .835, Microsoft
    .956, Amazon .952 and the rest row .97). **Not applied to this document's E block** (Amazon,
    Meta, Oracle): the move comes from Alphabet's and Microsoft's own EPS, which this build already
    carries in its company blocks CG and CM. For the names in the E block the evidence is Amazon
    .952 and the rest row .97, a blend of .96 (gap −0.01, below the 0.05 rule). Applied as a
    sensitivity, it changes no figure at two decimals.
  - All other rows this document reads are unchanged since 17 Oct (H1–H4 and T paths and their
    cash conversion, all exit P/Es and payouts, the E-rest row).
- **`docs/msft-analysis.md` v3 (28 Oct, Q1 FY27; read v2 of 15 Oct):** Base EPS 20.77 / 23.40 /
  26.11 / 28.39 (+0.9–1.2% a year); V_T Bear 404.5 / **Base 692.1** / Bull 921.4; dividends
  unchanged.
- **`docs/googl-analysis.md` v2 (28 Oct, Q3; call addendum 29 Oct, model unchanged; read v1 of
  15 Oct):** Base core EPS 2027 13.45 → **12.66**; V_T Bear 215.1 → 202.6, **Base 390.1 → 371.1**,
  Bull 537.5 → 515.9; D_t unchanged.
  - Both company blocks keep the 15 Oct closes (the NAV date). Their interim values (end-2027,
    end-2028) are re-glided to that price with the analyses' own rule (core P/E glides from today's
    to the exit P/E; Bear at its exit P/E from end-2027) `[A]`. V_T, D_t and EPS are the analyses'
    figures.
- `docs/nvda-analysis.md` (v1, 17 Oct; calendarised, revenue-consistent Bear): company block,
  unchanged. `docs/tsm-analysis.md`: TSMC is not in MSCI World or the Climate Change index.
- `docs/oil-market-bbb.md` (17 Oct read; renewed 24 Oct, kept unchanged): Brent Base **88** / 77 /
  72 in 2027–29, mid-cycle 70; Bear 65 / 60 / 60.
- `docs/hy-market-bbb.md` (24 Oct, **kept unchanged**; read 17 Oct): Base NIBOR **4.38%** over the
  window (path unchanged); HY market Base 6.8% before fees; the HY market reference E / R
  **0.196** is now published there (unchanged).
- `docs/hy-funds-analysis.md` (18 Oct): HY market reference E / R **0.196** (the Nordic HY index
  after a typical 0.6% fee: Base 6.2%, E 1.82 pp, R 9.28 pp).

**This version** (sixth; 11, 12, 15, 17 and 18 Oct before) is an **input re-mark**. It:
- replaces the Microsoft block (v3) and the Alphabet block (v2) after their Q3 reports;
- takes the AI BBB's E-layer cash conversion of 22 Oct for the E block (Amazon, Meta, Oracle);
- keeps prices, NAVs and the stub at the **15 Oct NAV date**. The method needs one price date for
  the NAV, the block weights and the World price, and the 15 Oct set is consistent. Prices were
  therefore not re-marked; the move since then is a memo under Near term (World in NOK ≈ −1.7%,
  almost all NOK).

**Results:** both funds fall **0.08 pp in Base** (DNB on Nordnet 4.66 → **4.58%**, Nordnet 4.81 →
**4.73%** after cost). Alphabet's lower EPS path gives −0.06 pp, the E cash conversion −0.02 pp
and Microsoft 0.00. E / R falls to 0.008–0.012 against the HY reference 0.196. Nordnet stays
0.15 pp ahead in Base and 1.8 pp deeper in the 2027 Bear; **the model still cannot rank the two on
return.** The E / R trigger moves from −15.2% to **−15.5%** (DNB NAV ≈ 733). Verdicts unchanged.

## Summary

**Verdict**

- **What changed on 29 Oct: Alphabet, a little.**
  - **Alphabet v2** (Q3: Services margin −1 pp, Alphabet-level AI costs +$5bn, ATM dilution): Base
    EPS 2027 −6%, V_T −4.9%. As a block it now returns **2.4%** in Base (was 4.0%), Bear 2027
    −48.7% (was −45.2%). On the funds: **−0.06 pp** in Base.
  - **E-layer cash conversion** (AI BBB Update 3, −.20 / .00 / .20): the E block (Amazon, Meta,
    Oracle) builds more net debt; 6.4% → 6.0% as a block, **−0.02 pp** on the funds.
  - **Microsoft v3:** EPS +1%, V_T unchanged at 692; **0.00 pp**.
  - **The AI BBB's E 2027 point (.97 → .92) is not applied to the E block:** it comes from
    Alphabet's and Microsoft's EPS, already in their blocks here. As a sensitivity it changes
    nothing at two decimals (2027 EPS enters only through the dividend and the retained cash).
  - **World** on these inputs: 4.84% before cost at the 15 Oct price (18 Oct: 4.93%); 5.13% at the
    Equity BBB's 16 Oct price (its own figure 5.22%, on the 15 Oct company analyses).
- **The AI blocks:** World's AI part returns **4.6%** a year in Base (was 4.95%; Bear 2027
  −42.2%). NVIDIA is the best AI block (10.9%), but it has the same weight in both indices.
  Microsoft (8.9%) is the block that separates them: Nordnet holds 1.5× as much.
- **The two funds, after cost (NAV of 15 Oct):**

  | | DNB Global Indeks A (Nordnet 0.25% / DNB pension platform 0.21%) | Nordnet Global Indeks (0.19%) |
  |---|---|---|
  | Base to end-2029 | **4.58% / 4.62%** (18 Oct: 4.66 / 4.71) | **4.73%** (18 Oct: 4.81) |
  | Bear 2027 / window | −21.7% / −2.3% a year | **−23.5% / −3.0%** a year |
  | AI-only financing break, 2027 | −8.8% | **−11.3%** |
  | E / R (HY market reference 0.196) | 0.008 / 0.009 | 0.012 |
  | Margin of safety | −19.0% / −18.9% | −18.7% |

  - Nordnet leads by 0.15 pp in Base, from Microsoft's own path; on the layer path it would trail
    by 0.16 pp.
  - **The lead reverses if its rest premium halves** (4.17%; about half of that premium is
    Tesla). Its Bear is 1.8 pp deeper in 2027 and 2.5 pp deeper in an AI-only break.
  - Under the skill's rule the model cannot rank them on return. On E / R both are near zero.
- **Against the HY market, both funds are far behind:** E / R 0.008–0.012 against 0.196. Their Base
  (4.6–4.7% after cost) is below the HY market's 6.2% after a typical fee, and their one-year
  stress is ~2.8× HY's.
- **Both fail the IAF hurdle** (margin of safety −18.7% to −19.0%) and lose capital in Bear over
  the window (−6.8% to −9.0%).
- **Between the two funds (model): DNB Global Indeks A, on risk and structure** (unchanged). It
  has the shallower Bear and the smaller AI stress, is physically replicated, and holds plain MSCI
  World. Nordnet's fund is the cheaper on Nordnet and slightly ahead in Base. It carries more AI
  and Tesla, a swap structure and an index Nordnet has changed three times.
- **Triggers (NAV change from 15 Oct at unchanged earnings):**
  - **E / R = 0.196: DNB NAV ≈ 733 (−15.5%)**; Nordnet ≈ 192 (−16.4%).
  - Base = k: DNB ≈ 703 (−19.0%); Nordnet ≈ 187 (−18.7%).
  - Pre-alert, Base = the HY market's 6.2% after a typical fee: DNB ≈ 828 (−4.6%); Nordnet ≈ 221
    (−4.2%).
  - The Equity BBB's World trigger (−14.1% from 16 Oct = −14.8% from 15 Oct, NAV ≈ 740) is on the
    15 Oct company analyses; the DNB trigger adds the fund's cost and the new Alphabet block.
  - **Indicative NAVs, 28 Oct** (URTH × USD/NOK, not re-marked) `[A]`: DNB ≈ 853 (−1.7%),
    Nordnet ≈ 226: all triggers still well below.

**Decision table** (NAV of 15 Oct 2026 = 100; NOK, after the all-in cost, before tax)

| | DNB Global Indeks A, on Nordnet (0.25%) | DNB Global Indeks A, DNB pension platform (0.21%) | Nordnet Global Indeks (0.19%) |
|---|---|---|---|
| IRR_T to 31 Dec 2029, Bear / **Base** / Bull | −2.3 / **4.58** / 9.6% | −2.3 / **4.62** / 9.6% | −3.0 / **4.73** / 10.0% |
| 2027 return (Year 1), Bear / Base / Bull | −21.7 / 4.7 / 12.4% | −21.7 / 4.7 / 12.5% | −23.5 / 4.7 / 13.1% |
| NAV at end-2029, Bear / Base / Bull (from 867.98 / 230.31) | 813 / 1,001 / 1,159 | 814 / 1,002 / 1,160 | 211.0 / 266.7 / 311.7 |
| **Hurdle NAV P_k (k = 12%) / margin of safety** | **703 / −19.0%** | **704 / −18.9%** | **187.2 / −18.7%** |
| Capital preserved in Bear? (ΣD + V_T vs P) | No, −7.0% | No, −6.8% | No, −9.0% |
| NOK 1m at end-2029, Bear / Base / Bull | 937k / 1,153k / 1,335k | 938k / 1,154k / 1,337k | 916k / 1,158k / 1,354k |
| Year-1 stress on NOK 1m (Bear 2027) | ≈ −NOK 218k | ≈ −NOK 217k | ≈ −NOK 236k |
| **E / R** (HY market reference 0.196) | **0.008** | **0.009** | **0.012** |
| AI-only Bear (financing break, no recession): 2027 / window | −8.8% / 0.6% | −8.8% / 0.6% | −11.3% / 0.1% |
| Oil-shock side case, 2027 (not weighted; carried over) | ≈ −15% | ≈ −15% | ≈ −21% |
| Mid-cycle return after cost (Equity BBB World 8.2% before fees) | ≈ 8.0% | ≈ 8.0% | ≈ 8.0% |

**Per-year path** (NAV, accumulating; NOK after cost)

| | Now (15 Oct) | End-2026 (stub) | 2027 | 2028 | 2029 | Exit year 2030 (normalised) |
|---|---|---|---|---|---|---|
| **DNB GI A (on Nordnet)**: Base EPS (World blocks, CY27 consensus = 1.00) | | — | 0.968 | 1.000 | 1.040 | 1.087 |
| Base value multiple at year-end (V / next-year EPS, incl. retained cash) | 17.2 on CY27 (MSCI forward ≈ 18.1) | — | 17.6 | 17.3 | 17.0 | |
| Base return / NAV | 867.98 | +0.4% / 872 | +4.7% / 912 | +4.5% / 954 | +4.9% / 1,001 | |
| Bear return / NAV | | +0.4% / 872 | −21.7% / 683 | +8.4% / 740 | +9.9% / 813 | EPS 0.917 |
| Bull return / NAV | | +0.4% / 872 | +12.4% / 980 | +9.0% / 1,069 | +8.5% / 1,159 | EPS 1.194 |
| **Nordnet GI**: Base EPS (blocks, CY27 consensus = 1.00) | | — | 0.957 | 0.999 | 1.044 | 1.093 |
| Base value multiple at year-end | 18.1 on CY27 (MSCI forward ≈ 19.0) | — | 18.6 | 18.3 | 18.0 | |
| Base return / NAV | 230.31 | +0.4% / 231.2 | +4.7% / 242.1 | +4.9% / 254.0 | +5.0% / 266.7 | |
| Bear return / NAV | | +0.4% / 231.2 | −23.5% / 176.8 | +8.4% / 191.7 | +10.1% / 211.0 | EPS 0.918 |
| Bull return / NAV | | +0.4% / 231.2 | +13.1% / 261.6 | +9.6% / 286.8 | +8.7% / 311.7 | EPS 1.213 |

- The window IRR is the XIRR on dated flows (cash yield at mid-year), as in the baseline. The NAV
  CAGR to end-2029 is within 0.1 pp of it.

## Tags

`[F]` fact from a fund document, index factsheet, holdings file or market print · `[E]` external
or secondary · `[A]` own assumption · `[?]` not found or unverified.

## Header

| Item | DNB Global Indeks A | Nordnet Global Indeks (NOK) |
|---|---|---|
| Legal name, ISIN | DNB Global Indeks A, **NO0010582984** (Bloomberg DNBNGBI NO); classes A–H `[F]` | Nordnet Global Index – NOK Class (Acc), **IE00BMTD2J60**; marketed in Norway as Nordnet Global Indeks; launched as Nordnet Index Fund Global ESG `[F]` (KIDs 2021 and 2025) |
| Structure, domicile | Norwegian UCITS, DNB Asset Management; physical, **full replication** `[F]` | Sub-fund of PassIM Structured Funds plc, Irish UCITS. Management company Carne Global Fund Managers (Ireland); investment manager J.P. Morgan Mansart; co-manager Nordnet Fonder AB; depositary BNP Paribas, Dublin. **Synthetic**: holds EEA government bonds and/or developed-market equities and swaps their return for the index return with a J.P. Morgan counterparty. Expected tracking volatility ≤ 1%. Base currency EUR `[F]` (KID 3 Jun 2025) |
| Index | **MSCI World Index Net** (NOK), minus DNB's exclusions: tobacco, controversial weapons, cannabis, pornography, oil sands and coal ≥ 30% of revenue, DNB's responsible-investment list; SFDR art. 8 `[F]` | **MSCI World Climate Change Index**, net, USD (MXWOCLNU), since **3 Jun 2025**. Before that MSCI World Selection Index (switch date `[?]`), and at launch MSCI World ESG Leaders (KID 2021). Excludes tobacco, controversial weapons, thermal coal and severe controversies; keeps defence; SFDR art. 8 `[F]` |
| Launched | 24 Sep 2010 `[F]` | 29 Jun 2020; NAV series from 2 Sep 2020 at 100 `[F]` |
| NAV (price P) | **NOK 867.98, 15 Oct 2026** (DNB AM; latest published on 18 Oct) `[F]`; 870.97 on 14 Oct, 880.91 on 9 Oct | **NOK 230.31, 15 Oct 2026** (Nordnet; latest published on 18 Oct) `[F]`; 230.85 on 14 Oct, 234.44 on 9 Oct |
| Size | NOK 165.0bn in the fund, NOK 70.1bn in class A `[F]` | `[?]` (not published on Nordnet); 81,899 owners on Nordnet `[F]` (11 Oct) |
| Holdings | 1,240 (benchmark 1,248) `[F]` | Index: 1,188 constituents (MSCI World 1,249), 30 Sep 2026 `[F]` |
| **Cost** | Fund: 0.10% management fee, 0.01% transaction costs `[F]`. **All-in: 0.25% on Nordnet** (0.10% + 0.15% platform fee for external index funds) · **0.21% on DNB's pension platform** (0.10% + 0.10% DNB platform fee + 0.01% transaction costs) `[F]` | Fund: **0.00%** ongoing, 0.00% transaction costs (KID, 3 Jun 2025) `[F]`. **All-in: 0.19% on Nordnet** = Nordnet's platform fee for its own index funds `[F]`. Sold only on Nordnet |
| Tracking record | Fund vs benchmark: YTD 5.87 vs 5.64%, 1 y 9.03 vs 8.94% (15 Oct); annualised 3 y **−0.14**, 5 y **−0.11**, 10 y **−0.12**, since launch −0.22 pp (8 Oct); tracking error 0.24% `[F]` | 1 y +8.19% (15 Oct) `[F]`. Since the switch: in line with its index within the measurement noise (±0.3 pp). Under the old index (EUR class, 2022–24): −0.40 to −0.55 pp a year against a 0.30% fee `[E]` (forum reading of the annual report) |
| Currency | USD 72.8%, EUR 8.2%, JPY 5.8%, CAD 3.3%, GBP 3.2%, CHF 2.4%, AUD 1.6%, other 2.7% (3 Sep) `[F]`. **Unhedged** `[E/A]` | USA 75.4%, euro area 7.7%, Japan 5.2%, Europe ex euro 3.8%, Canada 2.7% (31 Aug) `[F]`. **Unhedged** `[F]` (KID) |
| Risk | SRI 4; 3-year volatility 13.09% (benchmark 13.02%); max drawdown −22.2% `[F]` | SRI 4; index 3-year volatility 13.58% (MSCI World 11.85%), beta 1.03 `[F]` |
| Track | Index fund on the Equity BBB World build: **company blocks (Microsoft, Alphabet, NVIDIA) + AI layer blocks + energy + the explicit rest**, exactly as the baseline. Nordnet = the same blocks at its own weights; its rest carries the non-AI tilt premium | |
| k | **12%**, standard for both | |
| FX | USD/NOK 9.4931 (Yahoo, 15 Oct close); Equity BBB scenario paths applied relative to spot: 70% of earnings on USD/NOK, 30% on I-44 (Bear ×1.108 / 1.081 / 1.081, Bull ×0.973; Base flat) `[F/A]` | |

## Scenario definitions

Both funds use the Equity BBB's **World scenarios**, which now carry the AI BBB mechanism and the
company analyses inside the World blocks. 25/50/25 is a convention only, never a probability.

| Scenario | Equity BBB anchor | AI blocks (AI BBB v2.1, Update 5) | Microsoft, Alphabet, NVIDIA | Energy and rest | Earliest | Signposts |
|---|---|---|---|---|---|---|
| **Base** | World Base: oil Base (Brent 88 / 77 / 72), Norges Bank on the MPR path, AI boom slowing to trend; value multiple 17.2 → 17.0; NOK spot flat | **Contracted 2027 build, then digestion:** capex +42% in 2027, then +12% and +4%; compute EPS 0.92 → 0.97; memory to 35% of the 2027 consensus; platforms +9% a year. Hardware turns most earnings into free cash; platforms burn it in 2027 and keep none in 2028 (c −.20 / .00 / .20) | MSFT v3: EPS 20.77 in 2027, then +9–13% a year, exit core P/E 23. GOOGL v2: core EPS 12.66 in 2027, then +10–13% a year, exit 21; no buybacks, ATM dilution. NVDA: calendarised CY27 $15.21, EPS .92 / .98 / 1.00 / .97 | Energy falls ~31% from 2027 (Brent 88 → 70); **the rest: consensus −3% in 2027, then 5.5% a year**; rest multiple 17.2 / 16.7 / 16.3 | Ongoing | Capex guidance within ±10% (Q3: no 2027 figures; Alphabet 2026 unchanged, Microsoft CY26 ~170bn); NVIDIA within its guide (17 Nov); rest-of-World CY27 revisions within ±5% |
| **Bear** | World Bear: recession H1 2027 + oil Bear; World EPS 0.80 of CY27 consensus in 2027; USD/NOK +12%, I-44 +8%; value multiple to 15 | **Financing break + monetisation disappointment.** Revenue-consistent Bears: compute .68 / .50 / .53 / .57, foundry and equipment .76 / .63 / .67 / .71, networking .75 / .54 / .56 / .65. Multiples at the Bear exit by end-2027 | MSFT −30% in NOK in 2027; GOOGL −49%; NVDA −43% | Energy on the oil Bear; **rest .83 / .87 / .95 / 1.02**, multiple ~15; Nordnet's rest premium halves | H1 2027 | US HY OAS > 450 bp; MSCI World forward P/E < 15.5; lab run-rate growth < 10% q/q twice; a hyperscaler guides capex flat/down; new vendor loans or guarantees > USD 50bn in a quarter, or one called; platform equity funding (Alphabet's Q3 ATM sales crossed the AI BBB's Bear side) |
| **Bull** | World Bull: soft landing, oil Base; value multiple to 18.5; USD/NOK −3%, I-44 −2% | **Agentic adoption:** lab revenue +130% in 2027; capex to USD 1.3–1.7tn | MSFT +25%, GOOGL +22%, NVDA +33% in NOK in 2027 | **Rest 1.00 / 1.07 / 1.14 / 1.21**, multiple ~17.5 | Q2 2027 | S&P CY27 consensus holds ≥ +15%; 2027 capex consensus > USD 1.3tn; lab run-rate > USD 250bn by mid-2027 |

- **AI-only stress** (AI and company blocks on Bear; energy, rest and NOK on Base): 2027
  **DNB −8.8%, Nordnet −11.3%**; window 0.6% and 0.1% a year. AI-only Bull: 7.6% and 8.2%.
- **Side case (not weighted): oil Bull / stagflation.** World ≈ −15% in 2027 (Equity BBB);
  Nordnet ≈ −21% (no energy cushion, growth multiples fall more, as in 2022). Carried over; not
  rebuilt on the blocks.
- Tail risks not modelled (as in the AI BBB): a Taiwan conflict and export-control escalation.
  Neither fund holds TSMC, but both hold its customers.

## AI exposure and the World blocks

**Mapping** `[A]`: the AI BBB's basket names in MSCI World, at the iShares MSCI World ETF (URTH)
weights of 9 Oct, repriced to the 15 Oct closes `[F]`, as in the Equity BBB World build.

| Block | Names in MSCI World | Path source |
|---|---|---|
| **CM** Microsoft | Microsoft | `docs/msft-analysis.md` v3 (28 Oct): per-share V_t, D_t, EPS per scenario, at $539.44 (interim V_t re-glided from the analysis's $531.01) |
| **CG** Alphabet | Alphabet A + C | `docs/googl-analysis.md` v2 (28 Oct): at $349.22 (A) and $344.91 (C) (interim V_t re-glided from $324.89) |
| **CN** NVIDIA | NVIDIA | `docs/nvda-analysis.md`, calendarised, revenue-consistent Bear: at $217.23 |
| **E** platforms | Amazon, Meta, Oracle | AI BBB "E rest" row (the E path for names outside the company blocks: .97 / 1.07 / 1.17 / 1.27 Base), E-layer exit P/E, payout and cash conversion (−.20 / .00 / .20) |
| **H1** compute | Broadcom, AMD, Marvell | AI BBB H1 |
| **H2** memory | Micron (SK hynix and Samsung are emerging markets) | AI BBB H2 |
| **H3** equipment | ASML, Applied Materials, Lam Research (TSMC is an emerging market) | AI BBB H3 |
| **H4** networking and DC | Arista, Vertiv, Eaton | AI BBB H4 |
| **T** software | Palantir, SAP, Salesforce, ServiceNow, Snowflake, Adobe, Datadog, Intuit | AI BBB T |
| **EN** energy | MSCI World energy | Oil BBB: (Brent − 30) / 49; payout 0.76; cash conversion 0.80 |
| **Rest** | Everything else | Equity BBB explicit rest path |

- **Wider list, left in the rest:** Cisco, CrowdStrike, Palo Alto, GE Vernova, KLA, SanDisk,
  Amphenol, Shopify, Advantest, Tokyo Electron, Dell, Kioxia, Corning and smaller names, ~4.1% of
  MSCI World `[F]`. **Apple and Tesla** are not in an AI BBB layer.
- **Nordnet's weights** `[A]`: Microsoft ×1.47, Amazon ×1.42, AMD ×2.25 and Broadcom ×1.35 (MSCI
  30 Sep ratios); NVIDIA, Alphabet and Meta ×1.0; Micron ×1.21 and Marvell 0.47% (Nordnet,
  31 Aug); ASML ×0.55; others ×1.0 (sensitivity ×0.7 / ×1.3).

| Block (15 Oct) | MSCI World: weight / P/E CY27 / share of CY27 earnings | Climate Change: weight / P/E / earnings share |
|---|---|---|
| CM Microsoft | 4.18% / 24.8 / 2.9% | **6.17%** / 24.8 / 4.5% |
| CG Alphabet | 4.02% / 23.1 / 3.0% | 4.02% / 23.1 / 3.2% |
| CN NVIDIA | 5.49% / 14.3 / 6.6% | 5.47% / 14.3 / 7.0% |
| E Amazon, Meta, Oracle | 4.74% / 22.3 / 3.7% | 5.91% / 22.6 / 4.7% |
| H1 Broadcom, AMD, Marvell | 2.94% / 22.4 / 2.3% | **5.00%** / **24.3** / 3.7% |
| H2 memory (Micron) | 1.16% / 4.8 / 4.1% | 1.41% / 4.8 / 5.3% |
| H3 equipment | 1.47% / 25.5 / 1.0% | 1.15% / 25.2 / 0.8% |
| H4 networking and DC | 0.47% / 28.3 / 0.3% | 0.48% / 28.3 / 0.3% |
| T software | 1.55% / 26.6 / 1.0% | 1.55% / 26.6 / 1.1% |
| **AI layers + companies** | **26.0% / 18.0 / 24.8%** | **31.2% / 18.5 / 30.5%** |
| Energy | 4.32% / 15.2 / 4.9% | 0.31% / 15.2 / 0.4% |
| Rest | 69.7% / 17.1 / 70.3% | 68.5% / **18.0** / 69.1% |
| **Index** | **100% / 17.2** | **100% / 18.1** |

**Each block alone** (before cost, NOK; IRR Bear / **Base** / Bull, and the 2027 Bear year):

| Block | MSCI World composition | Climate Change composition |
|---|---|---|
| **CN NVIDIA** | −11.0 / **10.9** / 23.6 · −43.0% | same |
| **CM Microsoft** (v3; 18 Oct −5.3 / 8.9 / 17.8 · −29.5%) | −5.5 / **8.9** / 17.9 · −29.8% | same |
| **CG Alphabet** (v2; 18 Oct −11.5 / 4.0 / 13.9 · −45.2%) | −13.1 / **2.4** / 12.5 · −48.7% | same |
| E Amazon, Meta, Oracle (cash conversion −.20 / .00 / .20; 18 Oct 6.4 / 5.9 in Base) | −3.3 / **6.0** / 12.0 · −26.1% | −3.7 / 5.5 / 11.4 · −27.2% |
| H1 Broadcom, AMD, Marvell | −23.4 / **−5.1** / 5.9 · −65.1% | −25.2 / **−7.4** / 3.3 · −67.7% |
| *All compute (H1 + CN)* | *−14.9 / 5.8 / 18.0 · −50.7%* | *−17.2 / 2.9 / 14.8 · −54.8%* |
| H2 memory (Micron) | −13.7 / **−0.4** / 9.2 · −35.6% | same |
| H3 equipment | −20.1 / **−2.7** / 6.6 · −59.2% | −19.8 / −2.4 / 7.0 · −58.8% |
| H4 networking and DC | −23.2 / **−3.9** / 5.3 · −65.7% | same |
| T software | −10.8 / **−0.3** / 7.2 · −43.9% | same |
| **AI layers + companies** (18 Oct 4.95 / 4.3 in Base) | **−10.8 / 4.6 / 14.3 · −42.2%** | **−11.1 / 4.0 / 13.5 · −42.7%** |
| Energy | −15.9 / **−6.9** / −5.6 · −46.6% | same (0.3% weight) |
| **Rest** | **1.5 / 5.5 / 8.9 · −12.2%** | 0.6 / 5.4 / 8.7 · −14.5% |

- **The rest now returns a little more than the AI part** (5.5% against 4.6%). On 17 Oct the
  implied rest returned 7.5% and carried World; on the explicit trend path it does not.
- **The rest's Bear is deeper** (−12.2% in 2027, was −7.4% on 17 Oct): the baseline gives the rest
  its own recession path (EPS 0.83 of consensus) instead of what was left after the AI Bear.
- **Alphabet is now the weakest company block** (2.4% in Base, −48.7% in the 2027 Bear): its Q3
  cut the Base EPS path ~6% while the price at the NAV date (15 Oct, $349) is 7% above the
  analysis's $324.89. At the analysis's own price it returns 4.6%.
- **Microsoft is the block that separates the funds:** Nordnet holds 6.2%, World 4.2%. NVIDIA is
  the best block but the same weight in both.
- **Nordnet's compute tilt is the clearest cost of its tilt:** AMD at 2.25× its World weight takes
  the non-NVIDIA compute block from P/E 22.4 to 24.3 (−7.4% vs −5.1%).
- **Developed-market indices hold the dearer half of AI hardware:** Micron at P/E 4.8 against 3.3
  for the AI BBB memory basket with SK hynix and Samsung; ASML, Applied and Lam at 25.5 against
  TSMC at ~18.

## Funds and status

**Index composition** (MSCI factsheets, 30 Sep 2026; October factsheets not yet out) `[F]`:

| Sector | MSCI World | MSCI World Climate Change | Active |
|---|---|---|---|
| Information technology | 31.78% | **37.21%** | **+5.4** |
| Consumer discretionary | 8.36% | 11.19% | +2.8 |
| Health care | 9.20% | 10.92% | +1.7 |
| Real estate | ~1.5% | 2.21% | +0.7 |
| Utilities | 2.30% | 2.39% | +0.1 |
| Communication services | 8.31% | 8.14% | −0.2 |
| Financials | 15.74% | 14.70% | −1.0 |
| Materials | 3.21% | 1.83% | −1.4 |
| Consumer staples | 4.77% | 2.78% | −2.0 |
| Industrials | 10.80% | 8.32% | −2.5 |
| **Energy** | **4.03%** | **0.30%** | **−3.7** |

| Top 10 of the Climate Change index (30 Sep) | Weight | Weight in MSCI World | × | P/E on CY27 consensus (15 Oct) `[F/A]` | Block |
|---|---|---|---|---|---|
| Microsoft | 5.88% | 4.00% | 1.5 | 24.8 | CM |
| NVIDIA | 5.78% | 5.81% | 1.0 | 14.3 (calendarised) | CN |
| Apple | 5.53% | 5.41% | 1.0 | ~36 (fwd) | rest |
| Amazon | 3.79% | 2.67% | 1.4 | 24.1 | E |
| **Tesla** | **2.95%** | 1.12% | **2.6** | **~165** | rest |
| **AMD** | **2.48%** | 1.10% | **2.3** | 35.7 | H1 |
| Broadcom | 2.37% | 1.76% | 1.3 | 17.7 | H1 |
| Alphabet A / C | 2.23% / 1.75% | 2.23% / 1.76% | 1.0 | 23.2 / 22.9 | CG |
| Meta | 1.77% | 1.76% | 1.0 | 21.7 | E |
| **These ten** | **34.53%** | 27.63% | | | |

- **What the tilt does:** it buys Microsoft, Amazon, AMD, Broadcom and Tesla, and sells energy,
  staples, materials and industrials. Of Nordnet's +5.2 pp of AI weight, platforms and Microsoft
  are +3.1 pp (Microsoft +2.0) and compute +2.1 pp (all of it outside NVIDIA).
- **DNB Global Indeks A** holds MSCI World less 8 names `[F]`.

**Record** (NOK, %; DNB from DNB AM's table, labels read in order, checked against Yahoo NAV for
2023–2024; Nordnet from Yahoo NAV) `[F]`:

| Year | DNB GI A | MSCI World NOK (DNB benchmark) | Nordnet GI | Nordnet's index that year |
|---|---|---|---|---|
| 2016 | 4.16 | 4.55 | — | — |
| 2017 | 15.45 | 16.31 | — | — |
| 2018 | −3.43 | −3.36 | — | — |
| 2019 | 29.46 | 29.56 | — | — |
| 2020 | 13.64 | 12.93 | (+5.1 from 2 Sep) | ESG Leaders |
| 2021 | 25.50 | 25.46 | 27.53 | ESG Leaders / Selection |
| 2022 | −9.05 | −8.56 | **−10.33** | Selection `[?]` |
| 2023 | 27.81 | 27.62 | 29.07 | Selection |
| 2024 | 32.75 | 32.71 | 31.14 | Selection |
| 2025 | 6.97 | 7.55 | 7.82 | Selection → Climate Change (3 Jun) |
| 2026 to 8 Oct | 6.67 | 6.42 | 5.98 | Climate Change |
| 3 y / 5 y cumulative to 8 Oct | 56.16 / 94.06 | 56.71 / 94.95 | 54.63 / 92.63 | |
| 9 → 15 Oct 2026 | −1.47 | — | **−1.76** | Climate Change |

- **DNB tracks its benchmark closely:** within 0.1 pp a year after its 0.10% fee over 3–10 years
  `[F]`; YTD to 15 Oct +0.23 pp ahead (5.87 vs 5.64%).
- **Nordnet's record is mostly on other indices;** since the switch it is level with DNB
  (−0.3 pp over 16 months). In the AI sell-off of 9–15 Oct it fell 0.3 pp more.
- **The Climate Change index itself** (net, USD, MSCI; back-tested before 20 Jun 2019) `[F]`:

| | 2022 | 2023 | 2024 | 2025 | 1 y to Sep-26 | 3 y ann. | 5 y ann. | 10 y ann. | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| World Climate Change | **−22.86** | 31.25 | 24.99 | 20.30 | 14.86 | 23.39 | 13.01 | 14.08 | −33.0% (Covid) |
| MSCI World | −18.14 | 23.79 | 18.67 | 21.09 | 15.24 | 21.40 | 11.89 | 12.81 | −34.0% (Covid) |

## Near term

- **Stub (17 Oct–31 Dec 2026, 75 days):** price flat by convention; cash accrual less cost
  **+0.4%** for both, the same in all scenarios.
- **Price since the NAV date (memo, not re-marked)** `[F/A]`: URTH 208.11 (15 Oct) → **208.07**
  (28 Oct close, −0.02% in USD); USD/NOK 9.4931 → **9.334** (−1.7%). World in NOK ≈ −1.7%, so DNB
  NAV ≈ 853 and Nordnet ≈ 226 (indicative). The move is almost all NOK. A NOK move shifts the NAV
  and the NAV triggers together (Base is spot flat), so Base and the trigger distances barely
  change. Alphabet fell a further 10% after hours on 28 Oct ($292.50; its analysis gives 8.1% there
  against 4.6% at the close). On its ~4% weight that is ~0.4% off the NAVs, worth ~+0.1 pp of
  Base at a re-mark `[A]`.
- **Next reports for the 2027 AI path:** Amazon Q3 (29 Oct, after the US close; the AI BBB's small
  update follows on 30 Oct), NVIDIA Q3 FY27 (17 Nov), AMD (November) for Nordnet's tilt. Microsoft
  and Alphabet reported on 28 Oct (in this re-mark); their CY27 consensus is not yet revised.
- **Rates:** the Fed (early November); Norges Bank on 5 Nov (the HY BBB is stale after it).
- **MSCI's November index review** re-weights the Climate Change index.

## Market input (how the baselines enter)

| Input | From | Used as |
|---|---|---|
| World blocks: company, AI layer and energy blocks with the AI BBB paths and cash conversion; **rest EPS** Bear .83 / .87 / .95 / 1.02 · **Base .97 / 1.023 / 1.080 / 1.139** (5.5% a year) · Bull 1.00 / 1.07 / 1.14 / 1.21; **rest multiples** Bear 15.08 / 14.96 / 14.86 · **Base 17.17 / 16.67 / 16.29** · Bull 17.78 / 17.61 / 17.44; rest payout ~0.48–0.50 | `docs/equity-market-bbb.md` (18 Oct), `references/upd.py` | DNB = World on this build; Nordnet = the same blocks at its weights, rest with its premium |
| Energy: payout 0.76, cash conversion 0.80; Brent Base 88 / 77 / 72, mid-cycle 70; Bear 65 / 60 / 60 | Equity BBB; `docs/oil-market-bbb.md` (17 Oct) | Energy block (IXC +2.5% since 9 Oct) |
| FX: 70% USD/NOK (Bear 10.70 / 10.42 / 10.42 and Bull 9.27, relative to 9.5555), 30% I-44 (Bear +8% / +6% / +6%, Bull −2%); Base flat | `docs/equity-market-bbb.md` | Whole index, relative to the 15 Oct spot |
| **AI layer paths, v2.1**: EPS, exit P/E, payout, cash conversion; E block on the "E rest" row with the E-layer cash conversion −.20 / .00 / .20 (Update 3); the E-layer Base 2027 point .92 (Update 5) as a sensitivity only | `docs/ai-market-bbb.md` (Update 5, 29 Oct) | Layer blocks |
| **NVIDIA (v1), Microsoft (v3), Alphabet (v2):** per-share V_t, D_t, EPS per scenario; Microsoft's and Alphabet's interim V_t re-glided to the 15 Oct closes `[A]` | Company analyses (17 and 28 Oct) | Company blocks at the 15 Oct closes |
| Prices 15 Oct of every block name, URTH 208.11, IXC 61.38, USD/NOK 9.4931, EUR/USD 1.1195 | Yahoo chart API (`close.py`) | Block weights and the World price at the NAV date (+0.85% vs 16 Oct) |
| Base 3M NIBOR → **4.38% over the window** (HY BBB 24 Oct, kept unchanged) | `docs/hy-market-bbb.md` | E = Base IRR − NIBOR |
| HY market reference E / R 0.196; HY market Base 6.8% before fees, 6.2% after a typical 0.6% fee | `docs/hy-market-bbb.md` (published there since 24 Oct), `docs/hy-funds-analysis.md` | Decision rule and triggers |
| Check: on the 18 Oct inputs, at the baseline's 16 Oct prices and zero cost, the World run gives −1.72 / 5.22 / 10.22%, 2027 −20.6 / 5.6 / 13.4%, E / R 0.024 (after 0.20%): the Equity BBB's figures exactly. On the 29 Oct inputs: −1.80 / **5.13** / 10.14%, 2027 −20.8 / 5.4 / 13.2%, E / R **0.021** | `docs/equity-market-bbb.md` | Consistency; the difference is flagged to the Equity BBB |

## Look-through valuation

| Measure | MSCI World (DNB) | World Climate Change (Nordnet) | Source |
|---|---|---|---|
| Forward P/E (30 Sep) → 15 Oct (× URTH move) | 17.92 → **18.1** | 18.93 → **19.0** (×1.056) | MSCI factsheets `[F]`; scaled `[A]` |
| P/E on CY27 consensus, 15 Oct | **17.2** | **18.1** | Equity BBB × price move `[A]` |
| Trailing P/E / P/BV / dividend yield (30 Sep) | 22.69 / 4.10 / 1.52% | 24.11 / 4.53 / 1.34% | `[F]` |
| AI layers + companies: weight / P/E | 26.0% / 18.0 | 31.2% / 18.5 | URTH, AI BBB consensus, company analyses `[F/A]` |
| Rest: P/E | 17.1 | 18.0 (×1.054; ex Tesla ×1.03) | derived |
| Energy: weight / share of CY27 earnings | 4.32% / 4.9% (P/E 15.2) | 0.31% / 0.4% | URTH, IXC `[F/A]` |

- **World Base EPS** (sum of blocks): 0.968 / 1.000 / 1.040 / 1.087 of CY27 consensus (+2.6% a
  year; 18 Oct 0.970 / 1.001 / 1.042 / 1.088, the difference is Alphabet v2), against 0.95 /
  1.017 / 1.078 / 1.137 on the old top-down path. The AI and company part is about flat after 2027
  (0.93 → 1.00), energy falls, and the rest grows 5.5% a year.
- **Nordnet's Base EPS** is 0.957 / 0.999 / 1.044 / 1.093: a lower 2027 (no energy at Brent 88,
  more AI with a Year-1 haircut), then slightly faster growth.
- **The AI BBB's −0.5% on World's 2027 EPS** (its downstream note for Update 5) is for a World
  that holds Microsoft and Alphabet on the E layer. Here they are company blocks, and their own Q3
  changes (Alphabet −6%, Microsoft +1% in 2027) move World's 2027 EPS by −0.2%. Applying the .92
  point to the E block as well would count Alphabet's cut twice (a further −0.2% in 2027, nothing
  in IRR).
- **Nordnet's rest premium:** 18.0 vs 17.1 (×1.054) on CY27. About half is Tesla (3.0% of the
  index at a P/E of ~165, against 1.2% of World). Kept in Base and Bull, half lost in Bear.
- **Data handling:**
  - Block weights: URTH 9 Oct weights (ticker + country) repriced to the 15 Oct closes; Alphabet A
    and C at their own prices; SAP in EUR × EUR/USD; the ASML line at the ADR's move.
  - CY27 consensus: the AI BBB's calendarised figures of 17 Oct (kept on 29 Oct, the Equity BBB's
    basis; the Microsoft and Alphabet consensus is not yet revised after their reports).
  - Index prices: World −0.5% in USD since 9 Oct (URTH); the Climate Change index a further −0.3%,
    inferred from the two NAVs (Nordnet −1.76% vs DNB −1.47%, both NOK).
  - NAVs: 15 Oct, the latest published on 18 Oct. The baseline is priced at 16 Oct; the funds are
    run at the 15 Oct index level with the baseline's paths (the skill's NAV-date rule).

## Common assumptions

| Item | DNB Global Indeks A (MSCI World) | Nordnet Global Indeks (Climate Change) | Basis |
|---|---|---|---|
| Microsoft, Alphabet, NVIDIA | Company V_t, D_t, EPS per scenario (MSFT v3, GOOGL v2, NVDA v1); their cash is inside V_t; MSFT and GOOGL interim V_t re-glided to the 15 Oct closes; block CY27 consensus kept at 21.75 / 15.05 (Equity BBB basis) | Same | Company analyses |
| AI layer blocks: EPS path (Base), exit P/E, payout | E (E-rest row) .97/1.07/1.17/1.27, exit 21, 34% · H1 .92/.98/1.00/.97, 17, 25% · H2 .90/.60/.40/.35, 10, 15% · H3 .95/1.03/1.10/1.16, 18, 45% · H4 .95/1.02/1.07/1.11, 20, 35% · T .95/1.03/1.11/1.19, 20, 45%. Bear (v2): H1 .68/.50/.53/.57, H3 .76/.63/.67/.71, H4 .75/.54/.56/.65; E (Amazon, Meta, Oracle) .88/.88/.97/1.05; Bull E 1.00/1.13/1.27/1.41 | Same | `docs/ai-market-bbb.md` (Update 5) |
| Cash conversion c (Base 2027 / 28 / 29) | **E −.20 / .00 / .20** (Bear −.10 / .30 / .50; Bull −.30 / −.20 / .00; 18 Oct −.10 / .10 / .30) · H1 .80 / .90 / .90 · H2 .70 / .65 / .60 · H3 .75 / .80 / .82 · H4 .90 · T .80 · energy .80; (c − payout) × EPS accumulates into V_t | Same | AI BBB v2.1 (22 Oct); Equity BBB |
| Layer P/E path | Base and Bull glide from the 15 Oct block P/E to exit; Bear at the exit level at end-2027 | Same | Fund mode, AI BBB |
| Energy | 4.32% of value; EPS (Brent − 30) / 49; P/E 15.2 → exit 11 / 12 / 13; payout 0.76 | 0.31% | Equity BBB |
| Rest | Equity BBB explicit path (EPS, multiple, payout) | Same EPS and payout; multiple × 1.054 in Base and Bull, × 1.027 in Bear | Equity BBB; `[A]` for the premium |
| Currency | 70% USD/NOK, 30% I-44, relative to spot | Same | Equity BBB `[A]` |
| Cost (all-in) | 0.25% (Nordnet) · 0.21% (DNB pension platform) | 0.19% | `[F]` |
| Tracking beyond cost | 0 | 0 (sensitivity +0.20% swap drag) | `[A]` |
| Triggers | Price change at unchanged earnings and unchanged future values (Equity BBB convention) | Same | Equity BBB `triggers.py` |

## Return split, structural run and sensitivities

| Window, % a year | DNB on Nordnet: Bear / **Base** / Bull | Nordnet: Bear / **Base** / Bull |
|---|---|---|
| IRR_T (after cost) | −2.31 / **4.58** / 9.56 | −3.00 / **4.73** / 10.02 |
| d (cash yield) | 2.35 / **2.65** / 2.74 | 2.13 / **2.37** / 2.46 |
| g (value growth, P → V_T) | −4.77 / **1.93** / 6.91 | −5.23 / **2.37** / 7.65 |
| — normalised EPS growth (USD) | −2.66 / **2.63** / 5.69 | −2.64 / **2.82** / 6.20 |
| — value-multiple change (CY27 basis → exit, incl. retained cash) | −4.28 / **−0.43** / +2.27 (17.2 → 15.0 / 17.0 / 18.5) | −4.82 / **−0.25** / +2.43 (18.1 → 15.5 / 18.0 / 19.6) |
| — FX (NOK path, 70/30) | +2.47 / 0 / −0.85 | +2.47 / 0 / −0.85 |
| — cost | −0.25 | −0.19 |
| c (timing) | 0.10 / 0.00 / −0.08 | 0.10 / −0.01 / −0.09 |
| ΣD / V_T (P = 100) | 7.5 / 85.5 · **8.5 / 106.3** · 8.8 / 123.9 | 6.8 / 84.2 · **7.6 / 107.8** · 7.9 / 126.7 |

- **Nordnet against DNB in Base (+0.15 pp):** +0.19 pp normalised EPS growth (no energy to
  normalise, more Microsoft) and +0.18 pp from the multiple; against that −0.28 pp of cash yield;
  plus 0.06 pp of lower cost.
- Structural run: exempt, as in the baseline (the blocks carry their own cyclical paths).

**Exit cross-check against the equity market** (iaf-valuation 2026-10-18.2, Step 3; World from
`docs/equity-market-bbb.md`) `[A]`:

| Bear / **Base** / Bull | DNB GI A (MSCI World) | Nordnet GI (Climate Change) | Equity BBB World |
|---|---|---|---|
| Exit value multiple (V_2029 ÷ 2030 EPS, incl. retained cash) | 15.0 / **17.0** / 18.5 | 15.5 / **18.0** / 19.6 | 15 / **17** / 18.5 |
| Exit P/B | ≈ 2.46 / **3.14** / 3.69 (= World) | ≈ 2.7 / **3.5** / 4.1 (World × 1.10, today's P/BV ratio 4.53 / 4.10) | 2.46 / **3.14** / 3.69 |
| Buyer's implied return at exit (cash yield at 0.49 cash conversion + long-run growth) | 7.1 / **8.2** / 8.7% | ≈ 7.0–7.2 / **8.0–8.2** / 8.6–8.8% (yield 3.2 / 2.7 / 2.5% at the higher multiple; growth at World's, or +0.2 pp as in the window) | 7.1 / **8.2** / 8.7% |

- DNB's exit is World's by construction. Nordnet's exit multiple is 6% above World's (the rest
  premium); a buyer then earns 0–0.2 pp less than on World, depending on whether its faster growth
  (+0.2 pp a year in the window) lasts past exit. The stated reason is its higher growth
  (more AI and Tesla), and the sensitivity is the premium halving or going (below). Neither exit is
  generous on a return basis.

**Attribution from the 18 Oct version** (after cost; Base / Bear 2027 / E / R; prices, NAVs and
stub unchanged at 15 Oct):

| Step | DNB on Nordnet | DNB pension platform | Nordnet GI |
|---|---|---|---|
| 18 Oct version | 4.66 / −21.5 / 0.011 | 4.71 / −21.5 / 0.013 | 4.81 / −23.4 / 0.016 |
| 1. + Microsoft v3 (Q1 FY27) | 4.66 / −21.5 / 0.011 | 4.71 / −21.5 / 0.013 | 4.81 / −23.4 / 0.016 |
| 2. + Alphabet v2 (Q3) | 4.60 / −21.7 / 0.009 | 4.64 / −21.6 / 0.010 | 4.75 / −23.5 / 0.013 |
| 3. + E-layer cash conversion −.20 / .00 / .20 (AI BBB Update 3) (= model) | **4.58 / −21.7 / 0.008** | **4.62 / −21.7 / 0.009** | **4.73 / −23.5 / 0.012** |
| Sensitivity: + E Base 2027 .92 (AI BBB Update 5) on the E block | 4.58 / −21.7 / 0.008 | 4.62 / −21.7 / 0.009 | 4.73 / −23.5 / 0.012 |
| Sensitivity: company interim V_t not re-glided (Base 2027 4.4%) | 4.58 / −21.7 / 0.008 | 4.62 / −21.7 / 0.009 | 4.73 / −23.5 / 0.013 |

- Price effect: none (prices kept at the 15 Oct NAV date). All of the change is input.
- Step 2 is most of it: Alphabet's V_T falls 4.9% on a ~4% weight. Microsoft's v3 moves its V_T by
  +$0.1 and its 2027 EPS by +1%: nothing at two decimals.
- The re-glide changes only the 2027 and 2028 year returns (Base 2027 +0.3 pp), not the window
  IRR, P_k or the Bear.

**Sensitivities** (window IRR, %; E / R with the HY definitions):

| Change | Bear | Base | Bull | Bear 2027 / Base 2027 | E / R | MoS (Base) |
|---|---|---|---|---|---|---|
| **DNB GI A on Nordnet, model** | −2.31 | **4.58** | 9.56 | −21.7 / 4.7 | 0.008 | −19.0% |
| DNB on the DNB pension platform (0.21%) | −2.27 | 4.62 | 9.61 | −21.7 / 4.7 | 0.009 | −18.9% |
| DNB: exit multiples −1 / +1 (blocks and rest) | −4.11 / −0.59 | 2.94 / 6.16 | 8.02 / 11.06 | −26.3 / −17.1 | −0.05 / 0.07 | −22.8 / −15.2% |
| DNB: CY27 consensus −5% | −3.92 | 2.85 | 7.76 | −25.6 / −0.6 | −0.06 | −23.0% |
| DNB: rest growth 4.5% / 6.5% | | 3.93 / 5.23 | | | −0.02 / 0.03 | −20.5 / −17.4% |
| DNB: NOK 10% weaker / stronger by 2029 | | 7.77 / 1.17 | | | 0.11 / −0.14 | −11.2 / −26.8% |
| DNB: AI-only Bear / Bull | 0.58 | | 7.60 | −8.8 / — | | |
| DNB and Nordnet: E block Base 2027 at the E-layer .92 (AI BBB Update 5) | unchanged | unchanged | unchanged | unchanged | unchanged | unchanged |
| **Nordnet GI, model** | −3.00 | **4.73** | 10.02 | −23.5 / 4.7 | 0.012 | −18.7% |
| **Rest premium halves by exit** | −3.29 | **4.17** | 9.47 | −24.3 / 2.9 | −0.008 | −20.0% |
| Rest premium gone | −3.58 | 3.61 | 8.91 | −25.0 / 1.1 | −0.029 | −21.4% |
| Microsoft and Alphabet on the E layer path | −2.74 | 4.42 | 9.30 | −23.0 / 4.1 | 0.002 | −19.4% |
| NVIDIA on the H1 layer path | −3.03 | 4.66 | 9.94 | −23.6 / 4.6 | 0.010 | −18.9% |
| Memory-stressed Bear (Micron's Bear exit at today's 4.8×, not 8×) | −3.09 | 4.73 | 10.02 | −23.8 | 0.012 | |
| Tail weights ×0.7 / ×1.3 | −2.94 / −3.06 | 4.75 / 4.70 | 10.01 / 10.04 | | 0.013 / 0.011 | |
| Nordnet: exit multiples −1 / +1 | −4.69 / −1.37 | 3.21 / 6.19 | 8.60 / 11.41 | −27.8 / −19.3 | −0.04 / 0.06 | −22.3 / −15.2% |
| Nordnet: CY27 consensus −5% | −4.59 | 3.00 | 8.22 | −27.4 / −0.5 | −0.05 | −22.8% |
| Nordnet: rest growth 4.5% / 6.5% | | 4.10 / 5.36 | | | −0.01 / 0.03 | −20.2 / −17.2% |
| Nordnet: NOK 10% weaker / stronger by 2029 | | 7.92 / 1.31 | | | 0.11 / −0.12 | −10.8 / −26.6% |
| Hidden swap drag +0.20% | −3.19 | 4.52 | 9.80 | −23.7 / 4.5 | 0.005 | −19.2% |
| Cost 0.25% | −3.06 | 4.66 | 9.96 | | 0.010 | −18.9% |
| Nordnet: AI-only Bear / Bull | 0.06 | | 8.20 | −11.3 / — | | |

- **The Base ranking flips inside the sensitivities.** Nordnet leads by 0.15 pp in the model; it
  trails by 0.16 pp with Microsoft and Alphabet on the layer path, by 0.41 pp if its rest premium
  halves, and by 0.97 pp if the premium goes. Under the skill's rule, **the model cannot rank the
  two on return.** Nordnet is behind in every Bear case.
- **The NOK is the largest single sensitivity** (+3.2 / −3.4 pp for a 10% weaker / stronger NOK
  by 2029), larger than the
  multiple. Only a 10% weaker NOK lifts E / R to ~0.11, still below 0.196.
- **No plausible input reaches k at today's price** for either fund.

## Results

| | DNB GI A (Nordnet): Bear / **Base** / Bull | Nordnet GI: Bear / **Base** / Bull |
|---|---|---|
| IRR_T (d + g + c, after cost) | −2.3 / **4.6** / 9.6% | −3.0 / **4.7** / 10.0% |
| P_k (hurdle NAV) / margin of safety | 571 / −34.2% · **703 / −19.0%** · 811 / −6.5% | 148.0 / −35.7% · **187.2 / −18.7%** · 218.0 / −5.4% |
| Rule 1: d + g > k? | No · **No** · No | No · **No** · No |
| Capital preserved? ΣD + V_T vs P | No, −7.0% · Yes, +14.8% · Yes, +32.7% | No, −9.0% · Yes, +15.4% · Yes, +34.5% |
| Share of Bull already priced | **153%** | **140%** |

- Both NAVs are above the Bull hurdle by 5–7%: the price is above what even the Bull case pays at
  12%. The Year-1 drawdown is −21.7% (DNB) and −23.5% (Nordnet).
- No survival question: open-ended UCITS funds with daily dealing and no leverage. Nordnet's
  swap exposure to J.P. Morgan is capped at 10% of NAV under UCITS `[E]`.

## Against high yield and each other

| Base window, NOK, before tax | Base return | E (pp over NIBOR) | R (Base 2027 − Bear 2027, pp) | **E / R** | Bear 2027 |
|---|---|---|---|---|---|
| Nordic HY market (after a typical 0.6% fee) | 6.2 | 1.82 | 9.28 | **0.196** (reference) | −2.8 |
| World index (Equity BBB, 16 Oct price, after 0.20%; 15 Oct company analyses) | 5.0 | 0.64 | 26.3 | 0.024 | −20.8 |
| *World on this document's 29 Oct inputs (16 Oct price, after 0.20%)* | *4.9* | *0.54* | *26.3* | *0.021* | *−21.0* |
| **DNB Global Indeks A, on Nordnet (0.25%)** | **4.58** | **0.20** | **26.3** | **0.008** | **−21.7** |
| **DNB Global Indeks A, DNB pension platform (0.21%)** | **4.62** | **0.25** | **26.3** | **0.009** | **−21.7** |
| **Nordnet Global Indeks (0.19%)** | **4.73** | **0.35** | **28.3** | **0.012** | **−23.5** |
| AI layers + companies in World, alone (before cost) | 4.6 | 0.3 | 46.3 | 0.005 | −42.2 |
| Rest of World, alone (before cost) | 5.5 | 1.2 | 18.0 | 0.06 | −12.2 |

- The fund rows sit 0.85% above the World row's price (15 vs 16 Oct); at the same price their Base
  would be ~0.3 pp higher.

**Triggers** (NAV change from 15 Oct at unchanged earnings and unchanged future values):

| Trigger | DNB GI A (on Nordnet) | DNB GI A (DNB pension platform) | Nordnet GI |
|---|---|---|---|
| Pre-alert: Base = HY market 6.2% (after a typical fee) | −4.6% → **NAV ≈ 828** (fwd P/E 17.2) | −4.5% → ≈ 829 | −4.2% → **NAV ≈ 221** (fwd P/E 18.2) |
| *Base = HY market 6.8% (before fees, the Equity BBB's pre-alert)* | *−6.3% → ≈ 814 (17.0)* | *−6.1% → ≈ 815* | *−5.9% → ≈ 217 (17.9)* |
| **E / R = HY market reference 0.196** | **−15.5% → NAV ≈ 733** (fwd P/E 15.3) | −15.4% → ≈ 734 | **−16.4% → NAV ≈ 192** (fwd P/E 15.9) |
| **Base IRR = k = 12% (P_k)** | **−19.0% → ≈ 703** (14.7) | −18.9% → ≈ 704 | **−18.7% → ≈ 187** (15.5) |

- Forward P/Es are MSCI's 30 Sep figures × the index move since then × the trigger's change `[A]`.
- **The E / R trigger moved from −15.2% to −15.5%** (18 Oct: NAV ≈ 736; 17 Oct ≈ 783): Alphabet v2
  and the E cash conversion lower Base by 0.08 pp.
- The Equity BBB's own World trigger (−14.1% from 16 Oct) is −14.8% from the 15 Oct price, a DNB
  NAV of ≈ 740 before the fund's cost, on the 15 Oct company analyses; with the cost and the
  29 Oct company blocks it is ≈ 733.
- **Indicative NAVs on 28 Oct** (URTH × USD/NOK; see Near term): DNB ≈ 853, Nordnet ≈ 226. The
  move is NOK, which shifts the NAV triggers with it, so the distances stay ~−15% to −19%.
- It drifts up about 0.2% a month with reinvested dividends, moves about one for one with
  consensus revisions, and moves with the AI paths and NIBOR.
- **Tax (general):** in a taxable account an equity fund (≥ 80% equities) is taxed like shares
  (37.84% on returns above the skjermingsrente). For Nordnet's synthetic fund, check its reported
  tax equity share `[?]`. Tax does not change the model.
- **Reading `[A]`:**
  - **Against HY:** both funds are dominated on the 3-year rule: lower Base than the HY market
    after fees, and ~2.8× its one-year stress. At the 15 Oct NAVs the AI part and the rest of World
    return 4.6% and 5.5% before cost; neither carries the index above HY.
  - **Between the two:**
    - **Cost:** 0.06 pp in Nordnet's favour on Nordnet (≈ NOK 600 a year per NOK 1m).
    - **Model return:** within ±0.2 pp, and it flips with the rest premium or Microsoft's path.
    - **E / R:** both near zero (0.008 vs 0.012).
    - **Bear:** 1.8 pp deeper for Nordnet in 2027; 2.5 pp deeper in an AI-only break.
    - **Concentration:** Nordnet holds 5 pp more AI, 2 pp more Microsoft and 2 pp more Tesla.
    - **Structure:** physical, Norwegian and stable (DNB), against synthetic, Irish and on its
      third index (Nordnet).
    - **Availability:** DNB's fund is sold on Nordnet and on DNB's pension platform; Nordnet's only
      on Nordnet.

## Verdict and caveat

- **Verdict (unchanged): both fail k** (margin of safety −19.0% DNB on Nordnet, −18.9% DNB
  pension platform, −18.7% Nordnet) and both NAVs sit above even the Bull hurdle. Neither preserves
  capital in Bear over the window (−6.8% to −9.0%); the Year-1 loss is −22% to −24%. Both are far
  below the HY market reference on E / R (0.008–0.012 against 0.196).
- **Between the funds:** **DNB Global Indeks A** for the shallower Bear, the smaller AI stress,
  the plain index and physical replication. Nordnet Global Indeks is a fair alternative on Nordnet:
  cheapest, and within 0.2 pp in Base.
- **Buy levels on the HY rule** (NAV of 15 Oct basis): DNB NAV ≈ 733, Nordnet ≈ 192 (E / R =
  0.196); k at ≈ 703 and ≈ 187.
- **What would change the choice between them:**
  - Microsoft's or the AI platform and compute paths turning up favours the index with more of
    them (Nordnet). The 28 Oct reports did not: Microsoft's path rose ~1% and Alphabet's (same
    weight in both) fell, so the gap stayed at 0.15 pp. NVIDIA's report (17 Nov) weighs the same in
    both.
  - A financing break, or a growth sell-off on rates, favours DNB.
  - Nordnet moving back to plain MSCI World; fee changes; swap costs in Nordnet's tracking.
- **Caveat:**
  - A margin-of-safety screen on the baselines' index model, not a price target or personal
    advice.
  - The AI paths are the AI BBB's; Microsoft's, Alphabet's and NVIDIA's are their analyses'; the
    rest path is the Equity BBB's.
  - The funds are priced at 15 Oct against a baseline priced at 16 Oct; this re-mark keeps that
    price date and changes inputs only. The company analyses are priced at 28 Oct; their interim
    values are re-glided to the 15 Oct closes `[A]`.
  - Nordnet's tail weights and rest premium are own assumptions.

## Risks and signposts

| Signpost | Threshold | Now | Source |
|---|---|---|---|
| DNB GI A NAV (triggers) | ≤ 828 pre-alert · **≤ 733 E / R trigger** · ≤ 703 k | 867.98 (15 Oct); ≈ 853 indicative (28 Oct) | DNB AM, Nordnet |
| Nordnet GI NAV (triggers) | ≤ 221 · ≤ 192 · ≤ 187 | 230.31 (15 Oct); ≈ 226 indicative (28 Oct) | Nordnet |
| Rest-of-World CY27 consensus revisions | −5% / +5% | Equity BBB base (rest P/E 17.0 on CY27) | Equity BBB |
| MSCI World forward P/E | < 15.5 / > 19.5 | ≈ 18.1 (15 Oct, scaled) | MSCI factsheets |
| Microsoft, Alphabet next reports (late Jan / early Feb 2027; 2027 capex guides); post-report CY27 consensus | company Bear / Bull signposts | Reported 28 Oct (in this re-mark). MSFT $531.01 (k at ≈ $494.5); GOOGL $324.89 (k at ≈ $261), post-market $292.50 | Company analyses |
| Amazon Q3 (29 Oct, after the US close) | AWS against the E2 row; capex; FCF | In the E block on the E-rest row; `docs/amzn-analysis.md` v2 to follow | AI BBB small update (30 Oct) |
| NVIDIA Q3 FY27 (17 Nov) | Q4 guide below Q3 / > +15% q/q | Q3 guide USD 108bn; FY28 ~+70% guided (= Bull); $217.23 | `docs/nvda-analysis.md` |
| Next-year capex guidance | flat/down / 2027 consensus > USD 1.3tn | No 2027 figures at the Q3 reports (Alphabet "increase significantly"); 2027 consensus ~USD 1.1tn | AI BBB |
| Vendor-financing flow; platform equity funding | new loans or guarantees > USD 50bn in a quarter, or one called; new share sales by a platform | Vendor financing ≥ USD 220bn; Alphabet sold $12.4bn of shares through its ATM in Q3 (Bear side crossed, AI BBB) | AI BBB |
| US rates: 10-year; US HY OAS | > 5.5% / > 4.5% (Bear) | 5.10%; 3.23% (15 Oct) | FRED |
| USD/NOK; I-44 | > 10.5 / < 9.2; > 117 / < 107 | 9.33 (28 Oct close); 109.52 (16 Oct) | Yahoo; Equity BBB |
| AI share of MSCI World (strict mapping) | > 30% | 26.0% (15 Oct) | URTH + prices |
| Climate Change / World forward P/E ratio | < 1.03 (Nordnet's premium fading) / > 1.08 | ~1.05 | MSCI factsheets |
| Nordnet index or fee change | any announcement | Climate Change since 3 Jun 2025; 0.19% | Nordnet / KID |

**Before the next update:** the NAVs after 15 Oct (re-mark prices at the next input change);
Amazon's Q3 and the AI BBB's small update (30 Oct); Norges Bank (5 Nov; the HY BBB is stale
after it); the Equity BBB's full update (stale after 10 Nov; it should take the 28 Oct company
analyses and decide whether Amazon becomes a World block); NVIDIA's Q3 FY27 (17 Nov); MSCI's
October month-end factsheets and the November index review.

**Stale after 17 Nov 2026** (NVIDIA's report), or earlier at the Equity BBB's full update or a
NIBOR path change in the HY BBB. Re-run when any of these baselines or company analyses is
updated, or if a NAV crosses a trigger.

## For other modules

- **`equity-market-bbb` (for its full update; no re-run on its own):** on the 28 Oct company
  analyses (Microsoft v3, Alphabet v2) and the AI BBB's E cash conversion of 22 Oct, its World
  build at its own 16 Oct prices gives Base **5.22% → 5.13%** before fees, Bear −1.72 → −1.80%,
  Bull 10.22 → 10.14%, E / R 0.024 → **0.021** (Alphabet −0.07 pp, cash conversion −0.02 pp,
  Microsoft 0.00). Two checkpoints: (1) the AI BBB's E 2027 point (.92) should not be applied on top
  of the company blocks (double count; see Look-through); (2) Amazon now has its own analysis, and
  its Bear (.74 / .62 / .70 / .81) and Bull (1.03 / 1.28 / 1.51 / 1.74) differ from the E-rest row
  by ≥ 0.05 from 2027–28: whether it becomes a World block is the baseline's decision.
- **`ai-market-bbb`:** no input to its paths. Its downstream note for this document ("E-layer
  Base 2027, ≈ −0.5% on World's 2027 EPS") assumes Microsoft and Alphabet on the layer; here they
  are company blocks, so the point is not applied (sensitivity: no change). The developed-market AI
  inside World returns 4.6% in Base (15 Oct prices) against ~5.5% for the all-six baskets at 28/29
  Oct prices (Micron vs SK hynix and Samsung; ASML, Applied and Lam vs TSMC).
- **Company analyses (NVIDIA, Microsoft, Alphabet, TSMC):** used as blocks or context; no input
  back.

## Change log

- **11 Oct 2026 — first analysis.**
- **12 Oct 2026 — AI market update:** AI layer split with an implied rest; rest-growth flag raised.
- **15 Oct 2026 — AI BBB Update 1, Microsoft and Alphabet analyses:** company blocks; NAVs of
  14 Oct; trigger convention aligned.
- **17 Oct 2026 — AI BBB Update 2 (method v2), NVIDIA and TSMC analyses:** NVIDIA as a company
  block (±0.01 pp on either fund); TSMC in neither index; retained cash in layer and energy blocks.
  DNB 6.03%, Nordnet 6.16% in Base. That version stated Brent's Base path as unchanged; the oil
  BBB of 17 Oct had raised Base 2027 to 88 (effect < 0.01 pp, corrected here).
- **18 Oct 2026 — Equity BBB Update 1 (World from blocks, amended 18 Oct twice); market only**
  (equity-market-bbb 2026-10-18.4):
  - **World rest explicit** (the Equity BBB's trend path) instead of implied from the 11 Oct path:
    Base −1.38 pp (DNB) and −1.35 pp (Nordnet).
  - **Brent Base 2027 88, energy payout 0.76:** ≤ +0.01 pp.
  - **Currency 70% USD/NOK, 30% I-44:** Base unchanged; Bear 2027 −0.8 to −0.9 pp.
  - **Portfolio content removed (user instruction):** no HY book (6.9%, E / R 0.291) in the tables
    or triggers; no position, planned amount or account check; `docs/portfolio-overview.md` is
    neither read nor updated. Pre-alert is now Base = the HY market's 6.2% after a typical fee;
    the "E / R = HY book" trigger is dropped. Amounts are shown per NOK 1m.
  - NAVs kept at 15 Oct (16 Oct not published on 18 Oct).
  - **Results:**

    | | 17 Oct | 18 Oct |
    |---|---|---|
    | DNB on Nordnet: Base / Bear / Bull | 6.03 / −0.32 / 10.97% | **4.66 / −2.23 / 9.64%** |
    | DNB: Bear 2027 / E / R / margin of safety | −18.0% / 0.068 / −15.5% | **−21.5% / 0.011 / −18.8%** |
    | DNB triggers (E / R / k) | 783 / 733 | **736 / 705** |
    | Nordnet: Base / Bear / Bull | 6.16 / −1.04 / 11.40% | **4.81 / −2.91 / 10.10%** |
    | Nordnet: Bear 2027 / E / R / margin of safety | −20.0% / 0.068 / −15.2% | **−23.4% / 0.016 / −18.5%** |
    | Nordnet triggers (E / R / k) | 206 / 195 | **193 / 188** |
    | Rest of World, Base (before cost) | 7.5% (implied) | **5.5% (explicit trend)** |

  - **Conclusion:** unchanged between the funds (DNB on risk and structure; no return ranking).
    Against HY both are now further away: E / R near zero, trigger ~−15%.
- **29 Oct 2026 — re-mark on inputs (update chain): Microsoft v3, Alphabet v2, AI BBB Updates 3–5**
  (iaf-valuation **2026-10-18.2**, was 2026-10-11.3; ai-market-bbb Update 5, rev 2026-10-29.1).
  - **Causes:** ai changed 29 Oct (read 17 Oct); msft changed 28 Oct (read 15 Oct); googl changed
    28 Oct (read 15 Oct). Unchanged since read: equity (18 Oct), nvda (17 Oct), oil (renewed 24 Oct,
    kept unchanged), hy (24 Oct, **kept unchanged**: NIBOR path 4.38% and HY reference 0.196 as
    read), hy-funds (18 Oct).
  - **Change gate:** the company blocks and the E cash conversion are values this document reads,
    and they move Base by −0.08 pp and E / R by −0.003 to −0.004: re-marked.
  - **Taken:** Microsoft v3 (V_T Base 692.0 → 692.1, Bear 406.9 → 404.5, Bull 919.7 → 921.4; EPS
    +0.9–1.2%); Alphabet v2 (V_T 390.1 → 371.1, Bear 215.1 → 202.6, Bull 537.5 → 515.9; Base EPS
    2027 13.45 → 12.66); interim V_t re-glided to the 15 Oct closes `[A]`; E cash conversion
    −.10 / .10 / .30 → −.20 / .00 / .20 (Update 3).
  - **Not taken, with reason:** the E-layer Base 2027 .97 → .92 (Update 5) for the E block: it is
    driven by Alphabet's and Microsoft's own EPS, already in their blocks (double count); the
    E-block names blend to .96 (Amazon .952, E-rest .97), below the 0.05 rule. Sensitivity: no
    change. The E-layer Bear and Bull of Update 3 (Microsoft, Alphabet, Amazon blend): the E block
    stays on the E-rest row (the path the AI BBB keeps for names outside its company check; here
    Amazon has no block yet, as in the Equity BBB's World build). Amazon as a block (its v2 follows
    tonight's report) is an open item for the Equity BBB's full update.
  - **Method (iaf-valuation 2026-10-18.2):** exit cross-check table added; the exit principle and
    the NOK path label were already practice. No number changed by the method.
  - **Prices:** kept at the 15 Oct NAV date (no price effect); memo of the 28 Oct move under Near
    term.
  - **Results:**

    | | 18 Oct | 29 Oct |
    |---|---|---|
    | DNB on Nordnet: Base / Bear / Bull | 4.66 / −2.23 / 9.64% | **4.58 / −2.31 / 9.56%** |
    | DNB: Bear 2027 / E / R / margin of safety | −21.5% / 0.011 / −18.8% | **−21.7% / 0.008 / −19.0%** |
    | DNB pension platform: Base / E / R | 4.71% / 0.013 | **4.62% / 0.009** |
    | DNB triggers (E / R / k) | 736 / 705 | **733 / 703** |
    | Nordnet: Base / Bear / Bull | 4.81 / −2.91 / 10.10% | **4.73 / −3.00 / 10.02%** |
    | Nordnet: Bear 2027 / E / R / margin of safety | −23.4% / 0.016 / −18.5% | **−23.5% / 0.012 / −18.7%** |
    | Nordnet triggers (E / R / k) | 193 / 188 | **192 / 187** |
    | AI layers + companies in World, Base (before cost) | 4.95% | **4.6%** |

  - **Conclusion:** verdicts unchanged (both fail k; DNB on risk and structure; no return
    ranking).

## Appendix: own assumptions

By weight on the result:

1. The rest of World follows the Equity BBB's explicit path (consensus −3%, then 5.5% a year);
   ±1 pp of rest growth moves Base by ±0.6–0.7 pp.
2. Microsoft (v3), Alphabet (v2) and NVIDIA (v1) take their analyses' per-share paths at the
   15 Oct closes; Microsoft's and Alphabet's interim values re-glided from their 28 Oct run prices
   with the analyses' own P/E glide; NVIDIA on the calendarised, revenue-consistent variant. Other
   AI names on the AI BBB layers; Amazon, Meta and Oracle on the E-rest row with the E-layer cash
   conversion; other AI-related names (~4.1%) stay in the rest.
3. The funds are run at the 15 Oct price on the baseline's 16 Oct paths (the 29 Oct re-mark keeps
   that price date).
4. Nordnet's weights and its index move since 9 Oct (−0.3% beyond World, from the NAVs).
5. Nordnet's rest keeps its 5.4% premium in Base and Bull and halves it in Bear; half of it is
   Tesla.
6. Tracking beyond cost is zero; a 0.20% swap drag is a sensitivity.
7. Equity BBB FX paths (70/30) applied relative to the 15 Oct spot.

## Appendix: sources

| # | Source | Content | Observed / published |
|---|---|---|---|
| S1 | [DNB Asset Management, DNB Global Indeks](https://dnbam.com/en/our-funds/funds/dnb-global-indeks) | NAV 867.98 (15 Oct; latest on 18 Oct), YTD 5.87 vs 5.64%, 1 y 9.03 vs 8.94%; fund NOK 165,022m, class A 70,104m; holdings, fee, exclusions, currencies, risk | 18 Oct 2026 |
| S2 | [DNB pension fund page, DNB Global Index A](https://www.dnb.no/pensjon/fond-liste/d/dnb-global-indeks-a-NO0010582984) (in-app browser) | Annual cost 0.20% = 0.10% + 0.10% platform; transaction costs 0.01% | 11 Oct 2026 |
| S3 | [Nordnet, DNB Global Index A](https://www.nordnet.no/fond/liste/dnb-global-indeks-a-nok-7b4b0894) | Total pris 0.25% | 8 Oct 2026 |
| S4 | [Nordnet, Nordnet Global Indeks](https://www.nordnet.no/fond/liste/nordnet-global-indeks-nok-799b8152) | NAV 230.31 (15 Oct; latest on 18 Oct), 1 y +8.19%; Total pris 0.19% | 18 Oct 2026 |
| S5 | Nordnet Global Index NOK Class KID (doc.morningstar.com) | Structure, synthetic swap, 0.00% costs, base currency EUR | KID 3 Jun 2025 |
| S6 | Nordnet Index Fund Global ESG KID | Launch 29 Jun 2020; index then MSCI World ESG Leaders | KID 30 Jun 2021 |
| S7 | [Nordnet Danmark blog](https://www.nordnet.dk/blog/nordnets-egne-indeksfonde-skifter-indeks/) | Index switch on 3 Jun 2025 | 23 May 2025 |
| S8 | [Nordnet FAQ, platform fee](https://www.nordnet.no/faq/priser/prismodell-for-fond/hva-er-plattformavgift) | Platform fees | Oct 2026 |
| S9 | [MSCI World Climate Change (CTB) Index factsheet](https://www.msci.com/documents/10199/255599/msci-world-climate-change-index-usd-net.pdf) | Fundamentals, sectors, top 10 vs parent, returns, risk | 30 Sep 2026 |
| S10 | [MSCI World Index factsheet](https://www.msci.com/documents/10199/255599/msci-world-index.pdf) | Sector weights, fundamentals | 30 Sep 2026 |
| S11 | [iShares MSCI World ETF (URTH) holdings CSV](https://www.ishares.com/us/products/239696/ishares-msci-world-etf/latest-holdings.csv) | All holdings and weights | 9 Oct 2026 |
| S12 | `docs/equity-market-bbb.md` (Update 1, amended 18 Oct) and `references/upd.py` | World blocks, explicit rest path, energy rule, currency mix, scenarios, World triggers | 18 Oct 2026 |
| S13 | `docs/ai-market-bbb.md` (Update 5; Updates 3–4 read for their changes) | Layer paths v2.1, E-rest row, E cash conversion, E-layer company check, calendarised consensus | 29 Oct 2026 |
| S14 | `docs/nvda-analysis.md`, `docs/tsm-analysis.md` (v1); `docs/msft-analysis.md` (v3), `docs/googl-analysis.md` (v2, call addendum 29 Oct); `docs/dnb-teknologi-analysis.md` (NVIDIA variant rebuild) | Per-share V_t, D_t, EPS per scenario; TSMC not in MSCI World | 17–29 Oct 2026 |
| S15 | Yahoo chart API (`close.py`), 15 Oct closes: URTH 208.11, USD/NOK 9.4931, EUR/USD 1.1195, IXC 61.38, TSLA 362.44 and every block name; 16 Oct: URTH 206.34; fund NAVs on Yahoo end 15 Oct | Prices at the NAV date | 17–18 Oct 2026 |
| S16 | FRED `DGS10`, `BAMLH0A0HYM2` | US 10-year 5.10%, US HY OAS 3.23% (15 Oct) | 17 Oct 2026 |
| S17 | [Rika Tillsammans forum](https://rikatillsammans.se/forum/t/nordnet-global-index-0-32-dold-avgift/94763) | EUR-class tracking under the old index | 8 Jan 2025 `[E]` |
| S18 | `docs/oil-market-bbb.md` (renewed 24 Oct, kept unchanged), `docs/hy-market-bbb.md` (24 Oct, kept unchanged), `docs/hy-funds-analysis.md` | Brent path, NIBOR, HY market Base and reference E / R | 18–24 Oct 2026 |
| S19 | Yahoo chart API: URTH 208.07 (28 Oct close), USD/NOK 9.334 (28 Oct), 9.27 (29 Oct morning) | Price memo only (not re-marked) | 29 Oct 2026 |

**Computed from Yahoo NAVs** (monthly log returns, Mar 2022–Sep 2026) `[F]` derived: volatility
DNB 12.2%, Nordnet 12.9%; correlation with World NOK 0.969 / 0.956, with OSEBX −0.01 / −0.06,
with Brent −0.31 / −0.33; max daily drawdown since Mar 2022 −18.2% / −19.2% (8 Apr 2025).

- **Validation notes:**
  - On the 18 Oct inputs, at the baseline's 16 Oct prices and zero cost, the World run reproduces
    the Equity BBB exactly
    (−1.72 / 5.22 / 10.22%; 2027 −20.6 / 5.6 / 13.4%; E / R 0.024 after 0.20%).
  - The company blocks reproduce their analyses at the analysis prices in USD (NVIDIA 11.4% /
    −12.8%; Microsoft 8.8%; Alphabet 3.8%; 17 Oct check). 29 Oct: V_T and D_t are the v3 / v2
    tables; at the 15 Oct closes the blocks give Microsoft 8.9% and Alphabet 2.4% in NOK Base
    (their analyses 9.5% at $531.01 and 4.6% at $324.89), consistent with the price gaps.
  - `idxai5.py` with all switches off reproduces the 18 Oct figures exactly (4.66 / 4.71 / 4.81%).
  - URTH duplicate tickers are matched on country.
- **Scripts:** `.claude/skills/equity-market-bbb/references/fund/`:
  - `idxai4.py`: the Equity BBB World build (blocks + explicit rest, energy rule, 70/30 currency)
    for MSCI World and the Climate Change index at the NAV-date price; `--d16` reproduces the
    baseline at 16 Oct.
  - `idxai4detail.py`: blocks alone, fund results, AI-only stress, attribution from 17 Oct,
    sensitivities (multiples, consensus, rest growth, NOK, premium, company paths, cost), triggers
    on the HY market references.
  - `idxai5.py` (29 Oct): `idxai4.py` with Microsoft v3, Alphabet v2 (interim V_t re-glided) and
    the E cash conversion; `setup()` switches give the attribution and the .92 and no-re-glide
    sensitivities; `--d16` gives World at the Equity BBB's 16 Oct prices. `idxai5detail.py`: the
    `idxai4detail.py` tables on these inputs, attribution from 18 Oct and the exit multiples.
  - The 11–18 Oct scripts are kept (`idxai3.py` is imported by `idxai4.py` and by the Equity BBB's
    `upd.py`; neither was changed).
