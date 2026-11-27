# CLAUDE.md — Pet Printables production pipeline

This file is the operating context for Claude Code working in this repo. Read it
first. It defines what we build, the exact design system, the build pipeline, and
the rules that keep the whole shop visually consistent.

> **Owner:** Pócz-Héjja Nóra (egyéni vállalkozó).
> **Business:** a dog/cat themed family of **printable digital products** sold on
> **Etsy** and **Amazon KDP**.
> **Store name:** _TBD — fill in once the Etsy shop name is confirmed._
> **Working language of the products:** US English. Reports to the owner: Hungarian.

---

## 1. What this repo produces

Each product is a **print-ready, 7–8 page PDF** that the customer downloads,
prints at home on a regular printer, and reuses (a log, journal, tracker, or
record book). Nothing is physically shipped.

The pipeline is:

```
content + layout (one HTML file per product)
        │
        ▼  Playwright → Chromium → page.pdf()
print-ready PDF (US Letter, 8.5 × 11 in)
        │
        ▼  (marketing) Higgsfield gpt_image_2_5
one 4:5 cover / flat-lay image per product
        │
        ▼  Etsy title + 13 tags (hand-written, see docs/ETSY_LISTINGS.md)
owner reviews → owner uploads to Etsy / KDP (never automated)
```

**Hard rule:** this pipeline only produces files and hands them to the owner for
review. It never emails, posts, or uploads anything on her behalf. The owner does
every upload herself.

---

## 2. Daily cadence (this is a scheduled, memory-less routine)

A scheduled task fires once per day. **Each run is a fresh session with no memory
of previous runs**, so products are pinned to the **day of the week** to avoid
overlap. Hungarian day names in parentheses.

| Day            | Build                                                                 |
| -------------- | --------------------------------------------------------------------- |
| Monday (Hétfő) | ① Cat Memorial Keepsake Journal · ② New Kitten Starter Kit            |
| Tuesday (Kedd) | ③ Pet Health & Vaccination Record Book (KDP-friendly logbook) · ④ Pet Sitter Instructions & Info Sheet |
| Wednesday (Szerda) | ⑤ Dog Walking & Feeding Log (habit-tracker style) · ⑥ Senior Dog Care Journal |
| Thursday / Friday | **No new products.** Instead: make a new **colour variant** of an existing product (blush, dusty blue, terracotta, greige, or charcoal palette), **or** write Etsy titles + keywords for earlier products. If there's nothing to do, say so in one sentence. |

See `docs/PRODUCT_ROADMAP.md` for the full list, each product's page plan, and
current status.

---

## 3. Design system — follow it exactly

Consistency across the shop matters more than per-product creativity. Every page
of every product uses the same tokens, type, and components. The canonical,
copy-pasteable stylesheet lives in `templates/_design-system.css`.

### Page
- **Size:** 8.5 × 11 in (US Letter). `@page { size: 8.5in 11in; margin: 0; }`
- `.page` is `8.5in × 11in`, `padding: 0.7in 0.75in 0.8in`.
- Each page is one `<div class="page">`; `page-break-after: always`.
- **Footer** on every non-cover page: product name bottom-left, page name
  bottom-right, thin top border.

### Type
- **Font:** `'Poppins'` (installed on the build machine as a system font).
- Headings `700`; body `300–400`.

### Palette (CSS variables)
| Token      | Hex       | Use                                    |
| ---------- | --------- | -------------------------------------- |
| `--ink`    | `#2f3a34` | body text                              |
| `--soft`   | `#5f6f66` | secondary text                         |
| `--line`   | `#d7e0d8` | borders, rules, writing lines          |
| `--sage`   | `#8aa893` | primary brand colour, table headers    |
| `--dark`   | `#4f6b58` | headings, icons                        |
| `--tint`   | `#eef3ec` | faint card backgrounds                 |
| `--cream`  | `#faf8f2` | zebra rows, cover base                 |
| `--accent` | `#e0a458` | warm accent (lines, numerals)          |

For keepsake / memorial products a **warmer beige-brown variant** is allowed
(`--warm #f3ede2`, `--warmline #e4d9c6`), used on the Senior Dog Care Journal.

### Style rules
- Clean, generous white space.
- Rounded corners: `border-radius: 10–16px`.
- Faint `--tint` background cards.
- Tables: `--sage` header row, **white** header text, zebra rows in `--cream`.
- Checkboxes: **dashed** outline (`1.6px dashed var(--sage)`), never filled.
- Icons: small **inline SVG**, stroke-based, in `--dark`. **No emoji** anywhere
  functional.
- **Printer-friendly:** no large dark fills (saves customer ink).
- **Cover:** soft linear gradient `--cream → --tint`, a circular SVG medallion
  with a paw/animal motif, a thin `--accent` line, title in `--dark`.

Full spec with rationale and component snippets: `docs/DESIGN_SPEC.md`.

---

## 4. Build pipeline

### Prerequisites (already true on the standard build machine)
- Node + Playwright with Chromium preinstalled (`require('playwright')` works).
- Poppins font installed system-wide (`fc-list | grep -i poppins`).
- `pdftoppm` / `pdfinfo` (poppler) and ImageMagick `montage` for verification.

### Steps
1. **Write the HTML** — one self-contained file per product in `products/`
   (inline CSS; copy the design system from `templates/_design-system.css`).
   Every page is a `<div class="page">`. 7–8 pages: cover + 6–7 functional +
   "The Small Print".
2. **Render to PDF** with `scripts/render_pdf.js`:
   `page.pdf({ width: '8.5in', height: '11in', printBackground: true })`.
   The script also runs an **overflow check** (each `.page` must not scroll past
   11in) and must report `OVERFLOW: none`.
3. **Verify:** `pdfinfo` → 8 pages, page size `612 × 792 pts (letter)`; render a
   `pdftoppm` + `montage` contact sheet and eyeball it (images not overlapping
   text, footers correct).
4. **Cover image (marketing):** one Higgsfield image per product —
   `generate_image_batch`, model `gpt_image_2_5`, `aspect_ratio '4:5'`,
   `count 1`. Warm overhead flat-lay, home-printed sheets/cards, the matching
   animal, sage-cream palette, **"no text, no lettering"**. **Check the Higgsfield
   balance first; if generating would drop it below 5 credits, skip the image and
   say so.** (~0.25 credit each at low quality.)
5. **Deliver:** `SendUserFile` the PDFs; `SendUserMessage` the Etsy title +
   8–13 keywords per product; end with a short Hungarian summary + next step.

See `docs/WORKFLOW.md` for the full checklist.

---

## 5. Repo layout

```
.
├── CLAUDE.md                  ← you are here
├── README.md                  ← human-facing overview
├── TODO.md                    ← outstanding work
├── package.json               ← playwright dependency + npm scripts
├── .gitignore
├── docs/
│   ├── DESIGN_SPEC.md         ← full design system + component snippets
│   ├── PRODUCT_ROADMAP.md     ← the weekly list, page plans, status
│   ├── WORKFLOW.md            ← step-by-step production checklist
│   └── ETSY_LISTINGS.md       ← finished titles + tags, naming conventions
├── scripts/
│   └── render_pdf.js          ← Playwright HTML→PDF renderer + overflow check
├── templates/
│   ├── _design-system.css     ← canonical tokens + components (source of truth)
│   └── base-page.html         ← minimal skeleton to start a new product
└── products/
    └── examples/
        ├── dog_walking_feeding_log.html   ← reference build (Wed ⑤)
        └── senior_dog_care_journal.html   ← reference build (Wed ⑥)
```

---

## 6. Conventions & guardrails

- **Avoid trademarks** in copy and titles. (e.g. never "Elf on the Shelf" →
  "Kindness Elf"; don't imply any official brand.)
- Every product ends with a **"The Small Print"** page: personal-use licence,
  AI-assisted design disclosure, "not veterinary/medical advice," adult
  supervision, "no physical item will be shipped."
- **US Letter is the required format** for the Etsy printables. Add an A4 variant
  only if a product explicitly needs it (e.g. a KDP logbook has its own trim).
- Output file names: `Product_Name_US_Letter.pdf` (underscores, Title_Case).
- Keep each run's working files in the session scratchpad; deliver finals with
  `SendUserFile`.
- Nothing ships automatically — **owner reviews and uploads.**

## 7. Commands

```bash
npm install            # one-time: installs playwright (chromium already present)
npm run build          # render every products/*.html to products/*.pdf
node scripts/render_pdf.js products/examples/dog_walking_feeding_log.html
```

(See `package.json`; `render_pdf.js` accepts explicit file paths or globs.)
