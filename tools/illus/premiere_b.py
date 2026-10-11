#!/usr/bin/env python3
"""Illustrations Première – S07 et suivantes."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "premiere"))
out = lambda s, n: os.path.join(ROOT, s, "images", n)


def s07():
    d = "S07-routeur-routage-statique"
    f = Fig(1000, 520, "Aller et retour à travers deux routeurs",
            "PC1 envoie un paquet vers le serveur : R1 puis R2 le font suivre grâce à leurs routes. La réponse refait le chemin inverse : R2 doit aussi connaître le réseau de PC1.")
    f.title_bar("Un paquet va… et la réponse doit revenir")
    X = [110, 360, 640, 890]; Y = 190
    node(f, "pc", X[0], Y, "PC1", "192.168.10.11")
    node(f, "router", X[1], Y, "R1", "gi0/0 .10.1 | gi0/1 10.0.0.1")
    node(f, "router", X[2], Y, "R2", "gi0/1 10.0.0.2 | gi0/0 .20.1")
    node(f, "server", X[3], Y, "SRV1", "192.168.20.100")
    # câbles
    for a, b in ((0, 1), (1, 2), (2, 3)):
        f.line(X[a] + 48, Y, X[b] - 48, Y, GRY_D, 3)
    f.text((X[1] + X[2]) / 2, Y - 12, "10.0.0.0/30", 14, MUTED, "middle", "700")
    # aller
    f.text(500, 80, "ALLER : « je veux joindre 192.168.20.100 »", 16, IND, "middle", "700")
    for a, b, t in ((0, 1, "① passerelle"), (1, 2, "② route statique"), (2, 3, "③ réseau connecté")):
        f.arrow(X[a] + 40, 108, X[b] - 40, 108, IND, 4)
        f.text((X[a] + X[b]) / 2, 128, t, 13, IND, "middle", "600")
    # retour
    f.text(500, 292, "RETOUR : « réponse pour 192.168.10.11 »", 16, ORA, "middle", "700")
    for a, b, t in ((3, 2, "④ passerelle"), (2, 1, "⑤ route statique"), (1, 0, "⑥ réseau connecté")):
        f.arrow(X[a] - 40, 312, X[b] + 40, 312, ORA, 4)
        f.text((X[a] + X[b]) / 2, 334, t, 13, ORA, "middle", "600")
    # tables
    f.rect(70, 360, 420, 130, IND_L, IND, 2, 10)
    f.text(280, 382, "Table de routage de R1", 15, IND, "middle", "700")
    for i, (t, c) in enumerate((("C  192.168.10.0/24   → gi0/0", INK), ("C  10.0.0.0/30        → gi0/1", INK), ("S  192.168.20.0/24   → via 10.0.0.2", RED))):
        f.mono(90, 410 + i * 26, t, 14, c, "start", "700" if c == RED else "400")
    f.rect(510, 360, 420, 130, ORA_L, ORA, 2, 10)
    f.text(720, 382, "Table de routage de R2", 15, ORA, "middle", "700")
    for i, (t, c) in enumerate((("C  192.168.20.0/24   → gi0/0", INK), ("C  10.0.0.0/30        → gi0/1", INK), ("S  192.168.10.0/24   → via 10.0.0.1", RED))):
        f.mono(530, 410 + i * 26, t, 14, c, "start", "700" if c == RED else "400")
    f.text(500, 508, "C = réseau connecté (automatique) · S = route statique (écrite à la main)", 13, MUTED, "middle")
    f.save(out(d, "aller-retour.svg"))

    # --- ce que fait un routeur d'un paquet
    f = Fig(900, 470, "Que fait un routeur d'un paquet ?", "Il lit l'adresse de destination, cherche la route la plus précise dans sa table, puis envoie au prochain routeur ; sans route il rejette.")
    f.title_bar("Ce que fait un routeur de chaque paquet")
    steps = [("1", "Lire l'adresse de destination", "dans l'en-tête IP"), ("2", "Chercher dans la table de routage", "la route la plus précise (masque le plus long)"),]
    x = 60
    for i, (n, t, s) in enumerate(steps):
        y = 60 + i * 95
        f.rect(x, y, 380, 70, IND_L, IND, 2.5, 12); f.badge(x + 28, y + 35, n, IND, 16)
        f.text(x + 56, y + 31, t, 16, IND, "start", "700"); f.text(x + 56, y + 53, s, 13.5, INK, "start")
    f.arrow(250, 130, 250, 155, LINE, 3)
    f.rect(480, 110, 340, 100, YEL_L, YEL, 2.5, 12)
    f.text(650, 142, "Une route correspond-elle ?", 17, INK, "middle", "700")
    f.text(650, 168, "(réseau connecté, statique, par défaut)", 13.5, MUTED, "middle")
    f.arrow(440, 190, 480, 160, LINE, 3)
    # oui
    f.arrow(590, 210, 590, 255, GRN, 3); f.text(608, 238, "oui", 15, GRN, "start", "700")
    f.rect(440, 260, 300, 80, GRN_L, GRN, 2.5, 12)
    f.text(590, 290, "3. Envoyer au prochain saut", 16, GRN, "middle", "700")
    f.text(590, 314, "ou directement (réseau connecté)", 13.5, INK, "middle")
    # non
    f.arrow(780, 210, 780, 348, RED, 3)
    f.text(798, 300, "non", 15, RED, "start", "700")
    f.rect(60, 350, 760, 80, RED_L, RED, 2.5, 12)
    f.text(440, 380, "Sinon : pas de route ⇒ le paquet est jeté", 16, RED, "middle", "700")
    f.text(440, 404, "le routeur répond « destination injoignable » à l'émetteur (message ICMP)", 13.5, INK, "middle")
    f.save(out(d, "decision-routeur.svg"))


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s07"]):
        globals()[w](); print("OK", w)
