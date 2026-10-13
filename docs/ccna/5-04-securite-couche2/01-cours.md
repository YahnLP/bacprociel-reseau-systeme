# 📖 Cours – Sécurité de couche 2

*Parcours CCNA – Domaine 5 – module 5-04 (sujet 5.7)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] configurer la **sécurité des ports** (*port security*) ;
- [ ] expliquer **DHCP snooping** et **Dynamic ARP Inspection (DAI)** ;
- [ ] citer les **bonnes pratiques** d'un switch d'accès.

---

## 1. Pourquoi sécuriser la couche 2 ?

Dans un LAN, **n'importe qui peut brancher un câble**. Sans protection, un poste malveillant peut : **inonder** la table MAC, installer un **faux serveur DHCP**, **usurper** une adresse ARP, brancher un **switch pirate**.

## 2. Port security

Elle limite **qui** peut utiliser un port d'accès.

```text
interface fa0/1
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
```

| Paramètre | Rôle |
|---|---|
| `maximum <n>` | Nombre d'adresses MAC autorisées (**1** par défaut) |
| `mac-address sticky` | Le switch **apprend** les adresses et les **écrit dans la configuration** |
| `violation shutdown` | Si une MAC inconnue apparaît, le port passe en **err-disabled** (coupé) — **défaut** |
| `violation restrict` | Jette les trames de l'intrus, **journalise** et compte |
| `violation protect` | Jette les trames de l'intrus, **sans journal** |

| Commande | Rôle |
|---|---|
| `show port-security` | résumé par port |
| `show port-security interface fa0/1` | détail (violation, dernière MAC) |
| `show interfaces status err-disabled` | ports coupés |

Pour **réactiver** un port err-disabled : `shutdown` puis `no shutdown` sur l'interface.

> [!NOTE]
> Les valeurs **par défaut** (`maximum 1`, `violation shutdown`) **n'apparaissent pas** dans `show running-config`. Pour les voir, utilise `show port-security interface`.

## 3. DHCP snooping et DAI

| Protection | Problème traité | Principe |
|---|---|---|
| **DHCP snooping** | Un **faux serveur DHCP** distribue de mauvaises adresses | Seuls les ports **de confiance** (*trusted*, vers le vrai serveur) peuvent envoyer des **Offer**. Le switch construit une **table de correspondance** IP/MAC/port |
| **DAI** (*Dynamic ARP Inspection*) | **Usurpation ARP** | Le switch **vérifie** chaque réponse ARP avec la table du DHCP snooping |

```text
ip dhcp snooping
ip dhcp snooping vlan 10
interface gi0/1
 ip dhcp snooping trust
ip arp inspection vlan 10
interface gi0/1
 ip arp inspection trust
```

> [!WARNING]
> Ces deux protections **ne s'affichent pas** (`show ip dhcp snooping`) dans le simulateur du site : retiens leur **principe** et la **syntaxe** pour l'examen (voir l'alternative Packet Tracer, plus bas).

## 4. Les autres bonnes pratiques

- **Couper les ports inutilisés** (`shutdown`) et les placer dans un VLAN **sans usage**.
- Utiliser un **VLAN natif** inutilisé et limiter les **VLAN autorisés** sur les trunks.
- Désactiver la **négociation de trunk** sur les ports d'accès (`switchport mode access`).
- Activer **BPDU guard** sur les ports d'accès (module 2-04).

---

## 🔧 Dépanner : « le port est en err-disabled »

> [!NOTE]
> **Pourquoi ce chapitre ?** La sécurité de port **coupe volontairement** un port quand elle détecte une violation. Ce n'est donc pas une panne matérielle : le port s'est **protégé**. Le bon réflexe n'est pas de le rallumer, mais de **comprendre ce qui l'a déclenché**.

### Reconnaître et comprendre

```text
SW1# show interfaces status
Fa0/1        err-disabled  1   a-full  a-100 10/100BaseTX
Fa0/2        err-disabled  1   a-full  a-100 10/100BaseTX

SW1# show port-security
Secure Port  MaxSecureAddr  CurrentAddr  SecurityViolation  Security Action
Fa0/1                    1            1                  1         Shutdown
```

`SecurityViolation = 1` : une violation a eu lieu ; l'action prévue est `Shutdown`.

### Remettre en service… sans masquer le problème

La procédure classique : `shutdown` puis `no shutdown` sur le port. Mais **si l'équipement non autorisé est toujours branché**, la violation se reproduit aussitôt. Dans le simulateur, après cette manipulation, le compteur passe de **1 à 2** et le port retombe en `err-disabled`.

**Méthode :**

1. Lire `show port-security interface fa0/1` : quelle adresse est autorisée, laquelle a violé ?
2. **Débrancher** (ou identifier) l'équipement fautif.
3. Seulement ensuite : `shutdown` puis `no shutdown`.
4. Vérifier `show interfaces status` : retour à `connected`.

### Cas fréquent en entreprise

Un technicien remplace un PC : la **nouvelle adresse MAC** diffère de celle apprise (*sticky*). Le port se coupe. Ce n'est pas une attaque, mais le processus est le même : on **change l'adresse autorisée** (`no switchport port-security mac-address sticky …` et réapprentissage) plutôt que de désactiver la sécurité.

---

## 🧠 Quiz de fin

**1.** Quel est le mode de violation par défaut ?

<details markdown="1"><summary>Voir la réponse</summary>

**shutdown** : le port passe en err-disabled.

</details>

**2.** Que fait `mac-address sticky` ?

<details markdown="1"><summary>Voir la réponse</summary>

Le switch **apprend** les adresses MAC des postes et les **inscrit** dans la configuration.

</details>

**3.** Quel est le rôle d'un port « trusted » en DHCP snooping ?

<details markdown="1"><summary>Voir la réponse</summary>

Il laisse passer les **réponses DHCP** (celles du vrai serveur) : les autres ports ne le peuvent pas.

</details>

**4.** Quelle attaque la DAI empêche-t-elle ?

<details markdown="1"><summary>Voir la réponse</summary>

L'**usurpation ARP** (*ARP spoofing*).

</details>

➡️ Suite : [le TP du module](02-tp.md).
