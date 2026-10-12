# 📖 Cours – Lire un dossier d'installation

*Bac Pro CIEL – Terminale – E31 – S02*

> [!IMPORTANT]
> **Une idée à la fois.** Réponds à la question **avant** de déplier la réponse.

## 🎯 À la fin de ce cours, tu sauras

- [ ] nommer les **pièces** d'un dossier d'installation ;
- [ ] vérifier la **complétude** et la **cohérence** d'un dossier ;
- [ ] **lire** un plan d'alimentation et **vérifier** qu'il suffit (charge, PoE) ;
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

## 3. Le plan d'alimentation de la baie

### 🤔 Avant de lire : à ton avis ?

Un switch PoE doit alimenter **huit caméras de 7 W**. **De quelles informations as-tu besoin avant de les brancher ?**

<details markdown="1"><summary>Voir la réponse</summary>

De la **puissance totale** que le switch peut fournir (son **budget PoE**), de la **puissance de chaque caméra**, et du **circuit électrique** disponible dans la baie (prises, protection, onduleur).

</details>

### 💡 L'idée

Un plan d'alimentation montre **d'où vient le courant** et **ce qui est branché dessus**.

| Symbole / élément | Rôle |
|---|---|
| **Disjoncteur** | Protège le circuit (coupe en cas de surcharge) |
| **Prise 230 V** | Alimente les équipements de la baie |
| **Multiprise de baie** | Répartit plusieurs équipements sur une prise |
| **Onduleur** | Garde la baie alimentée quelques minutes en cas de coupure |
| **Parafoudre** | Protège contre les surtensions |
| **Terre** | Évacue les courants de défaut |

> [!TIP]
> **La règle :** la **somme des puissances** des équipements doit rester **inférieure à la capacité** disponible. Exemple : 8 caméras × 7 W = **56 W**, pour un budget PoE de 120 W : **c'est suffisant**.

> [!WARNING]
> On **ne touche pas** au tableau électrique sans **habilitation** (B1V) : on **signale** et on demande à un électricien.

### ✅ Vérifie que tu as compris

Un switch PoE a un budget de 120 W. On veut brancher 1 borne Wi-Fi de 15 W et 4 caméras de 12 W. **Le budget suffit-il ?**

<details markdown="1"><summary>Voir la réponse</summary>

15 W + 4 × 12 W = **63 W**, inférieur à 120 W : **oui**, il reste **57 W** de marge.

</details>

---

## 4. Préparer la liste du matériel

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
- Le plan d'alimentation se vérifie : **somme des puissances ≤ capacité** ; on ne touche pas au tableau sans habilitation.
- La liste du matériel se compare **toujours** au stock.
