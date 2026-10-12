# S10 – Un serveur Linux et la connexion à distance

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S10 – lundi 11 janvier 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | Seconde S05–S06 (VM Ubuntu, terminal), Première S07 (passerelle) |
| **Référentiel** | C10 · lignes de commande (niv. 3) · connexion à distance (niv. 3) · serveurs (niv. 2) |

> [!NOTE]
> **Question qui guide la séance :** *« Un serveur est dans une baie, sans écran. Comment l'installer, lui donner une adresse fixe, créer les comptes… et s'en occuper depuis son poste sans jamais le toucher ? »*

## 🎯 Objectifs

1. **Installer** un serveur Linux **sans interface graphique** (Ubuntu Server) dans une VM.
2. **Naviguer** et **lire** le système en ligne de commande (arborescence, `/etc`, journaux).
3. **Donner une adresse IP fixe** (netplan) et **vérifier** la passerelle.
4. **Créer** un utilisateur, gérer `sudo`.
5. **Administrer à distance** en **SSH**, puis par **clé**, et durcir l'accès.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Serveur sans écran, arborescence, utilisateurs/`sudo`, services, SSH et clés |
| [🛠️ TP](02-tp.md) | Panne réseau d'un serveur (simulateur) puis installation et administration d'Ubuntu Server (VM) |
| [📝 Aide-mémoire Linux](03-aide-memoire-linux.md) | Commandes de la séance |
| [`tp/p10-serveur.json`](tp/p10-serveur.json) | Simulateur : poste admin, routeur, serveur Linux sans passerelle |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 40 | **Accroche** : le serveur joint depuis un autre réseau ne répond pas (simulateur, partie A) ; retour mission entreprise | Binôme |
| 0 h 40 – 1 h 00 | **Mini-cours 1** : serveur sans écran, arborescence (§1–§2) | Classe |
| 1 h 00 – 1 h 50 | **TP B** : créer la VM et installer Ubuntu Server (pendant l'installation : cours §3) | Binôme |
| 1 h 50 – 2 h 05 | Pause | |
| 2 h 05 – 3 h 00 | **TP C–D** : premiers pas, IP fixe, utilisateur | Binôme |
| 3 h 00 – 3 h 45 | **TP E** : SSH depuis le poste, clé, durcissement | Binôme |
| 3 h 45 – 4 h 00 | **TP F** : fiche d'identité du serveur, bilan | Individuel |

## 🧪 Matériel et préparation

- Simulateur avec `tp/p10-serveur.json`.
- **VirtualBox** et l'**ISO Ubuntu Server 24.04 LTS** déjà téléchargés (≈ 2 Go). Un réseau « Accès NAT » + une carte « Réseau privé hôte » (192.168.56.0/24).
- **Plan B** : une VM Ubuntu Server **déjà installée** (OVA) si l'installation prend trop de temps.
- Un poste client avec un terminal OpenSSH (Windows 10/11 : PowerShell ; Linux/macOS : terminal).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur (partie A)** | 2 contrôles automatiques : PC1↔SRV1 dans les deux sens |
| **VM : fiche d'identité du serveur** | Vérifiée par le professeur : IP fixe, utilisateur, `sudo`, SSH par clé, mot de passe désactivé |
| **Oral** | 3 questions de bilan |

## 🏭 Mission en entreprise

> *Demander **comment on administre un serveur** de l'entreprise (écran, console, SSH, bureau à distance) et **qui a un compte administrateur**. Ne jamais saisir de mot de passe d'administration.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Ce que le simulateur ne fait pas** : il n'émule pas un vrai Linux serveur (pas de `sshd`, de comptes, de fichiers `/etc`). La partie A (réseau) est simulée ; **toute la partie B–F se fait sur une VM Ubuntu Server réelle**. Cette partie **n'a pas été validée en direct par l'auteur du cours** : tester une fois la procédure (noms d'interfaces `enp0s3`/`enp0s8` selon VirtualBox) avant la séance.
- **Réseau VirtualBox** : adaptateur 1 « NAT » (accès Internet pour `apt`) ; adaptateur 2 « Réseau privé hôte » (le PC hôte est en 192.168.56.1). Si le réseau privé hôte n'existe pas : *Fichier ▸ Outils ▸ Gestionnaire de réseau*.
- **Piège classique** : fichier netplan avec indentation à la tabulation (le YAML n'accepte que des espaces) ; fichier trop permissif (`chmod 600`).
- **Piège SSH** : sur Ubuntu 24.04 le fichier `50-cloud-init.conf` peut imposer `PasswordAuthentication yes` ; notre réglage est dans `10-ciel.conf` (lu en premier). **Toujours tester dans un second terminal avant de fermer la session**.
- Les mots de passe sont ceux des élèves : ne pas les écrire au tableau.
- Corrigés : `corriges/premiere/P10-corrige.md`, `P10-serveur-corrige.json`.

</details>
