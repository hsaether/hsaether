# AI Market BBB — Memory cycle: the H2 path the price implies (basket and names). Added 1 Nov 2026 (skill 2026-11-01.1).
# Base method: exit P/E 10, payout 15%, cash conversion .70/.65/.60, Base FX (NOK = USD). Reads model.py's inputs and data/q.json.
# Outputs: uniform multiplier on Base 2028-30 (2027 at Base) for k = 12% and for 0%; the same on all years; the flat 2028-30
# level; IRR of named turn-date and depth paths at exit P/E 10 and 8; the basket multiplier at exit P/E 8 / 10 / 11. Run: py -I impl.py
import sys; sys.argv=['model.py']; exec(open('model.py',encoding='utf-8').read().split("out = {}")[0])
name, mem, PE, po = L['H2']
W = {s: mc(s) for s in mem}; Wt = sum(W.values())
pe_b = Wt/sum(W[s]/(q[s]['regularMarketPrice']/eps27[s]) for s in mem)
def r(P, e, ex=10, cv=None):
    cv = cv or CONV['H2']['Base']
    V, D = build(e, P, ex, po, cv, False)
    return irr([(0,-P)]+[(T0+k+.5,D[k]) for k in range(3)]+[(T0+3,V[2])])*100
def solve(P, f, target, lo=0.0, hi=3.0):
    for _ in range(80):
        m=(lo+hi)/2
        if r(P, f(m)) < target: lo=m
        else: hi=m
    return m
B = PATHS['H2']['Base']
print(f"H2 basket P/E CY27 {pe_b:.2f}; Base {r(pe_b,B):.1f}%  members P/E:", {s: round(q[s]['regularMarketPrice']/eps27[s],2) for s in mem})
for lab, P in [('basket', pe_b)] + [(s, q[s]['regularMarketPrice']/eps27[s]) for s in mem]:
    m12 = solve(P, lambda m: (B[0], B[1]*m, B[2]*m, B[3]*m), 12); m0 = solve(P, lambda m: (B[0], B[1]*m, B[2]*m, B[3]*m), 0)
    a12 = solve(P, lambda m: tuple(x*m for x in B), 12); a0 = solve(P, lambda m: tuple(x*m for x in B), 0)
    f12 = solve(P, lambda x: (B[0], x, x, x), 12); f0 = solve(P, lambda x: (B[0], x, x, x), 0)
    print(f"{lab:10s} P/E {P:5.2f} | 2028-30 x m: k at {m12:.2f} ({', '.join(f'{x*m12:.2f}' for x in B[1:])}), 0% at {m0:.2f} ({', '.join(f'{x*m0:.2f}' for x in B[1:])}) | all years x: k {a12:.2f}, 0% {a0:.2f} | flat 2028-30 level: k {f12:.2f}, 0% {f0:.2f}")
print("\nTurn-date and depth paths (2027/28/29/2030 norm), basket, Base method, exit P/E 10 (and 8):")
paths = {
 'Base: turn 2028 (2017-19 analogue)': B,
 'Earlier turn: prices fall from 2H-27': (.80,.45,.35,.35),
 'Later turn: prices hold through 2028, fall 2029': (.95,.85,.55,.40),
 'Shallower: LTA floors hold, mid-cycle higher': (.90,.70,.55,.45),
 'Deeper: 2019-depth fall, pre-AI-style mid-cycle': (.90,.45,.30,.25),
 'Bull path': PATHS['H2']['Bull'],
 'Bear path (at the Base exit P/E 10)': PATHS['H2']['Bear'],
}
for k, e in paths.items():
    print(f"  {k:52s} {'/'.join(f'{x:.2f}' for x in e)}  IRR {r(pe_b,e):6.1f}%  (exit 8: {r(pe_b,e,8):6.1f}%)  sum EPS 27-29 {sum(e[:3]):.2f}")
# implied: turn year shift of the Base fall for k: path holds .90 until year t then follows Base shape
print(chr(10)+"Exit P/E sensitivity of the basket multiplier (2028-30 x Base):")
def solve_ex(P, f, target, ex):
    lo,hi=0.0,3.0
    for _ in range(80):
        m=(lo+hi)/2
        if r(P, f(m), ex) < target: lo=m
        else: hi=m
    return m
for ex in (8,10,11):
    m12=solve_ex(pe_b, lambda m:(B[0],B[1]*m,B[2]*m,B[3]*m),12,ex); m0=solve_ex(pe_b, lambda m:(B[0],B[1]*m,B[2]*m,B[3]*m),0,ex)
    print(f"  exit P/E {ex}: 2028-30 x {m12:.2f} for k, x {m0:.2f} for 0%")
