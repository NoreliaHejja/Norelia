#!/usr/bin/env python3
"""Általános Kindness-kit generátor (Kindness Elf minta). A Reindeer-kit szerkezete, szereplőnként konfigurálva.
  python3 scripts/build_kindness_kit.py <snowman|cupid|wichtel>
Képek: termekek/<slug>/char.png és char-bye.png (átlátszó hátterű akvarell)."""
import sys
from pathlib import Path
from common import page_head, icon, footer

ROOT = Path(__file__).resolve().parent.parent / "termekek"

BASE_CSS = """.cv{ background:linear-gradient(180deg,var(--cream),var(--tint)); align-items:center; justify-content:center; text-align:center; }
.cv img{ width:2.6in; } .cv h1{ font-size:38pt; color:var(--sage); margin:6px 0 4px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:18px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.letter{ border:3px double var(--sage); border-radius:18px; padding:26px 30px; background:#fff; flex:1; margin-bottom:.15in; display:flex; flex-direction:column; align-items:center; text-align:center; }
.letter img{ width:1.9in; } .letter h2{ color:var(--sage); font-size:24pt; margin:6px 0 10px; }
.letter p{ font-size:15pt; line-height:1.55; margin:0 0 10px; color:#333; max-width:5.6in; } .letter .sig{ margin-top:auto; font-size:14pt; color:var(--dark); font-style:italic; }
.notes{ display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:12px; flex:1; margin-bottom:.12in; }
.note{ border:2px dashed var(--sage); border-radius:16px; padding:12px 14px; background:#fff; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap:6px; }
.note:nth-child(even){ border-color:var(--dark); } .note .d{ font-size:10pt; color:var(--sage); font-weight:700; letter-spacing:.06em; }
.note .m{ font-size:16pt; font-weight:600; color:#333; line-height:1.3; } .note .f{ font-size:10pt; color:var(--dark); font-style:italic; }
.track{ display:grid; grid-template-columns:repeat(6,1fr); gap:12px; margin:8px 0 14px; }
.track div{ border:2.5px solid var(--dark); border-radius:50%; aspect-ratio:1; display:flex; align-items:center; justify-content:center; font-size:20pt; font-weight:700; color:var(--dark); }
.track.t14{ grid-template-columns:repeat(5,1fr); }
.pp{ border:2px solid var(--line); border-radius:14px; padding:12px 16px; background:#fff; margin-bottom:12px; }
.pp h3{ margin:0 0 6px; color:var(--sage); font-size:13pt; } .ln{ border-bottom:1.5px solid var(--line); height:.4in; }
.draw{ border:2px dashed var(--dark); border-radius:14px; height:3in; display:flex; align-items:flex-end; justify-content:center; padding:8px; color:var(--dark); font-size:11pt; margin-bottom:12px; }
.ideas{ columns:2; column-gap:22px; font-size:11pt; line-height:1.55; } .ideas li{ margin-bottom:4px; }
.cert{ border:6px double var(--accent); border-radius:20px; padding:30px; flex:1; margin-bottom:.15in; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; background:#fff; }
.cert h2{ font-size:30pt; color:var(--sage); margin:8px 0; } .cert .name{ border-bottom:2px solid var(--dark); width:4.6in; height:.55in; margin:14px 0; }
"""

# ---------------------------------------------------------------- SNOWMAN (január)
SNOWMAN = dict(
    slug="kindness-snowman-kit", name="Kindness Snowman Kit", lang="en", days=24,
    colors=":root{ --dark:#2c4a6e; --sage:#3f7cac; --tint:#eaf3fb; --line:#cfe0ef; --accent:#d9a441; --warm:#f4f7fb; --warmline:#d6dfeb; --cream:#fbfdff; }",
    ic="#3f7cac", sig="Love, your Kindness Snowman", fn="♥ your Kindness Snowman",
    eyebrow="Printable kit · Ages 3 to 8 · January",
    h1="Kindness<br>Snowman Kit",
    tg="The elf has gone home, but the kindness doesn't have to stop. A little snowman brings one kind mission a day all through January. No mess, five minutes a morning.",
    pill="20 pages · US Letter + A4",
    how_title="How the Kindness Snowman works",
    how_sub="January can feel long after the holidays. Each morning your child finds a note from the Kindness Snowman with one small, kind thing to do. Read it together, do it together, and color one snowflake on the tracker.",
    steps=[("Meet your snowman", "Any soft toy or a paper snowman can be your Kindness Snowman. Fill in the snowman passport together."),
           ("Print and cut", "Print the notes on paper or cardstock and cut them apart (4 per page). Keep them in an envelope."),
           ("One note a day", "Leave a note out in the evening, read it together in the morning. Most missions take five minutes and cost nothing."),
           ("Celebrate", "Color a circle on the tracker. After 24 days, read the goodbye letter and give the \"I was kind\" certificate.")],
    tip1=("Forgot a note?", "Use the lifesaver letters: \"I was busy building snow forts\" and \"Too warm today!\""),
    tip2=("Make it yours", "Start any day in January. Skip any mission that doesn't fit and use the blank notes and 30 extra ideas."),
    arrive=("Hello from the snowy hills!", ["Hi, friend! The elves told me you were SO kind in December. Now it's my turn to visit.", "Every morning I will leave you one kind mission. Kindness keeps snowmen from melting, so every kind thing you do keeps me cool and happy.", "Let's make January the kindest month ever!"]),
    passport="My snowman passport", draw="Draw your snowman here",
    pp=["My snowman's name", "My snowman's favorite winter game", "My name", "Day my snowman arrived"],
    missions=[("hug", "Give someone a warm winter hug."), ("toy", "Tidy up your toys before dinner."), ("heart", "Say “thank you” to your teacher."),
              ("star", "Draw a snowy picture for a grandparent."), ("leaf", "Put out seeds for the winter birds."), ("child", "Invite someone new to play."),
              ("shoe", "Line up the wet boots by the door."), ("cat", "Help feed or brush a pet."), ("sun", "Smile and wave at a neighbor."),
              ("book", "Read a winter story to someone younger."), ("spoon", "Help make a warm cup of cocoa for someone."), ("heart", "Make a card for someone who feels sick."),
              ("shirt", "Help fold the scarves and mittens."), ("bowl", "Help clear the table after dinner."), ("star", "Give three compliments today."),
              ("hug", "Tell someone why you love them."), ("toy", "Share your favorite toy for a whole game."), ("window", "Make a thank-you note for the snow plow or mail carrier."),
              ("sun", "Sing a song to cheer someone up."), ("child", "Help a friend put on their coat."), ("star", "Make a paper snowflake for a friend."),
              ("leaf", "Pick up one piece of litter on a walk (with a grown-up)."), ("bowl", "Bake or decorate cookies to share."), ("heart", "Give everyone a good-night hug.")],
    tracker_sub="After each kind mission, color one circle. Can you keep your snowman cool for all 24 days?",
    life1=("Sorry, I was building snow forts!", ["Good morning! I got so busy building a snow fort with my friends that I forgot the time.", "Today's kind mission: help someone without being asked. I'll be back on time tomorrow!"]),
    life2=("Too warm today!", ["Brrr, it got a little warm last night, so I hid in the shade.", "Today's kind mission: give someone a cold drink of water and a big smile. See you tomorrow!"]),
    mid=("You're doing great!", ["Twelve kind missions done! All the snowmen on the hill are cheering for you.", "Keep going, little friend. Your kindness is keeping me frosty and happy."]),
    extra_title="Snow day kindness", extra_sub="Stuck inside on a snow day? Pick one of these cozy kind missions together.",
    extra_notes=["Make hot cocoa for the family", "Build a blanket fort for a sibling", "Draw a winter card for a neighbor", "Help shovel a path (with a grown-up)"],
    extra_head="SNOW DAY MISSION", extra_foot="Do it together on a snow day",
    extra_mini="Cut out the cards and keep them for snowy days. Stay warm and safe outside, always with a grown-up.",
    bye=("Goodbye for now!", ["Spring is coming, and it's time for me to go back to the snowy mountains.", "Thank you for every hug, every smile and every kind thing you did. Keep being kind all year long.", "See you next winter!"]),
    bye_sig="Love forever, your Kindness Snowman",
    cert=("Official Snowy Hills award", "I Was Kind!", "for 24 days of January kindness. Every snowman on the hill is proud of you!", "Signed: Your Kindness Snowman"),
    ideas_sub="Swap in any of these when a note doesn't fit your day. Keep missions short, concrete and done together.",
    ideas=["Hold the door for someone", "Help carry the groceries", "Give your sibling the first turn", "Say “please” at every meal", "Bring a grown-up a glass of water",
           "Help feed the pet", "Tidy up the bookshelf", "Make a get-well drawing", "Leave a sticker on someone’s pillow", "Call a grandparent and sing",
           "Give a compliment: “I like your hat!”", "Help fold the towels", "Put a toy back for someone else", "Make a picture for the school bus driver",
           "Comfort a sad friend", "Hang up your coat and someone else’s", "Wash plastic cups in the sink", "Share your snack", "Help make breakfast toast",
           "Give the plants a drink", "Clean up crayons without being asked", "Say “sorry” and hug", "Wave at a neighbor’s window", "Make a bracelet for a friend",
           "Help match the socks", "Let someone else choose the song", "Brush the dog or the teddy", "Fill the bird feeder", "Warm up someone’s slippers", "Give a good-night hug to everyone"],
    pair="Loved the Kindness Elf or the Kindness Reindeer in December? The Snowman keeps the same 5-minute habit going in January. Find them in our shop.",
    foot_names=dict(how="For grown-ups", arr="Arrival letter", pas="Passport", notes="Notes", track="Tracker", life="Lifesaver letter", mid="Mid-month letter",
                    extra="Snow day cards", bye="Goodbye letter", cert="Certificate", blank="Blank notes", ideas="For personal use only · © AureliaVenn"),
    labels=dict(grown="For grown-ups", cut="Cut and use one a day", notes="Kindness notes · days", trk_h="Color one circle a day", trk="My kindness tracker",
                fav="My favorite kind thing", meet="Meet your snowman", own="Your own ideas", blank="Blank kindness notes", more="30 more tiny kindness ideas",
                pair="Pair it with", day="DAY", date="Date ____________", forg="Forgot a note?"),
)

# ---------------------------------------------------------------- CUPID (február, 14 nap)
CUPID = dict(
    slug="valentine-kindness-cupid-kit", name="Valentine Kindness Cupid Kit", lang="en", days=14,
    colors=":root{ --dark:#7a2848; --sage:#d2486e; --tint:#fdeef2; --line:#f3cfd9; --accent:#e5a823; --warm:#fff4f6; --warmline:#f2d6de; --cream:#fffafb; }",
    ic="#d2486e", sig="Love, your Kindness Cupid", fn="♥ your Kindness Cupid",
    eyebrow="Printable kit · Ages 3 to 8 · February",
    h1="Valentine<br>Kindness Cupid",
    tg="A little cupid brings one kind mission a day for the 14 days before Valentine's Day. Hearts instead of candy, five minutes a morning, no mess.",
    pill="18 pages · US Letter + A4",
    how_title="How the Kindness Cupid works",
    how_sub="Valentine's Day is about love, and kids show love best by doing. From February 1 to 14, your child finds a note from the Kindness Cupid with one small, kind thing to do. Color one heart on the tracker after each one.",
    steps=[("Meet your cupid", "Any soft toy or a paper heart can be your Kindness Cupid. Fill in the cupid passport together."),
           ("Print and cut", "Print the notes on paper or cardstock and cut them apart (4 per page). Keep them in an envelope."),
           ("One note a day", "Start on February 1. Leave a note out each evening and read it together in the morning."),
           ("Celebrate", "Color a heart on the tracker. On Valentine's Day, read the goodbye letter and give the \"I was kind\" certificate.")],
    tip1=("Forgot a note?", "Use the lifesaver letters: \"My wings got tangled\" and \"I was busy making cards\"."),
    tip2=("Make it yours", "Start any day. Use the 12 Valentine kindness cards for classmates and the blank notes for your own ideas."),
    arrive=("Hello, little friend!", ["Hi! I'm a Kindness Cupid. Instead of arrows, I carry little hearts full of kindness.", "For the next 14 days, I will leave you one kind mission every morning. Every kind thing you do fills my heart bag a little more.", "On Valentine's Day, we will share all that love together!"]),
    passport="My cupid passport", draw="Draw your cupid here",
    pp=["My cupid's name", "My cupid's favorite color", "My name", "Day my cupid arrived"],
    missions=[("heart", "Tell someone in your family why you love them."), ("hug", "Give a big hug to someone who looks tired."), ("star", "Make a heart drawing for a grandparent."),
              ("child", "Play with someone who is playing alone."), ("spoon", "Help set the table with a heart napkin."), ("toy", "Share a toy you really like."),
              ("book", "Read a story to someone younger."), ("sun", "Give three people a compliment today."), ("window", "Make a heart for the mail carrier's box."),
              ("cat", "Be extra gentle with a pet or a teddy."), ("bowl", "Help clean up after dinner."), ("heart", "Make a Valentine card for your teacher."),
              ("leaf", "Put out seeds for the birds, with love."), ("hug", "Give everyone a Valentine hug tonight.")],
    tracker_sub="After each kind mission, color one heart circle. Fill all 14 before Valentine's Day!",
    life1=("My wings got tangled!", ["Good morning! My little wings got tangled in a ribbon last night, so I'm a bit late.", "Today's kind mission: help someone untangle a problem. See you tomorrow!"]),
    life2=("I was busy making cards!", ["I made so many Valentine cards last night that I forgot to leave your note!", "Today's kind mission: make one card for someone special. I'll be back tomorrow!"]),
    mid=("Halfway there!", ["Seven kind missions done! Your kindness hearts are making my bag so heavy and happy.", "Keep going, little friend. Valentine's Day is getting closer!"]),
    extra_title="Valentine kindness cards", extra_sub="Classroom-friendly cards with no candy. Write a name, add a heart and give them to classmates or family.",
    extra_notes=["You make me smile!", "You're a great friend!", "Thanks for being kind!", "You're one of a kind!"],
    extra_head="TO: ____________", extra_foot="FROM: ____________",
    extra_mini="Print this page 3 times for a whole class. Kids can color the hearts before giving them away.",
    bye=("Happy Valentine's Day!", ["Today I fly home with a bag full of your kindness hearts.", "Thank you for every hug, every card and every kind thing you did. Love grows when we share it.", "Keep being kind all year long!"]),
    bye_sig="Love forever, your Kindness Cupid",
    cert=("Official Valentine award", "I Was Kind!", "for 14 days of Valentine kindness. Every cupid is proud of you!", "Signed: Your Kindness Cupid"),
    ideas_sub="Swap in any of these when a note doesn't fit your day. Keep missions short, concrete and done together.",
    ideas=["Hold the door for someone", "Say “I love you” at breakfast", "Give your sibling the first turn", "Say “please” at every meal", "Bring a grown-up a glass of water",
           "Help feed the pet", "Make a heart for the neighbor's door", "Make a get-well drawing", "Leave a heart sticker on someone’s pillow", "Call a grandparent and say “I love you”",
           "Give a compliment: “I like your drawing!”", "Help fold the towels", "Put a toy back for someone else", "Draw a heart for the bus driver",
           "Comfort a sad friend", "Help carry the laundry basket", "Wash plastic cups in the sink", "Share your snack", "Help make breakfast toast",
           "Give the plants a drink", "Clean up crayons without being asked", "Say “sorry” and hug", "Wave at a neighbor’s window", "Make a bracelet for a friend",
           "Help match the socks", "Let someone else choose the song", "Brush the dog or the teddy", "Make a heart chain for the window", "Write a love note to a parent", "Give a good-night hug to everyone"],
    pair="Our Kindness Elf, Kindness Reindeer and Kindness Snowman kits follow the same 5-minute idea for December and January. Find them in our shop.",
    foot_names=dict(how="For grown-ups", arr="Arrival letter", pas="Passport", notes="Notes", track="Tracker", life="Lifesaver letter", mid="Halfway letter",
                    extra="Valentine cards", bye="Goodbye letter", cert="Certificate", blank="Blank notes", ideas="For personal use only · © AureliaVenn"),
    labels=dict(grown="For grown-ups", cut="Cut and use one a day", notes="Kindness notes · days", trk_h="Color one heart a day", trk="My kindness tracker",
                fav="My favorite kind thing", meet="Meet your cupid", own="Your own ideas", blank="Blank kindness notes", more="30 more tiny kindness ideas",
                pair="Pair it with", day="DAY", date="Date ____________", forg="Forgot a note?"),
)

# ---------------------------------------------------------------- WICHTEL (német, december)
WICHTEL = dict(
    slug="freundlichkeits-wichtel-kit", name="Freundlichkeits-Wichtel", lang="de", days=24,
    colors=":root{ --dark:#3d5a3a; --sage:#b8322a; --tint:#fdf3ee; --line:#efd2c6; --accent:#d9a441; --warm:#eef6ef; --warmline:#cfe3d2; --cream:#fffaf3; }",
    ic="#b8322a", sig="Dein Freundlichkeits-Wichtel", fn="♥ dein Wichtel",
    eyebrow="Druckvorlage · 3 bis 8 Jahre · Dezember",
    h1="Freundlichkeits-<br>Wichtel",
    tg="Ein kleiner Wichtel zieht hinter der Wichteltür ein und bringt jeden Morgen eine freundliche Aufgabe. Kein Chaos, kein Mehl auf dem Boden, fünf Minuten am Tag.",
    pill="20 Seiten · A4 + US Letter",
    how_title="So funktioniert der Freundlichkeits-Wichtel",
    how_sub="Kinder lieben kleine Rituale. Jeden Morgen findet Ihr Kind an der Wichteltür einen Zettel mit einer kleinen, freundlichen Aufgabe. Gemeinsam lesen, gemeinsam machen und einen Kreis im Tracker ausmalen.",
    steps=[("Der Wichtel zieht ein", "Eine kleine Tür an der Fußleiste, ein Kuscheltier oder einfach ein Briefumschlag am Fenster reicht. Füllt zusammen den Wichtel-Ausweis aus."),
           ("Drucken und schneiden", "Die Zettel auf Papier oder Karton drucken und ausschneiden (4 pro Seite). In einem Umschlag bereitlegen."),
           ("Ein Zettel pro Tag", "Abends einen Zettel an die Wichteltür legen, morgens gemeinsam lesen. Die meisten Aufgaben dauern fünf Minuten und kosten nichts."),
           ("Feiern", "Einen Kreis im Tracker ausmalen. An Heiligabend den Abschiedsbrief lesen und die Urkunde überreichen.")],
    tip1=("Zettel vergessen?", "Dafür gibt es die Rettungsbriefe: „Ich habe verschlafen“ und „Schneesturm!“."),
    tip2=("Ganz nach Ihrer Familie", "Aufgaben, die nicht passen, einfach weglassen. Dafür gibt es leere Zettel und 30 weitere Ideen."),
    arrive=("Hallo, ich bin da!", ["Hallo, mein Freund! Ich bin ein kleiner Wichtel und wohne ab heute hinter deiner Wichteltür.", "Jeden Morgen lasse ich dir eine freundliche Aufgabe da. Freundlichkeit ist mein Wichtelzauber: Mit jeder guten Tat leuchtet meine Mütze ein bisschen heller.", "Ich freue mich schon auf all die lieben Dinge, die du tust!"]),
    passport="Mein Wichtel-Ausweis", draw="Male hier deinen Wichtel",
    pp=["So heißt mein Wichtel", "Das isst mein Wichtel am liebsten", "Mein Name", "An diesem Tag ist mein Wichtel eingezogen"],
    missions=[("hug", "Umarme jemanden, den du lieb hast."), ("toy", "Räume deine Spielsachen auf, ohne dass jemand fragt."), ("heart", "Sag „Danke“ zu der Person, die gekocht hat."),
              ("star", "Male ein Bild für Oma oder Opa."), ("leaf", "Streue Vogelfutter für die Vögel aus."), ("child", "Lass heute einen Freund oder dein Geschwister zuerst."),
              ("cart", "Hilf beim Einkäufe-Tragen."), ("cat", "Sei heute besonders sanft zu einem Tier oder Kuscheltier."), ("sun", "Winke und lächle einem Nachbarn zu."),
              ("leaf", "Gieße eine Pflanze in eurer Wohnung."), ("book", "Lies jemand Jüngerem eine Geschichte vor (oder dem Teddy)."), ("spoon", "Hilf beim Tischdecken."),
              ("heart", "Bastle eine Karte für jemanden, der traurig ist."), ("hug", "Sag drei Menschen, warum du sie magst."), ("bowl", "Hilf nach dem Essen beim Aufräumen."),
              ("shoe", "Stell alle Schuhe ordentlich an die Tür."), ("star", "Mach jedem beim Frühstück ein Kompliment."), ("sun", "Sing deiner Familie ein Weihnachtslied vor."),
              ("toy", "Such ein Spielzeug aus, das du an ein anderes Kind verschenkst."), ("shirt", "Hilf beim Wäsche-Falten."), ("window", "Mal ein Dankeschön-Bild für den Postboten."),
              ("star", "Bastle einen Papierstern für einen Freund."), ("bowl", "Back oder verziere Plätzchen zum Verschenken."), ("heart", "Gib heute Abend allen eine Dankeschön-Umarmung.")],
    tracker_sub="Nach jeder freundlichen Aufgabe malst du einen Kreis aus. Schau, wie deine Freundlichkeit bis Weihnachten wächst!",
    life1=("Ich habe verschlafen!", ["Guten Morgen! Ich war gestern so lange in der Wichtelwerkstatt, dass ich verschlafen habe.", "Deine Aufgabe heute: Schenke jemandem ein großes Lächeln. Morgen bin ich wieder pünktlich!"]),
    life2=("Schneesturm!", ["Ein großer Schneesturm hat mich gestern Nacht aufgehalten.", "Deine Aufgabe heute: Hilf jemandem, der einen schweren Tag hat. Morgen bin ich wieder da!"]),
    mid=("Du machst das toll!", ["Der Weihnachtsmann hat von all deinen guten Taten gehört. Er hat sich so gefreut, dass er ein Tänzchen gemacht hat!", "Mach weiter so, kleiner Freund. Weihnachten kommt näher und deine Freundlichkeit leuchtet hell."]),
    extra_title="Schilder für die Wichteltür", extra_sub="Ausschneiden und an die Wichteltür kleben. Ein Schild für die Ankunft, eins für Ruhe, eins für die Post und eins für den Abschied.",
    extra_notes=["Willkommen, kleiner Wichtel!", "Psst! Wichtel schläft", "Wichtelpost", "Danke und bis nächstes Jahr!"],
    extra_head="WICHTELTÜR", extra_foot="ausschneiden und aufkleben",
    extra_mini="Tipp: Auf Karton drucken. Kein Glitzer, kein Mehl: Der Wichtel mag es ordentlich.",
    bye=("Auf Wiedersehen!", ["Heute Nacht fliege ich mit dem Weihnachtsmann zurück in den Wichtelwald.", "Danke für jede Umarmung, jedes Lächeln und jede liebe Tat. Bleib das ganze Jahr so freundlich.", "Bis nächstes Jahr!"]),
    bye_sig="Für immer dein Freundlichkeits-Wichtel",
    cert=("Offizielle Wichtel-Urkunde", "Ich war freundlich!", "für 24 Tage Freundlichkeit. Alle Wichtel sind stolz auf dich!", "Unterschrift: Dein Wichtel"),
    ideas_sub="Wenn ein Zettel nicht in den Tag passt, nehmen Sie eine dieser Ideen. Kurz, konkret und gemeinsam gemacht.",
    ideas=["Jemandem die Tür aufhalten", "Mit einem Erwachsenen ein Stück Müll aufheben", "Dem Geschwister den Vortritt lassen", "Bei jedem Essen „bitte“ sagen",
           "Einem Erwachsenen ein Glas Wasser bringen", "Beim Füttern des Haustiers helfen", "Das Bücherregal aufräumen", "Ein Gute-Besserung-Bild malen",
           "Einen Sticker aufs Kopfkissen legen", "Oma anrufen und ein Lied singen", "Ein Kompliment machen: „Schöne Mütze!“", "Beim Handtücher-Falten helfen",
           "Ein Spielzeug für jemanden zurücklegen", "Ein Bild für den Busfahrer malen", "Einen traurigen Freund trösten", "Den Wäschekorb mittragen",
           "Plastikbecher spülen", "Den Snack teilen", "Beim Frühstück helfen", "Die Pflanzen gießen", "Stifte aufräumen, ohne gefragt zu werden",
           "„Entschuldigung“ sagen und umarmen", "Einem Nachbarn am Fenster winken", "Ein Armband für einen Freund basteln", "Socken sortieren",
           "Jemand anderen das Lied aussuchen lassen", "Den Hund oder den Teddy bürsten", "Vogelfutter nachfüllen", "Hausschuhe für jemanden anwärmen", "Allen eine Gute-Nacht-Umarmung geben"],
    pair="Unsere Kits gibt es auch auf Englisch (Kindness Elf, Kindness Reindeer) – praktisch für zweisprachige Familien. Alle im Shop AureliaVenn.",
    foot_names=dict(how="Für Eltern", arr="Ankunftsbrief", pas="Ausweis", notes="Zettel", track="Tracker", life="Rettungsbrief", mid="Brief zur Halbzeit",
                    extra="Türschilder", bye="Abschiedsbrief", cert="Urkunde", blank="Leere Zettel", ideas="Nur für den privaten Gebrauch · © AureliaVenn"),
    labels=dict(grown="Für Eltern", cut="Ausschneiden, ein Zettel pro Tag", notes="Freundlichkeits-Zettel · Tag", trk_h="Jeden Tag einen Kreis ausmalen", trk="Mein Freundlichkeits-Tracker",
                fav="Meine liebste gute Tat", meet="Lerne deinen Wichtel kennen", own="Eigene Ideen", blank="Leere Freundlichkeits-Zettel", more="30 weitere kleine Ideen",
                pair="Passt dazu", day="TAG", date="Datum ____________", forg="Zettel vergessen?"),
)

KITS = {"snowman": SNOWMAN, "cupid": CUPID, "wichtel": WICHTEL}


def img(name, w):
    return f'<img src="{name}" style="width:{w}" alt="">'


def build(k):
    out = ROOT / k["slug"]; out.mkdir(parents=True, exist_ok=True)
    N, L, F = k["name"], k["labels"], k["foot_names"]
    def letter(t, paras, sig=k["sig"], pic="char.png"):
        return f'<div class="letter">{img(pic, "1.9in")}<h2>{t}</h2>{"".join(f"<p>{p}</p>" for p in paras)}<div class="sig">{sig}</div></div>'
    pg = [f'<div class="page cv">{img("char.png", "2.6in")}<div class="eyebrow">{k["eyebrow"]}</div><h1>{k["h1"]}</h1><div class="tg">{k["tg"]}</div><div class="pill">{k["pill"]}</div></div>']
    steps = "".join(f'<div class="step"><div class="num">{i + 1}</div><div><b>{a}</b><p>{b}</p></div></div>' for i, (a, b) in enumerate(k["steps"]))
    pg.append(f"""<div class="page">{page_head(L["grown"], k["how_title"], "book")}<p class="subtitle">{k["how_sub"]}</p>{steps}
<div class="row" style="margin-top:auto"><div class="card col"><h3>{k["tip1"][0]}</h3><div class="mini">{k["tip1"][1]}</div></div>
<div class="card warm col"><h3>{k["tip2"][0]}</h3><div class="mini">{k["tip2"][1]}</div></div></div>{footer(N, F["how"])}</div>""")
    pg.append(f'<div class="page">{letter(*k["arrive"])}{footer(N, F["arr"])}</div>')
    pps = "".join(f'<div class="pp"><h3>{x}</h3><div class="ln"></div></div>' for x in k["pp"])
    pg.append(f'<div class="page">{page_head(L["meet"], k["passport"], "star")}<div class="draw">{k["draw"]}</div>{pps}{footer(N, F["pas"])}</div>')
    M = k["missions"]; D = k["days"]
    for i in range(0, D, 4):
        ns = "".join(f'<div class="note"><div class="d">{L["day"]} {d + 1}</div>{icon(ic, 46, k["ic"], 1.6)}<div class="m">{m}</div><div class="f">{k["fn"]}</div></div>'
                     for d, (ic, m) in list(enumerate(M))[i:i + 4])
        ns += "".join('<div class="note" style="visibility:hidden"></div>' for _ in range(4 - len(M[i:i + 4])))
        pg.append(f'<div class="page">{page_head(L["cut"], f"{L["notes"]} {i + 1}–{min(i + 4, D)}", "heart")}<div class="notes">{ns}</div>{footer(N, F["notes"])}</div>')
    circles = "".join(f"<div>{n}</div>" for n in range(1, D + 1))
    pg.append(f"""<div class="page">{page_head(L["trk_h"], L["trk"], "check")}<p class="subtitle">{k["tracker_sub"]}</p>
<div class="track{' t14' if D == 14 else ''}">{circles}</div>
<div class="row" style="margin-top:auto;margin-bottom:.15in"><div class="card col"><h3>{L["fav"]}</h3><div class="ln"></div><div class="ln"></div></div>{img("char.png", "1.6in")}</div>{footer(N, F["track"])}</div>""")
    pg.append(f'<div class="page">{letter(*k["life1"])}{footer(N, F["life"])}</div>')
    pg.append(f'<div class="page">{letter(*k["life2"])}{footer(N, F["life"])}</div>')
    pg.append(f'<div class="page">{letter(*k["mid"])}{footer(N, F["mid"])}</div>')
    ex = "".join(f'<div class="note"><div class="d">{k["extra_head"]}</div>{img("char.png", "1.1in")}<div class="m">{t}</div><div class="f">{k["extra_foot"]}</div></div>' for t in k["extra_notes"])
    pg.append(f'<div class="page">{page_head(L["cut"] if k["lang"] == "de" else "Bonus", k["extra_title"], "star")}<p class="subtitle">{k["extra_sub"]}</p><div class="notes">{ex}</div><div class="mini" style="margin-bottom:.12in">{k["extra_mini"]}</div>{footer(N, F["extra"])}</div>')
    pg.append(f'<div class="page">{letter(*k["bye"], sig=k["bye_sig"], pic="char-bye.png")}{footer(N, F["bye"])}</div>')
    c = k["cert"]
    to = "Diese Urkunde bekommt" if k["lang"] == "de" else "This certificate goes to"
    pg.append(f'<div class="page"><div class="cert">{img("char.png", "1.8in")}<div class="eyebrow">{c[0]}</div><h2>{c[1]}</h2><div style="font-size:14pt">{to}</div><div class="name"></div><div style="font-size:14pt">{c[2]}</div><div style="margin-top:22px;font-size:12pt;color:var(--dark)">{L["date"]} &nbsp;&nbsp; {c[3]}</div></div>{footer(N, F["cert"])}</div>')
    for _ in range(2):
        ns = "".join(f'<div class="note"><div class="d">{L["day"]} ___</div><div style="height:.9in;width:100%;border-bottom:1.5px solid var(--line)"></div><div class="f">{k["fn"]}</div></div>' for _ in range(4))
        pg.append(f'<div class="page">{page_head(L["own"], L["blank"], "heart")}<div class="notes">{ns}</div>{footer(N, F["blank"])}</div>')
    ideas = "".join(f"<li>{x}</li>" for x in k["ideas"])
    pg.append(f"""<div class="page">{page_head(L["grown"], L["more"], "star")}<p class="subtitle">{k["ideas_sub"]}</p><ul class="ideas">{ideas}</ul>
<div class="card warm" style="margin-top:auto;margin-bottom:.15in"><h3>{L["pair"]}</h3><div class="mini">{k["pair"]}</div></div>{footer(N, F["ideas"])}</div>""")
    html = f'<!DOCTYPE html><html lang="{k["lang"]}"><head><meta charset="utf-8"><title>{N}</title><link rel="stylesheet" href="../../assets/base.css"><style>{k["colors"]}{BASE_CSS}</style></head><body>{"".join(pg)}</body></html>'
    (out / f'{k["slug"]}.html').write_text(html, encoding="utf-8")
    print(k["slug"], "wrote", len(pg), "pages")




def _spring(**kw):
    """14 napos tavaszi kit a CUPID szerkezetére (közös mezők felülírva)."""
    k = dict(CUPID); k.update(kw); return k


LEPRECHAUN = _spring(
    slug="kindness-leprechaun-kit", name="Kindness Leprechaun Kit", days=14,
    colors=":root{ --dark:#2f5a3c; --sage:#3e8e4f; --tint:#edf6ef; --line:#cfe5d4; --accent:#d9a441; --warm:#f5faf6; --warmline:#d6e8da; --cream:#fbfdfb; }",
    ic="#3e8e4f", sig="Love, your Kindness Leprechaun", fn="♥ your Kindness Leprechaun",
    eyebrow="Printable kit · Ages 3 to 8 · March", h1="Kindness<br>Leprechaun Kit",
    tg="A cheeky little leprechaun leaves one kind mission a day for the 14 days before St. Patrick's Day. Gold coins for good deeds, no mess, five minutes a morning.",
    pill="18 pages · US Letter + A4", how_title="How the Kindness Leprechaun works",
    how_sub="From March 3 to 16, your child finds a note from the Kindness Leprechaun with one small, kind thing to do. After each one, color a gold coin on the tracker. On St. Patrick's Day, the leprechaun leaves a goodbye letter.",
    steps=[("Meet your leprechaun", "No special doll needed. A paper hat, a green sock or a little drawing can be your leprechaun. Fill in the passport together."),
           ("Print and cut", "Print the notes on paper or cardstock and cut them apart (4 per page). Keep them in an envelope."),
           ("One note a day", "Leave a note out each evening, read it together in the morning. Most missions take five minutes."),
           ("Celebrate", "Color a coin on the tracker. On St. Patrick's Day, read the goodbye letter and give the \"I was kind\" certificate.")],
    tip1=("Forgot a note?", "Use the lifesaver letters: \"I got lost at the end of the rainbow\" and \"I was counting my gold\"."),
    tip2=("Make it yours", "Use the 4 gold coin cards as small rewards and the blank notes for your own ideas."),
    arrive=("Top of the morning!", ["Hello, friend! I'm a little leprechaun, and I collect something more precious than gold: kindness.", "For the next 14 days, I'll leave you one kind mission every morning. Every kind thing you do adds a shiny coin to my pot.", "Let's fill it all the way up by St. Patrick's Day!"]),
    passport="My leprechaun passport", draw="Draw your leprechaun here", pp=["My leprechaun's name", "Where my leprechaun hides", "My name", "Day my leprechaun arrived"],
    tracker_sub="After each kind mission, color one gold coin. Fill all 14 before St. Patrick's Day!",
    life1=("I got lost at the end of the rainbow!", ["Good morning! I followed a rainbow last night and it went on and on.", "Today's kind mission: help someone find something they lost. See you tomorrow!"]),
    life2=("I was counting my gold!", ["I was so busy counting coins that I forgot your note!", "Today's kind mission: share something you have with someone else. Back tomorrow!"]),
    mid=("Halfway to the gold!", ["Seven kind missions done! My pot of kindness is getting so full.", "Keep going, little friend. St. Patrick's Day is almost here!"]),
    extra_title="Gold coin reward cards", extra_sub="Cut out these little cards and give one for an extra-kind moment.",
    extra_notes=["Kind hands award", "Great helper award", "Super sharer award", "Big heart award"], extra_head="GOLD COIN", extra_foot="for an extra-kind moment",
    extra_mini="Print on yellow paper for real gold coins. Not for children under 3 if you add small extras.",
    bye=("Happy St. Patrick's Day!", ["Today I go back to my rainbow with a pot full of your kindness.", "Thank you for every hug, every smile and every kind thing you did.", "Keep being kind all year long!"]),
    bye_sig="Love forever, your Kindness Leprechaun",
    cert=("Official rainbow award", "I Was Kind!", "for 14 days of kindness. Every leprechaun is proud of you!", "Signed: Your Kindness Leprechaun"),
    pair="Our Kindness Snowman (January), Kindness Cupid (February) and Kindness Bunny (Easter) kits follow the same 5-minute idea. Find them in our shop.",
    foot_names=dict(CUPID["foot_names"], extra="Coin cards", mid="Halfway letter"),
    labels=dict(CUPID["labels"], trk_h="Color one coin a day", meet="Meet your leprechaun"),
)

BUNNY = _spring(
    slug="kindness-bunny-kit", name="Kindness Bunny Kit", days=14,
    colors=":root{ --dark:#6b4a7a; --sage:#c06a8f; --tint:#fbeff4; --line:#f0d3e0; --accent:#e5b84a; --warm:#f6f2fb; --warmline:#e3d8ee; --cream:#fffbfd; }",
    ic="#c06a8f", sig="Love, your Kindness Bunny", fn="♥ your Kindness Bunny",
    eyebrow="Printable kit · Ages 3 to 8 · Easter", h1="Kindness<br>Bunny Kit",
    tg="A little bunny hops in with one kind mission a day for the 14 days before Easter. Kindness instead of more candy, five minutes a morning.",
    pill="18 pages · US Letter + A4", how_title="How the Kindness Bunny works",
    how_sub="For the 14 days before Easter, your child finds a note from the Kindness Bunny with one small, kind thing to do. After each one, color an egg on the tracker. On Easter morning, the bunny leaves a goodbye letter.",
    steps=[("Meet your bunny", "Any soft toy or a paper bunny can be your Kindness Bunny. Fill in the bunny passport together."),
           ("Print and cut", "Print the notes and cut them apart (4 per page). Keep them in an envelope or a little basket."),
           ("One note a day", "Leave a note out each evening, read it together in the morning."),
           ("Celebrate", "Color an egg on the tracker. On Easter, read the goodbye letter and give the \"I was kind\" certificate.")],
    tip1=("Forgot a note?", "Use the lifesaver letters: \"I hopped too far\" and \"I was painting eggs\"."),
    tip2=("Make it yours", "Use the 4 egg hunt clue cards for a kindness egg hunt on Easter morning."),
    arrive=("Hello, little friend!", ["Hop, hop! I'm a little Kindness Bunny, and I've come to help you get ready for Easter.", "For the next 14 days, I'll leave you one kind mission every morning. Every kind thing you do makes my eggs a little more colorful.", "Let's make this the kindest spring ever!"]),
    passport="My bunny passport", draw="Draw your bunny here", pp=["My bunny's name", "My bunny's favorite snack", "My name", "Day my bunny arrived"],
    tracker_sub="After each kind mission, color one egg circle. Fill all 14 before Easter!",
    life1=("I hopped too far!", ["Good morning! I hopped so far through the meadow that I got back late.", "Today's kind mission: help someone who is in a hurry. See you tomorrow!"]),
    life2=("I was painting eggs!", ["I painted eggs all night and forgot your note!", "Today's kind mission: make something colorful for someone you love. Back tomorrow!"]),
    mid=("Halfway to Easter!", ["Seven kind missions done! The meadow is full of colorful eggs thanks to you.", "Keep going, little friend!"]),
    extra_title="Kindness egg hunt clues", extra_sub="Hide a little treat or a kind note and use these clue cards on Easter morning.",
    extra_notes=["Look where we brush our teeth", "Look where the books sleep", "Look under something soft", "Look where we eat breakfast"], extra_head="EGG HUNT CLUE", extra_foot="hide a kind note or a treat here",
    extra_mini="Write your own clues on the blank notes for older kids.",
    bye=("Happy Easter!", ["Today I hop back to the meadow with a basket full of your kindness.", "Thank you for every hug, every smile and every kind thing you did.", "Keep being kind all year long!"]),
    bye_sig="Love forever, your Kindness Bunny",
    cert=("Official meadow award", "I Was Kind!", "for 14 days of kindness. Every bunny is proud of you!", "Signed: Your Kindness Bunny"),
    pair="Our Kindness Cupid (February) and Kindness Leprechaun (March) kits follow the same 5-minute idea. Find them in our shop.",
    foot_names=dict(CUPID["foot_names"], extra="Egg hunt clues", mid="Halfway letter"),
    labels=dict(CUPID["labels"], trk_h="Color one egg a day", meet="Meet your bunny"),
)
SPRING_MISSIONS = [("heart", "Tell someone in your family why you love them."), ("hug", "Give a big hug to someone who looks tired."), ("leaf", "Plant a seed or water a plant."),
    ("child", "Play with someone who is playing alone."), ("spoon", "Help set the table."), ("toy", "Share a toy you really like."), ("book", "Read a story to someone younger."),
    ("sun", "Give three people a compliment today."), ("window", "Draw a picture for a neighbor's window."), ("cat", "Be extra gentle with a pet or a teddy."),
    ("bowl", "Help clean up after dinner."), ("star", "Make a card for someone who needs cheering up."), ("leaf", "Pick up one piece of litter outside (with a grown-up)."), ("hug", "Give everyone a thank-you hug tonight.")]
SPRING_IDEAS = [x for x in CUPID["ideas"] if "Valentine" not in x and "heart" not in x.lower()] + ["Plant flower seeds together", "Make a bird feeder", "Pick a flower for someone (with permission)", "Clean up the garden toys"]
for _k in (LEPRECHAUN, BUNNY):
    _k["missions"] = SPRING_MISSIONS; _k["ideas"] = SPRING_IDEAS[:30]
KITS.update({"leprechaun": LEPRECHAUN, "bunny": BUNNY})

if __name__ == "__main__":
    for a in sys.argv[1:] or KITS:
        build(KITS[a])
