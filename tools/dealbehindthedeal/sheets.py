import subprocess, sys, glob, os
from PIL import Image, ImageDraw, ImageFont
f=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf',22)
name=sys.argv[1]; step=float(sys.argv[2]) if len(sys.argv)>2 else 5
os.makedirs(f'th_{name}',exist_ok=True)
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'{name}.mp4','-vf',f'fps=1/{step},scale=320:180',f'th_{name}/t_%03d.jpg'])
fs=sorted(glob.glob(f'th_{name}/t_*.jpg')); per=42
for s in range(0,len(fs),per):
    sheet=Image.new('RGB',(320*6,180*7))
    for i,fp in enumerate(fs[s:s+per]):
        im=Image.open(fp); d=ImageDraw.Draw(im); t=int((s+i)*step)
        d.rectangle([0,0,80,28],fill=(0,0,0)); d.text((4,2),f"{t//60}:{t%60:02d}",font=f,fill=(255,220,0))
        sheet.paste(im,((i%6)*320,(i//6)*180))
    sheet.save(f'sheet_{name}_{s//per}.jpg',quality=82)
print(name,len(fs))
