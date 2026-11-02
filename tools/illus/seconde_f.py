#!/usr/bin/env python3
"""Illustrations Seconde – S04 : fiches « créer une clé USB bootable » (Ventoy, Rufus, outil Microsoft)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "seconde", "S04-windows", "images"))
out = lambda n: os.path.join(ROOT, n)
WINBG = "#f3f4f8"


def window(f, x, y, w, h, title):
    """Fenêtre Windows simplifiée (barre de titre + corps)."""
    f.rect(x, y, w, h, WINBG, "#8a93b8", 2, 8)
    f.rect(x, y, w, 30, IND_L, "#8a93b8", 2, 8)
    f.text(x + 12, y + 21, title, 14, INK, "start", "700")
    f.text(x + w - 16, y + 21, "×", 20, MUTED, "middle")


def field(f, x, y, w, label, value, lw=150, h=28, fill=WHITE, stroke="#8a93b8", vcol=INK, arrow=True):
    f.text(x, y + 19, label, 13.5, MUTED, "start", "600")
    f.rect(x + lw, y, w - lw, h, fill, stroke, 1.5, 4)
    f.text(x + lw + 8, y + 19, value, 13.5, vcol, "start")
    if arrow:
        dd(f, x + w - 14, y + 14)


def dd(f, x, y):
    f.poly([(x - 5, y), (x + 5, y), (x, y + 6)], MUTED, MUTED, 1)


def usb(f, x, y, w=120, h=44, c=IND):
    f.rect(x, y, w, h, GRY, c, 2.5, 8)
    f.rect(x - 22, y + 10, 24, h - 20, GRY_D, c, 2, 3)
    f.rect(x - 16, y + 17, 6, 5, WHITE, c, 1, 1); f.rect(x - 16, y + h - 22, 6, 5, WHITE, c, 1, 1)


def cle_choix():
    f = Fig(1000, 500, "Choisir son outil", "Comparaison de Ventoy, Rufus et de l'outil de création de média Microsoft : plusieurs ISO, hors-ligne, réglages, effort.")
    f.title_bar("Trois outils, trois façons de faire une clé d'installation")
    cols = [(30, "Ventoy", "★ l'outil prioritaire", TEAL, TEAL_L), (353, "Rufus", "l'outil précis", IND, IND_L), (676, "Outil Microsoft", "le plus simple, mais limité", ORA, ORA_L)]
    rows = ["Plusieurs systèmes sur la même clé", "On remplace l'ISO sans reformater la clé", "Règle le mode BIOS (UEFI / Legacy)", "Télécharge Windows pour toi", "Effort après la 1re fois"]
    vals = {"Ventoy": [True, True, False, False, "Copier un fichier"],
            "Rufus": [False, False, True, True, "Tout refaire"],
            "Outil Microsoft": [False, False, False, True, "Tout refaire"]}
    for x, n, sub, c, fill in cols:
        f.rect(x, 60, 294, 410, fill, c, 3, 14)
        f.text(x + 147, 98, n, 26, c, "middle", "700"); f.text(x + 147, 122, sub, 14, INK, "middle", "600")
        f.line(x + 14, 136, x + 280, 136, c, 2)
        for i, r in enumerate(rows):
            y = 168 + i * 58
            f.text(x + 16, y, wrap(r, 190, 14, "600"), 14, INK, "start", "600")
            v = vals[n][i]
            if isinstance(v, bool):
                f.check(x + 262, y + (6 if "\n" in wrap(r, 190, 14, "600") else -4), v, 22)
            else:
                f.text(x + 262, y - 2, wrap(v, 80, 12.5, "700"), 12.5, c, "end", "700")
    f.text(500, 488, "Dans tous les cas : la clé est entièrement effacée la première fois.", 14, RED, "middle", "700")
    f.save(out("cle-choix-outils.svg"))


def ventoy_principe():
    f = Fig(1000, 470, "Le principe de Ventoy", "Une clé Ventoy a deux partitions : une grande qui contient les fichiers ISO que l'on copie, une petite de démarrage. Au démarrage, Ventoy affiche un menu des ISO.")
    f.title_bar("Ventoy : on prépare la clé UNE fois, ensuite on copie des ISO")
    f.text(240, 72, "① La clé après installation de Ventoy", 16, TEAL, "middle", "700")
    usb(f, 70, 95, 340, 56, TEAL)
    f.rect(70, 95, 270, 56, TEAL_L, TEAL, 2.5, 8); f.text(205, 118, "Partition 1 : « Ventoy »", 14, TEAL, "middle", "700"); f.text(205, 138, "exFAT · presque toute la clé", 12.5, INK)
    f.rect(340, 95, 70, 56, YEL_L, "#b28704", 2.5, 8); f.text(375, 118, "VTOYEFI", 12, INK, "middle", "700"); f.text(375, 138, "32 Mo", 12, MUTED)
    f.text(240, 178, "(la petite partition sert à démarrer, on n'y touche pas)", 12.5, MUTED, "middle", italic=True)
    f.text(240, 225, "② Tu copies tes ISO comme des fichiers normaux", 16, TEAL, "middle", "700")
    files = [("Windows11_25H2_fr.iso", "~ 7 Go"), ("Windows10_22H2.iso", "~ 6 Go"), ("ubuntu-24.04.iso", "~ 6 Go"), ("hirens-bootcd.iso", "~ 3 Go")]
    for i, (n, s) in enumerate(files):
        y = 245 + i * 42
        f.rect(80, y, 320, 34, WHITE, GRY_D, 1.5, 6)
        f.rect(90, y + 7, 16, 20, IND_L, IND, 1.5, 2)
        f.mono(116, y + 22, n, 13.5, INK); f.text(392, y + 22, s, 12.5, MUTED, "end")
    f.text(240, 438, "Aucun formatage : glisser-déposer.", 14, TEAL, "middle", "700")
    f.arrow(440, 250, 540, 250, TEAL, 4)
    f.text(490, 228, "on démarre", 13, TEAL, "middle", "700"); f.text(490, 244, "dessus", 13, TEAL, "middle", "700")
    f.text(760, 72, "③ Au démarrage : le menu Ventoy", 16, TEAL, "middle", "700")
    window(f, 560, 95, 400, 300, "Ventoy 1.1.18 – menu de démarrage")
    f.rect(560, 125, 400, 270, "#0f1630", "#8a93b8", 2, 8)
    items = ["Windows10_22H2.iso", "Windows11_25H2_fr.iso", "hirens-bootcd.iso", "ubuntu-24.04.iso"]
    for i, n in enumerate(items):
        y = 160 + i * 38
        if i == 1:
            f.rect(576, y - 20, 368, 30, "#e8eaf6", None, 0, 4)
        f.mono(592, y, n, 15, "#0f1630" if i == 1 else "#e8eaf6")
    f.mono(592, 360, "↑ ↓ choisir  ·  Entrée valider", 12.5, "#9fa8da")
    f.text(760, 424, "Les ISO sont classées par ordre alphabétique.", 13, INK, "middle", "600")
    f.text(760, 444, "Un seul fichier = un seul choix à faire à l'écran.", 13, INK, "middle", "600")
    f.save(out("ventoy-principe.svg"))


def ventoy_installateur():
    f = Fig(1000, 560, "La fenêtre Ventoy2Disk", "Maquette de la fenêtre Ventoy2Disk : choisir le périphérique, régler le menu Option (Secure Boot, style de partition), puis cliquer sur Install.")
    f.title_bar("Ventoy2Disk.exe : trois gestes seulement")
    window(f, 30, 60, 520, 440, "Ventoy2Disk")
    f.text(50, 110, "Périphérique", 13.5, MUTED, "start", "600")
    f.rect(50, 118, 480, 30, WHITE, "#8a93b8", 1.5, 4); f.text(60, 138, "[E:] SanDisk Ultra  28.7 GB", 14, INK, "start"); dd(f, 512, 132)
    f.rect(50, 168, 230, 90, WHITE, GRY_D, 1.5, 6); f.text(165, 190, "Ventoy dans le package", 12.5, MUTED, "middle", "600"); f.text(165, 232, "1.1.18", 26, INK, "middle", "700")
    f.rect(300, 168, 230, 90, WHITE, GRY_D, 1.5, 6); f.text(415, 190, "Ventoy sur la clé", 12.5, MUTED, "middle", "600"); f.text(415, 232, "(vide)", 22, GRY_D, "middle", "700")
    f.rect(50, 276, 480, 30, WHITE, GRY_D, 1.5, 6); f.text(290, 296, "Secure Boot activé · MBR", 13, TEAL, "middle", "700")
    # Option menu
    f.text(60, 332, "Menu « Option » (barre du haut)", 13.5, MUTED, "start", "600")
    f.rect(50, 340, 250, 112, WHITE, "#8a93b8", 1.5, 4)
    for i, (t, on) in enumerate([("Secure Boot Support", True), ("Partition Style  >  MBR / GPT", False), ("Partition Configuration  >", False), ("Clear Ventoy", False)]):
        y = 362 + i * 25
        if on:
            f.check(66, y - 5, True, 16)
        f.text(84, y, t, 13, INK, "start", "700" if i < 2 else "400")
    f.rect(330, 372, 130, 56, TEAL, "#00695c", 2, 8); f.text(395, 408, "Install", 22, WHITE, "middle", "700")
    f.rect(330, 438, 130, 40, WHITE, "#8a93b8", 2, 8); f.text(395, 464, "Update", 17, INK, "middle", "700")
    f.badge(40, 133, "1", TEAL); f.badge(40, 395, "2", ORA); f.badge(318, 400, "3", RED)
    # Explications
    xs = 590
    f.rect(xs, 70, 380, 130, TEAL_L, TEAL, 2.5, 10)
    f.badge(xs + 24, 94, "1", TEAL); f.text(xs + 46, 100, "Bon périphérique ?", 16, TEAL, "start", "700")
    f.text(xs + 16, 128, "Vérifier la lettre ET la taille :\nle disque du PC n'est jamais\nune clé de 28 Go.", 13.5, INK, "start")
    f.rect(xs, 214, 380, 150, ORA_L, ORA, 2.5, 10)
    f.badge(xs + 24, 238, "2", ORA); f.text(xs + 46, 244, "Deux réglages (menu Option)", 16, ORA, "start", "700")
    f.text(xs + 16, 270, "Secure Boot Support : coché (laisser).\nPartition Style : MBR par défaut\n(démarre en UEFI et en Legacy).\nGPT seulement si le prof le demande.", 13.5, INK, "start")
    f.rect(xs, 378, 380, 122, RED_L, RED, 2.5, 10)
    f.badge(xs + 24, 402, "3", RED); f.text(xs + 46, 408, "Install = effacement", 16, RED, "start", "700")
    f.text(xs + 16, 434, "Ventoy demande deux confirmations :\ntout ce qui est sur la clé disparaît.\nUpdate, lui, garde tes ISO.", 13.5, INK, "start")
    f.text(500, 536, "Résultat attendu : « Ventoy sur la clé » affiche 1.1.18, la clé se nomme « Ventoy » dans l'Explorateur.", 13.5, INK, "middle", "700")
    f.save(out("ventoy-installateur.svg"))


def bios_modes():
    f = Fig(1000, 580, "UEFI ou Legacy : deux chemins", "Selon que la clé est démarrée en mode UEFI ou en mode Legacy/CSM, Windows crée un disque GPT ou MBR, ce qui détermine Secure Boot et Windows 11.")
    f.title_bar("Le mode dans lequel on démarre la clé décide de TOUT le reste")
    f.rect(30, 60, 940, 70, YEL_L, YEL, 2.5, 10)
    f.text(50, 88, "Dans le menu de démarrage (F12…), la même clé apparaît en double :", 14.5, INK, "start", "700")
    f.mono(50, 114, "« UEFI : SanDisk Ultra »    et    « SanDisk Ultra »  (sans UEFI = mode Legacy)", 14, INK)
    # lanes
    lanes = [(160, "Tu choisis « UEFI : … »", TEAL, TEAL_L, "GPT", "Disque GPT + partition EFI", ["Secure Boot possible", "Windows 11 accepté", "Disques > 2 To utilisables"], True),
             (355, "Tu choisis l'entrée sans « UEFI »", RED, RED_L, "MBR", "Disque MBR (ancien format)", ["Secure Boot impossible", "Windows 11 refuse d'installer", "Disque limité à 2 To"], False)]
    for y, title, c, fill, tag, disk, cons, ok in lanes:
        f.rect(30, y, 940, 175, fill, c, 3, 14)
        f.rect(46, y + 14, 230, 70, WHITE, c, 2.5, 10); f.text(161, y + 44, wrap(title, 205, 15, "700"), 15, c, "middle", "700")
        f.arrow(278, y + 50, 332, y + 50, c, 4)
        f.rect(336, y + 14, 270, 70, WHITE, c, 2.5, 10); f.text(471, y + 40, "Windows crée sur le PC :", 12.5, MUTED, "middle", "600"); f.text(471, y + 66, disk, 14.5, INK, "middle", "700")
        f.arrow(608, y + 50, 662, y + 50, c, 4)
        f.rect(666, y + 14, 288, 148, WHITE, c, 2.5, 10); f.text(810, y + 40, "Conséquences", 15, c, "middle", "700")
        for i, t in enumerate(cons):
            f.check(690, y + 64 + i * 32, ok, 18); f.text(708, y + 70 + i * 32, t, 13.5, INK, "start", "600")
        # disque schéma
        parts = ([("EFI\n100 Mo", YEL_L, 60), ("MSR\n16 Mo", GRY, 46), ("C: (Windows)", IND_L, 150), ("Récup.", GRY, 56)] if ok else
                 [("Réservé\n500 Mo", YEL_L, 80), ("C: (Windows)", IND_L, 240)])
        x = 46
        for t, col, w in parts:
            f.rect(x, y + 104, w, 48, col, c, 1.5, 4); f.text(x + w / 2, y + 125, t, 11.5, INK, "middle", "700"); x += w + 4
    f.text(500, 560, "Changer de mode après coup ≠ simple réglage : il faut convertir le disque ou tout réinstaller. Donc : on choisit bien au départ.", 13.5, INK, "middle", "700")
    f.save(out("bios-modes-uefi-legacy.svg"))


def secureboot():
    f = Fig(1000, 470, "Secure Boot et Ventoy", "Avec Secure Boot, le BIOS n'exécute que des programmes signés. Ventoy utilise un programme signé par Microsoft qui demande d'enregistrer la clé de Ventoy au premier démarrage.")
    f.title_bar("Secure Boot : le vigile du BIOS ne laisse passer que les programmes signés")
    # chaîne
    steps = [("BIOS / UEFI", "contient la liste des\nsignatures acceptées", IND, IND_L), ("Programme signé", "(« shim », signé\npar Microsoft)", TEAL, TEAL_L), ("Clé de Ventoy", "à enregistrer UNE fois\n(MokManager)", ORA, ORA_L), ("Ventoy", "puis ton ISO\nWindows", GRN, GRN_L)]
    for i, (t, s, c, fill) in enumerate(steps):
        x = 40 + i * 240
        f.rect(x, 70, 200, 110, fill, c, 3, 12); f.text(x + 100, 102, t, 17, c, "middle", "700"); f.text(x + 100, 132, s, 13, INK)
        if i < 3:
            f.arrow(x + 204, 125, x + 236, 125, c, 4)
    f.rect(30, 210, 440, 230, WHITE, ORA, 3, 12)
    f.text(250, 238, "1er démarrage sur la clé Ventoy (écrans en anglais)", 14.5, ORA, "middle", "700")
    for i, t in enumerate(["Écran bleu « Perform MOK management »", "→ Enroll key from disk", "→ VTOYEFI → ENROLL_THIS_KEY_IN_MOKMANAGER.cer", "→ Continue → Yes → Reboot"]):
        f.badge(56, 268 + i * 38, str(i + 1), ORA, 11); f.text(78, 273 + i * 38, t, 12.5, INK, "start", "600")
    f.text(250, 428, "Les démarrages suivants : plus d'écran bleu.", 12.5, GRN, "middle", "700")
    f.rect(500, 210, 470, 230, WHITE, IND, 3, 12)
    f.text(735, 238, "Que faire si ça bloque ?", 15, IND, "middle", "700")
    tips = [("« Security Violation » / clé refusée", "→ l'enregistrement n'a pas été fait : recommencer"), ("Certains PC ne l'acceptent pas", "→ option BIOS « Allow Microsoft 3rd Party UEFI CA »"), ("Pas de temps / PC de TP", "→ prof : désactiver Secure Boot, ou utiliser Rufus")]
    for i, (a, b) in enumerate(tips):
        y = 272 + i * 56
        f.text(520, y, a, 13, INK, "start", "700"); f.text(520, y + 20, b, 12.5, MUTED, "start", "600")
    f.text(500, 462, "Désactiver Secure Boot est un dernier recours : Windows 11 le demande à l'usage. On le réactive après l'installation.", 12.5, RED, "middle", "700")
    f.save(out("secureboot-ventoy.svg"))


def rufus_fenetre():
    f = Fig(1000, 640, "La fenêtre de Rufus", "Maquette de Rufus : périphérique, sélection de l'ISO, schéma de partition, système cible, système de fichiers, bouton DÉMARRER.")
    f.title_bar("Rufus : six repères, chacun a une conséquence")
    window(f, 30, 60, 500, 560, "Rufus 4.15")
    f.text(46, 110, "Propriétés du lecteur", 14, IND, "start", "700")
    field(f, 60, 124, 454, "Périphérique", "SanDisk Ultra (E:) [29 Go]", 136)
    field(f, 60, 160, 454, "Type de démarrage", "Image disque ou ISO", 136, arrow=True)
    f.rect(414, 160, 100, 28, IND, IND, 1.5, 4); f.text(464, 179, "SÉLECTIONNER", 12, WHITE, "middle", "700")
    field(f, 60, 196, 454, "Option d'image", "Installation Windows standard", 136)
    field(f, 60, 232, 454, "Schéma de partition", "GPT", 136)
    field(f, 60, 268, 454, "Système cible", "UEFI (non CSM)", 136)
    f.text(46, 322, "Options de formatage", 14, IND, "start", "700")
    field(f, 60, 336, 454, "Nom de volume", "WIN11_25H2_FR", 136, arrow=False)
    field(f, 60, 372, 454, "Système de fichiers", "FAT32 (par défaut)", 136)
    field(f, 60, 408, 454, "Taille de cluster", "16 kilo-octets (défaut)", 136)
    f.rect(46, 460, 454, 26, GRY, GRY_D, 1.5, 4); f.text(280, 478, "PRÊT", 13, MUTED, "middle", "700")
    f.rect(150, 510, 130, 44, TEAL, "#00695c", 2, 8); f.text(215, 539, "DÉMARRER", 17, WHITE, "middle", "700")
    f.rect(300, 510, 130, 44, WHITE, "#8a93b8", 2, 8); f.text(365, 539, "FERMER", 17, INK, "middle", "700")
    for n, y, c in [("1", 138, TEAL), ("2", 174, TEAL), ("3", 246, ORA), ("4", 282, ORA), ("5", 386, RED), ("6", 524, GRN)]:
        f.badge(42 if n != "6" else 134, y, n, c, 11)
    xs = 560
    notes = [(70, TEAL, TEAL_L, "1·2  La clé et l'ISO", "Vérifier la taille de la clé. Sélectionner l'ISO\ntéléchargé sur le site Microsoft."),
             (160, ORA, ORA_L, "3·4  Le mode BIOS", "GPT + UEFI : PC récents, Secure Boot OK.\nMBR + BIOS (ou UEFI-CSM) : vieux PC, pas\nde Windows 11. Rufus propose le bon couple."),
             (278, RED, RED_L, "5  Le système de fichiers", "FAT32 : démarre partout, même avec Secure\nBoot. NTFS : accepte les fichiers > 4 Go,\nmais ajoute une petite partition UEFI:NTFS\nque Secure Boot peut refuser."),
             (410, GRN, GRN_L, "6  DÉMARRER", "Efface TOUTE la clé (message d'alerte).\nPuis une fenêtre « Expérience utilisateur\nWindows » propose des réglages : voir fiche.")]
    yy = 70
    for _, c, fill, t, b in notes:
        y = yy
        h = 18 + 22 + b.count("\n") * 17 + 36
        f.rect(xs, y, 410, h, fill, c, 2.5, 10); f.text(xs + 14, y + 26, t, 15.5, c, "start", "700"); f.text(xs + 14, y + 50, b, 13, INK, "start"); yy += h + 14
    f.save(out("rufus-fenetre.svg"))


def mct_etapes():
    f = Fig(1000, 400, "L'outil de création de média Microsoft", "Cinq étapes : télécharger l'outil, accepter, choisir langue et édition, choisir clé USB, attendre la création.")
    f.title_bar("Outil Microsoft : cinq écrans, aucun réglage BIOS")
    steps = [("Télécharger", "« Créer un support\nd'installation » sur\nmicrosoft.com", IND), ("Accepter", "avis et conditions\nde licence", IND), ("Langue + édition", "décocher « options\nrecommandées »\nsi besoin", ORA), ("Lecteur flash USB", "≥ 8 Go, sera\nentièrement effacé", RED), ("Attendre", "téléchargement,\nvérification, création\n(20 à 60 min)", GRN)]
    for i, (t, s, c) in enumerate(steps):
        x = 30 + i * 192
        f.rect(x, 70, 170, 190, WHITE, c, 3, 12); f.badge(x + 24, 94, str(i + 1), c)
        f.text(x + 85, 142, wrap(t, 150, 16, "700"), 16, c, "middle", "700"); f.text(x + 85, 186, s, 12.5, INK)
        if i < 4:
            f.arrow(x + 172, 165, x + 190, 165, LINE, 3)
    f.rect(30, 290, 940, 90, YEL_L, YEL, 2.5, 10)
    f.text(50, 318, "À savoir avant de choisir cet outil", 15, INK, "start", "700")
    f.text(50, 344, "Toujours la dernière version de Windows 11 (pas de choix de version). La clé est préparée au format FAT32 pour démarrer en UEFI :", 13.5, INK, "start")
    f.text(50, 366, "aucun choix de mode BIOS, aucun contournement des exigences TPM / Secure Boot de Windows 11.", 13.5, INK, "start")
    f.save(out("mct-etapes.svg"))


if __name__ == "__main__":
    for fn in (cle_choix, ventoy_principe, ventoy_installateur, bios_modes, secureboot, rufus_fenetre, mct_etapes):
        fn(); print("OK", fn.__name__)
