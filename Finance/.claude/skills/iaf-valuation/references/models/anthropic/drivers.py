"""Anthropic (ANT) - driver breakdown Base -> Bear / Bull, one driver at a time, at $74.
docs/anthropic-analysis.md v1.0, 13 Nov 2026. Imports model.py. Run: py drivers.py"""
from model import build, SC

B = SC["Base"]


def steps(target):
    t = SC[target]
    seq = [
        ("revenue: E1 path x share", dict(E1src=target, share=t["share"], g=t["g"])),
        ("+ window costs (compute, opex, capex, rate)", dict(compute=t["compute"], other=t["other"], capex=t["capex"],
                                                            r=t["r"], need=t["need"])),
        ("+ normalised 2030 margin", dict(c_norm=t["c_norm"], o_norm=t["o_norm"], sbc_norm=t["sbc_norm"])),
        ("+ exit P/E", dict(pe=t["pe"])),
        ("+ commitment overhang terms", dict(takedown=t["takedown"], resale=t["resale"], tail_years=t["tail_years"],
                                             shield=t["shield"], lr_growth=t["lr_growth"])),
    ]
    ov = {}
    print(f"Base -> {target}: Base {build('Base', 74)['irr']:.1%}")
    for lab, o in seq:
        o = dict(o)
        src = o.pop("E1src", None)
        ov.update(o)
        if src:
            ov["_E1"] = src
        r = run(ov)
        print(f"  {lab}: IRR {r['irr']:.1%}, V_T {r['VT']:.1f}")


def run(ov):
    import model
    o = dict(ov)
    src = o.pop("_E1", "Base")
    saved = model.E1["Base"]
    model.E1["Base"] = model.E1[src]
    try:
        return build("Base", 74, **o)
    finally:
        model.E1["Base"] = saved


if __name__ == "__main__":
    steps("Bear")
    steps("Bull")
