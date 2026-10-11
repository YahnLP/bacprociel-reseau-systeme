#!/usr/bin/env python3
"""Enchaîne des actions dans plusieurs fenêtres du simulateur puis capture la dernière.
Usage : python3 tools/shot_seq.py topo.json sortie.png --step "PC1|Terminal|ping 198.51.100.80" ... --final "BOX|Console (CLI)|show ip nat translations"
Une étape = « équipement | onglet | commande » (commande facultative)."""
import sys, os, argparse
from playwright.sync_api import sync_playwright
ap = argparse.ArgumentParser(); ap.add_argument("json"); ap.add_argument("out"); ap.add_argument("--step", action="append", default=[]); ap.add_argument("--final", required=True)
a = ap.parse_args()
html = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "simulateur", "simulateur-reseau.html"))
def run(pg, spec, shot=None):
    dev, tab, cmd = (spec.split("|") + ["", ""])[:3]
    pg.locator("#stage").locator(f"text={dev}").first.dblclick(); pg.wait_for_timeout(600)
    w = pg.locator(".win").last
    if tab: w.locator(f"text={tab}").first.click(); pg.wait_for_timeout(500)
    if cmd:
        pg.keyboard.type(cmd); pg.keyboard.press("Enter"); pg.wait_for_timeout(8000 if cmd.split()[0] in ("ping", "nslookup", "tracert") else 1500)
    if shot: w.screenshot(path=shot)
    else: w.locator("text=×").first.click(); pg.wait_for_timeout(300)
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"]); pg = b.new_page(viewport={"width": 1400, "height": 900})
    pg.goto("file://" + html); pg.wait_for_timeout(600); pg.set_input_files("#filein", a.json); pg.wait_for_timeout(1500)
    for s in a.step: run(pg, s)
    run(pg, a.final, a.out); b.close()
print("ok", a.out)
