import json, math
L=lambda s: json.load(open(f"data/d_{s}.json"))
F=L("0P00000MVB.IR"); U=L("URTH"); X=L("NOK_X"); O=L("OSEBX.OL"); B=L("BZ_F"); I=L("IXN")
def me(d,i=1): return {k:v[i] for k,v in d["me"].items()}
f=me(F); u=me(U); x=me(X,0); o=me(O); b=me(B,0); ix=me(I)
keys=sorted(k for k in f if k in u and k in x and k in o and k in b and k in ix)
keys=[k for k in keys if k<="2026-09"]
print("months",keys[0],keys[-1],len(keys))
def lr(s): return [math.log(s[keys[i]]/s[keys[i-1]]) for i in range(1,len(keys))]
wn={k:u[k]*x[k] for k in keys}; ixn={k:ix[k]*x[k] for k in keys}
R={"fund":lr(f),"worldNOK":lr(wn),"worldUSD":lr(u),"IXN_NOK":lr(ixn),"OSEBX":lr(o),"Brent":lr(b),"USDNOK":lr(x)}
def st(a): m=sum(a)/len(a); return math.sqrt(sum((v-m)**2 for v in a)/(len(a)-1))
def corr(a,c):
    ma=sum(a)/len(a); mc=sum(c)/len(c); cov=sum((p-ma)*(q-mc) for p,q in zip(a,c))/(len(a)-1); return cov/st(a)/st(c), cov/st(c)**2
for k,v in R.items(): print(f"vol {k:9s} {st(v)*math.sqrt(12)*100:5.1f}%")
for k in ["worldNOK","worldUSD","IXN_NOK","OSEBX","Brent","USDNOK"]:
    c,beta=corr(R["fund"],R[k]); print(f"fund ~ {k:9s} corr {c:5.2f} beta {beta:5.2f}")
# drawdown daily
pk=0;dd=0;w=None
for d,c,a in F["daily"]:
    pk=max(pk,a); v=a/pk-1
    if v<dd: dd=v; w=d
print("max daily drawdown fund since 2022-03", round(dd*100,1), w)
# 2026 drawdown
pk=0;dd=0
for d,c,a in F["daily"]:
    if d<"2025-12-31": continue
    pk=max(pk,a); v=a/pk-1
    if v<dd: dd=v; w=d
print("2026 max drawdown", round(dd*100,1), w)
for y in ["2022","2023","2024","2025","2026"]:
    pass
def yr(s,a,bk): return (s[bk]/s[a]-1)*100
for a,bk in [("2022-03","2022-12"),("2022-12","2023-12"),("2023-12","2024-12"),("2024-12","2025-12"),("2025-12","2026-09")]:
    print(a,bk,"fund %.1f worldNOK %.1f IXN_NOK %.1f"%(yr(f,a,bk),yr(wn,a,bk),yr(ixn,a,bk)))
# episodes
for a,bk in [("2022-03","2022-09"),("2025-12","2026-02"),("2025-01","2025-04")]:
    if a in f and bk in f: print("episode",a,bk,"fund %.1f worldNOK %.1f IXN_NOK %.1f USDNOK %.1f"%(yr(f,a,bk),yr(wn,a,bk),yr(ixn,a,bk),yr(x,a,bk)))
# monthly path 2026
for k in keys:
    if k>="2025-10": print(k, round(f[k],1), round(wn[k],1), round(x[k],4))
