# Pet Printables

A production pipeline for a family of **dog/cat themed printable digital
products** sold on **Etsy** and **Amazon KDP** (logs, journals, trackers, record
books). Each product is a print-ready 7–8 page PDF that customers print at home
and reuse.

Owner: Pócz-Héjja Nóra (egyéni vállalkozó). The pipeline produces files for the
owner to review; **she does all uploads herself** — nothing is published
automatically.

## How it works

1. A product is one self-contained HTML file (one `<div class="page">` per page)
   that follows the shared design system in `templates/_design-system.css`.
2. `scripts/render_pdf.js` renders it to a US Letter PDF with Playwright/Chromium
   and checks for layout overflow.
3. A marketing cover image is generated with Higgsfield (`gpt_image_2_5`, 4:5,
   no text).
4. Etsy title + 13 tags are written per product (see `docs/ETSY_LISTINGS.md`).

New to the repo? Read, in order: **`CLAUDE.md`** → `docs/DESIGN_SPEC.md` →
`docs/WORKFLOW.md` → `docs/PRODUCT_ROADMAP.md`.

## Quick start

```bash
npm install
npm run build        # renders products/*.html → products/*.pdf
```

Requires Node, Playwright (Chromium), the Poppins font installed system-wide, and
poppler (`pdfinfo`, `pdftoppm`) + ImageMagick (`montage`) for verification.

## Status

Two reference products are built and shippable (Wednesday's set): the
**Dog Walking & Feeding Log** and the **Senior Dog Care Journal**. See `TODO.md`
for what's next.
