# AI Market BBB — layer baskets, IAF index-level build (USD and NOK). Version 2.1 (run of 11 Nov 2026, K1 re-set).
# Prices: Yahoo close Fri 6 Nov 2026 (US, Europe, Korea; Update 7, not re-marked). Consensus: Yahoo earningsTrend 7 Nov 2026.
# K1D (11 Nov, skill 2026-11-11.2): K1 Base 2028-29 1,250 / 1,300 -> 1,170 / 1,170 (K1 capex cycle; review
# docs/review-ai-k1-sustainability.md, Option D). Knock-on: H1 and H4 Base revenue and EPS 2028-30, E cash conversion.
# U7 (7 Nov): inputs only (price re-mark; Equity BBB 6 Nov NOK path; stub 54 days); no path change.
# U6 (1 Nov): inputs only (no path change); new output: the price-implied H2 memory path (Memory cycle section).
# U5 (29 Oct): E Base 2027 .97 -> .92 (company check: MSFT v3, GOOGL v2, AMZN v1; blend .92, gap -0.05).
# 2.1 (22 Oct): E layer recalibrated with the Amazon analysis (switch AMZN: E Bear/Bull paths and cash
# conversion); USD/NOK path from the 17/18 Oct Equity BBB; Bear-cap and exit cross-check diagnostics.
# Changes from version 1 (16 Oct): (1) retained cash counted once: each year the layer converts
# conv x EPS into free cash after growth capex (net of dilution offsets); payout x EPS is paid as
# D_t and the rest (conv - payout) x EPS accumulates at face value into V_t and V_T (negative =
# net debt build). (2) Fiscal-year consensus calendarised by months (NVDA by calendar quarters,
# docs/nvda-analysis.md; MU by calendar quarters, docs/mu-analysis.md); ASML's consensus is in EUR
# and is converted to USD. (3) Bear paths reconciled to revenue (H1, H3, H4) and the E layer moved
# to the Microsoft and Alphabet company analyses where the gap is >= 0.05.
# Switches (for the attribution in the change log): CAL, RET, PATH, AMZN, U5, K1D; BEARCAP = diagnostic
# (Bear P/E capped at today's). Run: py -I model.py [CAL RET PATH AMZN U5 K1D] [BEARCAP]
import json, sys
ARGS = set(sys.argv[1:]) or {'CAL', 'RET', 'PATH', 'AMZN', 'U5', 'K1D'}
if ARGS == {'BEARCAP'}: ARGS = {'CAL', 'RET', 'PATH', 'AMZN', 'U5', 'K1D', 'BEARCAP'}
CAL, RET, PATH, AMZN, U5, BEARCAP = 'CAL' in ARGS, 'RET' in ARGS, 'PATH' in ARGS, 'AMZN' in ARGS, 'U5' in ARGS, 'BEARCAP' in ARGS
K1D = 'K1D' in ARGS
KRW = 1363.65; EUR = 1.11433   # Yahoo KRW=X, EURUSD=X, final quote Fri 6 Nov 2026 (7 Nov run)
q = {r['symbol']: r for r in json.load(open('data/q.json'))}
def mc(s):
    r = q[s]; m = r.get('marketCap') or 0
    if r.get('currency') == 'KRW': m /= KRW
    if r.get('currency') == 'EUR': m *= EUR
    return m / 1e9
# CY27 consensus EPS (Yahoo earningsTrend 7 Nov 2026), in the price currency of each line.
# Old convention (version 1): next fiscal year taken as CY27 for FY Jan names, ORCL FY mean,
# ASML in EUR read as USD. Calendarised (version 2): by months, or by quarters where a company
# analysis did so.
cal = dict(
 NVDA=15.21,                                   # by calendar quarters (nvda-analysis); FY Jan-28 15.91
 AMD=16.77999, AVGO=19.46507,                  # 7 Nov: AMD 15.94 -> 16.78 after its Q3 (3 Nov). AVGO FY Oct-27 (no FY28 consensus; understates CY27 by up to ~5%)
 MRVL=4.2224/12 + 7.34277*11/12,               # FY Jan: 1/12 FY Jan-27 + 11/12 FY Jan-28
 MU=191.8,                                     # by calendar quarters (mu-analysis v2, 22 Oct: FY27 176.50, FY28 206.85); 7 Nov FY27 176.50, FY28 207.76 (+0.15% on CY27, kept)
 **{'000660.KS': 529348.1, '005930.KS': 77323.65},   # 7 Nov: SK hynix 527,157 -> 529,348 (38), Samsung 75,627 -> 77,324 (33)
 TSM=23.38529, ASML=56.43418*EUR,              # ASML consensus in EUR -> USD (7 Nov 55.93 -> 56.43)
 AMAT=18.55645, LRCX=(9.65024 + 12.23633)/2,   # AMAT FY Oct-27; LRCX FY Jun: 1/2 + 1/2
 ANET=5.64382, VRT=9.84233, ETN=16.29264,      # 7 Nov: ANET 5.22 -> 5.64 after its Q3 (3 Nov; 2027 guide +38-40%)
 MSFT=(20.00388 + 24.17933)/2,                 # FY Jun: 1/2 + 1/2
 GOOGL=14.95356, AMZN=10.6718, META=33.92516,
 ORCL=8.14185*5/12 + 11.05442*7/12,            # FY May: 5/12 FY May-27 + 7/12 FY May-28
 NOW=4.8023, CRM=16.75484/12 + 16.01523*11/12, ADBE=27.429, PLTR=2.48939,
 **{'SAP.DE': 8.47518}, INTU=23.81046*7/12 + 26.94382*5/12,
 SNOW=2.22364/12 + 3.02718*11/12, DDOG=3.07031)
old = dict(cal, NVDA=15.9146, MRVL=7.34277, CRM=16.01523, SNOW=3.02718,
           ORCL=(8.14185 + 11.05442)/2, ASML=56.43418)
eps27 = cal if CAL else old
# CY26 (display only: consensus growth CY26 -> CY27)
eps26 = {'NVDA': 4.77/12 + 9.31242*11/12, 'AMD': 8.06686, 'AVGO': 11.66568, 'TSM': 17.50426, 'MU': 118.9,
         '000660.KS': 359088.7, 'ANET': 4.28216, 'VRT': 7.18808, 'ETN': 13.68423,
         'MSFT': (17.28 + 20.00388)/2, 'META': 29.12343, 'ORCL': 7.63*5/12 + 8.14185*7/12,
         'NOW': 3.95455, 'CRM': 12.52/12 + 16.75484*11/12, 'ADBE': 24.47791, 'PLTR': 1.70215,
         'SAP.DE': 7.1569, 'SNOW': 1.25/12 + 2.22364*11/12, 'DDOG': 2.68786}
# Layer: members, EPS 2027/28/29/2030 norm (CY27 consensus = 1), exit P/E Bear/Base/Bull, payout,
# cash conversion (free cash after growth capex and dilution offsets / EPS) 2027/28/29 per scenario.
P1 = {  # version 1 paths
 'H1': dict(Bear=(.70,.60,.70,.75), Base=(.92,.98,1.00,.97), Bull=(1.0,1.15,1.25,1.30)),
 'H2': dict(Bear=(.60,.30,.25,.25), Base=(.90,.60,.40,.35), Bull=(1.0,.80,.55,.45)),
 'H3': dict(Bear=(.80,.75,.85,.92), Base=(.95,1.03,1.10,1.16), Bull=(1.0,1.15,1.28,1.40)),
 'H4': dict(Bear=(.75,.65,.75,.85), Base=(.95,1.02,1.07,1.11), Bull=(1.0,1.12,1.22,1.30)),
 'E':  dict(Bear=(.88,.88,.97,1.05), Base=(.97,1.07,1.17,1.27), Bull=(1.0,1.13,1.27,1.41)),
 'T':  dict(Bear=(.88,.85,.93,1.00), Base=(.95,1.03,1.11,1.19), Bull=(1.0,1.10,1.20,1.30))}
P2 = {k: dict(v) for k, v in P1.items()}  # version 2 paths
P2['H1']['Bear'] = (.68, .50, .53, .57)   # revenue-consistent (NVIDIA margin build, nvda-analysis)
P2['H3']['Bear'] = (.76, .63, .67, .71)   # revenue-consistent (TSMC margin build, tsm-analysis)
P2['H4']['Bear'] = (.75, .54, .56, .65)   # revenue -20% in 2028 at ~1.4x operating leverage, flat 2029 [A]
P2['E']['Bear']  = (.82, .80, .88, .96)   # MSFT + GOOGL company Bears for their 62% of the basket
P2['E']['Bull']  = (1.0, 1.13, 1.27, 1.47) # 2030 only (+0.06); 2028-29 gaps < 0.05
if AMZN:  # 22 Oct: MSFT, GOOGL, AMZN company paths for their 83% of E, the old layer path for META and ORCL
    P2['E'] = dict(P2['E'], Bear=(.82, .75, .82, .91), Bull=(1.0, 1.19, 1.37, 1.54))
if U5:  # 29 Oct: E Base 2027 on the company blend (MSFT v3 .96, GOOGL v2 .83, AMZN v1 .95, rest .97 -> .92); 2028-30 gaps < 0.05
    P2['E'] = dict(P2['E'], Base=(.92, 1.07, 1.17, 1.27))
# K1D (11 Nov 2026): K1 Base 2027-29 1,120 / 1,250 / 1,300 -> 1,120 / 1,170 / 1,170 (2030 = 2029). Rows set from K1:
#  - H1 and H4 Base revenue held at their ratio to K1 (Base keeps the non-K1 share; SKILL Step 2). H4 Base growth
#    tracked K1 growth in 2028-29 (+10% / +4% against +12% / +4%), so it takes the same ratio as H1;
#  - their Base EPS 2028-30 interpolated between the Base and Bear paths by the revenue gap (the layer's own
#    revenue-to-EPS link, as in docs/review-ai-h1-non-k1-funding.md 4.4), from the unrounded revenue, to two decimals;
#  - E cash conversion (below): the five's capex is K1, so c rises by 0.86 x the capex cut (after the cash-tax
#    effect of expensing) / the E basket's earnings on its Base path.
#  H2 is not moved (the memory Base already assumes AI capex digestion in 2028). H3's knock-on (20-30% of the H1
#  change) is below the minimum change and is noted, not applied. Bear and Bull K1 are unchanged.
K1_OLD = (1120, 1250, 1300); K1_NEW = (1120, 1170, 1170)
K1D_SET = dict(H1=(.92, .91, .88, .87), H4=(.95, .94, .94, .99), Ec=(-.20, .11, .36))  # as published 11 Nov; the
# derivation below is printed beside them as a check (a consensus refresh must not move a published path)
K1_REV = {'H1': dict(Base=(730, 800, 825), Bear=(585, 470, 490)),     # USD bn
          'H4': dict(Base=(125, 138, 144), Bear=(110, 88, 88))}       # index, 2026 = 100
def k1_knockon(key):
    rb = K1_REV[key]['Base'] + K1_REV[key]['Base'][2:]; rr = K1_REV[key]['Bear'] + K1_REV[key]['Bear'][2:]
    ratio = [n/o for n, o in zip(K1_NEW, K1_OLD)]; ratio.append(ratio[2])
    rn = [rb[i]*ratio[i] for i in range(4)]
    eb, er = P2[key]['Base'], P2[key]['Bear']
    eps = tuple(round(eb[i] - (eb[i] - er[i])*(rb[i] - rn[i])/(rb[i] - rr[i]), 2) for i in range(4))
    return rn, eps
if K1D:
    for _k in ('H1', 'H4'):
        _rn, _e = k1_knockon(_k)
        P2[_k] = dict(P2[_k], Base=K1D_SET[_k])
        print(f"K1D {_k}: Base revenue 2027-30 {' / '.join(f'{x:.1f}' for x in _rn)}; Base EPS derived {' / '.join(f'{x:.2f}' for x in _e)}, set {' / '.join(f'{x:.2f}' for x in K1D_SET[_k])}")
PATHS = P2 if PATH else P1
CONV = {  # [A], calibrated on the company analyses' FCF after growth capex
 'H1': dict(Bear=(.85,.95,.95), Base=(.80,.90,.90), Bull=(.75,.85,.90)),   # NVDA .77/.95/.97
 'H2': dict(Bear=(.70,.75,.70), Base=(.70,.65,.60), Bull=(.70,.70,.55)),   # MU .71/.67/.60
 'H3': dict(Bear=(.75,.90,.95), Base=(.75,.80,.82), Bull=(.70,.72,.78)),   # TSM .63/.68/.74 (60%), equipment ~.95
 'H4': dict(Bear=(.90,.90,.90), Base=(.90,.90,.90), Bull=(.90,.90,.90)),   # asset-light, no analysis
 'E':  dict(Bear=(.00,.40,.60), Base=(-.10,.10,.30), Bull=(-.20,-.10,.10)),# MSFT .22/.34/.45, GOOGL -.30/-.14/.06 (after withholding)
 'T':  dict(Bear=(.80,.80,.80), Base=(.80,.80,.80), Bull=(.80,.80,.80))}   # non-GAAP EPS; SBC dilution offset
if AMZN:  # AMZN -.48/-.16/.11 (Bear -.58/.00/.30; Bull -.75/-.52/-.22); META assumed like GOOGL (Q3-26 FCF -2.1bn)
    CONV['E'] = dict(Bear=(-.10,.30,.50), Base=(-.20,.00,.20), Bull=(-.30,-.20,.00))
if K1D:  # E = the five K1 names: their capex is K1. c(Base) += 0.86 x (K1 old - K1 new) / (E earnings CY27 x Base path)
    _earn27 = sum(mc(s)/(q[s]['regularMarketPrice']/eps27[s]) for s in ['MSFT','GOOGL','AMZN','META','ORCL'])
    _cb = CONV['E']['Base']; _eb = PATHS['E']['Base']
    _c = tuple(round(_cb[k] + .86*(K1_OLD[k] - K1_NEW[k])/(_earn27*_eb[k]), 2) for k in range(3))
    CONV['E'] = dict(CONV['E'], Base=K1D_SET['Ec'])
    print(f"K1D E: CY27 earnings {_earn27:.1f}bn; Base cash conversion derived {' / '.join(f'{x:+.2f}' for x in _c)}, set {' / '.join(f'{x:+.2f}' for x in K1D_SET['Ec'])}")
L = {
 'H1': ('H1 Compute (NVDA AMD AVGO MRVL)', ['NVDA','AMD','AVGO','MRVL'], (13,17,19), .25),
 'H2': ('H2 Memory (MU SK hynix Samsung)', ['MU','000660.KS','005930.KS'], (8,10,11), .15),
 'H3': ('H3 Foundry and equipment (TSM ASML AMAT LRCX)', ['TSM','ASML','AMAT','LRCX'], (14,18,21), .45),
 'H4': ('H4 Networking and DC infrastructure (ANET VRT ETN)', ['ANET','VRT','ETN'], (15,20,24), .35),
 'E':  ('E Engines and cloud platforms (MSFT GOOGL AMZN META ORCL)', ['MSFT','GOOGL','AMZN','META','ORCL'], (17,21,23.5), .34),
 'T':  ('T Tools and application software (NOW CRM ADBE PLTR SAP INTU SNOW DDOG)', ['NOW','CRM','ADBE','PLTR','SAP.DE','INTU','SNOW','DDOG'], (15,20,24), .45)}
FX = dict(Bear=(10.41,10.14,10.14), Base=(9.29,9.29,9.29), Bull=(9.02,9.02,9.02)); FX0 = 9.29  # Equity BBB 6 Nov (spot 9.29; relative moves +12/+9/+9%, -3% unchanged)
NIB = 4.38; T0 = 54/365  # 7 Nov -> 31 Dec (prices 6 Nov); NIBOR window from HY BBB 5 Nov (path unchanged)
def irr(fl):
    lo, hi = -0.9, 2.0
    for _ in range(200):
        m = (lo + hi)/2; v = sum(c/(1 + m)**t for t, c in fl)
        lo, hi = (m, hi) if v > 0 else (lo, m)
    return m
def build(e, P, ex, po, cv, bear):
    """Year-end values V (per unit of CY27 consensus EPS) and payouts D for 2027-29."""
    if bear and BEARCAP: ex = min(ex, P)   # diagnostic: no re-rating above today's multiple in the Bear
    pe = [ex]*3 if bear else [P + (ex - P)*k/3 for k in (1, 2, 3)]
    D = [po*e[k] for k in range(3)]
    C, cum = [], 0.0
    for k in range(3):
        cum += (cv[k] - po)*e[k] if RET else 0.0
        C.append(cum)
    V = [pe[k]*e[k + 1] + C[k] for k in range(3)]
    return V, D
out = {}
for key, (name, mem, PE, po) in L.items():
    W = {s: mc(s) for s in mem}; Wt = sum(W.values())
    pe27 = Wt/sum(W[s]/(q[s]['regularMarketPrice']/eps27[s]) for s in mem)
    g2627 = sum(W[s]*(eps27[s]/eps26[s] - 1) for s in mem if s in eps26)/sum(W[s] for s in mem if s in eps26)
    res = {}
    for i, sc in enumerate(['Bear', 'Base', 'Bull']):
        e = PATHS[key][sc]; V, D = build(e, pe27, PE[i], po, CONV[key][sc], sc == 'Bear')
        for cur in ('USD', 'NOK'):
            f = [x/FX0 for x in FX[sc]] if cur == 'NOK' else [1, 1, 1]
            fl = [(0, -pe27)] + [(T0 + k + 0.5, D[k]*f[k]) for k in range(3)] + [(T0 + 3, V[2]*f[2])]
            res[(sc, cur)] = irr(fl)*100
            if cur == 'NOK': res[(sc, 'r27')] = ((V[0] + D[0])*f[0]/pe27 - 1)*100
        if sc == 'Base':
            f = [x/FX0 for x in FX[sc]]
            pk = sum(D[k]*f[k]/1.12**(T0 + k + 0.5) for k in range(3)) + V[2]*f[2]/1.12**(T0 + 3)
            res['Pk'] = pk; res['mos'] = (pk/pe27 - 1)*100
    E_ = res[('Base', 'NOK')] - NIB; R_ = res[('Base', 'r27')] - res[('Bear', 'r27')]
    out[key] = dict(name=name, mcap=Wt, pe27=pe27, g2627=g2627*100,
                    **{f'{k[0]}_{k[1]}': v for k, v in res.items() if isinstance(k, tuple)},
                    Pk=res['Pk'], mos=res['mos'], E=E_, R=R_, ER=E_/R_)
# implied growth: constant EPS growth after 2027 (from the Base 2027 level) that gives 12% NOK at the Base exit P/E
def irr_g(key, g):
    name, mem, PE, po = L[key]; e0 = PATHS[key]['Base'][0]
    e = [e0, e0*(1 + g), e0*(1 + g)**2, e0*(1 + g)**3]
    V, D = build(e, out[key]['pe27'], PE[1], po, CONV[key]['Base'], False)
    return irr([(0, -out[key]['pe27'])] + [(T0 + k + 0.5, D[k]) for k in range(3)] + [(T0 + 3, V[2])])
for key in L:
    lo, hi = -0.5, 1.5
    for _ in range(80):
        m = (lo + hi)/2; lo, hi = (m, hi) if irr_g(key, m) < 0.12 else (lo, m)
    out[key]['g_req'] = m*100
tot = sum(v['mcap'] for v in out.values())
w = lambda k: sum(v['mcap']*v[k] for v in out.values())/tot
print('switches', sorted(ARGS))
print(f"{'layer':4s} {'mcap':>6s} {'P/E':>5s} {'g26-27':>6s} | NOK Bear / Base / Bull | Base USD | r27 Bear/Base/Bull | Pk / MoS | E / R / ratio | g_req")
for k, v in out.items():
    print(f"{k:4s} {v['mcap']/1e3:6.2f} {v['pe27']:5.1f} {v['g2627']:+5.0f}% | {v['Bear_NOK']:6.1f} {v['Base_NOK']:6.1f} {v['Bull_NOK']:6.1f} | {v['Base_USD']:6.1f} | "
          f"{v['Bear_r27']:6.1f} {v['Base_r27']:5.1f} {v['Bull_r27']:5.1f} | {v['Pk']:5.1f} {v['mos']:+6.1f}% | {v['E']:6.2f} {v['R']:5.1f} {v['ER']:+.3f} | {v['g_req']:5.1f}%")
print(f"ALL  {tot/1e3:6.2f}             | {w('Bear_NOK'):6.1f} {w('Base_NOK'):6.1f} {w('Bull_NOK'):6.1f} | {w('Base_USD'):6.1f} | {w('Bear_r27'):6.1f}")
print('weights', {k: round(v['mcap']/tot*100) for k, v in out.items()})
json.dump(out, open('model_out_' + '_'.join(sorted(ARGS)) + '.json', 'w'), default=float, indent=1)
# Exit cross-check (IAF Step 3, Track A form): buyer's implied return at the Base exit = c(2029) / exit P/E
# + long-run growth (World's 5.3%), against World's mid-cycle return 8.2% at exit P/E 17 (Equity BBB 18 Oct).
print('exit cross-check (Base): layer, exit P/E, c 2029, cash yield, + g 5.3% = buyer return vs World 8.2%')
for key, (name, mem, PE, po) in L.items():
    c = CONV[key]['Base'][2]; y = c/PE[1]*100
    print(f'  {key:3s} {PE[1]:5.1f} {c:5.2f} {y:5.1f}% {y + 5.3:5.1f}%')

