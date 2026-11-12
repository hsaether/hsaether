# Review: exit criteria in IAF and alignment with Equity BBB — 18 Oct 2026

Skill revisions behind the documents reviewed: **iaf-valuation 2026-10-11.3**, **equity-market-bbb
2026-10-18.5**, **rig-market-bbb 2026-10-10.1**.

Documents reviewed: `.claude/skills/iaf-valuation/SKILL.md` (Steps 2A, 2B, 3, 5),
`.claude/skills/equity-market-bbb/SKILL.md` (Steps A, C, D), `docs/equity-market-bbb.md` (Oslo build,
P/B–ROE table, mid-cycle inputs), `docs/SED-analysis.md` (17 Oct), `docs/msft-analysis.md`,
`docs/nvda-analysis.md`, `docs/rig-market-bbb.md` (asset-value convention). No new market data was
fetched. Figures tagged `[A]` are my own calculations in this review.

**Status 18 Oct: all six changes applied** (iaf-valuation 2026-10-18.1, equity-market-bbb
2026-10-18.6) and SED re-run. See "Applied" at the end; two statements in section 3 are corrected
there.

**Question (user):** IAF and Equity BBB need to be aligned. IAF says the share "trades at NAV at
exit", while Equity BBB uses P/B. SED says contracts assumed after 2029 no longer count in V_T, but
the business does not end in 2029. Review the exit criteria in IAF.

## Answer in brief

- **The exit is not the end of the business.** V_T is the price a buyer would pay for the share on
  31 Dec 2029, for a company that keeps operating afterwards. The window ends there only because the
  forecast stops there; everything after 2029 is priced into V_T at normalised (mid-cycle)
  earnings. The skill never says this in one sentence, and it should.
- **"Trades at NAV" and the index P/B do not contradict each other**, because NAV is not book. NAV
  marks the rigs and ships at what the asset market pays for their mid-cycle cash flows; book is
  historic cost. SED's V_T is above its book, so P/NAV = 1 already means P/B > 1. What *is*
  missing is a check that the return a buyer at exit gets is consistent with the market's return
  in Equity BBB. Equity BBB has that check (P/B against ROE); IAF has none.
- **The SED exit rule is too strict, and the reasons given for it are confusing.** Within the Base
  scenario, SED has signed contracts that run into 2030–31. On 31 Dec 2029 they are backlog, and a
  buyer pays for them. The 17 Oct version ignores them. About three quarters of that premium is
  utilisation (a contracted rig is not idle) and one quarter rate; both are real for a contract in
  place. What the 10 Oct version lacked was a limit on how far a scenario's contracts reach past
  exit. Recommendation: count backlog the scenario holds at exit, capped at 2 years after exit and
  on the same earnings basis as the asset marks.
- **Track A (steady companies): the skill text still assumes today's P/E holds at exit.** The
  Microsoft and NVIDIA analyses already use an independent exit P/E, as Equity BBB does. The
  difference is large: Microsoft gives 12.4% at constant P/E and 8.8% at exit P/E 23. The skill
  should say what the analyses already do.
- **Six changes are proposed** (table at the end). Two change numbers: the backlog rule (re-run
  SED) and FX in Bear/Bull. The other four make the text clear and add a cross-check.

## 1. What V_T is

| Question | Answer |
|---|---|
| What is sold at exit? | The share, at a market price, on 31 Dec of Year 3 (now 2029) |
| Does the business stop? | No. The buyer pays for all cash flows after 2029 |
| How are cash flows after 2029 valued? | At **normalised (mid-cycle)** earnings, because a 3-year forecast cannot see the cycle beyond 2029 |
| At what required return? | **The market's at exit**, not k. k = 12% is the investor's hurdle for buying today. A buyer in 2029 pays the market price, and the market prices at its own required return |
| Why mid-cycle and not 2029 earnings? | 2029 can be a peak or a trough. Capitalising a peak (or a trough) for ever is the most common valuation error in cyclicals |
| Where does the forecast meet mid-cycle? | The exit-consistency test (Step 3): a gap > 10% between 2029 and mid-cycle needs a named reason or a 2-year reversion tail |

The three exit methods in use are three versions of this one rule:

| | Track B (rigs, ships, OSVs) | Track A (MSFT, NVDA, defense) | Equity BBB (Oslo, World) |
|---|---|---|---|
| V_T | NAV: assets at mid-cycle asset values (age at exit) + contract premium − net debt | Exit P/E × normalised EPS of 2030 + net cash (practice); constant P/E (skill text) | Mid-cycle P/E × normalised EPS of 2030 + retained cash |
| Market price set by | The secondhand asset market (Rig BBB: annuity at 8% over remaining life, checked against transactions) | Own P/E history, AI BBB layer exit P/E | Long-run forward P/E averages |
| Required return implied at exit | ~8% nominal on the assets (Rig BBB rate) | Not stated | Oslo 9.1%, World 8.2% (Base mid-cycle return, Step D) |
| Re-rating | Named: P/NAV_0 gap closing by exit | Named in practice; absent in the skill's Track A | Named: P/E now → exit P/E |
| Cross-check | None | None in the skill | P/B against ROE, exit P/B inside the history band |

## 2. NAV at exit versus P/B

**The two are linked by one identity.** Price = book × (ROE − g) ÷ (r − g), where r is the market's
required return. A company earning ROE above r trades above book. A company whose assets are marked
at market value earns about r on that marked value, so it trades at about 1.0x that value.

- **Oslo index:** exit P/B 1.75 at a normalised ROE of 15.2% (Equity BBB, P/B–ROE table). This holds
  because Equinor, DNB, Kongsberg and others earn well above r on historic book.
- **SED:** the exit rig values (Base, $336.5m) are above rig book ($279m at 30 Jun 2026 `[F]`, lower
  by 2029 after depreciation). So V_T at NAV already implies P/B above 1.
- **So "trades at NAV" is not "trades at book".** There is no conflict in principle.

**The gap is the missing check.** IAF never asks what return a buyer at exit gets:
- Rig values are an annuity at **8%** over the rig's remaining life (Rig BBB convention, checked
  against the 2026 jackup sales at +8% to +12%).
- The Oslo index at its exit P/E gives a buyer **9.1%** (Base mid-cycle return).
- At 9.1% instead of 8%, a rig with 12 years left is worth **about 5.5% less** `[A]`. For SED Base
  that is about $18m, or NOK 0.24 per share `[A]` (rough: before the $10m floor and tax effects).
- The asset market and the stock market can price the same rig differently. Listed owners often
  trade below NAV for long periods. The workspace has no P/NAV history to test this `[?]`.

**Recommendation:** keep NAV at mid-cycle marks as the Track B exit. It is the most independent
exit available, because it comes from transactions, not from the analyst. Add a cross-check in
every analysis: exit P/E (V_T ÷ normalised earnings), exit P/B (V_T ÷ book at exit) and the
buyer's implied return, beside the Equity BBB figures. If the buyer's return is below the Oslo
mid-cycle return with no stated reason, show a sensitivity at that return.

## 3. The SED rule: which contracts count at exit

**What it says, in plain words.** At 31 Dec 2029 each rig is valued as if it will earn mid-cycle
rates for the rest of its life. A rig on a contract above mid-cycle is worth more, so the excess (the
"firm-contract premium") is added. The question is which contracts count:
- **10 Oct version:** every contract in the scenario that runs past 2029, including those the
  scenario assumes SED signs in 2027–29 (for example T-16 at $85k from Jul 2029 for 30 months).
- **17 Oct version:** only contracts signed today (EDrill-2, to Oct 2030). The rigs on contracts
  the scenario assumes are treated as idle at mid-cycle from 1 Jan 2030. Effect −$34m in V_T and
  −2.3 pp in Base IRR.

**Assessment: the 17 Oct rule is internally inconsistent.**
- Base is the decision case and is trusted to 31 Dec 2029. In Base, T-16 is on contract into 2031
  on that date. A buyer would pay for it. Ignoring it values a contracted rig as idle.
- The rule's stated reason ("no scenario rate path past T") does not fit SED. The Base rate gap is
  only +6% (85 vs 80), below the 10% materiality threshold.
- **The real issue in the 10 Oct version was utilisation, not rate.** It valued the assumed
  contracts at full utilisation against a mid-cycle that assumes 80% utilisation (MCU). Per day:
  contract $85k × ~98% against mid-cycle $80k × 80% × ~98% gives a gap of ~$20k a day. About
  **three quarters of it comes from utilisation and one quarter from rate** `[A]`. Applied to
  contracts of whatever length the scenario chose, that inflated V_T.
- **The skill itself does not settle this.** Step 3 speaks of "days under firm contract after T"
  without saying firm when. SED read it as "firm today". DOF, Hafnia and CAPT do not use that
  reading. The analyses are therefore not consistent with each other.

**Proposed rule (Step 3, replaces the open wording):**
- **NAV_0 (valuation date):** only contracts firm today. No change.
- **V_T (exit):** count the backlog the scenario holds on the exit date:
  - contracts firm today, for their full term;
  - contracts the scenario assumes are signed before exit, for **at most 2 years after exit** (the
    same bridge length as the reversion tail), at the scenario's rate when signed, and never longer
    than the typical term in the sector BBB.
- **Premium on the same earnings basis as the asset marks:** (contract rate × revenue efficiency) −
  (mid-cycle rate × MCU × revenue efficiency). If the sector BBB gives no MCU for the row (tender
  rigs today), state the MCU used and tag it `[A]`.
- **Days counted as backlog are left out of the exit-consistency gap test.** This avoids counting
  them twice with the tail.
- **Show the assumed-backlog premium as its own line** in the V_T bridge, with IRR_T and P_k without
  it (the 17 Oct rule) as a sensitivity.

**Effect on SED (re-run 18 Oct):** all of the −2.3 pp comes back (Base 6.0% → 8.3%). The 10 Oct
model already used the earnings basis, and SED's assumed contracts end in Jan 2031, inside the
cap; only Bull Vencedor is cut. The verdict stays **fails** (margin of safety −8.0%).

## 4. Track A: the skill text versus the analyses

- **Skill text (Definitions and Step 2A):** g = EPS CAGR, "value growth at a constant PE". This means
  the exit P/E equals today's P/E.
- **Practice:** Microsoft and NVIDIA build V_T = independent exit P/E × normalised 2030 EPS + net
  cash, with a dated IRR and P_k. This is the Equity BBB method.
- **The difference is large:** Microsoft passes Rule 1 at constant P/E (d + g = 12.4%) but returns
  8.8% at exit P/E 23 and fails. At 29x earnings, a constant P/E assumes the growth premium lasts
  for ever.
- **Proposal:** Track A decides on the dated IRR to an **independent exit P/E** on normalised EPS
  of the year after exit. Anchors: own history, the AI BBB layer exit P/E or Equity BBB's index exit
  P/E, with the premium or discount to the index stated. Rule 1 at constant P/E stays as a quick
  screen, labelled "assumes today's P/E holds". Rule 3 is unchanged.

## 5. Other alignment points

- **FX.** IAF says it keeps spot FX; Equity BBB sets the NOK path per scenario. In Base this makes no
  difference (MPR I-44 flat ≈ spot). In Bear it does: the index weakens the krone, which cushions
  USD earners in NOK. The Microsoft analysis already uses that (Bear −7.6% in USD, −5.0% in NOK),
  against the skill text. **Proposal:** P_k and the decision stay in the trading currency at spot;
  Bear and Bull report the NOK return on the Equity BBB NOK path for USD cash flows and V_T. For
  Oslo-listed USD reporters (SED, DOF, Hafnia) this lifts Bear in NOK.
- **Exit consistency in Equity BBB.** IAF tests the jump from 2029 to mid-cycle; Equity BBB jumps
  from 2029 EPS to normalised 2030 EPS with no test. Today no Oslo block is material (energy 0.86
  in 2029 against 0.82 normalised, +4.9%; F 0.95 against 0.93) `[A]`. **Proposal:** add the same
  > 10% test per block (named reason or 2-year tail). No number changes today.
- **Required return at exit.** Both modules already price the exit at the market's return, not at
  k, but only Equity BBB says so (via the mid-cycle P/E). **Proposal:** one sentence in IAF Step 3.

## 6. Proposed changes

| # | Change | Skill | Changes numbers? |
|---|---|---|---|
| 1 | One exit principle at the top of Step 3: V_T is the market price of the continuing business at exit, on normalised earnings, at the market's return at exit (never k, never the ceiling) | IAF; Equity BBB refers to it | No |
| 2 | Backlog at exit: firm today in full; scenario-signed for at most 2 years after exit; earnings basis; own bridge line and sensitivity | IAF Step 3 | **Yes: re-run SED** (check DOF, PLSV, Hafnia, CAPT) |
| 3 | Track A: decide on the dated IRR to an independent exit P/E; constant-P/E Rule 1 as a labelled screen | IAF Definitions, Step 2A | No (practice already) |
| 4 | Exit cross-check in every analysis: exit P/E, exit P/B, buyer's implied return beside Equity BBB (Oslo 9.1%, World 8.2%); sensitivity if below | IAF Step 3 and Step 7 | Adds a table |
| 5 | Exit-consistency test per block in the index build | Equity BBB Step C | No (no block material today) |
| 6 | Bear/Bull NOK return on the Equity BBB NOK path for USD flows; decision at spot | IAF Data sources, FX rule | Yes, Bear in NOK for USD earners |

Order of work if accepted: 1, 3 and 4 together (text), then 2 with the SED re-run, then 5 and 6.

## Applied (18 Oct 2026)

| # | Where | What was done |
|---|---|---|
| 1 | IAF Step 3 (top) | Exit principle: continuing business, normalised earnings, market pricing at exit, never k |
| 2 | IAF Step 3, 5, 7, checks | Backlog at exit (firm today in full; scenario-signed capped at 2 years; earnings basis; own bridge line; firm-today-only sensitivity). Exit-consistency test on open days only. Structural run keeps scenario backlog at the mid-cycle rate |
| 3 | IAF Definitions, Step 1, 2A, 6, checks | Track A decides on a dated IRR to an independent exit P/E; constant-P/E Rule 1 is a labelled screen |
| 4 | IAF Step 3, 7, checks | Exit cross-check table (exit P/E, exit P/B, buyer's return vs Equity BBB) with a sensitivity at the index return |
| 5 | Equity BBB Step C, Interface, checks | Exit principle; exit-consistency test per block; exit reference rows in the Interface. The document gets the table at its next run (no block is material today) |
| 6 | IAF FX rule, Data sources, Step 7 | Decision at spot; Bear/Bull also in NOK on the Equity BBB NOK path |

**SED re-run** (`docs/SED-analysis.md`, 18 Oct; inputs unchanged):

| | Bear | Base | Bull |
|---|---|---|---|
| IRR_T, 17 Oct rule → backlog rule | −35.3% → −31.4% | 6.0% → **8.3%** | 27.8% → 29.9% |
| P_k / margin of safety | 2.13 / −67.5% | **6.02 / −8.0%** | 9.59 / +46.4% |
| IRR_T in NOK on the Equity BBB path | −29.3% | 8.3% | 28.5% |
| Exit P/E on FCF_normalised before holdco G&A / exit P/B | 17.2x / 0.38 | 10.2x / 1.19 | 9.2x / 1.93 |

**Corrections to section 3:** the 10 Oct premium was already on the earnings basis, so the "earnings
basis" in the proposed rule does not cut it; and the 2-year cap binds only for Bull Vencedor. Hence
the full reversal.

**Holdco G&A (decided by the user, 18 Oct; iaf-valuation 2026-10-18.2):** holding-company G&A is
**not** deducted in NAV. NAV values the assets; the holding company finances and sets strategy but
does not operate them. Overhead that runs the assets belongs in the asset opex. Holdco G&A stays in
the window's cash flows as paid. The cross-check's exit P/E is therefore on asset-level earnings
(before holdco G&A): SED Base 10.2x against Oslo's 11.5x, consistent. PLSV deducts holdco G&A
(−$45m) and needs a re-run under this rule.
