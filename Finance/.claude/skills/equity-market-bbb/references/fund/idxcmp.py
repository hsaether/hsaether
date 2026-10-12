import json, math, datetime as dt
L=lambda s: json.load(open(f"data/d_{s}.json"))
N=L("0P0001K6NJ.IR"); D=L("0P0000PS3V.IR"); U=L("URTH"); X=L("NOK_X"); O=L("OSEBX.OL"); B=L("BZ_F")
def dd(s): return {d:a for d,c,a in s["daily"]}
n=dd(N); d=dd(D); u=dd(U); x=dd(X)
def at(s,day):  # last value on or before day
    ks=[k for k in s if k<=day]; return s[max(ks)] if ks else None
def lastday(s,day): ks=[k for k in s if k<=day]; return max(ks)
print("Nordnet first/last",min(n),max(n)," DNB first/last",min(d),max(d))
wn=lambda day: at(u,day)*at(x,day)
pts=[("2020-09-02","2020-12-31"),("2020-12-31","2021-12-31"),("2021-12-31","2022-12-30"),("2022-03-07","2022-12-30"),("2022-12-30","2023-12-29"),("2023-12-29","2024-12-31"),("2024-12-31","2025-12-31"),("2025-12-31","2026-10-08"),
     ("2022-03-07","2026-10-08"),("2025-06-02","2026-10-08"),("2023-10-06","2026-10-08"),("2025-10-08","2026-10-08"),("2021-10-08","2026-10-08")]
print(f"{'period':25s} {'Nordnet':>8s} {'DNB':>8s} {'URTHxNOK':>9s} {'N-D':>7s} {'N-U':>7s} {'D-U':>7s} ann(N-D)")
for a,b in pts:
    rn=at(n,b)/at(n,a)-1
    rd=(at(d,b)/at(d,a)-1) if a>=min(d) else None
    ru=wn(b)/wn(a)-1
    yrs=(dt.date.fromisoformat(b)-dt.date.fromisoformat(a)).days/365.25
    s=f"{a}->{b} {rn*100:8.2f} {'' if rd is None else f'{rd*100:8.2f}':>8s} {ru*100:9.2f}"
    if rd is not None:
        ann=((1+rn)/(1+rd))**(1/yrs)-1
        s+=f" {(rn-rd)*100:7.2f} {(rn-ru)*100:7.2f} {(rd-ru)*100:7.2f}  {ann*100:6.2f}/yr ({yrs:.2f}y)"
    else:
        ann=((1+rn)/(1+ru))**(1/yrs)-1; s+=f" {'':7s} {(rn-ru)*100:7.2f} {'':7s}  N-U {ann*100:6.2f}/yr"
    print(s)
# monthly log returns, month-end, overlap
def me(s,i=1): return {k:v[i] for k,v in s["me"].items()}
mn=me(N); md=me(D); mu=me(U); mx=me(X,0); mo=me(O); mb=me(B,0)
keys=sorted(k for k in mn if k in md and k in mu and k in mx and k<="2026-09")
print("overlap months",keys[0],keys[-1],len(keys))
lr=lambda s,ks:[math.log(s[ks[i]]/s[ks[i-1]]) for i in range(1,len(ks))]
wnm={k:mu[k]*mx[k] for k in mu if k in mx}
def st(a): m=sum(a)/len(a); return math.sqrt(sum((v-m)**2 for v in a)/(len(a)-1))
def corr(a,c):
    ma=sum(a)/len(a); mc=sum(c)/len(c); cov=sum((p-ma)*(q-mc) for p,q in zip(a,c))/(len(a)-1); return cov/st(a)/st(c), cov/st(c)**2
R={"Nordnet":lr(mn,keys),"DNB":lr(md,keys),"WorldNOK":lr(wnm,keys),"WorldUSD":lr(mu,keys),"OSEBX":lr(mo,keys),"Brent":lr(mb,keys),"USDNOK":lr(mx,keys)}
for k,v in R.items(): print(f"vol {k:9s} {st(v)*math.sqrt(12)*100:5.1f}%")
for f in ["Nordnet","DNB"]:
    for k in ["WorldNOK","WorldUSD","OSEBX","Brent","USDNOK"] + (["DNB"] if f=="Nordnet" else []):
        c,b=corr(R[f],R[k]); print(f"{f} ~ {k:9s} corr {c:5.3f} beta {b:5.2f}")
# tracking error Nordnet vs DNB monthly
diff=[a-b for a,b in zip(R["Nordnet"],R["DNB"])]; print("TE Nordnet vs DNB (monthly, ann.)", round(st(diff)*math.sqrt(12)*100,2),"%  mean diff/yr", round(sum(diff)/len(diff)*12*100,2))
diff2=[a-b for a,b in zip(R["DNB"],R["WorldNOK"])]; print("TE DNB vs URTHxNOK", round(st(diff2)*math.sqrt(12)*100,2),"% mean/yr", round(sum(diff2)/len(diff2)*12*100,2))
# subperiods: before/after index change Jun-2025
for lab,cond in [("pre Jun-25",lambda k:k<="2025-05"),("post Jun-25",lambda k:k>="2025-06")]:
    ks=[k for k in keys if cond(k)]
    if lab.startswith("post"): ks=["2025-05"]+ks
    a=lr(mn,ks); b=lr(md,ks); df=[p-q for p,q in zip(a,b)]
    print(lab, ks[0],ks[-1], "TE", round(st(df)*math.sqrt(12)*100,2), "mean diff/yr", round(sum(df)/len(df)*12*100,2), "corr", round(corr(a,b)[0],3))
# max drawdowns daily
for nm,s in [("Nordnet",n),("DNB",d)]:
    pk=0;mdd=0;w=None
    for k in sorted(s):
        if k<"2022-03-07": continue
        pk=max(pk,s[k]); v=s[k]/pk-1
        if v<mdd: mdd=v; w=k
    print(nm,"max daily drawdown since Mar-22",round(mdd*100,1),w)
# Nordnet from start: CAGR vs World NOK
a="2020-09-02"; b="2026-10-08"; yrs=(dt.date.fromisoformat(b)-dt.date.fromisoformat(a)).days/365.25
print("Nordnet since start CAGR", round(((at(n,b)/at(n,a))**(1/yrs)-1)*100,2), "URTHxNOK", round(((wn(b)/wn(a))**(1/yrs)-1)*100,2))
