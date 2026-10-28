# Korea ETFs (EWY, FLKR, KORX) — look-through IAF model, version 1 (26 Oct 2026). Runs under iaf-valuation.
# Samsung (common, preference) and SK hynix take per-share D_t and V_t from their company analyses
# (docs/samsung-analysis.md v1, docs/skhynix-analysis.md v1, both 25 Oct at the 23 Oct close). The SK holdcos
# (SK Square, SK Inc) follow SK hynix at a constant holdco discount. The rest of Korea (K) is an own block [A]
# on consensus. Each ETF is a portfolio of these blocks; capped ETFs are re-capped at each year-end.
# Usage: py korea.py            (results)      py korea.py SENS   (sensitivities)
import json, os, sys, copy
HERE=os.path.dirname(os.path.abspath(__file__))
STUB=66/365; T=STUB+3; K=0.12              # valuation 26 Oct 2026 (Seoul close) -> exit 31 Dec 2029
SC=["Bear","Base","Bull","Cap"]           # Cap = Bear with S, H and holdcos capped at today's multiple (diagnostic)
NIB={"stub":4.80,"2027":4.79,"2028":4.39,"2029":3.86}   # Base NIBOR, hy-market-bbb
nibw=((1+NIB["stub"]/100)**STUB*(1+NIB["2027"]/100)*(1+NIB["2028"]/100)*(1+NIB["2029"]/100))**(1/T)-1
FX={"Bear":[1.076,1.058,1.058],"Base":[1,1,1],"Bull":[0.977,0.977,0.977]}   # I-44 path (equity BBB) for KRW
FX["Cap"]=FX["Bear"]

# ---- company blocks (KRW per share). PF = analysis price (23 Oct close), P = 26 Oct close (Yahoo).
CS=dict(PF=215500,P=213250,CONS=72281,NC=32173,PEcap=2.536,
  Base=dict(D=[19047,25932,19400],V=[297855,315124,366220],EPS=[64365,44888,31739,26964]),
  Bear=dict(D=[16640,17861,12460],V=[228270,212696,224502],EPS=[42441,22659,19850,18874]),
  Bull=dict(D=[19673,29117,24492],V=[392337,431985,482564],EPS=[71341,58640,42208,33824]),
  # capped: V_t = 2.536 x next-year core EPS + year-end net cash (reconstructed [A]; reproduces -8.6%, capital -21.9%)
  Cap=dict(D=[16640,17861,12460],V=[110415,111031,121452],EPS=[42441,22659,19850,18874]))
CH=dict(PF=1277000,P=1282000,CONS=467761,NC=197646+35470,PEcap=2.23,DST=375,
  Base=dict(D=[224781,107231,63586],V=[1731374,1841148,2139886],EPS=[420985,280657,187104,163716]),
  Bear=dict(D=[174948,62705,51083],V=[1398786,1268475,1313646],EPS=[280657,140328,116940,116940]),
  Bull=dict(D=[237380,143684,83061],V=[2275705,2570932,2893760],EPS=[467761,374209,257269,210492]),
  # capped: V_t = 2.23 x next-year EPS + net cash + Kioxia halved (reconstructed [A]; reproduces -11.4%, capital -27.3%)
  Cap=dict(D=[174948,62705,51083],V=[577281,587831,638914],EPS=[280657,140328,116940,116940]))
PREF=dict(PF=167900,P=164800)             # same D_t as common; V = common V x (1 - discount)
DISC0=1-PREF["P"]/CS["P"]                 # 22.7% on 26 Oct
DISC={"Base":[DISC0]*3,"Bear":[0.30]*3,"Cap":[0.30]*3,"Bull":[DISC0+(0.18-DISC0)*(i+1)/3 for i in range(3)]}

def comp_path(c,s,P):
    """per-share D and V at price P; Base/Bull interim marks keep the analysis glide (price change fades by exit),
    the decision Bear is independent of P from end-2027, the capped Bear scales the multiple part."""
    y=c[s]; D=list(y["D"]); V=list(y["V"])
    if s in ("Base","Bull"):
        V=[V[i]+(P-c["PF"])*(1-(i+1)/3) for i in range(3)]
    if s=="Cap":                          # today's core multiple moves with the price: (P - NC) / (PF - NC)
        f=(P-c["NC"])/(c["PF"]-c["NC"])
        V=[v+(f-1)*c["PEcap"]*y["EPS"][i+1] for i,v in enumerate(V)]
    return D,V

# ---- rest of Korea, block K [A]: EPS rel. to CY27 consensus = 1.00: 2027, 2028, 2029, 2030 normalised
KEPS={"Bear":[.80,.78,.85,.92],"Base":[.95,.9975,1.047,1.100],"Bull":[1.00,1.07,1.14,1.22]}
KEPS["Cap"]=KEPS["Bear"]
KPEX={"Bear":7.5,"Base":10.4,"Bull":12.0}; KPEX["Cap"]=7.5   # 20-year ex-semis average 10.4 (Kiwoom via MoneyToday 20 Oct); crisis 7-8
KPAY=0.30; KCONV=0.50                                       # payout and cash conversion: g 5% at ROE ~10% needs ~50% reinvested
KPE0=None                                                   # set from data (rest P/E on CY27 consensus at 26 Oct)

def k_path(s,pe0,ksh=0.0,keps=1.0):
    e=[x*keps/pe0 for x in KEPS[s]]                 # EPS per unit of price (P = 1)
    pe1=KPEX[s]+ksh
    pe=[pe1]*3 if s in ("Bear","Cap") else [pe0+(pe1-pe0)*(i+1)/3 for i in range(3)]
    cum=0.0; D=[]; V=[]
    for i in range(3):
        cum+=(KCONV-KPAY)*e[i]
        D.append(KPAY*e[i]); V.append(pe[i]*e[i+1]+cum)
    return D,V

def blocks(s,sh=0.0,ksh=0.0,keps=1.0,hp=1.0):
    """per-unit-of-price paths (P = 1) for each block: dict b -> (D[3], V[3], stubD)"""
    out={}
    D,V=comp_path(CS,s,CS["P"])
    if hp!=1.0: V=[v*hp for v in V]
    if sh and s!="Cap": V[2]+=sh*CS[s]["EPS"][3]
    out["S"]=([d/CS["P"] for d in D],[v/CS["P"] for v in V],0.0)
    out["SP"]=([d/PREF["P"] for d in D],[v*(1-DISC[s][i])/PREF["P"] for i,v in enumerate(V)],0.0)
    D,V=comp_path(CH,s,CH["P"])
    if hp!=1.0: V=[v*hp for v in V]
    if sh and s!="Cap": V[2]+=sh*CH[s]["EPS"][3]
    out["H"]=([d/CH["P"] for d in D],[v/CH["P"] for v in V],CH["DST"]/CH["P"])
    # SK holdcos: SK hynix total return, nothing paid out (discount held) [A]
    d,v,st=out["H"]; tr=[]; prev=1.0+st
    for i in range(3):
        prev=prev*(d[i]+v[i])/(v[i-1] if i else 1.0); tr.append(prev)
    out["Q"]=([0,0,0],tr,0.0)
    out["K"]=k_path(s,KPE0,ksh,keps)+(0.0,)
    return out

def irr(fl):
    lo,hi=-0.9,2.0
    for _ in range(200):
        m=(lo+hi)/2; v=sum(c/(1+m)**t for t,c in fl)
        lo,hi=(m,hi) if v>0 else (lo,m)
    return m
def pv(fl,k): return sum(c/(1+k)**t for t,c in fl)

# Cap levels at each review (Samsung common + preference, SK hynix, both together) [A]:
#  EWY  MSCI 25/50: issuer <= 22.5%, issuers > 4.5% together <= 45%
#  FLKR FTSE RIC:   the same, and SK Square (~4.5% in FTSE Korea) takes its share of the 45%
#  FLXK FTSE Korea 30/18 and IQQK / LKOR MSCI Korea 20/35, DBX8 MSCI Korea 20/35 Custom (UCITS): the levels observed
#  after the last review (justETF, 27-31 Aug 2026): FLXK 29.3 / 16.7, IQQK and LKOR 31.2 / 18.9, DBX8 30.4 / 14.1
CAPS={"EWY":(0.225,0.225,0.45),"FLKR":(0.225,0.225,0.405),"FLXK":(0.293,0.167,1.0),"IQQK":(0.312,0.189,1.0),
      "LKOR":(0.312,0.189,1.0),"DBX8":(0.304,0.141,1.0)}
def recap(w,u,rule):
    """re-cap at the review from the uncapped market weights u (KOSPI 200 proxy, drifting with prices); the rest and
    the holdcos take the remainder in their current proportions [A]."""
    if rule is None: return w
    cs,ch_,agg=CAPS[rule]
    pf=w["SP"]/(w["S"]+w["SP"]) if w["S"]+w["SP"]>0 else 0.0
    s=min(cs,u["S"]+u["SP"]); h=min(ch_,u["H"])
    if s+h>agg: f=agg/(s+h); s*=f; h*=f
    oth=w["Q"]+w["K"]; left=1-s-h
    return {"S":s*(1-pf),"SP":s*pf,"H":h,"Q":w["Q"]/oth*left,"K":w["K"]/oth*left}

def run_etf(w0,fee,rule,s,**kw):
    B=blocks(s,**kw)
    w=dict(w0); Dst=sum(w[b]*B[b][2] for b in w)*100
    u=dict(UNC)                                     # uncapped market weights (KOSPI 200 proxy)
    w=recap(w,u,rule)                               # December 2026 reviews (MSCI 1 Dec, FTSE ~21 Dec): stub is price-flat
    Vprev=100.0; Ds=[]; Vs=[]; r=[]
    vb={b:w[b]*100 for b in w}                      # value per block at the end of the stub (price flat)
    for i in range(3):
        newv={}; d=0.0; nu={}
        for b in w:
            Db,Vb,_=B[b]
            lvl_prev=Vb[i-1] if i else 1.0
            d+=vb[b]*Db[i]/lvl_prev; newv[b]=vb[b]*Vb[i]/lvl_prev; nu[b]=u[b]*Vb[i]/lvl_prev
        Vt=sum(newv.values()); tu=sum(nu.values()); u={b:nu[b]/tu for b in nu}
        fx=FX[s][i]; drag=(1-fee)**(STUB+i+1)
        Ds.append(d*fx*(1-fee)**(STUB+i+0.5)); Vs.append(Vt*fx*drag)
        r.append((d+Vt)/Vprev-1); Vprev=Vt
        ww=recap({b:newv[b]/Vt for b in w},u,rule)   # year-end review (annual stand-in for quarterly), no trading cost
        vb={b:ww[b]*Vt for b in w}
    fl=[(0,-100.0),(STUB,Dst*(1-fee)**(STUB/2))]+[(STUB+i+0.5,Ds[i]) for i in range(3)]+[(T,Vs[2])]
    I=irr(fl); Pk=pv(fl[1:],K)
    g=(Vs[2]/100)**(1/T)-1; dd=(sum(x for _,x in fl[1:-1]))/T/100
    # NOK year returns (for E / R): include FX and fee
    rn=[]; prevn=100*(1-fee)**STUB
    for i in range(3):
        rn.append((Ds[i]+Vs[i])/prevn-1); prevn=Vs[i]
    return dict(irr=I,Pk=Pk,mos=Pk/100-1,VT=Vs[2],sumD=sum(x for _,x in fl[1:-1]),kept=(sum(x for _,x in fl[1:-1])+Vs[2])/100-1,
                d=dd,g=g,c=I-dd-g,r=r,rn=rn,V=Vs,D=Ds)

def eps_lookthrough(w,s="Base"):
    """CY27-consensus earnings per 100 of price and the S+H share; EPS path rel. to CY27 consensus"""
    e={"S":w["S"]/(CS["P"]/CS["CONS"]),"SP":w["SP"]/(PREF["P"]/CS["CONS"]),"H":w["H"]/(CH["P"]/CH["CONS"]),
       "Q":w["Q"]/QPE,"K":w["K"]/KPE0}
    tot=sum(e.values())
    return 1/tot, (e["S"]+e["SP"]+e["H"])/tot, (e["S"]+e["SP"]+e["H"]+e["Q"])/tot

# ---- holdings (weights of the equity portfolio, repriced to 26 Oct) ----
D_=json.load(open(os.path.join(HERE,"korea_data.json")))
KPE0=D_["KPE0"]; QPE=D_["QPE"]
ETF=D_["etf"]; UNC=dict(ETF["KOSPI200"])
# UCITS funds (Xetra on Nordnet): start at their cap levels after the December review; SK Square as observed (31 Aug);
# preference share of the Samsung weight as observed; the rest of Korea takes the remainder [A]
for nm,(q,pf) in {"FLXK":(0.0372,3.39/29.28),"IQQK":(0.0384,3.42/31.24),"LKOR":(0.0383,3.41/31.15),"DBX8":(0.0427,3.37/30.41)}.items():
    cs,ch_,_=CAPS[nm]; ETF[nm]={"S":cs*(1-pf),"SP":cs*pf,"H":ch_,"Q":q,"K":1-cs-ch_-q}
FEE={"EWY":0.0059,"FLKR":0.0009,"KORX":0.0045*1.13,"FLXK":0.0009,"IQQK":0.0065,"LKOR":0.0045,"DBX8":0.0045,
     "KOSPI200":0.0,"S+H":0.0,"K":0.0}
RULE={"EWY":"EWY","FLKR":"FLKR","KORX":None,"FLXK":"FLXK","IQQK":"IQQK","LKOR":"LKOR","DBX8":"DBX8",
      "KOSPI200":None,"S+H":None,"K":None}

def report(name,w,**kw):
    res={s:run_etf(w,FEE[name],RULE[name],s,**kw) for s in SC}
    E=(res["Base"]["irr"]-nibw)*100
    Rd=(res["Base"]["rn"][0]-res["Bear"]["rn"][0])*100; Rc=(res["Base"]["rn"][0]-res["Cap"]["rn"][0])*100
    return res,E,Rd,Rc

if __name__=="__main__":
    print(f"NIBOR window {nibw*100:.2f}%  T {T:.3f}  rest P/E CY27 {KPE0:.2f}  holdco P/E {QPE:.2f}  pref discount {DISC0:.3f}")
    # reproduce the company analyses at their own prices (KRW, no fee)
    for nm,c in (("Samsung",CS),("SK hynix",CH)):
        for s in ("Bear","Base","Bull","Cap"):
            D,V=comp_path(c,s,c["PF"]); stub=c.get("DST",0)
            fl=[(0,-c["PF"]),(STUB,stub)]+[(STUB+i+0.5,D[i]) for i in range(3)]+[(T,V[2])]
            print(f"  check {nm:8s} {s:4s} IRR at analysis price {irr(fl)*100:5.1f}%  capital {(sum(D)+V[2]+stub)/c['PF']-1:+.1%}")
    names=["KORX","EWY","FLKR","KOSPI200","S+H","K"] if "ALL" in sys.argv else ["KORX","EWY","FLKR"]
    if "SENS" not in sys.argv:
        for nm in ["KORX","EWY","FLKR","FLXK","IQQK","LKOR","DBX8","KOSPI200","S+H","K"]:
            w=ETF[nm]; pe,sh,shq=eps_lookthrough(w)
            res,E,Rd,Rc=report(nm,w)
            print(f"\n{nm}: S {w['S']*100:.1f} pref {w['SP']*100:.1f} H {w['H']*100:.1f} holdco {w['Q']*100:.1f} rest {w['K']*100:.1f} | P/E CY27 {pe:.2f} | S+H share of CY27 earnings {sh:.1%} (+holdcos {shq:.1%}) | fee {FEE[nm]*100:.2f}%")
            for s in SC:
                x=res[s]
                print(f"  {s:4s} IRR {x['irr']*100:6.1f}  d {x['d']*100:4.1f} g {x['g']*100:5.1f} c {x['c']*100:5.1f} | NOK yr {[round(v*100,1) for v in x['rn']]} | VT {x['VT']:6.1f} sumD {x['sumD']:5.1f} | Pk {x['Pk']:6.1f} MoS {x['mos']:+.1%} | capital {x['kept']:+.1%}")
            print(f"  E {E:.2f} pp | R decision Bear {Rd:.1f} pp -> E/R {E/Rd if Rd>0 else float('nan'):.3f} | R capped Bear {Rc:.1f} pp -> E/R {E/Rc:.3f}")
    else:
        def line(lab,**kw):
            out=[]
            for nm in ["KORX","EWY","FLKR","FLXK"]:
                res,E,Rd,Rc=report(nm,ETF[nm],**kw)
                out.append(f"{nm} {res['Base']['irr']*100:5.1f}/{res['Cap']['irr']*100:5.1f}/{res['Cap']['rn'][0]*100:5.1f}/{E/Rc:.3f}")
            print(f"{lab:38s} "+" | ".join(out))
        print("Base IRR / capped Bear IRR / capped Bear 2027 / E/R(capped)")
        line("model")
        line("S and H exit P/E -2",sh=-2); line("S and H exit P/E +2",sh=2)
        line("rest exit P/E -2",ksh=-2); line("rest exit P/E +2",ksh=2)
        line("rest EPS path x0.9",keps=0.9)
        line("S and H values x0.8 (2030 earnings x0.8 approx)",hp=0.8)
        KCONV=0.30; line("rest cash conversion 0.30 (= payout)"); KCONV=0.50
        FX0=copy.deepcopy(FX); FX["Cap"]=[1.0,1.0,1.0]; line("capped Bear without the I-44 cushion"); FX.update(FX0)
        RULE0=dict(RULE); RULE["EWY"]=None; RULE["FLKR"]=None; line("no re-capping (weights drift)"); RULE.update(RULE0)
        # costs outside the model: bid-ask round trip (entry and exit) and Korean withholding at fund level on D_t
        SPREAD={"KORX":0.011,"EWY":0.0002,"FLKR":0.001,"FLXK":0.002}
        for lab,wht,spr in (("after the bid-ask round trip",0,1),("Korean withholding 15% inside the funds on all D_t",0.15,0),("both",0.15,1)):
            out=[]
            for nm in ["KORX","EWY","FLKR","FLXK"]:
                res=run_etf(ETF[nm],FEE[nm],RULE[nm],"Base"); x=res
                fl=[(0,-100*(1+SPREAD[nm]/2*spr))]+[(STUB+i+0.5,x["D"][i]*(1-wht)) for i in range(3)]+[(T,x["V"][2]*(1-SPREAD[nm]/2*spr))]
                out.append(f"{nm} Base {irr(fl)*100:5.1f}")
            print(f"{lab:38s} "+" | ".join(out))
    if "TRIG" in sys.argv:
        for nm in ["KORX","EWY","FLKR","FLXK","IQQK","KOSPI200"]:
            res,E,Rd,Rc=report(nm,ETF[nm])
            b=res["Base"]; c=res["Cap"]
            def at(x):        # ETF price x (1 = today) at unchanged paths
                fl=[(0,-100*x)]+[(STUB+i+0.5,b["D"][i]) for i in range(3)]+[(T,b["V"][2])]
                I=irr(fl); r0=(b["D"][0]+b["V"][0])/(100*x*(1-FEE[nm])**STUB)-1; rc=(c["D"][0]+c["V"][0])/(100*x*(1-FEE[nm])**STUB)-1
                return I,(I-nibw)*100/((r0-rc)*100)
            lo,hi=0.5,3.0
            for _ in range(80):
                m=(lo+hi)/2; lo,hi=(m,hi) if at(m)[1]>0.196 else (lo,m)
            print(f"{nm}: k trigger {b['mos']:+.1%} | E/R = 0.196 at {m-1:+.1%} (Base IRR there {at(m)[0]*100:.1f}%)")
