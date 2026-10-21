"""Rebuild web/assets/nicolas.jpg from the cutout: clean edges, 4:5 crop, site black background."""
import os
from PIL import Image, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(HERE, "portrait_cutout.png")).convert("RGBA")
a = im.getchannel("A").point(lambda v: 255 if v > 128 else 0)
a = a.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.2))  # drop colored fringe
im.putalpha(a)
w, h = im.size
im = im.crop((0, 0, w, int(w * 5 / 4)))
base = Image.new("RGBA", im.size, "#111111")
base.alpha_composite(im)
base.convert("RGB").resize((640, 800), Image.LANCZOS).save(
    os.path.join(HERE, "..", "web", "assets", "nicolas.jpg"), quality=86, optimize=True, progressive=True)
print("portrait written")
