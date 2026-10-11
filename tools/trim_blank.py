#!/usr/bin/env python3
"""Supprime la plus grande bande blanche horizontale d'une capture de l'analyseur (liste / détail)."""
import sys
from PIL import Image
for f in sys.argv[1:]:
    im = Image.open(f).convert('RGB'); w, h = im.size
    blank = [all(im.getpixel((x, y)) == (255, 255, 255) for x in range(0, w // 2, 7)) for y in range(h)]
    best = (0, 0); s = None
    for y, b in enumerate(blank + [False]):
        if b and s is None: s = y
        if not b and s is not None:
            if y - s > best[1] - best[0]: best = (s, y)
            s = None
    a, b = best
    if b - a > 40:
        out = Image.new('RGB', (w, h - (b - a) + 12), (255, 255, 255)); out.paste(im.crop((0, 0, w, a + 6)), (0, 0)); out.paste(im.crop((0, b - 6, w, h)), (0, a + 6)); out.save(f); print('trim', f)
