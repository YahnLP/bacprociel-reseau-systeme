# 📖 Cours – Utilisateurs et authentification

*Parcours Stormshield – module S08*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours Stormshield (préparation CSNA). Lien avec l'**annuaire** vu dans le [parcours serveurs, module 4](../../serveurs/m4-active-directory/01-cours.md) et avec **AAA/RADIUS** ([CCNA 5-02](../../ccna/5-02-acces-equipements-aaa/01-cours.md)).

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer pourquoi filtrer **par utilisateur** plutôt que par adresse IP ;
- [ ] citer les **annuaires** et **méthodes d'authentification** d'un SNS ;
- [ ] décrire le **portail captif** et le **SSO**.

---

## 1. Pourquoi authentifier ?

Une règle basée sur une **adresse IP** suit **le poste**, pas la **personne** : si le stagiaire s'assoit au poste de l'administrateur, il hérite de ses droits. En authentifiant l'**utilisateur**, la règle suit **la personne**, quel que soit son poste.

## 2. L'annuaire

| Annuaire | Contenu |
|---|---|
| **LDAP interne** | base d'utilisateurs créée **sur le pare-feu** |
| **LDAP externe / Active Directory** | le pare-feu interroge l'annuaire de l'entreprise |

> [!NOTE]
> Avec **Active Directory**, on réutilise les **mêmes comptes** que ceux du domaine : une seule base à gérer.

## 3. Les méthodes d'authentification

| Méthode | Principe |
|---|---|
| **LDAP** | identifiant + mot de passe vérifiés dans l'annuaire |
| **Kerberos** | ticket du domaine Windows |
| **RADIUS** | serveur d'authentification externe (UDP **1812**) |
| **Certificat SSL** | le poste présente un certificat |
| **SPNEGO / SSO** | l'utilisateur déjà connecté à Windows est reconnu **sans retaper** son mot de passe |

## 4. Le portail captif

Avec l'authentification **explicite**, l'utilisateur est redirigé vers une **page de connexion** (le portail captif) avant d'accéder à Internet. Une fois authentifié, ses règles s'appliquent. Utile pour les invités et les postes non Windows.

## 5. Enrôlement et règles

| Étape | Rôle |
|---|---|
| **Enrôlement** | créer ou importer les comptes (et les groupes) |
| **Politique d'authentification** | dire **quel flux** doit s'authentifier et **par quelle méthode** |
| **Règle de filtrage** | utiliser l'utilisateur ou le groupe comme **source** |

## 6. Dans les simulateurs

> [!NOTE]
> 🧊 **Limite du simulateur.** Le pare-feu du simulateur ne gère ni utilisateurs, ni annuaire, ni portail captif. **Alternatives :** (1) **VM EVA** + **VM Active Directory** (TP du module) ; (2) **Packet Tracer** : un serveur AAA (RADIUS) joint par un routeur ou un switch, comme au module [CCNA 5-02](../../ccna/5-02-acces-equipements-aaa/02-tp.md).

---

## 🧠 Quiz de fin

**1.** Pourquoi une règle par utilisateur est-elle plus sûre qu'une règle par adresse IP ?

<details markdown="1"><summary>Voir la réponse</summary>

Elle suit la **personne** et non le poste ; on peut aussi **tracer** qui a fait quoi.

</details>

**2.** Citez trois méthodes d'authentification d'un SNS.

<details markdown="1"><summary>Voir la réponse</summary>

Par exemple : LDAP, Kerberos, RADIUS, certificat SSL, SPNEGO.

</details>

**3.** À quoi sert le portail captif ?

<details markdown="1"><summary>Voir la réponse</summary>

À faire **s'authentifier** l'utilisateur sur une page web avant d'accéder au réseau.

</details>

**4.** Quel est l'avantage du SSO ?

<details markdown="1"><summary>Voir la réponse</summary>

L'utilisateur est reconnu **sans ressaisir** son mot de passe.

</details>

➡️ Suite : [le TP du module](02-tp.md).
