# 📖 Cours – VPN et IPsec

*Parcours CCNA – Domaine 5 – module 5-05 (sujet 5.5)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**. Tu as utilisé un VPN déjà configuré en Terminale (S09) ; ici, tu en **construis un**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer ce qu'est un **VPN** et distinguer **site à site** et **accès distant** ;
- [ ] décrire le rôle d'**IPsec** (IKE phase 1 et 2, ESP) ;
- [ ] configurer un **VPN IPsec site à site** sur deux routeurs.

---

## 1. Qu'est-ce qu'un VPN ?

Un **VPN** (*Virtual Private Network*) crée un **tunnel chiffré** à travers un réseau **non sûr** (Internet) : deux sites parlent **comme s'ils étaient sur le même réseau privé**.

| Type | Principe | Exemple |
|---|---|---|
| **Site à site** (*site-to-site*) | Deux **routeurs / pare-feu** relient deux réseaux | Siège ↔ agence |
| **Accès distant** (*remote access*) | Un **poste** se connecte au réseau de l'entreprise | Télétravail |

## 2. IPsec en bref

**IPsec** est un ensemble de protocoles qui assure :

| Service | Rôle |
|---|---|
| **Confidentialité** | **Chiffrement** (AES) |
| **Intégrité** | Vérification que rien n'a été modifié (SHA) |
| **Authentification** | On sait **qui** est de l'autre côté (clé partagée, certificat) |
| **Anti-rejeu** | Un message copié ne peut pas être rejoué |

### Les deux phases

| Phase | Protocole | Rôle |
|---|---|---|
| **Phase 1** | **IKE** (*ISAKMP*) | Les deux routeurs **s'authentifient** et négocient un canal sûr (politique : chiffrement, hachage, groupe Diffie-Hellman, clé) |
| **Phase 2** | **IPsec** (ESP) | Négocie le **chiffrement du trafic réel** (transform-set) |

**ESP** (*Encapsulating Security Payload*) chiffre **et** authentifie les données. **AH** n'authentifie que (sans chiffrement).

### 🤔 Avant de lire : à ton avis ?

Pourquoi le trafic entre **deux réseaux privés** (192.168.1.0 et 192.168.2.0) ne peut-il pas passer sur Internet **sans** VPN ?

<details markdown="1"><summary>Voir la réponse</summary>

Les routeurs d'Internet **ne connaissent pas** les adresses privées (elles ne sont pas routées). Le VPN **encapsule** les paquets dans un paquet de **l'adresse publique**, que tout le monde sait router.

</details>

## 3. Configuration d'un VPN IPsec site à site

Les **mêmes réglages** sur les deux routeurs (adresses inversées) :

```text
! 1. Le trafic à chiffrer (« trafic intéressant »)
access-list 101 permit ip 192.168.1.0 0.0.0.255 192.168.2.0 0.0.0.255

! 2. Phase 1 : politique IKE et clé
crypto isakmp policy 10
 encryption aes 256
 hash sha256
 authentication pre-share
 group 14
crypto isakmp key Cle#VPN2027 address 198.51.100.6

! 3. Phase 2 : transform-set
crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac

! 4. La crypto map
crypto map CMAP 10 ipsec-isakmp
 set peer 198.51.100.6
 set transform-set TS
 match address 101

! 5. Application sur l'interface vers Internet
interface gigabitEthernet 0/1
 crypto map CMAP
```

| Commande | Rôle |
|---|---|
| `show crypto isakmp sa` | Phase 1 : association de sécurité IKE |
| `show crypto ipsec sa` | Phase 2 : paquets chiffrés / déchiffrés |

> [!WARNING]
> Les **ACL 101 des deux routeurs** doivent être des **images miroirs** (source ↔ destination inversées), et la **clé** et les **paramètres** (chiffrement, hachage, groupe) **identiques**. Une seule différence : le tunnel ne monte pas.

---

## 🧠 Quiz de fin

**1.** Quelle phase d'IPsec authentifie les deux routeurs ?

<details markdown="1"><summary>Voir la réponse</summary>

La **phase 1** (IKE).

</details>

**2.** Que fait ESP que ne fait pas AH ?

<details markdown="1"><summary>Voir la réponse</summary>

ESP **chiffre** les données ; AH ne fait que **authentifier**.

</details>

**3.** À quoi sert l'ACL d'une crypto map ?

<details markdown="1"><summary>Voir la réponse</summary>

À définir le **trafic à chiffrer** (« trafic intéressant »).

</details>

**4.** Quel type de VPN pour un salarié en télétravail ?

<details markdown="1"><summary>Voir la réponse</summary>

Un VPN d'**accès distant**.

</details>

➡️ Suite : [le TP du module](02-tp.md).
