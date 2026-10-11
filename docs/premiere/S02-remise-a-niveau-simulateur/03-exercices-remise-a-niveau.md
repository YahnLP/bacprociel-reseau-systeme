# 🧮 Fiche d'exercices – Adresses IP (remise à niveau)

*Réponds **avant** de déplier la correction. Niveau A = facile · B = moyen · C = difficile.*

## Niveau A – Je lis une adresse

**1.** `192.168.1.25/24` : quel est le **réseau** ?

<details markdown="1"><summary>Correction</summary>

**`192.168.1.0`**. En `/24`, les 3 premiers nombres sont le réseau.

</details>

**2.** `10.0.0.5/8` : combien de nombres désignent le **réseau** ?

<details markdown="1"><summary>Correction</summary>

**Un seul** (le `10`). `/8` = 8 bits = un nombre.

</details>

**3.** Dans `192.168.5.0/24`, donne la **première** et la **dernière** adresse **utilisable**.

<details markdown="1"><summary>Correction</summary>

**`192.168.5.1`** et **`192.168.5.254`**. `.0` est le réseau, `.255` la diffusion.

</details>

**4.** Peut-on donner `192.168.5.255` à un PC en `/24` ? Pourquoi ?

<details markdown="1"><summary>Correction</summary>

**Non** : c'est l'adresse de **diffusion**.

</details>

## Niveau B – Je compare deux adresses

**5.** `192.168.10.20/24` et `192.168.10.70/24` : même réseau ?

<details markdown="1"><summary>Correction</summary>

**Oui** (`192.168.10.0/24`). Ils se voient directement.

</details>

**6.** `192.168.10.20/24` et `192.168.100.20/24` : même réseau ?

<details markdown="1"><summary>Correction</summary>

**Non** : `192.168.10.0` ≠ `192.168.100.0`. *Attention aux nombres qui se ressemblent !*

</details>

**7.** `172.16.4.9/16` et `172.16.200.9/16` : même réseau ?

<details markdown="1"><summary>Correction</summary>

**Oui** : en `/16`, seuls `172.16` comptent. Réseau `172.16.0.0/16`.

</details>

**8.** Un PC en `192.168.1.40/24` a pour passerelle `192.168.2.1`. Est-ce possible ? Pourquoi ?

<details markdown="1"><summary>Correction</summary>

**Non** : la passerelle doit être **dans le même réseau** que le poste (`192.168.1.x`). Sinon, le poste ne sait pas la joindre.

</details>

## Niveau C – Je passe aux calculs

**9.** Écris le masque `255.255.255.0` en notation `/..`

<details markdown="1"><summary>Correction</summary>

**`/24`** (3 × 8 bits à 1).

</details>

**10.** `255.255.255.128` : quel préfixe ? *(indice : 128 = `10000000`)*

<details markdown="1"><summary>Correction</summary>

**`/25`** : 24 bits + 1 bit à 1. *(On le reverra en S06 : sous-réseaux.)*

</details>

**11.** Dans un `/24`, combien d'adresses **utilisables** ? Dans un `/16` ?

<details markdown="1"><summary>Correction</summary>

`/24` : 2⁸ − 2 = **254**. `/16` : 2¹⁶ − 2 = **65 534**. *(On enlève le réseau et la diffusion.)*

</details>

**12.** L'imprimante est en `192.168.1.150`. Le DHCP distribue de `.10` à `.100`. Y a-t-il un risque de conflit ? Justifie.

<details markdown="1"><summary>Correction</summary>

**Non** : `.150` est **hors de la plage DHCP** (.10–.100). Un conflit serait possible avec `.50`, par exemple.

</details>
