# Update register — change log

Moved out of `docs/update-register.md` on 12 Nov 2026 (lean documents). New entries go at the end.


- **2026-10-24:** register created; first fill from the document headers.
- **2026-10-24 (later):** report dates from the user: CAPT Q3 30 Nov, SED Q3 18 Nov, Storebrand
  Q3 21 Oct (reported; the analysis is from 19 Oct; first entered as 23 Oct, corrected from the
  Storebrand run) and Q4 10 Feb 2027, TSMC Q4 14 Jan 2027,
  Micron Q1 FY27 16 Dec, Rheinmetall Q3 5 Nov.
- **2026-10-24 (update run):** shb (v3, changed), stb (kept unchanged), borr (v3, Bull only),
  hafnia (v7, price and FX re-mark) updated and recorded. Added: Handelsbanken year-end report
  3 Feb 2027, TORM Q3 4 Nov, Borr's input from Equity BBB.
- **2026-10-24 (news run):** rig small update on the Gulf escalation since 22 Oct: kept
  unchanged (no offshore suspension or force majeure found; Gulf-jackup Bear catalyst not
  triggered). Added the Westwood weekly counts of 26 Oct and 2 Nov.
- **2026-10-25:** new document `skh` (`docs/skhynix-analysis.md`, v1) with its inputs (ai, equity,
  hy, nvda, mu). Back-references added: `ai` reads it as a loop company check, and `dnbtek` reads it
  as a company block; both entered at the date they last used the layer path for SK hynix (24 and
  22 Oct), so the next check flags them. Events: SK hynix Q3 now also affects skh; added Samsung Q3
  (29 Oct) and the end of SK hynix's buyback (19 Nov); NVIDIA Q3 and Micron FQ1 also affect skh.
- **2026-10-25 (links check):**
  - Added `mu` ← `skh` as a loop peer check. Micron's peer table uses SK hynix's market
    multiples, and should use the analysis from now on.
  - Added DNB Teknologi's existing company blocks, which were missing from the register:
    - amzn, nvda, tsm, msft and googl (`main`);
    - mu (`loop`, memory evidence).
  - Not linked: global-index and equity (SK hynix is an emerging-market name outside MSCI World),
    and portfolio (no direct holding).
- **2026-10-25:** `plsv` (Paratus) retired on the user's instruction: type static, its five inputs
  removed, the Paratus Q3 event dropped. The file stays as a cited source.
- **2026-10-25:** new document `smsn` (`docs/samsung-analysis.md`, v1) with its inputs (ai, equity,
  hy, nvda, mu, skh). Back-references: `ai` (loop company check, layer method only until 24 Oct),
  `dnbtek` (company blocks for the common and preference shares, layer path only until 22 Oct), and
  `mu` and `skh` (loop peer checks, not yet read), so the next check flags them. Events: Samsung Q3
  (29 Oct) now also affects smsn and includes the Q3 dividend; SK hynix Q3, NVIDIA Q3 and Micron FQ1
  also affect smsn; added Samsung's Q4 report and January board on the rest of the 2026 return
  (~29 Jan 2027, approx).
- **2026-10-25 (register audit):** first lint run (`update_check.py lint`). No structural
  error. Added 12 links the document headers name but the register lacked (dnbtek ← hy, hy-funds,
  global-index, portfolio (loop); equity ← global-index (loop); global-index ← hy-funds; hy ←
  hy-issuers (loop); mu ← hy-funds; msft ← hy; portfolio ← equity, hy, oil). New table "Not
  links" for six references judged not to be inputs. smsn and skh rows checked: correct.
- **2026-10-25 (week-ahead input):** from DNB Carnegie Week Ahead (23 Oct, user input):
  - **new status `watch`**, for data and decisions where a hold is expected;
  - **as `watch`:** FOMC 28 Oct, Norway retail 28 Oct, ECB 29 Oct, US GDP and PCE 29 Oct, Sweden
    GDP indicator 29 Oct, Norway registered unemployment and Norges Bank FX 30 Oct, euro-area and
    France GDP and France CPI 30 Oct;
  - **as `open`:** the UK Budget on 28 Oct (defense).
- **2026-10-26:** new document `kospi` (`docs/kospi-analysis.md`, v1, type fund, iaf-valuation
  2026-10-18.2) with its inputs: smsn and skh (company blocks), ai, equity, hy (`main`), and hy-funds,
  global-index and dnbtek (comparison rows, `main`). Downstream search of `docs/` (Kospi, EWY, FLKR,
  KORX, FLXK, MSCI Korea): only market-mood mentions in ai, msft, smsn and skh; no document reads it.
  Events: kospi added to SK hynix Q3 (28 Oct), Samsung Q3 (29 Oct), NVIDIA Q3, Micron FQ1 and the
  Samsung January board; new `watch` events for the MSCI November review (~12 Nov) and the FTSE and
  KOSPI 200 December reviews (~11 Dec). Lint: no structural error, no hints after naming the
  comparison files in the header.
- **2026-10-26 (later):** `kospi` v1.1, the user's choice to follow one or two candidates: FLXK and
  KORX. The MSCI November review event `dropped` (no candidate tracks MSCI); the FTSE and KOSPI 200
  December event now names FLXK and KORX. No value other documents read moved.
- **2026-10-26 (odl):** new document `odl` (`docs/odl-analysis.md`, v1, type company,
  iaf-valuation 2026-10-18.2, stale after 9 Nov). Inputs: rig (HE semis NCS row), oil (background
  via rig scenarios) and equity (exit cross-check, NOK path), all `main`. Not links: odl ↔ hy (the
  header says HY BBB is not used). Downstream search of `docs/` (Odfjell, ODL, ODRG02): only
  market facts in rig (fixtures, cover) and Odfjell Technology (a different issuer) in hy-funds; no
  document reads the analysis. Events: Odfjell Q3 report (3 Nov) added; odl added to Transocean
  Q3 (2 Nov); new event for the Deepsea Nordkapp 2028 rate (by 31 Dec, approx; odl, rig). Lint:
  no structural error, no hints.
- **2026-10-26 (v1.2):** `kospi` personal tax and account type removed at the user's instruction;
  candidates unchanged (FLXK, KORX). No value other documents read moved.
- **2026-10-26 (v1.3):** `kospi` follows FLXK only (user). The December event now names the FTSE
  review and FLXK only (KOSPI 200 review and KORX removed). No value other documents read moved.
- **2026-10-27 (scatec):** new document `scatec` (`docs/scatec-analysis.md`, v1, type company,
  iaf-valuation 2026-10-18.2, stale after 26 Nov). Inputs: equity (exit cross-check, NOK path) and
  hy (Bear refinancing spread), both `main`; no sector BBB covers renewables, so the asset marks
  and the Philippine reserve-market view are own assumptions. Downstream search of `docs/`
  (Scatec, SCATC): hy-funds holds Scatec bonds (Sissener, Fondsfinans HY), linked `hy-funds ←
  scatec` as `loop` (issuer credit check, not yet read); no other document uses the company.
  Events: Scatec Q3 report (30 Oct) and the Philippine reserve-market redesign proposal (~12 Apr
  2027, approx), both open. Lint: no structural error, no hints.
- **2026-10-27 (sed):** `sed` news update for the T-16 CPOC award (iaf-valuation 2026-10-18.2):
  Base IRR 8.3% → 6.7%, P_k NOK 6.02 → 6.03, price 6.55 → 6.80; verdict still fails; recorded
  `--changed no` (leaf), stale after 17 Nov. The 27 Oct award event now names `rig` only (a
  tender-assist print, ~$95k effective, for the next Rig BBB run). Events added: T-16 Phase 6
  end (~31 Mar 2027) and Phase 7 start (~1 Jul 2027), both approx.
- **2026-10-28 (run):** rig and supply small updates, both kept unchanged (`--changed no`);
  events closed: Westwood 26 Oct (count not public), T-16 award, Brazil runoff. `dof` news update
  for the Skandi Implementer sale, `--changed yes` (Base 11.3% → 9.0%, now fails); sale event done,
  delivery event added (~30 Jun 2027). Missing links added: `portfolio` ← capt, dof, hafnia, sed
  (`main`; the overview quotes each holding's IRR and verdict), entered at its 11 Oct base.
- **2026-10-28 (skh):** `skh` version 2 after the Q3 report, `--changed yes` (Seoul Base 27.7% →
  21.1%, still clears; nearly all from the price, +16%). The 28 Oct event now names ai, smsn and kospi
  only; the 19 Nov buyback event done (finished 21 Oct). Events added: Q3 business report (~16 Nov),
  Q3 dividend record date (30 Nov), Q4 report and the rest of the FY2026 return (~28 Jan 2027).
- **2026-10-28 (kospi):** `kospi` v1.4, FLXK only at the user's instruction (the six other ETFs and
  the KOSPI 200 comparison removed); SK hynix v2 inputs and 28 Oct prices. `--changed no` (no reader).
- **2026-10-28 (googl):** `googl` v2 after the Q3 report (iaf-valuation 2026-10-18.2), `--changed yes`
  (Base 3.8% → 4.6%, fails). The Alphabet Q3 event stays open for `ai` only. Events added: call
  transcript re-check (29 Oct), 10-Q (~5 Nov), Q4 report (~2 Feb 2027).
- **2026-10-29 (msft):** `msft` v3 after the Q1 FY27 report and call (iaf-valuation 2026-10-18.2),
  `--changed yes` (Base 8.8% → 9.5%, fails; company-block moves small). The Microsoft Q3 event stays
  open for `ai` only. Event added: Q2 FY27 report (~28 Jan 2027). update-chain 2026-10-29.1: Mode F
  now updates reporting companies at once.
- **2026-10-29:** `kospi` v1.5: FLXK cannot be bought on Nordnet (user's order rejected; no KID in
  Nordnet's instrument data). The followed fund is now IQQK (KID present). MSCI November review
  event back to `watch` (re-caps IQQK); FTSE December review `dropped`. No value other documents
  read moved.
- **2026-10-29 (smsn):** `smsn` v2 after the Q3 report, `--changed yes` (common Base 26.9% → 23.3%,
  preference 29.5% → 25.6%, both clear; new: chip bonus pool 12% of DS profit). The Samsung Q3 event
  stays open for ai and kospi. Event added: Q4 preliminary (~7 Jan 2027).
- **2026-10-29 (ai):** `ai` Update 5 (ai-market-bbb 2026-10-29.1, references refreshed), `--changed yes`:
  E-layer Base 2027 .97 → .92; all else kept; Bear signpost crossed (platform equity funding). Events
  done: Microsoft, Alphabet and SK hynix Q3 (all readers done); Samsung Q3 stays open for kospi.
  Events added: Samsung DART Q3 report (~14 Nov), Oracle Q2 FY27 (~10 Dec).
- **2026-10-29 (change gate):** msft, googl, mu, skh and smsn read AI BBB Update 5; the rows they read
  are unchanged (per its for-downstream table), so each got a kept-unchanged note and `--changed no`.
- **2026-10-29 (global-index):** re-mark, `--changed yes` (small: Base −0.08 pp, verdicts unchanged).
- **2026-10-29 (kospi):** v1.6 with Samsung v2 and 29 Oct prices, `--changed no`; Samsung Q3 event done
  (all readers done); kospi added to the Samsung DART event (~14 Nov). The dnbtek input is left unread
  (its 30 Oct run follows Amazon's report).
- **2026-10-29 (kog):** `kog` v2 after the Q3 report, `--changed yes` (Base −19.9% → −16.2%, fails; price
  +13% on the day). Links added: kog ← equity (exit references, new in v2) and portfolio ← kog (the overview
  quotes its margin of safety). The Kongsberg Q3 event stays open for defense; Q4 (11 Feb 2027) added.
  New event: Heimdal Høyrente NAV −1.4% in a week (open, hy-funds and hy-issuers).
- **2026-10-30 (scatec):** `scatec` v2 after the Q3 report (iaf-valuation 2026-10-29.1), `--changed yes`
  (Base 14.5% → 16.4%, P_k NOK 86.5 → 95.5 vs 84.65, +13%, clears; Bear −17.9%; the Bear corporate NIBD
  that hy-funds reads moved 6.0 → 8.5bn by 2029). Q4 Philippine EBITDA guided 200–300 (impact −80m);
  corporate NIBD 5.7bn at 30 Sep. Scatec Q3 event done. Events added: Scatec Q4 report (29 Jan 2027),
  EBRD Egypt platform closing (~31 Mar 2027, date assumed), SCATC05 repayment (H1 2027). The ERC
  redesign event (~12 Apr 2027) stays open.
- **2026-10-30 (amzn):** `amzn` v2 after the Q3 report (iaf-valuation 2026-10-29.1), `--changed yes` (Base
  6.8% → 9.2%, fails). The Amazon Q3 event stays open for `ai`. Event added: Amazon Q4 (~4 Feb 2027).
- **2026-10-31 (hy-issuers):** update on Heimdal's marks (user paste of the managers' forum posts), `--changed
  yes`: Intrum and Trustly Distressed, HX split, new Fund read-out section. Intrum Q3 and the Heimdal NAV events
  stay open for hy-funds. Events added: Trustly Q3 (25 Nov), HX top-up certificate (~12 Jan 2027); the Heimdal
  October report event (~6 Nov) now also names hy-funds.
- **2026-10-31 (dnbtek):** re-run on Amazon v2, MSFT v3, GOOGL v2, SK hynix v2, Samsung v2, AI Update 5 and
  the index funds; `--changed yes` (Base 7.2% → 8.6%, fails; P_k NAV 6,715 vs 7,375). Memory now via company
  blocks; after-tax rows removed (no-tax rule).
- **2026-10-31 (hy-funds):** re-run, `--changed yes` (HH N 0.219 → 0.239, Attractive; HH+ 0.355; SIS 0.347;
  FF HY 0.395; FFK 0.424; HY reference unchanged at 0.196). Events done: Intrum Q3, Heimdal NAV week. Events
  added: FF and Sissener October reports (~10 Nov), Intrum Q4 (4 Feb), HX February coupon (~11 Feb), Nordic
  Trustee default report (~15 Feb); hy-funds added to the HX certificate event.
- **2026-11-01 (hy-funds):** checkpoint 1 closed on the user's word: Heimdal's report yields are in NOK.
  No carry correction; the NOK-basis case (0.29–0.34) dropped. `--changed no`.
- **2026-11-01 (global-index):** scope note: Nordnet Global Indeks dropped from the next run (user); no value
  changed now. `--changed no`.
- **2026-11-01 (googl):** price re-mark (30 Oct close $279.84, −13.9%), `--changed no` (EPS, D_t, V_T
  unchanged; only interim V_t glide moved; readers unaffected).
- **2026-11-01 (review-kospi):** new static document `docs/review-kospi-analysis.md` (review of kospi v1.6
  for an IQQK position; no inputs tracked, read by no document, no events). `kospi` rev used corrected
  2026-10-29.1 → 2026-10-18.2 to match its header (the header wins); no value changed.
- **2026-11-01 (review-kospi):** section 5 added on the user's follow-up: E / R against HY is not the gate
  for IQQK; the analysis should lead with the memory cycle (to be written in the AI BBB H2 layer). Static,
  no value other documents read.
- **2026-11-01 (ai):** Update 6 (ai-market-bbb 2026-11-01.1: new Step 2b memory cycle), `--changed yes`
  (no path moved; the kospi memory basket row moved on prices and skh, smsn, kospi lead with the new
  section). Amazon Q3 event done. Events added: contract price prints (~30 Nov, ~31 Dec); ai and kospi
  added to the SK hynix business-report event. iaf-valuation 2026-11-01.1: cyclical positions lead
  with the cycle.
- **2026-11-02 (nvda):** v1.1 light update, `--changed yes` (Base 13.0% → 13.3%, P_k $220.1 → $211.7; Bear
  −4.0% → −11.4% from AI Update 2's Bear path, read late). Not-links row nvda–global-index removed (v1.1
  takes World from Equity BBB only).
- **2026-11-04 (oil):** recorded the 31 Oct weekly-run oil update the run left unrecorded: kept unchanged,
  stale after 7 Nov (planned follow-up).
- **2026-11-04 (change gate):** amzn, googl, msft, mu, skh and smsn read AI BBB Update 6 (rows unchanged);
  skh and smsn also NVIDIA v1.1 (supply commitments unchanged), mu also hy-funds 31 Oct (reference
  unchanged). Each got a kept-unchanged note and `--changed no`.
- **2026-11-04 (kospi):** v1.7 per the user's review (cycle-first, withholding in Base, korea.py stub fix,
  E / R gate dropped), 4 Nov Seoul close, `--changed no`.
- **2026-11-04 (change gate, rig):** borr, odl, sed and hy read the 4 Nov rig update (their rows unchanged);
  kept-unchanged notes, `--changed no`.
- **2026-11-04 (oil):** update for OPEC+ (held) and the US midterms (Democratic House and Senate), `--changed
  no` (paths, mid-cycle and weights kept; stub and Year-1 quarters mechanical; catalyst timing text). OPEC+ event
  done; the midterm event now names defense and equity. Events added: OPEC+ 29 Nov, Brent trigger watch (30 Nov),
  FY27 stopgap 11 Dec (watch), new Congress 3 Jan 2027.
- **2026-11-04 (supply):** small update, `--changed no` (paths kept; Q4-26 spot stubs re-marked; DOF takes the
  AHTS stub at its Q3 run on 12 Nov). Two recalibration triggers fired: full update due after the full rig
  update. Seabreeze October done; Equinor AHTS award moved to ~20 Nov (bids were due 3 Nov); Tidewater fixed to
  9 Nov; added Petrobras PSV proposals 17 Nov and Seabreeze November (~4 Dec).
- **2026-11-04 (hy-issuers):** Heimdal October reports read, `--changed yes` (Borr to Watch; HX SSSN to
  Stressed; HH net 2027 Base vs paths −0.15 → −0.50). Heimdal October event done. Flags: HY BBB stale trigger
  (October Nordic spread 490 bp, +60 bp); the October report shows the box yield (HH 8.78%) separately from the
  NOK yield (9.60%), which reopens the funds' yield-basis question. Events: Heimdal November reports (~4 Dec);
  hy-issuers added to the FF/Sissener October reports event.
- **2026-11-04 (rig, entered 5 Nov):** small update on Q3 fleet status (Transocean, Valaris, Noble, Seadrill) and
  Westwood September, `--changed yes`: recalibration trigger on UDW drillships; drillship Base 2027 400 → 420,
  Bull 430 → 450; other rows kept. Westwood Sep and 2 Nov events done (Transocean already done by the daily run);
  the early-Nov Q3 event stays open for borr; added Westwood October dashboard (~27 Nov). (These lines were missed
  on 4 Nov because a failed event-done stopped the script.)
- **2026-11-05 (review-ai-debt, ai):** new static document `docs/review-ai-debt-and-market-power.md` (evaluation of
  debt-funded AI expansion, data-centre multiples and market power; Mode D: Documents row only, no inputs, read by no
  document). Event added for ai: Meta Q4 report and first 2027 capex figure (~28 Jan 2027). `ai` recorded as of
  2026-11-05, `--changed no`: no path, scenario or verdict other documents read moved; the AI baseline got a second
  5 Nov note, a credit-by-tier signpost row and re-read signposts (neocloud funding and capex ÷ OCF with debt share
  crossed; Oracle credit row extended). The `record` command also moved the ai Inputs dates for mu, amzn, nvda, msft,
  googl, skh and smsn to their latest; they were restored by hand to the dates actually read (1 Nov and earlier),
  because the review did not re-read those analyses' 2–4 Nov changes. Lint: structure none, B none; C hints are the
  three older portfolio rows (dof, kog, hafnia), unrelated to this change, left.
- **2026-11-05 (ai, method change):** on the user's go-ahead the four method additions from `docs/review-ai-debt-and-market-power.md`
  were applied to `ai-market-bbb` (revision 2026-11-01.1 → **2026-11-05.1**): tiers for the E layer, credit by tier in
  K3, an independent per-company K1 build and payback coverage in Step 3; new `references/credit_tests.py` and
  `payback.py`. The baseline got the standing outputs (K1 company build, K3 credit row, payback coverage, tier tables);
  no value moved. `ai` recorded with `--rev 2026-11-05.1 --changed no --skip-inputs mu,amzn,nvda,tsm,msft,googl,skh,smsn`
  so the company-analysis input dates stay at what was read. No other skill or CLAUDE.md line changed.
- **2026-11-06 (ai, revert):** on the user's instruction ("not the qualification grade to be expected") the
  2026-11-05.1 method additions are reverted: `ai-market-bbb` → **2026-11-06.1** (text again 2026-11-01.1's;
  `references/credit_tests.py` and `payback.py` removed). `docs/ai-market-bbb.md`: second 5 Nov note, K1 company
  build, K3 credit-by-tier row, payback coverage, tier tables and the credit-by-tier signpost row removed; signposts
  back to the first 5 Nov reading (neocloud funding and capex ÷ OCF: first leg only). `ai` rev column set to
  2026-11-06.1; no value moved, so no record and no cascade. The review document stays as a static record, marked
  not adopted; the Meta Q4 event kept (a genuine K1 read-out), its review reference dropped.
- **2026-11-06 (mu, tsm, nvda, entered 6 Nov):** re-marks on the 5 Nov sell-off close (SOX −10 to −12% on fears that
  the Democratic sweep slows the data-centre build; AI BBB 5 Nov: a price event). mu v3 fails → clears (18.3%,
  +14.5%); tsm v1.1 light update fails → clears narrowly (13.7%, +4.8%; also read ai Updates 2–6, nvda, equity);
  nvda v1.2 clears by more (17.9%, +16.7%). All `--changed yes` (Base IRR and verdicts that dnbtek, global-index and
  the AI company check read moved), stale after 17 Nov (NVIDIA Q3). Event added: TSMC October revenue (~10 Nov).
- **2026-11-06 (equity):** Update 2, full update on the 5 Nov closes, `--changed yes`, stale 6 Dec. World Base
  5.2% → 6.6%, Oslo 2.5% → 2.6%; triggers moved with the HY reference (0.254); none crossed, World 1.6% above its
  pre-alert. New loop inputs amzn and mu (company blocks). Midterm event: equity read, defense left. Events: equity
  added to Norges Bank MPR 4/26 (17 Dec); MSCI November month-end (30 Nov) added.
- **2026-11-06 (dnbtek):** re-run on the 4 Nov NAV (5 Nov not yet published; 5 Nov estimate shown beside it),
  `--changed yes` (E / R, trigger NAV, Bear 2027 and the Sissener row moved), stale 17 Nov, skip global-index and
  portfolio. Base 8.6%, margin −8.9%, fails; E / R trigger now 6,399, below P_k 6,721. Edge texts: dnbtek→hy now
  supplies the HY reference, dnbtek→hy-funds only Sissener R. Events added: 5 Nov NAV (~7 Nov), October report (~15 Nov).
- **2026-11-06 (kospi):** version 1.8, price re-mark on the 6 Nov Seoul close, `--changed yes`, stale 17 Nov, skip
  hy-funds (on hold). Paths and blocks unchanged; margin +11% → +25%. Edge texts: the HY reference moves from
  kospi→hy-funds to kospi→hy. kospi added to the state-siting signpost events (ERCOT 10 Dec, governors, Texas Legislature).
- **2026-11-06 (dof):** news note on the Skandi Olinda extension (user link), `--changed no`, stale-after kept at
  11 Nov (Q3 12 Nov), inputs skipped (not re-read). Already inside every scenario; the rate is undisclosed. Supply BBB
  takes it as company backlog in its next update; no row moves.
- **2026-11-06 (hy-funds):** short update for Sissener on its October report (user), `--changed yes`, stale 10 Nov.
  The other four funds are not rerun; their 31 Oct E / R is restated against the new reference 0.254, and Heimdal
  Høyrente N falls to 94% (Marginal band). hy-issuers needs the Hofseth re-mark (~72) and an Intrum 2028 row
  (Sissener holds ~2%). October-reports event narrowed to Fondsfinans; Sissener November report (~8 Dec) added.
- **2026-11-06 (hy-funds, correction):** the user supplied Sissener's Norwegian NOK-R October report (F32): October
  +0.19% (derived ~+0.1%) and Intrum 2028 at 1.7% (~2%). Sissener E / R 0.333 → 0.343 (135% of 0.254); still
  Attractive. No date or link change.
- **2026-11-07 (holds, user):** HOLD prefixes in the notes: rig, shipping, supply and the Oslo companies (dof, sed,
  odl, scatec, capt, hafnia, dnb, stb) and shb until Wed 11 Nov; defense, rhm and kog until lifted; borr only on
  request (its value is the credit read in hy-issuers).
- **2026-11-07 (trigger rule, update-chain 2026-11-07.1):** new Documents column `affects` (after `last change`).
  Set by hand for the unread changes: hy → hy-issuers, global-index, portfolio (spread path and the HY reference;
  NIBOR path unchanged, so not the companies); equity → global-index, portfolio (World return; Oslo exit references
  and the NOK relative path barely moved); ai (7 Nov prices only), mu, nvda, tsm (price re-marks) → none; hy-funds,
  dnbtek → portfolio; all others `all`. Backup of the register before the change in the session scratchpad.
- **2026-11-08 (capt):** news note on the Amor 15-month TC (user paste), `--changed no`, inputs skipped (on hold to
  11 Nov; not re-read). ~+$14m in Base, verdict unchanged. Events: the TC (done) and a shipping period-market
  data point (watch).
- **2026-11-09 (dof):** news note on the Skandi Mariner option (user paste), `--changed no`, inputs skipped (on hold to
  11 Nov; not re-read), stale-after kept at 11 Nov. Event added (done).
- **2026-11-09 (portfolio retired):** the user deleted `docs/portfolio-overview.md` and does not keep a portfolio
  document. Its Documents, Inputs and Not links rows are removed, and `portfolio` is taken out of the `affects` lists.
- **2026-11-09 (capt):** on hold, only on request (user; position sold). No full update is planned at Q3 (30 Nov).
- **2026-11-09 (hy-issuers, hy-funds):** Fondsfinans' October report (user link). hy-issuers short update (`--affects hy-funds`,
  stale 18 Nov), then the full hy-funds re-run (`--affects none`: kospi, global-index and mu read only the market reference, now
  from hy; dnbtek reads Sissener, unmoved; stale 5 Dec). Events: Fondsfinans October reports and the Hofseth covenant step done
  (first test 31 Dec); Fondsfinans November holdings and the Cegal repayment added (watch).
- **2026-11-09 (hy-funds, Arctic):** Arctic Return L rerun on its October report and the 5 Nov HY BBB (user), `--affects none`.
  E / R 0.119 → 0.109; step-ups shift slightly, no graded fund or verdict moves.
- **2026-11-10 (dof, dnb):** news notes (user), both `--changed no`, inputs skipped (on hold to 11 Nov). Events: PLSV results (done),
  DNB Capital Markets Day (done), a supply PLSV data point (watch), and two NVIDIA watch items (probe; export controls).
- **2026-11-10 (iaf-valuation 2026-11-10.1):** output layout rules (user, after the NVIDIA report structure review). Every
  iaf document now shows the newer revision in list 6; that triggers no run. The NVIDIA Q3 event names the restructure.
- **2026-11-11 (nvda):** v1.3 short update (user, before 16:00), `--changed no`, stale 17 Nov. Base kept; China and customer
  financing answered in the Summary. Events: House briefing and Trump–Xi (18 Nov, watch), Senate Banking (Jan), Supermicro trial (Mar).
  tsm note corrected to v1.2 (the daily run recorded the dates but kept the v1.1 text).
- **2026-11-11 (oil):** full update (user ran the due list), `--changed yes --affects none` (Base Brent 2027 −4.5%, below the
  15% recalibration trigger; every reader checked, none near 1 pp or a verdict flip), stale 30 Nov. F27 trigger event done (fired
  4 Nov); IEA OMR, re-armed front trigger, Russian jet ban end and STEO added (watch).
- **2026-11-11 (hy, hy-issuers):** hy kept unchanged (`--changed no`; Taptravel, CPI, Riksbank minutes, oil 84 checked). hy-issuers:
  the Taptravel outcome added by hand (not held; `--changed no`). Events: Taptravel and CPI done; the Riksbank minutes stay open
  for shb only; November CPI (watch) and the Taptravel longstop added.
- **2026-11-11 (ai):** kept unchanged (`--changed no`), stale 17 Nov. CoreWeave event done; CoreWeave Q4 (~25 Feb) added.
  Open checkpoint 10 in the AI BBB: H1 assumes the neoclouds and labs NVIDIA helps fund stay funded (a method question for the user).
- **2026-11-11 (review-ai-h1):** new static review of AI BBB checkpoint 10 (user asked for a proper evaluation); no inputs,
  no readers. Nothing applied to the AI BBB or its skill until the user decides.
- **2026-11-11 (ai, Option A+):** applied on the user's go-ahead ("I trust the evaluation"): skill 2026-11-11.1, H1 note,
  widened signpost, checkpoint 10 closed. `--changed no`. A separate evaluation of K1 sustainability is running (user).
- **2026-11-11 (review-ai-k1):** new static review of K1 sustainability (user); no inputs, no readers. Nothing applied.
- **2026-11-11 (dof hold):** the user wants Supply BBB considered after DOF's Q3 (12 Nov) and before the DOF update, so dof is held
  until that check (the daily run would otherwise update dof first). Odfjell link of 11 Nov is an old release (Dec 2023 / Jan
  2024; Nordkapp to end-2026), superseded by the Jul 2026 extension to end-2028 already in odl: no change.
- **2026-11-11 (holds ended):** the 7 Nov holds to Wed 11 Nov are removed (10 rows: rig, shipping, supply and the Oslo names,
  shb). Still held: defense, rhm, kog (until lifted), borr and capt (on request), dof (supply check first).
- **2026-11-11 (ai, Option D):** re-run under skill 2026-11-11.2 (user: "Yes, apply D"), `--changed yes --affects nvda, msft,
  googl, amzn, dnbtek, global-index, equity`. The agent marked msft and googl urgent on a ±5% band; the iaf bands are ±2%, and
  both stay below −2% on the upper bound (−4.4% / −4.7%), so no verdict can flip and neither is marked urgent. tsm and the memory
  readers are not affected (H3, H2 kept). review-ai-k1 marked adopted. Events: GPU rental indices (watch), January roll-forward.
- **2026-11-12 (supply skill 2026-11-12.1):** Paratus not tracked (user: overhead, narrow segment); its company note in the
  skill is replaced by a market-data-only line. If a second covered owner is needed, Solstad Offshore (SOFF) is preferred, then
  Subsea 7 (SUBC). No register row changes (plsv already static since 25 Oct).
- **2026-11-12 (rig):** full update (user), `--changed yes --affects none` (only Bull 2027, the stub and secondary ranges moved;
  every reader checked), stale 12 Dec. SED Q3 event now also names rig; Westwood dashboard and the Hakuryu-5 FID added (watch).
  Noted for hy: its Oil Service text still quotes the drillship Bear as 400 (380 since 10 Oct); text only.
- **2026-11-12 (supply):** full update on rig 12 Nov (user), `--changed yes --affects none` (NS PSV spot Base 2027 +12%, PLSV Bear
  and Bull mid-cycle only; DOF's Base rows unchanged), stale 12 Dec. Tidewater Q3 and the PLSV data point done; DOF Q3 event now
  dof only; PLSV signatures (watch) and Tidewater Q4 added. The agent ran one read-only git command at its start (it failed, nothing
  changed); reported to the user.
- **2026-11-12 (dof):** hold lifted after the supply check; full update after Q3 in the new iaf layout, `--changed yes --affects none`
  (no readers), stale 12 Dec. Verdict fails → marginal. The 10 Nov "possible ~$60m upside" note is refuted: the round's rates are
  Petrobras totals, DOF's own backlog figures give a flat basis. DOF Q3 event done; dividend ex 20 Nov (watch), Q4 18 Feb and
  annual report 7 Apr 2027 added.
- **2026-11-12 (shb hold):** user: wait with Handelsbanken to its quarter report. HOLD until 3 Feb 2027 (year-end report); the
  Riksbank decision and minutes events are marked done here and are read at that run.
- **2026-11-12 (iaf-valuation 2026-11-12.1):** three rules from the DOF run (user): awarded-not-signed contracts at the awarded
  rate in every scenario; a rate-basis check for JV and charter-plus-services rates; model scripts kept in
  references/models/<id>/ (DOF and NVIDIA v1.3 copied; DOF reproduces 11.8% / P_k 127.9). Method only; list 6 shows it.
- **2026-11-12 (lean documents):** the user adopted lean documents. CLAUDE.md rule; update-chain 2026-11-12.1; lint part D (size
  budget); this change log moved here from the register (register 738 → 437 lines). Documents are compacted at their own next run;
  the AI BBB is compacted now (agent).
- **2026-11-12 (nvda):** v1.5 news update after Huang's resignation (user), `--changed yes --affects ai, equity, global-index, dnbtek`
  (no verdict flips), stale 17 Nov. Board-decision event done; 13F, Anthropic pricing, NDAA and permanent-CEO events added. The
  agent ran one read-only `git config` by mistake (no change); a v1.4 re-mark of 08:22 came from the daily run.
- **2026-11-12 (log folder):** docs/archive/ is git-ignored (**/Archive/ in the root .gitignore), so the register log moved to
  docs/log/register-log.md to stay versioned; references updated (CLAUDE.md, update-chain, memory).
- **2026-11-12 (ai, compaction):** AI BBB compacted to the lean rules (3,228 → 763 lines, Interface section first), `--changed no`.
  2,458 interface numbers checked (38 removed, all superseded); every script reproduces the figures. Old version in git.
- **2026-11-13 (events, duplicates):** two duplicate events set to `dropped`: the DOF $0.40 ex-dividend `watch` row (the
  `open` row stays) and the Westwood October dashboard `open` row (the `watch` row with the MCU/backlog re-run test stays).
  The two Anthropic IPO rows are not duplicates (different documents and status) and stay.
- **2026-11-13 (odl):** v2.1 ex-dividend re-mark, compacted 721 → 450 lines; Base IRR 8.1% → 9.0%, hurdle NOK 95.5 vs NOK 102.80, fails. `--changed yes --affects none`; event "ODL Q3 dividend ... goes ex" done.
- **2026-11-13 (shipping):** update run; stub and "now" asset values re-marked, paths unchanged. `--changed yes --affects none`. Events: port-fee deadline and Amor watch done; Trump–Xi gets shipping; added Hafnia Q3 deck (watch), Frontline Q3 (watch), port-fee suspensions end 10 Jan 2027 (open). capt Inputs row: Suezmax added (header uses VLCC / Suezmax / Aframax-LR2).
