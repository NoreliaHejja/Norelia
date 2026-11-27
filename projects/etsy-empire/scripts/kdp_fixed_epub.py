#!/usr/bin/env python3
"""Fix elrendezésű (pre-paginated) EPUB3 Kindle-re oldalkép-alapú PDF-ből – az oldalak NEM fordulnak fekvőbe
(rendition:orientation = portrait, rendition:spread = none). KDP elfogadja (Kindle e-book manuscript: EPUB).
   python3 scripts/kdp_fixed_epub.py <interior.pdf> <kimenet.epub> "Cím" "Szerző" [borító.jpg] [nyelv=en]"""
import sys, subprocess, tempfile, zipfile, uuid, datetime
from pathlib import Path
from PIL import Image
src, out, title, author = sys.argv[1], Path(sys.argv[2]), sys.argv[3], sys.argv[4]
cover = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else None
lang = sys.argv[6] if len(sys.argv) > 6 else "en"
W = 1200  # szélesség px (méret/letöltési díj kímélése); magasság az oldalarányból
with tempfile.TemporaryDirectory() as t:
    subprocess.run(["pdftoppm", "-r", "150", "-png", src, f"{t}/p"], check=True)
    pages = sorted(Path(t).glob("p-*.png"))
    imgs = []
    for i, p in enumerate(pages, 1):
        im = Image.open(p); im = im.convert("L") if im.mode in ("L", "LA", "1") or all(e == im.getextrema()[0] for e in im.getextrema()[:1]) else im.convert("RGB")
        H = round(W * im.height / im.width); im = im.resize((W, H), Image.LANCZOS)
        name = f"p{i:03d}.jpg"; buf = Path(t) / name; im.save(buf, quality=80, optimize=True); imgs.append((name, buf.read_bytes()))
    if cover:
        c = Image.open(cover).convert("RGB"); cb = Path(t) / "cover.jpg"; c.save(cb, quality=88); cover_bytes = cb.read_bytes()
    uid = f"urn:uuid:{uuid.uuid4()}"; now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    css = f"html,body{{margin:0;padding:0;width:{W}px;height:{H}px}} img{{display:block;width:{W}px;height:{H}px}}"
    def page(n): return (f'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{lang}">'
                         f'<head><title>{title}</title><meta name="viewport" content="width={W}, height={H}"/><link rel="stylesheet" href="s.css"/></head>'
                         f'<body><img src="{n}" alt="Page"/></body></html>')
    manifest = ['<item id="css" href="s.css" media-type="text/css"/>', '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>']
    spine = []
    if cover:
        manifest.append('<item id="cimg" href="cover.jpg" media-type="image/jpeg" properties="cover-image"/>')
        manifest.append('<item id="cpage" href="cover.xhtml" media-type="application/xhtml+xml"/>'); spine.append('<itemref idref="cpage"/>')
    for i, (n, _) in enumerate(imgs, 1):
        manifest.append(f'<item id="i{i}" href="{n}" media-type="image/jpeg"/>')
        manifest.append(f'<item id="x{i}" href="p{i:03d}.xhtml" media-type="application/xhtml+xml"/>'); spine.append(f'<itemref idref="x{i}"/>')
    opf = (f'<?xml version="1.0" encoding="UTF-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bid" prefix="rendition: http://www.idpf.org/vocab/rendition/#">'
           f'<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="bid">{uid}</dc:identifier><dc:title>{title}</dc:title><dc:creator>{author}</dc:creator><dc:language>{lang}</dc:language>'
           f'<meta property="dcterms:modified">{now}</meta><meta property="rendition:layout">pre-paginated</meta><meta property="rendition:orientation">portrait</meta><meta property="rendition:spread">none</meta>'
           + ('<meta name="cover" content="cimg"/>' if cover else '') +
           f'<meta name="original-resolution" content="{W}x{H}"/><meta name="fixed-layout" content="true"/><meta name="orientation-lock" content="portrait"/><meta name="book-type" content="children"/></metadata>'
           f'<manifest>{"".join(manifest)}</manifest><spine>{"".join(spine)}</spine></package>')
    nav = (f'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"><head><title>{title}</title></head><body>'
           f'<nav epub:type="toc"><ol><li><a href="p001.xhtml">{title}</a></li></ol></nav></body></html>')
    with zipfile.ZipFile(out, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>', compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED); z.writestr("OEBPS/nav.xhtml", nav, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/s.css", css, compress_type=zipfile.ZIP_DEFLATED)
        if cover:
            z.writestr("OEBPS/cover.jpg", cover_bytes); z.writestr("OEBPS/cover.xhtml", page("cover.jpg"), compress_type=zipfile.ZIP_DEFLATED)
        for i, (n, b) in enumerate(imgs, 1):
            z.writestr(f"OEBPS/{n}", b); z.writestr(f"OEBPS/p{i:03d}.xhtml", page(n), compress_type=zipfile.ZIP_DEFLATED)
print(f"OK {out} · {len(imgs)} oldal · {W}x{H}px · {out.stat().st_size/1e6:.1f} MB")
