# Corrigé – Première S16 (étude)

Plan de référence : voir `docs/premiere/S17-projet-2-realisation/00-plan-de-reference.md` (adressage, ports, câblage, 9 câbles droits). Installation complète : `P16-projet-corrige.json`.

**Flux** : Direction et Atelier → tout (sauf invités, « inutile ») ; Invités → serveur web + DNS seulement ; invités → Direction, Atelier, imprimante : NON.

**Découpage attendu** : Direction /27 (3 personnes + portables, marge large), Atelier /27 (2 postes + imprimante + serveur + marge), Invités /26 (62). Variante acceptable : Direction /28 (14 machines utiles) ; invités /27 si moins de 28 invités. **Pas acceptable** : blocs non alignés, chevauchement, adresses fixes dans le pool.

**Réponses à la revue** : invités et imprimante → non (imprimante en Atelier, ACL) ; 5 recrues à l'Atelier → /27 offre 30 machines, il reste de la marge, sinon prendre un bloc de la réserve .128/25 ; panne du switch → tous les services coupés (point unique de défaillance) ; câbles → étiquettes C01 à C09 aux deux bouts + tableau.

**Question de la partie A** : non, les invités ne peuvent pas imprimer (imprimante en VLAN 20, ACL de la patte Invités).

**Partie D** : 9 câbles droits.
