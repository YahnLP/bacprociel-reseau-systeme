# Corrigé P12 – Web et partage de fichiers

## Partie A
`ping intranet…` : répond (nom résolu → 192.168.10.2) ; `curl` : « Failed to connect: Connection refused » : le nom est résolu, la machine répond, mais **aucun service n'écoute sur le port 80** (service web arrêté).

## Partie B
Page par défaut du serveur, code 200. `/absente.html` : « 404 Not Found » (le serveur web répond, c'est la page qui manque), contrairement à « Connexion refusée » (service arrêté).

## Partie C
Page d'accueil + `/direction.html` publiées ; PC2 les affiche (200).

## Partie D
HTTP : le contenu HTML est visible dans la capture. HTTPS : Client Hello, Server Hello, Certificate, Key Exchange, Change Cipher Spec, puis Application Data ; contenu illisible. Ports 80 / 443. Mot de passe en HTTP : il circule en clair.

## Partie E (VM, non testée en direct par l'auteur)
`drwxrws---` : propriétaire root (rwx), groupe (rwx + bit setgid « s » : les nouveaux fichiers héritent du groupe), autres rien. Seuls les membres du groupe `direction` (et root) entrent. Accès : alice → direction OK / atelier refusé ; carl → atelier OK / direction refusé. Groupes : gestion en un seul endroit, arrivée/départ simples.

## Contrôles automatiques (P12-web-corrige.json)
3 contrôles : page d'accueil (200), `/direction.html` (200), HTTPS.
