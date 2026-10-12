# TP 0 – Préparer VirtualBox

> [!EXAMPLE] 🚀 Pour aller plus loin
> Prérequis commun aux TP serveurs.

## Réseau des VM

Chaque VM a **deux cartes réseau** :

| Carte | Mode | Rôle |
|---|---|---|
| Carte 1 | **NAT** | accès à Internet (mises à jour, paquets) |
| Carte 2 | **Réseau privé hôte** (*Host-only*) | dialogue entre ton PC et tes VM, sans toucher le réseau du lycée |

Dans VirtualBox : *Paramètres de la VM → Réseau*. Le réseau privé hôte se crée dans *Fichier → Outils → Gestionnaire de réseau*.

## Instantanés

*Machine → Prendre un instantané*, nommé par exemple « propre-avant-apache ». Revenir en arrière : *Instantanés → Restaurer*.

## Vérifier

Sur un serveur Linux :

```bash
ip a            # les deux cartes ont-elles une adresse ?
ping -c 2 8.8.8.8
```

Note l'adresse de la carte privée hôte (souvent en 192.168.56.x) : les autres TP l'utilisent.

> [!TIP]
> VM Linux conseillée : **Debian ou Ubuntu Server** (sans interface graphique, légère).
