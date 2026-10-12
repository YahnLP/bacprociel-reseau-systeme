# S12 – Serveur web et partage de fichiers

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S12 – lundi 8 février 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S10 (serveur Linux, SSH), S11 (DNS) |
| **Référentiel** | C09 · C10 · services web et fichiers (niv. 3) |

> [!NOTE]
> **Question qui guide la séance :** *« L'entreprise veut un intranet que tout le monde ouvre avec un nom, et des dossiers partagés où la Direction ne voit pas l'Atelier. Qui sert la page ? Qui décide des droits ? »*

## 🎯 Objectifs

1. **Expliquer** le dialogue **client / serveur** web (requête, code 200/404, port 80/443).
2. **Publier** un site simple sur un serveur web et le joindre **par son nom**.
3. **Comparer** HTTP et HTTPS dans une capture.
4. **Créer** un partage de fichiers réseau avec **groupes et droits** (Samba).
5. **Accéder** au partage depuis un poste Windows.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Web (HTTP, codes, HTTPS) et partage de fichiers (groupes, droits, SMB) |
| [🛠️ TP](02-tp.md) | Intranet (simulateur) puis partage Samba (VM Ubuntu Server) |
| [📝 Aide-mémoire](03-aide-memoire-web-partage.md) | Codes HTTP, commandes, fichier de partage |
| [`tp/p12-web.json`](tp/p12-web.json) | Simulateur : serveur au nom `intranet.mecapro.local`, service web arrêté |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : `curl` donne « Connection refused » ; retour mission entreprise | Classe |
| 0 h 20 – 0 h 55 | **Mini-cours 1** : HTTP, codes, HTTPS (§1–§2) | Classe |
| 0 h 55 – 1 h 55 | **TP A–D** : intranet, page Direction, HTTP/HTTPS en capture | Binôme |
| 1 h 55 – 2 h 10 | Pause | |
| 2 h 10 – 2 h 40 | **Mini-cours 2** : partage de fichiers, groupes et droits (§3–§4) | Classe |
| 2 h 40 – 3 h 40 | **TP E** : partage Samba + accès depuis Windows | Binôme |
| 3 h 40 – 4 h 00 | **TP F** : fiche de synthèse, bilan | Individuel |

## 🧪 Matériel et préparation

- Simulateur : `tp/p12-web.json`.
- **VM Ubuntu Server** de S10 (réseau : NAT pour `apt` + réseau privé hôte 192.168.56.10), et un poste **Windows** (le PC hôte) pour accéder au partage.
- Prévoir la **connexion Internet** de la VM pour installer Samba (`apt`).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Simulateur : 3 contrôles automatiques** | Page d'accueil, page Direction, HTTPS |
| **Partage Samba** | Vérification par le professeur : un membre de la Direction accède, un membre de l'Atelier est refusé |
| **Fiche de synthèse** | Complétée en fin de séance |

## 🏭 Mission en entreprise

> *Demander **où sont stockés les fichiers** de l'entreprise (serveur, NAS, cloud) et **comment sont gérés les droits** (par service ? par personne ?). **Ne pas ouvrir** de dossiers sans autorisation.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Ce que le simulateur ne fait pas** : il ne simule **pas** de partage de fichiers (SMB/NFS). Le partage est fait en **vraie VM** (Samba). Cette partie **n'a pas été validée en direct** par l'auteur du cours : tester la procédure avant la séance (noms de groupes, `testparm`, accès Windows).
- **Pas de HTML à écrire dans le simulateur ?** Si : l'onglet *Services → Web* contient un éditeur de page. Les élèves écrivent un HTML simple (fourni dans le TP).
- **Windows 11** refuse les accès invités SMB : on utilise un **vrai compte** (`alice`), ce qui est le but pédagogique.
- **Piège Samba** : un utilisateur Samba doit **d'abord exister côté Linux** (`adduser`), puis recevoir un mot de passe Samba (`smbpasswd -a`).
- **Droits** : on travaille avec des **groupes** (principe vu dans le cours §4).
- Corrigés : `corriges/premiere/P12-corrige.md` et `P12-web-corrige.json`.

</details>
