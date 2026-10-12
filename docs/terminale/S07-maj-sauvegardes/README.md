# S07 – Mises à jour et sauvegardes

| Élément | Détail |
|---|---|
| **Niveau** | Terminale Bac Pro CIEL |
| **Semaine** | S07 – 30 novembre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🔴 Autonome |
| **Prérequis** | Première S05 (switch administrable), S14 (sécurité de base), Terminale S05 |
| **Référentiel** | C10 · mises à jour · optimisations · lignes de commande (niv. 3) |

> [!NOTE]
> **Question qui guide la séance :** *« Le switch tombe en panne un lundi matin. As-tu de quoi remettre l'entreprise en route avant 10 h ? Et une mise à jour, est-ce toujours une bonne idée ? »*

## 🎯 Objectifs

1. **Distinguer** `running-config` et `startup-config`, et **sauvegarder** une configuration.
2. **Restaurer** une configuration sur un équipement neuf.
3. **Appliquer** la démarche de mise à jour (5 étapes) avec **retour arrière**.
4. **Tenir un journal des modifications** lisible par un collègue.
5. **Appliquer** la règle de sauvegarde « 3-2-1 » à une petite entreprise.
6. **Optimiser** un réseau qui fonctionne (ports, descriptions, VLAN) avec une preuve avant / après.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | running/startup ; sauvegarde et restauration ; mise à jour en 5 étapes ; journal |
| [🛠️ TP](02-tp.md) | Atelier Bonnet : constater la perte de configuration, sauvegarder, restaurer sur un switch neuf |
| [📝 Aide-mémoire](03-aide-memoire.md) | Commandes de sauvegarde, démarche de mise à jour, modèle de journal |
| [`tp/t07-optimisation.json`](tp/t07-optimisation.json) | Simulateur (partie G) : switch qui marche mais mal optimisé (ports libres actifs, aucune description, VLAN inutilisé) |
| [`tp/t07-sauvegarde.json`](tp/t07-sauvegarde.json) | Simulateur : switch configuré mais jamais sauvegardé |
| [`tp/t07-restauration.json`](tp/t07-restauration.json) | Simulateur : switch neuf, vierge, à remettre dans l'état du switch d'avant |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : le switch est mort, qu'est-ce qui manque ? | Classe |
| 0 h 20 – 0 h 45 | **Mini-cours** : running / startup, sauvegarde | Classe |
| 0 h 45 – 1 h 45 | **TP A–C** : constater, sauvegarder, redémarrer | Binôme |
| 1 h 45 – 2 h 00 | Pause |  |
| 2 h 00 – 2 h 30 | **Mini-cours** : mise à jour en 5 étapes, journal, optimiser (cours §3–§5) | Classe |
| 2 h 30 – 3 h 15 | **TP D–E** : restaurer sur un équipement neuf, règle 3-2-1 | Binôme |
| 3 h 15 – 4 h 00 | **TP F–G** : journal et plan de mise à jour, optimisation du réseau | Individuel |

## 🧪 Matériel et préparation

- Les deux `.json` du simulateur.
- Un éditeur de texte (Bloc-notes) pour garder la sauvegarde.
- [Aide-mémoire](03-aide-memoire.md) imprimé.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 12 contrôles automatiques** (config sauvegardée, restaurée, réseau optimisé) | Formatif |
| **Journal de modifications + plan de mise à jour d'un équipement** | Grille : version notée, sauvegarde faite, retour arrière prévu |

## 🏭 Mission en entreprise

> *Demander comment sont faites les mises à jour et les sauvegardes des équipements ; noter la procédure.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Limite du simulateur :** pas de **TFTP/SCP** ni de **mise à jour du micrologiciel** (la commande `show flash:` affiche un fichier fixe). La **sauvegarde** se fait par **copie du texte** de `show running-config` dans un fichier ; la **restauration** par **collage** dans le terminal. La procédure TFTP (`copy running-config tftp:`) est présentée **sur fiche** et à tester sur le matériel réel du plateau si disponible.
- **Partie G (optimisation)** : séance dense ; si le temps manque, faire la partie G en début de S08 ou la réduire à l'audit écrit (questions 1 et 2). Le simulateur ne gère ni débit ni canaux Wi-Fi.
- **Mise à jour du micrologiciel** : jamais faite sur le simulateur ; la démarche en 5 étapes est travaillée sur **un cas écrit** (partie F).
- Le piège classique : **modifier sans `write memory`** puis redémarrer. Il est **fait vivre** en partie A.
- La sauvegarde fournie dans le TP contient volontairement `enable secret` en clair pour l'exercice. Rappeler qu'**une sauvegarde de configuration est un fichier sensible** : on ne l'envoie pas par e-mail non protégé.
- Au passage de `copy`/`paste` dans le terminal du simulateur : coller **ligne par ligne** si besoin.
- Corrigé : `corriges/terminale/T07-corrige.md`, `T07-sauvegarde-corrige.json`, `T07-restauration-corrige.json`.

</details>
