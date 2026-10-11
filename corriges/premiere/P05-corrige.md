# Corrigé P05 – Switch administrable

## Partie A
Modèle Cisco Catalyst 2960-24TT, IOS 15.0(2)SE4 (simulé) ; 24 FastEthernet + 2 Gigabit ; connectés : Fa0/1, Fa0/2, Fa0/3, Gi0/1 ; table MAC : vide au départ ou quelques entrées selon le trafic ; pas d'IP de gestion.
Expérience : après `clear mac address-table dynamic` + ping de PC1 vers SRV1 : apparaissent PC1 (Fa0/1) et SRV1 (Gi0/1) ; PC2/PC3 n'ont rien émis.

## Partie B
Prompt `SW-ATELIER#` ; après `exit` + `enable` : demande le mot de passe ; secret haché (`enable secret 5 $1$…`). `secret` = haché, `password` = en clair.

## Partie C
21 ports disabled (Fa0/4 à Fa0/24) ; un PC branché sur un port coupé n'obtient aucune liaison (notconnect/disabled).

## Partie D
`ping 192.168.10.2` répond. SSH : `ssh admin@192.168.10.2` → Username: admin → Password. `transport input ssh` : Telnet refusé.

## Partie E
Avant : « startup-config is not present » ; après : la configuration complète. Courant coupé avant `write memory` : la configuration est perdue.

## Contrôles automatiques (fichier P05-switch-corrige.json)
6 contrôles : nom, enable secret, descriptions, ports Fa0/4–24 shutdown, ping du switch, ping serveur.
