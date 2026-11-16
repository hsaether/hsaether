# IQQK / Korea (docs/kospi-analysis.md), version 1.9 (16 Nov 2026): attribution v1.8 -> v1.9 in steps, each one change, by
# running korea.py with switches. Spot FX held flat (the decision); P_k in EUR = P_k on the index x the EUR analysis level.
# Usage: py attrib19.py
import subprocess, sys, re, os
HERE=os.path.dirname(os.path.abspath(__file__))
LVL={"D06":88.6,"16":91.55}     # EUR analysis level (NAV-equivalent at the Seoul close): 6 Nov (v1.8); 16 Nov (v1.9, see the document Header)
STEPS=[("v1.8 (6 Nov close, v2 blocks)",["D06"],"D06"),
       ("price: 16 Nov close, stub 45 days, v2 blocks re-priced",["S2","H2"],"16"),
       ("Samsung v3 (common and preference)",["H2"],"16"),
       ("SK hynix v3 (SK Square still on v2)",["QV2"],"16"),
       ("holdcos: SK Square on SK hynix v3 (= v1.9)",[],"16")]
def run(sw):
    out=subprocess.run([sys.executable,os.path.join(HERE,"korea.py"),"FUND","IQQK","IMPL","SPOT"]+sw,capture_output=True,text=True,cwd=HERE).stdout
    spot=out[out.index("at spot FX held flat"):]
    r={}
    for s in ("Bear","Base","Bull","Cap"):
        m=re.search(rf"  {s:4s} IRR\s+(-?[\d.]+) \| 2027\s+(-?[\d.]+) .*?Pk ([\d.]+) MoS ([+-][\d.]+)% capital ([+-][\d.]+)%",spot)
        r[s]=tuple(float(x) for x in m.groups())
    m=re.search(r"exit P/E 10 \(Base\)\s+2028-30 x m: k at x([\d.]+), 0% at x([\d.]+)",out); r["m"]=(float(m.group(1)),float(m.group(2)))
    m=re.search(r"IQQK: S ([\d.]+) pref ([\d.]+) H ([\d.]+)",out) or re.search(r"IQQK at \S+: S ([\d.]+) pref ([\d.]+) H ([\d.]+)",out)
    return r
prev=None
print(f"{'step':58s} {'Base':>6s} {'dBase':>6s} {'MoS':>7s} {'PkEUR':>7s} {'dPkEUR':>7s} {'Bear':>5s} {'Cap':>6s} {'Cap27':>6s} {'Bull':>5s} {'m_k':>5s} {'m_0':>5s}")
for lab,sw,lv in STEPS:
    r=run(sw); b=r["Base"]; pk=b[2]*LVL[lv]/100
    d=(b[0]-prev[0][0]) if prev else 0.0; dp=(pk-prev[1]) if prev else 0.0
    print(f"{lab:58s} {b[0]:6.1f} {d:+6.1f} {b[3]:+6.1f}% {pk:7.1f} {dp:+7.1f} {r['Bear'][0]:5.1f} {r['Cap'][0]:6.1f} {r['Cap'][1]:6.1f} {r['Bull'][0]:5.1f} {r['m'][0]:5.2f} {r['m'][1]:5.2f}")
    prev=(b,pk)
