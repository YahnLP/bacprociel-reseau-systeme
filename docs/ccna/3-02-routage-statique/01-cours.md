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

## 🔧 Dépanner : « je pinge, ça ne répond pas »

> [!NOTE]
> **Pourquoi ce chapitre ?** Une route statique, c'est **une promesse écrite à la main** : si l'adresse, le masque ou le prochain saut est faux, rien ne vous le dit. Et le routage est **à double sens** : le paquet aller doit connaître le chemin, mais la **réponse** aussi.

### La méthode : suivre le paquet saut par saut

1. `show ip route` sur le routeur de départ : existe-t-il une route vers le réseau d'arrivée ?
2. `traceroute` depuis le poste : **jusqu'à quel saut** ça répond ? Le premier `* * *` désigne le routeur **suivant** le dernier qui répond, ou son chemin de retour.
3. Recommencer **dans l'autre sens**, depuis le routeur qui s'est tu.

### Panne 1 – La route de retour manque

*Symptôme : `ping` de `PC1` vers `PC3` : 100 % de perte, alors que la route aller est correcte.*

```text
PC1$ traceroute 192.168.3.10
 1  192.168.1.1   0.231 ms
 2  10.0.12.2     0.332 ms
 3  * * *
 4  * * *
```

On atteint `R2`, puis plus rien. Sur `R3`, `show ip route` ne contient **aucune route vers 192.168.1.0/24** : le paquet arrive à `PC3`, mais **la réponse ne sait pas revenir**.

**Correction :** `ip route 192.168.1.0 255.255.255.0 10.0.13.1` sur `R3`.

> [!WARNING]
> **Règle d'or :** chaque réseau a besoin d'une route **dans les deux sens**. Un ping qui échoue ne dit pas si c'est l'aller ou le retour.

### Panne 2 – Mauvais prochain saut… masqué par la route de secours

On remplace la route principale par un prochain saut inexistant (`10.0.12.9`). Résultat : **le ping marche encore**.

```text
R1# show ip route static
S    192.168.3.0/24 [200/0] via 10.0.13.2     <- seule la route de SECOURS reste
```

La route de secours (distance 200) a pris le relais : l'utilisateur ne voit **rien**, mais le trafic passe maintenant par le chemin de secours, **moins bon**.

> [!TIP]
> **Leçon :** une redondance qui fonctionne **cache** les pannes. Après chaque modification, on contrôle `show ip route` (route principale présente, distance `[1/0]`) et pas seulement le ping.

### Tableau de synthèse

| Symptôme | Commande | Cause |
|---|---|---|
| Ping aller sans réponse, `traceroute` s'arrête | `show ip route` sur le routeur **suivant** | route de retour absente |
| Ping OK mais chemin inattendu | `show ip route` / `traceroute` | route principale absente, secours actif |
| `Destination Net Unreachable` renvoyé par un routeur | `show ip route <destination>` sur ce routeur | aucune route vers la destination |

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
