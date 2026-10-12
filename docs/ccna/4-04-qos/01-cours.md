# 📖 Cours – QoS (qualité de service)

*Parcours CCNA – Domaine 4 – module 4-04 (sujet 4.7)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer **pourquoi** la QoS est utile (voix, vidéo) ;
- [ ] décrire les 5 mécanismes : **classification**, **marquage**, **mise en file**, **gestion de la congestion**, **limitation / lissage** ;
- [ ] configurer une politique simple (priorité à la voix).

---

## 1. Pourquoi la QoS ?

### 🤔 Avant de lire : à ton avis ?

Un lien est saturé par un gros téléchargement. Un appel de visioconférence sur le même lien devient haché. Que faut-il faire, **à part** acheter plus de débit ?

<details markdown="1"><summary>Voir la réponse</summary>

**Prioriser** le trafic sensible (voix, vidéo) devant le trafic qui supporte le retard (téléchargement). C'est la **QoS**.

</details>

| Trafic | Ce qu'il supporte mal |
|---|---|
| **Voix** | Le **délai** (> 150 ms), la **gigue** (variation du délai), la **perte** |
| **Vidéo** | La perte, la gigue |
| **Données** (web, fichiers) | Peu sensibles au délai |

Quatre mots à connaître : **débit** (*bandwidth*), **délai** (*delay*, *latency*), **gigue** (*jitter*), **perte** (*loss*).

## 2. Les mécanismes (le programme de l'examen)

| Mécanisme | Rôle | Anglais |
|---|---|---|
| **Classification** | Reconnaître le type de trafic (voix, vidéo…) | *classification* |
| **Marquage** | Écrire une **étiquette** dans le paquet (DSCP, CoS) | *marking* |
| **Mise en file** | Ranger les paquets dans des **files** selon leur classe | *queueing* |
| **Gestion de la congestion** | Choisir **quel paquet envoyer** quand le lien est saturé, ou **lequel jeter** | *congestion management / avoidance* |
| **Limitation (policing)** | **Jeter** (ou re-marquer) ce qui dépasse un débit | *policing* |
| **Lissage (shaping)** | **Retarder** ce qui dépasse, pour lisser le débit | *shaping* |

> [!NOTE]
> **Policing** = on **jette** l'excédent (réaction immédiate). **Shaping** = on **met en attente** l'excédent (plus doux, mais ajoute du délai).

### Le marquage DSCP

Un champ de 6 bits dans l'en-tête IP. Valeurs à connaître :

| DSCP | Nom | Usage |
|---|---|---|
| **EF** (46) | *Expedited Forwarding* | **Voix** |
| **AF41** | *Assured Forwarding* | Visioconférence |
| **CS3 / AF31** | | Signalisation |
| **0** (*default*) | *Best effort* | Tout le reste |

## 3. Configurer une politique simple

```text
class-map match-any VOIX
 match dscp ef
policy-map SORTIE
 class VOIX
  priority 256
 class class-default
  fair-queue
interface gigabitEthernet 0/1
 service-policy output SORTIE
```

| Élément | Rôle |
|---|---|
| `class-map` | **Reconnaît** un trafic (classification) |
| `policy-map` | **Décide** quoi faire pour chaque classe |
| `priority 256` | File **prioritaire** de 256 kb/s garantis |
| `service-policy output` | **Applique** la politique en sortie d'une interface |

`show policy-map interface gi0/1` : statistiques par classe.

### ✅ Vérifie que tu as compris

Pourquoi appliquer la politique **en sortie** sur l'interface vers le lien lent ?

<details markdown="1"><summary>Voir la réponse</summary>

C'est **à la sortie** que se forme la **file d'attente** : le lien lent est le goulot, c'est là qu'il faut décider qui passe en premier.

</details>

---

## 🧠 Quiz de fin

**1.** Quel marquage DSCP pour la voix ?

<details markdown="1"><summary>Voir la réponse</summary>

**EF** (46).

</details>

**2.** Différence entre policing et shaping ?

<details markdown="1"><summary>Voir la réponse</summary>

Policing **jette** l'excédent ; shaping le **met en attente**.

</details>

**3.** Que fait une class-map ?

<details markdown="1"><summary>Voir la réponse</summary>

Elle **classe** (reconnaît) un type de trafic.

</details>

**4.** Qu'appelle-t-on « gigue » ?

<details markdown="1"><summary>Voir la réponse</summary>

La **variation du délai** entre paquets successifs.

</details>

➡️ Suite : [le TP du module](02-tp.md).
