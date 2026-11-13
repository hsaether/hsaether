# NVIDIA (docs/nvda-analysis.md) -- version 1.6, 13 Nov 2026: vendor-financing CASCADE stress test (user, 13 Nov).
# Reported next to Base and Bear; never Base. Built on v15.py (model unchanged; price re-mark only).
# Run from this folder: py v16_cascade.py [price]   (default 166.19 = 12 Nov close)
# Steps (cumulative from Base): 1 trigger (no new discretionary funding from 2028; direct-support revenue lost)
# -> 2 funded neoclouds fail (buy-backs, land/power/shell guarantees, leases called or stranded; bad debt)
# -> 3 stakes (neoclouds to zero, OpenAI x0.4) and SB Energy guaranty phases called (wrong-way)
# -> 4 volume (the whole funded share of data-center demand lost, K1 backfill only where supply-limited)
# -> 5 price and margin (gross margin pinned at the test level incl. excess-purchase charges; unit cost at Base)
# -> 6 exit P/E 13 (Bear's), 6b exit 11.
# Also: H2-2027 variant, grid GM 60/65/70 x funded share 30/39/45 (start 2028 and H2 2027), cost of the alternative.
# All parameters are [A] own assumptions unless noted; standard library only.
import sys
import v15 as m

P = float(sys.argv[1]) if len(sys.argv) > 1 else 166.19
pct = lambda x: f"{x*100:.1f}%"
SH = m.SH
TAX = 0.17
GM0 = 0.75            # Base gross margin [A] (Q2 FY27 75.0% [F]; Q3 guide 74.0% [F])
DC = 0.925            # data center share of revenue (Q2 FY27 89.0 / 96.2 [F])
B = m.BASE
R_B = m.base_rev(B) + [B['eps30'] * SH / 0.545]           # Base revenue 2027-30 ($bn)
NI_B = [e * SH for e in B['eps']] + [B['eps30'] * SH]
OPEX = [GM0 * r - ni / (1 - TAX) for r, ni in zip(R_B, NI_B)]  # implied opex net of other income (fixed)
ST_EXIT = (m.ST26_BOOK + m.REMARK + sum(B['stakes'])) # stakes at book at exit, $bn (129.4)


def pl(i, v, p, E):
    """Cascade P&L for year index i (0=2027 .. 3=2030): volume loss v, price cut p, charges E (in COGS)."""
    R = R_B[i]
    rev = R * (1 - v) * (1 - p)
    cogs = (1 - GM0) * R * (1 - v) + E
    ni = (rev - cogs - OPEX[i]) * (1 - TAX)
    return dict(rev=rev, gm=(rev - cogs) / rev, ni=ni, eps=ni / SH, cogs=cogs)


def price_for_gm(i, v, E, gm):
    """Price cut p on all sales that gives gross margin gm (incl. charges E), unit cost at Base."""
    R = R_B[i]
    cogs = (1 - GM0) * R * (1 - v) + E
    return 1 - cogs / ((1 - gm) * R * (1 - v))


CENTRAL = dict(
    f=0.39,                       # funded share of data-center demand lost (demand-dependence table: 30-45%)
    back=[None, 0.25, 0.10, 0.10],  # K1 backfill of the lost volume (2028: rationed 2027 orders; then surplus)
    gm=[None, 0.62, 0.62],        # gross margin test level 2028-29 (2030: 2029 price held, charges end)
    E=[0, 20.0, 8.0, 0],          # excess-purchase and inventory charges in COGS, $bn
    direct=10.0,                  # direct-support revenue lost from the trigger year ($bn a year; sensitivity (a))
    # step 2: cross-funding calls, $bn (cash in window; exit = liability left at exit, PV)
    buyback=[0, 6.0, 5.25], buyback_exit=11.25,   # 8 / 7 then 6 + 9, re-rented at 25%
    lps=[0, 2.8, 0],                               # land/power/shell 3.5 less 0.7 escrow, all called
    lease=[0, 1.0, 1.0], lease_exit=7.7,           # 20 over 15 years, sublet 25%
    baddebt=[0, 5.0, 0],                           # receivables of failed buyers
    # step 3: stakes and SB Energy
    neo_stakes=12.0, openai=30.0, openai_f=0.4,
    sbe=[0, 2.5, 5.0], sbe_exit=10.0,              # two phases x ~11.7 = 23.4 called, re-let 25% -> 17.5
    capex=[13, 11, 11], pe=13,
    start=2028,
)


def variant_h2_2027(c):
    c = dict(c)
    c.update(start=2027, back=[0.5, 0.10, 0.10, 0.10], E=[10.0, 15.0, 3.0, 0],
             buyback=[2.25, 6.0, 5.25], lps=[2.8, 0, 0], lease=[0.5, 1.0, 1.0], baddebt=[5.0, 0, 0],
             capex=[12, 11, 11])
    return c


def scen(c, step=6, pe=None, wc=0.25):
    """Scenario dict for m.build after cumulative step `step` (0 = Base)."""
    s = dict(B, name='Cascade', wc=wc)
    eps = list(B['eps']); eps30 = B['eps30']; rev = list(R_B[:3])
    charge = [0.0, 0.0, 0.0]; exitliab = 0.0; sf = 1.0
    h2 = c['start'] == 2027
    info = {}
    if step >= 1:   # trigger: direct-support revenue lost (H2 2027: half of a year in 2027)
        vs = [(0.5 if h2 else 0.0) * c['direct'] / R_B[0]] + [c['direct'] / R_B[i] for i in (1, 2, 3)]
        out = [pl(i, vs[i], 0, 0) for i in range(4)]
        eps = [o['eps'] for o in out[:3]]; eps30 = out[3]['eps']; rev = [o['rev'] for o in out[:3]]
        s['stakes'] = [B['stakes'][0], B['stakes'][1], B['stakes'][2]]   # Base already funds only commitments
    if step >= 2:
        charge = [c['buyback'][i] + c['lps'][i] + c['lease'][i] + c['baddebt'][i] for i in range(3)]
        exitliab = c['buyback_exit'] + c['lease_exit']
    if step >= 3:
        charge = [charge[i] + c['sbe'][i] for i in range(3)]
        exitliab += c['sbe_exit']
        loss = c['neo_stakes'] + c['openai'] * (1 - c['openai_f'])
        sf = (ST_EXIT - loss) / ST_EXIT
        info['stake_loss'] = loss
    if step >= 4:
        f = c['f']
        b = list(c['back'])
        v = [(0.5 * f * DC * (1 - b[0])) if h2 else c['direct'] / R_B[0] * 0] + [f * DC * (1 - b[i]) for i in (1, 2, 3)]
        if not h2:
            v[0] = 0.0
        info['v'] = v
        out = [pl(i, v[i], 0, 0) for i in range(4)]
        eps = [o['eps'] for o in out[:3]]; eps30 = out[3]['eps']; rev = [o['rev'] for o in out[:3]]
        s['capex'] = c['capex']
    if step >= 5:
        gms = list(c['gm'])
        if h2:
            gms[0] = 0.5 * GM0 + 0.5 * c['gm'][1]
        else:
            gms[0] = None
        p = [0.0] * 4
        for i in range(3):
            if gms[i] is not None:
                p[i] = price_for_gm(i, v[i], c['E'][i], gms[i])
        p[3] = p[2]
        out = [pl(i, v[i], p[i], c['E'][i]) for i in range(4)]
        eps = [o['eps'] for o in out[:3]]; eps30 = out[3]['eps']; rev = [o['rev'] for o in out[:3]]
        info['p'] = p; info['out'] = out
    if step >= 6:
        s['pe'] = c['pe'] if pe is None else pe
    s.update(eps=eps, eps30=eps30, rev=rev, charge=charge, exitliab=exitliab, sf=sf, sfg=[1, 1, sf])
    return s, info


def res(s):
    r = m.build(s, P)
    cap = (sum(r['D']) + r['VT']) / P - 1
    return r, cap


if __name__ == '__main__':
    print(f"P = {P}; Base revenue 2027-30 {[round(x,1) for x in R_B]}; implied opex {[round(x,1) for x in OPEX]}; stakes at exit {ST_EXIT:.1f}")
    base = m.build(B, P)
    print(f"Base: {pct(base['irr'])} P_k {base['pk']:.1f}")
    bear = m.build(m.BEAR, P)
    print(f"Bear: {pct(bear['irr'])} P_k {bear['pk']:.1f} cap {(sum(bear['D'])+bear['VT'])/P-1:+.1%}")
    labels = ['Base', '1 trigger: direct support lost', '2 neoclouds fail: calls, leases, bad debt',
              '3 stakes and SB Energy', '4 volume: funded share lost', '5 price and margin (GM 62%)', '6 exit P/E 13']
    for name, c in [('From 2028', CENTRAL), ('H2 2027', variant_h2_2027(CENTRAL))]:
        print(f"== Steps, {name} ==")
        for k in range(7):
            s, info = scen(c, k)
            r, cap = res(s)
            print(f"  {labels[k]}: IRR {pct(r['irr'])} P_k {r['pk']:.1f} margin {r['pk']/P-1:+.1%} VT {r['VT']:.1f} cap {cap:+.1%} "
                  f"EPS {[round(x,2) for x in s['eps']]} e30 {s['eps30']:.2f} NC/sh {[round(x,2) for x in r['NC']]}")
        s, info = scen(c, 6, pe=11); r, cap = res(s)
        print(f"  6b exit P/E 11: IRR {pct(r['irr'])} P_k {r['pk']:.1f} VT {r['VT']:.1f} cap {cap:+.1%}")
        s, info = scen(c, 6); r, cap = res(s)
        print(f"  final: D {[round(x,2) for x in r['D']]} sumD {sum(r['D']):.2f} VT {r['VT']:.1f} NC $bn {[round(x*SH,1) for x in r['NC']]} "
              f"FCF {[round(x,1) for x in r['FCF']]} NI {[round(x,1) for x in r['NI']]} REV {[round(x,1) for x in r['REV']]} "
              f"charges {s['charge']} exitliab {s['exitliab']:.1f} sf {s['sf']:.3f} stake loss {info.get('stake_loss')}")
        print(f"  v {[round(x,4) for x in info['v']]} p {[round(x,4) for x in info['p']]} GM {[round(o['gm'],4) for o in info['out']]} "
              f"rev {[round(o['rev'],1) for o in info['out']]} eps {[round(o['eps'],2) for o in info['out']]}")
        # NOK: no recession -> Equity BBB Base NOK path (flat) -> same as USD
        print(f"  WC release halved: {pct(res(scen(c, 6, wc=0.125)[0])[0]['irr'])}")

    # P&L decomposition, central, 2028-2030
    print("== P&L decomposition, central (from 2028) ==")
    s, info = scen(CENTRAL, 6)
    v, p, out = info['v'], info['p'], info['out']
    for i, yr in [(1, 2028), (2, 2029), (3, 2030)]:
        R = R_B[i]; n = NI_B[i] / R
        vol = n * R * v[i] / SH
        opl = (1 - TAX) * OPEX[i] * v[i] / SH
        prc = (1 - TAX) * R * (1 - v[i]) * p[i] / SH
        chg = (1 - TAX) * CENTRAL['E'][i] / SH
        eb = NI_B[i] / SH
        print(f"  {yr}: Base rev {R:.1f} EPS {eb:.2f}; volume v {v[i]:.1%} -> rev {R*(1-v[i]):.1f}; price p {p[i]:.1%} -> rev {out[i]['rev']:.1f} "
              f"({out[i]['rev']/R-1:+.1%}); GM {out[i]['gm']:.1%}; charges {CENTRAL['E'][i]}; opex {OPEX[i]:.1f}; NI {out[i]['ni']:.1f}; EPS {out[i]['eps']:.2f} ({out[i]['eps']/eb-1:+.1%})")
        print(f"     EPS bridge: volume at Base net margin {-vol:+.2f}; operating leverage (opex kept) {-opl:+.2f}; price {-prc:+.2f}; charges {-chg:+.2f}; "
              f"check {eb - vol - opl - prc - chg:.2f}; GM before charges {1 - (1-GM0)/(1-p[i]):.1%}")
    # step damage, central
    print("== Grid: GM x funded share (exit 13) ==")
    for name, base_c in [('2028', CENTRAL), ('H2 2027', variant_h2_2027(CENTRAL))]:
        for f in [0.30, 0.39, 0.45]:
            row = []
            for gm in [0.60, 0.65, 0.70]:
                c = dict(base_c, f=f, gm=[None, gm, gm])
                s, info = scen(c, 6); r, cap = res(s)
                row.append(f"{pct(r['irr'])} (${r['pk']:.0f}; p28 {info['p'][1]:.0%})")
            print(f"  start {name} f {f:.0%}: GM 60/65/70 -> {row}")
    # Bear GM range for reference: what GM would give Bear-like
    print("== Gross margin at which the cascade equals the Bear IRR, central volume ==")
    lo, hi = 0.55, 0.80
    for _ in range(60):
        mid = (lo + hi) / 2
        c = dict(CENTRAL, gm=[None, mid, mid]); r, _ = res(scen(c, 6)[0])
        if r['irr'] < bear['irr']:
            lo = mid
        else:
            hi = mid
    print(f"  GM {mid:.1%}")
    print("== Volume only, Base GM (no price leg), exit 13 / 17 ==")
    for pe in [13, 17]:
        s, _ = scen(CENTRAL, 4); s['pe'] = pe; r, cap = res(s)
        print(f"  exit {pe}: {pct(r['irr'])} P_k {r['pk']:.1f}")
    s, _ = scen(CENTRAL, 5); s['pe'] = 17; r, cap = res(s)
    print(f"  price leg at exit 17: {pct(r['irr'])} P_k {r['pk']:.1f}")
    print("== Robustness (central, exit 13) ==")
    # (i) order: price and margin without the volume step (steps 1-3, 5, 6; v = 0)
    s, info = scen(CENTRAL, 3)
    p0 = [0.0] + [price_for_gm(i, 0.0, CENTRAL['E'][i], 0.62) for i in (1, 2)]
    p0.append(p0[2])
    o = [pl(i, 0.0, p0[i], CENTRAL['E'][i]) for i in range(4)]
    s2 = dict(s, eps=[o[i]['eps'] for i in range(3)], eps30=o[3]['eps'], rev=[o[i]['rev'] for i in range(3)], pe=13)
    r, _ = res(s2)
    print(f"  price and margin first (no volume loss): IRR {pct(r['irr'])} P_k {r['pk']:.1f} (p {[round(x,3) for x in p0]})")
    # (ii) K1 keeps its dollar budget (AI BBB K1 path): price cut on K1 sales comes back as units; k = K1 share of remaining sales
    k = 0.75
    s, info = scen(CENTRAL, 6)
    v, p = info['v'], info['p']
    eps_k1 = []
    for i in range(4):
        R = R_B[i]; S = R * (1 - v[i])
        rev = k * S + (1 - k) * S * (1 - p[i])
        cogs = (1 - GM0) * k * S / (1 - p[i]) + (1 - GM0) * (1 - k) * S + CENTRAL['E'][i]
        ni = (rev - cogs - OPEX[i]) * (1 - TAX)
        eps_k1.append((ni / SH, rev, (rev - cogs) / rev))
    s3 = dict(s, eps=[e[0] for e in eps_k1[:3]], eps30=eps_k1[3][0], rev=[e[1] for e in eps_k1[:3]])
    r, _ = res(s3)
    print(f"  K1 holds its dollar budget (k {k:.0%}): IRR {pct(r['irr'])} P_k {r['pk']:.1f}; GM {[round(e[2],3) for e in eps_k1]}; rev {[round(e[1]) for e in eps_k1]}")
    # (iii) exit year: surplus clears by 2030 (price leg halved in 2030)
    o30 = pl(3, v[3], p[3] / 2, 0)
    s4 = dict(s, eps30=o30['eps'])
    r, _ = res(s4)
    print(f"  2030 price leg halved (GM {o30['gm']:.1%}, EPS {o30['eps']:.2f}): IRR {pct(r['irr'])} P_k {r['pk']:.1f}")
    # (iv) charges: none / doubled
    for Ef in [0.0, 2.0]:
        c = dict(CENTRAL, E=[e * Ef for e in CENTRAL['E']])
        r, _ = res(scen(c, 6)[0])
        print(f"  charges x{Ef}: IRR {pct(r['irr'])} P_k {r['pk']:.1f}")
    # (v) OpenAI factor 0 / 1; SB Energy none / all 4.25 GW (~3.5 x)
    for fo in [0.0, 1.0]:
        r, _ = res(scen(dict(CENTRAL, openai_f=fo), 6)[0]); print(f"  OpenAI stake x{fo}: IRR {pct(r['irr'])} P_k {r['pk']:.1f}")
    # balance sheet: net cash after the exit liabilities, gross cash (notes 33.5)
    s, info = scen(CENTRAL, 6); r, _ = res(s)
    nc = [x * SH for x in r['NC']]
    print(f"  net cash $bn {[round(x,1) for x in nc]}; after exit liabilities {nc[-1]-s['exitliab']:.1f}; gross cash ~ {[round(x+33.5,1) for x in nc]}")
    T = r['T']; sumD = sum(r['D'])
    print(f"  d/g: d {sumD/T/P*100:.1f} g {((r['VT']/P)**(1/T)-1)*100:.1f} c {(r['irr']-sumD/T/P-((r['VT']/P)**(1/T)-1))*100:+.1f}")
    print("== Cost of the alternative (Base kept: NVIDIA funds the buyers; cash out 2028-29, recovery at exit) ==")
    for X in [15, 30, 60, 100]:
        for rec in [1.0, 0.5, 0.0]:
            s = dict(B, charge=[0, X, X], exitliab=-rec * 2 * X)
            r = m.build(s, P)
            perm = dict(s, eps30=B['eps30'] - X * (1 - rec) / SH)
            rp = m.build(perm, P)
            print(f"  X {X}/yr rec {rec:.0%}: Base IRR {pct(r['irr'])} P_k {r['pk']:.1f} | permanent (loss capitalised at 17x) {pct(rp['irr'])} P_k {rp['pk']:.1f}"
                  f" | FCF 2028 {r['FCF'][1]:.0f} ({X/327.2:.0%} of Base)")

    def alt(X, rec=0.5, perm=True):
        s = dict(B, charge=[0, X, X], exitliab=-rec * 2 * X)
        if perm:
            s['eps30'] = B['eps30'] - X * (1 - rec) / SH
        return m.build(s, P)['irr']
    print(f"  X at which a permanent program gives Base = k: half lost {m.solve(lambda x: alt(x), 0.12, 0, 300):.0f}; all lost {m.solve(lambda x: alt(x, 0.0), 0.12, 0, 300):.0f}")
    s = dict(B, charge=[0, 30, 45], exitliab=-0.5 * 75, eps30=B['eps30'] - 67.5 * 0.5 / SH)
    r = m.build(s, P)
    print(f"  growing need (Minsky): 30 -> 45 -> 67.5 a year after exit, half lost: {pct(r['irr'])} P_k {r['pk']:.1f}")
