#!/usr/bin/env node
/**
 * Render product HTML files to print-ready US Letter PDFs and check for overflow.
 *
 * Usage:
 *   node scripts/render_pdf.js products/examples/dog_walking_feeding_log.html
 *   node scripts/render_pdf.js "products/**\/*.html"      # quote globs
 *   npm run build                                          # all products/*.html
 *
 * For each input foo.html it writes foo.pdf beside it and prints an overflow
 * report. Each `.page` must fit within 11in (1056px @96dpi) or it is flagged.
 * Exit code is non-zero if any page overflows, so it can gate a build.
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// --- tiny glob (supports ** and *) so we need no extra dependency ----------
function expand(patterns) {
  const out = [];
  for (const p of patterns) {
    if (!/[*?]/.test(p)) { out.push(path.resolve(p)); continue; }
    const abs = path.resolve(p);
    const parts = abs.split(path.sep);
    const base = parts[0] || path.sep;
    walk(base === '' ? path.sep : base, parts.slice(1), out);
  }
  return [...new Set(out)];
}
function walk(dir, rest, out) {
  if (rest.length === 0) { if (fs.existsSync(dir) && fs.statSync(dir).isFile()) out.push(dir); return; }
  const [seg, ...tail] = rest;
  let entries = [];
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { return; }
  if (seg === '**') {
    walk(dir, tail, out); // ** matches zero segments
    for (const e of entries) if (e.isDirectory()) walk(path.join(dir, e.name), rest, out);
    return;
  }
  const re = new RegExp('^' + seg.replace(/[.+^${}()|[\]\\]/g, '\\$&').replace(/\*/g, '.*').replace(/\?/g, '.') + '$');
  for (const e of entries) if (re.test(e.name)) walk(path.join(dir, e.name), tail, out);
}

async function main() {
  const args = process.argv.slice(2);
  const patterns = args.length ? args : ['products/**/*.html'];
  const files = expand(patterns).filter(f => f.toLowerCase().endsWith('.html'));
  if (files.length === 0) { console.error('No HTML files matched:', patterns.join(' ')); process.exit(1); }

  const browser = await chromium.launch();
  const page = await browser.newPage();
  let anyOverflow = false;

  for (const src of files) {
    const out = src.replace(/\.html$/i, '.pdf');
    await page.goto('file://' + src, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);

    const report = await page.evaluate(() => {
      const pages = [...document.querySelectorAll('.page')];
      return pages.map((p, i) => ({
        idx: i + 1,
        over: p.scrollHeight - Math.round(p.getBoundingClientRect().height),
      }));
    });
    const overflow = report.filter(r => r.over > 1);

    await page.pdf({ path: out, width: '8.5in', height: '11in', printBackground: true });

    console.log(`\n=== ${path.basename(src)} ===  pages: ${report.length}`);
    if (overflow.length) {
      anyOverflow = true;
      console.log('OVERFLOW:', JSON.stringify(overflow));
    } else {
      console.log('OVERFLOW: none');
    }
    console.log('wrote', path.relative(process.cwd(), out));
  }

  await browser.close();
  if (anyOverflow) { console.error('\nBuild gate failed: at least one page overflows.'); process.exit(2); }
}

main().catch(e => { console.error(e); process.exit(1); });
