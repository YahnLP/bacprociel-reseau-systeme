# Corrigé – Première S18 (recette et dépannage)

Fichier : `P18-panne-corrige.json` (installation réparée).

| Panne | Symptôme | Test | Cause | Correction |
|---|---|---|---|---|
| 1 | `PC-AT2` a une adresse 192.168.50.7x | `show vlan brief` | Fa0/10 dans le VLAN 30 | `interface fa0/10` → `switchport access vlan 20` (mot de passe `Archi#2027`), `ipconfig /renew` |
| 2 | `PC-DIR` sans adresse (169.254) | `show running-config` sur R1 | Pas d'`ip helper-address` sur Gi0/0 | `interface gi0/0` → `ip helper-address 192.168.50.34`, `ipconfig /renew` |
| 3 | Invités : site par adresse OK, par nom KO | `nslookup` → délai dépassé ; `show access-lists` | Règle DNS absente de l'ACL | `ip access-list extended INVITES-IN` → `25 permit udp 192.168.50.64 0.0.0.63 host 192.168.50.34 eq 53` |

**Recette** : 14 tests réussis sur le corrigé ; les tests 11 et 12 doivent **échouer** (c'est le résultat attendu).
