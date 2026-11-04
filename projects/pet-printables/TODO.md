# TODO

## Done (reference builds)
- [x] **Dog Walking & Feeding Log** — 8-page US Letter PDF, verified (no overflow),
      Etsy title + 13 tags, Higgsfield cover generated. (Wed ⑤)
- [x] **Senior Dog Care Journal** — 8-page US Letter PDF, verified, Etsy title +
      13 tags, Higgsfield cover generated. (Wed ⑥)

## Outstanding products (per weekly schedule)
- [ ] **① Cat Memorial Keepsake Journal** (Mon) — warmer beige-brown variant.
- [ ] **② New Kitten Starter Kit** (Mon) — profile, vaccination log, feeding/weight,
      litter training, vet contacts, shopping list, first-week to-dos.
- [ ] **③ Pet Health & Vaccination Record Book** (Tue) — KDP-friendly logbook
      (needs its own KDP trim size + interior; not just US Letter).
- [ ] **④ Pet Sitter Instructions & Info Sheet** (Tue) — feeding, walks, meds,
      emergency contacts, habits/quirks.
- [x] **⑤ Dog Walking & Feeding Log** (Wed)
- [x] **⑥ Senior Dog Care Journal** (Wed)

## Variants & marketing (Thu/Fri work)
- [ ] Colour variants of shipped products: blush, dusty blue, terracotta, greige,
      charcoal. (Parameterise the palette — see "palette swap" idea below.)
- [ ] Etsy listing copy (title + 13 tags + description) for every product that
      doesn't have it yet.
- [ ] Listing mockup images (5 per product: hero, "what's inside", page close-ups,
      "how it works").

## Infrastructure / nice-to-haves
- [ ] Confirm and record the **Etsy store name** (fill into `CLAUDE.md`).
- [ ] Decide KDP trim sizes for logbook-style products (③) and add an A4/KDP
      render target to `render_pdf.js`.
- [ ] **Palette swap:** move the 8 palette hexes to a small JSON/CSS file per
      variant so a colour variant is a one-file change, not a rewrite.
- [ ] Automate the contact-sheet verification (render + montage) as an npm script.
- [ ] Decide how cover images are stored/named (they currently live only in the
      Higgsfield account; the cloud sandbox can't download from the CDN).
- [ ] Pinterest / social scheduling (manual for now; owner-driven).

## Known constraints
- The cloud build sandbox **cannot reach the Higgsfield CloudFront CDN**, so cover
  images can't be downloaded there — they stay in the Higgsfield gallery and are
  shared by URL (links expire ~24h). On a local machine with network access this
  isn't an issue.
