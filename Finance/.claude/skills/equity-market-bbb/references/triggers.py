import io, contextlib, json
src=open("model.py").read().split("# ---------- oil-shock")[0]
buf=io.StringIO()
with contextlib.redirect_stdout(buf): exec(src)
def solve(fn, target, lo=40, hi=130):
    for _ in range(80):
        m=(lo+hi)/2
        if fn(m)>target: lo=m   # fn decreasing in price
        else: hi=m
    return m
def metrics(P, which):
    if which=="osl": o,E,R,_=run("x",P,E27,eps,pe_osl,0.66,0.056*100/P,verbose=False)
    else: o,E,R,_=run("x",P,E27w,epsw,pe_w,0.45,0.025*100/P,fx=fxw,fx_share=1.0,verbose=False)
    return o,E,R
for which,lev,name in [("osl",2068.38,"OSEBX"),("w",100,"World NOK")]:
    print("\n==",name)
    for lab,fn,tgt in [("Base IRR = 12% (k)",lambda P:metrics(P,which)[0]["Base"]["irr"],0.12),
                       ("E/R = HY market ref 0.196",lambda P:(lambda o,E,R:E/R)(*metrics(P,which)),0.196),
                       ("E/R = HY book 0.291",lambda P:(lambda o,E,R:E/R)(*metrics(P,which)),0.291),
                       ("Base IRR = HY book 6.9%",lambda P:metrics(P,which)[0]["Base"]["irr"],0.069),
                       ("Base IRR = 9.0% (HY 6.9 + ~2pp, tax-neutral-ish)",lambda P:metrics(P,which)[0]["Base"]["irr"],0.09)]:
        P=solve(fn,tgt); o,E,R=metrics(P,which)
        print(f" {lab:45s} price {P:5.1f} ({P-100:+.1f}%) level {lev*P/100:8.1f} | Base {o['Base']['irr']*100:.1f}% Bear27 {o['Bear']['r'][0]*100:.1f}% E {E:.2f} R {R:.1f} E/R {E/R:.3f}")
# structural run Oslo: EPS at Base normalized level from 2027
o,E,R,_=run("struct",100,E27,{s:[eps[s][3]]*4 for s in SC},pe_osl,0.66,0.056,verbose=False)
print("\nOslo structural IRR", {s:round(o[s]['irr']*100,1) for s in SC})
o,E,R,_=run("struct",100,E27w,{s:[epsw[s][3]/1.055**(3-i) for i in range(4)] for s in SC},pe_w,0.45,0.025,verbose=False)
# sensitivities Oslo exit PE
for d in (-1,1):
    pe2={s:[x+d for x in v] for s,v in pe_osl.items()}
    o,E,R,_=run("s",100,E27,eps,pe2,0.66,0.056,verbose=False); print("Oslo exit P/E",d,"Base IRR",round(o['Base']['irr']*100,1))
    pe2={s:[x+d for x in v] for s,v in pe_w.items()}
    o,E,R,_=run("s",100,E27w,epsw,pe2,0.45,0.025,fx=fxw,fx_share=1.0,verbose=False); print("World exit P/E",d,"Base IRR",round(o['Base']['irr']*100,1))
# Brent +/-10 in Oslo base all years
for d in (-10,10):
    epsx=[sum(w[b]*((blocks['Base'][b][i]) if b!='E' else (([85,77,72,70][i]+d-30)/49)) for b in w) for i in range(4)]
    o,E,R,_=run("s",100,E27,{"Bear":eps["Bear"],"Base":epsx,"Bull":eps["Bull"]},pe_osl,0.66,0.056,verbose=False); print("Oslo Brent path",d,"Base IRR",round(o['Base']['irr']*100,1), [round(x,3) for x in epsx])
# hedged world NOK: USD return + carry
o,E,R,_=run("h",100,E27w,epsw,pe_w,0.45,0.025,verbose=False)
carry=[4.79-3.6,4.39-3.4,3.86-3.25]  # [A] SOFR path guess
print("Hedged world: Base 2027", round((o['Base']['r'][0])*100+carry[0],1),"Bear 2027",round(o['Bear']['r'][0]*100+(4.21-3.0),1))
