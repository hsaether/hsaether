# DNB Teknologi A: estimate of the next NAV from the model holdings' closes after the NAV date (model v6, 30 Oct 2026) [A].
# Reads blocks.json (_meta: holdings and NAV) and closes.json (close.py with the FX crosses NOK=X KRW=X EURNOK=X SEKNOK=X
# JPYNOK=X) from the working folder. Each holding moves with its local close x its currency against NOK; the ~20% of NAV
# outside the model is assumed to move like the model; fund cost for the day ignored.
import json
B=json.load(open("blocks.json")); M=B["_meta"]; C=json.load(open("closes.json"))
def fx(t,k):
    v=lambda s:(C[s]["last"][1] if k=="last" else C[s]["14"])
    if t.endswith(".KS"): return v("NOK=X")/v("KRW=X")
    if t.endswith(".ST"): return v("SEKNOK=X")
    if t.endswith((".DE",".AS",".PA")): return v("EURNOK=X")
    if t.endswith(".T"): return v("JPYNOK=X")
    if t.endswith(".OL"): return 1.0
    return v("NOK=X")
tot=0; W=0; byb={}
for t,w,b,pe in M["hold"]:
    r=C[t]["last"][1]/C[t]["14"]*fx(t,"last")/fx(t,"14")-1
    tot+=w*r; W+=w; byb.setdefault(b,[0,0]); byb[b][0]+=w*r; byb[b][1]+=w
    print(f"{t:10s} {b:3s} w {w:5.2f} local {C[t]['last'][1]/C[t]['14']-1:+6.1%}  NOK {r:+6.1%}  ({C[t]['last'][0]})")
m=tot/W
print("by block", {b:f"{x[0]/x[1]:+.1%}" for b,x in byb.items()})
print(f"model move {m:+.2%} -> NAV {M['nav']:.2f} x {1+m:.4f} = {M['nav']*(1+m):.2f}  (USD/NOK {fx('MSFT','14'):.4f} -> {fx('MSFT','last'):.4f})")
