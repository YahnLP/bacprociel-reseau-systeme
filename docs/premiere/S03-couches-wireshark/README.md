# S03 – Les couches : comprendre ce qui circule

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S03 – lundi 28 septembre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S02 (simulateur, adresse + masque, `ping`) |
| **Référentiel** | C06 · modèles OSI/IP en couches (niv. 1) · IPv4 (niv. 3) |

> [!NOTE]
> **Question qui guide la séance :** *« Quand je tape `ping`, qu'est-ce qui part vraiment sur le câble ? Et pourquoi dit-on qu'un réseau fonctionne « par couches » ? »*

## 🎯 Objectifs

1. **Expliquer** l'**encapsulation** : données → segment → paquet → trame.
2. **Associer** chaque protocole et chaque équipement à sa **couche** (Ethernet, IP, ICMP ; switch, routeur).
3. **Distinguer** adresse **MAC** (locale) et adresse **IP** (de bout en bout).
4. **Lire** une trame dans l'analyseur : champs Ethernet, IP, ICMP, **TTL**.
5. **Expliquer** **ARP** et ce qui change (ou non) quand un paquet traverse un **routeur**.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Couches, encapsulation, MAC, ARP, IP, TTL |
| [🛠️ TP](02-tp.md) | Capturer et lire des trames : même réseau, puis à travers un routeur |
| [📝 Fiche de lecture d'une trame](03-fiche-lecture-trame.md) | Aide-mémoire + QCM final |
| [`tp/p03-couches.json`](tp/p03-couches.json) | Simulateur : deux réseaux reliés par un routeur |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : la lettre dans l'enveloppe dans le colis ; retour mission entreprise | Classe |
| 0 h 20 – 1 h 00 | **Mini-cours 1** : couches et encapsulation (cours §1–§2) | Classe |
| 1 h 00 – 1 h 40 | **TP A–B** : lire une trame, observer ARP | Binôme |
| 1 h 40 – 1 h 55 | Pause | |
| 1 h 55 – 2 h 20 | **Mini-cours 2** : MAC / IP / TTL à travers un routeur (§3–§4) | Classe |
| 2 h 20 – 3 h 20 | **TP C–D** : comparer deux segments, mener l'enquête | Binôme |
| 3 h 20 – 4 h 00 | **Bilan** : fiche de lecture, QCM, passeport | Individuel |

## 🧪 Matériel et préparation

- Simulateur avec `tp/p03-couches.json` (aucun autre logiciel).
- Si possible : **Wireshark** installé sur un poste réel pour une démonstration finale (même lecture qu'avec l'analyseur du simulateur).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **TP : tableaux de lecture** | Comparer avec le corrigé (formatif) |
| **QCM final** | 8 questions (fiche) |

## 🏭 Mission en entreprise

> *Repérer sur le réseau de l'entreprise **un équipement de couche 2** (switch) et **un de couche 3** (routeur / pare-feu) ; noter leur modèle.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Analyseur** : il imite Wireshark (filtres, détail par couche, octets). Les liaisons se choisissent dans la liste « Capture sur ».
- **Valeurs attendues** (fichier fourni) : MAC `PC1` = `00:14:22:00:00:0b`, `R1` Gi0/0 = `00:00:0c:00:00:0f`, `R1` Gi0/1 = `00:00:0c:00:00:10`, `SRV2` = `00:14:22:00:00:12` ; TTL 128 sur le segment 1, 127 sur le segment 2.
- **Notion difficile** : « la MAC change, l'IP reste ». Ne pas passer trop vite sur la partie C.
- **Bruit** : trames ICMPv6 et *ARP Announcement* normales ; filtrer avec `icmp` / `arp`.
- Corrigé : `corriges/premiere/P03-corrige.md`.

</details>
