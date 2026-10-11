# Corrigé – Tableau comparatif Windows / Linux (S05)

*Éléments de correction, à adapter selon ce que les élèves ont réellement observé.*

| Sujet | Windows | Linux |
|---|---|---|
| Démarrage de l'installation | Clé USB / ISO, ordre de démarrage | Idem (ISO dans la VM) |
| Dossier personnel | `C:\Users\nom` | `/home/nom` |
| Chemin | `C:\Users\nom\Documents` (anti-slash) | `/home/nom/Documents` (slash) |
| Lecteurs | Lettres `C:`, `D:` | Un seul arbre à partir de `/` |
| Installer un logiciel | Télécharger un `.exe`, assistant | `apt install` ou *Logiciels* (dépôts officiels) |
| Mises à jour | Windows Update | `apt update` puis `apt upgrade` |
| Droits d'administrateur | Compte administrateur / demande UAC | `sudo` / compte `root` |
| Commandes | Invite de commandes / PowerShell | Terminal (bash) |
| Licence | Payante (incluse avec le PC) | Libre et gratuite |
| Où le trouve-t-on ? | Postes de travail | Serveurs, box, Android, NAS |
