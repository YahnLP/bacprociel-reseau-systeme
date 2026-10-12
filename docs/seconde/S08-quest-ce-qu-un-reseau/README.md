# S08 – Qu'est-ce qu'un réseau ?

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S08 – lundi 11 janvier 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟢 Guidé |
| **Prérequis** | S01 (connecteurs), S06 (terminal : `ipconfig`, `ping`) |
| **Référentiel** | C06 · C09 · savoirs : schémas de réseaux (niveau 3), architectures (niveau 2) |

> [!NOTE]
> **Question qui guide la séance :** *« Quand je clique sur un site, par où passent mes données dans le bâtiment, et comment le dessiner ? »* On part du **réel** (suivre les câbles) pour arriver au **schéma**.

## 🎯 Objectifs

1. **Suivre** le trajet physique : prise murale → panneau de brassage → switch → routeur → Internet.
2. **Utiliser le vocabulaire** : topologie (étoile), client, serveur, switch, routeur, box, borne Wi-Fi, LAN, WAN, Internet, débit.
3. **Dessiner** le schéma du réseau de la salle (à la main, puis avec un logiciel).
4. **Retrouver** ce schéma dans le simulateur et **interpréter** ce qu'on y observe.

## 📚 Contenu

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Réseau, vocabulaire, topologies, LAN / WAN / Internet, lire et dessiner un schéma |
| [🛠️ TP : suivre les câbles et dessiner](02-tp.md) | Enquête dans le bâtiment, schéma papier, schéma numérique, simulateur |
| [`tp/s08-reseau-salle.json`](tp/s08-reseau-salle.json) | Fichier du simulateur : un petit réseau complet qui fonctionne |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité |
|---|---|
| 0 h 00 – 0 h 20 | **Restitution du voyage** (15 min, photos des équipements vus à Paris) + accroche : « par où passent mes données ? » |
| 0 h 20 – 0 h 50 | **Mini-cours** : trajet physique et vocabulaire (cours §1–§2, dont la topologie en étoile) |
| 0 h 50 – 2 h 15 | **TP A : enquête** dans le bâtiment (suivre le câble) + **TP B : schéma papier** |
| 2 h 15 – 2 h 30 | Pause |
| 2 h 30 – 3 h 15 | **TP C : schéma numérique** (draw.io ou équivalent) |
| 3 h 15 – 3 h 50 | **TP D : simulateur** : retrouver le réseau, observer |
| 3 h 50 – 4 h 00 | Bilan, passeport |

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| Schéma légendé du réseau de la salle | Grille : tous les équipements, câbles, légende, étiquettes (formatif) |

## 🏭 Mission en entreprise

> *Faire un schéma, même approximatif, du réseau de l'entreprise : box, switch, postes, imprimantes.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- Prévoir l'**accès à la baie** (porte ouverte, sous surveillance) et un **plan du bâtiment** de la salle.
- Les élèves confondent **switch, routeur et box** : le cours donne une règle simple (*le switch relie les machines d'un même réseau ; le routeur relie des réseaux différents ; la box fait les deux, plus le Wi-Fi*).
- Le fichier simulateur `s08-reseau-salle.json` fonctionne **sans rien configurer** : c'est volontaire (observation avant configuration).
- Les noms et adresses de la partie « Internet » du simulateur sont **fictifs** (plages réservées à la documentation).

</details>
