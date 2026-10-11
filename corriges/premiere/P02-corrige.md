# Corrigé P02 – Remise à niveau et simulateur

## TP
- **Partie A** : équipements : SW1, PC1, PC2, SRV1 ; 2 câbles ; SRV1 = 192.168.10.100 ; PC2 non relié ; RAZ réseau = efface ce que les équipements ont appris (ARP, DHCP…).
- **Partie B** : câbler PC2 sur un port libre de SW1 ; `192.168.10.12/24` ; deux `ping` OK (fichier solution : `P02-decouverte-corrige.json`).
- **Partie C** : 4 trames ICMP par ping (2 sauts × requête + réponse) ; source de la 1re trame = 192.168.10.12 ; type 8 (requête) / type 0 (réponse) ; ARP : « qui a 192.168.10.100 ? » puis réponse.
- **Partie D** : exercices 1–12 : corrigés repliés dans la fiche.

## Points d'attention
- Les élèves qui n'arrivent pas à poser le câble : outil « Câble » non sélectionné.
- Les « trames de bruit » (ICMPv6, ARP Announcement) à ignorer avec le filtre `icmp`.
