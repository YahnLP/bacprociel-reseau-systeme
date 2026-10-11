# 📝 QCM de révision – 20 questions

*Bac Pro CIEL – Première – S15 – **individuel**, 25 minutes, sans document*

Une seule bonne réponse par question. **Entoure** ta réponse, puis corrige avec la grille en bas de page. Note le **domaine** de chaque erreur.

## Adressage (A)

**1.** Le masque `255.255.255.192` s'écrit :
a) /24  b) /25  c) /26  d) /27

**2.** Combien de machines peut-on adresser dans un `/27` ?
a) 32  b) 30  c) 28  d) 62

**3.** Adresse de diffusion de `192.168.50.64/26` :
a) 192.168.50.127  b) 192.168.50.95  c) 192.168.50.255  d) 192.168.50.63

## Routage (R)

**4.** Une passerelle par défaut sert à :
a) joindre les machines du même réseau  b) joindre les autres réseaux  c) obtenir une adresse  d) résoudre un nom

**5.** Dans `show ip route`, la lettre `C` signifie :
a) route configurée à la main  b) réseau directement connecté  c) route par défaut  d) route apprise par RIP

**6.** Le ping passe à l'aller mais pas au retour : cause la plus probable ?
a) câble coupé  b) route retour absente  c) masque erroné sur le DNS  d) VLAN supprimé

## VLAN (V)

**7.** Un port `access` appartient à :
a) tous les VLAN  b) un seul VLAN  c) aucun VLAN  d) uniquement le VLAN 1 natif

**8.** Un lien `trunk` transporte :
a) un seul VLAN  b) plusieurs VLAN étiquetés  c) uniquement le VLAN natif  d) du Wi-Fi

**9.** Commande pour voir quel port est dans quel VLAN :
a) show interfaces  b) show vlan brief  c) show ip route  d) show startup-config

## Services (S)

**10.** Le DHCP distribue :
a) des mots de passe  b) des adresses IP et paramètres réseau  c) des pages web  d) des noms de domaine

**11.** `ip helper-address` sert à :
a) relayer les demandes DHCP vers un serveur d'un autre réseau  b) filtrer le web  c) créer un VLAN  d) chiffrer SSH

**12.** Le DNS traduit :
a) une adresse MAC en IP  b) un nom en adresse IP  c) une IP en VLAN  d) un port en service

**13.** Le port par défaut de HTTPS est :
a) 22  b) 53  c) 80  d) 443

**14.** Pour tester la résolution d'un nom, on utilise :
a) nslookup  b) tracert  c) ipconfig /release  d) show vlan

## Sécurité et câblage (C)

**15.** Pourquoi préférer SSH à Telnet ?
a) il est plus rapide  b) il chiffre l'échange, mot de passe compris  c) il ne demande pas de mot de passe  d) il passe le pare-feu

**16.** Que fait `enable secret` ?
a) protège l'accès privilégié avec un mot de passe chiffré  b) crée un VLAN  c) active SSH  d) sauvegarde la configuration

**17.** Une ACL se lit :
a) de bas en haut  b) de haut en bas, la première règle qui correspond s'applique  c) au hasard  d) toutes les règles s'additionnent

**18.** Un câble cuivre de catégorie 6 relie deux équipements au maximum sur :
a) 10 m  b) 50 m  c) 90 m de câblage fixe (100 m avec les cordons)  d) 500 m

**19.** Quelle commande enregistre la configuration d'un équipement Cisco ?
a) save  b) write memory  c) commit  d) store

**20.** Un poste a l'adresse 169.254.x.x. Cause probable :
a) le DHCP n'a pas répondu  b) le DNS est faux  c) le mot de passe est faux  d) la passerelle est absente de la table de routage

<details markdown="1"><summary>🔑 Correction (à ouvrir après avoir répondu)</summary>

| Q | Rép. | Domaine | | Q | Rép. | Domaine |
|---|---|---|---|---|---|---|
| 1 | c | A | | 11 | a | S |
| 2 | b | A | | 12 | b | S |
| 3 | a | A | | 13 | d | S |
| 4 | b | R | | 14 | a | S |
| 5 | b | R | | 15 | b | C |
| 6 | b | R | | 16 | a | C |
| 7 | b | V | | 17 | b | C |
| 8 | b | V | | 18 | c | C |
| 9 | b | V | | 19 | b | C |
| 10 | b | S | | 20 | a | S |

**Décompte par domaine** : A = Q1-3 ; R = Q4-6 ; V = Q7-9 ; S = Q10-14 et Q20 ; C = Q15-19. Un domaine à **moins de la moitié** des points = atelier de remédiation conseillé (voir [le TP](03-tp-ateliers.md)).

</details>
