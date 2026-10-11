# 📖 Cours – Préparer une soutenance technique

*Bac Pro CIEL – Première – E31 – S19*

> [!IMPORTANT]
> **Une idée à la fois.** Réponds à la question **avant** de déplier la réponse.

## 🎯 À la fin de ce cours, tu sauras

- [ ] construire un **plan** de 8 minutes ;
- [ ] choisir une **démonstration** qui convainc ;
- [ ] répondre à une question **sans bluffer** ;
- [ ] **dépanner en parlant** : verbaliser sa démarche.

---

## 1. Le plan en 4 temps

### 🤔 Avant de lire : à ton avis ?

Tu as 8 minutes. Vaut-il mieux présenter **tout** ce que tu as fait, ou **choisir** ?

<details markdown="1"><summary>Voir la réponse</summary>

**Choisir.** Le jury ne retient que **3 idées**. Il vaut mieux 3 choix **bien justifiés** que 20 détails survolés.

</details>

### 💡 L'idée

| Temps | Durée | Contenu |
|---|---|---|
| **1. Le besoin** | 1 min | Le client, les 3 services, les exigences clés |
| **2. La solution** | 3 min | Schéma, découpage, VLAN, filtrage : **pourquoi ces choix ?** |
| **3. La preuve** | 3 min | La recette : ce qui marche **et** ce qui est bloqué |
| **4. Le bilan** | 1 min | Difficultés, ce qu'on referait autrement |

> [!TIP]
> **Chacun parle.** Répartis par **rôle** (réseau, services, recette), pas par diapositive.

### ✅ Vérifie que tu as compris

Quel élément du schéma **montres-tu** quand tu expliques le filtrage des invités ?

<details markdown="1"><summary>Voir la réponse</summary>

Le **chemin** d'un invité : portable → borne → VLAN 30 → routeur (ACL) → serveur : **autorisé** (web, DNS) ; vers Direction ou imprimante : **bloqué**. On **suit le trajet** avec le doigt ou le pointeur.

</details>

---

## 2. La démonstration

- Prépare **5 tests** courts (30 secondes chacun) : 3 qui **marchent**, 2 qui **échouent volontairement**.
- **Annonce** ce que tu attends **avant** de lancer : « Je vais prouver que le portable invité n'atteint pas la Direction. »
- Garde une **maquette de secours** (fichier enregistré) si quelque chose casse.

---

## 3. Les questions du jury

### 🤔 Avant de lire : à ton avis ?

Le jury te demande quelque chose que **tu ne sais pas**. Que fais-tu ?

<details markdown="1"><summary>Voir la réponse</summary>

Tu **dis que tu ne sais pas** et tu **raisonnes** : « Je ne suis pas sûr, mais je vérifierais d'abord… ». Le jury **valorise** la démarche. **Inventer** une réponse fausse est pire que l'honnêteté.

</details>

### Questions fréquentes

| Question | Pistes |
|---|---|
| Pourquoi ce masque ? | Nombre de machines + marge |
| Que se passe-t-il si le routeur tombe ? | Services isolés, **point unique de défaillance** |
| Pourquoi des VLAN ? | Séparer, **sécuriser**, ne pas gaspiller de matériel |
| Un invité peut-il imprimer ? | Non : ACL, imprimante dans l'Atelier |
| Comment retrouver la config ? | Dossier technique, `write memory`, copie texte |

---

## 4. Dépanner en parlant

Pour la panne en direct, **dis ce que tu fais** :

> « Je constate… je regarde si… mon hypothèse est… je teste avec… donc la cause est… je corrige par… et je vérifie. »

Le jury évalue ta **méthode** : constater, délimiter, tester une hypothèse à la fois, vérifier.

## 🧠 À retenir

- **Choisir** 3 idées, les **justifier**.
- Montrer **ce qui marche et ce qui est bloqué**.
- **Parler** pendant qu'on dépanne.
