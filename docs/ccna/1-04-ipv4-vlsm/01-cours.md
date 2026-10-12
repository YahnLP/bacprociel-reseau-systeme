# 📖 Cours – IPv4 : sous-réseaux et VLSM

*Parcours CCNA – Domaine 1 – module 1-04 (sujets 1.6 et 1.7)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**. Tu as déjà vu les sous-réseaux en Première : ici, on enchaîne avec le **VLSM**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] **calculer** adresse de réseau, de diffusion, première et dernière adresse utilisable ;
- [ ] **découper** un réseau en sous-réseaux **de tailles différentes** (VLSM) ;
- [ ] reconnaître les **adresses privées** (RFC 1918).

---

## 1. Rappel : calculer un sous-réseau

### 🤔 Avant de lire : à ton avis ?

Combien d'adresses **utilisables** y a-t-il dans un `/26` ?

<details markdown="1"><summary>Voir la réponse</summary>

Un `/26` laisse **6 bits** pour les machines : 2⁶ = 64 adresses, moins 2 (réseau et diffusion) = **62 utilisables**.

</details>

**Formule :** machines utilisables = 2ⁿ − 2, où **n** = nombre de bits à 0 dans le masque (32 − préfixe).

| Préfixe | Masque | Taille du bloc | Utilisables |
|---|---|---|---|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |

### 🛠️ Méthode en 4 étapes (exemple : `192.168.50.77/27`)

1. **Taille du bloc** : /27 → 32 adresses.
2. **Réseau** : le multiple de 32 juste en dessous de 77 → **64**. Réseau = `192.168.50.64`.
3. **Diffusion** : 64 + 32 − 1 = **95**. Diffusion = `192.168.50.95`.
4. **Plage utilisable** : de `.65` à `.94`.

### ✅ Vérifie que tu as compris

Donne le réseau et la diffusion de `10.4.9.130/28`.

<details markdown="1"><summary>Voir la réponse</summary>

Bloc de 16. Multiple de 16 sous 130 : 128. Réseau = **10.4.9.128**, diffusion = 128 + 16 − 1 = **10.4.9.143**.

</details>

---

## 2. Adresses privées

| Plage | Préfixe |
|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

Ces adresses ne sont **pas routées sur Internet** : il faut le **NAT** pour sortir (voir module de la suite du parcours).

---

## 3. Le VLSM : des sous-réseaux de tailles différentes

### 🤔 Avant de lire : à ton avis ?

Un service a besoin de 50 adresses, un autre de 25, et le lien entre deux routeurs de 2 adresses. Faut-il donner **le même masque** à tous ?

<details markdown="1"><summary>Voir la réponse</summary>

Non : donner un `/26` (62 adresses) à un lien de 2 machines **gaspille** 60 adresses. Le **VLSM** (*Variable Length Subnet Mask*) permet d'adapter le masque **à chaque besoin**.

</details>

### 🛠️ Méthode VLSM

1. **Classer** les besoins du plus grand au plus petit.
2. Donner à chacun le **plus petit bloc** suffisant (puissance de 2 ≥ besoin + 2).
3. Placer les blocs **à la suite**, sans chevauchement, en commençant au début du réseau.

**Exemple : `192.168.50.0/24`**

| Besoin | Hôtes | Bloc | Préfixe | Réseau | Plage utilisable | Diffusion |
|---|---|---|---|---|---|---|
| Service A | 50 | 64 | **/26** | 192.168.50.0 | .1 à .62 | .63 |
| Service B | 25 | 32 | **/27** | 192.168.50.64 | .65 à .94 | .95 |
| Lien R1–R2 | 2 | 4 | **/30** | 192.168.50.192 | .193 à .194 | .195 |

Il reste de la place (de `.96` à `.191`) pour d'autres besoins futurs.

> [!WARNING]
> **Classe d'abord le plus grand.** Si tu places les petits blocs en premier, tu risques de bloquer l'alignement des gros.

### ✅ Vérifie que tu as compris

Quel préfixe pour un sous-réseau de **100** machines ? Pour **10** machines ?

<details markdown="1"><summary>Voir la réponse</summary>

100 machines → 128 adresses → **/25**. 10 machines → 16 adresses (14 utilisables) → **/28**.

</details>

---

## 🧠 Quiz de fin

**1.** Quel est le masque d'un `/28` ?

<details markdown="1"><summary>Voir la réponse</summary>

**255.255.255.240**.

</details>

**2.** `172.20.5.9` est-elle une adresse privée ?

<details markdown="1"><summary>Voir la réponse</summary>

**Oui** : elle est dans 172.16.0.0/12 (172.16 à 172.31).

</details>

**3.** Quel est le plus petit préfixe pour 300 machines ?

<details markdown="1"><summary>Voir la réponse</summary>

300 + 2 = 302 → 512 adresses → **/23**.

</details>

**4.** Combien d'adresses utilisables a un `/30` ? À quoi sert-il ?

<details markdown="1"><summary>Voir la réponse</summary>

**2** : c'est le bloc classique d'un **lien point à point** entre deux routeurs.

</details>

➡️ Suite : [le TP du module](02-tp.md).
