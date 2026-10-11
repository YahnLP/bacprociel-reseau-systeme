# 📝 Aide-mémoire – Intégrer un équipement

## Procédure d'intégration

1. **Où ?** 2. **Adresse fixe** (hors DHCP) 3. **VLAN** 4. **Brancher / configurer** 5. **Tester** 6. **Documenter**.

## Commandes du switch niveau 3

```text
ip routing
vlan 40
 name OBJETS
interface fa0/3
 switchport mode access
 switchport access vlan 40
interface vlan 40
 ip address 192.168.40.1 255.255.255.0
 no shutdown
ip dhcp excluded-address 192.168.10.1 192.168.10.49
```

## PoE : rappel

Budget du switch (W) ≥ somme des puissances des appareils. Câble : catégorie 5e minimum.

## Plan d'adressage type

| Plage | Usage |
|---|---|
| `.1` | passerelle |
| `.2` – `.49` | équipements fixes |
| `.50` – `.200` | DHCP |
