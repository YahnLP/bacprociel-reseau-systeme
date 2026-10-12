# 📖 Cours – Le NAS

*Parcours serveurs – module 3*

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer ce qu'est un **NAS** et à quoi il sert ;
- [ ] distinguer **partage**, **droits** et **utilisateurs** ;
- [ ] expliquer pourquoi **RAID n'est pas une sauvegarde**.

---

## 1. Qu'est-ce qu'un NAS ?

Un **NAS** (*Network Attached Storage*) est un petit serveur de fichiers prêt à l'emploi : un ou plusieurs disques, un système dédié et une interface web. Plusieurs postes y accèdent **en même temps** par le réseau.

| | Disque dur USB | **NAS** |
|---|---|---|
| Branchement | un seul poste | réseau, plusieurs postes |
| Droits par utilisateur | non | **oui** |
| Services (sauvegarde, partage) | non | oui |

## 2. Partages et droits

| Protocole | Pour qui | Accès |
|---|---|---|
| **SMB/CIFS** | Windows (et Linux, macOS) | `\\nas\partage` |
| **NFS** | Linux | montage du dossier |
| **FTP/SFTP** | transferts de fichiers | client FTP |

Un **dossier partagé** reçoit des **droits** par utilisateur ou groupe : lecture seule, lecture/écriture, aucun accès.

## 3. Disponibilité et sauvegarde

| Technique | Protège contre | Ne protège pas contre |
|---|---|---|
| **RAID 1** (miroir) | la panne d'**un disque** | une suppression, un virus |
| **Sauvegarde** (copie ailleurs) | suppression, virus, sinistre | — |

> [!WARNING]
> **RAID n'est pas une sauvegarde.** Si un fichier est effacé ou chiffré par un virus, il l'est sur les deux disques.

Règle **3-2-1** : 3 copies, sur 2 supports, dont 1 hors site.

---

## 🧠 Quiz de fin

**1.** Que signifie NAS ?

<details markdown="1"><summary>Voir la réponse</summary>

*Network Attached Storage* : stockage relié au réseau.

</details>

**2.** Quel protocole pour accéder à un partage depuis Windows ?

<details markdown="1"><summary>Voir la réponse</summary>

**SMB/CIFS** (`\\nas\partage`).

</details>

**3.** RAID 1 protège-t-il d'un fichier supprimé par erreur ?

<details markdown="1"><summary>Voir la réponse</summary>

**Non** : la suppression est copiée sur les deux disques. Il faut une **sauvegarde**.

</details>

**4.** Que dit la règle 3-2-1 ?

<details markdown="1"><summary>Voir la réponse</summary>

3 copies, sur 2 supports différents, dont 1 hors site.

</details>

➡️ Suite : [le TP du module](02-tp.md).
