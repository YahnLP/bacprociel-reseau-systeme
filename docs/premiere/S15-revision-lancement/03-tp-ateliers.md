# 🛠️ TP – Ateliers de remédiation

*Bac Pro CIEL – Première – E31 – S15 – binôme*

> [!NOTE]
> **Mission.** Tu as fait le QCM. Choisis **2 ateliers** (sur 4) correspondant à tes **domaines les plus faibles**. Chaque atelier réutilise un fichier du simulateur déjà vu : cette fois, **tu le fais sans le TP guidé**, en t'aidant seulement de l'**aide-mémoire** de la séance.
>
> **Temps prévu :** 2 × 1 h. **Binôme :** ____________ / ____________

## Comment choisir ?

| Domaine faible au QCM | Atelier conseillé |
|---|---|
| **A** – Adressage | Atelier 1 |
| **V** – VLAN (et **R** – Routage) | Atelier 2 |
| **S** – Services | Atelier 3 |
| **C** – Sécurité et câblage | Atelier 4 |

Règle : **un atelier du domaine le plus faible**, un du **deuxième**.

---

## Atelier 1 – Découper un réseau (adressage)

**Fichier :** `S06-sous-reseaux/tp/p06-sousreseaux.json` (au départ, non corrigé).

1. Ouvre le fichier et relis la consigne de la [S06](../S06-sous-reseaux/02-tp.md) **sans** regarder les aides.
2. Rends **tous les contrôles verts** dans le simulateur.
3. **Sans calculatrice**, remplis :

| Réseau | Masque | Adresse réseau | Diffusion | 1re / dernière machine |
|---|---|---|---|---|
| 192.168.50.0/27 | | | | |
| 192.168.50.32/27 | | | | |
| 192.168.50.64/26 | | | | |

> [!TIP]
> **Aide :** la taille d'un bloc = `256 − dernier octet du masque`. Dans un `/27`, le masque finit par 224 → blocs de **32**.

<details markdown="1"><summary>✅ Vérifie</summary>

`/27` en `.0` : réseau .0, diffusion .31, machines .1 à .30. `/27` en `.32` : réseau .32, diffusion .63, machines .33 à .62. `/26` en `.64` : réseau .64, diffusion .127, machines .65 à .126.

</details>

## Atelier 2 – VLAN et trunk

**Fichiers :** `S08-vlan-1/tp/p08-vlan-panne.json` puis `S09-vlan-2-trunk/tp/p09-trunk-panne.json`.

1. Ouvre `p08-vlan-panne.json` : des postes ne se joignent pas. **Trouve la panne** avec `show vlan brief`, corrige-la, et rends les contrôles verts.
2. Ouvre `p09-trunk-panne.json` : même démarche ; pense à `show interfaces trunk`.
3. Écris pour chacune : **symptôme → test → cause → correction**.

| Panne | Symptôme | Test utilisé | Cause | Correction |
|---|---|---|---|---|
| S08 | | | | |
| S09 | | | | |

## Atelier 3 – DHCP et DNS

**Fichier :** `S11-dhcp-dns-serveur/tp/p11-dhcp-dns.json`, puis `p11-dhcp-dns-panne.json`.

1. Sur `p11-dhcp-dns.json`, configure le serveur (DHCP + DNS) **sans relire le TP** ; contrôles verts.
2. Sur `p11-dhcp-dns-panne.json`, trouve pourquoi le nom `intranet.mecapro.local` ne fonctionne pas : `ipconfig /all` puis `nslookup`.
3. Explique à ton binôme, **en 3 phrases**, la différence entre « pas d'adresse » et « pas de nom ».

## Atelier 4 – Sécurité de base

**Fichier :** `S14-securite-base/tp/p14-securite.json`.

1. Remplis la [checklist d'audit](../S14-securite-base/03-checklist-audit.md) (colonne *Avant*).
2. Applique **seulement** les corrections de base : `enable secret`, SSH, bannière, ports libres coupés, `write memory`, ACL du routeur.
3. Rends les **7 contrôles** verts, puis calcule ton score après.

---

## ✅ Bilan de séance (5 min)

| Question | Ta réponse |
|---|---|
| Quel domaine m'a posé le plus de problèmes ? | |
| Quelle erreur ai-je faite deux fois ? | |
| Quel **réflexe** vais-je appliquer pendant le projet ? | |
