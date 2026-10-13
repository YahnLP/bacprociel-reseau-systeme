# 🔧 La méthode de dépannage

*Parcours serveurs – fiche transversale à garder sous les yeux dans **tous** les TP*

> [!NOTE]
> Un technicien ne se reconnaît pas à ce qu'il sait installer, mais à ce qu'il sait **faire quand ça ne marche pas**. Cette méthode s'applique à tout : un site web inaccessible, un partage refusé, un poste qui n'ouvre plus de session.

## Les 7 étapes

| # | Étape | La question à se poser | Exemple (« mon site ne s'affiche pas ») |
|---|---|---|---|
| 1 | **Décrire le symptôme** | Qu'est-ce qui ne marche pas **exactement** ? Qu'est-ce qui marchait avant ? | « Le navigateur affiche *connexion refusée* depuis mon PC ; hier ça marchait » |
| 2 | **Délimiter** | Qui est touché ? Depuis où ? Tout ou une partie ? | « Seulement depuis mon PC ? Depuis la VM elle-même ? » |
| 3 | **Chercher ce qui a changé** | Qu'a-t-on modifié depuis que ça marchait (configuration, mise à jour, câble, instantané restauré) ? | « J'ai modifié le fichier du site et rechargé » |
| 4 | **Poser des hypothèses, du plus simple au plus probable** | Par **couches** : réseau → service → configuration → droits → application | « Le service est-il arrêté ? Le port est-il ouvert ? La configuration est-elle valide ? » |
| 5 | **Tester une hypothèse à la fois** | Quelle commande la confirme ou l'élimine ? | `systemctl status`, `ss -tlnp`, `curl -v`, journal |
| 6 | **Corriger, un seul changement à la fois** | Si je change deux choses, saurai-je laquelle a corrigé ? | je corrige, je recharge, je reteste |
| 7 | **Vérifier et documenter** | Le problème est-il vraiment résolu **et** n'en ai-je pas créé un autre ? Qu'écrire dans le journal de bord ? | « Cause : droits du dossier. Correctif : `chmod`. Vérifié depuis le PC. » |

> [!WARNING]
> **Les deux erreurs classiques :** (1) **changer plusieurs choses à la fois** « pour voir » ; (2) **ne pas lire le message d'erreur**. Dans neuf cas sur dix, le message (à l'écran ou dans le journal) dit déjà ce qui ne va pas.

## Raisonner par couches

On teste **de bas en haut**. Si une couche basse est en panne, inutile de chercher plus haut.

| Couche | On vérifie | Outil (Linux) | Outil (Windows) |
|---|---|---|---|
| 1. **Machine** | la VM tourne, elle a de la place et de la mémoire | `df -h`, `free -h` | Gestionnaire des tâches |
| 2. **Réseau** | adresse, passerelle, connectivité, nom | `ip a`, `ping`, `ip r` | `ipconfig /all`, `ping` |
| 3. **Nom** | le nom devient la bonne adresse | `getent hosts nom`, `dig nom` | `nslookup nom` |
| 4. **Port / pare-feu** | quelque chose écoute, rien ne bloque | `ss -tlnp`, `curl -v` | `netstat -ano`, `Test-NetConnection` |
| 5. **Service** | le programme tourne, sans erreur | `systemctl status`, `journalctl -u` | `Get-Service`, Observateur d'événements |
| 6. **Configuration** | le fichier est valide et pris en compte | `apache2ctl configtest`, `nginx -t` | outil de gestion du rôle |
| 7. **Droits** | le compte du service a le droit de lire/écrire | `ls -l`, `namei -l`, `id` | onglet Sécurité, `icacls` |
| 8. **Application** | la page, la base, le partage fonctionnent | `curl`, `mysql`, `smbclient` | le client lui-même |

## Où trouver le message d'erreur

1. **À l'écran** : le code ou le texte renvoyé (404, 403, `530 Login incorrect`, `NT_STATUS_ACCESS_DENIED`).
2. **Dans le journal du service** : `/var/log/apache2/error.log`, `/var/log/nginx/error.log`, `/var/log/vsftpd.log`, `journalctl -u nom-du-service`.
3. **Dans le test de configuration** : la commande qui **valide avant de recharger**.

> [!TIP]
> Le réflexe : ouvrir un terminal dédié avec `sudo tail -f /var/log/…` **pendant** que tu refais le test. Le message apparaît en direct.

## Le journal de bord

Pour **chaque** panne, note (voir la [fiche de dépannage](fiche-depannage.md)) : le symptôme, ce que tu as testé, la cause, le correctif, ce qu'il faut faire pour que **ça ne se reproduise pas**. C'est exactement ce que tu devras fournir en entreprise (ticket d'incident) et dans ton dossier de preuves.
