# Corrigé – Terminale S08

Fichier : `T08-integration-corrige.json`.

**Partie B** : on réserve `.1`–`.49` pour les adresses fixes et la passerelle ; le DHCP distribue à partir de `.50`.

**Partie C** : `IMP` `192.168.40.20/24`, passerelle `.40.1` ; `NAS` `192.168.40.30/24`, passerelle `.40.1`.

**Partie D** : les trois pings aboutissent. Si l'imprimante ne répond pas : 1) câble et voyant du port (`show ip interface brief`, `show interfaces status`) ; 2) VLAN du port (`show vlan brief`) ; 3) adresse et passerelle de l'imprimante.

**Partie E (réponses attendues)** : caméra : VLAN 40, `192.168.40.31`, passerelle `.40.1`, PoE (vérifier le budget), mot de passe changé, test : image visible depuis un poste, risque : mot de passe par défaut / accès depuis Internet ; ESP32 : VLAN 40, `192.168.40.40`, passerelle `.40.1`, alimentation par bloc 5 V, test : la température remonte, risque : réseau Wi-Fi peu protégé / absence de mise à jour.

**Partie F** : le plan d'adressage doit comporter les 4 équipements avec VLAN, adresse, emplacement ; le journal indique date, modification, auteur.

**Contrôles automatiques** : 5/5 verts sur le corrigé.
