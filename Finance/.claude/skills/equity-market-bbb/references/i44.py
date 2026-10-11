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
print("I-44 now", i44[(2026,10)], "TWI", twi[(2026,10)], "USD", usd[(2026,10)], "EUR", eur[(2026,10)])
# NOK strength = -dlog(I44)
for start,lab in [((2007,8),"since 2007"),((2016,9),"10y"),((2021,9),"5y"),((2023,9),"3y")]:
    ks=sorted(k for k in set(i44)&set(br)&set(usd)&set(eur)&set(ur) if start<=k<=(2026,9))
    s44=[-x for x in R(i44,ks)]; su=[-x for x in R(usd,ks)]; se=[-x for x in R(eur,ks)]; b=R(br,ks); w=R(ur,ks)
    bb,r2=ols([[1,x,y] for x,y in zip(w,b)],s44)
    print(f"{lab:10s} n={len(b)} | I44~Brent {corr(s44,b):.2f} (beta {beta(s44,b):.3f}) | USD~Brent {corr(su,b):.2f} | EUR~Brent {corr(se,b):.2f} | I44~World {corr(s44,w):.2f} | NOK(I44) = {bb[1]:.2f} World + {bb[2]:.3f} Brent R2 {r2:.2f} | vol I44 {sd(s44)*100:.1f} USD {sd(su)*100:.1f} EUR {sd(se)*100:.1f}")
print("\nRolling 36m at Sep: I44~Brent | I44~World(USD)")
for y in range(2010,2027):
    ks=sorted(k for k in set(i44)&set(br)&set(ur) if k<=(y,9))[-37:]
    s44=[-x for x in R(i44,ks)]; print(y, f"{corr(s44,R(br,ks)):.2f} {corr(s44,R(ur,ks)):.2f}")
# levels: annual avg I44 from monthly NB file
mon={}
with open("nb/exr_monthly.csv",encoding="utf-8") as f:
    for r in csv.DictReader(f,delimiter=";"):
        if r["BASE_CUR"]=="I44" and r["OBS_VALUE"]: mon[r["TIME_PERIOD"]]=float(r["OBS_VALUE"])
ann={}
for k,v in mon.items(): ann.setdefault(int(k[:4]),[]).append(v)
print("\nI-44 annual averages:", {y:round(sum(v)/len(v),1) for y,v in sorted(ann.items()) if y%2==0 or y>=2020})
vals=list(mon.values()); cur=i44[(2026,10)]
for lab,st in [("1990-",1990),("2000-",2000),("2014-",2014),("2016-",2016)]:
    v=[x for k,x in mon.items() if int(k[:4])>=st]; print(lab, "avg",round(sum(v)/len(v),1),"min",min(v),"max",max(v),"pct rank now",round(sum(1 for x in v if x<cur)/len(v)*100))
# Episodes I44
for a,b,lab in [((2014,6),(2016,1),"oil crash"),((2019,12),(2020,3),"covid"),((2022,5),(2022,9),"2022"),((2025,12),(2026,9),"2026 YTD"),((2008,7),(2008,12),"GFC")]:
    print(lab, f"I44 {(i44[b]/i44[a]-1)*100:+.1f}% Brent {(br[b]/br[a]-1)*100:+.1f}% USD {(usd[b]/usd[a]-1)*100:+.1f}% EUR {(eur[b]/eur[a]-1)*100:+.1f}%")
# World in NOK via I44-like translation? compare world NOK (USD) vol 
