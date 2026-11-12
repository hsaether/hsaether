# Review: HY Market BBB, the HY fund report and default tracking — 18 Oct 2026

Skill revision behind this review: **hy-market-bbb 2026-10-17.1**. The documents reviewed were
written under older revisions: `docs/hy-market-bbb.md` (baseline 17 Oct, under 2026-10-15.1),
`docs/hy-funds-analysis.md` (says 2026-10-11.3, last edited 18 Oct) and `docs/hy-issuers.md` (says
2026-10-11.1). No new market data was fetched. Every number below comes from those documents,
unless it is tagged `[A]` (my own arithmetic or assumption in this review).

**Questions (user):** review HY Market BBB and the HY fund report; review the report's
readability; evaluate how potential defaults are tracked.

## Answer in brief

- **The method holds up.** Every E / R, step-up and 2027 build in the comparison reproduces from
  its inputs (checked: all six E / R values, all five step-ups, the market reference 0.196 and the
  market step-up 0.212). The idea of charging loss only to named bonds, with one price, PD and
  recovery per bond across all funds, is sound and well documented.
- **The fund report is hard to read.** It is accurate line by line, but it is 1,151 lines long with
  no summary at the top. The comparison table has 16 columns with prose in its cells. Abbreviations
  are not explained, and a 146-line change log sits in the main body. Partial updates have also
  left it out of step with itself (section 2).
- **Default tracking works for the bonds the funds hold, but not at market level:**
  - Bond by bond it is good. Prices come from actual holdings, notices are read and classified, and
    Hofseth was caught on its way from 97.9 to 76.
  - The market-level running default rate cannot be measured yet. So the main default trigger
    cannot fire.
  - 58–73% of the named loss in Sissener and the two Heimdal funds rests on prices that are 8–10
    months old or assumed.
  - Funds get **no allowance in 2027 for defaults that are not visible today**, while the market
    reference they are judged against has one. That tilts every verdict towards "attractive". It
    matters only for Høyrente N, which would drop to the line (section 3, gap 2).

## 1. Readability of the fund report

**What works:**
- Plain English, short sentences, and tags on every number.
- "What it means" passages turn numbers into consequences, for example "if Hofseth defaults, the
  fund loses 2.8% × 28% ≈ 0.8% of NAV".
- "What would change the verdicts" is the most useful part of the file. Keep it.

**What gets in the way** (line counts from the file):

| # | Problem | Where | Fix |
|---|---|---|---|
| R1 | No summary. The first result appears after 60 lines of metadata and method | Top | A 6–10 line summary first: one line per fund (verdict, E / R, what drives it), what changed, and the two open items that could flip a verdict |
| R2 | The comparison table has 16 columns, and cells hold sentences ("Balanced: selective; also workouts (Havila 49 → 76 in 2024; an equity conversion up 23×)") | Comparison | Split it into three tables of ≤ 7 columns: **Decision** (fund, Base window, E, R, E / R as % of market, step-up, verdict); **Risk** (at-risk % of NAV, Base loss 2027, Bear loss 2027, Bear window / worst year, single-name stress, oil share); **Profile** (style, yield and basis, durations, cash read as, liquidity). Style text goes in the fund sections |
| R3 | Abbreviations without a legend: FF (45 uses), HH, HH N, HH+, SIS, q, E, R, PD, LGD, EL, MTM, YTM, AT1/T2, ASK, AIF | Whole file | A short "How to read this" box after the summary: the decision rule, the tags and the abbreviations |
| R4 | Reference material sits in the main flow. The share-class and Nordnet section (55 lines) comes between the comparison and the credit loss | After the comparison | Move it to an appendix. It changes no verdict |
| R5 | The change log is 146 lines (13% of the file). It is full of superseded ratios (0.442, 0.386, 0.182 …) that a reader can mistake for current ones | End | Keep the latest run in full and one line per older run. Git holds the rest |
| R6 | Fund sections are uneven. FF has 145 lines with five portfolio subsections (including year-end 2025). Pluss has 66 lines, with no mapping table and no 2027 build. The Kreditt *evaluation* (160 lines) is longer than any tracked fund | Fund sections | One fixed template per fund: Facts · Snapshot · Credit loss · 2027 build · Return paths · Verdict. Move historical portfolios to an appendix and cut Kreditt to ~40 lines |
| R7 | One bond, several prices: Hofseth appears at 72.5, ≈ 74 clean, 76.2, 77.0 and 97.9 | Bond table, FF section, change log | Show one current price per bond, with its date, in the bond table. Older prices only in a price-history line |
| R8 | Nesting is deep. 55 bullets sit at the third level or deeper | Throughout | Keep to two levels; turn third-level lists into short tables or sentences |
| R9 | False precision. E / R is shown to three decimals (0.392) on inputs that are `[A]` or `[?]` | Comparison | Two decimals plus % of the market reference |

**Proposed order:**
1. Summary.
2. How to read this.
3. Decision, Risk and Profile tables.
4. What would change the verdicts.
5. Credit loss bond by bond.
6. Fund sections (fixed template).
7. Reference fund.
8. Appendix: share classes and route, manager record, historical portfolios, change log, sources.

## 2. Consistency: the three files are out of step

Most of these come from partial updates (prices only, or one file only) that did not carry
through to the other tables and files. None of them moves a verdict.

| # | What | Says | Should say |
|---|---|---|---|
| C1 | Fund file H1 and Metadata date | 11 Oct 2026 | 18 Oct (the change log has 18 Oct entries) |
| C2 | Fund file skill revision | 2026-10-11.3 | 2026-10-17.1 (the 17 Oct change log entry cites .17.1) |
| C3 | Fund file "HY Market BBB used" | 5 Oct baseline, stale after 4 Nov | 17 Oct baseline (kept unchanged), stale after 5 Nov |
| C4 | FF at-risk weight | 4.6% in the comparison and in the FF section | 4.4% in the bond table (30 Sep weights) |
| C5 | Named losses at 30 Sep prices | Recomputed in a bullet (FF 0.39, SIS 0.75, HH+ 1.13, HH 1.02) | The comparison and the credit-loss table still show 0.40 / 0.74 / 1.12 / 1.01. Not rerunning is correct (below the minimum change), but the tables should say "11 Oct values, not rerun" |
| C6 | Sissener: Hofseth's share of the loss | 0.19 in the credit-loss table | 0.20 in the Sissener section |
| C7 | Hofseth clean price at 30 Sep | ≈ 74 (fund file); ≈ 75 (market file, twice) | ≈ 74: 76.2 − 0.25 × 8.244 = 74.1 (skill rule) |
| C8 | "What changed since 6 Oct" table | Ends at 11 Oct | Add the 18 Oct price row, or rename the table |
| C9 | Kistos and Eldorado notices | Issuer file: purpose "not read" `[?]` (data gap 4) | Market file: Kistos read on 17 Oct (escrow waiver, routine). The issuer file was not updated after 11 Oct |
| C10 | Stamdata scan window | Issuer file 4 Aug–6 Oct; market log 4 Aug–16 Oct; market checkpoint 1 "1 Sep to 16 Oct"; market source S8 "1 Sep–5 Oct" | One window, stated once and referenced |
| C11 | Fund checkpoint 1: the five Heimdal-only names "set ~60% of the Heimdal named loss" | ~60% | ~31% (HH) and ~32% (HH+) for those five. It is 58–65% only when Shearwater and Viaplay, priced in Feb 2026 and at end-2025, are added `[A]` |
| C12 | 2027 builds (FF, Kreditt): "− 0.15" in the spread carry | Not explained | Name what it is |
| C13 | News held only in the market file | Elcano sold its loss-making LNG ship (held by both FF funds); Hofseth's NOK 600m equity raise pushed to year-end | Add both to the issuer file, which is the funds' credit-loss input |
| C14 | Market file change log and checkpoints | Not in date order; the first checkpoint (HX) has no number | Date order; number every checkpoint |

## 3. How potential defaults are tracked

**The chain today:**

| Layer | File | What it tracks | Source | Feeds |
|---|---|---|---|---|
| Market | `hy-market-bbb.md` | NT first-time default rate (annual); own default and distress log; running FTD replica; watchlist in buckets (a)–(d); signpost: distress notices per month | NT report (Feb); Stamdata news read by hand; press | Market FTD and EL paths, the market reference 0.196, the Bear catalyst loss |
| Issuer | `hy-issuers.md` | 29 companies: price, yield, status, PD, recovery, loss if default, expected return | Fund holdings (FF prices), annual reports, Heimdal contributions, Stamdata notice PDFs | The named loss in every fund |
| Fund | `hy-funds-analysis.md` | Named at-risk bonds per fund with weights; restructurings; residual from the manager's record | The issuer file and the fund holdings | E, R and the verdict |

**What works:**
- **The definitions are right.** NT first-time defaults include distressed exchanges and are
  weighted by volume, and re-defaults are not counted twice.
- **Notices are read, not just counted.** The PDFs are classified as distressed or routine
  (Kistos, Brightstar and Keystone were read as routine), which keeps false alarms out of the
  loss.
- **Prices come from actual holdings where possible:** Fondsfinans month-end holdings, annual
  reports, and price moves inferred from Heimdal's monthly contributions (HX: about −26% in
  August).
- **One bond, one set of inputs across funds,** so funds cannot look different just because they
  were assessed differently.
- **It caught a real case.** Hofseth went from 97.9 at end-2025 to 76.2, and the fund reports'
  commentary was cross-checked against the price.

**Gaps, most material first:**

1. **The market running default rate is not measured, so the main default trigger cannot fire.**
   - The log covers Stamdata only from 4 Aug, plus two press items for H1. Most outstanding
     volumes are `[?]`, and the running FTD is `[?]`. The recalibration trigger "running FTD
     deviates > 1.5 pp from Base" can therefore never be tested.
   - The "~3–4% a year" pace in the conclusion cannot be reproduced from the log. The market is
     ~NOK 750bn (implied by "9bn ≈ 1.2%").
     - **Corrected on 18 Oct.** The first version annualised over 4 Aug–16 Oct (~4.4% with HX,
       ~1.6% without). But the market-wide feed was read only from 1 Sep; August was read for held
       companies only (`docs/hy-market-bbb.md`, Metadata).
     - Over the market-wide window, 1 Sep–16 Oct (46 days), the logged FTDs with a volume are
       Booster 0.65bn, Cabonline 1.17bn and SIBS 0.61bn (NOK). That gives **~2.6% a year**, 1.9%
       without SIBS (whose first default may be 2025) and 3.7% with the pending Dooba `[A]`.
     - HX (Aug, NOK 4.2bn ≈ 0.56% of the market) falls outside that window.
     - The point stands: the pace moves with one or two classifications, and a six-week window is
       too short to annualise.
2. **The 2027 fund loss has no allowance for defaults that are not visible today, but the market
   reference has one.**
   - The skill sets the fund residual to 0 in 2027 ("one-year defaults are almost always visible
     beforehand"). The market reference charges the full FTD × LGD (1.65% in Base 2027). So each
     fund is compared with a benchmark that pays for a loss the fund is assumed never to have.
   - The files' own evidence argues against a hard zero. Hofseth was at 97.9 on 1 Jan and
     distressed by August, which is inside a year. The DNB vintage study puts ~10% of defaults
     within 18 months of issue.
   - **Size of the effect, illustration only** `[A]`: assume half of a year's defaults come from
     names that look healthy at the start of the year (untested). The 2027 allowance is then
     0.5 × 1.65 × q: FF 0.66, SIS 0.62, HH+ 0.84, HH N 0.68 pp. E / R becomes FF ≈ 0.36, SIS ≈
     0.34, HH+ ≈ 0.31, Kreditt ≈ 0.40, and **HH N ≈ 0.20, on the 0.196 line**. Only Høyrente N
     changes character.
   - **The claim can be tested.** Add a column to the default log: "priced < 90 or on the
     watchlist at 1 Jan of the default year?". After a year of log entries, the share of unseen
     defaults is measured instead of assumed.
3. **Stale or assumed prices carry most of the named loss outside Fondsfinans** `[A]`:

| Fund | Named loss 2027 | On a 30 Sep price | On a price from Feb 2026 or older, or assumed | Share stale or assumed |
|---|---|---|---|---|
| FF HY | 0.40 | all five names | — | 0% |
| Sissener | 0.74 | Hofseth 0.20 | Shearwater, W&T, Tullow, Viaplay, Trustly 0.54 | **73%** |
| Høyrente N | 1.01 | Sigma, Foxway 0.42 | Shearwater, Viaplay, Flora, Intrum, Trustly, Convene, Norse 0.59 | **58%** |
| Høyrente Pluss | 1.12 | Sigma, Foxway 0.40 | the same seven names, 0.73 | **65%** |

   The skill's own staleness rule (bond prices older than one week) is flagged in the text but
   still drives the PDs. Fixes, in order of yield:
   - Sissener's semi-annual report at 30 Jun 2026: every holding with a market value, from the same
     CDN as the annual report. Check whether it is out.
   - The Heimdal contribution method (already in the skill) for Shearwater, Trustly, Intrum,
     Convene, Norse and Flora. It has so far been applied only to HX.
   - For the non-Nordic bonds (W&T, Tullow), a public price page for the ISIN, as a source to try.
4. **The bucket rules are not applied consistently.** Each effect is ≤ 0.1 pp, so this is about
   traceability, not size:
   - **Shearwater (~86), Tullow (~88) and Viaplay (89.6) are priced 80–90 ("stressed", 10%) but
     get the watch value (5%).** At the stressed value their Base PDs would be 16.8 / 17.9 / 11.3
     instead of 14.3 / 15.4 / 8.8, adding ~0.07 pp to Sissener and ~0.06 pp to Høyrente `[A]`.
   - **Three Bear PDs do not follow "1.3 × the higher of bucket and implied".** Hofseth 52.0
     (the rule gives 33.3), Sigma 32.5 (20.0) and Viaplay 19.5 (16.5). The overrides are harsher,
     which is conservative, but they are not written down.
   - **The placeholders (5% for Trustly, Convene, Norse and Flora opco) sit below the rule's own
     result.** At the assumed ~12% yield the rule gives ~7%.
   - **Hofseth's market-implied PD uses the generic 45% LGD,** not its own 40% (recovery 60): 25.6
     instead of 28.8.
   - **There is a cliff at 80.** Sigma at exactly 80.0 gets 12.7%; at 79.9 the same rule gives
     17.7%. A continuous rule (the implied PD with a floor by price band) would remove the jump.
5. **There are two watchlists on two scales, and no master list.**
   - Market Step 5 uses buckets (a) vote or standstill, (b) < 60, (c) 60–80 and (d) maturity
     < 12 months. Step F9 uses watch / stressed 80–90 / distressed < 80. The market watchlist
     table mixes "(c)", "80–90", "monitor" and "watch (recovered)".
   - **8 of the 14 named fund bonds are missing from the market watchlist:** Shearwater, Tullow,
     W&T, Viaplay, Intrum, Convene, Norse and Flora opco. Bucket volumes are mostly `[?]`, which is
     why the Year-1 bucket build (Step 6) was never applied and Base 2027 FTD is set top-down.
6. **Outcomes are not recorded, so the PDs can never be calibrated.**
   - Names leave the list without a record: Kistos and Eldorado (back to performing), Sissener's
     Intrum bond (repaid), Foxway (74.65 → 96).
   - The 5 / 10 / 20% bucket values and the 50 / 50 / 20 / 30% conversion rates are `[A]` and
     "recalibrated from the log as outcomes arrive". Without an entry date, price and bucket, and
     an exit date and outcome (defaulted, cured, repaid, sold), there is nothing to recalibrate on.
7. **Recoveries are not collected.** The log has one recovery (LR Health & Beauty, ~67 ultimate).
   The 30-day post-event price is `[?]` for every event. The monthly Fondsfinans holdings and the
   Heimdal contributions could supply it for held names (HX first).

**Recommended tracking design** (fits the existing files and the Stamdata access rules):

| Change | What it gives |
|---|---|
| **One master watchlist in `hy-issuers.md`** with one status scale, used by both the market and the funds. Columns: entry date, entry price and bucket, current price and its date, exit date and outcome, held by. The market file references it and adds only the market names that are not held | One list, one scale; the outcome history that calibrates the PDs |
| **A held-universe default rate.** FTDs among all issuers held by the tracked funds (about 200, all known from the holdings), plus market events ≥ NOK 500m. Labelled as a replica and reconciled with NT in Feb 2027 | A running rate that is complete on a defined universe, instead of `[?]` on the whole market |
| **A monthly tracking row** in the market file: month, Stamdata pages and window read, distress notices, new FTDs (number and NOKm), pending cases, and the LTM pace with and without the pending cases | The signpost (> 10 notices a month) and the trigger as a time series; scan gaps become visible |
| **A log column: "visible at 1 Jan?"** (priced < 90 or on the list) | Tests the 2027 residual of 0 (gap 2) |
| **H1 2026 back-fill, once:** Stamdata news pages for Jan–Jul (~31 pages at about one week a page), read by hand like the current routine. First check whether the news feed can be filtered by tag, which would cut this to a few pages | Closes the H1 gap, so the running rate has a full year by the Feb 2027 NT report |
| **Price refresh order:** Sissener 30 Jun report → Heimdal contributions → ISIN price pages for the non-Nordic names | Cuts the stale or assumed share in gap 3 |

## 4. Notes on the skill (`hy-market-bbb`)

- **Size:** 1,219 lines and 95 KB. The source quirks (~170 lines, Data sources → Quirks) are
  operating notes, not method. Moving them to `references/sources-and-quirks.md` would make the
  method readable. The skill currently says "no reference files", so this is a method choice for
  the user.
- **Bucket rules:** unify Step 5 (a)–(d), the "Watchlist" definition and F9 into one scale. Spell
  out F9 as "Base PD = (bucket value + market-implied PD) ÷ 2"; the current wording ("midpoint of
  the bucket value and the market-implied PD") reads two ways. Use the bond's own recovery in the
  implied PD. Write any Bear override into the table with its reason.
- **2027 residual:** replace the hard 0 with a value tested on the log (gap 2), or at least add
  it as a stated sensitivity in every verdict.
- **Fund output template:** add the Summary and "How to read this" sections, the split comparison
  tables and a capped change log (R1–R5).
- **Checks before finishing:** add two checks. A partial update must label the tables it did not
  rerun (C5). The fund, issuer and market files must carry the same skill revision, baseline date
  and scan window (C1–C3, C9, C10).

## 5. Proposed changes

**Status 18 Oct:** items 1–4 applied (user: "Apply review items 1–4"); item 5 not started. Two
results differ from the estimates above:
- Applying the PD rule consistently raises the named 2027 loss by 0.11 (Sissener), 0.14
  (Høyrente N) and 0.19 pp (Pluss). That is more than the ≤ 0.1 pp per finding estimated in gap 4,
  because the findings add up. It is still below the minimum change; E / R moves ≤ 0.004.
- With the current PDs, the stale or assumed share of the named loss is 75% (Sissener), 63% (HH)
  and 69% (HH+).

Moving the source quirks to a reference file (section 4) was left alone; that is the user's
choice.

1. **Fund report:** restructure as in section 1 and fix C1–C8, C11 and C12. No figure changes.
2. **Issuer file:** make it the master watchlist (section 3), add the 17 Oct scan results and C13,
   and recompute the PDs where the bucket rules were applied inconsistently. The changes are
   ≤ 0.1 pp, so no fund rerun is needed.
3. **Market file:** add the monthly tracking row, the held-universe FTD and the "visible at 1 Jan"
   column, and fix C7, C10 and C14.
4. **Skill:** the rule and template changes in section 4, with the revision bumped.
5. **Data work:** the H1 back-fill and the price refreshes. These are separate runs that need the
   in-app browser.
