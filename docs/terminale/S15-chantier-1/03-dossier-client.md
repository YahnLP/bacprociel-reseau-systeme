# 📄 Dossier client – Cabinet dentaire Vidal

*Terminale – E31 – S15 (chantier d'entraînement n°1)*

## 1. Contexte

Le **Dr Vidal** ouvre un cabinet dentaire. Il souhaite un **réseau fiable** pour le secrétariat et le cabinet de soins, une **imprimante partagée** et un **Wi-Fi pour ses patients**, qui ne doivent **pas** accéder à l'imprimante ni aux postes du cabinet.

## 2. Exigences du client

| N° | Exigence |
|---|---|
| E1 | Les postes du secrétariat et du cabinet reçoivent leur adresse **automatiquement** et accèdent à **Internet**. |
| E2 | L'imprimante est joignable par les postes du cabinet, avec une **adresse fixe**. |
| E3 | Les patients disposent d'un **Wi-Fi sécurisé** (WPA2) avec accès à Internet. |
| E4 | Les patients **ne voient pas** l'imprimante ni les postes. |
| E5 | La configuration est **sauvegardée** et **documentée**. |

## 3. Matériel et schéma (à câbler)

| Équipement | Rôle | Connexion |
|---|---|---|
| `R1` (routeur) | Passerelle, DHCP, NAT, filtrage | `gi0/0` → FAI `gi0/2` ; `gi0/1` → `SW1 Fa0/24` |
| `SW1` (switch 24 ports) | Distribution | – |
| `PC-SECR` | Poste du secrétariat | `SW1 Fa0/1` |
| `PC-DENT` | Poste du cabinet | `SW1 Fa0/2` |
| `IMP` | Imprimante | `SW1 Fa0/3` |
| `AP1` | Borne Wi-Fi | `SW1 Fa0/10` |
| `LAP-INV` | Portable d'un patient | Wi-Fi `VIDAL-PATIENTS` |

**Adresse publique du routeur :** `203.0.113.3/29` ; passerelle du FAI : `203.0.113.2`. **DNS du FAI :** `198.51.100.53`.

## 4. Plan d'adressage (à compléter)

| Réseau | VLAN | Adresse réseau / masque | Passerelle | Plage DHCP | Adresses fixes |
|---|---|---|---|---|---|
| Soins | 10 | | | | Imprimante : |
| Patients | 20 | | | | – |

**Noms :** switch `SW-VIDAL`, routeur `R-VIDAL`. **Mot de passe `enable` du switch :** `Vidal#2027`. **Wi-Fi :** SSID `VIDAL-PATIENTS`, clé `Patients#2027`, WPA2.

> [!NOTE]
> Étiquettes à noter : ______________________________________

## 5. Contraintes

- Si l'ACL des patients se termine par un `deny ip any any`, elle doit **laisser passer le DHCP** (UDP 68 vers 67).
- Les configurations des **deux équipements** sont **sauvegardées**.
- Aucune adresse n'est fournie à l'avance pour les postes : **DHCP**.

## 6. Cahier de recette (à remplir)

| N° | Exigence | Test | Attendu | Obtenu | Statut |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

## 7. Compte rendu (8 lignes)

Contexte · Ce qui a été installé · Configuration (VLAN, DHCP, NAT, ACL, Wi-Fi) · Tests réalisés · Écarts et corrections · Documents remis · À suivre · Durée.
