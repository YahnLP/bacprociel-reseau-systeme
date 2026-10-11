# 📝 Aide-mémoire – Wi-Fi d'entreprise

## Réglages d'une borne

| Réglage | À vérifier |
|---|---|
| **SSID** | Nom exact (majuscules !) |
| **Clé** | Identique sur la borne et sur le client |
| **Sécurité** | WPA2 ou WPA3 (jamais WEP) |
| **Port du switch** | Bon VLAN (access) ou trunk si plusieurs SSID |

## Commandes utiles

```text
show vlan brief
show interfaces trunk
show ip dhcp pool
show ip dhcp binding
show access-lists
```

Côté poste : `ipconfig` (Windows) · `ip a` (Linux).

## Dépannage Wi-Fi : l'ordre des tests

1. **Signal** suffisant ? 2. **Clé** correcte ? 3. **Adresse** reçue (`169.254` = DHCP) ? 4. **Bon VLAN** ? 5. **Passerelle** joignable ? 6. **ACL** : bloque-t-elle trop ?
