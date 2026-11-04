#!/usr/bin/env python3
"""Generates the sellable lead product: Kalkulations-Kit für Reinigungsfirmen (29 €).

Output: products/Kalkulations-Kit_Reinigungsfirma_v1.0.xlsx
Sheets: Start · Stundensatz · Leistungswerte · Objektkalkulation · Angebot

After building, ALWAYS recalculate and check for formula errors (LibreOffice), e.g.:
    python3 <xlsx-skill>/scripts/recalc.py products/Kalkulations-Kit_Reinigungsfirma_v1.0.xlsx 60
Expected with the example values: Mindest-Stundensatz netto 29,75 €/h;
example office 360 m² -> Monatspreis netto 1.046,71 € (2,91 €/m²).

Rules: German UI text, Arial, inputs = yellow fill + blue font, formulas black,
cross-sheet links green. Only Excel-2007-era functions (Google Sheets compatible).
"""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "products" / "Kalkulations-Kit_Reinigungsfirma_v1.0.xlsx"

F = "Arial"
PETROL = "0F4C5C"
FOAM = "E6F6F1"
YELLOW = "FFF4C2"
GREY = "5B6975"
LINE = "D5DDDF"


def font(bold=False, size=10, color="000000", italic=False):
    return Font(name=F, bold=bold, size=size, color=color, italic=italic)


INP_FONT = font(color="0000FF")
INP_FILL = PatternFill("solid", fgColor=YELLOW)
HEAD_FILL = PatternFill("solid", fgColor=PETROL)
RES_FILL = PatternFill("solid", fgColor=FOAM)
thin = Side(style="thin", color=LINE)
BOX = Border(top=thin, bottom=thin, left=thin, right=thin)
EUR = '#,##0.00 "€";-#,##0.00 "€";"-"'
EUR0 = '#,##0 "€";-#,##0 "€";"-"'
PCT = "0.0%"
NUM1 = '#,##0.0;-#,##0.0;"-"'
NUM2 = '#,##0.00;-#,##0.00;"-"'
LINK = font(color="008000")


def base(ws, widths):
    ws.sheet_view.showGridLines = False
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


def title(ws, text, sub):
    ws["A1"] = text
    ws["A1"].font = font(True, 16, PETROL)
    ws["A2"] = sub
    ws["A2"].font = font(size=10, color=GREY, italic=True)
    ws.row_dimensions[1].height = 26


def inp(c, v, fmt=None):
    c.value = v
    c.font = INP_FONT
    c.fill = INP_FILL
    c.border = BOX
    if fmt:
        c.number_format = fmt


def label(c, v, bold=False):
    c.value = v
    c.font = font(bold)


def header_row(ws, row, labels):
    for i, t in enumerate(labels):
        c = ws.cell(row=row, column=i + 1, value=t)
        c.font = font(True, 10, "FFFFFF")
        c.fill = HEAD_FILL
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = BOX
    ws.row_dimensions[row].height = 30


def section(ws, cell, text):
    ws[cell] = text
    ws[cell].font = font(True, 11, PETROL)


wb = Workbook()

# ---------------- Start ----------------
ws = wb.active
ws.title = "Start"
base(ws, {"A": 4, "B": 30, "C": 70})
ws["B2"] = "Kalkulations-Kit für Reinigungsfirmen"
ws["B2"].font = font(True, 18, PETROL)
ws["B3"] = "Stundensatz · Objektkalkulation · Angebot  |  Version 1.0"
ws["B3"].font = font(size=10, color=GREY)
rows = [
    ("So benutzen Sie die Vorlage", None),
    ("1. Stundensatz", "Tragen Sie Lohn, Ausfalltage und Gemeinkosten ein. Ergebnis: Ihr Mindest-Stundensatz."),
    ("2. Leistungswerte", "Richtwerte in m² pro Stunde je Raumart. Passen Sie diese an Ihre eigene Erfahrung an."),
    ("3. Objektkalkulation", "Bereiche, Flächen und Reinigungen pro Woche eintragen. Ergebnis: Stunden und Monatspreis."),
    ("4. Angebot", "Füllt sich automatisch aus der Objektkalkulation. Nur Firmen- und Kundendaten ergänzen, dann drucken oder als PDF speichern."),
    ("", None),
    ("Farben", None),
    ("Gelbes Feld, blaue Schrift", "Eingabe: hier tragen Sie Ihre Werte ein."),
    ("Schwarze Schrift", "Formel: wird automatisch berechnet, bitte nicht überschreiben."),
    ("Grüne Schrift", "Wert kommt aus einem anderen Tabellenblatt."),
    ("", None),
    ("Hinweise", None),
    ("Beispielwerte", "Alle vorausgefüllten Zahlen sind Beispiele. Ersetzen Sie sie durch Ihre eigenen."),
    ("Lohnnebenkosten", "Die Prozentsätze sind Richtwerte. Die genauen Werte für Ihren Betrieb nennt Ihnen Ihr Steuerberater oder Lohnbüro."),
    ("Länder", "Funktioniert für Deutschland, Österreich und die Schweiz: MwSt-Satz im Blatt Stundensatz anpassen (DE 19 %, AT 20 %, CH 8,1 %)."),
    ("Google Sheets", "Datei in Google Drive hochladen und mit Google Sheets öffnen. Alle Formeln funktionieren."),
]
r = 5
for a, b in rows:
    if b is None and a:
        ws.cell(row=r, column=2, value=a).font = font(True, 11, PETROL)
    else:
        ws.cell(row=r, column=2, value=a).font = font(True)
        c = ws.cell(row=r, column=3, value=b)
        c.font = font()
        c.alignment = Alignment(wrap_text=True, vertical="top")
    r += 1
ws["B12"].fill = INP_FILL
ws["B12"].font = font(True, color="0000FF")
ws["B14"].font = font(True, color="008000")

# ---------------- Stundensatz ----------------
s = wb.create_sheet("Stundensatz")
base(s, {"A": 44, "B": 16, "C": 58})
title(s, "Stundensatz-Kalkulation", "Was muss eine verkaufte Reinigungsstunde mindestens kosten?")

section(s, "A4", "Lohn")
label(s["A5"], "Bruttostundenlohn Reinigungskraft"); inp(s["B5"], 15.00, EUR)
s["C5"] = "Ihr Tariflohn bzw. tatsächlich gezahlter Lohn"
label(s["A6"], "Arbeitgeberanteil Sozialversicherung"); inp(s["B6"], 0.21, PCT)
s["C6"] = "Richtwert DE ca. 20–22 %, bitte mit Lohnbüro prüfen"
label(s["A7"], "Umlagen, Berufsgenossenschaft, Sonstiges"); inp(s["B7"], 0.05, PCT)
s["C7"] = "U1/U2, Insolvenzgeld, BG. Richtwert, bitte prüfen"
label(s["A8"], "Lohnnebenkosten gesamt"); s["B8"] = "=B6+B7"; s["B8"].number_format = PCT
label(s["A9"], "Lohnkosten je bezahlte Stunde"); s["B9"] = "=B5*(1+B8)"; s["B9"].number_format = EUR

section(s, "A11", "Ausfallzeiten (pro Jahr, je Vollzeitkraft)")
label(s["A12"], "Arbeitstage pro Jahr (5-Tage-Woche)"); inp(s["B12"], 261, "0")
label(s["A13"], "Urlaubstage"); inp(s["B13"], 26, "0")
label(s["A14"], "Feiertage (Werktage)"); inp(s["B14"], 10, "0")
label(s["A15"], "Krankheitstage (Durchschnitt)"); inp(s["B15"], 12, "0")
label(s["A16"], "Produktive Tage"); s["B16"] = "=B12-B13-B14-B15"; s["B16"].number_format = "0"
label(s["A17"], "Produktive Zeit (Anteil)"); s["B17"] = "=IF(B12>0,B16/B12,0)"; s["B17"].number_format = PCT
s["C17"] = "Bezahlt wird 100 %, gearbeitet nur dieser Anteil"
label(s["A18"], "Lohnkosten je produktive Stunde"); s["B18"] = "=IF(B17>0,B9/B17,0)"; s["B18"].number_format = EUR

section(s, "A20", "Gemeinkosten pro Monat")
gk = [("Büro / Miete", 400), ("Fahrzeuge (Leasing, Sprit, Versicherung)", 900),
      ("Betriebs- und Haftpflichtversicherung", 120), ("Steuerberater / Buchhaltung", 250),
      ("Telefon, Software, Internet", 80), ("Geschäftsführer-Gehalt (Ihr eigener Lohn)", 0),
      ("Werbung", 100), ("Sonstiges", 150)]
r = 21
for name, v in gk:
    label(s.cell(row=r, column=1), name); inp(s.cell(row=r, column=2), v, EUR0); r += 1
s["C26"] = "Ihr eigenes Gehalt nicht vergessen, wenn Sie nicht selbst mitreinigen"
label(s["A29"], "Gemeinkosten gesamt pro Monat", True)
s["B29"] = "=SUM(B21:B28)"; s["B29"].number_format = EUR0; s["B29"].font = font(True)
label(s["A30"], "Verrechenbare Stunden pro Monat (alle Mitarbeiter)"); inp(s["B30"], 800, "#,##0")
s["C30"] = "Stunden, die Sie Kunden tatsächlich in Rechnung stellen"
label(s["A31"], "Gemeinkosten je verrechenbare Stunde"); s["B31"] = "=IF(B30>0,B29/B30,0)"; s["B31"].number_format = EUR

section(s, "A33", "Material, Gewinn, Steuer")
label(s["A34"], "Material & Reinigungsmittel je Stunde"); inp(s["B34"], 0.90, EUR)
s["C34"] = "Richtwert 0,60–1,20 €/h in der Unterhaltsreinigung"
label(s["A35"], "Wagnis & Gewinn (Aufschlag auf Selbstkosten)"); inp(s["B35"], 0.12, PCT)
label(s["A36"], "Mehrwertsteuersatz"); inp(s["B36"], 0.19, PCT)
s["C36"] = "DE 19 %, AT 20 %, CH 8,1 %"

section(s, "A38", "Ergebnis")
res = [("Lohnkosten je produktive Stunde", "=B18"), ("Gemeinkosten je Stunde", "=B31"),
       ("Material je Stunde", "=B34"), ("Selbstkosten je Stunde", "=B39+B40+B41"),
       ("Wagnis & Gewinn", "=B42*B35"), ("Mindest-Stundensatz netto", "=B42+B43"),
       ("Mindest-Stundensatz brutto (inkl. MwSt)", "=B44*(1+B36)")]
r = 39
for name, f in res:
    a = s.cell(row=r, column=1, value=name)
    b = s.cell(row=r, column=2, value=f)
    b.number_format = EUR
    for c in (a, b):
        c.fill = RES_FILL; c.border = BOX
    a.font = font(r in (42, 44)); b.font = font(r in (42, 44))
    r += 1
s["A44"].font = font(True, 12, PETROL); s["B44"].font = font(True, 12, PETROL)
s["C44"] = "Diesen Wert übernimmt die Objektkalkulation automatisch"
for rr in range(4, 46):
    s.cell(row=rr, column=3).font = font(size=9, color=GREY)
s.freeze_panes = "A4"

# ---------------- Leistungswerte ----------------
l = wb.create_sheet("Leistungswerte")
base(l, {"A": 34, "B": 18, "C": 60})
title(l, "Leistungswerte Unterhaltsreinigung",
      "Richtwerte: wie viele m² eine Kraft pro Stunde schafft. Bitte an Ihre Objekte anpassen.")
header_row(l, 4, ["Raumart", "Leistungswert (m²/h)", "Hinweis"])
lw = [("Büro, Hartboden", 200, "Normal möbliert"), ("Büro, Teppich", 180, "Saugen braucht mehr Zeit"),
      ("Büro, stark möbliert", 140, "Viele Arbeitsplätze, viel Kleinkram"),
      ("Flur / Verkehrsfläche", 300, "Wenig Möbel"),
      ("Eingangsbereich / Foyer", 220, "Glas und Schmutzfangmatten beachten"),
      ("Treppenhaus", 150, "Pro m² Grundfläche inkl. Stufen"), ("Sanitär / WC", 60, "Hoher Aufwand, Hygiene"),
      ("Teeküche", 110, "Spüle, Geräte außen"), ("Besprechungsraum", 220, ""), ("Umkleide / Dusche", 90, ""),
      ("Arztpraxis / Behandlungsraum", 120, "Ggf. Desinfektion extra kalkulieren"),
      ("Lager / Nebenraum", 400, "Nur Boden"),
      ("Werkstatt / Produktion", 250, "Stark abhängig vom Verschmutzungsgrad"),
      ("Eigene Raumart 1", 150, "Name und Wert frei wählbar"),
      ("Eigene Raumart 2", 150, "Name und Wert frei wählbar")]
r = 5
for name, v, h in lw:
    inp(l.cell(row=r, column=1), name); inp(l.cell(row=r, column=2), v, "#,##0")
    c = l.cell(row=r, column=3, value=h); c.font = font(size=9, color=GREY); c.border = BOX
    r += 1
l["A21"] = ("Richtwerte aus der Praxis der Unterhaltsreinigung. Tatsächliche Werte hängen von Möblierung, "
            "Verschmutzung und Personal ab. Messen Sie bei neuen Objekten eine Probereinigung.")
l["A21"].font = font(size=9, color=GREY, italic=True)
l.merge_cells("A21:C22")
l["A21"].alignment = Alignment(wrap_text=True, vertical="top")

# ---------------- Objektkalkulation ----------------
o = wb.create_sheet("Objektkalkulation")
base(o, {"A": 26, "B": 28, "C": 12, "D": 13, "E": 13, "F": 13, "G": 13, "H": 15})
title(o, "Objektkalkulation", "Flächen und Intervalle eintragen, Stunden und Monatspreis werden berechnet.")
label(o["A4"], "Kunde"); inp(o["B4"], "Muster Steuerberatung GmbH")
label(o["A5"], "Objekt / Adresse"); inp(o["B5"], "Hauptstraße 12, 1. OG")
label(o["D4"], "Stundensatz netto")
o["F4"] = "=Stundensatz!B44"; o["F4"].number_format = EUR; o["F4"].font = LINK
o["G4"] = "aus Blatt Stundensatz"; o["G4"].font = font(size=9, color=GREY)
label(o["D5"], "Wochen pro Monat"); inp(o["F5"], 4.33, NUM2)
o["G5"] = "52 Wochen ÷ 12"; o["G5"].font = font(size=9, color=GREY)

header_row(o, 7, ["Bereich", "Raumart", "Fläche (m²)", "Leistungs-\nwert (m²/h)", "Reinigungen\npro Woche",
                  "Stunden je\nReinigung", "Stunden\npro Monat", "Kosten\npro Monat"])
ex = [("Büros", "Büro, Teppich", 240, 3), ("Flur", "Flur / Verkehrsfläche", 60, 3),
      ("WC Damen/Herren", "Sanitär / WC", 18, 5), ("Teeküche", "Teeküche", 12, 5),
      ("Besprechung", "Besprechungsraum", 30, 1)]
FIRST, LAST = 8, 27
dv = DataValidation(type="list", formula1="=Leistungswerte!$A$5:$A$19", allow_blank=True)
o.add_data_validation(dv)
for r in range(FIRST, LAST + 1):
    vals = ex[r - FIRST] if r - FIRST < len(ex) else (None, None, None, None)
    inp(o.cell(row=r, column=1), vals[0]); inp(o.cell(row=r, column=2), vals[1])
    inp(o.cell(row=r, column=3), vals[2], "#,##0"); inp(o.cell(row=r, column=5), vals[3], "0")
    dv.add(o.cell(row=r, column=2))
    o.cell(row=r, column=4, value=f'=IF(B{r}="","",IFERROR(INDEX(Leistungswerte!$B$5:$B$19,MATCH(B{r},Leistungswerte!$A$5:$A$19,0)),""))')
    o.cell(row=r, column=6, value=f'=IF(OR(C{r}="",D{r}="",D{r}=0),"",C{r}/D{r})')
    o.cell(row=r, column=7, value=f'=IF(OR(F{r}="",E{r}=""),"",F{r}*E{r}*$F$5)')
    o.cell(row=r, column=8, value=f'=IF(G{r}="","",G{r}*$F$4)')
    for col, fmt in ((4, "#,##0"), (6, NUM2), (7, NUM1), (8, EUR)):
        c = o.cell(row=r, column=col); c.number_format = fmt; c.border = BOX; c.font = font()
    o.cell(row=r, column=4).font = LINK

T = LAST + 2  # Summenzeile (29)
label(o.cell(row=T, column=1), "Summe", True)
o.cell(row=T, column=3, value=f"=SUM(C{FIRST}:C{LAST})").number_format = "#,##0"
o.cell(row=T, column=7, value=f"=SUM(G{FIRST}:G{LAST})").number_format = NUM1
o.cell(row=T, column=8, value=f"=SUM(H{FIRST}:H{LAST})").number_format = EUR
for col in (1, 3, 7, 8):
    o.cell(row=T, column=col).font = font(True)

section(o, f"A{T+2}", "Zuschläge und Monatspreis")
rr = T + 3  # 32
label(o.cell(row=rr, column=1), "Anfahrt je Einsatz (netto)"); inp(o.cell(row=rr, column=3), 8, EUR)
label(o.cell(row=rr + 1, column=1), "Einsätze pro Woche"); inp(o.cell(row=rr + 1, column=3), 5, "0")
label(o.cell(row=rr + 2, column=1), "Anfahrt pro Monat")
o.cell(row=rr + 2, column=3, value=f"=C{rr}*C{rr+1}*F5").number_format = EUR
label(o.cell(row=rr + 3, column=1), "Sonderzuschlag (z. B. Nacht, Wochenende)")
inp(o.cell(row=rr + 3, column=3), 0, PCT)

P = rr + 5  # 37
out = [("Monatspreis netto", f"=H{T}*(1+C{rr+3})+C{rr+2}", EUR),
       ("MwSt", f"=C{P}*Stundensatz!B36", EUR),
       ("Monatspreis brutto", f"=C{P}+C{P+1}", EUR),
       ("Preis je m² und Monat (netto)", f"=IF(C{T}>0,C{P}/C{T},0)", EUR),
       ("Jahreswert netto", f"=C{P}*12", EUR0)]
for i, (name, f, fmt) in enumerate(out):
    r = P + i
    a = o.cell(row=r, column=1, value=name)
    b = o.cell(row=r, column=3, value=f)
    o.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
    b.number_format = fmt
    for c in (a, o.cell(row=r, column=2), b):
        c.fill = RES_FILL; c.border = BOX
    a.font = font(i == 0); b.font = font(i == 0)
o.cell(row=P, column=1).font = font(True, 12, PETROL)
o.cell(row=P, column=3).font = font(True, 12, PETROL)
o.cell(row=P + 3, column=4, value="Zum Vergleich mit Marktpreisen je m²").font = font(size=9, color=GREY)
o.freeze_panes = "A8"

# ---------------- Angebot ----------------
a = wb.create_sheet("Angebot")
base(a, {"A": 26, "B": 26, "C": 12, "D": 16, "E": 16})
inp(a["A1"], "Ihre Firma GmbH"); a["A1"].font = Font(name=F, bold=True, size=14, color="0000FF")
inp(a["A2"], "Musterstraße 1 · 12345 Musterstadt · info@ihre-firma.de")
a["D1"] = "ANGEBOT"; a["D1"].font = font(True, 18, PETROL)
label(a["D3"], "Angebots-Nr."); inp(a["E3"], "2026-001")
label(a["D4"], "Datum"); inp(a["E4"], "=TODAY()", "DD.MM.YYYY")
label(a["A4"], "An:", True)
a["A5"] = "=Objektkalkulation!B4"; a["A5"].font = LINK
a["A6"] = "=Objektkalkulation!B5"; a["A6"].font = LINK
a["A8"] = "Unterhaltsreinigung"; a["A8"].font = font(True, 13, PETROL)
a["A9"] = ("Sehr geehrte Damen und Herren, vielen Dank für Ihre Anfrage. Gerne bieten wir Ihnen die "
           "regelmäßige Reinigung Ihrer Räume wie folgt an:")
a["A9"].font = font(); a["A9"].alignment = Alignment(wrap_text=True, vertical="top")
a.merge_cells("A9:E10"); a.row_dimensions[9].height = 18

header_row(a, 12, ["Bereich", "Raumart", "Fläche (m²)", "Reinigungen\npro Woche", "Stunden\npro Monat"])
for i in range(FIRST, LAST + 1):
    r = 13 + (i - FIRST)
    a.cell(row=r, column=1, value=f'=IF(Objektkalkulation!A{i}="","",Objektkalkulation!A{i})')
    a.cell(row=r, column=2, value=f'=IF(Objektkalkulation!B{i}="","",Objektkalkulation!B{i})')
    a.cell(row=r, column=3, value=f'=IF(Objektkalkulation!C{i}="","",Objektkalkulation!C{i})').number_format = "#,##0"
    a.cell(row=r, column=4, value=f'=IF(Objektkalkulation!E{i}="","",Objektkalkulation!E{i})').number_format = "0"
    a.cell(row=r, column=5, value=f'=IF(Objektkalkulation!G{i}="","",Objektkalkulation!G{i})').number_format = NUM1
    for col in range(1, 6):
        c = a.cell(row=r, column=col); c.font = font(); c.border = Border(bottom=thin)
end = 13 + (LAST - FIRST)
Q = end + 2
rows = [("Gesamtfläche", f"=Objektkalkulation!C{T}", '#,##0 "m²"'),
        ("Monatlicher Pauschalpreis netto", f"=Objektkalkulation!C{P}", EUR),
        ("zzgl. MwSt", f"=Objektkalkulation!C{P+1}", EUR),
        ("Monatlicher Pauschalpreis brutto", f"=Objektkalkulation!C{P+2}", EUR)]
for i, (name, f, fmt) in enumerate(rows):
    r = Q + i
    a.cell(row=r, column=2, value=name).font = font(i in (1, 3))
    a.cell(row=r, column=2).alignment = Alignment(horizontal="right")
    a.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
    c = a.cell(row=r, column=5, value=f); c.number_format = fmt; c.font = font(i in (1, 3), color="008000")
    if i == 3:
        for col in (2, 3, 4, 5):
            a.cell(row=r, column=col).fill = RES_FILL
a.cell(row=Q + 3, column=2).font = font(True, 11, PETROL)

B = Q + 6
section(a, f"A{B}", "Konditionen")
conds = ["Leistungsumfang gemäß beiliegendem Leistungsverzeichnis.",
         "Reinigungsmittel und Material sind im Preis enthalten.",
         "Abrechnung monatlich, zahlbar innerhalb von 14 Tagen ohne Abzug.",
         "Vertragslaufzeit 12 Monate, danach monatlich kündbar mit 3 Monaten Frist.",
         "Dieses Angebot ist 30 Tage gültig."]
for i, t in enumerate(conds):
    inp(a.cell(row=B + 1 + i, column=1), "• " + t)
    a.merge_cells(start_row=B + 1 + i, start_column=1, end_row=B + 1 + i, end_column=5)
inp(a.cell(row=B + 7, column=1), "Mit freundlichen Grüßen, Ihr Name")
a.merge_cells(start_row=B + 7, start_column=1, end_row=B + 7, end_column=3)

a.print_area = f"A1:E{B+8}"
a.page_setup.orientation = "portrait"
a.page_setup.paperSize = a.PAPERSIZE_A4
a.page_setup.fitToWidth = 1
a.page_setup.fitToHeight = 1
a.sheet_properties.pageSetUpPr.fitToPage = True

ws.page_setup.paperSize = ws.PAPERSIZE_A4
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.page_setup.fitToHeight = 1
for sh in (s, l, o):
    sh.page_setup.paperSize = sh.PAPERSIZE_A4
    sh.sheet_properties.pageSetUpPr.fitToPage = True
    sh.page_setup.fitToHeight = 0

s.sheet_properties.tabColor = PETROL
o.sheet_properties.tabColor = PETROL
a.sheet_properties.tabColor = "9FE3D1"

OUT.parent.mkdir(parents=True, exist_ok=True)
wb.save(OUT)
print("saved", OUT.relative_to(ROOT))
