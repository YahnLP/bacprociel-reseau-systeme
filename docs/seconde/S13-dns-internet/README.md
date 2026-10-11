# S13 – DNS et accès à Internet

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S13 – lundi 29 mars 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S11 (adresses), S12 (DHCP, passerelle, box) |
| **Référentiel** | C06 · C09 · savoir : IPv4 (niveau 3) · modèles IP (niveau 1, intuition) |

> [!NOTE]
> **Question qui guide la séance :** *« Quand je tape www.exemple.fr, comment mon PC sait-il où aller ? Et pourquoi, parfois, "j'ai Internet mais pas les sites" ? »*

## 🎯 Objectifs

1. **Expliquer** le rôle du **DNS** (nom → adresse) avec l'image de l'annuaire.
2. **Utiliser** `nslookup`, `ping` d'un **nom**, et `tracert` pour « voir » le chemin.
3. **Raconter** les étapes d'un accès web : DNS, passerelle, serveur.
4. **Distinguer** adresse **privée** et **publique** et **expliquer le NAT** en une image.
5. **Diagnostiquer** une **panne DNS** (« le ping par adresse marche, par nom non ») et la réparer.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | DNS, `nslookup`, chemin d'un accès web, `tracert`, NAT, panne DNS |
| [🛠️ TP](02-tp.md) | Observer, casser, réparer, lire la table NAT, schéma final |
| [`tp/s13-dns.json`](tp/s13-dns.json) | Simulateur : 3 postes, box, Internet (FAI, DNS, site web) ; un poste a un DNS erroné |
| [📝 Schéma et mini-QCM](03-schema-qcm.md) | Évaluation formative à rendre |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : *« Sans votre répertoire, sauriez-vous appeler vos amis ? »* ; retour mission entreprise | Oral |
| 0 h 20 – 0 h 50 | **Mini-cours 1** : le DNS, l'annuaire (cours §1) | Classe |
| 0 h 50 – 1 h 40 | **TP A–B** : `nslookup`, `ping` par nom, navigateur | Binôme |
| 1 h 40 – 1 h 55 | Pause | |
| 1 h 55 – 2 h 25 | **Mini-cours 2** : le chemin d'un accès web, `tracert` (§2–§3) | Classe |
| 2 h 25 – 3 h 05 | **TP C–D** : `tracert`, panne DNS du poste PC2, réparation | Binôme |
| 3 h 05 – 3 h 25 | **Mini-cours 3 + TP E** : adresse privée / publique, NAT (§4) | Binôme |
| 3 h 25 – 4 h 00 | **Schéma + mini-QCM** (évaluation formative), bilan | Individuel |

## 🧪 Matériel et préparation

- Simulateur avec `tp/s13-dns.json` (la box, le FAI, le DNS public et le site `www.exemple.fr` sont déjà en place).
- Quelques vrais postes connectés à Internet : pour `nslookup` et `ping` d'un vrai site (si le réseau de l'établissement l'autorise).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Schéma « Comment mon PC atteint un site web » + mini-QCM** | [Fiche](03-schema-qcm.md), formatif (compétence C06 en lecture de schéma) |
| Oral | « C'est quoi le DNS ? Que veut dire 'je pingue l'adresse mais pas le nom' ? » |

## 🏭 Mission en entreprise

> *Avec l'accord du tuteur, tester `nslookup` ou `ping` sur un nom et noter le serveur DNS utilisé.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Pas de DNS en détail** : pas de hiérarchie ni d'enregistrements autres que « nom → adresse ». Les types d'enregistrements et la hiérarchie sont vus en Première.
- Le **NAT** est présenté **en une image**, comme demandé par le plan. La table NAT de la box se lit dans l'onglet **Console (CLI)** de la BOX : `show ip nat translations` (une seule commande à donner).
- Dans le simulateur, le site de test est `www.exemple.fr` (adresse `198.51.100.80`) ; le DNS public est `198.51.100.53`. Les adresses en `203.0.113.0/24` et `198.51.100.0/24` sont des adresses **réservées à la documentation** : aucun risque de confusion avec le réel.
- `tracert` : le 2ᵉ saut peut afficher « Délai d'attente… » (équipement qui ne répond pas) : le préciser, c'est normal.
- Panne DNS : le poste PC2 a un DNS erroné (`198.51.100.99`). Après correction (DNS = `192.168.1.1`, la box), le site s'ouvre.
- Corrigé : `corriges/seconde/S13-corrige.md` et `S13-dns-corrige.json` (non publiés).

</details>
