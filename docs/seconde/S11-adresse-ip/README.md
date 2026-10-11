# S11 – Donner une adresse à chaque machine (IP)

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S11 – lundi 1ᵉʳ mars 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S06 (`ipconfig`, `ping`), S10 (l'énigme : lien établi ≠ conversation) |
| **Référentiel** | C06 · C09 · savoir : IPv4 (niveau 3) |

> [!NOTE]
> **Question qui guide la séance :** *« Pourquoi nos deux PC de S10 ne se voyaient-ils pas ? »* Réponse : **ils n'avaient pas d'adresse**. On apprend à en **donner**, à les **lire**, et à **trouver les erreurs**.

## 🎯 Objectifs

1. **Expliquer** pourquoi chaque machine a besoin d'une **adresse IP** (analogie de la rue).
2. **Lire** un octet comme **8 interrupteurs** et **convertir** quelques valeurs (192, 168, 255, 0…).
3. **Décrire** une adresse IPv4 en décimal pointé et **le masque 255.255.255.0 (/24)** : adresse de **réseau**, de **diffusion**, **plage utilisable**.
4. **Reconnaître** une adresse **privée**.
5. **Configurer** une IP **statique** sous Windows et sous Linux et **tester** avec `ping`.
6. **Diagnostiquer** trois erreurs : adresse dans un autre réseau, mauvais masque, doublon ; **comprendre** pourquoi le pare-feu bloque parfois le ping.

## 📚 Contenu

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Adresse IP, octet, masque /24, plage, privé, configuration, erreurs |
| [🛠️ TP : l'adressage](02-tp.md) | Cartes binaires, plan d'adressage, simulateur, vrais postes, chasse aux erreurs |
| [`tp/s11-adressage-vierge.json`](tp/s11-adressage-vierge.json) | Simulateur : 3 postes à configurer |
| [`tp/s11-erreurs.json`](tp/s11-erreurs.json) | Simulateur : 4 postes, 3 erreurs à trouver |
| [📝 Tableau d'adressage](03-tableau-adressage.md) | Modèle à remplir et à rendre |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité |
|---|---|
| 0 h 00 – 0 h 20 | **Retour sur l'énigme de S10** : chacun relit ses hypothèses ; on les trie |
| 0 h 20 – 1 h 00 | **Activité « 8 interrupteurs »** (cartes 128, 64, 32, 16, 8, 4, 2, 1) + mini-cours (§1–§2) |
| 1 h 00 – 1 h 40 | **Mini-cours** : adresse, masque /24, plage, privé (§3–§4) + **plan d'adressage** |
| 1 h 40 – 2 h 15 | **TP simulateur** : configurer les 3 PC, matrice de ping |
| 2 h 15 – 2 h 30 | Pause |
| 2 h 30 – 3 h 15 | **TP vrais postes** (Windows et Linux), pare-feu et ping |
| 3 h 15 – 3 h 50 | **Chasse aux erreurs** (simulateur) |
| 3 h 50 – 4 h 00 | Bilan, passeport |

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Tableau d'adressage + 3 postes configurés et validés par ping** | Formatif **noté** (grille dans le TP) |
| Oral | « Que dit un masque /24 ? Pourquoi `.0` et `.255` ne sont-ils pas attribués ? » |

## 🏭 Mission en entreprise

> *Avec l'accord du tuteur, relever l'adresse IP, le masque et la passerelle d'un poste (`ipconfig`).*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **On n'aborde que le /24** : pas de /25, pas de calcul de sous-réseaux (Première, S06).
- L'**activité des 8 cartes** est **essentielle** pour donner du sens : ne pas la sauter. Cartes recto/verso (0 / 1) ou 8 interrupteurs à dessiner.
- **Pare-feu Windows** : par défaut, les requêtes d'écho (ping) entrantes sont **bloquées** : un PC Windows ne répond pas au ping mais peut en émettre. Le TP guide l'activation de la règle (ou la case dans le simulateur).
- **Doublon d'adresse** : Windows affiche une alerte de conflit ; dans le simulateur, la panne apparaît sous forme de ping défaillant.
- Les messages d'erreur du ping ont été relevés **dans le simulateur** ; sur de vrais postes, le libellé peut varier légèrement.

</details>
