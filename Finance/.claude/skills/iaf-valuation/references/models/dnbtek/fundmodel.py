# DNB Teknologi A — look-through scenario model (docs/dnb-teknologi-analysis.md) under iaf-valuation, version 8 (16 Nov 2026;
# v7 6 Nov, v6 30 Oct). v8: company blocks NVIDIA v1.6 (13 Nov, $166.19), TSMC v1.2 (11 Nov, $396.48), Amazon's 11 Nov re-mark
# ($270.87, re-glided interim V_t), Samsung v3 (16 Nov, 196,800 / 161,300, preference discount 18.0%), Microsoft's 7 Nov re-mark
# ($530.61) and Alphabet's 7 Nov block ($284.78); AI BBB 11 Nov: H1 Base .92 / .91 / .88 / .87 and the E cash conversion
# Base -.20 / .11 / .36. Options: V7CO = the v7 company values; V7AI = the v7 AI rows (both for the attribution).
# Layer blocks follow docs/ai-market-bbb.md (method v2.1): EPS path x P/E glide, payout x EPS paid, and (cash conversion -
# payout) x EPS retained at face value into V_t (retained cash counted once). Company blocks take per-share V_t, D_t and EPS
# from their analyses; a price different from the analysis price is a return difference. X = non-AI, own [A].
# Working folder: blocks.json (blocks.py; NAV, stub days and currency mix in "_meta") and closes.json (close.py).
import json, sys, os, copy
K=0.12
BL={}; META={}; CL={}; STUB=T=NAV=USD=OTH=None; PXKEY="14"; V7F="V7CO" in sys.argv; V7AIF="V7AI" in sys.argv
RET=True                         # retained cash on
NIB={"stub":4.80,"2027":4.79,"2028":4.39,"2029":3.86}   # Base NIBOR, hy-market-bbb (5 Nov, kept 11 Nov)
def nibw(): return ((1+NIB["stub"]/100)**STUB*(1+NIB["2027"]/100)*(1+NIB["2028"]/100)*(1+NIB["2029"]/100))**(1/T)-1
SC=["Bear","Base","Bull"]
# EPS paths rel. to block CY27 consensus = 1.00: [2027, 2028, 2029, 2030 normalised] — AI BBB Interface (11 Nov paths)
EPS={"E": {"Bear":[.88,.88,.97,1.05],"Base":[.97,1.07,1.17,1.27],"Bull":[1.00,1.13,1.27,1.41]},   # AI BBB "E rest" row (Meta, Oracle)
     "H1":{"Bear":[.68,.50,.53,.57],"Base":[.92,.91,.88,.87],"Bull":[1.00,1.15,1.25,1.30]},   # 11 Nov: K1 plateau (was .92/.98/1.00/.97)
     "H3":{"Bear":[.76,.63,.67,.71],"Base":[.95,1.03,1.10,1.16],"Bull":[1.00,1.15,1.28,1.40]},
     "T": {"Bear":[.88,.85,.93,1.00],"Base":[.95,1.03,1.11,1.19],"Bull":[1.00,1.10,1.20,1.30]},
     "X": {"Bear":[.85,.85,.93,1.00],"Base":[.97,1.05,1.13,1.21],"Bull":[1.00,1.09,1.18,1.27]}}
PEX={"E":{"Bear":17,"Base":21,"Bull":23.5},"H1":{"Bear":13,"Base":17,"Bull":19},
     "H3":{"Bear":14,"Base":18,"Bull":21},"T":{"Bear":15,"Base":20,"Bull":24},"X":{"Bear":13.5,"Base":16.5,"Bull":18}}
PAY={"E":0.34,"H1":0.25,"H3":0.45,"T":0.45,"X":0.45}
# cash conversion (free cash after growth capex and dilution offsets / EPS), 2027/28/29 — AI BBB v2.1; X own [A]
CONV={"E": {"Bear":[-.10,.30,.50],"Base":[-.20,.11,.36],"Bull":[-.30,-.20,.00]},   # 11 Nov: Base -.20/.11/.36 (was -.20/.00/.20)
      "H1":{"Bear":[.85,.95,.95],"Base":[.80,.90,.90],"Bull":[.75,.85,.90]},
      "H3":{"Bear":[.75,.90,.95],"Base":[.75,.80,.82],"Bull":[.70,.72,.78]},
      "T": {s:[.80]*3 for s in SC},
      "X": {s:[.75]*3 for s in SC}}   # [A]: payout consistency, ~8% growth at ROE ~30% needs ~25% retention
AI7={"H1":[.92,.98,1.00,.97],"E":[-.20,.00,.20]}   # the v7 Base rows (AI BBB Update 6, 5 Nov check)
if V7AIF: EPS["H1"]["Base"]=list(AI7["H1"]); CONV["E"]["Base"]=list(AI7["E"])
# Company blocks: per-share V_t (year-end 2027-29), D_t (paid in year), stub payment DST, EPS 2027-30 (2030 = exit-year EPS),
# PA = analysis price, CA_ = the analysis' CY27 consensus (used only when blocks.json carries no consensus), TK = Yahoo ticker.
# Cap = memory Bear capped at today's multiple (the analyses' diagnostic V_t; D_t as Bear), re-priced: + (P - PA) / CA_ x EPS(t+1).
# DISC (CP) = the preference discount by scenario in the Samsung analysis.
COMP={
 "CM":dict(TK="MSFT",PA=530.61,CA_=21.72,DST=0.98,             # docs/msft-analysis.md v3, re-mark 7 Nov (6 Nov close; interim V_t re-glided)
   Bear=dict(V=[337.7,368.8,404.5],D=[3.97,4.17,4.38],EPS=[18.18,17.84,19.16,20.61]),
   Base=dict(V=[585.4,643.1,692.1],D=[4.01,4.37,4.76],EPS=[20.77,23.40,26.11,28.39]),
   Bull=dict(V=[681.3,805.8,921.4],D=[4.02,4.42,4.86],EPS=[22.03,26.26,30.37,33.80])),
 "CG":dict(TK="GOOGL",PA=284.78,CA_=15.17,DST=0.22,            # docs/googl-analysis.md v2, 7 Nov block (6 Nov close; 10-Q net cash)
   Bear=dict(V=[160.3,179.3,202.9],D=[0.88,0.88,0.88],EPS=[10.47,9.83,11.01,12.34]),
   Base=dict(V=[310.4,339.9,371.3],D=[0.91,0.96,1.01],EPS=[12.67,14.29,15.90,17.45]),
   Bull=dict(V=[377.3,441.8,515.9],D=[0.95,1.04,1.14],EPS=[13.81,16.67,18.98,21.40])),
 # docs/nvda-analysis.md v1.6 (13 Nov, $166.19): AI BBB 11 Nov H1 path (.92/.91/.88/.87 x $15.21), exit 17, stub $0.49
 "CN":dict(TK="NVDA",PA=166.19,CA_=15.21,DST=0.49,
   Bear=dict(V=[106.6,115.8,125.8],D=[5.07,4.86,4.41],EPS=[10.34,7.61,8.06,8.67]),
   Base=dict(V=[195.5,219.6,247.1],D=[6.59,8.11,7.92],EPS=[13.99,13.84,13.38,13.23]),
   Bull=dict(V=[256.5,332.4,402.2],D=[7.00,9.59,10.70],EPS=[15.21,17.49,19.01,19.77])),
 # docs/tsm-analysis.md v1.2 (11 Nov, $396.48; CY27 basis $23.43; dividends NT$35/44/52, the 2Q26 NT$7 paid 7 Jan 2027)
 "CT":dict(TK="TSM",PA=396.48,CA_=23.43,DST=0.0,
   Bear=dict(V=[218.2,233.9,250.9],D=[5.18,5.79,6.40],EPS=[17.81,14.76,15.70,16.64]),
   Base=dict(V=[436.8,472.0,504.4],D=[5.34,6.71,7.93],EPS=[22.26,24.14,25.78,27.18]),
   Bull=dict(V=[477.2,585.1,698.9],D=[5.41,7.32,9.15],EPS=[23.43,26.95,30.00,32.81])),
 # docs/amzn-analysis.md v2, re-mark 11 Nov ($270.87): core EPS, no dividends; V_t incl. the AI stakes after tax, net debt
 "CA":dict(TK="AMZN",PA=270.87,CA_=10.67,DST=0.0,
   Bear=dict(V=[105.9,119.6,141.4],D=[0,0,0],EPS=[7.54,6.23,7.05,8.22]),
   Base=dict(V=[291.0,305.4,317.3],D=[0,0,0],EPS=[9.69,11.28,12.68,14.00]),
   Bull=dict(V=[344.5,387.2,432.1],D=[0,0,0],EPS=[10.51,13.07,15.35,17.73])),
 # docs/samsung-analysis.md v3 (16 Nov, Q3 DART report), its "For other modules": stub 0; EPS incl. interest, 2030 core;
 # preference discount 18.0% held in Base, 30% from end-2027 in Bear and capped, 18.0% -> 15% in Bull
 "CS":dict(TK="005930.KS",PA=196800,CA_=77324,DST=0,
   Bear=dict(V=[244346,226416,238354],D=[16344,19338,12803],EPS=[44914,23995,20967,19881]),
   Base=dict(V=[303029,328889,387294],D=[18815,27658,20099],EPS=[68045,47438,33469,28366]),
   Bull=dict(V=[398714,450483,509818],D=[19503,30999,25230],EPS=[75428,62009,44554,35634]),
   Cap=dict(V=[109725,110489,121079])),
 "CP":dict(TK="005935.KS",PA=161300,CA_=77324,DST=0,CAPF=0.70/(1-0.180),DISC={"Bear":0.30,"Base":0.180,"Bull":0.15},
   Bear=dict(V=[171042,158491,166848],D=[16344,19338,12803],EPS=[44914,23995,20967,19881]),
   Base=dict(V=[248367,269562,317431],D=[18815,27658,20099],EPS=[68045,47438,33469,28366]),
   Bull=dict(V=[330830,378348,433345],D=[19503,30999,25230],EPS=[75428,62009,44554,35634]),
   Cap=dict(V=[76808,77342,84755])),
 # docs/skhynix-analysis.md v2 (28 Oct, Q3; kept 4 Nov): stub 34,181 (Q3 dividend 20,000, record 30 Nov, + the 10tn buyback);
 # 2027 D_t incl. the FY2026 rest 50,144; V_t incl. net cash and the Kioxia stake
 "CH":dict(TK="000660.KS",PA=1487000,CA_=467761,DST=34181,
   Bear=dict(V=[1348025,1218755,1264700],D=[175021,63034,51145],EPS=[280657,140328,116940,116940]),
   Base=dict(V=[1807139,1832050,2088422],D=[224423,107481,63776],EPS=[420985,280657,187104,163716]),
   Bull=dict(V=[2376584,2571208,2841287],D=[236889,143905,83259],EPS=[467761,374209,257269,210492]),
   Cap=dict(V=[624739,616017,661962]))}
# v7 company values (6 Nov version) of the blocks that moved in v8, for the attribution
V7={"CM":dict(PA=531.01,Base=dict(V=[585.8,643.2,692.1],D=[4.01,4.37,4.76],EPS=[20.77,23.40,26.11,28.39]),
              Bull=dict(V=[681.6,806.0,921.4],D=[4.02,4.42,4.86],EPS=[22.03,26.26,30.37,33.80])),
 "CG":dict(PA=279.84,Bear=dict(V=[160.1,179.0,202.6],D=[0.88,0.88,0.88],EPS=[10.46,9.82,11.00,12.33]),
   Base=dict(V=[306.6,337.9,371.1],D=[0.91,0.96,1.01],EPS=[12.66,14.28,15.89,17.44]),
   Bull=dict(V=[373.0,439.3,515.9],D=[0.95,1.04,1.14],EPS=[13.80,16.66,18.97,21.39])),
 "CN":dict(PA=181.60,DST=0.56,Bear=dict(V=[106.7,116.0,126.9],D=[5.12,4.92,4.43],EPS=[10.34,7.61,8.06,8.67]),
   Base=dict(V=[220.8,253.3,274.1],D=[6.59,8.46,8.81],EPS=[13.99,14.91,15.21,14.75]),
   Bull=dict(V=[269.5,339.6,402.6],D=[7.00,9.59,10.70],EPS=[15.21,17.49,19.01,19.77])),
 "CT":dict(PA=352.03,Bear=dict(V=[218.7,235.1,252.7],D=[4.54,5.15,5.75],EPS=[17.81,14.76,15.70,16.64]),
   Base=dict(V=[405.5,456.3,506.1],D=[4.84,6.06,7.27],EPS=[22.26,24.14,25.78,27.18]),
   Bull=dict(V=[477.3,585.6,699.7],D=[5.15,6.96,8.78],EPS=[23.43,26.95,30.00,32.81])),
 "CA":dict(PA=240.35,CA_=10.55,Base=dict(V=[267.2,292.0,317.3],D=[0,0,0],EPS=[9.69,11.28,12.68,14.00]),
   Bull=dict(V=[316.9,371.0,432.1],D=[0,0,0],EPS=[10.51,13.07,15.35,17.73])),
 "CS":dict(PA=232000,CA_=72281,
   Bear=dict(V=[227401,210885,222348],D=[16081,18251,12172],EPS=[42387,22642,19815,18873]),
   Base=dict(V=[305037,315368,363445],D=[18359,25924,18910],EPS=[64310,44857,31685,26963]),
   Bull=dict(V=[402248,432587,478856],D=[18981,28982,23639],EPS=[71286,58607,42141,33823]),
   Cap=dict(V=[115118,114002,124263])),
 "CP":dict(PA=183900,CA_=72281,CAPF=0.70/(1-0.207),DISC={"Bear":0.30,"Base":0.207,"Bull":0.15},
   Bear=dict(V=[159181,147619,155644],D=[16081,18251,12172],EPS=[42387,22642,19815,18873]),
   Base=dict(V=[241795,249983,288092],D=[18359,25924,18910],EPS=[64310,44857,31685,26963]),
   Bull=dict(V=[326538,359433,407027],D=[18981,28982,23639],EPS=[71286,58607,42141,33823]),
   Cap=dict(V=[80583,79801,86984]))}
NEWCOMP=copy.deepcopy(COMP)
MEM={"CS","CP","CH"}
def setup():
    """price every company block at its close (NAV date or last) and set its EPS path rel. to the consensus in blocks.json"""
    for c,x in COMP.items():
        cl=CL.get(x["TK"])
        x["PF"]=(cl["last"][1] if PXKEY=="last" else cl["14"]) if cl else x["PA"]
        x["CONS"]=BL[c].get("cons",x["CA_"]) if c in BL else x["CA_"]
        EPS[c]={s:[e/x["CONS"] for e in x[s]["EPS"]] for s in SC}
        PEX[c]={s:x[s]["V"][2]/x[s]["EPS"][3] for s in SC}   # all-in exit multiple (incl. net cash, stakes), reporting only
        PAY[c]=x["Base"]["D"][0]/x["Base"]["EPS"][0]
def use_company(v7=None,only=None):
    """company values: v8 (default); v7=True the v7 values (only = a subset of blocks moved to v8)"""
    global V7F
    if v7 is None: v7=V7F
    COMP.clear(); COMP.update(copy.deepcopy(NEWCOMP)); V7F=v7
    if v7:
        for c,x in V7.items():
            if only and c in only: continue
            COMP[c].update(copy.deepcopy(x))
    setup()
def use_ai(v7):
    """AI BBB Base rows: v7 (5 Nov check) or v8 (11 Nov)"""
    EPS["H1"]["Base"]=list(AI7["H1"]) if v7 else [.92,.91,.88,.87]
    CONV["E"]["Base"]=list(AI7["E"]) if v7 else [-.20,.11,.36]
def load(folder="."):
    """read blocks.json (with NAV, stub days and currency mix) and closes.json from a working folder"""
    global BL,META,CL,STUB,T,NAV,USD,OTH,PXKEY
    b=json.load(open(os.path.join(folder,"blocks.json"))); META=b.pop("_meta",{})
    BL.clear(); BL.update(b); CL=json.load(open(os.path.join(folder,"closes.json")))
    STUB=META.get("stub",48)/365; T=STUB+3          # stub = valuation date (day after the NAV date) -> 31 Dec 2026
    NAV=META.get("nav",7603.41)
    USD,OTH=META.get("usd",0.6283),META.get("oth",0.3514)   # DNB AM currency mix (30 Oct 2026: USD 62.83, other foreign 35.14)
    PXKEY="last" if META.get("prices")=="last" else "14"
    use_company()
load()
FXU={"Bear":[1.12,1.09,1.09],"Base":[1,1,1],"Bull":[0.97,0.97,0.97]}     # USD/NOK rel. to today (equity BBB 6 Nov, Update 2)
FXO={"Bear":[1.076,1.058,1.058],"Base":[1,1,1],"Bull":[0.977,0.977,0.977]} # I-44 rel. (equity BBB)
MEMPEX={"Bear":8,"Base":10,"Bull":11}   # memory exit P/E in the Samsung and SK hynix analyses (AI BBB H2)
def irr(fl):
    lo,hi=-0.9,1.5
    for _ in range(200):
        m=(lo+hi)/2; v=sum(c/(1+m)**t for t,c in fl)
        lo,hi=(m,hi) if v>0 else (lo,m)
    return m
def pv(fl,k): return sum(c/(1+k)**t for t,c in fl)
def run(P0=100.0,fee=0.0114,alpha=0.0,pex_shift=0.0,eps_mult=1.0,cap=False,mem_pex=None,mem_e30=None,fxflat=False):
    """cap: memory Bear at today's multiple (company Cap V_t); mem_pex: {scenario: exit P/E shift} for the memory company blocks
    (Bear from end-2027, Base/Bull glide); mem_e30: memory 2030 EPS multiplier in Base (V_t lowered by the Base exit P/E x the
    EPS change, glide to exit)"""
    out={}
    for s in SC:
        fx=(lambda i: 1.0) if fxflat else (lambda i: 1-USD-OTH+USD*FXU[s][i]+OTH*FXO[s][i])
        V=[0,0,0]; D=[0,0,0]; E=[0,0,0,0]; Rc=[0,0,0]; VM=[0,0,0]; EM=[0,0,0,0]
        for b,x in BL.items():
            w=x["w"]*P0; e27=w/x["pe27"]*eps_mult
            ep=[e27*m for m in EPS[b][s]]
            for i in range(4): E[i]+=ep[i]
            if b in MEM:
                for i in range(4): EM[i]+=ep[i]
            Vb=[0,0,0]
            if b in COMP:   # company block: value and dividends straight from the company analysis
                c=COMP[b]; y=c[s]; dsc=c.get("DISC",{})
                for i in range(3):
                    sh=pex_shift*y["EPS"][i+1]*(1 if s=="Bear" else (i+1)/3)
                    v=y["V"][i]
                    if b in MEM and s=="Bear" and cap:
                        v=c["Cap"]["V"][i]+(c["PF"]-c["PA"])*c.get("CAPF",1.0)/c["CA_"]*y["EPS"][i+1]
                    if b in MEM and mem_pex and s in mem_pex:
                        sh+=mem_pex[s]*y["EPS"][i+1]*(1 if s=="Bear" else (i+1)/3)*((1-dsc[s]) if dsc else 1.0)
                    if b in MEM and mem_e30 is not None and s=="Base":
                        sh+=MEMPEX[s]*(mem_e30-1)*y["EPS"][3]*(i+1)/3*((1-dsc["Base"]) if dsc else 1.0)
                    Vb[i]=w*(v*eps_mult+sh)/c["PF"]; V[i]+=Vb[i]; D[i]+=w*y["D"][i]*eps_mult/c["PF"]
            else:
                pe0=x["pe27"]; pe1=PEX[b][s]+pex_shift
                pe=[pe1]*3 if s=="Bear" else [pe0+(pe1-pe0)*(i+1)/3 for i in range(3)]
                cum=0.0
                for i in range(3):
                    if RET: cum+=(CONV[b][s][i]-PAY[b])*ep[i]
                    Vb[i]=pe[i]*ep[i+1]+cum; V[i]+=Vb[i]; D[i]+=PAY[b]*ep[i]; Rc[i]+=cum
            if b in MEM:
                for i in range(3): VM[i]+=Vb[i]
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
        out[s]=dict(stub=(Dst+Vst)/P0-1,r=r,irr=I,VT=V[2],sumD=Dst+sum(D),Pk=Pk,d=d,g=g,c=I-d-g,E=E,yld0=yld0,Vr=Vr,D=D,V=V,Rc=Rc,VM=VM,EM=EM)
    Ex=(out["Base"]["irr"]-nibw())*100; R=(out["Base"]["r"][0]-out["Bear"]["r"][0])*100
    return out,Ex,R
def line(o,Ex,R,lab=""):
    return (f"{lab:60s} Bear {o['Bear']['irr']*100:6.2f} Base {o['Base']['irr']*100:6.2f} Bull {o['Bull']['irr']*100:6.2f} | "
            f"Bear27 {o['Bear']['r'][0]*100:6.1f} | MoS {o['Base']['Pk']/100-1:+.1%} | E/R {Ex/R:.3f}")
if __name__=="__main__":
    o,Ex,R=run()
    print(f"NAV {NAV}  stub {STUB*365:.0f} d  T {T:.3f}  NIBOR window {nibw()*100:.2f}%  cash yield on CY27 {o['Base']['yld0']*100:.2f}%  mix USD {USD} other {OTH}")
    E27=sum(x['w']*100/x['pe27'] for x in BL.values())
    for s in SC:
        x=o[s]; print(f"{s:4s} stub {x['stub']*100:5.1f} | 27 {x['r'][0]*100:6.1f} 28 {x['r'][1]*100:6.1f} 29 {x['r'][2]*100:6.1f} | IRR {x['irr']*100:5.2f} d {x['d']*100:.1f} g {x['g']*100:.1f} c {x['c']*100:.1f} | sumD {x['sumD']:.1f} VT {x['VT']:.1f} | Pk {x['Pk']:.1f} = NAV {NAV*x['Pk']/100:,.0f} MoS {x['Pk']/100-1:+.1%} | kept {(x['sumD']+x['VT'])/100-1:+.1%} | EPS rel {[round(v/E27,3) for v in x['E']]} | retained (layer blocks, cum.) {[round(v,1) for v in x['Rc']]}")
    print(f"E {Ex:.2f} pp  R {R:.1f} pp  E/R {Ex/R:.3f}")
    print("fund P/E CY27", round(100/E27,2), " company prices", {c:round(x['PF'],2) for c,x in COMP.items() if c in BL})
    oc,Exc,Rc=run(cap=True); print(line(oc,Exc,Rc,"memory-stressed Bear (capped at today's multiple)"), f"| Bear kept {(oc['Bear']['sumD']+oc['Bear']['VT'])/100-1:+.1%} Pk Bear NAV {NAV*oc['Bear']['Pk']/100:,.0f}")
    of,Exf,Rf=run(fxflat=True); print(line(of,Exf,Rf,"spot FX held flat in Bear and Bull (memo)"), f"| Pk Bear/Bull NAV {NAV*of['Bear']['Pk']/100:,.0f} / {NAV*of['Bull']['Pk']/100:,.0f}")
