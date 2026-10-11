# 📝 Aide-mémoire – Routeur (Cisco IOS)

*Bac Pro CIEL – Première – S07 – à garder dans ton classeur*

## Les modes (comme sur le switch)

| Prompt | Mode | Pour… |
|---|---|---|
| `R1>` | utilisateur | regarder un peu |
| `R1#` | privilégié (`enable`) | tout lire (`show`) |
| `R1(config)#` | configuration (`configure terminal`) | modifier |
| `R1(config-if)#` | interface | régler une interface |

## Configurer une interface

```text
configure terminal
hostname R1
interface gi0/0
 ip address 192.168.10.1 255.255.255.0
 no shutdown
 exit
```

> [!WARNING]
> Une interface de routeur est **éteinte** (`administratively down`) tant qu'on n'a pas tapé `no shutdown`.

## Routes

| Besoin | Commande |
|---|---|
| Route vers un réseau | `ip route 192.168.20.0 255.255.255.0 10.0.0.2` |
| Route par défaut | `ip route 0.0.0.0 0.0.0.0 10.0.0.2` |
| Supprimer une route | `no ip route …` (mêmes paramètres) |

## Vérifier

| Commande | Ce qu'elle montre |
|---|---|
| `show ip interface brief` | IP et état (up/up) de chaque interface |
| `show ip route` | La table de routage (C, L, S, S\*) |
| `ping 10.0.0.2` | Le voisin répond-il ? (`!!!!!` = oui) |
| `tracert 192.168.20.100` (sur un PC) | Les routeurs traversés |
| `write memory` | Sauvegarde |

## Méthode de dépannage « aller – retour »

1. **Le PC joint-il sa passerelle ?** sinon : IP, masque, câble.
2. **Le routeur joint-il le routeur voisin ?** sinon : interfaces, masques du lien.
3. **Le routeur connaît-il le réseau d'arrivée ?** `show ip route` (ligne `S`).
4. **L'autre routeur connaît-il le réseau de départ ?** (**la route retour !**)
5. **La destination a-t-elle une passerelle ?**
