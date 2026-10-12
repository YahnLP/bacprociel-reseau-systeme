# Corrigé – Terminale S07

Fichiers : `T07-sauvegarde-corrige.json`, `T07-restauration-corrige.json`.

**Partie A** : `show startup-config` est vide ou affiche « startup-config is not present » : la configuration n'a **jamais** été enregistrée ; un redémarrage la **perd entièrement**.

**Partie B** : `write memory` ; la `startup-config` contient `hostname SW-ATELIER`, `vlan 20`, `enable secret`. Réponse à la question : « le switch ne se souvient que de la *startup-config* ; et si le switch meurt, tout part avec lui ».

**Partie C** : le VLAN 30 a disparu après `reload` car il n'était **que** dans la *running-config*.

**Partie D** : après collage et `write memory`, le VLAN 10/20 existe ; `PC-A` (VLAN 10) ne joint plus `PC-B` (VLAN 20, même réseau IP mais **domaines de diffusion différents**) ; sans `write memory`, un redémarrage effacerait la restauration.

**Partie E (proposition)** : copie 1 sur le **serveur de fichiers** ; copie 2 sur une **clé USB** gardée au bureau du responsable ; copie 3 dans un **espace en ligne** du prestataire. Responsable : le prestataire (nous) + le patron.

**Partie F** : plan attendu : 1) `show version` + sauvegarde ; 2) lire la notice du constructeur ; 3) prévenir le patron, intervenir hors horaires ; 4) mettre à jour, redémarrer ; 5) `show version`, pings, retour à l'ancienne version et restauration si échec.

**Contrôles automatiques** : 4/4 (sauvegarde) et 3/3 (restauration) verts sur les corrigés.


## Partie G – Optimisation (ajout)

Corrigé : `T07-optimisation-corrige.json`. Attendu : `interface range fa0/5 - 24` + `shutdown` ; `description` sur Fa0/1 et Fa0/3 ; `no vlan 30` ; `write memory`. Vérifier que PC-A et PC-B restent séparés. Question du collègue : avant de supprimer un VLAN, vérifier qu'aucun port ne l'utilise (`show vlan brief`), le noter dans le journal, sauvegarder, prévoir le retour arrière.
