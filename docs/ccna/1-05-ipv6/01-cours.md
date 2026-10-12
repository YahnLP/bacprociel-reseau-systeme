# 📖 Cours – IPv6

*Parcours CCNA – Domaine 1 – module 1-05 (sujets 1.8 et 1.9)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** (seul IPv4 figure au programme). IPv6 est pourtant **partout** dans le métier.

## 🎯 À la fin de ce cours, tu sauras

- [ ] **écrire** et **raccourcir** une adresse IPv6 ;
- [ ] reconnaître les **types d'adresses** : global, unique local, lien local, multicast, anycast ;
- [ ] **calculer** un identifiant **EUI-64** ;
- [ ] **configurer** IPv6 sur un routeur et ajouter une route statique.

---

## 1. Pourquoi IPv6 ?

IPv4 offre environ 4,3 milliards d'adresses : **elles sont épuisées**. IPv6 a **128 bits** (au lieu de 32), soit un nombre quasi illimité d'adresses, **sans NAT** nécessaire.

## 2. Écrire une adresse IPv6

Une adresse = **8 groupes** de 4 chiffres hexadécimaux, séparés par `:`.

`2001:0db8:0000:0000:0000:0000:0000:0001`

**Deux règles pour raccourcir :**

1. Dans chaque groupe, on supprime les **zéros de tête** : `0db8` → `db8`, `0000` → `0`.
2. Une **seule** suite de groupes à zéro peut être remplacée par `::` (une seule fois par adresse).

→ `2001:db8::1`

### ✅ Vérifie que tu as compris

Raccourcis `fe80:0000:0000:0000:0202:b3ff:fe1e:8329`.

<details markdown="1"><summary>Voir la réponse</summary>

`fe80::202:b3ff:fe1e:8329`

</details>

### 💡 Structure : préfixe + identifiant d'interface

Une adresse unicast = **64 bits de préfixe** (réseau) + **64 bits d'identifiant d'interface**. Le masque est presque toujours **/64** pour un réseau local.

## 3. Les types d'adresses

| Type | Préfixe | Rôle |
|---|---|---|
| **Global unicast** | `2000::/3` (commence par 2 ou 3) | Adresse **publique**, routable sur Internet |
| **Unique local** | `fc00::/7` (en pratique `fd…`) | Adresse **privée**, non routée sur Internet |
| **Link-local** | `fe80::/10` | Valable **sur le lien uniquement** ; sert aux voisins et au routage |
| **Multicast** | `ff00::/8` | Un envoi vers **un groupe** (remplace la diffusion) |
| **Anycast** | adresse unicast partagée | Plusieurs machines ; la **plus proche** répond |
| **Boucle locale** | `::1` | Équivalent de 127.0.0.1 |

> [!NOTE]
> **IPv6 n'a plus de diffusion (broadcast)** : elle est remplacée par le multicast. Exemples : `ff02::1` = tous les nœuds du lien ; `ff02::2` = tous les routeurs.

Une interface IPv6 a **plusieurs adresses** à la fois : au moins une **link-local** (créée automatiquement) et une adresse globale.

## 4. L'EUI-64 : fabriquer l'identifiant avec l'adresse MAC

Pour une MAC `00:1A:2B:3C:4D:5E` :

1. Couper la MAC en deux : `00:1A:2B` | `3C:4D:5E`.
2. Insérer `FF:FE` au milieu : `00:1A:2B:FF:FE:3C:4D:5E`.
3. **Inverser le 7ᵉ bit** du premier octet : `00` (0000 0000) devient `02` (0000 0010).

→ identifiant d'interface : `021A:2BFF:FE3C:4D5E`. Avec le préfixe `2001:db8:acad:1::/64` : **`2001:db8:acad:1:21a:2bff:fe3c:4d5e`**.

### ✅ Vérifie que tu as compris

Quel est l'identifiant EUI-64 de la MAC `AA:BB:CC:11:22:33` ?

<details markdown="1"><summary>Voir la réponse</summary>

Insertion de FFFE : `AA:BB:CC:FF:FE:11:22:33`. Premier octet `AA` = 1010 1010 → on inverse le 7ᵉ bit → 1010 1000 = `A8`. Résultat : **`A8BB:CCFF:FE11:2233`**.

</details>

## 5. Configurer IPv6 sur un routeur Cisco

```text
configure terminal
ipv6 unicast-routing
interface gi0/0
 ipv6 address 2001:db8:acad:1::1/64
 no shutdown
 exit
ipv6 route 2001:db8:acad:2::/64 2001:db8:acad:12::2
end
show ipv6 interface brief
show ipv6 route
```

> [!WARNING]
> Sans **`ipv6 unicast-routing`**, le routeur se comporte comme un simple **hôte** IPv6 : il ne route pas.

| Commande | Rôle |
|---|---|
| `show ipv6 interface brief` | adresses de chaque interface |
| `show ipv6 route` | table de routage IPv6 |
| `ping <adresse IPv6>` | tester |
| `ipv6 address <préfixe>/64 eui-64` | construit l'identifiant avec la MAC |

---

## 🧠 Quiz de fin

**1.** Combien de bits a une adresse IPv6 ?

<details markdown="1"><summary>Voir la réponse</summary>

**128**.

</details>

**2.** `2001:db8::` et `2001:db8::1` peuvent-elles être écrites avec deux `::` ?

<details markdown="1"><summary>Voir la réponse</summary>

Non : **un seul** `::` par adresse. Ici, chaque adresse en contient déjà un.

</details>

**3.** Une adresse commence par `fe80`. De quel type est-elle ?

<details markdown="1"><summary>Voir la réponse</summary>

**Link-local** : valable uniquement sur le lien local.

</details>

**4.** Par quoi le broadcast est-il remplacé en IPv6 ?

<details markdown="1"><summary>Voir la réponse</summary>

Par le **multicast**.

</details>

**5.** Quelle commande active le routage IPv6 sur un routeur ?

<details markdown="1"><summary>Voir la réponse</summary>

`ipv6 unicast-routing`.

</details>

➡️ Suite : [le TP du module](02-tp.md).
