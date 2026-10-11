#!/usr/bin/env python3
"""Illustrations Terminale – S06 et suivantes."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "terminale"))
out = lambda s, n: os.path.join(ROOT, s, "images", n)


def s06():
    d = "S06-wifi-entreprise"
    f = Fig(1000, 440, "Deux SSID, deux VLAN, un routeur qui filtre", "Le portable du personnel se connecte à GARCIA-PERSONNEL (VLAN 20), le portable invité à GARCIA-INVITES (VLAN 30). Le routeur relie les VLAN et l'ACL interdit aux invités d'aller vers le réseau interne.")
    f.title_bar("Un SSID = un VLAN = un réseau IP")
    node(f, "laptop", 90, 130, "Personnel", "GARCIA-PERSONNEL")
    node(f, "laptop", 90, 330, "Invité", "GARCIA-INVITES")
    node(f, "ap", 330, 130, "Borne", "SSID personnel")
    node(f, "ap", 330, 330, "Borne", "SSID invités")
    wifi_link(f, 140, 130, 280, 130); wifi_link(f, 140, 330, 280, 330)
    node(f, "switch", 570, 230, "Switch", "VLAN 20 / 30 / trunk")
    f.line(380, 130, 520, 215, LINE, 3); f.line(380, 330, 520, 250, LINE, 3)
    f.text(450, 150, "VLAN 20", 13, IND, "middle", "700"); f.text(450, 330, "VLAN 30", 13, ORA, "middle", "700")
    node(f, "router", 820, 120, "Routeur", "ACL INVITES-IN")
    f.line(625, 215, 770, 135, LINE, 3); f.text(690, 150, "trunk", 13, MUTED, "middle", "700")
    node(f, "server", 820, 340, "Serveur interne", "VLAN 10")
    f.line(820, 175, 820, 290, LINE, 3, arrow=True)
    f.text(845, 235, "autorisé", 13, GRN, "start", "700")
    f.rect(640, 285, 120, 70, RED_L, RED, 2.5, 10); f.text(700, 313, "Invités", 13, RED, "middle", "700"); f.text(700, 334, "bloqués ✗", 13, RED, "middle", "700")
    f.save(out(d, "wifi-vlan.svg"))


if __name__ == "__main__":
    for w_ in (sys.argv[1:] or ["s06"]):
        globals()[w_](); print("OK", w_)
