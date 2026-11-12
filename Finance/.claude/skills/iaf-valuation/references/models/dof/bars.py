import sys, pymupdf
pdf = sys.argv[1]; pno = int(sys.argv[2])
doc = pymupdf.open(pdf); page = doc[pno-1]
# vector drawings: list filled rectangles in the chart area
for d in page.get_drawings():
    r = d.get("rect"); fill = d.get("fill")
    if r is None: continue
    if r.width < 2 or r.height < 2: continue
    if r.x0 < 250: continue
    print(f"x0={r.x0:7.2f} x1={r.x1:7.2f} y0={r.y0:7.2f} y1={r.y1:7.2f} h={r.height:7.2f} w={r.width:6.2f} fill={fill} type={d.get('type')}")
