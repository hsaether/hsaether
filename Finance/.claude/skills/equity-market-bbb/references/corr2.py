import json, math
def load(f, adj=True):
    d=json.load(open(f"data/d_{f}.json")); return {tuple(map(int,k.split('-'))):(v[1] if adj else v[0]) for k,v in d["me"].items()}
osebx=load("OSEBX.OL"); brent=load("BZ_F",False); usdnok=load("NOK_X",False); eurnok=load("EURNOK_X",False); urth=load("URTH"); acwi=load("ACWI")
def corr(a,b):
    n=len(a); ma=sum(a)/n; mb=sum(b)/n
    return sum((x-ma)*(y-mb) for x,y in zip(a,b))/math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))
def beta(y,x):
    mx=sum(x)/len(x); my=sum(y)/len(y); return sum((a-mx)*(b-my) for a,b in zip(x,y))/sum((a-mx)**2 for a in x)
def ols(X,y):
    k=len(X[0]); M=[[sum(r[i]*r[j] for r in X) for j in range(k)]+[sum(r[i]*yy for r,yy in zip(X,y))] for i in range(k)]
    for i in range(k):
        for r in range(k):
            if r!=i:
                f=M[r][i]/M[i][i]; M[r]=[a-f*b for a,b in zip(M[r],M[i])]
    b=[M[i][k]/M[i][i] for i in range(k)]; yh=[sum(c*x for c,x in zip(b,r)) for r in X]; my=sum(y)/len(y)
    return b, 1-sum((a-c)**2 for a,c in zip(y,yh))/sum((a-my)**2 for a in y)
sd=lambda a: math.sqrt(sum((x-sum(a)/len(a))**2 for x in a)/(len(a)-1))*math.sqrt(12)
keys=sorted(k for k in set(osebx)&set(brent)&set(usdnok)&set(urth)&set(eurnok) if (2013,3)<=k<=(2026,9))
def R(s,ks): return [math.log(s[k]/s[p]) for p,k in zip(ks[:-1],ks[1:])]
def win(start,end=(2026,9)):
    ks=[k for k in keys if start<=k<=end]
    ob,br,un,en,ur=R(osebx,ks),R(brent,ks),R(usdnok,ks),R(eurnok,ks),R(urth,ks)
    ns=[-x for x in un]; nse=[-x for x in en]; wn=[a+b for a,b in zip(ur,un)]; bn=[a+b for a,b in zip(br,un)]
    b,r2=ols([[1,a,c] for a,c in zip(ur,br)],ob); b2,r22=ols([[1,a,c] for a,c in zip(ur,br)],ns)
    yrs=(len(ks)-1)/12; cg=lambda s:((s[ks[-1]]/s[ks[0]])**(1/yrs)-1)*100
    wnl={k:urth[k]*usdnok[k] for k in ks}
    print(f"{ks[0]}-{ks[-1]} n={len(ob)} | OSEBX~Brent {corr(ob,br):.2f} (beta {beta(ob,br):.2f}) | OSEBX~BrentNOK {corr(ob,bn):.2f} | NOK/USD~Brent {corr(ns,br):.2f} (beta {beta(ns,br):.3f}) | NOK/EUR~Brent {corr(nse,br):.2f} (beta {beta(nse,br):.3f}) | OSEBX~WorldNOK {corr(ob,wn):.2f} (beta {beta(ob,wn):.2f}) | OSEBX~WorldUSD {corr(ob,ur):.2f} | World~Brent {corr(ur,br):.2f} | NOK~WorldUSD {corr(ns,ur):.2f}")
    print(f"   OSEBX = {b[0]*1200:.1f}%/yr + {b[1]:.2f} World(USD) + {b[2]:.2f} Brent  R2 {r2:.2f} | NOK/USD = {b2[1]:.2f} World + {b2[2]:.3f} Brent R2 {r22:.2f}")
    print(f"   vol: OSEBX {sd(ob)*100:.1f} World USD {sd(ur)*100:.1f} World NOK {sd(wn)*100:.1f} Brent {sd(br)*100:.1f} USDNOK {sd(un)*100:.1f} | CAGR OSEBX {cg(osebx):.1f} WorldTR USD {cg(urth):.1f} WorldTR NOK {cg(wnl):.1f} Brent {cg(brent):.1f} USDNOK {cg(usdnok):.1f}")
for s in [(2013,3),(2016,9),(2021,9),(2023,9)]: win(s)
print("\nYear | OSEBX TR | World TR USD | World TR NOK | Brent chg | USDNOK chg | EURNOK chg")
for y in range(2014,2027):
    s=(y-1,12); e=(y,12) if y<2026 else (2026,10)
    f=lambda d:(d[e]/d[s]-1)*100
    print(y, " ".join(f"{v:6.1f}" for v in [f(osebx),f(urth),((urth[e]*usdnok[e])/(urth[s]*usdnok[s])-1)*100,f(brent),f(usdnok),f(eurnok)]))
print("\nRolling 36m corr at Sep: OSEBX~Brent | NOK/USD~Brent | NOK/EUR~Brent | OSEBX~WorldNOK")
for y in range(2016,2027):
    ks=[k for k in keys if k<=(y,9)][-37:]
    ob,br,un,en,ur=R(osebx,ks),R(brent,ks),R(usdnok,ks),R(eurnok,ks),R(urth,ks)
    print(y, f"{corr(ob,br):.2f} {corr([-x for x in un],br):.2f} {corr([-x for x in en],br):.2f} {corr(ob,[a+b for a,b in zip(ur,un)]):.2f}")
print("\nEpisodes (month-end): OSEBX | Brent | USDNOK | World USD | World NOK")
for a,b,lab in [((2014,6),(2016,1),"oil crash 14-16"),((2019,12),(2020,3),"covid"),((2022,5),(2022,9),"2022 rates"),((2018,9),(2018,12),"Q4-18"),((2026,2),(2026,5),"2026 war spring"),((2025,12),(2026,9),"YTD-26")]:
    f=lambda d:(d[b]/d[a]-1)*100
    print(lab, a,b, " ".join(f"{v:6.1f}" for v in [f(osebx),f(brent),f(usdnok),f(urth),((urth[b]*usdnok[b])/(urth[a]*usdnok[a])-1)*100]))
pk=0;m=0
for k in keys:
    pk=max(pk,osebx[k]); m=min(m,osebx[k]/pk-1)
print("max drawdown month-end OSEBX", round(m*100,1))
# daily max drawdown OSEBX
d=json.load(open("data/d_OSEBX.OL.json"))["daily"]; pk=0; m=0; at=None
for t,c,a in d:
    pk=max(pk,c)
    if c/pk-1<m: m=c/pk-1; at=t
print("max daily drawdown OSEBX", round(m*100,1), at)
