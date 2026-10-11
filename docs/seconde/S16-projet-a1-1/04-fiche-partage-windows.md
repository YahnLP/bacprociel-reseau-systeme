# 🧩 Fiche guidée – Partager un dossier et une imprimante (Windows 11, groupe de travail)

*Projet A1 – S16 – étape D. Les captures et libellés peuvent légèrement varier selon la version de Windows.*

> [!NOTE]
> **Objectif.** Sur le **poste 1**, partager le dossier `Commandes` : le compte `direction` **modifie**, le compte `atelier` **lit**. Puis ajouter l'imprimante réseau `192.168.1.150`.

## 1. Préparer le poste 1

1. Ouvre **Paramètres → Réseau et Internet → Paramètres réseau avancés → Paramètres de partage avancés**.
2. Dans **Réseaux privés** : active **Découverte du réseau** et **Partage de fichiers et d'imprimantes**.
3. Vérifie que le réseau est de profil **Privé** (Paramètres → Réseau → *Ethernet* → Type de profil réseau).

## 2. Créer les comptes (en administrateur)

Dans un terminal **administrateur**, ou **Gestion de l'ordinateur → Utilisateurs et groupes locaux** :

```text
net user direction MotDePasse1! /add
net user atelier MotDePasse2! /add
```

> [!WARNING]
> **Les mots de passe ci-dessus sont des exemples** pour le TP. Choisis les tiens (≥ 12 caractères) et ne les réutilise jamais ailleurs.

## 3. Créer et partager le dossier

1. Crée `C:\Commandes`.
2. Clic droit → **Propriétés → Partage → Partage avancé…**
3. Coche **Partager ce dossier** ; **Autorisations** : donne **Contrôle total** au groupe **Tout le monde** (le partage laisse passer ; les droits fins sont dans l'onglet *Sécurité*).

## 4. Régler les droits (onglet **Sécurité**)

1. **Modifier… → Ajouter…** → `direction` : cocher **Modification**.
2. **Ajouter…** → `atelier` : cocher **Lecture et exécution** seulement.
3. Retire le groupe **Utilisateurs** s'il donne plus de droits que prévu (clique **Avancé** pour vérifier).

## 5. Tester depuis le poste 2

1. Dans l'Explorateur : `\\PC1\Commandes` (ou l'adresse IP du poste 1 : `\\192.168.1.xx\Commandes`).
2. Connecte-toi avec `atelier` → tu **lis**, tu ne peux **pas supprimer** ✔.
3. Déconnecte-toi (`net use * /delete`), reconnecte-toi avec `direction` → tu **modifies** ✔.

## 6. Ajouter l'imprimante réseau

1. **Paramètres → Bluetooth et appareils → Imprimantes et scanners → Ajouter un appareil → Ajouter manuellement**.
2. Choisis **Ajouter une imprimante avec une adresse IP ou un nom d'hôte**.
3. Type d'appareil : **TCP/IP** ; nom d'hôte : `192.168.1.150`.
4. Pilote : selon le modèle (ou *Imprimante générique* pour le TP) ; imprime une **page de test**.

✅ **Contrôle :** la page de test sort (ou, en simulateur, le `ping` de l'imprimante répond).

## ✍️ À consigner dans ton dossier

| Élément | Valeur |
|---|---|
| Comptes créés | |
| Chemin du partage | |
| Droits `direction` / `atelier` | |
| Test refusé pour `atelier` (suppression) | ✔ / ✘ |
| Imprimante ajoutée (adresse) | |
