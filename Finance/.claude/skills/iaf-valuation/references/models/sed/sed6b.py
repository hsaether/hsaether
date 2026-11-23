"""SED Step 6b: cash-flow rebuild from docs/SED-analysis.md (27 Oct build): D_t per share (NOK, quarterly mid-quarter) and V_T; re-mark at a new price, date and USD/NOK."""
import sys
from datetime import date
K=0.12; EXIT=date(2029,12,31)
D={'Bear':[0.69,0.18,0.08],'Base':[0.89,0.82,0.57],'Bull':[1.06,1.01,1.02]}
VT={'Bear':1.59,'Base':5.43,'Bull':9.35}; NC={'Bear':-0.16,'Base':0.20,'Bull':0.54}
STUBD=(date(2026,12,11),0.32)   # Q2 distribution: ex 7 Dec, paid ~11 Dec (release 4 Nov 2026)
def yf(a,b): return (b-a).days/365.25
def irr(c):
    lo,hi=-0.9,2.0
    for _ in range(200):
        m=(lo+hi)/2; v=sum(x/(1+m)**t for t,x in c); lo,hi=(m,hi) if v>0 else (lo,m)
    return m
def flows(n,P,d0,f=1.0,vx=1.0,stub=True):
    c=[(0,-P)]
    if stub and STUBD[0]>d0: c.append((yf(d0,STUBD[0]),STUBD[1]*f))
    for i,y in enumerate((2027,2028,2029)):
        for m in (2,5,8,11): c.append((yf(d0,date(y,m,15)),D[n][i]/4*f))
    marks=VT[n]-NC[n]; c.append((yf(d0,EXIT),(marks*vx+NC[n])*f)); return c
def res(n,P,d0,f=1.0,vx=1.0):
    c=flows(n,P,d0,f,vx); r=irr(c); pk=sum(x/(1+K)**t for t,x in c[1:]); return r,pk
def solve(fn,tgt,lo,hi):
    up=fn(hi)>fn(lo)
    for _ in range(100):
        m=(lo+hi)/2
        if (fn(m)>tgt)==up: hi=m
        else: lo=m
    return m
print('check 27 Oct @6.80:',{n:(round(res(n,6.80,date(2026,10,27))[0]*100,1),round(res(n,6.80,date(2026,10,27))[1],2)) for n in D})
P=float(sys.argv[1]) if len(sys.argv)>1 else 6.19; d0=date(2026,11,20); fx=9.7525/9.32; dil=737.3/736.1
f=fx*dil
for n in D:
    r,pk=res(n,P,d0,f); print(f'{n}: IRR {r*100:.1f}% P_k {pk:.2f} MoS {pk/P-1:+.1%}')
print('Base FX only (no price move, 6.80 cum at 20 Nov n/a)')
for lab,ff in (('USD/NOK held 9.32',dil),):
    r,pk=res('Base',P,d0,ff); print(f'  {lab}: IRR {r*100:.1f}% P_k {pk:.2f} MoS {pk/P-1:+.1%}')
vk=solve(lambda v: res('Base',P,d0,f,v)[0],K,0.5,2.5); v0=solve(lambda v: res('Base',P,d0,f,v)[0],0.0,0.1,2.5)
print(f'price implies exit marks x{vk:.3f} Base for k; x{v0:.3f} for 0%')
vk0=solve(lambda v: res('Base',6.80,date(2026,10,27),1.0,v)[0],K,0.5,2.5); print(f'27 Oct check: marks x{vk0:.3f} for k (doc: ~1.21)')
