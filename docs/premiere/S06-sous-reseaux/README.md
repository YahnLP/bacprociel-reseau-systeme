# S06 – Découper un réseau en sous-réseaux

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S06 – lundi 2 novembre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | Seconde S09–S10 (adresse IP, masque), Première S03 (couches) |
| **Référentiel** | C06 · C09 · IPv4 (niv. 3) |

> [!NOTE]
> **Question qui guide la séance :** *« Une PME a un seul réseau 192.168.1.0/24 pour 60 postes : Direction, Atelier, Invités. Comment les séparer sans changer de plage d'adresses ? »*

## 🎯 Objectifs

1. **Rappeler** ce que fait le masque (partie réseau / partie machine).
2. **Découper** un /24 en 2 ou 4 sous-réseaux (/25, /26) : combien de sous-réseaux, de machines ?
3. **Calculer** pour chaque sous-réseau : adresse de réseau, de diffusion, plage utilisable.
4. **Diagnostiquer** une panne due à un mauvais masque ou à une adresse dans le mauvais sous-réseau.
5. **Construire** un plan d'adressage pour une PME.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Masque, emprunt de bits, tableau des puissances de 2, méthode de calcul |
| [🛠️ TP](02-tp.md) | Trouver deux erreurs d'adressage dans le simulateur, lire une capture |
| [📝 Exercices et plan d'adressage](03-exercices.md) | Entraînement progressif + plan d'adressage d'une PME |
| [`tp/p06-sousreseaux.json`](tp/p06-sousreseaux.json) | Simulateur : 1 switch, 4 PC, 2 erreurs cachées |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : le TP-panne « PC4 joint PC1 dans un sens seulement » (voir TP, partie A) ; retour mission entreprise | Classe |
| 0 h 20 – 1 h 00 | **Mini-cours 1** : masque et emprunt de bits (cours §1–§2) | Classe |
| 1 h 00 – 1 h 45 | **TP A–B** : constater la panne, corriger | Binôme |
| 1 h 45 – 2 h 00 | Pause | |
| 2 h 00 – 2 h 30 | **Mini-cours 2** : méthode de calcul et plan d'adressage (§3–§4) | Classe |
| 2 h 30 – 3 h 30 | **Exercices** progressifs (niveaux 1 à 3) | Individuel puis correction |
| 3 h 30 – 4 h 00 | **Plan d'adressage de la PME** (noté, formatif) | Individuel |

## 🧪 Matériel et préparation

- Simulateur avec `tp/p06-sousreseaux.json`.
- Feuille de brouillon : le **tableau des puissances de 2** (cours §3) à imprimer.
- Pas de calculatrice « réseau » avant l'exercice 4 : la méthode à la main d'abord.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **TP : 3 contrôles automatiques** | PC1↔PC2, PC3↔PC4, PC1 ne joint pas PC3 (séparation voulue) |
| **Exercices + plan d'adressage** | Correction par barème (formatif noté) |

## 🏭 Mission en entreprise

> *Demander au tuteur **le plan d'adressage** du site (ou le relever sur les postes : `ipconfig`) : quelle plage, quel masque, combien de sous-réseaux ? Ne rien modifier.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Panne asymétrique** : au départ, `PC4 → PC1` répond « Délai d'attente dépassé » (PC4, en /24, croit PC1 local, mais PC1 n'a pas de route pour répondre hors de son /26) alors que `PC1 → PC4` échoue immédiatement (« échec général »). Les élèves sont surpris : l'analyse de capture (partie B) montre les ARP et ICMP qui partent sans réponse.
- **Routeur** : volontairement absent. S07 introduit le routeur pour **faire communiquer** deux sous-réseaux.
- **Difficulté usuelle** : confondre « 64 adresses » et « 64 machines » (réseau + diffusion = −2). Revenir au schéma `decoupage-26.svg`.
- Corrigés : `corriges/premiere/P06-corrige.md` et `P06-sousreseaux-corrige.json`.

</details>
