# S16 – Projet A2 (1/3) : étude et préparation

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S16 – lundi 3 mai 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | [Cahier des charges](../S15-revision-lancement/04-cahier-des-charges.md) lu ; S06 à S14 |
| **Référentiel** | C06 · C09 |

> [!NOTE]
> **Question qui guide la séance :** *« Avant de toucher au moindre câble, que dois-je décider et écrire pour que la réalisation se passe sans improviser ? »*

## 🎯 Objectifs

1. **Extraire** du cahier des charges la **matrice des flux** (qui peut joindre quoi).
2. **Découper** 192.168.50.0/24 en **trois sous-réseaux** justifiés.
3. **Établir** le plan de VLAN, le plan d'adressage et le **tableau de câblage**.
4. **Dessiner** un schéma lisible, **lister** le matériel et préparer la baie.
5. **Défendre** son étude lors d'une **revue de conception**.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Méthode d'étude : flux, découpage, VLAN, câblage, baie |
| [🛠️ TP : l'étude](02-tp.md) | Produire le dossier d'étude, étape par étape |
| [📝 Modèle de dossier d'étude](03-modele-dossier.md) | Tableaux à remplir |
| [`tp/p16-projet-depart.json`](tp/p16-projet-depart.json) | Simulateur : matériel posé, **aucun câble, aucune configuration** |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : reprise du cahier des charges, chaque équipe énonce **ses 3 questions** | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : flux, découpage, plan de câblage (§1–§4) | Classe |
| 0 h 50 – 1 h 50 | **TP A–C** : flux, découpage, VLAN et ports | Équipe |
| 1 h 50 – 2 h 05 | Pause | |
| 2 h 05 – 3 h 05 | **TP D–E** : schéma, tableau de câblage, liste du matériel | Équipe |
| 3 h 05 – 3 h 45 | **Revue de conception** avec l'enseignant (≈ 8 min par équipe) | Équipe |
| 3 h 45 – 4 h 00 | Corrections et préparation de S17 | Équipe |

## 🧪 Matériel et préparation

- Simulateur : `tp/p16-projet-depart.json`.
- Papier A3 ou outil de dessin (draw.io, LibreOffice Draw) pour le schéma.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Revue de conception** | Grille en fin de [TP](02-tp.md) : flux, adressage, VLAN, câblage, lisibilité |
| **Dossier d'étude** | Rendu à la fin de la séance (formatif) |

## 🏭 Mission en entreprise

> *Avancer le dossier d'étude : avec le tuteur, **repérer un schéma réseau réel** (même simple) et noter ce qui y est écrit : noms, adresses, VLAN, repérage des câbles.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Plusieurs découpages sont valides.** À la revue, **valider la logique** (blocs alignés, marge, pas de chevauchement) plutôt qu'un résultat unique. Ensuite, **distribuer le plan de référence** ([S17](../S17-projet-2-realisation/00-plan-de-reference.md)) : les contrôles automatiques de S17 s'appuient dessus.
- Les élèves ne connaissent **pas** l'inter-VLAN par une seule interface (Terminale) : le projet utilise donc **une interface du routeur par service** (3 câbles du switch vers le routeur).
- Le fichier de départ pose le matériel **sans câble** : l'équipe vérifie que **rien ne manque** par rapport à sa liste.
- Corrigé : `corriges/premiere/P16-corrige.md` (plan d'adressage, plan de ports, liste de matériel) et `P16-projet-corrige.json` (installation complète).

</details>
