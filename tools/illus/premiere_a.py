#!/usr/bin/env python3
"""Illustrations Première – S01 à S04."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "premiere"))
out = lambda s, n: os.path.join(ROOT, s, "images", n)


def s01():
    d = "S01-diagnostic-retour"
    f = Fig(980, 520, "La carte de l'année de Première", "Six étapes : comprendre les couches et protocoles, découper et relier, séparer avec les VLAN, héberger des services, protéger, puis le projet A2.")
    f.title_bar("La carte de l'année : six étapes, une brique à la fois")
    etapes = [
        ("1", "Comprendre", "S03–S04", "Les couches, les trames, les protocoles usuels", IND_L, IND),
        ("2", "Découper et relier", "S05–S07", "Switch administrable, sous-réseaux, routeur", TEAL_L, TEAL),
        ("3", "Séparer", "S08–S09", "VLAN et trunk : deux réseaux sur un même switch", ORA_L, ORA),
        ("4", "Héberger", "S10–S12", "Serveur Linux, SSH, DHCP, DNS, web, partage", GRN_L, GRN),
        ("5", "Protéger", "S13–S14", "Cuivre certifié, fibre, sécurité de base", RED_L, RED),
        ("6", "Le projet A2", "S15–S20", "Étude, réalisation, recette, soutenance", YEL_L, "#b28704"),
    ]
    f.line(78, 70, 78, 500, IND_M, 4)
    for i, (n, t, s, txt, fill, st) in enumerate(etapes):
        y = 62 + i * 76
        f.badge(78, y + 30, n, st, 18)
        f.rect(120, y, 820, 62, fill, st, 2.5, 12)
        f.text(145, y + 28, t, 20, st, "start", "700")
        f.text(145, y + 50, txt, 15, INK, "start")
        f.rect(820, y + 14, 100, 34, WHITE, st, 2, 17)
        f.text(870, y + 37, s, 15, st, "middle", "700")
    f.save(out(d, "carte-annee.svg"))

def s02():
    d = "S02-remise-a-niveau-simulateur"
    f = Fig(740, 360, "Adresse et masque", "Avec /24, les trois premiers nombres désignent le réseau et le dernier la machine. Avec /16, les deux premiers désignent le réseau.")
    f.title_bar("Le masque coupe l'adresse en deux : le réseau | la machine")

    def ligne(y, octets, nres, titre, masque):
        f.text(40, y - 14, titre, 17, INK, "start", "700")
        for i, o in enumerate(octets):
            x = 40 + i * 175
            res = i < nres
            f.rect(x, y, 150, 56, IND_L if res else ORA_L, IND if res else ORA, 2.5, 10)
            f.text(x + 75, y + 37, o, 26, IND if res else ORA, "middle", "700")
        # accolades
        x1, x2 = 40, 40 + nres * 175 - 25
        f.line(x1, y + 72, x2, y + 72, IND, 4); f.text((x1 + x2) / 2, y + 98, "RÉSEAU (le même pour tous)", 14, IND, "middle", "700")
        x3, x4 = 40 + nres * 175, 40 + 4 * 175 - 25
        f.line(x3, y + 72, x4, y + 72, ORA, 4); f.text((x3 + x4) / 2, y + 98, "MACHINE (change)", 14, ORA, "middle", "700")
        f.text(700, y - 14, "masque : " + masque, 15, MUTED, "end", "700")

    ligne(80, ["192", "168", "10", "11"], 3, "192.168.10.11 / 24", "255.255.255.0")
    ligne(250, ["172", "16", "5", "200"], 2, "172.16.5.200 / 16", "255.255.0.0")
    f.save(out(d, "adresse-masque.svg"))

def s03():
    d = "S03-couches-wireshark"
    # 1. encapsulation : boîtes imbriquées
    f = Fig(980, 470, "L'encapsulation", "Les données sont placées dans un segment ou message, lui-même placé dans un paquet IP, lui-même placé dans une trame Ethernet.")
    f.title_bar("Encapsulation : des poupées russes")
    cols = [("Trame Ethernet", "couche 2 – liaison", "MAC source et destination", TEAL_L, TEAL, 40, 70, 900, 360),
            ("Paquet IP", "couche 3 – réseau", "IP source et destination, TTL", IND_L, IND, 130, 140, 720, 270),
            ("Segment TCP / UDP / message ICMP", "couche 4 – transport", "ports (ou type ICMP)", ORA_L, ORA, 220, 210, 540, 180),
            ]
    for (t, c, h, fill, st, x, y, w, hh) in cols:
        f.rect(x, y, w, hh, fill, st, 3, 14)
        f.text(x + 20, y + 28, t, 18, st, "start", "700")
        f.text(x + 20, y + 50, c + " : " + h, 14, INK, "start")
    f.rect(310, 290, 360, 70, WHITE, GRN, 3, 12); f.text(490, 322, "Données", 20, GRN, "middle", "700"); f.text(490, 346, "couche 7 – application (HTTP, DNS…)", 13, INK)
    f.save(out(d, "encapsulation.svg"))
    # 2. MAC change, IP reste
    f = Fig(980, 520, "MAC qui changent, IP qui restent", "PC1 envoie un ping vers SRV2 à travers le routeur R1. Sur chaque segment, les adresses MAC changent ; les adresses IP restent les mêmes ; le TTL baisse de 1 au passage du routeur.")
    f.title_bar("Au passage du routeur : les MAC changent, les IP restent")
    ic_pc(f, 140, 80, "PC1", "192.168.10.11"); ic_router(f, 490, 80, "R1", ""); ic_server(f, 840, 80, "SRV2", "192.168.20.100")
    f.line(190, 105, 440, 105, LINE, 3); f.line(540, 105, 790, 105, LINE, 3)
    f.text(315, 94, "segment 1", 13, MUTED, "middle", "700"); f.text(665, 94, "segment 2", 13, MUTED, "middle", "700")
    def trame(x, titre, macs, ttl, col):
        f.rect(x, 200, 400, 250, WHITE, col, 3, 12)
        f.text(x + 200, 232, titre, 18, col, "middle", "700")
        f.rect(x + 16, 248, 368, 74, TEAL_L, TEAL, 2, 8); f.text(x + 28, 272, "Ethernet (MAC)", 15, TEAL, "start", "700")
        f.text(x + 28, 296, macs[0], 14, INK, "start"); f.text(x + 28, 314, macs[1], 14, INK, "start")
        f.rect(x + 16, 332, 368, 74, IND_L, IND, 2, 8); f.text(x + 28, 356, "IP", 15, IND, "start", "700")
        f.text(x + 28, 380, "source 192.168.10.11  →  dest. 192.168.20.100", 14, INK, "start"); f.text(x + 28, 398, ttl, 14, INK, "start", "700")
        f.text(x + 200, 430, "ICMP : demande d'écho (ping)", 13, MUTED)
    trame(60, "Trame sur le segment 1", ("source : MAC de PC1", "destination : MAC de R1 (côté Gi0/0)"), "TTL = 128", TEAL)
    trame(520, "Trame sur le segment 2", ("source : MAC de R1 (côté Gi0/1)", "destination : MAC de SRV2"), "TTL = 127   (−1 au passage de R1)", ORA)
    f.line(260, 150, 260, 198, TEAL, 3); f.line(720, 150, 720, 198, ORA, 3)
    f.save(out(d, "mac-ip-saut.svg"))

def s04():
    d = "S04-protocoles-usuels"
    f = Fig(940, 470, "DHCP : DORA", "Le client diffuse un Discover, le serveur propose une adresse (Offer), le client la demande (Request), le serveur confirme (ACK).")
    f.title_bar("DHCP : les quatre messages « DORA »")
    cols = [(220, "PC (client)", "pas d'adresse : 0.0.0.0", IND), (720, "Serveur DHCP (box)", "192.168.1.1", ORA)]
    sequence(f, cols, [
        (0, 1, "1  DISCOVER : « Y a-t-il un serveur DHCP ? » (diffusion)", IND, False),
        (1, 0, "2  OFFER : « Je te propose 192.168.1.10 »", ORA, True),
        (0, 1, "3  REQUEST : « Je prends 192.168.1.10, merci »", IND, False),
        (1, 0, "4  ACK : « C'est à toi, pour 24 h » (+ masque, passerelle, DNS)", ORA, True)], step=75)
    f.text(470, 440, "Ports : le client écoute sur UDP 68, le serveur sur UDP 67. Messages en diffusion : le client n'a pas encore d'adresse.", 13, MUTED, "middle")
    f.save(out(d, "dora.svg"))
    f = Fig(940, 610, "TCP puis HTTP", "Poignée de main TCP en trois temps (SYN, SYN-ACK, ACK), puis requête HTTP GET, réponse 200 OK, puis fermeture.")
    f.title_bar("Ouvrir une page web : la poignée de main TCP, puis HTTP")
    cols = [(220, "PC (client)", "192.168.1.10 : port 49499", IND), (720, "Serveur web", "198.51.100.80 : port 80", GRN)]
    sequence(f, cols, [
        (0, 1, "SYN  « On se parle ? »", IND, False),
        (1, 0, "SYN-ACK  « Oui, et toi ? »", GRN, True),
        (0, 1, "ACK  « Oui » → connexion ouverte", IND, False),
        (0, 1, "HTTP  GET /  « Donne-moi la page »", IND, False),
        (1, 0, "HTTP  200 OK  + la page web", GRN, True),
        (1, 0, "FIN  « J'ai fini »  (puis ACK du client)", GRN, True)], step=70)
    f.rect(40, 555, 860, 38, GRY, GRY_D, 1.5, 8)
    f.text(470, 580, "Les 3 premiers messages = TCP (transport). GET et 200 OK = HTTP (application).", 14, INK, "middle", "700")
    f.save(out(d, "tcp-http.svg"))

def s05():
    d = "S05-switch-administrable"
    f = Fig(980, 570, "Les modes de la console Cisco", "Quatre modes : utilisateur, privilégié, configuration globale, configuration d'interface. enable monte d'un mode, configure terminal aussi, interface aussi ; exit redescend.")
    f.title_bar("Les modes de la console : on monte, on descend")
    modes = [("SW>", "Mode utilisateur", "regarder un peu (show limité)", GRY, GRY_D),
             ("SW#", "Mode privilégié", "tout regarder (show …), sauvegarder", IND_L, IND),
             ("SW(config)#", "Configuration globale", "nom, mots de passe, routes… (ce qui concerne tout le switch)", TEAL_L, TEAL),
             ("SW(config-if)#", "Configuration d'une interface (ou d'une ligne)", "description, shutdown, VLAN… (un port à la fois)", ORA_L, ORA)]
    for i, (p_, t, txt, fill, st) in enumerate(modes):
        y = 60 + i * 125
        f.rect(170, y, 640, 85, fill, st, 3, 12)
        f.mono(190, y + 34, p_, 20, st, "start", "700")
        f.text(190, y + 60, t, 14, INK, "start", "700", maxw=600); f.text(190, y + 78, txt, 13, INK, "start", maxw=600)
    cmds = ["enable", "configure terminal", "interface fa0/1"]
    for i, c in enumerate(cmds):
        y = 60 + i * 125
        f.arrow(330, y + 88, 330, y + 122, GRN, 4); f.text(345, y + 110, c, 14, GRN, "start", "700", halo=WHITE)
        f.arrow(650, y + 122, 650, y + 88, RED, 4); f.text(665, y + 110, "exit", 14, RED, "start", "700", halo=WHITE)
    f.text(490, 548, "end  (ou Ctrl+Z) : retour direct au mode privilégié", 14, MUTED, "middle", "700")
    f.save(out(d, "modes-cli.svg"))

def s06():
    d = "S06-sous-reseaux"
    # 1. découpage d'un /24 en 4 x /26
    f = Fig(980, 380, "Un /24 découpé en quatre /26", "Le réseau 192.168.1.0/24 (256 adresses) est découpé en quatre sous-réseaux de 64 adresses : .0, .64, .128 et .192.")
    f.title_bar("192.168.1.0 /24  →  quatre sous-réseaux /26")
    f.rect(40, 62, 900, 44, GRY, GRY_D, 2, 8); f.text(490, 91, "le 4ᵉ nombre va de 0 à 255 : 256 adresses", 16, INK, "middle", "700")
    cols = [IND_L, TEAL_L, ORA_L, GRN_L]; sts = [IND, TEAL, ORA, GRN]
    for k in range(4):
        x = 40 + k * 225
        f.rect(x, 130, 225, 150, cols[k], sts[k], 3, 10)
        f.text(x + 112, 160, f"Sous-réseau {chr(65 + k)}", 18, sts[k], "middle", "700")
        f.mono(x + 112, 188, f"192.168.1.{64 * k} /26", 15, INK, "middle", "700")
        f.text(x + 112, 214, f"machines : .{64 * k + 1} à .{64 * k + 62}", 14, INK)
        f.text(x + 112, 236, f"diffusion : .{64 * k + 63}", 14, INK)
        f.text(x + 112, 262, "62 machines", 14, sts[k], "middle", "700")
    for k in range(5):
        f.text(40 + k * 225, 304, str(64 * k), 14, MUTED, "middle", "700")
    f.callout(40, 320, 900, "Chaque sous-réseau a son adresse de réseau (1ère) et sa diffusion (dernière) : 64 − 2 = 62 machines utilisables.", YEL_L, YEL, 14.5)
    f.save(out(d, "decoupage-26.svg"))
    # 2. emprunter des bits
    f = Fig(980, 480, "Emprunter des bits à la partie machine", "Le masque /24 devient /26 : on emprunte les deux premiers bits du dernier octet à la partie machine. Ces deux bits désignent le numéro du sous-réseau.")
    f.title_bar("Du /24 au /26 : on emprunte 2 bits à la partie machine")
    f.text(40, 80, "4ᵉ octet du MASQUE (8 bits) : 1 = fait partie du réseau, 0 = fait partie de la machine", 15, INK, "start", "700")
    def octet(y, nres, titre):
        f.text(40, y - 12, titre, 15, MUTED, "start", "700")
        for i in range(8):
            r = i < nres; x = 40 + i * 70
            f.rect(x, y, 62, 48, IND_L if r else ORA_L, IND if r else ORA, 2.5, 8)
            f.text(x + 31, y + 33, "1" if r else "0", 24, IND if r else ORA, "middle", "700")
        f.text(40 + nres * 35, y + 70, f"{nres} bits empruntés" if nres else "", 14, IND, "middle", "700") if nres else None
        f.text(40 + nres * 70 + (8 - nres) * 35, y + 70, f"{8 - nres} bits machine", 14, ORA, "middle", "700")
    octet(120, 0, "/24 : masque 255.255.255.0 → tout le 4ᵉ octet = machine")
    octet(250, 2, "/26 : masque 255.255.255.192 → 2 bits « sous-réseau » + 6 bits machine")
    f.rect(40 + 0 * 70 - 4, 246, 144, 56, "none", RED, 3, 10)
    f.text(40, 362, "dans l'adresse, ces 2 bits donnent le sous-réseau : 00 = A · 01 = B · 10 = C · 11 = D", 14, RED, "start", "700")
    f.callout(40, 385, 900, "2 bits empruntés → 2² = 4 sous-réseaux. Il reste 6 bits machine → 2⁶ − 2 = 62 machines par sous-réseau. 192 = 128 + 64 = 11000000.", YEL_L, YEL, 14.5)
    f.save(out(d, "emprunt-bits.svg"))


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s01", "s02", "s03", "s04", "s05", "s06"]):
        globals()[w](); print("OK", w)
