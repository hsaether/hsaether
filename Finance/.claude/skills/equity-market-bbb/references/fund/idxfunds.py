# Global index funds on the Equity Market BBB World paths (11 Oct 2026)
# DNB Global Indeks A = MSCI World (DNB exclusions); Nordnet Global Indeks = MSCI World Climate Change (CTB) NR
import copy
STUB=81/365; T=STUB+3; K=0.12
NIB={"stub":4.80,"2027":4.79,"2028":4.39,"2029":3.86}   # Base 3M NIBOR, hy-market-bbb
nibw=((1+NIB["stub"]/100)**STUB*(1+NIB["2027"]/100)*(1+NIB["2028"]/100)*(1+NIB["2029"]/100))**(1/T)-1
SC=["Bear","Base","Bull"]
FX={"Bear":[1.12,1.09,1.09],"Base":[1,1,1],"Bull":[0.97,0.97,0.97]}   # USD/NOK rel. to 9.5555 (equity BBB), applied to the whole index as the baseline does
# --- World (equity BBB, unchanged) ---
W_EPS={"Bear":[.75,.82,.90,.97],"Base":[.95,1.0165,1.0775,1.137],"Bull":[1.00,1.09,1.17,1.25]}
W_PE={"Bear":[15.0,15.0,15.0],"Base":[17.6,17.3,17.0],"Bull":[18.2,18.4,18.5]}
W_PE27=17.3; W_PAY=0.45; W_Y=0.025
# --- energy split of the World path (oil BBB block E path; same as the Oslo build) [A] ---
SH_E=0.055   # energy share of MSCI World CY27 earnings [A]: weight 4.0% at P/E ~15 (IXC) vs index ~22 (URTH), trailing
E_PATH={"Bear":[(65-30)/49,(60-30)/49,(60-30)/49,(60-30)/49],"Base":[(85-30)/49,(77-30)/49,(72-30)/49,(70-30)/49],"Bull":[(85-30)/49,(77-30)/49,(72-30)/49,(70-30)/49]}
def resid(s,sh=SH_E): return [(W_EPS[s][i]-sh*E_PATH[s][i])/(1-sh) for i in range(4)]
# --- Climate Change index ---
PREM=18.93/17.92   # MSCI fwd P/E ratio CC / World, 30 Sep 2026
def cc_params(prem_exit=PREM, prem_bear=None, sh=SH_E):
    eps={s:resid(s,sh) for s in SC}
    pe={}
    for s in SC:
        if s=="Bear":
            pb=prem_bear if prem_bear is not None else 1+(PREM-1)/2
            pe[s]=[x*pb for x in W_PE[s]]
        else:
            # premium glides from PREM today to prem_exit at exit
            pe[s]=[W_PE[s][i]*(PREM+(prem_exit-PREM)*(i+1)/3) for i in range(3)]
    return dict(pe27=W_PE27*PREM, eps=eps, pe=pe, pay=0.44, y=0.0234)
def irr(fl):
    lo,hi=-0.9,1.5
    for _ in range(200):
        m=(lo+hi)/2; v=sum(c/(1+m)**t for t,c in fl)
        lo,hi=(m,hi) if v>0 else (lo,m)
    return m
def pv(fl,k): return sum(c/(1+k)**t for t,c in fl)
def run(pe27,eps,pe,pay,y,cost=0.0,P0=100.0,eps_mult=1.0):
    out={}
    E27=100/pe27*eps_mult    # earnings per 100 of today's value (unchanged earnings when P0 moves)
    drag=lambda t:(1-cost)**t
    for s in SC:
        e=[E27*x for x in eps[s]]; f=FX[s]
        V=[pe[s][i]*e[i+1]*f[i]*drag(STUB+i+1) for i in range(3)]
        D=[pay*e[i]*f[i]*drag(STUB+i+0.5) for i in range(3)]
        Dst=100*y*STUB*drag(STUB/2); Vst=P0*drag(STUB)
        r=[]; prev=Vst
        for i in range(3): r.append((D[i]+V[i])/prev-1); prev=V[i]
        fl=[(0,-P0),(STUB,Dst)]+[(STUB+i+0.5,D[i]) for i in range(3)]+[(T,V[2])]
        I=irr(fl); Pk=pv(fl[1:],K)
        g=(V[2]/P0)**(1/T)-1; d=(Dst+sum(D))/T/P0
        lv=[Vst]
        for x in r: lv.append(lv[-1]*(1+x))
        out[s]=dict(stub=(Dst+Vst)/P0-1,r=r,irr=I,VT=V[2],sumD=Dst+sum(D),Pk=Pk,d=d,g=g,c=I-d-g,E=e,lv=lv)
    Ex=(out["Base"]["irr"]-nibw)*100; R=(out["Base"]["r"][0]-out["Bear"]["r"][0])*100
    return out,Ex,R
def show(lab,o,Ex,R,nav=None):
    print(f"\n== {lab}   E {Ex:.2f} pp  R {R:.1f} pp  E/R {Ex/R:.3f}")
    for s in SC:
        x=o[s]
        print(f" {s:4s} stub {x['stub']*100:4.1f} | 27 {x['r'][0]*100:6.1f} 28 {x['r'][1]*100:5.1f} 29 {x['r'][2]*100:5.1f} | IRR {x['irr']*100:5.2f} d {x['d']*100:.2f} g {x['g']*100:.2f} c {x['c']*100:.2f} | sumD {x['sumD']:.1f} VT {x['VT']:.1f} kept {(x['sumD']+x['VT'])/100-1:+.1%} | Pk {x['Pk']:.1f} MoS {x['Pk']/100-1:+.1%}"+(f" | NAV Pk {nav*x['Pk']/100:.1f} levels {[round(nav*v/100,1) for v in x['lv']]}" if nav else ""))
W=dict(pe27=W_PE27,eps=W_EPS,pe=W_PE,pay=W_PAY,y=W_Y)
if __name__=="__main__":
    print(f"NIBOR window {nibw*100:.2f}%")
    o,Ex,R=run(**W); show("World index, no cost (must equal equity BBB: -0.2/6.1/11.0; 2027 -18.2/5.9/13.8)",o,Ex,R)
    o,Ex,R=run(**W,cost=0.0020); show("World, 0.20% (baseline E/R check 0.063)",o,Ex,R)
    print("\nresidual (World ex energy) EPS:",{s:[round(v,4) for v in resid(s)] for s in SC})
    o,Ex,R=run(**W,cost=0.0025); show("DNB Global Indeks A on Nordnet (0.25%)",o,Ex,R,nav=874.58)
    o,Ex,R=run(**W,cost=0.0021); show("DNB Global Indeks A in DNB pension (0.20% + 0.01% transaction)",o,Ex,R,nav=874.58)
    C=cc_params()
    print("\nCC P/E paths:",{s:[round(v,2) for v in C['pe'][s]] for s in SC}, "pe27",round(C['pe27'],2))
    o,Ex,R=run(**C,cost=0.0019); show("Nordnet Global Indeks (CC index, 0.19%), premium persists",o,Ex,R,nav=232.43)
    o,Ex,R=run(**C); show("CC index, no cost",o,Ex,R)
    # exit P/E of CC on normalised EPS and EPS CAGR
    for s in SC: print(s,"CC exit P/E",round(C['pe'][s][2],2),"norm EPS",round(C['eps'][s][3],4),"World exit",W_PE[s][2],"norm",W_EPS[s][3])
