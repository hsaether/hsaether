import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import idxfunds as M
W=M.W; C=M.cc_params()
for name,p,cost,nav in [("DNB GI on Nordnet",W,0.0025,874.58),("DNB GI in DNB pension",W,0.0021,874.58),("Nordnet GI",C,0.0019,232.43)]:
    o,E,R=M.run(**p,cost=cost); print("\n==",name,f"E {E:.2f} R {R:.1f} E/R {E/R:.3f}")
    for s in M.SC:
        x=o[s]; lv=[nav*v/100 for v in x['lv']]
        cum=[(x['lv'][i]/100)**(1/(M.STUB+i))-1 for i in range(1,4)]
        print(f" {s}: EPS {[round(v,3) for v in p['eps'][s]]} PE {[round(v,1) for v in p['pe'][s]]} | r stub {x['stub']*100:.1f} {[round(v*100,1) for v in x['r']]} | NAV {[round(v,1) for v in lv]} | IRR to YE {[round(v*100,1) for v in cum]} | XIRR {x['irr']*100:.2f}")
        print(f"     508k -> end-29 {508*x['lv'][3]/100:.1f}k ; 2027 change on 508k {508*x['lv'][1]/100-508*x['lv'][0]/100:+.1f}k ; Pk NAV {nav*x['Pk']/100:.1f} MoS {x['Pk']/100-1:+.1%} ; kept {(x['sumD']+x['VT'])/100-1:+.1%}")
    # return split Base
    import math
    for s in M.SC:
        x=o[s]; en=p['eps'][s][3]; T=M.T
        epsg=en**(1/T)-1; rer=(p['pe'][s][2]/p['pe27'])**(1/T)-1; fx=[1.09,1,0.97][M.SC.index(s)]**(1/T)-1
        print(f" split {s}: IRR {x['irr']*100:.2f} d {x['d']*100:.2f} g {x['g']*100:.2f} (EPS {epsg*100:.2f}, rerate {rer*100:.2f} [{p['pe27']:.2f}->{p['pe'][s][2]:.2f}], FX {fx*100:.2f}, cost {-cost*100:.2f}) c {x['c']*100:.2f} | sumD {x['sumD']:.1f} VT {x['VT']:.1f}")
# share of Bull priced
for name,p,cost in [("DNB",W,0.0025),("NGI",C,0.0019)]:
    o,E,R=M.run(**p,cost=cost); b=o['Base']['Pk']; u=o['Bull']['Pk']; print(name,"share of Bull priced",round((100-b)/(u-b)*100),"%")
