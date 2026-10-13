# 📖 Cours – NAT et PAT

*Parcours CCNA – Domaine 4 – module 4-01 (sujet 4.1)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** au niveau de configuration demandé (le NAT d'une box est vu en Seconde, S13).

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer **pourquoi** et **comment** le NAT traduit les adresses ;
- [ ] distinguer **NAT statique**, **NAT dynamique (pool)** et **PAT (surcharge)** ;
- [ ] utiliser le vocabulaire **inside / outside**, **local / global** ;
- [ ] configurer et vérifier le PAT.

---

## 1. Pourquoi le NAT ?

Les adresses **privées** (192.168.x.x, 10.x.x.x, 172.16-31.x.x) ne sont **pas routées sur Internet**. Pour qu'un poste privé accède à Internet, le routeur de bordure **remplace** son adresse par une adresse **publique**. C'est le **NAT** (*Network Address Translation*).

| Type | Principe | Usage |
|---|---|---|
| **NAT statique** | **Une** adresse privée ↔ **une** adresse publique, **fixe** | Publier un **serveur** (web, messagerie) |
| **NAT dynamique** | Les privées utilisent **un pool** d'adresses publiques, à la demande | Peu courant |
| **PAT** (*NAT overload*) | **Toutes** les privées partagent **une** adresse publique, grâce aux **numéros de port** | **Le plus courant** : box, routeur de bordure |

## 2. Le vocabulaire

| Terme | Sens |
|---|---|
| **Inside** | Le côté **réseau interne** (LAN) |
| **Outside** | Le côté **Internet** |
| **Inside local** | Adresse du poste **telle qu'on la voit à l'intérieur** (privée) |
| **Inside global** | Adresse du même poste **telle qu'on la voit à l'extérieur** (publique) |
| **Outside local / global** | Adresses du **serveur distant**, vues de l'intérieur / de l'extérieur |

### 🤔 Exemple

`PC1` (192.168.10.11) visite le serveur `198.51.100.80`. L'interface publique du routeur est `203.0.113.2`. Quelles sont les 4 adresses ?

<details markdown="1"><summary>Voir la réponse</summary>

- Inside local : `192.168.10.11`
- Inside global : `203.0.113.2`
- Outside local et global : `198.51.100.80` (identique, sans NAT côté distant)

</details>

## 3. Configurer le PAT

```text
access-list 1 permit 192.168.10.0 0.0.0.255

interface gigabitEthernet 0/0
 ip nat inside
interface gigabitEthernet 0/1
 ip nat outside

ip nat inside source list 1 interface gigabitEthernet 0/1 overload
```

| Étape | Commande | Rôle |
|---|---|---|
| 1 | `access-list 1 permit …` | Liste les adresses internes **à traduire** |
| 2 | `ip nat inside` / `ip nat outside` | Marque les deux côtés |
| 3 | `ip nat inside source list 1 interface … overload` | Traduit, avec **partage** de l'adresse de l'interface |

**NAT statique :** `ip nat inside source static 192.168.10.5 203.0.113.5`

**Vérifier :**

| Commande | Rôle |
|---|---|
| `show ip nat translations` | table des traductions en cours |
| `show ip nat statistics` | compteurs, interfaces inside/outside |

> [!WARNING]
> **Pas d'`ip nat inside` / `outside` = pas de traduction.** C'est l'oubli numéro un. Le deuxième : une ACL qui ne couvre pas les adresses du LAN.

### ✅ Vérifie que tous les postes passent

Comment le routeur distingue-t-il les réponses destinées à `PC1` et à `PC2` alors qu'ils partagent la même adresse publique ?

<details markdown="1"><summary>Voir la réponse</summary>

Par le **numéro de port** source : à chaque connexion, le routeur choisit un port différent et le note dans sa table.

</details>

---

## 🔧 Dépanner : « les postes n'accèdent plus à Internet »

> [!NOTE]
> **Pourquoi ce chapitre ?** Le NAT est le point de passage obligé entre le réseau privé et Internet. Si une seule des **trois** conditions manque, rien ne sort : ① les interfaces sont déclarées `inside` / `outside`, ② une ACL désigne **qui** a le droit d'être traduit, ③ la règle `ip nat inside source` relie l'ACL à l'adresse publique.

### Les commandes de diagnostic

| Commande | Ce qu'elle montre |
|---|---|
| `show ip nat translations` | les traductions **en cours** (qui est sorti, avec quel port) |
| `show ip nat statistics` | les interfaces `inside` / `outside`, le nombre de traductions, les échecs |
| `show access-lists` | l'ACL de sélection, avec ses **compteurs de correspondances** |
| `show ip route` | la route par défaut vers le FAI |

### Panne 1 – `ip nat inside` oublié

*Symptôme : le ping vers un serveur d'Internet échoue (100 % de perte).*

```text
R1# show ip nat statistics
Outside interfaces:
  GigabitEthernet0/1
Inside interfaces:                 <- la liste est VIDE
```

**Correction :** `interface gi0/0` puis `ip nat inside`. Aucune erreur n'avait été affichée à la configuration : la commande manquante ne produit **aucun message**.

### Panne 2 – L'ACL ne désigne pas le bon réseau

```text
R1# show access-lists
Standard IP access list 1
    10 permit 192.168.11.0, wildcard bits 0.0.0.255      <- le LAN est en .10.0
```

Le LAN est en `192.168.10.0/24`, l'ACL autorise `192.168.11.0/24` : **personne n'est traduit**. Indice supplémentaire : l'ACL n'a **aucune correspondance** (pas de « matches »). **Correction :** réécrire l'ACL avec le bon réseau.

> [!WARNING]
> **Piège de test.** Après une panne, la table des traductions peut encore contenir d'**anciennes** entrées. Vide-la (`clear ip nat translation *`) avant de retester, sinon tu interprètes un état ancien.

### Check-list « pas d'Internet »

1. Le poste joint-il **sa passerelle** (le routeur) ? Sinon, ce n'est pas le NAT.
2. Le routeur joint-il le **FAI** (`ping` de l'adresse du FAI) ? Route par défaut ? Interface `up/up` ?
3. `show ip nat statistics` : interfaces `inside`/`outside` correctes ?
4. `show access-lists` : l'ACL **correspond-elle** aux adresses du LAN ?
5. `show ip nat translations` : une traduction apparaît-elle quand le poste teste ?

---

## 🧠 Quiz de fin

**1.** Quel NAT permet de partager **une** adresse publique entre tous les postes ?

<details markdown="1"><summary>Voir la réponse</summary>

Le **PAT** (*overload*).

</details>

**2.** Quel NAT pour rendre un serveur interne joignable depuis Internet ?

<details markdown="1"><summary>Voir la réponse</summary>

Le **NAT statique**.

</details>

**3.** Quelle commande affiche les traductions en cours ?

<details markdown="1"><summary>Voir la réponse</summary>

`show ip nat translations`.

</details>

**4.** « Inside global » désigne quelle adresse ?

<details markdown="1"><summary>Voir la réponse</summary>

L'adresse **publique** du poste interne, vue de l'extérieur.

</details>

➡️ Suite : [le TP du module](02-tp.md).
