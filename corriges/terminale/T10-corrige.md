# Corrigé – Terminale S10

Fichier : `T10-supervision-corrige.json`.

**Partie A** : pas de réponse (« timeout ») : SNMP n'est pas activé sur le switch.

**Partie B** : `snmp-server community supervision RO`, `snmp-server location …`, `snmp-server contact …`, `snmp-server host 192.168.1.5 version 2c supervision`, `snmp-server enable traps`, `logging host 192.168.1.5`, `logging trap informational`, `write memory`. `public` est une valeur par défaut **connue de tous**.

**Partie C** : `sysName` : `SW-IMPRIMERIE` ; `sysLocation` : `Atelier - baie 1` ; état des ports : `Fa0/1`, `Fa0/2`, `Fa0/3` en `up(1)` (SUP, PC-1, IMP).

**Partie D** : le port `Fa0/2` passe à `down(2)` ; `show logging` : `%LINK-3-UPDOWN: Interface FastEthernet0/2, changed state to down`.

**Partie E** : module `LINK` ; gravité 3 (erreur) ; événement : changement d'état (`UPDOWN`) ; interface `FastEthernet0/2`.

**Partie F (exemple de ticket 1)** : *Symptôme* : le poste PC-1 n'a plus de réseau ; *Cause* : câble débranché sur Fa0/2 (port `down`) ; *Action* : câble rebranché ; *Résultat* : port `up`, ping OK ; *Durée* : 5 min.

**Contrôles automatiques** : 5/5 verts sur le corrigé.
