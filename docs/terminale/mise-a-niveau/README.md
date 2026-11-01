# 🚀 Parcours de mise à niveau – Terminale en 15 semaines (E31)

**Pour qui ?** Un(e) élève qui arrive en Terminale **sans avoir suivi Seconde ni Première**. **Objectif :** être prêt(e) pour l'**épreuve pratique E31** (3 h : préparer, intervenir, assurer la maintenance) en 15 semaines de 4 h, soit 60 h.

> [!NOTE]
> **Principe.** On ne rejoue pas trois ans. On garde ce qui est utile le jour de l'épreuve : câbler, tester, configurer un switch (VLAN, passerelle, DHCP), régler le Wi-Fi, sauvegarder, dépanner, rendre compte. Chaque séance est un **cours complet et autonome** (cours, TP, bilan), écrit pour ce parcours : tu n'as **pas besoin** des séances de Seconde et de Première. Chaque semaine vise **une tâche d'épreuve** précise, avec une preuve dans le passeport d'autonomie.

## 🗓️ Les 15 semaines

| Séance | Thème | Tâche d'épreuve | Compétences |
|---|---|---|---|
| **M01** | [Réseau, matériel, sécurité, diagnostic de départ](M01.md) | Reconnaître les équipements d'une baie et appliquer les consignes de sécurité | C09 |
| **M02** | [Câblage cuivre : poser, tester, brasser, étiqueter](M02.md) | Raccorder, tester et étiqueter une prise RJ45 en T568B (sur un vrai câble) | C09 · C06 |
| **M03** | [Adresses IP, masque, passerelle, DHCP, DNS](M03.md) | Lire un plan d'adressage et vérifier la configuration d'un poste | C06 |
| **M04** | [Couches, protocoles, première méthode de dépannage](M04.md) | Appliquer la méthode : constater, délimiter, tester | C10 |
| **M05** | [Switch administrable (OmniSwitch)](M05.md) | Prendre en main le switch : console, nom, mot de passe, sauvegarde | C09 |
| **M06** | [Sous-réseaux et plan d'adressage](M06.md) | Remplir un plan d'adressage cohérent avec des sous-réseaux | C06 · C09 |
| **M07** | [VLAN (1)](M07.md) | Créer des VLAN et affecter des ports | C09 |
| **M08** | [VLAN (2) : trunk, passerelle, relais DHCP](M08.md) | Configurer un trunk, la passerelle d'un VLAN et le relais DHCP | C09 |
| **M09** | [Wi-Fi d'entreprise et isolement des patients](M09.md) | Rattacher un SSID à un VLAN et isoler le réseau des patients | C09 · C06 |
| **M10** | [Sauvegardes, mises à jour, journal d'intervention](M10.md) | Sauvegarder, planifier une mise à jour et tenir le journal | C10 |
| **M11** | [Lire un dossier, préparer l'intervention, recetter](M11.md) | Lire un dossier technique, planifier, écrire un plan de tests, rédiger un compte rendu | C06 |
| **M12** | [Dépannage d'une panne injectée](M12.md) | Traiter une panne de bout en bout et rendre compte | C10 |
| **M13** | [Mini-épreuve A : préparer, intervenir, valider](M13.md) | S'entraîner à la partie préparation et intervention en 1 h 30, puis combler les écarts | C06 · C09 |
| **M14** | [Mini-épreuve B : maintenance, dépannage, compte rendu](M14.md) | S'entraîner à la maintenance en 1 h 30, puis combler les écarts | C10 |
| **M15** | [Épreuve blanche de 3 h et bilan](M15.md) | Passer le sujet complet dans les conditions de l'examen | C06 · C09 · C10 |

## ⏱️ Rythme d'une séance de 4 h

Reprise (30 min) → essentiel (45 min) → TP (2 h) → bilan et passeport (30 min), plus une pause. Les TP se font dans le **simulateur réseau** (switch OmniSwitch simulé), sauf le câblage et les épreuves de fin de parcours, qui se font sur le **matériel réel**.

## 🚦 Trois jalons

| Jalon | Fin de la séance | Si non validé |
|---|---|---|
| 1 | M05 – câblage et réseau de base | M06 sert de rattrapage |
| 2 | M09 – switch, VLAN, Wi-Fi seul(e) avec la fiche | M10 sert de rattrapage |
| 3 | M12 – méthode de dépannage | M13 sert de rattrapage |

## 🧩 Couverture du référentiel

| Compétence | Séances |
|---|---|
| **C06** Valider la conformité d'une installation | M02, M03, M06, M09, M11, M13, M15 |
| **C09** Installer les éléments d'un système informatique | M01, M02, M05 à M09, M13, M15 |
| **C10** Exploiter un réseau informatique | M04, M10, M12, M14, M15 |

> [!WARNING]
> **À valider par l'enseignant.** Ce tableau s'appuie sur les intitulés U31 (C06, C09, C10) : à confronter à la grille nationale d'évaluation. Les TP sont écrits pour le simulateur (OmniSwitch AOS 6.4) et le plateau réel : **à tester** avant usage, en particulier la configuration du serveur DHCP du simulateur (M08) et les règles de filtrage `policy`, qui ne sont pas appliquées par le simulateur (M09).

## 🔭 Ce qui n'est pas au programme du parcours

Supervision et tickets, accès à distance, serveur Linux en détail et analyse approfondie des trames : utiles au métier, **non exigés** pour l'épreuve. À lire en option si le temps le permet.
