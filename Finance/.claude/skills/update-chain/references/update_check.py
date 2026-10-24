"""Update-chain check: reads docs/update-register.md and the skill revisions, and lists
what needs updating, in dependency order.

Usage (from the Finance folder or anywhere; paths are resolved from this file):
  py update_check.py [status] [--today YYYY-MM-DD] [--days 14]
  py update_check.py record <id> --as-of YYYY-MM-DD --changed yes|no
                     [--stale-after YYYY-MM-DD] [--rev REV] [--skip-inputs id1,id2]
  py update_check.py event-done "<text that matches one open event>"

status      : the check. Prints nothing to disk.
record      : after a document is updated. Sets its "as of" (and "last change" when values
              that downstream documents read moved), stale-after and revision, and marks
              every input it reads as read at the upstream's current "as of".
event-done  : marks one event in the Events table as done.

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
                rows.append((i, dict(zip(header, cells))))
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


# ---------- status ----------

def status(today, days):
    lines, t, docs = load()
    edges = [r for _, r in t["Inputs"][1]]
    events = [r for _, r in t["Events"][1]]
    revs = skill_revisions()
    order, ups = topo_order(docs, edges)
    warn = []

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
    for i in order:
        d = docs[i]
        sa = parse_date(d["stale after"])
        if sa and today > sa:
            update.setdefault(i, []).append(f"stale after {sa}")
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
                msg = f"{e['reads']} changed {lc} (read {used})"
                (update if e["link"] == "main" else loop_check).setdefault(i, []).append(msg)
            elif ao and ao > used:
                notes.setdefault(i, []).append(f"{e['reads']} {ao:%d %b}")
        for ev in events:
            aff = [x.strip() for x in ev["affects"].split(",")]
            evd = parse_date(ev["date"])
            if i in aff and ev["status"].lower() == "open" and evd and evd < today:
                update.setdefault(i, []).append(f"event passed {evd}: {ev['event']}")
        sk = d["skill"]
        if sk in revs and d["rev used"] not in ("", "-", "?"):
            if rev_key(revs[sk]) > rev_key(d["rev used"]):
                method[i] = f"{sk} {d['rev used']} -> {revs[sk]}"
        elif sk in revs and d["rev used"] in ("?",):
            method[i] = f"{sk} revision used not recorded (now {revs[sk]})"

    wait = {}
    for i in update:
        for dn in downstream(ups, i):
            if dn not in update:
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
    print("4. NO ACTION: upstream re-run but kept unchanged (mention in the header at the next run)")
    shown = [i for i in order if i in notes and i not in update]
    if not shown:
        print("   none")
    for i in shown:
        print(f"   - {i:<14} " + ", ".join(notes[i]))
    print()
    horizon = today + dt.timedelta(days=days)
    print(f"5. EVENTS IN THE NEXT {days} DAYS (to {horizon})")
    up = [ev for ev in events if ev["status"].lower() == "open"
          and parse_date(ev["date"]) and today <= parse_date(ev["date"]) <= horizon]
    up.sort(key=lambda ev: parse_date(ev["date"]))
    if not up:
        print("   none")
    for ev in up:
        firm = "" if ev["firm"].lower() == "yes" else " (approx.)"
        print(f"   - {ev['date']}{firm}  {ev['event']}  -> {ev['affects']}")
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
    d["as of"] = a.as_of
    if a.changed == "yes":
        d["last change"] = a.as_of
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
          f"stale after {d['stale after']}")
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
    r = sub.add_parser("record")
    r.add_argument("id")
    r.add_argument("--as-of", required=True)
    r.add_argument("--changed", choices=["yes", "no"], required=True)
    r.add_argument("--stale-after")
    r.add_argument("--rev")
    r.add_argument("--skip-inputs")
    e = sub.add_parser("event-done")
    e.add_argument("text")
    a = p.parse_args()
    if a.cmd == "record":
        for v in (a.as_of, a.stale_after):
            if v:
                dt.date.fromisoformat(v)
        record(a)
    elif a.cmd == "event-done":
        event_done(a.text)
    else:
        today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
        status(today, a.days)


if __name__ == "__main__":
    main()
