# 📖 Cours – Les objets

*Parcours Stormshield – module S03*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours Stormshield (préparation CSNA).

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer pourquoi on utilise des **objets** plutôt que des adresses saisies à la main ;
- [ ] distinguer les types d'objets : **hôte, réseau, plage, groupe, service** ;
- [ ] nommer correctement tes objets.

---

## 1. Pourquoi des objets ?

Dans une règle de pare-feu, on n'écrit pas « 192.168.1.10 » mais le **nom** d'un objet (`srv_web`, `net_lan`). Avantages : la règle se **lit** toute seule, et si l'adresse du serveur change, on la modifie **une fois** dans l'objet et toutes les règles suivent.

## 2. Les types d'objets

| Type | Exemple | Contient |
|---|---|---|
| **Hôte** (*host*) | `srv_web` | une adresse : 172.16.0.10 |
| **Réseau** (*network*) | `net_lan` | 192.168.1.0/24 |
| **Plage** (*range*) | `plage_dhcp` | 192.168.1.100 à 192.168.1.200 |
| **Groupe** (*group*) | `grp_admins` | plusieurs objets réunis |
| **Service** (*port*) | `https` | protocole + port : TCP 443 |
| **Nom de domaine** (*FQDN*) | `www_exemple` | un nom DNS |

Les pare-feux Stormshield créent déjà des objets utiles : les **interfaces** (`Firewall_in`, `Firewall_out`…), des services courants (`http`, `https`, `dns`…) et des réseaux internes.

## 3. Bonnes pratiques de nommage

| À faire | Exemple |
|---|---|
| un **préfixe** pour le type | `srv_`, `net_`, `grp_` |
| un nom **parlant** | `srv_web_dmz` plutôt que `objet1` |
| **pas d'espaces** ni d'accents | `net_compta` |
| **supprimer** les objets inutilisés | ménage régulier |

> [!TIP]
> Un bon nommage rend la politique de filtrage **lisible par un collègue** qui reprend le pare-feu.

## 4. Dans le simulateur

> [!NOTE]
> 🧊 **Limite du simulateur.** Il n'a **pas de menu Objets** : dans une règle, tu saisis directement l'adresse (`192.168.1.10/32`) ou le réseau (`192.168.1.0/24`) et le port (`80,443`). Le principe est le même, la lisibilité en moins : **note le nom de l'objet dans le commentaire** de la règle. **Alternatives :** (1) **VM Stormshield EVA** (TP du module) ; (2) **Packet Tracer** : les listes d'accès Cisco peuvent utiliser des **groupes d'objets** (`object-group`) sur certains équipements (ASA) ; sur un routeur, les ACL nommées jouent un rôle proche (module [CCNA 5-03](../../ccna/5-03-acl/01-cours.md)).

## 🔧 Dépanner : les objets

> [!NOTE]
> **Pourquoi ce chapitre ?** Un objet est utilisé par **plusieurs** règles. Une erreur dans l'objet se propage donc **partout** : c'est pratique quand on corrige, dangereux quand on se trompe.

| Symptôme | Cause fréquente | Vérification |
|---|---|---|
| Une règle « ne correspond jamais » | l'objet a un **mauvais masque** ou une mauvaise adresse | relire l'objet (adresse **et** masque) |
| Plusieurs règles changent de comportement d'un coup | un objet partagé a été modifié | chercher où l'objet est utilisé avant de le modifier |
| Un objet « nom de machine » ne fonctionne pas | résolution DNS impossible | tester la résolution du nom depuis le pare-feu |
| Règle illisible | objets nommés `obj1`, `obj2`… | donner des **noms explicites** (`SRV-WEB-DMZ`, `LAN-COMPTA`) |

---

## 🧠 Quiz de fin

**1.** Pourquoi utiliser un objet plutôt qu'une adresse dans une règle ?

<details markdown="1"><summary>Voir la réponse</summary>

Pour la **lisibilité** et pour modifier l'adresse **à un seul endroit**.

</details>

**2.** Quel type d'objet réunit plusieurs hôtes ?

<details markdown="1"><summary>Voir la réponse</summary>

Un **groupe**.

</details>

**3.** Que contient un objet « service » ?

<details markdown="1"><summary>Voir la réponse</summary>

Un **protocole** et un **port** (par exemple TCP 443).

</details>

➡️ Suite : [le TP du module](02-tp.md).
