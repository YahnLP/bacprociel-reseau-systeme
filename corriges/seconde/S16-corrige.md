# Corrigé S16 – Projet A1 (1/2)

## Plan d'adressage attendu
| Équipement | Adresse | Mode |
|---|---|---|
| BOX | 192.168.1.1/24 | fixe (passerelle, DNS) |
| PC1 à PC4 | 192.168.1.10 à .100 (DHCP) | DHCP |
| IMP1 | 192.168.1.150/24, GW .1 | fixe hors plage |
| AP1 | sans adresse IP propre (borne non administrable dans le simulateur) | – |
| LAP-INV | DHCP | via Wi-Fi ATELIER-INVITES |

## Câblage de la maquette
SW1 p1↔BOX lan1 ; PC1–PC4 sur SW1 p2–p5 ; IMP1 sur SW1 p6 ; AP1 sur BOX lan2. Fichier solution : `S16-projet-a1-corrige.json`.

## Longueurs (exemple)
Coin technique (bas gauche) → poste 4 (haut droite) ≈ 9 m horizontal + 8 m vertical (Manhattan) ≈ 17 m + 2×2 m montée/descente ≈ 21 m + 10 % ≈ 23 m → câble 25 m (ou 30 m). Les élèves peuvent proposer un autre trajet : valider la méthode, pas la valeur exacte.

## Partage Windows (non simulé)
Droits attendus : `direction` = Modification ; `atelier` = Lecture et exécution ; test refusé à la suppression pour `atelier`.

## Remarques
- Question A : borne sur la box (et pas le switch) : permet d'isoler l'invité sur la vraie box ; dans le simulateur, pas d'isolation.
- Cours §1 « 7 liens » : 4 postes + imprimante + SW1↔BOX + AP↔BOX.
