# S10 – Raccorder et organiser

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S10 – lundi 8 février 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟢 Guidé |
| **Prérequis** | S08 (trajet physique), S09 (câble RJ45) |
| **Référentiel** | C09 · savoirs : raccordement (niveau 3), éléments actifs (niveau 3) |

> [!NOTE]
> **Question qui guide la séance :** *« Je sais fabriquer un câble. Comment l'installer proprement, brancher deux PC à un switch et savoir si tout va bien ? »* La séance se termine par une **énigme** : les PC sont branchés, les voyants sont verts… et pourtant ils ne se voient pas. La réponse arrive en **S11**.

## 🎯 Objectifs

1. **Monter** une prise murale RJ45 (module keystone) et **brasser** sur un panneau 19″.
2. **Étiqueter** prises, panneau et câbles.
3. **Relier** deux PC à un switch non administrable et **lire les voyants** (lien, activité, vitesse).
4. **Tester la continuité** de l'installation avec un testeur.
5. **Formuler** une hypothèse sur l'énigme finale (« pourquoi ne se voient-ils pas ? »).

## 📚 Contenu

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Prise, panneau de brassage, étiquetage, voyants |
| [🛠️ TP : raccorder, brasser, étiqueter](02-tp.md) | Montage guidé, tests, énigme |
| [`tp/s10-deux-pc-switch.json`](tp/s10-deux-pc-switch.json) | Fichier du simulateur pour l'énigme |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité |
|---|---|
| 0 h 00 – 0 h 20 | **Retour mission**, rappel : « sais-tu retrouver la prise d'un PC ? » |
| 0 h 20 – 0 h 50 | **Mini-cours** : prise, panneau, étiquetage, voyants (cours §1–§3) |
| 0 h 50 – 2 h 15 | **TP A : monter une prise** + **TP B : brasser et étiqueter** |
| 2 h 15 – 2 h 30 | Pause |
| 2 h 30 – 3 h 10 | **TP C : relier deux PC au switch, lire les voyants, test de continuité** |
| 3 h 10 – 3 h 50 | **TP D : l'énigme** (physique, puis simulateur) |
| 3 h 50 – 4 h 00 | Bilan, passeport |

## 🧭 Évaluation

| Critère | Points |
|---|---|
| Prise montée (module serti, couleurs conformes) | 3 |
| Brassage correct (bon cordon, bon port) | 3 |
| Étiquetage clair et cohérent | 2 |
| Test de continuité effectué et noté | 2 |
| Sécurité et rangement | 2 |
| **Total** | **/12** (grille, formatif noté) |

## 🏭 Mission en entreprise

> *Repérer le panneau de brassage ou la baie de l'entreprise (photo si autorisée) et lire les étiquettes.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- Prévoir des **modules keystone à outil de pose (110)** ou **sans outil**, selon l'équipement. Fournir un **schéma de câblage** collé sur le module.
- **L'énigme** : volontairement non résolue en S10. Les PC sont branchés, mais **sans adresse IP configurée** (ou dans des réseaux différents). Laissez les élèves **émettre des hypothèses** (câble ? switch ? Windows ?) puis les noter : on y reviendra en S11.
- Sur de vrais postes Windows, **le pare-feu** peut aussi bloquer le ping : désactiver ou autoriser le ping avant la séance, ou travailler avec le **simulateur**.

</details>
