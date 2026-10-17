# AI Market BBB — layer baskets, IAF index-level build (USD and NOK). Version 2 (17 Oct 2026).
# Prices: Yahoo close 16 Oct 2026 (US, Europe, Korea). Consensus: Yahoo earningsTrend 17 Oct 2026.
# Changes from version 1 (16 Oct): (1) retained cash counted once: each year the layer converts
# conv x EPS into free cash after growth capex (net of dilution offsets); payout x EPS is paid as
# D_t and the rest (conv - payout) x EPS accumulates at face value into V_t and V_T (negative =
# net debt build). (2) Fiscal-year consensus calendarised by months (NVDA by calendar quarters,
# docs/nvda-analysis.md; MU by calendar quarters, docs/mu-analysis.md); ASML's consensus is in EUR
# and is converted to USD. (3) Bear paths reconciled to revenue (H1, H3, H4) and the E layer moved
# to the Microsoft and Alphabet company analyses where the gap is >= 0.05.
# Switches (for the attribution in the change log): CAL, RET, PATH. Run: py -I model2.py [CAL RET PATH]
import json, sys
ARGS = set(sys.argv[1:]) or {'CAL', 'RET', 'PATH'}
CAL, RET, PATH = 'CAL' in ARGS, 'RET' in ARGS, 'PATH' in ARGS
KRW = 1329.6; EUR = 1.12435
q = {r['symbol']: r for r in json.load(open('data/q.json'))}
def mc(s):
    r = q[s]; m = r.get('marketCap') or 0
    if r.get('currency') == 'KRW': m /= KRW
    if r.get('currency') == 'EUR': m *= EUR
    return m / 1e9
# CY27 consensus EPS (Yahoo earningsTrend 17 Oct 2026), in the price currency of each line.
# Old convention (version 1): next fiscal year taken as CY27 for FY Jan names, ORCL FY mean,
# ASML in EUR read as USD. Calendarised (version 2): by months, or by quarters where a company
# analysis did so.
cal = dict(
 NVDA=15.21,                                   # by calendar quarters (nvda-analysis); FY Jan-28 15.91
 AMD=15.75529, AVGO=19.39695,                  # AVGO FY Oct-27 (no FY28 consensus; understates CY27 by up to ~5%)
 MRVL=4.22026/12 + 7.29625*11/12,              # FY Jan: 1/12 FY Jan-27 + 11/12 FY Jan-28
 MU=192.1,                                     # by calendar quarters (mu-analysis 191.3 at FY28 204.47; FY28 now 206.89)
 **{'000660.KS': 466735.6, '005930.KS': 72043.35},
 TSM=23.10742, ASML=55.92932*EUR,              # ASML consensus in EUR -> USD
 AMAT=18.45665, LRCX=(9.47647 + 11.76569)/2,   # AMAT FY Oct-27; LRCX FY Jun: 1/2 + 1/2
 ANET=5.22238, VRT=9.19314, ETN=16.28635,
 MSFT=(19.77839 + 23.72118)/2,                 # FY Jun: 1/2 + 1/2
 GOOGL=15.07611, AMZN=10.55194, META=33.91912,
 ORCL=8.14059*5/12 + 10.99155*7/12,            # FY May: 5/12 FY May-27 + 7/12 FY May-28
 NOW=5.00529, CRM=16.7558/12 + 16.02297*11/12, ADBE=27.50756, PLTR=2.3505,
 **{'SAP.DE': 8.37917}, INTU=23.81046*7/12 + 26.94382*5/12,
 SNOW=2.22372/12 + 3.00785*11/12, DDOG=2.97446)
old = dict(cal, NVDA=15.9146, MRVL=7.29625, CRM=16.02297, SNOW=3.00785,
           ORCL=(8.14059 + 10.99155)/2, ASML=55.92932)
eps27 = cal if CAL else old
# CY26 (display only: consensus growth CY26 -> CY27)
eps26 = {'NVDA': 4.77/12 + 9.31242*11/12, 'AMD': 7.5868, 'AVGO': 11.65797, 'TSM': 17.30924, 'MU': 118.9,
         '000660.KS': 354197.5, 'ANET': 4.11675, 'VRT': 6.73516, 'ETN': 13.59405,
         'MSFT': (17.28 + 19.77839)/2, 'META': 30.61042, 'ORCL': 7.63*5/12 + 8.14059*7/12,
         'NOW': 4.06681, 'CRM': 12.52/12 + 16.7558*11/12, 'ADBE': 24.47602, 'PLTR': 1.61873,
         'SAP.DE': 7.13783, 'SNOW': 1.25/12 + 2.22372*11/12, 'DDOG': 2.52764}
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
PATHS = P2 if PATH else P1
CONV = {  # [A], calibrated on the company analyses' FCF after growth capex
 'H1': dict(Bear=(.85,.95,.95), Base=(.80,.90,.90), Bull=(.75,.85,.90)),   # NVDA .77/.95/.97
 'H2': dict(Bear=(.70,.75,.70), Base=(.70,.65,.60), Bull=(.70,.70,.55)),   # MU .71/.67/.60
 'H3': dict(Bear=(.75,.90,.95), Base=(.75,.80,.82), Bull=(.70,.72,.78)),   # TSM .63/.68/.74 (60%), equipment ~.95
 'H4': dict(Bear=(.90,.90,.90), Base=(.90,.90,.90), Bull=(.90,.90,.90)),   # asset-light, no analysis
 'E':  dict(Bear=(.00,.40,.60), Base=(-.10,.10,.30), Bull=(-.20,-.10,.10)),# MSFT .22/.34/.45, GOOGL -.30/-.14/.06 (after withholding)
 'T':  dict(Bear=(.80,.80,.80), Base=(.80,.80,.80), Bull=(.80,.80,.80))}   # non-GAAP EPS; SBC dilution offset
L = {
 'H1': ('H1 Compute (NVDA AMD AVGO MRVL)', ['NVDA','AMD','AVGO','MRVL'], (13,17,19), .25),
 'H2': ('H2 Memory (MU SK hynix Samsung)', ['MU','000660.KS','005930.KS'], (8,10,11), .15),
 'H3': ('H3 Foundry and equipment (TSM ASML AMAT LRCX)', ['TSM','ASML','AMAT','LRCX'], (14,18,21), .45),
 'H4': ('H4 Networking and DC infrastructure (ANET VRT ETN)', ['ANET','VRT','ETN'], (15,20,24), .35),
 'E':  ('E Engines and cloud platforms (MSFT GOOGL AMZN META ORCL)', ['MSFT','GOOGL','AMZN','META','ORCL'], (17,21,23.5), .34),
 'T':  ('T Tools and application software (NOW CRM ADBE PLTR SAP INTU SNOW DDOG)', ['NOW','CRM','ADBE','PLTR','SAP.DE','INTU','SNOW','DDOG'], (15,20,24), .45)}
FX = dict(Bear=(10.70,10.42,10.42), Base=(9.5555,9.5555,9.5555), Bull=(9.27,9.27,9.27)); FX0 = 9.5555
NIB = 4.38; T0 = 75/365  # 17 Oct -> 31 Dec
def irr(fl):
    lo, hi = -0.9, 2.0
    for _ in range(200):
        m = (lo + hi)/2; v = sum(c/(1 + m)**t for t, c in fl)
        lo, hi = (m, hi) if v > 0 else (lo, m)
    return m
def build(e, P, ex, po, cv, bear):
    """Year-end values V (per unit of CY27 consensus EPS) and payouts D for 2027-29."""
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
