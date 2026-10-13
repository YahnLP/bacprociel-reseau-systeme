# 📖 Glossaire – Parcours serveurs

| Français | Anglais | Définition simple | Module |
|---|---|---|---|
| Machine virtuelle | *VM (virtual machine)* | Un ordinateur simulé dans un logiciel | 0 |
| Hyperviseur | *hypervisor* | Logiciel qui fait tourner les VM (VirtualBox) | 0 |
| Instantané | *snapshot* | Photo de l'état d'une VM, pour revenir en arrière | 0 |
| Réseau privé hôte | *host-only network* | Réseau entre ton PC et tes VM seulement | 0 |
| Service | *service / daemon* | Programme qui tourne en arrière-plan | 1 |
| Serveur web | *web server (Apache, Nginx)* | Envoie des pages aux navigateurs (HTTP) | 1 |
| Pile LAMP | *LAMP stack* | Linux, Apache, MariaDB, PHP | 1 |
| Racine du site | *document root* | Dossier des pages du site (`/var/www/html`) | 1 |
| Transfert de fichiers | *FTP / SFTP* | FTP en clair ; SFTP chiffré par SSH | 2 |
| Cage de l'utilisateur | *chroot* | Limite l'utilisateur à son dossier | 2 |
| Stockage en réseau | *NAS (network attached storage)* | Serveur de fichiers prêt à l'emploi | 3 |
| Partage de fichiers | *SMB / CIFS* | Protocole de partage Windows | 3 |
| Redondance de disques | *RAID* | Plusieurs disques pour la disponibilité (≠ sauvegarde) | 3 |
| Annuaire | *Active Directory (AD)* | Base centrale des comptes et ordinateurs | 4 |
| Contrôleur de domaine | *domain controller (DC)* | Serveur qui porte l'AD | 4 |
| Unité d'organisation | *OU* | Dossier de l'annuaire pour ranger comptes et ordinateurs | 4 |
| Stratégie de groupe | *GPO (group policy object)* | Règles appliquées aux comptes et postes | 4 |
| Code d'état | *HTTP status code* | 200 OK, 403 interdit, 404 introuvable, 502 passerelle | 1 |
| Site virtuel | *virtual host* | Plusieurs sites sur une même adresse, distingués par le nom | 1 |
| Serveur mandataire inverse | *reverse proxy* | Reçoit les requêtes et les transmet à une application | 1 |
| Mode passif | *passive mode (FTP)* | Le client ouvre aussi la connexion de données | 2 |
| Chroot | *chroot* | Enferme l'utilisateur dans un dossier | 2 |
| Niveaux de droits d'un partage | *share permissions / file permissions* | Droit du partage + droit du dossier : le plus restrictif s'applique | 3 |
| Règle 3-2-1 | *3-2-1 backup rule* | 3 copies, 2 supports, 1 hors site | 3 |
| Kerberos | *Kerberos* | Authentification par tickets (heure précise exigée) | 4 |
| Enregistrement de service | *SRV record* | Entrée DNS qui indique où se trouve un service (le DC) | 4 |
| Relation d'approbation | *trust / secure channel* | Lien de confiance entre un poste et le domaine | 4 |
| Incident | *incident / ticket* | Signalement d'un dysfonctionnement à traiter | 5 |
| Contournement | *workaround* | Solution provisoire, sans traiter la cause | 5 |
