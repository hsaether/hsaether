import csv, json, math
# NB daily -> month-end
me={}
with open("nb/exr_daily.csv",encoding="utf-8") as f:
    for r in csv.DictReader(f,delimiter=";"):
        if r["OBS_VALUE"]=="" : continue
        y,m,d=r["TIME_PERIOD"].split("-"); me.setdefault(r["BASE_CUR"],{})[(int(y),int(m))]=float(r["OBS_VALUE"])  # last day wins (sorted asc)
i44,twi,usd,eur=me["I44"],me["TWI"],me["USD"],me["EUR"]
def ld(f): return {tuple(map(int,k.split("-"))):v for k,v in json.load(open(f)).items()}
br={k:v[0] for k,v in ld("data/long_BZ_F.json").items()}; ur={k:v[1] for k,v in ld("data/long_URTH.json").items()}; ob={k:v[1] for k,v in ld("data/long_OSEBX.OL.json").items()}
corr=lambda a,b:(lambda n,ma,mb:sum((x-ma)*(y-mb) for x,y in zip(a,b))/math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b)))(len(a),sum(a)/len(a),sum(b)/len(b))
beta=lambda y,x:(lambda mx,my:sum((a-mx)*(b-my) for a,b in zip(x,y))/sum((a-mx)**2 for a in x))(sum(x)/len(x),sum(y)/len(y))
R=lambda s,ks:[math.log(s[k]/s[p]) for p,k in zip(ks[:-1],ks[1:])]
sd=lambda a:math.sqrt(sum((x-sum(a)/len(a))**2 for x in a)/(len(a)-1))*math.sqrt(12)
def ols(X,y):
    k=len(X[0]); M=[[sum(r[i]*r[j] for r in X) for j in range(k)]+[sum(r[i]*yy for r,yy in zip(X,y))] for i in range(k)]
    for i in range(k):
        for r in range(k):
            if r!=i: f=M[r][i]/M[i][i]; M[r]=[a-f*b for a,b in zip(M[r],M[i])]
    b=[M[i][k]/M[i][i] for i in range(k)]; yh=[sum(c*x for c,x in zip(b,r)) for r in X]; my=sum(y)/len(y)
    return b,1-sum((a-c)**2 for a,c in zip(y,yh))/sum((a-my)**2 for a in y)
for start,lab in [((2013,3),"13.6y"),((2016,10),"10y"),((2021,10),"5y"),((2023,10),"3y")]:
    ks=sorted(k for k in set(i44)&set(br)&set(usd)&set(eur)&set(ur) if start<=k<=(2026,10))
    s44=[-x for x in R(i44,ks)]; b=R(br,ks); w=R(ur,ks)
    bb,r2=ols([[1,x,y] for x,y in zip(w,b)],s44)
    print(f"{lab:6s} {ks[0]}-{ks[-1]} n={len(b)} | I44~Brent {corr(s44,b):.2f} (beta {beta(s44,b):.3f}) | I44~World {corr(s44,w):.2f} | NOK(I44) = {bb[1]:.2f} World + {bb[2]:.3f} Brent R2 {r2:.2f} | vol I44 {sd(s44)*100:.1f}")
