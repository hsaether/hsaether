# DNB Teknologi A, model v6 (30 Oct 2026): attribution from the 22 Oct version (v5), method sensitivities, memory stress.
# Usage: py attrib.py <v5 folder> <v5co folder> <v5w folder> <v6 folder>
#   v5   = 22 Oct data (hold.json, closes.json of 21 Oct, blocks.json of v5: 16 Sep weights, memory as the H2 layer)
#   v5co = 22 Oct data, blocks.py W0916 NAV=7615.95 STUB=70 (memory as company blocks CS / CP / CH)
#   v5w  = 22 Oct data, blocks.py NAV=7615.95 STUB=70 (24 Sep weights and currency mix)
#   v6   = this version (closes of 29 Oct, consensus 30 Oct, blocks.py NAV=7375.01 STUB=62)
import sys,os,copy; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M
V5,V5CO,V5W,V6=sys.argv[1:5]
def show(lab,**kw):
    o,E,R=M.run(**kw); print(M.line(o,E,R,lab)); return o,E,R
EPS0=copy.deepcopy(M.EPS)
print("Step 0-1: company blocks (21 Oct prices, 16 Sep weights)")
M.load(V5); M.use_company(old=True); show("0 22 Oct version (v5)")
for c,lab in (("CM","Microsoft v3"),("CG","Alphabet v2"),("CA","Amazon v2")):
    M.use_company(old=True); M.COMP[c].update(copy.deepcopy(M.NEWCOMP[c])); M.setup(); show(f"   only {lab}")
M.use_company(old=False); show("1a + Microsoft v3, Alphabet v2, Amazon v2 (memory still on the H2 layer)")
M.load(V5CO); show("1b + memory as company blocks (Samsung v2 common / preference, SK hynix v2)")
show("   memory-stressed Bear here",cap=True)
print("Step 2: AI rows (Update 5)")
show("2 + AI BBB Update 5 rows read here: none moved (E-rest row, H1, T, exit P/Es unchanged)")
M.EPS["E"]["Base"][0]=0.92; show("   check: Meta on the E path's new 2027 point .92 (not applied)"); M.EPS=copy.deepcopy(EPS0); M.setup()
print("Step 3: price")
M.load(V5W); show("3a + holdings of 24 Sep (DNB AM top 10, Korea 5.12%, currency mix)")
M.load(V6); show("3b + NAV 29 Oct 7,375.01, closes 29 Oct, consensus 30 Oct, stub 62 days = v6")
show("   memory-stressed Bear (v6)",cap=True)
print("Method sensitivities (v6)")
EPS0=copy.deepcopy(M.EPS); CONV0=copy.deepcopy(M.CONV)
M.CONV["E"]={s:[-.38,-.20,.02] for s in M.SC}; show("   Meta cash conversion like Alphabet v2 (-.38/-.20/.02)"); M.CONV=copy.deepcopy(CONV0)
M.CONV["X"]={s:[.45]*3 for s in M.SC}; show("   X without retained cash (c = payout 0.45)"); M.CONV=copy.deepcopy(CONV0)
M.CONV["X"]={s:[.90]*3 for s in M.SC}; show("   X c = 0.90"); M.CONV=copy.deepcopy(CONV0)
M.EPS["E"]["Bear"]=[.76,.70,.78,.86]; show("   Meta on the analysed-platform Bear blend (.76/.70/.78/.86; AI BBB note)"); M.EPS=copy.deepcopy(EPS0); M.setup()
print("Memory sensitivities (v6)")
for pe in (6,4): show(f"   memory Bear exit P/E {pe} (analyses 8)",mem_pex={"Bear":pe-8})
show("   memory Base exit P/E 8 (analyses 10)",mem_pex={"Base":-2})
for m in (0.6,0.5): show(f"   memory 2030 EPS x{m} in Base (the analyses' own test)",mem_e30=m)
