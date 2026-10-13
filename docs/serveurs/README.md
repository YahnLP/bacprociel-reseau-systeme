# 🌐 Parcours serveurs sur VirtualBox

*Parcours complémentaire : installer, sécuriser et **dépanner** de vrais serveurs.*

> [!NOTE]
> Ce parcours **complète** les séances de la classe. Il s'appuie sur des **machines virtuelles VirtualBox** : le simulateur réseau ne remplace pas un vrai système (pas de vrai Apache, Samba ni Active Directory). Il forme à **comprendre** ce que l'on installe, à **sécuriser**, et à **résoudre les pannes** avec méthode, comme un technicien.

## 🎯 Ce que tu apprends dans chaque module

Chaque module suit **le même fil** :

| Étape | Question à laquelle on répond |
|---|---|
| **Comprendre** | Comment ça marche ? Que se passe-t-il entre le client et le serveur ? |
| **Installer en justifiant** | Pourquoi cette commande ? Qu'est-ce qu'elle change ? |
| **Configurer et sécuriser** | Quels réglages, avec quels **droits minimaux** ? |
| **Surveiller** | Où lire les journaux, que signifient les codes ? |
| **Dépanner** | Quel est le message d'erreur **réel**, la cause, la vérification, la correction ? (les pannes décrites ont été **reproduites** pour Apache, Nginx, MariaDB, vsftpd, SFTP et Samba) |
| **S'entraîner** | Un TP en plusieurs parties, dont des **pannes provoquées par ton binôme** à diagnostiquer |

## 🧭 Les outils transversaux (à avoir ouverts en TP)

| Fiche | Usage |
|---|---|
| [🔧 La méthode de dépannage](methode-depannage.md) | 7 étapes, raisonnement par couches |
| [📋 Fiche de dépannage](fiche-depannage.md) | à remplir pour **chaque** panne (ton dossier de preuves) |

## 📚 Les modules

| Module | Contenu | Durée indicative | Niveau |
|---|---|---|---|
| [0 · VirtualBox, Linux serveur et diagnostic](m0-virtualbox/01-cours.md) | Virtualisation, réseaux des VM, Linux (droits, services, journaux), 1ers dépannages | 2 h + 1 h | À faire en premier |
| [1 · Serveur web](m1-serveur-web/01-cours.md) | HTTP, Apache/Nginx, sites virtuels, droits, LAMP, 403/404/500/502 | 3 h | ⭐⭐ |
| [2 · FTP, FTPS et SFTP](m2-ftp-sftp/01-cours.md) | Fonctionnement FTP, sécurité, vsftpd, SFTP cloisonné, codes de réponse | 3 h | ⭐⭐ |
| [3 · NAS et partages](m3-nas/01-cours.md) | SMB, deux niveaux de droits, Samba, OpenMediaVault, sauvegarde | 4 h | ⭐⭐⭐ |
| [4 · Active Directory](m4-active-directory/01-cours.md) | Domaine, DNS, Kerberos, OU, GPO, jonction, pannes | 5 h | ⭐⭐⭐ |
| [5 · Dépannage de synthèse](m5-depannage/01-synthese.md) | Le technicien face à l'incident : tickets, priorités, compte rendu | 3 h | ⭐⭐⭐ |

## 🛡️ Règles du jeu

- **Instantané avant chaque manipulation** : si tu casses quelque chose, tu reviens en arrière.
- **Jamais d'accès par pont** sur le réseau du lycée sans l'accord de l'enseignant : NAT + réseau privé hôte.
- Les **images ISO** sont téléchargées à l'avance : demande-les à l'enseignant.
- **On ne corrige pas avant d'avoir compris** : `chmod 777` n'est **jamais** une solution.
- Chaque panne **documentée** (fiche) rejoint ton **dossier de preuves**.

> [!NOTE]
> Le module 4 (Active Directory) n'a pas pu être testé sur un vrai Windows Server lors de la rédaction : ses commandes sont celles de la documentation Microsoft, **à valider avec ton enseignant**.

> [!TIP]
> Lien avec le [parcours CCNA](../ccna/README.md) (réseau) et le [parcours Stormshield](../stormshield/README.md) (pare-feu) : les trois se complètent.
