import sys, subprocess
from PIL import Image
src, out = sys.argv[1], sys.argv[2]; ts = [float(x) for x in sys.argv[3].split(",")]
ims = []
for i, t in enumerate(ts):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", "-vf", "crop=1920:190:0:830", f"/tmp/cap_{i}.png"])
    ims.append(Image.open(f"/tmp/cap_{i}.png").copy())
s = Image.new("RGB", (1920, 190 * len(ims)))
for i, im in enumerate(ims): s.paste(im, (0, 190 * i))
s.resize((1200, int(190 * len(ims) * 1200 / 1920))).save(out)
