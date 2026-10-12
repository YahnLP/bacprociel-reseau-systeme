# TP 4 – Active Directory sur Windows Server

> [!EXAMPLE] 🚀 Pour aller plus loin
> **Active Directory (AD)** centralise les comptes et les règles d'un parc Windows. C'est le sujet le plus long : prévois plusieurs séances.

## Préparation

- ISO d'évaluation de Windows Server et de Windows 10/11 fournies par l'enseignant.
- **VM1 Serveur** : 2 Go de RAM minimum, NAT + réseau privé hôte. **VM2 Client** Windows, réseau privé hôte uniquement.
- Adresses fixes sur le réseau privé hôte : serveur 192.168.56.10/24 (DNS = lui-même), client 192.168.56.20/24, DNS = 192.168.56.10.

## Étapes

1. Renommer le serveur (`SRV-AD`) et fixer son IP.
2. *Gestionnaire de serveur → Ajouter des rôles* : **services AD DS** (et DNS).
3. **Promouvoir** en contrôleur de domaine : nouvelle forêt, par exemple `entreprise.local`. Redémarrer.
4. Dans *Utilisateurs et ordinateurs Active Directory* : créer une **unité d'organisation** « Compta », deux utilisateurs et un groupe.
5. Joindre le **client** au domaine (*Paramètres système → Domaine*), puis ouvrir une session avec un compte du domaine.
6. Créer une **GPO** simple (ex. fond d'écran imposé ou lecteur réseau) liée à l'unité d'organisation, puis `gpupdate /force` sur le client.

## Points de contrôle

- [ ] le client ouvre une session avec un compte de l'AD ;
- [ ] la GPO s'applique sur le compte de l'unité « Compta » mais pas ailleurs ;
- [ ] je sais expliquer : domaine, contrôleur de domaine, unité d'organisation, GPO.

> [!WARNING]
> Le DNS du client doit pointer vers le serveur AD, sinon la jonction au domaine échoue : c'est la panne la plus fréquente.
