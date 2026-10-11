# 📖 Cours – Recette et dépannage

*Bac Pro CIEL – Première – E31 – S18*

> [!IMPORTANT]
> **Une idée à la fois.** Réponds à la question **avant** de déplier la réponse.

## 🎯 À la fin de ce cours, tu sauras

- [ ] écrire un **test de recette** (action, attendu, obtenu, preuve) ;
- [ ] dépanner avec une **méthode** en 6 temps ;
- [ ] décrire le contenu d'un **dossier technique**.

---

## 1. La recette : prouver que ça marche

### 🤔 Avant de lire : à ton avis ?

Un technicien dit : « J'ai testé, ça marche. » Que manque-t-il pour que le **client** le croie ?

<details markdown="1"><summary>Voir la réponse</summary>

Une **trace** : *quoi* a été testé, *comment*, avec **quel résultat**, et **une preuve** (capture, copie de commande). La recette est un document **signé** : sans elle, la discussion « ça marchait avant » n'a pas de fin.

</details>

### 💡 L'idée

Chaque **exigence** du cahier des charges donne **un ou plusieurs tests** :

| Test | Action | Résultat **attendu** | Résultat **obtenu** | Preuve | OK ? |
|---|---|---|---|---|---|
| T1 | `ipconfig` sur `PC-DIR` | Adresse 192.168.50.10 à .30 | | Capture | |
| T7 | `ping` du portable invité vers `PC-DIR` | **Échec** (« Impossible de joindre ») | | Capture | |

> [!NOTE]
> Écris le **résultat attendu AVANT** de lancer le test. Sinon, on a tendance à trouver « normal » ce qu'on observe.

### ✅ Vérifie que tu as compris

Pourquoi un test dont le résultat attendu est « **échec** » est-il utile ?

<details markdown="1"><summary>Voir la réponse</summary>

Il prouve que le **filtrage** fonctionne : sans lui, on ne saurait pas si les invités sont **vraiment** isolés.

</details>

---

## 2. La méthode de dépannage en 6 temps

| Temps | Question | Exemple |
|---|---|---|
| 1. **Constater** | Que se passe-t-il exactement ? Depuis quand ? | « PC-DIR n'a pas d'adresse » |
| 2. **Délimiter** | Qui est touché ? Qui ne l'est pas ? | « Seule la Direction » |
| 3. **Hypothèses** | Quelles causes possibles, par couche ? | Port, VLAN, relais, pool |
| 4. **Tester** | **Un** test pour **une** hypothèse | `show ip int` sur le routeur |
| 5. **Corriger** | **Un** changement à la fois | Ajouter `ip helper-address` |
| 6. **Vérifier et noter** | Le symptôme a-t-il disparu ? Rien d'autre cassé ? | `ipconfig /renew` ✓ |

### 🤔 Avant de lire : à ton avis ?

Pourquoi ne corriger **qu'une chose à la fois** ?

<details markdown="1"><summary>Voir la réponse</summary>

Si tu changes **trois** choses et que ça remarche, tu ne sais pas **laquelle** réparait. Et si tu casses autre chose, tu ne sais pas **quel** changement l'a causé.

</details>

---

## 3. Le dossier technique

Le dossier que **tu laisses** au client contient :

| Pièce | Contenu |
|---|---|
| **Schéma réseau** | Lisible, daté, légendé |
| **Plan d'adressage** | Réseaux, masques, passerelles, plages, adresses fixes |
| **Plan de VLAN et de ports** | Port par port |
| **Tableau de câblage** | Câbles étiquetés |
| **Configurations** | `show running-config` de chaque équipement, **datée** |
| **Comptes** | Qui a quel mot de passe (**dans un coffre**, pas dans le dossier) |
| **Cahier de recette** | Signé |

> [!WARNING]
> **Ne mets jamais les mots de passe en clair** dans un dossier remis au client : ils vont dans un **gestionnaire de mots de passe** ou une enveloppe scellée.

## 🧠 À retenir

- Une recette = **action, attendu, obtenu, preuve**.
- **Constater → délimiter → hypothèses → tester → corriger → vérifier.**
- Le dossier doit permettre à **quelqu'un d'autre** de reprendre l'installation.
