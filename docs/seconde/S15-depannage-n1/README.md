# S15 – Dépanner : la méthode de niveau 1 + remédiation

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S15 – lundi 3 mai 2027 (CFA) |
| **Durée** | 4 heures (2 h dépannage + 2 h remédiation) |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S10 à S14 (câblage, IP, DHCP, DNS, Wi-Fi) |
| **Référentiel** | C06 · C10 · savoir : diagnostic d'une panne (niveau 2) |

> [!NOTE]
> **Question qui guide la séance :** *« Internet ne marche plus. Par où commencer, et comment savoir où ça casse ? »*

## 🎯 Objectifs

1. **Appliquer l'échelle du diagnostic** : câble → adresse IP → passerelle → Internet par adresse → Internet par nom.
2. **Lire** les indices : voyants, `ipconfig`, réponses de `ping`.
3. **Identifier** la cause parmi 5 pannes classiques et **la corriger**.
4. **Rédiger** une fiche d'intervention claire (symptôme, tests, cause, correction, vérification).
5. **Se positionner** sur le Passeport d'autonomie et **combler** ses lacunes (remédiation).

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | L'échelle du diagnostic, les 5 symptômes, la fiche d'intervention |
| [🛠️ TP](02-tp.md) | 5 pannes à diagnostiquer en rotation (simulateur) + panne Wi-Fi |
| [📝 Fiche d'intervention](03-fiche-intervention.md) | À imprimer : une fiche par panne |
| `tp/s15-panne-1.json` … `s15-panne-5.json` | Simulateur : un réseau, une panne par fichier |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 15 | **Accroche** : le professeur annonce « Ça ne marche pas » sur un poste préparé ; qu'est-ce qu'on fait ? (les idées des élèves au tableau) ; retour mission entreprise | Oral |
| 0 h 15 – 0 h 55 | **Mini-cours** : l'échelle du diagnostic, démonstration sur la panne 3 | Classe |
| 0 h 55 – 1 h 40 | **TP A** : pannes 1 et 2 (guidées), fiche d'intervention | Binôme |
| 1 h 40 – 1 h 55 | Pause | |
| 1 h 55 – 3 h 00 | **TP B** : pannes 3, 4, 5 en autonomie (rotation) | Binôme |
| 3 h 00 – 3 h 20 | **Contrôle** : une panne inconnue tirée au sort, seul, avec la fiche | Individuel |
| 3 h 20 – 4 h 00 | **Remédiation** : on relit son Passeport, on choisit une séance à reprendre (TP S11 à S14 ou bibliothèque d'exercices) | Individuel |

## 🧪 Matériel et préparation

- Simulateur avec les 5 fichiers `tp/s15-panne-N.json` (un par panne).
- **Option matériel réel :** provoquer les pannes à l'avance sur 3 ou 4 postes (câble débranché, IP fixe fausse, DNS modifié).
- Fiches d'intervention imprimées (une par panne et par élève).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Panne inconnue en autonomie** (parmi les 5) | Fiche d'intervention + panne résolue (formatif noté) |
| Oral | « Ton premier test ? Pourquoi dans cet ordre ? » |

## 🏭 Mission en entreprise

> *Noter **une panne** vécue en entreprise (informatique ou réseau) : symptôme, cause, solution, sur une fiche d'intervention.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Les 5 pannes** (poste `PC-CLIENT`, poste de référence `PC-REF`) :

| N° | Panne | Symptôme visible | Correction |
|---|---|---|---|
| 1 | PC non relié au switch | `ipconfig` : *Média déconnecté* | Brancher sur un port libre (port 3) |
| 2 | IP fixe d'un autre réseau (`192.168.10.30`) | `ping` de la box : *échec* | Passer en DHCP ou `192.168.1.30/24` |
| 3 | Passerelle fausse (`192.168.1.2`) | Box OK, Internet KO | Passerelle `192.168.1.1` |
| 4 | DNS faux (`192.168.1.5`) | Internet par adresse OK, par nom KO | DNS `192.168.1.1` |
| 5 | Switch non relié à la box | Les deux postes en `169.254.x.x` | Câbler `SW1` ↔ `BOX` |

- **Pas de panne « DHCP de la box arrêté »** : l'état du service DHCP de la box ne survit pas à l'enregistrement du fichier du simulateur. Le cas `169.254.x.x` est donc couvert par la panne 5 ; l'arrêt du DHCP se montre sur une vraie box.
- **Panne 6 (bonus) :** le fichier de la séance 14 (`s14-wifi.json`, portable `LAP3` avec une mauvaise clé) sert de panne Wi-Fi.
- **Remédiation** : les élèves choisissent d'après leur Passeport ; prévoir des exercices de reprise (QCM, TP S11 à S14).
- Corrigés : `corriges/seconde/S15-corrige.md` et `S15-panne-N-corrige.json`.

</details>
