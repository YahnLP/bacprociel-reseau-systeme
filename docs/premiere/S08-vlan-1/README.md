# S08 – VLAN (1) : séparer sans multiplier le matériel

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S08 – lundi 30 novembre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S05 (console du switch), S06 (sous-réseaux), S07 (routeur) |
| **Référentiel** | C06 · C09 · C10 · éléments actifs (niv. 3) · VLAN |

> [!NOTE]
> **Question qui guide la séance :** *« La Direction et l'Atelier sont branchés sur le même switch, et l'Atelier peut voir les postes de la Direction. Faut-il acheter un second switch ? »*

## 🎯 Objectifs

1. **Expliquer** ce qu'est un **VLAN** et pourquoi on sépare des réseaux.
2. **Créer** des VLAN (numéro + nom) sur un switch administrable.
3. **Affecter** des ports à un VLAN (mode *access*).
4. **Vérifier** : `show vlan brief`, `show interfaces status`, ping.
5. **Dépanner** un port mal affecté.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | VLAN, domaine de diffusion, ports *access*, bonnes pratiques |
| [🛠️ TP](02-tp.md) | Séparer Direction et Atelier + dépannage de deux ports mal affectés |
| [📝 Aide-mémoire VLAN](03-aide-memoire-vlan.md) | Commandes et plan de numérotation |
| [`tp/p08-vlan.json`](tp/p08-vlan.json) | Simulateur : switch 2960 d'usine, 4 PC |
| [`tp/p08-vlan-panne.json`](tp/p08-vlan-panne.json) | Simulateur : VLAN déjà créés, 2 ports mal affectés |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : depuis `PC3` (Atelier), on joint `PC1` (Direction) ; retour mission entreprise | Classe |
| 0 h 20 – 1 h 00 | **Mini-cours 1** : domaine de diffusion, VLAN (§1–§2) | Classe |
| 1 h 00 – 1 h 50 | **TP A–C** : constater, créer les VLAN, affecter les ports | Binôme |
| 1 h 50 – 2 h 05 | Pause | |
| 2 h 05 – 2 h 30 | **Mini-cours 2** : bonnes pratiques de numérotation, VLAN et adressage (§3–§4) | Classe |
| 2 h 30 – 3 h 20 | **TP D** : un VLAN = un sous-réseau | Binôme |
| 3 h 20 – 4 h 00 | **TP E–F** : dépannage (fichier panne) + fiche de synthèse | Individuel |

## 🧪 Matériel et préparation

- Simulateur avec `tp/p08-vlan.json` puis `tp/p08-vlan-panne.json`.
- **Option matériel réel** : un switch administrable d'occasion (2960 ou équivalent) et 4 PC / portables.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **TP : 4 contrôles automatiques** | PC1↔PC2, PC3↔PC4, PC1 ne joint pas PC3, VLAN et ports corrects |
| **Dépannage** | Fichier panne : 3 contrôles |
| **Fiche de synthèse** | Plan de VLAN de la PME rempli |

## 🏭 Mission en entreprise

> *Demander s'il existe **plusieurs réseaux séparés** dans l'entreprise (Direction, production, invités…) et **comment** ils sont séparés (VLAN, switchs différents ?). Noter les noms/numéros sans rien modifier.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- Le simulateur gère `vlan`, `name`, `switchport mode access`, `switchport access vlan`, `show vlan brief`, `show interfaces status` / `switchport`. Les liens trunk viennent en **S09**.
- **Entre VLAN** : sans routeur, pas de communication ; le routage **inter-VLAN** est vu en **Terminale (S03)**.
- **Piège** : un ping « ne passe pas » pour deux raisons très différentes (VLAN séparés, ou mauvais sous-réseau). La partie B met les **mêmes adresses IP** dans deux VLAN : c'est bien le **VLAN** qui bloque.
- Les ports non utilisés restent dans le VLAN 1 : on discutera de les couper ou de les isoler (S14, sécurité).
- Corrigés : `corriges/premiere/P08-corrige.md`, `P08-vlan-corrige.json`, `P08-vlan-panne-corrige.json`.

</details>
