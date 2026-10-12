# S01 – Diagnostic A3 et retour de PFMP

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S01 – lundi 24 août 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🔴 Autonome |
| **Prérequis** | Année de Première ; PFMP |
| **Référentiel** | C06 · C09 · C10 |

> [!NOTE]
> **Question qui guide la séance :** *« Où en suis-je, moi, au début de l'année de l'épreuve ? Qu'est-ce que je sais faire **seul**, et qu'est-ce qui me manque pour le livret ? »*

## 🎯 Objectifs

1. **Réaliser** un **mini-chantier de positionnement** (câbler, configurer, tester, documenter) en autonomie.
2. **Faire le point** sur la PFMP : activités déjà documentées, lacunes du livret.
3. **Comprendre** les modalités de l'épreuve E31 et la **grille nationale**.
4. **Établir** son **plan de remédiation** personnel.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Le chantier en 6 étapes, la grille d'évaluation, le livret |
| [🛠️ TP](02-tp.md) | Mini-chantier, retour de PFMP, plan de remédiation |
| [📝 Fiche de positionnement](03-fiche-positionnement.md) | Grille de lecture du mini-chantier |
| [📝 Point sur le livret](04-point-livret.md) | Activités documentées / lacunes |
| [`tp/t01-mini-chantier.json`](tp/t01-mini-chantier.json) | Simulateur : cabinet médical, matériel posé, rien câblé |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 15 | **Accueil** : l'année en un schéma, le principe du diagnostic (non noté) | Classe |
| 0 h 15 – 2 h 15 | **Mini-chantier de positionnement** (individuel, **sans aide**) | Individuel |
| 2 h 15 – 2 h 30 | Pause | |
| 2 h 30 – 3 h 00 | **Mini-cours** : les modalités de l'E31, la grille nationale | Classe |
| 3 h 00 – 3 h 40 | **Retour de PFMP** et point sur le livret | Binôme puis classe |
| 3 h 40 – 4 h 00 | **Plan de remédiation** personnel | Individuel |

## 🧪 Matériel et préparation

- Simulateur : `tp/t01-mini-chantier.json`.
- Le **livret** de chaque élève ; leurs documents de PFMP.
- Imprimer la [fiche de positionnement](03-fiche-positionnement.md) (une par élève).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Mini-chantier** | **Diagnostic non noté** : 7 contrôles automatiques + fiche de positionnement |
| **Plan de remédiation** | Individuel, à valider avec l'enseignant |

## 🏭 Mission en entreprise

> *Rassembler les **preuves déjà réalisées** (procès-verbaux, schémas, comptes rendus) pour le livret.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Diagnostic, pas évaluation** : annoncer clairement que rien n'est noté. L'**absence d'aide** est le but : observer ce que l'élève fait **seul**.
- Le fichier de départ pose le matériel **sans câble** ; compter **7 contrôles** automatiques (adresses DHCP, nom, imprimante, sécurité du switch, sauvegarde). Le **mot de passe** du switch est libre (le contrôle vérifie la **présence** d'un `enable secret`).
- **Modalités de l'E31** : le cours rappelle le cadre : **épreuve pratique de 3 h, coefficient 5**, plateau technique, documentation d'appui autorisée, C06/C09/C10. **Compléter** avec le calendrier et le déroulé précis de l'établissement ; les textes officiels font foi.
- Le **livret** : s'appuyer sur les activités **R2, R3, R5** ; repérer les élèves **sans aucune activité documentée**.
- Corrigé : `corriges/terminale/T01-corrige.md` et `T01-mini-chantier-corrige.json`.

</details>
