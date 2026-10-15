import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fundmodel as M, copy
NAV=7637.81
o,E,R=M.run(); BL=M.BL
E27=sum(x['w']*100/x['pe27'] for x in BL.values())
for s in M.SC:
    x=o[s]; lv=[NAV*(1+x['stub'])]
    for r in x['r']: lv.append(lv[-1]*(1+r))
    cum=[(lv[i]/NAV)**(1/(M.STUB+i))-1 for i in range(1,4)]
    fpe=[x['Vr'][i]/x['E'][i+1] for i in range(3)]
    print(f"{s}: r stub {x['stub']*100:.1f} {[round(v*100,1) for v in x['r']]} | NAV eq {[round(v) for v in lv]} | IRR to ye {[round(c*100,1) for c in cum]} | fwdPE {[round(p,1) for p in fpe]} | EPS {[round(e/E27,3) for e in x['E']]}")
    print(f"   IRR {x['irr']*100:.2f} d {x['d']*100:.1f} g {x['g']*100:.1f} c {x['c']*100:.1f} sumD {x['sumD']:.1f} VT {x['VT']:.1f} Pk {x['Pk']:.1f} -> NAV {NAV*x['Pk']/100:.0f} MoS {x['Pk']/100-1:+.1%} kept {(x['sumD']+x['VT'])/100-1:+.1%}")
    # ex memory exit P/E: Vr[2] and E[3] without H2
    w=BL['H2']; eH2=w['w']*100/w['pe27']; vH2=M.PEX['H2'][s]*eH2*M.EPS['H2'][s][3]
    print(f"   exit P/E blend {x['Vr'][2]/x['E'][3]:.1f}; ex memory {(x['Vr'][2]-vH2)/(x['E'][3]-eH2*M.EPS['H2'][s][3]):.1f}; norm EPS {x['E'][3]/E27:.3f}")
print("E",round(E,2),"R",round(R,1),"E/R",round(E/R,3), "ex-mem PE now", round((100-BL['H2']['w']*100)/(E27-BL['H2']['w']*100/BL['H2']['pe27']),1))
# structural
base=copy.deepcopy(M.EPS); compb=copy.deepcopy(M.COMP)
for b in M.EPS:
    if b in M.COMP: continue
    for s in M.SC: M.EPS[b][s]=[base[b][s][3]]*4
o2,_,_=M.run(); M.EPS=base
print("structural (company blocks as in their analyses)", {s:round(o2[s]['irr']*100,1) for s in M.SC})
# attribution: company blocks replaced by the E layer path at the same prices
M.BL['E2']=dict(w=M.BL['CM']['w']+M.BL['CG']['w'],pe27=(M.BL['CM']['w']+M.BL['CG']['w'])/(M.BL['CM']['w']/M.BL['CM']['pe27']+M.BL['CG']['w']/M.BL['CG']['pe27']),share=0)
cm,cg=M.BL.pop('CM'),M.BL.pop('CG')
M.EPS['E2']=M.EPS['E']; M.PEX['E2']=M.PEX['E']; M.PAY['E2']=M.PAY['E']
o3,E3,R3=M.run(); print("MSFT+GOOGL on the E layer path instead:", {s:round(o3[s]['irr']*100,2) for s in M.SC}, "E/R", round(E3/R3,3))
