# Corrigé – Terminale S06

Fichiers : `T06-wifi-corrige.json`, `T06-panne-corrige.json`.

**Partie A** : avant configuration, les portables ne se connectent pas (bornes non branchées) ou n'ont pas d'adresse.

**Partie B** : `Fa0/10` et `Fa0/11` sont en **access** car chaque borne simulée diffuse un seul SSID, donc un seul VLAN. Une borne réelle à plusieurs SSID serait sur un **trunk**.

**Partie C** : sous-interfaces `.10/.20/.30`, pools `PERSONNEL` et `INVITES`. On exclut `.1`–`.9` pour réserver les adresses des équipements (la passerelle ne doit pas être distribuée).

**Partie D** : SSID/clés comme indiqué. `LAP-PERS` : `192.168.20.x` ; `LAP-INV` : `192.168.30.x`.

**Partie E** : `INVITES-IN` : `deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255` ; `deny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255` ; `permit ip any any` ; `in` sur `gi0/0.30`. Les invités gardent l'accès à `192.168.30.1` (DHCP, passerelle).

**Partie F (pannes)** : 1) `LAP-PERS` : clé `Perso#Garcia27` (était `…26`) → pas de connexion ; 2) `SW1 Fa0/11` : `switchport access vlan 30` (était 20) → invités dans le VLAN du personnel ; 3) `R1 gi0/0.30` : `ip access-group INVITES-IN in` (retiré).

**Contrôles automatiques** : 6/6 verts sur les deux corrigés.
