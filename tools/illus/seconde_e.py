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


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s15"]):
        globals()[w](); print("OK", w)
