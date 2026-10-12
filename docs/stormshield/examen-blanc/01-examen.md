# 📝 Examen blanc CSNA

*Parcours Stormshield – questions sur les modules S01 à S10*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Questionnaire d'**entraînement** à faire **sans cours** ni simulateur. Il teste les **notions** ; l'examen officiel CSNA est passé chez Stormshield et comporte ses propres questions.

> [!TIP]
> Note tes réponses sur une feuille puis ouvre « Voir la réponse ». **≥ 70 %** : tu es bien parti. Sinon, reprends les modules des questions ratées.


## S01 – Prise en main

**Q1.** Avant une mise à jour du système d'un pare-feu, on doit :

- A. redémarrer le routeur
- B. sauvegarder la configuration
- C. supprimer les journaux
- D. désactiver le filtrage

<details markdown="1"><summary>Voir la réponse</summary>

**B.** sauvegarder la configuration — Sauvegarde d'abord, mise à jour ensuite.

</details>

**Q2.** Quel est le meilleur usage de l'interface web d'administration ?

- A. l'exposer sur Internet
- B. la laisser avec le mot de passe d'usine
- C. l'utiliser depuis un réseau interne maîtrisé, mot de passe changé
- D. la désactiver pour toujours

<details markdown="1"><summary>Voir la réponse</summary>

**C.** l'utiliser depuis un réseau interne maîtrisé, mot de passe changé — Accès restreint et mot de passe changé.

</details>

**Q3.** EVA désigne :

- A. un protocole VPN
- B. l'image virtuelle d'un pare-feu Stormshield
- C. un type d'attaque
- D. un module d'antivirus

<details markdown="1"><summary>Voir la réponse</summary>

**B.** l'image virtuelle d'un pare-feu Stormshield — Elastic Virtual Appliance.

</details>


## S02 – Journaux

**Q4.** Un flux est bloqué avec le motif « politique par défaut ». Cela signifie :

- A. une règle l'a explicitement bloqué
- B. aucune règle ne l'autorise
- C. le pare-feu est en panne
- D. le flux est chiffré

<details markdown="1"><summary>Voir la réponse</summary>

**B.** aucune règle ne l'autorise — Il faut créer une règle si le flux est légitime.

</details>

**Q5.** Première action pour dépanner un flux qui ne passe pas :

- A. redémarrer le pare-feu
- B. chercher la ligne dans le journal de filtrage
- C. supprimer toutes les règles
- D. changer l'adresse du serveur

<details markdown="1"><summary>Voir la réponse</summary>

**B.** chercher la ligne dans le journal de filtrage — Le journal indique l'action et la règle.

</details>


## S03 – Objets

**Q6.** Quel objet regroupe plusieurs hôtes ?

- A. un service
- B. une plage
- C. un groupe
- D. une interface

<details markdown="1"><summary>Voir la réponse</summary>

**C.** un groupe — Un groupe réunit plusieurs objets.

</details>

**Q7.** Principal intérêt d'un objet nommé dans une règle :

- A. la vitesse
- B. la lisibilité et la modification à un seul endroit
- C. le chiffrement
- D. l'authentification

<details markdown="1"><summary>Voir la réponse</summary>

**B.** la lisibilité et la modification à un seul endroit — On change l'adresse dans l'objet, pas dans toutes les règles.

</details>

**Q8.** Un objet « service » contient :

- A. une adresse MAC
- B. un protocole et un port
- C. un utilisateur
- D. un certificat

<details markdown="1"><summary>Voir la réponse</summary>

**B.** un protocole et un port — Par exemple TCP 443.

</details>


## S04 – Configuration réseau

**Q9.** Quel mode insère un pare-feu sans changer l'adressage existant ?

- A. routeur
- B. transparent (pont)
- C. VPN
- D. NAT

<details markdown="1"><summary>Voir la réponse</summary>

**B.** transparent (pont) — Les interfaces sont regroupées dans un pont.

</details>

**Q10.** Pour joindre Internet, le pare-feu a besoin :

- A. d'une route par défaut vers le FAI
- B. d'un serveur DHCP
- C. d'un certificat
- D. d'un antivirus

<details markdown="1"><summary>Voir la réponse</summary>

**A.** d'une route par défaut vers le FAI — Route par défaut vers le routeur du fournisseur.

</details>

**Q11.** L'interface qui va vers Internet appartient à la zone :

- A. interne
- B. DMZ
- C. externe (WAN)
- D. VPN

<details markdown="1"><summary>Voir la réponse</summary>

**C.** externe (WAN) — Zone externe.

</details>


## S05 – NAT

**Q12.** Le NAT qui permet à tout un LAN de sortir avec une adresse publique :

- A. redirection
- B. masquerade (PAT)
- C. NAT 1:1
- D. aucun

<details markdown="1"><summary>Voir la réponse</summary>

**B.** masquerade (PAT) — Translation de source dynamique.

</details>

**Q13.** Pour publier un serveur web interne, il faut :

- A. seulement une redirection
- B. seulement une règle de filtrage
- C. une redirection et une règle de filtrage
- D. un VPN

<details markdown="1"><summary>Voir la réponse</summary>

**C.** une redirection et une règle de filtrage — Le NAT ne laisse rien passer à lui seul.

</details>

**Q14.** Un SNS évalue la politique de filtrage sur les adresses :

- A. après translation
- B. avant translation
- C. au hasard
- D. sans tenir compte des adresses

<details markdown="1"><summary>Voir la réponse</summary>

**B.** avant translation — Selon la documentation, avant translation.

</details>


## S06 – Filtrage

**Q15.** Une connexion web sortante autorisée : la réponse du serveur est…

- A. bloquée
- B. acceptée automatiquement (filtrage à états)
- C. journalisée uniquement
- D. redirigée

<details markdown="1"><summary>Voir la réponse</summary>

**B.** acceptée automatiquement (filtrage à états) — Le pare-feu mémorise la connexion.

</details>

**Q16.** Deux règles : (1) autoriser LAN→WAN tout ; (2) bloquer le poste 192.168.1.50. Résultat :

- A. le poste est bloqué
- B. le poste est autorisé : la règle 2 n'est jamais atteinte
- C. le pare-feu refuse la configuration
- D. le poste n'a plus d'adresse

<details markdown="1"><summary>Voir la réponse</summary>

**B.** le poste est autorisé : la règle 2 n'est jamais atteinte — La première règle qui correspond s'applique.

</details>

**Q17.** Que fait un flux qui ne correspond à aucune règle ?

- A. il passe
- B. il est bloqué
- C. il est redirigé
- D. il est chiffré

<details markdown="1"><summary>Voir la réponse</summary>

**B.** il est bloqué — Politique par défaut : bloquer.

</details>

**Q18.** « Reset » (rejeter) diffère de « block » car :

- A. il chiffre le paquet
- B. il prévient l'émetteur du refus
- C. il autorise
- D. il journalise moins

<details markdown="1"><summary>Voir la réponse</summary>

**B.** il prévient l'émetteur du refus — Block ignore silencieusement.

</details>


## S07 – Protection applicative

**Q19.** Quelle fonction bloque les attaques connues dans le trafic ?

- A. URL filtering
- B. IPS
- C. NAT
- D. DHCP

<details markdown="1"><summary>Voir la réponse</summary>

**B.** IPS — Intrusion Prevention System.

</details>

**Q20.** Quelle fonction exécute un fichier suspect dans un environnement isolé ?

- A. antivirus à signatures
- B. bac à sable (sandbox)
- C. masquerade
- D. portail captif

<details markdown="1"><summary>Voir la réponse</summary>

**B.** bac à sable (sandbox) — Analyse comportementale.

</details>

**Q21.** Pour analyser du trafic HTTPS, le pare-feu doit :

- A. l'ignorer
- B. le déchiffrer puis rechiffrer, avec une autorité reconnue des postes
- C. le bloquer
- D. changer le port

<details markdown="1"><summary>Voir la réponse</summary>

**B.** le déchiffrer puis rechiffrer, avec une autorité reconnue des postes — Inspection SSL.

</details>


## S08 – Authentification

**Q22.** Pourquoi authentifier l'utilisateur plutôt que l'adresse IP ?

- A. c'est plus rapide
- B. la règle suit la personne, pas le poste
- C. l'IP n'existe plus
- D. c'est obligatoire

<details markdown="1"><summary>Voir la réponse</summary>

**B.** la règle suit la personne, pas le poste — On trace qui fait quoi.

</details>

**Q23.** Quelle méthode évite à l'utilisateur de ressaisir son mot de passe sur un poste du domaine ?

- A. portail captif
- B. SSO (Kerberos/SPNEGO)
- C. RADIUS seul
- D. aucune

<details markdown="1"><summary>Voir la réponse</summary>

**B.** SSO (Kerberos/SPNEGO) — Single sign-on.

</details>

**Q24.** La page de connexion présentée avant l'accès réseau s'appelle :

- A. portail captif
- B. DMZ
- C. tunnel
- D. profil IPS

<details markdown="1"><summary>Voir la réponse</summary>

**A.** portail captif — Portail captif.

</details>


## S09 – VPN IPsec

**Q25.** La phase 1 d'IPsec sert à :

- A. chiffrer les données applicatives
- B. authentifier les pairs et établir un canal sûr
- C. configurer le NAT
- D. filtrer les URL

<details markdown="1"><summary>Voir la réponse</summary>

**B.** authentifier les pairs et établir un canal sûr — IKE SA.

</details>

**Q26.** Pour un VPN site à site, les deux réseaux doivent :

- A. être identiques
- B. ne pas se chevaucher
- C. être en DMZ
- D. utiliser le même DHCP

<details markdown="1"><summary>Voir la réponse</summary>

**B.** ne pas se chevaucher — Sinon le routage est ambigu.

</details>

**Q27.** Une VTI est :

- A. un type d'attaque
- B. une interface virtuelle représentant le tunnel
- C. un serveur d'annuaire
- D. un profil antivirus

<details markdown="1"><summary>Voir la réponse</summary>

**B.** une interface virtuelle représentant le tunnel — Le trafic y arrive par routage.

</details>


## S10 – VPN SSL

**Q28.** Un télétravailleur isolé utilise plutôt :

- A. un VPN site à site
- B. un VPN nomade (SSL)
- C. un pont
- D. un NAT 1:1

<details markdown="1"><summary>Voir la réponse</summary>

**B.** un VPN nomade (SSL) — Un poste vers un réseau.

</details>

**Q29.** Le VPN SSL traverse facilement les réseaux car il peut utiliser :

- A. le port 21
- B. le port 443
- C. le port 23
- D. aucun port

<details markdown="1"><summary>Voir la réponse</summary>

**B.** le port 443 — Port 443, rarement bloqué.

</details>


## 🏁 Score

*29 questions.* Note ton score et reprends les modules des questions ratées.
