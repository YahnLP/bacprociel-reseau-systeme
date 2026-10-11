#!/usr/bin/env python3
"""Capture la fenêtre d'un équipement du simulateur (terminal, configuration IP, services…).
Usage : python3 tools/shot_win.py topo.json sortie.png --dev PC1 [--tab "Configuration IP"] [--cmd "ipconfig" --cmd "ping 192.168.1.12"]
        [--set "ip=192.168.1.11" ...] [--w 900 --h 520]"""
import sys, os, argparse
from playwright.sync_api import sync_playwright
ap = argparse.ArgumentParser(); ap.add_argument("json"); ap.add_argument("out"); ap.add_argument("--dev", required=True)
ap.add_argument("--tab"); ap.add_argument("--cmd", action="append", default=[]); ap.add_argument("--w", type=int, default=1400); ap.add_argument("--h", type=int, default=800)
ap.add_argument("--wait", type=int, default=1500); ap.add_argument("--scroll", action="store_true")
a = ap.parse_args()
html = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "simulateur", "simulateur-reseau.html"))
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"]); pg = b.new_page(viewport={"width": a.w, "height": a.h})
    pg.goto("file://" + html); pg.wait_for_timeout(600)
    pg.set_input_files("#filein", a.json); pg.wait_for_timeout(a.wait)
    pg.locator(f'#stage .node[aria-label^="{a.dev},"]').first.dblclick(force=True); pg.wait_for_timeout(700)
    win = pg.locator(".win").last
    if a.tab:
        win.locator(f"text={a.tab}").first.click(); pg.wait_for_timeout(400)
    for c in a.cmd:
        pg.keyboard.type(c); pg.keyboard.press("Enter"); pg.wait_for_timeout(8000 if c.split()[0] in ("ping", "nslookup", "tracert") else 1500)
    if a.scroll:
        win.evaluate("el => el.querySelectorAll('*').forEach(e => { if (e.scrollHeight > e.clientHeight + 5) e.scrollTop = e.scrollHeight; })"); pg.wait_for_timeout(300)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    win.screenshot(path=a.out); b.close()
print("ok", a.out)
