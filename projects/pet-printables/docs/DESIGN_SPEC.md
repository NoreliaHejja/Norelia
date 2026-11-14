# Design Spec

The shop reads as one brand because every product shares these tokens and
components. `templates/_design-system.css` is the canonical, copy-pasteable
source; this file explains it and gives the component snippets. When in doubt,
match the two reference products in `products/examples/`.

## 1. Page geometry

```css
@page { size: 8.5in 11in; margin: 0; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page {
  width: 8.5in; height: 11in;
  padding: 0.7in 0.75in 0.8in;
  position: relative; overflow: hidden;
  page-break-after: always;
  display: flex; flex-direction: column;
  background: #fff;
}
.page:last-child { page-break-after: auto; }
```

- One `<div class="page">` per printed page.
- Content area ≈ 7.0in × 9.5in. Keep content clear of the footer (absolute, at
  `bottom: 0.42in`).

## 2. Type

- Font: `'Poppins'` (system font on the build machine; verify with
  `fc-list | grep -i poppins`).
- Headings `700`, body `300–400`.
- Page title ≈ 20pt; cover title ≈ 33pt; body ≈ 9–9.5pt; labels ≈ 8pt uppercase
  with letter-spacing.

## 3. Palette

```css
:root{
  --ink:#2f3a34;  --soft:#5f6f66; --line:#d7e0d8; --sage:#8aa893;
  --dark:#4f6b58; --tint:#eef3ec; --cream:#faf8f2; --accent:#e0a458;
  /* warm variant for keepsake/memorial products */
  --warm:#f3ede2; --warmline:#e4d9c6;
}
```

| Token | Hex | Role |
|-------|-----|------|
| ink | #2f3a34 | body text |
| soft | #5f6f66 | secondary text, captions |
| line | #d7e0d8 | borders, writing lines, rules |
| sage | #8aa893 | primary brand, table header fill, eyebrow |
| dark | #4f6b58 | headings, SVG icon stroke |
| tint | #eef3ec | card backgrounds |
| cream | #faf8f2 | zebra table rows, cover gradient base |
| accent | #e0a458 | thin accent lines, numerals, warm detail |
| warm / warmline | #f3ede2 / #e4d9c6 | beige-brown cards for keepsake products |

**Colour-variant palettes** (Thu/Fri work): blush, dusty blue, terracotta,
greige, charcoal. Keep the same *roles*; only swap the hexes. The cleanest
implementation is to lift the 8 variables into a per-variant file and include it
(see `TODO.md` → "palette swap").

## 4. Components (snippets)

### Footer (every non-cover page)
```html
<div class="footer"><span class="fp">Product Name</span><span>Page name</span></div>
```
```css
.footer{ position:absolute; left:0.75in; right:0.75in; bottom:0.42in;
  display:flex; justify-content:space-between; align-items:center;
  font-size:7.5pt; color:var(--soft); letter-spacing:.08em; text-transform:uppercase;
  border-top:1px solid var(--line); padding-top:8px; }
.footer .fp{ font-weight:600; color:var(--sage); }
```

### Page head (icon chip + eyebrow + title)
```html
<div class="pagehead">
  <div class="icon-circle"><!-- inline SVG, stroke=var(--dark) --></div>
  <div><div class="eyebrow">Section</div><h1 class="page-title">Title</h1></div>
</div>
```

### Card
```css
.card{ background:var(--tint); border:1px solid var(--line); border-radius:14px; padding:16px 18px; }
.card.warm{ background:var(--warm); border-color:var(--warmline); }   /* keepsake */
```

### Table (sage header, white text, cream zebra)
```css
thead th{ background:var(--sage); color:#fff; font-weight:600; font-size:8pt;
  text-transform:uppercase; letter-spacing:.04em; padding:9px 10px; text-align:left; }
thead th:first-child{ border-top-left-radius:10px; }
thead th:last-child{ border-top-right-radius:10px; }
tbody td{ border-bottom:1px solid var(--line); height:0.46in; padding:0 10px;
  font-size:9pt; font-weight:300; }
tbody tr:nth-child(even){ background:var(--cream); }
```

### Dashed checkbox (never filled)
```css
.chk{ width:14px; height:14px; border:1.6px dashed var(--sage); border-radius:4px;
  display:inline-block; vertical-align:middle; margin-right:7px; }
```

### Writing line / label
```css
.wline{ border-bottom:1px solid var(--line); height:0.36in; }
.lbl{ font-size:8pt; letter-spacing:.14em; text-transform:uppercase;
  color:var(--sage); font-weight:600; display:block; margin-bottom:5px; }
```

### Cover
```css
.cover{ background:linear-gradient(158deg,var(--cream) 0%, var(--tint) 100%);
  align-items:center; text-align:center; justify-content:center; padding:1in 0.9in; }
.cover .medallion{ width:2.5in; height:2.5in; border-radius:50%; background:#fff;
  border:1.5px solid var(--line); box-shadow:0 14px 36px rgba(79,107,88,.09);
  display:flex; align-items:center; justify-content:center; margin-bottom:34px; }
.accent-line{ width:70px; height:3px; background:var(--accent); border-radius:2px; }
```
The medallion holds a circular **inline SVG** paw / animal motif. Keepsake covers
use the `--cream → --warm` gradient and `--accent` motifs.

## 5. Icons

Small **inline SVG**, `viewBox="0 0 24 24"`, `fill="none"`,
`stroke="#4f6b58"` (`--dark`), `stroke-width≈1.6`, round caps/joins. Put each in a
44–46px `.icon-circle` chip. **No emoji** in any functional role (headers, labels,
list bullets). Decorative emoji are out entirely — keep the look editorial.

## 6. Print-friendliness

- No large dark fills (customer ink cost). The darkest fill is the sage table
  header; everything else is tint/cream/white.
- `print-color-adjust: exact` so backgrounds render when printed.
- Writing areas are real white space with thin `--line` rules.

## 7. Page budget

7–8 pages per product: **cover + 6–7 functional + "The Small Print."** Each
functional page is self-contained so a customer can reprint just the page they
need (e.g. a fresh daily log).
