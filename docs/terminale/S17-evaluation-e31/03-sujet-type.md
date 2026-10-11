# 📄 Sujet type – Étude notariale Pasquier

*Terminale – E31 – S17 (sujet d'entraînement ; adaptable)*

## 1. Contexte

L'**étude notariale de Me Pasquier** emménage dans de nouveaux locaux. Elle souhaite un **réseau** pour les bureaux, une **imprimante partagée** et un **Wi-Fi pour les visiteurs**, qui ne doivent **pas** accéder aux postes ni à l'imprimante.

## 2. Exigences du client

| N° | Exigence |
|---|---|
| E1 | Les postes des bureaux reçoivent leur adresse **automatiquement** et accèdent à **Internet**. |
| E2 | L'imprimante est joignable avec une **adresse fixe**. |
| E3 | Les visiteurs disposent d'un **Wi-Fi sécurisé** (WPA2) avec accès à Internet. |
| E4 | Les visiteurs **ne voient pas** l'imprimante ni les postes (confidentialité des dossiers). |
| E5 | Les configurations sont **sauvegardées** et **documentées**. |

## 3. Matériel (même plan de câblage qu'en S15)

| Équipement | Connexion |
|---|---|
| `R1` | `gi0/0` → FAI `gi0/2` ; `gi0/1` → `SW1 Fa0/24` |
| `PC-SECR` | `SW1 Fa0/1` |
| `PC-DENT` (poste du notaire) | `SW1 Fa0/2` |
| `IMP` | `SW1 Fa0/3` |
| `AP1` | `SW1 Fa0/10` |
| `LAP-INV` (portable visiteur) | Wi-Fi |

**Adresse publique :** `203.0.113.3/29` ; passerelle FAI `203.0.113.2` ; DNS `198.51.100.53`.

## 4. Plan d'adressage (imposé)

| Réseau | VLAN | Réseau | Passerelle | DHCP | Fixe |
|---|---|---|---|---|---|
| Bureaux | **11** | `172.16.11.0/24` | `.1` | à partir de `.100` | imprimante `172.16.11.20` |
| Visiteurs | **21** | `172.16.21.0/24` | `.1` | à partir de `.100` | – |

**Noms :** `SW-PASQUIER`, `R-PASQUIER`. **Enable (switch) :** `Pasquier#2027`. **Wi-Fi :** `PASQUIER-VISITEURS`, clé `Visiteurs#2027`, WPA2.

## 5. À remettre

1. Plan d'adressage **complété** (adresses, plages).
2. **Cahier de recette** rempli (au moins 6 tests dont 2 négatifs).
3. **Compte rendu** de l'intervention.
4. Configurations **sauvegardées**.
