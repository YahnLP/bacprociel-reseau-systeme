# 📖 Cours – Routage statique IPv4 et IPv6

*Parcours CCNA – Domaine 3 – module 3-02 (sujet 3.3)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** au niveau de détail demandé. Tu as déjà écrit des routes statiques en Première (S07) : ici, on ajoute la **route par défaut**, la **route flottante** et l'**hôte**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] écrire une route statique **réseau**, **hôte** et **par défaut** (IPv4 et IPv6) ;
- [ ] créer une route **flottante** de secours ;
- [ ] vérifier avec `show ip route` et `ping`.

---

## 1. Les types de routes statiques

```text
! Route vers un réseau
ip route 192.168.3.0 255.255.255.0 10.0.12.2

! Route par défaut (tout ce qui n'a pas de route plus précise)
ip route 0.0.0.0 0.0.0.0 10.0.12.2

! Route vers UN hôte (/32)
ip route 10.0.99.5 255.255.255.255 10.0.12.2

! IPv6
ipv6 route 2001:db8:acad:2::/64 2001:db8:acad:12::2
ipv6 route ::/0 2001:db8:acad:12::2
```

| Type | Préfixe IPv4 | Quand l'utiliser |
|---|---|---|
| **Réseau** | `/n` | Joindre un réseau précis |
| **Hôte** | `/32` | Joindre **une seule machine** |
| **Par défaut** | `0.0.0.0/0` | Sortie vers Internet ou « tout le reste » |

> [!TIP]
> Le **next hop** peut être **l'adresse du routeur voisin** ou **l'interface de sortie**. Sur un lien Ethernet, préfère l'**adresse** du voisin.

### ✅ Vérifie que tu as compris

Un routeur de bordure doit envoyer **tout** ce qui est inconnu vers le FAI en `203.0.113.1`. Écris la commande.

<details markdown="1"><summary>Voir la réponse</summary>

`ip route 0.0.0.0 0.0.0.0 203.0.113.1`

</details>

## 2. La route flottante (*floating static route*)

Une route statique a une distance de **1**. Si on lui donne une distance **plus grande** (par exemple 200), elle **n'est pas utilisée** tant qu'une meilleure route existe : elle ne **flotte** que si la route principale disparaît. C'est un **secours**.

```text
ip route 0.0.0.0 0.0.0.0 10.0.12.2          ! principale (distance 1)
ip route 0.0.0.0 0.0.0.0 10.0.13.2 200      ! secours (distance 200)
```

> [!WARNING]
> **Le secours ne fonctionne que si la route principale disparaît de la table.** Elle disparaît quand l'**interface** de sortie tombe. Si le routeur voisin est en panne **mais** que le lien reste « up » (switch entre les deux, par exemple), la route principale **reste** et le secours ne s'active pas.

### ✅ Vérifie que tu as compris

Pourquoi donner une distance **supérieure à 110** à une route flottante qui sert de secours à OSPF ?

<details markdown="1"><summary>Voir la réponse</summary>

Pour qu'elle ne **concurrence pas** les routes OSPF (110) : tant qu'OSPF fonctionne, la statique flottante **perd**.

</details>

---

## 🧠 Quiz de fin

**1.** Comment s'écrit la route par défaut IPv6 ?

<details markdown="1"><summary>Voir la réponse</summary>

`ipv6 route ::/0 <next hop>`.

</details>

**2.** Quelle distance a une route statique par défaut ?

<details markdown="1"><summary>Voir la réponse</summary>

**1**.

</details>

**3.** Quel préfixe pour une route vers une seule machine ?

<details markdown="1"><summary>Voir la réponse</summary>

**/32** (IPv4) ou **/128** (IPv6).

</details>

**4.** Deux routes par défaut, distances 1 et 200. Laquelle est dans la table ?

<details markdown="1"><summary>Voir la réponse</summary>

Celle de distance **1**. L'autre n'apparaît que si la première disparaît.

</details>

➡️ Suite : [le TP du module](02-tp.md).
