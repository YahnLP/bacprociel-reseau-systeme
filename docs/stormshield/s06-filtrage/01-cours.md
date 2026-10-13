# 📖 Cours – Le filtrage

*Parcours Stormshield – module S06*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours Stormshield (préparation CSNA). Lien avec les ACL : [module CCNA 5-03](../../ccna/5-03-acl/01-cours.md).

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer le **filtrage à états** ;
- [ ] écrire une **politique** minimale selon le **moindre privilège** ;
- [ ] **ordonner** les règles correctement.

---

## 1. Filtrage à états (*stateful*)

Un pare-feu à états **mémorise** les connexions. Quand un poste du LAN ouvre une connexion vers un site web, la **réponse** est acceptée automatiquement : pas besoin de règle « retour ». Un paquet **sans connexion connue** (par exemple une réponse non sollicitée) est bloqué.

## 2. Une règle de filtrage

| Champ | Question |
|---|---|
| **Action** | autoriser (*pass*), bloquer (*block*, sans réponse) ou rejeter (*reset* : le client est averti) |
| **Source** | d'où ? (zone, adresse) |
| **Destination** | vers où ? |
| **Service / port** | quel protocole ? |
| **Commentaire** | pourquoi cette règle existe |

## 3. L'ordre compte

Les règles sont lues **de haut en bas** ; **la première qui correspond s'applique**, les suivantes sont ignorées. À la fin, la **politique par défaut** bloque tout.

| Ordre | Règle | Effet |
|---|---|---|
| 1 | Bloquer `192.168.1.50` → Internet | le stagiaire est refusé |
| 2 | Autoriser LAN → Internet, web | les autres passent |

> [!WARNING]
> **Si on inverse** (règle 2 avant la règle 1), le stagiaire est autorisé par la règle 2 : la règle de blocage n'est **jamais atteinte**. **Le plus précis en haut, le plus général en bas.**

## 4. Moindre privilège

On n'autorise que **le strict nécessaire** : un flux = une règle précise (zones, source, service). On évite `any → any`.

| À éviter | À préférer |
|---|---|
| LAN → WAN, **tout** | LAN → WAN, TCP **80 et 443**, UDP **53** |
| DMZ → LAN, tout | aucune règle (bloqué par défaut) |

## 5. Dans le simulateur

Onglet **Règles de filtrage** : tableau ordonné, boutons **↑ ↓** pour changer l'ordre, case **On** pour activer ou désactiver, colonne **Hits** (nombre d'utilisations). La dernière ligne grisée est la politique par défaut (**bloquer**).

> [!NOTE]
> 🧊 **Limite du simulateur.** Pas d'inspection applicative (IPS, antivirus, URL), pas de règles par utilisateur ni par heure, pas d'objets, pas de plusieurs politiques (*slots*). **Alternative Packet Tracer :** une ACL étendue sur un routeur Cisco : ordre, `permit`/`deny`, refus implicite final (module [CCNA 5-03](../../ccna/5-03-acl/01-cours.md)). **Alternative VM :** EVA, rubrique *Politique de sécurité → Filtrage et NAT*.

## 🔧 Dépanner : « la bonne règle existe, mais ce n'est pas elle qui s'applique »

> [!NOTE]
> **Pourquoi ce chapitre ?** Dans 80 % des cas, une panne de filtrage n'est pas une règle *absente* : c'est une règle **mal placée**, **mal écrite** (mauvaise zone, mauvais port) ou **désactivée**. Le journal indique quelle règle a décidé : on compare avec celle qu'on attendait.

### Panne 1 – L'ordre des règles

*Situation voulue :* `PC-STAGIAIRE` est bloqué. On déplace la règle de blocage **sous** la règle générale « web ».

```text
Avant (règle de blocage en 1) :
BLOCK 192.168.1.50:50489 → 198.51.100.80:80 [LAN→WAN] règle 1

Après (déplacée en 2) :
PASS  192.168.1.50:50490 → 198.51.100.80:80 [LAN→WAN] règle 1
```

Le stagiaire **passe** : la règle générale, placée avant, correspond la première et le moteur s'arrête là. **Correction :** remettre la règle **spécifique** (le blocage) **au-dessus** de la règle générale. Les règles sont évaluées **de haut en bas**, la première qui correspond s'applique.

### Panne 2 – La mauvaise zone

*Situation :* la règle « LAN → DMZ, tcp 80 » est écrite par erreur avec la zone source `WAN`.

```text
BLOCK 192.168.1.10:49474 → 172.16.0.10:80 [LAN→DMZ] politique par défaut
```

Le journal dit `LAN→DMZ` (la **réalité** du flux) et `politique par défaut` : aucune règle `LAN→DMZ` n'existe plus. **Méthode :** compare la zone **du journal** avec la zone **de ta règle**.

### Panne 3 – La règle est désactivée

Même signature que la panne précédente (`politique par défaut`), mais la règle est bien là : elle est simplement **décochée**. Regarde l'état (activée / désactivée) de chaque règle, pas seulement son contenu.

> [!TIP]
> **Le compteur de correspondances (*Hits*).** Une règle qui devrait servir et dont le compteur reste à **0** ne correspond jamais : zone, adresses ou port mal écrits, ou règle placée derrière une autre.

### Récapitulatif

| Journal | Cause probable |
|---|---|
| `PASS … règle N` alors que tu voulais bloquer | une règle plus **haute** ou plus **large** passe avant |
| `BLOCK … politique par défaut` | règle absente, désactivée, mauvaise zone ou mauvais port |
| `BLOCK … règle N` alors que tu voulais passer | règle de blocage trop **large** ou trop **haute** |

---

## 🧠 Quiz de fin

**1.** Qu'est-ce que le filtrage à états ?

<details markdown="1"><summary>Voir la réponse</summary>

Le pare-feu **mémorise les connexions** : les réponses aux connexions autorisées passent automatiquement.

</details>

**2.** Dans quel ordre place-t-on les règles ?

<details markdown="1"><summary>Voir la réponse</summary>

Les **plus précises en haut**, les plus générales en bas.

</details>

**3.** Que fait le pare-feu d'un flux qui ne correspond à aucune règle ?

<details markdown="1"><summary>Voir la réponse</summary>

Il le **bloque** (politique par défaut).

</details>

**4.** Quelle différence entre *block* et *reset* ?

<details markdown="1"><summary>Voir la réponse</summary>

*Block* **ignore** le paquet sans rien dire ; *reset* **prévient** l'émetteur que la connexion est refusée.

</details>

➡️ Suite : [le TP du module](02-tp.md).
