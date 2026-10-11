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



def s09():
    d = "S09-acces-distance"
    f = Fig(1000, 470, "Trois façons d'entrer dans un réseau à distance", "Le SSH chiffre l'administration ; la redirection de port expose un service sur Internet ; le VPN crée un tunnel chiffré vers le réseau interne.")
    f.title_bar("Trois façons d'accéder à distance, trois niveaux de risque")
    cols = [("SSH", "Je me connecte à UN équipement", "(administration)", "Chiffré. Compte nominatif.", "Telnet = en clair : à bannir.", TEAL_L, TEAL),
            ("Redirection de port", "J'expose UN service sur Internet", "(ex. site web port 8080)", "Visible de tout le monde.", "Chaque port ouvert = un risque.", ORA_L, ORA),
            ("VPN", "J'entre DANS le réseau interne", "(tunnel chiffré)", "Comme si j'étais au bureau.", "Le plus sûr pour la télémaintenance.", IND_L, IND)]
    for i, (t, a, b, c, dd, fill, st) in enumerate(cols):
        x = 30 + i * 322
        f.rect(x, 75, 300, 280, fill, st, 3, 14)
        f.text(x + 150, 112, t, 21, st, "middle", "700")
        f.text(x + 150, 160, a, 14.5, INK, "middle", "700"); f.text(x + 150, 183, b, 13.5, MUTED)
        f.rect(x + 20, 205, 260, 3, st, st, 0, 1)
        f.text(x + 150, 240, c, 14, INK); f.text(x + 150, 272, dd, 14, INK, "middle", "700")
        f.text(x + 150, 325, "Niveau de sécurité", 12.5, MUTED)
        for k in range(3):
            f.rect(x + 90 + k * 40, 335, 34, 10, st if k <= (1 if i != 1 else 0) + (1 if i == 2 else 0) else GRY, st if k <= (1 if i != 1 else 0) + (1 if i == 2 else 0) else GRY_D, 1, 3)
    f.rect(30, 385, 940, 62, YEL_L, YEL, 2, 10)
    f.text(500, 410, "Règle de télémaintenance : un compte par technicien, une autorisation écrite du client,", 14.5, INK)
    f.text(500, 434, "un accès limité dans le temps et une trace dans le journal.", 14.5, INK)
    f.save(out(d, "acces-distance.svg"))



def s10():
    d = "S10-supervision-tickets"
    f = Fig(1000, 440, "De l'alerte à la clôture du ticket", "Un équipement tombe en panne, l'outil de supervision détecte et alerte, un ticket est ouvert, le technicien diagnostique, répare et clôture en notant la cause et l'action.")
    f.title_bar("Du capteur au ticket : le cycle d'un incident")
    et = [("1", "Détecter", "Le switch ne répond", "plus (SNMP / ping)", TEAL_L, TEAL), ("2", "Alerter", "L'outil prévient :", "e-mail, tableau de bord", IND_L, IND),
          ("3", "Ouvrir", "un ticket :", "symptôme, heure, lieu", YEL_L, "#b28704"), ("4", "Diagnostiquer", "hypothèses, tests,", "cause trouvée", ORA_L, ORA),
          ("5", "Réparer", "action menée,", "retour à la normale", RED_L, RED), ("6", "Clôturer", "ticket complété,", "client prévenu", GRN_L, GRN)]
    for i, (n, t, a, b, fill, st) in enumerate(et):
        x = 25 + (i % 3) * 320; y = 75 + (i // 3) * 165
        f.rect(x, y, 300, 140, fill, st, 3, 14); f.badge(x + 34, y + 36, n, st, 16)
        f.text(x + 170, y + 42, t, 20, INK, "middle", "700"); f.text(x + 150, y + 85, a, 14.5, INK); f.text(x + 150, y + 108, b, 14.5, INK)
    f.rect(25, 400, 950, 30, GRY, GRY_D, 1.5, 8)
    f.text(500, 421, "Un ticket bien rempli = symptôme + cause + action : c'est la mémoire de l'entreprise.", 14, INK, "middle", "700")
    f.save(out(d, "cycle-incident.svg"))



def s11():
    d = "S11-depanner-1"
    f = Fig(1000, 480, "L'échelle des tests : du poste vers le serveur", "Six tests dans l'ordre : sa propre carte, son adresse, la passerelle, une adresse au-delà du routeur, le serveur, puis le nom. Le premier test qui échoue désigne la zone en cause.")
    f.title_bar("L'échelle des tests : on monte marche par marche")
    steps = [("1", "Mon câble / ma carte", "voyant, ipconfig : lien actif ?", "câble, port, carte"),
             ("2", "Mon adresse", "ipconfig : 169.254 ? bon réseau ?", "DHCP, VLAN, IP fixe"),
             ("3", "Ma passerelle", "ping de la passerelle", "VLAN, masque, passerelle"),
             ("4", "Un autre réseau", "ping d'une adresse derrière le routeur", "routage, sous-interface"),
             ("5", "Le serveur (adresse)", "ping + page par adresse IP", "ACL, serveur"),
             ("6", "Le serveur (nom)", "page par son nom", "DNS")]
    for i, (n, t, a, z) in enumerate(steps):
        y = 70 + i * 66
        x = 40 + i * 30
        f.rect(x, y, 560, 56, [TEAL_L, TEAL_L, IND_L, IND_L, ORA_L, ORA_L][i], [TEAL, TEAL, IND, IND, ORA, ORA][i], 2.5, 10)
        f.badge(x + 26, y + 28, n, [TEAL, TEAL, IND, IND, ORA, ORA][i], 14)
        f.text(x + 52, y + 24, t, 15.5, INK, "start", "700"); f.text(x + 52, y + 44, a, 12.5, MUTED, "start")
        f.text(x + 575, y + 33, "si KO : " + z, 13.5, RED, "start", "700")
    f.save(out(d, "echelle-tests.svg"))


if __name__ == "__main__":
    for w_ in (sys.argv[1:] or ["s06", "s07", "s08", "s09", "s10", "s11"]):
        globals()[w_](); print("OK", w_)
