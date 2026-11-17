#!/usr/bin/env python3
"""KDP keménytáblás (case laminate) borító egy Gentle-könyvhöz (2026-11-17).

  python3 scripts/hardcover_cover.py books/<slug> <KDP_szelesseg_in> <KDP_magassag_in>

A teljes méretet a KDP adja (hibaüzenet „Your expected cover size is W x H”, vagy a KDP Cover Calculator).
Ebből: ráhajtás (wrap) = (H - trim_h) / 2 minden oldalon, gerinc = W - 2*trim_w - 2*wrap.
Biztonság: szöveg ≥ wrap + 0,5 in a lap szélétől, és ≥ 0,4 in (zsanér) + 0,25 in a gerinctől.
Kimenet: books/<slug>/out/cover-hardcover.pdf (+ előnézet).
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
DPI = 300
FX = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
FB = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
FR = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"


def main(folder, Win, Hin):
    folder = ROOT / folder if not Path(folder).is_absolute() else Path(folder)
    b = json.loads((folder / "book.json").read_text())
    TW, TH = b.get("trim", [6, 9])
    Win, Hin = float(Win), float(Hin)
    wrap_in = (Hin - TH) / 2
    spine = Win - 2 * TW - 2 * wrap_in
    assert 0 < spine < 3 and 0.3 < wrap_in < 1, f"furcsa méret: wrap {wrap_in:.3f}, gerinc {spine:.3f}"
    W, H = round(Win * DPI), round(Hin * DPI)
    color = b["color"]
    img = Image.new("RGB", (W, H), color); d = ImageDraw.Draw(img)
    sx0 = round((wrap_in + TW) * DPI); sx1 = round((wrap_in + TW + spine) * DPI)  # gerinc
    # elülső kép: a gerinc után a lap jobb széléig (a ráhajtásra is kifut)
    fx0 = sx1; fw = W - fx0
    a = Image.open(folder / "img" / "cover.png").convert("RGB"); r = max(fw / a.width, H / a.height)
    a = a.resize((int(a.width * r), int(a.height * r)), Image.LANCZOS)
    a = a.crop(((a.width - fw) // 2, (a.height - H) // 2, (a.width - fw) // 2 + fw, (a.height - H) // 2 + H))
    img.paste(a, (fx0, 0))

    def wrapt(text, font, maxw):
        o, c = [], ""
        for w in text.split():
            t = (c + " " + w).strip()
            if d.textlength(t, font=font) <= maxw: c = t
            else: o.append(c); c = w
        return o + [c]

    edge = int((wrap_in + 0.5) * DPI)          # külső szélektől
    hinge = int((0.4 + 0.25) * DPI)            # gerinctől
    bx0, bx1 = fx0 + hinge, W - edge
    ft = ImageFont.truetype(FX, 150); tl = wrapt(b["title"], ft, bx1 - bx0 - 100)
    fs = ImageFont.truetype(FB, 54); sl = wrapt(b.get("cover_sub", b["subtitle"]), fs, bx1 - bx0 - 120)
    bh = 70 + len(tl) * 170 + len(sl) * 72 + 50
    ty0 = edge
    d.rounded_rectangle((bx0, ty0, bx1, ty0 + bh), 50, fill=(255, 252, 245))
    y = ty0 + 55
    for t in tl: d.text(((bx0 + bx1) // 2, y), t, font=ft, fill="#1F2A44", anchor="ma"); y += 170
    for t in sl: d.text(((bx0 + bx1) // 2, y), t, font=fs, fill=color, anchor="ma"); y += 72
    cx = (bx0 + bx1) // 2
    ab1 = H - edge; ab0 = ab1 - int(.45 * DPI)
    d.rounded_rectangle((cx - 560, ab0, cx + 560, ab1), 40, fill=(255, 252, 245))
    d.text((cx, (ab0 + ab1) // 2), b["author"].upper(), font=ImageFont.truetype(FB, 70), fill="#1F2A44", anchor="mm")
    # hátsó borító szövege
    bxl, bxr = edge, sx0 - hinge
    y = edge + int(.2 * DPI); fr = ImageFont.truetype(FR, 46)
    for para in b["back"].split("|"):
        for t in wrapt(para, fr, bxr - bxl): d.text((bxl, y), t, font=fr, fill="white"); y += 66
        y += 30
    # vonalkód-hely: 2 x 1,2 in, a hátsó panel jobb alsó sarkában, a biztonsági sávon belül
    bxe, bye = sx0 - hinge, H - edge
    assert y < bye - int(1.2 * DPI) - 30, "HIBA: a hátsó szöveg belelóg a vonalkód-területbe"
    d.rectangle((bxe - int(2 * DPI), bye - int(1.2 * DPI), bxe, bye), fill="white")
    od = folder / "out"
    img.save(od / "cover-hardcover.pdf", "PDF", resolution=W / Win)  # pontosan a KDP által kért méret
    img.resize((W // 6, H // 6)).save(od / "cover-hardcover-preview.jpg", quality=85)
    print(od / "cover-hardcover.pdf", f"{W/DPI:.3f} x {H/DPI:.3f} in, ráhajtás {wrap_in:.4f}, gerinc {spine:.4f} in")


if __name__ == "__main__":
    main(*sys.argv[1:4])
