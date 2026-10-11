@echo off
rem Prepare la chasse au tresor (S06 - terminal). A lancer UNE fois : double-clic ou creer-tresor.cmd
cd /d %USERPROFILE%
if exist chasse-au-tresor rmdir /s /q chasse-au-tresor
mkdir chasse-au-tresor
cd chasse-au-tresor
mkdir carte
mkdir foret
mkdir foret\clairiere
mkdir riviere
mkdir riviere\pont
mkdir montagne
mkdir montagne\grotte
mkdir coffre
echo BIENVENUE, CHERCHEUR DE TRESOR !> LISEZ-MOI.txt
echo.>> LISEZ-MOI.txt
echo Un tresor est cache dans ces dossiers. Pour le trouver, tu n'as droit>> LISEZ-MOI.txt
echo qu'a UN outil : le terminal (pas d'explorateur de fichiers !).>> LISEZ-MOI.txt
echo.>> LISEZ-MOI.txt
echo Chaque indice contient UNE LETTRE. A la fin, les 7 lettres forment un mot.>> LISEZ-MOI.txt
echo.>> LISEZ-MOI.txt
echo Premier indice : le fichier etape1.txt est dans le dossier carte.>> LISEZ-MOI.txt
echo Pour lire un fichier dans le terminal : cat (Linux) ou type (Windows).>> LISEZ-MOI.txt
echo ETAPE 1 - Bravo, tu sais LIRE un fichier !> carte\etape1.txt
echo Lettre 1 : C>> carte\etape1.txt
echo.>> carte\etape1.txt
echo Prochaine mission : va dans le dossier foret (commande cd).>> carte\etape1.txt
echo Regarde ce qu'il contient (commande ls sous Linux, dir sous Windows).>> carte\etape1.txt
echo Puis entre dans le dossier clairiere et lis etape2.txt.>> carte\etape1.txt
echo Ce fichier est un piege : il ne contient aucune lettre.> foret\arbre-creux.txt
echo Un bon technicien lit ce qu'il y a dans le dossier avant de choisir.>> foret\arbre-creux.txt
echo ETAPE 2 - Tu navigues bien !> foret\clairiere\etape2.txt
echo Lettre 2 : A>> foret\clairiere\etape2.txt
echo.>> foret\clairiere\etape2.txt
echo Il y a un FICHIER CACHE dans cette clairiere : son nom commence par etape3.>> foret\clairiere\etape2.txt
echo Pour afficher les fichiers caches : ls -a (Linux) ou dir /a (Windows).>> foret\clairiere\etape2.txt
echo Lis-le avec cat ou type.>> foret\clairiere\etape2.txt
echo ETAPE 3 - Bien joue, tu as trouve le fichier cache !> foret\clairiere\etape3-cache.txt
echo Lettre 3 : B>> foret\clairiere\etape3-cache.txt
echo.>> foret\clairiere\etape3-cache.txt
echo Maintenant, remonte d'un dossier avec cd .. (deux points).>> foret\clairiere\etape3-cache.txt
echo Remonte encore une fois pour revenir dans chasse-au-tresor.>> foret\clairiere\etape3-cache.txt
echo Puis va dans riviere, puis dans pont. Lis etape4.txt.>> foret\clairiere\etape3-cache.txt
attrib +h foret\clairiere\etape3-cache.txt
echo ETAPE 4 - Les chemins n'ont plus de secret pour toi ?> riviere\pont\etape4.txt
echo Lettre 4 : L>> riviere\pont\etape4.txt
echo.>> riviere\pont\etape4.txt
echo La grotte est dans le dossier montagne. Depuis ici, le chemin RELATIF est :>> riviere\pont\etape4.txt
echo ../../montagne/grotte   (sous Windows : ..\..\montagne\grotte)>> riviere\pont\etape4.txt
echo Tape cd avec ce chemin, en UNE seule commande. Lis etape5.txt.>> riviere\pont\etape4.txt
echo ETAPE 5 - Tu es dans la grotte.> montagne\grotte\etape5.txt
echo Lettre 5 : A>> montagne\grotte\etape5.txt
echo.>> montagne\grotte\etape5.txt
echo 1) Cree un dossier nomme camp dans chasse-au-tresor (commande mkdir).>> montagne\grotte\etape5.txt
echo    Astuce : le dossier chasse-au-tresor est deux niveaux plus haut : ../../camp>> montagne\grotte\etape5.txt
echo 2) COPIE le fichier cle.txt de cette grotte dans le dossier camp (cp ou copy).>> montagne\grotte\etape5.txt
echo 3) Verifie avec ls ou dir que cle.txt est dans camp ET toujours dans la grotte.>> montagne\grotte\etape5.txt
echo Ensuite, va au coffre : dossier coffre, dans chasse-au-tresor. Lis etape6.txt.>> montagne\grotte\etape5.txt
echo Je suis la CLE du coffre. Copie-moi dans le dossier camp, sans me deplacer.> montagne\grotte\cle.txt
echo ETAPE 6 - Le coffre !> coffre\etape6.txt
echo Lettre 6 : G>> coffre\etape6.txt
echo.>> coffre\etape6.txt
echo 1) Il y a ici un fichier piege.txt : SUPPRIME-LE (rm ou del).>> coffre\etape6.txt
echo    Attention : pas de corbeille dans le terminal. C'est definitif !>> coffre\etape6.txt
echo 2) Cree un fichier nomme mon-nom.txt contenant ton prenom>> coffre\etape6.txt
echo    (echo Prenom ^> mon-nom.txt).>> coffre\etape6.txt
echo 3) DEPLACE ce fichier mon-nom.txt dans le dossier camp (mv ou move).>> coffre\etape6.txt
echo Dernier indice : lis final.txt (dans ce dossier).>> coffre\etape6.txt
echo Supprime-moi ! (et demande-toi pourquoi il faut faire attention avant de supprimer).> coffre\piege.txt
echo ETAPE 7 - DERNIERE ETAPE> coffre\final.txt
echo Lettre 7 : E>> coffre\final.txt
echo.>> coffre\final.txt
echo Assemble les 7 lettres dans l'ordre : le mot est le nom d'un metier de CIEL.>> coffre\final.txt
echo Montre ton terminal a l'enseignant et explique chaque commande utilisee.>> coffre\final.txt
echo Chasse au tresor prete dans %USERPROFILE%\chasse-au-tresor
pause
