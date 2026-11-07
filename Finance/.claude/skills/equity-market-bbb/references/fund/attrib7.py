# DNB Teknologi A, model v7 (6 Nov 2026): attribution from the 30/31 Oct version (v6), method and memory sensitivities.
# Usage: py attrib7.py <v6 folder> <v6w folder> <v7 folder>
#   v6  = 31 Oct data (hold.json 30 Oct, closes 29 Oct, blocks.json of v6: 24 Sep / 31 Aug weights)
#   v6w = v6 data + ASML (close 29 Oct), blocks.py NAV=7375.01 STUB=62 (30 Sep weights and currency mix)
#   v7  = this version (closes 4 Nov, consensus 6 Nov, blocks.py NAV=7381.56 STUB=56)
import sys,os,copy; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M
V6,V6W,V7=sys.argv[1:4]
def show(lab,**kw):
    o,E,R=M.run(**kw); kc=dict(kw,cap=True); print(M.line(o,E,R,lab)+f" | Bear27 capped {M.run(**kc)[0]['Bear']['r'][0]*100:6.1f}"); return o,E,R
print("Step 0: the 31 Oct version (v6 data, v6 company values)")
M.load(V6); M.use_company(v6=True); show("0 v6 (NAV 7,375.01, 29 Oct)")
print("Step 1: company blocks (at the 29 Oct prices and 24 Sep weights)")
for c,lab in (("CN","NVIDIA v1.2 only"),("CT","TSMC v1.1 only"),("CG","Alphabet re-mark pair only")):
    M.use_company(v6=True,only={c}); show(f"   {lab}")
M.use_company(v6=False); show("1 + NVIDIA v1.2, TSMC v1.1, Alphabet re-mark pair")
print("Step 2: inputs (AI rows, Equity NOK path, HY NIBOR): none of the values read here moved")
show("2 + AI BBB 5 Nov (paths kept), Equity Update 2 (NOK moves kept), HY 5 Nov (NIBOR kept)")
print("Step 3: holdings of 30 Sep (DNB AM top 10, Nordnet rest, ASML in, Nintendo out, currency mix)")
M.load(V6W); show("3 + holdings of 30 Sep at the 29 Oct prices")
print("Step 4: price")
M.load(V7); show("4 + NAV 4 Nov 7,381.56, closes 4 Nov, consensus 6 Nov, stub 56 days = v7")
show("   memory-stressed Bear (v7)",cap=True)
print("Method sensitivities (v7)")
EPS0=copy.deepcopy(M.EPS); CONV0=copy.deepcopy(M.CONV)
M.CONV["E"]={s:[-.38,-.20,.02] for s in M.SC}; show("   Meta cash conversion like Alphabet v2 (-.38/-.20/.02)"); M.CONV=copy.deepcopy(CONV0)
M.CONV["X"]={s:[.45]*3 for s in M.SC}; show("   X without retained cash (c = payout 0.45)"); M.CONV=copy.deepcopy(CONV0)
M.CONV["X"]={s:[.90]*3 for s in M.SC}; show("   X c = 0.90"); M.CONV=copy.deepcopy(CONV0)
M.EPS["E"]["Bear"]=[.76,.70,.78,.86]; show("   Meta on the analysed-platform Bear blend (.76/.70/.78/.86)"); M.EPS=copy.deepcopy(EPS0); M.setup()
print("Memory sensitivities (v7)")
for pe in (6,4): show(f"   memory Bear exit P/E {pe} (analyses 8)",mem_pex={"Bear":pe-8})
show("   memory Base exit P/E 8 (analyses 10)",mem_pex={"Base":-2})
for m in (0.8,0.6,0.5): show(f"   memory 2030 EPS x{m} in Base",mem_e30=m)
