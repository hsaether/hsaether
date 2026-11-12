# DNB Teknologi A — IAF fund analysis on the Equity and AI Market BBBs — 6 November 2026

**Skill revisions used:**
- `iaf-valuation` **2026-11-01.1** (31 Oct run: 2026-10-29.1): k = 12%, hurdle and
  margin-of-safety rules, retained cash counted once, Track A on a dated IRR to an independent exit
  P/E, exit cross-check, prices as NAVs in NOK. **New since 2026-10-29.1:** opportunistic cyclical
  equity positions lead with the cycle (user rule, 1 Nov). Applied here to the memory part only:
  memory is judged on the AI BBB's memory cycle section, and its returns are shown in whole
  points. The fund as a whole stays on the HY switch rule (E / R against the HY reference), as the
  user asked.
- `ai-market-bbb` skill **2026-11-06.1**; document **Update 6 of 1 Nov with the 5 Nov check**
  (31 Oct run: Update 5 of 29 Oct): layer EPS paths, the "E rest" row, cash conversion, exit P/Es,
  payouts, basket references, the memory cycle section, catalysts and signposts.
- `equity-market-bbb` skill **2026-10-24.1**; document **Update 2 of 6 Nov** (31 Oct run: 17 Oct,
  amended 18 Oct): market inputs only (World scenarios, NOK path, World return, exit P/E and
  mid-cycle return). No skill carries an equity fund mode; the look-through method of earlier
  versions is kept under `iaf-valuation` (see For other modules).
- `hy-market-bbb` skill **2026-10-24.1**; document of **5 Nov**: NIBOR path and the HY market
  reference.

**Inputs:**
- `docs/equity-market-bbb.md` (**Update 2, 6 Nov 2026**; read 17/18 Oct before):
  - World Base **5.2% → 6.6%** before fees (2027 +7.7%), Bear 2027 −18.3% in NOK, E / R **0.080**;
    the move is mostly price (URTH −3.3% in USD since 16 Oct).
  - **NOK Base spot flat at I-44 107.8 and USD/NOK 9.29**; Bear USD/NOK +12% / +9% / +9% and I-44
    +8% / +6% / +6%; Bull −3% and −2%. **The relative moves the fund model uses are unchanged.**
  - World exit P/E 17.0 (15.0 / 18.5), mid-cycle return 8.2%, long-run growth 5.3%: unchanged.
- `docs/hy-market-bbb.md` (**5 Nov**; read 24 Oct before): **NIBOR path unchanged** (4.80 / 4.79 /
  4.39 / 3.86); HY market Base window **6.8% → 7.2%** before fees; **HY market reference E / R
  0.196 → 0.254** (E 2.15 pp after a 0.6% fee, R 8.47 pp; 0.216 with Bear read as a shock). The
  reference is now taken from this document.
- `docs/hy-funds-analysis.md` (31 Oct partial re-run; **on hold until the October fund reports,
  mid-November**): Sissener Corporate Bond R **as it stands**: Base 6.4%, E / R **0.347** (0.368 on
  24 Oct), Bear 2027 +0.4%. These are on the old 0.196 market basis; the fund re-run may move them.
- `docs/ai-market-bbb.md` (Update 6 of 1 Nov, **5 Nov check**): the chip sell-off is a price event;
  **every path the fund reads is kept** (E rest, H1, H3, T, exit P/Es, payouts, cash conversion).
  New: the memory cycle section (read for memory) and the baskets at the 5 Nov prices.
- **Company blocks:**
  - `docs/nvda-analysis.md` **v1.2 (5 Nov, $181.60)**; read v1 of 17 Oct before. The block values
    are v1.1's (2 Nov), on the AI BBB basis this fund already used; the interim V_t now glide from
    the 5 Nov price.
  - `docs/tsm-analysis.md` **v1.1 (5 Nov, $352.03)**; read v1 of 17 Oct before. CY27 basis $23.43;
    the H3 Bear the fund already used.
  - `docs/googl-analysis.md` v2 with its **1 Nov price re-mark** ($279.84): same block, the interim
    Base and Bull V_t re-glided; the fund now takes that pair (was the $324.89 pair).
  - Read as they stand: `docs/msft-analysis.md` v3 (28 Oct), `docs/amzn-analysis.md` v2 (30 Oct),
    `docs/skhynix-analysis.md` v2 (28 Oct), `docs/samsung-analysis.md` v2 (29 Oct); each kept
    unchanged on 4 Nov by its change gate.
- `docs/mu-analysis.md` **v3 (5 Nov, $656.39)**: the fund holds no Micron; memory evidence only.
- `docs/global-index-funds-analysis.md` (29 Oct) is **not read for values this run**: it predates
  Equity Update 2. The World row below is the Equity BBB's own index row.
- `docs/portfolio-overview.md` is not read: the position (21.874 units) and the HY book figures
  (0.291, 6.9%) are kept as cited in earlier versions.

**This version** (seventh; 11, 12, 15, 17, 22 and 31 Oct before) has five changes:
1. **NAV 4 Nov (7,381.56), the latest published at this run**, with every holding at its 4 Nov
   close. **The 5 Nov NAV, which carries the 5 Nov tech sell-off, was not yet published** (DNB AM
   and Nordnet both show 4 Nov on the morning of 6 Nov). It is estimated at **≈ 7,145 (−3.2%)**
   from the 5 Nov closes and shown beside the decision in every table.
2. **Holdings of 30 Sep** (DNB AM top 10, Nordnet's full list): Samsung leaves the top 10, **ASML
   enters** (1.27%, on the AI BBB H3 layer), Nintendo leaves the list; Korea 5.12% → 4.91%.
3. **NVIDIA v1.2, TSMC v1.1 and Alphabet's re-mark pair** replace their blocks.
4. **HY market reference 0.196 → 0.254** (HY BBB 5 Nov): the E / R trigger falls well below P_k.
5. **Memory on the cycle** (iaf-valuation 2026-11-01.1): the memory view is read from the AI BBB
   memory cycle section, with no precise IRR for memory.

**Verdict unchanged: fails k.** At the 4 Nov NAV: Base **8.6%** (31 Oct: 8.6%), P_k NAV **6,721**,
margin of safety **−8.9%** (−9.0%), Bear 2027 **−29.3%** (−28.7%), E / R **0.113** (0.110) against
the new reference **0.254**. At the estimated 5 Nov NAV: Base 10.0%, margin −5.4%, E / R 0.147.

## Summary

**Verdict**

- **Fails the IAF hurdle.** Base return to end-2029 is **8.6% a year in NOK after the 1.14% all-in
  cost** (31 Oct: 8.6%). **NAV NOK 7,381.56 (4 Nov) against a Base hurdle NAV P_k of NOK 6,721:
  margin of safety −8.9%.** Bear P_k NOK 4,425; Bull P_k NOK 8,348 (the Bull clears k: 16.6%,
  margin +13.1%).
- **The 5 Nov sell-off, not yet in a published NAV:** the model holdings at their 5 Nov closes put
  the 5 Nov NAV at **≈ NOK 7,145 (−3.2%)** `[A]` (NVIDIA −9.3%, Broadcom −10.4%, TSMC −10.8%, SK
  hynix −9.5%, Samsung −7.6%, ASML −6.5%, Microsoft −3.6%). There: **Base 10.0%, P_k NOK 6,762,
  margin −5.4%**, Bear 2027 −26.8%, E / R 0.147. **Still a fail; k needs a NAV near 6,720–6,760.**
- **What moved since 31 Oct (Base −0.02 pp; E / R +0.003; the reference +0.058):**
  - **Company blocks +0.01 pp:** NVIDIA v1.2, TSMC v1.1 and Alphabet's re-mark pair change values
    the fund already used, or only the interim glide.
  - **Inputs 0.00 pp:** no AI path, NOK relative move or NIBOR point the fund reads moved. World
    (5.2% → 6.6%) and the HY reference (0.196 → 0.254) move only the comparison and the triggers.
  - **Holdings −0.12 pp:** the 30 Sep weights (Meta down, ASML in at P/E 24, Samsung down).
  - **Price +0.09 pp:** the NAV rose 0.1% (7,375.01 → 7,381.56) while NVIDIA (−6.3%), TSMC (−8.4%)
    and Korean memory (−6 to −9%) fell and Amazon (+9.1%), Visa, Mastercard and Microsoft (+5–6%)
    rose. The 5 Nov estimate would add +1.4 pp.
- **The HY reference moved away from the fund.** HY now pays **0.254** per unit of stress (was
  0.196). The fund's E / R is 0.113 (0.147 at 5 Nov): **the E / R trigger is NOK 6,399, below P_k
  (6,721)**. On 31 Oct the two coincided (6,723 and 6,715). At k the fund's E / R is only 0.205.
- **Two-thirds of the fund is an AI bet:** 68% of the model weight and **75% of 2027 consensus
  earnings** sit in AI blocks; eight company blocks (seven analyses) cover 44% of the model.
- **Memory, judged on the cycle** (AI BBB memory cycle section, 1 Nov, re-marked 5 Nov; no own
  view):
  - **Where:** late upcycle. Contract prices still rise into Q1-27 (+3–8%) but q/q growth has
    halved twice since Q2-26; mobile DRAM and NAND outside enterprise SSD are flat; margins are
    records.
  - **What turns it:** new supply from 2H-27 into 2028 meeting AI capex digestion after the
    contracted 2027 build; US state siting policy (5 Nov) leans to the earlier or deeper side for
    2028 demand, with no figure yet.
  - **How likely and when:** Base kept (turn in 2028); timing risk 1–2 quarters earlier for NAND
    and commodity DRAM; 2029–30 risk deeper.
  - **What the price implies:** at the 5 Nov prices SK hynix earns k at **~0.66×** and Samsung at
    **~0.75×** the Base 2028–30 path (memory basket 0.80×). The Korean prices already discount a
    turn about a third below Base.
  - **In the fund:** memory is 6% of the model and **32% of 2027 consensus earnings** at P/E 2.6.
    Its Base return is in the mid-20s a year before cost; it rises in the decision Bear (8× trough
    exit) and falls ~40% capped at today's multiple. **A memory 2030 level at 0.6× Base takes the
    fund's Base from 8.6% to 7.8%**: the cycle moves the fund by about a point, and the fund fails
    k with or without it.
- **Bear breaks capital:** −29.3% in 2027 (≈ −NOK 47k on the position; −32.9% ≈ −NOK 53k
  memory-stressed); −5.5% a year; capital −15.6% at exit.
- **On the decision rule:** E / R **0.113** (stressed 0.104; 0.147 at 5 Nov) against the HY
  reference **0.254**, the HY book 0.291 and World's 0.080. The Base beats HY (6.6% after the
  typical fee) and World (6.6% before fees); per unit of stress it is less than half of HY.
- **The manager's AI selection still shows:** at the 5 Nov prices the fund's AI holdings return
  **12.1% before cost** against **10.1%** for the six AI baskets (AI BBB 5 Nov, same method).

**Decision table** (traded price: the fund's NAV in NOK; NOK after the 1.14% all-in cost on Nordnet
incl. its 0.29% platform fee; holdings at their 4 Nov closes, USD/NOK 9.270)

| | Bear | Base | Bull |
|---|---|---|---|
| **Price P: NAV (4 Nov 2026, DNB AM and Nordnet)** | NOK 7,381.56 | **NOK 7,381.56** | NOK 7,381.56 |
| **P_k: hurdle NAV (k = 12%) / margin of safety** | **NOK 4,425 / −40.1%** | **NOK 6,721 / −8.9%** | **NOK 8,348 / +13.1%** |
| IRR_T to 31 Dec 2029 (NOK path, Equity BBB) | **−5.5%** (memory-stressed −6.5%) | **8.6%** | **16.6%** |
| IRR_T / P_k at spot FX held flat (IAF FX rule) | −7.8% / NOK 4,103 | 8.6% / NOK 6,721 | 17.7% / NOK 8,581 |
| 2027 return (Year 1) | −29.3% (stressed −32.9%) | +8.0% | +20.9% |
| NAV equivalent at exit (look-through cash reinvested) | NOK 6,273 | NOK 9,555 | NOK 11,921 |
| Capital preserved? ΣD + V_T vs P | **No, −15.6%** | Yes, +28.7% | Yes, +60.1% |
| Position (21.874 units = NOK 161,464 at the 4 Nov NAV) at end-2029 | ≈ 137.2k | ≈ 209.0k | ≈ 260.8k |
| Year-1 stress on the position | ≈ −NOK 47k in 2027 (stressed −NOK 53k) | | |
| E / R (HY rule; reference **0.254**, HY book 0.291) | | **0.113** (stressed 0.104) | |
| **At the estimated 5 Nov NAV ≈ NOK 7,145 `[A]`: IRR_T / P_k (margin)** | −4.4% / NOK 4,437 (−37.9%) | **10.0% / NOK 6,762 (−5.4%)** | 18.2% / NOK 8,418 (+17.8%) |
| At the 5 Nov estimate: Bear 2027 / E / R | −26.8% (stressed −30.8%) | E / R **0.147** (stressed 0.133) | |

- **FX:** the Base decision is the same on the NOK path and at spot FX. Bear, Bull and E / R stay
  on the Equity BBB NOK path, as in earlier versions, so they compare with the HY and World rows.
  At spot FX the Bear is deeper (2027 −36.0%; E / R 0.096): on the NOK path the krone weakens in
  the Bear, which cushions a NOK holder.
- **NAV triggers** (at unchanged earnings, composition and upstream paths; from the 4 Nov NAV):
  - Base = k at **NOK 6,721**; **E / R = HY reference 0.254 at NOK 6,399** (6,205 on the
    memory-stressed Bear; 6,645 at 0.216, the reference with the HY Bear read as a shock);
  - E / R = HY book 0.291 at NOK 6,171; Base = HY book 6.9% at NOK 7,746 (the NAV is below it).
  - From the 5 Nov estimate: k at 6,762; 0.254 at 6,401.

**Per-year path** (look-through, index P = 100 at the 4 Nov NAV; NOK after cost)

| | Stub 5 Nov–31 Dec 2026 | 2027 | 2028 | 2029 | Exit-year 2030 (normalised) |
|---|---|---|---|---|---|
| Base EPS (2027 consensus = 1.00) | — | 0.904 | 0.880 | 0.878 | 0.906 |
| Base value ÷ next-year EPS at year-end (incl. retained cash) | 13.5 now | 16.4 | 17.8 | 18.7 | — |
| Base return | +0.1% | +8.0% | +9.8% | +9.0% | |
| Base NAV equivalent, year-end (NOK) | 7,391 | 7,984 | 8,763 | 9,555 | |
| Base IRR to year-end | — | 7.0% | 8.3% | 8.5% | |
| Bear EPS / return | — / +0.1% | 0.716 / −29.3% | 0.596 / +8.1% | 0.629 / +11.2% | 0.672 |
| Bear NAV equivalent (NOK) | 7,391 | 5,222 | 5,644 | 6,273 | |
| Bull EPS / return | — / +0.1% | 0.968 / +20.9% | 1.004 / +16.5% | 1.015 / +14.6% | 1.056 |
| Bull NAV equivalent (NOK) | 7,391 | 8,934 | 10,405 | 11,921 | |

- Base EPS falls 2027–29 because memory (29% of Base 2027 earnings) falls to mid-cycle. The value
  multiple rises for two reasons: memory's multiple re-rates as its earnings fall (with its net
  cash), and the layer, X and company blocks build cash and stakes.
- Base 2027 (+8.0%) is lower than on 31 Oct (+10.0%) and 2028–29 higher: NVIDIA's, TSMC's and
  Alphabet's interim values now glide from their lower 5 Nov / 30 Oct prices, which spreads their
  re-rating over three years instead of front-loading it into 2027.

## Tags

`[F]` fact from a fund document or market print · `[E]` external or secondary · `[A]` own
assumption · `[?]` not found or unverified.

## Header

| Item | Value |
|---|---|
| Fund | **DNB Teknologi A**, ISIN NO0010337678; Norwegian UCITS equity fund, accumulating; launched 6 Aug 2001 `[F]` |
| Manager | DNB Asset Management; Anders Tandberg-Johansen since launch `[F]` |
| Benchmark | MSCI World Communication Services & Information Technology (in NOK) `[F]` |
| NAV (price P) | **NOK 7,381.56, 4 Nov 2026** (DNB AM and Nordnet agree; Nordnet `last_nav_date` 4 Nov on the morning of 6 Nov; +1.73% on 4 Nov) `[F]`. Valuation date **5 Nov 2026**; holdings priced at their **4 Nov closes** (the NAV date). The 5 Nov NAV was not yet published; the 5 Nov closes give **≈ 7,145** `[A]` |
| Window | Stub 5 Nov–31 Dec 2026 (56 days) + 2027–2029; exit 31 Dec 2029, **T = 3.15 years** |
| Holdings | 64 companies (DNB AM). Model = 26 lines, **79.1% of NAV**: top 10 from DNB AM and the rest from Nordnet's full list, **both of 30 Sep 2026**. Korea 4.91% = SK hynix 1.99% + Samsung common 1.73% (Nordnet) + preference **1.19%** (the rest of Korea) `[A]` |
| Cost | **All-in 1.14% a year on Nordnet** (0.85% fee + 0.29% platform fee; Nordnet "Total pris" 1.14%) `[F]` |
| Currency (30 Sep 2026) | USD 66.69%, EUR 12.05%, SEK 6.39%, KRW 4.91%, JPY 3.46%, TWD 2.35%, NOK 2.11%, CHF 1.79%, HKD 0.24% `[F]`. Unhedged `[E/A]` |
| Position | 21.874 units, **≈ NOK 161,464 at the 4 Nov NAV**; cost NOK 150,000 `[F]` (as cited) |
| Look-through valuation | **P/E 13.5** on 2027 consensus (12.8 at 5 Nov); **18.6 without memory** (17.9); cash yield incl. buybacks ~2.4% `[A]` |
| Track | Track A as an index portfolio (look-through). AI layer blocks on the AI BBB method v2.1; **company blocks for Microsoft, Alphabet, NVIDIA, Amazon, TSMC, SK hynix and Samsung (common, preference)** |
| k | **12%**, standard |
| FX | USD/NOK 9.2700 (Yahoo, 4 Nov close; 5 Nov 9.2944, Norges Bank fixing 9.2984 on 5 Nov); I-44 107.76 (Norges Bank, 5 Nov, via the Equity BBB) `[F]` |

## Scenario definitions

The Equity BBB World scenarios carry the macro. The AI BBB supplies the mechanism for the AI
blocks, and the company analyses their names. 25/50/25 is a convention only.

| Scenario | Equity BBB anchor | AI BBB catalyst and mechanism | Company blocks | Non-AI block (X) | Signposts |
|---|---|---|---|---|---|
| **Base** | World Base (AI boom slows to trend); NOK spot flat (I-44 107.8) | **Contracted 2027 build, then digestion:** capex +42% in 2027, then +12% and +4%; memory turns in 2028 and normalises; software 7–8% | Own Base at the analysis price: NVIDIA 17.9% ($181.60), TSMC 13.7% ($352.03), Alphabet 9.6% ($279.84), Microsoft 9.5% ($531.01), Amazon 9.2% ($240.35); SK hynix and Samsung in the low-to-mid 20s (analysis prices) | Consensus −3%, then ~8% a year | NVIDIA Q3 (17 Nov) · memory business reports (14–16 Nov) · Anthropic IPO (~20 Nov) · 2027 capex guides (Jan–Feb) · memory contract prices |
| **Bear** | World Bear: recession H1 2027 + oil Bear; USD/NOK +12%, I-44 +8% | **Financing break + monetisation disappointment**, now with **US state siting policy** as a second route to the 2028 capex cut (AI BBB 5 Nov). 2028 capex −16%. Revenue-consistent Bears; Meta on the E rest row. Memory overshoots in 2028 | 2027 in NOK, before cost: Amazon −56%, NVIDIA −38%, Alphabet −39%, TSMC −38%, Microsoft −32%; memory up ~20% on the analyses' 8× trough exit, about −38% capped at today's multiple | −15% in 2027 | Vendor financing, platform equity funding (crossed: Alphabet's ATM), a hyperscaler guiding capex down, DRAM contract prices falling, the Texas data-center audit (10 Dec), CoreWeave (new 2026 low on 5 Nov) |
| **Bull** | World Bull: soft landing | **Agentic adoption:** lab revenue +130% in 2027; capex to USD 1.3–1.7tn | NVIDIA at consensus, then +15% / +9%; Amazon on its Bull | Consensus met, then ~8–9% | 2027 capex consensus > USD 1.3tn · lab run-rate > USD 250bn by mid-2027 |

- **The Bear is mostly the AI Bear:** AI blocks on Bear with X and the NOK on Base give **−25.0%
  in 2027** and −3.2% a year. AI Bull alone: +22.0% in 2027, 16.4% a year.
- **Side case (oil Bull / stagflation):** ≈ −13% in 2027, while Oslo rises.
- **Memory in the Bear:** see the memory-stressed Bear (Summary, Sensitivities).

## Fund and status

- **What the model holds** (DNB AM top 10 and Nordnet's list, both of 30 Sep) `[F]`:

| # | Holding | Weight | Block | # | Holding | Weight | Block |
|---|---|---|---|---|---|---|---|
| 1 | Microsoft | 9.62% | CM | 14 | Sony | 2.30% | X |
| 2 | Alphabet | 7.07% | CG | 15 | T-Mobile US | 2.19% | X |
| 3 | NVIDIA | 6.10% | CN | 16 | SK hynix | 1.99% | **CH** |
| 4 | Amazon | 5.05% | CA | 17 | Dassault Systèmes | 1.95% | T |
| 5 | Meta Platforms | 4.60% | E | 18 | Logitech | 1.79% | X |
| 6 | Broadcom | 4.18% | H1 | 19 | Samsung Electronics, common | 1.73% | **CS** |
| 7 | Mastercard | 3.73% | X | 20 | Nordic Semiconductor | 1.43% | X |
| 8 | Visa | 3.62% | X | 21 | Intuit | 1.40% | T |
| 9 | Ericsson B | 3.42% | X | 22 | HP Inc. | 1.34% | X |
| 10 | Adyen | 3.07% | X | 23 | Skyworks | 1.27% | X |
| 11 | SAP | 2.82% | T | 24 | **ASML (new)** | 1.27% | **H3** |
| 12 | Atlassian | 2.38% | T | 25 | Booking | 1.25% | X |
| 13 | TSMC (ADR) | 2.37% | CT | 26 | Samsung Electronics, preference (Korea − SK hynix − common) | ~1.19% `[A]` | **CP** |
| | | | | | **Model total** | **79.1%** | |

- **Changes from 24 Sep (top 10) and 31 Aug (the rest) to 30 Sep:**
  - Microsoft 9.39% → 9.62%, NVIDIA 5.92% → 6.10%, Broadcom 3.98% → 4.18%; Meta 4.95% → 4.60%,
    Visa, Mastercard and Ericsson slightly down; Adyen back in the top 10 (3.07%).
  - Samsung out of the top 10 (common 1.73%); Korea 5.12% → 4.91%; TSMC 1.97% → 2.37%.
  - **ASML in (1.27%)**, Nintendo out (below 1.25%); Atlassian 2.93% → 2.38%, Dassault 2.22% →
    1.95%, HP 1.63% → 1.34%, T-Mobile 1.99% → 2.19%.
  - Nordnet's weights run ~0.7% higher than DNB AM's on the same day (Microsoft 9.69% vs 9.62%);
    DNB AM's are used for the top 10 `[A]`. All are from before October's moves.
- **Style:** a quality-tilted, lower-beta tech fund. It holds the large and cheap AI names (NVIDIA
  at 13.2×, Korean memory at 2.6×) and payments. It has no AMD, Marvell, Micron, Oracle, Palantir,
  Snowflake, Arista or Vertiv among its 26 largest lines.
- **Record** (DNB AM, cumulative to the 4 Nov NAV; the page gives no date for the return block)
  `[F]`:
  - YTD +13.6% (benchmark +3.2%), 1 year +12.4% (+1.0%);
  - 3 years +106.7% (benchmark +75.8%), 5 years +169.8% (+109.4%), 10 years +685.3% (+557.6%);
  - November to date +2.8% against the benchmark's +0.4%.
- **NAV path:** 7,375.01 (29 Oct) → ≈ 7,179 (30 Oct, implied by the November-to-date return; the
  31 Oct estimate was 7,208, 0.4% high) `[A]` → ≈ 7,256 (3 Nov) → **7,381.56 (4 Nov)** → ≈ 7,145
  (5 Nov, estimated) `[A]`.

## Near term

- **Stub (5 Nov–31 Dec, 56 days):** price flat. The stub return is +0.1%, the same in all
  scenarios: cash accrual plus the Microsoft (0.98), Alphabet (0.22), NVIDIA (0.56) and SK hynix
  (KRW 34,181: the Q3 dividend, record date 30 Nov, and the 10tn buyback) payments, less cost.
- **No company report since 31 Oct.** NVIDIA v1.2, TSMC v1.1 and Micron v3 are price re-marks on
  the 5 Nov sell-off; the AI BBB reads it as a de-rating of the capex receivers after the US
  midterms (3 Nov), not a change to Base fundamentals. No hyperscaler, NVIDIA or utility changed
  guidance.
- **After the NAV date (5 Nov closes, not in the decision)** `[F]`:
  - down: TSMC −10.8%, Broadcom −10.4%, SK hynix −9.5%, NVIDIA −9.3%, Samsung −7.6% (preference
    −6.6%), ASML −6.5%, Nordic Semiconductor −5.5%, Ericsson −4.2%, Meta −4.0%, Microsoft −3.6%,
    Atlassian −3.5%, Visa −3.2%, Mastercard −2.5%, Alphabet and Amazon −2.2%;
  - up: Sony +7.1%, Adyen +4.5%, Dassault +1.4%, T-Mobile +0.9%, SAP +0.7%;
  - USD/NOK +0.3% (9.270 → 9.294).
  - **The 5 Nov NAV is likely ≈ 7,145 (−3.2%)** `[A]` (model holdings at their 5 Nov closes in
    NOK; the ~21% outside the model moving alike). At that NAV: Base 10.0%, Bear −4.4%, Bull
    18.2%, Bear 2027 −26.8%, E / R 0.147; P_k 6,762 / 4,437 / 8,418.
  - **Seoul fell again on 6 Nov** (intraday at this run: SK hynix 1,128,000, −10.8%; Samsung
    188,700, −6.4%; preference 150,700, −6.0%) `[F]`. On 4.91% of NAV that is roughly −0.4% more
    for the 6 Nov NAV, before the US session `[A]`.
- **Dates:**
  - the 5 Nov NAV (expected ~7 Nov);
  - Samsung and SK hynix Q3 business reports (~14 and ~16 Nov: LTA terms, floors, deposits);
  - **NVIDIA Q3 FY27 (17 Nov)** and the re-run of its analysis;
  - the Anthropic IPO (~20 Nov);
  - the HY funds re-run after the October reports (mid-November);
  - the October monthly report (holdings of 31 Oct);
  - DRAM and NAND contract prints (~30 Nov); the Texas data-center audit (10 Dec); Micron FQ1
    (16 Dec); Norges Bank MPR 4/26 (17 Dec);
  - the new governors (11–19 Jan) and the hyperscalers' 2027 capex figures (late Jan–early Feb).

## Market input (how the baselines enter)

| Input | From | Used as |
|---|---|---|
| **AI layer method v2.1:** EPS path, exit P/E, payout and cash conversion per layer; revenue-consistent Bears; "E rest" row | `docs/ai-market-bbb.md` (Update 6, 5 Nov check: all paths kept) | Blocks E (Meta, on the E rest row with the E cash conversion −.20 / .00 / .20), H1 (Broadcom), **H3 (ASML, new)**, T (software). The E-layer 2027 point (.92) is not applied: it sits in the company blocks |
| **Memory cycle section** (where, what turns it, likelihood, price-implied path, signposts) | `docs/ai-market-bbb.md` (1 Nov, re-marked 5 Nov) | The memory view in the Summary; memory returns shown in whole points |
| **Samsung** per-share V_t, D_t, EPS (common and preference; capped Bear) | `docs/samsung-analysis.md` v2 | Blocks CS (KRW 218,000 on 4 Nov) and CP (171,700); analysis prices 232,000 / 183,900 |
| **SK hynix** per-share V_t, D_t (incl. buybacks), EPS (capped Bear) | `docs/skhynix-analysis.md` v2 | Block CH at KRW 1,396,000 (analysis 1,487,000) |
| **Amazon** per-share V_t, EPS (core); no dividends | `docs/amzn-analysis.md` v2 | Block CA at $266.03 (analysis $240.35) |
| **Microsoft, Alphabet** per-share V_t, D_t, EPS | `docs/msft-analysis.md` v3, `docs/googl-analysis.md` v2 (re-mark pair at $279.84) | Blocks CM ($555.80; analysis $531.01) and CG ($288.93; re-mark $279.84) |
| **NVIDIA** per-share V_t, D_t, EPS (calendarised; revenue-consistent Bear) | `docs/nvda-analysis.md` **v1.2** | Block CN at $200.13 (analysis $181.60) |
| **TSMC** per-share V_t, D_t, EPS (revenue-consistent Bear; basis $23.43) | `docs/tsm-analysis.md` **v1.1** | Block CT at $395.75 (analysis $352.03) |
| Micron v3; AI BBB Bear-cap diagnostic | `docs/mu-analysis.md`, AI BBB | Evidence for the memory-stressed Bear and the memory cycle |
| World scenarios; USD/NOK and I-44 relative paths; World exit P/E 17, mid-cycle 8.2%, growth 5.3% | `docs/equity-market-bbb.md` (**Update 2, 6 Nov**) | Macro frame; NOK translation (USD 66.69%, other foreign 31.20%); exit cross-check; World comparison row |
| NIBOR 4.80 / 4.79 / 4.39 / 3.86; **HY reference 0.254**; HY market Base 7.2% | `docs/hy-market-bbb.md` (5 Nov) | Decision rule, triggers |
| Sissener R 0.347 / 6.4% / Bear 2027 +0.4%; HY book 0.291 / 6.9% | `docs/hy-funds-analysis.md` (31 Oct, on hold); HY book as cited | Switch check |

**Blocks** `[A]`:

| Block | Holdings | Path source |
|---|---|---|
| **CM / CG / CN / CA / CT** | Microsoft / Alphabet / NVIDIA / Amazon / TSMC | Company analyses |
| **CS / CP / CH** — memory | Samsung common / Samsung preference / SK hynix | Company analyses |
| **E** — other platforms | Meta | AI BBB "E rest" row: Bear .88 / .88 / .97 / 1.05, Base .97 / 1.07 / 1.17 / 1.27, Bull 1.00 / 1.13 / 1.27 / 1.41; E exit P/E, payout and cash conversion |
| **H1** — compute | Broadcom | AI BBB H1 |
| **H3** — foundry and equipment (new) | ASML | AI BBB H3 (Bear .76 / .63 / .67 / .71, Base .95 / 1.03 / 1.10 / 1.16, Bull 1.00 / 1.15 / 1.28 / 1.40; exit P/E 14 / 18 / 21; payout 45%) |
| **T** — software | SAP, Atlassian, Dassault, Intuit | AI BBB T |
| **X** — not AI-led | Visa, Mastercard, Adyen, Booking, T-Mobile US, Sony, Logitech, HP, Ericsson, Skyworks, Nordic Semiconductor | Own `[A]` (Nintendo left the list) |

- **Company blocks are priced at their 4 Nov closes and take the analyses' V_t, D_t and EPS as
  published.** A price different from the analysis price is a return difference. The interim V_t
  of each analysis glide from its own analysis price (see For other modules, method point).
- **NVIDIA and TSMC:** v1.2 and v1.1 carry the values this fund already used since 17 Oct
  (calendarised NVIDIA, revenue-consistent Bears); V_T Base $274.1 (was 273.9) and $506.1 (was
  499.0, now on the $23.43 basis). Only the interim glide moved.
- **Memory blocks:** the analyses' Bear (exit 8× at the trough, reached at end-2027) is the
  decision Bear. Their "capped" Bear (today's multiple on trough earnings) is the memory-stressed
  Bear, re-priced to the 4 Nov close. The preference line keeps the analysis' discount rule (20.7%
  held in Base, 30% in Bear, 15% at exit in Bull).

## Look-through valuation

Model holdings (79.1% of NAV), **prices at the 4 Nov close**, Yahoo consensus EPS of 6 Nov (NVIDIA
calendarised 15.21) `[F]`:

| Block | Weight (model = 100) | P/E on CY27 consensus | **Share of CY27 earnings** | Company or layer reference |
|---|---|---|---|---|
| **CM** — Microsoft | 12.2% | 25.2 | 6.5% | Analysis Base 9.5% at $531.01 |
| **CG** — Alphabet | 8.9% | 19.3 | 6.2% | Analysis Base 9.6% at $279.84 |
| **CN** — NVIDIA | 7.7% | 13.2 | 7.9% | Analysis Base 17.9% at $181.60 (11.9× calendarised CY27 there) |
| **CA** — Amazon | 6.4% | 24.9 | 3.4% | Analysis Base 9.2% at $240.35 |
| **CT** — TSMC | 3.0% | 16.9 | 2.4% | Analysis Base 13.7% at $352.03 (15.0× CY27 there) |
| **CS** — Samsung common | 2.2% | 2.9 | 10.3% | AI BBB 5 Nov: Samsung 2.65× |
| **CP** — Samsung preference | 1.5% | 2.3 | 9.0% | — |
| **CH** — SK hynix | 2.5% | 2.6 | 12.8% | AI BBB 5 Nov: SK hynix 2.39× |
| *Memory together* | **6.2%** | **2.6** | **32.1%** | Memory basket 2.79× (5 Nov) |
| **E** — Meta | 5.8% | 18.6 | 4.2% | — |
| **H1** — Broadcom | 5.3% | 16.7 | 4.3% | — |
| **H3** — ASML (new) | 1.6% | 23.7 | 0.9% | — |
| **T** — software | 10.8% | 21.2 | 6.9% | — |
| **X** — not AI-led | 32.1% | 17.2 | 25.2% | — |
| **Fund (model)** | 100% | **13.5** | 100% | |
| AI blocks together | **67.9%** | 12.2 | **74.8%** | |
| Fund without memory | 93.8% | **18.6** | 67.9% | |

- **Memory:** P/E 2.9 (29 Oct) → **2.6 (4 Nov)**; 2.4 at the 5 Nov closes. Prices fell (SK hynix
  −8.5%, Samsung −6.0%, preference −6.6% from 29 Oct to 4 Nov) and consensus rose a little: SK
  hynix CY27 527,157 → **529,348**, Samsung 74,057 → **75,994** `[F]`. The company blocks use the
  analyses' own EPS (built on 467,761 and 72,281: 13% and 5% below today's consensus).
- **Consensus (6 Nov):** Microsoft CY27 22.09, Alphabet 14.95, Amazon 10.67, Meta 33.93, TSMC
  23.39 (13 analysts; the analysis uses 23.43), ASML EUR 56.43 `[F]`.
- **Data handling** as in earlier versions: calendarised consensus (NVIDIA by quarters; Microsoft
  and Intuit fiscal-year blends); Alphabet and Amazon on CY27; Atlassian on Yahoo's forward P/E;
  Nordic Semiconductor's EPS in NOK; the Samsung preference shares on common EPS.
- **The remaining ~21% of NAV** is assumed to look like the model `[A]`.

## Common assumptions

| Item | Value | Basis |
|---|---|---|
| **Layer blocks** (EPS 2027 / 28 / 29 / 2030 norm.; CY27 consensus = 1.00), Bear · **Base** · Bull | E rest .88/.88/.97/1.05 · **.97/1.07/1.17/1.27** · 1.00/1.13/1.27/1.41 — H1 .68/.50/.53/.57 · **.92/.98/1.00/.97** · 1.00/1.15/1.25/1.30 — H3 .76/.63/.67/.71 · **.95/1.03/1.10/1.16** · 1.00/1.15/1.28/1.40 — T .88/.85/.93/1.00 · **.95/1.03/1.11/1.19** · 1.00/1.10/1.20/1.30 | AI BBB Update 6 and 5 Nov check (unchanged rows) |
| Exit P/E (Bear / Base / Bull), payout | E 17 / 21 / 23.5, 34% · H1 13 / 17 / 19, 25% · H3 14 / 18 / 21, 45% · T 15 / 20 / 24, 45% | AI BBB |
| **Cash conversion c**, Base 2027 / 28 / 29 (Bear; Bull) | E −.20 / .00 / .20 (−.10 / .30 / .50; −.30 / −.20 / .00) · H1 .80 / .90 / .90 (.85 / .95 / .95; .75 / .85 / .90) · H3 .75 / .80 / .82 (.75 / .90 / .95; .70 / .72 / .78) · T .80 | AI BBB. Retained cash = (c − payout) × EPS each year, at face value into V_t (counted once) |
| **SK hynix (CH)**, KRW per share, Bear · **Base** · Bull | V_t 1,348,025/1,218,755/1,264,700 · **1,807,139/1,832,050/2,088,422** · 2,376,584/2,571,208/2,841,287; D_t 175,021/63,034/51,145 · **224,423/107,481/63,776** · 236,889/143,905/83,259; stub 34,181; EPS 2027–30 Base **420,985/280,657/187,104/163,716**; capped Bear V_t 624,739/616,017/661,962 | `docs/skhynix-analysis.md` v2 (unchanged) |
| **Samsung common (CS)**, KRW per share | V_t 227,401/210,885/222,348 · **305,037/315,368/363,445** · 402,248/432,587/478,856; D_t 16,081/18,251/12,172 · **18,359/25,924/18,910** · 18,981/28,982/23,639; stub 0; EPS Base **64,310/44,857/31,685/26,963**; capped Bear V_t 115,118/114,002/124,263 | `docs/samsung-analysis.md` v2 (unchanged) |
| **Samsung preference (CP)** | Same D_t and EPS; V_t 159,181/147,619/155,644 · **241,795/249,983/288,092** · 326,538/359,433/407,027; capped 80,583/79,801/86,984 | `docs/samsung-analysis.md` v2 |
| **Amazon (CA)**, USD per share | V_t 105.9/119.6/141.4 · **267.2/292.0/317.3** · 316.9/371.0/432.1; D_t 0; EPS 2027–30 7.54/6.23/7.05/8.22 · **9.69/11.28/12.68/14.00** · 10.51/13.07/15.35/17.73 | `docs/amzn-analysis.md` v2 (unchanged) |
| **Microsoft (CM)** | V_t 337.7/368.8/404.5 · **585.8/643.2/692.1** · 681.6/806.0/921.4; D_t Base **4.01/4.37/4.76**; stub 0.98; EPS Base **20.77/23.40/26.11/28.39** | `docs/msft-analysis.md` v3 (unchanged) |
| **Alphabet (CG)**, re-mark pair at $279.84 | V_t 160.1/179.0/202.6 · **306.6/337.9/371.1** · 373.0/439.3/515.9; D_t Base **0.91/0.96/1.01**; stub 0.22; EPS Base **12.66/14.28/15.89/17.44** | `docs/googl-analysis.md` v2, re-mark 1 Nov (was 340.4 / 356.8 and 412.5 / 461.8 at $324.89; same V_T) |
| **NVIDIA (CN)**, USD per share | V_t 106.7/116.0/126.9 · **220.8/253.3/274.1** · 269.5/339.6/402.6; D_t 5.12/4.92/4.43 · **6.59/8.46/8.81** · 7.00/9.59/10.70; stub 0.56; EPS Base **13.99/14.91/15.21/14.75** (Bear 10.34/7.61/8.06/8.67) | `docs/nvda-analysis.md` **v1.2** (Base V_t was 237.5 / 261.8 / 273.9) |
| **TSMC (CT)**, USD per ADS | V_t 218.7/235.1/252.7 · **405.5/456.3/506.1** · 477.3/585.6/699.7; D_t 4.54/5.15/5.75 · **4.84/6.06/7.27** · 5.15/6.96/8.78; EPS Base **22.26/24.14/25.78/27.18** (Bear 17.81/14.76/15.70/16.64; Bull 23.43/26.95/30.00/32.81) | `docs/tsm-analysis.md` **v1.1** (Base V_t was 447.1 / 474.9 / 499.0) |
| **X block** | Bear .85/.85/.93/1.00 · **Base .97/1.05/1.13/1.21** · Bull 1.00/1.09/1.18/1.27; exit 13.5 / **16.5** / 18; payout 45%; cash conversion 0.75 | Own `[A]`, unchanged |
| P/E path | Layer blocks: Base and Bull glide to exit; Bear drops at end-2027. Company blocks: the analyses' own values | Look-through method |
| Fund cost / alpha | 1.14% all-in / 0 in Base | |
| NOK | USD 66.69% × USD/NOK path; other foreign 31.20% × I-44 path; NOK 2.11% flat; one mix for all blocks | Equity BBB Update 2 (relative moves unchanged) `[A]` |

## Period table and year-end path

Index P = 100 at the 4 Nov NAV; NOK, after cost.

| Scenario | | Stub Q4-26 | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| **Base** | EPS (CY27 cons. = 1.00) | — | 0.904 | 0.880 | 0.878 |
| | Value ÷ next-year EPS (incl. retained cash) | — | 16.4 | 17.8 | 18.7 |
| | Retained cash in layer and X blocks (cumulative, P = 100) | — | 0.7 | 1.6 | 2.6 |
| | Return r_t | +0.1% | +8.0% | +9.8% | +9.0% |
| | IRR to year-end | — | 7.0% | 8.3% | **8.5%** (XIRR 8.6%) |
| **Bear** | EPS | — | 0.716 | 0.596 | 0.629 |
| | Return r_t | +0.1% | **−29.3%** | +8.1% | +11.2% |
| | IRR to year-end | — | −25.9% | −11.7% | **−5.0%** (XIRR −5.5%) |
| **Bull** | EPS | — | 0.968 | 1.004 | 1.015 |
| | Return r_t | +0.1% | +20.9% | +16.5% | +14.6% |
| | IRR to year-end | — | 18.0% | 17.3% | **16.4%** (XIRR 16.6%) |

- **Bear 2027 by block** (NOK, before cost):
  - ASML −56%, **Amazon −56%**, Broadcom −53%, Alphabet −39%, NVIDIA −38%, TSMC −38%, Microsoft
    −32%, software −30%, X −22%, Meta −12%.
  - **Memory up ~20%** on the analyses' decision Bear (8× trough exit). It falls about −38%
    capped at today's multiple.

## Return split, structural run and sensitivities

| Window, % a year | Bear | Base | Bull |
|---|---|---|---|
| IRR_T (after cost) | −5.5 | **8.6** | 16.6 |
| d (look-through cash yield) | 2.0 | 2.4 | 2.5 |
| g (value growth, P → V_T) | −7.6 | **6.3** | 14.2 |
| — normalised EPS growth (CY27 consensus → 2030) | −11.8 | **−3.1** | +1.7 |
| — value multiple (13.5 now → exit, incl. retained cash and company net cash) | +3.5 | **+10.9** | +14.6 |
| — FX (NOK path) | +2.4 | 0 | −0.9 |
| — fund cost | −1.1 | −1.1 | −1.1 |
| c (timing) | 0.1 | −0.1 | −0.2 |
| Structural IRR (layer blocks at normalised EPS from 2027; company blocks as analysed) | −5.2 | 8.9 | 16.9 |
| Cyclical (pp) | −0.3 | −0.3 | −0.3 |

- The g components compound (1 + g = the product of the four), so they do not add exactly.
- **The +11% a year "value multiple" in Base is not a re-rating.** It has three parts:
  - memory's multiple rising from 2.6 as its earnings fall to mid-cycle, with the analyses' net
    cash;
  - retained cash: 2.6 points of the 100 by 2029 in the layer and X blocks, plus the company
    blocks' net cash;
  - the company blocks' stakes (Amazon's Anthropic and OpenAI stakes, Alphabet's Anthropic stake,
    NVIDIA's holdings).
- Without memory, the exit value multiple is 19.5 against 18.6 now.
- **Structural run:** memory's cycle sits inside its company blocks, so the run normalises only
  the layer and X blocks. On the memory analyses' own structural runs the fund's structural Base
  would be ≈ 0.5 pp lower `[A]`.

**Exit cross-check** (IAF, Track A): the buyer's implied return at the Base exit is the cash
yield plus growth.
- Exit value multiple 18.7 (19.5 without memory). The earnings-weighted cash conversion in 2029 is
  **0.65** (0.62 without memory): layers from the AI BBB, company blocks from their analyses
  (Microsoft .42, Alphabet .02, Amazon .08, NVIDIA .97, TSMC .74, Samsung .95, SK hynix .68), X at
  0.75 `[A]`.
- Cash yield 0.65 ÷ 18.7 = **3.5%**. With World's long-run growth of 5.3% (Equity BBB Update 2,
  unchanged), the buyer's return is **8.8%**, against World's mid-cycle return of 8.2% and exit
  P/E of 17.0.
- **The exit is not generous against the market.**

**By block** (each block alone, before cost, NOK; 4 Nov prices) against its reference:

| Block | Weight | P/E CY27 | IRR Bear / **Base** / Bull | Bear 2027 | Reference (Base) |
|---|---|---|---|---|---|
| CM — Microsoft | 12.2% | 25.2 | −6.5 / **8.0** / 17.1 | −32.1% | Company 9.5% (at $531.01) |
| CG — Alphabet | 8.9% | 19.3 | −8.1 / **8.6** / 19.5 | −38.5% | Company 9.6% (at $279.84) |
| CN — NVIDIA | 7.7% | 13.2 | −8.6 / **14.2** / 27.5 | −38.3% | Company 17.9% (at $181.60), 13.3% (at $204.64) |
| CA — Amazon | 6.4% | 24.9 | −16.2 / **5.7** / 15.6 | **−56.1%** | Company 9.2% (at $240.35) |
| CT — TSMC | 3.0% | 16.9 | −9.7 / **9.5** / 20.2 | −37.7% | Company 13.7% (at $352.03) |
| CS / CP / CH — memory (whole points; cycle rule) | 6.2% | 2.6 | ~9 / **~26** / ~37 | ~+20% (capped ~−38%) | Memory basket ~19% at 5 Nov; the Korean prices imply ~0.66–0.75× Base 2028–30 |
| E — Meta | 5.8% | 18.6 | 2.5 / **12.6** / 19.0 | −11.6% | E rest row |
| H1 — Broadcom | 5.3% | 16.7 | −16.2 / **4.3** / 16.5 | −53.3% | Compute basket 11.8% (5 Nov) |
| H3 — ASML | 1.6% | 23.7 | −18.5 / **−0.4** / 9.3 | −56.3% | Foundry basket 11.7% (5 Nov) |
| T — software | 10.8% | 21.2 | −4.3 / **7.3** / 15.5 | −30.0% | Software basket 3.4% (5 Nov) |
| **AI blocks together** | **67.9%** | 12.2 | −6.1 / **10.2** / 20.3 | −31.6% (capped −36.8%) | **All six baskets 10.1% (5 Nov)**; the fund's AI blocks at 5 Nov: **12.1%** |
| X — not AI-led | 32.1% | 17.2 | −0.8 / **9.1** / 12.6 | −22.2% | — |

- **Selection still shows, by less:** at the same 5 Nov prices the fund's AI holdings return 12.1%
  before cost against the baskets' 10.1% (31 Oct: 10.2% vs 5.5% at 28/29 Oct prices). The baskets'
  return rose more (5.5% → 10.1%) because they hold more of the names that fell most since
  mid-October (Micron, AMD, Marvell, Lam) `[A]`.
- **ASML enters below its basket:** at P/E 24 on the H3 path it earns about 0% in Base. On 1.6% of
  the model it costs the fund ~0.1 pp.
- **Meta on the E rest row** still has a mild Bear (−12% in 2027 at P/E 18.6). On the
  analysed-platform Bear blend the fund's Bear 2027 is −30.4% instead of −29.3%.

**Attribution from the 31 Oct version** (NOK after cost):

| Step | Bear | **Base** | Bull | Bear 2027 | MoS | E / R |
|---|---|---|---|---|---|---|
| 31 Oct version (NAV 7,375.01 and closes of 29 Oct; 24 Sep weights) | −5.11 | 8.62 | 16.39 | −28.7 | −9.0% | 0.110 |
| **Company blocks:** NVIDIA v1.2 (0.00), TSMC v1.1 (+0.01), Alphabet re-mark pair (0.00), at the 29 Oct prices | −5.08 | 8.63 | 16.40 | −28.7 | −8.9% | 0.116 |
| **Inputs:** AI BBB 5 Nov (paths kept), Equity Update 2 (NOK relative moves kept), HY 5 Nov (NIBOR kept) | −5.08 | 8.63 | 16.40 | −28.7 | −8.9% | 0.116 |
| **Holdings** of 30 Sep (top 10, Nordnet list, ASML in, Nintendo out, currency mix; −0.12) | −5.42 | 8.51 | 16.41 | −29.4 | −9.2% | 0.111 |
| **Price:** + NAV 7,381.56 and closes of 4 Nov, consensus 6 Nov, stub 56 days (+0.09) = **this version** | **−5.45** | **8.60** | **16.60** | **−29.3** | **−8.9%** | **0.113** |
| Memo: + the estimated 5 Nov NAV ≈ 7,145 and the 5 Nov closes, stub 55 days (+1.39) | −4.36 | 9.99 | 18.19 | −26.8 | −5.4% | 0.147 |

- **Split of the Base change (−0.02 pp): company blocks +0.01, inputs 0.00, holdings −0.12, price
  +0.09.** The decision moves through the reference: HY's E / R rose 0.196 → 0.254, so the gap to
  the fund widened from 0.086 to 0.141.
- The company step lifts E / R (+0.006) without moving Base: the re-glided interim values lower
  Base 2027 and so the stress loss R.
- Memory-stressed Bear: −6.1% / −32.0% (31 Oct) → **−6.5% / −32.9%**; E / R 0.101 → **0.104**.

**Sensitivities** (Base unless stated; 4 Nov NAV):

| Change | Bear IRR | Base IRR | Bull IRR | Bear 2027 | E / R |
|---|---|---|---|---|---|
| Model as above | −5.5 | **8.6** | 16.6 | −29.3 | 0.113 |
| **Memory-stressed Bear:** memory capped at today's multiple (the analyses' diagnostic) | −6.5 | 8.6 | 16.6 | **−32.9** | **0.104** |
| Memory Bear exit P/E 6 / 4 (analyses 8) | −5.9 / −6.3 | 8.6 | 16.6 | −30.7 / −32.0 | 0.109 / 0.106 |
| Memory Base exit P/E 8 (analyses 10) | | 8.2 | | | 0.105 |
| **Memory 2030 EPS ×0.8 / ×0.6 / ×0.5 in Base** (cycle: the Korean prices imply ~0.66–0.75× Base 2028–30) | | 8.2 / 7.8 / 7.6 | | | 0.104 / 0.094 / 0.089 |
| Meta cash conversion like Alphabet v2 (−.38 / −.20 / .02) | −5.6 | 8.6 | 16.6 | −29.4 | 0.112 |
| Meta on the analysed-platform Bear blend (.76 / .70 / .78 / .86) | −5.9 | 8.6 | 16.6 | −30.4 | 0.110 |
| X without retained cash (c = payout 0.45) | −6.0 | 8.1 | 16.2 | −29.9 | 0.101 |
| X cash conversion 0.90 | −5.2 | 8.8 | 16.8 | −29.1 | 0.120 |
| Cost at 0.20% (the same portfolio at index cost) | −4.5 | 9.6 | 17.7 | −28.7 | 0.140 |
| Manager alpha +1.14 pp / +2.0 pp (10-year record) | −4.4 / −3.6 | 9.8 / 10.8 | 17.9 / 18.9 | −28.6 / −28.0 | 0.145 / 0.168 |
| Exit P/E −1 / +1 (all layer blocks; company blocks on their exit EPS) | −7.4 / −3.6 | 6.8 / 10.4 | 14.8 / 18.3 | −34.2 / −24.5 | 0.060 / 0.173 |
| 2027 consensus −5% for all blocks | −7.0 | 6.8 | 14.7 | −32.9 | 0.068 |
| Bear and Bull at spot FX held flat (IAF FX rule; NOK path in the model) | −7.8 | 8.6 | 17.7 | −36.0 | 0.096 |
| **NAV at the 5 Nov estimate (−3.2%, ≈ 7,145)** | −4.4 | **10.0** | 18.2 | −26.8 | **0.147** |
| At the 5 Nov estimate: alpha +2.0 pp / exit P/E +1 | −2.5 / −2.5 | 12.2 / 11.8 | 20.6 / 19.9 | −25.3 / −21.7 | 0.201 / 0.209 |
| AI-only Bear / Bull (X and NOK on Base) | −3.2 (2027 −25.0) | | 16.4 (2027 +22.0) | | |

- **No plausible single input reaches k at the 4 Nov NAV.** The highest are the manager's 10-year
  alpha record (10.8%) and an exit P/E one turn higher (10.4%). At the 5 Nov estimate the alpha
  record would just reach k (12.2%).
- **E / R never reaches the HY reference (0.254).** The best case is 0.209.
- **Memory moves the fund by about a point either way:** its cycle is the largest single
  assumption inside the fund, but not the reason it fails.

## Results

| | Bear | Base | Bull |
|---|---|---|---|
| Price P (NAV, NOK, 4 Nov) | 7,381.56 | **7,381.56** | 7,381.56 |
| IRR_T (Track A: d + g + c, after cost; NOK path) | −5.5% (stressed −6.5%) | **8.6%** | 16.6% |
| IRR_T at spot FX held flat (memo) | −7.8% | 8.6% | 17.7% |
| d / g / c | 2.0 / −7.6 / 0.1 | 2.4 / 6.3 / −0.1 | 2.5 / 14.2 / −0.2 |
| Structural IRR / cyclical (pp) | −5.2 / −0.3 | 8.9 / −0.3 | 16.9 / −0.3 |
| ΣD / V_T (P = 100) | 6.4 / 77.9 | 7.5 / 121.1 | 8.0 / 152.2 |
| **P_k (hurdle NAV, NOK) / margin of safety** | **4,425 / −40.1%** | **6,721 / −8.9%** | **8,348 / +13.1%** |
| Rule 1: d + g > k? | No | **No** (8.6% vs 12%) | **Yes** (16.6%) |
| Rule 3: P/E vs ceiling (d + g)/k² | 13.5 vs < 0 | **13.5 vs 6.8** (d + g before cost 9.8%) | 13.5 vs 12.4 |
| Exit cross-check (buyer's return at exit) | | 8.8% vs World mid-cycle 8.2%: not generous | |
| Capital preserved? ΣD + V_T vs P | **No, −15.6%** | Yes, +28.7% | Yes, +60.1% |
| At the estimated 5 Nov NAV (≈ 7,145): IRR_T / P_k / margin | −4.4% / 4,437 / −37.9% | **10.0% / 6,762 / −5.4%** | 18.2% / 8,418 / +17.8% |

- **Share of Bull already priced:** (100 − 91.1) / (113.1 − 91.1) = **40%** (31 Oct: 42%).
- **Bear capital:** −15.6% at exit (≈ −NOK 25k); −29.3% (≈ −NOK 47k) in 2027; stressed −32.9%
  (≈ −NOK 53k).

## Against high yield and World

| Base window, NOK | Base return | E (pp over NIBOR) | R (pp) | **E / R** | Bear 2027 |
|---|---|---|---|---|---|
| **Nordic HY market** (HY BBB 5 Nov; after the 0.6% typical fee) | 6.6 | 2.15 | 8.47 | **0.254** (reference) | −1.0 |
| User's HY book (after fund fees; as cited, on the 0.196 basis) | 6.9 | 2.53 | 8.69 | **0.291** | −1.9 |
| **Sissener Corporate Bond R** (the planned replacement; hy-funds 31 Oct, on hold; before Nordnet's 0.19% platform fee) | 6.4 | 1.99 | 5.73 | **0.347** | +0.4 |
| World (MSCI World in NOK, Equity BBB Update 2; return before fund fees, E after a 0.20% fee) | 6.6 | 2.08 | 25.9 | 0.080 | −18.3 |
| All six AI baskets (AI BBB, 5 Nov prices, before fees) | 10.1 | — | — | — | — |
| **DNB Teknologi A (after 1.14%; 4 Nov NAV)** | **8.6** | **4.23** | **37.4** | **0.113** | **−29.3** |
| DNB Teknologi A, memory-stressed Bear | 8.6 | 4.23 | 40.9 | 0.104 | −32.9 |
| DNB Teknologi A at the estimated 5 Nov NAV (≈ 7,145) | 10.0 | 5.62 | 38.1 | 0.147 | −26.8 |

- **Triggers** (NAV levels in NOK; at unchanged earnings, composition and upstream paths; from the
  4 Nov NAV of 7,381.56):

| Trigger | NAV change | **NAV level (NOK)** | Look-through P/E CY27 (ex memory) |
|---|---|---|---|
| Base = HY book 6.9% | +4.9% | **≈ 7,746** (already below: Base 8.6%) | 14.1 (19.5) |
| **Base IRR = k = 12% (P_k)** | **−8.9%** | **≈ 6,721** (E / R there 0.205) | 12.3 (16.9) |
| E / R = 0.216 (the reference with the HY Bear read as a shock) | −10.0% | ≈ 6,645 | 12.1 (16.8) |
| **E / R = HY market reference 0.254** | **−13.3%** | **≈ 6,399** | 11.7 (16.1) |
| E / R = 0.254 on the memory-stressed Bear | −15.9% | ≈ 6,205 | |
| E / R = HY book 0.291 | −16.4% | ≈ 6,171 | 11.3 (15.6) |

- **The E / R trigger has moved below P_k** (31 Oct: 6,723 and 6,715 coincided). At the old
  reference (0.196) it would be ≈ 6,780.
- From the estimated 5 Nov NAV: k at 6,762 (−5.4%), 0.254 at 6,401 (−10.4%), 0.291 at 6,167.
- Company triggers (from their analyses; 4 Nov / 5 Nov closes):
  - **NVIDIA:** P_k $211.9, E / R 0.254 at $178.6; $200.13 / **$181.60** (below P_k on both days);
  - **TSMC:** P_k $368.9 (clears below $361.7); $395.75 / **$353.10** (clears on 5 Nov);
  - Microsoft P_k ≈ $494 ($555.80 / $535.93); Alphabet $261.6 ($288.93 / $282.57); Amazon $221.5
    ($266.03 / $260.21): all three above their hurdles;
  - SK hynix P_k KRW 1,835,729 and Samsung 306,225 (preference 253,646): both far below.

**The planned switch (DNB Teknologi → Sissener R)**, checked on the agreed rule (E / R, Base,
Bear 2027):

| | DNB Teknologi A | Sissener R | Switch passes? |
|---|---|---|---|
| E / R | 0.113 (stressed 0.104; 0.147 at the 5 Nov estimate) | 0.347 | **Yes** (×3.1; ×2.4 at 5 Nov) |
| Bear 2027 | −29.3% (stressed −32.9%; −26.8% at 5 Nov) | +0.4% | **Yes** (≈ 30 pp better; ≈ 27 pp at 5 Nov) |
| Base window | **8.6%** (10.0% at 5 Nov; after all-in cost) | 6.4% (≈ 6.2% after Nordnet's 0.19%) | **No: −2.2 to −2.4 pp** (−3.6 to −3.8 pp at 5 Nov) |

- **Mixed, as on 31 Oct; the Base gap widens after the sell-off.** On E / R and on Bear the switch
  wins by a wide margin. On Base return it gives up ~2.2–2.4 pp a year at the 4 Nov NAV, ~3.6–3.8
  pp at the 5 Nov estimate.
- Sissener's figures are the hy-funds document's of 31 Oct, on the old market basis; that run is on
  hold until the October reports. Under the user's rule this is a choice, not a clear pass: about
  2–4 pp a year of expected return against a Bear year ~30 pp (≈ NOK 47k) better. **The user's
  call.**
- **Reading `[A]`:**
  - **The fund beats World and HY on return, and loses on risk.** It pays HY's return plus ~2 pp
    for more than four times HY's Year-1 stress. HY now pays 0.254 per unit of stress, more than
    twice the fund's 0.113.
  - **A third of 2027 consensus earnings is memory at 2.6×.** The Korean prices already discount a
    turn deeper than the AI BBB's Base; in the fund that cycle is worth about a point of Base.

## Verdict and caveat

- **Verdict: fails** (unchanged). Base margin of safety **−8.9%**: NAV NOK 7,381.56 (4 Nov) against
  a Base hurdle NAV of **NOK 6,721** (Base IRR 8.6% vs k 12%). At the estimated 5 Nov NAV
  (≈ 7,145) the margin is −5.4% (Base 10.0%): still a fail. It does **not survive Bear**: Bear P_k
  NOK 4,425; capital −15.6% at exit; −29.3% in 2027, −32.9% memory-stressed. Bull clears k (P_k
  NOK 8,348, +13.1%).
- **What the price needs:** a NAV near **NOK 6,720–6,760** for k (−8.9% from 4 Nov; −5.4% from the
  5 Nov estimate), and **≈ NOK 6,400 for E / R to reach the HY reference 0.254** (−13% from 4 Nov;
  −10% from 5 Nov).
- **What would flip it:**
  - the NAV at the trigger levels (the 5 Nov sell-off took it about a third of the way to k, and
    Seoul fell again on 6 Nov);
  - NVIDIA's Q3 (17 Nov) and the memory business reports (14–16 Nov) moving the company Bases;
  - **memory:** the cycle moves the fund's Base by about a point (memory 2030 at 0.6× Base: 7.8%).
- **For the position:** the planned switch to Sissener R stays a trade-off (better E / R and Bear,
  ~2–4 pp lower Base), not a dominance.
- **Caveat:** this is a margin-of-safety screen on a look-through model, not an intrinsic
  valuation, a price target or personal advice.
  - The paths are the AI BBB's and the company blocks' assumptions.
  - Own assumptions: the X block, its cash conversion, the Korea split, the 30 Sep weights, the
    ~21% of NAV outside the model and the 5 Nov NAV estimate.

## Risks and signposts

| Signpost | Threshold (Bear / Bull) | Now | Source |
|---|---|---|---|
| Fund NAV (triggers) | ≤ 6,721 k; ≤ 6,399 E / R 0.254 / ≥ 8,934 (Bull end-2027) | 7,381.56 (4 Nov); 5 Nov likely ≈ 7,145 | DNB AM, Nordnet |
| NVIDIA Q3 FY27 (17 Nov) | Q4 guide below Q3, supply commitments cut / Q4 guide > ~$124bn | $200.13 (4 Nov), $181.60 (5 Nov); P_k $211.9 | `docs/nvda-analysis.md` |
| Memory: Q3 business reports (~14 and ~16 Nov), contract prints (~30 Nov, ~31 Dec) | Ranges lowered, DRAM flat or down m/m / floors disclosed, DRAM up > 5% m/m | Late upcycle; Korean prices imply ~0.66–0.75× Base 2028–30 (5 Nov); P/E 2.6 in the fund (4 Nov) | AI BBB memory cycle section |
| US state siting policy (new 5 Nov) | Pause extended or a moratorium after 12 Jan / pause lifted with cost rules | Texas audit 10 Dec; governors 11–19 Jan | AI BBB |
| Alphabet: ATM equity sales; Amazon: FCF and capex 2027 | More equity for capex; FCF negative with capex > USD 290bn / FCF positive | USD 12.4bn ATM in Q3 (crossed); Amazon Q3 FCF −USD 33.5bn | Company analyses, AI BBB |
| Next-year capex guidance (late Jan–early Feb) | Flat or down / 2027 consensus > USD 1.3tn | No figure yet; no guidance change after the midterms | AI BBB |
| Vendor financing; Anthropic IPO (~20 Nov); neoclouds | Pulled or below the marks; CoreWeave credit / above the marks | CoreWeave new 2026 low on 5 Nov (touched) | AI BBB |
| Equity BBB (World) | as in `docs/equity-market-bbb.md` | World Base 6.6%; 1.6% above its pre-alert; stale after 6 Dec | Equity BBB |
| HY reference and Sissener R | Re-run after the October fund reports | 0.254 (HY BBB 5 Nov); Sissener 0.347 (31 Oct, on hold) | HY documents |
| Fund holdings | Memory cut / raised further | Korea 4.91% (30 Sep); ASML in | Monthly report |

**Before the next update:** the published 5 Nov NAV; NVIDIA's Q3 (17 Nov) and the re-run of its
analysis; the memory business reports (14–16 Nov) and the SK hynix and Samsung analyses on the
cycle lead; the HY funds re-run (Sissener on the 0.254 basis); the October monthly report.

## For other modules

- **Skill gap (for the user, unchanged):** no skill carries an equity fund mode (`equity-market-bbb`
  is market only since 18 Oct). This run kept the look-through method under `iaf-valuation`. Its
  scripts and the run data are in `.claude/skills/equity-market-bbb/references/fund/`. Decide where
  equity fund analyses live.
- **Method point (for the user; no skill text changed):** company blocks priced at a different
  price than their analysis keep the analysis' interim V_t, so the gap between the two prices lands
  in Year 1 and moves Base 2027, R and E / R (not the IRR or P_k). The NVIDIA, TSMC and Alphabet
  re-marks moved E / R by +0.006 this way. A re-glide to the fund's price date (as the World build
  does) would remove it. Decide whether the fund build should re-glide.
- **Cycle rule in a fund (for the user):** `iaf-valuation` 2026-11-01.1 leads opportunistic
  cyclical positions with the cycle. Here it is applied to the memory part only (cycle view first,
  whole-point returns), with the fund on E / R as asked. The skill does not say how the rule
  applies to a diversified fund that holds memory; a line in the skill would settle it.
- **`docs/portfolio-overview.md`** (for its owner; not edited here): the DNB Teknologi rows read:
  - Base **8.6%** (unchanged) at NAV 7,381.56 (4 Nov); hurdle NAV **≈ 6,721**; margin **−8.9%**;
    Bear P_k 4,425, Bull P_k 8,348; at the estimated 5 Nov NAV (≈ 7,145) Base 10.0%, margin −5.4%;
  - Bear 2027 **−29.3%** (−32.9% stressed); E / R **0.113** (0.104) against the new reference
    **0.254**; E / R trigger **≈ 6,399** (was 6,723);
  - position ≈ NOK 161k; switch row still **"Mixed"**, against Sissener 0.347 / 6.4% / +0.4%, with
    the Base gap ~2.2–2.4 pp (3.6–3.8 pp at 5 Nov).
- **`docs/kospi-analysis.md`** (reads this document's comparison row): DNB Teknologi 8.6% (10.0% at
  the 5 Nov estimate), E / R 0.113 (0.147), Bear 2027 −29.3%; memory 6.2% of the model and 32% of
  its 2027 earnings.
- **`ai-market-bbb`:** no row is asked to move. Observations:
  - **ASML** is now a fund holding (1.27%, 30 Sep). On the H3 path at 4 Nov (P/E 23.7) it earns
    ~0% in Base, against the foundry basket's 11.7% at 5 Nov: the basket's return sits in TSMC.
  - The fund's AI holdings return 12.1% before cost against the six baskets' 10.1% at the 5 Nov
    prices (same method).
  - Meta's E-rest Bear stays mild (−12% in 2027 at P/E 18.6), against −32% to −56% for the analysed
    platforms. Support for the Meta analysis already suggested.
- **`docs/skhynix-analysis.md`, `docs/samsung-analysis.md`:** read as company blocks; for their
  next run (cycle lead): CY27 consensus 529,348 (SK hynix, +13% on their basis) and 75,994
  (Samsung, +5%); Seoul fell again on 6 Nov (SK hynix 1,128,000, Samsung 188,700 intraday).
- **`docs/hy-funds-analysis.md`:** this document now reads the HY market reference from
  `docs/hy-market-bbb.md` and only Sissener R from the funds document.
- **`docs/global-index-funds-analysis.md`:** not read for values this run (it predates Equity
  Update 2); no input from here.
- **Company analyses (Microsoft, Alphabet, Amazon, NVIDIA, TSMC, Micron):** read only; no flag.

## Change log

- **11 Oct 2026 — first analysis.** Base 4.8%.
- **12 Oct 2026 — AI market update** (layer paths; Samsung preference shares). Base 4.9%.
- **15 Oct 2026 — Microsoft and Alphabet as company blocks**; 14 Oct NAV. Base 5.6%.
- **17 Oct 2026 — AI BBB Update 2 (method v2), NVIDIA and TSMC analyses, Micron as evidence.**
  Retained cash counted once; NVIDIA and TSMC as company blocks; v2 Bears; memory-stressed Bear and
  the Sissener R switch check added. Base 7.1%, Bear 2027 −29.0%, E / R 0.075; switch "Mixed".
- **22 Oct 2026 — AI BBB Update 3, Amazon analysis, new NAV and holdings** (iaf-valuation
  2026-10-18.2, ai-market-bbb 2026-10-22.1). Base 7.2%, hurdle NAV 6,654 (−12.6%), Bear 2027
  −30.8% (stressed −34.7%), E / R 0.074; AI holdings 8.7% vs baskets 5.1%. Fails k; switch mixed.
- **31 Oct 2026 (dated 30 Oct in its title) — Q3 company analyses, memory as company blocks, AI BBB
  Update 5, new NAV and holdings** (iaf-valuation 2026-10-29.1). NAV 7,375.01 (29 Oct); top 10 of
  24 Sep; memory as company blocks CS / CP / CH; prices as NAVs; after-tax and account rows
  dropped. Base 8.6%, P_k 6,715 (−9.0%), Bear 2027 −28.7% (stressed −32.0%), E / R 0.110 against
  0.196; AI holdings 10.2% vs baskets 5.5%. Fails k; switch mixed.
- **6 Nov 2026 — Equity Update 2, HY 5 Nov (reference 0.254), AI BBB 5 Nov check, NVIDIA v1.2,
  TSMC v1.1, 30 Sep holdings, NAV 4 Nov** (iaf-valuation **2026-11-01.1**; ai-market-bbb skill
  2026-11-06.1, document Update 6 with the 5 Nov check; equity-market-bbb document Update 2;
  hy-market-bbb document 5 Nov):
  - **Causes (register):** equity changed 6 Nov (read 18 Oct); hy changed 5 Nov (read 24 Oct); ai
    5 Nov check (read 29 Oct); nvda v1.2 and tsm v1.1 5 Nov (read 17 Oct); googl re-mark 1 Nov
    (read 29 Oct); mu v3 5 Nov (evidence only).
  - **Method:** HY reference from `docs/hy-market-bbb.md` (0.254); memory judged on the AI BBB
    memory cycle section, whole-point returns (iaf-valuation 2026-11-01.1); ASML as an H3 layer
    block; the 5 Nov NAV estimate beside the decision, since the 5 Nov NAV was not yet published.
  - **Valuation:** NAV 7,375.01 (29 Oct) → **7,381.56 (4 Nov)**; holdings at their 4 Nov closes;
    top 10 and Nordnet list of 30 Sep; consensus 6 Nov; stub 62 → 56 days.
  - **Results:**

    | | 31 Oct | 6 Nov (4 Nov NAV) | Memo: 5 Nov estimate (≈ 7,145) |
    |---|---|---|---|
    | Base IRR | 8.6% | **8.6%** (company +0.01, inputs 0.00, holdings −0.12, price +0.09) | 10.0% |
    | Bear / Bull IRR | −5.1% (stressed −6.1%) / 16.4% | −5.5% (stressed −6.5%) / 16.6% | −4.4% / 18.2% |
    | Hurdle NAV P_k Bear / Base / Bull | 4,456 / 6,715 / 8,300 | **4,425 / 6,721 / 8,348** | 4,437 / 6,762 / 8,418 |
    | Margin of safety (Base) | −9.0% | **−8.9%** | −5.4% |
    | E / R (reference) | 0.110 (0.196) | **0.113 (0.254)** | 0.147 |
    | E / R trigger NAV | 6,723 | **6,399** | 6,401 |
    | Bear 2027 | −28.7% (stressed −32.0%) | −29.3% (stressed −32.9%) | −26.8% |
    | AI holdings vs baskets (Base, before cost) | 10.2% vs 5.5% (29 Oct) | 12.1% vs 10.1% (5 Nov) | |

    **Verdict unchanged (fails k).** The switch to Sissener R stays mixed; the E / R gap to HY
    widened with the new reference.

## Appendix: own assumptions

1. **Memory on the SK hynix and Samsung analyses** (v2), at the AI BBB's 0.35 mid-cycle; judged on
   the AI BBB's memory cycle section. 32% of the fund's 2027 consensus earnings rest on them at P/E
   2.6. The memory-stressed Bear (the analyses' capped Bear) is shown beside the decision Bear.
2. **NVIDIA and TSMC** as in v1.2 and v1.1 (calendarised NVIDIA; revenue-consistent Bears).
3. **Meta on the "E rest" row** with the E layer's cash conversion; Alphabet's conversion and the
   analysed-platform Bear blend as sensitivities.
4. **The X block:** Base −3% then ~8% a year, exit P/E 16.5, cash conversion 0.75.
5. **The Korea split:** SK hynix 1.99% and Samsung common 1.73% from Nordnet (30 Sep); preference
   = Korea 4.91% (DNB AM) − 1.99 − 1.73 = 1.19%.
6. **Weights:** DNB AM top 10 and Nordnet's full list, both of 30 Sep, priced at 4 Nov. ASML on the
   AI BBB H3 layer.
7. Manager alpha 0 in Base; one currency mix for all blocks; the ~21% of NAV outside the model
   looks like the model.
8. Company blocks use the analyses' V_t, D_t and EPS at the 4 Nov close; a capped memory Bear is
   re-priced by (close − analysis price) ÷ the analysis' consensus × next-year EPS.
9. **The 5 Nov NAV estimate:** model holdings at their 5 Nov closes (European closes from Yahoo's
   regular-market price, as the daily bars were still empty), each on its currency against NOK.
   The 31 Oct estimate (7,208) was 0.4% above the implied 30 Oct NAV (≈ 7,179).

## Appendix: sources

| # | Source | Content | Observed / published |
|---|---|---|---|
| S1 | [DNB Asset Management, DNB Teknologi](https://dnbam.com/vare-fond/fond/dnb-teknologi) | NAV 7,381.56 (4 Nov); top 10, Korea 4.91%, currency mix (holdings of 30 Sep 2026); cumulative returns; 64 companies | 6 Nov 2026 |
| S2 | [Nordnet, DNB Teknologi A](https://www.nordnet.no/market/funds/16802428-dnb-teknologi-a) (public instrument API and page) | NAV 7,381.56, `last_nav_date` 4 Nov; Total pris 1.14%; full holdings list of 30 Sep (25 lines) | 6 Nov 2026 |
| S3 | Yahoo chart and quoteSummary API | 4 and 5 Nov closes; consensus EPS (6 Nov); USD/NOK, USD/KRW, EUR/NOK, SEK/NOK, JPY/NOK; Seoul intraday 6 Nov | 6 Nov 2026 |
| S4 | `docs/nvda-analysis.md` (v1.2), `docs/tsm-analysis.md` (v1.1), `docs/googl-analysis.md` (v2, re-mark 1 Nov), `docs/msft-analysis.md` (v3), `docs/amzn-analysis.md` (v2), `docs/skhynix-analysis.md` (v2), `docs/samsung-analysis.md` (v2), `docs/mu-analysis.md` (v3) | Company paths, capped Bears, triggers | 28 Oct–5 Nov 2026 |
| S5 | `docs/ai-market-bbb.md` (Update 6, 5 Nov check) | Layer paths, E rest row, cash conversion, memory cycle section, baskets at 5 Nov prices, signposts | 1 and 5 Nov 2026 |
| S6 | `docs/equity-market-bbb.md` (Update 2) | World scenarios and returns, NOK paths, exit P/E, mid-cycle return | 6 Nov 2026 |
| S7 | `docs/hy-market-bbb.md`; `docs/hy-funds-analysis.md` | NIBOR; HY reference 0.254 and market row; Sissener R | 5 Nov / 31 Oct 2026 |

**Linkage** (monthly, Mar 2022–Sep 2026; unchanged) `[F]` derived:
- fund volatility 15.9%;
- correlation (beta) with World NOK 0.77 (0.99), OSEBX 0.07, Brent −0.14;
- max daily drawdown −20.0% (Apr 2025); 2026 −16.2% (Mar).

**Prices used (4 Nov close; 5 Nov in brackets)** `[F]`:

| Ticker | Block | Close | CY27 EPS used (analysts) | P/E CY27 |
|---|---|---|---|---|
| MSFT / GOOGL | CM / CG | 555.80 (535.93) / 288.93 (282.57) | 22.09 (32/33) / 14.95 (51) | 25.2 / 19.3 |
| NVDA | CN | 200.13 (181.60) | 15.21 calendarised (FY Jan-28 15.91, 52) | 13.2 |
| AMZN | CA | 266.03 (260.21) | 10.67 (56) | 24.9 |
| TSM (ADR) | CT | 395.75 (353.10) | 23.39 (13; analysis 23.43) | 16.9 |
| 005930.KS / 005935.KS / 000660.KS | CS / CP / CH | 218,000 (201,500) / 171,700 (160,400) / 1,396,000 (1,264,000) | 75,994 (33) / 529,348 (38) | 2.9 / 2.3 / 2.6 |
| META | E | 630.00 (605.08) | 33.93 (57) | 18.6 |
| AVGO | H1 | 325.48 (291.53) | 19.47 (48) | 16.7 |
| ASML.AS | H3 | 1,337.60 (1,250.00) | 56.43 (27) | 23.7 |
| SAP / TEAM / DSY / INTU | T | 214.30 / 189.88 / 25.84 / 356.64 | 8.48 / fwd P/E / 1.440 / CY blend 25.13 | 25.3 / 28.2 / 17.9 / 14.2 |
| X (11 names) | X | V 436.57, MA 672.68, ADYEN 854.00, BKNG 170.97, TMUS 159.17, Sony 3,933, LOGI 100.12, HPQ 29.93, ERIC 107.35, SWKS 82.92, NOD 181.00 | Yahoo 6 Nov | blend 17.2 |

- **Scripts** (model v7): `.claude/skills/equity-market-bbb/references/fund/`:
  - `close.py` (closes on the NAV date and on a given last date: `close.py <NAV date>,<last date>`;
    falls back to the regular-market price when the day's bar is still empty);
  - `hold.py` (consensus);
  - `blocks.py` (weights, blocks, P/E; options `W0916`, `W0924`, `MEMLAYER`, `LAST`, `NAV=`,
    `STUB=`; default the 30 Sep holdings with ASML);
  - `fundmodel.py` (model v7: NVIDIA v1.2, TSMC v1.1, Alphabet re-mark pair; option `V6CO` for the
    v6 company values; `OLDCO` for v5);
  - `detail.py`, `sens.py` (triggers at the 0.254 reference, plus 0.216 and 0.196), `aisplit.py`,
    `navest.py`;
  - `attrib7.py` (attribution from 31 Oct, method and memory sensitivities; `attrib.py` is the
    31 Oct one).

  Run data in `fund/dnbtek/`: `v7` (this version, NAV 4 Nov), `v7last` (5 Nov closes, NAV
  7,144.76), `v6w` (v6 data with the 30 Sep holdings and ASML), and the earlier `v6`, `v6last`,
  `v5`, `v5co`, `v5w`. In a data folder run `py ../../fundmodel.py`, then `detail.py`, `sens.py`
  and `aisplit.py` the same way; from `v7`, `py ../../attrib7.py ../v6 ../v6w ../v7`. The v6
  figures reproduce with `fundmodel.py V6CO` in `v6`, and the 31 Oct attribution with
  `py ../../attrib.py ../v5 ../v5co ../v5w ../v6 V6CO` there.
