# Nordic HY Market BBB — 5 November 2026 (note 11 Nov: kept unchanged)

## Note, 11 Nov 2026 — HY Market BBB kept unchanged

Small update (skill `hy-market-bbb` **2026-11-08.1**; `iaf-valuation` 2026-11-10.1, time grid
only). Causes from the update chain: Taptravel's bondholder vote (9 Nov), SSB October CPI
(10 Nov), Riksbank minutes (10 Nov). Also read: Oil Market BBB of 11 Nov and DNB's Capital
Markets Day (10 Nov). **No value other documents read moves**: the NIBOR path, GDP, spreads,
default rates, market return and the reference E / R stay as on 5 Nov.

| Input | Finding | Against Base / the threshold | Effect |
|---|---|---|---|
| **SSB CPI, October** (table 14706, published 10 Nov 08:00) | CPI **3.6%**, CPI-ATE **2.7%** (12-month; Sep 3.4 / 3.0) `[F]` | Norges Bank MPR 3/26 projected **3.8 / 2.7** for October (Table 2a): CPI-ATE exactly on path, CPI 0.2 pp below. Stagflation signpost (CPI-ATE > 3.3%) not hit; Bull signpost (< 2.5%) not hit | None. Nothing here for MPR 4/26 to raise the path on; the weaker krone since 5 Nov (I-44 107.76 → 109.57, 10 Nov) leans the other way. NIBOR path kept |
| **Riksbank minutes** (meeting 3 Nov, decision 4 Nov; published 10 Nov) | Unanimous hike to 2.00%. All five members expect the rate to be raised further over the coming year in line with the September path: Jansson reads that as "just under two further increases", with timing open and possibly a little faster; Thedéen expects them "over the coming six months or so" if no major surprises; Bunge flags a risk from household rate sensitivity, AI-related credit risk and rising credit spreads `[F]` | On the Riksbank's own path (~2.4% by Q3-27 `[E]`), as read on 5 Nov | None. No Swedish row moves; SEK hedge carry ~+2.65 pp kept |
| **Taptravel vote** (closed 9 Nov) | Both written procedures **approved** (quorum met; ≥ 66⅔% in favour). The changes take effect only when the conditions precedent are met: a share issue of ≥ SEK 50m (Ridge Capital, ≥ 80% ownership after) by a **31 Mar 2027 longstop** (failure = event of default; the company sees bankruptcy as likely if the issue fails). Senior bonds 8% PIK from 3 Oct 2026, maturity 2028 → Apr 2030; super senior 6% cash + 4% PIK, maturity 2028 → Dec 2029; deferred interest paid in cash by 31 Mar 2027 `[F]` | A distressed amendment on an issuer whose first default was July 2026: **no new FTD** (re-default is not counted again). Volume tiny (super senior ≤ SEK 124m) | None. Log and watchlist updated; status stays In restructuring |
| **Oil Market BBB, 11 Nov** | Base Brent 2027 **88 → 84**; 2028–29 (77 / 72), mid-cycle (70), Bear (65 / 60 / 60) and Bull unchanged | E&P row: Base FTD 3.0% comes from small single-asset issuers, not price. Base 2027 at 84 is still $14 above the oil mid-cycle and $19 above the Bear 2027 level where this baseline puts borrowing-base and refinancing stress; the change is far below the 2.0 pp sector minimum. **The oil agent's "not material for HY" holds** | None. Text updated (E&P, scenario table, Brent signpost). The stagflation side case loses a little more support (lower front, Base 84) |
| **DNB Capital Markets Day** (10 Nov; as briefed, not confirmed in a primary source here `[E]`) | DNB Carnegie: policy rate settles at **4.00%** after two cuts in H2 2027; mainland GDP ~**1.5%** a year to 2030 | Implied 3M NIBOR ≈ 4.6 / 4.25 / 4.25 (2027–29, +0.25 premium `[A]`) vs Base **4.79 / 4.39 / 3.86**: −0.2 / −0.15 / +0.4 pp. GDP +0.5 / +0.5 / +0.2 pp above Base (1.0 / 1.0 / 1.3). One house's view: not a Norges Bank, SSB or Riksbank forecast, so not a trigger | None. Recorded as a cross-check for MPR 4/26 (17 Dec): one house sees earlier cuts but a higher floor than Norges Bank |
| Market path check (zero curve, 10 Nov) | 1-year forwards 4.68 / 4.44 / 4.27 + NIBOR–T-bill ~0.28 `[A]` = **~4.96 / 4.72 / 4.55** `[F/A]` | Gap to Base +0.17 / +0.33 / +0.69 pp (4 Nov: +0.17 / +0.33 / +0.71) | None; re-test on MPR 4/26 (checkpoint 13) |
| Fondsfinans October report (read in `docs/hy-funds-analysis.md`, 9 Nov) | DNB Carnegie Nordic spread ~+50 bp in October `[E]` | In line with Heimdal's 490 anchor; the ≥ 50 bp gap trigger did not fire | None; checkpoint 4 partly closed (direction agrees; level not printed) |

- **Register:** `--changed no`; `--affects none`. Stale after **5 Dec 2026** is kept (30 days from
  the 5 Nov update, before MPR 4/26 on 17 Dec). Earlier-stale triggers still open: the November
  anchor spread (early Dec) ≥ 50 bp from 490; a rig or supply full update whose downstream note
  flags a change for the Oil Service row.

## Change summary, 5 Nov 2026 (values other documents read)

**HY Market BBB changed: spreads and expected returns re-marked; the NIBOR path, GDP and default
rates are kept.** Trigger: the October anchor spread (490 bp) hit this baseline's re-mark trigger
(≥ 480 bp), plus the Norges Bank (5 Nov) and Riksbank (4 Nov) decisions.

| Value read by other documents | Before (5 Oct values, kept to 4 Nov) | After (5 Nov) | Why |
|---|---|---|---|
| **NIBOR path** Base, 3M annual avg (stub / 2027 / 2028 / 2029; mid-cycle) | 4.80 / 4.79 / 4.39 / 3.86; 3.45 | **unchanged** | Norges Bank held 4.50% and saw no material change in the outlook since the September MPR. Bear and Bull paths unchanged |
| Policy rate Base (stub / 2027 / 2028 / 2029) | 4.51 / 4.55 / 4.20 / 3.65 | **unchanged** | As above. Market path +0.17 / +0.33 / +0.71 pp above Base (4 Nov): narrower than on 22 Oct, so Base keeps the Norges Bank path until MPR 4/26 (17 Dec) |
| **Nordic GDP** Base (Norway mainland 2026–29; Sweden) | 0.9 / 1.0 / 1.0 / 1.3; Sweden 2.8 / 2.4 / 1.3 / 1.6 | **unchanged** | No new GDP release (SSB next 26 Nov); Sweden Q3 +0.4% q/q in line with the Riksbank. Unemployment paths unchanged |
| **Nordic HY spread** Base, annual avg (stub / 2027 / 2028 / 2029; mid-cycle) | 430 / 440 / 460 / 470; 500 | **490 / 490 / 490 / 495; 500** | October anchor 430 → 490 bp (+60, above the 50 bp minimum). The start is now at the normal level, so the drift toward normal is complete |
| Spread year-end Base (2027 / 2028 / 2029) | 450 / 465 / 475 | **490 / 495 / 500** | Same |
| Spread Bear / Bull 2027 avg (year-end levels kept) | 650 / 410 | **680 / 440** | Mechanical: the higher start feeds the 2027 average. Bear YE-27 850 and Bull YE-27 390 kept |
| **Default rates** (FTD Nordic HY, Base 2027 / 2028 / 2029; Bear peak; LGD) | 3.0 / 3.5 / 3.5; Bear 8.6; LGD 55% | **unchanged** | Four more 2026 FTDs logged (Achilles, Calligo, Caybon, Proximar), but the pace over the market-wide window (1 Sep–5 Nov) is ~2.2% a year, inside Base |
| **Expected NOK return**, Nordic HY Base (stub / 2027 / 2028 / 2029 / window) | 1.9 / 7.0 / 6.7 / 6.4 / 6.8 | **1.1 / 8.0 / 7.2 / 6.8 / 7.2** | October returned −0.2% instead of the ~+0.6% expected (carry less EL) (stub); the wider spread pays ~0.5 pp more carry a year from 2027 and no longer drifts wider (MTM ~0 instead of −0.5) |
| Expected return Bear / Bull (2027; window) | −2.2 / 8.9; 5.6 / 7.4 | **−0.4 / 10.7; 6.0 / 7.7** | Same start effect: less widening to the Bear peak, more tightening to the Bull trough |
| **HY market reference E / R** (fund rule) | E 1.82 / R 9.28 = **0.196** | E 2.15 / R 8.47 = **0.254** | Window excess 2.4 → 2.75 pp; Bear 2027 less negative. Sensitivity: Bear read as a shock (+420 bp from the start, YE-27 910) gives R 9.97 and **0.216** |

- **Register:** `--changed yes` (spreads, expected returns and the market reference moved). Fund
  analyses must re-run on the new reference; the user has put that run on hold until the Sissener
  and Fondsfinans October reports (~10 Nov).
- **4 Nov 2026 (carried, now applied):** Rig Market BBB small update of 4 Nov: drillship Base
  2027 $400k → $420k (MCU 91% kept). The Oil Service row text now reads $420k / 91%; its default
  rates do not change.

## Metadata

- **Analysis date:** Thu 5 Nov 2026, evening, Europe/Oslo. Information cut-off 5 Nov 2026 20:00
  (Norges Bank decision 5 Nov 10:00; Riksbank 4 Nov; Norges Bank market data to 4 Nov, FX to
  5 Nov; FRED HY OAS and SOFR to 4 Nov; Stamdata news to 5 Nov).
  - **Status: Update — HY Market BBB changed (Final).** Spreads, expected returns and the market
    reference are re-marked; the NIBOR path, the GDP view, default rates, LGD, scenario
    definitions, weights and mid-cycle values are kept. Details in the change summary at the top
    and the change log (5 Nov entry).
  - **11 Nov note (kept unchanged):** October CPI, the Riksbank minutes, Taptravel's vote, the
    oil BBB of 11 Nov and DNB's CMD read; no value moves (note at the top). Skill 2026-11-08.1.
  - **Trigger:** the October anchor spread (490 bp, Heimdal, 30 Oct) hit the ≥ 480 bp re-mark
    trigger set on 24 Oct, plus the Norges Bank rate decision (5 Nov) and the Riksbank decision
    (4 Nov). The user asked for the update "based on the rate decisions".
  - The initial baseline's three weaknesses remain: the 2026 default log is incomplete for H1
    (this run found two more H1/July FTDs, Achilles and Calligo), the anchor spread series starts
    in Aug 2025, and watchlist volumes are mostly `[?]`.
  - **Amended 24 Oct (later):** the Oil Service Base default row was aligned with the rig and supply
    baselines (2028–29: 2.0 / 2.5 → 1.5 / 1.5; Bull 1.0). See the change log.
- **Skill revisions:** `hy-market-bbb` **2026-10-24.1** (unchanged since the last run);
  `iaf-valuation` **2026-11-01.1** (time grid and scenario convention only; 2026-10-18.2 on 24 Oct).
- **Previous baseline:** 24 Oct 2026 (12 days; kept unchanged 24 Oct and 4 Nov; values as 5 Oct).
  Window: stub Q4-26 + 2027–2029 (T = 3.24 years from 1 Oct).
  - **Stale after 5 Dec 2026** (30-day rule; it comes before Norges Bank's MPR 4/26 on **17 Dec**,
    which needs a full run in any case), or earlier on any of:
    - the Fondsfinans October report (~10 Nov) if DNB Carnegie's October spread differs from
      Heimdal's 490 by ≥ 50 bp, or the November anchor print (early Dec) moves ≥ 50 bp from 490;
    - an Oil Market BBB follow-up (7 Nov) or a rig or supply full update (due by ~9–12 Nov) whose
      downstream note flags a change for the energy rows;
    - SSB CPI for October (10 Nov) with CPI-ATE ≥ 3.3% (the stagflation signpost).
- **Upstream baselines used:**

| Baseline | Date | Status | Stale after | Used for | HY reading this run |
|---|---|---|---|---|---|
| Oil Market BBB | **11 Nov 2026** (read in the 11 Nov note); before: 31 Oct 2026, update 4 Nov | Final | 30 Nov 2026 | E&P row; scenario mapping (Bear = oil Bear, Bull/Base = oil Base); stagflation test = oil Bull | **11 Nov: Base 2027 88 → 84**; 2028–29, mid-cycle, Bear and Bull unchanged; its downstream note for HY: no action (E&P still far above breakeven), checked and agreed in the 11 Nov note. 4 Nov reading: paths and mid-cycle unchanged (Brent Base 88 / 77 / 72); stub 110.4 → 104.3. Downstream note for HY: "no path change"; the Q4 inflation channel is a little weaker; the Bear catalyst (a deal) is closer after the Democratic sweep (Congress seated 3 Jan); the Bull window runs mainly to 3 Jan |
| Rig Market BBB | 10 Oct 2026 (small updates to 4 Nov) | Final; a full update is due by 9 Nov | 9 Nov 2026 | Oil Service row (drillers) | **4 Nov: drillship Base 2027 $400k → $420k, MCU 91% kept**; NCS HE semis, jackups and 2028–29 kept. Firmer for drillers; no default-row change (below the 2.0 pp sector minimum) |
| Supply Market BBB | 17 Oct 2026 (small updates 28 Oct, 4 Nov) | Final; two triggers fired, full update due | 9 Nov 2026 | Oil Service row (OSV, subsea) | Paths kept; NS AHTS spot weak in October (£43.8k, 42% utilisation), PSV firm (£19.5k, 82%). No change to the Oil Service row |
| Oil Shipping BBB | 24 Oct 2026 | Final (stub re-marked only); its earlier-stale triggers (OPEC+ 1 Nov, US midterms 3 Nov) have passed | 23 Nov 2026 | Shipping row (tanker part) | 2027–29 and mid-cycle unchanged. The oil baseline kept its paths through both events, so the Shipping row is not affected `[A]`; read again after its next update |

- **Series used** (skill "Fixed series"):
  - Spread: "Kredittpåslag Norden / Norge", monthly, from the Heimdal Høyrente report (the
    underlying index provider is not named; DNB Carnegie is the likely source, `[?]`). First
    observation used: Aug 2025.
  - Monthly index return: DNB Carnegie Nordic HY index as quoted by Heimdal and Fondsfinans `[E]`.
  - Annual index return and FTD rates: Nordic Trustee 2025 report (NBP indices, NT/Stamdata FTD).
  - Rates: Norges Bank API and the MPR 3/26 dataset (`data-mpr-3-26.xlsx`, sheets Data A and E).
  - No series change this run. **October anchor: 490 bp** (Heimdal's October reports for Høyrente
    and Høyrente Pluss, dated 30 Oct, read in `docs/hy-issuers.md` on 4 Nov) `[F]`. Cross-source
    note: Fondsfinans quoted DNB Carnegie's Nordic HY spread at 445 bp for end-Sep against 430 bp
    in Heimdal's series (~15 bp apart). DNB Carnegie's October figure comes with the Fondsfinans
    October report (~10 Nov) and is not read yet `[?]`; the two series are never mixed.
- **Stamdata scan coverage** (stated here only; the issuer and fund files refer to it):
  - **market-wide news feed** (all issuers): **1 Sep–5 Nov 2026** (S8: 1 Sep–5 Oct, pages 1–5;
    S17: 23 Sep–16 Oct, pages 1–3; S25: 13–23 Oct; **S33: 19 Oct–5 Nov, pages 1–2, read 5 Nov**);
  - **held companies**, issuer by issuer: from **4 Aug to 23 Oct** (the screen in
    `docs/hy-issuers.md`, not rerun here). The market-wide pages read on 5 Nov show no notice from
    a held issuer except Booster (standstill prolonged to 1 Dec).
  - whether the market-wide feed was read for August is not recorded `[?]`: the log has no August
    entry for a name that is not held. Jan–Jul 2026 comes from press and later notices only.
- **FX** (Norges Bank, 30 Sep 2026; used for holdings prices): USD/NOK 9.6006 · EUR/NOK 10.9015 ·
  SEK/NOK 0.9621. **5 Nov 2026** (Norges Bank): USD/NOK 9.2984 · EUR/NOK 10.4365 · SEK/NOK 0.9501
  · I-44 107.76. New log volumes use the 5 Nov rates.
- **Hedge carry:** 3M NIBOR (NB projection Q4-26) 4.80 − SOFR 3.94 (FRED, 4 Nov) ≈ **+0.9 pp** for
  USD bonds hedged to NOK (unchanged); − STIBOR 3M ~1.94 (FRED, Sep), rising to ~2.15 after the
  Riksbank hike to 2.00% on 11 Nov `[A]` ≈ **+2.65 pp** for SEK bonds (+2.8 before; below the
  minimum change, noted).
- **Tags:** `[F]` fact · `[E]` external forecast or secondary · `[A]` own assumption · `[?]` unknown.

## Conclusion

- **5 Nov 2026 update: HY Market BBB changed (spreads and returns); rates, macro and defaults
  kept.** I tested Base against the two rate decisions, the October spread print, a month of
  Norwegian and Swedish data and the Stamdata feed to 5 Nov.
  - **Norges Bank, 5 Nov (decided 4 Nov): policy rate held at 4.50%** `[F]`.
    - Guidance, unchanged from September: "It will likely be necessary to keep the policy rate
      elevated for a time", and the Committee is "prepared to raise the policy rate if needed"
      (Governor Wolden Bache). No new forecasts; MPR 4/26 comes on **17 Dec**.
    - New since September (statement): domestic inflation higher than projected; registered
      unemployment a bit lower and employment a little higher than projected; capacity
      utilisation slightly below normal; **the krone stronger than assumed**; oil spot lower,
      futures, gas and power higher. The Committee has not seen information that changes the
      outlook materially since September.
    - **Reading `[A]`:** a hawkish hold. The upward pressures (domestic inflation, labour market,
      foreign rates) and the downward one (the krone, I-44 ~107 vs ~110 assumed) roughly offset.
      A December path within ±0.15 pp of September is the likeliest outcome, below the 25 bp
      minimum change. **Base keeps the MPR 3/26 path** (NIBOR 4.79 / 4.39 / 3.86).
    - **Market check (4 Nov):** NIBOR-equivalent forwards 4.96 / 4.72 / 4.57 for 2027–29, i.e.
      +0.17 / +0.33 / +0.71 pp above Base (22 Oct: +0.25 / +0.55 / +0.9). The 2027 gap is below the
      0.3 pp test; 2028–29 remain above it but narrowed by 0.2 pp in two weeks as global yields
      fell. The "higher for longer" reading holds for 2028–29 and is the risk to the path; it is
      tested again on MPR 4/26 (decision recorded in Drivers → Rates).
  - **Riksbank, 4 Nov: policy rate raised 0.25 pp to 2.00%** (effective 11 Nov) `[F]`. If the
    outlook holds, a further hike in the coming year is likely, in line with the September path
    (to ~2.4% by Q3-27 `[E]`). Q3 GDP +0.4% q/q and employment were in line with the forecast;
    CPIF 1.5% (Sep), 3.0% excluding temporary fiscal measures. Next MPR 16 Dec. Sweden's GDP and
    unemployment Base is unchanged. For Swedish issuers (real estate, finance), refinancing costs
    rise with STIBOR but the economy strengthens: net Base stable, as before.
  - **Spreads — re-marked (the trigger):** the Nordic anchor widened **430 → 490 bp** in October,
    Norway ~525 `[A]`. Europe widened more (2.8 → 3.7%) and the US 2.9 → 3.4% (Heimdal) `[E]`.
    DNB Carnegie Nordic HY returned **−0.2%** in October (YTD +5.6%) `[E]`.
    - The widening is broad (Europe +90 bp), not only the Nordic distressed names (Intrum,
      Trustly, HX, Borr, Archer). Heimdal Høyrente had ~9% net redemptions in October.
    - Early November eased: Euro HY 3.59 → 3.45% and US 3.44 → 3.32% (30 Oct → 4 Nov, FRED), and
      Fondsfinans High Yield B's NAV rose 0.08% (30 Oct → 3 Nov) `[F]`. The Nordic November print
      may be lower; that is a checkpoint, not a reason to discount the anchor.
    - **Base now holds ~490 bp** (the normal level is 500) instead of drifting 430 → 475. Base 2027
      returns **8.0%** (7.0 before): 0.5 pp more carry and no widening MTM. The stub falls 1.9 →
      **1.1%** (October's MTM). Window **7.2%** a year (6.8).
  - **Defaults: Base kept** (3.0 / 3.5 / 3.5%).
    - New in the feed 24 Oct–5 Nov: Proximar Seafood missed interest (NOK 300m, 27 Oct); Caybon
      deferred interest on both bonds (SEK ~311m); Achilles Capital non-payment and events of
      default (EUR 170m; maturity already extended in June); Calligo's bonds written down to zero
      in a debt-for-equity swap (EUR ≤ 50m, effective 5 Nov); Engebø Rutile forbearance with a
      priming super senior bridge (USD ~186m, pending).
    - Pace over the market-wide window 1 Sep–5 Nov (66 days): **~2.2% a year** (1.8% without SIBS;
      4.3% with the pending Dooba and Engebø) `[A]`, inside Base's 2.0–4.0%. The window is still
      shorter than the full quarter the FTD trigger needs.
    - Held names (`docs/hy-issuers.md`, 4 Nov): Borr Watch (~93), HX super senior Stressed (~84),
      Intrum Distressed (73.75), Trustly Distressed (79). The year-1 watchlist build at status
      values gives ~0.5–0.6 pp of the 3.0% (Year-1 build under Defaults).
  - **Norway data:** registered unemployment **2.0%** seasonally adjusted in October (59,100
    unadjusted; NAV, 30 Oct), below Norges Bank's 2.1% for 2026; LFS 4.6% (trend, Sep). Retail
    sales volume **−0.4% m/m** in September, flat q/q in Q3 and −1.1% y/y (SSB 07129). No GDP
    release since 27 Aug (Q2 mainland +0.3% q/q); Q3 comes on 26 Nov. October CPI comes on 10 Nov.
    Norges Bank's net FX purchase is **NOK 176m a day in November, unchanged** from September and
    October: no larger NOK sale yet, so the tailwind to the krone from this channel does not fade
    this month.
  - **US midterms (3 Nov):** Democrats won both chambers; nothing changes in law before 3 Jan.
    The global backdrop eased: Norwegian 3Y 4.77 → 4.64% and 10Y 4.49 → 4.37% (22 Oct → 4 Nov),
    HY OAS tighter. Markets price ECB and Fed hikes in December (Riksbank MPU) `[E]`. No path
    change.
  - **Energy:** oil kept; drillship Base 2027 $420k / 91% (rig, 4 Nov) is firmer; supply kept. No
    energy row moves.
  - **Market reference (fund rule): E / R 0.196 → 0.254** (E 1.82 → 2.15; R 9.28 → 8.47). Fund
    verdicts must be re-run against it.
- **24 Oct 2026 update (kept unchanged):** the details are in the change log.
- **17 Oct 2026 update (kept unchanged):** the details are in the change log.
- **Base (5 Nov):**
  - Nordic HY earns about **7.2% a year in NOK (2.75 pp over NIBOR) through 2029**: 8.0% in 2027,
    7.2% in 2028, 6.8% in 2029. The return falls as NIBOR follows Norges Bank's path down
    (4.8% → 3.9%), while spreads hold near the 5.0% normal.
  - First-time defaults rise moderately from the 2025 low (2.6%) to **3.0–3.5%**. Energy issuers
    stay healthy on the upstream baselines; the risk sits in sponsor-backed continental and
    consumer issuers and Swedish finance and real estate, where 2026 defaults have clustered.
- **Row ranking by risk premium (spread − expected loss), strongest → weakest:**
  1. **Oil Service:** ~440 bp premium; the rig and OSV baselines are firm through 2029 (Base FTD
     1.5% a year, aligned 24 Oct; drillships $420k / 91% in 2027).
  2. **O&G E&P:** ~450 bp premium, but the 2025 FTD rate was 8.3% (small single-asset issuers).
  3. **Other non-energy** (finance, industry, consumer, telecom, transport): ~370 bp; most 2026
     defaults are here.
  4. **Real Estate:** ~300 bp; Swedish stress has passed (Swedish FTD 10.1% → 3.0% in 2025), but
     the Riksbank is now hiking (2.00% from 11 Nov).
  - Shipping: no sector spread found `[?]`; tanker earnings normalise in 2028–29.
  - The row premiums use the 2025 new-issue spreads (NT) and are not re-marked for October.
- **Main Bear catalyst:** oil Bear (a durable Iran–USA deal plus an OPEC+ market-share fight)
  together with a global recession in H1 2027. That hits the 25% energy block and the
  leveraged non-energy issuers at once. Spreads jump to ~850 bp by end-2027 and defaults peak at
  ~8.6% in 2028 (the 2016 analogue). Return −0.4% in 2027 (−2.2% before; the start is wider),
  recovered through carry in 2028–29. The deal leg is closer after the midterms (oil baseline).
- **Main Bull catalyst:** a soft landing. Inflation falls faster, Norges Bank cuts from mid-2027,
  oil stays on its Base path, and Nordic spreads compress back towards ~390–400 bp (10.7% in 2027).

## Interface — rates and macro (point values; ranges below)

| Series Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| Policy rate, annual avg (%) | 4.51 / 4.51 / 4.51 | 3.96 / 4.55 / 4.42 | 3.25 / 4.20 / 3.90 | 3.25 / 3.65 / 3.40 | 3.0 / 3.2 / 3.2 |
| 3M NIBOR, annual avg (%) | 4.80 / 4.80 / 4.80 | 4.21 / 4.79 / 4.65 | 3.55 / 4.39 / 4.15 | 3.50 / 3.86 / 3.65 | 3.25 / 3.45 / 3.45 |
| Norway mainland GDP growth (%) | 0.9 / 0.9 / 0.9 (2026) | −0.5 / 1.0 / 1.5 | 0.5 / 1.0 / 1.8 | 1.5 / 1.3 / 1.8 | 1.3 |
| Sweden GDP growth (%) | 2.8 / 2.8 / 2.8 (2026) | 0.0 / 2.4 / 2.8 | 1.0 / 1.3 / 2.0 | 2.0 / 1.6 / 1.8 | 1.5 |
| Norway unemployment, registered NAV (%) | 2.1 / 2.1 / 2.1 | 2.6 / 2.3 / 2.1 | 3.0 / 2.4 / 2.2 | 2.9 / 2.4 / 2.3 | 2.4 |
| Sweden unemployment, LFS (%) | 8.6 / 8.6 / 8.6 | 9.2 / 8.1 / 7.9 | 9.4 / 7.6 / 7.4 | 8.9 / 7.4 / 7.2 | 7.5 |
| Fiscal (Base only): SOBU % of mainland trend GDP / withdrawal % of GPFG / budget indicator (pp) | 12.7 / 2.7 / +1.1 (2026) | 12.6 / 2.7 / 0.0 | `[?]` (next budget Oct 2027) | `[?]` | — |
| Market path check: 1-year forwards from the zero curve + NIBOR–T-bill spread (4 Nov) | — | ~4.96 | ~4.72 | ~4.57 | — |

- **Base = Norges Bank MPR 3/26** (24 Sep 2026) `[E]`:
  - Quarterly policy rate and 3-month money-market rate (NIBOR) from the dataset.
  - Mainland GDP 0.9 / 1.0 / 1.0 / 1.3 (2026–29); registered unemployment 2.1 / 2.3 / 2.4 / 2.4.
  - Sweden from the Riksbank MPR (Sep 2026): GDP 2.8 / 2.4 / 1.3 (2026–28), unemployment 8.6 /
    8.1 / 7.6 `[E]`; 2029 extended at potential `[A]`.
- **Method change vs the skill template:** Norwegian unemployment is shown as registered (NAV),
  not LFS, because that is the measure Norges Bank projects. Sweden unemployment added. Logged
  in the skill.
- **Mid-cycle NIBOR:** Norges Bank's model normal rate is **3.2%** (raised 0.2 pp in MPR 3/26),
  plus the 0.25 pp money-market premium = 3.45% `[E/A]`. Neutral real rate interval 0.25–1.75%
  `[E]`. Bear 3.25% `[A]`.
- Ranges: NIBOR Base ±0.3 pp in 2027 and ±0.5 pp in 2028–29; GDP ±0.7 pp.
- Denmark and Finland (≈ EUR 1bn and 3bn of local HY, 6% of the Nordic market) are not assessed.
- **Base confirmed after the 5 Nov decision:** Norges Bank held 4.50%, repeated "elevated for a
  time" with a hiking bias, and saw no material change in the outlook. No new forecasts were made,
  so MPR 3/26 stays the Base anchor until MPR 4/26 on 17 Dec.
- **Market path check (4 Nov):**
  - government zero curve 6M 4.690 · 9M 4.714 · 12M 4.704 · 2Y 4.586 · 3Y 4.492 · 4Y 4.431 `[F]`,
    giving 1-year forwards ≈ 4.68 / 4.44 / 4.29 for calendar 2027 / 28 / 29 (linear zero
    interpolation; the same method reproduces the 22 Oct values 4.76 / 4.66 / 4.46);
  - plus a NIBOR–T-bill spread of ~0.28 pp `[A]`, kept from 22 Oct. The generic 3M T-bill jumped
    4.52 → 4.73 on 29 Oct while NOWA stayed 4.50 and the 6M zero moved only 4.66 → 4.69; that looks
    like a change of reference bill, so the spread is not re-measured on it `[A]`.
  - Gap to Base **+0.17 / +0.33 / +0.71 pp** (22 Oct +0.25 / +0.55 / +0.9; 15 Oct ~5.0 / 4.9 / 4.75;
    7 Oct ~5.1 / 4.9 / 4.8). Above the 0.3 pp test in 2028–29 only, and narrowing. The forwards
    include a term premium, so this is a check, never the path (skill Step 3b). Decision in
    Drivers → Rates.

## Year 1 by quarter — policy rate and 3M NIBOR (%)

| Scenario | Q1-27 | Q2-27 | Q3-27 | Q4-27 | Year avg |
|---|---|---|---|---|---|
| Bear — policy | 4.50 | 4.10 | 3.75 | 3.50 | 3.96 |
| Bear — NIBOR | 4.70 | 4.35 | 4.00 | 3.80 | 4.21 |
| **Base — policy** | **4.57** | **4.60** | **4.58** | **4.46** | **4.55** |
| **Base — NIBOR** | **4.84** | **4.85** | **4.78** | **4.68** | **4.79** |
| Bull — policy | 4.50 | 4.50 | 4.42 | 4.25 | 4.42 |
| Bull — NIBOR | 4.78 | 4.73 | 4.62 | 4.47 | 4.65 |

- Base is NB's quarterly average path. The policy average above 4.50 in 2027 implies some chance
  of one more hike `[E]`. NB assumes a constant 0.25 pp money-market premium.
- Bear: cuts from Q2-27 to 3.50% by Q4-27 as oil and growth collapse; premium 0.20–0.30 pp `[A]`.
  Bull: the first cut in Q3-27 `[A]`.
- Quarters average to the annual values (checked).

## Interface — credit (point values; ranges below)

| Row Bear / Base / Bull | Stub Q4-26 | 2027 | 2028 | 2029 | Mid-cycle |
|---|---|---|---|---|---|
| Nordic HY spread, annual avg (bp) | 490 / 490 / 490 | 680 / **490** / 440 | 720 / **490** / 400 | 570 / **495** / 410 | 575 / 500 / 450 |
| Nordic HY spread, year-end (bp) | 490 / 490 / 490 | 850 / **490** / 390 | 650 / **495** / 400 | 520 / **500** / 420 | — |
| FTD rate Nordic HY (%) | 3.0 / 3.0 / 3.0 | 5.6 / 3.0 / 2.3 | 8.6 / 3.5 / 2.2 | 6.6 / 3.5 / 2.3 | 5.5 / 4.0 / 3.0 |
| FTD O&G E&P (%) | 3.0 / 3.0 / 3.0 | 8.0 / 3.0 / 2.5 | 15.0 / 3.5 / 3.0 | 12.0 / 4.0 / 3.0 | 9.0 / 5.0 / 4.0 |
| FTD Oil Service (%) | 1.5 / 1.5 / 1.5 | 4.0 / 1.5 / 1.0 | 12.0 / **1.5** / **1.0** | 10.0 / **1.5** / **1.0** | 7.0 / 3.0 / 2.0 |
| FTD Shipping (%) | 1.5 / 1.5 / 1.5 | 3.0 / 1.5 / 1.0 | 7.0 / 2.5 / 1.5 | 6.0 / 3.5 / 2.0 | 5.0 / 3.0 / 2.0 |
| FTD Real Estate (%) | 2.5 / 2.5 / 2.5 | 5.0 / 2.5 / 1.5 | 6.0 / 2.5 / 1.5 | 4.0 / 2.5 / 1.5 | 4.0 / 2.5 / 1.5 |
| LGD Nordic HY (%) | 55 / 55 / 55 | 65 / 55 / 50 | 65 / 55 / 50 | 65 / 55 / 50 | 60 / 55 / 50 |
| Expected loss Nordic HY (% p.a.) | 1.65 / 1.65 / 1.65 | 3.64 / 1.65 / 1.15 | 5.59 / 1.93 / 1.10 | 4.29 / 1.93 / 1.15 | 3.3 / 2.2 / 1.5 |

- The stub FTD and EL are annual rates; a quarter carries one quarter of them (EL 0.41%).
- Spreads: **start 490 bp** `[F]` (Nordic, end-Oct 2026, Heimdal's October reports; 430 at
  end-Sep). The stub holds 490 to year-end (no scenario spread in the stub). Norway runs about
  35 bp wider (Feb 2026: 519 vs 484; Nov 2025: 520 vs 490 `[F]`), so Norway ≈ 525 bp now `[A]`.
  - **Base (re-marked 5 Nov):** the start is at the 500 bp normal level, so Base holds ~490 in
    2027 and drifts to 500 by end-2029. The old path (430 → 475) was the same drift toward normal
    from a lower start. The risk premium (spread − EL) is 325 bp in 2027, above the 280 bp normal,
    falling to ~300 in 2028–29 as EL rises.
  - The 2028–29 moves (+25–30 bp) are below the 50 bp minimum on their own. They follow from the
    re-marked start, so the path is re-marked as one (the 24 Oct checkpoint 10 rule).
  - **Bear and Bull keep their catalyst levels** (Bear YE-27 850, mid-2027 peak ~900; Bull YE-27
    390). Only their 2027 averages move with the start (650 → 680; 410 → 440).
- Ranges (Base): spread ±60 bp in 2027 and ±90 bp in 2028–29; FTD 2.0–4.0% (2027), 2.5–5.0%
  (2028–29); LGD 45–65%. Bear FTD peak 7–10%; Bull FTD 1.5–3.0%.

## Interface — expected return, NOK hedged, before fees (%)

| Row Bear / Base / Bull | Stub Q4-26 (quarter) | 2027 | 2028 | 2029 | Window (ann.) | Mid-cycle |
|---|---|---|---|---|---|---|
| Nordic HY total return | 1.1 / 1.1 / 1.1 | −0.4 / **8.0** / 10.7 | 10.8 / **7.2** / 7.1 | 8.2 / **6.8** / 6.1 | 6.0 / **7.2** / 7.7 | 5.7 / 6.3 / 6.5 |
| Nordic HY excess return over NIBOR | −0.1 / −0.1 / −0.1 | −4.6 / **3.25** / 6.05 | 7.2 / **2.84** / 2.95 | 4.7 / **2.9** / 2.45 | 2.1 / **2.75** / 3.5 | 2.5 / 2.8 / 3.0 |
| Norway HY total return | 1.2 / 1.2 / 1.2 | −1.4 / **8.4** / 11.1 | 11.6 / **7.6** / 7.5 | 8.7 / **7.1** / 6.4 | 6.1 / **7.5** / 8.1 | 5.8 / 6.5 / 6.7 |

- The stub is one quarter, not annualised: **October actual −0.2%** (DNB Carnegie Nordic HY, via
  Heimdal `[E]`) plus November–December carry at today's yield (NIBOR 4.80 + spread 4.90) less the
  Base EL pro rata = **+1.14%**. The window is geometric over 3.24 years, including the stub.
  Cumulative: Bear +20.6%, Base +25.1%, Bull +27.2% (before: +19.3 / +23.8 / +26.1).
- Ranges (Base): 2027 6.5–9.0, 2028 5.5–8.5, 2029 5.0–8.0, window 6.2–8.0 (each +0.5–1.0 with the
  spread re-mark).
- Norway HY: spread +35 bp over Nordic; FTD on Norwegian sector weights (Base 2.9 / 3.3 / 3.35
  after the 24 Oct Oil Service alignment; Bear 5.5 / 9.0 / 7.0); Bear spread moves × 1.15 for the
  heavier energy weight `[A]`. The Norway October return is not published in the sources read, so
  its stub uses the Nordic −0.2% `[A]`. Norway 2028–29 Bear and Bull are kept (unchanged inputs).
- **Sweden HY (secondary, Base only, low confidence):**
  - FTD 3.0% a year (Swedish 2025 year-end 3.0%, down from 10.1% `[F]`).
  - NOK-hedged return ≈ NIBOR + ~440 bp (NT 2025 average Swedish HY issue spread `[F]`; no
    current Swedish spread found `[?]`) − EL 1.65, with no MTM ≈ **7.5 / 7.1 / 6.6%**. Kept: the
    Riksbank notes that Swedish credit spreads have increased (MPU 4 Nov), but no Swedish HY
    spread level is published in the sources read `[?]`.

## Scenario definitions

| Scenario | Weight (convention) | Rate path | Macro path | Oil BBB scenario (and sector BBBs) | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|---|---|
| **Bear** | 25% | NB cuts from Q2-27 to 3.50% by Q4-27, 3.25% in 2028–29 | Global recession H1 2027; Norway mainland −0.5% in 2027; Sweden 0.0%, unemployment 9.4% in 2028 | **Oil Bear** (Brent 65 / 60 / 60); rig Bear, supply Bear, tanker Bear | **Energy:** durable Iran–USA deal + OPEC+ market-share fight. **Macro:** recession after the energy shock. **Market:** global HY repricing, fund outflows, a shut new-issue window for 2–3 quarters | Energy (25% of the index) loses cash flow while refinancing is shut. Leveraged sponsor-backed issuers miss on EBITDA. Spreads lead (YE-27 850 bp), defaults lag (peak 8.6% in 2028). Carry at ~7% spreads repays most MTM in 2028–29 | Q1 2027 | Oil Bear signposts (Dec-27 Brent < $70, ceasefire > 60 days) · Nordic spread > 550 bp · monthly issuance < NOK 10bn for 2 months · > 10 distress notices a month on Stamdata for 3 months · NAV unemployment > 2.6% · US HY OAS > 450 bp |
| **Base** | 50% | Norges Bank MPR 3/26: 4.50% held through 2027, falling to ~3.5% by end-2029 | Mainland GDP ~1%; Sweden 2.4% then 1.3%; low unemployment | **Oil Base** (Brent 84 / 77 / 72; 2027 was 88 to 10 Nov); rig, supply and tanker Base | Higher-for-longer rates with a slowly fading energy upcycle; record issuance by foreign sponsor-backed issuers seasons into defaults in 2027–28 | Carry ~9%. FTD rises from 2.6% to 3.0–3.5%, concentrated in non-energy, non-Nordic and consumer issuers. Spreads hold near normal (490 → 500 bp; re-marked 5 Nov from 430 → 475) | Ongoing | Nordic spread 400–550 bp · issuance NOK 15–30bn a month · NB on path (5 Nov: held, path confirmed; next 17 Dec) · distress notices 3–8 a month |
| **Bull** | 25% | First NB cut Q3-27; policy 3.4% avg 2029 | Soft landing: mainland 1.5–1.8%, Sweden 2.8% in 2027 | **Oil Base** (energy cash flows stay strong) | Inflation falls faster than NB projects; global risk appetite holds; Nordic premium vs Europe narrows | Spreads compress to ~390–410 bp; FTD ~2.2%; MTM gain in 2027 | Q2 2027 | CPI-ATE < 2.5% by mid-2027 · NB signals cuts · Nordic spread < 400 bp · Nordic–Euro HY gap < 120 bp |

- **Why this Bear and not stagflation:** the alternative tail (oil Bull: renewed strikes after 3
  Nov, Brent 118; Norges Bank hikes to ~5.0%; NIBOR 5.2%; spreads to 600 bp YE-27; FTD 4.0%) gives
  about **+4.9% in 2027** from the 490 bp start (+3.4% from 430 before 5 Nov: 60 bp less widening
  to reach 600 is ~1.5 pp less MTM) `[A]`. Higher FRN carry and healthy energy issuers cushion it,
  so it is still less damaging than the recession-plus-oil-collapse Bear (−0.4%). Tested `[A]`;
  kept as a mixed path. Its timing window (strikes before 3 Jan, oil baseline) is shorter after
  the midterms.
- 25/50/25 is a labelled convention. Scenario-weighted window ≈ 7.0% a year (6.7 before 5 Nov) (reference only).

## Return decomposition — Nordic HY, per scenario (%)

Credit duration 2.5 years, rate duration 1.2 years `[A]` (funds report 1.9–2.3 and 1.1–1.3;
FRN share 55% `[E]`, BNP AM Aug 2026). Spread MTM = −2.5 × change in year-end spread. Base has
no rate MTM because the NB path is close to market pricing (MPR 3/26) `[E]`.

| Scenario | Year | NIBOR | Spread carry | Expected loss | Spread MTM | Rate MTM | Total | Excess |
|---|---|---|---|---|---|---|---|---|
| All | Stub Q4-26: October actual (DNB Carnegie) | — | — | — | — | — | −0.20 | — |
| All | Stub Q4-26: Nov–Dec (2 months) | 0.80 | 0.82 | −0.28 | 0.00 | 0.00 | 1.34 | 0.54 |
| All | **Stub Q4-26, quarter** | 1.20 | — | — | — | — | **1.14** | **−0.06** |
| Bear | 2027 | 4.21 | 6.80 | −3.64 | −9.00 | +1.20 | −0.43 | −4.64 |
| Bear | 2028 | 3.55 | 7.20 | −5.59 | +5.00 | +0.60 | 10.76 | 7.21 |
| Bear | 2029 | 3.50 | 5.70 | −4.29 | +3.25 | 0.00 | 8.16 | 4.66 |
| **Base** | **2027** | **4.79** | **4.90** | **−1.65** | **0.00** | **0.00** | **8.04** | **3.25** |
| **Base** | **2028** | **4.39** | **4.90** | **−1.93** | **−0.13** | **0.00** | **7.23** | **2.84** |
| **Base** | **2029** | **3.86** | **4.95** | **−1.93** | **−0.13** | **0.00** | **6.76** | **2.90** |
| Bull | 2027 | 4.65 | 4.40 | −1.15 | +2.50 | +0.30 | 10.70 | 6.05 |
| Bull | 2028 | 4.15 | 4.00 | −1.10 | −0.25 | +0.30 | 7.10 | 2.95 |
| Bull | 2029 | 3.65 | 4.10 | −1.15 | −0.50 | 0.00 | 6.10 | 2.45 |

- **Re-marked 5 Nov** (previous: stub 1.86; Bear 2027 −2.24 with spread carry 6.50 and MTM
  −10.50; Base 2027–29 7.04 / 6.69 / 6.39 with carry 4.40 / 4.60 / 4.70 and MTM −0.50 / −0.38 /
  −0.25; Bull 2027 8.90 with carry 4.10 and MTM +1.00). 2028–29 Bear and Bull rows are unchanged.
  The Bear 2027 NIBOR is now the Interface value 4.21 (4.20 before).
- **Spread MTM is a timing effect:** October's widening cost ~0.8 pp against carry in the stub, and
  the same widening pays ~0.5 pp a year more carry from 2027. Over the window the net is +0.35 pp a
  year (6.8 → 7.2%), because the old Base also expected spreads to widen toward normal.
- **Bear drawdown inside 2027:** with spreads peaking ~900 bp mid-year, the mark-to-market trough
  is about −7% from start `[A]` (−8% from a 430 start). That is milder than March 2020, when Heimdal
  Høyrente fell 15.6% in a month (−23% intra-month) as its yield jumped from 5.7% to 12.7% `[F]`.
- **Bear as a shock size (sensitivity, not applied):** if Bear is read as +420 bp from the start
  (YE-27 910) instead of a level (850), Bear 2027 is −1.9% and R 9.97. Base keeps the level reading
  because the analogues (2016, 2020, 2022) peaked at levels of 850–1,000 bp from different starts.
- **Risk premium (spread − EL), Base:** 325 / 297 / 302 bp (2027–29) vs 280 bp at mid-cycle
  (before: 275 / 267 / 277). At 490 bp the market pays more than the normal premium, because Base
  expected losses (1.65–1.93%) are below the 2.2% normal.
- Linear model: convexity, reinvestment timing, swing pricing and transaction costs are ignored.

## Defaults and losses per row — point (range)

Volume share = NBP Nordic HY index weight, end-2025 (O&G 17% split E&P 7 / Oil Service 10 using
the NT Norwegian shares 10 / 15) `[F/A]`. Default counts behind each row are not published, and
the own log starts in 2026 (`[?]`), so every row is **low confidence** until the log matures.

| Scenario | Row | 2027 | 2028 | 2029 | Mid-cycle | Volume share | n defaults (3 yrs) | Confidence |
|---|---|---|---|---|---|---|---|---|
| Base | O&G E&P | 3.0 (2–6) | 3.5 (2–7) | 4.0 (2–8) | 5.0 | 7% | `[?]` | Low |
| Base | Oil Service | 1.5 (0.5–3) | 1.5 (0.5–3.5) | 1.5 (0.5–4) | 3.0 | 10% | `[?]` | Low |
| Base | Shipping | 1.5 (0.5–3) | 2.5 (1–4) | 3.5 (1.5–5) | 3.0 | 8% | `[?]` | Low |
| Base | Real Estate | 2.5 (1.5–4) | 2.5 (1.5–4) | 2.5 (1.5–4) | 2.5 | 12% | `[?]` | Low |
| Base | Other non-energy (secondary) | 3.5 (2.5–5) | 4.0 (3–6) | 3.75 (2.5–5.5) | 4.5 | 63% | `[?]` | Low |
| **Base** | **Nordic HY total** | **3.0** | **3.5** | **3.5** | **4.0** | 100% | — | Low–medium |
| Bear | E&P / Oil Service / Shipping / RE / Other | 8 / 4 / 3 / 5 / 6 | 15 / 12 / 7 / 6 / 8 | 12 / 10 / 6 / 4 / 6 | — | — | — | Low |
| Bear | Nordic HY total | 5.6 | 8.6 | 6.6 | 5.5 | 100% | — | Low |
| Bull | E&P / Oil Service / Shipping / RE / Other | 2.5 / 1.0 / 1.0 / 1.5 / 2.8 | 3.0 / 1.0 / 1.5 / 1.5 / 2.5 | 3.0 / 1.0 / 2.0 / 1.5 / 2.5 | — | — | — | Low |
| Bull | Nordic HY total | 2.3 | 2.2 | 2.3 | 3.0 | 100% | — | Low |

- **Reconciliation:** Σ row × volume share against the market rate (Base 2.99 / 3.42 / 3.37;
  Bear 5.58 / 8.57 / 6.58; Bull 2.30 / 2.19 / 2.23).
  - Within 0.05 pp in 2027 and in every Bear year. After the 24 Oct Oil Service alignment, the
    bottom-up sum is 0.08–0.13 pp below the Base market point in 2028–29 and up to 0.07 pp below
    Bull.
  - The market points (3.0 / 3.5 / 3.5) are kept: the gap is well below the 1.0 pp minimum change
    for the market rate. Moving them would lower Base expected loss by ~0.05–0.07 pp a year and
    raise returns by the same amount, without changing any rounded return or the market
    reference (E / R uses 2027 only). The gap is reapplied at the next re-mark.
- **Other non-energy, split (secondary, Base 2027 / 28 / 29):**
  - Finance (16%): 2.0 / 2.5 / 2.5.
  - Industry (14%): 4.0 / 4.5 / 4.0.
  - Consumer (7%): 6.0 / 6.5 / 6.0.
  - Telecom/IT, Transportation, Other (26%): 3.5 / 4.0 / 3.75.
- **Year-1 build, partial check (5 Nov) `[A]`:** the priced part of the watchlist at status
  values (Definitions), NOK m: Borr (Watch, ~18,800 × 5%) 940 · Intrum (Distressed, ~7,600 × 20%;
  XS notes, possibly outside the NT universe) 1,520 · Trustly (Distressed, ~3,870 × 20%) 770 · HX
  super senior (Stressed, ~800 × 10%) 80 · Dooba (Vote or standstill, ~1,030 × 50%) 515 · Engebø
  (Vote or standstill, ~1,730 × 50%) 865 · Achilles (maturity Apr 2027 after the EUR 100m
  amortisation due 31 Dec; already in default, so not counted again). Sum ≈ NOK 4.7bn ≈ **0.6% of
  the market**, leaving ~2.4% for the background rate and the names not priced. It supports the
  3.0% point; it is not complete enough to replace the top-down set.
- **Year-1 build (5 Oct):** the watchlist volume could not be priced (most bond prices `[?]`), so the
  bucket method was not applied. Base 2027 is set top-down `[A]`:
  - the 2025 FTD of 2.6–2.9%;
  - a steady 2026 flow of small defaults (see the log);
  - the cohort pattern: most defaults come 1.5–2.5 years after issue `[E, unconfirmed]`, and
    2025–26 brought record, increasingly non-Nordic issuance (56% international in 2026 `[E]`).
- **LGD:** Base 55% (market recovery ~45%), Bear 65%, Bull 50% `[A]`.
  - NHH studies of Norwegian and Nordic defaults find recoveries comparable to international
    levels, with no clear benefit from security `[E]`.
  - The 2026 log so far: LR Health & Beauty ~1/3 written off (ultimate recovery ~67 `[E]`).
  - Energy asset cover is good while the rig, OSV and tanker values in the upstream baselines
    are above mid-cycle.

### Do sector spreads pay for sector losses? (added 17 Oct 2026, user question)

**Realised 2025** (NT 2025 report, Nordic table; issue spread = average spread of 2025 new issues;
loss = FTD × 55% LGD `[A]`):

| Sector | Issue spread (bp) | FTD 2025 (%) | Loss (bp) | Spread − loss (bp) | Market share (%) |
|---|---|---|---|---|---|
| Convenience goods | 599 | 10.9 | 600 | 0 | 3 |
| Agriculture | 394 | 9.7 | 534 | −140 | 1 |
| O&G E&P | 621 | 8.3 | 457 | 164 | 7 |
| Utilities | 591 | 7.9 | 434 | 156 | 2 |
| Transportation | 507 | 6.6 | 363 | 144 | 7 |
| Industry | 605 | 4.1 | 225 | 380 | 14 |
| Seafood | 594 | 2.8 | 154 | 440 | 2 |
| Consumer services | 446 | 2.8 | 154 | 292 | 6 |
| Real Estate | 435 | 2.1 | 116 | 320 | 18 |

- Spreads rise with defaults, but loosely. The correlation is 0.19 across sectors and 0.58 when
  weighted by volume. Spreads span only 394–621 bp while FTD spans 2–11%.
- The small consumer sectors and agriculture paid nothing net in 2025. The large sectors (Industry,
  Real Estate) kept 300–380 bp.
- **Caveat:** 2025 defaults come from bonds issued in earlier years, while the issue spread is for new
  2025 bonds. Sectors with 1–3% share hold only a handful of issuers, so the comparison is noisy.
  Oil Service and Shipping are not in the Nordic table. Norway's table has Oil Service at FTD 0.8%
  and ~520 bp, but its values are not printed in label order, so the other Norwegian sectors are
  not used `[?]`.

**Forward, baseline rows** (Base EL = average 2027–29 FTD × 55%; Bear EL = the Bear peak year ×
65%; Other non-energy spread = 550 bp, volume-weighted from the Nordic table):

| Row | Spread (bp) | Base EL (bp a year) | Premium in Base (bp) | Bear-peak EL (bp) | Spread ÷ Bear-peak EL |
|---|---|---|---|---|---|
| O&G E&P | 621 | 193 | 428 | 975 (2028) | 0.64 |
| Oil Service | ~520 (Norway) | 83 (110 before 24 Oct) | ~440 | 780 (2028) | 0.67 |
| Other non-energy | ~550 | 206 | ~345 | 520 (2028) | 1.06 |
| Real Estate | 435 | 138 | 297 | 390 (2028) | 1.12 |
| Shipping | `[?]` (no sector spread published) | 138 | `[?]` | 455 (2028) | `[?]` |

- **In Base, the order holds:** energy pays the most premium over its expected loss (E&P ~430,
  Oil Service ~440 bp) and Real Estate the least (~300 bp).
- **In Bear, it flips:**
  - one year of Bear-peak losses is ~1.5× the spread in E&P and Oil Service;
  - the spread still covers the Bear-peak loss in Real Estate and the other non-energy sectors.
  - So the market prices energy on today's strong cash flows, not on its oil-cycle tail. That is
    consistent with the baseline: energy is where Bear does the most damage, and oil-heavy funds
    carry it in their stress loss R.

## Market check

| Measure | Latest (date, source) | Previous baseline | 12 months ago | Long-run (years) |
|---|---|---|---|---|
| Nordic HY spread (anchor) | **490 bp (30 Oct 2026, Heimdal October reports)** `[F]`; 430 at 30 Sep. DNB Carnegie Oct `[?]` (Fondsfinans report ~10 Nov; 445 at 30 Sep) | 430 bp (24 Oct; ~460 implied from fund NAVs to 22 Oct) | 450 bp (Sep 2025) | `[?]` series too short; BNP AM quotes "460 bp" (Aug 2026) as the current average `[E]`; mid-cycle set at 500 `[A]` |
| Norway HY spread | ~525 bp `[A]` (Nordic + 35; last quoted 519 bp, Feb 2026) | ~465 `[A]` | 470 (Sep 2025, as printed) | `[?]` |
| Euro / US HY OAS (context) | **345 / 332 bp (4 Nov)** `[F]` FRED; 359 / 344 on 30 Oct (Heimdal end-Oct: 3.7 / 3.4%); 354 / 340 on 22 Oct; 279 / 293 on 25 Sep | 354 / 340 (22 Oct) | 281 (Sep 2025 avg) / `[?]` | FRED keeps 3 years only |
| New-issue spread, Nordic HY | 541 bp avg 2025; Norway 583 `[F]` NT | — | — | — |
| Index return (DNB Carnegie Nordic HY) | **Oct −0.2%, YTD +5.6%** (Heimdal October reports) `[E]`; Europe −1.1%, US +0.3% in Oct. Sep +0.4% (Heimdal) or +0.1% (Fondsfinans; variant `[?]`) | +6.1% YTD (Sep) | +7.0% YTD (Sep 2025) | NBP Norway HY CAGR 9.1% 2020–25 `[F]` |
| Index return 2025 (NBP) | Nordic 9.8%, Norway 9.3%, Sweden 8.5% `[F]` | — | — | — |
| FTD rate (NT, LTM) | 2.6% Nordic, Q4-25 (Energy 3.0%, RE 2.2%); Norway 2.6%; Sweden 3.0% `[F]` | — | Nordic 5.5%, Sweden 10.1% (Q4-24) | 5.4% average since 2007 `[E]` BNP AM; 8.0% end-2016 `[E]` |
| Running FTD 2026 (NT-definition replica) | Lower bound: logged 2026 FTDs ≥ **NOK 11.7bn (~1.6% of the market)** by 5 Nov (H1 from press and later notices only). Pace over the market-wide window 1 Sep–5 Nov ~2.2% a year `[A]` (Default tracking) | ≥ NOK 8.8bn (~1.2%); pace ~2.2% (1 Sep–23 Oct) | — | — |
| Fund proxy for the index | Fondsfinans High Yield B **+0.16% in October** (NAV 11,392.82 → 11,411.42) and +0.08% 30 Oct–3 Nov `[F]` (Yahoo). A quality fund: it beat the index (−0.2%) in October | −0.18% (30 Sep–22 Oct) | — | — |
| Issuance | October ~EUR 1.9bn (~NOK 20bn), YTD EUR 21.1bn (Heimdal) `[E]`; Sep ~NOK 25.5–29bn. Slower, still open | ~NOK 220bn YTD (Sep) | 2025: NOK 278bn by Nov | — |
| Market size | > EUR 70bn (Aug 2026) `[E]`; EUR 63bn at YE-25 (NO 42.2, SE 16.5, FI 3.1, DK 1.0) `[F]` | — | — | — |
| Distress ratio, maturity wall | `[?]` not available without a licence | — | — | — |

- **Anchor spread history** (Heimdal, Nordic / Norway):

| Month | Nordic | Norway |
|---|---|---|
| Aug 2025 | 450 | 480 |
| Sep 2025 | 450 | 470 |
| Nov 2025 | 490 | 520 |
| Jan 2026 | 480 | 520 |
| Feb 2026 | 484 | 519 |
| Apr 2026 | 480 | — |
| May 2026 | 470 | — |
| Jun 2026 | 480 | — |
| Jul 2026 | 460 | — |
| Aug 2026 | 450 | — |
| Sep 2026 | 430 | — |
| **Oct 2026** | **490** | — |

  **October: +60 bp** (Europe +90, US +50 in the same reports), the first widening month since
  June. Before that, spreads tightened 50 bp from June despite the Gulf war and rising global
  rates. In Aug 2026
  Heimdal put the Nordic premium at > 2.0 pp over Euro HY and 1.8 pp over US HY, "somewhat above
  the historical average" `[E]`. The Aug value comes from the Høyrente Pluss August report
  (same manager and series).
- **Longer history (Heimdal year-end reports) `[E]`:**
  - Nordic spread: 6.1% (end 2023; Norway 5.6%) → 4.2% (end 2024; Norway 4.3%) → ~4.85% (end
    2025; Norway ~5.2%). Intra-2025 peak 5.2% / 5.5% in April (tariff sell-off).
  - DNB Carnegie Nordic HY: 2023 +9.1%, 2024 +12.4%, 2025 +8.4% (Norway +10.6 / +10.4 / +8.5).
  - **Caveat:** 2025's spread widening (+0.65 pp) did not show up as a price loss (the index
    returned +8.4%). The quoted spread moves with composition (record non-Nordic issuance) and
    the DNB Markets → DNB Carnegie change in Jan 2025, so it is a yield measure, not a clean MTM
    series. Fund calibration therefore uses index returns (skill 2026-10-06.4).
- **DNB Carnegie Nordic HY, monthly 2026 `[E]`:** Jan +1.0 · Feb +0.8 · Mar ≈ −0.2 (derived) · Apr
  +0.9 · May +0.8 · Jun +0.6 · Jul +0.8 · Aug +1.0 (YTD 5.7) · Sep +0.4 · YTD +6.1 · **Oct −0.2
  (YTD +5.6 as printed; the months above compound to ~5.9, so one figure has been restated `[?]`)**.
  Nordic HY held up in September while Euro HY fell 1.5% and US HY 1.8%; in October it fell less
  than Europe (−1.1%).

## Default tracking

(Added 18 Oct 2026; skill 2026-10-18.1, Step 5. Built from the log in the Appendix; updated 5 Nov
with the Stamdata feed to 5 Nov (S33). Scan coverage is in Metadata. Market size ≈ NOK 750bn
`[A]`, implied by "NOK 8.8bn ≈ 1.2%" and EUR ~69bn at 10.9. New volumes at the 5 Nov FX.)

**Monthly tracking:**

| Month | Window and pages read | Distress notices (issuers) | New FTDs (n / NOKm) | Pending (n / NOKm) | Routine or technical | Pace, annualised `[A]` |
|---|---|---|---|---|---|---|
| H1 2026 | Press only (S11); later notices (S33) | `[?]` | 3 / ≥ 3,170 (LR Health & Beauty 1,400; **Achilles Capital 1,770**, maturity extension Apr–Jun, found 5 Nov; Nordwest `[?]`) | — | — | Not scanned |
| Jul 2026 | Not scanned; seen in later notices | `[?]` | 3 / ≥ 1,290 (Point Properties 770; **Calligo ≤ 520**, debt-for-equity written procedure 17 Jul, found 5 Nov; Taptravel `[?]`) | — | — | Not scanned |
| Aug 2026 | Held companies only | `[?]` market-wide | 1 / ~4,200 (HX, "likely y" `[A]`) | — | 2 (Ocean Yield, Kistefos) | Market-wide feed not read |
| Sep 2026 | Market-wide feed (S8, pages 1–5) | ~6–8 | 4 / ≥ 945 (Booster 650; **Caybon 295**, amended terms, reclassified 5 Nov after its interest deferral; Jøtul and Catena `[?]`) | 2 / `[?]` (Convene, Solteq) | 3 (Eldorado, North Investment Group, Specac) | — |
| Oct 1–16 | Market-wide feed (S17, pages 1–3) | ~4 + 2 technical | 2 / 1,780 (Cabonline 1,170; SIBS 610, first default possibly 2025) | 1 / 1,030 (Dooba) | 5 (Kistos, Brightstar, Keystone, Storsala, Island Offshore legacy) | — |
| Oct 17–23 | Market-wide feed (S25, page 1 = 13–23 Oct) | 3 (Taptravel recapitalisation vote; Dooba information call; Rebellion covenant reset) | 0 | 1 / 1,030 (Dooba, carried) | 5 (Kistos adopted, DistIT cap, Eiendomskreditt tap, Elcano EGM; calls: Ventura, Airswift, First Mover) | — |
| Oct 24–31 | Market-wide feed (S33, page 2 = 19–29 Oct; page 1 from 30 Oct) | 3 (Proximar non-payment; Caybon interest deferral on both bonds; Dooba bondholder presentation) | 1 / 300 (Proximar, NOK 300m convertible; an earlier extension may be its first default `[?]`) | 1 / 1,030 (Dooba) | 6 (Konzmann issuer substitution into Nimlas for a fee; Thon Holding reorganisation; Banco Plata listing deadline; Grøntvedt guarantees; calls: Andfjord Salmon, Pearl Petroleum, Avarda) | — |
| Nov 1–5 | Market-wide feed (S33, page 1 = 30 Oct–5 Nov) | 4 (Achilles events of default; Calligo write-down effective; Engebø forbearance and priming bridge; Booster standstill prolonged to 1 Dec) | 0 new (Achilles and Calligo first defaulted in Jun and Jul; logged there) | 2 / ~2,760 (Dooba 1,030; Engebø ~1,730) | 4 (Galileo share distribution from the 2025 restructuring; Shamaran call condition met; Fortaco partial redemption; Oceanity Petrobras contract) | — |
| **Market-wide window, 1 Sep–5 Nov (66 days)** | | | **7 / ≥ 3,025** | **4 / ≥ 2,760** | | **~2.2%** (1.8% without SIBS; 4.3% with Dooba and Engebø) |

- Pace = FTD volume dated inside the window ÷ NOK 750bn × 365 ÷ 66 `[A]`. It understates if
  Jøtul's and Catena's volumes are material (both `[?]`). On 23 Oct (53 days) it was ~2.2%; on
  17 Oct ~2.6%.
- **October:** ~8 distress issuers (Point Properties, Dooba, SIBS, Solis legacy, Taptravel,
  Rebellion, Proximar, Caybon) + 2 technical: at the top of Base's 3–8 a month, below the Bear
  signpost (> 10 a month for 3 months). **1–5 Nov:** 4 issuers in five days. Watch the full month.
- **Running FTD replica 2026:** logged FTD volume ≥ **NOK 11.7bn ≈ 1.6% of the market by 5 Nov**
  (LR Health & Beauty 1,400 · Achilles 1,770 · Point Properties 770 · Calligo ≤ 520 · HX 4,200 ·
  Booster 650 · Caybon 295 · Cabonline 1,170 · SIBS 610 · Proximar 300). It is a lower bound: H1
  is from press and later notices only (two H1/July names surfaced only this week), and four
  volumes are `[?]` (Nordwest, Taptravel, Jøtul, Catena). Annualised over Jan–Oct it is ~1.9%, on
  a lower bound.
- **Trigger status:** not testable. The market-wide reading covers 66 days, less than the full
  quarter the FTD trigger needs (skill Step 5); it reaches a full quarter on 30 Nov. NT's official
  2026 rate comes with the annual report (Feb 2027).
- **Visible at 1 Jan (new entries):** Caybon y (85.5 at end-2025, FF annual report); Achilles,
  Calligo, Proximar, Engebø `[?]`. So far 3 of the logged 2026 FTDs were visible (HX, SIBS, Caybon),
  none is confirmed as not visible, and the rest are `[?]`.

**Fund default record 2026** (FTD events among the tracked funds' holdings; weights at 30 Sep,
after markdowns):

| Fund | FTD events in 2026 | Weight (% of NAV) | Pending |
|---|---|---|---|
| Heimdal Høyrente | HX (Aug), Booster (Sep), Jøtul (Sep) | 1.83 + 0.30 + 0.28 = 2.41 (HX was NOK ~240m in Jan, ~153m in Sep) | Convene 1.10 (FTD `[?]`) |
| Heimdal Høyrente Pluss | HX, Booster, Jøtul | 1.58 + 0.26 + 0.12 = 1.96 | Convene 2.93 (FTD `[?]`) |
| Fondsfinans High Yield | None logged | 0 | — |
| Sissener Corporate Bond | None logged | 0 | — |
| Fondsfinans Kreditt | None logged | 0 | — |
| Arctic Return (reference) | None logged | 0 | — |

- The 2026 defaults among held bonds sit in the two Heimdal workout funds. Those bonds are valued
  as restructurings in the fund analysis, not as named PDs.
- **5 Nov:** none of the names added this run (Achilles, Calligo, Caybon, Proximar, Engebø) is a
  known holding of a tracked fund. Fondsfinans held Caybon at end-2025 (85.5) and sold it during
  2026 (`docs/hy-issuers.md`), so it is not in this record. Holdings beyond the published lists
  are `[?]`.
- **Watchlist:** the held names are in the master watchlist in `docs/hy-issuers.md` (one status
  scale, open entries and an outcome record). The names that are not held are in the Appendix.
- **"Visible at 1 Jan"** is a new column in the log. Most 2026 entries are `[?]`. HX (estimated
  85–90 at the start of 2026, so Stressed) and SIBS (PIK since 2025) were visible. The column tests
  the funds' 2027 zero for unseen defaults (skill F4 item 5).

## Drivers

### Rates (Norges Bank path, NIBOR–policy spread, hedge carry)

- **5 Nov 2026 decision (press release, norges-bank.no, 10:00)** `[F]`: policy rate **kept at
  4.50%** (decided 4 Nov). Main points:
  - "Inflation is too high. It will likely be necessary to keep the policy rate elevated for a
    time, and we are prepared to raise the policy rate if needed" (Governor Ida Wolden Bache).
  - Since September: Middle East uncertainty; oil spot down, futures somewhat up; gas and power
    up; imported price impulses up as expected; **the krone stronger than assumed**; CPI 3.4% and
    CPI-ATE 3.0% (Sep), broadly as projected, but **domestic inflation higher than projected**;
    registered unemployment a bit lower and employment a little higher than projected; capacity
    utilisation slightly below normal.
  - No new forecasts; **MPR 4/26 with the next decision on 17 Dec 2026**.
  - Market reaction: I-44 107.19 → 107.76 and EUR/NOK 10.40 → 10.44 on 5 Nov (krone ~0.5% weaker)
    `[F]`. The zero curve for 5 Nov is not in the API yet `[?]`.
- **Decision on the Base path (the test planned on 24 Oct) `[A]`: keep the MPR 3/26 path.**
  - The Committee saw no material change in the outlook, so the published path is still its
    view. The upward drivers since September (domestic inflation, the labour market, foreign
    rates: the Fed and ECB are priced to hike in December) and the downward one (the krone, ~2–3%
    stronger than assumed) roughly offset. In MPR 3/26's own decomposition (Data K), the krone
    took −0.18 pp off end-2027 for an ~8% move, so a further ~2–3% is worth about −0.05 to −0.1 pp.
  - The market leans higher (+0.17 / +0.33 / +0.71 pp for 2027–29) but has moved toward Base since
    22 Oct; the 2027 gap is below the 0.3 pp test. The 2028–29 gap is partly term premium.
  - Moving Base six weeks before MPR 4/26 on a judgement path would risk a double move. The
    "higher for longer" risk stays in the stagflation side case and the signposts. **Re-test on
    MPR 4/26 (17 Dec):** if its path or the market path sits ≥ 0.25 pp above Base in 2028–29,
    move Base.
  - Effect on the HY numbers if Base took the market path: NIBOR +0.17 / +0.33 / +0.71 pp lifts
    the NOK carry about one for one (the model's carry is NIBOR + spread; the ~45% fixed-rate part
    would give some of it back through rate MTM). The excess return and E / R barely move.
- **Policy rate history** (Norges Bank API) `[F]`: 4.50 → 4.25 (Jun 2025) → 4.00 (Sep 2025) → 4.25
  (May 2026) → **4.50 (25 Sep 2026)** → 4.50 held (5 Nov 2026). Both 2025 cuts are now reversed.
- **Why NB hiked:** inflation has been above target for years, cost growth is strong, and energy
  prices are rising (MPR 3/26). The path holds 4.5% "for a while", then falls gradually from late
  2027 to just under 3.5% by end-2029.
- **Market rates** `[F]` (Norges Bank, 2 Oct 2026): 3M T-bill 4.46, 3Y government 4.79, 10Y 4.59.
  **15 Oct 2026:** policy rate 4.50, NOWA 4.50, 3M T-bill 4.51, 3Y 4.75, 10Y 4.49. Norges Bank's
  financial conditions index −1.58 (loose; −1.50 on 8 Oct).
  **22 Oct 2026:** policy rate 4.50, NOWA 4.50, 3M T-bill 4.52, 3Y 4.77, 10Y 4.49; FCI −1.50
  (still loose; the HY widening has not tightened Norwegian conditions).
  **4 Nov 2026:** policy rate 4.50, NOWA 4.50, 3M T-bill 4.73 (reference bill changed on 29 Oct
  `[A]`), 3Y 4.64, 10Y 4.37; FCI −1.65 (29 Oct; still loose) `[F]`. Rates fell ~12–13 bp after
  the US midterms.
  The 3M money-market rate averaged 4.62 in Q3-26 (NB). NIBOR fixings were not read directly
  (NoRe not accessed; cbonds blocked); OECD/FRED shows 4.51 for Aug 2026.
- **Money-market premium:** 0.22–0.25 pp in 2026 (NB `[F]`), assumed 0.25 pp ahead.
- **Abroad:** the ECB and Fed hiked 25 bp in Sep 2026 and held at end-October; markets price a
  high probability of a hike by both in December and one to two more in 2027 (Riksbank MPU,
  pricing of 2 Nov) `[E]`. NB's trading-partner policy expectation is 3.6–3.7% in 2027–29 (MPR
  3/26); it is likely higher in MPR 4/26 `[A]`.
- **Riksbank, 4 Nov 2026** (press release and Monetary Policy Update, riksbank.se) `[F]`:
  - **policy rate raised 0.25 pp to 2.00%**, effective 11 Nov (1.75% since Sep 2025);
  - guidance: if the outlook for inflation and economic activity holds, the policy rate is likely
    to be raised further in the coming year, in line with the September forecast (~2.4% by Q3-27
    `[E]`, MPR Sep 2026);
  - why: stronger activity, cost increases from supply disruptions and a weaker krona this year
    are expected to lift CPIF and underlying inflation above 2% next year. CPIF 1.5% in September
    (in line), CPIF excluding energy 0.5% (lower than forecast), 3.0% excluding temporary fiscal
    measures; GDP +0.4% q/q in Q3 (GDP indicator) and employment in line; the krona stronger since
    September;
  - risks named: supply disruptions (inflation too high), faster growth, a weaker labour-market
    recovery, global demand (geopolitics, **concerns about AI investments**, weak public finances).
    Swedish credit spreads have increased; financial conditions tightened somewhat but remain
    expansionary;
  - no new forecasts; minutes 10 Nov; **next MPR 16 Dec 2026**.
  - For this baseline: no Swedish row moves. For Swedish issuers (real estate, finance) the hike
    adds ~0.25 pp to STIBOR-linked coupons now and ~0.4–0.6 pp by Q3-27, against a strengthening
    economy. This is a reading of the Riksbank's own path, not a STIBOR forecast.
- **Hedge carry:** NOK-hedged USD bonds earn ~+0.9 pp (SOFR 3.94, 4 Nov), SEK bonds ~+2.65 pp after
  the Riksbank hike (+2.8 before) `[A]`. The NOK base dominates the NOK-hedged return.
- **Norges Bank FX purchases** `[F]`: net purchase of foreign currency (= NOK sale) of **NOK 176m a
  day in November** (300 for the government less 124 to fund the dividend transfer), the same as in
  September and October. The government purchase has not been raised, so the NOK-sale channel
  does not grow in November. The December amount (~30 Nov) and the 2027 budget's petroleum cash
  flow set it next.

### Nordic macro (GDP, unemployment, inflation, property)

- **Norway `[E]`, NB MPR 3/26:**
  - Mainland GDP 1.7% (2025) → 0.9 / 1.0 / 1.0 / 1.3 (2026–29). Total GDP falls in 2028–29 as
    petroleum output declines.
  - Registered unemployment 2.1% (Aug 2026 `[F]`) → 2.4%. The output gap turns negative.
    **Sep 2026: 2.0%** (NAV, unadjusted; 59,413 fully unemployed, −2,542 y/y) `[F]`.
    **Oct 2026: 2.0% seasonally adjusted, unchanged** (+400 persons SA; 59,100 unadjusted, 2.0%;
    NAV, 30 Oct) `[F]`. Construction fell most (foreign workers going home, says NAV). Norges Bank
    (5 Nov) calls registered unemployment "a bit lower than projected".
  - **LFS** (SSB 13760, 22 Oct) `[F]`: 4.6% (3-month average to Aug; trend 4.6% in Sep), flat
    since spring.
  - **Retail sales volume** (SSB 07129, 28 Oct) `[F]`: September −0.4% m/m seasonally adjusted
    (95.5 → 95.1), Q3 flat on Q2, −1.1% y/y. Goods consumption is weak under 4.5% rates;
    services consumption is not in this series.
  - **GDP:** no release since 27 Aug (mainland Q2 +0.3% q/q, June 0.0% m/m) `[F]`. SSB's next
    national accounts (Q3 and September) come on **26 Nov** `[F]`. Base kept (0.9 / 1.0 / 1.0 /
    1.3): Norges Bank sees no material change, and the Regional Network (Sep) showed only minor
    changes.
  - IMF WEO (Oct 2026, via Placera 13 Oct): Norway 1.5% (2026) and 1.3% (2027), total GDP `[E]`. Not
    comparable with Norges Bank's mainland 0.9 / 1.0, so Base is kept.
  - CPI-ATE 3.0% (Sep `[F]`, SSB 9 Oct; CPI 3.4%) → 2.1% by 2029. Wage growth 4.4% (2026).
    **October (SSB 14706, 10 Nov) `[F]`: CPI 3.6%, CPI-ATE 2.7%**, against MPR 3/26's 3.8 / 2.7
    for the month: core on path, headline 0.2 pp below.
  - The import-weighted krone is 8% stronger than in 2025 (I-44 119.6 → 110), and stronger again
    since: **I-44 107.2–107.8 in early November** `[F]` (Norges Bank), "stronger than assumed".
  - Real-estate development remains a stress point: bankrupt developers' share of sector debt
    stayed high through Q1 2026 (Finanstilsynet, June 2026 `[E]`). Finanstilsynet also warns that
    credit is priced with low risk premiums.
- **Sweden `[E]`, Riksbank Sep 2026:** GDP 2.8 / 2.4 / 1.3 (2026–28); the economy is entering a
  boom; unemployment 8.6% falling to 7.6%. **Hiking resumed on 4 Nov (2.00%)**; the Riksbank's
  MPU finds Q3 GDP (+0.4% q/q), employment and unemployment in line with that forecast, so the
  Base is unchanged. September LFS (SCB, 16 Oct) `[F]`:
  8.7% seasonally adjusted, 8.1% unadjusted (8.3% a year earlier); employment +54k y/y. On the
  Riksbank path. For Swedish real estate, that means
  cash flow helped by growth and hurt by rates; net Base stable.

### Fiscal policy and the rate path (added 11 Oct 2026; skill 2026-10-11.7; paths unchanged)

Prompted by the user's view (input, tested here): rising oil-fund spending keeps inflation and
rates high and limits Norges Bank.

| Year | 2016 | 2019 | 2021 | 2023 | 2024 | 2025 | 2026 | 2027 (budget) |
|---|---|---|---|---|---|---|---|---|
| SOBU, % of mainland trend GDP | 7.2 | 7.2 | 9.6 | 9.0 | 9.8 | 11.6 | **12.7** | **12.6** |
| Budget indicator (impulse, pp; average 2001–27 +0.4) | +0.8 | +0.5 | −1.1 | +0.4 | +0.8 | **+1.8** | **+1.1** | **0.0** |
| Withdrawal, % of GPFG (rule: 3%) | 2.7 | 2.8 | 3.1 | 2.9 | 2.6 | 2.6 | 2.7 | 2.7 |
| Fund money, % of state spending | 16.7 | 17.1 | 21.9 | 20.1 | 21.5 | 24.5 | 26.5 | 26.6 |

Source: Nasjonalbudsjettet 2027, chapter 3 figure data (regjeringen.no, Oct 2026) `[F]`. SOBU 2027
NOK 608.4bn. GPFG NOK 21,919bn (23 Sep 2026) `[F]`.

- **What holds:**
  - Fund money in the economy rose from ~7% of mainland GDP (2016–19) to ~12.6% (2026–27). The
    withdrawal rate stayed at 2.6–2.7% only because the fund grew faster (equity returns and a
    weak NOK). The 3% rule is a ceiling on a growing fund, not a brake on the share of GDP.
  - 2025 and 2026 gave the largest impulses outside Covid (+1.8, +1.1 pp).
  - Norges Bank raised its path in September (MPR 3/26, Data K): of the +0.26 pp at end-2027,
    stronger demand (output gap) gave +0.16, wage costs +0.07 and foreign rates +0.09, partly
    offset by the stronger krone (−0.18) `[F]`. Wages 4.4 / 4.0 / 3.6% vs CPI 3.3 / 2.6 / 2.3%
    (2026–28): real wage growth ~1–1.4% a year `[E]`.
  - The market prices a higher path than Norges Bank: ~5.1 / 4.9 / 4.8% NIBOR-equivalent for
    2027–29 on 7 Oct, ~4.96 / 4.72 / 4.57 on 4 Nov (zero curve + NIBOR–T-bill spread) vs Base
    4.79 / 4.39 / 3.86 `[A]`.
- **What does not hold, or is overstated:**
  - The 2027 budget is **neutral** (impulse 0.0); the share of GDP stops rising.
  - Real wages fell in 2016, 2022 and 2023; "above inflation for many years" holds from 2024
    (see the inflation table below).
  - Norges Bank sees a negative output gap (−0.8 / −1.1 / −1.0, 2027–29) and CPI-ATE falling to 2.1%:
    fiscal policy has not removed its room to cut, it has delayed it.
  - "Very unlikely to go down" is not certain: the rule ties spending to a fund that moves with
    global equities and the krone. At 2027 spending, a 20% fall in the fund lifts the withdrawal to
    **~3.4%**, above the rule; a 10% stronger NOK alone lifts it to **~3.0%** `[A]`. An equity
    Bear forces a fiscal choice.
  - The wealth-tax emigration is real but too small to move inflation or rates.
- **Inflation, wages and rates (added 15 Oct 2026):**

| Year | CPI | CPI-ATE (core) | Wages | Real wage (wages − CPI) | I-44 change (+ = weaker NOK) | Money-market rate |
|---|---|---|---|---|---|---|
| 2016 | 3.6 | 3.0 | 1.7 | −1.9 | +1.8 | 1.1 |
| 2017 | 1.8 | 1.4 | 2.3 | +0.5 | −0.8 | 0.9 |
| 2018 | 2.7 | 1.6 | 2.8 | +0.1 | +0.1 | 1.1 |
| 2019 | 2.2 | 2.2 | 3.5 | +1.3 | +2.9 | 1.6 |
| 2020 | 1.3 | 3.0 | 3.1 | +1.8 | +6.7 | 0.7 |
| 2021 | 3.5 | 1.7 | 3.5 | 0.0 | −5.3 | 0.5 |
| 2022 | 5.8 | 3.9 | 4.3 | −1.5 | +1.2 | 2.1 |
| 2023 | 5.5 | **6.2** | 5.2 | −0.3 | **+8.5** | 4.2 |
| 2024 | 3.1 | 3.7 | 5.6 | **+2.5** | +0.8 | 4.7 |
| 2025 | 3.1 | 3.1 | 4.9 | +1.8 | −0.6 | 4.4 |
| 2026 (SSB fcst; Jan–Oct actual) | 3.2 (3.2) | 3.0 (3.0) | 4.3 | +1.1 | −6.2 | 4.5 |
| 2027 SSB / NB | 2.5 / 2.6 | 2.5 / 2.7 | 3.7 / 4.0 | +1.2 / +1.4 | −2.2 / — | 4.6 / 4.8 (NIBOR) |
| 2028 SSB / NB | 2.2 / 2.3 | 2.3 / 2.4 | 3.4 / 3.6 | +1.2 / +1.3 | 0 / — | 4.0 / 4.4 |
| 2029 SSB / NB | 2.1 / 2.1 | 2.1 / 2.1 | 3.0 / 3.4 | +0.9 / +1.3 | 0 / — | 3.8 / 3.9 |

  Annual averages, %. Actuals and SSB forecasts: SSB table 12880 (Economic Survey, 15 Sep 2026);
  monthly CPI: SSB table 14706 (Sep 2026 published 9 Oct). NB: MPR 3/26 Table 3 and the NIBOR path
  above `[F/E]`.
  - **Latest:** Oct 2026 CPI **3.6%**, CPI-ATE **2.7%** (12-month; Sep 3.4 / 3.0; SSB 14706, 10 Nov).
    CPI-ATE has been 2.7–3.4% all of 2026 (Jan–Oct average 3.0), in line with Norges Bank's 3.0%
    for the year; October matches MPR 3/26's monthly projection (2.7).
  - **Core inflation has been above the 2% target for five years** (2022–2026). That supports the
    user's point that inflation is persistent.
  - **The 2026 test:** the krone has strengthened 6% (I-44) this year, which should lower imported
    inflation, yet core inflation is still 3.0%. With wages rising 4.3–4.9% a year, the
    persistence is now domestic (wages and services), not imported. In 2023 it was the opposite:
    core 6.2% came with an 8.5% weaker krone.
  - Both SSB and Norges Bank expect core inflation to reach ~2.1% only in 2029, and both keep the
    money-market rate around 4% or higher through 2028. Neither institution forecasts a quick
    return to low rates `[E]`.
  - Real wages: on average +0.8% a year 2012–2025, but negative in 2016, 2022 and 2023; positive
    at about 1% a year (0.9–1.4%) in every forecast year.
- **Reading for this baseline `[A]`:** Base keeps the Norges Bank path (the default; the gap to the
  market is partly term premium). The risk to the rate path is **upward**: a "higher for longer"
  NIBOR, which raises HY carry (55% FRN) and hurts leveraged non-energy and real-estate issuers.
  That is the stagflation side case's mechanism. **Decided 5 Nov: Base keeps the Norges Bank
  path** (the gap narrowed to +0.17 / +0.33 / +0.71 pp; reasons in Drivers → Rates); re-test on
  MPR 4/26 (17 Dec).

### Energy issuers (translation from oil / rig / supply / shipping baselines)

- **E&P:** Brent Base **84** / 77 / 72 (oil BBB 11 Nov: 2027 88 → 84, the rest unchanged; mid-cycle
  70) keeps cash flows strong: 2027 is still $14 above mid-cycle and $19 above the Bear level, so
  the E&P row is kept (11 Nov note). The front fell after OPEC+ and the midterms (F27 113 → 104 on 3 Nov), and the
  2027 strip (89.7) now sits at Base. Pearl Petroleum is refinancing early (new senior secured
  bond, call exercised 29 Oct); Shamaran's call condition is met (4 Nov): Kurdistan E&P credit is
  being refinanced, not stressed. Kistos (USD 400m) closed its escrow waiver for a 0.10% fee on 20 Oct. The 2025 FTD of 8.3%
  came from small single-asset issuers, not price. Base FTD 3–4%. Bear (Brent 65 / 60 / 60)
  breaks borrowing bases and refinancing for the smaller USD issuers: 8 / 15 / 12%.
- **Oil Service:**
  - Rig Base: drillships **$420k/day at 91% in 2027** (raised from $400k on 4 Nov after two
    Transocean fixtures at $465k and $499k; it was cut from $425k / 93% on 10 Oct), then
    $455–470k for 2028–29. NCS harsh-environment semis are booked through 2027 and largely 2028 at
    $430–517k.
  - Supply Base: North Sea AHTS and PSV term firm; Brazil soft in 2027.
  - Norwegian Oil Service FTD was 0.8% in 2025 `[F]` with the largest market share (15–16%).
  - **Base 1.5% a year, flat 2027–29** (aligned 24 Oct, on user instruction; it was 1.5 / 2.0 /
    2.5). The upstream Base paths do not turn down in the window:
    - rig: drillships $420k at 91% (2027; $400k before 4 Nov) → $455k at 95% (2028) → $470k at
      94% (2029);
      NCS harsh-environment semis $425k → $450k → $470k;
    - supply: North Sea large PSV term £19.5k / 19.0k / 19.5k at 88–89% utilization.
    - So the old rise towards the 3.0% mid-cycle was a drift towards the cycle average, not a
      translation of the sector baselines. The skill requires energy rows to come from them
      (Step 6). Only the ranges widen with the horizon (0.5–3 → 0.5–4), because visibility falls.
    - Bull is 1.0% a year (2028–29 were 1.5, equal to the new Base).
  - In Bear (drillship 400 → 360k, utilization 83%; OSV Bear), 12% at the 2028 peak, below the
    2016 analogue (oil and gas ~23% `[E]`) because 2016–21 restructurings left lower leverage.
    Unchanged.
- **Shipping:** the tanker Base (Oil Shipping BBB, 24 Oct) falls from crisis levels. The crisis
  structure unwinds in H2-27, then the delivery wave (~290 VLCCs in 2027–29, ~38% of the
  compliant fleet) sets 2028–29, with **2029 as the trough** `[E]`:
  - spot TCE, $k/day, Base 2027 / 2028 / 2029 (mid-cycle): VLCC **180 / 50 / 36** (44);
    Suezmax 115 / 44 / 30 (33); Aframax and LR2 65 / 38 / 35 (30); MR 37 / 25 / 22 (21);
  - so VLCC and Suezmax end the window below their mid-cycle; Aframax, LR2 and MR end at or
    slightly above it.
  - *(24 Oct: updated from "VLCC 140 → 65 → 45", which was out of date. The default path was set on
    the same shape — a 2028–29 downturn with a 2029 trough — so the row is unchanged.)*
  - Tankers are a minority of Nordic HY shipping (dry bulk, car carriers and containers too, not
    covered upstream `[A]`).
  - Base FTD 1.5 → 2.5 → 3.5%, above the 3.0% mid-cycle in 2029 because the tanker trough falls
    there.

### Non-energy sectors (real estate, finance, industry, consumer)

- 2025 NT sector FTD `[F]`:
  - Nordic: Convenience Goods 10.9%, Transportation 6.6%, Industry 4.1%, Consumer Services
    2.8%, Real Estate 2.1%.
  - Norway: Convenience Goods 17.5%, Transportation 9.5%, Industry 4.9%, Finance 0.4%.
  - Sweden: Industry 5.8%, Consumer Services 6.1%, Real Estate 2.4%, Finance 1.5%.
- **October adds Swedish real estate and small corporates:** Point Properties Portfolio 1 (property
  sales to repay), SIBS (debt-to-equity), Dooba Finance (events of default), Holmström Fastigheter
  (amendments tied to a disposal).
- **Late October–early November adds Swedish finance and small issuers** (S33): Achilles Capital
  (NPL and secured collections; non-payment of the 19 Oct interest and events of default after a
  maturity extension; EUR 100m amortisation due 31 Dec 2026), Caybon (interest deferral on both
  bonds), Calligo (IT services; bonds written down to zero for equity), Proximar Seafood (missed
  interest), Engebø Rutile (mining; forbearance and a priming super senior bridge). In the held
  book the same theme shows as price stress in Swedish finance: Intrum 73.75 and Trustly 79
  (`docs/hy-issuers.md`). Finance (non-bank) is a secondary row (Base 2.0 / 2.5 / 2.5%); the
  evidence is a cluster of small names, below the 2.0 pp sector minimum, so the row is kept and
  flagged for the next run.
- **2026 defaults cluster in non-Nordic sponsor-backed and consumer names** (log): LR Health &
  Beauty, Nordwest Industrie, Booster, Jøtul, Cabonline, Catena Media, Taptravel, Calligo. Bloomberg
  (Feb 2026) flags weaker covenants among foreign issuers: > $8.6bn of 2025 issuance from
  non-Nordic companies, and > two-thirds of buyers from outside the Nordics `[E]`.

### Primary market and refinancing (issuance, maturity wall, covenants)

- Issuance ~NOK 220bn YTD Sep 2026 (Aug NOK 14bn, Sep NOK 29bn), at record pace; tap issues are
  large; average new-issue size is at a record (NOK 1.4bn in Norway, 2025).
- **October ~EUR 1.9bn (~NOK 20bn)**, EUR 21.1bn YTD (Heimdal) `[E]`: slower than September but
  well above the Bear signpost (< NOK 10bn for two months). Refinancings still clear: Pearl
  Petroleum (new senior secured bond to refinance, 26 Oct), Konzmann moving into the Nimlas
  structure (leverage 3.9x pro forma, majority support), and calls by Shamaran, Andfjord, Avarda,
  Ventura, Airswift and First Mover.
- Covenants (Norway 2025): maintenance 72% (82% in 2024), incurrence 23%, none 5% `[F]`.
  Weakening, but still stronger than in Euro HY.
- Average new-issue tenor 4.2 years (Norway, Q4-25) `[F]`. The maturity wall by year is `[?]`.
- The open market lets weaker issuers refinance today. In Bear it shuts, as in 2016 and March 2020.

### Recovery and restructuring practice

- Restructurings run through bondholder votes or written resolutions with a two-thirds majority,
  often with standstills, interest deferrals, PIK, equity conversion and new money from the
  bondholders themselves (Jøtul in Sep 2026, Convene in Sep 2026, Engebø's super senior bridge in
  Nov 2026).
- **New outcomes (5 Nov):** Calligo's bonds (incl. capitalised and accrued interest) were written
  down to zero on 5 Nov in exchange for equity: recovery = the equity's value, `[?]`. Galileo
  (restructured Dec 2025) is distributing the shares to bondholders and Halliburton. Neither has a
  published value yet.
- Market recovery is measured on price ~30 days after the event; ultimate recovery includes new
  bonds and equity. Both are thinly documented; see Data gaps.

## Signposts and monitoring

| Signpost | Threshold (Bear / Bull) | Now | Previous | Direction |
|---|---|---|---|---|
| Nordic HY spread (Heimdal series) | > 550 bp / < 400 bp | **490 bp (30 Oct)** `[F]`; Base re-marked to it. Early Nov eased globally (Euro HY −14 bp, US −12 bp to 4 Nov) | 430 bp (Sep); ~460 implied to 22 Oct | Wider in Oct; easing early Nov |
| Monthly Nordic HY issuance | < NOK 10bn for 2 months / > NOK 30bn | ~EUR 1.9bn ≈ NOK 20bn (Oct) `[E]` | ~NOK 25.5–29bn (Sep) | Slowing, open |
| Distress notices on Stamdata (deferrals, EoD, standstills, distressed votes) | > 10 issuers a month for 3 months / < 3 | Oct: ~8 issuers + 2 technical; **1–5 Nov: 4** (Achilles, Calligo, Engebø, Booster); monthly series in Default tracking | ~6 (1–23 Oct); ~6–8 (Sep) | Rising |
| Norges Bank policy rate | Cut before Q3-27 (Bear) / hike above 4.75% (stagflation path) | **4.50% held 5 Nov**; "elevated for a time", ready to hike; market path +0.17 / +0.33 / +0.69 pp above Base (10 Nov; +0.71 for 2029 on 4 Nov) | 4.50% (22 Oct); market +0.25 / +0.55 / +0.9 | On path; hiking bias; market gap narrowing |
| Riksbank policy rate (Swedish issuers) | Cut (Bear) / — | **2.00% from 11 Nov** (+0.25); minutes (10 Nov): unanimous, all members expect further hikes over the coming year in line with September (~two more) | 1.75% | Rising, as signalled |
| Brent Dec-27 (oil BBB) | < $70 (Bear) / > $100 (stagflation path) | **Brent Base 2027 avg 84** (oil BBB 11 Nov); 2027 strip 81.2, front F27 91.49 (10 Nov) | Base 88; 2027 strip 89.7, F27 103.6 (3 Nov) | Lower; strip below Base |
| NAV registered unemployment | > 2.6% (Bear) / < 2.1% (Bull) | **2.0% SA (Oct)**: at the Bull threshold, below Norges Bank's projection | 2.0% (Sep, unadjusted) | Flat, low |
| Swedish unemployment (LFS) | > 9.2% / < 8.0% | 8.7% SA (Sep, SCB); Q3 in line with the Riksbank | ~8.6% (2026 avg, Riksbank) | Flat |
| US HY OAS (global context) | > 450 bp / < 280 bp | 332 bp (4 Nov); 344 on 30 Oct | 340 bp (22 Oct) | Peaked late Oct |
| Nordic–Euro HY spread gap | > 250 bp / < 120 bp | **~130 bp** (Nordic 490 vs Euro 359, 30 Oct): just above the Bull level, narrow because Europe widened more. Read as a catch-up risk, **not** a Bull signal | ~105 bp (22 Oct, implied) | Narrow |
| CPI-ATE (Norway) | > 3.3% (stagflation path) / < 2.5% (Bull) | **2.7% (Oct; CPI 3.6%)**, on Norges Bank's projection (2.7; CPI 3.8) | 3.0% (Sep; CPI 3.4%) | Lower, on path |
| Financial conditions (Norges Bank FCI) | > +1 (tight) / — | −1.65 (29 Oct), loose | −1.50 (22 Oct) | Flat |

- **Open checkpoints and data gaps** (status 5 Nov):
  1. HX Hold Co restructuring: terms read (30 Oct, `docs/hy-issuers.md`): old 2030 loan 12.5, In
     restructuring; super senior bonds ~84, Stressed. Counts as an FTD in August `[A]`. **Closed
     for the market log; prices tracked in the issuer file.**
  2. Build the 2026 default log back to January and compute the NT-definition running FTD.
     **Carried;** the market-wide feed is read from 1 Sep to 5 Nov (Metadata). Jan–Aug remains;
     this week's notices exposed two more H1/July FTDs (Achilles, Calligo), so the H1 gap is real.
     Stamdata's old site (www) now needs a subscription; the new site (stamdata.com/news) is public.
  3. Watchlist prices: **partly closed** (held names re-marked in `docs/hy-issuers.md` to 4 Nov:
     Borr ~93, HX super senior ~84, Intrum 73.75, Trustly 79). EHAB, Booster and Convene are still
     `[?]`; the names not held are mostly unpriced.
  4. Confirm the provider of the Heimdal "kredittpåslag" series, and find a longer history.
     **Carried;** DNB Carnegie's figure differs by ~15 bp (445 vs 430 at end-Sep); its October
     figure is due with the Fondsfinans report (~10 Nov).
  5. 3M NIBOR fixings: **carried.** NoRe licenses the data; the site shows no public fixings.
     OECD/FRED shows 4.80 for September (monthly average).
  6. **DNB vintage study confirmed** (DNB page, Feb 2026) `[E]`:
     - ~12% lifetime hard defaults for the 2015–22 cohorts;
     - ~40% of defaults come 1.5–2.5 years after issue, and ~10% within 18 months;
     - the 2023–24 cohorts are defaulting faster than average.
     The BNP AM "5.4% since 2007" definition is still unconfirmed.
  7. Maturity wall 2027–2029 by sector. **Carried.**
  8. Dooba Finance: information due public by 30 Nov (bondholder presentation of 15 Oct circulated
     27 Oct). Point Properties: the committee's solution before the extended maturity on 30 Nov.
     SIBS: whether its first default was in 2025 (PIK) or 2026 (conversion). Taptravel: **vote
     approved 9 Nov**; effective when the ≥ SEK 50m share issue closes (longstop 31 Mar 2027).
     Booster: standstill to 1 Dec. **Carried.**
  9. (18 Oct) Fill "visible at 1 Jan" for every 2026 log entry. **Carried** (Caybon filled: y).
  10. (24 Oct) **October anchor spread: closed.** Heimdal printed 490 bp; the stub, the 2027 MTM
      and the Base path were re-marked (change log 5 Nov). DNB Carnegie cross-check carried to
      checkpoint 4.
  11. (24 Oct) Rebellion Capital: what sits behind the covenant reset (Q3 report). **Carried.**
  12. (New, 5 Nov) **November anchor spread** (Heimdal, early Dec): if it is ≤ 440 bp (the
      October widening reversed), re-mark Base back toward the old path; if ≥ 540, test the Bear
      signpost (550).
  13. (New, 5 Nov) **NIBOR path re-test on MPR 4/26 (17 Dec):** move Base if the new Norges Bank
      path, or the market path, sits ≥ 0.25 pp above or below Base in a window year.
  14. (New, 5 Nov) Engebø Rutile (forbearance, priming super senior bridge) and Achilles Capital
      (EoD; EUR 100m amortisation due 31 Dec): outcomes and recoveries. Calligo and Galileo: value
      of the equity received.
  15. (New, 5 Nov) Finance (non-bank) row: Swedish finance stress (Achilles, Intrum, Trustly).
      Test the row (Base 2.0 / 2.5 / 2.5%) at the next full run against the Q3 reports (Trustly
      25 Nov) and the Achilles outcome.
- **Next decisive observations:**
  - Fondsfinans and Sissener October reports (~10 Nov): DNB Carnegie's October spread and the
    issuance figures;
  - SSB national accounts Q3 (26 Nov); NAV unemployment for November (end-Nov/early Dec); SSB
    November CPI (10 Dec); (11 Nov: October CPI, the Riksbank minutes, Taptravel's vote, the oil
    update and the Fondsfinans October report are read; see the 11 Nov note);
  - the rig and supply full updates (on hold to 11 Nov);
  - Dooba, Point Properties (30 Nov); Booster's standstill (1 Dec); Achilles' EUR 100m
    amortisation (31 Dec); Taptravel's share issue (longstop 31 Mar 2027);
  - the November anchor spread (early Dec); Riksbank MPR (16 Dec); Norges Bank MPR 4/26 (17 Dec).

## For fund analyses and IAF

- **11 Nov: no material change** (October CPI, Riksbank minutes, Taptravel, oil Base 2027 84,
  DNB CMD read; every Interface value and the reference E / R 0.254 kept).
- **5 Nov: material change for fund analyses** (the fund run is on hold until the Sissener and
  Fondsfinans October reports, ~10 Nov):
  - **Market reference E / R: 0.196 → 0.254** (E_mkt 1.82 → 2.15 pp after the 0.6% fee
    convention; R 9.28 → 8.47 pp). Sensitivity with Bear read as a shock size: 0.216.
  - **Spread path for β = 1 fund carry:** Base 490 / 490 / 490 / 495 (stub / 2027–29), not 430 /
    440 / 460 / 470. Every fund's carry rises ~0.5 pp in 2027, and its Bear 2027 MTM shrinks with
    the wider start, as the market's does. The fund ratios and the reference move together, so
    verdicts may change in either direction: re-run all six funds.
  - **Stub:** October was −0.2% for the index; use each fund's own October return (the Heimdal
    reports and NAVs are in `docs/hy-issuers.md`).
  - NIBOR path, default rates, LGD and the sector rows used for the Bear catalyst loss are
    unchanged.
- **24 Oct (later): Oil Service Base default row aligned** to 1.5% a year in 2028–29 (was 2.0 /
  2.5). For funds, the Bear catalyst loss on the performing book uses Bear − Base sector rates, so
  the Oil Service gap widens by 0.5 pp (2028) and 1.0 pp (2029). For an oil-heavy fund that adds
  about 0.02–0.05 pp a year in Bear 2028–29 `[A]` (weight × gap × 65% LGD × q). R uses 2027
  only. Apply it at the next fund run.
- **24 Oct and 17 Oct:** no material change for fund analyses (reference 0.196 then); details in
  the change log.
- **Fund analyses:** use the Interface tables. The market Base window return is **7.2%** before
  fees (NIBOR + 2.75 pp). The market's stress loss R (Base 2027 − Bear 2027) is **8.47 pp**.
  - **Market reference for the yield-versus-risk rule:** E_mkt after a 0.6% fee = **2.15 pp**, so
    E / R = **0.254**.
  - Funds are judged on their own E / R against this, not on yield alone (skill 2026-10-06.2).
- **IAF:**
  - The NIBOR path (Base 4.79 / 4.39 / 3.86) is for NOK floating-rate debt service: unchanged.
  - Refinancing in Bear: add ~300 bp to the issuer's spread and assume no market access for 2–3
    quarters in 2027.
  - New-issue spreads (2025): E&P ~620 bp, Oil Service ~520 bp (Norway), Real Estate ~430 bp. The
    secondary market is ~60 bp wider than at end-September (490 bp); no October new-issue spread
    by sector is published in the sources read `[?]`.
  - Riksbank: 2.00% from 11 Nov, further hikes likely in 2027 (for Handelsbanken and Swedish
    issuers; a reading, not a STIBOR path).
- **Issuers on the watchlist that are IAF companies:** **Borr Drilling** (`docs/borr-analysis.md`):
  Watch since 4 Nov, notes ~93 derived (`docs/hy-issuers.md`). DOF, CAPT, SED and Hafnia are not on
  it.

## Change log

- **11 Nov 2026 — small update (note); HY Market BBB kept unchanged** (skill 2026-11-08.1;
  iaf-valuation 2026-11-10.1; baseline date stays 5 Nov; causes: Taptravel vote 9 Nov, SSB
  October CPI 10 Nov, Riksbank minutes 10 Nov; also read: oil BBB 11 Nov, DNB CMD 10 Nov):
  - **Unchanged:** every Interface value (policy rate and NIBOR paths, GDP and unemployment,
    spreads, FTD and LGD, returns, mid-cycle), scenario definitions, weights and the market
    reference E / R 0.254.
  - **Text updated:** the 11 Nov note at the top; oil upstream row, E&P driver and Base scenario
    row (Brent 2027 88 → 84); signposts (CPI-ATE 2.7% Oct; Riksbank minutes; Brent; market path
    10 Nov); inflation lines; Taptravel log and watchlist rows; checkpoint 8; next observations;
    sources S38–S41.
  - **Reason:** October CPI-ATE on Norges Bank's projection (2.7) and CPI below it (3.6 vs 3.8);
    the Riksbank minutes confirm the September path (no Swedish row moves); Taptravel's approved
    amendments are a re-default of a July FTD on a tiny volume; oil Base 2027 −$4 leaves the E&P
    row far from its Bear stress; the market path is unchanged (+0.17 / +0.33 / +0.69 pp); DNB's
    view is one house's, below the trigger list. None moves a value by the minimum change.
  - **Fund analyses and IAF:** no material change.
- **5 Nov 2026 — update; HY Market BBB changed** (skill 2026-10-24.1; iaf-valuation 2026-11-01.1;
  new baseline date 5 Nov; triggers: the October anchor spread ≥ 480 bp, the Norges Bank decision
  of 5 Nov, the Riksbank decision of 4 Nov):
  - **Changed (previous → new):**
    - Nordic HY spread, Base annual avg: stub 430 → **490**; 2027 440 → **490**; 2028 460 →
      **490**; 2029 470 → **495**. Year-end: 450 / 465 / 475 → **490 / 495 / 500**. Bear 2027 avg
      650 → 680; Bull 2027 avg 410 → 440 (start effect only). Mid-cycle 500 unchanged.
    - Expected NOK return, Nordic HY: stub 1.9 → **1.1** (all scenarios); Base 2027 7.0 → **8.0**,
      2028 6.7 → **7.2**, 2029 6.4 → **6.8**, window 6.8 → **7.2**; Bear 2027 −2.2 → **−0.4**,
      window 5.6 → **6.0**; Bull 2027 8.9 → **10.7**, window 7.4 → **7.7**. Excess, Base window
      2.4 → **2.75**.
    - Norway HY: stub 2.0 → 1.2; Base 8.4 / 7.6 / 7.1 (7.4 / 7.1 / 6.7); window 7.2 → 7.5; Bear
      2027 −3.4 → −1.4; Bull 2027 9.3 → 11.1.
    - **Market reference E / R 0.196 → 0.254** (E 1.82 → 2.15; R 9.28 → 8.47).
    - Risk premium Base 275 / 267 / 277 → 325 / 297 / 302 bp. Return ranges shifted +0.5–1.0 pp.
    - Market path check row: 4 Nov ~4.96 / 4.72 / 4.57 (22 Oct ~5.05 / 4.95 / 4.75).
  - **Unchanged:** policy rate and NIBOR paths (all scenarios, Year-1 quarters, mid-cycle);
    Norway and Sweden GDP and unemployment; fiscal block; FTD rates per row and the market rate;
    LGD; EL; scenario definitions and catalysts; 25/50/25 weights; mid-cycle values.
  - **Reason and evidence:**
    - Spread: Heimdal's October reports print the Nordic spread at 490 bp (+60), with Europe +90
      and the US +50; the DNB Carnegie Nordic HY index returned −0.2% in October. The move exceeds
      the 50 bp minimum and the 24 Oct trigger. The start is now at the 500 bp normal, so the Base
      drift to normal is complete; the path is re-marked as one. Catalyst levels for Bear (850)
      and Bull (390) are kept.
    - Rates: Norges Bank held 4.50% with unchanged guidance and a hiking bias, and saw no material
      change in the outlook; the market path moved toward Base. The Riksbank hiked to 2.00% as
      signalled. Neither moves a Base point by the minimum change.
    - Macro: NAV unemployment 2.0% SA (Oct), retail −0.4% m/m (Sep), LFS 4.6%; no GDP release; the
      Riksbank finds Q3 in line. Below the 0.5 pp GDP threshold.
    - Defaults: Stamdata 19 Oct–5 Nov (S33, pages 1–2): new log entries Proximar, Caybon (FTD
      reclassified), Achilles and Calligo (H1/July FTDs found late), Engebø (pending), Konzmann,
      Thon, Banco Plata, Grøntvedt (routine) and several calls. Pace ~2.2% a year over 66 days:
      inside Base. Running replica ≥ 1.6% by 5 Nov (lower bound).
    - Energy: rig 4 Nov ($420k / 91% drillships, text updated), oil 4 Nov and supply 4 Nov kept.
    - US midterms: lower global yields and tighter HY OAS in early November; no path change.
  - **Forecast vs actual (stub Q4-26):** October actual −0.2% (index) against ~+0.6% expected for
    the month (carry less EL): a ~0.8 pp miss, all spread MTM, not loss. The stub is now 1.1%.
  - **Default log:** see Default tracking and the Appendix (S33 rows).
  - **Weights:** 25/50/25 kept.
  - **Fund analyses:** must re-run on the new reference (on hold by the user until ~10 Nov).
- **24 Oct 2026 (later) — text correction, Shipping driver** (user instruction; no value
  changed): the tanker rates quoted under Drivers → Shipping were out of date (VLCC 140 → 65 →
  45k/day). They now match the Oil Shipping BBB of 24 Oct (VLCC 180 / 50 / 36, mid-cycle 44; the
  other segments added). The Shipping FTD row (1.5 / 2.5 / 3.5) already follows that shape, so
  it is kept.
- **24 Oct 2026 (later) — consistency correction: Oil Service default row aligned with the rig and
  supply baselines** (user instruction; the baseline date stays 24 Oct):
  - **Changed (previous → new):**
    - Base FTD Oil Service 2028 2.0 → **1.5**, 2029 2.5 → **1.5** (2027 stays 1.5);
    - ranges 1–4 → 0.5–3.5 (2028) and 1–5 → 0.5–4 (2029);
    - Bull 2028 1.5 → **1.0**, 2029 1.5 → **1.0**.
  - **Unchanged:** Bear (4 / 12 / 10, from the rig and supply Bear paths), mid-cycle (3.0), the
    other rows, the market points (3.0 / 3.5 / 3.5), returns, spreads and the market reference.
  - **Reason:**
    - The 2028–29 rise was a drift towards the cycle average. The rig and supply Base paths
      firm instead: drillships $400k → $455k → $470k at 91–95% utilization, NCS harsh-environment
      semis $425k → $470k, North Sea PSV term about £19–19.5k.
    - The skill takes energy rows from the sector baselines (Step 6), never from a drift.
  - **Minimum change:** the move (0.5–1.0 pp) is below the 2.0 pp sector-row minimum. It is
    applied as a correction of an inconsistency, not as new evidence.
  - **Knock-on (noted, not re-marked):**
    - Σ rows now sits 0.08–0.13 pp below the Base market rate in 2028–29 (Reconciliation);
    - Norway Base FTD 2.9 / 3.3 / 3.35;
    - Oil Service Base EL 110 → 83 bp a year, premium ~410 → ~440 bp;
    - fund Bear catalyst loss +0.02–0.05 pp a year in 2028–29 for oil-heavy funds.
    - All are below their minimum changes.
- **24 Oct 2026 — update; HY Market BBB kept unchanged** (skill 2026-10-24.1; new baseline date
  24 Oct):
  - **Unchanged:** all Interface values (rates, macro, spreads, FTD per row, LGD, EL, returns,
    mid-cycle), the scenario definitions and the 25/50/25 weights. The market reference ratio stays
    0.196. Only the market path check row is re-dated (22 Oct: ~5.05 / 4.95 / 4.75).
  - **Upstream:** oil (24 Oct, kept unchanged), tanker (24 Oct, stub only), rig (22 Oct small
    update, kept unchanged), supply (17 Oct). None flags an HY change.
  - **Data refreshed:** Norges Bank rates, zero curve and FCI at 22 Oct; Euro and US HY OAS 354 /
    340 bp (22 Oct); SOFR 3.90; Swedish LFS for September; Fondsfinans NAVs to 22 Oct; Stamdata
    13–23 Oct (S25).
  - **Tests (pre-mortem):**
    - **Spreads (closest call):** Euro HY +18 bp and US HY +17 bp in the week; Nordic ~+30 bp in
      October, implied from FF HY's NAV `[A]`. Inside the Base range, below the 50 bp minimum
      change and far from the Bear signpost. A re-mark trigger at ≥ 480 bp is set for the October
      print (checkpoint 10).
    - **Defaults:** no new FTD 16–23 Oct; the pace over 1 Sep–23 Oct is ~2.2% a year, inside the
      Base range. Rebellion's covenant reset is a warning sign only (Watch).
    - **Rates:** unchanged; the market path is 0.25–0.9 pp above Base, as before. Base is kept
      until 5 Nov.
    - **Macro, energy:** no change.
  - **Forecast vs actual (stub Q4-26):** October to the 22nd ~−0.2% (fund proxy) against ~+0.45%
    of carry net of EL. The quarter tracks ~1.2% vs 1.9%. The miss (~0.65 pp) is spread MTM; it is
    below the 1.0 pp minimum: noted, not applied.
  - **Default log:** Taptravel recapitalisation proposal (vote 9 Nov); Rebellion Capital covenant
    reset (Watch); DistIT working-capital cap (routine; Watch, post-restructuring); Kistos adopted
    (routine, closed); Dooba information call (pending); Elcano EGM; calls by Ventura Offshore,
    Airswift and First Mover Group.
  - **Weights:** 25/50/25 kept.
- **18 Oct 2026 — amendment: default tracking** (review `docs/review-hy-funds-and-defaults.md`;
  skill 2026-10-18.1). **No value changed**; the baseline date stays 17 Oct.
  - **Added:** a Default tracking section (monthly table, running FTD replica, trigger status,
    fund default record), a "visible at 1 Jan" column in the log, and the scan coverage, stated
    once in Metadata.
  - **Watchlist:** on the skill's status scale. The held names moved to the master watchlist in
    `docs/hy-issuers.md`; the appendix keeps the names that are not held.
  - **Default pace restated from the log:** ~2.6% a year over the market-wide window 1 Sep–16 Oct.
    The Conclusion said "~3–4% for Aug–Oct", which could not be reproduced. It is still inside
    Base's 2.0–4.0% range, so the conclusion holds.
  - **Hofseth's clean price** at 30 Sep is ≈ 74 (76.2 − 0.25 × 8.244), not ≈ 75.
  - The change log is in date order, and the checkpoints are numbered.
- **17 Oct 2026 (later) — sector spread vs loss table added** under Defaults (user question). No
  value changed.
- **17 Oct 2026 — update; HY Market BBB kept unchanged** (skill 2026-10-15.1; new baseline date
  17 Oct):
  - **Unchanged:** all Interface values (rates, macro, spreads, FTD per row, LGD, EL, returns,
    mid-cycle), the scenario definitions and the 25/50/25 weights. The market reference ratio stays
    0.196.
  - **Added** (template rows): fiscal (SOBU 12.7 / 12.6% of trend GDP; withdrawal 2.7%; impulse
    +1.1 / 0.0) and the market path check (~5.0 / 4.9 / 4.75%).
  - **Data refreshed:**
    - rates at 15 Oct and the FCI;
    - Euro and US HY OAS (336 / 323 bp);
    - NAV unemployment 2.0% (Sep);
    - IMF October WEO (Norway);
    - Fondsfinans 30 Sep holdings prices for the watchlist;
    - Stamdata scan 6–16 Oct.
  - **Tests (pre-mortem):**
    - **Defaults:** the Aug–Oct pace is ~3–4% a year: within range, upper half.
    - **Spreads:** Nordic 430 is on path, but Europe widened 57 bp. The catch-up risk is noted;
      no Bear signpost is crossed (Nordic > 550, US > 450).
    - **Rates:** the market path is above Base by 0.2–0.9 pp. Base is kept until the 5 Nov decision.
    - **Energy:** oil +$3 and drillships −6% net out.
    - **Bull signposts:** NAV unemployment and the Nordic–Euro gap are at their Bull thresholds,
      but the gap narrowed for the wrong reason (Europe widening).
  - **Forecast vs actual (stub Q4-26):**
    - October to the 15th is ~0% (fund NAV proxy) against ~+0.3% of carry; the quarter tracks
      ~1.6% vs 1.9%.
    - The miss is spread MTM (~20 bp of implied widening), not loss.
    - It is below the minimum change: noted, not applied.
  - **Default log:**
    - new FTDs: Point Properties Portfolio 1 (maturity extensions without redemption; first in
      July), SIBS (debt-to-equity conversion; the first default may be the 2025 PIK amendment);
    - Dooba Finance events of default: pending;
    - routine or technical: Kistos (escrow waiver for Block 9; closes the 6 Oct item), Brightstar
      (hedge counterparty waiver), Keystone (100% vote), Storsala (2-day technical payment delay with
      default interest).
- **15 Oct 2026 amendment (skill 2026-10-15.1):** inflation, wage and real-wage table added to
  the fiscal block (SSB 12880 and 14706, NB MPR 3/26); Sep 2026 CPI/CPI-ATE updated. No path
  changed; it strengthens the "higher for longer" risk already flagged.
- **11 Oct 2026 amendment (skill 2026-10-11.7):** fiscal block added under Drivers (oil-fund
  spending, Norges Bank's rate-path decomposition, market path check). **No path changed**; the
  upward risk to NIBOR is flagged for the next update.
- **11 Oct 2026, data addendum (no model change; baseline kept, still current):**
  - **Upstream:** the oil, rig, supply and tanker baselines were renewed on 10 Oct. None flags an
    HY change. The oil baseline notes a stronger inflation channel for non-energy issuers, from
    higher diesel cracks (Q4-26/H1-27); that is consistent with the Base rate path.
  - **September tracking** (fund reports `[E]`):
    - the DNB Nordic HY index returned +0.1% in September and 5.9% YTD (Fondsfinans);
    - Nordic HY held up while iTraxx Crossover widened 53 bp and long rates rose sharply;
    - issuance was ~NOK 25.5bn in September (Sissener; Heimdal ~29bn) and ~NOK 220bn YTD
      (Heimdal).
    - The Sep spread from Heimdal's report is 4.3% (Aug 4.5%). That is on the Base path.
  - **Watchlist:**
    - Hofseth ~72.5 (FF: "trading at 70–75"; needs new equity);
    - Kistos (Oman approval, leverage < 1x) and Eldorado (first rig contract) read as positive;
    - W&T Offshore noted (a Sissener position; price stale).
  - **Reference fund:** Arctic Return added in fund mode (skill 2026-10-11.1). The market reference
    ratio is unchanged.
- **6 Oct 2026, holdings addendum (no model change):** watchlist prices from the Fondsfinans
  holdings (Hofseth 77.0, Sigma 81.6, Magnolia Bostad 86.4, Varel 89.9) and HX weights from the
  Heimdal holdings pages.
- **6 Oct 2026, data addendum (no model change; paths unchanged):**
  - Aug 2026 spread 450 bp and DNB Carnegie Aug +1.0% added from the Høyrente Pluss August report.
  - HX Hold Co restructuring added to the log and watchlist; Trustly added to the watchlist.
  - None moves a point value by the minimum change: HX is small relative to the market.
- **5 Oct 2026 — new baseline** (initial; no previous values). All rows, series, paths,
  mid-cycle values and catalysts are new.
  - **Forecast vs actual:** not applicable (initial). 2026 tracking to date: DNB Carnegie Nordic HY
    +6.1% YTD (Sep), Nordic spread 484 → 430 bp from Feb to Sep.
  - **Weights:** 25/50/25 convention set.
  - **Method notes, logged in the skill (revision 2026-10-05.2):**
    - Norwegian unemployment uses registered (NAV); Sweden unemployment added.
    - Sector FTD rows in the credit Interface are listed one per row.
    - NT's FTD comes on two bases in the same report: the quarterly LTM chart (Nordic 2.6% at
      Q4-25) and the annual sector table on average outstanding (Nordic 2.9%). The LTM chart is the
      anchor; sector rates are on the table's basis.
  - New baseline date: **5 Oct 2026**.

## Appendix

### Default and distress log, 2026 (incomplete: coverage in Metadata — market-wide feed 1 Sep–5 Nov, held companies 4 Aug–23 Oct, H1 from press and later notices)

Volumes in NOK at the FX in Metadata. "FTD" follows the NT definition: non-payment, or a change
to terms without adequate compensation. `[A]` marks classifications made without the full
proposal.

| Issuer | ISIN | Row | Currency | Outstanding NOKm | Event | Date | FTD y/n | Visible at 1 Jan | Price before / after | Recovery | Source | Tracked funds holding |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LR Health & Beauty SE (DE) | SE-law bond | Consumer | EUR 130m | ~1,400 | Restructuring, ~1/3 written off | H1 2026 (reported 24 Feb) | y | `[?]` | `[?]` | ~67 ultimate `[E]` | Bloomberg via Swissinfo | `[?]` |
| Nordwest Industrie Group (DE) | `[?]` | Industry | `[?]` | `[?]` | Court-enforced restructuring within a year of issue | H1 2026 | y `[A]` | `[?]` (default within a year of issue) | `[?]` | `[?]` | Bloomberg via Swissinfo | `[?]` |
| Taptravel Nordic AB (SE) | NO0013699975 (super senior, max SEK 124m, 2025/28), NO0013326041 (senior secured PIK toggle, 2024) | Consumer | SEK ≤ 124m super senior + senior `[?]` | `[?]` | Missed interest 3 Jul 2026 and 3 Oct 2026; covenant breaches. **23 Oct:** written procedures on both bonds: Ridge Capital to subscribe ≥ SEK 50m in a share issue and take control; missed coupons paid in cash by 31 Mar 2027 without default interest; from 3 Jan 2027 interest 6% cash + 4% PIK (total 10% unchanged); equity cure added. Votes close 9 Nov; > 50% indicated support. The issuer says it likely cannot meet its obligations without the share issue. **9 Nov: both written procedures approved** (quorum met; ≥ 66⅔% in favour); effective on conditions precedent (EGM, ≥ SEK 50m share issue with Ridge Capital at ≥ 80% after, longstop **31 Mar 2027**, failure = event of default). Terms per the 23 Oct notice: senior 8% PIK from 3 Oct 2026, maturity 31 Oct 2028 → 30 Apr 2030; super senior maturity 30 Jun 2028 → 31 Dec 2029; deferred interest in cash by 31 Mar 2027. A re-default, not a new FTD | 3 Jul 2026 (FTD); 23 Oct (proposal); 9 Nov (approved) | y (Jul) | `[?]` | `[?]` | `[?]` | Stamdata, NT notices 5 Oct and 23 Oct (read 24 Oct); MFN releases 24 Oct and 9 Nov (read 11 Nov) | — |
| Booster Precision Components Holding GmbH (DE) | NO0012713520 (also NO0013754499) | Industry (auto) | EUR ≤ 60m | ~650 | Events of default; written procedure; standstill prolonged; **2 Nov: standstill with the ad hoc group extended to 1 Dec 2026** ("constructive discussions") | 3 Sep 2026 | y `[A]` | `[?]` | `[?]` | `[?]` | Stamdata, NT notices 3 Sep, 22 Sep, 1 Oct, 2 Nov | Heimdal Høyrente (small; −0.02 pp in May) |
| Jøtul AS (NO) | multiple | Consumer | NOK | `[?]` | Written resolution; recapitalisation with new bondholder capital | 2 Sep 2026 (completed Sep) | y `[A]` | `[?]` | `[?]` | `[?]` | Stamdata; Heimdal Sep report | Heimdal Høyrente |
| Catena Media plc | SE0014262192 | Other (media) | SEK | `[?]` | Interest deferral | 30 Sep 2026 | y | `[?]` | `[?]` | `[?]` | Stamdata | — |
| Cabonline Group Holding AB (SE) | SE0017767346 + 1 | Transportation | SEK 1,225m | ~1,170 | Interest deferral on secured notes | 2 Oct 2026 (stub) | y | `[?]` | `[?]` | `[?]` | Stamdata, issuer notice | — |
| Island Offshore Shipholding LP (NO) | NO0010673866, NO0010760507 | Oil Service | NOK | `[?]` | Written resolution adopted on legacy 2013/2016 bonds | 1 Oct 2026 | n (legacy, previously restructured) `[A]` | — | — | — | Stamdata, NT | — |
| North Investment Group AB (SE) | SE0015938493 | Real Estate/Finance | SEK | `[?]` | Event of default — delisting | 21 Sep 2026 | n (technical) `[A]` | — | — | — | Stamdata | — |
| Convene Midco S.à r.l. | NO0012883174 | Other | NOK | `[?]` | Written resolutions with a subscription (new money) | Sep 2026 | `[?]` | `[?]` | `[?]` | — | Stamdata; Heimdal Sep report (new NOK 250m bond) | Heimdal Høyrente |
| Caybon Holding AB (SE) | SE0023950902 (SEK 180.6m super senior 2025/28), SE0021923562 (SEK 130m senior secured 2024/29) | Other | SEK 310.6m | ~295 | Written procedure → amended and restated terms (21–23 Sep). **30 Oct: the issuer elects to defer all interest due 27 Nov (super senior) and 3 Dec (senior) to redemption**, under the deferral clauses of the terms | 21–23 Sep 2026; 30 Oct (deferral) | **y `[A]`** (reclassified 5 Nov: deferral without compensation; dated to the Sep amendment) | y (85.5 at end-2025, FF annual report) | 85.5 (YE-25) / `[?]` | `[?]` | Stamdata (S33: two deferral notices, 30 Oct) | — (FF sold in 2026) |
| Solteq Oyj (FI) | FI4000442264 | Telecom/IT | EUR | `[?]` | Written procedure, revised proposal, outcome | 17 Sep 2026 | `[?]` | `[?]` | — | — | Stamdata | — |
| HX Hold Co (formerly Hurtigruten Expeditions) | NO0010874548 (EUR 258m 7% senior secured), NO0013465997 (EUR 130m 12.5% senior secured 2025/30) | Consumer (cruise) / Transportation | EUR 388m | ~4,200 | Restructuring: written resolutions adopted 13 and 17 Aug 2026 (summonses 29 Jul and 6 Aug); secured on two modern expedition ships | Aug 2026 | likely y `[A]` (terms not public) | y `[E]` (~85–90 at the start of 2026) | `[?]`; about −26% in Aug (Heimdal contribution −0.56 p.p. at ~2.2% weight); estimated ~50–60 `[E]` | `[?]` | Stamdata notices; Heimdal reports (Aug, Sep 2026) | Heimdal Høyrente 1.83%, Pluss 1.58% |
| Kistos Holdings PLC | NO0013741843 | E&P | USD 400m | ~3,840 | Written resolution summoned 5 Oct: waiver to release the USD 20m second escrow amount into the Block 9 SPA escrow, with a first-priority pledge for bondholders and long-stop mechanics (summons read 17 Oct). **Adopted 20 Oct with a 0.10% amendment fee** | 6 Oct 2026; adopted 20 Oct | **n (routine; closed)** | — | — | — | Stamdata (5 and 20 Oct); FF Sep report | Fondsfinans 0.69% |
| Eldorado Drilling BondCo | NO0013756023 | Oil Service | USD | `[?]` | Bond terms amended (purpose not read); first contract for the Deep Value Driller in Sep (FF) → not distress `[A]` | 29 Sep 2026 | n (read) `[A]` | — | — | — | Stamdata; FF Sep report | Fondsfinans 0.92% |
| Point Properties Portfolio 1 AB (SE) | SE0015556535 | Real Estate | SEK 800m | ~770 | Written procedures: maturity extended 6 months (Jul 2026, to 15 Oct) and again 6 weeks (adopted 15 Oct, to 30 Nov 2026); the issuer cannot redeem; its whole property portfolio is for sale; a bondholder committee is negotiating a longer solution | Jul 2026 (first extension); 15 Oct 2026 | y `[A]` (extension without redemption; compensation `[?]`) | `[?]` | `[?]` | `[?]` | Stamdata, NT notices 25 Sep and 15 Oct | — |
| SIBS AB (publ) (SE) | SE0023112487 | Other / Industry `[?]` | SEK ≤ 1,000m (SEK 633m after the conversion, incl. PIK) | ~610 | Amended and restated terms 9 Oct 2026: partial debt-to-equity conversion under the July 2026 written procedure; PIK interest since the 2025 written procedure | 9 Oct 2026 (effective) | y `[A]` (first default possibly 2025, PIK) | y (PIK since 2025) | `[?]` | `[?]` | Stamdata (amended terms, 9 Oct) | — |
| Dooba Finance AB (SE) | NO0013739201 (SEK 770.5m super senior 2026/29), NO0013219493 (SEK ≤ 300m senior 2024/31) | Real Estate/Finance `[?]` | SEK ~1,070m | ~1,030 | Events of default: cross-default on a bridge loan (Carlyon Bay Project) and failure to deliver audited accounts; information call 15 Oct | 6 Oct 2026 | pending `[A]` (EoD, no payment default yet) | `[?]` | `[?]` | — | Stamdata, NT notices 6 and 12 Oct | — |
| Storsala AB (SE) | SE0029279777 | Real Estate | SEK 300m | ~290 | Interest due 5 Oct paid on 7 Oct (technical CSD/bank error), with default interest | 7 Oct 2026 | n (technical) | — | — | — | Stamdata | — |
| Solis Bond Company DAC | NO0010914914 (2021/24 senior secured green, still outstanding) | Utilities | `[?]` | `[?]` | Information call on status and next steps | 9–15 Oct 2026 | n (legacy, earlier default) `[A]` | — | — | — | Stamdata | — |
| Futura Resources Ltd (AU, coking coal) | `[?]` (Jan 2026 bond) | Other (mining) | `[?]` | `[?]` | Trustee commissioned an independent technical due-diligence review of the mines | 2–12 Oct 2026 | n (monitor) | — | — | — | Stamdata | — |
| Specac International Ltd (UK) | NO0013736975 | Industry | `[?]` | `[?]` | 2025 audited accounts late (auditor change); information to bondholders | 18 Sep / 6 Oct 2026 | n (technical) | — | — | — | Stamdata | — |
| Brightstar Resources Ltd | NO0013698365 (USD 120m 12.5% 2026/30) | Other (gold mining) | USD 120m | ~1,150 | Written resolution adopted (69.5%): a BB+ hedge counterparty accepted and a guarantor added | 14 Oct 2026 | n (routine) | — | — | — | Stamdata | — |
| Keystone Academic Solutions AS | NO0013462671 (EUR 200m FRN 2025/29) | Other | EUR 200m | ~2,180 | Minimum-liquidity covenant added (24 Sep); written resolution adopted with 100% (7 Oct); purpose not read | 7 Oct 2026 | n (routine `[A]`) | — | — | — | Stamdata | — |
| Brödernas Group AB (SE) | NO0013250597 | Consumer | SEK | `[?]` | Distribution from bankruptcy estates (earlier default) | 25 Sep 2026 update | (earlier year) | — | — | `[?]` | Stamdata | — |
| Holmström Fastigheter (SE) | `[?]` | Real Estate | SEK | `[?]` | Amendments tied to a disposal | Oct 2026 | n (routine `[A]`) | — | — | — | Stamdata (S17) | — |
| Rebellion Capital AB (SE) | SE0023113790 (SEK ≤ 1,000m senior secured FRN 2024/28) | Other `[?]` | SEK ≤ 1,000m | ≤ ~960 | Leverage maintenance covenant reset from 4.50x to 5.50x, for a 0.20% consent fee (agreed in principle with ~40% of holders; adopted 20 Oct, effective 20 Oct). Leverage 3.99x at 30 Jun 2026; R12 operating FCF SEK 117m; RCF SEK 90m undrawn; cost cuts SEK 19.5m | 1 Oct 2026 (notice); 20 Oct (adopted) | n (compensated covenant relaxation: a warning sign, not a default) | — | `[?]` | — | Stamdata (notices 1 Oct and 21 Oct, read 24 Oct) | — |
| DistIT AB (publ) (SE) | SE0015949359 (originally SEK ≤ 300m senior unsecured FRN 2021/28, STIBOR + 4.50%) | Telecom/IT | SEK `[?]` (written down in the 2025 debt-to-equity swap) | `[?]` | Working-capital facility cap raised from SEK 50m to SEK 100m (62% voting undertakings; adopted 20 Oct). The bond was restructured in 2025 (debt-to-equity swap, issuer option to defer interest) | 20 Oct 2026 | n (routine; the first default was the 2025 restructuring `[A]`) | — | — | — | Stamdata (notice 1 Oct; results and restated terms 20 Oct, read 24 Oct) | — |
| Empresa Naviera Elcano (ES) | `[?]` | Shipping | `[?]` | `[?]` | EGM on 18 Nov 2026 to report on "the completion of the Corporate Refinancing Transaction" and appoint a director | 19 Oct 2026 | n (credit-positive) | — | — | — | Stamdata (19 Oct) | Fondsfinans High Yield, Kreditt |
| Ventura Offshore Midco; Airswift Global; First Mover Group | `[?]`; `[?]`; NO0013264556 (NOK 65m 2024/27) | Oil Service; Oil Service; Other | — | — | Call options exercised (First Mover at 102.50%, repayment 4 Nov) | 19–21 Oct 2026 | n (repayments) | — | — | — | Stamdata | `[?]` |
| Achilles Capital AB (publ) (SE) | SE0015797683 (up to EUR 200m senior secured fixed 2021/2026; EUR 170m outstanding) | Finance (NPL and secured collections) | EUR 170m | ~1,770 | Maturity 19 Apr 2026 extended to 30 Apr 2027 with an ad hoc group (Arrow), EUR 100m amortisation due 31 Dec 2026, terms amended 23 Jul 2026. **19 Oct interest not paid; events of default notified 4 Nov** (non-payment; missing surplus cash-flow report). The issuer cites adviser costs > EUR 6m, slower collections and court delays, but expects to repay principal by 30 Apr 2027 | Apr–Jun 2026 (extension); 19 Oct / 4 Nov 2026 (non-payment, EoD) | **y `[A]`** (the extension without full repayment; the non-payment is a further default of the same bond) | `[?]` | `[?]` | `[?]` | Stamdata (S33: issuer update 3 Nov; NT&A notice of events of default 4 Nov) | — |
| Calligo (UK) Limited | NO0011179806 (max EUR 50m senior secured fixed compound interest) | Telecom/IT (IT services) | EUR ≤ 50m | ≤ ~520 | Written procedure (17 Jul 2026): debt-for-equity swap. Conditions met; **bonds, including capitalised and accrued interest, written down to zero on 5 Nov 2026**; bonds delisted | 17 Jul 2026 (procedure); 5 Nov 2026 (effective) | **y** (debt-for-equity conversion) | `[?]` | `[?]` | equity only, value `[?]` | Stamdata (S33: NT&A notice of effective date and write-down, 4 Nov) | — |
| Proximar Seafood AS (NO) | NO0012733387 (7.00% subordinated unsecured convertible NOK 300m 2022/2025) | Seafood | NOK 300m | ~300 | **Interest due 27 Oct 2026 not paid** (non-payment under Clause 17.1(a)); the issuer is in talks with its main shareholders on funding. The bond is still outstanding past its 2025 maturity, so an earlier amendment may be its first default `[?]` | 27 Oct 2026 | **y** (first default possibly earlier `[?]`) | `[?]` | `[?]` | `[?]` | Stamdata (S33: NT notice 27 Oct with the issuer's stock exchange notice) | — |
| Engebø Rutile and Garnet AS (NO; Nordic Mining) | NO0012734112 (12.5% senior secured USD 2022/2027; USD 100m + taps 33, 22.5, 30 and 0.7) | Other (mining) | USD ~186m `[A]` | ~1,730 | Sep 2026 written resolution: minimum-liquidity covenant suspended and a USD 30m tap for USD 7.5m of cash. **5 Nov: written resolution adopted the same day as summoned** (> 2/3 support indicated): forbearance on the existing events of default (not waived) to an extended waiver date, further covenant suspension, and up to USD 6m of **super senior emergency bridge bonds** ranking ahead | 10 Sep 2026; 5 Nov 2026 | **pending `[A]`** (standstill and priming; no payment default seen; the Sep discounted tap may already qualify) | `[?]` | `[?]` | `[?]` | Stamdata (S33: summons and notice from written resolution, 5 Nov) | — |
| Galileo Global Technologies PLC | NO0013481242 (Tranche C), NO0013697714 (interest claims); USD 75.5m 13.75% senior secured 2025/2028 | Other | USD 75.5m | ~700 | Comprehensive restructuring summoned 9 Dec 2025; ownership moved to a bondholder SPV on 15 Dec 2025. **4 Nov 2026: shares in the SPV to be distributed to bondholders and Halliburton** | Dec 2025; 4 Nov 2026 (distribution) | (2025 default; not a 2026 FTD) `[A]` | — | — | equity, value `[?]` | Stamdata (S33, 4 Nov) | — |
| Konzmann Group Holding GmbH (DE) | NO0013683466 (EUR 85m senior secured) | Industry (technical installations) | EUR 85m | ~890 | Written resolution (30 Oct): Nimlas AB to replace Konzmann as issuer, pari passu with Nimlas's EUR 375m bonds; pro forma net leverage 3.9x (4.3x Konzmann); 0.125% consent fee + 0.125% early-bird fee; majority wall-crossed and supportive | 30 Oct 2026 | n (compensated, credit-positive) | — | — | — | Stamdata (S33: summons and press release 30 Oct) | — |
| Thon Holding AS; Banco Plata S.A.; Grøntvedt AS | NO0010809148; NO0013596668; multiple | Real Estate; Finance; Seafood | — | — | Thon: issuer substitution in a group reorganisation, with a fee. Banco Plata: listing deadline for subsequent bonds aligned (obvious-error amendment). Grøntvedt: additional guarantees | 26–28 Oct 2026 | n (routine) | — | — | — | Stamdata (S33) | — |
| Pearl Petroleum; Shamaran Petroleum; Andfjord Salmon; Avarda Bank; Fortaco | NO0013387860; NO0011057622; NO0013587246; SE0017085244; NO0012547274 | E&P; E&P; Seafood; Finance; Industry | — | — | Calls and refinancing: Pearl a new senior secured bond and a call (26–29 Oct); Shamaran's conditional call condition met (4 Nov); Andfjord and Avarda calls; Fortaco a mandatory partial redemption (2 Nov) | 26 Oct–4 Nov 2026 | n (repayments) | — | — | — | Stamdata (S33) | `[?]` |
Other September written procedures whose purpose was not read (could be routine): Ocean Yield
(repeated meeting), Galileo Global Technologies, DEAG, Jasmine Energy, Engebø Rutile and Garnet,
GQM Marine Services, Acroud (withdrawn). Waivers: Conapto, Magle Chemoswed. Read on 17 Oct and
logged above: Keystone Academic Solutions, Brightstar Resources, Point Properties Portfolio 1.
Read on 24 Oct and logged above: Rebellion Capital, DistIT, Taptravel (23 Oct), Kistos (result).
Read on 5 Nov (S33, pages 1–2, 19 Oct–5 Nov) and logged above: Achilles, Calligo, Caybon (deferral),
Proximar, Engebø, Galileo, Konzmann, Thon, Banco Plata, Grøntvedt, Booster (standstill), Dooba
(presentation), calls and refinancings. Not read (company information only): First Camp Q3, Latina
Offshore budget, Kosmos Energy GTA Q3, Futura annual report, Vital Energi accounts, Jasmine Energy
drilling update, AKA T2, Brightstar quarterly, KLP Boligkreditt; Oceanity (CMM OSV) won a four-year
Petrobras charter (credit-positive).

### Watchlist — names not held (status scale, skill Definitions)

The held names (HX, Booster, Jøtul, Hofseth, Sigma and Flora, Magnolia, Varel, Shearwater, Tullow,
Viaplay, W&T, Foxway, Trustly, Intrum, Convene, Norse, EHAB) are in the master watchlist in
`docs/hy-issuers.md`, with entry dates and an outcome record (moved there on 18 Oct).

| Issuer | ISIN | Status | Outstanding NOKm | Price / spread | Maturity | Trigger |
|---|---|---|---|---|---|---|
| Dooba Finance AB | NO0013739201, NO0013219493 | Vote or standstill (events of default) | ~1,030 | `[?]` | 2029 / 2031 | Cross-default and missing accounts; information calls 15 and 21 Oct; the 15 Oct presentation was circulated on 27 Oct; information public by 30 Nov |
| **Engebø Rutile and Garnet AS** (new 5 Nov) | NO0012734112 | Vote or standstill (forbearance on existing events of default; priming super senior bridge) | ~1,730 | `[?]` | 2027 | Bridge funding and forbearance to an extended waiver date; FTD pending `[A]` |
| **Achilles Capital AB** (new 5 Nov) | SE0015797683 | In restructuring (extension Apr–Jun 2026; 19 Oct interest unpaid; events of default 4 Nov) + maturity flag (30 Apr 2027; EUR 100m due 31 Dec 2026) | ~1,770 | `[?]` | 30 Apr 2027 | Collections behind plan; ad hoc group led by Arrow; recovery `[?]` |
| **Proximar Seafood AS** (new 5 Nov) | NO0012733387 | In restructuring (interest due 27 Oct unpaid) | ~300 | `[?]` | past 2025 maturity (extended) | Funding talks with main shareholders |
| **Calligo (UK) Limited** (new 5 Nov) | NO0011179806 | In restructuring → bonds written down to zero for equity (5 Nov) | ≤ ~520 | — | — | Leaves the list when the equity value (recovery) is logged |
| Point Properties Portfolio 1 AB | SE0015556535 | In restructuring (FTD y `[A]`) + maturity flag | ~770 | `[?]` | 30 Nov 2026 | Portfolio sale needed to redeem; bondholder committee |
| Caybon Holding AB | SE0023950902, SE0021923562 | **In restructuring** (from Vote or standstill, 5 Nov: interest deferred to redemption on both bonds; FTD y `[A]`) | ~295 | `[?]` (85.5 at end-2025) | 2028 / 2029 | Deferred coupons 27 Nov and 3 Dec; recovery `[?]` |
| Solteq Oyj | FI4000442264 | Vote or standstill (FTD `[?]`) | `[?]` | `[?]` | `[?]` | Written procedure, revised proposal, 17 Sep |
| Rebellion Capital AB | SE0023113790 | **Watch** (from Vote or standstill, 24 Oct: the vote was a compensated covenant reset) | ≤ ~960 | `[?]` | 2028 | Leverage covenant 4.5x → 5.5x (leverage 3.99x at 30 Jun); next: Q3 report |
| DistIT AB | SE0015949359 | **Watch** (from Vote or standstill, 24 Oct: routine working-capital amendment; post-restructuring) | `[?]` | `[?]` | 19 May 2028 | Restructured 2025 (debt-to-equity swap; interest deferral option) |
| Futura Resources | `[?]` | Watch | `[?]` | `[?]` | `[?]` | Trustee's technical review of the mines |
| Taptravel Nordic AB | NO0013699975, NO0013326041 | In restructuring (missed interest 3 Jul and 3 Oct) | `[?]` | `[?]` | 2028 → Dec 2029 (super senior; senior → Apr 2030) once effective | Recapitalisation **approved 9 Nov**; effective when the ≥ SEK 50m share issue (Ridge Capital) closes, longstop 31 Mar 2027 (failure = EoD, bankruptcy likely per the company); super senior 6% cash + 4% PIK, senior 8% PIK; recovery `[?]` |
| Cabonline Group Holding AB | SE0017767346 + 1 | In restructuring (interest deferral) | ~1,170 | `[?]` | `[?]` | Recovery `[?]` |
| Catena Media plc | SE0014262192 | In restructuring (interest deferral) | `[?]` | `[?]` | `[?]` | Recovery `[?]` |
| SIBS AB | SE0023112487 | In restructuring (debt-to-equity conversion, effective 9 Oct) | ~610 | `[?]` | `[?]` | First default in 2025 or 2026 `[?]` |

- Names in restructuring stay on the list until their recovery is logged (the price ~30 days
  after the event, or the ultimate outcome).

### Maturity wall (year × sector, NOKbn)

`[?]` Not available from public sources read (Stamdata statistics need a licence). Carried as an
open checkpoint.

### Sources

| ID | Source | Content | Definition / universe | Observed / published |
|---|---|---|---|---|
| S1 | Nordic Trustee / Ocorian, *Nordic Corporate Bond Market Report 2025* (PDF) | Market size, sector shares, FTD rates, issue spreads, NBP index returns, covenants, definitions | NT/Stamdata HY classification; FTD = first-time defaults ÷ outstanding (LTM chart; annual sector table) | YE-2025 / Feb 2026 |
| S2 | Norges Bank, MPR 3/26 and dataset `data-mpr-3-26.xlsx` | Policy rate and 3M money-market path (quarterly), macro projections, normal rate 3.2% | Quarterly averages | 24 Sep 2026 |
| S3 | Norges Bank API (KPRA, NOWA, GOVT_GENERIC_RATES) | Policy rate history; 3M T-bill, 3Y, 10Y | Daily | to 2 Oct 2026 |
| S4 | Riksbank, MPR September 2026 (PDF) | Sweden GDP, unemployment, policy path | Annual / quarterly | 24 Sep 2026 |
| S5 | Heimdal Høyrente monthly reports, Aug 2025–Sep 2026 | Spread series (Nordic/Norway), DNB Carnegie index returns, issuance, fund metrics | As quoted; provider `[?]` | Monthly, latest 30 Sep 2026 |
| S6 | Heimdal Høyrente March and April 2020 reports | Shock calibration (−15.6% month; yield 5.7% → 12.7%) | Fund NAV | Mar/Apr 2020 |
| S7 | Fondsfinans, *Markedsrapport August 2026* (HY pages) | Hofseth, Foxway, EHAB, Snowball; fund metrics | — | 31 Aug 2026 |
| S8 | Stamdata news (public, read manually in the in-app browser, pages 1–5) | Distress notices 1 Sep–5 Oct 2026; NT notices (Taptravel, Cabonline, Island Offshore, Booster) | Stamdata tags | 5 Oct 2026 |
| S9 | FRED: SOFR, IR3TIB01NOM156N, IR3TIB01SEM156N, BAMLHE00EHYIOAS, BAMLH0A0HYM2 | Hedge carry, global HY context | ICE BofA OAS (context only) | to 2 Oct 2026 |
| S10 | BNP Paribas AM, "Talking heads: Nordic high-yield bonds" | Market > EUR 70bn, spread 460 bp, FRN 55%, default 5.4% since 2007, international issuers 56% of 2026 issuance | Manager commentary `[E]` | 27 Aug 2026 |
| S11 | Bloomberg via Swissinfo, "Souring bond deals threaten to undermine a Nordic credit boom" | LR Health & Beauty, Nordwest Industrie, Flora Food | Press `[E]` | 24 Feb 2026 |
| S12 | Finanstilsynet, *Finansielt utsyn*, June 2026 | Low risk premiums; real-estate development stress | Supervisor `[E]` | Jun 2026 |
| S13 | TradeWinds / search summaries | Norwegian oil and gas bond default rate ~23% (2016); Nordic spec-grade 8.02% end-2016 vs 4.50% end-2015 | Grade C `[E]`, definition unclear | Historical |
| S14 | Upstream baselines `docs/oil-market-bbb.md`, `rig-market-bbb.md`, `supply-market-bbb.md`, `oil-shipping-bbb.md` | Energy row drivers | As stated there | 4–5 Oct 2026 |
| S15 | Yahoo FX | USD/NOK, EUR/NOK, SEK/NOK | Spot | 5 Oct 2026 ~21:15 UTC |
| S16 | NHH master theses (open access) on Norwegian HY default and recovery | Recovery comparable to international; security adds little | Academic `[E]` | Various |
| S17 | Stamdata news, new public site `stamdata.com/news` (pages 1–3, read in the in-app browser 17 Oct) and notice PDFs | Notices 23 Sep–16 Oct 2026: Point Properties, SIBS, Dooba, Kistos, Brightstar, Keystone, Storsala, Solis, Futura, Specac, Holmström, Elcano | Stamdata tags | 16 Oct 2026 |
| S18 | Norges Bank API (KPRA, NOWA, GOVT_GENERIC_RATES, GOVT_ZEROCOUPON, FCI, EXR) | Policy rate, NOWA, T-bill, 3Y, 10Y, zero curve, FCI, FX at 30 Sep | Daily | to 15 Oct 2026 |
| S19 | FRED: BAMLHE00EHYIOAS, BAMLH0A0HYM2, SOFR | Euro / US HY OAS, SOFR | ICE BofA OAS (context only) | to 15 Oct 2026 |
| S20 | NAV, "Hovedtall om arbeidsmarkedet", September 2026 | Fully unemployed 2.0% (59,413) | Registered, unadjusted | 30 Sep 2026 |
| S21 | IMF WEO October 2026, via Placera (Finwire) 13 Oct | Norway 1.5% / 1.3% (2026–27) | Total GDP `[E]` | 13 Oct 2026 |
| S22 | fondsfinans.fundlist.com holdings, High Yield and Kreditt (Morningstar), daily NAVs | Watchlist prices at 30 Sep; NAV change 30 Sep–15 Oct (proxy for October) | Dirty prices; NAV per unit | 30 Sep / 15 Oct 2026 |
| S23 | DNB, "Uncovering the dark side of high-yield vintages" (via search, Feb 2026) | ~12% lifetime hard defaults (2015–22), timing of defaults, faster 2023–24 cohorts | DNB credit research `[E]` | Feb 2026 |
| S24 | Upstream baselines (oil 17 Oct, rig 10 Oct + 13/17 Oct, supply 17 Oct, shipping 17 Oct) | Energy row drivers | As stated there | 10–17 Oct 2026 |
| S25 | Stamdata news, `stamdata.com/news` page 1 (13–23 Oct) and page 3 (1 Oct notices), read in the in-app browser 24 Oct; notice PDFs via `/news/api/pdf/<id>` | Taptravel (2 written procedures, 23 Oct), Rebellion (notice and result), DistIT (notice, result, restated terms), Kistos result, Dooba information call, Elcano EGM, Eiendomskreditt tap, calls (Ventura, Airswift, First Mover) | Stamdata tags | 23 Oct 2026 |
| S26 | Norges Bank API (KPRA, NOWA, GOVT_GENERIC_RATES, GOVT_ZEROCOUPON, FCI) | Policy rate, NOWA, T-bill, 3Y, 10Y, zero curve 6M–5Y, FCI | Daily | to 22 Oct 2026 |
| S27 | FRED `fredgraph.csv`: BAMLHE00EHYIOAS, BAMLH0A0HYM2, SOFR | Euro / US HY OAS 354 / 340 bp; SOFR 3.90 | ICE BofA OAS (context only) | to 22 Oct 2026 |
| S28 | Yahoo chart `0P0001SXZ4.IR` (Fondsfinans High Yield B, daily NAV); fondsfinans.fundlist.com holdings pages (Morningstar `DayEnd` block, HY and Kreditt B) | FF HY B NAV 11,392.82 (30 Sep) → 11,371.79 (22 Oct); Kreditt B trailing month −0.10% | NAV per unit, NOK, after fees | 22 Oct 2026 |
| S29 | SCB, Arbetskraftsundersökningarna (AKU), September 2026 | Swedish unemployment 8.7% SA, 8.1% unadjusted | LFS, 15–74 | 16 Oct 2026 |
| S30 | Upstream baselines (oil 24 Oct, shipping 24 Oct, rig 10 Oct + 22 Oct, supply 17 Oct) | Energy row drivers | As stated there | 17–24 Oct 2026 |
| S31 | Norges Bank press release "Policy rate kept unchanged at 4.5 percent" (`norges-bank.no/en/news-events/news/Press-releases/2026/2026-11-05-rate/`) | Decision, assessment, guidance; MPR 4/26 on 17 Dec | Primary | Meeting 4 Nov; published 5 Nov 2026 10:00 |
| S32 | Riksbank press release "Policy rate raised to 2 per cent" and Monetary Policy Update November 2026 (riksbank.se PDFs) | Decision (2.00% from 11 Nov), guidance, Q3 GDP +0.4%, CPIF, risks, next MPR 16 Dec | Primary | 4 Nov 2026 |
| S33 | Stamdata news, `stamdata.com/news` pages 1–2 (19 Oct–5 Nov), read in the in-app browser 5 Nov; notice PDFs via `/news/api/pdf/<id>` | Achilles (issuer update 3 Nov, events of default 4 Nov), Calligo (write-down 4 Nov), Caybon (two deferral notices 30 Oct), Proximar (non-payment 27 Oct), Engebø (summons and result 5 Nov), Galileo, Konzmann, Thon, Banco Plata, Booster (standstill 2 Nov), Dooba (27 Oct), calls | Stamdata tags | 5 Nov 2026 |
| S34 | Norges Bank API (KPRA, NOWA, GOVT_GENERIC_RATES, GOVT_ZEROCOUPON, FCI, EXR) and press releases "Foreign exchange transactions in October / November 2026" (30 Sep, 30 Oct) | Policy rate, NOWA, T-bill, 3Y, 10Y, zero curve 6M–5Y (4 Nov), FCI (29 Oct), FX and I-44 (5 Nov); FX purchases NOK 176m a day (Sep–Nov) | Daily; monthly | to 4–5 Nov 2026 |
| S35 | SSB: table 07129 (retail volume, 28 Oct), 13760 (LFS, 22 Oct), national accounts page (last 27 Aug; next 26 Nov); NAV press release "Liten økning i arbeidsledigheten i oktober" (30 Oct) | Retail Sep −0.4% m/m; LFS 4.6%; registered unemployment 2.0% SA (Oct) | Official statistics | Sep–Oct 2026 |
| S36 | `docs/hy-issuers.md` (4 Nov: Heimdal October reports dated 30 Oct); FRED `fredgraph.csv` (BAMLHE00EHYIOAS, BAMLH0A0HYM2, SOFR, IR3TIB01SEM156N, IR3TIB01NOM156N); Yahoo `0P0001SXZ4.IR` | Nordic spread 490 bp, DNB Carnegie −0.2% (Oct), Europe/US spreads, issuance; Euro / US HY OAS 345 / 332 (4 Nov); SOFR 3.94; STIBOR 3M 1.94 (Sep); NIBOR-proxy 4.80 (Sep); FF HY B NAV to 3 Nov | As stated; OAS context only | 30 Oct–4 Nov 2026 |
| S37 | Upstream baselines: oil 31 Oct (update 4 Nov), rig 10 Oct (small update 4 Nov), supply 17 Oct (small update 4 Nov), shipping 24 Oct | Energy row drivers; drillship 2027 $420k / 91% | As stated there | 24 Oct–4 Nov 2026 |
| S38 | SSB API v2 table 14706 (CPI and CPI-ATE, 12-month change, 2025M09–2026M10; table updated 10 Nov 07:00 UTC); Norges Bank `data-mpr-3-26.xlsx` sheet Data C (Table 2a, monthly CPI and CPI-ATE projections Sep–Dec 2026) | October CPI 3.6 / CPI-ATE 2.7 vs MPR 3/26 3.8 / 2.7 | Primary | 10 Nov 2026 (read 11 Nov) |
| S39 | Riksbank, "Minutes of the monetary policy meeting 3 November 2026" (riksbank.se PDF, published 10 Nov) | Board views on further hikes (Jansson, Hjelm, Seim, Bunge, Thedéen); unanimous decision | Primary | 10 Nov 2026 |
| S40 | Taptravel releases on MFN: "initiates written procedures … share issue of at least SEK 50 million" (24 Oct) and "receives bondholder approval of the amendments and waivers under its Senior Bonds and Super Senior Bonds" (9 Nov) | Vote outcome, conditions precedent, longstop, new terms | Issuer | 9 Nov 2026 (read 11 Nov) |
| S41 | `docs/oil-market-bbb.md` (11 Nov, Final); Norges Bank API zero curve, policy rate, NOWA, T-bill and EXR to 10 Nov; DNB Capital Markets Day view as briefed by the update chain (DNB Carnegie: policy rate 4.00% after two cuts in H2 2027, mainland GDP ~1.5% to 2030; not found in a primary source in this run `[E]`) | Oil check; market path check (+0.17 / +0.33 / +0.69 pp); I-44 109.57 (10 Nov); DNB cross-check | As stated | 10–11 Nov 2026 |

- **Input assessment:** the user's link (NT 2025 report) is the anchor for size, sectors and FTD.
  It gives Energy only as E&P + Service combined in the Nordic chart and leaves out shipping FTD,
  so the shipping row is `[A]`.
