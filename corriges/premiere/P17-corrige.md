# Corrigé – Première S17 (mise en service)

Installation : `P16-projet-corrige.json` (identique au résultat attendu).

**Commandes switch** : voir `00-plan-de-reference.md` et l'aide-mémoire (VLAN 10/20/30 ; `interface range fa0/1-8` access 10, `fa0/9-16` 20, `fa0/17-24` 30 ; `enable secret Archi#2027` ; bannière ; ports libres `shutdown` ; `write memory`).

**Routeur** : gi0/0 192.168.50.1/27 + helper 192.168.50.34 ; gi0/1 192.168.50.33/27 ; gi0/2 192.168.50.65/26 + helper ; ACL `INVITES-IN` (DHCP, DNS, web, deny) en entrée sur gi0/2.

**Serveur** : 192.168.50.34/27, passerelle .33, DNS .34 ; pools Direction .10-.30, Atelier .40-.62, Invités .70-.120 ; exclusions des adresses de passerelles/fixes ; DNS `intranet` et `imprimante` ; web démarré.

**Wi-Fi** : AP1 SSID `ARCHI-INVITES`, WPA2, clé `Invites#2027` ; portable avec le même SSID et la même clé.

**Questions** : 9 câbles ; pas de relais côté Atelier (serveur dans ce réseau) ; 169.254.x.x → le DHCP n'a pas répondu : (1) port/VLAN ou relais, (2) pool/serveur arrêté ; sans règle DHCP dans l'ACL → invité sans adresse.

**Contrôles automatiques** : les 9 tests du jalon sont verts sur le corrigé (vérifié par le moteur du simulateur).
