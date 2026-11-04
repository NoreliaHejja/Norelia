import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from docx import Document
from docx.shared import Pt, Cm, RGBColor
OUT=sys.argv[1]
GREEN='0B6E4F'; YEL=PatternFill('solid',fgColor='FFF4C2'); HEAD=PatternFill('solid',fgColor='0B6E4F'); LIGHT=PatternFill('solid',fgColor='E3F4EC')
thin=Side(style='thin',color='C9D3CE'); B=Border(left=thin,right=thin,top=thin,bottom=thin)
wb=Workbook()
# --- Start
s=wb.active; s.title='Start'
rows=[('Preiserhöhungs-Rechner für Reinigungsfirmen',),('Reinigungsfirma OS · Version 1.0',),('',),
('So geht\'s',),('1. Blatt „Annahmen“: alten und neuen Stundenlohn, Lohnanteil und Sachkosten-Steigerung eintragen.',),
('2. Blatt „Objekte“: pro Kunde den heutigen Monatspreis eintragen. Neuer Preis und Erhöhung werden berechnet.',),
('3. Den neuen Preis in das Musterschreiben (Word-Datei) übernehmen.',),('',),
('Farben',),('Gelbe Felder = hier tragen Sie Ihre Zahlen ein. Alle anderen Felder rechnen automatisch.',),('',),
('Hinweis',),('Arbeitshilfe ohne Gewähr, keine Steuer- oder Rechtsberatung. Prüfen Sie Ihre Verträge (Preisanpassungsklausel, Kündigungsfristen) und Zahlen mit Ihrem Steuerberater.',)]
for r in rows: s.append(list(r))
s['A1'].font=Font(size=16,bold=True,color=GREEN); s['A2'].font=Font(italic=True,color='4A5A54')
for c in ('A4','A9','A12'): s[c].font=Font(bold=True,color=GREEN)
s['A10'].fill=YEL; s.column_dimensions['A'].width=110
for r in range(1,14): s.cell(r,1).alignment=Alignment(wrap_text=True,vertical='top')
# --- Annahmen
a=wb.create_sheet('Annahmen')
a.append(['Annahme','Wert','Erläuterung'])
data=[('Bisheriger Stundenlohn (€)',14.25,'Lohn, den Sie bisher zahlen (Lohngruppe 1 o. Ä.)'),
('Neuer Stundenlohn (€)',15.00,'Lohn ab Stichtag – aktuellen Tarifvertrag prüfen!'),
('Lohnanteil am Preis (%)',0.70,'Anteil der Lohnkosten (inkl. Nebenkosten) am Verkaufspreis; typisch 65–80 %'),
('Steigerung Sachkosten (%)',0.04,'Material, Fahrzeug, Versicherung, Energie'),
('Stichtag der Preisanpassung','01.01.2027','Datum für das Kundenschreiben'),
('Lohnsteigerung (%)','=B3/B2-1','berechnet'),
('Erforderliche Preiserhöhung (%)','=B4*B7+(1-B4)*B5','berechnet: Lohnanteil × Lohnsteigerung + Sachanteil × Sachkostensteigerung')]
for d in data: a.append(list(d))
for r in range(2,7): a.cell(r,2).fill=YEL
for r in (2,3): a.cell(r,2).number_format='#,##0.00 "€"'
for r in (4,5,7,8): a.cell(r,2).number_format='0.0%'
a['B8'].font=Font(bold=True,color=GREEN); a['B8'].fill=LIGHT
# --- Objekte
o=wb.create_sheet('Objekte')
o.append(['Kunde / Objekt','Heutiger Monatspreis netto (€)','Neuer Monatspreis netto (€)','Erhöhung pro Monat (€)','Erhöhung pro Jahr (€)','Notiz'])
examples=[('Beispiel: Bürogebäude Müller GmbH',1047),('Beispiel: Arztpraxis Dr. Weber',620),('Beispiel: Treppenhaus Hausverwaltung Nord',310)]
for i in range(30):
    r=i+2
    name,val=(examples[i] if i<len(examples) else ('',None))
    o.cell(r,1,name); o.cell(r,2,val)
    o.cell(r,3,f'=IF(B{r}="","",ROUND(B{r}*(1+Annahmen!$B$8),2))')
    o.cell(r,4,f'=IF(B{r}="","",C{r}-B{r})'); o.cell(r,5,f'=IF(B{r}="","",D{r}*12)')
    for c in (1,2,6): o.cell(r,c).fill=YEL
    for c in (2,3,4,5): o.cell(r,c).number_format='#,##0.00 "€"'
o.cell(33,1,'Summe').font=Font(bold=True)
for c,col in ((2,'B'),(3,'C'),(4,'D'),(5,'E')):
    o.cell(33,c,f'=SUM({col}2:{col}31)'); o.cell(33,c).number_format='#,##0.00 "€"'; o.cell(33,c).font=Font(bold=True,color=GREEN); o.cell(33,c).fill=LIGHT
for ws,widths in ((a,[34,16,70]),(o,[40,26,26,22,22,30])):
    for i,w in enumerate(widths): ws.column_dimensions[chr(65+i)].width=w
    for c in ws[1]: c.font=Font(bold=True,color='FFFFFF'); c.fill=HEAD; c.alignment=Alignment(wrap_text=True,vertical='center')
    ws.freeze_panes='A2'
    for row in ws.iter_rows(min_row=1,max_row=ws.max_row):
        for c in row: c.border=B
wb.save(f'{OUT}/Preiserhoehungs-Rechner_Reinigungsfirma_v1.0.xlsx')

# --- Word
d=Document()
st=d.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(11)
for sec in d.sections: sec.left_margin=sec.right_margin=Cm(2.2)
def h(t,l=1):
    p=d.add_heading(t,l)
    for r in p.runs: r.font.color.rgb=RGBColor(0x0B,0x6E,0x4F)
h('Preiserhöhungs-Paket für Reinigungsfirmen',0)
d.add_paragraph('Reinigungsfirma OS · Version 1.0 · Zwei Musterschreiben, Argumentationshilfe und Checkliste. Platzhalter in [eckigen Klammern] ersetzen. Arbeitshilfe ohne Gewähr – keine Rechtsberatung.')
h('Checkliste vor dem Versand')
for t in ['Vertrag prüfen: Gibt es eine Preisanpassungsklausel? Welche Fristen gelten?',
'Neuen Preis mit dem Preiserhöhungs-Rechner (Excel) ermitteln.',
'Stichtag mit ausreichendem Vorlauf wählen (Empfehlung: mindestens 6–8 Wochen).',
'Wichtige Kunden vorher anrufen – das Schreiben bestätigt dann nur das Gespräch.',
'Schreiben per E-Mail und zusätzlich per Post oder mit Lesebestätigung senden.']:
    d.add_paragraph(t,style='List Bullet')
def letter(title,body):
    d.add_page_break(); h(title)
    for line in ['[Ihr Firmenname] · [Straße Nr.] · [PLZ Ort]','','[Kunde]','[Ansprechpartner]','[Straße Nr.]','[PLZ Ort]','','[Ort], [Datum]','']:
        d.add_paragraph(line)
    for para in body: d.add_paragraph(para)
    for line in ['','Mit freundlichen Grüßen','','[Name]','[Firmenname]']: d.add_paragraph(line)
letter('Muster 1 – Anpassung wegen Mindestlohnerhöhung',[
'Betreff: Anpassung der Reinigungsvergütung ab [Stichtag] – Objekt [Objektname]',
'Sehr geehrte/r [Anrede Name],',
'vielen Dank für die gute Zusammenarbeit. Wir möchten Sie rechtzeitig über eine notwendige Anpassung informieren.',
'Zum [Stichtag des Tarifvertrags] steigt der allgemeinverbindliche Mindestlohn in der Gebäudereinigung von [alter Lohn] € auf [neuer Lohn] € pro Stunde. Diese Erhöhung sind wir gesetzlich verpflichtet an unsere Mitarbeiterinnen und Mitarbeiter weiterzugeben. Da die Lohnkosten den größten Teil unserer Leistung ausmachen, passen wir die Vergütung entsprechend an.',
'Ab dem [Stichtag] beträgt die monatliche Vergütung für das Objekt [Objektname] [neuer Preis] € netto (bisher [alter Preis] € netto). Das entspricht einer Anpassung um [Prozent] %. Leistungsumfang und Reinigungsintervalle bleiben unverändert.',
'Die Anpassung erfolgt gemäß [§ / Ziffer der Preisanpassungsklausel] unseres Vertrags vom [Vertragsdatum]. [Falls keine Klausel: Wir bitten Sie um Ihre Bestätigung bis zum [Datum].]',
'Für Fragen stehe ich Ihnen gern persönlich zur Verfügung – gern auch in einem kurzen Gespräch vor Ort.'])
letter('Muster 2 – Anpassung wegen allgemeiner Kostensteigerung',[
'Betreff: Preisanpassung ab [Stichtag] – Objekt [Objektname]',
'Sehr geehrte/r [Anrede Name],',
'seit unserer letzten Preisanpassung im [Jahr] sind die Kosten für Personal, Reinigungsmittel, Fahrzeuge und Versicherungen deutlich gestiegen. Um die gewohnte Qualität und zuverlässige Besetzung Ihres Objekts sicherzustellen, passen wir unsere Vergütung an.',
'Ab dem [Stichtag] beträgt die monatliche Vergütung [neuer Preis] € netto (bisher [alter Preis] € netto, Anpassung [Prozent] %). Leistungsumfang und Intervalle bleiben gleich.',
'Gern zeigen wir Ihnen in einem kurzen Termin, wie sich die Kalkulation zusammensetzt, und prüfen gemeinsam, ob Intervalle oder Leistungen optimiert werden können.',
'Wir bitten um Ihre Bestätigung bis zum [Datum] und danken Ihnen für Ihr Vertrauen.'])
d.add_page_break(); h('Argumentationshilfe: häufige Einwände')
qa=[('„Das ist uns zu teuer.“','Verstehe ich. Die Erhöhung entspricht im Wesentlichen der gesetzlichen Lohnsteigerung, die wir eins zu eins an unser Team weitergeben müssen. Sollen wir gemeinsam schauen, ob ein angepasstes Intervall (z. B. Flure 2× statt 3× pro Woche) Ihr Budget hält?'),
('„Andere Firmen sind günstiger.“','Das kann sein. Ein seriöses Angebot muss aber den Mindestlohn, Urlaub, Krankheit und Versicherung abdecken. Darunter wird entweder an Stunden oder an Personal gespart – das merken Sie an der Qualität.'),
('„Können wir die Erhöhung verschieben?“','Den Lohn zahlen wir ab dem Stichtag. Möglich ist, die Anpassung auf zwei Schritte zu verteilen: [x] % zum [Stichtag], der Rest zum [Datum].'),
('„Warum gerade jetzt?“','Weil der neue Tarifvertrag ab dem [Stichtag] gilt. Wir informieren Sie bewusst früh, damit Sie es in Ihrer Planung berücksichtigen können.'),
('„Wir kündigen.“','Das bedauern wir. Darf ich fragen, welcher Preis für Sie tragbar wäre? Dann prüfen wir, welcher Leistungsumfang dazu passt – oft finden wir eine Lösung.')]
t=d.add_table(rows=1,cols=2); t.style='Light Grid Accent 1'
t.rows[0].cells[0].text='Einwand'; t.rows[0].cells[1].text='Mögliche Antwort'
for q,ans in qa:
    c=t.add_row().cells; c[0].text=q; c[1].text=ans
d.add_paragraph(''); d.add_paragraph('Hinweis: Arbeitshilfe ohne Gewähr. Für die rechtliche Prüfung Ihrer Verträge wenden Sie sich bitte an eine Rechtsanwältin oder einen Rechtsanwalt.')
d.save(f'{OUT}/Preiserhoehung_Musterschreiben_Reinigungsfirma_v1.0.docx')
print('ok')
