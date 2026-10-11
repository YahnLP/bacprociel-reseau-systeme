# 📝 Aide-mémoire – Linux serveur

*Bac Pro CIEL – Première – S10*

## Se repérer

| Commande | Rôle |
|---|---|
| `pwd` / `ls -l` / `cd` | Où suis-je, que contient ce dossier, y aller |
| `cat` / `less` / `nano` | Lire / parcourir / éditer |
| `man commande` | Manuel (q pour quitter) |
| `cat /etc/os-release` | Version de la distribution |
| `hostnamectl` | Nom du serveur |

## Réseau

| Commande | Rôle |
|---|---|
| `ip a` (ou `ip -br a`) | Adresses des interfaces |
| `ip r` | Table de routage (passerelle = ligne `default via`) |
| `ping -c 4 IP` | Joindre une machine |
| `ss -tlnp` | Services qui écoutent (port 22 = SSH) |
| `sudo netplan apply` | Appliquer la configuration réseau |

Fichier netplan (espaces, **jamais de tabulation**) :

```yaml
network:
  version: 2
  ethernets:
    enp0s8:
      addresses: [192.168.56.10/24]
```

## Utilisateurs

| Commande | Rôle |
|---|---|
| `whoami`, `id` | Qui suis-je |
| `sudo adduser nom` | Créer un compte |
| `sudo usermod -aG sudo nom` | Lui donner `sudo` |
| `sudo passwd nom` | Changer le mot de passe |

## Services et journaux

| Commande | Rôle |
|---|---|
| `systemctl status ssh` | État du service |
| `sudo systemctl restart ssh` | Redémarrer |
| `sudo journalctl -u ssh -n 20` | 20 dernières lignes du journal SSH |
| `sudo sshd -t` | Tester la configuration SSH (rien = OK) |

## SSH

| Commande | Rôle |
|---|---|
| `ssh eleve@192.168.56.10` | Se connecter |
| `ssh-keygen -t ed25519` | Créer une paire de clés |
| `exit` | Fermer la session |

Fichiers : `~/.ssh/authorized_keys` (clés autorisées, côté serveur), `/etc/ssh/sshd_config.d/` (réglages du serveur).
