# TP 1 – Serveur web : Apache, Nginx, LAMP

> [!EXAMPLE] 🚀 Pour aller plus loin
> Sur Debian/Ubuntu Server. Un seul serveur web à la fois (ils utilisent le port 80).

## A. Apache

```bash
sudo apt update
sudo apt install -y apache2
systemctl status apache2
```

Depuis ton PC : `http://adresse-privee-hote/` → page « Apache2 Default Page ».
La page se trouve dans `/var/www/html/index.html` : modifie-la.

```bash
echo "<h1>Serveur de $(hostname)</h1>" | sudo tee /var/www/html/index.html
curl http://localhost
```

Journaux : `/var/log/apache2/access.log` et `error.log` (`tail -f`).

## B. Nginx (à la place d'Apache)

```bash
sudo systemctl disable --now apache2
sudo apt install -y nginx
systemctl status nginx
```

Page : `/var/www/html/`. Configuration : `/etc/nginx/sites-available/`. Test avant rechargement :

```bash
sudo nginx -t && sudo systemctl reload nginx
```

## C. Pile LAMP (Linux, Apache, MariaDB, PHP)

```bash
sudo systemctl disable --now nginx
sudo systemctl enable --now apache2
sudo apt install -y mariadb-server php libapache2-mod-php php-mysql
echo "<?php phpinfo();" | sudo tee /var/www/html/info.php
```

`http://adresse/info.php` affiche la configuration PHP. **Supprime** ce fichier ensuite (il révèle des informations sensibles).

Base de données : `sudo mysql` puis `CREATE DATABASE test;`.

## Points de contrôle

- [ ] la page personnalisée s'affiche depuis ton PC ;
- [ ] je sais où sont les fichiers du site et les journaux ;
- [ ] j'ai arrêté un serveur web et démarré l'autre avec `systemctl` ;
- [ ] `info.php` est supprimé.

> [!WARNING]
> Un serveur web exposé sans mise à jour est une porte d'entrée : `sudo apt upgrade` régulièrement.
