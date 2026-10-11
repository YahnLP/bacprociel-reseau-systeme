# Réseaux et systèmes – Bac Pro CIEL (E31)

Cours, TP et ressources du module **E31 « Mise en œuvre de réseaux informatiques »** du Bac Pro CIEL (Seconde, Première, Terminale). Auteur : Yahn LE PRETTRE, Enseignant à la MFR de Pontonx – licence CC BY-NC-SA 4.0.

📖 **Site (GitHub Pages) :** <https://yahnlp.github.io/bacprociel-reseau-systeme/>

## Contenu

| Dossier | Contenu |
|---|---|
| [`docs/seconde`](docs/seconde/README.md) | 18 séances : matériel, systèmes, terminal, câblage, IP, DHCP, DNS, Wi-Fi, dépannage, projet A1 |
| [`docs/premiere`](docs/premiere/README.md) | 20 séances : couches, switch, sous-réseaux, routage, VLAN, serveurs, sécurité, projet A2 |
| [`docs/terminale`](docs/terminale/README.md) | 19 séances : chantiers autonomes, dépannage, recette, préparation de l'E31 |
| [`docs/ressources`](docs/ressources/README.md) | Passeport d'autonomie, glossaire, mode d'emploi du simulateur |
| [`docs/simulateur`](docs/simulateur/) | Le simulateur réseau hors ligne (un seul fichier HTML) |
| [`corriges`](corriges/) | Corrigés et fichiers de correction **réservés à l'enseignant** (non publiés sur le site) |
| [`tools`](tools/) | Scripts de fabrication des figures SVG, des TP du simulateur et des index |

## Principe pédagogique

Manipuler → nommer → comprendre → configurer → dépanner → documenter. Chaque cours contient des **questions de compréhension** avec réponses repliées.

## Travailler en local

```bash
pip install -r requirements.txt
mkdocs serve        # http://127.0.0.1:8000
```

Régénérer les figures et les TP :

```bash
python3 tools/illus/seconde_a.py        # figures SVG
node tools/tp/seconde.js                # fichiers .json du simulateur (vérifiés par le moteur)
python3 tools/make_nav.py               # index des années
```

## Licence

Contenus : **CC BY-NC-SA 4.0**. Simulateur : **EUPL 1.2**.
