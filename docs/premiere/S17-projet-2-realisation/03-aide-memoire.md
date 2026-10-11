# 📝 Aide-mémoire – Commandes du projet

## Switch (Cisco 2960)

```text
enable
configure terminal
hostname SW1
vlan 10
 name DIRECTION
exit
interface range fa0/1 - 8
 switchport mode access
 switchport access vlan 10
exit
interface range fa0/2 - 7
 shutdown                 ! ports libres
exit
enable secret MotDePasse
banner motd #Acces reserve#
end
write memory
```

Vérifier : `show vlan brief` · `show interfaces status` · `show running-config`

## Routeur (Cisco 2911)

```text
enable
configure terminal
hostname R1
interface gi0/0
 ip address 192.168.50.1 255.255.255.224
 ip helper-address 192.168.50.34
 no shutdown
exit
```

Vérifier : `show ip interface brief` · `show ip route`

## ACL

```text
ip access-list extended INVITES-IN
 permit udp any eq 68 any eq 67
 permit udp 192.168.50.64 0.0.0.63 host 192.168.50.34 eq 53
 permit tcp 192.168.50.64 0.0.0.63 host 192.168.50.34 eq 80
 deny ip any any
exit
interface gi0/2
 ip access-group INVITES-IN in
```

Vérifier : `show access-lists` (regarde les **matches**)

> [!NOTE]
> Le **masque inverse** (*wildcard*) : `0.0.0.63` désigne les 64 adresses d'un `/26` ; `0.0.0.31` un `/27` ; `0.0.0.0` une machine seule (`host`).

## Postes

| Commande | Utilité |
|---|---|
| `ipconfig /all` | Adresse, passerelle, DNS, serveur DHCP |
| `ipconfig /renew` | Redemander une adresse |
| `ping adresse` | Tester le chemin |
| `nslookup nom` | Tester le DNS |
