# Anthropic, PBC (ANT) — IAF analysis after the IPO, stub 20 Nov–Dec 2026 + 2027–2029

**Version 1.1 — 20 Nov 2026** · price **$97.17** (Nasdaq first close 19 Nov; IPO priced at **$83.00** on 18 Nov, above the $70–78 range) · skills: iaf-valuation **2026-11-18.1**; inputs AI BBB 18 Nov (E1 paths of 11 Nov), Equity BBB 18 Nov note (values of 6 Nov), HY BBB 18 Nov · **verdict: fails** (Base margin of safety −39.4% at $97.17; −29.0% at the $83 IPO price).

**Author's note:** written by Claude, an Anthropic model, so this is an analysis of the author's maker. It applies the same method and sources as for any other company, every number is tagged [F] (prospectus, filing or market print), [E] (third-party estimate), [A] (own assumption) or [C] (carried from a workspace document), and neither the Bear case nor the verdict is softened.

## Summary

**Verdict**
- **Fails. Base IRR −4.6% a year at the first close of $97.17 (NOK 946) against k = 12%; P_k $58.9 (NOK 574); margin of safety −39.4%.** For an IPO allocant at $83: 0.3% a year, margin −29.0%. The +2% "clears" band starts at **$57.8**, about the Series H price per common share ($58.90, May–June 2026) [C].
- **Base does not preserve capital at $97.17:** V_T $83.9 (−13.7%). The buyer pays **30x Base 2030 normalised after-tax operating profit today** (EV $1,533bn fully diluted, 13.9x Base 2027 revenue). Base reaches k only with an exit P/E of **47** (Base 26), or a normalised EBIT margin of **47%** (Base 25%), or revenue above the whole AI BBB lab market: **101% of E1** in 2029 ($363bn instead of $209bn). Bull revenue with Base costs and multiple gives 10.1%.
- **Bear (AI BBB financing break): −42.1% a year, capital not preserved (−82%).** The company survives (net cash ≥ $178bn), the equity does not: ~$67bn of cash burn in 2027–29 against committed compute, and $55bn of commitments above need after 2029.
- **Bull (agentic adoption): +21.1% a year;** the price already reflects 59% of the way from Base to Bull.

**Base in brief**
- Revenue on the AI BBB E1 Base path at a constant **58% share** (Anthropic's share of E1 in 2026): $110 / 160 / 209bn in 2027–29 (2026: $54.7bn; Run-Rate Revenue ~$81bn at 31 Oct [F]). Compute follows the contracts, not revenue: $77 / 115 / 135bn (70% / 72% / 65% of revenue), so the adjusted operating margin falls to 5% in 2027–28 before recovering to 14% in 2029 (9M-2026: 12%).
- Exit: 26x normalised 2030 NOPAT (revenue $255bn, EBIT 25% after SBC, 21% tax) plus net cash $270bn, less a $7bn commitment overhang; **V_T $83.9** on 18.73bn exit shares.
- **Where the return comes from (per share):** earnings growth +$109.9, multiple 70.4x → 26x −$122.2, dilution −$1.7, overhang −$0.4, cash +$1.0: $97.17 → $83.9. The business case for the compute is good (ROIC_g 27% > k); the market price capitalises more than all of it.

**Bear in brief**
- Story: the AI BBB financing break inside the equity Bear (earliest H1 2027): lab revenue stalls (E1 155 / 170 / 187), enterprise and VC-funded coding customers cut spend, prices fall. Anthropic keeps 55% of E1: $85 / 94 / 103bn, flat on the Q4-26 run-rate.
- Worst years 2028–29: compute ~105% of revenue even after conditional contracts lapse and SpaceXAI is cancelled (Google and Amazon true-ups bind); adjusted operating margin about −30%.
- Capital not preserved: V_T $17.7 (−82%). Net cash bottoms at $178bn at exit; the $5bn liquidity covenant is never near; no new equity needed. Damage: the revenue path with fixed commitments (−4.6% → −30.6%), then the normalised margin and the exit P/E (→ −44.5%).

**Decision table (USD per Class A share; P = $97.17 first close; fully diluted 18,292m shares)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (USD) / NOK path (Equity BBB) | −42.1% / −40.5% | **−4.6% / −4.6%** | 21.1% / 20.0% |
| V_T (31 Dec 2029) | 17.7 | **83.9** | 176.6 |
| **P_k / margin of safety** | 12.4 / −87.2% | **58.9 / −39.4%** | 124.1 / +27.7% |
| P_k in NOK (USD/NOK 9.7391) | 121 | **574** | 1,208 |
| Capital preserved? (V_T vs P; no dividends) | No, −81.8% | **No, −13.7%** | Yes, +81.8% |
| Cumulative FCF per share 2027–29 | −3.68 | **1.31** | 4.05 |
| Net cash per share at exit | 9.45 | **14.41** | 16.77 |
| Balance sheet | Burns ~$67bn 2027–29; net cash $178bn at exit | Net cash $270bn | Net cash $320bn |

**Entry prices** (the deal fixes shares and cash; NOK at USD/NOK 9.7391)

| Entry price | $83.00 IPO (NOK 808) | **$97.17 first close (NOK 946)** | $111.50 first-day open (NOK 1,086) |
|---|---|---|---|
| Fully diluted shares / market cap / EV | 18,283m / $1,517bn / $1,273bn | **18,292m / $1,777bn / $1,533bn** | 18,299m / $2,040bn / $1,796bn |
| Market cap on issued shares (13,396m) | $1,112bn | **$1,302bn** | $1,494bn |
| Base IRR / P_k / margin of safety | 0.3% / 58.9 / −29.0% | **−4.6% / 58.9 / −39.4%** | −8.7% / 58.9 / −47.2% |
| Bear / Bull IRR (USD) | −39.1% / 27.4% | −42.1% / 21.1% | −44.6% / 15.9% |
| Bear / Bull IRR, NOK path | −37.4% / 26.2% | −40.5% / 20.0% | −43.0% / 14.8% |
| Exit P/E for k (Base) / E1 share for k | 38.7 / 83% | 47.2 / 101% | 54.9 / 117% |

**Per-share path** (Track A with explicit compute; $bn and $ per fully diluted share at $97.17; V_t is a diagnostic mark)

| | Q4-26 (stub) | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Base revenue / compute ($bn; % of revenue) | 21.5 / 13.0 (60%) | 110.2 / 77 (70%) | 159.5 / 115 (72%) | 208.8 / 135 (65%) |
| Base adjusted operating income $bn (margin) | 3.0 (14%) | 5.7 (5%) | 7.8 (5%) | 30.0 (14%) |
| Base FCF $bn / per share | 1.3 / 0.07 | −4.5 / −0.25 | 0.6 / 0.03 | 27.9 / 1.53 |
| Base net cash $bn / per share | 245.9 / 13.44 | 241.3 / 13.19 | 241.9 / 13.23 | 269.9 / 14.75 |
| Base core EPS (normalised SBC, 21% tax, ex interest) | — | 0.05 | 0.06 | 0.93 |
| Base V_t | 97.2 | 106.0 | 102.0 | 83.9 |
| Bear FCF per share / V_t | 0.07 / 97.2 | −1.04 / 42.1 | −1.39 / 30.9 | −1.26 / 17.7 |
| Bull FCF per share / V_t | 0.07 / 97.2 | −0.21 / 182.6 | 0.68 / 192.1 | 3.58 / 176.6 |

Tags: `[F]` prospectus, filing or market print · `[E]` third-party estimate · `[C]` carried from a workspace document · `[A]` own assumption · `[?]` not found. Bafin prospectus page numbers are printed pages (PDF page − 10).

## Header

| Item | Value |
|---|---|
| Company | Anthropic, PBC (Delaware public benefit corporation), San Francisco. Class A common stock, Nasdaq Global Select "ANT", CUSIP 03703U107, ISIN US03703U1079 [F] |
| Price | **$97.17**, Nasdaq close 19 Nov 2026, first trading day (open $111.50, high $115.10, low $92.72, 853m shares) [F] (Yahoo, Nasdaq real-time); post-market $92.60 (20 Nov 00:59 UTC). IPO price **$83.00** (priced 18 Nov, above the $70–78 range) [F] (pricing FWP, 424B4). One trading day old: today's session not yet open |
| Valuation date / exit / T | **20 Nov 2026** (closing of the offering and settlement of the placement) / 31 Dec 2029 / **3.115 years** |
| Shares | Issued after the deal (incl. the option, Public Benefit Fund and post-September issuance) **13,396m**; **fully diluted 18,292m** at $97.17 (bridge in Common assumptions) |
| Market cap / EV at $97.17 | $1,302bn issued; **$1,777bn fully diluted**; net cash at closing **$244.6bn**; EV **$1,533bn** = 28.0x 2026 revenue, 22.6x Q3-26 annualised, 18.9x Run-Rate Revenue (31 Oct), 13.9x Base 2027. Press figures ($1.27–1.8tn) mix share bases; Yahoo's $1,272bn uses the pre-upsizing 13,087m |
| NAV | Not used (Track A): an AI lab has no asset-market NAV. Net tangible book after the deal $128.2bn, **$9.70 per share** ($10.50 with the option) [F] |
| FX | USD price. USD/NOK **9.7391** (Yahoo, 07:24 UTC 20 Nov) [F]; AllRatesToday 9.7398 (20 Nov); Norges Bank fixing 9.6866 (19 Nov, 14:15 CET; the gap is the afternoon's move). NOK 946 for $97.17, 808 for $83, before broker FX fees. NOK path for Bear and Bull from the Equity BBB |
| Track | **A with explicit compute and capex**: value at exit is a going-concern multiple on earnings, but compute commitments drive cash flow, so the build is year by year as in Track B |
| k | **12%**, not raised: no debt beyond $5.6bn of Amazon notes settled in shares, deep liquidity (853m shares traded on day one). Governance, concentration and commitments are in Bear and Risks, not in k |
| Dividends | None; the company intends to retain all earnings and the credit agreement limits payouts (p. 291) [F]. D_t = 0 in all scenarios |
| Primary sources | **Final prospectus 424B4** (EDGAR, filed 19 Nov 2026, dated 18 Nov) and the pricing FWP (18 Nov) for the deal, share count and cash [F]; EU retail prospectus approved by Bafin 11 Nov 2026 for the business, financials and commitments (the 424B4 repeats the items used) [F] |
| Inputs read | `docs/ai-market-bbb.md` **18 Nov 2026** (Interface: E1 paths and E-layer exit P/E of 11 Nov, turn calls 18–19 Nov, lab-financing signpost); `docs/equity-market-bbb.md` **18 Nov note** (World exit P/E and P/B, mid-cycle return, USD/NOK path: values of 6 Nov); `docs/hy-market-bbb.md` **18 Nov** (rates context; SOFR 3.94% via Equity BBB). Cross-checks only: `amzn` (11 Nov), `googl` (11 Nov), `nvda` v1.9 (19 Nov), `msft` |
| Stale after | **15 Dec 2026** (quiet period ends ~14 Dec, first staged lock-up release 15 Dec) |

## Scenarios

| | Bear | **Base** | Bull |
|---|---|---|---|
| Story and catalyst | AI BBB **financing break** in the equity Bear: a lab short of its commitments, neocloud contracts renegotiated, AI credit tightens, price war. Earliest H1 2027 | AI BBB Base: contracted 2027 build, then a K1 digestion plateau; lab revenue ~3.6x by 2029 | AI BBB **agentic adoption**: lab revenue +130% in 2027. Earliest Q2 2027 |
| AI BBB rows | E1 155 / 170 / 187 | **E1 190 / 275 / 360** | E1 230 / 370 / 515 |
| Company driver: share of E1 / revenue 2027–29 (2030) | 55% / $85 / 94 / 103bn ($111bn) | **58% / $110 / 160 / 209bn ($255bn)** | 62% / $143 / 229 / 319bn ($415bn) |
| Compute $bn (% of revenue) | 75 / 100 / 108 (88 / 107 / 105%) | **77 / 115 / 135 (70 / 72 / 65%)** | 92 / 145 / 172 (65 / 63 / 54%) |
| Adjusted operating margin 2027–29 | −14% / −32% / −29% | **5% / 5% / 14%** | 11% / 15% / 26% |
| Normalised 2030: compute / other cash opex / SBC → EBIT | 58 / 21 / 5% → 16% | **52 / 19 / 4% → 25%** | 48 / 18 / 3% → 31% |
| Exit P/E (EV ÷ 2030 NOPAT) | 15 | **26** | 30 |
| Company items | Overhang PV $55bn (firm contracts to 2033, 50% resale); capex 15 / 6 / 4 | **Overhang $7bn; capex 20 / 20 / 15** | No overhang; capex 30 / 35 / 30; PBF +2% once ($124.50) |
| Macro and NOK | Equity Bear; USD/NOK +12% / +9% / +9%; cash yield 3.0% | Equity Base; NOK flat; 3.75% | Equity Bull; NOK −3%; 3.75% |
| Result at $97.17: IRR / P_k / capital | −42.1% / $12.4 / −82% | **−4.6% / $58.9 / −14%** | 21.1% / $124.1 / +82% |

**Driver breakdown** (one driver at a time from Base, IRR at $97.17)

| Step | Base → Bear | Base → Bull |
|---|---|---|
| Base | −4.6% | −4.6% |
| Revenue: E1 path × own share (window compute held at the contracts) | −30.6% | 9.7% |
| + window costs (compute lapses or extra capacity, opex, capex, cash yield) | −28.4% | 9.3% |
| + normalised 2030 margin | −36.3% | 16.2% |
| + exit P/E (15 / 30) | −44.5% | 21.1% |
| + overhang terms (full term, resale, no tax shield / none) | −42.1% | 21.1% |

Bear: the fixed commitments do the damage once revenue stalls; the lapses and resale help (+2.2 pp, +2.4 pp). Bull: revenue alone takes Base to 9.7%; Base costs and multiple on the Bull revenue give 10.1%, still below k.

**Base return bridge (USD per share, $97.17 → V_T $83.9):** entry = EV $83.80 + net cash $13.37. Earnings growth (normalised NOPAT $21.8bn on 2027 revenue → $50.3bn in 2030, at the entry multiple 70.4x) **+$109.9**; multiple 70.4x → 26x **−$122.2**; commitment overhang −$0.4; dilution after the IPO −$1.7; cash +$1.0. The entry multiple (70.4x Base 2027 normalised NOPAT) is a 2027 growth multiple that 2030 growth (+22%) no longer carries: the earnings growth is real but more than paid for.

## Company and status

**Business (p. 151–161) [F].** Frontier lab selling Claude through its API platform (pay-per-token), first-party applications (Claude Code, Cowork, vertical products) and the three big clouds (AWS, GCP, Azure). Revenue $41m (2023), $386m (2024), $4,585m (2025); 9M-2026 **$33,242m**; quarters Q1–Q3 2026 **$4,731m / $11,555m / $16,956m** (+47% q/q in Q3, with ~$600m of price cuts). **Run-Rate Revenue ~$81bn at 31 Oct 2026, +$10bn from 30 Sep** (424B4 p. 203; a 28-day annualisation, not a forecast).
- **Mix (9M-26):** consumption $26.3bn (79%), subscriptions $6.9bn (21%); CSP marketplaces billed **44%** of revenue and 52% of receivables. **Top five customers 25% of 9M revenue** (21% of Q3; 36% of Q1); none above 10%. 11,900+ customers at ≥ $100k TTM (74% of revenue), 1,900+ at ≥ $1m, ~250 at ≥ $10m; net revenue retention ~900% (p. 29, 153, 159–160).
- **Revenue quality:** 5–7% of 9M revenue came from customers later found to breach usage terms; enforcement was stepped up in Aug–Sep (p. 161). Model versions under six months old were > 80% of Q3 revenue (p. 160).
- **Costs (9M-26, % of revenue):** compute and infrastructure $18.8bn (57%; Q3 58%, incl. **$5.0bn of short-term compute** at a premium), personnel $4.9bn (15%, of which SBC $3.3bn), sales, marketing and partnerships $5.5bn (17%, mostly channel fees), other $5.3bn (16%, incl. $2.1bn of non-cash donation matching) (p. 164–167).
- **Margins:** operating loss $(1,260)m; Q2 +$974m, Q3 $(567)m. Adjusted operating income $4,081m (12%); Q2 19%, Q3 15%. Revenue per dollar of compute 0.40x (Q1-25) → 2.08x (Q2-26) → **1.72x (Q3-26)** (p. 154, 175–178).
- **GAAP net loss $(104.0)bn** in 9M-26 is $94.3bn of fair-value changes on notes, derivatives and SAFEs plus $10.4bn on partner financing arrangements: valuation marks, not operations. Cash flow 9M-26: operating **+$6.6bn**, investing $(36.5)bn (mostly short-term investments; capex and prepayments about $3–6bn derived [A]), financing +$110.7bn (p. S-3, 188–189). The IPO adds a $14.7bn RSU modification charge and $3.7bn for the post-September grants (non-cash; 424B4).

**Compute commitments (p. 155, 190–192; repeated in the 424B4) [F]:** **$900.9bn** in total (contract table $320.0bn, short-term $17.4bn, leases not yet commenced $451.2bn, post-September $105.7bn and $6.6bn), of which **$451.6bn before end-2030**, **$70.7bn in the 12 months to Sep 2027**, and **$186.2bn subject to termination rights or counterparty conditions**. Plus **$150–175bn** without a fixed dollar amount (additional Google TPU $125–150bn delivered 2028–31; AMD Helios > $20bn from 2027).

| Counterparty | Commitment | Term | Can it be cut? |
|---|---|---|---|
| Google (CSP hosting, TPU) | ≥ $121.3bn | Apr 2026–Jul 2033 | No; shortfall paid as a true-up |
| Amazon (AWS, Trainium) | ≥ $110.0bn | May 2026–Apr 2036 | No; true-up |
| Broadcom (five-year TPU equipment leases, finance leases) | ~$161.2bn rent | From 2026–27 | No; cash deposit, cross-defaults |
| SpaceXAI (NVIDIA GPUs) | Up to $120.5bn; ~$3.1bn a month at full capacity (Dec 2026) | Into 2029 | Yes: 90 days' notice after Jan / Mar 2027 |
| Microsoft (Azure) | $47.2–49.2bn | Nov 2026–Jun 2033 | No, except undelivered tranches |
| Nscale / Lambda (NVIDIA GPUs) | Up to $44.6bn / $41.3bn | To 2033 / 2034 | Nscale contingent on its financing; Lambda's $34.9bn now terminable |
| Contract table by year (purchase commitments, leases) | 2026 $5.2bn · 2027 $29.2bn · 2028 $44.4bn · 2029 $47.8bn · 2030 $45.1bn · later $148.4bn | | |

The schedule used here (contracts plus commenced and pending leases plus the variable TPU and AMD capacity, spread on their stated terms) is **~$77 / 125 / 147 / 155bn in 2027–30**, then falling (135 / 120 / 100bn in 2031–33) [A]. It is the key uncertainty in the model (±15% is a sensitivity).

**Funding (p. 155, 180–185; 424B4 p. 144) [F]:** cash and short-term investments $131.8bn at 30 Sep ($95.6bn cash, $36.3bn short-term investments); A&R credit facility to 2031 with $14.8bn available (liquidity covenant ≥ $5bn from Q4-26). Partner capacity $77.0bn under the NPAs, less $10.0bn when the Google placement closes; AMD equity $5.0bn, less $2.5bn. Google NPA (draws settled at the 30-day VWAP; requests to Dec 2030), Amazon NPA $15bn (VWAP shares, compute milestones, to May 2029), Broadcom NPA **$42bn** to finance lease rent (9% PIK, converts at 90% of VWAP; **13% and 85% if revenue conditions fail**). Amazon's notes (1,840.4m shares in all) convert only up to a 12% ownership cap that Amazon did not waive: **$612.7m (292.8m Class N) converted at the IPO; 1,547.7m shares roll over** and convert quarterly as the cap allows, or are repaid in 2034–35.

**The offer (424B4, FWP) [F]:** **956.35m new Class A + 23.65m sold by the seven co-founders (3.38m each) at $83.00** (upsized); option **147.0m, all primary, no underwriting discount on option shares**; underwriters pay $82.43878 per base share (spread 0.68%). Base offering $81.34bn gross ($79.38bn primary). **Concurrent Class N placement $26.0bn = 313.25m shares at $83**, closing immediately after the offering subject to conditions: Google 120.48m ($10.0bn), **NVIDIA 120.48m ($10.0bn)**, AMD 30.12m ($2.5bn), Broadcom, Micron and Microsoft 12.05m each ($1.0bn), TSMC 6.02m ($0.5bn). **Net proceeds $104.8bn incl. the placement ($117.0bn with the option)**; $4.28bn of it settles RSU tax withholding (51.6m shares withheld). Directors' indications up to $305m. Pricing 18 Nov, first trade 19 Nov, settlement 20 Nov.

**Governance (p. S-1–S-2, S-4–S-5, 160–161, 255–257) [F]:**
- **Long-Term Benefit Trust** (five financially disinterested trustees) holds Class T and elects a **board majority**; **Founder LLC** (the seven co-founders) holds one Class F share with **50.1% of the votes** on all ordinary matters. Class A votes are capped at 49.9% in total, so **Class A holders cannot decide any vote**. Nasdaq "controlled company".
- **PBC duty:** the board must balance stockholders' pecuniary interests against the public-benefit purpose. Public-benefit spending (donation matching $2.1bn in 9M-26) is expected to rise.
- **Anthropic Public Benefit Fund** holds 846.8m Class N (6.3% of the shares after the deal), may sell or donate them; the board may add **2% of outstanding shares each time the price rises 50%** from the IPO price ($124.50, $186.75; 90 of 120 trading days). Donation matching: 553.4m shares owed on vested-award pledges, reserve +1% a year 2027–36. Co-founders pledge 80% of their equity to philanthropy.
- **Holders after the deal (424B4) [F]:** Amazon 1,936.5m Class N (14.6% of the capital; 3,484.1m and 23.6% with the notes fully converted), Google 1,775.0m (13.4%).

**Lock-ups (424B4 p. 22, Shares Eligible for Future Sale) [F]:** holders of ~15.5bn shares are locked; employees and non-founder directors may sell 10% from day one; other holders release in steps from day 27 (15 Dec 2026), 48 (5 Jan 2027), 62 (19 Jan), 76 (2 Feb) and after the FY26 and Q1-27 results; general expiry at the Q1-27 results or day 180 (**17 May 2027**); **up to 3.7bn shares can trade before then**. Holders above 0.5% and the co-founders are locked to the Q3-27 results or day 365 (**18 Nov 2027**), with staged releases (founders 29% from day 180). The $26bn placement is **not locked up** (restricted, with registration rights).

## Near term: stub (all scenarios)

| Q4-26E [A] | Revenue | Compute (%) | Other cash opex | Adj. operating income | Interest | Capex | FCF |
|---|---|---|---|---|---|---|---|
| $bn | 21.5 (+27% q/q) | 13.0 (60%) | 5.5 (26%) | 3.0 (14%) | 1.5 | 3.0 | **+1.3** |

- 2026 revenue **$54.7bn** (AI BBB build ~55, Q4 21.7: −1%); 2026 compute ~$31.8bn. Q4 at $21.5bn (= $86bn annualised) fits Run-Rate Revenue of $81bn at 31 Oct with November growth and the late-December code-freeze dip (−20% in two weeks last year, p. 160), enforcement and price cuts.
- **Net cash bridge:** cash and short-term investments 30 Sep $131.8bn + net proceeds $104.8bn (offering $78.8bn + placement $26.0bn) − RSU withholding $4.3bn = **$232.4bn pro forma as adjusted** [F] + option 147.0m × $83 with no discount $12.2bn [A: exercised] = **$244.6bn at closing** ($13.37 per share) + Q4 FCF $1.3bn = **$245.9bn at 31 Dec** ($13.44).
- **Dates:** closing and placement settlement **20 Nov** (8-K not yet filed [?]); option window to ~18 Dec; research quiet period ends ~14 Dec (25 days, market convention [E]): first broker ratings and consensus; lock-up steps from 15 Dec; FY26 results date not given [?].

## Market input (AI BBB rows and how they enter)

| AI BBB row (Interface 18 Nov; paths of 11 Nov) | Bear / Base / Bull | How it enters |
|---|---|---|
| E1 frontier-lab revenue (OpenAI + Anthropic) 2027–29 | 155/170/187 · **190/275/360** · 230/370/515 | Revenue = E1 × own share (55 / 58 / 62%); 2026 ~100 (build 94) |
| Scenario definitions and catalysts | Financing break · digestion · agentic adoption | Bear and Bull stories; compute lapses in Bear (conditional contracts), extra capacity in Bull |
| E-layer and T-layer exit P/E | E 17 / 21 / 23.5; T 15 / 20 / 24 | Anchor for the exit P/E (premium explained under V_T) |
| Lab financing signpost (Anthropic IPO) | Pulled or below Series H / at the marks / well above | **Priced $83 = 1.41x the Series H per common share ($58.90); first close 1.65x: the Bull-side line is crossed** (for the AI BBB to read) |
| Turn calls (18–19 Nov) | E1 flat (pending this pricing); H1 2028–30 order cut by funded buyers (watch, 45%); K1 2028 lower (watch) | Translated under Price versus our call |

Equity BBB (18 Nov note, values of 6 Nov): World exit P/E 15 / **17** / 18.5, exit P/B 2.47 / **3.17** / 3.74, mid-cycle return 7.1 / **8.2** / 8.7%; USD/NOK Base flat, Bear +12% / +9% / +9%, Bull −3%. World Base window 6.6%.

## Common assumptions

**Fully diluted shares at $97.17 (millions) [F] unless tagged:** outstanding after the offering and placement **13,219.6** (Class A 7,583.1; Class N 5,636.5 incl. the 846.8 Public Benefit Fund shares, the 292.8 Amazon notes converted at the IPO and the 313.3 placement shares) + option 147.0 [A, assumed exercised] + issued after September 29.4 (acquisitions 1.4, donation matching 28.0) = **issued 13,396.0**; + **Amazon notes not converted 1,547.7** + options 1,774.3 at $2.91 (1,721.2 net, treasury method at $97.17) + unvested RSUs 1,073.7 (incl. 47.0 granted after September) + vested matching obligation 553.4 = **18,292.1** (18,283.0 at $83).
- RSUs and options count gross with no cash cost (net settlement at a 50.9% withholding rate is the same value paid in cash). Unrecognised SBC belongs to awards already counted, so it is not deducted again.
- **Dilution after the IPO [A]:** new grants 3% of revenue a year at the path price; further donation matching 0.5% a year; PBF milestones 2% each at +50% steps from the IPO price (Bull reaches $124.50). Exit shares 18,877m / **18,731m** / 19,078m.
- Draws on the Amazon and Google NPAs are at the 30-day VWAP: value-neutral, not modelled. The Broadcom NPA (90% or 85% of VWAP) is a Bear risk, not drawn in the model (cash suffices).
- **Option and placement:** both sell shares at $83, about the Base V_T, so V_T moves −$0.06 without the option and −$0.18 without the option and the placement.

**Costs and cash [A]:** compute in the window as in the scenario table (contracts, less lapses in Bear and Base, plus extra in Bull, never below the ratio needed to serve revenue: 62 / 60 / 57% in Base); other cash opex (personnel cash, channel fees, other ex donations) 25 / 23 / 21% of revenue in Base (Q3-26: 27%); owned-infrastructure capex depreciated over 5 years inside compute; cash on hand earns 3.75% (SOFR 3.94% on 5 Nov) [C], 3.0% in Bear; cash tax 0 / 5 / 12% of positive pre-tax profit in 2027–29 (RSU-vesting deductions, losses carried forward), 21% in exit earnings. SBC and non-cash donations are excluded from FCF and enter through the share count; normalised SBC (4% of revenue in Base) is deducted in exit earnings.

## Period tables and year-end path

| $bn | Bear 2027 / 28 / 29 | **Base 2027 / 28 / 29** | Bull 2027 / 28 / 29 |
|---|---|---|---|
| Revenue | 85.3 / 93.5 / 102.9 | **110.2 / 159.5 / 208.8** | 142.6 / 229.4 / 319.3 |
| E1 share | 55% | **58%** | 62% |
| Compute and infrastructure | 75 / 100 / 108 | **77 / 115 / 135** | 92 / 145 / 172 |
| Adjusted operating income | −11.9 / −29.9 / −29.8 | **5.7 / 7.8 / 30.0** | 16.4 / 33.9 / 83.4 |
| Interest income / cash tax | 7.4 / 6.8 / 6.0; 0 | **9.2 / 9.1 / 9.1; 0 / 0.8 / 4.7** | 9.2 / 9.1 / 9.5; 0 / 2.2 / 11.2 |
| Capex (D&A added back) | 15 / 6 / 4 (0.6 / 3.6 / 4.8) | **20 / 20 / 15 (0.6 / 4.6 / 8.6)** | 30 / 35 / 30 (0.6 / 6.6 / 13.6) |
| FCF ($bn / per share) | −18.9 / −25.5 / −23.0 (−1.04 / −1.39 / −1.26) | **−4.5 / 0.6 / 27.9 (−0.25 / 0.03 / 1.53)** | −3.8 / 12.5 / 65.4 (−0.21 / 0.68 / 3.58) |
| Net cash at year end ($bn / per share) | 226.9 / 201.4 / 178.5 (12.40 / 11.01 / 9.76) | **241.3 / 241.9 / 269.9 (13.19 / 13.23 / 14.75)** | 242.0 / 254.5 / 319.9 (13.23 / 13.91 / 17.49) |

Per share on the 18,292m fully diluted shares at $97.17; net cash per share at exit on exit shares is in the decision table.

**Year-end path** (D_t = 0; interim marks: the entry-implied P/E of 70.4x on Base 2027 normalised NOPAT glides to the exit P/E; diagnostic only)

| | Bear V_t / r_t | **Base V_t / r_t** | Bull V_t / r_t |
|---|---|---|---|
| End-2026 (stub, same in all) | 97.2 / +0.1% | **97.2 / +0.1%** | 97.2 / +0.1% |
| End-2027 | 42.1 / −56.7% | **106.0 / +9.0%** | 182.6 / +87.8% |
| End-2028 | 30.9 / −26.7% | **102.0 / −3.8%** | 192.1 / +5.2% |
| End-2029 (V_T) | 17.7 / −42.7% | **83.9 / −17.8%** | 176.6 / −8.1% |
| IRR to 2027 / 2028 / T | −52.9% / −41.9% / −42.1% | **+8.1% / +2.3% / −4.6%** | +76.3% / +38.0% / +21.1% |

The Base path looks fair in 2027 only because the mark still carries the entry multiple; the multiple compresses as growth slows, so the last two years lose value.

## V_T build and exit checks

**V_T = exit P/E × normalised 2030 NOPAT + net cash at exit − commitment overhang, ÷ exit shares.**

| $bn | Bear | **Base** | Bull |
|---|---|---|---|
| 2030 revenue (growth) | 111.1 (+8%) | **254.7 (+22%)** | 415.1 (+30%) |
| Normalised EBIT margin → NOPAT (21% tax) | 16% → 14.0 | **25% → 50.3** | 31% → 101.7 |
| × exit P/E → EV | 15 → 211 | **26 → 1,308** | 30 → 3,050 |
| + net cash at exit | 178.5 | **269.9** | 319.9 |
| − commitment overhang | 55.2 | **7.4** | 0 |
| = equity ÷ exit shares | 334 ÷ 18,877m | **1,571 ÷ 18,731m** | 3,370 ÷ 19,078m |
| **V_T** | **17.7** | **83.9** | **176.6** |

**Exit P/E, Base 26 [A]:** the AI BBB E-layer exit P/E is 21 and World 17. Anthropic in 2030 still grows ~20% (Base +22%, 2031 +18%) with margin expansion ahead, against ~10% for the platforms, so a premium of 5 points is given; for reference, Microsoft trades at a core P/E of 24.1 on ~15% growth and Alphabet's 5-year forward-P/E median is 20.8 (15.6–31.7) [C]. Bear 15 (World Bear; growth stalled, contracts overhang), Bull 30.

**Exit consistency** (Year 3 = 2029 against the normalised 2030 economics; material if the gap > 10%)

| Row | Scenario | 2029 compute (adj. margin) | Normalised | Treatment | Per share |
|---|---|---|---|---|---|
| Compute ratio and margin | Bear | 105% (−29%) | 58% (21%) | Contracts firm today count for their full term (backlog rule): excess of paid (80% of the schedule) over need, 2030–33, 50% resold, no tax shield, at 8% | −$2.92 |
| | **Base** | **65% (14%)** | **52% (29%)** | **Named reason [F]: the contract schedule flattens after 2029 ($451.6bn before end-2030, the rest spread over 2031–45) while revenue grows 22%; the residual 2030 excess ($8.0bn after tax) is deducted** | **−$0.40** |
| | Bull | 54% (26%) | 48% (34%) | Named reason: committed 2030 compute ($155bn) is below the need ($199bn); no excess | 0 |

Other treatment as a sensitivity: the skill's 2-year tail on the Base margin gap (−$26.7bn after tax instead of −$7.4bn) gives V_T $82.8, **IRR −5.0%, P_k $58.2**; no overhang at all gives −4.5%, $59.2.

**Exit cross-check**

| | Bear | **Base** | Bull | World (Equity BBB) Bear / Base / Bull |
|---|---|---|---|---|
| Exit P/E: EV ÷ NOPAT / equity incl. interest | 15 / 18.3 | **26 / 26.9** | 30 / 30.3 | 15 / 17 / 18.5 |
| EV ÷ 2030 revenue | 1.9x | **5.1x** | 7.3x | — |
| Exit P/B (book incl. the Amazon notes) | 1.6 | **4.9** | 8.4 | 2.47 / 3.17 / 3.74 |
| Buyer's implied return (0.7 × earnings yield + long-run growth 4 / 7 / 8%) | 7.8% | **9.6%** | 10.3% | 7.1 / 8.2 / 8.7% |

The Base buyer at exit earns more than the World mid-cycle return (9.6% against 8.2%), so the exit is not stretched; the P/B above World reflects an asset-light, high-return business.

## Growth capex test

Growth investment = compute expensed above the normalised ratio in 2027–29 + capex (incl. the stub) + committed excess after exit; ΔNOPAT = 2030 normalised NOPAT − 2026 revenue at the same margin [A].

| | Bear | **Base** | Bull |
|---|---|---|---|
| Growth investment $bn | 274 | **146** | 175 |
| ΔNOPAT $bn a year | 7.1 | **39.5** | 88.2 |
| ROIC_g vs k = 12% | **2.6%: destroys value** | **27%: accretive** | 50%: accretive |
| Value created ≈ investment × (ROIC_g ÷ k − 1) | −$214bn | **+$183bn** | +$560bn |

Evidence: revenue per dollar of compute rose from 0.40x to 1.72–2.08x in six quarters [F]; Base needs 1.92x by 2030, Bear stays at ~1x in 2028–29. In Base the compute build earns well above k; the shareholder at $97.17 still fails because the price pays for the build in advance. In Bear the commitments turn growth spending into a value transfer to the compute suppliers.

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (dated, to V_T) | −42.1% | **−4.6%** | 21.1% |
| IRR_T in NOK on the Equity BBB NOK path | −40.5% | **−4.6%** | 20.0% |
| Rule 1 screen d + g at constant P/E | n/m: EPS base near zero (2027 core EPS $0.05), hygiene rule 3 | **n/m** | n/m |
| d / g / c | 0 / −42.1% / 0 | **0 / −4.6% / 0** | 0 / 21.1% / 0 |
| g: re-rating / NAV growth | n/a (Track A; the multiple effect is in the return bridge) | **n/a** | n/a |
| Structural / cyclical | n/a: no rate cycle; the commitment overhang is the cyclical element (Base without it −4.5%) | **n/a** | n/a |
| ΣD_t / V_T | 0 / 17.7 | **0 / 83.9** | 0 / 176.6 |
| P_k / margin of safety | 12.4 / −87.2% | **58.9 / −39.4%** | 124.1 / +27.7% |
| Rule 3: P/E on 2030 normalised EPS vs ceiling IRR_T ÷ k² | 130.6x vs negative | **36.2x vs negative: fails** | 18.2x vs 14.7x: fails |
| Capital preserved? V_T vs P | No, −81.8% | **No, −13.7%** | Yes, +81.8% |

**Sensitivities (Base at $97.17: IRR / P_k / margin of safety)**

| Change | Result | Change | Result |
|---|---|---|---|
| Exit P/E 21 (E layer) | −9.9% / 49.4 / −49.2% | Exit P/E 30 | −0.8% / 66.5 / −31.6% |
| Exit P/E 24 (governance discount −2) | −6.6% / 55.1 / −43.3% | E1 share 50% / 65% | −9.6% / 49.8 / −48.7%; −0.7% / 66.7 / −31.4% |
| Normalised compute 48% / 56% | −0.8% / 66.5 / −31.5%; −8.8% / 51.3 / −47.2% | Window compute ±15% | −5.6% / 57.1; −3.8% / 60.4 |
| No dilution after the IPO | −3.9% / 60.3 / −37.9% | Cash yield 3.0% | −4.7% / 58.7 / −39.6% |
| E1 Bull revenue, Base costs and P/E | **10.1% / 92.1 / −5.2%** | Entry at $83 / $92.60 (post-market) / $100 | 0.3% / −3.1% / −5.5% (P_k $58.9) |
| Bear at 58% share / at exit P/E 21 | −40.5% / −37.7% | | |

- **What the price needs (reverse test, $97.17):** an exit P/E of **47.2**, or normalised compute at **30.5%** of revenue (EBIT 47%), or **101% of E1** (2029 revenue $363bn, 2030 $443bn). Each is beyond the Bull case; none is in the AI BBB Base.
- **Scenario-weighted reference (convention 25/50/25 on V_T levels):** V_T $90.5, IRR −2.3%. Not the decision.
- **Share of Bull already priced:** (97.17 − 58.9) ÷ (124.1 − 58.9) = **59%**.
- **Bear balance-sheet survival:** net cash falls from $246bn to $178bn by end-2029; $14.8bn of the credit facility available; covenant ($5bn liquidity) far away. If unvested RSUs are net-settled at Bear prices, withholding costs ~$16bn more [A]. The Broadcom NPA ($42bn at 13% PIK, 85% of VWAP) and the VWAP NPAs are dilutive fall-backs. True-ups make Google and Amazon capacity payable whether used or not. **The company survives; the equity is the shock absorber.**

## Price versus our call

- **What the price implies:** at $97.17 Base returns k only if Anthropic takes **101% of the AI BBB's Base E1** in 2029 ($363bn), i.e. more than the whole Base lab market, or the exit P/E is **47** on a 25% margin, or the normalised margin is **47%** on a 26x multiple. At the $83 IPO price: 83% of E1 or an exit P/E of 39.
- **Sector turn calls (AI BBB 18–19 Nov):** E1 is flat with the call pending this pricing (no path change). The H1 watch call "order cut by funded buyers" (45%) is a supplier-side call: Anthropic is now a funded buyer (+$117bn), so its revenue path does not move; if rival labs lose funding, its E1 share could rise (65%: −0.7%, still fails). K1 2028 lower (watch, 50%): context only. Equity BBB's World de-rating watch maps to the exit P/E 24 row (−6.6%). No call takes Base to k.
- **Company leading signals (20 Nov):**

| Signal | Score | Evidence |
|---|---|---|
| Order intake | +1 | Run-Rate Revenue ~$81bn at 31 Oct, +$10bn in one month [F]; Base 2027 ($110bn) is 1.28x the Q4-26 annualised stub |
| Issuance | 0 | Upsized primary (+155m shares, option 147m) at 1.41x the Series H: cash for the commitments, sold where demand was |
| Insider dealings | 0 | Co-founders sold 23.65m shares ($1.96bn) in the offering; directors indicated up to $305m of purchases |
| Contract behaviour | 0 | Commitments $900.9bn in the 424B4, the same total as the 11 Nov prospectus: no new compute contract disclosed |
| Guidance vs consensus | 0 | No guidance; consensus forms after the quiet period (~14 Dec) [?] |

- **Verdict line: ahead (more negative than the price).** The market pays for a lab revenue share the AI BBB lab market does not hold in Base, plus a premium multiple. What it may be missing: $451.6bn of compute is committed before 2030, so the margin depends on the revenue share, and the 2027–28 margin stays near 5%. The risk to this call is the order-intake signal: 2027 revenue tracking ~$140bn (the Bull path) would move Base toward Bull, and even that alone gives 10.1%.
- **Scorecard:** opened 20 Nov 2026 at $97.17: "Base V_T $83.9 below the price; P_k $58.9". Mark at the next run.

## Verdict and caveat

- Band: **clears** above +2%, **marginal** −2% to +2%, **fails** below −2% on the Base margin of safety. At $97.17 the margin is −39.4% (−29.0% at $83): fails (verdict in the Summary).
- **What flips it:** a price at or below **$57.8** (+2% band; NOK 562); or evidence that Anthropic's revenue runs on the E1 Bull path **and** that margins reach the Bull level (2027 revenue ~$140bn against Base $110bn, with normalised compute near 48% of revenue, 2.1x revenue per compute dollar: 16.2% at the Base exit P/E); revenue alone is not enough (10.1%). A cut in contracted compute without a revenue cut moves Base up ~1 pp per 15%.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation or a price target. The revenue share, compute schedule, normalised margin and exit P/E are own assumptions [A]; the scenario paths for the lab market come from the AI BBB.
- **Practical for a Norwegian buyer:** the share trades on Nasdaq at $97.17 (NOK 946 at 9.7391, before broker FX fees); a limit at the +2% band ($57.8, NOK 562) sits 41% below the market.

## Tracking

- No quarter reported since the first version; first tracking at the FY26 results. **Deal outcome against the model:** priced $83 (model range $70–78), 956.35m primary + 147.0m option (model 801.4m + 123.75m), cash at closing $244.6bn (model $221.7bn at $74). The extra shares were sold at about the Base V_T, so Base P_k moved +$0.5 to $58.9; the verdict worsened through the price.

## Risks and signposts

| Risk | Why it matters | Signpost (Bear / Bull) | Next |
|---|---|---|---|
| **Commitments vs revenue** | $900.9bn + $150–175bn of compute against Run-Rate Revenue of $81bn; true-ups bind | Compute > 75% of revenue two quarters in 2027 / compute efficiency > 2.0x with revenue ahead of the 58% path | FY26 results; Q1-27 |
| Competition and price | Google, OpenAI; price cuts −$600m in Q3; > 80% of revenue from models < 6 months old | Revenue growth < 10% q/q twice (AI BBB lab run-rate line) / > 20% q/q into H2-27 | Each quarter |
| Customer and channel concentration | Top five 25% of 9M revenue; CSPs bill 44%; VC-funded coding customers | Top-five share up, a top customer lost / top-five share < 15% | Prospectus metrics in each report |
| Suppliers are owners and rivals | Google, Amazon, Microsoft, NVIDIA, Broadcom fund, supply and compete | A partner reprices, delays or withdraws capacity / new independent financing | Ongoing |
| Governance (not in the valuation) | LTBT board majority, Class F 50.1%, PBC balancing duty: Class A cannot change control or strategy; public-benefit spending can rise | PBF issues beyond the framework, larger donations / none | Proxy, 2027 |
| Dilution and supply | PBF 846.8m + 2% per +50%; donation matching; options; lock-up steps; 3.7bn shares before day 180; placement unlocked | Lock-up releases with the price below $83 / absorbed above it | 15 Dec 2026 – 18 Nov 2027 |
| Aftermarket | Day one: open $111.50, close $97.17, post-market $92.60; first broker ratings after ~14 Dec | Below the $83 IPO price / above the $111.50 open | Quiet-period end ~14 Dec |
| Safety, regulation, litigation | Release delays (Mythos, Fable 5), liability for misuse, Bartz-type settlements ($1.5bn in 2025); FTC civil investigative demand (Oct 2026) | Release restricted or a large claim / none | Ongoing |

## For other modules

| Value | Bear | **Base** | Bull |
|---|---|---|---|
| Anthropic revenue $bn 2026 / 2027 / 2028 / 2029 / 2030 | 54.7 / 85.3 / 93.5 / 102.9 / 111 | **54.7 / 110.2 / 159.5 / 208.8 / 255** | 54.7 / 142.6 / 229.4 / 319.3 / 415 |
| Implied share of E1 (2026: ~58% of the AI BBB build of 94) | 55% | **58%** | 62% |
| Compute and infrastructure spend $bn 2027 / 28 / 29 | 75 / 100 / 108 | **77 / 115 / 135** | 92 / 145 / 172 |
| V_T / P_k per share | 17.7 / 12.4 | **83.9 / 58.9** | 176.6 / 124.1 |
| Equity value: market at $97.17 / at P_k (fully diluted 18,292m; issued 13,396m) | | **$1,777bn / $1,078bn; issued $1,302bn / $789bn** | |

**Stakes** (pre-tax, USD bn; shares after the deal [F], 424B4)

| Holder | Shares | at the IPO price $83 | at the first close $97.17 | at Base P_k $58.9 |
|---|---|---|---|---|
| Amazon (1,936.5m Class N + 1,547.7m in unconverted notes) | 3,484.1m | 289.2 | 338.6 | 205.2 |
| Alphabet (incl. the 120.5m placement shares) | 1,775.0m | 147.3 | 172.5 | 104.6 |
| NVIDIA (placement) | 120.5m | 10.0 | 11.7 | 7.1 |
| AMD (placement) | 30.1m | 2.5 | 2.9 | 1.8 |
| Broadcom, Micron, Microsoft (placement, each) | 12.0m | 1.0 | 1.17 | 0.71 |
| TSMC (placement) | 6.0m | 0.5 | 0.59 | 0.35 |

- **ai-market-bbb:** E1 share and the 2026 Anthropic revenue ($54.7bn, Q4 $21.5bn [A]); Run-Rate Revenue $81bn at 31 Oct [F]; the commitment schedule (~$77 / 125 / 147bn in 2027–29) as lab demand inside K4; placement split [F] (NVIDIA $10.0bn, Microsoft $1.0bn) for the K3 vendor-financing row. **Lab-financing signpost: priced 1.41x and closed 1.65x the Series H per common share (Bull-side line crossed).** No E1 path moves from this document.
- **amzn / googl:** the stake rows above; Amazon's claim includes the notes that stay outstanding after the IPO. **nvda:** the $10bn placement (120.5m shares); Anthropic's NVIDIA-GPU capacity via SpaceXAI, Nscale, Lambda and Microsoft. **msft:** Anthropic's ≥ $47.2bn Azure commitment (Nov 2026–Jun 2033) for E2, the $1bn placement. **tsm / mu:** placement only, immaterial.

## Change log

- **20 Nov 2026 — v1.1, re-mark after the IPO** (424B4 and FWP of 18–19 Nov; first close $97.17): priced $83 above the range, upsized to 956.35m primary + 147m option; FD 18,292m, cash at closing $244.6bn. Base −4.6%, P_k $58.9, −39.4%, fails (at $83: 0.3%, −29.0%); Bear −42.1%, Bull 21.1%; Step 6b added (skill 2026-11-18.1).
- **13 Nov 2026 — v1.0, new analysis** at the IPO range ($70–78) from the Bafin EU prospectus of 11 Nov 2026 and the AI BBB of 11 Nov: Track A with explicit compute; Base fails (3.8% at $74, P_k $58.4, −21.1%), Bear −38.3%, Bull 31.4%. Model: `.claude/skills/iaf-valuation/references/models/anthropic/`.

## Appendix: own assumptions `[A]`

| Assumption | Bear / Base / Bull | Basis |
|---|---|---|
| Share of E1 | 55 / 58 / 62% | 2026 ~58% of the AI BBB build; Q3-26 ~61%; Bear loses enterprise and VC-funded coding demand, Bull holds the Q3 share |
| Revenue growth 2030 / 2031 | 8 / 22 / 30%; 6 / 18 / 25% | E1 Base growth halves each year (AI BBB); Bear stalled |
| Compute schedule (contracts) | ~77 / 125 / 147 / 155bn in 2027–30; 135 / 120 / 100bn in 2031–33 | $900.9bn and its timing, $451.6bn to 2030, variable TPU and AMD on their delivery windows [F] |
| Compute taken 2027–29 | 75 / 100 / 108 · 77 / 115 / 135 · 92 / 145 / 172 | Bear: conditional contracts lapse, SpaceXAI cancelled; Base: ~8% of 2028–29 not taken; Bull: extra capacity |
| Normalised compute / other opex / SBC | 58 / 21 / 5% · 52 / 19 / 4% · 48 / 18 / 3% | Q2-26 compute 48%, Q3 58%; other cash opex 27% in Q3 falling with scale |
| Exit P/E (EV ÷ NOPAT 2030) | 15 / 26 / 30 | World 15 / 17 / 18.5; E layer 17 / 21 / 23.5; growth premium in Base and Bull |
| Overhang terms | 80% paid, 50% resold, to 2033, no shield · 92%, 2 years · none | Termination rights and conditions on $186.2bn; true-ups on Google and Amazon [F] |
| Capex (owned infrastructure, prepayments) | 15 / 6 / 4 · 20 / 20 / 15 · 30 / 35 / 30 | "Significant net cash used in operating and investing activities" (p. 179) |
| Cash yield; cash tax 2027–29 | 3.0 / 3.75 / 3.75%; 0 / 5 / 12% | SOFR 3.94% (5 Nov); RSU-vesting deductions |
| Dilution after the IPO | Grants 3% of revenue; matching 0.5% a year; PBF 2% per +50% from $83 | Plans and framework [F]; issuance [A] |
| Q4-26 stub | Revenue 21.5, compute 13.0, other 5.5, capex 3.0, interest 1.5 | Q3 run-rate, Run-Rate Revenue $81bn at 31 Oct, seasonality, SpaceXAI full from December |
| Option | Exercised (147.0m, $12.2bn, no underwriting discount) | Deal upsized and priced above the range; first close +17% |

## Appendix: sources

| # | Source | Used for | Date |
|---|---|---|---|
| S0 | Anthropic, PBC — final prospectus **424B4** (EDGAR CIK 2130357, accession 0001628280-26-074944): The Offering (p. 20–24), Use of Proceeds, Capitalization, Dilution (p. 129–136), Liquidity (p. 144), Run-Rate Revenue (p. 203), notes (p. 172), lock-up schedule; **pricing FWP** (0001628280-26-074937); S-1MEF (0001628280-26-074904) | Price, deal size, option, placement split, share count after the deal, cash pro forma as adjusted, NTBV, Amazon conversion, holders, lock-ups | Dated 18 Nov, filed 19 Nov 2026 |
| S1 | Anthropic, PBC — EU retail prospectus approved by Bafin (user file `bafin-prospectus.pdf`, 307 pages; printed page = PDF − 10): Summary S-1–S-7; Risk factors (p. 29–31, 84–85); MD&A (p. 152–192); Shareholders (p. 255–257); Dividend policy (p. 291) | Business, financials, metrics, commitments, NPAs, governance [F] | 11 Nov 2026 (data to 30 Sep 2026) |
| S2 | Yahoo Finance (`ANT` quote and daily chart; `NOK=X`); AllRatesToday USD/NOK; Norges Bank `EXR/B.USD.NOK.SP` | First-day prices and volume; USD/NOK 9.7391 (cross-checks 9.7398, 9.6866) | 19 Nov close; 20 Nov 07:24 UTC |
| S3 | `docs/ai-market-bbb.md` (Interface: E1, layer exit P/E, turn calls, signpost states; lab-financing signpost row) | E1 paths, scenarios, layer exit P/Es, Series H per common share $58.90 [C] | 18 Nov 2026 (paths 11 Nov) |
| S4 | `docs/equity-market-bbb.md` (Interface) | World exit P/E, P/B, mid-cycle return, USD/NOK path, SOFR 3.94% | 18 Nov note (values 6 Nov) |
| S5 | `docs/hy-market-bbb.md` (Interface, rates) | Rate context only | 18 Nov 2026 |
| S6 | `docs/amzn-analysis.md`, `docs/googl-analysis.md`, `docs/nvda-analysis.md`, `docs/msft-analysis.md` (grep only) | Stake carrying values, peer P/Es [C] | 7–19 Nov 2026 |
| S7 | Zacks commentary, 19 Nov 2026 18:04 ET [E] | Day-one context (record volume, intraday ~$110) | 19 Nov 2026 |
| S8 | Model `.claude/skills/iaf-valuation/references/models/anthropic/` (`model.py`, `report.py`, `drivers.py`, v1.1) | Every computed figure | 20 Nov 2026 |

Not available: the closing 8-K and whether the option was exercised (closing 20 Nov, not yet filed) [?]; the audited statements' notes (Note 8 cost of revenue, Note 13 commitments by year) [?]; capex for 9M-26 as a line [?]; the FY26 results date [?]; analyst consensus (quiet period to ~14 Dec) [?].
