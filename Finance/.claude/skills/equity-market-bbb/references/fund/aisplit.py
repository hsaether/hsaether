# DNB Teknologi A, model v6: per-block IRRs (each block alone, before cost), AI part vs X, memory together, AI-only scenarios
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M, copy
EPS0=copy.deepcopy(M.EPS); PEX0=copy.deepcopy(M.PEX); BL0=copy.deepcopy(M.BL); FXU0=copy.deepcopy(M.FXU); FXO0=copy.deepcopy(M.FXO)
def reset():
    M.EPS=copy.deepcopy(EPS0); M.PEX=copy.deepcopy(PEX0); M.BL.clear(); M.BL.update(copy.deepcopy(BL0)); M.FXU.update(copy.deepcopy(FXU0)); M.FXO.update(copy.deepcopy(FXO0))
AI=[b for b in BL0 if b!="X"]
print("Block alone, before cost (Bear/Base/Bull IRR NOK; 2027 Bear; capped memory Bear):")
for b in BL0:
    reset(); w=BL0[b]; M.BL.clear(); M.BL[b]=dict(BL0[b],w=1.0)
    o,E,R=M.run(fee=0.0); oc,_,_=M.run(fee=0.0,cap=True)
    print(f"  {b:3s} w {BL0[b]['w']*100:4.1f}% PE {w['pe27']:5.2f} | {o['Bear']['irr']*100:6.1f} {o['Base']['irr']*100:6.1f} {o['Bull']['irr']*100:6.1f} | Bear27 {o['Bear']['r'][0]*100:6.1f}"
          +(f" | capped {oc['Bear']['irr']*100:6.1f} / 2027 {oc['Bear']['r'][0]*100:6.1f}" if b in M.MEM else "")+f" | E/R {E/R:.3f}")
for lab,keep in [("AI blocks",AI),("Non-AI (X)",["X"]),("Memory (CS+CP+CH)",[b for b in BL0 if b in M.MEM]),
                 ("Platforms (CM+CG+CA+E)",["CM","CG","CA","E"])]:
    reset(); sub={b:BL0[b] for b in keep}; tw=sum(x['w'] for x in sub.values()); M.BL.clear()
    for b,x in sub.items(): M.BL[b]=dict(x,w=x['w']/tw)
    pe=1/sum(x['w']/tw/x['pe27'] for x in sub.values())
    o,E,R=M.run(fee=0.0); oc,Ec,Rc=M.run(fee=0.0,cap=True)
    print(f"{lab:24s} weight {tw*100:.1f}% of the model, P/E {pe:.1f} | before cost Bear {o['Bear']['irr']*100:.1f} Base {o['Base']['irr']*100:.1f} Bull {o['Bull']['irr']*100:.1f} | Bear27 {o['Bear']['r'][0]*100:.1f} (capped {oc['Bear']['r'][0]*100:.1f}) | E/R {E/R:.3f}")
# AI-only Bear: AI blocks on Bear, X on Base, NOK on Base (financing break without recession)
reset()
for s,tgt in [("Bear","Base"),("Bull","Base")]:
    M.EPS["X"][s]=list(EPS0["X"][tgt]); M.PEX["X"][s]=PEX0["X"][tgt]; M.FXU[s]=list(FXU0[tgt]); M.FXO[s]=list(FXO0[tgt])
o,E,R=M.run()
print(f"AI-only Bear (X and NOK on Base): IRR {o['Bear']['irr']*100:.1f}  2027 {o['Bear']['r'][0]*100:.1f} | AI-only Bull: IRR {o['Bull']['irr']*100:.1f} 2027 {o['Bull']['r'][0]*100:.1f}")
reset()
