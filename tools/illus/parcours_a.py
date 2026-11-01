#!/usr/bin/env python3
"""Illustrations du parcours de mise à niveau – M01 à M03."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "terminale", "mise-a-niveau", "images"))
out = lambda n: os.path.join(ROOT, n)

# couleurs des fils T568B
WIRE = [("blanc/orange", "#ef6c00", True), ("orange", "#ef6c00", False), ("blanc/vert", "#2e9d4a", True), ("bleu", "#1e63c9", False),
        ("blanc/bleu", "#1e63c9", True), ("vert", "#2e9d4a", False), ("blanc/marron", "#8d5a3b", True), ("marron", "#8d5a3b", False)]


def wire(f, x, y, w, h, color, striped, r=4):
    """Un fil : plein, ou blanc rayé de la couleur de sa paire."""
    if not striped:
        f.rect(x, y, w, h, color, "#222", 1.5, r)
        return
    f.rect(x, y, w, h, "#fafafa", "#222", 1.5, r)
    n = int(h // 14)
    for k in range(n):
        yy = y + 6 + k * 14
        f.poly([(x + 1, yy), (x + w - 1, yy - 7), (x + w - 1, yy + 1), (x + 1, yy + 8)], color, color, 0)


def m01_reseau():
    f = Fig(1000, 480, "Le réseau du cabinet du Parc", "Internet, la box, le switch, le serveur, les postes, l'imprimante et la borne Wi-Fi du cabinet.")
    f.title_bar("Le réseau du cabinet du Parc : qui est relié à quoi ?")
    f.line(130, 120, 232, 120, LINE, 3); f.line(308, 120, 458, 120, LINE, 3); f.line(542, 120, 725, 112, LINE, 3)
    items = [("pc", 130, "PC secrétaire", "Accueil"), ("printer", 330, "Imprimante", "Accueil"), ("pc", 530, "PC praticien", "Salle de soins"), ("ap", 740, "Borne Wi-Fi", "Salle d'attente")]
    for k, x, l, s in items:
        f.line(500, 112, x, 330 - (26 if k != "ap" else 22), LINE, 2.5)
    for k, x, l, s in items:
        node(f, k, x, 330, l); f.text(x, 330 + 55, s, 12.5, MUTED)
    node(f, "cloud", 90, 120, "Internet")
    node(f, "box", 270, 120, "Box", "l'accès Internet")
    node(f, "switch", 500, 120, "Switch", "le « carrefour »")
    node(f, "server", 760, 110, "Serveur", "adresses, fichiers")
    node(f, "phone", 880, 330, "Patient")
    f.line(765, 322, 855, 322, TEAL, 3, "3 7"); f.text(812, 305, "Wi-Fi", 13, TEAL, "middle", "700")
    f.rect(40, 425, 920, 32, YEL_L, YEL, 2, 8)
    f.text(500, 447, "Les traits pleins sont des câbles réseau (RJ45). Le pointillé vert est une liaison sans fil.", 14, INK)
    f.save(out("m01-reseau-cabinet.svg"))


def m01_baie():
    f = Fig(1000, 560, "Une baie de brassage vue de face", "Une baie 19 pouces : panneau de brassage, switch, serveur, box et onduleur, avec les câbles venant des prises murales et les cordons de brassage.")
    f.title_bar("Dans le local technique : la baie de brassage")
    # armoire
    f.rect(260, 70, 330, 450, "#cfd8dc", "#455a64", 4, 6)
    f.rect(275, 82, 300, 426, "#263238", "#263238", 1, 3)
    def unit(y, h, label, fill, stroke):
        f.rect(285, y, 280, h, fill, stroke, 2.5, 3)
        f.text(425, y + h / 2 + 5, label, 14, INK, "middle", "700")
    # panneau
    f.rect(285, 95, 280, 62, "#eceff1", "#455a64", 2.5, 3)
    for i in range(12):
        f.rect(293 + i * 22.6, 108, 17, 15, "#263238", "#90a4ae", 1, 2)
        f.text(301.5 + i * 22.6, 143, f"A{i+1:02d}", 8.5, MUTED)
    f.text(425, 152, "", 1)
    # passe-câbles
    f.rect(285, 165, 280, 22, "#37474f", "#90a4ae", 1.5, 2)
    # switch
    f.rect(285, 197, 280, 52, TEAL_L, TEAL, 2.5, 3)
    for i in range(12):
        f.rect(293 + i * 22.6, 212, 17, 15, WHITE, TEAL, 1.5, 2)
        f.circle(301.5 + i * 22.6, 236, 2.2, GRN if i not in (5, 6, 11) else GRY_D, GRN if i not in (5, 6, 11) else GRY_D, 1)
    f.text(425, 206, "", 1)
    # serveur
    f.rect(285, 262, 280, 56, IND_L, IND, 2.5, 3)
    f.rect(295, 272, 120, 34, WHITE, IND, 1.5, 2)
    for i in range(4): f.line(305, 280 + i * 7, 405, 280 + i * 7, IND_M, 1.5)
    f.circle(530, 290, 5, GRN, GRN, 1); f.circle(546, 290, 5, YEL, YEL, 1)
    # box
    f.rect(285, 330, 280, 42, ORA_L, ORA, 2.5, 3); f.circle(540, 351, 4, GRN, GRN, 1)
    f.rect(300, 343, 70, 16, WHITE, ORA, 1.5, 2)
    # onduleur
    f.rect(285, 384, 280, 62, "#fff8e1", "#8d6e63", 2.5, 3); f.text(425, 420, "ONDULEUR", 13, "#6d4c41", "middle", "700")
    f.rect(285, 456, 280, 40, "#455a64", "#455a64", 1, 3); f.text(425, 481, "prise multiple protégée", 12, "#cfd8dc")
    # cordons de brassage (panneau → switch)
    cols = [IND, ORA, TEAL, "#8e24aa", RED, GRN]
    for i, c in enumerate(cols):
        x1 = 301.5 + i * 22.6 * 2; x2 = 301.5 + i * 22.6 * 2 + (10 if i % 2 else -6)
        f.path(f"M{x1},{160} C{x1+8},{185} {x2-8},{190} {x2},{212}", "none", c, 3)
    # câbles venant des prises (haut)
    f.rect(330, 36, 190, 24, YEL_L, YEL, 2, 6); f.text(425, 53, "vers les prises murales", 13, INK, "middle", "700")
    for i in range(0, 12, 2):
        f.line(301.5 + i * 22.6, 108, 301.5 + i * 22.6, 62, "#455a64", 4)
    # annotations gauche et droite
    def lab(y, txt, sub, side, c):
        if side == "L":
            f.line(256, y, 285, y, c, 2); f.text(245, y - 4, txt, 15, c, "end", "700"); f.text(245, y + 14, sub, 12.5, MUTED, "end")
        else:
            f.line(565, y, 596, y, c, 2); f.text(606, y - 4, txt, 15, c, "start", "700"); f.text(606, y + 14, sub, 12.5, MUTED, "start")
    lab(125, "1  Panneau de brassage", "arrivée de toutes les prises", "L", "#455a64")
    lab(223, "2  Switch", "il relie les équipements", "L", TEAL)
    lab(290, "3  Serveur", "services pour tout le cabinet", "L", IND)
    lab(351, "4  Box", "la sortie vers Internet", "L", ORA)
    lab(415, "5  Onduleur", "garde le courant quelques minutes", "L", "#6d4c41")
    f.text(606, 150, "cordons de", 15, "#8e24aa", "start", "700"); f.text(606, 168, "brassage", 15, "#8e24aa", "start", "700")
    f.text(606, 188, "courts, de couleurs différentes", 12.5, MUTED, "start")
    f.line(598, 190, 520, 190, "#8e24aa", 2, "4 4", arrow=True)
    f.text(606, 250, "câble fixe = ne se déplace pas", 12.5, MUTED, "start")
    f.text(606, 268, "cordon = se débranche, se déplace", 12.5, MUTED, "start")
    f.save(out("m01-baie.svg"))


def m01_switch_routeur():
    f = Fig(1000, 430, "Switch ou routeur ?", "À gauche, un switch relie des équipements d'un même réseau. À droite, un routeur relie deux réseaux différents.")
    f.title_bar("Switch ou routeur : ne pas confondre")
    f.rect(30, 60, 450, 350, IND_L, IND, 3, 14)
    f.rect(520, 60, 450, 350, ORA_L, ORA, 3, 14)
    f.text(255, 92, "Le SWITCH", 20, IND, "middle", "700"); f.text(255, 116, "relie des équipements d'UN MÊME réseau", 14, INK)
    f.text(745, 92, "Le ROUTEUR", 20, ORA, "middle", "700"); f.text(745, 116, "relie DEUX réseaux différents", 14, INK)
    for x, y, k in [(90, 190, "pc"), (90, 320, "printer"), (420, 190, "laptop"), (420, 320, "server")]:
        f.line(255, 224, x + (28 if x < 255 else -28), y, LINE, 2.5)
    for x, y, k in [(90, 190, "pc"), (90, 320, "printer"), (420, 190, "laptop"), (420, 320, "server")]:
        node(f, k, x, y)
    node(f, "switch", 255, 224, "switch")
    f.text(255, 370, "Réseau 192.168.10.0/24", 14, IND, "middle", "700")
    f.text(255, 392, "ils se parlent directement", 13, MUTED)
    f.rect(545, 140, 170, 210, "#ffffff", ORA, 2.5, 12, "6 5"); f.text(630, 164, "Réseau A", 14, ORA, "middle", "700"); f.text(630, 182, "192.168.10.0/24", 12, MUTED)
    f.rect(775, 140, 170, 210, "#ffffff", TEAL, 2.5, 12, "6 5"); f.text(860, 164, "Réseau B", 14, TEAL, "middle", "700"); f.text(860, 182, "192.168.20.0/24", 12, MUTED)
    f.line(710, 250, 640, 275, ORA, 3); f.line(780, 250, 855, 275, TEAL, 3)
    node(f, "router", 745, 252, "routeur")
    node(f, "pc", 600, 275); node(f, "pc", 660, 330); node(f, "laptop", 890, 275); node(f, "phone", 835, 330)
    f.text(745, 396, "pour passer d'un réseau à l'autre, on passe par lui", 13, MUTED)
    f.save(out("m01-switch-routeur.svg"))


def m01_securite():
    f = Fig(1000, 400, "Six risques d'un chantier réseau", "Six cartes : risque électrique, coupure, chute de hauteur, câbles au sol, coupure de service et données du client.")
    f.title_bar("Avant de toucher au matériel : six risques à connaître")
    cards = [("Électrique", "câble abîmé,", "multiprise surchargée", RED, "bolt"), ("Coupure", "cutter, outil de pose,", "pince coupante", ORA, "blade"),
             ("Hauteur", "plafond technique,", "borne Wi-Fi", IND, "ladder"), ("Chute", "câbles au sol", "dans le passage", YEL, "trip"),
             ("Service", "couper ce qui", "fonctionne", TEAL, "plug"), ("Données", "dossiers patients :", "ne pas les lire", "#8e24aa", "lock")]
    for i, (t, a, b, c, ic) in enumerate(cards):
        x = 30 + (i % 3) * 318; y = 62 + (i // 3) * 150
        f.rect(x, y, 304, 136, WHITE, c, 3, 12); f.rect(x, y, 92, 136, c, c, 0, 12); f.rect(x + 80, y, 12, 136, c, c, 0, 0)
        cx, cy = x + 46, y + 68
        if ic == "bolt": f.poly([(cx + 6, cy - 30), (cx - 14, cy + 4), (cx - 1, cy + 4), (cx - 8, cy + 30), (cx + 16, cy - 8), (cx + 2, cy - 8)], YEL, WHITE, 2)
        elif ic == "blade": f.poly([(cx - 24, cy + 20), (cx + 18, cy - 24), (cx + 26, cy - 16), (cx - 16, cy + 28)], "#eceff1", WHITE, 2); f.rect(cx - 30, cy + 14, 22, 18, "#37474f", WHITE, 2, 3)
        elif ic == "ladder":
            f.line(cx - 14, cy - 30, cx - 22, cy + 30, WHITE, 5); f.line(cx + 14, cy - 30, cx + 22, cy + 30, WHITE, 5)
            for k in range(4): f.line(cx - 17 + k * 0.6, cy - 18 + k * 16, cx + 17 - k * 0.6, cy - 18 + k * 16, WHITE, 4)
        elif ic == "trip":
            f.path(f"M{cx-30},{cy+16} C{cx-10},{cy-14} {cx+10},{cy+30} {cx+30},{cy}", "none", WHITE, 6)
            f.warn(cx, cy - 18, 12)
        elif ic == "plug":
            f.rect(cx - 16, cy - 8, 32, 26, WHITE, WHITE, 0, 5); f.line(cx - 8, cy - 8, cx - 8, cy - 26, WHITE, 5); f.line(cx + 8, cy - 8, cx + 8, cy - 26, WHITE, 5); f.line(cx, cy + 18, cx, cy + 32, WHITE, 5)
        else:
            f.rect(cx - 20, cy - 4, 40, 32, WHITE, WHITE, 0, 5); f.path(f"M{cx-12},{cy-4} v-12 a12,12 0 0 1 24,0 v12", "none", WHITE, 5); f.circle(cx, cy + 12, 4, c, c, 1)
        f.text(x + 106, y + 40, t, 19, c, "start", "700"); f.text(x + 106, y + 72, a, 14, INK, "start"); f.text(x + 106, y + 92, b, 14, INK, "start")
    f.text(500, 385, "Règle d'or : on réfléchit, on prévient, puis on intervient.", 15, MUTED, "middle", "700")
    f.save(out("m01-risques.svg"))


def m02_rj45():
    f = Fig(1000, 530, "Le code couleur T568B", "Huit fils numérotés de 1 à 8 avec leur couleur en norme T568B, groupés en quatre paires torsadées : orange, vert, bleu et marron.")
    f.title_bar("Les 8 fils, de gauche à droite, en norme T568B")
    # paires (fond)
    pairs = [(0, 1, "paire orange", "#ef6c00"), (2, 5, "paire verte", "#2e9d4a"), (3, 4, "paire bleue", "#1e63c9"), (6, 7, "paire marron", "#8d5a3b")]
    x0 = 90; step = 100
    for i, (n, col, st) in enumerate(WIRE):
        x = x0 + i * step
        wire(f, x, 90, 56, 230, col, st, 6)
        f.badge(x + 28, 360, str(i + 1), IND, 18)
        f.text(x + 28, 410, n, 14, INK, "middle", "700")
    # accolades de paires
    for a, b, t, c in pairs:
        xa = x0 + a * step + 28; xb = x0 + b * step + 28
        y = {(0, 1): 462, (2, 5): 440, (3, 4): 462, (6, 7): 462}[(a, b)]
        f.path(f"M{xa},{432} L{xa},{y} L{xb},{y} L{xb},{432}", "none", c, 2.5)
        f.text((xa + xb) / 2, y + 22, t, 13, c, "middle", "700")
    f.rect(60, 62, 880, 24, YEL_L, YEL, 2, 6)
    f.text(500, 79, "Les fils « blanc/couleur » sont blancs avec des rayures de la couleur de leur paire", 13.5, INK)
    f.text(40, 365, "broche", 12.5, MUTED, "start")
    f.text(500, 508, "À retenir : orange (1-2), vert (3 et 6, la paire est « coupée en deux »), bleu au milieu (4-5), marron à la fin (7-8).", 13, MUTED)
    f.save(out("m02-t568b.svg"))


def m02_connecteur():
    f = Fig(1000, 400, "Le connecteur RJ45 vu de face", "Un connecteur RJ45, ergot vers le bas, contacts vers l'observateur : la broche 1 est à gauche, la broche 8 à droite.")
    f.title_bar("Sens de lecture d'un connecteur RJ45")
    # connecteur vu de face (contacts vers soi, ergot vers le bas)
    f.rect(330, 80, 340, 190, "#e3f2fd", "#37474f", 4, 10)
    f.rect(350, 100, 300, 70, "#cfd8dc", "#37474f", 2, 4)
    for i in range(8):
        x = 360 + i * 36
        f.rect(x, 108, 22, 56, "#ffd54f", "#b8860b", 1.5, 2)
        f.badge(x + 11, 200, str(i + 1), IND, 12)
    f.rect(440, 262, 120, 26, "#e3f2fd", "#37474f", 3, 4)  # ergot
    f.text(500, 281, "ergot", 12.5, MUTED, "middle", "700")
    f.arrow(250, 135, 330, 135, RED, 3); f.text(230, 128, "broche 1", 15, RED, "end", "700"); f.text(230, 148, "(à gauche)", 13, MUTED, "end")
    f.arrow(750, 135, 672, 135, GRN, 3); f.text(770, 128, "broche 8", 15, GRN, "start", "700"); f.text(770, 148, "(à droite)", 13, MUTED, "start")
    f.text(500, 320, "Tiens le connecteur avec les contacts dorés tournés vers toi et l'ergot vers le bas.", 15, INK, "middle", "700")
    f.text(500, 346, "Câble : le fil 1 (blanc/orange) va dans la fente de gauche.", 14, MUTED)
    f.save(out("m02-connecteur.svg"))


def m02_paires():
    f = Fig(1000, 420, "Pourquoi les paires sont torsadées", "Une coupe d'un câble avec quatre paires torsadées, une croix de séparation et une gaine, puis une paire vue de côté.")
    f.title_bar("À l'intérieur d'un câble réseau : 4 paires torsadées")
    f.circle(220, 215, 150, "#cfd8dc", "#455a64", 5); f.circle(220, 215, 128, "#eceff1", "#90a4ae", 2)
    f.line(220, 100, 220, 330, "#b0bec5", 8); f.line(105, 215, 335, 215, "#b0bec5", 8)
    for (cx, cy, c, n) in [(160, 155, "#ef6c00", "orange"), (280, 155, "#2e9d4a", "vert"), (160, 275, "#1e63c9", "bleu"), (280, 275, "#8d5a3b", "marron")]:
        f.circle(cx - 14, cy, 18, c, "#222", 2); f.circle(cx + 14, cy, 18, "#fafafa", "#222", 2)
        f.poly([(cx + 4, cy - 12), (cx + 20, cy - 12), (cx + 20, cy), (cx + 8, cy + 12)], c, c, 0) if False else None
    f.text(220, 60, "coupe du câble", 15, MUTED, "middle", "700")
    f.arrow(40, 110, 100, 150, MUTED, 2); f.text(38, 100, "gaine", 14, INK, "start", "700")
    f.arrow(225, 380, 220, 345, MUTED, 2); f.text(225, 400, "croix de séparation", 13, INK, "middle", "700")
    # paire vue de côté
    f.text(720, 70, "une paire torsadée (vue de côté)", 15, MUTED, "middle", "700")
    import math
    for k, col in ((0, "#ef6c00"), (1, "#bdbdbd")):
        pts = []
        for t in range(0, 241, 4):
            x = 520 + t * 1.65; y = 150 + 26 * math.sin(math.radians(t * 3 + k * 180))
            pts.append(f"{x:.1f},{y:.1f}")
        f.add(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#222" stroke-width="9" stroke-linecap="round"/>')
        f.add(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="6" stroke-linecap="round"/>')
    f.rect(470, 210, 500, 190, YEL_L, YEL, 2, 12)
    f.text(490, 240, "Pourquoi tordre les fils ?", 16, INK, "start", "700")
    f.text(490, 268, "• Les perturbations électriques (moteur, néon,", 14, INK, "start"); f.text(500, 288, "câble voisin) touchent les deux fils de la même façon.", 14, INK, "start")
    f.text(490, 314, "• Comme le message est lu par différence entre", 14, INK, "start"); f.text(500, 334, "les deux fils, ces perturbations s'annulent.", 14, INK, "start")
    f.text(490, 362, "• Détorsader trop près du connecteur annule ce bénéfice.", 14, INK, "start")
    f.save(out("m02-paires.svg"))


def m02_pose():
    f = Fig(1000, 430, "Poser une prise en cinq étapes", "Cinq étapes : dénuder, détorsader, ranger les fils, piquer et couper, tester.")
    f.title_bar("Câbler une prise RJ45 : cinq gestes")
    steps = [("1", "Dénuder", "2 à 3 cm de gaine,\nsans entailler\nles fils"), ("2", "Détorsader", "au minimum\n(≈ 13 mm)\net redresser"), ("3", "Ranger", "dans l'ordre T568B,\nrepéré sur le\nmodule"),
             ("4", "Piquer", "enfoncer chaque\nfil avec l'outil,\nqui coupe l'excédent"), ("5", "Tester", "testeur : 8 voyants\ndans l'ordre\nPASS")]
    for i, (n, t, d) in enumerate(steps):
        x = 24 + i * 192
        f.rect(x, 58, 180, 350, WHITE, IND, 3, 12)
        f.rect(x, 58, 180, 40, IND, IND, 0, 12); f.rect(x, 80, 180, 18, IND, IND, 0, 0)
        f.text(x + 90, 85, f"{n}  {t}", 17, WHITE, "middle", "700")
        cx = x + 90
        if i == 0:
            f.rect(cx - 70, 150, 90, 40, "#cfd8dc", "#455a64", 2.5, 6)
            for k, c in enumerate(["#ef6c00", "#2e9d4a", "#1e63c9", "#8d5a3b"]): f.line(cx + 20, 160 + k * 8, cx + 66, 160 + k * 8, c, 4)
            f.line(cx + 12, 142, cx + 12, 198, RED, 2.5, "4 3"); f.text(cx + 12, 216, "coupe ici", 12, RED, "middle", "700")
        elif i == 1:
            import math
            for k, c in enumerate(["#ef6c00", "#2e9d4a", "#1e63c9", "#8d5a3b"]):
                f.path(f"M{cx-60},{150+k*14} C{cx-20},{150+k*14} {cx-10},{140+k*14-6*k} {cx+60},{136+k*20}", "none", c, 4)
            f.rect(cx - 70, 138, 30, 62, "#cfd8dc", "#455a64", 2, 4)
        elif i == 2:
            for k, (n_, col, st) in enumerate(WIRE): wire(f, cx - 64 + k * 17, 140, 12, 70, col, st, 2)
            f.text(cx, 232, "1 2 3 4 5 6 7 8", 12.5, MUTED, "middle", "700")
        elif i == 3:
            f.rect(cx - 52, 170, 104, 40, "#e3f2fd", "#37474f", 3, 5)
            for k in range(8): f.line(cx - 42 + k * 12, 150, cx - 42 + k * 12, 170, "#555", 3)
            f.rect(cx - 12, 108, 24, 40, "#ffb74d", "#e65100", 2.5, 4); f.arrow(cx, 112, cx, 168, RED, 2.5)
        else:
            f.rect(cx - 60, 140, 120, 34, "#263238", "#263238", 1, 5)
            for k in range(8): f.circle(cx - 49 + k * 14, 157, 4, GRN, GRN, 1)
            f.text(cx, 200, "PASS", 22, GRN, "middle", "700")
        for j, ln in enumerate(d.split("\n")): f.text(x + 90, 276 + j * 22, ln, 13.5, INK)
    f.save(out("m02-pose.svg"))


def m02_testeur():
    f = Fig(1000, 470, "Lire un testeur de câble", "Quatre résultats possibles d'un testeur : câble correct, fil coupé, fils inversés, court-circuit, avec la lecture des huit voyants.")
    f.title_bar("Le testeur raconte l'histoire de chaque fil")
    cases = [("Câble correct", GRN, [1, 2, 3, 4, 5, 6, 7, 8], "Les 8 voyants s'allument\ndans l'ordre, à l'identique\ndes deux côtés.", "PASS"),
             ("Fil coupé", RED, [1, 2, 3, None, 5, 6, 7, 8], "Un voyant reste éteint :\nle fil 4 est coupé ou\nmal enfoncé.", "FAIL"),
             ("Fils inversés", RED, [1, 2, 6, 4, 5, 3, 7, 8], "Côté distant, l'ordre change :\n3 et 6 sont permutés\n(un côté en T568A ?).", "FAIL"),
             ("Court-circuit", RED, [1, 2, 3, "45", "45", 6, 7, 8], "Deux fils se touchent :\nles voyants 4 et 5\ns'allument ensemble.", "FAIL")]
    for i, (t, c, seq, d, v) in enumerate(cases):
        x = 24 + i * 245
        f.rect(x, 58, 232, 390, WHITE, c, 3, 12); f.rect(x, 58, 232, 40, c, c, 0, 12); f.rect(x, 80, 232, 18, c, c, 0, 0)
        f.text(x + 116, 85, t, 17, WHITE, "middle", "700")
        f.text(x + 116, 128, "testeur principal", 12, MUTED); f.rect(x + 20, 136, 192, 40, "#263238", "#263238", 1, 6)
        for k in range(8): f.circle(x + 40 + k * 22, 156, 6, "#ffeb3b" if True else GRY_D, "#b8860b", 1); f.text(x + 40 + k * 22, 192, str(k + 1), 11, MUTED)
        f.text(x + 116, 228, "testeur distant", 12, MUTED); f.rect(x + 20, 236, 192, 40, "#263238", "#263238", 1, 6)
        for k in range(8):
            s = seq[k]
            col = "#ffeb3b" if s is not None else "#455a64"
            f.circle(x + 40 + k * 22, 256, 6, col, "#b8860b" if s is not None else "#37474f", 1)
            lab = "–" if s is None else (str(s) if not isinstance(s, str) else "4+5")
            f.text(x + 40 + k * 22, 292, lab, 10.5, RED if (s is None or s != k + 1) else MUTED, "middle", "700")
        f.text(x + 116, 336, v, 26, c, "middle", "700")
        for j, ln in enumerate(d.split("\n")): f.text(x + 116, 372 + j * 20, ln, 13, INK)
    f.save(out("m02-testeur.svg"))


def m02_chaine():
    f = Fig(1000, 400, "De la prise murale au switch", "La liaison complète : prise murale, câble fixe de 90 mètres maximum, panneau de brassage, cordon de brassage, switch. Même étiquette P9 sur la prise, le panneau et le cordon.")
    f.title_bar("La liaison complète d'une prise au switch")
    f.rect(30, 150, 110, 90, WHITE, GRY_D, 3, 8); f.text(85, 118, "Salle de soins 2", 14, MUTED, "middle", "700")
    f.rect(55, 168, 60, 54, "#fafafa", "#455a64", 3, 6); f.rect(70, 182, 30, 26, "#263238", "#263238", 1, 3)
    f.rect(78, 232, 44, 22, YEL_L, YEL, 2, 3); f.text(100, 248, "P9", 13, INK, "middle", "700")
    f.text(85, 280, "prise murale", 14, INK, "middle", "700"); f.text(85, 298, "(keystone)", 12.5, MUTED)
    f.line(140, 195, 410, 195, "#455a64", 6); f.text(275, 178, "câble fixe (dans les murs)", 15, INK, "middle", "700"); f.text(275, 232, "90 m au maximum", 14, RED, "middle", "700")
    f.rect(410, 150, 150, 90, "#eceff1", "#455a64", 3, 6)
    for i in range(6): f.rect(420 + i * 22, 170, 17, 15, "#263238", "#90a4ae", 1, 2)
    f.rect(500, 200, 44, 22, YEL_L, YEL, 2, 3); f.text(522, 216, "P9", 13, INK, "middle", "700")
    f.text(485, 280, "panneau de brassage", 14, INK, "middle", "700"); f.text(485, 298, "(port A09)", 12.5, MUTED)
    f.text(485, 262, "", 1)
    f.path("M530,185 C575,185 600,170 650,185", "none", ORA, 5); f.text(600, 150, "cordon de brassage", 15, ORA, "middle", "700")
    f.rect(578, 200, 44, 22, YEL_L, YEL, 2, 3); f.text(600, 216, "P9", 13, INK, "middle", "700")
    f.text(600, 262, "10 m au maximum", 14, RED, "middle", "700")
    f.rect(640, 150, 210, 90, TEAL_L, TEAL, 3, 6)
    for i in range(8): f.rect(652 + i * 23, 172, 18, 16, WHITE, TEAL, 1.5, 2); f.circle(661 + i * 23, 210, 2.5, GRN if i != 7 else GRY_D, GRN if i != 7 else GRY_D, 1)
    f.text(745, 280, "switch", 14, INK, "middle", "700"); f.text(745, 298, "(port 1/10)", 12.5, MUTED)
    f.rect(30, 330, 940, 50, YEL_L, YEL, 2, 10)
    f.text(500, 352, "Lien permanent : 90 m max de câble fixe + cordons : 100 m au total.", 14.5, INK, "middle", "700")
    f.text(500, 372, "Même repère (P9) sur la prise, le panneau et le cordon : le prochain technicien s'y retrouve.", 13.5, MUTED)
    f.save(out("m02-liaison.svg"))


def m03_ip():
    f = Fig(1000, 470, "Une adresse IP et son masque", "L'adresse 192.168.10.25 en quatre octets de huit bits, avec le masque 255.255.255.0 qui sépare la partie réseau de la partie équipement.")
    f.title_bar("Lire une adresse IP : 4 nombres, 32 bits")
    octs = [("192", "11000000"), ("168", "10101000"), ("10", "00001010"), ("25", "00011001")]
    for i, (n, b) in enumerate(octs):
        x = 80 + i * 220
        net = i < 3
        f.rect(x, 70, 190, 80, IND_L if net else ORA_L, IND if net else ORA, 3, 10)
        f.text(x + 95, 125, n, 40, IND if net else ORA, "middle", "700")
        if i < 3: f.circle(x + 205, 140, 5, INK, INK, 1)
        f.rect(x, 168, 190, 40, WHITE, IND if net else ORA, 2, 8)
        for k, ch in enumerate(b): f.mono(x + 12 + k * 21.5, 195, ch, 19, IND if net else ORA, "start", "700")
        f.text(x + 95, 232, f"octet n°{i+1} = 8 bits", 12.5, MUTED)
    f.text(500, 60, "adresse IP : 192.168.10.25", 0.1, INK)
    # masque
    for i, (n, b) in enumerate([("255", "11111111"), ("255", "11111111"), ("255", "11111111"), ("0", "00000000")]):
        x = 80 + i * 220
        f.rect(x, 262, 190, 38, GRY, GRY_D, 2, 8)
        f.text(x + 95, 290, n, 24, INK, "middle", "700")
    f.text(40, 255, "MASQUE", 13, MUTED, "start", "700")
    f.path("M80,325 L80,345 L850,345 L850,325", "none", IND, 3); f.text(465, 372, "partie RÉSEAU : « dans quelle rue j'habite » (24 bits à 1)", 15, IND, "middle", "700")
    f.path("M870,325 L870,345 L1000,345", "none", ORA, 0.1)
    f.rect(740, 395, 220, 56, ORA_L, ORA, 2.5, 10)
    f.text(850, 418, "partie ÉQUIPEMENT", 14, ORA, "middle", "700"); f.text(850, 438, "« quel numéro dans la rue »", 12.5, INK)
    f.rect(40, 395, 680, 56, YEL_L, YEL, 2, 10)
    f.text(380, 418, "Écriture courte : 192.168.10.25 /24  (« 24 bits de réseau »)", 14.5, INK, "middle", "700")
    f.text(380, 439, "Deux équipements dont la partie réseau est identique sont dans le même réseau.", 13, MUTED)
    f.save(out("m03-adresse-ip.svg"))


def m03_passerelle():
    f = Fig(1000, 450, "La passerelle", "Un poste parle directement à un voisin du même réseau, mais passe par sa passerelle pour joindre un autre réseau ou Internet.")
    f.title_bar("Même réseau : direct. Autre réseau : par la passerelle")
    f.rect(30, 70, 520, 330, IND_L, IND, 3, 16); f.text(60, 102, "Réseau du cabinet 192.168.10.0/24", 16, IND, "start", "700")
    node(f, "pc", 120, 190, "PC-A", "192.168.10.25"); node(f, "printer", 120, 330, "Imprimante", "192.168.10.20")
    node(f, "switch", 300, 260, "switch"); node(f, "router", 470, 260, "Passerelle", "192.168.10.1")
    f.line(120, 215, 280, 255, LINE, 2.5); f.line(120, 340, 280, 270, LINE, 2.5); f.line(342, 260, 432, 260, LINE, 3)
    f.arrow(165, 175, 165, 165, GRN, 1)
    f.path("M150,160 C220,120 260,120 300,236", "none", GRN, 4, arrow=True); f.badge(222, 128, "1", GRN, 13)
    f.path("M148,200 C230,225 380,200 440,238", "none", RED, 4, arrow=True); f.badge(300, 214, "2", RED, 13)
    f.line(505, 260, 600, 260, LINE, 3); node(f, "box", 640, 260, "Box"); f.line(678, 260, 790, 260, LINE, 3); node(f, "cloud", 850, 260, "Internet")
    f.rect(560, 150, 400, 70, YEL_L, YEL, 2, 10)
    f.text(760, 175, "La passerelle est l'adresse du routeur de ton réseau.", 14, INK, "middle", "700")
    f.text(760, 197, "Elle est toujours dans le MÊME réseau que le poste.", 13.5, MUTED)
    f.badge(60, 424, "1", GRN, 12); f.text(80, 429, "vers l'imprimante : directement, car même réseau", 14, GRN, "start", "700")
    f.badge(540, 424, "2", RED, 12); f.text(560, 429, "vers Internet : par la passerelle, car autre réseau", 14, RED, "start", "700")
    f.save(out("m03-passerelle.svg"))


def m03_dora():
    f = Fig(1000, 520, "Le dialogue DHCP : DORA", "Quatre messages entre un poste et le serveur DHCP : Discover, Offer, Request, Acknowledge.")
    cols = [(180, "Poste (PC)", "n'a pas d'adresse", IND), (820, "Serveur DHCP", "192.168.10.5", TEAL)]
    msgs = [(0, 1, "①  DISCOVER : « Y a-t-il un serveur DHCP ? »", IND, False), (1, 0, "②  OFFER : « Je te propose 192.168.10.101 »", TEAL, False),
            (0, 1, "③  REQUEST : « D'accord, je prends cette adresse »", IND, False), (1, 0, "④  ACK : « Confirmé pour 8 heures, passerelle .1, DNS .1 »", TEAL, False)]
    f.title_bar("Obtenir une adresse automatiquement : DORA")
    sequence(f, cols, msgs, top=50, step=62, textsize=14)
    f.rect(40, 440, 920, 60, YEL_L, YEL, 2, 10)
    f.text(500, 464, "Discover / Offer / Request / Acknowledge. Si personne ne répond, Windows prend une adresse 169.254.x.x :", 14, INK)
    f.text(500, 486, "c'est le signe que le DHCP est injoignable (serveur éteint, câble, VLAN, relais).", 14, MUTED)
    f.save(out("m03-dora.svg"))


def m03_dns():
    f = Fig(1000, 380, "Le DNS, annuaire d'Internet", "Le poste demande au DNS l'adresse du nom www.exemple.fr, reçoit 203.0.113.10, puis contacte ce serveur.")
    f.title_bar("Le DNS traduit un nom en adresse IP")
    node(f, "pc", 120, 200, "Ton PC"); node(f, "server", 500, 130, "Serveur DNS", "l'annuaire"); node(f, "server", 880, 250, "Serveur web", "203.0.113.10")
    f.path("M160,170 C250,110 340,110 462,120", "none", IND, 4, arrow=True); f.text(250, 90, "①  « Quelle est l'adresse de", 13.5, IND, "start", "700"); f.text(250, 107, "www.exemple.fr ? »", 13.5, IND, "start", "700")
    f.path("M462,170 C380,230 280,240 168,215", "none", TEAL, 4, arrow=True); f.text(250, 262, "②  « C'est 203.0.113.10 »", 13.5, TEAL, "start", "700")
    f.path("M165,245 C300,335 700,335 845,285", "none", ORA, 4, arrow=True); f.text(500, 345, "③  le PC contacte directement 203.0.113.10", 13.5, ORA, "middle", "700")
    f.save(out("m03-dns.svg"))


def m03_ipconfig():
    f = Fig(1000, 470, "Lire le résultat de ipconfig /all", "Une fenêtre de commandes avec le résultat d'ipconfig /all : adresse physique, DHCP activé, adresse IPv4, masque, passerelle, serveur DHCP et serveur DNS, avec des repères.")
    f.title_bar("Lire un « ipconfig /all » : ligne par ligne")
    f.rect(30, 56, 600, 390, "#1e1e1e", "#37474f", 3, 8); f.rect(30, 56, 600, 28, "#37474f", "#37474f", 0, 8)
    f.text(46, 76, "C:\\> ipconfig /all", 13, "#cfd8dc", "start", "700", family="Consolas, Menlo, monospace")
    rows = [("Adresse physique . . . . : ", "00-D0-95-12-34-56", "A"), ("DHCP activé . . . . . . . : ", "Oui", "B"), ("Adresse IPv4 . . . . . . . : ", "192.168.10.101", "C"),
            ("Masque de sous-réseau . . : ", "255.255.255.0", "D"), ("Passerelle par défaut . . : ", "192.168.10.1", "E"), ("Serveur DHCP . . . . . . . : ", "192.168.10.5", "F"),
            ("Serveurs DNS . . . . . . . : ", "192.168.100.1", "G"), ("Bail obtenu . . . . . . . : ", "lundi 18 janvier 08:12", "H")]
    for i, (k, v, l) in enumerate(rows):
        y = 118 + i * 38
        f.mono(46, y, k, 14, "#b0bec5"); f.mono(52 + len(k) * 8.4, y, v, 14, "#fff59d", "start", "700")
        f.badge(612 + 40, y - 5, l, IND, 13); f.line(560, y - 5, 640, y - 5, IND_M, 1.5, "3 3") if False else None
    notes = [("A", "Adresse MAC : l'identité de la carte"), ("B", "Oui = adresse reçue automatiquement"), ("C", "L'adresse du poste (dans la plage DHCP)"), ("D", "Définit quel est son réseau (/24)"),
             ("E", "Le routeur à qui parler pour sortir"), ("F", "Qui a distribué l'adresse"), ("G", "Qui traduit les noms en adresses"), ("H", "Durée de validité de l'adresse")]
    for i, (l, t) in enumerate(notes):
        y = 118 + i * 38
        f.text(712, y, f"{l}  {t}", 13, INK, "start", "600", maxw=270)
    f.rect(30, 455, 940, 0.1, WHITE, WHITE, 0, 0)
    f.save(out("m03-ipconfig.svg"))


if __name__ == "__main__":
    for fn in (m01_reseau, m01_baie, m01_switch_routeur, m01_securite, m02_rj45, m02_connecteur, m02_paires, m02_pose, m02_testeur, m02_chaine, m03_ip, m03_passerelle, m03_dora, m03_dns, m03_ipconfig):
        fn()
    print("ok")
