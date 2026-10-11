# S16 – Projet A1 (1/2) : le réseau d'une petite entreprise

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S16 – lundi 17 mai 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S10 à S15 (câblage, IP, DHCP, DNS, Wi-Fi, dépannage) |
| **Référentiel** | C06 · C09 · C10 |

> [!NOTE]
> **Question qui guide le projet :** *« Une petite entreprise ouvre un atelier. Peux-tu lui installer un réseau complet, qui marche et que tu sais expliquer ? »*

## 🎯 Objectifs

1. **Lire** un cahier des charges et en **extraire** les besoins.
2. **Dessiner** le schéma réseau et **construire** le plan d'adressage (/24).
3. **Câbler** (calcul des longueurs, fabrication ou brassage) et **configurer** box, DHCP, imprimante, Wi-Fi invité.
4. **Partager** un dossier et une imprimante avec des **droits adaptés** (Windows, groupe de travail).
5. **Documenter** son travail : le dossier avance séance après séance.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Du besoin au schéma ; plan d'adressage ; droits de partage |
| [📄 Cahier des charges](03-cahier-des-charges.md) | Le sujet du projet (à lire en premier) |
| [🛠️ TP / projet](02-tp.md) | Étapes A à F, grille d'avancement |
| [🧩 Fiche guidée : partage Windows](04-fiche-partage-windows.md) | Comptes, droits, dossier et imprimante |
| [`tp/projet-a1-depart.json`](tp/projet-a1-depart.json) | Simulateur : équipements posés, **ni câblés ni configurés** |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Lancement** : lecture du cahier des charges, questions, formation des binômes ; retour mission entreprise | Classe |
| 0 h 20 – 0 h 50 | **Mini-cours** : du besoin au schéma, plan d'adressage (cours §1–§2) | Classe |
| 0 h 50 – 1 h 40 | **Étapes A–B** : schéma, plan d'adressage, longueurs de câbles | Binôme |
| 1 h 40 – 1 h 55 | Pause | |
| 1 h 55 – 2 h 40 | **Étape C** : maquette dans le simulateur (câbler, configurer) | Binôme |
| 2 h 40 – 3 h 05 | **Mini-cours** : droits de partage (cours §3) | Classe |
| 3 h 05 – 3 h 50 | **Étape D** : partage de dossier et d'imprimante (postes réels) | Binôme |
| 3 h 50 – 4 h 00 | Point d'avancement, grille | Individuel |

## 🧪 Matériel et préparation

- Simulateur avec `tp/projet-a1-depart.json`.
- **Matériel réel (option recommandée)** : 1 box (ou routeur), 1 switch, 4 postes Windows, 1 imprimante réseau, 1 borne Wi-Fi, câbles RJ45 et outillage de sertissage.
- Postes Windows 11 en **groupe de travail**, comptes locaux préparés selon la fiche de partage.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **Suivi par grille d'avancement** | Une grille par binôme, relevée en fin de séance ([TP](02-tp.md)) |
| Contrôle oral court | « Pourquoi cette adresse pour l'imprimante ? Qui a le droit de modifier ? » |

## 🏭 Mission en entreprise

> *Avancer le dossier du projet : compléter le schéma et le tableau d'adressage.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Simulateur** : box (DHCP .10 à .100), imprimante et borne sont posées mais non câblées. Les limites sont à annoncer : **le réseau invité isolé et le partage de fichiers Windows ne sont pas simulés** ; le simulateur vérifie l'adressage, le câblage, le DHCP, le Wi-Fi et l'accès Internet. Le reste se fait sur matériel réel ou se documente.
- **Imprimante** : adresse fixe `192.168.1.150`, hors plage DHCP (la réservation DHCP n'est pas simulée).
- **Wi-Fi invité** : dans le simulateur, la borne porte `ATELIER-INVITES` (WPA2). L'isolation par rapport au réseau interne se montre sur la vraie box.
- **Fiche de partage Windows** : procédure écrite pour **Windows 11** ; les libellés peuvent varier selon la version. À tester avant la séance sur vos postes.
- **Rythme** : certains binômes termineront C avant la pause de 15 h ; ils avancent sur D ou sur le dossier.
- Corrigé : `corriges/seconde/S16-projet-a1-corrige.json` et `S16-corrige.md`.

</details>
