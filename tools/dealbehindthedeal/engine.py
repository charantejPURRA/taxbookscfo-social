"""TaxBooksCFO 'Deal Behind the Deal' engine: one episode config -> 9:16, 1:1, 16:9 renders.
Episode config provides: SRC, VO, VO_END, COLD (list of (src_start, dur, mode)), BT (beat start in VO time),
ORDER, TEXT (narration per beat), SHOTS (beat -> [(src_start, dur, mode)]), CALLOUTS (beat -> [(frac, kind, payload)]),
SIL (silences in VO), EPLABEL, TAIL (seconds after VO before end card)."""
import sys, os, subprocess, wave, json, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FPS = 30
NAVY = (10, 26, 47); ORANGE = (217, 98, 43); PEACH = (244, 162, 122); WHITE = (255, 255, 255)
MUTED = (176, 188, 206); SLATE = (58, 82, 117)
A = "/mnt/user-data/uploads/taxbookscfo-content-agent/assets/fonts/"
_fc = {}
def SERIF(sz, it=False):
    sz = max(8, int(sz)); k = ("s", sz, it)
    if k not in _fc: _fc[k] = ImageFont.truetype(A + ("DMSerifDisplay-Italic.ttf" if it else "DMSerifDisplay-Regular.ttf"), sz)
    return _fc[k]
def SANS(sz, wt=600):
    sz = max(8, int(sz)); k = ("a", sz, wt)
    if k not in _fc:
        f = ImageFont.truetype(A + "SourceSans3.ttf", sz); f.set_variation_by_axes([wt]); _fc[k] = f
    return _fc[k]
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def eo(t): t = clamp(t); return 1 - (1 - t) ** 3
def P(t, s, d=0.45): return eo((t - s) / d)

STYLE = {"w": (WHITE, False), "o": (ORANGE, False), "oi": (ORANGE, True), "wi": (WHITE, True), "p": (PEACH, False), "m": (MUTED, False)}

FORMATS = {
    "9x16": dict(W=1080, H=1920, s=1.0, zx=64, zy=1170, zw=952, capy=1700, capsz=46, band_cy=820, band_w=1274, chrome=1.0),
    "1x1":  dict(W=1080, H=1080, s=0.6, zx=48, zy=600, zw=984, capy=992, capsz=32, band_cy=330, band_w=1080, chrome=0.72),
    "16x9": dict(W=1920, H=1080, s=0.62, zx=72, zy=540, zw=1150, capy=990, capsz=36, band_cy=0, band_w=0, chrome=0.72),
}

class Fmt:
    def __init__(self, name):
        self.name = name; f = FORMATS[name]; self.__dict__.update(f)
        W, H = self.W, self.H
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        top = np.clip(1 - yy / (0.17 * H), 0, 1) * 0.6
        if name == "16x9":
            bot = np.clip((yy - 0.38 * H) / (0.5 * H), 0, 1) ** 1.1 * 0.9
            left = np.clip(1.25 - xx / (0.7 * W), 0, 1)
            m = np.maximum(top, bot * np.maximum(left, 0.35))
        else:
            start = 0.56 if name == "9x16" else 0.42
            bot = np.clip((yy - start * H) / (0.3 * H), 0, 1) ** 1.2 * 0.9
            m = np.maximum(top, bot)
        self.mask = m[..., None]
        self.navy = np.array(NAVY, np.float32)
        self.grid = self._grid()
    def _grid(self):
        W, H = self.W, self.H
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        img = np.zeros((H, W, 3), np.float32) + np.array(NAVY, np.float32)
        d = np.sqrt((xx - W * 0.95) ** 2 + (yy - 60) ** 2); g = np.clip(1 - d / (0.85 * max(W, H) * 0.55), 0, 1) ** 2 * 0.55
        img = img * (1 - g[..., None]) + np.array((150, 80, 45), np.float32) * g[..., None]
        im = Image.fromarray(img.astype(np.uint8)); dr = ImageDraw.Draw(im, "RGBA")
        step = int(72 * max(self.s, 0.7))
        for x in range(0, W, step): dr.line([(x, 0), (x, H)], fill=(255, 255, 255, 10))
        for y in range(0, H, step): dr.line([(0, y), (W, y)], fill=(255, 255, 255, 10))
        return im

    def compose(self, fr, mode, zoom=1.0):
        W, H = self.W, self.H
        if mode == "fit" and self.name != "16x9":
            bg = fr.resize((240, 135)).filter(ImageFilter.GaussianBlur(6))
            bw = int(1920 * H / 1080); bg = bg.resize((bw, H), Image.BILINEAR)
            x = (bw - W) // 2; im = bg.crop((x, 0, x + W, H))
            im = Image.blend(im, Image.new("RGB", (W, H), NAVY), 0.45)
            fw = int(self.band_w * zoom); fh = int(fw * 9 / 16)
            im.paste(fr.resize((fw, fh), Image.BILINEAR), ((W - fw) // 2, int(self.band_cy - fh / 2)))
        else:
            h = int(H * zoom); w = int(1920 * h / 1080)
            if w < W: w = int(W * zoom); h = int(1080 * w / 1920)
            big = fr.resize((w, h), Image.BILINEAR)
            x = (w - W) // 2; y = (h - H) // 2
            im = big.crop((x, y, x + W, y + H))
        a = np.asarray(im, np.float32)
        a = a * (1 - self.mask) + self.navy * self.mask
        return Image.fromarray(a.astype(np.uint8))

# ---------- text drawing with true alpha ----------
def draw_parts(img, d, x, y, parts, size_fn, a, rise=0.0):
    a = clamp(a)
    if a <= 0.01: return
    fonts = [size_fn(st) for _, st in parts]
    asc = max(f.getmetrics()[0] for f in fonts)
    by = y + asc + (1 - a) * rise
    for (s, st), f in zip(parts, fonts):
        col = STYLE[st][0]
        if a >= 0.99:
            d.text((x, by), s, font=f, fill=col, anchor="ls")
        else:
            l, t, r, b = d.textbbox((x, by), s, font=f, anchor="ls")
            l, t, r, b = int(l) - 2, int(t) - 2, int(r) + 2, int(b) + 2
            m = Image.new("L", (max(1, r - l), max(1, b - t)), 0)
            ImageDraw.Draw(m).text((x - l, by - t), s, font=f, fill=int(255 * a), anchor="ls")
            img.paste(col, (l, t), m)
        x += d.textlength(s, font=f)

def parts_width(d, parts, size_fn):
    return sum(d.textlength(s, font=size_fn(st)) for s, st in parts)

KIND = {  # base size (at s=1), font family, line height multiplier
    "label": (32, "sans750", 1.45), "big": (124, "serif", 1.12), "line": (72, "serif", 1.22),
    "sub": (42, "sans650", 1.4), "slam": (132, "serif", 1.12), "note": (24, "sans500", 1.5),
}
def font_for(kind, size, st):
    fam = KIND[kind][1]; it = STYLE[st][1]
    if fam == "serif": return SERIF(size, it)
    return SANS(size, int(fam[4:]))

def layout_callouts(fmt, img, d, items, t_beat, beat_dur):
    """items: [(frac, kind, payload)] stacked from the zone top; each appears at frac*beat_dur."""
    y = fmt.zy; s = fmt.s
    for frac, kind, payload in items:
        st0 = frac * beat_dur; a = P(t_beat, st0)
        if kind in KIND:
            parts = payload if isinstance(payload, list) else [(payload, "o" if kind == "label" else "w")]
            size = KIND[kind][0] * s
            if kind == "slam" and t_beat > st0:
                k = eo((t_beat - st0) / 0.15); size = size * (1 + 0.18 * (1 - k)); a = 1.0 if t_beat > st0 else 0
            while parts_width(d, parts, lambda st_: font_for(kind, size, st_)) > fmt.zw and size > 10: size *= 0.94
            draw_parts(img, d, fmt.zx, y, parts, lambda st_: font_for(kind, size, st_), a, 18 * s)
            y += KIND[kind][0] * s * KIND[kind][2]
        elif kind == "card":
            title, parts = payload
            h = 250 * s
            if a > 0.01:
                d.rounded_rectangle([fmt.zx - 16 * s, y, fmt.zx + fmt.zw, y + h], radius=int(22 * s),
                                    fill=(10, 26, 47, int(225 * a)), outline=(ORANGE[0], ORANGE[1], ORANGE[2], int(230 * a)), width=max(2, int(3 * s)))
                draw_parts(img, d, fmt.zx + 28 * s, y + 26 * s, [(title, "m")], lambda st_: SANS(36 * s, 650), a)
                size = 104 * s
                while parts_width(d, parts, lambda st_: SERIF(size, STYLE[st_][1])) > fmt.zw - 60 * s and size > 10: size *= 0.94
                draw_parts(img, d, fmt.zx + 28 * s, y + 82 * s, parts, lambda st_: SERIF(size, STYLE[st_][1]), a, 10 * s)
            y += h + 30 * s
        elif kind == "chips":
            x = fmt.zx; f = SANS(40 * s, 750)
            for i, c in enumerate(payload):
                ai = P(t_beat, st0 + i * 0.35)
                w_ = d.textlength(c, font=f) + 56 * s
                if ai > 0.01:
                    d.rounded_rectangle([x, y, x + w_, y + 72 * s], radius=int(36 * s), fill=(ORANGE[0], ORANGE[1], ORANGE[2], int(255 * ai)))
                    draw_parts(img, d, x + 28 * s, y + 12 * s, [(c, "w")], lambda st_: f, ai)
                x += w_ + 16 * s
            y += 72 * s + 30 * s
        elif kind == "gap":
            y += payload * s

def chrome(fmt, img, d, g, total, eplabel):
    W = fmt.W; c = fmt.chrome
    d.rectangle([0, 0, W, int(6 * c)], fill=(255, 255, 255, 40))
    d.rectangle([0, 0, int(W * clamp(g / total)), int(6 * c)], fill=ORANGE)
    x = 64 * c
    draw_parts(img, d, x, 72 * c, [("TaxBooks", "w"), ("CFO", "o")], lambda st_: SERIF(46 * c), 1.0)
    f = SANS(24 * c, 650); lab = eplabel
    w_ = d.textlength(lab, font=f)
    d.text((W - 64 * c - w_, 90 * c), lab, font=f, fill=(255, 255, 255, 220))

def caption(fmt, d, text):
    f = SANS(fmt.capsz, 750); tw = d.textlength(text, font=f)
    while tw > fmt.W * 0.9:
        f = SANS(f.size * 0.94, 750); tw = d.textlength(text, font=f)
    x = (fmt.W - tw) / 2; y = fmt.capy
    d.text((x + 2, y + 3), text, font=f, fill=(0, 0, 0)); d.text((x, y), text, font=f, fill=WHITE)

# ---------- end card ----------
def endcard(fmt, t):
    W, H = fmt.W, fmt.H; im = fmt.grid.copy(); d = ImageDraw.Draw(im, "RGBA")
    k = min(1.0, H / 1920 * 1.0) if fmt.name == "9x16" else 0.58
    cy = H / 2; Y = lambda y: cy + (y - 1055) * k
    def center(y, parts, size_fn, a, rise=14):
        w_ = parts_width(d, parts, size_fn); draw_parts(im, d, (W - w_) / 2, Y(y), parts, size_fn, a, rise * k)
    d.rectangle([0, 0, W, int(6 * fmt.chrome)], fill=ORANGE)
    a = P(t, 0.0); s = 168 * k; x0 = (W - s) / 2; y0 = Y(470) + (1 - a) * 30 * k
    if a > 0.01:
        d.rounded_rectangle([x0, y0, x0 + s, y0 + s], radius=int(18 * k), fill=(ORANGE[0], ORANGE[1], ORANGE[2], int(255 * a)))
        f = SANS(64 * k, 750); tw = d.textlength("TBC", font=f); draw_parts(im, d, (W - tw) / 2, y0 + 44 * k, [("TBC", "w")], lambda st_: f, a)
    center(700, [("TaxBooks", "w"), ("CFO", "o")], lambda st_: SERIF(110 * k), P(t, 0.25), 20)
    center(850, [("TAX · ACCOUNTING · CFO ADVISORY · TRANSACTIONS", "m")], lambda st_: SANS(28 * k, 700), P(t, 0.45), 8)
    p = P(t, 0.6, 0.5)
    if p > 0: d.rectangle([W / 2 - 220 * k * p, Y(930), W / 2 + 220 * k * p, Y(934)], fill=ORANGE)
    center(990, [("We don't recap the pitch.", "w")], lambda st_: SERIF(64 * k), P(t, 0.8))
    center(1075, [("We follow the ", "w"), ("money.", "oi")], lambda st_: SERIF(64 * k, STYLE[st_][1]), P(t, 1.0))
    a3 = P(t, 1.4, 0.4)
    if a3 > 0.01:
        bw, bh = 760 * k, 120 * k; bx = (W - bw) / 2; by = Y(1250)
        d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=int(60 * k), fill=(ORANGE[0], ORANGE[1], ORANGE[2], int(255 * a3)))
        f = SANS(46 * k, 750); tw = d.textlength("Buying or selling a business?", font=f)
        draw_parts(im, d, (W - tw) / 2, by + 30 * k, [("Buying or selling a business?", "w")], lambda st_: f, a3)
    center(1410, [("Talk with an advisor at ", "w"), ("taxbookscfo.com", "p")], lambda st_: SANS(40 * k, 800 if st_ == "p" else 550), P(t, 1.7), 10)
    center(1560, [("FOLLOW FOR THE NEXT DEAL AUTOPSY", "o")], lambda st_: SANS(30 * k, 800), P(t, 2.1), 8)
    center(1610, [("LinkedIn · Instagram · Facebook · YouTube · X", "m")], lambda st_: SANS(34 * k, 600), P(t, 2.1), 8)
    return im
ENDCARD = 3.6

# ---------- episode runtime ----------
class Reader:
    def __init__(self, src, s, dur):
        self.last = None
        self.p = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-ss", str(s), "-t", str(dur + 1), "-i", src, "-an",
                                   "-vf", f"fps={FPS},scale=1920:1080", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    def next(self):
        b = self.p.stdout.read(1920 * 1080 * 3)
        if len(b) == 1920 * 1080 * 3: self.last = Image.frombuffer("RGB", (1920, 1080), b)
        return self.last
    def close(self): self.p.kill()

class Episode:
    def __init__(self, cfg):
        self.c = cfg
        self.COLD = sum(x[1] for x in cfg.COLD_SHOTS)
        self.VO_START = self.COLD
        self.VO_DUR = cfg.VO_END
        self.TOTAL = self.COLD + cfg.VO_END + cfg.TAIL + ENDCARD
        self.tl = self.timeline(); self.caps = self.captions()
    def bend(self, b):
        o = self.c.ORDER; i = o.index(b)
        return self.c.BT[o[i + 1]] if i + 1 < len(o) else self.c.VO_END
    def timeline(self):
        c = self.c; tl = []; g = 0.0
        for s, d, m in c.COLD_SHOTS: tl.append((g, d, s, m, "cold")); g += d
        for b in c.ORDER:
            st = self.COLD + c.BT[b]; en = self.COLD + self.bend(b) + (c.TAIL if b == c.ORDER[-1] else 0)
            shots = c.SHOTS[b]; tot = sum(x[1] for x in shots); k = min(1.0, (en - st) / tot); g = st
            for j, (s, d, m) in enumerate(shots):
                dd = d * k if j < len(shots) - 1 else en - g
                tl.append((g, dd, s, m, b)); g += dd
                if g >= en - 1e-3: break
        tl.append((self.COLD + c.VO_END + c.TAIL, ENDCARD, None, "end", "end"))
        return tl
    def captions(self):
        c = self.c; out = []
        for b in c.ORDER:
            st, en = c.BT[b], self.bend(b)
            words = c.TEXT[b].split(); chunks, cur = [], []
            for w_ in words:
                cur.append(w_)
                if len(cur) >= 5 or (w_.endswith((".", "?", ",", ":")) and len(cur) >= 2): chunks.append(" ".join(cur)); cur = []
            if cur: chunks.append(" ".join(cur))
            sp, t0 = [], st
            for a_, b_ in c.SIL:
                if b_ <= st or a_ >= en: continue
                if a_ > t0: sp.append((t0, min(a_, en)))
                t0 = max(t0, b_)
            if t0 < en: sp.append((t0, en))
            speech = sum(b_ - a_ for a_, b_ in sp); tot = sum(len(x) for x in chunks)
            def at(x):
                for a_, b_ in sp:
                    if x <= b_ - a_: return a_ + x
                    x -= b_ - a_
                return en
            acc = 0
            for ch in chunks:
                s0 = at(speech * acc / tot); acc += len(ch); s1 = at(speech * acc / tot)
                out.append((self.COLD + s0, self.COLD + max(s1, s0 + 0.5), ch))
        return out

    def frame(self, fmt, g, st):
        idx = max(i for i, x in enumerate(self.tl) if x[0] <= g + 1e-6)
        g0, dur, s, mode, seg = self.tl[idx]; lt = g - g0
        if seg == "end":
            return endcard(fmt, lt)
        if st.get("idx") != idx:
            if st.get("rd"): st["prev"] = st.get("img"); st["rd"].close()
            st["rd"] = Reader(self.c.SRC, s, dur); st["idx"] = idx
        fr = st["rd"].next()
        im = fmt.compose(fr, mode, 1.0 + 0.05 * lt / max(dur, 1))
        if idx > 0 and self.tl[idx - 1][4] == "cold" and seg != "cold" and lt < 0.12:
            im = Image.blend(im, Image.new("RGB", im.size, WHITE), 1 - lt / 0.12)
        elif st.get("prev") is not None and lt < 0.2:
            im = Image.blend(st["prev"], im, clamp(lt / 0.2))
        d = ImageDraw.Draw(im, "RGBA")
        if seg == "cold":
            layout_callouts(fmt, im, d, self.c.CALLOUTS.get("cold", []), g, self.COLD)
        else:
            bs = self.COLD + self.c.BT[seg]; bd = self.bend(seg) - self.c.BT[seg]
            layout_callouts(fmt, im, d, self.c.CALLOUTS.get(seg, []), g - bs, bd)
            for a_, b_, ch in self.caps:
                if a_ <= g < b_: caption(fmt, d, ch.replace("TaxBooks C F O.", "TaxBooksCFO.")); break
        chrome(fmt, im, d, g, self.TOTAL, self.c.EPLABEL)
        if lt >= 0.2: st["img"] = im
        return im

    def audio(self, path):
        SR = 48000; c = self.c
        src = np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-i", c.SRC, "-vn", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32).reshape(-1, 2)
        vo = np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-i", c.VO, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32).reshape(-1, 2)
        n = int(self.TOTAL * SR); out = np.zeros((n, 2), np.float32); rng = np.random.default_rng(3)
        def add(t0, sig, gain=1.0):
            if sig.ndim == 1: sig = np.stack([sig, sig], 1)
            s0 = int(max(0, t0) * SR); e = min(n, s0 + len(sig))
            if e > s0: out[s0:e] += sig[: e - s0] * gain
        for g0, dur, s, mode, seg in self.tl:
            if s is None: continue
            x = src[int(s * SR): int((s + dur) * SR)].copy(); f = min(len(x) // 2, int(.05 * SR))
            if f: x[:f] *= np.linspace(0, 1, f)[:, None]; x[-f:] *= np.linspace(1, 0, f)[:, None]
            add(g0, x, 1.0 if seg == "cold" else 0.07)
        add(self.COLD, vo[: int(c.VO_END * SR)] * 1.15)
        def impact(t0, g=.5):
            L = int(.9 * SR); tt = np.arange(L) / SR
            add(t0, (np.sin(2 * np.pi * (55 * tt + 40 * (1 - np.exp(-tt * 18)) / 18)) * np.exp(-tt * 6) + rng.standard_normal(L) * np.exp(-tt * 40) * .3) * g)
        def whoosh(t0, dur=.7, g=.3):
            L = int(dur * SR); tt = np.arange(L) / L; nz = rng.standard_normal(L)
            add(t0 - dur * .7, (nz * .2 + np.convolve(nz, np.ones(30) / 30, 'same') * 2.2) * np.sin(np.pi * tt) ** 2 * g)
        whoosh(self.COLD); impact(self.COLD, .5); whoosh(self.TOTAL - ENDCARD, .6, .25)
        for b, items in c.CALLOUTS.items():
            if b == "cold": continue
            bd = self.bend(b) - c.BT[b]
            for frac, kind, _ in items:
                if kind in ("slam", "card", "big"): impact(self.COLD + c.BT[b] + frac * bd, .28)
        out = np.tanh(out * 1.05) * 0.9
        s16 = (np.clip(out, -1, 1) * 32767).astype(np.int16)
        with wave.open(path, "wb") as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(s16.tobytes())

    def render(self, fmt_name, out_mp4, audio_wav):
        fmt = Fmt(fmt_name); tmp = out_mp4 + ".v.mp4"
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{fmt.W}x{fmt.H}", "-r", str(FPS), "-i", "-",
                              "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
        st = {}
        for i in range(int(self.TOTAL * FPS)): p.stdin.write(self.frame(fmt, i / FPS, st).tobytes())
        p.stdin.close(); p.wait()
        if st.get("rd"): st["rd"].close()
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", audio_wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", out_mp4])
        os.remove(tmp)

    def stills(self, fmt_name, times, prefix):
        fmt = Fmt(fmt_name); paths = []
        for g in times:
            st = {}; idx = max(i for i, x in enumerate(self.tl) if x[0] <= g); g0 = self.tl[idx][0]; im = None
            for k in range(int((g - g0) * FPS) + 1): im = self.frame(fmt, g0 + k / FPS, st)
            if st.get("rd"): st["rd"].close()
            pth = f"{prefix}_{fmt_name}_{g:06.1f}.png"; im.save(pth); paths.append(pth)
        return paths
