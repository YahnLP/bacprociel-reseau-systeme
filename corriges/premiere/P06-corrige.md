# Corrigé P06 – Sous-réseaux

## TP
- Partie A : PC1 → réseau .0/26 ; PC2 (.70) → réseau .64/26 (mal placé : devrait être en A) ; PC3 (.71) → .64/26 ; PC4 (.80/24) : sa « vue » est le /24 entier, donc il se croit dans le même réseau que PC1 (erreur de masque).
- Partie B : PC1→PC2 : « Délai d'attente dépassé » (PC2 est dans l'autre /26) ; PC3→PC4 : répond ; PC4→PC1 : « Délai d'attente dépassé » (requête arrive, pas de réponse) ; PC1→PC4 : « échec général » (hors réseau, pas de passerelle).
- Capture : PC4 fait ARP « Who has 192.168.1.10 », PC1 répond, les Echo request arrivent, aucune Echo reply (PC1 juge .80 hors de son /26 → passerelle absente).
- Partie C : PC2 → 192.168.1.20 (ou toute adresse .1 à .62 libre) ; PC4 → 255.255.255.192.
- Partie D : PC1↔PC2 et PC3↔PC4 répondent ; PC1→PC3 ne répond pas (routeur nécessaire, S07).
- Contrôles automatiques du fichier `P06-sousreseaux-corrige.json` : 3.

## Exercices
**N1** : /25 : 7 bits, 128, 126 ; /26 : 6 bits, 64, 62 ; /27 : 5 bits, 32, 30 ; /28 : 4 bits, 16, 14.

**N2** :
| Adresse | Réseau | Diffusion | Utilisable |
|---|---|---|---|
| .45/26 | .0 | .63 | oui |
| .100/26 | .64 | .127 | oui |
| .127/26 | .64 | .127 | **non** (diffusion) |
| .130/26 | .128 | .191 | oui |
| .192/26 | .192 | .255 | **non** (adresse du réseau) |

**N3** : 12 → 14 → 16 → 4 bits → /28 ; 25 → 27 → 32 → 5 bits → /27 ; 60 → 62 → 64 → 6 bits → /26 ; 100 → 102 → 128 → 7 bits → /25.

**N4** : Direction 13 → bloc 16 (/28) ; Atelier 50 → 64 (/26) ; Invités 25 → 32 (/27).
| Service | Réseau | Plage | Diffusion | Passerelle |
|---|---|---|---|---|
| Atelier | 192.168.1.0/26 | .1–.62 | .63 | .62 |
| Invités | 192.168.1.64/27 | .65–.94 | .95 | .94 |
| Direction | 192.168.1.96/28 | .97–.110 | .111 | .110 |
Il reste libre : 192.168.1.112 à .255 (marge de croissance). Autres placements corrects acceptés si pas de chevauchement et alignés sur le pas.

**N5** : 192.168.1.0/27 couvre .0 à .31 ; 192.168.1.16/28 couvre .16 à .31 : **chevauchement** (et .16 n'est pas aligné sur… il l'est pour /28 mais il est *dans* le /27). Correction : Invités en 192.168.1.32/28.

## Barème indicatif (plan d'adressage, /10)
Masques justes (3) · blocs alignés et sans chevauchement (3) · plages et diffusions (2) · passerelles (1) · marge (1).
