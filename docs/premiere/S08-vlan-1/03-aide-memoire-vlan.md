# 📝 Aide-mémoire – VLAN (Cisco IOS)

*Bac Pro CIEL – Première – S08*

## Créer et affecter

```text
configure terminal
vlan 10
 name DIRECTION
 exit
interface range fa0/1 - 2
 switchport mode access
 switchport access vlan 10
 exit
end
write memory
```

## Vérifier

| Commande | Montre |
|---|---|
| `show vlan brief` | Les VLAN et leurs ports |
| `show interfaces status` | La colonne **Vlan** de chaque port |
| `show interfaces fa0/1 switchport` | Mode (access) et VLAN du port |
| `show mac address-table` | Les MAC apprises, par VLAN |

## Plan de VLAN de la PME (à compléter)

| VLAN | Nom | Sous-réseau | Ports | Passerelle |
|---|---|---|---|---|
| 10 | DIRECTION | 192.168.10.0/24 | Fa0/1 – 2 | 192.168.10.1 |
| 20 | ATELIER | 192.168.20.0/24 | Fa0/3 – 4 | 192.168.20.1 |
| | | | | |

## Méthode de dépannage « un poste ne joint pas ses collègues »

1. Le **câble** est-il sur le bon port ? (`show interfaces status`)
2. Le **port** est-il dans le **bon VLAN** ?
3. Le VLAN **existe-t-il** (`show vlan brief`) ?
4. Le poste a-t-il la **bonne adresse** pour son VLAN ?
