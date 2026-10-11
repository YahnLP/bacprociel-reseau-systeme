import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance

S = dict(
 prerequis="Seconde S13 à S15 (Wi-Fi), Première S08–S09 (VLAN, trunk), Terminale S05 (inter-VLAN)",
 question="Dans une entreprise, le personnel et les invités utilisent le même Wi-Fi… sans jamais se voir. Comment est-ce possible, et comment s'assurer que c'est sûr ?",
 objectifs=["**Expliquer** ce qu'est un SSID et le **relier à un VLAN**.", "**Choisir** une sécurité Wi-Fi adaptée (WPA2, WPA3, réseau ouvert) et **justifier**.", "**Mettre en service** un Wi-Fi personnel et un Wi-Fi invités **séparés** et **filtrés**.", "**Lire** un schéma d'authentification d'entreprise (RADIUS).", "**Dépanner** un Wi-Fi : clé, VLAN, filtrage, signal et canaux."],
 cours_role="SSID et VLAN ; sécurité WPA2/WPA3 ; RADIUS (lecture) ; canaux et signal",
 tp_role="Cabinet Garcia : Wi-Fi du personnel et Wi-Fi invités, puis dépannage",
 memo_role="Réglages d'une borne, commandes de vérification, check-list de dépannage Wi-Fi",
 fichiers=[("t06-wifi.json", "Simulateur : matériel posé, bornes non branchées, switch et routeur vierges"), ("t06-panne.json", "Simulateur : Wi-Fi installé mais avec 3 défauts")],
 deroule=[("0 h 00 – 0 h 20", "**Accroche** : « Ton téléphone voit 6 réseaux Wi-Fi dans la salle. Lesquels sont à nous ? »", "Classe"), ("0 h 20 – 0 h 50", "**Mini-cours** : SSID, VLAN, sécurité", "Classe"), ("0 h 50 – 1 h 50", "**TP A–C** : câbler les bornes, VLAN, sous-interfaces, DHCP", "Binôme"), ("1 h 50 – 2 h 05", "Pause", ""), ("2 h 05 – 2 h 30", "**Mini-cours** : RADIUS (lecture), canaux, signal", "Classe"), ("2 h 30 – 3 h 15", "**TP D–E** : SSID, clés, filtrage des invités", "Binôme"), ("3 h 15 – 4 h 00", "**TP F–G** : dépannage, fiche de mise en service", "Individuel")],
 materiel=["Les deux fichiers `.json` ci-dessus (à ouvrir **au départ**).", "[Aide-mémoire](03-aide-memoire.md) imprimé.", "Si possible : un téléphone avec une application d'analyse Wi-Fi pour la discussion sur les canaux (non indispensable)."],
 eval=[("**Simulateur : 6 contrôles automatiques** (adresses, accès au serveur, filtrage invités)", "Formatif"), ("**Fiche de mise en service Wi-Fi** (SSID, VLAN, sécurité, justification)", "Grille : exactitude, justification de la sécurité, test réalisé")],
 notes=["**Limite du simulateur :** une borne = **un SSID**. Pour représenter « deux SSID sur un même boîtier », on place **deux bornes**, chacune branchée sur un port d'**un VLAN différent**. Dans la réalité, **une seule borne** diffuse plusieurs SSID et les associe à des VLAN par un **trunk**. À dire clairement aux élèves.", "**RADIUS et WPA3** : présentés **en lecture** (schéma), non configurés, comme le prévoit le référentiel (authentification d'entreprise : niveau d'information).", "**Canaux et puissance** : le simulateur ne modélise pas les interférences ; la partie canaux est faite **à l'oral et sur schéma**.", "**Pannes (t06-panne)** : 1) le portable du personnel a une clé erronée (`…26` au lieu de `…27`) ; 2) la borne invités est branchée sur `Fa0/11` en **VLAN 20** (au lieu de 30) ; 3) l'ACL des invités n'est plus posée sur la sous-interface `Gi0/0.30`.", "Aucun mot de passe `enable` dans ces fichiers : la séance porte sur le Wi-Fi, pas sur la sécurisation du switch (vue en Première S14)."],
 cours_titre="Le Wi-Fi d'une entreprise",
 sauras=["expliquer le lien **SSID ↔ VLAN ↔ réseau IP** ;", "choisir entre **WPA2-Personnel**, **WPA3** et **WPA2/3-Entreprise** ;", "**isoler** un Wi-Fi invités du réseau interne ;", "dire ce que fait un **serveur RADIUS** ;", "**diagnostiquer** un problème de connexion Wi-Fi."],
 sections=[
  dict(h="Un SSID, c'est quoi ?", q="Tu vois dans ta classe les réseaux « CFA-ELEVES » et « CFA-PROFS ». Il y a **une seule borne** au plafond. Comment est-ce possible ?",
       a="Une borne peut **diffuser plusieurs SSID** (plusieurs « noms de réseau »). Chaque SSID est comme un **réseau séparé** : son nom, sa clé, son réseau IP.",
       idee="> **Un SSID = un nom de réseau Wi-Fi.** En entreprise, on associe chaque SSID à **un VLAN** : le trafic des invités et celui du personnel ne se mélangent jamais.\n\n| SSID | VLAN | Réseau IP | Qui ? |\n|---|---|---|---|\n| `GARCIA-PERSONNEL` | 20 | 192.168.20.0/24 | Le personnel |\n| `GARCIA-INVITES` | 30 | 192.168.30.0/24 | Les visiteurs |\n\nLa borne est reliée au switch par **un câble** (un *trunk* si elle diffuse plusieurs SSID, un port d'accès si elle n'en diffuse qu'un).",
       img=("wifi-vlan.svg", "Deux SSID, deux VLAN, un routeur qui filtre"),
       c="Un visiteur se connecte à `GARCIA-INVITES`. **Dans quel VLAN** arrive-t-il, et **quelle passerelle** reçoit-il ?",
       r="Dans le **VLAN 30**. Il reçoit une adresse en `192.168.30.x` et pour passerelle `192.168.30.1` (la sous-interface du routeur)."),
  dict(h="Sécuriser : la clé et le protocole", q="Un restaurant laisse son Wi-Fi **ouvert** « pour que ce soit plus simple ». Cite **un risque**.",
       a="N'importe qui peut **se connecter** (et utiliser la connexion pour des actes illégaux, c'est le propriétaire qui répond) et **espionner** les échanges non chiffrés des autres clients.",
       idee="| Protocole | Clé | À retenir |\n|---|---|---|\n| **Ouvert** | aucune | À éviter, ou avec **portail captif** pour un accueil du public |\n| **WPA2-Personnel (PSK)** | une clé partagée | Standard actuel des petits réseaux ; clé **longue**, à **changer** quand un salarié part |\n| **WPA3-Personnel** | une clé partagée | Plus résistant au piratage de la clé ; si les équipements le gèrent |\n| **WPA2/WPA3-Entreprise** | **un compte par personne** (RADIUS) | Le plus sûr : on retire **un** compte sans changer la clé de tous |\n\n> [!WARNING]\n> **WEP** et **WPA (v1)** sont **cassés** : on les remplace.",
       c="Un salarié part de l'entreprise. Le Wi-Fi est en **WPA2-Personnel**. Que faut-il faire ? Et en WPA2-Entreprise ?",
       r="En PSK : **changer la clé** et la redonner à **tous** les autres. En Entreprise : **désactiver son compte** seulement, personne d'autre n'est dérangé."),
  dict(h="RADIUS : l'authentification d'entreprise (lecture)", q="À l'entrée d'un immeuble, le gardien ne connaît pas tous les visiteurs. Qui lui dit s'il peut laisser entrer ?",
       a="Il **téléphone à l'accueil** qui a la **liste** des personnes autorisées. Le gardien exécute, l'accueil décide.",
       idee="> La **borne** joue le gardien ; le **serveur RADIUS** joue l'accueil : il détient la liste des comptes.\n\n```text\nPortable ──identifiants──► Borne ──question──► Serveur RADIUS\nPortable ◄──accès accordé── Borne ◄──réponse──── (annuaire : comptes)\n```\n\nTu **ne configures pas** RADIUS en Terminale ; tu dois savoir le **lire sur un schéma** et dire **pourquoi** on l'utilise : un compte par personne, retrait immédiat, traçabilité.",
       c="Sur un schéma, une flèche relie la borne à un serveur marqué « RADIUS ». **Que se passe-t-il** quand un salarié saisit son identifiant ?",
       r="La borne **transmet** les identifiants au serveur RADIUS, qui **répond oui ou non**. Si oui, la borne autorise la connexion (et peut placer le client dans un VLAN selon son groupe)."),
  dict(h="Canaux et signal : pourquoi ça rame", q="Dans un immeuble, **dix** box diffusent sur le **même canal**. Que se passe-t-il ?",
       a="Elles se **gênent** : comme dix personnes qui parlent en même temps dans une pièce. Les débits chutent.",
       idee="| Bande | Portée | Débit | Canaux sans chevauchement |\n|---|---|---|---|\n| **2,4 GHz** | grande | modeste | **1, 6, 11** seulement (3 canaux) |\n| **5 GHz** | moyenne | élevé | beaucoup (selon la largeur) |\n\n**Réflexes de dépannage :** 1) le **signal** est-il suffisant (distance, murs) ? 2) le **canal** est-il saturé ? 3) la **clé** est-elle bonne ? 4) le client est-il dans le **bon VLAN** ? 5) le **DHCP** répond-il ?",
       c="Un portable se connecte au Wi-Fi mais obtient `169.254.x.x`. **Wi-Fi ou DHCP ?**",
       r="Le **Wi-Fi fonctionne** (il est associé à la borne) ; c'est le **DHCP** qui ne répond pas (mauvais VLAN, serveur DHCP éteint, relais absent). Chercher côté réseau, pas côté radio."),
 ],
 retenir=["**SSID = nom de réseau ; VLAN = séparation ; ACL = règles.**", "**Invités** : VLAN dédié + **aucun accès** au réseau interne.", "**WPA2/WPA3**, jamais WEP ; **Entreprise** = un compte par personne (RADIUS).", "**Dépannage** : signal → clé → VLAN → DHCP.", "**Ne jamais** laisser le même mot de passe Wi-Fi des années."],
 tp_titre="Le Wi-Fi du cabinet Garcia", tp_format="binôme, on **échange les rôles** à chaque partie", tp_temps="3 h 30",
 mission="Le **cabinet Garcia** veut deux Wi-Fi : un pour le **personnel** (accès au serveur interne) et un pour les **invités** (accès limité). Tu câbles les bornes, tu crées les VLAN, tu configures le routeur et le DHCP, tu **filtres** les invités, puis tu **dépannes** une installation défectueuse.",
 memo_titre="Wi-Fi d'entreprise",
 tp="""**Binôme :** ____________ / ____________

Ouvre le [simulateur](../../simulateur/simulateur-reseau.html), puis **Ouvre** [`t06-wifi.json`](tp/t06-wifi.json).

| Équipement | VLAN | Réseau | Branché sur |
|---|---|---|---|
| `PC-GES`, `SRV` | 10 (GESTION) | 192.168.10.0/24 (déjà adressés, passerelle .1) | SW1 Fa0/1 et Fa0/2 |
| `AP-INT` (SSID personnel) | 20 | 192.168.20.0/24 | SW1 **Fa0/10** |
| `AP-INV` (SSID invités) | 30 | 192.168.30.0/24 | SW1 **Fa0/11** |
| `R1` | – | .1 de chaque réseau | SW1 **Fa0/24** (trunk) |

> [!NOTE]
> Dans le simulateur, une borne diffuse **un** SSID. On utilise donc **deux bornes** pour représenter les deux SSID d'une borne réelle (voir le cours).

## Partie A – Prévoir (≈ 10 min)

Avant de configurer, **note ce que tu prévois** :

| Test | Prévision | Résultat |
|---|---|---|
| `LAP-PERS` se connecte-t-il au Wi-Fi ? | | |
| `LAP-INV` a-t-il une adresse ? | | |

## Partie B – Câbler et créer les VLAN (≈ 40 min)

1. **Câble** `AP-INT` (port `eth0`) sur `SW1 Fa0/10` et `AP-INV` sur `SW1 Fa0/11`.
2. Sur **SW1** : crée les **VLAN 10, 20, 30** (avec noms), place les ports d'accès (`Fa0/1-2` → 10 ; `Fa0/10` → 20 ; `Fa0/11` → 30) et mets `Fa0/24` en **trunk**.

✅ **Points de contrôle :** `show vlan brief` (3 VLAN, bons ports) ; `show interfaces trunk` (`Fa0/24` en trunk).

❓ **Pourquoi `Fa0/10` et `Fa0/11` sont-ils en mode *access* et pas *trunk* ici ?** ______________

## Partie C – Le routeur et le DHCP (≈ 40 min)

Sur `R1` : `gi0/0` en `no shutdown`, **trois sous-interfaces** (`.10`, `.20`, `.30`), puis **deux pools DHCP** (`PERSONNEL`, `INVITES`) :

```text
ip dhcp excluded-address 192.168.20.1 192.168.20.9
ip dhcp pool PERSONNEL
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
```

✅ **Points de contrôle :** `show ip interface brief` (4 interfaces `up`) ; `show ip dhcp pool`.

❓ **Pourquoi exclut-on `.1` à `.9` du pool ?** ______________

## Partie D – Les SSID et les clés (≈ 30 min)

Double-clique sur chaque **borne** et règle :

| Borne | SSID | Clé | Sécurité |
|---|---|---|---|
| `AP-INT` | `GARCIA-PERSONNEL` | `Perso#Garcia27` | WPA2 |
| `AP-INV` | `GARCIA-INVITES` | `Invites2027` | WPA2 |

Double-clique sur chaque **portable** et renseigne le SSID et la clé correspondants (`LAP-PERS` → personnel ; `LAP-INV` → invités).

✅ **Points de contrôle :** `LAP-PERS` : `ipconfig` → `192.168.20.x` ; `LAP-INV` → `192.168.30.x`.

## Partie E – Filtrer les invités (≈ 30 min)

**Exigence :** *« Les invités ne voient ni le réseau de gestion ni le Wi-Fi du personnel. »*

1. Écris l'ACL `INVITES-IN` (deux `deny` + `permit ip any any`) et pose-la **`in`** sur `gi0/0.30`.
2. **Teste :**

| Test | Attendu | Obtenu |
|---|---|---|
| `LAP-PERS` → `ping 192.168.10.10` | ✓ | |
| `LAP-INV` → `ping 192.168.10.10` | ✗ | |
| `LAP-INV` → ping de l'adresse de `LAP-PERS` | ✗ | |
| `LAP-INV` → `ping 192.168.30.1` | ✓ | |

❓ **Pourquoi laisse-t-on les invités joindre `192.168.30.1` ?** (indice : c'est leur passerelle et leur DHCP) ______________

## Partie F – Dépanner (≈ 40 min, individuel)

Ouvre [`t06-panne.json`](tp/t06-panne.json). Le Wi-Fi a été installé, mais **trois choses ne vont pas**. Démarche : **symptôme → hypothèses → test → correction**.

| Symptôme observé | Hypothèse | Test | Cause trouvée | Correction |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

✅ **Quand c'est fini :** les six tests de la partie E sont conformes.

## Partie G – Fiche de mise en service (≈ 20 min)

Complète pour ton client :

| Élément | Valeur |
|---|---|
| SSID personnel / VLAN / sécurité | |
| SSID invités / VLAN / sécurité | |
| Pourquoi cette sécurité ? | |
| Qui connaît les clés ? Quand les changer ? | |
| Test final réalisé (date, résultat) | |

## 🏁 Ce que je sais faire maintenant

| Je sais… | Pas encore | Avec aide | Seul(e) |
|---|---|---|---|
| associer un SSID à un VLAN | ☐ | ☐ | ☐ |
| isoler un Wi-Fi invités | ☐ | ☐ | ☐ |
| dépanner un Wi-Fi avec une méthode | ☐ | ☐ | ☐ |
""",
 memo="""## Réglages d'une borne

| Réglage | À vérifier |
|---|---|
| **SSID** | Nom exact (majuscules !) |
| **Clé** | Identique sur la borne et sur le client |
| **Sécurité** | WPA2 ou WPA3 (jamais WEP) |
| **Port du switch** | Bon VLAN (access) ou trunk si plusieurs SSID |

## Commandes utiles

```text
show vlan brief
show interfaces trunk
show ip dhcp pool
show ip dhcp binding
show access-lists
```

Côté poste : `ipconfig` (Windows) · `ip a` (Linux).

## Dépannage Wi-Fi : l'ordre des tests

1. **Signal** suffisant ? 2. **Clé** correcte ? 3. **Adresse** reçue (`169.254` = DHCP) ? 4. **Bon VLAN** ? 5. **Passerelle** joignable ? 6. **ACL** : bloque-t-elle trop ?
""",
 corrige="""Fichiers : `T06-wifi-corrige.json`, `T06-panne-corrige.json`.

**Partie A** : avant configuration, les portables ne se connectent pas (bornes non branchées) ou n'ont pas d'adresse.

**Partie B** : `Fa0/10` et `Fa0/11` sont en **access** car chaque borne simulée diffuse un seul SSID, donc un seul VLAN. Une borne réelle à plusieurs SSID serait sur un **trunk**.

**Partie C** : sous-interfaces `.10/.20/.30`, pools `PERSONNEL` et `INVITES`. On exclut `.1`–`.9` pour réserver les adresses des équipements (la passerelle ne doit pas être distribuée).

**Partie D** : SSID/clés comme indiqué. `LAP-PERS` : `192.168.20.x` ; `LAP-INV` : `192.168.30.x`.

**Partie E** : `INVITES-IN` : `deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255` ; `deny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255` ; `permit ip any any` ; `in` sur `gi0/0.30`. Les invités gardent l'accès à `192.168.30.1` (DHCP, passerelle).

**Partie F (pannes)** : 1) `LAP-PERS` : clé `Perso#Garcia27` (était `…26`) → pas de connexion ; 2) `SW1 Fa0/11` : `switchport access vlan 30` (était 20) → invités dans le VLAN du personnel ; 3) `R1 gi0/0.30` : `ip access-group INVITES-IN in` (retiré).

**Contrôles automatiques** : 6/6 verts sur les deux corrigés.""",
)
if __name__ == "__main__":
    seance("S06", S)
