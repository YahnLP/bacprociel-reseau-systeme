# Corrigé S12 – DHCP, box, passerelle (enseignant)

**A.** PC1, PC3, PC4 : DHCP activé « Oui », 192.168.1.x / 255.255.255.0, passerelle 192.168.1.1, serveur DHCP 192.168.1.1 (les x dépendent de l'ordre : .10, .11, .12…). **PC2 : DHCP « Non »**, 192.168.1.50 /24, **passerelle vide**.
**B.** `release` → adresse vide ; ping box : « PING : échec général. » ; `renew` → adresse réattribuée (souvent la même).
**C.** PC2 → PC1 : réponse ; PC2 → box : réponse ; PC2 → 203.0.113.1 : « échec général ». Cause : passerelle vide. Réparations : passerelle 192.168.1.1 (et DNS 192.168.1.1) ou DHCP. Corrigé : S12-dhcp-box-corrige.json.
**D.** Box sans DHCP : PC4 en 169.254.x.x / 255.255.0.0, pas de passerelle ; ping box et site : échec. Réactivation : adresse 192.168.1.x de nouveau.
**E.** Exemples : imprimante .150, NAS .151, bornes .152 et .153 (hors .20–.120) ; .50 est dans la plage → doublon possible.
**Remarque simulateur :** changer la plage DHCP sans éteindre les baux ne change pas l'adresse d'un poste qui fait `renew` ; la fenêtre BOX n'a ni mot de passe ni réservation.
