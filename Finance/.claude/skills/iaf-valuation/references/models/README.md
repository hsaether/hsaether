# Model scripts per analysis

One folder per document id. The scripts that built the latest version; the next run starts from them.

| Folder | Document | Version | Date |
|---|---|---|---|
| anthropic/ | docs/anthropic-analysis.md | v1.0 at the IPO range (model.py: build and scenarios; report.py: tables, reverse tests, sensitivities, stakes; drivers.py: driver breakdown) | 13 Nov 2026 |
| dof/ | docs/DOF-analysis.md | full update after Q3 (dof_model.py, inputs_new.py, report.py, sens.py) | 12 Nov 2026 |
| nvda/ | docs/nvda-analysis.md | v1.6: v15.py (model, unchanged since v1.5), v15_run.py and v15_sens.py (decision figures and sensitivities; run with the price, e.g. `py v15_run.py 166.19`), v16_cascade.py (vendor-financing cascade stress test, grid, cost of the alternative); v13.py kept for the v1.4 reproduction | 13 Nov 2026 |
| odl/ | docs/odl-analysis.md | v2.1 re-mark layer (odl_remark.py) on v2's published streams; the v2 rig-day model was not kept, so the next full run (Q4 report) rebuilds it here | 13 Nov 2026 |
