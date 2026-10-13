# 🚀 Parcours CCNA

*Parcours complémentaire – non exigé à l'épreuve E31.*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Ce parcours est **complémentaire**. Il est fait pour les élèves qui **terminent les TP avant les autres** et veulent utiliser leur temps utilement : il prépare au **CCNA 200-301** (certification réseau de Cisco, reconnue dans le métier). Tu avances **à ton rythme**, sans attendre la classe.

## 🎯 Comment ça marche

1. **Quand ?** Dès que tu as terminé ton TP de la séance et fait valider tes points de contrôle par ton enseignant.
2. **Quoi ?** Des **modules** courts. Chaque module contient un **cours**, un **TP dans le simulateur réseau** (fichier `.json` à ouvrir hors ligne) et un **quiz**.
3. **Où j'en suis ?** Coche tes modules sur la [feuille de route](feuille-de-route.md).
4. **Le vocabulaire** est en français, avec les **termes anglais** de l'examen à côté : l'examen CCNA est en anglais. Retrouve-les dans le [glossaire CCNA](glossaire-ccna.md).

> [!TIP]
> Le simulateur sert **tout le temps** : on n'apprend pas le CCNA en lisant. Pour chaque notion, tu tapes les commandes et tu **vérifies** ce que le réseau fait.

## 🗺️ Le programme (6 domaines de l'examen)

| Domaine | Poids à l'examen | Statut ici |
|---|---|---|
| **1 – Network Fundamentals** (bases des réseaux) | 20 % | ✅ disponible |
| **2 – Network Access** (commutation, VLAN, STP) | 20 % | ✅ disponible |
| **3 – IP Connectivity** (routage, OSPF) | 25 % | ✅ disponible |
| **4 – IP Services** (NAT, DHCP, NTP, SSH…) | 10 % | ✅ disponible |
| **5 – Security Fundamentals** (ACL, sécurité L2, VPN) | 15 % | ✅ disponible |
| **6 – Automation and Programmability** (API, JSON, Ansible) | 10 % | ✅ disponible |
| **7 – Dépannage** (méthode, transversal) | – | ✅ disponible : chaque module technique comporte une section 🔧 « Dépanner » |

## 📚 Modules disponibles

### Domaine 1 – Network Fundamentals

| Module | Contenu | TP simulateur |
|---|---|---|
| [1-01 · Équipements et architectures](1-01-equipements-architectures/01-cours.md) | Rôle des équipements, 2 et 3 niveaux, SOHO, WAN, cloud | [🖥️ explorer un réseau à 3 niveaux](1-01-equipements-architectures/02-tp.md) |
| [1-02 · Interfaces, câbles et diagnostic](1-02-interfaces-diagnostic/01-cours.md) | Cuivre/fibre, vitesse, duplex, erreurs | [🖥️ lire l'état des interfaces](1-02-interfaces-diagnostic/02-tp.md) |
| [1-03 · TCP, UDP et outils des postes](1-03-tcp-udp-postes/01-cours.md) | TCP/UDP, ports, vérifier l'IP sous Windows/Linux/macOS, virtualisation | exercices |
| [1-04 · IPv4 : sous-réseaux et VLSM](1-04-ipv4-vlsm/01-cours.md) | Découpage, VLSM, adresses privées | [🖥️ plan VLSM](1-04-ipv4-vlsm/02-tp.md) |
| [1-05 · IPv6](1-05-ipv6/01-cours.md) | Écriture, types d'adresses, EUI-64, routage statique | [🖥️ réseau IPv6](1-05-ipv6/02-tp.md) |
| [1-06 · Sans fil : les bases](1-06-sans-fil-bases/01-cours.md) | Canaux, SSID, chiffrement | exercices |

### Domaine 2 – Network Access

| Module | Contenu | TP simulateur |
|---|---|---|
| [2-01 · Commutation, table MAC et VLAN](2-01-commutation-vlan/01-cours.md) | Apprentissage MAC, flooding, VLAN, VLAN voix | [🖥️ table MAC et VLAN](2-01-commutation-vlan/02-tp.md) |
| [2-02 · Trunk, VLAN natif et inter-VLAN](2-02-trunk-inter-vlan/01-cours.md) | 802.1Q, VLAN natif, routeur sur un bras | [🖥️ deux switchs, un routeur](2-02-trunk-inter-vlan/02-tp.md) |
| [2-03 · CDP, LLDP et EtherChannel](2-03-lldp-etherchannel/01-cours.md) | Découverte de voisins, LACP | [🖥️ regrouper deux liens](2-03-lldp-etherchannel/02-tp.md) |
| [2-04 · STP et Rapid PVST+](2-04-stp/01-cours.md) | Pont racine, rôles et états, PortFast, BPDU guard | [🖥️ choisir le pont racine](2-04-stp/02-tp.md) |
| [2-05 · Sans fil Cisco et gestion des équipements](2-05-sans-fil-cisco-gestion/01-cours.md) | WLC, modes d'AP, SSH, RADIUS/TACACS+ | exercices |

### Domaine 3 – IP Connectivity

| Module | Contenu | TP simulateur |
|---|---|---|
| [3-01 · Table de routage et décision de transfert](3-01-table-routage/01-cours.md) | Codes, distance administrative, métrique, plus long préfixe | [🖥️ lire trois tables de routage](3-01-table-routage/02-tp.md) |
| [3-02 · Routage statique IPv4 et IPv6](3-02-routage-statique/01-cours.md) | Réseau, hôte, défaut, route flottante | [🖥️ routes et secours](3-02-routage-statique/02-tp.md) |
| [3-03 · OSPFv2 mono-zone](3-03-ospf/01-cours.md) | Voisins, DR/BDR, router-id, coût | [🖥️ OSPF sur trois routeurs](3-03-ospf/02-tp.md) |
| [3-04 · Redondance du premier saut](3-04-redondance-premier-saut/01-cours.md) | HSRP, VRRP, GLBP | cours seul (non simulé) |

### Domaine 4 – IP Services

| Module | Contenu | TP simulateur |
|---|---|---|
| [4-01 · NAT et PAT](4-01-nat/01-cours.md) | Statique, dynamique, surcharge | [🖥️ PAT sur un routeur de bordure](4-01-nat/02-tp.md) |
| [4-02 · DHCP, relais et DNS](4-02-dhcp-dns/01-cours.md) | DORA, `ip helper-address`, enregistrements | [🖥️ serveur DHCP distant](4-02-dhcp-dns/02-tp.md) |
| [4-03 · NTP, SNMP et syslog](4-03-ntp-snmp-syslog/01-cours.md) | Heure commune, supervision, gravités | [🖥️ syslog et SNMP](4-03-ntp-snmp-syslog/02-tp.md) (NTP non simulé) |
| [4-04 · QoS](4-04-qos/01-cours.md) | DSCP, classification, priorité, policing/shaping | [🖥️ priorité à la voix](4-04-qos/02-tp.md) |
| [4-05 · SSH, TFTP et FTP](4-05-ssh-tftp/01-cours.md) | SSH complet, transferts, SFTP | [🖥️ sécuriser l'accès distant](4-05-ssh-tftp/02-tp.md) |

### Domaine 5 – Security Fundamentals

| Module | Contenu | TP simulateur |
|---|---|---|
| [5-01 · Concepts de sécurité](5-01-concepts-securite/01-cours.md) | Menaces, attaques, CIA, mots de passe, MFA | exercices |
| [5-02 · Accès aux équipements et AAA](5-02-acces-equipements-aaa/01-cours.md) | enable secret, bannière, utilisateurs locaux, AAA | [🖥️ durcir un switch](5-02-acces-equipements-aaa/02-tp.md) |
| [5-03 · Listes de contrôle d'accès (ACL)](5-03-acl/01-cours.md) | Standard, étendue, wildcard, placement | [🖥️ filtrer vers un serveur](5-03-acl/02-tp.md) |
| [5-04 · Sécurité de couche 2](5-04-securite-couche2/01-cours.md) | Port-security, DHCP snooping, DAI | [🖥️ port-security](5-04-securite-couche2/02-tp.md) (snooping/DAI via 🧊) |
| [5-05 · VPN IPsec](5-05-vpn-ipsec/01-cours.md) | IKE, ESP, tunnel site à site | [🖥️ relier deux sites](5-05-vpn-ipsec/02-tp.md) |
| [5-06 · Sécurité du Wi-Fi](5-06-securite-wifi/01-cours.md) | WPA2/WPA3, PSK, 802.1X | cours + 🧊 |

### Domaine 6 – Automation and Programmability

| Module | Contenu | TP |
|---|---|---|
| [6-01 · Automatisation et contrôleurs](6-01-automatisation-controleurs/01-cours.md) | SDN, plans, réseaux pilotés par contrôleur | cours + 🧊 |
| [6-02 · API REST et JSON](6-02-api-rest-json/01-cours.md) | REST, CRUD, JSON, mini-TP Python | exercice Python |
| [6-03 · Ansible et Terraform](6-03-ansible-terraform/01-cours.md) | Gestion de configuration, IaC | cours seul |

### Domaine 7 – Dépannage (transversal)

| Module | Contenu | TP simulateur |
|---|---|---|
| [7-01 · Dépanner un réseau](7-01-depannage-reseau/01-cours.md) | Méthode, échelle du ping, lecture des erreurs, fiche réflexe, journal de dépannage | [🖥️ réseau en panne](7-01-depannage-reseau/02-tp.md) |

### 📝 Examen blanc

[Examen blanc CCNA](examen-blanc/01-examen.md) : 43 questions sur les 6 domaines, avec corrigé.

> [!TIP]
> Pour les services et les serveurs (web, FTP, NAS, Active Directory), voir le [parcours serveurs sur VirtualBox](../serveurs/README.md), qui complète ce parcours.

## 🧭 Sources utilisées

Le plan suit le programme officiel de l'examen :
[page de l'examen CCNA 200-301 (Cisco)](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccna.html) et [liste des sujets v1.1 (Cisco Learning Network)](https://learningnetwork.cisco.com/s/ccna-v1-1-exam-topics), complétés par des synthèses de la liste des sujets ([Computingforgeeks](https://computingforgeeks.com/ccna-exam-topics/), [Open Exam Prep](https://open-exam-prep.com/study-guides/ccna/introduction/exam-domains-and-weights)). Les cours et TP sont **originaux**, écrits pour ce site et testés dans le simulateur.

> [!NOTE]
> Le simulateur reproduit la plupart des commandes Cisco IOS du programme, pas toutes (par exemple, il n'accepte pas le filtre `| include`, ni HSRP, NTP ou TFTP). Quand une commande est à connaître pour l'examen mais **n'existe pas dans le simulateur**, c'est indiqué dans le cours, avec une **alternative sur Cisco Packet Tracer** (encadré 🧊).

## 🧊 Cisco Packet Tracer

*Packet Tracer* est le simulateur gratuit de Cisco Networking Academy ([netacad.com](https://www.netacad.com)). Il complète le simulateur du site pour ce qu'il ne fait pas (HSRP, NTP, TFTP, canaux Wi-Fi…). Les encadrés 🧊 « Alternative avec Cisco Packet Tracer » donnent un petit scénario à monter toi-même. Les fonctions disponibles dépendent de la **version** installée : vérifie avec ton enseignant.
