import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance

S = dict(
 prerequis="Première S18 (recette de projet), Terminale S06 (Wi-Fi), S11–S12",
 question="Comment montrer au client que l'installation est conforme à ce qu'il a demandé, et comment lui expliquer simplement comment s'en servir ?",
 objectifs=["**Établir** un cahier de recette (tests, attendus, résultats obtenus, réserves).", "**Dérouler** la recette sur une installation et **repérer** un écart.", "**Rédiger** un procès-verbal de réception.", "**Accompagner** le client : l'écouter, répondre à ses questions, remettre une **notice d'une page**."],
 cours_role="Cahier de recette, réserves, procès-verbal ; accompagner le client ; notice",
 tp_role="Recette du Wi-Fi du cabinet Garcia, avec un écart à trouver ; jeu de rôle de réception",
 memo_role="Modèles : cahier de recette, procès-verbal, notice",
 fichiers=[("t13-recette.json", "Simulateur : Wi-Fi du cabinet Garcia installé, avec un écart par rapport au cahier des charges")],
 deroule=[("0 h 00 – 0 h 20", "**Accroche** : « Un artisan finit ton installation électrique : comment sais-tu que c'est bien fait ? »", "Classe"), ("0 h 20 – 0 h 50", "**Mini-cours** : la recette, les réserves, le PV", "Classe"), ("0 h 50 – 2 h 00", "**TP A–C** : établir et dérouler la recette", "Binôme"), ("2 h 00 – 2 h 15", "Pause", ""), ("2 h 15 – 2 h 45", "**Mini-cours** : accompagner le client", "Classe"), ("2 h 45 – 3 h 30", "**TP D–E** : jeu de rôle de réception", "Binôme"), ("3 h 30 – 4 h 00", "**TP F** : rédiger la notice d'une page", "Individuel")],
 materiel=["Le fichier `t13-recette.json`.", "Les modèles de l'[aide-mémoire](03-aide-memoire.md) imprimés.", "Rôles pour le jeu : « le client » (carte avec ses attentes et ses questions)."],
 eval=[("**Simulateur : 6 contrôles automatiques** après correction", "Formatif"), ("**Cahier de recette rempli + PV + notice d'une page** ; **jeu de rôle** observé", "Grille : tests pertinents, écart repéré, PV complet, langage adapté au client")],
 notes=["**L'installation de départ comporte un écart** : l'ACL des invités n'est pas posée, donc les invités **joignent le serveur interne** et **le Wi-Fi du personnel**. Les élèves doivent **le découvrir par leurs tests**, pas par la lecture de la configuration.", "**Ne pas dire** aux élèves quel test échoue. S'ils réussissent tous les tests, c'est qu'**ils n'ont pas testé les interdictions** (tests **négatifs**) : bon moment pour en parler.", "**Jeu de rôle** : le « client » a des attentes précises (« les clients ne doivent pas voir mon serveur ») et **des questions de non-initié** (« c'est quoi un SSID ? »). Un observateur remplit une grille : vocabulaire, écoute, clarté.", "**Notice d'une page** : à destination d'un utilisateur, **sans jargon**. Longueur maximale : **une page**.", "**Lien avec R1/R2** (compétences relationnelles) : ce TP est la meilleure occasion d'**observer** la communication orale."],
 corriges_extra=", `T13-recette-corrige.json`",
 cours_titre="Recette et accompagnement du client",
 sauras=["**construire** un cahier de recette avec des tests **positifs** et **négatifs** ;", "**noter** un écart en **réserve** ;", "**rédiger** un procès-verbal ;", "**expliquer** simplement à un client."],
 sections=[
  dict(h="Le cahier de recette", q="Tu viens de terminer une installation Wi-Fi. Le client demande : « Comment je sais que vous avez fait ce que je voulais ? ». **Que lui montres-tu ?**",
       a="Une **liste de tests** qui prouvent chaque point demandé, avec le **résultat obtenu** : le **cahier de recette**.",
       idee="| N° | Exigence du client | Test | Attendu | Obtenu | Statut |\n|---|---|---|---|---|---|\n| 1 | Le personnel a le Wi-Fi interne | `LAP-PERS` se connecte à `GARCIA-PERSONNEL` | adresse `192.168.20.x` | | |\n| 2 | Le personnel accède au serveur | ping `192.168.10.10` | réponse | | |\n| 3 | Les invités ont Internet / passerelle | ping `192.168.30.1` | réponse | | |\n| 4 | **Les invités ne voient pas le serveur** | ping `192.168.10.10` depuis `LAP-INV` | **pas de réponse** | | |\n\n> [!IMPORTANT]\n> **Teste aussi ce qui doit être IMPOSSIBLE** (tests **négatifs**) : c'est souvent là qu'on trouve les défauts de sécurité.",
       c="Le client dit : « Mes invités ne doivent pas voir mon serveur. » **Quel test écris-tu ?**",
       r="Un test **négatif** : depuis un poste du Wi-Fi invités, **ping du serveur** ; **attendu : aucune réponse**."),
  dict(h="Écarts et réserves", q="Un test échoue à la recette, mais le client veut **quand même** emménager vendredi. **Peut-on recevoir l'installation ?**",
       a="Cela dépend de la **gravité** de l'écart. Un écart **mineur** (logo manquant) → oui, avec une **réserve**. Un écart **bloquant** (les invités voient le serveur) → il faut **corriger** d'abord.",
       idee="![Trois issues d'un test de recette](images/recette-3-issues.svg)\n\nUne **réserve** s'écrit : **quel test**, **quel écart**, **qui corrige**, **pour quand**.",
       c="Tu trouves un écart de **sécurité** (les invités voient le serveur). Réserve ou non-conformité ?",
       r="**Non conforme** (bloquant) : un défaut de sécurité **ne doit pas rester** en production. On corrige, puis on refait le test."),
  dict(h="Le procès-verbal de réception", q="À quoi sert une **signature** du client en fin de chantier ?",
       a="À **prouver** que le client a reçu l'installation, **tests à l'appui**, et à **fixer** la date : la garantie et la facturation en dépendent.",
       idee="Le PV comporte : **client**, **prestataire**, **date**, **liste des tests** (conformes), **réserves** (avec délai), **documents remis**, **signatures** des deux parties.\n\n> [!NOTE]\n> Signer, c'est **engager** : il faut que **tout** ce qui est écrit soit **vrai**. On ne coche pas un test qu'on n'a pas fait.",
       c="Tu es pressé. Peux-tu cocher « test 4 conforme » sans l'avoir fait ?",
       r="**Non** : c'est un **faux** dans un document contractuel. Et si le défaut est découvert plus tard, **tu en es responsable**."),
  dict(h="Accompagner le client", q="Tu dis à un client : « J'ai créé deux SSID sur des VLAN séparés avec une ACL. » **A-t-il compris ?**",
       a="**Non**, sauf s'il est du métier. Tu dois **traduire** : « Vos clients ont leur **propre Wi-Fi**, qui ne leur permet **pas** d'accéder à vos ordinateurs. »",
       idee="**Quatre règles pour parler à un client :**\n\n1. **Écouter** d'abord ses attentes et ses inquiétudes.\n2. **Parler son langage** (pas de sigles sans explication).\n3. **Montrer** plutôt qu'expliquer (« essayez de vous connecter »).\n4. **Laisser une trace** : la **notice d'une page**.\n\n**La notice d'une page** : à quoi sert l'installation, **comment s'en servir**, **qui appeler** en cas de problème. **Sans jargon.**",
       c="Réécris pour un client : « Le DHCP est configuré sur le VLAN 20 avec un bail de 8 heures. »",
       r="« Vos ordinateurs reçoivent **automatiquement** leur réglage réseau chaque jour : **vous n'avez rien à faire**. »"),
 ],
 retenir=["**Recette = tests (positifs et négatifs) + attendu + obtenu.**", "**Réserve** : écart mineur, avec date de levée ; **non-conformité** : on corrige avant de recevoir.", "**PV** : tests, réserves, signatures ; on n'écrit **que ce qui est vrai**.", "**Client** : écouter, traduire, montrer, laisser une notice.", "**Une page** de notice, **sans jargon**."],
 tp_titre="Recette du Wi-Fi du cabinet Garcia", tp_format="binôme, on **échange les rôles** (technicien / client)", tp_temps="3 h 30",
 mission="Tu viens d'installer le **Wi-Fi du cabinet Garcia** (voir [S06](../S06-wifi-entreprise/02-tp.md)). Avant de remettre les clés au client, tu **déroules la recette**, tu notes les **écarts**, tu **proposes la correction**, puis tu **reçois l'installation** avec le client.",
 memo_titre="Recette et accompagnement",
 tp="""**Binôme :** ____________ / ____________

Ouvre le [simulateur](../../simulateur/simulateur-reseau.html), puis **Ouvre** [`t13-recette.json`](tp/t13-recette.json).

## Le besoin du client (extrait du cahier des charges)

- Le **personnel** se connecte à `GARCIA-PERSONNEL` et accède au **serveur interne** `192.168.10.10`.
- Les **invités** se connectent à `GARCIA-INVITES` et **ne doivent accéder ni au serveur interne, ni aux ordinateurs du personnel**.
- Les invités peuvent utiliser leur passerelle (`192.168.30.1`).

## Partie A – Écrire le cahier de recette (≈ 30 min)

Complète les colonnes **Test** et **Attendu** (au moins **six** lignes, dont **au moins deux tests négatifs**) :

| N° | Exigence | Test | Attendu | Obtenu | Statut (✔ / réserve / ✘) |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

## Partie B – Dérouler la recette (≈ 45 min)

Exécute **chaque test** sur le simulateur, **sans modifier** la configuration. Note l'**obtenu** et le **statut**.

✅ **Point de contrôle :** tous les tests ont un résultat écrit.

## Partie C – Traiter l'écart (≈ 30 min)

Au moins un test est **non conforme**.

| Question | Réponse |
|---|---|
| Quel test ? Quel écart ? | |
| Réserve ou non-conformité ? **Pourquoi ?** | |
| Quelle est la **cause** probable ? | |
| Quelle **correction** ? (commande) | |

**Corrige** (sur le routeur), puis **refais** le test. Mets à jour la colonne « Statut ».

✅ **Point de contrôle :** après correction, tous les tests sont ✔.

## Partie D – Le procès-verbal (≈ 20 min)

Complète le [modèle de PV](03-aide-memoire.md#proces-verbal-de-reception).

## Partie E – Jeu de rôle : la réception avec le client (≈ 40 min)

- **Rôle 1 : le technicien** présente l'installation, **montre** un test, répond aux questions, fait signer le PV.
- **Rôle 2 : le client** (Mme Garcia, non informaticienne) pose des questions : *« C'est quoi un SSID ? », « Et si un invité devine le mot de passe du personnel ? », « Qui j'appelle si ça ne marche plus ? »*.
- **Observateur** (ou l'enseignant) : grille ci-dessous.

| Critère | ✔ / ✘ |
|---|---|
| Le technicien a écouté avant de parler | |
| Vocabulaire compréhensible (pas de sigles sans explication) | |
| Il a **montré** un test réel | |
| Il a répondu **honnêtement** (« je ne sais pas, je vérifie ») | |
| Le PV a été relu avant signature | |

**Échangez les rôles**, puis recommencez.

## Partie F – La notice d'une page (≈ 40 min, individuel)

Rédige **une page** pour Mme Garcia : *à quoi servent les deux Wi-Fi ; comment connecter un invité ; qui appeler ; ce qu'il ne faut jamais faire* (partager le mot de passe du personnel). **Aucun jargon.**

## 🏁 Ce que je sais faire maintenant

| Je sais… | Pas encore | Avec aide | Seul(e) |
|---|---|---|---|
| écrire un cahier de recette (avec tests négatifs) | ☐ | ☐ | ☐ |
| distinguer réserve et non-conformité | ☐ | ☐ | ☐ |
| expliquer simplement à un client | ☐ | ☐ | ☐ |
""",
 memo="""## Cahier de recette (modèle)

| N° | Exigence | Test | Attendu | Obtenu | Statut |
|---|---|---|---|---|---|

Statut : ✔ conforme · réserve (écart mineur, date de levée) · ✘ non conforme (bloquant).

## Procès-verbal de réception

| Rubrique | À remplir |
|---|---|
| Client / adresse | |
| Prestataire / technicien | |
| Date et heure | |
| Installation reçue (description en 2 lignes) | |
| Tests réalisés (renvoi au cahier de recette) | |
| Réserves (n°, écart, correction, **date de levée**) | |
| Documents remis (schéma, plan d'adressage, notice) | |
| Signature du client | |
| Signature du technicien | |

## Parler à un client

Écouter · traduire · montrer · laisser une notice d'une page.

## Notice (plan)

À quoi ça sert · Comment s'en servir · Qui appeler · Ce qu'il ne faut pas faire.
""",
 corrige="""Fichier : `T13-recette-corrige.json`.

**Partie A (exemple)** : 1) Le personnel se connecte au Wi-Fi interne → adresse `192.168.20.x` ; 2) le personnel joint le serveur → ping OK ; 3) un invité se connecte → adresse `192.168.30.x` ; 4) un invité joint sa passerelle `192.168.30.1` → OK ; 5) **négatif** : un invité ne joint **pas** `192.168.10.10` ; 6) **négatif** : un invité ne joint **pas** le portable du personnel.

**Partie B** : sur l'installation de départ, les tests 1 à 4 sont conformes ; les tests 5 et 6 sont **non conformes** (les invités joignent le serveur et le portable du personnel).

**Partie C** : cause : l'ACL `INVITES-IN` n'est pas appliquée à `gi0/0.30` ; correction : `interface gi0/0.30` → `ip access-group INVITES-IN in` (l'ACL existe déjà dans le fichier : la commande applique sa définition) ; après correction, tests 5 et 6 conformes. **Non-conformité** (et pas simple réserve), car c'est un défaut de **sécurité** demandé explicitement par le client.

**Partie D** : PV complété avec 6 tests, 0 réserve après correction, documents remis (plan d'adressage, schéma, notice), signatures.

**Partie E** : le client doit comprendre « un SSID = le nom du réseau Wi-Fi », que les invités ne peuvent pas atteindre le réseau du personnel, et qui contacter.

**Contrôles automatiques** : 6/6 verts sur le corrigé.""",
)
if __name__ == "__main__":
    seance("S13", S)
