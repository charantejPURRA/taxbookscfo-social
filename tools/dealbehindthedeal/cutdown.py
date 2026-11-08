"""Build a cutdown config from a full-episode config by picking narration beats.
usage: python3 cutdown.py <ep_module> <name> <beats,comma> <cold:0|1> "<label>" <fmt|all>
"""
import sys, types, importlib, subprocess, wave, os
import numpy as np
sys.path.insert(0, '/home/claude/deals')
import engine

def make_cut(base, beats, cold, label, name):
    SR = 48000
    vo = np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-i", base.VO, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                      capture_output=True).stdout, np.float32)
    o = base.ORDER
    def bend(b):
        i = o.index(b); return base.BT[o[i + 1]] if i + 1 < len(o) else base.VO_END
    parts, BT, SIL, t = [], {}, [], 0.0
    for b in beats:
        s, e = base.BT[b], bend(b)
        seg = vo[int(s * SR): int(e * SR)].copy(); f = int(.015 * SR)
        seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
        parts.append(seg); BT[b] = t
        for a_, b_ in base.SIL:
            if a_ >= s and b_ <= e: SIL.append([a_ - s + t, b_ - s + t])
        t += e - s
    out = np.concatenate(parts)
    path = f"/home/claude/deals/vo/{name}_vo.wav"
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(out, -1, 1) * 32767).astype(np.int16).tobytes())
    c = types.SimpleNamespace(
        SRC=base.SRC, VO=path, VO_END=len(out) / SR, TAIL=base.TAIL, EPLABEL=label, SIL=SIL,
        ORDER=list(beats), BT=BT, TEXT={b: base.TEXT[b] for b in beats},
        COLD_SHOTS=base.COLD_SHOTS if cold else [], SHOTS={b: base.SHOTS[b] for b in beats},
        CALLOUTS={k: v for k, v in base.CALLOUTS.items() if k in beats or (cold and k == "cold")})
    return c

if __name__ == "__main__":
    mod, name, beats, cold, label, fmt = sys.argv[1:7]
    base = importlib.import_module(mod)
    c = make_cut(base, beats.split(","), cold == "1", label, name)
    E = engine.Episode(c)
    wav = f"/home/claude/deals/out/{name}_audio.wav"
    if not os.path.exists(wav): E.audio(wav)
    fmts = ["9x16", "1x1", "16x9"] if fmt == "all" else [fmt]
    for f in fmts:
        E.render(f, f"/home/claude/deals/out/{name}_{f}.mp4", wav)
    print("done", name, round(E.TOTAL, 1))
