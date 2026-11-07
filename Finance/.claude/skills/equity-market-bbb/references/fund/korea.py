# Korea ETFs (EWY, FLKR, KORX, FLXK, IQQK, LKOR, DBX8) — look-through IAF model, version 1.8 (6 Nov 2026; 1.7: 4 Nov). Runs under
# iaf-valuation. Samsung (common, preference) and SK hynix take per-share D_t and V_t from their company analyses
# (docs/samsung-analysis.md v2, 29 Oct at the 29 Oct close, v1 of 25 Oct kept as S1; docs/skhynix-analysis.md v2,
# 28 Oct at the 28 Oct close, v1 of 25 Oct kept as H1 for the before figures). The SK holdcos
# (SK Square, SK Inc) follow SK hynix at a constant holdco discount. The rest of Korea (K) is an own block [A]
# on consensus. Each ETF is a portfolio of these blocks; capped ETFs are re-capped at each year-end.
# Usage: py korea.py            (results)      py korea.py SENS   (sensitivities)      py korea.py TRIG (triggers)
#        py korea.py FUND IQQK (one fund in full, with its sensitivities)
#        py korea.py FUND IQQK IMPL (v1.7: the Samsung and SK hynix Base 2028-30 EPS multiplier the price implies, the AI BBB's
#        named turn-date and depth paths, and the reconstruction checks against the company analyses' own sensitivities)
#        py korea.py FUND IQQK SPOT (v1.7: all scenarios at spot FX held flat, the iaf-valuation FX rule for the decision)
#        valuation date: default 6 Nov close (v1.8; IQQK from its 4 Nov daily file, HY reference 0.254 in TRIG); D04 = 4 Nov close (v1.7);
#        D29 = 29 Oct close; D28 = 28 Oct close; D26 = 26 Oct. Inputs: S1 = Samsung v1
#        (re-priced), H1 = SK hynix v1. v1.7 switches (each turns one v1.7 change off): NOFIX = the stub distribution left out of
#        TRIG and the cost lines (the v1.6 bug); NOWHT = no Korean withholding in the paths; W31AUG = IQQK starts at its 31 Aug cap
#        levels, not at its 2 Nov daily holdings file; V16 = all three. "py korea.py D29 V16 SENS FUND IQQK TRIG" = document v1.6;
#        "py korea.py D26 S1 H1 V16" = v1.3; "py korea.py D28 S1 V16" = v1.4 (FLXK) and v1.5 (IQQK); "py korea.py D29 S1 V16" =
#        the price step of v1.6; "py korea.py D04 FUND IQQK IMPL TRIG SPOT" = v1.7; "py korea.py FUND IQQK IMPL TRIG SPOT" = v1.8
import json, os, sys, copy
HERE=os.path.dirname(os.path.abspath(__file__))
VD="2026-10-26" if "D26" in sys.argv else ("2026-10-28" if "D28" in sys.argv else ("2026-10-29" if "D29" in sys.argv else ("2026-11-04" if "D04" in sys.argv else "2026-11-06")))
H1="H1" in sys.argv; S1="S1" in sys.argv
V16="V16" in sys.argv
FIX=not (V16 or "NOFIX" in sys.argv)      # v1.7 bug fix: the stub distribution is in TRIG and in the cost lines
WHT=0.0 if (V16 or "NOWHT" in sys.argv) else 0.15   # v1.7: Korean withholding on the cash-dividend part of D_t, all scenarios
DAILY=not (V16 or "W31AUG" in sys.argv)   # v1.7: IQQK starts at its own daily holdings file (2 Nov, repriced), where one exists
STUB={"2026-10-26":66,"2026-10-28":64,"2026-10-29":63,"2026-11-04":57,"2026-11-06":55}[VD]/365; T=STUB+3; K=0.12   # valuation date (Seoul close) -> exit 31 Dec 2029
SC=["Bear","Base","Bull","Cap"]           # Cap = Bear with S, H and holdcos capped at today's multiple (diagnostic)
NIB={"stub":4.80,"2027":4.79,"2028":4.39,"2029":3.86}   # Base NIBOR, hy-market-bbb
nibw=((1+NIB["stub"]/100)**STUB*(1+NIB["2027"]/100)*(1+NIB["2028"]/100)*(1+NIB["2029"]/100))**(1/T)-1
FX={"Bear":[1.076,1.058,1.058],"Base":[1,1,1],"Bull":[0.977,0.977,0.977]}   # I-44 path (equity BBB) for KRW
FX["Cap"]=FX["Bear"]

# ---- company blocks (KRW per share). PF = analysis price, P = valuation-date close (Yahoo; 26 Oct 15:10 KST stamp).
PX={"2026-10-26":dict(S=213250,SP=164800,H=1282000),"2026-10-28":dict(S=242000,SP=190100,H=1487000),
    "2026-10-29":dict(S=232000,SP=183900,H=1526000),"2026-11-04":dict(S=218000,SP=171700,H=1396000),
    "2026-11-06":dict(S=188700,SP=150300,H=1132000)}[VD]
# Samsung v1 (25 Oct, 23 Oct close), kept as S1 for the before figures
CS1=dict(PF=215500,P=PX["S"],CONS=72281,NC=32173,PEcap=2.536,
  Base=dict(D=[19047,25932,19400],V=[297855,315124,366220],EPS=[64365,44888,31739,26964]),
  Bear=dict(D=[16640,17861,12460],V=[228270,212696,224502],EPS=[42441,22659,19850,18874]),
  Bull=dict(D=[19673,29117,24492],V=[392337,431985,482564],EPS=[71341,58640,42208,33824]),
  # capped: V_t = 2.536 x next-year core EPS + year-end net cash (reconstructed [A]; reproduces -8.6%, capital -21.9%)
  Cap=dict(D=[16640,17861,12460],V=[110415,111031,121452],EPS=[42441,22659,19850,18874]))
# Samsung v2 (29 Oct, Q3 report, 29 Oct close; its "For other modules" section): stub D_t 0 (the Q3 4,601 went ex on
# 29 Sep); D_t paid by year (2027 includes the 2026 remainder 9,895 on 15 Apr 2027); capped Bear at today's core P/E
# 2.803 = (price - end-2026 net cash 29,401) / CY27 consensus 72,281, V_t as published (115,118 / 114,002 / 124,263)
CS2=dict(PF=232000,P=PX["S"],CONS=72281,NC=29401,
  Base=dict(D=[18359,25924,18910],V=[305037,315368,363445],EPS=[64310,44857,31685,26963]),
  Bear=dict(D=[16081,18251,12172],V=[227401,210885,222348],EPS=[42387,22642,19815,18873]),
  Bull=dict(D=[18981,28982,23639],V=[402248,432587,478856],EPS=[71286,58607,42141,33823]),
  Cap=dict(D=[16081,18251,12172],V=[115118,114002,124263],EPS=[42387,22642,19815,18873]))
CS2["PEcap"]=(CS2["PF"]-CS2["NC"])/CS2["CONS"]
# v1.7 [A]: Base net cash at year-end (2027-29) and the payout rule, for the EPS multiplier (IMPL): 50% of FCF, 30% paid in the
# year and 70% the next April (2029's 70% stays in net cash); interim P/E on next-year EPS implied by the published marks
CS2["NCB"]=[67470,82709,93818]; CS2["STK"]=0; CS2["PAY"]=(0.15,0.35)
CS=CS1 if S1 else CS2
CH1=dict(PF=1277000,P=PX["H"],CONS=467761,NC=197646+35470,PEcap=2.23,DST=375,         # SK hynix v1 (25 Oct, 23 Oct close)
  Base=dict(D=[224781,107231,63586],V=[1731374,1841148,2139886],EPS=[420985,280657,187104,163716]),
  Bear=dict(D=[174948,62705,51083],V=[1398786,1268475,1313646],EPS=[280657,140328,116940,116940]),
  Bull=dict(D=[237380,143684,83061],V=[2275705,2570932,2893760],EPS=[467761,374209,257269,210492]),
  # capped: V_t = 2.23 x next-year EPS + net cash + Kioxia halved (reconstructed [A]; reproduces -11.4%, capital -27.3%)
  Cap=dict(D=[174948,62705,51083],V=[577281,587831,638914],EPS=[280657,140328,116940,116940]))
# SK hynix v2 (28 Oct, Q3 report, 28 Oct close): stub D_t 34,181 (Q3 dividend 20,000 + 10tn buyback) in all scenarios;
# capped Bear at today's core P/E 2.85 = (price - end-2026 net cash 124,667 - Kioxia 31,198) / CY27 consensus
CH2=dict(PF=1487000,P=PX["H"],CONS=467761,NC=124667+31198,DST=34181,
  Base=dict(D=[224423,107481,63776],V=[1807139,1832050,2088422],EPS=[420985,280657,187104,163716]),
  Bear=dict(D=[175021,63034,51145],V=[1348025,1218755,1264700],EPS=[280657,140328,116940,116940]),
  Bull=dict(D=[236889,143905,83259],V=[2376584,2571208,2841287],EPS=[467761,374209,257269,210492]),
  Cap=dict(D=[175021,63034,51145],V=[624739,616017,661962],EPS=[280657,140328,116940,116940]))
CH2["PEcap"]=(CH2["PF"]-CH2["NC"])/CH2["CONS"]
# v1.7 [A]: Base net cash at year-end and the Kioxia stake (held flat); payout 50% of FCF in the same year (1 July)
CH2["NCB"]=[248803,356284,420060]; CH2["STK"]=31198; CH2["PAY"]=(0.50,0.0)
CH=CH1 if H1 else CH2
PREF=dict(PF=167900 if S1 else 183900,P=PX["SP"])   # same D_t as common; V = common V x (1 - discount)
DISC0=1-PREF["P"]/CS["P"]                 # 22.7% on 26 Oct, 21.4% on 28 Oct, 20.7% on 29 Oct, 21.2% on 4 Nov, 20.3% on 6 Nov
DBULL=0.18 if S1 else 0.15                # Bull exit discount: v1 18%; v2 15% (Samsung's statement on preference buybacks)
DISC={"Base":[DISC0]*3,"Bear":[0.30]*3,"Cap":[0.30]*3,"Bull":[DISC0+(DBULL-DISC0)*(i+1)/3 for i in range(3)]}
# v1.7: cash-dividend share of each block's D_t (the rest is buybacks for cancellation, on which the fund pays no tax) [A]:
# Samsung and SK hynix 50% (SK hynix FY2026 ~30% dividends, Samsung 2026 >= 35%: mixed, so half); SK hynix stub 20,000 of 34,181;
# rest of Korea 100% (its 30% payout is dividends); SK Square pays nothing. Rate 15% = Korea-Ireland treaty portfolio rate
DIVSH={"S":0.5,"SP":0.5,"H":0.5,"Q":0.0,"K":1.0}; DIVST={"S":0.0,"SP":0.0,"H":20000/34181,"Q":0.0,"K":0.0}

def eps_mult(c,em):
    """v1.7 [A]: Base D and V at the analysis price with Base EPS 2027-30 x em[0..3]. The EPS change passes one for one into
    FCF (capex, D&A and working capital unchanged), into D_t by the payout rule, into net cash, and into V_t at the interim P/E
    the published marks imply on next-year EPS (exit P/E 10 on 2030)."""
    y=c["Base"]; E=y["EPS"]; D=list(y["D"]); V=list(y["V"])
    dE=[E[i]*(em[i]-1) for i in range(4)]
    a,b=c["PAY"]; nc=0.0; prevF=0.0
    for i in range(3):
        pe=(y["V"][i]-c["NCB"][i]-c["STK"])/E[i+1]
        dD=a*dE[i]+b*prevF; D[i]+=dD; nc+=dE[i]-dD; prevF=dE[i]
        V[i]+=pe*dE[i+1]+nc
    return D,V

def comp_path(c,s,P,em=None):
    """per-share D and V at price P; Base/Bull interim marks keep the analysis glide (price change fades by exit),
    the decision Bear is independent of P from end-2027, the capped Bear scales the multiple part."""
    y=c[s]; D=list(y["D"]); V=list(y["V"])
    if em is not None and s=="Base": D,V=eps_mult(c,em)
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

def blocks(s,sh=0.0,ksh=0.0,keps=1.0,hp=1.0,em=None):
    """per-unit-of-price paths (P = 1) for each block: dict b -> (D[3], V[3], stubD)"""
    out={}
    D,V=comp_path(CS,s,CS["P"],em)
    if hp!=1.0: V=[v*hp for v in V]
    if sh and s!="Cap": V[2]+=sh*CS[s]["EPS"][3]*(em[3] if em is not None and s=="Base" else 1)
    out["S"]=([d/CS["P"] for d in D],[v/CS["P"] for v in V],0.0)
    out["SP"]=([d/PREF["P"] for d in D],[v*(1-DISC[s][i])/PREF["P"] for i,v in enumerate(V)],0.0)
    D,V=comp_path(CH,s,CH["P"],em)
    if hp!=1.0: V=[v*hp for v in V]
    if sh and s!="Cap": V[2]+=sh*CH[s]["EPS"][3]*(em[3] if em is not None and s=="Base" else 1)
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
    w=dict(w0); Dst=sum(w[b]*B[b][2]*(1-WHT*DIVST[b]) for b in w)*100
    u=dict(UNC)                                     # uncapped market weights (KOSPI 200 proxy)
    w=recap(w,u,rule)                               # December 2026 reviews (MSCI 1 Dec, FTSE ~21 Dec): stub is price-flat
    Vprev=100.0; Ds=[]; Vs=[]; r=[]
    vb={b:w[b]*100 for b in w}                      # value per block at the end of the stub (price flat)
    for i in range(3):
        newv={}; d=0.0; nu={}
        for b in w:
            Db,Vb,_=B[b]
            lvl_prev=Vb[i-1] if i else 1.0
            d+=vb[b]*Db[i]*(1-WHT*DIVSH[b])/lvl_prev; newv[b]=vb[b]*Vb[i]/lvl_prev; nu[b]=u[b]*Vb[i]/lvl_prev
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
                d=dd,g=g,c=I-dd-g,r=r,rn=rn,V=Vs,D=Ds,Dst=fl[1][1])

def stubfl(x):
    """v1.7 fix: the stub distribution as a cash flow in the TRIG and cost lines (left out in v1.6; NOFIX restores that)"""
    return [(STUB,x["Dst"])] if FIX else []

def eps_lookthrough(w,s="Base"):
    """CY27-consensus earnings per 100 of price and the S+H share; EPS path rel. to CY27 consensus"""
    e={"S":w["S"]/(CS["P"]/CS["CONS"]),"SP":w["SP"]/(PREF["P"]/CS["CONS"]),"H":w["H"]/(CH["P"]/CH["CONS"]),
       "Q":w["Q"]/QPE,"K":w["K"]/KPE0}
    tot=sum(e.values())
    return 1/tot, (e["S"]+e["SP"]+e["H"])/tot, (e["S"]+e["SP"]+e["H"]+e["Q"])/tot

# ---- holdings (weights of the equity portfolio, repriced to 26 Oct) ----
D_=json.load(open(os.path.join(HERE,"korea_data.json")))[VD]
KPE0=D_["KPE0"]; QPE=D_["QPE"]
ETF=D_["etf"]; UNC=dict(ETF["KOSPI200"])
# UCITS funds (Xetra on Nordnet): start at their cap levels after the December review; SK Square as observed (31 Aug);
# preference share of the Samsung weight as observed; the rest of Korea takes the remainder [A]
for nm,(q,pf) in {"FLXK":(0.0372,3.39/29.28),"IQQK":(0.0384,3.42/31.24),"LKOR":(0.0383,3.41/31.15),"DBX8":(0.0427,3.37/30.41)}.items():
    cs,ch_,_=CAPS[nm]; ETF[nm]={"S":cs*(1-pf),"SP":cs*pf,"H":ch_,"Q":q,"K":1-cs-ch_-q}
if DAILY and "IQQK_d" in ETF: ETF["IQQK"]=dict(ETF["IQQK_d"])   # v1.7: IQQK's 2 Nov daily holdings file (v1.8: 4 Nov), repriced (korea_prep.py)
# IQQK, LKOR, DBX8: Nordnet's total cost from the fund's KID (api/2/instruments, 29 Oct; TER 0.65 / 0.45 / 0.45)
FEE={"EWY":0.0059,"FLKR":0.0009,"KORX":0.0045*1.13,"FLXK":0.0009,"IQQK":0.0074,"LKOR":0.0065,"DBX8":0.0065,
     "KOSPI200":0.0,"S+H":0.0,"K":0.0}
RULE={"EWY":"EWY","FLKR":"FLKR","KORX":None,"FLXK":"FLXK","IQQK":"IQQK","LKOR":"LKOR","DBX8":"DBX8",
      "KOSPI200":None,"S+H":None,"K":None}

def report(name,w,**kw):
    res={s:run_etf(w,FEE[name],RULE[name],s,**kw) for s in SC}
    E=(res["Base"]["irr"]-nibw)*100
    Rd=(res["Base"]["rn"][0]-res["Bear"]["rn"][0])*100; Rc=(res["Base"]["rn"][0]-res["Cap"]["rn"][0])*100
    return res,E,Rd,Rc

if __name__=="__main__":
    print(f"valuation {VD}  Samsung {'v1' if S1 else 'v2'}  SK hynix {'v1' if H1 else 'v2'}  NIBOR window {nibw*100:.2f}%  T {T:.3f}  rest P/E CY27 {KPE0:.2f}  holdco P/E {QPE:.2f}  pref discount {DISC0:.3f}")
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
        for lab,wht,spr in ((("after the bid-ask round trip",0,1),("Korean withholding 15% inside the funds on all D_t",0.15,0),("both",0.15,1))
                            if WHT==0 else (("after the bid-ask round trip (withholding in the paths)",0,1),)):
            out=[]
            for nm in ["KORX","EWY","FLKR","FLXK"]:
                res=run_etf(ETF[nm],FEE[nm],RULE[nm],"Base"); x=res
                fl=[(0,-100*(1+SPREAD[nm]/2*spr))]+[(t,c*(1-wht)) for t,c in stubfl(x)]+[(STUB+i+0.5,x["D"][i]*(1-wht)) for i in range(3)]+[(T,x["V"][2]*(1-SPREAD[nm]/2*spr))]
                out.append(f"{nm} Base {irr(fl)*100:5.1f}")
            print(f"{lab:38s} "+" | ".join(out))
    if "FUND" in sys.argv:          # one fund in full: py korea.py FUND IQQK
        nm=sys.argv[sys.argv.index("FUND")+1]; w=ETF[nm]; pe,sh,shq=eps_lookthrough(w)
        sg=w["S"]+w["SP"]; parts={nm:(w,FEE[nm],RULE[nm]),
            "S+H part":({"S":w["S"]/(sg+w["H"]),"SP":w["SP"]/(sg+w["H"]),"H":w["H"]/(sg+w["H"]),"Q":0,"K":0},0.0,None),
            "rest":({"S":0,"SP":0,"H":0,"Q":0,"K":1.0},0.0,None)}
        print(f"\n{nm} at {VD}: S {w['S']*100:.1f} pref {w['SP']*100:.1f} H {w['H']*100:.1f} SK Square {w['Q']*100:.1f} rest {w['K']*100:.1f}"
              f" | P/E CY27 {pe:.2f} | S+H share of CY27 earnings {sh:.1%} (+SK Square {shq:.1%}) | fee {FEE[nm]*100:.2f}%")
        for lab,(ww,fee,rule) in parts.items():
            res={s:run_etf(ww,fee,rule,s) for s in SC}
            E=(res["Base"]["irr"]-nibw)*100; Rc=(res["Base"]["rn"][0]-res["Cap"]["rn"][0])*100; Rd=(res["Base"]["rn"][0]-res["Bear"]["rn"][0])*100
            print(f" {lab}:")
            for s in SC:
                x=res[s]
                print(f"  {s:4s} IRR {x['irr']*100:5.1f} d/g/c {x['d']*100:.1f}/{x['g']*100:.1f}/{x['c']*100:.1f} | D {[round(v,1) for v in x['D']]} V {[round(v,1) for v in x['V']]} r {[round(v*100,1) for v in x['rn']]}"
                      f" | sumD {x['sumD']:.1f} VT {x['VT']:.1f} Pk {x['Pk']:.1f} MoS {x['mos']:+.1%} capital {x['kept']:+.1%}")
            print(f"  E {E:.1f} R capped {Rc:.1f} E/R {E/Rc:.3f} | decision-Bear E/R {E/Rd if Rd>0 else float('nan'):.3f}")
            if lab==nm:
                wts={"Bear":.25,"Base":.5,"Bull":.25}
                Dw=[sum(wts[s]*res[s]["D"][i] for s in wts) for i in range(3)]; Vw=sum(wts[s]*res[s]["V"][2] for s in wts)
                print(f"  scenario-weighted reference {irr([(0,-100)]+[(STUB+i+0.5,Dw[i]) for i in range(3)]+[(T,Vw)])*100:.1f}")
        if "SPOT" in sys.argv:      # v1.7: the iaf-valuation FX rule (decision at spot FX held flat in all scenarios)
            FX0=copy.deepcopy(FX)
            for s_ in ("Bear","Bull","Cap"): FX[s_]=[1.0,1.0,1.0]
            print(f" {nm} at spot FX held flat (KRW = NOK = EUR from today's rates; the paths above use the Equity BBB I-44 path in Bear and Bull):")
            for s_ in SC:
                x=run_etf(w,FEE[nm],RULE[nm],s_)
                print(f"  {s_:4s} IRR {x['irr']*100:5.1f} | 2027 {x['rn'][0]*100:5.1f} | D {[round(v,1) for v in x['D']]} V {[round(v,1) for v in x['V']]} r {[round(v*100,1) for v in x['rn']]}"
                      f" | sumD {x['sumD']:.1f} VT {x['VT']:.1f} Pk {x['Pk']:.1f} MoS {x['mos']:+.1%} capital {x['kept']:+.1%}")
            FX.update(FX0)
        def one(lab,**kw):
            res,E,Rd,Rc=report(nm,w,**kw); print(f"  {lab:44s} {res['Base']['irr']*100:5.1f} / {res['Cap']['irr']*100:5.1f} / {res['Cap']['rn'][0]*100:5.1f} / {E/Rc:.3f}")
        print(" sensitivities: Base / capped IRR / capped 2027 / E/R")
        one("model"); one("S and H exit P/E -2",sh=-2); one("S and H exit P/E +2",sh=2); one("S and H values x0.8",hp=0.8)
        one("rest exit P/E -2 (all scenarios)",ksh=-2); one("rest exit P/E +2",ksh=2); one("rest EPS x0.9",keps=0.9)
        one("adverse together",hp=0.8,keps=0.9,ksh=-2)
        KCONV=0.30; one("rest cash conversion 0.30"); KCONV=0.50
        FX0=copy.deepcopy(FX); FX["Cap"]=[1.0,1.0,1.0]; one("capped Bear without the I-44 cushion"); FX.update(FX0)
        R0=RULE[nm]; RULE[nm]=None; one("no re-capping"); RULE[nm]=R0
        lo,hi=0.1,1.5
        for _ in range(60):
            m=(lo+hi)/2; r=run_etf(w,FEE[nm],RULE[nm],"Base",hp=m)["irr"]
            if r<K: lo=m
            else: hi=m
        print(f"  S and H values for k: x{m:.3f}")
        TER={"IQQK":0.0065,"LKOR":0.0045,"DBX8":0.0045}
        if nm in TER:
            print(f"  {'cost at TER '+format(TER[nm]*100,'.2f')+'%':44s} Base {run_etf(w,TER[nm],RULE[nm],'Base')['irr']*100:5.1f}")
        lo,hi=-5.0,10.0
        for _ in range(60):
            m=(lo+hi)/2; r=run_etf({"S":0,"SP":0,"H":0,"Q":0,"K":1.0},0.0,None,"Base",ksh=m)["irr"]
            lo,hi=(m,hi) if r<K else (lo,m)
        print(f"  rest of Korea exit P/E for k on its own: {KPEX['Base']+m:.1f}")
        b=run_etf(w,FEE[nm],RULE[nm],"Base")
        cl=(("bid-ask round trip 0.2%",0,0.002),("Korean withholding 15% on all D_t",0.15,0)) if WHT==0 else (("bid-ask round trip 0.2%",0,0.002),)
        for lab,wht,spr in cl:
            fl=[(0,-100*(1+spr/2))]+[(t,c*(1-wht)) for t,c in stubfl(b)]+[(STUB+i+0.5,b["D"][i]*(1-wht)) for i in range(3)]+[(T,b["V"][2]*(1-spr/2))]
            print(f"  {lab:44s} Base {irr(fl)*100:5.1f}")
        if WHT>0:        # v1.7: withholding is in the paths; the lines below replace it, never add to it
            DS0,DT0=dict(DIVSH),dict(DIVST)
            DIVSH.update({k:(1.0 if k!="Q" else 0.0) for k in DIVSH}); DIVST.update({"H":1.0})
            x=run_etf(w,FEE[nm],RULE[nm],"Base"); print(f"  {'withholding 15% on all D_t (upper bound)':44s} Base {x['irr']*100:5.1f} P_k {x['Pk']:.1f}")
            DIVSH.update(DS0); DIVST.update(DT0)
            W0=WHT; WHT=0.22; x=run_etf(w,FEE[nm],RULE[nm],"Base"); print(f"  {'22% on the dividend part (no treaty relief)':44s} Base {x['irr']*100:5.1f} P_k {x['Pk']:.1f}")
            WHT=0.0; x=run_etf(w,FEE[nm],RULE[nm],"Base"); print(f"  {'no withholding (v1.6 basis)':44s} Base {x['irr']*100:5.1f} P_k {x['Pk']:.1f}"); WHT=W0
    if "IMPL" in sys.argv:          # v1.7: what the price implies about the memory cycle (py korea.py FUND IQQK IMPL)
        nm=sys.argv[sys.argv.index("FUND")+1] if "FUND" in sys.argv else "IQQK"; w=ETF[nm]
        def cirr(c,em,P=None,sh=0.0):        # one company block in KRW, no fee and no fund withholding, at price P
            P=P or c["PF"]; D,V=comp_path(c,"Base",P,em); V=list(V); V[2]+=sh*c["Base"]["EPS"][3]*em[3]
            return irr([(0,-P),(STUB,c.get("DST",0))]+[(STUB+i+0.5,D[i]) for i in range(3)]+[(T,V[2])])
        print("\n reconstruction check (company analyses at their own prices, KRW): the EPS multiplier vs their own sensitivities")
        print(f"  SK hynix 2030 EPS x0.6 {cirr(CH,[1,1,1,.6])*100:5.1f}% (analysis 8.8%) | whole path x0.81 {cirr(CH,[.81]*4)*100:5.1f}% (analysis: 12% at -19%)")
        print(f"  Samsung 2030 EPS x0.636 (= memory x0.6) {cirr(CS,[1,1,1,.636])*100:5.1f}% (analysis 13.0%) | x0.545 (memory x0.5) {cirr(CS,[1,1,1,.545])*100:5.1f}% (analysis 10.0%)"
              f" | whole path x0.75 (memory -27%) {cirr(CS,[.75]*4)*100:5.1f}% (analysis: 12%)")
        nc=[.35/.90,.35/.60,.35/.40,1.0]
        print(f"  structural (2030 EPS from 2027): Samsung {cirr(CS,nc)*100:5.1f}% (analysis 16.8%) | SK hynix {cirr(CH,nc)*100:5.1f}% (analysis 12.9%)")
        def solve(f,target,lo=0.0,hi=2.5):
            for _ in range(70):
                m=(lo+hi)/2
                if f(m)<target: lo=m
                else: hi=m
            return m
        print(f" single names at the {VD} close (KRW, no fee), 2028-30 EPS x m (2027 at Base) for k / for 0%:")
        for lab,c in (("Samsung",CS),("SK hynix",CH)):
            print(f"  {lab:8s} P {c['P']:,} Base {cirr(c,[1]*4,c['P'])*100:5.1f}% | k at x{solve(lambda m:cirr(c,[1,m,m,m],c['P']),K):.2f} | 0% at x{solve(lambda m:cirr(c,[1,m,m,m],c['P']),0.0):.2f}")
        fi=lambda m,sh=0.0,al=False: run_etf(w,FEE[nm],RULE[nm],"Base",em=([m]*4 if al else [1,m,m,m]),sh=sh)["irr"]
        print(f" {nm} (NOK after cost and withholding), Samsung and SK hynix Base EPS x m, rest of Korea at Base:")
        print(f"  model Base {fi(1.0)*100:.1f}%")
        for lab,sh in (("exit P/E 10 (Base)",0.0),("exit P/E 8",-2.0),("exit P/E 11",1.0)):
            print(f"  {lab:20s} 2028-30 x m: k at x{solve(lambda m:fi(m,sh),K):.2f}, 0% at x{solve(lambda m:fi(m,sh),0.0):.2f} | all years x m: k at x{solve(lambda m:fi(m,sh,True),K):.2f}, 0% at x{solve(lambda m:fi(m,sh,True),0.0):.2f}")
        B=(.90,.60,.40,.35)
        P={"Base: turn in 2028":B,"Earlier turn (prices fall from 2H-27)":(.80,.45,.35,.35),"Later turn (hold through 2028)":(.95,.85,.55,.40),
           "Shallower (LTA floors hold)":(.90,.70,.55,.45),"Deeper (2019 depth, pre-AI mid-cycle)":(.90,.45,.30,.25),
           "Bull path":(1.00,.80,.55,.45),"Bear path (at Base exit P/E)":(.60,.30,.25,.25),"No cycle: the 2030 level from 2027":(.35,.35,.35,.35)}
        print(f" {nm} on the AI BBB's named memory paths (EPS 2027/28/29/2030, CY27 consensus = 1), Base mechanics; exit P/E 10 / 8:")
        for lab,e in P.items():
            em=[e[i]/B[i] for i in range(4)]
            ra=run_etf(w,FEE[nm],RULE[nm],"Base",em=em); a=ra["irr"]; b8=run_etf(w,FEE[nm],RULE[nm],"Base",em=em,sh=-2)["irr"]
            print(f"  {lab:40s} {'/'.join(f'{x:.2f}' for x in e)}  {a*100:5.1f}% / {b8*100:5.1f}%  | P_k {ra['Pk']:.1f} (MoS {ra['mos']:+.1%})")
    if "TRIG" in sys.argv:
        HYREF=0.254 if VD>="2026-11-05" else 0.196   # HY market reference E / R: hy-funds 31 Oct (0.196); HY BBB 5 Nov (0.254)
        for nm in ["KORX","EWY","FLKR","FLXK","IQQK","LKOR","DBX8","KOSPI200"]:
            res,E,Rd,Rc=report(nm,ETF[nm])
            b=res["Base"]; c=res["Cap"]
            def at(x):        # ETF price x (1 = today) at unchanged paths
                fl=[(0,-100*x)]+stubfl(b)+[(STUB+i+0.5,b["D"][i]) for i in range(3)]+[(T,b["V"][2])]
                I=irr(fl); r0=(b["D"][0]+b["V"][0])/(100*x*(1-FEE[nm])**STUB)-1; rc=(c["D"][0]+c["V"][0])/(100*x*(1-FEE[nm])**STUB)-1
                return I,(I-nibw)*100/((r0-rc)*100)
            lo,hi=0.5,3.0
            for _ in range(80):
                m=(lo+hi)/2; lo,hi=(m,hi) if at(m)[1]>HYREF else (lo,m)
            print(f"{nm}: k trigger {b['mos']:+.1%} | E/R = {HYREF} at {m-1:+.1%} (Base IRR there {at(m)[0]*100:.1f}%)")
