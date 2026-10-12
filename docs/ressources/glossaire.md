# 📖 Glossaire

*Les mots du métier, classés par thème. La colonne « Vu en » indique la séance où le mot est travaillé. Utilise la recherche du site (en haut) pour retrouver un mot.*

## 🖥️ Matériel et systèmes

| Mot | Définition simple | Vu en |
|---|---|---|
| **Système d'exploitation (OS)** | Logiciel qui fait le lien entre les programmes et le matériel | Seconde S04 |
| **Pilote (driver)** | Logiciel qui permet d'utiliser un matériel précis | Seconde S04 |
| **Partition** | Compartiment d'un disque | Seconde S04 |
| **BIOS / UEFI** | Programme de la carte mère qui démarre l'ordinateur avant le système | Seconde S03 |
| **Carte mère** | Grande carte électronique qui relie tous les composants | Seconde S02 |
| **RAM** | Mémoire de travail rapide, vidée à l'extinction | Seconde S02 |
| **Distribution Linux** | Système complet construit autour du noyau Linux | Seconde S05 |
| **apt** | Gestionnaire de paquets de Debian / Ubuntu | Seconde S05 |
| **Terminal** | Fenêtre où l'on tape des commandes | Seconde S06 |
| **Prompt** | Début de ligne : utilisateur et dossier courant | Seconde S06 |
| **Chemin absolu / relatif** | Adresse d'un fichier depuis la racine / depuis ici | Seconde S06 |
| **Service** | Programme qui tourne en arrière-plan et répond à des demandes (web, DHCP…) | Première S10 |
| **Serveur / client** | Le serveur offre un service ; le client le demande | Seconde S08 |

## 🔌 Câblage et mesures

| Mot | Définition simple | Vu en |
|---|---|---|
| **RJ45** | Connecteur à 8 contacts des câbles réseau cuivre | Seconde S09 |
| **Paire torsadée** | Câble cuivre dont les fils sont torsadés deux à deux pour limiter les parasites | Seconde S09 |
| **T568B** | Ordre normalisé des couleurs de fils dans un connecteur RJ45 | Seconde S09 |
| **Câble droit / croisé** | Droit : relie deux types d'équipements différents ; croisé : deux équipements semblables | Seconde S09 |
| **Cartographie (câble)** | Test qui vérifie que chaque fil arrive au bon contact | Terminale S04 |
| **Panneau de brassage** | Panneau où arrivent les câbles des prises murales, reliés au switch par des cordons | Seconde S10 |
| **Brassage** | Relier une prise à un port de switch avec un cordon | Seconde S10 |
| **Baie** | Armoire normalisée qui accueille les équipements réseau | Seconde S10 |
| **Fibre optique** | Câble qui transporte la lumière : longues distances, insensible aux parasites | Première S13 |
| **Atténuation (dB)** | Perte de signal le long d'un câble | Terminale S04 |
| **PoE** | Alimentation électrique d'un appareil par le câble réseau | Terminale S08 |
| **ESD** | Décharge d'électricité statique qui peut abîmer un composant | Terminale S03 |
| **AIPR** | Autorisation d'intervenir à proximité des réseaux | Terminale S03 |

## 🔢 Adresses et services de base

| Mot | Définition simple | Vu en |
|---|---|---|
| **Adresse IP** | Numéro d'un équipement sur un réseau IP | Seconde S11 |
| **Adresse MAC** | Identifiant matériel d'une carte réseau | Seconde S11 |
| **Masque de sous-réseau** | Indique quelle partie de l'adresse IP désigne le réseau (ex. /24) | Seconde S11 |
| **Passerelle** | Équipement (routeur) qui permet de sortir du réseau local | Seconde S11 |
| **Adresse privée / publique** | Privée : usage interne ; publique : visible sur Internet | Seconde S12 |
| **169.254.x.x** | Adresse que se donne un poste qui n'a pas reçu d'adresse DHCP | Seconde S12 |
| **DHCP** | Service qui distribue automatiquement les adresses IP | Seconde S12 |
| **Bail DHCP** | Durée pendant laquelle une adresse est prêtée à un poste | Seconde S12 |
| **Plage DHCP** | Ensemble d'adresses que le serveur DHCP peut distribuer | Seconde S12 |
| **Adresse réservée / fixe** | Adresse qui ne change pas, placée hors de la plage DHCP | Terminale S08 |
| **DNS** | Service qui traduit un nom (www.exemple.fr) en adresse IP | Seconde S13 |
| **NAT** | Le routeur remplace les adresses privées par son adresse publique | Seconde S13 |
| **Redirection de port** | Règle qui envoie un service interne vers l'extérieur par un port choisi | Terminale S09 |
| **ping** | Test pour savoir si une autre machine répond | Seconde S06 |
| **traceroute / tracert** | Affiche les routeurs traversés pour joindre une destination | Première S07 |
| **ipconfig / ip a** | Commandes qui affichent la configuration réseau d'un poste | Seconde S11 |

## 📶 Wi-Fi

| Mot | Définition simple | Vu en |
|---|---|---|
| **SSID** | Nom d'un réseau Wi-Fi | Seconde S14 |
| **WPA2 / WPA3** | Protocoles de sécurité du Wi-Fi (chiffrement) | Seconde S14 |
| **Clé Wi-Fi (PSK)** | Mot de passe partagé du réseau Wi-Fi | Seconde S14 |
| **Borne Wi-Fi (point d'accès)** | Équipement qui diffuse le Wi-Fi et se relie au réseau filaire | Seconde S14 |
| **2,4 GHz / 5 GHz** | Bandes de fréquences : 2,4 GHz porte plus loin, 5 GHz va plus vite | Terminale S06 |
| **Canal** | Fréquence utilisée par un réseau Wi-Fi ; des canaux voisins se gênent | Terminale S06 |
| **RADIUS** | Serveur qui vérifie les comptes des utilisateurs (Wi-Fi d'entreprise) | Terminale S06 |

## 🔍 Protocoles et couches

| Mot | Définition simple | Vu en |
|---|---|---|
| **Modèle OSI / TCP-IP** | Découpage en couches des fonctions d'un réseau | Première S03 |
| **Trame** | Unité de données de la couche 2 (Ethernet) | Première S03 |
| **Paquet** | Unité de données de la couche 3 (IP) | Première S03 |
| **Port (TCP/UDP)** | Numéro qui désigne le service visé sur une machine (80 = web) | Première S04 |
| **TCP / UDP** | TCP : fiable, avec connexion ; UDP : rapide, sans suivi | Première S04 |
| **ARP** | Protocole qui retrouve l'adresse MAC d'une adresse IP | Première S04 |
| **ICMP** | Protocole des messages de contrôle (le ping) | Première S04 |
| **HTTP / HTTPS** | Protocole du web / sa version chiffrée | Première S04 |
| **Capture (Wireshark)** | Enregistrement des trames qui circulent pour les analyser | Première S03 |
| **Broadcast (diffusion)** | Message envoyé à tous les équipements d'un réseau | Première S04 |

## 🔀 Switch, routeur, VLAN

| Mot | Définition simple | Vu en |
|---|---|---|
| **Switch (commutateur)** | Équipement qui relie les postes d'un réseau local | Seconde S08 |
| **Topologie** | Façon dont les équipements sont reliés : bus, anneau, **étoile** (la plus courante), maillé | Seconde S08 |
| **Routeur** | Équipement qui relie des réseaux différents | Première S07 |
| **Table MAC** | Liste des adresses MAC connues par le switch et leur port | Première S05 |
| **Sous-réseau** | Découpage d'un réseau IP en réseaux plus petits | Première S06 |
| **Notation CIDR (/24)** | Écriture du masque par le nombre de bits du réseau | Première S06 |
| **Route statique** | Chemin vers un réseau inscrit à la main dans un routeur | Première S07 |
| **Route par défaut** | Chemin utilisé quand aucune autre route ne convient | Première S07 |
| **VLAN** | Réseau virtuel : sépare des postes d'un même switch | Première S08 |
| **Port d'accès** | Port de switch qui appartient à un seul VLAN | Première S08 |
| **Trunk** | Lien qui transporte plusieurs VLAN étiquetés | Première S09 |
| **802.1Q (dot1Q)** | Norme d'étiquetage des VLAN sur un trunk | Première S09 |
| **Sous-interface** | Interface logique d'un routeur associée à un VLAN | Terminale S05 |
| **Switch de niveau 3** | Switch qui sait aussi router entre VLAN | Terminale S05 |
| **Interface VLAN (SVI)** | Interface logique d'un switch niveau 3 : passerelle d'un VLAN | Terminale S05 |
| **ACL** | Liste de règles qui autorise ou interdit des échanges | Première S14 |
| **Relais DHCP (helper-address)** | Fait suivre les demandes DHCP vers un serveur d'un autre réseau | Première S16 |

## 🛡️ Sécurité et accès à distance

| Mot | Définition simple | Vu en |
|---|---|---|
| **Mot de passe fort** | Long, difficile à deviner, propre à chaque service | Première S14 |
| **enable secret** | Mot de passe chiffré qui protège le mode privilégié d'un équipement Cisco | Première S14 |
| **SSH** | Connexion à distance chiffrée à une machine ou un équipement | Première S10 |
| **Telnet** | Connexion à distance non chiffrée : à éviter | Terminale S09 |
| **VPN** | Tunnel chiffré qui relie un poste distant au réseau de l'entreprise | Terminale S09 |
| **Pare-feu** | Équipement ou logiciel qui filtre les échanges réseau | Première S14 |
| **Télémaintenance** | Intervention sur un équipement à distance, avec autorisation | Terminale S09 |
| **Compte nominatif** | Compte propre à une personne, pour savoir qui fait quoi | Terminale S09 |

## 🧰 Exploitation et dépannage

| Mot | Définition simple | Vu en |
|---|---|---|
| **running-config** | Configuration en cours d'un équipement (perdue au redémarrage) | Première S05 |
| **startup-config** | Configuration enregistrée (conservée au redémarrage) | Première S05 |
| **write memory** | Commande qui enregistre la configuration en cours | Première S05 |
| **Sauvegarde 3-2-1** | 3 copies, sur 2 supports, dont 1 hors site | Terminale S07 |
| **Journal des modifications** | Liste datée de ce qui a été changé sur un réseau | Terminale S07 |
| **SNMP** | Protocole qui permet d'interroger un équipement (état, nom…) | Terminale S10 |
| **Supervision** | Surveillance continue des équipements avec alertes | Terminale S10 |
| **Syslog (journaux)** | Messages d'événements envoyés par un équipement | Terminale S10 |
| **Ticket** | Fiche de suivi d'un incident (symptôme, cause, action) | Terminale S10 |
| **Échelle des tests** | Ordre de tests du plus proche au plus lointain pour localiser une panne | Terminale S11 |
| **Compte rendu d'intervention** | Document qui retrace le problème, la cause, l'action et le résultat | Terminale S12 |
| **Escalade** | Passer la main à un niveau supérieur (responsable, constructeur) | Terminale S12 |
| **Recette** | Série de tests qui prouve que l'installation répond au besoin | Première S18 |
| **Réserve** | Écart mineur noté à la réception, avec une date de correction | Terminale S13 |
| **Procès-verbal de réception** | Document signé qui valide la réception d'une installation | Terminale S13 |
| **Plan d'adressage** | Tableau des réseaux, plages et adresses fixes d'une installation | Première S16 |
| **PFMP** | Période de formation en milieu professionnel | Seconde S01 |
