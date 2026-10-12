# 🚀 Serveurs sur VirtualBox

*Pour aller plus loin – hors programme, non exigé à l'épreuve E31.*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Des **TP serveurs** à faire sur des **machines virtuelles VirtualBox**, pour les élèves en avance. Le simulateur du site ne remplace pas un vrai système : ici, on installe de **vrais** services.

| TP | Ce que tu installes | Durée indicative | Niveau |
|---|---|---|---|
| [0 · Préparer VirtualBox](01-preparer-virtualbox.md) | Réseau NAT + réseau privé hôte, instantanés | 30 min | à faire en premier |
| [1 · Serveur web](02-serveur-web.md) | Apache, Nginx, pile LAMP | 1 h 30 | ⭐⭐ |
| [2 · Serveur FTP / SFTP](03-serveur-ftp-sftp.md) | vsftpd, SFTP via SSH | 1 h | ⭐⭐ |
| [3 · NAS](04-nas.md) | OpenMediaVault, partage SMB | 2 h | ⭐⭐ |
| [4 · Active Directory](05-active-directory.md) | Windows Server, domaine, utilisateurs, GPO | 3 h | ⭐⭐⭐ |

## Règles du jeu

1. Ces TP viennent **après** tes TP de la séance, validés par l'enseignant.
2. **Instantané avant chaque manipulation** : si tu casses, tu reviens en arrière.
3. Ne jamais mettre une VM en **accès par pont** sur le réseau du lycée sans l'accord de l'enseignant : utilise NAT + réseau privé hôte.
4. Les images ISO sont **téléchargées à l'avance** (le réseau est limité) : demande-les à l'enseignant.
5. Note tes commandes et captures dans ton **dossier de preuves**.

> [!NOTE]
> Ces pages n'ont pas d'équivalent dans le simulateur : les vérifications se font **avec de vrais outils** (`curl`, `systemctl status`, explorateur Windows…). Ce sont des trames de TP à adapter à ton matériel.
