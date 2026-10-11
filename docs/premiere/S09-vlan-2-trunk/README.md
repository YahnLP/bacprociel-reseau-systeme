# S09 – VLAN (2) : deux switchs et lien trunk

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S09 – lundi 14 décembre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S08 (VLAN, ports *access*) |
| **Référentiel** | C06 · C09 · C10 · éléments actifs (niv. 3) · VLAN, trunk |

> [!NOTE]
> **Question qui guide la séance :** *« La Direction a des postes dans deux bâtiments. Faut-il tirer un câble par VLAN entre les deux switchs ? »*

## 🎯 Objectifs

1. **Expliquer** ce qu'est un lien **trunk** et le rôle de l'étiquette **802.1Q**.
2. **Configurer** un trunk entre deux switchs (`switchport mode trunk`).
3. **Contrôler** : `show interfaces trunk`, ping, capture de l'étiquette.
4. **Limiter** les VLAN autorisés sur le trunk (`allowed vlan`).
5. **Dépanner** un trunk à moitié configuré.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Pourquoi un trunk, étiquette 802.1Q, VLAN autorisés, VLAN natif |
| [🛠️ TP](02-tp.md) | Relier deux switchs ; capturer l'étiquette ; dépannage |
| [📝 Aide-mémoire trunk](03-aide-memoire-trunk.md) | Commandes + méthode de dépannage |
| [`tp/p09-trunk.json`](tp/p09-trunk.json) | Simulateur : 2 switchs, VLAN prêts, trunk à faire |
| [`tp/p09-trunk-panne.json`](tp/p09-trunk-panne.json) | Simulateur : trunk à moitié fait, 2 erreurs |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : `PC1` ne joint pas `PC3` (même VLAN, autre switch) ; retour mission | Classe |
| 0 h 20 – 0 h 55 | **Mini-cours 1** : trunk et étiquette (§1–§2) | Classe |
| 0 h 55 – 1 h 50 | **TP A–C** : constater, configurer le trunk, vérifier | Binôme |
| 1 h 50 – 2 h 05 | Pause | |
| 2 h 05 – 2 h 30 | **Mini-cours 2** : VLAN autorisés, VLAN natif (§3) | Classe |
| 2 h 30 – 3 h 15 | **TP D–E** : capture 802.1Q, `allowed vlan` | Binôme |
| 3 h 15 – 4 h 00 | **TP F** : dépannage (fichier panne) + bilan | Individuel |

## 🧪 Matériel et préparation

- Simulateur : `tp/p09-trunk.json` puis `tp/p09-trunk-panne.json`.
- **Option matériel réel** : deux switchs administrables et un câble droit (ou croisé) entre les ports Gi.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **TP : 4 contrôles automatiques** | PC1↔PC3, PC2↔PC4, PC1 ne joint pas PC2, trunk actif |
| **Dépannage** | Fichier panne : 3 contrôles |

## 🏭 Mission en entreprise

> *Repérer, dans la baie de brassage, **un câble qui relie deux switchs** : où va-t-il ? Combien de câbles relient la baie au reste du bâtiment ? **Ne rien débrancher.***

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- Dans le simulateur, un lien entre ports *access* du VLAN 1 **ne laisse pas passer** les VLAN 10/20 : le trunk est donc bien indispensable (comportement conforme à l'équipement réel).
- Le message `Impossible de joindre l'hôte de destination` (venant de sa **propre** adresse) = ARP sans réponse ; différent de `Impossible de joindre le réseau de destination` (venant d'un routeur, S07).
- Le simulateur ne négocie pas DTP : `switchport mode trunk` est à taper **des deux côtés**.
- VLAN natif : évoqué (cours §3) mais non manipulé ; à ne pas laisser sur le VLAN 1 en production (S14).
- Corrigés : `corriges/premiere/P09-corrige.md`, `P09-trunk-corrige.json`, `P09-trunk-panne-corrige.json`.

</details>
