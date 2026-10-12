# 📖 Cours – Transférer des fichiers : FTP et SFTP

*Parcours serveurs – module 2*

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer le fonctionnement de **FTP** et pourquoi il est risqué ;
- [ ] installer et régler un serveur **vsftpd** ;
- [ ] utiliser **SFTP** et expliquer pourquoi on le préfère.

---

## 1. FTP

**FTP** (*File Transfer Protocol*) utilise deux connexions TCP : le port **21** (commandes) et le port **20** en mode actif (données).

> [!WARNING]
> FTP envoie l'identifiant et le mot de passe **en clair**. Quelqu'un qui capture le réseau (Wireshark) les lit.

| Réglage de `/etc/vsftpd.conf` | Effet |
|---|---|
| `anonymous_enable=NO` | interdit la connexion anonyme |
| `local_enable=YES` | autorise les comptes locaux |
| `write_enable=YES` | autorise l'écriture |
| `chroot_local_user=YES` | enferme l'utilisateur dans son dossier |

## 2. SFTP

**SFTP** (*SSH File Transfer Protocol*) passe par **SSH**, port **22**. Tout est **chiffré**, il n'y a **rien de plus à installer** si SSH est déjà là.

| | FTP | SFTP |
|---|---|---|
| Port | 21 (+ 20) | 22 |
| Chiffrement | **non** | **oui** |
| Serveur | vsftpd | `openssh-server` |
| Client | `ftp`, FileZilla | `sftp`, FileZilla, WinSCP |

Commandes usuelles du client : `ls`, `cd`, `get fichier` (télécharger), `put fichier` (envoyer), `exit`.

> [!NOTE]
> Même idée côté Cisco : TFTP et FTP sont en clair ; l'équivalent sécurisé passe par SSH (voir le module 4-05 du [parcours CCNA](../../ccna/4-05-ssh-tftp/01-cours.md)).

---

## 🧠 Quiz de fin

**1.** Quel port écoute le serveur FTP pour les commandes ?

<details markdown="1"><summary>Voir la réponse</summary>

Le port **21**.

</details>

**2.** Pourquoi FTP est-il dangereux sur un réseau non maîtrisé ?

<details markdown="1"><summary>Voir la réponse</summary>

Identifiant et mot de passe circulent **en clair**.

</details>

**3.** Quel port utilise SFTP ?

<details markdown="1"><summary>Voir la réponse</summary>

Le port **22**, comme SSH.

</details>

**4.** Que fait `chroot_local_user=YES` ?

<details markdown="1"><summary>Voir la réponse</summary>

Il **enferme** chaque utilisateur dans son dossier personnel.

</details>

➡️ Suite : [le TP du module](02-tp.md).
