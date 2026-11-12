import sys, fitz
pdf, out = sys.argv[1], sys.argv[2]
pages = [int(x) for x in sys.argv[3].split(",")]
doc = fitz.open(pdf)
for p in pages:
    pix = doc[p-1].get_pixmap(dpi=110)
    pix.save(f"{out}/p{p}.png")
print(doc.page_count)
