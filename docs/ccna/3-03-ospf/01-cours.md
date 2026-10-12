# 📖 Cours – OSPFv2 mono-zone

*Parcours CCNA – Domaine 3 – module 3-03 (sujet 3.4)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** (le routage dynamique n'est pas au programme). C'est le plus gros sujet du domaine 3.

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer pourquoi on préfère le **routage dynamique** au routage statique ;
- [ ] décrire comment OSPF construit ses routes : **voisins**, **base de données**, **plus court chemin** ;
- [ ] configurer OSPF dans **une seule aire** ;
- [ ] expliquer le **router-id**, le **DR/BDR** et le coût.

---

## 1. Pourquoi OSPF ?

### 🤔 Avant de lire : à ton avis ?

Un réseau compte **30 routeurs**. Écrire toutes les routes à la main, et les corriger à chaque panne : est-ce réaliste ?

<details markdown="1"><summary>Voir la réponse</summary>

Non : trop long, trop d'erreurs, et rien ne se corrige **tout seul**. Le **routage dynamique** fait découvrir les routes **automatiquement** et s'adapte aux pannes.

</details>

**OSPF** (*Open Shortest Path First*) est un protocole à **état de liens** (*link-state*) :
1. Chaque routeur **découvre ses voisins** (messages *Hello*).
2. Chaque routeur **annonce l'état de ses liens** : tous les routeurs ont la **même carte** du réseau (la **LSDB**).
3. Chaque routeur calcule le **plus court chemin** (algorithme de Dijkstra) vers chaque réseau.

| Caractéristique | Valeur |
|---|---|
| Distance administrative | **110** |
| Métrique | **Coût** (basé sur la bande passante) |
| Messages | Multicast `224.0.0.5` (tous les routeurs OSPF) et `224.0.0.6` (DR/BDR) |
| Protocole | IP numéro **89** |

## 2. Voisins et adjacences

Deux routeurs deviennent **voisins** s'ils s'accordent sur : **même aire**, **même réseau (sous-réseau) sur le lien**, **mêmes temps Hello/Dead** (10 s / 40 s par défaut sur Ethernet), et compatibilité de l'**authentification**.

États (dans l'ordre) : **Down → Init → 2-Way → ExStart → Exchange → Loading → Full**. Un voisin sain est **Full**.

> [!NOTE]
> Sur un réseau **broadcast** (Ethernet), les routeurs élisent un **DR** (*Designated Router*) et un **BDR** (*Backup*) : seuls eux deviennent « Full » avec **tous** les autres. Les autres routeurs restent en **2-Way** entre eux. Sur un lien **point à point**, il n'y a **pas d'élection**.

**L'élection DR/BDR :** la plus **haute priorité** (par défaut 1) gagne ; à égalité, le **plus grand router-id**. Une priorité à **0** interdit de devenir DR.

## 3. Le router-id

Chaque routeur OSPF s'identifie par un **router-id** (une valeur au format d'adresse IPv4). Choix automatique, dans l'ordre :
1. celui **configuré** (`router-id 1.1.1.1`) ;
2. sinon la **plus haute adresse d'une interface loopback** ;
3. sinon la **plus haute adresse d'une interface active**.

> [!TIP]
> **Fixe toujours le router-id à la main** : il ne change plus, même si on modifie les adresses.

## 4. Configuration

```text
router ospf 1
 router-id 1.1.1.1
 network 192.168.1.0 0.0.0.255 area 0
 network 10.0.12.0 0.0.0.3 area 0
 passive-interface gigabitEthernet 0/0
```

| Commande | Rôle |
|---|---|
| `router ospf 1` | Active OSPF (le « 1 » est un numéro **local**, sans lien avec les voisins) |
| `network <réseau> <wildcard> area 0` | Active OSPF sur les **interfaces** dont l'adresse est dans ce réseau |
| `passive-interface <if>` | N'envoie **pas** de Hello sur cette interface (côté LAN : on annonce le réseau, mais pas de voisin à chercher) |
| `default-information originate` | Annonce une **route par défaut** aux voisins |

**Wildcard** = l'inverse du masque : `/24` → `0.0.0.255`, `/30` → `0.0.0.3`.

| Commande de vérification | Ce qu'elle montre |
|---|---|
| `show ip ospf neighbor` | voisins, état (FULL), interface |
| `show ip route ospf` | routes apprises par OSPF (code `O`) |
| `show ip ospf interface brief` | interfaces OSPF, coût, nombre de voisins |
| `show ip protocols` | résumé du protocole |

## 5. Le coût

**Coût = bande passante de référence ÷ bande passante de l'interface** (référence par défaut : **100 Mb/s**). FastEthernet = 1 ; 10 Mb/s = 10. Problème : tout lien ≥ 100 Mb/s a le **même coût de 1**. On corrige avec `auto-cost reference-bandwidth 1000` (ou plus) **sur tous les routeurs**.

### ✅ Vérifie que tu as compris

Deux routeurs ne deviennent pas voisins. Cite **trois** causes possibles.

<details markdown="1"><summary>Voir la réponse</summary>

Réseaux **différents** sur le lien (masques différents), **aires différentes**, **Hello/Dead** différents, interface **passive**, `network` mal écrit (wildcard faux), authentification différente.

</details>

---

## 🧠 Quiz de fin

**1.** Quelle est la distance administrative d'OSPF ?

<details markdown="1"><summary>Voir la réponse</summary>

**110**.

</details>

**2.** Quel état indique une adjacence complète ?

<details markdown="1"><summary>Voir la réponse</summary>

**Full**.

</details>

**3.** Que fait `passive-interface` ?

<details markdown="1"><summary>Voir la réponse</summary>

Il empêche l'envoi de Hello : on n'établit **pas de voisin** sur cette interface, mais son réseau est **toujours annoncé**.

</details>

**4.** Quelle wildcard pour un `/26` ?

<details markdown="1"><summary>Voir la réponse</summary>

**0.0.0.63**.

</details>

**5.** Comment est choisi le DR ?

<details markdown="1"><summary>Voir la réponse</summary>

Plus haute **priorité**, puis plus grand **router-id**.

</details>

➡️ Suite : [le TP du module](02-tp.md).
