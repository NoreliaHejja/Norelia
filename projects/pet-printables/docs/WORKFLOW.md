# Production Workflow

The checklist a run follows to produce a day's products. A run is a fresh,
memory-less session — day-of-week decides what to build (see
`PRODUCT_ROADMAP.md`).

## 0. Decide the day's work
- Determine today's weekday (Hungarian time). Pick the two products for that day.
- Thu/Fri: make a colour variant or write Etsy copy instead; if nothing to do,
  say so in one sentence and stop.

## 1. Content + layout
- Write one self-contained HTML file per product in `products/`.
- Copy the design system from `templates/_design-system.css` (inline it in the
  file). Start from `templates/base-page.html`.
- US English, warm, short sentences. Avoid trademarks.
- Required pages: cover, "Read this first", the functional pages, and
  **"The Small Print"** (personal use, AI-assisted design disclosure, not
  medical/veterinary advice, adult supervision, no physical item shipped).
- 7–8 pages total. Every page is `<div class="page">` with a footer.

## 2. Render to PDF
```bash
node scripts/render_pdf.js products/your_product.html
```
- Uses Playwright/Chromium, `page.pdf({width:'8.5in',height:'11in',printBackground:true})`.
- The script runs an **overflow check**: each `.page` must not scroll past 11in.
- **Gate:** output must say `OVERFLOW: none`. If not, tighten the page and re-render.

## 3. Verify
```bash
pdfinfo products/your_product.pdf | grep -E "Pages|Page size"   # 8 pages, 612 x 792 pts (letter)
pdftoppm -png -r 70 products/your_product.pdf prev/p
montage prev/p-*.png -tile 4x2 -geometry +6+6 -background white prev/contact.png
```
- Eyeball the contact sheet: footers correct, nothing overlaps, SVG icons render,
  writing lines aligned.
- Optional: `pdfimages -list products/your_product.pdf` (expect raster count
  matching any embedded images; our pages are vector/SVG so this may be 0).

## 4. Cover image (Higgsfield, marketing)
- **Check balance first** (`mcp__Higgsfield__balance`). If generating would drop
  below **5 credits**, skip the image and say so in the report.
- `generate_image_batch`, model `gpt_image_2_5`, `aspect_ratio '4:5'`, `count 1`
  per product (~0.25 credit each).
- Prompt: warm overhead flat-lay, home-printed plain sheets/cards, the matching
  animal (partially in frame), sage-cream palette, styled & minimal,
  **"no text, no lettering, no words anywhere."**
- `jobs_wait` (≤15s polls) → `show_generation_by_ids` to surface them.
- **Note:** the cloud sandbox can't download from the Higgsfield CDN; the image
  stays in the gallery and is shared by URL (expires ~24h). On a local machine
  with network access, download and store it with the product.

## 5. Deliver & report
- `SendUserFile` the PDFs (and cover images if downloadable).
- `SendUserMessage` per product: Etsy **title** (≤140 chars) + **8–13 tags**
  (each ≤20 chars), English, US/DACH market.
- End with a short **Hungarian** summary: what was built + the next suggested step.
- **Never** upload/post/email anything — the owner reviews and uploads herself.

## Verification gates (must all pass before delivery)
- [ ] `OVERFLOW: none`
- [ ] `pdfinfo` → 8 pages, `612 x 792 pts (letter)`
- [ ] Contact sheet looks clean (no overlaps, footers right)
- [ ] Each product has an Etsy title + 8–13 tags
- [ ] Higgsfield balance check done (image generated or explicitly skipped)
