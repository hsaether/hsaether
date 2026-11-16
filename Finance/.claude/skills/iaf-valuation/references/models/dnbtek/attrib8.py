# DNB Teknologi A, model v8 (16 Nov 2026): attribution from the 6 Nov version (v7), method and memory sensitivities.
# Usage (from the v8 folder): py ../attrib8.py ../v7 ../v8w ../v8wfy ../v8
#   v7    = 6 Nov data (hold.json 6 Nov, closes 4 Nov, 30 Sep weights; NAV 7,381.56, stub 56)
#   v8w   = v7 hold.json and closes + blocks.py NAV=7381.56 STUB=56 OLDFY (30 Oct weights and currency mix, old FY mapping)
#   v8wfy = the same with the v8 FY mapping (Visa and Skyworks on FY Sep-2027 = CY27)
#   v8    = this version (closes 12 Nov, consensus 16 Nov, blocks.py NAV=7603.41 STUB=48)
import sys,os,copy; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M
V7,V8W,V8WFY,V8=sys.argv[1:5]
def show(lab,**kw):
    o,E,R=M.run(**kw); kc=dict(kw,cap=True); print(M.line(o,E,R,lab)+f" | Bear27 capped {M.run(**kc)[0]['Bear']['r'][0]*100:6.1f}"); return o,E,R
print("Step 0: the 6 Nov version (v7 data, v7 company values, v7 AI rows)")
M.load(V7); M.use_ai(True); M.use_company(v7=True); show("0 v7 (NAV 7,381.56, 4 Nov)")
print("Step 1: company blocks (at the 4 Nov prices and 30 Sep weights)")
for only,lab in (({"CN"},"NVIDIA v1.6 only"),({"CT"},"TSMC v1.2 only"),({"CA"},"Amazon 11 Nov re-glide only"),
                 ({"CS","CP"},"Samsung v3 only"),({"CM"},"Microsoft 7 Nov re-glide only"),({"CG"},"Alphabet 7 Nov block only")):
    M.use_company(v7=True,only=only); show(f"   {lab}")
M.use_company(v7=False); show("1 + all company blocks")
print("Step 2: AI BBB 11 Nov (H1 Base .92/.91/.88/.87; E cash conversion Base -.20/.11/.36); Equity and HY unchanged")
M.use_ai(False); EPS1=copy.deepcopy(M.EPS); CONV1=copy.deepcopy(M.CONV)
M.EPS["H1"]["Base"]=[.92,.91,.88,.87]; M.CONV["E"]["Base"]=[-.20,.00,.20]; show("   H1 only")
M.EPS=copy.deepcopy(EPS1); M.CONV=copy.deepcopy(CONV1); M.setup(); show("2 + AI BBB 11 Nov (H1 and E conversion)")
print("Step 3: holdings of 30 Oct (DNB AM factsheet: top 10, Korea, country-derived lines, currency mix) at the 4 Nov prices")
M.load(V8W); show("3a + holdings of 30 Oct (old FY mapping)")
M.load(V8WFY); show("3b + FY mapping fix (Visa, Skyworks on FY Sep-2027)")
print("Step 4: price")
M.load(V8); show("4 + NAV 12 Nov 7,603.41, closes 12 Nov, consensus 16 Nov, stub 48 days = v8")
show("   memory-stressed Bear (v8)",cap=True)
print("Method sensitivities (v8)")
EPS0=copy.deepcopy(M.EPS); CONV0=copy.deepcopy(M.CONV)
M.CONV["E"]={s:[-.38,-.20,.02] for s in M.SC}; show("   Meta cash conversion like Alphabet v2 (-.38/-.20/.02)"); M.CONV=copy.deepcopy(CONV0)
M.CONV["X"]={s:[.45]*3 for s in M.SC}; show("   X without retained cash (c = payout 0.45)"); M.CONV=copy.deepcopy(CONV0)
M.CONV["X"]={s:[.90]*3 for s in M.SC}; show("   X c = 0.90"); M.CONV=copy.deepcopy(CONV0)
M.EPS["E"]["Bear"]=[.82,.75,.82,.91]; show("   Meta on the E-layer Bear row (.82/.75/.82/.91)"); M.EPS=copy.deepcopy(EPS0); M.setup()
M.EPS["E"]["Bear"]=[.76,.70,.78,.86]; show("   Meta on the analysed-platform Bear blend (.76/.70/.78/.86)"); M.EPS=copy.deepcopy(EPS0); M.setup()
print("Memory sensitivities (v8)")
for pe in (6,4): show(f"   memory Bear exit P/E {pe} (analyses 8)",mem_pex={"Bear":pe-8})
show("   memory Base exit P/E 8 (analyses 10)",mem_pex={"Base":-2})
for m in (0.8,0.6,0.5,0.45): show(f"   memory 2030 EPS x{m} in Base",mem_e30=m)
