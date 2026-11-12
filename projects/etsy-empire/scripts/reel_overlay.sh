#!/usr/bin/env bash
# Emily reel: 9:16 1080x1920, felül hook (2 sor), 2,5 mp-től alul "Printable - link in bio" sáv.
# Használat: scripts/reel_overlay.sh be.mp4 ki.mp4 "Hook 1. sor" "Hook 2. sor" ["CTA (alap: Printable - link in bio)"]
set -e
F=/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf
ffmpeg -y -v error -i "$1" -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,drawbox=x=90:y=70:w=900:h=230:color=white@0.9:t=fill,drawtext=fontfile=$F:text='$3':fontsize=62:fontcolor=0x1F2A44:x=(w-tw)/2:y=110,drawtext=fontfile=$F:text='$4':fontsize=62:fontcolor=0xE4572E:x=(w-tw)/2:y=200,drawbox=x=0:y=1640:w=1080:h=170:color=0xE4572E@0.95:t=fill:enable='gte(t,2.5)',drawtext=fontfile=$F:text='${5:-Printable - link in bio}':fontsize=60:fontcolor=white:x=(w-tw)/2:y=1700:enable='gte(t,2.5)'" -c:v libx264 -pix_fmt yuv420p -an -movflags +faststart "$2"
echo "OK $2"
