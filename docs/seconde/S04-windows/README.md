# S04 – Installer et prendre en main Windows

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S04 – lundi 12 octobre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟢 Guidé (pas à pas, binôme) |
| **Prérequis** | S02–S03 : composants d'un PC, démarrage, BIOS / UEFI (ordre de démarrage) |
| **Référentiel** | C09 *Installer / configurer* · C10 *Maintenir* · savoir : systèmes Windows (niveau 2) |

> [!NOTE]
> **Question qui guide toute la séance :** *« Je reçois un PC vide. Que dois-je faire pour le rendre à son utilisateur, prêt à travailler ? »*

## 🎯 Objectifs

À la fin de la séance, l'élève est capable de :

1. **Expliquer** en une phrase le rôle d'un système d'exploitation (avec l'analogie du serveur de restaurant).
2. **Installer** Windows depuis une clé préparée, en suivant une fiche pas à pas, et **dire pourquoi** on fait chaque étape.
3. **Créer** un compte administrateur et un compte utilisateur standard, et **distinguer** leurs droits.
4. **Repérer et corriger** un pilote manquant dans le Gestionnaire de périphériques.
5. **Lancer** Windows Update et **relever** l'identité du poste (version, processeur, mémoire, stockage).
6. **Livrer** un poste « prêt à l'emploi » en validant une checklist.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | Les idées à comprendre, une à la fois, avec des questions pour vérifier la compréhension |
| [🛠️ TP guidé](02-tp.md) | Installation pas à pas + fiche d'identité du PC + checklist de livraison |
| [✅ Checklist « poste prêt à l'emploi »](03-checklist.md) | Document à imprimer et à faire signer par le binôme |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : on montre un PC vide. « Qu'est-ce qui lui manque pour servir ? » Rappel S03 (BIOS, ordre de boot) | Oral, tableau |
| 0 h 20 – 0 h 50 | **Mini-cours 1** : à quoi sert un système d'exploitation ? Les 7 étapes de l'installation (cours §1 et §2) | Cours + questions flash |
| 0 h 50 – 2 h 15 | **TP partie A** : installer Windows (la copie des fichiers dure ~15 min : on en profite pour faire le cours §3) | Binôme, pas à pas |
| 2 h 15 – 2 h 30 | Pause | |
| 2 h 30 – 3 h 15 | **TP parties B et C** : comptes, nom du poste, pilotes, informations système | Binôme |
| 3 h 15 – 3 h 45 | **TP partie D** : Windows Update, logiciels de base, checklist | Binôme |
| 3 h 45 – 4 h 00 | **Vérification de compréhension** : chaque élève explique une étape à l'enseignant ; bilan, Passeport d'autonomie | Individuel, oral |

## 🧪 Matériel et préparation

- Un poste (ou une machine virtuelle) par binôme, **sans données à conserver**.
- Une clé USB d'installation Windows 11 Pro (ou 10) par binôme, ou un ISO monté dans la machine virtuelle.
- Un accès Internet (pour Windows Update).
- Fiches du TP imprimées (ou affichées) + [checklist](03-checklist.md).

## 🧭 Évaluation

| Quoi | Comment | Quand |
|---|---|---|
| Poste « prêt à l'emploi » | Checklist validée par le binôme **puis** par l'enseignant | Fin de séance |
| Compréhension | Oral de 2 min : « explique-moi pourquoi on fait cette étape » (grille ci-dessous) | Fin de séance |
| Passeport d'autonomie | Ligne « Installer un système d'exploitation » : *vu en guidé* | Fin de séance |

| Critère | ✅ Acquis | 🔶 En cours | ❌ À reprendre |
|---|---|---|---|
| Explique le rôle d'un OS avec ses mots | | | |
| Cite 3 étapes de l'installation dans l'ordre | | | |
| Distingue administrateur / utilisateur | | | |
| Sait ce que signifie un triangle jaune | | | |

## 🏭 Mission en entreprise

> *Noter la version de Windows des postes de l'entreprise et l'état des mises à jour ; demander comment un poste neuf est préparé.*

À rapporter en début de S05 sur une demi-page (ou en 5 lignes à l'oral).

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1">
<summary>Points d'attention (cliquer pour déplier)</summary>

- **Compte local à l'installation de Windows 11** : la procédure pour éviter l'obligation d'un compte Microsoft change selon la version de l'ISO. Testez-la **avant** la séance sur l'image utilisée (câble réseau débranché pendant la configuration initiale, puis, selon la version, la commande indiquée dans la fiche TP). En cas de doute, utilisez une image préparée ou une machine virtuelle dont le fichier de réponses crée un compte local.
- **Machine virtuelle** : le réseau en *accès par pont* ou *NAT* suffit pour Windows Update. Prévoir un snapshot « poste vierge » pour recommencer vite.
- **Remédiation** : un élève qui bloque sur la première étape peut observer un binôme plutôt que de rester sans rien faire ; il reprend la main à la partie B.
- **Compréhension** : ne pas se contenter de « ça a marché ». Poser systématiquement *« pourquoi on a fait ça ? »* (voir les questions dans le cours).
- **Après la séance** : remettre les postes en état (snapshot) pour la classe suivante.

</details>
