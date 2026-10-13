# 📖 Cours – Le NAT sur un pare-feu

*Parcours Stormshield – module S05*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours Stormshield (préparation CSNA). Les bases du NAT sont dans le [module CCNA 4-01](../../ccna/4-01-nat/01-cours.md) et en Terminale.

## 🎯 À la fin de ce cours, tu sauras

- [ ] distinguer **masquerade**, **redirection** et **NAT 1:1** ;
- [ ] expliquer sur quelle adresse porte une règle de filtrage pour un flux publié ;
- [ ] configurer la **sortie** et la **publication** d'un serveur.

---

## 1. Trois usages

| Type | Sens | Exemple |
|---|---|---|
| **Translation de source** (*masquerade*) | du LAN vers Internet | tout le LAN sort avec l'adresse du pare-feu |
| **Redirection** (*destination NAT*) | d'Internet vers un serveur interne | `203.0.113.2:80` → `172.16.0.10:80` |
| **NAT bidirectionnel** (*1:1*) | un serveur a **sa propre** adresse publique | 203.0.113.5 ↔ 172.16.0.10 |

> [!NOTE]
> Le masquerade est le **PAT** vu en CCNA : plusieurs postes partagent une adresse, le pare-feu distingue les connexions par leur **port**.

## 2. NAT et filtrage vont ensemble

Le NAT **ne laisse rien passer** : c'est le **filtrage** qui autorise. Pour publier un serveur, il faut **deux** choses : la **redirection** *et* une **règle** qui autorise le flux.

| Étape | Rôle |
|---|---|
| **Règle de filtrage** | autorise `WAN → serveur`, TCP 80 |
| **Règle de NAT** (redirection) | remplace l'adresse publique par celle du serveur |

> [!WARNING]
> Sur un SNS, la documentation précise que la politique de filtrage est évaluée sur les adresses **avant** translation : pour joindre un serveur depuis Internet, c'est l'adresse **publique** (celle du pare-feu) qui apparaît comme destination de la règle ([documentation](https://documentation.stormshield.eu/SNS/v4/en/Content/User_Configuration_Manual_SNS_v4/Filtering_and_NAT/FILTERING_AND_NAT.htm)). Dans le simulateur, la règle se base sur la zone et le port et le résultat est identique tant que le **port ne change pas**.

## 3. Dans le simulateur

Onglet **NAT / redirections** :

| Zone interne | Zone externe | Effet |
|---|---|---|
| `LAN` | `WAN` | masquerade du LAN vers Internet |

Rubrique **Redirections de ports** : protocole, **port externe**, adresse et port **internes**.

> [!NOTE]
> 🧊 **Limite du simulateur.** Pas de NAT 1:1 avec une adresse publique dédiée, ni de règles de NAT détaillées (par source, par service). **Alternative Packet Tracer :** NAT sur un routeur Cisco : `ip nat inside source list … overload` (PAT) et `ip nat inside source static` (module [CCNA 4-01](../../ccna/4-01-nat/01-cours.md)).

## 🔧 Dépanner : les trois pannes du NAT

> [!NOTE]
> **Pourquoi ce chapitre ?** Le NAT et le filtrage sont **deux étages distincts** : le NAT *réécrit* les adresses, le filtrage *autorise ou refuse*. Une publication de service ne fonctionne que si **les trois éléments** sont présents : la **redirection**, la **règle de filtrage** correspondante, et un serveur qui **répond** correctement. Les pannes se reconnaissent à la façon dont le journal réagit.

### Panne 1 – Le masquerade est absent (accès Internet)

*Symptôme : `PC-ADMIN` n'ouvre plus aucun site d'Internet, alors que le site de la DMZ fonctionne.*

```text
PASS  192.168.1.10:49475 → 198.51.100.80:80  tcp [LAN→WAN]  règle 1
```

Le journal affiche **`PASS`** : le filtrage a laissé sortir le paquet. Mais il part avec une adresse **privée** (`192.168.1.10`) : Internet ne sait pas y répondre. **Signature :** `PASS` dans le journal, aucune réponse. **Correction :** recréer la règle de NAT « masquerade LAN → WAN ».

### Panne 2 – La redirection est absente (publication du site)

*Symptôme : depuis Internet, `http://203.0.113.2` ne répond plus.*

```text
BLOCK 198.51.100.20:50949 → 203.0.113.2:80  tcp [WAN→FW]  connexion vers le pare-feu refusée (WAN)
```

Sans redirection, la demande vise le **pare-feu lui-même** (zone `FW`), qui refuse les connexions WAN par défaut. **Signature :** destination = **adresse publique du pare-feu**, zone d'arrivée `FW`. **Correction :** recréer la redirection (`tcp 80` → `172.16.0.10:80`).

### Panne 3 – La règle de filtrage manque ou est désactivée

*Symptôme : la redirection existe, mais la publication ne marche pas.*

```text
BLOCK 198.51.100.20:50949 → 172.16.0.10:80  tcp [WAN→DMZ]  politique par défaut
```

Cette fois, l'adresse a bien été **traduite** (destination = `172.16.0.10`, le serveur), mais **aucune règle** `WAN→DMZ` n'autorise le flux : on tombe sur la **politique par défaut**. **Signature :** destination = **adresse du serveur**, zone `WAN→DMZ`, motif « politique par défaut ». **Correction :** créer (ou réactiver) la règle `WAN → DMZ, tcp 80`.

> [!TIP]
> **Comment les distinguer en un coup d'œil ?**
>
> | La destination du journal est… | Le NAT… | Le problème est… |
> |---|---|---|
> | l'**adresse publique** du pare-feu | n'a pas été appliqué | la **redirection** |
> | l'**adresse du serveur** | a été appliqué | le **filtrage** |
> | n'importe laquelle, mais `PASS` et pas de réponse | – | le **retour** (masquerade, passerelle du serveur) |

> [!WARNING]
> **Piège du simulateur.** Le simulateur filtre sur l'adresse et le port **après** traduction (adresse du serveur). Le matériel Stormshield réel évalue la politique de filtrage sur les adresses **avant** NAT (adresse publique). Écris donc tes règles en pensant au produit réel, et ne te fie pas au simulateur pour ce détail.

---

## 🧠 Quiz de fin

**1.** Quel type de NAT permet à tout le LAN de sortir avec une seule adresse ?

<details markdown="1"><summary>Voir la réponse</summary>

Le **masquerade** (PAT).

</details>

**2.** Pour publier un serveur web, que faut-il en plus de la redirection ?

<details markdown="1"><summary>Voir la réponse</summary>

Une **règle de filtrage** qui autorise le flux.

</details>

**3.** Quelle adresse est la destination d'un client Internet qui veut joindre le site publié ?

<details markdown="1"><summary>Voir la réponse</summary>

L'adresse **publique** du pare-feu (ou celle réservée au serveur en NAT 1:1).

</details>

➡️ Suite : [le TP du module](02-tp.md).
