# S15 – Chantier complet d'entraînement n°1

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S15 – 26 avril 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🔴 Autonome |
| **Prérequis** | Tout le parcours Terminale S01–S14 ; fiche « 15 points essentiels » (S14) |
| **Référentiel** | C06 · C09 · C10 |

> [!NOTE]
> **Question qui guide la séance :** *« Suis-je capable de mener un chantier complet, seul(e), dans les conditions de l'épreuve ? »*

## 🎯 Objectifs

1. **Conduire** un chantier complet en **3 heures** : étudier, préparer, installer, configurer, tester, documenter.
2. **Justifier** ses choix (adressage, VLAN, sécurité).
3. **Rédiger** une recette et un compte rendu.
4. **Se positionner** sur la grille d'entraînement et **identifier** ses erreurs.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Méthode pour réussir un chantier (gestion du temps, preuves, check-list) |
| [🛠️ TP](02-tp.md) | Cabinet dentaire Vidal : chantier complet depuis une installation vierge |
| [📝 Aide-mémoire](03-aide-memoire.md) | Check-list de chantier et de preuves |
| [`tp/t15-chantier-depart.json`](tp/t15-chantier-depart.json) | Simulateur : matériel posé, aucun câble, aucune configuration |
| [📄 Dossier client](03-dossier-client.md) | Cahier des charges et plan d'adressage à compléter |
| [📊 Grille d'entraînement](04-grille-entrainement.md) | Grille à blanc (auto-évaluation et évaluation) |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Briefing** : règles, documents autorisés, critères | Classe |
| 0 h 20 – 3 h 20 | **Chantier** (3 h) en autonomie, **sans aide** de l'enseignant (une « question jokers » possible) | Individuel |
| 3 h 20 – 4 h 00 | **Correction collective** et fiche d'erreurs individuelle | Classe / individuel |

## 🧪 Matériel et préparation

- Le fichier `t15-chantier-depart.json` (ouvert au départ).
- Le **dossier client** imprimé, l'aide-mémoire, la **fiche « 15 points essentiels »** (si autorisée), la documentation d'appui (fiches mémo, documentation constructeur).
- Un chronomètre visible de la classe.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 8 contrôles automatiques** | Formatif ; sert de preuve de réalisation |
| **Grille d'entraînement** + **recette** + **compte rendu** | Positionnement à blanc, sans note certificative |

## 🏭 Mission en entreprise

> *Relire les fiches mémo et les commandes ; mettre à jour le livret.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Conditions de l'épreuve** : **seul(e)**, **3 h**, documentation d'appui **autorisée**. L'enseignant observe et remplit la grille ; il n'aide pas (une question « joker » est tolérée pour débloquer).
- **Correction automatique :** les 8 contrôles du simulateur renseignent sur la **réalisation technique** ; ils ne remplacent pas l'évaluation de la **démarche** et des **preuves écrites**.
- **Solution de référence** : `corriges/terminale/T15-corrige.md` et `T15-chantier-corrige.json`. Le **filtrage patients** est réalisé par une **ACL** sur la sous-interface du VLAN 20.
- **Piège possible** : une ACL terminée par `deny ip any any` **sans** `permit udp any eq 68 any eq 67` empêche les patients d'obtenir une **adresse** (le DHCP est bloqué). La solution de référence autorise le DHCP et laisse passer le reste ; à signaler lors de la correction si un élève a choisi un `deny` final.
- **Dossier** : le plan d'adressage est **à compléter** par l'élève (partie du travail évalué).
- Corrigé : `corriges/terminale/T15-corrige.md`, `T15-chantier-corrige.json`.

</details>
