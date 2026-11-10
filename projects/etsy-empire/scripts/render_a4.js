#!/usr/bin/env node
// US Letter-re tervezett termék HTML → A4 PDF (97%-os méretezés, oldalanként egy A4).
// Használat: node scripts/render_a4.js termekek/<slug>/<slug>.html  → <slug>-A4.pdf
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const src = path.resolve(process.argv[2]);
  const out = src.replace(/\.html$/i, '-A4.pdf');
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + src, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.addStyleTag({ content: '@page{size:A4;margin:0} .page{margin:0 auto}' });
  await p.pdf({ path: out, format: 'A4', scale: 0.97, printBackground: true, preferCSSPageSize: true });
  await b.close(); console.log('wrote', path.relative(process.cwd(), out));
})();
