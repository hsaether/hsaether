# Korea ETFs: holdings -> block weights repriced to the valuation-date Seoul close (26, 28 and 29 Oct and 4 Nov 2026); rest-of-Korea
# P/E on the 26 Oct consensus. Writes korea_data.json with one entry per valuation date (v1.4, 28 Oct: 28 Oct closes added;
# v1.6, 29 Oct: 29 Oct closes added; v1.7, 4 Nov: 30 Oct, 2, 3 and 4 Nov closes added, and IQQK's own daily holdings file;
# v1.8, 6 Nov: 5 and 6 Nov closes added, and IQQK's daily holdings file of 4 Nov for the 6 Nov entry).
# Holdings: EWY iShares latest-holdings.csv (23 Oct 2026); FLKR Zacks get_etf_holdings (1 Oct 2026; Yahoo topHoldings
# agrees on the top 10 and gives stock 99.48% / cash 0.46%); KORX Global X Canada product page (top 10, 30 Sep 2026);
# IQQK iShares UK (IKOR) latest-holdings.csv of 2 Nov 2026 (korea_prices.json "iqqk_holdings_ishares_2nov"), used from v1.7;
# of 4 Nov 2026 ("iqqk_holdings_ishares_4nov"), used from v1.8 (6 Nov entry).
# Prices and CY26/CY27 consensus: Yahoo (korea_prices.json: consensus and closes fetched 26 Oct; 27-28 Oct closes fetched 28 Oct;
# 29 Oct closes fetched 29 Oct after the Seoul close; 30 Oct-4 Nov closes fetched 4 Nov 07:25 UTC, after the Seoul close;
# 5-6 Nov closes fetched 6 Nov ~07:00 UTC, after the Seoul close).
import json, os
ALL={}
HERE=os.path.dirname(os.path.abspath(__file__))
X=json.load(open(os.path.join(HERE,"korea_prices.json")))
C=X["consensus_yahoo_26oct"]; PX=X["closes_yahoo"]
P26={"005930.KS":213250,"005935.KS":164800,"000660.KS":1282000,"402340.KS":774000}   # Yahoo quote 26 Oct (15:10 KST stamp)
def p(s,d):
    if d=="2026-10-26" and s in P26: return P26[s]
    return PX[s][d]
EWY={"005930.KS":22.81,"000660.KS":22.34,"402340.KS":2.64,"009150.KS":2.53,"105560.KS":2.17,"055550.KS":1.61,"005380.KS":1.56,
 "086790.KS":1.44,"068270.KS":1.42,"006400.KS":1.36,"035420.KS":1.19,"012450.KS":1.17,"034020.KS":1.15,"000270.KS":1.14,"028260.KS":1.11,
 "316140.KS":1.03,"033780.KS":1.02,"373220.KS":1.00,"000810.KS":0.99,"032830.KS":0.98,"207940.KS":0.96,"005490.KS":0.93,"012330.KS":0.91,
 "066570.KS":0.89,"034730.KS":0.73,"138040.KS":0.73,"196170.KQ":0.70,"010120.KS":0.66,"005830.KS":0.66,"018260.KS":0.66,"003550.KS":0.64,
 "051910.KS":0.62,"010140.KS":0.61,"009540.KS":0.60,"035720.KS":0.60,"011200.KS":0.58,"000100.KS":0.56,"267260.KS":0.55,"003490.KS":0.55,
 "298040.KS":0.54,"086280.KS":0.54,"010950.KS":0.54,"024110.KS":0.53,"042700.KS":0.53,"329180.KS":0.53,"042660.KS":0.44,"005935.KS":0.05}
EWY_TAIL=98.90-sum(EWY.values())          # equities 98.90% (cash and futures 1.10%); the other 35 names at the rest's move
FLKR={"000660.KS":19.65,"005930.KS":18.52,"402340.KS":4.35,"009150.KS":3.66,"105560.KS":2.63,"005935.KS":2.47,"005380.KS":2.11,
 "055550.KS":2.06,"034020.KS":1.61,"086790.KS":1.57,"012450.KS":1.48,"006400.KS":1.39,"035420.KS":1.31,"000270.KS":1.23,"028260.KS":1.21,
 "068270.KS":1.18,"316140.KS":1.10,"032830.KS":1.05,"005490.KS":1.04,"066570.KS":1.00,"012330.KS":0.95,"034730.KS":0.93,"000810.KS":0.90,
 "373220.KS":0.77,"033780.KS":0.77,"207940.KS":0.73,"267260.KS":0.69,"010120.KS":0.69,"009540.KS":0.66,"298040.KS":0.64,"329180.KS":0.63,
 "010140.KS":0.59,"196170.KQ":0.58,"051910.KS":0.54,"042660.KS":0.51,"035720.KS":0.47,"042700.KS":0.44,"OTHER":0.48}  # SK Innovation -> OTHER
FLKR_TAIL=99.48*sum(FLKR.values())/sum(FLKR.values())  # placeholder, set below
KORX={"005930.KS":34.37,"000660.KS":27.27,"402340.KS":2.81,"009150.KS":2.27,"105560.KS":1.34,"005380.KS":1.28,"055550.KS":1.13,
 "034020.KS":0.95,"012450.KS":0.86+0.03,"006400.KS":0.86}
KORX["012450.KS"]=0.89
for VD in ("2026-10-26","2026-10-28","2026-10-29","2026-11-04","2026-11-06"):
    REST=[s for s in EWY if s not in ("005930.KS","005935.KS","000660.KS","402340.KS","034730.KS")]
    W=sum(EWY[s] for s in REST)
    def restmove(d0):
        return sum(EWY[s]*p(s,VD)/p(s,d0) for s in REST)/W
    mv={d:restmove(d) for d in ("2026-09-30","2026-10-01","2026-10-23")+(("2026-11-02",) if VD>="2026-11-02" else ())+(("2026-11-04",) if VD>="2026-11-06" else ())}
    KPE0=W/sum(EWY[s]*C[s]["eps27"]/p(s,VD) for s in REST)
    KPE0_26=W/sum(EWY[s]*C[s]["eps26"]/p(s,VD) for s in REST)
    Qw={"402340.KS":2.64,"034730.KS":0.73}
    QPE=sum(Qw.values())/sum(w*C[s]["eps27"]/p(s,VD) for s,w in Qw.items())
    def blocks(h,d0,tail):
        v={"S":0,"SP":0,"H":0,"Q":0,"K":0}
        for s,w in h.items():
            if s=="OTHER": v["K"]+=w*mv[d0]; continue
            m=p(s,VD)/p(s,d0); b={"005930.KS":"S","005935.KS":"SP","000660.KS":"H","402340.KS":"Q","034730.KS":"Q"}.get(s,"K")
            v[b]+=w*m
        v["K"]+=tail*mv[d0]
        tot=sum(v.values()); return {b:x/tot for b,x in v.items()}, tot
    ewy,_=blocks(EWY,"2026-10-23",EWY_TAIL)
    flkr,_=blocks(FLKR,"2026-10-01",99.48-sum(FLKR.values()))
    korx,_=blocks(KORX,"2026-09-30",100-0.81-sum(KORX.values()))
    sh=korx["S"]+korx["H"]
    out=dict(KPE0=KPE0,KPE0_26=KPE0_26,QPE=QPE,restmove=mv,
      etf={"EWY":ewy,"FLKR":flkr,"KORX":korx,"KOSPI200":korx,
           "S+H":{"S":korx["S"]/sh,"SP":0.0,"H":korx["H"]/sh,"Q":0.0,"K":0.0},
           "K":{"S":0.0,"SP":0.0,"H":0.0,"Q":0.0,"K":1.0}},
      tails={"EWY":EWY_TAIL,"FLKR":99.48-sum(FLKR.values()),"KORX":100-0.81-sum(KORX.values())})
    if VD>="2026-11-02":
        # IQQK from its own daily holdings file (2 Nov; 4 Nov from the 6 Nov entry), repriced to VD: Samsung, preference, SK hynix,
        # SK Square at their closes; everything else (incl. SK Inc and cash) at the rest sample's move [A]. Weights of the whole fund.
        fk,d0=("iqqk_holdings_ishares_4nov","2026-11-04") if VD>="2026-11-06" else ("iqqk_holdings_ishares_2nov","2026-11-02")
        hq=X[fk]["weights_pct"]
        v={"S":hq["005930.KS"]*p("005930.KS",VD)/p("005930.KS",d0),"SP":hq["005935.KS"]*p("005935.KS",VD)/p("005935.KS",d0),
           "H":hq["000660.KS"]*p("000660.KS",VD)/p("000660.KS",d0),"Q":hq["402340.KS"]*p("402340.KS",VD)/p("402340.KS",d0)}
        v["K"]=(100-hq["005930.KS"]-hq["005935.KS"]-hq["000660.KS"]-hq["402340.KS"])*mv[d0]
        tot=sum(v.values()); out["etf"]["IQQK_d"]={b:x/tot for b,x in v.items()}; out["iqqk_move_"+("4nov" if VD>="2026-11-06" else "2nov")]=tot/100-1
    ALL[VD]=out
json.dump(ALL,open(os.path.join(HERE,"korea_data.json"),"w"),indent=1)
print(json.dumps({d:{k:v for k,v in o.items() if k!='etf'} for d,o in ALL.items()},indent=1))
print("rest sample weight in EWY",round(W,2),"of",round(98.90-22.81-0.05-22.34-2.64-0.73,2))
