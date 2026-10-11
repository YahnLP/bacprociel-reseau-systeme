# S02 – Remise à niveau et découverte du simulateur

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S02 – lundi 14 septembre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟢 Guidé |
| **Prérequis** | S01 (diagnostic) ; adresse IP et réseau vus en Seconde (S11) |
| **Référentiel** | C06 · C09 |

> [!NOTE]
> **Question qui guide la séance :** *« Comment tester un réseau sans casser le vrai ? Et quelles notions de Seconde dois-je remettre à jour pour la suite ? »*

## 🎯 Objectifs

1. **Utiliser le simulateur** : ouvrir un fichier, brancher, configurer, tester, enregistrer.
2. **Lire** une adresse IP avec son masque : **réseau**, **plage**, **diffusion**.
3. **Utiliser** `ping`, `ipconfig` / `ip a` et l'**analyseur de trames** (premier contact).
4. **Combler** les lacunes repérées au diagnostic.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Le simulateur (visite guidée) ; remise à niveau IP ; commandes essentielles |
| [🛠️ TP](02-tp.md) | Visite du simulateur, câblage, test, capture, mise à niveau |
| [🧮 Fiche d'exercices](03-exercices-remise-a-niveau.md) | 12 exercices progressifs sur les adresses (corrigés repliés) |
| [`tp/p02-decouverte.json`](tp/p02-decouverte.json) | Simulateur : 1 switch, 2 PC, 1 serveur ; `PC2` à câbler et configurer |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « Et si on cassait un réseau pour de faux ? » ; présentation du simulateur | Classe |
| 0 h 20 – 1 h 00 | **TP A** : visite guidée de l'interface | Binôme |
| 1 h 00 – 1 h 30 | **Mini-cours** : adresse + masque → réseau (cours §2) | Classe |
| 1 h 30 – 1 h 45 | Pause | |
| 1 h 45 – 2 h 45 | **TP B–C** : câbler, configurer, tester, premier regard sur les trames | Binôme |
| 2 h 45 – 3 h 40 | **TP D** : exercices de remise à niveau, à son rythme | Individuel |
| 3 h 40 – 4 h 00 | Bilan, passeport | |

## 🧪 Matériel et préparation

- Un PC par élève avec un **navigateur** récent (Chrome, Edge, Firefox).
- Le simulateur : [`simulateur-reseau.html`](../../simulateur/simulateur-reseau.html) (fonctionne **hors ligne**).
- Résultats du **QCM de S01** pour constituer des groupes de besoin.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| TP B–C | Contrôle du ping `PC2` ↔ `SRV1` (formatif) |
| Fiche d'exercices | Autocorrection ; relevé des exercices non réussis |

## 🏭 Mission en entreprise

> *Relever le **plan d'adressage** du réseau de l'entreprise (ou en demander une copie) : plages, réseaux, passerelle.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Simulateur** : il fonctionne dans le navigateur, sans installation. Les fichiers `.json` se chargent avec le bouton **Ouvrir** (pas par double-clic).
- **Remise à niveau** : les exercices sont classés (A = facile, B = moyen, C = difficile). Les élèves forts passent directement à C.
- **Ping** : dans le simulateur comme sur Windows, un `ping` qui échoue peut venir d'un pare-feu. Ici, tous les postes répondent.
- Corrigé : `corriges/premiere/P02-corrige.md` et `P02-decouverte-corrige.json`.

</details>
