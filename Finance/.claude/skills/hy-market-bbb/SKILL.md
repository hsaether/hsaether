---
name: hy-market-bbb
description: Nordic HY Market BBB (HY BBB) — the Nordic high-yield bond market baseline and the method for judging Nordic high-yield funds. Produces Bear/Base/Bull paths on the IAF time grid (stub quarter(s) of the current year + 3 calendar years, now 2027–2029) for the NIBOR path, Nordic HY spreads, first-time default rates and loss given default (market and per sector, with oil service, E&P and shipping linked to the oil, rig, supply and tanker baselines), Nordic GDP, and the expected NOK total return of the market, plus mid-cycle values, a default and distress log, and named catalysts with signposts. Base is the decision case; Bear and Bull are catalyst-based stress tests; 25/50/25 is a labelled convention, never a probability. Fund mode applies the baseline to named funds (Heimdal Høyrente, Heimdal Høyrente Pluss, Sissener Corporate Bond, Fondsfinans High Yield and others) to give the expected net return, loss and liquidity risk per fund. Reads docs/oil-market-bbb.md (and the rig, supply and tanker baselines for energy issuers) and never makes its own oil, rig, OSV or tanker forecast; it is the only place a NIBOR path or Nordic GDP view is set. ALWAYS use when the user mentions HY BBB / Nordic HY / høyrente / high yield, asks to create, run or update ("oppdater modul") the HY module, or asks about Nordic or Norwegian high-yield bonds, default rates, kredittpåslag or credit spreads, NIBOR-linked bonds, bond restructurings, Stamdata or Nordic Trustee statistics, Nordic GDP, the Norges Bank rate path, or high-yield funds such as Heimdal Høyrente, Høyrente Pluss, Sissener Corporate Bond or Fondsfinans High Yield — even without naming the skill.
---

# Nordic HY Market BBB

**Revision:** 2026-10-06.8 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/hy-market-bbb/` in the Finance folder.

A Bear/Base/Bull baseline for the Nordic high-yield bond market. It answers two questions:

1. **Market:** what NOK total return should a Nordic HY investor expect, year by year, which
   default and loss rates sit behind it, and what named events would move it?
2. **Funds:** for a named Nordic HY fund, what net return can it deliver on that baseline, how
   much of its yield is compensation for losses, and how does it behave in Bear?

It is a testable hypothesis with explicit risks, not a news summary or a fund recommendation.

**Position in the chain.** It sits beside the sector BBBs and below [[oil-market-bbb]]. Energy is
the largest risk block in Nordic HY (Norwegian corporate HY at year-end 2025: Oil Service 15%,
O&G E&P 10%, Shipping 10% of NOK 499bn outstanding `[F]`, Nordic Trustee 2025 report), so energy
issuers are translated from the existing baselines, never re-forecast:

**Oil path ([[oil-market-bbb]]) → E&P cash flow; rig activity ([[rig-market-bbb]]) → drillers;
OSV market ([[supply-market-bbb]]) → OSV and subsea owners; tanker market ([[oil-shipping-bbb]]) →
tanker issuers → sector default and loss rates → market loss rate.** The non-energy part runs on
the skill's own macro block: **Nordic GDP, unemployment and the NIBOR path → refinancing cost and
cash flow of leveraged issuers → default and loss rates.** Spreads and the NIBOR path then give
carry and mark-to-market.

**Scope:** Nordic corporate HY bonds (NO, SE, DK, FI ISINs, plus XS bonds from Nordic issuers
when a fund holds them), all currencies (NOK, SEK, EUR, USD), FRN and fixed; NIBOR and the
Norges Bank policy rate path; STIBOR, EURIBOR and SOFR only as hedge-carry inputs; Nordic GDP,
unemployment and inflation as default drivers; defaults, restructurings and recoveries; Nordic HY
funds in fund mode. **Out of scope:** oil price (→ [[oil-market-bbb]]; read only); rig, OSV and
tanker markets (→ sector BBBs; read only); equity valuation of an issuer (→ [[iaf-valuation]]);
investment-grade corporates, covered bonds and government bonds except as the secondary
"IG / bank capital" row used when a fund holds them; personal tax and suitability advice.

## Standing parameters

- **Time grid = IAF grid:** stub (remaining quarters of the current year) + 3 full calendar years,
  now Q4 2026 + 2027–2029. Roll forward with the first run each January: the first year becomes
  "realised" (forecast vs actual) and a new end year is added. Rolling is not a reset.
- **Year-1 by quarter for the rate block only** (policy rate and 3M NIBOR): FRN coupons reset
  quarterly, so the quarterly path drives Year-1 carry. Spreads, defaults and returns are annual.
- **Return basis:** total return in **NOK**, foreign-currency bonds **hedged to NOK** (the hedge
  swaps the foreign base rate for NIBOR, see Return model). Nominal, calendar-year, before tax.
  Market rows are **before fees**; fund rows are **after the fund's ongoing fees**.
- **Rates in % p.a., spreads in bp, default rates in % of outstanding volume, LGD in %.**
- **Point value + range** for every scenario figure. Fund analyses use the point value; the range
  shows uncertainty inside the scenario.
- **Base = the decision case.** Bear and Bull are stress tests tied to named catalysts.
  **25/50/25** is a labelled convention for optional weighted figures — never a probability.
- **Stub has no scenario spread** (IAF rule): the same value in all three scenarios. Stub return =
  quarter-to-date actual index return + carry for the rest of the quarter at today's yield less
  the Base loss rate pro rata. Stub NIBOR = fixings to date + the Norges Bank path for the rest.
  Scenarios diverge from Year 1.
- **Yield is a promise, not an expectation.** Expected return always deducts expected credit loss
  and shows mark-to-market separately. A quoted yield is never used as an expected return.
- **Minimum change (convention):** a point value moves only if the evidence moves it by at least
  25 bp (policy rate, NIBOR annual average), 50 bp (spread), 1.0 pp (market default rate; 2.0 pp
  for a sector row), 10 pp (LGD), 0.5 pp (GDP growth) or 1.0 pp (annual expected return).
  Smaller moves are noted, not applied.
- **Staleness:** the baseline is stale after 30 days, after a Norges Bank rate decision or
  Monetary Policy Report, or when `docs/oil-market-bbb.md` (or a sector BBB used for an energy
  row) gets a newer baseline date whose downstream section flags a change. Fund analyses treat a
  stale baseline as provisional.
- **Fund decision rule: yield versus risk** (revised 2026-10-06 on user input; the conventions
  below may be changed by the user). High yield is not equity: there is no fixed required return
  like IAF's k. A fund is judged on **how much excess return it earns per unit of risk**, compared
  with the market.
  - **E (reward)** = Base expected net excess return over 3M NIBOR, window average, after fees and
    expected loss.
  - **R (risk)** = stress loss = Base 2027 return − Bear 2027 return, in pp. It captures credit
    duration, credit quality, sector tilt (oil) and spread beta in one number. Single-name
    concentration is shown separately as the single-name stress.
  - **Reward-to-risk ratio** E / R. The **market reference** is the Nordic HY index's own ratio
    after a typical fund fee of 0.6% (convention): E_mkt = market Base window excess − 0.6.
  - **Verdict:**
    - **Attractive:** E / R ≥ the market reference ratio and E ≥ 1.0 pp.
    - **Marginal:** E / R between 75% and 100% of the market reference, or E between 0.5 and
      1.0 pp.
    - **Unattractive:** E / R below 75% of the reference, or E < 0.5 pp (a money-market fund does
      as well).
  - Also report the old absolute test (NIBOR + 2.0 pp) for orientation only, whether the fund
    **preserves capital in Bear** (cumulative Bear window ≥ 0), and the worst Bear calendar year.
  - A low yield is not a fault in itself. Funds holding better-rated paper, IG or bank capital earn
    less and lose less; the ratio, not the yield, decides.
- Rows, series and definitions below are fixed. Changing one is a method change and goes in the
  change log.

## Files

- Skill: `.claude/skills/hy-market-bbb/SKILL.md` (this file only, no reference files).
- Inputs (read only): `docs/oil-market-bbb.md`; for energy rows `docs/rig-market-bbb.md`,
  `docs/supply-market-bbb.md`, `docs/oil-shipping-bbb.md`; company analyses `docs/*-analysis.md`
  for issuers already analysed (e.g. DOF: Bear balance-sheet survival); the IAF skill
  `.claude/skills/iaf-valuation/SKILL.md` for the time grid and scenario convention.
- Outputs:
  - `docs/hy-market-bbb.md` — one running market baseline. Baseline date in the H1.
  - `docs/hy-exposure.md` — company look-through across the user's funds and the Stamdata
    distress screen (Step F9).
  - `docs/hy-funds-analysis.md` — one running fund file: comparison table plus one section per
    fund. Funds are compared side by side, so they share one file.
- Git holds the history, so the previous version is read from the file before it is overwritten.
- Write with Write/Edit, then **read the file back** and check every table and number. An answer
  in the conversation alone is not delivery.

## Universe, rows and series

**Universe:** Nordic corporate HY as classified by Nordic Trustee / Stamdata / Nordic Bond Pricing
(NT report "Definitions"): official rating where it exists; for unrated bonds, a bond is HY when
its spread is above the IG threshold set from comparable rated IG bonds (± 1 year duration, same
seniority and segment, two-week average prices; reclassification needs 3 months of prices). This
is a statistical split, not a credit view. Non-Nordic issuers in the Norwegian market (48% of
Norwegian corporate HY in 2025 `[F]`) are inside the universe.

| Row | Definition | Default series | Spread / return series | Role |
|---|---|---|---|---|
| **Nordic HY — total** | Nordic corporate HY, NO/SE/DK/FI ISIN | NT first-time default rate (FTD), LTM, Nordic corporate HY | Spread: Nordic HY credit spread (anchor series below); return: NBP Nordic HY aggregated benchmark index (NOK) | Core BBB |
| **Norway HY** | NO ISIN corporate HY | NT FTD, Norwegian corporate HY | NBP Norwegian HY aggregated index; Norway HY credit spread | Core BBB |
| **Sweden HY** | SE ISIN corporate HY (real-estate heavy) | NT FTD, Swedish corporate HY | NBP Swedish HY index | Core BBB (Base + range; Bear/Bull when a fund needs it) |
| **O&G E&P** | NT sector "O&G E&P" | NT sector FTD | Sector spread from fund reports / new-issue spreads | Core BBB, linked to [[oil-market-bbb]] |
| **Oil Service** | NT sector "Oil Service": drillers, OSV, subsea, seismic, FPSO/accommodation | NT sector FTD | As above | Core BBB, linked to [[rig-market-bbb]] and [[supply-market-bbb]] |
| **Shipping** | NT sector "Shipping": tankers, dry bulk, containers, car carriers, other | NT sector FTD | As above | Core BBB; tanker part linked to [[oil-shipping-bbb]], rest judged here |
| **Real Estate** | NT sector "Real Estate" (mostly Swedish) | NT sector FTD | As above | Core BBB |
| Finance (non-bank) | Consumer lenders, debt collectors, payment and investment companies | NT sector FTD | — | Secondary |
| Industry | NT sector "Industry" | NT sector FTD | — | Secondary |
| Consumer | NT "Convenience Goods" + "Consumer Services" | NT sector FTD | — | Secondary |
| Seafood, Transportation, Telecom/IT, Utilities, Other | NT sectors | NT sector FTD | — | Secondary (Base only) |
| IG / bank capital | Nordic IG corporates, bank T2 and AT1 held by funds | — (not a default row) | Spread context only | Secondary, used only for fund mapping |

- **Core rows** get full Bear/Base/Bull for default rate, LGD and spread, with ranges and
  mid-cycle. **Secondary rows** get a Base point + range; Bear and Bull only when a fund analysis
  needs the row. Confidence is stated on each.
- Sector rows follow **Nordic Trustee's sector labels** so the default series stays on one
  definition. A fund's own sector labels are mapped to these rows in fund mode, with the mapping
  shown.
- Add a row when a fund analysis needs it and records the gap. Log it as a method change.

**Fixed series:**

| Series | Definition | Unit | Role |
|---|---|---|---|
| Policy rate | Norges Bank key policy rate (Norges Bank API `IR/B.KPRA.SD.R`) | % | Rate block anchor |
| 3M NIBOR | NIBOR 3 months, administrator Norske Finansielle Referanser (NoRe) | % | FRN base rate; carry |
| NIBOR proxy (daily) | Norges Bank 3M Treasury bill (`GOVT_GENERIC_RATES/B.3M.TBIL`) and NOWA (`SHORT_RATES/B.NOWA.ON.R`) | % | Daily check when NIBOR fixings are not at hand; never relabelled as NIBOR |
| NIBOR–policy spread | 3M NIBOR − policy rate, same date | bp | Bank funding premium; normally positive and small |
| Swap rate | NOK swap rate at the market's fixed-rate duration (press/bank data) | % | MTM of fixed-rate bonds |
| Hedge carry | Base-rate differential: 3M NIBOR − 3M SOFR / EURIBOR / STIBOR | pp | Converts foreign-currency yields to NOK hedged |
| **Credit spread (anchor)** | "Kredittpåslag Norge / Norden" as quoted monthly in the Heimdal Høyrente report (underlying index provider to be confirmed and recorded) | bp | Spread path and mark-to-market |
| New-issue spread | NT average issue spread: FRN margin; fixed = coupon − swap | bp | Pricing of new risk; per sector in the NT report |
| **Market return (annual)** | NBP Nordic HY aggregated benchmark index, NOK base (SE+NO ISIN, issue ≥ 300m, market-cap weighted, total return) | % | Forecast vs actual |
| Market return (monthly) | DNB Carnegie Nordic HY and Norwegian HY index returns as quoted in fund reports | % | Tracking between NT reports; tagged `[E]`, never mixed with NBP in one comparison |
| **FTD rate** | NT: new first-time defaults over the last four quarters ÷ total outstanding (volume), quarterly LTM | % | Default anchor |
| Global context | ICE BofA Euro HY OAS `BAMLHE00EHYIOAS`, US HY OAS `BAMLH0A0HYM2` (FRED) | % | Context only; never a Nordic series |

## Definitions and units

| Term | Definition |
|---|---|
| **Default (NT)** | "Any non-payment or change to bond terms where investors are not adequately compensated." Includes missed coupon or principal, bankruptcy, and distressed amendments (interest deferral or PIK without compensation, maturity extension, haircut, debt-to-equity conversion) |
| **First-time default (FTD)** | The first time a bond defaults; a re-default of the same bond is not counted again. FTD rate = FTD volume in the last 4 quarters ÷ total outstanding volume (NT) |
| Distressed exchange | A restructuring by bondholder vote or written resolution that leaves holders with less than the original claim in value or time. Counts as default |
| Routine amendment | A bondholder vote on a waiver, tap, security change or call that compensates holders (fee, higher coupon). Not a default; logged as a warning sign only when it relaxes a covenant to avoid a breach |
| Recovery | Value received per 100 of claim. **Market recovery** = bond price about 30 days after the default event `[A convention]`; **ultimate recovery** = value of cash, new bonds and equity received at the end of the restructuring. State which one |
| LGD | 1 − recovery (on the same basis) |
| **Expected loss (EL)** | Default rate × LGD, % of the portfolio per year |
| Credit duration | Spread duration: price sensitivity to the credit spread (≈ time to maturity or call for FRNs) |
| Rate duration | Price sensitivity to the swap rate. ≈ 0.1–0.25 years for an FRN; the fixed-rate share drives it |
| Yield after fees | Fund-reported running yield after the management fee. Check whether distressed bonds are capped (Fondsfinans caps each bond at 30%) |
| Running spread | Yield − base rate of the same currency; for a fund, implied as (yield after fee + fee) − 3M NIBOR on NOK-hedged portfolios |
| Distress ratio | Share of outstanding volume priced below 80 or above 1,000 bp spread. Leading indicator of defaults |
| Maturity wall | HY volume maturing per year in the window (NT/Stamdata) |
| Watchlist | Bonds with an ongoing non-routine bondholder vote, a standstill, a missed payment grace period, a price below 80, or a maturity inside 12 months without announced refinancing |

**Rating → one-year default probability** (long-run global corporate averages, approximate, S&P
Global annual default studies `[E]`; confirm the exact values when the study is read). Used for
fund quality (Step F4). Applied to manager-internal ratings with that caveat.

| Rating | A or better / deposits | BBB | BB+ | BB | BB− | B+ | B | B− | CCC/C | Equity |
|---|---|---|---|---|---|---|---|---|---|---|
| PD % p.a. | 0.05 | 0.15 | 0.3 | 0.5 | 0.9 | 1.9 | 3.0 | 5.5 | 26 | n/a (price risk) |

- **Default rates are volume-weighted** (NT basis). An issuer-count rate is a cross-check and is
  labelled as such.
- **FTD, not total defaults, drives EL.** A re-default hits bonds already marked down; counting it
  again would double count the loss.
- Never mix rates from different bases in one comparison: NBP vs DNB Carnegie index returns, NT
  FTD vs a bank's issuer-count default rate, BofA OAS vs Nordic FRN margins.

## Return model

Per row (or fund), scenario s and year t, all in NOK hedged:

```
B_t     = average 3M NIBOR in year t (scenario rate path)
S_t     = average running spread in year t (start-of-year spread, moved with the scenario path)
Carry_t = B_t + S_t                                   (− fees for a fund)
EL_t    = DR_t × LGD_t                                (FTD rate × loss given default)
MTM_t   = − D_credit × (S_end − S_start) − D_rate × (swap_end − swap_start)
R_t     = Carry_t − EL_t + MTM_t                      expected total return, NOK
Excess_t = R_t − B_t                                  return above money market
```

- **Hedging:** a USD bond hedged to NOK earns its USD yield + (NIBOR − SOFR) over the hedge
  period; EUR and SEK likewise with EURIBOR and STIBOR. A fund that reports a NOK yield has done
  this conversion; check that it has.
- **FRN vs fixed:** FRN carry follows the NIBOR path; fixed-rate carry is locked until maturity
  and carries swap MTM. Use the fixed-rate share or the reported rate duration — never assume an
  all-FRN portfolio.
- **Spread MTM is mostly a timing effect.** A spread widening in Bear Year 1 is earned back as
  higher carry and pull-to-par later, unless it is realised through a default. Show MTM per year
  so the path is visible; the 3-year total nets most of it out.
- **Calls and pull-to-par:** Nordic HY bonds are mostly callable at a premium. Yield-to-maturity
  overstates carry on bonds trading above the call price; use yield-to-worst where the source
  gives it, and say which yield a figure is.
- **Distressed bonds:** a bond trading at 50 shows a yield of 30%+; most of that is expected loss.
  Either the source caps it (state the cap) or the fund analysis removes it and prices the bond on
  its recovery case. Never put an uncapped distressed yield into carry and a market EL on top
  without stating the overlap.
- **Mid-cycle return** = neutral NIBOR + normal spread − normal EL, with no MTM.
- The formula is linear: convexity, reinvestment timing, swing pricing and transaction costs are
  ignored and named as such.

## Data sources

Primary data beats commentary. Every figure states source, definition, unit and both observation
and publication date. If a connector or page fails, say so and use the next source. Never fill a
gap with an invented number.

| Need | First choice | Fallback / cross-check |
|---|---|---|
| Brent path, long end, mid-cycle, disruptions | **`docs/oil-market-bbb.md`** | — never a connector or own estimate |
| Rig, OSV and tanker market paths for energy issuers | **`docs/rig-market-bbb.md`, `docs/supply-market-bbb.md`, `docs/oil-shipping-bbb.md`** | — never an own sector forecast |
| Market size, sector shares, issuance, FTD rates (total, Energy, sector), issue spreads, index returns, covenant mix, definitions | **Nordic Trustee "Nordic Corporate Bond Market Report"** (annual, published ~February; 2025 edition: `nordictrustee.com/app/uploads/2026/02/Nordic-Corporate-Bond-Market-Report-2025.pdf`) | Ocorian knowledge hub (Nordic Trustee is an Ocorian company; older reports have moved to `ocorian.com`) |
| Bond master data, outstanding volumes, notices, defaults, bondholder meetings, written resolutions | **Stamdata** (`stamdata.com`: News with tags, Statistics, Calendar) — one bond or issuer at a time in the in-app browser | Nordic Trustee "Ongoing" page (initiated voting procedures, notices) |
| Issuer announcements: results, refinancing, bondholder meetings, standstills | **Nordic Financial** `search_filings` with `source="newsweb"` + `ticker` + `fiscal_year` (Oslo-listed issuers and Nordic ABM bonds) | FinancialFilings `filings_list`; issuer IR; Swedish issuers via MFN / Cision |
| Issuer financials (leverage, liquidity, maturities) for watchlist names | **Nordic Financial** `company_research` / `parse_pdf_to_text` on the IR PDF | FinancialFilings `companies_financials_retrieve` |
| Policy rate, NOWA, T-bill and government yields | **Norges Bank API** `https://data.norges-bank.no/api/data/<flow>/<key>?format=csv&lastNObservations=N&locale=en` (`IR/B.KPRA.SD.R`, `SHORT_RATES/B.NOWA.ON.R`, `GOVT_GENERIC_RATES/B.3M.TBIL`, `B.10Y.GBON`) | FRED `IR3TIB01NOM156N` (3M interbank, OECD monthly), `IRLTLT01NOM156N` |
| Policy rate path (Base anchor), Norwegian macro projections, neutral rate | **Norges Bank Monetary Policy Report** (March, June, September, December) and rate decisions | Norges Bank Expectations Survey; Regional Network |
| 3M NIBOR fixings | NoRe (administrator; check the publication delay) | Bank rate pages, press; FRED `IR3TIB01NOM156N` (monthly, lagged) |
| STIBOR, EURIBOR, SOFR (hedge carry) | Riksbank / SFBF (STIBOR), EMMI (EURIBOR), FRED `SOFR` | AllRatesToday `get_official_rates` for central-bank tables |
| Swedish, Danish, Finnish policy rates and projections | Riksbank MPR, Danmarks Nationalbank, ECB (Finland) | FRED |
| Norway GDP (mainland and total), unemployment, bankruptcies | **SSB API** `https://data.ssb.no/api/v0/no/table/09190` (quarterly national accounts) and `09189` (annual); SSB bankruptcy statistics | FRED Eurostat series `CLVMNACSCAB1GQNO` (total GDP, chained euros) |
| Sweden, Denmark, Finland GDP | Statistics Sweden (SCB), Statistics Denmark, Statistics Finland | FRED Eurostat series (`CLVMNACSCAB1GQSE`, `…DK`, `…FI` — check the id with `fred-search-series`) |
| GDP forecasts (Base anchor `[E]`) | Norges Bank MPR, SSB forecasts, Riksbank, Finance ministries' budgets | IMF WEO (April, October), OECD Economic Outlook (June, December), European Commission (spring, autumn) |
| Monthly index returns, spreads, market colour, fund metrics | **Fund monthly reports**: Heimdal (`heimdalfondene.no` → Markedsrapporter), Fondsfinans (`fondsfinans.no/nyheter/rapporter/`, monthly "Markedsrapport", HY pages near the end), Sissener (`sissener.no` → monthly reports) | Morningstar factsheets; Nordnet; Finansportalen (fees) |
| **Full fund holdings** (weights; prices where available) | **Fondsfinans:** `fondsfinans.fundlist.com/details/holdings/<ISIN>`; the page embeds Morningstar data in `__NEXT_DATA__` (each holding's weight, market value in NOK, nominal, currency, maturity; credit-quality breakdown; calendar-year returns since 2016). **Heimdal:** `heimdalfondene.no/fondsportefolje-heimdal-hoyrente/` and `/fondsportefolje-heimdal-hoyrente-pluss-2/` (HTML table of all holdings with weights, no prices) | Top 10 in monthly reports; annual reports (full holdings, semi-annual) |
| **Sissener holdings** | **Annual / semi-annual report** of Sissener SICAV (`irp.cdn-website.com/411e317f/files/uploaded/Sissener+SICAV_Annual+Report_<date>…pdf`): full statement of investments (nominal, cost, market value, % of NAV) and industrial and geographical classification. Use `pdftotext -raw` on the statement pages; `-layout` scrambles the columns. **Nordnet** fund page ("Største eierandeler" via "Se alle"): top ~25 holdings at month-end (Morningstar), read in the in-app browser | Monthly report (top 10) |
| Fund rules: mandate, limits, fees, liquidity terms, share classes | **Prospectus, vedtekter and PRIIPs KID** from the manager's site | Finanstilsynet register; annual and half-year reports (holdings) |
| Global HY context | **FRED** `BAMLHE00EHYIOAS`, `BAMLH0A0HYM2`, `BAMLH0A3HYC` (CCC) | Moody's / S&P default outlooks via press `[E]` |
| FX for hedge and conversion | **Yahoo** spot; **AllRatesToday** `get_rates_authenticated` with `time` | — |
| Research and press | DNB Carnegie, Pareto, Arctic, SEB credit research via press; Finansavisen, DN, E24, HedgeNordic | `[E]`, grade C, never sole evidence for a default rate |
| Recovery history | Own default log (Procedure Step 5); NHH studies of Norwegian HY recoveries (e.g. 112 defaulted bonds; market-based recoveries on 78 Nordic defaults 2014–2016) | Manager commentary on restructurings `[E]` |

Quirks (observed in the 2026-10-05 build):

- **Nordic Trustee report PDF:** downloads with `curl -sL -A "Mozilla/5.0"`; WebFetch does not
  read it. Each PDF page holds two printed pages. `pdftotext -layout` mixes the two columns; plain
  `pdftotext -f N -l N` (no flag) gives clean text per spread. Charts come out as number lists
  with labels in a separate order: map values to labels from the legend before using them. FTD
  by sector: "Defaults vs. issue spreads" lists sector, FTD rate, average issue spread and volume
  share in that order. Definitions are on the last spread. `pdfinfo` and `pdftoppm` are not
  installed.
- **Stamdata public access** (tested 2026-10-06):
  - the news feed and notice PDFs work;
  - **Nordic Bond Pricing prices** on `/issues/<ISIN>/prices` are licensed (table empty without a
    login);
  - `/issues/<ISIN>/documents` and `/issuers/<id>/news` come back empty when logged out;
  - `/prices/trade-reporting` (Swedish SSMA trade reports) showed no trades for the HY bonds
    tested.
  - So prices come from fund holdings (Fondsfinans/Morningstar), annual reports and press.
- **Stamdata** is a JavaScript app; `curl` gets only the shell. Public content is free for
  non-systematic, non-commercial use; **scraping or systematic download is prohibited**. Read one
  issuer, bond or news filter at a time in the in-app browser and cite what was read. Never bulk-
  download.
- **Nordic Trustee "Ongoing"** (voting procedures, bondholder notices) loads through an API:
  `curl` shows "API error". Use the in-app browser.
- **Norges Bank API** works without a key (tested 2026-10-05: policy rate 4.50 on 2026-10-02,
  NOWA 4.50, 3M T-bill 4.46, 10Y 4.59). **NIBOR is not in the API.**
- **Norges Bank MPR dataset** (first run 2026-10-05): the meeting page
  (`norges-bank.no/en/topics/monetary-policy/Monetary-policy-meetings/<year>/<month>-<year>/`)
  links `data-mpr-<n>-<yy>.xlsx`. Sheet **Data A** = quarterly policy-rate path (current and
  previous MPR); sheet **Data E** = quarterly **3-month money-market rate (the NIBOR path)** and
  the money-market premium. Read with `py` + `openpyxl` (installed 2026-10-05). The MPR PDF's
  Tabell 3 gives annual macro projections; use plain `pdftotext -f N -l N` (the `-layout` mode
  shifts the row labels).
- **Riksbank MPR PDF** (`riksbank.se/.../penningpolitisk-rapport-<month>-<year>.pdf`):
  `pdftotext -layout` reads Tabell 2 (GDP, unemployment), Tabell 4 (policy path) and Tabell 10
  cleanly. The decision page also links the xlsx data ("Sifferunderlag").
- **Stamdata news** shows about one week per page of 25 (544 pages in Oct 2026). Read the most
  recent pages and filter rows on distress words (default, deferral, standstill, written
  procedure/resolution, waiver, bankruptcy) in the in-app browser. Individual notice PDFs at
  `stamdata.com/news/api/pdf/<id>` download with `curl` and parse with `pdftotext`. Decline
  optional cookies.
- **Nordic Trustee FTD on two bases:** the quarterly LTM chart (Nordic 2.6% at Q4-25) and the
  annual sector table on average outstanding (Nordic 2.9% for 2025). The LTM chart is the anchor;
  sector rates stay on the table basis. The Nordic sector table omits Oil Service and Shipping;
  the Norwegian table has Oil Service and Finance.
- **cbonds** (NIBOR, NOK swap pages) returns 403. FRED `IR3TIB01EZM156N` (euro 3M) stopped in Jan
  2026; use EMMI or the ECB for EURIBOR.
- **SSB API** v0 answers on table metadata (`09190`, `09189`); query with a JSON POST for values.
- **FRED ICE BofA series** keep only 3 years of history since April 2026. Use them for the current
  level and recent trend, not for long-run averages.
- **Fund report metrics are not comparable as printed.** Check per fund: yield before or after
  fee; YTM or yield-to-worst; distressed cap (Fondsfinans: 30% per bond); share-class currency
  (Sissener quotes class-currency yields, e.g. SEK).
  - **Multi-currency funds may quote a local-currency yield blend:** USD, EUR and SEK bonds at
    their own base rates (SOFR, EURIBOR, STIBOR), not NOK-hedged. Sissener, Aug 2026: yield
    7.3% but credit spread ~340 bp.
  - In that case carry = NIBOR + the manager's credit spread × the invested share, not yield −
    NIBOR. The wrong basis understated Sissener's carry by ~0.4 pp a year in the first run.
  - Also check whether cash and short bonds count as cash (Fondsfinans: bonds < 92 days are
    "cash").
- **Heimdal report file names are irregular and not all are linked from the fund pages.** For
  example, Høyrente Pluss Aug/Sep 2026 are `wp-content/uploads/2026/09/Manedsrapport-august-10.pdf`
  and `.../2026/10/Manedsrapport-september-20.pdf`; Høyrente Sep 2026 is
  `Heimdal-Hoyrente-September-2026-3.pdf`. Do not conclude a report is missing because a guessed
  URL returns 404. Check the uploads folder for the publication month, the news page, or ask the
  user for the link.
- **Fund yields can include distressed bonds.** A fund yield that rises while the market spread
  falls (Høyrente Pluss: 8.19% → 9.4% from Jul to Sep 2026 as the market tightened 30 bp) signals
  distressed holdings. Strip the estimated distressed part from carry and show the full-yield case
  as an upside sensitivity.
- **The quoted Nordic spread is not a clean MTM series.** In 2025 the Heimdal-quoted Nordic spread
  widened from 4.2% to ~4.85%, yet the DNB Carnegie Nordic HY index returned +8.4%. Composition
  (record non-Nordic issuance) and the DNB Markets → DNB Carnegie change in Jan 2025 move the
  number.
  - Use spread changes for scenario MTM (forward), but calibrate funds on index returns (relative
    method).
  - Year-end anchor values: 2023 6.1% (Norway 5.6%), 2024 4.2% (4.3%), 2025 ~4.85% (~5.2%).
- **Heimdal yield rule:** Heimdal uses the **coupon rate instead of YTM for bonds priced below 70**
  if the issuer pays its coupon (report footnote). Its yields therefore understate distressed
  YTM. A non-paying distressed bond may still be at YTM `[?]`.
- **Holdings pages (first read 2026-10-06):**
  - **fundlist (Fondsfinans):** Morningstar lists ~99 lines = ~78% of NAV (cash and the smallest
    positions are left out). **Price** = market value (NOK) ÷ (nominal × FX at the portfolio
    date) × 100. That price includes accrued interest; use AllRatesToday `time` for the FX.
    Fondsfinans 31 Aug 2026: only Hofseth (77) below 80; 3.6% of NAV below 90.
  - **Heimdal:** a plain HTML table with names and weights (no prices); updated around month-end.
    Group lines by issuer (several ISINs per issuer) and by type: boligkreditt = covered bonds,
    "Kontanter" = cash, "Valutaterminer" = FX forwards.
- **Prospectus beats factsheet:** the Fondsfinans HY web page states rate duration 0–5 years and
  credit duration ≤ 5, while the Morningstar factsheet states ≤ 4 and 0–2 (2026-09). Record the
  conflict and use the prospectus/vedtekter.
- **Mandate changes break track records:** Heimdal Høyrente changed from mainly Norwegian to
  mainly Nordic (up to 25% outside the Nordics) on 2025-11-28. Returns before such a date are a
  different product.
- **Press telegrams** (Placera, MFN) on fund months can carry the wrong year in search snippets;
  check the date in the article itself.
- Paid databases (Bloomberg, Stamdata licence, NBP index data, DNB Carnegie index history) are not
  available. Monthly spread and index history is built from fund reports, so keep one source per
  series and record its first observation.

## Data discipline

- Tag every number: `[F]` reported fact · `[E]` external forecast or secondary claim · `[A]` own
  assumption · `[?]` unknown. Missing news of defaults is not evidence of no defaults: Nordic
  restructurings often run as written resolutions with little press.
- For each finding: (1) the fact, (2) what it means for loss (volume affected, likely recovery,
  sector), (3) whether it changes the model. One default does not move the market rate unless it
  is large relative to the market; a cluster in one sector moves that sector row.
- **One series = one source.** If a source changes, document it and show both values for one
  overlapping date.
- **Never double count:** a bond defaults once in the FTD rate; a distressed yield and an EL
  allowance for the same bond are not both added; a fund's sector exposure is mapped to one row
  each; an energy issuer's stress comes from its sector BBB, not also from the macro block.
- **Managers talk their book.** Fund commentary on "attractive yields" and "limited default
  risk" is `[E]`; Base comes from the default log, the watchlist, the sector baselines and macro.
- **Sample size:** the Nordic market is small; one large issuer moves a sector FTD rate by
  several points. Report the volume and number of defaults behind every sector rate, and give
  rows with fewer than 3 defaults over 3 years a range and "low confidence".
- Known weak data: recovery rates (few published outcomes), sector spreads (no public series),
  monthly default counts between NT reports (own log only), unrated credit quality (fund-internal
  ratings), fund holdings beyond the top 10.
- **User input is input, not a reference.** Links, numbers and drafts are assessed critically
  (what it measures, how fresh, which definition); use what holds, reject the rest, and note the
  assessment in the source appendix.

## Scenarios

There is no statistical distribution behind defaults waves, oil shocks or rate cycles, so Bear and
Bull are not percentiles.

- **Base:** the most likely path and the decision case for fund analyses.
- **Bear / Bull:** the worst and best reasonably foreseeable paths for Nordic HY returns, each
  tied to **named catalysts** with mechanism, earliest timing and **signposts**.
- **Three drivers, not one.** Each scenario states its **rate path**, its **macro path** (GDP,
  unemployment) and the **[[oil-market-bbb]] scenario** it uses, plus the sector BBB scenarios for
  the energy rows. The mapping is not one-to-one:
  - **Higher NIBOR is not simply Bear.** For an FRN market, higher NIBOR raises carry; it hurts
    through refinancing cost, interest cover and real estate values. Bear is the combination that
    lowers return most, after the carry gain.
  - **High oil is not good for all of HY.** An oil price spike helps E&P and oil service but feeds
    inflation and rates, hitting real estate, consumer and leveraged industry. An oil collapse
    reverses it. Test both directions against the sector weights.
  - **Lags:** defaults follow stress by 2–6 quarters (liquidity runs out, maturities arrive).
    Year 1 is mostly set by the watchlist and the maturity wall; later years by macro, oil and
    refinancing conditions.
  - **Spreads lead, defaults lag.** Spreads widen first (MTM in the shock year), defaults peak a
    year or more later, and the carry earned on wider spreads repays much of the MTM. Show this
    sequence in Bear.
- Consider for each tail a **rates/macro** catalyst (Norges Bank higher for longer or cuts, Nordic
  recession, Swedish property stress), an **energy** catalyst (oil collapse or spike from the oil
  baseline; offshore cycle from the rig and supply baselines) and a **market** catalyst (fund
  outflows, closed new-issue window, global HY repricing). Choose the combination with the most
  relevant stress for return and say why.
- **Historical analogues** for calibration (state the numbers when used): the 2015–2017 oil
  service default wave, the 2020 COVID shock (spreads spiked, defaults limited), the 2022 rate
  shock, the 2023–2024 Swedish real estate stress.
- If a scenario needs an oil, rig, OSV or tanker path the input baselines do not have, flag it for
  the relevant skill — never invent one here.

## Procedure — market baseline

Two modes, one procedure:

- **Initiate** — "create HY BBB", "new HY baseline", or automatically when `docs/hy-market-bbb.md`
  does not exist. Full research on every step; status "Initial baseline"; no change log values.
- **Update** — "update HY BBB", "oppdater modul" in an HY context, or a recalibration trigger.
  Run every step in order; it is not a menu.

> Updating does not mean "summarise the latest bond news". It means new, thorough research that
> tests whether the current baseline is still right. Start from the last baseline but do not
> anchor on it: every run actively tries to falsify Base. If the evidence is not strong enough to
> change the model, say so explicitly: **HY Market BBB kept unchanged.**

**Step 0 — Setup.** State the revision of this skill and of [[iaf-valuation]]. Note analysis date
(Europe/Oslo), information cut-off, previous baseline date and days since. Roll the window if this
is the first run in a new year. Read the previous `docs/hy-market-bbb.md` and record its point
values, catalysts, signposts, watchlist and open checkpoints — they become the "previous" column
in the change log, and every open checkpoint is closed or carried with a new status.

**Step 1 — Upstream input.** Read `docs/oil-market-bbb.md` and, for the energy rows,
`docs/rig-market-bbb.md`, `docs/supply-market-bbb.md` and `docs/oil-shipping-bbb.md`: baseline
dates, status, "stale after" dates, Interface tables, scenario definitions. If one is stale or older
than the latest material event, say so, mark this baseline **Provisional**, and get it updated
first when the HY conclusion depends on it. Translate, do not re-analyse:

| Input | HY effect |
|---|---|
| Brent path per scenario and mid-cycle vs E&P breakevens, hedge books and reserve-based lending limits | E&P cash flow, borrowing base, default rate |
| Rig dayrates, utilization and contract cover | Driller EBITDA, refinancing ability, default rate |
| OSV and subsea rates, utilization, vessel values | OSV owner cash flow, asset cover (recovery), default rate |
| Tanker TCE and asset values | Tanker issuer cash flow and asset cover |
| Disruptions (e.g. Hormuz) | Inflation and rate channel (non-energy rows) as well as the energy rows |

**Step 2 — Rates block.** Policy rate and 3M NIBOR now (dated); the latest Norges Bank decision,
MPR path and its date; NIBOR–policy spread; NOK swap rates at the market's fixed-rate duration;
STIBOR, EURIBOR and SOFR for hedge carry. Base path = Norges Bank's published path `[E]`, adjusted
only with a stated reason (newer data, market pricing that clearly differs). Bear and Bull rate
paths follow the scenario catalysts. Year-1 by quarter for policy rate and NIBOR; annual averages
for the rest of the window; neutral nominal rate for mid-cycle (Norges Bank's estimate + 2%
inflation target; state it).

**Step 3 — Macro block.** Norway mainland GDP growth, Norwegian unemployment (NAV registered and
LFS), CPI-ATE, bankruptcies; Sweden, Denmark, Finland GDP and unemployment; house prices and
commercial property values (Sweden for real estate). Latest actuals with dates, then forecasts from
Norges Bank, SSB, Riksbank, IMF, OECD, EU Commission `[E]` with report dates. Base GDP path = the
central institutional view, stated; Bear/Bull from the catalysts. This block is the workspace's
only Nordic macro view: other skills read it here.

**Step 4 — Market observation.** Latest complete month as anchor:
- Spread (anchor series), new-issue spreads by sector (NT), global HY OAS for context; spread
  percentile against its own history (state the window).
- Index returns: month, YTD, last 12 months (one series per comparison).
- Primary market: new issue volume (month, YTD vs last year), taps, share of sole-led deals,
  covenant mix; whether weaker issuers can refinance.
- Maturity wall: HY volume maturing in the stub and each window year, by sector where available.
- Fund flows where published (VFF statistics) — outflows force selling in a thin market.

**Step 5 — Default and distress log.** Update the log (appendix) from Stamdata news, Nordic
Trustee notices and voting procedures, Newsweb and press since the last baseline. For each event:
issuer, ISIN(s), sector row, country, currency, outstanding (NOK equivalent at the event-date
FX), event type (missed payment, bankruptcy, distressed amendment, distressed exchange,
standstill), date, **FTD under the NT definition yes/no**, price before and ~30 days after,
restructuring outcome and recovery when known, source, and which tracked funds hold it. Then:
- **Running FTD rate** for the current year: logged FTD volume ÷ outstanding (latest NT figure,
  adjusted for net issuance), labelled "NT-definition replica `[A]`" until NT publishes the
  official figure; reconcile with NT when it does and log the gap.
- **Watchlist** with volume per bucket: (a) non-routine vote or standstill ongoing, (b) price < 60,
  (c) price 60–80, (d) maturity < 12 months without refinancing. Distress ratio where data allows.
- Recoveries realised in the log so far (market and ultimate), per sector, with n.

**Step 6 — Default rates per row.** Per core row, scenario and year:
- **Year 1:** watchlist volume × conversion probability per bucket + a background rate on the rest.
  Conversion probabilities are `[A]` conventions (start: (a) 50%, (b) 50%, (c) 20%, (d) 30%) and
  are recalibrated from the log as outcomes arrive; record each recalibration.
- **Years 2–3:** background rate driven by the macro path (non-energy rows), the sector BBB paths
  (energy rows: compare scenario cash flow with debt service and maturities of the sector's main
  issuers) and refinancing conditions (spread level, new-issue window).
- **Market rate** = Σ sector rate × sector volume share (NT shares, stated year), reconciled with
  the bottom-up total; explain any gap.
- Cross-check with history: NT FTD history (2025: Nordic 2.6% at year-end, Energy 3.0%, Real
  Estate 2.2% `[F]`), the cohort evidence (around 12% of 2015–2022 Nordic HY bonds ended in hard
  default over their life; about 40% of defaults came 1.5–2.5 years after issue; sole-led deals
  ~35% of volume but ~55% of hard defaults — seen in search summaries 2026-10-05, attributed to
  DNB credit research "Uncovering the dark side of high-yield vintages"; the page did not load, so
  confirm the source before relying on it `[E]`), and the analogues in Scenarios.

**Step 7 — Recovery and LGD.** Per core row and scenario: LGD from the log, the NHH studies and
asset cover (sector BBB asset values for energy issuers: vessel and rig values at the scenario's
mid-cycle marks; property values for real estate). Secured asset-backed bonds and unsecured holdco
bonds differ; state the mix assumed. Bear LGD is higher (asset values fall when defaults cluster).

**Step 8 — Spread path.** Per scenario: start spread, annual averages and year-end levels, set
from the default and loss outlook (spread ≥ EL + a liquidity and risk premium), the rate and
macro path, primary-market conditions and the global HY context. State the implied risk premium
(spread − EL) per year and compare it with its own history; a path where the premium goes to zero
or turns very high must be explained.

**Step 9 — Returns.** Apply the Return model per core row and scenario: carry, EL, MTM, total and
excess return for the stub, each year, the window (geometric) and mid-cycle, as point + range.
Duration inputs: credit and rate duration of the index (from fund reports or NT tenor data) `[A]`
where not published. Show the return decomposition table.

**Step 10 — Test BBB.**
- **Base:** what would have to be true for Base to be wrong, and do we see it? Search actively for
  exactly that (pre-mortem): defaults in the log above the Base pace, spreads moving against the
  path, a sector baseline turning.
- **Bear / Bull:** are the catalysts still the right ones? Has one come closer, been triggered, or
  become irrelevant? Has a signpost been crossed? Is a catalyst missing?
- **Forecast vs actual:** compare the realised index return, FTD rate and spread for elapsed
  periods with the previous baseline, and decompose the miss (carry, loss, MTM).
- **Evidence threshold:** change a scenario, catalyst or path only when several independent data
  points point the same way, or one event materially changes defaults, rates or spreads — and only
  by more than the minimum change.

**Step 11 — Mid-cycle.** Set separately from the annual path: neutral NIBOR, normal spread (long-
run average of the anchor series; state the years, with and without 2016 and 2020), normal FTD
rate (cycle average from NT history and the cohort evidence), normal LGD, and the resulting
normal return and excess return. A recent calm year does not establish a normal level.

**Step 12 — Write, log and check.** Write the document in the output format, with a complete
change log (new / unchanged / changed with previous → new value, reason and source; forecast vs
actual; weights kept or changed; whether fund analyses should update). Read it back and run the
checks below.

## Procedure — fund mode

Run when the user asks about a named HY fund, after (or together with) the market baseline. The
baseline must be current or the fund analysis is **Provisional**. Default fund set: **Heimdal
Høyrente, Heimdal Høyrente Pluss, Sissener Corporate Bond, Fondsfinans High Yield**; add others on
request. Write to `docs/hy-funds-analysis.md`.

**Share classes (the user's classes; use these unless told otherwise):**

| Fund | Class | ISIN | Ongoing fee | Note |
|---|---|---|---|---|
| Heimdal Høyrente | N | NO0012948878 | 0.70% | A: 0.85% |
| Heimdal Høyrente Pluss | B | NO0013580654 | 0.70% | A: 0.85%. Minimum NOK 50m direct, or NOK 100 via distributors without retrocession |
| Fondsfinans High Yield | B | NO0013168773 | 0.41% | A: 0.45% + 0.5% entry and 0.5% exit charge (Morningstar). B minimum NOK 100m direct |
| Sissener Corporate Bond | NOK-R | LU1923202326 | TER 0.41% + 20% above 3M NIBOR + 1% (high-water mark) | NOK-RF: 1.00% flat |

- Monthly reports quote **class A** yields after the A fee. **Class yield = A yield + (A fee − class
  fee).** Track-record gaps need no adjustment (the fee is in both the yield and the return).
- Fees from the PRIIPs KID (Heimdal: `heimdalfondene.no/wp-content/uploads/.../<date>-Priips-<fund>-<class>.pdf`),
  or Morningstar `OngoingCharge` on fundlist (Fondsfinans).

**Step F0 — Setup.** State this skill's revision and the HY baseline date used. Read the previous
`docs/hy-funds-analysis.md` and record the previous figures per fund.

**Step F1 — Fund facts** (from prospectus, vedtekter, KID; factsheets only as cross-check):
legal form (UCITS, national fund/AIF), domicile, share class used and its currency and hedging,
fees (management, performance fee with hurdle and high-water mark, entry/exit, swing pricing),
mandate (geography, rating floor, duration limits, issuer and concentration limits, equity and IG/
AT1 limits, leverage), liquidity terms (dealing frequency, notice, gates, suspension rules), size,
manager, inception, and mandate changes with dates.

**Step F2 — Portfolio snapshot** (latest monthly report, dated): yield after fee (and its basis:
YTM or YTW, distressed cap), rate duration, credit duration, time to maturity, cash, number of
bonds and issuers, **rating mix** (official or manager-internal — say which; use it whenever it is
published, e.g. Fondsfinans shows the split from CCC upwards), sector weights, top 10 and their
weights, currency and hedging, equity from restructurings.
- **Read cash in context, never as a fault by default:**
  - A **notice-period fund** (e.g. Høyrente Pluss: monthly dealing, one month's notice) knows its
    redemptions in advance, so it does not need a cash buffer. Near-zero cash is design, not risk.
  - A **daily-dealing UCITS** that holds its buffer in **covered bonds or short IG** (e.g. Heimdal
    Høyrente: ~11% boligkreditt) keeps a standing **liquidity buffer**. It earns about NIBOR, is
    not redeployed in the model, and dilutes carry permanently. Only cash clearly above the
    fund's usual buffer is dry powder.
  - A **daily-dealing UCITS** holding cash well above its liquidity needs (~5%) has usually
    **chosen** to wait for better entry points: dry powder (e.g. Sissener "a lot of dry powder",
    Fondsfinans 17% cash and short bonds). Model it as dry powder (Step F5), not as permanent
    dilution.

**Step F3 — Map to market rows.** Map every reported sector to one market row (table with the
fund's label → row → weight). IG and AT1 go to the "IG / bank capital" row, cash to NIBOR.
Compute the fund's oil exposure (E&P + Oil Service + oil shipping) and compare with the market.

**Step F4 — Fund-specific loss rate.** Start from the mapped market rows' DR and LGD per scenario,
then adjust for quality, manager style and concentration with stated reasons:
- **Quality:**
  - **Rating split published** (preferred): q = PD_fund ÷ PD_sector-mapped, both at mid-cycle.
    PD_fund = Σ rating weight × the one-year PD in the rating table (Definitions); PD_sector-mapped
    = Σ sector weight × the mid-cycle sector FTD.
  - **No rating split:** q = HY-sleeve spread ÷ market spread, where the HY sleeve excludes cash,
    IG and bank capital `[A]`.
  - **A yield below "NIBOR + market spread" is expected** when a fund holds better-rated paper. It
    is a quality signal and is scored through q and R, never as underperformance.
- **Manager style** (record it per fund with evidence; it changes LGD, distressed carry and
  horizon):
  - **Avoider** (e.g. Sissener: sells or avoids names heading for restructuring):
    - lower DR (q) and lower carry;
    - losses taken at the market price on exit (LGD on market recovery, often early and smaller);
    - no workout upside; shorter effective horizon.
  - **Workout / active** (e.g. Heimdal: stays in, or buys into, restructurings where the yield
    pays, as in DOF 2022–23, where converting bondholders got ~53% of the equity):
    - higher carry, including distressed yield;
    - LGD on ultimate recovery, which can beat the market price at default (new money, equity
      upside);
    - a longer horizon, which needs a liquidity structure that supports it (notice periods,
      AIF).
- **Use full holdings when published** (they beat the manager's sector chart):
  - map each issuer to a row;
  - aggregate by issuer for concentration (top-10 issuers, not top-10 lines);
  - list positions priced below 80 and 80–90 (distress ratio) and the hard restructurings;
  - show the currency split.
- **Distressed yield must be consistent across funds holding the same names.** Estimate it per
  name: weight × (that name's yield − a normal HY yield), with the price from any fund that
  publishes prices (e.g. the Fondsfinans holdings give Sigma/Flora at 81.6). Sister funds with
  similar weights get similar estimates (Heimdal Høyrente and Pluss, Oct 2026: ~110 and ~120 bp).
- **Concentration:** the top-10 share and the largest position. Show a single-name stress: loss if
  the largest position defaults at the row's Bear LGD.
- **Watchlist overlap:** fund holdings that are on the market watchlist, with weights.
- **Sanity check against IG:** a forward excess over NIBOR near IG levels (≤ ~1.2 pp) for a HY
  fund needs an explicit explanation: quality, cash share, fees, yield basis. Decompose the first
  window year line by line (NIBOR, spread carry, dry powder, fees, EL, calibration, MTM,
  performance fee).
- **Credit-cost calibration from the fund's own record** (added 2026-10-06 on user input). The
  market-based EL above is a prior. Blend it with what the manager has actually delivered:
  1. **Per year** (or year-to-date, annualised), from the monthly reports:
     - fund gap = calendar-year return − start-of-year yield after fee (on a NOK-hedged basis;
       see the yield-basis quirk);
     - market gap = DNB Carnegie Nordic HY index return − start-of-year index yield (3M NIBOR +
       the anchor spread at the start of the year).
  2. **Relative = fund gap − market gap.** Comparing with the index removes most of the common
     spread MTM and NIBOR drift. Do not calibrate on changes in the quoted spread (see Quirks).
  3. **Fund net credit cost** in that year = market realised EL (NT FTD at year-end × 55%) −
     relative. It nets defaults, workout recoveries, repricing, calls at a premium and equity
     windfalls.
  4. **Weight the record by its length:** Z = years of record ÷ (years + 3) `[A]`.
     - Blended cost = (1 − Z) × model net cost + Z × record. Model net cost = EL − the ρ part of
       distressed yield.
     - The shift (model − blended) is added to Base and Bull carry. **Bear keeps the model EL**
       unless the record contains a Bear-type year (e.g. 2015–16, 2020).
  5. **Young funds** (record < 2 years) use the record of a sister fund run by the same team
     with the same style (Høyrente Pluss uses Heimdal Høyrente plus both funds' 2026), and say
     so.
  6. **Caveats:**
     - **Survivorship and selection bias:** funds the user chose to analyse tend to have good
       records. Z is capped by the formula, and records shorter than 3 years get less than half
       the weight.
     - Mandate changes (Heimdal Høyrente, Nov 2025): keep pre-change years only if the team and
       style are unchanged, and say so.
  - This replaces the separate "repricing term": repricing gains are inside the record.
- **Track record table** in each fund section: year, start yield, return, fund gap, market gap,
  relative, net credit cost, plus annual returns further back as context.

**Step F5 — Return paths.** Per scenario and year: carry = NIBOR path + the fund's implied running
spread (moved with the market spread path, β = 1 unless evidence says otherwise `[A]`) − fees; EL
from F4; MTM from the fund's credit and rate duration and the scenario spread and swap paths;
total and excess return; window total. For non-NOK share classes, report in the class currency
and in NOK-equivalent terms (base-rate differential), never mixed.
- **Dry powder:** cash above ~5% of NAV in a daily-dealing fund is redeployed at the scenario's
  market spread and market loss rate: half in 2027, all from 2028 `[A]`. In Bear this is a benefit
  (entry at wide spreads), and the R measure shows it.
- **Distressed yield** (yield up while the market tightens, or named restructurings):
  - **Avoider:** strip it from carry (expected to be sold at market).
  - **Workout manager:** earn it × a realisation factor ρ: Base 0.5, Bear 0, Bull 1.0 `[A]`.
    Show the range 0–1 as a sensitivity.

**Step F6 — Liquidity and structure.** Dealing terms vs the liquidity of the holdings; swing
pricing.
- For **notice-period funds and AIFs** (e.g. Heimdal Høyrente Pluss: not UCITS, monthly dealing,
  one month's notice, exempt from the UCITS liquidity, placement and issuer-ownership rules):
  - The cost falls on the **investor** (an exit takes up to ~2 months and is paid at a later
    NAV), not on the fund. The structure protects the fund from forced selling and lets it run
    workout cases and stay fully invested.
  - State whether the extra yield pays for the investor's lost liquidity.
- For **daily UCITS**: swing pricing and gates are the exit costs; a cash buffer is their
  insurance.

**Step F7 — Verdict per fund** on the fund decision rule (yield versus risk): E, R, E / R against
the market reference, then attractive / marginal / unattractive. Also report:
- Bear capital preservation and worst year;
- Bull upside;
- the old absolute test (NIBOR + 2 pp, for orientation);
- the assumptions that would flip the verdict;
- the fund's main differentiators (manager style, quality, oil exposure, concentration,
  liquidity, fees).

**Step F8 — Comparison and write.** Comparison table across funds (same date, same baseline),
then the per-fund sections. Read the file back and run the fund checks.

**Step F9 — Company look-through across the user's funds** (added 2026-10-06; the risk is the
company, not the fund). Write to `docs/hy-exposure.md`.
1. **Combine all holdings** (Step F4 sources) and map every line to one **company or group**
   (all ISINs of an issuer; parent and sister issuers, e.g. Flora Food Group + Sigma Holdco).
   Covered bonds, cash and FX forwards are separate rows.
2. **Look-through exposure** to company *i* = Σ_f (user amount in fund *f* ÷ total) × weight of *i*
   in fund *f*.
   - Use the user's actual amounts when given; otherwise equal amounts, labelled EW.
   - Record each fund's holdings date and coverage (e.g. a top-25 list = partial).
3. **Report:**
   - the largest companies (top 20 with per-fund weights);
   - pairwise fund overlap = Σ_i min(w_a, w_b) over HY names; above 50% means the two funds are
     close to one position (Heimdal Høyrente vs Pluss, Oct 2026: 68%);
   - sector look-through and **correlated clusters** (e.g. the largest oil service names, which
     move together in a rig/OSV Bear);
   - the share of the top 10 and top 20 companies.
4. **Distress screen** (Stamdata routine below): match the companies against the notices; classify
   each as hard (default, restructuring, price < 80), stressed (80–90), watch or
   post-restructuring, or routine. Total the exposure per group and per fund.
5. **Company-level stress:** loss at Bear LGD from par and from the current price for the largest
   flagged names; a cluster shock (e.g. −20% MTM on the oil service cluster); all hard and stressed
   names defaulting.

**Stamdata distress routine** (each update and on request):
- Read `stamdata.com/news` page by page (`?page=N`, about one week per page, ~25 notices; wait
  about 4 s for the table to render in the in-app browser) back to the previous scan date.
- Filter rows on: default, deferral, standstill, written resolution or procedure, summons,
  bondholders' meeting, waiver, amendment, recapitalisation, bankruptcy or estates.
- For each hit on a **held company** (or a large issuer for the market log), download the notice
  PDF (`/news/api/pdf/<id>`, free via curl) and classify it:
  - default / distressed amendment (deferral, PIK, extension without compensation, haircut,
    equity conversion) / recapitalisation;
  - **routine** (fee-compensated alignment, change of owner, waiver with a fee).
  - Older summonses may lack a public PDF; record what the notice says.
- Add the hits to the default and distress log (market baseline) and to `docs/hy-exposure.md`.
  Record the scan window.

## Recalibration triggers

A full update is due when any of these occurs:

- Norges Bank changes the policy rate, or publishes an MPR path that differs ≥ 25 bp from Base in
  any window year
- The anchor spread moves > 100 bp within a month, or the monthly index return is below −2%
- A default or distressed exchange of an issuer ≥ 1% of the Nordic HY market, or ≥ 3 defaults in
  one sector row within a quarter
- The running FTD rate deviates > 1.5 pp from the Base path for the current year
- The new-issue market shuts (monthly issuance < 25% of the same month last year) or reopens
- Nordic Trustee publishes a new annual report, or NT/Stamdata publish new default statistics
- `docs/oil-market-bbb.md` or a sector BBB used for an energy row gets a new baseline whose
  downstream section flags a change
- A GDP or unemployment forecast for Norway or Sweden changes ≥ 0.5 pp at Norges Bank, SSB or the
  Riksbank
- A tracked fund changes mandate, fees or liquidity terms (fund mode)
- A Bear or Bull catalyst is triggered or a signpost is crossed
- The baseline is older than 30 days

## Output: `docs/hy-market-bbb.md`

Keep the main part short per heading; the default log, watchlist and source details go to the
appendix.

```markdown
# Nordic HY Market BBB — [baseline date]

## Metadata
- Analysis date (Europe/Oslo), information cut-off, status (Initial / Final / Provisional and why)
- Skill revisions used (hy-market-bbb, iaf-valuation)
- Previous baseline (date, days), window (stub + 2027–2029), stale after [date]
- Upstream baselines used (oil, rig, supply, shipping: baseline date, status, stale-after date)
- Series used per row; any series change since last baseline
- FX and base rates used for hedge carry (pair, rate, source, time)

## Conclusion
- BBB changed / kept unchanged — explicit
- Base in two sentences (return and its drivers; default outlook)
- Row ranking by risk premium (spread − EL), with the main reason
- Main Bear catalyst and main Bull catalyst

## Interface — rates and macro (point values; ranges below)
| Series Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| Policy rate, annual avg (%) | | | | | |
| 3M NIBOR, annual avg (%) | | | | | |
| Norway mainland GDP growth (%) | | | | | |
| Sweden GDP growth (%) | | | | | |
| Norway unemployment, registered NAV (%) | | | | | |
| Sweden unemployment, LFS (%) | | | | | |

## Year 1 by quarter — policy rate and 3M NIBOR (%)
| Scenario | Q1-27 | Q2-27 | Q3-27 | Q4-27 | Year avg |
|---|---|---|---|---|---|

## Interface — credit (point values; ranges below)
| Row Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| Nordic HY spread, annual avg (bp) | | | | | |
| FTD rate Nordic HY (%) | | | | | |
| Nordic HY spread, year-end (bp) | | | | | — |
| FTD O&G E&P (%) | | | | | |
| FTD Oil Service (%) | | | | | |
| FTD Shipping (%) | | | | | |
| FTD Real Estate (%) | | | | | |
| LGD Nordic HY (%) | | | | | |
| Expected loss Nordic HY (%) | | | | | |

## Interface — expected return, NOK hedged, before fees (%)
| Row Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Window (ann.) | Mid-cycle |
|---|---|---|---|---|---|---|
| Nordic HY total return | | | | | | |
| Nordic HY excess return over NIBOR | | | | | | |
| Norway HY total return | | | | | | |

## Scenario definitions
| Scenario | Weight (convention) | Rate path | Macro path | Oil BBB scenario (and sector BBBs) | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|---|---|
| Bear | 25% | | | | | | | |
| Base | 50% | | | | | | | |
| Bull | 25% | | | | | | | |

## Return decomposition — Nordic HY, per scenario (%)
| Scenario | Year | NIBOR | Spread carry | Expected loss | Spread MTM | Rate MTM | Total | Excess |
|---|---|---|---|---|---|---|---|---|

## Defaults and losses per row — point (range)
| Scenario | Row | 2027 | 2028 | 2029 | Mid-cycle | Volume share | n defaults (3 yrs) | Confidence |
|---|---|---|---|---|---|---|---|---|
- Year-1 build from the watchlist (bucket volume × conversion) plus background rate
- LGD per row and the security mix assumed

## Market check
| Measure | Latest (date, source) | Previous baseline | 12 months ago | Long-run (years) |
|---|---|---|---|---|
| Spread, new-issue spread, index return YTD, running FTD rate, issuance YTD, distress ratio, maturity wall | | | | |

## Drivers
### Rates (Norges Bank path, NIBOR–policy spread, hedge carry)
### Nordic macro (GDP, unemployment, inflation, property)
### Energy issuers (translation from oil / rig / supply / shipping baselines)
### Non-energy sectors (real estate, finance, industry, consumer)
### Primary market and refinancing (issuance, maturity wall, covenants)
### Recovery and restructuring practice

## Signposts and monitoring
| Signpost | Threshold (Bear / Bull) | Now | Previous | Direction |
|---|---|---|---|---|
- Open checkpoints and data gaps (carried / closed) and the next decisive observation

## For fund analyses and IAF
- What changed that fund analyses must take in, or "no material change"
- Rate path and refinancing conditions for [[iaf-valuation]] (leveraged issuers' debt service)
- Issuers on the watchlist that are also IAF companies

## Change log
- New / unchanged / changed (previous → new, reason, source)
- Forecast vs actual for the realised or partly observed year (return, FTD, spread), decomposed
- Weights kept or changed — explicit
- New baseline date

## Appendix
### Default and distress log (issuer, ISIN, row, currency, outstanding NOKm, event, date, FTD y/n, price before/after, recovery, source, funds holding)
### Watchlist (issuer, ISIN, bucket, outstanding NOKm, price/spread, maturity, trigger, funds holding)
### Maturity wall (year × sector, NOKbn)
### Sources
| ID | Source | Content | Definition / universe | Observed / published |
|---|---|---|---|---|
```

## Output: `docs/hy-funds-analysis.md`

```markdown
# Nordic HY funds — [analysis date]

## Metadata
- Analysis date, status, skill revision, HY Market BBB baseline date and status
- Share classes used (ISIN, currency, fee) and report dates per fund

## Comparison (Base unless stated; % p.a., NOK or class currency as marked)
| Fund | Style | Yield after fee (date, basis) | Rating PD / q | Credit / rate duration | Oil exposure | Cash (read as) | Base net return (window) | E: excess over NIBOR | R: stress loss | E / R vs market reference | Bear window / worst year | Liquidity | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

- Below the comparison: the **held-to-maturity view**. Window returns value the portfolio at the
  window-end spread, and any spread MTM still open at the end reverses by maturity if nothing
  defaults. Show the per-year size of that leftover.

## [Fund name]
### Facts (legal form, class, fees, mandate, liquidity terms, mandate changes)
### Portfolio snapshot (date; yield basis; durations; rating mix; top 10; cash; issuers)
### Mapping to market rows (fund label → row → weight)
### Loss rate (quality and concentration adjustments; single-name stress; watchlist overlap)
### Credit-cost calibration (year: start yield, return, fund gap, market gap, relative, net credit cost; blend)
### Return paths
| Scenario | Stub | 2027 | 2028 | 2029 | Window (ann.) | Excess over NIBOR |
|---|---|---|---|---|---|---|
### Liquidity and structure
### Verdict (attractive / marginal / unattractive; Bear capital preservation; what flips it)

## Change log
## Appendix: sources
```

## Interface to IAF and other skills

Every baseline delivers, in the fixed Interface tables and the sections behind them:

- Policy rate and 3M NIBOR paths per scenario (Year 1 by quarter), Nordic GDP and unemployment
  paths — the workspace's only Nordic rate and macro view.
- Nordic HY spread, FTD rates, LGD and expected return per row and scenario, with mid-cycle values.
- The default and distress log and the watchlist.

Use by skill:

- **Fund mode** (this skill): as in the fund procedure.
- **[[iaf-valuation]]:** NIBOR path for floating-rate debt service in the Track B build (NOK debt;
  USD debt keeps SOFR from its own source), the HY spread path and new-issue spreads for
  refinancing assumptions in Bear balance-sheet survival, and the watchlist as a distress signal
  for analysed issuers. Spreads can support raising k for a leveraged company; they never lower it
  (IAF rule).
- **Sector BBBs** do not read this baseline for their market paths; it reaches energy companies
  only through IAF financing assumptions.

## Checks before finishing

- Skill revisions stated; window and stub correct for today's date; upstream baselines' dates and
  status stated and not stale (or this baseline marked Provisional).
- No own oil, rig, OSV or tanker forecast: every energy-row driver traces to its baseline.
- Every number tagged and sourced with dates; one source per series; NT-definition replica
  labelled until NT confirms.
- Stub identical across scenarios; Year-1 rate quarters average to the annual value.
- Point value and range for every core-row scenario figure; mid-cycle set and anchored separately.
- Return built as carry − EL + MTM; no quoted yield used as an expected return; no double counting
  of distressed yield and EL; FRN/fixed split and hedging stated.
- Market default rate reconciles with Σ sector rates × volume shares; sector rates show n and
  volume.
- Bear and Bull each tied to named catalysts with rate, macro and oil scenarios and signposts; no
  probability language.
- Fund mode: prospectus used for rules; yield basis, share class currency and fee stated; sector
  mapping shown; single-name stress shown; rating split used where published; cash read in
  context (notice period vs dry powder); manager style stated; verdict on yield versus risk (E / R
  against the market reference).
- Change log complete (previous → new) or explicit "kept unchanged".
- File written, read back, tables render.
