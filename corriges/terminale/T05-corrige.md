# Corrigé – Terminale S05

Fichiers : `T05-intervlan-corrige.json`, `T05-switch-niveau3-corrige.json`, `T05-panne-corrige.json`.

**Partie A** : avant config, le `PC-CPT` ne joint pas le serveur (pas de routeur, VLAN non créés) ; `PC-COM` ne joint pas `192.168.20.1`.

**Partie B** : trunks Fa0/24 (SW1), Gi0/1 (SW1 et SW2). Les VLAN doivent exister sur **tous** les switches traversés (sinon le trunk n'étiquette/transporte pas le VLAN inconnu).

**Partie C** : `Gi0/0.10`, `.20`, `.30` avec `encapsulation dot1Q 10/20/30` et les passerelles .1 ; trois lignes `C` dans `show ip route`.

**Partie D** : ACL `COMMERCIAL-IN` : `deny ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255` ; `permit ip any any` ; appliquée `in` sur `Gi0/0.20`. Le ping compta → commercial échoue car la **réponse** est bloquée (ACL sans état).

**Partie E** : `CORE` : `ip routing`, VLAN 10/20/30, SVI avec .1, trunk avec `switchport trunk encapsulation dot1q`. Pas de câble de retour vers un routeur ; passerelles = adresses des interfaces VLAN du switch.

**Partie F (pannes)** : 1) SW2 : `switchport trunk allowed vlan add 20` sur Gi0/1 (le VLAN 20 ne passait plus) ; 2) R1 : `interface gi0/0.30` → `encapsulation dot1Q 30` (était `3`) ; 3) SRV : passerelle `192.168.30.1` (était `.254`).

**Contrôles automatiques** : 6/6 verts sur le corrigé.
