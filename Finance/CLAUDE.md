# Finance — investment analysis workspace

This folder is the only source of truth for the investment-analysis skills and their outputs.
Git provides history.

## Layout

| Path | Content |
|---|---|
| `.claude/skills/<name>/SKILL.md` | Skill masters (plus `references/`). Loaded automatically by Claude Code |
| `docs/` | All outputs: market baselines and company analyses (one running file each) |

Skills and the chain between them:

- `oil-market-bbb` → top of the chain; output `docs/oil-market-bbb.md`
- `oil-shipping-bbb` → reads the oil baseline; output `docs/oil-shipping-bbb.md`
- `rig-market-bbb` → reads the oil baseline; output `docs/rig-market-bbb.md`
- `supply-market-bbb` (Supply BBB: OSVs, focus North Sea and South America) → reads the oil and
  rig baselines; output `docs/supply-market-bbb.md`
- `hy-market-bbb` (Nordic HY BBB: NIBOR path, Nordic GDP, HY spreads, default rates, expected
  returns) → reads the oil baseline and, for energy issuers, the rig, supply and shipping
  baselines; output `docs/hy-market-bbb.md`. Fund mode (Heimdal Høyrente, Heimdal Høyrente Pluss,
  Sissener Corporate Bond, Fondsfinans High Yield, Fondsfinans Kreditt) → `docs/hy-funds-analysis.md`; company bond assessment
  (expected return and risk per bond) and the Stamdata distress screen → `docs/hy-issuers.md`
- `defense-market-bbb` (Defense BBB: European defense spending per country, equipment and
  addressable spending, segment order and revenue paths) → top of its own chain, independent of
  oil; reads Nordic GDP from `docs/hy-market-bbb.md`; output `docs/defense-market-bbb.md`
- `equity-market-bbb` (Equity BBB: Oslo/OSEBX and global/MSCI World index returns in NOK, IAF at
  index level, oil and NOK linkage, equity triggers mirroring the HY rule) → reads the oil
  baseline (Oslo energy earnings) and the HY baseline (NIBOR, GDP, HY return and the HY market
  reference E / R); output `docs/equity-market-bbb.md`. Market only: it
  analyses no named fund or single paper and does not read or write `docs/portfolio-overview.md`
- `ai-market-bbb` (AI BBB: AI capex and its financing, hardware (compute, memory, foundry and
  equipment, networking and DC infrastructure, power), AI engines (frontier labs, AI cloud) and
  tools (copilots, AI-native tools, incumbent software); layer-basket IAF test) → reads the equity
  baseline (scenarios, NOK path, World) and NIBOR from the HY baseline; output
  `docs/ai-market-bbb.md`
- `iaf-valuation` → company valuation using the sector baselines; outputs
  `docs/<company>-analysis.md` (e.g. `docs/capt-analysis.md`, `docs/SED-analysis.md`)
- Background on the IAF reasoning: `docs/iaf-reference-notes.md`
- `update-chain` → orchestrator over all of the above: it keeps `docs/update-register.md` (which
  document reads which input version, stale dates, planned events) and updates documents in
  dependency order, each by its own skill; check script
  `.claude/skills/update-chain/references/update_check.py`

## Working rules

- Write every skill change and every output document to this folder, then read the file back to
  check tables and content. An answer in the conversation alone is not delivery.
- **Lean documents (user, 12 Nov 2026; overrides any skill output template that keeps history):**
  - **Current state only.** Git keeps every earlier version, so a document holds no superseded
    notes, no old values in brackets, no old attributions and no dated re-mark blocks at the top.
    Its change log keeps the **last 3 versions, one or two lines each**; older entries are deleted.
  - **Size budgets:** company and fund analyses ≤ 450 lines; market baselines and books ≤ 800 lines;
    reviews are static and exempt. `update_check.py lint` flags documents over budget.
  - **Interface block:** every market baseline starts, after its status line, with a section
    "## Interface (values other documents read)": one compact table of the paths, references and
    signpost states that downstream documents use, with the as-of date.
  - **Read sections, not files.** A run that reads an upstream document reads its Interface
    section and its latest change-log entry, and goes deeper only for a value it needs. A run
    reads a skill's steps for its own task, not every appendix.
  - A document is compacted to these rules at its next run; no separate rewrite run is needed.
- Python: standard-library scripts (`update_check.py`, the model scripts) run with `py`. Scripts
  that import a package (`pypdf`, `numpy`, `openpyxl`, `pymupdf`) run with the workspace venv,
  `C:/GitWork/hsaether/Finance/.venv/Scripts/python` (add `-I` when reading downloaded files).
  Packages are listed in `requirements.txt`. Installing outside the venv is denied in
  `.claude/settings.json`; if a package is missing, ask the user rather than work around it.
- When asked to save or change a skill, do it without asking first.
- Every skill master carries a `**Revision:** YYYY-MM-DD.n` line. Bump it on every change to that
  skill (date + counter). Start every analysis by stating the revision of each skill used.
- Input the user gives (links, drafts, numbers) is input, not a reference: assess its value
  critically, extract what is sensible, and update the skill or document accordingly.
- Downstream skills never make their own oil-market forecast; they read the current
  `docs/oil-market-bbb.md`. Supply BBB likewise never makes its own rig forecast; it reads
  `docs/rig-market-bbb.md`. The NIBOR path and Nordic GDP view are set only in
  `docs/hy-market-bbb.md`; other skills read them there. Defense spending paths and the defense
  market view are set only in `docs/defense-market-bbb.md`. Equity index return paths, index
  hurdles and the NOK scenario path are set only in `docs/equity-market-bbb.md`. AI market paths
  (capex, layer revenues, lab revenue, adoption, layer EPS paths) are set only in
  `docs/ai-market-bbb.md`.
- After any document in `docs/` is updated, by any skill and also outside the update chain,
  record it in the register:
  `py .claude/skills/update-chain/references/update_check.py record <id> --as-of <date> --changed yes|no --affects <ids>|none --stale-after <date>`.
  `--changed yes` only when a value other documents read moved; `--affects` names only the
  downstream documents for which it moved materially (trigger rule in the `update-chain` skill;
  a price-only re-mark is `none`). A note starting `HOLD (user` keeps a document out of runs. Add the new dated events (report
  dates, decisions) to the register's Events table.
- The register is part of delivering a document, so do it without being asked. A **new or retired
  document** follows Mode D of the `update-chain` skill step by step:
  - its own inputs;
  - a search of `docs/` for every document that should read it;
  - the events;
  - edits by whole lines only;
  - then `update_check.py lint`, which must show no structural error, with every hint judged.

  Say in the answer what was changed in the register.
- Never use git for any work (no git mv, rm, add, commit, status, etc.) and never ask about
  commits. The user handles all git transactions. Use plain file operations only.
