# S05 – Découvrir Linux

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S05 – lundi 2 novembre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟢 Guidé |
| **Prérequis** | S04 : rôle d'un OS, installation guidée de Windows (la démarche est la même) |
| **Référentiel** | C09 · C10 · savoir : systèmes UNIX / Linux (niveau 2) · mises à jour |

> [!NOTE]
> **Question qui guide la séance :** *« Windows n'est pas le seul système d'exploitation. Qu'est-ce que Linux, pourquoi est-il partout (serveurs, box, téléphones) et comment s'en sert-on ? »*

## 🎯 Objectifs

À la fin de la séance, l'élève est capable de :

1. **Expliquer** ce qu'est Linux (noyau + distribution) et **citer 3 endroits** où on le trouve.
2. **Installer** Ubuntu (ou Debian) dans une machine virtuelle en suivant une fiche.
3. **Se repérer** dans le bureau et dans l'**arborescence** (`/`, `/home`, `/etc`…).
4. **Installer un logiciel** et **mettre à jour** le système avec `apt`.
5. **Comparer** Windows et Linux dans un tableau qu'il construit lui-même.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Linux, distributions, arborescence, utilisateurs, `apt` |
| [🛠️ TP guidé](02-tp.md) | Installer la VM, explorer, installer un logiciel, comparer avec Windows |
| [📊 Tableau comparatif](03-comparatif.md) | Fiche à compléter pendant le TP |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : retour mission entreprise (« Linux chez nous ? »). Devinette : *où y a-t-il du Linux autour de vous ?* (box, téléphone Android, serveurs…) | Oral |
| 0 h 20 – 0 h 50 | **Mini-cours 1** : noyau, distribution, bureau (cours §1–§2) | Cours + questions |
| 0 h 50 – 2 h 00 | **TP partie A** : créer la VM et installer Ubuntu | Binôme |
| 2 h 00 – 2 h 15 | Pause | |
| 2 h 15 – 3 h 00 | **TP partie B** : explorer le bureau, l'arborescence, les utilisateurs (cours §3) | Binôme |
| 3 h 00 – 3 h 40 | **TP partie C** : installer un logiciel, mettre à jour avec `apt` (cours §4) | Binôme |
| 3 h 40 – 4 h 00 | **Tableau comparatif** Windows / Linux, bilan oral | Individuel |

## 🧪 Matériel et préparation

- Un poste avec **VirtualBox** (ou équivalent) et l'**ISO Ubuntu Desktop 24.04 LTS** (ou Debian 12 avec bureau), **déjà téléchargés** (le téléchargement prend du temps).
- Machines virtuelles : 4 Go de RAM, 25 Go de disque, accès réseau en **NAT**.
- Accès Internet pour `apt`.

## 🧭 Évaluation

| Quoi | Comment | Quand |
|---|---|---|
| Installation + mise à jour | Checklist validée (TP) | Fin de séance |
| Tableau comparatif | Au moins 6 lignes justes, remplies par l'élève | Fin de séance |
| Compréhension orale | « Où est ton dossier personnel sous Linux ? Pourquoi `sudo` ? » | Fin de séance |

## 🏭 Mission en entreprise

> *Repérer si l'entreprise utilise Linux (serveur, NAS, box, objets connectés) ; sinon poser la question à un collègue.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1">
<summary>Points d'attention</summary>

- Sur une **machine virtuelle**, « effacer le disque » est sans risque : c'est un fichier. Profitez-en pour **rappeler le contraste** avec le PC réel de S04 (sauvegarde d'abord).
- Les élèves découvriront le terminal à la **séance suivante (S06)**. Ici, on donne les commandes `apt` à **copier** et on explique ce qu'elles font : c'est une première exposition volontairement guidée.
- Prévoir un snapshot de la VM juste après l'installation pour dépanner vite.
- Si l'installateur Ubuntu change d'écran d'une version à l'autre, les étapes de la fiche restent valables dans leur logique (langue, clavier, disque, compte).

</details>
