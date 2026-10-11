# Corrigé – Terminale S15

Fichiers : `T15-chantier-corrige.json`.

**Plan d'adressage attendu** : `192.168.10.0/24` (Soins), passerelle `.1`, DHCP à partir de `.50` (exclusion `.1`–`.49`), imprimante `192.168.10.20` ; `192.168.20.0/24` (Patients), passerelle `.1`, DHCP à partir de `.10` ; WAN `203.0.113.3/29` (passerelle FAI `203.0.113.2`).

**Câblage** : `R1 gi0/0` → FAI `gi0/2` ; `R1 gi0/1` → `SW1 Fa0/24` ; `PC-SECR` Fa0/1 ; `PC-DENT` Fa0/2 ; `IMP` Fa0/3 ; `AP1` Fa0/10.

**Switch** : VLAN 10 `SOINS`, 20 `PATIENTS` ; Fa0/1-3 VLAN 10 ; Fa0/10 VLAN 20 ; Fa0/24 trunk ; `enable secret` ; `write memory`.

**Routeur** : `gi0/0` WAN avec `ip nat outside` ; sous-interfaces `gi0/1.10` / `.20` ; DHCP (`dns-server 198.51.100.53`) ; route par défaut vers `203.0.113.2` ; NAT en surcharge ; ACL `PATIENTS-IN` (autorise UDP 68→67, interdit le VLAN 10, autorise le reste) posée `in` sur `gi0/1.20` ; `write memory`.

**Wi-Fi** : SSID `VIDAL-PATIENTS`, clé `Patients#2027`, WPA2.

**Contrôles automatiques** : 8/8 verts.
