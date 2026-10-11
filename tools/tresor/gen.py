#!/usr/bin/env python3
"""Génère les deux scripts qui préparent la « chasse au trésor » du terminal (S06) :
   - creer-tresor.sh  (Linux / bash)
   - creer-tresor.cmd (Windows / cmd)
La chaîne d'indices est écrite UNE seule fois ici : les deux systèmes restent identiques.
Aucun accent ni caractère spécial dans les textes (compatibilité cmd)."""
import os

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "seconde", "S06-terminal", "ressources"))
ROOT = "chasse-au-tresor"

# (chemin relatif en '/', contenu (liste de lignes), caché ?)
FILES = [
    ("LISEZ-MOI.txt", [
        "BIENVENUE, CHERCHEUR DE TRESOR !",
        "",
        "Un tresor est cache dans ces dossiers. Pour le trouver, tu n'as droit",
        "qu'a UN outil : le terminal (pas d'explorateur de fichiers !).",
        "",
        "Chaque indice contient UNE LETTRE. A la fin, les 7 lettres forment un mot.",
        "",
        "Premier indice : le fichier etape1.txt est dans le dossier carte.",
        "Pour lire un fichier dans le terminal : cat (Linux) ou type (Windows).",
    ], False),
    ("carte/etape1.txt", [
        "ETAPE 1 - Bravo, tu sais LIRE un fichier !",
        "Lettre 1 : C",
        "",
        "Prochaine mission : va dans le dossier foret (commande cd).",
        "Regarde ce qu'il contient (commande ls sous Linux, dir sous Windows).",
        "Puis entre dans le dossier clairiere et lis etape2.txt.",
    ], False),
    ("foret/arbre-creux.txt", [
        "Ce fichier est un piege : il ne contient aucune lettre.",
        "Un bon technicien lit ce qu'il y a dans le dossier avant de choisir.",
    ], False),
    ("foret/clairiere/etape2.txt", [
        "ETAPE 2 - Tu navigues bien !",
        "Lettre 2 : A",
        "",
        "Il y a un FICHIER CACHE dans cette clairiere : son nom commence par etape3.",
        "Pour afficher les fichiers caches : ls -a (Linux) ou dir /a (Windows).",
        "Lis-le avec cat ou type.",
    ], False),
    ("foret/clairiere/etape3-cache.txt", [
        "ETAPE 3 - Bien joue, tu as trouve le fichier cache !",
        "Lettre 3 : B",
        "",
        "Maintenant, remonte d'un dossier avec cd .. (deux points).",
        "Remonte encore une fois pour revenir dans chasse-au-tresor.",
        "Puis va dans riviere, puis dans pont. Lis etape4.txt.",
    ], True),
    ("riviere/pont/etape4.txt", [
        "ETAPE 4 - Les chemins n'ont plus de secret pour toi ?",
        "Lettre 4 : L",
        "",
        "La grotte est dans le dossier montagne. Depuis ici, le chemin RELATIF est :",
        "../../montagne/grotte   (sous Windows : ..\\..\\montagne\\grotte)",
        "Tape cd avec ce chemin, en UNE seule commande. Lis etape5.txt.",
    ], False),
    ("montagne/grotte/etape5.txt", [
        "ETAPE 5 - Tu es dans la grotte.",
        "Lettre 5 : A",
        "",
        "1) Cree un dossier nomme camp dans chasse-au-tresor (commande mkdir).",
        "   Astuce : le dossier chasse-au-tresor est deux niveaux plus haut : ../../camp",
        "2) COPIE le fichier cle.txt de cette grotte dans le dossier camp (cp ou copy).",
        "3) Verifie avec ls ou dir que cle.txt est dans camp ET toujours dans la grotte.",
        "Ensuite, va au coffre : dossier coffre, dans chasse-au-tresor. Lis etape6.txt.",
    ], False),
    ("montagne/grotte/cle.txt", [
        "Je suis la CLE du coffre. Copie-moi dans le dossier camp, sans me deplacer.",
    ], False),
    ("coffre/etape6.txt", [
        "ETAPE 6 - Le coffre !",
        "Lettre 6 : G",
        "",
        "1) Il y a ici un fichier piege.txt : SUPPRIME-LE (rm ou del).",
        "   Attention : pas de corbeille dans le terminal. C'est definitif !",
        "2) Cree un fichier nomme mon-nom.txt contenant ton prenom",
        "   (echo Prenom > mon-nom.txt).",
        "3) DEPLACE ce fichier mon-nom.txt dans le dossier camp (mv ou move).",
        "Dernier indice : lis final.txt (dans ce dossier).",
    ], False),
    ("coffre/piege.txt", [
        "Supprime-moi ! (et demande-toi pourquoi il faut faire attention avant de supprimer).",
    ], False),
    ("coffre/final.txt", [
        "ETAPE 7 - DERNIERE ETAPE",
        "Lettre 7 : E",
        "",
        "Assemble les 7 lettres dans l'ordre : le mot est le nom d'un metier de CIEL.",
        "Montre ton terminal a l'enseignant et explique chaque commande utilisee.",
    ], False),
]
DIRS = ["carte", "foret", "foret/clairiere", "riviere", "riviere/pont", "montagne", "montagne/grotte", "coffre"]


def sh():
    L = ["#!/bin/bash", "# Prepare la chasse au tresor (S06 - terminal). A lancer UNE fois : bash creer-tresor.sh",
         f'# Cree le dossier ~/{ROOT}', 'cd ~ || exit 1', f'rm -rf "{ROOT}"', f'mkdir "{ROOT}"', f'cd "{ROOT}" || exit 1']
    for d in DIRS:
        L.append(f'mkdir -p "{d}"')
    for path, lines, hidden in FILES:
        target = path
        if hidden:
            d, n = os.path.split(path)
            target = os.path.join(d, "." + n)
        L.append(f'cat > "{target}" <<\'FIN\'')
        L.extend(lines)
        L.append("FIN")
    L.append('echo "Chasse au tresor prete dans ~/' + ROOT + ' ."')
    return "\n".join(L) + "\n"


def cmd():
    L = ["@echo off", "rem Prepare la chasse au tresor (S06 - terminal). A lancer UNE fois : double-clic ou creer-tresor.cmd",
         f"cd /d %USERPROFILE%", f"if exist {ROOT} rmdir /s /q {ROOT}", f"mkdir {ROOT}", f"cd {ROOT}"]
    for d in DIRS:
        L.append("mkdir " + d.replace("/", "\\"))
    for path, lines, hidden in FILES:
        p = path.replace("/", "\\")
        first = True
        for ln in lines:
            txt = "".join("^" + c if c in "<>|&^" else ("%%" if c == "%" else c) for c in ln)
            if txt.strip() == "":
                L.append(f"echo.{'>' if first else '>>'} {p}")
            else:
                # echo texte> fichier : on colle le > au texte, sans espace superflu
                L.append(f"echo {txt}{'>' if first else '>>'} {p}")
            first = False
        if hidden:
            L.append(f"attrib +h {p}")
    L.append(f"echo Chasse au tresor prete dans %USERPROFILE%\\{ROOT}")
    L.append("pause")
    return "\r\n".join(L) + "\r\n"


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "creer-tresor.sh"), "w", encoding="utf-8", newline="\n") as f:
        f.write(sh())
    with open(os.path.join(OUT, "creer-tresor.cmd"), "w", encoding="utf-8", newline="") as f:
        f.write(cmd())
    print("ok")
