# Corrigé P04 – Protocoles usuels

## Partie A (DHCP)
Discover : 0.0.0.0 → 255.255.255.255, UDP 68 → 67 ; Offer / ACK : 192.168.1.1 → 255.255.255.255 (diffusion), UDP 67 → 68 ; Request : 0.0.0.0 → 255.255.255.255. ACK : adresse 192.168.1.10, masque 255.255.255.0, routeur 192.168.1.1, DNS 192.168.1.1, bail 86400 s (24 h).

## Partie B (DNS)
Requête : 192.168.1.10 → 192.168.1.1, UDP port source aléatoire → 53, A www.exemple.fr. Réponse : 192.168.1.1 → 192.168.1.10, A 198.51.100.80. La box relaie.

## Partie C (TCP)
1) PC1 → 198.51.100.80 : SYN ; 2) serveur → PC1 : SYN, ACK ; 3) PC1 → serveur : ACK. Port source aléatoire (ex. 49499), destination 80, seq relatif 0. Le port source change à chaque connexion.

## Partie D (HTTP)
GET / HTTP/1.1 ; Host: www.exemple.fr ; User-Agent: SimuReseau/1.0 ; réponse 200 OK, text/html.

## Fiche : voir corrections repliées.
