# S13 – Cuivre certifié, fibre optique et sécurité

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S13 – lundi 15 février 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | Seconde S09 (câble RJ45), Première S08–S09 (liens entre switchs) |
| **Référentiel** | C09 · C06 · raccordement filaire / optique (niv. 3) · appareils de mesure (niv. 3) · sécurité électrique |

> [!NOTE]
> **Question qui guide la séance :** *« Le câble est posé, le voyant est allumé : le client peut-il signer la réception ? Comment PROUVER qu'un lien est bon, et quand faut-il passer à la fibre ? »*

## 🎯 Objectifs

1. **Choisir** le bon type de câble (droit/croisé, cuivre/fibre) et **diagnostiquer** un câble inadapté.
2. **Tester** un lien cuivre (cartographie, longueur) et **lire** un rapport de test.
3. **Distinguer** fibre monomode et multimode ; **identifier** les connecteurs (LC, SC).
4. **Calculer** un bilan de liaison optique simple (dB).
5. **Appliquer** les règles de **sécurité** : laser, électricité de baie, PoE.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Cuivre certifié, rapport de test, fibre, bilan optique, sécurité |
| [🛠️ TP](02-tp.md) | Câbles du mauvais type (simulateur), lecture de rapports, tests sur matériel, bilan optique |
| [📝 Exercices et fiche de résultats](03-exercices-fiche-resultats.md) | Calculs, QCM, fiche de mesures à remplir |
| [`tp/p13-cables.json`](tp/p13-cables.json) | Simulateur : 3 câbles du mauvais type (mode « câbles stricts ») |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « le voyant est vert, donc c'est bon ? » (photo d'un rapport de test) ; retour mission | Classe |
| 0 h 20 – 0 h 55 | **Mini-cours 1** : cuivre certifié, rapport de test (§1–§2) | Classe |
| 0 h 55 – 1 h 50 | **TP A–B** : câbles du mauvais type (simulateur), lecture de rapports | Binôme |
| 1 h 50 – 2 h 05 | Pause | |
| 2 h 05 – 2 h 40 | **Mini-cours 2** : fibre, bilan optique, sécurité (§3–§5) | Classe |
| 2 h 40 – 3 h 30 | **TP C–D** : tests réels (testeur, fibre, VFL) ou démonstration + bilan optique | Binôme |
| 3 h 30 – 4 h 00 | **Fiche de résultats** + QCM sécurité | Individuel |

## 🧪 Matériel et préparation

- Simulateur : `tp/p13-cables.json` (activer « Câbles stricts » si besoin : déjà enregistré dans le fichier).
- **Matériel réel** (si disponible) : testeur de câble (cartographie + longueur), 3 câbles RJ45 (1 bon, 1 avec défaut volontaire, 1 long), jarretières fibre LC-LC et SC-LC (mono et multimode), source lumineuse visible (VFL), kit de nettoyage, **lunettes**, bobine.
- **Sans matériel de mesure** : les rapports du TP (fournis) suffisent pour atteindre les objectifs ; les mesures réelles sont un plus.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 4 contrôles automatiques** | PC1↔PC2, PC3↔PC4, PC1↔PC3, PC2↔PC4 |
| **Fiche de résultats** | Grille : lecture de rapport, bilan optique, sécurité (formatif noté) |

## 🏭 Mission en entreprise

> *Repérer, dans l'entreprise, **des liaisons en fibre** (jarretières jaunes ou aqua, connecteurs LC/SC) ou **des rapports de test** d'une installation : prendre des photos **si c'est autorisé**. Ne rien débrancher.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Simulateur** : le mode « câbles stricts » exige câble **droit** entre un poste et un switch, **croisé** entre deux switchs, et **fibre** uniquement entre ports optiques (les équipements simulés n'ont **pas de ports optiques** : une fibre sur un port cuivre ne monte pas). Les équipements réels sont **auto-MDI-X** : le croisé n'est plus nécessaire en pratique, mais l'exercice reste utile pour comprendre.
- **Valeurs numériques** (pertes en dB, distances, budgets) : des **valeurs usuelles d'exercice** ; vérifier avec la documentation des composants et des normes utilisés dans votre centre (NF EN 50173 / ISO 11801).
- **Habilitation électrique** : la séance sensibilise (risques de la baie, PoE) et **n'habilite pas**. La préparation à l'habilitation (B1V, selon le référentiel et l'organisme) est **à mutualiser avec la formation U2** : à adapter par l'équipe.
- **Sécurité laser** : ne jamais regarder dans une fibre ou un port actif, même « éteint » ; la VFL (laser rouge visible, classe 2) ne se pointe jamais vers un œil.
- Corrigés : `corriges/premiere/P13-corrige.md` et `P13-cables-corrige.json`.

</details>
