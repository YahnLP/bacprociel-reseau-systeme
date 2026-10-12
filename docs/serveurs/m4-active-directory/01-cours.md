# 📖 Cours – Active Directory

*Parcours serveurs – module 4*

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer ce qu'est un **annuaire** et un **domaine** ;
- [ ] décrire le rôle du **contrôleur de domaine**, du **DNS**, des **unités d'organisation** et des **GPO** ;
- [ ] expliquer pourquoi le DNS du client doit pointer vers le serveur AD.

---

## 1. Pourquoi un annuaire ?

Dans un parc de 30 postes, créer les comptes un par un sur chaque PC est ingérable. **Active Directory (AD)** est un **annuaire** : une base centrale des comptes, groupes et ordinateurs. Un utilisateur se connecte avec **le même compte sur n'importe quel poste du domaine**.

## 2. Les mots de l'AD

| Terme | Sens |
|---|---|
| **Domaine** | ensemble de comptes et postes gérés ensemble (`entreprise.local`) |
| **Contrôleur de domaine (DC)** | serveur Windows qui porte l'AD et valide les connexions |
| **Unité d'organisation (OU)** | « dossier » de l'annuaire (Compta, Direction…) |
| **Groupe** | ensemble d'utilisateurs auxquels on donne des droits |
| **GPO** | règles appliquées automatiquement aux comptes et postes d'une OU |

## 3. AD et DNS

L'AD **s'appuie sur le DNS** : un poste trouve le contrôleur de domaine en posant des questions DNS.

> [!WARNING]
> **Le DNS du client doit pointer vers le serveur AD** (pas vers la box ni 8.8.8.8). C'est la cause n°1 d'échec de la jonction au domaine.

## 4. Les GPO

Une **GPO** impose un réglage sans passer sur chaque poste : fond d'écran, lecteur réseau, interdiction du panneau de configuration, mot de passe plus long… Elle est **liée** à une OU et s'applique à tout ce qu'elle contient.

| Commande côté client | Effet |
|---|---|
| `gpupdate /force` | applique les GPO tout de suite |
| `gpresult /r` | montre les GPO appliquées |
| `whoami` | indique le compte connecté |

---

## 🧠 Quiz de fin

**1.** Quel est l'avantage principal d'un annuaire ?

<details markdown="1"><summary>Voir la réponse</summary>

Gérer **les comptes une seule fois, au même endroit**, pour tous les postes.

</details>

**2.** Qu'est-ce qu'un contrôleur de domaine ?

<details markdown="1"><summary>Voir la réponse</summary>

Le serveur Windows qui **porte l'AD** et valide les connexions.

</details>

**3.** Le client ne trouve pas le domaine : quelle est la première vérification ?

<details markdown="1"><summary>Voir la réponse</summary>

Son **DNS** doit pointer vers le serveur AD.

</details>

**4.** À quoi sert une GPO ?

<details markdown="1"><summary>Voir la réponse</summary>

Appliquer des **réglages automatiquement** aux comptes et postes d'une OU.

</details>

➡️ Suite : [le TP du module](02-tp.md).
