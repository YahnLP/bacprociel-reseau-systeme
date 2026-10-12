# TP 3 – Utiliser un NAS (OpenMediaVault)

> [!EXAMPLE] 🚀 Pour aller plus loin
> Un **NAS** (*Network Attached Storage*) est un serveur de fichiers prêt à l'emploi. OpenMediaVault (OMV) en est une version libre, installable en VM.

## Préparation

- ISO d'OpenMediaVault fournie par l'enseignant ; VM : 2 Go de RAM, 1 disque système de 8 Go **+ 1 disque de données de 10 Go**, deux cartes réseau (NAT + privé hôte).
- Après l'installation, l'interface web est à `http://adresse-vm/` (identifiants par défaut indiqués dans la documentation d'OMV : **change-les tout de suite**).

## Étapes

1. Dans l'interface : repérer le disque de données, créer le **système de fichiers**, puis le **monter**.
2. Créer un **dossier partagé** « commun ».
3. Créer deux **utilisateurs** (ex. `eleve1`, `eleve2`) et donner à `eleve1` le droit d'écriture, à `eleve2` la lecture seule.
4. Activer le service **SMB/CIFS** et publier le dossier.
5. Depuis Windows : explorateur → `\\adresse-vm\commun`, connexion en `eleve1`. Depuis Linux : `smbclient //adresse-vm/commun -U eleve1`.

## Points de contrôle

- [ ] `eleve1` crée un fichier, `eleve2` ne peut que le lire ;
- [ ] je sais expliquer la différence entre un NAS et un disque dur USB ;
- [ ] je connais deux idées de sauvegarde (copie sur un 2ᵉ disque, RAID n'est **pas** une sauvegarde).

> [!NOTE]
> Lien avec le programme : l'intégration d'un NAS dans une installation client (Terminale, séance 08).
