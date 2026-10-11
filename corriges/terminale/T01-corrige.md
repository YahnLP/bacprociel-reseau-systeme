# Corrigé – Terminale S01

Installation : `T01-mini-chantier-corrige.json`.

**Câblage** : 4 câbles droits : `PC1` Fa0/1, `PC2` Fa0/2, `IMP` Fa0/3, `SRV` Fa0/4.

**Switch** (exemple) : `hostname SW-CABINET` ; `enable secret …` ; `banner motd #…#` ; `interface range fa0/5 - 24` → `shutdown` ; `write memory`.

**Serveur** : 192.168.1.2/24 ; DHCP : pool `.50` à `.100`, DNS `192.168.1.2`, domaine `martin.local`, exclusion `.1` à `.49` ; DNS : `cabinet.martin.local` → .2 et `imprimante.martin.local` → .20 ; web démarré.

**Imprimante** : 192.168.1.20/24 (hors plage DHCP).

**Contrôles** : les 7 sont verts sur le corrigé.

**Lecture du diagnostic** : un élève qui câble bien mais oublie `write memory` ou l'adresse fixe de l'imprimante → travailler la **recette** ; un élève bloqué sur le DHCP → reprendre S11 de Première.
