# 📝 Exercices – Sous-réseaux et plan d'adressage

*Bac Pro CIEL – Première – E31 – S06 – individuel*

> [!IMPORTANT]
> Pas de calculatrice « réseau » avant l'exercice 4. Utilise le **tableau des puissances de 2** du [cours](01-cours.md) (§3).

## Niveau 1 – Tableau de départ

Complète (réseau `192.168.1.0`) :

| Masque | Bits machine | Adresses | Machines utilisables |
|---|---|---|---|
| /24 | 8 | 256 | 254 |
| /25 | | | |
| /26 | | | |
| /27 | | | |
| /28 | | | |

## Niveau 2 – Placer des adresses

Pour chaque adresse /26, donne l'**adresse du réseau**, la **diffusion** et dis si l'adresse est **utilisable** :

| Adresse | Réseau | Diffusion | Utilisable ? |
|---|---|---|---|
| 192.168.1.45/26 | | | |
| 192.168.1.100/26 | | | |
| 192.168.1.127/26 | | | |
| 192.168.1.130/26 | | | |
| 192.168.1.192/26 | | | |

## Niveau 3 – Choisir le masque

| Besoin | Machines + 2 | Bloc | Bits machine | Masque |
|---|---|---|---|---|
| 12 machines | | | | |
| 25 machines | | | | |
| 60 machines | | | | |
| 100 machines | | | | |

## Niveau 4 – Plan d'adressage de la PME (noté)

La PME **MécaPro** possède la plage `192.168.1.0/24`. Elle a besoin de :

| Service | Machines aujourd'hui | Prévoir (+ 25 %) |
|---|---|---|
| Direction | 10 | |
| Atelier | 40 | |
| Invités | 20 | |

1. Complète la colonne **Prévoir** (arrondi au supérieur).
2. Pour chaque service, choisis le **masque** et **place** les blocs **sans chevauchement** (commence par le plus gros).
3. Remplis le plan :

| Service | Réseau/masque | Plage utilisable | Diffusion | Passerelle (dernière utilisable) |
|---|---|---|---|---|
| Atelier | | | | |
| Invités | | | | |
| Direction | | | | |

4. **Vérifie** avec l'outil du professeur (ou une calculatrice de sous-réseaux) : écris les écarts trouvés.

> [!TIP]
> **Méthode :** place d'abord le plus **gros** bloc au début, puis le suivant juste après, et ainsi de suite. On gaspille moins d'adresses.

> [!EXAMPLE]+ 🚀 Pour aller plus loin : le VLSM
> Découper ainsi un réseau en blocs de **tailles différentes** s'appelle le **VLSM** (*Variable Length Subnet Mask*) : chaque sous-réseau reçoit un masque adapté à son nombre de machines.

## Niveau 5 – Défi

Un technicien note : *« Direction 192.168.1.0/27, Invités 192.168.1.16/28. »* Trouve **l'erreur** (indice : cherche le chevauchement).

*Corrigé : `corriges/premiere/P06-corrige.md` (non publié).*
