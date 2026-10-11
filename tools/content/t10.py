import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance

S = dict(
 prerequis="Première S04 (protocoles), S10 (Linux, SSH), Terminale S07",
 question="Le réseau tombe à 3 h du matin. Comment l'apprendre avant le client, et comment ne pas oublier ce qui s'est passé ?",
 objectifs=["**Expliquer** à quoi servent la **supervision**, **SNMP** et les **journaux** (syslog).", "**Activer** SNMP et l'envoi des journaux sur un switch.", "**Interroger** un équipement depuis un poste de supervision et **lire** les valeurs.", "**Lire** une alerte et **ouvrir** un ticket complet.", "**Rédiger** un ticket : symptôme, cause, action."],
 cours_role="Supervision, SNMP, syslog ; alertes ; tickets",
 tp_role="Imprimerie Laporte : SNMP, journaux, interrogation depuis SUP, simulation de panne et ticket",
 memo_role="Commandes SNMP/syslog, OID utiles, modèle de ticket",
 fichiers=[("t10-supervision.json", "Simulateur : switch administrable + poste de supervision, rien de configuré")],
 deroule=[("0 h 00 – 0 h 20", "**Accroche** : « Comment l'entreprise sait-elle qu'une machine est en panne avant d'appeler ? »", "Classe"), ("0 h 20 – 0 h 50", "**Mini-cours** : supervision, SNMP, syslog", "Classe"), ("0 h 50 – 2 h 00", "**TP A–C** : activer SNMP et journaux, interroger", "Binôme"), ("2 h 00 – 2 h 15", "Pause", ""), ("2 h 15 – 2 h 45", "**Mini-cours** : alertes et tickets (GLPI en démonstration)", "Classe"), ("2 h 45 – 3 h 30", "**TP D–E** : provoquer une panne, lire l'alerte", "Binôme"), ("3 h 30 – 4 h 00", "**TP F** : rédiger les tickets", "Individuel")],
 materiel=["Le fichier `t10-supervision.json`.", "Optionnel : une démonstration d'un outil de supervision (Zabbix, Uptime Kuma) ou de **GLPI** sur le plateau.", "[Aide-mémoire](03-aide-memoire.md) imprimé."],
 eval=[("**Simulateur : 5 contrôles automatiques** (SNMP, journaux, alertes, sauvegarde)", "Formatif"), ("**Deux tickets rédigés** (panne câble, panne switch)", "Grille : symptôme décrit, cause, action, résultat, durée")],
 notes=["**Limite du simulateur :** il n'a **ni Zabbix, ni Uptime Kuma, ni GLPI**. La supervision est travaillée avec **`snmpget`/`snmpwalk`** depuis un poste Linux et avec `show logging` sur le switch ; les **outils** sont présentés en **démonstration** (si le plateau en dispose) ; le **ticket** est rédigé **sur papier ou en traitement de texte** (modèle fourni).", "**SNMP v2c** : communauté `supervision` en **lecture seule (RO)**. Expliquer que v2c n'est **pas chiffré** (v3 le serait) : la communauté se comporte comme un mot de passe en clair ; on l'utilise **dans un réseau interne**.", "**Débrancher un câble** dans le simulateur (clic droit sur le câble) puis relancer `snmpwalk … ifOperStatus` : le port passe à `down(2)`. C'est la partie « simulation de panne ». Ne pas annoncer le résultat avant que les élèves l'aient **prévu** (partie D).", "**Lien avec U32 :** la **gestion des incidents** est développée en U32 ; ici on ne prend que le **ticket d'intervention**.", "Le routeur/switch porte une adresse de gestion `192.168.1.2` en VLAN 1 (**uniquement ici**, par simplicité) : en production on utilise un **VLAN de gestion** dédié."],
 corriges_extra=", `T10-supervision-corrige.json`",
 cours_titre="Superviser et tracer les incidents",
 sauras=["dire à quoi servent **supervision**, **SNMP** et **syslog** ;", "activer SNMP et syslog sur un switch ;", "**interroger** un équipement et **lire** la réponse ;", "**rédiger** un ticket exploitable."],
 sections=[
  dict(h="Superviser, c'est surveiller sans être devant", q="Une entreprise a 40 équipements réseau. Le technicien peut-il les surveiller **tous**, **toute la journée**, à la main ?",
       a="**Non.** Il faut un **outil** qui interroge les équipements **en continu** et **prévient** quand quelque chose change.",
       idee="> **Superviser = mesurer en continu et alerter.**\n\n| Ce qu'on surveille | Exemple | Pourquoi |\n|---|---|---|\n| **Disponibilité** | ping : l'équipement répond-il ? | savoir qu'il est tombé |\n| **État des ports** | port `up` / `down` | un câble débranché |\n| **Charge** | débit, processeur | avant que ça rame |\n| **Événements** | journal (syslog) | comprendre ce qui s'est passé |\n\nOutils courants : **Zabbix**, **Uptime Kuma**, Centreon… (démonstration).",
       c="Un port du switch passe de `up` à `down` à 14 h 03. **Quel type d'information** est-ce (disponibilité, charge, événement) ?",
       r="Un **événement** (changement d'état) **et** une information de **disponibilité** du poste branché."),
  dict(h="SNMP : poser des questions aux équipements", q="Tu veux savoir « combien de temps le switch est-il allumé ? » depuis ton poste. **Comment lui demander** sans te connecter dessus ?",
       a="Avec un protocole fait pour ça : **SNMP**. Le switch répond à des **questions standardisées**.",
       idee="Le switch tient à jour une sorte de **tableau de valeurs** (la **MIB**). Chaque valeur a un **numéro** (un **OID**). Le poste de supervision **demande** (`get`), le switch **répond**.\n\n```text\nsnmp-server community supervision RO\nsnmp-server location Atelier - baie 1\nsnmp-server host 192.168.1.5 version 2c supervision\nsnmp-server enable traps\n```\n\nDepuis le poste de supervision :\n\n```text\nsnmpget  -v2c -c supervision 192.168.1.2 1.3.6.1.2.1.1.5.0     # nom du switch (sysName)\nsnmpwalk -v2c -c supervision 192.168.1.2 1.3.6.1.2.1.2.2.1.8   # état de chaque port (ifOperStatus)\n```\n\n| OID | Signification |\n|---|---|\n| `1.3.6.1.2.1.1.5.0` | nom de l'équipement |\n| `1.3.6.1.2.1.1.6.0` | emplacement |\n| `1.3.6.1.2.1.2.2.1.8` | état des ports (1 = up, 2 = down) |\n\n> [!WARNING]\n> La **communauté** (`supervision`) joue le rôle d'un mot de passe, **sans chiffrement** en SNMP v2c. On la met en **lecture seule (RO)** et on **ne laisse pas** `public`.",
       c="Pourquoi met-on la communauté en **RO** (lecture seule) ?",
       r="Pour que le poste de supervision puisse **lire** mais **pas modifier** la configuration des équipements : si la communauté fuit, on limite les dégâts."),
  dict(h="Les journaux : la boîte noire du réseau", q="Un switch a redémarré cette nuit. Le lendemain, on veut savoir **pourquoi**. Où chercher ?",
       a="Dans les **journaux** (*logs*) du switch. Mais s'ils sont **seulement dans le switch** et qu'il redémarre, ils peuvent disparaître : on les envoie à un **serveur de journaux** (syslog).",
       idee="```text\nlogging host 192.168.1.5\nlogging trap informational\nservice sequence-numbers\n```\n\n`show logging` affiche le journal local. Un message ressemble à :\n\n```text\n%LINK-3-UPDOWN: Interface FastEthernet0/2, changed state to down\n```\n\n| Partie | Sens |\n|---|---|\n| `%LINK` | quel **module** |\n| `-3-` | **gravité** (0 = très grave … 7 = détail) |\n| `UPDOWN` | **type** d'événement |\n| texte | le détail |",
       c="Pourquoi envoie-t-on les journaux **hors** du switch ?",
       r="Pour **les conserver** si le switch tombe ou redémarre (et pour les consulter **au même endroit** pour tous les équipements)."),
  dict(h="Le ticket : garder la mémoire", q="Tu répares la même panne chez le même client pour la 3ᵉ fois en un mois. **Qu'est-ce qui t'aurait aidé ?**",
       a="Un **historique** des interventions : « 12 oct. : câble de la salle 2 abîmé, remplacé ». Tu aurais **vu le motif** et proposé de changer **toute la liaison**.",
       idee="Un **ticket** est la **fiche de vie** d'un incident.\n\n| Champ | Exemple |\n|---|---|\n| **Date / heure** | 12/10, 8 h 42 |\n| **Demandeur** | Mme Laporte |\n| **Symptôme** | « Les 2 postes de la compta n'ont plus Internet » |\n| **Cause** | Câble du poste 1 sectionné ; switch redémarré |\n| **Action** | Câble remplacé, `write memory` |\n| **Résultat** | Internet OK, test réalisé |\n| **Durée** | 25 min |\n\n> [!NOTE]\n> **GLPI** (outil libre) gère les tickets : il numérote, assigne, suit, clôture. Le **contenu** que tu rédiges est le même que sur papier.",
       img=("cycle-incident.svg", "Du capteur au ticket"),
       c="Ce ticket est-il bien rempli ? « Internet en panne. Réparé. »",
       r="**Non** : pas de symptôme précis, pas de **cause**, pas d'**action** ni de **résultat**. Un collègue ne pourrait **rien en tirer**."),
 ],
 retenir=["**Superviser = mesurer en continu + alerter.**", "**SNMP** : le poste **demande**, l'équipement **répond** (OID). Communauté **RO**.", "**Syslog** : envoyer les journaux **hors** de l'équipement.", "**Ticket** = symptôme + cause + action + résultat.", "Un ticket vide ne sert **à personne**."],
 tp_titre="Imprimerie Laporte : superviser et tracer", tp_format="binôme", tp_temps="3 h 30",
 mission="L'**imprimerie Laporte** veut être **prévenue** quand un équipement tombe. Tu actives **SNMP** et l'envoi des **journaux** vers le poste de supervision (`SUP`), tu **interroges** le switch, tu **provoques** une panne pour voir l'alerte, puis tu rédiges les **tickets**.",
 memo_titre="Supervision et tickets",
 tp="""**Binôme :** ____________ / ____________

Ouvre le [simulateur](../../simulateur/simulateur-reseau.html), puis **Ouvre** [`t10-supervision.json`](tp/t10-supervision.json).

| Équipement | Adresse | Rôle |
|---|---|---|
| `SW1` (hostname `SW-IMPRIMERIE`) | 192.168.1.2 | Switch à surveiller |
| `SUP` | 192.168.1.5 | Poste de supervision (Linux) |
| `PC-1` | 192.168.1.50 | Poste (Fa0/2) |
| `IMP` | 192.168.1.20 | Imprimante (Fa0/3) |

## Partie A – Constater (≈ 15 min)

Depuis `SUP`, ouvre le terminal et tape :

```text
snmpget -v2c -c supervision 192.168.1.2 1.3.6.1.2.1.1.5.0
```

Quelle est la réponse ? ______________ **Pourquoi ?** ______________

## Partie B – Activer SNMP et les journaux (≈ 40 min)

Sur `SW1` (`enable` puis `configure terminal`) :

1. Communauté `supervision` en **lecture seule** ;
2. emplacement : `Atelier - baie 1` ; contact : `support@laporte-imprimerie.fr` ;
3. envoi des **alertes (traps)** vers `192.168.1.5` ;
4. envoi des **journaux** vers `192.168.1.5`, niveau `informational` ;
5. `write memory`.

✅ **Points de contrôle :** `show snmp community` ; `show logging` (la ligne `Logging to 192.168.1.5`).

❓ **Pourquoi ne choisit-on pas la communauté `public` ?** ______________

## Partie C – Interroger depuis SUP (≈ 30 min)

| Commande depuis `SUP` | Réponse attendue |
|---|---|
| `snmpget -v2c -c supervision 192.168.1.2 1.3.6.1.2.1.1.5.0` | le nom du switch |
| `snmpget -v2c -c supervision 192.168.1.2 1.3.6.1.2.1.1.6.0` | l'emplacement |
| `snmpwalk -v2c -c supervision 192.168.1.2 1.3.6.1.2.1.2.2.1.8` | l'état de chaque port |

Note l'état des ports `Fa0/1`, `Fa0/2`, `Fa0/3` (OID `…10001`, `…10002`, `…10003`) : ______________

## Partie D – Provoquer une panne (≈ 30 min)

1. **Prévois** : si je débranche `PC-1`, quel port change d'état dans la réponse du `snmpwalk` ? ______________
2. **Supprime le câble** de `PC-1` dans le simulateur, puis relance le `snmpwalk`. Qu'observes-tu ? ______________
3. Sur `SW1` : `show logging`. Recopie la ligne qui décrit l'événement : ______________
4. **Rebranche** `PC-1` et vérifie le retour à `up(1)`.

## Partie E – Lire une alerte (≈ 20 min)

À partir de la ligne copiée en D3, remplis :

| Partie | Sens |
|---|---|
| Module | |
| Gravité (numéro) | |
| Événement | |
| Interface concernée | |

## Partie F – Les tickets (≈ 45 min, individuel)

Rédige **deux tickets** avec le [modèle](#modele-de-ticket) :

1. la panne de la partie D (câble de `PC-1`) ;
2. un second incident de ton choix : « le switch ne répond plus à la supervision ».

### Modèle de ticket

| Champ | À remplir |
|---|---|
| Numéro / date / heure | |
| Demandeur | |
| **Symptôme** | |
| **Cause** | |
| **Action** | |
| **Résultat** (test réalisé) | |
| Durée / à surveiller | |

## 🏁 Ce que je sais faire maintenant

| Je sais… | Pas encore | Avec aide | Seul(e) |
|---|---|---|---|
| activer SNMP et les journaux | ☐ | ☐ | ☐ |
| interroger un équipement (snmpget/walk) | ☐ | ☐ | ☐ |
| lire un message de journal | ☐ | ☐ | ☐ |
| rédiger un ticket complet | ☐ | ☐ | ☐ |
""",
 memo="""## Switch

```text
snmp-server community supervision RO
snmp-server location Atelier - baie 1
snmp-server contact support@laporte-imprimerie.fr
snmp-server host 192.168.1.5 version 2c supervision
snmp-server enable traps
logging host 192.168.1.5
logging trap informational
```

Vérifier : `show snmp community` · `show logging`.

## Poste de supervision (Linux)

```text
snmpget  -v2c -c supervision <ip> 1.3.6.1.2.1.1.5.0     (nom)
snmpget  -v2c -c supervision <ip> 1.3.6.1.2.1.1.6.0     (emplacement)
snmpwalk -v2c -c supervision <ip> 1.3.6.1.2.1.2.2.1.8   (état des ports : 1 = up, 2 = down)
```

## Gravité des messages

0 urgence · 1 alerte · 2 critique · 3 erreur · 4 avertissement · 5 notification · 6 information · 7 débogage.

## Ticket

Symptôme · Cause · Action · Résultat · Durée.
""",
 corrige="""Fichier : `T10-supervision-corrige.json`.

**Partie A** : pas de réponse (« timeout ») : SNMP n'est pas activé sur le switch.

**Partie B** : `snmp-server community supervision RO`, `snmp-server location …`, `snmp-server contact …`, `snmp-server host 192.168.1.5 version 2c supervision`, `snmp-server enable traps`, `logging host 192.168.1.5`, `logging trap informational`, `write memory`. `public` est une valeur par défaut **connue de tous**.

**Partie C** : `sysName` : `SW-IMPRIMERIE` ; `sysLocation` : `Atelier - baie 1` ; état des ports : `Fa0/1`, `Fa0/2`, `Fa0/3` en `up(1)` (SUP, PC-1, IMP).

**Partie D** : le port `Fa0/2` passe à `down(2)` ; `show logging` : `%LINK-3-UPDOWN: Interface FastEthernet0/2, changed state to down`.

**Partie E** : module `LINK` ; gravité 3 (erreur) ; événement : changement d'état (`UPDOWN`) ; interface `FastEthernet0/2`.

**Partie F (exemple de ticket 1)** : *Symptôme* : le poste PC-1 n'a plus de réseau ; *Cause* : câble débranché sur Fa0/2 (port `down`) ; *Action* : câble rebranché ; *Résultat* : port `up`, ping OK ; *Durée* : 5 min.

**Contrôles automatiques** : 5/5 verts sur le corrigé.""",
)
if __name__ == "__main__":
    seance("S10", S)
