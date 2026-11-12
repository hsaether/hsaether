# AI Market BBB — K1 return gauge (skill 2026-11-11.2, Step 1b item 3). Standard library only.
# Built from the review's ret.py + ret2.py (docs/review-ai-k1-sustainability.md, section 4); it reproduces the
# review's tables 4.2 (taper path), 4.3 (sensitivities) and 4.4 (other K1 paths) exactly.
#
# What it measures. The AI asset base = K1 hyperscaler capex above a non-AI baseline, by monthly vintage.
# Each month's AI spend is depreciated from when it is placed in service; net assets include construction
# in progress (the capital is invested before it earns). For each year:
#   required AI revenue at r = (r x average net AI assets + AI depreciation) / (1 - cash cost ratio)
#   supply = the AI revenue the baseline's own Base paths deliver (E2 cloud above a 10% trend from 2023,
#            T1 Copilot seats x ~$240 a year, Meta's revenue above a 10% trend: an upper bound)
#   coverage = supply / required;  pre-tax return = (supply x (1 - cash cost) - AI depreciation) / avg net AI assets
# It is a durability gauge for the K1 cycle judgement, never a path-setter (SKILL.md, Definitions).
#
# Parameters [F] from filings unless tagged (review, 3.3-3.4 and 4.1):
#   K1 2022-25 165 / 165 / 262 / 450 (cash capex of the five + finance leases; the baseline's ~435 for 2025 is [A])
#   non-AI capex 140 in 2023, +5% a year [A, calibrated: model AI depreciation ~98bn annualised in Q3-26 against
#     ~96bn of the five's D&A above a 5% non-AI trend]
#   short-lived 65% (Alphabet Q3 servers and networking), life 5.5 years, in service after 2 months [lag A]
#   long-lived 35%, life 20 years, in service after 12 months, 5% of it land (not depreciated) [A]
#   cash cost ratio of AI revenue 40% (AWS 41% in Q3-26, CoreWeave 38%); required pre-tax return 10%
#   K1 after 2029 flat at the 2029 level (it only carries depreciation)
#
# Run:  py -I k1ret.py                 gauge on the current Base, sensitivities, other K1 paths
#       py -I k1ret.py taper           the full table for a named path (base, taper, flat, hold, bear, bull)
# Update PATHS['base'] when the baseline's K1 Base moves; E2 / T1 / Meta below when those Base rows move.
import sys
sys.stdout.reconfigure(encoding='utf-8')

YEARS = list(range(2022, 2034))                 # monthly model span; tables show 2025-2031
K1_HIST = {2022: 165, 2023: 165, 2024: 262, 2025: 450}
PATHS = {  # K1 2026-29 (USD bn); flat after 2029
    'base':  {2026: 790, 2027: 1120, 2028: 1170, 2029: 1170},   # Base since 11 Nov 2026 (digestion plateau)
    'taper': {2026: 790, 2027: 1120, 2028: 1250, 2029: 1300},   # guidance-and-consensus taper; review table 4.2
    'flat':  {2026: 790, 2027: 1120, 2028: 1120, 2029: 1120},
    'hold':  {2026: 790, 2027: 1120, 2028: 650, 2029: 650},     # holds the 2027 coverage by 2029
    'bear':  {2026: 790, 2027: 950, 2028: 800, 2029: 820},
    'bull':  {2026: 790, 2027: 1300, 2028: 1550, 2029: 1700},
}
DEFAULT = dict(r=.10, cost=.40, s=.65, life_s=5.5, life_l=20.0, lag_s=2, lag_l=12, land=.05,
               nonai0=140.0, nonai_g=.05, meta=True, e2='base')
# Supply on the AI BBB Base E-paths [A]
E2_2026 = 440.0                                  # four clouds, CY26 (AWS actuals)
E2_GROWTH = {'base': (.38, .25, .18), 'bull': (.45, .32, .22)}   # 2027-29; then +12% / +10% / +8% / +8%
E2_LATE = (.12, .10, .08, .08)                   # 2030-33
E2_HIST = {2023: 180.0, 2024: 225.0, 2025: 286.0}
SEATS = {2024: 0, 2025: 5, 2026: 10, 2027: 14, 2028: 23, 2029: 31, 2030: 38, 2031: 44, 2032: 48, 2033: 50}
META = {2023: 134.9, 2024: 164.5, 2025: 201.0, 2026: 256.0}  # then +13% a year


def k1_path(name_or_dict):
    p = PATHS[name_or_dict] if isinstance(name_or_dict, str) else name_or_dict
    k = dict(K1_HIST); k.update(p)
    last = k[max(p)]
    for y in YEARS:
        k.setdefault(y, last)
    return k


def e2_path(case):
    e = dict(E2_HIST); e[2026] = E2_2026
    for y, g in zip((2027, 2028, 2029, 2030, 2031, 2032, 2033), E2_GROWTH[case] + E2_LATE):
        e[y] = e[y - 1] * (1 + g)
    return e


def meta_path():
    m = dict(META)
    for y in range(2027, 2034):
        m[y] = m[y - 1] * 1.13
    return m


def supply(y, meta=True, e2='base'):
    """AI revenue on the Base E-paths: (total, cloud, Copilot, Meta)."""
    cloud = max(0.0, e2_path(e2)[y] - 180.0 * 1.10 ** (y - 2023))
    seats = SEATS.get(y, 0)
    m = max(0.0, meta_path().get(y, 0.0) - 134.9 * 1.10 ** (y - 2023)) if meta else 0.0
    return cloud + seats + m, cloud, seats, m


def assets(k1, s, life_s, life_l, lag_s, lag_l, land, nonai0, nonai_g, **_):
    """Monthly vintages: AI capex, depreciation, average and end net AI assets per year."""
    months = [(y, m) for y in YEARS for m in range(12)]
    spend = []
    for y, m in months:
        spend.append(max(0.0, k1[y] - nonai0 * (1 + nonai_g) ** max(0, y - 2023)) / 12)
    out = {y: dict(capex=0.0, dep=0.0, avg=0.0, net=0.0, cum=0.0) for y in YEARS}
    cum = acc = 0.0
    for i, (y, m) in enumerate(months):
        d = 0.0
        for j in range(i + 1):
            age = i - j
            if lag_s <= age < lag_s + life_s * 12:
                d += spend[j] * s / (life_s * 12)
            if lag_l <= age < lag_l + life_l * 12:
                d += spend[j] * (1 - s) * (1 - land) / (life_l * 12)
        cum += spend[i]; acc += d
        o = out[y]; o['capex'] += spend[i]; o['dep'] += d; o['avg'] += (cum - acc) / 12
        o['net'] = cum - acc; o['cum'] = cum
    return out


def gauge(path='base', **kw):
    """Rows per year 2025-2031 for one K1 path and parameter set."""
    p = dict(DEFAULT, **kw)
    k1 = k1_path(path)
    a = assets(k1, **p)
    rows = {}
    for y in range(2025, 2032):
        need = (p['r'] * a[y]['avg'] + a[y]['dep']) / (1 - p['cost'])
        need0 = a[y]['dep'] / (1 - p['cost'])
        tot, cloud, seats, m = supply(y, p['meta'], p['e2'])
        ebit = tot * (1 - p['cost']) - a[y]['dep']
        rows[y] = dict(k1=k1[y], capex=a[y]['capex'], cum=a[y]['cum'], dep=a[y]['dep'], avg=a[y]['avg'],
                       need=need, need0=need0, supply=tot, cloud=cloud, seats=seats, meta=m,
                       cover=tot / need, gap=tot - need, ret=ebit / a[y]['avg'],
                       da5=93.5 * 1.05 ** (y - 2023) + a[y]['dep'])
    return rows


def table(path='base', **kw):
    g = gauge(path, **kw); ys = list(g)
    f = lambda key, fmt: ' | '.join(fmt(g[y][key]) for y in ys)
    print(f"\nK1 path '{path}' {kw or ''}: USD bn | " + ' | '.join(str(y) for y in ys))
    print('K1                      | ' + f('k1', lambda v: f'{v:,.0f}'))
    print('AI capex                | ' + f('capex', lambda v: f'{v:,.0f}'))
    print('Cumulative AI capex     | ' + f('cum', lambda v: f'{v:,.0f}'))
    print('AI depreciation         | ' + f('dep', lambda v: f'{v:,.0f}'))
    print('Average net AI assets   | ' + f('avg', lambda v: f'{v:,.0f}'))
    print('Revenue needed, r = 10% | ' + f('need', lambda v: f'{v:,.0f}'))
    print('Revenue needed, r = 0%  | ' + f('need0', lambda v: f'{v:,.0f}'))
    print('Supply (cloud/T1/Meta)  | ' + ' | '.join(f"{g[y]['supply']:,.0f} ({g[y]['cloud']:.0f} / {g[y]['seats']:.0f} / {g[y]['meta']:.0f})" for y in ys))
    print('Coverage of the need    | ' + f('cover', lambda v: f'{v*100:.0f}%'))
    # gap = rounded supply - rounded need, as the published tables show it; '—' where supply covers the need
    print('Gap to the need         | ' + ' | '.join(
        '—' if g[y]['gap'] >= 0 else f"{round(g[y]['supply']) - round(g[y]['need']):+,}" for y in ys))
    print('Pre-tax return          | ' + f('ret', lambda v: f'{v*100:.1f}%'))
    print('Five-company D&A        | ' + f('da5', lambda v: f'{v:,.0f}'))


def sensitivities(path='base'):
    cases = [('Central', {}), ('r = 8%', dict(r=.08)), ('r = 12%', dict(r=.12)),
             ('Cash cost 35%', dict(cost=.35)), ('Cash cost 45%', dict(cost=.45)),
             ('Short life 6.0 years', dict(life_s=6.0)), ('Short life 4.0 years (economic)', dict(life_s=4.0)),
             ('Short-lived share 75%', dict(s=.75)), ('Strict: no Meta uplift', dict(meta=False)),
             ('E2 at the Bull row (+45% / +32% / +22%)', dict(e2='bull'))]
    print(f"\nSensitivities on K1 '{path}': coverage 2028 / 2029 | revenue needed 2029 | supply 2029 | pre-tax return 2028 / 2029")
    for lab, kw in cases:
        g = gauge(path, **kw)
        print(f"  {lab:40s} {g[2028]['cover']*100:.0f}% / {g[2029]['cover']*100:.0f}% | {g[2029]['need']:,.0f} | "
              f"{g[2029]['supply']:,.0f} | {g[2028]['ret']*100:.1f}% / {g[2029]['ret']*100:.1f}%")


def other_paths():
    print('\nOther K1 paths (supply on the Base E-paths): K1 2027 / 28 / 29 | coverage 2027 / 28 / 29 / 2030 | pre-tax return 2028 / 29 / 2030')
    for name in ('base', 'taper', 'flat', 'hold', 'bear', 'bull'):
        g = gauge(name); k = PATHS[name]
        print(f"  {name:6s} {k[2027]:,} / {k[2028]:,} / {k[2029]:,} | "
              + ' / '.join(f"{g[y]['cover']*100:.0f}" for y in (2027, 2028, 2029, 2030)) + '% | '
              + ' / '.join(f"{g[y]['ret']*100:.1f}" for y in (2028, 2029, 2030)) + '%')


if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        for a in args:
            table(a)
    else:
        table('base'); sensitivities('base'); other_paths()
