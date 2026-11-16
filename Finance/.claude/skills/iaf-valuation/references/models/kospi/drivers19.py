# IQQK / Korea (docs/kospi-analysis.md), version 1.9 (16 Nov 2026): driver breakdown (Base -> Bear / capped Bear / Bull, one
# block group at a time, spot FX) and the Base return bridge by block. Imports korea.py (default date and blocks).
# Usage: py drivers19.py
import sys; sys.argv=["korea.py"]
import korea as K
w=K.ETF["IQQK"]; fee=K.FEE["IQQK"]; rule=K.RULE["IQQK"]
for s in ("Bear","Bull","Cap"): K.FX[s]=[1.0,1.0,1.0]          # spot FX held flat (the decision)
B={s:K.blocks(s) for s in K.SC}
orig=K.blocks
def mixed(m):
    """m: block -> scenario; FX and the scenario label of run_etf are spot/Base"""
    K.blocks=lambda s,**kw:{b:B[m.get(b,"Base")][b] for b in ("S","SP","H","Q","K")}
    x=K.run_etf(w,fee,rule,"Base"); K.blocks=orig; return x
SH=("S","SP","H","Q")
steps=[("Base",{}),
       ("Samsung + SK hynix + SK Square to the decision Bear (rest at Base)",{b:"Bear" for b in SH}),
       ("+ rest of Korea to Bear (= decision Bear)",{**{b:"Bear" for b in SH},"K":"Bear"}),
       ("Samsung + SK hynix + SK Square capped, rest at Base",{b:"Cap" for b in SH}),
       ("+ rest of Korea to Bear (= capped Bear)",{**{b:"Cap" for b in SH},"K":"Bear"}),
       ("Samsung + SK hynix + SK Square to Bull (rest at Base)",{b:"Bull" for b in SH}),
       ("+ rest of Korea to Bull (= Bull)",{**{b:"Bull" for b in SH},"K":"Bull"})]
print("driver breakdown, spot FX: IRR / 2027 / P_k (index) / capital")
for lab,m in steps:
    x=mixed(m); print(f"  {lab:68s} {x['irr']*100:5.1f}% / {x['rn'][0]*100:6.1f}% / {x['Pk']:6.1f} / {x['kept']:+.1%}")
# Base return bridge by block (per 100 of IQQK at the start; block paths without re-capping, fee or withholding; the remainder
# is re-capping, the 0.74% cost and Korean withholding)
x=K.run_etf(w,fee,rule,"Base"); tot=x["sumD"]+x["VT"]-100
print(f"\nBase return bridge (spot = NOK in Base): sumD + V_T - 100 = {tot:.1f}")
acc=0.0
for b,lab in (("S","Samsung common"),("SP","Samsung preference"),("H","SK hynix"),("Q","SK Square"),("K","rest of Korea")):
    D,V,st=B["Base"][b]; c=w[b]*100*(sum(D)+st+V[2]-1); acc+=c
    print(f"  {lab:20s} weight {w[b]*100:5.1f}  (sumD {sum(D)+st:.3f}, V_T {V[2]:.3f} per unit) -> {c:+6.1f}")
print(f"  re-capping, cost and withholding {tot-acc:+6.1f}")
