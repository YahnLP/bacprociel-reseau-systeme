# 🔥 Parcours Stormshield

*Pour aller plus loin – parcours pour les élèves qui terminent leurs TP en avance.*

> [!EXAMPLE] 🚀 Pour aller plus loin
> **Stormshield** est un fabricant français de pare-feux (gamme **SNS**, *Stormshield Network Security*). Ce parcours t'apprend à administrer un pare-feu d'entreprise et prépare au **CSNA** (*Certified Stormshield Network Administrator*). Tu avances **à ton rythme**.

## 🎯 Comment ça marche

1. **Quand ?** Après ton TP de la séance, validé par ton enseignant.
2. **Quoi ?** Des **modules** : un **cours** (avec son quiz) et un **TP** sur le **simulateur réseau** (qui contient un pare-feu Stormshield SN210), ou à défaut sur **Cisco Packet Tracer**, ou sur une **machine virtuelle**.
3. **Où j'en suis ?** Coche tes modules sur la [feuille de route](feuille-de-route.md).
4. **Le vocabulaire** est dans le [glossaire Stormshield](glossaire-stormshield.md) (français + anglais).

## 🧭 Deux façons de le suivre

| Parcours | Modules | Pour qui |
|---|---|---|
| **Découverte** | S01, S04, S05, S06 | Comprendre ce que fait un pare-feu et le configurer |
| **Préparation CSNA** | tous les modules (S01 à S10) + examen blanc | Viser la certification |

> [!NOTE]
> La **certification CSNA** elle-même se passe chez Stormshield (examen payant). Ce parcours t'y **prépare**, il ne la remplace pas. Les cours sont **originaux**, écrits pour ce site ; les documents officiels de Stormshield restent la référence.

## 📚 Les modules

| Module | Contenu | TP |
|---|---|---|
| [S01 · Prise en main du pare-feu](s01-prise-en-main/01-cours.md) | Rôle, interface web, licence, mises à jour, sauvegarde | [🖥️ découvrir l'interface](s01-prise-en-main/02-tp.md) |
| [S02 · Journaux et supervision](s02-journaux-supervision/01-cours.md) | Lire un journal, trouver pourquoi un flux est bloqué | [🖥️ le ping qui ne passe pas](s02-journaux-supervision/02-tp.md) |
| [S03 · Objets](s03-objets/01-cours.md) | Hôtes, réseaux, plages, groupes, services | [exercices + 🧊](s03-objets/02-tp.md) |
| [S04 · Configuration réseau](s04-configuration-reseau/01-cours.md) | Modes de déploiement, interfaces, zones, routage | [🖥️ mettre en réseau un pare-feu](s04-configuration-reseau/02-tp.md) |
| [S05 · NAT](s05-nat/01-cours.md) | Masquerade, redirection, NAT 1:1 | [🖥️ sortir et publier](s05-nat/02-tp.md) |
| [S06 · Filtrage](s06-filtrage/01-cours.md) | Politique, ordre des règles, état des connexions | [🖥️ une politique propre](s06-filtrage/02-tp.md) |
| [S07 · Protection applicative](s07-protection-applicative/01-cours.md) | Filtrage d'URL, antivirus, bac à sable, IPS | [exercices + VM EVA](s07-protection-applicative/02-tp.md) |
| [S08 · Utilisateurs et authentification](s08-utilisateurs-authentification/01-cours.md) | Annuaire, Kerberos, RADIUS, portail captif, SSO | [VM EVA + AD, ou 🧊](s08-utilisateurs-authentification/02-tp.md) |
| [S09 · VPN IPsec](s09-vpn-ipsec/01-cours.md) | Phases, IKEv1/v2, clé pré-partagée, VTI | [🖥️ tunnel IPsec (routeurs Cisco)](s09-vpn-ipsec/02-tp.md) |
| [S10 · VPN SSL](s10-vpn-ssl/01-cours.md) | VPN nomade, mise en service | [VM EVA ou OpenVPN](s10-vpn-ssl/02-tp.md) |
| [S11 · Dépanner un pare-feu](s11-depannage/01-cours.md) | Lire le journal, arbre de décision, fiche réflexe, journal de dépannage | [🖥️ site en panne (simulateur)](s11-depannage/02-tp.md) |
| [📝 Examen blanc](examen-blanc/01-examen.md) | 29 questions sur S01 à S10 | corrigé inclus |

## 🧪 Le matériel de TP

| Outil | Usage |
|---|---|
| **Simulateur du site** (SN210) | Zones, règles ordonnées, NAT, redirections, journal : S02, S04, S05, S06 ; VPN IPsec avec des routeurs Cisco : S09 |
| **Cisco Packet Tracer** (🧊) | Concepts équivalents avec un routeur Cisco (ACL, NAT) quand le simulateur est limité |
| **VM Stormshield EVA** | Vrai système SNS, pour les notions que les simulateurs n'ont pas (objets, utilisateurs, IPS, VPN) : sur demande à l'enseignant |

> [!WARNING]
> **Limites du simulateur** : il n'a ni objets, ni authentification, ni filtrage d'URL, ni antivirus, ni IPS, ni VPN, ni haute disponibilité. Les cours le disent à chaque fois et proposent une alternative.

## 🧭 Sources

Le plan suit les chapitres du programme CSNA : [CSNA (NT-CSNA) – Lifelong Learning Luxembourg](https://www.lifelong-learning.lu/formation/certified-stormshield-network-administrator-nt-/fr), [programme Stormshield Academy](https://www.stormshield.com/fr/besoin-accompagnement/services/stormshield-academy/) et la [documentation officielle SNS](https://documentation.stormshield.eu/SNS/v4/en/Content/User_Configuration_Manual_SNS_v4/Filtering_and_NAT/FILTERING_AND_NAT.htm).
