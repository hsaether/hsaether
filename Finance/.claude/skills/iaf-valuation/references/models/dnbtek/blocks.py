# DNB Teknologi A — look-through IAF build (docs/dnb-teknologi-analysis.md; runs under iaf-valuation; model v8, 16 Nov 2026;
# v7 6 Nov, v6 30 Oct). Reads hold.json (hold.py, consensus) and closes.json (close.py <NAV date>,<last date> ...) from the
# working folder; writes blocks.json.
# Options: W0930 = holdings of 30 Sep (v7 weights and currency mix); default (v8) = DNB AM factsheet of 30 Oct 2026 (top 10,
#          country and currency mix) with the rest at Nordnet's 30 Sep list; OLDFY = the v7 consensus mapping ("+1y" for
#          every FY Sep/Oct name: Visa and Skyworks then sit on FY2028 after Yahoo's fiscal-year roll); LAST = the last close
#          in closes.json instead of the NAV-date close; NAV=<NOK> STUB=<days to 31 Dec from the valuation date>.
# blocks: company analyses CM Microsoft, CG Alphabet, CN NVIDIA, CT TSMC, CA Amazon, CS / CP Samsung common / preference,
#         CH SK hynix (docs/<co>-analysis.md); E = META on the AI BBB 'E rest' row; H1 Broadcom; H3 ASML; T software; X not AI-led
# CY27 mapping (v8): the Yahoo trend period whose fiscal year is CY27 by most months: FY ending Sep-Dec 2027, or Jan-Mar 2028;
#   FY Jun/Jul = half-year blend (MSFT .5/.5, INTU .58/.42); NVIDIA calendarised by quarters (15.21, docs/nvda-analysis.md);
#   Atlassian on Yahoo's forward P/E (its +1y estimate is inconsistent).
import json, sys
H=json.load(open("hold.json")); C=json.load(open("closes.json"))
W0930="W0930" in sys.argv; OLDFY="OLDFY" in sys.argv; LAST="LAST" in sys.argv
def e(s,p): return H[s]["tr"][p]["eps"]
def ya(s): return H[s]["tr"]["0y"]["ya"]
def cy(s,y):
    """EPS of the fiscal year that is calendar year y by most months (FY end Sep-Dec of y, or Jan-Mar of y+1)"""
    if OLDFY: return e(s,"+1y") if y==2027 else e(s,"0y")
    for p in ("0y","+1y"):
        t=H[s]["tr"].get(p) or {}; end=t.get("end") or ""
        if not end: continue
        yy,mm=int(end[:4]),int(end[5:7])
        if (yy==y and mm>=9) or (yy==y+1 and mm<=3): return t["eps"]
    return None
WT=dict(MSFT=9.62,GOOGL=7.07,NVDA=6.10,AMZN=5.05,V=3.62,MA=3.73,AVGO=4.18,META=4.60,ERIC=3.42,ADYEN=3.07,
        S=1.73,SP=4.91-1.99-1.73,SKH=1.99) if W0930 else \
   dict(MSFT=8.41,GOOGL=6.80,NVDA=5.61,AMZN=4.84,V=3.49,MA=3.40,AVGO=4.57,META=3.52,ERIC=4.19,ADYEN=3.47,
        S=3.48*1.73/2.92,SP=3.48*1.19/2.92,SKH=5.40-3.48)
# v8 (30 Oct 2026, DNB AM factsheet): top 10 as published; Mastercard left the top 10 (<= Adyen's 3.47): 3.40 [A];
#   Samsung 3.48 (common + preference, one line) split as on 30 Sep (1.73 / 1.19) [A]; SK hynix = Korea 5.40 - Samsung 3.48 = 1.92;
#   from the country mix: TSMC = Taiwan 2.62 (the only Taiwan line on 25 Sep), SAP = Germany 2.72, Logitech = Switzerland 1.55
#   - Swisscom 0.01, Nordic Semiconductor = Norway 1.54 - Atea 0.08, ASML = Netherlands 4.85 - Adyen 3.47 - TomTom 0.24 [A];
#   the rest at Nordnet's 30 Sep list (the latest there on 16 Nov).
RW=dict(SAP=2.82,TEAM=2.38,SONY=2.30,DSY=1.95,TMUS=2.19,TSM=2.37,LOGI=1.79,HPQ=1.34,INTU=1.40,NOD=1.43,SWKS=1.27,BKNG=1.25,ASML=1.27) if W0930 else \
   dict(SAP=2.72,TEAM=2.38,SONY=2.30,DSY=1.95,TMUS=2.19,TSM=2.62,LOGI=1.54,HPQ=1.34,INTU=1.40,NOD=1.46,SWKS=1.27,BKNG=1.25,ASML=1.14)
HOLD={
"MSFT":(WT["MSFT"],"CM",.5*ya("MSFT")+.5*e("MSFT","0y"),.5*e("MSFT","0y")+.5*e("MSFT","+1y")),
"GOOGL":(WT["GOOGL"],"CG",None,e("GOOGL","+1y")),      # CY26 includes one-off gains
"NVDA":(WT["NVDA"],"CN",e("NVDA","0y"),15.21),        # CY27 calendarised by quarters (docs/nvda-analysis.md, AI BBB)
"AMZN":(WT["AMZN"],"CA",None,e("AMZN","+1y")),        # same as GOOGL
"V":(WT["V"],"X",cy("V",2026),cy("V",2027)),
"MA":(WT["MA"],"X",cy("MA",2026),cy("MA",2027)),
"AVGO":(WT["AVGO"],"H1",cy("AVGO",2026),cy("AVGO",2027)),
"META":(WT["META"],"E",cy("META",2026),cy("META",2027)),
"ERIC-B.ST":(WT["ERIC"],"X",cy("ERIC-B.ST",2026),cy("ERIC-B.ST",2027)),
"SAP.DE":(RW["SAP"],"T",cy("SAP.DE",2026),cy("SAP.DE",2027)),
"ADYEN.AS":(WT["ADYEN"],"X",cy("ADYEN.AS",2026),cy("ADYEN.AS",2027)),
"TEAM":(RW["TEAM"],"T",None,None),                   # +1y estimate inconsistent; Yahoo forward P/E used [A]
"6758.T":(RW["SONY"],"X",cy("6758.T",2026),cy("6758.T",2027)),
"DSY.PA":(RW["DSY"],"T",cy("DSY.PA",2026),cy("DSY.PA",2027)),
"TMUS":(RW["TMUS"],"X",cy("TMUS",2026),cy("TMUS",2027)),
"TSM":(RW["TSM"],"CT",cy("TSM",2026),cy("TSM",2027)),
"005930.KS":(WT["S"],"CS",cy("005930.KS",2026),cy("005930.KS",2027)),
"000660.KS":(WT["SKH"],"CH",cy("000660.KS",2026),cy("000660.KS",2027)),
"005935.KS":(WT["SP"],"CP",cy("005930.KS",2026),cy("005930.KS",2027)),   # preference on common EPS
"LOGI":(RW["LOGI"],"X",cy("LOGI",2026),cy("LOGI",2027)),
"HPQ":(RW["HPQ"],"X",cy("HPQ",2026),cy("HPQ",2027)),
"INTU":(RW["INTU"],"T",.58*ya("INTU")+.42*e("INTU","0y"),.58*e("INTU","0y")+.42*e("INTU","+1y")),
"NOD.OL":(RW["NOD"],"X",cy("NOD.OL",2026),cy("NOD.OL",2027)),   # EPS on Yahoo is NOK per share
"SWKS":(RW["SWKS"],"X",cy("SWKS",2026),cy("SWKS",2027)),
"BKNG":(RW["BKNG"],"X",cy("BKNG",2026),cy("BKNG",2027)),
"ASML.AS":(RW["ASML"],"H3",cy("ASML.AS",2026),cy("ASML.AS",2027)),   # AI BBB H3 foundry and equipment layer
}
HOLD={k:v for k,v in HOLD.items() if v[0]>0}
def px(s): return C[s]["last"][1] if LAST else C[s]["14"]   # key "14" = close on the date passed to close.py (the NAV date)
rows=[]; CONS={}
for s,(w,b,a,c) in HOLD.items():
    p=px(s)
    if s=="TEAM": pe27=H[s]["fpe"]*p/H[s]["px"]; g=None
    else:
        pe27=p/c; g=(c/a-1) if a else None
    if b.startswith("C"): CONS[b]=c
    dy=(H[s]["dy"] or 0)*100
    rows.append((s,w,b,pe27,g,dy)); print(f"{s:10s} {b:3s} w {w:5.2f} px {p:11.2f} EPS27 {c if c else 0:10.2f} PE27 {pe27:6.1f} gEPS27 {'' if g is None else f'{g:+.0%}':>6s} dy {dy:.2f}")
B={}
for s,w,b,pe,g,dy in rows:
    x=B.setdefault(b,dict(w=0,e=0,eg=0,ew=0,dy=0)); x["w"]+=w; x["e"]+=w/pe; x["dy"]+=w*dy
    if g is not None: x["eg"]+=w/pe/(1+g); x["ew"]+=w/pe
W=sum(x["w"] for x in B.values()); E=sum(x["e"] for x in B.values())
print("\nsample weight",round(W,2))
for b,x in sorted(B.items()):
    print(f"{b:3s} w {x['w']:5.2f} ({x['w']/W:.1%}) PE27 {x['w']/x['e']:5.2f} earn share27 {x['e']/E:.1%} EPS g CY27 {(x['ew']/x['eg']-1) if x['eg'] else float('nan'):+.0%} dy {x['dy']/x['w']:.2f}")
eg=sum(x["eg"] for x in B.values()); ew=sum(x["ew"] for x in B.values())
print(f"FUND sample PE27 {W/E:.2f}  EPS g CY26->27 (ex GOOGL/AMZN/TEAM) {ew/eg-1:+.1%}  div yield {sum(x['dy'] for x in B.values())/W:.2f}")
out={b:dict(w=x["w"]/W,pe27=x["w"]/x["e"],share=x["e"]/E) for b,x in B.items()}
for b,c in CONS.items(): out[b]["cons"]=c
# run settings for fundmodel.py: NAV (price P in NOK), stub days to 31 Dec, currency mix (USD, other foreign; rest NOK)
KV=dict(a.split("=",1) for a in sys.argv[1:] if "=" in a)
NAV=float(KV.get("NAV",7603.41)); STUBD=int(KV.get("STUB",48))   # v8: NAV 12 Nov 2026, valuation 13 Nov -> 48 days (v7: 7,381.56, 56)
USD,OTH=(0.6669,0.3120) if W0930 else (0.6283,0.3514)   # DNB AM currency mix 30 Sep / 30 Oct (NOK 2.11 / 2.03)
out["_meta"]=dict(model_weight=W,prices="last" if LAST else "nav-date",weights="30 Sep" if W0930 else "30 Oct",
                  mem="company",nav=NAV,stub=STUBD,usd=USD,oth=OTH,fy="old" if OLDFY else "v8",
                  hold=[(s,w,b,round(pe,3)) for s,w,b,pe,g,dy in rows])
json.dump(out,open("blocks.json","w"),indent=1)
