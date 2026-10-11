# Corrigé P10 – Serveur Linux et SSH

## Partie A (simulateur)
PC1→SRV1 : « Délai d'attente de la demande dépassé » ; `tracert` : 1 saut (192.168.10.1) puis `*`. SRV1 : `ip r` n'a pas de ligne `default via` ; `ping` : « Network is unreachable ». Cause : pas de passerelle sur le serveur (route retour). Correction : `ip route add default via 192.168.20.1` → ping OK (TTL 127), tracert 2 sauts (192.168.10.1 puis 192.168.20.100). Fichier `P10-serveur-corrige.json` : SRV1 avec passerelle 192.168.20.1.

## Partie B–F (VM, non testée en direct par l'auteur)
- OpenSSH server coché : permet l'administration à distance dès la fin de l'installation.
- Carte NAT : adresse 10.0.2.x ; carte réseau privé hôte : 192.168.56.x/aucune. Service `sshd` écoute sur `0.0.0.0:22`.
- netplan : `/etc/netplan/60-ciel.yaml` avec `addresses: [192.168.56.10/24]` ; `sudo chmod 600`, `sudo netplan apply`.
- Adresse fixe : un serveur doit toujours être joignable à la même adresse (DNS, pare-feu, supervision en dépendent).
- `sudo whoami` → `root`. Question empreinte : le client vérifie l'identité du serveur (détection d'usurpation).
- Clé privée : `id_ed25519` (jamais copiée). Clé publique collée dans `~/.ssh/authorized_keys` (droits 700/600).
- Durcissement : `/etc/ssh/sshd_config.d/10-ciel.conf` (lu avant `50-cloud-init.conf`).
- Journal : `Accepted publickey for admin1 from 192.168.56.1` et `Failed password`/`Permission denied (publickey)`.
