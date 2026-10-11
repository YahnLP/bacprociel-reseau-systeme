# 📝 Aide-mémoire – Accès à distance

## SSH sur un routeur ou un switch

```text
ip domain-name garage.local
username tech privilege 15 secret Tech#2027
crypto key generate rsa modulus 1024
ip ssh version 2
line vty 0 4
 transport input ssh
 login local
```

Connexion : `ssh tech@192.168.1.1`.

## Redirection de port (NAT statique)

```text
ip nat inside source static tcp <ip-interne> <port-interne> <ip-publique> <port-externe>
show ip nat translations
```

## Réflexes

- Jamais de **telnet**. Jamais de **bureau à distance** exposé.
- Un port ouvert = un risque : **le moins possible**.
- **VPN** pour entrer dans le réseau.

## Fiche de télémaintenance

Autorisation · Compte nominatif · Périmètre · Durée · Fermeture · Journal.
