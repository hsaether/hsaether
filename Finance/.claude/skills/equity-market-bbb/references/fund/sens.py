# DNB Teknologi A, model v7: sensitivities and NAV triggers (run in the version's working folder)
# v7: HY market reference E / R 0.196 -> 0.254 (hy-market-bbb 5 Nov); 0.216 = HY Bear read as a shock (sensitivity)
REF=0.254
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M, copy
base=copy.deepcopy(M.EPS)
def b(**kw):
    M.EPS=copy.deepcopy(base); o,E,R=M.run(**kw); return o,E,R
o,E,R=b(); print("BASE IRR %.2f E %.2f R %.1f E/R %.3f"%(o['Base']['irr']*100,E,R,E/R))
for lab,kw in [("fee 0.20 (index-like cost)",dict(fee=0.002)),("alpha +1.14 (manager earns fee)",dict(alpha=0.0114)),("alpha +2.0 (10y record vs benchmark)",dict(alpha=0.02)),
               ("exit P/E -1",dict(pex_shift=-1)),("exit P/E +1",dict(pex_shift=1)),("CY27 EPS -5% all",dict(eps_mult=0.95))]:
    o,E,R=b(**kw); print(f"{lab:40s} Bear {o['Bear']['irr']*100:5.1f} Base {o['Base']['irr']*100:5.1f} Bull {o['Bull']['irr']*100:5.1f} | Base 2027 {o['Base']['r'][0]*100:5.1f} Bear 2027 {o['Bear']['r'][0]*100:5.1f} | E/R {E/R:.3f}")
# triggers: NAV change at unchanged earnings
def solve(f,lo=-0.6,hi=0.3):
    for _ in range(80):
        m=(lo+hi)/2
        if f(m)>0: lo=m
        else: hi=m
    return m
def at(dp,**kw):
    M.EPS=copy.deepcopy(base)
    # price change at unchanged earnings: P0 = 100*(1+dp) while earnings fixed -> scale P/E now
    BL=copy.deepcopy(M.BL)
    PF={c:M.COMP[c]['PF'] for c in M.COMP}
    for k in M.BL: M.BL[k]['pe27']=BL[k]['pe27']*(1+dp)
    for c in M.COMP: M.COMP[c]['PF']=PF[c]*(1+dp)   # company blocks: price moves with the NAV
    o,E,R=M.run(P0=100*(1+dp),**kw); M.BL.update(BL)
    for c in M.COMP: M.COMP[c]['PF']=PF[c]
    return o,E,R
NAV=M.NAV
PE0=sum(x['w'] for x in M.BL.values())*100/sum(x['w']*100/x['pe27'] for x in M.BL.values())
mw=sum(M.BL[k]['w'] for k in M.BL if k in M.MEM); me=sum(M.BL[k]['w']*100/M.BL[k]['pe27'] for k in M.BL if k in M.MEM)
PEX0=(100-mw*100)/(sum(x['w']*100/x['pe27'] for x in M.BL.values())-me)
for lab,fn in [("Base IRR = 6.9% (HY book)",lambda m: 0.069-at(m)[0]['Base']['irr']),("E/R = 0.254 (HY market ref)",lambda m: REF-at(m)[1]/at(m)[2]),("E/R = 0.216 (ref, Bear as shock)",lambda m: 0.216-at(m)[1]/at(m)[2]),("E/R = 0.196 (old ref)",lambda m: 0.196-at(m)[1]/at(m)[2]),
               ("Base IRR = 12% (k)",lambda m: 0.12-at(m)[0]['Base']['irr']),("E/R = 0.291 (HY book)",lambda m: 0.291-at(m)[1]/at(m)[2])]:
    m=solve(lambda x: -fn(x)); o,E,R=at(m)
    print(f"{lab:30s} NAV change {m*100:6.1f}% -> NAV {NAV*(1+m):7.0f}; look-through P/E CY27 {PE0*(1+m):.1f} (ex memory {PEX0*(1+m):.1f}); Base IRR {o['Base']['irr']*100:.1f} E/R {E/R:.3f}")
m=solve(lambda x: (REF-at(x,cap=True)[1]/at(x,cap=True)[2])*-1); print(f"E/R = {REF} on the memory-stressed Bear: NAV change {m*100:.1f}% -> NAV {NAV*(1+m):.0f}")
# side case: oil Bull / stagflation 2027: EPS = Base 2027 x 0.95, fwd P/E x 0.85, NOK flat
M.EPS=copy.deepcopy(base); o,E,R=M.run()
print("side case 2027 approx", round(((1+o['Base']['r'][0])*0.95*0.85-1)*100,1))
