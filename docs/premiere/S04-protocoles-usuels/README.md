# S04 – Protocoles usuels vus de l'intérieur

| Élément | Détail |
|---|---|
| **Niveau** | Première Bac Pro CIEL |
| **Semaine** | S04 – lundi 12 octobre 2026 (CFA) |
| **Durée** | 4 heures |
| **Autonomie visée** | 🟡 Semi-guidé |
| **Prérequis** | S03 (couches, trame, MAC / IP, analyseur) |
| **Référentiel** | C06 · C09 · protocoles usuels IPv4 (niv. 3) |

> [!NOTE]
> **Question qui guide la séance :** *« Quand j'ouvre un site web, que se disent mon PC, la box et le serveur ? Et quels messages précis échangent-ils ? »*

## 🎯 Objectifs

1. **Décrire** l'échange **DHCP** (DORA) et **le retrouver** dans une capture.
2. **Décrire** une résolution **DNS** (requête / réponse) et lire ses champs.
3. **Expliquer** la différence **TCP / UDP** et la **poignée de main TCP**.
4. **Lire** une requête **HTTP** (`GET`, `200 OK`).
5. **Associer** un service à son **port** et à son **protocole de transport**.

## 📚 Contenu de la séance

| Document | Rôle |
|---|---|
| [📖 Cours élève](01-cours.md) | DHCP, DNS, TCP/UDP, HTTP, ports |
| [🛠️ TP](02-tp.md) | Capturer et lire DHCP, DNS, TCP, HTTP |
| [📝 Fiche des protocoles](03-fiche-protocoles.md) | Tableau de synthèse + enquête |
| [`tp/p04-protocoles.json`](tp/p04-protocoles.json) | Simulateur : 2 PC, une box, Internet (DNS et site web) |

## ⏱️ Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « Combien de messages pour ouvrir une page ? » (les élèves devinent) ; retour mission entreprise | Classe |
| 0 h 20 – 0 h 55 | **Mini-cours 1** : DHCP et DNS (cours §1–§2) | Classe |
| 0 h 55 – 1 h 45 | **TP A–B** : capturer DHCP, puis DNS | Binôme |
| 1 h 45 – 2 h 00 | Pause | |
| 2 h 00 – 2 h 30 | **Mini-cours 2** : TCP, UDP, HTTP, ports (§3–§4) | Classe |
| 2 h 30 – 3 h 20 | **TP C–D** : poignée de main TCP, requête HTTP | Binôme |
| 3 h 20 – 4 h 00 | **TP E** : l'enquête (fiche des protocoles), bilan | Individuel |

## 🧪 Matériel et préparation

- Simulateur avec `tp/p04-protocoles.json`.
- Le site `www.exemple.fr` est fourni par le fichier (serveur web et DNS simulés).

## 🧭 Évaluation

| Quoi | Comment |
|---|---|
| **TP : tableaux de lecture** | Comparaison avec le corrigé (formatif) |
| **Fiche de synthèse + enquête** | Notée sur 10 (facultatif) |

## 🏭 Mission en entreprise

> *Demander **quels services réseau** tournent dans l'entreprise (DHCP, DNS, web, messagerie…) et sur **quelle machine**.*

## 🧑‍🏫 Notes pour l'enseignant

<details markdown="1"><summary>Points d'attention</summary>

- **Commandes disponibles dans le terminal du simulateur** : `ipconfig /release`, `ipconfig /renew`, `nslookup`, `curl`, `netstat`, `telnet`, `ssh`. `curl` affiche la page HTML (pas les en-têtes) ; les en-têtes se lisent dans l'analyseur.
- **Filtres utiles** : `dhcp`, `dns`, `tcp`, `http`, `tcp.flags.syn == 1`.
- **Avant le TP** : demander aux élèves d'**effacer** l'analyseur après l'ouverture du fichier pour n'avoir que les trames utiles.
- **Le HTTPS n'est pas simulé en détail** ; on le présente dans le cours comme la version chiffrée du HTTP (port 443).
- Corrigé : `corriges/premiere/P04-corrige.md`.

</details>
