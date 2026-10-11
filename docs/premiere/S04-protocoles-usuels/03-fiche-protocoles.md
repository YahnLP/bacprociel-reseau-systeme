# 📝 Fiche des protocoles + enquête

## Tableau de synthèse (à compléter)

| Protocole | À quoi il sert | Transport | Port(s) | Un message typique |
|---|---|---|---|---|
| **DHCP** | | | | |
| **DNS** | | | | |
| **HTTP** | | | | |
| **HTTPS** | | | | |
| **SSH** | | | | |
| **ICMP** (ping) | | *(pas de port)* | – | |

<details markdown="1"><summary>Correction</summary>

| Protocole | Rôle | Transport | Port(s) | Message |
|---|---|---|---|---|
| DHCP | distribuer adresse, masque, passerelle, DNS | UDP | 67 / 68 | Discover |
| DNS | nom → adresse | UDP (TCP pour gros transferts) | 53 | Standard query A |
| HTTP | page web en clair | TCP | 80 | GET / |
| HTTPS | page web chiffrée | TCP | 443 | (chiffré) |
| SSH | accès distant chiffré | TCP | 22 | – |
| ICMP | tester, signaler une erreur | – (couche IP) | – | Echo request |

</details>

## L'enquête

Pour chaque extrait, **nomme le protocole**, la **couche** et dis **ce qui se passe**.

| N° | Extrait de capture | Protocole ? | Que se passe-t-il ? |
|---|---|---|---|
| 1 | `0.0.0.0 → 255.255.255.255  UDP 68 → 67  Boot Request` | | |
| 2 | `192.168.1.10 → 192.168.1.1  UDP 49497 → 53  Standard query A www.exemple.fr` | | |
| 3 | `192.168.1.10 → 198.51.100.80  TCP 49499 → 80  [SYN]` | | |
| 4 | `198.51.100.80 → 192.168.1.10  HTTP/1.1 404 Not Found` | | |
| 5 | `192.168.1.10 → 198.51.100.80  TCP 49500 → 443  [SYN]` | | |

<details markdown="1"><summary>Correction</summary>

1. **DHCP** (Discover) : un poste sans adresse cherche un serveur ; couche application (sur UDP).
2. **DNS** : le PC demande l'adresse de `www.exemple.fr` à la box (qui relaie).
3. **TCP** : début de connexion (SYN) vers un serveur **web** (port 80).
4. **HTTP** : le serveur répond « page introuvable » (code 404).
5. **TCP** vers le port **443** : début d'une connexion **HTTPS**.

</details>

## Un problème à résoudre

Un collègue dit : « Le ping vers `198.51.100.80` répond, mais la page ne s'ouvre pas dans le navigateur. » Tu captures et tu vois seulement : `SYN` partant du PC, **aucune réponse**.

**À quelle couche cherches-tu ? Quelles hypothèses ?** ______________________

<details markdown="1"><summary>Correction</summary>

Le **ping** (ICMP, couche réseau) marche : le chemin existe. Mais **TCP port 80 ne répond pas** : le **service web** est **arrêté** sur le serveur, ou un **pare-feu** bloque le port 80. On cherche **couche 4 / 7**, pas câble ni IP.

</details>
