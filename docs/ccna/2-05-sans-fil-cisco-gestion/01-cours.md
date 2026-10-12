# 📖 Cours – Sans fil Cisco et gestion des équipements

*Parcours CCNA – Domaine 2 – module 2-05 (sujets 2.6, 2.7, 2.8 et 2.9)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] comparer les **architectures sans fil** (autonome, contrôleur, cloud) ;
- [ ] citer les **modes** d'un point d'accès ;
- [ ] expliquer comment **AP** et **contrôleur** se branchent ;
- [ ] choisir un **mode de gestion** d'un équipement (console, Telnet, **SSH**, HTTPS, **RADIUS**, **TACACS+**).

---

## 1. Architectures sans fil

| Architecture | Principe | Usage |
|---|---|---|
| **Autonome** (*autonomous AP*) | Chaque borne est configurée **individuellement** | Petit site, quelques bornes |
| **À contrôleur** (*split-MAC, lightweight AP + WLC*) | Les bornes sont « légères » ; le **contrôleur (WLC)** décide de tout. Tunnel **CAPWAP** entre borne et contrôleur | Entreprise, centaines de bornes |
| **Cloud** (*cloud-based*) | Gestion depuis un **portail internet** (ex. Meraki) | Sites répartis, peu de personnel réseau |

### Modes d'un point d'accès léger

| Mode | Rôle |
|---|---|
| **Local** | Mode normal : sert les clients |
| **FlexConnect** | Sert les clients même si le lien avec le contrôleur est coupé (sites distants) |
| **Monitor** | N'émet pas ; **surveille** les attaques |
| **Sniffer** | Capture le trafic pour analyse |
| **Bridge** | Relie deux bâtiments en point à point |

## 2. Connexions AP et WLC

- Une borne légère se branche sur un **port d'accès** du switch (un seul VLAN, plus un éventuel PoE).
- Le **contrôleur** se branche sur un **trunk**, souvent en **LAG** (EtherChannel), pour porter plusieurs VLAN et résister à la panne d'un câble.

## 3. Gérer un équipement

| Méthode | Sécurité | Remarque |
|---|---|---|
| **Console** | Accès physique | Première configuration, dépannage |
| **Telnet** (port 23) | ❌ en clair | À proscrire |
| **SSH** (port 22) | ✅ chiffré | Standard pour la ligne de commande |
| **HTTP** (80) | ❌ en clair | |
| **HTTPS** (443) | ✅ chiffré | Interface web |
| **Gestion cloud** | ✅ via le portail | Selon le fournisseur |

### SSH sur un équipement Cisco

```text
hostname SW1
ip domain-name ciel.local
username admin secret Pa55w0rd!
crypto key generate rsa modulus 2048
ip ssh version 2
interface vlan 1
 ip address 10.0.0.1 255.255.255.0
 no shutdown
line vty 0 4
 login local
 transport input ssh
```

Les clés RSA ont besoin d'un **nom d'hôte** et d'un **nom de domaine** : sinon la commande échoue.

### Authentification centralisée : AAA

| Protocole | Origine | Particularités |
|---|---|---|
| **RADIUS** | Standard (UDP) | Surtout pour **l'accès réseau** (Wi-Fi 802.1X, VPN) |
| **TACACS+** | Cisco (TCP 49) | Surtout pour **l'administration des équipements** ; chiffre tout le message et sépare authentification, autorisation et comptabilité |

## 4. Interface graphique d'un contrôleur

Pour créer un **WLAN** sur un WLC :

1. Donner un **nom de profil** et un **SSID**.
2. Choisir la **sécurité** (WPA2-PSK, WPA2/3-Enterprise).
3. Associer une **interface / un VLAN** de données.
4. Choisir un **profil QoS** : **Platinum** (voix), **Gold** (vidéo), **Silver** (au mieux, par défaut), **Bronze** (arrière-plan).

---

## 🧠 Quiz de fin

**1.** Quel protocole relie une borne légère à son contrôleur ?

<details markdown="1"><summary>Voir la réponse</summary>

**CAPWAP**.

</details>

**2.** Pourquoi préférer SSH à Telnet ?

<details markdown="1"><summary>Voir la réponse</summary>

SSH **chiffre** la session, y compris le mot de passe ; Telnet l'envoie **en clair**.

</details>

**3.** Quel profil QoS convient à la voix sur IP ?

<details markdown="1"><summary>Voir la réponse</summary>

**Platinum**.

</details>

**4.** RADIUS ou TACACS+ pour administrer des équipements ?

<details markdown="1"><summary>Voir la réponse</summary>

**TACACS+** (séparation authentification / autorisation / comptabilité).

</details>

**5.** Quelles conditions faut-il pour générer des clés RSA ?

<details markdown="1"><summary>Voir la réponse</summary>

Un **nom d'hôte** et un **nom de domaine** configurés.

</details>

## 🛠️ Mini-TP dans le simulateur

Sur un switch d'un TP de ton année :

1. Configure **SSH** avec les commandes ci-dessus.
2. Depuis un poste Linux du TP : `ssh admin@10.0.0.1` (adapte l'adresse).
3. Vérifie avec `show ip ssh`.

✅ **Point de contrôle :** tu te connectes en SSH, et Telnet est refusé (`transport input ssh`).
