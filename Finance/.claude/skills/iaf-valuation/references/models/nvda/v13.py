from datetime import date
import sys
SH=24.2; K=0.12
def irr(cf):
    lo,hi=-0.95,3.0
    for _ in range(300):
        m=(lo+hi)/2
        if sum(c/(1+m)**t for t,c in cf)>0: lo=m
        else: hi=m
    return m
def pvk(cf,k=K): return sum(c/(1+k)**t for t,c in cf)
BASE=dict(eps=[13.99,14.91,15.21],eps30=14.75,margin=[.555,.55,.545],rev=None,capex=[13,15,17],da=[6.5,9,11],
          stakes=[16.9,2,2],charge=[0,0,0],sf=1.0,sfg=[1,1,1],pe=17,payout=.6,wc=.25)
BEAR=dict(BASE,eps=[10.34,7.61,8.06],eps30=8.67,rev=[497,404,422],capex=[12,11,11],charge=[0,5,10],sf=.5,sfg=[.5,.5,.5],pe=13)
BULL=dict(BASE,eps=[15.21,17.49,19.01],eps30=19.77,margin=[.56,.555,.55],capex=[14,17,19],sf=1.25,sfg=[1.08,1.17,1.25],pe=19)
NOKF={'Base':[1,1,1,1],'Bear':[1,1.12,1.09,1.09],'Bull':[1,.97,.97,.97]}
def build(s,stub_days,P,vdate,neglide=True,overrides=None):
    s=dict(s,**(overrides or {}))
    nc26=41.8; st26=115.0
    # stub
    f=stub_days/56
    sfcf=22.5*f; sD=0.6*sfcf; nc0=nc26-(sfcf-sD); st0=st26-4.4*f
    rev0=411.8; nc=nc26; st=st26; D=[sD/SH]; NC=[]; ST=[]; prev=rev0
    for i in range(3):
        ni=s['eps'][i]*SH
        rev=s['rev'][i] if s['rev'] else ni/s['margin'][i]
        wc=s['wc']*(rev-prev); prev=rev
        fcf=ni-(s['capex'][i]-s['da'][i])-wc-s['stakes'][i]-s['charge'][i]
        d=s['payout']*fcf; nc+=fcf-d; st+=s['stakes'][i]
        D.append(d/SH); NC.append(nc/SH); ST.append(st/SH)
    VT=s['pe']*s['eps30']+NC[-1]+s['sf']*ST[-1]
    t=lambda d:(d-vdate).days/365.25
    dates=[date(2026,12,28),date(2027,7,1),date(2028,7,1),date(2029,7,1)]
    cf=[(t(d),x) for d,x in zip(dates,D)]+[(t(date(2029,12,31)),VT)]
    res=dict(D=D,VT=VT,NC=NC,ST=ST,cf=cf,nc0=nc0/SH,st0=st0/SH,nc26=nc26/SH,st26=st26/SH,s=s)
    if P is not None:
        res['irr']=irr([(0,-P)]+cf)
    res['pk']=pvk(cf)
    return res
def nok_irr(r,name,P):
    f=NOKF[name]; cf=[(t,c*f[min(i,3)]) for i,(t,c) in enumerate(r['cf'][:4])]+[(r['cf'][4][0],r['cf'][4][1]*f[3])]
    return irr([(0,-P)]+cf)
def interim(r,name,P,base_eps27=13.99):
    s=r['s']; core0=(P-r['nc0']-r['st0'])/base_eps27
    V=[]
    for i,y in enumerate([2027,2028]):
        if name=='Bear': pe=13
        else: pe=core0+(s['pe']-core0)*(i+1)/3
        V.append(pe*s['eps'][i+1]+r['NC'][i]+s['sfg'][i]*r['ST'][i])
    V26=P+(r['nc26']-r['nc0'])
    return V26,V
