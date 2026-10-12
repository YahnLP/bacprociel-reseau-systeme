# 📖 Cours – API REST et JSON

*Parcours CCNA – Domaine 6 – module 6-02 (sujets 6.5 et 6.7)*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Module du parcours CCNA, **hors programme E31**. Tu manipules déjà des fichiers `.json` : ceux du simulateur !

## 🎯 À la fin de ce cours, tu sauras

- [ ] expliquer ce qu'est une **API REST** ;
- [ ] relier les **verbes HTTP** aux opérations **CRUD** ;
- [ ] lire et écrire du **JSON** ;
- [ ] comprendre les **codes de réponse** HTTP.

---

## 1. Qu'est-ce qu'une API REST ?

Une **API** (*Application Programming Interface*) est une « prise » par laquelle un **programme** parle à un autre. **REST** est un style d'API qui utilise **HTTP** : on envoie une **requête** à une **URL**, on reçoit une **réponse**.

| Élément d'une requête | Exemple |
|---|---|
| **Verbe** (méthode) | `GET` |
| **URL** | `https://controleur.exemple.fr/api/v1/devices` |
| **En-têtes** | `Content-Type: application/json`, jeton d'authentification |
| **Corps** (pour `POST`, `PUT`) | `{"hostname": "SW1"}` |

### CRUD et verbes HTTP

| Opération | Verbe HTTP | Effet |
|---|---|---|
| **C**reate | **POST** | Créer une ressource |
| **R**ead | **GET** | Lire |
| **U**pdate | **PUT** / **PATCH** | Remplacer / modifier en partie |
| **D**elete | **DELETE** | Supprimer |

## 2. Authentification des API

| Type | Principe |
|---|---|
| **Basic** | Identifiant et mot de passe (encodés, **pas chiffrés** : exige HTTPS) |
| **Clé d'API** (*API key*) | Une longue clé dans un en-tête |
| **Jeton** (*token*, Bearer) | On obtient un **jeton temporaire** puis on l'envoie à chaque requête |
| **OAuth 2.0** | Accès délégué, avec jetons à durée limitée |

## 3. Codes de réponse HTTP

| Code | Sens |
|---|---|
| **200** OK | Succès |
| **201** Created | Ressource créée |
| **204** No Content | Succès, rien à renvoyer |
| **400** Bad Request | Requête mal formée |
| **401** Unauthorized | Authentification manquante ou fausse |
| **403** Forbidden | Authentifié, mais **pas le droit** |
| **404** Not Found | Ressource introuvable |
| **500** Internal Server Error | Erreur du **serveur** |

## 4. JSON

**JSON** (*JavaScript Object Notation*) est un format **texte** lisible pour échanger des données.

```json
{
  "hostname": "SW1",
  "model": "WS-C2960",
  "interfaces": [
    {"name": "Fa0/1", "status": "up", "vlan": 10},
    {"name": "Fa0/2", "status": "down", "vlan": 20}
  ],
  "managed": true,
  "uptime_days": 42,
  "notes": null
}
```

| Composant | Notation | Exemple |
|---|---|---|
| **Objet** | `{ }` : paires **clé : valeur** | `{"vlan": 10}` |
| **Tableau** | `[ ]` : liste ordonnée | `[10, 20, 30]` |
| **Chaîne** | entre **guillemets doubles** | `"SW1"` |
| **Nombre** | sans guillemets | `42` |
| **Booléen** | `true` / `false` | `true` |
| **Nul** | `null` | `null` |

> [!WARNING]
> **Règles de syntaxe :** les clés sont **toujours entre guillemets doubles** ; **pas de virgule finale** ; **pas de commentaires**. Une erreur et le fichier est rejeté.

### Autres encodages

**XML** (balises, plus lourd), **YAML** (indentation, très utilisé avec Ansible). JSON est le plus répandu pour les API REST.

---

## ✍️ Exercices

**1.** Dans l'exemple ci-dessus, comment accède-t-on au **statut de `Fa0/2`** ?

<details markdown="1"><summary>Voir la réponse</summary>

`interfaces[1].status` → `"down"` (le tableau commence à l'indice **0**).

</details>

**2.** Quelle requête REST **crée** un nouveau VLAN ? Quel code attend-on en cas de succès ?

<details markdown="1"><summary>Voir la réponse</summary>

Un **POST** sur l'URL des VLAN, avec le JSON du VLAN dans le corps. Succès : **201 Created**.

</details>

**3.** Ce JSON est-il valide ? `{ nom: "SW1", "ports": [1, 2, 3,] }`

<details markdown="1"><summary>Voir la réponse</summary>

**Non** : la clé `nom` n'est pas entre guillemets et il y a une **virgule finale** après `3`.

</details>

**4.** Tu reçois `401`. Que vérifies-tu ? Et pour `403` ?

<details markdown="1"><summary>Voir la réponse</summary>

`401` : le **jeton / les identifiants**. `403` : les **droits** du compte (il est reconnu mais non autorisé).

</details>

## 🛠️ Mini-TP : lire du JSON avec Python

Tous les postes de la salle ont Python. Enregistre le script `lire.py` :

```python
import json

texte = """
{"hostname": "SW1",
 "interfaces": [
   {"name": "Fa0/1", "status": "up",   "vlan": 10},
   {"name": "Fa0/2", "status": "down", "vlan": 20}
 ]}
"""
equipement = json.loads(texte)
print("Équipement :", equipement["hostname"])
for i in equipement["interfaces"]:
    print(i["name"], "→", i["status"])
```

Lance-le avec `python3 lire.py`. Puis :

1. Ajoute une interface `Fa0/3` en VLAN 30 et relance.
2. Affiche **seulement** les interfaces `down`.
3. Ouvre un fichier `.json` du simulateur du site et affiche le nom de chaque équipement (indice : regarde sa structure).

✅ **Point de contrôle :** tu sais lire une valeur imbriquée dans un JSON.
