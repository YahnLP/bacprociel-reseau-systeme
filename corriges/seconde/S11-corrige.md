# Corrigé S11 – Adressage (enseignant)

**A.** 1 = 00000001 ; 12 = 00001100 (8+4) ; 13 = 00001101 (8+4+1) ; 168 = 10101000 (128+32+8) ; 255 = 11111111.

**B.** PC1 192.168.1.11 ; PC2 192.168.1.12 ; PC3 192.168.1.13 ; masque 255.255.255.0.

**C1.** « PING : échec général. » (pas d'IP). **C3.** 6 ✅. **C4.** Autre réseau : « échec général » ; masque /25 côté PC2 (255.255.255.128) : PC2 .12 reste dans la même moitié que PC1 .11 → le ping passe encore ; à discuter (le masque n'est faux que si l'on compare avec une machine > .127).

**E.** PC2 192.168.11.12 : hors réseau (« échec général »). PC3 192.168.1.200/25 : mauvais masque, hors du sous-réseau 0–127 de PC1 (« Délai d'attente » ou échec). PC4 192.168.1.11 : doublon de PC1. Corrections : PC2 .12, PC3 .13 /24, PC4 .14.
Fichiers solutions : S11-adressage-corrige.json, S11-erreurs-corrige.json.
