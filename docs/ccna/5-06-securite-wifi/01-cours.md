# 📖 Cours – Sécurité du Wi-Fi

*Parcours CCNA – Domaine 5 – module 5-06 (sujets 5.9 et 5.10)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**. Il prolonge le [module 1-06](../1-06-sans-fil-bases/01-cours.md).

## 🎯 À la fin de ce cours, tu sauras

- [ ] comparer **WPA, WPA2 et WPA3** ;
- [ ] distinguer **Personal (PSK)** et **Enterprise (802.1X)** ;
- [ ] créer un **WLAN WPA2-PSK** dans l'interface graphique d'un contrôleur.

---

## 1. Évolution des protocoles

| Protocole | Chiffrement | Authentification (Personal) | État |
|---|---|---|---|
| **WEP** | RC4 | Clé partagée | ❌ Cassé |
| **WPA** | TKIP | PSK | ⚠️ Obsolète |
| **WPA2** | **AES-CCMP** | **PSK** | ✅ Courant |
| **WPA3** | **AES-GCMP** (256 bits en Enterprise) | **SAE** (remplace le PSK) | ✅ Le plus sûr |

**WPA3-Personal / SAE** : même avec un mot de passe **faible**, un attaquant ne peut pas **tester hors ligne** (dictionnaire) les échanges capturés. WPA3 impose aussi les **trames de gestion protégées** (PMF).

## 2. Personal ou Enterprise ?

| | **Personal** | **Enterprise** |
|---|---|---|
| Authentification | **Mot de passe partagé** (PSK ou SAE) | **802.1X** : chaque utilisateur s'authentifie, serveur **RADIUS** |
| Usage | Maison, petit site, invités | Entreprise |
| Retirer un utilisateur | Changer le mot de passe pour tous | Désactiver **un seul** compte |

## 3. Créer un WLAN WPA2-PSK sur un contrôleur

Dans l'interface graphique d'un **WLC** :

1. **WLANs → Create New** : type *WLAN*, **nom de profil** et **SSID**.
2. **General** : activer le WLAN, choisir l'**interface/VLAN**.
3. **Security → Layer 2** : *WPA+WPA2* ; **WPA2 Policy**, chiffrement **AES** ; **Auth Key Mgmt : PSK** ; saisir la **clé**.
4. **QoS** : choisir le profil (Silver par défaut).
5. **Apply**.

> [!TIP]
> **Pour un invité**, utilise un **VLAN séparé** et une **ACL** qui interdit l'accès au réseau interne (Terminale S06).

---

## 🧊 Alternative avec Cisco Packet Tracer

> [!TIP]
> Packet Tracer propose un **point d'accès** et, selon la version, un **contrôleur** (*WLC*). Monte ce scénario :
>
> 1. Une borne, deux portables, un switch et un routeur DHCP.
> 2. Sur la borne : **Config → Port 1 → Authentication**, sélectionne **WPA2-PSK**, saisis une clé.
> 3. Sur un portable : **Config → Wireless0**, même SSID, bonne clé, puis mauvaise clé.
> 4. Observe le résultat dans **Config → Wireless0** et teste un `ping`.

---

## 🧠 Quiz de fin

**1.** Quel protocole Wi-Fi utilise SAE ?

<details markdown="1"><summary>Voir la réponse</summary>

**WPA3**.

</details>

**2.** Pourquoi WPA2-Enterprise est-il préférable en entreprise ?

<details markdown="1"><summary>Voir la réponse</summary>

Chaque utilisateur a **ses identifiants** (802.1X + RADIUS) : on peut en retirer un sans changer le mot de passe de tous.

</details>

**3.** Quel chiffrement utilise WPA2 ?

<details markdown="1"><summary>Voir la réponse</summary>

**AES** (CCMP).

</details>

**4.** Quel est le risque du WEP ?

<details markdown="1"><summary>Voir la réponse</summary>

Il est **cassable en quelques minutes** : ne plus l'utiliser.

</details>
