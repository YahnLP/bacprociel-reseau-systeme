# 📖 Cours – CDP, LLDP et EtherChannel

*Parcours CCNA – Domaine 2 – module 2-03 (sujets 2.3 et 2.4)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] **découvrir** les équipements voisins avec **CDP** et **LLDP** ;
- [ ] expliquer l'intérêt d'un **EtherChannel** ;
- [ ] configurer un EtherChannel **LACP** et le vérifier.

---

## 1. CDP et LLDP : découvrir ses voisins

| | **CDP** | **LLDP** |
|---|---|---|
| Origine | **Cisco** (propriétaire) | **IEEE 802.1AB** (standard ouvert) |
| Activé par défaut ? | **Oui** sur les équipements Cisco | **Non** (à activer) |
| Commande d'activation | – | `lldp run` |
| Voir les voisins | `show cdp neighbors` | `show lldp neighbors` |
| Plus de détails | `show cdp neighbors detail` | `show lldp neighbors detail` |

Les deux protocoles envoient des messages **toutes les quelques dizaines de secondes** : nom de l'équipement, port, modèle, adresse de gestion.

> [!WARNING]
> **Sécurité :** CDP et LLDP donnent beaucoup d'informations à qui est branché. On les **désactive sur les ports vers les utilisateurs** (`no cdp enable`, `no lldp transmit`).
> **Dans le simulateur :** CDP est disponible ; LLDP **n'est pas** simulé. Apprends les commandes LLDP pour l'examen.

### ✅ Vérifie que tu as compris

Tu branches un switch Cisco à un switch d'une autre marque. CDP ou LLDP ?

<details markdown="1"><summary>Voir la réponse</summary>

**LLDP** : CDP est propre à Cisco.

</details>

---

## 2. EtherChannel

### 🤔 Avant de lire : à ton avis ?

Deux switchs sont reliés par **deux** câbles. Sans réglage, le spanning-tree en désactive un. Comment profiter des **deux** ?

<details markdown="1"><summary>Voir la réponse</summary>

En les **regroupant** en un seul lien logique : un **EtherChannel**.

</details>

Un **EtherChannel** regroupe plusieurs liens physiques en **un lien logique** (*Port-channel*) : plus de **débit** et de la **redondance**. Le spanning-tree voit **un seul lien**.

| Protocole | Standard | Modes |
|---|---|---|
| **LACP** | IEEE 802.3ad (ouvert) | `active` (propose) ou `passive` (attend) |
| **PAgP** | Cisco | `desirable` ou `auto` |
| **Statique** | – | `on` (sans négociation) |

**Règles de réussite :** les ports doivent avoir la **même vitesse**, le **même duplex**, le **même mode** (access ou trunk) et le **même VLAN natif**.

> [!TIP]
> Au moins **un** des deux côtés doit être `active` en LACP (`active–active` ou `active–passive`). Deux côtés `passive` : le lien **ne se forme jamais**.

```text
interface range fa0/23 - 24
 channel-group 1 mode active
 exit
interface port-channel 1
 switchport mode trunk
```

| Commande | Rôle |
|---|---|
| `show etherchannel summary` | état du groupe : `Po1(SU)` = couche 2, en service |
| `show interfaces port-channel 1` | détails du lien logique |

Dans `show etherchannel summary` : **S** = couche 2, **U** = en service, **P** = port groupé dans le Port-channel. `SD` = couche 2 **down** : le lien ne fonctionne pas.

### ✅ Vérifie que tu as compris

Dans le résultat `Po1(SU)  LACP  Fa0/23(P)  Fa0/24(P)`, que peux-tu affirmer ?

<details markdown="1"><summary>Voir la réponse</summary>

Le Port-channel 1 est de **couche 2**, **en service**, en **LACP**, avec **deux ports groupés**.

</details>

---

## 🔧 Dépanner : l'EtherChannel ne se forme pas

> [!NOTE]
> **Pourquoi ce chapitre ?** Un EtherChannel est un « faisceau » de liens physiques vus comme un seul. Il ne se forme que si **les deux côtés sont d'accord** (même protocole, modes compatibles, mêmes réglages sur tous les ports). S'ils ne le sont pas, les ports restent **seuls** (stand-alone) : le lien peut sembler fonctionner, mais sans l'agrégation attendue.

### La commande clé : `show etherchannel summary`

Faisceau sain (LACP, deux ports regroupés) :

```text
Group  Port-channel  Protocol    Ports
1      Po1(SU)       LACP        Fa0/23(P)  Fa0/24(P)
```

| Lettre | Signifie |
|---|---|
| `S` (sur Po) | **L**ayer 2 | 
| `U` (sur Po) | **in use** : le faisceau est en service |
| `P` (sur un port) | le port est **bundled** (regroupé) |
| `I` (sur un port) | le port est **stand-alone** : il n'a pas rejoint le faisceau |
| `D` (sur Po) | **down** : aucun port regroupé |

### Panne – « passive » des deux côtés

Les deux modes `passive` **attendent que l'autre commence** : personne ne propose, rien ne se forme. Sortie réelle du simulateur :

```text
SW1# show etherchannel summary
Group  Port-channel  Protocol    Ports
1      Po1(SD)       LACP        Fa0/23(I)  Fa0/24(I)
```

`Po1(SD)` et les ports en `(I)` : le faisceau est **down** et les ports sont seuls. **Correction :** mettre **au moins un** côté en `active` (`channel-group 1 mode active`).

### Les causes classiques (à vérifier une à une)

| Cause | Comment la voir | Correction |
|---|---|---|
| `passive` + `passive` (ou `auto` + `auto` en PAgP) | `(I)` / `Po1(SD)` | un côté en `active` |
| `on` d'un côté, LACP de l'autre | un côté regroupe, l'autre non (comportement réel du matériel) | même mode des deux côtés (LACP : `active`) |
| Ports aux réglages **différents** (vitesse, VLAN, trunk) | `show running-config` des ports | réglages identiques sur tous les ports du groupe |
| Un des câbles est coupé | `show interfaces status` | rétablir le lien |

> [!WARNING]
> **Limite du simulateur.** Le simulateur ne reproduit pas l'incohérence « `on` contre LACP » (il regroupe quand même). Le cas `passive`/`passive` est en revanche fidèle. Pour étudier le premier, utilise Packet Tracer 🧊.

---

## 🧠 Quiz de fin

**1.** Quel protocole de découverte est un standard IEEE ?

<details markdown="1"><summary>Voir la réponse</summary>

**LLDP**.

</details>

**2.** Deux côtés LACP en `passive` : le canal se forme-t-il ?

<details markdown="1"><summary>Voir la réponse</summary>

**Non** : l'un des deux doit être `active`.

</details>

**3.** Quelles conditions doivent respecter les ports d'un EtherChannel ?

<details markdown="1"><summary>Voir la réponse</summary>

Même **vitesse**, même **duplex**, même **mode** (access/trunk), même **VLAN natif**.

</details>

**4.** Quel est l'équivalent Cisco de LACP ?

<details markdown="1"><summary>Voir la réponse</summary>

**PAgP**.

</details>

➡️ Suite : [le TP du module](02-tp.md).
