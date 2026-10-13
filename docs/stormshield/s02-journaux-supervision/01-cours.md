# 📖 Cours – Journaux et supervision

*Parcours Stormshield – module S02*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours Stormshield (préparation CSNA).

## 🎯 À la fin de ce cours, tu sauras

- [ ] dire quelles **catégories de journaux** existent ;
- [ ] **lire** une ligne de journal de filtrage ;
- [ ] **trouver pourquoi** un flux est bloqué.

---

## 1. À quoi servent les journaux

Un pare-feu **note** ce qu'il fait : c'est la première source pour **dépanner** (« pourquoi mon flux ne passe pas ? »), **surveiller** (pics, attaques) et **prouver** (qui a fait quoi).

| Catégorie (exemples) | Contenu |
|---|---|
| **Trafic réseau** | connexions autorisées ou bloquées |
| **Alarmes** | attaques détectées (IPS) |
| **Web** | sites consultés (filtrage d'URL) |
| **Authentification** | connexions des utilisateurs |
| **Système** | démarrage, mises à jour, erreurs |
| **VPN** | tunnels montés ou tombés |

Sur un SNS, ils sont dans la rubrique **Notifications** (Journaux – Audit), avec des filtres par période, source, destination, service.

## 2. Lire une ligne de filtrage

| Champ | Signification |
|---|---|
| **Heure** | quand |
| **Action** | *Pass* (autorisé) ou *Block* (bloqué) |
| **Source / Destination** | qui parle à qui |
| **Protocole / port** | quel service |
| **Règle** | quelle règle a décidé (ou « politique par défaut ») |

> [!TIP]
> **Méthode de dépannage :** 1) refais le test qui échoue ; 2) cherche dans le journal la ligne qui correspond ; 3) regarde l'**action** et la **règle** ; 4) corrige la règle ; 5) **refais le test**.

## 3. Supervision

Au-delà des journaux, un SNS fournit des **tableaux de bord** et des **graphiques** (charge, débit, nombre de connexions, alarmes) pour repérer un comportement anormal dans la durée.

## 4. Dans le simulateur

Onglet **Journal** du pare-feu : une ligne par décision (autorisé ou bloqué) avec le **motif** (« règle 2 », « politique par défaut »). Le compteur **Hits** de chaque règle (onglet *Règles de filtrage*) montre aussi combien de fois elle a servi.

> [!NOTE]
> 🧊 **Limite du simulateur.** Pas de graphiques historiques ni de catégories (alarmes, web…). **Alternative Packet Tracer :** sur un routeur Cisco, `show access-lists` affiche des compteurs de correspondances, et `log` à la fin d'une ACL journalise (module [CCNA 5-03](../../ccna/5-03-acl/01-cours.md)).

## 🔧 Dépanner : lire le motif du journal

> [!NOTE]
> **Pourquoi ce chapitre ?** Un pare-feu qui bloque ne s'excuse pas : il écrit **pourquoi** dans son journal. Savoir lire le **motif** transforme « ça ne marche pas » en « la règle 3 est désactivée ». Les quatre motifs ci-dessous ont été relevés dans le simulateur.

### Les quatre cas à reconnaître

| Ce que dit le journal | Ce que ça veut dire | Où chercher |
|---|---|---|
| `BLOCK … règle 1` | une règle **précise** a bloqué le flux | est-ce la règle voulue ? n'est-elle pas **trop haut** dans la liste ? |
| `BLOCK … politique par défaut` | **aucune règle** n'a correspondu : tout ce qui n'est pas autorisé est refusé | règle manquante, **désactivée**, mauvaise **zone**, mauvais **port** |
| `BLOCK … connexion vers le pare-feu refusée` | le flux vise **le pare-feu lui-même** (son adresse) | une **redirection** (NAT) manque ou n'est pas appliquée |
| `PASS …` mais le service ne répond pas | le **filtrage n'est pas en cause** | NAT, route, passerelle du serveur, service arrêté |

> [!WARNING]
> **`PASS` ne veut pas dire « ça marche ».** Cela veut dire que le pare-feu a **laissé passer le paquet aller**. Si la réponse ne revient pas (pas de NAT, mauvaise passerelle sur le serveur), le journal affiche quand même `PASS`. Dans ce cas, **cherche ailleurs que dans les règles**.

### La méthode de lecture

1. **Refais le test** pendant que le journal est ouvert, pour retrouver *ta* ligne (adresse source, adresse destination, port).
2. Lis **l'action** (`PASS`/`BLOCK`), les **zones** (`LAN→DMZ`), puis le **motif**.
3. Si `BLOCK` : ouvre la règle citée (ou la liste, si c'est la politique par défaut) et compare avec le flux.
4. Si `PASS` mais ça échoue : le problème est **hors filtrage** (S04, S05).
5. Si **aucune ligne** n'apparaît pour ton test : le flux n'arrive pas jusqu'au filtrage (câblage, adresse, route) : voir [S04](../s04-configuration-reseau/01-cours.md).

---

## 🧠 Quiz de fin

**1.** Quelle est la première chose à regarder quand un flux ne passe pas ?

<details markdown="1"><summary>Voir la réponse</summary>

Le **journal de filtrage** : ligne correspondante, action et règle.

</details>

**2.** Que signifie un blocage « politique par défaut » ?

<details markdown="1"><summary>Voir la réponse</summary>

**Aucune règle** n'autorise ce flux : il faut en créer une (si le flux est légitime).

</details>

**3.** Cite deux catégories de journaux.

<details markdown="1"><summary>Voir la réponse</summary>

Par exemple : trafic réseau, alarmes, web, authentification, système, VPN.

</details>

➡️ Suite : [le TP du module](02-tp.md).
