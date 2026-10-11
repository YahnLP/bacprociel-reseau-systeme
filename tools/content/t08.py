import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance

S = dict(
 prerequis="Seconde S11 (adresses fixes et DHCP), Première S08–S09 (VLAN), Terminale S05",
 question="Le patron branche une caméra connectée sur le réseau « parce que c'est du Wi-Fi/RJ45, ça doit marcher ». Qu'est-ce qui peut mal tourner, et comment l'intégrer proprement ?",
 objectifs=["**Intégrer** un équipement réseau (imprimante, NAS) avec une **adresse réservée** hors plage DHCP.", "**Placer** les objets connectés dans un **VLAN dédié**.", "**Expliquer** le PoE et **choisir** entre alimentation par câble réseau ou par bloc secteur.", "**Tester** l'équipement (test fonctionnel) et **mettre à jour la documentation**.", "**Repérer** les équipements d'un réseau industriel (aperçu)."],
 cours_role="Intégration en 6 étapes ; réservation d'adresse ; VLAN objets ; PoE ; aperçu industriel",
 tp_role="Cabinet Lemoine : imprimante + NAS dans un VLAN dédié, puis fiche d'intégration (caméra IP et ESP32 sur papier)",
 memo_role="Procédure d'intégration, plan d'adressage type, PoE en un coup d'œil",
 fichiers=[("t08-integration.json", "Simulateur : équipements posés, aucun câble, switch cœur vierge")],
 deroule=[("0 h 00 – 0 h 20", "**Accroche** : « Qui a déjà branché une caméra ou une enceinte connectée chez lui ? Qu'est-ce qui s'est passé ? »", "Classe"), ("0 h 20 – 0 h 50", "**Mini-cours** : intégrer en 6 étapes, réservation, VLAN objets", "Classe"), ("0 h 50 – 2 h 00", "**TP A–C** : câbler, VLAN 40, adresses fixes", "Binôme"), ("2 h 00 – 2 h 15", "Pause", ""), ("2 h 15 – 2 h 45", "**Mini-cours** : PoE, ESP32, réseaux industriels (aperçu)", "Classe"), ("2 h 45 – 3 h 30", "**TP D–E** : tests, fiche d'intégration d'une caméra IP et d'un ESP32", "Individuel"), ("3 h 30 – 4 h 00", "**TP F** : mise à jour de la documentation", "Individuel")],
 materiel=["Le fichier `t08-integration.json`.", "Si disponible : un petit switch PoE, une caméra IP ou un ESP32 du plateau, **uniquement pour observer** (non indispensable).", "[Aide-mémoire](03-aide-memoire.md) imprimé."],
 eval=[("**Simulateur : 5 contrôles automatiques** (adresses, VLAN, tests, sauvegarde)", "Formatif"), ("**Fiche d'intégration** (caméra IP) + **plan d'adressage mis à jour**", "Grille : adresse réservée, VLAN justifié, test fonctionnel, documentation à jour")],
 notes=["**Limite du simulateur :** il n'a ni **caméra IP**, ni **PoE**, ni **ESP32**. L'**imprimante** et le **NAS** servent de cas réel ; la caméra et l'ESP32 sont travaillés **sur fiche** (partie E) et, si possible, sur du matériel réel du plateau.", "**Réservation d'adresse :** le TP utilise des adresses **fixes hors plage DHCP** (méthode la plus simple). La **réservation DHCP par adresse MAC** est présentée au cours mais non refaite.", "**Aperçu des réseaux industriels :** simple repérage (automate, capteur, passerelle, protocoles Modbus/Profinet) ; **aucune configuration** n'est demandée.", "**Sécurité IoT :** insister sur le **mot de passe par défaut** à changer et sur l'**isolement** dans un VLAN.", "Le switch cœur est un 3560 (niveau 3) ; il a pour DHCP le pool `POSTES`. `ip dhcp excluded-address 192.168.10.1 192.168.10.49` réserve le bas de plage."],
 corriges_extra=", `T08-integration-corrige.json`",
 cours_titre="Intégrer de nouveaux équipements",
 sauras=["**intégrer** un équipement réseau avec une méthode en 6 étapes ;", "**réserver** une adresse et éviter les conflits ;", "**isoler** les objets connectés dans un VLAN ;", "expliquer le **PoE** ;", "**mettre à jour** la documentation après l'intégration."],
 sections=[
  dict(h="Intégrer, c'est plus que brancher", q="Un client branche une imprimante neuve qui prend une adresse par DHCP. Trois semaines plus tard, plus personne n'imprime. **Pourquoi ?**",
       a="Le DHCP a **changé son adresse** (bail renouvelé, autre adresse attribuée). Les postes cherchaient l'ancienne. Un équipement que d'autres utilisent doit avoir **une adresse qui ne bouge pas**.",
       idee="**Les 6 étapes d'une intégration :**\n\n1. **Où ?** emplacement, prise, alimentation.\n2. **Quelle adresse ?** fixe, **hors de la plage DHCP**, notée dans le plan d'adressage.\n3. **Quel VLAN ?** objets → VLAN dédié.\n4. **Brancher et configurer** (port du switch, adresse, passerelle, mot de passe).\n5. **Tester** (ping, fonction réelle : imprimer, sauvegarder…).\n6. **Documenter** (plan d'adressage, schéma, journal).",
       c="Dans une plage DHCP de `.50` à `.200`, où places-tu l'adresse fixe d'une imprimante, et pourquoi ?",
       r="**En dehors** de la plage : par exemple `.20`. Sinon le DHCP pourrait la donner à un autre poste (**conflit d'adresse**)."),
  dict(h="Un VLAN pour les objets", q="Une caméra connectée a le mot de passe `admin` d'origine. Elle est sur le même réseau que la comptabilité. **Quel risque ?**",
       a="Un pirate qui **prend la caméra** (mot de passe connu) se retrouve **dans le réseau** de l'entreprise, **à côté** des ordinateurs de la comptabilité.",
       idee="> **Les objets connectés sont souvent mal protégés.** On les **isole** dans un VLAN à part (ici VLAN 40) : si l'un est compromis, l'attaque **ne gagne pas** les postes.\n\n| VLAN | Réseau | Équipements |\n|---|---|---|\n| 10 POSTES | 192.168.10.0/24 | Ordinateurs (DHCP `.50`+) |\n| 40 OBJETS | 192.168.40.0/24 | Imprimante `.20`, NAS `.30`, caméra `.31`, ESP32 `.40` |",
       img=("vlan-objets.svg", "Un VLAN pour les objets connectés"),
       c="Pourquoi change-t-on **toujours** le mot de passe par défaut d'un objet connecté ?",
       r="Parce que les mots de passe **par défaut sont publics** (dans les notices et sur Internet) : n'importe qui les connaît."),
  dict(h="Le PoE : un seul câble pour tout", q="Une caméra est fixée au plafond, loin de toute prise électrique. Comment l'alimenter **sans** tirer un second câble ?",
       a="Avec le **PoE** (*Power over Ethernet*) : le **câble réseau** apporte **aussi l'électricité**.",
       idee="| | Sans PoE | Avec PoE |\n|---|---|---|\n| Câbles | réseau **+** secteur | réseau **seul** |\n| Matériel | bloc d'alimentation par objet | switch **PoE** (ou injecteur) |\n| Panne de courant | coupure | peut être sauvé par **un seul** onduleur sur le switch |\n\n> [!WARNING]\n> Le switch doit fournir **assez de puissance** (budget PoE en watts) pour **tous** les appareils branchés. Sinon, certains ne démarrent pas.",
       c="Un switch PoE offre 120 W. Tu veux brancher 6 caméras de 15 W. **Est-ce possible ?**",
       r="6 × 15 = **90 W** ≤ 120 W : **oui**, avec 30 W de marge."),
  dict(h="Un aperçu des réseaux industriels", q="Dans un atelier, une machine envoie des informations à un ordinateur. **Comment ?**",
       a="Souvent par un **réseau de type industriel** : un **automate** (le « cerveau de la machine ») relié à des **capteurs** et à un **switch**, avec des protocoles comme **Modbus** ou **Profinet**.",
       idee="Tu **repères** les équipements, tu **ne les configures pas** en Terminale :\n\n| Équipement | Rôle |\n|---|---|\n| **Capteur** | mesure (température, présence…) |\n| **Automate** | décide et commande |\n| **Passerelle** | relie l'atelier au réseau de bureau |\n| **Switch industriel** | robuste, rail DIN |\n\nCe qui reste **pareil** : adresse IP, VLAN, câblage, documentation.",
       c="Quelle règle de ce cours s'applique **aussi** à un automate d'atelier ?",
       r="**Adresse fixe réservée**, **VLAN dédié**, **mot de passe changé**, **documentation à jour**."),
 ],
 retenir=["**6 étapes :** où, adresse, VLAN, brancher, tester, documenter.", "**Adresse fixe hors plage DHCP.**", "**Objets connectés → VLAN dédié, mot de passe changé.**", "**PoE** : un câble pour réseau + courant ; vérifier le **budget en watts**.", "**La documentation est la dernière étape** : intégration non documentée = intégration non terminée."],
 tp_titre="Cabinet Lemoine : intégrer imprimante et NAS", tp_format="binôme", tp_temps="3 h 30",
 mission="Le **cabinet d'architectes Lemoine** reçoit une **imprimante réseau** et un **NAS**. Tu les intègres dans un **VLAN dédié**, avec des **adresses réservées**, tu **testes**, puis tu rédiges la **fiche d'intégration** d'une caméra IP et d'une carte ESP32.",
 memo_titre="Intégrer un équipement",
 tp="""**Binôme :** ____________ / ____________

Ouvre le [simulateur](../../simulateur/simulateur-reseau.html), puis **Ouvre** [`t08-integration.json`](tp/t08-integration.json).

## Plan d'adressage à respecter

| Équipement | VLAN | Adresse | Passerelle | Port du switch |
|---|---|---|---|---|
| `PC-1`, `PC-2` | 10 POSTES | DHCP (`.50` et +) | 192.168.10.1 | Fa0/1, Fa0/2 |
| `IMP` (imprimante) | 40 OBJETS | 192.168.40.20/24 | 192.168.40.1 | Fa0/3 |
| `NAS` | 40 OBJETS | 192.168.40.30/24 | 192.168.40.1 | Fa0/4 |
| Switch cœur `CORE` | – | `.10.1` et `.40.1` | – | – |

## Partie A – Câbler (≈ 15 min)

Relie les 4 équipements à `CORE` (`PC-1` → Fa0/1, `PC-2` → Fa0/2, `IMP` → Fa0/3, `NAS` → Fa0/4).

✅ **Point de contrôle :** tous les liens sont verts.

## Partie B – VLAN et routage (≈ 45 min)

Sur `CORE` : `ip routing` ; VLAN **10 POSTES** et **40 OBJETS** ; ports d'accès ; **interfaces VLAN** `.10.1` et `.40.1` ; **pool DHCP** `POSTES` avec `ip dhcp excluded-address 192.168.10.1 192.168.10.49` ; `write memory`.

✅ **Points de contrôle :** `show vlan brief` ; `show ip interface brief` (`Vlan10`, `Vlan40` en `up`).

❓ **Pourquoi exclut-on `192.168.10.1` à `.49` du pool ?** ______________

## Partie C – Adresses de l'imprimante et du NAS (≈ 30 min)

Sur `IMP` et `NAS` : adresse **fixe** selon le tableau, **passerelle** `192.168.40.1`.

✅ **Point de contrôle :** `PC-1` obtient bien une adresse `192.168.10.5x` ou plus.

## Partie D – Tester (≈ 30 min)

| Test | Attendu | Obtenu |
|---|---|---|
| `PC-1` → `ping 192.168.40.20` | ✓ | |
| `PC-2` → `ping 192.168.40.30` | ✓ | |
| `PC-1` → `ping 192.168.10.1` | ✓ | |

❓ **Si l'imprimante ne répond pas au ping, quelles sont tes 3 premières vérifications ?** ______________

## Partie E – Cas écrit : une caméra IP PoE et un ESP32 (≈ 45 min, individuel)

Le client veut **une caméra IP** (alimentée en PoE) à l'entrée et **une carte ESP32** qui envoie la température de la salle serveur. Complète la fiche :

| Élément | Caméra IP | ESP32 |
|---|---|---|
| VLAN | | |
| Adresse (hors plage DHCP) | | |
| Passerelle | | |
| Alimentation (PoE ? bloc ?) | | |
| Mot de passe par défaut changé ? | | |
| Test fonctionnel prévu | | |
| Risque principal | | |

## Partie F – Mettre à jour la documentation (≈ 30 min)

Complète le **plan d'adressage** du cabinet et le **journal de modifications** (voir [S07](../S07-maj-sauvegardes/01-cours.md)) avec les 4 équipements.

## 🏁 Ce que je sais faire maintenant

| Je sais… | Pas encore | Avec aide | Seul(e) |
|---|---|---|---|
| intégrer un équipement en 6 étapes | ☐ | ☐ | ☐ |
| réserver une adresse hors plage DHCP | ☐ | ☐ | ☐ |
| justifier un VLAN pour les objets | ☐ | ☐ | ☐ |
""",
 memo="""## Procédure d'intégration

1. **Où ?** 2. **Adresse fixe** (hors DHCP) 3. **VLAN** 4. **Brancher / configurer** 5. **Tester** 6. **Documenter**.

## Commandes du switch niveau 3

```text
ip routing
vlan 40
 name OBJETS
interface fa0/3
 switchport mode access
 switchport access vlan 40
interface vlan 40
 ip address 192.168.40.1 255.255.255.0
 no shutdown
ip dhcp excluded-address 192.168.10.1 192.168.10.49
```

## PoE : rappel

Budget du switch (W) ≥ somme des puissances des appareils. Câble : catégorie 5e minimum.

## Plan d'adressage type

| Plage | Usage |
|---|---|
| `.1` | passerelle |
| `.2` – `.49` | équipements fixes |
| `.50` – `.200` | DHCP |
""",
 corrige="""Fichier : `T08-integration-corrige.json`.

**Partie B** : on réserve `.1`–`.49` pour les adresses fixes et la passerelle ; le DHCP distribue à partir de `.50`.

**Partie C** : `IMP` `192.168.40.20/24`, passerelle `.40.1` ; `NAS` `192.168.40.30/24`, passerelle `.40.1`.

**Partie D** : les trois pings aboutissent. Si l'imprimante ne répond pas : 1) câble et voyant du port (`show ip interface brief`, `show interfaces status`) ; 2) VLAN du port (`show vlan brief`) ; 3) adresse et passerelle de l'imprimante.

**Partie E (réponses attendues)** : caméra : VLAN 40, `192.168.40.31`, passerelle `.40.1`, PoE (vérifier le budget), mot de passe changé, test : image visible depuis un poste, risque : mot de passe par défaut / accès depuis Internet ; ESP32 : VLAN 40, `192.168.40.40`, passerelle `.40.1`, alimentation par bloc 5 V, test : la température remonte, risque : réseau Wi-Fi peu protégé / absence de mise à jour.

**Partie F** : le plan d'adressage doit comporter les 4 équipements avec VLAN, adresse, emplacement ; le journal indique date, modification, auteur.

**Contrôles automatiques** : 5/5 verts sur le corrigé.""",
)
if __name__ == "__main__":
    seance("S08", S)
