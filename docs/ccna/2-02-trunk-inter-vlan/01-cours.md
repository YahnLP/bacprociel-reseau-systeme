# 📖 Cours – Trunk, VLAN natif et routage inter-VLAN

*Parcours CCNA – Domaine 2 – module 2-02 (sujets 2.1 et 2.2)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** au niveau de détail demandé. Le routage inter-VLAN est vu en Terminale (S05) : ici, on ajoute le **VLAN natif** et la **sécurisation du trunk**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer ce qu'est un **trunk** et l'**étiquette 802.1Q** ;
- [ ] définir le **VLAN natif** et pourquoi on le change ;
- [ ] configurer un trunk entre deux switchs ;
- [ ] configurer le routage inter-VLAN avec un **routeur sur un bras** (*router-on-a-stick*).

---

## 1. Le trunk

### 🤔 Avant de lire : à ton avis ?

Deux switchs ont chacun des postes des VLAN 10 et 20. Combien de câbles faut-il entre eux pour que **chaque VLAN** communique ?

<details markdown="1"><summary>Voir la réponse</summary>

Sans astuce : **un câble par VLAN**. Avec un **trunk** : **un seul** câble transporte tous les VLAN.

</details>

Un **trunk** est une liaison qui transporte **plusieurs VLAN**. Pour que le switch en face sache de quel VLAN vient chaque trame, on ajoute une **étiquette** de 4 octets (*tag*) : c'est le **802.1Q**, qui contient notamment le **numéro de VLAN**.

```text
interface fa0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 switchport trunk native vlan 99
```

| Commande | Rôle |
|---|---|
| `show interfaces trunk` | ports en trunk, VLAN autorisés, VLAN natif |
| `switchport trunk allowed vlan` | limite les VLAN transportés |
| `switchport trunk native vlan 99` | choisit le VLAN natif |

## 2. Le VLAN natif

Sur un trunk, les trames du **VLAN natif** sont envoyées **sans étiquette**. Par défaut, c'est le **VLAN 1**.

> [!WARNING]
> **Les deux bouts doivent avoir le même VLAN natif**, sinon Cisco signale une erreur (`%CDP-4-NATIVE_VLAN_MISMATCH`) et le trafic est mélangé.
> **Bonne pratique de sécurité :** utiliser pour le natif un VLAN **inutilisé** (par exemple 99), jamais le VLAN 1 : cela limite les attaques par **VLAN hopping**.

### ✅ Vérifie que tu as compris

SW1 a le natif 99, SW2 a le natif 1. Que se passe-t-il ?

<details markdown="1"><summary>Voir la réponse</summary>

**Incohérence de VLAN natif** : les trames non étiquetées seront rangées dans le mauvais VLAN. Il faut le **même natif** des deux côtés.

</details>

---

## 3. Le routage inter-VLAN : routeur sur un bras

Deux VLAN ne se parlent que par un **routeur**. Avec **une seule** interface physique du routeur reliée au switch (en trunk), on crée **une sous-interface par VLAN**.

```text
interface gi0/0
 no shutdown
interface gi0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
interface gi0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
interface gi0/0.99
 encapsulation dot1Q 99 native
 ip address 192.168.99.1 255.255.255.0
```

Chaque sous-interface sert de **passerelle** au VLAN correspondant.

| Alternative | Principe |
|---|---|
| **Switch de couche 3** (SVI) | On crée `interface vlan 10` avec une adresse IP, et on active `ip routing` |

### ✅ Vérifie que tu as compris

Pourquoi appelle-t-on cette configuration « routeur sur un bras » ?

<details markdown="1"><summary>Voir la réponse</summary>

Parce qu'**une seule** interface physique est utilisée pour **tous** les VLAN : le trafic y **entre et en ressort** (comme sur un seul bras).

</details>

---

## 🧠 Quiz de fin

**1.** Quel standard définit l'étiquette VLAN sur un trunk ?

<details markdown="1"><summary>Voir la réponse</summary>

**IEEE 802.1Q**.

</details>

**2.** Quel VLAN est envoyé sans étiquette ?

<details markdown="1"><summary>Voir la réponse</summary>

Le **VLAN natif** (par défaut le VLAN 1).

</details>

**3.** Quelle commande affiche les trunks ?

<details markdown="1"><summary>Voir la réponse</summary>

`show interfaces trunk`.

</details>

**4.** Que fait `encapsulation dot1Q 20` sur une sous-interface ?

<details markdown="1"><summary>Voir la réponse</summary>

Elle indique que la sous-interface **traite les trames étiquetées VLAN 20**.

</details>

**5.** Pourquoi limiter les VLAN autorisés sur un trunk ?

<details markdown="1"><summary>Voir la réponse</summary>

Pour **ne transporter que les VLAN utiles** : meilleure sécurité et moins de trafic inutile.

</details>

➡️ Suite : [le TP du module](02-tp.md).
