# Corrigé P11 – DHCP et DNS

## Partie A
PC1 : 169.254.x.x / 255.255.0.0, pas de passerelle ; ping 192.168.10.1 : « échec général » (pas de route). Adresse APIPA = aucun DHCP.

## Partie B
Pool LAN, réseau 192.168.10.0, masque 255.255.255.0, passerelle 192.168.10.1, DNS 192.168.10.2, domaine mecapro.local, plage .50→.150, bail 28800 s ; exclusions .1→.49 ; service activé. Postes : 192.168.10.50, .51, .52 (selon ordre) ; passerelle .1 ; DNS .2. Bail : durée 8 h (28 800 s) ; le serveur liste 3 baux actifs.

## Partie C
srv → 192.168.10.2 ; intranet → 192.168.10.2 ; imprimante → 192.168.10.30. nslookup : « Réponse ne faisant pas autorité » (pas de zone déclarée comme faisant autorité dans le simulateur ; sans conséquence). Pings par nom : réponses.

## Partie D
`ping inconnu…` : « La requête Ping n'a pas pu trouver l'hôte… » (nom introuvable) ; nslookup : « Non-existent domain ». Différence : DNS ne trouve pas le nom / nom trouvé mais l'hôte ne répond pas (éteint, mauvaise adresse).

## Partie E
`ipconfig /all` : DNS reçu 192.168.10.3 (faux) → nslookup : « Délai d'attente dépassé (le serveur 192.168.10.3 ne répond pas) ». Erreur 1 : pool DHCP distribue le DNS 192.168.10.3 → mettre 192.168.10.2 puis `ipconfig /renew` sur chaque poste. Erreur 2 : zone : `intranet.mecapro.local` → 192.168.10.20 au lieu de 192.168.10.2 → corriger l'enregistrement.

## Partie F
Plan : fixes .1–.49 ; pool .50–.150 ; bail 8 h ; noms srv, intranet, imprimante. 169.254 → service DHCP, pool, câble. IP OK / nom KO → DNS.
