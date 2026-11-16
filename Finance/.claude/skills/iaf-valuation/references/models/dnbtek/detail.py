# DNB Teknologi A (docs/dnb-teknologi-analysis.md), model v8 (16 Nov 2026): per-year path, NAV equivalents, exit multiple, exit cross-check, structural run.
# Run in the working folder of the version (blocks.json, closes.json).
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M, copy
NAV=M.NAV
o,E,R=M.run(); BL=M.BL
E27=sum(x['w']*100/x['pe27'] for x in BL.values())
for s in M.SC:
    x=o[s]; lv=[NAV*(1+x['stub'])]
    for r in x['r']: lv.append(lv[-1]*(1+r))
    cum=[(lv[i]/NAV)**(1/(M.STUB+i))-1 for i in range(1,4)]
    fpe=[x['Vr'][i]/x['E'][i+1] for i in range(3)]
    print(f"{s}: r stub {x['stub']*100:.1f} {[round(v*100,1) for v in x['r']]} | NAV eq {[round(v) for v in lv]} | IRR to ye {[round(c*100,1) for c in cum]} | value/next EPS {[round(p,1) for p in fpe]} | EPS {[round(e/E27,3) for e in x['E']]}")
    print(f"   IRR {x['irr']*100:.2f} d {x['d']*100:.2f} g {x['g']*100:.2f} c {x['c']*100:.2f} sumD {x['sumD']:.1f} VT {x['VT']:.1f} Pk {x['Pk']:.1f} -> NAV {NAV*x['Pk']/100:,.0f} MoS {x['Pk']/100-1:+.1%} kept {(x['sumD']+x['VT'])/100-1:+.1%}")
    print(f"   exit value multiple {x['Vr'][2]/x['E'][3]:.1f}; ex memory {(x['Vr'][2]-x['VM'][2])/(x['E'][3]-x['EM'][3]):.1f}; norm EPS {x['E'][3]/E27:.3f}; memory share of 2027 / 2030 earnings {x['EM'][0]/x['E'][0]:.1%} / {x['EM'][3]/x['E'][3]:.1%}")
mw=sum(BL[b]['w'] for b in BL if b in M.MEM); me=sum(BL[b]['w']*100/BL[b]['pe27'] for b in BL if b in M.MEM)
print("E",round(E,2),"R",round(R,1),"E/R",round(E/R,3),"| P/E now",round(100/E27,2),"ex memory",round((100-mw*100)/(E27-me),2),"| memory weight",round(mw*100,1),"% earnings share",round(me/E27*100,1),"%")
# exit cross-check (IAF Step 3, Track A): buyer's return = cash yield (earnings-weighted c 2029 / exit multiple) + growth
# c 2029: layers from the AI BBB; company blocks from their analyses (FCF after growth capex and dilution offsets / EPS) [A]
C29={"CM":0.42,"CG":0.02,"CA":0.08,"CN":13.21/13.38,"CT":19.23/25.78,"CS":31823/33469,"CP":31823/33469,"CH":127553/187104}   # v8: NVIDIA v1.6, TSMC v1.2, Samsung v3 (FCF after growth / EPS 2029)
x=o['Base']; w29={};
for b,bl in BL.items():
    w29[b]=bl['w']*100/bl['pe27']*M.EPS[b]['Base'][2]
c29=sum(w29[b]*(C29[b] if b in C29 else M.CONV[b]['Base'][2]) for b in BL)/sum(w29.values())
xm=x['Vr'][2]/x['E'][3]; xmx=(x['Vr'][2]-x['VM'][2])/(x['E'][3]-x['EM'][3])
c29x=sum(w29[b]*(C29[b] if b in C29 else M.CONV[b]['Base'][2]) for b in BL if b not in M.MEM)/sum(w29[b] for b in BL if b not in M.MEM)
print(f"exit cross-check: c2029 {c29:.2f} (ex memory {c29x:.2f}); exit multiple {xm:.1f} (ex memory {xmx:.1f}); cash yield {c29/xm*100:.1f}% (ex memory {c29x/xmx*100:.1f}%); + World growth 5.3% = {c29/xm*100+5.3:.1f}% (ex memory {c29x/xmx*100+5.3:.1f}%)")
# structural: layer blocks at their normalised (2030) EPS from 2027; company blocks as in their analyses
base=copy.deepcopy(M.EPS)
for b in M.EPS:
    if b in M.COMP: continue
    for s in M.SC: M.EPS[b][s]=[base[b][s][3]]*4
o2,_,_=M.run(); M.EPS=base
print("structural (company blocks as in their analyses)", {s:round(o2[s]['irr']*100,1) for s in M.SC})

# g split (compounding parts; 1 + g = product): normalised EPS growth (CY27 consensus -> 2030), value multiple (P/E now -> exit
# value multiple incl. retained cash and company net cash), FX on the NOK path, fund cost
import math
PE0=100/E27
for s in M.SC:
    x=o[s]; fxT=1-M.USD-M.OTH+M.USD*M.FXU[s][2]+M.OTH*M.FXO[s][2]
    ge=(x['E'][3]/E27)**(1/M.T)-1; gm=((x['Vr'][2]/x['E'][3])/PE0)**(1/M.T)-1; gf=fxT**(1/M.T)-1
    print(f"g split {s}: EPS {ge*100:+.1f}  multiple {gm*100:+.1f}  FX {gf*100:+.1f}  cost -1.1  -> product {((1+ge)*(1+gm)*(1+gf)*(1-0.0114)-1)*100:+.1f} vs g {x['g']*100:+.1f}")

# Base return bridge per 100 of NAV (NOK): earnings at today's P/E, value multiple to exit (incl. retained cash, net cash, stakes),
# fund cost, distributions; memory and the rest shown apart. Before cost on the blocks; cost = V_T after cost - V_T before cost.
x=o['Base']; T=M.T
fx2=1.0
mE27={g:sum(BL[b]['w']*100/BL[b]['pe27'] for b in BL if (b in M.MEM)==g) for g in (True,False)}
mW={g:sum(BL[b]['w']*100 for b in BL if (b in M.MEM)==g) for g in (True,False)}
mE30={True:x['EM'][3],False:x['E'][3]-x['EM'][3]}; mV={True:x['VM'][2],False:x['Vr'][2]-x['VM'][2]}
for g,lab in ((True,"memory"),(False,"rest")):
    pe0=mW[g]/mE27[g]; earn=pe0*(mE30[g]-mE27[g]); mult=mV[g]-pe0*mE30[g]
    print(f"bridge {lab}: weight {mW[g]:.1f} earnings {earn:+.1f} multiple {mult:+.1f} -> value at exit before cost {mV[g]:.1f}")
print(f"bridge: cost on V_T {x['VT']-x['Vr'][2]:+.1f}; distributions {x['sumD']:.1f}; V_T {x['VT']:.1f}; total {x['VT']+x['sumD']:.1f}; retained in layer and X blocks {x['Rc'][2]:.1f}")
