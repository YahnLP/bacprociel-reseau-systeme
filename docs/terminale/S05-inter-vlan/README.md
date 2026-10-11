# S05 – Routage entre VLAN et réseau d'une PME

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S05 – lundi 19 octobre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | Première S07 (routeur), S08–S09 (VLAN, trunk), S14 (ACL) |
| **Référentiel** | C06 · C10 · architectures tertiaires (niv. 2) |

> [!NOTE]
> **Question qui guide la séance :** *« Les VLAN séparent les services. Comment les faire **communiquer quand c'est voulu**, et **seulement** quand c'est voulu ? »*

## 🎯 Objectifs

1. **Configurer** le routage entre VLAN avec un **routeur** (sous-interfaces 802.1Q).
2. **Configurer** le même routage avec un **switch de niveau 3** (interfaces VLAN).
3. **Filtrer** les échanges par une **ACL** (règles d'accès simples).
4. **Dépanner** une panne combinée (trunk, encapsulation, passerelle).
5. **Documenter** l'architecture par un **schéma commenté**.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Pourquoi router entre VLAN ; routeur sur un tronc ; switch de niveau 3 ; ACL |
| [🛠️ TP](02-tp.md) | PME Rivière : routeur, puis switch niveau 3, puis dépannage |
| [📝 Aide-mémoire](03-aide-memoire.md) | Commandes et schéma de vérification |
| [`tp/t05-intervlan.json`](tp/t05-intervlan.json) | Simulateur : 3 VLAN, 2 switches, 1 routeur vierges |
| [`tp/t05-panne.json`](tp/t05-panne.json) | Simulateur : même réseau avec 3 pannes |
| [`tp/t05-switch-niveau3.json`](tp/t05-switch-niveau3.json) | Simulateur : version avec switch de niveau 3 |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « Pourquoi la compta ne peut-elle pas imprimer au commercial alors qu'elle est sur le même switch ? » | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : inter-VLAN par routeur | Classe |
| 0 h 50 – 1 h 50 | **TP A–C** : VLAN, trunks, sous-interfaces | Binôme |
| 1 h 50 – 2 h 05 | Pause | |
| 2 h 05 – 2 h 30 | **Mini-cours** : switch de niveau 3, ACL | Classe |
| 2 h 30 – 3 h 15 | **TP D–E** : ACL, switch de niveau 3 | Binôme |
| 3 h 15 – 4 h | **TP F–G** : dépannage, schéma commenté | Individuel |

## 🧪 Matériel et préparation

- Les trois fichiers `.json` ci-dessus (rouverts **au départ**).
- [Aide-mémoire](03-aide-memoire.md) imprimé.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 6 contrôles automatiques** (VLAN, trunk, routage x2, filtrage x2) | Formatif |
| **Schéma commenté** | Grille : tous les équipements, VLAN, adresses, flux autorisés/interdits |

## 🏭 Mission en entreprise

> *Repérer si l'entreprise utilise des **VLAN** et du **routage entre VLAN** ; relever le **schéma** (avec accord, sans donnée sensible).*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **ACL sans état** : l'ACL de la partie D **bloque aussi les réponses** (le commercial ne peut pas répondre à la compta). C'est **voulu** : on le fait **observer** (`show access-lists`, matches). Pour autoriser « la compta appelle le commercial mais pas l'inverse », il faudrait `established` (TCP) : à présenter **sans** le faire faire.
- **Le DHCP par VLAN** est rappelé (relais `ip helper-address`, vu en Première S17) mais **non refait** ici : il est repris dans le chantier d'entraînement.
- **Switch de niveau 3** : `ip routing` + interfaces VLAN + `switchport trunk encapsulation dot1q` (spécifique au 3560).
- **Pannes (t05-panne)** : 1) le trunk de SW2 n'autorise plus le VLAN 20 ; 2) la sous-interface Gi0/0.30 est en encapsulation `3` ; 3) la passerelle du serveur est fausse (`192.168.30.254`).
- Le mot de passe des switches : aucun (pas de `enable secret`) dans ces fichiers.
- Corrigé : `corriges/terminale/T05-corrige.md`, `T05-intervlan-corrige.json`, `T05-panne-corrige.json`, `T05-switch-niveau3-corrige.json`.

</details>
