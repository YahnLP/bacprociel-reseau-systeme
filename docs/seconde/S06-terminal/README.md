# S06 – Le terminal : premiers pas

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S06 – lundi 23 novembre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟢 Guidé |
| **Prérequis** | S04 (Windows) et S05 (Linux, arborescence, `sudo`) |
| **Référentiel** | C10 · savoir : lignes de commande (niveau 3) |

> [!NOTE]
> **Question qui guide la séance :** *« Un technicien réseau passe beaucoup de temps devant une fenêtre noire. Pourquoi ? Et comment s'y retrouver quand on débute ? »*

## 🎯 Objectifs

À la fin de la séance, l'élève est capable de :

1. **Lire un prompt** et dire dans quel dossier il se trouve.
2. **Se déplacer** (`cd`), **lister** (`ls` / `dir`), **créer** (`mkdir`), **copier**, **déplacer**, **supprimer** (avec prudence).
3. **Distinguer** chemin absolu et chemin relatif.
4. **Obtenir de l'aide** (`--help`, `man`, `/?`) au lieu de bloquer.
5. **Afficher l'identité réseau** d'un poste (`hostname`, `ipconfig` / `ip a`) et **tester** un voisin avec `ping`.
6. **Rédiger sa fiche mémo** personnelle de commandes.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Anatomie d'une commande, déplacements, fichiers, aide, premières commandes réseau |
| [🛠️ TP : chasse au trésor](02-tp.md) | Parcours guidé dans l'arborescence avec 2 scripts de préparation (Windows et Linux) |
| [🌐 TP simulateur : qui suis-je sur le réseau ?](03-tp-reseau.md) | `hostname`, `ipconfig`, `ip a`, `ping` dans le simulateur |
| [📝 Fiche mémo](04-fiche-memo.md) | Modèle à compléter et à garder |
| 📦 Ressources |  [`creer-tresor.sh`](ressources/creer-tresor.sh) (Linux), [`creer-tresor.cmd`](ressources/creer-tresor.cmd) (Windows) |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : on donne la même consigne en cliquant (explorateur) et en terminal ; on compare | Démonstration |
| 0 h 20 – 1 h 00 | **Mini-cours** : prompt, commande/option/argument, chemins (cours §1–§2) avec exercices flash | Cours + questions |
| 1 h 00 – 2 h 15 | **TP chasse au trésor, niveau Linux ou Windows** (cours §3–§4 au fil des étapes) | Binôme |
| 2 h 15 – 2 h 30 | Pause | |
| 2 h 30 – 3 h 15 | **Même chasse sur l'autre système** (comparer les commandes) | Binôme |
| 3 h 15 – 3 h 50 | **TP simulateur** : identité réseau, `ping` entre deux postes | Binôme |
| 3 h 50 – 4 h 00 | Fiche mémo, bilan | Individuel |

## 🧪 Matériel et préparation

- Un poste Windows et la VM Ubuntu de S05 (ou deux machines).
- Fichiers [`creer-tresor.sh`](ressources/creer-tresor.sh) et [`creer-tresor.cmd`](ressources/creer-tresor.cmd) à distribuer.
- [Simulateur réseau](../../simulateur/simulateur-reseau.html) et le fichier [`s06-terminal-reseau.json`](tp/s06-terminal-reseau.json).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| Défi terminal | Les 7 lettres trouvées + commandes expliquées à l'oral (formatif) |
| Fiche mémo | 10 commandes minimum, avec un exemple chacune |
| Compréhension | « Où suis-je ? Comment remonter d'un dossier ? Pourquoi prudence avec `rm` / `del` ? » |

## 🏭 Mission en entreprise

> *Observer les commandes ou outils qu'un collègue utilise pour diagnostiquer (`ipconfig`, `ping`…) et noter une situation.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1">
<summary>Points d'attention</summary>

- Les scripts de chasse au trésor sont générés par `tools/tresor/gen.py` : la chaîne d'indices est identique sous Linux et Windows. Le texte n'a **pas d'accents** (compatibilité de l'invite de commandes). Le mot final est **CABLAGE**.
- Le script Windows n'a pas pu être testé ici sur une vraie machine Windows : **à essayer une fois avant la séance**.
- Interdire l'explorateur graphique pendant la chasse : tout se fait au terminal.
- Insister sur la **prudence avec la suppression** (pas de corbeille) et sur l'habitude *« je regarde où je suis avant d'agir »* (`pwd` / `cd` seul).
- Beaucoup d'élèves croient que la touche `Tab` est un luxe : montrez la **complétion automatique** dès le début.

</details>
