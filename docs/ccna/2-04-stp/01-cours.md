# 📖 Cours – STP et Rapid PVST+

*Parcours CCNA – Domaine 2 – module 2-04 (sujet 2.5)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**. C'est l'un des sujets les plus importants du domaine 2.

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer **pourquoi** on a besoin du spanning-tree ;
- [ ] dire comment le **pont racine** (*root bridge*) est élu ;
- [ ] reconnaître les **rôles** et les **états** des ports ;
- [ ] configurer **Rapid PVST+**, **PortFast** et **BPDU guard**.

---

## 1. Le problème : la boucle

### 🤔 Avant de lire : à ton avis ?

Trois switchs sont reliés en triangle, pour la **redondance**. Un poste envoie une trame de **diffusion**. Que se passe-t-il ?

<details markdown="1"><summary>Voir la réponse</summary>

Chaque switch retransmet la diffusion aux deux autres, qui la retransmettent… **sans fin**. C'est une **tempête de diffusion** (*broadcast storm*) : le réseau est saturé en quelques secondes. Une trame Ethernet n'a **pas de durée de vie** (contrairement au TTL d'un paquet IP).

</details>

Le **spanning-tree** (STP) empêche les boucles : il **bloque** volontairement certains ports pour ne garder qu'un **arbre** sans boucle, et les réactive si un lien tombe.

## 2. L'élection du pont racine

Tous les switchs échangent des messages, les **BPDU**. Le switch ayant le **plus petit identifiant de pont** (*Bridge ID*) devient **racine** :

> **Bridge ID = priorité + numéro de VLAN + adresse MAC**

- La priorité par défaut est **32768** (+ le numéro de VLAN, donc 32769 pour le VLAN 1).
- Priorité égale → la **plus petite MAC** gagne.
- On peut la modifier par **multiples de 4096** : `spanning-tree vlan 1 priority 4096`.

> [!TIP]
> **Ne laisse jamais l'élection au hasard.** Sans réglage, le plus **vieux** switch (plus petite MAC) devient racine, parfois un petit switch d'accès. On force la racine sur un switch de **cœur**.

## 3. Rôles et états des ports

**Chemin le moins coûteux vers la racine.** Le coût dépend du débit :

| Débit | Coût (méthode courte) |
|---|---|
| 10 Mb/s | 100 |
| 100 Mb/s | 19 |
| 1 Gb/s | 4 |
| 10 Gb/s | 2 |

| Rôle | Signification |
|---|---|
| **Root port** | Le port d'un switch **non racine** qui mène à la racine au moindre coût (un par switch) |
| **Designated port** | Le port qui **transmet** sur chaque segment (tous les ports du pont racine le sont) |
| **Alternate port** | Le port **bloqué** qui offre un chemin de secours (Rapid PVST+) |
| **Backup port** | Un deuxième port sur le même segment (Rapid PVST+) |

| État STP classique | État Rapid PVST+ | Le port… |
|---|---|---|
| Blocking, Listening | **Discarding** | ne transmet pas de trafic |
| Learning | **Learning** | apprend les MAC mais ne transmet pas |
| Forwarding | **Forwarding** | transmet normalement |

## 4. Les variantes

| Version | Standard | Particularité |
|---|---|---|
| **STP (802.1D)** | IEEE | Convergence **lente** (30 à 50 s) |
| **PVST+** | Cisco | Un arbre **par VLAN** |
| **Rapid PVST+** | Cisco (basé sur 802.1w) | Un arbre par VLAN, convergence **rapide** (quelques secondes) |
| **MST (802.1s)** | IEEE | Un arbre pour un **groupe** de VLAN |

L'examen CCNA se concentre sur **Rapid PVST+**.

## 5. Configuration et protections

```text
spanning-tree mode rapid-pvst
spanning-tree vlan 1 priority 4096
interface fa0/1
 spanning-tree portfast
 spanning-tree bpduguard enable
```

| Fonction | Rôle |
|---|---|
| **PortFast** | Un port d'accès passe **immédiatement** en forwarding (poste, imprimante) |
| **BPDU guard** | Si un BPDU arrive sur un port PortFast, le port passe en **err-disabled** (protège contre un switch branché par erreur) |
| **BPDU filter** | Empêche l'envoi/réception de BPDU sur le port (à utiliser avec prudence) |
| **Root guard** | Empêche un switch voisin de **devenir racine** |
| **Loop guard** | Évite les boucles si les BPDU cessent d'arriver |

| Commande | Rôle |
|---|---|
| `show spanning-tree` | racine, priorité, rôle et état de chaque port |
| `show spanning-tree vlan 1` | idem pour un VLAN |
| `show spanning-tree summary` | résumé (mode, ports par état) |

### ✅ Vérifie que tu as compris

Un élève branche par erreur un petit switch sur une prise murale d'un poste. Le port est configuré avec PortFast + BPDU guard. Que se passe-t-il ?

<details markdown="1"><summary>Voir la réponse</summary>

Le switch envoie des **BPDU**. Le port reçoit un BPDU alors qu'il ne devrait pas : il passe en **err-disabled** (coupé), ce qui évite une boucle ou une prise de pouvoir de la racine.

</details>

---

## 🔧 Dépanner : « le pont racine n'est plus celui qu'on avait prévu »

> [!NOTE]
> **Pourquoi ce chapitre ?** STP élit lui-même un pont racine : si on ne force pas ce choix, ou si quelqu'un branche un switch mal réglé, **le chemin de tout le trafic peut changer sans qu'aucune alarme ne sonne**. Le réseau « marche », mais mal (liens saturés, chemins absurdes). Il faut donc savoir **vérifier qui est la racine**.

### La commande clé : `show spanning-tree root`

Situation voulue : `SW2` (priorité 4096) est la racine du VLAN 1.

```text
SW1# show spanning-tree root
VLAN0001         4097 0000.0c00.001c   19   2  20  2   Fa0/23
```

(priorité 4096 + numéro de VLAN 1 = **4097**).

### Panne – un switch d'accès prend la racine

Un autre switch est branché (ou reconfiguré) avec une priorité plus basse, ici `spanning-tree vlan 1 priority 0` sur `SW3`. Sortie réelle sur `SW1` :

```text
SW1# show spanning-tree root
VLAN0001         1 0000.0c00.0037     19   2  20  2   Fa0/24
```

Le **Root ID a changé** (priorité `1` = 0 + VLAN 1, autre adresse MAC) et **le port racine de `SW1` est passé de `Fa0/23` à `Fa0/24`** : le trafic ne prend plus le même chemin.

**Correction :** retirer le réglage du switch fautif (`no spanning-tree vlan 1 priority`) ; la racine redevient `SW2` après la convergence (vérifié dans le simulateur).

> [!TIP]
> **Prévention.** Fixer explicitement le pont racine et son secours (priorité 4096 et 8192), activer **PortFast + BPDU guard** sur les ports d'accès : un switch inconnu branché sur un port d'accès **coupe le port** (`err-disabled`) au lieu de prendre la racine.

### Autres symptômes à connaître

| Symptôme | Lecture | Piste |
|---|---|---|
| Réseau lent, voyants qui clignotent à toute vitesse | tempête de diffusion (boucle) | un lien redondant a été branché **sans STP** ou STP désactivé |
| Un port d'accès passe `err-disabled` | BPDU guard a réagi | un switch (ou un équipement qui émet des BPDU) a été branché dessus |
| Poste qui met 30 s à obtenir une adresse | le port passe par les états STP | PortFast manquant sur les ports d'accès |

---

## 🧠 Quiz de fin

**1.** Qui devient pont racine quand toutes les priorités sont égales ?

<details markdown="1"><summary>Voir la réponse</summary>

Le switch avec la **plus petite adresse MAC**.

</details>

**2.** Quelle est la priorité par défaut ?

<details markdown="1"><summary>Voir la réponse</summary>

**32768** (32769 pour le VLAN 1 avec l'extension de VLAN).

</details>

**3.** Combien de root ports par switch non racine ?

<details markdown="1"><summary>Voir la réponse</summary>

**Un seul**.

</details>

**4.** Quel est le coût d'un lien Gigabit ?

<details markdown="1"><summary>Voir la réponse</summary>

**4**.

</details>

**5.** À quoi sert PortFast ?

<details markdown="1"><summary>Voir la réponse</summary>

À faire passer **immédiatement** un port d'accès en forwarding, sans attendre la convergence.

</details>

➡️ Suite : [le TP du module](02-tp.md).
