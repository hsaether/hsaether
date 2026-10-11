# consensus (Yahoo earningsTrend, 11 Oct 2026); prices 9 Oct close
fx={"NOK":1,"USD":9.5555,"EUR":10.70411}
d={ # sym: (weight%, block, price NOK, ccy, eps26, eps27, divyield fwd %)
"EQNR":(16.1,"E",417.9,"USD",5.6789,4.42852,3.54),
"AKRBP":(6.2,"E",353.7,"USD",3.52129,2.97614,7.43),
"VAR":(1.5,"E",53.2,"USD",0.73711,0.48742,10.29),
"SUBC":(4.3,"E",338.6,"USD",2.57323,2.69656,6.03),
"FRO":(2.5,"E",543.6,"USD",8.5775,5.16,18.79),
"DNB":(10.4,"F",302.4,"NOK",26.49917,28.12707,5.92),
"STB":(4.9,"F",187.9,"NOK",11.68615,13.44888,2.93),
"GJF":(2.5,"F",254.2,"NOK",15.30021,17.32513,4.04),
"KOG":(7.3,"O",295.4,"NOK",7.33323,11.40049,0.75),
"NHY":(6.7,"O",78.9,"NOK",8.62394,8.25514,3.83),
"MOWI":(5.1,"O",203.8,"EUR",1.15617,1.40604,3.77),
"TEL":(4.7,"O",124.5,"NOK",10.37406,9.32793,7.61),
"YAR":(4.2,"O",413.6,"USD",55.48273/9.5555*1.0,46.82372/9.5555,5.28),
"ORK":(3.5,"O",93.05,"NOK",6.61106,6.86423,4.31),
}
# Yara EPS on Yahoo looks NOK-denominated (55 NOK ~ 5.8 USD); check P/E both ways
tot={};
for b in "EFO": tot[b]=[0,0,0,0]
allw=0;e26=0;e27=0;dy=0
for s,(w,b,p,c,a,bb,y) in d.items():
    pe26=p/(a*fx[c]); pe27=p/(bb*fx[c])
    print(f"{s:6s} {b} w{w:5.1f} PE26 {pe26:6.1f} PE27 {pe27:6.1f} g {bb/a-1:+.1%} dy {y}")
    tot[b][0]+=w; tot[b][1]+=w/pe26; tot[b][2]+=w/pe27; tot[b][3]+=w*y
    allw+=w; e26+=w/pe26; e27+=w/pe27; dy+=w*y
print("sample weight",allw)
for b,(w,a,c,y) in tot.items():
    print(b, f"w {w:.1f} ({w/allw:.0%}) PE26 {w/a:.1f} PE27 {w/c:.1f} EPSg {c/a-1:+.1%} earnings share26 {a/e26:.0%} share27 {c/e27:.0%} dy {y/w:.2f}")
print(f"Index sample PE26 {allw/e26:.2f} PE27 {allw/e27:.2f} EPS g {e27/e26-1:+.1%} dy {dy/allw:.2f}")
