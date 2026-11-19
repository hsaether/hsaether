"""NVIDIA v1.8 -- the user's funding-loss scenario (19 Nov 2026), built step by step on the v1.8 Base.
User view: funding of customers keeps absorbing cash, the funded book (junk-rated neoclouds, labs) produces
losses, FCF to holders falls well short. Run: py v18_userfund.py [price]
Steps are cumulative; all sizes are [A] (own assumptions), anchored on the Q3 FY27 CFO commentary."""
import sys
import v18 as m

P = float(sys.argv[1]) if len(sys.argv) > 1 else 150.96
B = m.BASE
SH = m.SH
pct = lambda x: f"{x*100:.1f}%"


def show(lab, s):
    r = m.build(s, P)
    fcfh = [f - 0 for f in r['FCF']]
    print(f"{lab:78s} IRR {pct(r['irr']):>6s}  P_k {r['pk']:6.1f}  MoS {r['pk']/P-1:+6.1%}  V_T {r['VT']:6.1f}  "
          f"FCF to holders $bn {[round(x) for x in fcfh]}")
    return r


print(f"P = {P}")
show("0. Base v1.8 (stakes 18.9 / 2 / 2bn; no charges; stakes at book; exit 17)", B)
s1 = dict(B, stakes=[75, 75, 75])
show("1. Funding continues at the 2026 pace: $75bn a year into stakes/loans, at book", s1)
s2 = dict(s1, sf=0.5)
show("2. + the funded book is junk: all stakes worth 50% at exit", s2)
s3 = dict(s2, charge=[0, 15, 15], exitliab=30)
show("3. + guarantees called: $15bn in 2028 and 2029, $30bn more owed at exit", s3)
s4 = dict(s3, pe=15)
show("4. + the market de-rates NVIDIA for the losses: exit P/E 15", s4)
s5 = dict(s4, eps=[B['eps'][0], B['eps'][1] * 0.9, B['eps'][2] * 0.9], eps30=B['eps30'] * 0.9)
show("5. + funded customers cut orders: 2028-30 EPS x0.9", s5)
s6 = dict(s5, stakes=[100, 100, 100])
show("6. + funding needs grow to $100bn a year (5 with more cash out)", s6)

print("\nPrice at which each step returns k (12%):")
for lab, s in [("Base", B), ("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5), ("6", s6)]:
    print(f"  {lab}: ${m.build(s, P)['pk']:.1f}")

# what EPS multiplier on 2028-30 makes step 4 fail k at today's price
def f(x):
    s = dict(s4, eps=[B['eps'][0], B['eps'][1] * x, B['eps'][2] * x], eps30=B['eps30'] * x)
    return m.build(s, P)['irr']
print(f"\nStep 4 (cash leak + losses + de-rating) returns k down to 2028-30 EPS x{m.solve(f, 0.12, 0.3, 1.5):.2f} of Base")
r = m.build(B, P)
print("Base FCF after growth $bn", [round(x) for x in r['FCF']], "NI", [round(x) for x in r['NI']])
