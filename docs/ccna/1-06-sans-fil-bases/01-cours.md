# 📖 Cours – Sans fil : les bases

*Parcours CCNA – Domaine 1 – module 1-06 (sujet 1.11)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** au niveau de détail demandé ici. Tu as déjà configuré un Wi-Fi en Seconde et en Terminale.

## 🎯 À la fin de ce cours, tu sauras

- [ ] choisir des **canaux sans chevauchement** ;
- [ ] expliquer **SSID**, **BSS**, **ESS** ;
- [ ] distinguer **2,4 GHz** et **5 GHz** ;
- [ ] comparer **WEP, WPA, WPA2, WPA3** (chiffrement et authentification).

---

## 1. Les canaux

### 🤔 Avant de lire : à ton avis ?

Trois bornes voisines utilisent des canaux qui se **chevauchent**. Quelle conséquence ?

<details markdown="1"><summary>Voir la réponse</summary>

Elles se **brouillent** : plus de collisions, un débit qui chute.

</details>

| Bande | Canaux utilisables (Europe) | Canaux **sans chevauchement** | Portée / débit |
|---|---|---|---|
| **2,4 GHz** | 1 à 13 (largeur de 20 MHz) | **1, 6, 11** (en pratique) | Portée **plus grande**, débit plus faible, très encombrée |
| **5 GHz** | beaucoup de canaux (36 à 140…) | presque tous, en 20 MHz | Portée plus courte, **débit plus élevé** |

> [!TIP]
> Sur la bande 2,4 GHz, on utilise **1, 6 et 11** pour que trois bornes voisines ne se gênent pas.

## 2. SSID, BSS, ESS

| Terme | Définition |
|---|---|
| **SSID** | Le **nom** du réseau Wi-Fi |
| **BSS** | Une borne et ses clients (*Basic Service Set*) |
| **ESS** | **Plusieurs** bornes avec le **même SSID**, reliées par le réseau filaire : le client peut **se déplacer** sans perdre la connexion (*roaming*) |
| **BSSID** | L'adresse MAC de la borne pour ce réseau |

## 3. La sécurité du Wi-Fi

| Norme | Chiffrement | Authentification | Verdict |
|---|---|---|---|
| **Ouvert** | aucun | aucune | à éviter |
| **WEP** | RC4 | clé partagée | **cassé**, ne plus utiliser |
| **WPA** | TKIP | PSK ou 802.1X | obsolète |
| **WPA2** | **AES-CCMP** | **PSK** (clé partagée) ou **802.1X** (entreprise, RADIUS) | standard courant |
| **WPA3** | AES (CCMP/GCMP) | **SAE** (personnel) ou 802.1X (entreprise) | le plus sûr |

- **Personal (PSK)** : un mot de passe partagé, pour la maison ou une petite structure.
- **Enterprise (802.1X)** : **chaque utilisateur** s'authentifie auprès d'un serveur **RADIUS**.

### ✅ Vérifie que tu as compris

Pourquoi une entreprise préfère-t-elle WPA2-Enterprise à WPA2-Personal ?

<details markdown="1"><summary>Voir la réponse</summary>

Chaque salarié a **ses propres identifiants** : on peut en retirer un sans changer le mot de passe de tous les autres.

</details>

---

## 🧠 Quiz de fin

**1.** Quels canaux 2,4 GHz ne se chevauchent pas ?

<details markdown="1"><summary>Voir la réponse</summary>

**1, 6 et 11**.

</details>

**2.** Qu'est-ce que le SSID ?

<details markdown="1"><summary>Voir la réponse</summary>

Le **nom** du réseau sans fil.

</details>

**3.** Quelle bande offre la plus grande portée ?

<details markdown="1"><summary>Voir la réponse</summary>

**2,4 GHz**.

</details>

**4.** Quel chiffrement utilise WPA2 ?

<details markdown="1"><summary>Voir la réponse</summary>

**AES** (mode CCMP).

</details>

**5.** Que signifie ESS ?

<details markdown="1"><summary>Voir la réponse</summary>

Plusieurs bornes avec le **même SSID**, reliées par le réseau filaire, permettant le **roaming**.

</details>

## 🛠️ Mini-TP dans le simulateur

Reprends le TP Wi-Fi de Terminale ([S06 · Wi-Fi d'entreprise](../../terminale/S06-wifi-entreprise/README.md)) ou un TP avec borne Wi-Fi, puis :

1. Ouvre les propriétés de chaque borne : relève le **SSID**, la **sécurité** et la **clé**.
2. Vérifie qu'un portable ne se connecte **qu'avec la bonne clé** (essaie une mauvaise clé, puis la bonne).
3. Pour chaque borne, indique à l'écrit la bande qui conviendrait (2,4 ou 5 GHz) et pourquoi.

> [!NOTE]
> Le simulateur ne modélise pas les interférences entre canaux : les règles des canaux 1, 6 et 11 sont à connaître pour l'examen, pas à tester ici.

## 🧊 Alternative avec Cisco Packet Tracer

> [!TIP]
> Le simulateur du site **ne modélise pas** les canaux Wi-Fi ni les interférences. Dans Packet Tracer :
>
> 1. Place deux points d'accès (*Access Point-PT*) et deux portables sans fil.
> 2. Sur chaque borne, onglet **Config → Port 1** : règle le **SSID**, le **canal** (essaie 1, 6, 11 puis deux canaux voisins) et la **sécurité** (WPA2-PSK).
> 3. Sur chaque portable, onglet **Config → Wireless0** : saisis le SSID et la clé.
> 4. Compare la connexion avec des canaux différents et la même clé, puis avec une mauvaise clé.
