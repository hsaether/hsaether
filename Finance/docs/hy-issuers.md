# Nordic HY — master watchlist and company bond assessment — 26 November 2026

## Metadata

- **Status (26 Nov 2026, event update for Norse Atlantic and Trustly; skill `hy-market-bbb`
  2026-11-18.2; last full refresh 19 Nov).** Prices: fund holdings and marks to 31 Oct
  (Fondsfinans holdings, Heimdal and Sissener October reports), Intrum's tender of 10 Nov, derived
  Borr and HX SSSN prices, and an assumed Norse price (26 Nov). Heimdal weights now come from its
  30 Oct holdings pages `[F]`. The November reports (~4 Dec) are the next price round. Inputs: HY
  Market BBB 18 Nov (market NIBOR path; credit values of 5 Nov), Oil 18 Nov, Rig 12 Nov.
  - **Changed this run:** **Norse Atlantic Watch → Deep distress.** On 25 Nov the company said
    its situation is "critical" and that it depends on new financing for its short-term liquidity
    and to keep operating `[F]`. Oslo Børs put the shares in the Recovery Box `[F]`, and flights
    stopped that night `[E]`. The holding is very likely the USD 52m 15% senior secured facility of
    Aug 2026 `[A]`. It is marked ~95 assumed → **~40 assumed** (range 20–60), with recovery 25 / 10
    `[A]`, Base PD 75%, Base −18%, Bear −69%.
  - **Heimdal weights** go to the 30 Oct holdings pages; the largest change is HH+'s Intrum, 2.0
    assumed → 3.1 `[F]`.
  - **Named 2027 Base:** HH 2.17 → **2.26**, HH+ 2.07 → **2.44**; Bear HH 5.38 → **5.57**, HH+ 5.26 →
    **6.03**. SIS, FF and FFK keep their values.
  - **Expected Norse NAV mark in the Q4 stub** (realised, not part of the named loss): HH ~−0.46,
    HH+ ~−1.22 pp `[A]`.
  - **Read, status kept: Trustly.** In Q3, adjusted EBITDA doubled from Q2 to SEK 86.9m, but cash
    was SEK 103.5m at 30 Sep. The equity raise closed at ~USD 60m (above the >USD 40m committed),
    and the going-concern statement is unqualified `[F]`. With no new price, the 79 mark (~30 Oct)
    and the Distressed status stay; the 80 edge still applies.
  - **Screen:** Newsweb (Oslo Børs news API) and MFN read for Norse and Trustly on 26 Nov. The last
    Stamdata page-by-page screen covered 14 Oct–19 Nov (19 Nov run).

- **Question:** for each company that matters in the analysed funds, **what return can its bonds
  be expected to give, and what is the risk?** It covers the largest positions and every name
  flagged by the Stamdata scan or by price: 29 companies. The funds are listed only as "held by".
- **This table is the funds' credit loss.** The at-risk bonds below, with these prices, default
  probabilities and recoveries, are what `docs/hy-funds-analysis.md` charges each fund. Bonds not
  on the watchlist carry no loss in Base.
- **Inputs:**
  - Prices are FX-adjusted market value ÷ nominal and include accrued interest. Sources:
    Fondsfinans holdings (30 Sep 2026), Sissener annual report (31 Dec 2025) and reports (Feb
    2026), and price moves from Heimdal's monthly contributions.
  - **From 30 Oct also fund marks** stated by the managers (Heimdal, Nordnet forum, 27–30 Oct; user
    paste `[E]`; the managers invite brokers to correct them). They are clean prices `[A]` and are
    checked against exchange quotes, bids and offers where found. Each price states its basis: fund
    mark, bid/offer or trade.
  - **From 4 Nov also prices derived from Heimdal's monthly contributions** (skill: price move ≈
    contribution ÷ the start-of-month weight, less one month's carry; accrued interest and coupons
    paid in the month are allowed for) `[A]`. Used for Borr and the HX SSSNs, which have no
    observed price, and to bound names Heimdal does not name (a name not listed lies between the
    smallest listed positive and negative contributions).
  - **Oldest price input:** end-2025 (Viaplay, W&T, both stale).
  - **Scan coverage:** as stated once in `docs/hy-market-bbb.md` (Metadata). The market-wide news
    feed was read 1 Sep–23 Oct; held companies were read issuer by issuer 4 Aug–23 Oct.
- **Method `[A]`** (skill F9 and the status scale in Definitions):
  - **Yield** = approximate yield to maturity, or to an assumed call at 102 within 1.5 years when
    the clean price (≈ dirty − 0.25 × coupon) is above 102, **plus the NOK hedge pickup** (NIBOR −
    local base: USD +0.9, EUR +2.6, SEK +2.8 pp).
  - **Status scale** (status value = one-year Base PD): Performing 0 · Watch 5% (≥ 90 with a named
    warning) · Stressed 10% (80 to below 90) · Distressed 20% (60 to below 80) · Deep distress 50%
    (< 60) · Vote or standstill 50% · Maturity flag 30% · In restructuring (in default, valued on
    its own). A price older than one month is **stale**.
  - **A bond either defaults or it does not.**
    - **Performing bonds** have no expected loss in Base: they earn their yield and pull to par.
      In Bear they take the market baseline's Bear 2027 sector default rate (the catalyst stress).
    - **At-risk bonds:** market-implied PD = (yield − NIBOR − 3 pp) ÷ (1 − the bond's own Base
      recovery). **Base PD = (status value + implied PD) ÷ 2. Bear PD = 1.3 × the higher of the
      two**, unless an override is shown with its reason.
  - **Recovery (% of par):** secured 55 / 40 (Base / Bear), senior unsecured 35 / 25, hybrid 25 /
    10. Hofseth 60 / 45: both managers see asset cover (FF, Sep: the bonds trade below the value of
    the assets and licences).
  - **Loss if default** (% of today's value) = (price − recovery) ÷ price + half a year of the
    yield (a default forfeits about half the year's carry, pull-to-par included).
  - **Expected loss (EL)** = PD × loss if default.
  - **Expected 1-year return:** Base = yield − EL. Bear = yield − Bear EL − credit duration × Bear
    spread shock (energy +5.5 pp, others +4.2 pp; stressed and watch +4.0–5.0 pp). The 30 Oct
    re-marks (Intrum, Trustly, HX super senior) use +4.5 pp, the middle of the at-risk range, × the
    modified duration at today's yield `[A]`. Borr (4 Nov, energy) uses +5.0 pp, the top of the
    at-risk range and the nearest to the energy shock, × 3.6 years `[A]`.
  - **Restructurings in progress:** the loss is in the price. Return on today's value in 2027 is
    Base 0 and Bull +25%. Bear is −25% when the bond is secured on modern, saleable assets and the
    price has absorbed the terms, and −40% otherwise (Booster, Jøtul and, from 30 Oct, HX's old 2030
    loan, which now ranks behind the new super senior debt).
- **Tags:** `[F]` fact · `[E]` external or secondary · `[A]` own assumption · `[?]` unknown.
- **Fund abbreviations:** FF = Fondsfinans High Yield · FFK = Fondsfinans Kreditt · SIS = Sissener
  Corporate Bond · HH = Heimdal Høyrente · HH+ = Heimdal Høyrente Pluss.

## Conclusion

- **Performing bonds earn their yield in Base:**
  - Floatel 9.6% (Bear −1.3%) · Archer 8.6% (−2.3%) · McDermott 10.9% (−5.5%);
  - Nynas 10.8% (+0.4%) · European Energy hybrid 13.5% (−2.8%).
  - Their Bear loss comes from the Bear catalysts (an oil Bear for drillers and E&P), not from a
    default expected today.
- **At-risk bonds pay more than their expected loss, but carry the Bear risk:**

| Bond | Status | Yield | Default probability (Base) | Loss if default | Base 1-year return | Bear 1-year return |
|---|---|---|---|---|---|---|
| **Borr 2032/2034 (~93, derived 30 Oct; Q3 read 19 Nov)** | **Watch** | 12% | 7.3% | 47% | 8.7% | −13.8% |
| **Intrum 8.5% 2030 (68.0, tender 10 Nov)** | Distressed | 25% | 25.8% | 46% | 13.1% | −14.7% |
| **Norse Atlantic USD 15% facility 2027 (~40 assumed, 26 Nov)** | **Deep distress** (Watch until 26 Nov) | 15.9% (coupon basis) | 75% | 46% | −18% | −69% |
| Trustly FRN 2030 (~30 Oct mark; Q3 and ~USD 60m equity read 26 Nov) | Distressed (at the 80 edge) | 21% | 24.3% | 41% | 10.7% | −13.2% |
| **HX super senior 2028 (~84, derived 30 Oct)** | **Stressed** (Watch until 4 Nov) | 25% | 33.1% | 29% | 15.1% | −19.7% |
| **Hofseth (~72, October; Sissener, re-marked 7 Nov)** | Distressed | 21% | 26.9% | 27% | 14.0% | −16% |
| **Intrum 7.75% 2028 (~84.3, tender proxy 10 Nov)** | Stressed | 20% | 16.3% | 57% | 11.0% | −8.9% |
| **Sigma Holdco (Flora) (79.2, 31 Oct)** | **Distressed** (Stressed until 9 Nov) | 18% | 18.0% | 65% | 6.5% | −18% |
| Magnolia Bostad (88.0, 31 Oct) | Stressed | 26% | 24.9% | 50% | 13.2% | −15% |
| **Heimstaden AB 6.75% hybrid (84.7, 31 Oct; new 9 Nov)** | Stressed | ~14% `[A]` | 9.1% | 78% | 6.9% | −11% `[A]` |
| Varel Oil & Gas (89.5, 30 Sep; left FF's and Kreditt's lists in October) | Stressed (no longer held `[A]`) | 24% | 22.6% | 50% | 12.2% | −14% |
| Shearwater (price stale) | Stressed | 18% | 16.8% | 45% | 10.8% | −11% |
| Tullow (price stale) | Stressed | 19% | 17.9% | 47% | 11.0% | −11% |
| W&T Offshore (price stale) | Watch | 15% | 10.0% | 48% | 9.8% | −7.8% |

  The market prices them for a default chance of 10–42% a year (the implied PD; the HX SSSNs
  show 56%, inflated by their high assumed recovery of 70). If they do not default they return
  12–27%; if they do, they lose 29–65% of today's value. Norse is the exception: at an assumed
  ~40 its Base return is negative, because a default is now the most likely outcome (note 10).
- **Expensive or long performing bonds give little in Base for their Bear risk:**
  - BlueNord: price 111.5, ~3.6% to an assumed call; Bear −11%;
  - NEO NEXT+: 7.5%, Bear −12.6% (unsecured E&P);
  - Ocean Yield 7.0% / −6.6%; Kistefos 8.4% / −6.9%.
- **Borr is now on the watchlist (4 Nov), and it is Høyrente's second-largest issuer** (HH 5.6%;
  HH+ 4.4%, fifth). The October reports give the first price signal after the Prospector 5 loss:
  −0.21 / −0.18 pp, a price fall of ~4–5% in the month. That puts the notes at ~93 `[A]`, so they
  are Watch, not Stressed. On Heimdal's marks the rig loss is a dent, not a solvency event: one
  rig of 29, probably insured. Q3 (19 Nov read): the $200m hull cover is recommended for payment and EBITDA recovered from Q2's
  trough (~$79m); leverage is high (~7.4× annualised) but no maturity is near. Kept Watch.
- **Heimdal's two largest Distressed names:** Intrum fell again. Its own tender (settled 10 Nov)
  bought the 8.5% 2030 notes at **68.0** (Heimdal's 27 Oct mark 73.75; ~93 at 30 Sep): Base PD
  25.8%, ~25% NOK-hedged, Base 13.1%, Bear −14.7%. The fall is a further NAV mark of ~−0.17 pp for
  HH in November.
- **Trustly (read 26 Nov; status and values kept):**
  - **Q3** `[F]`:
    - revenue SEK 630m (+7.8%; Americas +19.9%, Europe −6.6%);
    - adjusted EBITDA SEK 86.9m, against 42.3m in Q2, after tighter US approval rules cut credit
      losses; loss SEK 279m;
    - cash SEK 103.5m at 30 Sep, and EUR 15m drawn on the RCF after a further EUR 10.5m in October.
  - **Equity:** the raise closed after the quarter at **~USD 60m** (SEK ~600m), above the
    >USD 40m committed, with BlackRock funds joining. The going-concern note now rests on it.
  - **Reading:** the bond (79 at ~30 Oct) already priced the commitment. Gross leverage is still
    ~12× Q3 adjusted EBITDA annualised. Interest of ~SEK 420m a year exceeds adjusted EBITDA, so
    the raise buys about two years of cash burn `[A]`, not deleveraging.
  - With no new mark, the status stays Distressed at the 80 edge (Base PD 24%, Base 10.7%, Bear
    −13%). A mark of 80 or more moves it to Stressed (note 6).
- **Norse Atlantic (26 Nov): Watch → Deep distress.**
  - **What happened** `[F]`: on 25 Nov the company said "The Company's financial situation is
    critical" and that it depends on new financing to meet short-term liquidity needs and keep
    operating. Talks on a takeover and on short-term financing carry "no assurances". The shares
    went into the Recovery Box (−53% at the close, −86% intraday) and the Q3 report moved to 30 Nov.
  - **Since then** `[E]`: flights stopped that night (PIA: "unexpected operational suspension"), and
    staff were reportedly told wages could not be paid on time. No company release confirmed the
    stop by 26 Nov morning.
  - **What Heimdal holds:** most likely the **USD 52m 15% senior secured facility** of Norse
    Atlantic Airways AS `[A]` (19 Aug 2026; issued at 95, repaid at 103 in May 2027, plus a 3% M&A
    fee on a sale; Q2 report `[F]`). HH has 0.80% and HH+ 2.10% at the 30 Oct marks `[F]`.
  - **Mark and loss:** ~40 assumed (range 20–60; no quote seen). Base PD 75%, loss if default 46%,
    Base −18%, Bear −69%.
  - **What it means for the funds:**
    - a NAV mark of ~−0.46 pp (HH) and ~−1.22 pp (HH+) when Heimdal marks it down;
    - named 2027 Base loss 0.11 / 0.30 pp, on the smaller re-marked weights;
    - a total loss would cost 0.80 / 2.10 pp.
  - **Next:** Q3 report and a financing or insolvency outcome. In a bankruptcy or payment default,
    it becomes In restructuring and is valued on its own.
- **Restructurings in progress:** HX's old 2030 loan (marked 12.5), Booster (default,
  standstill) and Jøtul (recapitalised). Booster's and Jøtul's prices are not public.
- **HX in more detail** (updated 30 Oct; sources: the HX summonses of 29 Jul and 6 Aug with the
  term sheet, the outcome notices of 13 and 17 Aug, the H1 2026 report of 28 Aug, all on HX's
  investor page `[F]`; Heimdal's forum post of 28 Oct `[E]`):
  - **Why:** the move to a new booking system disrupted bookings in the 2026 "wave season" and
    drained liquidity. Compliance with the minimum-liquidity covenant was uncertain.
  - **Capital structure after August 2026** `[F]`:
    - **Super senior** (rank first): the EUR 50m cash management facility (Jan 2026, PIK, EURIBOR
      + 6.5% from 19 Aug, matures 30 Jun 2027), a guarantee tranche for Hurtigruten of up to EUR
      20.3m, and the **new 7% super senior bonds (SSSNs)**. The SSSNs are EUR 19.9m of new money at
      96, plus a 3-for-1 roll-up of Senior SSNs for each euro of new money. They mature on 30 Jun
      2028 at 104, pay cash interest, and a EUR 10.2m tap is committed if cash is short before the
      February 2027 coupon.
    - **Senior SSNs:** 7% EUR 257.6m 2030 (NO0010874548), less the rolled-up part (~EUR 57m at
      full take-up, ~EUR 87m with the tap `[A]`). They are secured on the two hybrid ships Roald
      Amundsen and Fridtjof Nansen, now behind the super senior debt.
    - **Junior SSNs:** 12.5% EUR 130m 2030 (NO0013465997), plus a EUR 4.46m tap at 65 in August.
      They hold first security on MS Fram and second security on the rest.
  - **Votes:** on the 7% Senior SSNs, Resolutions 1 and 5 were adopted (13 Aug) and 2–4 were voted
    down; the funding transaction went ahead without them. The Junior SSN proposals were adopted
    on 17 Aug, with ~98.6% support indicated in advance.
  - **H1 2026** `[F]`:
    - EBITDA was −EUR 13.8m and equity −EUR 131m.
    - Cash was EUR 29.5m, and customer deposits EUR 123m.
    - The guidance for 2026 normalised EBITDA is EUR −17 to −25m. The target is breakeven in 2027
      and positive cash flow after vessel capex in 2028.
    - The directors state a **material uncertainty on going concern**. More funding is needed in
      Q2 2027 (the MS Spitsbergen financing falls due in June 2027, and the cash management
      facility must be refinanced).
  - **Heimdal's split (28 Oct)** `[E]`:
    - The **old 2030 loan** was marked 25 → 12.5 after a small trade that was not Heimdal's. It is
      now 0.34% of HH (−0.36% of NAV).
    - The rest of the HX exposure "sits in debt moved up the capital structure with better
      priority", i.e. the SSSNs. HH 30 Sep 1.83% − 0.72% (the old loan at 25) ≈ **1.1% of NAV in
      SSSNs** `[A]`.
    - Heimdal does not name the ISIN of the old loan. A pro rata take-up of the new money and the
      3-for-1 roll-up on a Senior SSN holding fits both figures (SSSNs at ~96, the remaining Senior
      SSNs at 25 on 30 Sep). So the old loan is most likely the **Senior SSN stub** `[A]`; the
      Junior SSNs are the alternative `[?]`.
  - **Reading:**
    - The SSSNs rank first on two modern ships (vessel book EUR 322m for four ships at 30 Jun).
      The whole super senior class is ~EUR 150m (facility, guarantee tranche and SSSNs) and up to
      ~EUR 190m with the tap and its roll-up `[A]`. They are valued as a named at-risk bond (Watch
      on 30 Oct; Stressed from 4 Nov).
    - The old loan's price says the market sees almost nothing for the creditors behind the super
      senior debt. Base 0, Bear −40% (now behind the super senior debt), Bull +25%.
    - The February 2027 coupon (tap or PIK) and the June 2027 refinancing are the next tests.
  - **4 Nov (October reports `[F]`):** both funds repeat the 28 Oct post: the old loan was cut
    25 → 12.5 after a small trade, and Heimdal sees limited further downside on it. But HX cost HH
    −0.49 pp and HH+ −0.40 pp in October. The old loan explains ~−0.35 and ~−0.27, so the SSSNs
    lost ~12% in the month `[A]`. They are now Stressed at ~84 (note 9). Heimdal's own NAV no
    longer carries the super senior bonds near their issue price.

## Master watchlist — open entries

Held names only; names that are not held are in `docs/hy-market-bbb.md` (Appendix, Watchlist).
Weights are % of NAV at 30 Sep (Sissener: 30 Sep top 10, otherwise 31 Aug or earlier), except
where a later date is shown: Heimdal's 30 Oct top 10 and HX old-loan weights (October reports
`[F]`), and derived 30 Oct weights for the HX SSSNs and Pluss's Intrum `[A]`.

| Issuer | Row | Status now | On list since (date: price, status) | Price now (date; stale / assumed) | Next decisive event | Held by (% of NAV) | Outstanding NOKm |
|---|---|---|---|---|---|---|---|
| **Borr Drilling: 8.75% 2032 and 9.00% 2034 senior secured notes** | Oil Service (jackups) | **Watch** (new entry 4 Nov) | 4 Nov: ~93 derived, Watch (after the Prospector 5 loss on 24 Oct) | **~93** (30 Oct; derived from Heimdal's October contribution, range 91–96; no observed quote) `[A]` | **Q3 read 19 Nov:** $200m hull cover recommended for payment (no loss of hire); EBITDA ~$79m; debt $2.53bn, $51m due in 12 months. Next: insurance paid; coupon ~$110m on 15 Jan 2027; Heimdal's November report (~4 Dec). Shares NOK 31.0 (19 Nov, −9% on the day) | **HH 5.6, HH+ 4.4 (30 Oct)** `[F]` | ~18,800 ($2,035m at USD/NOK 9.23, 30 Oct) |
| HX Hold Co: old 2030 loan (most likely the 7% Senior SSN stub `[A]`) | Consumer (cruise) | In restructuring | 6 Oct: ~45 assumed (whole HX position), In restructuring | **12.5** (Heimdal fund mark ~27 Oct after a small third-party trade; 25 before; confirmed in the October reports `[F]`) | February 2027 coupon (tap or PIK); refinancing of the cash management facility by 30 Jun 2027 | **HH 0.35, HH+ 0.27 (30 Oct)** `[F]` | ~2,070 (EUR ~200m left after the roll-up `[A]`) |
| HX Hold Co: 7% super senior bonds 2028 (SSSN; new money and roll-up, Aug 2026) | Consumer (cruise) | **Stressed** (Watch 30 Oct–4 Nov) | 30 Oct: ~96 assumed, Watch | **~84** (30 Oct; derived: HX's October contribution less the old-loan mark, both funds; range 79–88) `[A]` | The same; HX's Q3 report (date `[?]`); the top-up certificate (~12 Jan 2027) | HH ~1.16, HH+ ~0.87 (30 Oct) `[A]` | ~800 (EUR ~78m at full take-up `[A]`) |
| Booster Precision | Industry (auto) | In restructuring | 5 Oct: `[?]`, Vote or standstill | `[?]` | Outcome of the standstill (prolonged 1 Oct and again 2 Nov, Stamdata) | HH 0.30, HH+ 0.26 | ~650 |
| Jøtul | Consumer | In restructuring | 6 Oct: `[?]`, In restructuring | `[?]` | Terms of the new bonds; Q3 investor call 18 Nov, annual report 11 Nov (Stamdata) | HH 0.28, HH+ 0.12 | `[?]` |
| Hofseth | Consumer (seafood) | Distressed | 6 Oct: 77.0 (31 Aug), Distressed | **~72 dirty ≈ 70 clean** (FF's 31 Oct holdings 72.8 dirty ≈ 70.9 clean; FF "just under 70", Sissener "around 70" `[E]`; re-marked 7 Nov, confirmed 9 Nov); 76.2 dirty (30 Sep, FF) | **Q3 (16 Nov): revenue −46%, processing contracts lost (Salmon Business `[E]`)**; covenant step in force from 7 Nov (value-adjusted equity ratio 25 → 27.5%; first test 31 Dec); NOK 600m equity raise still open; Japanese partners wrote down their investment (early Nov `[E]`); Dyrkorn plant delayed by a municipal error (FF `[E]`) | **FF 0.91, FFK 0.75 (31 Oct)**, **SIS 2.6 (30 Oct)** | `[?]` |
| Sigma Holdco (Flora, KKR) | Consumer | **Distressed** (Stressed until 9 Nov) | 6 Oct: 81.6 (31 Aug), Stressed | **79.2 (31 Oct, FF holdings)**; 80.0 (30 Sep) | Within one point of the 80 edge: at 80 it is Stressed again (Base PD ~13) | **FF 0.83 (31 Oct)**, **HH 3.7 (30 Oct)**, HH+ 2.67 | `[?]` |
| Flora Food (opco, secured) | Consumer | Watch | 6 Oct: ~95 assumed, Watch | ~95 assumed (October: between −4% and +0.5% in both funds) | Same group as Sigma | **HH 4.1, HH+ 3.8 (30 Oct)** | `[?]` |
| Magnolia Bostad | Real Estate | Stressed | 6 Oct: 86.4 (31 Aug), Stressed | **88.0 (31 Oct, FF holdings)**; 87.3 (30 Sep) | Swedish residential sales; real estate bonds hit hardest in October (Sissener `[E]`) | **FF 0.60 (31 Oct)** | `[?]` |
| **Heimstaden AB 6.75% hybrid** (new 9 Nov) | Real Estate | **Stressed** | 9 Nov: 84.7 (31 Oct), Stressed | **84.7 dirty (31 Oct, FF holdings)**; bought at low prices in the second half of October (FF `[E]`) | Hybrid call or extension (first-call date not read `[?]`) | **FF 0.40 (31 Oct)** | `[?]` |
| Varel Oil & Gas | E&P | Stressed (**no longer in FF's or Kreditt's 31 Oct lists** `[A]`) | 6 Oct: 89.9 (31 Aug), Stressed | 89.5 (30 Sep; no October price) | Confirm the exit at the November holdings | **0 `[A]`** (FF 0.98, FFK 0.62 on 30 Sep) | `[?]` |
| Shearwater | Oil Service | Stressed (Watch until 18 Oct) | 6 Oct: ~86 (Feb 2026), Watch | ~86 (Feb 2026, **stale**; Sep +2% and Oct ~flat from Heimdal contributions; year-to-date contributions point to ~88–93 `[A]`, not applied) | A current price | **HH 3.3, HH+ 3.8 (30 Oct)**, SIS 2.24 | `[?]` |
| Tullow | E&P | Stressed (Watch until 18 Oct) | 6 Oct: ~88 (Feb 2026), Watch | ~88 (Feb 2026, **stale**) | A current price | SIS 1.80 | `[?]` |
| Viaplay | Other (media) | Stressed (Watch until 18 Oct) | 6 Oct: 89.6 (end-2025), Watch | 89.6 (end-2025, **stale**); October ~−1% in price (HH year-to-date contribution 0.20 → 0.20, i.e. no carry gain) `[A]` | A current price | HH 1.19, HH+ 1.67, SIS ~1.6 `[A]` | `[?]` |
| W&T Offshore | E&P | Watch | 11 Oct: ~92 (end-2025), Watch | ~92 (end-2025, **stale**) | A current price; Sissener bought "significantly" in Sep | SIS 2.8 | `[?]` |
| Foxway (Ytinrete BidCo) | Other | Watch (recovered) | 6 Oct: 96.3 (31 Aug), Watch | **93.7 (31 Oct, FF holdings)**; 96.0 (30 Sep) | — | **FF 1.05, FFK 0.58 (31 Oct)**, HH 2.38, HH+ 3.11 | `[?]` |
| Trustly | Finance | Distressed (at the 80 edge) (Watch until 30 Oct) | 6 Oct: ~95 assumed, Watch | **79** (Heimdal fund mark ~30 Oct; bid 76/77 for size not filled, offer 80.375 for 400k; no trade) `[E]`. **Rose in October** (+0.42 / +0.44 pp `[F]`) from ~70 at 30 Sep `[A]` | Owner equity of >USD 40m closing in November; Q3 report 25 Nov | **HH 3.8, HH+ 3.7 (30 Oct)**, SIS 1.84 (31 Aug) | ~3,870 (EUR 375m) |
| **Intrum: 7.75% senior secured exchange notes 2028 (XS3099990296; Sissener)** | Finance | **Stressed** (new entry 7 Nov) | 7 Nov: ~85 assumed, Stressed (held throughout; wrongly recorded as repaid from 11 Oct) | **~84.3** (19 Nov; Intrum's tender settled 10 Nov bought the SEK 7.75% 2028 at a weighted 84.26, max 87.70: proxy for the EUR 2028 `[E]`) | Q4 report 4 Feb 2027 | **SIS 1.7** (NOK-R October report `[F]`) | `[?]` |
| Intrum (Heimdal's 8.5% notes) | Finance | Distressed (Watch until 30 Oct) | 6 Oct: ~90 assumed, Watch | **68.0** (Intrum's tender of the 8.5% 2030 notes, settled 10 Nov `[F]`); 73.75 Heimdal mark 27 Oct; ~93 at 30 Sep `[A]` | Cost plan finalised in Q4; Q4 report 4 Feb 2027 | **HH 3.0 (30 Oct)** `[F]`; HH+ ~2.0 `[A]` (bought more; 1.82 on 30 Sep) | ~7,600 (8.5% 2030: EUR ~737m `[E]`) |
| Convene | Other | Watch (recapitalised Sep; FTD `[?]`) | 6 Oct: ~90 assumed, Watch | ~90 **assumed** | Whether the recapitalisation counts as an FTD | HH 1.10, HH+ 2.93 | `[?]` |
| Norse Atlantic | Other (airline) | Watch | 6 Oct: ~95 assumed, Watch | ~95 **assumed** | — | HH 0.76, HH+ 2.27 | `[?]` |
| EHAB | `[?]` | Watch `[A]` | 5 Oct: `[?]`, Watch (largest negative contributor at FF in Aug) | `[?]` (a +3 bp contributor in Sep) | Weight and price; not yet in FF's named loss | FF `[?]` | `[?]` |

## Outcome record

**Exits and status changes since the list started (5–6 Oct):**

| Issuer | From (date: price, status) | To (date: status or outcome) | Outcome | Note |
|---|---|---|---|---|
| Kistos | 6 Oct: ~100 `[?]`, Watch (written resolution summoned) | 11 Oct: Performing | Cured | Oman's final approval for Blocks 3 and 4; leverage < 1x (FF, Sep). Summons read 17 Oct: a waiver releasing the USD 20m escrow into the Block 9 deal, with a first-priority pledge for bondholders (routine) |
| Eldorado Drilling | 6 Oct: ~100 `[?]`, Watch (terms amended, purpose not read) | 11 Oct: Performing | Cured `[A]` | First contract for the Deep Value Driller; FF added. The amendment's purpose is still not read |
| Intrum (Sissener's bond) | 6 Oct: ~90 assumed, Watch | Sep 2026 (seen 11 Oct): repaid | Repaid — **corrected 7 Nov: wrong** | The September tender bought the 7.75% 2027 notes at 102 `[E]`. Sissener's 7.75% 2028 notes (1.7%) stayed (NOK-R October report `[F]`) and are back on the list from 7 Nov as Stressed (~85 assumed). From 11 Oct to 7 Nov the position carried no named loss (SIS ~0.15 pp too low) |
| Shearwater, Tullow, Viaplay | 6 Oct: Watch | 18 Oct: Stressed | Reclassified | The rule applied to their (stale) 80–90 prices; no market move |
| Intrum (Heimdal's 8.5% notes) | 6 Oct: ~90 assumed, Watch | 27 Oct: 73.75 (fund mark), Distressed | Price fall after the Q3 report; no default | Q3 (23 Oct): SEK 1.5bn goodwill impairment, servicing income still falling; shares −39% intraday. The issuer's own 30 Sep fair value of all its bonds was 95.2% of nominal, so the assumption was roughly right before the report |
| Trustly | 6 Oct: ~95 assumed, Watch | 30 Oct: 79 (fund mark), Distressed | Assumption corrected; no default | The ~95 assumption was wrong: Sissener bought at 75.50 in mid-June after a weak Q1. The status was too mild from 6 Oct. **4 Nov:** the October reports show it rose in October (+0.42 / +0.44 pp), from ~70 at 30 Sep `[A]` (Distressed already then) |
| HX Hold Co | 6 Oct: ~45 assumed, In restructuring (one position) | 30 Oct: split into the old 2030 loan (12.5, In restructuring) and the new SSSNs (~96 assumed, Watch) | Restructuring terms read | The August transaction primed the Senior SSNs that did not roll up (an FTD under the NT definition, already logged as In restructuring). Heimdal moved most of its exposure into the super senior bonds |
| HX SSSN 2028 | 30 Oct: ~96 assumed, Watch | 4 Nov: ~84 derived (30 Oct), Stressed | Price fall; no default | HX's October contribution exceeds the old-loan mark by 0.13–0.14 pp in both funds: ~−12% on the SSSNs `[A]`. No trade or quote seen |
| Borr Drilling (2032/2034 notes) | 25 Oct: par assumed, Performing (provisional; Prospector 5 lost 24 Oct) | 4 Nov: ~93 derived (30 Oct), Watch | Price fall; no default | First price signal: Heimdal's October contribution, −0.21 / −0.18 pp (≈ −4–5% in price). September was already ~−4%, mostly US rates. Insurance is still not stated by Borr |
| Intrum (Heimdal's 8.5% notes) | 27 Oct: 73.75, Distressed | 10 Nov: 68.0 (tender), Distressed | Price fall; no default | Intrum bought €100m of its notes below par (2029 at 79.4, 2030 at 68.0) |
| Sigma Holdco | 6 Oct: 81.6, Stressed | 9 Nov: 79.2 (31 Oct), Distressed | Price fall; no default | FF's 31 Oct holdings settle the 80 edge |
| Varel Oil & Gas | 6 Oct: 89.9, Stressed | 9 Nov: not in FF's or Kreditt's 31 Oct lists | Sold or cut below 0.39% `[A]`; no default | +2 bp contributor in October; the manager has not confirmed an exit |
| Heimstaden AB hybrid | not held | 9 Nov: 84.7 (31 Oct), Stressed; new entry | FF bought in the second half of October | Not a fallen performer: a deliberate purchase at low prices |

**Year-end 2025 → latest price** (bonds with published year-end prices in the FF and Sissener
annual reports; the first transition data for calibrating the status values):

| Bond | 31 Dec 2025 (price: status) | Latest (date: price, status) | Outcome so far |
|---|---|---|---|
| Foxway | 74.65: Distressed | 30 Sep: 96.0, Watch | Recovered; no default |
| Tullow | 73.5: Distressed | Feb 2026: ~88, Stressed | Maturity extended to 2028 with a consent fee (compensated, so not an FTD) |
| Esmaeilzadeh | 76.25: Distressed | FF exited by Aug | `[?]` |
| Sunborn | 71.0: Distressed | FF exited by Aug | `[?]` |
| Sigma Holdco | 87.0: Stressed | 30 Sep: 80.0, Stressed | No default; weaker |
| Varel Oil & Gas | 87.25: Stressed | 30 Sep: 89.5, Stressed | No default |
| Caybon | 85.5: Stressed | Written procedure, amended and restated terms (Sep 2026); FF exited | FTD `[?]` |
| Shearwater | 83.0: Stressed | Feb 2026: ~86, Stressed | No default |
| Viaplay | 89.6: Stressed | No newer price | `[?]` |
| Hofseth | 97.9: Performing | 30 Sep: 76.2, Distressed | Fell into distress inside the year; no default yet |
| Magnolia Bostad | 95.0: Performing | 30 Sep: 87.3, Stressed | No default yet |

- **Reading:** of nine bonds priced below 90 at year-end, none is a confirmed first-time default
  nine months later. Caybon is open, and two outcomes are unknown after FF sold. Two performing
  bonds fell into stress.
- That is too few cases to recalibrate the 5 / 10 / 20% status values. It is the start of the
  record, and the next data point is the 2026 annual reports.

## Company bond table

| Company | Row | Bond | Price (date) | Yield, NOK-hedged | Status | PD 1y Base / Bear (market-implied) | Recovery Base / Bear | Loss if default Base / Bear | EL Base / Bear | **Exp. 1y return Base / Bear** | Held by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Floatel | Oil Service | 9.75% 2029 USD, secured | 104.9 (31 Aug) | 9.6 | Performing; booked 2026 | 0 / 4.0 (3.9) | 55 / 40 | — / 67 | 0 / 2.7 | **9.6 / −1.3** | FF, HH, HH+, FFK |
| Archer | Oil Service | 9.5% 2030 USD, secured | 106.7 (31 Aug) | 8.6 | Performing | 0 / 4.0 (1.8) | 55 / 40 | — / 67 | 0 / 2.7 | **8.6 / −2.3** | FF, HH, HH+, FFK |
| McDermott | Oil Service | 10.5% 2031 USD, secured | 104.5 (31 Aug) | 10.9 | Performing (restructured twice before) | 0 / 4.0 (6.9) | 55 / 40 | — / 67 | 0 / 2.7 | **10.9 / −5.5** | FF, SIS, FFK |
| Nynas | Industry | 11.75% 2028 USD, secured | 105.8 (end-2025) | 10.8 | Performing | 0 / 6.0 (6.7) | 55 / 40 | — / 68 | 0 / 4.1 | **10.8 / +0.4** | SIS |
| European Energy | Other | 10.5% hybrid 2036 EUR | 100.2 (31 Aug) | 13.5 | Performing; subordinated | 0 / 6.0 (7.6) | 25 / 10 | — / 97 | 0 / 5.8 | **13.5 / −2.8** | FF, HH, HH+, FFK |
| DGOC | E&P | 9.75% 2029 USD, secured | 106.4 (31 Aug) | 8.9 | Performing | 0 / 8.0 (2.5) | 55 / 40 | — / 67 | 0 / 5.3 | **8.9 / −4.7** | FF, HH, HH+, SIS, FFK |
| Kistefos | Finance | NOK FRNs 2027–30, unsecured | ~104 (31 Aug) | 8.4 | Performing; terms aligned (fee) | 0 / 6.0 (0.9) | 35 / 25 | — / 80 | 0 / 4.8 | **8.4 / −6.9** | FF, HH, HH+, SIS, FFK |
| Ocean Yield | Shipping | 7.39% FRN 2031 NOK, unsecured | 103.5 (31 Aug) | 7.0 | Performing; new owner A.P. Møller Holding | 0 / 3.0 (0.0) | 35 / 25 | — / 79 | 0 / 2.4 | **7.0 / −6.6** | FF, SIS, FFK |
| NEO NEXT+ Energy | E&P | 6.625% 2031 USD, unsecured | 101.6 (31 Aug) | 7.5 | Performing | 0 / 8.0 (0.0) | 35 / 25 | — / 79 | 0 / 6.3 | **7.5 / −12.6** | FF, HH, HH+, FFK |
| BlueNord | E&P | 7.875% 2031 USD, unsecured | 111.5 (31 Aug) | ~3.6 to call `[A]` | Performing; expensive | 0 / 8.0 | 35 / 25 | — / 79 | 0 / 6.4 | **3.6 / −11.0** (call terms `[?]`) | FF, HH, FFK |
| Kistos | E&P | NOK/USD bonds | ~100 `[?]` | ~10 `[A]` | Performing (since 11 Oct; outcome record) | 0 / 8.0 | 55 / 40 | — / 65 | 0 / 5.2 | **~10 / ~−9** `[A]` | FF, FFK |
| Eldorado Drilling | Oil Service | USD bonds | ~100 `[?]` | ~10 `[A]` | Performing (since 11 Oct; outcome record) | 0 / 4.0 | 55 / 40 | — / 65 | 0 / 2.6 | **~10 / ~−6** `[A]` | FF, FFK |
| **Borr Drilling** | Oil Service | 8.75% 2032 ($1,100m) + 9.00% 2034 ($935m) USD, senior secured; 5% a year amortised at 102.5 from Jul 2027 (the 2028/2030 notes were redeemed in Jun 2026) `[F]` | **~93 (30 Oct; derived from Heimdal's October contribution, −0.21 / −0.18 pp ≈ −4–5% in price; range 91–96; no observed quote)** `[A]` | **~12.1** (YTM ~11.2 + 0.9; ~4.7-year average life) `[A]` | **Watch**: price fall after the Prospector 5 loss; Q3 (19 Nov read): hull cover $200m recommended for payment, EBITDA ~$79m, leverage ~7.4× (note 5) | **7.3 / 12.5 (9.6)** | 55 / 40 | **47 / 63** | **3.4 / 7.9** | **8.7 / −13.8** | HH 5.6, HH+ 4.4 (30 Oct) |
| Foxway | Other | 9.642% FRN 2028 EUR, secured | **93.7 (31 Oct, FF)**; 96.0 (30 Sep); 74.65 end-2025 | **17.9** | Watch, recovered | **13.7 / 29.2 (22.4)** | 55 / 40 | **50 / 66** | **6.9 / 19.3** | **11.0 / −8.6** | FF, HH, HH+, FFK |
| W&T Offshore | E&P | 10.75% 2029 USD, senior secured (US Gulf of Mexico) | ~92 (91.8 end-2025, SIS annual report; **stale** `[E]`) | ~14.6 | Watch: leveraged offshore E&P | 10.0 / 19.5 (15.1) | 55 / 40 | 48 / 64 | 4.8 / 12.4 | **9.8 / −7.8** | SIS (2.8%) |
| Viaplay | Other | FRN 2028 SEK, post-restructuring | 89.6 (end-2025, **stale**) | 16.0 | **Stressed** | **11.3** / 19.5 ¹ (12.6) | 35 / 25 | 69 / 80 | **7.8** / 15.6 | **8.2 / −8.4** | HH, HH+, SIS (~1.6% `[A]`) |
| Tullow | E&P | 10.25% extended to 2028 USD | ~88 (Feb 2026, **stale** `[E]`) | 19.4 | **Stressed**; amended (consent fee) | **17.9** / 33.5 (25.8) | 55 / 40 | 47 / 64 | **8.4** / 21.5 | **11.0 / −10.5** | SIS |
| Shearwater | Oil Service | 9.5% 2029 USD | ~86 (Feb 2026, **stale** `[E]`); October ~flat (Heimdal) | 18.4 | **Stressed**; repricing case | **16.8** / 30.6 (23.6) | 55 / 40 | 45 / 63 | **7.6** / 19.2 | **10.8 / −10.8** | HH, HH+, SIS |
| Varel Oil & Gas | E&P | 12.25% 2028 USD | 89.5 (30 Sep; no October price; left the FF and Kreditt lists `[A]`) | 23.6 | Stressed | 22.6 / 45.7 (35.1) | 55 / 40 | 50 / 67 | 11.4 / 30.7 | **12.2 / −13.9** | none now `[A]` |
| Magnolia Bostad | Real Estate | 10.816% FRN 2028 SEK | **88.0 (31 Oct, FF)**; 87.3 (30 Sep) | **25.7** | Stressed | **24.9 / 51.7 (39.8)** | 55 / 40 | **50 / 67** | **12.5 / 34.9** | **13.2 / −15.4** | FF |
| **Heimstaden AB** (new 9 Nov) | Real Estate | 6.75% hybrid, perpetual, EUR; first call not read `[?]` | **84.7 (31 Oct, FF, dirty)** | **~14** `[A]` (running 8% + hedge 2.6, part of the pull to par) | **Stressed** | **9.1 / 13.0 (8.3)** | 25 / 10 | **78 / 95** | **7.1 / 12.4** | **6.9 / −11** `[A]` | FF |
| Sigma Holdco (Flora, KKR) | Consumer | 8.625% 2031 EUR, thin unsecured holdco layer | **79.2 (31 Oct, FF)**; 80.0 (30 Sep); 87.0 end-2025 | **18.2** | **Distressed** (Stressed until 9 Nov) | **18.0** / 32.5 ² (**16.0**) | 35 / 25 | 65 / 78 | **11.7** / 25.2 | **6.5 / −18.3** | FF, HH, HH+ |
| Flora Food (opco) | Consumer | senior secured | ~95 (**assumed**) | ~11 `[A]` | Watch (same group as Sigma) | **6.1** / 15 ³ (7.1) | 55 / 40 | 48 / 63 | **2.9** / 9.5 | **8.1 / −4.5** | HH, HH+ |
| Hofseth | Consumer | 8.244% FRN 2030 EUR, secured | **~72 dirty ≈ 70 clean (FF's 31 Oct holdings 72.8 dirty ≈ 70.9 clean; FF "just under 70", Sissener "around 70" `[E]`; re-marked 7 Nov, confirmed 9 Nov)**; 76.2 dirty (30 Sep, FF); quoted 70–75 during Sep (FF); 97.9 end-2025 | **~21.3** | Distressed; needs new equity; Q3 16 Nov | **26.9** / 52.0 ⁴ (**33.8**) | 60 / 45 | **27 / 48** | **7.3 / 25.0** | **14.0 / −16.2** | FF, SIS, FFK |
| Trustly | Finance | EUR 375m senior secured FRN 8 Oct 2030, EURIBOR + 6.75% (coupon now 9.35%; NO0013646943); a super senior RCF (Mar 2026) ranks ahead | **79 (~30 Oct, Heimdal fund mark; bid 76/77, offer 80.375, no trade)**; ~70 at 30 Sep, derived `[A]` (rose in October); 75.50 mid-Jun (Sissener's purchase) | **20.7** (NIBOR + 6.75 + pull to par; 20.0 at the offer, 22.0 at the bid) | **Distressed (at the 80 edge)**: weak Q2, owner equity >USD 40m closing Nov | **24.3** / 37.3 (28.7); 19.3 at the Stressed band ⁶ | 55 / 40 | **41 / 60** | **10.0** / 22.4 | **10.7 / −13.2** | HH, HH+, SIS |
| **Intrum (Sissener)** | Finance | **Intrum Investments & Financing 7.75% senior secured exchange notes 2028, EUR (XS3099990296)**; same ranking as the 8.5% notes | **~84.3 (10 Nov; the SEK 7.75% 2028 tender clearing price, proxy `[E]`)** | **~20.2** (YTM ~17.6 + 2.6) | **Stressed**: price 80 to below 90; same credit as the 8.5% notes | **16.3 / 29.4 (22.6)** ⁱ | 45 / 30 ⁷ | **57 / 75** | **9.2 / 21.9** | **11.0 / −8.9** | SIS (1.7) |
| Intrum | Finance | Intrum Investments & Financing 8.5% senior secured exchange notes, EUR, quarterly coupon; 2030 note assumed (XS3099996814, 11 Sep 2030) `[A]` | **68.0 (10 Nov, Intrum's own tender, €7.3m of the 2030s accepted)** `[F]`; 73.75 Heimdal mark 27 Oct; ~93 at 30 Sep `[A]` | **~25.1** (YTM ~22.5 + 2.6) | **Distressed**: Q3 goodwill impairment, servicing income falling; buying back below par | **25.8** / 41.0 (31.5) | **45 / 30** ⁷ | **46 / 69** | **12.0** / 28.1 | **13.1 / −14.7** | HH, HH+ |
| Convene | Other | NOK, after recapitalisation | ~90 (**assumed**) | ~12 `[A]` | Watch; recapitalised Sep 2026 | **7.2** / 15 ³ (9.3) | 55 / 40 | 45 / 62 | **3.2** / 9.2 | **8.8 / −3.2** | HH, HH+ |
| Norse Atlantic | Other | USD | ~95 (**assumed**) | ~12 `[A]` | Watch | **7.2** / 20 ³ (9.3) | 55 / 40 | 48 / 64 | **3.4** / 12.8 | **8.6 / −6.8** | HH, HH+ |
| HX: 7% super senior bonds (SSSN) | Consumer | 7% super senior secured, 30 Jun 2028 at 104, cash coupon; pari passu with the EUR 50m cash management facility; senior to the Senior SSNs | **~84 (30 Oct; derived: HX's October contribution less the old-loan mark, ~−12% in both funds; range 79–88; no trade or quote)** `[A]`; 96 issue price (21 Aug) | **24.6** (YTM 22.0 + 2.6) | **Stressed** (4 Nov; Watch 30 Oct–4 Nov): price 80 to below 90; going-concern uncertainty; February 2027 coupon may need the tap or PIK | **33.1 / 73.0 (56.2)** | 70 / 50 ⁸ | **29 / 53** | **9.6 / 38.5** | **15.1 / −19.7** | HH, HH+ |
| HX: old 2030 loan (most likely the 7% Senior SSNs not rolled up `[A]`) | Consumer | 7% senior secured EUR 2030, now behind ~EUR 150m of super senior debt | **12.5 (~27 Oct, Heimdal fund mark after a small third-party trade; 25 before)** `[E]`; confirmed in the October reports `[F]` | coupon basis 7% (YTM ~133% at 12.5); removed from carry | **In restructuring** (adopted 13 and 17 Aug 2026) | in default | behind the super senior debt | priced in | — | **0 / −40% of value** (Bull +25%) `[A]` | HH, HH+ |
| Booster Precision | Industry | EUR 60m FRN, secured | `[?]` | — | **In restructuring**: default; standstill | in default | — | priced in | — | **0 / −40%** `[A]` | HH, HH+ |
| Jøtul | Consumer | NOK | `[?]` | — | **In restructuring**: recapitalised with new money | — | — | — | — | **0 / −40%** `[A]` | HH, HH+ |

Values in **bold** changed on 19 Nov (the two Intrum rows: tender prices) or are the latest re-marks
(Borr and the HX SSSNs 4 Nov; Trustly and the HX old loan 30 Oct). Bear PDs set above the
rule (rule value: 1.3 × the higher of the status value and the implied PD):
1. **Viaplay** 19.5 (rule 16.4): post-restructuring credit. The original reason was not recorded;
   it is kept because it is harsher than the rule.
2. **Sigma** 32.5 (rule 26.0 from 9 Nov; 20.0 before): a thin unsecured holdco layer under a group with weak leverage and
   interest cover. The original reason was not recorded; kept as harsher.
3. **Assumed-price names** (Flora opco, Convene 15; Norse 20; rule 8.4–12.1): no published
   price, so the Bear is set above the rule `[A]`. Trustly and Intrum left this group on 30 Oct:
   they now have prices, and their Bear PDs are the rule values (37.3 and 33.4). The HX SSSNs left
   it on 4 Nov (derived price ~84; rule value 73.0), and so did Borr (rule value 12.5).
4. **Hofseth** 52.0 (rule 37.4): the NOK 600m equity raise is still outstanding, and in Bear it is
   assumed to fail `[A]`. The original reason was not recorded.

**Note 5 (not a Bear override): Borr Drilling, signposts after the Prospector 5 loss** (25 Oct;
status-scale thresholds).

- **Watch (5%):** the first price is ≥ 90 but shows a fall ("a recent price fall"; the skill sets
  no size for it). Also Watch on a non-routine bondholder notice whose purpose is not yet read, or
  on a Borr statement that the hull cover is disputed or short of the rig's value.
- **Stressed (10%):** the first price is 80 to below 90. **Distressed (20%):** 60 to below 80.
- **Vote or standstill (50%):** a bondholder vote or a standstill.
- **Performing confirmed:** Borr confirms hull and machinery cover at the agreed value, and the
  notes hold near par.
- A move of more than 10 points must be confirmed in a second source before it moves the status
  (skill plausibility check).
- **30 Oct status: no signpost hit; Performing kept (provisional).**
  - No price for the 2032/2034 notes was found (news and web search, 30 Oct) `[?]`.
  - BW Energy's Q3 report (29 Oct) `[F]`:
    - the MaBoMo Phase 2 campaign is delayed by the rig loss, and "it is too early to confirm when
      drilling will resume";
    - the planned workover will use a hydraulic workover unit instead of a rig;
    - BW was already searching for a new rig for the Bourdon programme;
    - MaBoMo production resumed on 28 Oct with no damage reported.
  - No replacement Borr rig is named, so the ~$15m EBITDA loss to Jul 2027 assumed on 25 Oct
    stands, unless loss-of-income cover applies `[A]`.
  - Insurance is still not stated by Borr. Next: Borr's Q3 report (~18 Nov `[E]`) and Heimdal's
    October reports (~6 Nov: Borr's contribution, the first price signal).
- **4 Nov status: Watch signpost hit (first price ≥ 90 with a fall). Performing → Watch.**
  - **The signal** `[F]`: Borr contributed −0.21 pp to Høyrente and −0.18 pp to Pluss in October,
    on start weights of 5.36% and 4.78%. That is a total return of about −3.9% in both funds.
  - **Price derivation** `[A]`:
    - No coupon fell in October (coupons 15 Jan and 15 Jul). The price change is the total less
      one month's accrual (~0.74 points): about −4.6% in October.
    - September was already −0.18 / −0.16 pp (≈ −4% in price). Heimdal blames rising US rates on
      the fixed-rate USD bonds for September.
    - If the notes were near par to 102 at end-Aug, they ended October at ~91.5–93.5, or ~95.5 if
      they were still at par on 30 Sep. Point ~93, range 91–96: Watch in the whole range.
    - The move is below 10 points, so no second source is needed. It rests on Heimdal's NAV only,
      and no quote has been seen.
  - **Part of the fall is the sector:** Archer, a performing oil-service bond in the same
    funds, fell ~3% in October (−0.17 / −0.13 pp). Borr's own discount is thus ~1–2 points `[A]`.
    On Heimdal's marks the rig loss is a dent, not a solvency event.
  - **Borr's updates** (6-Ks of 29 Oct and 2 Nov `[F]`):
    - the bodies of four people have been recovered and one person is still missing;
    - an independent investigation by a classification society has been engaged;
    - ~280 m³ of marine diesel was on board, and environmental measures have been mobilised.
    - Nothing is said on insurance, the BW Energy contract or the notes. A report that Gabon's oil
      minister ordered a technical investigation is `[E]` (TIKR).
  - **Weights (30 Oct `[F]`):** HH 5.6% (5.36% on 30 Sep; the rise fits no sale while the fund
    shrank ~9%); HH+ 4.4% (4.78%; fits no sale while Pluss grew ~3%) `[A]`. Borr is the second-largest issuer in HH and the fifth in HH+.
  - **Next signposts:**
    - Stressed if a quote or the next contribution puts the notes below 90;
    - Performing again if Borr confirms the hull cover at the agreed value and the notes recover
      to ~par;
    - Vote or standstill on any bondholder notice.
  - **Funds:** named 2027 Base loss HH 0.19, HH+ 0.15 pp (at Stressed, 89: 0.29 / 0.23). Borr
    leaves the performing book, so its share of the Bear catalyst loss must leave the funds' Bear
    catalyst line (~0.07 pp each `[A]`).
- **What it would mean for the funds** `[A]`. The illustration uses a ~4.7-year average life with
  amortisation, NIBOR 4.79, and recovery 55 / 40.

| Borr's first price | Status | Implied PD | Base PD | Loss if default | Named loss 2027: HH / HH+ (pp) |
|---|---|---|---|---|---|
| ~100, with a warning | Watch | 4.5 | 4.7 | 50% | 0.13 / 0.11 |
| 95 | Watch | 8.0 | 6.5 | 48% | 0.17 / 0.15 |
| 85 | Stressed | 16.3 | 13.1 | 43% | 0.30 / 0.27 |
| 70 | Distressed | 33.2 | 26.6 | 33% | 0.47 / 0.42 |

The 25 Oct illustration above uses the 30 Sep weights (5.36 / 4.78). At the 4 Nov value (~93,
Watch) and the 30 Oct weights (5.6 / 4.4): implied PD 9.6, Base PD 7.3, loss if default 47%,
named loss 0.19 / 0.15 pp.

Notes added on 30 Oct (not Bear overrides):

6. **Trustly sits one point below the 80 edge.** In the Stressed band (status value 10%), the
   Base PD would be 19.3 instead of 24.3 and the EL 7.9 instead of 10.0. The mark (79) lies inside
   the bid/offer (76–77 / 80.375), so the band is not settled.
7. **Intrum's recovery is raised from 35 / 25 to 45 / 30** `[A]`.
   - The notes are senior secured exchange notes (SEC Form T-3; Intrum's tender releases), not
     unsecured as the old row assumed.
   - They rank behind the RCF (SEK 5.2bn drawn at 30 Sep; super senior `[A]`) and the new 7% 2031
     notes (EUR 525m; rated B+ against B− for the exchange notes `[E]`; ranking ahead `[A]`). So
     they stay below the secured convention (55 / 40).
   - Asset cover at 30 Sep: portfolio book SEK 23.7bn and servicing EBITDA ≈ SEK 4.1bn (implied
     from servicing leverage 4.5x), against gross borrowings of SEK 39.5bn.
   - At the old 35 / 25: Base PD 20.9, loss if default 64%, EL 13.3% (HH +0.06 pp, HH+ +0.04).
8. **HX SSSN recovery 70 / 50** `[A]`.
   - The bonds rank first, beside the cash management facility and the guarantee tranche, on the
     two hybrid ships (vessel book EUR 322m for four owned ships).
   - The old loan at 12.5 implies the market values the secured assets at about the super senior
     class plus ~12% of the Senior SSNs left behind it (~EUR 175m against a ~EUR 150m class)
     `[A]`.
   - At an assumed price of 90 instead of 96: Base PD 22.0, EL 7.0% (HH and HH+ +0.02 pp each).
     Superseded on 4 Nov by the derived ~84 (note 9).
   - **Kept at 70 / 50 on 4 Nov** `[A]`. At ~84 the rule gives an implied PD of 56%, which mostly
     says that the price doubts the 70 recovery. At the secured convention (55 / 40) the Base PD
     would be 23.7 and the EL 11.1% instead of 9.6% (HH +0.02, HH+ +0.01 pp). The book value of the
     ships, against a ~EUR 150–190m super senior class, still supports 70; the next HX report
     tests it.

Note added on 4 Nov (not a Bear override):

9. **HX SSSN price, derived ~84 (range 79–88)** `[A]`:
   - **The signal** `[F]`: HX contributed −0.49 pp to Høyrente and −0.40 pp to Pluss in October.
     The old loan, now 0.35% and 0.27% at 12.5, lost half its value: ~−0.35 and ~−0.27 pp.
   - **The rest is the SSSNs:** −0.14 pp on ~1.18% of HH's 30 Sep NAV, and −0.13 pp on ~1.03%
     of HH+'s. That is −12% in both funds, and −12.6% in price after one month's accrual of 7%.
   - **From the issue price of 96, that gives ~84.** The range:
     - ~79 if September's HX loss (−0.08 / −0.07 pp) was also on the SSSNs;
     - up to ~88 if Heimdal marked them above 96 at 30 Sep.
   - The move is over 10 points against the assumption. The check is met only by the two funds
     agreeing, which is the same manager's mark, so the status is provisional. It replaces an
     assumed price, not an observed one.
   - **Derived weights at 30 Oct:** HH ~1.16, HH+ ~0.87 (HX 1.83 / 1.58 at 30 Sep, less the old
     loan at 25, after the October fall and the change in fund size).
   - At 79 (Distressed): Base PD 46.0, EL 12.0% (HH and HH+ +0.02 pp each).

## Fund read-out (19 Nov; the values `docs/hy-funds-analysis.md` reads)

**Named loss, 2027 (at-risk bonds; % of NAV or pp)** — weight × PD × loss if default from the
rounded table values. Weights: Fondsfinans 31 Oct holdings `[F]`; Heimdal 30 Oct top 10 and 30 Sep
for the rest; Sissener as in the funds file.

| Fund | At-risk bonds (% of NAV) | **Named 2027 Base** | **Named 2027 Bear** | Largest contributions (Base) | Changed 19 Nov |
|---|---|---|---|---|---|
| FF HY B | 3.8 | **0.34** | **0.90** | Sigma 0.10, Magnolia 0.08, Hofseth 0.07, Foxway 0.07, Heimstaden 0.03 | none |
| FFK B | 1.3 | **0.09** | **0.30** | Hofseth 0.05, Foxway 0.04 | none |
| SIS NOK-R | 14.6 | **1.11** | **2.85** | Hofseth 0.19, Trustly 0.18, Shearwater 0.17, Intrum 2028 0.16, Tullow 0.15, W&T 0.13, Viaplay 0.12 | Intrum 2028 +0.01 |
| HH+ B | 31.2 | **2.07** | **5.26** | Trustly 0.37, Sigma 0.31, Shearwater 0.29, Intrum 0.24, Foxway 0.21, Borr 0.15, Viaplay 0.13, Flora 0.11 | Intrum +0.01 (Bear +0.09) |
| HH N | 30.1 | **2.17** | **5.38** | Sigma 0.43, Trustly 0.38, Intrum 0.36, Shearwater 0.25, Borr 0.19, Foxway 0.16, Flora 0.12, HX SSSN 0.11 | Intrum +0.02 (Bear +0.14) |

- Bear catalyst line (performing book): HH 0.84, HH+ 1.18; FFK 0.62 (q 0.47 on the October rating
  split).
- **November NAV marks** (realised, not named loss): Intrum 73.75 → 68.0 is ~−0.17 pp for HH and
  ~−0.12 pp for HH+ `[A]`; Borr's −9% equity move has no observed note price yet.

**Restructurings in progress (HH and HH+ only)**

| Fund | Weight: 30 Oct → 4 Nov | HX yield removed from carry (pp): 30 Oct → 4 Nov | 2027 Bear on restructurings (pp): 30 Oct → 4 Nov |
|---|---|---|---|
| HH+ B | 0.69 (HX old loan ~0.31 `[A]`, Booster 0.26, Jøtul 0.12) → **0.65** (old loan 0.27 `[F]`) | 0.02 → **0.02** (coupon basis; 0.41 → **0.36** at YTM) | 0.28 → **0.26** (0.46 → 0.42 if the old loan is a total loss) |
| HH N | 0.92 (HX old loan 0.34, Booster 0.30, Jøtul 0.28) → **0.93** (old loan 0.35 `[F]`) | 0.02 → **0.02** (coupon basis; 0.45 → **0.47** at YTM) | 0.37 → **0.37** (0.57 → 0.58 if the old loan is a total loss) |

- **Why the coupon basis:** Heimdal's report footnote says it uses the coupon, not the YTM, for
  bonds priced below 70 while the coupon is paid. No missed payment on the Senior SSNs has been
  found, though the February 2027 coupon may be paid in kind. So the coupon basis (7% × weight)
  is the working value. A YTM of ~133% at a price of 12.5 has no meaning as carry. The YTM basis
  is the skill's conservative default when the basis is unknown, so it is shown as the
  sensitivity.
- The **SSSN's yield (24.6% at ~84) stays in carry**, since it pays cash, and its risk is charged
  in the named loss above. Before 30 Oct, the whole HX position's yield was removed.
- Neither report names Booster or Jøtul in October.

**Marks already in the NAV in October** (realised mark-to-market in the Q4 stub, not part of the
2027 loss; October reports `[F]`, splits `[A]`)

| Fund | October return (class A) | Intrum | HX: old loan / SSSN | Borr | Trustly | Net of these four names |
|---|---|---|---|---|---|---|
| HH | −0.48% | −0.56 | −0.49: ~−0.35 / ~−0.14 | −0.21 | +0.42 | **−0.84** |
| HH+ | −0.14% (swing pricing on the last day) | −0.46 | −0.40: ~−0.27 / ~−0.13 | −0.18 | +0.44 | **−0.60** |
| SIS NOK-R | not read | — | — | — | `[?]` (Sissener's mark not stated) | — |

- **Other named contributors** (HH / HH+): Floatel +0.10 / +0.05, Moreld +0.03 / +0.03, Ellos
  +0.03 / +0.03, DGOC +0.02 (HH), Shearwater +0.03 (HH+); Archer −0.17 / −0.13 (performing; its
  Q3 trading update of 21 Oct: EBITDA $44.2m, exit from new offshore-wind EPC work `[E]`).
- **Class N and B** ≈ class A + 0.0125 pp a month (fee gap 0.15 pp a year): HH N ≈ −0.47%, HH+ B
  ≈ −0.13% `[A]`. Class A NAV 30 Oct: HH 122.83 (123.43 on 30 Sep), HH+ 108.25 (108.41).
- **The 27 Oct day and the week to 29 Oct** (−0.74% and −1.4% for HH N) are now explained by the
  month: the Intrum, HX and Borr marks, Archer and wider spreads, partly offset by Trustly.
- **Swing pricing** was triggered on 27 Oct (HH) and on the last day of October (HH+, report
  footnote: it is corrected at the next NAV). It is technical, not a credit loss.
- **Fund size and flows** `[F]` (flows `[A]`):
  - HH: NOK 8,354m → 7,554m, i.e. ~NOK 760m (~9%) of net redemptions in October.
  - The outflow was met partly from the covered-bond buffer ("Kontanter & IG" 10.6% → 8.8%) and
    partly by trimming bonds. BlueNord left the top 10 (3.5% → below 3.0%), and Flora, Floatel and
    Shearwater were trimmed, judging by their weights.
  - HH+: NOK 3,170m → 3,257m, ~NOK 90m of net subscriptions.
- **Market (both reports):**
  - DNB Carnegie Nordic HY −0.2% in October (YTD +5.6%); Europe −1.1%, US +0.3%.
  - Spreads at end-October: Nordic 4.9% (4.3% at end-Sep), Europe 3.7% (2.8%), US 3.4% (2.9%).
  - Issuance ~EUR 1.9bn in October, EUR 21.1bn YTD. Heimdal joined no new issues.
- **Fund yields** (class A, after fee) `[F]`:

| Fund | End-Aug, in NOK (manager) | 30 Sep, report box | 30 Oct, report box | 30 Oct, "measured in NOK" | Rate / credit duration, 30 Oct (30 Sep) |
|---|---|---|---|---|---|
| Heimdal Høyrente A | 8.9% | 8.0% | 8.78% | **9.60%** | 1.13 / 2.17 (1.17 / 2.18) |
| Høyrente Pluss A | 9.74% | 9.4% | 9.42% | **10.28%** | 1.19 / 2.14 (1.24 / 2.24) |

  - **The report box yield is not the NOK yield.**
    - The October text gives the box figure first and then the yield "measured in Norwegian
      kroner".
    - The gap (0.82 / 0.86 pp) is the hedge pickup on EUR and USD bonds.
    - The September box (8.0 / 9.4) gives no NOK figure. On this evidence it is the same basis.
    - Pluss's end-Aug box (8.41%) against its 9.74% in NOK points the same way.
  - **This contradicts the funds file's checkpoint 1**, closed on 1 Nov as "report yields are in
    NOK". The funds run should reopen it: the HH and HH+ carry would be ~0.8 pp a year higher
    on the NOK basis `[A]`.
  - **What drove the rise** (HH box 8.0 → 8.78% in one month; NOK 8.9% at end-Aug → 9.60%):
    - wider spreads, most of all outside the Nordics (Nordic +60 bp, Europe +90 bp);
    - the price falls on the fund's own names (Intrum, the HX SSSNs, Borr, Archer). Heimdal says
      the weaker period has lifted the yield.
    - It is not new return: the NAV paid for it (−0.48% in October). Pluss's box yield was flat
      (9.4 → 9.42%) while its NOK yield rose 0.54 pp from end-Aug. That is not explained `[?]`.
  - Classes N and B: + 0.15 pp (HH N 8.93% box / 9.75% NOK; HH+ B 9.57% / 10.43%) `[A]`.
  - EUR and USD bonds in the funds are fixed-rate; NOK bonds are floating (manager, 28 Oct).
- **The October anchor spread of 490 bp is at or above the HY Market BBB stale trigger (≥ 480 bp),
  and +60 bp exceeds the 50 bp minimum change.** It belongs to `docs/hy-market-bbb.md`, not here.

**Sensitivities on the 2027 named Base loss (pp)**

| Sensitivity | SIS | HH+ | HH |
|---|---|---|---|
| Trustly in the Stressed band (a price of 80 or more) | −0.04 | −0.08 | −0.08 |
| Intrum at the old recovery 35 / 25 | — | +0.04 | +0.06 |
| Borr Stressed (89) instead of Watch (~93) | — | +0.08 | +0.10 |
| Borr at 96 (top of its range) | — | −0.02 | −0.03 |
| HX SSSN at 79 (Distressed) instead of ~84 | — | +0.02 | +0.02 |
| HX SSSN recovery 55 / 40 instead of 70 / 50 | — | +0.01 | +0.02 |
| HH+ Intrum weight 1.8 or 2.3 instead of 2.0 | — | −0.02 / +0.03 | — |
| HX carry on the YTM basis (removed from carry, not named loss) | — | +0.34 | +0.45 |
| HX old loan a total loss in Bear (Bear, not Base) | — | +0.16 | +0.21 |

## Price history (FX-adjusted; Fondsfinans and Sissener data)

| Company | 31 Dec 2025 | 31 Aug 2026 | 30 Sep 2026 | 31 Oct 2026 | Change since year-end |
|---|---|---|---|---|---|
| Hofseth | 97.9 | 77.0 | 76.2 | 72.8 | −25.1 |
| Magnolia Bostad | 95.0 | 86.4 | 87.3 | 88.0 | −7.0 |
| Flora / Sigma | 87.0 | 81.6 | 80.0 | 79.2 | −7.8 |
| Varel Oil & Gas | 87.25 | 89.9 | 89.5 | — (left the list) | +2.3 (Sep) |
| Foxway | 74.65 | 96.3 | 96.0 | 93.7 | +19.0 |
| Floatel | 93.5 | 104.9 | — | — | +11.4 (Aug) |
| Norske Skog | 92.5 | 103.2 | — | — | +10.7 (Aug) |
| Tullow | 73.5 | ~88 (Feb) | — | — | ~+15 (Feb) |
| Shearwater | 83.0 | ~86 (Feb) | — | — | ~+3 (Feb) |

**October 2026 marks** (added 30 Oct, extended 4 Nov; fund marks are manager statements `[E]`,
clean `[A]`; October contributions from the reports `[F]`; derived prices `[A]`):

| Bond | Earlier evidence | 30 Sep (derived from the October contribution, unless stated) | Latest (date; basis) | Cross-check |
|---|---|---|---|---|
| Intrum 8.5% 2030 (Heimdal) | Issuer's own 30 Sep fair value of all its bonds: 95.2% of nominal (Level 1) `[F]`; 80 (Heimdal, 23–26 Oct) | ~93 (HH −0.56 pp on 2.77%, i.e. ~−20% in the month) | **73.75** (27 Oct; fund mark) | Trades 75–77 on 26 Oct `[E]`; exchange quotes 73.25 (2030) and 76.59 (2029), undated, read 30 Oct `[E]`; the 7.75% 2027 stub at 96.4 and the 7% 2031 at 83.8. HH+ −0.46 pp on 1.82% (−25%) does not fit the same note and weight `[?]` |
| Trustly FRN 2030 | 75.50 (Sissener's purchase, mid-June) `[F]`; Heimdal's Sep contribution +0.06 / +0.07 pp (part of August's fall won back) | ~70 (+0.42 / +0.44 pp, i.e. ~+13% incl. the 8 Oct coupon) | **79** (~30 Oct; fund mark; the reports confirm the rise) | Bid 76/77 for size, not filled; offer 80.375 for 400k; no trade `[E]`. Gettex 71.71 (undated) now fits the 30 Sep level |
| HX old 2030 loan | Whole HX position ~50–60 (Heimdal contributions, Sep) | 25 (stated) | **12.5** (~27 Oct; fund mark after a small third-party trade; both reports `[F]`) | Single source; the NAV moves fit |
| HX SSSN 2028 | 96 (issue price, 21 Aug) `[F]` | ~96 (assumed) | **~84** (30 Oct; derived, range 79–88; note 9) | No trade or quote seen |
| Borr 2032/2034 | Par assumed (issue, 2026); September −0.18 / −0.16 pp (≈ −4%, US rates) | ~96–98 (if par to 102 at end-Aug) | **~93** (30 Oct; derived, range 91–96; note 5) | No trade or quote seen. Archer −3% in the same month: part of the move is the sector |
| Sigma Holdco 2031 | 80.0 (30 Sep, FF) | — | **79.2** (31 Oct; FF holdings) | Inside Heimdal's October bound (~76–80.5) |
| Foxway 2028 | 96.0 (30 Sep, FF) | — | **93.7** (31 Oct; FF holdings) | Heimdal's contributions implied ~95 |
| Shearwater 2029 | ~86 (Feb, stale); Sep +0.06 / +0.09 pp | — | October ~flat (HH +0.01, HH+ +0.03 pp) | Year-to-date contributions (HH 0.67, HH+ 0.60) point to ~88–93 against 83.0 at end-2025, depending on the weight path `[A]`; not applied |

- The Intrum and Trustly moves exceed 10 points against the old assumed prices. Each is confirmed
  by a second source (trades or quotes), as the skill's plausibility check requires. The HX old
  loan rests on Heimdal's mark alone, but it is the value inside the fund.
- The HX SSSN move (~12 points) rests on the two funds' contributions only, which are the same
  manager's mark. It replaces an assumption, so it is applied, but it is labelled derived and
  provisional. Borr's move is below 10 points.
- Hofseth fell from 97.9 to 76 in nine months. A bond that looks performing today can be at risk
  within a year. That is why the funds carry a residual for defaults not yet visible from 2028,
  and why the 2027 zero is now shown as a sensitivity (skill F4 item 5).

## Stamdata and news screen, held companies

Scan coverage: Stamdata news read page by page 14 Oct–19 Nov 2026 (19 Nov run; earlier held-company
window 4 Aug–23 Oct), plus company reports, 6-Ks and press for the watchlist names.

| Company | Notice or news | Date | Reading |
|---|---|---|---|
| HX | Written resolutions adopted (two secured bonds, EUR 388m). **Terms read 30 Oct** (HX investor page: summonses, term sheet, outcome notices `[F]`): EUR 19.9m of new 7% super senior bonds at 96, maturing 30 Jun 2028 at 104; a 3-for-1 roll-up of Senior SSNs; a EUR 10.2m contingent tap before the February 2027 coupon; a guarantee tranche of up to EUR 20.3m for Hurtigruten; a Junior SSN tap of EUR 4.46m at 65; the free-liquidity floor cut to EUR 10m until 31 Mar 2027. New money settled ~21 Aug and the roll-up ~26 Aug. **H1 report (28 Aug):** material uncertainty on going concern; funding needed in Q2 2027. **Heimdal (28 Oct):** old 2030 loan marked 25 → 12.5 | 29 Jul–17 Aug; 28 Aug; 28 Oct | In restructuring (distressed amendment: the Senior SSNs that did not roll up were primed). Split into the old loan and the SSSNs |
| Intrum | **Q3 report** `[F]`: net loss SEK 1,487m incl. a SEK 1,517m goodwill impairment (Germany); External servicing income for 2026 now seen below 2025; adjusted EBIT SEK 976m (1,234). Balance sheet better after the July steps: SEK 7.5bn capital raise and SEK 2.5bn in cash from the sale of a portfolio associate (to Brocc; "Orange" in the notes); servicing leverage 4.5x (5.7x end-2025); net debt / cash EBITDA 4.1x; net debt SEK 37.2bn; RCF drawn SEK 5.2bn (11.9); cash SEK 2.9bn. The EUR 525m 7% 2031 notes refinanced the 8% New Money Notes (July). EUR 200m of 7.75% 2027/2028 notes were bought back in September. Debt matures 2027–2031. Shares −39% intraday (register `[E]`). Heimdal marked its 8.5% notes 80 → 73.75 on 27 Oct and bought more | 23 Oct; 27–28 Oct | Distressed (price). It is not a payment or covenant event, and liquidity is adequate. The risk is a second restructuring if servicing income keeps falling and the 2027 cost plan (total costs toward SEK 11bn) fails. Next: Q4 report 4 Feb 2027 |
| Trustly | **Q2 report** `[F]`: revenue SEK 634m (+6%); adjusted EBITDA SEK 42m (85), hit by higher US loss rates after looser risk rules; loss SEK 218m in Q2 and SEK 359m in H1; cash SEK 193m at 30 Jun (444 at end-2025); a RCF agreed in March 2026 (EUR 4.5m drawn in July). **2 Oct:** binding commitments for >USD 40m of new equity from Nordic Capital and Alfvén & Didrikson, closing in November `[E]` (Placera). **Mid-June:** Sissener bought the bond at 75.50 (spread just under 1,500 bp) after a weak Q1 `[F]` (Sissener's June report via Placera). **~30 Oct:** Heimdal marks it at 79 `[E]` | 27 Aug; 2 Oct; Jun; 30 Oct | Distressed (price). The owners are adding equity, which supports the bond. On the bond alone, leverage is very high: EUR 375m ≈ SEK 4.1bn against adjusted EBITDA of SEK 267m (H1 annualised) or SEK 169m (Q2 annualised), i.e. ~15–24x `[A]`. Next: equity closing (Nov) and the Q3 report (25 Nov) |
| Heimdal Høyrente and Høyrente Pluss | **October reports** `[F]`: returns −0.48% / −0.14% (class A); contributions Trustly +0.42 / +0.44 (rose on the main owners' commitment of new equity), Intrum −0.56 / −0.46 (weak Q3; Heimdal sees an overreaction and increased the position), HX −0.49 / −0.40 (old 2030 loan 25 → 12.5 after a small trade; now 0.35% / 0.27%; the rest of the exposure sits in debt with better priority), Borr −0.21 / −0.18, Archer −0.17 / −0.13. Top 10 at 30 Oct: HH Archer 6.0, Borr 5.6, Floatel 4.2, Kistefos 4.2, European Energy 4.2, Flora 4.1, Trustly 3.8, Sigma 3.7, Shearwater 3.3, Intrum 3.0; HH+ Archer 6.7, Agilyx 6.1, Floatel 5.9, European Energy 4.6, Borr 4.4, Kistefos 4.1, Flora 3.8, Shearwater 3.8, Trustly 3.7, Neo Bidco 3.4. Fund size HH NOK 7,554m (8,354), HH+ 3,257m (3,170) | 30 Oct (published early Nov) | Borr → Watch; HX SSSN → Stressed; Intrum, Trustly and HX old-loan marks confirmed; Trustly rose in October. No new name in trouble is named: the negative list is the known names plus Archer |
| Borr Drilling | **6-Ks of 29 Oct and 2 Nov** `[F]`: three, then four bodies recovered; one person still unaccounted for; an independent root-cause investigation by a classification society; ~280 m³ of marine diesel on board, environmental measures mobilised with the customer and authorities. Nothing on insurance, the BW Energy contract, the notes or the Q3 date. Gabon's oil minister reportedly ordered a technical investigation `[E]` (TIKR) | 29 Oct; 2 Nov | Watch from 4 Nov on the price signal (note 5). The fatalities and the diesel on board widen the liability and regulatory questions; the insurance statement is still missing. Next: Q3 report (~18 Nov `[E]`) |
| Archer | Q3 trading update `[E]` (search summary, not read in full): EBITDA $44.2m, margin 16.5%, revenue $267.6m, incl. ~$3m from a Norwegian offshore strike; stops pursuing new offshore-wind EPC projects and explores a sale of Archer Wind. Bond −0.17 / −0.13 pp in October in Heimdal (~−3% in price `[A]`) | 21 Oct | Performing kept (price still above par `[A]`). The cause of the October fall is not stated `[?]` |
| Borr Drilling (BW Energy) | **BW Energy Q3 report** `[F]`: MaBoMo Phase 2 delayed by the rig loss, "too early to confirm when drilling will resume"; workover with a hydraulic unit instead; already searching for a new rig for Bourdon; MaBoMo production resumed 28 Oct | 29 Oct | No replacement Borr rig named. Performing kept, provisional (note 5) |
| Booster Precision | Events of default; written procedure; standstill prolonged (again 2 Nov) | 3 Sep, 22 Sep, 1 Oct, 2 Nov | Default; no terms yet |
| Jøtul | Intended recapitalisation, new bonds offered; resolution adopted; Recovery Holdco annual report 2025 (11 Nov); Q3 investor call (18 Nov) | 17 Aug–18 Nov | Recapitalisation (distressed); no price |
| Intrum | Tender results: €100m bought below par (2028 SEK 84.26, 2029 EUR 79.43, 2030 68.00) | 9–10 Nov | Price signal; Distressed kept |
| Hofseth | Q3: revenue −46% on lost processing contracts (Salmon Business `[E]`); NOK 600m raise still open | 16 Nov | Negative; Distressed kept, Bear override kept |
| Convene | Written resolutions with a new-money subscription | Sep | Recapitalisation; FTD `[?]` |
| Eldorado Drilling | Bond terms amended | 29 Sep | Purpose not read `[?]`; the September contract news is positive → performing |
| Kistos | Written resolution summoned; adopted with a 0.10% amendment fee | 6 Oct (read 17 Oct); adopted 20 Oct | Routine: escrow waiver for the Block 9 deal, with a first-priority pledge for bondholders. Closed |
| Ocean Yield | Approval of A.P. Møller Holding as equity investor | Aug | Routine, credit-positive |
| Kistefos | Bond terms aligned with KIST13, for a fee | Aug (withdrawn 1 Sep, revised) | Routine |
| Hofseth | NOK 600m equity raise pushed to year-end (news, not a notice). **4 Nov check** (web search): no equity raise, bondholder notice or covenant news since; the 7 Nov step of the value-adjusted equity ratio covenant (25 → 27.5%; first test 31 Dec) has not passed yet | Sep–Oct; 4 Nov | Keeps it Distressed; the Bear override rests on it. Status only: re-check after 7 Nov and at FF's October holdings |
| Elcano | Sold its loss-making LNG ship and repaid the lease on it (news); EGM held 18 Nov on "the completion of the Corporate Refinancing Transaction" (Stamdata, 19 Oct) | Oct; 18 Nov | Credit-positive; performing (FF, FFK) |
| Borr Drilling | **Jackup Prospector 5 (2014, F&G JU-2000E, high-spec) sank on the Dussafu licence, Gabon**, at 20:37 local time on 24 Oct. It lost stability while jacking up for BW Energy's drilling campaign; the preliminary cause is a punch-through during preload. Of 115 people on board, 110 were accounted for and 5 were still missing on 25 Oct; the search was ongoing. BW Energy shut MaBoMo production as a precaution and reports no damage to the facility and no discharge `[F]`. Sources: BW Energy release (MFN, 25 Oct); Reuters; Offshore Energy (25 Oct, quoting Borr). **No Borr release has been found on EDGAR (last 6-K 16 Oct), on Newsweb (in the Nordic Financial database) or on borrdrilling.com** `[?]`. **No news report mentions insurance.** **Insurance** (20-F 2025) `[F]`: hull and machinery cover on the whole fleet at each rig's agreed value, less a deductible. Loss-of-income cover applies only "for certain rigs" (whether Prospector 5 has it `[?]`). P&I covers crew injury and death and third parties. **Collateral** (H1 2026 report) `[F]`: all 29 rigs are pledged, with a book value of $3,036.5m (≈ $105m a rig). The new notes are secured "by most of the rigs", on the same security as the $250m super senior RCF and the $45m guarantee facility. Three of the five ex-Noble rigs secure the $150m seller's credit. Prospector 5 (an original Borr rig) is very likely in the notes pool `[A]`. The indenture (144A) is not public, so its event-of-loss and insurance-proceeds clauses are `[?]`; market practice is to apply the proceeds to prepay debt or replace the collateral `[E]`. **Collateral coverage:** one rig of 29 is ~3–4% of the pledged book. On values, Rig BBB's Base value for a 12-year-old high-spec jackup is $42m, and 2026 transactions were $57–72m a rig. Hull proceeds at an agreed value near book would exceed that, so collateral coverage falls only if the cover fails or is short `[A]`. **Liquidity:** cash $223.6m plus the undrawn $250m RCF = $473.6m (30 Jun). The BW firm term ran to Jul 2027; ~270 days lost cost roughly $15m of EBITDA at ~$125–134k a day less $75k opex `[A]`, unless loss-of-income cover applies or another rig replaces it. The coupon of ~$110m falls due on 15 Jan 2027. The deductible, wreck removal and investigation costs are `[?]` | 24–25 Oct | **Performing kept, provisional** (note 5). The event is operational and not a payment or covenant event. The collateral loss is small and probably insured. The human loss and possible liability, regulatory and contract consequences in Gabon are not yet known. The first bond price (26 Oct) and Borr's own statement on insurance decide the status |
| Havila Shipping | Lost to DNB, Danske Bank and Swedbank on the 2020 restructuring agreement: Oslo District Court 8 Dec 2025, Borgarting Court of Appeal 19 Oct 2026 (Havila's refinancing of lenders who elected settlement on 30 Dec 2024 breached the agreement). Appeal to the Supreme Court; deadline 19 Nov 2026 `[F]`. Banks' claim (Dec 2025): NOK 130.8m interest-bearing, NOK 595.1m non-interest-bearing B tranche (nominal), NOK 7.9m interest; they seek to enforce security on Havila Foresight and Havila Harmony `[E]`. Finansavisen 21 Oct: "Havila Shipping i dobbel millionskvis" (paywalled; headline only) | 8 Dec 2025, 19 Oct 2026 | Bank debt, no bond named. Distressed at equity and vessel level; no bond loss for the funds unless a Havila bond is still held (FF had only a converted or legacy stub at end-2025, below 80). Not on the watchlist |

Market-wide hits that are not held (19 Nov scan: North Investment Group and Achilles Capital events of default, Proximar Seafood non-payment, Magle Chemoswed PIK and written procedure, Konzmann and Engebø written resolutions, Brödernas written procedure, Calligo write-down, Caybon interest deferral; earlier: Cabonline, Catena Media, Taptravel, Dooba, Point Properties,
SIBS, Caybon, Solteq and others) go to the default log in `docs/hy-market-bbb.md`.

## Data gaps

1. **Stale and assumed prices.** Share of each fund's 2027 named loss that rests on them `[A]`
   (4 Nov; Borr and the HX SSSN now carry prices derived from Heimdal's October contributions):

| Fund | Named loss 2027 (9 Nov) | On a current price (31 Oct holdings, or a late-Oct mark) | Derived from Heimdal's October contributions | On a stale or assumed price | Share stale or assumed: 9 Nov (4 Nov) |
|---|---|---|---|---|---|
| FF HY | 0.34 | 0.34 | 0 | 0 | 0% (0%) |
| FF Kreditt | 0.09 | 0.09 | 0 | 0 | 0% (0%) |
| Sissener | 1.10 | 0.37 (Hofseth, Trustly) | 0 | 0.73 (Shearwater, Tullow, W&T, Viaplay; Intrum 2028 assumed) | 66% (59%) |
| Høyrente N | 2.15 | 1.31 (Sigma, Trustly, Intrum, Foxway) | 0.30 (Borr, HX SSSN) | 0.53 (Shearwater, Flora, Viaplay, Convene, Norse) | 25% (27%) |
| Høyrente Pluss | 2.06 | 1.12 (Trustly, Sigma, Intrum, Foxway) | 0.23 (Borr, HX SSSN) | 0.70 (the same five names) | 34% (36%) |

   Rounding: parts may differ from the totals by 0.01. FF's 31 Oct holdings (read 9 Nov) replace the 30 Sep prices.
   Heimstaden's yield is assumed (the hybrid's call terms were not read), its price is observed.
   Varel's exit is inferred from the lists and is not confirmed.
   Next steps (data work, not done in this update):
   - FF's November holdings (early Dec): Varel's exit, Sigma, Hofseth, Magnolia,
     Foxway;
   - Sissener's semi-annual report at 30 Jun 2026 for every
     Sissener price;
   - a quote for the Borr 2032/2034 notes and the HX SSSNs (both derived only);
   - Heimdal's November reports (~early December) and the 30 Oct holdings page (all weights);
   - a public price page for the W&T and Tullow ISINs.
2. **HX** (the terms were read on 30 Oct; still open):
   - which bond is "the old 2030 loan": the Senior SSN stub (most likely `[A]`) or the Junior
     SSNs;
   - an observed SSSN price (~84 derived on 4 Nov, range 79–88). Whether September's −0.08 /
     −0.07 pp was already on the SSSNs decides the low end. Also the final SSSN and roll-up
     amounts;
   - HH+'s split. Its old loan is now stated (0.27%); the SSSN weight is derived;
   - whether the August 2026 Senior SSN coupon was paid in cash, which decides the carry basis;
   - the date of HX's Q3 report.
3. Bond terms (coupon, maturity, security, call schedule) for the names marked `[?]`, especially
   BlueNord's call schedule, which decides its yield. BlueNord left HH's top 10 in October (3.5%
   → below 3.0%), probably sold into the outflow `[A]`.
4. The purpose of the Eldorado amendment (Kistos closed on 17 Oct: routine).
5. EHAB: weight and price at FF, so it can enter FF's named loss.
6. Convene: whether the September recapitalisation counts as a first-time default.
7. Sissener positions beyond the top 10 (Viaplay's weight is the end-2025 figure).
8. Havila Shipping: whether FF's end-2025 stub is a bond or shares, whether it is still held at
   30 Sep, and whether any Havila bond is outstanding (Stamdata). If a bond is held, it enters the
   watchlist as Distressed or In restructuring. Also unread: the stock exchange notices of 1 Apr
   and 30 May 2026.
9. **Borr Drilling** (25 Oct; updated 4 Nov) `[?]`:
   - Borr's statement on Prospector 5's insurance: the agreed hull value, loss-of-income cover and
     deductible. None in the 6-Ks of 26 Oct, 29 Oct and 2 Nov;
   - the event-of-loss and insurance-proceeds clauses in the 2032/2034 indenture, and whether
     Prospector 5 is in the notes pool;
   - an observed bond price. The ~93 is derived from Heimdal's contribution, and the end-Aug and
     30 Sep levels are not known;
   - liability and environmental costs (four dead, one missing, ~280 m³ of diesel on board);
   - whether BW Energy keeps the campaign with a replacement Borr rig. Answered in part on 29 Oct:
     BW names no replacement and is searching for a new rig.
10. **Intrum** (30 Oct; updated 4 Nov) `[?]`:
    - which 8.5% note Heimdal holds (the 2030 note is assumed; the 2029 note quotes ~3 points
      higher);
    - **HH+'s note and weight.** Relative to its 30 Sep weight, Pluss lost more on Intrum than
      Høyrente in both months: September −0.08 pp on 1.82% (Høyrente's was too small to be named)
      and October −0.46 pp (−25%, against −20% in Høyrente). So Pluss holds a longer note or more
      than 1.82% `[A]`. After its October purchases it is assumed ~2.0% (range 1.8–2.3);
    - the dates of the exchange quotes;
    - the intercreditor ranking of the RCF and the 7% 2031 notes against the exchange notes (not
      read; the recovery of 45 / 30 rests on it).
11. **Trustly** (30 Oct; updated 4 Nov) `[?]`:
    - answered 4 Nov: the mark moved up during October (+0.42 / +0.44 pp), from ~70 at 30 Sep
      `[A]`;
    - the size of the super senior RCF;
    - Sissener's current mark.
12. **Heimdal weights after the October outflow** (added 4 Nov) `[A]`:
    - HH shrank ~9% through redemptions. Positions it did not sell rose ~10% in weight.
    - Only the top 10 are stated at 30 Oct. Foxway, Viaplay, Convene and Norse are still at 30 Sep
      (about +0.03 pp of named loss if they were not sold).
    - The 30 Oct holdings page (heimdalfondene.no) would settle it.

## Change log

- **26 Nov 2026 — event update** (skill 2026-11-18.2): Norse Atlantic **Watch → Deep distress** (25 Nov: "critical", Recovery Box, flights stopped `[E]`); the USD 52m 15% secured facility marked ~95 → ~40 assumed (20–60), Base PD 75%, Base −18%, Bear −69%; expected NAV mark HH ~−0.46, HH+ ~−1.22 pp. Heimdal weights to the 30 Oct holdings pages. Named 2027 Base HH 2.17 → 2.26, HH+ 2.07 → 2.44. Trustly Q3 read: Distressed kept (79). Recorded and committed from the user's session (the daily run stopped before recording).
- **19 Nov 2026 — full refresh and compaction** (skill 2026-11-18.2): Intrum re-marked on its 10 Nov tender (8.5% 2030 → 68.0; 7.75% 2028 → ~84.3); Borr Q3 and Hofseth Q3 read, statuses kept; Stamdata screen 14 Oct–19 Nov; dated notes removed (git keeps them), fund read-out reduced to current values; 990 → 670 lines.
- **9 Nov 2026** (skill 2026-11-08.1): Fondsfinans' October report and 31 Oct holdings: Sigma → Distressed (79.2), Hofseth ~72, Foxway 93.7, Magnolia 88.0, Heimstaden hybrid new (84.7, Stressed), Varel out.
