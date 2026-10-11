# S13 – Recette et accompagnement du client

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S13 – 29 mars 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🔴 Autonome |
| **Prérequis** | Première S18 (recette de projet), Terminale S06 (Wi-Fi), S11–S12 |
| **Référentiel** | C06 · C09 · R1 · R2 |

> [!NOTE]
> **Question qui guide la séance :** *« Comment montrer au client que l'installation est conforme à ce qu'il a demandé, et comment lui expliquer simplement comment s'en servir ? »*

## 🎯 Objectifs

1. **Établir** un cahier de recette (tests, attendus, résultats obtenus, réserves).
2. **Dérouler** la recette sur une installation et **repérer** un écart.
3. **Rédiger** un procès-verbal de réception.
4. **Accompagner** le client : l'écouter, répondre à ses questions, remettre une **notice d'une page**.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Cahier de recette, réserves, procès-verbal ; accompagner le client ; notice |
| [🛠️ TP](02-tp.md) | Recette du Wi-Fi du cabinet Garcia, avec un écart à trouver ; jeu de rôle de réception |
| [📝 Aide-mémoire](03-aide-memoire.md) | Modèles : cahier de recette, procès-verbal, notice |
| [`tp/t13-recette.json`](tp/t13-recette.json) | Simulateur : Wi-Fi du cabinet Garcia installé, avec un écart par rapport au cahier des charges |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « Un artisan finit ton installation électrique : comment sais-tu que c'est bien fait ? » | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : la recette, les réserves, le PV | Classe |
| 0 h 50 – 2 h 00 | **TP A–C** : établir et dérouler la recette | Binôme |
| 2 h 00 – 2 h 15 | Pause |  |
| 2 h 15 – 2 h 45 | **Mini-cours** : accompagner le client | Classe |
| 2 h 45 – 3 h 30 | **TP D–E** : jeu de rôle de réception | Binôme |
| 3 h 30 – 4 h 00 | **TP F** : rédiger la notice d'une page | Individuel |

## 🧪 Matériel et préparation

- Le fichier `t13-recette.json`.
- Les modèles de l'[aide-mémoire](03-aide-memoire.md) imprimés.
- Rôles pour le jeu : « le client » (carte avec ses attentes et ses questions).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 6 contrôles automatiques** après correction | Formatif |
| **Cahier de recette rempli + PV + notice d'une page** ; **jeu de rôle** observé | Grille : tests pertinents, écart repéré, PV complet, langage adapté au client |

## 🏭 Mission en entreprise

> *Collecter des preuves de recette ou de relation client pour le livret.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **L'installation de départ comporte un écart** : l'ACL des invités n'est pas posée, donc les invités **joignent le serveur interne** et **le Wi-Fi du personnel**. Les élèves doivent **le découvrir par leurs tests**, pas par la lecture de la configuration.
- **Ne pas dire** aux élèves quel test échoue. S'ils réussissent tous les tests, c'est qu'**ils n'ont pas testé les interdictions** (tests **négatifs**) : bon moment pour en parler.
- **Jeu de rôle** : le « client » a des attentes précises (« les clients ne doivent pas voir mon serveur ») et **des questions de non-initié** (« c'est quoi un SSID ? »). Un observateur remplit une grille : vocabulaire, écoute, clarté.
- **Notice d'une page** : à destination d'un utilisateur, **sans jargon**. Longueur maximale : **une page**.
- **Lien avec R1/R2** (compétences relationnelles) : ce TP est la meilleure occasion d'**observer** la communication orale.
- Corrigé : `corriges/terminale/T13-corrige.md`, `T13-recette-corrige.json`.

</details>
