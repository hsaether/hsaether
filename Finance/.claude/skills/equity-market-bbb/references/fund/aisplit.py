import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M, copy
EPS0=copy.deepcopy(M.EPS); PEX0=copy.deepcopy(M.PEX); BL0=copy.deepcopy(M.BL); FXU0=copy.deepcopy(M.FXU); FXO0=copy.deepcopy(M.FXO)
def reset():
    M.EPS=copy.deepcopy(EPS0); M.PEX=copy.deepcopy(PEX0); M.BL.clear(); M.BL.update(copy.deepcopy(BL0)); M.FXU.update(copy.deepcopy(FXU0)); M.FXO.update(copy.deepcopy(FXO0))
AI=["CM","CG","E","H1","H2","H3","T"]
# 1) per-block IRR inside the fund (before cost), each block alone
print("Block alone, before cost (Bear/Base/Bull IRR NOK; 2027 Bear):")
for b in BL0:
    reset(); w=BL0[b]; M.BL.clear(); M.BL[b]=dict(w=1.0,pe27=w['pe27'],share=1.0)
    o,E,R=M.run(fee=0.0); print(f"  {b:3s} w {BL0[b]['w']*100:4.1f}% PE {w['pe27']:5.1f} | {o['Bear']['irr']*100:6.1f} {o['Base']['irr']*100:6.1f} {o['Bull']['irr']*100:6.1f} | Bear27 {o['Bear']['r'][0]*100:6.1f}")
# AI part vs non-AI part
for lab,keep in [("AI layers",AI),("Non-AI (X)",["X"])]:
    reset(); sub={b:BL0[b] for b in keep}; tw=sum(x['w'] for x in sub.values()); M.BL.clear()
    for b,x in sub.items(): M.BL[b]=dict(w=x['w']/tw,pe27=x['pe27'],share=0)
    pe=1/sum(x['w']/tw/x['pe27'] for x in sub.values())
    o,E,R=M.run(fee=0.0); print(f"{lab:10s} weight {tw*100:.1f}% of top-25 sample, P/E {pe:.1f} | before cost Bear {o['Bear']['irr']*100:.1f} Base {o['Base']['irr']*100:.1f} Bull {o['Bull']['irr']*100:.1f} | Bear27 {o['Bear']['r'][0]*100:.1f}")
# 2) AI-only Bear: AI layers on Bear, X on Base, NOK on Base (financing break without recession)
reset()
for s,tgt in [("Bear","Base"),("Bull","Base")]:
    M.EPS["X"][s]=list(EPS0["X"][tgt]); M.PEX["X"][s]=PEX0["X"][tgt]; M.FXU[s]=list(FXU0[tgt]); M.FXO[s]=list(FXO0[tgt])
o,E,R=M.run()
print(f"AI-only Bear (X and NOK on Base): IRR {o['Bear']['irr']*100:.1f}  2027 {o['Bear']['r'][0]*100:.1f} | AI-only Bull: IRR {o['Bull']['irr']*100:.1f} 2027 {o['Bull']['r'][0]*100:.1f}")
# 3) old (11 Oct) H1 path for comparison & T at P-block path
reset(); M.EPS["H1"]["Base"]=[.92,.95,.95,.95]; o,E,R=M.run(); print("H1 Base on the 11 Oct path:",round(o['Base']['irr']*100,2))
reset(); M.EPS["T"]=copy.deepcopy(EPS0["E"]); M.PEX["T"]=dict(PEX0["E"]); o,E,R=M.run(); print("T on platform path and exit 21:",round(o['Base']['irr']*100,2))
reset(); M.PEX["T"]["Base"]=BL0["T"]["pe27"]; o,E,R=M.run(); print("T exit at today's P/E:",round(o['Base']['irr']*100,2))
# 4) memory weight at 31 Aug Nordnet (no pref): handled by reading blocks.json of 11 Oct? report memory share effect
