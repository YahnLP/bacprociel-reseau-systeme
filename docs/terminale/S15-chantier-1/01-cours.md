# 📖 Cours – Réussir un chantier complet

*Bac Pro CIEL – Terminale – E31 – S15*

> [!IMPORTANT]
> **Une idée à la fois.** Réponds à la question **avant** de déplier la réponse.

## 🎯 À la fin de ce cours, tu sauras

- [ ] **organiser** ses 3 heures ;
- [ ] **prouver** ce qu'on fait ;
- [ ] **ne pas bloquer** sur une étape.

---

## 1. Un chantier, c'est du temps à répartir

### 🤔 Avant de lire : à ton avis ?

Tu as 3 heures. Tu passes 1 h 30 à configurer le Wi-Fi parfaitement. **Quel est le risque ?**

<details markdown="1"><summary>Voir la réponse</summary>

Tu n'auras **pas le temps** de tester, documenter et rédiger la recette : or **l'évaluateur regarde aussi ces traces**.

</details>

### 💡 L'idée

![Répartir 3 heures](images/chantier-3h.svg)

**Chaque étape se termine par une preuve :** capture d'écran, résultat de commande, ligne de compte rendu.

### ✅ Vérifie que tu as compris

À la 2ᵉ heure, tu es en retard de 15 minutes sur le câblage. **Que fais-tu ?**

<details markdown="1"><summary>Voir la réponse</summary>

Je **finis le câblage proprement** (c'est la base), je **note le retard** et j'**enchaîne** : la configuration en dépend. Je rattrape en **documentant au fil de l'eau**.

</details>

---

## 2. Je commence par le dossier

### 🤔 Avant de lire : à ton avis ?

Un dossier de chantier contient un **cahier des charges** de 12 lignes. Combien de minutes pour le lire ? Qu'en tires-tu ?

<details markdown="1"><summary>Voir la réponse</summary>

**10 à 15 minutes** : je **surligne chaque exigence** et j'en fais une **liste de tests**. Cette liste devient mon **cahier de recette**.

</details>

### 💡 L'idée

1. Je **lis** tout le dossier.
2. Je **liste** les exigences (« les patients ont Internet », « les patients ne voient pas l'imprimante »…).
3. Je **complète le plan d'adressage** (réseaux, plages, adresses fixes).
4. Je **déduis les tests** (dont les **négatifs**).
5. Je **prépare** : matériel, étiquettes, ordre des commandes.

### ✅ Vérifie que tu as compris

L'exigence est : « les patients ne doivent pas voir l'imprimante ». **Quel test écris-tu ?**

<details markdown="1"><summary>Voir la réponse</summary>

Un test **négatif** : depuis le Wi-Fi patients, **ping de l'imprimante**, **attendu : aucune réponse**.

</details>

---

## 3. Si je bloque

### 🤔 Avant de lire : à ton avis ?

Ton poste n'a pas d'adresse `192.168.20.x` en Wi-Fi alors que tout semble bien configuré. **Que fais-tu ?**

<details markdown="1"><summary>Voir la réponse</summary>

Je **monte l'échelle des tests** : lien Wi-Fi associé ? bon SSID/clé ? bon VLAN ? **DHCP joignable** ? **ACL** qui bloque le DHCP ?

</details>

### 💡 L'idée

> **Quand je bloque : je n'essaie pas au hasard. J'applique la méthode (S11).**

Une **ACL** qui se termine par `deny ip any any` bloque aussi le **DHCP** : il faut alors autoriser `udp any eq 68 any eq 67`.

### ✅ Vérifie que tu as compris

Une ACL se termine par `deny ip any any`. Les patients n'ont plus d'adresse. **Quelle règle manque-t-il ?**

<details markdown="1"><summary>Voir la réponse</summary>

`permit udp any eq 68 any eq 67` : elle laisse passer les demandes **DHCP** des clients vers le serveur.

</details>

---

## 🧠 À retenir

- **3 h = 6 étapes chronométrées.**
- **Le dossier donne les tests.**
- **Chaque étape laisse une preuve.**
- **Bloqué ? méthode, pas hasard.**
- **Documenter au fil de l'eau.**
