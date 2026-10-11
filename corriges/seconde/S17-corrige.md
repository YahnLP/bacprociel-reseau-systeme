# Corrigé S17 – Projet A1 (2/2)

## Pannes introduites (fichiers corrigés `S17-panne-*-corrige.json`)
| Panne | Symptômes | Cause | Correction |
|---|---|---|---|
| imprimante | Internet OK, `ping 192.168.1.150` KO ; recette tests 4 et 6 KO | IMP1 en 192.168.10.150 (autre réseau) | IMP1 : 192.168.1.150/24, GW 192.168.1.1 |
| poste | PC4 en 169.254.x.x (ou « média déconnecté ») ; tests 1, 3, 4 KO pour PC4 | PC4 non relié à SW1 | Relier PC4 au port 5 de SW1 |

## Fiche de recette – attendus
Tests 1 à 11 attendus **OK** (6, 7, 8, 9 sur postes réels). Test 12 : refus sur vraie box seulement (le simulateur n'isole pas l'invité) : accepter « non testable en simulateur » si justifié.

## Barème (/20)
Recette complète 6 · panne diagnostiquée dans l'ordre 4 · fiche d'intervention 4 · dossier 6.
