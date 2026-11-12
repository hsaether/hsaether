# Review: H1 compute bought outside K1, and how it is funded — 11 Nov 2026

**Reviewed:** `docs/ai-market-bbb.md` (1 Nov baseline, Update 7 of 7 Nov, note of 11 Nov), open
checkpoint 10 ("H1 demand outside K1").

**Skill revisions:**
- `ai-market-bbb` **2026-11-06.1** (method; not changed here);
- `iaf-valuation` **2026-11-10.1**, through the company analyses read: `docs/nvda-analysis.md` v1.3,
  `docs/tsm-analysis.md` v1.2, `docs/mu-analysis.md` v3.

**Status:** a proposal for the user's decision. Nothing in the baseline, the skills or the register
is changed.

**Tags:** `[F]` reported fact (filing or release) · `[E]` external, call transcript or secondary ·
`[A]` my own assumption or calculation, with its reasoning · `[?]` not found.

**Paths used** (`docs/ai-market-bbb.md`, Interface — hardware): H1 2026 **~470** (440–490); Base
**730 / 800 / 825** in 2027–29; Bear 585 / 470 / 490; Bull 820 / 985 / 1,080. K1 Base 790 /
1,120 / 1,250 / 1,300. The question's "2027 Base 800" is the 2028 point; 2027 is 730.

**Calculations** (scratchpad, `py -I`):
- `nonk1.py` copies the `model.py` v2.1 build for H1. At the Update 7 inputs it reproduces the
  baseline: P/E 13.71, Base 11.2%, hurdle P/E 13.40, margin of safety −2.2%.
- `nonk1_h23.py` passes the shock to TSMC (H3) and Micron (H2).
- `implied.py` derives the non-K1 path that each scenario implies.

## 1. Question

The H1 path is set from K1, the capex of Microsoft, Alphabet, Amazon, Meta and Oracle. Part of H1
is bought by others:
- neoclouds;
- xAI;
- the labs' own and leased builds;
- sovereign and enterprise buyers.

Some of them depend on external money, vendor financing and NVIDIA's support. Should the AI BBB
make the Base assumption ("these buyers stay funded") explicit, or tie H1 to the financing (K3) and
backlog (K4) rows?

## 2. Short answer

- **Size.** Buyers outside K1 take **30–46% of H1 in 2026: ~140–215bn of ~470, central ~185
  (39%)** `[A]`. This rests on three estimates that overlap (4.1). NVIDIA's "AI Clouds, Industrial
  and Enterprise" (ACIE) segment was 45% of its Q2 FY27 data center `[F]`.
- **What Base assumes.** Base keeps that share about constant. That means non-K1 H1 grows **~+60%
  in 2027 (+43% to +76%) and is then flat** `[A]`.
- **Funding for 2027 is mostly raised already:**
  - Anthropic: ~$132bn of cash and short-term investments `[F]` plus its IPO;
  - SpaceX: ~$90bn of liquidity after its IPO `[F]`;
  - OpenAI: its $122bn round lasts into 2028 `[E]`.

  What must still be raised is the neoclouds' contract-backed debt. NVIDIA's direct support funds
  about **5–8%** of non-K1 H1 `[A]`.
- **The method already carries the risk.** The Bear's financing break names neoclouds and labs.
  Measured against Base, it already holds non-K1 H1 **−25 to −30% in 2027 and −45 to −55% in
  2028–29** `[A]`.
- **Effect on decision figures:**
  - A **temporary** non-K1 shortfall of 20–40% in 2027–28 moves the H1 basket by **−0.2 to −0.8
    pp** and NVIDIA by **≤ 0.9 pp**. No verdict changes.
  - Only a **persistent** shortfall moves decisions, because the exit rests on 2030 earnings. It
    cuts the H1 basket by **2–8 pp** and takes NVIDIA to **12–18%**. NVIDIA still clears, at the
    edge in the worst case.
- **Recommendation: Option A+.** State the assumption in the H1 notes, and turn the existing
  "Neocloud funding" signpost into a "Non-K1 compute funding" signpost with three legs that
  quarterly filings measure. This adds no row and moves no path. H1 is not tied to K3 or K4: that
  would double count the Bear, and it rests on `[A]` splits with no sourced elasticity.

## 3. Findings with sources

### 3.1 NVIDIA's split, and why ACIE is not the same as "outside K1"

| NVIDIA data center, USD bn `[F]` | Q1 FY26 | Q2 FY26 | Q3 FY26 | Q4 FY26 | Q1 FY27 | **Q2 FY27** |
|---|---|---|---|---|---|---|
| Hyperscale | 22.26 | 24.17 | 35.14 | 42.21 | 43.05 | **48.71** |
| AI Clouds, Industrial and Enterprise (ACIE) | 16.85 | 16.93 | 16.08 | 20.10 | 32.20 | **40.31** |
| ACIE share of data center | 43.1% | 41.2% | 31.4% | 32.3% | 42.8% | **45.3%** |

Quarters are NVIDIA fiscal quarters; Q2 FY27 is May–July 2026. Source: NVIDIA's Q2 FY27 "Revenue by
Market Platform" slides (S2), with every quarter recast.

**Definitions:**
- **Hyperscale** is "the public cloud and the world's largest consumer Internet companies", i.e.
  "five or six, seven" companies `[E]` (Q1 FY27 call, S3).
- **ACIE** holds the AI-native clouds (the CEO confirmed that neoclouds sit here), industrial,
  enterprise and sovereign `[E]`.
- Q2 ACIE growth was "driven by end-demand from AI natives, enterprises, and sovereign customers,
  **as well as hyperscalers utilizing AI clouds**" `[F]` (10-Q, S1).

**ACIE ≠ non-K1, in two directions:**

| Offset | Evidence | Size `[A]` |
|---|---|---|
| **− K1 demand inside ACIE** | Hyperscalers rent AI-cloud capacity `[F]`: Microsoft ~$60bn of neocloud contracts; Meta with CoreWeave and Nebius `[E]` (secondary, S12). CoreWeave says > 75% of its committed capex is tied to investment-grade and enterprise customers `[E]` (Q3 call via `docs/nvda-analysis.md`). Some of this is already in K1: Microsoft's capex includes finance leases, and its Q1 FY27 capex fell short because "third-party capacity deliveries slipped" `[E]` (AI BBB K1 note) | 7–12 pp of NVIDIA data center |
| **+ non-K1 demand inside Hyperscale** | In Q2 FY27 NVIDIA moved one company from ACIE to Hyperscale "due to a change in their business model" `[F]`. That moved ~$5.2bn in Q1 FY27: the split first reported was ~37.9 / 37.4 `[E]`, the recast one 43.05 / 32.20 `[F]`. The name is not disclosed `[?]`. The fit is SpaceXAI: it began selling compute to Anthropic in May 2026 `[F]` (S-1/A), and its Q1 2026 capex was $7.7bn `[E]`. If so, Hyperscale holds ~$5–10bn a quarter of non-K1 demand | 0–9 pp |

**Net: non-K1 is ~31–47% of NVIDIA's data center revenue** `[A]`. One more pointer: NVIDIA says
OpenAI "contributed a meaningful amount of our revenue by purchasing cloud services from our
customers" `[F]`. OpenAI's demand thus mostly reaches H1 through K1 clouds (Microsoft, Oracle, AWS),
and so through K1.

### 3.2 The large buyers outside K1 (filed figures)

| Buyer | 2026 spend | Demand behind it | Source |
|---|---|---|---|
| **CoreWeave** | Capex guide **$37–39bn**; cash capex $23.6bn in 9M (Q3 $9.4bn) `[F]` | Backlog **$132.5bn** (30 Sep) `[F]`; > 75% of committed capex tied to investment-grade and enterprise customers `[E]`; 4.6 GW contracted, 1.7 GW active `[F]` | 8-K Ex. 99.1, 10 Nov (S4) |
| **Nebius** | Capex guide **$20–25bn** `[E]` | Microsoft and Meta contracts `[E]` | Call remark via Newsquawk (S11); Q3 report on **12 Nov** |
| **SpaceX "SI" segment (xAI)** | Capex **$40.0bn** in 9M, **$16.4bn** in Q3 `[F]` | SI revenue $7.56bn in Q3 `[F]`; nameplate compute 1.7 GW (0.6 GW a year earlier) `[F]`; Anthropic up to $120.5bn, ~$3.1bn a month from full delivery (December 2026) `[F]` | SpaceX 10-Q Q3 (S6); Anthropic S-1/A (S5) |
| **Anthropic, outside K1** | Leased TPU racks from Broadcom (online from 2026, more from 2027) `[F]`; orders of ~$10bn + $11bn for 2026 delivery `[E]` (Broadcom call, Dec 2025) | See the table below | S-1/A No. 2 (S5) |
| **OpenAI, outside K1** | CoreWeave; SB Energy's PORTS campus (4.25 GW, nine phases from FY29); Broadcom; AMD; Cerebras `[F]`/`[E]` | Most of its compute is bought from K1 clouds `[F]` (NVIDIA 10-Q) | NVIDIA 10-Q and 8-K (S1); press `[E]` |
| **Sovereign** | NVIDIA sovereign revenue **> $30bn in FY26**; +80% y/y in Q1 FY27 `[E]`; about double y/y in Q2 FY27 `[E]` (secondary, unverified) | State budgets and funds | NVIDIA calls (S3, S13) |
| **Enterprise and industrial on-prem** | Inside ACIE; no figure `[?]` | Corporate cash flow | — |

**Anthropic's compute commitments: more are placed outside K1 than inside** (S-1/A No. 2, 10 Nov,
contractual obligations section) `[F]`:

| Counterparty | USD bn | Firmness |
|---|---|---|
| Google (Apr 2026–Jul 2033) | ≥ 121.3, plus an estimated 125–150 of further TPU compute in 2028–31 (from Google or a third-party TPU provider; not in the table) | Non-cancelable |
| Amazon (May 2026–Apr 2036) | ≥ 110.0 | Non-cancelable |
| Microsoft (Nov 2026–Jun 2033) | 47.2–49.2 | Non-cancelable |
| **K1 subtotal** | **~279–281** | |
| Broadcom: TPU equipment, five-year finance leases | **161.2** of rent | Non-cancelable; secured on the equipment |
| SpaceXAI | up to **120.5** | Cancellable on 90 days' notice after January/March 2027 |
| Nscale | up to **44.6** | Nscale must first obtain "qualifying financing" |
| Lambda | **41.3** | 34.9 of it terminable: Lambda did not secure the facility lease |
| AMD Helios racks, first tranche in 2027 | > **20** | Conditions include pricing and financing terms |
| **Non-K1 subtotal** | **~388** (firm ~188) | |
| Obligations subject to termination rights or contingent conditions, such as "the counterparty's ability to secure financing" | **186.2** | — |

### 3.3 How the non-K1 spend is funded

| Buyer group | Funding in 2026 `[F]` unless tagged | Cost / form | 2027: committed or still to raise |
|---|---|---|---|
| **Neoclouds** (CoreWeave, Nebius, Lambda, Nscale, Crusoe, others) | CoreWeave 9M: operating cash flow $5.6bn (incl. prepayments), debt issued $27.0bn, repaid $7.6bn, private placements $3.0bn, against cash capex $23.6bn. ~$9bn of customer prepayments and deposits expected in the next three months | Asset-level secured debt against contracts (DDTL 5.5: $2.6bn); converts $4.2bn; ATM up to 35m shares. Cost of debt **7.9%**; "no unsecured debt at current yields through 2027" `[E]` | **To be raised:** 2027 capex is not guided `[?]`. Contract-backed debt, so it depends on the counterparties (K1 or labs) |
| **xAI (SpaceX SI)** | SpaceX: IPO proceeds $85.7bn (10-Q financing line; the press reported ~$75bn at $135 `[E]`); **$25bn senior unsecured notes at 5.35–6.65% (weighted 5.86%)**; operating cash flow $13.1bn (9M, group); cash $51.3bn + short-term securities $38.6bn on 30 Sep; debt $38.0bn | Equity and investment-grade-like unsecured debt | **In hand.** Its revenue from Anthropic can be cancelled on 90 days' notice from early 2027 `[F]` |
| **Anthropic** (own and leased builds) | Preferred equity $110.7bn and operating cash flow **+$6.6bn** in 9M. Cash $95.6bn + short-term investments $36.3bn on 30 Sep. IPO: 801.4m primary shares at $70–78 (~$56–62bn `[A]`) plus a **$26.0bn** Class N placement | Equity. Broadcom leases (lessor finance, partly assigned to financing vehicles) and a $42.0bn note facility with Broadcom | **In hand:** contractual payments of $70.7bn in the next 12 months, of which $4.2bn is contingent, against ~$214–220bn of liquidity after the deal `[A]` |
| **OpenAI** (outside K1) | Round of **$122bn** closed 31 Mar 2026 at $852bn (Amazon up to 50, NVIDIA 30, SoftBank 30) `[E]` | Equity; partners finance the sites `[E]` | Burn ~$25bn in 2026 and ~$57bn in 2027 `[E]`. The cash lasts into 2028 `[E]` (FT via Reuters). **2028 needs a new round or an IPO** |
| **Sovereign** | Budgets and state funds `[A]` | — | Budgeted, not market-funded `[A]` |
| **Enterprise** | Operating cash flow `[A]` | — | Cyclical with the equity Bear `[A]` |

### 3.4 NVIDIA's own support

| Item (NVIDIA 10-Q of 26 Jul 2026 unless tagged) | USD bn | Whose H1 demand it supports |
|---|---|---|
| Purchases of equity securities, H1 FY27 (Feb–Jul 2026) | 42.4 gross, 35.2 net `[F]` | Mostly labs: OpenAI ~30 `[E]`. Neoclouds: CoreWeave and Nebius ~2 each `[E]` |
| Net additions to private stakes, H1 FY27 | 31.0 `[F]` | Private labs and clouds |
| Equity commitments | 25 `[F]` | "AI model makers, infrastructure financiers" |
| AI cloud agreements (NVIDIA buys back unsold capacity; typically six years) | 36 `[F]` | AI clouds (ACIE) |
| Land, power and shell guarantees | 3.5 `[F]` | AI clouds |
| Third-party data-center leases | 20 `[F]` | AI clouds, from FY28–29 |
| SB Energy guarantees (OpenAI tenant) | up to 105 `[F]` | OpenAI's PORTS campus; effective phase by phase **from FY29**, so 2028 onward |
| Receivables build on extended payment terms, H1 FY27 | 24.6 `[F]` (`docs/nvda-analysis.md`) | Large multi-quarter customers |
| Anthropic Class N placement (November) | ~10 `[E]` | Anthropic |

- **Direct support to non-K1 buyers in a year** is about $10–15bn `[A]`: cloud buy-backs (~6 a
  year), neocloud stakes (~4) and guarantees (3.5). That is **~5–8% of non-K1 H1** (central 185).
- The large equity cheques go to OpenAI, whose compute is mostly bought from K1 clouds, and to
  Anthropic, which already holds the cash it needs.
- So NVIDIA's support matters more as a signal, and for the lab-dependent part of K1, than as the
  funding of non-K1 volume. The SB Energy guaranty supports 2028–29, not 2027.

### 3.5 What the current method already captures

**(a) The Bear's financing break.** The catalyst names "contracts at Oracle and neoclouds are
renegotiated" and "a frontier lab falls short … or cannot raise". The table below measures it
against Base:

| H1, USD bn | 2027 | 2028 | 2029 |
|---|---|---|---|
| Base / Bear | 730 / 585 | 800 / 470 | 825 / 490 |
| Bear gap | **−145 (−20%)** | **−330 (−41%)** | **−335 (−41%)** |
| Non-K1 H1 that the Bear implies, against Base `[A]` | **−25 to −30%** | **−47 to −55%** | **−45 to −50%** |
| Test shock −20% of non-K1, central (gross) | −58 | −64 | — |
| Test shock −40% of non-K1, central / high | −117 / −146 | −128 / −160 | — |

The Bear's 2027 gap is as large as the worst −40% non-K1 shock. Its 2028 gap is 2–3 times larger,
and it persists (2030 EPS .57). **The Bear already spans a non-K1 funding shortfall.** It adds the
K1 cut and the recession on top.

**(b) Signposts that already watch it:**

| Signpost (baseline) | Watches | Does not measure |
|---|---|---|
| Neocloud funding (24 Oct) | CoreWeave: missed payment, renegotiation, distressed raise; share price with spreads | Volume: non-K1 capex, NVIDIA ACIE |
| Lab financing | Anthropic IPO, OpenAI raises, SB Energy lease payments | Anthropic's $186.2bn of conditional obligations |
| Vendor financing (≥ $50bn a quarter, a call or an impairment) | NVIDIA, Broadcom, Google, Amazon support flows | — |
| Lab run-rates; K4 backlog; NVIDIA Q4 guide, DSO and inventory | Lab revenue; K1 clouds' backlog; NVIDIA's total | Whether NVIDIA's non-K1 part is falling |

**(c) Is Base internally consistent?** Yes. The H1/K1 ratio is 0.595 / 0.652 / 0.640 / 0.635
(2026–29) `[A]`. It fits a constant non-K1 share if K1 buys ~8–10% more chip value per dollar from
2027, from Rubin's larger content per GW: ~$40bn of NVIDIA revenue a GW against ~$25bn for Blackwell
`[E]`.
- **The implied non-K1 path is ~185 → ~294 → ~304 → ~309** (2026–29, central; 4.3) `[A]`: +59% in
  2027, then flat.
- The contracted evidence supports the 2027 step:
  - ACIE grew +138% y/y in Q2 FY27 `[F]`;
  - CoreWeave has 4.6 GW contracted against 1.7 GW active `[F]`;
  - Anthropic's Broadcom, AMD, Nscale and Lambda capacity arrives from 2027 `[F]`.
- The assumption is unstated, and the 2027 step adds ~$110bn of non-K1 hardware. Part of that is
  financed with neocloud debt that is not yet raised.
- Bull side note: the Bull has a lower H1/K1 ratio in 2027 (0.631) than Base. That fits the
  skill's rule that supply limits cap Bull volume, so it is not an error.

## 4. Sizing tables

### 4.1 Non-K1 H1 in 2026: three estimates

| Estimate | Build | Non-K1 USD bn / share of ~470 |
|---|---|---|
| **1. By supplier** (the AI BBB's own 2026 H1 build) | NVIDIA data center ~376 × 31–47% (3.1) = 115–175; Broadcom AI ~58 × 25–45% (Anthropic's TPU racks ~21 `[E]`, OpenAI, ByteDance; the rest Google and Meta) = 15–26; AMD Instinct ~12 × 30–60% = 4–7; custom and other ~20 × 20–40% = 4–8 `[A]` | **138–216 / 29–46%** |
| **2. Top-down from K1** | 790 × short-lived share 60–70% (Alphabet 65% servers and networking `[F]`; Microsoft about two-thirds to three-quarters `[E]`) × accelerator and AI-network share of that 50–65% `[A]` = 237–360 K1-linked | **110–233 / 23–50%** |
| **3. Named buyers' capex** | CoreWeave 37–39 `[F]`, Nebius 20–25 `[E]`, SpaceX SI ~55–60 (9M 40.0 `[F]` + Q4 `[A]`), Anthropic's leased TPUs ~20 `[E]`, other neoclouds 25–45 `[A]`, sovereign outside neoclouds 25–40 `[A]`, enterprise 15–30 `[A]` = ~200–260 of capex × H1 content 60–75% `[A]` | **120–195 / 25–41%** |
| **Used here** | All three overlap at ~140–195. The upper end, to ~215, rests on estimates 1 and 2 | **~140–215; central ~185 (39%)** `[A]` |

### 4.2 By funding exposure (2026, central ~185) `[A]`

| Group | USD bn | What its funding rests on |
|---|---|---|
| Neocloud capacity rented by K1 platforms | 30–50 | K1 credit: it holds while K1 holds; partly inside K1 already (finance leases) |
| Lab-dependent (xAI's build; Anthropic's and OpenAI's own and leased builds; neocloud capacity for labs) | 60–90 | Lab equity and IPOs (in hand for 2027), lessor and neocloud debt |
| Sovereign | 30–45 | Budgets |
| Enterprise and industrial | 15–30 | Corporate cash flow |
| **Directly NVIDIA-supported** (overlaps the rows above) | **10–15 a year** | Buy-backs, stakes, guarantees: ~5–8% |

### 4.3 The non-K1 path implied by each scenario (2026 share ~30% / 39% / 48%) `[A]`

| Scenario | 2026 | 2027 | 2028 | 2029 | Growth 2027 / 28 / 29 | Against Base 2027 / 28 / 29 |
|---|---|---|---|---|---|---|
| Base, central | 185 | **294** | 304 | 309 | +59% / +4% / +2% | — |
| Base, low / high share | 140 / 225 | 225 / 355 | 226 / 374 | 228 / 382 | +61% / +58% in 2027 | — |
| Bear, central | 185 | 215 | 153 | 165 | +16% / −29% / +8% | **−27% / −50% / −47%** |
| Bull, central | 185 | 313 | 370 | 405 | +69% / +18% / +10% | +7% / +22% / +31% |

- **Method:** K1-linked H1 = K1 × the 2026 chip intensity (470 − non-K1, ÷ 790) × a chip-content
  uplift of 1.08 / 1.10 / 1.10 in 2027–29 `[A]`. Non-K1 = H1 − K1-linked.
- **Sensitivity (central):** an uplift of 1.00 or 1.15 in 2027 gives non-K1 2027 of 326 (+76%) or
  265 (+43%).

### 4.4 Effect on the decision figures

The shock is the shortfall in non-K1 spend × the non-K1 share of Base H1. It is applied to 2027–28
("temporary") or to 2027–2030 ("persistent"), with no backfill. EPS follows the layer's own
revenue-to-EPS link, interpolated between Base and Bear (H1: 1% of revenue ≈ 1.2–1.3% of EPS in
2027–29, ≈ 1.0% in 2030) `[A]`.
- **Company figures:** the layer-method change is added to each company analysis's own Base, and its
  P_k is scaled by the layer-method P_k ratio `[A]`.
- **TSMC** takes 20–30% of the H1 revenue change: AI accelerators were "high-teens" % of 2025 revenue
  `[E]` and grow at a mid-to-high-50s% CAGR `[E]`.
- **Micron** takes 30–50% (HBM and AI server memory) `[A]`.

| Case (non-K1 share 40–50%) | H1 basket, Base NOK 11.2%; hurdle P/E 13.4 at P/E 13.7 | NVIDIA, 20.9%; P_k $212.1 at $168.89 | TSMC, 9.5%; P_k $369.8 at $396.48 | Micron, 18.3%; P_k $751.6 at $656.39 |
|---|---|---|---|---|
| Temporary −20% | 10.8–10.9%; 13.25–13.28 | 20.4–20.5%; $210 | 9.4%; $369 | 17.9–18.1%; $743–747 |
| Temporary −40% | 10.4–10.5%; 13.10–13.16 | 20.0–20.2%; $207–208 | 9.3–9.4%; $367–368 | 17.3–17.8%; $731–742 |
| Persistent −20% | 7.3–8.1%; 12.00–12.28 | 16.7–17.6%; $190–194 | 8.4–8.8%; $359–362 | 16.9–17.5%; $724–735 |
| Persistent −40% | **3.1–4.8%**; 10.60–11.16 | **12.2–14.0%; $168–177** | 6.7–8.0%; $342–355 | 14.8–16.6%; $682–718 |
| *Bear, for scale (decision Bear)* | *−10.3%* | *−5.7%; $101.5* | *−12.0%; $190.2* | *−1.7%; $472.9* |

For TSMC and Micron the −20% rows use a 40% share and the −40% rows 40–50%; their ranges also span
the pass-through (TSMC 20–30%, Micron 30–50%). Shares of 30% give smaller moves than every row shown.

**Reading:**
- **Temporary shortfalls cost ≤ 1 pp everywhere.** In the IAF build, 2027–28 earnings enter only
  through the dividends and the retained cash. The value sits in the 2030 exit.
  - Backfill makes it smaller still. NVIDIA calls supply "limited through at least the end of"
    FY28 `[E]`, and Anthropic can move capacity to its K1 contracts.
  - With 50% backfill in 2027 and 25% in 2028, the H1 basket moves only −0.2 to −0.5 pp.
- **Only persistence matters.** A shortfall that lowers the 2030 level of compute earnings is the
  Bear's mechanism, at a milder depth (2030 EPS .77–.89 against Base .97 and Bear .57).
- **No verdict flips**, with one marginal case:
  - NVIDIA still clears. At persistent −40% with a 50% share, P_k ≈ price, i.e. marginal. That
    matches NVIDIA's own price-implied k at 0.78× Base 2028–30: this shock is ~0.77–0.80×.
  - The H1 basket stays below its hurdle (it already is).
  - TSMC already fails; Micron clears at its analysis price. At $690 (6 Nov) Micron's worst case
    is marginal.
- **Minimum-change rule:** if a −20% non-K1 shortfall were evidenced, the H1 2027 EPS point would
  move by ~0.07–0.12 and 2027 growth by ~9–15 pp. Both exceed the existing rules (0.05 and 5 pp).
  The method therefore moves on evidence without a new row. What it lacks is an early, measurable
  read.

## 5. Options compared

| Option | Evidence and measurability | Double counting with the Bear | Effect on decision figures | One-place rule | Maintenance per update |
|---|---|---|---|---|---|
| **A. Document the assumption in the H1 notes** | Uses filed figures for the size; no new data stream | None | None by design (4.4: ≤ 1 pp unless persistent) | Kept: stated where H1 is set | ~0; re-state the share at the re-baseline |
| **B. New "non-K1 funding" signpost or row** | Quarterly data exist: NVIDIA ACIE `[F]`, CoreWeave, Nebius and SpaceX SI capex `[F]`, Anthropic 10-Q from Q4 `[F]`. A *row* needs the non-K1 split, which is `[A]`-heavy (3.1) | Signpost: none. Row: risk, if it adds to a Bear that already embeds −27% / −50% | None in Base until crossed | Kept | Signpost: low, but a fourth overlapping funding signpost. Row: a re-split each update |
| **C. H1 = K1-linked + a non-K1 component driven by K3/K4** | The split is `[A]` (ACIE ≠ non-K1; an unnamed reclassified company; K1 finance leases hold some neocloud capacity). K3 levels and K4 backlogs have no sourced elasticity to spend. K4 already holds lab commitments | **High:** the Bear's −27% / −50% non-K1 would be cut again through K3/K4 | None at calibration (it must reproduce 730 / 800 / 825). It opens an `[A]` channel to move H1 | Kept, but a second driver for one path | **High:** a row-definition change (method), two sub-paths, a quarterly re-split |
| **D. Company analyses only** (NVIDIA sensitivity) | Company data (ACIE) is available | None | Same numbers as above | **Weakened:** H1 feeds NVIDIA, TSMC (via its H1 check) and Micron (HBM). Each would re-derive the assumption | Spread over 3+ documents. NVIDIA v1.3 already has it |
| **A+. A, plus three measurable legs folded into the existing "Neocloud funding" signpost** (recommended) | The legs are filed quarterly: NVIDIA ACIE, named non-K1 capex, Anthropic's conditional obligations | None: a signpost, no path | None in Base. A crossing triggers a re-test, as today | Kept | **Low:** read at events already in the register (NVIDIA quarterly, CoreWeave). Two extra filings a quarter (Nebius, SpaceX). No new update events |

## 6. Recommendation

**Option A+.**

**Why it beats the alternatives:**
- **Against C:** C would double count the Bear, which already holds non-K1 −25 to −30% in 2027 and
  −45 to −55% in 2028–29. It needs an elasticity that no source gives, and it changes no Base figure.
- **Against B as a row:** the non-K1 split is too uncertain to carry a row (30–46%; one large
  customer unnamed). As a separate signpost, B duplicates three existing ones.
- **Against D:** the assumption belongs to the H1 path, which is set in one place.
- **Against A alone:** A gives no measurable early read of the 2027 non-K1 step (~+$110bn) that
  Base needs. A+ adds that read without a new row or a new update event.
- **Scale:** in all cases the decision figures move ≤ 1 pp unless the shortfall persists into
  2030, and a persistent shortfall is the Bear's mechanism.

**Revision needed:**
- `ai-market-bbb` **2026-11-DD.1**, with DD the day it is applied (2026-11-11.1 if today). The skill
  change is two clarifying lines (7b): a Step 2 check and the K2 sources. No row, path, scenario or
  basket method changes.
- The baseline changes are text (7a): the H1 note, the signpost row and closing checkpoint 10. Under
  the change gate the update is "kept unchanged" (`--changed no --affects none`).

**Evidence that would change the recommendation:**

| Evidence | Would point to |
|---|---|
| ACIE ≥ 50% of data center for two quarters, with named non-K1 capex guided ≥ +50% for 2027 | H1 growing faster than K1 for a reason K1 does not carry. Then reconsider C, or move H1 Bull-side |
| NVIDIA (or Broadcom, AMD) disclosing buyer-type revenue every quarter (AI clouds, sovereign, enterprise) | The split becomes measurable, so a K2-based sub-path becomes feasible |
| A non-K1-only shortfall while K1 holds: neocloud debt closed, CoreWeave or Nebius 2027 capex guided below 2026, ≥ $50bn of lab obligations lapsing for counterparty financing | Move H1 under the minimum-change rule. If it recurs, give non-K1 its own memo path |
| The Anthropic IPO pulled or priced below the Series H per share (~18 Nov), or OpenAI unable to raise for 2028 | The existing lab-financing Bear line, not a new mechanism |

## 7. Proposed text (not applied)

### 7a. `docs/ai-market-bbb.md`

**(1) Under "Interface — hardware", after the "H1 2026 build" bullet:**

```markdown
- **H1 buyers outside K1 (Base assumption):** H1 is set from K1, but 30–46% of H1 2026 (~140–215bn
  of ~470; central ~185) is bought outside the five platforms' capex: AI clouds and neoclouds,
  xAI, the labs' own and leased builds, sovereign and enterprise `[A]`. NVIDIA's ACIE segment was
  45% of its Q2 FY27 data center `[F]`; the sizing is in `docs/review-ai-h1-non-k1-funding.md`.
  - Base 730 / 800 / 825 keeps that share about constant: non-K1 H1 ~+60% in 2027 (range +43% to
    +76%), then flat `[A]`. **Base therefore assumes these buyers stay funded at their current
    share.**
  - Their 2027 funding is mostly raised: labs' equity and IPOs, SpaceX's IPO and notes. Neocloud
    debt is still to be raised.
  - NVIDIA's direct support is ~5–8% of non-K1 H1 `[A]`.
  - A shortfall is the financing-break Bear, which already holds non-K1 H1 −25 to −30% in 2027 and
    −45 to −55% in 2028–29 against Base `[A]`.
  - Signpost: "Non-K1 compute funding".
```

**(2) Signposts table: replace the row "Neocloud funding (new, 24 Oct)" with:**

```markdown
| **Non-K1 compute funding** (neoclouds, xAI, labs' own and leased builds; replaces "Neocloud funding") | Bear: any two of (a) NVIDIA ACIE revenue down q/q for two quarters; (b) CoreWeave + Nebius + SpaceX SI capex down q/q for two quarters, or 2027 capex guided below 2026; (c) a neocloud misses a payment, renegotiates a contract or raises at distressed terms, or ≥ USD 50bn of lab compute obligations lapse in a quarter for counterparty financing / Bull: ACIE ≥ 50% of data center for two quarters with named non-K1 capex guided ≥ +50% for 2027, or neocloud debt refinanced at investment-grade-like terms | ACIE $40.3bn, 45.3% of data center (Q2 FY27) `[F]`; CoreWeave 2026 capex $37–39bn (Q3 $9.4bn), cost of debt 7.9% `[F]`/`[E]`; Nebius 2026 capex $20–25bn `[E]`; SpaceX SI capex $16.4bn in Q3 `[F]`; Anthropic obligations subject to counterparty conditions $186.2bn `[F]`. Neither line. Next: Nebius Q3 (12 Nov), NVIDIA Q3 FY27 (17 Nov) | NVIDIA 10-Q; CoreWeave and SpaceX filings; Nebius release; Anthropic S-1/A and 10-Q |
```

- The thresholds are conventions `[A]`.
- In the ten quarters of NVIDIA's recast series (S2), ACIE never fell q/q twice running. It fell
  once, in Q3 FY26, during the boom.
- 50bn is above the largest single lapse now visible (Lambda, 34.9bn terminable).

**(3) Open checkpoint 10: replace it with:**

```markdown
10. **H1 demand outside K1: closed (Option A+ of `docs/review-ai-h1-non-k1-funding.md`).** The Base
    assumption is stated in the H1 notes. The non-K1 funding read is the "Non-K1 compute funding"
    signpost. No row and no path changed.
```

### 7b. `.claude/skills/ai-market-bbb/SKILL.md` (revision 2026-11-DD.1)

- **Rows, Money in, K2:** replace "Memo, `[?]` until a source exists" with "Memo; sources: NVIDIA
  ACIE (10-Q), CoreWeave and Nebius capex, SpaceX SI segment capex, Anthropic filings".
- **Step 2, the check sentence:** append ", and the non-K1 share that the H1/K1 ratio implies
  against NVIDIA's ACIE share and the named non-K1 capex (Base keeps that share; a shortfall is the
  financing-break Bear)".
- **Change note:** "2026-11-DD.1: H1's non-K1 buyers made explicit (K2 sources, Step 2 check), from
  `docs/review-ai-h1-non-k1-funding.md` Option A+. No row, path, scenario or basket-method change."

## 8. Open data gaps

| Gap | Why it matters | When it may close |
|---|---|---|
| The company NVIDIA moved from ACIE to Hyperscale (~$5.2bn in Q1 FY27) `[?]` | It decides whether Hyperscale holds non-K1 demand (0–9 pp of data center) | NVIDIA Q3 FY27 call (17 Nov), if asked |
| NVIDIA's split of ACIE (AI clouds, sovereign, enterprise) and the share of AI-cloud capacity rented by K1 `[?]` | The main reason the range is 30–46% and not tighter | Not disclosed; growth rates only |
| Whether K1 neocloud rentals sit in K1 capex as finance leases `[?]` | It removes a possible overlap between K1 and ACIE | Microsoft 10-Q lease notes; partial evidence only |
| Broadcom's XPU customer mix (six customers, unnamed) and AMD Instinct revenue `[?]` | It sets the non-K1 part of the ~90bn of H1 outside NVIDIA (23–41) | Broadcom Q4 FY26 (~mid-December); AMD 10-K |
| CoreWeave and Nebius 2027 capex and funding plans `[?]` | The part of 2027 non-K1 funding still to be raised | Nebius Q3 (12 Nov); CoreWeave Q4 (~late February 2027) |
| OpenAI's audited cash, burn and the timing of its next round `[E]`/`[?]` | The 2028 funding step; OpenAI is private | Press; Microsoft 10-Q (receivables) |
| Sovereign and enterprise totals `[A]` | 45–75bn of the 2026 estimate | NVIDIA commentary only |
| The H1 content of non-K1 capex (60–75%) and the chip-content uplift per K1 dollar (1.08–1.10) `[A]` | They drive estimate 3 and the implied path (4.3) | Company capex breakdowns, e.g. SpaceX SI by asset type |

## Sources

| # | Source | Used for |
|---|---|---|
| S1 | NVIDIA 10-Q, Q2 FY27 (EDGAR, filed 26 Aug 2026): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm | Platform revenue, customer notes, reclassification, AI cloud agreements, SB Energy guarantees, equity purchases `[F]` |
| S2 | NVIDIA Q2 FY27 Revenue by Market Platform slides: https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q227-Revenue-by-Market-Platform-Slides.pdf | Ten quarters of Hyperscale and ACIE, recast `[F]` |
| S3 | NVIDIA Q1 FY27 call, FactSet corrected transcript: https://s201.q4cdn.com/141608511/files/doc_financials/2027/q1/NVDA-Q1-2027-Earnings-Call-20-May-2026-5_00-PM-ET.pdf | Hyperscale and ACIE definitions, neoclouds in ACIE, sovereign +80% `[E]` |
| S4 | CoreWeave 8-K Ex. 99.1, Q3 2026 (EDGAR, 10 Nov 2026): https://www.sec.gov/Archives/edgar/data/1769628/000176962826000461/coreweave3q26earningspress.htm; Q2 2026 call transcript: https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CRWV-US-CORRECTED-TRANSCRIPT-CoreWeave-Q2-2026-Earnings-Call-11August2026.pdf | Capex, backlog, cash flows, financing `[F]`; funding model `[E]` |
| S5 | Anthropic S-1/A No. 2 (EDGAR, 10 Nov 2026): https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm | Contractual obligations, Broadcom leases, SpaceXAI, Nscale, Lambda, AMD, liquidity, IPO `[F]` |
| S6 | SpaceX 10-Q, Q3 2026 (EDGAR, 22 Oct 2026): https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm | SI segment capex and revenue, notes, IPO proceeds, liquidity `[F]` |
| S7 | `docs/nvda-analysis.md` v1.3 (11 Nov) | CoreWeave Q3 call items (> 75% investment grade, 7.9% cost of debt) `[E]`; receivables; P_k and price-implied multiplier |
| S8 | `docs/tsm-analysis.md` v1.2, `docs/mu-analysis.md` v3 | Base, P_k, prices for the pass-through |
| S9 | OpenAI round: Bloomberg, 31 Mar 2026 (https://www.bloomberg.com/news/articles/2026-03-31/openai-valued-at-852-billion-after-completing-122-billion-round); Engadget (https://www.engadget.com/ai/openai-secures-another-110-billion-in-funding-from-amazon-nvidia-and-softbank-171006356.html) | $122bn at $852bn; Amazon, NVIDIA, SoftBank amounts `[E]` |
| S10 | OpenAI burn: Reuters/FT via The Star, 19 Sep 2026 (https://www.thestar.com.my/tech/tech-news/2026/09/19/openai-forecasts-cash-burn-near-280-billion-by-2030-ft-reports); The Decoder (https://the-decoder.com/openai-adds-111-billion-to-its-cash-burn-forecast-as-ai-costs-spiral-beyond-projections/) | Burn 2026–27; cash into 2028 `[E]` |
| S11 | Nebius 2026 capex guide: Newsquawk (https://www.newsquawk.com/headlines/nebius-nbis-raises-2026-capex-guidance-to-between-usd-20-25bln-according-to-remarks-on-conference-call) | $20–25bn `[E]` |
| S12 | Neocloud contracts and NVIDIA's stakes in CoreWeave and Nebius: NeuronFeed, 11 Jul 2026, summarising io-fund (https://neuronfeed.com/news/nvidia-invests-4-billion-in-coreweave-and-nebius-gpu-cloud-partners) | Microsoft ~$60bn, Meta contracts, $2bn stakes each. Secondary `[E]`; used only for orders of magnitude |
| S13 | NVIDIA sovereign: Motley Fool Q4 FY26 call summary (https://www.fool.com/investing/2026/02/28/nvda-earnings-call-stock-q4-ceo-cfo); Crypto Briefing on Q2 FY27 (https://cryptobriefing.com/nvidia-cfo-sovereign-ai-business-doubles-yoy/) | > $30bn in FY26; about double y/y in Q2 FY27 `[E]` |
| S14 | Broadcom Q3 FY26: 8-K (https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm) and call coverage (https://www.datacenterdynamics.com/en/news/broadcom-slams-ai-silicon-fueled-q3-promises-double-double-on-the-way/) | AI revenue $16.7bn, Q4 guide $21.7bn `[F]`; FY27 ~$115bn, six XPU customers `[E]` |
| S15 | SpaceX IPO pricing: Benzinga (https://cdn2.benzinga.com/markets/ipos/26/06/53180108/spacex-stock-closes-up-19-in-record-shattering-ipo-debut); xAI capex history: TechCrunch (https://techcrunch.com/2026/05/20/xai-burned-6-4b-last-year-spacexs-ipo-filing-shows-why-the-spending-is-far-from-over/) | ~$75bn at $135 `[E]`; xAI Q1 2026 capex $7.7bn `[E]` |
| S16 | TSMC AI-accelerator share: Q4 2025 call via secondary coverage (https://www.nextplatform.com/compute/2026/01/16/tsmc-has-no-choice-but-to-trust-the-sunny-ai-forecasts-of-its-customers/4092173) | "High-teens" % of 2025 revenue; mid-to-high-50s% CAGR `[E]` |
