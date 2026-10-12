import json
L=lambda s: json.load(open(f"data/d_{s}.json"))
n={d:a for d,c,a in L("0P0001K6NJ.IR")["daily"]}; d={x:a for x,c,a in L("0P0000PS3V.IR")["daily"]}
def at(s,day): return s[max(k for k in s if k<=day)]
def lst(s,day): return max(k for k in s if k<=day)
for a,b,cc,w in [("2025-09-30","2026-09-30",14.86,15.24),("2025-12-31","2026-09-30",11.09,11.75)]:
    rn=at(n,b)/at(n,a)-1; rd=at(d,b)/at(d,a)-1
    rel=(1+rn)/(1+rd)-1; idx=(1+cc/100)/(1+w/100)-1
    print(f"{a}->{b} [{lst(n,a)},{lst(n,b)} | {lst(d,a)},{lst(d,b)}] Nordnet {rn*100:.2f} DNB {rd*100:.2f}  N/D {rel*100:+.2f}  CC/World (USD) {idx*100:+.2f}  -> Nordnet vs own index relative to DNB {(rel-idx)*100:+.2f}")
# NAV values around month ends to check dates
for k in ["2025-09-29","2025-09-30","2025-10-01","2025-12-30","2025-12-31","2026-01-02","2026-09-29","2026-09-30","2026-10-01","2025-06-02","2025-06-03"]:
    print(k, n.get(k), d.get(k))
