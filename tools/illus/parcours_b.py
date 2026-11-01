#!/usr/bin/env python3
"""Illustrations du parcours de mise à niveau – M04 à M08."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "terminale", "mise-a-niveau", "images"))
out = lambda n: os.path.join(ROOT, n)


def m04_couches():
    f = Fig(1000, 520, "Les quatre couches", "Quatre couches empilées : application, transport, réseau et accès réseau, avec leur rôle, leur adresse et ce qui peut les casser.")
    f.title_bar("Un message traverse quatre couches")
    L = [("APPLICATION", "le service demandé", "Port : 80, 443, 53, 67", "Service arrêté, mauvais DNS", IND, IND_L),
         ("TRANSPORT", "le dialogue de bout en bout", "Numéro de port, TCP / UDP", "Port filtré, service sur un autre port", TEAL, TEAL_L),
         ("RÉSEAU", "aller d'un réseau à l'autre", "Adresse IP, ping (ICMP)", "Mauvaise adresse, passerelle, route", ORA, ORA_L),
         ("ACCÈS RÉSEAU", "aller chez le voisin direct", "Adresse MAC, Ethernet, Wi-Fi", "Câble, port, VLAN, carte réseau", "#8e24aa", "#f3e5f5")]
    f.text(130, 68, "Couche", 13, MUTED, "middle", "700"); f.text(350, 68, "Son rôle", 13, MUTED, "middle", "700"); f.text(590, 68, "Son adresse / repère", 13, MUTED, "middle", "700"); f.text(840, 68, "Ce qui la casse", 13, MUTED, "middle", "700")
    for i, (t, r, a, b, c, fl) in enumerate(L):
        y = 80 + i * 92
        f.rect(30, y, 940, 80, fl, c, 3, 12); f.rect(30, y, 200, 80, c, c, 0, 12); f.rect(210, y, 20, 80, c, c, 0, 0)
        f.text(130, y + 47, t, 17, WHITE, "middle", "700")
        f.text(350, y + 36, r, 14.5, INK, "middle", "700", maxw=180); f.text(590, y + 36, a, 14.5, INK, "middle", "700", maxw=200); f.text(840, y + 36, b, 14, INK, "middle", maxw=200)
    f.arrow(995, 90, 995, 430, GRY_D, 2)
    f.rect(30, 455, 940, 50, YEL_L, YEL, 2, 10)
    f.text(500, 477, "Pour dépanner : on remonte de la couche du bas (câble) vers celle du haut (service).", 14.5, INK, "middle", "700")
    f.text(500, 496, "Un problème en bas rend inutile tout ce qui se règle au-dessus.", 13.5, MUTED)
    f.save(out("m04-couches.svg"))


def m04_encapsulation():
    f = Fig(1000, 420, "L'emballage des données", "Les données sont enveloppées par un en-tête de transport, puis un en-tête IP, puis un en-tête Ethernet avec adresses MAC.")
    f.title_bar("Chaque couche ajoute son enveloppe (encapsulation)")
    f.rect(330, 70, 340, 56, IND_L, IND, 3, 8); f.text(500, 104, "DONNÉES (ex. : demande de page web)", 14.5, IND, "middle", "700")
    f.rect(230, 150, 540, 56, TEAL_L, TEAL, 3, 8); f.rect(230, 150, 100, 56, TEAL, TEAL, 0, 8); f.text(280, 184, "port 443", 14, WHITE, "middle", "700"); f.text(550, 184, "DONNÉES", 14.5, TEAL, "middle", "700")
    f.rect(130, 230, 740, 56, ORA_L, ORA, 3, 8); f.rect(130, 230, 200, 56, ORA, ORA, 0, 8); f.text(230, 255, "IP source 192.168.10.25", 11.5, WHITE, "middle", "700"); f.text(230, 273, "IP dest. 203.0.113.10", 11.5, WHITE, "middle", "700"); f.text(600, 264, "port + DONNÉES", 14.5, ORA, "middle", "700")
    f.rect(30, 310, 940, 56, "#f3e5f5", "#8e24aa", 3, 8); f.rect(30, 310, 260, 56, "#8e24aa", "#8e24aa", 0, 8); f.text(160, 335, "MAC source : 00:D0:95:12:34:56", 11, WHITE, "middle", "700"); f.text(160, 353, "MAC dest. : (la passerelle)", 11, WHITE, "middle", "700"); f.text(630, 344, "IP + port + DONNÉES", 14.5, "#8e24aa", "middle", "700")
    for y, t, c in [(98, "Application", IND), (178, "Transport", TEAL), (258, "Réseau", ORA), (338, "Accès réseau", "#8e24aa")]:
        f.text(120 if y > 250 else (220 if y > 170 else 320), y + 5, "", 1)
    f.text(30, 100, "Application", 13, IND, "start", "700"); f.text(30, 184, "Transport", 13, TEAL, "start", "700"); f.text(30, 262, "Réseau", 13, ORA, "start", "700")
    f.text(500, 398, "L'ensemble est une « trame » : ce qui circule réellement sur le câble. Chaque équipement lit la couche qui le concerne.", 13.5, MUTED)
    f.save(out("m04-encapsulation.svg"))


def m04_arp():
    f = Fig(1000, 400, "Le protocole ARP", "Le poste demande à tous quelle est la MAC de 192.168.10.5, le serveur répond avec sa MAC.")
    f.title_bar("ARP : retrouver la MAC d'un équipement dont on connaît l'IP")
    f.line(120, 230, 880, 230, LINE, 4)
    node(f, "pc", 150, 210, "PC-1", "192.168.10.25"); node(f, "server", 520, 195, "Serveur", "192.168.10.5"); node(f, "printer", 850, 210, "Imprimante", "192.168.10.20")
    f.rect(70, 60, 400, 56, IND_L, IND, 3, 10); f.text(270, 84, "①  À TOUS (diffusion) :", 14.5, IND, "middle", "700"); f.text(270, 104, "« Qui a l'adresse 192.168.10.5 ? »", 14.5, INK)
    f.arrow(200, 118, 200, 175, IND, 3); f.arrow(250, 118, 440, 160, IND, 2, "6 4"); f.arrow(300, 118, 800, 160, IND, 2, "6 4")
    f.rect(540, 60, 410, 56, TEAL_L, TEAL, 3, 10); f.text(745, 84, "②  Le serveur répond, à PC-1 seul :", 14.5, TEAL, "middle", "700"); f.text(745, 104, "« C'est moi, ma MAC est 00:D0:95:AA:BB:CC »", 14, INK)
    f.arrow(520, 150, 270, 185, TEAL, 3)
    f.rect(60, 300, 880, 72, YEL_L, YEL, 2, 10)
    f.text(500, 326, "③  PC-1 garde la réponse dans sa table ARP (commande arp -a) pour ne pas redemander.", 14.5, INK, "middle", "700")
    f.text(500, 350, "L'imprimante, qui n'est pas concernée, ignore la question.", 13.5, MUTED)
    f.save(out("m04-arp.svg"))


def m04_mac():
    f = Fig(1000, 440, "Le switch apprend les adresses MAC", "Un switch avec trois PC. Il note la MAC source de chaque trame et le port d'arrivée dans sa table, puis n'envoie ensuite que vers le bon port.")
    f.title_bar("Le switch apprend : MAC source → port d'arrivée")
    f.rect(330, 120, 340, 100, TEAL_L, TEAL, 4, 12)
    for i in range(4):
        f.rect(350 + i * 76, 135, 56, 34, WHITE, TEAL, 2, 4); f.text(378 + i * 76, 157, f"1/{i+1}", 14, TEAL, "middle", "700")
    f.text(500, 200, "SWITCH", 15, TEAL, "middle", "700")
    for i, (x, n, m) in enumerate([(120, "PC-1", "…:11"), (330, "PC-2", "…:22"), (670, "PC-3", "…:33")]):
        pass
    for p, (x, n, m) in zip([378, 454, 530], [(100, "PC-1", "MAC …:11"), (360, "PC-2", "MAC …:22"), (640, "PC-3", "MAC …:33")]):
        f.line(p, 169, x + 40, 280, LINE, 3)
        node(f, "pc", x + 40, 300, n, m)
    f.rect(720, 70, 250, 190, WHITE, IND, 3, 12); f.text(845, 96, "Table d'adresses MAC", 14.5, IND, "middle", "700")
    for i, (m, p) in enumerate([("…:11", "1/1"), ("…:22", "1/2"), ("…:33", "1/3")]):
        f.rect(735, 112 + i * 38, 220, 30, IND_L, IND_M, 1.5, 5); f.text(790, 133 + i * 38, m, 14, INK, "middle", "700"); f.text(870, 133 + i * 38, "→ port " + p, 14, INK, "middle", "700")
    f.rect(30, 380, 940, 48, YEL_L, YEL, 2, 10)
    f.text(500, 402, "Quand PC-1 envoie à PC-3, le switch lit la MAC source (…:11), la mémorise avec le port 1/1,", 13.5, INK)
    f.text(500, 420, "puis envoie vers le port de PC-3 seulement. Si la MAC est inconnue, il envoie sur tous les ports sauf celui d'arrivée.", 13.5, MUTED)
    f.save(out("m04-table-mac.svg"))


def m04_echelle():
    f = Fig(1000, 470, "Délimiter une panne avec des ping successifs", "Une échelle de cinq ping, du plus proche au plus lointain : sa propre adresse, un voisin, la passerelle, une adresse Internet, un nom.")
    f.title_bar("L'échelle des ping : on monte jusqu'à la première marche qui échoue")
    steps = [("1", "ping 127.0.0.1", "ma propre pile réseau", "poste à réparer"), ("2", "ping un voisin", "câble, switch, VLAN, adresse", "câble, port, VLAN, masque"),
             ("3", "ping la passerelle", "poste bien relié au routeur", "passerelle erronée, routeur"), ("4", "ping 8.8.8.8", "Internet joignable par IP", "route par défaut, box"),
             ("5", "ping www.exemple.fr", "le DNS fonctionne", "serveur DNS erroné")]
    f.text(560, 66, "si ça marche, c'est que…", 13, GRN, "middle", "700"); f.text(860, 66, "si ça échoue, suspecter…", 13, RED, "middle", "700")
    for i, (n, c, ok, ko) in enumerate(steps):
        y = 78 + i * 74
        f.rect(30 + i * 36, y, 300, 60, IND_L, IND, 2.5, 10); f.badge(52 + i * 36, y + 30, n, IND, 14); f.mono(76 + i * 36, y + 36, c, 14.5, INK, "start", "700")
        f.arrow(335 + i * 36 - 0, y + 30, 420, y + 30, GRN, 2.5) if False else None
        f.rect(430, y, 240, 60, GRN_L, GRN, 2, 10); f.text(550, y + 36, ok, 13.5, INK, "middle", maxw=220)
        f.rect(690, y, 280, 60, RED_L, RED, 2, 10); f.text(830, y + 36, ko, 13.5, INK, "middle", maxw=260)
    f.save(out("m04-echelle-ping.svg"))


def m05_console():
    f = Fig(1000, 380, "La connexion console", "Un PC portable relié par un câble console USB vers RJ45 au port console du switch, avec les réglages du terminal.")
    f.title_bar("Première configuration : par le câble console")
    node(f, "laptop", 130, 210, "PC portable", "terminal série"); node(f, "switch", 720, 200, "OmniSwitch")
    f.rect(770, 96, 90, 34, "#eceff1", "#455a64", 2, 4)
    f.text(815, 118, "CONSOLE", 11.5, "#455a64", "middle", "700")
    f.path("M165,225 C300,300 640,300 780,134", "none", "#00acc1", 6); f.path("M165,225 C300,300 640,300 780,134", "none", "#e0f7fa", 2)
    f.text(430, 322, "câble console (USB → RJ45)", 15, "#00838f", "middle", "700")
    f.rect(70, 70, 330, 90, "#1e1e1e", "#37474f", 3, 8)
    f.mono(86, 98, "Terminal série (PuTTY…)", 13, "#80cbc4", "start", "700"); f.mono(86, 120, "Vitesse : 9600 bauds", 13, "#fff59d"); f.mono(86, 140, "8 bits · pas de parité · 1 arrêt", 13, "#fff59d")
    f.rect(440, 70, 300, 90, YEL_L, YEL, 2, 10)
    f.text(590, 96, "Pourquoi la console ?", 14.5, INK, "middle", "700"); f.text(590, 118, "Elle marche même sans réseau", 13.5, INK); f.text(590, 138, "ni adresse IP : accès de secours.", 13.5, INK)
    f.save(out("m05-console.svg"))


def m05_cli():
    f = Fig(1000, 470, "Une session sur l'OmniSwitch", "Une fenêtre de commandes AOS avec l'invite -> et quatre commandes annotées : system name, show system, write memory, copy working certified.")
    f.title_bar("Une session AOS commentée")
    f.rect(30, 56, 580, 390, "#1e1e1e", "#37474f", 3, 8); f.rect(30, 56, 580, 28, "#37474f", "#37474f", 0, 8)
    f.text(46, 76, "OmniSwitch – console", 13, "#cfd8dc", "start", "700")
    lines = [("-> ", "system name SW-KINE", "#fff59d", "A"), ("-> ", "user admin password Kine#Adm2027", "#fff59d", "B"), ("-> ", "show system", "#fff59d", "C"), ("   Name:        SW-KINE,", "", "#b0bec5", ""),
             ("   Description: Alcatel-Lucent OS6400…", "", "#b0bec5", ""), ("-> ", "write memory", "#fff59d", "D"), ("-> ", "copy working certified", "#fff59d", "E"), ("-> ", "show interfaces status", "#fff59d", "F")]
    for i, (p, c, col, lab) in enumerate(lines):
        y = 116 + i * 40
        f.mono(46, y, p, 14, "#80cbc4", "start", "700"); f.mono(46 + len(p) * 8.6, y, c, 14, col, "start", "700")
        if lab: f.badge(588, y - 5, lab, IND, 12)
    notes = {"A": "Donne un nom au switch", "B": "Remplace le mot de passe d'usine", "C": "Nom, version, durée de marche", "D": "Écrit dans le répertoire working", "E": "Certifie : reprise au redémarrage", "F": "Ports up/down, vitesse"}
    for j, (l, t) in enumerate(notes.items()):
        f.badge(650, 112 + j * 52, l, IND, 12); f.text(672, 117 + j * 52, t, 14, INK, "start", "600", maxw=290)
    f.text(500, 462, "", 1)
    f.save(out("m05-session-aos.svg"))


def m05_repertoires():
    f = Fig(1000, 400, "Working et certified", "Les commandes modifient la configuration en cours en mémoire vive ; write memory l'écrit dans working ; copy working certified la certifie, et elle est relue au démarrage.")
    f.title_bar("Où va ce que tu tapes ? Trois niveaux")
    boxes = [(40, "Configuration\nen cours", "en mémoire vive", "perdue si le switch\nredémarre", ORA, ORA_L), (370, "répertoire\nworking", "enregistré sur le switch", "ta version de travail", IND, IND_L), (700, "répertoire\ncertified", "enregistré, certifié", "relu au démarrage", GRN, GRN_L)]
    for x, t, a, b, c, fl in boxes:
        f.rect(x, 80, 260, 200, fl, c, 3.5, 14); f.text(x + 130, 125, t, 18, c, "middle", "700"); f.text(x + 130, 190, a, 14, INK, "middle", "700"); f.text(x + 130, 232, b, 13.5, MUTED)
    f.arrow(305, 180, 365, 180, LINE, 4); f.arrow(635, 180, 695, 180, LINE, 4)
    f.rect(290, 118, 100, 28, WHITE, LINE, 1.5, 6); f.mono(340, 138, "write memory", 11.5, INK, "middle", "700")
    f.rect(570, 118, 150, 28, WHITE, LINE, 1.5, 6); f.mono(645, 138, "copy working certified", 10.5, INK, "middle", "700")
    f.rect(40, 310, 920, 70, RED_L, RED, 2.5, 10); f.warn(76, 345, 16)
    f.text(520, 336, "Si tu oublies d'enregistrer, une coupure de courant efface tout ton travail.", 15, INK, "middle", "700")
    f.text(520, 360, "Enregistrer et certifier fait partie de l'intervention, pas d'un « plus ».", 14, MUTED)
    f.save(out("m05-working-certified.svg"))


def m06_binaire():
    f = Fig(1000, 440, "Le binaire d'un octet", "Un octet de huit bits avec les valeurs 128, 64, 32, 16, 8, 4, 2, 1 et la façon de retrouver un nombre, puis la table des valeurs d'un masque.")
    f.title_bar("Un octet : 8 cases qui valent 128, 64, 32, 16, 8, 4, 2, 1")
    vals = [128, 64, 32, 16, 8, 4, 2, 1]
    f.text(500, 62, "exemple : 25  =  16 + 8 + 1", 15, INK, "middle", "700")
    for i, v in enumerate(vals):
        x = 70 + i * 107
        on = v in (16, 8, 1)
        f.rect(x, 78, 96, 56, ORA_L if on else GRY, ORA if on else GRY_D, 3, 8); f.text(x + 48, 114, str(v), 24, ORA if on else GRY_D, "middle", "700")
        f.rect(x, 140, 96, 44, ORA if on else WHITE, ORA if on else GRY_D, 2, 8); f.text(x + 48, 172, "1" if on else "0", 26, WHITE if on else GRY_D, "middle", "700")
    f.text(500, 212, "0 0 0 1 1 0 0 1  →  16 + 8 + 1 = 25", 15, MUTED, "middle", "700")
    f.text(500, 252, "Les valeurs possibles d'un octet de MASQUE (les 1 sont toujours à gauche)", 15, IND, "middle", "700")
    ms = [("0", "00000000"), ("128", "10000000"), ("192", "11000000"), ("224", "11100000"), ("240", "11110000"), ("248", "11111000"), ("252", "11111100"), ("254", "11111110"), ("255", "11111111")]
    for i, (v, b) in enumerate(ms):
        x = 40 + i * 104
        f.rect(x, 270, 96, 110, IND_L, IND, 2.5, 10); f.text(x + 48, 308, v, 26, IND, "middle", "700"); f.mono(x + 48, 338, b, 12.5, INK, "middle", "700"); f.text(x + 48, 366, f"{i} bit{'s' if i>1 else ''} à 1", 12.5, MUTED)
    f.rect(40, 395, 920, 34, YEL_L, YEL, 2, 8); f.text(500, 418, "/24 = 255.255.255.0  ·  /25 = 255.255.255.128  ·  /26 = 255.255.255.192  ·  /27 = 255.255.255.224", 13.5, INK, "middle", "700")
    f.save(out("m06-binaire.svg"))


def m06_decoupe():
    f = Fig(1000, 470, "Découper un réseau /24", "Une barre de 256 adresses découpée en deux blocs de 128 (deux /25) puis en quatre blocs de 64 (quatre /26), avec l'adresse de réseau et de diffusion de chaque bloc.")
    f.title_bar("Découper un /24 : on coupe le bloc de 256 en deux, puis en quatre")
    def bar(y, n, label, cols):
        w = 900 / n
        for i in range(n):
            x = 50 + i * w
            f.rect(x, y, w, 60, cols[i % len(cols)][0], cols[i % len(cols)][1], 3, 0)
            start = i * (256 // n); end = start + 256 // n - 1
            f.text(x + w / 2, y + 26, f"{label}", 14, INK, "middle", "700") if False else None
            f.text(x + w / 2, y + 25, f".{start}", 13.5, INK, "middle", "700"); f.text(x + w / 2, y + 45, f"à .{end}", 13, MUTED)
    f.text(500, 66, "192.168.10.0 /24 : 256 adresses, 254 utilisables (réseau = .0, diffusion = .255)", 14.5, INK, "middle", "700")
    bar(76, 1, "", [(IND_L, IND)])
    f.text(500, 164, "→ 2 blocs de 128 : masque /25 (255.255.255.128), 126 adresses utilisables chacun", 14.5, IND, "middle", "700")
    bar(176, 2, "", [(TEAL_L, TEAL), (ORA_L, ORA)])
    f.text(500, 264, "→ 4 blocs de 64 : masque /26 (255.255.255.192), 62 adresses utilisables chacun", 14.5, IND, "middle", "700")
    bar(276, 4, "", [(TEAL_L, TEAL), (ORA_L, ORA), (IND_L, IND), ("#f3e5f5", "#8e24aa")])
    f.rect(50, 360, 900, 90, YEL_L, YEL, 2, 10)
    f.text(500, 386, "Dans chaque bloc : la 1ʳᵉ adresse est celle du RÉSEAU, la dernière est la DIFFUSION, toutes deux inutilisables.", 14, INK, "middle", "700")
    f.text(500, 410, "Exemple, bloc .128 à .191 : réseau .128 · utilisables .129 à .190 · diffusion .191", 14, INK)
    f.text(500, 434, "Taille du bloc = 256 − valeur du masque (192 → 64).", 13.5, MUTED)
    f.save(out("m06-decoupe.svg"))


def m06_plan():
    f = Fig(1000, 380, "Un plan d'adressage visuel", "Le réseau 192.168.10.0/24 représenté en bande : passerelle .1, serveur .5, imprimante .20, borne .30, plage DHCP .100 à .150, libre ensuite.")
    f.title_bar("Plan d'adressage du réseau POSTES : 192.168.10.0 /24")
    x0, w = 50, 900
    def X(n): return x0 + w * n / 256
    f.rect(x0, 110, w, 60, GRY, GRY_D, 3, 4)
    f.rect(X(100), 110, X(151) - X(100), 60, GRN_L, GRN, 3, 0); f.text((X(100) + X(151)) / 2, 148, "plage DHCP", 16, GRN, "middle", "700")
    f.text((X(100) + X(151)) / 2, 90, ".100 à .150", 13.5, GRN, "middle", "700")
    for k, (n, t, c) in enumerate([(1, "passerelle", ORA), (5, "serveur", IND), (20, "imprimante", IND), (30, "borne Wi-Fi", TEAL)]):
        f.rect(X(n) - 3, 100, 7, 80, c, c, 0, 2)
        lx = 130 + k * 190
        f.line(X(n), 180, lx, 236, c, 2)
        f.rect(lx - 80, 236, 160, 50, WHITE, c, 2.5, 8); f.text(lx, 258, t, 14, c, "middle", "700"); f.text(lx, 276, f"192.168.10.{n}", 13, INK, "middle", "700")
    f.text(x0 + 14, 98, ".0 réseau", 12, RED, "start", "700"); f.text(x0 + w, 98, ".255 diffusion", 12, RED, "end", "700")
    f.text(X(210), 148, "libre pour", 14, MUTED, "middle", "700"); f.text(X(210), 166, "l'avenir", 14, MUTED, "middle", "700")
    f.rect(50, 308, 900, 56, YEL_L, YEL, 2, 10)
    f.text(500, 332, "Les adresses FIXES (passerelle, serveur, imprimante, borne) sont HORS de la plage DHCP :", 14, INK, "middle", "700")
    f.text(500, 352, "sinon un poste pourrait recevoir une adresse déjà utilisée (conflit).", 13.5, MUTED)
    f.save(out("m06-plan-adressage.svg"))


def m07_vlan():
    f = Fig(1000, 470, "Un switch coupé en deux VLAN", "Un même switch physique dont les ports 1 à 4 sont en VLAN 10 (postes) et 5 à 8 en VLAN 20 (patients). Les deux groupes ne communiquent pas.")
    f.title_bar("Un seul switch, deux réseaux séparés")
    f.rect(120, 150, 760, 110, GRY, GRY_D, 3, 12); f.text(500, 283, "un seul switch physique", 13.5, MUTED, "middle", "700") if False else f.text(150, 140, "un seul switch physique", 13.5, MUTED, "start", "700")
    f.rect(130, 160, 340, 90, IND_L, IND, 3, 10); f.text(300, 185, "VLAN 10 · POSTES", 15, IND, "middle", "700")
    f.rect(530, 160, 340, 90, ORA_L, ORA, 3, 10); f.text(700, 185, "VLAN 20 · PATIENTS", 15, ORA, "middle", "700")
    for i in range(4):
        f.rect(150 + i * 78, 200, 60, 38, WHITE, IND, 2.5, 4); f.text(180 + i * 78, 225, f"1/{i+1}", 14, IND, "middle", "700")
        f.rect(550 + i * 78, 200, 60, 38, WHITE, ORA, 2.5, 4); f.text(580 + i * 78, 225, f"1/{i+5}", 14, ORA, "middle", "700")
    for i, k in enumerate(["pc", "pc", "printer", "server"]):
        x = 180 + i * 78; f.line(x, 238, x, 318, IND, 2.5); node(f, k, x, 345 if k != "server" else 350)
    for i, k in enumerate(["laptop", "phone", "laptop", "phone"]):
        x = 580 + i * 78; f.line(x, 238, x, 318, ORA, 2.5); node(f, k, x, 345)
    f.rect(470, 175, 60, 60, "#ffffff", RED, 3, 8); f.text(500, 212, "⛔", 0.1, RED)
    f.line(486, 190, 514, 220, RED, 5); f.line(514, 190, 486, 220, RED, 5)
    f.text(500, 150, "pas de communication directe", 13, RED, "middle", "700")
    f.rect(60, 420, 880, 36, YEL_L, YEL, 2, 8); f.text(500, 443, "Les diffusions (broadcast) restent dans leur VLAN. Pour passer de l'un à l'autre : un routeur (niveau 3).", 13.5, INK)
    f.save(out("m07-vlan.svg"))


def m07_broadcast():
    f = Fig(1000, 400, "Avec et sans VLAN : la diffusion", "À gauche sans VLAN la diffusion d'un poste atteint tous les ports. À droite avec deux VLAN elle reste dans son VLAN.")
    f.title_bar("La diffusion (broadcast) : avant et après les VLAN")
    for x0, ttl, vl in [(30, "SANS VLAN : tout le monde reçoit", False), (520, "AVEC VLAN : seul son VLAN reçoit", True)]:
        f.rect(x0, 56, 450, 330, WHITE, GRY_D, 3, 14); f.text(x0 + 225, 88, ttl, 15, IND if vl else RED, "middle", "700")
        f.rect(x0 + 160, 150, 130, 50, TEAL_L, TEAL, 3, 8); f.text(x0 + 225, 181, "switch", 14, TEAL, "middle", "700")
        pos = [(x0 + 60, 120), (x0 + 60, 270), (x0 + 390, 120), (x0 + 390, 270)]
        for i, (x, y) in enumerate(pos):
            c = (IND if i < 2 else ORA) if vl else GRY_D
            f.line(x0 + 225, 200 if y > 200 else 150, x + (22 if x < x0 + 200 else -22), y, c, 2.5)
        for i, (x, y) in enumerate(pos):
            node(f, "pc", x, y)
        f.text(pos[0][0], pos[0][1] + 48, "émetteur", 12.5, INK, "middle", "700")
        f.circle(pos[0][0], pos[0][1] - 2, 36, "none", RED, 3) if False else None
        for i in (1, 2, 3):
            ok = (not vl) or i == 1
            x, y = pos[i]
            f.text(x, y - 48 if y < 200 else y + 52, "reçoit la diffusion" if ok else "ne reçoit rien", 12.5, GRN if ok else RED, "middle", "700")
        if vl:
            f.text(x0 + 60, 360, "VLAN 10", 13, IND, "middle", "700"); f.text(x0 + 390, 360, "VLAN 20", 13, ORA, "middle", "700")
    f.save(out("m07-broadcast.svg"))


def m08_trunk():
    f = Fig(1000, 470, "Le trunk 802.1Q", "Un câble unique entre le switch et la borne Wi-Fi, qui transporte deux VLAN grâce à une étiquette 802.1Q dans chaque trame, et la structure d'une trame étiquetée.")
    f.title_bar("Le trunk : plusieurs VLAN sur un seul câble")
    node(f, "switch", 150, 160, "Switch", "port 1/9"); node(f, "ap", 850, 160, "Borne Wi-Fi", "")
    f.line(195, 160, 805, 160, LINE, 8)
    f.rect(260, 128, 120, 28, IND_L, IND, 2.5, 6); f.text(320, 148, "VLAN 10", 13.5, IND, "middle", "700")
    f.rect(430, 128, 150, 28, ORA_L, ORA, 2.5, 6); f.text(505, 148, "VLAN 20 · étiq. 20", 12.5, ORA, "middle", "700")
    f.rect(620, 128, 120, 28, ORA_L, ORA, 2.5, 6); f.text(680, 148, "VLAN 20", 13.5, ORA, "middle", "700")
    f.text(500, 232, "un seul câble, deux réseaux : chaque trame du VLAN 20 porte une étiquette avec son numéro", 13.5, INK, "middle", "700")
    f.text(500, 258, "Une trame Ethernet ÉTIQUETÉE (802.1Q)", 15, IND, "middle", "700")
    parts = [("MAC\ndestination", 150, GRY, GRY_D), ("MAC\nsource", 150, GRY, GRY_D), ("ÉTIQUETTE 802.1Q\nVLAN = 20", 220, ORA, ORA), ("type", 80, GRY, GRY_D), ("données", 220, IND_L, IND)]
    x = 50
    for t, w, fl, st in parts:
        f.rect(x, 268, w - 4, 70, fl, st, 2.5, 6)
        c = WHITE if fl == ORA else INK
        for j, ln in enumerate(t.split("\n")): f.text(x + (w - 4) / 2, 298 + j * 18, ln, 13, c, "middle", "700")
        x += w
    f.rect(60, 370, 880, 76, YEL_L, YEL, 2, 10)
    f.text(500, 396, "Port d'accès (non étiqueté) : un seul VLAN, l'équipement ignore les VLAN.", 14, INK, "middle", "700")
    f.text(500, 418, "Port trunk (étiqueté) : plusieurs VLAN, chacun marqué de son numéro.", 14, INK, "middle", "700")
    f.text(500, 438, "Un VLAN peut rester non étiqueté sur un trunk : on l'appelle le VLAN natif (ici le VLAN 10).", 13, MUTED)
    f.save(out("m08-trunk.svg"))


def m08_routage():
    f = Fig(1000, 470, "Le switch de niveau 3 route entre VLAN", "Un switch niveau 3 avec deux interfaces IP, une par VLAN, servant de passerelle, et une route par défaut vers la box.")
    f.title_bar("Le switch de niveau 3 : une passerelle par VLAN")
    f.rect(330, 150, 340, 130, TEAL_L, TEAL, 4, 14); f.text(500, 178, "SWITCH NIVEAU 3 (OmniSwitch)", 15, TEAL, "middle", "700")
    f.rect(350, 196, 140, 68, IND_L, IND, 3, 8); f.text(420, 220, "interface VLAN10", 12.5, IND, "middle", "700"); f.mono(420, 244, "192.168.10.1", 13, INK, "middle", "700")
    f.rect(510, 196, 140, 68, ORA_L, ORA, 3, 8); f.text(580, 220, "interface VLAN20", 12.5, ORA, "middle", "700"); f.mono(580, 244, "192.168.20.1", 13, INK, "middle", "700")
    f.arrow(490, 232, 508, 232, LINE, 3); f.arrow(508, 242, 490, 242, LINE, 3)
    f.rect(70, 100, 190, 200, IND_L, IND, 3, 14); f.text(165, 128, "VLAN 10 · POSTES", 14, IND, "middle", "700"); f.text(165, 148, "192.168.10.0/24", 12, MUTED)
    node(f, "pc", 120, 215, "PC", ".101"); node(f, "server", 215, 205, "SRV", ".5")
    f.rect(740, 100, 190, 200, ORA_L, ORA, 3, 14); f.text(835, 128, "VLAN 20 · PATIENTS", 14, ORA, "middle", "700"); f.text(835, 148, "192.168.20.0/24", 12, MUTED)
    node(f, "laptop", 800, 215, "Portable", ".101"); node(f, "phone", 890, 215, "Tél.", ".102")
    f.arrow(262, 230, 345, 230, IND, 3); f.arrow(738, 230, 655, 230, ORA, 3)
    f.text(165, 330, "passerelle des postes : 192.168.10.1", 12.5, IND, "middle", "700"); f.text(835, 330, "passerelle des patients : 192.168.20.1", 12.5, ORA, "middle", "700")
    node(f, "box", 500, 395, "Box", "192.168.100.1"); f.line(500, 360, 500, 282, LINE, 3)
    f.text(560, 328, "route par défaut →", 13, MUTED, "start", "700")
    f.rect(60, 420, 300, 38, WHITE, WHITE, 0, 0)
    f.text(190, 440, "vers tout ce que le switch ne connaît pas : la box", 13, MUTED, "middle", "700", maxw=300) if False else None
    f.save(out("m08-routage-vlan.svg"))


def m08_relais():
    f = Fig(1000, 520, "Le relais DHCP", "Un portable du VLAN 20 envoie un Discover en diffusion, le switch le relaie au serveur DHCP situé dans le VLAN 10, le serveur choisit une adresse dans la plage du VLAN 20.")
    cols = [(130, "Portable (VLAN 20)", "n'a pas d'adresse", ORA), (500, "Switch · relais", "ip helper address", TEAL), (870, "Serveur DHCP (VLAN 10)", "192.168.10.5", IND)]
    msgs = [(0, 1, "①  DISCOVER en diffusion (reste dans le VLAN 20)", ORA, False), (1, 2, "②  Le switch le transmet en direct au serveur, en ajoutant « je viens du réseau 192.168.20.1 »", TEAL, False),
            (2, 1, "③  Le serveur choisit une adresse dans la plage 192.168.20.100–150 : OFFER", IND, False), (1, 0, "④  Le switch rend l'OFFER au portable : il reçoit 192.168.20.101", TEAL, False)]
    f.title_bar("Un serveur DHCP dans un autre VLAN : le relais")
    sequence(f, cols, msgs, top=50, step=72, textsize=13)
    f.rect(40, 450, 920, 54, YEL_L, YEL, 2, 10)
    f.text(500, 474, "Sans relais, la diffusion du portable ne sort jamais du VLAN 20 : le serveur ne la reçoit pas.", 14, INK, "middle", "700")
    f.text(500, 494, "Le portable obtient alors une adresse 169.254.x.x (APIPA).", 13.5, MUTED)
    f.save(out("m08-relais-dhcp.svg"))


if __name__ == "__main__":
    for fn in (m04_couches, m04_encapsulation, m04_arp, m04_mac, m04_echelle, m05_console, m05_cli, m05_repertoires, m06_binaire, m06_decoupe, m06_plan, m07_vlan, m07_broadcast, m08_trunk, m08_routage, m08_relais):
        fn()
    print("ok")
