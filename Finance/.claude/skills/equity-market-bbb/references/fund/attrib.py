import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M, copy
BL0=copy.deepcopy(M.BL)
def merge():
    M.BL.clear(); M.BL.update(copy.deepcopy(BL0))
    for c,l in (("CN","H1"),("CT","H3")):
        a=M.BL.pop(c)
        if l in M.BL:
            b=M.BL[l]; w=a['w']+b['w']; M.BL[l]=dict(w=w,pe27=w/(a['w']/a['pe27']+b['w']/b['pe27']),share=0)
        else: M.BL[l]=a
def show(lab):
    o,E,R=M.run(); print(f"{lab:60s} Bear {o['Bear']['irr']*100:6.2f} Base {o['Base']['irr']*100:6.2f} Bull {o['Bull']['irr']*100:6.2f} | Bear27 {o['Bear']['r'][0]*100:6.1f} | E/R {E/R:.3f}")
P2={"H1":copy.deepcopy(M.EPS["H1"]),"H3":copy.deepcopy(M.EPS["H3"])}
M.RET=False; merge()
M.EPS["H1"]["Bear"]=[.70,.60,.70,.75]; M.EPS["H3"]["Bear"]=[.80,.75,.85,.92]
show("1 15 Oct method, 15 Oct NAV/prices, NVDA+TSM on layer (v1 Bears)")
M.EPS["H1"]=copy.deepcopy(P2["H1"]); M.EPS["H3"]=copy.deepcopy(P2["H3"])
show("2 + AI BBB v2 Bear paths (H1, H3)")
M.BL.clear(); M.BL.update(copy.deepcopy(BL0))
show("3 + NVIDIA and TSMC as company blocks")
M.RET=True
show("4 + retained cash in layer blocks and X (= model)")
M.CONV["X"]={s:[.45]*3 for s in M.SC}
show("   sensitivity: X without retained cash (c = payout 0.45)")
M.CONV["X"]={s:[.90]*3 for s in M.SC}
show("   sensitivity: X c = 0.90")
M.CONV["X"]={s:[.75]*3 for s in M.SC}
# NVDA / TSM unadjusted analyses (13.0% NVDA FY basis + old Bear; TSM old Bear)
c0=copy.deepcopy(M.COMP)
M.COMP["CN"]["Bear"]=dict(V=[132.2,156.7,171.1],D=[5.47,5.73,6.03],EPS=[11.14,9.55,11.14,11.93]); M.COMP["CN"]["Base"]=dict(V=[248.1,273.5,286.3],D=[6.80,8.86,9.22],EPS=[14.64,15.59,15.91,15.43]); M.COMP["CN"]["Bull"]=dict(V=[302.0,366.0,420.7],D=[7.23,10.05,11.21],EPS=[15.92,18.31,19.90,20.68])
M.COMP["CT"]["Bear"]=dict(V=[254.6,291.2,320.4],D=[4.63,5.24,5.86],EPS=[18.48,17.33,19.64,21.26])
show("   sensitivity: NVDA and TSM on their unadjusted v1 analyses")
M.COMP.clear(); M.COMP.update(c0)
merge(); show("   sensitivity: NVDA and TSM on the layer method (v2) instead")
# memory-stressed Bear (layer method lets memory rise in a Bear when today's P/E < the Bear exit P/E)
M.BL.clear(); M.BL.update(copy.deepcopy(BL0)); P=copy.deepcopy(M.PEX)
for pe in (6,4,2.6):
    M.PEX["H2"]["Bear"]=pe; show(f"   memory Bear exit P/E {pe} (AI BBB 8)")
M.PEX=copy.deepcopy(P)
