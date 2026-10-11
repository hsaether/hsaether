import json
# ---------- common ----------
STUB=81/365            # 11 Oct -> 31 Dec 2026
T=STUB+3
NIBOR={"stub":4.80,"2027":(4.21,4.79,4.65),"2028":(3.55,4.39,4.15),"2029":(3.50,3.86,3.65)}  # Bear/Base/Bull from hy-market-bbb
FEE=0.20  # index fund fee pp [A]
def irr(flows):
    lo,hi=-0.9,1.0
    for _ in range(200):
        m=(lo+hi)/2; v=sum(cf/(1+m)**t for t,cf in flows)
        if v>0: lo=m
        else: hi=m
    return m
def pv(flows,k): return sum(cf/(1+k)**t for t,cf in flows)
SC=["Bear","Base","Bull"]
def run(name,P0,E27c,eps,pe,payout,stub_yield,fx=None,fx_share=0.0,verbose=True):
    """eps[s]=[2027,2028,2029,2030n] rel to E27c; pe[s]=[end27,end28,exit29] forward P/E on next-year EPS;
       fx[s]=[end27,end28,end29] NOK per foreign unit relative to today (1.0 = flat); fx_share = share of value translated"""
    out={}
    for s in SC:
        e=[E27c*x for x in eps[s]]
        f=fx[s] if fx else [1,1,1]
        tr=lambda v,i: v*(1-fx_share+fx_share*f[i])   # translate to NOK
        V26=P0                                         # stub: price flat (convention), same all scenarios
        D_stub=P0*stub_yield*STUB
        V=[tr(pe[s][0]*e[1],0), tr(pe[s][1]*e[2],1), tr(pe[s][2]*e[3],2)]
        D=[tr(payout*e[0],0)*(1+0), tr(payout*e[1],1), tr(payout*e[2],2)]
        # annual returns
        prev=V26; r=[]
        for i in range(3):
            r.append((D[i]+V[i])/prev-1); prev=V[i]
        stub_r=D_stub/P0
        flows=[(0,-P0),(STUB,D_stub)]+[(STUB+i+0.5,D[i]) for i in range(3)]+[(T,V[2])]
        I=irr(flows); Pk=pv(flows[1:],0.12)
        out[s]=dict(r=r,stub=stub_r,irr=I,VT=V[2],sumD=D_stub+sum(D),Pk=Pk,V=V,D=D,flows=flows,eps=e)
    base=out["Base"]; bear=out["Bear"]
    nib_win=((1+NIBOR["stub"]/100)**STUB*(1+NIBOR["2027"][1]/100)*(1+NIBOR["2028"][1]/100)*(1+NIBOR["2029"][1]/100))**(1/T)-1
    E=(base["irr"]-nib_win)*100-FEE
    R=(base["r"][0]-bear["r"][0])*100
    if verbose:
        print(f"\n===== {name}  P0 {P0}")
        for s in SC:
            o=out[s]
            print(f"{s:5s} stub {o['stub']*100:5.1f}% | 2027 {o['r'][0]*100:6.1f}% 2028 {o['r'][1]*100:6.1f}% 2029 {o['r'][2]*100:6.1f}% | window IRR {o['irr']*100:5.1f}% | sumD {o['sumD']:.1f} VT {o['VT']:.1f} | P_k(12%) {o['Pk']:.1f} MoS {o['Pk']/P0-1:+.1%} | capital kept {(o['sumD']+o['VT'])/P0-1:+.1%}")
        print(f" NIBOR window {nib_win*100:.2f}% | E (after {FEE} fee) {E:.2f} pp | R {R:.1f} pp | E/R {E/R:.3f}")
    return out,E,R,nib_win
# ---------- OSLO (OSEBX GI 2068.38 = 100) ----------
PE27_OSL=11.84; E27=100/PE27_OSL
w={"E":0.42,"F":0.22,"O":0.36}
blocks={
 "Bear":{"E":[(65-30)/49,(60-30)/49,(60-30)/49,(60-30)/49],"F":[.85,.80,.88,.90],"O":[.85,.85,.93,1.00]},
 "Base":{"E":[(85-30)/49,(77-30)/49,(72-30)/49,(70-30)/49],"F":[.98,.96,.95,.93],"O":[.97,1.02,1.07,1.10]},
 "Bull":{"E":[(85-30)/49,(77-30)/49,(72-30)/49,(70-30)/49],"F":[1.00,1.03,1.05,1.02],"O":[1.00,1.08,1.15,1.19]},
}
# FX (USDNOK rel. to today 9.5555), per year [2027,2028,2029,2030n]
fxp={"Bear":[1.12,1.09,1.09,1.09],"Base":[1,1,1,1],"Bull":[0.97,0.97,0.97,0.97]}
FXSH={"E":1.0,"F":0.0,"O":0.5}  # share of block earnings in foreign currency [A]
eps={}
for s in SC:
    eps[s]=[sum(w[b]*blocks[s][b][i]*(1-FXSH[b]+FXSH[b]*fxp[s][i]) for b in w) for i in range(4)]
    print("Oslo EPS rel", s, [round(x,3) for x in eps[s]])
pe_osl={"Bear":[10.5,10.5,10.5],"Base":[11.7,11.6,11.5],"Bull":[12.0,12.3,12.5]}
osl,Eo,Ro,nw=run("OSLO (OSEBX)",100,E27,eps,pe_osl,payout=0.66,stub_yield=0.056)
# ---------- WORLD (MSCI World, USD, then NOK) ----------
PE27_W=17.3; E27w=100/PE27_W
epsw={"Bear":[.75,.82,.90,.97],"Base":[.95,1.0165,1.0775,1.137],"Bull":[1.00,1.09,1.17,1.25]}
pe_w={"Bear":[15.0,15.0,15.0],"Base":[17.6,17.3,17.0],"Bull":[18.2,18.4,18.5]}
wu,Ewu,Rwu,_=run("WORLD in USD",100,E27w,epsw,pe_w,payout=0.45,stub_yield=0.025)
fxw={"Bear":[1.12,1.09,1.09],"Base":[1,1,1],"Bull":[0.97,0.97,0.97]}
wn,Ewn,Rwn,_=run("WORLD in NOK (unhedged)",100,E27w,epsw,pe_w,payout=0.45,stub_yield=0.025,fx=fxw,fx_share=1.0)
json.dump({"osl":{s:{k:v for k,v in o.items() if k!='flows'} for s,o in osl.items()},"wn":{s:{k:v for k,v in o.items() if k!='flows'} for s,o in wn.items()}},open("model_out.json","w"),default=float)
# ---------- oil-shock side case (oil Bull / stagflation) ----------
side_eps_osl=[sum(w[b]*x for b,x in zip("EFO",vals)) for vals in zip([(118-30)/49,(102-30)/49,(90-30)/49,(82-30)/49],[1.0,.96,.95,.93],[.90,.92,.98,1.04])]
print("\nOil-shock Oslo EPS rel",[round(x,3) for x in side_eps_osl])
r_side_osl=(0.66*side_eps_osl[0]*E27+11.0*side_eps_osl[1]*E27)/100-1
r_side_w=(0.45*0.90*E27w+15.5*0.92*E27w)/100-1
print(f"Oil-shock 2027: Oslo {r_side_osl*100:.1f}%  World USD {r_side_w*100:.1f}%  (NOK flat->) World NOK with NOK +5%: {((1+r_side_w)*0.95-1)*100:.1f}%")
