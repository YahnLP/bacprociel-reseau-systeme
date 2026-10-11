import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance

S = dict(
 prerequis="Tout le parcours (Seconde, Première, Terminale S01–S13)",
 question="Qu'est-ce que je maîtrise vraiment, et qu'est-ce qui me ferait perdre des points le jour de l'épreuve ?",
 objectifs=["**Repérer** ses acquis et ses lacunes d'après le livret.", "**Retravailler** les points faibles par un atelier choisi (câblage, adressage, configuration, dépannage).", "**Construire** sa fiche personnelle « 15 points essentiels ».", "**Chronométrer** un mini-chantier pour évaluer sa vitesse."],
 cours_role="Quatre fiches de révision (câblage, adressage, configuration, dépannage)",
 tp_role="Auto-positionnement, ateliers par niveau (fichiers des années précédentes), fiche « 15 points essentiels »",
 memo_role="Fiche « 15 points essentiels » à compléter",
 fichiers=[],
 deroule=[("0 h 00 – 0 h 30", "**Auto-positionnement** à partir du livret (passeport d'autonomie)", "Individuel"), ("0 h 30 – 0 h 50", "**Mini-cours** de remise à niveau selon les besoins du groupe", "Classe"), ("0 h 50 – 2 h 00", "**Ateliers par niveau** (1 ou 2 ateliers au choix, avec guidage adapté)", "Individuel / binôme"), ("2 h 00 – 2 h 15", "Pause", ""), ("2 h 15 – 3 h 15", "**Atelier chronométré** (un mini-chantier)", "Individuel"), ("3 h 15 – 4 h 00", "**Fiche « 15 points essentiels »**", "Individuel")],
 materiel=["Le **passeport d'autonomie** et le livret de l'élève.", "Les fichiers `.json` des ateliers (liens dans le TP) ; l'aide-mémoire imprimé.", "Un chronomètre."],
 eval=[("**Auto-positionnement** (livret) et **choix des ateliers**", "Formatif, individualisé"), ("**Fiche « 15 points essentiels »** + temps du mini-chantier", "Grille : exactitude, personnalisation, progrès")],
 notes=["**Individualisation :** chaque élève choisit ses ateliers **à partir de ses lacunes** ; l'enseignant **valide** le choix et **oriente** si besoin. Les ateliers réutilisent des fichiers de Seconde, Première et Terminale : **rien de nouveau à préparer**.", "**Passeport d'autonomie :** les lignes « Vu » et « Guidé » doivent **évoluer** vers « Autonome » ; c'est la séance pour les **faire valider**.", "**Fiche « 15 points essentiels »** : strictement **personnelle**, **recto-verso**, autorisée pendant les chantiers d'entraînement (S15–S16) si l'enseignant le décide.", "Le **mini-chantier chronométré** peut reprendre [S01](../S01-diagnostic-retour/README.md) pour mesurer la progression depuis la rentrée.", "**Limite :** certains éléments (VM Ubuntu, Samba, `ufw`, scripts Windows) ne sont **pas** dans le simulateur : si l'élève a un doute, le diriger vers le plateau."],
 cours_titre="Révision et remédiation",
 sauras=["situer ses **acquis** et ses **lacunes** ;", "choisir un atelier **adapté** ;", "résumer l'essentiel sur une **fiche personnelle**."],
 sections=[
  dict(h="Câblage et matériel", q="Un câble relie deux ordinateurs sans switch. **Droit ou croisé ?** Et un PC vers un switch ?",
       a="PC ↔ PC : **croisé** (sauf équipement auto-MDIX, courant aujourd'hui). PC ↔ switch : **droit**. On étiquette toujours les **deux bouts**.",
       idee="| Point à maîtriser | Rappel |\n|---|---|\n| Brochage RJ45 | **T568B** aux deux bouts = droit |\n| Test | **cartographie**, **longueur**, continuité |\n| Fibre | **atténuation** (dB), jamais regarder le laser |\n| Baie | lourd en bas, **étiquettes**, brassage propre |\n\n🔗 Retravailler : [Seconde S09–S10](../../seconde/S10-raccorder-brasser/README.md), [Première S13](../../premiere/S13-cuivre-fibre-securite/README.md), [Terminale S04](../S04-installer-mesurer/README.md).",
       c="La cartographie du câble montre une paire **inversée**. **Que fais-tu ?**",
       r="Je **refais le sertissage** (ou le raccordement) en suivant le **code couleur** T568B aux deux bouts, puis je **retesté**."),
  dict(h="Adressage et services de base", q="Un poste a l'adresse `192.168.1.50/24`. **Quel est son réseau ? Sa passerelle possible ? Peut-il joindre `192.168.2.10` sans routeur ?**",
       a="Réseau `192.168.1.0/24` ; passerelle `192.168.1.1` en général ; **non** pour `192.168.2.10` (autre réseau) sans **routeur**.",
       idee="| Point | Rappel |\n|---|---|\n| Masque | `/24` = `255.255.255.0` |\n| Adresse **169.254** | **pas de DHCP** reçu |\n| Passerelle | doit être **dans le même réseau** que le poste |\n| DNS | traduit un **nom** en adresse |\n\n🔗 Retravailler : [Seconde S11–S13](../../seconde/S11-adresse-ip/README.md), [Première S06](../../premiere/S06-sous-reseaux/README.md), [Première S11](../../premiere/S11-dhcp-dns-serveur/README.md).",
       c="Ping d'une **adresse IP** : OK. Ouverture d'un site par son **nom** : KO. **Que vérifies-tu ?**",
       r="Le **DNS** : serveur DNS du poste, serveur DNS joignable, enregistrement correct."),
  dict(h="Configuration : VLAN, routage, services", q="Deux postes du **même switch** ne se voient pas. **Donne deux causes possibles** liées aux VLAN.",
       a="Les ports sont dans des **VLAN différents**, ou le **VLAN n'existe pas** sur un switch intermédiaire / n'est pas autorisé sur le **trunk**.",
       idee="| Point | Rappel |\n|---|---|\n| VLAN | `vlan 10` / `switchport access vlan 10` |\n| Trunk | `switchport mode trunk` ; VLAN **autorisés** |\n| Inter-VLAN | sous-interfaces `dot1Q` ou interfaces VLAN (L3) |\n| ACL | **sens** et **interface** ; sans état |\n| Sauvegarde | `write memory` |\n\n🔗 Retravailler : [Première S08–S09](../../premiere/S08-vlan-1/README.md), [Terminale S05](../S05-inter-vlan/README.md).",
       c="Tu as configuré un switch, tout marche, mais tu n'as pas tapé `write memory`. **Risque ?**",
       r="Au redémarrage, la configuration est **perdue** (seule la `startup-config` survit)."),
  dict(h="Dépanner avec méthode", q="Un poste n'a plus Internet. **Quel est ton premier test ?**",
       a="Le **plus proche** : lien physique et **adresse** du poste (`ipconfig`). On monte ensuite l'**échelle des tests**.",
       idee="**Démarche :** symptôme → hypothèses → tests → cause → action → vérification. **Une correction à la fois.** **Deux pannes** possibles.\n\n🔗 Retravailler : [Seconde S15](../../seconde/S15-depannage-n1/README.md), [Terminale S11](../S11-depanner-1/README.md), [Terminale S12](../S12-depanner-2/README.md).",
       c="Tu as réparé un défaut et le test passe au vert. Les trois autres restent rouges. **Quelle est ta conclusion ?**",
       r="Il y a **une autre panne** : on n'a fini que quand **tout** est vert."),
 ],
 retenir=["**Je connais mes lacunes** : je les retravaille d'abord.", "**Ma fiche « 15 points »** : mes pièges, mes commandes.", "**Je me chronomètre** pour mesurer mes progrès.", "**La méthode de dépannage** s'applique à tout."],
 tp_titre="Révision et remédiation individualisée", tp_format="individuel, parcours personnalisé", tp_temps="3 h 30",
 mission="Tu choisis **toi-même** les ateliers dont tu as besoin, à partir de ton **passeport d'autonomie**, puis tu construis **ta fiche** des 15 points essentiels.",
 memo_titre="Ma fiche « 15 points essentiels »",
 tp="""**Nom :** ____________

## Partie A – Auto-positionnement (≈ 30 min)

Reprends ton [passeport d'autonomie](../../ressources/passeport-autonomie.md). Pour chaque famille, entoure ton niveau (**Vu** / **Guidé** / **Autonome**) :

| Famille | Mon niveau | Une preuve (activité, TP, PFMP) |
|---|---|---|
| Câblage et matériel | | |
| Adressage, DHCP, DNS | | |
| Configuration (VLAN, routage, services) | | |
| Dépannage | | |

**Mes deux priorités :** 1) ______________ 2) ______________

## Partie B – Les ateliers (≈ 70 min)

Choisis **un ou deux** ateliers (validés par l'enseignant). Ouvre le fichier dans le [simulateur](../../simulateur/simulateur-reseau.html).

| Famille | Atelier | Fichier de départ |
|---|---|---|
| Câblage | Raccorder et brasser | [`s10-deux-pc-switch.json`](../../seconde/S10-raccorder-brasser/tp/s10-deux-pc-switch.json) |
| Adressage | Erreurs d'adressage à trouver | [`s11-erreurs.json`](../../seconde/S11-adresse-ip/tp/s11-erreurs.json) |
| Services | DHCP + DNS en panne | [`p11-dhcp-dns-panne.json`](../../premiere/S11-dhcp-dns-serveur/tp/p11-dhcp-dns-panne.json) |
| Configuration | VLAN en panne | [`p08-vlan-panne.json`](../../premiere/S08-vlan-1/tp/p08-vlan-panne.json) |
| Configuration | Trunk en panne | [`p09-trunk-panne.json`](../../premiere/S09-vlan-2-trunk/tp/p09-trunk-panne.json) |
| Inter-VLAN | Réseau PME en panne | [`t05-panne.json`](../S05-inter-vlan/tp/t05-panne.json) |
| Dépannage | Pannes combinées A, B ou C | [`t11-panne-a.json`](../S11-depanner-1/tp/t11-panne-a.json), [`b`](../S11-depanner-1/tp/t11-panne-b.json), [`c`](../S11-depanner-1/tp/t11-panne-c.json) |

> [!TIP]
> Le fichier contient un **résumé** de la mission (ouvre-le pour le lire). Les corrigés sont chez l'enseignant.

Pour chaque atelier : écris **ce que tu as trouvé**, **ce qui t'a bloqué(e)**, **ce que tu retiens**.

## Partie C – Mini-chantier chronométré (≈ 60 min)

Au choix (avec l'enseignant) : refaire [le mini-chantier de S01](../S01-diagnostic-retour/02-tp.md) **ou** un atelier de dépannage **non encore fait**. ⏱️ Temps : ______ min. Comparaison avec ta première tentative : ______________

## Partie D – Ma fiche « 15 points essentiels » (≈ 45 min)

Une feuille **recto-verso**, écrite **à ta façon** (commandes, pièges, méthode). Elle sera utile pour les chantiers d'entraînement.

| N° | Mon point essentiel | Pourquoi c'est important pour moi |
|---|---|---|
| 1 | | |
| 2 | | |
| … | | |
| 15 | | |

## 🏁 Ce que je sais faire maintenant

| Je sais… | Pas encore | Avec aide | Seul(e) |
|---|---|---|---|
| identifier mes lacunes | ☐ | ☐ | ☐ |
| retravailler un point faible seul(e) | ☐ | ☐ | ☐ |
| me servir de ma fiche pendant un chantier | ☐ | ☐ | ☐ |
""",
 memo="""## Ma fiche « 15 points essentiels » (modèle)

Idées de rubriques :

1. **Câblage** : brochage, test, étiquette.
2. **Adressage** : masque, passerelle, plages.
3. **DHCP / DNS** : symptômes `169.254`, nom ≠ adresse.
4. **VLAN / trunk** : commandes et vérifications.
5. **Inter-VLAN** : sous-interfaces ou SVI.
6. **ACL** : sens, interface, sans état.
7. **Wi-Fi** : SSID, clé, VLAN.
8. **Sauvegarde** : `write memory`, fichier, journal.
9. **Accès distant** : SSH, redirection, VPN.
10. **Dépannage** : échelle des tests, deux pannes.
11. **Recette** : tests positifs et négatifs.
12. **Compte rendu** : contexte, symptôme, cause, action.
13. **Sécurité** : mot de passe, VLAN invités.
14. **Mes erreurs fréquentes** (à écrire).
15. **Mes commandes préférées** (à écrire).
""",
 corrige="""Pas de corrigé unique : la séance est **individualisée**.

**Partie A** : l'enseignant valide le choix des ateliers au regard du passeport.

**Partie B** : se reporter aux corrigés de chaque séance d'origine (`corriges/seconde`, `corriges/premiere`, `corriges/terminale`).

**Partie C** : le temps est comparé au mini-chantier de S01 (progression attendue : −30 % ou plus).

**Partie D** : la fiche doit être **personnelle** (erreurs propres à l'élève), contenir **au moins** : brochage, commandes de vérification, échelle de tests, modèle de compte rendu.""",
)
if __name__ == "__main__":
    seance("S14", S)
