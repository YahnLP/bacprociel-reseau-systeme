# 📖 Cours – La recette et l'oral

*Bac Pro CIEL – Seconde – E31 – S17*

> [!IMPORTANT]
> **Une idée à la fois.** Réponds à la question **avant** de déplier la réponse.

## 🎯 À la fin de ce cours, tu sauras

- [ ] écrire une **fiche de recette** ;
- [ ] **tester** sans oublier de cas ;
- [ ] **présenter** un projet en 5 minutes.

---

## 1. La recette : prouver que ça marche

### 🤔 Avant de lire : à ton avis ?

Tu as fini l'installation. Tu dis au client : « Ça marche, j'ai essayé sur mon poste. » **Est-ce suffisant ?**

<details markdown="1"><summary>Voir la réponse</summary>

Non. Un test sur **un** poste ne prouve rien pour les trois autres, ni pour l'imprimante, ni pour le Wi-Fi. La **recette** est l'ensemble des tests, **écrits**, qui prouvent que **chaque besoin du cahier des charges** est satisfait.

</details>

### 💡 L'idée

Pour **chaque besoin**, on écrit **un test** : **ce que je fais**, **le résultat attendu**, **le résultat obtenu**, **OK ou KO**.

| Besoin | Test | Attendu | Obtenu | OK ? |
|---|---|---|---|---|
| B1 Internet | Depuis chaque poste : ouvrir `http://www.exemple.fr` | Page affichée | | |
| B2 Imprimante | `ping 192.168.1.150` depuis chaque poste | 4 réponses | | |

> [!TIP]
> **Un bon test est précis** (commande ou action exacte), **mesurable** (réponse ou page) et **répétable** (un collègue peut le refaire).

### ✅ Vérifie que tu as compris

Le besoin B5 est « le Wi-Fi invité n'accède pas aux fichiers ». **Quel test écris-tu ?**

<details markdown="1"><summary>Voir la réponse</summary>

Depuis le **portable invité**, essayer d'ouvrir `\\192.168.1.10\Commandes` et de joindre `192.168.1.150` : **résultat attendu : refus / pas de réponse** (alors qu'`http://www.exemple.fr` s'ouvre). *Un test peut avoir pour résultat attendu un **échec**.*

</details>

---

## 2. Présenter son projet en 5 minutes

### 🤔 Avant de lire : à ton avis ?

Tu as 5 minutes pour présenter un réseau. Qu'est-ce que le client veut **vraiment** voir ?

<details markdown="1"><summary>Voir la réponse</summary>

**Que ça marche** (une démonstration), **que tu comprends** ce que tu as fait (le schéma, les choix), et **qu'il pourra dépanner** (le dossier). Pas la liste de tout ce que tu as cliqué.

</details>

### 💡 L'idée

Plan en **5 temps** (voir [le plan de l'oral](04-plan-oral.md)) :

1. **Le besoin** (30 s) : « Le client voulait… »
2. **Le schéma** (1 min) : montrer et expliquer les liens.
3. **Mes choix** (1 min 30) : adresses, plage DHCP, imprimante, Wi-Fi.
4. **La démo** (1 min 30) : un test en direct.
5. **Un problème rencontré** (30 s) : ce qui n'a pas marché et comment tu l'as réglé.

### ✅ Vérifie que tu as compris

« J'ai mis `192.168.1.150` à l'imprimante » est une phrase **incomplète** à l'oral. Que manque-t-il ?

<details markdown="1"><summary>Voir la réponse</summary>

**Pourquoi** : *« …en dehors de la plage DHCP .10–.100, pour que le DHCP ne la donne jamais à un poste. »* Un choix **expliqué** vaut plus qu'un choix **annoncé**.

</details>

---

## 📌 Vocabulaire

| Mot | Définition |
|---|---|
| **Recette** | Ensemble des tests qui valident l'installation |
| **Résultat attendu / obtenu** | Ce qu'on devrait voir / ce qu'on voit réellement |
| **OK / KO** | Test réussi / test échoué |
| **Dossier technique** | Les documents qui permettent de comprendre et dépanner |

## 🏁 Retiens l'essentiel

- [ ] Un besoin = un **test écrit**.
- [ ] Je note le **résultat obtenu**, pas seulement « OK ».
- [ ] Je **présente** : besoin, schéma, choix, démo, problème.

➡️ **Suite :** [le TP](02-tp.md).
