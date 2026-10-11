#!/usr/bin/env python3
"""Illustrations Terminale – S01 à S04."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "terminale"))
out = lambda s, n: os.path.join(ROOT, s, "images", n)


def s01():
    d = "S01-diagnostic-retour"
    f = Fig(1000, 400, "Un chantier en six étapes", "Du dossier à la recette : étudier, préparer, installer, configurer, tester et dépanner, rendre compte. Chaque étape laisse une trace écrite.")
    f.title_bar("Un chantier = six étapes, six traces écrites")
    et = [("1", "Étudier", "dossier, plans,", "cahier des charges", "C06", IND_L, IND), ("2", "Préparer", "matériel, outillage,", "sécurité, planning", "C06", IND_L, IND),
          ("3", "Installer", "câbles, baie,", "équipements", "C09", TEAL_L, TEAL), ("4", "Configurer", "VLAN, routage,", "services, Wi-Fi", "C09", TEAL_L, TEAL),
          ("5", "Tester", "recette, dépannage,", "sauvegardes", "C10", ORA_L, ORA), ("6", "Rendre compte", "compte rendu,", "dossier, client", "C10", ORA_L, ORA)]
    for i, (n, t, a, b, c, fill, st) in enumerate(et):
        x = 30 + i * 158
        f.rect(x, 80, 146, 180, fill, st, 3, 14)
        f.badge(x + 73, 108, n, st, 17)
        f.text(x + 73, 150, t, 17, INK, "middle", "700"); f.text(x + 73, 180, a, 13, INK); f.text(x + 73, 200, b, 13, INK)
        f.rect(x + 43, 222, 60, 26, st, st, 0, 13); f.text(x + 73, 240, c, 14, WHITE, "middle", "700")
        if i < 5:
            f.arrow(x + 148, 170, x + 158, 170, MUTED, 3)
    f.text(500, 310, "À l'épreuve E31, tu es évalué sur ces trois compétences : C06 (préparer), C09 (installer, configurer), C10 (tester, dépanner).", 14, MUTED)
    f.text(500, 335, "La grille nationale regarde ce que tu fais, ce que tu écris et comment tu le justifies.", 14, MUTED)
    f.save(out(d, "chantier-6-etapes.svg"))


def s02():
    d = "S02-dossier-installation"
    f = Fig(1000, 520, "Plan du local du cabinet Dubois", "Plan simplifié du cabinet : cinq pièces, huit prises RJ45 repérées P1 à P8 et un local technique. À comparer au cahier des charges.")
    f.title_bar("Plan du local – cabinet Dubois (échelle : 1 carreau = 1 m)")
    # contour
    X0, Y0 = 40, 60
    rooms = [("Accueil", 40, 60, 220, 200), ("Bureau 1", 260, 60, 300, 200), ("Bureau 2", 560, 60, 240, 200), ("Salle de réunion", 800, 60, 160, 200),
             ("Local technique", 700, 260, 260, 160), ("Cuisine", 40, 330, 250, 90), ("Sanitaires", 290, 330, 410, 90)]
    for n, x, y, w, h in rooms:
        fill = IND_L if n != "Local technique" else ORA_L
        f.rect(x, y, w, h, fill, LINE, 3, 0)
        f.text(x + 12, y + 26, n, 15, INK, "start", "700")
    f.rect(40, 260, 660, 70, GRY, LINE, 2, 0); f.text(370, 300, "Couloir", 14, MUTED, "middle", "700")
    # prises : (id, x, y)
    prises = [("P1", 70, 230), ("P2", 220, 230), ("P3", 290, 230), ("P4", 420, 230), ("P5", 530, 230), ("P6", 590, 230), ("P7", 700, 230), ("P8", 830, 230)]
    for pid, x, y in prises:
        f.rect(x - 14, y - 13, 28, 26, TEAL, WHITE, 2, 5); f.text(x, y + 5, pid[1:], 13, WHITE, "middle", "700")
    f.rect(720, 290, 100, 110, ORA, WHITE, 2, 6); f.text(770, 340, "Baie", 15, WHITE, "middle", "700"); f.text(770, 360, "24 U", 12, WHITE)
    f.text(870, 345, "Arrivée", 13, INK); f.text(870, 363, "opérateur", 13, INK)
    # légende
    f.rect(40, 440, 920, 60, YEL_L, YEL, 2, 10)
    f.rect(56, 458, 28, 24, TEAL, WHITE, 2, 5); f.text(98, 476, "= prise RJ45 murale (n° de prise)", 14, INK, "start")
    f.rect(430, 456, 28, 28, ORA, WHITE, 2, 5); f.text(472, 476, "= baie de brassage", 14, INK, "start")
    f.text(660, 476, "Hauteur sous plafond : 2,60 m", 14, MUTED, "start")
    f.save(out(d, "plan-local.svg"))


def s02b():
    d = "S02-dossier-installation"
    f = Fig(1000, 470, "Schéma d'architecture du cabinet Dubois", "Schéma fourni dans le dossier : la box est reliée à un switch 8 ports, qui dessert l'accueil, les bureaux, la salle de réunion avec sa borne Wi-Fi et un NAS dans la baie.")
    f.title_bar("Schéma d'architecture fourni dans le dossier (version 1)")
    node(f, "cloud", 90, 110, "Internet")
    node(f, "box", 280, 110, "Box FAI", "192.168.10.1")
    node(f, "switch", 520, 110, "SW1 – switch 8 ports", "non administrable")
    f.line(150, 110, 235, 110, LINE, 3); f.line(325, 110, 465, 110, LINE, 3)
    groups = [("Accueil", "2 postes", "1 imprimante réseau", 90), ("Bureau 1", "4 postes", "", 270), ("Bureau 2", "3 postes", "", 450), ("Salle de réunion", "1 borne Wi-Fi", "SSID invités", 630), ("Baie", "NAS", "192.168.10.10", 810)]
    for t, a, b, x in groups:
        f.rect(x - 78, 300, 156, 100, IND_L, IND, 2.5, 10)
        f.text(x, 328, t, 15, INK, "middle", "700"); f.text(x, 355, a, 14, INK); f.text(x, 377, b, 13, MUTED)
        f.line(520, 172, x, 300, LINE, 2.5)
    f.rect(700, 70, 270, 90, YEL_L, YEL, 2.5, 10)
    f.text(715, 96, "Plan d'adressage (extrait)", 14, "#8a6d00", "start", "700")
    f.text(715, 120, "Postes et imprimante : 192.168.10.0/24", 13, INK, "start")
    f.text(715, 142, "DHCP : 192.168.10.10 à 192.168.10.60", 13, INK, "start")
    f.save(out(d, "schema-architecture.svg"))


def s03():
    d = "S03-preparer-chantier"
    f = Fig(1000, 470, "Les six risques d'un chantier réseau", "Six cartes : électrique, hauteur, laser de la fibre optique, électricité statique, manutention et amiante ; pour chacune, le réflexe à avoir.")
    f.title_bar("Six risques, six réflexes")
    cards = [("Électrique", "Je ne travaille pas", "sous tension. Je coupe,", "je vérifie, je signale.", RED_L, RED),
             ("Hauteur", "Escabeau en bon état,", "3 points d'appui,", "jamais seul sur un faux-plafond.", ORA_L, ORA),
             ("Laser fibre", "Invisible mais dangereux :", "je ne regarde jamais", "un bout de fibre.", YEL_L, "#b28704"),
             ("Statique (ESD)", "Bracelet antistatique,", "composants tenus", "par les bords.", IND_L, IND),
             ("Manutention", "Charge lourde : je plie", "les genoux, je demande", "de l'aide (UPS, baie).", TEAL_L, TEAL),
             ("Amiante", "Bâtiment ancien : pas de", "perçage sans diagnostic", "ni accord du client.", GRY, GRY_D)]
    for i, (t, a, b, c, fill, st) in enumerate(cards):
        x = 30 + (i % 3) * 320; y = 75 + (i // 3) * 190
        f.rect(x, y, 300, 170, fill, st, 3, 14)
        f.text(x + 150, y + 38, t, 20, st if st != GRY_D else INK, "middle", "700")
        for k, l in enumerate((a, b, c)):
            f.text(x + 150, y + 82 + k * 26, l, 14.5, INK)
    f.save(out(d, "six-risques.svg"))


def s05():
    d = "S05-inter-vlan"
    f = Fig(1000, 480, "Le routeur sur un tronc : un seul câble, deux VLAN", "Le poste de la compta (VLAN 10) joint le serveur (VLAN 30). La trame monte vers le routeur étiquetée VLAN 10, le routeur la route et la renvoie sur le même câble étiquetée VLAN 30.")
    f.title_bar("Un seul câble entre le switch et le routeur : le trunk")
    node(f, "router", 500, 110, "R1", "Gi0/0.10  192.168.10.1  /  Gi0/0.30  192.168.30.1")
    node(f, "switch", 500, 330, "SW1", "VLAN 10 et VLAN 30")
    node(f, "pc", 130, 330, "PC-CPT", "VLAN 10 – 192.168.10.11")
    node(f, "server", 870, 330, "SRV", "VLAN 30 – 192.168.30.10")
    f.rect(470, 175, 60, 120, GRY, GRY_D, 2, 8); f.text(500, 168, "trunk 802.1Q", 13, MUTED, "middle", "700")
    f.arrow(485, 285, 485, 190, IND, 4); f.arrow(515, 190, 515, 285, GRN, 4)
    f.text(455, 240, "②", 20, IND, "end", "700"); f.text(545, 240, "③", 20, GRN, "start", "700")
    f.text(440, 205, "trame étiquetée", 13, IND, "end", "700"); f.text(440, 222, "VLAN 10", 13, IND, "end", "700")
    f.text(560, 205, "trame étiquetée", 13, GRN, "start", "700"); f.text(560, 222, "VLAN 30", 13, GRN, "start", "700")
    f.arrow(190, 345, 440, 345, IND, 4); f.text(315, 332, "① envoi (sans étiquette)", 13, IND)
    f.arrow(560, 345, 810, 345, GRN, 4); f.text(685, 332, "④ arrivée", 13, GRN)
    f.rect(40, 410, 920, 55, YEL_L, YEL, 2.5, 10)
    f.text(60, 434, "Le routeur reçoit sur Gi0/0.10 (sous-interface du VLAN 10), décide, et renvoie par Gi0/0.30 : un seul port physique.", 14, INK, "start")
    f.text(60, 454, "Si le trunk tombe, ou si un VLAN n'est pas autorisé dessus, plus aucune communication entre VLAN.", 14, INK, "start")
    f.save(out(d, "routeur-sur-un-tronc.svg"))


def s04():
    d = "S04-installer-mesurer"
    f = Fig(1000, 380, "Le canal de transmission en cuivre", "Un canal complet va du poste au switch : cordon de brassage côté poste, liaison permanente jusqu'au panneau, cordon de brassage côté switch. Limite : 100 m au total dont 90 m de liaison permanente.")
    f.title_bar("Canal = cordons + liaison permanente (100 m maximum)")
    xs = [75, 320, 680, 925]
    labels = [("Poste", IND), ("Prise", TEAL), ("Panneau", TEAL), ("Switch", ORA)]
    for x, (t, c) in zip(xs, labels):
        f.rect(x - 55, 110, 110, 70, WHITE, c, 3, 10); f.text(x, 150, t, 15, c, "middle", "700")
    f.line(xs[0] + 55, 145, xs[1] - 55, 145, LINE, 4); f.text((xs[0] + xs[1]) / 2, 128, "cordon ≤ 5 m", 13, INK)
    f.line(xs[1] + 55, 145, xs[2] - 55, 145, TEAL, 6); f.text((xs[1] + xs[2]) / 2, 168, "liaison permanente ≤ 90 m", 14, TEAL, "middle", "700")
    f.line(xs[2] + 55, 145, xs[3] - 55, 145, LINE, 4); f.text((xs[2] + xs[3]) / 2, 128, "cordon ≤ 5 m", 13, INK)
    f.rect(320, 215, 360, 12, TEAL, TEAL, 0, 6)
    f.text(500, 250, "Liaison permanente : on la certifie (cartographie, longueur, atténuation, diaphonie)", 14, INK)
    f.rect(75, 215, 245, 12, IND_M, IND_M, 0, 6); f.rect(680, 215, 245, 12, IND_M, IND_M, 0, 6)
    f.rect(40, 285, 920, 70, YEL_L, YEL, 2.5, 12)
    f.text(60, 313, "À retenir", 15, "#8a6d00", "start", "700")
    f.text(60, 337, "Les cordons de brassage s'achètent ; la liaison permanente se pose et se mesure. Un défaut vient souvent du cordon, pas du câble posé.", 14, INK, "start")
    f.save(out(d, "canal.svg"))

    f = Fig(1000, 500, "Face avant d'une baie de brassage", "De haut en bas : panneau de brassage 24 ports, passe-câbles, switch, passe-câbles, routeur, serveur. Des cordons courts relient le panneau au switch.")
    f.title_bar("Une baie bien rangée : de haut en bas")
    bx, bw = 250, 500
    f.rect(bx - 20, 70, bw + 40, 410, GRY, GRY_D, 3, 8)
    # panneau
    f.rect(bx, 85, bw, 56, WHITE, TEAL, 3, 4); f.text(bx + 10, 105, "Panneau de brassage 24 ports (étiquettes A01 à A24)", 13, TEAL, "start", "700")
    for i in range(12):
        x = bx + 22 + i * 38
        f.rect(x, 114, 26, 18, TEAL_L, TEAL, 1.5, 3)
    # passe-câbles
    f.rect(bx, 148, bw, 22, YEL_L, YEL, 2, 4); f.text(bx + bw / 2, 164, "passe-câbles", 12, MUTED)
    # switch
    f.rect(bx, 178, bw, 56, WHITE, IND, 3, 4); f.text(bx + 10, 198, "Switch 24 ports PoE (Fa0/1 à Fa0/24)", 13, IND, "start", "700")
    for i in range(12):
        x = bx + 22 + i * 38
        f.rect(x, 207, 26, 18, IND_L, IND, 1.5, 3)
    # cordons (entre passe-câbles): trois traits
    for k, (i, col) in enumerate([(0, ORA), (1, RED), (2, GRN)]):
        x = bx + 35 + (i + 8) * 38
        f.line(x, 132, x, 150, col, 3); f.line(x, 170, x, 207, col, 3)
    f.rect(bx, 242, bw, 22, YEL_L, YEL, 2, 4); f.text(bx + bw / 2, 258, "passe-câbles", 12, MUTED)
    f.rect(bx, 272, bw, 56, WHITE, ORA, 3, 4); f.text(bx + 10, 292, "Routeur", 13, ORA, "start", "700")
    f.rect(bx, 336, bw, 66, WHITE, IND, 3, 4); f.text(bx + 10, 356, "Serveur 1U", 13, IND, "start", "700")
    f.rect(bx, 410, bw, 56, WHITE, GRN, 3, 4); f.text(bx + 10, 430, "Onduleur (en bas : il est lourd)", 13, GRN, "start", "700")
    f.rect(780, 90, 200, 110, YEL_L, YEL, 2, 10)
    for k, t in enumerate(("Cordons de brassage :", "A09 → Fa0/9", "A10 → Fa0/10", "A11 → Fa0/11")):
        f.text(795, 115 + k * 22, t, 13, INK, "start", "700" if k == 0 else "400")
    f.rect(20, 90, 200, 110, YEL_L, YEL, 2, 10)
    for k, t in enumerate(("Étiquettes :", "le même repère aux", "deux bouts du câble", "(A09 ↔ prise 9)")):
        f.text(35, 115 + k * 22, t, 13, INK, "start", "700" if k == 0 else "400")
    f.save(out(d, "baie.svg"))


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s01", "s02", "s02b", "s03", "s04", "s05"]):
        globals()[w](); print("OK", w)
