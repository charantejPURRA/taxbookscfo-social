"""Branded cover thumbnails: 9:16 (Reels/Shorts cover), 1:1 (feed), 16:9 (YouTube)."""
import sys, subprocess, os
sys.path.insert(0, "/home/claude/deals")
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from engine import SERIF, SANS, NAVY, ORANGE, PEACH, WHITE, MUTED

EPS = [
 ("EP1", "Scrub Daddy", "/home/claude/st/src.mp4", 686.0, [("The ", "w"), ("bidding war", "o")], [("for a sponge.", "wi")], "FIVE SHARKS. ONE SPONGE."),
 ("EP2", "Scrub Daddy", "/home/claude/st/src.mp4", 457.0, [("Kevin's ", "w"), ("royalty", "o")], [("trap.", "wi")], "A ROYALTY NEVER ENDS"),
 ("EP3", "Ring", "/home/claude/deals/ring.mp4", 297.5, [("Walked away", "w")], [("from Kevin. ", "w"), ("$1B later.", "oi")], "THE WRONG DEAL IS WORSE THAN NO DEAL"),
 ("EP4", "Wicked Good Cupcakes", "/home/claude/deals/wicked.mp4", 480.0, [("50¢ a jar.", "w")], [("Forever.", "oi")], "THE ROYALTY THAT CAME WITH THE SALE"),
 ("EP5", "Bombas", "/home/claude/deals/bombas.mp4", 585.0, [("5% ", "w"), ("became ", "m"), ("17.5%", "o")], [("Best deal ever?", "wi")], "THE MONEY WASN'T THE PRIZE"),
 ("EP6", "GrooveBook", "/home/claude/deals/groovebook.mp4", 777.0, [("Said no to ", "w"), ("$750K", "o")], [("Sold for ", "w"), ("$14.5M.", "oi")], "READ THE STRUCTURE, NOT THE HEADLINE"),
 ("EP7", "Breathometer", "/home/claude/deals/breathometer.mp4", 653.0, [("5 Sharks. ", "w"), ("$1M.", "o")], [("Then the FTC.", "oi")], "HYPE RAISES THE PRICE, NOT THE ODDS"),
 ("EP8", "Coffee Meets Bagel", "/home/claude/deals/coffeemeetsbagel.mp4", 677.5, [("They said no", "w")], [("to ", "w"), ("$30 million.", "oi")], "WAS IT THE RIGHT CALL?"),
 ("EP9", "Plated", "/home/claude/deals/plated.mp4", 50.5, [("$200M ", "o"), ("exit.", "w")], [("Then a write-down.", "oi")], "FEAR IS NOT A VALUATION"),
 ("EP10", "Bantam Bagels", "/home/claude/deals/bantam.mp4", 208.5, [("$275K ", "w"), ("for control?", "o")], [("Sold for ", "w"), ("$34M.", "oi")], "NEVER SELL CONTROL TO GET STARTED"),
]
COL = {"w": (WHITE, False), "wi": (WHITE, True), "o": (ORANGE, False), "oi": (ORANGE, True), "m": (MUTED, False)}

def frame(src, t):
    p = "/tmp/thumb_src.png"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", p])
    im = Image.open(p).convert("RGB"); im = im.crop((0, 0, im.width, int(im.height * 0.86)))
    im = ImageEnhance.Contrast(im).enhance(1.08); im = ImageEnhance.Color(im).enhance(1.1)
    return im

def cover(img, W, H):
    s = max(W / img.width, H / img.height); r = img.resize((int(img.width * s) + 1, int(img.height * s) + 1), Image.LANCZOS)
    x = (r.width - W) // 2; y = (r.height - H) // 2
    return r.crop((x, y, x + W, y + H))

def line(d, x, y, parts, size, maxw):
    while True:
        w = sum(d.textlength(t, font=SERIF(size, COL[s][1])) for t, s in parts)
        if w <= maxw or size < 20: break
        size *= 0.95
    cx = x
    for t, s in parts:
        f = SERIF(size, COL[s][1]); d.text((cx, y), t, font=f, fill=COL[s][0]); cx += d.textlength(t, font=f)
    return size

def grad(W, H, y0, y1, a1=255):
    g = Image.new("L", (1, H), 0)
    for yy in range(H):
        g.putpixel((0, yy), int(a1 * min(1, max(0, (yy - y0) / max(1, y1 - y0)))))
    return g.resize((W, H))

def wordmark(d, x, y, size):
    f1 = SERIF(size); d.text((x, y), "TaxBooks", font=f1, fill=WHITE); d.text((x + d.textlength("TaxBooks", font=f1), y), "CFO", font=f1, fill=ORANGE)

def build(ep, kind):
    tag, name, src, t, l1, l2, sub = ep
    base = frame(src, t)
    if kind == "9x16": W, H = 1080, 1920
    elif kind == "1x1": W, H = 1080, 1080
    else: W, H = 1280, 720
    im = Image.new("RGB", (W, H), NAVY)
    if kind == "16x9":
        ph = cover(base, int(W * 0.58), H); im.paste(ph, (W - ph.width, 0))
        m = Image.new("L", (W, H), 0); dm = ImageDraw.Draw(m)
        for xx in range(W): dm.line([(xx, 0), (xx, H)], fill=int(255 * max(0, min(1, (W * 0.6 - xx) / (W * 0.18)))))
        im.paste(Image.new("RGB", (W, H), NAVY), (0, 0), m)
        d = ImageDraw.Draw(im)
        d.rectangle([0, 0, W, 8], fill=ORANGE)
        d.text((48, 52), f"DEAL BEHIND THE DEAL · {tag}", font=SANS(26, 800), fill=ORANGE)
        line(d, 48, 210, l1, 92, 560); line(d, 48, 320, l2, 92, 560)
        d.text((48, 470), name.upper(), font=SANS(30, 700), fill=MUTED)
        wordmark(d, 48, H - 100, 48)
    else:
        ph_h = int(H * (0.62 if kind == "9x16" else 0.58))
        ph = cover(base, W, ph_h); im.paste(ph, (0, 0))
        im.paste(Image.new("RGB", (W, H), NAVY), (0, 0), grad(W, H, int(ph_h * 0.62), ph_h, 255))
        d = ImageDraw.Draw(im)
        d.rectangle([0, 0, W, 10], fill=ORANGE)
        k = 1.0 if kind == "9x16" else 0.78; x = 64 * k
        y = ph_h - int(60 * k)
        d.rounded_rectangle([x, y, x + d.textlength(f"DEAL BEHIND THE DEAL · {tag}", font=SANS(30 * k, 800)) + 36 * k, y + 52 * k], radius=int(26 * k), fill=ORANGE)
        d.text((x + 18 * k, y + 9 * k), f"DEAL BEHIND THE DEAL · {tag}", font=SANS(30 * k, 800), fill=WHITE)
        y += int(100 * k)
        line(d, x, y, l1, 112 * k, W - 2 * x); line(d, x, y + 128 * k, l2, 112 * k, W - 2 * x)
        y2 = y + int(290 * k)
        d.text((x, y2), sub, font=SANS(30 * k, 750), fill=PEACH)
        d.text((x, y2 + 48 * k), name.upper(), font=SANS(28 * k, 650), fill=MUTED)
        wordmark(d, x, H - int(120 * k), 54 * k)
        ft = "taxbookscfo.com"; f = SANS(30 * k, 700)
        d.text((W - x - d.textlength(ft, font=f), H - int(108 * k)), ft, font=f, fill=MUTED)
    return im

if __name__ == "__main__":
    out = "/home/claude/deals/out/covers"; os.makedirs(out, exist_ok=True)
    sel = sys.argv[1:] or [e[0] for e in EPS]
    for ep in EPS:
        if ep[0] not in sel: continue
        for kind in ("9x16", "1x1", "16x9"):
            build(ep, kind).save(f"{out}/TaxBooksCFO_{ep[0]}_cover_{kind}.png")
        print("cover", ep[0])
