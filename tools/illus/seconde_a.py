#!/usr/bin/env python3
"""Illustrations Seconde – séances S01 à S06 (matériel, Windows, Linux, terminal)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "seconde"))


def out(seance, name):
    return os.path.join(ROOT, seance, "images", name)


# ------------------------------------------------------------------ S04 Windows
def s04():
    d = "S04-windows"

    # 1. Rôle d'un système d'exploitation : le serveur du restaurant
    f = Fig(860, 360, "Rôle d'un système d'exploitation",
            "Trois couches : applications, système d'exploitation, matériel. Analogie avec un restaurant : client, serveur, cuisine.")
    f.title_bar("Le système d'exploitation : l'intermédiaire")
    cols = [(40, "Les applications", "Navigateur, Word,\njeux, Teams…", IND_L, IND, "Le client\nqui commande"),
            (330, "Le système d'exploitation", "Windows, Linux,\nmacOS, Android…", ORA_L, ORA, "Le serveur\nqui fait le lien"),
            (620, "Le matériel", "Processeur, mémoire,\ndisque, écran, réseau…", TEAL_L, TEAL, "La cuisine\nqui prépare")]
    for x, t, b, fi, st, an in cols:
        f.rect(x, 70, 200, 130, fi, st, 3, 14)
        f.text(x + 100, 102, t, 18 if len(t) < 20 else 15.5, st, "middle", "700")
        f.text(x + 100, 132, b, 15, INK)
        f.rect(x + 20, 230, 160, 62, WHITE, st, 2, 31, dash="6 5")
        f.text(x + 100, 255, an, 15, INK, "middle", "600")
    f.arrow(240, 135, 328, 135, LINE, 3); f.arrow(328, 150, 240, 150, LINE, 3)
    f.arrow(530, 135, 618, 135, LINE, 3); f.arrow(618, 150, 530, 150, LINE, 3)
    f.text(430, 330, "Une application ne parle jamais directement au matériel : elle passe par le système.", 15, MUTED, "middle", "600", italic=True)
    f.save(out(d, "os-role.svg"))

    # 2. Le chemin de l'installation
    f = Fig(960, 330, "Les grandes étapes d'une installation de Windows",
            "Clé USB, démarrage depuis la clé, installateur, choix du disque, copie des fichiers, premier démarrage, bureau, mises à jour et pilotes.")
    f.title_bar("Installer Windows : le chemin en 7 étapes")
    steps = [("1", "Préparer", "la clé USB\n(l'installateur)"), ("2", "Démarrer", "sur la clé\n(ordre de boot)"), ("3", "Choisir", "langue, édition,\nle disque"),
             ("4", "Copier", "Windows copie\nses fichiers"), ("5", "Configurer", "clavier, nom,\ncompte"), ("6", "Mettre\nà jour", "Windows Update\n+ pilotes"), ("7", "Livrer", "checklist\nposte prêt")]
    x0, w, gap = 18, 122, 12
    for i, (n, t, b) in enumerate(steps):
        x = x0 + i * (w + gap)
        col = ORA if i in (1,) else (GRN if i == 6 else IND)
        fill = ORA_L if i == 1 else (GRN_L if i == 6 else IND_L)
        f.rect(x, 90, w, 150, fill, col, 3, 12)
        f.badge(x + w / 2, 90, n, col, 16)
        f.text(x + w / 2, 132 if "\n" not in t else 124, t, 16, col, "middle", "700")
        f.text(x + w / 2, 176, b, 13, INK)
        if i < 6:
            f.arrow(x + w + 1, 165, x + w + gap - 1, 165, LINE, 3)
    f.text(480, 275, "Étape 2 : si le PC redémarre sur son ancien Windows, c'est l'ordre de démarrage (BIOS/UEFI) à corriger.", 14.5, ORA, "middle", "600")
    f.text(480, 302, "Étape 3 : c'est ici qu'on EFFACE ce qui se trouve sur le disque. Toujours sauvegarder avant.", 14.5, RED, "middle", "600")
    f.save(out(d, "etapes-installation.svg"))

    # 3. Disque et partitions
    f = Fig(860, 330, "Un disque découpé en partitions",
            "Un disque vierge (espace non alloué) est découpé automatiquement par Windows : partition système EFI, réservée, Windows (C:), récupération.")
    f.title_bar("Le disque : un grand placard qu'on découpe")
    f.text(30, 75, "AVANT (disque neuf)", 15, MUTED, "start", "700")
    f.rect(30, 85, 800, 50, GRY, GRY_D, 2, 8)
    f.text(430, 117, "Espace non alloué  (256 Go)", 17, MUTED, "middle", "600")
    f.arrow(430, 140, 430, 175, LINE, 3)
    f.text(30, 195, "APRÈS (Windows a découpé tout seul)", 15, MUTED, "start", "700")
    parts = [(30, 70, ORA_L, ORA, "EFI", "démarrage"), (100, 40, GRY, GRY_D, "MSR", "réservé"), (140, 560, IND_L, IND, "Windows (C:)", "système + tes fichiers + programmes"), (700, 130, TEAL_L, TEAL, "Récupération", "réparation")]
    for x, w, fi, st, t, b in parts:
        f.rect(x, 205, w, 60, fi, st, 2.5, 6)
        f.text(x + w / 2, 232 if w > 60 else 240, t, 15 if w > 60 else 12, st, "middle", "700")
        if w > 60:
            f.text(x + w / 2, 252, b, 12.5, INK)
    f.text(430, 305, "En pratique : tu cliques sur « Espace non alloué » puis « Suivant ». Windows fait le reste.", 15, INK, "middle", "600")
    f.save(out(d, "disque-partitions.svg"))

    # 4. Compte administrateur / standard
    f = Fig(860, 300, "Compte administrateur et compte standard",
            "Le compte administrateur peut tout modifier ; le compte standard utilise le poste mais ne peut pas installer ni changer le système.")
    f.title_bar("Deux types de comptes")
    for x, t, st, fi, lines, who in [(40, "Administrateur", ORA, ORA_L, [(1, "installer des logiciels"), (1, "créer des comptes"), (1, "changer le système"), (0, "un virus peut tout casser")], "Le technicien"),
                                       (450, "Utilisateur standard", TEAL, TEAL_L, [(1, "utiliser ses logiciels"), (1, "ses propres fichiers"), (0, "pas d'installation"), (1, "plus sûr au quotidien")], "L'utilisateur au quotidien")]:
        f.rect(x, 60, 370, 200, fi, st, 3, 14)
        f.text(x + 185, 95, t, 20, st, "middle", "700")
        for i, (ok, ln) in enumerate(lines):
            f.check(x + 38, 130 + i * 28, bool(ok))
            f.text(x + 62, 135 + i * 28, ln, 16, INK, "start")
        f.text(x + 185, 250, who, 14, MUTED, "middle", "600", italic=True)
    f.save(out(d, "comptes.svg"))

    # 5. Gestionnaire de périphériques (schéma)
    f = Fig(860, 360, "Le Gestionnaire de périphériques (schéma)",
            "Liste de familles de matériel ; un périphérique avec un triangle jaune n'a pas de pilote correct.")
    f.title_bar("Gestionnaire de périphériques : repérer le triangle jaune")
    f.rect(40, 55, 520, 285, WHITE, LINE, 2, 6)
    f.rect(40, 55, 520, 28, IND_L, LINE, 2, 6)
    f.text(56, 75, "Gestionnaire de périphériques", 14, INK, "start", "700")
    rows = [(0, "Cartes graphiques", None), (0, "Cartes son, vidéo et contrôleurs de jeu", None), (1, "Autres périphériques", None),
            (2, "Contrôleur Ethernet", "warn"), (0, "Cartes réseau", None), (0, "Claviers", None), (0, "Disques", None), (0, "Processeurs", None), (0, "Souris", None)]
    for i, (a, t, w) in enumerate(rows):
        y = 112 + i * 27
        if w:
            f.rect(48, y - 18, 504, 24, YEL_L, YEL, 1.5, 4)
            f.warn(80, y - 5, 10)
        if a == 0:
            f.poly([(58, y - 12), (58, y), (65, y - 6)], GRY_D, GRY_D, 1)
        elif a == 1:
            f.poly([(56, y - 10), (66, y - 10), (61, y - 3)], GRY_D, GRY_D, 1)
        f.text(100 if w else 74, y, t, 15, INK, "start", "600" if w else "400")
    f.callout(590, 100, 240, "Triangle jaune = Windows voit un matériel mais n'a pas son pilote.", YEL_L, YEL, 15)
    f.callout(590, 200, 240, "Que faire ?\n1. Windows Update\n2. Site du constructeur\n3. Rien au hasard sur Internet", GRN_L, GRN, 15)
    f.text(430, 352, "Schéma simplifié : l'apparence réelle dépend de la version de Windows.", 12.5, MUTED, "middle", italic=True)
    f.save(out(d, "gestionnaire-peripheriques.svg"))

    # 6. Poste prêt à l'emploi
    f = Fig(860, 380, "Checklist d'un poste prêt à l'emploi",
            "Huit points à vérifier avant de rendre un poste : nom, compte, date et heure, mises à jour, pilotes, réseau, antivirus, logiciels.")
    f.title_bar("Un poste « prêt à l'emploi », c'est quoi ?")
    items = ["Nom du poste clair (ex. : CIEL-PC01)", "Compte utilisateur créé, mot de passe noté", "Date, heure et langue corrects",
             "Windows à jour (Windows Update)", "Aucun triangle jaune dans le Gestionnaire de périphériques", "Réseau OK : une page web s'ouvre",
             "Antivirus actif (Sécurité Windows)", "Logiciels demandés installés et testés"]
    for i, t in enumerate(items):
        x = 40 + (i % 2) * 400
        y = 65 + (i // 2) * 72
        f.rect(x, y, 380, 56, GRN_L, GRN, 2, 10)
        f.badge(x + 26, y + 28, str(i + 1), GRN)
        f.text(x + 52, y + (24 if est_w(t, 15, "600") > 310 else 33), t, 15, INK, "start", "600", maxw=315)
    f.save(out(d, "poste-pret.svg"))


# ------------------------------------------------------------------ S05 Linux
def s05():
    d = "S05-linux"
    # arborescence
    f = Fig(860, 420, "L'arborescence Linux", "Tout part de la racine /. Dossiers principaux : home, etc, var, usr, bin, tmp.")
    f.title_bar("Linux : tout part de la racine  /")
    f.rect(370, 55, 120, 44, IND, IND, 2, 10); f.text(430, 84, "/  (racine)", 18, WHITE, "middle", "700")
    kids = [("home", "les dossiers\npersonnels", TEAL), ("etc", "les réglages\ndu système", ORA), ("var", "journaux, données\nqui changent", IND), ("usr", "programmes\ninstallés", IND), ("bin", "commandes\nde base", IND), ("tmp", "fichiers\ntemporaires", GRY_D)]
    for i, (n, b, c) in enumerate(kids):
        x = 25 + i * 138
        f.line(430, 99, x + 55, 150, GRY_D, 2)
        f.rect(x, 150, 110, 40, WHITE, c, 3, 8)
        f.mono(x + 55, 176, "/" + n, 16, c, "middle", "700")
        f.text(x + 55, 210, b, 13, INK)
    f.line(95, 238, 95, 275, GRY_D, 2)
    f.rect(20, 275, 150, 40, TEAL_L, TEAL, 2, 8); f.mono(95, 301, "/home/eleve", 15, TEAL, "middle", "700")
    f.line(95, 315, 95, 330, GRY_D, 2); f.line(85, 330, 365, 330, GRY_D, 2)
    for xx in (85, 225, 365): f.line(xx, 330, xx, 345, GRY_D, 2)
    for i, n in enumerate(["Documents", "Téléchargements", "Bureau"]):
        f.rect(20 + i * 140, 345, 130, 32, WHITE, TEAL, 1.5, 6); f.text(85 + i * 140, 366, n, 12.5, INK)
    f.callout(450, 285, 380, "Windows : C:\\Users\\eleve\\Documents\nLinux : /home/eleve/Documents\nLe chemin, c'est la même idée : seul le séparateur change.", GRN_L, GRN, 14.5)
    f.save(out(d, "arborescence.svg"))

    f = Fig(860, 300, "apt : le magasin d'applications en ligne de commande", "Le gestionnaire de paquets apt télécharge les logiciels depuis un dépôt officiel et les installe.")
    f.title_bar("apt : un magasin d'applications officiel")
    f.rect(40, 70, 200, 110, IND_L, IND, 3, 12); f.text(140, 105, "Dépôt officiel", 18, IND, "middle", "700"); f.text(140, 135, "(serveurs Debian/Ubuntu)\nlogiciels vérifiés", 14, INK)
    f.rect(330, 70, 200, 110, ORA_L, ORA, 3, 12); f.text(430, 105, "apt", 20, ORA, "middle", "700"); f.text(430, 135, "télécharge, installe,\nmet à jour", 14, INK)
    f.rect(620, 70, 200, 110, TEAL_L, TEAL, 3, 12); f.text(720, 105, "Ton PC", 18, TEAL, "middle", "700"); f.text(720, 135, "logiciel installé\net à jour", 14, INK)
    f.arrow(242, 125, 328, 125); f.arrow(532, 125, 618, 125)
    f.mono(40, 225, "sudo apt update      : « quoi de neuf dans le catalogue ? »", 15, INK, "start", "700")
    f.mono(40, 252, "sudo apt install vlc : installer un logiciel (ici VLC)", 15, INK, "start", "700")
    f.mono(40, 279, "sudo apt upgrade     : mettre à jour ce qui est installé", 15, INK, "start", "700")
    f.save(out(d, "apt.svg"))
    # famille Linux
    f = Fig(860, 390, "Le noyau Linux et ses distributions", "Un noyau commun, plusieurs distributions (Debian, Ubuntu, Mint, Kali...) et des appareils très variés.")
    f.title_bar("Linux : un noyau, plein de « distributions »")
    cx, cy = 430, 210
    dist = [(130, 120, "Debian", "stable, serveurs"), (130, 300, "Ubuntu", "grand public"), (730, 120, "Linux Mint", "proche de Windows"), (730, 300, "Kali Linux", "cybersécurité"), (430, 90, "Android", "téléphones"), (430, 340, "Box, NAS, routeurs", "objets connectés")]
    for x, y, n, b in dist:
        f.line(cx, cy, x, y, GRY_D, 2, "5 5")
    f.circle(cx, cy, 62, ORA_L, ORA, 4); f.text(cx, cy - 4, "Noyau\nLinux", 19, ORA, "middle", "700")
    for x, y, n, b in dist:
        f.rect(x - 85, y - 28, 170, 56, IND_L, IND, 2.5, 12)
        f.text(x, y - 3, n, 16, IND, "middle", "700"); f.text(x, y + 16, b, 13, INK)
    f.save(out(d, "famille-linux.svg"))



# ------------------------------------------------------------------ S06 terminal
def s06():
    d = "S06-terminal"
    f = Fig(860, 330, "Le terminal : dialoguer avec l'ordinateur par le texte",
            "Une commande, un résultat. Anatomie d'une commande : commande, option, argument.")
    f.title_bar("Anatomie d'une commande")
    f.rect(40, 60, 780, 80, "#1e1e2e", "#1e1e2e", 2, 10)
    f.mono(70, 108, "ping  -n 4  192.168.1.1", 28, "#a6e3a1", "start", "700")
    for x, w, t, c, y in [(70, 90, "commande", ORA, 175), (190, 70, "option", TEAL, 175), (290, 190, "argument", IND, 175)]:
        f.line(x + w / 2, 118, x + w / 2, 160, c, 3)
        f.text(x + w / 2, y + 20, t, 16, c, "middle", "700")
    f.text(70, 232, "commande : ce qu'on demande de faire", 15, INK, "start")
    f.text(70, 258, "option   : comment le faire (ici : 4 fois seulement)", 15, INK, "start")
    f.text(70, 284, "argument : sur quoi le faire (ici : la machine 192.168.1.1)", 15, INK, "start")
    f.save(out(d, "anatomie-commande.svg"))

    f = Fig(860, 360, "Chemins absolu et relatif", "Un arbre de dossiers : chemin absolu depuis la racine, chemin relatif depuis le dossier courant.")
    f.title_bar("Où suis-je ? (chemin absolu / relatif)")
    f.rect(360, 50, 140, 36, IND, IND, 2, 8); f.mono(430, 74, "/home/eleve", 15, WHITE, "middle", "700")
    for i, (n, c) in enumerate([("Documents", IND), ("Images", GRY_D), ("tresor", TEAL)]):
        x = 130 + i * 250
        f.line(430, 86, x + 60, 130, GRY_D, 2)
        f.rect(x, 130, 120, 36, WHITE, c, 3, 8); f.text(x + 60, 154, n, 15, c, "middle", "700")
    f.line(190, 166, 190, 210, GRY_D, 2)
    f.rect(130, 210, 120, 36, WHITE, IND, 2, 8); f.text(190, 234, "cours", 15, IND, "middle", "700")
    f.callout(40, 275, 780, "Absolu : cd /home/eleve/Documents/cours     (marche de partout)\nRelatif : cd Documents/cours  depuis /home/eleve      |      cd ..  = remonter d'un dossier", GRN_L, GRN, 14.5)
    f.save(out(d, "chemins.svg"))


if __name__ == "__main__":
    which = sys.argv[1:] or ["s04", "s05", "s06"]
    for w in which:
        globals()[w]()
        print("OK", w)
