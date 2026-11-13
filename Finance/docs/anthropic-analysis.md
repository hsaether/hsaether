# Anthropic, PBC (ANT) — IAF analysis at the IPO, stub 20 Nov–Dec 2026 + 2027–2029

**Version 1.0 — 13 Nov 2026** · price: US range **$70–78** (midpoint $74; pricing ~18 Nov, first trade 19 Nov) · skills: iaf-valuation **2026-11-12.1**; inputs AI BBB 11 Nov (ai-market-bbb 2026-11-11.2), Equity BBB 6 Nov, HY BBB 5 Nov · **verdict: fails** (Base margin of safety −21.1% at $74; −16.9% at $70, −24.9% at $78).

**Author's note:** written by Claude, an Anthropic model, so this is an analysis of the author's maker. It applies the same method and sources as for any other company, every number is tagged [F] (prospectus or filing), [E] (third-party estimate), [A] (own assumption) or [C] (carried from a workspace document), and neither the Bear case nor the verdict is softened.

## Summary

**Verdict**
- **Fails at every point of the range. Base IRR 5.5% / 3.8% / 2.2% a year at $70 / $74 / $78 against k = 12%. P_k ≈ $58.2–58.6 per Class A share; margin of safety −16.9% / −21.1% / −24.9%.** Buying at the IPO clears k only at an IPO price of about **$57.5** (the +2% "clears" band at **$56.3**), roughly the Series H price per common share ($58.90, May–June 2026) [C].
- At $74 the buyer pays **22x the Base 2030 normalised after-tax operating profit today** (EV $1.12tn fully diluted, 10.2x Base 2027 revenue). Base reaches k only with an exit P/E of **34** (Base 26), or a normalised EBIT margin of **33%** (Base 25%), or **73% of frontier-lab revenue** (E1) in 2029 instead of 58% (revenue $264bn instead of $209bn).
- **Bear (AI BBB financing break): −38% a year, capital not preserved (−78%).** The company survives (net cash ≥ $153bn), the equity does not: ~$70bn of cash burn in 2027–29 against committed compute, and $55bn of commitments above need after 2029.
- **Bull (agentic adoption): +31% a year;** the price already reflects 25% of the way from Base to Bull. An aftermarket entry after a first-day pop is worse: Base −2.1% at $90.

**Base in brief**
- Revenue on the AI BBB E1 Base path at a constant **58% share** (Anthropic's share of E1 in 2026): $110 / 160 / 209bn in 2027–29 (2026: $54.7bn). Compute follows the contracts, not revenue: $77 / 115 / 135bn (70% / 72% / 65% of revenue), so the adjusted operating margin falls to 5% in 2027–28 before recovering to 14% in 2029 (9M-2026: 12%).
- Exit: 26x normalised 2030 NOPAT (revenue $255bn, EBIT 25% after SBC, 21% tax) plus net cash $245bn, less a $7bn commitment overhang; **V_T $83.1** on 18.59bn fully diluted shares.
- **Where the return comes from (per share):** earnings growth +$81.0, multiple 51.5x → 26x −$70.7, dilution −$1.7, overhang −$0.4, cash +$0.9: $74 → $83.1. The business case for the compute is good (ROIC_g 27% > k); the IPO price already capitalises it.

**Bear in brief**
- Story: the AI BBB financing break inside the equity Bear (earliest H1 2027): lab revenue stalls (E1 155 / 170 / 187), enterprise and VC-funded coding customers cut spend, prices fall. Anthropic keeps 55% of E1: $85 / 94 / 103bn, flat on the Q4-26 run-rate.
- Worst years 2028–29: compute ~105% of revenue even after conditional contracts lapse and SpaceXAI is cancelled (Google and Amazon true-ups bind); adjusted operating margin about −30%.
- Capital not preserved: V_T $16.5 (−78%). Net cash bottoms at $153bn at exit; the $5bn liquidity covenant is never near; no new equity needed. Damage: the revenue path with fixed commitments (3.8% → −25%), then the normalised margin and the exit P/E (→ −41%).

**Decision table (USD per Class A share; P = $74 midpoint; fully diluted 18,138m shares)**

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (USD) / NOK path (Equity BBB) | −38.3% / −36.5% | **3.8% / 3.8%** | 31.4% / 30.1% |
| V_T (31 Dec 2029) | 16.5 | **83.1** | 173.2 |
| **P_k / margin of safety** | 11.6 / −84.4% | **58.4 / −21.1%** | 121.7 / +64.4% |
| Capital preserved? (V_T vs P; no dividends) | No, −77.7% | Yes, +12.3% | Yes, +134% |
| Cumulative FCF per share 2027–29 | −3.83 | **1.19** | 3.95 |
| Net cash per share at exit | 8.18 | **13.16** | 15.26 |
| Balance sheet | Burns ~$70bn 2027–29; net cash $153bn at exit | Net cash $245bn | Net cash $295bn |

**The range** (each column at its own share count and IPO proceeds; NOK at USD/NOK 9.5610)

| IPO price | $70 (NOK 669) | **$74 (NOK 708)** | $78 (NOK 746) |
|---|---|---|---|
| Fully diluted shares / market cap / EV | 18,154m / $1,271bn / $1,053bn | **18,138m / $1,342bn / $1,120bn** | 18,124m / $1,414bn / $1,188bn |
| Base IRR / P_k / margin of safety | 5.5% / 58.2 / −16.9% | **3.8% / 58.4 / −21.1%** | 2.2% / 58.6 / −24.9% |
| Bear / Bull IRR (USD) | −37.4% / 33.7% | −38.3% / 31.4% | −39.0% / 30.1% |
| Bear / Bull IRR, NOK path | −35.7% / 32.4% | −36.5% / 30.1% | −37.3% / 28.9% |
| Exit P/E for k (Base) / E1 share for k | 32.2 / 69% | 34.1 / 73% | 36.1 / 77% |

**Per-share path** (Track A with explicit compute; $bn and $ per fully diluted share at $74; V_t is a diagnostic mark)

| | Q4-26 (stub) | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Base revenue / compute ($bn; % of revenue) | 21.5 / 13.0 (60%) | 110.2 / 77 (70%) | 159.5 / 115 (72%) | 208.8 / 135 (65%) |
| Base adjusted operating income $bn (margin) | 3.0 (14%) | 5.7 (5%) | 7.8 (5%) | 30.0 (14%) |
| Base FCF $bn / per share | 1.3 / 0.07 | −5.4 / −0.30 | −0.2 / −0.01 | 27.1 / 1.50 |
| Base net cash $bn / per share | 223.0 / 12.30 | 217.6 / 12.00 | 217.4 / 11.99 | 244.6 / 13.48 |
| Base core EPS (normalised SBC, 21% tax, ex interest) | — | 0.05 | 0.06 | 0.94 |
| Base V_t | 74.1 | 84.6 | 87.9 | 83.1 |
| Bear FCF per share / V_t | 0.07 / 74.1 | −1.08 / 33.3 | −1.44 / 25.5 | −1.31 / 16.5 |
| Bull FCF per share / V_t | 0.07 / 74.1 | −0.26 / 144.6 | 0.64 / 164.6 | 3.56 / 173.2 |

Tags: `[F]` prospectus or filing · `[E]` third-party estimate · `[C]` carried from a workspace document · `[A]` own assumption · `[?]` not found. Prospectus page numbers are printed pages (PDF page − 10).

## Header

| Item | Value |
|---|---|
| Company | Anthropic, PBC (Delaware public benefit corporation), San Francisco. Class A common stock, Nasdaq Global Select "ANT", ISIN US03703U1079 [F] |
| Price | IPO range **$70–78**, midpoint $74 (US offering); EU retail maximum $120; one price for all investors [F]. Not yet priced: the analysis is shown at $70 / $74 / $78 |
| Valuation date / exit / T | **20 Nov 2026** (closing; the IPO price is paid) / 31 Dec 2029 / **3.115 years** |
| Shares | Issued after the deal (incl. over-allotment, Public Benefit Fund) **13,243m**; **fully diluted 18,138m** at $74 (bridge in Common assumptions) |
| Market cap / EV at $74 | $980bn issued; **$1,342bn fully diluted**; net cash at closing **$221.7bn**; EV **$1,120bn** = 20.5x 2026 revenue, 16.5x Q3-26 annualised, 10.2x Base 2027 |
| NAV | Not used (Track A): an AI lab has no asset-market NAV. Net tangible book after the deal $107.4bn, $8.21 per share [F] |
| FX | USD price. USD/NOK **9.5610** (EODHD 18:25 UTC 12 Nov, via `docs/nvda-analysis.md` v1.5) [C], one day old: NOK 669 / 708 / 746 for $70 / 74 / 78, before broker FX fees. NOK path for Bear and Bull from the Equity BBB |
| Track | **A with explicit compute and capex**: value at exit is a going-concern multiple on earnings, but compute commitments drive cash flow, so the build is year by year as in Track B |
| k | **12%**, not raised: no debt beyond $6.2bn of Amazon notes settled in shares, deep liquidity expected. Governance, concentration and commitments are in Bear and Risks, not in k |
| Dividends | None; the company intends to retain all earnings and the credit agreement limits payouts (p. 291) [F]. D_t = 0 in all scenarios |
| Primary source | EU retail prospectus approved by Bafin on **11 Nov 2026** (307 pages; financial statements incorporated by reference, not in the file), cross-checked against the EU summary (S-1 to S-7) [F] |
| Inputs read | `docs/ai-market-bbb.md` **11 Nov 2026** (E1 paths, scenarios, layer exit P/Es, lab rows); `docs/equity-market-bbb.md` **6 Nov 2026** (World exit P/E and P/B, mid-cycle return, USD/NOK path); `docs/hy-market-bbb.md` **5 Nov 2026** (rates context; SOFR 3.94% via Equity BBB). Cross-checks only: `amzn` (11 Nov re-mark), `googl` (11 Nov note), `nvda` v1.5 (12 Nov) |
| Stale after | **19 Nov 2026** (re-mark at the final IPO price and first trade) |

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
| Company items | Overhang PV $55bn (firm contracts to 2033, 50% resale); capex 15 / 6 / 4 | **Overhang $7bn; capex 20 / 20 / 15** | No overhang; capex 30 / 35 / 30; PBF +2% twice |
| Macro and NOK | Equity Bear; USD/NOK +12% / +9% / +9%; cash yield 3.0% | Equity Base; NOK flat; 3.75% | Equity Bull; NOK −3%; 3.75% |
| Result at $74: IRR / P_k / capital | −38.3% / $11.6 / −78% | **3.8% / $58.4 / +12%** | 31.4% / $121.7 / +134% |

**Driver breakdown** (one driver at a time from Base, IRR at $74)

| Step | Base → Bear | Base → Bull |
|---|---|---|
| Base | 3.8% | 3.8% |
| Revenue: E1 path × own share (window compute held at the contracts) | −25.2% | 19.7% |
| + window costs (compute lapses or extra capacity, opex, capex, cash yield) | −22.6% | 19.2% |
| + normalised 2030 margin | −31.6% | 26.8% |
| + exit P/E (15 / 30) | −41.0% | 31.4% |
| + overhang terms (full term, resale, no tax shield / none) | −38.3% | 31.4% |

Bear: the fixed commitments do the damage once revenue stalls; the lapses and resale help (+2.6 pp, +2.7 pp). Bull: revenue alone takes Base to 19.7%; Base costs and multiple on the Bull revenue give 20.0%.

**Base return bridge (USD per share, $74 → V_T $83.1):** entry = EV $61.78 + net cash $12.22. Earnings growth (normalised NOPAT $21.8bn on 2027 revenue → $50.3bn in 2030, at the entry multiple 51.5x) **+$81.0**; multiple 51.5x → 26x **−$70.7**; commitment overhang −$0.4; dilution after the IPO −$1.7; cash +$0.9. The entry multiple (51.5x Base 2027 normalised NOPAT) is a 2027 growth multiple that 2030 growth (+22%) no longer carries: the earnings growth is real but already paid for.

## Company and status

**Business (p. 151–161) [F].** Frontier lab selling Claude through its API platform (pay-per-token), first-party applications (Claude Code, Cowork, vertical products) and the three big clouds (AWS, GCP, Azure). Revenue $41m (2023), $386m (2024), $4,585m (2025); 9M-2026 **$33,242m**; quarters Q1–Q3 2026 **$4,731m / $11,555m / $16,956m** (+47% q/q in Q3, with ~$600m of price cuts).
- **Mix (9M-26):** consumption $26.3bn (79%), subscriptions $6.9bn (21%); CSP marketplaces billed **44%** of revenue and 52% of receivables. **Top five customers 25% of 9M revenue** (21% of Q3; 36% of Q1); none above 10%. 11,900+ customers at ≥ $100k TTM (74% of revenue), 1,900+ at ≥ $1m, ~250 at ≥ $10m; net revenue retention ~900% (p. 29, 153, 159–160).
- **Revenue quality:** 5–7% of 9M revenue came from customers later found to breach usage terms; enforcement was stepped up in Aug–Sep (p. 161). Model versions under six months old were > 80% of Q3 revenue (p. 160).
- **Costs (9M-26, % of revenue):** compute and infrastructure $18.8bn (57%; Q3 58%, incl. **$5.0bn of short-term compute** at a premium), personnel $4.9bn (15%, of which SBC $3.3bn), sales, marketing and partnerships $5.5bn (17%, mostly channel fees), other $5.3bn (16%, incl. $2.1bn of non-cash donation matching) (p. 164–167).
- **Margins:** operating loss $(1,260)m; Q2 +$974m, Q3 $(567)m. Adjusted operating income $4,081m (12%); Q2 19%, Q3 15%. Revenue per dollar of compute 0.40x (Q1-25) → 2.08x (Q2-26) → **1.72x (Q3-26)** (p. 154, 175–178).
- **GAAP net loss $(104.0)bn** in 9M-26 is $94.3bn of fair-value changes on notes, derivatives and SAFEs plus $10.4bn on partner financing arrangements: valuation marks, not operations. Cash flow 9M-26: operating **+$6.6bn**, investing $(36.5)bn (mostly short-term investments; capex and prepayments about $3–6bn derived [A]), financing +$110.7bn (p. S-3, 188–189).

**Compute commitments (p. 155, 190–192) [F]:** **$900.9bn** in total (contract table $320.0bn, short-term $17.4bn, leases not yet commenced $451.2bn, post-September $105.7bn and $6.6bn), of which **$451.6bn before end-2030**, **$70.7bn in the 12 months to Sep 2027**, and **$186.2bn subject to termination rights or counterparty conditions**. Plus **$150–175bn** without a fixed dollar amount (additional Google TPU $125–150bn delivered 2028–31; AMD Helios > $20bn from 2027).

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

**Funding (p. 155, 180–185) [F]:** cash and short-term investments $131.8bn at 30 Sep; $15bn revolver to 2031 (undrawn; liquidity covenant ≥ $5bn from Q4-26). Partner capacity: Google NPA $20bn ($10bn after the placement; draws settled at the 30-day VWAP; requests to Dec 2030), Amazon NPA $15bn (VWAP shares, compute milestones, to May 2029), Broadcom NPA **$42bn** to finance lease rent (9% PIK, converts at 90% of VWAP; **13% and 85% if revenue conditions fail**), AMD equity $2.5bn left. Amazon's notes ($6.2bn principal at 30 Sep, 1,840.4m shares in all) convert only up to a 12% ownership cap that Amazon did not waive: $0.58bn (276.8m shares) converts at the IPO, the rest (1,563.6m shares) rolls over and converts quarterly as the cap allows, or is repaid in 2034–35.

**The offer (p. S-5–S-7, 202–223) [F]:** 801.4m new Class A + 23.6m sold by the seven co-founders (3.4m each) + up to 123.75m over-allotment; net proceeds **$84.6bn** at $74 ($93.7bn with the option), of which $58.6bn from the offering and **$26.0bn from the concurrent Class N placement** at the IPO price: Google $10.0bn, **NVIDIA $10.0bn**, AMD $2.5bn, Broadcom, Micron and Microsoft $1.0bn each, TSMC $0.5bn. Use: general corporate purposes incl. compute and infrastructure; $3.8bn for RSU tax withholding. Directors' indications up to $303m (incl. a $300m donor-advised fund linked to Reed Hastings). EU retail tranche ≤ 80.1m shares; orders below $70 receive nothing; **unlimited orders are valid up to $120**.

**Governance (p. S-1–S-2, S-4–S-5, 160–161, 255–257) [F]:**
- **Long-Term Benefit Trust** (five financially disinterested trustees) holds Class T and elects a **board majority**; **Founder LLC** (the seven co-founders) holds one Class F share with **50.1% of the votes** on all ordinary matters. Class A votes are capped at 49.9% in total (44.5% for today's holders after the offering), so **Class A holders cannot decide any vote**. Nasdaq "controlled company".
- **PBC duty:** the board must balance stockholders' pecuniary interests against the public-benefit purpose. Public-benefit spending (donation matching $2.1bn in 9M-26) is expected to rise.
- **Anthropic Public Benefit Fund** holds 846.8m Class N (6.5% after the deal), may sell or donate them; the board may add **2% of outstanding shares each time the price rises 50%** from the IPO price (90 of 120 trading days). Donation matching: 553.4m shares owed on vested-award pledges, reserve +1% a year 2027–36. Co-founders pledge 80% of their equity to philanthropy.

**Lock-ups (p. 84–85, 215–221) [F]:** employees may sell 10% from day one (~316m shares), +35% after the FY26 results; other holders release in steps from day 27 (15 Dec 2026), 48 (5 Jan 2027), 62 (19 Jan), 76 (2 Feb) and after the FY26 results; general expiry at the Q1-27 results or day 180 (**17 May 2027**); up to 3.3bn shares can trade before then. Holders above 0.5% and the co-founders are locked to the Q3-27 results or day 365 (**18 Nov 2027**), with staged releases (founders 29% from day 180). The $26bn placement is **not locked up** (restricted, with registration rights).

## Near term: stub (all scenarios)

| Q4-26E [A] | Revenue | Compute (%) | Other cash opex | Adj. operating income | Interest | Capex | FCF |
|---|---|---|---|---|---|---|---|
| $bn | 21.5 (+27% q/q) | 13.0 (60%) | 5.5 (26%) | 3.0 (14%) | 1.5 | 3.0 | **+1.3** |

- 2026 revenue **$54.7bn** (AI BBB build ~55, Q4 21.7: −1%); 2026 compute ~$31.8bn. Q4 is held below the AI BBB build for the late-December code-freeze dip (−20% in two weeks last year, p. 160), enforcement and price cuts.
- **Net cash bridge:** cash and short-term investments 30 Sep $131.8bn + net proceeds $84.6bn − RSU tax $3.8bn = $212.7bn as further adjusted at $74 [F] + over-allotment $9.05bn [A] = **$221.7bn at closing** ($12.22 per share) + Q4 FCF $1.3bn = **$223.0bn at 31 Dec** ($12.30). Each $1 on the IPO price moves cash by $0.79bn [F].
- **Dates:** offer ends 18 Nov 16:00 CET, price and results on ipo.anthropic.com; first trade **19 Nov**; closing and placement **20 Nov**; over-allotment window to ~18 Dec; lock-up steps from 15 Dec; FY26 results date not given [?].

## Market input (AI BBB rows and how they enter)

| AI BBB row (11 Nov) | Bear / Base / Bull | How it enters |
|---|---|---|
| E1 frontier-lab revenue (OpenAI + Anthropic) 2027–29 | 155/170/187 · **190/275/360** · 230/370/515 | Revenue = E1 × own share (55 / 58 / 62%); 2026 ~100 (build 94) |
| Scenario definitions and catalysts | Financing break · digestion · agentic adoption | Bear and Bull stories; compute lapses in Bear (conditional contracts), extra capacity in Bull |
| E-layer and T-layer exit P/E | E 17 / 21 / 23.5; T 15 / 20 / 24 | Anchor for the exit P/E (premium explained under V_T) |
| Lab financing signpost (Anthropic pricing ~18 Nov) | Pulled or below Series H / in range / well above | Pricing inside the range crosses the AI BBB Bull line; P_k sits at the Series H price |
| K1 capex, H rows | 950/800/820 · 1,120/1,170/1,170 · 1,300/1,550/1,700 | Context: Anthropic's commitments are inside the K4 backlogs of Google, Amazon and Microsoft |

Equity BBB (6 Nov): World exit P/E 15 / **17** / 18.5, exit P/B 2.47 / **3.17** / 3.74, mid-cycle return 7.1 / **8.2** / 8.7%; USD/NOK Base flat, Bear +12% / +9% / +9%, Bull −3%. World Base window 6.6%, AI E basket 8.6% (NOK, AI BBB).

## Common assumptions

**Fully diluted shares at $74 (millions) [F] unless tagged:** outstanding at the last practicable date 11,966.4 (Class A 6,630.2, Class N 5,336.2, incl. the 846.8 Public Benefit Fund shares, legally outstanding though excluded from accounting EPS) + new Class A 801.4 + over-allotment 123.75 [A, assumed exercised] + placement 351.4 ($26.0bn ÷ $74) + **Amazon notes not converted at the IPO 1,563.6** + options 1,774.3 at $2.91 (1,704.6 net, treasury method) + unvested RSUs 1,073.7 (incl. 47.0 granted after September) + vested matching obligation 553.4 = **18,138.2** (18,154.3 at $70; 18,123.8 at $78). Issued only: 13,242.9.
- RSUs and options count gross with no cash cost (net settlement at a 50.9% withholding rate is the same value paid in cash). The $26.2bn of unrecognised SBC belongs to awards already counted, so it is not deducted again.
- **Dilution after the IPO [A]:** new grants 3% of revenue a year at the path price; further donation matching 0.5% a year; PBF milestones 2% each (Bull: $111 and $166.5 reached). Exit shares 18,758m / **18,588m** / 19,312m.
- Draws on the Amazon and Google NPAs are at the 30-day VWAP: value-neutral, not modelled. The Broadcom NPA (90% or 85% of VWAP) is a Bear risk, not drawn in the model (cash suffices).

**Costs and cash [A]:** compute in the window as in the scenario table (contracts, less lapses in Bear and Base, plus extra in Bull, never below the ratio needed to serve revenue: 62 / 60 / 57% in Base); other cash opex (personnel cash, channel fees, other ex donations) 25 / 23 / 21% of revenue in Base (Q3-26: 27%); owned-infrastructure capex depreciated over 5 years inside compute; cash on hand earns 3.75% (SOFR 3.94% on 5 Nov) [C], 3.0% in Bear; cash tax 0 / 5 / 12% of positive pre-tax profit in 2027–29 (RSU-vesting deductions, losses carried forward), 21% in exit earnings. SBC and non-cash donations are excluded from FCF and enter through the share count; normalised SBC (4% of revenue in Base) is deducted in exit earnings.

## Period tables and year-end path

| $bn | Bear 2027 / 28 / 29 | **Base 2027 / 28 / 29** | Bull 2027 / 28 / 29 |
|---|---|---|---|
| Revenue | 85.3 / 93.5 / 102.9 | **110.2 / 159.5 / 208.8** | 142.6 / 229.4 / 319.3 |
| E1 share | 55% | **58%** | 62% |
| Compute and infrastructure | 75 / 100 / 108 | **77 / 115 / 135** | 92 / 145 / 172 |
| Adjusted operating income | −11.9 / −29.9 / −29.8 | **5.7 / 7.8 / 30.0** | 16.4 / 33.9 / 83.4 |
| Interest income / cash tax | 6.7 / 6.1 / 5.3; 0 | **8.4 / 8.2 / 8.2; 0 / 0.8 / 4.6** | 8.4 / 8.2 / 8.6; 0 / 2.1 / 11.0 |
| Capex (D&A added back) | 15 / 6 / 4 (0.6 / 3.6 / 4.8) | **20 / 20 / 15 (0.6 / 4.6 / 8.6)** | 30 / 35 / 30 (0.6 / 6.6 / 13.6) |
| FCF ($bn / per share) | −19.6 / −26.2 / −23.7 (−1.08 / −1.44 / −1.31) | **−5.4 / −0.2 / 27.1 (−0.30 / −0.01 / 1.50)** | −4.7 / 11.6 / 64.6 (−0.26 / 0.64 / 3.56) |
| Net cash at year end ($bn / per share) | 203.4 / 177.2 / 153.5 (11.21 / 9.77 / 8.46) | **217.6 / 217.4 / 244.6 (12.00 / 11.99 / 13.48)** | 218.4 / 230.0 / 294.6 (12.04 / 12.68 / 16.24) |

Per share on the 18,138m fully diluted shares at $74; net cash per share at exit on exit shares is in the decision table.

**Year-end path** (D_t = 0; interim marks: the entry-implied P/E of 51.5x on Base 2027 normalised NOPAT glides to the exit P/E; diagnostic only)

| | Bear V_t / r_t | **Base V_t / r_t** | Bull V_t / r_t |
|---|---|---|---|
| End-2026 (stub, same in all) | 74.1 / +0.1% | **74.1 / +0.1%** | 74.1 / +0.1% |
| End-2027 | 33.3 / −55.1% | **84.6 / +14.2%** | 144.6 / +95.2% |
| End-2028 | 25.5 / −23.3% | **87.9 / +3.9%** | 164.6 / +13.8% |
| End-2029 (V_T) | 16.5 / −35.5% | **83.1 / −5.4%** | 173.2 / +5.2% |
| IRR to 2027 / 2028 / T | −51.2% / −39.6% / −38.3% | **+12.7% / +8.5% / +3.8%** | +82.6% / +46.0% / +31.4% |

The Base path looks good in 2027 only because the mark still carries the entry multiple; the multiple compresses as growth slows, so the last year loses value.

## V_T build and exit checks

**V_T = exit P/E × normalised 2030 NOPAT + net cash at exit − commitment overhang, ÷ exit shares.**

| $bn | Bear | **Base** | Bull |
|---|---|---|---|
| 2030 revenue (growth) | 111.1 (+8%) | **254.7 (+22%)** | 415.1 (+30%) |
| Normalised EBIT margin → NOPAT (21% tax) | 16% → 14.0 | **25% → 50.3** | 31% → 101.7 |
| × exit P/E → EV | 15 → 211 | **26 → 1,308** | 30 → 3,050 |
| + net cash at exit | 153.5 | **244.6** | 294.6 |
| − commitment overhang | 55.2 | **7.4** | 0 |
| = equity ÷ exit shares | 309 ÷ 18,758m | **1,545 ÷ 18,588m** | 3,344 ÷ 19,312m |
| **V_T** | **16.5** | **83.1** | **173.2** |

**Exit P/E, Base 26 [A]:** the AI BBB E-layer exit P/E is 21 and World 17. Anthropic in 2030 still grows ~20% (Base +22%, 2031 +18%) with margin expansion ahead, against ~10% for the platforms, so a premium of 5 points is given; for reference, Microsoft trades at a core P/E of 24.1 on ~15% growth and Alphabet's 5-year forward-P/E median is 20.8 (15.6–31.7) [C]. Bear 15 (World Bear; growth stalled, contracts overhang), Bull 30.

**Exit consistency** (Year 3 = 2029 against the normalised 2030 economics; material if the gap > 10%)

| Row | Scenario | 2029 compute (adj. margin) | Normalised | Treatment | Per share |
|---|---|---|---|---|---|
| Compute ratio and margin | Bear | 105% (−29%) | 58% (21%) | Contracts firm today count for their full term (backlog rule): excess of paid (80% of the schedule) over need, 2030–33, 50% resold, no tax shield, at 8% | −$2.94 |
| | **Base** | **65% (14%)** | **52% (29%)** | **Named reason [F]: the contract schedule flattens after 2029 ($451.6bn before end-2030, the rest spread over 2031–45) while revenue grows 22%; the residual 2030 excess ($8.0bn after tax) is deducted** | **−$0.40** |
| | Bull | 54% (26%) | 48% (34%) | Named reason: committed 2030 compute ($155bn) is below the need ($199bn); no excess | 0 |

Other treatment as a sensitivity: the skill's 2-year tail on the Base margin gap (−$26.7bn after tax instead of −$7.4bn) gives V_T $82.1, **IRR 3.4%, P_k $57.7**; no overhang at all gives 4.0%, $58.7.

**Exit cross-check**

| | Bear | **Base** | Bull | World (Equity BBB) Bear / Base / Bull |
|---|---|---|---|---|
| Exit P/E: EV ÷ NOPAT / equity incl. interest | 15 / 17.5 | **26 / 26.8** | 30 / 30.3 | 15 / 17 / 18.5 |
| EV ÷ 2030 revenue | 1.9x | **5.1x** | 7.3x | — |
| Exit P/B (book incl. converted Amazon notes) | 1.7 | **5.2** | 8.8 | 2.47 / 3.17 / 3.74 |
| Buyer's implied return (0.7 × earnings yield + long-run growth 4 / 7 / 8%) | 8.0% | **9.6%** | 10.3% | 7.1 / 8.2 / 8.7% |

The Base buyer at exit earns more than the World mid-cycle return (9.6% against 8.2%), so the exit is not stretched; the P/B above World reflects an asset-light, high-return business.

## Growth capex test

Growth investment = compute expensed above the normalised ratio in 2027–29 + capex (incl. the stub) + committed excess after exit; ΔNOPAT = 2030 normalised NOPAT − 2026 revenue at the same margin [A].

| | Bear | **Base** | Bull |
|---|---|---|---|
| Growth investment $bn | 274 | **146** | 175 |
| ΔNOPAT $bn a year | 7.1 | **39.5** | 88.2 |
| ROIC_g vs k = 12% | **2.6%: destroys value** | **27%: accretive** | 50%: accretive |
| Value created ≈ investment × (ROIC_g ÷ k − 1) | −$214bn | **+$183bn** | +$560bn |

Evidence: revenue per dollar of compute rose from 0.40x to 1.72–2.08x in six quarters [F]; Base needs 1.92x by 2030, Bear stays at ~1x in 2028–29. In Base the compute build earns well above k; the shareholder at $74 still fails because the price pays for the build in advance. In Bear the commitments turn growth spending into a value transfer to the compute suppliers.

## Results

| | Bear | **Base** | Bull |
|---|---|---|---|
| IRR_T (dated, to V_T) | −38.3% | **3.8%** | 31.4% |
| IRR_T in NOK on the Equity BBB NOK path | −36.5% | **3.8%** | 30.1% |
| Rule 1 screen d + g at constant P/E | n/m: EPS base near zero (2027 core EPS $0.05), hygiene rule 3 | **n/m** | n/m |
| d / g / c | 0 / −38.3% / 0 | **0 / 3.8% / 0** | 0 / 31.4% / 0 |
| g: re-rating / NAV growth | n/a (Track A; the multiple effect is in the return bridge) | **n/a** | n/a |
| Structural / cyclical | n/a: no rate cycle; the commitment overhang is the cyclical element (Base without it 4.0%) | **n/a** | n/a |
| ΣD_t / V_T | 0 / 16.5 | **0 / 83.1** | 0 / 173.2 |
| P_k / margin of safety | 11.6 / −84.4% | **58.4 / −21.1%** | 121.7 / +64.4% |
| Rule 3: P/E on 2030 normalised EPS vs ceiling IRR_T ÷ k² | 98.9x vs negative | **27.3x vs 2.6x: fails** | 14.1x vs 21.8x |
| Capital preserved? V_T vs P | No, −77.7% | **Yes, +12.3%** | Yes, +134% |

**Sensitivities (Base at $74: IRR / P_k / margin of safety)**

| Change | Result | Change | Result |
|---|---|---|---|
| Exit P/E 21 (E layer) | −2.0% / 48.8 / −34.0% | Exit P/E 30 | 8.0% / 66.1 / −10.7% |
| Exit P/E 24 (governance discount −2) | 1.6% / 54.6 / −26.3% | E1 share 50% / 65% | −1.7% / 49.2 / −33.5%; 8.1% / 66.2 / −10.5% |
| Normalised compute 48% / 56% | 8.0% / 66.1 / −10.7%; −0.8% / 50.7 / −31.5% | Window compute ±15% | 2.8% / 56.6; 4.7% / 59.9 |
| No dilution after the IPO | 4.6% / 59.9 / −19.1% | Cash yield 3.0% | 3.7% / 58.2 / −21.3% |
| E1 Bull revenue, Base costs and P/E | **20.0% / 91.9 / +24.1%** | Aftermarket entry $90 / $100 | −2.1% / −5.1% (P_k $59.2 / $59.7) |
| Bear at 58% share / at exit P/E 21 | −36.4% / −33.2% | | |

- **What the price needs (reverse test, $74):** an exit P/E of **34.1**, or normalised compute at **44%** of revenue (EBIT 33%), or **73% of E1** (2029 revenue $264bn, 2030 $322bn). Each is a Bull-side assumption; none is in the AI BBB Base.
- **Scenario-weighted reference (convention 25/50/25 on V_T levels):** V_T $89.0, IRR 6.1%. Not the decision.
- **Share of Bull already priced:** (74 − 58.4) ÷ (121.7 − 58.4) = **25%**.
- **Bear balance-sheet survival:** net cash falls from $223bn to $153bn by end-2029; revolver $15bn undrawn; covenant ($5bn liquidity) far away. If unvested RSUs are net-settled at Bear prices, withholding costs ~$16bn more [A]. The Broadcom NPA ($42bn at 13% PIK, 85% of VWAP) and the VWAP NPAs are dilutive fall-backs. True-ups make Google and Amazon capacity payable whether used or not. **The company survives; the equity is the shock absorber.**

## Verdict and caveat

- Band: **clears** above +2%, **marginal** −2% to +2%, **fails** below −2% on the Base margin of safety. At $70–78 the margin is −17% to −25%: fails (verdict in the Summary).
- **What flips it:** an IPO price at or below **$56.3** (+2% band); or evidence that Anthropic's E1 share heads to ~70% (Q4-26 and 2027 revenue against the 58% path: Base needs $110bn in 2027; ~$130bn would point that way); or compute efficiency reaching ~2.3x revenue per compute dollar with the contracts in place. A cut in contracted compute without a revenue cut moves Base up ~1 pp per 15%.
- **Caveat:** a margin-of-safety screen, not an intrinsic valuation or a price target. The revenue share, compute schedule, normalised margin and exit P/E are own assumptions [A]; the scenario paths for the lab market come from the AI BBB.
- **Practical for a Norwegian retail order:** the EU retail tranche fills at the single final price, up to $120 for unlimited orders; a limit order at the hurdle (~$57, below the range) would receive nothing. The FX cost (NOK → USD) comes on top.

## Risks and signposts

| Risk | Why it matters | Signpost (Bear / Bull) | Next |
|---|---|---|---|
| **Commitments vs revenue** | $900.9bn + $150–175bn of compute against $68bn annualised revenue; true-ups bind | Compute > 75% of revenue two quarters in 2027 / compute efficiency > 2.0x with revenue ahead of the 58% path | FY26 results; Q1-27 |
| Competition and price | Google, OpenAI; price cuts −$600m in Q3; > 80% of revenue from models < 6 months old | Revenue growth < 10% q/q twice (AI BBB lab run-rate line) / > 20% q/q into H2-27 | Each quarter |
| Customer and channel concentration | Top five 25% of 9M revenue; CSPs bill 44%; VC-funded coding customers | Top-five share up, a top customer lost / top-five share < 15% | Prospectus metrics in each report |
| Suppliers are owners and rivals | Google, Amazon, Microsoft, NVIDIA, Broadcom fund, supply and compete | A partner reprices, delays or withdraws capacity / new independent financing | Ongoing |
| Governance (not in the valuation) | LTBT board majority, Class F 50.1%, PBC balancing duty: Class A cannot change control or strategy; public-benefit spending can rise | PBF issues beyond the framework, larger donations / none | Proxy, 2027 |
| Dilution and supply | PBF 846.8m + 2% per +50%; donation matching; options; lock-up steps; 3.3bn shares before day 180; placement unlocked | Lock-up releases with the price below the IPO / absorbed above it | 15 Dec 2026 – 18 Nov 2027 |
| IPO mechanics | First-day pop raises the aftermarket price (Base −2.1% at $90); price may be set above the range | Priced above $78 or first trade > $90 / priced at the low end | 18–19 Nov |
| Safety, regulation, litigation | Release delays (Mythos, Fable 5), liability for misuse, Bartz-type settlements ($1.5bn in 2025) | Release restricted or a large claim / none | Ongoing |

## For other modules

| Value | Bear | **Base** | Bull |
|---|---|---|---|
| Anthropic revenue $bn 2026 / 2027 / 2028 / 2029 / 2030 | 54.7 / 85.3 / 93.5 / 102.9 / 111 | **54.7 / 110.2 / 159.5 / 208.8 / 255** | 54.7 / 142.6 / 229.4 / 319.3 / 415 |
| Implied share of E1 (2026: ~58% of the AI BBB build of 94) | 55% | **58%** | 62% |
| Compute and infrastructure spend $bn 2027 / 28 / 29 | 75 / 100 / 108 | **77 / 115 / 135** | 92 / 145 / 172 |
| V_T / P_k per share ($74 deal) | 16.5 / 11.6 | **83.1 / 58.4** | 173.2 / 121.7 |
| Equity value at P_k: fully diluted / issued | | **$1,059bn / $773bn** | |

**Stakes** (pre-tax, USD bn; shares [F]: Amazon 1,920.5m Class N + 1,563.6m in unconverted notes = 3,484.1m; Google 1,654.5m + the $10bn placement; NVIDIA the $10bn placement)

| Holder | at $70 | at $74 | at $78 | at P_k $58.4 (shares of the $74 deal) |
|---|---|---|---|---|
| Amazon (3,484.1m) | 243.9 | 257.8 | 271.8 | 203.5 |
| Alphabet (1,797.3m / 1,789.6m / 1,782.7m) | 125.8 | 132.4 | 139.0 | 104.5 |
| NVIDIA placement (142.9m / 135.1m / 128.2m shares) | 10.0 | 10.0 | 10.0 | 7.9 |
| AMD 2.5; Broadcom, Micron, Microsoft 1.0 each; TSMC 0.5 (placement, at cost) | | | | × 0.79 at P_k |

- **ai-market-bbb:** E1 share and the 2026 Anthropic revenue ($54.7bn, Q4 $21.5bn [A]); the commitment schedule (~$77 / 125 / 147bn in 2027–29) as lab demand inside K4; the placement split is now [F] (NVIDIA $10.0bn, Microsoft $1.0bn): the K3 vendor-financing row. Lab financing signpost at pricing.
- **amzn / googl:** the stake rows above; Amazon's claim includes the notes that stay outstanding after the IPO. **nvda:** the $10bn placement stake; Anthropic's NVIDIA-GPU capacity via SpaceXAI, Nscale, Lambda and Microsoft. **msft:** Anthropic's ≥ $47.2bn Azure commitment (Nov 2026–Jun 2033) for E2, the $1bn placement. **tsm / mu:** placement only, immaterial.

## Change log

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
| Dilution after the IPO | Grants 3% of revenue; matching 0.5% a year; PBF 2% per +50% | Plans and framework [F]; issuance [A] |
| Q4-26 stub | Revenue 21.5, compute 13.0, other 5.5, capex 3.0, interest 1.5 | Q3 run-rate, seasonality, SpaceXAI full from December |
| Over-allotment | Exercised (123.75m, $9.05bn) | Demand indications |

## Appendix: sources

| # | Source | Used for | Date |
|---|---|---|---|
| S1 | Anthropic, PBC — EU retail prospectus approved by Bafin (user file `bafin-prospectus.pdf`, 307 pages; printed page = PDF − 10): Summary S-1–S-7; Risk factors 1.1.18–1.1.19 (p. 29–31), 1.6.6 (p. 84–85); MD&A 5.2–5.12 (p. 152–192); Offer 8.6–8.8 (p. 215–225); Shareholders 11.1 (p. 255–257); Dividend policy (p. 291) | All [F] values: financials, metrics, commitments, NPAs, capitalization, offer, lock-ups, governance | 11 Nov 2026 (data to 30 Sep 2026 and the last practicable date) |
| S2 | EU summary (user file `summary-eu-prospectus.pdf`, 7 pages) | Cross-check of the summary tables, share counts, timetable: identical to S1 S-1–S-7 | 11 Nov 2026 |
| S3 | `docs/ai-market-bbb.md` (Interface, Engines notes, Scenario definitions, K4 memo, signposts) | E1 paths, scenarios, layer exit P/Es, Series H per common share $58.90 [C], lab financing signpost | 11 Nov 2026 |
| S4 | `docs/equity-market-bbb.md` (Interface) | World exit P/E, P/B, mid-cycle return, USD/NOK path, SOFR 3.94% | 6 Nov 2026 |
| S5 | `docs/hy-market-bbb.md` (Interface, rates) | Rate context only | 5 Nov 2026 |
| S6 | `docs/amzn-analysis.md`, `docs/googl-analysis.md`, `docs/nvda-analysis.md`, `docs/msft-analysis.md` (grep only) | Stake cross-checks (Amazon ~3,480m as converted; Google 1,654.5m), USD/NOK 9.5610, peer P/Es [C] | 7–12 Nov 2026 |
| S7 | Model `.claude/skills/iaf-valuation/references/models/anthropic/` (`model.py`, `report.py`, `drivers.py`) | Every computed figure | 13 Nov 2026 |

Not available: the audited financial statements and notes (incorporated by reference; Note 8 cost of revenue and gross margin, Note 13 commitments by year) [?]; capex for 9M-26 as a line [?]; the FY26 results date [?]; analyst consensus (none before the IPO); a live USD/NOK quote (one day old).
