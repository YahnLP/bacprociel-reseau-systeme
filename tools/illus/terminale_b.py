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



def s08():
    d = "S08-integrer-equipements"
    f = Fig(1000, 500, "Un VLAN pour les objets connectés", "Les postes sont dans le VLAN 10. L'imprimante, le NAS, la caméra IP et la carte ESP32 sont dans un VLAN 40 dédié, relié au switch cœur qui route et peut filtrer.")
    f.title_bar("Les objets connectés ont leur propre VLAN")
    node(f, "switch", 500, 230, "CORE (niveau 3)", "routage + passerelles")
    f.rect(40, 70, 230, 170, IND_L, IND, 3, 14); f.text(155, 98, "VLAN 10 – POSTES", 15, IND, "middle", "700")
    node(f, "pc", 100, 160, "PC-1", "DHCP .50+"); node(f, "pc", 215, 160, "PC-2", "DHCP .50+")
    f.rect(330, 320, 640, 150, ORA_L, ORA, 3, 14); f.text(650, 348, "VLAN 40 – OBJETS  (adresses fixes, hors plage DHCP)", 15, ORA, "middle", "700")
    node(f, "printer", 420, 392, "Imprimante", ".20"); node(f, "server", 590, 392, "NAS", ".30")
    node(f, "phone", 760, 392, "Caméra IP", ".31 (PoE)"); node(f, "box", 900, 392, "ESP32", ".40")
    f.line(270, 170, 450, 235, LINE, 3); f.line(500, 292, 500, 320, LINE, 3)
    f.rect(740, 80, 230, 150, YEL_L, YEL, 2.5, 12)
    for k, t in enumerate(("Pourquoi un VLAN à part ?", "• on les filtre facilement", "• une panne ou une attaque", "ne gagne pas les postes", "• adresses faciles à retenir")):
        f.text(752, 106 + k * 24, t, 13.5, INK, "start", "700" if k == 0 else "400")
    f.save(out(d, "vlan-objets.svg"))


if __name__ == "__main__":
    for w_ in (sys.argv[1:] or ["s06", "s07", "s08"]):
        globals()[w_](); print("OK", w_)
