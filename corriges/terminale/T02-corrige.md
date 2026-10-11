# Corrigé – Terminale S02 (dossier Dubois)

## Les 8 écarts volontaires

| # | Écart | Type | Chiffres |
|---|---|---|---|
| 1 | **Prises insuffisantes** : le plan montre **8** prises (Accueil 2, Bureau 1 : 3, Bureau 2 : 2, Réunion : 1), le cahier en demande **12** (3 + 4 + 3 + 2), plus l'évolution | Incohérence plan ↔ cahier | 4 manquantes (1 par pièce), 3 de plus pour EX8 |
| 2 | **Switch 8 ports** pour **15** ports nécessaires (12 prises + borne + NAS + box) | Incohérence schéma ↔ cahier | Il faut ≥ 18 ports avec l'évolution : **24 ports** |
| 3 | Switch **non administrable** : impossible de créer un VLAN invités (EX7) | Incohérence | Switch administrable obligatoire |
| 4 | **Plage DHCP .10 à .60** recouvre le **NAS (.10)** et l'**imprimante (.20)** en adresses fixes | Risque | Conflit d'adresses ; plage à décaler (ex. .50 à .150) |
| 5 | **Panneau 12 ports** : insuffisant pour 12 prises + borne + NAS | Incohérence liste ↔ cahier | Panneau 24 ports |
| 6 | **Borne Wi-Fi sans alimentation PoE** : switch non PoE, aucun injecteur | Manque | Switch PoE (ou injecteur : 0 en stock) |
| 7 | **Isolation des invités** (EX7) : un seul réseau, aucun routeur/pare-feu ni ACL, la box seule ne suffit pas à isoler | Manque | VLAN invités + routeur avec ACL (ou box avec réseau invité isolé) |
| 8 | **Métrage de câble** et **cordons** absents ou sous-dimensionnés : 13 cordons de 2 m pour **28** nécessaires (2 par liaison) ; câble cat. 6 non quantifié | Manque | Cordons 2 m ≈ 14 (+ marge), 0,5 m ≈ 14 (+ marge) ; câble ≈ 12 prises × 30 m ≈ 360 m + marge (**2 bobines**) |

## Liste du matériel corrigée (exemple)

Switch administrable **PoE** 24 ports (1 en stock) ; panneau 24 ports (1) ; prises murales 15 (20 en stock) ; cordons 2 m : 16 (20) ; cordons 0,5 m : 16 (15 → **1 à commander** ou 3 m) ; câble cat. 6 : ≈ 400 m (305 m en stock → **à commander**) ; borne Wi-Fi (1) ; NAS (**0 → à commander**) ; baie 12 U (1) ; routeur ou pare-feu (**à prévoir**).

## Quelle décision ?

**On démarre après réponse du client** (items 3, 4, 6, 7, 8) ; items 1, 2, 5 sont des corrections de dossier à valider.

## Terrain

Réponses libres selon la salle. Attendu : le technicien **ne modifie pas seul** : il **note**, **photographie**, **informe** le chargé d'affaires et **fait valider**.
