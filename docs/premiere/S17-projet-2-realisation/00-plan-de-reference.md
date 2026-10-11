# 📋 Plan de référence du projet ArchiPlus

> [!WARNING]
> **Ne l'ouvre qu'après la revue de conception de S16.** Compare-le à **ton** étude et corrige ton dossier : les contrôles automatiques du simulateur s'appuient sur **ce plan**.

## Plan d'adressage (192.168.50.0/24)

| Service | VLAN | Réseau | Masque | Passerelle | Plage DHCP | Adresses fixes |
|---|---|---|---|---|---|---|
| **Direction** | 10 | 192.168.50.0 | /27 (255.255.255.224) | 192.168.50.1 | .10 à .30 | – |
| **Atelier** | 20 | 192.168.50.32 | /27 (255.255.255.224) | 192.168.50.33 | .40 à .62 | Serveur **.34**, imprimante **.35** |
| **Invités** | 30 | 192.168.50.64 | /26 (255.255.255.192) | 192.168.50.65 | .70 à .120 | – |
| Réserve libre | – | 192.168.50.128 à .255 | | | | |

> [!NOTE]
> **Pourquoi ce découpage ?** Direction et Atelier tiennent chacun dans 30 machines (`/27`) ; les **invités**, plus nombreux et imprévisibles, ont un `/26` (62). Il reste **la moitié du /24** pour grandir.

## Plan de ports du switch SW1 (Cisco 2960)

| Ports | Équipement | VLAN |
|---|---|---|
| Fa0/1 | Poste Direction (`PC-DIR`) | 10 |
| Fa0/8 | Routeur `R1` – Gi0/0 | 10 |
| Fa0/9 | Poste Atelier 1 (`PC-AT1`) | 20 |
| Fa0/10 | Poste Atelier 2 (`PC-AT2`) | 20 |
| Fa0/11 | Imprimante (`IMP`) | 20 |
| Fa0/12 | Serveur (`SRV`) | 20 |
| Fa0/16 | Routeur `R1` – Gi0/1 | 20 |
| Fa0/17 | Borne Wi-Fi (`AP1`) | 30 |
| Fa0/24 | Routeur `R1` – Gi0/2 | 30 |
| Fa0/2-7, 13-15, 18-23 | **Libres** | à désactiver (`shutdown`) |

Regroupement par service : **Fa0/1-8** → VLAN 10, **Fa0/9-16** → VLAN 20, **Fa0/17-24** → VLAN 30.

## Tableau de câblage

| N° | De | Vers | Câble |
|---|---|---|---|
| C01 | `PC-DIR` eth0 | `SW1` Fa0/1 | droit |
| C02 | `R1` Gi0/0 | `SW1` Fa0/8 | droit |
| C03 | `PC-AT1` eth0 | `SW1` Fa0/9 | droit |
| C04 | `PC-AT2` eth0 | `SW1` Fa0/10 | droit |
| C05 | `IMP` | `SW1` Fa0/11 | droit |
| C06 | `SRV` ens33 | `SW1` Fa0/12 | droit |
| C07 | `R1` Gi0/1 | `SW1` Fa0/16 | droit |
| C08 | `AP1` eth0 | `SW1` Fa0/17 | droit |
| C09 | `R1` Gi0/2 | `SW1` Fa0/24 | droit |

**9 câbles droits.**

## Paramètres des services

| Élément | Valeur |
|---|---|
| Serveur | 192.168.50.34/27, passerelle 192.168.50.33, DNS 192.168.50.34 |
| Domaine | `archiplus.local` |
| DNS | `intranet.archiplus.local` → 192.168.50.34 ; `imprimante.archiplus.local` → 192.168.50.35 |
| Baux | Direction et Atelier 8 h, Invités 1 h |
| Wi-Fi | SSID `ARCHI-INVITES`, WPA2, clé `Invites#2027` (exemple de TP) |
| Switch | `enable secret Archi#2027` (exemple de TP) |
