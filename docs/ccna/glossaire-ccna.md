# 📖 Glossaire CCNA (français – anglais)

*L'examen est en anglais : apprends chaque notion avec **son nom anglais**. La colonne « Module » indique où elle est travaillée.*

## 🌐 Bases des réseaux

| Français | Anglais | Définition simple | Module |
|---|---|---|---|
| Commutateur | *switch* | Relie les appareils d'un réseau local d'après les MAC | 1-01 |
| Routeur | *router* | Relie des réseaux d'après les adresses IP | 1-01 |
| Pare-feu | *firewall* | Autorise ou bloque le trafic selon des règles | 1-01 |
| Alimentation par Ethernet | *PoE (Power over Ethernet)* | Courant fourni par le câble réseau | 1-01 |
| Point d'accès | *access point (AP)* | Donne le Wi-Fi | 1-01 |
| Contrôleur Wi-Fi | *WLC (Wireless LAN Controller)* | Gère toutes les bornes | 1-01 |
| Trois niveaux | *three-tier* | Accès, distribution, cœur | 1-01 |
| Deux niveaux | *collapsed core / two-tier* | Distribution et cœur fusionnés | 1-01 |
| Fibre monomode / multimode | *single-mode / multimode fiber* | Longue distance / courte distance | 1-02 |
| Incohérence de duplex | *duplex mismatch* | Un bout en full, l'autre en half | 1-02 |
| Poignée de main en 3 temps | *three-way handshake* | SYN, SYN-ACK, ACK : ouverture d'une connexion TCP | 1-03 |
| Hyperviseur | *hypervisor* | Logiciel qui fait tourner des VM | 1-03 |
| Masque de sous-réseau à longueur variable | *VLSM* | Sous-réseaux de tailles différentes | 1-04 |
| Adresse privée | *private address (RFC 1918)* | 10/8, 172.16/12, 192.168/16 | 1-04 |
| Adresse de diffusion | *broadcast address* | Dernière adresse d'un réseau | 1-04 |
| Lien local | *link-local* | Adresse IPv6 `fe80::/10` valable sur le lien | 1-05 |
| Multidiffusion | *multicast* | Envoi vers un groupe | 1-05 |
| Identifiant EUI-64 | *EUI-64* | Identifiant d'interface construit avec la MAC | 1-05 |

## 🔀 Accès réseau

| Français | Anglais | Définition simple | Module |
|---|---|---|---|
| Table d'adresses MAC | *MAC address table* | Associe chaque MAC à un port | 2-01 |
| Apprentissage / inondation / vieillissement | *learning / flooding / aging* | Les trois comportements du switch | 2-01 |
| Réseau local virtuel | *VLAN* | Découpage logique d'un switch | 2-01 |
| Lien agrégé / tronc | *trunk* | Lien qui transporte plusieurs VLAN | 2-02 |
| VLAN natif | *native VLAN* | VLAN envoyé sans étiquette sur un trunk | 2-02 |
| Routeur sur un bras | *router-on-a-stick* | Une interface, une sous-interface par VLAN | 2-02 |
| Protocole de découverte Cisco | *CDP* | Découvre les voisins Cisco | 2-03 |
| Protocole de découverte standard | *LLDP* | Découvre les voisins (IEEE 802.1AB) | 2-03 |
| Agrégation de liens | *EtherChannel / LACP* | Regroupe plusieurs liens en un | 2-03 |
| Pont racine | *root bridge* | Switch central de l'arbre STP | 2-04 |
| Tempête de diffusion | *broadcast storm* | Diffusion qui tourne en boucle | 2-04 |
| Message STP | *BPDU* | Trame échangée entre switchs STP | 2-04 |
| Port rapide | *PortFast* | Port d'accès qui passe tout de suite en forwarding | 2-04 |
| Protection BPDU | *BPDU guard* | Coupe un port d'accès qui reçoit un BPDU | 2-04 |
| Tunnel contrôleur-borne | *CAPWAP* | Protocole entre AP et WLC | 2-05 |
| Authentification, autorisation, comptabilité | *AAA* | Qui es-tu, que peux-tu faire, qu'as-tu fait | 2-05 |
