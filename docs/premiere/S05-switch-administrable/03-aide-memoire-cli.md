# 📝 Aide-mémoire – La console du switch

## Se déplacer

| Je veux… | Commande | Prompt |
|---|---|---|
| Passer en mode privilégié | `enable` | `SW#` |
| Entrer en configuration | `configure terminal` | `SW(config)#` |
| Configurer un port | `interface fa0/1` | `SW(config-if)#` |
| Configurer plusieurs ports | `interface range fa0/4 - 24` | `SW(config-if-range)#` |
| Configurer les accès à distance | `line vty 0 4` | `SW(config-line)#` |
| Remonter d'un niveau | `exit` | |
| Revenir en mode privilégié | `end` (ou Ctrl+Z) | `SW#` |

## Lire

| Commande | Résultat |
|---|---|
| `show version` | Modèle, version, MAC |
| `show interfaces status` | État de tous les ports |
| `show mac address-table` | MAC ↔ ports |
| `show cdp neighbors` | Équipements voisins branchés (nom, port) |
| `show ip interface brief` | Adresses IP |
| `show running-config` | Configuration en cours |
| `show startup-config` | Configuration sauvegardée |
| `show ip ssh` | État de SSH |

## Configurer

| Je veux… | Commandes |
|---|---|
| Nommer | `hostname SW-ATELIER` |
| Protéger le mode privilégié | `enable secret MotDePasse` |
| Bannière | `banner motd #texte#` |
| Décrire un port | `interface fa0/1` → `description PC-COMPTA` |
| Couper des ports | `interface range fa0/4 - 24` → `shutdown` |
| Rallumer | `no shutdown` |
| Adresse du switch | `interface vlan 1` → `ip address A.B.C.D MASQUE` → `no shutdown` |
| Passerelle du switch | `ip default-gateway A.B.C.D` |
| SSH | `ip domain-name …` · `username … secret …` · `crypto key generate rsa modulus 1024` · `ip ssh version 2` · `line vty 0 4` → `transport input ssh` + `login local` |
| Sauvegarder | `write memory` |
| Annuler une commande | Mettre `no` devant (`no shutdown`, `no description`) |

## Astuces

- `?` : liste des commandes ; `show ?` : sous-commandes.
- **Tab** : complète. Les **abréviations** marchent (`sh int st`).
- **↑** : rappelle la commande précédente.
