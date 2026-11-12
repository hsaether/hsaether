import datetime as dt
D = dt.date

def old_inputs():
    eb = {
        "Base": {"Q4-26": 212.0, "Q1-27": 204.9, "Q2-27": 229.3, "Q3-27": 227.9, "Q4-27": 223.7, "2028": 903.9, "2029": 876.9},
        "Bear": {"Q4-26": 212.0, "Q1-27": 191.2, "Q2-27": 212.5, "Q3-27": 213.8, "Q4-27": 209.3, "2028": 737.7, "2029": 665.7},
        "Bull": {"Q4-26": 212.0, "Q1-27": 218.7, "Q2-27": 246.5, "Q3-27": 241.5, "Q4-27": 238.6, "2028": 1078.4, "2029": 1108.2},
    }
    q = lambda a, b, c, d, e, f, g: {"Q4-26": a, "Q1-27": b, "Q2-27": c, "Q3-27": d, "Q4-27": e, "2028": f, "2029": g}
    return dict(
        val_date=D(2026, 10, 27), P=134.3, fx=9.328, k=0.12,
        nibd0=1279.0, cash0=468.0,
        ebitda=eb, tax=0.095, payout=0.90, lev_cap=1.87, r_debt=0.063, r_cash=0.03, int_mode="start",
        lease=q(15, 15, 15, 15, 15, 55, 45), maint=q(40, 35, 35, 35, 35, 140, 145),
        amort=q(37, 37.5, 37.5, 37.5, 37.5, 166, 166),
        growth=q((35, 30), (42, 36), (42, 36), (37, 31), (98, 63.6), (251, 180.6), (180, 138)),
        sale={"Q2-27": 147.0},
        div_q3_26=93.6, div_q4_26=93.6,
        exit={
            "Base": dict(fleet=3063.0, firm=86.0, signed=55.0, norseman=165.0, salt=224.0, rsv=386.0, rov=135.0, services=500.0, tail=12.3),
            "Bear": dict(fleet=1812.0, firm=136.0, signed=50.3, norseman=150.0, salt=148.0, rsv=330.0, rov=135.0, services=270.0, tail=3.4),
            "Bull": dict(fleet=4576.0, firm=54.0, signed=55.5, norseman=175.0, salt=306.0, rsv=400.0, rov=135.0, services=800.0, tail=0.0),
        },
        signed_struct={"Bear": 28.0, "Base": 19.0, "Bull": 12.0},
        struct_delta={s: q(0, 0, 0, 0, 0, 0, 0) for s in ("Bear", "Base", "Bull")},
        fxpath={"Bear": {2026: 1.0, 2027: 1.12, 2028: 1.091, 2029: 1.091}, "Bull": {2026: 1.0, 2027: 0.97, 2028: 0.97, 2029: 0.97}, "Base": {}},
        use_fxpath=False,
    )
