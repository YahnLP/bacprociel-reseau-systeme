# 📖 Cours – Révision et remédiation

*Bac Pro CIEL – Terminale – E31 – S14*

> [!IMPORTANT]
> **Une idée à la fois.** Réponds à la question **avant** de déplier la réponse.

## 🎯 À la fin de ce cours, tu sauras

- [ ] situer ses **acquis** et ses **lacunes** ;
- [ ] choisir un atelier **adapté** ;
- [ ] résumer l'essentiel sur une **fiche personnelle**.

---

## 1. Câblage et matériel

### 🤔 Avant de lire : à ton avis ?

Un câble relie deux ordinateurs sans switch. **Droit ou croisé ?** Et un PC vers un switch ?

<details markdown="1"><summary>Voir la réponse</summary>

PC ↔ PC : **croisé** (sauf équipement auto-MDIX, courant aujourd'hui). PC ↔ switch : **droit**. On étiquette toujours les **deux bouts**.

</details>

### 💡 L'idée

| Point à maîtriser | Rappel |
|---|---|
| Brochage RJ45 | **T568B** aux deux bouts = droit |
| Test | **cartographie**, **longueur**, continuité |
| Fibre | **atténuation** (dB), jamais regarder le laser |
| Baie | lourd en bas, **étiquettes**, brassage propre |

🔗 Retravailler : [Seconde S09–S10](../../seconde/S10-raccorder-brasser/README.md), [Première S13](../../premiere/S13-cuivre-fibre-securite/README.md), [Terminale S04](../S04-installer-mesurer/README.md).

### ✅ Vérifie que tu as compris

La cartographie du câble montre une paire **inversée**. **Que fais-tu ?**

<details markdown="1"><summary>Voir la réponse</summary>

Je **refais le sertissage** (ou le raccordement) en suivant le **code couleur** T568B aux deux bouts, puis je **retesté**.

</details>

---

## 2. Adressage et services de base

### 🤔 Avant de lire : à ton avis ?

Un poste a l'adresse `192.168.1.50/24`. **Quel est son réseau ? Sa passerelle possible ? Peut-il joindre `192.168.2.10` sans routeur ?**

<details markdown="1"><summary>Voir la réponse</summary>

Réseau `192.168.1.0/24` ; passerelle `192.168.1.1` en général ; **non** pour `192.168.2.10` (autre réseau) sans **routeur**.

</details>

### 💡 L'idée

| Point | Rappel |
|---|---|
| Masque | `/24` = `255.255.255.0` |
| Adresse **169.254** | **pas de DHCP** reçu |
| Passerelle | doit être **dans le même réseau** que le poste |
| DNS | traduit un **nom** en adresse |

🔗 Retravailler : [Seconde S11–S13](../../seconde/S11-adresse-ip/README.md), [Première S06](../../premiere/S06-sous-reseaux/README.md), [Première S11](../../premiere/S11-dhcp-dns-serveur/README.md).

### ✅ Vérifie que tu as compris

Ping d'une **adresse IP** : OK. Ouverture d'un site par son **nom** : KO. **Que vérifies-tu ?**

<details markdown="1"><summary>Voir la réponse</summary>

Le **DNS** : serveur DNS du poste, serveur DNS joignable, enregistrement correct.

</details>

---

## 3. Configuration : VLAN, routage, services

### 🤔 Avant de lire : à ton avis ?

Deux postes du **même switch** ne se voient pas. **Donne deux causes possibles** liées aux VLAN.

<details markdown="1"><summary>Voir la réponse</summary>

Les ports sont dans des **VLAN différents**, ou le **VLAN n'existe pas** sur un switch intermédiaire / n'est pas autorisé sur le **trunk**.

</details>

### 💡 L'idée

| Point | Rappel |
|---|---|
| VLAN | `vlan 10` / `switchport access vlan 10` |
| Trunk | `switchport mode trunk` ; VLAN **autorisés** |
| Inter-VLAN | sous-interfaces `dot1Q` ou interfaces VLAN (L3) |
| ACL | **sens** et **interface** ; sans état |
| Sauvegarde | `write memory` |

🔗 Retravailler : [Première S08–S09](../../premiere/S08-vlan-1/README.md), [Terminale S05](../S05-inter-vlan/README.md).

### ✅ Vérifie que tu as compris

Tu as configuré un switch, tout marche, mais tu n'as pas tapé `write memory`. **Risque ?**

<details markdown="1"><summary>Voir la réponse</summary>

Au redémarrage, la configuration est **perdue** (seule la `startup-config` survit).

</details>

---

## 4. Dépanner avec méthode

### 🤔 Avant de lire : à ton avis ?

Un poste n'a plus Internet. **Quel est ton premier test ?**

<details markdown="1"><summary>Voir la réponse</summary>

Le **plus proche** : lien physique et **adresse** du poste (`ipconfig`). On monte ensuite l'**échelle des tests**.

</details>

### 💡 L'idée

**Démarche :** symptôme → hypothèses → tests → cause → action → vérification. **Une correction à la fois.** **Deux pannes** possibles.

🔗 Retravailler : [Seconde S15](../../seconde/S15-depannage-n1/README.md), [Terminale S11](../S11-depanner-1/README.md), [Terminale S12](../S12-depanner-2/README.md).

### ✅ Vérifie que tu as compris

Tu as réparé un défaut et le test passe au vert. Les trois autres restent rouges. **Quelle est ta conclusion ?**

<details markdown="1"><summary>Voir la réponse</summary>

Il y a **une autre panne** : on n'a fini que quand **tout** est vert.

</details>

---

## 🧠 À retenir

- **Je connais mes lacunes** : je les retravaille d'abord.
- **Ma fiche « 15 points »** : mes pièges, mes commandes.
- **Je me chronomètre** pour mesurer mes progrès.
- **La méthode de dépannage** s'applique à tout.
