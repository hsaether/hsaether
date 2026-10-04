---
name: iaf-valuation
description: Investment Analysis Framework (IAF) — a forward-looking valuation screen using a dividend-yield-plus-growth hurdle test (d plus g must exceed k) and the resulting PE (or P/FCF) ceiling, combined with a Bear/Base/Bull scenario build. ALWAYS use this skill whenever the user asks to value or screen a company "using the IAF" or "the framework", mentions "d+g" versus "k", a "PE ceiling", a "BBB case" or "Bear/Base/Bull", asks whether a stock "clears the hurdle" or "k", or wants an investment thesis / stock screen built around a required-return test — even if they don't say "IAF" by name. This is the standing valuation methodology for this workspace; default to it for any company valuation request unless the user asks for a different approach.
---

# Investment Analysis Framework (IAF)

A forward-looking, total-return-based screen for whether a stock's price is defensible. It is a
margin-of-safety filter, not a discounted cash flow model — it tells you what multiple is
defensible given expected yield and growth, not an intrinsic value. Always be explicit about that
distinction when presenting results.

## Definitions

| Symbol | Meaning |
|---|---|
| P | Current stock price |
| E | Earnings (use for most companies) |
| FCF | Free Cash Flow (use instead of E for shipping, offshore, and other capex/D&A-distorted, cyclical sectors) |
| d | Forward dividend yield at entry price — the income component of expected return |
| g | Expected per-share growth in the chosen metric (EPS for PE, FCF/share for P/FCF) to the terminal year of the forecast window (3–5 years out) — the capital-appreciation component. It is a consequence of the capital-allocation build (see Growth policy), not an independently forecast number |
| k | Required rate of return. Baseline **12%**, and **never set below 10%** |
| PE | P/E (or P/FCF for FCF-based names) |

## Core test

**Rule 1 — total return hurdle:**
```
d + g > k        equivalently        (d + g) / k > 1
```

**Rule 2 — no-growth fair-value anchor:**
```
PE = 1/k         (a zero-growth stock priced to return exactly k)
```

**Rule 3 — combined PE ceiling** (Rule 1 and Rule 2 combined, PE·k=1 and (d+g)/k>1):
```
PE < (d + g) / k²
```
For FCF-based names, substitute P/FCF for PE throughout.

Worked examples at k=12% (k²=0.0144):
- d=1%, g=20% → PE < 14.6
- d=1%, g=30% → PE < 21.5

**Note the two things being combined**: Rule 1 is a total-return hurdle test; Rule 2 is a no-growth
earnings-yield anchor. Multiplying them gives a defensible-multiple heuristic, not a value derived
from a single coherent cash-flow model — say so when presenting a ceiling, so it's never mistaken
for a price target.

## Computing g: forward, year-by-year, to a terminal value

1. **Forward-looking only** — never trailing. d, g, and PE/P-FCF must all sit on the same
   forward-looking basis.
2. **Build each of the 3–5 years bottom-up**, driven by the real levers for that company (charter
   rates, deliveries, dry-docking and capex cycles for shipping/offshore; unit growth, pricing,
   margin trajectory for others) — not a flat extrapolated growth rate.
3. **What matters is the end value.** g is derived from the terminal year (year 3 or year 5) versus
   today, not from requiring every single intermediate year to individually clear d+g>k. A weak
   year in the middle of an otherwise strong build is not a failure on its own — it's just part of
   the path to the endpoint.
4. **d is separate from this build** — it's the yield earned on the entry price over the holding
   period, not a terminal-year figure.
5. Apply Rule 1 and Rule 3 to the resulting (d, g) pair.

## Growth policy

Growth is the softest input in the framework. Fix its definition before projecting it.

**All companies**

1. **Match the metric to the multiple**: EPS growth for PE, FCF-per-share growth for P/FCF.
   Revenue growth is a driver, never the g in d+g.
2. **Per share, not aggregate.** Adjust for dilution (new equity issued to fund growth) and
   buybacks.
3. **Decompose and forecast drivers**: revenue = volume × price; earnings = revenue × margin;
   FCF = earnings − capex + D&A ± working capital. Let g fall out of the drivers.
4. **Use geometric (compound) growth**, never the average of annual rates. Fade growth toward a
   sustainable long-run rate; no above-k growth in perpetuity.
5. **Strip out non-repeatable items** (one-offs, vessel-sale gains, M&A, FX) before measuring
   growth.
6. **Never compute a growth rate from a base near zero or negative.** Work with levels and express
   the change against a stable base (per-share value, market cap).

**Growth as a capital-allocation decision (linking reinvestment to the terminal value)**

Growth is not free: capital spent to grow the business reduces cash available for distribution now,
and the payoff shows up later as a larger earning or cash-generating base. A model that forecasts
lower near-term FCF because of growth capex, without crediting the resulting increase in the
company's earning power, makes growth look like a pure cost. Make the link mechanical, not implicit:

1. **Split each year's cash flow into maintenance FCF and growth capex.** Maintenance FCF is what
   the business generates before any capital spent to grow it (replacement capex only). Growth
   capex is capital spent beyond that, to expand the earning base (new vessels, new rigs, expansion
   projects). The distribution used in the IRR, D_t = maintenance FCF − growth capex (adjusted for
   debt funding if growth is debt-funded rather than self-funded from FCF).
2. **Roll the invested capital forward.** Track an invested-capital or NAV base that increases each
   year by that year's growth capex (plus any asset revaluation). The terminal value V_t is not a
   free-standing guess — it is this rolled-forward base (or the earning power it supports) at year t.
3. **State the return assumption on the growth capex explicitly: ROIC (or ROE for equity-funded
   growth).** Derive it from realised economics — historical returns on past newbuilds or
   projects, contracted day rates/charters on the new capacity — not an invented number. This ROIC
   is what turns growth capex (lower D_t) into a larger V_T.
4. **Test ROIC on the growth capex against k, separately from the overall d+g>k test.** This is the
   actual investment decision on growth:
   - ROIC on new capital > k → growth is accretive to IRR even though it lowers near-term
     distributions. State this explicitly, so growth isn't penalised by a naive read of falling D_t.
   - ROIC on new capital ≤ k → growth is value-destructive even if it raises revenue, earnings, or
     FCF in absolute terms. Flag this — rising FCF is not the same as rising value if the capital
     funding it doesn't earn its keep.
5. **g is a consequence of this build, not an independently forecast number.** The implied g
   (= IRR − d) should fall out of the maintenance-FCF / growth-capex / ROIC build above.

**Cyclical and asset-heavy names (tankers, offshore, etc.)**

- **Cyclical growth mean-reverts; it does not compound.** A rate spike is a recovery that
  reverses, not a growth engine. Do not capitalise it into g — keep it separate from the structural
  growth produced by the capital-allocation build above.
- **The base year decides the answer** (a trough flatters, a peak penalises). Use a normalized,
  mid-cycle base and terminal value, state how it is defined, and never take the last modeled year
  as the terminal value by default.
- **Model levels, not growth rates.** Build FCF to equity per year in each scenario, then derive
  growth from the levels.
- **Definition: IRR, year by year.** For each year t = 1..T (T = 3 or 5) in each scenario, estimate
  the distribution per share D_t (from the maintenance-FCF/growth-capex split above) and the
  normalized value per share V_t at the end of that year — built from the rolled-forward
  invested-capital/NAV base and stated ROIC, never assumed independently and never the IAF PE
  ceiling itself as the exit multiple (that is circular) — with V_0 = P. Report for every year:
  - the annual total return r_t = (D_t + V_t − V_(t−1)) / V_(t−1), and
  - the cumulative IRR from entry to an exit at year t, solving
    P = sum over s≤t of D_s / (1+IRR)^s + V_t / (1+IRR)^t.
  Rule 1 is tested on the terminal-year IRR (year T) > k, and implied g = IRR_T − d is used in
  Rule 3. The yearly r_t and the IRR-to-each-year are a path diagnostic, not a per-year pass/fail:
  a weak middle year is not a failure, but it must be visible.
- **Split implied g into structural and cyclical parts** — structural = growth capex compounding at
  its ROIC (fleet additions, NAV change); cyclical = rate reversion around mid-cycle — and report
  both, so it is visible how much of the return depends on the cycle turning versus capital actually
  being put to work above k.
- **Flag growth quality**: growth funded by share issuance, gains on asset sales, and dependence on
  the cycle turning.

## Bear / Base / Bull (BBB): stress tests around a Base case, not statistical percentiles

There is no return distribution behind these scenarios — they are built from a qualitative read of
specific drivers (chokepoints, fleet supply, OPEC decisions, rig demand, etc., typically from the
relevant sector BBB skill) rather than from historical data you could calibrate a percentile
against. Treating Bear/Bull as a 25th/75th percentile overstates the rigor behind them.

1. **Base is the investment case.** It carries the IRR (or d+g) used for the Rule 1 and Rule 3
   decision. It is the single most-likely path, built from the central view in the relevant sector
   BBB skill(s) (Oil Market BBB, Oil Shipping BBB, Rig Market BBB, etc.) and the capital-allocation
   build above.
2. **Bear and Bull are stress tests, each anchored to a specific, named catalyst or risk** from the
   sector BBB skill(s) (e.g. a named chokepoint reopening, an oversupply event, a demand-destruction
   scenario) — not a generic "X% worse/better" shift applied mechanically to the Base case. They do
   not need to be symmetric in severity; use the worst and best *reasonably foreseeable* cases, not
   an arbitrary symmetric band.
3. **Use Bear to test resilience, not to compute an expected value.** Report whether the Base case
   decision survives Bear — IRR still acceptable, or at least capital broadly preserved (e.g. V_T
   doesn't fall through a liquidation/NAV floor). If Bear breaks the thesis, say so plainly; that is
   the point of the stress test.
4. **Use Bull to show the asymmetry and optionality**, not a 25% chance of happening. Report how
   much upside is available if the named catalyst materialises, and whether the Base case already
   prices much of it in.
5. **Do not default to a single probability-weighted number.** Report Base, Bear, and Bull as three
   distinct IRRs (and PE/P-FCF ceilings), each with the catalyst behind it. If a single comparable
   figure is wanted for screening across many names, it may be shown as a "scenario-weighted
   reference figure" using the 25/50/25 convention — but it must be labelled explicitly as a
   summarising convention, not a calibrated probability-weighted expectation, and it must never
   replace showing Base on its own as the actual decision case.

## Sector variant: E vs FCF

- **Default**: earnings (E) and PE.
- **Shipping, offshore, and other capital-intensive, cyclical sectors**: use FCF and P/FCF instead.
  Capex and amortization swing E around in ways that don't reflect the underlying cash economics,
  and a single year's FCF is rarely representative — which is exactly why the multi-year forward
  build matters most for these names. Apply the cyclical rules in the Growth policy section.

## Applying the framework to a company

When asked to run the IAF on a company, produce:

1. **Inputs**: current price, current forward dividend yield (d), whether this is an E-based or
   FCF-based name (state which and why).
2. **The year-by-year build** for Base, Bear, and Bull, out to year 3 or 5 — name the catalyst
   behind each scenario, and show the terminal value driving each scenario's g, the maintenance
   FCF / growth capex split, and the ROIC assumption on growth capex. State the growth metric and
   base used, and for cyclicals show the year-by-year table (D_t, V_t, r_t, cumulative IRR) and the
   structural vs cyclical split.
3. **Rule 1 check** (IRR or d+g vs k) for Base — the decision figure — and the resilience/upside
   read from Bear and Bull.
4. **ROIC vs k on growth capex**, stated separately from Rule 1 — flag whether growth is accretive
   or value-destructive regardless of the direction of FCF/earnings.
5. **Rule 3 ceiling** (PE or P/FCF < (d+g)/k²) for Base, Bear, and Bull individually. An optional
   scenario-weighted reference figure (25/50/25) may be shown alongside, clearly labelled as a
   convention, not a probability-weighted expectation.
6. **A read against the current multiple**: is the stock's actual PE/P-FCF inside the Base ceiling,
   and does the position survive the Bear stress test — not just whether it clears a blended number.
7. A short caveat line noting this is a margin-of-safety screen, not an intrinsic valuation.

## Standing parameters (don't ask the user to re-supply these each time)

- k = 12% baseline; hard floor of 10% — never go lower even for very safe names.
- BBB weights = 25% Bear / 50% Base / 25% Bull remain only as the convention for an optional
  scenario-weighted reference figure, not as calibrated probabilities. The Base-case IRR is the
  primary decision figure.
