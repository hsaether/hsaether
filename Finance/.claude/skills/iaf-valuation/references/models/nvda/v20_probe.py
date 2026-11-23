"""NVIDIA v2.0 (20 Nov 2026) -- SEC accounting-probe sensitivity (g) on the v1.9 Base. Run: py v20_probe.py [price]
Reuters 20 Nov: SEC enforcement staff examine "potential accounting issues"; no practice named. Channels [A]:
 1. Restatement: amounts paid to funded customers (capacity buy-backs ~$32bn, cloud service agreements ~$28bn,
    ~six years) re-characterised as consideration payable to a customer (ASC 606), i.e. netted against revenue at
    ~100% margin. Cash is unchanged: the funding flows are already in Base, so the EPS cut is offset in stakes.
 2. A penalty or settlement in 2028.
 3. A credibility discount on the exit multiple (Base 15 already prices the funding losses and the CEO change).
 4. Wide case only: the restatement shows funded demand is weaker -> 2028-30 EPS x0.9 (the AI BBB order-cut watch).
"""
import sys
import v19 as m

P = float(sys.argv[1]) if len(sys.argv) > 1 else 125.53
B = m.BASE
SH = m.SH; TAX = 0.17
pct = lambda x: f"{x*100:.1f}%"


def restate(s, bn):
    """revenue netted by bn a year 2027-30 at ~100% margin: EPS down, cash neutral (stakes absorb it)"""
    d = bn * (1 - TAX) / SH
    return dict(s, eps=[e - d for e in s['eps']], eps30=s['eps30'] - d,
                stakes=[st - bn * (1 - TAX) for st in s['stakes']])


def show(lab, s):
    r = m.build(s, P)
    print(f"{lab:84s} IRR {pct(r['irr']):>6s}  P_k {r['pk']:6.1f}  MoS {r['pk']/P-1:+6.1%}  V_T {r['VT']:6.1f}  EPS30 {s['eps30']:.2f}")
    return r


print(f"P = {P}")
show("Base v1.9", B)
for bn in (5, 10, 20):
    show(f"1. restatement: ${bn}bn a year netted from revenue (EPS -{bn*(1-TAX)/SH:.2f}), cash neutral", restate(B, bn))
c = restate(B, 10)
show("central 1+2: $10bn restated + $10bn penalty in 2028", dict(c, charge=[0, B['charge'][1] + 10, B['charge'][2]]))
cc = dict(c, charge=[0, B['charge'][1] + 10, B['charge'][2]], pe=14)
show("central 1+2+3: + exit 14 (credibility)", cc)
w = restate(B, 25)
w = dict(w, charge=[0, B['charge'][1] + 25, B['charge'][2]], pe=13)
show("wide 1+2+3: $25bn restated + $25bn penalty + exit 13", w)
w4 = dict(w, eps=[w['eps'][0], w['eps'][1] - 0.1 * B['eps'][1], w['eps'][2] - 0.1 * B['eps'][2]], eps30=w['eps30'] - 0.1 * B['eps30'])
show("wide 1+2+3+4: + funded buyers cut orders (2028-30 x0.9 of Base)", w4)
show("penalty only: $25bn in 2028", dict(B, charge=[0, B['charge'][1] + 25, B['charge'][2]]))
show("credibility only: exit 13", dict(B, pe=13))
print("Price at which each case returns k:")
for lab, s in [("central", cc), ("wide", w), ("wide + order cut", w4)]:
    print(f"  {lab}: ${m.build(s, P)['pk']:.1f}")
