# 📖 Cours – Accès aux équipements et AAA

*Parcours CCNA – Domaine 5 – module 5-02 (sujets 5.3 et 5.8)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** au niveau de détail demandé. Tu as déjà sécurisé des accès en Terminale (S09).

## 🎯 À la fin de ce cours, tu sauras

- [ ] protéger l'accès à un équipement avec des **mots de passe locaux** ;
- [ ] expliquer la différence **enable password / enable secret** ;
- [ ] décrire **AAA** : authentification, autorisation, comptabilité ;
- [ ] comparer **RADIUS** et **TACACS+**.

---

## 1. Mots de passe locaux

| Commande | Rôle |
|---|---|
| `enable secret <mdp>` | Protège le mode privilégié, **haché** (chiffrement fort) |
| `enable password <mdp>` | Même rôle mais **en clair** : à éviter |
| `username admin secret <mdp>` | Compte local, mot de passe **haché** |
| `service password-encryption` | **Brouille** les mots de passe en clair de la configuration |
| `line console 0` + `password` + `login` | Protège le port console |
| `line vty 0 4` + `login local` | Les connexions distantes utilisent les comptes locaux |
| `exec-timeout 5 0` | Déconnecte après 5 minutes d'inactivité |
| `banner motd #texte#` | Message d'**avertissement légal** à la connexion |

> [!WARNING]
> `service password-encryption` n'offre qu'un **chiffrement faible** (réversible). La vraie protection, c'est **`secret`**. Si `enable password` **et** `enable secret` existent, **`secret`** prime.

### ✅ Vérifie que tu as compris

Pourquoi écrire une **bannière** disant que l'accès est réservé ?

<details markdown="1"><summary>Voir la réponse</summary>

Pour **rendre explicite** l'interdiction d'accès : une bannière du type « bienvenue » peut affaiblir une action en justice. Elle ne doit **jamais** contenir d'information sur le réseau.

</details>

## 2. AAA

**AAA** répond à trois questions :

| Lettre | Question | Exemple |
|---|---|---|
| **A**uthentication | **Qui** es-tu ? | Identifiant et mot de passe, MFA |
| **A**uthorization | Que **peux-tu faire** ? | Droits : lecture seule ou administrateur |
| **A**ccounting | Qu'**as-tu fait** ? | Journal des commandes, durée de session |

Un **serveur AAA** central (RADIUS ou TACACS+) évite de gérer des comptes sur **chaque** équipement : on retire un utilisateur **en un seul endroit**.

| | **RADIUS** | **TACACS+** |
|---|---|---|
| Origine | Standard ouvert | Cisco |
| Transport | **UDP** (1812/1813) | **TCP 49** |
| Chiffrement | Seulement le **mot de passe** | **Tout** le message |
| Séparation A-A-A | Authentification + autorisation **ensemble** | **Trois** fonctions **séparées** |
| Usage typique | **Accès réseau** (Wi-Fi, VPN, 802.1X) | **Administration** des équipements |

```text
aaa new-model
aaa authentication login default local
```

---

## 🧠 Quiz de fin

**1.** Quelle commande protège le mode privilégié avec un mot de passe haché ?

<details markdown="1"><summary>Voir la réponse</summary>

`enable secret`.

</details>

**2.** Que fait AAA « Accounting » ?

<details markdown="1"><summary>Voir la réponse</summary>

Il **journalise** ce que fait chaque utilisateur.

</details>

**3.** RADIUS ou TACACS+ pour administrer des switchs Cisco ?

<details markdown="1"><summary>Voir la réponse</summary>

**TACACS+**.

</details>

**4.** Quel port utilise TACACS+ ?

<details markdown="1"><summary>Voir la réponse</summary>

**TCP 49**.

</details>

➡️ Suite : [le TP du module](02-tp.md).
