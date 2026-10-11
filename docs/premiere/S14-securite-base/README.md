# S14 – Sécurité de base d'un réseau

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S14 – lundi 15 mars 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S05 (console switch), S07 (routeur), S10 (serveur Linux), S12 (web) |
| **Référentiel** | C10 · bonnes pratiques de sécurité (niv. 2) |

> [!NOTE]
> **Question qui guide la séance :** *« Le réseau marche. Est-il pour autant protégé ? Que peut-on corriger en une heure, sans rien racheter, pour réduire fortement le risque ? »*

## 🎯 Objectifs

1. **Auditer** un mini-réseau avec une **checklist de 10 points**.
2. **Durcir** un switch : secret, SSH seul, bannière, ports libres coupés, sauvegarde.
3. **Filtrer** avec une **ACL** de routeur : n'autoriser que le web vers un serveur.
4. **Activer** le **pare-feu d'un serveur Linux** sans se couper l'accès.
5. **Expliquer** mises à jour et sauvegardes comme mesures de sécurité.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Défense en profondeur, mots de passe, services, pare-feu, ACL, MAJ, sauvegardes |
| [🛠️ TP](02-tp.md) | Audit, durcissement du switch, ACL, pare-feu `ufw`, sauvegarde |
| [📝 Checklist d'audit (10 points)](03-checklist-audit.md) | Grille à remplir avant / après |
| [`tp/p14-securite.json`](tp/p14-securite.json) | Simulateur : switch faible, routeur sans filtrage, serveur web |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : de l'extérieur, on ouvre `telnet` sur le switch et on lit le mot de passe en capture ; retour mission | Classe |
| 0 h 20 – 0 h 55 | **Mini-cours 1** : défense en profondeur, mots de passe, services, MAJ (§1–§3) | Classe |
| 0 h 55 – 1 h 50 | **TP A–B** : audit, durcissement du switch | Binôme |
| 1 h 50 – 2 h 05 | Pause | |
| 2 h 05 – 2 h 35 | **Mini-cours 2** : pare-feu et ACL (§4) | Classe |
| 2 h 35 – 3 h 30 | **TP C–D** : ACL du routeur, pare-feu `ufw` du serveur (VM) | Binôme |
| 3 h 30 – 4 h 00 | **TP E–F** : sauvegarde, ré-audit, bilan | Individuel |

## 🧪 Matériel et préparation

- Simulateur : `tp/p14-securite.json`.
- **VM Ubuntu Server** de S10 (partie D, facultative) — avec accès SSH en place.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 7 contrôles automatiques** | Secret, SSH seul, bannière, ports coupés, sauvegarde, web OK, ping filtré |
| **Checklist d'audit (avant / après)** | Notée (formatif) |

## 🏭 Mission en entreprise

> *Faire le point avec le tuteur sur **3 bonnes pratiques** de l'entreprise : mots de passe, mises à jour, sauvegardes. **Ne copier aucune donnée sensible.***

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Limites du simulateur** : `enable password` est traité comme un `secret` (haché) ; `service password-encryption` n'est **pas** reflété dans `show running-config` ; les mots de passe `username … secret` s'affichent en clair dans la configuration simulée. Ces points sont **expliqués en cours** (réalité des équipements) mais **non vérifiés** automatiquement.
- **ACL** : le simulateur gère `ip access-list extended`, `permit/deny`, `ip access-group … in`, `show access-lists` avec compteurs (« matches »).
- **Pare-feu `ufw`** (partie D, VM réelle, **non testée en direct par l'auteur**) : le piège pédagogique est de **s'enfermer dehors** si l'on active `ufw` sans avoir autorisé SSH ; faire autoriser SSH **avant**.
- **Windows** : le pare-feu du poste est présenté en cours ; l'exercice facultatif utilise `netsh advfirewall` (droits administrateur requis, souvent indisponibles sur les postes du CFA).
- Corrigés : `corriges/premiere/P14-corrige.md` et `P14-securite-corrige.json`.

</details>
