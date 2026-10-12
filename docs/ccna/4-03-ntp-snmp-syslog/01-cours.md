# 📖 Cours – NTP, SNMP et syslog

*Parcours CCNA – Domaine 4 – module 4-03 (sujets 4.2, 4.4 et 4.5)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**. La supervision est abordée en Terminale (S10) avec un outil de tickets.

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer pourquoi tous les équipements doivent avoir **la même heure** (**NTP**) ;
- [ ] décrire **SNMP** : gestionnaire, agent, **MIB**, `get`, `set`, `trap` ;
- [ ] lire les **niveaux de gravité** de **syslog** (0 à 7) ;
- [ ] configurer syslog et SNMP sur un routeur.

---

## 1. NTP : une heure commune

### 🤔 Avant de lire : à ton avis ?

Un incident survient à 14 h 02. Les journaux de trois équipements indiquent 14:02, 14:09 et 13:58. Quel problème pour l'enquête ?

<details markdown="1"><summary>Voir la réponse</summary>

On **ne peut plus reconstituer l'ordre** des événements. Il faut la **même heure** partout.

</details>

**NTP** (*Network Time Protocol*, UDP **123**) synchronise les horloges sur un **serveur de temps**.

| Notion | Sens |
|---|---|
| **Strate** (*stratum*) | Distance à une horloge de référence. **Strate 0** : horloge atomique/GPS ; **strate 1** : serveur relié à elle ; chaque saut **+1** |
| **Client / serveur** | Le client se règle sur le serveur |

```text
ntp server 10.0.0.9          ! le routeur est CLIENT du serveur 10.0.0.9
ntp master 3                 ! le routeur devient serveur de temps (strate 3)
show ntp status
show ntp associations
```

> [!WARNING]
> **NTP n'est pas simulé** dans le simulateur : ces commandes servent pour l'examen. Dans le TP, on ne fait que **syslog** et **SNMP**.

## 2. SNMP : superviser à distance

| Élément | Rôle |
|---|---|
| **Gestionnaire** (*manager / NMS*) | Le serveur de supervision qui **interroge** |
| **Agent** | Le logiciel sur l'équipement qui **répond** |
| **MIB** | La « base » des informations disponibles (charge CPU, trafic, état d'interface…) |
| **OID** | L'adresse d'une information dans la MIB |

| Opération | Sens |
|---|---|
| `get` | Le gestionnaire **lit** une valeur |
| `set` | Le gestionnaire **modifie** une valeur |
| `trap` | L'agent **prévient** le gestionnaire d'un événement (sans qu'on lui demande) |

| Version | Sécurité |
|---|---|
| **SNMPv1 / v2c** | Une **communauté** (mot de passe) envoyée **en clair** |
| **SNMPv3** | **Authentification et chiffrement** : à utiliser |

```text
snmp-server community CIEL-RO RO       ! lecture seule
snmp-server location SalleServeurs
show snmp
```

> [!WARNING]
> Une communauté en **écriture** (`RW`) permet à un attaquant de **modifier** l'équipement. Préfère `RO`.

## 3. Syslog : les journaux

Les équipements envoient leurs messages à un **serveur syslog** (UDP **514**). Chaque message a une **gravité** :

| Niveau | Nom | Exemple |
|---|---|---|
| 0 | **Emergency** | Système inutilisable |
| 1 | **Alert** | Action immédiate |
| 2 | **Critical** | Condition critique |
| 3 | **Error** | Erreur |
| 4 | **Warning** | Avertissement |
| 5 | **Notice** | Événement normal important |
| 6 | **Informational** | Information |
| 7 | **Debugging** | Messages de débogage |

> [!TIP]
> Moyen mnémotechnique en anglais : **E**very **A**wesome **C**isco **E**ngineer **W**ill **N**eed **I**ce-cream **D**aily. Plus le **chiffre est petit**, plus c'est **grave**.

`logging trap warnings` envoie les niveaux **0 à 4** (warning **et plus grave**).

```text
logging host 10.9.0.10
logging trap warnings
logging buffered 4096
show logging
```

---

## 🧠 Quiz de fin

**1.** Quel port utilise NTP ?

<details markdown="1"><summary>Voir la réponse</summary>

UDP **123**.

</details>

**2.** Quel message SNMP part de l'agent sans qu'on l'interroge ?

<details markdown="1"><summary>Voir la réponse</summary>

Le **trap**.

</details>

**3.** Quel est le niveau syslog le plus grave ?

<details markdown="1"><summary>Voir la réponse</summary>

**0** (Emergency).

</details>

**4.** `logging trap errors` : quels niveaux sont envoyés ?

<details markdown="1"><summary>Voir la réponse</summary>

Les niveaux **0 à 3**.

</details>

**5.** Pourquoi SNMPv3 est-il préférable à v2c ?

<details markdown="1"><summary>Voir la réponse</summary>

Il **authentifie et chiffre** les échanges ; v2c envoie la communauté **en clair**.

</details>

➡️ Suite : [le TP du module](02-tp.md).
