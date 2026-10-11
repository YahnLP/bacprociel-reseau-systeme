# Corrigé – Terminale S11

Fichiers : `T11-panne-a-corrige.json`, `T11-panne-b-corrige.json`, `T11-panne-c-corrige.json`.

**Atelier A** — Cause 1 : `Fa0/3` en `shutdown` → `no shutdown`. Cause 2 : passerelle de `PC-COM` = `192.168.20.254` au lieu de `192.168.20.1`. Piège : après avoir réactivé le port, le poste est « connecté » mais ne joint toujours pas le serveur.

**Atelier B** — Cause 1 : `Fa0/1` dans le VLAN 30 (le poste reçoit `169.254.x.x`, pas de pool DHCP pour le VLAN 30) → `switchport access vlan 10`, puis `ipconfig /renew`. Cause 2 : enregistrement DNS `intranet.delmas.local` → `192.168.30.11` au lieu de `192.168.30.10`.

**Atelier C** — Cause 1 : sous-interface `gi0/0.20` en `shutdown` (l'atelier n'a plus de passerelle) → `no shutdown`. Cause 2 : pool DHCP `BUREAU` sans `dns-server 192.168.30.10` → ajouter, puis `ipconfig /renew` sur `PC-CPT`.

**Contrôles automatiques** : 4/4 verts sur les trois corrigés.
