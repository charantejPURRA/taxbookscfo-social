import sys, subprocess, numpy as np
src = sys.argv[1]
W, H = 192, 108
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", src, "-vf", f"fps=2,scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3).astype(int)
band = fr[:, 88:98, 30:110]           # lower-third caption band
score = (band[..., 2] - band[..., 0]).mean((1, 2))  # blue minus red
hits = [i / 2 for i, s in enumerate(score) if s > 45]
# group runs
runs = []
for t in hits:
    if runs and t - runs[-1][1] <= 1.0: runs[-1][1] = t
    else: runs.append([t, t])
print([(a, b) for a, b in runs if b - a >= 1.0])
