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

## Restaurer

`enable` → `configure terminal` → coller → `end` → `write memory` → vérifier.

## Mise à jour : 5 étapes

Sauvegarder · Noter la version · Notice · Prévenir le client · Mettre à jour · Tester ou revenir en arrière.

## Journal (colonnes)

Date · Équipement · Modification · Pourquoi · Par qui · Fichier de sauvegarde.
