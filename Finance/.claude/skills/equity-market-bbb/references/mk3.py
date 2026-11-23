s = open('world2.py', encoding='utf-8').read()
R = [
 ("# Equity BBB Update 2 (6 Nov 2026; skill 2026-10-24.1)",
  "# Equity BBB 20 Nov 2026 leading-view note (skill 2026-11-18.1): world2.py (6 Nov) re-priced to the 20 Nov close with the company analyses\n"
  "# of 19-20 Nov (MSFT v3.2, GOOGL v2.2, NVDA v2.0, AMZN v2.1, MU v4 at $594.51), AI BBB 18 Nov rows (H1 .92/.85/.82/.81, H4 .95/.94/.94/.99,\n"
  "# E cash conversion -.20/.11/.36), Oil BBB 18 Nov Base 80/73/72/70, HY BBB 18 Nov NIBOR market path, stub 41 days. Needs dl2/recent_1120.json.\n"
  "# Was: Equity BBB Update 2 (6 Nov 2026; skill 2026-10-24.1)"),
 ("M.STUB = STUB = 55/365", "M.STUB = STUB = 41/365"),
 ("NIB = (4.80, 4.79, 4.39, 3.86)", "NIB = (4.80, 4.79, 4.78, 4.58)"),
 ('RC = json.load(open("dl2/recent_1105.json"))', 'RC = json.load(open("dl2/recent_1105.json")); RC20 = json.load(open("dl2/recent_1120.json"))'),
 ("EU5 = 1.1235", "EU5 = 1.0974539518356323; D20 = '2026-11-20'"),
 ('P5 = {n: RC[n]["2026-11-05"] for n in', 'P5 = {n: RC20[n][D20] for n in'),
 ("P5[\"SAP\"] = 215.75*EU5", "P5[\"SAP\"] = RC20['SAP.DE'][D20]*EU5"),
 ("MOVE = {n: P5[n]/RC[n][\"2026-11-04\"] for n in P5 if n != \"SAP\"}", "MOVE = {n: P5[n]/RC[n][\"2026-11-04\"] for n in P5 if n != \"SAP\"}"),
 ("MOVE[\"SAP\"] = (215.75/214.30)*(EU5/1.1207)", "MOVE[\"SAP\"] = (RC20['SAP.DE'][D20]/214.30)*(EU5/1.1207)"),
 ("R_URTH = RC[\"URTH\"][\"2026-11-05\"]/RC[\"URTH\"][\"2026-11-04\"]", "R_URTH = RC20[\"URTH\"][D20]/RC[\"URTH\"][\"2026-11-04\"]"),
 ("(RC[\"IXC\"][\"2026-11-05\"]/RC[\"IXC\"][\"2026-11-04\"])/R_URTH", "(RC20[\"IXC\"][D20]/RC[\"IXC\"][\"2026-11-04\"])/R_URTH"),
 ("EN_PE = 14.8*RC[\"IXC\"][\"2026-11-05\"]/59.88", "EN_PE = 14.8*RC20[\"IXC\"][D20]/59.88"),
 ("M.CONV[\"E\"] = dict(Bear=(-.10, .30, .50), Base=(-.20, .00, .20), Bull=(-.30, -.20, .00))",
  "M.CONV[\"E\"] = dict(Bear=(-.10, .30, .50), Base=(-.20, .11, .36), Bull=(-.30, -.20, .00))\n"
  "M.AI[\"H1\"] = (dict(M.AI[\"H1\"][0], Base=(.92, .85, .82, .81)),) + tuple(M.AI[\"H1\"][1:])\n"
  "M.AI[\"H4\"] = (dict(M.AI[\"H4\"][0], Base=(.95, .94, .94, .99)),) + tuple(M.AI[\"H4\"][1:])"),
 ("def set_energy(b27=88,", "def set_energy(b27=80,"),
 ("Bb = [b27+dB, 77+dB, 72+dB, 70+dB]", "Bb = [b27+dB, 73+dB, 72+dB, 70+dB]"),
 (""" "CM": dict(names=["MSFT"], cons=22.08, stub=0.98, p_an=531.01, e27=20.77,
            V=dict(Bear=(337.7, 368.8, 404.5), Base=(585.8, 643.2, 692.1), Bull=(681.6, 806.0, 921.4)),""",
  """ "CM": dict(names=["MSFT"], cons=22.11, stub=0.0, p_an=498.30, e27=20.77,
            V=dict(Bear=(337.7, 368.8, 404.3), Base=(561.1, 629.5, 692.1), Bull=(654.0, 790.0, 921.4)),"""),
 (""" "CG": dict(names=["GOOGL", "GOOG"], cons=14.84, stub=0.22, p_an=279.84, e27=12.66,
            V=dict(Bear=(160.1, 179.0, 202.6), Base=(306.6, 337.9, 371.1), Bull=(373.0, 439.3, 515.9)),
            D=dict(Bear=(0.88, 0.88, 0.88), Base=(0.91, 0.96, 1.01), Bull=(0.95, 1.04, 1.14)),
            EPS=dict(Bear=(10.46, 9.82, 11.00, 12.33), Base=(12.66, 14.28, 15.89, 17.44), Bull=(13.80, 16.66, 18.97, 21.39))),""",
  """ "CG": dict(names=["GOOGL", "GOOG"], cons=14.91, stub=0.22, p_an=272.66, e27=12.64,
            V=dict(Bear=(160.6, 179.5, 203.0), Base=(301.7, 335.8, 372.9), Bull=(367.3, 437.4, 518.9)),
            D=dict(Bear=(0.88, 0.88, 0.88), Base=(0.91, 0.96, 1.01), Bull=(0.95, 1.04, 1.14)),
            EPS=dict(Bear=(10.44, 9.80, 10.98, 12.31), Base=(12.64, 14.26, 15.87, 17.42), Bull=(13.78, 16.64, 18.95, 21.37))),"""),
 (""" "CN": dict(names=["NVDA"], cons=15.21, stub=0.56, p_an=181.60, e27=13.99,
            V=dict(Bear=(106.7, 116.0, 126.9), Base=(220.8, 253.3, 274.1), Bull=(269.5, 339.6, 402.6)),
            D=dict(Bear=(5.12, 4.92, 4.43), Base=(6.59, 8.46, 8.81), Bull=(7.00, 9.59, 10.70)),
            EPS=dict(Bear=(10.34, 7.61, 8.06, 8.67), Base=(13.99, 14.91, 15.21, 14.75), Bull=(15.21, 17.49, 19.01, 19.77))),""",
  """ "CN": dict(names=["NVDA"], cons=15.21, stub=0.81, p_an=125.53, e27=13.99,
            V=dict(Bear=(103.9, 111.4, 119.9), Base=(147.5, 171.8, 196.4), Bull=(219.8, 308.0, 392.6)),
            D=dict(Bear=(6.72, 6.25, 5.77), Base=(6.71, 7.32, 6.78), Bull=(9.07, 12.67, 14.13)),
            EPS=dict(Bear=(10.34, 7.61, 8.06, 8.67), Base=(13.99, 12.93, 12.47, 12.32), Bull=(15.21, 17.49, 19.01, 19.77))),"""),
 (""" "CA": dict(names=["AMZN"], cons=10.65, stub=0.0, p_an=240.35, e27=9.69,
            V=dict(Bear=(105.9, 119.6, 141.4), Base=(267.2, 292.0, 317.3), Bull=(316.9, 371.0, 432.1)),""",
  """ "CA": dict(names=["AMZN"], cons=10.66, stub=0.0, p_an=257.37, e27=9.69,
            V=dict(Bear=(109.5, 123.2, 144.9), Base=(282.0, 303.4, 324.3), Bull=(334.1, 385.6, 442.6)),"""),
 (""" "CU": dict(names=["MU"], cons=191.80, stub=0.0, p_an=656.39, e27=172.6,
            V=dict(Bear=(512.6, 435.9, 435.9), Base=(697.0, 650.5, 723.6), Bull=(928.4, 933.5, 1001.8)),
            D=dict(Bear=(115.2, 43.6, 33.6), Base=(158.4, 77.7, 45.8), Bull=(171.1, 107.3, 58.9)),
            EPS=dict(Bear=(115.1, 57.5, 48.0, 48.0), Base=(172.6, 115.1, 76.7, 67.1), Bull=(191.8, 153.4, 105.5, 86.3)))}""",
  """ "CU": dict(names=["MU"], cons=191.80, stub=0.0, p_an=594.51, e27=172.6,
            V=dict(Bear=(512.5, 435.8, 435.8), Base=(565.0, 523.2, 589.3), Bull=(892.9, 921.4, 1001.6)),
            D=dict(Bear=(115.2, 43.6, 33.6), Base=(158.3, 61.1, 29.8), Bull=(171.0, 107.3, 58.9)),
            EPS=dict(Bear=(115.1, 57.5, 48.0, 48.0), Base=(172.6, 95.9, 61.4, 53.7), Bull=(191.8, 153.4, 105.5, 86.3)))}"""),
 ("S_UNIT = 209.14/199.63", "S_UNIT = 209.14/RC20['URTH'][D20]"),
 ("FPE0 = 17.38*199.63/204.64; PB0 = 4.06*199.63/204.64", "FPE0 = 17.38*RC20['URTH'][D20]/204.64; PB0 = 4.06*RC20['URTH'][D20]/204.64"),
 ("URTH_NOK = 199.63*9.2944", "URTH_NOK = RC20['URTH'][D20]*RC20['NOK=X'][D20]"),
 ('print(f"World 5 Nov:', 'print(f"World 20 Nov:'),
 ("(\"Base=7.2% (HY market Base)\", lambda p: world(dp=p)[0]['Base']['irr'], 0.072)", "(\"Base=7.5% (HY market Base)\", lambda p: world(dp=p)[0]['Base']['irr'], 0.075)"),
 ("URTH USD {199.63*(1+p):.1f}", "URTH USD {RC20['URTH'][D20]*(1+p):.1f}"),
]
bad = []
for a, b in R:
    if a == b: continue
    n = s.count(a)
    if n != 1: bad.append((n, a[:70])); continue
    s = s.replace(a, b)
open('world3.py', 'w', encoding='utf-8').write(s)
print('bad', bad)
