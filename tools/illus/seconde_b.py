#!/usr/bin/env python3
"""Illustrations Seconde – S01 (ports, sécurité), S02 (anatomie du PC), S03 (démarrage, BIOS)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "seconde"))
out = lambda s, n: os.path.join(ROOT, s, "images", n)


# ---- petits dessins de connecteurs (centrés sur x,y)
def p_rj45(f, x, y, c=IND):
    f.rect(x - 14, y - 12, 28, 24, WHITE, c, 2.5, 2); f.rect(x - 7, y - 12, 14, 7, WHITE, c, 1.5, 1)
    for i in range(4): f.line(x - 8 + i * 5.3, y + 1, x - 8 + i * 5.3, y + 9, c, 1.5)

def p_usb(f, x, y, blue=False):
    f.rect(x - 15, y - 8, 30, 16, "#90caf9" if blue else WHITE, LINE, 2.5, 2); f.rect(x - 11, y - 2, 22, 4, GRY_D, GRY_D, 1, 1)

def p_hdmi(f, x, y):
    f.poly([(x - 18, y - 8), (x + 18, y - 8), (x + 18, y + 2), (x + 11, y + 9), (x - 11, y + 9), (x - 18, y + 2)], WHITE, LINE, 2.5)

def p_jack(f, x, y, col=GRN):
    f.circle(x, y, 9, WHITE, col, 3); f.circle(x, y, 3, col, col, 1)

def p_power(f, x, y):
    f.rect(x - 16, y - 12, 32, 24, GRY, LINE, 2.5, 3)
    for dx in (-7, 7): f.line(x + dx, y - 5, x + dx, y + 5, LINE, 3)


def s01():
    d = "S01-accueil-diagnostic"
    f = Fig(900, 420, "Les connecteurs : jeu « repère les ports »", "Face arrière d'un PC, d'un switch et d'une box avec les connecteurs numérotés.")
    f.title_bar("Repère les ports !")
    # PC arrière
    f.text(170, 62, "Arrière d'un PC", 16, IND, "middle", "700")
    f.rect(30, 75, 280, 190, GRY, LINE, 3, 10)
    p_power(f, 270, 110); f.badge(270, 85, "1", RED)
    for i in range(4): p_usb(f, 70 + (i % 2) * 40, 110 + (i // 2) * 28, blue=i > 1)
    f.badge(55, 85, "2", RED)
    p_rj45(f, 160, 125); f.badge(160, 95, "3", RED)
    p_hdmi(f, 70, 215); f.badge(70, 190, "4", RED)
    p_jack(f, 150, 215, GRN); p_jack(f, 180, 215, ORA); p_jack(f, 210, 215, "#ec407a"); f.badge(180, 190, "5", RED)
    # switch
    f.text(520, 62, "Face avant d'un switch", 16, TEAL, "middle", "700")
    f.rect(370, 80, 300, 60, TEAL_L, TEAL, 3, 8)
    for i in range(8): p_rj45(f, 400 + i * 34, 112, TEAL)
    f.badge(400, 92, "6", RED)
    for i in range(8): f.circle(400 + i * 34, 94, 2.5, GRN if i < 5 else GRY_D, GRN if i < 5 else GRY_D, 1)
    f.badge(660, 108, "7", RED); f.circle(645, 108, 5, GRN, GRN, 1)
    # box
    f.text(520, 192, "Arrière d'une box", 16, ORA, "middle", "700")
    f.rect(370, 205, 300, 60, ORA_L, ORA, 3, 8)
    p_rj45(f, 400, 235, ORA); f.badge(400, 215, "8", RED)
    for i in range(3): p_rj45(f, 445 + i * 36, 235, ORA)
    p_power(f, 640, 235); f.badge(640, 214, "1", RED)
    # légende
    leg = [("1", "Alimentation (secteur)"), ("2", "USB (le bleu est plus rapide : USB 3)"), ("3", "RJ45 : le réseau"), ("4", "HDMI : l'écran"), ("5", "Prises audio (jack)"), ("6", "Ports RJ45 du switch"), ("7", "Voyant : lien / activité"), ("8", "Port WAN de la box : vers Internet")]
    for i, (n, t) in enumerate(leg):
        x = 30 + (i % 2) * 440; y = 300 + (i // 2) * 28
        f.badge(x + 12, y, n, RED, 11); f.text(x + 32, y + 5, t, 14.5, INK, "start")
    f.save(out(d, "ports.svg"))

    f = Fig(900, 300, "Règles de sécurité du plateau technique", "Quatre règles : électricité, décharges électrostatiques, rangement, charte.")
    f.title_bar("4 règles pour travailler en sécurité")
    R = [("1", "Électricité", "Je débranche le PC\n(secteur) AVANT d'ouvrir.\nJamais les mains mouillées.", RED, RED_L),
         ("2", "Décharges (ESD)", "Je touche le boîtier\nmétallique ou je mets\nle bracelet antistatique.", ORA, ORA_L),
         ("3", "Rangement", "Une zone de travail\nrangée : pas de câble\nqui traîne, pas de sac.", TEAL, TEAL_L),
         ("4", "Charte informatique", "Je n'installe rien sans\naccord, je protège mon\nmot de passe.", IND, IND_L)]
    for i, (n, t, b, c, fi) in enumerate(R):
        x = 20 + i * 220
        f.rect(x, 60, 205, 200, fi, c, 3, 14); f.badge(x + 102, 60, n, c, 16)
        f.text(x + 102, 105, t, 17, c, "middle", "700"); f.text(x + 102, 140, b, 14, INK)
    f.save(out(d, "regles.svg"))


def s02():
    d = "S02-pc-interieur"
    f = Fig(900, 520, "L'intérieur d'un PC (vue schématique de la carte mère)", "Carte mère avec processeur, RAM, SSD M.2, carte graphique, connecteur d'alimentation, pile, ports arrière.")
    f.title_bar("L'intérieur d'un PC : la carte mère et ses invités")
    f.rect(40, 55, 520, 440, "#e8f5e9", GRN, 4, 10)   # carte mère
    f.text(300, 78, "CARTE MÈRE", 13, GRN, "middle", "700")
    # ports arrière (gauche)
    f.rect(40, 95, 60, 200, GRY, LINE, 2.5, 4); f.text(70, 92, "", 10)
    for i in range(4): p_usb(f, 70, 120 + i * 24)
    p_rj45(f, 70, 230); p_hdmi(f, 70, 265)
    # CPU + ventilo
    f.rect(150, 100, 110, 110, "#ffe0b2", ORA, 3, 8); f.circle(205, 155, 38, WHITE, ORA, 3)
    for a in range(0, 360, 60):
        import math
        f.line(205, 155, 205 + 34 * math.cos(math.radians(a)), 155 + 34 * math.sin(math.radians(a)), ORA, 3)
    f.badge(150, 100, "1", RED)
    # RAM (4 barrettes)
    for i in range(4):
        f.rect(330 + i * 26, 100, 18, 190, "#b3e5fc" if i < 2 else GRY, IND, 2, 3)
        for k in range(6): f.rect(332 + i * 26, 110 + k * 28, 14, 14, IND, IND, 1, 1)
    f.badge(380, 100, "2", RED)
    # chipset
    f.rect(240, 235, 50, 50, GRY, LINE, 2, 4); f.text(265, 265, "chipset", 10, MUTED)
    # PCIe + GPU
    f.rect(150, 335, 330, 18, GRY_D, LINE, 2, 3); f.badge(165, 344, "3", RED)
    # M.2
    f.rect(150, 295, 80, 26, "#d1c4e9", "#5e35b1", 2.5, 3); f.badge(150, 295, "4", RED)
    # SATA
    for i in range(4): f.rect(440, 380 + i * 14, 46, 10, "#fff9c4", YEL, 2, 2)
    f.badge(440, 380, "5", RED)
    # alim 24 pins
    f.rect(520, 150, 26, 120, "#f8bbd0", "#c2185b", 2.5, 3); f.badge(533, 150, "6", RED)
    # pile
    f.circle(200, 440, 18, "#eceff1", GRY_D, 3); f.badge(200, 420, "7", RED)
    # façade
    f.rect(120, 440, 200, 24, GRY, LINE, 2, 3); f.text(220, 457, "connecteurs de façade", 11, MUTED)
    f.badge(120, 440, "8", RED)
    # légende
    leg = [("1", "Processeur (CPU) + ventilateur", "le cerveau"), ("2", "Barrettes de RAM", "la mémoire de travail"), ("3", "Slot PCIe", "carte graphique, carte réseau…"),
           ("4", "SSD M.2", "le rangement (très rapide)"), ("5", "Connecteurs SATA", "disques HDD / SSD 2,5″"), ("6", "Alimentation 24 broches", "le courant"),
           ("7", "Pile de la carte mère", "garde l'heure et le BIOS"), ("8", "Connecteurs de façade", "boutons, USB avant")]
    for i, (n, t, b) in enumerate(leg):
        y = 85 + i * 50
        f.badge(600, y, n, RED, 11); f.text(620, y + 5, t, 14, INK, "start", "700"); f.text(620, y + 22, b, 12.5, MUTED, "start")
    f.save(out(d, "carte-mere.svg"))

    # HDD vs SSD
    f = Fig(900, 300, "Disque dur (HDD) et SSD", "Comparaison HDD à plateaux mécaniques et SSD à mémoire flash.")
    f.title_bar("Ranger les données : HDD ou SSD ?")
    f.rect(30, 60, 400, 220, GRY, LINE, 3, 12)
    f.circle(160, 165, 80, WHITE, LINE, 3); f.circle(160, 165, 20, GRY, LINE, 3)
    f.path("M160,165 L260,95", "none", ORA, 5); f.circle(260, 95, 8, ORA, ORA, 1)
    f.text(330, 110, "HDD", 22, IND, "middle", "700"); f.text(330, 145, "plateau qui tourne\n+ tête de lecture", 14, INK)
    f.text(330, 215, "lent · fragile aux chocs\nbruyant · pas cher au Go", 14, INK)
    f.rect(470, 60, 400, 220, "#ede7f6", "#5e35b1", 3, 12)
    f.rect(500, 100, 180, 120, WHITE, "#5e35b1", 2.5, 6)
    for i in range(4): f.rect(515 + i * 40, 125, 30, 70, "#b39ddb", "#5e35b1", 1.5, 3)
    f.text(780, 110, "SSD", 22, "#5e35b1", "middle", "700"); f.text(780, 145, "puces mémoire\n(aucune pièce mobile)", 14, INK)
    f.text(780, 215, "rapide · silencieux\nrésiste aux chocs", 14, INK)
    f.save(out(d, "hdd-ssd.svg"))

    # anatomie par analogie
    f = Fig(900, 330, "Le PC par analogie", "Processeur = cerveau, RAM = bureau, stockage = armoire, alimentation = cœur, carte mère = système nerveux.")
    f.title_bar("Un PC, c'est un peu comme toi")
    A = [("Processeur", "le CERVEAU", "réfléchit, calcule", ORA, ORA_L), ("RAM", "le BUREAU", "ce que j'utilise\nmaintenant\n(vidé quand\nj'éteins)", IND, IND_L),
         ("SSD / HDD", "l'ARMOIRE", "tout ce que\nje garde\n(même éteint)", "#5e35b1", "#ede7f6"), ("Alimentation", "le CŒUR", "distribue le\ncourant à tous\nles organes", RED, RED_L),
         ("Carte mère", "le SYSTÈME\nNERVEUX", "relie tout\nle monde", GRN, GRN_L)]
    for i, (n, a, b, c, fi) in enumerate(A):
        x = 15 + i * 177
        f.rect(x, 60, 165, 240, fi, c, 3, 14)
        f.text(x + 82, 95, n, 17, c, "middle", "700"); f.text(x + 82, 150, a, 17, INK, "middle", "700"); f.text(x + 82, 205, b, 14, INK)
    f.save(out(d, "analogie.svg"))


def s03():
    d = "S03-remonter-pc"
    f = Fig(900, 330, "RAM : sens d'insertion", "Une barrette de RAM possède un ergot décalé qui empêche de l'inverser ; on la pousse jusqu'au clic des deux clips.")
    f.title_bar("Insérer une barrette de RAM")
    f.rect(60, 190, 400, 30, "#a5d6a7", GRN, 3, 4); f.rect(80, 150, 12, 40, GRY, LINE, 2, 2); f.rect(428, 150, 12, 40, GRY, LINE, 2, 2)  # slot + clips
    f.text(260, 247, "Slot de la carte mère", 14, GRN, "middle", "700")
    f.rect(100, 70, 320, 60, "#b3e5fc", IND, 3, 4)
    for i in range(8): f.rect(112 + i * 38, 82, 28, 36, IND, IND, 1, 2)
    f.poly([(250, 130), (270, 130), (270, 140), (250, 140)], WHITE, IND, 2)
    f.text(240, 160, "", 1)
    f.line(260, 135, 260, 185, ORA, 5, arrow=True)
    f.callout(500, 80, 360, "L'ergot (l'encoche) est décalé : la barrette ne rentre que DANS UN SENS. Si ça ne rentre pas, on ne force pas : on la retourne.", YEL_L, YEL, 14.5)
    f.callout(500, 175, 360, "On pousse franchement jusqu'au CLIC : les deux clips latéraux se verrouillent.", GRN_L, GRN, 14.5)
    f.callout(500, 240, 360, "Pas de clic = mal enclenchée = le PC ne démarre pas (bips).", RED_L, RED, 14.5)
    f.save(out(d, "ram.svg"))

    f = Fig(900, 330, "L'ordre de démarrage (boot order)", "Liste ordonnée des supports sur lesquels le PC cherche un système : clé USB, SSD, réseau.")
    f.title_bar("L'ordre de démarrage : le PC cherche un système dans cet ordre")
    f.rect(40, 60, 380, 230, "#1a237e", "#1a237e", 2, 6)
    f.text(60, 92, "BIOS / UEFI – Boot", 15, "#ffffff", "start", "700")
    rows = ["1.  Clé USB", "2.  SSD  (Windows Boot Manager)", "3.  Démarrage réseau (PXE)", "4.  DVD"]
    for i, t in enumerate(rows):
        f.rect(55, 108 + i * 42, 350, 34, "#3949ab" if i != 1 else "#5c6bc0", "#9fa8da", 1.5, 3); f.text(70, 131 + i * 42, t, 15, "#ffffff", "start", "600")
    f.callout(450, 70, 410, "Le PC essaie le n°1 ; s'il n'y trouve pas de système, il passe au n°2, etc.", IND_L, IND, 15)
    f.callout(450, 140, 410, "Pour installer un système depuis une clé : la clé doit passer AVANT le SSD (ou on utilise le menu de démarrage, souvent F12).", ORA_L, ORA, 15)
    f.callout(450, 225, 410, "Après l'installation : on remet le SSD en premier.", GRN_L, GRN, 15)
    f.save(out(d, "ordre-boot.svg"))

    f = Fig(900, 320, "Diagnostic d'une panne au démarrage", "Arbre de décision : le PC ne démarre pas, que vérifier dans l'ordre.")
    f.title_bar("Le PC ne démarre pas : on vérifie dans l'ordre")
    S = [("1", "Alimentation", "Câble secteur\nbranché ?\nInterrupteur sur I ?"), ("2", "Connecteurs", "24 broches et\nprise CPU bien\nenfoncées ?"),
         ("3", "RAM", "Barrettes\nclipsées ?\n(bips au démarrage)"), ("4", "Façade", "Bouton power\nbranché sur la\ncarte mère ?"), ("5", "Boot", "Le bon support\nest-il en\npremier ?")]
    for i, (n, t, b) in enumerate(S):
        x = 15 + i * 177
        f.rect(x, 60, 160, 200, IND_L, IND, 3, 14); f.badge(x + 80, 60, n, IND, 16)
        f.text(x + 80, 105, t, 17, IND, "middle", "700"); f.text(x + 80, 140, b, 13.5, INK)
        if i < 4: f.arrow(x + 162, 160, x + 175, 160, LINE, 3)
    f.text(450, 295, "On part du plus simple (le courant) vers le plus fin (le logiciel).", 15, MUTED, "middle", "600", italic=True)
    f.save(out(d, "diagnostic.svg"))


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s01", "s02", "s03"]):
        globals()[w](); print("OK", w)
