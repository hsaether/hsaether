"""msft_n20.py - version 3.3 (20 Nov 2026 close): msft_remark.py at $484.52, valuation date 20 Nov, Anthropic at $88.91 (20 Nov close).
Run: py msft_n20.py"""
from datetime import date
import msft_remark as m
cfg, meta = m.remark_cfg(P=484.52, vdate=date(2026, 11, 20), ant_px=88.91)
m.report(cfg, 0.0472, 0.075, '20 Nov close re-mark (v3.3)', meta)
print('=== attribution v3.2 -> v3.3')
c0, _ = m.remark_cfg()
for lab, c in [('v3.2 (19 Nov, $498.30, ANT 97.17)', c0),
               ('+ Anthropic 88.91', m.remark_cfg(P=498.30, ant_px=88.91)[0]),
               ('+ date 20 Nov', m.remark_cfg(P=498.30, vdate=date(2026, 11, 20), ant_px=88.91)[0]),
               ('+ price 484.52', cfg)]:
    r = m.build(c)['base']
    print(f'  {lab:40s} IRR {r["irr"]*100:6.2f}%  P_k {r["pk"]:7.2f}  MoS {r["mos"]*100:6.2f}%  V_T {r["VT"]:7.2f}')
m.sens(cfg, meta); m.drivers(cfg); m.bridge(cfg)
