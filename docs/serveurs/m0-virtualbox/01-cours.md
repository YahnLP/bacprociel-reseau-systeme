# 📖 Cours – Virtualisation et VirtualBox

*Parcours serveurs – module 0*

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer ce qu'est une **machine virtuelle** et un **hyperviseur** ;
- [ ] choisir le bon **mode réseau** d'une VM ;
- [ ] utiliser les **instantanés** pour travailler sans risque.

---

## 1. Machine virtuelle et hyperviseur

Une **machine virtuelle (VM)** est un ordinateur « simulé » : elle a son processeur, sa mémoire, son disque et ses cartes réseau, mais tout cela est fourni par ton vrai PC (**l'hôte**). Le logiciel qui les fournit est l'**hyperviseur**.

| | Type 1 | Type 2 |
|---|---|---|
| Fonctionne | directement sur le matériel | dans un système déjà installé |
| Exemples | Proxmox, VMware ESXi, Hyper-V | **VirtualBox**, VMware Workstation |
| Usage | serveurs de production | apprentissage, tests |

## 2. Les modes réseau de VirtualBox

| Mode | La VM… | Usage |
|---|---|---|
| **NAT** | sort sur Internet, mais personne ne peut la joindre | mises à jour, paquets |
| **Réseau privé hôte** (*host-only*) | dialogue avec ton PC et les autres VM, **sans** sortie | tes TP serveurs |
| **Réseau interne** | dialogue seulement avec les VM du même réseau interne | tests entre VM |
| **Accès par pont** (*bridge*) | apparaît sur le réseau réel comme un vrai poste | à éviter au lycée sans accord |

> [!TIP]
> Pour tes serveurs : **carte 1 en NAT** (Internet) et **carte 2 en réseau privé hôte** (ton PC joint le serveur).

## 3. Instantanés (snapshots)

Un **instantané** garde l'état exact de la VM. Tu en prends un **avant** une manipulation risquée ; si tout casse, tu **restaures**.

> [!WARNING]
> Un instantané n'est pas une sauvegarde : il reste dans le même dossier que la VM. Pour une vraie sauvegarde, **exporte** la VM (*Fichier → Exporter un appareil virtuel*).

---

## 🧠 Quiz de fin

**1.** VirtualBox est-il un hyperviseur de type 1 ou 2 ?

<details markdown="1"><summary>Voir la réponse</summary>

De **type 2** : il s'installe dans un système existant.

</details>

**2.** Quel mode permet à ton PC de joindre un serveur VM sans passer par le réseau du lycée ?

<details markdown="1"><summary>Voir la réponse</summary>

Le **réseau privé hôte**.

</details>

**3.** Pourquoi prendre un instantané avant de modifier un serveur ?

<details markdown="1"><summary>Voir la réponse</summary>

Pour **revenir en arrière** si la modification casse le système.

</details>

➡️ Suite : [le TP du module](02-tp.md).
