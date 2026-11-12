# IQQK (iShares MSCI Korea UCITS ETF, Dist) — the memory cycle and an IAF look-through on the Samsung and SK hynix analyses — 6 November 2026

**Version 1.8 — 6 Nov 2026: price re-mark after the 5–6 Nov chip sell-off.**
- Prices: **Seoul close of Fri 6 Nov** for every holding (version 1.7: 4 Nov). IQQK on Xetra in EUR
  (the trading line): **analysis level EUR 88.6**, the NAV-equivalent at the 6 Nov Seoul close
  (Header). Since 4 Nov, Seoul fell on both days: SK hynix −18.9%, Samsung −13.4%, Kospi −11.0%;
  IQQK's look-through −10.5% in KRW.
- Unchanged: every path, the company blocks (both analyses as they stand, 4 Nov), the method and
  the withholding. The AI BBB kept all paths on 5 Nov (a price event); the Equity BBB (Update 2,
  6 Nov) kept the I-44 relative path; the HY BBB (5 Nov) kept the NIBOR path.
- New in this version: IQQK's daily holdings file of 4 Nov; the HY market reference E / R is read
  from `docs/hy-market-bbb.md` (5 Nov): **0.254** (was 0.196).
- Earlier versions: 1.7 (4 Nov) the memory cycle first; 1.6 (29 Oct) Samsung v2; 1.5 (29 Oct) FLXK
  replaced by IQQK, because FLXK cannot be bought on Nordnet; 1.4 (28 Oct) followed FLXK; 1–1.3
  (26 Oct) compared seven Korea ETFs.

**Skill revisions used:**
- `iaf-valuation` **2026-11-01.1** (as in version 1.7). It sets k = 12%, the hurdle price and
  margin of safety, and retained cash counted once. Track B for memory runs through the company
  analyses, with the exit cross-check. From Step 7:
  - the price and P_k in the traded line, IQQK on Xetra in EUR;
  - an opportunistic cyclical position leads with the cycle and states what the price implies;
  - E / R against HY is a reference row only, with no switch rows against HY funds;
  - the decision is at spot FX held flat (FX rule).

  The fund look-through method is the one in `docs/dnb-teknologi-analysis.md` (no skill has a fund
  mode; see For other modules).
- `ai-market-bbb` **2026-11-06.1** (document **Update 6 of 1 Nov with the 5 Nov check**; version
  1.7 read Update 6 under 2026-11-01.1, the same text). It supplies:
  - the section **"H2 Memory cycle"**, which this document leads with, including its 5 Nov re-mark
    of the price-implied multipliers and the new US siting-policy row;
  - the H2 memory scenarios and catalysts (unchanged) and the capped-Bear diagnostic;
  - the memory basket at the 5 Nov prices.

  Paths, exit P/E and cash conversion are unchanged.
- `equity-market-bbb` **2026-10-24.1** (document **Update 2, 6 Nov**; stale after 6 Dec):
  - the I-44 path for KRW: relative moves unchanged (Bear +7.6% / +5.8% / +5.8%, Base flat, Bull
    −2.3%; NOK-path line only), now on spot I-44 107.8;
  - World Base **6.6%** (was 5.2%), Bear 2027 −18.3%, E / R **0.080** (was 0.024);
  - World exit P/E 17 and mid-cycle return 8.2% (unchanged).
- `hy-market-bbb` **2026-10-24.1** (document **5 Nov**; stale after 5 Dec):
  - NIBOR path unchanged; Base window NIBOR **4.37%** (stub 55 days), for the E / R reference row
    only;
  - the HY market reference E / R **0.254** (E 2.15 pp after a 0.6% fee, R 8.47 pp), now read from
    this document. `docs/hy-funds-analysis.md` is on hold until the October fund reports and is
    not needed here.

**Inputs:**
- `docs/ai-market-bbb.md` Update 6 (1 Nov) with the **5 Nov check**: the Memory cycle section, read
  as written:
  - where the cycle is, what turns it, likelihood and timing (unchanged on 5 Nov; a US
    siting-policy row added as a 2028 demand risk with no figure);
  - what the price implies, **re-marked at the 5 Nov prices: basket 0.80× / 0.52× Base 2028–30 for
    k / 0%** (0.97× / 0.65× on 30 Oct); SK hynix 0.66× / 0.43×; Samsung 0.75× / 0.49×; Micron
    1.05× / 0.70×;
  - the dated signposts (new on 5 Nov: the ERCOT/PUCT audit, 10 Dec; the governors and the Texas
    Legislature, 11–19 Jan).

  **No own memory forecast here** (CLAUDE.md).
- `docs/samsung-analysis.md` **v2** (29 Oct, Q3 report; kept unchanged at its change gate on
  4 Nov): per-share D_t, V_t and the capped Bear for the common share (analysis price KRW 232,000),
  the preference line, its net cash and payout rule. **Re-priced to 188,700 (−18.7%).**
- `docs/skhynix-analysis.md` **v2** (28 Oct, Q3 report; kept unchanged at its change gate on
  4 Nov): the same blocks (analysis price 1,487,000), stub cash KRW 34,181 a share (Q3 dividend
  20,000, record date 30 Nov, plus the 10tn buyback for cancellation), its net cash, Kioxia stake
  and payout rule. **Re-priced to 1,132,000 (−23.9%).**
- Both blocks still reproduce their analyses at their own prices: Samsung 23.5 / 5.3 / 34.6 /
  capped −10.5 against 23.3 / 5.3 / 34.3 / −10.5; SK hynix 21.2 / 2.4 / 34.0 / −14.8 against 21.1 /
  2.4 / 33.7 / −14.7 (the model's stub is now 55 days, and D_t is paid mid-year).
- `docs/nvda-analysis.md` **v1.2** (5 Nov) and `docs/mu-analysis.md` **v3** (5 Nov), for memory
  evidence only: both are price re-marks with no company data and no new memory datum. NVIDIA's
  supply commitments ($279bn, "primarily memory") are next read on 17 Nov; Micron's 86.25% gross
  margin floor for FY27 stands until FQ1-27 (16 Dec).
- **IQQK holdings: iShares' daily holdings file of 4 Nov** `[F]` (version 1.7: 2 Nov); NAV of 5 Nov.
- Comparison rows only:
  - `docs/hy-market-bbb.md` (5 Nov): the HY market reference 0.254;
  - `docs/equity-market-bbb.md` Update 2 (6 Nov): World;
  - `docs/global-index-funds-analysis.md` (re-mark 29 Oct): DNB Global Indeks A, **as it stands; it
    predates Equity Update 2** (World 5.2% → 6.6%), so its row is a day-old basis;
  - `docs/dnb-teknologi-analysis.md` (**re-run of 6 Nov**, NAV 4 Nov): Base 8.6%, E / R 0.113.
- The rest of Korea is an own block `[A]` on Yahoo consensus (42 names, 77% of the rest by weight,
  from the full EWY holdings file of 23 Oct). Its valuation anchors are FnGuide and Kiwoom via
  MoneyToday (20 Oct) `[E]`.
- Oil, rig, supply, shipping and defense baselines are not used (Korean shipbuilders and defense
  names sit in the rest block at consensus).

Model: `.claude/skills/equity-market-bbb/references/fund/korea.py` (with `korea_prep.py`,
`korea_prices.json`, `korea_data.json`; the 5–6 Nov closes, the 6 Nov index and FX entry and the
IQQK file of 4 Nov added).
- `py korea.py FUND IQQK IMPL TRIG SPOT` reproduces every figure of version 1.8.
- `py korea.py D04 FUND IQQK IMPL TRIG SPOT` reproduces version 1.7 exactly (checked line by line).
- The holdings step: version 1.8 with the 2 Nov file in place of the 4 Nov file gives the same
  figures to one decimal.

## Summary

### The memory cycle (AI Market BBB, "H2 Memory cycle", 1 Nov; checked 5 Nov)

1. **Where it is: late upcycle. Unchanged since 1 Nov.**
   - Contract prices still rise: Q4-26 conventional DRAM +10–15%, ~+20% with HBM; Q1-27 +3–8%.
     But q/q growth has halved twice since Q2-26.
   - Mobile DRAM and NAND outside enterprise SSD are about flat.
   - Supplier inventory is under two weeks, and margins are records (SK hynix 80% operating).
   - **No memory datum has moved since 1 Nov:** no contract print, no LTA terms, no capex figure.
     The 5–6 Nov falls are a price event. The AI BBB reads 5 Nov as a de-rating of the AI capex
     receivers after the US midterms (3 Nov), not a change to the fundamentals.
   - The shares: at the 6 Nov close SK hynix is **−61%**, Samsung **−48%** and Kospi **−44%** from
     their June closing highs. Both names are now further down than in either full past downturn
     (SK hynix −39% / −49%, Samsung −35% / −42%).
2. **What can turn it:**
   - Supply from 2H-27 into 2028: new fabs, the 1δ / G11 nodes, CXMT's +31% in wafers, and HBM
     wafers returning to DRAM if HBM growth slows.
   - Demand: that supply meets AI capex digestion after the contracted 2027 build, and a consumer
     market already shrinking at today's prices.
   - **New (5 Nov): US state siting policy.** Governors who pledged data-center pauses won Texas,
     Georgia and Ohio. Fewer new US sites in 2028 would mean less HBM and server DRAM installed that
     year. The 2027 build and the LTAs are not hit. It leans to the earlier or deeper side for
     2028, with no figure yet, and nothing changes before the governors sit (11–19 Jan).
   - Contracts: the LTAs are price ranges that follow the market. They soften a fall but cap the
     rise, and SK hynix and Samsung disclose no floors.
3. **How likely, and when, against Base (turn in 2028): Base kept (AI BBB, 5 Nov).**
   - **The cycle continues through 2027** (prices up into Q1-27, the 2027 build and HBM contracted)
     **and turns in 2028.** The risk is 1–2 quarters earlier for NAND and commodity DRAM.
   - 2028 depth: Base or shallower for the leaders.
   - **2029–30: Base or deeper. This is the main risk** (the 2028–29 supply wave is larger than
     2017–19's).
4. **What the price implies (AI BBB, 5 Nov prices):**
   - The memory basket earns k at **0.80× the Base 2028–30 earnings path** (0.97× on 30 Oct) and 0%
     at 0.52×. It now discounts a turn about 20% deeper or earlier than Base.
   - SK hynix prices a path 34% below Base, Samsung 25% below. Seoul fell again on 6 Nov, after
     that re-mark.

### What IQQK's price implies (6 Nov Seoul close)

Uniform multiplier m on the **Samsung and SK hynix Base earnings for 2028–30** (2027 at Base; the
rest of Korea at Base). It runs through their payouts, net cash and exit value. Read it as "the
price returns k if 2028–30 earnings come in at m × Base":

| Price-implied 2028–30 multiplier | for **k = 12%** | for **0%** |
|---|---|---|
| **IQQK** (exit P/E 10, the Base) | **0.61×** (4 Nov: 0.80×) | **0.20×** (0.32×) |
| IQQK at an exit P/E of 8 / 11 | 0.73× / 0.56× | 0.24× / 0.18× |
| Samsung / SK hynix alone (their own builds, 6 Nov) | 0.52× / 0.53× | 0.31× / 0.34× |
| *AI BBB memory basket (layer method, 5 Nov)* | *0.80×* | *0.52×* |
| *AI BBB Samsung / SK hynix (layer method, 5 Nov)* | *0.75× / 0.66×* | *0.49× / 0.43×* |

- **IQQK's price now discounts a 2028–30 turn about 40% deeper than Base** (4 Nov: about 20%).
  That is deeper than the AI BBB's 2019-depth path (~0.74× Base on 2028–30) and about the Bear's
  depth from 2028.
- IQQK still needs less than the basket: the company builds carry net cash and a faster cash
  return, Micron is not in IQQK, and the Korean shares fell again on 6 Nov after the AI BBB's
  re-mark. The rest of Korea (50% of the fund, ~9% a year, below k) lifts IQQK's multiplier from
  the names' 0.52–0.53× to 0.61×.
- **Depth decides, not timing.** IQQK on the AI BBB's named paths (EPS 2027 / 28 / 29 / 2030
  against CY27 consensus; exit P/E 10, with 8 in brackets):

  | Path | IQQK a year | P_k in EUR |
  |---|---|---|
  | **Base: turn in 2028** (.90 / .60 / .40 / .35) | **~21%** (~18%) | **~110** |
  | Earlier turn: prices fall from 2H-27 (.80 / .45 / .35 / .35) | ~19% (~16%) | ~107 |
  | Later turn: prices hold through 2028 (.95 / .85 / .55 / .40) | ~26% (~22%) | ~124 |
  | Shallower: LTA floors hold (.90 / .70 / .55 / .45) | ~26% (~23%) | ~125 |
  | **Deeper: 2019 depth, pre-AI mid-cycle** (.90 / .45 / .30 / .25) | **~15%** (~12%) | **~95** |
  | Bear path at the Base exit P/E (.60 / .30 / .25 / .25) | ~13% (~10%) | ~90 |
  | No cycle: the 2030 level from 2027 (.35 flat) | ~17% (~14%) | ~102 |

- **Against the AI BBB's judgement:**
  - The timing risk (an earlier turn) costs one to two points.
  - The 2028 judgement (Base or shallower) helps.
  - The risk named as the main one, a deeper 2029–30, **now clears k** (~15%; at an exit P/E of 8,
    ~12%). On 4 Nov it failed (~10%).
  - The exit multiple still matters as much as the depth: at an exit P/E of 8, k needs 0.73× Base.
- **Buying IQQK at EUR ~89 is a bet that the 2029–30 memory mid-cycle holds within about 40% of the
  Base** (2030 EPS ≥ ~0.21 of CY27 consensus) **and that the market pays ~10× for it at exit.** The
  price now allows for an earlier turn and for a 2019-depth one. It does not allow for a 2019-depth
  turn together with an exit P/E of 8 (~12%, at the line).

### Verdict

- **IQQK clears k in Base, with a wide margin.**
  - Base: about **21% a year** in NOK, after the 0.74% cost and Korean withholding.
  - Hurdle **P_k ≈ EUR 110** against EUR ~89: **margin of safety ≈ +25%**.
  - The hurdle did not move; the price fell 11% in EUR. A shift in the cycle moves these figures by
    whole points, so they are rounded.
- **Bear (spot FX):**
  - Decision Bear: about **4% a year**, capital preserved (+12%), P_k ≈ EUR 71. It is flattered:
    the company analyses' Bear marks for end-2027 were set at their own prices and do not fall
    with the price, and both names now trade below those marks.
  - **Capped Bear** (memory at today's multiple on trough earnings; the stress to read): **−8% a
    year; 2027 about −39%**; capital −21% at exit.
  - On the Equity BBB NOK path the krone cushions ~5 points of the 2027 loss (−34%). That cushion
    is uncertain, because KRW and NOK tend to fall together.
- **Bull:** ~32% (P_k ≈ EUR 143). The price is below the Base hurdle, so none of the Bull is
  priced.
- **What the price needs (any one):**
  - Samsung and SK hynix 2028–30 earnings at **≥ 0.61× Base** (≥ 0.73× at an exit P/E of 8);
  - or IQQK at or below **EUR ~110** at unchanged paths.
- **E / R against the HY market reference (reference only, not the gate):** 0.249 against 0.254
  (4 Nov: 0.189 against 0.196).
- Model results, not personal advice. This document neither reads nor writes
  `docs/portfolio-overview.md`.

**Decision table** (IQQK; P = 100 = the NAV-equivalent at the 6 Nov Seoul close = **EUR 88.6**; NOK
after 0.74% and withholding; spot FX held flat; EUR rows at today's EUR/KRW and EUR/NOK)

| | Bear (decision) | Capped Bear (diagnostic) | **Base** | Bull |
|---|---|---|---|---|
| IRR_T to 31 Dec 2029 (rounded) | ~4% | **~−8%** | **~21%** | ~32% |
| 2027 return | −2% | **−39%** | +32% | +66% |
| **Hurdle P_k in EUR** (price EUR 88.6) | **71** | 51 | **110** | **143** |
| Margin of safety | −19% | −42% | **+25%** | +62% |
| V_T / ΣD_t in EUR | 86 / 13 | 56 / 14 | **137 / 17** | 182 / 19 |
| Capital preserved? ΣD_t + V_T vs P | Yes, +12% | **No, −21%** | Yes, +74% | Yes, +127% |
| On the Equity BBB NOK path (I-44): IRR / 2027 / P_k EUR | 6% / +6% / 76 | −6% / −34% / 54 | as Base | 31% / +62% / 140 |
| E / R vs the HY reference 0.254 (reference only; NOK path, as in earlier versions) | | 0.249 | | |

**Per-year path** (value index, P = 100; NOK after cost; D_t paid in the year; spot FX)

| | Stub Q4-26 | 2027 | 2028 | 2029 (exit) |
|---|---|---|---|---|
| Base: D_t / V_t / return | 0.4 / 100 / +0.4% | 7.5 / 124.5 / +32% | 6.3 / 134.9 / +14% | 4.8 / **155.1** / +18% |
| Capped Bear: D_t / V_t / return | 0.4 / 100 / +0.4% | 6.2 / 55.1 / **−39%** | 5.0 / 58.1 / +15% | 3.9 / 63.7 / +16% |
| Bear / Bull V_t | 100 / 100 | 91.8 / 158.0 | 91.5 / 179.6 | 97.6 / 205.7 |

- The stub D_t is SK hynix's Q3 dividend and Q3 buyback, the only stub cash. Samsung's Q3 dividend
  (KRW 4,601) went ex on 29 Sep, so today's buyer does not get it.
- The 2027 Base return is mostly Samsung's and SK hynix's multiple gliding from ~2.5× to ~5×
  next-year earnings while their payouts come out (company analyses). It is a path diagnostic, not a
  price forecast.

**Change since version 1.7** (IQQK; spot FX for Bear, capped Bear and Bull, as in the decision
table)

| Step | Base IRR / margin of safety | Bear / capped Bear a year; capped 2027 | Bull | Base P_k in EUR | Price-implied m for k |
|---|---|---|---|---|---|
| Version 1.7 (4 Nov close; EUR 99.2) | 16.0% / +10.9% | −0.4% / −10.2%; −42.1% | 26.6% | ~110.0 | 0.80× |
| **Price:** 6 Nov close, stub 55 days (look-through −10.5% in KRW; EUR/KRW −0.7%) | 20.8% / +24.7% | 3.9% / −7.9%; −38.7% | 32.0% | ~110.5 | 0.61× |
| **Holdings:** iShares' daily file of 4 Nov, re-priced (= version 1.8) | **20.8% / +24.7%** | **3.9% / −7.9%; −38.7%** | **32.0%** | **~110.5** | **0.61×** |

- **The hurdle in EUR did not move; the price fell.** P_k is EUR ~110.0 → ~110.5. The price fell
  from EUR 99.2 to 88.6. So the margin widened from +11% to +25%.
- **Why the hurdle holds:** the Base exit values come from the company analyses and the rest's exit
  P/E on its earnings, not from today's price. A lower price buys the same paths cheaper.
- **Both Bears improved, by different amounts:** the decision Bear by 4 points (−0.4% → +3.9%),
  because its end-2027 marks are fixed; the capped Bear by 2 points (−10.2% → −7.9%), because its
  multiple moves down with the price. The capped Bear still loses about a fifth of capital.

## Tags

`[F]` fact from a fund document, filing or market print · `[E]` external or secondary · `[C]` carried
from a company analysis · `[A]` own assumption · `[?]` not found or unverified.

## Header

| Item | Value |
|---|---|
| Object | **IQQK**, iShares MSCI Korea UCITS ETF USD (Dist), ISIN IE00B0M63391 (Ireland; physical; Xetra, EUR; on Nordnet with a KID, checked 29 Oct), followed since 29 Oct |
| Purpose (user) | Exposure to SK hynix and Samsung, as an opportunistic position on the memory cycle; diversification in Korea is not the goal |
| Valuation date / exit | **6 Nov 2026** (Seoul close; run 6 Nov ~07:00 UTC) / 31 Dec 2029; **T = 3.15 years** (stub 55 days) |
| Prices `[F]` | Yahoo, close 6 Nov (15:30 KST): **Samsung 188,700** (−6.4% on the day; open 180,000, range 179,200–196,500; −13.4% since 4 Nov), preference 150,300 (discount **20.3%**), **SK hynix 1,132,000** (−10.4%; open and low 1,089,000, high 1,217,000; −18.9% since 4 Nov), SK Square 724,000 (−10.5%; −19.5%). Rest sample −4.7% since 4 Nov (−1.1% on 5 Nov, −3.7% on 6 Nov). **KOSPI 5,059.69** (−6.0%; range 4,911–5,269; −11.0% since 4 Nov; −44.5% from the 22 Jun closing high 9,114.55). 5 Nov closes: Samsung 201,500 (−7.6%), SK hynix 1,264,000 (−9.5%), Kospi 5,383.80 (−5.3%); EODHD gives the same closes for both names to 5 Nov (6 Nov not yet in EODHD) |
| IQQK price (EUR, Xetra) | **Analysis level EUR 88.6** = the NAV-equivalent at the 6 Nov Seoul close `[A]`. It is the iShares NAV of 5 Nov (**USD 105.53** `[F]`, 1-day change −5.89 USD, −5.3%; = EUR 94.04 at EUR/USD 1.1222, 16:00 UTC) rolled forward by IQQK's look-through move to the 6 Nov Seoul close (−5.89% in KRW) at today's EUR/KRW (1,517.1 at 16:00 UTC → 1,515.8). **Latest Xetra prints `[F]`:** 5 Nov open **94.39**, low 87.79, close **89.50** (−9.0%); 4 Nov open 99.22, close 98.31. The 6 Nov open (09:00 CET) was not printed at run time. Xetra trades while Seoul is shut, so the 5 Nov close already held part of 6 Nov's Seoul fall |
| Fund | 9.499m shares, NAV ≈ USD 1.00bn (5 Nov); 75 shares; cash 1.17% (incl. 0.44% futures margin), against 71 KOSPI 200 Dec-26 futures with a notional of ~1.1% of NAV, so the fund is fully invested; distributes semi-annually (iShares `[F]`) |
| Cost | **0.74% total cost at Nordnet** (from the KID; management fee 0.65% = TER) `[F]` |
| Withholding | **15% on the cash-dividend part of D_t, in the paths** (Korea–Ireland treaty, portfolio rate 15%; Revenue.ie table "10/15" `[F]`). Korea's domestic rate is 22% `[E]`. Whether the fund obtains the treaty rate is unverified `[?]` (sensitivity at 22%) |
| FX `[F]` | Yahoo, 6 Nov ~07:00 UTC: EUR/KRW **1,515.8**, EUR/NOK **10.455**, USD/KRW 1,356.2, EUR/USD 1.1186, USD/NOK 9.347 → **NOK 6.897 per 1,000 KRW** (4 Nov: 6.902). Norges Bank I-44 107.76 (5 Nov fixing; 6 Nov not yet published). The decision is at spot FX held flat; Bear and Bull are also shown on the Equity BBB **I-44 path** |
| Track | Fund look-through. Samsung and SK hynix are company blocks (Track B in their analyses), and SK Square follows SK hynix. The rest of Korea is an own block in Track A form (EPS path, exit P/E, payout, cash conversion) |
| k | **12%**, not raised (liquid large caps; single-country concentration is carried in the Bear, not in k) |
| Decision rule | **The cycle first:** the price-implied multiplier against the AI BBB's Base and its judgement (Summary). Then Base IRR against k, with the margin of safety P_k / P − 1. E / R against the HY market reference is a reference row only (user rule, 1 Nov; iaf-valuation Step 7) |

- **The NAV-equivalent depends on the fund's FX point by up to ~1%.** On 5 Nov the iShares NAV fell
  5.3% in USD while the model's look-through fell 4.9% in KRW and the won weakened 0.9% between the
  16:00 UTC prints. If the NAV used FX near the Seoul close instead, the level is EUR 87.8; the
  version-1.7 level rolled forward two days on the look-through gives EUR 88.2 `[?]`. EUR 88.6
  follows version 1.7's method (NAV at 16:00 UTC FX). Every P_k in EUR scales with it.
- **The 6 Nov Xetra open** will be on screen next to EUR 88.6. It also carries the US session of
  5 Nov after the Seoul close.
- **Cause of 6 Nov:** the US chip sell-off of 5 Nov (SOX ~−10%) carried into Seoul for a second day.
  A web search found no coverage of a Korean or company-specific cause `[?]`.

## Scenario definitions (from AI Market BBB and Equity Market BBB)

| Scenario | Samsung and SK hynix (company analyses) | Rest of Korea (own block `[A]`) | NOK (I-44; NOK-path line only) |
|---|---|---|---|
| **Base** | Contracted 2027 memory build, then digestion. Memory earnings 0.90 / 0.60 / 0.40 / 0.35 of CY27 consensus (2027–30), exit P/E 10 | EPS 0.95 of CY27 consensus in 2027, then +5% a year. P/E from 9.9 (6 Nov) to the 20-year ex-semis average 10.4 | Flat |
| **Bear** (decision) | AI financing break and a 2028 memory overshoot inside the equity recession (AI BBB 5 Nov: state siting policy is a second route to the 2028 capex cut). Memory 0.60 / 0.30 / 0.25 / 0.25; exit P/E 8, reached at end-2027 | Recession in H1 2027: EPS 0.80 / 0.78 / 0.85 / 0.92; P/E 7.5 (the 2008 and 2020 lows, 7–8) from end-2027 | +7.6% / +5.8% / +5.8% |
| **Capped Bear** (diagnostic) | As Bear, but today's core multiple is held. That multiple moves with the price: Samsung 2.80× at its analysis price → **2.20×** at 188,700; SK hynix 2.85× → **2.09×** at 1,132,000. SK Square follows SK hynix | As Bear | As Bear |
| **Bull** | Agentic adoption. Memory 1.00 / 0.80 / 0.55 / 0.45; exit P/E 11 | EPS at consensus, +7% a year; exit P/E 12 | −2.3% |

The cycle paths of the Summary (earlier, later, shallower, deeper, no cycle) are the AI BBB's named
paths, run inside the Base mechanics. They are not extra scenarios.

- **The decision Bear at today's price:** the company analyses' Bear marks for end-2027 (Samsung
  227,401, SK hynix 1,348,025 a share) were set at 232,000 and 1,487,000 and do not move with the
  price. Both names now trade below them, so the decision Bear shows a small 2027 loss only. The
  capped Bear, tied to today's multiple, is the stress this document reads.

## IQQK, its holdings and the index context

**IQQK** (iShares daily holdings file, **4 Nov 2026** `[F]`, prices at the 4 Nov Seoul close): MSCI
Korea 20/35; Samsung **27.59%** (+ preference 3.73% = group 31.32%), SK hynix **17.09%**, SK Square
4.25%, SK Inc 0.96%, Samsung Electro-Mechanics 3.20%; 75 shares; cash 1.17%, covered by KOSPI 200
futures. On 2 Nov it was 28.08 + 3.73 / 17.46 / 4.35. Re-priced to 6 Nov: Samsung 26.7 + 3.6, SK
hynix 15.5, SK Square 3.8, the rest 50.4 (SK Inc and cash included).
- **Check of the look-through weights:** on the 4 Nov weights the model's block moves give
  **−4.91%** for 5 Nov in KRW. iShares reports a 5 Nov NAV change of **−5.29%** in USD `[F]`, while
  USD/KRW rose 0.9% between the two 16:00 UTC prints (in KRW at those prints: −4.45%). The gap is
  ±0.4 pp depending on the fund's FX point `[?]`; on 3 Nov the check matched to 0.04 pp.
- **MSCI capping decides the Samsung and SK hynix weight.** MSCI Korea 20/35 lets the largest
  issuer (Samsung) reach ~31–35% and the others ~19–20% at each quarterly review.
  - The model resets IQQK to the levels seen after the August review (31.2 / 18.9) at the November
    review (effective ~1 Dec), and then at every year-end `[A]`.
  - SK hynix has drifted down to 15.5% (re-priced), so the November review would lift it by ~3
    points. The uncapped weights are above both caps (KOSPI 200 proxy).
- **SK Square** (owns ~20% of SK hynix; 1.69× CY27 consensus against 2.42× for SK hynix, 6 Nov) is
  an indirect SK hynix stake at a holdco discount.
- **Samsung-group holdings outside the thesis:** Samsung C&T, Life and Fire hold Samsung Electronics
  stakes; Samsung Electro-Mechanics and Hanmi are AI-hardware names. All sit in the rest block at
  consensus `[A]`.

**Vehicle check at 6 Nov** (after Nordnet's KID costs; withholding in; NOK path):

| | **IQQK** iShares (physical) | LKOR Amundi (swap) | DBX8 Xtrackers (physical) |
|---|---|---|---|
| Base IRR / margin of safety | **20.8% / +24.7%** | 21.1% / +25.3% | 19.8% / +21.9% |
| Capped Bear a year; 2027 | −6.0%; −34.0% | −5.9%; −33.9% | −5.7%; −33.8% |

- IQQK and LKOR are level, and the swap counterparty breaks the tie for IQQK, as before. LKOR and
  DBX8 start at their 31 Aug cap levels (no daily file read).
- FLXK (20.7%) still has no KID at Nordnet and cannot be bought (user's order rejected, 29 Oct
  `[F]`).

**Tradability on Nordnet:** unchanged since 29 Oct. IQQK has a KID at Nordnet (instrument API
`[F]`); only the order screen confirms an order. Not re-checked today `[?]`.

**Index context** (Yahoo; FnGuide and Kiwoom via MoneyToday 20 Oct `[E]`; AI BBB):
- KOSPI 5,060 on 6 Nov: 5,684 (4 Nov) → 5,384 (5 Nov, −5.3%) → 5,060 (−6.0%). That is −11.0% since
  4 Nov, −27.8% since 2 Oct (7,004) and −44.5% from the 22 Jun close.
  - On 6 Nov it opened −2.2%, fell to −8.8% and closed −6.0%. SK hynix opened at its low (−13.8%)
    and closed −10.4%.
  - Foreign net selling was above USD 10bn in October; net buying returned on 21 Oct (AI BBB). No
    November flow figure was read `[?]`.
- 12-month forward P/E 4.41× (FnGuide, 20 Oct). Ex-semis 10.3× against a 20-year average of 10.4×
  (2026 high 14.5×); crisis lows 7–8× `[E]`.
- Bottom-up check on the rest block (Yahoo consensus of 26 Oct; 42 names): **9.9× CY27 on 6 Nov
  prices** (10.2× on 4 Nov).

## Near term

| Date | Event | What it moves |
|---|---|---|
| 5–6 Nov | Seoul down two days: Samsung −13.4%, SK hynix −18.9%, rest −4.7% since 4 Nov; IQQK look-through −10.5% (KRW); IQQK on Xetra −9.0% on 5 Nov | Price only: margin +10.9% → +24.7% |
| ~12 Nov / ~1 Dec | MSCI November review announced / effective `[A]` | IQQK re-capped (SK hynix up from ~15.5% to ~19%) |
| ~14 Nov / ~16 Nov | Samsung Q3 report on DART / SK hynix Q3 business report: LTA terms, deposits, tax and bonus lines | Cycle signpost (floors?); company blocks, small |
| 17 Nov | NVIDIA Q3 FY27: Q4 guide, supply commitments ("primarily memory"), HBM per GPU | Cycle signpost; AI BBB |
| ~20 Nov | Anthropic IPO (lab financing) | Cycle signpost (AI BBB) |
| 27 Nov | Samsung Q3 dividend paid (ex 29 Sep) | Not to today's buyer |
| 30 Nov | SK hynix Q3 dividend record date (KRW 20,000) | In the stub D_t |
| ~30 Nov, ~31 Dec | DRAM and NAND monthly contract prints | Cycle signpost |
| 10 Dec | ERCOT/PUCT data-center audit to the Texas PUC (new, AI BBB 5 Nov) | Cycle signpost (2028 demand, US siting) |
| 16 Dec | Micron FQ1-27 | Cycle signpost; AI BBB recalibration trigger |
| 17 Dec | Norges Bank MPR 4/26 (new I-44 projection; Equity BBB) | NOK-path line only |
| ~7 Jan / 11–19 Jan / late Jan | Samsung Q4 preliminary / governors of Ohio and Georgia (11 Jan) and Texas (19 Jan), Texas Legislature from 12 Jan (new) / SK hynix (~28 Jan) and Samsung (~29 Jan) Q4 reports: 2027 capex, the rest of the 2026 returns (Samsung 55–75tn, 65 assumed; SK hynix ~35tn) | Company blocks; cycle signposts (capex, siting) |

- **Stub:** price flat at the stub-end mark. The only stub distribution is SK hynix's KRW 34,181 a
  share (3.0% of its price; 20,000 of it a dividend), paid at the stub end in the model. That is 0.43
  of IQQK after cost and withholding.

## Market input (how the baselines enter)

| Input | From | Used as |
|---|---|---|
| Samsung common (analysis price 232,000): D_t 18,359 / 25,924 / 18,910 and V_t 305,037 / 315,368 / 363,445 (Base); Bear 16,081 / 18,251 / 12,172 and 227,401 / 210,885 / 222,348; Bull 18,981 / 28,982 / 23,639 and 402,248 / 432,587 / 478,856 (KRW); stub D_t 0. Base EPS 64,310 / 44,857 / 31,685 / 26,963 (2030 core); net cash 67,470 / 82,709 / 93,818; payout 50% of FCF (30% in the year, 70% the next April) | `docs/samsung-analysis.md` v2 `[C]` | Block S, **re-priced to 188,700**: interim Base and Bull marks move by the price change × the glide left (2/3, 1/3, 0) |
| Samsung capped Bear: V_t = 2.803 × next-year core EPS + net cash → 115,118 / 114,002 / 124,263 at 232,000 | Samsung analysis v2 `[C]` | Capped Bear; the multiple moves with the price (2.20× at 188,700) |
| Samsung preference (150,300): same D_t; V = common × (1 − discount): **20.3% held** (Base), 30% (Bear, capped), 20.3% → 15% (Bull) | Samsung analysis v2 `[C]`; price Yahoo `[F]` | Block SP |
| SK hynix (analysis price 1,487,000): stub D_t 34,181; D_t 224,423 / 107,481 / 63,776 and V_t 1,807,139 / 1,832,050 / 2,088,422 (Base); Bear 175,021 / 63,034 / 51,145 and 1,348,025 / 1,218,755 / 1,264,700; Bull 236,889 / 143,905 / 83,259 and 2,376,584 / 2,571,208 / 2,841,287; capped V_t 624,739 / 616,017 / 661,962. Base EPS 420,985 / 280,657 / 187,104 / 163,716; net cash 248,803 / 356,284 / 420,060; Kioxia 31,198; payout 50% of FCF in the year | `docs/skhynix-analysis.md` v2 `[C]` | Block H, **re-priced to 1,132,000** (same rules; capped multiple 2.09×) |
| SK Square | SK hynix total return, nothing paid out, holdco discount held `[A]` | Block Q |
| **H2 Memory cycle section:** where, what turns it (with the 5 Nov US siting-policy row), likelihood and timing, the price-implied multipliers re-marked at 5 Nov (basket 0.80 / 0.52; SK hynix 0.66 / 0.43; Samsung 0.75 / 0.49), the named turn-date and depth paths, the dated signposts | `docs/ai-market-bbb.md` Update 6 with the 5 Nov check | **Lead of the Summary**; the named paths run through IQQK |
| H2 scenarios, catalysts, the Bear-multiple warning, the capped diagnostic; memory basket at the 5 Nov prices (Base 19.4%, P/E CY27 2.79, margin +21.1%) | `docs/ai-market-bbb.md` 5 Nov check | Scenario frame; capped Bear as the stress; comparison |
| I-44 path (KRW → NOK; relative moves unchanged, spot 107.8); World 6.6%, Bear 2027 −18.3%, E / R 0.080; World exit P/E 17, mid-cycle 8.2% | `docs/equity-market-bbb.md` Update 2 (6 Nov) | NOK-path line; comparison; exit cross-check |
| NIBOR window 4.37% (stub 55 days); HY reference E / R **0.254**; HY Base 7.2% (6.6% after 0.6%), Bear 2027 −1.0% after the fee | `docs/hy-market-bbb.md` (5 Nov) | **Reference row only** |
| DNB Global Indeks A (re-mark 29 Oct; predates Equity Update 2); DNB Teknologi A (re-run of 6 Nov, NAV 4 Nov) | `docs/global-index-funds-analysis.md`, `docs/dnb-teknologi-analysis.md` | Comparison rows |

## Look-through valuation

IQQK on its 4 Nov holdings, re-priced to the 6 Nov close `[F]`/`[A]`:

| | Samsung (+ pref) | SK hynix | SK Square | Rest (incl. cash) | P/E on CY27 consensus | Samsung + SK hynix share of CY27 earnings (+ SK Square) | After each review: Samsung + SK hynix |
|---|---|---|---|---|---|---|---|
| IQQK, 6 Nov | 26.7 (+3.6) | 15.5 | 3.8 | 50.4 | **3.92** | **71.9%** (80.1%) | 50.1% |
| *IQQK, 4 Nov (version 1.7)* | *27.6 (+3.7)* | *17.1* | *4.3* | *47.3* | *4.35* | *71.7% (79.8%)* | *50.1%* |

- CY27 consensus (Yahoo, 26 Oct `[F]`; 11 days old) at the 6 Nov prices:
  - Samsung KRW 72,281: P/E 2.61;
  - SK hynix 467,761: 2.42;
  - SK Square 428,469: 1.69.

  The preference share is on common EPS.
- On the 5 Nov consensus the AI BBB uses (SK hynix 529,348; Samsung 75,994) the two are at 2.14× and
  2.48×.
  - The look-through keeps the 26 Oct basis for all names, so one date applies throughout. It is
    not a valuation input.
  - The company blocks' paths are on their own (26 Oct) basis, so the multipliers in the Summary
    are against those paths (see the basis note under What the price implies).

## Common assumptions

| Item | Value | Basis |
|---|---|---|
| Rest-of-Korea EPS, rel. to CY27 consensus = 1.00 (2027 / 28 / 29 / 2030 normalised), Bear · **Base** · Bull | .80 / .78 / .85 / .92 · **.95 / .9975 / 1.047 / 1.100** · 1.00 / 1.07 / 1.14 / 1.22 | `[A]`. Base: a 5% haircut on consensus, then +5% a year. Bear: Equity BBB World rest 0.83 in 2027, deeper for Korean exporters |
| Rest exit P/E (Bear / **Base** / Bull) | 7.5 / **10.4** / 12 | 20-year ex-semis average 10.4 (Kiwoom); crisis lows 7–8; 2026 high 14.5 `[E]`/`[A]`. Bear P/E reached at end-2027; Base and Bull glide from today's 9.9 |
| Rest payout / cash conversion | 30% / 0.50 → retained cash 0.20 × EPS a year at face value | `[A]`: +5% growth at ROE ~10% needs ~50% reinvested |
| Samsung, SK hynix, preference | Company analyses, both re-priced (see Market input) | `[C]` |
| SK Square | SK hynix total return; discount held | `[A]` |
| Caps | IQQK 31.2 (Samsung group) / 18.9 (SK hynix) after each review. Freed weight goes to the rest and SK Square pro rata. IQQK starts at its 4 Nov daily file, re-priced | `[A]` from the levels seen after the August review |
| Cost | 0.74% (Nordnet total cost from the KID) | `[F]` |
| Korean withholding | 15% on the cash-dividend part of D_t, every scenario. Cash-dividend share: Samsung and SK hynix 50% of D_t; SK hynix stub 20,000 of 34,181; rest of Korea 100%; SK Square nil. Buybacks for cancellation carry no tax for a holder that does not sell | Rate: treaty `[F]`; shares `[A]` (SK hynix's FY2026 return is ~30% dividends, Samsung's 2026 ≥ 35%) |
| FX | Decision at spot FX held flat. Equity BBB I-44 path (KRW; relative moves, Update 2 unchanged): Bear 1.076 / 1.058 / 1.058, Base 1, Bull 0.977, as a line | iaf-valuation FX rule; Equity BBB |
| Not in the model | Bid-ask, Nordnet FX fee | Sensitivities below |
| Personal tax and account type | Not considered: the decision is on investment value (user, 26 Oct) | — |

## Results

All NOK; P = 100 at the 6 Nov NAV-equivalent. Bear and Bull in this table are on the NOK path
(I-44), as in earlier versions; the spot-FX decision figures are in the Summary. Model output has
one decimal for tracking. A shift in the cycle moves these figures by whole points.

| | **IQQK** (after cost) | its Samsung + SK hynix part (no cost) | its rest of Korea (no cost) |
|---|---|---|---|
| **Base IRR_T** | **20.8%** | 32.8% | 8.8% |
| d / g / c (Base) | 6.0 / 14.9 / −0.2 | 10.5 / 22.6 / −0.3 | 2.4 / 6.4 / −0.1 |
| ΣD_t / V_T (Base) | 19.0 / 155.1 | 33.0 / 189.9 | 7.7 / 121.7 |
| **P_k / margin of safety** | 124.7 / **+24.7%** | 160.9 / +60.9% | 91.5 / −8.5% |
| Bear IRR / 2027 (NOK path) | 6.0% / +5.5% | 14.8% / +38.9% | −5.0% / −32.4% |
| Bear IRR / 2027 at spot FX | 3.9% / −1.9% | | |
| **Capped Bear IRR / 2027** (NOK path; spot FX) | −6.0% / −34.0%; **−7.9% / −38.7%** | −5.8% / −34.6% | −5.0% / −32.4% |
| Capital preserved? (Bear / capped; NOK path) | +18.5% / −16.1% | +47.3% / −14.6% | −14.4% / −14.4% |
| Bull IRR (NOK path; spot FX) | 30.9%; 32.0% | 44.3% | 16.3% |
| E / R, capped Bear (reference; E 16.5 pp, R 66.1 pp) | 0.249 | 0.313 | 0.116 |

- The Samsung + SK hynix part is IQQK's mix (Samsung group 30.3, SK hynix 15.5), without SK Square,
  re-capping or cost; withholding is in all three columns.
- **The Bear of the Samsung + SK hynix part gains in 2027 (+39%)** because the company analyses'
  Bear marks at end-2027 sit above today's prices (Scenario definitions). The capped Bear is the
  stress to read.
- **Share of Bull already priced:** negative (P below the Base hurdle).
- **Structural vs cyclical:** the cycle path "no cycle" sets memory earnings at the 2030 level from
  2027, with payouts and net cash following. On it IQQK returns **17.4%**, so the 2027–28 upcycle
  adds ~3 pp to the 20.8%.
  - At today's price the 2030 mid-cycle alone pays more than k. The margin rests on that mid-cycle
    and the exit multiple, not on the upcycle years.
  - The reconstruction gives the analyses' own structural IRRs: SK hynix 13.0% (analysis 12.9%),
    Samsung 16.3% (16.8%).
- **Exit cross-check:** the rest of Korea at exit P/E 10.4 has a cash yield of 4.8% plus 5% growth:
  a **~9.8% buyer's return**, above World's mid-cycle 8.2% (Korea's 20-year average is the reason).
  Samsung and SK hynix exit checks are in their analyses.
- **Scenario-weighted reference (convention, 25/50/25 on levels, decision Bear, NOK path):** 20.1%.
  It never replaces Base.

### What the price implies: the build

- **Method** `[A]` (unchanged):
  - Samsung's and SK hynix's Base EPS for 2028, 2029 and 2030 are scaled by one multiplier m (2027
    at Base). The change passes one for one into FCF (capex, D&A and working capital unchanged).
  - It reaches D_t by each company's payout rule: SK hynix 50% of FCF in the year; Samsung 50% of
    FCF, 30% paid in the year and 70% the next April. The rest builds net cash.
  - It reaches V_t at the interim P/E the published marks imply on next-year EPS: Samsung 5.3× and
    7.3×, SK hynix 5.4× and 7.7×, and 10× on 2030 at exit.
  - The rest of Korea stays at Base. For Samsung the scaling is on total EPS, so the non-memory
    ~9% is scaled as well.
- **Check against the company analyses' own sensitivities** (their prices, KRW; stub 55 days):

  | Test | Reconstruction | Analysis |
  |---|---|---|
  | SK hynix 2030 EPS ×0.6 | 8.9% | 8.8% |
  | SK hynix whole path ×0.81 | 12.1% | 12% |
  | Samsung 2030 memory ×0.6 / ×0.5 | 13.1% / 10.1% | 13.0% / 10.0% |
  | Samsung whole memory path −27% | 12.2% | 12% |
  | Structural: SK hynix / Samsung | 13.0% / 16.3% | 12.9% / 16.8% |

- **IQQK, all multipliers** (NOK after cost and withholding):

  | Exit P/E of Samsung and SK hynix | 2028–30 × m: for k / for 0% | all years × m: for k / for 0% |
  |---|---|---|
  | **10 (Base)** | **0.61 / 0.20** (4 Nov: 0.80 / 0.32) | 0.68 / 0.32 (0.84 / 0.42) |
  | 8 | 0.73 / 0.24 (0.95 / 0.39) | 0.79 / 0.38 (0.96 / 0.50) |
  | 11 | 0.56 / 0.18 (0.74 / 0.29) | 0.63 / 0.30 (0.78 / 0.39) |

- **Single names at 6 Nov** (their own builds, KRW, no fee):
  - Samsung: Base 32.9%; k at ×0.52, 0% at ×0.31 (4 Nov: 26.2%; ×0.64, ×0.40);
  - SK hynix: Base 34.6%; k at ×0.53, 0% at ×0.34 (4 Nov: 24.1%; ×0.70, ×0.47).
- **Basis note:** the company paths are on their 26 Oct CY27 consensus. The AI BBB's multipliers
  are on the 5 Nov consensus, which is 13.2% (SK hynix) and 5.1% (Samsung) higher, and at the 5 Nov
  prices, before Seoul's 6 Nov fall.
  - The company builds need less than the layer method (0.52–0.53× against 0.66–0.75×). The gap is
    net cash, the fast cash return and the preference line, which the layer method leaves out, plus
    the consensus basis and one more day of falling prices.
- **Named paths, full output** (exit P/E 10 / 8; P_k on the index; EUR at 0.886):

  | Path | IRR | P_k / margin | P_k EUR |
  |---|---|---|---|
  | Base | 20.8% / 17.6% | 124.7 / +24.7% | 110.5 |
  | Earlier turn | 19.4% / 15.9% | 120.5 / +20.5% | 106.8 |
  | Later turn | 25.7% / 22.5% | 139.9 / +39.9% | 124.0 |
  | Shallower | 26.2% / 22.7% | 141.6 / +41.6% | 125.5 |
  | Deeper | 14.6% / 11.7% | 106.9 / +6.9% | 94.7 |
  | Bull path at the Base exit P/E | 27.5% / 24.0% | 145.7 / +45.7% | 129.1 |
  | Bear path at the Base exit P/E | 12.8% / 9.5% | 102.1 / +2.1% | 90.5 |
  | No cycle | 17.4% / 13.7% | 115.2 / +15.2% | 102.1 |

**Sensitivities** (IQQK: Base IRR / capped Bear IRR / capped Bear 2027 / E / R as a reference; NOK
path):

| Change | IQQK |
|---|---|
| Model | 20.8 / −6.0 / −34.0 / 0.249 |
| Samsung and SK hynix exit P/E −2 / +2 | 17.6 / 23.9 |
| Samsung and SK hynix values ×0.8 every year | 16.4 / −8.4 / −39.7 / 0.212 |
| Samsung and SK hynix values for k (Base = 12%) | ×0.613 (the cycle multiplier on 2028–30 EPS is 0.61, Summary) |
| Rest exit P/E −2 (all scenarios) | 18.0 / −9.8 / −41.8 / 0.192 |
| Rest exit P/E +2 | 23.4 / −2.5 / −26.2 / 0.310 |
| Rest EPS path ×0.9 | 19.3 / −7.6 / −37.1 / 0.232 |
| Rest cash conversion 0.30 (no retained cash) | 20.1 / −6.9 / −34.8 / 0.238 |
| Adverse together (values ×0.8, rest EPS ×0.9, rest exit −2) | **11.9** / −14.0 / −49.9 / 0.128 |
| Capped Bear without the I-44 cushion (= spot FX) | −7.9 / −38.7 / 0.233 |
| No re-capping (weights drift) | 20.4 / −5.9 / −33.9 / 0.250 |
| After a 0.2% bid-ask round trip `[?]` | 20.7 |
| Withholding 15% on all D_t (upper bound) | 20.4 (P_k 123.6) |
| Withholding 22% on the dividend part (no treaty relief) | 20.5 (P_k 123.9) |
| No withholding (version 1.6 basis) | 21.4 (P_k 126.3) |
| Cost at TER 0.65% instead of 0.74% | 20.9 |

- The rest of Korea needs an exit P/E of **11.5** (2026 high 14.5) to pay k on its own (4 Nov: 11.9).
- The adverse combination is now just under k (11.9%); on 4 Nov it gave 7.5%.
- KRW and NOK tend to fall together in risk-off, so the I-44 cushion in the Bear is uncertain.
  This is why the decision is at spot FX.

## Reference only: against high yield and World

E / R against the HY market reference is **not the gate** for this position (user rule, 1 Nov).
HY's R is ~8–9 pp and an equity's 40–60 pp, so an equity needs about five times HY's excess return
to tie. No switch rows against HY funds are shown. Switches inside the HY book follow the
head-to-head rule there.

| Base window, NOK | Base | E (pp) | R (pp) | E / R | Bear 2027 |
|---|---|---|---|---|---|
| Nordic HY market (after 0.6% typical fee; HY BBB 5 Nov) | 6.6 | 2.15 | 8.47 | **0.254** (reference) | −1.0 |
| World (MSCI World in NOK; Equity BBB Update 2, 6 Nov; after a 0.20% fee) | 6.4 | 2.08 | 25.9 | 0.080 | −18.5 |
| World index fund (DNB Global Indeks A, re-mark 29 Oct; **predates Equity Update 2**, on World 5.2%) | 4.6 | 0.20 | 26.3 | 0.008 | −21.7 |
| DNB Teknologi A (**re-run of 6 Nov**, NAV 4 Nov; after 1.14%) | 8.6 | 4.23 | 37.4 | 0.113 | −29.3 |
| AI BBB memory basket (H2; 5 Nov prices; before fees) | 19.4 | — | — | not re-published at 5 Nov | — |
| **IQQK** (NOK path, as the rows above) | **20.8** | **16.5** | **66.1** | **0.249** | **−34.0** (capped) |

- DNB Teknologi at its estimated 5 Nov NAV: 10.0% and E / R 0.147 (its own document).
- DNB Teknologi holds the same Samsung and SK hynix blocks, so IQQK adds to the same memory factor.
  This document does not read the portfolio.

## Verdict and caveat

- **The cycle:** late upcycle, unchanged since 1 Nov. It continues through 2027 and turns in 2028
  (AI BBB Base, kept on 5 Nov). The AI BBB names a deeper 2029–30 as the main risk, and since 5 Nov
  US state siting policy as a new 2028 demand risk with no figure.
- **What the price implies:** IQQK's price returns k if Samsung's and SK hynix's 2028–30 earnings
  are **0.61× Base** (4 Nov: 0.80×). That is a turn about 40% deeper than Base, deeper than the AI
  BBB's 2019-depth path.
  - The price allows for an earlier turn (~19%) and for the 2019-depth path (~15%).
  - The Bear path at the Base exit P/E still returns ~13%.
  - At an exit P/E of 8: ~18% on the Base path, and k needs 0.73× Base; the 2019-depth path is
    then at the line (~12%).
- **Verdict: clears k in Base** (~21% a year, margin of safety ~+25%; **P_k ≈ EUR 110** against
  EUR ~89). The margin comes from the price fall since 4 Nov, not from a new path.
- **Bear:**
  - The decision Bear keeps capital (+12% at spot FX), but it is flattered by fixed company Bear
    marks.
  - The capped Bear loses ~21% at exit and ~39% in 2027 at spot FX (~34% on the NOK path).
- **IQQK is the buyable vehicle on Nordnet** (KID; physical; level with the swap-based LKOR).
- **Caveat:**
  - This is a margin-of-safety screen, not a price target or personal advice.
  - Everything rests on the AI BBB memory path through the company analyses. The 2029–30 mid-cycle
    (0.40 / 0.35 of CY27 consensus) and the exit P/E of 10 decide it.
  - Both company blocks are re-priced (−19% and −24% from their analysis prices), not re-run; their
    consensus basis is 11 days old (both moved up since).
  - The multiplier is a reconstruction `[A]` of the company builds. It matches their own
    sensitivities within 0.5 pp.
  - The analysis level depends on the fund's FX point by up to ~1% (Header).
  - Withholding shares are assumptions. The fund's treaty status is unverified.
  - IQQK's Nordnet spread is unverified.

## Tracking

| Run | Price (EUR) | Base IRR / margin | Base P_k (EUR) | Cycle multiplier for k | Note |
|---|---|---|---|---|---|
| Version 1.6, 29 Oct | 104.6 | 14.4% / +6.4% | 111.3 | — (values ×0.878 for k) | Samsung v2 |
| Version 1.7, 4 Nov | 99.2 | 16.0% / +10.9% | ~110.0 | 0.80× (2028–30 EPS) | Price −4.5% (KRW); withholding −0.6 pp; daily holdings ±0 |
| **Version 1.8, 6 Nov** | **88.6** | **20.8% / +24.7%** | **~110.5** | **0.61×** | Price −10.7% in EUR (look-through −10.5% in KRW) after the 5–6 Nov chip sell-off; holdings file of 4 Nov ±0 |

- **Ahead of or behind the Base path?** Neither. No memory datum has moved since 1 Nov: no
  contract-price decline, no LTA floor, no capex figure. Only prices moved, and the AI BBB read the
  5 Nov move as a price event.

## Risks and signposts

**Memory-cycle signposts, dated** (from the AI BBB's Memory cycle section, table 6, with the 5 Nov
additions):

| Date | Event | Confirms Base | Earlier or deeper turn | Later or shallower turn |
|---|---|---|---|---|
| ~14 Nov (Samsung, DART), ~16 Nov (SK hynix, 6-K) | Q3 business reports: LTA terms, deposits, contract liabilities | Ranges without floors | Ranges lowered, renegotiation language, contract liabilities falling | Floors or take-or-pay terms; large deposits |
| 17 Nov | NVIDIA Q3 FY27: Q4 guide, supply commitments, HBM per GPU | Commitments flat to up | Commitments cut; 8-Hi in place of 12-Hi | Commitments raised beyond FY29 |
| ~20 Nov | Anthropic IPO (lab financing) | Priced at or above the marks | Pulled, or priced below the Series H | Well above the marks |
| ~30 Nov, ~31 Dec | DRAMeXchange / TrendForce monthly contract prints | DRAM still up m/m; NAND flat | DRAM flat or down; NAND down; spot below contract | DRAM up > 5% m/m |
| 10 Dec (new) | ERCOT/PUCT data-center audit (Texas pause on new loads ≥ 75 MW since 3 Aug) | Audit closes; energisation resumes under conditions | Pause extended into 2027, or a statutory moratorium | Pause lifted with clear cost terms |
| Late Dec–early Jan | TrendForce Q1-27 contract outlook | Blended +0–8% | Conventional DRAM flat or negative | > +10% |
| 16 Dec | Micron FQ1-27 (margin vs the 86.25% floor, FY27 capex, RPO) | Margin ≥ 86%, sequential growth | Margin guided down; pushouts | RPO > $200bn; more floors |
| ~7 Jan 2027 | Samsung Q4 preliminary | About at consensus | A miss on memory prices | A beat |
| 11–19 Jan 2027 (new) | Governors sworn in (Ohio and Georgia 11 Jan, Texas 19 Jan); Texas Legislature from 12 Jan | Conditions and cost rules, no blanket bans | A statewide moratorium; a hyperscaler moves or cancels ≥ 1 GW | Pledges softened into cost rules |
| Late Jan (SK hynix ~28 Jan, Samsung ~29 Jan) | 2027 capex; Q1-27 bit and price guides | 2027 capex up moderately (~+20% for the three) | +30% or more, fab pull-ins: 2028–29 deeper | Flat; fabs staged back |
| Late Jan–early Feb | Hyperscaler 2027 capex figures | K1 2027 ~1.1tn | A platform guides 2027 flat or down | > 1.3tn |
| Mid-2027 | 2028 HBM volume and price negotiations | Volumes up, prices flat to down | Prices down sharply or volumes cut | Sold out at higher prices |

**IQQK and Korea:**

| Signpost | Level / trigger | Now | Source |
|---|---|---|---|
| IQQK price against P_k | Base P_k ≈ EUR 110; on the Deeper path ≈ EUR 95; on the Bear path at the Base exit ≈ EUR 90 | EUR 88.6 (5 Nov Xetra close 89.50): **below every named path's P_k** | This document |
| Samsung's January board: the rest of the 2026 return | Below KRW 55tn, or no buyback for cancellation (path: 65tn) | 55–75tn guided (29 Oct) | Samsung analysis |
| Foreign net selling of Kospi | > USD 20bn in a quarter with DRAM falling (AI BBB) | > USD 10bn in October; net buying from 21 Oct; November not read `[?]` | AI BBB |
| KOSPI ex-semis forward P/E | < 8 (Bear in progress) / > 12.5 (Bull) | 10.3 (20 Oct); rest sample 9.9× CY27 at 6 Nov | FnGuide / Kiwoom `[E]`; this document |
| KRW vs NOK in a sell-off | KRW/NOK −10% in a quarter (no I-44 cushion) | NOK 6.90 per 1,000 KRW (6 Nov; 6.90 on 4 Nov) | Yahoo |
| Index review | MSCI Korea 20/35 cap levels (IQQK) | Samsung 31.3%, SK hynix 17.1% (4 Nov file); ~30.3 / 15.5 re-priced to 6 Nov | MSCI (Nov), iShares |
| IQQK at Nordnet | KID withdrawn or an order rejected | KID present (29 Oct) | Nordnet API |

- **Tail risks not modelled:** a Korean peninsula event; US export controls reaching Korean memory
  sold to China; a Korea Value-up reversal (the rest's exit P/E).

## For other modules

- **`iaf-valuation`:** no change requested. The fund look-through still runs from `references/fund/`
  in the equity-market-bbb folder; no skill has a fund mode.
  - Observation, not a request: a company block re-priced far below its analysis price keeps the
    analysis's decision-Bear marks, which then sit above the price (both names now). The decision
    Bear is flattered; the capped Bear carries the stress. The company analyses' next real runs
    re-set their Bear marks.
- **`ai-market-bbb`:** no path change. Input for its next run (assessed here):
  - On their own builds at the 6 Nov close, Samsung prices **0.52×** and SK hynix **0.53×** Base
    2028–30, against 0.75× and 0.66× on the layer method at 5 Nov. The gap is net cash, cash return,
    the consensus basis and Seoul's 6 Nov fall.
  - IQQK prices 0.61×.
  - Kospi 5,060 on 6 Nov (−6.0%; −11.0% over 5–6 Nov; −44.5% from the June high). SK hynix −61% and
    Samsung −48% from their June highs.
- **`docs/samsung-analysis.md`, `docs/skhynix-analysis.md`:** no input back. Their own multipliers on
  their builds at 6 Nov prices are 0.52× and 0.53× for k (reconstruction `[A]`, Results). Both
  prices are now below their own decision-Bear marks for end-2027.
- **`docs/portfolio-overview.md`:** not read or written. A position would be an opportunistic equity
  line on the memory cycle. The HY-book switch rule does not apply to it (user, 1 Nov).

## Change log

- **2026-10-26 v1–1.3:** KOSPI and seven Korea ETFs on Nordnet compared on investment value
  (Samsung and SK hynix as the point of the investment; no tax, no account types). The user chose
  **FLXK** (Base 17.9%, margin +16.4%, capped Bear −6.2% / −35.0%, E / R 0.216).
- **2026-10-28 v1.4:** FLXK only; SK hynix v2 (Q3 report); all prices at the 28 Oct close. FLXK Base
  14.4%, margin +6.3%, E / R 0.169 (below the HY reference); Bear 0.1%, Bull 23.5%, capped −8.1% a
  year.
- **2026-10-29 v1.5: FLXK replaced by IQQK.**
  - The user's FLXK order was rejected at submission (EU regulation, missing information). Nordnet's
    instrument data shows no KID for FLXK, EWY, FLKR or KORX, and a KID for IQQK, LKOR and DBX8.
  - Head-to-head among the three with a KID, at 28 Oct prices and Nordnet's KID costs: IQQK 14.2% /
    +5.9% / E / R 0.163; LKOR 14.3% / +6.1% / 0.164 (swap); DBX8 13.6% / +4.3% / 0.158. **IQQK
    chosen** (physical, level with LKOR).
  - IQQK figures: Bear −0.1%, Bull 23.4%, capped −8.9% a year and −38.8% in 2027; triggers k +5.9%,
    E / R −7.7%.
  - Cost basis for the KID funds: Nordnet's total cost (IQQK 0.74%, LKOR and DBX8 0.65%) instead of
    TER; at TER IQQK gives 14.3%.
  - Model: `korea.py` (KID costs; `FUND <ticker>` report; LKOR and DBX8 in the triggers).
- **2026-10-29 v1.6: Samsung v2 (Q3).** Causes: smsn changed 29 Oct (read 25 Oct); ai changed
  29 Oct (read 24 Oct); global-index changed 29 Oct (comparison row); Samsung's Q3 report of 29 Oct
  passed.
  - Samsung blocks replaced by `docs/samsung-analysis.md` v2 (29 Oct close; D_t, V_t and capped
    V_t from its "For other modules" section; capped multiple 2.536 → 2.803; preference discount
    20.7%, Bull exit discount 18% → 15%).
  - All prices moved to the **29 Oct Seoul close**, valuation date 29 Oct, stub 63 days:
    - SK hynix re-priced to 1,526,000 on its v2 paths;
    - SK Square and the 42-name rest sample re-marked;
    - IQQK NAV-equivalent −1.05%.
  - Effect, price first and then the Samsung input:
    - Base 14.2% → 14.5% → **14.4%**; margin +5.9% → +6.8% → **+6.4%**;
    - Bear −0.1% → 0.3% → **0.2%**; Bull 23.4% → 23.8% → **23.7%**;
    - capped −8.9% → −8.8% → **−8.9%** a year (2027 −38.8% → −38.6% → **−38.7%**);
    - E / R 0.163 → 0.168 → **0.167**;
    - triggers k +5.9% → **+6.4%**, E / R −7.7% → **−6.9%**.
  - Head-to-head re-run at 29 Oct: LKOR 14.5% / +6.7% / 0.168; DBX8 13.9% / +4.9% / 0.162; FLXK
    14.6% / +6.9% / 0.173. IQQK stays the pick.
  - Comparison rows:
    - memory basket 12.5% / 0.114 → **9.1% / 0.072** (capped; Bear 2027 −52.2% → −53.5%; AI BBB
      Update 5);
    - DNB Global Indeks A 4.7% / 0.011 → **4.6% / 0.008** (Bear 2027 −21.7%; re-mark 29 Oct);
    - DNB Teknologi kept (22 Oct; re-run due 30 Oct).
  - Verdict unchanged: clears k with a thin margin, E / R below the HY reference.
  - The rest's exit P/E for k is now taken from the model's solver: 12.0 (v1.5 gave 12.1).
  - Model:
    - `korea.py`: 29 Oct as the default valuation date; `D28` for 28 Oct; Samsung v2 as default,
      `S1` for v1; TER and rest-exit-P/E-for-k lines in `FUND`;
    - `korea_prep.py` and `korea_prices.json`: 29 Oct closes added;
    - `korea_data.json` regenerated, with the 26 and 28 Oct entries unchanged.
- **2026-11-04 v1.7: the memory cycle first.** Causes: the user's review of v1.6 (1 Nov,
  `docs/review-kospi-analysis.md`, sections 4–5); AI BBB Update 6 (1 Nov: the Memory cycle section
  and the price-implied multipliers); iaf-valuation 2026-11-01.1 (Step 7); the price fall since
  29 Oct.
  - **Structure:**
    - The Summary opens with the AI BBB's cycle view, then IQQK's own price-implied multiplier
      (**0.80× Base 2028–30 for k, 0.32× for 0%**, against the basket's 0.97×), then the k verdict
      and P_k in EUR, rounded, then the signposts.
    - IQQK is run on the AI BBB's named turn-date and depth paths.
  - **E / R against HY is no longer the gate:** one reference table; the E / R trigger is dropped;
    no switch rows against HY funds.
  - **Prices:** 4 Nov Seoul close (Samsung 218,000, preference 171,700, SK hynix 1,396,000, SK
    Square 899,000, the 42-name rest sample, Kospi 5,683.80). Both company blocks are re-priced.
    - IQQK analysis level **EUR 99.2** (NAV-equivalent from the iShares NAV of 3 Nov).
    - Price step: Base 14.4% → 16.6%, margin +6.4% → +12.3%.
  - **Holdings:** IQQK starts from iShares' daily holdings file (2 Nov) instead of its 31 Aug cap
    levels: Base 16.6% → 16.6% (P_k +0.1).
  - **Korean withholding in the paths:** 15% on the cash-dividend part of D_t; 15% on all D_t is
    the upper bound (15.7%). Base 16.6% → **16.0%**, margin +12.4% → **+10.9%**.
  - **Bug fix** in `korea.py` (found by the review):
    - The stub distribution now enters the trigger (`TRIG`) and the cost lines (bid-ask,
      withholding).
    - On the version-1.6 basis: the withholding line 13.4% → 13.6%, the bid-ask line 14.2% →
      14.3%, the old E / R trigger −6.9% → −6.3%. The decision figures did not change.
    - `py korea.py D29 V16 SENS FUND IQQK TRIG` still reproduces version 1.6 exactly.
  - **FX rule:** the decision table is at spot FX held flat (iaf-valuation FX rule). The Equity BBB
    NOK path is a line.
    - At spot: Bear −0.4% (version 1.6: −1.8%), capped −10.2% / 2027 −42.1% (−10.7% / −43.0%),
      Bull 26.6% (24.7%).
    - On the NOK path: Bear 1.6%, capped −8.4% / −37.7%, Bull 25.6%.
  - **Comparison rows:** DNB Teknologi refreshed to its run of 30 Oct (7.2% / 0.074 → **8.6% /
    0.110**, Bear 2027 −28.7%); memory basket to Update 6 (12.9%; capped E / R 0.118; −52.1%); HY
    reference unchanged (0.196, 31 Oct).
  - **Header correction logged:** the v1.6 header carried a correction of itself ("Version 1.6
    called EUR 107.30 a USD NAV; it is the 28 Oct Xetra close in EUR") without a change-log line.
    The note is removed; the figure was right (28 Oct Xetra close EUR 107.30).
  - **Model:**
    - `korea.py`: 4 Nov as the default date (`D29` for 29 Oct); switches `NOFIX`, `NOWHT`, `W31AUG`
      and `V16`; withholding; the stub fix; `IMPL` (EPS multiplier, named paths, reconstruction
      checks); `SPOT` (spot-FX decision lines).
    - `korea_prep.py`: the 4 Nov entry and IQQK's daily file.
    - `korea_prices.json`: closes of 30 Oct and 2–4 Nov, the 4 Nov index and FX entry, the IQQK
      holdings of 2 Nov.
    - `korea_data.json`: regenerated; the 26, 28 and 29 Oct entries unchanged.
- **2026-11-06 v1.8: price re-mark after the 5–6 Nov chip sell-off.** Causes: Seoul −11.0% (Kospi)
  over 5–6 Nov with the US chip sell-off after the midterms (SK hynix −18.9%, Samsung −13.4% since
  4 Nov); the AI BBB's 5 Nov check (paths kept; multipliers re-marked; US siting-policy row and
  signposts); Equity BBB Update 2 (6 Nov: World 6.6%, I-44 spot 107.8, relative path unchanged);
  HY BBB 5 Nov (NIBOR path unchanged; reference E / R 0.196 → 0.254).
  - **Prices:** 6 Nov Seoul close (Samsung 188,700, preference 150,300, SK hynix 1,132,000, SK
    Square 724,000, the 42-name rest sample, Kospi 5,059.69); stub 57 → 55 days. Both company blocks
    re-priced (capped multiples 2.20× and 2.09×).
    - IQQK analysis level **EUR 99.2 → 88.6** (NAV-equivalent from the iShares NAV of 5 Nov, USD
      105.53; FX-point range EUR 87.8–88.6, Header).
  - **Holdings:** iShares' daily file of 4 Nov replaces that of 2 Nov: ±0.0 pp.
  - **Effect (spot FX):** Base 16.0% → **20.8%**; margin +10.9% → **+24.7%**; P_k EUR ~110.0 →
    **~110.5**; Bear −0.4% → 3.9%; capped −10.2% → **−7.9%** a year (2027 −42.1% → **−38.7%**);
    Bull 26.6% → 32.0%. NOK path: Bear 6.0%, capped −6.0% / −34.0%, Bull 30.9%.
  - **Price-implied multiplier:** 0.80× → **0.61×** Base 2028–30 for k (0.32× → 0.20× for 0%); at
    an exit P/E of 8, 0.95× → 0.73×. Single names on their own builds: Samsung 0.64× → 0.52×, SK
    hynix 0.70× → 0.53×. The 2019-depth path now clears k (10.2% → 14.6%).
  - **E / R (reference):** 0.189 against 0.196 → **0.249 against 0.254**.
  - **Comparison rows:** HY market from the HY BBB (6.6% after the fee, 0.254); World added from
    Equity BBB Update 2 (6.4% after 0.20%, 0.080); DNB Global Indeks A kept as it stands (re-mark
    29 Oct, predates Equity Update 2); DNB Teknologi refreshed to its 6 Nov re-run (8.6%, 0.113,
    Bear 2027 −29.3%); memory basket to the AI BBB's 5 Nov prices (19.4%; capped figures not
    re-published).
  - **Observation recorded:** the decision Bear is flattered at prices below the company analyses'
    Bear marks (Scenario definitions; For other modules).
  - **Model:**
    - `korea.py`: 6 Nov as the default date (`D04` for 4 Nov, which reproduces version 1.7 line by
      line); 6 Nov prices and stub; the TRIG line reads the HY reference by date (0.196 to 4 Nov,
      0.254 from 5 Nov).
    - `korea_prep.py`: the 6 Nov entry, with IQQK's 4 Nov daily file.
    - `korea_prices.json`: closes of 5 and 6 Nov, the 6 Nov index and FX entry (with 15-minute FX
      at the NAV and Seoul-close times), the IQQK holdings and NAV of 4–5 Nov.
    - `korea_data.json`: regenerated; the 26, 28, 29 Oct and 4 Nov entries unchanged.

## Appendix: own assumptions `[A]`

1. Rest-of-Korea block: EPS path, exit P/E 7.5 / 10.4 / 12, payout 30%, cash conversion 0.50. Its
   P/E and price moves come from a 42-name sample weighted by the full EWY holdings file (23 Oct).
2. SK Square follows SK hynix's total return at a constant discount; nothing paid out.
3. Capped Bear marks: Samsung as published in its v2 (2.803× next-year core EPS + net cash); SK
   hynix as given in its v2. The capped multiple moves with the price when a block is re-priced
   (now 2.20× and 2.09×).
4. IQQK cap levels are the ones seen after the August review (31.2 / 18.9). IQQK starts at its 4 Nov
   daily holdings file, re-priced with the block moves (SK Inc and cash at the rest's move). It is
   re-capped at the November review (~1 Dec) and every year-end against uncapped market weights
   (KOSPI 200 proxy). Freed weight goes to the rest and SK Square pro rata.
5. A company block re-priced from its analysis price (now Samsung −18.7%, SK hynix −23.9%) keeps the
   analysis's glide in its interim Base and Bull marks; the price change fades linearly to zero by
   exit. Its decision-Bear marks are not re-priced (they are independent of the price from end-2027),
   so below the analysis's own Bear marks the decision Bear is flattered.
6. IQQK analysis level = NAV-equivalent at the 6 Nov Seoul close: the iShares NAV of 5 Nov in EUR
   (16:00 UTC EUR/USD), rolled forward by the look-through move (−5.89% in KRW) at today's EUR/KRW.
   The fund's FX point is not known; at Seoul-close FX the level is ~1% lower. The Xetra open is the
   traded check.
7. A KID at Nordnet is taken as the sign that a retail order will go through.
8. **Withholding:** 15% treaty rate on the cash-dividend part of D_t. Cash-dividend shares: Samsung
   and SK hynix 50%, SK hynix stub 58.5%, rest 100%.
9. **Cycle multiplier:**
   - ΔEPS passes one for one into FCF.
   - The company payout rules take their share into D_t; the rest builds net cash.
   - V_t moves at the interim P/E implied by the published marks (10× at exit).
   - Samsung is scaled on total EPS. The AI BBB's named paths enter as year-by-year ratios to the
     Base path.

## Appendix: sources

| Source | Content | As of |
|---|---|---|
| User | FLXK order rejected at submission on Nordnet (EU regulation, missing information); the cycle-first rule (review, section 5) | 29 Oct, 1 Nov 2026 |
| [iShares UK, IKOR (= IQQK) product page](https://www.ishares.com/uk/individual/en/products/251871/ishares-msci-korea-ucits-etf-usd-dist) and its `latest-holdings.csv` | **Holdings "as of 04/Nov/2026"** (weights, cash, 71 KOSPI 200 Dec-26 futures; prices in USD at the 4 Nov Seoul closes); **NAV USD 105.53 and 1-day change −5.89 USD (5 Nov)**; 9,499,000 shares. Earlier: holdings of 2 Nov, NAV USD 110.82 (3 Nov) | 4–5 Nov 2026 (fetched 6 Nov ~07:05 UTC); 2–3 Nov (fetched 4 Nov) |
| Yahoo (chart API) | **Closes 5 and 6 Nov** (15:30 KST; 6 Nov OHLC for the four block names and Kospi) for Samsung, preference, SK hynix, SK Square, SK Inc, the 42-name rest sample, KOSPI, KOSPI 200; IQQK.DE (Xetra) bars to 5 Nov (close 89.50 from the quote meta); EUR/KRW, EUR/NOK, USD/KRW, USD/NOK, EUR/USD (daily and 15-minute) | Fetched 6 Nov 2026, ~07:00 UTC (after the Seoul close, before the Xetra open) |
| Yahoo (chart API), version 1.7 | Closes 30 Oct, 2, 3 and 4 Nov; FX and IQQK.DE bars | Fetched 4 Nov 2026, 07:25–07:35 UTC |
| EODHD (EOD prices) | Cross-check of Samsung and SK hynix closes 3–5 Nov: identical to Yahoo (6 Nov not yet in EODHD) | Fetched 6 Nov 2026 |
| Norges Bank API (`EXR/B.I44.NOK.SP`) | I-44 106.65 / 107.19 / 107.76 (3–5 Nov) | Fetched 6 Nov 2026 |
| Yahoo (quoteSummary `earningsTrend`) | CY26/CY27 consensus of 47 Korean shares | 26 Oct 2026 |
| [Revenue (Ireland): tax treaty rates](https://www.revenue.ie/en/tax-professionals/tax-agreements/rates/index.aspx) | Korea: dividends 10/15 (treaty in effect 1992) | Fetched 4 Nov 2026 |
| Nordnet instrument API (`/api/2/instruments/<id>`) | KID links and total cost for IQQK, LKOR, DBX8, FLXK, EWY, FLKR, KORX | 29 Oct 2026 |
| [justETF](https://www.justetf.com/en/etf-profile.html?isin=IE00B0M63391) | IQQK holdings at the August review level (cap levels) | 31 Aug 2026 |
| [iShares EWY latest holdings](https://www.ishares.com/us/products/239681/ishares-msci-south-korea-etf) (CSV) | Weights of the rest-of-Korea sample (data source only) | 23 Oct 2026 |
| [Global X Canada KORX](https://www.globalx.ca/product/korx) | KOSPI 200 top-10 weights as the uncapped market-weight proxy (data source only) | 30 Sep 2026 |
| [MoneyToday, 20 Oct 2026](https://www.mt.co.kr/index.php/en/stock/2026/10/20/2026102015013299958) | KOSPI forward P/E 4.41× (FnGuide), ex-semis 10.3× vs 20-year 10.4×, crisis 7–8× (Kiwoom) `[E]` | 20 Oct 2026 |
| `docs/samsung-analysis.md` (v2), `docs/skhynix-analysis.md` (v2) | Company blocks, net cash, payout rules, sensitivities (reconstruction check) | 29 Oct / 28 Oct 2026 (change gate 4 Nov: unchanged; as they stand 6 Nov) |
| `docs/nvda-analysis.md` (v1.2), `docs/mu-analysis.md` (v3) | Memory evidence only: price re-marks, no new memory datum; supply commitments and the FY27 margin floor | 5 Nov 2026 |
| `docs/ai-market-bbb.md` (Update 6 with the 5 Nov check; skill 2026-11-06.1) | **H2 Memory cycle section** (cycle view, multipliers re-marked at 5 Nov, named paths, dated signposts incl. the 5 Nov additions); US midterms note; scenarios; memory basket at 5 Nov; consensus of 5 Nov | 1 Nov / 5 Nov 2026 |
| `docs/equity-market-bbb.md` (Update 2), `docs/hy-market-bbb.md` | I-44 path (relative moves unchanged, spot 107.8), World 6.6% / 0.080; NIBOR path (unchanged), HY market reference E / R 0.254 | 6 Nov / 5 Nov 2026 |
| `docs/global-index-funds-analysis.md` (re-mark; predates Equity Update 2), `docs/dnb-teknologi-analysis.md` (re-run) | Comparison rows | 29 Oct / 6 Nov 2026 |
| `docs/hy-funds-analysis.md` | Not read in version 1.8 (on hold; the reference now comes from the HY BBB) | 31 Oct 2026 |
| `docs/review-kospi-analysis.md` | Weak spots of v1.6 and the user's rule | 1 Nov 2026 |
