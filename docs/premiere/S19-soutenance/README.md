# S19 – Soutenance du projet A2

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S19 – lundi 14 juin 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S16 à S18 terminées ; dossier technique rendu |
| **Référentiel** | C06 · C09 · C10 |

> [!NOTE]
> **Question qui guide la séance :** *« Suis-je capable d'expliquer, de montrer et de réparer ce que j'ai construit, devant quelqu'un qui n'était pas là ? »*

## 🎯 Objectifs

1. **Présenter** son projet en **8 minutes** : besoin, solution, choix justifiés.
2. **Démontrer** l'installation par des tests choisis.
3. **Répondre** à des questions techniques.
4. **Dépanner en direct** une panne inconnue (**individuel**).
5. **S'auto-évaluer** sur la grille critériée.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Préparer et tenir une soutenance technique |
| [🛠️ TP : préparation et passage](02-tp.md) | Répétition, passage, auto-évaluation |
| [📝 Grille de soutenance](03-grille-soutenance.md) | Grille critériée alignée sur C06, C09, C10 |

## ⏱️ Déroulé conseillé (4 h)

Une classe de 12 élèves en 4 équipes de 3 : **30 min de préparation**, puis **4 passages de 35 min** (équipe), le reste de la classe **dépanne la maquette de la classe** ou fait une **veille** (voir TP).

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 30 | **Préparation finale** : plan, répartition de la parole, vérification de la maquette | Équipe |
| 0 h 30 – 3 h 30 | **Passages** (35 min par équipe : 8 min de présentation, 7 min de démonstration, 8 min de questions, **12 min de dépannage individuel**) | Équipe / jury |
| 3 h 30 – 4 h 00 | **Auto-évaluation** et retour collectif | Individuel |

## 🧪 Matériel et préparation

- La maquette de **chaque équipe** (fichier `archiplus-final.json`), ou le **corrigé** si besoin.
- Un **jury** : l'enseignant (idéalement avec un second professionnel).
- **Banque de pannes** (voir les notes) pour le dépannage en direct.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Soutenance A2** | [Grille critériée](03-grille-soutenance.md) alignée sur **C06, C09, C10** |
| **Auto-évaluation** | Même grille, remplie par l'élève |

## 🏭 Mission en entreprise

> *Rédiger un **bilan personnel** (une page) ; identifier **3 activités** (R2, R3, R5) à documenter pour le livret.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Banque de pannes pour le dépannage en direct</summary>

À injecter **dans l'ordre de difficulté** dans une copie de la maquette (corrigé de S17). Chaque panne a **une seule cause**.

| # | Panne | Symptôme observé | Injection |
|---|---|---|---|
| 1 | Câble débranché (Fa0/9) | `PC-AT1` « câble déconnecté » | Supprimer le câble `PC-AT1`–`SW1` |
| 2 | Port dans le mauvais VLAN | `PC-AT1` reçoit une adresse du pool invités | `interface fa0/9` → `switchport access vlan 30` |
| 3 | Masque erroné sur le serveur | Le serveur joint `PC-AT1` mais pas les autres réseaux | Mettre `/24` à la place de `/27` sur `SRV` |
| 4 | Passerelle du pool Direction erronée | `PC-DIR` a une adresse, ne sort pas du réseau | Dans le pool Direction, passerelle `.2` au lieu de `.1` |
| 5 | Interface routeur `shutdown` | Tout un service injoignable | `interface gi0/1` → `shutdown` |
| 6 | Enregistrement DNS faux | Le site s'ouvre par adresse, pas par nom | `intranet` → mauvaise adresse |
| 7 | ACL appliquée dans le mauvais sens | Les invités n'ont rien ou tout | `ip access-group … out` au lieu de `in` |
| 8 | Serveur web arrêté | Aucune page, mais le serveur répond au ping | Arrêter le service web |

- **Un tirage par élève** : 12 minutes pour **constater, délimiter, trouver, corriger** ; l'élève **verbalise** sa démarche.
- Les **pannes 1, 2, 6** sont du niveau attendu en Première ; 3 à 8 pour **différencier**.
- La grille est **critériée** : on valorise la **méthode**, pas la vitesse.

</details>

<details markdown="1"><summary>Organisation</summary>

- Si la classe est plus grande, **dédoubler** : un jury par demi-groupe, ou répartir les passages sur **deux séances**.
- Les élèves **non passants** font la **veille technique** (fiche) ou **dépannent** un fichier de panne de S08, S09 ou S11.
- Conserver **les grilles** : elles alimentent le **livret** et le bilan A2 (S20).

</details>
