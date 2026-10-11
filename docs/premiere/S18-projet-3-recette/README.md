# S18 – Projet A2 (3/3) : recette et dossier technique

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S18 – lundi 31 mai 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S17 terminée ; fichier `archiplus-final.json` |
| **Référentiel** | C06 · C10 |

> [!NOTE]
> **Question qui guide la séance :** *« Comment **prouver** au client que l'installation fait ce qui était demandé, et que la prochaine personne pourra la dépanner ? »*

## 🎯 Objectifs

1. **Dérouler** un **cahier de recette** : tests, résultats attendus, résultats obtenus, preuves.
2. **Dépanner** une installation avec **3 pannes** glissées, avec méthode.
3. **Assembler** le **dossier technique** : schémas, plans, configurations sauvegardées.
4. **Rendre compte** : conclure la recette par des **réserves** claires.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Recette, preuves, méthode de dépannage, dossier technique |
| [🛠️ TP](02-tp.md) | Recette de la maquette, dépannage de 3 pannes, dossier |
| [📝 Cahier de recette (modèle)](03-cahier-de-recette.md) | 14 tests à remplir |
| [`tp/p18-panne.json`](tp/p18-panne.json) | Simulateur : l'installation avec **3 pannes** |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : un client signe une recette sans la lire… que risque-t-on ? | Classe |
| 0 h 20 – 0 h 45 | **Mini-cours** : recette et méthode de dépannage | Classe |
| 0 h 45 – 1 h 55 | **TP A** : recette de **sa** maquette (cahier de recette) | Équipe |
| 1 h 55 – 2 h 10 | Pause | |
| 2 h 10 – 3 h 10 | **TP B** : dépannage des **3 pannes** (fichier de l'enseignant) | Équipe |
| 3 h 10 – 4 h 00 | **TP C** : dossier technique, conclusion de la recette ; **jalon noté** | Équipe |

## 🧪 Matériel et préparation

- `archiplus-final.json` de chaque équipe, **ou** le corrigé fourni par l'enseignant.
- `tp/p18-panne.json` (la maquette avec les pannes).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Jalon noté : recette + dossier** | Cahier de recette rempli (14 tests, preuves) + dossier technique complet |
| **Dépannage** | 3 pannes trouvées et corrigées, **méthode** écrite |

## 🏭 Mission en entreprise

> *Préparer la soutenance (plan, supports) ; **répéter** devant le tuteur en 10 minutes chrono.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- Les **3 pannes** : (1) `Fa0/10` de `PC-AT2` dans le **VLAN 30** au lieu de 20 ; (2) **relais DHCP absent** sur `Gi0/0` (Direction sans adresse) ; (3) **règle DNS oubliée** dans l'ACL invités (le site s'ouvre par adresse mais pas par nom).
- **Piège d'ordre** : corriger le **VLAN** change le DHCP de `PC-AT2` ; il faut `ipconfig /renew` après chaque correction.
- **Correction de l'ACL** : insérer la règle avec un **numéro de séquence** (`25 permit …`) **avant** le `deny`. Beaucoup d'élèves ajoutent la règle **après** le `deny` (inactive).
- Le switch a un **`enable secret`** : le mot de passe est `Archi#2027` (le donner si besoin).
- Corrigé : `corriges/premiere/P18-corrige.md` et `P18-panne-corrige.json`.

</details>
