# S10 – Superviser et tracer les incidents

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S10 – 1er février 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🔴 Autonome |
| **Prérequis** | Première S04 (protocoles), S10 (Linux, SSH), Terminale S07 |
| **Référentiel** | C10 · alertes consignées |

> [!NOTE]
> **Question qui guide la séance :** *« Le réseau tombe à 3 h du matin. Comment l'apprendre avant le client, et comment ne pas oublier ce qui s'est passé ? »*

## 🎯 Objectifs

1. **Expliquer** à quoi servent la **supervision**, **SNMP** et les **journaux** (syslog).
2. **Activer** SNMP et l'envoi des journaux sur un switch.
3. **Interroger** un équipement depuis un poste de supervision et **lire** les valeurs.
4. **Lire** une alerte et **ouvrir** un ticket complet.
5. **Rédiger** un ticket : symptôme, cause, action.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Supervision, SNMP, syslog ; alertes ; tickets |
| [🛠️ TP](02-tp.md) | Imprimerie Laporte : SNMP, journaux, interrogation depuis SUP, simulation de panne et ticket |
| [📝 Aide-mémoire](03-aide-memoire.md) | Commandes SNMP/syslog, OID utiles, modèle de ticket |
| [`tp/t10-supervision.json`](tp/t10-supervision.json) | Simulateur : switch administrable + poste de supervision, rien de configuré |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « Comment l'entreprise sait-elle qu'une machine est en panne avant d'appeler ? » | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : supervision, SNMP, syslog | Classe |
| 0 h 50 – 2 h 00 | **TP A–C** : activer SNMP et journaux, interroger | Binôme |
| 2 h 00 – 2 h 15 | Pause |  |
| 2 h 15 – 2 h 45 | **Mini-cours** : alertes et tickets (GLPI en démonstration) | Classe |
| 2 h 45 – 3 h 30 | **TP D–E** : provoquer une panne, lire l'alerte | Binôme |
| 3 h 30 – 4 h 00 | **TP F** : rédiger les tickets | Individuel |

## 🧪 Matériel et préparation

- Le fichier `t10-supervision.json`.
- Optionnel : une démonstration d'un outil de supervision (Zabbix, Uptime Kuma) ou de **GLPI** sur le plateau.
- [Aide-mémoire](03-aide-memoire.md) imprimé.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 5 contrôles automatiques** (SNMP, journaux, alertes, sauvegarde) | Formatif |
| **Deux tickets rédigés** (panne câble, panne switch) | Grille : symptôme décrit, cause, action, résultat, durée |

## 🏭 Mission en entreprise

> *Repérer l'outil de supervision ou de tickets utilisé ; consigner un incident réel.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Limite du simulateur :** il n'a **ni Zabbix, ni Uptime Kuma, ni GLPI**. La supervision est travaillée avec **`snmpget`/`snmpwalk`** depuis un poste Linux et avec `show logging` sur le switch ; les **outils** sont présentés en **démonstration** (si le plateau en dispose) ; le **ticket** est rédigé **sur papier ou en traitement de texte** (modèle fourni).
- **SNMP v2c** : communauté `supervision` en **lecture seule (RO)**. Expliquer que v2c n'est **pas chiffré** (v3 le serait) : la communauté se comporte comme un mot de passe en clair ; on l'utilise **dans un réseau interne**.
- **Débrancher un câble** dans le simulateur (clic droit sur le câble) puis relancer `snmpwalk … ifOperStatus` : le port passe à `down(2)`. C'est la partie « simulation de panne ». Ne pas annoncer le résultat avant que les élèves l'aient **prévu** (partie D).
- **Lien avec U32 :** la **gestion des incidents** est développée en U32 ; ici on ne prend que le **ticket d'intervention**.
- Le routeur/switch porte une adresse de gestion `192.168.1.2` en VLAN 1 (**uniquement ici**, par simplicité) : en production on utilise un **VLAN de gestion** dédié.
- Corrigé : `corriges/terminale/T10-corrige.md`, `T10-supervision-corrige.json`.

</details>
