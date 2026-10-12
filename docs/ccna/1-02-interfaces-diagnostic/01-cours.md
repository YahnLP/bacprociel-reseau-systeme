# 📖 Cours – Interfaces, câbles et diagnostic

*Parcours CCNA – Domaine 1 – module 1-02 (sujets 1.3 et 1.4)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**. Tu connais déjà le câble RJ45 : ici, on va plus loin.

## 🎯 À la fin de ce cours, tu sauras

- [ ] choisir entre **cuivre** et **fibre** (monomode / multimode) ;
- [ ] distinguer **média partagé** et **liaison point à point** ;
- [ ] lire l'état d'une interface et repérer un problème de **duplex**, de **vitesse** ou d'**erreurs**.

---

## 1. Cuivre ou fibre ?

### 🤔 Avant de lire : à ton avis ?

Deux bâtiments sont distants de 800 m. Pourquoi ne pas simplement tirer un câble RJ45 ?

<details markdown="1"><summary>Voir la réponse</summary>

Le câble cuivre est limité à **100 m**. Au-delà, il faut de la **fibre optique** (ou un équipement intermédiaire).

</details>

| Média | Distance typique | Débit | Avantage | Inconvénient |
|---|---|---|---|---|
| **Cuivre** (paires torsadées Cat5e/6) | jusqu'à **100 m** | 100 Mb/s à 10 Gb/s | peu cher, facile | parasites, distance limitée |
| **Fibre multimode** (*MMF*) | quelques centaines de mètres | 1 à 10 Gb/s | insensible aux parasites | coût plus élevé |
| **Fibre monomode** (*SMF*) | **dizaines de kilomètres** | 10 Gb/s et plus | très longue distance | optiques plus chères |

> [!NOTE]
> **Multimode** : plusieurs « rayons » de lumière dans un cœur large, pour les **courtes distances**. **Monomode** : un seul rayon dans un cœur très fin, pour les **longues distances**.

### 💡 Partagé ou point à point ?

- **Média partagé** : plusieurs appareils utilisent **le même support** (l'ancien Ethernet à hub, le **Wi-Fi**). Ils doivent se partager la parole : risque de **collisions**.
- **Point à point** : un câble relie **deux** équipements seulement (switch ↔ poste). Aucune collision en **full duplex**.

---

## 2. Duplex, vitesse et erreurs

### 💡 Duplex

| Mode | Principe |
|---|---|
| **Half duplex** | On émet **ou** on reçoit, jamais les deux en même temps (talkie-walkie) |
| **Full duplex** | On émet **et** on reçoit en même temps (téléphone) |

Les deux bouts d'un câble doivent utiliser **la même vitesse et le même duplex**.

### 🔎 Le piège : l'incompatibilité de duplex (*duplex mismatch*)

Si une extrémité est en **full duplex** et l'autre en **half duplex**, le lien « marche » mais est **très lent** et génère des erreurs (**collisions tardives**, **erreurs CRC**).

| Symptôme sur une interface | Cause probable |
|---|---|
| `CRC` en augmentation | câble abîmé, parasites, ou duplex différent |
| `late collision` | duplex différent (un bout en half) |
| `runts` (trames trop courtes) | collisions, duplex |
| `giants` (trames trop longues) | carte réseau défaillante, mauvaise configuration |
| interface `down` | câble débranché ou mauvais type de câble |

### 🛠️ Commandes utiles

| Commande | Ce qu'elle montre |
|---|---|
| `show interfaces status` | une ligne par port : état, VLAN, **duplex**, **vitesse** |
| `show interfaces fa0/1` | détail : état, MTU, compteurs d'entrée/sortie, erreurs |
| `show ip interface brief` | (routeur) adresse IP et état de chaque interface |

```text
SW1#show interfaces status
Port      Name   Status      Vlan   Duplex  Speed  Type
Fa0/1            connected   1      a-full  a-100  10/100BaseTX
Fa0/2            notconnect  1      auto    auto   10/100BaseTX
```

Le préfixe **`a-`** (*auto*) signifie « **négocié** automatiquement » : `a-full`, `a-100`.

> [!WARNING]
> Dans le simulateur, forcer `speed 10` et `duplex half` sur un seul port **n'entraîne pas de panne visible** : l'incompatibilité n'est pas simulée. Sur du matériel réel, tu verrais les compteurs d'erreurs grimper.

### ✅ Vérifie que tu as compris

Un lien se met à ramer et `show interfaces` affiche des `late collisions`. Quelle est la cause la plus probable ?

<details markdown="1"><summary>Voir la réponse</summary>

Une **incompatibilité de duplex** : un bout est en half duplex, l'autre en full.

</details>

---

## 🧠 Quiz de fin

**1.** Quelle distance maximale pour un câble cuivre Ethernet ?

<details markdown="1"><summary>Voir la réponse</summary>

**100 m**.

</details>

**2.** Pour relier deux sites à 15 km, quelle fibre ?

<details markdown="1"><summary>Voir la réponse</summary>

**Monomode** (*single-mode*).

</details>

**3.** Que veut dire `a-full` dans `show interfaces status` ?

<details markdown="1"><summary>Voir la réponse</summary>

Duplex **full**, **négocié automatiquement**.

</details>

**4.** Le Wi-Fi est-il un média partagé ou point à point ?

<details markdown="1"><summary>Voir la réponse</summary>

**Partagé** : tous les appareils d'un canal se partagent le même air.

</details>

➡️ Suite : [le TP du module](02-tp.md).
