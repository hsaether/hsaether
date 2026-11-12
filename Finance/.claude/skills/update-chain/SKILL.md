---
name: update-chain
description: Update Chain — the orchestrator that keeps every document in docs/ current and updates them in the right order. Reads the update register (docs/update-register.md) and runs the check script, which lists what is stale, which documents were built on an input that has changed since, which planned events (rate decisions, OPEC+, quarterly reports, tenders) have passed or are coming up, and which skills have a newer revision. On the user's go-ahead it updates one document at a time in dependency order (oil → shipping / rig → supply → HY → equity → AI → defense → company analyses → funds → portfolio), each by its own skill in a fresh subagent. A change gate stops the cascade when an update keeps its values unchanged. It also takes unplanned news (a link, a company announcement) and finds every document it touches. Runs on a schedule: a weekly update run (Saturday) and a daily company news search (weekdays), both reported in docs/weekly-update.md. It makes no forecast and changes no method itself. ALWAYS use when the user asks what needs updating, what is stale, to run or check the update chain, to "update everything" / "oppdater alt" / "kjør oppdateringene", to update in the right order, or pastes news and asks what it affects across the documents — even without naming the skill.
---

# Update Chain

**Revision:** 2026-11-12.2 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/update-chain/` in the Finance folder.

The update chain keeps the documents in `docs/` current and in step with each other. It
decides **what** to update and **in which order**. Each document is still updated by its own
skill (`oil-market-bbb`, `iaf-valuation`, …), so this skill makes no forecast, sets no path,
and never changes another skill's method.

## Files

| File | Role |
|---|---|
| `docs/update-register.md` | The bookkeeping. **Documents**: id, file, skill, type, as of, last change, stale after, revision used. **Inputs**: which document reads which, and the version it read (`main` or `loop`). **Events**: planned events with the documents they affect |
| `references/update_check.py` | The check. Reads the register and the `**Revision:**` line in each skill. Never guesses a date from a document's text. `lint` also flags documents over the size budget (CLAUDE.md) |
| `docs/archive/register-log.md` | The register's change log (moved out of the register on 12 Nov 2026 to keep the register lean). New entries go at the end |
| `docs/weekly-update.md` | The run reports. Keep the last 14 days; move older entries to `docs/archive/weekly-update-YYYY-MM.md` at the weekly run |

Commands (run from the Finance folder; `py`, not `python`):

```bash
py .claude/skills/update-chain/references/update_check.py
```

```bash
py .claude/skills/update-chain/references/update_check.py record <id> --as-of YYYY-MM-DD --changed yes|no --affects id1,id2|none --stale-after YYYY-MM-DD
```

```bash
py .claude/skills/update-chain/references/update_check.py event-done "<event text>"
```

```bash
py .claude/skills/update-chain/references/update_check.py lint
```

- `lint` checks the register's structure (broken or merged rows, duplicates, bad values). It
  also compares the register's links with each document's own header. It prints hints to judge,
  not errors. The **Not links** table in the register holds the references judged not to be
  inputs.
- `status` (the default) also takes `--today YYYY-MM-DD`, `--days N` (event horizon,
  default 14) and `--defer-days N` (deferral window, default 14).
- `record` also takes `--rev REV` (defaults to the skill's current revision) and
  `--skip-inputs id1,id2` (inputs the run did not read). With `--changed yes`, `--affects` is
  required by this skill (the script falls back to `all` with a warning).

## Trigger rule (2026-11-07)

Every update costs a full skill run, so an upstream change triggers a downstream update only
when it matters there. Three gates, applied in this order:

1. **Hold.** A Documents note that starts `HOLD (user` keeps the document out of every run
   list, whatever the causes, until the date the note names or until the user lifts it. Holds
   come from the user only. When a dated hold has passed, the check says so; remove the prefix.
2. **Materiality, judged once at the source.** When a run records `--changed yes`, it names in
   `--affects` only the downstream documents for which a value they read (the Inputs "reads
   what") moved materially:
   - a path, scenario or mid-cycle value they read moved by more than the upstream skill's
     recalibration trigger;
   - a reference or hurdle they test against moved: the HY market reference E / R, a NIBOR path
     point by 0.25 pp or more, the NOK scenario path's relative moves, an exit reference;
   - or the move would shift their Base IRR by about 1 pp or more, or could flip their verdict
     (margin of safety within ±5%, or on a band line). Mark these `id!` (urgent).

   Never material: a re-mark of the upstream's own price or index level, a stub re-mark, a
   consensus refresh, a changed verdict of the upstream itself, or text and signposts. A
   price-only re-mark records `--affects none`. Use `all` only after a full re-baseline that
   moved Base paths broadly. The rest of the downstream documents see the change under "no
   action" and read it at their own next update. Documents named by an earlier change that have
   not read it yet stay named (the script keeps them).
3. **Deferral.** A document flagged only by upstream changes is not run now when its own update
   is planned within 14 days (an open event of its own, such as its report, or its stale-after
   date). It reads the change then. Urgent flags (`id!`) are not deferred.

Own causes (a passed report or event, the stale-after date) are not touched by gates 2 and 3.

## What the check reports

1. **Update now, in order.** The causes:
   - the document is past its stale-after date;
   - a `main` input has a *last change* newer than the version the document read, **and** that
     change names this document in its `affects` (the trigger rule), and the flag is not
     deferred;
   - a planned event that affects it has passed and is still `open`. A `watch` event (a data
     release or decision where no change is expected) never flags an update on its own; read it
     at the document's next run, and change it to `open` if it surprised.

   The order is a topological sort of the `main` inputs: upstream first, then by type (market →
   book → company → fund → portfolio).
   - **1a. Deferred:** flagged only by upstream changes, with its own update due within the
     deferral window. Not run now.
   - **1b. On hold:** held by the user. Never run, whatever the causes; the check counts the
     causes waiting.
2. **Re-check after an upstream update.** Documents downstream of an item in list 1. They need
   work only if that update moves values they read.
3. **Loop checks.** A back-reference changed (Equity BBB reads the AI baseline and company
   blocks; the AI baseline reads company analyses as a check). These are checked once, at the
   end, and never restart the chain.
4. **No action.** An upstream was re-run but kept unchanged, or changed in values that are not
   material for this document (not in its `affects`). Mention it in the header at the
   document's next run.
5. **Events in the next N days.**
6. **Method changed.** The skill has a newer revision than the one the document was built
   under.
7. **Companies with no open report date** in the register.
- **Register warnings:** unknown ids, files missing from the register, missing dates.

## Mode A — status (default)

1. Run the check. Start by stating the revision of this skill.
2. Show the user the result in a short table:
   - list 1 in order, with the cause per item;
   - list 2 grouped under its upstream;
   - the events of the next 14 days;
   - a single line each for lists 3, 4 and 6.
3. Leave lists 1a (deferred) and 1b (on hold) out of the run proposal; one line each.
4. Say which items are worth running now. Rule of thumb:
   - a passed event or a changed `main` input outranks a stale date alone;
   - a market baseline outranks the companies below it.

   Then **wait for the go-ahead**. Never start updates unasked; each one is a full skill run.

## Mode B — run the updates

Work through list 1 **one document at a time, in the script's order**. For each document:

1. **Brief a fresh subagent** (Agent tool, `subagent_type: "general-purpose"`, `model: "opus"`;
   use `model: "fable"` when the user asks for it). One document per subagent keeps each run in a
   clean context. A full chain in one context is what causes slips. **Effort by job:**
   - `effort: "xhigh"` for a full re-baseline of a market document, a company after a passed
     report, or an upstream change that the upstream's "for downstream" section says touches rows
     this document reads;
   - `effort: "high"` for a re-mark (price, FX, stub), a small update on news, a method-only
     re-run, or an upstream change its "for downstream" section calls "no change";
   - when in doubt, `xhigh`.

   The brief gives:
   - the document id and file, and the skill to invoke by name;
   - the causes from the check, word for word;
   - for each changed upstream: its file, the date of the version read, the date of its last
     change, and the instruction to read that upstream's **Interface section** (or, until it has
     one, its "for downstream" section) and its latest change-log entry, going deeper only for a
     value it needs. Never "read the whole document";
   - the lean-document rules in CLAUDE.md: current state only, change log of the last 3 versions,
     the size budget, and compacting the document at this run if it is over budget;
   - for each passed event: what it is, and that the subagent must find its outcome;
   - the **change gate**: first decide whether the change touches values this document reads. If
     it does not, follow the skill's own minimum-change rule: write a short dated note in the
     metadata ("kept unchanged; read X of date D") and change nothing else;
   - the workspace rules in CLAUDE.md: write to the file, read it back, state the skill revisions;
     the subagent never uses git (the orchestrating session commits);
   - what to return:
     - `changed: yes|no`: did a value other documents read move (path, scenario, mid-cycle,
       stub, verdict, decision figure)?
     - `affects`: the downstream documents (from the Inputs table, the rows that read this one)
       for which a value they read moved materially, by the trigger rule's tests; `id!` where
       their verdict could flip; `none` for a price-only re-mark. One reason per name;
     - one line on what moved;
     - the new stale-after date;
     - every new dated event found (next report date, decision date) with the documents it
       affects;
     - any input it could not get.
2. **Check the result yourself.** Read the document's metadata and conclusion; do not take the
   subagent's report on trust. If the document was not written, or the conclusion does not match
   the report, stop the chain and tell the user.
3. **Record:**
   - run `record <id> --as-of <run date> --changed yes|no --affects <ids|none> --stale-after
     <date>`. Check the subagent's `affects` against the trigger rule before you record it:
     trim names whose read values did not move materially;
   - run `event-done` for each passed event the run dealt with;
   - add the new events the subagent returned to the Events table, so that every company ends up
     with its next report date;
   - **commit** the files the run changed, by path (the document, the register, the register log,
     any changed skill or script), with the message and attribution line CLAUDE.md gives. Before
     briefing a run that will rewrite or compact a document with uncommitted changes, commit it.
4. **Re-run the check** before the next item. A `changed: yes` adds to list 1 only the
   downstream documents named in `affects` that are not deferred or on hold. A `changed: no`
   leaves them all alone. This is how the cascade stops.

After list 1 is empty:

- **Loop checks:** run each item in list 3 once, through the same steps. If it comes back
  `changed: no`, record it and stop. Never loop a second time in the same run.
- **Finish with a report:** a table of the documents updated (changed or kept), what moved, what
  is left and why, and the next events.

**Parallel runs:** documents at the same point in the order that do not read each other may run
in parallel, two subagents at most (four in parallel hit the session limit on 24 Oct; one run
costs 250–400k tokens). In practice that means company analyses under the same,
already-updated baseline. Market baselines always run one at a time.

**Stop and ask** when:

- a subagent fails or lacks a key input;
- an update moves a Base path by more than its skill's recalibration trigger (the user should
  see that before the cascade runs);
- the next item needs a logged-in source. `portfolio` reads Nordnet through Edge with approval
  per connection, so it never runs unattended.

## Mode C — news and other unplanned input

The user pastes a link, an announcement or a number.

1. Assess it critically, as CLAUDE.md requires: is it new, is it material, is it a fact `[F]` or
   a claim?
2. Find the documents it touches:
   - **company news** → that company's analysis;
   - **sector or macro news** → the baseline that owns that variable (CLAUDE.md "set only in");
     never a downstream document directly.

   Use the Inputs table ("reads what") to see who else reads that variable.
3. **Company news or a company report: update that company's analysis at once,** without waiting
   for a go-ahead or for Saturday (user rule, 29 Oct 2026), then its downstream documents as the
   change gate flags them. Sector or macro news: show the user the affected documents and the
   order, then run Mode B from the highest affected document. The change gate decides how far
   the cascade goes. A casually shared item that turns out immaterial gets a one-line verdict and
   no update.
4. If the news carries a date (a decision date, a report date, a tender deadline), add it to the
   Events table.

## Mode D — keeping the register right

Keeping the register right is part of delivering any document: the chat that writes or retires a
document does this, without being asked (CLAUDE.md), and says in its answer what it changed in
the register.

**New document — all seven steps:**

1. **Documents row:**
   - a short, unique id;
   - type: `market`, `book`, `company` or `fund`;
   - "as of" and "last change": the build date;
   - stale after: from the header, else 30 days after "as of";
   - the skill revision used.
2. **Its inputs:** one Inputs row per document its header says it read. "input as of" is the
   date of the version read, as the header states it. The link is `main`, unless that upstream
   itself reads the new document as `main` (then use `loop`, to break the cycle).
3. **Who reads it (downstream).** The lint cannot find these, so search for them:
   - search all of `docs/` for the company's name and ticker;
   - every document that uses the company gets a row "document ← new id". That covers a fund
     that holds it, an index or fund block, a peer comparison, and a baseline's layer or company
     check;
   - the link is `main` when the new analysis will feed that document's figures (a holding, a
     block), and `loop` when it is a check (peer, layer check);
   - "input as of" is that document's current "as of", and "reads what" ends with "not yet
     read". The check then flags it.
   - Not linked: documents that only mention the name (for example, an emerging-market name
     outside MSCI World is not linked to World).
4. **Events:**
   - the next report date and other dated events;
   - add the new id to existing events that affect it: peers' reports, the main customer's
     report.
5. **Edit by whole lines.** Insert or replace complete table rows; never delete by joining lines.
   For an existing document, use `record`.
6. **Lint:** run `update_check.py lint`.
   - Part A (structure) must say "none".
   - Judge every hint in B and C: either add the Inputs row, or add a row to the **Not links**
     table with the reason.
7. **Check and log:** run the check, add a dated change-log entry to `docs/archive/register-log.md`, and read it
   back.

**Retired document** (the user stops tracking it):

- set its type to `static` and write the reason in its note;
- remove its own Inputs rows;
- mark its open events `dropped`;
- keep the file if other documents cite it, and add a "no longer tracked" note at its top.

**New skill or baseline:** add it to CLAUDE.md (layout and chain), then to the register as
above.

**A back-reference that creates a cycle:** the script stops with an error. Mark the reference
that is a check, not a driver, as `loop` (CLAUDE.md's chain gives the direction).

After any hand edit: run `lint` and the check, and read the register back.

## Rules

- The register is bookkeeping only. Numbers, paths and verdicts live in the documents. When a
  header and the register disagree, the header wins: fix the register.
- *Last change* moves only when a value other documents read moved. A run that keeps everything
  unchanged updates only *as of*. *Affects* names only the downstream documents for which that
  move is material (trigger rule).
- A newer skill revision alone (list 6) does not trigger a re-run. Mention it. The method is
  applied at the document's next run, or when the user asks.
- Upstream before downstream, always. Never update a document while a `main` input of it is in
  list 1.
- Git: the orchestrating session commits each run (CLAUDE.md); subagents never use git; never
  push or rewrite history.

## Mode E — weekly run (scheduled, Saturday 09:00)

Started by the scheduled task `weekly-update-chain`. The user agreed (24 Oct 2026) that this run
updates documents without waiting for a go-ahead, within the limits below. It runs unattended, so
it never asks; anything that needs the user goes into the report under **Needs you**.

1. **Check.** State this skill's revision. Run the check with `--today` set to the run date.
2. **Start the report** at the top of `docs/weekly-update.md` (newest week first): the check
   result in short form. Write the report as you go, so a run stopped by the usage limit still
   leaves a report and a consistent register.
3. **News sweep for the week** (since the previous weekly entry). For companies, start from the
   week's daily entries (Mode F) and search only the days they did not cover. Use web search and
   the market-data connectors. **Never Edge**, so no Nordnet and no Newsweb through Edge:
   - **politics and macro:** the Gulf and Middle East, US politics and trade, Ukraine and
     European defense, OPEC+, Norges Bank, the Riksbank, the Fed and the ECB;
   - **sectors:** tankers, rigs, OSVs, Nordic HY defaults and restructurings, defense orders, AI
     capex and the labs;
   - **companies:** every `company` and `fund` row in the register: reports, guidance, contracts,
     capital moves.

   Treat each item as in Mode C: assess it, map it to the document that owns the variable, and
   add any dated event to the Events table. For every `watch` event that passed this week, find
   the outcome. If it surprised against the stated expectation, change it to `open` (so the check
   flags its documents); otherwise mark it `done` and give the outcome in the report.
4. **Run list,** in the check's order, from list 1 only (never 1a deferred or 1b on hold),
   **at most 6 documents**. Priority:
   1. market baselines with a passed event, a changed `main` input, or material news;
   2. companies with a passed report or material news;
   3. other changed-input items;
   4. stale-date-only items.

   Whatever does not fit goes into the report under **Left for next run**.
5. **Run them as in Mode B** (effort by job, two in parallel at most, market baselines one at a
   time), and record and commit each one as soon as it is checked. Three unattended rules:
   - If an update moves a Base path by more than its skill's recalibration trigger, record it, do
     **not** run its downstream documents, and put it under **Needs you**.
   - A subagent that fails or lacks a key input: record nothing for it, and put it under
     **Needs you**.
   - Never run `portfolio` (Nordnet through Edge).
6. **Finish the report entry:**
   - **Summary:** verdicts and Base paths that moved, in a few lines.
   - **Updated:** a table of document, changed or kept, what moved, stale after.
   - **News that mattered**, with the document it went to.
   - **Needs you**, and **Left for next run**.
   - **Events in the next 14 days.**

   Read the file back.

## Mode F — daily company news and updates (scheduled, weekdays 08:00)

Started by the scheduled task `daily-company-news`. **A company that reported or has material
news is updated in this run, not on Saturday** (user rule, 29 Oct 2026: "When a company reports
results, or has news that might impact analysis, it needs to be updated immediately"). The
08:00 slot catches the previous evening's US reports (with the call transcript out) and the
Oslo and Asian morning reports. It runs unattended, so it never asks; the Mode E unattended
rules apply.

1. **Window:** since the previous daily entry in `docs/weekly-update.md`. On Monday that covers
   the weekend.
2. **Who:**
   - every `company` and `fund` row in the register (not `static`);
   - the issuers on the HY master watchlist (`docs/hy-issuers.md`) that a tracked fund holds.
3. **What:** use web search and the market-data connectors; **never Edge**, so no Nordnet and no
   Newsweb through Edge. Look for:
   - stock-exchange releases, reports and guidance, profit warnings;
   - contracts won or lost, accidents and incidents, management changes;
   - capital moves: issues, buybacks, dividends, refinancing, bondholder notices, covenant
     waivers, defaults;
   - rating actions, and large price moves with a named cause.

   **Fund managers' forum posts (public, no login; read with WebFetch, not Edge).** The Nordnet
   fund pages show the Nordnet Social forum, where the managers answer questions (e.g. Heimdal
   Erik, Heimdal Martin): bond marks, trades, yields, contributions. Read the posts since the
   previous daily entry on:
   - Heimdal Høyrente N: https://www.nordnet.no/fond/liste/heimdal-hoyrente-n-nok-6e890321
   - Heimdal Høyrente Pluss B: https://www.nordnet.no/fond/liste/heimdal-hoyrente-pluss-b-nok-4c49fed8
   - Sissener Corporate Bond R: https://www.nordnet.no/fond/liste/sissener-corporate-bond-r-nok-bdb89592
     (SissenerFredrik = Fredrik Galtung, IR at Sissener: monthly figures, duration, holdings answers)
   - Fondsfinans High Yield B: https://www.nordnet.no/fond/liste/fondsfinans-high-yield-b-nok-8bfcfdd4
   - Fondsfinans Kreditt B: https://www.nordnet.no/fond/liste/fondsfinans-kreditt-b-nok-7e0cbe6d
     (Eotnes = Eyvind Otnes, communications at Fondsfinans, not a manager: mostly links to the monthly
     manager commentary and return figures; follow the link only when it is new)

   Use only posts by these fund-house people, tagged `[E]` (fund-house statement); other users' posts are
   context at most. A stated bond mark, trade, yield or contribution goes to `hy-issuers` /
   `hy-funds` as an item (and a same-day event if material); general market talk is left out.
4. **Assess each item as in Mode C:** is it new, is it material, is it a fact `[F]` or a claim
   `[E]`? Map it to the document that owns it: the company's analysis, the watchlist for a bond
   issuer, or a sector baseline for an industry-wide fact.
5. **Register:** add every new dated event (report dates, decision dates, deadlines) to the
   Events table. Add a same-day event for material news, so the check flags the document.
6. **Update at once.** Run the check (`--today` = run date). Then run Mode B for:
   1. every `company` document whose own report event has passed, or that has material news in
      this window (a report is always material);
   2. a `fund` document only when the news is about the fund itself;
   3. with room left, the downstream `company` and `fund` documents a `changed: yes` above flags
      (the cascade: only those named in its `affects`, not deferred), in the check's order.

   Never a document on hold (list 1b) or deferred (list 1a).

   **At most 6 documents per run,** two subagents in parallel, effort by job (a passed report is
   `xhigh`). Overflow goes under **Left for next run** and is first in line at the next daily
   run. The company update runs on the current baselines: market baselines are not re-run here
   (they follow Mode E or the user), and when a baseline later changes, the change gate re-runs
   the company. Before running a US report, check that the call transcript or a call summary is
   out; if not, run on the release and add a same-day "call re-check" event. Never `portfolio`;
   never Edge. Record and commit each document as soon as it is checked.
7. **Write a short entry at the top of `docs/weekly-update.md`,** headed "Daily news — <weekday>
   <date>". **It must be short: at most 12 lines and about 150 words.** The user reads it in the
   morning; the details belong in the documents, not here.
   - **Updated:** one line per document updated: id, Base IRR before → after, verdict (and
     "flipped" when it did). This counts toward the line limit.
   - **Material items, at most 6 bullets,** one line each (about 25 words): the company, the
     document id in brackets, what happened, and the tag `[F]` or `[E]`. No source lists, no
     tables, no prices beyond the one number that matters. An item already in **Updated** gets
     no second bullet.
   - **Minor items: at most one line in total**, names and a word or two each. Leave out what
     changes nothing.
   - **Needs you:** one line, only when something needs the user. Examples: a verdict that
     flipped, a default or bondholder notice, a subagent that failed, overflow left for the next
     run.
   - **Register:** one line naming the events added.
   - "No material company news" when there is none, and nothing else.
   - Never include method, sources searched, the search window, "nothing found for" lists or
     coverage notes. A coverage gap goes in only when it hides a held name, in one short line.

   Read the file back.

Saturday's run (Mode E, step 3) starts from these daily entries instead of searching the whole
week again.

## Change log

- **2026-11-12.2:** commits are part of the run (user): the orchestrating session commits each recorded run by path;
  subagents never use git.
- **2026-11-12.1:** lean documents (user): briefs read the upstream Interface section, not whole files; the register change
  log moves to docs/archive/register-log.md; weekly-update keeps 14 days; lint flags documents over budget. Older change-log
  entries removed (git keeps them).
- **2026-11-09.1:** script fix only: documents on hold no longer appear in list 2 (re-check).
