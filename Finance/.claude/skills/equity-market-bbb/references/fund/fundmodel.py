# DNB Teknologi A — fund-mode scenario model (equity-market-bbb), version 4 (17 Oct 2026).
# Layer blocks follow docs/ai-market-bbb.md Update 2 (method v2): EPS path x P/E glide, payout x EPS paid,
# and (cash conversion - payout) x EPS retained at face value into V_t (retained cash counted once).
# Company blocks (CM Microsoft, CG Alphabet, CN NVIDIA, CT TSMC) take per-share V_t, D_t and EPS from
# their company analyses (NVIDIA calendarised and NVIDIA/TSMC Bears revenue-consistent, as those analyses
# quantify and the AI BBB adopted). X = non-AI block, own [A].
import json, sys
BL=json.load(open("blocks.json"))
STUB=75/365; T=STUB+3; K=0.12   # stub 17 Oct -> 31 Dec 2026
RET=True                          # retained cash on (False = method v1, for the attribution)
NIB={"stub":4.80,"2027":4.79,"2028":4.39,"2029":3.86}   # Base NIBOR, hy-market-bbb
nibw=((1+NIB["stub"]/100)**STUB*(1+NIB["2027"]/100)*(1+NIB["2028"]/100)*(1+NIB["2029"]/100))**(1/T)-1
SC=["Bear","Base","Bull"]
# EPS paths rel. to block CY27 consensus = 1.00: [2027, 2028, 2029, 2030 normalised]
EPS={"E": {"Bear":[.88,.88,.97,1.05],"Base":[.97,1.07,1.17,1.27],"Bull":[1.00,1.13,1.27,1.41]},   # AI BBB: E path for names other than MSFT/GOOGL
     "H1":{"Bear":[.68,.50,.53,.57],"Base":[.92,.98,1.00,.97],"Bull":[1.00,1.15,1.25,1.30]},   # AI BBB v2 (revenue-consistent Bear)
     "H2":{"Bear":[.60,.30,.25,.25],"Base":[.90,.60,.40,.35],"Bull":[1.00,.80,.55,.45]},
     "H3":{"Bear":[.76,.63,.67,.71],"Base":[.95,1.03,1.10,1.16],"Bull":[1.00,1.15,1.28,1.40]},
     "T": {"Bear":[.88,.85,.93,1.00],"Base":[.95,1.03,1.11,1.19],"Bull":[1.00,1.10,1.20,1.30]},
     "X": {"Bear":[.85,.85,.93,1.00],"Base":[.97,1.05,1.13,1.21],"Bull":[1.00,1.09,1.18,1.27]}}
PEX={"E":{"Bear":17,"Base":21,"Bull":23.5},"H1":{"Bear":13,"Base":17,"Bull":19},"H2":{"Bear":8,"Base":10,"Bull":11},
     "H3":{"Bear":14,"Base":18,"Bull":21},"T":{"Bear":15,"Base":20,"Bull":24},"X":{"Bear":13.5,"Base":16.5,"Bull":18}}
PAY={"E":0.34,"H1":0.25,"H2":0.15,"H3":0.45,"T":0.45,"X":0.45}
# cash conversion (free cash after growth capex and dilution offsets / EPS), 2027/28/29 — AI BBB v2; X own [A]
CONV={"E": {"Bear":[.00,.40,.60],"Base":[-.10,.10,.30],"Bull":[-.20,-.10,.10]},
      "H1":{"Bear":[.85,.95,.95],"Base":[.80,.90,.90],"Bull":[.75,.85,.90]},
      "H2":{"Bear":[.70,.75,.70],"Base":[.70,.65,.60],"Bull":[.70,.70,.55]},
      "H3":{"Bear":[.75,.90,.95],"Base":[.75,.80,.82],"Bull":[.70,.72,.78]},
      "T": {s:[.80]*3 for s in SC},
      "X": {s:[.75]*3 for s in SC}}   # [A]: payout consistency, ~8% growth at ROE ~30% needs ~25% retention
# Company blocks: per-share V_t (year-end), D_t (paid in year), stub dividend, EPS 2027-30. PF = close on the NAV date (15 Oct).
COMP={"CM":dict(PF=539.44,CONS=(19.78192+23.71027)/2,DST=0.98,   # docs/msft-analysis.md v2 (15 Oct)
        Bear=dict(V=[339.1,370.7,406.9],D=[3.97,4.17,4.38],EPS=[18.02,17.67,18.97,20.41]),
        Base=dict(V=[592.3,646.5,692.0],D=[4.01,4.37,4.76],EPS=[20.58,23.16,25.81,28.06]),
        Bull=dict(V=[688.1,808.8,919.7],D=[4.02,4.42,4.86],EPS=[21.83,25.98,30.02,33.39])),
      "CG":dict(PF=349.22,CONS=15.04601,DST=0.22,                    # docs/googl-analysis.md (15 Oct)
        Bear=dict(V=[170.8,190.4,215.1],D=[0.88,0.88,0.88],EPS=[11.12,10.48,11.66,13.02]),
        Base=dict(V=[361.5,377.1,390.1],D=[0.91,0.96,1.01],EPS=[13.45,15.04,16.70,18.27]),
        Bull=dict(V=[434.2,484.2,537.5],D=[0.95,1.04,1.14],EPS=[14.60,17.40,19.79,22.24])),
      # docs/nvda-analysis.md v1 (17 Oct), adjusted as that analysis quantifies [A]: EPS calendarised (x 15.21/15.91),
      # 60% of FCF paid, net cash rolled; Bear on the revenue-consistent path .68/.50/.53/.57 (AI BBB v2 H1 Bear)
      "CN":dict(PF=217.23,CONS=15.21,DST=0.75,
        Bear=dict(V=[106.7,115.7,126.4],D=[4.99,4.57,4.18],EPS=[10.34,7.61,8.06,8.67]),
        Base=dict(V=[237.5,261.8,273.9],D=[6.41,8.45,8.80],EPS=[13.99,14.91,15.21,14.75]),
        Bull=dict(V=[289.0,350.2,402.5],D=[6.81,9.56,10.68],EPS=[15.21,17.49,19.01,19.77])),
      # docs/tsm-analysis.md v1 (17 Oct): Base and Bull as analysed; Bear on the revenue-consistent path .76/.63/.67/.71
      # (that analysis' own -13.2% case, AI BBB v2 H3 Bear), net cash rolled, dividends as analysed [A]
      "CT":dict(PF=422.25,CONS=23.11,DST=0.0,
        Bear=dict(V=[214.9,229.3,244.7],D=[4.63,5.24,5.86],EPS=[17.56,14.56,15.48,16.41]),
        Base=dict(V=[447.1,474.9,499.0],D=[4.93,6.17,7.40],EPS=[21.95,23.80,25.42,26.80]),
        Bull=dict(V=[523.8,606.7,690.0],D=[5.24,7.09,8.94],EPS=[23.11,26.58,29.58,32.35]))}
for c,x in COMP.items():
    EPS[c]={s:[e/x["CONS"] for e in x[s]["EPS"]] for s in SC}
    PEX[c]={s:x[s]["V"][2]/x[s]["EPS"][3] for s in SC}   # all-in exit multiple (incl. net cash, stakes), reporting only
    PAY[c]=x["Base"]["D"][0]/x["Base"]["EPS"][0]
USD,OTH=0.6730,0.3117   # currency mix 10 Sep 2026 (DNB AM): USD 67.30, other foreign 31.17, NOK 1.53
FXU={"Bear":[1.12,1.09,1.09],"Base":[1,1,1],"Bull":[0.97,0.97,0.97]}     # USD/NOK rel. to today (equity BBB)
FXO={"Bear":[1.076,1.058,1.058],"Base":[1,1,1],"Bull":[0.977,0.977,0.977]} # I-44 rel. (equity BBB)
def irr(fl):
    lo,hi=-0.9,1.5
    for _ in range(200):
        m=(lo+hi)/2; v=sum(c/(1+m)**t for t,c in fl)
        lo,hi=(m,hi) if v>0 else (lo,m)
    return m
def pv(fl,k): return sum(c/(1+k)**t for t,c in fl)
def run(P0=100.0,fee=0.0114,alpha=0.0,pex_shift=0.0,eps_mult=1.0,s1n=None,verbose=False):
    if s1n is not None: EPS['H2']['Base'][3]=s1n; EPS['H2']['Base'][2]=max(EPS['H2']['Base'][2],s1n)
    out={}
    for s in SC:
        fx=lambda i: 1-USD-OTH+USD*FXU[s][i]+OTH*FXO[s][i]
        V=[0,0,0]; D=[0,0,0]; E=[0,0,0,0]; Rc=[0,0,0]
        for b,x in BL.items():
            w=x["w"]*P0; e27=w/x["pe27"]*eps_mult
            ep=[e27*m for m in EPS[b][s]]
            for i in range(4): E[i]+=ep[i]
            if b in COMP:   # company block: value and dividends straight from the company analysis
                c=COMP[b]; y=c[s]
                for i in range(3):
                    sh=pex_shift*y["EPS"][i+1]*(1 if s=="Bear" else (i+1)/3)
                    V[i]+=w*(y["V"][i]*eps_mult+sh)/c["PF"]; D[i]+=w*y["D"][i]*eps_mult/c["PF"]
                continue
            pe0=x["pe27"]; pe1=PEX[b][s]+pex_shift
            pe=[pe1]*3 if s=="Bear" else [pe0+(pe1-pe0)*(i+1)/3 for i in range(3)]
            cum=0.0
            for i in range(3):
                if RET: cum+=(CONV[b][s][i]-PAY[b])*ep[i]
                V[i]+=pe[i]*ep[i+1]+cum; D[i]+=PAY[b]*ep[i]; Rc[i]+=cum
        drag=lambda t:((1-fee)*(1+alpha))**t
        Vr=list(V)
        V=[V[i]*fx(i)*drag(STUB+i+1) for i in range(3)]
        D=[D[i]*fx(i)*drag(STUB+i+0.5) for i in range(3)]
        yld0=sum(PAY[b]*x["w"]*100/x["pe27"] for b,x in BL.items() if b not in COMP)/100
        Dst=(P0*yld0*STUB+sum(BL[c]["w"]*P0*COMP[c]["DST"]/COMP[c]["PF"] for c in COMP if c in BL))*drag(STUB/2)
        yld0+=sum(BL[c]["w"]*COMP[c]["Base"]["D"][0]/COMP[c]["PF"] for c in COMP if c in BL)
        Vst=P0*drag(STUB)
        r=[]; prev=Vst
        for i in range(3): r.append((D[i]+V[i])/prev-1); prev=V[i]
        fl=[(0,-P0),(STUB,Dst)]+[(STUB+i+0.5,D[i]) for i in range(3)]+[(T,V[2])]
        I=irr(fl); Pk=pv(fl[1:],K)
        g=(V[2]/P0)**(1/T)-1; d=(Dst+sum(D))/T/P0
        out[s]=dict(stub=(Dst+Vst)/P0-1,r=r,irr=I,VT=V[2],sumD=Dst+sum(D),Pk=Pk,d=d,g=g,c=I-d-g,E=E,yld0=yld0,Vr=Vr,D=D,V=V,Rc=Rc)
    Ex=(out["Base"]["irr"]-nibw)*100; R=(out["Base"]["r"][0]-out["Bear"]["r"][0])*100
    return out,Ex,R
if __name__=="__main__":
    if "NORET" in sys.argv: RET=False
    o,Ex,R=run()
    print(f"NIBOR window {nibw*100:.2f}%  cash yield on CY27 {o['Base']['yld0']*100:.2f}%")
    E27=sum(x['w']*100/x['pe27'] for x in BL.values())
    for s in SC:
        x=o[s]; print(f"{s:4s} stub {x['stub']*100:5.1f} | 27 {x['r'][0]*100:6.1f} 28 {x['r'][1]*100:6.1f} 29 {x['r'][2]*100:6.1f} | IRR {x['irr']*100:5.1f} d {x['d']*100:.1f} g {x['g']*100:.1f} c {x['c']*100:.1f} | sumD {x['sumD']:.1f} VT {x['VT']:.1f} | Pk {x['Pk']:.1f} MoS {x['Pk']/100-1:+.1%} | kept {(x['sumD']+x['VT'])/100-1:+.1%} | EPS rel {[round(v/E27,3) for v in x['E']]} | retained (layer blocks, cum.) {[round(v,1) for v in x['Rc']]}")
    print(f"E {Ex:.2f} pp  R {R:.1f} pp  E/R {Ex/R:.3f}")
    print("fund P/E CY27", round(100/E27,1))
