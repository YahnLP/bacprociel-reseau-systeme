# 🗄️ Parcours serveurs sur VirtualBox

*Parcours complémentaire : installer et administrer de vrais serveurs.*

> [!NOTE]
> Ce parcours **complète** les séances de la classe. Les élèves qui terminent leur TP de la séance l'utilisent pour avancer à leur rythme. Il s'appuie sur des **machines virtuelles VirtualBox** : le simulateur réseau ne remplace pas un vrai système (pas de vrai Apache, Samba ni Active Directory).

## 🎯 Comment ça marche

1. **Quand ?** Après ton TP de la séance, validé par ton enseignant.
2. **Quoi ?** Des **modules** autonomes. Chaque module contient un **cours** (avec son quiz), puis un **TP** à réaliser sur tes machines virtuelles.
3. **Où j'en suis ?** Coche tes modules sur la [feuille de route](feuille-de-route.md).
4. **Le vocabulaire** est dans le [glossaire serveurs](glossaire-serveurs.md).
5. **Preuves.** Garde captures et commandes dans ton **dossier de preuves**.

## 📚 Les modules

| Module | Contenu | Durée indicative | Niveau |
|---|---|---|---|
| [0 · Préparer VirtualBox](m0-virtualbox/01-cours.md) | Virtualisation, modes réseau, instantanés | 1 h | À faire en premier |
| [1 · Serveur web](m1-serveur-web/01-cours.md) | Apache, Nginx, pile LAMP | 2 h | ⭐⭐ |
| [2 · Serveur FTP et SFTP](m2-ftp-sftp/01-cours.md) | vsftpd, SFTP, transferts sécurisés | 1 h 30 | ⭐⭐ |
| [3 · Utiliser un NAS](m3-nas/01-cours.md) | OpenMediaVault, partage SMB, droits | 2 h | ⭐⭐ |
| [4 · Active Directory](m4-active-directory/01-cours.md) | Windows Server, domaine, GPO | 3 h | ⭐⭐⭐ |

## 🛡️ Règles du jeu

- **Instantané avant chaque manipulation** : si tu casses quelque chose, tu reviens en arrière.
- **Jamais d'accès par pont** sur le réseau du lycée sans l'accord de l'enseignant : tu utilises NAT + réseau privé hôte.
- Les **images ISO** sont téléchargées à l'avance (le réseau est limité) : demande-les à l'enseignant.

> [!TIP]
> Lien avec le [parcours CCNA](../ccna/README.md) : les deux se complètent (réseau d'un côté, services et serveurs de l'autre).
