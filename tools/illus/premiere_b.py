#!/usr/bin/env python3
"""Illustrations Première – S07 et suivantes."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "premiere"))
out = lambda s, n: os.path.join(ROOT, s, "images", n)


def s07():
    d = "S07-routeur-routage-statique"
    f = Fig(1000, 520, "Aller et retour à travers deux routeurs",
            "PC1 envoie un paquet vers le serveur : R1 puis R2 le font suivre grâce à leurs routes. La réponse refait le chemin inverse : R2 doit aussi connaître le réseau de PC1.")
    f.title_bar("Un paquet va… et la réponse doit revenir")
    X = [110, 360, 640, 890]; Y = 190
    node(f, "pc", X[0], Y, "PC1", "192.168.10.11")
    node(f, "router", X[1], Y, "R1", "gi0/0 .10.1 | gi0/1 10.0.0.1")
    node(f, "router", X[2], Y, "R2", "gi0/1 10.0.0.2 | gi0/0 .20.1")
    node(f, "server", X[3], Y, "SRV1", "192.168.20.100")
    # câbles
    for a, b in ((0, 1), (1, 2), (2, 3)):
        f.line(X[a] + 48, Y, X[b] - 48, Y, GRY_D, 3)
    f.text((X[1] + X[2]) / 2, Y - 12, "10.0.0.0/30", 14, MUTED, "middle", "700")
    # aller
    f.text(500, 80, "ALLER : « je veux joindre 192.168.20.100 »", 16, IND, "middle", "700")
    for a, b, t in ((0, 1, "① passerelle"), (1, 2, "② route statique"), (2, 3, "③ réseau connecté")):
        f.arrow(X[a] + 40, 108, X[b] - 40, 108, IND, 4)
        f.text((X[a] + X[b]) / 2, 128, t, 13, IND, "middle", "600")
    # retour
    f.text(500, 292, "RETOUR : « réponse pour 192.168.10.11 »", 16, ORA, "middle", "700")
    for a, b, t in ((3, 2, "④ passerelle"), (2, 1, "⑤ route statique"), (1, 0, "⑥ réseau connecté")):
        f.arrow(X[a] - 40, 312, X[b] + 40, 312, ORA, 4)
        f.text((X[a] + X[b]) / 2, 334, t, 13, ORA, "middle", "600")
    # tables
    f.rect(70, 360, 420, 130, IND_L, IND, 2, 10)
    f.text(280, 382, "Table de routage de R1", 15, IND, "middle", "700")
    for i, (t, c) in enumerate((("C  192.168.10.0/24   → gi0/0", INK), ("C  10.0.0.0/30        → gi0/1", INK), ("S  192.168.20.0/24   → via 10.0.0.2", RED))):
        f.mono(90, 410 + i * 26, t, 14, c, "start", "700" if c == RED else "400")
    f.rect(510, 360, 420, 130, ORA_L, ORA, 2, 10)
    f.text(720, 382, "Table de routage de R2", 15, ORA, "middle", "700")
    for i, (t, c) in enumerate((("C  192.168.20.0/24   → gi0/0", INK), ("C  10.0.0.0/30        → gi0/1", INK), ("S  192.168.10.0/24   → via 10.0.0.1", RED))):
        f.mono(530, 410 + i * 26, t, 14, c, "start", "700" if c == RED else "400")
    f.text(500, 508, "C = réseau connecté (automatique) · S = route statique (écrite à la main)", 13, MUTED, "middle")
    f.save(out(d, "aller-retour.svg"))

    # --- ce que fait un routeur d'un paquet
    f = Fig(900, 470, "Que fait un routeur d'un paquet ?", "Il lit l'adresse de destination, cherche la route la plus précise dans sa table, puis envoie au prochain routeur ; sans route il rejette.")
    f.title_bar("Ce que fait un routeur de chaque paquet")
    steps = [("1", "Lire l'adresse de destination", "dans l'en-tête IP"), ("2", "Chercher dans la table de routage", "la route la plus précise (masque le plus long)"),]
    x = 60
    for i, (n, t, s) in enumerate(steps):
        y = 60 + i * 95
        f.rect(x, y, 380, 70, IND_L, IND, 2.5, 12); f.badge(x + 28, y + 35, n, IND, 16)
        f.text(x + 56, y + 31, t, 16, IND, "start", "700"); f.text(x + 56, y + 53, s, 13.5, INK, "start")
    f.arrow(250, 130, 250, 155, LINE, 3)
    f.rect(480, 110, 340, 100, YEL_L, YEL, 2.5, 12)
    f.text(650, 142, "Une route correspond-elle ?", 17, INK, "middle", "700")
    f.text(650, 168, "(réseau connecté, statique, par défaut)", 13.5, MUTED, "middle")
    f.arrow(440, 190, 480, 160, LINE, 3)
    # oui
    f.arrow(590, 210, 590, 255, GRN, 3); f.text(608, 238, "oui", 15, GRN, "start", "700")
    f.rect(440, 260, 300, 80, GRN_L, GRN, 2.5, 12)
    f.text(590, 290, "3. Envoyer au prochain saut", 16, GRN, "middle", "700")
    f.text(590, 314, "ou directement (réseau connecté)", 13.5, INK, "middle")
    # non
    f.arrow(780, 210, 780, 348, RED, 3)
    f.text(798, 300, "non", 15, RED, "start", "700")
    f.rect(60, 350, 760, 80, RED_L, RED, 2.5, 12)
    f.text(440, 380, "Sinon : pas de route ⇒ le paquet est jeté", 16, RED, "middle", "700")
    f.text(440, 404, "le routeur répond « destination injoignable » à l'émetteur (message ICMP)", 13.5, INK, "middle")
    f.save(out(d, "decision-routeur.svg"))


def s08():
    d = "S08-vlan-1"
    # --- avant / après
    f = Fig(1000, 470, "Un switch, deux réseaux séparés avec les VLAN",
            "À gauche, tous les postes sont dans le même réseau de diffusion. À droite, les VLAN 10 et 20 découpent le même switch en deux réseaux qui ne se voient plus.")
    f.title_bar("Les VLAN : un seul boîtier, plusieurs réseaux séparés")
    for ox, titre, sep in ((20, "SANS VLAN : tout le monde se voit", False), (520, "AVEC VLAN : Direction | Atelier", True)):
        f.rect(ox, 55, 460, 395, WHITE, GRY_D, 2, 14, dash="6 5")
        f.text(ox + 230, 85, titre, 17, RED if not sep else GRN, "middle", "700")
        cx = ox + 230
        f.rect(cx - 170, 220, 340, 50, TEAL_L, TEAL, 3, 8)
        f.text(cx, 247, "SWITCH", 15, TEAL, "middle", "700")
        cols = [(IND, IND_L, "Direction"), (IND, IND_L, "Direction"), (ORA, ORA_L, "Atelier"), (ORA, ORA_L, "Atelier")]
        xs = [cx - 135, cx - 45, cx + 45, cx + 135]
        for i, x in enumerate(xs):
            c, cl, lab = cols[i]
            col, colL = (c, cl) if sep else (GRY_D, GRY)
            f.rect(x - 22 + 0, 262 - 0, 0, 0)
            f.line(x, 270, x, 330, col, 3)
            f.rect(x - 28, 330, 56, 38, colL, col, 3, 6)
            f.text(x, 354, f"PC{i+1}", 14, col, "middle", "700")
            f.text(x, 392, lab, 13, col, "middle", "600")
            f.rect(x - 7, 258, 14, 12, col, col, 1, 2)
        if sep:
            f.rect(cx - 90, 135, 80, 36, IND_L, IND, 2.5, 8); f.text(cx - 50, 159, "VLAN 10", 14, IND, "middle", "700")
            f.rect(cx + 10, 135, 80, 36, ORA_L, ORA, 2.5, 8); f.text(cx + 50, 159, "VLAN 20", 14, ORA, "middle", "700")
            f.line(cx - 50, 171, xs[0], 256, IND, 2, "4 4"); f.line(cx - 50, 171, xs[1], 256, IND, 2, "4 4")
            f.line(cx + 50, 171, xs[2], 256, ORA, 2, "4 4"); f.line(cx + 50, 171, xs[3], 256, ORA, 2, "4 4")
            f.text(cx, 118, "deux « switchs virtuels » dans un boîtier", 14, MUTED, "middle")
            f.text(cx, 432, "Un message de diffusion de PC1 n'atteint pas PC3 ni PC4", 14, GRN, "middle", "700")
        else:
            f.text(cx, 160, "un seul réseau de diffusion", 15, RED, "middle", "700")
            f.text(cx, 182, "(un broadcast arrive chez tous les postes)", 13.5, MUTED, "middle")
            f.text(cx, 432, "L'atelier voit les postes de la Direction", 14, RED, "middle", "700")
    f.save(out(d, "vlan-principe.svg"))

    # --- ports du switch
    f = Fig(1000, 400, "Affectation des ports aux VLAN", "Sur le switch, les ports Fa0/1 et Fa0/2 sont dans le VLAN 10, Fa0/3 et Fa0/4 dans le VLAN 20, les autres restent dans le VLAN 1.")
    f.title_bar("Chaque port appartient à UN VLAN (mode « access »)")
    f.rect(40, 70, 920, 110, TEAL_L, TEAL, 3, 10)
    f.text(60, 95, "Switch Catalyst 2960 – face avant", 14, TEAL, "start", "700")
    for i in range(12):
        x = 70 + i * 72
        vl = 10 if i < 2 else 20 if i < 4 else 1
        c, cl = (IND, IND_L) if vl == 10 else (ORA, ORA_L) if vl == 20 else (GRY_D, GRY)
        f.rect(x, 115, 56, 44, cl, c, 2.5, 5)
        f.text(x + 28, 133, f"Fa0/{i+1}", 12.5, c, "middle", "700")
        f.text(x + 28, 150, f"VLAN {vl}", 12, c, "middle", "600")
    f.text(70 + 12 * 72 + 4, 140, "…", 20, MUTED, "start", "700")
    f.rect(40, 215, 920, 160, WHITE, LINE, 2, 10)
    f.text(60, 240, "SW1# show vlan brief", 15, INK, "start", "700", family="monospace")
    rows = [("VLAN", "Nom", "Ports"), ("1", "default", "Fa0/5 … Fa0/24, Gi0/1, Gi0/2"), ("10", "DIRECTION", "Fa0/1, Fa0/2"), ("20", "ATELIER", "Fa0/3, Fa0/4")]
    for i, (a, b, c_) in enumerate(rows):
        y = 272 + i * 28
        col = INK if i == 0 else IND if a == "10" else ORA if a == "20" else MUTED
        w = "700" if i == 0 else "400"
        f.mono(70, y, a, 15, col, "start", w); f.mono(150, y, b, 15, col, "start", w); f.mono(380, y, c_, 15, col, "start", w)
    f.line(60, 280, 940, 280, GRY_D, 1)
    f.save(out(d, "ports-vlan.svg"))


def s09():
    d = "S09-vlan-2-trunk"
    f = Fig(1000, 470, "Un trunk transporte plusieurs VLAN sur un seul câble",
            "Deux switchs reliés par un seul câble trunk. Les trames des VLAN 10 et 20 y circulent avec une étiquette indiquant leur VLAN.")
    f.title_bar("Un seul câble, plusieurs VLAN : le trunk")
    S1, S2, Y = 270, 730, 230
    for x, n in ((S1, "SW1 – bâtiment A"), (S2, "SW2 – bâtiment B")):
        f.rect(x - 90, Y - 28, 180, 56, TEAL_L, TEAL, 3, 10); f.text(x, Y + 6, n, 15, TEAL, "middle", "700")
    # PCs
    for x, side in ((S1, -1), (S2, 1)):
        px = x + side * 230
        node(f, "pc", px, 120, "Direction" , "VLAN 10", c=IND); node(f, "pc", px, 330, "Atelier", "VLAN 20", c=ORA)
        f.line(px - side * 35, 120, x - side * 60, Y - 28, IND, 3)
        f.line(px - side * 35, 330, x - side * 60, Y + 28, ORA, 3)
    # trunk
    f.rect(S1 + 90, Y - 14, S2 - S1 - 180, 28, GRY, LINE, 3, 6)
    f.text((S1 + S2) / 2, Y + 6, "TRUNK (802.1Q)", 15, INK, "middle", "700")
    f.rect(S1 + 100, Y - 80, 130, 36, IND_L, IND, 2.5, 8); f.text(S1 + 165, Y - 57, "[VLAN 10] trame", 12.5, IND, "middle", "700")
    f.rect(S2 - 230, Y - 80, 130, 36, IND_L, IND, 2.5, 8); f.text(S2 - 165, Y - 57, "[VLAN 10] trame", 12.5, IND, "middle", "700")
    f.rect(S1 + 100, Y + 44, 130, 36, ORA_L, ORA, 2.5, 8); f.text(S1 + 165, Y + 67, "[VLAN 20] trame", 12.5, ORA, "middle", "700")
    f.rect(S2 - 230, Y + 44, 130, 36, ORA_L, ORA, 2.5, 8); f.text(S2 - 165, Y + 67, "[VLAN 20] trame", 12.5, ORA, "middle", "700")
    f.text(500, Y - 100, "Chaque trame porte une étiquette (VLAN ID)", 15, INK, "middle", "700")
    f.callout(70, 400, 860, "Sur le trunk, la trame est « étiquetée » (4 octets ajoutés : le VLAN ID). Le switch d'arrivée lit l'étiquette, l'enlève et envoie la trame seulement aux ports de ce VLAN.", YEL_L, YEL, 14.5)
    f.save(out(d, "trunk-principe.svg"))


def s10():
    d = "S10-serveur-linux-ssh"
    f = Fig(1000, 560, "Ce qui se passe quand on tape ssh", "Le client ouvre une connexion TCP vers le port 22 du serveur, vérifie l'empreinte du serveur, puis s'authentifie par mot de passe ou par clé, et obtient un terminal chiffré.")
    f.title_bar("Se connecter en SSH : les 4 étapes")
    cols = [(240, "Poste admin (client)", "ssh eleve@192.168.20.100", IND), (760, "Serveur Linux", "openssh-server – port 22", ORA)]
    msgs = [(0, 1, "① connexion TCP vers le port 22", IND, False),
            (1, 0, "② empreinte du serveur (clé d'hôte)", ORA, True),
            (0, 1, "③ identifiant + mot de passe (ou clé)", IND, False),
            (1, 0, "④ accès accordé : terminal chiffré", GRN, True)]
    b = sequence(f, cols, msgs, top=50, step=62)
    f.callout(60, b + 30, 880, "1re connexion : le client demande « Are you sure you want to continue connecting (yes/no) ? » : il mémorise l'empreinte dans known_hosts. Si elle change plus tard, SSH alerte : le serveur a été réinstallé… ou quelqu'un se fait passer pour lui.", YEL_L, YEL, 14.5)
    f.save(out(d, "ssh-etapes.svg"))

    f = Fig(1000, 470, "L'arborescence Linux", "Tout part de la racine /. Les dossiers importants pour l'administrateur : /etc pour la configuration, /var/log pour les journaux, /home pour les utilisateurs.")
    f.title_bar("Linux : tout part de la racine « / »")
    f.rect(430, 55, 140, 46, IND_L, IND, 3, 10); f.text(500, 85, "/", 22, IND, "middle", "700")
    dirs = [("/etc", "configuration", ORA_L, ORA, "netplan/ ssh/ hostname"), ("/home", "dossiers des utilisateurs", GRN_L, GRN, "eleve/ admin/"),
            ("/var/log", "journaux", RED_L, RED, "auth.log syslog"), ("/usr/bin", "programmes", TEAL_L, TEAL, "ls cat ssh"), ("/tmp", "fichiers temporaires", GRY, GRY_D, "effacé au redémarrage")]
    for i, (n, role, fill, st, ex) in enumerate(dirs):
        x = 40 + i * 190; y = 190
        f.line(500, 101, x + 80, y, GRY_D, 2.5)
        f.rect(x, y, 160, 150, fill, st, 2.5, 12)
        f.text(x + 80, y + 32, n, 18, st, "middle", "700")
        f.text(x + 80, y + 62, role, 13.5, INK, "middle", maxw=140)
        f.mono(x + 80, y + 118, ex, 12, MUTED, "middle")
    f.callout(40, 375, 920, "Chemin absolu : il commence par « / » (ex. /etc/ssh/sshd_config). Chemin relatif : à partir de là où l'on est (pwd). « ~ » = ton dossier personnel.", YEL_L, YEL, 14.5)
    f.save(out(d, "arborescence.svg"))


def s11():
    d = "S11-dhcp-dns-serveur"
    f = Fig(1000, 440, "Plan d'adresses du réseau 192.168.10.0/24", "La plage dynamique du DHCP (50 à 150) est séparée des adresses fixes (routeur, serveur, imprimante) pour éviter les doublons.")
    f.title_bar("Un plan d'adresses : fixes d'un côté, DHCP de l'autre")
    x0, w = 40, 920
    segs = [(0, 49, "Adresses FIXES\n.1 routeur · .2 serveur · .30 imprimante", GRY, GRY_D, "exclues du DHCP"), (50, 150, "POOL DHCP\n192.168.10.50 → .150", GRN_L, GRN, "101 adresses distribuées"), (151, 254, "Libre / réserve", YEL_L, YEL, "pour l'avenir")]
    for a, b, lab, fill, st, sub in segs:
        xa = x0 + a / 256 * w; xb = x0 + (b + 1) / 256 * w
        f.rect(xa, 100, xb - xa, 90, fill, st, 3, 6)
        l1, _, l2 = lab.partition("\n")
        f.text((xa + xb) / 2, 135, l1, 17, st if st != YEL else "#8a6d00", "middle", "700")
        if l2: f.text((xa + xb) / 2, 160, l2, 12.5, INK, "middle", maxw=xb - xa - 8)
        f.text((xa + xb) / 2, 215, sub, 13.5, MUTED, "middle")
    for v in (0, 50, 150, 255):
        x = x0 + v / 256 * w
        f.line(x, 190, x, 200, LINE, 2); f.text(x, 238, f".{v}", 14, INK, "middle", "700")
    f.text(500, 82, "dernier octet de l'adresse (0 à 255)", 14, MUTED, "middle")
    f.rect(40, 280, 440, 130, IND_L, IND, 2.5, 12)
    f.text(260, 308, "Ce que le serveur DHCP remet au poste", 16, IND, "middle", "700")
    for i, t in enumerate(("① une adresse IP (dans le pool)", "② le masque (255.255.255.0)", "③ la passerelle (192.168.10.1)", "④ le serveur DNS (192.168.10.2)")):
        f.text(62, 336 + i * 20, t, 14, INK, "start")
    f.rect(520, 280, 440, 130, ORA_L, ORA, 2.5, 12)
    f.text(740, 308, "Le bail (lease)", 16, ORA, "middle", "700")
    f.text(540, 336, "L'adresse est PRÊTÉE pour une durée (ex. 8 h).", 14, INK, "start")
    f.text(540, 358, "À la moitié du bail, le poste demande à renouveler.", 14, INK, "start")
    f.text(540, 380, "Poste éteint : l'adresse retourne dans le pool.", 14, INK, "start")
    f.save(out(d, "plan-adresses.svg"))

    f = Fig(1000, 420, "Résolution d'un nom par le serveur DNS local", "Le poste demande l'adresse de intranet.mecapro.local à son serveur DNS ; le serveur répond avec l'adresse trouvée dans sa zone.")
    f.title_bar("Le DNS : l'annuaire qui traduit un nom en adresse")
    node(f, "pc", 130, 160, "Poste", "DHCP : 192.168.10.50")
    node(f, "server", 500, 160, "SRV1 – DNS", "192.168.10.2")
    f.rect(740, 70, 230, 175, WHITE, ORA, 2.5, 12)
    f.text(855, 96, "Zone mecapro.local", 15, ORA, "middle", "700")
    for i, (n, a) in enumerate((("srv", "192.168.10.2"), ("intranet", "192.168.10.2"), ("imprimante", "192.168.10.30"))):
        f.mono(755, 128 + i * 32, f"{n:<11}A  {a}", 12.5, INK, "start")
    f.line(540, 160, 740, 160, ORA, 2, "4 4")
    f.arrow(200, 120, 440, 120, IND, 4); f.text(320, 108, "« intranet.mecapro.local ? »", 14, IND, "middle", "700")
    f.arrow(440, 200, 200, 200, GRN, 4); f.text(320, 224, "« c'est 192.168.10.2 »", 14, GRN, "middle", "700")
    f.callout(40, 290, 920, "Le poste connaît l'adresse de son serveur DNS parce que le DHCP la lui a remise (④). Si ce DNS est faux : les adresses IP marchent, mais PAS les noms.", YEL_L, YEL, 14.5)
    f.text(500, 385, "Test : nslookup nom  →  la réponse doit donner la bonne adresse", 14, MUTED, "middle")
    f.save(out(d, "dns-resolution.svg"))


def s12():
    d = "S12-web-partage"
    f = Fig(1000, 430, "HTTP et HTTPS vus par un espion sur le réseau", "En HTTP, le contenu de la page est lisible par quiconque capture les trames. En HTTPS, il est chiffré : seul le serveur et le navigateur le lisent.")
    f.title_bar("HTTP en clair, HTTPS chiffré : ce que voit un espion")
    for ox, titre, col, colL, lines, verdict in (
        (30, "HTTP (port 80)", RED, RED_L, ["GET /direction.html HTTP/1.1", "Host: intranet.mecapro.local", "", "<h1>Espace Direction</h1>", "salaires : …"], "Tout est lisible"),
        (520, "HTTPS (port 443)", GRN, GRN_L, ["16 03 03 02 ac 01 00 02", "a8 03 03 5f 3a 91 d0 7c", "e4 af 57 a9 00 86 2e 16", "6c 63 99 fa e3 4f ba e6", "bc 21 6d 09 6d 33 96 f2"], "Illisible sans la clé")):
        f.rect(ox, 60, 450, 300, colL, col, 3, 14)
        f.text(ox + 225, 92, titre, 19, col, "middle", "700")
        f.rect(ox + 25, 110, 400, 170, WHITE, col, 2, 8)
        for i, l in enumerate(lines):
            f.mono(ox + 40, 142 + i * 28, l, 14, INK, "start")
        f.text(ox + 225, 320, verdict, 18, col, "middle", "700")
        f.text(ox + 225, 345, "(ce qu'on voit dans l'analyseur de trames)", 13, MUTED, "middle")
    f.text(500, 405, "Le cadenas du navigateur = HTTPS : la page ET les mots de passe sont protégés pendant le trajet.", 14.5, INK, "middle", "700")
    f.save(out(d, "http-https.svg"))

    f = Fig(1000, 470, "Partage de fichiers : groupes et droits", "Deux dossiers partagés, un par service. Le groupe Direction lit et écrit dans son dossier mais n'a aucun accès à celui de l'Atelier, et réciproquement.")
    f.title_bar("Un partage = des dossiers + des groupes + des droits")
    node(f, "user", 70, 95, "alice", None, c=IND); node(f, "user", 70, 200, "bob", None, c=IND); node(f, "user", 70, 335, "carl", None, c=ORA)
    f.rect(190, 125, 130, 44, IND_L, IND, 2.5, 22); f.text(255, 153, "Direction", 16, IND, "middle", "700")
    f.rect(190, 313, 130, 44, ORA_L, ORA, 2.5, 22); f.text(255, 341, "Atelier", 16, ORA, "middle", "700")
    f.line(108, 100, 190, 140, IND, 3); f.line(108, 205, 190, 158, IND, 3); f.line(108, 340, 190, 335, ORA, 3)
    f.text(255, 112, "groupe", 12.5, MUTED, "middle"); f.text(255, 300, "groupe", 12.5, MUTED, "middle")
    f.rect(620, 90, 330, 100, IND_L, IND, 3, 12); f.text(785, 120, "\\\\SRV\\direction", 17, IND, "middle", "700"); f.text(785, 148, "groupe Direction : lecture + écriture", 13.5, INK, "middle"); f.text(785, 170, "autres : aucun accès", 13.5, RED, "middle", "700")
    f.rect(620, 290, 330, 100, ORA_L, ORA, 3, 12); f.text(785, 320, "\\\\SRV\\atelier", 17, ORA, "middle", "700"); f.text(785, 348, "groupe Atelier : lecture + écriture", 13.5, INK, "middle"); f.text(785, 370, "autres : aucun accès", 13.5, RED, "middle", "700")
    f.arrow(320, 147, 610, 140, GRN, 4); f.text(465, 125, "accès autorisé", 13.5, GRN, "middle", "700")
    f.arrow(320, 335, 610, 340, GRN, 4); f.text(465, 365, "accès autorisé", 13.5, GRN, "middle", "700")
    f.line(320, 318, 625, 195, RED, 3, "6 5"); f.check(470, 257, False, 26); f.text(540, 285, "accès refusé", 13.5, RED, "middle", "700")
    f.callout(40, 415, 920, "Principe : on donne les droits à des GROUPES, jamais personne par personne. Un nouvel arrivant dans la Direction = on l'ajoute au groupe, et c'est tout.", YEL_L, YEL, 14.5)
    f.save(out(d, "partage-droits.svg"))


T568B = [("blanc-orange", "#ffffff", "#ef6c00"), ("orange", "#ef6c00", None), ("blanc-vert", "#ffffff", "#2e7d32"), ("bleu", "#1e88e5", None),
         ("blanc-bleu", "#ffffff", "#1e88e5"), ("vert", "#2e7d32", None), ("blanc-marron", "#ffffff", "#795548"), ("marron", "#795548", None)]


def wire(f, x, y, i, w=26, h=34):
    n, c1, c2 = T568B[i]
    f.rect(x, y, w, h, c1, INK, 1.5, 3)
    if c2:
        f.rect(x + 1.5, y + h * 0.3, w - 3, h * 0.4, c2, c2, 0, 1)


def s13():
    d = "S13-cuivre-fibre-securite"
    # --- 1. cartographie des paires
    f = Fig(1000, 540, "La cartographie des paires (wiremap)", "Le testeur vérifie que chacune des 8 broches d'un côté arrive sur la même broche de l'autre côté. Exemples de défauts : coupure, paires inversées, croisement de paires.")
    f.title_bar("Cartographie des paires : ce que vérifie le testeur")
    cas = [("Câble correct", "1→1  2→2  3→3 … 8→8", GRN, [1, 2, 3, 4, 5, 6, 7, 8], "OK"),
           ("Coupure (fil 5)", "la broche 5 n'arrive nulle part", RED, [1, 2, 3, 4, None, 6, 7, 8], "ÉCHEC"),
           ("Paire inversée", "les broches 1 et 2 sont permutées", RED, [2, 1, 3, 4, 5, 6, 7, 8], "ÉCHEC"),
           ("Câble croisé", "paires 2 et 3 permutées (1↔3, 2↔6)", ORA, [3, 6, 1, 4, 5, 2, 7, 8], "croisé")]
    for r, (t, sub, col, mp, verdict) in enumerate(cas):
        y = 62 + r * 118
        f.rect(30, y, 940, 104, WHITE, col, 2.5, 12)
        f.text(50, y + 28, t, 17, col, "start", "700"); f.text(50, y + 52, sub, 13.5, INK, "start")
        f.rect(50, y + 66, 110, 26, col, col, 0, 13); f.text(105, y + 85, verdict, 14, WHITE, "middle", "700")
        x0 = 360
        for i in range(8):
            x = x0 + i * 62
            f.text(x + 13, y + 26, str(i + 1), 13, MUTED, "middle", "700")
            f.text(x + 13, y + 100, str(i + 1), 13, MUTED, "middle", "700")
            wire(f, x, y + 32, i, 26, 14)
            wire(f, x, y + 66, i, 26, 14)
            if mp[i] is None:
                f.line(x + 13, y + 46, x + 13, y + 66, RED, 2, "3 3"); f.line(x + 5, y + 52, x + 21, y + 60, RED, 3)
            else:
                f.line(x + 13, y + 46, x0 + (mp[i] - 1) * 62 + 13, y + 66, col, 2)
        f.text(330, y + 44, "côté A", 12, MUTED, "end"); f.text(330, y + 80, "côté B", 12, MUTED, "end")
    f.save(out(d, "wiremap.svg"))

    # --- 2. rapport de test
    f = Fig(1000, 470, "Lire un rapport de test cuivre", "Trois liaisons testées : la A est conforme, la B dépasse la longueur maximale du lien permanent (90 m), la C a une paire inversée.")
    f.title_bar("Un rapport de test : trois liaisons, trois verdicts")
    cols = ["Liaison", "Longueur", "Cartographie", "Atténuation", "Diaphonie (NEXT)", "Résultat"]
    xs = [40, 170, 300, 470, 640, 840]
    f.rect(30, 60, 940, 40, IND, IND, 0, 6)
    for x, c in zip(xs, cols):
        f.text(x, 86, c, 14.5, WHITE, "start", "700")
    rows = [("A  bureau 12", "62 m", "OK", "OK (marge 6,1 dB)", "OK (marge 8,4 dB)", "RÉUSSI", GRN),
            ("B  atelier 03", "103 m", "OK", "ÉCHEC (−2,0 dB)", "OK (marge 3,0 dB)", "ÉCHEC", RED),
            ("C  accueil 01", "34 m", "Paire 1-2 inversée", "—", "—", "ÉCHEC", RED)]
    for i, row in enumerate(rows):
        y = 100 + i * 52
        f.rect(30, y, 940, 52, GRN_L if row[6] == GRN else RED_L, GRY_D, 1, 0)
        for j, (x, v) in enumerate(zip(xs, row[:6])):
            f.text(x, y + 32, v, 14, row[6] if j == 5 else INK, "start", "700" if j in (0, 5) else "400")
    f.text(40, 290, "À savoir : limite du lien permanent = 90 m ; avec les 2 cordons de brassage (5 m chacun) : canal = 100 m.", 14.5, INK, "start", "700")
    f.callout(40, 310, 920, "B : 103 m > 90 m : le câble est trop long, d'où l'atténuation hors limite. Remède : raccourcir le trajet, ou ajouter un brassage intermédiaire (un switch) près du poste, ou passer en fibre.", RED_L, RED, 14.5)
    f.callout(40, 375, 920, "C : une paire inversée (broches 1 et 2) se corrige en ré-sertissant / re-poinçonnant la prise. Le câble fait pourtant passer le courant : seul un testeur de cartographie le voit.", YEL_L, YEL, 14.5)
    f.save(out(d, "rapport-test.svg"))

    # --- 3. fibre
    f = Fig(1000, 520, "Fibre monomode et multimode", "En monomode le cœur de 9 µm ne laisse passer qu'un seul chemin à la lumière, ce qui permet de grandes distances. En multimode, le cœur de 50 µm laisse passer plusieurs chemins : distance limitée.")
    f.title_bar("Fibre optique : monomode (OS2) ou multimode (OM3/OM4) ?")
    for ox, titre, col, colL, core, rays, rows in (
        (30, "MONOMODE (OS2) – gaine jaune", "#b28704", YEL_L, 9, 1, ["cœur 9 µm", "1 seul chemin de lumière", "laser 1310 / 1550 nm", "de 2 km à plus de 10 km", "ex. 1000BASE-LX, 10GBASE-LR"]),
        (520, "MULTIMODE (OM3/OM4) – gaine aqua", TEAL, TEAL_L, 50, 3, ["cœur 50 µm", "plusieurs chemins de lumière", "VCSEL 850 nm", "jusqu'à 300 – 400 m en 10 G", "ex. 1000BASE-SX, 10GBASE-SR"])):
        f.rect(ox, 55, 450, 330, colL, col, 3, 14)
        f.text(ox + 225, 85, titre, 16.5, col, "middle", "700")
        h = 18 + core * 1.2
        f.rect(ox + 25, 118, 400, 90, WHITE, GRY_D, 2, 4)           # gaine
        f.rect(ox + 25, 163 - h / 2, 400, h, col, col, 0, 2, op=.35)  # coeur
        f.text(ox + 225, 110, "coupe d'une fibre : gaine de 125 µm (cadre), cœur coloré", 12, MUTED, "middle")
        for k in range(rays):
            yy = 163 + (k - (rays - 1) / 2) * (h / 4)
            f.path(f"M{ox+30},{yy:.0f} L{ox+130},{yy+ (k-(rays-1)/2)*h*0.25:.0f} L{ox+230},{yy - (k-(rays-1)/2)*h*0.25:.0f} L{ox+330},{yy + (k-(rays-1)/2)*h*0.25:.0f} L{ox+420},{yy:.0f}", "none", RED, 2.5)
        for i, t in enumerate(rows):
            f.text(ox + 30, 245 + i * 28, "• " + t, 14.5, INK, "start", "700" if i == 0 else "400")
    f.rect(30, 400, 940, 100, WHITE, GRY_D, 2, 10)
    f.text(50, 428, "Connecteurs usuels :  LC (petit, 2 fibres, le plus courant sur les SFP) · SC (carré, à clic) · ST (à baïonnette, anciens)", 14, INK, "start", "700")
    f.text(50, 456, "Jarretière duplex : une fibre pour émettre, une pour recevoir (attention à ne pas inverser Tx/Rx).", 14, INK, "start")
    f.text(50, 482, "Propreté : on nettoie TOUJOURS les extrémités avant de brancher ; un grain de poussière peut couper la liaison.", 14, RED, "start", "700")
    f.save(out(d, "fibre.svg"))

    # --- 4. bilan optique
    f = Fig(1000, 400, "Bilan de liaison optique", "Le bilan additionne les pertes de la fibre, des connecteurs et des soudures ; il doit rester inférieur à la perte maximale admise par l'émetteur.")
    f.title_bar("Bilan de liaison : on additionne les pertes en dB")
    node(f, "switch", 90, 150, "Switch A", None)
    node(f, "switch", 910, 150, "Switch B", None)
    f.line(140, 150, 860, 150, "#b28704", 5)
    for x, lab in ((200, "connecteur\n0,5 dB"), (500, "soudure\n0,1 dB"), (800, "connecteur\n0,5 dB")):
        f.circle(x, 150, 9, WHITE, RED, 3)
        l1, l2 = lab.split("\n"); f.text(x, 116, l1, 13, RED, "middle", "700"); f.text(x, 100, l2, 13, RED, "middle", "700")
    f.text(350, 185, "fibre 2 km × 0,4 dB/km = 0,8 dB", 14, "#8a6d00", "middle", "700")
    f.rect(40, 230, 920, 130, YEL_L, YEL, 2.5, 12)
    f.text(60, 262, "Perte totale = 0,8 + 0,5 + 0,1 + 0,5 = 1,9 dB", 17, INK, "start", "700")
    f.text(60, 292, "Perte maximale admise par l'émetteur (exemple 1000BASE-LX) : environ 6 dB", 14.5, INK, "start")
    f.text(60, 322, "1,9 dB < 6 dB  ⇒  marge de 4,1 dB : la liaison est conforme", 15.5, GRN, "start", "700")
    f.text(60, 348, "(Valeurs usuelles d'exercice : à vérifier avec la fiche technique des composants utilisés.)", 12.5, MUTED, "start")
    f.save(out(d, "bilan-optique.svg"))


def s14():
    d = "S14-securite-base"
    f = Fig(1000, 480, "La sécurité par couches", "Plusieurs barrières successives : accès physique, réseau, équipements, systèmes et utilisateurs. Si une barrière cède, la suivante protège encore.")
    f.title_bar("Défense en profondeur : plusieurs barrières, pas une seule")
    couches = [("Utilisateurs", "sensibilisation, mots de passe longs, pas de partage de compte", RED_L, RED),
               ("Systèmes", "mises à jour, pare-feu du poste, services inutiles coupés", ORA_L, ORA),
               ("Équipements réseau", "mots de passe forts, SSH (pas Telnet), ports libres coupés, sauvegarde", YEL_L, "#b28704"),
               ("Réseau", "VLAN, filtrage (ACL) entre les zones, Wi-Fi invités séparé", GRN_L, GRN),
               ("Accès physique", "local technique et baie fermés à clé, badge, caméra", IND_L, IND)]
    for i, (t, sub, fill, st) in enumerate(couches):
        w = 900 - i * 80; x = 50 + i * 40; y = 60 + i * 76
        f.rect(x, y, w, 66, fill, st, 3, 14)
        f.text(x + 22, y + 28, t, 18, st, "start", "700")
        f.text(x + 22, y + 52, sub, 14, INK, "start")
    f.save(out(d, "defense-profondeur.svg"))

    f = Fig(1000, 470, "Comment le routeur lit une liste de filtrage (ACL)", "Le routeur compare chaque paquet aux règles de haut en bas ; la première règle qui correspond s'applique, puis il s'arrête. Une règle « refuser tout » termine la liste.")
    f.title_bar("Une ACL se lit de haut en bas : la 1re règle qui correspond gagne")
    rules = [("10", "permit", "tcp  192.168.10.0/24  →  192.168.20.100  port 80", GRN, GRN_L), ("20", "permit", "tcp  192.168.10.0/24  →  192.168.20.100  port 443", GRN, GRN_L), ("30", "deny", "ip  tout  →  tout", RED, RED_L)]
    f.text(40, 70, "Liste « WEB-ONLY » appliquée en entrée sur l'interface côté postes", 15, INK, "start", "700")
    for i, (n, act, txt, c, cl) in enumerate(rules):
        y = 90 + i * 60
        f.rect(40, y, 560, 48, cl, c, 2.5, 8)
        f.badge(70, y + 24, n, c, 15); f.text(100, y + 31, act, 17, c, "start", "700"); f.mono(190, y + 30, txt, 13, INK, "start")
    f.text(40, 290, "Tests depuis un poste du réseau 192.168.10.0/24 :", 15, INK, "start", "700")
    tests = [("Navigateur vers le serveur (port 80)", "→ règle 10", "AUTORISÉ", GRN), ("Ping vers le serveur (ICMP)", "→ règle 30", "REFUSÉ", RED), ("Accès SSH vers le serveur (port 22)", "→ règle 30", "REFUSÉ", RED)]
    for i, (t, r, v, c) in enumerate(tests):
        y = 305 + i * 44
        f.text(60, y + 28, t, 14.5, INK, "start"); f.text(420, y + 28, r, 14, MUTED, "start", "700")
        f.rect(520, y + 8, 110, 30, c, c, 0, 15); f.text(575, y + 29, v, 13.5, WHITE, "middle", "700")
    f.rect(660, 90, 300, 168, YEL_L, YEL, 2.5, 12)
    f.text(810, 118, "Bon à savoir", 16, "#8a6d00", "middle", "700")
    for i, t in enumerate(("• chaque ACL se termine par un", "  « deny » implicite (même caché)", "• l'ordre des règles compte", "• on place l'ACL le plus près", "  possible de la source")):
        f.text(676, 148 + i * 22, t, 13.5, INK, "start")
    f.save(out(d, "acl-lecture.svg"))


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s07", "s08", "s09", "s10", "s11", "s12", "s13", "s14"]):
        globals()[w](); print("OK", w)
