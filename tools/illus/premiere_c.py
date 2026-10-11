#!/usr/bin/env python3
"""Illustrations Première – projet A2 (S15 à S20)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "premiere"))
out = lambda s, n: os.path.join(ROOT, s, "images", n)


def s15():
    d = "S15-revision-lancement"
    f = Fig(1000, 400, "Le fil du projet A2 en quatre étapes",
            "Le projet se déroule sur quatre séances : étude, réalisation, recette puis soutenance. Chaque étape produit un livrable précis.")
    f.title_bar("Quatre séances, quatre livrables")
    ets = [("S16", "Étude", "schéma, plan d'adressage,", "liste du matériel", IND_L, IND),
           ("S17", "Réalisation", "câblage, VLAN, routeur,", "serveur, Wi-Fi, sauvegardes", TEAL_L, TEAL),
           ("S18", "Recette", "tests, pannes à réparer,", "dossier technique", ORA_L, ORA),
           ("S19", "Soutenance", "démonstration,", "questions, panne en direct", GRN_L, GRN)]
    for i, (s, t, a, b, fill, st) in enumerate(ets):
        x = 40 + i * 238
        f.rect(x, 80, 210, 230, fill, st, 3, 14)
        f.badge(x + 105, 108, s, st, 22) if False else None
        f.text(x + 105, 118, s, 26, st, "middle", "700")
        f.text(x + 105, 155, t, 20, INK, "middle", "700")
        f.text(x + 105, 200, a, 14, INK); f.text(x + 105, 222, b, 14, INK)
        if i < 3:
            f.arrow(x + 214, 195, x + 234, 195, MUTED, 3)
    f.text(500, 350, "Tout ce que tu as appris de S05 à S14 sert ici : switch, VLAN, routeur, DHCP, DNS, web, sécurité.", 15, MUTED)
    f.save(out(d, "fil-projet.svg"))


def s16():
    d = "S16-projet-1-etude"
    f = Fig(1000, 470, "Qui a le droit de joindre quoi ?",
            "Tableau des flux voulus entre les trois services et le serveur. Une case verte signifie « autorisé », une case rouge « interdit ».")
    f.title_bar("Matrice des flux voulus (cahier des charges ArchiPlus)")
    cols = ["Direction", "Atelier", "Invités", "Serveur"]
    rows = [("Direction", ["—", "oui", "inutile", "oui"]), ("Atelier", ["oui", "—", "inutile", "oui"]), ("Invités", ["NON", "NON", "—", "web + DNS"])]
    x0, y0, cw, rh = 220, 100, 180, 62
    f.text(x0 - 90, y0 + 8, "de ↓  vers →", 14, MUTED, "middle", "700")
    for j, c in enumerate(cols):
        f.rect(x0 + j * cw, y0 - 24, cw - 6, 44, IND, IND, 0, 8); f.text(x0 + j * cw + cw / 2 - 3, y0 + 4, c, 17, WHITE, "middle", "700")
    for i, (r, vals) in enumerate(rows):
        y = y0 + 34 + i * (rh + 6)
        f.rect(40, y, 160, rh, IND_L, IND, 2, 8); f.text(120, y + 38, r, 17, INK, "middle", "700")
        for j, v in enumerate(vals):
            ok = v in ("oui", "web + DNS"); no = v == "NON"
            fill, st = (GRN_L, GRN) if ok else ((RED_L, RED) if no else (GRY, GRY_D))
            f.rect(x0 + j * cw, y, cw - 6, rh, fill, st, 2.5, 8); f.text(x0 + j * cw + cw / 2 - 3, y + 38, v, 17, st if v not in ("—", "inutile") else MUTED, "middle", "700")
    f.rect(40, 345, 920, 90, YEL_L, YEL, 2.5, 12)
    f.text(60, 375, "Comment le réaliser ?", 15, "#8a6d00", "start", "700")
    f.text(60, 400, "• chaque service dans son propre VLAN et son propre sous-réseau ;", 14, INK, "start")
    f.text(60, 421, "• le routeur relie les services ; une ACL sur la patte « Invités » ne laisse passer que le web et le DNS vers le serveur.", 14, INK, "start")
    f.save(out(d, "matrice-flux.svg"))


def s16b():
    d = "S16-projet-1-etude"
    f = Fig(1000, 430, "Découper un /24 en blocs alignés",
            "Exemple d'un autre client : un réseau 192.168.100.0/24 découpé en trois blocs : 100 machines, 40 machines et 12 machines. Les blocs sont rangés du plus grand au plus petit, chacun commence à un multiple de sa taille.")
    f.title_bar("Exemple (autre client) : ranger du plus grand au plus petit")
    x0, W = 40, 920
    f.text(x0, 82, "192.168.100.0/24 = 256 adresses (de .0 à .255)", 15, INK, "start", "700")
    blocs = [("Bureaux", "100 machines → /25", 0, 128, IND_L, IND, ".0 à .127"), ("Atelier", "40 machines → /26", 128, 64, TEAL_L, TEAL, ".128 à .191"),
             ("Accueil", "12 machines → /28", 192, 16, ORA_L, ORA, ".192 à .207"), ("Libre", "réserve", 208, 48, GRY, GRY_D, ".208 à .255")]
    for n, t, a, size, fill, st, plage in blocs:
        x = x0 + a / 256 * W; w = size / 256 * W
        f.rect(x, 100, w - 3, 90, fill, st, 3, 8)
        if w > 120:
            f.text(x + w / 2, 135, n, 17, st, "middle", "700"); f.text(x + w / 2, 160, t, 13.5, INK); f.text(x + w / 2, 180, plage, 13, MUTED)
    f.text(x0 + 200 / 256 * W, 222, "Accueil /28 : .192 à .207", 13, ORA, "middle", "700")
    f.line(x0 + 200 / 256 * W, 195, x0 + 200 / 256 * W, 208, ORA, 2)
    f.rect(40, 245, 920, 160, YEL_L, YEL, 2.5, 12)
    f.text(60, 273, "La méthode en 4 gestes", 16, "#8a6d00", "start", "700")
    for i, t in enumerate(("1. Compter les machines de chaque service, avec une marge de croissance (≈ 30 %).",
                           "2. Choisir la plus petite puissance de 2 qui contient (machines + 3) : réseau, diffusion, passerelle.",
                           "3. Classer du plus grand au plus petit et placer chaque bloc à un multiple de sa taille.",
                           "4. Noter dans le plan : réseau, masque, passerelle, plage DHCP, adresses fixes.")):
        f.text(60, 303 + i * 26, t, 14.5, INK, "start")
    f.save(out(d, "decoupage-exemple.svg"))


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s15", "s16", "s16b"]):
        globals()[w](); print("OK", w)
