# IAF — Reference Notes

Background notes on the Investment Analysis Framework (IAF), for your own reference alongside the
skill definition in `.claude/skills/iaf-valuation/SKILL.md`. This captures the reasoning behind the rules,
not just the rules themselves.

## What the framework actually is

Two different ideas, combined:

1. **Total return hurdle** (d + g > k) — dividend yield plus growth should clear the required
   return.
2. **No-growth fair-value anchor** (PE = 1/k) — the earnings yield a zero-growth stock "should"
   trade at if priced to return k.

Multiplying them gives the PE ceiling PE < (d+g)/k². This is a **margin-of-safety screening
heuristic**, not a discounted cash flow value. Unlike a Gordon-growth justified PE
(payout/(k−g)), it stays bounded and linear in (d+g) rather than diverging as g approaches k —
useful for high-growth names, but it means the ceiling is "how much premium is defensible," not
an intrinsic price target.

## Design decisions made while building this

- **g comes from the BBB scenarios, not a separate forward-estimate source.** BBB is upstream of
  the test: you build the scenarios first, then g falls out of them.
- **g and d are modeled year-by-year within the 3–5 year build**, not as a single blended/endpoint
  guess — for capex/D&A-heavy sectors (shipping, offshore) a flat growth assumption hides too much.
- **What matters most is the end (terminal) value**, not a per-year pass/fail. The year-by-year
  build exists to make the terminal number defensible, not to gate every individual year against
  d+g>k. A weak year in the middle of a strong multi-year build is not itself a failure.
- **Risk lives in the Bear/Base/Bull spread, not inside a single scenario** — and (revised) the
  spread is a set of stress tests around Base, not a statistical range. See "BBB reframed" below.
- **FCF replaces E for shipping/offshore and similarly capex/D&A-distorted, cyclical sectors**,
  with P/FCF replacing PE throughout the same formulas.

## Growth policy (added later)

- Match the growth metric to the multiple (EPS for PE, FCF/share for P/FCF), measured per share,
  geometric, from drivers rather than a flat rate. Never compute growth from a near-zero or
  negative base.
- Cyclicals (e.g. tankers): growth from a rate recovery mean-reverts and does not compound. Use a
  normalized mid-cycle base and terminal value, model FCF levels per scenario, and define d+g as the
  scenario IRR (buy at P, year-by-year distributions, sell at normalized terminal value). Implied
  g = IRR - d. Split g into structural (fleet, NAV) and cyclical (rate reversion) parts.
  **Superseded 2026-10-05:** g is now the value CAGR (V_T vs P), IRR = d + g + c, and the
  structural/cyclical split is made on IRR. See the review below.
- Weight scenario levels, not growth rates, then derive the weighted g or IRR from the weighted path.
- Decision: IRR, computed year by year (annual return each year plus the cumulative IRR to each exit
  year), with the terminal-year IRR tested against k. The yearly path is a diagnostic, not a
  per-year pass/fail.

## BBB reframed: stress tests, not percentiles (added later)

There's no return distribution behind the sector events (chokepoints, OPEC decisions, rig demand) —
they're qualitative, not drawn from historical data you could calibrate a percentile against.
Treating Bear/Bull as a 25th/75th percentile overstated the rigor behind them. Revised structure:

- Base is the investment case and carries the actual decision (IRR/d+g vs k). It's the central view
  from the relevant sector BBB skill, not an average of three scenarios.
- Bear and Bull are stress tests anchored to a specific named catalyst each, not a generic
  symmetric shift. Bear asks "does the thesis survive this"; Bull asks "how much upside, and is it
  already priced in" — neither is a calibrated probability.
- No default probability-weighted blend. An optional 25/50/25 "scenario-weighted reference figure"
  can still be shown for cross-name screening, but must be labelled as a convention, never as a
  calibrated expectation, and never substituted for Base as the decision figure.

## Growth as capital allocation (added later)

Growth capex reduces distributable cash now and raises earning power later — a model that shows
the cost (lower FCF) without crediting the benefit (higher terminal value) makes growth look like a
pure drag. Revised to make the link mechanical:

- Split each year into maintenance FCF (before growth spending) and growth capex. D_t (the
  distribution used in the IRR) = maintenance FCF − growth capex.
- Roll invested capital/NAV forward by each year's growth capex; the terminal value V_t is built
  from that rolled-forward base at a stated ROIC, not assumed independently.
- State the ROIC on growth capex explicitly (from realised economics — past newbuild returns,
  contracted charters — not invented), and test it against k separately from d+g>k: ROIC > k means
  growth is accretive even though near-term distributions fall; ROIC ≤ k means growth is
  value-destructive even if FCF/earnings are rising.
- g becomes an output of this build (implied g = IRR − d), not an independently forecast number.

## Optimization review (2026-10-04)

- Two tracks: Track A (steady, E/PE, Rules 1–3) and Track B (cyclical/capital-intensive, FCF,
  year-by-year IRR). When in doubt, Track B.
- Track B decides on the hurdle price P_k (value at k of D_t and V_T) versus P. IRR > k and P < P_k
  are the same test, but P_k is not circular, while the Rule 3 ceiling built from IRR depends on P.
  Rule 3 is kept as a cross-check. Note: Track B is in effect a short-horizon cash-flow valuation.
- D_t is defined as actual distributions (dividends + buybacks); retained cash goes into V_t via net
  debt. Fixes a possible double count and resolves the dividend-policy open item.
- Growth capex valued as capex × ROIC_g / k (NAV for finite-life assets), so ROIC_g > k shows up as
  value created inside the IRR.
- V_T must be shown as a bridge (start value, growth capex value, net debt change, cycle
  normalization).
- Bear has explicit tests: Bear IRR, capital preservation (ΣD_t + V_T vs P), balance-sheet survival.
- Optional 25/50/25 figure weights levels (D_t, V_T), not IRRs.
- k may be raised (never lowered) for leverage, single-asset exposure or illiquidity.
- Fixed output template and a final checklist added.

## Time grid: stub period + 3 calendar years (added 2026-10-04)

- Horizon = rest of the current year (stub) + 3 full calendar years; exit 31 Dec of year 3; window
  rolls forward each January. Calendar years match company reporting and the sector BBB skills.
- Stub and Year 1 modelled quarterly, Years 2–3 annually. Stub built from locked-in information
  (booked days, guidance, actual spot); never annualised.
- Cash flows discounted from actual payment dates (XIRR style); declared dividends count only if
  the share is not yet ex-dividend.
- The stub matters little for the IRR; its value is the starting net debt (rolled forward to
  31 Dec), near-term catalysts, and tracking actuals against the Base path after each report.
- Scenarios barely differ in the stub; Bear and Bull diverge from Year 1.

## Review against CAPT, SED and DOF (2026-10-05)

Test cases: `docs/capt-analysis.md` (rev .12, shipping), `docs/SED-analysis.md` (rev .12, rigs),
`docs/DOF-analysis.md` (rev .13, OSV). The three original Python models were re-run unchanged and
the d/g split was recomputed from them. Result: skill rev **2026-10-05.1**.

### Decision figures: correct

All nine IRR_T and P_k values (3 companies × Bear/Base/Bull) reproduce exactly from the models.
d, the margin of safety, the Bull share priced and the Rule 3 ceilings also check. None of the
findings below changes a verdict: CAPT fails, SED fails, DOF is marginal.

### g: computed as the skill said, but the skill's formula was wrong

The analyses all used g = IRR_T − d, as the skill prescribed (rev .12 and .13). That formula has
three problems.

**1. It is a plug, not value growth.** d is a simple, undiscounted yield on the entry price and IRR
is compound and time-weighted, so IRR − d contains a timing term c. The plug differs from the true
per-share value CAGR (V_T vs P) by up to 1.9 pp, and it flatters g whenever value falls.

**2. It hides a re-rating.** V_T is a NAV but P is a market price, so g contains the P/NAV gap
closing by exit. Where the price sits away from mid-cycle NAV, this dominates g.

**3. The structural/cyclical split was mislabelled.**
- It was made on g only, so the cycle's effect through d was missed. DOF noticed this; CAPT and SED
  did not.
- Bear and Bull were measured against the Base structural run, so their lower or higher mid-cycle
  asset values were labelled "cyclical".

| Case | IRR_T | d | g reported (IRR − d) | g value CAGR | c | P/NAV_0 | re-rating / NAV growth | Structural IRR, own mid-cycle | Cyclical, IRR pp (reported, g only) |
|---|---|---|---|---|---|---|---|---|---|
| CAPT Bear | −20.9 | 3.3 | −24.1 | −24.2 | 0.0 | 3.54 | −32.3 / +12.0 | −23.6 | +2.8 (−14.8) |
| CAPT Base | 2.6 | 7.5 | −4.9 | −5.5 | +0.6 | 1.65 | −14.4 / +10.3 | −5.5 | +8.1 (+4.4) |
| CAPT Bull | 35.5 | 20.4 | 15.1 | 15.7 | −0.6 | 0.96 | +1.3 / +14.2 | 11.1 | +24.3 (+24.4) |
| SED Bear | −35.6 | 5.4 | −41.1 | −40.7 | −0.4 | 2.09 | −20.3 / −25.6 | −38.2 | +2.6 (−31.9) |
| SED Base | 5.3 | 12.6 | −7.3 | −9.3 | +1.9 | 0.90 | +3.4 / −12.3 | 2.8 | +2.4 (+1.9) |
| SED Bull | 28.3 | 17.0 | 11.3 | 10.3 | +1.0 | 0.59 | +17.8 / −6.3 | 27.4 | +0.9 (+20.5) |
| DOF Bear | −11.5 | 5.6 | −17.1 | −17.5 | +0.4 | 1.54 | −12.5 / −5.7 | −11.7 | +0.3 (−16.8) |
| DOF Base | 11.3 | 11.6 | −0.3 | −1.1 | +0.7 | 0.86 | +4.6 / −5.4 | 9.5 | +1.8 (0.0) |
| DOF Bull | 29.6 | 14.9 | 14.6 | 15.3 | −0.7 | 0.56 | +19.6 / −3.6 | 26.5 | +3.0 (+14.9) |

All figures are % a year. NAV_0 is at each scenario's own mid-cycle marks at the valuation date.
CAPT's "NAV today" of NOK 169 is at war-time market marks; at Base mid-cycle marks it is NOK 111.6.

What the corrected split shows:
- **CAPT:** the price is 1.09x market NAV but 1.65x Base mid-cycle NAV, and equals NAV at *Bull*
  mid-cycle marks (0.96x). The windfall cash and the newbuild programme grow NAV by ~10% a year, but
  the cycle premium in the price unwinds by 14% a year. CAPT Bull is a genuine rate-cycle test
  (+24 pp cyclical). On Bull mid-cycle rates from 2027 the IRR is only 11.1%.
- **SED:** NAV at Base marks falls 12% a year (contract roll-off, ageing). The 10% discount closing
  adds 3.4% a year. Bear and Bull are mid-cycle shifts, not cycles (cyclical +2.6 / +0.9 pp).
- **DOF:** g ≈ 0 is NAV falling 5.4% a year, offset by a 14% discount to NAV assumed to close by
  2029. The DOF text says "RSV value created roughly offsets fleet ageing and premium roll-off".
  Its own V_T bridge contradicts that: RSVs add NOK 3.8 per share, against ageing −25.0, premium
  roll-off −10.7 and net debt −9.7. Bear and Bull are mid-cycle shifts.

### Reporting consistency across the three

| Item | CAPT | SED | DOF | Fix in rev 2026-10-05.1 |
|---|---|---|---|---|
| "NAV today" | Market marks, valuation date (169, 1.09x) | Base mid-cycle + contract premium, valuation date (7.19, 0.90x) | Base mid-cycle at 31 Dec labelled "today" (145.5, 0.88x); broker fleet only (109, 1.17x) | Two NAVs at the valuation date: market marks and NAV_0 (Base mid-cycle) |
| Interim V_t | Glide from market marks; end-2026 equal in all scenarios | Scenario mid-cycle from end-2026: stub r_t −51% / +13.5% / +73% | Same: stub r_t −34% / +17% / +79% | Glide from market marks; end-of-stub marks identical (Step 6). SED/DOF "IRR to 2027" (12.4% / 19.4%) is an artefact |
| Maintenance FCF | After debt amortisation | After debt amortisation | Before amortisation ($86m a year) | Before amortisation; amortisation on its own line |
| Rule 3 FCF_normalised | After amortisation, no ageing | After amortisation, no ageing | Before amortisation, no ageing | After a fleet-renewal charge, before amortisation |
| Rule 3 on that basis (P/FCF vs ceiling) | 22.8x → 16.4x vs 1.8x | 18.1x → 86.7x vs 3.6x | 8.1x → 17.2x vs 7.8x | DOF goes from "fails narrowly" to a clear fail; no verdict changes |
| Rule 3 row order | Ceiling vs actual | Ceiling vs actual | Actual vs ceiling | "P/FCF x vs ceiling y" |
| V_T bridge start | Delivered fleet − net debt at end-2026 | NAV end-2026 | NAV end-2026 | From NAV_0, with re-rating shown above it |
| Structural run | Base mid-cycle from Q1-27 | Base mid-cycle incl. options | Base mid-cycle, open days | Own mid-cycle per scenario; on IRR |
| Tags | F E A ? | + C | + B | Standard set F B E C A ? |
| Sections | No Market input, For other modules or Sources appendix | All | All (no Tracking: first version) | Fixed document order |

Also:
- **Verdict band.** "Marginal (within ±2% of k)" was ambiguous. DOF read it as the margin of safety
  (−1.7%), which matches the worked example (IRR 11.0%, MoS −2.5%, "fails"). Rev .1 now defines it
  on the margin of safety: within ±2%.
- **Retained cash.** No analysis showed the retained-cash line; all three showed net debt instead,
  which is equivalent. Rev .1 makes net debt the required line.

### Corrections needed in the analyses (next update, under rev 2026-10-05.1)

- **All three:**
  - Results rows: d / g / c, re-rating / NAV growth, structural IRR / cyclical (per own mid-cycle).
  - V_T bridge from NAV_0.
  - Rule 3 with the renewal charge.
  - Standard tags and section order.
- **CAPT:** add NAV_0 at Base mid-cycle marks (111.6, 1.65x) beside market NAV. Restate
  "structural g −9.3%": it is mostly the cycle premium in the price unwinding.
- **SED:** re-mark interim V_t with a glide (end-2026 equal across scenarios). Restate Bear/Bull as
  mid-cycle shifts.
- **DOF:**
  - Correct the structural-g sentence.
  - Re-mark interim V_t.
  - Rule 3 reads 17.2x vs 7.8x.
  - Move amortisation to its own line (dividends unchanged: the payout follows the leverage policy).

## Open items / things to revisit later

- Whether to raise k as a default for small-cap, highly leveraged names, or keep 12% and judge
  case by case.
- Roll CAPT, SED and DOF onto rev 2026-10-05.1 (corrections listed above).
- Track A has not been tested on a real case yet (all three tests were Track B).
