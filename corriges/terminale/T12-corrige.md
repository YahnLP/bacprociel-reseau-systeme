# Corrigé – Terminale S12

Fichier : `T12-remplacement-corrige.json`.

**Partie A** : avant restauration, `PC-CPT` n'a pas d'adresse (`169.254…` ou aucune) ; `PC-COM` ne joint pas le serveur ; `show vlan brief` : tous les ports en VLAN 1, VLAN 10/20/30 absents.

**Partie B** : la configuration dépend du **numéro de port** (VLAN d'accès, trunk vers le routeur).

**Partie C** : après collage, `write memory`, et `ipconfig /renew` sur `PC-CPT`, les VLAN et le trunk sont en place.

**Partie D** : T1 à T5 réussis.

**Partie E (exemple)** : *Contexte* : PME Delmas, 30/11/2026, 8 h 40, M. Delmas. *Symptôme* : plus aucun accès au réseau depuis le matin. *Diagnostic* : switch éteint (voyants éteints), poste sans adresse, routeur et serveur OK. *Cause* : bloc d'alimentation du switch défaillant. *Action* : switch de remplacement installé aux mêmes ports ; configuration restaurée depuis la sauvegarde du 12/10 ; `write memory`. *Résultat* : 5 tests OK, utilisateur a confirmé. *À suivre* : programmer une sauvegarde mensuelle, prévoir un switch de secours. *Durée* : 55 min.

**Partie F** : phrases attendues — symptôme (PC-COM n'accède pas à l'intranet), tests (ping passerelle KO / OK…), modifications (switch restauré, rien d'autre), demande (avis sur le routeur/DNS).

**Contrôles automatiques** : 5/5 verts sur le corrigé.
