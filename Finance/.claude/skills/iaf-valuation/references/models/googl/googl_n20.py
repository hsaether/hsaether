"""googl_n20.py - version 2.3 (20 Nov 2026 close): googl_remark.py at $265.29, valuation date 20 Nov, SPCX $127.79, Anthropic $88.91 (20 Nov closes).
Run: py googl_n20.py"""
from datetime import date
import googl_remark as m
cfg, meta = m.remark_cfg(P=265.29, vdate=date(2026, 11, 20), spcx=127.79, ant=88.91)
m.report(cfg, 0.0472, 0.075, '20 Nov close re-mark (v2.3)', meta)
print('=== attribution v2.2 -> v2.3')
c0, _ = m.remark_cfg()
for lab, c in [('v2.2 (19 Nov, $272.66, SPCX 138.43, ANT 97.17)', c0),
               ('+ SPCX 127.79', m.remark_cfg(spcx=127.79)[0]),
               ('+ Anthropic 88.91', m.remark_cfg(spcx=127.79, ant=88.91)[0]),
               ('+ date 20 Nov', m.remark_cfg(vdate=date(2026, 11, 20), spcx=127.79, ant=88.91)[0]),
               ('+ price 265.29', cfg)]:
    r = m.build(c)['base']
    print(f'  {lab:48s} IRR {r["irr"]*100:6.2f}%  P_k {r["pk"]:7.2f}  MoS {r["mos"]*100:6.2f}%  V_T {r["VT"]:7.2f}')
m.sens(cfg, meta); m.drivers(cfg); m.bridge(cfg)
