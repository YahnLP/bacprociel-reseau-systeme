# Corrigé – Terminale S13

Fichier : `T13-recette-corrige.json`.

**Partie A (exemple)** : 1) Le personnel se connecte au Wi-Fi interne → adresse `192.168.20.x` ; 2) le personnel joint le serveur → ping OK ; 3) un invité se connecte → adresse `192.168.30.x` ; 4) un invité joint sa passerelle `192.168.30.1` → OK ; 5) **négatif** : un invité ne joint **pas** `192.168.10.10` ; 6) **négatif** : un invité ne joint **pas** le portable du personnel.

**Partie B** : sur l'installation de départ, les tests 1 à 4 sont conformes ; les tests 5 et 6 sont **non conformes** (les invités joignent le serveur et le portable du personnel).

**Partie C** : cause : l'ACL `INVITES-IN` n'est pas appliquée à `gi0/0.30` ; correction : `interface gi0/0.30` → `ip access-group INVITES-IN in` (l'ACL existe déjà dans le fichier : la commande applique sa définition) ; après correction, tests 5 et 6 conformes. **Non-conformité** (et pas simple réserve), car c'est un défaut de **sécurité** demandé explicitement par le client.

**Partie D** : PV complété avec 6 tests, 0 réserve après correction, documents remis (plan d'adressage, schéma, notice), signatures.

**Partie E** : le client doit comprendre « un SSID = le nom du réseau Wi-Fi », que les invités ne peuvent pas atteindre le réseau du personnel, et qui contacter.

**Contrôles automatiques** : 6/6 verts sur le corrigé.
