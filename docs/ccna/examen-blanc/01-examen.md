# 📝 Examen blanc CCNA

*Parcours CCNA – 43 questions, tous domaines*

> [!EXAMPLE] 🚀 Pour aller plus loin
> Questionnaire d'**entraînement** : à faire **sans cours** ni simulateur. L'examen officiel dure 120 minutes et comporte aussi des simulations ; ici, on teste surtout les **notions**.

> [!TIP]
> Note tes réponses sur une feuille, puis ouvre « Voir la réponse » pour corriger. **≥ 80 %** : tu es au bon niveau. Sinon, relis les modules du domaine raté.


## Domaine 1 – Network Fundamentals

**Q1.** Quel équipement sépare les domaines de broadcast par défaut ?

- A. Switch
- B. Hub
- C. Routeur
- D. Répéteur

<details markdown="1"><summary>Voir la réponse</summary>

**C.** Routeur — Un routeur ne transmet pas les broadcasts ; un switch seul les propage (sauf VLAN).

</details>

**Q2.** Combien d'hôtes utilisables dans un /26 ?

- A. 62
- B. 64
- C. 30
- D. 126

<details markdown="1"><summary>Voir la réponse</summary>

**A.** 62 — 2^6 − 2 = 62.

</details>

**Q3.** Quelle adresse est privée (RFC 1918) ?

- A. 172.32.0.1
- B. 172.20.5.9
- C. 192.169.1.1
- D. 11.0.0.1

<details markdown="1"><summary>Voir la réponse</summary>

**B.** 172.20.5.9 — 172.16.0.0/12 va de 172.16 à 172.31.

</details>

**Q4.** Quel protocole de transport est sans connexion ?

- A. TCP
- B. UDP
- C. SSH
- D. HTTP

<details markdown="1"><summary>Voir la réponse</summary>

**B.** UDP — UDP n'établit pas de connexion.

</details>

**Q5.** Une adresse IPv6 commençant par FE80 est :

- A. globale unicast
- B. link-local
- C. multicast
- D. unique-local

<details markdown="1"><summary>Voir la réponse</summary>

**B.** link-local — FE80::/10 = link-local.

</details>

**Q6.** Quel est l'écriture abrégée de 2001:0db8:0000:0000:0000:0000:0000:0001 ?

- A. 2001:db8::1
- B. 2001:db8:0:1
- C. 2001::db8::1
- D. 2001:db8::0001

<details markdown="1"><summary>Voir la réponse</summary>

**A.** 2001:db8::1 — Un seul « :: » ; zéros de tête supprimés.

</details>

**Q7.** Le duplex se négocie mal : on observe surtout…

- A. des erreurs CRC et collisions tardives
- B. un VLAN natif différent
- C. un changement de racine STP
- D. un ACL refusé

<details markdown="1"><summary>Voir la réponse</summary>

**A.** des erreurs CRC et collisions tardives — Duplex mismatch → collisions tardives, erreurs.

</details>


## Domaine 2 – Network Access

**Q8.** Un switch reçoit une trame de destination MAC inconnue. Il…

- A. la jette
- B. la diffuse sur tous les ports sauf celui d'entrée
- C. la renvoie à l'émetteur
- D. l'envoie au routeur

<details markdown="1"><summary>Voir la réponse</summary>

**B.** la diffuse sur tous les ports sauf celui d'entrée — C'est le flooding (unknown unicast).

</details>

**Q9.** Quel standard définit le trunk avec balise VLAN ?

- A. 802.1Q
- B. 802.3ad
- C. 802.11
- D. 802.1X

<details markdown="1"><summary>Voir la réponse</summary>

**A.** 802.1Q — 802.1Q.

</details>

**Q10.** Sur un trunk 802.1Q, quel trafic n'est pas balisé par défaut ?

- A. VLAN natif
- B. VLAN voix
- C. VLAN 1000
- D. VLAN de gestion obligatoirement

<details markdown="1"><summary>Voir la réponse</summary>

**A.** VLAN natif — Le VLAN natif.

</details>

**Q11.** Quel protocole standard négocie un EtherChannel ?

- A. PAgP
- B. LACP
- C. STP
- D. VTP

<details markdown="1"><summary>Voir la réponse</summary>

**B.** LACP — LACP (802.3ad). PAgP est propriétaire Cisco.

</details>

**Q12.** Qui devient pont racine STP ?

- A. le plus grand Bridge ID
- B. le plus petit Bridge ID (priorité puis MAC)
- C. le switch avec le plus de ports
- D. le plus ancien

<details markdown="1"><summary>Voir la réponse</summary>

**B.** le plus petit Bridge ID (priorité puis MAC) — Plus petit Bridge ID.

</details>

**Q13.** Quelle fonction coupe un port PortFast qui reçoit une BPDU ?

- A. Root guard
- B. BPDU guard
- C. Loop guard
- D. UDLD

<details markdown="1"><summary>Voir la réponse</summary>

**B.** BPDU guard — BPDU guard met le port en err-disabled.

</details>

**Q14.** Mode d'AP où le WLC gère tout via CAPWAP :

- A. Autonome
- B. Lightweight
- C. Bridge
- D. Monitor uniquement

<details markdown="1"><summary>Voir la réponse</summary>

**B.** Lightweight — Lightweight.

</details>


## Domaine 3 – IP Connectivity

**Q15.** Distance administrative d'OSPF ?

- A. 1
- B. 90
- C. 110
- D. 120

<details markdown="1"><summary>Voir la réponse</summary>

**C.** 110 — OSPF = 110 ; statique = 1 ; RIP = 120.

</details>

**Q16.** Deux routes vers 10.1.0.0/16 et 10.1.1.0/24 : pour 10.1.1.5 laquelle est choisie ?

- A. /16
- B. /24
- C. les deux
- D. aucune

<details markdown="1"><summary>Voir la réponse</summary>

**B.** /24 — Plus long préfixe.

</details>

**Q17.** Quelle route statique est « flottante » ?

- A. AD = 1
- B. AD supérieure à celle de la route principale
- C. vers un hôte
- D. sans next-hop

<details markdown="1"><summary>Voir la réponse</summary>

**B.** AD supérieure à celle de la route principale — AD plus élevée = secours.

</details>

**Q18.** Les routeurs OSPF élisent DR/BDR sur :

- A. liens point à point
- B. réseaux broadcast multi-accès
- C. tout type de lien
- D. aucun

<details markdown="1"><summary>Voir la réponse</summary>

**B.** réseaux broadcast multi-accès — Réseaux Ethernet multi-accès.

</details>

**Q19.** Quelle commande affiche les voisins OSPF ?

- A. show ip ospf neighbor
- B. show ospf peers
- C. show ip route ospf
- D. show ip protocols neighbor

<details markdown="1"><summary>Voir la réponse</summary>

**A.** show ip ospf neighbor — show ip ospf neighbor.

</details>

**Q20.** Que désigne « Gateway of last resort » ?

- A. la route par défaut
- B. l'adresse du DNS
- C. le routeur racine
- D. le DR

<details markdown="1"><summary>Voir la réponse</summary>

**A.** la route par défaut — 0.0.0.0/0.

</details>

**Q21.** HSRP sert à :

- A. agréger des liens
- B. fournir une passerelle virtuelle redondante
- C. chiffrer le trafic
- D. filtrer des paquets

<details markdown="1"><summary>Voir la réponse</summary>

**B.** fournir une passerelle virtuelle redondante — FHRP : passerelle virtuelle.

</details>


## Domaine 4 – IP Services

**Q22.** Quel type de NAT permet à de nombreux hôtes de partager une adresse publique ?

- A. NAT statique
- B. PAT (overload)
- C. NAT 1-1
- D. Proxy ARP

<details markdown="1"><summary>Voir la réponse</summary>

**B.** PAT (overload) — PAT utilise les ports.

</details>

**Q23.** Les 4 messages DHCP dans l'ordre :

- A. Discover, Offer, Request, Ack
- B. Request, Offer, Ack, Discover
- C. Offer, Discover, Ack, Request
- D. Discover, Request, Offer, Ack

<details markdown="1"><summary>Voir la réponse</summary>

**A.** Discover, Offer, Request, Ack — DORA.

</details>

**Q24.** Commande pour relayer DHCP vers un serveur distant :

- A. ip dhcp relay
- B. ip helper-address
- C. ip forward-protocol
- D. dhcp server

<details markdown="1"><summary>Voir la réponse</summary>

**B.** ip helper-address — ip helper-address sur l'interface côté clients.

</details>

**Q25.** Gravité syslog 0 correspond à :

- A. Emergency
- B. Debug
- C. Warning
- D. Informational

<details markdown="1"><summary>Voir la réponse</summary>

**A.** Emergency — 0 = Emergency, 7 = Debug.

</details>

**Q26.** Valeur DSCP de la voix (EF) ?

- A. 10
- B. 26
- C. 46
- D. 0

<details markdown="1"><summary>Voir la réponse</summary>

**C.** 46 — EF = 46.

</details>

**Q27.** Quel protocole est sécurisé pour l'accès CLI à distance ?

- A. Telnet
- B. SSH
- C. TFTP
- D. HTTP

<details markdown="1"><summary>Voir la réponse</summary>

**B.** SSH — SSH, TCP 22.

</details>

**Q28.** Port d'écoute standard de DNS ?

- A. 53
- B. 67
- C. 123
- D. 161

<details markdown="1"><summary>Voir la réponse</summary>

**A.** 53 — 53 (UDP/TCP). 67 DHCP, 123 NTP, 161 SNMP.

</details>


## Domaine 5 – Security Fundamentals

**Q29.** Quelle commande stocke un mot de passe enable haché fort ?

- A. enable password
- B. enable secret
- C. service password-encryption
- D. password

<details markdown="1"><summary>Voir la réponse</summary>

**B.** enable secret — enable secret.

</details>

**Q30.** Dans une ACL, l'instruction implicite finale est :

- A. permit any
- B. deny any
- C. log
- D. aucune

<details markdown="1"><summary>Voir la réponse</summary>

**B.** deny any — deny ip any any implicite.

</details>

**Q31.** Où placer une ACL étendue de préférence ?

- A. près de la destination
- B. près de la source
- C. sur le switch d'accès uniquement
- D. n'importe où

<details markdown="1"><summary>Voir la réponse</summary>

**B.** près de la source — Étendue près de la source ; standard près de la destination.

</details>

**Q32.** Wildcard pour 192.168.10.0/24 :

- A. 255.255.255.0
- B. 0.0.0.255
- C. 0.0.0.0
- D. 255.255.255.255

<details markdown="1"><summary>Voir la réponse</summary>

**B.** 0.0.0.255 — Inverse du masque.

</details>

**Q33.** Violation port-security par défaut :

- A. protect
- B. restrict
- C. shutdown
- D. ignore

<details markdown="1"><summary>Voir la réponse</summary>

**C.** shutdown — shutdown (err-disabled).

</details>

**Q34.** Quelle fonction bloque un faux serveur DHCP ?

- A. DHCP snooping
- B. Port-security
- C. BPDU guard
- D. PortFast

<details markdown="1"><summary>Voir la réponse</summary>

**A.** DHCP snooping — DHCP snooping (ports trusted/untrusted).

</details>

**Q35.** IPsec site à site : le mode de tunnel chiffre :

- A. seulement l'en-tête
- B. le paquet IP d'origine entier
- C. seulement l'application
- D. rien

<details markdown="1"><summary>Voir la réponse</summary>

**B.** le paquet IP d'origine entier — En mode tunnel, tout le paquet d'origine est encapsulé.

</details>

**Q36.** Quel est le meilleur choix de sécurité Wi-Fi à domicile/entreprise ?

- A. WEP
- B. WPA
- C. WPA2/WPA3
- D. SSID masqué

<details markdown="1"><summary>Voir la réponse</summary>

**C.** WPA2/WPA3 — WPA2 ou WPA3 (AES).

</details>

**Q37.** AAA signifie :

- A. Authentication, Authorization, Accounting
- B. Access, Admin, Audit
- C. Auth, Alert, Archive
- D. Allow, Accept, Apply

<details markdown="1"><summary>Voir la réponse</summary>

**A.** Authentication, Authorization, Accounting — Authentification, autorisation, traçabilité.

</details>


## Domaine 6 – Automation and Programmability

**Q38.** Quel format est un JSON valide ?

- A. {nom: Yahn}
- B. {"nom": "Yahn"}
- C. [nom=Yahn]
- D. <nom>Yahn</nom>

<details markdown="1"><summary>Voir la réponse</summary>

**B.** {"nom": "Yahn"} — Clés et chaînes entre guillemets doubles.

</details>

**Q39.** Méthode REST pour créer une ressource ?

- A. GET
- B. POST
- C. DELETE
- D. HEAD

<details markdown="1"><summary>Voir la réponse</summary>

**B.** POST — POST = Create.

</details>

**Q40.** Code HTTP « ressource non trouvée » ?

- A. 200
- B. 301
- C. 404
- D. 500

<details markdown="1"><summary>Voir la réponse</summary>

**C.** 404 — 404.

</details>

**Q41.** Ansible est…

- A. avec agent, en pull
- B. sans agent, en push via SSH
- C. un langage de programmation compilé
- D. un protocole de routage

<details markdown="1"><summary>Voir la réponse</summary>

**B.** sans agent, en push via SSH — Agentless, YAML, SSH.

</details>

**Q42.** Terraform sert surtout à :

- A. gérer la configuration des logiciels sur serveurs
- B. décrire et créer l'infrastructure (IaC)
- C. chiffrer des liens
- D. supervision SNMP

<details markdown="1"><summary>Voir la réponse</summary>

**B.** décrire et créer l'infrastructure (IaC) — Infrastructure as Code déclarative.

</details>

**Q43.** Dans une architecture SDN, le plan de contrôle est…

- A. distribué dans chaque équipement uniquement
- B. centralisé dans un contrôleur
- C. supprimé
- D. dans le câble

<details markdown="1"><summary>Voir la réponse</summary>

**B.** centralisé dans un contrôleur — Contrôleur centralisé (northbound/southbound API).

</details>


## 🏁 Score

*43 questions.* Bilan par domaine : note tes erreurs et reprends les modules concernés. Ensuite, refais les TP **sans regarder** les cours.
