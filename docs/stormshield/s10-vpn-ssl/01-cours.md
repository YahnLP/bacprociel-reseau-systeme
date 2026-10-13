# 📖 Cours – VPN SSL

*Parcours Stormshield – module S10*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours Stormshield (préparation CSNA).

## 🎯 À la fin de ce cours, tu sauras

- [ ] distinguer **VPN site à site** et **VPN nomade** ;
- [ ] expliquer comment fonctionne un **VPN SSL** ;
- [ ] décrire les étapes de mise en service pour un **télétravailleur**.

---

## 1. Deux familles de VPN

| | **Site à site** | **Nomade** (*remote access*) |
|---|---|---|
| Relie | deux **réseaux** | **un poste** à un réseau |
| Exemple | siège ↔ agence | télétravailleur ↔ entreprise |
| Technologie courante | IPsec | **VPN SSL**, IPsec |

## 2. Le VPN SSL

Le VPN SSL crée un **tunnel chiffré** entre le poste de l'utilisateur et le pare-feu, en s'appuyant sur **TLS** (la même famille de protocoles que HTTPS). Sur un SNS, il repose sur la technologie **OpenVPN** avec un **client** à installer sur le poste.

| Avantage | Pourquoi |
|---|---|
| **Traverse facilement les réseaux** | il peut utiliser le port **443**, rarement bloqué |
| **Simple pour l'utilisateur** | un client, un fichier de configuration |
| **Authentification de l'utilisateur** | compte d'annuaire (module S08), parfois certificat |

## 3. Mise en service

| Étape | Rôle |
|---|---|
| 1. **Autorité de certification** | le pare-feu a un certificat de serveur |
| 2. **Utilisateurs autorisés** | via l'annuaire (groupe « télétravail ») |
| 3. **Paramètres du VPN SSL** | adresse publique, port, **réseau attribué aux clients**, **réseaux accessibles** |
| 4. **Règle de filtrage** | autoriser les clients VPN vers les ressources voulues |
| 5. **Client** | installer le client, importer la configuration, se connecter |

> [!WARNING]
> **Moindre privilège aussi pour les nomades :** un télétravailleur n'a pas besoin d'accéder à tout le réseau interne, seulement aux **ressources de son métier**.

## 4. Dans les simulateurs

> [!NOTE]
> 🧊 **Limite du simulateur.** Il n'a pas de VPN (IPsec ni SSL) sur le pare-feu. **Alternatives :** (1) **VM EVA** + poste client (TP du module) ; (2) **VirtualBox, sans Stormshield** : un serveur **OpenVPN** sur une VM Linux (TP du module) pour comprendre le principe ; (3) **Packet Tracer** : seulement le VPN IPsec (module [CCNA 5-05](../../ccna/5-05-vpn-ipsec/01-cours.md)).

## 🔧 Dépanner : le VPN SSL (nomade)

> [!NOTE]
> **Pourquoi ce chapitre ?** Le VPN nomade touche des postes que tu ne maîtrises pas (domicile, hôtel). Les pannes viennent souvent du **poste** ou du **réseau de l'utilisateur**, autant que du pare-feu.

> [!WARNING]
> **Ce tableau n'est pas reproductible dans le simulateur** du site (pas de VPN SSL). Il décrit les causes **classiques** à connaître pour la certification ; **vérifie-les sur ta VM EVA** (ou en classe) avant de les considérer comme acquises.

| Symptôme | Cause fréquente | Vérification |
|---|---|---|
| Le client ne se connecte pas | adresse / port du pare-feu faux, port bloqué par le réseau de l'utilisateur | tester l'accès au port depuis le poste |
| Avertissement de certificat | certificat auto-signé non reconnu par le poste | installer l'autorité de certification sur le poste |
| Connexion refusée après identification | utilisateur **non autorisé** à utiliser le VPN SSL | droits de l'utilisateur / groupe |
| Connecté mais aucune ressource accessible | réseaux à joindre non annoncés ; règle de filtrage pour le trafic VPN absente | politique de filtrage, réseaux annoncés au client |
| Conflit d'adresses | le réseau du domicile utilise le même plan d'adresses que l'entreprise | choisir un plan d'adressage peu courant pour le LAN et le pool VPN |

---

## 🧠 Quiz de fin

**1.** Quand préfère-t-on un VPN nomade à un site à site ?

<details markdown="1"><summary>Voir la réponse</summary>

Quand **un poste isolé** (télétravailleur) doit joindre le réseau de l'entreprise.

</details>

**2.** Pourquoi le VPN SSL traverse-t-il facilement les réseaux ?

<details markdown="1"><summary>Voir la réponse</summary>

Il peut utiliser le **port 443**, presque toujours ouvert.

</details>

**3.** Que faut-il prévoir pour limiter les droits d'un télétravailleur ?

<details markdown="1"><summary>Voir la réponse</summary>

Une **règle de filtrage** n'autorisant que les ressources nécessaires.

</details>

➡️ Suite : [le TP du module](02-tp.md).
