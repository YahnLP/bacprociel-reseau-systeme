#!/usr/bin/env python3
"""Capture annotée de l'interface du simulateur : des pastilles numérotées sur les zones.
Usage : python3 tools/shot_ui.py topologie.json sortie.png"""
import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont
html = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "simulateur", "simulateur-reseau.html"))
# points d'ancrage absolus (fenêtre 1400 × 820)
PTS = [(500, 56), (1155, 56), (216, 140), (205, 216), (330, 180), (1000, 760), (1250, 345)]
NOMS = ["Ouvrir / Enregistrer", "+1 min / RAZ réseau", "Outils (sélection, câble)", "Palette d'équipements", "Schéma", "Analyseur de trames", "Propriétés"]
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"]); pg = b.new_page(viewport={"width": 1400, "height": 820})
    pg.goto("file://" + html); pg.wait_for_timeout(1000)
    pg.set_input_files("#filein", sys.argv[1]); pg.wait_for_timeout(2500)
    pg.evaluate("document.querySelectorAll('.toast,#toasts').forEach(e=>e.remove())")
    pg.screenshot(path="/tmp/_ui.png"); b.close()
im = Image.open("/tmp/_ui.png").convert("RGB"); d = ImageDraw.Draw(im)
try: ft = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
except Exception: ft = ImageFont.load_default()
for i, (x, y) in enumerate(PTS, 1):
    d.ellipse([x - 16, y - 16, x + 16, y + 16], fill=(230, 81, 0), outline=(255, 255, 255), width=3)
    w = d.textlength(str(i), font=ft); d.text((x - w / 2, y - 12), str(i), fill=(255, 255, 255), font=ft)
os.makedirs(os.path.dirname(os.path.abspath(sys.argv[2])), exist_ok=True)
im.save(sys.argv[2]); print("ok", sys.argv[2], list(zip(range(1, 8), NOMS)))
