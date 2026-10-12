# 📑 Cahier des charges – Projet A2 « ArchiPlus »

*Bac Pro CIEL – Première – E31 – S15 à S19 – équipe de **2 ou 3***

## 1. Le client

**ArchiPlus** est un petit cabinet d'architecture de **12 personnes**. Il déménage dans de nouveaux locaux et te confie la **mise en place complète du réseau**. Le gérant, M. Durand, résume ses attentes :

> *« Je veux que la Direction et l'atelier travaillent ensemble sans se gêner, que mes clients aient du Wi-Fi sans toucher à nos dossiers, et que tout soit documenté pour que le prochain technicien s'y retrouve. »*

## 2. Les trois services

| Service | Personnes | Machines | Besoin |
|---|---|---|---|
| **Direction** | 3 | 1 poste fixe (+ portables) | Accès au serveur, à l'atelier |
| **Atelier** | 7 | 2 postes, 1 imprimante | Accès au serveur ; imprimante à **adresse fixe** |
| **Invités** | clients, visiteurs | Wi-Fi uniquement | Voir le **site de présentation** du cabinet, **rien d'autre** |

Le **serveur** (Linux) héberge : DHCP (pour les trois services), DNS (`intranet.archiplus.local`, `imprimante.archiplus.local`) et le **site web** du cabinet.

## 3. Matériel disponible

| Équipement | Quantité | Remarque |
|---|---|---|
| Switch administrable (Cisco 2960, 24 ports) | 1 | |
| Routeur (Cisco 2911, **3 interfaces Gigabit**) | 1 | une « patte » par service |
| Serveur Linux | 1 | |
| Borne Wi-Fi | 1 | |
| Postes, imprimante, portable de test | selon plan | |

## 4. Exigences

### 4.1 Réseau

- **E1** – Trois **VLAN** : Direction (10), Atelier (20), Invités (30).
- **E2** – Trois **sous-réseaux** distincts à partir de **192.168.50.0/24** (à découper et justifier : tailles de blocs suffisantes, **sans gaspiller**).
- **E3** – Le **routeur** relie les trois services (une interface par service).
- **E4** – Les **invités** n'accèdent **qu'au site web et au DNS** du serveur ; **jamais** à la Direction, à l'Atelier ni à l'imprimante.

### 4.2 Services

- **E5** – DHCP centralisé sur le serveur, **un pool par service** (adresses fixes réservées en dehors de la plage).
- **E6** – DNS : les noms `intranet` et `imprimante` fonctionnent depuis la Direction.
- **E7** – Site web du cabinet accessible **par son nom**.
- **E8** – **Wi-Fi invité** : SSID `ARCHI-INVITES`, WPA2, clé robuste.

### 4.3 Sécurité et exploitation

- **E9** – Switch et routeur : **mot de passe chiffré**, **bannière**, **ports libres coupés**.
- **E10** – **Configurations sauvegardées** (`write memory` + copie du texte dans le dossier).
- **E11** – Un **dossier technique** : schéma, plan d'adressage, plan de VLAN, tableau de câblage, configurations.
- **E12** – Un **cahier de recette** : chaque exigence a un test, un résultat attendu et un résultat obtenu.

## 5. Contraintes

| Contrainte | Valeur |
|---|---|
| **Adresses** | Réseau privé 192.168.50.0/24 imposé |
| **Pas d'accès Internet** dans ce projet | (reporté à la Terminale) |
| **Délai** | 3 séances : étude, réalisation, recette |
| **Budget** | Aucun achat : le matériel ci-dessus suffit |

## 6. Livrables et évaluation

| Livrable | Séance | Compétence |
|---|---|---|
| Dossier d'étude (schéma, adressage, VLAN, câblage) | S16 | Préparation du projet |
| Maquette configurée et sauvegardée | S17 | C09 – Installer |
| Cahier de recette + dossier technique + dépannage | S18 | C06 – Valider la conformité · C10 – Exploiter |
| **Soutenance** (démonstration + panne en direct) | S19 | C06 · C09 · C10 |

## 7. Rôles dans l'équipe

| Rôle | Mission | Nom |
|---|---|---|
| **Chef de projet** | Planning, décisions, lien avec l'enseignant | |
| **Technicien réseau** | Switch, routeur, VLAN | |
| **Technicien services** | Serveur (DHCP, DNS, web), Wi-Fi | |

> [!IMPORTANT]
> Les rôles **tournent** : tout le monde doit savoir **tout expliquer** à la soutenance.

## 8. Mes questions au client

*(à compléter pendant la séance, à poser à l'enseignant)*

1. ______________________________________________
2. ______________________________________________
3. ______________________________________________
