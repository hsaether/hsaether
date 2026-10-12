import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import idxfunds as M, copy
W=M.W; C=M.cc_params()
def line(lab,o,E,R):
    print(f"{lab:58s} Bear {o['Bear']['irr']*100:5.2f} Base {o['Base']['irr']*100:5.2f} Bull {o['Bull']['irr']*100:5.2f} | 27: {o['Bear']['r'][0]*100:6.1f} / {o['Base']['r'][0]*100:5.1f} | E/R {E/R:.3f} | MoS {o['Base']['Pk']/100-1:+.1%}")
print("=== DNB Global Indeks A (World) ===")
for lab,kw in [("on Nordnet 0.25%",dict(cost=0.0025)),("DNB pension 0.21%",dict(cost=0.0021)),("exit P/E -1",dict(cost=0.0025,pe={s:[x-1 for x in v] for s,v in M.W_PE.items()})),
               ("exit P/E +1",dict(cost=0.0025,pe={s:[x+1 for x in v] for s,v in M.W_PE.items()})),("CY27 consensus -5%",dict(cost=0.0025,eps_mult=0.95))]:
    p=dict(W); p.update({k:v for k,v in kw.items() if k in ("pe",)}); o,E,R=M.run(**p,**{k:v for k,v in kw.items() if k not in ("pe",)}); line(lab,o,E,R)
print("=== Nordnet Global Indeks (CC) ===")
P=M.PREM
cases=[("Base model: premium persists, 0.19%",{},0.0019),
       ("premium halves by exit",dict(prem_exit=1+(P-1)/2),0.0019),
       ("premium gone vs World ex energy (exit x1.012)",dict(prem_exit=1.012),0.0019),
       ("Tesla P/E halves by exit (CC weight 2.95%)",dict(prem_exit=P*(1-0.0295*0.5)),0.0019),
       ("Bear keeps full premium",dict(prem_bear=P),0.0019),
       ("Bear loses full premium",dict(prem_bear=1.0),0.0019),
       ("energy share of World earnings 3% (not 5.5%)",dict(sh=0.03),0.0019),
       ("energy share 8%",dict(sh=0.08),0.0019),
       ("hidden swap drag +0.20% (old EUR-class evidence)",{},0.0039),
       ("cost 0.25% (same as DNB on Nordnet)",{},0.0025)]
for lab,kw,cost in cases:
    c=M.cc_params(**kw); o,E,R=M.run(**c,cost=cost); line(lab,o,E,R)
c=M.cc_params(); 
for d in (-1,1):
    c2=copy.deepcopy(c); c2['pe']={s:[x+d for x in v] for s,v in c['pe'].items()}; o,E,R=M.run(**c2,cost=0.0019); line(f"exit P/E {d:+d}",o,E,R)
o,E,R=M.run(**c,cost=0.0019,eps_mult=0.95); line("CY27 consensus -5%",o,E,R)
# triggers (NAV change at unchanged earnings)
def solve(fn,lo=-0.6,hi=0.4):
    for _ in range(80):
        m=(lo+hi)/2
        if fn(m)>0: lo=m
        else: hi=m
    return m
def met(p,cost,dp):
    p2=dict(p); P0=100*(1+dp)
    o,E,R=M.run(**p2,cost=cost,P0=P0); return o,E,R
for name,p,cost,nav,pe_now in [("DNB GI on Nordnet",W,0.0025,874.58,17.92),("DNB GI in DNB pension",W,0.0021,874.58,17.92),("Nordnet GI",c,0.0019,232.43,18.93)]:
    print("\n== triggers",name)
    for lab,f in [("Base = HY book 6.9% (pre-alert)",lambda o,E,R:o['Base']['irr']-0.069),("E/R = 0.196 (HY market ref)",lambda o,E,R:E/R-0.196),("E/R = 0.291 (HY book)",lambda o,E,R:E/R-0.291),("Base = k 12%",lambda o,E,R:o['Base']['irr']-0.12)]:
        m=solve(lambda x: f(*met(p,cost,x)))
        o,E,R=met(p,cost,m)
        print(f" {lab:34s} {m*100:6.1f}% -> NAV {nav*(1+m):7.1f}; fwd P/E {pe_now*(1+m):.1f} | Base {o['Base']['irr']*100:.1f} E/R {E/R:.3f}")
# structural run (as equity BBB: normalised EPS deflated at 5.5% a year)
for name,p,cost in [("World/DNB 0.25",W,0.0025),("CC/Nordnet 0.19",c,0.0019)]:
    p2=dict(p); p2['eps']={s:[p['eps'][s][3]/1.055**(3-i) for i in range(4)] for s in M.SC}
    o,E,R=M.run(**p2,cost=cost); print(name,"structural IRR",{s:round(o[s]['irr']*100,2) for s in M.SC})
# side case oil Bull 2027
E27w=100/17.3; rw=(0.45*0.90*E27w+15.5*0.92*E27w)/100-1
E27c=100/(17.3*P); x27=(0.90-0.055*(118-30)/49)/0.945; x28=(0.92-0.055*(102-30)/49)/0.945
rc=(0.44*x27*E27c+15.5*P*0.97*x28*E27c)/100-1
print(f"\nside case 2027 (NOK flat): World {rw*100:.1f}%  CC {rc*100:.1f}%  (CC EPS 2027 {x27:.3f}, 2028 {x28:.3f})")
# mid-cycle
print("mid-cycle cash yield CC", round(0.44/(17.0*P)*100,2), "World", round(0.45/17.0*100,2))
