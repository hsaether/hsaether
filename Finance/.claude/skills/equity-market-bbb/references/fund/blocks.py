# DNB Teknologi A — look-through IAF build (runs under iaf-valuation; model v7, 6 Nov 2026; v6 30 Oct)
# Reads hold.json (hold.py, consensus) and closes.json (close.py <NAV date> ...) from the working folder; writes blocks.json.
# Options: W0916 = holdings of 16 Sep (v5 weights); W0924 = holdings of 24 Sep / 31 Aug (v6 weights); default (v7) = 30 Sep; MEMLAYER = memory as one AI BBB H2 layer block (v5)
#          instead of the company blocks CS / CP / CH; LAST = the last close in closes.json instead of the NAV-date close.
import json, sys
H=json.load(open("hold.json")); C=json.load(open("closes.json"))
W0916="W0916" in sys.argv; W0924="W0924" in sys.argv or W0916; MEMLAYER="MEMLAYER" in sys.argv; LAST="LAST" in sys.argv
# holding: (weight %, block, CY26 EPS, CY27 EPS) in the price currency of the Yahoo listing
# weights: top 10 from DNB AM (holdings 24 Sep 2026; v5: 16 Sep); others Nordnet (31 Aug 2026; still the latest there on 30 Oct)
# Korea [A]: 24 Sep Samsung 3.06% (common + preference, split 60.3 / 39.7 as on 10 Sep), SK hynix = Korea 5.12% - 3.06% = 2.06%
#            (16 Sep: Korea 4.97% = 1.81 + 1.19 + 1.97). Adyen out of the 24 Sep top 10 (<= 3.06%): kept at 3.02% (16 Sep).
# blocks: company analyses CM Microsoft, CG Alphabet, CN NVIDIA, CT TSMC, CA Amazon, CS / CP Samsung common / preference,
#         CH SK hynix (docs/<co>-analysis.md); E = META on the AI BBB 'E rest' row; H1 Broadcom; T software; X not AI-led
# CY mapping: FY Jun/Jul = half-year blend; FY Jan/Mar next year -> CY of most months; FY Sep/Oct -> same CY
def e(s,p): return H[s]["tr"][p]["eps"]
def ya(s): return H[s]["tr"]["0y"]["ya"]
WT=dict(MSFT=9.34,GOOGL=7.15,NVDA=5.62,AMZN=5.06,V=3.99,MA=3.90,AVGO=3.75,META=4.33,ERIC=3.67,ADYEN=3.02,
        S=1.81,SP=1.19,SKH=1.97) if W0916 else \
   dict(MSFT=9.39,GOOGL=7.07,NVDA=5.92,AMZN=5.08,V=3.73,MA=3.85,AVGO=3.98,META=4.95,ERIC=3.54,ADYEN=3.02,
        S=3.06*1.81/3.00,SP=3.06*1.19/3.00,SKH=5.12-3.06) if W0924 else \
   dict(MSFT=9.62,GOOGL=7.07,NVDA=6.10,AMZN=5.05,V=3.62,MA=3.73,AVGO=4.18,META=4.60,ERIC=3.42,ADYEN=3.07,
        S=1.73,SP=4.91-1.99-1.73,SKH=1.99)
# v7 (30 Sep 2026): top 10 from DNB AM; the rest from Nordnet's full list of 30 Sep (25 lines >= 1.25%): Samsung common 1.73,
#   SK hynix 1.99; preference = Korea 4.91% (DNB AM) - 1.99 - 1.73 = 1.19% [A]; Nintendo left the list (< 1.25%), ASML entered (1.27%)
RW=dict(SAP=2.96,TEAM=2.93,SONY=2.41,DSY=2.22,TMUS=1.99,TSM=1.97,LOGI=1.65,HPQ=1.63,INTU=1.40,NTDO=1.30,NOD=1.27,SWKS=1.24,BKNG=1.23,ASML=0) if W0924 else \
   dict(SAP=2.82,TEAM=2.38,SONY=2.30,DSY=1.95,TMUS=2.19,TSM=2.37,LOGI=1.79,HPQ=1.34,INTU=1.40,NTDO=0,NOD=1.43,SWKS=1.27,BKNG=1.25,ASML=1.27)
MS,MP,MH=("H2","H2","H2") if MEMLAYER else ("CS","CP","CH")
HOLD={
"MSFT":(WT["MSFT"],"CM",.5*ya("MSFT")+.5*e("MSFT","0y"),.5*e("MSFT","0y")+.5*e("MSFT","+1y")),
"GOOGL":(WT["GOOGL"],"CG",None,e("GOOGL","+1y")),      # CY26 includes one-off gains
"NVDA":(WT["NVDA"],"CN",e("NVDA","0y"),15.21),        # CY27 calendarised by quarters (docs/nvda-analysis.md, AI BBB)
"AMZN":(WT["AMZN"],"CA",None,e("AMZN","+1y")),        # same as GOOGL
"V":(WT["V"],"X",e("V","0y"),e("V","+1y")),
"MA":(WT["MA"],"X",e("MA","0y"),e("MA","+1y")),
"AVGO":(WT["AVGO"],"H1",e("AVGO","0y"),e("AVGO","+1y")),
"META":(WT["META"],"E",e("META","0y"),e("META","+1y")),
"ERIC-B.ST":(WT["ERIC"],"X",e("ERIC-B.ST","0y"),e("ERIC-B.ST","+1y")),
"SAP.DE":(RW["SAP"],"T",e("SAP.DE","0y"),e("SAP.DE","+1y")),
"ADYEN.AS":(WT["ADYEN"],"X",e("ADYEN.AS","0y"),e("ADYEN.AS","+1y")),
"TEAM":(RW["TEAM"],"T",None,None),                   # +1y estimate (n8) inconsistent; Yahoo forward P/E used [A]
"6758.T":(RW["SONY"],"X",e("6758.T","0y"),e("6758.T","+1y")),
"DSY.PA":(RW["DSY"],"T",e("DSY.PA","0y"),e("DSY.PA","+1y")),
"TMUS":(RW["TMUS"],"X",e("TMUS","0y"),e("TMUS","+1y")),
"TSM":(RW["TSM"],"CT",e("TSM","0y"),e("TSM","+1y")),
"005930.KS":(WT["S"],MS,e("005930.KS","0y"),e("005930.KS","+1y")),
"000660.KS":(WT["SKH"],MH,e("000660.KS","0y"),e("000660.KS","+1y")),
"005935.KS":(WT["SP"],MP,e("005930.KS","0y"),e("005930.KS","+1y")),   # preference on common EPS
"LOGI":(RW["LOGI"],"X",e("LOGI","0y"),e("LOGI","+1y")),
"HPQ":(RW["HPQ"],"X",e("HPQ","0y"),e("HPQ","+1y")),
"INTU":(RW["INTU"],"T",.58*ya("INTU")+.42*e("INTU","0y"),.58*e("INTU","0y")+.42*e("INTU","+1y")),
"7974.T":(RW["NTDO"],"X",e("7974.T","0y"),e("7974.T","+1y")),
"NOD.OL":(RW["NOD"],"X",e("NOD.OL","0y"),e("NOD.OL","+1y")),   # EPS on Yahoo is NOK per share
"SWKS":(RW["SWKS"],"X",e("SWKS","0y"),e("SWKS","+1y")),
"BKNG":(RW["BKNG"],"X",e("BKNG","0y"),e("BKNG","+1y")),
"ASML.AS":(RW["ASML"],"H3",e("ASML.AS","0y") if "ASML.AS" in H else None,e("ASML.AS","+1y") if "ASML.AS" in H else 1),   # v7: AI BBB H3 foundry and equipment layer
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
    rows.append((s,w,b,pe27,g,dy)); print(f"{s:10s} {b:3s} w {w:5.2f} px {p:11.2f} PE27 {pe27:6.1f} gEPS27 {'' if g is None else f'{g:+.0%}':>6s} dy {dy:.2f}")
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
NAV=float(KV.get("NAV",7381.56)); STUBD=int(KV.get("STUB",56))   # v7: NAV 4 Nov 2026, valuation 5 Nov -> 56 days (v6: 7,375.01, 62)
USD,OTH=(0.6696,0.3148) if W0916 else (0.6692,0.3127) if W0924 else (0.6669,0.3120)   # DNB AM currency mix 16 Sep / 24 Sep / 30 Sep (NOK 1.56 / 1.81 / 2.11)
out["_meta"]=dict(model_weight=W,prices="last" if LAST else "nav-date",weights="16 Sep" if W0916 else "24 Sep" if W0924 else "30 Sep",
                  mem="H2 layer" if MEMLAYER else "company",nav=NAV,stub=STUBD,usd=USD,oth=OTH,
                  hold=[(s,w,b,round(pe,3)) for s,w,b,pe,g,dy in rows])
json.dump(out,open("blocks.json","w"),indent=1)
