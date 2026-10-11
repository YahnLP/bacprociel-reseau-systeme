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



def s07():
    d = "S07-maj-sauvegardes"
    f = Fig(1000, 330, "Mettre à jour sans risque : cinq étapes", "Sauvegarder, vérifier la compatibilité, mettre à jour, tester, puis garder le plan de retour arrière. La sauvegarde vient toujours avant la mise à jour.")
    f.title_bar("Mettre à jour sans risque : toujours cinq étapes")
    et = [("1", "Sauvegarder", "la configuration", "et noter la version", TEAL_L, TEAL), ("2", "Vérifier", "la notice de la", "nouvelle version", IND_L, IND),
          ("3", "Prévenir", "le client, choisir", "un créneau calme", YEL_L, "#b28704"), ("4", "Mettre à jour", "l'appareil et", "le redémarrer", ORA_L, ORA), ("5", "Tester", "ou revenir en", "arrière", GRN_L, GRN)]
    for i, (n, t, a, b, fill, st) in enumerate(et):
        x = 30 + i * 190
        f.rect(x, 75, 175, 160, fill, st, 3, 14); f.badge(x + 87, 103, n, st, 16)
        f.text(x + 87, 148, t, 18, INK, "middle", "700"); f.text(x + 87, 180, a, 14, INK); f.text(x + 87, 202, b, 14, INK)
        if i < 4:
            f.arrow(x + 177, 155, x + 190, 155, MUTED, 3)
    f.rect(30, 262, 940, 44, RED_L, RED, 2, 10)
    f.text(500, 290, "Règle d'or : si la sauvegarde n'est pas faite ET vérifiée, on ne met rien à jour.", 15, RED, "middle", "700")
    f.save(out(d, "maj-5-etapes.svg"))


if __name__ == "__main__":
    for w_ in (sys.argv[1:] or ["s06", "s07"]):
        globals()[w_](); print("OK", w_)
