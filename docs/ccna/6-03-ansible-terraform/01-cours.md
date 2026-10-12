# 📖 Cours – Ansible et Terraform

*Parcours CCNA – Domaine 6 – module 6-03 (sujet 6.6)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**. Cours théorique : l'examen demande de **reconnaître** les outils, pas de les installer.

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer la **gestion de configuration** (*configuration management*) ;
- [ ] décrire **Ansible** (playbook, inventaire, sans agent) ;
- [ ] décrire **Terraform** (infrastructure as code, état) ;
- [ ] comparer les approches **impérative** et **déclarative**.

---

## 1. Le problème : la dérive de configuration

Quand des équipements sont configurés **à la main**, ils **s'éloignent** peu à peu de la référence (*configuration drift*). La **gestion de configuration** décrit l'état voulu **dans des fichiers** et l'applique automatiquement. C'est l'**infrastructure as code** (IaC) : le réseau se gère **comme du code** (fichiers versionnés, relus, testés).

## 2. Impératif ou déclaratif ?

| Approche | Principe | Exemple |
|---|---|---|
| **Impérative** | On décrit **les étapes** à exécuter | « Entre dans le switch, tape ces 5 commandes » |
| **Déclarative** | On décrit **l'état final voulu**, l'outil trouve comment y arriver | « Le VLAN 10 doit exister et s'appeler COMPTA » |

Une approche déclarative est **idempotente** : on peut l'appliquer **plusieurs fois**, le résultat est le **même** (pas de doublon).

## 3. Ansible

| Élément | Rôle |
|---|---|
| **Inventaire** (*inventory*) | La **liste des équipements**, en groupes |
| **Playbook** | Fichier **YAML** qui décrit les tâches à appliquer |
| **Module** | Une action prête à l'emploi (ex. configurer un VLAN) |
| **Sans agent** (*agentless*) | **Rien à installer** sur l'équipement : connexion par **SSH** ou API |
| **Mode** | Surtout **« push »** : la machine de contrôle **pousse** les changements |

```yaml
---
- name: Créer le VLAN 10 sur les switchs
  hosts: switchs
  gather_facts: no
  tasks:
    - name: VLAN 10 COMPTA
      cisco.ios.ios_vlans:
        config:
          - vlan_id: 10
            name: COMPTA
        state: merged
```

## 4. Terraform

| Élément | Rôle |
|---|---|
| **Langage HCL** | Fichiers `.tf` **déclaratifs** |
| **Fournisseur** (*provider*) | Le « pilote » qui parle à un service (cloud, réseau, ...) |
| **État** (*state*) | Fichier qui retient ce qui **existe déjà** |
| `terraform plan` | **Montre** ce qui va changer |
| `terraform apply` | **Applique** le changement |

Terraform sert surtout à **créer l'infrastructure** (réseaux virtuels, machines, pare-feu dans le cloud). Ansible sert surtout à **configurer** ce qui existe.

## 5. Comparaison

| | **Ansible** | **Terraform** |
|---|---|---|
| Rôle principal | **Configurer** des équipements | **Provisionner** l'infrastructure |
| Langage | YAML | HCL |
| Agent | **Aucun** | Aucun |
| Style | Plutôt procédural (tâches) | **Déclaratif** |
| Mémoire de l'état | Non (on interroge l'équipement) | **Oui** (fichier d'état) |

---

## ✍️ Quiz de fin

**1.** Que signifie « sans agent » pour Ansible ?

<details markdown="1"><summary>Voir la réponse</summary>

Aucun **logiciel à installer** sur l'équipement : Ansible s'y connecte en **SSH** ou par **API**.

</details>

**2.** Quelle commande Terraform montre les changements prévus ?

<details markdown="1"><summary>Voir la réponse</summary>

`terraform plan`.

</details>

**3.** Pourquoi l'approche déclarative est-elle « idempotente » ?

<details markdown="1"><summary>Voir la réponse</summary>

On décrit un **état final** : l'appliquer **plusieurs fois** donne le **même** résultat.

</details>

**4.** Quel outil pour créer des réseaux virtuels dans le cloud ?

<details markdown="1"><summary>Voir la réponse</summary>

**Terraform**.

</details>

## 🛠️ Mini-activité sur papier

Écris, en **YAML**, un playbook qui crée le VLAN **20** nommé **ATELIER** sur un groupe `switchs` (inspire-toi de l'exemple). Puis explique **ce qui se passe** si tu l'exécutes **deux fois**.
