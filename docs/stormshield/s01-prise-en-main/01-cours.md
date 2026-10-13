# 📖 Cours – Prise en main d'un pare-feu Stormshield

*Parcours Stormshield – module S01*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours Stormshield (préparation CSNA).

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer le rôle d'un **pare-feu** dans un réseau d'entreprise ;
- [ ] te connecter à l'**interface d'administration** d'un SNS ;
- [ ] dire à quoi servent la **licence**, la **mise à jour** et la **sauvegarde** de configuration.

---

## 1. Le rôle d'un pare-feu

Un **pare-feu** (*firewall*) est placé **entre des réseaux** : il regarde chaque flux et décide de le laisser passer ou de le bloquer, selon une **politique** écrite par l'administrateur.

| Réseau | Exemple | Confiance |
|---|---|---|
| **Interne (LAN)** | postes des employés | élevée |
| **DMZ** | serveur web exposé | moyenne |
| **Externe (WAN)** | Internet | aucune |

Un pare-feu Stormshield **SNS** est un pare-feu « nouvelle génération » : au-delà du filtrage réseau, il offre aussi la **protection applicative** (URL, antivirus, détection d'intrusion), l'**authentification** des utilisateurs et les **VPN**. Les modules suivants les détaillent.

## 2. Se connecter à l'administration

| Moyen | Pour quoi faire |
|---|---|
| **Interface web** (navigateur, `https://adresse-du-pare-feu/admin`) | administrer au quotidien |
| **Console** (câble série ou console de la VM) | premier réglage, dépannage |
| **SSH** | commandes avancées |

> [!WARNING]
> À la première mise en service, **change le mot de passe administrateur** (les identifiants d'usine sont dans la documentation de ta version). Ne laisse jamais l'accès d'administration ouvert à Internet.

Le menu de l'interface web est organisé en grandes rubriques : **Système**, **Réseau**, **Objets**, **Utilisateurs**, **Politique de sécurité**, **Protection applicative**, **VPN**, **Notifications** (journaux). Les noms exacts varient un peu selon la version.

## 3. Licence, mises à jour, sauvegarde

| Sujet | À retenir |
|---|---|
| **Licence** | Elle active les fonctions (nombre d'utilisateurs, modules). Elle se télécharge depuis l'espace client Stormshield (compte *MyStormshield*). |
| **Mise à jour** | Le système (*firmware*) se met à jour par fichier ; **sauvegarde d'abord**, puis mise à jour, puis vérification. |
| **Sauvegarde** | La configuration s'exporte dans un fichier : à faire **avant toute modification importante** et à garder hors du pare-feu. |

> [!TIP]
> Un pare-feu sans sauvegarde de configuration, c'est un pare-feu à reconfigurer entièrement après une panne.

## 4. Dans le simulateur

Le simulateur contient un **Stormshield SN210** à quatre ports : `OUT` (zone WAN), `IN` (LAN), `DMZ1` et `DMZ2`. Double-clique sur le pare-feu : tu trouves les onglets **Interfaces**, **Règles de filtrage**, **NAT / redirections**, **Journal** et **Diagnostic**.

> [!NOTE]
> 🧊 **Limite du simulateur.** Il n'a pas de licence, de mise à jour, de sauvegarde ni de comptes administrateurs. **Alternative :** machine virtuelle **Stormshield EVA** (voir le TP). Sur **Cisco Packet Tracer**, l'équivalent est la sauvegarde de configuration d'un routeur : `copy running-config startup-config` (module [CCNA 4-05](../../ccna/4-05-ssh-tftp/01-cours.md)).

## 🔧 Dépanner : « je n'arrive pas à ouvrir l'interface d'administration »

> [!NOTE]
> **Pourquoi ce chapitre ?** La toute première panne qu'un technicien rencontre est de **joindre** l'équipement. La méthode est celle des réseaux : de la couche 1 à la couche 7.

| Étape | Test | Cause fréquente |
|---|---|---|
| 1 | Le câble est-il sur le **bon port** ? voyant allumé ? | port `OUT` au lieu de `IN` ; câble défectueux |
| 2 | Le poste est-il **dans le même réseau** que l'adresse d'administration ? | mauvaise adresse ou mauvais masque sur le poste |
| 3 | `ping` de l'adresse du pare-feu | pare-feu non démarré, mauvaise adresse |
| 4 | `https://adresse/admin` (**https**, chemin `/admin`) | adresse tapée en `http`, sans `/admin` |
| 5 | Avertissement du navigateur sur le certificat | normal au premier accès : le certificat est auto-signé |
| 6 | Identifiants refusés | compte par défaut modifié ; vérifier avec l'enseignant |

---

## 🧠 Quiz de fin

**1.** Entre quels réseaux place-t-on un pare-feu ?

<details markdown="1"><summary>Voir la réponse</summary>

Entre des réseaux de **niveaux de confiance différents** (LAN, DMZ, Internet).

</details>

**2.** Que faire avant une mise à jour du système ?

<details markdown="1"><summary>Voir la réponse</summary>

**Sauvegarder la configuration.**

</details>

**3.** Pourquoi changer le mot de passe d'usine ?

<details markdown="1"><summary>Voir la réponse</summary>

Il est **public** (dans la documentation) : n'importe qui pourrait administrer le pare-feu.

</details>

➡️ Suite : [le TP du module](02-tp.md).
