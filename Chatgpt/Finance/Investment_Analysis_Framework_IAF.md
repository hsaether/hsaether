# Investment Analysis Framework (IAF)

**Owner:** Harald  
**Version:** 1.1 — consolidated reference with updated growth methodology  
**Last updated:** 2026-09-28  
**Status:** Canonical reference consolidated from the agreed IAF and subsequent growth update.  
**Intended location:** `C:\GitWork\hsaether\Chatgpt\Investment_Analysis_Framework_IAF.md`

## 1. Purpose and governance

The IAF is the stable guideline for company and equity investment analysis. It connects purchase price, shareholder distributions, sustainable growth, capital allocation, risk, and valuation in a consistent framework.

The IAF sits above sector modules such as Shipping Market BBB, Oil Market BBB, Rig Market BBB, and Forsvarsmarked. Sector modules supply market assumptions; company models translate those assumptions into company economics and shareholder returns.

**Analysis sequence:**

```text
Market assumptions
  → Company fundamentals and capital requirements
  → FCF / EPS / NAV per share
  → Dividend yield + normalized economic growth
  → Bear / Base / Bull investor IRR
  → Valuation and investment conclusion
```

Keep this file stable. Update market data, company forecasts, and sector assumptions in their own documents. Change the IAF's fundamental principles only following an explicit decision, and record each change in the change log.

This edition preserves the agreed rules and incorporates the approved growth update. Sections identified as **implementation clarifications** make the rules operational; they do not represent additional historical agreements. Examples are illustrative, not company forecasts. A saved file becomes a usable reference when supplied to or read by an analysis; saving it alone does not guarantee automatic use in every future conversation.

## 2. Core rules at a glance

| Item | IAF rule |
| --- | --- |
| Required return | Normally `k = 12%` annually. Keep the hurdle normally above 10%; any use of 10% or below requires explicit exceptional justification. |
| Fundamental return screen | `d + g > k`, equivalently `(d + g) / k > 1`. |
| Growth definition | Forward CAGR in normalized economic earning power or economic value **per share**, allowing for the capital required to produce it. |
| Growth quality | Validate growth against reinvestment requirements and incremental returns on capital. |
| P/E reference | `P/E = 1 / k` is a no-growth reference, not a universal valuation identity. |
| P/E screening hurdle | `P/E < (d + g) / k²`, used as a personal screening heuristic, not absolute fair value. |
| Forecast horizon | Normally 3–5 years. State the duration and sustainability of growth. |
| Scenario weights | Bear 25%, Base 50%, Bull 25%, unless a change is explicitly explained. |
| Scenario construction | Vary operating drivers, cash flows, investment, financing, and distributions; do not vary only exit multiples. |
| Final return check | Compare scenario investor IRRs with `k`. Use `d + g` as a transparent sanity check. |
| Cyclical businesses | Normalize earning power through the cycle; put cyclical rate changes primarily in scenarios and valuation. |
| Capital allocation | Include dividends, reinvestment, buybacks, dilution, and net debt changes without double counting. |
| Risk | Avoid penalizing the same risk mechanically in both scenario cash flows and an inflated hurdle rate. |

**Threshold provenance:** The original request specified `k > 10%`; the later fixed-module summary allowed explicitly justified exceptions. This edition retains 12% as the default and treats the lower boundary as exceptional, not a routine alternative.

## 3. Definitions and conventions

| Symbol or term | Definition |
| --- | --- |
| `P₀` | Current share price or proposed purchase price, dated and in a stated currency. |
| `Pₙ` | Estimated exit share price at the end of year `N`. |
| `Dₜ` | Cash dividend per share in year `t`. |
| `dₜ` | Forecast dividend yield on purchase price: `Dₜ / P₀`. |
| `d` | Sustainable forward dividend yield used in the quick return screen; specify its calculation. |
| `g` | Forward annualized growth in the selected normalized economic metric per share. |
| `k` | Required annual shareholder return; normally 12%. |
| `N` | Forecast horizon in years; normally 3–5. |
| `Xₜ` | The explicitly selected normalized economic metric per share at time `t`. |
| EPS | Earnings per share; EPS is already a per-share measure. |
| FCF | Free cash flow; always define maintenance, growth investment, working capital, and financing treatment. |
| FCFF / FCFE | Free cash flow to the firm / to equity; distinguish these before choosing a valuation denominator or discount rate. |
| NAV/share | Net asset value attributable to common equity divided by the relevant share count. |
| NOPAT | Net operating profit after tax, before financing effects. |
| ROIC | Return on invested capital; distinguish existing-capital returns from incremental investment returns. |
| BBB | Bear / Base / Bull scenario analysis. |

Use decimal inputs in formulas: 12% = `0.12`. Keep currency, nominal/real treatment, forecast dates, and share-count conventions consistent. State whether investor returns include taxes and transaction costs; do not silently mix conventions.

## 4. Required return and the D+G screen

At broadly stable valuation multiples, the quick fundamental return approximation is:

```text
Expected annual shareholder return ≈ d + g
IAF screen: d + g > k
Default k = 12%
```

Rerating can affect actual investor returns, but it is separate from `g`. The complete scenario cash-flow model determines whether the purchase price meets the required return.

For cyclicals, do not assume the latest dividend is sustainable. Forecast annual dividends and show `dₜ = Dₜ / P₀`. If one summary yield is needed, identify whether it is a normalized forward yield or the arithmetic average of forecast annual dividends divided by `P₀`. An average yield is a screening convention, not an IRR.

Keep `k` broadly stable across scenarios for the same company. A higher hurdle may be justified by leverage, uncertainty, or other material risks, but explain the reason. Where a bear scenario changes financing risk substantially, document any resulting change in `k` and its relationship to risks already modeled in cash flows.

## 5. Updated growth methodology

### 5.1 The definition of IAF growth

> Growth means forward growth in sustainable, normalized economic earning power or economic value per share, after allowing for the capital required to achieve it.

The four requirements are:

1. **Forward-looking:** historical growth provides evidence, not the forecast itself.
2. **Normalized:** remove temporary peak/trough effects and nonrecurring items.
3. **Per share:** incorporate dilution, buybacks, and financing effects.
4. **Economically justified:** assess whether incremental capital earns an adequate return.

Revenue, EPS, and FCF growth are evidence for estimating `g`; none is automatically its definition. Report low-return expansion even when it increases earnings, but do not describe it as value-accretive growth without supporting economics.

### 5.2 Separate three layers

| Layer | What it measures | Examples |
| --- | --- | --- |
| Business growth | Expansion in operating scale | Units, customers, vessels, capacity, available operating days. |
| Financial growth | Change in reported or forecast financial results | Revenue, EBITDA, NOPAT, EPS, FCF. |
| IAF economic growth | Change in normalized per-share economics | Sustainable cash earning power/share, normalized EPS, or normalized NAV/share. |

Every analysis should distinguish **reported/operating growth** from **IAF economic growth `g`**. They can legitimately differ in both magnitude and sign.

### 5.3 Calculate and explain `g`

```text
g = (Xₙ / X₀)^(1/N) − 1
```

State the metric, normalized starting value, ending value, horizon, share counts, and normalization assumptions. Select one primary metric and use other measures as cross-checks; do not add EPS growth, FCF growth, and NAV growth together.

**Implementation clarifications:** Use comparable economics at both endpoints. If using economic value/share, hold valuation conventions consistent so that multiple expansion or cyclical asset-price changes do not enter structural `g`. Use post-distribution company value when adding dividends separately. If the starting value is zero or negative, or the measure crosses zero, ordinary CAGR is unsuitable: show the annual path and absolute change instead.

Growth duration matters. A one-year increase of 30% does not establish a five-year growth rate of 30%, and a 3–5 year forecast rate is not a perpetual terminal growth assumption.

### 5.4 Choose a metric suited to the business

| Business type | Primary evidence for `g` | Cross-checks |
| --- | --- | --- |
| Asset-light compounder | Normalized FCF/share or EPS | Incremental returns, conversion to cash, dilution. |
| Software | Normalized FCF/share, supported by revenue and margin economics | Stock-based compensation, dilution, incremental economics. |
| Industrial | Normalized operating earning power, bridged to equity per share | ROIC, working capital, capex, financing. |
| Bank | Normalized EPS and tangible book value/share | ROE versus cost of equity, capital requirements, payout. |
| REIT | AFFO/share and NAV/share | Recurring property investment, acquisition/development returns, leverage. |
| Oil producer | Normalized FCF/share and resource value/share | Commodity assumptions, depletion, replacement investment. |
| Shipping/offshore | Normalized cash earning power/share and NAV/share | Fleet economics, asset values, net debt, capex commitments. |
| Mature dividend company | Normalized EPS or FCF/share | Payout coverage and reinvestment needs. |
| Early growth company | Revenue and unit economics as supporting evidence | Credible path to positive per-share cash generation and adequate returns. |

### 5.5 Growth quality and reinvestment

For every material growth assumption, answer: **What capital must be reinvested, when, and at what expected return?**

For operating growth attributable to new investment, a useful consistency check is:

```text
Operating earnings growth ≈ reinvestment rate × incremental return on capital
```

State the reinvestment definition and allow for investment-to-earnings delays. Efficiency improvements and changes in returns on existing assets require a separate bridge. This is a check on operating growth, not an identity for every per-share `g`. See [Damodaran: Fundamental Determinants of Growth](https://pages.stern.nyu.edu/adamodar/New_Home_Page/valquestions/growth.htm).

The agreed IAF capital-discipline screen is normally **incremental ROIC > `k`**. **Implementation clarification:** `k` is the investor's shareholder hurdle, while unlevered ROIC is conventionally assessed against the cost of capital for the business. Show both when relevant; do not assume they are identical. For banks or equity-only investment measures, compare like-for-like equity returns and equity hurdles.

## 6. Cyclical normalization

### 6.1 Separate structural change from the cycle

Build a bridge that attributes earnings changes to:

```text
Structural operating change
  + Cyclical price/rate/utilization effects
  + Capital-allocation effects
  + Financing and share-count effects
  + Nonrecurring/accounting effects
```

Use mutually exclusive components so the same effect appears only once. For shipping, structural drivers can include fleet capacity, normalized vessel days, fleet mix, and durable operating efficiencies. Rate changes primarily belong in BBB cash flows and valuation. Temporary utilization recovery also belongs to the cycle; a durable operational improvement may support structural growth.

**A recovery from trough earnings to normalized earnings is not structural growth.** Likewise, falling earnings from a cyclical peak do not automatically imply structural decline. Rerating is not growth.

### 6.2 Normalize unit economics, then apply the relevant scale

Do not blindly average historical dollar earnings when the company has materially changed size. Estimate through-cycle margins, returns, or unit economics and apply them to the current and forecast operating base. Document the cycle window and adjustments for structural changes. [Damodaran: More on Normalizing Earnings](https://pages.stern.nyu.edu/adamodar/New_Home_Page/valquestions/normearn.htm).

A shipping model can use:

```text
Normalized TCE earnings = normalized TCE/day × earning days
  − vessel operating costs
  − corporate costs
  → normalized EBITDA
  − cash interest, cash taxes, working-capital investment
  − necessary maintenance / dry-docking investment
  → normalized cash earning capacity
  − growth investment, with financing shown separately
  → equity cash-flow bridge
```

TCE is time-charter-equivalent revenue after voyage expenses; avoid subtracting voyage expenses twice. Reconcile the result to reported revenue and the company's own cash-flow definitions. Apply realistic delivery timing, disposals, off-hire, fleet age, and replacement needs.

Use normalized economics to estimate structural `g`, while modeling the actual transition from current conditions in scenario cash flows. Do not assume immediate normalization in a valuation unless that is the stated scenario. Keep normalization of earnings, reinvestment, and financing internally consistent. [Damodaran: Commodity Companies—Value Drivers](https://pages.stern.nyu.edu/adamodar/New_Home_Page/littlebook/commodityvaluedrivers.htm).

### 6.3 Illustrative CAPT-style case

A company expands its fleet while market rates fall. Reported EPS may decline even as normalized earning capacity/share rises. Conversely, unchanged capacity combined with a rate surge can produce large reported EPS growth without comparable structural `g`.

Fleet expansion contributes to per-share growth only after accounting for its purchase price, operating economics, financing, delivery timing, and dilution. The direction of fleet growth alone is insufficient.

## 7. Cash flow, maintenance, and growth investment

Separate maintenance and replacement requirements from growth investment:

```text
Total capex = maintenance / replacement capex + growth capex
```

Cash earning capacity after necessary maintenance helps assess sustainable economics. FCF after all investment shows the actual cash remaining. Show both where the distinction matters; pre-growth-investment cash flow is not all distributable if the growth forecast requires that investment.

Illustration: operating cash flow of 100 less maintenance capex of 20 gives 80 before growth investment. A further 60 of growth capex reduces residual cash to 20. The decline is not sufficient evidence of deterioration: evaluate the incremental return, timing, and financing of the 60 investment. Equally, higher FCF achieved by deferring essential investment does not establish better economics.

For shipping/offshore, give FCF/share, NAV/share, net debt, and the capex schedule greater weight than reported earnings alone. Disclose dry-docking, committed newbuild payments, and sustainable replacement needs.

**Implementation clarification:** Match the cash-flow measure to the value being assessed. FCFF belongs with enterprise value and an appropriate business discount rate; FCFE belongs with equity value and an equity return requirement. Define any quoted `FCF yield = FCF/share / P₀` as an equity-consistent measure or clearly identify the approximation.

## 8. Capital allocation and double-counting controls

| Item | Treatment |
| --- | --- |
| Dividends | Include in `d` and investor cash flows; deduct cash paid from the company's balance sheet. |
| Buybacks | Model repurchase price, cash use, and share reduction; their effect normally enters per-share `g` and terminal value. |
| Equity issuance / stock compensation | Reflect dilution and any proceeds or cash-flow adjustments consistently. |
| Debt reduction / cash retention | Reflect in net debt, interest expense, financing risk, and equity value. |
| Growth capex / acquisitions | Include cash required and subsequent earnings; assess incremental returns and financing. |
| Asset disposals | Remove sold assets and their earnings, recognize proceeds, and follow their use. |

Do not add a buyback yield to `d + g` if buybacks are already reflected in `g`. A separate dividend-plus-buyback-plus-organic-growth bridge is acceptable only when the growth component explicitly excludes repurchase effects and reconciles to the per-share model.

For an asset-based valuation:

```text
Equity NAV = gross asset value − net debt − other senior claims
NAV/share = equity NAV / relevant shares outstanding
```

At unchanged gross asset value and other claims, lower net debt increases equity NAV. **Implementation clarification:** Repaying debt with existing cash reduces debt and cash together, leaving net debt unchanged at that instant. Newly generated retained cash can reduce net debt and increase equity value. Do not count debt repayment, cash retention, and NAV growth as independent returns when they describe the same cash.

Leverage can amplify per-share outcomes without improving the underlying business. Keep financing effects visible and assess the associated risk.

## 9. Valuation screens

### 9.1 No-growth earnings reference

```text
P/E reference = 1 / k
At k = 12%: P/E reference ≈ 8.33×
```

This is a useful reference where sustainable earnings are distributable and growth is absent. It is not a universal identity; reinvestment requirements, payout, duration, and risk matter.

### 9.2 Growth-adjusted P/E heuristic

```text
IAF screening hurdle: P/E < (d + g) / k²
```

| `k` | `d` | `g` | Screening P/E ceiling |
| --- | --- | --- | --- |
| 12% | 1% | 20% | `0.21 / 0.12² = 14.58×` |
| 12% | 1% | 30% | `0.31 / 0.12² = 21.53×` |

Retain this as the user's heuristic. It does not establish intrinsic value or guarantee a return. Use a stated, appropriate earnings basis; peak-cycle earnings can make a stock look artificially cheap, and a negative or near-zero denominator makes the screen unhelpful.

**Implementation clarification:** Because `d` depends on price, hold the evaluation price explicit. Do not mechanically turn the heuristic into a price target while leaving dividend yield fixed. An analogous P/FCF screen requires a defined equity cash-flow measure and remains a heuristic.

Use the scenario model for valuation conclusions, particularly where cash flows, leverage, or investment vary substantially over time.

## 10. Bear / Base / Bull analysis

Normally model 3–5 years using Bear/Base/Bull probabilities of 25%/50%/25%. Explain departures and ensure probabilities sum to 100%.

| Required output | Bear | Base | Bull |
| --- | --- | --- | --- |
| Probability | 25% | 50% | 25% |
| Market drivers | Model | Model | Model |
| Operating capacity, volume, utilization | Model annually | Model annually | Model annually |
| Revenue, margins, EPS | Model annually | Model annually | Model annually |
| Maintenance and growth investment | Model annually | Model annually | Model annually |
| FCF/share and dividends/share | Model annually | Model annually | Model annually |
| Cash, debt, net debt, share count | Model annually | Model annually | Model annually |
| Normalized endpoint metric and `g` | Calculate | Calculate | Calculate |
| Exit valuation method and `Pₙ` | Explain | Explain | Explain |
| Investor IRR and difference from `k` | Calculate | Calculate | Calculate |

Make each scenario economically coherent. Consider rates/prices, volumes, costs, investment timing, financing, and payout constraints before applying an exit valuation. Avoid a bear case that assumes stressed cash generation but unchanged unaffordable dividends.

Show the dependence of the outcome on terminal value, refinancing, and potential dilution. Use sector BBB modules as dated inputs and identify any company-specific deviations.

## 11. Investor IRR as the final return check

For annual cash flows, solve for `r`:

```text
P₀ = Σ[t=1..N] Dₜ / (1+r)^t + Pₙ / (1+r)^N
```

Equivalently, the investor pays `−P₀` at inception, receives dividends during ownership, and receives the final dividend plus exit proceeds in year `N`. Model any additional investor contributions or distributions explicitly. Use actual payment dates where their timing materially affects returns.

Compare each scenario IRR with `k`, then evaluate the probability-weighted economics, downside, and uncertainty. Reconcile the IRR result with `d + g`: explain the contributions of changing dividends, cycle effects, rerating, financing, and timing.

**Implementation clarifications:**

- An IRR is a modeled return, not a guaranteed outcome.
- A probability-weighted average of scenario IRRs is a descriptive statistic, not generally the IRR of probability-weighted cash flows.
- If aggregating, label the method. A useful price comparison is the probability-weighted present value of scenario investor cash flows discounted at `k`.
- With nonstandard cash-flow signs, IRR may be ambiguous; use net present value at `k` as an additional check.
- Avoid subtracting net debt twice when converting enterprise/asset value to equity, or retaining dividend cash in terminal value after paying it to investors.

## 12. Standard structure for an IAF company analysis

1. **Scope and snapshot:** company/security, price and date, currency, horizon, IAF version, and `k`.
2. **Business and market assumptions:** operating drivers and relevant dated sector modules.
3. **Reported fundamentals:** results, cash-flow definitions, balance sheet, share count, and source dates.
4. **Normalization:** cycle position, recurring economics, adjustments, and chosen primary growth metric.
5. **Growth bridge:** reported/operating growth versus IAF `g`, including capital requirements and incremental returns.
6. **Capital allocation:** maintenance, growth investment, dividends, buybacks, dilution, and net debt.
7. **Valuation screens:** `d + g`, relevant earnings/FCF yields, NAV, and the P/E heuristic where applicable.
8. **BBB forecasts:** annual financial paths, probabilities, terminal valuation, and investor IRRs.
9. **Risks and sensitivities:** principal uncertainties, downside, financing constraints, and assumptions that would invalidate the conclusion.
10. **Conclusion:** whether the price offers adequate modeled return against `k`, what drives that result, and what evidence should prompt reassessment.

## 13. Quality-control checklist

- [ ] The purchase price, currency, forecast dates, and hurdle are explicit.
- [ ] Reported growth and normalized per-share `g` are shown separately.
- [ ] The normalization reflects the current and forecast scale of the business.
- [ ] Cyclical recovery, asset-price changes, and rerating are not hidden inside structural `g`.
- [ ] Growth capex, maintenance/replacement investment, working capital, and financing are funded consistently.
- [ ] Incremental returns support the claimed quality of growth.
- [ ] Buybacks, dilution, distributions, and net debt are reconciled without double counting.
- [ ] FCF definitions and valuation denominators match.
- [ ] Scenarios vary fundamentals and cash flows; probabilities sum to 100%.
- [ ] Exit value is consistent with the end-of-period assets, debt, cash, shares, and distributions.
- [ ] IRRs are compared with `k`, and any aggregation method is clearly labeled.
- [ ] The P/E rule is presented as a heuristic, not an intrinsic-value formula.
- [ ] Risk is not duplicated mechanically in both scenarios and the required return.
- [ ] Assumptions, estimates, facts, and remaining uncertainties are distinguishable.

## 14. Source record and maintenance

### Framework provenance

| Source | Role |
| --- | --- |
| [Investment Analysis Framework (IAF)](chatgpt-conversation://6aa52930-d248-83ed-8a4a-1ed5184e7a83) | Original user rules, agreed refinements, and fixed-module summary. |
| [Best Practice Growth Analysis](chatgpt-conversation://6abaa38a-5440-83ed-940e-da2e4bd38316) | Approved revision of `g`, growth-quality checks, cyclical normalization, and request for a canonical Markdown file. |

Both conversations were retrieved in full for this consolidation on 2026-09-28. Conversation links require access to the relevant ChatGPT account. The original conversations contain claims of saved memory; this document records their visible content, not an independent verification of that memory.

The external methodology links in Sections 5–6 support implementation details. They do not establish the user's personal 12% hurdle, 25/50/25 probabilities, or P/E heuristic. Editorial clarifications address formula limits, denominator consistency, financing, and double counting; they are labeled where introduced.

### Maintenance procedure

1. Keep this filename and location stable so other analysis files can reference it.
2. Record the IAF version used in each company analysis.
3. Keep live prices, company estimates, and sector outlooks outside this document.
4. For an agreed methodology change, edit the relevant section and add a dated change-log entry.
5. Use version control to inspect changes; avoid maintaining competing copies as separate sources of truth.

### Change log

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | Prior agreed framework; consolidated 2026-09-28 | Original hurdle, return screen, P/E heuristic, capital-allocation rules, 3–5 year BBB analysis, and IRR discipline. |
| 1.1 | 2026-09-28 | Incorporated approved normalized per-share growth methodology; separated operating growth from economic growth, cycle effects, and rerating; added maintainable structure, source record, and labeled implementation clarifications. |
