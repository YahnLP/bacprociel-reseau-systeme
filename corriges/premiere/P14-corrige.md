# Corrigé P14 – Sécurité de base

## Partie A
Switch d'origine : aucun `enable secret` ; `line vty` : `password cisco` visible, `transport input all` (Telnet autorisé) ; 24 ports actifs/`notconnect` (2 utilisés) ; `startup-config` vide/absente. Capture Telnet : `Data: cisco\r\n` : le mot de passe est lisible par quiconque capture le trafic (poste compromis, Wi-Fi, switch pirate). Web : 200 OK ; ping vers le serveur : répond (inutile et utile à un attaquant pour cartographier). Pas d'ACL.

## Partie B
Telnet refusé, SSH demandé, Fa0/3–24 `disabled`. Mots de passe par défaut : listés en premier par les attaquants. Ports libres : empêcher un branchement non autorisé.

## Partie C
Web : OK ; ping 192.168.20.100 : « Communication administrativement filtrée » (règle 30) ; ping 192.168.20.1 : filtré aussi (la règle `deny ip any any` bloque aussi les paquets vers le routeur, destination 192.168.20.1 — noter que le trafic **vers** le routeur lui-même, sur son interface d'entrée, est aussi filtré par l'ACL). Matches : règle 10 (web) et règle 30 (refus). Sans `deny` explicite : refus implicite identique, mais invisible et non compté.

## Partie D (VM, non testée en direct)
`ss -tlnp` : 22 (ssh) et éventuellement 53 (systemd-resolved, local). Sans `allow 22/tcp` avant `enable`, la session SSH est coupée et inaccessible : il faut la console. Nombre de paquets à mettre à jour : variable.

## Partie E
`startup-config` contient `transport input ssh`. 3-2-1 : copie sur le PC, copie sur un autre support (clé/NAS), copie hors site (cloud privé/coffre).

## Contrôles automatiques (P14-securite-corrige.json)
7 contrôles : enable secret, SSH seul, bannière, ports Fa0/24 shutdown, startup-config sauvegardée, web OK, ping filtré.
