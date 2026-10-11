#!/usr/bin/env python3
"""Génère les pages d'index (README.md de chaque année) et les fichiers .pages
à partir de tools/curriculum.json. Une séance sans dossier = « en préparation ».
Usage : python3 tools/make_nav.py"""
import json, os, datetime
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS = os.path.join(ROOT, "docs")
cur = json.load(open(os.path.join(ROOT, "tools", "curriculum.json"), encoding="utf-8"))
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
YEARS = {
 "seconde": ("Seconde", "🌱", """**Objectif de l'année :** devenir **autonome sur le matériel et le réseau de base**. L'élève n'a jamais fait d'informatique ni de réseau : on avance **une idée à la fois**, toujours en **manipulant d'abord**.

**Progression :** 🔧 le matériel (PC, systèmes, terminal) → 🔌 le câblage (réseau physique) → 🔢 les adresses (IP, DHCP, DNS) → 📶 le Wi-Fi → 🩺 le dépannage de niveau 1 → 🏗️ un petit projet complet (**A1**)."""),
 "premiere": ("Première", "🌿", """**Objectif de l'année :** **comprendre ce qui circule** sur un réseau et **configurer** des équipements administrables : switch, routeur, VLAN, serveurs Linux, DHCP, DNS, sécurité de base.

**Progression :** 🔍 les couches et les protocoles (on *regarde* les trames) → 🔀 switch, sous-réseaux, routeur → 🏷️ VLAN → 🖥️ serveurs (Linux, DHCP, DNS, web, partage) → 🛡️ sécurité de base → 🏗️ projet **A2**."""),
 "terminale": ("Terminale", "🌳", """**Objectif de l'année :** **réaliser des chantiers complets en autonomie** et se préparer à l'épreuve **E31 / U31** : lire un dossier, préparer, installer, configurer, tester, dépanner, rendre compte.

**Progression :** 📑 dossier et chantier → 🔌 installation et mesures → 🏢 réseau de PME (inter-VLAN, Wi-Fi, sauvegardes) → 🔐 accès distant et supervision → 🩺 dépannage méthodique → ✅ recette client → 🏁 chantiers d'entraînement et évaluation."""),
}
def write_pages(r, y):
    fp = os.path.join(DOCS, y, f"{r['code']}-{r['slug']}")
    if os.path.isdir(fp):
        t = r["theme"].replace('"', "'")
        open(os.path.join(fp, ".pages"), "w", encoding="utf-8").write(f'title: "{r["code"]} · {t}"\n')


AUTO = {"Guidé": "🟢 Guidé", "Semi-guidé": "🟡 Semi-guidé", "Autonome": "🔴 Autonome", "—": "—"}


def fr(d):
    y, m, j = map(int, d.split("-"))
    return f"{'1er' if j == 1 else j} {MOIS[m-1]} {y}"


def folder(r):
    return f"{r['code']}-{r['slug']}"


for y, (label, ico, intro) in YEARS.items():
    rows = [r for r in cur if r["year"] == y]
    for r in rows:
        write_pages(r, y)
    L = [f"# {ico} {label} – Réseaux et systèmes (E31)", "", intro, "",
         "> [!NOTE]", "> Chaque séance contient une **fiche séance**, un **cours** (avec des questions pour vérifier la compréhension), un **TP** guidé et, quand c'est utile, un **fichier pour le simulateur réseau** à ouvrir hors ligne.", "",
         "## 📅 Progression", "",
         "| Séance | Semaine (CFA) | Thème | Autonomie | Contenu |", "|---|---|---|---|---|"]
    for r in rows:
        fp = os.path.join(DOCS, y, folder(r))
        if os.path.isdir(fp) and os.path.exists(os.path.join(fp, "README.md")):
            link = f"[📘 Ouvrir]({folder(r)}/README.md)"
        elif r["code"] == "S07" and y == "seconde":
            link = "✈️ Voyage à Paris"
        else:
            link = "🚧 en préparation"
        L.append(f"| **{r['code']}** | {fr(r['date'])} | {r['theme']} | {AUTO.get(r.get('auto','—'), r.get('auto'))} | {link} |")
    L += ["", "## 🧭 Autonomie : comment lire les pastilles", "",
          "| Pastille | Signification |", "|---|---|",
          "| 🟢 **Guidé** | Fiche pas à pas, chaque étape expliquée, l'enseignant est très présent |",
          "| 🟡 **Semi-guidé** | Consigne et aide au besoin ; l'élève cherche d'abord seul |",
          "| 🔴 **Autonome** | Cahier des charges seul ; l'élève décide, justifie et documente |", ""]
    open(os.path.join(DOCS, y, "README.md"), "w", encoding="utf-8").write("\n".join(L))
    open(os.path.join(DOCS, y, ".pages"), "w", encoding="utf-8").write(f"title: {label}\n")
open(os.path.join(DOCS, ".pages"), "w", encoding="utf-8").write("nav:\n  - index.md\n  - seconde\n  - premiere\n  - terminale\n  - ressources\n")
print("ok")
