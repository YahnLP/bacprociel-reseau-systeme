# S12 – Dépanner (2) : réparer et rendre compte

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S12 – 15 mars 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🔴 Autonome |
| **Prérequis** | Terminale S07 (sauvegardes), S11 (démarche de dépannage) |
| **Référentiel** | R5 · C10 · C06 |

> [!NOTE]
> **Question qui guide la séance :** *« Un équipement est mort chez le client. Comment le remplacer vite, sans rien oublier, et comment rendre compte à ceux qui n'étaient pas là ? »*

## 🎯 Objectifs

1. **Remplacer** un équipement (switch) et **restaurer** sa configuration.
2. **Vérifier** le retour à la normale avec des **tests** précis.
3. **Rédiger** un compte rendu d'intervention exploitable.
4. **Décider** quand et comment **passer la main**.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Remplacer, restaurer, vérifier ; compte rendu ; escalade |
| [🛠️ TP](02-tp.md) | PME Delmas : le switch a grillé, remplacement et restauration, compte rendu |
| [📝 Aide-mémoire](03-aide-memoire.md) | Procédure de remplacement, modèle de compte rendu, règles d'escalade |
| [`tp/t12-remplacement.json`](tp/t12-remplacement.json) | Simulateur : switch de remplacement, déjà câblé, VIERGE |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « Le switch fume. Tu as 30 minutes. Que fais-tu d'abord ? » | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : remplacer, restaurer, vérifier | Classe |
| 0 h 50 – 2 h 00 | **TP A–C** : restauration du switch | Binôme |
| 2 h 00 – 2 h 15 | Pause |  |
| 2 h 15 – 2 h 45 | **Mini-cours** : compte rendu et escalade | Classe |
| 2 h 45 – 3 h 30 | **TP D–E** : compte rendu, cas d'escalade | Individuel |
| 3 h 30 – 4 h 00 | **Jeu de rôle** : passer la main par téléphone | Binôme |

## 🧪 Matériel et préparation

- Le fichier `t12-remplacement.json`.
- [Aide-mémoire](03-aide-memoire.md) imprimé.
- Si possible : un vrai switch du plateau pour **rejouer** la restauration à la main.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 5 contrôles automatiques** (4 tests + sauvegarde) | Formatif |
| **Compte rendu d'intervention** + **jeu de rôle d'escalade** | Grille : faits, tests, cause, action, résultat, clarté de la transmission |

## 🏭 Mission en entreprise

> *Rédiger un compte rendu d'intervention réel ou participer à une recette (avec accord du tuteur).*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Rappel :** la sauvegarde utilisée est celle qui aurait été faite en [S07](../S07-maj-sauvegardes/README.md). Si un binôme n'a pas sa sauvegarde, le TP est l'occasion de comprendre pourquoi elle est **indispensable**.
- **Après restauration**, le poste `PC-CPT` doit **renouveler son bail DHCP** (`ipconfig /renew`) car il n'avait plus d'adresse pendant la panne.
- **Le jeu de rôle** (partie E) : un élève est « le technicien » qui appelle, un autre « le responsable / le constructeur ». Le technicien doit tout dire **sans** être relancé : symptôme, tests, ce qu'il a fait.
- **Limite du simulateur :** pas de vraie « panne matérielle » (fumée, ventilateur) : on la représente par un switch **vierge** déjà câblé.
- Corrigé : `corriges/terminale/T12-corrige.md`, `T12-remplacement-corrige.json`.

</details>
