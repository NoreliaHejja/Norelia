V={
"v1":(29.05,[(0.44,"2,91 € pro m²"),(3.11,"Klingt wenig?"),(4.31,"Ich zeig dir, warum das fair ist."),(6.90,"360 m² Büro,"),(9.12,"3× pro Woche."),(10.64,"Mit realistischen Leistungswerten"),(12.53,"sind das rund 26 Stunden im Monat."),(15.75,"Mal deinen echten Stundensatz,"),(17.71,"plus Material,"),(19.12,"und du landest bei gut 1.000 € im Monat."),(22.57,"Wer 1,80 € anbietet,"),(24.53,"zahlt drauf."),(25.85,"Rechne deinen Preis kostenlos."),(27.81,"Link in der Bio")]),
"v2":(24.05,[(0.52,"Dein Team arbeitet jeden fünften Tag umsonst."),(3.93,"Wenn du das vergisst."),(5.19,"Urlaub,"),(5.90,"Krankheit, Feiertage:"),(7.76,"Du zahlst sie."),(9.17,"Der Kunde nicht."),(10.85,"Außer, du rechnest sie ein."),(13.19,"Das sind rund 20 % Aufschlag – nur dafür."),(16.68,"Fehlt er,"),(17.64,"fehlt dein Gewinn."),(19.12,"Speicher dir das – und rechne nach."),(21.63,"Der Rechner ist kostenlos."),(23.09,"Link in der Bio")]),
"v3":(27.05,[(0.0,"15 € Lohn –"),(2.11,"und trotzdem 29,75 € Stundensatz?"),(5.67,"Pass auf."),(6.96,"Lohn"),(7.87,"+ Lohnnebenkosten"),(9.51,"+ Ausfallzeiten"),(11.08,"+ Gemeinkosten"),(12.55,"+ Material"),(13.83,"+ Wagnis & Gewinn"),(16.28,"= 29,75 € netto pro Stunde"),(20.22,"Darunter verdienst du nichts."),(22.40,"Und deine eigenen Zahlen?"),(24.39,"Der Rechner ist gratis."),(25.97,"Link im Profil")]),
}
def t(s):
    h=int(s//3600); m=int(s%3600//60); return f"{h}:{m:02d}:{s%60:05.2f}"
HEAD="""[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,DejaVu Sans,46,&H00FFFFFF,&H00FFFFFF,&H00000000,&H9A2F3A34,-1,0,0,0,100,100,0,0,3,14,0,2,70,70,330,1
Style: Lbl,DejaVu Sans,24,&H00FFFFFF,&H00FFFFFF,&H00000000,&H802F3A34,0,0,0,0,100,100,0,0,3,8,0,8,40,40,70,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
for k,(dur,segs) in V.items():
    out=HEAD+f"Dialogue: 0,{t(0)},{t(dur)},Lbl,,0,0,0,,KI-generierte Figur\n"
    for i,(s,txt) in enumerate(segs):
        e=segs[i+1][0] if i+1<len(segs) else dur
        out+=f"Dialogue: 1,{t(s)},{t(e-0.05)},Sub,,0,0,0,,{txt}\n"
    open(k+".ass","w").write(out)
