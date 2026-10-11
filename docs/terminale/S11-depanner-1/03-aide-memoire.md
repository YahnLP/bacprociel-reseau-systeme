# 📝 Aide-mémoire – Dépannage – démarche et commandes

## Démarche

**Symptôme → hypothèses → tests → cause → action → vérification.** Une correction à la fois.

## Échelle des tests

1. Câble / carte · 2. Adresse (`169.254` ?) · 3. Passerelle · 4. Autre réseau · 5. Serveur par adresse · 6. Serveur par nom (DNS).

## Symptôme → premières hypothèses

| Symptôme | À regarder en premier |
|---|---|
| `169.254.x.x` | VLAN du port, DHCP, câble |
| Joint la passerelle, pas plus loin | routage, ACL, VLAN du serveur |
| Joint par adresse, pas par nom | DNS (poste ou serveur) |
| Un poste seul est touché | câble, port, configuration du poste |
| Tout un VLAN est touché | trunk, sous-interface, DHCP |

## Commandes

`ipconfig /all` · `ping` · `show vlan brief` · `show interfaces trunk` · `show ip interface brief` · `show ip dhcp binding` · `show running-config`.
