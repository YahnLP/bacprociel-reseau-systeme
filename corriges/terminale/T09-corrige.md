# Corrigé – Terminale S09

Fichier : `T09-acces-corrige.json`.

**Partie A** : Internet fonctionne (NAT en surcharge) ; depuis `DISTANT`, le port 8080 ne répond pas ; telnet fonctionne et le mot de passe y est transmis en clair (visible dans une capture).

**Partie B** : `ip domain-name`, `username tech privilege 15 secret …`, `crypto key generate rsa modulus 1024`, `ip ssh version 2`, `line vty 0 4` + `transport input ssh` + `login local`, `write memory`. `login local` : chaque technicien utilise **son** compte.

**Partie C** : `ip nat inside source static tcp 192.168.1.10 80 203.0.113.3 8080`. Le port 80 de l'adresse WAN **n'est pas** redirigé : le test échoue, c'est normal.

**Partie D (réponses attendues)** : tout Internet ; fuite possible d'informations ; protections : authentification sur le site, HTTPS, mises à jour, filtrage par adresse source, ou VPN à la place ; bureau à distance : **jamais** exposé directement (attaques automatiques) → VPN.

**Partie F** : la fiche doit comporter une autorisation écrite, un compte nominatif, un VPN ou SSH justifié, une durée d'une semaine, la suppression du compte à la fin, et une trace dans le journal.

**Contrôles automatiques** : 6/6 verts sur le corrigé (le refus de telnet n'est vérifié que par la configuration).
