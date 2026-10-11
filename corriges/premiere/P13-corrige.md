# Corrigé P13 – Cuivre, fibre, sécurité

## Partie A (simulateur)
Départ : les 4 pings échouent. Câbles défectueux : PC1–SW1 (croisé → droit), SW1–SW2 (droit → croisé), PC3–SW2 (fibre → droit). Un mauvais type ne donne pas un lien lent mais **aucun lien** : les paires d'émission/réception ne se rejoignent pas (MDI/MDI-X) ; la fibre ne peut pas se brancher sur un port cuivre. Après remplacement : 4 pings OK.

## Partie B
A : réussi → accepter. B : échec (103 m > 90 m, atténuation −2 dB) → raccourcir le trajet, ou un brassage intermédiaire (switch) près du poste, ou fibre. C : échec (paire 1-2 inversée) → re-poinçonner ; les voyants s'allument pourtant (le lien « passe ») : seul le testeur de cartographie le détecte.
Rapports : 82 m tout OK → réussi ; paire 4-5 coupée → échec (le Gigabit est impossible, 100 Mb/s possible) ; 91 m avec atténuation −0,5 dB → échec (dépasse 90 m).

## Partie D
Fibre 0,72 dB + connecteurs 1,0 dB + soudures 0,2 dB = **1,92 dB** ; marge 6 − 1,92 = 4,08 dB : conforme. Multimode : 1,8 × 3,5 = 6,3 dB + 1,0 + 0,2 = 7,5 dB > 3,5 dB (et au-delà de la portée en 1 Gb/s multimode d'exercice) : impossible. SFP monomode des deux côtés (longueur d'onde et type de fibre doivent correspondre).

## Fiche d'exercices
**Ex. 1** : 1) 1,2 + 1,0 = 2,2 dB, conforme ; 2) 4,0 + 1,0 + 0,4 = 5,4 dB, conforme (marge 0,6) ; 3) 1,05 + 1,0 = 2,05 dB, conforme ; 4) 1,75 + 2,0 = 3,75 dB > 3,5 dB, non conforme.
**Ex. 2** : 45 m → cuivre cat. 6 ; 350 m + foudre → fibre multimode (isolation électrique) ; 15 m, 10 Gb/s → cuivre cat. 6A ou DAC/fibre multimode ; 6 km → fibre monomode.
**Ex. 3** : 94 m → échec (> 90 m) → raccourcir/fibre ; paires 3-6 coupées → échec → re-poinçonner/changer ; diaphonie −1,1 dB à 71 m → échec → refaire le sertissage/la prise (paires trop détorsadées).
**Ex. 4** : 1 faux ; 2 faux (ne pas ouvrir un switch PoE sous tension) ; 3 préviens le responsable ; 4 contenant dédié.

## Contrôles automatiques (P13-cables-corrige.json)
4 contrôles : PC1↔PC2, PC3↔PC4, PC1↔PC3, PC2↔PC4.
