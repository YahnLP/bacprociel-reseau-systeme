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
    f = Fig(940, 270, "Les adresses d'un réseau /24", "De 192.168.1.0 à 192.168.1.255 : .0 est l'adresse du réseau, .1 à .254 sont utilisables, .255 est l'adresse de diffusion.")
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


def s12():
    d = "S12-dhcp-box"
    # 1. la conversation DHCP (version simplifiée) : diagramme de séquence
    f = Fig(940, 470, "La conversation DHCP", "Le PC demande une adresse, la box en propose une, le PC l'accepte, la box confirme et note le bail.")
    f.title_bar("DHCP : la box distribue les adresses, en 4 phrases")
    ic_pc(f, 200, 100, "Nouveau PC", "")
    ic_box(f, 740, 100, "Box (serveur DHCP)", "")
    f.line(200, 150, 200, 440, GRY_D, 2, dash="6 5"); f.line(740, 150, 740, 440, GRY_D, 2, dash="6 5")
    msgs = [("1", "demande", "« Je suis nouveau : qui distribue des adresses ? »", 1, IND), ("2", "offre", "« Moi ! Je te propose 192.168.1.10 pour 24 h. »", -1, ORA),
            ("3", "acceptation", "« Parfait, je prends 192.168.1.10. »", 1, IND), ("4", "confirmation", "« C'est à toi (+ passerelle et DNS). »", -1, ORA)]
    for i, (n, k, t, dr, c) in enumerate(msgs):
        y = 205 + i * 62
        x1, x2 = (210, 730) if dr > 0 else (730, 210)
        f.arrow(x1, y, x2, y, c, 3)
        f.rect(250, y - 28, 440, 22, WHITE, WHITE, 0, 0); f.text(470, y - 11, t, 13, INK, "middle", "700", maxw=430)
        f.badge(60, y, n, c); f.text(90, y + 5, k, 14, c, "start", "700")
    f.save(out(d, "dhcp-conversation.svg"))

    # 2. la passerelle
    f = Fig(940, 400, "La passerelle par défaut", "Pour joindre une machine du même réseau, le PC l'atteint directement ; pour sortir du réseau, il envoie tout à la passerelle, la box.")
    f.title_bar("La passerelle = la porte de sortie du réseau")
    f.rect(30, 55, 520, 335, IND_L, IND, 3, 16, dash="8 6"); f.text(290, 85, "Mon réseau local 192.168.1.0/24", 15, IND, "middle", "700")
    ic_pc(f, 110, 170, "PC1", "192.168.1.10"); ic_pc(f, 110, 310, "PC2", "192.168.1.11"); ic_box(f, 430, 220, "Box", "passerelle 192.168.1.1")
    f.arrow(200, 300, 200, 190, GRN, 4); f.text(215, 250, "même réseau : direct", 13, GRN, "start", "700")
    f.arrow(170, 175, 375, 215, ORA, 4)
    f.text(270, 150, "autre réseau : « à la passerelle »", 13, ORA, "middle", "700")
    ic_cloud(f, 760, 220, "Internet", "203.0.113.1, sites web…")
    f.line(480, 220, 685, 220, LINE, 4)
    f.callout(580, 290, 340, "Sans passerelle, un PC parle à son réseau… mais jamais à Internet.", YEL_L, YEL, 13.5)
    f.save(out(d, "passerelle.svg"))

    # 3. plage DHCP
    f = Fig(940, 300, "Le plan d'adresses d'une box", "Dans 192.168.1.0/24 : .1 la box, .2 à .9 réservées, .10 à .100 distribuées par le DHCP, .101 à .254 pour les équipements fixes.")
    f.title_bar("Qui a quelle adresse ? Le plan d'adressage de la box")
    segs = [(".0", 40, 40, GRY, MUTED), (".1", 80, 40, ORA_L, ORA), (".2 – .9", 120, 90, YEL_L, "#b28704"), (".10 – .100", 210, 330, GRN_L, GRN), (".101 – .254", 540, 300, IND_L, IND), (".255", 840, 60, GRY, MUTED)]
    for t, x, w, fi, c in segs:
        f.rect(x, 70, w, 60, fi, c, 2.5, 4); f.text(x + w / 2, 107, t, 15 if w > 60 else 12, c, "middle", "700")
    labs = [(60, "réseau"), (100, "box"), (165, "postes fixes\nspéciaux"), (375, "DHCP : distribuées\nautomatiquement"), (690, "serveurs, imprimantes,\nadresses fixes"), (870, "diffusion")]
    for i, (x, t) in enumerate(labs): f.text(x, 160 + (24 if i == 1 else 0), t, 12.5, INK, "middle", "700")
    f.callout(40, 215, 860, "Règle d'or : une adresse fixe ne doit JAMAIS être dans la plage DHCP, sinon la box peut la donner à un autre PC → doublon !", RED_L, RED, 14.5)
    f.save(out(d, "plage-dhcp.svg"))

    # 4. lire ipconfig /all
    f = Fig(940, 440, "Lire ipconfig /all", "Chaque ligne de ipconfig /all : adresse IPv4, masque, passerelle par défaut, serveur DHCP, bail, serveur DNS.")
    f.title_bar("Lire le résultat de « ipconfig /all »")
    f.rect(30, 55, 520, 360, "#0b1220", "#0b1220", 1, 10)
    lines = [("DHCP activé . . . . . . . . : Oui", YEL), ("Adresse IPv4 . . . . . . . : 192.168.1.10", GRN), ("Masque de sous-réseau . . : 255.255.255.0", IND_M),
             ("Passerelle par défaut . . : 192.168.1.1", ORA), ("Serveur DHCP . . . . . . . : 192.168.1.1", YEL), ("Bail obtenu . . . . . . . . : 30 sept. 08:00", "#cfd8dc"),
             ("Bail expirant . . . . . . : 1er oct. 08:00", "#cfd8dc"), ("Serveurs DNS . . . . . . . : 192.168.1.1", "#80deea")]
    ys = []
    for i, (t, c) in enumerate(lines):
        y = 100 + i * 42; ys.append(y); f.mono(45, y, t, 13.5, c, "start", "700")
    notes = ["Adresse donnée\nautomatiquement ?", "MON adresse", "où coupe le réseau", "LA PORTE DE SORTIE", "qui m'a donné l'adresse", "début du prêt", "fin du prêt (il faut renouveler)", "qui traduit les noms (S13)"]
    for y, t in zip(ys, notes):
        f.line(552, y - 5, 590, y - 5, LINE, 2, arrow=True); f.text(600, y, t.replace("\n", " "), 14, INK, "start", "700")
    f.save(out(d, "lire-ipconfig.svg"))

    # 5. bail
    f = Fig(940, 220, "Le bail DHCP", "L'adresse est prêtée pour une durée limitée : le bail. Le poste la renouvelle avant la fin, sinon la box peut la reprendre.")
    f.title_bar("Une adresse DHCP est PRÊTÉE (bail)")
    f.line(80, 130, 860, 130, LINE, 6)
    for x, t, c in [(80, "obtenu\n(08:00)", GRN), (470, "mi-bail :\nle PC demande\nà renouveler", IND), (860, "fin du bail\n(le lendemain)", RED)]:
        f.circle(x, 130, 13, c, c, 2); f.text(x, 175, t, 13, INK, "middle", "700")
    f.callout(100, 60, 740, "ipconfig /release : je rends l'adresse  -  ipconfig /renew : j'en redemande une", YEL_L, YEL, 14)
    f.save(out(d, "bail.svg"))


def s13():
    d = "S13-dns-internet"
    # 1. annuaire
    f = Fig(940, 365, "Le DNS, l'annuaire d'Internet", "Le DNS transforme un nom facile à retenir comme www.exemple.fr en adresse IP utilisable par les machines.")
    f.title_bar("Le DNS : l'annuaire d'Internet")
    f.rect(40, 70, 380, 200, IND_L, IND, 3, 14); f.text(230, 100, "Ce que TU tapes", 17, IND, "middle", "700")
    f.mono(230, 160, "www.exemple.fr", 22, INK, "middle", "700"); f.text(230, 200, "facile à retenir, mais\nles machines ne comprennent pas", 14, MUTED)
    f.rect(520, 70, 380, 200, ORA_L, ORA, 3, 14); f.text(710, 100, "Ce que la machine utilise", 17, ORA, "middle", "700")
    f.mono(710, 160, "198.51.100.80", 24, INK, "middle", "700"); f.text(710, 200, "une adresse IP", 14, MUTED)
    f.arrow(425, 150, 515, 150, GRN, 5); f.text(470, 128, "DNS", 17, GRN, "middle", "700"); f.text(470, 180, "traduit", 13, GRN, "middle", "700")
    f.callout(40, 285, 860, "Comme dans ton téléphone : tu cherches « Maman », le répertoire trouve le numéro. Le DNS fait pareil pour les sites.", YEL_L, YEL, 14.5)
    f.save(out(d, "dns-annuaire.svg"))

    # 2. chemin d'une requête : diagramme de séquence
    f = Fig(940, 520, "Du nom à la page web", "PC, box, DNS du FAI et serveur web : le PC demande l'adresse au DNS via la box, puis demande la page au serveur.")
    f.title_bar("Comment mon PC atteint un site web")
    cols = [(110, "Mon PC", "192.168.1.10", IND), (350, "Box", "192.168.1.1", ORA), (590, "DNS du FAI", "198.51.100.53", TEAL), (830, "www.exemple.fr", "198.51.100.80", IND)]
    for x, n, ip, c in cols:
        f.rect(x - 80, 50, 160, 50, WHITE, c, 3, 10); f.text(x, 72, n, 15, c, "middle", "700"); f.mono(x, 92, ip, 11.5, MUTED, "middle")
        f.line(x, 100, x, 500, GRY_D, 2, dash="6 5")
    msgs = [(0, 1, "1  « Adresse de ce nom ? »", IND, False), (1, 2, "2  la box interroge le DNS", ORA, False), (2, 1, "3  « c'est 198.51.100.80 »", GRN, True),
            (1, 0, "4  « c'est 198.51.100.80 »", GRN, True), (0, 3, "5  « Donne-moi la page ! » (via la passerelle)", IND, False), (3, 0, "6  la page web revient", GRN, True)]
    for i, (a_, b_, t, c, dash) in enumerate(msgs):
        y = 145 + i * 58; x1, x2 = cols[a_][0], cols[b_][0]
        f.arrow(x1 + (8 if x2 > x1 else -8), y, x2 - (8 if x2 > x1 else -8), y, c, 3, "6 4" if dash else None)
        f.halo = WHITE; f.text((x1 + x2) / 2, y - 10, t, 12.5, c, "middle", "700", maxw=abs(x2 - x1) - 10); f.halo = None
    f.rect(40, 468, 860, 40, GRY, GRY_D, 1.5, 8); f.text(470, 494, "Étapes 1 à 4 = le DNS (traduire). Étapes 5 et 6 = le web (aller chercher la page).", 14, INK, "middle", "700")
    f.save(out(d, "chemin-site.svg"))

    # 3. NAT en une image
    f = Fig(940, 470, "Le NAT en une image", "Trois PC en adresses privées sortent sur Internet avec la même adresse publique, celle de la box.")
    f.title_bar("NAT : toute la maison sort avec UNE adresse publique")
    f.rect(30, 55, 330, 400, IND_L, IND, 3, 16, dash="8 6"); f.text(195, 82, "Réseau privé (chez toi)", 14.5, IND, "middle", "700")
    for i, ip in enumerate(["192.168.1.10", "192.168.1.11", "192.168.1.12"]): ic_pc(f, 100, 120 + i * 112, "PC" + str(i + 1), ip)
    ic_box(f, 440, 220, "Box", "fait le NAT"); ic_cloud(f, 810, 220, "Internet", "")
    for i in range(3): f.line(150, 120 + i * 112, 395, 215, IND, 2.5)
    f.line(485, 220, 750, 220, ORA, 4)
    f.rect(540, 130, 190, 60, WHITE, ORA, 2.5, 10); f.text(635, 155, "Pour Internet :", 12.5, MUTED, "middle", "700"); f.mono(635, 178, "203.0.113.2", 16, ORA, "middle", "700")
    f.callout(520, 265, 400, "La box note : « PC1 a demandé » → elle remplace son adresse privée par la sienne et, au retour, remet la réponse au bon PC.", YEL_L, YEL, 13.5)
    f.save(out(d, "nat.svg"))

    # 4. arbre de diagnostic « pas Internet »
    f = Fig(940, 400, "J'ai un réseau mais pas Internet : par où commencer ?", "Ping de la box, ping d'une adresse sur Internet, ping d'un nom : trois tests dans l'ordre pour trouver la panne.")
    f.title_bar("« Je n'ai pas Internet » : 3 pings, dans l'ordre")
    steps = [("1", "ping 192.168.1.1", "(la box)", "ÉCHEC → problème de câble, d'adresse ou de DHCP\n(S10, S11, S12)", RED),
             ("2", "ping 203.0.113.1", "(une adresse sur Internet)", "ÉCHEC → passerelle absente ou box sans accès\nau FAI (S12)", RED),
             ("3", "ping www.exemple.fr", "(un nom)", "ÉCHEC alors que le 2 marche → panne DNS\n(vérifier le serveur DNS : ipconfig /all)", RED)]
    for i, (n, c, k, r, col) in enumerate(steps):
        y = 65 + i * 105
        f.badge(60, y + 40, n, IND, 16); f.rect(95, y, 330, 85, WHITE, IND, 2.5, 10); f.mono(110, y + 35, c, 17, IND, "start", "700"); f.text(110, y + 62, k, 13.5, MUTED, "start")
        f.rect(450, y, 460, 85, RED_L, col, 2.5, 10); f.text(465, y + 32, r, 13.5, INK, "start", "700", maxw=435)
        if i < 2: f.text(260, y + 100, "OK ↓", 12, GRN, "middle", "700")
    f.save(out(d, "diagnostic-internet.svg"))


def s14():
    d = "S14-wifi"
    # 1. SSID / clé / DHCP : diagramme de séquence
    f = Fig(940, 520, "Se connecter à un Wi-Fi", "Trois étapes : choisir le SSID annoncé par la borne, donner la clé, puis obtenir une adresse IP du DHCP de la box.")
    f.title_bar("Se connecter en Wi-Fi : 3 étapes, dans l'ordre")
    cols = [(150, "Portable", "", IND), (470, "Borne Wi-Fi", "SSID : ATELIER-CIEL", TEAL), (790, "Box (DHCP)", "192.168.1.1", ORA)]
    for x, n, sub_, c in cols:
        f.rect(x - 85, 50, 170, 54, WHITE, c, 3, 10); f.text(x, 73, n, 15, c, "middle", "700"); f.mono(x, 94, sub_, 11.5, MUTED, "middle")
        f.line(x, 104, x, 440, GRY_D, 2, dash="6 5")
    msgs = [(1, 0, "« Je suis le réseau ATELIER-CIEL »", TEAL, True, "1"), (0, 1, "« Je veux me connecter, voici la clé »", IND, False, "2"), (1, 0, "« Clé correcte : tu es connecté »", GRN, True, "2"),
            (0, 2, "« Quelle adresse pour moi ? » (via la borne)", IND, False, "3"), (2, 0, "« Prends 192.168.1.12 »", GRN, True, "3")]
    for i, (a_, b_, t, c, dash, n) in enumerate(msgs):
        y = 150 + i * 60; x1, x2 = cols[a_][0], cols[b_][0]
        f.arrow(x1 + (8 if x2 > x1 else -8), y, x2 - (8 if x2 > x1 else -8), y, c, 3, "6 4" if dash else None)
        f.halo = WHITE; f.text((x1 + x2) / 2, y - 10, t, 12.5, c, "middle", "700", maxw=abs(x2 - x1) - 20); f.halo = None
        f.badge(40 if i in (0,) else (40 if i in (1, 2) else 40), y, n, [IND, ORA, ORA, GRN, GRN][i] if False else (TEAL if n == "1" else (ORA if n == "2" else GRN)))
    f.rect(25, 450, 890, 50, YEL_L, YEL, 2, 8)
    f.text(470, 472, "1 = je choisis le réseau (SSID) · 2 = je donne la clé · 3 = je reçois une adresse (DHCP, comme en S12)", 13.5, INK, "middle", "700")
    f.text(470, 491, "Si l'étape 2 échoue (mauvaise clé) : pas d'adresse IP, l'adressage vient après la connexion Wi-Fi.", 13, RED, "middle", "700")
    f.save(out(d, "etapes-wifi.svg"))

    # 2. 2,4 GHz vs 5 GHz
    f = Fig(940, 340, "Bandes 2,4 GHz et 5 GHz", "2,4 GHz porte plus loin mais est plus encombré et plus lent ; 5 GHz est plus rapide mais traverse moins bien les obstacles.")
    f.title_bar("Deux bandes, deux compromis")
    for x, t, c, lines in [(30, "2,4 GHz", ORA, ["PORTÉE : longue (traverse mieux les murs)", "DÉBIT : plus faible", "ENCOMBREMENT : fort (voisins, micro-ondes, Bluetooth)", "Canaux utiles : 1, 6, 11"]),
                           (490, "5 GHz", IND, ["PORTÉE : plus courte", "DÉBIT : plus élevé", "ENCOMBREMENT : faible", "Plus de canaux, moins de brouillage"])]:
        f.rect(x, 60, 420, 210, WHITE, c, 3, 14); f.rect(x, 60, 420, 44, c, c, 3, 14); f.text(x + 210, 90, t, 20, WHITE, "middle", "700")
        for i, l in enumerate(lines): f.text(x + 18, 134 + i * 34, l, 13.5, INK, "start", "700" if i < 2 else "400", maxw=390)
    f.callout(30, 285, 880, "Pour un atelier : 5 GHz pour le travail (rapide) ; 2,4 GHz pour les objets connectés et les zones éloignées.", YEL_L, YEL, 14.5)
    f.save(out(d, "bandes.svg"))

    # 3. canaux 2,4 GHz
    f = Fig(940, 350, "Canaux 2,4 GHz : 1, 6 et 11", "Les canaux 1, 6 et 11 ne se chevauchent pas : on les choisit pour éviter les interférences entre bornes voisines.")
    f.title_bar("2,4 GHz : seuls 3 canaux ne se chevauchent pas")
    f.line(50, 230, 890, 230, LINE, 3)
    cols = {1: IND, 6: ORA, 11: GRN}
    import math
    for ch in range(1, 12):
        cx = 50 + 40 + (ch - 1) * 75
        if ch in cols:
            c = cols[ch]; pts = [(cx - 85 + i * 8.5, 230 - 120 * math.sin(math.pi * i / 20) ** 2) for i in range(21)]
            f.path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), "none", c, 4)
            f.text(cx, 255, "canal " + str(ch), 14, c, "middle", "700")
        else:
            f.text(cx, 255, str(ch), 12, MUTED)
    f.callout(40, 280, 860, "Deux bornes voisines sur des canaux proches (1 et 2) se gênent : mets-les sur 1, 6 et 11.", YEL_L, YEL, 14)
    f.save(out(d, "canaux.svg"))

    # 4. force du signal
    f = Fig(940, 300, "Lire la force du signal", "Le signal se mesure en dBm : plus le nombre est proche de zéro, meilleur est le signal.")
    f.title_bar("Force du signal (dBm) : plus c'est proche de 0, mieux c'est")
    bands = [("-30 à -50", "Excellent", GRN, GRN_L), ("-50 à -67", "Très bon", GRN, GRN_L), ("-67 à -70", "Correct (limite)", YEL, YEL_L), ("-70 à -80", "Faible", ORA, ORA_L), ("< -80", "Inutilisable", RED, RED_L)]
    for i, (v, t, c, fi) in enumerate(bands):
        x = 30 + i * 180
        f.rect(x, 70, 172, 120, fi, c, 3, 12); f.text(x + 86, 112, v, 18, c, "middle", "700"); f.text(x + 86, 150, t, 14.5, INK, "middle", "700")
    f.callout(30, 215, 880, "Objectif en entreprise : au moins -67 dBm partout où l'on travaille. Les murs épais, le métal, l'eau et les miroirs affaiblissent le signal.", YEL_L, YEL, 14)
    f.save(out(d, "signal.svg"))

    # 5. ouvert vs WPA2 + réseau invité
    f = Fig(940, 440, "Réseau interne et réseau invité", "Le réseau invité donne Internet aux visiteurs sans leur donner accès aux ordinateurs et serveurs de l'entreprise.")
    f.title_bar("Réseau interne / réseau invité")
    ic_box(f, 470, 100, "Box / borne", "")
    f.rect(30, 190, 420, 220, IND_L, IND, 3, 14); f.text(240, 218, "ATELIER-CIEL  (interne)", 16, IND, "middle", "700")
    ic_pc(f, 100, 280, "PC", ""); ic_server(f, 200, 275, "Serveur", ""); ic_printer(f, 300, 280, "Imprimante", ""); f.text(240, 380, "WPA2/WPA3 + clé forte : les salariés", 12.5, INK, "middle", "700")
    f.rect(490, 190, 420, 220, ORA_L, ORA, 3, 14); f.text(700, 218, "ATELIER-INVITES  (invité)", 16, ORA, "middle", "700")
    ic_phone(f, 600, 285, "Visiteur", ""); ic_laptop(f, 790, 285, "Portable", ""); f.text(700, 380, "clé simple, accès à Internet SEULEMENT", 12.5, INK, "middle", "700")
    f.arrow(420, 150, 330, 188, IND, 3); f.arrow(520, 150, 610, 188, ORA, 3)
    f.line(450, 300, 490, 300, RED, 4, dash="5 4"); f.text(470, 330, "mur", 11, RED, "middle", "700")
    f.save(out(d, "invite.svg"))


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s11", "s12", "s13", "s14"]):
        globals()[w](); print("OK", w)
