# TP 2 – Serveur FTP / SFTP

> [!EXAMPLE] 🚀 Pour aller plus loin
> FTP envoie les mots de passe **en clair**. On l'installe pour comprendre, puis on lui préfère **SFTP**.

## A. FTP avec vsftpd

```bash
sudo apt install -y vsftpd
sudo nano /etc/vsftpd.conf
```

Vérifie ou règle : `anonymous_enable=NO`, `local_enable=YES`, `write_enable=YES`, `chroot_local_user=YES`, `allow_writeable_chroot=YES` (pour ce TP).

```bash
sudo systemctl restart vsftpd
sudo adduser eleve1
```

Depuis ton PC : `ftp adresse-privee-hote` (ou FileZilla), connexion avec `eleve1`.

## B. Voir le problème

Lance Wireshark sur ta carte privée hôte, filtre `ftp` : tu lis `USER` et `PASS` **en clair**.

## C. SFTP (via SSH, port 22)

```bash
sudo apt install -y openssh-server
sftp eleve1@adresse-privee-hote
```

Mêmes transferts (`put`, `get`, `ls`), mais **chiffrés** : dans Wireshark, plus de mot de passe lisible. Tu peux arrêter vsftpd : `sudo systemctl disable --now vsftpd`.

## Points de contrôle

- [ ] j'ai transféré un fichier en FTP puis en SFTP ;
- [ ] j'ai capturé le mot de passe FTP en clair ;
- [ ] je sais dire pourquoi on utilise SFTP aujourd'hui ;
- [ ] vsftpd est désactivé à la fin.

> [!NOTE]
> Lien avec le parcours CCNA : module 4-05 (TFTP, FTP, SFTP).
