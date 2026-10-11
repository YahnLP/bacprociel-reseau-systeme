# Corrigé S13 – DNS et accès à Internet (enseignant)

**A.** DNS de PC1 : 192.168.1.1 ; nslookup : serveur 192.168.1.1, www.exemple.fr → 198.51.100.80 ; ping : [198.51.100.80].
**B.** PC2 : ping box OK ; ping 198.51.100.80 OK ; ping nom : « La requête Ping n'a pas pu trouver l'hôte… ». DNS de PC2 = 198.51.100.99 (aucun serveur). Réparation : DNS 192.168.1.1 ou DHCP. Corrigé : S13-dns-corrige.json.
**C.** 1 = 192.168.1.1 (box) ; 2 = équipement qui ne répond pas (« * ») ; 3 = 198.51.100.80 (serveur).
**D.** Inside local 192.168.1.x → Inside global 203.0.113.2 pour toutes les lignes.
**E.** Selon le réseau : plusieurs sauts, serveur DNS de l'établissement.
**QCM :** Q1 b · Q2 b · Q3 b · Q4 a · Q5 b · Q6 a. Diagnostic : ping box → ping adresse Internet → ping nom ; si le 1 réussit et le 2 échoue : passerelle (ou box sans accès FAI).
