# Review: the 2029 step-down in CAPT, Hafnia, SED and DOF — 10 Oct 2026

Skill revisions behind the documents reviewed: **iaf-valuation 2026-10-10.1**; **oil-shipping-bbb
2026-10-10.3** (baseline 10 Oct; rates set under 2026-10-05.1, fleet register under 2026-10-10.3);
**oil-market-bbb 2026-10-10.2** (baseline produced under 2026-10-10.1); **rig-market-bbb
2026-10-10.1** (baseline produced under 2026-10-08.2); **supply-market-bbb 2026-10-10.2** (baseline
produced under 2026-10-10.1).

Documents reviewed (all dated 10 Oct 2026): `docs/capt-analysis.md`, `docs/hafnia-analysis.md`
(v3), `docs/SED-analysis.md`, `docs/DOF-analysis.md` (afternoon version), `docs/oil-shipping-bbb.md`,
`docs/oil-market-bbb.md`, `docs/rig-market-bbb.md`, `docs/supply-market-bbb.md`. No new market data
was fetched; every number below comes from those documents unless it is tagged `[A]` (my own
estimate in this review).

**Question (user):** all four analyses show strong income in 2027–2028 and lower income and value in
2029. Is that a conservative estimate made because the future is uncertain, or is it founded in a
weaker market balance or demand?

## Answer in brief

- **No uncertainty haircut is applied to Base.** The framework puts uncertainty in Bear and Bull and
  in the ranges, not in a shaded Base. But Base is not the scenario average either: tanker upside is
  larger than downside, so the 25/50/25 reference is above Base for CAPT (10.6% vs 4.5%) and Hafnia
  (0.7% vs −1.3%).
- **The 2029 step has three different sources, and the mix differs by company:**
  1. **Market balance with evidence behind it:** CAPT (crude tanker delivery wave) and Hafnia's
     2028 step.
  2. **Model convention:** rates that revert to newbuild parity or mid-cycle where the evidence runs
     out (Hafnia's 2029 product rows), exit value set at mid-cycle NAV (all four), the
     asset-life convention (DOF, SED), and the linear interim value glide (all four).
  3. **Company mechanics:** class surveys and contract timing (SED), contract roll-off (DOF).
- **Per company:**
  - **CAPT:** founded. If anything the 2029 Base is generous, not conservative.
  - **Hafnia:** 2028 is founded. 2029 is **not** supported by the shipping baseline's own balance
    check and reads as reversion to parity. *Corrected by the evening re-test: the balance inputs
    were wrong, and 2029 is mostly founded (see Follow-up).*
  - **SED:** not a market fade at all; mainly a special-survey year.
  - **DOF:** hardly a fade (−4% EBITDA). The part that matters (NS CSV) rests on thin evidence.
- **The "value reduction" in 2029 is mostly by construction.** The year-end value path glides
  linearly to mid-cycle NAV at exit, so 2029 is simply the last step of the glide. It is not a
  forecast that asset prices fall in 2029. Interim values do not enter IRR_T; only the exit value
  V_T does.

## The 2028 → 2029 change per company (Base)

| | EBITDA 2028 → 2029 | Maintenance FCF per share | Year-end value per share | Main driver of the 2029 step | Classification |
|---|---|---|---|---|---|
| **CAPT** | $493m → $313m (−37%) | NOK 29.19 → 16.24 (−44%) | 175.6 → 166.0 (−5%) | Fleet TCE 53.5 → 37.4 ($k/day): VLCC 65 → 45, Suezmax 50 → 35, Aframax/LR2 44 → 35. 2029 lands at mid-cycle (fleet mid-cycle ≈ 36) | **Market balance, founded** |
| **Hafnia** | $535m → $387m (−28%) | NOK 7.43 → 4.74 (−36%) | 77.6 → 70.8 (−9%) | TCE 27.2 → 23.0: LR2 44 → 35, LR1 33 → 25, MR 25 → 22 | **2029 mainly convention** (reversion to parity). *Re-test: mostly founded; see Follow-up* |
| **SED** | $102m → $89m (−13%) | NOK 0.94 → 0.61 (−35%) | 5.60 → 5.51 (−2%) | Four class surveys (off-hire and capex $28m vs $15m) and one re-contracting gap; the tender-assist rate *rises* 82 → 85 | **Company mechanics (timing)** |
| **DOF** | $932m → $897m (−4%) | NOK 21.27 → 19.91 (−6%) | 130.5 → 119.7 (−8%) | AHTS term roll-off, NS CSV re-pricing, cost drag; AHTS spot pool up | **Mixed; small** |

## CAPT (crude tankers)

**What drives 2029:** VLCC 65 → 45, Suezmax 50 → 35 and Aframax/LR2 44 → 35 in the shipping
baseline, on a fleet that grows from 16 to 33 ships. Fleet days rise only 3% in 2029, so the fall in
rates goes straight through to EBITDA.

**The evidence is market balance, and it is sourced:**
- VLCC orderbook 304 ships = 33.5% of the fleet (Frontline, 11 Aug), about 40% of the commercially
  traded fleet.
- Delivery schedule 62 / 125 / 100 for 2027–29 (Frontline/Clarksons, BRS and Signal triangulated):
  225 VLCCs arrive in 2028–29 alone.
- Contracting has not stopped: about 40 VLCCs were ordered in Q3 (4.4% of the fleet), and the
  contracting trigger fired. Chinese yards still sell late-2028 slots.
- Demand: the ~1 bn bbl restocking that supports 2027–28 ends once stocks are normal by end-2028
  (Oil BBB balance 2029: 0 to +0.5 mb/d).
- Balance check: VLCC Base −4 / −6 / −3 pp of tightness in 2027–29. 2029 is still loosening.
- **The period market prices the same fade.** The 3-year TC ($106k) is 65% of Base's
  Oct-26 → Sep-29 average (~$164k); the 1-year TC is 61–71% of Base's next-12-month average. The
  same discount on both tenors means the paper market sees the same shape as Base.

**Where Base is generous, not conservative:**
- **2029 lands exactly at newbuild parity** (VLCC 45 vs parity 44) while the balance is still
  loosening. Past delivery waves took VLCC earnings well below parity (roughly $15–25k/day in 2013
  and 2018) `[E, background]`.
- **Scrapping:** Base needs 40 VLCCs scrapped in 2028 and 50 in 2029, against 7 in 2022–26 (Drewry).
  At $45–65k/day, old ships keep trading, and the shadow fleet absorbs them. Supply risk is upward.
- **The 2029 schedule will grow:** Q3–Q4 2026 orders land in 2028–30.
- **Mid-cycle asset values** use today's high newbuild price ($131m) and an 8% discount rate (k is
  12%). Neither is conservative.

**The case against the fade** (this is the Bull logic, not Base):
- About 17% of VLCC capacity is sanctioned, and 30% of the fleet will be ≥ 20 years old at full
  delivery. Compliant supply may stay tighter than the headline orderbook.
- Aramco is reportedly considering the shuttle/STS model as a lasting setup (+6% VLCCs per mb/d).
  **Base assumes most of the war inefficiency unwinds in H2-27 without a deal.** That is the
  single most judgmental element in the crude Base, and it is not evidenced. It deserves a named
  signpost (STS time, shuttle share) rather than an assumption.

**Value:** the 2029 value step is the last part of the glide (85% → 100% of mid-cycle). The real
issue is the level: the exit marks a 5-year VLCC at $121m against $210m in today's market. That is a
deliberate disagreement with the secondhand market. It is defensible, because a newbuild costs $131m
for late-2028 delivery, so a 5-year ship cannot hold 1.6× newbuild once the windfall has passed. But
it is the input the CAPT verdict hangs on: exit values ×1.2 give 11.9%.

**Classification:** the 2029 income drop is founded in market balance and is, if anything,
optimistic. The value gap is a deliberate convention, and it is the key judgment.

## Hafnia (product tankers)

*Superseded in part by the Follow-up section: the re-test traced the inconsistency below to the balance inputs (scrapping, 2029 deliveries), not to the 2029 rates.*

**2028 is founded:**
- The dislocation unwinds: Gulf product exports recover towards ~2 mb/d by mid-2027, and LR2s return
  to clean trade in H2-27 (+~5% clean supply).
- More than 50% of the product orderbook delivers in 2028 or later (BIMCO), and LR1/MR fleet growth
  is +4% in 2028.

**2029 is not supported by the baseline's own balance check:**

| Shipping BBB, Base | 2027 | 2028 | 2029 | Rate 2028 → 2029 |
|---|---|---|---|---|
| Aframax/LR2 balance (pp of tightness) | −1.5 | −1.0 | **+1.5** | LR2 44 → 35 (−20%) |
| LR1/MR balance | −3 | −4 | **+1** | LR1 33 → 25 (−24%); MR 25 → 22 (−12%) |

- Both balances **tighten** in 2029. The cumulative loosening from end-2026 is smaller in 2029 than in
  2028, yet all three rates fall 12–24%.
- The baseline gives one line of justification: "At parity in 2029 as the balance turns." That
  describes the result, not a cause.
- The second run on 10 Oct raised LR2 2029 from 31 to 35 on exactly this logic. LR1/MR were not
  moved, because their schedules are `[?]`.
- **This is the honest form of the conservatism you suspected:** where the 2029 evidence runs out,
  the rows default to newbuild parity.
- **Path shape:** the Year-1 quarters end 2027 at LR2 35 and LR1 30. The 2028 annual values (44 and
  33) sit *above* that exit run-rate, and 2029 drops back. Either 2028 is too high or 2029 is too
  low; the baseline does not explain the bump.

**What could still justify a lower 2029:**
- MR contracting continues with 2028–29 slots open (≥ 39 MRs reported ordered in Q3), so the 2029
  delivery bar (10m dwt) will probably fill.
- The +1 pp also depends on 3% product-tanker scrapping in 2029 `[A]`. That is high for ships
  earning around parity.
- Both points belong in the balance table, not in an unexplained rate step.

**Effect `[A]`:** holding LR1, MR and Handy in 2029 at their 2028 rows adds about $130m (+16%) to
2029 TCE income. Scaled from the analysis's own sensitivity (open-day rates +12% → P_k +NOK 5.5),
that is roughly **+NOK 2 on P_k and +~1 pp on IRR**. Margin of safety goes from −27.5% to about
−25%, so **the verdict is unchanged**. The Hafnia result rests on P/NAV 1.14 and fleet ageing, not on
2029 rates.

**Value:**
- The 2029 step (77.6 → 70.8) is the glide plus ageing of a 9.7-year-old fleet (−NOK 10/share over
  the horizon) and the TORM stake marked to mid-cycle.
- Newbuild capex of $230m in 2029 moves cash into ships valued at about cost, so it is not a loss.
- Mid-cycle marks are only 8–14% below today's LR2/LR1/MR values. **The value decline is mostly
  physical ageing, which is founded.**

## SED (tender rigs)

**No market fade:** Rig BBB's tender-assist Base *rises* in 2028–29: 78 / 82 / 85 ($k/day).

**What the 2029 dip is (approximate split `[A]`, from the rig-by-rig schedule):**

| Item | Effect 2028 → 2029 | Basis |
|---|---|---|
| Four class surveys (EDrill-2, T-15, T-16, Vencedor; 15 days off-hire each) | Revenue −~$5.6m; maintenance capex $15m → $28m | Last SPS 2024 → next 2029 on the 5-year cycle. **SPS years read from a garbled table `[F/?]`** |
| Vencedor option ends Dec 2028, idle Jan 2029, re-let at $125k | Revenue −~$3.8m | `[A]` Base idle convention |
| EDrill-1 / T-15 18-month terms roll early 2029, one idle month each, re-let at $85k | ≈ 0 (rate step-up offsets the gap) | Term length `[A]` |
| T-16 $80k → $85k from Jul 2029 | +~$0.9m | Base path |
| Opex +3% a year vs flat contract rates | EBITDA −~$2.5m | `[A]` |

- About three quarters of the drop in maintenance FCF ($72m → $47m) comes from the survey year.
  **This is timing, not value.** The cost would fall in 2029 whatever the market does, and moving it
  a year changes IRR only marginally.
- **SED's real fade is 2026 → 2027:** contracts at $94–160k roll into $78–85k after PTTEP gave two
  follow-on tenders to Foresight jackups (reportedly $60–70k). That step is founded in market
  evidence.
- **Value:** 5.60 → 5.51 is small (ageing and contract roll-off). The conservative element sits in
  conventions, not in 2029: a **30-year rig life** (35 years → IRR 14.2%, a pass) and
  company-anchored semi-tender rates `[A]`. Flat nominal opex in the rig values is generous, not
  conservative.

## DOF (offshore vessels and subsea)

**Hardly a fade:** EBITDA −4%. The Base rows for Brazil are flat-to-up in 2029 (AHTS 70 → 72,
RSV 107 → 110, PLSV 295 → 300).

**EBITDA bridge 2028 → 2029 ($m, from the analysis's block table):**

| Block | Change | Evidence |
|---|---|---|
| AHTS terms (two 2027 contracts end; Hera continues) | −14 | Contract fact |
| NS CSV re-pricing (row £52k / 83% → £50k / 82%; open share 45% → 60%) | −20 | **Thin:** one secondary orderbook figure (~30 CSV newbuilds, OE Digital, early 2026) and no vessel-only fixture with a rate (n = 0). Supply BBB rates the row low confidence |
| Cost inflation not passed through | −12 | `[A]`, about 1% of the cost base: plausible, not evidenced |
| Subsea services margin 145 → 140 | −5 | `[A]` |
| AHTS spot pool (more vessels in spot at £60k, still 1.6× mid-cycle) | +9 | Supply BBB row |
| Brazil AHTS, PLSV, SALT | +7 | Rows and contracts |
| **Total** | **−35** | |

- **The weak-evidence item matters for the verdict.** The analysis's own sensitivity gives
  CSV rates flat at the 2026 level (£55k, 90%) → IRR 11.8%, P_k NOK 130.0, margin of safety −0.5%.
  That moves DOF from "fails narrowly" to **marginal**.

**Value (130.5 → 119.7):** no 2029-specific event; it is the glide plus:
- **Ageing at the 25-year life convention:** −$653m over the horizon, the largest line in the bridge.
  A 30-year life gives 13.6% (a pass). Supply BBB applies 25 years to all rows without evidence per
  segment.
- **PLSV marked at mid-cycle $250k** against a Base path of $295–300k in 2028–29 and today's $285k
  (fleet factor 0.69). The exit assumes a step down that the horizon path does not show. PLSVs at the
  broker level give 12.4%.
- **AHTS and CSV exit at mid-cycle is supported by the asset market:** asset-implied rates are
  ~£32–33k, below the mid-cycle rows. Not conservative.
- **Check item `[A]`:** Base assumes new 4-year PLSV contracts for Buzios, Olinda and Recife from
  1Q28, running to 2032. The exit firm-contract premium lists Brazil AHTS, Hera, RSVs and
  Lifter/Logger/Mover, but not these PLSVs. If they were left out, V_T is understated by roughly
  $30m (≈ NOK 1/share). Verify in the DOF model.

## What in the method creates a 2029 step

| Mechanism | Where | Conservative? |
|---|---|---|
| Rates revert to newbuild parity or mid-cycle by year 3 when evidence runs out | Hafnia LR1/MR/LR2; CAPT lands at parity | Conservative for products (contradicts the baseline's balance); generous for crude (a wave usually overshoots below parity) |
| V_T = NAV at mid-cycle marks in every scenario | All four | Depends on mid-cycle vs market: far below today for VLCC; modest for products, AHTS and CSV; a pure convention for PLSV and tender rigs |
| Exit at mid-cycle while the Base 2029 rate is above it (no catalyst named for the post-2029 decline) | DOF PLSV (300 vs 250), SED tender (85 vs 80), Hafnia LR2 (35 vs 30) | Conservative by convention where the asset market does not support it (PLSV, tender) |
| Linear interim value glide | All four | Display only: interim values do not enter IRR_T |
| Asset-life conventions (OSV 25 years, tender 30, tanker values on 20–25 years) | DOF, SED, Hafnia | Conservative and unevidenced for high-end OSVs and tender barges |
| 8% discount in asset values (k = 12%); today's newbuild prices as mid-cycle; flat nominal opex in rig values | Tankers, rigs | Generous |
| Base, not the scenario mean, is the decision case | Tankers especially | Deliberate: with right-skewed outcomes, Base is below the 25/50/25 reference |

## Recommendations (nothing has been changed; your call)

1. **Oil Shipping BBB:**
   - Re-test LR1/MR/LR2 2029 against its own balance check. Either hold 2029 near 2028, or put the
     evidence that turns 2029 loose into the balance table (2029 MR deliveries from new orders, a
     realistic scrapping rate).
   - Explain or fix the 2028 bump above the Q4-27 exit rate (LR2, LR1).
   - Add Cal-28/Cal-29 FFA to the market check (now `[?]`). It is the missing market test of the
     2028–29 paths.
   - For VLCC, test the downside: scrapping of 40/50 a year, and 2029 below parity.
   - Turn "war inefficiency unwinds in H2-27 without a deal" into a signposted assumption.
   - Hafnia's Q3 deck (18 Nov) can fill the product schedules.
2. **Supply BBB:**
   - Date and verify the ~30 CSV newbuild figure, and find vessel-only CSV fixtures.
   - State the economic life per row with evidence (the DOF analysis has already asked for this).
   - *Done (10 Oct, Supply BBB second run, skill 2026-10-10.3):*
     - *The ~30 CSV figure is confirmed: Fearnley Offshore Supply, Dec 2025. It is stale and
       global.*
     - *No 2026 vessel-only CSV fixture with a disclosed rate exists; the row stays low confidence.*
     - *Life stays at 25 years for every row. Secondhand prices for PSVs, AHTS and CSVs sit at or
       below the 25-year model value, so DOF's 30-year case remains a sensitivity, not Base.*
3. **IAF skill:** when the Base final-year rate is materially above the mid-cycle used at exit,
   require either a named reason for the post-horizon decline or a short reversion tail in V_T.
   This is a method change. *Done (10 Oct): iaf-valuation rev 2026-10-10.2, Step 3 "Exit
   consistency". It is symmetric: a Year-3 rate more than 10% above or below mid-cycle needs a named
   reason from the sector BBB or a 2-year reversion tail in V_T.*
4. **DOF analysis:** verify the PLSV post-2029 contract premium; keep the cost-drag line tagged as
   an assumption.
5. **SED analysis:** confirm the 2029 survey schedule at the Q3 report (18 Nov).

## Follow-up: shipping baseline re-test (10 Oct, evening)

Recommendation 1 was run as the third run of `docs/oil-shipping-bbb.md` (skill 2026-10-10.3). **It
corrects the Hafnia finding above.**

- **The balance check, not the 2029 rates, was mostly wrong.**
  - Its 2029 tightening rested on scrapping far above the observed run-rate: 3% of LR1/MR and 40
    Aframax/LR2 a year, against ~0.5–0.6% a year for all tankers in 2026 (Allied, Galbraiths). Most
    old tonnage is sanctioned and hard to recycle.
  - It also used a 2029 delivery bar that predates the Q3 orders.
  - Corrected, 2029 is about flat for products.
- **The period market argues against raising late-window rates** (new check: the forward TC implied
  by the 1-year and 3-year TC). It sits below Base for MR, Aframax/LR2 and, by a wide margin, VLCC.
  LR1 is the exception.
- **Changes:**
  - LR1 2029 25 → 28 (lightest product orderbook, 13.6%).
  - LR1 2028 33 → 30 and Aframax/LR2 2028 44 → 38 (the 2028 values sat above the Q4-27 run-rate).
  - A seasonal Q4-27.
  - MR and LR2 2029 unchanged.
- **Effect on Hafnia:** roughly neutral (≈ −$10–15m EBITDA over 2028–29) instead of the +NOK 2 on P_k
  estimated above. **The Hafnia 2029 step-down is mostly founded, not convention.** Against 2025, the
  product fleet grows ~10 pp more than demand by 2029, and Base 2029 sits at 2025 period-rate levels.
- **Effect on CAPT:** ~−$16m of 2028 EBITDA (Aframax/LR2 pool). Small.
- **New flag for CAPT:** crude Base scrapping (VLCC 40 / 50 in 2028–29) fails the same test, and the
  VLCC paper market sits far below Base. A crude re-test is more likely to cut than to raise 2028–29.

**Crude re-test (fourth run of the shipping baseline, same evening).** This changes the CAPT finding
above: the crude 2029 step was not too deep but too shallow.
- **Base scrapping was inconsistent with Base rates.** Base scrapped 40–50 VLCCs a year while rates
  stayed above parity. That only happened in 2018, at earnings near opex, and only 7 VLCCs went in
  2022–26.
- **Supply growth was measured on the nominal fleet.** Measured on the compliant fleet (160 VLCCs
  are sanctioned), the 2028 supply growth is +14% rather than +9%.
- **Base changes:** VLCC 2028 / 2029 65 / 45 → **50 / 36**; Suezmax 50 / 35 → **44 / 30**.
- **Bear changes:** VLCC → **26 / 24**; Suezmax → **27 / 25**.
- **Unchanged:** mid-cycle and V_T.
- **CAPT effect, rough `[A]`:** about −$170m of 2028–29 cash. Base IRR is likely ~2% rather than
  4.5%, P_k ~NOK 154 rather than 164. Bear LTV pressure rises.
- **Updated classification:** the CAPT 2029 decline is founded in market balance, and the old Base
  was optimistic. The exit at mid-cycle now assumes a 2030–31 recovery from a 2029 trough (36 vs
  44).

## Sources

All within this folder, dated 10 Oct 2026: `docs/capt-analysis.md` (summary, sections 2, 5–10),
`docs/hafnia-analysis.md` (summary, market input, period tables, results, sensitivity),
`docs/SED-analysis.md` (market input, rig-by-rig assumptions, period tables, V_T bridge, sensitivity),
`docs/DOF-analysis.md` (EBITDA build by block, V_T bridge, exit assets, sensitivity),
`docs/oil-shipping-bbb.md` (interface, Year-1 quarters, market check, fleet register, fleet supply,
balance check), `docs/oil-market-bbb.md` (Brent path, balance check), `docs/rig-market-bbb.md`
(tender-assist row), `docs/supply-market-bbb.md` (interface, asset anchors, supply, capital cycle,
balance check). Historical VLCC earnings in past delivery waves are background knowledge `[E]`, not
re-sourced in this review.
