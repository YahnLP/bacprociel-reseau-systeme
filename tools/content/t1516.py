import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance, w, ROOT

GRILLE = """# 📊 Grille d'entraînement (à blanc)

> [!NOTE]
> Cette grille est une **grille d'entraînement**, inspirée de la logique de la grille nationale de l'épreuve E31. **L'évaluation certificative** utilise la **grille officielle** de l'épreuve (voir [S17](../S17-evaluation-e31/README.md)).

**Élève :** ____________  **Date :** ____________  **Scénario :** ____________

Niveaux : **0** non réalisé · **1** réalisé avec aide importante · **2** réalisé avec aide ponctuelle · **3** réalisé seul · **4** réalisé seul **et justifié**.

| Compétence | Indicateur observable | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| **C06** Valider la conformité | Relève les besoins du dossier (liste écrite) | ☐ | ☐ | ☐ | ☐ | ☐ |
| | Écrit des **tests** (dont négatifs) avant de configurer | ☐ | ☐ | ☐ | ☐ | ☐ |
| | Déroule la **recette** et note les écarts | ☐ | ☐ | ☐ | ☐ | ☐ |
| **C09** Installer | Prépare matériel et plan d'adressage | ☐ | ☐ | ☐ | ☐ | ☐ |
| | Câble proprement et **étiquette** | ☐ | ☐ | ☐ | ☐ | ☐ |
| | Configure les équipements (VLAN, routage, services, Wi-Fi) | ☐ | ☐ | ☐ | ☐ | ☐ |
| **C10** Exploiter | Applique une **démarche** de dépannage | ☐ | ☐ | ☐ | ☐ | ☐ |
| | **Sauvegarde** et documente (journal, schéma) | ☐ | ☐ | ☐ | ☐ | ☐ |
| | Rédige un **compte rendu** exploitable | ☐ | ☐ | ☐ | ☐ | ☐ |
| **Attitude** | Respecte les règles de sécurité, gère son temps | ☐ | ☐ | ☐ | ☐ | ☐ |

**Points forts :** ______________________________________

**Points à travailler (fiche d'erreurs) :** ______________________________________
"""

def grille(code, folder):
    w(os.path.join(ROOT, "docs", "terminale", folder, "04-grille-entrainement.md"), GRILLE)

# ---------------- S15
S15 = dict(
 prerequis="Tout le parcours Terminale S01–S14 ; fiche « 15 points essentiels » (S14)",
 question="Suis-je capable de mener un chantier complet, seul(e), dans les conditions de l'épreuve ?",
 objectifs=["**Conduire** un chantier complet en **3 heures** : étudier, préparer, installer, configurer, tester, documenter.", "**Justifier** ses choix (adressage, VLAN, sécurité).", "**Rédiger** une recette et un compte rendu.", "**Se positionner** sur la grille d'entraînement et **identifier** ses erreurs."],
 cours_role="Méthode pour réussir un chantier (gestion du temps, preuves, check-list)",
 tp_role="Cabinet dentaire Vidal : chantier complet depuis une installation vierge",
 memo_role="Check-list de chantier et de preuves",
 fichiers=[("t15-chantier-depart.json", "Simulateur : matériel posé, aucun câble, aucune configuration")],
 autres=[("[📄 Dossier client](03-dossier-client.md)", "Cahier des charges et plan d'adressage à compléter"), ("[📊 Grille d'entraînement](04-grille-entrainement.md)", "Grille à blanc (auto-évaluation et évaluation)")],
 deroule=[("0 h 00 – 0 h 20", "**Briefing** : règles, documents autorisés, critères", "Classe"), ("0 h 20 – 3 h 20", "**Chantier** (3 h) en autonomie, **sans aide** de l'enseignant (une « question jokers » possible)", "Individuel"), ("3 h 20 – 4 h 00", "**Correction collective** et fiche d'erreurs individuelle", "Classe / individuel")],
 materiel=["Le fichier `t15-chantier-depart.json` (ouvert au départ).", "Le **dossier client** imprimé, l'aide-mémoire, la **fiche « 15 points essentiels »** (si autorisée), la documentation d'appui (fiches mémo, documentation constructeur).", "Un chronomètre visible de la classe."],
 eval=[("**Simulateur : 8 contrôles automatiques**", "Formatif ; sert de preuve de réalisation"), ("**Grille d'entraînement** + **recette** + **compte rendu**", "Positionnement à blanc, sans note certificative")],
 notes=["**Conditions de l'épreuve** : **seul(e)**, **3 h**, documentation d'appui **autorisée**. L'enseignant observe et remplit la grille ; il n'aide pas (une question « joker » est tolérée pour débloquer).", "**Correction automatique :** les 8 contrôles du simulateur renseignent sur la **réalisation technique** ; ils ne remplacent pas l'évaluation de la **démarche** et des **preuves écrites**.", "**Solution de référence** : `corriges/terminale/T15-corrige.md` et `T15-chantier-corrige.json`. Le **filtrage patients** est réalisé par une **ACL** sur la sous-interface du VLAN 20.", "**Piège possible** : une ACL terminée par `deny ip any any` **sans** `permit udp any eq 68 any eq 67` empêche les patients d'obtenir une **adresse** (le DHCP est bloqué). La solution de référence autorise le DHCP et laisse passer le reste ; à signaler lors de la correction si un élève a choisi un `deny` final.", "**Dossier** : le plan d'adressage est **à compléter** par l'élève (partie du travail évalué)."],
 corriges_extra=", `T15-chantier-corrige.json`",
 cours_titre="Réussir un chantier complet",
 sauras=["**organiser** ses 3 heures ;", "**prouver** ce qu'on fait ;", "**ne pas bloquer** sur une étape."],
 sections=[
  dict(h="Un chantier, c'est du temps à répartir", q="Tu as 3 heures. Tu passes 1 h 30 à configurer le Wi-Fi parfaitement. **Quel est le risque ?**",
       a="Tu n'auras **pas le temps** de tester, documenter et rédiger la recette : or **l'évaluateur regarde aussi ces traces**.",
       idee="![Répartir 3 heures](images/chantier-3h.svg)\n\n**Chaque étape se termine par une preuve :** capture d'écran, résultat de commande, ligne de compte rendu.",
       c="À la 2ᵉ heure, tu es en retard de 15 minutes sur le câblage. **Que fais-tu ?**",
       r="Je **finis le câblage proprement** (c'est la base), je **note le retard** et j'**enchaîne** : la configuration en dépend. Je rattrape en **documentant au fil de l'eau**."),
  dict(h="Je commence par le dossier", q="Un dossier de chantier contient un **cahier des charges** de 12 lignes. Combien de minutes pour le lire ? Qu'en tires-tu ?",
       a="**10 à 15 minutes** : je **surligne chaque exigence** et j'en fais une **liste de tests**. Cette liste devient mon **cahier de recette**.",
       idee="1. Je **lis** tout le dossier.\n2. Je **liste** les exigences (« les patients ont Internet », « les patients ne voient pas l'imprimante »…).\n3. Je **complète le plan d'adressage** (réseaux, plages, adresses fixes).\n4. Je **déduis les tests** (dont les **négatifs**).\n5. Je **prépare** : matériel, étiquettes, ordre des commandes.",
       c="L'exigence est : « les patients ne doivent pas voir l'imprimante ». **Quel test écris-tu ?**",
       r="Un test **négatif** : depuis le Wi-Fi patients, **ping de l'imprimante**, **attendu : aucune réponse**."),
  dict(h="Si je bloque", q="Ton poste n'a pas d'adresse `192.168.20.x` en Wi-Fi alors que tout semble bien configuré. **Que fais-tu ?**",
       a="Je **monte l'échelle des tests** : lien Wi-Fi associé ? bon SSID/clé ? bon VLAN ? **DHCP joignable** ? **ACL** qui bloque le DHCP ?",
       idee="> **Quand je bloque : je n'essaie pas au hasard. J'applique la méthode (S11).**\n\nUne **ACL** qui se termine par `deny ip any any` bloque aussi le **DHCP** : il faut alors autoriser `udp any eq 68 any eq 67`.",
       c="Une ACL se termine par `deny ip any any`. Les patients n'ont plus d'adresse. **Quelle règle manque-t-il ?**",
       r="`permit udp any eq 68 any eq 67` : elle laisse passer les demandes **DHCP** des clients vers le serveur."),
 ],
 retenir=["**3 h = 6 étapes chronométrées.**", "**Le dossier donne les tests.**", "**Chaque étape laisse une preuve.**", "**Bloqué ? méthode, pas hasard.**", "**Documenter au fil de l'eau.**"],
 tp_titre="Chantier n°1 : le cabinet dentaire Vidal", tp_format="individuel, **en autonomie**, conditions de l'épreuve", tp_temps="3 h",
 mission="Tu es technicien. Le **cabinet dentaire du Dr Vidal** s'équipe : tu dois **installer et configurer** son réseau et son Wi-Fi patients, **tester**, **documenter** et **rendre compte**. Le dossier client est dans [le document dédié](03-dossier-client.md).",
 memo_titre="Check-list de chantier",
 tp="""**Nom :** ____________  **Heure de début :** ______

Ouvre le [simulateur](../../simulateur/simulateur-reseau.html), puis **Ouvre** [`t15-chantier-depart.json`](tp/t15-chantier-depart.json). Lis le [dossier client](03-dossier-client.md).

## Étape 1 – Étudier (≈ 20 min)

- [ ] J'ai listé les **exigences** du client.
- [ ] J'ai complété le **plan d'adressage** du dossier.
- [ ] J'ai écrit **au moins six tests** (dont **deux négatifs**) dans le cahier de recette (partie 6).

## Étape 2 – Préparer et installer (≈ 60 min)

- [ ] J'ai **câblé** (le tableau de câblage du dossier fait foi).
- [ ] Les **voyants/liens** sont verts.
- [ ] J'ai noté mes **étiquettes** (partie 4 du dossier).

## Étape 3 – Configurer (≈ 50 min)

- [ ] Switch : VLAN, ports, trunk, mot de passe, `write memory`.
- [ ] Routeur : sous-interfaces, DHCP, NAT, ACL patients, `write memory`.
- [ ] Imprimante : adresse fixe.
- [ ] Borne Wi-Fi et portable patient : SSID et clé.

## Étape 4 – Tester et corriger (≈ 30 min)

Remplis le **cahier de recette** (partie 6 du dossier) avec les **résultats obtenus**. Corrige les écarts, **refais** les tests.

## Étape 5 – Documenter et rendre compte (≈ 20 min)

- [ ] Plan d'adressage final, schéma simple.
- [ ] **Compte rendu** de 8 lignes (partie 7 du dossier).

**Heure de fin :** ______  **Durée :** ______

## Après le chantier : ma fiche d'erreurs

| Ce qui m'a fait perdre du temps | Ce que je ferai la prochaine fois |
|---|---|
| | |
| | |
""",
 memo="""## Avant de commencer

Dossier lu · exigences listées · plan d'adressage complété · tests écrits.

## Pendant

Câbler → étiqueter → configurer par **blocs** (switch, routeur, services, Wi-Fi) → **tester après chaque bloc** → `write memory`.

## À la fin

Recette remplie · réserves notées · plan d'adressage final · compte rendu · sauvegarde.

## Pièges fréquents

- Oublier `write memory`.
- Oublier `no shutdown` (interface physique du routeur).
- ACL qui bloque le DHCP.
- Passerelle erronée.
- Test négatif non fait.
""",
 corrige="""Fichiers : `T15-chantier-corrige.json`.

**Plan d'adressage attendu** : `192.168.10.0/24` (Soins), passerelle `.1`, DHCP à partir de `.50` (exclusion `.1`–`.49`), imprimante `192.168.10.20` ; `192.168.20.0/24` (Patients), passerelle `.1`, DHCP à partir de `.10` ; WAN `203.0.113.3/29` (passerelle FAI `203.0.113.2`).

**Câblage** : `R1 gi0/0` → FAI `gi0/2` ; `R1 gi0/1` → `SW1 Fa0/24` ; `PC-SECR` Fa0/1 ; `PC-DENT` Fa0/2 ; `IMP` Fa0/3 ; `AP1` Fa0/10.

**Switch** : VLAN 10 `SOINS`, 20 `PATIENTS` ; Fa0/1-3 VLAN 10 ; Fa0/10 VLAN 20 ; Fa0/24 trunk ; `enable secret` ; `write memory`.

**Routeur** : `gi0/0` WAN avec `ip nat outside` ; sous-interfaces `gi0/1.10` / `.20` ; DHCP (`dns-server 198.51.100.53`) ; route par défaut vers `203.0.113.2` ; NAT en surcharge ; ACL `PATIENTS-IN` (autorise UDP 68→67, interdit le VLAN 10, autorise le reste) posée `in` sur `gi0/1.20` ; `write memory`.

**Wi-Fi** : SSID `VIDAL-PATIENTS`, clé `Patients#2027`, WPA2.

**Contrôles automatiques** : 8/8 verts.""",
)

DOSSIER15 = """# 📄 Dossier client – Cabinet dentaire Vidal

*Terminale – E31 – S15 (chantier d'entraînement n°1)*

## 1. Contexte

Le **Dr Vidal** ouvre un cabinet dentaire. Il souhaite un **réseau fiable** pour le secrétariat et le cabinet de soins, une **imprimante partagée** et un **Wi-Fi pour ses patients**, qui ne doivent **pas** accéder à l'imprimante ni aux postes du cabinet.

## 2. Exigences du client

| N° | Exigence |
|---|---|
| E1 | Les postes du secrétariat et du cabinet reçoivent leur adresse **automatiquement** et accèdent à **Internet**. |
| E2 | L'imprimante est joignable par les postes du cabinet, avec une **adresse fixe**. |
| E3 | Les patients disposent d'un **Wi-Fi sécurisé** (WPA2) avec accès à Internet. |
| E4 | Les patients **ne voient pas** l'imprimante ni les postes. |
| E5 | La configuration est **sauvegardée** et **documentée**. |

## 3. Matériel et schéma (à câbler)

| Équipement | Rôle | Connexion |
|---|---|---|
| `R1` (routeur) | Passerelle, DHCP, NAT, filtrage | `gi0/0` → FAI `gi0/2` ; `gi0/1` → `SW1 Fa0/24` |
| `SW1` (switch 24 ports) | Distribution | – |
| `PC-SECR` | Poste du secrétariat | `SW1 Fa0/1` |
| `PC-DENT` | Poste du cabinet | `SW1 Fa0/2` |
| `IMP` | Imprimante | `SW1 Fa0/3` |
| `AP1` | Borne Wi-Fi | `SW1 Fa0/10` |
| `LAP-INV` | Portable d'un patient | Wi-Fi `VIDAL-PATIENTS` |

**Adresse publique du routeur :** `203.0.113.3/29` ; passerelle du FAI : `203.0.113.2`. **DNS du FAI :** `198.51.100.53`.

## 4. Plan d'adressage (à compléter)

| Réseau | VLAN | Adresse réseau / masque | Passerelle | Plage DHCP | Adresses fixes |
|---|---|---|---|---|---|
| Soins | 10 | | | | Imprimante : |
| Patients | 20 | | | | – |

**Noms :** switch `SW-VIDAL`, routeur `R-VIDAL`. **Mot de passe `enable` du switch :** `Vidal#2027`. **Wi-Fi :** SSID `VIDAL-PATIENTS`, clé `Patients#2027`, WPA2.

> [!NOTE]
> Étiquettes à noter : ______________________________________

## 5. Contraintes

- Si l'ACL des patients se termine par un `deny ip any any`, elle doit **laisser passer le DHCP** (UDP 68 vers 67).
- Les configurations des **deux équipements** sont **sauvegardées**.
- Aucune adresse n'est fournie à l'avance pour les postes : **DHCP**.

## 6. Cahier de recette (à remplir)

| N° | Exigence | Test | Attendu | Obtenu | Statut |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

## 7. Compte rendu (8 lignes)

Contexte · Ce qui a été installé · Configuration (VLAN, DHCP, NAT, ACL, Wi-Fi) · Tests réalisés · Écarts et corrections · Documents remis · À suivre · Durée.
"""

# ---------------- S16
S16 = dict(S15)
S16.update(dict(
 prerequis="S15 (chantier n°1) ; fiche d'erreurs de S15",
 question="Suis-je capable, à la fois, de dépanner et de rendre compte, comme à l'épreuve ?",
 objectifs=["**Diagnostiquer** une installation existante tombée en panne (plusieurs causes).", "**Corriger** avec méthode et **prouver** le retour à la normale.", "**Rédiger** un compte rendu d'intervention.", "**Se positionner** sur la grille et **bâtir un plan de travail individuel**."],
 cours_role="Méthode pour un chantier de dépannage ; corriger sa fiche d'erreurs de S15",
 tp_role="Le cabinet Vidal rappelle : plusieurs pannes à diagnostiquer",
 memo_role="Check-list de dépannage et de compte rendu",
 fichiers=[("t16-chantier-depart.json", "Simulateur : l'installation de S15, en panne")],
 autres=[("[📄 Dossier de la demande](03-dossier-rappel.md)", "Appel du client et attentes"), ("[📊 Grille d'entraînement](04-grille-entrainement.md)", "Grille à blanc")],
 deroule=[("0 h 00 – 0 h 20", "**Briefing** et rappel des erreurs fréquentes de S15", "Classe"), ("0 h 20 – 3 h 20", "**Chantier de dépannage** (3 h) en autonomie, avec **compte rendu**", "Individuel"), ("3 h 20 – 4 h 00", "**Correction** et **plan de travail individuel**", "Classe / individuel")],
 materiel=["Le fichier `t16-chantier-depart.json`.", "Le **dossier de la demande** imprimé, l'aide-mémoire, la fiche « 15 points essentiels », la documentation d'appui.", "Les **fiches d'erreurs** de S15."],
 eval=[("**Simulateur : 8 contrôles automatiques**", "Formatif ; preuve de dépannage"), ("**Compte rendu** + **grille d'entraînement**", "Positionnement à blanc")],
 notes=["**Trois causes** : 1) le port de l'imprimante (`Fa0/3`) a été déplacé dans le VLAN 20 ; 2) la clé Wi-Fi du portable patient est erronée (`Patient#2027` au lieu de `Patients#2027`) ; 3) la liste d'accès du NAT ne couvre plus que le VLAN 10 : les patients n'ont **pas Internet** même une fois connectés. Le 3ᵉ défaut n'apparaît **qu'après** la correction du 2ᵉ : **c'est le piège** de la double panne.", "**Corrigé** : `corriges/terminale/T16-corrige.md`, `T16-chantier-corrige.json`.", "**Plan de travail individuel** : à partir de la grille et de la fiche d'erreurs, **trois points** à retravailler avant S17.", "**Conditions de l'épreuve** : seul(e), 3 h, documentation d'appui, comme S15."],
 corriges_extra=", `T16-chantier-corrige.json`",
 cours_titre="Un chantier de dépannage",
 sauras=["**rassembler** les indices ;", "**ne pas** s'arrêter à la première cause ;", "**rendre compte** clairement."],
 tp_titre="Chantier n°2 : le cabinet Vidal rappelle", tp_format="individuel, **en autonomie**, conditions de l'épreuve",
 mission="Trois mois après l'installation, le **cabinet Vidal** vous rappelle : plusieurs choses ne fonctionnent plus. Tu **diagnostiques**, tu **corriges**, tu **prouves** le retour à la normale et tu **rédiges le compte rendu**. Lis [la demande](03-dossier-rappel.md).",
 memo_titre="Check-list de dépannage et de compte rendu",
))
S16["sections"] = [
  dict(h="Collecter les indices avant d'agir", q="Le client dit « rien ne marche ». **Quelle est ta première action ?**",
       a="**Préciser** : quoi, qui, depuis quand ? Je **reproduis** le problème et je note **ce qui marche encore**.",
       idee="| Question | Pourquoi |\n|---|---|\n| Qu'est-ce qui ne marche **plus** ? | précise le symptôme |\n| Qu'est-ce qui marche **encore** ? | élimine des causes |\n| Depuis **quand** ? | relie à un changement |\n| **Qu'a-t-on changé** récemment ? | première piste |",
       c="L'imprimante ne répond plus, **mais** les postes ont Internet. Que déduis-tu ?",
       r="Le **réseau général** (routeur, DHCP, NAT) fonctionne : je cherche **autour de l'imprimante** (port, VLAN, adresse, câble)."),
  dict(h="Une panne peut en cacher une autre", q="Tu corriges la clé Wi-Fi : le patient se connecte et a une adresse, mais **n'ouvre toujours pas** un site. **Est-ce que ta correction était fausse ?**",
       a="**Non** : elle était **juste** mais il y a **une deuxième panne** derrière (ici, le NAT).",
       idee="> **Après chaque correction, je reprends l'échelle des tests du début.**\n\n![Répartir 3 heures](images/chantier-3h.svg)",
       c="Comment sais-tu que **tout** est réparé ?",
       r="Quand **tous** les tests de mon cahier de recette (positifs **et** négatifs) sont **conformes**."),
  dict(h="Le compte rendu : écrire pour être utile", q="Que doit pouvoir faire un collègue qui lit ton compte rendu **sans** t'avoir vu travailler ?",
       a="**Comprendre** ce qui s'est passé, ce que tu as changé et ce qui reste à surveiller, **sans te rappeler**.",
       idee="Contexte · symptôme · diagnostic · causes (**toutes**) · actions · résultat · à suivre · durée. **Un exemple complet** : [S12](../S12-depanner-2/01-cours.md).",
       c="Ton compte rendu dit « problème réglé ». **Que lui manque-t-il ?**",
       r="Les **causes**, les **actions** précises et les **tests** qui prouvent le retour à la normale."),
]
S16["retenir"] = ["**Indices d'abord**, actions ensuite.", "**Une panne peut en cacher une autre.**", "**Tous les tests verts** = fini.", "**Compte rendu** : causes + actions + résultat.", "**Plan de travail individuel** après chaque chantier."]
S16["tp"] = """**Nom :** ____________  **Heure de début :** ______

Ouvre le [simulateur](../../simulateur/simulateur-reseau.html), puis **Ouvre** [`t16-chantier-depart.json`](tp/t16-chantier-depart.json). Lis la [demande du client](03-dossier-rappel.md).

## Étape 1 – Collecter les indices (≈ 20 min)

| Question | Réponse |
|---|---|
| Qu'est-ce qui ne marche plus ? | |
| Qu'est-ce qui marche encore ? | |
| Que dit le client sur les changements récents ? | |
| Mes **hypothèses** (au moins quatre) | |

## Étape 2 – Diagnostiquer (≈ 60 min)

Complète pour **chaque** cause trouvée :

| Cause n° | Test qui l'a révélée | Preuve (commande, résultat) | Correction |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Étape 3 – Corriger et retester (≈ 40 min)

Applique les corrections **une à la fois**, **reteste** à chaque fois, **sauvegarde** (`write memory`).

Tests de retour à la normale :

| Test | Résultat |
|---|---|
| `PC-SECR` a une adresse `192.168.10.x` | |
| `PC-DENT` ouvre `www.exemple.fr` | |
| `PC-SECR` joint l'imprimante `192.168.10.20` | |
| `LAP-INV` a une adresse `192.168.20.x` | |
| `LAP-INV` ouvre `www.exemple.fr` | |
| `LAP-INV` ne joint **pas** l'imprimante | |

## Étape 4 – Compte rendu (≈ 30 min)

Rédige-le avec le modèle de l'[aide-mémoire](03-aide-memoire.md).

## Étape 5 – Plan de travail individuel (≈ 30 min)

À partir de la **grille** et de ma **fiche d'erreurs** :

| Point à retravailler | Comment (atelier, séance, exercice) | Pour quand |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
"""
S16["memo"] = """## Indices

Quoi ? Qui ? Depuis quand ? Qu'est-ce qui marche encore ? Qu'a-t-on changé ?

## Démarche

Symptôme → hypothèses → tests → cause → action → vérification. Une correction à la fois ; reprendre l'échelle des tests.

## Compte rendu

Contexte · Symptôme · Diagnostic · Causes · Actions · Résultat · À suivre · Durée.
"""
S16["corrige"] = """Fichiers : `T16-chantier-corrige.json`.

**Cause 1** : `SW1 Fa0/3` en VLAN 20 → `switchport access vlan 10` (l'imprimante, adresse `192.168.10.20`, est isolée du VLAN Soins). **Cause 2** : clé Wi-Fi du portable `Patient#2027` → `Patients#2027` (le portable n'est pas associé à la borne). **Cause 3** : `access-list 1 permit 192.168.10.0 0.0.0.255` ne couvre plus le VLAN 20 → patients sans Internet ; remplacer par `permit 192.168.0.0 0.0.255.255`.

**Ordre de découverte attendu** : l'imprimante d'abord (aisée), puis le Wi-Fi (pas d'adresse), puis Internet des patients (une fois connectés).

**Compte rendu attendu** : 3 causes, 3 actions, 6 tests conformes, sauvegarde, recommandations (revoir la liste d'accès NAT, contrôler les ports après intervention).

**Contrôles automatiques** : 8/8 verts."""

DOSSIER16 = """# 📄 La demande du client – le cabinet Vidal rappelle

*Terminale – E31 – S16 (chantier d'entraînement n°2)*

## Appel du client (reçu à 8 h 50)

> « Bonjour, c'est le cabinet du Dr Vidal. Depuis ce matin, **l'imprimante ne répond plus** au secrétariat. Une patiente me dit aussi qu'elle **ne peut plus se connecter au Wi-Fi**. Pourtant, nous avons Internet aux deux postes. J'ai un rendez-vous important dans une heure. Pouvez-vous passer ? »

## Ce qui est connu

- L'installation date de **trois mois** (voir [S15](../S15-chantier-1/03-dossier-client.md)).
- Une personne du cabinet a **déplacé des câbles** « pour faire de la place » il y a quelques jours.
- Le **mot de passe du Wi-Fi** a été **ressaisi** sur le portable d'un patient « pour tester ».

## Ta mission

1. **Diagnostiquer** toutes les causes.
2. **Corriger** et **prouver** le retour à la normale (tests positifs et négatifs).
3. **Rédiger** un compte rendu d'intervention.

## Exigences initiales (rappel)

Postes en DHCP avec Internet · imprimante à `192.168.10.20` · patients en Wi-Fi `VIDAL-PATIENTS` avec Internet · patients **sans accès** aux postes et à l'imprimante · configuration sauvegardée.
"""

if __name__ == "__main__":
    b = seance("S15", S15); grille("S15", "S15-chantier-1"); w(os.path.join(b, "03-dossier-client.md"), DOSSIER15)
    b = seance("S16", S16); grille("S16", "S16-chantier-2"); w(os.path.join(b, "03-dossier-rappel.md"), DOSSIER16)
