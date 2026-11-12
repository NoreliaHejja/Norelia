"""Közös építőelemek az etsy-empire termékekhez (design: assets/base.css)."""

P = {  # stroke-alapú, 24×24 ikonok
 "wash": '<path d="M12 3c3 4 5 6.5 5 9a5 5 0 0 1-10 0c0-2.5 2-5 5-9z"/>',
 "count": '<path d="M5 6h3v12M5 18h6M14 6h4l-4 6h4v6h-4"/>',
 "stack": '<path d="M12 3v18"/><circle cx="12" cy="7" r="2.5"/><circle cx="12" cy="13" r="2.5"/>',
 "mash": '<path d="M6 13h12l-1.5 6h-9z"/><path d="M12 3v7M9 10h6"/>',
 "stir": '<path d="M5 12h14l-2 7H7z"/><path d="M14 4l-3 9"/>',
 "shape": '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>',
 "spread": '<path d="M4 16l10-10 4 4-10 10H4z"/><path d="M12 8l4 4"/>',
 "sprinkle": '<circle cx="7" cy="7" r="1"/><circle cx="12" cy="5" r="1"/><circle cx="17" cy="8" r="1"/><circle cx="9" cy="12" r="1"/><circle cx="15" cy="13" r="1"/><path d="M4 19h16"/>',
 "wait": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "pour": '<path d="M5 5h9v6a4 4 0 0 1-4 4H9a4 4 0 0 1-4-4z"/><path d="M14 7h2a2 2 0 0 1 0 4h-2M8 18v3"/>',
 "press": '<circle cx="12" cy="12" r="4"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/>',
 "sort": '<circle cx="6" cy="7" r="2.5"/><circle cx="18" cy="7" r="2.5"/><circle cx="12" cy="17" r="2.5"/>',
 "dip": '<path d="M4 14h16l-2 6H6z"/><path d="M14 3l-4 9"/>',
 "roll": '<rect x="4" y="9" width="16" height="6" rx="3"/><path d="M8 9v6M16 9v6"/>',
 "crack": '<path d="M12 3c-4 0-6 6-6 10a6 6 0 0 0 12 0c0-4-2-10-6-10z"/><path d="M8 11l2 2 2-2 2 2 2-2"/>',
 "star": '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/>',
 "book": '<path d="M4 5h9a3 3 0 0 1 3 3v11a2.5 2.5 0 0 0-2.5-2.5H4z"/><path d="M20 5h-4a3 3 0 0 0-3 3v11a2.5 2.5 0 0 1 2.5-2.5H20z"/>',
 "spoon": '<ellipse cx="12" cy="7" rx="4" ry="5"/><path d="M12 12v9"/>',
 "cart": '<path d="M3 4h2l2 11h11l2-8H6"/><circle cx="9" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "leaf": '<path d="M5 19c0-8 6-14 15-14 0 9-6 15-14 15"/><path d="M5 19l8-8"/>',
 "check": '<path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/>',
 "fridge": '<rect x="6" y="3" width="12" height="18" rx="2"/><path d="M6 10h12M9 6v2M9 13v3"/>',
 "child": '<circle cx="12" cy="6" r="3"/><path d="M7 21v-6a5 5 0 0 1 10 0v6"/>',
}

P.update({
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',
 "moon": '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
 "tooth": '<path d="M7 3c-2 0-3 2-3 4 0 3 1 4 1.5 7S6 21 8 21s1.5-5 4-5 2 5 4 5 2-4 2.5-7S20 10 20 7c0-2-1-4-3-4-2 0-3 1-5 1S9 3 7 3z"/>',
 "bed": '<path d="M3 18V8M3 14h18v4M21 18v-4a3 3 0 0 0-3-3h-7v3"/><circle cx="7" cy="11" r="2"/>',
 "shirt": '<path d="M8 3l-5 3 2 4 3-1v12h8V9l3 1 2-4-5-3a4 4 0 0 1-8 0z"/>',
 "bath": '<path d="M4 12h16v3a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M6 12V6a2 2 0 0 1 4 0"/>',
 "bowl": '<path d="M4 12h16a8 8 0 0 1-16 0z"/><path d="M9 8c0-2 2-2 2-4M14 8c0-2 2-2 2-4"/>',
 "hug": '<circle cx="12" cy="7" r="3"/><path d="M5 21c0-4 3-7 7-7s7 3 7 7"/><path d="M8 15l-3 3M16 15l3 3"/>',
 "cat": '<path d="M5 10l1-6 4 3h4l4-3 1 6v4a7 7 0 0 1-14 0z"/><circle cx="9.5" cy="12" r=".8" fill="#4f6b58"/><circle cx="14.5" cy="12" r=".8" fill="#4f6b58"/>',
 "toy": '<path d="M4 20c4-4 6-8 6-12"/><circle cx="13" cy="5" r="2"/><path d="M14.5 6.5l4 4"/>',
 "heart": '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>',
 "scale": '<rect x="4" y="5" width="16" height="15" rx="3"/><path d="M9 10a3 3 0 0 1 6 0M12 10l1-2"/>',
 "window": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M12 3v18M4 12h16"/>',
 "potty": '<path d="M7 4h10v6H7zM5 10h14a7 7 0 0 1-14 0z"/>',
 "shoe": '<path d="M3 15c0-3 2-6 4-6l3 3h4l6 3v3H3z"/>',
})
ICONS = P


def icon(name, size=22, color="#4f6b58", sw=1.6):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{P[name]}</svg>')


def page_head(eyebrow, title, ic):
    return (f'<div class="pagehead"><div class="icon-circle">{icon(ic)}</div>'
            f'<div><div class="eyebrow">{eyebrow}</div><h1 class="page-title">{title}</h1></div></div>')


def footer(name, right):
    return f'<div class="footer"><span class="fp">{name}</span><span>{right}</span></div>'


def cover(name, tag, eyebrow, foot, ic):
    big = icon(ic, 120, sw=1.3)
    return (f'<div class="page cover"><div class="medallion">{big}</div><div class="eyebrow">{eyebrow}</div>'
            f'<h1>{name}</h1><div class="tag">{tag}</div><div class="accent-line"></div><div class="foot">{foot}</div></div>')
