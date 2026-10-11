# S14 – Wi-Fi : installer, sécuriser, bons réflexes

| Élément | Détail |
|---|---|
| **Niveau** | Seconde Bac Pro CIEL |
| **Semaine** | S14 – lundi 26 avril 2027 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S12 (DHCP, box), S13 (DNS) ; ondes en physique-chimie ; cyberhygiène (U32) |
| **Référentiel** | C09 · C10 · savoir : bonnes pratiques de sécurité (niveau 2) |

> [!NOTE]
> **Question qui guide la séance :** *« Le Wi-Fi, c'est pratique… et c'est la porte d'entrée la plus facile pour un intrus. Comment l'installer correctement et le sécuriser ? »*

## 🎯 Objectifs

1. **Expliquer** SSID, **bandes 2,4 et 5 GHz**, **canaux**, **portée** et effet des **obstacles**.
2. **Configurer** une borne : SSID, **WPA2/WPA3**, clé forte ; **connecter** un ordinateur et un smartphone.
3. **Mesurer** la couverture avec une application d'analyse et **lire** un niveau de signal (dBm).
4. **Sécuriser** : mot de passe administrateur, **WPS désactivé**, **réseau invité**, mises à jour.
5. **Appliquer** les **bons réflexes** : mots de passe, mises à jour, pare-feu, sauvegarde.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | SSID, bandes, canaux, signal, WPA2/WPA3, invité, bons réflexes |
| [🛠️ TP](02-tp.md) | Cartographie Wi-Fi, borne sécurisée (simulateur), couverture, grille de contrôle |
| [`tp/s14-wifi.json`](tp/s14-wifi.json) | Simulateur : borne d'usine non sécurisée, 3 portables |
| [✅ Grille de contrôle d'une borne](03-grille-controle.md) | À remplir sur la borne réelle (évaluation) |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : *« Combien de Wi-Fi voyez-vous dans la salle ? »* (tous sortent leur téléphone) ; retour mission entreprise | Oral |
| 0 h 20 – 0 h 55 | **Mini-cours 1** : SSID, bandes, canaux, signal (cours §1–§2) | Classe |
| 0 h 55 – 1 h 40 | **TP A** : cartographier les Wi-Fi de la salle avec l'application d'analyse | Binôme |
| 1 h 40 – 1 h 55 | Pause | |
| 1 h 55 – 2 h 20 | **Mini-cours 2** : WPA2/WPA3, invité, WPS (§3–§4) | Classe |
| 2 h 20 – 3 h 05 | **TP B** : sécuriser la borne et connecter les portables (simulateur) | Binôme |
| 3 h 05 – 3 h 50 | **TP C–D** : borne réelle (grille), couverture, bons réflexes | Binôme |
| 3 h 50 – 4 h 00 | Bilan, passeport | |

## 🧪 Matériel et préparation

- **Une borne Wi-Fi ou une box par binôme** (remise à zéro) **ou** une borne démonstration pour la classe.
- **Smartphones** des élèves avec une application d'analyse Wi-Fi (installer **avant** la séance : *WiFiman*, *Wi-Fi Analyzer*, *NetSpot*, selon le système).
- Simulateur avec `tp/s14-wifi.json`.

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **TP : borne configurée et sécurisée** | [Grille de contrôle](03-grille-controle.md) (formatif noté) |
| Oral | « Pourquoi WPA2 ? À quoi sert un réseau invité ? Pourquoi désactiver le WPS ? » |

## 🏭 Mission en entreprise

> *Relever le nom du Wi-Fi de l'entreprise et son type de sécurité (interne / invités). **Ne jamais relever les mots de passe.***

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Simulateur** : la borne règle SSID, clé et sécurité (Ouvert / WPA2 / WPA3). Bandes, canaux, WPS, réseau invité **ne sont pas simulés** : ils sont vus avec l'application d'analyse et la borne réelle.
- **Respect de la vie privée** : l'analyse Wi-Fi montre les réseaux des voisins ; ne relever ni mots de passe ni identifiants. Rappeler le **cadre légal** : on n'essaie jamais de se connecter à un réseau qui n'est pas le sien.
- **Mots de passe** : une phrase de passe (4 mots + chiffre) est préférable à `P@ssw0rd`.
- La clé donnée dans le corrigé du simulateur est *Atelier-Ciel#2027* ; les élèves choisissent la leur (≥ 12 caractères).
- Corrigé : `corriges/seconde/S14-corrige.md` et `S14-wifi-corrige.json`.

</details>
