#!/usr/bin/env python3
"""Capture de l'analyseur de trames du simulateur après des commandes.
Usage : python3 tools/shot_cap.py topo.json sortie.png --dev PC1 --cmd "ping 192.168.10.100" [--filter icmp] [--row 0] [--link "Toutes les liaisons"]"""
import sys, os, argparse
from playwright.sync_api import sync_playwright
ap = argparse.ArgumentParser(); ap.add_argument("json"); ap.add_argument("out"); ap.add_argument("--dev", required=True)
ap.add_argument("--cmd", action="append", default=[]); ap.add_argument("--filter", default=""); ap.add_argument("--row", type=int, default=0)
ap.add_argument("--w", type=int, default=1400); ap.add_argument("--h", type=int, default=900); ap.add_argument("--wait", type=int, default=2000)
ap.add_argument("--rowtext", default=""); ap.add_argument("--expand", action="append", default=[]); ap.add_argument("--clear", action="store_true"); ap.add_argument("--link"); ap.add_argument("--full", action="store_true")
a = ap.parse_args()
html = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "simulateur", "simulateur-reseau.html"))
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"]); pg = b.new_page(viewport={"width": a.w, "height": a.h})
    pg.goto("file://" + html); pg.wait_for_timeout(800)
    pg.set_input_files("#filein", a.json); pg.wait_for_timeout(a.wait)
    if a.clear:
        pg.locator("#pane-analyzer button:has-text('Effacer')").click(); pg.wait_for_timeout(300)
    if a.cmd:
        pg.locator(f'#stage .node[aria-label^="{a.dev},"]').first.dblclick(force=True); pg.wait_for_timeout(700)
        for c in a.cmd:
            pg.keyboard.type(c); pg.keyboard.press("Enter"); pg.wait_for_timeout(8000 if c.split()[0] in ("ping", "nslookup", "tracert", "curl") else 1800)
        pg.locator(".win").last.locator("text=×").first.click(); pg.wait_for_timeout(400)
    if a.link:
        pg.locator("#pane-analyzer select").first.select_option(label=a.link); pg.wait_for_timeout(400)
    if a.filter:
        f = pg.locator("#pane-analyzer input[type=text]").first; f.fill(a.filter); pg.locator("#pane-analyzer button:has-text('Appliquer')").click(); pg.wait_for_timeout(500)
    rows = pg.locator("#pane-analyzer .wsrow")
    sel = rows.filter(has_text=a.rowtext) if a.rowtext else rows
    if sel.count() > a.row:
        sel.nth(a.row).click(); pg.wait_for_timeout(500)
    for t in a.expand:
        pg.locator("#pane-analyzer").get_by_text(t, exact=False).first.click(); pg.wait_for_timeout(300)
    pg.locator("#dockmax").click(); pg.wait_for_timeout(500)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    (pg.screenshot(path=a.out) if a.full else pg.locator("#dock").screenshot(path=a.out)); b.close()
print("ok", a.out)
