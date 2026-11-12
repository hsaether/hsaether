"""Update-chain check: reads docs/update-register.md and the skill revisions, and lists
what needs updating, in dependency order.

Usage (from the Finance folder or anywhere; paths are resolved from this file):
  py update_check.py [status] [--today YYYY-MM-DD] [--days 14] [--defer-days 14]
  py update_check.py record <id> --as-of YYYY-MM-DD --changed yes|no
                     [--affects id1,id2|all|none] [--stale-after YYYY-MM-DD] [--rev REV]
                     [--skip-inputs id1,id2]
  py update_check.py event-done "<text that matches one open event>"

status      : the check. Prints nothing to disk.
record      : after a document is updated. Sets its "as of" (and "last change" when values
              that downstream documents read moved), stale-after and revision, and marks
              every input it reads as read at the upstream's current "as of".
              With --changed yes, --affects is required: the downstream documents for which a
              value they read moved materially (the trigger rule in SKILL.md). Only those are
              flagged; the others see the change under "no action". Documents named by an
              earlier change that have not read it yet are kept in the list.
event-done  : marks one event in the Events table as done.

Trigger rule in status (2026-11-07):
  - a note starting "HOLD (user" keeps a document out of list 1 (until the date in the note,
    or until the user lifts it);
  - an upstream change flags a downstream document only if the upstream's "affects" names it
    (or is "all");
  - a flag that comes only from upstream changes is deferred when the document has its own
    update planned within --defer-days (an open event of its own, or its stale-after date):
    the change is read then.

Standard library only. The register is the single source of the bookkeeping; this script
never guesses a date from a document's text.
"""
import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]          # .../Finance
REGISTER = ROOT / "docs" / "update-register.md"
SKILLS = ROOT / ".claude" / "skills"

TYPE_RANK = {"market": 0, "book": 1, "company": 2, "fund": 3, "portfolio": 4}
SIZE_BUDGET = {"market": 800, "book": 800, "company": 450, "fund": 450}   # lines; CLAUDE.md

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


# ---------- register parsing ----------

def clean(cell):
    return cell.strip().replace("**", "").replace("`", "").strip()


def parse_date(s):
    s = clean(s)
    if not s or s in ("-", "—", "?"):
        return None
    return dt.date.fromisoformat(s)


def read_tables(lines):
    """Return {section heading: (header list, [(line index, cells)])} for the first table
    under each '## ' heading."""
    tables, section, i = {}, None, 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            section = line[3:].strip()
        elif line.lstrip().startswith("|") and section and section not in tables:
            header = [clean(c).lower() for c in line.strip().strip("|").split("|")]
            rows, i = [], i + 2                      # skip the separator row
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = [clean(c) for c in lines[i].strip().strip("|").split("|")]
                row = dict(zip(header, cells))
                row["_n"] = len(cells)
                rows.append((i, row))
                i += 1
            tables[section] = (header, rows)
            continue
        i += 1
    return tables


def load():
    lines = REGISTER.read_text(encoding="utf-8").splitlines()
    t = read_tables(lines)
    for need in ("Documents", "Inputs", "Events"):
        if need not in t:
            sys.exit(f"Register has no '## {need}' table: {REGISTER}")
    docs = {}
    for idx, r in t["Documents"][1]:
        r["_line"] = idx
        docs[r["id"]] = r
    return lines, t, docs


def save(lines):
    """Write the register back with the line endings it already has."""
    eol = "\r\n" if b"\r\n" in REGISTER.read_bytes() else "\n"
    with open(REGISTER, "w", encoding="utf-8", newline="") as f:
        f.write(eol.join(lines) + eol)


def write_row(lines, idx, header, row):
    lines[idx] = "| " + " | ".join(row.get(h, "") for h in header) + " |"


def skill_revisions():
    revs = {}
    for f in SKILLS.glob("*/SKILL.md"):
        m = re.search(r"\*\*Revision:\*\*\s*([0-9]{4}-[0-9]{2}-[0-9]{2}\.[0-9]+)",
                      f.read_text(encoding="utf-8"))
        if m:
            revs[f.parent.name] = m.group(1)
    return revs


def rev_key(r):
    d, n = r.split(".")
    return (d, int(n))


MONTHS = {m: n for n, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
HOLD_UNTIL = re.compile(r"until (?:[A-Za-z]{3} )?(\d{1,2}) ([A-Za-z]{3})[a-z]* (\d{4})")


def hold_of(d, today):
    """(on hold?, text) from a note that starts 'HOLD (user'. A hold with a date in the past
    has lapsed: (False, 'lapsed ...')."""
    note = d.get("note", "")
    if not note.startswith("HOLD (user"):
        return False, ""
    text = note.split(".")[0] + "."
    m = HOLD_UNTIL.search(text)
    if m:
        day, mon, year = int(m.group(1)), MONTHS.get(m.group(2).lower()[:3]), int(m.group(3))
        if mon and today > dt.date(year, mon, day):
            return False, f"hold lapsed {dt.date(year, mon, day)}: remove the HOLD prefix"
    return True, text


def affects_of(d):
    """The downstream ids an upstream's last change was recorded for: a set, or 'all'."""
    a = d.get("affects", "all").strip().lower()
    if a in ("", "all", "?"):
        return "all"
    if a in ("none", "-"):
        return set()
    return {x.strip().rstrip("!") for x in a.split(",") if x.strip()}


def urgent_of(d):
    """Downstream ids marked 'id!' in affects: the change may flip their verdict, so the flag
    is not deferred."""
    return {x.strip().rstrip("!") for x in d.get("affects", "").split(",")
            if x.strip().endswith("!")}


# ---------- order ----------

def topo_order(docs, edges):
    ids = [i for i, d in docs.items() if d["type"] != "static"]
    ups = {i: set() for i in ids}
    for e in edges:
        if e["link"] == "main" and e["document"] in ups and e["reads"] in ups:
            ups[e["document"]].add(e["reads"])
    order, done = [], set()
    while len(order) < len(ids):
        ready = [i for i in ids if i not in done and ups[i] <= done]
        if not ready:
            left = sorted(set(ids) - done)
            sys.exit("Cycle in the main inputs among: " + ", ".join(left)
                     + ". Mark the back-reference as 'loop' in the Inputs table.")
        ready.sort(key=lambda i: (TYPE_RANK.get(docs[i]["type"], 9), i))
        order.append(ready[0])
        done.add(ready[0])
    return order, ups


def downstream(ups, start):
    out, frontier = set(), {start}
    while frontier:
        nxt = {d for d, u in ups.items() if u & frontier} - out
        out |= nxt
        frontier = nxt
    return out


# ---------- register structure ----------

def structure_warnings(t, docs):
    """Errors in the register itself: broken or merged rows, duplicates, bad values."""
    warn = []
    for name in ("Documents", "Inputs", "Events"):
        header, rows = t[name]
        for idx, r in rows:
            if r["_n"] != len(header):
                warn.append(f"{name} line {idx + 1}: {r['_n']} cells, expected {len(header)} "
                            "(merged or broken row)")
    seen = {}
    for idx, r in t["Documents"][1]:
        if r["id"] in seen:
            warn.append(f"Documents: id '{r['id']}' twice (lines {seen[r['id']] + 1}, {idx + 1})")
        seen[r["id"]] = idx
        if r["type"] != "static" and r["type"] not in TYPE_RANK:
            warn.append(f"Documents: '{r['id']}' has unknown type '{r['type']}'")
        for col in ("as of", "last change", "stale after"):
            try:
                parse_date(r.get(col, ""))
            except ValueError:
                warn.append(f"Documents: '{r['id']}' has a bad date in '{col}': {r.get(col)}")
    pairs = {}
    for idx, e in t["Inputs"][1]:
        key = (e["document"], e["reads"])
        if key in pairs:
            warn.append(f"Inputs: {key[0]} <- {key[1]} twice (lines {pairs[key] + 1}, {idx + 1})")
        pairs[key] = idx
        if e["document"] == e["reads"]:
            warn.append(f"Inputs line {idx + 1}: '{e['document']}' reads itself")
        if e["link"] not in ("main", "loop"):
            warn.append(f"Inputs line {idx + 1}: link '{e['link']}' is not main or loop")
        for k in ("document", "reads"):
            d = docs.get(e[k])
            if d and d["type"] == "static":
                warn.append(f"Inputs line {idx + 1}: {e['document']} <- {e['reads']} involves "
                            f"static document '{e[k]}'")
        try:
            parse_date(e["input as of"])
        except ValueError:
            warn.append(f"Inputs line {idx + 1}: bad date '{e['input as of']}'")
    for idx, ev in t["Events"][1]:
        if ev["status"].lower() not in ("open", "watch", "done", "dropped"):
            warn.append(f"Events line {idx + 1}: status '{ev['status']}' is not "
                        "open/watch/done/dropped")
        if ev["firm"].lower() not in ("yes", "approx"):
            warn.append(f"Events line {idx + 1}: firm '{ev['firm']}' is not yes/approx")
        try:
            parse_date(ev["date"])
        except ValueError:
            warn.append(f"Events line {idx + 1}: bad date '{ev['date']}'")
    return warn


# ---------- lint: register links against the documents' own headers ----------

HEADER_END = ("## Summary", "## Conclusion", "## Header")
NOT_USED = re.compile(r"not used|not read|is not an input|are not used|no longer|"
                      r"used only through|neither reads", re.I)


def doc_names(path):
    """Names other documents use for a document: its H1 up to ' — ' or ' (', and the short
    form without 'Nordic ' and ' Market' ('Nordic HY Market BBB' -> 'HY BBB')."""
    try:
        first = path.read_text(encoding="utf-8").splitlines()[0]
    except (OSError, IndexError):
        return []
    name = first.lstrip("# ").split(" — ")[0].split(" (")[0].strip()
    if not name:
        return []
    short = name.replace("Nordic ", "").replace(" Market", "")
    return [name] + ([short] if short != name else [])


def lint():
    _, t, docs = load()
    edges = [r for _, r in t["Inputs"][1]]
    by_file = {d["file"]: i for i, d in docs.items()}
    have = {(e["document"], e["reads"]) for e in edges}
    have |= {(r["document"], r["names"]) for _, r in t.get("Not links", ([], []))[1]}
    missing, unnamed = [], []
    for i, d in docs.items():
        if d["type"] == "static":
            continue
        path = ROOT / d["file"]
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        head = []
        for n, line in enumerate(text.splitlines()):
            if n > 0 and line.startswith(HEADER_END):
                break
            head.append(line)
        for line in head:
            if NOT_USED.search(line):
                continue
            for m in re.finditer(r"docs/([A-Za-z0-9_.-]+\.md)", line):
                up = by_file.get(f"docs/{m.group(1)}")
                if up and up != i and docs[up]["type"] != "static" and (i, up) not in have:
                    missing.append(f"{i:<14} header names docs/{m.group(1)} ({up}); no Inputs row")
        low = text.lower()
        for e in edges:
            if e["document"] != i or e["reads"] not in docs:
                continue
            u = docs[e["reads"]]
            names = doc_names(ROOT / u["file"])
            if u["file"] in text or any(n.lower() in low for n in names):
                continue
            if "not yet read" in e.get("reads what", "").lower():
                continue
            unnamed.append(f"{i:<14} <- {e['reads']:<12} the document never names "
                           f"{u['file']} or " + " / ".join(f"'{n}'" for n in names))
    print("Lint: register links against the document headers")
    print()
    print("A. STRUCTURE (errors in the register itself)")
    sw = structure_warnings(t, docs)
    print("   none" if not sw else "\n".join(f"   ! {w}" for w in sw))
    print()
    print("B. POSSIBLY MISSING LINKS (a header names a document the register does not link)")
    print("   none" if not missing else "\n".join(f"   - {m}" for m in sorted(set(missing))))
    print()
    print("C. POSSIBLY STALE LINKS (the register links a document the text never names)")
    print("   none" if not unnamed else "\n".join(f"   - {u}" for u in unnamed))
    print()
    print("D. OVER THE SIZE BUDGET (CLAUDE.md lean documents; compact at the document's next run)")
    over = []
    for i, d in sorted(docs.items()):
        budget = SIZE_BUDGET.get(d["type"])
        path = ROOT / d["file"]
        if budget and path.exists():
            n = len(path.read_text(encoding="utf-8").splitlines())
            if n > budget:
                over.append(f"{i:<14} {n:>5} lines (budget {budget})")
    print("   none" if not over else "\n".join(f"   - {o}" for o in over))
    print()
    print("B, C and D are hints, not errors: judge each one. Downstream links (who should read a new")
    print("document) cannot be found this way; see Mode D in the skill.")


# ---------- status ----------

def status(today, days, defer_days=14):
    lines, t, docs = load()
    edges = [r for _, r in t["Inputs"][1]]
    events = [r for _, r in t["Events"][1]]
    revs = skill_revisions()
    order, ups = topo_order(docs, edges)
    warn = structure_warnings(t, docs)

    for e in edges:
        for k in ("document", "reads"):
            if e[k] not in docs:
                warn.append(f"Inputs row {e['document']} <- {e['reads']}: unknown id '{e[k]}'")
    for ev in events:
        for a in [x.strip() for x in ev["affects"].split(",") if x.strip()]:
            if a not in docs:
                warn.append(f"Event '{ev['event']}': unknown id '{a}'")
    files = {d["file"] for d in docs.values()}
    for f in sorted((ROOT / "docs").glob("*.md")):
        rel = f"docs/{f.name}"
        if rel not in files and f.name != "update-register.md":
            warn.append(f"{rel} is not in the register")
    for d in docs.values():
        if not (ROOT / d["file"]).exists():
            warn.append(f"{d['id']}: file {d['file']} does not exist")

    update, loop_check, notes, method = {}, {}, {}, {}
    own = {}                  # causes of the document's own (stale date, passed event)
    held, lapsed, deferred, urgent = {}, {}, {}, set()
    defer_to = today + dt.timedelta(days=defer_days)
    for i in order:
        d = docs[i]
        on_hold, htext = hold_of(d, today)
        if on_hold:
            held[i] = htext
        elif htext:
            lapsed[i] = htext
        sa = parse_date(d["stale after"])
        if sa and today > sa:
            own.setdefault(i, []).append(f"stale after {sa}")
        for e in edges:
            if e["document"] != i or e["reads"] not in docs:
                continue
            u = docs[e["reads"]]
            used = parse_date(e["input as of"])
            lc, ao = parse_date(u["last change"]), parse_date(u["as of"])
            if used is None:
                warn.append(f"{i} <- {e['reads']}: no 'input as of' date")
                continue
            if lc and lc > used:
                aff = affects_of(u)
                if aff == "all" or i in aff:
                    msg = f"{e['reads']} changed {lc} (read {used})"
                    if i in urgent_of(u):
                        msg += " [urgent: verdict at risk]"
                        urgent.add(i)
                    (update if e["link"] == "main" else loop_check).setdefault(i, []).append(msg)
                else:
                    notes.setdefault(i, []).append(f"{e['reads']} {lc:%d %b} (not material here)")
            elif ao and ao > used:
                notes.setdefault(i, []).append(f"{e['reads']} {ao:%d %b}")
        for ev in events:
            aff = [x.strip() for x in ev["affects"].split(",")]
            evd = parse_date(ev["date"])
            if i in aff and ev["status"].lower() == "open" and evd and evd < today:
                own.setdefault(i, []).append(f"event passed {evd}: {ev['event']}")

    # Deferral: a flag that comes only from upstream changes waits for the document's own
    # planned update when that is near (an open event of its own, or its stale-after date).
    for i in list(update):
        if i in own or i in urgent:
            continue
        d = docs[i]
        sa = parse_date(d["stale after"])
        nxt = [parse_date(ev["date"]) for ev in events
               if i in [x.strip() for x in ev["affects"].split(",")]
               and ev["status"].lower() == "open" and parse_date(ev["date"])
               and today <= parse_date(ev["date"]) <= defer_to]
        when = min([x for x in nxt + [sa] if x and today <= x <= defer_to], default=None)
        if when:
            deferred[i] = (when, update.pop(i))
    for i, causes in own.items():
        update[i] = causes + update.get(i, [])
    for i in held:
        if i in update:
            held[i] = (held[i], update.pop(i))
        else:
            held[i] = (held[i], [])
        loop_check.pop(i, None)
        deferred.pop(i, None)
    for i in order:
        d = docs[i]
        sk = d["skill"]
        if sk in revs and d["rev used"] not in ("", "-", "?"):
            if rev_key(revs[sk]) > rev_key(d["rev used"]):
                method[i] = f"{sk} {d['rev used']} -> {revs[sk]}"
        elif sk in revs and d["rev used"] in ("?",):
            method[i] = f"{sk} revision used not recorded (now {revs[sk]})"

    wait = {}
    for i in update:
        for dn in downstream(ups, i):
            if dn not in update and dn not in held:
                wait.setdefault(dn, []).append(i)

    print(f"Update-chain check, {today} (register: docs/update-register.md)")
    print()
    print("1. UPDATE NOW, in this order")
    if not update:
        print("   none")
    n = 0
    for i in order:
        if i in update:
            n += 1
            d = docs[i]
            print(f"   {n:>2}. {i:<14} {d['file']:<40} skill {d['skill']}")
            for r in update[i]:
                print(f"         - {r}")
    print()
    print(f"1a. DEFERRED: upstream change only, read at the document's own update within "
          f"{defer_days} days")
    if not deferred:
        print("   none")
    for i in order:
        if i in deferred:
            when, causes = deferred[i]
            print(f"   - {i:<14} next own update {when}: " + "; ".join(causes))
    print()
    print("1b. ON HOLD (user): not run, whatever the causes")
    if not held and not lapsed:
        print("   none")
    for i in order:
        if i in held:
            htext, causes = held[i]
            extra = f"  [{len(causes)} cause(s) waiting]" if causes else ""
            print(f"   - {i:<14} {htext}{extra}")
        elif i in lapsed:
            print(f"   ! {i:<14} {lapsed[i]}")
    print()
    print("2. RE-CHECK AFTER AN UPSTREAM UPDATE (only if it changes values this document reads)")
    if not wait:
        print("   none")
    for i in order:
        if i in wait:
            print(f"   - {i:<14} after {', '.join(sorted(wait[i], key=order.index))}")
    print()
    print("3. LOOP CHECKS (back-references; check once, do not re-run the chain for them)")
    if not loop_check:
        print("   none")
    for i in order:
        if i in loop_check and i not in update:
            print(f"   - {i:<14} " + "; ".join(loop_check[i]))
    print()
    print("4. NO ACTION: upstream re-run but kept unchanged, or changed in values not material "
          "here (mention in the header at the next run)")
    shown = [i for i in order if i in notes and i not in update and i not in held]
    if not shown:
        print("   none")
    for i in shown:
        print(f"   - {i:<14} " + ", ".join(notes[i]))
    print()
    horizon = today + dt.timedelta(days=days)
    print(f"5. EVENTS IN THE NEXT {days} DAYS (to {horizon})")
    up = [ev for ev in events if ev["status"].lower() in ("open", "watch")
          and parse_date(ev["date"]) and today <= parse_date(ev["date"]) <= horizon]
    up.sort(key=lambda ev: parse_date(ev["date"]))
    if not up:
        print("   none")
    for ev in up:
        firm = "" if ev["firm"].lower() == "yes" else " (approx.)"
        watch = " [watch]" if ev["status"].lower() == "watch" else ""
        print(f"   - {ev['date']}{firm}{watch}  {ev['event']}  -> {ev['affects']}")
    print()
    print("6. METHOD CHANGED SINCE THE LAST RUN (skill revision; re-run only if the change matters)")
    if not method:
        print("   none")
    for i in order:
        if i in method:
            print(f"   - {i:<14} {method[i]}")
    nodate = [i for i in order if docs[i]["type"] == "company" and not any(
        i in [x.strip() for x in ev["affects"].split(",")] and ev["status"].lower() == "open"
        and "report" in ev["event"].lower() for ev in events)]
    if nodate:
        print()
        print("7. COMPANIES WITH NO OPEN REPORT DATE IN THE REGISTER")
        print("   " + ", ".join(nodate))
    if warn:
        print()
        print("REGISTER WARNINGS")
        for w in warn:
            print(f"   ! {w}")


# ---------- record / event-done ----------

def record(a):
    lines, t, docs = load()
    if a.id not in docs:
        sys.exit(f"Unknown id '{a.id}'")
    revs = skill_revisions()
    hdr = t["Documents"][0]
    d = docs[a.id]
    if "affects" not in hdr:
        sys.exit("The Documents table has no 'affects' column (see SKILL.md, trigger rule)")
    if a.changed == "yes":
        if not a.affects:
            print("WARNING: --changed yes without --affects; recorded as 'all' (every downstream "
                  "flagged). Give the downstream ids whose read values moved materially, or "
                  "'none' (trigger rule in SKILL.md).")
        new = (a.affects or "all").strip().lower()
        if new != "all":
            ids = set() if new == "none" else {x.strip() for x in new.split(",") if x.strip()}
            bad = sorted({x.rstrip("!") for x in ids} - set(docs))
            if bad:
                sys.exit("Unknown id(s) in --affects: " + ", ".join(bad))
            # keep documents named by the previous change that have not read it yet
            old_lc, old_aff = parse_date(d["last change"]), affects_of(d)
            if old_lc:
                for _, e in t["Inputs"][1]:
                    used = parse_date(e["input as of"])
                    if (e["reads"] == a.id and used and used < old_lc
                            and (old_aff == "all" or e["document"] in old_aff)
                            and e["document"] + "!" not in ids):
                        ids.add(e["document"] + ("!" if e["document"] in urgent_of(d) else ""))
                ids = {x for x in ids if x + "!" not in ids}
            new = ", ".join(sorted(ids)) or "none"
        d["affects"] = new
        d["last change"] = a.as_of
    d["as of"] = a.as_of
    if a.stale_after:
        d["stale after"] = a.stale_after
    if a.rev:
        d["rev used"] = a.rev
    elif d["skill"] in revs:
        d["rev used"] = revs[d["skill"]]
    write_row(lines, d["_line"], hdr, d)
    skip = {s.strip() for s in (a.skip_inputs or "").split(",") if s.strip()}
    ihdr = t["Inputs"][0]
    bumped = []
    for idx, e in t["Inputs"][1]:
        if e["document"] == a.id and e["reads"] in docs and e["reads"] not in skip:
            e["input as of"] = docs[e["reads"]]["as of"]
            write_row(lines, idx, ihdr, e)
            bumped.append(f"{e['reads']}={e['input as of']}")
    save(lines)
    print(f"Recorded {a.id}: as of {a.as_of}, changed {a.changed}, rev {d['rev used']}, "
          f"stale after {d['stale after']}, affects {d.get('affects', 'all')}")
    print("Inputs marked as read: " + (", ".join(bumped) or "none"))


def event_done(text):
    lines, t, _ = load()
    hdr, rows = t["Events"]
    hits = [(i, r) for i, r in rows if text.lower() in r["event"].lower()
            and r["status"].lower() == "open"]
    if len(hits) != 1:
        sys.exit(f"'{text}' matches {len(hits)} open events; give a more exact text")
    i, r = hits[0]
    r["status"] = "done"
    write_row(lines, i, hdr, r)
    save(lines)
    print(f"Done: {r['date']} {r['event']}")


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")
    s = sub.add_parser("status")
    for q in (p, s):
        q.add_argument("--today", default=None)
        q.add_argument("--days", type=int, default=14)
        q.add_argument("--defer-days", type=int, default=14)
    r = sub.add_parser("record")
    r.add_argument("id")
    r.add_argument("--as-of", required=True)
    r.add_argument("--changed", choices=["yes", "no"], required=True)
    r.add_argument("--affects")
    r.add_argument("--stale-after")
    r.add_argument("--rev")
    r.add_argument("--skip-inputs")
    e = sub.add_parser("event-done")
    e.add_argument("text")
    sub.add_parser("lint")
    a = p.parse_args()
    if a.cmd == "lint":
        lint()
    elif a.cmd == "record":
        for v in (a.as_of, a.stale_after):
            if v:
                dt.date.fromisoformat(v)
        record(a)
    elif a.cmd == "event-done":
        event_done(a.text)
    else:
        today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
        status(today, a.days, a.defer_days)


if __name__ == "__main__":
    main()
