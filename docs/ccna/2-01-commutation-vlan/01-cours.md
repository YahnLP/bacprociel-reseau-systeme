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
