import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from seance import seance

S = dict(
 prerequis="Première S10 (SSH), S14 (sécurité de base), Terminale S05, S07",
 question="Un technicien doit dépanner l'entreprise du soir depuis chez lui. Comment entre-t-il, sans que n'importe qui puisse faire pareil ?",
 objectifs=["**Administrer** un routeur par **SSH** et **désactiver** telnet.", "**Publier** un service interne par une **redirection de port** (NAT/PAT) et **mesurer les risques**.", "**Expliquer** ce qu'est un **VPN** et l'**utiliser** quand il est déjà configuré.", "**Appliquer** les règles de télémaintenance (autorisation, compte nominatif, journal)."],
 cours_role="SSH vs telnet ; redirection de port ; VPN ; règles de télémaintenance",
 tp_role="Garage Dupuy : routeur en SSH, site interne publié, test depuis l'extérieur",
 memo_role="Commandes SSH et NAT, tableau de risques, fiche de télémaintenance",
 fichiers=[("t09-acces.json", "Simulateur : routeur en telnet, site interne non publié, poste « technicien à distance » côté Internet")],
 deroule=[("0 h 00 – 0 h 20", "**Accroche** : « Une caméra de surveillance est piratée parce qu'elle était visible depuis Internet. Comment ? »", "Classe"), ("0 h 20 – 0 h 50", "**Mini-cours** : SSH, telnet, redirection de port", "Classe"), ("0 h 50 – 2 h 00", "**TP A–C** : passer en SSH, tester", "Binôme"), ("2 h 00 – 2 h 15", "Pause", ""), ("2 h 15 – 2 h 45", "**Mini-cours** : VPN, télémaintenance", "Classe"), ("2 h 45 – 3 h 30", "**TP D–E** : publier le site, tester de l'extérieur", "Binôme"), ("3 h 30 – 4 h 00", "**TP F** : fiche de télémaintenance", "Individuel")],
 materiel=["Le fichier `t09-acces.json`.", "Optionnel : accès à un VPN déjà configuré sur le plateau (observation), sinon la partie VPN est travaillée **sur fiche**.", "[Aide-mémoire](03-aide-memoire.md) imprimé."],
 eval=[("**Simulateur : 6 contrôles automatiques** (SSH, NAT, redirection, sauvegarde)", "Formatif"), ("**Fiche de télémaintenance** remplie", "Grille : autorisation, compte, périmètre, durée, trace")],
 notes=["**Le TP** est conçu sur un routeur (NAT en surcharge + redirection `ip nat inside source static tcp … 8080`). Le poste « Technicien à distance » est branché côté Internet pour tester **de l'extérieur**.", "**Limite du simulateur :** `transport input ssh` est **mémorisé** (visible dans `show running-config`) mais **non appliqué** : telnet reste possible. À dire aux élèves ; sur du matériel réel du plateau, le tester.", "**Authentification SSH par clé** : présentée **à l'oral** ; le simulateur ne gère pas les clés. Elle peut être travaillée sur le **serveur Ubuntu** du plateau (voir Première S10).", "**VPN** : le référentiel demande d'**utiliser un VPN déjà configuré**, pas de le monter. Le simulateur propose des VPN (menu dédié) mais ce n'est pas testé dans ce TP : voir la fiche écrite en partie F.", "**Bureau à distance (RDP)** : mentionné ; ne jamais l'exposer directement sur Internet (cible n°1 des attaques).", "**Panne de 2e tour** : si les élèves publient `80` au lieu de `8080`, le test « port 80 non joignable » échoue : bonne occasion de discuter du risque d'exposer un port standard."],
 corriges_extra=", `T09-acces-corrige.json`",
 cours_titre="Accéder à distance, en sécurité",
 sauras=["expliquer pourquoi **telnet** est dangereux et **SSH** protégé ;", "configurer **SSH** sur un routeur ;", "**publier** un service par redirection de port et **en citer les risques** ;", "dire à quoi sert un **VPN** ;", "**appliquer** les règles de télémaintenance."],
 sections=[
  dict(h="Telnet ou SSH ?", q="Tu te connectes à un routeur depuis un café. Le mot de passe passe **en clair** dans le Wi-Fi. **Qui peut le lire ?**",
       a="**Toute personne** qui écoute le Wi-Fi ou un point du chemin (appareil compromis, réseau public). Avec telnet, le mot de passe voyage **tel quel**.",
       idee="| | Telnet | SSH |\n|---|---|---|\n| Port | 23 | 22 |\n| Chiffrement | **non** | **oui** |\n| Mot de passe | visible en clair | protégé |\n| Usage | à **bannir** | à **utiliser** |\n\n```text\nip domain-name garage.local\nusername tech privilege 15 secret Tech#2027\ncrypto key generate rsa modulus 1024\nip ssh version 2\nline vty 0 4\n transport input ssh\n login local\n```\n\nPuis de ton poste : `ssh tech@192.168.1.1`.\n\n> [!TIP]\n> **Un compte nominatif par technicien** (`tech`, `lucas`, …) : on sait **qui** a fait **quoi**, et on retire un compte sans changer celui des autres.",
       c="Que signifie `transport input ssh` sur les lignes `vty` ?",
       r="Que **seul SSH** est accepté pour se connecter à distance : **telnet est refusé**."),
  dict(h="La redirection de port : montrer un service à Internet", q="Un restaurateur veut que ses clients voient sa carte sur un petit serveur installé **dans** son local. Comment un visiteur d'Internet peut-il l'atteindre, alors que le serveur a une adresse **privée** ?",
       a="Il ne peut **pas** l'atteindre directement (adresse privée). Il faut que le routeur **redirige** les connexions arrivant sur son adresse **publique** vers le serveur : c'est la **redirection de port**.",
       idee="```text\nip nat inside source static tcp 192.168.1.10 80 203.0.113.3 8080\n```\n\n« Ce qui arrive sur **203.0.113.3 : 8080** est envoyé vers **192.168.1.10 : 80**. »\n\n> [!WARNING]\n> **Un port ouvert est visible de tous** : des robots scannent Internet en permanence. On ne publie que **le strict nécessaire**, on **protège** le service (mot de passe fort, mises à jour) et on le place si possible dans une zone isolée.\n\n| Service | À exposer directement sur Internet ? |\n|---|---|\n| Site web public | oui, avec précautions |\n| **Bureau à distance (RDP)** | **jamais** : passer par un **VPN** |\n| Administration du routeur | **jamais** : passer par un **VPN** |",
       c="Pourquoi utilise-t-on le port **8080** à l'extérieur alors que le serveur écoute sur le **80** ?",
       r="Pour **ne pas utiliser le port standard** (très scanné) et pour pouvoir publier **plusieurs** services : 8080 → serveur A, 8081 → serveur B. Les postes de l'extérieur doivent alors taper `:8080`."),
  dict(h="Le VPN : entrer dans le réseau comme si on y était", q="Un commercial est en déplacement et veut accéder au **dossier partagé** de l'entreprise. Publier le serveur de fichiers sur Internet, est-ce une bonne idée ?",
       a="**Non**, c'est dangereux. La bonne solution est un **VPN**.",
       idee="> **Un VPN est un tunnel chiffré** entre ton poste et le réseau de l'entreprise. Une fois connecté, tu es **comme au bureau** (adresse interne, accès aux dossiers) sans exposer les serveurs.\n\n| | Redirection de port | VPN |\n|---|---|---|\n| Ce qui est exposé | le service | **uniquement** la porte d'entrée du VPN |\n| Authentification | celle du service | compte (+ souvent code) |\n| Risque | élevé | **plus faible** |\n\nEn Terminale, tu **utilises un VPN déjà configuré** : tu vérifies la connexion (adresse reçue, accès au serveur) et tu sais l'expliquer.",
       c="Tu es connecté en VPN depuis chez toi. **Quelle adresse** as-tu pour le serveur de fichiers ?",
       r="L'adresse **interne** (par ex. `192.168.1.10`), comme si tu étais sur place : c'est tout l'intérêt du VPN."),
  dict(h="Les règles de télémaintenance", q="Un technicien se connecte la nuit au réseau d'un client « pour aider ». Le client ne le sait pas. **Qu'est-ce qui ne va pas ?**",
       a="**Tout** : pas d'**autorisation**, pas de **trace**. Même bien intentionné, c'est une **intrusion** dans un système informatique.",
       idee="**Avant une intervention à distance :**\n\n1. **Autorisation** du client (écrite, même par e-mail).\n2. **Compte nominatif** du technicien (pas de compte partagé).\n3. **Périmètre** : quels équipements, quelle durée.\n4. **Journal** : date, heure, actions, résultat.\n5. **Fermeture** : on retire ou désactive l'accès à la fin.",
       c="Un collègue te donne le mot de passe du compte `admin` pour que tu dépannes à sa place. **Que dis-tu ?**",
       r="Que chacun doit avoir **son propre compte** : sinon on ne sait plus **qui** a fait **quoi**, et on ne peut pas retirer l'accès d'un seul."),
 ],
 retenir=["**SSH (22) chiffre ; telnet (23) non.** `transport input ssh`.", "**Compte nominatif** par technicien.", "**Redirection de port** : un port ouvert est vu de tous ; on publie le **minimum**.", "**VPN** : tunnel chiffré, on entre **dans** le réseau sans exposer les serveurs.", "**Télémaintenance** : autorisation, compte, périmètre, journal."],
 tp_titre="Garage Dupuy : accès à distance", tp_format="binôme", tp_temps="3 h 30",
 mission="Le **garage Dupuy** administre son routeur en **telnet** et voudrait montrer son **intranet** (site web interne) à un technicien à distance. Tu sécurises l'administration, tu **publies** le site par une redirection de port, tu testes **depuis l'extérieur** et tu remplis une **fiche de télémaintenance**.",
 memo_titre="Accès à distance",
 tp="""**Binôme :** ____________ / ____________

Ouvre le [simulateur](../../simulateur/simulateur-reseau.html), puis **Ouvre** [`t09-acces.json`](tp/t09-acces.json).

| Équipement | Adresse | Rôle |
|---|---|---|
| `R1` | 192.168.1.1 (LAN) / 203.0.113.3 (WAN) | Routeur du garage |
| `PC-ADM` | 192.168.1.50 | Poste de l'administrateur |
| `SRV` | 192.168.1.10 | Serveur web interne (intranet) |
| `DISTANT` | 198.51.100.100 | Poste du technicien, **côté Internet** |

## Partie A – Constater (≈ 20 min)

1. Depuis `PC-ADM`, ouvre `http://www.exemple.fr` : Internet fonctionne-t-il ? ______________
2. Depuis `DISTANT`, ouvre `http://203.0.113.3:8080`. Que se passe-t-il ? ______________
3. Depuis `PC-ADM`, tape `telnet 192.168.1.1`. Peux-tu te connecter ? Que voit-on passer ? ______________

## Partie B – Passer en SSH (≈ 40 min)

Sur `R1` : **domaine**, **compte nominatif** `tech` (mot de passe `Tech#2027`), **clés RSA**, **SSH version 2**, lignes `vty 0 4` avec `transport input ssh` et `login local`. Puis `write memory`.

✅ **Points de contrôle :**
- depuis `PC-ADM` : `ssh tech@192.168.1.1` fonctionne ;
- `telnet 192.168.1.1` : **sur du matériel réel**, il serait refusé ; **le simulateur n'applique pas cette règle** (il mémorise seulement la configuration) : tu **vérifies donc la ligne `transport input ssh`** dans `show running-config` ;
- `show running-config` contient `transport input ssh`.

❓ **Pourquoi `login local` (et pas un simple mot de passe de ligne) ?** ______________

## Partie C – Publier l'intranet (≈ 40 min)

Sur `R1` : redirige **le port 8080** de l'adresse WAN `203.0.113.3` vers **`192.168.1.10` port 80**.

✅ **Points de contrôle :**
- depuis `DISTANT` : `http://203.0.113.3:8080` affiche « Intranet du garage Dupuy » ;
- `http://203.0.113.3` (port 80) **ne répond pas** ;
- `show ip nat translations` montre la redirection.

## Partie D – Mesurer les risques (≈ 30 min)

| Question | Ta réponse |
|---|---|
| Qui peut ouvrir `http://203.0.113.3:8080` maintenant ? | |
| Quel risque si l'intranet contient des informations clients ? | |
| Que faut-il ajouter pour **protéger** ce service ? (3 idées) | |
| Faut-il publier le **bureau à distance** du serveur de la même façon ? Pourquoi ? | |

## Partie E – Sauvegarder et documenter (≈ 20 min)

`write memory`, puis note dans ton **journal** (voir [S07](../S07-maj-sauvegardes/01-cours.md)) : date, équipement, modification, **pourquoi**.

## Partie F – Fiche de télémaintenance (≈ 40 min, individuel)

Le garage demande qu'un technicien puisse **dépanner le serveur à distance** pendant une semaine. Remplis la fiche :

| Élément | À remplir |
|---|---|
| Qui autorise (nom, date, moyen) ? | |
| Compte du technicien (nominatif ?) | |
| Méthode d'accès (SSH, VPN, autre) et **pourquoi** | |
| Équipements concernés | |
| Durée de l'autorisation | |
| Comment l'accès est **fermé** ensuite | |
| Où est tracée l'intervention ? | |

## 🏁 Ce que je sais faire maintenant

| Je sais… | Pas encore | Avec aide | Seul(e) |
|---|---|---|---|
| configurer SSH et refuser telnet | ☐ | ☐ | ☐ |
| publier un service par redirection de port | ☐ | ☐ | ☐ |
| expliquer le risque d'un port ouvert | ☐ | ☐ | ☐ |
| utiliser un VPN (déjà configuré) | ☐ | ☐ | ☐ |
""",
 memo="""## SSH sur un routeur ou un switch

```text
ip domain-name garage.local
username tech privilege 15 secret Tech#2027
crypto key generate rsa modulus 1024
ip ssh version 2
line vty 0 4
 transport input ssh
 login local
```

Connexion : `ssh tech@192.168.1.1`.

## Redirection de port (NAT statique)

```text
ip nat inside source static tcp <ip-interne> <port-interne> <ip-publique> <port-externe>
show ip nat translations
```

## Réflexes

- Jamais de **telnet**. Jamais de **bureau à distance** exposé.
- Un port ouvert = un risque : **le moins possible**.
- **VPN** pour entrer dans le réseau.

## Fiche de télémaintenance

Autorisation · Compte nominatif · Périmètre · Durée · Fermeture · Journal.
""",
 corrige="""Fichier : `T09-acces-corrige.json`.

**Partie A** : Internet fonctionne (NAT en surcharge) ; depuis `DISTANT`, le port 8080 ne répond pas ; telnet fonctionne et le mot de passe y est transmis en clair (visible dans une capture).

**Partie B** : `ip domain-name`, `username tech privilege 15 secret …`, `crypto key generate rsa modulus 1024`, `ip ssh version 2`, `line vty 0 4` + `transport input ssh` + `login local`, `write memory`. `login local` : chaque technicien utilise **son** compte.

**Partie C** : `ip nat inside source static tcp 192.168.1.10 80 203.0.113.3 8080`. Le port 80 de l'adresse WAN **n'est pas** redirigé : le test échoue, c'est normal.

**Partie D (réponses attendues)** : tout Internet ; fuite possible d'informations ; protections : authentification sur le site, HTTPS, mises à jour, filtrage par adresse source, ou VPN à la place ; bureau à distance : **jamais** exposé directement (attaques automatiques) → VPN.

**Partie F** : la fiche doit comporter une autorisation écrite, un compte nominatif, un VPN ou SSH justifié, une durée d'une semaine, la suppression du compte à la fin, et une trace dans le journal.

**Contrôles automatiques** : 6/6 verts sur le corrigé (le refus de telnet n'est vérifié que par la configuration).""",
)
if __name__ == "__main__":
    seance("S09", S)
