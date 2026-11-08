import subprocess, sys, json
from PIL import Image, ImageDraw, ImageFont
f=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf',15)
src=sys.argv[1]; wins=json.loads(sys.argv[2]); out=sys.argv[3]; step=float(sys.argv[4]) if len(sys.argv)>4 else 1.0
tiles=[]
for a,b in wins:
    subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',str(a),'-t',str(b-a),'-i',src,'-vf',f'fps={1/step},scale=176:99','/tmp/st_%03d.jpg'])
    i=0
    while True:
        try: im=Image.open(f'/tmp/st_{i+1:03d}.jpg').copy()
        except: break
        if a+i*step>=b: break
        d=ImageDraw.Draw(im); t=a+i*step; d.rectangle([0,0,58,18],fill=(0,0,0)); d.text((2,1),f"{t:.1f}",font=f,fill=(255,220,0)); tiles.append(im); i+=1
    subprocess.run('rm -f /tmp/st_*.jpg',shell=True)
cols=12; s=Image.new('RGB',(176*cols,99*((len(tiles)+cols-1)//cols)))
for i,im in enumerate(tiles): s.paste(im,((i%cols)*176,(i//cols)*99))
s.save(out,quality=82); print(len(tiles))
