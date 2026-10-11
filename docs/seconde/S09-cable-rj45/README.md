# S09 – Fabriquer un câble RJ45

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S09 – lundi 25 janvier 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟢 Guidé |
| **Prérequis** | S01 (RJ45, sécurité), S08 (trajet physique) |
| **Référentiel** | C09 · savoirs : raccordement (niveau 3), appareils de mesure (niveau 3) |

> [!NOTE]
> **Question qui guide la séance :** *« Pourquoi huit fils, des couleurs précises dans un ordre précis, et comment être sûr qu'un câble est bon ? »*

## 🎯 Objectifs

1. **Décrire** un câble à paires torsadées (4 paires) et **donner** les catégories usuelles (Cat 5e / 6) et la longueur maximale (100 m).
2. **Sertir** un connecteur RJ45 en respectant la norme **T568B** (câble droit).
3. **Tester** un câble avec un testeur et **lire** les défauts (coupure, inversion, court-circuit).
4. **Utiliser** les outils (pince à sertir, dénudeur, testeur) **en sécurité**.

## 📚 Contenu

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Paires torsadées, catégories, T568B, tests |
| [🛠️ TP : fabriquer et tester un câble](02-tp.md) | Pas à pas, grille de conformité, défauts à diagnostiquer |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité |
|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : un câble coupé en deux (on **regarde** les 8 fils), question « pourquoi tordus ? » |
| 0 h 20 – 0 h 55 | **Mini-cours** (§1–§3) : paires, T568B, catégories |
| 0 h 55 – 1 h 15 | **Démonstration** du sertissage (l'enseignant, 3 min, puis les élèves) + sécurité |
| 1 h 15 – 2 h 15 | **TP A : premier câble** (guidé) |
| 2 h 15 – 2 h 30 | Pause |
| 2 h 30 – 3 h 15 | **TP B : tester et dépanner** (câbles défectueux fournis) |
| 3 h 15 – 3 h 50 | **TP C : câble conforme noté** (formatif noté) : chronométré, avec grille |
| 3 h 50 – 4 h 00 | Bilan, passeport |

## 🧪 Matériel

Câble Cat 5e ou 6 (UTP), connecteurs RJ45 (prévoir **2 à 3 fois** plus que nécessaire), pinces à sertir, dénudeurs, ciseaux/coupe-fil, testeur de câble, **2 câbles défectueux** (coupure, inversion), lunettes de protection.

## 🧭 Évaluation

| Critère (grille) | Points |
|---|---|
| Ordre des paires conforme T568B aux **deux** extrémités | 4 |
| Gaine bien engagée dans le connecteur (serre-câble) | 2 |
| Sertissage correct (fils au bout, cuivre visible) | 2 |
| Test OK (8 voyants dans l'ordre) | 2 |
| Sécurité et rangement | 2 |
| **Total** | **/12** (formatif noté) |

## 🏭 Mission en entreprise

> *Observer les câbles et prises réseau de l'entreprise : types de prises, étiquetage, baie ou coffret.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- Le **câble droit en T568B** est le plus courant. Le T568A existe : un câble avec un bout en T568A et l'autre en T568B est **croisé** (peu utile aujourd'hui car les ports sont auto-MDIX). Ne pas trop insister.
- Les erreurs fréquentes : **gaine non engagée** (câble qui sort), **fils non aplatis**, **fils trop longs** (le connecteur ne ferme pas), **ordre faux**. Prévoir un test dès le **premier** câble.
- **Sécurité** : coupe loin du corps, lunettes pour la coupe, chutes jetées.
- Le **nombre de connecteurs** nécessaire est souvent sous-estimé (un connecteur raté = un connecteur perdu).

</details>
