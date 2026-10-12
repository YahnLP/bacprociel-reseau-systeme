#!/usr/bin/env python3
"""Illustrations Seconde – S08 (réseau), S09 (câble RJ45), S10 (raccordement)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "seconde"))
out = lambda s, n: os.path.join(ROOT, s, "images", n)

WIRE = {"bo": ("#ffffff", "#f57c00"), "o": ("#f57c00", None), "bv": ("#ffffff", "#2e7d32"), "b": ("#1e88e5", None),
        "bb": ("#ffffff", "#1e88e5"), "v": ("#2e7d32", None), "bm": ("#ffffff", "#6d4c41"), "m": ("#6d4c41", None)}
T568B = ["bo", "o", "bv", "b", "bb", "v", "bm", "m"]
NAMES = {"bo": "blanc-orange", "o": "orange", "bv": "blanc-vert", "b": "bleu", "bb": "blanc-bleu", "v": "vert", "bm": "blanc-marron", "m": "marron"}


def wire_v(f, x, y1, y2, code, w=16):
    """fil vertical (rayé si « blanc-… »)"""
    base, stripe = WIRE[code]
    f.rect(x - w / 2, y1, w, y2 - y1, base, "#455a64", 1.5, 3)
    if stripe:
        n = int((y2 - y1) / 10)
        for i in range(n):
            if i % 2 == 0:
                f.rect(x - w / 2 + 1, y1 + i * 10 + 1, w - 2, 5, stripe, stripe, 0, 1)


def s08():
    d = "S08-quest-ce-qu-un-reseau"
    f = Fig(980, 330, "Du mur jusqu'à Internet", "Prise murale, câble dans le mur, panneau de brassage, cordon, switch, routeur ou box, Internet.")
    f.title_bar("Le trajet d'une donnée dans le bâtiment")
    y = 150
    steps = [(80, "1", "Prise murale", "RJ45 dans la salle"), (240, "2", "Câble dans le mur", "ou goulotte"), (400, "3", "Panneau de brassage", "dans la baie"),
             (560, "4", "Switch", "distribue"), (720, "5", "Box / routeur", "sort du bâtiment"), (880, "6", "Internet", "le reste du monde")]
    for i, (x, n, t, b) in enumerate(steps):
        if i == 0:
            f.rect(x - 28, y - 22, 56, 44, GRY, LINE, 3, 6); p = x; f.rect(x - 14, y - 12, 28, 24, WHITE, IND, 2.5, 2)
        elif i == 1:
            f.path(f"M{x-45},{y} q 22,-30 45,0 t 45,0", "none", GRY_D, 6)
        elif i == 2:
            f.rect(x - 55, y - 20, 110, 40, GRY, LINE, 3, 4)
            for k in range(8): f.rect(x - 48 + k * 12, y - 8, 9, 16, WHITE, LINE, 1.5, 1)
        elif i == 3:
            ic_switch(f, x, y)
        elif i == 4:
            ic_router(f, x, y)
        else:
            ic_cloud(f, x, y)
        f.badge(x, y - 50, n, IND)
        f.text(x, y + 60, t, 14.5, INK, "middle", "700"); f.text(x, y + 78, b, 12.5, MUTED)
        if i < 5:
            f.arrow(x + 62, y, steps[i + 1][0] - 62, y, LINE, 3)
    f.callout(70, 255, 840, "Chaque étape est un point où une panne peut se cacher. Un bon technicien sait suivre le trajet, étape par étape.", YEL_L, YEL, 15)
    f.save(out(d, "chemin-physique.svg"))


    f = Fig(980, 330, "Les quatre topologies", "Bus, anneau, étoile et maillé : quatre façons de relier des machines. L'étoile est celle utilisée aujourd'hui.")
    f.title_bar("Quatre façons de relier les machines")
    cols = [(130, "Bus", "un seul câble partagé", GRY_D), (370, "Anneau", "chacun relié à deux voisins", GRY_D), (610, "Étoile", "tout passe par le centre", TEAL), (850, "Maillé", "tout le monde relié à tout le monde", GRY_D)]
    import math
    for (cx, name, sub, col) in cols:
        f.rect(cx - 112, 58, 224, 236, TEAL_L if col == TEAL else GRY, col, 3 if col == TEAL else 2, 12)
        f.text(cx, 84, name, 17, TEAL if col == TEAL else INK, "middle", "700")
        f.text(cx, 278, sub, 12.5, MUTED)
    pts = lambda cx, cy, r, n, a0=-90: [(cx + r * math.cos(math.radians(a0 + i * 360 / n)), cy + r * math.sin(math.radians(a0 + i * 360 / n))) for i in range(n)]
    # bus
    f.line(40, 190, 220, 190, LINE, 5)
    for x in (62, 112, 162, 205):
        f.line(x, 190, x, 150 if x in (62, 162) else 230, LINE, 3)
        f.circle(x, 138 if x in (62, 162) else 242, 12, IND_L, IND, 2.5)
    # anneau
    P = pts(370, 180, 62, 5)
    for i in range(5): f.line(*P[i], *P[(i + 1) % 5], LINE, 3)
    for (x, y) in P: f.circle(x, y, 12, IND_L, IND, 2.5)
    # étoile
    P = pts(610, 180, 68, 5)
    for (x, y) in P: f.line(610, 180, x, y, LINE, 3)
    for (x, y) in P: f.circle(x, y, 12, IND_L, IND, 2.5)
    f.rect(590, 168, 40, 24, TEAL, TEAL, 2, 5); f.text(610, 185, "SW", 12.5, WHITE, "middle", "700")
    # maillé
    P = pts(850, 180, 66, 5)
    for i in range(5):
        for j in range(i + 1, 5): f.line(*P[i], *P[j], GRY_D, 2)
    for (x, y) in P: f.circle(x, y, 12, IND_L, IND, 2.5)
    f.save(out(d, "topologies.svg"))

    f = Fig(940, 400, "LAN, WAN, Internet", "Un réseau local (LAN) avec postes, imprimante et switch relié par une box à Internet (WAN).")
    f.title_bar("LAN, WAN et Internet : qui est où ?")
    f.rect(30, 55, 580, 330, IND_L, IND, 3, 16, dash="8 6")
    f.text(60, 82, "LAN : mon réseau local (la salle, la maison)", 15, IND, "start", "700")
    f.halo = IND_L
    for (x, y) in [(100, 140), (100, 310), (290, 160), (290, 290)]:
        f.line(290, 220, x, y, LINE, 3)
    f.line(290, 220, 520, 220, LINE, 3)
    node(f, "switch", 290, 220, "Switch")
    node(f, "pc", 100, 140, "Client", "PC-01"); node(f, "laptop", 100, 310, "Client", "PC-02")
    node(f, "server", 290, 125, "Serveur", "partage"); node(f, "printer", 290, 320, "Imprimante")
    node(f, "box", 520, 220, "Box")
    f.halo = None
    f.line(558, 220, 760, 220, ORA, 5); f.text(660, 205, "WAN", 14, ORA, "middle", "700")
    node(f, "cloud", 830, 220, "Internet")
    f.text(830, 300, "WAN : le réseau\nétendu (opérateur)", 14, ORA, "middle", "700")
    f.save(out(d, "lan-wan.svg"))

    f = Fig(900, 330, "Symboles pour les schémas", "Légende : PC, portable, serveur, imprimante, switch, box/routeur, borne Wi-Fi, Internet, trait pour câble, pointillé pour Wi-Fi.")
    f.title_bar("Ma légende pour dessiner un schéma réseau")
    L = [("pc", "PC fixe"), ("laptop", "Portable"), ("server", "Serveur"), ("printer", "Imprimante"), ("switch", "Switch"), ("box", "Box / routeur"), ("ap", "Borne Wi-Fi"), ("cloud", "Internet")]
    for i, (k, t) in enumerate(L):
        x = 80 + (i % 4) * 215; y = 100 + (i // 4) * 105
        ICONS[k](f, x, y, t)
    f.line(60, 295, 200, 295, LINE, 3); f.text(215, 300, "câble Ethernet", 14, INK, "start")
    f.line(400, 295, 540, 295, TEAL, 3, "3 7"); f.text(555, 300, "liaison Wi-Fi", 14, INK, "start")
    f.save(out(d, "symboles.svg"))


def s09():
    d = "S09-cable-rj45"
    f = Fig(900, 360, "Le câble RJ45 en coupe", "Quatre paires torsadées : orange, verte, bleue, marron, dans une gaine.")
    f.title_bar("Dans la gaine : 4 paires torsadées")
    f.rect(40, 150, 100, 70, "#cfd8dc", "#455a64", 3, 30); f.text(90, 245, "la gaine\n(l'enveloppe)", 13, MUTED, "middle", "700")
    import math
    for i, (c1, c2, y0) in enumerate([("bo", "o", 60), ("bv", "v", 120), ("b", "bb", 180), ("bm", "m", 240)]):
        pass
    pairs = [("bo", "o", 85), ("bv", "v", 145), ("bb", "b", 205), ("bm", "m", 265)]
    for (a, b, y) in pairs:
        # fils torsadés (ondes opposées)
        for sgn, code in ((1, a), (-1, b)):
            base, stripe = WIRE[code]
            pts = []
            for k in range(0, 41):
                x = 150 + k * 10
                pts.append((x, y + sgn * 9 * math.sin(k * 0.8)))
            d_ = "M" + " L".join(f"{px:.1f},{py:.1f}" for px, py in pts)
            f.path(d_, "none", "#455a64", 9)
            f.path(d_, "none", base, 6.5)
            if stripe:
                f.path(d_, "none", stripe, 3, dash="6 8")
    f.text(595, 60, "", 1)
    f.callout(570, 70, 310, "Pourquoi torsader ? Les perturbations (moteurs, néons, câbles voisins) agissent des deux côtés de la paire : elles s'annulent. Plus de torsades = moins de parasites.", YEL_L, YEL, 14.5)
    f.callout(570, 205, 310, "4 paires = 8 fils : orange, verte, bleue, marron. Chaque paire = un fil de couleur + un fil blanc rayé de cette couleur.", IND_L, IND, 14.5)
    f.save(out(d, "paires.svg"))

    f = Fig(900, 440, "Norme T568B", "Connecteur RJ45 vu de face, broches 1 à 8 et couleurs de la norme T568B.")
    f.title_bar("Norme T568B : l'ordre des fils (broches 1 à 8)")
    f.rect(60, 70, 420, 150, "#eceff1", "#455a64", 3, 10)
    f.text(270, 92, "RJ45 vu de face, clip vers le bas", 13, MUTED, "middle", "600")
    for i, code in enumerate(T568B):
        x = 100 + i * 46
        wire_v(f, x, 110, 205, code, 28)
        f.badge(x, 232, str(i + 1), IND, 13)
    f.text(100, 262, "broche 1", 12, MUTED, "middle"); f.text(422, 262, "broche 8", 12, MUTED, "middle")
    for i, code in enumerate(T568B):
        y = 85 + i * 33
        wire_v(f, 535, y - 10, y + 10, code, 22) if False else None
        f.rect(520, y - 11, 34, 22, WIRE[code][0], "#455a64", 1.5, 3)
        if WIRE[code][1]:
            for k in range(4): f.rect(522 + k * 8, y - 9, 4, 18, WIRE[code][1], WIRE[code][1], 0, 1)
        f.text(565, y + 5, f"{i+1}  {NAMES[code]}", 14.5, INK, "start", "600")
    f.callout(60, 365, 780, "Câble droit = T568B aux DEUX extrémités. Astuce : la paire verte est « écartée » (3 et 6) ; la paire bleue reste au milieu (4 et 5).", GRN_L, GRN, 15)
    f.save(out(d, "t568b.svg"))

    f = Fig(940, 300, "Sertir un RJ45 en 6 gestes", "Dénuder, démêler, ordonner et aplatir, couper droit, insérer, sertir.")
    f.title_bar("Sertir un connecteur RJ45 : 6 gestes")
    S = [("1", "Dénuder", "enlever ~3 cm\nde gaine\n(sans entailler\nles fils)"), ("2", "Démêler", "séparer les\n4 paires, les\ndétordre"), ("3", "Ordonner", "mettre dans l'ordre\nT568B, bien\naplatis, côte à côte"),
         ("4", "Couper", "couper droit, il\nreste ~1,2 cm\nde fils"), ("5", "Insérer", "pousser jusqu'au\nfond : on voit le\ncuivre au bout"), ("6", "Sertir", "serrer la pince\nà fond (clic)\npuis tester")]
    for i, (n, t, b) in enumerate(S):
        x = 12 + i * 155
        f.rect(x, 60, 145, 150, IND_L, IND, 3, 12); f.badge(x + 72, 60, n, IND, 15)
        f.text(x + 72, 100, t, 17, IND, "middle", "700"); f.text(x + 72, 135, b, 13, INK)
    f.callout(12, 228, 915, "Sécurité : on coupe loin du corps, on garde les doigts hors de la lame, on jette les chutes dans la poubelle.", RED_L, RED, 14.5)
    f.save(out(d, "sertissage.svg"))

    f = Fig(900, 310, "Catégories de câbles", "Cat5e, Cat6 et Cat6A : débit, fréquence, distance maximale de 100 mètres.")
    f.title_bar("Catégories : de quoi parle-t-on ?")
    hdr = ["Catégorie", "Débit usuel", "Fréquence", "Longueur max."]
    rows = [("Cat 5e", "1 Gb/s", "100 MHz", "100 m"), ("Cat 6", "1 Gb/s (10 Gb/s ≤ 55 m)", "250 MHz", "100 m"), ("Cat 6A", "10 Gb/s", "500 MHz", "100 m")]
    xs = [40, 220, 520, 700]
    f.rect(30, 55, 840, 36, IND, IND, 2, 4)
    for x, h in zip(xs, hdr): f.text(x, 79, h, 15, WHITE, "start", "700")
    for i, r in enumerate(rows):
        y = 91 + i * 42
        f.rect(30, y, 840, 42, IND_L if i % 2 == 0 else WHITE, GRY_D, 1, 0)
        for x, c in zip(xs, r): f.text(x, y + 27, c, 15, INK, "start", "700" if x == xs[0] else "400")
    f.callout(30, 235, 840, "Longueur maximale d'une liaison Ethernet sur cuivre : 100 m (90 m de câble dans le mur + 10 m de cordons). Au-delà : un switch ou de la fibre.", YEL_L, YEL, 14.5)
    f.save(out(d, "categories.svg"))

    f = Fig(900, 340, "Résultats d'un testeur de câble", "Le testeur allume les voyants 1 à 8 en séquence : câble correct, coupure, inversion, court-circuit.")
    f.title_bar("Lire les voyants du testeur")
    cases = [("Câble OK", "1 2 3 4 5 6 7 8 s'allument\ndans l'ordre aux deux bouts", GRN, "12345678"), ("Coupure", "un voyant ne s'allume pas\n(ex. : le 4)", RED, "123 5678"), ("Inversion", "les voyants s'allument\ndans le désordre (ex. : 1 3 2 4…)", ORA, "13245678"), ("Court-circuit", "deux voyants s'allument\nen même temps", RED, "12 34 5678")]
    for i, (t, b, c, seq) in enumerate(cases):
        x = 15 + i * 222
        f.rect(x, 60, 210, 260, WHITE, c, 3, 12); f.text(x + 105, 92, t, 18, c, "middle", "700")
        for k in range(8):
            on = True
            if t == "Coupure" and k == 3: on = False
            col = c if on else GRY_D
            f.circle(x + 25 + k * 23, 125, 9, col if on else WHITE, col, 2)
            f.text(x + 25 + k * 23, 129, str(k + 1), 10, WHITE if on else MUTED, "middle", "700")
        f.text(x + 105, 175, b, 13.5, INK, maxw=190)
        f.text(x + 105, 285, ("→ on sertit à nouveau" if t != "Câble OK" else "→ on peut l'utiliser"), 14, c, "middle", "700")
    f.save(out(d, "testeur.svg"))


def s10():
    d = "S10-raccorder-brasser"
    f = Fig(900, 360, "Une baie de brassage", "Panneau de brassage au-dessus d'un switch, relié par des cordons courts ; prises murales numérotées.")
    f.title_bar("Brasser : relier une prise à un port du switch")
    f.rect(40, 55, 460, 285, "#37474f", "#263238", 3, 8)
    f.text(60, 80, "Baie 19\" (vue de face)", 13, "#cfd8dc", "start", "600")
    f.rect(60, 95, 420, 54, "#eceff1", "#455a64", 2, 3)
    for k in range(12):
        f.rect(72 + k * 33, 118, 24, 22, WHITE, "#455a64", 1.5, 2); f.text(84 + k * 33, 112, str(k + 1), 10, INK, "middle", "700")
    f.text(70, 135, "", 1)
    f.rect(60, 250, 420, 62, TEAL_L, TEAL, 2, 3)
    for k in range(12):
        f.rect(72 + k * 33, 275, 24, 22, WHITE, TEAL, 1.5, 2); f.text(84 + k * 33, 307, str(k + 1), 10, INK, "middle", "700")
    # cordons
    for (a, b, col) in [(2, 3, "#e53935"), (5, 6, "#1e88e5"), (8, 9, "#43a047")]:
        xa = 84 + (a - 1) * 33; xb = 84 + (b - 1) * 33
        f.path(f"M{xa},140 C{xa},190 {xb},200 {xb},275", "none", col, 4)
    f.text(470, 205, "cordons de brassage", 12.5, "#cfd8dc", "end", "600")
    f.text(470, 240, "switch", 12.5, "#cfd8dc", "end", "600")
    f.text(470, 80, "panneau de brassage", 12.5, "#cfd8dc", "end", "600")
    f.callout(530, 70, 340, "Panneau de brassage : l'arrière reçoit les câbles des prises murales ; l'avant offre des ports RJ45 propres et numérotés.", IND_L, IND, 14.5)
    f.callout(530, 170, 340, "Un cordon relie le port du panneau au port du switch. Changer de port = changer de cordon, sans toucher au câble du mur.", GRN_L, GRN, 14.5)
    f.callout(530, 265, 340, "Étiqueter : « P12 » sur la prise murale = « 12 » sur le panneau. Sans étiquette, c'est la panne assurée.", YEL_L, YEL, 14.5)
    f.save(out(d, "baie.svg"))

    f = Fig(900, 300, "Voyants d'un port réseau", "Voyant fixe : lien établi ; clignotant : activité ; éteint : pas de lien. La couleur indique souvent la vitesse.")
    f.title_bar("Lire les voyants d'un port")
    S = [("Éteint", GRY, GRY_D, "Pas de lien", "câble absent / défectueux, équipement éteint"), ("Fixe", GRN, GRN, "Lien établi", "câble OK, les deux bouts se voient"), ("Clignote", YEL, YEL, "Activité", "des données circulent"), ("Couleur différente", ORA_L, ORA, "Vitesse", "ex. vert : 1000 Mb/s, orange : 100 Mb/s (selon le modèle)")]
    for i, (t, fi, c, a, b) in enumerate(S):
        x = 15 + i * 222
        f.rect(x, 60, 210, 215, WHITE, c, 3, 12); f.circle(x + 105, 105, 18, fi, c, 3)
        f.text(x + 105, 150, t, 17, c if c != GRY_D else INK, "middle", "700"); f.text(x + 105, 175, a, 15, INK, "middle", "600"); f.text(x + 105, 205, b, 13, MUTED, maxw=190)
    f.save(out(d, "voyants.svg"))

    f = Fig(900, 300, "Deux PC reliés à un switch : se voient-ils ?", "Deux PC reliés à un switch non administrable, sans adresse IP configurée.")
    f.title_bar("Branchés… mais se voient-ils ?")
    cable(f, 450, 120, 235, 195); cable(f, 450, 120, 665, 195)
    f.halo = WHITE
    node(f, "switch", 450, 100, "Switch", "non administrable")
    f.halo = None
    node(f, "pc", 220, 205, "PC-1"); node(f, "pc", 680, 205, "PC-2")
    f.text(450, 285, "Les voyants sont verts : le « lien » est là. Mais « lien » ne veut pas dire « conversation ».", 14.5, ORA, "middle", "700")
    f.save(out(d, "se-voient-ils.svg"))


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s08", "s09", "s10"]):
        globals()[w](); print("OK", w)
