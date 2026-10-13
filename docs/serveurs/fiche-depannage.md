# 📋 Fiche de dépannage (à imprimer)

*Une fiche par panne. Garde-les dans ton dossier de preuves.*

| Champ | À remplir |
|---|---|
| **Date / machine / service** | |
| **Symptôme observé** (ce que voit l'utilisateur, copie du message exact) | |
| **Depuis quand ? Qu'est-ce qui avait changé ?** | |
| **Périmètre** (qui, depuis où, tout ou partie) | |
| **Hypothèses** (de la plus simple à la plus complexe) | 1. <br> 2. <br> 3. |
| **Tests réalisés** (commande → résultat) | |
| **Message du journal** (copie) | |
| **Cause identifiée** | |
| **Correctif appliqué** (une seule modification à la fois) | |
| **Vérification** (comment je sais que c'est réglé) | |
| **Prévention** (comment éviter que ça revienne) | |

## Aide-mémoire : symptôme → première vérification

| Symptôme | Première chose à regarder |
|---|---|
| « Impossible de se connecter » / *connection refused* | Le service tourne-t-il ? Écoute-t-il (`ss -tlnp`) sur la bonne adresse et le bon port ? |
| « Délai dépassé » / *timeout* | Réseau ou pare-feu : `ping`, route, règle de pare-feu |
| « Nom introuvable » | DNS ou fichier `hosts` |
| Code **403** / *Access denied* | Droits du compte du service sur les fichiers ; règle d'accès |
| Code **404** | Mauvais chemin, mauvais site virtuel, fichier absent |
| Code **500 / 502** | Erreur applicative ou service en amont arrêté : **lire le journal** |
| Le service ne démarre pas | `systemctl status`, `journalctl -u`, test de configuration |
| « Identifiant ou mot de passe incorrect » | Bon compte ? Bonne base d'utilisateurs ? Clavier, verrouillage, mot de passe réinitialisé ? |
| « Ça marchait hier » | Qu'a-t-on changé ? Mise à jour, instantané restauré, espace disque plein, heure décalée |
