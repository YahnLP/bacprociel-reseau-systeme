# 📖 Cours – Lire un dossier d'installation

*Bac Pro CIEL – Terminale – E31 – S02*

> [!IMPORTANT]
> **Une idée à la fois.** Réponds à la question **avant** de déplier la réponse.

## 🎯 À la fin de ce cours, tu sauras

- [ ] nommer les **pièces** d'un dossier d'installation ;
- [ ] vérifier la **complétude** et la **cohérence** d'un dossier ;
- [ ] **poser les bonnes questions** avant le chantier.

---

## 1. Les pièces d'un dossier

### 🤔 Avant de lire : à ton avis ?

On te remet « le dossier » d'un chantier. De quoi as-tu **besoin** pour travailler sans devoir téléphoner dix fois ?

<details markdown="1"><summary>Voir la réponse</summary>

D'un **besoin clair** (cahier des charges), de **plans** (où sont les prises, la baie), d'un **schéma d'architecture** (comment les équipements sont reliés), d'un **plan d'adressage** (adresses et VLAN), d'une **liste de matériel** et de **consignes** (accès, horaires, sécurité).

</details>

### 💡 L'idée

| Pièce | Elle répond à… | Ce que tu y vérifies |
|---|---|---|
| **Cahier des charges** | *Que veut le client ?* | Chaque exigence est **testable** |
| **Plans du local** | *Où ?* | Prises, baie, cheminement, hauteurs |
| **Schéma d'architecture** | *Comment est-ce relié ?* | Chaque équipement du cahier y figure |
| **Plan d'adressage** | *Quelles adresses ?* | Pas de **chevauchement**, adresses fixes **hors DHCP** |
| **Liste de matériel** | *De quoi a-t-on besoin ?* | Quantités **suffisantes**, compatibles |
| **Consignes** | *Dans quelles conditions ?* | Accès, horaires, sécurité, interlocuteur |

---

## 2. La lecture critique

### 🤔 Avant de lire : à ton avis ?

Le schéma montre un switch **8 ports** et le cahier des charges demande **13 prises** raccordées. Que fais-tu ?

<details markdown="1"><summary>Voir la réponse</summary>

Tu **signales l'incohérence** avant d'installer : 13 équipements ne tiennent pas sur 8 ports. Tu proposes une solution (switch 24 ports) et tu la **fais valider** par le client. Câbler « en espérant » = **arrêt de chantier**.

</details>

### 💡 L'idée : trois questions pour chaque pièce

1. **Est-elle complète ?** (tout ce qui est annoncé est-il présent ?)
2. **Est-elle cohérente avec les autres ?** (mêmes équipements, mêmes nombres, mêmes adresses)
3. **Est-elle conforme au terrain ?** (le plan correspond-il à ce qu'on voit sur place ?)

| Type d'anomalie | Exemple |
|---|---|
| **Manque** | Pas de plan du local technique |
| **Incohérence** | 3 prises sur le plan, 4 postes dans le cahier |
| **Écart terrain** | Une prise du plan est derrière une armoire |
| **Risque** | Une plage DHCP recouvre l'imprimante en adresse fixe |

### ✅ Vérifie que tu as compris

Classe : (a) « le plan montre 8 prises, le cahier demande 10 » ; (b) « la prise du plan est dans un mur porteur impossible à percer ».

<details markdown="1"><summary>Voir la réponse</summary>

(a) **Incohérence** entre deux pièces (plan ↔ cahier). (b) **Écart terrain** (plan ↔ réalité).

</details>

---

## 3. Préparer la liste du matériel

Pour chaque ligne : **quantité** nécessaire, **marge** (≈ 10 %), **disponible en stock ?**, **à commander ?**.

| Matériel | Besoin | Stock | Manque |
|---|---|---|---|
| Switch 24 ports PoE | 1 | 2 | 0 |
| Cordons RJ45 2 m | 13 + marge | 20 | … |

> [!TIP]
> Compte **d'abord les prises** (une par équipement), puis les **cordons** (deux par liaison : poste→prise, panneau→switch).

## 🧠 À retenir

- Un dossier se lit avec **trois questions** : complet ? cohérent ? conforme au terrain ?
- On **signale** et on **fait valider** avant d'installer.
- La liste du matériel se compare **toujours** au stock.
