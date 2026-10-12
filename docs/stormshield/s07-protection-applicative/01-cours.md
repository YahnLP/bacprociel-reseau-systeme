# 📖 Cours – Protection applicative

*Parcours Stormshield – module S07*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours Stormshield (préparation CSNA).

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer pourquoi le filtrage par **ports** ne suffit plus ;
- [ ] décrire le **filtrage d'URL**, l'**antivirus**, l'**analyse en bac à sable** et l'**IPS** ;
- [ ] expliquer le problème du trafic **chiffré** (HTTPS).

---

## 1. Les limites du filtrage par ports

Une règle « autoriser TCP 80 et 443 » laisse passer **tout** ce qui utilise ces ports : un site légitime comme un logiciel malveillant, ou un site interdit. La **protection applicative** regarde **le contenu** des flux, au-delà de l'adresse et du port.

## 2. Les quatre fonctions à connaître

| Fonction | Rôle | Exemple |
|---|---|---|
| **Filtrage d'URL** (*URL filtering*) | autorise ou bloque des sites par **catégorie** | bloquer « jeux », « réseaux sociaux » |
| **Antivirus** (*antivirus*) | analyse les fichiers transférés | bloquer un `.exe` infecté |
| **Bac à sable** (*sandbox*, Breach Fighter) | exécute un fichier suspect dans un environnement isolé pour observer son comportement | détecter un malware inconnu |
| **IPS** (*Intrusion Prevention System*) | repère les attaques connues dans le trafic (signatures, comportements) et les **bloque** | tentative d'exploitation d'une faille |

> [!NOTE]
> **IDS** détecte et **alerte** seulement ; **IPS** détecte et **bloque**. Un SNS applique un **profil d'inspection de sécurité** : on choisit, par règle, quel profil s'applique.

## 3. Le trafic chiffré

Avec HTTPS, le pare-feu ne voit que l'adresse du site, pas le contenu. Pour analyser un flux chiffré, il doit **l'ouvrir** (*SSL inspection*) : le pare-feu **déchiffre**, analyse, puis **rechiffre**. Pour que les navigateurs l'acceptent, ils doivent **faire confiance** au certificat d'une autorité propre au pare-feu.

> [!WARNING]
> Déchiffrer le trafic pose des questions de **vie privée et de légalité** : on n'ouvre pas les flux bancaires ou de santé, et les utilisateurs sont **informés** (charte informatique).

## 4. Où ça s'active ?

Dans une **règle de filtrage**, on choisit le niveau d'**inspection** (pare-feu seul, IDS, IPS) et, pour le web, la **politique d'URL** associée. Rubrique **Protection applicative** pour les profils, les catégories et l'antivirus.

## 5. Dans les simulateurs

> [!NOTE]
> 🧊 **Limite du simulateur.** Il ne fait ni filtrage d'URL, ni antivirus, ni IPS, ni déchiffrement. **Alternatives :** (1) **VM Stormshield EVA** (TP du module) ; (2) **Packet Tracer** : pas d'équivalent applicatif ; on illustre seulement la **limite des ports** avec une ACL qui bloque ou autorise le port 80 (module [CCNA 5-03](../../ccna/5-03-acl/01-cours.md)), et on lit les catégories d'URL à la main.

---

## 🧠 Quiz de fin

**1.** Pourquoi une règle « TCP 443 autorisé » ne suffit-elle pas ?

<details markdown="1"><summary>Voir la réponse</summary>

Elle laisse passer **tout** le contenu qui utilise ce port, y compris des sites interdits ou des malwares.

</details>

**2.** Différence entre IDS et IPS ?

<details markdown="1"><summary>Voir la réponse</summary>

IDS **alerte** ; IPS **bloque**.

</details>

**3.** Que fait un bac à sable ?

<details markdown="1"><summary>Voir la réponse</summary>

Il **exécute le fichier** dans un environnement isolé pour observer son comportement.

</details>

**4.** Pourquoi déchiffrer HTTPS demande-t-il une autorité de confiance sur les postes ?

<details markdown="1"><summary>Voir la réponse</summary>

Le pare-feu **présente son propre certificat** : sans confiance dans son autorité, le navigateur affiche une alerte.

</details>

➡️ Suite : [le TP du module](02-tp.md).
