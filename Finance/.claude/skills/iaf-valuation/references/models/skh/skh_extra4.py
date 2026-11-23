# SK hynix v4 (19 Nov 2026): price triggers, extra sensitivities and the ADR at the 13 Nov close.
import skh_model as m
from skh_run4 import R, solve, I, FX, ADR13, pct, K
rb = R('Base')
def irr_at(P, s='Base', **ov):
    r = R(s, **ov); return m.irr(P, r['dates'], r['D'], r['VT'], r['vd'])
for tgt, nm in [(0.075, 'HY market Base 7.5%'), (0.064, 'World Base 6.4%'), (0.12, 'k')]:
    p = solve(lambda x: irr_at(x), 500000, 5000000, tgt)
    print(f"Base = {nm} at KRW {K(p)}")
print("Base at 1,132,000 (6 Nov):", pct(irr_at(1132000)), "at 1,216,000 (13 Nov):", pct(irr_at(1216000)))
for f in (0.5, 0.4):
    x = R('Base', mem30_mult=f); print(f"2030 EPS x{f}: {pct(x['irr'])} ({K(x['pk'])})")
for s in ['Bear', 'Base', 'Bull']:
    r = R(s); Pa = ADR13 * 10 * 1333.78
    prem = {'Bear': 0.0, 'Base': 0.15, 'Bull': ADR13 * 10 * 1333.78 / 1216000 - 1}[s]
    print(f"ADR 13 Nov close {s}: {pct(m.irr(Pa, r['dates'], r['D'], r['VT']*(1+prem), r['vd']))}")
# stub and Year-1 quarterly
q = I['q4']; f = 42 / 92
eps_q4 = (q['op'] + q['intr']) * (1 - m.TAX) / (I['sh'] / 1e6)
print("Q4E EPS", K(eps_q4), "stub EPS", K(eps_q4 * f), "stub rev", round(q['rev'] * f, 1), "stub EBITDA", round((q['op'] + q['da']) * f, 1),
      K((q['op'] + q['da']) * f / (I['sh'] / 1e6)), "stub FCF", round(m.bridge(I)['fcf_q4'] * f, 1), K(m.bridge(I)['fcf_q4'] * f / (I['sh'] / 1e6)))
split = [118446, 134000, 140000, 145465]
for nm, h in [('Base', [.98, .93, .87, .83]), ('Bear', [.85, .62, .50, .46])]:
    v = [a * b for a, b in zip(split, h)]
    print(nm, [K(x) for x in v], K(sum(v)), round(sum(v) / I['cons27'], 3))
print("mcap tn", round(I['P'] * I['sh'] / 1e6, 1), "USD bn", round(I['P'] * I['sh'] / 1e6 / FX * 1000, 0))
