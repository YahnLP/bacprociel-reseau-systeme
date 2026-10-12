# 📖 Cours – SSH, TFTP et FTP

*Parcours CCNA – Domaine 4 – module 4-05 (sujets 4.8 et 4.9)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** au niveau de détail demandé. L'accès distant (SSH) est vu en Terminale (S09) et Première (S10).

## 🎯 À la fin de ce cours, tu sauras

- [ ] configurer un accès **SSH** et **interdire Telnet** ;
- [ ] expliquer le rôle de **TFTP** et de **FTP** ;
- [ ] choisir le bon protocole pour **sauvegarder** une configuration.

---

## 1. SSH sur un équipement Cisco

Tu l'as vu au [module 2-05](../2-05-sans-fil-cisco-gestion/01-cours.md#3-gerer-un-equipement). Voici la **liste complète**, dans l'ordre :

```text
hostname SW1
ip domain-name ciel.local
username admin secret Pa55w0rd!
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 4
 login local
 transport input ssh
```

| Étape | Pourquoi |
|---|---|
| `hostname` + `ip domain-name` | Obligatoires pour générer les clés |
| `username … secret` | Compte local, mot de passe **haché** |
| `crypto key generate rsa` | Crée la paire de clés qui **chiffre** la session |
| `ip ssh version 2` | Version 2, plus sûre |
| `login local` | Les lignes vty utilisent les comptes locaux |
| `transport input ssh` | **Refuse Telnet** |

> [!TIP]
> **Modulus 2048** : en dessous de 2048 bits, la clé est jugée trop faible aujourd'hui.

**Se connecter :** `ssh -l admin 10.0.0.1` (depuis un équipement Cisco) ou `ssh admin@10.0.0.1` (depuis un poste).

## 2. TFTP et FTP

| | **TFTP** | **FTP** |
|---|---|---|
| Transport | **UDP** 69 | **TCP** 20 (données) et 21 (contrôle) |
| Authentification | **Aucune** | Identifiant et mot de passe (en clair) |
| Fonctions | Envoyer/recevoir un fichier, **rien d'autre** | Lister, créer, supprimer, naviguer |
| Fiabilité | Faible | Bonne (TCP) |
| Usage réseau | **Sauvegarder** une config, charger un **système (IOS)** | Transferts de fichiers plus complets |

> [!WARNING]
> **TFTP et FTP circulent en clair.** Pour un transfert sécurisé, utilise **SFTP** (par SSH) ou **SCP**.

**Sauvegarder une configuration :**

```text
copy running-config tftp:
 Address or name of remote host []? 10.0.0.9
 Destination filename [r1-confg]?
```

> [!NOTE]
> **TFTP n'est pas simulé** dans le simulateur : la commande `copy … tftp:` est à connaître, pas à tester.

---

## 🧠 Quiz de fin

**1.** Quelle commande empêche Telnet ?

<details markdown="1"><summary>Voir la réponse</summary>

`transport input ssh` sur les lignes vty.

</details>

**2.** Pourquoi faut-il un nom de domaine pour générer les clés RSA ?

<details markdown="1"><summary>Voir la réponse</summary>

Le nom de la clé est formé du **nom d'hôte** et du **nom de domaine** (`SW1.ciel.local`).

</details>

**3.** Quel protocole de transfert n'a aucune authentification ?

<details markdown="1"><summary>Voir la réponse</summary>

**TFTP**.

</details>

**4.** Quelle alternative sécurisée à FTP ?

<details markdown="1"><summary>Voir la réponse</summary>

**SFTP** (ou **SCP**), qui passent par **SSH**.

</details>

➡️ Suite : [le TP du module](02-tp.md).
