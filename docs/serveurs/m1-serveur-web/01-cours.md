# 📖 Cours – Le serveur web

*Parcours serveurs – module 1*

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer ce que fait un **serveur web** ;
- [ ] comparer **Apache** et **Nginx** ;
- [ ] décrire la pile **LAMP** ;
- [ ] gérer un **service** avec `systemctl` et lire ses **journaux**.

---

## 1. Rôle d'un serveur web

Le navigateur envoie une requête **HTTP** (port **80**) ou **HTTPS** (port **443**) ; le serveur répond avec une page. Le serveur web est un **service** : un programme qui tourne en arrière-plan et écoute sur un port.

## 2. Apache et Nginx

| | **Apache** | **Nginx** |
|---|---|---|
| Paquet Debian | `apache2` | `nginx` |
| Fichiers du site | `/var/www/html` | `/var/www/html` |
| Configuration | `/etc/apache2/` | `/etc/nginx/` |
| Journaux | `/var/log/apache2/` | `/var/log/nginx/` |
| Test de configuration | `apache2ctl configtest` | `nginx -t` |

> [!NOTE]
> Les deux écoutent le port 80 : **un seul à la fois** sur la même machine.

## 3. La pile LAMP

| Lettre | Élément | Rôle |
|---|---|---|
| **L** | Linux | système |
| **A** | Apache | serveur web |
| **M** | MariaDB (ou MySQL) | base de données |
| **P** | PHP | pages dynamiques |

## 4. Gérer un service

| Commande | Effet |
|---|---|
| `systemctl status apache2` | état du service |
| `sudo systemctl start / stop apache2` | démarrer / arrêter |
| `sudo systemctl enable apache2` | démarrer au démarrage |
| `sudo systemctl reload nginx` | recharger la config sans coupure |
| `sudo ss -tlnp` | ports à l'écoute |

> [!WARNING]
> Après chaque modification de configuration, **teste** (`nginx -t`) avant de recharger.

---

## 🧠 Quiz de fin

**1.** Quel port utilise HTTP ? Et HTTPS ?

<details markdown="1"><summary>Voir la réponse</summary>

**80** et **443**.

</details>

**2.** Pourquoi ne peut-on pas lancer Apache et Nginx ensemble sur le port 80 ?

<details markdown="1"><summary>Voir la réponse</summary>

Un port ne peut être ouvert que par **un seul** programme à la fois.

</details>

**3.** Que signifient les quatre lettres de LAMP ?

<details markdown="1"><summary>Voir la réponse</summary>

**L**inux, **A**pache, **M**ariaDB/MySQL, **P**HP.

</details>

**4.** Quelle commande montre quels ports sont à l'écoute ?

<details markdown="1"><summary>Voir la réponse</summary>

`sudo ss -tlnp`.

</details>

➡️ Suite : [le TP du module](02-tp.md).
