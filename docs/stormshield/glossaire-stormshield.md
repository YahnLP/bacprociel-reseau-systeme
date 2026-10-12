# 📖 Glossaire – Parcours Stormshield

| Français | Anglais | Définition simple | Module |
|---|---|---|---|
| Pare-feu | *firewall* | Équipement qui autorise ou bloque les flux entre réseaux | S01 |
| Stormshield Network Security | *SNS* | Système des pare-feux Stormshield | S01 |
| Image virtuelle Stormshield | *EVA (Elastic Virtual Appliance)* | Le pare-feu sous forme de machine virtuelle | S01 |
| Journal | *log* | Trace des flux, alarmes et événements | S02 |
| Objet | *object* | Nom donné à une adresse, un réseau, un service… réutilisable dans les règles | S03 |
| Zone | *zone* | Groupe d'interfaces de même confiance (LAN, WAN, DMZ) | S04 |
| Zone démilitarisée | *DMZ* | Réseau des serveurs exposés | S04 |
| Passerelle par défaut | *default gateway* | Routeur vers Internet | S04 |
| Translation d'adresses | *NAT* | Remplace les adresses dans les paquets | S05 |
| Translation de source (masquerade) | *source NAT / masquerade* | Les postes sortent avec l'adresse du pare-feu | S05 |
| Redirection | *destination NAT / port forwarding* | Publie un serveur interne | S05 |
| Règle de filtrage | *filter rule* | Autorise ou bloque selon source, destination, service | S06 |
| Filtrage à états | *stateful inspection* | Le retour d'une connexion autorisée passe tout seul | S06 |
| Politique par défaut | *default policy (block all)* | Tout ce qui n'est pas autorisé est bloqué | S06 |
| Filtrage d'URL | *URL filtering* | Autorise ou bloque des sites par catégorie | S07 |
| Antivirus | *antivirus* | Analyse les fichiers transférés | S07 |
| Bac à sable | *sandbox* | Exécution isolée d'un fichier suspect | S07 |
| Prévention d'intrusion | *IPS / IDS* | Bloque (IPS) ou signale (IDS) les attaques | S07 |
| Annuaire | *directory (LDAP, Active Directory)* | Base des utilisateurs | S08 |
| Portail captif | *captive portal* | Page de connexion avant l'accès | S08 |
| Authentification unique | *SSO* | Pas de mot de passe à retaper | S08 |
| Échange de clés Internet | *IKE (IKEv1, IKEv2)* | Négociation d'un VPN IPsec | S09 |
| Clé pré-partagée | *PSK* | Secret commun aux deux pare-feux | S09 |
| Interface de tunnel virtuelle | *VTI* | Interface représentant le tunnel IPsec | S09 |
| VPN nomade | *remote access VPN* | Relie un poste à l'entreprise | S10 |
