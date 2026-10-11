# 📖 Cours – Accéder à distance, en sécurité

*Bac Pro CIEL – Terminale – E31 – S09*

> [!IMPORTANT]
> **Une idée à la fois.** Réponds à la question **avant** de déplier la réponse.

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer pourquoi **telnet** est dangereux et **SSH** protégé ;
- [ ] configurer **SSH** sur un routeur ;
- [ ] **publier** un service par redirection de port et **en citer les risques** ;
- [ ] dire à quoi sert un **VPN** ;
- [ ] **appliquer** les règles de télémaintenance.

---

## 1. Telnet ou SSH ?

### 🤔 Avant de lire : à ton avis ?

Tu te connectes à un routeur depuis un café. Le mot de passe passe **en clair** dans le Wi-Fi. **Qui peut le lire ?**

<details markdown="1"><summary>Voir la réponse</summary>

**Toute personne** qui écoute le Wi-Fi ou un point du chemin (appareil compromis, réseau public). Avec telnet, le mot de passe voyage **tel quel**.

</details>

### 💡 L'idée

| | Telnet | SSH |
|---|---|---|
| Port | 23 | 22 |
| Chiffrement | **non** | **oui** |
| Mot de passe | visible en clair | protégé |
| Usage | à **bannir** | à **utiliser** |

```text
ip domain-name garage.local
username tech privilege 15 secret Tech#2027
crypto key generate rsa modulus 1024
ip ssh version 2
line vty 0 4
 transport input ssh
 login local
```

Puis de ton poste : `ssh tech@192.168.1.1`.

> [!TIP]
> **Un compte nominatif par technicien** (`tech`, `lucas`, …) : on sait **qui** a fait **quoi**, et on retire un compte sans changer celui des autres.

### ✅ Vérifie que tu as compris

Que signifie `transport input ssh` sur les lignes `vty` ?

<details markdown="1"><summary>Voir la réponse</summary>

Que **seul SSH** est accepté pour se connecter à distance : **telnet est refusé**.

</details>

---

## 2. La redirection de port : montrer un service à Internet

### 🤔 Avant de lire : à ton avis ?

Un restaurateur veut que ses clients voient sa carte sur un petit serveur installé **dans** son local. Comment un visiteur d'Internet peut-il l'atteindre, alors que le serveur a une adresse **privée** ?

<details markdown="1"><summary>Voir la réponse</summary>

Il ne peut **pas** l'atteindre directement (adresse privée). Il faut que le routeur **redirige** les connexions arrivant sur son adresse **publique** vers le serveur : c'est la **redirection de port**.

</details>

### 💡 L'idée

```text
ip nat inside source static tcp 192.168.1.10 80 203.0.113.3 8080
```

« Ce qui arrive sur **203.0.113.3 : 8080** est envoyé vers **192.168.1.10 : 80**. »

> [!WARNING]
> **Un port ouvert est visible de tous** : des robots scannent Internet en permanence. On ne publie que **le strict nécessaire**, on **protège** le service (mot de passe fort, mises à jour) et on le place si possible dans une zone isolée.

| Service | À exposer directement sur Internet ? |
|---|---|
| Site web public | oui, avec précautions |
| **Bureau à distance (RDP)** | **jamais** : passer par un **VPN** |
| Administration du routeur | **jamais** : passer par un **VPN** |

### ✅ Vérifie que tu as compris

Pourquoi utilise-t-on le port **8080** à l'extérieur alors que le serveur écoute sur le **80** ?

<details markdown="1"><summary>Voir la réponse</summary>

Pour **ne pas utiliser le port standard** (très scanné) et pour pouvoir publier **plusieurs** services : 8080 → serveur A, 8081 → serveur B. Les postes de l'extérieur doivent alors taper `:8080`.

</details>

---

## 3. Le VPN : entrer dans le réseau comme si on y était

### 🤔 Avant de lire : à ton avis ?

Un commercial est en déplacement et veut accéder au **dossier partagé** de l'entreprise. Publier le serveur de fichiers sur Internet, est-ce une bonne idée ?

<details markdown="1"><summary>Voir la réponse</summary>

**Non**, c'est dangereux. La bonne solution est un **VPN**.

</details>

### 💡 L'idée

> **Un VPN est un tunnel chiffré** entre ton poste et le réseau de l'entreprise. Une fois connecté, tu es **comme au bureau** (adresse interne, accès aux dossiers) sans exposer les serveurs.

| | Redirection de port | VPN |
|---|---|---|
| Ce qui est exposé | le service | **uniquement** la porte d'entrée du VPN |
| Authentification | celle du service | compte (+ souvent code) |
| Risque | élevé | **plus faible** |

En Terminale, tu **utilises un VPN déjà configuré** : tu vérifies la connexion (adresse reçue, accès au serveur) et tu sais l'expliquer.

### ✅ Vérifie que tu as compris

Tu es connecté en VPN depuis chez toi. **Quelle adresse** as-tu pour le serveur de fichiers ?

<details markdown="1"><summary>Voir la réponse</summary>

L'adresse **interne** (par ex. `192.168.1.10`), comme si tu étais sur place : c'est tout l'intérêt du VPN.

</details>

---

## 4. Les règles de télémaintenance

### 🤔 Avant de lire : à ton avis ?

Un technicien se connecte la nuit au réseau d'un client « pour aider ». Le client ne le sait pas. **Qu'est-ce qui ne va pas ?**

<details markdown="1"><summary>Voir la réponse</summary>

**Tout** : pas d'**autorisation**, pas de **trace**. Même bien intentionné, c'est une **intrusion** dans un système informatique.

</details>

### 💡 L'idée

**Avant une intervention à distance :**

1. **Autorisation** du client (écrite, même par e-mail).
2. **Compte nominatif** du technicien (pas de compte partagé).
3. **Périmètre** : quels équipements, quelle durée.
4. **Journal** : date, heure, actions, résultat.
5. **Fermeture** : on retire ou désactive l'accès à la fin.

### ✅ Vérifie que tu as compris

Un collègue te donne le mot de passe du compte `admin` pour que tu dépannes à sa place. **Que dis-tu ?**

<details markdown="1"><summary>Voir la réponse</summary>

Que chacun doit avoir **son propre compte** : sinon on ne sait plus **qui** a fait **quoi**, et on ne peut pas retirer l'accès d'un seul.

</details>

---

## 🧠 À retenir

- **SSH (22) chiffre ; telnet (23) non.** `transport input ssh`.
- **Compte nominatif** par technicien.
- **Redirection de port** : un port ouvert est vu de tous ; on publie le **minimum**.
- **VPN** : tunnel chiffré, on entre **dans** le réseau sans exposer les serveurs.
- **Télémaintenance** : autorisation, compte, périmètre, journal.
