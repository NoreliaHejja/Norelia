# Amazon KDP – feltöltési csomagok

Fiók: Amazon Account ID A1BYNK4N45CETG (KDP). Connector nincs → Claude elkészíti a csomagot, Nóra tölti fel (kb. 10 perc/termék).
Szabály: puhafedeles könyv **min. 24 oldal** → a 8 oldalas printable-eket napló-könyvvé bővítjük (ismétlődő írólapok + jegyzetoldalak).
Build script: `ceg/projektek/kdp-build/kdp_build.py` (forrás PDF → 300 dpi, fehér papír, szürkeárnyalatos belív, teljes borító kifutóval).

---

## 1. A Life Well Loved – Pet Memorial Journal (paperback)

### Fájlok
| Fájl | Mi ez |
|---|---|
| `A-Life-Well-Loved_KDP_interior_8.5x11_32p.pdf` | belív, 32 oldal, 8,5×11 in, fekete-fehér, nincs kifutó (bleed: No) |
| `A-Life-Well-Loved_KDP_cover_5197x3375px.pdf` | teljes borító (hát + gerinc + előlap), 17,322×11,25 in, 0,125 in kifutóval, 300 dpi |

Oldalrend: címoldal · About My Beloved Friend · How We Met · Favourite Memories ×5 · All Their Little Ways ×3 · What I Miss Most ×5 · A Letter to You ×8 · Always With Me ×3 · Notes ×5.
A belső címoldalon és a borítón a „Printable · US Letter & A4” felirat helyett: „A keepsake journal to hold on to”.

### 1. lap – Paperback Details
| Mező | Érték |
|---|---|
| Language | English |
| Book Title | A Life Well Loved |
| Subtitle | Pet Memorial Journal and Keepsake Book to Remember, Grieve and Celebrate Your Beloved Dog or Cat |
| Series | (üres) |
| Edition | (üres) |
| Author | AureliaVenn (pen name) |
| Contributors | (üres) |
| Primary audience | Sexually explicit: No · Reading age: üres |
| Primary marketplace | Amazon.com |
| Categories (3) | Self-Help › Death, Grief & Bereavement · Pets › General · Self-Help › Journaling |
| Low-content book | ✅ **This is a low-content book** (ISBN nem kötelező) |
| Large print | No |

**Keywords (7)**
1. pet loss gifts for dog owners
2. pet memorial journal
3. dog memorial book
4. cat loss sympathy gift
5. grief journal for pet loss
6. rainbow bridge keepsake book
7. in loving memory pet remembrance

**Description**
```
A gentle place for everything you never want to forget.

A Life Well Loved is a keepsake journal to remember, grieve and celebrate a beloved dog, cat or any companion who meant the world to you. There is no right way or right time to fill it in. Take one page at a time and come back whenever you are ready.

Inside you will find:
• About My Beloved Friend – their name, nickname, breed, dates and a frame for a favourite photo
• How We Met – the day they became yours
• Favourite Memories – adventures and the silly things only they would do
• All Their Little Ways – favourite treats, nap spot, greeting, and space for a paw print or a lock of fur
• What I Miss Most – a safe place for grief
• A Letter to You – eight pages to say everything your heart needs to say
• Always With Me – how you will carry their love forward
• Extra lined pages for notes and memories

Details: 32 pages, large 8.5 × 11 inch format, matte cover, white paper.

A quiet, personal sympathy gift for a friend who has just lost their pet – or a keepsake for yourself.
```

### 2. lap – Paperback Content
| Mező | Érték |
|---|---|
| Print ISBN | low-content → nem kell (vagy ingyenes KDP ISBN) |
| Publication date | (üres) |
| Print options | Ink and paper: **Black & white interior with white paper** · Trim size: **8.5 × 11 in** · Bleed: **No bleed** · Cover finish: **Matte** |
| Manuscript | `…_interior_8.5x11_32p.pdf` |
| Book Cover | **Upload a cover you already have (print-ready PDF only)** → `…_cover_5197x3375px.pdf` |
| AI-Generated Content | **Yes** – Images: some AI-assisted design; Text: AI-assisted (a KDP kérdőívben ennek megfelelően jelölni) |
| Previewer | Launch Previewer → ellenőrizd, hogy nincs hiba; a vonalkód helye a hátlap jobb alsó sarkában üres |

### 3. lap – Rights & Pricing
| Mező | Érték |
|---|---|
| Territories | All territories (worldwide rights) |
| Primary marketplace | Amazon.com |
| Price | **$8.99** (Amazon.de: 8,99 €, Amazon.co.uk: £7.99) |
| Royalty (becslés) | 60% × 8,99 − nyomtatási költség (~2,8 $, a KDP pontosan kiírja) ≈ **2,5 $ / eladás** |
| Expanded Distribution | Off (alacsony árnál nem éri meg) |

Ár-teszt: 30 nap után 9,99 $, ha jön legalább heti 2 eladás.

---

## Következő KDP-csomagok (sorrend)
1. **New Puppy Starter Kit** → „New Puppy Journal & Health Record Book” (32–48 oldal: profil, oltások ×4, súly ×4, rutin ×8, kontaktok, bevásárlólista, jegyzet). Szezon: karácsonyi kiskutya-ajándék.
2. Karácsonyi tervező (ha előkerül a fájl) → csak dec. 10-ig érdemes.
3. Kutyatenyésztő alom-tracker → „Dog Breeder Litter Record Book” (niche, kevés verseny).
