# S05 – Switch administrable : prise en main

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S05 – lundi 19 octobre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S03 (trame, MAC, switch = couche 2) |
| **Référentiel** | C10 · lignes de commande (niv. 3) · éléments actifs (niv. 3) |

> [!NOTE]
> **Question qui guide la séance :** *« Un switch neuf, c'est un boîtier qui marche tout seul. Pourquoi, en entreprise, doit-on le configurer — et comment le fait-on sans écran ni souris ? »*

## 🎯 Objectifs

1. **Se connecter** à la console d'un switch et **naviguer** dans les modes (`>`, `#`, `(config)#`).
2. **Lire** l'état du switch : `show version`, `show interfaces status`, `show mac address-table`.
3. **Configurer** : nom, mot de passe `enable secret`, bannière, descriptions, ports libres désactivés.
4. **Donner une adresse de gestion** et **administrer à distance** (SSH).
5. **Sauvegarder** la configuration (`running-config` / `startup-config`).

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Switch administrable, modes de la console, `show`, configuration de base |
| [🛠️ TP](02-tp.md) | Configurer un Catalyst 2960 neuf, étape par étape |
| [📝 Aide-mémoire CLI](03-aide-memoire-cli.md) | Les commandes de la séance (à garder) |
| [`tp/p05-switch.json`](tp/p05-switch.json) | Simulateur : switch 2960 d'usine, 3 PC, 1 serveur |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : montrer un vrai switch administrable (ports, console) ; retour mission entreprise | Classe |
| 0 h 20 – 1 h 00 | **Mini-cours 1** : modes, `show`, MAC (cours §1–§2) | Classe |
| 1 h 00 – 1 h 45 | **TP A–B** : explorer le switch, le nommer et le protéger | Binôme |
| 1 h 45 – 2 h 00 | Pause | |
| 2 h 00 – 2 h 25 | **Mini-cours 2** : ports, gestion, SSH, sauvegarde (§3–§4) | Classe |
| 2 h 25 – 3 h 30 | **TP C–E** : ports, adresse de gestion, SSH, sauvegarde | Binôme |
| 3 h 30 – 4 h 00 | **TP F** : fiche d'identité et contrôle, bilan | Individuel |

## 🧪 Matériel et préparation

- Simulateur avec `tp/p05-switch.json`.
- **Option matériel réel** : un switch administrable d'occasion + câble console (USB-série) et un terminal (PuTTY). Les commandes sont les mêmes.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **TP : 6 contrôles automatiques** | Vérifiés par le professeur dans le simulateur (nom, secret, descriptions, ports libres, IP de gestion, ping) |
| **Fiche d'identité du switch** | Complétée en fin de séance |

## 🏭 Mission en entreprise

> *Demander à voir **un switch administrable** de l'entreprise : noter la marque, le nombre de ports et la manière de s'y connecter (console, SSH, interface web). **Ne jamais saisir de mot de passe d'administration.***

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Commandes utiles du simulateur** : `show version`, `show interfaces status`, `show mac address-table`, `show ip interface brief`, `show running-config`, `show startup-config`, `write memory`, `show ip ssh`. Les filtres de sortie (`| include …`) **ne sont pas gérés**.
- **Reload** : le simulateur redémarre mais **ne revient pas à la `startup-config`** : on ne peut donc pas montrer « la config non sauvegardée est perdue » ; on montre la différence `running-config` / `startup-config` avec `show startup-config` (« not present » avant `write memory`).
- **SSH depuis le PC** : `ssh admin@192.168.10.2` ; le client demande ensuite `Username:` (retaper `admin`) puis `Password:`.
- **Secrets** : `enable secret` est stocké haché par le simulateur ; les mots de passe du corrigé (`Cisco123`, `Adm1n!`) sont des exemples de TP — les élèves choisissent les leurs.
- Corrigé : `corriges/premiere/P05-corrige.md` et `P05-switch-corrige.json`.

</details>
