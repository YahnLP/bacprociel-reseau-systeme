# S17 – Projet A1 (2/2) : tests, recette et dossier

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S17 – lundi 31 mai 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S15 (diagnostic), S16 (installation de l'atelier) |
| **Référentiel** | C06 · C09 · C10 |

> [!NOTE]
> **Question qui guide la séance :** *« Comment prouver au client que son réseau marche… et que tu sais le dépanner ? »*

## 🎯 Objectifs

1. **Dérouler** une fiche de recette complète et **consigner** les résultats.
2. **Dépanner** une panne introduite par le professeur, avec une fiche d'intervention.
3. **Finaliser** le dossier : schéma, plan d'adressage, recette.
4. **Préparer** une démonstration orale de 5 minutes.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Qu'est-ce qu'une recette ? Présenter un projet en 5 minutes |
| [🛠️ TP](02-tp.md) | Recette, panne introduite, dossier, répétition d'oral |
| [✅ Fiche de recette](03-fiche-recette.md) | À remplir pendant les tests (jalon noté) |
| [🗣️ Plan de l'oral](04-plan-oral.md) | Trame de la démonstration de 5 minutes |
| `tp/projet-a1-panne-imprimante.json` | Simulateur : l'atelier **fini**, avec une panne (imprimante) |
| `tp/projet-a1-panne-poste.json` | Simulateur : l'atelier **fini**, avec une autre panne (poste 4) |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 15 | **Reprise** : où en est le projet ? Retour mission entreprise | Classe |
| 0 h 15 – 0 h 45 | **Mini-cours** : la recette, l'oral en 5 minutes | Classe |
| 0 h 45 – 1 h 45 | **TP A** : dérouler la fiche de recette sur la maquette et le matériel | Binôme |
| 1 h 45 – 2 h 00 | Pause | |
| 2 h 00 – 2 h 40 | **TP B** : la panne introduite (une panne du professeur, fiche d'intervention) | Binôme |
| 2 h 40 – 3 h 30 | **TP C** : finaliser le dossier | Binôme |
| 3 h 30 – 4 h 00 | **TP D** : répéter l'oral (devant un autre binôme) | Binôme |

## 🧪 Matériel et préparation

- Les maquettes de S16 de chaque binôme (ou les fichiers corrigés si besoin).
- **Pannes à préparer** : fichiers `tp/projet-a1-panne-*.json`, ou provoquer la panne sur le matériel réel pendant la pause.
- Impression des fiches de recette et d'intervention ([S15](../S15-depannage-n1/03-fiche-intervention.md)).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Jalon noté : recette du projet** | Fiche de recette complétée + panne dépannée (grille ci-dessous) |

| Critère | Points |
|---|---|
| Fiche de recette complète, résultats précis | /6 |
| Panne diagnostiquée dans l'ordre | /4 |
| Fiche d'intervention claire | /4 |
| Dossier complet (schéma, adressage, recette) | /6 |

## 🏭 Mission en entreprise

> *Finaliser le dossier et **répéter l'oral** (5 min) avec le tuteur ou un collègue.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Deux pannes prêtes** : `panne-imprimante` (IP de l'imprimante dans un autre réseau → impression impossible, Internet OK) et `panne-poste` (poste 4 non relié). Les alterner pour limiter les copies.
- **Les partages Windows** ne sont pas simulés ; la recette de la partie « droits » se fait sur postes réels (ou en démonstration).
- Les corrigés des pannes sont dans `corriges/seconde/S17-panne-*-corrige.json` et `S17-corrige.md`.

</details>
