import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance

BACKUP = """```text
hostname SW1
vlan 10
 name BUREAU
vlan 20
 name ATELIER
vlan 30
 name SERVEURS
interface fa0/1
 switchport mode access
 switchport access vlan 10
interface fa0/2
 switchport mode access
 switchport access vlan 30
interface fa0/3
 switchport mode access
 switchport access vlan 20
interface fa0/24
 switchport mode trunk
```"""

S = dict(
 prerequis="Terminale S07 (sauvegardes), S11 (démarche de dépannage)",
 question="Un équipement est mort chez le client. Comment le remplacer vite, sans rien oublier, et comment rendre compte à ceux qui n'étaient pas là ?",
 objectifs=["**Remplacer** un équipement (switch) et **restaurer** sa configuration.", "**Vérifier** le retour à la normale avec des **tests** précis.", "**Rédiger** un compte rendu d'intervention exploitable.", "**Décider** quand et comment **passer la main**."],
 cours_role="Remplacer, restaurer, vérifier ; compte rendu ; escalade",
 tp_role="PME Delmas : le switch a grillé, remplacement et restauration, compte rendu",
 memo_role="Procédure de remplacement, modèle de compte rendu, règles d'escalade",
 fichiers=[("t12-remplacement.json", "Simulateur : switch de remplacement, déjà câblé, VIERGE")],
 deroule=[("0 h 00 – 0 h 20", "**Accroche** : « Le switch fume. Tu as 30 minutes. Que fais-tu d'abord ? »", "Classe"), ("0 h 20 – 0 h 50", "**Mini-cours** : remplacer, restaurer, vérifier", "Classe"), ("0 h 50 – 2 h 00", "**TP A–C** : restauration du switch", "Binôme"), ("2 h 00 – 2 h 15", "Pause", ""), ("2 h 15 – 2 h 45", "**Mini-cours** : compte rendu et escalade", "Classe"), ("2 h 45 – 3 h 30", "**TP D–E** : compte rendu, cas d'escalade", "Individuel"), ("3 h 30 – 4 h 00", "**Jeu de rôle** : passer la main par téléphone", "Binôme")],
 materiel=["Le fichier `t12-remplacement.json`.", "[Aide-mémoire](03-aide-memoire.md) imprimé.", "Si possible : un vrai switch du plateau pour **rejouer** la restauration à la main."],
 eval=[("**Simulateur : 5 contrôles automatiques** (4 tests + sauvegarde)", "Formatif"), ("**Compte rendu d'intervention** + **jeu de rôle d'escalade**", "Grille : faits, tests, cause, action, résultat, clarté de la transmission")],
 notes=["**Rappel :** la sauvegarde utilisée est celle qui aurait été faite en [S07](../S07-maj-sauvegardes/README.md). Si un binôme n'a pas sa sauvegarde, le TP est l'occasion de comprendre pourquoi elle est **indispensable**.", "**Après restauration**, le poste `PC-CPT` doit **renouveler son bail DHCP** (`ipconfig /renew`) car il n'avait plus d'adresse pendant la panne.", "**Le jeu de rôle** (partie E) : un élève est « le technicien » qui appelle, un autre « le responsable / le constructeur ». Le technicien doit tout dire **sans** être relancé : symptôme, tests, ce qu'il a fait.", "**Limite du simulateur :** pas de vraie « panne matérielle » (fumée, ventilateur) : on la représente par un switch **vierge** déjà câblé."],
 corriges_extra=", `T12-remplacement-corrige.json`",
 cours_titre="Dépanner (2) : réparer et rendre compte",
 sauras=["**remplacer** un équipement et **restaurer** sa configuration ;", "**prouver** que tout est revenu à la normale ;", "**rédiger** un compte rendu d'intervention ;", "**décider** de passer la main."],
 sections=[
  dict(h="Remplacer un équipement", q="Un switch grille. Le patron en achète un neuf identique. Tu le branches. **Tout fonctionne-t-il tout de suite ?**",
       a="**Non** : un switch neuf est **vierge** (tous les ports dans le VLAN 1, pas de trunk, pas de nom). Il faut **restaurer** la configuration de l'ancien.",
       idee="**Procédure de remplacement :**\n\n1. **Noter** l'état avant (photos des câbles, étiquettes).\n2. **Retrouver** la dernière sauvegarde de configuration.\n3. **Débrancher** l'ancien, **brancher** le neuf **aux mêmes ports** (les étiquettes servent !).\n4. **Restaurer** : `enable` → `configure terminal` → coller → `end` → `write memory`.\n5. **Vérifier** : tests, état des ports, adresses.\n6. **Documenter** (ancien numéro de série, nouveau, date).",
       c="Pourquoi rebrancher **aux mêmes ports** ?",
       r="Parce que la configuration (VLAN, trunk) dépend du **numéro de port**. Un câble sur un autre port = un poste dans un mauvais VLAN."),
  dict(h="Vérifier le retour à la normale", q="Tu as restauré le switch. Le patron demande : « C'est bon ? ». Tu réponds « Ça devrait. » **Est-ce suffisant ?**",
       a="**Non.** « Ça devrait » n'est pas une preuve. On **teste** et on **montre** que ça fonctionne.",
       idee="> **Retour à la normale = les tests qui échouaient réussissent maintenant, et rien d'autre n'est cassé.**\n\n| Test | Preuve |\n|---|---|\n| Postes ont une adresse | `ipconfig` |\n| Chaque poste joint sa passerelle | `ping` |\n| Les services fonctionnent | page de l'intranet |\n| Config sauvegardée | `show startup-config` |\n\nQuand c'est possible, on **demande à l'utilisateur** de **confirmer** (« Tu peux ouvrir ton logiciel ? »).",
       c="Après restauration, un poste **n'a toujours pas** d'adresse. Quelle est ta première hypothèse ?",
       r="Le **bail DHCP** : le poste doit le **renouveler** (`ipconfig /renew`) ou être rebranché. Sinon : mauvais port ou VLAN."),
  dict(h="Le compte rendu d'intervention", q="Tu as réparé un problème il y a trois semaines. Le client te rappelle pour le même symptôme. **Que te faudrait-il pour agir vite ?**",
       a="Un **compte rendu** de la précédente intervention : ce qui avait été trouvé, fait et **ce qui restait à surveiller**.",
       idee="| Rubrique | Contenu |\n|---|---|\n| **Contexte** | client, date, heure, lieu, demandeur |\n| **Symptôme** | ce que le client a constaté |\n| **Diagnostic** | tests faits et **résultats** |\n| **Cause** | ce qui est **prouvé** |\n| **Action** | ce qui a été **fait** (et par qui) |\n| **Résultat** | tests de retour à la normale |\n| **À suivre** | recommandations (par ex. changer le câble, doubler la sauvegarde) |\n| **Durée** | temps passé |\n\n> [!TIP]\n> Un bon compte rendu se lit en **2 minutes** et peut être **compris par le client**, pas seulement par un technicien.",
       c="Parmi ces phrases, laquelle est la mieux rédigée ? A) « Switch HS, remplacé. » B) « Le switch SW1 ne démarrait plus (voyants éteints, bloc d'alimentation défaillant). Remplacé par un modèle identique, configuration restaurée depuis la sauvegarde du 30/11, 4 tests de retour à la normale OK. »",
       r="**B** : elle donne le **symptôme**, la **cause**, l'**action** et le **résultat**. La A ne permet à personne de comprendre ce qui s'est passé."),
  dict(h="Passer la main", q="Tu cherches depuis 45 minutes et le client s'impatiente. **Continues-tu seul ?**",
       a="**Non** : au-delà d'un temps raisonnable, ou si le risque est élevé, il faut **demander de l'aide**. Insister seul peut **aggraver** la panne.",
       idee="![Les trois niveaux](images/escalade.svg)\n\n**Comment passer la main (script en 4 phrases) :**\n\n1. « Voici le **symptôme**… »\n2. « J'ai **testé**… et j'ai obtenu… »\n3. « J'ai **déjà modifié**… (rien / ceci) »\n4. « Il me faut **de l'aide pour**… »",
       c="Pourquoi faut-il dire **ce qu'on a déjà modifié** quand on passe la main ?",
       r="Pour que celui qui reprend **sache l'état réel** du système, et **ne perde pas de temps** à chercher une modification qu'on a oublié de signaler."),
 ],
 retenir=["**Remplacer** : mêmes ports, restaurer la config, **write memory**.", "**Vérifier** par des tests, pas par un « ça devrait ».", "**Compte rendu** : contexte, symptôme, diagnostic, cause, action, résultat, à suivre.", "**Passer la main** : tôt, en disant **tout** (symptôme, tests, modifications).", "Passer la main n'est pas un échec."],
 tp_titre="PME Delmas : le switch a grillé", tp_format="binôme", tp_temps="3 h 30",
 mission="Ce matin, le **switch de la PME Delmas** ne s'allume plus. Un switch **identique** est installé et câblé, mais il est **vierge**. Tu le remets en service, tu **prouves** que tout fonctionne, puis tu rédiges le **compte rendu**.",
 memo_titre="Remplacement et compte rendu",
 tp="""**Binôme :** ____________ / ____________

Ouvre le [simulateur](../../simulateur/simulateur-reseau.html), puis **Ouvre** [`t12-remplacement.json`](tp/t12-remplacement.json). Le réseau est le même que dans [S11](../S11-depanner-1/02-tp.md) : `PC-CPT` (DHCP), `PC-COM` (fixe), `SRV`, `R1`.

## Partie A – Constater (≈ 15 min)

| Test | Résultat |
|---|---|
| `PC-CPT` a-t-il une adresse `192.168.10.x` ? | |
| `PC-COM` joint-il `192.168.30.10` ? | |
| `show vlan brief` sur `SW1` : que voit-on ? | |

## Partie B – La sauvegarde (≈ 10 min)

Voici la dernière sauvegarde de l'ancien switch (faite lors de la dernière intervention) :

""" + BACKUP + """

❓ **Pourquoi chaque port (`Fa0/1`, `Fa0/2`, `Fa0/3`, `Fa0/24`) est-il important ?** ______________

## Partie C – Restaurer (≈ 45 min)

1. `enable`, puis `configure terminal`.
2. **Colle** la sauvegarde (ou tape-la).
3. `end`, puis **`write memory`**.
4. Sur `PC-CPT` : renouvelle l'adresse (`ipconfig /renew`).

✅ **Points de contrôle :** `show vlan brief` (3 VLAN, bons ports) ; `show interfaces trunk` (`Fa0/24`).

## Partie D – Prouver le retour à la normale (≈ 30 min)

| N° | Test | Résultat |
|---|---|---|
| T1 | `PC-CPT` a une adresse `192.168.10.x` | |
| T2 | `PC-CPT` ouvre `http://intranet.delmas.local` | |
| T3 | `PC-COM` ouvre `http://intranet.delmas.local` | |
| T4 | `PC-COM` joint `192.168.30.10` | |
| T5 | `show startup-config` contient `hostname SW1` | |

## Partie E – Compte rendu d'intervention (≈ 45 min, individuel)

Rédige le compte rendu avec les rubriques du cours. **Écris-le comme si le patron le lisait.**

| Rubrique | À remplir |
|---|---|
| Contexte (client, date, heure, demandeur) | |
| Symptôme | |
| Diagnostic (tests et résultats) | |
| Cause | |
| Action | |
| Résultat | |
| À suivre (recommandation) | |
| Durée | |

## Partie F – Jeu de rôle : passer la main (≈ 30 min)

**Scénario.** Tu as restauré le switch, mais `PC-COM` **n'a toujours pas** accès à l'intranet. Après 40 minutes, tu appelles ton responsable.

Prépare tes **4 phrases** (symptôme, tests, modifications, demande) :

1. ______________
2. ______________
3. ______________
4. ______________

Puis joue la scène avec ton binôme (échange des rôles).

## 🏁 Ce que je sais faire maintenant

| Je sais… | Pas encore | Avec aide | Seul(e) |
|---|---|---|---|
| remplacer un switch et restaurer | ☐ | ☐ | ☐ |
| prouver le retour à la normale | ☐ | ☐ | ☐ |
| rédiger un compte rendu | ☐ | ☐ | ☐ |
| passer la main correctement | ☐ | ☐ | ☐ |
""",
 memo="""## Remplacer un switch

1. Photos / étiquettes · 2. Dernière sauvegarde · 3. Mêmes ports · 4. `enable` → `configure terminal` → coller → `end` → `write memory` · 5. Tests · 6. Documenter.

## Tests de retour à la normale

Adresse (`ipconfig`) · passerelle (`ping`) · service (page) · config sauvegardée (`show startup-config`) · **confirmation de l'utilisateur**.

## Compte rendu

Contexte · Symptôme · Diagnostic · Cause · Action · Résultat · À suivre · Durée.

## Passer la main : 4 phrases

« Voici le symptôme… » · « J'ai testé… » · « J'ai déjà modifié… » · « Il me faut de l'aide pour… ».
""",
 corrige="""Fichier : `T12-remplacement-corrige.json`.

**Partie A** : avant restauration, `PC-CPT` n'a pas d'adresse (`169.254…` ou aucune) ; `PC-COM` ne joint pas le serveur ; `show vlan brief` : tous les ports en VLAN 1, VLAN 10/20/30 absents.

**Partie B** : la configuration dépend du **numéro de port** (VLAN d'accès, trunk vers le routeur).

**Partie C** : après collage, `write memory`, et `ipconfig /renew` sur `PC-CPT`, les VLAN et le trunk sont en place.

**Partie D** : T1 à T5 réussis.

**Partie E (exemple)** : *Contexte* : PME Delmas, 30/11/2026, 8 h 40, M. Delmas. *Symptôme* : plus aucun accès au réseau depuis le matin. *Diagnostic* : switch éteint (voyants éteints), poste sans adresse, routeur et serveur OK. *Cause* : bloc d'alimentation du switch défaillant. *Action* : switch de remplacement installé aux mêmes ports ; configuration restaurée depuis la sauvegarde du 12/10 ; `write memory`. *Résultat* : 5 tests OK, utilisateur a confirmé. *À suivre* : programmer une sauvegarde mensuelle, prévoir un switch de secours. *Durée* : 55 min.

**Partie F** : phrases attendues — symptôme (PC-COM n'accède pas à l'intranet), tests (ping passerelle KO / OK…), modifications (switch restauré, rien d'autre), demande (avis sur le routeur/DNS).

**Contrôles automatiques** : 5/5 verts sur le corrigé.""",
)
if __name__ == "__main__":
    seance("S12", S)
