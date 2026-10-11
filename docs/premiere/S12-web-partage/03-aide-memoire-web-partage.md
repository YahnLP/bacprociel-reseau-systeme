# 📝 Aide-mémoire – Web et partage de fichiers

*Bac Pro CIEL – Première – S12*

## Web (simulateur)

| Où | Quoi |
|---|---|
| `SRV1` ▸ **Services ▸ Web** | Cocher « Serveur web activé » ; liste des pages ; éditeur ; « Enregistrer la page » |
| Même onglet | « HTTPS (443) » : activer le chiffrement |
| `PC1` ▸ **Navigateur** | Taper l'adresse puis **Aller** |
| `PC1` ▸ **Terminal** | `curl http://…`, `curl https://…` |

Codes : **200** OK · **403** interdit · **404** introuvable · « Connexion refusée » : service arrêté.

## Samba (VM Ubuntu Server)

```text
sudo apt update && sudo apt install -y samba
sudo groupadd direction
sudo adduser alice
sudo usermod -aG direction alice
sudo smbpasswd -a alice
sudo mkdir -p /srv/partage/direction
sudo chown root:direction /srv/partage/direction
sudo chmod 2770 /srv/partage/direction
```

À ajouter à la fin de `/etc/samba/smb.conf` :

```text
[direction]
   path = /srv/partage/direction
   valid users = @direction
   read only = no
```

```text
testparm
sudo systemctl restart smbd
```

Depuis Windows : `\\192.168.56.10\direction` (explorateur de fichiers) → identifiant `alice`.

## Vérifier

| Commande | Rôle |
|---|---|
| `testparm` | Valider `smb.conf` |
| `sudo smbstatus` | Qui est connecté ? |
| `ls -ld /srv/partage/direction` | Droits du dossier (`drwxrws---`) |
| `groups alice` | Groupes d'alice |
