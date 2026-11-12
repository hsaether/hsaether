# Review: debt-funded AI expansion, data-centre multiples and market power — 5 Nov 2026

> **Not adopted (user, 6 Nov 2026).** Judged not thorough enough to set method or re-read signposts:
> the credit levels come from aggregator sites, and the payback, funding and K1-build figures are
> order-of-magnitude `[A]` arithmetic. Everything this review added to the AI skill (revision
> 2026-11-05.1: tiers, credit by tier, K1 company build, payback coverage) and to
> `docs/ai-market-bbb.md` (second 5 Nov note, standing outputs, signposts read as crossed) was
> reverted on 6 Nov (skill 2026-11-06.1). Section 7's "applied" no longer holds. Kept as a dated
> record only; no document reads it.

Skill revisions behind this review: **ai-market-bbb 2026-11-01.1** (method, baselines, `model.py` v2.1),
**iaf-valuation 2026-11-01.1** (k = 12%, hurdle P/E). Baseline reviewed: `docs/ai-market-bbb.md` as of
5 Nov 2026 (paths of 1 Nov, kept unchanged on 5 Nov). Upstream read as they stand: Equity BBB 17/18 Oct
(NOK path Base 9.41), HY BBB 5 Nov (NIBOR window 4.38%).

Prices: Yahoo, 5 Nov 2026 20:22 UTC (US session open; Seoul close). Consensus EPS: Yahoo, 1 Nov,
calendarised as in the baseline. The model runs reproduce the baseline's 5 Nov basket table (all six
10.1%). Tags: `[F]` reported fact, `[E]` external or secondary, `[A]` my own assumption or calculation,
`[?]` unknown. Calculations are in the scratchpad (`tests.py`, `tests2.py`, copies of `model.py`).

**User's question (5 Nov):** the market questions debt-driven AI expansion. (1) Data-centre names trade at
high P/E; should they be priced like standard industry, since they have no market power? (2) Some
hyperscalers have expanded with debt and their bond pricing is rising; should we do the same? Do we
trust that income grows fast enough? Will the spending estimates have to come down? (3) MSFT, Google,
Anthropic and OpenAI have market power; do Meta and Oracle? Should the total spending estimate (K1) be
lowered?

## Answer in brief

- **AI Market BBB: kept unchanged (paths).** No K1, EPS path, exit P/E or cash-conversion point moves; every
  candidate change is below the minimum-change rule (5% of capex, 0.05 on an EPS path, 1 turn of exit
  P/E). The review reads two signposts as crossed, extends a third (below) and proposes four method
  additions, which were applied to the skill after the user's go-ahead.
- **1. Data-centre multiples: yes for owners, lessors and neoclouds, and the market has mostly done it.**
  - Eaton and Vertiv already trade at 18–20× CY27, level with Schneider (18×). Only Arista carries a
    premium (31×).
  - At an industrial exit multiple (16×) the networking and DC-infrastructure basket (H4) falls from
    +1.3% to −4.9% a year (NOK); it needs a 28× exit to earn 12%. It fails at any plausible multiple.
  - H4 is 2% of the six baskets, so this is **decision-neutral for the baseline**. The multiple that
    matters is the platforms' (47% of the six): the E layer earns 8.0% at its 21× exit and **0.9% at
    World's 17×**. It needs 23.5× to reach k.
  - Neoclouds are leveraged contract vehicles: CoreWeave's 2031 bond yields ~15.8%, so its equity
    needs ≥ 20%, not 12%.
- **2. Debt: do the same only where the debt is the weak tier; trust income near term, not for payback.**
  - The four high-grade platforms pay ~35–50 bp more than the IG index. At ~300bn of new debt a year that
    is ~1.5bn against ~900bn of 2027 operating cash flow: no EPS or k change.
  - Oracle (CDS 292 bp, BBB−) and the neoclouds (CoreWeave CDS ~1,040 bp) are priced as high yield.
    The credit market is pricing **who bears the demand risk**, not the aggregate.
  - **Income:** near term yes. The four clouds grew ~59% in Q3 and 2026 runs ahead of the row (+53%
    against +50%). **For payback no:** at Base 2029 the incremental cloud earnings cover **~33–45%** of
    what the 2025–29 spend needs to earn its cost of capital `[A]`. The rest must come after 2029 or
    from outside the clouds. The baseline already says this ("not yet paid for in any scenario"); the
    bond market now prices it by tier.
  - **Spending estimates:** 2027 does not have to come down. 2028–29 depend on two labs' funding.
    The first cuts come from the elastic tiers (Oracle, Meta, neocloud and developer capex outside K1).
- **3. Market power.** MSFT, Google and Amazon: yes in AI infrastructure (own customers, backlog, own
  silicon). Meta: yes in advertising, **not in AI compute**: no third-party contracts prove a return on
  the incremental dollar. Oracle: **no**: a price-taker whose contracts, mostly one lab's, are the
  asset. OpenAI and Anthropic: growth and scarcity pricing today, but price per token falls ~47% a
  quarter at constant capability `[E]`, so it is a lead, not a moat.
- **K1 is not lowered.** 2027 (1,120) matches the Street (~1,100–1,130). A combined Oracle −30% and
  Meta −15% cut is **−4.9% of K1** in 2027 and 2028, just under the rule, and it is a Bear-side event.
  The risk is skewed down and sits outside K1 first (see sections 3 and 4).

## 1. What the credit market says, by tier

| Tier | Who | Pricing signal (date) | Tag | Reading |
|---|---|---|---|---|
| 1. Corporate bonds of the high-grade platforms | Microsoft, Alphabet, Amazon, Meta | IG hyperscaler composite ~+35 bp over the IG index in July, ~+50 bp in H1, narrowing since (Penn Mutual, 6 Aug). AI-related issuers ~115 bp against 78 bp for IG (Goldman Sachs AM, 2026, undated). Order books ~5× covered in Feb, under 2× in July (CCIR via Startup Fortune, 11 Oct). Meta 6.30% 2056 +58 bp since early June (29 Jul). Meta 5y CDS record **114.79 bp** (Markit via Reuters, ~22 Oct, first negative FCF quarter since 2012). NVIDIA CDS 79 bp record (28 Jul) | `[E]` | Higher price for long duration and heavy supply. Technical more than fundamental (RBC, Penn Mutual). Meta's CDS is about where Oracle's was in Nov 2025 (108 bp) |
| 2. Project finance on a hyperscaler lease | Meta El Paso (1 GW, online 2028) | USD 12.5bn amortising notes due 2048, **~7.5%, +2.875 pp over the 10-year**, A+ (S&P) / AA− (Fitch), 1.6× covered, secured by 20 years of Meta rent; did not tighten from day one; ~103 cents early. Hyperion (USD 27bn, Blue Owl) ~96 cents. Hyperscaler-leased DC bonds 5.70–7.875% against CoreWeave-leased 7.00–9.875% | `[E]` (IBTimes 29 Jul; CCIR) | The marginal dollar of off-balance-sheet capacity costs ~7–7.5%, ~2 pp over the corporate curve |
| 3. Oracle | Oracle | S&P **BBB−** since July, Moody's Baa2 negative. 5y CDS **292 bp** (2 Nov; 295 on 19 Oct, +287% y/y; 282 on 15 Oct); S&P: "more in line with BB and B". 4.95% 2031 bond yields 7.28%. Debt USD 125.3bn (31 Aug). FCF FY26 −23.7bn `[F]`, FY27 consensus −36bn `[E]`. **2 Nov: filed to sell USD 10bn of stock and 10bn of notes, which equals the whole USD 20bn capital-markets cap given for FY27–30 at the 28 Oct investor day**; shares −8.8% that day, −6.9% on 5 Nov (US intraday); −33% in 2026 as of 2 Nov. Positive FCF promised in H2 FY28, USD 30bn+ in FY29; capex peaks FY27–28, steps down FY29 | `[E]` (CNBC 19 Oct, 2 Nov; company release via search excerpt) | Priced as high yield. I could not verify whether the filing is a draw or a shelf |
| 4. Neoclouds | CoreWeave | S&P B+. 5y CDS ~**1,038 bp** (briefly > 1,140), 9.75% 2031 bond **15.78%**, debt > USD 51bn, backlog > USD 100bn (~two-thirds from IG counterparties) (CNBC, 15 Oct). Shares USD 43.88 on 5 Nov, −68% from the 6 May high. NVIDIA reportedly buys unsold capacity to Apr 2032 | `[E]` | S&P: ≥ 1,000 bp "generally signals distress". Backlog is real but is not the same as funded |
| 5. Bank-held construction debt | Oracle-leased and Stargate sites | USD 38bn of construction debt for a Texas and Wisconsin site leased to Oracle: **unsold after > 6 months**; JPMorgan, Morgan Stanley, SMBC and MUFG exploring risk transfers, near single-name limits (Bloomberg via Startup Fortune, 11 Oct). **5 Nov:** a ~USD 500m portfolio of DC loans put to auction, one slice on the Stargate site in New Mexico where Oracle reportedly sent a force-majeure notice (Bloomberg headline and search summary; article not readable) | `[E]` | The financing seam is where a lab-dependent tenant meets a developer |

- **Risk-neutral default probabilities** (5y CDS ÷ (1 − 40% recovery)), a price of risk that includes risk
  premia and CDS illiquidity, not a forecast `[A]`: Meta 1.9% a year (9% over five years), Oracle 4.9%
  (22%), CoreWeave 17% (61%; Reuters quotes 63%), NVIDIA 1.3% (6%).
- **Does k = 12% hold?** An equity claim must earn more than the same company's marginal debt. Oracle
  7.3% + ~4.7 pp = 12%: holds, with no room. Meta's SPV 7.5%: holds. **CoreWeave 15.8% means equity
  ≥ ~20%**: k = 12% does not apply to neoclouds, which are outside the baskets.
- **Source conflicts:** Oracle's CDS history differs between aggregators (a 198 bp record in April and
  151 bp "highest since 2009" in early October cannot both be right). Only the CNBC series (282, 295, 292)
  is used for levels. No Bloomberg or Reuters article was read directly.

## 2. Market power as the test

Market power is the ability to earn more than the cost of capital on the **marginal** dollar of capex
and to pass the price through. Evidence by name (facts from the baseline unless noted):

| Name | Sells AI to others at its own price? | Contract cover and counterparty | Funds capex from own cash flow? | Verdict and what it implies |
|---|---|---|---|---|
| **Microsoft** | Yes: Azure +48% (guide 49–50%), Copilot | Commercial RPO USD 677bn, **flat q/q**, bookings −12% y/y; OpenAI paid 10.0bn in the quarter (10.8% of revenue) | Yes: PP&E paid 68% of OCF, AAA, net cash 29bn | **Price-setter in enterprise**, weaker at the model layer (OpenAI is customer and rival). Low capex elasticity |
| **Alphabet** | Yes: Cloud +103%, own TPUs sold into customers' data centres | Cloud backlog USD 561bn (+9% q/q); Anthropic ≥ 114.5bn of it | Not in Q3: capex 121% of OCF, FCF −9.1bn, **ATM equity 12.4bn**, buybacks stopped | **Price-setter**, now funding with equity. Low elasticity |
| **Amazon** | Yes: AWS +39.3% (sixth quarter of acceleration) | Backlog USD 578bn (+16.5% q/q, 6.1 years); **OpenAI 138 and Anthropic ≥ 110 = 43% of it** | No: capex 179% of OCF in Q3, TTM FCF −42bn, long-term debt 181bn (69bn at end-2025) | **Price-setter in infrastructure, concentrated.** Elasticity low while the two labs fund |
| **Meta** | **No.** No cloud and no third-party AI revenue | **None.** The payoff is ad performance: Q3 revenue +26% (impressions +10%, price per ad +14%) | Barely: capex 135–145bn, Q3 FCF −2.1bn (106% of OCF), no buybacks, non-voting Class C from Jan 2027 for "capital raising", El Paso JV off balance sheet | **Market power in advertising, none in AI compute.** The return on the incremental dollar cannot be checked against a contract. **Highest elasticity** of the five: Meta cut capex plans and took data-centre charges when ad revenue stalled in late 2022 (background, not re-sourced here `[E]`) |
| **Oracle** | Yes, as a lessor of GPU capacity | RPO USD 664bn (31 Aug); **more than half OpenAI** (BofA via a Substack note `[E]`); USD 75bn covered by customer prepayments or customer-supplied hardware | **No:** FCF −23.7bn FY26 and −36bn FY27E, funding cap USD 20bn for FY27–30 now filed in full | **Price-taker.** Contracts are the asset, the counterparty is one lab, gross margin guided down in FY27. Priced like a lessor, not a platform |
| **OpenAI** | Yes | Run-rate ~USD 50bn (end-Sep, +77% in Q3); booked 2026 ~39bn `[A]`; compute plan ~600bn to 2030 `[E]` | No: spends ~its whole revenue with one cloud (10bn to Microsoft in Q3); NVIDIA guarantees up to 105bn of its Ohio leases | **Demand without a moat today.** Funded by raises |
| **Anthropic** | Yes | H1-26 revenue 16.3bn `[F]` (S-1); run-rate 65bn in July (includes cloud-partner sales); commitments ~518bn over ~10 years, ~80% non-cancellable `[E]` | Adjusted operating profit in Q2 (S-1 via Reuters `[E]`); IPO reported for the week of 16 Nov at USD 1.5–2tn | **Stronger than OpenAI on enterprise and coding**, still a lead in capability, not in price |
| **Neoclouds** | Yes, as lessors | Backlog > 100bn, ~two-thirds IG counterparties | No: 15–16% debt | **No market power;** leveraged infrastructure |
| **H4 suppliers** | Yes | Orders, no backlog series | Yes | Vertiv and Eaton: oligopoly in power and cooling, industrial multiples. **Arista:** a franchise in AI back-end networking, but NVIDIA and Broadcom compete |

**Answer to your point:** the claim holds for Microsoft and Google, and for Amazon in infrastructure. It is
only partly true for the labs. It is true for Meta in advertising and false for Meta's AI capex. It is
false for Oracle. The equity market already ranks the names this way on CY27 earnings: Microsoft 24.3×,
Amazon 24.4×, Alphabet 19.2×, **Meta 17.9×, Oracle 11.7×**. The baseline does not: its E layer uses one
exit P/E (17 / 21 / 23.5) for all five.

## 3. Do we trust that income grows fast enough?

- **Near term: yes, and ahead of the rows.** The four clouds grew ~+59% in Q3 against capex up ~84%
  in 2026 (K1). The 2026 cloud growth is ~+53% against the row's +50%. OpenAI's run-rate grew +77% in
  Q3. Lab revenue 2026 ~94–100bn. Backlog ~2,480bn (+3% q/q).
- **Payback: no, inside the window, in any scenario** `[A]`:
  - K1 2025–29 at Base is **USD 4,895bn** (435 + 790 + 1,120 + 1,250 + 1,300).
  - With 70% short-lived assets (6 years) and 30% long-lived (25 years), earning **8–12%** over the
    asset lives needs **USD 880–1,020bn** of annual cash earnings (820–1,170bn across 60–75% short-lived
    and 5–6 year lives), or revenue of ~USD 1.3–1.9tn at a 55–65% cash margin.
  - Base 2029 delivers incremental four-cloud revenue of ~USD 605bn over 2025 (891 against 286),
    which is **330–390bn** of cash earnings: **~33–45%** of the requirement.
  - Revenue outside the clouds (Meta's ad uplift, Copilot and Gemini seats) is not quantified `[?]`,
    and some K1 spend is non-AI. Treat it as an order of magnitude: the answer is "a third to a half",
    not a tenth and not 100%.
  - Lab revenue 2026–29 (919bn) is **21%** of K1 2026–29 (4,460bn).
- **Whose income is it?** At least **~USD 725bn (29%) of the 2,480bn backlog is two labs** `[A]`
  (AWS 248 = OpenAI 138 + Anthropic ≥ 110; Oracle > 332, more than half of 664; Google ≥ 114.5;
  Microsoft ~31). It is a lower bound: Microsoft's OpenAI share is not given. These are the contracts
  the labs fund with raises, so growth in 2028–29 rests on the Anthropic IPO and the OpenAI raises.
- **NVIDIA's weak-tier exposure:** the "AI Clouds, Industrial and Enterprise" platform was USD 40.3bn of
  Q2 FY27 (+138% y/y), against 48.7bn for hyperscale: **~45% of the two** `[F]`. It includes sovereign
  and industrial buyers, not only neoclouds. DSO rose 45 → 60 days, and NVIDIA guarantees 105bn and
  holds 25bn of committed equity. NVIDIA's own balance sheet is part of the financing of this tier.

## 4. Does the financing support K1?

| USD bn `[A]` | 2026 | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| K1 Base capex | 790 | 1,120 | 1,250 | 1,300 |
| Operating cash flow, five (Q3-26 ~199 a quarter; growth +17% / +11% / +8%) | ~770 | ~900 | ~1,000 | ~1,080 |
| Capex ÷ OCF | 103% | 124% | 125% | 120% |
| Gap, plus ~72bn of dividends and buybacks | 92 | **~290** | **~320** | **~290** |

- **External capital already raised by the five in nine months of 2026: ~USD 352bn** (annualised
  ~470bn): Amazon ~115 of debt (67% of cash capex), Alphabet ~80 of notes and 62 of equity (49.6 in June,
  12.4 ATM), Meta ~25, Oracle ~70 (debt and equity), Microsoft ~0 `[A]`. Debt alone is **~45% of the
  five's capex** (mixed periods, ±5 pp).
- **Reading:** the 2027 Base needs ~290bn, less than the 2026 pace. The funding gap is **not**
  the binding constraint for the high-grade four; price is. Each 5 pp of lower OCF growth adds ~40bn
  of need.
- **Elasticity by tier** (2026 shares of K1: Microsoft 21.5%, Alphabet 25.3%, Amazon 27.8%, **Meta 17.7%,
  Oracle 7.6%**): Oracle −30% and Meta −15% together is **−55bn in 2027 and −62bn in 2028, −4.9% of K1**.
  Oracle's own guide (capex peaks FY27–28, steps down in FY29) makes part of the Oracle cut likely in 2029 regardless.
- **Bottom-up check on 2027:** S&P Global's model (undated, may predate Q3 `[E]`) gives Alphabet 357,
  Amazon 319, Microsoft 189, Meta 164, which with Oracle at ~100 (calendar 2027 from FY27 90–95 and
  FY28 `[A]`) sums to ~1,130, against K1 1,120. Street ~1,100, Goldman and Morgan Stanley 1,200.
  **K1 2027 is inside the range.** Alphabet's 2027 consensus (~300–312) is above its analysis (275), an
  upside skew of ~25–37bn.
- **Gap in the baseline:** K1 is an input to the Microsoft, Alphabet and Amazon analyses (they take its
  shares), so they cannot test it, and Meta and Oracle have no analysis (the "E rest" row is the old
  layer path). **No independent per-company build of K1 2028–29 exists.** That is the main weakness
  this review finds.

## 5. Model tests (NOK, Base, 5 Nov prices; none applied)

**A. Standard-industry exit multiple.** Base IRR if every layer exits at World's 17× (memory left out:
cycle-first rule).

| Layer | P/E CY27 now | Base, layer's own exit | Base at 17× | Exit P/E needed for 12% |
|---|---|---|---|---|
| H1 Compute | 13.5 | 11.7% (17×) | 11.7% | 17.1 |
| H3 Foundry and equipment | 16.6 | 11.7% (18×) | 9.9% | 18.2 |
| **H4 Networking and DC infrastructure** | 24.0 | 1.3% (20×) | −3.3% | **28.3** |
| **E Platforms** | 21.1 | 8.0% (21×) | **0.9%** | **23.5** |
| T Software | 23.7 | 3.4% (20×) | −1.4% | 26.2 |

- **Compute and foundry are already priced at or below a standard multiple** after the 5 Nov sell-off.
  They are at their hurdle on Base (margin of safety −0.7% and −0.8%), so the price assumes Base K1 and
  holds no cushion for a cut.
- **H4** at exit 15 / 20 / 24 (now) +1.3%; 13 / 17 / 20 −3.3%; 12 / 16 / 19 **−4.9%**; 11 / 14 / 17 −8.4%.
  The price implies **1.38×** Base 2028–30 earnings at a 20× exit and 1.69× at 16×. Per name: Arista 30.8×,
  Vertiv 18.3×, Eaton 20.2× (Schneider 18.1×, Yahoo forward).
- **Platforms rest on the market-power premium.** The E layer needs 23.5×. Microsoft uses 23 in its own
  analysis.
- **Data-centre owners and neoclouds (5 Nov)** `[F]` Yahoo: CoreWeave USD 24.2bn market value against
  over 51bn of debt; Nebius 30.8bn; IREN 7.5bn; Applied Digital 4.4bn; all with negative forward EPS, so P/E
  does not apply. Equinix 48× and Digital Realty 58× forward P/E are GAAP-based; **price to FFO, the right
  yardstick, was not fetched `[?]`**. I make no call on them.

**B. Meta and Oracle without a market-power premium.** Per name on the layer method (company-blend Base
paths of 1 Nov for the three analysed; the old "E rest" path for Meta and Oracle).

| Name | P/E CY27 | Base IRR (own path, exit 21) | Multiplier on Base 2028–30 for 12%, exit 21 / 17 / 15 |
|---|---|---|---|
| Microsoft | 24.3 | 4.7% | 1.23 / 1.51 / 1.70 |
| Alphabet | 19.2 | 7.8% | 1.12 / 1.39 / 1.58 |
| Amazon | 24.4 | 3.3% | 1.28 / 1.58 / 1.79 |
| **Meta** | 17.9 | 13.0% | **0.97 / 1.20 / 1.36** |
| **Oracle** | 11.7 | 29.1% | **0.65 / 0.81 / 0.92** |

- **Oracle is already priced with no market power:** its price fits the rest-row Base only at 0.65× of
  its 2028–30 earnings at a 21× exit, or 0.92× at 15×. The 29% is the old layer path applied to a 11.7×
  stock, not an Oracle forecast.
- **Meta is the name that still carries the premium:** at 21× it needs 0.97× Base, at a standard 17×
  exit it needs 1.20×.
- **Effect on the E basket** (cap weights Meta 12.7%, Oracle 2.9%; E now 7.1% per name, 8.0% on the layer
  path):

| Variant for Meta and Oracle | E basket | Change | All six (E = 47%) |
|---|---|---|---|
| Base EPS, exit 17× | 5.8% | −1.2 pp | −0.6 pp |
| E-rest Bear EPS, exit 17× | 4.8% | −2.2 pp | −1.1 pp |
| E-rest Bear EPS, exit 15× | 4.2% | −2.9 pp | −1.4 pp |

  These move the layer's exit multiple by less than 1 turn (17% of the layer) and no EPS path by 0.05,
  so by the rules nothing is applied. It is the size of the tiering effect if the E layer is split.

**C. A K1 cut flowing through** (partial move from the Base to the Bear EPS path 2028–30, in proportion to
the K1 cut against the Bear K1 of 800 / 820; exit multiples at Base; memory at half strength because of
its LTAs `[A]`). **E is shown as "cut with revenue disappointment"**: a discretionary cut with revenue on
Base would help the spenders' cash flow, not hurt it.

| K1 2028 / 2029 | H1 | H3 | H4 | E | All six |
|---|---|---|---|---|---|
| Base 1,250 / 1,300 | 11.7% | 11.7% | 1.3% | 8.0% | 10.1% |
| −5% (1,188 / 1,235) | 9.7% | 9.8% | −0.6% | 6.6% | 8.6% |
| **−10% (1,125 / 1,170)** | 7.6% | 7.9% | −2.5% | 5.2% | **7.1%** |
| −20% (1,000 / 1,040) | 3.2% | 3.7% | −6.5% | 2.3% | 3.9% |
| Bear (800 / 820) | −5.4% | −4.2% | −14.4% | −3.1% | −2.1% |

Each 5% off K1 2028–29 costs compute, foundry and networking **~2 pp a year** of Base IRR. A 10% cut would
take the six from 10.1% to about 7.1%, still above World (5.2%).

## 6. Verdicts

| Question | Verdict | Basis |
|---|---|---|
| Price data-centre names like industry? | **Yes for owners, lessors and neoclouds; the market has largely done it.** Decision-neutral for the baskets | VRT, ETN 18–20×; H4 −4.9% at 16×; CoreWeave 15.8% debt |
| Should we do the same as the bond market? | **Partly.** Read the weak tier as the early warning; do not change k or EPS for the four high-grade names | 35–50 bp on ~300bn ≈ 1.5bn a year; Oracle 7.3% debt vs k 12%; neocloud k ≥ 20% |
| Do we trust income? | **Near term yes; payback no inside the window** | Q3 clouds +59%; Base 2029 covers ~33–45% `[A]`; 29% of backlog is two labs |
| Spending estimates come down? | **2027 no. 2028–29: not as Base; risk skewed down** | K1 2027 ≈ Street; −4.9% from Oracle and Meta; funding need ~290bn is below the 2026 pace |
| Does Meta have market power? | **In ads, not in AI compute.** Highest capex elasticity | No third-party contracts; FCF ≈ 0; Class C stock; CDS record |
| Does Oracle? | **No.** Priced that way (11.7×, CDS 292 bp) | Contracts are the asset, one lab, funding cap used up |
| Lower K1? | **No.** Below the 5% rule; Bear-side event | Section 4 |

**What would make me lower K1 2028–29** (my proposed rule: any two together, then re-test at −10%, six baskets ~7%):
1. The Anthropic IPO pulled or priced below the USD 965bn Series H, or an OpenAI raise failing
   (~20 Nov and after);
2. an aggregate 2027 capex guide below ~USD 1,000bn (−10%) in late Jan–early Feb;
3. lab run-rates below +10% q/q for two quarters;
4. Oracle cut to BB+, or its RPO falling at Q2 FY27 (~10 Dec);
5. AWS backlog down q/q (Q4, early Feb).

**Signposts re-read (in `docs/ai-market-bbb.md`):**
- **Neocloud funding: now crossed.** CoreWeave's CDS (~1,038 bp, 15 Oct) is the credit leg that was not
  measured, and the equity made a new low on 5 Nov. The credit reading is three weeks old.
- **Capex ÷ OCF and debt share: now crossed on both legs** (~116% and ~45% `[A]`).
- Platform equity funding: crossed since 29 Oct, and Oracle's USD 10bn of stock (2 Nov) and Meta's Class C
  add to it.
- Oracle credit: BB+ not reached, but the CDS is at BB/B-like levels.
- **A financing break needs more than these:** a lab missing commitments, a hyperscaler guiding capex
  flat or down, Oracle at BB+, or a called guarantee. None has happened. Vendor-financing flow: no new
  commitment found since 29 Oct.

## 7. Method additions (proposed in this review, applied to the skill on the user's go-ahead, 5 Nov, revision 2026-11-05.1)

1. **Tier the E layer** (A: Microsoft, Alphabet, Amazon; B: Meta; C: Oracle) with an exit P/E per tier.
   This needs Meta and Oracle analyses; the "E rest" row is the old layer path.
2. **Credit-by-tier rows in K3:** CDS, spreads, order-book cover, SPV pricing and loan syndication, each
   with a dated threshold (signposts table; `references/credit_tests.py`).
3. **An independent per-company K1 build** for 2027–29 (K1 now feeds the three analyses and cannot be
   tested by them).
4. **The payback arithmetic as a standing check** in Step 3 (required cash earnings against the Base; `references/payback.py`).

## 8. Dated signposts

| Date | Event | What it tests |
|---|---|---|
| 17 Nov | NVIDIA Q3 FY27 | Q4 guide; "AI Clouds, Industrial and Enterprise" growth against +138%; DSO; supply commitments |
| ~16–20 Nov | Anthropic IPO (week of 16 Nov, pricing ~20 Nov) | Lab financing: price against 965bn |
| ~10 Dec | Oracle Q2 FY27; ERCOT audit | RPO, capex, FCF path, rating; Texas siting |
| 3 Jan, 11–19 Jan | New Congress; governors | Siting law (K1 2028) |
| late Jan–early Feb | First 2027 capex figures (Alphabet, Amazon, Meta, Microsoft) | K1 2027 against the −10% line (1,000), Base (1,120) and Bull (1,300) |
| Weekly | Oracle 5y CDS (> 350 bp or < 200), CoreWeave 2031 yield (> 16% or < 11%), hyperscaler order-book cover (< 1.5× or > 3×), the USD 38bn Oracle-leased construction loan | Credit by tier |

## Sources and limits

- **Read:** CNBC 15 Oct (CoreWeave CDS), 19 Oct and 2 Nov (Oracle); investinglive 15 Oct (CoreWeave bond,
  S&P B+); IBTimes 29 Jul (Meta El Paso); Startup Fortune 11 Oct (syndication, order books, CCIR); Penn
  Mutual 6 Aug; aiweekly 28 Jul (CDS records, NVIDIA 79 bp); Finimize (Meta CDS 114.79 bp, undated);
  Spinel Capital (Oracle, author's view not used); Oracle investor-day facts via a search excerpt of the
  company release (28 Oct); the baseline and the company analyses.
- **Not read:** Bloomberg (403) and Reuters directly; the Goldman Sachs AM piece and the S&P Global
  capex model (search snippets, undated). Meta's Q3 call transcript (2027 capex) was not found.
  Aggregator sites disagree on dates and levels; every level here is `[E]` unless marked.
- **Not done:** no company analysis of Meta or Oracle; no P/FFO for Equinix and Digital Realty; no
  independent K1 build. The payback arithmetic and the funding table are `[A]` orders of magnitude.
