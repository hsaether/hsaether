# DNB Teknologi A — look-through IAF build on the Equity Market BBB grid (World scenarios)
import json
H=json.load(open("hold.json")); C=json.load(open("closes.json"))
# holding: (weight %, block, CY26 EPS, CY27 EPS) in the price currency of the Yahoo listing
# weights: top 10 from DNB AM (holdings 16 Sep 2026); others Nordnet (31 Aug 2026); Korea split [A] (Korea 4.97% on 16 Sep, 10 Sep split scaled)
# blocks: company analyses CM = Microsoft, CG = Alphabet, CN = NVIDIA, CT = TSMC, CA = Amazon (docs/<co>-analysis.md); E = META on the AI BBB 'E rest' row
# CY mapping: FY Jun/Jul = half-year blend; FY Jan/Mar next year -> CY of most months; FY Sep/Oct -> same CY
def e(s,p): return H[s]["tr"][p]["eps"]
def ya(s): return H[s]["tr"]["0y"]["ya"]
HOLD={
"MSFT":(9.34,"CM",.5*ya("MSFT")+.5*e("MSFT","0y"),.5*e("MSFT","0y")+.5*e("MSFT","+1y")),
"GOOGL":(7.15,"CG",None,e("GOOGL","+1y")),      # CY26 includes one-off gains: growth taken as P block median [A]
"NVDA":(5.62,"CN",e("NVDA","0y"),15.21),   # CY27 calendarised by quarters (docs/nvda-analysis.md, AI BBB 17 Oct)
"AMZN":(5.06,"CA",None,e("AMZN","+1y")),        # same as GOOGL
"V":(3.99,"X",e("V","0y"),e("V","+1y")),
"MA":(3.90,"X",e("MA","0y"),e("MA","+1y")),
"AVGO":(3.75,"H1",e("AVGO","0y"),e("AVGO","+1y")),
"META":(4.33,"E",e("META","0y"),e("META","+1y")),
"ERIC-B.ST":(3.67,"X",e("ERIC-B.ST","0y"),e("ERIC-B.ST","+1y")),
"SAP.DE":(2.96,"T",e("SAP.DE","0y"),e("SAP.DE","+1y")),
"ADYEN.AS":(3.02,"X",e("ADYEN.AS","0y"),e("ADYEN.AS","+1y")),
"TEAM":(2.93,"T",None,None),                   # +1y estimate (n8) inconsistent; Yahoo forward P/E used [A]
"6758.T":(2.41,"X",e("6758.T","0y"),e("6758.T","+1y")),
"DSY.PA":(2.22,"T",e("DSY.PA","0y"),e("DSY.PA","+1y")),
"TMUS":(1.99,"X",e("TMUS","0y"),e("TMUS","+1y")),
"TSM":(1.97,"CT",e("TSM","0y"),e("TSM","+1y")),
"005930.KS":(1.81,"H2",e("005930.KS","0y"),e("005930.KS","+1y")),
"000660.KS":(1.97,"H2",e("000660.KS","0y"),e("000660.KS","+1y")),
"005935.KS":(1.19,"H2",e("005930.KS","0y"),e("005930.KS","+1y")),
"LOGI":(1.65,"X",e("LOGI","0y"),e("LOGI","+1y")),
"HPQ":(1.63,"X",e("HPQ","0y"),e("HPQ","+1y")),
"INTU":(1.40,"T",.58*ya("INTU")+.42*e("INTU","0y"),.58*e("INTU","0y")+.42*e("INTU","+1y")),
"7974.T":(1.30,"X",e("7974.T","0y"),e("7974.T","+1y")),
"NOD.OL":(1.27,"X",e("NOD.OL","0y"),e("NOD.OL","+1y")),   # EPS on Yahoo is NOK per share (fwd P/E 36.4 consistent)
"SWKS":(1.24,"X",e("SWKS","0y"),e("SWKS","+1y")),
"BKNG":(1.23,"X",e("BKNG","0y"),e("BKNG","+1y")),
}
rows=[]
for s,(w,b,a,c) in HOLD.items():
    px=C[s]["14"]   # close on the NAV date (15 Oct 2026; key "14" = date passed to close.py)
    if s=="TEAM": pe27=H[s]["fpe"]*C[s]["14"]/H[s]["px"]; g=None
    else:
        pe27=px/c; g=(c/a-1) if a else None
    dy=(H[s]["dy"] or 0)*100
    rows.append((s,w,b,pe27,g,dy)); print(f"{s:10s} {b:3s} w {w:5.2f} PE27 {pe27:6.1f} gEPS27 {'' if g is None else f'{g:+.0%}':>6s} dy {dy:.2f}")
B={}
for s,w,b,pe,g,dy in rows:
    x=B.setdefault(b,dict(w=0,e=0,eg=0,ew=0,dy=0)); x["w"]+=w; x["e"]+=w/pe; x["dy"]+=w*dy
    if g is not None: x["eg"]+=w/pe/(1+g); x["ew"]+=w/pe
W=sum(x["w"] for x in B.values()); E=sum(x["e"] for x in B.values())
print("\nsample weight",round(W,2))
for b,x in sorted(B.items()):
    print(f"{b:3s} w {x['w']:5.2f} ({x['w']/W:.0%}) PE27 {x['w']/x['e']:5.1f} earn share27 {x['e']/E:.0%} EPS g CY27 {(x['ew']/x['eg']-1) if x['eg'] else float('nan'):+.0%} dy {x['dy']/x['w']:.2f}")
eg=sum(x["eg"] for x in B.values()); ew=sum(x["ew"] for x in B.values())
print(f"FUND sample PE27 {W/E:.1f}  EPS g CY26->27 (ex GOOGL/AMZN/TEAM) {ew/eg-1:+.1%}  div yield {sum(x['dy'] for x in B.values())/W:.2f}")
json.dump({b:dict(w=x["w"]/W,pe27=x["w"]/x["e"],share=x["e"]/E) for b,x in B.items()},open("blocks.json","w"),indent=1)
