---
name: update-chain
description: Update Chain — the orchestrator that keeps every document in docs/ current and updates them in the right order. Reads the update register (docs/update-register.md) and runs the check script, which lists what is stale, which documents were built on an input that has changed since, which planned events (rate decisions, OPEC+, quarterly reports, tenders) have passed or are coming up, and which skills have a newer revision. On the user's go-ahead it updates one document at a time in dependency order (oil → shipping / rig → supply → HY → equity → AI → defense → company analyses → funds → portfolio), each by its own skill in a fresh subagent. A change gate stops the cascade when an update keeps its values unchanged. It also takes unplanned news (a link, a company announcement) and finds every document it touches. Runs on a schedule: a weekly update run (Saturday) and a midweek check (Wednesday), both reported in docs/weekly-update.md. It makes no forecast and changes no method itself. ALWAYS use when the user asks what needs updating, what is stale, to run or check the update chain, to "update everything" / "oppdater alt" / "kjør oppdateringene", to update in the right order, or pastes news and asks what it affects across the documents — even without naming the skill.
---

# Update Chain

**Revision:** 2026-10-24.2 — bump on every change (date.counter). This file is the master and the
only copy; Claude Code loads it from `.claude/skills/update-chain/` in the Finance folder.

The update chain keeps the documents in `docs/` current and in step with each other. It
decides **what** to update and **in which order**. Each document is still updated by its own
skill (`oil-market-bbb`, `iaf-valuation`, …), so this skill makes no forecast, sets no path,
and never changes another skill's method.

## Files

| File | Role |
|---|---|
| `docs/update-register.md` | The bookkeeping. **Documents**: id, file, skill, type, as of, last change, stale after, revision used. **Inputs**: which document reads which, and the version it read (`main` or `loop`). **Events**: planned events with the documents they affect |
| `references/update_check.py` | The check. Reads the register and the `**Revision:**` line in each skill. Never guesses a date from a document's text |

Commands (run from the Finance folder; `py`, not `python`):

```bash
py .claude/skills/update-chain/references/update_check.py
```

```bash
py .claude/skills/update-chain/references/update_check.py record <id> --as-of YYYY-MM-DD --changed yes|no --stale-after YYYY-MM-DD
```

```bash
py .claude/skills/update-chain/references/update_check.py event-done "<event text>"
```

- `status` (the default) also takes `--today YYYY-MM-DD` and `--days N` (event horizon,
  default 14).
- `record` also takes `--rev REV` (defaults to the skill's current revision) and
  `--skip-inputs id1,id2` (inputs the run did not read).

## What the check reports

1. **Update now, in order.** The causes:
   - the document is past its stale-after date;
   - a `main` input has a *last change* newer than the version the document read;
   - a planned event that affects it has passed and is still `open`.

   The order is a topological sort of the `main` inputs: upstream first, then by type (market →
   book → company → fund → portfolio).
2. **Re-check after an upstream update.** Documents downstream of an item in list 1. They need
   work only if that update moves values they read.
3. **Loop checks.** A back-reference changed (Equity BBB reads the AI baseline and company
   blocks; the AI baseline reads company analyses as a check). These are checked once, at the
   end, and never restart the chain.
4. **No action.** An upstream was re-run but kept unchanged. Mention it in the header at the
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
3. Say which items are worth running now. Rule of thumb:
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
     change, and the instruction to read that upstream's conclusion, its "for downstream" section
     and its change-log entries since the read date;
   - for each passed event: what it is, and that the subagent must find its outcome;
   - the **change gate**: first decide whether the change touches values this document reads. If
     it does not, follow the skill's own minimum-change rule: write a short dated note in the
     metadata ("kept unchanged; read X of date D") and change nothing else;
   - the workspace rules in CLAUDE.md: write to the file, read it back, state the skill revisions,
     never use git;
   - what to return:
     - `changed: yes|no`: did a value other documents read move (path, scenario, mid-cycle,
       stub, verdict, decision figure)?
     - one line on what moved;
     - the new stale-after date;
     - every new dated event found (next report date, decision date) with the documents it
       affects;
     - any input it could not get.
2. **Check the result yourself.** Read the document's metadata and conclusion; do not take the
   subagent's report on trust. If the document was not written, or the conclusion does not match
   the report, stop the chain and tell the user.
3. **Record:**
   - run `record <id> --as-of <run date> --changed yes|no --stale-after <date>`;
   - run `event-done` for each passed event the run dealt with;
   - add the new events the subagent returned to the Events table, so that every company ends up
     with its next report date.
4. **Re-run the check** before the next item. A `changed: yes` adds downstream documents to
   list 1. A `changed: no` leaves them alone. This is how the cascade stops.

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
3. Show the user the affected documents and the order, then run Mode B from the highest affected
   document. The change gate decides how far the cascade goes.
4. If the news carries a date (a decision date, a report date, a tender deadline), add it to the
   Events table.

## Mode D — keeping the register right

- **New document:**
  - add a Documents row, with type, stale-after (company and fund: 30 days after "as of" unless
    its header says otherwise) and revision;
  - add one Inputs row per upstream it reads, with the date of the version read;
  - add its next report date to Events.
- **New skill or baseline:** add it to CLAUDE.md (layout and chain), then to the register.
- **A back-reference that creates a cycle:** the script stops with an error. Mark the reference
  that is a check, not a driver, as `loop` (CLAUDE.md's chain gives the direction).
- **Retired document:** set its type to `static`.
- After any hand edit, run the check and read the register back.

## Rules

- The register is bookkeeping only. Numbers, paths and verdicts live in the documents. When a
  header and the register disagree, the header wins: fix the register.
- *Last change* moves only when a value other documents read moved. A run that keeps everything
  unchanged updates only *as of*.
- A newer skill revision alone (list 6) does not trigger a re-run. Mention it. The method is
  applied at the document's next run, or when the user asks.
- Upstream before downstream, always. Never update a document while a `main` input of it is in
  list 1.
- No git, as everywhere in this folder.

## Mode E — weekly run (scheduled, Saturday 09:00)

Started by the scheduled task `weekly-update-chain`. The user agreed (24 Oct 2026) that this run
updates documents without waiting for a go-ahead, within the limits below. It runs unattended, so
it never asks; anything that needs the user goes into the report under **Needs you**.

1. **Check.** State this skill's revision. Run the check with `--today` set to the run date.
2. **Start the report** at the top of `docs/weekly-update.md` (newest week first): the check
   result in short form. Write the report as you go, so a run stopped by the usage limit still
   leaves a report and a consistent register.
3. **News sweep for the week** (since the previous weekly entry), using web search and the
   market-data connectors. **Never Edge**, so no Nordnet and no Newsweb through Edge:
   - **politics and macro:** the Gulf and Middle East, US politics and trade, Ukraine and
     European defense, OPEC+, Norges Bank, the Riksbank, the Fed and the ECB;
   - **sectors:** tankers, rigs, OSVs, Nordic HY defaults and restructurings, defense orders, AI
     capex and the labs;
   - **companies:** every `company` and `fund` row in the register: reports, guidance, contracts,
     capital moves.

   Treat each item as in Mode C: assess it, map it to the document that owns the variable, and
   add any dated event to the Events table.
4. **Run list,** in the check's order, **at most 6 documents**. Priority:
   1. market baselines with a passed event, a changed `main` input, or material news;
   2. companies with a passed report or material news;
   3. other changed-input items;
   4. stale-date-only items.

   Whatever does not fit goes into the report under **Left for next run**.
5. **Run them as in Mode B** (effort by job, two in parallel at most, market baselines one at a
   time), and record each one as soon as it is checked. Three unattended rules:
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

## Mode F — midweek check (scheduled, Wednesday 09:00)

Started by the scheduled task `midweek-update-check`, during the report season. **No updates.**

- Run steps 1 and 3 of Mode E: the check, and the news sweep since the last entry.
- Add the dated events to the register.
- Write a short **Midweek check** entry at the top of `docs/weekly-update.md`:
  - what the check flags;
  - the news that matters;
  - which documents are worth starting before Saturday, and why.

  Read the file back.

## Change log

- **2026-10-24.2:**
  - Mode E (weekly run, Saturday) and Mode F (midweek check, Wednesday), per the user's choices.
  - Effort by job (xhigh or high).
  - Parallel runs cut to two after the 24 Oct run hit the session limit.
- **2026-10-24.1:** initial version. Register first filled from the document headers of
  24 Oct 2026.
