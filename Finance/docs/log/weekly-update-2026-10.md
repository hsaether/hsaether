# Weekly update — archive 2026-10

Entries moved from `docs/weekly-update.md` (keeps the last 14 days). Newest first.

## Week 44 — Saturday 31 Oct 2026 (scheduled run)

Skill revisions: `update-chain` 2026-10-29.1; `defense-market-bbb` 2026-10-10.1; `ai-market-bbb`
2026-10-29.1; `iaf-valuation` 2026-10-29.1. *In progress — this entry is written as the run goes.*

### Check (31 Oct)

- **List 1, in order:** `defense` (UK Budget 28 Oct and Kongsberg Q3 passed; oil changed 17 Oct) →
  `ai` (Amazon Q3 passed) → `mu` (hy-funds) → `nvda`, `tsm` (ai 29 Oct, equity 18 Oct) →
  `global-index`, `dnbtek`, `kospi` (hy-funds 31 Oct; kospi also dnbtek) → `portfolio` (never run
  unattended).
- Already done earlier today, outside this run: `hy-issuers`, `hy-funds` (HY reference E / R unchanged
  at 0.196) and `dnbtek` (Base 7.2% → 8.6%, fails). So the hy-funds cause for `mu`, `global-index` and
  `kospi` is a change-gate case: the value they read did not move.
- **Re-check after upstream:** amzn, googl, msft, skh, smsn (after `ai`); kog, rhm (after `defense`).
- **Loop checks:** `hy` (hy-issuers), `equity` (ai, msft, googl, global-index), `skh` (smsn).
- **Method changed:** iaf-valuation 2026-10-29.1 for most companies; oil 2026-10-24.4; defense
  2026-10-10.1. No re-run on method alone.

### Run list (at most 6)

1. `defense` — xhigh (passed events, oil input, full re-baseline due)
2. `ai` — high (Amazon small update)
3. `nvda` — high (ai and equity inputs; re-mark)
4. `tsm` — high (ai and equity inputs; re-mark)
5. `kospi` — high (dnbtek row; hy-funds change gate)
6. spare — kept for a cascade from `defense` or `ai`, else `mu`

**Run list changed after the news sweep:** `oil` takes the spare slot and runs right after `defense`
(market baselines one at a time). An oil recalibration trigger fired: Hormuz crude volume changed
by more than 20% (see below). If `oil` moves a value, its downstream baselines (`shipping`, `rig`)
outrank `nvda`, `tsm` and `kospi` for the remaining slots.

### Progress

- **`defense`, done, kept unchanged** (recorded, stale after 4 Jan 2027). No path moved. The Bear
  fiscal-stress signpost fired: OAT–Bund widened more than 50 bp in a month, to 174.6 bp on 22 Oct
  (159 bp on 30 Oct). The ceasefire half of the Bear is absent, so Bear and the weights are kept.
  - UK Budget: the Defence Investment Plan is funded; 3% by 2030 is unfunded until the 2027
    Spending Review.
  - France PLF: EUR 63.4bn, in line with the LPM.
  - Kongsberg Q3: orders ahead of the air-defence row.
  - Italy cut its add-on from EUR 22bn to 14bn: flagged, Base held.

  `kog` and `rhm` are not re-run.
- **`oil`, running** (xhigh).

### News that mattered (sweep 24–31 Oct; companies from the daily entries 26–30 Oct)

- **Gulf, to `oil`:**
  - Kpler: Hormuz crude was **~7.3 mb/d in the week to 28 Oct**, more than 40% below pre-war and
    about half the ~14 mb/d the 24 Oct baseline cited. October averaged ~11.1 mb/d. Transits fell to
    single digits per day, and ship attacks doubled in October. `[E]`
  - The Houthis claim missile strikes on the Ras Tanura refinery (550 kb/d) and an Aramco site at
    Abqaiq (27–30 Oct). FIRMS heat signatures show a fire at Ras Tanura, but Saudi Arabia confirms
    only interceptions, and there is no Aramco damage statement. `[E]`
  - Brent front ~$116 on 30 Oct, about level with the 23 Oct Z26 settlement (116.72); a fourth
    monthly gain. `[E]`
  - Two of the baseline's Bull signposts are now close: "Hormuz crude < 8 mb/d for two weeks"
    (one week so far) and "ME crude incl. bypass < 13 mb/d".
  - OPEC+ meets on 1 Nov; Saudi output is reported ~4.5 mb/d below quota. `[E]`
- **Rates, watch events resolved:**
  - FOMC (28 Oct) held at 3.75–4.00% with a 10–2 vote; a December hike is still priced. As
    expected, so marked `done`.
  - ECB (29 Oct) held at 2.50%, with Sep HICP at 3.8% and a December hike still priced. Lagarde
    will step down in February 2027. The rate was as expected (`done`); the leadership change is a
    note for `equity`.
  - US Q3 GDP came in at +3.4% annualised (BEA advance) and Q3 PCE prices at +2.1%. No surprise
    (`done`).
- **Watch events still open, outcome not found:** Norway retail sales (Sep), Norway unemployment and
  Norges Bank's November FX purchases, the Sweden GDP indicator, euro-area/France Q3 GDP, and France
  CPI. These stay `watch` and are read at the next `hy` and `equity` runs (Norges Bank 5 Nov).
  The Heimdal 26 Oct NAV watch was superseded by the 31 Oct `hy-issuers` update and marked `done`.
- **Companies:** the daily entries covered 26–30 Oct (Borr, Intrum, DOF, DNB, SK hynix, Hofseth,
  SED, Anthropic S-1, Kongsberg, BW Energy, Amazon, Scatec). The 30 Oct `amzn` and `scatec` updates
  that had stalled were completed later on 30 Oct. No tracked-company news found for Friday after
  08:00 or Saturday.

## Daily news — Friday 30 Oct 2026

- **Updated:** none. Both updates stalled (see Needs you).
- **Amazon** (`amzn`, `ai`, `dnbtek`): Q3: AWS ~$46bn, +39%; EPS $1.89 vs ~$1.96; Q3 FCF ≈ −$33bn; capex guide ~$220bn kept; shares ~−6% after hours. `[E]`
- **Scatec** (`scatec`): Q3 proportionate EBITDA NOK 1,208m incl. NOK 140m Obelisk one-offs; 2026 power EBITDA guide cut NOK 300m to 3.3–3.6bn (NOK 80m Philippines). `[F]`
- Minor: Rheinmetall/KNDS JV Artec, 69 more Schakal vehicles (DE/NL).

**Needs you:** the `amzn` and `scatec` updates stalled with nothing written. They are first in line Saturday, then `dnbtek` (reads `amzn`).

**Register:** no changes; the Amazon and Scatec Q3 events stay open.

## Daily news — Thursday 29 Oct 2026

- **Updated:** `googl` Base 4.6% → 4.6%, fails (call read; model kept). After hours −10% to $292.50: Base 8.1% there, still fails `[E]`.
- **Kongsberg** (`kog`): Q3 reported this morning, "record-high order backlog". Figures not yet read into the analysis. `[F]`
- **BW Energy** (`borr`): Q3 report: MaBoMo Phase 2 delayed, no replacement rig named, 2026 capex guide suspended. Borr model unchanged (Prospector 5 already removed). `[F]`
- Minor: Amazon reports after the US close today (next run).

In progress elsewhere: `smsn` (Samsung Q3 today), `kospi`, `dnbtek`.

**Needs you:** the `kog` update stopped at the session limit, nothing written; it is first in line next run.

**Register:** `googl` recorded (kept); Alphabet call re-check and BW Energy Q3 closed; Kongsberg Q3 stays open. No events added.

## Daily news — Wednesday 28 Oct 2026

- **SK hynix** (`skh`, `ai`, `smsn`, `kospi`, `dnbtek`): Q3 operating profit KRW 83.3tn (79.7% margin) vs ~77tn consensus; revenue 104.6tn. Q3 dividend 14tn plus a 20tn buyback; 100tn returned for 2026. Verdict (clears) not at risk. `[F]`
- **Hofseth** (`hy-issuers`, `hy-funds`): new to the documents. The bond is at ~72 (12 Oct). The equity-ratio covenant tightens to 27.5% on 7 Nov (26.5% at end-June) and is first tested 31 Dec. The NOK 600m raise is still open. `[E]`
- **Borr** (`borr`, `hy-issuers`): NYSE −8.5 to −10% on 26 Oct; insurance still undisclosed; Q3 reported for ~18 Nov. `[E]`
- Minor: MSFT, GOOGL and AMZN previews only.

Borr bond price and Heimdal NAV still not found.

**Register:** events added: Hofseth covenant (7 Nov, 31 Dec) and Borr Q3 (~18 Nov, approx).

## Daily news — Tuesday 27 Oct 2026

- **SED** (`sed`, `rig`): CPOC LOA for T-16, 30 months firm from early Q3 2027 (+15 months options), ~USD 87m incl. mobilisation (≈$95k/d vs Base $80k); idle Q1–Q3 2027. `[F]`
- **Anthropic** (`ai`, `amzn`, `googl`): public S-1 filed 26 Oct; H1 revenue $16.3bn, close to the draft figures already in `ai`; IPO in November. `[F]`/`[E]`
- **Borr** (`borr`, `hy-issuers`): incident update, five still missing, investigation opened, nothing on insurance; shares −3.9% on 26 Oct; a major-holding notice (holder not read). `[F]`
- Minor: BlueNord Q3 invitation, DNB and Storebrand buyback status.

Borr bond price and Heimdal's 26 Oct NAV still not found.

**Register:** events added for the SED T-16 award and the Anthropic IPO pricing (~20 Nov).

## Daily news — Monday 26 Oct 2026

- **Borr** (`borr`, `hy-issuers`): Borr confirms the Prospector 5 loss. Reuters reports one of the
  five missing found dead; Gabon has opened a technical investigation. Nothing on insurance yet. `[F]`/`[E]`
- **Intrum** (`hy-issuers`, `hy-funds`): Q3 miss and a SEK 1.5bn goodwill write-down; the shares fell
  up to 39% on 23 Oct. No bond price yet. `[E]`
- **DOF** (`dof`): sells Skandi Implementer (delivery Q2 2027); price not given, "material" net-debt cut. `[F]`
- **DNB** (`dnb`): Capital Markets Day 10 Nov; Q4 report 4 Feb 2027. `[F]`
- Minor: Kistos bond tap (credit-positive), Viaplay Q3 neutral, SK hynix Q3 confirmed for 28 Oct.

**Needs you:** Borr's first bond and share prices today (the 18:00 check covers it). Intrum needs a
bond price before the Heimdal verdicts are re-read.

**Register:** events added for the DOF sale, Intrum Q3, DNB CMD and DNB Q4.

## Input — DNB Carnegie Week Ahead (23 Oct 2026), received Sunday 25 Oct

User input, broker macro research (marketing material) `[E]`. It has no company events. It is
read at the next run of each document named below and changes no document by itself. Skill
revision: `update-chain` 2026-10-25.3.

### What it says, and where it goes

| Item `[E]` | Document | What to look at, at its next run |
|---|---|---|
| Norges Bank's governor blames 4–5% wage growth for the slow progress to the 2% target: a hawkish reminder | `hy` | NIBOR path and the 5 Nov decision; the Bull and Bear rate paths |
| NOK is the G10 outperformer in October: EURNOK −1.5% and USDNOK −1.1% in the week, on oil and gas prices | `equity` (NOK path); every NOK figure in the company analyses | Spot against the Base "NOK flat" path; NOK-path IRRs |
| French 10y yield above 5% (a 14-year high), OAT–Bund spread above 170 bp, protests and curfews. DNB Carnegie expects a full debt crisis to be avoided | `defense` (France PLF 2027, already an event), `equity` (European risk) | France's equipment path and the Bear catalyst |
| ECB at 2.50% after hikes in June and September; DNB Carnegie expects hikes in December and March | `equity`, `hy` (EUR hedge carry) | Rate assumptions in Bear and Base |
| Fed at 3.75–4.00%; hold expected on 28 Oct, a hike in December; hawkish dissents possible | `equity`, `ai` (financing cost of the AI build) | US rate path in the scenarios |
| Rotation out of tech (NASDAQ −0.5% in the week) after disappointing AI results | `ai` | Already in Update 4 (Meta and the capex debate) |
| Brent front near its Mar/Apr highs; European gas three times its level at the start of the year | `oil` | Already the 24 Oct risk premium; the next run comes after OPEC+ on 1 Nov |

### Events added to the register

- **New status `watch`,** for data releases and decisions where a hold is expected. They are
  listed, but never force an update on their own; a surprise turns them `open`:
  - 28 Oct: FOMC; Norway retail sales;
  - 29 Oct: ECB; US Q3 GDP and Sep PCE; Sweden GDP indicator;
  - 30 Oct: Norway registered unemployment; Norges Bank FX purchases; euro-area and France GDP;
    France CPI.
- **New `open` event:** the UK Budget on 28 Oct, for UK defence spending (`defense`).

## Week 43 — Saturday 24 Oct 2026 (manual run, before the schedule started)

Skill revisions: `update-chain` 2026-10-24.1 for the run (2026-10-24.2 from this evening, which
added the schedule); `iaf-valuation` 2026-10-18.2; `rig-market-bbb` 2026-10-10.1.

### Summary

- Four company analyses updated. **No verdict moved: all four still fail.**
- Rig Market BBB kept unchanged after the Gulf escalation. The cascade stopped there.

### Updated

| Document | Result | What moved | Stale after |
|---|---|---|---|
| Handelsbanken (`shb`) | v3, changed | Q3 capital return: FY26 dividend SEK 9.61 → 12.05; Base IRR 8.1% → 8.9%, margin of safety −9.7% → −7.7% | 23 Nov |
| Storebrand (`stb`) | Kept unchanged | Q3 (21 Oct) on the Base path; a check run moved Base by +0.4 pp, below the minimum | 23 Nov |
| Borr (`borr`) | v3, Bull only | Base still no equity value; Bull 8.3% → 11.2% (price and current method) | 9 Nov |
| Hafnia (`hafnia`) | v7, changed | Price and FX only; Base IRR +1.2% → −0.5%, margin of safety −22.8% → −25.9% | 18 Nov |
| Rig Market BBB (`rig`) | Kept unchanged | Gulf escalation: no offshore suspension or force majeure found; Gulf-jackup Bear catalyst not triggered | 9 Nov |

### News that mattered

- **Gulf escalation since 22 Oct:** went to `rig`.
  - `[F]` Houthi attacks in Saudi Arabia's Eastern Province (Dammam airport; a drone aimed at
    Shaybah); Aramco evacuated its Dhahran headquarters; the US ordered non-emergency staff out.
  - `[E/?]` The IRGC claims seven tankers were hit (unverified).
  - The oil baseline of 24 Oct already carries the escalation as a front-end risk premium.

### Needs you

- DNB has no next report date in the register.

### Left for next run

- **Defense:** oil changed 17 Oct; Defense reads oil only for its Gulf export row.
- **AI-linked companies:** Amazon, Alphabet, Microsoft, NVIDIA and TSMC (AI Update 3 of 22 Oct;
  the equity baseline of 18 Oct). Run after the Q3 reports of Microsoft, Alphabet and Amazon on
  28–29 Oct.
- **Global index funds:** after the company blocks.

### Events in the next 14 days

- 26 Oct: Westwood weekly rig count, the first after the escalation.
- 28 Oct: Microsoft, Alphabet and SK hynix Q3.
- 29 Oct: Amazon and Kongsberg Q3.
- 1 Nov: OPEC+.
- 2 Nov: Transocean and Valaris Q3 with fleet status; Westwood count.
- 3 Nov: US midterms; Equinor AHTS tender.
- 4 Nov: Riksbank; TORM Q3.
- 5 Nov: Norges Bank; Rheinmetall Q3.
