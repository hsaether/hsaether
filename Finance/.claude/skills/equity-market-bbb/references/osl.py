# Oslo, Update 1 (17 Oct 2026): price 16 Oct, Brent Base 2027 88, NOK spot 9.4135 (USD earnings translated at spot), stub 75 d
STUB=75/365; T=STUB+3; FEE=0.20
NIB=(4.80,4.79,4.39,3.86); nibw=((1+NIB[0]/100)**STUB*(1+NIB[1]/100)*(1+NIB[2]/100)*(1+NIB[3]/100))**(1/T)-1
SC=["Bear","Base","Bull"]
def irr(fl):
    lo,hi=-0.9,1.0
    for _ in range(200):
        m=(lo+hi)/2; v=sum(c/(1+m)**t for t,c in fl); lo,hi=(m,hi) if v>0 else (lo,m)
    return m
PE27=11.84; E27=100/PE27; P0=100*2101.65/2068.38; FXNOW=9.4135/9.5555
w={"E":0.42,"F":0.22,"O":0.36}; FXSH={"E":1.0,"F":0.0,"O":0.5}
def blocks(b27=88, dB=0):
    Bb=[b27+dB,77+dB,72+dB,70+dB]
    return {"Bear":{"E":[(x-30)/49 for x in (65,60,60,60)],"F":[.85,.80,.88,.90],"O":[.85,.85,.93,1.00]},
            "Base":{"E":[(x-30)/49 for x in Bb],"F":[.98,.96,.95,.93],"O":[.97,1.02,1.07,1.10]},
            "Bull":{"E":[(x-30)/49 for x in Bb],"F":[1.00,1.03,1.05,1.02],"O":[1.00,1.08,1.15,1.19]}}
fxp={"Bear":[1.12,1.09,1.09,1.09],"Base":[1,1,1,1],"Bull":[0.97]*4}
PE={"Bear":[10.5]*3,"Base":[11.7,11.6,11.5],"Bull":[12.0,12.3,12.5]}
def run(dp=0.0, b27=88, dB=0, pesh=0.0, fxnow=FXNOW):
    bl=blocks(b27,dB); out={}
    for s in SC:
        eps=[sum(w[b]*bl[s][b][i]*(1-FXSH[b]+FXSH[b]*fxnow*fxp[s][i]) for b in w)*E27 for i in range(4)]
        P=P0*(1+dp); Dst=P0*0.056*STUB
        V=[(PE[s][k]+pesh)*eps[k+1] for k in range(3)]; D=[0.66*eps[k] for k in range(3)]
        r=[]; prev=P
        for k in range(3): r.append((D[k]+V[k])/prev-1); prev=V[k]
        fl=[(0,-P),(STUB,Dst)]+[(STUB+k+0.5,D[k]) for k in range(3)]+[(T,V[2])]
        out[s]=dict(irr=irr(fl),r=r,stub=Dst/P,VT=V[2],sumD=Dst+sum(D),Pk=sum(c/1.12**t for t,c in fl[1:]),eps=[e/E27*100 for e in eps],P=P)
    return out
def er(o): E=(o["Base"]["irr"]-nibw)*100-FEE; R=(o["Base"]["r"][0]-o["Bear"]["r"][0])*100; return E,R,E/R
def solve(fn,tgt,lo=-0.5,hi=0.5):
    for _ in range(80):
        m=(lo+hi)/2
        if fn(m)>tgt: lo=m
        else: hi=m
    return m
if __name__=="__main__":
    o=run()
    for s in SC:
        x=o[s]; print(f"{s}: IRR {x['irr']*100:.2f} r {[round(v*100,1) for v in x['r']]} stub {x['stub']*100:.1f} EPS {[round(v,1) for v in x['eps']]} sumD {x['sumD']/x['P']*100:.1f} VT {x['VT']/x['P']*100:.1f} Pk {x['Pk']:.1f} MoS {x['Pk']/x['P']-1:+.1%} kept {(x['sumD']+x['VT'])/x['P']-1:+.1%}")
    E,R,r=er(o); print(f"E {E:.2f} R {R:.1f} E/R {r:.3f} nibw {nibw*100:.2f}")
    print("sens Brent -10/+10:", [round(run(dB=d)['Base']['irr']*100,1) for d in (-10,10)], " exit P/E -1/+1:", [round(run(pesh=d)['Base']['irr']*100,1) for d in (-1,1)])
    print("old FX (no NOK firming):", round(run(fxnow=1.0)['Base']['irr']*100,2), " Brent 85:", round(run(b27=85)['Base']['irr']*100,2))
    lev=2101.65
    for lab,fn,tgt in [("E/R=0.196",lambda p: er(run(dp=p))[2],0.196),("Base=12%",lambda p: run(dp=p)['Base']['irr'],0.12),("Base=6.9%",lambda p: run(dp=p)['Base']['irr'],0.069),("E/R=0.291",lambda p: er(run(dp=p))[2],0.291)]:
        p=solve(fn,tgt); print(f"trigger {lab}: {p*100:+.1f}% -> {lev*(1+p):.0f}")
    for d in (-10,10):
        p=solve(lambda q: er(run(dp=q,dB=d))[2],0.196); print(f" trigger1 at Brent {d:+d}: {lev*(1+p):.0f}")
