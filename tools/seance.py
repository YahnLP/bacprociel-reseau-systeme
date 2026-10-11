#!/usr/bin/env python3
"""Fabrique les fichiers d'une séance (README, cours, TP, aide-mémoire, corrigé) à partir d'une description.
Utilisé pour la Terminale : python3 tools/content/t06.py"""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
cur = {(r["year"], r["code"]): r for r in json.load(open(os.path.join(ROOT, "tools", "curriculum.json"), encoding="utf-8"))}
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
AUTO = {"Guidé": "🟢 Guidé", "Semi-guidé": "🟡 Semi-guidé", "Autonome": "🔴 Autonome"}


def fr(d):
    y, m, j = map(int, d.split("-"))
    return f"{'1er' if j == 1 else j} {MOIS[m-1]} {y}"


def w(path, txt):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(txt.strip("\n") + "\n")


def details(q, a):
    return f"{q}\n\n<details markdown=\"1\"><summary>Voir la réponse</summary>\n\n{a}\n\n</details>\n"


def seance(code, S):
    r = cur[("terminale", code)]
    fold = f"{code}-{r['slug']}"
    base = os.path.join(ROOT, "docs", "terminale", fold)
    n = code[1:]
    files = S.get("fichiers", [])
    # ---- README
    rows = "\n".join(f"| {a} | {b} |" for a, b in [("[📖 Cours élève](01-cours.md)", S["cours_role"]), ("[🛠️ TP](02-tp.md)", S["tp_role"]), ("[📝 Aide-mémoire](03-aide-memoire.md)", S["memo_role"])] + [(f"[`tp/{f}`](tp/{f})", d) for f, d in files] + S.get("autres", []))
    deroule = "\n".join(f"| {a} | {b} | {c} |" for a, b, c in S["deroule"])
    objs = "\n".join(f"{i+1}. {o}" for i, o in enumerate(S["objectifs"]))
    ev = "\n".join(f"| {a} | {b} |" for a, b in S["eval"])
    notes = "\n".join(f"- {x}" for x in S["notes"])
    mat = "\n".join(f"- {x}" for x in S["materiel"])
    readme = f"""# {code} – {r['theme']}

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | {code} – {fr(r['date'])} (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | {AUTO[r['auto']]} |
| **Prérequis** | {S['prerequis']} |
| **Référentiel** | {r['ref']} |

> [!NOTE]
> **Question qui guide la séance :** *« {S['question']} »*

## 🎯 Objectifs

{objs}

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
{rows}

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
{deroule}

## 🧪 Matériel et préparation

{mat}

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
{ev}

## 🏭 Mission en entreprise

> *{r['ent']}*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

{notes}
- Corrigé : `corriges/terminale/T{n}-corrige.md`{S.get('corriges_extra', '')}.

</details>
"""
    w(os.path.join(base, "README.md"), readme)
    # ---- cours
    sauras = "\n".join(f"- [ ] {x}" for x in S["sauras"])
    secs = ""
    for i, s in enumerate(S["sections"], 1):
        secs += f"\n---\n\n## {i}. {s['h']}\n\n### 🤔 Avant de lire : à ton avis ?\n\n" + details(s["q"], s["a"])
        secs += f"\n### 💡 L'idée\n\n{s['idee']}\n"
        if s.get("img"):
            secs += f"\n![{s['img'][1]}](images/{s['img'][0]})\n"
        secs += f"\n### ✅ Vérifie que tu as compris\n\n" + details(s["c"], s["r"])
    retenir = "\n".join(f"- {x}" for x in S["retenir"])
    cours = f"""# 📖 Cours – {S['cours_titre']}

*Bac Pro CIEL – Terminale – E31 – {code}*

> [!IMPORTANT]
> **Une idée à la fois.** Réponds à la question **avant** de déplier la réponse.

## 🎯 À la fin de ce cours, tu sauras

{sauras}
{secs}
---

## 🧠 À retenir

{retenir}
"""
    w(os.path.join(base, "01-cours.md"), cours)
    # ---- TP
    tp = f"""# 🛠️ TP – {S['tp_titre']}

*Bac Pro CIEL – Terminale – E31 – {code} – {S['tp_format']}*

> [!NOTE]
> **Mission.** {S['mission']}
>
> **Temps prévu :** {S['tp_temps']}. **Prérequis :** [cours {code}](01-cours.md) lu ; [aide-mémoire](03-aide-memoire.md).

{S['tp']}
"""
    w(os.path.join(base, "02-tp.md"), tp)
    w(os.path.join(base, "03-aide-memoire.md"), f"# 📝 Aide-mémoire – {S['memo_titre']}\n\n{S['memo']}")
    cor = f"# Corrigé – Terminale {code}\n\n{S['corrige']}\n"
    w(os.path.join(ROOT, "corriges", "terminale", f"T{n}-corrige.md"), cor)
    for sub in ("images", "tp"):
        os.makedirs(os.path.join(base, sub), exist_ok=True)
    return base
