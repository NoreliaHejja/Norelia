import sys
from PIL import Image, ImageDraw, ImageFont
S=sys.argv[1]; K=S+'/kdp'
def load(i):
    im=Image.open(f'{K}/src/p-{i}.png').convert('RGB')
    if i==1:  # replace 'Printable · US Letter & A4' tagline (print book)
        d=ImageDraw.Draw(im); g=Image.new('L',(1,1))
        for y in range(2850,2960):
            c=im.getpixel((300,y)); d.line((0,y,im.width,y),fill=c)
        f=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-SemiBold.otf',44)
        t='A keepsake journal to hold on to'; tw=d.textlength(t,font=f)
        d.text(((im.width-tw)/2,2875),t,font=f,fill=(110,104,96))
    return im
def whiten(im, thr=244):
    # paper tint -> pure white (no tinted page edges in print), keep ink
    g=im.convert('L')
    mask=g.point(lambda v:255 if v>=thr else 0)
    white=Image.new('RGB',im.size,(255,255,255)); im=im.copy(); im.paste(white,(0,0),mask); return im
ref=load(7); line_col=ref.getpixel((1275,664))
def notes():
    im=Image.new('RGB',(2550,3300),(255,255,255)); d=ImageDraw.Draw(im)
    y=420
    while y<2960: d.rectangle((240,y,2310,y+2),fill=line_col); y+=106
    return im
P={i:whiten(load(i), 222 if i==1 else 244) for i in range(1,9)}
order=[1,2,3]+[4]*5+[5]*3+[6]*5+[7]*8+[8]*3
pages=[P[i] for i in order]+[whiten(notes()) for _ in range(5)]
assert len(pages)==32, len(pages)
gray=[p.convert('L').convert('RGB') for p in pages]   # B&W interior = cheaper print
gray[0].save(f'{K}/A-Life-Well-Loved_KDP_interior_8.5x11_32p.pdf',save_all=True,append_images=gray[1:],resolution=300)
# ---- Cover (paperback, white paper, no-bleed interior; cover with 0.125in bleed)
DPI=300; trim_w,trim_h=8.5,11; bleed=0.125; spine=32*0.002252
W=round((2*trim_w+spine+2*bleed)*DPI); H=round((trim_h+2*bleed)*DPI)
cov=Image.new('RGB',(W,H),(240,234,226))
front=load(1); fw=round((trim_w+bleed)*DPI); scale=max(fw/front.width,H/front.height)
fr=front.resize((round(front.width*scale),round(front.height*scale)),Image.LANCZOS)
fx=W-fw; cov.paste(fr.crop((0,(fr.height-H)//2,fw,(fr.height-H)//2+H)),(fx,0))
d=ImageDraw.Draw(cov); F='/usr/share/fonts/opentype/inter/Inter-'
ink=(51,48,43); acc=(185,138,106)
bx=round((bleed+0.75)*DPI); by=round((bleed+1.6)*DPI)
d.text((bx,by),'A gentle place for everything',font=ImageFont.truetype(F+'Bold.otf',96),fill=ink)
d.text((bx,by+125),'you never want to forget.',font=ImageFont.truetype(F+'Bold.otf',96),fill=ink)
body=['A keepsake journal to remember, grieve and celebrate','a beloved dog, cat or any companion who meant the','world to you. Fill it in slowly, at your own pace.','','Inside:','•  About my beloved friend – details and a favourite photo','•  How we met and our favourite memories','•  All their little ways – with space for a paw print','•  What I miss most, and letters to them','•  Always with me – carrying their love forward','•  Extra pages for notes and memories','','32 pages · 8.5 × 11 in']
f=ImageFont.truetype(F+'Regular.otf',50)
for i,l in enumerate(body): d.text((bx,by+330+i*78),l,font=f,fill=ink)
d.rectangle((bx,by+330+len(body)*78+60,bx+150,by+330+len(body)*78+66),fill=acc)
d.text((bx,by+330+len(body)*78+100),'AureliaVenn',font=ImageFont.truetype(F+'SemiBold.otf',56),fill=ink)
# barcode safe area (KDP places it bottom-right of back cover): keep empty, outline only in proof copy
cov.save(f'{K}/A-Life-Well-Loved_KDP_cover_{W}x{H}px.pdf',resolution=DPI)
cov.resize((W//4,H//4)).save(f'{K}/cover-preview.jpg',quality=85)
print('cover in', (2*trim_w+spine+2*bleed), 'x', trim_h+2*bleed, 'px', W, H)
