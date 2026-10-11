# 📝 Aide-mémoire – Inter-VLAN

## Switch d'accès (2960)

```text
vlan 10
 name COMPTA
interface fa0/1
 switchport mode access
 switchport access vlan 10
interface gi0/1
 switchport mode trunk
```

Vérifier : `show vlan brief` · `show interfaces trunk`

## Routeur sur un tronc

```text
interface gi0/0
 no shutdown
interface gi0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
```

Vérifier : `show ip interface brief` · `show ip route`

## Switch de niveau 3 (3560)

```text
ip routing
interface vlan 10
 ip address 192.168.10.1 255.255.255.0
 no shutdown
interface gi0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
```

## ACL

```text
ip access-list extended NOM
 deny ip <source> <wildcard> <destination> <wildcard>
 permit ip any any
interface gi0/0.20
 ip access-group NOM in
```

Ajouter **au milieu** d'une ACL : `25 permit …` (numéro de séquence).
Vérifier : `show access-lists`.

## Schéma de dépannage

| Couche | Test |
|---|---|
| 1 | Câble, voyants |
| 2 | `show vlan brief`, `show interfaces trunk` |
| 3 | `show ip interface brief`, `show ip route`, passerelle du poste |
| Filtrage | `show access-lists` (matches) |
