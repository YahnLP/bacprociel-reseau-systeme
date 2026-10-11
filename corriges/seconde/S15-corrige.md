# Corrigé S15 – Dépannage de niveau 1 (enseignant)

## Les 5 pannes (poste PC-CLIENT ; référence PC-REF)

| N° | Cause | Indices attendus | Correction | Vérification |
|---|---|---|---|---|
| 1 | PC-CLIENT non relié à SW1 | `ipconfig` : « Média déconnecté » ; schéma : pas de câble | Relier au port 3 de SW1 | DHCP : 192.168.1.x, site OK |
| 2 | IP fixe 192.168.10.30/24 (autre réseau) | `ipconfig` : 192.168.10.30 ; `ping 192.168.1.1` : « échec général » | DHCP (ou 192.168.1.30/24, GW et DNS 192.168.1.1) | ping box, Internet, site |
| 3 | Passerelle 192.168.1.2 (fausse) | Box OK ; `ping 203.0.113.1` : délai dépassé / impossible de joindre l'hôte | Passerelle 192.168.1.1 | ping Internet puis site |
| 4 | DNS 192.168.1.5 (faux) | `ping 203.0.113.1` OK ; `ping www.exemple.fr` : « n'a pas pu trouver l'hôte » ; `nslookup` en délai dépassé | DNS 192.168.1.1 | `nslookup`, site |
| 5 | SW1 non relié à BOX (lan1) | Les deux postes en 169.254.x.x | Câbler SW1 port1 ↔ BOX lan1, attendre le DHCP (ou `ipconfig /renew`) | 192.168.1.x puis site |

Fichiers corrigés : `S15-panne-N-corrige.json` (même dossier). Tous validés avec un contrôle automatique (3 tests : box, Internet par adresse, site par nom) : faux au départ pour les tests concernés, vrais après correction.

## Fiche d'intervention – attendus
Tests dans l'ordre ; valeurs lues (pas « ça ne marche pas ») ; une seule modification ; vérification par le site.

## Barème indicatif du contrôle (/10)
Échelle suivie dans l'ordre 3 · cause correcte 3 · correction + vérification 2 · fiche lisible 2.

## Remédiation
Orienter selon le Passeport : câblage → S10 ; adresses/masque → S11 ; DHCP/passerelle → S12 ; DNS → S13 ; Wi-Fi → S14.
