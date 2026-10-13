# 📖 Cours – Commutation, table MAC et VLAN

*Parcours CCNA – Domaine 2 – module 2-01 (sujets 1.13 et 2.1)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** au niveau de détail demandé ici. Les VLAN de base sont vus en Première (S08) : on les retrouve, avec la **table MAC** et le **VLAN voix**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer comment un switch **apprend** les adresses MAC (*learning*, *flooding*, *aging*) ;
- [ ] lire `show mac address-table` ;
- [ ] créer des **VLAN** et affecter des ports ;
- [ ] expliquer le **VLAN voix** et le **VLAN de données**.

---

## 1. Comment un switch décide

### 🤔 Avant de lire : à ton avis ?

Un switch neuf vient d'être branché. Il ne connaît **aucune** adresse. Comment finit-il par savoir quel poste est sur quel port ?

<details markdown="1"><summary>Voir la réponse</summary>

En **regardant l'adresse source** de chaque trame reçue : il note « cette MAC est derrière ce port ».

</details>

| Étape | Nom | Ce que fait le switch |
|---|---|---|
| 1 | **Learning** (apprentissage) | Il note la **MAC source** et le **port d'arrivée** dans sa table |
| 2 | **Forwarding** (transfert) | Si la **MAC destination** est connue, il envoie **sur le seul bon port** |
| 3 | **Flooding** (inondation) | Si la destination est **inconnue** ou en **diffusion**, il envoie sur **tous les ports** sauf celui d'arrivée |
| 4 | **Aging** (vieillissement) | Une entrée **inutilisée** pendant **300 s** (par défaut) est effacée |

```text
SW1#show mac address-table
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    0050.7966.6801    DYNAMIC     Fa0/1
  10    0050.7966.6802    DYNAMIC     Fa0/2
```

| Commande | Rôle |
|---|---|
| `show mac address-table` | affiche la table |
| `show mac address-table dynamic` | seulement les adresses apprises |
| `clear mac address-table dynamic` | vide la table (utile pour tester) |

### ✅ Vérifie que tu as compris

PC1 envoie une trame vers PC2, que le switch n'a **jamais** vu. Où la trame est-elle envoyée ? Et ensuite, quand PC2 répond ?

<details markdown="1"><summary>Voir la réponse</summary>

Première trame : **flooding** sur tous les ports sauf celui de PC1. Quand PC2 répond, le switch **apprend** la MAC de PC2 : les trames suivantes sont envoyées sur **le seul port** de PC2.

</details>

---

## 2. Les VLAN

Un **VLAN** découpe un switch en **plusieurs réseaux logiques** : chaque VLAN est un **domaine de diffusion** séparé. Deux VLAN ne communiquent que par un **routeur** (ou un switch de couche 3).

```text
configure terminal
vlan 10
 name COMPTA
vlan 20
 name ATELIER
exit
interface range fa0/1 - 2
 switchport mode access
 switchport access vlan 10
```

| Commande | Rôle |
|---|---|
| `show vlan brief` | VLAN existants et leurs ports |
| `show interfaces fa0/1 switchport` | mode et VLAN d'un port |

> [!WARNING]
> **Plage normale :** les VLAN **1 à 1005** sont de la plage normale (au programme du CCNA). Le VLAN **1** est le VLAN par défaut : il **ne peut pas être supprimé**.

### 💡 VLAN de données et VLAN voix

Un téléphone IP se branche sur le switch, et le **poste** se branche **derrière le téléphone**. Un seul câble arrive au switch pour **deux flux**. On sépare :

- le **VLAN de données** (le poste) ;
- le **VLAN voix** (le téléphone), pour appliquer de la priorité (QoS).

```text
interface fa0/5
 switchport mode access
 switchport access vlan 10
 switchport voice vlan 150
```

---

## 🔧 Dépanner : « le poste ne joint pas son voisin »

> [!NOTE]
> **Pourquoi ce chapitre ?** Un technicien passe plus de temps à *réparer* qu'à *installer*. Sur un switch, presque toutes les pannes de VLAN viennent de **deux sources** : un port qui n'est pas dans le bon VLAN, ou un VLAN qui n'existe pas (ou plus). Les commandes ci-dessous les révèlent en dix secondes, si on sait les lire.

### Les trois commandes qui disent presque tout

| Commande | Ce qu'elle répond | À regarder |
|---|---|---|
| `show interfaces status` | Le port est-il **utilisable** ? | `connected` (ok), `notconnect` (pas de câble ou poste éteint), `disabled` (`shutdown`), `err-disabled` (coupé par une sécurité) |
| `show vlan brief` | Quel port est dans **quel VLAN** ? | le port du poste est-il dans le bon VLAN ? le VLAN existe-t-il ? |
| `show mac address-table` | Le switch **voit-il** le poste ? | l'adresse MAC du poste apparaît-elle, dans le bon VLAN ? |

### Panne 1 – Un poste est dans le mauvais VLAN

*Symptôme : `PC10A` joint bien tout le monde sauf `PC10B`, pourtant branchés « au même réseau ».*

Sortie réelle du simulateur après avoir placé `Fa0/1` dans le VLAN 20 par erreur :

```text
SW1# show vlan brief
VLAN Name                             Status    Ports
10   COMPTA                           active
20   ATELIER                          active    Fa0/1, Fa0/2
```

Le VLAN 10 est **vide** : le poste n'est plus dans le bon domaine de diffusion. Le ping vers son voisin du VLAN 10 : **100 % de perte**.

**Correction :** `interface fa0/1` puis `switchport access vlan 10`. **Vérification :** `show vlan brief`, puis un ping.

### Panne 2 – Le VLAN a été supprimé

*Symptôme : tous les postes d'un service tombent d'un coup.*

Après `no vlan 20`, les ports `Fa0/3` et `Fa0/4` **disparaissent de la liste** : ils sont toujours configurés `switchport access vlan 20`, mais ce VLAN n'existe plus, donc les ports sont **inactifs** (ils ne transmettent plus rien).

```text
SW1# show vlan brief
1    default      active    Fa0/5, Fa0/6, Fa0/7, ...
10   COMPTA       active    Fa0/1, Fa0/2
                            (plus de VLAN 20, plus de Fa0/3 ni Fa0/4)
```

**Correction :** recréer le VLAN (`vlan 20` puis `name ATELIER`). Les ports reviennent d'eux-mêmes (vérifié dans le simulateur).

> [!WARNING]
> **Leçon d'exploitation :** supprimer un VLAN ne remet **pas** les ports dans le VLAN 1. Avant `no vlan X`, on déplace d'abord les ports (`show vlan brief`).

### Panne 3 – Le port lui-même

| `show interfaces status` | Cause | Que faire |
|---|---|---|
| `notconnect` | câble débranché, mauvais port, poste éteint | tester le câble, regarder le voyant, changer de port |
| `disabled` | quelqu'un a tapé `shutdown` | `no shutdown` (en sachant **pourquoi** il avait été coupé) |
| `err-disabled` | une sécurité a coupé le port (voir [5-04](../5-04-securite-couche2/01-cours.md)) | trouver la cause **avant** de remettre le port en service |

> [!TIP]
> **Le réflexe en 3 temps :** ① le **port** est-il `connected` ? ② est-il dans le **bon VLAN** ? ③ le switch **apprend-il** l'adresse MAC du poste ? Si oui aux trois, le problème est plus haut (adresse IP, passerelle).

---

## 🧠 Quiz de fin

**1.** Que fait un switch quand il reçoit une trame dont la destination est inconnue ?

<details markdown="1"><summary>Voir la réponse</summary>

Il fait du **flooding** : il l'envoie sur tous les ports sauf celui d'arrivée.

</details>

**2.** Combien de temps une adresse MAC reste-t-elle dans la table sans trafic (par défaut) ?

<details markdown="1"><summary>Voir la réponse</summary>

**300 secondes** (5 minutes).

</details>

**3.** Deux postes de VLAN différents sont sur le même switch. Peuvent-ils se parler directement ?

<details markdown="1"><summary>Voir la réponse</summary>

Non, il faut un **routeur** ou un switch de couche 3.

</details>

**4.** Pourquoi un téléphone IP utilise-t-il un VLAN voix ?

<details markdown="1"><summary>Voir la réponse</summary>

Pour **séparer** et **prioriser** le trafic de voix par rapport au trafic de données.

</details>

➡️ Suite : [le TP du module](02-tp.md).
