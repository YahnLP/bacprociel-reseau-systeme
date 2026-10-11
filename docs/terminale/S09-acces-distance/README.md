# S09 – Accès à distance sécurisé

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S09 – 18 janvier 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🔴 Autonome |
| **Prérequis** | Première S10 (SSH), S14 (sécurité de base), Terminale S05, S07 |
| **Référentiel** | C10 · connexion à distance (niv. 3) · sécurité (niv. 2) |

> [!NOTE]
> **Question qui guide la séance :** *« Un technicien doit dépanner l'entreprise du soir depuis chez lui. Comment entre-t-il, sans que n'importe qui puisse faire pareil ? »*

## 🎯 Objectifs

1. **Administrer** un routeur par **SSH** et **désactiver** telnet.
2. **Publier** un service interne par une **redirection de port** (NAT/PAT) et **mesurer les risques**.
3. **Expliquer** ce qu'est un **VPN** et l'**utiliser** quand il est déjà configuré.
4. **Appliquer** les règles de télémaintenance (autorisation, compte nominatif, journal).

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | SSH vs telnet ; redirection de port ; VPN ; règles de télémaintenance |
| [🛠️ TP](02-tp.md) | Garage Dupuy : routeur en SSH, site interne publié, test depuis l'extérieur |
| [📝 Aide-mémoire](03-aide-memoire.md) | Commandes SSH et NAT, tableau de risques, fiche de télémaintenance |
| [`tp/t09-acces.json`](tp/t09-acces.json) | Simulateur : routeur en telnet, site interne non publié, poste « technicien à distance » côté Internet |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « Une caméra de surveillance est piratée parce qu'elle était visible depuis Internet. Comment ? » | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : SSH, telnet, redirection de port | Classe |
| 0 h 50 – 2 h 00 | **TP A–C** : passer en SSH, tester | Binôme |
| 2 h 00 – 2 h 15 | Pause |  |
| 2 h 15 – 2 h 45 | **Mini-cours** : VPN, télémaintenance | Classe |
| 2 h 45 – 3 h 30 | **TP D–E** : publier le site, tester de l'extérieur | Binôme |
| 3 h 30 – 4 h 00 | **TP F** : fiche de télémaintenance | Individuel |

## 🧪 Matériel et préparation

- Le fichier `t09-acces.json`.
- Optionnel : accès à un VPN déjà configuré sur le plateau (observation), sinon la partie VPN est travaillée **sur fiche**.
- [Aide-mémoire](03-aide-memoire.md) imprimé.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 6 contrôles automatiques** (SSH, NAT, redirection, sauvegarde) | Formatif |
| **Fiche de télémaintenance** remplie | Grille : autorisation, compte, périmètre, durée, trace |

## 🏭 Mission en entreprise

> *Observer comment l'entreprise gère l'accès à distance (VPN, télémaintenance) et ses règles.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Le TP** est conçu sur un routeur (NAT en surcharge + redirection `ip nat inside source static tcp … 8080`). Le poste « Technicien à distance » est branché côté Internet pour tester **de l'extérieur**.
- **Limite du simulateur :** `transport input ssh` est **mémorisé** (visible dans `show running-config`) mais **non appliqué** : telnet reste possible. À dire aux élèves ; sur du matériel réel du plateau, le tester.
- **Authentification SSH par clé** : présentée **à l'oral** ; le simulateur ne gère pas les clés. Elle peut être travaillée sur le **serveur Ubuntu** du plateau (voir Première S10).
- **VPN** : le référentiel demande d'**utiliser un VPN déjà configuré**, pas de le monter. Le simulateur propose des VPN (menu dédié) mais ce n'est pas testé dans ce TP : voir la fiche écrite en partie F.
- **Bureau à distance (RDP)** : mentionné ; ne jamais l'exposer directement sur Internet (cible n°1 des attaques).
- **Panne de 2e tour** : si les élèves publient `80` au lieu de `8080`, le test « port 80 non joignable » échoue : bonne occasion de discuter du risque d'exposer un port standard.
- Corrigé : `corriges/terminale/T09-corrige.md`, `T09-acces-corrige.json`.

</details>
