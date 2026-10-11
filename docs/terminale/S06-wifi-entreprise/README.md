# S06 – Wi-Fi d'entreprise

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S06 – 16 novembre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | Seconde S13 à S15 (Wi-Fi), Première S08–S09 (VLAN, trunk), Terminale S05 (inter-VLAN) |
| **Référentiel** | C09 · C10 · C06 |

> [!NOTE]
> **Question qui guide la séance :** *« Dans une entreprise, le personnel et les invités utilisent le même Wi-Fi… sans jamais se voir. Comment est-ce possible, et comment s'assurer que c'est sûr ? »*

## 🎯 Objectifs

1. **Expliquer** ce qu'est un SSID et le **relier à un VLAN**.
2. **Choisir** une sécurité Wi-Fi adaptée (WPA2, WPA3, réseau ouvert) et **justifier**.
3. **Mettre en service** un Wi-Fi personnel et un Wi-Fi invités **séparés** et **filtrés**.
4. **Lire** un schéma d'authentification d'entreprise (RADIUS).
5. **Dépanner** un Wi-Fi : clé, VLAN, filtrage, signal et canaux.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | SSID et VLAN ; sécurité WPA2/WPA3 ; RADIUS (lecture) ; canaux et signal |
| [🛠️ TP](02-tp.md) | Cabinet Garcia : Wi-Fi du personnel et Wi-Fi invités, puis dépannage |
| [📝 Aide-mémoire](03-aide-memoire.md) | Réglages d'une borne, commandes de vérification, check-list de dépannage Wi-Fi |
| [`tp/t06-wifi.json`](tp/t06-wifi.json) | Simulateur : matériel posé, bornes non branchées, switch et routeur vierges |
| [`tp/t06-panne.json`](tp/t06-panne.json) | Simulateur : Wi-Fi installé mais avec 3 défauts |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « Ton téléphone voit 6 réseaux Wi-Fi dans la salle. Lesquels sont à nous ? » | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : SSID, VLAN, sécurité | Classe |
| 0 h 50 – 1 h 50 | **TP A–C** : câbler les bornes, VLAN, sous-interfaces, DHCP | Binôme |
| 1 h 50 – 2 h 05 | Pause |  |
| 2 h 05 – 2 h 30 | **Mini-cours** : RADIUS (lecture), canaux, signal | Classe |
| 2 h 30 – 3 h 15 | **TP D–E** : SSID, clés, filtrage des invités | Binôme |
| 3 h 15 – 4 h 00 | **TP F–G** : dépannage, fiche de mise en service | Individuel |

## 🧪 Matériel et préparation

- Les deux fichiers `.json` ci-dessus (à ouvrir **au départ**).
- [Aide-mémoire](03-aide-memoire.md) imprimé.
- Si possible : un téléphone avec une application d'analyse Wi-Fi pour la discussion sur les canaux (non indispensable).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 6 contrôles automatiques** (adresses, accès au serveur, filtrage invités) | Formatif |
| **Fiche de mise en service Wi-Fi** (SSID, VLAN, sécurité, justification) | Grille : exactitude, justification de la sécurité, test réalisé |

## 🏭 Mission en entreprise

> *Observer la configuration Wi-Fi de l'entreprise : SSID, VLAN invités, sécurité.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Limite du simulateur :** une borne = **un SSID**. Pour représenter « deux SSID sur un même boîtier », on place **deux bornes**, chacune branchée sur un port d'**un VLAN différent**. Dans la réalité, **une seule borne** diffuse plusieurs SSID et les associe à des VLAN par un **trunk**. À dire clairement aux élèves.
- **RADIUS et WPA3** : présentés **en lecture** (schéma), non configurés, comme le prévoit le référentiel (authentification d'entreprise : niveau d'information).
- **Canaux et puissance** : le simulateur ne modélise pas les interférences ; la partie canaux est faite **à l'oral et sur schéma**.
- **Pannes (t06-panne)** : 1) le portable du personnel a une clé erronée (`…26` au lieu de `…27`) ; 2) la borne invités est branchée sur `Fa0/11` en **VLAN 20** (au lieu de 30) ; 3) l'ACL des invités n'est plus posée sur la sous-interface `Gi0/0.30`.
- Aucun mot de passe `enable` dans ces fichiers : la séance porte sur le Wi-Fi, pas sur la sécurisation du switch (vue en Première S14).
- Corrigé : `corriges/terminale/T06-corrige.md`.

</details>
