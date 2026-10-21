from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import os

OUT = os.path.dirname(os.path.abspath(__file__))
INK = "#111111"
ACCENT = "#E8590C"
PAPER = "#FFFFFF"

FONTS = {
    "inter_med": "/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf",
    "inter_semi": "/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf",
    "inter_reg": "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
    "bask": "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf",
}
_cache = {}


def font(key):
    if key not in _cache:
        _cache[key] = TTFont(FONTS[key])
    return _cache[key]


def text_path(key, text, size, x, y, tracking=0.0):
    """Return (path_d, advance_width) with text converted to outlines."""
    f = font(key)
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    upm = f["head"].unitsPerEm
    s = size / upm
    hmtx = f["hmtx"]
    cx = x
    d = []
    for ch in text:
        gn = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        tp = TransformPen(pen, (s, 0, 0, -s, cx, y))
        gs[gn].draw(tp)
        d.append(pen.getCommands())
        cx += hmtx[gn][0] * s + tracking * size
    return " ".join(d), cx - x


def svg(w, h, body, bg=PAPER):
    bgrect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}">{bgrect}{body}</svg>')


def mark_sequence(x, y, s=1.0, ink=INK, accent=ACCENT):
    """0 -> 1 -> many : ring, bar, three dots. Baseline-centred on y."""
    r = 30 * s
    sw = 9 * s
    g = []
    # zero: open ring
    g.append(f'<circle cx="{x + r}" cy="{y}" r="{r - sw / 2}" fill="none" stroke="{ink}" stroke-width="{sw}"/>')
    # one: vertical bar
    bx = x + 2 * r + 26 * s
    bw = 10 * s
    g.append(f'<rect x="{bx}" y="{y - r}" width="{bw}" height="{2 * r}" fill="{ink}"/>')
    # many: three dots, 2 over 1 triangle, accent
    dx = bx + bw + 26 * s
    dr = 10.5 * s
    gap = 25 * s
    pts = [(dx + dr, y - gap / 2 - dr / 2 + 2 * s), (dx + dr + gap + 2 * s, y - gap / 2 - dr / 2 + 2 * s),
           (dx + dr + gap / 2 + s, y + gap / 2 + dr / 2 + 2 * s)]
    # place dots so cluster is vertically centred
    for (px, py) in pts:
        g.append(f'<circle cx="{px}" cy="{py - 2 * s}" r="{dr}" fill="{accent}"/>')
    width = (dx + dr + gap + 2 * s + dr) - x
    return "".join(g), width


# ---------- A : mark + wordmark ----------
def logo_a(bg=PAPER, ink=INK, accent=ACCENT):
    w, h = 1200, 400
    m, mw = mark_sequence(120, 200, 1.35, ink, accent)
    d, adv = text_path("inter_med", "Zero One Many", 96, 120 + mw + 70, 200 + 34, tracking=-0.02)
    body = m + f'<path d="{d}" fill="{ink}"/>'
    return svg(w, h, body, bg)


# ---------- B : serif wordmark ----------
def logo_b(bg=PAPER, ink=INK, accent=ACCENT):
    w, h = 1200, 400
    d, adv = text_path("bask", "Zero One Many", 118, 120, 215, tracking=-0.005)
    # accent full stop (square) after the word
    sq = 17
    body = f'<path d="{d}" fill="{ink}"/>'
    body += f'<rect x="{120 + adv + 10}" y="{215 - sq}" width="{sq}" height="{sq}" fill="{accent}"/>'
    # thin rule + descriptor
    d2, adv2 = text_path("inter_reg", "REVOPS  ·  GO TO MARKET  ·  HUBSPOT", 25, 124, 280, tracking=0.16)
    body += f'<rect x="124" y="244" width="64" height="3" fill="{accent}"/>'
    body += f'<path d="{d2}" fill="{ink}"/>'
    return svg(w, h, body, bg)


# ---------- C : monogram tile + stacked caps ----------
def logo_c(bg=PAPER, ink=INK, accent=ACCENT):
    w, h = 1200, 400
    t = 200
    tx, ty = 120, 100
    body = f'<rect x="{tx}" y="{ty}" width="{t}" height="{t}" fill="{ink}"/>'
    # 0 1 N inside tile
    d, adv = text_path("inter_semi", "01M", 84, 0, 0, tracking=0.03)
    ox = tx + (t - adv) / 2
    d, adv = text_path("inter_semi", "01M", 84, ox, ty + t / 2 + 30, tracking=0.03)
    body += f'<path d="{d}" fill="{PAPER if ink != PAPER else INK}"/>'
    body += f'<rect x="{tx + 30}" y="{ty + t - 38}" width="{t - 60}" height="6" fill="{accent}"/>'
    # stacked caps
    lx = tx + t + 60
    sizes = 58
    for i, word in enumerate(["ZERO", "ONE", "MANY"]):
        dd, a = text_path("inter_semi", word, sizes, lx, ty + 54 + i * 70, tracking=0.12)
        body += f'<path d="{dd}" fill="{ink}"/>'
    return svg(w, h, body, bg)


# ---------- favicon-size mark (A) ----------
def mark_only(bg=PAPER, ink=INK, accent=ACCENT):
    w, h = 400, 400
    m, mw = mark_sequence(0, 200, 1.35, ink, accent)
    ox = (w - mw) / 2
    m, mw = mark_sequence(ox, 200, 1.35, ink, accent)
    return svg(w, h, m, bg)


files = {
    "logo_A_sequence.svg": logo_a(),
    "logo_B_serif.svg": logo_b(),
    "logo_C_monogram.svg": logo_c(),
    "mark_A_only.svg": mark_only(),
    "logo_A_sequence_dark.svg": logo_a(bg=INK, ink="#FFFFFF"),
}
for n, c in files.items():
    open(os.path.join(OUT, n), "w").write(c)
print("ok", list(files))


# ---------- Final set: C with 01M ----------
def tile(x, y, t, ink=INK, fg=PAPER, accent=ACCENT, text_col=None):
    text_col = text_col or fg
    size = 84 * t / 200
    d, adv = text_path("inter_semi", "01M", size, 0, 0, tracking=0.03)
    ox = x + (t - adv) / 2
    d, adv = text_path("inter_semi", "01M", size, ox, y + t / 2 + 30 * t / 200, tracking=0.03)
    b = f'<rect x="{x}" y="{y}" width="{t}" height="{t}" fill="{ink}"/>'
    b += f'<path d="{d}" fill="{text_col}"/>'
    b += f'<rect x="{x + 30 * t / 200}" y="{y + t - 38 * t / 200}" width="{t - 60 * t / 200}" height="{6 * t / 200}" fill="{accent}"/>'
    return b


def stacked(x, y, t, col):
    size = 58 * t / 200
    b = ""
    for i, word in enumerate(["ZERO", "ONE", "MANY"]):
        dd, a = text_path("inter_semi", word, size, x, y + 54 * t / 200 + i * 70 * t / 200, tracking=0.12)
        b += f'<path d="{dd}" fill="{col}"/>'
    return b


# avatar / favicon: full-bleed square
open(os.path.join(OUT, "avatar_square.svg"), "w").write(svg(800, 800, tile(0, 0, 800)))
open(os.path.join(OUT, "favicon.svg"), "w").write(svg(64, 64, tile(0, 0, 64)))

# LinkedIn banner 1584x396, dark, block right of the photo zone
t = 150
word_w = 0
for w_ in ["ZERO", "ONE", "MANY"]:
    _, a = text_path("inter_semi", w_, 58 * t / 200, 0, 0, tracking=0.12)
    word_w = max(word_w, a)
gap = 45
block = t + gap + word_w
bx = 1584 - 150 - block
by = (396 - t) / 2
body = tile(bx, by, t, ink=PAPER, fg=INK, text_col=INK)
body += stacked(bx + t + gap, by, t, PAPER)
open(os.path.join(OUT, "banner_linkedin.svg"), "w").write(svg(1584, 396, body, bg=INK))
print("final set ok")
