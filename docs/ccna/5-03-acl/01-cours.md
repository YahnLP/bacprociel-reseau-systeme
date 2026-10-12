# 📖 Cours – Listes de contrôle d'accès (ACL)

*Parcours CCNA – Domaine 5 – module 5-03 (sujet 5.6)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** au niveau de détail demandé. Tu as vu une ACL pour isoler les invités au Wi-Fi (Terminale S06) : ici, on la comprend **en profondeur**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] écrire une ACL **standard** et une ACL **étendue** ;
- [ ] expliquer les **wildcards** ;
- [ ] **placer** une ACL au bon endroit et dans le bon sens ;
- [ ] vérifier avec `show access-lists`.

---

## 1. Qu'est-ce qu'une ACL ?

Une **ACL** (*Access Control List*) est une **liste de règles** `permit` / `deny` que le routeur lit **de haut en bas** pour chaque paquet.

> [!WARNING]
> **Trois règles d'or :**
> 1. Le routeur s'arrête à la **première règle** qui correspond.
> 2. Il y a un **`deny any` implicite** à la fin de chaque ACL : ce qui n'est pas autorisé est **refusé**.
> 3. **L'ordre compte** : les règles précises **avant** les règles générales.

### 🤔 Avant de lire : à ton avis ?

Une ACL contient : `1. permit ip any any` puis `2. deny ip host 192.168.10.12 any`. Le poste `192.168.10.12` est-il bloqué ?

<details markdown="1"><summary>Voir la réponse</summary>

**Non** : la règle 1 autorise tout, le routeur s'arrête là. Il faut **inverser** l'ordre.

</details>

## 2. Les wildcards

Une **wildcard** est l'**inverse du masque** : `0` = « ce bit doit être **identique** », `1` = « peu importe ».

| Masque | Wildcard | Signification |
|---|---|---|
| 255.255.255.0 | **0.0.0.255** | Tout le `/24` |
| 255.255.255.252 | **0.0.0.3** | Un `/30` |
| 255.255.255.255 | **0.0.0.0** | Une seule adresse (`host`) |
| 0.0.0.0 | **255.255.255.255** | Toutes les adresses (`any`) |

Raccourcis : `host 10.0.0.5` = `10.0.0.5 0.0.0.0` ; `any` = `0.0.0.0 255.255.255.255`.

## 3. Standard ou étendue ?

| | **ACL standard** | **ACL étendue** |
|---|---|---|
| Critère | **Adresse source** seulement | Source, **destination**, **protocole**, **ports** |
| Numéros | 1–99 et 1300–1999 | 100–199 et 2000–2699 |
| Placement conseillé | **Près de la destination** | **Près de la source** |

```text
! Standard nommée : seul le poste admin passe
ip access-list standard ADMIN
 permit host 10.0.0.2
 deny any log

! Étendue nommée
ip access-list extended VERS-SERVEUR
 deny ip host 192.168.10.12 any
 permit tcp host 192.168.10.11 host 192.168.20.10 eq 80
 deny ip any any
```

**Appliquer** sur une interface, avec un **sens** :

```text
interface gigabitEthernet 0/0
 ip access-group VERS-SERVEUR in
```

| Sens | Quand la règle s'applique |
|---|---|
| **in** | Au paquet qui **entre** dans l'interface |
| **out** | Au paquet qui **sort** de l'interface |

**Protéger l'accès distant :** `line vty 0 4` puis `access-class ADMIN in`.

| Commande | Rôle |
|---|---|
| `show access-lists` | règles et **compteurs** de correspondance |
| `show ip interface gi0/0` | ACL appliquée à l'interface, par sens |

### ✅ Vérifie que tu as compris

Où placer une ACL **étendue** qui refuse le trafic d'un poste vers un serveur : près du poste ou près du serveur ? Pourquoi ?

<details markdown="1"><summary>Voir la réponse</summary>

**Près de la source** (le poste) : le trafic refusé n'a **pas à traverser** tout le réseau pour être jeté.

</details>

---

## 🧠 Quiz de fin

**1.** Que se passe-t-il si un paquet ne correspond à aucune règle ?

<details markdown="1"><summary>Voir la réponse</summary>

Il est **refusé** (`deny any` implicite).

</details>

**2.** Quelle wildcard pour `192.168.4.0/22` ?

<details markdown="1"><summary>Voir la réponse</summary>

**0.0.3.255**.

</details>

**3.** ACL standard : filtre-t-elle sur le port de destination ?

<details markdown="1"><summary>Voir la réponse</summary>

**Non**, seulement sur l'**adresse source**.

</details>

**4.** Quelle commande applique l'ACL `WEB` aux paquets entrants sur une interface ?

<details markdown="1"><summary>Voir la réponse</summary>

`ip access-group WEB in`.

</details>

➡️ Suite : [le TP du module](02-tp.md).
