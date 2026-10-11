#!/usr/bin/env python3
"""Captures d'écran réelles du simulateur (hors ligne) avec une topologie chargée.
Usage : python3 tools/shot.py topologie.json sortie.png [--w 1100 --h 620]"""
import sys, os, argparse
from playwright.sync_api import sync_playwright
ap = argparse.ArgumentParser(); ap.add_argument("json"); ap.add_argument("out")
ap.add_argument("--w", type=int, default=1200); ap.add_argument("--h", type=int, default=640)
ap.add_argument("--wait", type=int, default=2500)
a = ap.parse_args()
html = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "simulateur", "simulateur-reseau.html"))
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": a.w, "height": a.h})
    pg.goto("file://" + html); pg.wait_for_timeout(800)
    pg.set_input_files("#filein", a.json); pg.wait_for_timeout(a.wait)
    try:
        pg.click("#btn-fit"); pg.wait_for_timeout(500)
    except Exception:
        pass
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    try:
        pg.evaluate("document.querySelectorAll('.toast,#toast').forEach(e=>e.remove())")
        pg.locator("#stage").screenshot(path=a.out)
    except Exception:
        pg.screenshot(path=a.out)
    b.close()
print("ok", a.out)
