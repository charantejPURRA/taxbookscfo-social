import sys, json, os, importlib
sys.path.insert(0, '/home/claude/deals')
mod = sys.argv[1]; name = mod.replace("ep_", "")
c = importlib.import_module(mod)
# fake beats proportional to text length (~14.5 chars/sec)
BT, t = {}, 0.0
for b in c.ORDER: BT[b] = t; t += len(c.TEXT[b]) / 14.5 + 0.6
c.BT, c.VO_END, c.SIL = BT, t, []
c.VO = "/home/claude/deals/vo/wicked_vo.wav"
import engine
from PIL import Image
E = engine.Episode(c)
ts = [E.COLD * 0.4, E.COLD * 0.85] + [E.COLD + BT[b] + (c.TEXT[b] and len(c.TEXT[b]) / 14.5 * 0.7) for b in c.ORDER]
p = E.stills("9x16", ts, f"/tmp/pv_{name}")
ims = [Image.open(x).resize((216, 384)) for x in p]
cols = 6; s = Image.new("RGB", (216 * cols, 384 * ((len(ims) + cols - 1) // cols)))
for i, im in enumerate(ims): s.paste(im, ((i % cols) * 216, (i // cols) * 384))
s.save(f"/home/claude/deals/pv_{name}.jpg", quality=85)
print("ok", name)
