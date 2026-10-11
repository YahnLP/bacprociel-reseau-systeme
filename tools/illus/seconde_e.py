#!/usr/bin/env python3
"""Illustrations Seconde – S15 (dépannage de niveau 1)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "seconde"))
out = lambda s, n: os.path.join(ROOT, s, "images", n)


def s15():
    d = "S15-depannage-n1"
    f = Fig(980, 640, "L'échelle du diagnostic", "Cinq tests dans l'ordre : câble, adresse IP, ping de la passerelle, ping d'Internet par IP, ping d'un nom. Le premier test qui échoue indique la panne.")
    f.title_bar("L'échelle du diagnostic : on monte marche par marche")
    f.text(215, 66, "Je teste…", 15, MUTED, "middle", "700")
    f.text(560, 66, "Avec quoi ?", 15, MUTED, "middle", "700")
    f.text(840, 66, "Si ça ÉCHOUE, la panne est…", 15, MUTED, "middle", "700")
    rows = [
        ("Le câble, les voyants", "regarder la prise et les LED", "le câble ou le port", IND_L, IND),
        ("Mon adresse IP", "ipconfig", "l'adresse (DHCP absent ? IP fausse ?)", IND_L, IND),
        ("La passerelle (la box)", "ping 192.168.1.1", "la liaison locale ou la passerelle", TEAL_L, TEAL),
        ("Internet, par une adresse", "ping 203.0.113.1", "la route vers Internet", ORA_L, ORA),
        ("Internet, par un nom", "ping www.exemple.fr", "le DNS", YEL_L, "#b28704"),
    ]
    y0, h, gap = 82, 86, 22
    for i, (a, cmd, bad, fill, st) in enumerate(rows):
        y = y0 + i * (h + gap)
        f.rect(40, y, 350, h, fill, st, 2.5, 12)
        f.badge(72, y + h / 2, str(i + 1), st, 17)
        f.text(105, y + h / 2 + 6, a, 17, INK, "start", "700")
        f.rect(410, y, 300, h, WHITE, LINE, 2, 12)
        f.mono(560, y + h / 2 + 6, cmd, 17, IND, "middle", "700")
        f.rect(730, y, 215, h, RED_L, RED, 2, 12)
        f.text(837, y + h / 2 - 2, bad, 14, INK, "middle", "700", maxw=195)
        if i < len(rows) - 1:
            f.arrow(215, y + h, 215, y + h + gap - 3, GRN, 3)
            f.text(240, y + h + 16, "OK ? → marche suivante", 12, GRN, "start", "700")
    f.save(out(d, "echelle-diagnostic.svg"))

def s16():
    d = "S16-projet-a1-1"
    f = Fig(980, 640, "Plan du local de l'atelier", "Pièce de 10 m sur 6 m : quatre postes le long du mur nord, une imprimante, un coin technique avec la box et le switch près de la porte.")
    f.title_bar("Plan du local (10 m × 6 m) – 1 carreau = 1 m")
    ox, oy, sc = 70, 70, 82  # origine, échelle (px par m)
    f.rect(ox, oy, 10 * sc, 6 * sc, "#fafbff", LINE, 4, 4)
    for k in range(1, 10):
        f.line(ox + k * sc, oy, ox + k * sc, oy + 6 * sc, "#e3e6f3", 1)
    for k in range(1, 6):
        f.line(ox, oy + k * sc, ox + 10 * sc, oy + k * sc, "#e3e6f3", 1)
    f.rect(ox, oy, 10 * sc, 6 * sc, "none", LINE, 4, 4)
    # porte (mur sud, à gauche)
    f.rect(ox + 0.8 * sc, oy + 6 * sc - 4, 1.2 * sc, 8, WHITE, WHITE, 1, 0)
    f.text(ox + 1.4 * sc, oy + 6 * sc + 26, "porte", 14, MUTED, "middle", "700")
    # postes au mur nord : x = 2, 4.5, 7, 9 m
    for k, xm in enumerate([1.8, 4.2, 6.6, 9.0]):
        x = ox + xm * sc
        f.rect(x - 38, oy + 12, 76, 56, IND_L, IND, 2.5, 8)
        f.text(x, oy + 46, f"Poste {k + 1}", 15, IND, "middle", "700")
    # imprimante
    f.rect(ox + 4.6 * sc, oy + 3.5 * sc, 100, 56, ORA_L, ORA, 2.5, 8)
    f.text(ox + 4.6 * sc + 50, oy + 3.5 * sc + 34, "Imprimante", 14, ORA, "middle", "700")
    # coin technique
    f.rect(ox + 0.2 * sc, oy + 4.1 * sc, 2.3 * sc, 1.6 * sc, TEAL_L, TEAL, 3, 10, dash="8 5")
    f.text(ox + 0.2 * sc + 1.15 * sc, oy + 4.1 * sc + 26, "Coin technique", 15, TEAL, "middle", "700")
    f.text(ox + 0.2 * sc + 1.15 * sc, oy + 4.1 * sc + 50, "box + switch", 14, INK, "middle", "700")
    f.text(ox + 0.2 * sc + 1.15 * sc, oy + 4.1 * sc + 72, "(prise FAI au mur)", 12.5, MUTED)
    # cotes
    f.line(ox, oy - 14, ox + 10 * sc, oy - 14, MUTED, 1.5); f.text(ox + 5 * sc, oy - 20, "10 m", 14, MUTED, "middle", "700")
    f.line(ox + 10 * sc + 16, oy, ox + 10 * sc + 16, oy + 6 * sc, MUTED, 1.5); f.text(ox + 10 * sc + 24, oy + 3 * sc, "6 m", 14, MUTED, "start", "700")
    f.text(ox + 5 * sc, oy + 6 * sc + 48, "Les câbles passent par le plafond technique : on compte la hauteur (2,5 m) en plus des distances au sol.", 14, INK, "middle", "700")
    f.save(out(d, "plan-local.svg"))

    f = Fig(940, 420, "Dossier partagé : qui a le droit de quoi", "Trois comptes : direction (modifier), atelier (lire), invité (aucun accès). Les droits les plus restrictifs l'emportent entre partage et sécurité.")
    f.title_bar("Un dossier partagé, trois niveaux d'accès")
    f.rect(330, 70, 280, 80, IND_L, IND, 3, 12); f.text(470, 104, "Dossier « Commandes »", 18, IND, "middle", "700"); f.text(470, 132, "sur le poste 1", 14, INK)
    cards = [(40, "direction", "Modifier", "lire, créer, supprimer", GRN_L, GRN),
             (350, "atelier", "Lire seulement", "ouvrir, copier", YEL_L, "#b28704"),
             (660, "invité", "Aucun accès", "dossier invisible", RED_L, RED)]
    for (x, who, droit, det, fill, st) in cards:
        f.rect(x, 250, 240, 120, fill, st, 3, 12)
        f.text(x + 120, 282, f"Compte « {who} »" if who != "invité" else "Visiteur / invité", 16, INK, "middle", "700")
        f.text(x + 120, 316, droit, 20, st, "middle", "700")
        f.text(x + 120, 346, det, 14, INK)
        f.line(470, 150, x + 120, 248, st, 3)
    f.save(out(d, "partage-droits.svg"))


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s15", "s16"]):
        globals()[w](); print("OK", w)
