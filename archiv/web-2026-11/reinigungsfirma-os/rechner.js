// Stundensatz-Rechner – Reinigungsfirma OS
// Logik 1:1 aus dem Design: Lohn → +SV → +Ausfall → +Gemeinkosten (= Selbstkosten) → +Gewinn.
(function () {
  'use strict';

  var LAND = {
    DE: { lohn: '15.00', mwst: 19 },
    AT: { lohn: '15.12', mwst: 20 }
  };
  var land = 'DE';

  function $(id) { return document.getElementById(id); }
  function num(v) {
    var n = parseFloat(String(v).replace(',', '.'));
    return isFinite(n) ? n : 0;
  }
  function fmt(n) {
    return n.toLocaleString('de-DE', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }
  function fmt0(n) {
    return Math.round(n).toLocaleString('de-DE');
  }
  function set(id, text) { $(id).textContent = text; }

  function berechne(werte) {
    var lohn = num(werte.lohn);
    var withSv = lohn * (1 + num(werte.sv) / 100);
    var withAusfall = withSv * (1 + num(werte.ausfall) / 100);
    var selbst = withAusfall * (1 + num(werte.gk) / 100);
    var netto = selbst * (1 + num(werte.gewinn) / 100);
    var preis = num(werte.preis);
    var stunden = num(werte.stunden);
    return {
      lohn: lohn, sv: withSv - lohn, ausfall: withAusfall - withSv, gk: selbst - withAusfall,
      selbst: selbst, gewinn: netto - selbst, netto: netto,
      preis: preis, stunden: stunden, gap: netto - preis
    };
  }

  function render() {
    var ids = ['lohn', 'sv', 'ausfall', 'gk', 'gewinn', 'preis', 'stunden'];
    var werte = {};
    ids.forEach(function (id) { werte[id] = $(id).value; });
    var r = berechne(werte);
    var mwst = LAND[land].mwst;

    set('r-netto', fmt(r.netto) + ' €');
    set('r-brutto', fmt(r.netto * (1 + mwst / 100)));
    set('r-mwst', String(mwst));
    set('r-lohn', fmt(r.lohn) + ' €');
    set('r-sv', fmt(r.sv) + ' €');
    set('r-ausfall', fmt(r.ausfall) + ' €');
    set('r-gk', fmt(r.gk) + ' €');
    set('r-selbst', fmt(r.selbst) + ' €');
    set('r-gewinn', fmt(r.gewinn) + ' €');

    var under = r.preis > 0 && r.gap > 0.005;
    var ok = r.preis > 0 && r.gap <= 0.005;
    $('hinweis-tief').hidden = !under;
    $('hinweis-ok').hidden = !ok;
    if (under) {
      set('gap-hour', fmt(r.gap));
      set('gap-stunden', fmt0(r.stunden));
      set('gap-month', fmt0(r.gap * r.stunden));
      set('gap-year', fmt0(r.gap * r.stunden * 12));
    }
    if (ok) set('plus-hour', fmt(-r.gap));
  }

  function waehleLand(neu) {
    land = neu;
    $('lohn').value = LAND[neu].lohn;
    document.querySelectorAll('[data-land]').forEach(function (btn) {
      btn.setAttribute('aria-pressed', btn.getAttribute('data-land') === neu ? 'true' : 'false');
    });
    render();
  }

  if (typeof document !== 'undefined') document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.fields input').forEach(function (input) {
      input.addEventListener('input', render);
    });
    document.querySelectorAll('[data-land]').forEach(function (btn) {
      btn.addEventListener('click', function () { waehleLand(btn.getAttribute('data-land')); });
    });
    render();
  });

  // Für Tests in Node
  if (typeof module !== 'undefined') module.exports = { berechne: berechne };
})();
