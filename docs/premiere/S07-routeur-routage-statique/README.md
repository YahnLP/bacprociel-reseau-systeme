# S07 – Relier deux réseaux : le routeur

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S07 – lundi 23 novembre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S05 (console), S06 (sous-réseaux) |
| **Référentiel** | C06 · C09 · C10 · éléments actifs (niv. 3) · routage statique |

> [!NOTE]
> **Question qui guide la séance :** *« Deux réseaux sont corrects chacun de leur côté, mais ne se parlent pas. Que doit connaître un routeur pour que le paquet aille… et que la réponse revienne ? »*

## 🎯 Objectifs

1. **Expliquer** le rôle du routeur et de la **passerelle par défaut**.
2. **Configurer** les interfaces d'un routeur (`ip address`, `no shutdown`).
3. **Écrire** une **route statique** et une **route par défaut**.
4. **Lire** une table de routage (`show ip route`) et suivre un paquet (`tracert`).
5. **Diagnostiquer** une panne de routage : pas de route à l'aller, **pas de route au retour**.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Routeur, passerelle, table de routage, route statique et par défaut |
| [🛠️ TP](02-tp.md) | Relier deux agences avec deux routeurs neufs |
| [📝 Aide-mémoire routeur](03-aide-memoire-routeur.md) | Commandes de la séance + schéma de décision |
| [`tp/p07-routage.json`](tp/p07-routage.json) | Simulateur : 2 LAN, 2 routeurs neufs, 1 serveur |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : `PC1` ne joint pas le serveur (départ du TP) ; retour mission entreprise | Classe |
| 0 h 20 – 1 h 00 | **Mini-cours 1** : routeur, passerelle, table de routage (§1–§2) | Classe |
| 1 h 00 – 1 h 45 | **TP A–C** : interfaces des deux routeurs | Binôme |
| 1 h 45 – 2 h 00 | Pause | |
| 2 h 00 – 2 h 25 | **Mini-cours 2** : routes statiques, route par défaut (§3–§4) | Classe |
| 2 h 25 – 3 h 30 | **TP D–F** : aller seul, retour manquant, réparation | Binôme |
| 3 h 30 – 4 h 00 | **TP G** : route par défaut, schéma commenté, bilan | Individuel |

## 🧪 Matériel et préparation

- Simulateur avec `tp/p07-routage.json` (routeurs Cisco 1941 neufs : interfaces éteintes).
- **Option matériel réel** : deux routeurs d'occasion (ex. Cisco 1841/1941) et un câble croisé ou des interfaces auto-MDI-X.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **TP : 5 contrôles automatiques** | PC1↔passerelle, R1↔R2, PC1→SRV1, SRV1→PC2, route statique présente |
| **Schéma commenté** | Aller et retour d'un paquet, avec les tables (partie G) |

## 🏭 Mission en entreprise

> *Demander **qui est la passerelle** du réseau de l'entreprise (`ipconfig` : « Passerelle par défaut ») et à quel équipement elle correspond (box, routeur, pare-feu). **Ne rien configurer.***

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Messages observés dans le simulateur** (identiques à Windows dans l'esprit) : route absente sur R1 → `Réponse de 192.168.10.1 : Impossible de joindre le réseau de destination` ; route retour absente → `Délai d'attente de la demande dépassé` ; `tracert` s'arrête après le saut 1 (R2 reçoit mais ne sait pas répondre).
- **Erreur classique** : oublier la route de **retour** sur R2 (ou la passerelle sur le serveur). Le TP la fait vivre volontairement (partie E).
- Le simulateur ne gère **pas** les protocoles dynamiques dans ce TP : on n'évoque RIP/OSPF qu'à l'oral (« quand il y a beaucoup de routeurs, on automatise »).
- Interfaces du routeur : **éteintes par défaut** (`shutdown`) → `no shutdown` indispensable.
- Corrigés : `corriges/premiere/P07-corrige.md` et `P07-routage-corrige.json`.

</details>
