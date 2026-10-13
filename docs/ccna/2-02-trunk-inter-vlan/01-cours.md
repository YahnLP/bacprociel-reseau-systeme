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

## 🔧 Dépanner : trunk et routage inter-VLAN

> [!NOTE]
> **Pourquoi ce chapitre ?** Le trunk et le routeur « sur un bras » font circuler **plusieurs VLAN sur un seul câble** : une seule erreur peut donc couper un VLAN, ou tous. La méthode : on commence **par le bas** (le lien est-il actif ?), puis on remonte (le VLAN passe-t-il sur le trunk ? le routeur répond-il dans ce VLAN ?).

### L'ordre des tests (du poste vers le routeur)

1. **Le poste joint sa passerelle ?** (`ping` de la passerelle). Non → le problème est entre le poste et le routeur (VLAN du port, trunk, sous-interface).
2. **Le poste joint un poste du même VLAN sur l'autre switch ?** Non → problème de **trunk** (VLAN autorisé ? lien actif ?).
3. **Le poste joint l'autre VLAN ?** Non alors que 1 et 2 marchent → problème de **routeur** (sous-interface, adresse, interface coupée).

### Panne 1 – Un VLAN manque sur le trunk

*Symptôme : le VLAN 10 fonctionne entre les deux switchs, le VLAN 20 ne passe plus (**100 % de perte**).*

```text
SW1# show interfaces trunk
Port        Vlans allowed on trunk
Fa0/23      10,20,99
Fa0/24      10,99            <- le VLAN 20 n'est plus autorisé
```

**Cause :** `switchport trunk allowed vlan 10,99` a **remplacé** la liste (sans `add`). **Correction :** `switchport trunk allowed vlan 10,20,99`.

> [!WARNING]
> `switchport trunk allowed vlan 30` **remplace** toute la liste. Pour ajouter : `switchport trunk allowed vlan add 30`.

### Panne 2 – VLAN natif différent des deux côtés

```text
SW1# show interfaces trunk         SW2# show interfaces trunk
Fa0/24  on  802.1q  trunking  99   Fa0/24  on  802.1q  trunking  1
```

Dans le simulateur, **le ping continue de passer** : seule la lecture de `show interfaces trunk` révèle l'erreur. Sur du matériel réel, elle provoque en plus des messages `%CDP-4-NATIVE_VLAN_MISMATCH` et peut faire « fuiter » du trafic d'un VLAN dans un autre.

> [!TIP]
> **Leçon :** une panne n'a pas toujours de symptôme visible. On **compare les deux bouts** d'un lien (`show interfaces trunk` des deux côtés) quand on met en service.

### Panne 3 – La sous-interface du routeur

*Symptôme : `PC10A` joint le switch et son propre VLAN, mais pas le VLAN 20.*

```text
R1# show running-config interface gi0/0.20
 encapsulation dot1Q 30          <- doit être 20
 ip address 192.168.20.1 255.255.255.0
```

`show ip interface brief` affiche pourtant `up/up` : **l'interface est active mais attend les trames d'un VLAN qui n'existe pas.** Un `up/up` ne prouve donc pas que la configuration est juste.

### Panne 4 – L'interface physique du routeur est coupée

```text
R1# show ip interface brief
GigabitEthernet0/0     unassigned   YES unset  administratively down down
```

**Correction :** `interface gi0/0` puis `no shutdown`. **Remarque :** quand l'interface physique tombe, **toutes** les sous-interfaces tombent avec elle : tous les VLAN perdent leur passerelle en même temps.

### Tableau de synthèse

| Symptôme | Commande | Cause probable |
|---|---|---|
| Un seul VLAN ne passe plus entre les switchs | `show interfaces trunk` | VLAN absent de `allowed vlan` |
| Un VLAN ne joint plus sa passerelle | `show running-config interface gi0/0.X` | mauvais numéro d'`encapsulation dot1Q` |
| Tous les VLAN perdent la passerelle | `show ip interface brief` | interface physique du routeur en `shutdown` |
| Rien ne se voit mais tout marche | `show interfaces trunk` des **deux** côtés | VLAN natif différent |

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
