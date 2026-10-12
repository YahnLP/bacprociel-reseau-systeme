# S11 – DHCP et DNS sur un serveur

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S11 – lundi 25 janvier 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S04 (DHCP, DNS observés), S06 (plan d'adressage), S10 (serveur) |
| **Référentiel** | C09 · C10 · DHCP, DNS (niv. 3) |

> [!NOTE]
> **Question qui guide la séance :** *« Le jour de l'ouverture, 40 postes arrivent : qui leur donne une adresse, une passerelle… et comment retrouvent-ils `intranet` sans taper une adresse IP ? »*

## 🎯 Objectifs

1. **Concevoir** un plan d'adresses (adresses fixes / plage DHCP / exclusions).
2. **Configurer** un serveur **DHCP** (pool, passerelle, DNS, durée du bail).
3. **Configurer** un serveur **DNS** (zone locale, enregistrements A).
4. **Vérifier** côté poste : `ipconfig /all`, `nslookup`, `ping nom`.
5. **Dépanner** « ça marche avec l'IP, pas avec le nom » et un mauvais DNS distribué.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Plan d'adresses, DHCP, bail, DNS, zone locale |
| [🛠️ TP](02-tp.md) | Configurer DHCP + DNS du serveur ; dépanner un serveur mal réglé |
| [📝 Aide-mémoire](03-aide-memoire-dhcp-dns.md) | Les champs à remplir + commandes de vérification |
| [`tp/p11-dhcp-dns.json`](tp/p11-dhcp-dns.json) | Simulateur : serveur sans service, postes en DHCP |
| [`tp/p11-dhcp-dns-panne.json`](tp/p11-dhcp-dns-panne.json) | Simulateur : DHCP/DNS en place mais 2 erreurs |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : les postes ont des adresses 169.254.x.x ; retour mission entreprise | Classe |
| 0 h 20 – 1 h 00 | **Mini-cours 1** : plan d'adresses, DHCP (§1–§2) | Classe |
| 1 h 00 – 1 h 50 | **TP A–B** : constater, configurer le DHCP | Binôme |
| 1 h 50 – 2 h 05 | Pause | |
| 2 h 05 – 2 h 30 | **Mini-cours 2** : DNS (§3) | Classe |
| 2 h 30 – 3 h 15 | **TP C–D** : DNS, tests de résolution | Binôme |
| 3 h 15 – 4 h 00 | **TP E–F** : dépannage (fichier panne), fiche de synthèse | Individuel |

## 🧪 Matériel et préparation

- Simulateur : `tp/p11-dhcp-dns.json` puis `p11-dhcp-dns-panne.json`.
- **Option VM réelle** (en prolongement, facultatif) : paquets `isc-dhcp-server` / `dnsmasq` sur la VM Ubuntu Server de S10.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **TP : 5 contrôles automatiques** | Adresses du pool, différentes, nom résolu, ping par nom |
| **Dépannage** | Fichier panne : 2 contrôles |
| **Fiche de synthèse** | Plan d'adresses complété |

## 🏭 Mission en entreprise

> *Relever sur un poste (`ipconfig /all`) : **qui est le serveur DHCP**, quelle est la **durée du bail**, quels **serveurs DNS** sont donnés. **Ne rien modifier.***

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- Le simulateur configure **le serveur par formulaires** (onglet *Services* → DHCP / DNS) : pas de fichier `dhcpd.conf`. C'est assumé : on travaille les **notions** (pool, exclusions, options, zone) ; la version fichiers peut être faite en VM (facultatif).
- **Exclusions** : le simulateur ne distribue jamais l'adresse d'une machine locale, mais on enseigne l'exclusion comme bonne pratique.
- **Redémarrage des postes** : après configuration, forcer un renouvellement (`ipconfig /renew` côté Windows, `dhclient` côté Linux) ou attendre quelques secondes.
- **Ne pas confondre** « le nom ne se résout pas » (DNS faux) et « le nom se résout mais l'hôte ne répond pas » (adresse fausse dans la zone) : la panne du TP les fait vivre.
- Réservation DHCP par adresse MAC : évoquée en cours, **non simulée**.
- Corrigés : `corriges/premiere/P11-corrige.md`, `P11-dhcp-dns-corrige.json`, `P11-dhcp-dns-panne-corrige.json`.

</details>
