#!/bin/bash
# Prepare la chasse au tresor (S06 - terminal). A lancer UNE fois : bash creer-tresor.sh
# Cree le dossier ~/chasse-au-tresor
cd ~ || exit 1
rm -rf "chasse-au-tresor"
mkdir "chasse-au-tresor"
cd "chasse-au-tresor" || exit 1
mkdir -p "carte"
mkdir -p "foret"
mkdir -p "foret/clairiere"
mkdir -p "riviere"
mkdir -p "riviere/pont"
mkdir -p "montagne"
mkdir -p "montagne/grotte"
mkdir -p "coffre"
cat > "LISEZ-MOI.txt" <<'FIN'
BIENVENUE, CHERCHEUR DE TRESOR !

Un tresor est cache dans ces dossiers. Pour le trouver, tu n'as droit
qu'a UN outil : le terminal (pas d'explorateur de fichiers !).

Chaque indice contient UNE LETTRE. A la fin, les 7 lettres forment un mot.

Premier indice : le fichier etape1.txt est dans le dossier carte.
Pour lire un fichier dans le terminal : cat (Linux) ou type (Windows).
FIN
cat > "carte/etape1.txt" <<'FIN'
ETAPE 1 - Bravo, tu sais LIRE un fichier !
Lettre 1 : C

Prochaine mission : va dans le dossier foret (commande cd).
Regarde ce qu'il contient (commande ls sous Linux, dir sous Windows).
Puis entre dans le dossier clairiere et lis etape2.txt.
FIN
cat > "foret/arbre-creux.txt" <<'FIN'
Ce fichier est un piege : il ne contient aucune lettre.
Un bon technicien lit ce qu'il y a dans le dossier avant de choisir.
FIN
cat > "foret/clairiere/etape2.txt" <<'FIN'
ETAPE 2 - Tu navigues bien !
Lettre 2 : A

Il y a un FICHIER CACHE dans cette clairiere : son nom commence par etape3.
Pour afficher les fichiers caches : ls -a (Linux) ou dir /a (Windows).
Lis-le avec cat ou type.
FIN
cat > "foret/clairiere/.etape3-cache.txt" <<'FIN'
ETAPE 3 - Bien joue, tu as trouve le fichier cache !
Lettre 3 : B

Maintenant, remonte d'un dossier avec cd .. (deux points).
Remonte encore une fois pour revenir dans chasse-au-tresor.
Puis va dans riviere, puis dans pont. Lis etape4.txt.
FIN
cat > "riviere/pont/etape4.txt" <<'FIN'
ETAPE 4 - Les chemins n'ont plus de secret pour toi ?
Lettre 4 : L

La grotte est dans le dossier montagne. Depuis ici, le chemin RELATIF est :
../../montagne/grotte   (sous Windows : ..\..\montagne\grotte)
Tape cd avec ce chemin, en UNE seule commande. Lis etape5.txt.
FIN
cat > "montagne/grotte/etape5.txt" <<'FIN'
ETAPE 5 - Tu es dans la grotte.
Lettre 5 : A

1) Cree un dossier nomme camp dans chasse-au-tresor (commande mkdir).
   Astuce : le dossier chasse-au-tresor est deux niveaux plus haut : ../../camp
2) COPIE le fichier cle.txt de cette grotte dans le dossier camp (cp ou copy).
3) Verifie avec ls ou dir que cle.txt est dans camp ET toujours dans la grotte.
Ensuite, va au coffre : dossier coffre, dans chasse-au-tresor. Lis etape6.txt.
FIN
cat > "montagne/grotte/cle.txt" <<'FIN'
Je suis la CLE du coffre. Copie-moi dans le dossier camp, sans me deplacer.
FIN
cat > "coffre/etape6.txt" <<'FIN'
ETAPE 6 - Le coffre !
Lettre 6 : G

1) Il y a ici un fichier piege.txt : SUPPRIME-LE (rm ou del).
   Attention : pas de corbeille dans le terminal. C'est definitif !
2) Cree un fichier nomme mon-nom.txt contenant ton prenom
   (echo Prenom > mon-nom.txt).
3) DEPLACE ce fichier mon-nom.txt dans le dossier camp (mv ou move).
Dernier indice : lis final.txt (dans ce dossier).
FIN
cat > "coffre/piege.txt" <<'FIN'
Supprime-moi ! (et demande-toi pourquoi il faut faire attention avant de supprimer).
FIN
cat > "coffre/final.txt" <<'FIN'
ETAPE 7 - DERNIERE ETAPE
Lettre 7 : E

Assemble les 7 lettres dans l'ordre : le mot est le nom d'un metier de CIEL.
Montre ton terminal a l'enseignant et explique chaque commande utilisee.
FIN
echo "Chasse au tresor prete dans ~/chasse-au-tresor ."
