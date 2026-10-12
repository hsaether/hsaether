import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M
o,E,R=M.run(); NAV=7730.93
BL=M.BL; E27={b:x['w']*100/x['pe27'] for b,x in BL.items()}; ET=sum(E27.values())
for s in M.SC:
    x=o[s]; print(s,"V path (NAV):",[round(NAV*v/100) for v in [100*(1+x['stub'])]] , "annual r",[round(r*100,1) for r in x['r']])
    # blended forward P/E at year ends: V_t / EPS_{t+1} before FX and fee
    pes=[]
    for i in range(3):
        v=0; e=0
        for b,y in BL.items():
            pe0=y['pe27']; pe1=M.PEX[b][s]; pe = pe1 if s=="Bear" else pe0+(pe1-pe0)*(i+1)/3
            ep=E27[b]*M.EPS[b][s][i+1]; v+=pe*ep; e+=ep
        pes.append(round(v/e,1))
    print("  fwd P/E end-27/28/29:",pes, " EPS rel:",[round(v/ET,3) for v in x['E']])
    print("  block share of normalised EPS:",{b:round(E27[b]*M.EPS[b][s][3]/x['E'][3],3) for b in BL})
# year-end NAV levels incl fee (IRR path) and cumulative IRR to each year end
import math
for s in M.SC:
    x=o[s]; lv=[NAV*(1+x['stub'])]
    for r in x['r']: lv.append(lv[-1]*(1+r))
    cum=[(lv[i]/NAV)**(1/(M.STUB+i))-1 if i>0 else None for i in range(4)]
    print(s,"NAV-equivalent (dividends reinvested) end-26/27/28/29:",[round(v) for v in lv],"IRR to year-end:",[None if c is None else round(c*100,1) for c in cum])
print("ex-memory P/E CY27:", round((100-BL['H2']['w']*100)/(ET-E27['H2']),1), "memory earnings share", round(E27['H2']/ET,3))
