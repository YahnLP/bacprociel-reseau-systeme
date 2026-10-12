# 📝 Aide-mémoire – Mises à jour et sauvegardes

## Commandes

```text
show running-config        # configuration en cours (RAM)
show startup-config        # configuration enregistrée (NVRAM)
write memory               # enregistrer (= copy running-config startup-config)
show version               # modèle, version, durée de fonctionnement
reload                     # redémarrer
```

Sauvegarde réseau (si disponible) : `copy running-config tftp:` · `copy tftp: running-config`.

## Optimiser

```text
show interfaces status           # ports actifs et libres
interface range fa0/5 - 24       # puis : shutdown   (couper les ports libres)
interface fa0/1                  # puis : description PC-BUREAU
no vlan 30                       # supprimer un VLAN inutilisé
```

Règle : mesurer avant · une modification à la fois · vérifier après · noter · sauvegarder.

## Restaurer

`enable` → `configure terminal` → coller → `end` → `write memory` → vérifier.

## Mise à jour : 5 étapes

Sauvegarder · Noter la version · Notice · Prévenir le client · Mettre à jour · Tester ou revenir en arrière.

## Journal (colonnes)

Date · Équipement · Modification · Pourquoi · Par qui · Fichier de sauvegarde.
