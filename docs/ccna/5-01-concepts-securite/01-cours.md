# 📖 Cours – Concepts de sécurité

*Parcours CCNA – Domaine 5 – module 5-01 (sujets 5.1, 5.2 et 5.4)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31** au niveau de détail demandé. Les bonnes pratiques de sécurité sont au programme (niveau 2) : ici, on ajoute le **vocabulaire de l'examen**.

## 🎯 À la fin de ce cours, tu sauras

- [ ] distinguer **menace**, **vulnérabilité**, **exploit**, **risque** et **atténuation** ;
- [ ] citer les éléments d'un **programme de sécurité** ;
- [ ] expliquer une **bonne politique de mots de passe**, la **MFA** et les **certificats**.

---

## 1. Le vocabulaire

| Terme | Anglais | Définition | Exemple |
|---|---|---|---|
| **Actif** | *asset* | Ce qu'il faut protéger | Données clients, serveur |
| **Vulnérabilité** | *vulnerability* | Une **faiblesse** | Logiciel non mis à jour |
| **Menace** | *threat* | Un **danger potentiel** | Un attaquant, un logiciel malveillant |
| **Exploit** | *exploit* | Le **moyen** d'utiliser une vulnérabilité | Un code qui profite de la faille |
| **Risque** | *risk* | Probabilité qu'une menace exploite une vulnérabilité × impact | Vol de données |
| **Atténuation** | *mitigation* | Ce qui **réduit** le risque | Mise à jour, pare-feu |

### 🤔 Avant de lire : à ton avis ?

Un serveur n'a pas reçu un correctif depuis un an. Où est la vulnérabilité ? La menace ? L'exploit ?

<details markdown="1"><summary>Voir la réponse</summary>

**Vulnérabilité** : le correctif manquant. **Menace** : un attaquant qui cherche des serveurs non corrigés. **Exploit** : l'outil qui utilise la faille.

</details>

### Les trois objectifs : la triade CIA

| Lettre | Objectif | Exemple de protection |
|---|---|---|
| **C**onfidentialité | Seuls les **autorisés** lisent | Chiffrement, droits d'accès |
| **I**ntégrité | L'information n'est **pas modifiée** | Sommes de contrôle, signatures |
| **A**vailability (disponibilité) | Le service est **disponible** | Redondance, sauvegardes |

## 2. Les attaques courantes

| Attaque | Principe | Défense |
|---|---|---|
| **Hameçonnage** (*phishing*) | Faux message pour voler un mot de passe | Sensibilisation, MFA |
| **Logiciel malveillant** (*malware*) | Virus, rançongiciel, cheval de Troie | Antivirus, mises à jour |
| **Déni de service** (*DoS / DDoS*) | Saturer un service | Pare-feu, filtrage |
| **Attaque de l'homme du milieu** (*MITM*) | S'insérer entre deux machines | Chiffrement (HTTPS, SSH) |
| **Force brute / dictionnaire** | Essayer des mots de passe | Mots de passe longs, blocage |
| **Ingénierie sociale** | Manipuler une personne | Formation |
| **Usurpation ARP / DHCP** | Fausse réponse sur le réseau local | Sécurité de couche 2 (module 5-04) |

## 3. Un programme de sécurité

| Élément | Rôle |
|---|---|
| **Sensibilisation** (*awareness*) | Informer **tout le monde** des risques |
| **Formation** (*training*) | Former les personnes à des **tâches précises** |
| **Contrôle d'accès physique** | Badges, serrures, caméras, salles fermées |
| **Politique de sécurité** | Règles écrites et appliquées |

## 4. Mots de passe, MFA, certificats, biométrie

| Notion | Principe |
|---|---|
| **Bon mot de passe** | **Long** (12 caractères ou plus), **unique** par service, mieux : une **phrase de passe** |
| **Gestionnaire de mots de passe** | Mémorise des mots de passe uniques et complexes |
| **MFA** (*multi-factor authentication*) | **Deux facteurs** ou plus : ce que je **sais** (mot de passe), ce que je **possède** (téléphone, clé), ce que je **suis** (empreinte) |
| **Certificat numérique** | Prouve l'**identité** d'un serveur ou d'un utilisateur, signé par une **autorité** |
| **Biométrie** | Empreinte, visage : pratique, mais **non révocable** |

> [!NOTE]
> Les recommandations actuelles privilégient la **longueur** plutôt que les caractères spéciaux imposés, et déconseillent de changer un mot de passe **sans raison**.

---

## 🧠 Quiz de fin

**1.** Quelle différence entre vulnérabilité et menace ?

<details markdown="1"><summary>Voir la réponse</summary>

La **vulnérabilité** est une faiblesse **du système** ; la **menace** est un danger **extérieur** qui peut l'exploiter.

</details>

**2.** Que veut dire CIA ?

<details markdown="1"><summary>Voir la réponse</summary>

**Confidentialité, Intégrité, Disponibilité** (*Availability*).

</details>

**3.** Un mot de passe + un code reçu par SMS : quel mécanisme ?

<details markdown="1"><summary>Voir la réponse</summary>

La **MFA** (deux facteurs).

</details>

**4.** Donne deux mesures d'atténuation contre le hameçonnage.

<details markdown="1"><summary>Voir la réponse</summary>

La **sensibilisation** des utilisateurs et la **MFA**.

</details>
