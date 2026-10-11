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


if __name__ == "__main__":
    for w in (sys.argv[1:] or ["s07", "s08", "s09", "s10", "s11"]):
        globals()[w](); print("OK", w)
