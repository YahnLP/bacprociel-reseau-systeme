# 📖 Cours – Mettre en service par couches

*Bac Pro CIEL – Première – E31 – S17*

> [!IMPORTANT]
> **Une idée à la fois.** Réponds à la question **avant** de déplier la réponse.

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer pourquoi on met en service **couche par couche** ;
- [ ] expliquer le **relais DHCP** (`ip helper-address`) ;
- [ ] concevoir une **ACL** qui laisse passer le DHCP, le DNS et le web, et rien d'autre.

---

## 1. L'ordre de mise en service

### 🤔 Avant de lire : à ton avis ?

Tu as tout câblé et tout configuré d'un coup. **Rien ne marche.** Quel est le problème de cette méthode ?

<details markdown="1"><summary>Voir la réponse</summary>

On ne sait **pas où chercher** : câble ? VLAN ? adresse ? serveur ? ACL ? Quand **tout** est fait en même temps, il y a **dix causes possibles**. En testant **après chaque étape**, une panne a **une seule** cause possible : la dernière étape.

</details>

### 💡 L'idée

| Étape | On fait | On teste |
|---|---|---|
| 1 | Câblage | Voyants verts, `show interfaces status` |
| 2 | VLAN et ports du switch | `show vlan brief` |
| 3 | Routeur (interfaces) | `show ip interface brief`, `ping` de la passerelle |
| 4 | Serveur : adresses fixes | `ping` serveur ↔ passerelle |
| 5 | DHCP (+ relais), DNS, web | Un poste reçoit une adresse, résout, ouvre le site |
| 6 | Wi-Fi invité | Le portable reçoit une adresse du bon pool |
| 7 | **Filtrage (ACL)** — **en dernier** | Tests d'autorisation **et** d'interdiction |
| 8 | Sécurité + sauvegarde | `write memory`, copie du texte |

> [!TIP]
> **Le filtrage se met en dernier** : si on filtre trop tôt, on ne sait plus si une panne vient du **réseau** ou du **filtre**.

### ✅ Vérifie que tu as compris

Pourquoi sauvegarder **après chaque étape validée** ?

<details markdown="1"><summary>Voir la réponse</summary>

Si une étape casse tout, on **revient** à la dernière configuration qui marchait, au lieu de tout refaire.

</details>

---

## 2. Le relais DHCP

> [!EXAMPLE]+ 🚀 Pour aller plus loin
> Ce passage va **au-delà du référentiel** : il est utile au métier, mais **non exigé à l'épreuve terminale**.

### 🤔 Avant de lire : à ton avis ?

Le serveur DHCP est dans le réseau **Atelier**. Un poste de la **Direction** envoie sa demande DHCP en **diffusion**. Le serveur la reçoit-il ?

<details markdown="1"><summary>Voir la réponse</summary>

**Non.** Une diffusion **reste dans son réseau** : le routeur ne la transmet pas. Il faut que le routeur **relaie** la demande vers le serveur.

</details>

### 💡 L'idée

Sur l'interface du routeur côté Direction :

```text
interface gi0/0
 ip address 192.168.50.1 255.255.255.224
 ip helper-address 192.168.50.34
```

Le routeur **reçoit** la diffusion et la **retransmet** en direct (unicast) au serveur, en indiquant **de quel réseau** elle vient. Le serveur choisit alors **le bon pool** (celui de la Direction) et répond.

### ✅ Vérifie que tu as compris

Il y a **trois pools** sur le serveur. Comment sait-il lequel utiliser pour un poste de la Direction ?

<details markdown="1"><summary>Voir la réponse</summary>

Par l'**adresse de l'interface du routeur** qui relaie (ici `192.168.50.1`, dans le réseau 192.168.50.0/27) : le serveur prend le pool **du même réseau**.

</details>

---

## 3. Filtrer sans tout couper

Une ACL a un **« deny » implicite** à la fin. Pour les invités, il faut donc **autoriser explicitement** ce dont ils ont besoin :

| Besoin | Règle |
|---|---|
| Obtenir une adresse (DHCP) | `permit udp any eq 68 any eq 67` |
| Résoudre un nom (DNS) | `permit udp <réseau invités> host <serveur> eq 53` |
| Ouvrir le site | `permit tcp <réseau invités> host <serveur> eq 80` |
| Tout le reste | `deny ip any any` |

### ✅ Vérifie que tu as compris

Si tu oublies la règle DHCP, que se passe-t-il pour le portable invité ?

<details markdown="1"><summary>Voir la réponse</summary>

Il **n'obtient jamais d'adresse** (169.254.x.x) : sa demande est bloquée **avant** d'arriver au serveur. Le filtre est la cause, pas le réseau.

</details>

---

## 🧠 À retenir

- **Une couche, un test, une sauvegarde.**
- Le **relais DHCP** permet un serveur unique pour plusieurs réseaux.
- On filtre **en dernier** et on **teste ce qui est interdit** autant que ce qui est permis.
