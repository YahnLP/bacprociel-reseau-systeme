# Corrigé P08 – VLAN (1)

## Partie A
Ping PC3→PC1 : répond. Fa0/1 à Fa0/4 : VLAN 1 (default). Un seul VLAN (le 1) existe. Tous les ports sont dans le même domaine de diffusion.

## Partie B
VLAN 10 : aucun port. PC3→PC1 : répond encore (les ports sont toujours en VLAN 1).

## Partie C
PC1↔PC2 : oui ; PC3↔PC4 : oui ; PC1→PC3 : « Délai d'attente dépassé » ; PC4→PC2 : idem. Ce qui sépare : les VLAN. La table MAC a une colonne **Vlan** renseignée (10 / 20).

## Partie D
PC1/PC2 en 192.168.10.x, PC3/PC4 en 192.168.20.x. Deux raisons : VLAN différents ET sous-réseaux différents (sans routeur).

## Partie E (fichier panne)
Paires qui échouent : PC1↔PC2 (PC2 est dans le VLAN 20) et PC3↔PC4 (PC4 est resté en VLAN 1). Corrections : `interface fa0/2` → `switchport access vlan 10` ; `interface fa0/4` → `switchport mode access` + `switchport access vlan 20`.

## Partie F
| VLAN | Nom | Sous-réseau | Ports | Passerelle |
|---|---|---|---|---|
| 10 | DIRECTION | 192.168.10.0/24 | Fa0/1–2 | 192.168.10.1 |
| 20 | ATELIER | 192.168.20.0/24 | Fa0/3–4 | 192.168.20.1 |

Bilan Q3 : un équipement partagé suppose du routage inter-VLAN (Terminale) ou une interface dans chaque VLAN.
