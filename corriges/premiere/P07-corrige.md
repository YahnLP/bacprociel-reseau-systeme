# Corrigé P07 – Routeur et routage statique

## Partie A
`PC1` ne joint pas sa passerelle (R1 n'a pas d'IP) ; `show ip interface brief` : interfaces `unassigned`, `administratively down` ; ping vers le serveur : délai dépassé (pas de passerelle joignable).

## Partie B
Interfaces `up/up`. Oublier `no shutdown` : `administratively down / down`. `show ip route` : `C 192.168.10.0/24` et `C 10.0.0.0/30` (+ lignes `L`).

## Partie C
R2 : gi0/0 192.168.20.1/24 ; gi0/1 10.0.0.2/30 ; `ping 10.0.0.2` depuis R1 : `!!!!!`.

## Partie D
Message : « Réponse de 192.168.10.1 : Impossible de joindre le réseau de destination. » C'est **R1** qui répond : il ne connaît pas 192.168.20.0/24.

## Partie E
E1 : après `ip route 192.168.20.0 255.255.255.0 10.0.0.2` sur R1 : ping « Délai d'attente de la demande dépassé » ; tracert : saut 1 = 192.168.10.1, puis `*`. Le dernier routeur qui répond est R1. R2 ne connaît pas 192.168.10.0/24 → réponse jetée.
E2 : `ip route 192.168.10.0 255.255.255.0 10.0.0.1` sur R2. Après : ping OK (TTL=62), tracert : 192.168.10.1 → 10.0.0.2 → 192.168.20.100.

## Partie F
`SRV1` joint `PC2` directement : R2 a la route vers 192.168.10.0/24 et R1 a le réseau connecté 192.168.10.0/24.

## Partie G
`S* 0.0.0.0/0 [1/0] via 10.0.0.2`, « Gateway of last resort is 10.0.0.2 ». `PC1` joint toujours SRV1. Avantage : **une seule** ligne quel que soit le nombre de réseaux lointains.

## Contrôles automatiques (fichier P07-routage-corrige.json)
5 contrôles : PC1→R1, R1→R2, PC1→SRV1, SRV1→PC2, route statique S vers 192.168.20.0 (le corrigé conserve la route statique, pas la route par défaut).
