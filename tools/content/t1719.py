import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance, w, ROOT

FOLD17 = "S17-evaluation-e31"

# ------------------------------------------------------------------ S17
S17 = dict(
 prerequis="Chantiers d'entraînement S15 et S16 ; fiche « 15 points essentiels »",
 question="Le jour de l'épreuve, que va-t-on regarder chez moi, et comment me donner les meilleures chances de le montrer ?",
 objectifs=["**Connaître** le déroulement et les critères de l'épreuve E31.", "**Conduire** un chantier complet en autonomie (installer, configurer, valider, exploiter).", "**Laisser des preuves** exploitables (captures, commandes, recette, compte rendu).", "**Compléter** son livret avec les preuves de l'évaluation."],
 cours_role="Conseils pour le jour de l'évaluation (avant, pendant, après)",
 tp_role="Sujet type d'entraînement : étude notariale Pasquier (même matériel, autre cahier des charges)",
 memo_role="Check-list du jour J",
 fichiers=[("t17-sujet-depart.json", "Simulateur : sujet type, matériel posé, aucun câble, aucune configuration")],
 autres=[("[📄 Sujet type](03-sujet-type.md)", "Dossier client de l'étude notariale Pasquier"), ("[🧑‍🏫 Organisation (enseignant)](04-organisation-enseignant.md)", "Mise en place, déroulé, éléments à confirmer")],
 deroule=[("0 h 00 – 0 h 20", "**Accueil** : consignes, documents autorisés, rappel des critères", "Classe"), ("0 h 20 – 3 h 20", "**Chantier complet** (3 h) en autonomie, **évalué**", "Individuel"), ("3 h 20 – 4 h 00", "**Entretien** court : justifier ses choix, répondre aux questions", "Individuel")],
 materiel=["Le plateau technique ou le simulateur (selon le dispositif retenu par l'établissement).", "Le **sujet** imprimé, l'aide-mémoire, la fiche « 15 points essentiels », la documentation d'appui autorisée.", "La **grille officielle** de l'épreuve (fournie par l'enseignant)."],
 eval=[("**Positionnement sur la grille nationale officielle** (C06, C09, C10)", "Certificatif, selon le dispositif de l'établissement (CCF ou épreuve ponctuelle)"), ("**Preuves du livret E31**", "Complétées après la séance")],
 notes=["**Cette séance est certificative** : les modalités exactes (**CCF** ou **épreuve ponctuelle**, nombre de situations, commission, calendrier) dépendent du **règlement d'examen** et de la **circulaire de l'établissement**. **À vérifier et à confirmer** avant la séance (voir [Organisation](04-organisation-enseignant.md)). Le plan de formation ne se substitue pas à ces textes.", "**Le sujet type** de ce dossier (étude notariale Pasquier, `t17-sujet-depart.json`) est **fourni à titre d'entraînement** et de sujet de **secours**. Il utilise **le même matériel** que S15 mais **un autre cahier des charges** (autres réseaux, VLAN, SSID, noms) : les élèves ne peuvent pas le dérouler de mémoire.", "**Si l'évaluation se fait sur le plateau physique**, le simulateur peut servir **uniquement** à préparer ou à une situation de rattrapage.", "**Vérification automatique :** 8 contrôles pour l'enseignant (aide au positionnement, pas la note). Corrigé : `corriges/terminale/T17-corrige.md`, `T17-sujet-corrige.json`.", "**Preuves** : demander à l'élève d'**imprimer ou d'enregistrer** ses captures, sa recette, son compte rendu et de les **ajouter à son livret**."],
 corriges_extra=", `T17-sujet-corrige.json`",
 cours_titre="Le jour de l'évaluation",
 sauras=["**savoir ce qui est évalué** ;", "**se préparer** (avant) ;", "**gérer son chantier** (pendant) ;", "**laisser des preuves** (après)."],
 sections=[
  dict(h="Ce qu'on regarde chez moi", q="À ton avis, l'évaluateur regarde-t-il **seulement** si ça marche à la fin ?",
       a="**Non** : il regarde aussi **comment** tu travailles (méthode, sécurité), **ce que tu prouves** (tests, documentation) et **comment tu expliques** tes choix.",
       idee="| Compétence | Ce qu'on peut observer |\n|---|---|\n| **C06** Valider la conformité | tu relèves les besoins, tu écris des **tests**, tu déroules une **recette** |\n| **C09** Installer | tu **prépares**, **câbles proprement**, **configures** |\n| **C10** Exploiter | tu **dépannes avec méthode**, **sauvegardes**, **documentes**, **rends compte** |\n\n> [!NOTE]\n> La **grille officielle** détaille les indicateurs. Utilise-la **avant** pour t'entraîner.",
       c="Tu as terminé la configuration, tout fonctionne, mais tu n'as **rien écrit**. Que risque-t-il de se passer ?",
       r="L'évaluateur **ne peut pas valider** ce qu'il ne voit pas : **tests, recette et compte rendu** sont des **preuves** nécessaires."),
  dict(h="Avant : se préparer", q="La veille, tu ne dors pas, tu relis n'importe quoi. **Est-ce une bonne préparation ?**",
       a="**Non.** Mieux vaut **dormir** et **relire ta fiche** « 15 points essentiels » ainsi que **ta fiche d'erreurs** de S15 et S16.",
       idee="**Avant le jour J :** relire ta **fiche**, refaire **un chantier** (S15/S16 ou le sujet type), vérifier ton **matériel personnel autorisé** (stylo, fiche, calculatrice si autorisée), connaître **les consignes de sécurité**.\n\n**Au début :** lis **tout** le dossier ; liste les exigences ; **planifie** tes 3 heures.",
       c="Tu découvres le sujet. **Que fais-tu pendant les dix premières minutes ?**",
       r="Je **lis tout** le dossier, je **liste** les exigences et j'**écris** mes tests : **je ne touche pas encore** au matériel."),
  dict(h="Pendant : conduire et prouver", q="Tu bloques depuis 20 minutes. **Ta priorité ?**",
       a="Appliquer la **méthode** (échelle des tests), **noter** ce que j'ai essayé, et si besoin **passer à l'étape suivante** pour ne pas perdre tout mon temps.",
       idee="1. **Étapes chronométrées** (voir [S15](../S15-chantier-1/01-cours.md)).\n2. **Preuves au fil de l'eau** : captures, résultats de commande.\n3. **Une correction à la fois**.\n4. **Sauvegarder** régulièrement (`write memory`).\n5. **Recette** et **compte rendu** : **ne pas les sacrifier**.",
       c="Il te reste 15 minutes. La configuration marche presque. Que fais-tu ?",
       r="Je **teste** (ma recette), je **sauvegarde** et je **rédige** mon compte rendu : mieux vaut un travail **prouvé à 90 %** qu'un travail parfait **non documenté**."),
  dict(h="Après : entretien et livret", q="À la fin, l'évaluateur te pose des questions sur ton travail. **Pourquoi ?**",
       a="Pour **vérifier que tu comprends** ce que tu as fait et que tu peux **le justifier**.",
       idee="**Prépare 3 justifications** : **pourquoi** ces VLAN, **pourquoi** cette sécurité, **comment** tu as testé. **Puis** : ajoute **tes preuves** au **livret E31** (recette, compte rendu, captures).",
       c="Pourquoi as-tu séparé les visiteurs des postes du notaire ? Donne **une** phrase.",
       r="« Pour que les visiteurs **ne puissent pas accéder** aux documents du notaire : c'est une exigence de **confidentialité**. »"),
 ],
 retenir=["**On évalue la méthode, les preuves, la justification.**", "**Lis tout, planifie, écris tes tests** avant de toucher au matériel.", "**Prouve au fil de l'eau.**", "**Recette + compte rendu** : ne pas les sacrifier.", "**Justifie** tes choix à l'oral."],
 tp_titre="Chantier d'évaluation (sujet type) : étude notariale Pasquier", tp_format="individuel, **conditions de l'épreuve**", tp_temps="3 h",
 mission="L'**étude notariale Pasquier** s'équipe : tu dois **installer, configurer, valider et documenter** son réseau. Lis le [sujet type](03-sujet-type.md).",
 memo_titre="Check-list du jour J",
 tp="""**Nom :** ____________  **Heure de début :** ______

Ouvre le [simulateur](../../simulateur/simulateur-reseau.html), puis **Ouvre** [`t17-sujet-depart.json`](tp/t17-sujet-depart.json). Lis le [sujet](03-sujet-type.md).

## Étapes à respecter

1. **Étudier** (≈ 20 min) : exigences, plan d'adressage complété, tests écrits.
2. **Préparer et installer** (≈ 60 min) : câblage selon le tableau, étiquettes.
3. **Configurer** (≈ 50 min) : switch, routeur, services, Wi-Fi ; `write memory`.
4. **Tester** (≈ 30 min) : cahier de recette rempli, écarts corrigés.
5. **Documenter** (≈ 20 min) : plan d'adressage final, compte rendu.

## Mes preuves

| Preuve | Où la trouver / où l'ajouter à mon livret |
|---|---|
| Plan d'adressage complété | |
| Cahier de recette rempli | |
| Captures de tests | |
| Compte rendu | |

## Mes trois justifications (pour l'entretien)

1. ______________
2. ______________
3. ______________
""",
 memo="""## La veille

Fiche « 15 points essentiels » relue · fiche d'erreurs relue · sommeil.

## Au début

Lire tout · lister les exigences · plan d'adressage · tests écrits · planning de 3 h.

## Pendant

Câbler → configurer par blocs → tester → corriger → `write memory`. **Preuves au fil de l'eau.**

## À la fin

Recette · compte rendu · sauvegarde · 3 justifications prêtes · preuves ajoutées au livret.
""",
 corrige="""Fichier : `T17-sujet-corrige.json`.

**Plan d'adressage attendu** : `172.16.11.0/24` (Bureaux, VLAN 11), passerelle `.1`, DHCP à partir de `.100`, imprimante `172.16.11.20` ; `172.16.21.0/24` (Visiteurs, VLAN 21), passerelle `.1`, DHCP à partir de `.100`.

**Câblage** : identique à S15 (`R1 gi0/0` → FAI `gi0/2` ; `R1 gi0/1` → `SW1 Fa0/24` ; `PC-SECR` Fa0/1 ; `PC-DENT` Fa0/2 ; `IMP` Fa0/3 ; `AP1` Fa0/10).

**Switch** : VLAN 11 `BUREAUX`, 21 `VISITEURS` ; Fa0/1-3 en VLAN 11 ; Fa0/10 en VLAN 21 ; Fa0/24 trunk ; `enable secret Pasquier#2027`. **Routeur** : sous-interfaces `gi0/1.11` / `.21`, DHCP, route par défaut, NAT en surcharge, ACL `VISITEURS-IN`. **Wi-Fi** : `PASQUIER-VISITEURS`, clé `Visiteurs#2027`.

**Contrôles automatiques** : 8/8 verts.""",
)

SUJET17 = """# 📄 Sujet type – Étude notariale Pasquier

*Terminale – E31 – S17 (sujet d'entraînement ; adaptable)*

## 1. Contexte

L'**étude notariale de Me Pasquier** emménage dans de nouveaux locaux. Elle souhaite un **réseau** pour les bureaux, une **imprimante partagée** et un **Wi-Fi pour les visiteurs**, qui ne doivent **pas** accéder aux postes ni à l'imprimante.

## 2. Exigences du client

| N° | Exigence |
|---|---|
| E1 | Les postes des bureaux reçoivent leur adresse **automatiquement** et accèdent à **Internet**. |
| E2 | L'imprimante est joignable avec une **adresse fixe**. |
| E3 | Les visiteurs disposent d'un **Wi-Fi sécurisé** (WPA2) avec accès à Internet. |
| E4 | Les visiteurs **ne voient pas** l'imprimante ni les postes (confidentialité des dossiers). |
| E5 | Les configurations sont **sauvegardées** et **documentées**. |

## 3. Matériel (même plan de câblage qu'en S15)

| Équipement | Connexion |
|---|---|
| `R1` | `gi0/0` → FAI `gi0/2` ; `gi0/1` → `SW1 Fa0/24` |
| `PC-SECR` | `SW1 Fa0/1` |
| `PC-DENT` (poste du notaire) | `SW1 Fa0/2` |
| `IMP` | `SW1 Fa0/3` |
| `AP1` | `SW1 Fa0/10` |
| `LAP-INV` (portable visiteur) | Wi-Fi |

**Adresse publique :** `203.0.113.3/29` ; passerelle FAI `203.0.113.2` ; DNS `198.51.100.53`.

## 4. Plan d'adressage (imposé)

| Réseau | VLAN | Réseau | Passerelle | DHCP | Fixe |
|---|---|---|---|---|---|
| Bureaux | **11** | `172.16.11.0/24` | `.1` | à partir de `.100` | imprimante `172.16.11.20` |
| Visiteurs | **21** | `172.16.21.0/24` | `.1` | à partir de `.100` | – |

**Noms :** `SW-PASQUIER`, `R-PASQUIER`. **Enable (switch) :** `Pasquier#2027`. **Wi-Fi :** `PASQUIER-VISITEURS`, clé `Visiteurs#2027`, WPA2.

## 5. À remettre

1. Plan d'adressage **complété** (adresses, plages).
2. **Cahier de recette** rempli (au moins 6 tests dont 2 négatifs).
3. **Compte rendu** de l'intervention.
4. Configurations **sauvegardées**.
"""

ORGA17 = """# 🧑‍🏫 Organisation de la séance d'évaluation (enseignant)

> [!WARNING]
> **À confirmer avant la séance** : le dispositif exact (**CCF** ou **épreuve ponctuelle**), le **nombre de situations**, la composition de la **commission**, le **calendrier** et les **documents autorisés** relèvent du **règlement d'examen en vigueur** et de la **circulaire de l'établissement**. Ce document est une **aide à l'organisation**, pas un texte réglementaire.

## Avant

| À faire | Fait |
|---|---|
| Récupérer la **grille nationale officielle** de l'épreuve et la **dernière circulaire** | ☐ |
| Fixer les **dates**, **horaires**, **salles** et **groupes** | ☐ |
| Préparer le **sujet** (ce dossier fournit un **sujet type** et un **sujet de secours**) | ☐ |
| Vérifier le **matériel** (plateau ou simulateur), les **comptes** et les **mots de passe** | ☐ |
| Informer les élèves : documents autorisés, déroulé, critères | ☐ |
| Prévoir une **situation de rattrapage** (voir [S18](../S18-remediation-dossier/README.md)) | ☐ |

## Pendant

- **Observation** de l'élève pendant les 3 heures ; renseigner la **grille officielle** au fil de l'eau.
- **Entretien** de fin : 3 questions de justification (choix de VLAN, de sécurité, de tests).
- **Aucune aide** (sauf incident matériel) ; **noter** toute aide apportée.

## Après

| À faire | Fait |
|---|---|
| **Positionner** l'élève sur la grille (ou transmettre à la commission) | ☐ |
| Demander à l'élève d'**ajouter ses preuves** au livret | ☐ |
| Archiver les **traces** (captures, recette, compte rendu) | ☐ |
| Organiser un **rattrapage** si nécessaire | ☐ |
"""

# ------------------------------------------------------------------ S18
S18 = dict(
 prerequis="S17 (évaluation) ; livret E31 en cours",
 question="Quelles preuves me manquent encore, et comment les obtenir avant la fin de l'année ?",
 objectifs=["**Identifier** les compétences à consolider ou à positionner.", "**Reprendre** un chantier ciblé (ou une seconde situation si elle est prévue).", "**Finaliser** le livret E31 : procès-verbaux, schémas, comptes rendus, mesures.", "**Vérifier** que chaque compétence a au moins une preuve."],
 cours_role="Constituer un livret de preuves : quoi garder, comment l'organiser",
 tp_role="Audit du livret, reprise ciblée, finalisation",
 memo_role="Check-list du livret E31",
 fichiers=[],
 autres=[("[📋 Fiche de suivi du livret](03-fiche-livret.md)", "Tableau des preuves par compétence")],
 deroule=[("0 h 00 – 0 h 30", "**Audit du livret** : preuves présentes / manquantes", "Individuel"), ("0 h 30 – 2 h 00", "**Reprise ciblée** : un atelier (voir S14) ou un chantier de rattrapage", "Individuel / binôme"), ("2 h 00 – 2 h 15", "Pause", ""), ("2 h 15 – 3 h 30", "**Finalisation du livret** (rédaction, mise en forme, vérification)", "Individuel"), ("3 h 30 – 4 h 00", "**Entretien individuel** avec l'enseignant", "Individuel")],
 materiel=["Le **livret E31** de l'élève (papier ou numérique).", "Les **preuves** déjà réalisées : recettes, comptes rendus, schémas, mesures, captures.", "Les ateliers de [S14](../S14-revision-remediation/README.md) ou un nouveau sujet type."],
 eval=[("**Livret E31 complet**", "Chaque compétence est appuyée par au moins une preuve"), ("**Reprise ciblée**", "Positionnement ou consolidation")],
 notes=["**Les élèves sont à des étapes différentes** : certains consolident, d'autres complètent leur livret, d'autres passent une **seconde situation** si elle est prévue par le dispositif. Prévoir plusieurs **postes de travail**.", "**Les preuves venues de l'entreprise** (PFMP) sont à **valider** avec le tuteur ; elles ne doivent contenir **aucune donnée confidentielle** (adresses publiques, mots de passe, noms de clients).", "**Modalités** : voir le dispositif de l'établissement (CCF ou épreuve ponctuelle) ; le livret sert dans les deux cas à **justifier** l'acquisition des compétences.", "Corrigé : `corriges/terminale/T18-corrige.md` (attendus de la fiche de suivi)."],
 cours_titre="Constituer son livret de preuves",
 sauras=["**distinguer** une bonne preuve d'une mauvaise ;", "**classer** ses preuves par compétence ;", "**protéger** les données confidentielles."],
 sections=[
  dict(h="Une preuve, c'est quoi ?", q="Pour montrer que tu sais configurer un VLAN, qu'est-ce qui est **convaincant** : « Je sais le faire » ou une capture de `show vlan brief` avec ton nom et la date ?",
       a="La **capture** : c'est **vérifiable**, **datée**, **liée à une situation**.",
       idee="| Type de preuve | Exemple |\n|---|---|\n| **Procès-verbal** | PV de réception signé |\n| **Schéma** | schéma d'architecture annoté |\n| **Compte rendu** | intervention de dépannage |\n| **Mesure** | rapport de test de câble |\n| **Capture** | `show vlan brief`, `ipconfig` |\n| **Attestation** | du tuteur (PFMP) |\n\nUne bonne preuve est **datée**, **précise**, **liée à une compétence** et **sans donnée confidentielle**.",
       c="Cette preuve est-elle bonne ? « Capture de la page d'accueil du routeur, sans date ni nom. »",
       r="**Insuffisante** : on ne sait ni **quand**, ni **qui**, ni **ce qu'elle prouve**. À compléter avec une **légende**."),
  dict(h="Classer par compétence", q="Tu as 30 documents en vrac. **Comment les retrouver rapidement** ?",
       a="En les **classant par compétence** (C06, C09, C10) avec un **index**.",
       idee="Pour **chaque compétence**, au moins **une** preuve :\n\n| Compétence | Preuves possibles |\n|---|---|\n| **C06** Valider la conformité | cahier de recette, PV |\n| **C09** Installer | schéma de câblage, plan d'adressage, captures de configuration |\n| **C10** Exploiter | compte rendu, tickets, journal, sauvegarde |\n\nUne **fiche de suivi** (voir [la fiche](03-fiche-livret.md)) liste tout.",
       c="Une compétence n'a aucune preuve. **Que fais-tu ?**",
       r="Je cherche une **activité** qui la sollicite (chantier, atelier, PFMP) et **je la réalise** pour produire une preuve."),
  dict(h="Protéger les données", q="Tu veux joindre à ton livret le schéma réseau de ton entreprise de stage. **Qu'est-ce qui pose problème ?**",
       a="Il peut contenir des **informations confidentielles** : adresses publiques, mots de passe, noms de clients.",
       idee="**Avant d'ajouter une preuve de l'entreprise :** **demande l'accord** du tuteur ; **masque** les mots de passe et adresses publiques ; **remplace** le nom du client si besoin.",
       c="Un mot de passe apparaît dans ta capture. **Que fais-tu ?**",
       r="Je le **masque** (rectangle noir) ou je **refais** la capture sans l'afficher."),
 ],
 retenir=["**Une preuve** : datée, précise, liée à une compétence.", "**Classer** par C06, C09, C10.", "**Chaque compétence** a au moins une preuve.", "**Confidentialité** : accord du tuteur, mots de passe masqués."],
 tp_titre="Audit et finalisation du livret", tp_format="individuel", tp_temps="3 h 30",
 mission="Tu fais **l'audit** de ton livret, tu **combles** les manques par une reprise ciblée, puis tu **finalises** le livret E31.",
 memo_titre="Check-list du livret E31",
 tp="""**Nom :** ____________

## Partie A – Audit (≈ 30 min)

Complète la [fiche de suivi](03-fiche-livret.md). Entoure les compétences **sans preuve**.

## Partie B – Reprise ciblée (≈ 90 min)

| Compétence à consolider | Atelier ou chantier choisi | Preuve que je produirai |
|---|---|---|
| | | |
| | | |

Réalise l'activité, **produis la preuve** (capture, compte rendu, recette…).

## Partie C – Finalisation (≈ 75 min)

- [ ] Chaque preuve est **datée** et **légendée**.
- [ ] Les données confidentielles sont **masquées**.
- [ ] Le livret est **classé** par compétence avec un **sommaire**.
- [ ] Les preuves de l'entreprise sont **validées** par le tuteur.

## Partie D – Entretien (≈ 30 min)

Avec l'enseignant : « Montre-moi ta meilleure preuve pour chaque compétence, et explique ce qu'elle prouve. »
""",
 memo="""## Check-list du livret

- [ ] Au moins **une preuve** pour C06, C09, C10.
- [ ] Preuves **datées**, **légendées**, **classées**.
- [ ] **Confidentialité** respectée.
- [ ] **Sommaire** à jour.
- [ ] **Validation** du tuteur pour les preuves PFMP.
""",
 corrige="""Pas de corrigé unique : la séance est individualisée.

**Fiche de suivi attendue** : au moins une preuve par compétence (C06 : recette/PV ; C09 : plan d'adressage, schéma, captures ; C10 : compte rendu, sauvegarde, journal).

**Attention** aux preuves non datées ou contenant des données confidentielles.""",
)
FICHE18 = """# 📋 Fiche de suivi du livret E31

**Élève :** ____________  **Date de mise à jour :** ____________

| Compétence | Preuve (titre) | Type | Date | Situation (S15, S16, S17, PFMP…) | Validée par |
|---|---|---|---|---|---|
| **C06** Valider la conformité | | | | | |
| **C06** | | | | | |
| **C09** Installer | | | | | |
| **C09** | | | | | |
| **C10** Exploiter | | | | | |
| **C10** | | | | | |

**Compétence(s) sans preuve :** ______________________________________

**Plan pour les obtenir :** ______________________________________
"""

# ------------------------------------------------------------------ S19
S19 = dict(
 prerequis="Les trois années de formation",
 question="Qu'ai-je appris en trois ans, de quoi suis-je fier(e), et que veux-je faire ensuite ?",
 objectifs=["**Faire le bilan** de ses compétences réseau sur trois ans.", "**Identifier** ses points forts et ses axes de progrès.", "**Découvrir** des poursuites d'études et des métiers possibles.", "**Préparer** la suite : CV, projet."],
 cours_role="Bilan de compétences, panorama des suites possibles",
 tp_role="Auto-évaluation sur 3 ans, projet personnel, fiche « mon bilan »",
 memo_role="Fiche « mon bilan de formation »",
 fichiers=[],
 autres=[("[🧭 Fiche bilan](03-fiche-bilan.md)", "Bilan de formation à compléter")],
 deroule=[("0 h 00 – 0 h 40", "**Auto-évaluation** à partir du passeport d'autonomie", "Individuel"), ("0 h 40 – 1 h 30", "**Atelier « mon parcours »** : projets, chantiers, PFMP marquants", "Binôme"), ("1 h 30 – 1 h 45", "Pause", ""), ("1 h 45 – 2 h 30", "**Panorama** : poursuite d'études, métiers, insertion", "Classe"), ("2 h 30 – 3 h 30", "**Mon projet** : CV, objectifs, démarches", "Individuel"), ("3 h 30 – 4 h 00", "**Tour de table** : ce que je retiens", "Classe")],
 materiel=["Le **passeport d'autonomie** de l'élève.", "Le **livret E31**.", "Des **brochures** ou sites d'orientation (voir ci-dessous)."],
 eval=[("**Bilan de formation**", "Complété et commenté avec l'enseignant")],
 notes=["**Les informations d'orientation évoluent** (offres de formation, conditions d'admission, calendrier de candidature) : **les vérifier** avant la séance auprès du **psychologue de l'Éducation nationale / CIO**, de l'**Onisep** et des **établissements concernés**. Ce document donne un **panorama général**, **pas une information officielle** à jour.", "**Poursuites d'études possibles** (à titre d'exemples) : **BTS CIEL** (cybersécurité, informatique et réseaux, électronique), autres BTS du numérique, **mentions complémentaires**, **insertion professionnelle**.", "**Ton** : valoriser le **parcours** de chaque élève, même s'il hésite sur la suite.", "Cette séance **ne comporte pas de TP simulateur**."],
 cours_titre="Bilan de formation et suite de parcours",
 sauras=["**nommer** ce que tu sais faire ;", "**identifier** tes points forts et tes progrès ;", "**te projeter** vers une suite."],
 sections=[
  dict(h="Ce que je sais faire aujourd'hui", q="Il y a trois ans, tu n'avais jamais fait de réseau. **Cite trois choses que tu sais faire maintenant.**",
       a="Réponse **personnelle** : par exemple « **câbler** et tester une prise », « **configurer** un switch en VLAN », « **dépanner** avec méthode », « **rédiger** un compte rendu ».",
       idee="**Quatre familles** de ton passeport :\n\n| Famille | Exemples |\n|---|---|\n| **Matériel et câblage** | assembler, câbler, mesurer |\n| **Adresses et services** | IP, DHCP, DNS, Wi-Fi |\n| **Configuration** | VLAN, routage, filtrage, sauvegarde |\n| **Exploitation** | dépanner, documenter, rendre compte |",
       c="Quelle compétence a **le plus progressé** pour toi ? Pourquoi ?",
       r="Réponse **personnelle** : cite un **moment précis** (un chantier, une panne résolue, une PFMP)."),
  dict(h="Mes points forts, mes progrès", q="Dans quelle situation te sens-tu **le plus à l'aise** ? Et **le moins** ?",
       a="Réponse **personnelle** : c'est **ton point de départ** pour la suite (études ou emploi).",
       idee="**Un point fort** se prouve par **un exemple concret**. **Un axe de progrès** se transforme en **action** (« je révise… », « je m'entraîne à… »).",
       c="Transforme ce constat en action : « Je suis lent(e) pour configurer le routage. »",
       r="« Je **refais** le chantier S05 en **chronométrant**, jusqu'à passer **sous X minutes**. »"),
  dict(h="Et après ?", q="Quelles suites connais-tu après un Bac Pro CIEL ?",
       a="**Poursuite d'études** (BTS), **mention complémentaire**, ou **entrée dans la vie active** (technicien réseaux, support).",
       idee="| Voie | Pour qui ? | Où se renseigner ? |\n|---|---|---|\n| **BTS** (par ex. CIEL) | poursuivre en 2 ans après le bac | établissement, plateformes d'orientation |\n| **Mention complémentaire** | se spécialiser en 1 an | établissement, CIO |\n| **Emploi** | commencer à travailler | entreprise d'accueil de PFMP, agences |\n\n> [!WARNING]\n> **Vérifie toujours** les informations (formations offertes, conditions, dates) auprès du **CIO**, de l'**Onisep** et des **établissements** : elles changent.",
       c="Quelles **trois questions** poserais-tu à un lycée qui propose un BTS ?",
       r="Par exemple : **conditions d'admission**, **débouchés après le diplôme**, **organisation** (alternance ou non)."),
 ],
 retenir=["**Je sais** : câbler, configurer, dépanner, documenter.", "**Mes points forts** se prouvent par des exemples.", "**Mes progrès** se transforment en actions.", "**Orientation** : toujours vérifier auprès du CIO et des établissements."],
 tp_titre="Mon bilan de formation", tp_format="individuel et en binôme", tp_temps="3 h 30",
 mission="Tu fais **le bilan de tes trois années** et tu prépares ta **suite de parcours**.",
 memo_titre="Mon bilan de formation",
 tp="""**Nom :** ____________

## Partie A – Mon passeport d'autonomie (≈ 40 min)

Reprends ton [passeport d'autonomie](../../ressources/passeport-autonomie.md) et **entoure** ce que tu maîtrises maintenant.

| Famille | Ce que je sais faire en autonomie | Un exemple concret |
|---|---|---|
| Matériel et câblage | | |
| Adresses et services | | |
| Configuration | | |
| Exploitation | | |

## Partie B – Mon parcours en trois moments (≈ 50 min, en binôme)

Raconte à ton binôme **un moment marquant** de Seconde, de Première et de Terminale :

| Année | Moment marquant | Ce que j'ai appris |
|---|---|---|
| Seconde | | |
| Première | | |
| Terminale | | |

## Partie C – Mon projet (≈ 60 min)

| Question | Ma réponse |
|---|---|
| Qu'est-ce que j'aimerais faire après le bac ? | |
| Ce qui m'attire | |
| Ce qui m'inquiète | |
| Trois questions à poser (lycée, entreprise, CIO) | |
| Prochaine démarche (avec une date) | |

## Partie D – Mon CV (≈ 40 min)

Rédige un **CV d'une page** : formation, stages et chantiers (avec **compétences**), langues, centres d'intérêt.

## Partie E – Tour de table (≈ 30 min)

« **Ce que je retiens** de ces trois ans en une phrase. »
""",
 memo="""## Mon bilan en 5 lignes

1. **Ce que je sais faire** :
2. **Mon point fort** :
3. **Mon axe de progrès** :
4. **Ma suite envisagée** :
5. **Ma prochaine démarche** (date) :
""",
 corrige="""Pas de corrigé : la séance est **personnelle**.

**Attendus** : le passeport est complété avec des **exemples concrets** ; le projet est **réaliste** et accompagné d'une **démarche datée** ; le CV est **lisible** (une page).

**Rappel** : les informations d'orientation sont à **vérifier** auprès du CIO / Onisep / établissements.""",
)
FICHE19 = """# 🧭 Mon bilan de formation

**Nom :** ____________  **Date :** ____________

| Question | Ma réponse |
|---|---|
| Trois choses que je sais faire seul(e) | |
| Mon plus beau chantier (et pourquoi) | |
| Une panne que je suis fier(e) d'avoir résolue | |
| Ce que je ferais différemment | |
| Ce que je veux faire ensuite | |
| Ma prochaine démarche (avec une date) | |

**Avis de l'enseignant :** ______________________________________
"""

if __name__ == "__main__":
    b = seance("S17", S17); w(os.path.join(b, "03-sujet-type.md"), SUJET17); w(os.path.join(b, "04-organisation-enseignant.md"), ORGA17)
    b = seance("S18", S18); w(os.path.join(b, "03-fiche-livret.md"), FICHE18)
    b = seance("S19", S19); w(os.path.join(b, "03-fiche-bilan.md"), FICHE19)
