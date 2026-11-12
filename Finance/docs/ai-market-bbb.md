# AI Market BBB — baseline 1 Nov 2026; K1 capex cycle re-run 11 Nov 2026

**Status (as of 11 Nov 2026; compacted 12 Nov):** skill `ai-market-bbb` 2026-11-11.2. Last change, 11 Nov (Option D of `docs/review-ai-k1-sustainability.md`): K1 Base 2028–29 set to a digestion plateau (1,170 / 1,170) and carried into H1, H4, the E cash conversion and the monetisation ratio. Prices are the 6 Nov close, not re-marked. The 12 Nov compaction changed no value.

## Interface (values other documents read)

As of **11 Nov 2026** (paths) and the **6 Nov 2026 close** (prices; consensus 7 Nov, calendarised; stub 54 days, 7 Nov–31 Dec; exit 31 Dec 2029). USD bn unless stated; cells Bear / **Base** / Bull; 2026 is the same in every scenario. Tags: `[F]` fact · `[E]` external forecast or secondary · `[A]` own assumption · `[?]` unknown.

**Paths**

| Row | 2025 | 2026 | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| **K1** Hyperscaler capex (MSFT, GOOGL, AMZN, META, ORCL) | ~435 `[A]` | **790** `[E]` | 950 / **1,120** / 1,300 | 800 / **1,170** / 1,550 | 820 / **1,170** / 1,700 |
| K1 growth y/y | | ~+84% | +20% / **+42%** / +65% | −16% / **+4.5%** / +19% | +3% / **0%** / +10% |
| K1 Base range | | 770–810 | 1,050–1,200 | 1,000–1,350 | 950–1,400 |
| **H1** Compute (accelerators + AI networking silicon) | | **~470** `[A]` (440–490) | 585 / **730** / 820 | 470 / **750** / 985 | 490 / **745** / 1,080 |
| H1 growth y/y | | | +25% / **+55%** / +75% | −20% / **+3%** / +20% | +5% / **−1%** / +10% |
| **H2** Memory revenue, index (2026 average = 100; Q4-26 run-rate ≈ 130) | | 100 | 100 / **138** / 150 | 72 / **118** / 133 | 67 / **103** / 118 |
| **H3** Foundry, packaging, equipment, index (TSMC Q4-26 run-rate ≈ 121) | | 100 | 110 / **125** / 132 | 99 / **140** / 156 | 104 / **151** / 175 |
| **H4** Networking and DC infrastructure, index | | 100 | 110 / **125** / 135 | 88 / **129** / 159 | 88 / **130** / 175 |
| **H5** Power: a constraint row, no path | | US needs ~68 GW new 2026–28, ~30 GW covered `[E]` | — | — | — |
| **E1** Frontier-lab revenue (OpenAI + Anthropic, booked) | ~18 `[E]` | **~100** `[A]` (90–110) | 155 / **190** / 230 | 170 / **275** / 370 | 187 / **360** / 515 |
| E1 exit run-rate (memo) | | ~150 `[A]` | | | |
| **E2** Hyperscaler cloud revenue growth (AWS, Azure, GCP, OCI; run-rate ~420bn `[A]`) | | **~+50%** `[A]` | +25% / **+38%** / +45% | +8% / **+25%** / +32% | +8% / **+18%** / +22% |
| **T1** M365 Copilot paid seats, m (year-end) | ~15 `[E]` | ~40 `[A]` (30 in Jul `[E]`) | 45 / **60** / 80 | 55 / **95** / 140 | 65 / **130** / 200 |
| **T2** AI-native tools revenue growth | | | +35% / **+80%** / +120% | +10% / **+45%** / +60% | +10% / **+30%** / +40% |
| **T3** Incumbent application software revenue growth | | ~+10% | +3% / **+8%** / +11% | 0% / **+7%** / +11% | +3% / **+7%** / +10% |
| **T4** US firms using AI (Census BTOS, year-end) | | ~22% `[E]` | 23% / **26%** / 30% | 25% / **30%** / 38% | 27% / **35%** / 45% |
| Monetisation ratio (E1 ÷ K1) | 0.04 | **0.13** | 0.16 / **0.17** / 0.18 | 0.21 / **0.24** / 0.24 | 0.23 / **0.31** / 0.30 |
| **K1 return gauge**, Base: coverage of the revenue needed for 10% pre-tax | 104% | 108% | **84%** | **70%** | **63%** |
| K1 return gauge, Base: pre-tax return on AI net assets | 10.9% | 11.9% | **6.2%** | **2.5%** | **0.2%** |

**Layer EPS paths and exit P/E** (CY27 consensus = 1.00; all `[A]`; the exit P/E is a reference, never the IAF ceiling)

| Layer | Bear 2027 / 28 / 29 / 2030 norm | **Base** | Bull | Exit P/E Bear / **Base** / Bull | Payout | Cash conversion c 2027 / 28 / 29, Base (Bear; Bull) |
|---|---|---|---|---|---|---|
| H1 Compute | .68 / .50 / .53 / .57 | **.92 / .91 / .88 / .87** | 1.00 / 1.15 / 1.25 / 1.30 | 13 / **17** / 19 | 25% | .80 / .90 / .90 (.85 / .95 / .95; .75 / .85 / .90) |
| H2 Memory | .60 / .30 / .25 / .25 | **.90 / .60 / .40 / .35** | 1.00 / .80 / .55 / .45 | 8 / **10** / 11 | 15% | .70 / .65 / .60 (.70 / .75 / .70; .70 / .70 / .55) |
| H3 Foundry and equipment | .76 / .63 / .67 / .71 | **.95 / 1.03 / 1.10 / 1.16** | 1.00 / 1.15 / 1.28 / 1.40 | 14 / **18** / 21 | 45% | .75 / .80 / .82 (.75 / .90 / .95; .70 / .72 / .78) |
| H4 Networking and DC infra | .75 / .54 / .56 / .65 | **.95 / .94 / .94 / .99** | 1.00 / 1.12 / 1.22 / 1.30 | 15 / **20** / 24 | 35% | .90 all |
| E Platforms | .82 / .75 / .82 / .91 | **.92 / 1.07 / 1.17 / 1.27** | 1.00 / 1.19 / 1.37 / 1.54 | 17 / **21** / 23.5 | 34% | **−.20 / .11 / .36** (−.10 / .30 / .50; −.30 / −.20 / .00) |
| *E rest: Meta, Oracle (memo; 17% of E on 30 Oct)* | *.88 / .88 / .97 / 1.05* | *.97 / 1.07 / 1.17 / 1.27* | *1.00 / 1.13 / 1.27 / 1.41* | | | *used for the unanalysed share* |
| T Software | .88 / .85 / .93 / 1.00 | **.95 / 1.03 / 1.11 / 1.19** | 1.00 / 1.10 / 1.20 / 1.30 | 15 / **20** / 24 | 45% | .80 all |

**Layer baskets** (IAF at index level, before fees and tax; NOK unless stated; method v2.1; E / R against the HY market reference 0.254; reproduced by `references/model.py`)

| Basket | Mcap USD tn | P/E CY27 | Cons. EPS CY26→27 | IRR NOK Bear / **Base** / Bull | Base USD | 2027 return NOK Bear / Base / Bull | Hurdle P/E / MoS | E / R / **ratio** | Implied EPS growth 2028–30 for 12% |
|---|---|---|---|---|---|---|---|---|---|
| H1 Compute | 6.77 | 13.7 | +74% | -10.3 / **7.5** / 24.1 | 7.5 | -42.1 / 3.7 / 31.3 | 12.1 / -11.8% | 3.13 / 45.8 / **0.068** | 3% |
| H2 Memory | 2.27 | 2.64 | +55% | 5.3 / **21.6** / 33.5 | 21.6 | 19.9 / 39.8 / 85.6 | 3.38 / **+28.1%** | 17.24 / 19.9 / **0.867** | -35% |
| H3 Foundry and equipment | 3.01 | 17.3 | +34% | -9.5 / **10.2** / 20.9 | 10.2 | -39.2 / 8.5 / 23.5 | 16.5 / -4.7% | 5.87 / 47.7 / **0.123** | 9% |
| H4 Networking and DC infrastructure | 0.42 | 24.3 | +29% | -19.5 / **-2.7** / 10.6 | -2.7 | -59.5 / -8.0 / 11.9 | 15.8 / -35.1% | -7.04 / 51.5 / **-0.137** | 18% |
| E Engines and cloud platforms | 12.17 | 21.0 | +18% | -5.7 / **8.6** / 17.6 | 8.6 | -32.3 / 6.2 / 18.8 | 19.1 / -9.1% | 4.21 / 38.5 / **0.110** | 15% |
| T Tools and application software | 1.29 | 23.5 | +26% | -7.2 / **3.7** / 11.5 | 3.7 | -35.9 / 1.1 / 10.8 | 18.6 / -21.1% | -0.71 / 37.0 / **-0.019** | 17% |
| **All six, cap-weighted** | 25.92 | | | ≈ -6.7 / **≈9.2** / ≈20.7 | 9.2 | ≈ -31.7 (Bear 2027) | | | |

Weights: E 47%, H1 26%, H3 12%, H2 9%, T 5%, H4 2%. Base USD = NOK in Base (flat USD/NOK path).

**References, gauges and price-implied paths**

| Item | Value | Source |
|---|---|---|
| HY market reference E / R (the HY reference used) | **0.254** (E 2.15 pp after a 0.6% fee, R 8.47 pp; 0.216 with the Bear read as a shock) | HY BBB 5 Nov, kept 11 Nov |
| Nordic HY market Base / Bear 2027; NIBOR window | 7.2% / −0.4%; NIBOR **4.38%** | HY BBB 5 Nov |
| MSCI World Base / Bear 2027 / E / R; exit P/E, mid-cycle return, long-run growth | 6.6% / −18.3% / 0.080; 17, 8.2%, 5.3% | Equity BBB 6 Nov |
| USD/NOK path | Base 9.29 flat; Bear 10.41 / 10.14 / 10.14 (+12 / +9 / +9%); Bull 9.02 (−3%) | Equity BBB 6 Nov |
| **Memory (H2) price-implied path** | Basket earns k at **0.75×** Base 2028–30 (.45 / .30 / .26), 0% at 0.49×. SK hynix **0.57×** (0% at 0.37×), Samsung **0.68×** (0.44×), Micron **1.08×** (0.72×) | `impl.py` |
| Memory capped-Bear diagnostic | H2 Bear −15.2% a year, Bear 2027 −48.5%, E / R **0.195**; all six Bear −8.5%, Bear 2027 −37.7% | `model.py BEARCAP` |
| Compute and platform price-implied paths | H1 basket k at **1.14×** Base 2028–30 (1.04 / 1.00 / .99), 0% at 0.79×; E basket **1.10×** (1.18 / 1.29 / 1.40), 0% at 0.78× | `impl.py H1`, `impl.py E` |
| K1 return gauge range | Coverage 2028 / 2029 51–79% across the sensitivities; Bear K1 81% / 79%, Bull K1 61% / 50% | `k1ret.py` |

**Signpost states** (neither = no line met; touched = one leg met; Bull-side = leaning, not crossed; pending = dated read-out ahead; detail under Signposts and monitoring)

| Signpost | State | Signpost | State |
|---|---|---|---|
| Next-year capex guidance | neither | K1 2027 first figures (late Jan–early Feb) | pending |
| K1 return gauge (2028 coverage) | neither | GPU rental indices | neither |
| FCF after shareholder returns (five) | neither | K4 backlog q/q | neither |
| E2 four-cloud growth | Bull-side | AWS growth against E2 | Bull-side |
| NVIDIA Q3 FY27 (17 Nov) | pending | NVIDIA supply commitments and working capital | neither |
| TSMC monthly revenue | Bull-side | TSMC Q4 report (mid-Jan) | pending |
| Lab run-rates | neither | Lab financing (Anthropic pricing ~18 Nov) | pending |
| Oracle credit | neither | Capex ÷ OCF and debt share | touched |
| Platform equity funding | **crossed (Bear)** | Vendor financing (flow) | neither |
| Non-K1 compute funding | neither | DRAM contract prices | neither |
| DRAM contract prices in 2H-27 | pending | NAND contract prices | neither |
| Micron SCAs and commitments | neither | Memory LTAs (SK hynix, Samsung) | neither |
| CXMT 4F² DRAM | neither | US data-center siting policy | neither |
| Federal AI and data-center law | neither | M365 Copilot seats | neither |
| BTOS AI use | neither | Basket P/E triggers | memory cleared; others not |
| Asian AI-hardware flows (mood) | neither | TSMC and SKHY ADR premiums (mood) | neither |

## Metadata

- **Runs behind the current values:** baseline 1 Nov 2026 (Europe/Oslo); price re-mark 7 Nov (Update 7: Yahoo regular close Fri 6 Nov for the US, Europe and Korea; consensus Yahoo `earningsTrend` 7 Nov, calendarised); K1 capex cycle re-run 11 Nov (method effect only, no re-mark: the skill re-marks on a sharp sell-off or at a recalibration trigger, and NVIDIA's Q3 on 17 Nov is the next one).
- **Stale after 16 Dec 2026** (45 days from 1 Nov; a re-mark does not restart the clock), or earlier at NVIDIA Q3 FY27 (**17 Nov**) or when the Equity BBB changes its scenarios (stale after 6 Dec). Micron FQ1-27 (16 Dec) is a memory recalibration trigger.
- **Skills:** `ai-market-bbb` 2026-11-11.2; `iaf-valuation` 2026-11-10.1 (method only, read through the company analyses).
- **Source quality:** company figures from their releases and filings, directly or via the company analyses `[F]`; call statements through third-party transcripts `[E]`; memory prices from TrendForce and press coverage of TrendForce, DRAMeXchange, brokers and Korean media `[E]` (no TrendForce report read in full); past-cycle share prices Yahoo and Micron's quarters Alpha Vantage `[F]`.
- **Market only:** compares with World and the Nordic HY market; no portfolio, HY book or fund document is read.

| Input | Date | Used for |
|---|---|---|
| Equity Market BBB (`equity-market-bbb` 2026-10-24.1) | 6 Nov 2026 (stale after 6 Dec) | Scenarios; USD/NOK path; World comparison values |
| Nordic HY Market BBB (`hy-market-bbb` 2026-10-24.1) | 5 Nov 2026, kept in its 11 Nov note (stale after 5 Dec) | NIBOR window, HY market Base and Bear, reference E / R |
| Oil Market BBB | 11 Nov 2026 (Base Brent 2027 84) | Not read directly; it reaches here through the Equity BBB, which has not read it yet |
| `docs/review-ai-k1-sustainability.md` (Option D, user 11 Nov) and its sources S1–S20 | 11 Nov 2026 | K1 capex cycle section |
| `docs/review-ai-h1-non-k1-funding.md` (Option A+, user 11 Nov) | 11 Nov 2026 | H1 buyers outside K1; the "Non-K1 compute funding" signpost |
| Company analyses: `nvda` v1.3 and `tsm` v1.2 (11 Nov), `amzn` v2 (11 Nov re-mark), `msft` v3 and `googl` v2 (7 Nov re-marks), `mu` v3 (5 Nov), `skhynix` v2 (28 Oct), `samsung` v2 (29 Oct) | 28 Oct–11 Nov 2026 | Company check; Q3 facts for K1, K3, K4, E2, H2; their capex as a share of K1 |
| `docs/review-kospi-analysis.md` (section 5); `docs/dnb-teknologi-analysis.md` | 31 Oct–1 Nov 2026 | The user's rule to lead memory with the cycle; the E-layer blend observation (≈ .91) |

## Conclusion

- **K1 Base is a digestion plateau after a contracted 2027:** 790 / 1,120 / 1,170 / 1,170 (2026–29). Both earlier hyperscaler surges ended in a flat year (2019 +4%, 2023 −2%) `[F]`; E2 slows by 25–28 pp from 2026 to 2028 on its own Base; NVIDIA's supply commitments are flat in FY28–29 `[F]`; on the Base E-paths the AI asset base earns ~2.5% pre-tax in 2028 and ~0% in 2029. An absolute cut is the Bear (financing break: 950 / 800 / 820).
- **The layers:** compute +55% in 2027, then +3% and −1%; memory peaks in 2027 and turns in 2028; frontier-lab revenue ~100bn (2026) → 360bn (2029); AI-native tools and copilots grow while seat-based software slows to high single digits.
- **Durability:** the monetisation ratio rises in every scenario (Base 0.13 → 0.31), so it cannot tell a sustainable path from an unsustainable one; the K1 return gauge can (~12% pre-tax in 2026, ~6% in 2027, ~2.5% in 2028, ~0% in 2029). Capex is three to eight times lab revenue and increasingly debt-financed (new debt 32% of capex, LTM); FCF is near zero for three of five. **The main risk is financing, not demand.**
- **Catalysts:** Bear = a financing break (a lab short of its commitments, Oracle and neoclouds renegotiate, AI credit tightens) on top of the equity Bear. Bull = agentic adoption that doubles lab revenue again in 2027 and takes capex to the brokers' upside (~USD 1.4tn).
- **Baskets (Base NOK, 6 Nov prices):** all six **9.2%** (Bear −6.7%, Bull 20.7%). Memory **21.6%** clears its hurdle P/E (+28.1%); for memory the cycle is the gate, and the price discounts a turn ~25% deeper or earlier than Base (k at 0.75×). Foundry 10.2%, platforms 8.6% and compute 7.5% are above World (6.6%); none reaches the HY reference (0.254). Compute earns k only at 1.14× its Base 2028–30, platforms at 1.10×. Networking −2.7%, software 3.7%.
- **Company analyses (own builds, their run prices):** NVIDIA, Micron, SK hynix and Samsung clear; TSMC, Microsoft, Alphabet and Amazon fail (Against World and high yield).

## Money in: K1 notes, K3 financing, K4 backlog

- **2026 (790):** guides Amazon ~220, Alphabet 195–205, Microsoft ~170 (calendar 2026; Q1 FY27 capex 45.2bn incl. 7.4bn of finance leases, third-party capacity slipped into H1 2027), Meta 135–145 (85.8bn in nine months), Oracle ~60–70 `[A]` (FY27 90–95bn, net cash capex capped at 70bn) `[F]`/`[E]`. FactSet "close to USD 800bn including finance leases", Moody's 785 `[E]`; 2025 back-solved from Goldman's +84% `[A]`. Alphabet Q3 PP&E 51.4bn (132.0bn in nine months; 65% servers and networking); Amazon Q3 cash capex $75.9bn ($172.2bn in nine months, leaving ~$48bn for Q4 `[?]`), property and equipment commitments $159.6bn ($63.9bn in 2027), leases not yet commenced $164.9bn.
- **Filings check:** K1 is ~450 (2025) and ~815 (2026, nine-month actuals and Q4 guides; Oracle's calendar 2026 ~85) by filings, against ~435 and 790 here: below the 5% rule, re-set at the January roll-forward. The return gauge uses the filed history (165 / 165 / 262 / 450 for 2022–25).
- **2027 Base +42%:** between consensus (+39%) and Goldman (+54%); 2027 is the only Base year with a contract argument. Contracted: Google Cloud backlog 561bn (just over 55% within 24 months), Microsoft RPO 677bn (~30% within 12 months), AWS 578bn (6.1 years), Amazon's $63.9bn of 2027 commitments, leases not yet commenced $364.6bn (Microsoft) and $164.9bn (Amazon), NVIDIA's supply commitments ~$87–88bn a year in FY28–29 `[F]`. Amazon: 2027 cash capex to "meaningfully increase"; Alphabet: "increase significantly" (consensus ~300–312bn `[E]`); Meta: "continue investing aggressively". No first 2027 figure before late January.
- Context `[E]`: 2027 ~1,100 (five companies; Goldman 25 Sep), big four 934.5; Goldman 1,200, upside 1,400 (2028: 1,400); Morgan Stanley 1,200.
- **2028–29 Base: a plateau at ~1,170** (K1 capex cycle section). **Bear:** 2027 builds continue (contracted, power-limited) but H2-27 orders are cut; 2028 falls 16% as the financing break and the recession bite; 2029 flat `[A]`.

| K3 Financing | Value | Source |
|---|---|---|
| Debt increase ÷ capex (five) | 9% (FY24) → **32%** (LTM to Jun 2026) | FactSet, 23 Jul 2026 `[E]` |
| Total debt (five); off-balance leases | ~USD 700bn; ~820bn | FactSet `[E]` |
| Equity raised | Alphabet **USD 49.6bn net in June** (common 30.5 incl. Berkshire 10; 6.25% mandatory convertible preferred 19.1) + a USD 40bn ATM, of which **12.4bn sold in Q3** (12m Class A for 4.3bn, 24m Class C for 8.1bn, ~$344 a share; **27.6bn left**): more than twice the 5.4bn of employee withholding. Oracle 20bn of common stock (Q1 FY27; FCF −5.4bn, capex 28.5bn against OCF ~23bn). FactSet's 84.75 likely counts ATM capacity `[?]` | Alphabet Q2 and Q3 releases `[F]`; Oracle (Zacks, 27–28 Oct) `[E]` |
| Buybacks | Alphabet none in 2026 to date (H1 2025: 28.3bn; share count +~0.9% a year in its Base); Amazon none since 2022; Microsoft still buys back (22.3bn FY26) | Releases `[F]`; `docs/googl-analysis.md` |
| Bonds | Alphabet: USD 25bn + A$5.5bn (Aug) after 31.1bn (Q1) and 20.3bn (Q2); Q3 28.7bn net, 3.6bn repaid; long-term debt **125.1bn** (end-2025 46.5bn). Amazon: ~92bn of notes in 2026 (incl. 25bn in July) | 8-K, Cleary `[F/E]`; Q3 releases `[F]` |
| Alphabet cash flow and commitments | Q3 FCF **−9.1bn** (consensus −2.7bn `[E]`; ≈ −3.9bn before the 5.2bn EC fine); capex **121% of OCF** (51.4 / 42.3); working capital −17.4bn (TPU inventory 13.3bn); TTM FCF 19.7bn. Purchase commitments **924bn** + 152bn of pre-commencement leases and other obligations | Q3 release `[F]`; call `[E]` |
| Oracle rating | S&P **BBB−** (9 Jul 2026); Moody's Baa2 negative | FactSet `[E]` |
| Microsoft leases and funding | Leases not yet commenced **364.6bn** (30 Sep); finance-lease liabilities 71.0bn (13-year average term). Net cash **29.0bn** after **12.9bn of component prepayments** (a platform pre-financing its suppliers: the reverse of vendor financing); 4.85bn of debt repaid; PP&E paid ÷ OCF 68%; CFO: will "access additional sources of funding" (leasing so far, debt "not yet") | 10-Q `[F]`; call `[E]` via `docs/msft-analysis.md` |
| OpenAI as a cloud customer | **10.0bn** of Microsoft's Q1 FY27 revenue incl. revenue sharing (**10.8%**); receivables 7.2bn; Microsoft's stake ~24% as converted. Lab spending inside E2, and the financing-break channel for Azure | 10-Q `[F]` |
| Vendor financing, by supplier | Broadcom: loan to Anthropic up to **42bn**; ~60bn of debt arranged for chip customers; AI XPV vehicle with Apollo and Blackstone (residual-value guarantees, size not disclosed). Google: up to **30bn** into Anthropic (10bn Series G-2 paid in April + 20bn of note capacity to Dec 2030, cut by its up-to-10bn IPO option; cap 14.99%; 5 GW of TPU). NVIDIA: residual value guaranties up to **105bn** (SB Energy leases for OpenAI's ~4.25 GW Ohio campus, nine phases from FY29) + 3.5bn of land, power and shell (108.5bn); equity stakes **99bn** (marketable 42.8, non-marketable 47.9) + **25bn committed**; AI cloud buy-backs 36bn; third-party DC leases 20bn; supply commitments 279bn; MoUs for > 500bn with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR. Amazon: Anthropic facility 20bn (15bn undrawn); **50.0bn of OpenAI Series C preferred** (15.0 Q1, 13.7 Q2, 21.3 Q3; fully paid) with OpenAI's AWS commitment of **138bn**. Micron: an Anthropic stake (size `[?]`) and 32bn of customer commitments the other way | NVIDIA 10-Q and 8-K (17 Aug) `[F]`; Alphabet 10-Q, Anthropic S-1 `[F]`; Amazon 10-Q `[F]`; Reuters `[E]` |
| **Vendor financing, level** (loans, guarantees at cap, equity commitments to AI customers) | **≥ USD 270bn**, up to ~286bn with the Anthropic Class N placement; loans and guarantees ~150bn. Equity already held (NVIDIA 99, Alphabet's Anthropic ~124) is on top. Class N placement **$26.0bn** at the IPO price: Google 10.0 (inside its 30bn), AMD 2.5 `[F]`; NVIDIA 10, Broadcom, Micron and Microsoft 1 each `[E]`; TSMC 0.5 + 0.5 of OpenAI preferred `[F]`. New supplier equity ≤ ~16.5bn in Q4; overlap with NVIDIA's 25bn committed `[?]`. Microsoft's prepayments run the other way and are not counted | This table; S-1/A `[F]` |
| Platforms' Anthropic stakes | Amazon **238.7bn** (30 Sep; notes 146.2 + preferred 92.5; ~20.5% as converted, implying ~1.16tn); Alphabet ~124bn: **~363bn** of platform value riding on E1 and the IPO, plus Amazon's 50bn in OpenAI | 10-Qs via the analyses `[F]` |
| Platform funding | Meta: Q3 FCF −2.1bn, capex ÷ OCF 106%, no buybacks, dividends 1.4bn, net debt issued 24.9bn in nine months, non-voting Class C from Jan 2027 for "capital raising". Amazon: capex ÷ OCF 179% (75.9 / 42.4; 125% TTM), Q3 FCF −33.5bn (TTM −42.4bn), long-term debt 180.9bn face (end-2025 68.8bn; incl. the 17.5bn term loan and £4.3bn of notes), long-term debt raised = 67% of nine-month cash capex, interest 1.7bn in Q3 (0.5bn a year earlier), no equity issued. Latest-quarter capex ÷ OCF: Alphabet 121%, Meta 106%, Oracle ~124% `[E]`, Microsoft 68%; **the five ~116%** (capex ~230bn, OCF ~199bn) `[A]` | Meta 8-K 21 Oct `[F]`; the analyses `[F]` |
| Supplier view of the constraint | Broadcom CEO (12 Oct): "capital" now the biggest constraint; wafer and memory shortages easing. NVIDIA (Huang, 22 Oct): neocloud demand "off the charts" but neoclouds lack the working capital to fund their growth; lenders should treat its compute as a "financeable asset" | Secondary reports; CNBC, Bloomberg `[E]` |

| K4 Contracted backlog | USD bn | Detail |
|---|---|---|
| Microsoft commercial RPO (30 Sep) | **677** | Flat q/q; +73% y/y; bookings −12% y/y; ~30% within 12 months, weighted duration ~2.3 years; total RPO 683 `[F]` |
| Oracle RPO (31 Aug) | 664 | +209bn y/y `[E]`; next report mid-December |
| Google Cloud backlog (30 Sep) | **561** | +9% q/q; "just over 55%" within 24 months; Anthropic share not given; call `[E]` |
| AWS backlog (30 Sep) | **578** | +16.5% q/q; weighted remaining life **6.1 years**; ~3.1× the run-rate (Google Cloud ~4.6×) `[F]`. Anthropic (≥ 110.0) and OpenAI (138) ≈ 248bn, ~43% of it if all of it sits in RPO |
| **Total** | **~2,480** | +3% q/q; includes labs' multi-year compute commitments (OpenAI targets ~USD 600bn of compute spend by 2030 `[E]`) |
| Memo: Anthropic obligations (S-1/A No. 2, 10 Nov) | ~901 + 150–175 | Google ≥ ~121.3 (Apr 2026–Jul 2033) plus an estimated 125–150bn of further TPU compute in 2028–31; Amazon ≥ 110.0 (May 2026–Apr 2036); Microsoft ~31, Broadcom ~161 `[E]`. Part of the backlog, not additive `[F]` |
| Memo: CoreWeave backlog (30 Sep) | 132.5 | Mostly lab and platform contracts already in the lab commitments; not additive `[F]` |

## K1 capex cycle (11 Nov 2026)

**Why.** K1 Base must be the most likely path, not guidance and consensus by default (user, 11 Nov; Option D of `docs/review-ai-k1-sustainability.md`; skill Step 1b). Guidance sets the current year, contracts the next, and this judgement the years after; the K1 view is set only here. Evidence (S1–S20) and the full arithmetic are in the review; `references/k1ret.py` reproduces the gauge.

**The cycle in five lines:**
1. **Where:** the fourth year of the build (the five's capex ~165 → ~262 → ~450 → ~815, 2023–26). Capex is 116% of OCF (Q3-26); FCF after dividends and buybacks was −48.8bn in Q3. D&A grows 44–90% y/y against revenue 19–39%. GPU rental prices still rise (B200 +27.6% year to date) and the term curve is backwardated. Backlog +3% q/q (Microsoft flat).
2. **Return gauge:** on Base K1 and the Base E-paths the AI asset base earns ~12% pre-tax in 2026, ~6% in 2027, ~2.5% in 2028 and ~0% in 2029. The revenue needed for 10% is ~860bn (2028) and ~1,180bn (2029) against ~600bn and ~740bn delivered: coverage 70% and 63% (51–79% across the sensitivities). The gap is locked in by the 2026–27 build: it sets the depth of the eventual digestion, not its date.
3. **Past cycles:** returns lagged spending for 4–5 years (telecom) and 10 (shale). Capex turned on equity, price, credit or revenue growth, in none of the four on a computed return. Hyperscaler surges ended in a flat year (2019 +4%, 2023 −2%).
4. **Judgement against Base:** 2027 contracted (1,120); 2028–29 a plateau (1,170 / 1,170). Risk later (AWS "over 40%" in 2027–28, rising rental prices, guidance beats of +10–22% in boom years) and deeper (funding of two labs, Meta and Oracle carrying the growth, siting).
5. **Price:** the compute basket earns k at 1.14× its Base 2028–30 path, the platform basket at 1.10×. NVIDIA's own k-path sits ~0.86× the Base (v1.3); TSMC needs 1.07× its H3 path (v1.2). The compute price still assumes no digestion.

### 1. Where is the cycle?

| Signal | Now (dated) | Reading | Source |
|---|---|---|---|
| Capex growth; capex ÷ OCF | The five: ~+72% (2025), ~+81% (2026E on 9M actuals and Q4 guides) `[F]`/`[A]`. Capex ÷ OCF 116% in Q3-26, 95% TTM; Amazon 182%, Oracle 123%, Alphabet 121% (Q3) `[F]` | Spending exceeds internal cash: the plan depends on markets | Filings via Alpha Vantage (review S3) |
| FCF after dividends and buybacks | The five −66.7bn TTM, **−48.8bn in Q3-26 alone** `[F]`/`[A]` | A funding need of ~$200bn a year at the Q3 pace `[A]` | Review S3 |
| Debt, equity and leases raised | Long-term debt end-2025 → 30 Sep 2026: Alphabet 46.5 → 125.1, Amazon 68.8 → 180.9 (face), Meta 58.7 → 80.9; Oracle 100.0 → 117.7 (Aug), BBB− `[F]`/`[E]`. Microsoft 35.4 → 31.1, but leases not yet commenced $364.6bn `[F]`. Equity: Alphabet $49.6bn + $12.4bn ATM, Oracle $20bn `[F]`/`[E]` | Four of five fund externally; Oracle is the weakest | K3; review S3, S8, S10 |
| D&A growth against revenue growth | Q3 y/y: AWS D&A +63% vs revenue +39%; Alphabet +49% vs +25%; Microsoft +56% vs +19%; Meta +44% vs +26%; Oracle +90% vs +30% `[F]` | The depreciation wave has started; the gauge has the five's D&A +44% in 2028 against cloud revenue +25% `[A]` | Review S3, S4, S10 |
| Margins | Microsoft Intelligent Cloud gross margin 66% → 62% → 58% (FY24–26); Meta 35% before its legal charge (40% a year earlier); AWS operating margin 38.7%, up `[F]` | Mixed: the fastest builders' margins fall; AWS's not yet | Review S4, S7, S8 |
| GPU rental prices and term curve | H100 $2.75 an hour (27 Jul); B200 **$5.62** (1 Sep, +27.6% year to date); B200 curve backwardated (3-month 5.73, 12-month 5.39) `[E]`; all four clouds "supply constrained" `[E]` | **No turn signal;** the curve expects lower prices next year | Silicon Data (review S15) |
| K4 backlog q/q | +3% (Q3); Microsoft flat, AWS +16.5%, Google Cloud +9% `[F]` | Slowing at Microsoft | K4 |
| Customer concentration | OpenAI 10.8% of Microsoft's revenue `[F]`; OpenAI 138 + Anthropic ≥ 110 ≈ 43% of AWS's backlog; Anthropic ≥ 121.3 ≈ 22% of Google Cloud's `[F]`/`[A]`; more than half of Oracle's RPO is OpenAI `[E]` | High: the return rests on two equity-funded labs | K3, K4 |
| Management language on returns | Asymmetric-risk framing (Zuckerberg, Pichai); **no hyperscaler states a return hurdle for AI capex** `[E]`/`[?]` | The plan is not return-gated | Review S17 |
| Suppliers' commitments | NVIDIA supply commitments flat at ~$87–88bn a year in FY28–29 after the FY27 step `[F]` | A plateau after 2027 is what the largest supplier has contracted for | Hardware |

**Reading:** funding and depreciation signals are on the Bear side, pricing signals on the Bull side, backlog mixed. Nothing turns 2027; the question is 2028–29.

### 2. Past cycles

| Episode | Run-up | Returns while spending ran ahead | Funding | What turned it | Signal → capex turn | Fall |
|---|---|---|---|---|---|---|
| **US telecom and fibre, 1996–2002** | Real communications-equipment investment ~18% a year to Q4 2000 `[E]`; nominal 70.8 (1996) → 123.3 (2000) `[F]` | The industry lost ~$20bn in 2001; capacity prices fell `[E]` | New entrants' equity and debt `[E]` | Equity first (Nasdaq telecom peak 10 Mar 2000), then overcapacity and falling prices, recession `[E]` | ~3 quarters | Nominal 123.3 → 83.7 (2002, −32%); the 2000 level not regained by 2007 `[F]` |
| **US shale, 2010–2016** | Well investment 86.6 (2010) → 169.8 (2014) `[F]` | Negative FCF every year 2010–19, ~$189bn for 34 producers `[E]` | High-yield debt and equity `[E]` | Price (Brent halved from mid-2014), then credit `[E]` | 2–3 quarters | 169.8 → 63.8 (2016, −62%) `[F]` |
| **Hyperscalers, 2017–2019** | The five's capex 42.6 → 68.2 (2018, +60%) `[F]` | High (operating income +16% in 2019) `[F]` | Operating cash flow | Digestion of the 2018 build, memory down-cycle, trade war `[E]` | ~1 year | +60% → **+4%** (2019); no absolute fall `[F]` |
| **Hyperscalers, 2020–2023** | 97.0 → 130.6 → 158.0 (+37%, +35%, +21%) `[F]` | Meta operating income −38% (2022); AWS growth 37% → 13% (2021–23) `[F]` | Operating cash flow | Revenue growth slowed; Meta cut its 2023 guide $34–37bn → $28.1bn `[E]`/`[F]` | Same year | **−2%** (2023; Amazon −17%, Meta −13%) `[F]` |
| **AI build, 2024–** | ~165 (2023) → ~262 → ~450 → ~815 (2026E): +59% / +72% / +81% `[F]`/`[A]` | Segment margins up today; ~0% on the AI asset base by 2029 on Base (gauge) `[A]` | OCF, then debt, equity, leases, vendor financing ≥ $270bn `[F]`/`[E]` | — | — | — |

**What the analogues say:** spending ran ahead of returns for years and funding kept it going, so funding is no evidence of a sustainable return. The turn came from a signal outside the accounts (equity then prices; price then credit; revenue growth), never a computed return. Hyperscaler surges ended in a flat year after 1–3 years of +21% to +60%; the AI build is in its fourth year in 2027 at Base +42%.

| Where today differs | Evidence | Direction |
|---|---|---|
| The issuers are cash-rich and investment-grade | OCF TTM $724bn; IG OAS 0.91% (9 Nov) `[F]` | Later and shallower than telecom or shale |
| Contracted backlog | K4 ~2,480; Google Cloud 55% within 24 months; AWS 6.1 years `[F]`. Two labs are ≥ ~17% of it on filed figures, ≥ ~30% with Oracle's OpenAI share `[F]`/`[E]`/`[A]` | Supports 2027 |
| Prices rise, not fall | H100 and B200 rental indices up in 2026 `[E]`; in telecom capacity prices fell before capex peaked | No turn signal yet |
| The customer layer is equity-funded and loss-making | Labs; neoclouds (CoreWeave: no unsecured debt at current yields) `[E]` | Like the new entrants of 2000 |
| Assets wear out in 5–6 years, not 20+ | Filed server lives 5–6 years; Amazon shortened part from 6 to 5 (2025) `[F]` | Idle capacity cannot wait a decade; the return must come within the asset life |

### 3. The return gauge (`references/k1ret.py`)

Method `[A]` unless tagged: the AI asset base is K1 above a non-AI baseline (140 in 2023, +5% a year, calibrated on the five's D&A), by monthly vintage, construction in progress counted. Short-lived 65% (Alphabet's servers and networking share `[F]`), 5.5 years, in service after 2 months; long-lived 35%, 20 years, after 12 months, 5% land. Cash cost 40% of AI revenue (AWS 41%, CoreWeave 38% `[F]`). Required revenue = (10% × average net AI assets + AI depreciation) ÷ (1 − cash cost). Supply = the Base E-paths: E2 above a 10% trend from 2023, T1 seats × ~$240 a year, Meta's revenue above a 10% trend (an upper bound). K1 history from filings; flat after 2029.

| Base K1, USD bn `[A]` | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---|---|---|---|---|---|---|
| K1 | 450 | 790 | 1,120 | 1,170 | 1,170 | 1,170 | 1,170 |
| AI capex | 296 | 628 | 950 | 991 | 982 | 973 | 963 |
| Cumulative AI capex | 461 | 1,089 | 2,038 | 3,030 | 4,012 | 4,985 | 5,948 |
| AI depreciation | 35 | 88 | 184 | 309 | 438 | 557 | 654 |
| Average net AI assets | 292 | 708 | 1,374 | 2,095 | 2,702 | 3,176 | 3,531 |
| **Revenue needed, r = 10%** | 106 | 265 | 536 | **864** | **1,181** | 1,458 | 1,679 |
| Revenue needed, r = 0% | 58 | 147 | 307 | 515 | 730 | 929 | 1,091 |
| **Supply** (cloud / Copilot / Meta) | 111 (68 / 5 / 38) | 287 (200 / 10 / 76) | 449 (344 / 14 / 92) | **602** (469 / 23 / 110) | **738** (577 / 31 / 130) | 845 | 944 |
| **Coverage of the 10% need** | 104% | 108% | 84% | **70%** | **63%** | 58% | 56% |
| Gap to the 10% need | — | — | −87 | −262 | −443 | −613 | −735 |
| **Pre-tax return on AI net assets** | 10.9% | 11.9% | 6.2% | **2.5%** | **0.2%** | −1.6% | −2.5% |
| The five's D&A (non-AI 93.5 in 2023 + 5% a year, plus AI) | 138 | 196 | 298 | 428 | 563 | 689 | 793 |

| Sensitivity (Base K1) | Coverage 2028 / 2029 | Revenue needed 2029 | Supply 2029 | Pre-tax return 2028 / 2029 |
|---|---|---|---|---|
| **Central** | **70% / 63%** | **1,181** | **738** | **2.5% / 0.2%** |
| r = 8% / 12% | 76% / 68%; 64% / 58% | 1,091 / 1,271 | 738 | unchanged |
| Cash cost 35% / 45% | 75% / 68%; 64% / 57% | 1,090 / 1,288 | 738 | 3.9% / 1.5%; 1.1% / −1.2% |
| Short life 6.0 years | 72% / 65% | 1,140 | 738 | 3.5% / 1.3% |
| **Short life 4.0 years (economic)** | 60% / 56% | 1,323 | 738 | −2.2% / −4.4% |
| Short-lived share 75% | 66% / 59% | 1,245 | 738 | 0.8% / −1.7% |
| **Strict: no Meta uplift** | 57% / 51% | 1,181 | 608 | −0.7% / −2.7% |
| **E2 at the Bull row** (+45% / +32% / +22%) | 79% / 74% | 1,181 | 870 | 4.9% / 3.1% |

| K1 path 2027 / 2028 / 2029 (supply on the Base E-paths) | Coverage 2027 / 2028 / 2029 / 2030 | Pre-tax return 2028 / 2029 / 2030 |
|---|---|---|
| **Base: plateau 1,120 / 1,170 / 1,170** | 84 / 70 / 63 / 58% | 2.5 / 0.2 / −1.6% |
| Taper on guidance and consensus 1,120 / 1,250 / 1,300 | 84 / 69 / 60 / 54% | 2.3 / −0.4 / −2.4% |
| Flat 1,120 / 1,120 / 1,120 | 84 / 70 / 64 / 60% | 2.6 / 0.5 / −1.1% |
| Holds the 2027 coverage by 2029: 1,120 / 650 / 650 | 84 / 77 / 81 / 84% | 4.2 / 4.8 / 5.3% |
| Bear 950 / 800 / 820 | 88 / 81 / 79 / 78% | 5.2 / 4.4 / 3.6% |
| Bull 1,300 / 1,550 / 1,700 | 80 / 61 / 50 / 44% | 0.5 / −2.6 / −5.0% |

**What the gauge says:**
- **The gap is revenue, and it is large.** The supply is a generous attribution, about twice the disclosed AI run-rates (Microsoft > $37bn, AWS > $25bn, OCI ~$30bn annualised `[E]`), and still covers only 70% and 63% of the 10% need in 2028–29. No case reaches 10% inside the window.
- **It shows in the 2027–28 reports:** coverage falls below 100% in 2027, and the five's D&A rises ~+50% a year in 2027–28 against revenue growth of ~13% `[A]`.
- **It is locked in by the 2026–27 build** (~1,580bn of AI capex, depreciating through 2031–33). Holding the 2027 coverage would need K1 at ~650 in 2028–29, below the Bear, so the gauge measures the depth of the eventual digestion; it is not a timer.
- **Base K1 assumes the return arrives after 2029:** AI revenue must keep growing well above +12% a year, or the companies accept returns below their cost of capital (after-tax WACC ~9–10%, ~11–12.5% pre-tax `[A]`; 10-year Treasury 4.88%, IG OAS 0.91% on 9 Nov `[F]`).
- Cross-check: the three analysed platforms' own D&A paths plus ~65 / 100 / 130 for Meta and Oracle `[A]` give 304 / 413 / 504 in 2027–29, within 2–12% of the five's D&A above.

### 4. Judgement against Base

| Year | Base `[A]` | Judgement | Later or higher than Base | Earlier or deeper than Base |
|---|---|---|---|---|
| **2027** | 1,120 (+42%), range 1,050–1,200 | **Contracted: kept** | AWS "over 40%" in 2027–28 (release `[E]`); NVIDIA FY28 ~70%, supply-limited `[E]`; guidance beat the initial guide by +10–22% in 2024–26 `[E]`; Goldman 1,200, upside 1,400 `[E]` | Microsoft's RPO flat, bookings −12% y/y `[F]`; capex 116% of OCF and FCF after returns −48.8bn in Q3 `[F]`; the K1 growth after 2026 rests on Meta and Oracle, the two names with no analysis and the weakest return evidence |
| **2028** | **1,170 (+4.5%)**, range 1,000–1,350 | **A digestion year, at the top of the past range** (+4%, −2%) | Backlog due in 2028 (Google Cloud 55% within 24 months; AWS 6.1 years); NVIDIA's commitments flat, not falling `[F]`; rental prices still rising `[E]`; IG spreads 0.91%; the labs are funded through 2027 | Return ~2.5% pre-tax (coverage 70%); D&A +44% against cloud revenue +25% `[A]`; two equity-funded labs ≥ ~17–30% of backlog; US siting policy (Texas, Georgia, Ohio) `[E]` |
| **2029** | **1,170 (0%)**, range 950–1,400 | **Flat:** no backlog evidence reaches it, and the return gap is at its widest | E2 still +18% on Base; the three analysed platforms with Meta and Oracle at the same growth give ~1,175 bottom-up `[A]` | Coverage 63%, return ~0%; −4.4% with a four-year economic life; 51% coverage on strict attribution |
| **Overall** | 790 / 1,120 / 1,170 / 1,170 | **Base kept as set on 11 Nov.** A point moves only by the minimum change (5% of the capex level, ~58bn). An absolute cut is the Bear's financing break (950 / 800 / 820), and nothing signals it yet: prices rise, IG spreads are tight and the labs are funded through 2027. 25/50/25 is a convention, not a probability | | |

### 5. What the price implies

Basket method (each layer's Base exit P/E, payout and cash conversion; 6 Nov prices, 7 Nov consensus; Base FX); 2027 held at Base, 2028–30 scaled by a uniform multiplier.

| Basket or name | P/E CY27 | Base IRR (NOK) | 2028–30 × Base for **k = 12%** (path) | for **0%** (path) | Source |
|---|---|---|---|---|---|
| **H1 compute basket** | 13.71 | 7.5% | **1.14** (1.04 / 1.00 / .99) | 0.79 (.72 / .70 / .69) | `impl.py H1` |
| **E platform basket** | 20.95 | 8.6% | **1.10** (1.18 / 1.29 / 1.40) | 0.78 (.83 / .91 / .99) | `impl.py E` |
| NVIDIA, own build (v1.3, $168.89) | — | — | k-path .76 / .78 / .75 of CY27 consensus = **~0.86×** the Base `[A]` | — | `docs/nvda-analysis.md`; restated at its 17 Nov run |
| TSMC, own build (v1.2, $396.48) | — | — | **1.07×** its H3 path | 0.76× | `docs/tsm-analysis.md` |

**Reading:** the compute price needs H1 EPS to hold at about the CY27 consensus level through 2030 (1.04 / 1.00 / .99), i.e. no digestion; on Base it digests to .91 / .88 / .87. NVIDIA's own build is cheaper (its k-path ~14% below Base). The platforms need ~10% more than Base 2028–30.

### 6. Signposts with dates

| Date | Event | Confirms Base | Later or higher | Earlier or deeper |
|---|---|---|---|---|
| 17 Nov | NVIDIA Q3 FY27: Q4 guide, supply commitments | Commitments flat in FY28–29; guide inside the band | Commitments raised beyond FY29; Q4 guide > ~$124bn | Commitments cut; inventory up while growth slows |
| ~18 Nov | Anthropic IPO pricing | Priced in the range | Well above the range | Pulled or below the Series H: the Bear (financing break), not Base |
| Monthly (~1st) | Silicon Data GPU rental indices (H100, B200) | B200 flat to down 10% from its high, curve backwardated | Still rising, curve in contango into mid-2027 | B200 −20% from its 2026 high for three months |
| ~Mid-Dec | Oracle Q2 FY27: capex, RPO, OCI | FY27 capex 90–95bn, RPO up | RPO +10% q/q or more | Capex cut; RPO down |
| Late Jan–early Feb 2027 | First 2027 capex figures: Microsoft (~27 Jan), Meta (~28 Jan), Alphabet (~2 Feb), Amazon (~4 Feb) | K1 2027 1,050–1,250 | > 1,300, or "continued strong growth" for 2028 from three of five | < 1,000, or a platform guiding next-year capex flat or down: toward 1,120 flat, or the Bear if funding breaks |
| Each quarter (Q4 reports) | FCF after shareholder returns (five) | Between −50bn and 0 a quarter | Positive | Below −50bn a quarter twice with E2 growth slowing |
| Each quarter | K4 backlog q/q | 0 to +10% | > +10% q/q | Total down, or two of four flat or down |
| January roll-forward, and when K1 or E2 moves | K1 return gauge (`k1ret.py`) | Coverage of the 10% need in 2028 of 60–90% | > 90% (AI revenue disclosures lift supply above ~800bn for 2028) | < 60% |

## Hardware: notes (paths in the Interface)

- **Rows set from K1 (11 Nov, Step 1b) `[A]`;** `references/model.py` (switch `K1D`) prints the derivation.
  - **H1 750 / 745** (748.8 / 742.5 unrounded): Base keeps the non-K1 share, so H1 holds its ratio to K1 (0.595 / 0.652 / 0.641 / 0.637 in 2026–29). In the compute-share build (K1 × 2026 chip intensity 0.361 × content uplift 1.10 in 2028–29, non-K1 share 38.0% / 37.5%) it is the same.
  - **H4 129 / 130** (129.2 / 129.6): H4's Base growth tracked K1's in 2028–29, so it takes H1's ratio to K1.
  - **H3 kept (125 / 140 / 151):** it reads K1 only through H1. At the 20–30% pass-through used for TSMC the index would be 138.2–137.3 / 148.0–146.5 (growth −1.4 to −2.2 pp in 2028, −0.8 to −1.2 pp in 2029; EPS −0.02 to −0.03 and −0.03 to −0.04): below the 5 pp and 0.05 rules, noted only.
  - **H2 kept:** its Base turn in 2028 already assumes AI capex digestion after 2027.
  - **H5:** a flat K1 in 2028–29 means fewer new gigawatts in those years; siting stays a signpost.
- **H1 2026 build (~470) `[A]`:** NVIDIA data center FY27 ≈ CY26: Q1 75.3 `[F]`, Q2 **89.0** `[F]`, Q3 ~100 (from the 108.0 total guide), Q4 ~112 → ~376; Broadcom AI semis FY26 ~58 `[E]` (Q3 16.7, Q4 guide 21.7); AMD Instinct ~12 `[A]` (data center 6.7 in Q2 incl. EPYC `[E]`; Q3 $8.5bn, +97%, Q4 guide ~$17bn total revenue, too small to move H1); custom and other ~20 `[A]`.
- **H1 buyers outside K1 (Base assumption):** 30–46% of H1 2026 (~140–215bn of ~470; central ~185) is bought outside the five platforms' capex: AI clouds and neoclouds, xAI, the labs' own and leased builds, sovereign and enterprise `[A]`; NVIDIA's ACIE segment was 45% of its Q2 FY27 data center `[F]`. Base keeps that share about constant: non-K1 H1 ~+60% in 2027 (range +43% to +76%), then ~285 and ~278, digesting with K1. **Base assumes these buyers stay funded at their current share.** Their 2027 funding is mostly raised (labs' equity and IPOs, SpaceX's IPO and notes); neocloud debt is still to be raised; NVIDIA's direct support is ~5–8% of non-K1 H1. A shortfall is the financing-break Bear (non-K1 H1 −25 to −30% in 2027, about −46% and −41% in 2028–29). Sizing in `docs/review-ai-h1-non-k1-funding.md`.
- **H1 2027 Base +55%:** below the supply-limited ~70% NVIDIA cites for FY28 `[E]` (= consensus, the Bull) and consensus CY27 EPS growth of +74% for the basket `[F]`; above K1's +42% because the compute share of capex rises (Microsoft: two-thirds short-lived assets `[E]`) and memory costs raise system prices. Broadcom's FY27 AI figure of ~USD 115bn is from a transcript summary only `[?]`.
- **NVIDIA (`docs/nvda-analysis.md`) `[F]`:** Q2 FY27 revenue 96.2bn (+106%), data center 89.0bn: Hyperscale 48.7bn (+102%), AI Clouds, Industrial and Enterprise 40.3bn (+138%), Edge 7.2bn; gross margin 75.0%; Q3 guide 108.0bn ± 2%, gross margin 74.0%; Rubin ~USD 40bn of revenue per GW (25bn for Blackwell) `[E]`. Receivables +24.6bn in H1 (DSO 60 from 45); inventory 31.6bn. Supply commitments 279bn (92bn rest of FY27, 87bn FY28, 88bn FY29), mostly memory: flat after the 2027 step. Its revenue-consistent Bear (gross margin 68–72%, opex USD 42–47bn) is the H1 Bear (.68 / .50 / .53 / .57); NVIDIA is 76% of the basket's CY27 earnings. v1.3 (11 Nov): board review of the CEO, China-diversion reports, possible export rules; no guidance change.
- **Custom silicon** `[E]`: Maia 300 (multi-GW Azure deployments from 2027), TPU 8i and external TPU system sales (~100 customers): a GPU-margin risk the Base already carries.
- **H2:** the index follows the EPS path. Consensus CY27 revenue is ~+50% on CY26 (index ~148–151 = the Bull's 150); revenue relative to consensus from Micron's mapping: EPS 0.90 → revenue ~0.92, 0.60 → ~0.68 `[A]`. Base revenue falls 14% in 2028 and 13% in 2029 while EPS falls 33% a year: margins fall faster than prices. Evidence and judgement: H2 Memory cycle.
- **H3:** TSMC Q3 USD 46.7bn (+41% y/y), gross margin 66.4%; Q4 guide USD 52.3–54.3bn (+14% q/q), gross margin 65–67%; 2026 ~+44% in USD (~176bn); capex 60–64bn, 2026–28 "well above" the 101bn of 2023–25; N2 capacity more than doubles in 2027; demand "well above" supply `[F]`. October revenue NT$586.89bn (+59.7% y/y); capital appropriations $40.93bn `[F]`. ASML Q3 EUR 11.7bn, 2026 EUR 44–45bn `[F]`; Lam Q1 FY27 USD 8.22bn, operating margin above 40%, supply-limited `[E]`. Run-rate test: Base 2027 (125) leaves ~3% above the Q4-26 run-rate (~121); TSMC Base EPS +27% against revenue +25%; consensus 2027 (+36%) is the Bull. TSMC's revenue-consistent Bear (.76 / .63 / .67 / .71; ~60% of the basket) is the H3 Bear.
- **H4:** Arista Q3 $3.66bn (+58.5%), 2027 +38–40%, AI networking ~3.5 → ~7bn; Vertiv Q3 $4.31bn (+61%) `[E]`. The H4 names' 2027 consensus revenue (~+22% revenue-weighted, ~+30% cap-weighted) brackets the Base (+25%).

## H2 Memory cycle (1 Nov 2026, re-marked 7 Nov) — the lead section for the Samsung, SK hynix and IQQK analyses

**Why.** User rule of 1 Nov (`docs/review-kospi-analysis.md`, section 5): opportunistic cyclical memory positions (IQQK, Samsung, SK hynix) lead with **the cycle** (where it is, what can turn it, how likely and when), then what the price implies. E / R against high yield and precise IRRs are not the gate: HY's R is ~9 pp and a memory share's 40–60 pp, and the IRR mostly echoes the 2030 mid-cycle. The memory view is set only here; `docs/skhynix-analysis.md`, `docs/samsung-analysis.md` and `docs/kospi-analysis.md` lead with this section, and `docs/mu-analysis.md` may. It is an assessment, not a re-baseline: the H2 paths are unchanged. The K1 plateau (1,170 / 1,170) is the AI capex digestion that the Base turn in 2028 already assumes.

**The cycle in five lines:**
1. **Where:** late upcycle. Contract prices still rise, but q/q growth has halved twice since Q2-26 (~80% → ~40% → ~20%; Q1-27 +3–8%). Mobile DRAM and NAND outside enterprise SSD are about flat. Supplier inventory is under two weeks, margins are records, and the shares peaked in June; the Korean ones have fallen further than in the full 2018–19 and 2021–22 downturns.
2. **What turns it:** supply from 2H-27 into 2028 (new fabs, 1δ / G11, CXMT's +31% in wafers, HBM wafers returning to DRAM) meets AI capex digestion after the contracted 2027 build and a consumer market already shrinking at today's prices. The LTAs soften the fall for the leaders but cap the rise; SK hynix and Samsung disclose no floors.
3. **Against Base (turn in 2028): Base kept.** Timing about Base, risk 1–2 quarters earlier for NAND and commodity DRAM; 2028 depth Base or shallower for the leaders; 2029–30 Base or deeper.
4. **What the price implies (6 Nov closes):** the basket earns k at **0.75×** Base 2028–30 and 0% at 0.49×: **the price discounts a turn about a quarter deeper or earlier than Base.** SK hynix prices 43% below Base, Samsung 32% below, Micron about Base (1.08×).
5. **Signposts:** the contract prints (end-Nov, end-Dec) and TrendForce's Q1-27 outlook; LTA ranges or floors in the Q3 business reports (~14–16 Nov); NVIDIA (17 Nov), Micron FQ1 (16 Dec), Samsung's Q4 preliminary (~7 Jan); the 2027 memory capex figures (late Jan); foreign flows in Kospi.

### 1. Where is the cycle?

| Indicator | Now | Momentum | Reading | Source |
|---|---|---|---|---|
| Conventional DRAM contract price, q/q | Q1-26 ~+90–95%, Q2-26 ~+80%, Q3-26 ~+40%; **Q4-26 +10–15%** conventional, **~+20%** blended with HBM; **Q1-27 +3–8%** | Rising, but q/q growth has halved twice since Q2-26 | The level still rises into Q1-27; the second derivative turned in Q2-26 (higher base, weaker end-market purchasing power, **LTA price ceilings**) | TrendForce 30 Sep and 20 Oct `[E]`; Q1-27 via Goldman `[E]` |
| By segment, Q4-26 | PC DRAM +13–18% (Q3 +18–23%); server DRAM undersupplied, but LTA suppliers lag the average; **mobile DRAM 0–5%** on elevated customer inventories; graphics up (GDDR7) | Mobile is the first to stall | The weakest segment is already near flat | TrendForce via Goldman (31 Aug), 30 Sep `[E]` |
| DRAM fixed price (DDR4 8Gb PC) | **$27.50 in October**, +5.8% m/m, a record | Rising | The contract level is at a record | DRAMeXchange via press, 30 Oct `[E]` |
| NAND contract | Q4-26 +15–20% (enterprise SSD +23–28%). **128Gb MLC flat in October**, the first flat month after 21; client SSD and eMMC/UFS weak | Stalling outside enterprise SSD | NAND turns first: TrendForce expects looser NAND in 2H-27; UBS models the NAND price peak in CQ3-27 | TrendForce 30 Jul and 30 Sep; press 30 Oct; UBS via Wccftech `[E]` |
| HBM | 2027 volumes and prices settled (SK hynix); 2027 sold out at target prices (Samsung); 2027 HBM blended ASP +121% y/y (mix to HBM4 and HBM4E) | Locked for 2027 | HBM is not where 2027 turns; the 2028 negotiations (around mid-2027) are | Company calls 28–29 Oct; TrendForce 29 Sep `[E]` |
| Spot (4 Nov) | DDR4 1Gx8 spot −0.09% w/w ($46.82), still above contract; buyers wait and volumes dropped sharply; DDR5 buyers raise targets on delivery pressure. 512Gb TLC wafer spot −4.33% w/w ($16.152); NAND sellers cut to clear stock | Stalling (DRAM); falling (NAND wafers) | No spot-below-contract signal yet; NAND wafer spot is the first clear spot decline, on the early side of section 4 | TrendForce 16 Sep and 4 Nov `[E]` |
| Supplier inventory | **< 10 days** at Samsung and SK hynix (KB Securities, Sep); ~3 weeks of DRAM and NAND at end-Q2 (Shinhan) | Falling | No supplier overhang | DigiTimes; Shinhan via press `[E]` |
| Customer inventory | PC OEMs ran down 1H-26 stock; module houses build stock; smartphone makers' inventory weeks elevated; no reliable weeks figure | Rising at the edges | Where an overhang forms first: Q4-21's decline (−3–8%) came "due to rising level of client inventory" | TrendForce Jun–Sep 2026 and 22 Sep 2021 `[E]`; weeks `[?]` |
| Utilisation, lead times | At ceiling; server RDIMM lead times 20+ weeks | Flat at the top | Lagging: they peak at the turn | Secondary `[E]`/`[?]` |
| Contract cover (LTAs) | **SK hynix:** 14 customers on **> 50% of 2027–28 capacity** within agreed price ranges. **Samsung:** 10 multi-year contracts, 10 in talks, target 60–70%. **Micron:** **> 75% of 2027 output committed**; 26 SCAs on > 35% of revenue through 2030 at floor margins "meaningfully above any prior cycle peak"; RPO ~$150bn; $32bn of customer commitments ($12.75bn in cash deposits). **SK hynix and Samsung disclose no floors** | Rising | LTAs soften a fall for the leaders and cap the rise: the ceilings bite in Q4-26 | Company releases and calls `[F]`/`[E]` |
| Margins | SK hynix Q3 operating margin **80%** (operating profit KRW 83.3tn; 2018's peak quarter 57%); Samsung operating profit 107.4tn (DS 106.5tn); Micron FQ1-27 gross margin guide 86.25%, "the floor for fiscal 2027" (peaks 61% in 2018, 47% in 2021–22) | At the top | Records by a wide margin, so EPS will fall faster than revenue | SK hynix, Samsung, Micron `[F]`; history `[E]`/`[F]` |
| Consensus | CY27 EPS still raised: SK hynix 466,736 (16 Oct) → **529,348** (7 Nov), Samsung 72,043 → **77,324**, Micron flat (191.8). CY27 revenue over CY26 (1 Nov): SK hynix +58%, Samsung group +40%, Micron ~+50% | Rising | Analysts have not called a peak; no rating downgrades in October | Yahoo 7 Nov `[F]`; Benzinga via BigGo (30 Oct) `[E]` |
| Share prices (6 Nov) | From the June closing highs: SK hynix **−61%** (2,919,000 on 22 Jun → 1,132,000), Samsung **−48%** (362,500 on 18 Jun → 188,700), Micron **−43%** ($1,213.56 on 25 Jun → $690.00), Kospi **−44%** (9,114.55 on 22 Jun → 5,059.69) | Falling since June | Korea has fallen further than in the full 2018–19 and 2021–22 downturns (table 2) | Yahoo `[F]` |
| Foreign flows (Kospi) | Net selling of ~KRW 20tn in the month to mid-October, mostly SK hynix and Samsung; SK hynix's foreign ownership 49.76% (2 Oct), the lowest since May 2023; net buyers again on 21 Oct | Selling paused | A mood indicator, not a fundamental | Korea Herald, Herald Business `[E]` |

**Reading:** late upcycle. The Base 2027 index (138) is only ~6% above the Q4-26 run-rate (~130), so the Base already assumes a plateau in 2027. Momentum peaked in Q2-26, the weakest segments are flat, and margins are far above any earlier peak. In past cycles this configuration (share peak, decelerating contract growth, record margins, a capex step-up) came 1–4 quarters before the first contract-price decline.

### 2. Past cycles: lead times

| | 2016–19 | 2020–23 | This cycle (2025–) |
|---|---|---|---|
| Capex step-up | Samsung semiconductor capex ~KRW 13tn (2016) → 27.3tn (2017); SK hynix ~17tn in 2018 | Samsung semiconductor ~33tn (2020) → 43.6tn (2021); SK hynix ~19tn in 2022 | **Samsung 52.7 → 84.4tn (2026, +60%)**, higher in 2027. SK hynix 2027 "significantly" higher. Micron gross capex $15.9bn (FY25) → $30.7bn (FY26) → ~$25bn in 1H FY27 alone. The three ~$146bn in 2027 `[E]`. CXMT ~320k → ~420k wafers a month by 2027 `[E]` |
| First q/q contract-price fall | **Q4-18** (DRAM revenue −18.3% q/q); in 2019 DRAM quotes fell > 50% and DRAM revenue 37.5% | **Q4-21** (−3–8%, client inventory), after +3–8% in Q3-21; steep falls from Q3-22 | **Not yet:** Q4-26 +10–15%, Q1-27 +3–8% |
| Capex step-up → first price fall | ~6–7 quarters (supply-led) | 0–3 quarters (demand-led) | The step began in 1H-26; the 2017 lag puts the first fall in Q3-27 to Q1-28; new DRAM fabs ramp in 2H-27 with "substantial output" in 2028 (TrendForce, Jul) |
| Share-price peak | Samsung 1 Nov 2017; SK hynix 23 May 2018; Micron 29 May 2018 | Samsung 11 Jan 2021; SK hynix 25 Feb 2021; Micron 14 Jan 2022 | Samsung 18 Jun 2026; SK hynix 22 Jun; Micron 25 Jun |
| Earnings peak | Q3-18: SK hynix operating profit 6.47tn, a record "as chip outlook dims"; Micron FQ4-18 operating income $4.38bn, gross margin 61.0% | SK hynix Q4-21 and Q2-22 (~4.2tn each); Samsung DS Q3-21 and Q2-22; Micron FQ4-21 and FQ3-22 ($3.0bn) | **Not yet:** CY27 consensus 47–64% above CY26; Micron guides sequential growth in every quarter of FY27 |
| Share peak → earnings peak | 3 months (Micron), 4 (SK hynix), 11 (Samsung) | 4 months (Micron), 8–17 (Samsung, SK hynix) | 4+ months so far; the past range puts the earnings peak between Sep 2026 and Nov 2027 |
| Peak-to-trough share fall | Samsung −35%, SK hynix −39%, Micron −54% | Samsung −42%, SK hynix −49%, Micron −50% | So far (6 Nov): **Samsung −48%, SK hynix −61%, Micron −43%** |
| Share trough → earnings trough | Dec 2018–Jan 2019 → Q4-19 (SK hynix ~0.24tn) and FQ1-20 (Micron $0.52bn): ~11 months | Sep–Dec 2022 → Q1-23 (SK hynix −3.4tn; Micron FQ2-23 −$2.3bn): 3–6 months | — |
| What turned it | Supply (the 2017 capex, node bits), plus a hyperscaler pause and the US–China trade war in late 2018 | Demand: PC and phone digestion after COVID, client inventory, rate rises | — |

**What the analogues say:** shares lead (peaks 3–17 months before earnings, falls of 35–54%); the market prices the turn ahead of the data. Prices turned about one quarter after q/q growth reached low single digits: on that pattern Q2-27 would bring the first decline, earlier than the Base's annual 2028 fall, but the LTAs (ceilings on > 50–75% of the leaders' output) and HBM's claim on wafers both slow a slide. The supply lag (6–7 quarters in 2017–18; new fabs ramping in 2H-27) points to 2028.

### 3. What can turn it

| Channel | Evidence | Direction and timing |
|---|---|---|
| **Supply: the capex wave** | Samsung 84.4tn in 2026 (+60%), higher in 2027: P4 lower line Nov 2026, P5 in full operation 2028, Taylor 2027. SK hynix: M15X full by end-2026, Yongin fab 1 Feb 2027, M17 Dec 2028, Y2 Jun 2029. Micron: ID1 and Tongluo mid-2027, ID2 and Japan late 2028, Singapore NAND 2H-28 `[F]`/`[E]` | Bits from 2H-27, mostly 2028–29. The wave is larger than 2017–19's in dollars (Micron's capex about doubles two years running `[A]`; Samsung +60% on a larger base) |
| **Supply: node bits** | Micron's 1δ DRAM (+mid-20s% bits per wafer) and G11 NAND (~2× density) ramp in 2H-27; industry DRAM bits +low-20s% and NAND +mid-20s% in 2027–28 (Micron) `[F]` | 2028 bits without new cleanrooms; in the Base |
| **Supply: CXMT and China** | ~8% of DRAM revenue in Q1-26; ~320k → ~420k wafers a month by 2027 (+31%), aim 500k; IPO $8.6bn (Jul). Counterpoint 11% of DRAM bits by 2028, Nomura 18%. 4F² commercial "after 2028" `[E]` | 2027–28, commodity DRAM first; export controls a tail |
| **Supply: HBM → DRAM** | HBM takes ~3× the wafer of DDR5 per bit `[E]`; 8-Hi in place of 12-Hi would cut HBM per GPU by ~33% `[E]` | The swing factor for 2028–29; signpost: the 2028 HBM negotiations (mid-2027) |
| Supply, slower (against) | Capex buys shells and cleanrooms first; Samsung: "higher capex does not add bits in proportion"; SK hynix stages its investment `[F]`/`[E]` | Delays bits: supports 2028 over 2027 |
| **Demand: AI capex digestion** | K1 Base +42% in 2027, then +4.5% and flat. Memory's share of hyperscaler capex ~35% (2026) → ~48% (2027) (CLSA `[E]`) inside budgets already above OCF (the five ~116% in Q3). Value test `[A]`: TrendForce's 2027 memory market (> USD 1.28tn; DRAM 903bn, +46%) `[E]` exceeds Base K1 2027 (1,120bn) | 2028 |
| **Demand: US siting policy** | Governors who pledged pauses won Texas (~27% of planned US GW), Georgia (~7%) and Ohio (~5%); Texas has paused new loads ≥ 75 MW since 3 Aug (audit 10 Dec). No law, cancellation or guidance change `[E]` | 2028: fewer new US sites energised means fewer accelerators and less HBM and server DRAM; 2027 and the LTAs not hit. Earlier-or-deeper side, no figure |
| **Demand: AI lab financing** | Platform equity-funding signpost crossed (Alphabet's ATM); vendor financing ≥ USD 270bn; neoclouds lack working capital (Huang) | Bear channel: hits HBM and server DRAM in 2028 |
| **Demand: phones and PCs at high prices** | Smartphones −12.9% and PCs −11.3% in 2026 (IDC, Feb); Q3-26 smartphones −20% y/y (Counterpoint, preliminary); both down again in 2027 (TrendForce) `[E]` | The non-AI floor is weaker than in 2018 |
| **Demand: customer inventory** | Module houses and phone makers hold stock; hyperscaler stock not measured `[?]` | The 2021 trigger; shows first in mobile and PC contracts |
| Demand: easing statements | Broadcom (12 Oct): shortages easing, "capital" the constraint. Against: Micron and Samsung "tight through 2028", SK hynix "demand above supply through 2030" (guidance `[E]`) | Mixed; supplier guidance is Bull-side |
| **Contracts: ranges renegotiated** | SK hynix prices "within a price range agreed upon with customers" that "reflects market conditions"; ceilings bind in Q4-26 | The contract channel of the Bear |
| **Contracts: floors** | Micron: floors on > 35% of revenue through 2030; $32bn of customer commitments. SK hynix: deposits, amounts not disclosed. Samsung: none disclosed. Q3 business reports (~14 Nov Samsung, ~16 Nov SK hynix) may show more `[F]`/`[?]` | A floor near today's prices makes 2028 shallower than Base |

**Depth check (value per bit)** `[A]`: memory revenue tracking AI capex in 2028 (+4.5%) with DRAM bits ~+22% means ~−14% per bit; the Base's 2028 index (138 → 118, −14%) implies ~−30% per bit; in 2019 quotes fell > 50% and revenue 37.5% `[E]`. The EPS fall (.90 → .60, −33%) is steeper than revenue because margins start from records.

### 4. How likely, and when: the judgement against Base

| Dimension | Base (EPS path unchanged since 12 Oct) | Judgement | For the judgement | Against it |
|---|---|---|---|---|
| **Timing of the turn** | 2027 up on price but flat from the Q4-26 run-rate (index 138 against ~130); EPS .90 of CY27 consensus; the fall in 2028 | **About Base; risk 1–2 quarters earlier.** First q/q declines may come in 2H-27 for NAND and commodity and mobile DRAM; HBM and LTA server DRAM follow in 2028 | q/q growth halved twice; mobile 0–5% and NAND flat; the 2021 pattern; customer stock at the edges; UBS's NAND peak in CQ3-27; looser NAND in 2H-27; IDC: prices "stabilise by mid-2027"; NAND wafer spot −4.3% (4 Nov) | LTAs on > 50–75% of output; 2027 HBM settled; supplier stock < 2 weeks; TrendForce: DRAM up "through 2027"; new fabs only from 2H-27 |
| **Depth in 2028** | EPS .60 (−33%); revenue −14% (≈ −30% per bit) | **Base or shallower for the three leaders** | Micron's floors and > 75% committed; settled HBM; capacity staged in shells; AI inference demand | No floors at SK hynix or Samsung; ranges follow the market; a weaker consumer floor than in 2018 |
| **Depth 2029–30 (mid-cycle)** | .40 / .35 (2030 ≈ 2.7× SK hynix's 2025 EPS and ~4× Samsung's 2025 net income: the AI-era structural assumption) | **Base or deeper: the main risk** | The 2028–29 supply wave (Yongin, P5, ID2, Japan, M17, Y2, CXMT toward 500k, 1δ, G11) lands while AI capex is flat (2029, K1 Base); HBM wafers can return to DRAM | More AI content per system; oligopoly discipline and LTAs; 1δ cost per bit supports margins |
| **Overall** | | **Base kept.** The evidence moves the timing risk slightly earlier and the 2029–30 risk deeper, and holds the 2028 point. No independent figure (a floor, a price decline, a capex figure) meets a minimum change. 25/50/25 is a convention, not a probability | | |

### 5. What the price implies

Basket method: Base exit P/E 10, payout 15%, cash conversion .70 / .65 / .60, Base FX; 6 Nov closes (Seoul before the US rebound), 7 Nov consensus; 2027 held at .90 and 2028–30 scaled on .60 / .40 / .35. `references/impl.py` reproduces every figure.

| | P/E CY27 | Base IRR (NOK) | 2028–30 × Base for **k = 12%** (path) | for **0%** (path) | Flat 2028–30 level for k / 0% |
|---|---|---|---|---|---|
| **Memory basket** | 2.64 | 21.6% | **0.75** (.45 / .30 / .26) | **0.49** (.29 / .19 / .17) | .27 / .18 |
| SK hynix | 2.14 | 30.5% | 0.57 (.34 / .23 / .20) | 0.37 (.22 / .15 / .13) | .21 / .13 |
| Samsung | 2.44 | 24.8% | 0.68 (.41 / .27 / .24) | 0.44 (.26 / .18 / .15) | .25 / .16 |
| Micron | 3.60 | 9.7% | 1.08 (.65 / .43 / .38) | 0.72 (.43 / .29 / .25) | .40 / .26 |

| Basket path (EPS 2027 / 28 / 29 / 2030, CY27 consensus = 1) | IRR, exit P/E 10 | IRR, exit P/E 8 |
|---|---|---|
| **Base: turn in 2028 (2017–19 analogue)** (.90 / .60 / .40 / .35) | **21.6%** | 15.5% |
| Earlier turn: prices fall from 2H-27 (.80 / .45 / .35 / .35) | 19.8% | 13.5% |
| Later turn: prices hold through 2028, fall in 2029 (.95 / .85 / .55 / .40) | 28.0% | 21.7% |
| Shallower: LTA floors hold, higher mid-cycle (.90 / .70 / .55 / .45) | 30.6% | 23.8% |
| Deeper: a 2019-depth fall, pre-AI-style mid-cycle (.90 / .45 / .30 / .25) | 10.9% | 5.6% |
| Bull path (1.00 / .80 / .55 / .45) | 31.7% | 25.0% |
| Bear path at the Base exit P/E (.60 / .30 / .25 / .25) | 7.3% | 1.6% |

Exit P/E sensitivity of the basket multiplier for k: 0.90 at exit P/E 8, 0.75 at 10, 0.69 at 11.

**Reading:**
- **The price discounts a turn about 25% deeper or earlier than Base on 2028–30.** The earlier-turn path returns 19.8% and the 2019-depth path 10.9%; only a 2019-depth fall, or the Bear, fails k.
- **Timing is mostly priced; depth is not.** The mid-cycle and the exit multiple dominate.
- **The Korean names price a deeper turn than the basket** (SK hynix 0.57×, Samsung 0.68×); from the June highs they are beyond both past full downturns (−39% / −49% and −35% / −42%). Micron (−43%) is inside its own (−54% / −50%) and prices about Base.
- **The company analyses imply a deeper discount still:** they carry net cash, the fast cash return and the preference line, which this method leaves out (SK hynix and Samsung failed k only at 2030 EPS ×0.6 and ×0.5 in their v2 runs).
- **Basis caveat (checkpoint 4):** the multipliers are on today's consensus; under the layer method a rise in peak-year consensus lifts 2028–30 one for one.

### 6. Signposts with dates

| Date | Event | Confirms Base | Earlier or deeper turn | Later or shallower turn |
|---|---|---|---|---|
| ~30 Nov, ~31 Dec | DRAMeXchange / TrendForce monthly contract prints (DDR4 and DDR5 PC, NAND MLC) | DRAM still up m/m; NAND flat | DRAM flat or down m/m; NAND down; spot below contract | DRAM up > 5% m/m; NAND rising again |
| Late Dec–early Jan | TrendForce Q1-27 contract outlook | Blended +0–8% | Conventional DRAM flat or negative; mobile DRAM and NAND down | > +10%; 2H-27 still rising |
| ~14 Nov (Samsung, DART), ~16 Nov (SK hynix, 6-K) | Q3 business reports: LTA terms, deposits, contract liabilities | Ranges without floors | Ranges lowered, renegotiation language, contract liabilities falling | Floors or take-or-pay terms; large deposits |
| 17 Nov | NVIDIA Q3 FY27: Q4 guide, supply commitments (279bn, "primarily memory"), HBM per GPU | Commitments flat to up; guide inside the band | Commitments cut; 8-Hi in place of 12-Hi; inventory up while growth slows | Commitments raised beyond FY29; Q4 guide > ~$124bn |
| ~18 Nov | Anthropic IPO pricing (lab financing) | Priced at or above the marks | Pulled, or priced below the Series H | Well above the marks |
| 10 Dec | ERCOT/PUCT data-center audit to the Texas PUC | Audit closes; energisation resumes under cost and water conditions | Pause extended into 2027, or a statutory moratorium after the Legislature meets (12 Jan) | Pause lifted with clear cost-allocation terms |
| 16 Dec | Micron FQ1-27: FQ2 guide, gross margin against the 86.25% floor, bits, FY27 capex, RPO and deposits | Margin ≥ 86% and sequential growth | Flat price increases in the FQ2 guide; margin guided down; pushouts | RPO > $200bn; more SCAs with floors; prices still up |
| ~7 Jan 2027 | Samsung Q4 preliminary | Operating profit about at consensus | A miss on memory prices | A beat |
| 11–19 Jan 2027 | Governors sworn in (Ohio and Georgia 11 Jan, Texas 19 Jan); Texas Legislature from 12 Jan | Conditions and cost rules, no blanket bans | A statewide moratorium; a hyperscaler moves or cancels ≥ 1 GW over policy | Pledges softened into cost-allocation rules |
| Late Jan (SK hynix ~28 Jan, Samsung ~29 Jan) | 2027 capex figures and Q1-27 bit and price guides | 2027 capex up moderately (~+20% for the three) | 2027 capex +30% or more with fab pull-ins | 2027 flat; fabs staged back |
| Late Jan–early Feb | Hyperscaler 2027 capex figures | K1 2027 ~1.1tn (Base) | A platform guides 2027 flat or down (K1 Bear) | > 1.3tn (Bull) |
| Mid-2027 | 2028 HBM volume and price negotiations | 2028 volumes up, prices flat to down | Prices down sharply or volumes cut: wafers return to DRAM | 2028 sold out at higher prices |
| Ongoing | Foreign flows in Kospi | — | Net selling > USD 20bn in a quarter with DRAM prices falling | Sustained net buying while contract prices still rise |
| Ongoing | CXMT | — | 4F² specs, a named customer and volume; 420k wafers a month reached early | Delays; export controls |
| Quarterly (mid-Jan for Q4) | Smartphone and PC shipments (IDC, Counterpoint) | 2027 flat to slightly down | Another double-digit fall | Recovery |

### 7. For the analyses that lead with this section

- `docs/skhynix-analysis.md`, `docs/samsung-analysis.md` and `docs/kospi-analysis.md` open with the five lines and the implied path (the basket figure and their own); the IRR follows as "what the price implies"; E / R against HY is a reference, not the gate (user rule, 1 Nov).
- Each states its own multiplier ("at today's price the analysis earns k at x× the Base 2028–30 path"); its distance from 1.0 is the margin in cycle terms.
- Rows they read: the H2 EPS path, revenue index, exit P/E (8 / 10 / 11), cash conversion, scenarios and catalysts.

## Engines and tools: notes (paths in the Interface)

- **E1 2026 (~100, range 90–110; build ≈ 94) `[A]`:** OpenAI Q1 5.7 + Q2 6.7 + Q3 ~11 + Q4 ~15 ≈ 39; Anthropic booked Q1 4.73, Q2 11.57, Q3 **16.96** (S-1/A `[F]`; operating loss 0.57bn): nine months 33.3, so the ~55 build needs Q4 ~21.7 (+28% q/q, after +47%). The −6% gap is below the 10% rule; the row is re-set at the next full update. 2025: Anthropic ~4.6 booked (draft S-1) + OpenAI ~13 `[?]` ≈ 18. Run-rates `[E]`: OpenAI ~50bn at end-September (+77% in Q3; ~70bn is its end-2026 target), Anthropic 65bn (July; includes cloud-partner sales, so not like for like); Anthropic's Q3 is ~68bn annualised. OpenAI paid Microsoft 10.0bn in the September quarter: inside E2, not E1.
- **E1 Base:** growth halves each year from ~+90% (2027) as the base grows and price per token keeps falling (Epoch AI: −47% a quarter at constant capability `[E]`). The exit run-rate covers most of 2027's Base.
- **Anthropic IPO (S-1/A No. 2, 10 Nov) `[F]`:** range **$70–78** (×1.19–1.32 the Series H per common share, $58.90); 801.4m primary + 23.6m secondary shares; $26.0bn concurrent Class N placement; 13,087m shares after the deal ($916bn / $968bn / $1,021bn at $70 / $74 / $78). Pricing ~18 Nov, first trade ~19 Nov `[E]`. Obligations (~$901bn + $150–175bn) are ~13× Q3 revenue annualised: the exposure the financing-break Bear describes.

| Cloud (memo, not a row) | Q3-26 USD bn | y/y | Q4-26 | CY26 USD bn / growth | Company 2027 Base used downstream |
|---|---|---|---|---|---|
| Azure | 33.17 `[F]` | +48% (Q2 restated +42%) | guided +49–50% (~36.3 `[A]`) | ~124.8 / ~+45% `[A]` | +38%, at the row (`docs/msft-analysis.md` v3: RPO flat q/q, no backlog support for a premium) |
| Google Cloud | 30.71 `[F]` | +103% (TPU system sales "a meaningful contributor") | ~35.5 `[A]` | ~111.0 / ~+89% `[A]` | +50% = row +12 pp backlog premium (`docs/googl-analysis.md` v2; backlog 561bn, +9% q/q) |
| AWS | **46.0** `[F]` | **+39.3%** (sixth quarter of acceleration) | ~50.0 (+40%) `[A]` | **175.8 / +36.6%** `[A]` | +38%, at the row (`docs/amzn-analysis.md` v2). The CEO projects "over 40%" in **2027 and 2028** (a company projection); backlog 578 |
| OCI | 7.4 (Jun–Aug quarter) `[E]` | +121% | Q2 FY27 cloud revenue guided +65–71% `[E]` | ~28 / ~+115% `[A]` | not analysed |
| **Four clouds** | **~117.3** | **~+59%** `[A]` | ~130.5 `[A]` (run-rate ~522) | **~440 / ~+53%** `[A]` | **~+41%** blended `[A]` (~+42% with AWS at "over 40%") |

- **E2 2026:** ~+53% (2025 base ~286bn: Azure ~86, Google Cloud ~59, AWS ~129, OCI ~13 `[A]`) against the row's ~+50%: current year, gap ~3 pp, below the 5 pp rule, **kept**.
- **E2 2027 Base +38% kept:** the bottom-up blend is ~+41% (Google Cloud's premium on its ~25% share). Run-rate test: the Q4-26 exit run-rate (~520bn) is ~18% above the CY26 average, so +38% needs ~6% sequential growth a quarter after 11–16% in 2026 (Q2 +16%, Q3 +13%, Q4 ~+12% `[A]`); Q4-27 exit growth ~+26%. Google Cloud alone at the row would mean ~3% a quarter, hence its premium.
- **E2 2028:** AWS on management's "over 40%" would lift the four clouds to ~+31% `[A]`, about the Bull (+32%). A company projection `[E]`; the Amazon analysis keeps AWS at the row (sensitivity 12.3%), so it is a Bull-side signpost, not a move.
- **T1:** 30m paid seats in July (~6.7% of commercial Office seats) `[E]`; no count since (premium seats "millions"); M365 commercial seats +5% with revenue +17% (18% cc): value growth on slowing seats. Copilot moves to consumption pricing, so seats will understate revenue later.
- **T2:** Cursor ~3–4bn ARR (mid-2026), Claude Code > 2.5bn run-rate (Feb 2026) `[E]`; no reliable total, so growth only.
- **T3:** seat-based software sold off on agent substitution (IGV −30% from its peak in six sessions in Feb; ServiceNow −57% from its 2025 peak in April) `[E]`; Salesforce organic growth high single digits. Base: AI SKUs offset seat compression; growth 7–8%. ServiceNow Q3: revenue USD 4.11bn (+20.5%), cRPO 13.65bn; the share fell 18% after hours (cause not read `[?]`).
- **T4:** BTOS 17–20% (Dec 2025–May 2026) `[F]`; 21.7% in July `[E]`; six-month expectations fell from +4.7 to +2.8 points `[E]`.
- **Monetisation ratio:** rises in every scenario (Bear: capex cut; Base and Bull: revenue grows faster), so the build-out is not paid for in any scenario within the window; the hyperscalers' own AI revenue and internal use are not in it. Base 2028–29 (275 / 1,170 = 0.235; 360 / 1,170 = 0.308) sits at or above the Bull (370 / 1,550 = 0.239; 515 / 1,700 = 0.303) because the plateau holds capex flat. Read it for direction; the durability measure is the K1 return gauge.

## Layer baskets: method, company check, exit cross-check

**Method v2.1** (`references/model.py`, switch `K1D` on by default): P/E on calendarised CY27 consensus (Yahoo 7 Nov); each layer converts EPS into free cash after growth capex at its cash conversion c, pays payout × EPS, and accrues (c − payout) × EPS once into V_t and V_T (negative for the platforms: net debt builds). NOK via the Equity BBB USD/NOK path; stub 54 days; E = Base NOK − NIBOR window, R = Base 2027 − Bear 2027. For memory the decision leads with the Memory cycle section.

- **Bear-cap diagnostic (`model.py BEARCAP`):** only memory changes (H2 Bear +5.3% → −15.2% a year, Bear 2027 +19.9% → −48.5%, E / R 0.867 → 0.195; all six Bear −8.5%, Bear 2027 −37.7%). Not the rule (memory's P/E on trough earnings normally rises); shown because memory's E / R rests on the 8× Bear multiple.
- **Consensus basis (7 Nov; fiscal-year labels checked with `trend2.py`):** NVIDIA CY27 **$15.21** by calendar quarters (FY Jan-28 $15.91); Micron **$191.8** by calendar quarters (FY27 176.50, FY28 207.76); Marvell (7.08), Salesforce and Snowflake 1/12 + 11/12; Oracle 5/12 + 7/12 (9.84); Lam ½ + ½ (10.94); Intuit 7/12 + 5/12 (25.12); Microsoft 22.09; ASML EUR 56.43 = USD 62.89 at 1.1143; SK hynix KRW 529,348; Samsung KRW 77,324. Broadcom, Applied (FY Oct-27) and Adobe (FY Nov-27) stand for CY27 and understate it when growing (Broadcom by up to ~5%) `[A]`.
- "Cons. EPS CY26→27" for E is distorted by Alphabet's and Amazon's one-off CY26 gains and Meta's legal charge (+10–37% on the others). Memory's "−35%" means memory still pays 12% if earnings fall by less than 35% a year from the Base 2027 level (Base ~−27% a year to mid-cycle).
- **Why the E 2027 point barely moves the E return:** 2027 EPS enters only through the 2027 dividend (payout 34%) and the retained cash ((c − payout) × EPS = −0.54 × EPS), which offset. The linear cash rule is a simplification (checkpoint 6).
- CoreWeave (USD 26bn at $46.40 on 6 Nov; 2026 closing low $43.66 on 5 Nov; $48.73 on 10 Nov; loss-making) is a memo, not in a basket.

**Company check** (each name on its layer path and method, `references/members.py`; NOK, 6 Nov prices, 7 Nov consensus, with the K1 re-set) against the company analyses (own currency, Base = NOK in Base, at their own run prices, margin against their own P_k):

| Layer / name | P/E CY27 | Bear / **Base** / Bull | Bear 2027 | E / R | Company analysis (Base, margin of safety, price) |
|---|---|---|---|---|---|
| H1 NVDA | 12.3 | -7.1 / **11.4** / 28.7 | -35.4 | 0.160 | **20.9%, P_k $212.1 at $168.89 (+25.6%; v1.3, 11 Nov)**, built on the H1 path before the re-set. On the re-set path ≈ **17.0%, P_k ≈ $192 (+13.4%)** `[A]`; it restates at its 17 Nov run |
| H1 AVGO | 15.1 | -13.1 / **4.2** / 20.3 | -47.4 | -0.004 | — |
| H1 AMD / MRVL | 26.8 / 19.9 | Bear -27.8 / -20.6; **Base -13.4 / -4.8**; Bull -0.0 / 10.0 | -70.4 / -60.2 | -0.335 / -0.182 | — |
| H2 MU | 3.6 | -5.0 / **9.7** / 20.4 | -12.2 | 0.210 | **18.3%, +14.5% at $656.39 (v3, 5 Nov; P_k ~$752)**; E / R 0.616; at $690.00 **≈ +9.0%**; price implies **1.08× Base 2028–30** |
| H2 SK hynix | 2.1 | 12.8 / **30.5** / 43.3 | +47.8 | 1.715 | **21.1%, +23.5% at KRW 1,487,000 (v2, 28 Oct)**; capped Bear −14.7%, E / R 0.215; at 1,132,000 (P_k ~1,836,000) ≈ +62%; price implies **0.57× Base** |
| H2 Samsung | 2.4 | 8.0 / **24.8** / 37.1 | +29.5 | 1.117 | **23.3%, +32.0% at KRW 232,000 (v2, 29 Oct)**; preference 25.6%; capped Bear −10.5%, E / R 0.249; at 188,700 (P_k ~306,000) ≈ +62%; price implies **0.68× Base** |
| H3 TSM | 16.1 | -7.2 / **13.0** / 24.0 | -34.5 | 0.187 | **9.5%, P_k $369.8 at $396.48 (−6.7%; v1.2, 11 Nov)**; reads H3, which the K1 re-set leaves unchanged |
| H3 ASML / AMAT / LRCX | 22.7 / 17.9 / 18.3 | Bear -17.1 / -10.5 / -11.1; **Base 0.9 / 9.0 / 8.2**; Bull 10.7 / 19.5 / 18.7 | -53.6 / -41.3 / -42.6 | -0.065 / 0.095 / 0.079 | — |
| E MSFT | 24.0 | -9.8 / **3.9** / 12.5 | -40.9 | -0.011 | **9.6%, P_k $495.9 at $530.61 (−6.5%; v3, 7 Nov re-mark)**; exit P/E 23; own c .19 / .31 / .42. The re-set adds ≈ +0.2 pp (cash) to +0.8 pp (lower D&A), P_k ≈ $499–507 (margin −6.1% to −4.4%) `[A]` |
| E GOOGL | 19.0 | -2.7 / **12.0** / 21.3 | -25.5 | 0.217 | **9.1%, P_k $262.3 at $284.78 (−7.9%; v2, 7 Nov re-mark, kept 11 Nov)**. Re-set ≈ +0.3 to +1.2 pp, P_k ≈ $265–271 (margin −7.0% to −4.7%) `[A]` |
| E AMZN | 24.3 | -10.1 / **3.5** / 12.1 | -41.6 | -0.020 | **5.2%, P_k $222.2 at $270.87 (−17.9%; 11 Nov re-mark)**; exit P/E 22; Anthropic and OpenAI stakes apart. Re-set ≈ +0.4 to +1.5 pp, P_k ≈ $225–233 (margin −16.9% to −14.1%) `[A]` |
| E META / ORCL | 18.0 / 11.8 | Bear -0.9 / +13.7; **Base 14.1 / 30.9**; Bull 23.6 / 41.8 | -21.1 / +20.3 | 0.295 / 2.053 | — (Oracle: layer method meaningless, priced near the Bear multiple) |

- **The layer method is not a per-name valuation:** names priced below the Bear exit multiple re-rate up in the Bear (Oracle, SK hynix, Samsung). It runs ~2–5 pp below the company analyses for NVIDIA, TSMC and Micron (net cash, stakes, payout) and ~5–9 pp below for SK hynix and Samsung (fast cash return, net cash ~8–10% of the price, preference line); for the platforms the gap runs either way (1 Nov, same prices: Microsoft ~+6 pp above, Alphabet −2.3 pp below, Amazon +3.6 pp above).
- **Meta:** on the layer method only −21% in the Bear 2027 (E-rest Bear .88 / .88 / .97 / 1.05), while the analysed platforms lose 34–42% and Meta lost 64% in 2022 on an EPS fall of 38% `[E]`. With Meta on the analysed platforms' Bear (.75 / .70 / .77 / .86) the layer Bear blend would be .757 / .705 / .778 / .861 (2027 gap −0.063). The rule keeps the old path for the unanalysed rest; **a Meta analysis is the fix** (checkpoint 9).

**Exit cross-check** (IAF Step 3, Track A form): buyer's implied return at the Base exit = cash yield (c 2029 ÷ exit P/E) + long-run growth, against World's exit P/E 17 and mid-cycle return 8.2%:

| Layer | Exit P/E (Base) | c 2029 | Cash yield | + growth 5.3% (World) | + the layer's own 2029–30 growth | Reading |
|---|---|---|---|---|---|---|
| H1 Compute | 17 | 0.90 | 5.3% | 10.6% | — (2030 is the normalised level) | ≥ World: the exit is not generous on a return basis |
| H2 Memory | 10 | 0.60 | 6.0% | 11.3% | — (normalised) | ≥ World |
| H3 Foundry and equipment | 18 | 0.82 | 4.6% | 9.9% | +5.5% → 10.1% | ≥ World |
| H4 Networking and DC infra | 20 | 0.90 | 4.5% | 9.8% | +5.3% → 9.8% | ≥ World (the 2029–30 step is lower operating leverage in the normalised year) |
| E Platforms | 21 | 0.36 | 1.7% | **7.0%** | +8.5% → **10.2%** | Below World on World's growth; the reason is growth: platforms reinvest ~65% of earnings at exit and grow ~8.5% a year into 2030 (Amazon +10%, Microsoft +9%) |
| T Software | 20 | 0.80 | 4.0% | 9.3% | +7.2% → 11.2% | ≥ World |

**Memory sensitivities** (Base / Bear 2027, NOK; 6 Nov prices, 7 Nov consensus):

| Change | MU | SK hynix | Samsung |
|---|---|---|---|
| Model | 9.7 / -12.2 | 30.5 / +47.8 | 24.8 / +29.5 |
| Cash conversion −0.2 | 6.7 / -15.9 | 27.0 / +41.5 | 21.5 / +24.0 |
| Base exit P/E 8 (not 10) | 4.1 / — | 23.9 / — | 18.5 / — |
| Bear exit P/E 6 (not 8) | — / -30.9 | — / +16.3 | — / +1.9 |
| Bear capped at today's P/E (Bear a year / Bear 2027 / E / R) | -19.5 / -53.3 / 0.080 | -11.7 / -44.4 / **0.243** | -14.0 / -47.1 / **0.215** |
| **Price-implied 2028–30 multiplier on Base for k / for 0%** | **1.08 / 0.72** | **0.57 / 0.37** | **0.68 / 0.44** |

- The Korean names are well above k on the layer method, also with lower cash conversion or a Base exit P/E of 8. Micron fails k on the layer method (9.7%) while its own analysis (v3) clears. Capped-Bear E / R (0.24 and 0.22) is just below the HY reference: a reference, not the gate.
- **The 2030 mid-cycle (0.35 of CY27 consensus) decides it:** SK hynix fails at 2030 EPS ×0.6 and Samsung at ×0.5 in their analyses; here it is the price-implied multiplier.

## EPS paths and cash conversion: basis (values in the Interface)

- **Base** paths as set 12 Oct except E 2027 (.92, set 29 Oct on the company blend) and, from the 11 Nov K1 re-set, H1 and H4 2028–30 and the E Base cash conversion. Year-1 haircut on consensus ~5–8% (as the Equity BBB World path); H1 follows its revenue (+3% and −1% after 2027) with a small margin give-back as custom ASICs and memory costs press GPU margins; H2 matches its revenue index.
- **K1 re-set `[A]`:** H1 and H4 Base EPS 2028–30 interpolated between Base and the revenue-consistent Bear by the revenue gap, from the unrounded revenue (2030 at 2029's gap): H1 .906 / .884 / .871, H4 .935 / .939 / .992 (moves −0.07 to −0.13, above the 0.05 rule). E Base cash conversion: 0.86 (after the cash-tax effect of expensing) × the K1 cut of 80bn and 130bn ÷ the basket's earnings on its path (580.7bn × 1.07 and × 1.17) adds +.11 and +.16. The E EPS path is kept: lower depreciation would add only +.005 / +.022 / +.045 in 2028–30, below the 0.05 rule. H3 kept; H2 and T do not read K1.
- **Bear:** H1 and H3 take NVIDIA's and TSMC's revenue-consistent Bears; H4 (no analysis) revenue −20% in 2028 at ~1.4× operating leverage, flat in 2029 (index 110 / 88 / 88); E on the Microsoft, Alphabet and Amazon Bears for 83% of the basket and the E-rest row for Meta and Oracle (bottom-up, so evidence); T untested: its Bear has EPS +9% in 2029 on revenue +3% (checkpoint 9).
- **Bull:** E on the three companies' Bulls (Amazon 1.03 / 1.28 / 1.51 / 1.74 on AWS at the E2 Bull) and the rest row; H1, H3 and H4 Bulls fit their revenue paths. NVIDIA, TSMC and Micron take the layer path as input, so they are not evidence for the Base level.

**E-layer company check (1 Nov; company EPS ÷ CY27 consensus of 1 Nov: Microsoft 22.08, Alphabet 14.84, Amazon 10.65):**

| Scenario | Microsoft v3 | Alphabet v2 | Amazon v2 | Rest row | **Blend** (30 Oct weights .326 / .290 / .219 / .166) | Layer path | Gaps |
|---|---|---|---|---|---|---|---|
| Base | .941 / 1.060 / 1.183 / 1.286 | .854 / .963 / 1.071 / 1.176 | .910 / 1.059 / 1.190 / 1.314 | .97 / 1.07 / 1.17 / 1.27 | **.914 / 1.033 / 1.150 / 1.258** | .92 / 1.07 / 1.17 / 1.27 | −0.006 / **−0.037** / −0.020 / −0.012 |
| Bear | .826 / .807 / .866 / .935 | .705 / .664 / .746 / .828 | .708 / .584 / .662 / .772 | .88 / .88 / .97 / 1.05 | **.774 / .729 / .804 / .887** | .82 / .75 / .82 / .91 | **−0.046** / −0.021 / −0.016 / −0.023 |
| Bull | .994 / 1.190 / 1.377 / 1.535 | .930 / 1.124 / 1.278 / 1.441 | .987 / 1.226 / 1.441 / 1.665 | 1.00 / 1.13 / 1.27 / 1.41 | **.975 / 1.169 / 1.345 / 1.516** | 1.00 / 1.19 / 1.37 / 1.54 | −0.025 / −0.021 / −0.025 / −0.024 |

- **Base 2027 .92 holds** (blend .914; DNB Teknologi ≈ .91). The 7 Nov consensus moves the blend by < 0.005 (Alphabet .854 → .848). Next to watch: Base 2028 (−0.037) and Bear 2027 (−0.046).
- **Cash conversion c** `[A]` (free cash after growth capex, working capital and stakes, less buybacks or withholding that only offset dilution, ÷ EPS), calibrated on the company analyses: NVIDIA .77 / .95 / .97 (Bear .82 / 1.00 / .90); Micron .71 / .67 / .60; TSMC .63 / .68 / .74 with ASML, Applied and Lam ~.95; Microsoft v3 .19 / .31 / .42; Alphabet v2 −.38 / −.20 / .02; Amazon v2 −.53 / −.20 / .08 (v1 Bear −.58 / .00 / .30, Bull −.75 / −.52 / −.22); Meta like Alphabet, Oracle ~−.5 / −.4 / .0. The cap-weighted E figure (1 Nov) ≈ −.23 / −.04 / .16 against −.20 / .00 / .20 (gaps ≤ 0.04, kept); the K1 re-set adds +.11 / +.16, giving −.20 / .11 / .36. The company analyses take their capex as a share of K1, so their own c rises the same way at their next runs. Software .80 (consensus EPS excludes stock compensation); networking .90 (asset-light, no analysis).
- **Exit P/E:** Base near the 10-year S&P 500 average (19.1) for platforms and software with growth above the market; compute at today's level less a cycle discount; memory mid-cycle. Bear ≈ the 2022 trough, reached at end-2027. Company analyses set their own (Microsoft 23, Amazon 22).

## Scenario definitions

| Scenario | Weight (convention) | Equity BBB scenario | AI catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|
| **Bear** | 25% | Bear (recession H1 2027 + oil Bear) | **Financing break** + monetisation disappointment; memory overshoot 2028 | Lab revenue growth stalls (price war, enterprise budgets cut); a lab misses commitments; Oracle/neocloud contracts renegotiated; AI credit tightens; hyperscalers cut 2028 capex 16%; GPU and memory prices fall | H1 2027 | Lab run-rate growth < 10% q/q for two quarters · a hyperscaler guides next-year capex flat/down · Oracle cut to BB+ or RPO falls · capex/OCF > 100% with debt share > 40% · DRAM contract prices fall q/q · new vendor loans or guarantees > USD 50bn in a quarter, or one called |
| **Base** | 50% | Base (AI boom slows to trend) | Contracted 2027 build, then digestion | 2027 capex +42% on backlog and supply limits; 2028–29 a digestion plateau (+4.5%, 0%) while the 2026–27 build earns in; lab revenue ~3.6× by 2029; memory normalises | Ongoing | Capex guidance within ±10% · NVIDIA within its guide · lab run-rate +15–30% q/q · BTOS rising ~1 pt a quarter |
| **Bull** | 25% | Bull (soft landing) | **Agentic adoption** | Adoption broadens; tokens per user multiply; lab revenue +130% in 2027; capex to ~1.3–1.7tn; supply limits turn demand into prices and margins | Q2 2027 | 2027 capex consensus > USD 1.3tn · lab run-rate > USD 250bn by mid-2027 · Copilot seats > 70m · BTOS > 30% |

- The AI Bear sits inside the equity Bear: a recession alone slows but does not break contracted 2027 builds; the financing break turns 2028 negative. State siting policy is a second route to the Bear's 2028 capex cut (a signpost; the definitions are unchanged).
- Tail risks not modelled: Taiwan conflict; export-control escalation (NVIDIA already assumes no China data-center compute revenue `[F]`).

## Drivers

- **Money in:** capex guidance has risen every quarter (guided 2026 spending > 150% above initial estimates `[E]`). Debt funds about a third of the increase; Alphabet (ATM) and Oracle sold equity; leases (~820bn) sit off balance sheet; Oracle is one notch above high yield. Vendor and circular financing is ≥ USD 270bn, led by NVIDIA's up-to-105bn guaranty for OpenAI's Ohio campus; no public series nets it out of demand `[?]`.
- **Hardware:** supply, not demand, limits 2026–27 (CoWoS, HBM and power sold out or short): that supports 2027 volumes and prices in every scenario and shifts the risk to 2028. Custom silicon gains (Google TPU systems sold externally, Broadcom AI +221% y/y, AMD MI450/Helios) `[E]`.
- **Engines:** two labs dominate visible revenue and grow faster than any software company has; their commitments are larger still (OpenAI ~600bn of compute by 2030, ~115bn of cash burn through 2029 `[E]`). **The labs' ability to keep raising money is the hinge between engines and hardware.**
- **Tools:** copilots ramp and pricing moves to consumption; AI-native tools (coding agents) grow fastest; seat-based multiples have compressed while Palantir and Snowflake price the winners (CY27 P/Es in the appendix). Gartner puts GenAI in the "trough of disillusionment" in 2026 (total AI spending 2.7tn, +49.5%; AI infrastructure 1.48tn → 1.98tn in 2027 `[E]`; broad definitions, cross-check only).
- **Power (H5):** US data centers need ~68 GW of new capacity 2026–28, ~30 GW covered, a ~38 GW gap (Morgan Stanley, Aug 2026, via a secondary summary `[E]`); interconnection 4+ years; gas turbines ~36 months order-to-operation `[E]`. Power stretches projects in a Bear and caps volume in a Bull.

**US policy channels after the 3 Nov midterms** (does the result change K1, its financing or the layer revenues for 2027–29?):

| Channel | What is stated or proposed | What can happen, and when | Rows | Moves Base? |
|---|---|---|---|---|
| Federal: data-center moratorium | Sanders and Ocasio-Cortez's AI Data Center Moratorium Act (Mar 2026) `[E]` | Cannot become law over a veto and needs 60 Senate votes | K1 | No |
| Federal: grid-cost allocation | Ratepayer Protection Act passed the House 417–3; Senate cloture failed 57–43 (30 Sep). Hyperscalers pledged (Mar 2026) to pay for new generation `[E]` | A binding version can draw votes from both parties from 3 Jan 2027 `[A]` | Cost per GW, not volume | No |
| Federal: tax | Permanent expensing (2025 law); CHIPS 48D credit (35%) for construction begun by end-2026 `[E]` | Repeal or extension needs the President; none expected `[A]` | K3 | No |
| Federal: export controls | Democrats object to NVIDIA's H200 licence for China; GAIN AI and SAFE Chips bills `[E]` | Could ride the FY28 NDAA in 2027 `[A]`; NVIDIA's guidance already excludes China data-center compute `[F]` | H1 (China tail) | No |
| Federal: oversight, appropriations | Hearings and subpoenas; FY27 stopgap ends 11 Dec (current Congress); FY28 riders possible from Oct 2027; FERC and NRC confirmations from January `[E]` | Headlines and delays, not paths | K1 (sentiment) | No |
| **States: Texas** | ~27% of planned US data-center GW `[E]`. Abbott's pause since 3 Aug on new loads ≥ 75 MW without own generation until an ERCOT/PUCT audit of the ~192 GW Batch Zero cohort (due 10 Dec); TCEQ permits halted since 21 Sep. Hinojosa (from 19 Jan) pledges a moratorium until the Legislature (from 12 Jan) passes protections `[E]` | Agency directives and PUC appointments; a statutory ban needs the Legislature. The pause predates the Q3 capex guides | K1 2028–29, H4, H5 | No: a risk to 2028 |
| **States: Georgia, Ohio, others** | Georgia (~7%): a temporary statewide pause pledged. Ohio (~5%): a conditional moratorium. Pennsylvania ~5%. Voters rejected data centers in 40 of 41 local ballot measures `[E]` | From 11 Jan; siting slower and costlier | K1 2028–29 | No: a risk to 2028 |
| Companies | No guidance change from a hyperscaler, NVIDIA or a utility; concessions instead (community commitments, Google's USD 1bn in local programmes) `[E]` | Next read-outs: NVIDIA (17 Nov), 2027 capex (late Jan–early Feb) | K1 | No |
| Sell side | No published hyperscaler capex cut. Ives: > USD 1tn in 2027. UBS: ~30% of 2028 capacity at risk (secondary); Goldman's ~45% unverified `[E]`/`[?]` | — | K1 2028 | No |

**Reading:** the market bought the payers and sold the receivers (30 Oct–5 Nov: Amazon +8%, Micron −24%, Vertiv −24%), but no company has said capex will be lower. The 2027 build is contracted and power-limited. 2028 carries the risk, and the Base already holds a plateau there; the illustrative slip (~3–4% of K1 2028 `[A]`, an upper bound) is below the 5% minimum change and inside the Base range. A statutory moratorium in Texas, or a hyperscaler moving or cancelling ≥ 1 GW over policy, would be the evidence to move it. A cap on new US sites raises the value of built capacity (supports E2 pricing) and lands on H1, H2, H4 and H5 through units.

## Against World and high yield

| Base, NOK, before fees | Return to end-2029 | Bear 2027 | E / R |
|---|---|---|---|
| Nordic HY market (`hy-market-bbb`, 5 Nov, kept 11 Nov) | 7.2% | −0.4% | **0.254** (reference; 0.216 with the Bear read as a shock) |
| MSCI World (Equity BBB, 6 Nov) | 6.6% | −18.3% | 0.080 |
| AI platforms (E) | 8.6% | −32.3% | 0.110 |
| AI compute (H1) | 7.5% | −42.1% | 0.068 |
| **AI memory (H2)** | **21.6%** | +19.9% (−48.5% with the Bear capped) | **0.867** (0.195 capped); for memory the cycle is the gate, not E / R |
| AI foundry and equipment (H3) | 10.2% | −39.2% | 0.123 |
| All AI baskets, cap-weighted | ≈9.2% | ≈−31.7% | — |
| NVIDIA (`docs/nvda-analysis.md` v1.3, $168.89 on 10 Nov; USD = NOK in Base) | 20.9% on its own build (H1 path before the K1 re-set); ≈ 17.0% on the re-set path `[A]` | see the analysis | restated at its 17 Nov run |
| **SK hynix / Samsung** (v2, KRW 1,487,000 / 232,000; KRW = NOK in Base) | **21.1% / 23.3%** at their run prices | +1% / +1.9% (decision Bear); −47% / −45% capped | 0.649 / 0.750; **0.215 / 0.249 capped** |
| Microsoft / Alphabet / Amazon / TSMC v1.2 / Micron v3 (at their run prices) | 9.6% / 9.1% / 5.2% / 9.5% / 18.3%; the platforms before the K1 re-set, which adds ≈ +0.2 to +1.5 pp `[A]` | see the analyses | see the analyses |

- **The HY rule (E / R against 0.254):** not the gate for memory (user, 1 Nov). No other basket reaches it: foundry 0.123, platforms 0.110, compute 0.068; foundry and platforms are above World (0.080), compute below. Foundry (10.2%) and platforms (8.6%) give more than World (6.6%) and the HY market (7.2%); compute (7.5%) is about the HY market. Their Bear 2027 loss is 1.8× (platforms) to 2.3× (compute) World's.
- The AI case is still a bet on growth after 2027 that the Base does not include: compute needs ~3% a year of EPS growth after 2027 for 12%, while its Base digests at about −2% a year to 2030 (.92 → .87); platforms need ~15% a year.
- **Triggers (where a layer pays k):** baskets at a CY27 P/E of compute ~12.1 (−11.8% from 13.7 now), platforms ~19.1 (−9.1%), foundry ~16.5 (−4.7%), memory ~3.38 (2.64 now: +28%, cleared). In cycle terms compute needs 1.14× its Base 2028–30; memory clears at 0.75×. Companies (P_k at each analysis's run price): clear: NVIDIA $212.1 at $168.89 (+25.6%; ≈ $192, +13.4%, on the re-set H1 path `[A]`), Micron ~$752 at $656.39 (+14.5%), SK hynix ~1,836,000 and Samsung ~306,000 (≈ +62% at the 6 Nov close); fail: TSMC $369.8 at $396.48 (−6.7%), Microsoft $495.9 at $530.61 (−6.5%), Alphabet $262.3 at $284.78 (−7.9%), Amazon $222.2 at $270.87 (−17.9%). The K1 re-set lifts the three platforms' P_k by ≈ $3–11 `[A]`; at the upper bound Microsoft (−4.4%) and Alphabet (−4.7%) enter the ±5% band.

## Signposts and monitoring

| Signpost | Threshold (Bear / Bull) | Now (11 Nov) | Source |
|---|---|---|---|
| Next-year capex guidance | flat/down / 2027 consensus > 1.3tn | **Neither.** Meta 2026 135–145bn, 2027 "continue investing aggressively"; Microsoft CY26 ~170bn (slippage, not a cut); Alphabet 195–205bn, 2027 "increase significantly"; Amazon ~220bn, 2027 "meaningfully increase". 2027 consensus ~1.1tn | Company reports `[F]`/`[E]` |
| K1 2027 first figures (late Jan–early Feb 2027) | < 1,000 / > 1,300; 1,050–1,250 confirms Base | Not yet guided; 2026 ~815 on nine-month actuals and Q4 guides | Company reports |
| K1 return gauge (January roll-forward, and when K1 or E2 moves) | Coverage of the 10% need in 2028 < 60% / > 90% | 70% (2028), 63% (2029) | `references/k1ret.py` |
| GPU rental indices (Silicon Data H100, B200; monthly) | B200 −20% from its 2026 high for three months / still rising with the curve in contango into mid-2027 | B200 $5.62 (1 Sep, +27.6% year to date; 12-month 5.39); H100 $2.75 (27 Jul) | Silicon Data `[E]` |
| FCF after shareholder returns, the five | < −50bn a quarter for two quarters with E2 growth slowing / positive | −48.8bn (Q3-26); −66.7bn TTM | Filings `[F]` |
| Contracted backlog K4, q/q | Total falls q/q, or two of four flat or down / > USD 2.8tn by Q4-26 | **~2,480 (+3%)**: Microsoft flat (677), Google Cloud +9% (561), AWS +16.5% (578), Oracle 664 (Aug) | Company reports `[F]`/`[E]` |
| E2 four-cloud growth, quarterly y/y | < 30% for two quarters in 2027 / > 45% through H1-27 | **~+59% in Q3-26** `[A]` (Azure +48%, Google Cloud +103%, AWS +39.3%, OCI +121%) | Company reports `[F]` |
| AWS growth against E2 | AWS < 30% in 2027 / AWS > 40% through 2027 (management: "over 40%" in 2027 and 2028 against the row's +38% / +25%) | +39.3% in Q3; backlog 578, 3.1× the run-rate | Amazon `[F]` |
| NVIDIA Q3 FY27 (**17 Nov**) | Q4 guide below Q3 or gross margin < 73% / Q4 guide > ~USD 124bn (+15% q/q) | Q3 guide 108.0bn, GM 74% | NVIDIA `[F]` |
| NVIDIA supply commitments and working capital | Commitments cut, DSO > 70 or inventory > 40bn with growth slowing / commitments raised | 279bn ("primarily memory": a memory signpost too); DSO 60; inventory 31.6bn | 10-Q `[F]` |
| TSMC monthly revenue (~10th) | y/y < +25% for two months in H1-27 / > +45% into 2027 | October NT$586.89bn, **+59.7%** y/y (September +54.6%): Bull side for a second month, not crossed (the line runs into 2027). Next ~10 Dec | TSMC 6-K `[F]` |
| TSMC Q4 report (mid-Jan 2027): 2027 revenue and capex guide | 2027 growth < +20% in USD or capex flat / ≥ +30% with capex ≥ 75bn | 2026 ~+44%; capex 60–64bn; November appropriations $40.93bn lean to the Bull side | TSMC |
| Lab run-rates | < +10% q/q twice / > 250bn by mid-2027 | OpenAI ~50bn (end-Sep; +77% in Q3); Anthropic booked Q3 $16.96bn (+47% q/q; ~68bn annualised) `[F]` | FT/Reuters, CNBC `[E]`; S-1/A `[F]` |
| Oracle credit | BB+ / upgrade | BBB− (S&P), Baa2 negative | Agencies `[E]` |
| Capex ÷ OCF and debt share (five) | > 100% and > 40% / falling | **First leg crossed:** the five ~116% in Q3 `[A]` (Amazon 179%, Oracle ~124% `[E]`, Alphabet 121%, Meta 106%, Microsoft 68%). Debt leg not measured for the five (FactSet's 32% is LTM June) | Q3 releases `[F]`; FactSet `[E]` |
| Platform equity funding | A platform sells new equity beyond employee withholding / buybacks resume | **Bear side crossed (Q3):** Alphabet sold 12.4bn through its ATM (36m shares) against 5.4bn of withholding; 27.6bn left. Meta Class C from Jan 2027 for "capital raising"; Oracle 20bn. No buybacks at Amazon, Alphabet or Meta | Alphabet Q3 release `[F]`; filings |
| DRAM contract prices | Fall q/q / > +10% q/q into 2027 | Q4-26 conventional +10–15%, blended ~+20%; mobile DRAM 0–5%; DDR4 8Gb fixed $27.50 (Oct, a record) | TrendForce; DRAMeXchange `[E]` |
| DRAM contract prices in 2H-27 | Falling q/q / still rising (management's "tight through 2028") | Q1-27 +3–8%; dated memory signposts in the Memory cycle section | TrendForce `[E]`, Micron |
| NAND contract prices | Down q/q in 1H-27 / still rising in 2H-27 | Q4-26 +15–20%, 128Gb MLC flat in October; UBS NAND peak CQ3-27; 512Gb TLC wafer spot −4.33% w/w (4 Nov; spot, not contract) | TrendForce; press `[E]` |
| Micron SCAs and commitments | RPO falls or floors renegotiated / RPO > USD 200bn, SCA share well above 35% | 26 SCAs, RPO ~150bn, > 35% of revenue through 2030; > 75% of 2027 output committed. Next: FQ1-27 on **16 Dec** | Micron `[F]`/`[E]` |
| Memory LTAs: SK hynix, Samsung | Customers renegotiate ranges down, or LTA shares fall / floors disclosed, or contract share > 60% of capacity | SK hynix 14 customers, > 50% of 2027–28 capacity; Samsung 10 signed, 10 in talks, target 60–70%. No floors disclosed; ceilings bind in Q4-26. Next: Q3 business reports **~14 Nov (Samsung), ~16 Nov (SK hynix)** | Company calls via the analyses `[F]`/`[E]` |
| CXMT 4F² DRAM | Specs + named customer + volume shipments in 2026 / claim slips | Claim only, no specs (13 Oct); Micron not pursuing 4F²; commercial "after 2028" `[E]`; ~320k → ~420k wafers a month by 2027 `[E]` | Company statements `[E]`/`[F]` |
| **Non-K1 compute funding** (neoclouds, xAI, labs' own and leased builds) | Bear: any two of (a) NVIDIA ACIE revenue down q/q for two quarters; (b) CoreWeave + Nebius + SpaceX SI capex down q/q for two quarters, or 2027 capex guided below 2026; (c) a neocloud misses a payment, renegotiates a contract or raises at distressed terms, or ≥ USD 50bn of lab compute obligations lapse in a quarter for counterparty financing / Bull: ACIE ≥ 50% of data center for two quarters with named non-K1 capex guided ≥ +50% for 2027, or neocloud debt refinanced at investment-grade-like terms | **Neither, leans Base.** ACIE $40.3bn, 45.3% of data center (Q2 FY27) `[F]`. CoreWeave Q3 revenue $3,661m (+168%), backlog ~$132.5bn, 2026 guide $13.0–13.3bn, capex $37–39bn (Q3 $9.4bn), ~$9bn of prepayments expected in three months, $4.2bn converts upsized, a first ATM (up to 35m shares), cost of debt 7.9%, no unsecured debt at current yields `[F]`/`[E]`; $48.73 (10 Nov) against its low of $43.66. Nebius 2026 capex $20–25bn `[E]`; SpaceX SI capex $16.4bn in Q3 `[F]`; Anthropic obligations subject to counterparty conditions $186.2bn `[F]`. Next: Nebius Q3 (12 Nov), NVIDIA (17 Nov) | NVIDIA 10-Q; CoreWeave 8-K; SpaceX filings; Nebius; Anthropic S-1/A |
| US data-center siting policy | A statewide moratorium by statute or order in a state with ≥ 5% of planned US GW, the Texas pause extended into 2027 after the 10 Dec audit, or a hyperscaler moving or cancelling ≥ 1 GW over policy / the audit closes and energisation resumes under cost-allocation rules | Pledges won in Texas (~27%), Georgia (~7%) and Ohio (~5%); Texas pause since 3 Aug; no law, cancellation or guidance change. Next: 10 Dec; 11, 12 and 19 Jan | Wells Fargo, CNBC, Fortune, Energy News Beat `[E]` |
| Federal AI and data-center law | A moratorium or binding siting limit signed into law, or export rules beyond China / a bipartisan law setting cost allocation and permitting terms | Nothing before the new Congress (3 Jan 2027); no export rule published (NVIDIA puts its exposure beyond China at ≈ 5–8% of revenue `[A]`); House briefing 18 Nov, Trump–Xi 18–19 Nov; FY28 NDAA the likely vehicle | IAPP, Al Jazeera, Bloomberg `[E]` |
| M365 Copilot seats | < 45m mid-2027 / > 70m | 30m (Jul); no count since (premium seats "millions") | Microsoft `[E]` |
| BTOS AI use | < 22% mid-2027 / > 30% | 17–20% (May), 21.7% (Jul) | Census `[F]`/`[E]` |
| Basket P/E CY27: compute / platforms / foundry / memory | ≤ 12.1 / ≤ 19.1 / ≤ 16.5 / ≤ 3.38 (k trigger) | 13.7 / 21.0 / 17.3 / 2.64 (6 Nov): compute −11.8%, platforms −9.1%, foundry −4.7% from their triggers; memory through its trigger (read with the multiplier, 0.75×). NVIDIA alone at $168.89 would put compute at ~12.9 `[A]` | This baseline |
| Lab financing: Anthropic IPO, OpenAI raises | IPO pulled or priced below the Series H (USD 965bn post-money, May 2026); OpenAI raise fails or misses SB Energy lease payments / IPO above those marks, OpenAI rated | **Pending:** S-1/A range $70–78, ×1.19–1.32 the Series H per common share ($58.90). Read per share: the 965bn post-money and the $0.92–1.02tn post-deal value count different share bases. A pricing inside the range (~18 Nov) crosses the Bull line and triggers a re-test. Amazon carries Anthropic at an implied ~1.16tn | S-1, S-1/A `[F]`; Reuters, Bloomberg `[E]` |
| Vendor financing (flow) | New loans, guarantees or equity commitments to AI customers > USD 50bn in a quarter, or any guarantee called or stake impaired / commitments falling | Level ≥ USD 270bn (up to ~286bn). New supplier equity in the Class N placement ≤ ~16.5bn in Q4: below the flow line | 8-K, 10-Q, S-1/A `[F]`; Reuters `[E]` |
| Asian AI-hardware flows (mood) | Foreign net selling of Kospi > USD 20bn in a quarter with DRAM prices falling / net buying returns | ~KRW 20tn (~USD 15bn) net sold to mid-October; net buying on 21 Oct; DRAM prices still rising | Korea Herald, Herald Business `[E]` |
| TSMC ADR premium (mood) | < 5% / > 20% | 10.6% (23 Oct; 2-year mean 19.5%) | Yahoo |
| SKHY ADR premium (mood) | < 15% (ADR creation opened, new ADR issue) / > 50% | 43.6% on 27 Oct (28–55% since 18 Aug) | Yahoo via `docs/skhynix-analysis.md` |

**Closest to Bear:** capital as the stated constraint (Broadcom, NVIDIA) and capex above OCF (the five ~116%); vendor financing ≥ USD 270bn; one platform selling equity (Alphabet) with two prepared (Meta's Class C, Oracle's 20bn); Microsoft's backlog flat; FCF after returns −48.8bn in one quarter; in memory, the deceleration of contract prices and NAND wafer spot. **Bull side:** cloud growth (Azure, Google Cloud, AWS with its 2027–28 projection), TSMC's monthly revenue, rising GPU rental prices.

**Next dates:** Samsung and SK hynix Q3 business reports (~14 and ~16 Nov); NVIDIA Q3 FY27 (17 Nov; recalibration trigger and re-mark point); Anthropic pricing (~18 Nov) and first trade (~19 Nov); House briefing on NVIDIA (18 Nov) and Trump–Xi (18–19 Nov); TSMC November revenue and the ERCOT/PUCT audit (10 Dec); FY27 stopgap expiry (11 Dec; context); Oracle Q2 FY27 (~mid-December); Micron FQ1-27 (16 Dec); new Congress (3 Jan); Samsung Q4 preliminary (~7 Jan); governors (11 and 19 Jan) and the Texas Legislature (12 Jan); TSMC Q4 (mid-Jan); SK hynix and Samsung Q4 and 2027 capex (late Jan); hyperscaler 2027 capex (late Jan–early Feb); CoreWeave Q4 (~late February; prepayments received).

## Open checkpoints (numbers kept for references)

1. **Memory:** LTA ranges, floors and deposits in the Q3 business reports; the November and December contract prints and TrendForce's Q1-27 outlook; NVIDIA's supply commitments (17 Nov); Micron FQ1-27 (16 Dec); 2027 memory capex (late January). A disclosed floor, a q/q price decline or a capex figure is the independent evidence that can move an H2 point.
2. **E-layer points to watch:** Base 2028 (blend gap −0.037) and Bear 2027 (−0.046; −0.063 with Meta on the analysed Bear).
3. **E2 per-cloud split:** a row-definition change, so a method change for the next full re-baseline; the memo table under Engines carries the per-cloud view.
4. **Mid-cycle anchor (method):** under the layer method a rise in peak-year (CY27) consensus lifts 2028–30 one for one. Whether the 2030 mid-cycle should be anchored to a fixed basis is for the re-baseline; the effect measured on 1 Nov was ~2 pp of the memory Base, or ~5% of price.
5. **Alphabet Q3 10-Q:** Cloud backlog `[F]` (561bn via the call `[E]`), the Anthropic share, the equity-securities split.
6. **Basket method:** retained cash tied to EPS makes the 2027 EPS point nearly irrelevant for layers with c < 0 (E); whether to tie it to capex is for the re-baseline.
7. **Not read `[?]`:** Oracle's investor day (28 Oct); ServiceNow's outlook; why Amazon's 2026 guide implies only ~48bn of capex in Q4.
8. **Dates:** under Signposts and monitoring ("Next dates").
9. **Missing analyses:** Meta (the E-rest Bear; capex above OCF; Class C), now the most useful one; the T Bear inconsistency (no company analysis); Broadcom (largest H1 name after NVIDIA; FY Oct calendarisation bias; vendor financing).
11. **K1 capex cycle data gaps** (review section 10): AI revenue by company on one definition `[?]` (the gauge's supply is about twice the disclosed run-rates; Q4 calls); Meta's and Oracle's 2027 capex `[?]`; the economic life of accelerators `[E]` (four years moves the 2029 return from ~0% to −4%) and the cash cost ratio beyond AWS and CoreWeave; K1 2025 and 2026 on filings (~450 and ~815): re-set both at the January roll-forward.

## For IAF and downstream skills

- **iaf-valuation (2026-11-10.1):** no method change requested. Company analyses use the layer paths (Years 2–3), the Track guidance in the skill (H2 Track B; H1 and H4 Track B while the build-out lasts; E and T Track A unless capex dominates FCF), the calendarised consensus basis (NVIDIA: its own 11.4% calendarised sensitivity is the layer basis) and their own exit cross-check. The exit P/E here is a reference, never the IAF ceiling.
- **K1 for the platform analyses:** Microsoft, Alphabet and Amazon set their capex as a share of K1 (MSFT 225 / 230, GOOGL 300 / 305, AMZN 310 / 320 in 2028–29). Each decides at its next run whether its capex follows K1 to 1,170 / 1,170 or its share rises, and states why; the AI BBB only sets K1.
- **Memory analyses lead with the cycle (user rule, 1 Nov):** see H2 Memory cycle, section 7.
- **Fund analyses and equity-market-bbb:** no fund value is set here; they may read this baseline, including the Memory cycle section.
- **Rows moved in the last change (11 Nov K1 re-run), for the cascade:** K1 Base 2028–29 (1,170 / 1,170; −80 / −130bn, −6.4% / −10.0%); H1 Base revenue 2028–29 (750 / 745) and EPS 2028–30 (.91 / .88 / .87); H4 Base index 2028–29 (129 / 130) and EPS 2028–30 (.94 / .94 / .99); the E Base cash conversion (−.20 / .11 / .36); the monetisation ratio (0.24 / 0.31); the H1, H4, E and all-six basket rows. Unchanged: H2, H3, E1, E2, T1–T4, every Bear and Bull path, exit P/Es, payouts, scenarios and catalysts. Effects `[A]` = the layer-method change added to each analysis's own Base:

| Document | Rows it reads (register) | What moved for it | Effect on its Base `[A]` | Material (trigger rule)? |
|---|---|---|---|---|
| `docs/nvda-analysis.md` | H1 compute layer | H1 Base revenue 2028–29 750 / 745 and EPS 2028–30 .91 / .88 / .87 (beyond the 5% and 0.05 rules); Bear and Bull unchanged | ≈ −3.9 pp: ≈ 17.0% (v1.3 20.9%), P_k ≈ $192 against $168.89 (margin ≈ +13.4%): still clears | **Yes**; its own run is the Q3 report (17 Nov) |
| `docs/tsm-analysis.md` | H3 foundry layer | Nothing it reads: H3 kept (knock-on below the rule) | 0 by the rule (the review's pass-through sizing, 8.2–8.6%, is not applied) | No |
| `docs/mu-analysis.md` | H2 memory layer | Nothing it reads: H2 kept | 0 | No |
| `docs/msft-analysis.md` | E2, T1, T3, K1 capex | K1 2028–29 −6.4% / −10.0%; its capex is a share of K1 | ≈ +0.2 pp (cash) to +0.8 pp (with lower D&A); P_k ≈ $499–507 against $530.61, margin −6.1% to −4.4%: the upper bound enters the ±5% band | **Yes, urgent (`msft!`)** |
| `docs/googl-analysis.md` | E2, K1 capex, E-layer EPS | K1 as above; E-layer EPS unchanged; E cash conversion −.20 / .11 / .36 (its consistency check) | ≈ +0.3 to +1.2 pp; P_k ≈ $265–271 against $284.78, margin −7.0% to −4.7%: the upper bound enters the ±5% band | **Yes, urgent (`googl!`)** |
| `docs/amzn-analysis.md` | E2, K1 capex, E-layer EPS and exit P/E | K1 as above; E-layer EPS and exit P/E unchanged | ≈ +0.4 to +1.5 pp; P_k ≈ $225–233 against $270.87, margin −16.9% to −14.1%: still fails | **Yes** |
| `docs/skhynix-analysis.md`, `docs/samsung-analysis.md`, `docs/kospi-analysis.md` | H2 paths, exit P/E, scenarios, catalysts, memory basket row | Nothing they read: H2, the memory basket row (21.6%) and the multipliers are unchanged | 0 | No |
| `docs/dnb-teknologi-analysis.md` | Layer EPS paths, exit P/Es | The H1 path (its Broadcom block) beyond the 0.05 rule; the E cash conversion (its Meta block) | ≈ −0.15 pp from Broadcom, +0.02 pp from Meta; margin −8.9%: no flip | **Yes** (a path beyond the trigger) |
| `docs/global-index-funds-analysis.md` | Layer paths | H1 (Broadcom, AMD, Marvell) and H4 (Arista, Vertiv, Eaton) Base paths beyond the rule; the E cash conversion (Amazon, Meta, Oracle) | Small: < 0.2 pp | **Yes** (a path beyond the trigger) |
| `equity-market-bbb` (loop) | AI layer paths in World | The H1 Base path beyond the rule; H4 and the E cash conversion | ≈ −1% of World EPS in 2028–30, ≈ −0.3 pp on World's Base | **Yes**, at its own next update |

## Change log

- **12 Nov 2026 — compacted to the lean-document rules (CLAUDE.md, 12 Nov):** dated notes, superseded values, older prints, mood tables and the return attribution removed; no value, path, method or verdict changed. Earlier versions are in git.
- **11 Nov 2026 (evening) — K1 Base 2028–29 re-set (skill 2026-11-11.2, Option D):** K1 1,250 / 1,300 → 1,170 / 1,170; carried into H1 (750 / 745; EPS .91 / .88 / .87), H4 (129 / 130; EPS .94 / .94 / .99), the E Base cash conversion (−.20 / .11 / .36) and the monetisation ratio (0.24 / 0.31). New section K1 capex cycle and `references/k1ret.py`. Base NOK at the same prices: all six 10.0% → 9.2%, compute 11.2% → 7.5%, platforms 8.2% → 8.6%, networking 0.9% → −2.7%.
- **11 Nov 2026 — note, kept unchanged:** CoreWeave Q3, TSMC October revenue, the Anthropic S-1/A No. 2 and NVIDIA v1.3 read against the signposts (none crossed); checkpoint 10 closed with Option A+ of `docs/review-ai-h1-non-k1-funding.md` (skill 2026-11-11.1: H1's non-K1 buyers stated, the neocloud signpost widened to "Non-K1 compute funding"). No value moved.

## Appendix: market prints and sources

**Market prints, Update 7** (Yahoo, close Fri 6 Nov 2026; consensus 7 Nov, calendarised) `[F]`:

| Layer | Name | Price | Mcap USD bn | P/E CY27 | CY27 EPS (calendarised) | vs 30 Oct | 6 Nov day |
|---|---|---|---|---|---|---|---|
| H1 | NVDA | 186.64 | 4,507 | 12.3 | 15.21 | −8.8% | +2.8% |
| H1 | AMD | 449.04 | 736 | 26.8 | 16.78 | −11.0% | +11.0% |
| H1 | AVGO | 293.69 | 1,402 | 15.1 | 19.47 | −9.9% | +0.7% |
| H1 | MRVL | 141.20 | 127 | 19.9 | 7.08 | −28.1% | +5.7% |
| H2 | MU | 690.00 | 781 | 3.6 | 191.80 | −22.0% | +5.1% |
| H2 | SK hynix | KRW 1,132,000 | 585 | 2.1 | KRW 529,348 | −20.2% | −10.4% |
| H2 | Samsung | KRW 188,700 | 901 | 2.4 | KRW 77,324 | −16.1% | −6.4% |
| H3 | TSM | 375.44 | 1,947 | 16.1 | 23.39 | −7.6% | +6.3% |
| H3 | ASML | 1,424.75 | 549 | 22.7 | 62.89 (EUR 56.43) | −9.0% | +5.0% |
| H3 | AMAT | 332.71 | 264 | 17.9 | 18.56 | −14.7% | +4.2% |
| H3 | LRCX | 200.44 | 251 | 18.3 | 10.94 | −16.2% | +8.2% |
| H4 | ANET | 170.80 | 216 | 30.3 | 5.64 | +1.1% | +7.3% |
| H4 | VRT | 182.86 | 70 | 18.6 | 9.84 | −21.4% | +3.5% |
| H4 | ETN | 341.72 | 133 | 21.0 | 16.29 | −7.6% | +4.5% |
| E | MSFT | 530.61 | 3,940 | 24.0 | 22.09 | +1.7% | −1.0% |
| E | GOOGL | 284.78 | 3,501 | 19.0 | 14.95 | +1.8% | +0.8% |
| E | AMZN | 259.30 | 2,804 | 24.3 | 10.67 | +7.9% | −0.3% |
| E | META | 610.15 | 1,560 | 18.0 | 33.93 | −0.8% | +0.8% |
| E | ORCL | 116.10 | 362 | 11.8 | 9.84 | −11.2% | +0.8% |
| T | NOW | 101.97 | 106 | 21.2 | 4.80 | −3.0% | −0.4% |
| T | CRM | 213.65 | 176 | 13.3 | 16.08 | −6.8% | −3.9% |
| T | ADBE | 239.30 | 93 | 8.7 | 27.43 | −4.4% | −2.9% |
| T | PLTR | 160.38 | 386 | 64.4 | 2.49 | −12.9% | +3.5% |
| T | SAP | EUR 210.75 | 271 | 24.9 | EUR 8.48 | −0.2% | −2.3% |
| T | INTU | 341.50 | 91 | 13.6 | 25.12 | +0.1% | −3.8% |
| T | SNOW | 275.88 | 97 | 93.2 | 2.96 | −9.9% | +2.4% |
| T | DDOG | 179.04 | 65 | 58.3 | 3.07 | −23.9% | +2.5% |
| memo | CRWV | 46.40 | 26 | n/m | (loss) | −15.4% | +6.3% |

- **Script inputs** (`references/model.py` carries them, switch `K1D` on by default; `members.py` and `impl.py` read them; `k1ret.py` needs no market data): KRW/USD 1,363.65 and EUR/USD 1.11433 (Yahoo final quotes, 6 Nov); USD/NOK closed ~9.30 on 6 Nov (the 7 Nov weekend quote of 9.45 is not used); `FX` = Equity BBB 6 Nov path (`FX0` 9.29); `NIB` 4.38; `T0` 54/365. `cal` (7 Nov): AMD 16.77999; MRVL 4.2224/12 + 7.34277 × 11/12; SK hynix 529,348.1; Samsung 77,323.65; ASML EUR 56.43418; AMAT 18.55645; ANET 5.64382; VRT 9.84233; ETN 16.29264; MSFT (20.00388 + 24.17933)/2; GOOGL 14.95356; AMZN 10.6718; ORCL 8.14185 × 5/12 + 11.05442 × 7/12; NOW 4.8023; ADBE 27.429; PLTR 2.48939; DDOG 3.07031; the rest unchanged.
- Analysts (7 Nov): SK hynix CY27 38, Samsung 33, NVDA 52, MU 36, AMD 49, ANET 28, GOOGL 51, AMZN 56. Samsung CY26 47,639 and CY27 revenue KRW 1,017tn; SK hynix CY26 359,089 and CY27 revenue KRW 578tn.
- Indices, 5 → 6 Nov: Nasdaq-100 26,630 → 26,990 (+1.4%); SOX 9,011 → 9,390 (+4.2%); S&P 500 7,354 → 7,377 (+0.3%); Kospi 5,384 → 5,060 (−6.0%); IQQK (Xetra) 89.50 → 89.42 (−0.1%); Vistra 112.89 → 124.80 (+10.6%) `[F]`. Since 6 Nov the move is company-specific (NVIDIA $168.89 on 10 Nov, −9.5%; TSM +5.6%, AMZN +4.5%), not a sector sell-off.
- **Past-cycle closes** (Yahoo daily, `cyclehist.py`) `[F]`: peaks Samsung 57,220 (1 Nov 2017), 91,000 (11 Jan 2021), 362,500 (18 Jun 2026); SK hynix 95,300 (23 May 2018), 148,500 (25 Feb 2021), 2,919,000 (22 Jun 2026); Micron $62.62 (29 May 2018), $97.36 (14 Jan 2022), $1,213.56 (25 Jun 2026). Troughs Samsung 37,450 (4 Jan 2019), 52,600 (29 Sep 2022); SK hynix 57,700 (3 Jan 2019), 75,000 (29 Dec 2022); Micron $29.02 (24 Dec 2018), $48.88 (26 Sep 2022). Micron operating income (Alpha Vantage) peaked at $4.38bn (FQ4-18) and $3.00bn (FQ3-22), troughed at $0.52bn (FQ1-20) and −$2.30bn (FQ2-23).

**Sources** (one line each; as-of date):
- Yahoo quote, chart and `earningsTrend` APIs (`quotes.py`, `hist.py`, `trend2.py`, `cyclehist.py`): prices, FX, indices, consensus, past-cycle closes `[F]` — 6–7 Nov 2026 (past cycles 1 Nov).
- Alpha Vantage `INCOME_STATEMENT` (MU): Micron quarters 2017–2023 `[F]` — 1 Nov 2026.
- `docs/review-ai-k1-sustainability.md` (Option D) and its S1–S20: filings of the five via Alpha Vantage, AWS segment, CoreWeave, FRED `C275RC1A027NBEA` and `C319RC1A027NBEA`, Silicon Data, Richmond Fed Economic Quarterly 89/4 (2003), IEEFA — 11 Nov 2026.
- `docs/review-ai-h1-non-k1-funding.md` (Option A+): H1 bought outside K1 and its funding — 11 Nov 2026.
- CoreWeave Q3 8-K Ex. 99.1 (EDGAR) and call: revenue, backlog, guide, financing `[F]`/`[E]` — 10 Nov 2026.
- TSMC 6-K, October revenue and November board appropriations `[F]` — 10 Nov 2026.
- Anthropic S-1/A No. 2 (EDGAR; Q3 revenue and placement via `docs/googl-analysis.md` and `docs/amzn-analysis.md`) `[F]` — 10–11 Nov 2026.
- Anthropic public S-1 (H1-26 revenue 16.3bn, Google and Amazon commitments) `[F]` — 26 Oct 2026; draft S-1 via [Yahoo](https://finance.yahoo.com/technology/ai/articles/anthropic-1-518-billion-commitment-165731037.html) and [xenospectrum](https://xenospectrum.com/en/anthropic-ipo-loss-compute-commitments/) (2025 revenue, Q1 2026) `[E]` — 28 Sep 2026.
- `docs/nvda-analysis.md` (v1: Q2 FY27 release, 10-Q, 8-Ks of 17 Aug and 3 Sep; v1.3: board review, export reports) — 17 Oct and 11 Nov 2026.
- [NVIDIA Q2 FY27 release](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027) `[F]` — 26 Aug 2026; [NVIDIA 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm) (SB Energy guaranties) `[F]` — 17 Aug 2026.
- `docs/tsm-analysis.md` (v1: 3Q26 management report, call, 6-Ks; v1.2) — 17 Oct and 11 Nov 2026; [TSMC Q3 2026 release](https://pr.tsmc.com/english/news/3346) `[F]` — 15 Oct 2026.
- [ASML Q3 2026 6-K](https://www.sec.gov/Archives/edgar/data/0000937966/000162828026065813/pressreleasefinancialresul.htm) `[F]` — 14 Oct 2026.
- `docs/mu-analysis.md` (v1 FQ4-26 release and 10-K; v2 technology webinar; v3) — 16 Oct, 22 Oct and 5 Nov 2026.
- `docs/msft-analysis.md` v3 (Q1 FY27 8-K and 10-Q; call transcripts), 7 Nov re-mark — 28 Oct and 7 Nov 2026; Microsoft Q4 FY26 ([Fierce](https://www.fierce-network.com/cloud/microsoft-azure-crosses-100b-mark-growth-hits-four-year-high), [Quartz](https://qz.com/microsoft-earnings-azure-100-billion-cloud-073026)) `[E]` — 29 Jul 2026.
- `docs/googl-analysis.md` v2 and call addendum (Q3 8-K, Anthropic S-1, transcripts), 7 Nov re-mark — 28–29 Oct and 7 Nov 2026; [Investing.com](https://www.investing.com/news/stock-market-news/alphabet-shares-tumble-65-as-earnings-miss-overshadows-cloud-boom-4980569) independent capex check `[E]` — 29 Oct 2026.
- `docs/amzn-analysis.md` v2 (Q3 release, 10-Q, call via Motley Fool), 11 Nov re-mark — 30 Oct and 11 Nov 2026.
- `docs/skhynix-analysis.md` v2 (Q3 release and call) — 28 Oct 2026; `docs/samsung-analysis.md` v2 (Q3 release, IR deck, call) — 29 Oct 2026.
- [Meta Q3 2026 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001326801/000162828026066700/meta-09302026xexhibit991.htm) `[F]`; [Fortune](https://fortune.com/2026/10/21/meta-q3-earnings-mark-zuckerberg-capex-muse/), [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-meta-beats-q3-2026-estimates-as-ai-push-lifts-shares-93CH-4964260) `[E]` — 21 Oct 2026.
- [Oracle Q1 FY27 (erp.today)](https://erp.today/oracle-q1-fy27-results-664b-backlog-ai-contracts/): RPO, OCI, capex, stock sale `[E]` — 10 Sep 2026.
- [Broadcom Q3 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm), [unite.ai](https://www.unite.ai/broadcom-posts-record-q3-revenue-as-ai-chip-sales-reach-16-7b/): AI semis 16.7, Q4 guide 21.7 `[E]` — 2–3 Sep 2026.
- [AMD Q2 2026 (aiweekly)](https://aiweekly.co/alerts/amd-q2-revenue-jumps-50-as-data-center-more-than-doubles) `[E]` — Aug 2026; [AMD Q3 2026 release (finviz)](https://finviz.com/news/414840/amd-reports-third-quarter-2026-financial-results), [Constellation Research](https://www.constellationr.com/insights/news/amd-q3-shines-data-center-revenue-nearly-doubles), [Crypto Briefing](https://cryptobriefing.com/amd-q3-2026-earnings-record-revenue/) `[E]` — 3 Nov 2026.
- [Arista Q3 2026 release (finviz)](https://finviz.com/news/414796/arista-networks-inc-reports-third-quarter-2026-financial-results), [24/7 Wall St.](https://247wallst.com/cards/arista-networks-q3-2026-earnings-anet-01m6hm6v5atgmt0qczy1xw4ymp) `[E]` — 3 Nov 2026.
- Zacks news: [Vertiv Q3](https://www.zacks.com/stock/news/3016720/vertiv-holdings-co.-(vrt)-q3-earnings-and-revenues-surpass-estimates), [ServiceNow Q3](https://www.zacks.com/stock/news/3017784/servicenow-(now)-reports-q3-earnings:-what-key-metrics-have-to-say), [Oracle](https://www.zacks.com/stock/news/3016284/3-reasons-to-buy-oracle-stock-now-despite-a-24-drop-in-6-months), [Oracle Autonomous Database](https://www.zacks.com/stock/news/3017612/is-oracle-stock-worth-buying-as-autonomous-database-use-keeps-growing?) (Maia 300, TPU 8i) `[E]` — 27–28 Oct 2026.
- [24/7 Wall St.: Lam Q1 FY27](https://247wallst.com/investing/2026/10/22/lam-research-just-posted-its-first-ever-40-operating-margin-but-sold-off/), [Invezz](https://invezz.com/news/2026/10/22/lam-research-stock-falls-9-despite-record-results-this-analyst-sees-stock-doubling/), [AOL](https://www.aol.com/articles/lam-research-sinks-9-supply-144450000.html) `[E]` — 21–22 Oct 2026.
- [FactSet: hyperscalers tap external financing](https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow) `[E]` — 23 Jul 2026.
- Goldman 2027 capex ([Yahoo](https://finance.yahoo.com/sectors/technology/articles/goldman-says-consensus-2027-hyperscaler-140152065.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-25/goldman-sees-hyperscaler-ai-capex-rising-50-to-1-2-trillion)), [Moody's (DCD)](https://www.datacenterdynamics.com/en/news/moodys-hyperscaler-capex-forecasts-marked-up-by-85bn-to-close-in-on-1trn-by-2027/) `[E]` — Sep 2026.
- [Broadcom CEO on capital (Yahoo)](https://finance.yahoo.com/technology/ai/articles/broadcom-ceo-sees-capital-main-103425026.html), [Anthropic loan (Yahoo/TIKR)](https://finance.yahoo.com/technology/ai/articles/broadcom-ceo-flags-capital-ai-074152257.html) `[E]` — 12–14 Oct 2026.
- [CNBC: Huang on neocloud capital](https://www.cnbc.com/2026/10/22/nvidia-jensen-huang-neocloud-demand-capital.html), [Bloomberg video](https://www.bloomberg.com/news/videos/2026-10-22/nvidia-s-huang-says-neoclouds-are-good-investment-video), [Yahoo: "financeable asset"](https://finance.yahoo.com/technology/ai/articles/nvidia-jensen-huang-wants-ai-105720331.html) `[E]` — 22 Oct 2026.
- [CNBC: Anthropic 65bn run-rate](https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html) `[E]` — 17 Aug 2026; [Reuters via Investing.com: OpenAI ~50bn](https://www.investing.com/news/stock-market-news/openais-annualized-revenue-20-billion-less-than-previously-signaled-ft-reports-4939854), [CNBC](https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html) `[E]` — 8 Oct 2026.
- OpenAI commitments ([the-decoder](https://the-decoder.com/openais-stargate-pivot-highlights-rift-with-microsoft-over-future-ai-computing-needs/), [heise](https://heise.de/-10640527)) `[E]` — 2026.
- [Epoch AI price decline (secondary)](https://pasqualepillitteri.it/en/news/21044/epoch-ai-ai-prices-fall-47-percent-quarter) `[E]` — 22 Sep 2026.
- [Census BTOS AI use](https://census.gov/library/stories/2026/05/ai-use-businesses.html), [WeWork analysis](https://www.wework.com/ideas/research-insights/the-new-ai-divide) `[F]`/`[E]` — May / Jul 2026.
- [Copilot 30m seats (UC Today)](https://www.uctoday.com/unified-communications/microsoft-365-copilot-passes-30-million-paid-seats-as-cloud-and-ai-growth-power-record-quarter) `[E]` — Jul 2026.
- [SaaS rout (SaaStr)](https://www.saastr.com/the-saas-rout-of-2026-is-even-worse-than-you-think-for-the-first-time-ever-software-now-trades-at-a-discount-to-the-sp-500) `[E]` — 2026.
- [Gartner AI spending](https://gartner.com/en/newsroom/press-releases/2026-09-16-gartner-forecasts-worldwide-ai-spending-to-grow-49-point-5-percent-in-2026) (search excerpt) `[E]` — 16 Sep 2026.
- Power: [S&P Global](https://www.spglobal.com/energy/en/news-research/latest-news/natural-gas/082626-gas-turbine-copper-supply-seen-as-near-term-data-center-constraints-in-pjm), [Turbomachinery](https://www.turbomachinerymag.com/view/ai-data-centers-gas-turbines-and-a-turbomachinery-legend) `[E]` — Aug–Oct 2026.
- [TrendForce: memory spot, 4 Nov](https://www.trendforce.com/news/?p=66203) `[E]` — 4 Nov 2026.
- [TrendForce: 4Q26 memory contract prices](https://www.trendforce.com/presscenter/news/20260930-13258.html) `[E]` — 30 Sep 2026.
- [TrendForce News: DRAM ~+20% in 4Q26](https://www.trendforce.com/news/2026/10/20/news-dram-prices-seen-rising-20-qoq-in-4q26-despite-slower-gains-ai-demand-tight-supply-support-outlook/) (LTA ceilings, CXMT 4F², 8-Hi vs 12-Hi) `[E]` — 20 Oct 2026.
- [TrendForce via I-Connect007: 2027 DRAM and NAND diverge](https://iconnect007.com/article/150995/2027-memory-market-sees-diverging-dram-nand-trends/150992/pcb) `[E]` — 30 Jul 2026.
- [KuCoin/TechFlow: Goldman on TrendForce 3Q26](https://www.kucoin.com/news/flash/goldman-sachs-trendforce-raises-pc-dram-price-outlook-to-18-23) `[E]` — 2 Sep 2026.
- [Tech-Insider: DRAM record, NAND flat](https://tech-insider.org/dram-record-high-nand-flat-21-months-october-2026/) `[E]` — 30 Oct 2026.
- [siliconanalysts: 2027 HBM ASP +121%](https://siliconanalysts.com/market/trendforce-2027-hbm-blended-asp-to-jump-121-as-hbm4-hbm4e-mix-shifts-2026-10-06) `[E]` — 6 Oct 2026.
- [Letsdatascience: inventories below ten days](https://letsdatascience.com/news/samsung-and-sk-hynix-inventories-fall-below-ten-days-f60f6a2f), [Wccftech: LTAs and peak prices](https://wccftech.com/peak-dram-prices-in-sight-as-samsung-sk-hynix-double-down-on-long-term-contracts/) `[E]` — Apr–Sep 2026.
- [Memory 2027 sold out (ainvest)](https://www.ainvest.com/news/2027-memory-sold-prices-spike-slow-2608/), [hostzealot](https://www.hostzealot.com/blog/news/samsung-sk-hynix-and-micron-max-out-dram-and-hbm-orders-up-to-2027) `[E]` — Aug–Sep 2026.
- [Cryptobriefing: memory share of hyperscaler capex](https://cryptobriefing.com/memory-share-hyperscaler-capex-2027/) `[E]` — 23 Jun 2026.
- [iTiger: TrendForce memory market 2027](https://www.itiger.com/news/1173429702) `[E]` — 2026.
- [CXMT IPO (Wccftech)](https://wccftech.com/cxmt-debuts-8-6-billion-ipo-as-dram-surge-chips-away-at-samsungs-dominance-by-2028/amp/), [Counterpoint](https://counterpointresearch.com/en/insights/cxmt-stock-market-big-three-memory-club) `[E]` — Jul 2026; CXMT 4F² claim ([Seoul Economic Daily](https://en.sedaily.com/finance/2026/10/14/chinas-cxmt-touts-next-generation-dram-with-no-specs-or), [technology.org](https://www.technology.org/2026/10/14/cxmt-4f2-dram-samsung-sk-hynix-shares-kospi/)) `[E]` — 13–14 Oct 2026.
- [IDC: memory crisis and devices](https://www.idc.com/resource-center/blog/higher-asps-lower-unit-volumes-how-the-memory-crisis-is-reshaping-the-pc-and-smartphone-outlook), [Counterpoint memory tracker](https://counterpointresearch.com/cn/reports/memory-price-tracker-and-forecast-oct-2026) `[E]` — Feb–Oct 2026.
- [BigGo Finance: memory stocks below 2026 highs](https://finance.biggo.com/news/873d9ecf-d02b-4f2f-99ea-a8169e870b8e) `[E]` — 30 Oct 2026.
- [Herald Business: Kospi](https://mbiz.heraldcorp.com/article/10910347), [Korea Herald](https://www.koreaherald.com/article/10892894) (foreign flows) `[E]` — Oct 2026.
- Past-cycle turning points: [TrendForce 4Q21](https://www.trendforce.com/presscenter/news/20210922-10947.html), [Investing.com: SK hynix Q3 2018](https://investing.com/news/stock-market-news/south-koreas-sk-hynix-posts-record-thirdquarter-profit-as-chip-outlook-dims-1658698), [Computing: Gartner 2019 DRAM −37.5%](https://www.computing.co.uk/news/3085045/dram-semiconductors-intel) `[E]` — 2018–2021.
- Midterms and siting: [CNBC: Texas governor](https://www.cnbc.com/2026/11/04/ai-stocks-texas-governor-data-centers.html), [CNBC: hyperscalers](https://www.cnbc.com/2026/11/04/apple-and-other-big-tech-stocks-surge-after-2026-midterm-elections.html), [CNBC: ballot measures](https://cnbc.com/2026/11/04/data-center-ballot-measures-2026-midterm.html) `[E]` — 4 Nov 2026.
- Midterms and siting: [Fortune](https://fortune.com/2026/11/05/midterm-elections-data-center-construction-big-tech-hinojosa-acton-lance-bottoms/), [IAPP](https://iapp.org/news/a/democratic-midterm-wins-set-stage-for-tougher-tech-and-ai-scrutiny), [Newsweek](https://www.newsweek.com/ai-politics/data-centers-were-the-big-loser-of-the-midterms-12665187), [The Standard](https://www.thestandard.com.hk/finance/article/347689/AI-stocks-slide-on-Wall-Street-after-midterm-data-center-backlash) `[E]` — 4–5 Nov 2026.
- Texas pause: [Energy News Beat](https://energynewsbeat.co/finance/chip-stocks-sink-and-texas-power-stocks-slide-did-voters-really-hit-pause-on-data-centers/), [KERA](https://www.keranews.org/texas-news/2026-08-27/gov-abbott-has-ordered-a-pause-on-data-center-approvals-will-it-make-a-difference), [Gibson Dunn](https://www.gibsondunn.com/what-governor-abbotts-data-center-audit-directive-means-for-ercot-and-the-batch-zero-study-process/) `[E]` — Aug–Nov 2026.
- Federal: [Al Jazeera: ratepayer bill](https://www.aljazeera.com/news/2026/9/30/us-senate-rejects-bill-targeting-ai-data-centre-electricity-costs), [Sanders: moratorium act](https://www.sanders.senate.gov/press-releases/news-sanders-ocasio-cortez-announce-ai-data-center-moratorium-act/), [Bloomberg: H200 licence](https://www.bloomberg.com/news/articles/2026-03-16/nvidia-s-h200-license-stirs-security-concern-among-top-democrats), [AP via WFTV: concessions](https://www.wftv.com/news/business/facing-pushback-data/42ALTF7EMA3YLCT7VDC35I53QY/) `[E]` — Mar–Oct 2026.
