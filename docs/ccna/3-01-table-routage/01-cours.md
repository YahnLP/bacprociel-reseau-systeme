# 📖 Cours – Table de routage et décision de transfert

*Parcours CCNA – Domaine 3 – module 3-01 (sujets 3.1 et 3.2)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** au niveau de détail demandé. Tu as déjà lu des tables de routage en Première (S07) : ici, on lit **toutes les colonnes**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] lire chaque ligne de `show ip route` : **code**, **préfixe**, **masque**, **next hop**, **distance administrative**, **métrique** ;
- [ ] expliquer la **passerelle par défaut** ;
- [ ] prévoir **quelle route** le routeur choisit.

---

## 1. Lire une ligne de la table

```text
R1#show ip route
S     192.168.3.0/24 [1/0] via 10.0.12.2
C     192.168.1.0/24 is directly connected, GigabitEthernet0/0
L     192.168.1.1/32 is directly connected, GigabitEthernet0/0
S*    0.0.0.0/0 [1/0] via 10.0.13.2
```

| Élément | Exemple | Signification |
|---|---|---|
| **Code** | `S`, `C`, `L`, `O` | Origine : **S**tatique, **C**onnecté, **L**ocal (l'adresse du routeur), **O** = OSPF |
| **Préfixe / masque** | `192.168.3.0/24` | Le réseau de destination |
| **Distance administrative** | `[1/…]` : le **1** | **Fiabilité** de la source de la route (plus petit = plus fiable) |
| **Métrique** | `[…/0]` : le **0** | **Coût** du chemin, propre à chaque protocole |
| **Next hop** | `via 10.0.12.2` | Le routeur suivant à qui envoyer le paquet |
| **Interface de sortie** | `GigabitEthernet0/0` | Par où le paquet sort |
| `*` | `S*` | Route **candidate par défaut** |

### Les distances administratives à retenir

| Source de la route | Distance administrative |
|---|---|
| Réseau **connecté** | **0** |
| Route **statique** | **1** |
| **EIGRP** (interne) | 90 |
| **OSPF** | **110** |
| **RIP** | 120 |

> [!NOTE]
> Quand **deux sources** connaissent le même réseau, le routeur garde celle qui a la **plus petite distance administrative**. La **métrique** ne départage que les routes **du même protocole**.

---

## 2. La décision de transfert (*forwarding decision*)

Pour chaque paquet, le routeur compare l'**adresse de destination** à **toutes** les routes et applique ces règles **dans l'ordre** :

1. **Plus long préfixe** (*longest prefix match*) : la route **la plus précise** (le plus grand `/n`) gagne.
2. En cas d'égalité de préfixe : la plus petite **distance administrative**.
3. En cas d'égalité de distance : la plus petite **métrique**.
4. Si tout est égal : le routeur **répartit** le trafic entre les routes (équilibrage).

### 🤔 Exemple

Le routeur a ces routes : `10.0.0.0/8`, `10.1.0.0/16`, `10.1.2.0/24`, `0.0.0.0/0`. Où part un paquet pour `10.1.2.77` ? Et pour `10.1.9.1` ? Et pour `8.8.8.8` ?

<details markdown="1"><summary>Voir la réponse</summary>

- `10.1.2.77` → `10.1.2.0/24` (le préfixe **le plus long** qui contient l'adresse).
- `10.1.9.1` → `10.1.0.0/16`.
- `8.8.8.8` → `0.0.0.0/0` : aucune autre route ne correspond, c'est la **route par défaut**.

</details>

### La passerelle de dernier recours

Si **aucune** route ne correspond et qu'il n'y a **pas de route par défaut**, le paquet est **jeté** (et le routeur renvoie « destination inaccessible »). La route `0.0.0.0/0` est la **passerelle de dernier recours** (*gateway of last resort*). Elle apparaît en haut de `show ip route`.

---

## 🧠 Quiz de fin

**1.** Que signifie le code `L` dans la table ?

<details markdown="1"><summary>Voir la réponse</summary>

Une route **locale** : l'adresse IP **du routeur lui-même**, en `/32`.

</details>

**2.** Une route OSPF et une route statique mènent au même réseau, avec le même préfixe. Laquelle est choisie ?

<details markdown="1"><summary>Voir la réponse</summary>

La **statique** (distance 1 < 110).

</details>

**3.** Routes : `192.168.0.0/16` et `192.168.3.0/24`. Destination `192.168.3.10`. Laquelle ?

<details markdown="1"><summary>Voir la réponse</summary>

Le **/24** : le **plus long préfixe** gagne, même si la distance de l'autre est meilleure.

</details>

**4.** Que fait un routeur sans route pour la destination ?

<details markdown="1"><summary>Voir la réponse</summary>

Il **jette** le paquet.

</details>

➡️ Suite : [le TP du module](02-tp.md).
