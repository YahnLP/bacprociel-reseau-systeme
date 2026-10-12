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

## 🧭 Routage

| Français | Anglais | Définition simple | Module |
|---|---|---|---|
| Distance administrative | *administrative distance (AD)* | Fiabilité d'une source de route : connecté 0, statique 1, OSPF 110 | 3-01 |
| Plus long préfixe | *longest prefix match* | La route la plus précise gagne | 3-01 |
| Passerelle de dernier recours | *gateway of last resort* | La route par défaut | 3-01 |
| Route flottante | *floating static route* | Route de secours à distance plus élevée | 3-02 |
| État de liens | *link-state* | Famille de protocoles dont OSPF fait partie | 3-03 |
| Routeur désigné | *DR / BDR* | Routeurs élus sur un réseau broadcast OSPF | 3-03 |
| Identifiant du routeur | *router-id* | Nom d'un routeur OSPF | 3-03 |
| Interface passive | *passive interface* | Interface sans Hello OSPF | 3-03 |
| Redondance du premier saut | *FHRP (HSRP, VRRP, GLBP)* | Passerelle virtuelle partagée | 3-04 |

## 🌍 Services IP

| Français | Anglais | Définition simple | Module |
|---|---|---|---|
| Traduction d'adresses | *NAT / PAT (overload)* | Remplace les adresses privées par une adresse publique | 4-01 |
| Relais DHCP | *DHCP relay (ip helper-address)* | Fait traverser le DHCP vers un autre réseau | 4-02 |
| Bail | *lease* | Durée d'une adresse attribuée par DHCP | 4-02 |
| Strate | *stratum* | Distance à l'horloge de référence NTP | 4-03 |
| Gestionnaire / agent | *manager / agent (SNMP)* | Qui interroge / qui répond | 4-03 |
| Journalisation | *syslog* | Envoi des messages des équipements à un serveur | 4-03 |
| Qualité de service | *QoS (DSCP, policing, shaping)* | Prioriser le trafic sensible | 4-04 |
| Gigue | *jitter* | Variation du délai | 4-04 |
| Transfert de fichier simple | *TFTP* | UDP 69, sans authentification | 4-05 |

## 🔐 Sécurité

| Français | Anglais | Définition simple | Module |
|---|---|---|---|
| Confidentialité, intégrité, disponibilité | *CIA triad* | Les trois objectifs de la sécurité | 5-01 |
| Authentification multifacteur | *MFA* | Plusieurs preuves d'identité | 5-01 |
| Authentification, autorisation, traçabilité | *AAA* | Qui, quels droits, quelles actions | 5-02 |
| Liste de contrôle d'accès | *ACL (access control list)* | Règles permit/deny sur le trafic | 5-03 |
| Masque inverse | *wildcard mask* | Bits « libres » dans une ACL | 5-03 |
| Sécurité des ports | *port security* | Limite les adresses MAC par port | 5-04 |
| Espionnage DHCP | *DHCP snooping* | Bloque les faux serveurs DHCP | 5-04 |
| Inspection ARP dynamique | *DAI* | Bloque l'usurpation ARP | 5-04 |
| Réseau privé virtuel | *VPN / IPsec* | Tunnel chiffré entre deux sites | 5-05 |
| Clé pré-partagée | *PSK (pre-shared key)* | Secret commun à deux pairs | 5-05 |
| Authentification par port | *802.1X* | Contrôle d'accès réseau par identifiant | 5-06 |

## 🤖 Automatisation

| Français | Anglais | Définition simple | Module |
|---|---|---|---|
| Réseau défini par logiciel | *SDN* | Contrôle centralisé du réseau | 6-01 |
| Plan de contrôle / de données | *control plane / data plane* | Décide / transfère | 6-01 |
| Interface de programmation | *API (REST)* | Dialogue entre programmes en HTTP | 6-02 |
| Format d'échange | *JSON* | Texte clé/valeur structuré | 6-02 |
| Infrastructure as code | *IaC (Terraform)* | Décrire l'infrastructure dans des fichiers | 6-03 |
| Gestion de configuration | *Ansible (playbook, YAML)* | Pousser une configuration sans agent | 6-03 |
