# S16 – Chantier complet d'entraînement n°2

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S16 – 17 mai 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🔴 Autonome |
| **Prérequis** | S15 (chantier n°1) ; fiche d'erreurs de S15 |
| **Référentiel** | C06 · C09 · C10 |

> [!NOTE]
> **Question qui guide la séance :** *« Suis-je capable, à la fois, de dépanner et de rendre compte, comme à l'épreuve ? »*

## 🎯 Objectifs

1. **Diagnostiquer** une installation existante tombée en panne (plusieurs causes).
2. **Corriger** avec méthode et **prouver** le retour à la normale.
3. **Rédiger** un compte rendu d'intervention.
4. **Se positionner** sur la grille et **bâtir un plan de travail individuel**.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Méthode pour un chantier de dépannage ; corriger sa fiche d'erreurs de S15 |
| [🛠️ TP](02-tp.md) | Le cabinet Vidal rappelle : plusieurs pannes à diagnostiquer |
| [📝 Aide-mémoire](03-aide-memoire.md) | Check-list de dépannage et de compte rendu |
| [`tp/t16-chantier-depart.json`](tp/t16-chantier-depart.json) | Simulateur : l'installation de S15, en panne |
| [📄 Dossier de la demande](03-dossier-rappel.md) | Appel du client et attentes |
| [📊 Grille d'entraînement](04-grille-entrainement.md) | Grille à blanc |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Briefing** et rappel des erreurs fréquentes de S15 | Classe |
| 0 h 20 – 3 h 20 | **Chantier de dépannage** (3 h) en autonomie, avec **compte rendu** | Individuel |
| 3 h 20 – 4 h 00 | **Correction** et **plan de travail individuel** | Classe / individuel |

## 🧪 Matériel et préparation

- Le fichier `t16-chantier-depart.json`.
- Le **dossier de la demande** imprimé, l'aide-mémoire, la fiche « 15 points essentiels », la documentation d'appui.
- Les **fiches d'erreurs** de S15.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 8 contrôles automatiques** | Formatif ; preuve de dépannage |
| **Compte rendu** + **grille d'entraînement** | Positionnement à blanc |

## 🏭 Mission en entreprise

> *Relire les erreurs des chantiers d'entraînement ; préparer l'évaluation.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Trois causes** : 1) le port de l'imprimante (`Fa0/3`) a été déplacé dans le VLAN 20 ; 2) la clé Wi-Fi du portable patient est erronée (`Patient#2027` au lieu de `Patients#2027`) ; 3) la liste d'accès du NAT ne couvre plus que le VLAN 10 : les patients n'ont **pas Internet** même une fois connectés. Le 3ᵉ défaut n'apparaît **qu'après** la correction du 2ᵉ : **c'est le piège** de la double panne.
- **Corrigé** : `corriges/terminale/T16-corrige.md`, `T16-chantier-corrige.json`.
- **Plan de travail individuel** : à partir de la grille et de la fiche d'erreurs, **trois points** à retravailler avant S17.
- **Conditions de l'épreuve** : seul(e), 3 h, documentation d'appui, comme S15.
- Corrigé : `corriges/terminale/T16-corrige.md`, `T16-chantier-corrige.json`.

</details>
