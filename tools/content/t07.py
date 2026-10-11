import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance

BACKUP = """```text
hostname SW-ATELIER
enable secret Pme#2027
banner motd #Atelier Bonnet - acces reserve#
vlan 10
 name BUREAU
vlan 20
 name ATELIER
interface range fa0/1 - 2
 switchport mode access
 switchport access vlan 10
interface range fa0/3 - 4
 switchport mode access
 switchport access vlan 20
```"""

S = dict(
 prerequis="Première S05 (switch administrable), S14 (sécurité de base), Terminale S05",
 question="Le switch tombe en panne un lundi matin. As-tu de quoi remettre l'entreprise en route avant 10 h ? Et une mise à jour, est-ce toujours une bonne idée ?",
 objectifs=["**Distinguer** `running-config` et `startup-config`, et **sauvegarder** une configuration.", "**Restaurer** une configuration sur un équipement neuf.", "**Appliquer** la démarche de mise à jour (5 étapes) avec **retour arrière**.", "**Tenir un journal des modifications** lisible par un collègue.", "**Appliquer** la règle de sauvegarde « 3-2-1 » à une petite entreprise."],
 cours_role="running/startup ; sauvegarde et restauration ; mise à jour en 5 étapes ; journal",
 tp_role="Atelier Bonnet : constater la perte de configuration, sauvegarder, restaurer sur un switch neuf",
 memo_role="Commandes de sauvegarde, démarche de mise à jour, modèle de journal",
 fichiers=[("t07-sauvegarde.json", "Simulateur : switch configuré mais jamais sauvegardé"), ("t07-restauration.json", "Simulateur : switch neuf, vierge, à remettre dans l'état du switch d'avant")],
 deroule=[("0 h 00 – 0 h 20", "**Accroche** : le switch est mort, qu'est-ce qui manque ?", "Classe"), ("0 h 20 – 0 h 45", "**Mini-cours** : running / startup, sauvegarde", "Classe"), ("0 h 45 – 1 h 45", "**TP A–C** : constater, sauvegarder, redémarrer", "Binôme"), ("1 h 45 – 2 h 00", "Pause", ""), ("2 h 00 – 2 h 30", "**Mini-cours** : mise à jour en 5 étapes, journal", "Classe"), ("2 h 30 – 3 h 30", "**TP D–E** : restaurer sur un équipement neuf", "Binôme"), ("3 h 30 – 4 h 00", "**TP F** : journal de modifications et plan de mise à jour", "Individuel")],
 materiel=["Les deux `.json` du simulateur.", "Un éditeur de texte (Bloc-notes) pour garder la sauvegarde.", "[Aide-mémoire](03-aide-memoire.md) imprimé."],
 eval=[("**Simulateur : 7 contrôles automatiques** (config sauvegardée, restaurée)", "Formatif"), ("**Journal de modifications + plan de mise à jour d'un équipement**", "Grille : version notée, sauvegarde faite, retour arrière prévu")],
 notes=["**Limite du simulateur :** pas de **TFTP/SCP** ni de **mise à jour du micrologiciel** (la commande `show flash:` affiche un fichier fixe). La **sauvegarde** se fait par **copie du texte** de `show running-config` dans un fichier ; la **restauration** par **collage** dans le terminal. La procédure TFTP (`copy running-config tftp:`) est présentée **sur fiche** et à tester sur le matériel réel du plateau si disponible.", "**Mise à jour du micrologiciel** : jamais faite sur le simulateur ; la démarche en 5 étapes est travaillée sur **un cas écrit** (partie F).", "Le piège classique : **modifier sans `write memory`** puis redémarrer. Il est **fait vivre** en partie A.", "La sauvegarde fournie dans le TP contient volontairement `enable secret` en clair pour l'exercice. Rappeler qu'**une sauvegarde de configuration est un fichier sensible** : on ne l'envoie pas par e-mail non protégé.", "Au passage de `copy`/`paste` dans le terminal du simulateur : coller **ligne par ligne** si besoin."],
 corriges_extra=", `T07-sauvegarde-corrige.json`, `T07-restauration-corrige.json`",
 cours_titre="Mises à jour et sauvegardes",
 sauras=["expliquer la différence entre **running-config** et **startup-config** ;", "**sauvegarder** puis **restaurer** une configuration ;", "**préparer** une mise à jour avec un **retour arrière** ;", "**tenir** un journal des modifications."],
 sections=[
  dict(h="Deux configurations, une seule survit au redémarrage", q="Tu tapes des commandes sur un switch : le réseau fonctionne. Le switch redémarre (coupure de courant). **Tes réglages sont-ils encore là ?**",
       a="**Pas forcément.** Les commandes agissent sur la configuration **en cours** (en mémoire vive). Au redémarrage, le switch relit la configuration **enregistrée**. Tout ce qui n'a pas été enregistré est **perdu**.",
       idee="| Configuration | Où ? | Survit au redémarrage ? | Commande pour la voir |\n|---|---|---|---|\n| `running-config` | mémoire vive (RAM) | **Non** | `show running-config` |\n| `startup-config` | mémoire permanente (NVRAM) | **Oui** | `show startup-config` |\n\n```text\nwrite memory          (ou : copy running-config startup-config)\n```\n\n> [!TIP]\n> Après **chaque** série de modifications validées : **`write memory`**. Et **vérifie** avec `show startup-config`.",
       c="Tu as ajouté un VLAN et le réseau marche. Tu ne tapes pas `write memory`. Le client éteint le switch le soir. Que trouve-t-il le lendemain ?",
       r="Le switch **a perdu le VLAN** (retour à la dernière configuration sauvegardée). Les postes concernés ne fonctionnent plus comme avant."),
  dict(h="Sauvegarder pour pouvoir remplacer", q="Un switch grille. Le patron en achète un neuf identique. **De quoi as-tu besoin** pour le remettre comme l'ancien ?",
       a="De la **configuration** de l'ancien switch (VLAN, ports, mots de passe, nom). Si elle n'a **jamais été copiée ailleurs**, elle est **perdue avec le switch**.",
       idee="> **Une sauvegarde utile est : récente, hors de l'appareil, et testée.**\n\n**Sauvegarde simple (copier-coller) :** `show running-config` → copier le texte → l'enregistrer dans un fichier `SW-ATELIER_2026-11-30.txt`.\n\n**Sauvegarde réseau (si le matériel le permet) :** `copy running-config tftp:` ou SCP vers un serveur.\n\n**Restauration :** coller les lignes dans le terminal en mode `configure terminal`, puis `write memory`.\n\n| Règle **3-2-1** | Sens |\n|---|---|\n| **3** copies | l'original + 2 sauvegardes |\n| **2** supports | par ex. serveur + clé USB |\n| **1** hors site | par ex. dans le cloud ou chez le responsable |",
       c="Pourquoi faut-il **tester** une sauvegarde ?",
       r="Parce qu'une sauvegarde **qu'on n'a jamais restaurée** peut être vide, incomplète ou illisible. On le découvre **le jour de la panne**, trop tard."),
  dict(h="Mettre à jour : la démarche en 5 étapes", q="Ton collègue dit : « Il y a une nouvelle version du micrologiciel, je la mets tout de suite sur le switch du client ! » **Que lui réponds-tu ?**",
       a="« **Attends** : on sauvegarde d'abord, on lit la notice, on prévient le client et on prévoit comment revenir en arrière. » Une mise à jour peut **casser** ce qui marchait.",
       idee="1. **Sauvegarder** la configuration et **noter la version** actuelle (`show version`).\n2. **Vérifier** la notice (compatibilité, ce qui change).\n3. **Prévenir** le client, choisir un **créneau calme** (pas en pleine activité).\n4. **Mettre à jour**, redémarrer, attendre le retour de l'équipement.\n5. **Tester** (`show version`, ping, services). **Si ça ne va pas : revenir en arrière** (ancienne version + configuration sauvegardée).\n\nPourquoi mettre à jour malgré le risque ? Pour corriger des **failles de sécurité** et des **bugs** : un équipement jamais mis à jour est une **porte ouverte**.",
       img=("maj-5-etapes.svg", "Les cinq étapes d'une mise à jour"),
       c="Quelle étape un technicien pressé oublie-t-il le plus souvent, et quelle est la conséquence ?",
       r="La **sauvegarde** (étape 1) ou le **plan de retour arrière** (étape 5). Conséquence : si la mise à jour échoue, il faut **tout reconfigurer à la main**, pendant que l'entreprise est à l'arrêt."),
  dict(h="Le journal des modifications", q="Un collègue intervient sur le même client trois mois après toi. **De quoi a-t-il besoin pour comprendre l'état du réseau ?**",
       a="D'un **historique** : ce qui a été changé, **quand**, **par qui**, **pourquoi**. Sans ça, il perd du temps ou refait une erreur déjà corrigée.",
       idee="| Date | Équipement | Modification | Pourquoi | Par qui | Sauvegarde |\n|---|---|---|---|---|---|\n| 30/11/2026 | SW-ATELIER | VLAN 20 « ATELIER » créé | Séparer l'atelier | Y. L. | `SW-ATELIER_2026-11-30.txt` |\n\n> [!NOTE]\n> Le journal est une **preuve** pour ton livret E31 : il montre que tu **documentes** ce que tu fais.",
       c="Complète : « Une modification **non notée** dans le journal, c'est… »",
       r="…une modification que **personne ne saura expliquer** à la prochaine panne (y compris toi)."),
 ],
 retenir=["**running-config** = en cours (perdue) ; **startup-config** = enregistrée.", "**Sauvegarder** = copier **hors de l'équipement** ; **tester** la restauration.", "**Mise à jour** : sauvegarde → notice → client prévenu → mise à jour → test/retour arrière.", "**Journal** : date, équipement, modification, pourquoi, qui.", "**Règle 3-2-1** : 3 copies, 2 supports, 1 hors site."],
 tp_titre="Atelier Bonnet : sauvegarder et restaurer", tp_format="binôme, on **échange les rôles** à chaque partie", tp_temps="3 h 30",
 mission="Chez **Atelier Bonnet** (menuiserie), le switch fonctionne mais **personne n'a jamais sauvegardé sa configuration**. Tu constates le risque, tu sauvegardes, puis tu remets en service un **switch neuf** à partir de la sauvegarde.",
 memo_titre="Mises à jour et sauvegardes",
 tp="""**Binôme :** ____________ / ____________

Ouvre le [simulateur](../../simulateur/simulateur-reseau.html), puis **Ouvre** [`t07-sauvegarde.json`](tp/t07-sauvegarde.json).

## Partie A – Constater le risque (≈ 20 min)

1. Sur `SW1`, tape `show running-config` : repère le **nom**, les **VLAN**, les **ports**.
2. Tape `show startup-config`. **Que vois-tu ?** ______________
3. **Prévois** : si on redémarre maintenant le switch, que perd-on ? ______________

✅ **Point de contrôle :** tu sais expliquer pourquoi `startup-config` est vide (ou ancienne).

## Partie B – Sauvegarder (≈ 30 min)

1. Tape `write memory`. Puis `show startup-config` : que vois-tu maintenant ?
2. **Copie le texte** de `show running-config` dans un fichier texte nommé `SW-ATELIER_AAAA-MM-JJ.txt`.
3. Dans ton journal (partie F), note la sauvegarde.

✅ **Points de contrôle :** `startup-config` contient `hostname SW-ATELIER`, `vlan 20`, `enable secret`.

❓ **Un technicien te dit : « Pas besoin de fichier, le switch se souvient. » Que réponds-tu ?** ______________

## Partie C – Tester la perte (≈ 20 min)

1. Dans le simulateur, ajoute **un VLAN 30** nommé `VISITEURS` **sans** faire `write memory`.
2. Fais `reload` (confirme). Attends le redémarrage.
3. `show vlan brief` : le VLAN 30 existe-t-il encore ? ______________ **Pourquoi ?** ______________

## Partie D – Restaurer sur un switch neuf (≈ 50 min)

Ouvre [`t07-restauration.json`](tp/t07-restauration.json). Le switch d'origine est mort ; le switch **neuf** est vierge. Tu as **cette sauvegarde** :

""" + BACKUP + """

1. Passe en `enable` puis `configure terminal`.
2. **Colle** la sauvegarde (ou tape-la ligne à ligne).
3. `end`, puis **`write memory`**.

✅ **Points de contrôle :**
- `show vlan brief` : VLAN 10 `BUREAU` et 20 `ATELIER`, bons ports ;
- `PC-A` ne joint plus `PC-B` (VLAN différents) : **explique pourquoi** ______________ ;
- `show startup-config` contient `hostname SW-ATELIER`.

❓ **Que se passerait-il si on avait oublié `write memory` ?** ______________

## Partie E – Règle 3-2-1 (≈ 20 min)

L'Atelier Bonnet a 1 switch, 1 routeur-box et 1 serveur de fichiers. **Propose** où ranger les sauvegardes (3 copies, 2 supports, 1 hors site) :

| Copie | Où ? | Qui s'en occupe ? |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

## Partie F – Journal et plan de mise à jour (≈ 50 min, individuel)

**1. Journal.** Complète les deux premières lignes avec ce que tu as fait aujourd'hui.

| Date | Équipement | Modification | Pourquoi | Par qui | Sauvegarde |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |

**2. Cas écrit.** Le constructeur publie une mise à jour du switch qui corrige une faille de sécurité. Écris ton **plan en 5 étapes** : ce que tu notes, ce que tu sauvegardes, quand tu interviens, comment tu testes, comment tu reviens en arrière.

______________________________________________

## 🏁 Ce que je sais faire maintenant

| Je sais… | Pas encore | Avec aide | Seul(e) |
|---|---|---|---|
| sauvegarder une configuration | ☐ | ☐ | ☐ |
| restaurer sur un équipement neuf | ☐ | ☐ | ☐ |
| préparer une mise à jour avec retour arrière | ☐ | ☐ | ☐ |
""",
 memo="""## Commandes

```text
show running-config        # configuration en cours (RAM)
show startup-config        # configuration enregistrée (NVRAM)
write memory               # enregistrer (= copy running-config startup-config)
show version               # modèle, version, durée de fonctionnement
reload                     # redémarrer
```

Sauvegarde réseau (si disponible) : `copy running-config tftp:` · `copy tftp: running-config`.

## Restaurer

`enable` → `configure terminal` → coller → `end` → `write memory` → vérifier.

## Mise à jour : 5 étapes

Sauvegarder · Noter la version · Notice · Prévenir le client · Mettre à jour · Tester ou revenir en arrière.

## Journal (colonnes)

Date · Équipement · Modification · Pourquoi · Par qui · Fichier de sauvegarde.
""",
 corrige="""Fichiers : `T07-sauvegarde-corrige.json`, `T07-restauration-corrige.json`.

**Partie A** : `show startup-config` est vide ou affiche « startup-config is not present » : la configuration n'a **jamais** été enregistrée ; un redémarrage la **perd entièrement**.

**Partie B** : `write memory` ; la `startup-config` contient `hostname SW-ATELIER`, `vlan 20`, `enable secret`. Réponse à la question : « le switch ne se souvient que de la *startup-config* ; et si le switch meurt, tout part avec lui ».

**Partie C** : le VLAN 30 a disparu après `reload` car il n'était **que** dans la *running-config*.

**Partie D** : après collage et `write memory`, le VLAN 10/20 existe ; `PC-A` (VLAN 10) ne joint plus `PC-B` (VLAN 20, même réseau IP mais **domaines de diffusion différents**) ; sans `write memory`, un redémarrage effacerait la restauration.

**Partie E (proposition)** : copie 1 sur le **serveur de fichiers** ; copie 2 sur une **clé USB** gardée au bureau du responsable ; copie 3 dans un **espace en ligne** du prestataire. Responsable : le prestataire (nous) + le patron.

**Partie F** : plan attendu : 1) `show version` + sauvegarde ; 2) lire la notice du constructeur ; 3) prévenir le patron, intervenir hors horaires ; 4) mettre à jour, redémarrer ; 5) `show version`, pings, retour à l'ancienne version et restauration si échec.

**Contrôles automatiques** : 4/4 (sauvegarde) et 3/3 (restauration) verts sur les corrigés.""",
)
if __name__ == "__main__":
    seance("S07", S)
