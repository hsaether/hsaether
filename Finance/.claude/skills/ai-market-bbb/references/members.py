# Per-name check: each name on its layer's v2 path and method (Base and Bear, NOK), against the company analyses.
import sys; sys.argv=['model.py']; exec(open('model.py',encoding='utf-8').read().split("out = {}")[0])
def one(s, key, conv=None, exbase=None, exbear=None):
    name, mem, PE, po = L[key]; P = q[s]['regularMarketPrice']/eps27[s]
    r = {}
    for i, sc in enumerate(['Bear','Base','Bull']):
        ex = PE[i]
        if sc=='Base' and exbase: ex=exbase
        if sc=='Bear' and exbear: ex=exbear
        cv = conv[sc] if conv else CONV[key][sc]
        V, D = build(PATHS[key][sc], P, ex, po, cv, sc=='Bear')
        f=[x/FX0 for x in FX[sc]]
        r[sc]=irr([(0,-P)]+[(T0+k+.5,D[k]*f[k]) for k in range(3)]+[(T0+3,V[2]*f[2])])*100
        if sc in('Base','Bear'): r[sc+'27']=((V[0]+D[0])*f[0]/P-1)*100
    ER=(r['Base']-NIB)/(r['Base27']-r['Bear27'])
    return P, r, ER
co={'NVDA':'13.0 (11.4 calendarised)','MU':'2.8','TSM':'7.4','MSFT':'8.8','GOOGL':'3.8','AMZN':'6.8'}
for key in ['H1','H2','H3','E']:
    for s in L[key][1]:
        P,r,ER=one(s,key); print(f"{key} {s:10s} P/E {P:5.1f}  Bear {r['Bear']:6.1f} Base {r['Base']:5.1f} Bull {r['Bull']:5.1f}  Bear27 {r['Bear27']:6.1f}  E/R {ER:+.3f}   company: {co.get(s,'-')}")
print('\nH2 sensitivities (basket members, Base / Bear NOK, E/R):')
lowc={'Bear':(.50,.55,.50),'Base':(.50,.45,.40),'Bull':(.50,.50,.35)}
for lab,kw in [('conversion -0.2',dict(conv=lowc)),('Base exit P/E 8',dict(exbase=8)),('Bear exit P/E 6',dict(exbear=6))]:
    for s in L['H2'][1]:
        P,r,ER=one(s,'H2',**kw); print(f"  {lab:16s} {s:10s} Base {r['Base']:5.1f} Bear {r['Bear']:6.1f} Bear27 {r['Bear27']:6.1f} E/R {ER:+.3f}")
