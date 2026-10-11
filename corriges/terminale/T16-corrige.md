# Corrigé – Terminale S16

Fichiers : `T16-chantier-corrige.json`.

**Cause 1** : `SW1 Fa0/3` en VLAN 20 → `switchport access vlan 10` (l'imprimante, adresse `192.168.10.20`, est isolée du VLAN Soins). **Cause 2** : clé Wi-Fi du portable `Patient#2027` → `Patients#2027` (le portable n'est pas associé à la borne). **Cause 3** : `access-list 1 permit 192.168.10.0 0.0.0.255` ne couvre plus le VLAN 20 → patients sans Internet ; remplacer par `permit 192.168.0.0 0.0.255.255`.

**Ordre de découverte attendu** : l'imprimante d'abord (aisée), puis le Wi-Fi (pas d'adresse), puis Internet des patients (une fois connectés).

**Compte rendu attendu** : 3 causes, 3 actions, 6 tests conformes, sauvegarde, recommandations (revoir la liste d'accès NAT, contrôler les ports après intervention).

**Contrôles automatiques** : 8/8 verts.
