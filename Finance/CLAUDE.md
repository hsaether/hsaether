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
  Sissener Corporate Bond, Fondsfinans High Yield) → `docs/hy-funds-analysis.md`; company bond assessment
  (expected return and risk per bond) and the Stamdata distress screen → `docs/hy-issuers.md`
- `defense-market-bbb` (Defense BBB: European defense spending per country, equipment and
  addressable spending, segment order and revenue paths) → top of its own chain, independent of
  oil; reads Nordic GDP from `docs/hy-market-bbb.md`; output `docs/defense-market-bbb.md`
- `iaf-valuation` → company valuation using the sector baselines; outputs
  `docs/<company>-analysis.md` (e.g. `docs/capt-analysis.md`, `docs/SED-analysis.md`)
- Background on the IAF reasoning: `docs/iaf-reference-notes.md`

## Working rules

- Write every skill change and every output document to this folder, then read the file back to
  check tables and content. An answer in the conversation alone is not delivery.
- When asked to save or change a skill, do it without asking first.
- Every skill master carries a `**Revision:** YYYY-MM-DD.n` line. Bump it on every change to that
  skill (date + counter). Start every analysis by stating the revision of each skill used.
- Input the user gives (links, drafts, numbers) is input, not a reference: assess its value
  critically, extract what is sensible, and update the skill or document accordingly.
- Downstream skills never make their own oil-market forecast; they read the current
  `docs/oil-market-bbb.md`. Supply BBB likewise never makes its own rig forecast; it reads
  `docs/rig-market-bbb.md`. The NIBOR path and Nordic GDP view are set only in
  `docs/hy-market-bbb.md`; other skills read them there. Defense spending paths and the defense
  market view are set only in `docs/defense-market-bbb.md`.
- Never use git for any work (no git mv, rm, add, commit, status, etc.) and never ask about
  commits. The user handles all git transactions. Use plain file operations only.
