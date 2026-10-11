# S11 – Dépanner (1) : raisonner

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S11 – 15 février 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🔴 Autonome |
| **Prérequis** | Seconde S16–S18 (dépannage de niveau 1), Première S06–S09, Terminale S05 |
| **Référentiel** | C06 · C10 · diagnostic (R5) |

> [!NOTE]
> **Question qui guide la séance :** *« « Ça ne marche pas. » Par où commencer quand il y a trois pannes à la fois, qu'on est chez un client et qu'on a une heure ? »*

## 🎯 Objectifs

1. **Appliquer** la démarche : symptôme → hypothèses → tests → cause → action.
2. **Utiliser** l'**échelle des tests** pour localiser une panne.
3. **Lire** les sorties de `ipconfig`, `ping`, `show vlan brief`, `show ip interface brief`, `show ip dhcp`.
4. **Dépanner** des **pannes combinées** (physique + IP + VLAN + DNS).
5. **Chronométrer** et **réduire** son temps de diagnostic.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Démarche de dépannage ; échelle des tests ; lire les commandes |
| [🛠️ TP](02-tp.md) | PME Delmas : trois ateliers de pannes combinées, avec chronomètre |
| [📝 Aide-mémoire](03-aide-memoire.md) | Échelle des tests, tableau « symptôme → hypothèses », commandes de diagnostic |
| [`tp/t11-panne-a.json`](tp/t11-panne-a.json) | Simulateur : atelier A (le poste de l'atelier n'a plus rien) |
| [`tp/t11-panne-b.json`](tp/t11-panne-b.json) | Simulateur : atelier B (le poste du bureau n'a plus d'adresse ; le nom ne marche pas) |
| [`tp/t11-panne-c.json`](tp/t11-panne-c.json) | Simulateur : atelier C (l'atelier ne joint plus le serveur ; le bureau ne résout plus le nom) |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « Une voiture ne démarre pas : par où commence un garagiste ? » | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : la démarche et l'échelle des tests | Classe |
| 0 h 50 – 1 h 40 | **Atelier A** (avec le cours ouvert) | Binôme |
| 1 h 40 – 1 h 55 | Pause |  |
| 1 h 55 – 2 h 45 | **Atelier B** (aide-mémoire seulement) | Binôme |
| 2 h 45 – 3 h 35 | **Atelier C** (individuel, chronométré) | Individuel |
| 3 h 35 – 4 h 00 | **Bilan** : « Quelle est la panne que tu as trouvée le plus vite, et pourquoi ? » | Classe |

## 🧪 Matériel et préparation

- Les trois `.json` ci-dessus : **un atelier = un fichier**.
- Un **chronomètre** (téléphone) ; la **fiche de diagnostic** du TP.
- [Aide-mémoire](03-aide-memoire.md) imprimé.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 4 contrôles automatiques** par atelier | Formatif |
| **Fiche de diagnostic** + **temps** de l'atelier C | Grille : méthode respectée, preuves, temps, réparation |

## 🏭 Mission en entreprise

> *Documenter une panne réelle : symptôme, tests, cause, correction.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Les causes sont volontairement cachées aux élèves** : ne pas les écrire au tableau. **Atelier A** : port `Fa0/3` désactivé **et** passerelle fausse (`192.168.20.254`). **Atelier B** : port `Fa0/1` dans le VLAN 30 (donc adresse `169.254`) **et** fiche DNS `intranet` pointant sur `192.168.30.11`. **Atelier C** : sous-interface `gi0/0.20` arrêtée **et** pool DHCP sans `dns-server`.
- **Deux défauts par atelier** : l'élève qui répare le premier croit avoir fini. L'insister : **« tu n'as fini que quand les quatre tests sont verts »**.
- **Chronométrage** : le temps sert à **s'améliorer** (comparer atelier A, B, C), pas à classer. Un élève qui **ne suit pas la méthode** va **plus lentement** à la fin : le montrer.
- Dans les ateliers B et C, après correction, **renouveler le bail DHCP** du poste (`ipconfig /renew`).
- **Limite du simulateur :** pas de pannes matérielles réelles (câble abîmé, carte réseau) : on les simule en **supprimant un câble** ou en **arrêtant un port**.
- Corrigé : `corriges/terminale/T11-corrige.md`, `T11-panne-a-corrige.json`, `T11-panne-b-corrige.json`, `T11-panne-c-corrige.json`.

</details>
