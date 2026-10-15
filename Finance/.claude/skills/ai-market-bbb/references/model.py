# AI Market BBB — layer baskets, IAF index-level build (USD and NOK). Prices: Yahoo close 14 Oct 2026 (US, Europe) and 15 Oct 2026 (Korea).
import json
KRW=1348.18; EUR=1.1212
q={r['symbol']:r for r in json.load(open('data/q.json'))}
def mc(s):
    r=q[s]; m=r.get('marketCap') or 0
    if r.get('currency')=='KRW': m/=KRW
    if r.get('currency')=='EUR': m*=EUR
    return m/1e9
# CY27 consensus EPS (Yahoo earningsTrend 11-12 Oct 2026; Samsung, TSM 15 Oct); calendarised [A]
eps27={'NVDA':15.9146,'AMD':15.72189,'AVGO':19.39382,'MRVL':7.28277,
 'MU':206.33243,'000660.KS':470324.3,'005930.KS':72180.14,
 'TSM':22.31735,'ASML':58.475166,'AMAT':18.47894,'LRCX':11.76415,
 'ANET':5.21686,'VRT':9.18451,'ETN':16.2461,
 'MSFT':(19.76867+23.67732)/2,'GOOGL':14.97242,'AMZN':10.5269,'META':34.07467,'ORCL':(8.14059+10.99899)/2,
 'NOW':5.00551,'CRM':16.0207,'ADBE':27.67328,'PLTR':2.35154,'SAP.DE':8.36656,'INTU':27.07543,'SNOW':3.0052,'DDOG':2.97446}
eps26={'NVDA':9.31242,'AMD':7.5868,'AVGO':11.65755,'TSM':17.05163,'MU':176.15115,'000660.KS':355218.94,'ANET':4.11606,'VRT':6.73858,
 'MSFT':(17.28+19.76867)/2,'META':31.04359,'ORCL':(7.63+8.14059)/2,'NOW':4.06673,'CRM':16.75426,'ADBE':24.48076,'PLTR':1.61977,'SAP.DE':7.13653,'SNOW':2.22305}
L={ # layer: members, Base/Bear/Bull EPS 2027,2028,2029,2030(norm) vs CY27 cons=1, exit PE B/Base/Bull, payout
 'H1 Compute (NVDA AMD AVGO MRVL)':(['NVDA','AMD','AVGO','MRVL'],
   dict(Bear=(.70,.60,.70,.75),Base=(.92,.98,1.00,.97),Bull=(1.0,1.15,1.25,1.30)),(13,17,19),.25),
 'H2 Memory (MU SK hynix Samsung)':(['MU','000660.KS','005930.KS'],
   dict(Bear=(.60,.30,.25,.25),Base=(.90,.60,.40,.35),Bull=(1.0,.80,.55,.45)),(8,10,11),.15),
 'H3 Foundry and equipment (TSM ASML AMAT LRCX)':(['TSM','ASML','AMAT','LRCX'],
   dict(Bear=(.80,.75,.85,.92),Base=(.95,1.03,1.10,1.16),Bull=(1.0,1.15,1.28,1.40)),(14,18,21),.45),
 'H4 Networking and DC infrastructure (ANET VRT ETN)':(['ANET','VRT','ETN'],
   dict(Bear=(.75,.65,.75,.85),Base=(.95,1.02,1.07,1.11),Bull=(1.0,1.12,1.22,1.30)),(15,20,24),.35),
 'E Engines and cloud platforms (MSFT GOOGL AMZN META ORCL)':(['MSFT','GOOGL','AMZN','META','ORCL'],
   dict(Bear=(.88,.88,.97,1.05),Base=(.97,1.07,1.17,1.27),Bull=(1.0,1.13,1.27,1.41)),(17,21,23.5),.34),
 'T Tools and application software (NOW CRM ADBE PLTR SAP INTU SNOW DDOG)':(['NOW','CRM','ADBE','PLTR','SAP.DE','INTU','SNOW','DDOG'],
   dict(Bear=(.88,.85,.93,1.00),Base=(.95,1.03,1.11,1.19),Bull=(1.0,1.10,1.20,1.30)),(15,20,24),.45),
}
FX=dict(Bear=(10.70,10.42,10.42),Base=(9.5555,9.5555,9.5555),Bull=(9.27,9.27,9.27)); FX0=9.5555
NIB=4.38; T0=77/365  # 15 Oct -> 31 Dec
def irr(fl):
    lo,hi=-0.9,2.0
    for _ in range(200):
        m=(lo+hi)/2; v=sum(c/(1+m)**t for t,c in fl)
        lo,hi=(m,hi) if v>0 else (lo,m)
    return m
out={}
for name,(mem,E,PE,po) in L.items():
    W={s:mc(s) for s in mem}; Wt=sum(W.values())
    # basket P/E on CY27 = sum mcap / sum (mcap/PE_i)
    pe27=Wt/sum(W[s]/(q[s]['regularMarketPrice']/eps27[s]) for s in mem)
    g=[eps27[s]/eps26[s]-1 for s in mem if s in eps26]
    g2627=sum(W[s]*(eps27[s]/eps26[s]-1) for s in mem if s in eps26)/sum(W[s] for s in mem if s in eps26)
    res={}
    for i,sc in enumerate(['Bear','Base','Bull']):
        e=E[sc]; ex=PE[i]; P=pe27
        pe_path=[ex,ex,ex] if sc=='Bear' else [P+(ex-P)*k/3 for k in (1,2,3)]
        V=[pe_path[k]*e[k+1] for k in range(3)]   # year-end value on next-year EPS
        D=[po*e[k] for k in range(3)]
        for cur in ('USD','NOK'):
            f=[x/FX0 for x in FX[sc]] if cur=='NOK' else [1,1,1]
            fl=[(0,-P)]+[(T0+k+0.5,D[k]*f[k]) for k in range(3)]+[(T0+3,V[2]*f[2])]
            res[(sc,cur)]=irr(fl)*100
            if cur=='NOK':
                r27=((V[0]+D[0])*f[0]/P-1)*100; res[(sc,'r27')]=r27
        # hurdle at k=12% NOK
        if sc=='Base':
            f=[x/FX0 for x in FX[sc]]
            pk=sum(D[k]*f[k]/1.12**(T0+k+0.5) for k in range(3))+V[2]*f[2]/1.12**(T0+3)
            res['Pk']=pk; res['mos']=(pk/P-1)*100
    E_=res[('Base','NOK')]-NIB; R_=res[('Base','r27')]-res[('Bear','r27')]
    out[name]=dict(mcap=Wt,pe27=pe27,g2627=g2627*100,**{f'{a}_{b}':v for (a,b),v in [(k,v) for k,v in res.items() if isinstance(k,tuple)]},Pk=res['Pk'],mos=res['mos'],E=E_,R=R_,ER=E_/R_)
    print(f"\n== {name}: mcap ${Wt:,.0f}bn  P/E CY27 {pe27:.1f}  cons EPS 26->27 {g2627*100:+.0f}%")
    for sc in ('Bear','Base','Bull'):
        print(f"   {sc:4s} IRR USD {res[(sc,'USD')]:6.1f}%  NOK {res[(sc,'NOK')]:6.1f}%  2027 NOK {res[(sc,'r27')]:6.1f}%")
    print(f"   Hurdle P/E (k=12%, NOK) {res['Pk']:.1f} vs {pe27:.1f}: MoS {res['mos']:+.1f}%   E {E_:.2f} R {R_:.1f} E/R {E_/R_:.3f}")

# implied growth: constant annual EPS growth g after 2027 (from Base 2027 level) at Base exit P/E that gives 12% NOK
def irr_g(name,g):
    mem,E,PE,po=L[name]; e0=E['Base'][0]; e=[e0,e0*(1+g),e0*(1+g)**2,e0*(1+g)**3]; P=out[name]['pe27']; ex=PE[1]
    pe_path=[P+(ex-P)*k/3 for k in (1,2,3)]; V=[pe_path[k]*e[k+1] for k in range(3)]; D=[po*e[k] for k in range(3)]
    return irr([(0,-P)]+[(T0+k+0.5,D[k]) for k in range(3)]+[(T0+3,V[2])])
for name in L:
    lo,hi=-0.5,1.5
    for _ in range(80):
        m=(lo+hi)/2
        lo,hi=(m,hi) if irr_g(name,m)<0.12 else (lo,m)
    out[name]['g_req']=m*100
    print(f'{name[:40]:40s} EPS growth/yr 2028-30 needed for 12% at Base exit P/E: {m*100:5.1f}%')
json.dump(out,open('model_out.json','w'),default=float,indent=1)
tot=sum(v['mcap'] for v in out.values()); print('\nTotal basket mcap $bn',round(tot))
for n,v in out.items(): print(f"{n[:3]} weight {v['mcap']/tot*100:.0f}%")
