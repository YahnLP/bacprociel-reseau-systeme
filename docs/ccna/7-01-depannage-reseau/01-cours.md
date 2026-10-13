# 🔧 Dépanner un réseau : la méthode

*Parcours CCNA – Domaine 7 (transversal) – module 7-01*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Ce module **rassemble** tout ce que tu as vu dans les dépannages des modules précédents. À faire en dernier, ou à tout moment si tu veux apprendre à **chercher une panne sans deviner**. Il correspond au thème « dépannage » (*troubleshooting*) de l'examen CCNA, qui traverse tous les domaines.

## 🎯 À la fin de ce cours, tu sauras

- appliquer une **méthode** en étapes plutôt que tester « au hasard » ;
- **localiser** une panne par couche avec `ping`, `traceroute` et les commandes `show` ;
- **lire** les messages d'erreur d'un `ping` pour savoir *où* chercher ;
- tenir un **journal de dépannage** que tu peux montrer à un client ou dans ton dossier de preuves.

---

## 1. Pourquoi une méthode ?

Face à un réseau en panne, la tentation est de « tout essayer ». C'est lent, et pire : **chaque changement au hasard peut créer une nouvelle panne** tout en masquant la première. Un technicien efficace fait l'inverse : il **observe**, il **choisit une hypothèse**, il **la teste avec une commande**, puis il **corrige une seule chose** et **vérifie**.

> [!WARNING]
> **Les trois erreurs qui font perdre une heure :** (1) changer plusieurs choses à la fois ; (2) ne pas lire le message d'erreur ; (3) croire que « ça marche » parce qu'un seul test est passé.

## 2. Les sept étapes

| # | Étape | Question à se poser | Exemple |
|---|---|---|---|
| 1 | **Décrire le symptôme** | Qu'est-ce qui ne marche pas, depuis quel poste, vers quoi ? | « `PC20` ne joint pas le serveur ; `PC10` si » |
| 2 | **Délimiter** | Qui est touché ? Un poste, un VLAN, tout le monde ? | « Seul le VLAN 20 est touché » |
| 3 | **Chercher le changement** | Qu'est-ce qui a été modifié depuis que ça marchait ? | « Quelqu'un a touché au trunk hier » |
| 4 | **Poser des hypothèses par couche** | Du plus simple (câble, interface) au plus complexe (routage, services) | « Le port du poste est-il dans le bon VLAN ? » |
| 5 | **Tester une hypothèse à la fois** | Quelle commande la confirme ou l'élimine ? | `show vlan brief` |
| 6 | **Corriger, un seul changement** | Si je change deux choses, saurai-je laquelle a réparé ? | corriger le port, retester |
| 7 | **Vérifier et documenter** | Tout marche-t-il vraiment ? Qu'écrire au journal ? | cause, correctif, preuve |

## 3. Raisonner par couches

On teste **de bas en haut** : tant qu'une couche basse est en panne, inutile de chercher plus haut.

| Couche | Question | Commandes Cisco | Signes d'une panne |
|---|---|---|---|
| **1 – Physique** | Le lien existe-t-il ? | `show interfaces status`, `show ip interface brief` | `notconnect`, `down/down`, `administratively down` |
| **2 – Liaison** | Le port est-il dans le bon VLAN ? Le trunk transporte-t-il le VLAN ? | `show vlan brief`, `show interfaces trunk`, `show mac address-table`, `show etherchannel summary`, `show spanning-tree` | port dans un autre VLAN, VLAN absent du trunk, `err-disabled`, ports `(I)` |
| **3 – Réseau** | L'adresse, le masque, la passerelle, les routes sont-ils justes ? | `show ip interface brief`, `show ip route`, `ping`, `traceroute`, `show ip ospf neighbor`, `show ip nat translations` | pas de route, route de retour absente, voisin OSPF absent |
| **4 – Transport / filtrage** | Un filtre bloque-t-il le port ? | `show access-lists`, `show ip interface` | compteur du `deny` qui monte, ACL au mauvais sens |
| **7 – Application / service** | Le service répond-il ? | `curl`, navigateur, `nslookup` | le ping passe mais le service non (ACL, port, service arrêté) |

> [!TIP]
> **Trois façons de s'y prendre.** *Bas en haut* (couche 1 puis 2 puis 3…) : sûre, adaptée quand on ne sait rien. *Haut en bas* : on part de l'application, utile quand le symptôme est précis. *Diviser pour régner* : on teste au **milieu** du chemin (par exemple le routeur central) pour savoir de quel côté se trouve la panne. En pratique, on combine.

## 4. L'échelle du ping

Un seul `ping` vers la destination finale dit seulement « ça marche » ou « non ». Pour **localiser**, on pinge **de plus en plus loin** et on s'arrête au premier échec :

| Test | Ce qu'il prouve |
|---|---|
| ① `ping` de **sa propre adresse IP** | la pile réseau du poste fonctionne |
| ② `ping` d'un poste **du même VLAN** | VLAN du port, switch, câble |
| ③ `ping` de la **passerelle** | le poste est bien dans le bon VLAN, le routeur répond |
| ④ `ping` d'un poste **d'un autre réseau** | routage aller **et** retour |
| ⑤ `ping` d'un **nom** (ex. `www.exemple.fr`) | DNS |

Le premier test qui échoue **désigne la couche à examiner**.

## 5. Lire les messages d'un `ping`

Ces messages ont été relevés dans le simulateur :

| Message | Qui le dit | Ce que ça signifie | Où chercher |
|---|---|---|---|
| `From 192.168.20.10 … Destination Host Unreachable` (l'adresse **du poste lui-même**) | le poste | il **n'a pas obtenu de réponse ARP** pour la cible ou la passerelle | couche 1 et 2 : VLAN du port, câble, trunk |
| `From 192.168.10.1 … Destination Net Unreachable` (l'adresse **d'un routeur**) | un routeur | ce routeur **n'a pas de route** vers la destination | couche 3 : `show ip route` sur **ce** routeur |
| Aucun message, `100% packet loss` | personne | un paquet s'est **perdu en silence** | route de retour absente, ACL, NAT |

> [!NOTE]
> La différence entre **« Host Unreachable » du poste** et **« Net Unreachable » d'un routeur** est l'indice le plus utile d'un ping : le premier dit *« je n'arrive même pas jusqu'à mon voisin »*, le second dit *« j'ai trouvé mon routeur, c'est lui qui ne sait pas où envoyer »*.

## 6. `traceroute` : trouver le saut où ça s'arrête

```text
PC1$ traceroute 192.168.3.10
 1  192.168.1.1   0.231 ms     <- R1 répond
 2  10.0.12.2     0.332 ms     <- R2 répond
 3  * * *                      <- plus rien
```

Le dernier saut qui répond est **le dernier équipement atteint**. La panne se trouve **juste derrière** : soit l'équipement suivant n'a pas de route (aller), soit **il ne sait pas renvoyer la réponse** (retour). Pour trancher, on se place sur cet équipement et on inspecte sa table de routage.

> [!WARNING]
> Dans le simulateur, quand un routeur répond « Net Unreachable », `traceroute` peut répéter plusieurs fois l'adresse de ce routeur : c'est un détail d'affichage du simulateur, la panne est bien **sur ce routeur**.

## 7. La fiche réflexe : symptôme → première commande

| Symptôme | Première commande | Cause fréquente | Module |
|---|---|---|---|
| Un poste n'a aucun lien | `show interfaces status` | câble, `shutdown`, `err-disabled` | [2-01](../2-01-commutation-vlan/01-cours.md), [5-04](../5-04-securite-couche2/01-cours.md) |
| Un poste ne joint pas son voisin du même VLAN | `show vlan brief` | mauvais VLAN, VLAN supprimé | [2-01](../2-01-commutation-vlan/01-cours.md) |
| Un VLAN ne passe plus entre switchs | `show interfaces trunk` | VLAN absent de `allowed vlan` | [2-02](../2-02-trunk-inter-vlan/01-cours.md) |
| Un VLAN n'a plus de passerelle | `show running-config interface gi0/0.X` | mauvais `encapsulation dot1Q` | [2-02](../2-02-trunk-inter-vlan/01-cours.md) |
| Le faisceau ne se forme pas | `show etherchannel summary` | `passive` + `passive`, modes incompatibles | [2-03](../2-03-lldp-etherchannel/01-cours.md) |
| Le trafic prend un chemin inattendu | `show spanning-tree root` | un switch a pris le rôle de racine | [2-04](../2-04-stp/01-cours.md) |
| Ping aller sans réponse | `traceroute`, puis `show ip route` du dernier saut | route de retour absente | [3-02](../3-02-routage-statique/01-cours.md) |
| Ping OK mais chemin bizarre | `show ip route static` | route principale perdue, secours actif | [3-02](../3-02-routage-statique/01-cours.md) |
| Pas de voisin OSPF | `show ip ospf neighbor`, `show ip ospf interface` | passive, zone, hello/dead | [3-03](../3-03-ospf/01-cours.md) |
| Pas d'accès à Internet | `show ip nat statistics`, `show access-lists` | `inside`/`outside` oublié, ACL fausse | [4-01](../4-01-nat/01-cours.md) |
| Pas d'adresse IP sur le poste | `ip a` / `ipconfig`, `show ip dhcp binding` | relais DHCP absent | [4-02](../4-02-dhcp-dns/01-cours.md) |
| Un service bloqué ou ouvert à tort | `show access-lists`, `show ip interface` | sens ou ordre de l'ACL | [5-03](../5-03-acl/01-cours.md) |
| Port `err-disabled` | `show port-security` | violation de sécurité de port | [5-04](../5-04-securite-couche2/01-cours.md) |

## 8. Le journal de dépannage

Pour **chaque** panne, écris :

| Champ | Exemple |
|---|---|
| **Symptôme** | `PC20` ne joint pas sa passerelle |
| **Ce que j'ai testé** (dans l'ordre) | ping passerelle ; `show vlan brief` |
| **Ce que j'ai observé** | `Fa0/2` est dans le VLAN 10 |
| **Cause** | port affecté au mauvais VLAN |
| **Correction** (une seule) | `switchport access vlan 20` sur `Fa0/2` |
| **Vérification** | ping passerelle OK ; ping serveur OK |
| **Pour que ça ne se reproduise pas** | documenter les affectations de ports |

C'est exactement la forme d'un **ticket d'incident** en entreprise, et une très bonne pièce pour ton **livret de preuves**.

---

## 🧠 Quiz de fin

**1.** `ping` répond « Destination Host Unreachable » avec l'adresse **du poste lui-même**. Quelle couche examiner ?

<details markdown="1"><summary>Voir la réponse</summary>

La **couche 1/2** : le poste n'obtient pas de réponse ARP (mauvais VLAN, câble, trunk), avant même d'arriver à un routeur.

</details>

**2.** `traceroute` s'arrête après `R2` alors que la route aller est correcte. Que soupçonnes-tu ?

<details markdown="1"><summary>Voir la réponse</summary>

Une **route de retour absente** sur l'équipement qui suit (ici `R3`) : le paquet arrive, la réponse ne revient pas.

</details>

**3.** Pourquoi ne faut-il corriger qu'**une chose à la fois** ?

<details markdown="1"><summary>Voir la réponse</summary>

Pour savoir **quel changement a réparé** la panne (et ne pas en créer une autre).

</details>

**4.** Une interface est `up/up` : la configuration est-elle forcément juste ?

<details markdown="1"><summary>Voir la réponse</summary>

Non. `up/up` dit que le **lien** fonctionne, pas que l'adresse, le VLAN ou l'`encapsulation` sont corrects.

</details>

**5.** Une panne ne se voit pas parce qu'une route de secours a pris le relais. Comment la détecter ?

<details markdown="1"><summary>Voir la réponse</summary>

En vérifiant la **table de routage** (`show ip route`) et pas seulement le ping : la route principale doit être présente.

</details>

➡️ Suite : [le TP « Réseau en panne »](02-tp.md).
