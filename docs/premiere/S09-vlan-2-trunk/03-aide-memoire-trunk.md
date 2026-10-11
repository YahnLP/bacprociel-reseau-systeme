# 📝 Aide-mémoire – Trunk (Cisco IOS)

*Bac Pro CIEL – Première – S09*

```text
interface gi0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20
```

| Besoin | Commande |
|---|---|
| Créer le trunk | `switchport mode trunk` (des **deux** côtés) |
| Limiter les VLAN | `switchport trunk allowed vlan 10,20` |
| Ajouter un VLAN | `switchport trunk allowed vlan add 30` |
| Voir les trunks | `show interfaces trunk` |
| Voir un port | `show interfaces gi0/1 switchport` |
| Sauvegarder | `write memory` |

## Méthode de dépannage « deux switchs, un VLAN »

1. **Même VLAN** des deux côtés ? (`show vlan brief` sur chaque switch)
2. **Ports** dans le bon VLAN ?
3. **Trunk** actif **des deux côtés** ? (`show interfaces trunk` sur chacun)
4. Le VLAN est-il dans la liste **allowed** ?
5. **Même VLAN natif** des deux côtés ?
