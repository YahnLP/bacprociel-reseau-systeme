#!/usr/bin/env python3
"""Illustrations Seconde – S11 (adresse IP), S12 (DHCP, box), S13 (DNS), S14 (Wi-Fi)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "seconde"))
out = lambda s, n: os.path.join(ROOT, s, "images", n)


def switch(f, x, y, on, val, w=64):
    f.rect(x - w / 2, y, w, 70, "#e8f5e9" if on else GRY, GRN if on else GRY_D, 3, 8)
    f.rect(x - 12, y + (6 if on else 36), 24, 28, GRN if on else GRY_D, GRN if on else GRY_D, 1, 6)
    f.text(x, y + 98, str(val), 15, INK, "middle", "700")
    f.text(x, y + 122, "1" if on else "0", 20, GRN if on else MUTED, "middle", "700")


def s11():
    d = "S11-adresse-ip"
    # 1. un octet = 8 interrupteurs
    f = Fig(940, 400, "Un octet = 8 interrupteurs", "Huit interrupteurs valant 128, 64, 32, 16, 8, 4, 2, 1. Exemple : 192 = 128 + 64 = 11000000.")
    f.title_bar("Un octet = 8 interrupteurs (0 = éteint, 1 = allumé)")
    vals = [128, 64, 32, 16, 8, 4, 2, 1]
    ex = [1, 1, 0, 0, 0, 0, 0, 0]
    for i, v in enumerate(vals):
        switch(f, 80 + i * 110, 60, bool(ex[i]), v)
    f.rect(40, 215, 860, 54, YEL_L, YEL, 2.5, 10)
    f.text(470, 250, "128 + 64 = 192   →   11000000   (on additionne les valeurs des interrupteurs allumés)", 17, INK, "middle", "700")
    f.text(40, 305, "Autres exemples :", 15, MUTED, "start", "700")
    f.mono(40, 335, "168 = 128 + 32 + 8        →  1 0 1 0 1 0 0 0", 17, IND, "start", "700")
    f.mono(40, 365, "  1 = 1                    →  0 0 0 0 0 0 0 1", 17, IND, "start", "700")
    f.mono(500, 335, "255 = tout allumé → 1 1 1 1 1 1 1 1", 17, ORA, "start", "700")
    f.mono(500, 365, "  0 = tout éteint → 0 0 0 0 0 0 0 0", 17, ORA, "start", "700")
    f.save(out(d, "octet.svg"))

    # 2. anatomie d'une adresse
    f = Fig(940, 330, "Anatomie d'une adresse IPv4", "192.168.1.11 : quatre octets séparés par des points ; les trois premiers désignent le réseau, le dernier la machine, avec le masque 255.255.255.0.")
    f.title_bar("Une adresse IPv4 : 4 nombres de 0 à 255")
    xs = [110, 300, 490, 680]
    nums = ["192", "168", "1", "11"]
    for i, (x, n) in enumerate(zip(xs, nums)):
        c = IND if i < 3 else ORA; fi = IND_L if i < 3 else ORA_L
        f.rect(x - 70, 70, 140, 80, fi, c, 3.5, 12); f.mono(x, 125, n, 44, c, "middle", "700")
        if i < 3: f.circle(x + 95, 138, 6, INK, INK, 1)
    f.line(40, 175, 565, 175, IND, 5); f.text(302, 205, "RÉSEAU : « le nom de la rue »", 17, IND, "middle", "700")
    f.line(615, 175, 745, 175, ORA, 5); f.text(680, 205, "MACHINE : « le n° »", 17, ORA, "middle", "700")
    f.rect(40, 235, 860, 70, WHITE, LINE, 2, 10)
    f.text(60, 262, "Masque : ", 17, INK, "start", "700"); f.mono(155, 262, "255.255.255.0", 17, INK, "start", "700")
    f.text(60, 290, "Il dit : « les 3 premiers nombres = le réseau, le dernier = la machine ». On l'écrit aussi /24 (24 interrupteurs allumés).", 14.5, MUTED, "start")
    f.save(out(d, "anatomie-ip.svg"))

    # 3. la rue
    f = Fig(940, 320, "Réseau = rue, machine = numéro", "Analogie : toutes les maisons d'une même rue partagent le nom de la rue et ont un numéro différent.")
    f.title_bar("L'analogie de la rue")
    f.rect(30, 140, 880, 40, "#cfd8dc", GRY_D, 2, 6)
    f.text(470, 166, "RUE 192.168.1  (le réseau)", 16, INK, "middle", "700")
    for i, n in enumerate([1, 11, 12, 13, 14]):
        x = 110 + i * 170
        col = ORA if n == 1 else IND
        f.poly([(x - 40, 120), (x, 70), (x + 40, 120)], col, col, 2)
        f.rect(x - 32, 120, 64, 20, IND_L if n != 1 else ORA_L, col, 2.5, 1)
        f.text(x, 100, "", 1)
        f.mono(x, 215, "192.168.1." + str(n), 15, col, "middle", "700")
        f.text(x, 240, "box (passerelle)" if n == 1 else f"PC {i}", 13, MUTED)
    f.callout(30, 262, 880, "Même rue (même réseau) = on peut se parler directement. Une autre rue = il faut passer par la passerelle (la box).", YEL_L, YEL, 15)
    f.save(out(d, "rue.svg"))

    # 4. la plage /24
    f = Fig(940, 330, "Les adresses d'un réseau /24", "De 192.168.1.0 à 192.168.1.255 : .0 est l'adresse du réseau, .1 à .254 sont utilisables, .255 est l'adresse de diffusion.")
    f.title_bar("192.168.1.0 /24 : 256 adresses, dont 254 pour les machines")
    f.rect(40, 70, 70, 60, GRY, GRY_D, 2.5, 6); f.mono(75, 107, ".0", 24, MUTED, "middle", "700")
    f.rect(110, 70, 720, 60, GRN_L, GRN, 2.5, 6); f.text(470, 108, ".1 à .254 : adresses utilisables (254)", 20, GRN, "middle", "700")
    f.rect(830, 70, 70, 60, GRY, GRY_D, 2.5, 6); f.mono(865, 107, ".255", 22, MUTED, "middle", "700")
    f.text(75, 160, "adresse du\nRÉSEAU", 13.5, INK, "middle", "700"); f.text(865, 160, "adresse de\nDIFFUSION", 13.5, INK, "middle", "700")
    f.text(75, 205, "le nom de la rue :\non ne l'attribue\njamais à une machine", 12.5, MUTED); f.text(865, 205, "le « haut-parleur » :\ntout le monde l'entend\n(jamais à une machine)", 12.5, MUTED)
    f.callout(160, 160, 600, "Habitude de technicien : .1 = la passerelle (box / routeur), .10 à .99 = postes, .100 et + = serveurs et imprimantes. Il faut un plan d'adressage !", IND_L, IND, 14.5)
    f.save(out(d, "plage.svg"))

    # 5. adresses privées
    f = Fig(940, 300, "Adresses privées et publiques", "Les adresses 192.168.x.x, 10.x.x.x et 172.16 à 172.31 sont privées : utilisées dans les réseaux locaux, non routées sur Internet.")
    f.title_bar("Adresses privées / publiques")
    f.rect(30, 60, 560, 200, IND_L, IND, 3, 14); f.text(310, 90, "PRIVÉES : réseaux locaux", 18, IND, "middle", "700")
    for i, t in enumerate(["192.168.0.0  à  192.168.255.255", "10.0.0.0  à  10.255.255.255", "172.16.0.0  à  172.31.255.255"]):
        f.mono(60, 130 + i * 38, t, 17, INK, "start", "700")
    f.text(310, 245, "Utilisées chez toi, en classe, en entreprise. Réutilisables partout.", 13.5, MUTED)
    f.rect(620, 60, 290, 200, ORA_L, ORA, 3, 14); f.text(765, 90, "PUBLIQUES", 18, ORA, "middle", "700")
    f.text(765, 130, "Toutes les autres.\nUniques au monde.\nAttribuées par\nl'opérateur (FAI).", 14.5, INK)
    f.save(out(d, "privees.svg"))

    # 6. les 3 messages d'erreur du ping
    f = Fig(940, 340, "Que dit le ping quand ça ne va pas ?", "Trois messages différents : échec général (mauvais réseau ou pas d'adresse), délai dépassé (pas de réponse), hôte inaccessible.")
    f.title_bar("Le message de ping est un indice")
    cases = [("PING : échec général.", "Ma machine ne sait même pas où envoyer le paquet.", "Mon adresse est vide ou dans un autre réseau (faute de frappe, mauvais masque).", RED),
             ("Délai d'attente de la demande dépassé.", "Le paquet est parti, mais aucune réponse ne revient.", "L'autre machine est éteinte, a un mauvais masque, ou son pare-feu bloque le ping.", ORA),
             ("Impossible de joindre l'hôte de destination.", "Une machine (souvent la mienne ou une passerelle) dit « je ne trouve personne ».", "Adresse qui n'existe pas dans le réseau, ou doublon d'adresse.", IND)]
    for i, (m, a, b, c) in enumerate(cases):
        x = 15 + i * 308
        f.rect(x, 60, 296, 255, WHITE, c, 3, 12)
        f.rect(x + 10, 70, 276, 70, "#1e1e2e", "#1e1e2e", 1, 6); f.mono(x + 18, 98, "", 1); f.text(x + 148, 100, m, 13, "#a6e3a1", "middle", "700", maxw=256)
        f.text(x + 148, 165, "Ça veut dire :", 13, c, "middle", "700"); f.text(x + 148, 185, a, 13, INK, maxw=270)
        f.text(x + 148, 245, "Pistes :", 13, c, "middle", "700"); f.text(x + 148, 265, b, 12.5, INK, maxw=270)
    f.save(out(d, "messages-ping.svg"))


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s11"]):
        globals()[w](); print("OK", w)
