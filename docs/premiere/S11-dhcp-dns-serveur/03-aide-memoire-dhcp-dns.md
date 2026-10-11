# 📝 Aide-mémoire – DHCP et DNS

*Bac Pro CIEL – Première – S11*

## Champs du pool DHCP (formulaire du simulateur)

| Champ | Valeur du TP |
|---|---|
| Nom du pool | LAN |
| Réseau / masque | 192.168.10.0 / 255.255.255.0 |
| Passerelle | 192.168.10.1 |
| DNS | 192.168.10.2 |
| Domaine | mecapro.local |
| Première / dernière adresse | 192.168.10.50 / 192.168.10.150 |
| Durée du bail | 28800 s |
| Adresses exclues | 192.168.10.1 → 192.168.10.49 |

Penser à **cocher « Service DHCP activé »** puis **Ajouter / remplacer le pool**.

## Enregistrements DNS du TP

| Nom | Type | Valeur |
|---|---|---|
| srv.mecapro.local | A | 192.168.10.2 |
| intranet.mecapro.local | A | 192.168.10.2 |
| imprimante.mecapro.local | A | 192.168.10.30 |

Penser à **cocher « Service DNS activé »**.

## Vérifier depuis un poste

| Windows | Linux | Rôle |
|---|---|---|
| `ipconfig /all` | `ip a` | Adresse, passerelle, DNS, serveur DHCP, bail |
| `ipconfig /renew` | `sudo dhclient` | Redemander une adresse |
| `nslookup nom` | `nslookup nom` / `dig nom` | Résoudre un nom |
| `ping nom` | `ping nom` | Résolution **et** réponse |

## Arbre de décision

1. Adresse en **169.254.x.x** ? → DHCP (service, pool, câble).
2. Adresse OK, **ping IP** échoue ? → passerelle, masque, routage.
3. Ping IP OK, **nom** échoue ? → DNS (serveur donné ? zone ? enregistrement ?).
4. Nom se résout mais **mauvaise adresse** ? → enregistrement de la zone.
