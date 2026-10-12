# 📖 Cours – Configuration réseau

*Parcours Stormshield – module S04*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours Stormshield (préparation CSNA).

## 🎯 À la fin de ce cours, tu sauras

- [ ] choisir un **mode de déploiement** ;
- [ ] configurer les **interfaces** (adresse, zone) et la **route par défaut** ;
- [ ] expliquer le rôle des **zones** LAN, WAN, DMZ.

---

## 1. Modes de déploiement

| Mode | Principe | Quand |
|---|---|---|
| **Routeur** (*routed / advanced*) | Chaque interface a son **réseau** ; le pare-feu **route** entre eux | cas le plus courant |
| **Transparent** (*bridge*) | Le pare-feu est **« invisible »** : interfaces regroupées dans un pont, sans changer l'adressage | insérer un pare-feu sans toucher au réseau existant |
| **Hybride** | Un mélange : certaines interfaces routées, d'autres en pont | cas particuliers |

Dans ce parcours, on travaille en **mode routeur**.

## 2. Interfaces et zones

Chaque interface est reliée à un réseau et **appartient à une zone** de confiance :

| Interface | Zone | Réseau (exemple) |
|---|---|---|
| `out` | **externe** (WAN, Internet) | 203.0.113.0/29 |
| `in` | **interne** (LAN) | 192.168.1.0/24 |
| `dmz1` | **DMZ** | 172.16.0.0/24 |

Types d'interfaces à connaître : **Ethernet** (physique), **VLAN** (une interface par VLAN sur un trunk), **pont** (*bridge*), **modem**, **GRETAP**.

> [!TIP]
> Les adresses de passerelle des postes pointent vers **l'adresse du pare-feu dans leur réseau** (ex. 192.168.1.254 pour le LAN).

## 3. Routage

Pour sortir sur Internet, le pare-feu a besoin d'une **route par défaut** (*default gateway*) vers le routeur du fournisseur d'accès. Il utilise aussi les routes **connectées** (ses propres réseaux) et des routes **statiques** vers d'autres réseaux internes.

| Étape de vérification | Outil |
|---|---|
| Le pare-feu joint sa passerelle | test de ping depuis le pare-feu |
| Un poste joint sa passerelle | `ping 192.168.1.254` |
| Un poste joint Internet | `ping` / navigateur (après NAT, S05) |

## 4. Dans le simulateur

Onglet **Interfaces** : zone, adresse IPv4, masque, DHCP, actif/inactif, et **passerelle par défaut**. Clique sur **Appliquer**.

> [!NOTE]
> 🧊 **Limite du simulateur.** Pas de mode transparent (pont), pas d'interfaces VLAN ni GRETAP, pas de routage avancé (routes par politique, dynamique). **Alternative Packet Tracer :** un routeur Cisco avec sous-interfaces 802.1Q (module [CCNA 2-02](../../ccna/2-02-trunk-inter-vlan/01-cours.md)) et des routes statiques (module [CCNA 3-02](../../ccna/3-02-routage-statique/01-cours.md)). **Alternative VM :** EVA, rubrique *Réseau → Interfaces*.

---

## 🧠 Quiz de fin

**1.** Dans quel mode un pare-feu s'insère-t-il sans changer l'adressage du réseau ?

<details markdown="1"><summary>Voir la réponse</summary>

En mode **transparent** (pont).

</details>

**2.** Quelle zone pour l'interface qui va vers Internet ?

<details markdown="1"><summary>Voir la réponse</summary>

La zone **externe** (WAN).

</details>

**3.** Que faut-il configurer sur le pare-feu pour qu'il joigne Internet ?

<details markdown="1"><summary>Voir la réponse</summary>

Une **route par défaut** vers le routeur du fournisseur d'accès.

</details>

➡️ Suite : [le TP du module](02-tp.md).
