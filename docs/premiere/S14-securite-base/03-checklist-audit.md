# 📝 Checklist d'audit express – 10 points

*Bac Pro CIEL – Première – S14*

Complète la colonne **Avant** au début du TP, puis **Après** à la fin. Mets ✅ (conforme), ❌ (non conforme) ou ❓ (impossible à vérifier).

| # | Point de contrôle | Comment le vérifier | Avant | Après |
|---|---|---|---|---|
| 1 | Mot de passe d'accès privilégié **chiffré** (`enable secret`) | `show running-config` | | |
| 2 | Accès distant en **SSH** seulement (pas Telnet) | `line vty` : `transport input ssh` | | |
| 3 | **Pas de mot de passe par défaut** (cisco, admin…) | Lecture de la configuration, test de connexion | | |
| 4 | **Bannière** d'avertissement | `banner motd` | | |
| 5 | **Ports libres désactivés** | `show interfaces status` | | |
| 6 | **Filtrage** vers le serveur (seul le web) | `show access-lists` | | |
| 7 | Services **inutiles** désactivés sur le serveur | `ss -tlnp` | | |
| 8 | **Mises à jour** appliquées | `apt list --upgradable` | | |
| 9 | **Configuration sauvegardée** (copie hors équipement) | `show startup-config`, fichier daté | | |
| 10 | **Pare-feu** actif sur le serveur | `sudo ufw status` | | |

**Score avant :** ___ / 10  **Score après :** ___ / 10

**Les 3 corrections les plus urgentes, par ordre de priorité, et pourquoi :**

1. ______________________
2. ______________________
3. ______________________
