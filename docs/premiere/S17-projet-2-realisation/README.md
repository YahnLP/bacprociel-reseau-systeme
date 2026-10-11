# S17 – Projet A2 (2/3) : réalisation et configuration

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S17 – lundi 10 mai 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S16 terminée (dossier d'étude revu) ; S05 à S14 |
| **Référentiel** | C09 · C10 |

> [!NOTE]
> **Question qui guide la séance :** *« Comment mettre en service un réseau complet **sans tout casser à la fois** ? »* Réponse : **une couche après l'autre**, avec un test et une sauvegarde à chaque étape.

## 🎯 Objectifs

1. **Câbler** selon le tableau de câblage et **contrôler** les liaisons.
2. **Configurer** le switch (VLAN, ports) et le routeur (3 interfaces, relais DHCP).
3. **Configurer** le serveur (DHCP à 3 pools, DNS, web) et le **Wi-Fi invité**.
4. **Filtrer** les invités avec une ACL.
5. **Sauvegarder** chaque configuration validée.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📋 Plan de référence](00-plan-de-reference.md) | Adressage, ports, câblage **(après la revue de S16)** |
| [📖 Cours élève](01-cours.md) | La mise en service par couches ; le relais DHCP |
| [🛠️ TP : la mise en service](02-tp.md) | 8 étapes avec points de contrôle |
| [📝 Aide-mémoire des commandes](03-aide-memoire.md) | Commandes du projet |
| [`tp/p16-projet-depart.json`](../S16-projet-1-etude/tp/p16-projet-depart.json) | Simulateur (le même qu'en S16) |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : retour sur la revue de S16, plan de référence, plan de la séance | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : mise en service par couches ; relais DHCP | Classe |
| 0 h 50 – 1 h 50 | **TP A–C** : câblage, switch, routeur | Équipe |
| 1 h 50 – 2 h 05 | Pause | |
| 2 h 05 – 3 h 20 | **TP D–F** : serveur, Wi-Fi, ACL | Équipe |
| 3 h 20 – 4 h 00 | **TP G–H** : sécurité, sauvegarde, **jalon noté** (mise en service) | Équipe |

## 🧪 Matériel et préparation

- Simulateur : `p16-projet-depart.json` (rouvert **au départ**, non corrigé).
- Le **plan de référence** imprimé.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Jalon noté : mise en service** | **9 contrôles automatiques** du simulateur + fichier enregistré |
| **Sauvegardes** | Une copie texte de chaque configuration dans le dossier |

## 🏭 Mission en entreprise

> *Compléter la documentation de la maquette ; **préparer la recette** : pour chaque exigence, quel test ?*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Plan de référence** : distribuer **après** la revue de S16 ; les 9 contrôles du simulateur s'appuient sur lui.
- Pièges attendus : (1) oubli du **`ip helper-address`** → pas d'adresses pour Direction et Invités ; (2) **ACL** qui bloque aussi le **DHCP** des invités (`permit udp any eq 68 any eq 67`) ; (3) serveur **sans passerelle** ; (4) **ports du routeur** dans le mauvais VLAN ; (5) oubli de `write memory`.
- Le Wi-Fi est réglé **sur la borne** (SSID, WPA2, clé) **et** sur le portable (même clé). Le **Wi-Fi invité n'est pas isolé** du reste par la borne dans le simulateur : l'**isolation** vient du **VLAN + ACL**.
- Corrigé : `corriges/premiere/P17-corrige.md` et `P16-projet-corrige.json`.

</details>
