import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance

S = dict(
 prerequis="Seconde S16–S18 (dépannage de niveau 1), Première S06–S09, Terminale S05",
 question="« Ça ne marche pas. » Par où commencer quand il y a trois pannes à la fois, qu'on est chez un client et qu'on a une heure ?",
 objectifs=["**Appliquer** la démarche : symptôme → hypothèses → tests → cause → action.", "**Utiliser** l'**échelle des tests** pour localiser une panne.", "**Lire** les sorties de `ipconfig`, `ping`, `show vlan brief`, `show ip interface brief`, `show ip dhcp`.", "**Dépanner** des **pannes combinées** (physique + IP + VLAN + DNS).", "**Chronométrer** et **réduire** son temps de diagnostic."],
 cours_role="Démarche de dépannage ; échelle des tests ; lire les commandes",
 tp_role="PME Delmas : trois ateliers de pannes combinées, avec chronomètre",
 memo_role="Échelle des tests, tableau « symptôme → hypothèses », commandes de diagnostic",
 fichiers=[("t11-panne-a.json", "Simulateur : atelier A (le poste de l'atelier n'a plus rien)"), ("t11-panne-b.json", "Simulateur : atelier B (le poste du bureau n'a plus d'adresse ; le nom ne marche pas)"), ("t11-panne-c.json", "Simulateur : atelier C (l'atelier ne joint plus le serveur ; le bureau ne résout plus le nom)")],
 deroule=[("0 h 00 – 0 h 20", "**Accroche** : « Une voiture ne démarre pas : par où commence un garagiste ? »", "Classe"), ("0 h 20 – 0 h 50", "**Mini-cours** : la démarche et l'échelle des tests", "Classe"), ("0 h 50 – 1 h 40", "**Atelier A** (avec le cours ouvert)", "Binôme"), ("1 h 40 – 1 h 55", "Pause", ""), ("1 h 55 – 2 h 45", "**Atelier B** (aide-mémoire seulement)", "Binôme"), ("2 h 45 – 3 h 35", "**Atelier C** (individuel, chronométré)", "Individuel"), ("3 h 35 – 4 h 00", "**Bilan** : « Quelle est la panne que tu as trouvée le plus vite, et pourquoi ? »", "Classe")],
 materiel=["Les trois `.json` ci-dessus : **un atelier = un fichier**.", "Un **chronomètre** (téléphone) ; la **fiche de diagnostic** du TP.", "[Aide-mémoire](03-aide-memoire.md) imprimé."],
 eval=[("**Simulateur : 4 contrôles automatiques** par atelier", "Formatif"), ("**Fiche de diagnostic** + **temps** de l'atelier C", "Grille : méthode respectée, preuves, temps, réparation")],
 notes=["**Les causes sont volontairement cachées aux élèves** : ne pas les écrire au tableau. **Atelier A** : port `Fa0/3` désactivé **et** passerelle fausse (`192.168.20.254`). **Atelier B** : port `Fa0/1` dans le VLAN 30 (donc adresse `169.254`) **et** fiche DNS `intranet` pointant sur `192.168.30.11`. **Atelier C** : sous-interface `gi0/0.20` arrêtée **et** pool DHCP sans `dns-server`.", "**Deux défauts par atelier** : l'élève qui répare le premier croit avoir fini. L'insister : **« tu n'as fini que quand les quatre tests sont verts »**.", "**Chronométrage** : le temps sert à **s'améliorer** (comparer atelier A, B, C), pas à classer. Un élève qui **ne suit pas la méthode** va **plus lentement** à la fin : le montrer.", "Dans les ateliers B et C, après correction, **renouveler le bail DHCP** du poste (`ipconfig /renew`).", "**Limite du simulateur :** pas de pannes matérielles réelles (câble abîmé, carte réseau) : on les simule en **supprimant un câble** ou en **arrêtant un port**."],
 corriges_extra=", `T11-panne-a-corrige.json`, `T11-panne-b-corrige.json`, `T11-panne-c-corrige.json`",
 cours_titre="Dépanner (1) : raisonner",
 sauras=["suivre la démarche **symptôme → hypothèses → tests → cause → action** ;", "utiliser l'**échelle des tests** ;", "**lire** les commandes de diagnostic ;", "**ne pas** s'arrêter à la première panne trouvée."],
 sections=[
  dict(h="La démarche : ne pas deviner, enquêter", q="Un poste n'a plus Internet. Un collègue change **tout de suite** le câble, puis la carte réseau, puis redémarre le routeur. Qu'est-ce qui cloche dans sa méthode ?",
       a="Il **essaie au hasard**. Il perd du temps, peut **aggraver** la situation (redémarrer le routeur coupe tout le monde) et **ne sait pas** ce qui était vraiment cassé.",
       idee="> **Symptôme → hypothèses → tests → cause → action → vérification.**\n\n| Étape | Question | Exemple |\n|---|---|---|\n| **Symptôme** | Qu'est-ce qui ne marche pas, **précisément** ? | « PC-COM n'ouvre pas l'intranet » |\n| **Hypothèses** | Qu'est-ce qui **pourrait** l'expliquer ? | câble, adresse, VLAN, routeur, DNS |\n| **Tests** | Comment **trier** les hypothèses ? | `ipconfig`, `ping` |\n| **Cause** | Qu'est-ce qui est **prouvé** ? | « passerelle erronée » |\n| **Action** | Je **corrige** une chose à la fois. | corriger la passerelle |\n| **Vérification** | Je **reteste** *tout*. | les 4 tests |",
       c="Pourquoi ne corrige-t-on qu'**une chose à la fois** ?",
       r="Pour **savoir** ce qui a résolu (ou aggravé) le problème. Si on change trois choses et que ça marche, on ne sait pas laquelle était la bonne."),
  dict(h="L'échelle des tests", q="Un poste n'ouvre pas le site de l'entreprise. Tu peux faire **six** tests. Dans quel **ordre** : du plus proche au plus lointain, ou l'inverse ?",
       a="Du **plus proche au plus lointain**. Si ta propre carte ne marche pas, inutile de tester le serveur.",
       idee="![L'échelle des tests](images/echelle-tests.svg)\n\n> **Le premier test qui échoue désigne la zone en cause.**",
       c="`ipconfig` affiche `169.254.12.7`. À quelle marche de l'échelle es-tu ? Quelles causes ?",
       r="**Marche 2** (adresse). `169.254.x.x` = le poste **n'a pas reçu** d'adresse DHCP : mauvais VLAN, DHCP éteint, relais absent, câble mal enfiché."),
  dict(h="Lire les commandes", q="Tu tapes `show ip interface brief` et vois `GigabitEthernet0/0.20  192.168.20.1  YES manual  administratively down  down`. **Que comprends-tu ?**",
       a="L'interface est **arrêtée volontairement** (`shutdown`). Il faut taper `no shutdown`.",
       idee="| Ce que je lis | Signification | Cause probable |\n|---|---|---|\n| `administratively down` | interface arrêtée par commande | `shutdown` oublié |\n| `down / down` | pas de lien | câble débranché, autre bout éteint |\n| `up / down` | lien présent, protocole en erreur | encapsulation, vitesse |\n| `up / up` | OK | – |\n\n| Commande | Utile pour |\n|---|---|\n| `ipconfig /all` | adresse, passerelle, DNS du poste |\n| `ping` | joignabilité |\n| `show vlan brief` | un port est-il dans le bon VLAN ? |\n| `show interfaces trunk` | le VLAN passe-t-il ? |\n| `show ip interface brief` | état et adresses des interfaces |\n| `show ip dhcp binding` | qui a reçu quelle adresse ? |",
       c="Ping de la passerelle : OK. Ping du serveur : KO. Ping d'un site par son nom : KO. **Que suspectes-tu en premier ?**",
       r="Entre la passerelle et le serveur : **routage, VLAN du serveur, ACL, serveur éteint**. Le nom (DNS) n'est qu'une conséquence : on le teste **après**."),
  dict(h="Deux pannes en même temps", q="Tu as réparé le port d'un poste. Il ne fonctionne toujours pas. **Est-ce que tu t'es trompé ?**",
       a="Pas forcément. Il y a peut-être **une deuxième panne** derrière la première. Tu l'as simplement **découverte** après avoir corrigé la première.",
       idee="> **Tu n'as fini que quand TOUS les tests de départ sont verts.**\n\nAprès chaque correction : **reprends l'échelle** du bas. Note ce que tu as corrigé **et** ce qui reste à faire.",
       c="Dans l'atelier, tu corriges un défaut et le premier test passe au vert. Les trois autres restent rouges. **Que fais-tu ?**",
       r="Je **continue** l'échelle : un test rouge restant = **une autre cause**. Je ne rends pas la main tant que **tout** n'est pas vert."),
 ],
 retenir=["**Symptôme → hypothèses → tests → cause → action → vérification.**", "**Échelle des tests** : du plus proche au plus lointain.", "**Une correction à la fois**, puis on reteste.", "**Plusieurs pannes** : on n'a fini que quand tout est vert.", "**Noter** ce qu'on observe : on gagne du temps et on prouve."],
 tp_titre="PME Delmas : trois ateliers de pannes", tp_format="binôme (A, B) puis individuel (C)", tp_temps="3 h 30",
 mission="Le réseau de la **PME Delmas** a **trois pannes différentes**, une par atelier. Chaque atelier cache **deux défauts**. À toi d'**enquêter** avec la démarche du cours, de **réparer**, puis de **prouver** que tout fonctionne (4 tests au vert).",
 memo_titre="Dépannage – démarche et commandes",
 tp="""**Binôme :** ____________ / ____________

## Le réseau (le même dans les trois ateliers)

| Équipement | VLAN | Adresse | Rôle |
|---|---|---|---|
| `PC-CPT` | 10 BUREAU | DHCP | Poste du bureau |
| `PC-COM` | 20 ATELIER | 192.168.20.11/24 (fixe) | Poste de l'atelier |
| `SRV` | 30 SERVEURS | 192.168.30.10/24 (fixe) | DNS + intranet `intranet.delmas.local` |
| `R1` | trunk | `.1` de chaque réseau | Routeur + DHCP du bureau |
| `SW1` | – | – | Switch |

**Les quatre tests à réussir à la fin de chaque atelier :**

| N° | Test | Atelier A | B | C |
|---|---|---|---|---|
| T1 | `PC-CPT` a une adresse `192.168.10.x` | | | |
| T2 | `PC-CPT` ouvre `http://intranet.delmas.local` | | | |
| T3 | `PC-COM` ouvre `http://intranet.delmas.local` | | | |
| T4 | `PC-COM` joint `192.168.30.10` | | | |

## Atelier A – « L'atelier n'a plus rien » (≈ 50 min)

Ouvre [`t11-panne-a.json`](tp/t11-panne-a.json). **Lance le chronomètre.**

| Étape | Ce que j'observe / je teste | Résultat |
|---|---|---|
| Symptôme (précis) | | |
| Hypothèses (au moins 3) | | |
| Test 1 (marche de l'échelle ?) | | |
| Test 2 | | |
| **Cause n°1** (preuve) | | |
| **Cause n°2** (preuve) | | |
| Action(s) | | |
| Vérification T1 à T4 | | |

⏱️ **Temps :** ______ min

## Atelier B – « Le bureau n'a plus d'adresse » (≈ 50 min)

Ouvre [`t11-panne-b.json`](tp/t11-panne-b.json). Même tableau, **sur ta feuille** (sans le gabarit : recopie les lignes).

⏱️ **Temps :** ______ min

## Atelier C – « L'atelier ne joint plus le serveur » (≈ 50 min, individuel)

Ouvre [`t11-panne-c.json`](tp/t11-panne-c.json). Cette fois, **sans l'aide du cours** (seulement l'aide-mémoire).

⏱️ **Temps :** ______ min

## Bilan (≈ 25 min)

| Question | Ma réponse |
|---|---|
| Quelle panne ai-je trouvée le plus vite ? Pourquoi ? | |
| Où ai-je perdu du temps (hypothèse non testée, deuxième panne oubliée…) ? | |
| Quelle commande m'a le plus aidé(e) ? | |
| Ce que je changerais dans ma méthode | |

## 🏁 Ce que je sais faire maintenant

| Je sais… | Pas encore | Avec aide | Seul(e) |
|---|---|---|---|
| utiliser l'échelle des tests | ☐ | ☐ | ☐ |
| lire `show ip interface brief` et `show vlan brief` | ☐ | ☐ | ☐ |
| trouver deux pannes combinées | ☐ | ☐ | ☐ |
""",
 memo="""## Démarche

**Symptôme → hypothèses → tests → cause → action → vérification.** Une correction à la fois.

## Échelle des tests

1. Câble / carte · 2. Adresse (`169.254` ?) · 3. Passerelle · 4. Autre réseau · 5. Serveur par adresse · 6. Serveur par nom (DNS).

## Symptôme → premières hypothèses

| Symptôme | À regarder en premier |
|---|---|
| `169.254.x.x` | VLAN du port, DHCP, câble |
| Joint la passerelle, pas plus loin | routage, ACL, VLAN du serveur |
| Joint par adresse, pas par nom | DNS (poste ou serveur) |
| Un poste seul est touché | câble, port, configuration du poste |
| Tout un VLAN est touché | trunk, sous-interface, DHCP |

## Commandes

`ipconfig /all` · `ping` · `show vlan brief` · `show interfaces trunk` · `show ip interface brief` · `show ip dhcp binding` · `show running-config`.
""",
 corrige="""Fichiers : `T11-panne-a-corrige.json`, `T11-panne-b-corrige.json`, `T11-panne-c-corrige.json`.

**Atelier A** — Cause 1 : `Fa0/3` en `shutdown` → `no shutdown`. Cause 2 : passerelle de `PC-COM` = `192.168.20.254` au lieu de `192.168.20.1`. Piège : après avoir réactivé le port, le poste est « connecté » mais ne joint toujours pas le serveur.

**Atelier B** — Cause 1 : `Fa0/1` dans le VLAN 30 (le poste reçoit `169.254.x.x`, pas de pool DHCP pour le VLAN 30) → `switchport access vlan 10`, puis `ipconfig /renew`. Cause 2 : enregistrement DNS `intranet.delmas.local` → `192.168.30.11` au lieu de `192.168.30.10`.

**Atelier C** — Cause 1 : sous-interface `gi0/0.20` en `shutdown` (l'atelier n'a plus de passerelle) → `no shutdown`. Cause 2 : pool DHCP `BUREAU` sans `dns-server 192.168.30.10` → ajouter, puis `ipconfig /renew` sur `PC-CPT`.

**Contrôles automatiques** : 4/4 verts sur les trois corrigés.""",
)
if __name__ == "__main__":
    seance("S11", S)
