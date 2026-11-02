import sys, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
S=sys.argv[1]; E=S+'/etsy'; OUT=E+'/out'
F='/usr/share/fonts/opentype/inter/Inter-'
def font(w,sz): return ImageFont.truetype(F+w+'.otf', sz)
W,H=3000,2250
def page(path,h):
    im=Image.open(path).convert('RGB'); r=h/im.height; return im.resize((int(im.width*r),h), Image.LANCZOS)
def paste_shadow(bg,im,xy,rot=0,blur=28,off=(18,26),alpha=70):
    if rot: im=im.convert('RGBA').rotate(rot,expand=True,resample=Image.BICUBIC)
    else: im=im.convert('RGBA')
    sh=Image.new('RGBA',(im.width+200,im.height+200),(0,0,0,0))
    mask=im.split()[3].point(lambda a: alpha if a>0 else 0)
    blk=Image.new('RGBA',im.size,(40,35,30,255)); blk.putalpha(mask)
    sh.paste(blk,(100,100),blk); sh=sh.filter(ImageFilter.GaussianBlur(blur))
    bg.paste(sh,(xy[0]-100+off[0],xy[1]-100+off[1]),sh); bg.paste(im,xy,im)
def text(d,xy,s,f,fill): d.text(xy,s,font=f,fill=fill)
def hero(pages,bgc,ink,accent,title_lines,sub_lines,badge,name):
    bg=Image.new('RGB',(W,H),bgc); d=ImageDraw.Draw(bg)
    p3=page(pages[2],1500); p2=page(pages[1],1560); p1=page(pages[0],1720)
    paste_shadow(bg,p3,(360,330),rot=-6); paste_shadow(bg,p2,(290,300),rot=4); paste_shadow(bg,p1,(170,250))
    x=1800; y=520
    for i,l in enumerate(title_lines): text(d,(x,y+i*150),l,font('ExtraBold',118),ink)
    y+=len(title_lines)*150+60
    for i,l in enumerate(sub_lines): text(d,(x,y+i*82),l,font('Medium',60),ink)
    y+=len(sub_lines)*82+80
    bw=d.textlength(badge,font=font('Bold',54))+100
    d.rounded_rectangle((x,y,x+bw,y+120),60,fill=accent); text(d,(x+50,y+30),badge,font('Bold',54),'#FFFFFF')
    bg.save(f'{OUT}/{name}.jpg',quality=92)
def grid(pages,bgc,ink,title,labels,name,cols=4):
    bg=Image.new('RGB',(W,H),bgc); d=ImageDraw.Draw(bg)
    tw=d.textlength(title,font=font('ExtraBold',110)); text(d,((W-tw)/2,120),title,font('ExtraBold',110),ink)
    ph=820; pw=int(ph*0.773); gx=(W-cols*pw)//(cols+1); rows=(len(pages)+cols-1)//cols
    for i,pth in enumerate(pages):
        r,c=divmod(i,cols); x=gx+c*(pw+gx); y=330+r*(ph+150)
        paste_shadow(bg,page(pth,ph),(x,y),blur=16,off=(8,12),alpha=55)
        lw=d.textlength(labels[i],font=font('SemiBold',44)); text(d,(x+(pw-lw)/2,y+ph+30),labels[i],font('SemiBold',44),ink)
    bg.save(f'{OUT}/{name}.jpg',quality=92)
def colours(covers,names,bgc,ink,title,name):
    bg=Image.new('RGB',(W,H),bgc); d=ImageDraw.Draw(bg)
    tw=d.textlength(title,font=font('ExtraBold',110)); text(d,((W-tw)/2,110),title,font('ExtraBold',110),ink)
    ph=820; pw=int(ph*0.773); gx=(W-3*pw)//4
    for i,(pth,n) in enumerate(zip(covers,names)):
        r,c=divmod(i,3); x=gx+c*(pw+gx); y=310+r*(ph+140)
        paste_shadow(bg,page(pth,ph),(x,y),blur=16,off=(8,12),alpha=55)
        lw=d.textlength(n,font=font('SemiBold',48)); text(d,(x+(pw-lw)/2,y+ph+28),n,font('SemiBold',48),ink)
    bg.save(f'{OUT}/{name}.jpg',quality=92)
pet=[f'{E}/pet/p-{i}.png' for i in range(1,9)]
hero(pet,'#EFE9E1','#33302B','#B98A6A',['Pet Memorial','Keepsake Journal'],['8 printable pages to remember,','grieve and celebrate a beloved pet'],'Printable + GoodNotes · Letter & A4','pet-01-hero')
grid(pet,'#F6F2EC','#33302B',"What's inside – 8 pages",['Cover','About Them','How We Met','Memories','Little Ways','What I Miss','A Letter','Always With Me'],'pet-02-inside')
pp=lambda c,i: f'{E}/puppy/{c}-{i}.png'
sage='01_New-Puppy-Starter-Kit_Sage'
hero([pp(sage,1),pp(sage,2),pp(sage,4)],'#E9EFE8','#2E3B33','#556B5D',['New Puppy','Starter Kit'],['Health records, feeding & weight logs,','routine trackers and checklists'],'6 colours · Letter & A4 · GoodNotes','puppy-01-hero')
grid([pp(sage,i) for i in range(1,9)],'#F3F6F2','#2E3B33',"What's inside – 8 pages",['Cover','Puppy Profile','Vaccinations','Feeding & Weight','Potty & Routine','Vet Contacts','Shopping List','First Week'],'puppy-02-inside')
cols=['01_New-Puppy-Starter-Kit_Sage','02_New-Puppy-Starter-Kit_Blush','03_New-Puppy-Starter-Kit_DustyBlue','04_New-Puppy-Starter-Kit_Terracotta','05_New-Puppy-Starter-Kit_Greige','06_New-Puppy-Starter-Kit_Charcoal']
colours([pp(c,1) for c in cols],['Sage','Blush','Dusty Blue','Terracotta','Greige','Charcoal'],'#F5F3EF','#2E3B33','All 6 colours included','puppy-03-colours')
print(sorted(os.listdir(OUT)))
