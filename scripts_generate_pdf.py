from pathlib import Path
import re

readme = Path('README.md').read_text(encoding='utf-8')
# Replace HTML img tags by explicit URL lines
readme = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', r'\n[Imagem] \1\n', readme)
# remove remaining HTML tags
readme = re.sub(r'<[^>]+>', '', readme)

lines = []
for raw in readme.splitlines():
    line = raw.rstrip()
    if not line:
        lines.append('')
        continue
    # basic wrapping
    while len(line) > 95:
        cut = line.rfind(' ', 0, 95)
        if cut <= 0:
            cut = 95
        lines.append(line[:cut])
        line = line[cut:].lstrip()
    lines.append(line)

# Minimal PDF writer (Helvetica)
objects = []

def add_obj(data: bytes):
    objects.append(data)
    return len(objects)

font_id = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

page_w, page_h = 595, 842
margin_x, margin_y = 40, 40
line_h = 14
usable_h = page_h - margin_y*2
lines_per_page = usable_h // line_h
pages = [lines[i:i+lines_per_page] for i in range(0, len(lines), lines_per_page)]

page_ids = []
content_ids = []

for p in pages:
    content_parts = [b"BT\n/F1 10 Tf\n"]
    y = page_h - margin_y
    for line in p:
        text = line.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
        content_parts.append(f"1 0 0 1 {margin_x} {y} Tm ({text}) Tj\n".encode('latin-1', errors='replace'))
        y -= line_h
    content_parts.append(b"ET\n")
    stream = b''.join(content_parts)
    c_id = add_obj(f"<< /Length {len(stream)} >>\nstream\n".encode()+stream+b"endstream")
    content_ids.append(c_id)
    p_id = add_obj(b"")
    page_ids.append(p_id)

pages_kids = ' '.join(f"{pid} 0 R" for pid in page_ids)
pages_id = add_obj(f"<< /Type /Pages /Kids [{pages_kids}] /Count {len(page_ids)} >>".encode())

for idx, pid in enumerate(page_ids):
    page_obj = f"<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 {page_w} {page_h}] /Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {content_ids[idx]} 0 R >>".encode()
    objects[pid-1] = page_obj

catalog_id = add_obj(f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode())

# write xref
pdf = bytearray(b"%PDF-1.4\n")
offsets = [0]
for i, obj in enumerate(objects, start=1):
    offsets.append(len(pdf))
    pdf += f"{i} 0 obj\n".encode() + obj + b"\nendobj\n"

xref_pos = len(pdf)
pdf += f"xref\n0 {len(objects)+1}\n".encode()
pdf += b"0000000000 65535 f \n"
for off in offsets[1:]:
    pdf += f"{off:010d} 00000 n \n".encode()
pdf += f"trailer\n<< /Size {len(objects)+1} /Root {catalog_id} 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode()

Path('README_docSales.pdf').write_bytes(pdf)
print('Gerado README_docSales.pdf com', len(pages), 'paginas')
