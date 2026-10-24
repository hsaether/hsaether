# Attribution from the 17 Oct version (v4) to v5 (22 Oct), method sensitivities and the memory-stressed Bear
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M, copy
BL0=copy.deepcopy(M.BL); CONV0=copy.deepcopy(M.CONV); PEX0=copy.deepcopy(M.PEX)
def merge(pairs):
    M.BL.clear(); M.BL.update(copy.deepcopy(BL0))
    for c,l in pairs:
        a=M.BL.pop(c)
        if l not in M.BL: M.BL[l]=a; continue
        b=M.BL[l]; w=a['w']+b['w']; M.BL[l]=dict(w=w,pe27=w/(a['w']/a['pe27']+b['w']/b['pe27']),share=0)
def reset():
    M.BL.clear(); M.BL.update(copy.deepcopy(BL0)); M.CONV=copy.deepcopy(CONV0); M.PEX=copy.deepcopy(PEX0)
def show(lab):
    o,E,R=M.run(); print(f"{lab:66s} Bear {o['Bear']['irr']*100:6.2f} Base {o['Base']['irr']*100:6.2f} Bull {o['Bull']['irr']*100:6.2f} | Bear27 {o['Bear']['r'][0]*100:6.1f} | MoS {o['Base']['Pk']/100-1:+.1%} | E/R {E/R:.3f}")
print("17 Oct version (v4): Bear -5.5 Base 7.1 Bull 14.5 | Bear27 -29.0 | MoS -12.9% | E/R 0.075")
merge([("CA","E")]); M.CONV["E"]={"Bear":[.00,.40,.60],"Base":[-.10,.10,.30],"Bull":[-.20,-.10,.10]}
show("1 NAV/prices 21 Oct, weights 16 Sep, cons. 22 Oct; Amazon on E, old E c")
M.CONV=copy.deepcopy(CONV0)
show("2 + E cash conversion of AI BBB Update 3 (-.20/.00/.20)")
reset(); show("3 + Amazon as a company block (= model v5)")
print("Sensitivities")
M.CONV["E"]={"Base":[-.30,-.14,.06],"Bear":[-.30,-.14,.06],"Bull":[-.30,-.14,.06]}; show("   Meta cash conversion like Alphabet (-.30/-.14/.06)")
reset(); M.CONV["X"]={s:[.45]*3 for s in M.SC}; show("   X without retained cash (c = payout 0.45)")
reset(); M.CONV["X"]={s:[.90]*3 for s in M.SC}; show("   X c = 0.90")
reset(); merge([("CN","H1"),("CT","H3")]); show("   NVDA and TSM on the layer method (v2.1) instead")
reset(); merge([("CA","E")]); show("   Amazon on the E layer (E rest path) instead")
for pe in (6,4,round(BL0["H2"]["pe27"],2)):
    reset(); M.PEX["H2"]["Bear"]=pe; show(f"   memory Bear exit P/E {pe} (AI BBB 8)")
reset(); M.CONV["H2"]={s:[v-.2 for v in CONV0["H2"][s]] for s in M.SC}; show("   memory cash conversion -0.2")
reset(); M.PEX["H2"]["Base"]=8; show("   memory Base exit P/E 8 (AI BBB 10)")
