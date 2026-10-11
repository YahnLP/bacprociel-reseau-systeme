# Corrigé P09 – VLAN (2) et trunk

## Partie A
PC1→PC3 : « Impossible de joindre l'hôte de destination » (ARP sans réponse). Les VLAN existent sur les deux switchs. `show interfaces trunk` : vide (aucun trunk). Le lien Gi0/1 est un port access du VLAN 1 : il ne transporte pas les VLAN 10/20.

## Partie B
Trunk sur SW1 seul : le ping échoue toujours (SW2 rejette les trames étiquetées sur son port access).

## Partie C
SW2 : `interface gi0/1` / `switchport mode trunk`. PC1↔PC3 et PC2↔PC4 : OK ; PC1→PC2 : échec ; `show interfaces trunk` : `trunking` des deux côtés.

## Partie D
VLAN ID 10 (puis 20 pour PC2→PC4) ; longueur 78 octets (74 + 4 d'étiquette). Capture PC1↔SW1 : **pas d'étiquette** (port access : trames normales, l'étiquette n'existe que sur le trunk).

## Partie E
`allowed vlan 10` : PC1→PC3 OK, PC2→PC4 échec (VLAN 20 non autorisé). Rétablir : `switchport trunk allowed vlan add 20`.

## Partie F (panne)
Erreur 1 : SW2 Gi0/1 est resté en access (pas de trunk de ce côté). Erreur 2 : SW1 n'autorise que le VLAN 10 sur son trunk. Corrections : SW2 `switchport mode trunk` ; SW1 `switchport trunk allowed vlan 10,20` (ou `add 20`).
