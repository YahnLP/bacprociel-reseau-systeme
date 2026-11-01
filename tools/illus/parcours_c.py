#!/usr/bin/env python3
"""Illustrations du parcours de mise à niveau – M09 à M15."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "terminale", "mise-a-niveau", "images"))
out = lambda n: os.path.join(ROOT, n)


def m09_ssid():
    f = Fig(1000, 470, "Deux SSID, deux VLAN", "Une borne Wi-Fi diffuse deux réseaux : KINE-WIFI rattaché au VLAN 10 et KINE-PATIENTS rattaché au VLAN 20, reliée au switch par un trunk.")
    f.title_bar("Une borne, deux SSID, deux VLAN")
    node(f, "ap", 500, 120, "Borne Wi-Fi", "1 câble PoE")
    f.rect(130, 200, 280, 60, IND_L, IND, 3, 12); f.text(270, 226, "SSID « KINE-WIFI »", 15, IND, "middle", "700"); f.text(270, 246, "WPA2 · VLAN 10 (cabinet)", 13, INK)
    f.rect(590, 200, 280, 60, ORA_L, ORA, 3, 12); f.text(730, 226, "SSID « KINE-PATIENTS »", 15, ORA, "middle", "700"); f.text(730, 246, "WPA2 · VLAN 20 (patients)", 13, INK)
    for x, c in ((270, IND), (730, ORA)):
        for r in (14, 24, 34): f.path(f"M{500 + (x-500)*0.16 - r},{150} A{r},{r} 0 0 1 {500 + (x-500)*0.16 + r},{150}", "none", c, 0.1)
    f.line(450, 128, 330, 198, IND, 2.5, "4 5"); f.line(550, 128, 670, 198, ORA, 2.5, "4 5")
    node(f, "laptop", 270, 330, "PC du cabinet", "réseau interne"); node(f, "phone", 730, 330, "Téléphone patient", "Internet seulement")
    f.line(270, 262, 270, 298, IND, 3, "3 7"); f.line(730, 262, 730, 298, ORA, 3, "3 7")
    f.line(500, 160, 500, 395, LINE, 6)
    f.rect(430, 395, 140, 46, TEAL_L, TEAL, 3, 8); f.text(500, 423, "Switch · port 1/9 (trunk)", 12.5, TEAL, "middle", "700")
    f.rect(480, 255, 40, 80, "#ffffff", "#ffffff", 0, 0)
    f.text(500, 290, "VLAN 10 + 20", 13, MUTED, "middle", "700")
    f.save(out("m09-ssid-vlan.svg"))


def m09_wpa():
    f = Fig(1000, 420, "Les niveaux de sécurité du Wi-Fi", "Un escalier de sécurité : ouvert, WEP, WPA2-Personnel, WPA3, WPA2 ou WPA3 Entreprise, avec un verdict pour chacun.")
    f.title_bar("La sécurité du Wi-Fi : de « à bannir » à « entreprise »")
    L = [("Ouvert", "aucun chiffrement", "à éviter", RED, RED_L), ("WEP", "cassé depuis 20 ans", "jamais", RED, RED_L), ("WPA2-Personnel", "chiffrement AES, une clé partagée (PSK)", "bon pour un petit cabinet", GRN, GRN_L),
         ("WPA3-Personnel", "plus récent, plus robuste", "si les appareils le gèrent", GRN, GRN_L), ("WPA2/3-Entreprise", "un compte par utilisateur (RADIUS)", "pour les grandes structures", IND, IND_L)]
    for i, (t, d, v, c, fl) in enumerate(L):
        y = 60 + i * 66; x = 30 + i * 30
        f.rect(x, y, 940 - i * 30, 56, fl, c, 3, 10); f.rect(x, y, 190, 56, c, c, 0, 10); f.rect(x + 170, y, 20, 56, c, c, 0, 0)
        f.text(x + 95, y + 34, t, 14.5, WHITE, "middle", "700"); f.text(x + 210, y + 25, d, 14, INK, "start", "700"); f.text(x + 210, y + 44, "Verdict : " + v, 13, c, "start", "700")
    f.text(500, 405, "Une clé WPA2 doit être longue (12 caractères et plus) et changée quand une personne quitte le cabinet.", 13.5, MUTED, "middle", "700")
    f.save(out("m09-securite-wifi.svg"))


def m09_isolement():
    f = Fig(1000, 440, "Isoler le Wi-Fi des patients", "Un patient en VLAN 20 peut accéder à Internet via la box mais le filtrage du switch bloque l'accès au réseau interne 192.168.10.0/24 : serveur, imprimante, postes.")
    f.title_bar("Ce que le patient peut faire, et ce qui est bloqué")
    node(f, "phone", 110, 220, "Patient", "VLAN 20")
    f.rect(330, 150, 160, 150, TEAL_L, TEAL, 4, 14); f.text(410, 180, "SWITCH", 15, TEAL, "middle", "700"); f.text(410, 204, "règle de filtrage", 13, INK, "middle", "700"); f.text(410, 224, "VLAN 20 → 192.168.10.0/24", 11.5, INK); f.text(410, 244, "= REFUSER", 14, RED, "middle", "700")
    f.line(150, 220, 328, 220, LINE, 3)
    f.rect(630, 80, 340, 120, GRN_L, GRN, 3, 12); node(f, "box", 700, 140, "Box"); node(f, "cloud", 880, 140, "Internet"); f.line(738, 140, 830, 140, LINE, 3)
    f.arrow(490, 190, 630, 150, GRN, 4); f.check(560, 145, True, 22)
    f.text(560, 120, "AUTORISÉ", 14, GRN, "middle", "700")
    f.rect(630, 240, 340, 160, RED_L, RED, 3, 12); f.text(800, 264, "Réseau interne 192.168.10.0/24", 13.5, RED, "middle", "700")
    node(f, "server", 700, 320, "Serveur"); node(f, "printer", 800, 320, "Imprimante"); node(f, "pc", 900, 320, "Postes")
    f.arrow(490, 260, 630, 300, RED, 4); f.check(560, 280, False, 22)
    f.text(560, 316, "BLOQUÉ", 14, RED, "middle", "700")
    f.rect(40, 395, 940, 36, YEL_L, YEL, 2, 8); f.text(500, 418, "Deux tests prouvent la sécurité : Internet OK (test positif) ET réseau interne refusé (test négatif).", 13.5, INK, "middle", "700")
    f.save(out("m09-isolement.svg"))


def m10_321():
    f = Fig(1000, 420, "La règle de sauvegarde 3-2-1", "Trois copies : l'original sur le switch, une sauvegarde sur le PC de l'administrateur, une copie hors site, sur deux supports différents.")
    f.title_bar("La règle 3-2-1 appliquée au switch du cabinet")
    items = [(150, "COPIE 1", "configuration en service", "sur le switch", "switch", TEAL), (500, "COPIE 2", "SW-KINE_2027-01-18.cfg", "sur le PC de l'administrateur", "pc", IND), (850, "COPIE 3", "même fichier", "chez l'installateur (hors site)", "cloud", ORA)]
    for x, t, a, b, k, c in items:
        f.rect(x - 140, 70, 280, 220, WHITE, c, 3.5, 14); f.rect(x - 140, 70, 280, 38, c, c, 0, 14); f.rect(x - 140, 90, 280, 18, c, c, 0, 0)
        f.text(x, 96, t, 16, WHITE, "middle", "700"); node(f, k, x, 160)
        f.text(x, 232, a, 12.5, INK, "middle", "700"); f.text(x, 254, b, 13, MUTED, "middle", maxw=250)
    f.arrow(292, 180, 358, 180, LINE, 3); f.arrow(642, 180, 708, 180, LINE, 3)
    for x, t, c in [(150, "3 copies", TEAL), (500, "2 supports différents", IND), (850, "1 copie hors site", ORA)]:
        f.rect(x - 110, 312, 220, 36, c, c, 0, 18); f.text(x, 336, t, 15, WHITE, "middle", "700")
    f.rect(40, 366, 920, 40, RED_L, RED, 2, 8); f.text(500, 391, "Une sauvegarde uniquement sur le switch disparaît avec lui : il faut une copie à l'extérieur.", 14, INK, "middle", "700")
    f.save(out("m10-regle-321.svg"))


def m10_maj():
    f = Fig(1000, 380, "Le plan de mise à jour", "Cinq étapes alignées dans le temps : lire le bulletin, sauvegarder, planifier, installer et tester, consigner, avec un retour arrière possible.")
    f.title_bar("Mettre à jour un switch : cinq étapes, un filet de sécurité")
    st = [("1", "Lire", "le bulletin,\nnoter la version", IND), ("2", "Sauvegarder", "la configuration\net l'ancienne version", TEAL), ("3", "Planifier", "hors horaires,\nprévenir le client", ORA), ("4", "Installer\net tester", "redémarrer,\nvérifier VLAN, Wi-Fi", "#8e24aa"), ("5", "Consigner", "journal et\nnouvelle sauvegarde", GRN)]
    for i, (n, t, d, c) in enumerate(st):
        x = 30 + i * 192
        f.rect(x, 70, 176, 190, WHITE, c, 3, 12); f.badge(x + 88, 70, n, c, 17)
        for j, ln in enumerate(t.split("\n")): f.text(x + 88, 120 + j * 22, ln, 17, c, "middle", "700")
        for j, ln in enumerate(d.split("\n")): f.text(x + 88, 186 + j * 20, ln, 13.5, INK)
        if i < 4: f.arrow(x + 178, 165, x + 190, 165, MUTED, 3)
    f.path("M720,262 C720,320 220,320 220,262", "none", RED, 3, "7 5", arrow=True)
    f.text(470, 340, "Si la mise à jour échoue : retour arrière (ancienne version + configuration sauvegardée)", 14, RED, "middle", "700")
    f.save(out("m10-plan-maj.svg"))


def m11_cycle():
    f = Fig(1000, 380, "Préparer avant d'intervenir", "Quatre étapes de préparation : comprendre, lister, planifier, prévoir, qui produisent reformulation, matériel, planning, risques et plan de tests.")
    f.title_bar("Avant de toucher au matériel : quatre étapes de préparation")
    st = [("1  Comprendre", "Que veut le client ?\nQuelles contraintes ?", "→ reformulation\n→ exigences", IND), ("2  Lister", "De quoi ai-je besoin ?", "→ matériel, outillage\n→ longueur de câble", TEAL), ("3  Planifier", "Dans quel ordre ?\nCombien de temps ?", "→ planning\nde tâches", ORA), ("4  Prévoir", "Qu'est-ce qui peut\nmal tourner ?", "→ risques\n→ plan de tests", "#8e24aa")]
    for i, (t, q, p, c) in enumerate(st):
        x = 30 + i * 238
        f.rect(x, 70, 224, 230, WHITE, c, 3.5, 14); f.rect(x, 70, 224, 44, c, c, 0, 14); f.rect(x, 96, 224, 18, c, c, 0, 0)
        f.text(x + 112, 100, t, 17, WHITE, "middle", "700")
        for j, ln in enumerate(q.split("\n")): f.text(x + 112, 150 + j * 20, ln, 14, INK)
        f.rect(x + 14, 206, 196, 76, c, c, 0, 10, op=0.12)
        for j, ln in enumerate(p.split("\n")): f.text(x + 112, 234 + j * 22, ln, 14, c, "middle", "700")
        if i < 3: f.arrow(x + 226, 185, x + 236, 185, MUTED, 3)
    f.rect(30, 322, 940, 40, YEL_L, YEL, 2, 8); f.text(500, 347, "Ordre logique d'une intervention : câbler → tester la liaison → brasser → configurer → tester → sauvegarder → consigner.", 13.5, INK, "middle", "700")
    f.save(out("m11-preparer.svg"))


def m11_tests():
    f = Fig(1000, 430, "Anatomie d'un bon test", "Un test précise d'où on le fait, ce qu'on fait, ce qu'on attend, et si c'est un test positif ou négatif ; deux exemples sont donnés.")
    f.title_bar("Un bon test répond à quatre questions")
    heads = [("D'où ?", IND), ("Que fait-on ?", TEAL), ("Qu'attend-on ?", ORA), ("Positif ou négatif ?", "#8e24aa")]
    xs = [30, 270, 570, 790]; ws = [236, 296, 216, 180]
    for (h, c), x, w in zip(heads, xs, ws):
        f.rect(x, 62, w, 40, c, c, 0, 8); f.text(x + w / 2, 88, h, 15, WHITE, "middle", "700")
    rows = [("PC-SOINS2", "ipconfig : l'adresse reçue\nest entre .100 et .150", "adresse 192.168.10.1xx", "positif", GRN, GRN_L), ("Portable patient", "ping 192.168.10.5\n(le serveur)", "AUCUNE réponse", "négatif", RED, RED_L)]
    for r, (a, b, c_, d, col, fl) in enumerate(rows):
        y = 112 + r * 100
        for x, w, txt in zip(xs, ws, (a, b, c_, d)):
            f.rect(x, y, w, 88, fl if x == xs[3] else WHITE, col if x == xs[3] else GRY_D, 2.5, 8)
            for j, ln in enumerate(txt.split("\n")): f.text(x + w / 2, y + 40 + j * 20 - (10 if "\n" in txt else 0), ln, 14, INK if x != xs[3] else col, "middle", "700" if x == xs[3] else "400")
    f.rect(30, 330, 940, 80, YEL_L, YEL, 2, 10)
    f.text(500, 356, "Sans « résultat attendu », on ne peut pas conclure. Sans test négatif, on ne prouve pas la sécurité.", 14, INK, "middle", "700")
    f.text(500, 380, "Chaque exigence du client doit être prouvée par au moins un test.", 13.5, MUTED)
    f.text(500, 400, "On écrit les tests AVANT d'intervenir, pour ne pas les adapter à ce qui marche.", 13.5, MUTED)
    f.save(out("m11-anatomie-test.svg"))


def m12_methode():
    f = Fig(1000, 430, "La méthode de dépannage en huit étapes", "Huit étapes enchaînées : constater, délimiter, hypothèses, tester, corriger, vérifier, prévenir, consigner.")
    f.title_bar("Dépanner : huit étapes, dans l'ordre")
    st = [("1", "Constater", "symptôme exact,\nqui est touché ?", IND), ("2", "Délimiter", "ce qui marche\nencore", IND), ("3", "Hypothèses", "causes possibles,\nordonnées", TEAL), ("4", "Tester", "un test\npar hypothèse", TEAL),
          ("5", "Corriger", "UNE seule\nmodification", ORA), ("6", "Vérifier", "la panne a-t-elle\ndisparu ?", ORA), ("7", "Prévenir", "pour que ça\nne revienne pas", GRN), ("8", "Consigner", "fiche, journal,\ncompte rendu", GRN)]
    for i, (n, t, d, c) in enumerate(st):
        x = 30 + (i % 4) * 238; y = 70 + (i // 4) * 170
        f.rect(x, y, 224, 150, WHITE, c, 3.5, 14); f.badge(x + 30, y + 30, n, c, 17); f.text(x + 125, y + 38, t, 18, c, "middle", "700")
        for j, ln in enumerate(d.split("\n")): f.text(x + 112, y + 88 + j * 22, ln, 14, INK)
        if i % 4 < 3: f.arrow(x + 226, y + 75, x + 236, y + 75, MUTED, 3)
    f.path("M940,222 C960,250 40,250 36,300", "none", GRY_D, 0.1)
    f.text(500, 418, "On s'arrête à l'étape 4 tant qu'on n'a pas de cause prouvée : on ne « corrige » pas au hasard.", 14, MUTED, "middle", "700")
    f.save(out("m12-methode.svg"))


def m12_arbre():
    f = Fig(1000, 470, "Quelle cause examiner selon le symptôme", "Un arbre de décision qui part d'un équipement injoignable et oriente vers le câble, le VLAN, l'adresse, la passerelle, le DNS ou le DHCP selon les tests.")
    f.title_bar("Le symptôme oriente la recherche de cause")
    def q(x, y, w, t, c=IND, fl=IND_L):
        f.rect(x, y, w, 50, fl, c, 3, 10); f.text(x + w / 2, y + 30, t, 13.5, INK, "middle", "700", maxw=w - 14)
    q(350, 60, 300, "Un équipement ne répond plus", IND, IND_L)
    q(30, 160, 280, "Voyant de lien éteint ?", TEAL, TEAL_L); q(360, 160, 280, "Joint dans son réseau, pas ailleurs ?", TEAL, TEAL_L); q(690, 160, 280, "Adresse en 169.254 ?", TEAL, TEAL_L)
    for x in (170, 500, 830): f.arrow(500, 112, x, 158, MUTED, 2.5)
    res = [(30, "Câble, port du switch,\ncordon débranché", ORA), (360, "Passerelle, masque,\nroute par défaut", ORA), (690, "DHCP injoignable :\nrelais, VLAN, serveur", ORA)]
    for x, t, c in res:
        f.arrow(x + 140, 212, x + 140, 258, MUTED, 2.5); f.text(x + 150, 244, "oui", 12.5, GRN, "start", "700")
        f.rect(x, 262, 280, 70, ORA_L, c, 3, 10)
        for j, ln in enumerate(t.split("\n")): f.text(x + 140, 292 + j * 20 - 6, ln, 14, INK, "middle", "700")
    f.rect(30, 352, 940, 94, YEL_L, YEL, 2, 10)
    f.text(500, 378, "Si la réponse est « non » partout : l'équipement est dans le mauvais VLAN, a une mauvaise adresse IP,", 13.5, INK)
    f.text(500, 400, "ou le DNS est en cause (adresse OK, nom injoignable).", 13.5, INK)
    f.text(500, 426, "Outils : show interfaces status · show mac-learning · show vlan port · show ip routes · show ip helper", 13, MUTED, "middle", "700")
    f.save(out("m12-arbre-pannes.svg"))


def m15_epreuve():
    f = Fig(1000, 400, "Le déroulé des 3 heures de l'épreuve", "Frise des quatre phases : préparer 40 minutes, réaliser 1 h 35, maintenance 30 minutes, restitution 15 minutes, avec les trois appels à l'examinateur.")
    f.title_bar("L'épreuve de 3 heures en un coup d'œil")
    ph = [("A · PRÉPARER", 40, IND, "dossier, matériel,\nplanning, tests"), ("B · RÉALISER", 95, TEAL, "câbler, brasser,\nconfigurer, tester"), ("C · MAINTENANCE", 30, ORA, "sauvegarde, MAJ,\ndépannage"), ("RESTIT.", 15, "#8e24aa", "compte rendu,\nentretien")]
    x = 40; W = 920 / 180
    for t, m, c, d in ph:
        w = m * W
        f.rect(x, 90, w - 3, 90, c, c, 0, 8); f.text(x + w / 2, 125, t, 14 if m > 30 else 12, WHITE, "middle", "700"); f.text(x + w / 2, 150, f"{m} min" if m != 95 else "1 h 35", 14, WHITE, "middle", "700")
        for j, ln in enumerate(d.split("\n")): f.text(x + w / 2, 212 + j * 18, ln, 12 if m < 40 else 13, INK, "middle")
        x += w
    for t, m in [("Appel 1", 40 + 40), ("Appel 2", 40 + 70), ("Appel 3", 40 + 95)]:
        px = 40 + m * W
        f.line(px, 74, px, 90, RED, 3); f.circle(px, 70, 7, RED, WHITE, 2)
    f.text(40 + 80 * W, 58, "Appel n°1", 12.5, RED, "middle", "700"); f.text(40 + 110 * W, 58, "Appel n°2", 12.5, RED, "middle", "700"); f.text(40 + 135 * W, 58, "Appel n°3", 12.5, RED, "middle", "700")
    for i, (t, d) in enumerate([("Appel 1", "raccordement\net mesure"), ("Appel 2", "configuration\ndu switch"), ("Appel 3", "tests négatifs\ndémontrés")]):
        xx = 80 + i * 300
        f.rect(xx, 290, 260, 84, RED_L, RED, 2.5, 10); f.text(xx + 130, 316, t, 15, RED, "middle", "700")
        for j, ln in enumerate(d.split("\n")): f.text(xx + 130, 340 + j * 18, ln, 13.5, INK)
    f.text(500, 270, "Trois points d'arrêt avec l'examinateur", 14, MUTED, "middle", "700")
    f.save(out("m15-deroule-epreuve.svg"))


if __name__ == "__main__":
    for fn in (m09_ssid, m09_wpa, m09_isolement, m10_321, m10_maj, m11_cycle, m11_tests, m12_methode, m12_arbre, m15_epreuve):
        fn()
    print("ok")
