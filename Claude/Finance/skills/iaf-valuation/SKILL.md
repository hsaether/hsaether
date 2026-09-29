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
| g | Expected per-share growth in the chosen metric (EPS for PE, FCF/share for P/FCF) to the terminal year of the forecast window (3–5 years out) — the capital-appreciation component. See Growth policy |
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
4. **Growth costs reinvestment.** Cash used to grow cannot also be paid as dividends. Check that d
   and g together are consistent with the cash generated and the return on new capital.
5. **Use geometric (compound) growth**, never the average of annual rates. Fade growth toward a
   sustainable long-run rate; no above-k growth in perpetuity.
6. **Strip out non-repeatable items** (one-offs, vessel-sale gains, M&A, FX) before measuring
   growth.
7. **Never compute a growth rate from a base near zero or negative.** Work with levels and express
   the change against a stable base (per-share value, market cap).

**Cyclical and asset-heavy names (tankers, offshore, etc.)**

- **Cyclical growth mean-reverts; it does not compound.** A rate spike is a recovery that
  reverses, not a growth engine. Do not capitalise it into g.
- **The base year decides the answer** (a trough flatters, a peak penalises). Use a normalized,
  mid-cycle base and terminal value (e.g. mid-cycle rates × operating days, or NAV), state how it
  is defined, and never take the last modeled year as the terminal value by default.
- **Model levels, not growth rates.** Build FCF to equity per year in each scenario, then derive
  growth from the levels.
- **Definition for cyclicals: IRR, year by year.** For each year t = 1..T (T = 3 or 5) in each
  scenario, estimate the distribution per share D_t and the normalized value per share V_t at the
  end of that year (NAV/share, or mid-cycle FCF/share × a stated exit multiple; never use the IAF
  PE ceiling itself as the exit multiple, that is circular), with V_0 = P. Report for every year:
  - the annual total return r_t = (D_t + V_t − V_(t−1)) / V_(t−1), and
  - the cumulative IRR from entry to an exit at year t, solving
    P = sum over s≤t of D_s / (1+IRR)^s + V_t / (1+IRR)^t.
  Rule 1 is tested on the terminal-year IRR (year T) > k, and implied g = IRR_T − d is used in
  Rule 3. The yearly r_t and the IRR-to-each-year are a path diagnostic, not a per-year pass/fail:
  a weak middle year is not a failure, but it must be visible.
- **Split implied g into structural and cyclical parts** — structural = fleet additions and asset
  value/NAV change; cyclical = rate reversion — and report both, so it is visible how much of the
  return depends on the cycle turning.
- **Flag growth quality**: growth funded by share issuance, gains on asset sales, and dependence on
  the cycle turning.

## Bear / Base / Bull (BBB): this is where risk lives

Risk is **not** handled inside a single scenario (e.g., by penalizing individual weak years) — it's
handled by running the year-by-year build **three times**:

1. Build Bear, Base, and Bull versions of the 3–5 year forecast.
2. Each produces its own terminal value → its own g → its own (d+g) and PE/P-FCF ceiling.
3. Weight the three scenarios **25% / 50% / 25%** (Bear / Base / Bull). Weight the levels (FCF or
   EPS paths and terminal values), not the growth rates: a probability-weighted average of three
   growth rates is not the growth of the weighted path. Derive the weighted g (or IRR) from the
   weighted path.
4. **Report the full Bear–Base–Bull range alongside the weighted figure** — don't collapse straight
   to a single weighted number. A wide spread between scenarios is itself informative (low
   conviction / high uncertainty in the name) and shouldn't be hidden behind an average.

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
2. **The year-by-year build** for Bear, Base, and Bull, out to year 3 or 5 — show the terminal
   value driving each scenario's g, and the key assumptions behind it. State the growth metric and
   base used, and for cyclicals show the year-by-year table (D_t, V_t, r_t, cumulative IRR) and the
   structural vs cyclical split.
3. **Rule 1 check** (d+g vs k) for each scenario.
4. **Rule 3 ceiling** (PE or P/FCF < (d+g)/k²) for each scenario, plus the 25/50/25 weighted
   figure.
5. **A read against the current multiple**: is the stock's actual PE/P-FCF comfortably inside the
   ceiling, close to it, or already through it — across the Bear, Base, and weighted cases?
6. A short caveat line noting this is a margin-of-safety screen, not an intrinsic valuation.

## Standing parameters (don't ask the user to re-supply these each time)

- k = 12% baseline; hard floor of 10% — never go lower even for very safe names.
- BBB weights = 25% Bear / 50% Base / 25% Bull, unless the user specifies otherwise for a given
  name.
