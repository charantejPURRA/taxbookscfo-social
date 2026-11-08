"""prep_vo.py <in.mp3> <out_prefix> <n_beats> [start end]
Takes one clean take (optionally a [start,end] window of the download), finds the n_beats-1 longest
pauses as beat boundaries, tightens all pauses (>=0.9s -> 0.65, 0.45-0.9 -> 0.42), and writes
<out_prefix>_vo.wav plus <out_prefix>_beats.json (BT, VO_END, SIL) for the episode config."""
import sys, json, subprocess, re, wave
import numpy as np
src, pre, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
SR = 48000
x = np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-i", src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True).stdout, np.float32).copy()
if len(sys.argv) > 5: x = x[int(float(sys.argv[4]) * SR): int(float(sys.argv[5]) * SR)]
w = int(.02 * SR); e = np.sqrt(np.mean(x[:len(x) // w * w].reshape(-1, w) ** 2, 1)); db = 20 * np.log10(e + 1e-7)
quiet = db < (np.percentile(db, 90) - 32)
sil = []; i = 0
while i < len(quiet):
    if quiet[i]:
        j = i
        while j < len(quiet) and quiet[j]: j += 1
        a, b = i * .02, j * .02
        if b - a >= .3 and a > 0.05 and j < len(quiet): sil.append([a, b])
        i = j
    else: i += 1
import os, importlib
EPM = os.environ.get("EPMOD")
if EPM:
    sys.path.insert(0, "/home/claude/deals")
    m = importlib.import_module(EPM)
    L = [len(m.TEXT[b]) for b in m.ORDER]
    tot = len(x) / SR; cum, E = 0, []
    for l in L[:-1]:
        cum += l; E.append(tot * cum / sum(L))
    C = sil; K = len(C); INF = 1e18
    def cost(j, i):
        mid = (C[i][0] + C[i][1]) / 2; d = C[i][1] - C[i][0]
        return (mid - E[j]) ** 2 - 6.0 * d
    # DP: f[j][i] = best cost placing boundary j at candidate i
    f = [[INF] * K for _ in E]; bk = [[-1] * K for _ in E]
    for i in range(K): f[0][i] = cost(0, i)
    for j in range(1, len(E)):
        best, bi = INF, -1
        for i in range(K):
            if i > 0 and f[j-1][i-1] < best: best, bi = f[j-1][i-1], i-1
            if bi >= 0: f[j][i] = best + cost(j, i); bk[j][i] = bi
    i = min(range(K), key=lambda k: f[-1][k]); idx = []
    for j in range(len(E) - 1, -1, -1): idx.append(i); i = bk[j][i]
    bounds = [C[k] for k in reversed(idx)]
else:
    bounds = sorted(sorted(sil, key=lambda s: s[1] - s[0], reverse=True)[: n - 1])
out, t, last, newsil, BT = [], 0.0, 0.0, [], [0.0]
def cap(d): return 0.65 if d >= .9 else (0.42 if d >= .45 else d)
for a, b in sil:
    seg = x[int(last * SR): int(a * SR)]; out.append(seg); t += len(seg) / SR
    d = cap(b - a); out.append(np.zeros(int(d * SR), np.float32)); newsil.append([round(t, 2), round(t + d, 2)]); t += d
    if [a, b] in bounds: BT.append(round(t, 2))
    last = b
seg = x[int(last * SR):]
k = len(seg) - 1
while k > 0 and abs(seg[k]) < 1e-3: k -= 1
seg = seg[: k + int(.15 * SR)]; out.append(seg); t += len(seg) / SR
y = np.concatenate(out)
with wave.open(f"{pre}_vo.wav", "wb") as f:
    f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
print("beats", len(BT), BT, "dur", round(t, 2))
json.dump({"BT_LIST": BT, "VO_END": round(t, 2), "SIL": newsil}, open(f"{pre}_beats_raw.json", "w"))
