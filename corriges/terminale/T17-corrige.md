# Corrigé – Terminale S17

Fichier : `T17-sujet-corrige.json`.

**Plan d'adressage attendu** : `172.16.11.0/24` (Bureaux, VLAN 11), passerelle `.1`, DHCP à partir de `.100`, imprimante `172.16.11.20` ; `172.16.21.0/24` (Visiteurs, VLAN 21), passerelle `.1`, DHCP à partir de `.100`.

**Câblage** : identique à S15 (`R1 gi0/0` → FAI `gi0/2` ; `R1 gi0/1` → `SW1 Fa0/24` ; `PC-SECR` Fa0/1 ; `PC-DENT` Fa0/2 ; `IMP` Fa0/3 ; `AP1` Fa0/10).

**Switch** : VLAN 11 `BUREAUX`, 21 `VISITEURS` ; Fa0/1-3 en VLAN 11 ; Fa0/10 en VLAN 21 ; Fa0/24 trunk ; `enable secret Pasquier#2027`. **Routeur** : sous-interfaces `gi0/1.11` / `.21`, DHCP, route par défaut, NAT en surcharge, ACL `VISITEURS-IN`. **Wi-Fi** : `PASQUIER-VISITEURS`, clé `Visiteurs#2027`.

**Contrôles automatiques** : 8/8 verts.
