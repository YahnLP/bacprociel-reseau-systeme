# S08 – Intégrer de nouveaux équipements

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S08 – 4 janvier 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🔴 Autonome |
| **Prérequis** | Seconde S11 (adresses fixes et DHCP), Première S08–S09 (VLAN), Terminale S05. Le TP fournit les commandes du service DHCP du switch de niveau 3 |
| **Référentiel** | C09 · C06 · IoT (niv. 2) · architectures industrielles (niv. 2) |

> [!NOTE]
> **Question qui guide la séance :** *« Le patron branche une caméra connectée sur le réseau « parce que c'est du Wi-Fi/RJ45, ça doit marcher ». Qu'est-ce qui peut mal tourner, et comment l'intégrer proprement ? »*

## 🎯 Objectifs

1. **Intégrer** un équipement réseau (imprimante, NAS) avec une **adresse réservée** hors plage DHCP.
2. **Placer** les objets connectés dans un **VLAN dédié**.
3. **Expliquer** le PoE et **choisir** entre alimentation par câble réseau ou par bloc secteur.
4. **Tester** l'équipement (test fonctionnel) et **mettre à jour la documentation**.
5. **Repérer** les équipements d'un réseau industriel (aperçu).

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Intégration en 6 étapes ; réservation d'adresse ; VLAN objets ; PoE ; aperçu industriel |
| [🛠️ TP](02-tp.md) | Cabinet Lemoine : imprimante + NAS dans un VLAN dédié, puis fiche d'intégration (caméra IP et ESP32 sur papier) |
| [📝 Aide-mémoire](03-aide-memoire.md) | Procédure d'intégration, plan d'adressage type, PoE en un coup d'œil |
| [`tp/t08-integration.json`](tp/t08-integration.json) | Simulateur : équipements posés, aucun câble, switch cœur vierge |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « Qui a déjà branché une caméra ou une enceinte connectée chez lui ? Qu'est-ce qui s'est passé ? » | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : intégrer en 6 étapes, réservation, VLAN objets | Classe |
| 0 h 50 – 2 h 00 | **TP A–C** : câbler, VLAN 40, adresses fixes | Binôme |
| 2 h 00 – 2 h 15 | Pause |  |
| 2 h 15 – 2 h 45 | **Mini-cours** : PoE, ESP32, réseaux industriels (aperçu) | Classe |
| 2 h 45 – 3 h 30 | **TP D–E** : tests, fiche d'intégration d'une caméra IP et d'un ESP32 | Individuel |
| 3 h 30 – 4 h 00 | **TP F** : mise à jour de la documentation | Individuel |

## 🧪 Matériel et préparation

- Le fichier `t08-integration.json`.
- Si disponible : un petit switch PoE, une caméra IP ou un ESP32 du plateau, **uniquement pour observer** (non indispensable).
- [Aide-mémoire](03-aide-memoire.md) imprimé.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 5 contrôles automatiques** (adresses, VLAN, tests, sauvegarde) | Formatif |
| **Fiche d'intégration** (caméra IP) + **plan d'adressage mis à jour** | Grille : adresse réservée, VLAN justifié, test fonctionnel, documentation à jour |

## 🏭 Mission en entreprise

> *Participer à l'intégration d'un équipement (imprimante, caméra, objet connecté) et la décrire.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Limite du simulateur :** il n'a ni **caméra IP**, ni **PoE**, ni **ESP32**. L'**imprimante** et le **NAS** servent de cas réel ; la caméra et l'ESP32 sont travaillés **sur fiche** (partie E) et, si possible, sur du matériel réel du plateau.
- **Réservation d'adresse :** le TP utilise des adresses **fixes hors plage DHCP** (méthode la plus simple). La **réservation DHCP par adresse MAC** est présentée au cours mais non refaite.
- **Aperçu des réseaux industriels :** simple repérage (automate, capteur, passerelle, protocoles Modbus/Profinet) ; **aucune configuration** n'est demandée.
- **Sécurité IoT :** insister sur le **mot de passe par défaut** à changer et sur l'**isolement** dans un VLAN.
- Le switch cœur est un 3560 (niveau 3) ; il a pour DHCP le pool `POSTES`. `ip dhcp excluded-address 192.168.10.1 192.168.10.49` réserve le bas de plage.
- Corrigé : `corriges/terminale/T08-corrige.md`, `T08-integration-corrige.json`.

</details>
