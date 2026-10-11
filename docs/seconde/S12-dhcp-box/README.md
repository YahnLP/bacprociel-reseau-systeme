# S12 – DHCP, box / routeur et passerelle

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S12 – lundi 22 mars 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S11 (adresse, masque /24, plage, `ping`, erreurs d'adressage) |
| **Référentiel** | C09 · C10 · savoir : éléments actifs (niveau 3) · IPv4 (niveau 3) |

> [!NOTE]
> **Question qui guide la séance :** *« En S11 on a donné les adresses à la main. Dans une entreprise de 50 postes, qui fait ça ? Et comment un PC sort-il de son réseau pour aller sur Internet ? »* Réponses : le **DHCP** distribue les adresses, et la **passerelle** (la box) est la porte de sortie.

## 🎯 Objectifs

1. **Expliquer** pourquoi on automatise l'adressage et **raconter la conversation DHCP** en 4 phrases (demande, offre, acceptation, confirmation).
2. **Lire** `ipconfig /all` (adresse, masque, passerelle, serveur DHCP, bail, DNS) et utiliser `ipconfig /release` et `/renew`.
3. **Reconnaître** une adresse **169.254.x.x** et en déduire « le DHCP ne répond pas ».
4. **Expliquer** le rôle de la **passerelle par défaut** : même réseau = direct, autre réseau = par la passerelle.
5. **Régler** une box ou un routeur de TP : adresse LAN, **plage DHCP**, mot de passe administrateur, réservation d'adresse (sur du matériel réel).
6. **Diagnostiquer** un poste configuré à la main qui « n'a pas Internet » (passerelle manquante).

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | DHCP, bail, `ipconfig /all`, 169.254, passerelle, plan d'adressage d'une box |
| [🛠️ TP](02-tp.md) | Observer le DHCP, casser et réparer, régler la box, noter les réglages |
| [`tp/s12-dhcp-box.json`](tp/s12-dhcp-box.json) | Simulateur : 4 postes, une box, Internet (FAI) ; un poste ne sort pas |
| [📋 Fiche de configuration de la box](03-fiche-box.md) | À remplir pendant le TP sur matériel réel (grille d'évaluation) |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « 30 PC à configurer à la main, combien de temps ? » ; retour mission entreprise (qui distribue les adresses chez vous ?) | Oral |
| 0 h 20 – 1 h 00 | **Mini-cours 1** : le DHCP en 4 phrases, le bail (cours §1–§2) + **jeu de rôle** (un élève = box, les autres = PC) | Classe |
| 1 h 00 – 1 h 50 | **TP A–B** : observer le DHCP dans le simulateur, `ipconfig /all`, `release` / `renew` | Binôme |
| 1 h 50 – 2 h 05 | Pause | |
| 2 h 05 – 2 h 30 | **Mini-cours 2** : la passerelle, le plan d'adressage d'une box (§3–§4) | Classe |
| 2 h 30 – 3 h 10 | **TP C–D** : le poste « sans Internet », la plage DHCP, la box éteinte (169.254) | Binôme |
| 3 h 10 – 3 h 50 | **TP E** : régler une box / un routeur de TP réel, fiche de configuration | Binôme |
| 3 h 50 – 4 h 00 | Bilan oral, passeport | |

## 🧪 Matériel et préparation

- Simulateur ouvert avec `tp/s12-dhcp-box.json`.
- **Une box ou un routeur de TP par binôme** (ou par groupe de 3) pour la partie E, remis à zéro (réglages d'usine), avec un PC relié en Ethernet. **Sans matériel réel**, la partie E se fait dans le simulateur (adresse, plage, DHCP) et l'enseignant démontre le mot de passe administrateur et la réservation d'adresse.
- Prévoir le **mot de passe d'usine** et l'adresse de la box (étiquette dessous).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **TP de configuration d'un routeur / d'une box de petite structure** | Grille de la [fiche de configuration](03-fiche-box.md) (formatif noté) |
| Oral | « Que fait le DHCP ? À quoi sert la passerelle ? Que veut dire 169.254 ? » |

## 🏭 Mission en entreprise

> *Demander au tuteur quel équipement distribue les adresses (box, serveur) et comment on y accède. Noter la passerelle d'un poste (`ipconfig`).*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Jeu de rôle (10 min)** très efficace : l'élève « box » a un paquet de 10 papiers « 192.168.1.x » ; chaque « PC » vient demander (phrase 1), reçoit une adresse (2), l'accepte (3), la box la raye de sa liste (4). On rejoue avec **la box absente** : personne n'a d'adresse.
- La conversation DHCP est présentée **volontairement simplifiée** (4 phrases, sans les noms DORA ni les ports). Les noms *Discover / Offer / Request / Ack* sont vus en Première (analyse de trames).
- Les adresses distribuées dépendent de l'ordre des demandes (`.10`, `.11`…). Ne pas annoncer d'adresse précise aux élèves.
- **Simulateur** : la box permet de régler adresse LAN, masque, plage DHCP et d'activer/désactiver le DHCP. Elle **n'a pas** de mot de passe administrateur ni de réservation d'adresse : ces points se font sur le matériel réel (fiche de configuration).
- Piège classique : une plage DHCP qui recouvre une **adresse fixe** (doublon, retour de la S11).
- Corrigé : `corriges/seconde/S12-corrige.md` et `S12-dhcp-box-corrige.json` (non publiés sur le site).

</details>
