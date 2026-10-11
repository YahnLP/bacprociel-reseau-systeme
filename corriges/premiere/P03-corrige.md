# Corrigé P03 – Les couches

## Mise en place (valeurs du fichier fourni)
PC1 `00:14:22:00:00:0b` · PC2 `00:14:22:00:00:0d` · R1 Gi0/0 `00:00:0c:00:00:0f` · R1 Gi0/1 `00:00:0c:00:00:10` · SRV2 `00:14:22:00:00:12`
(si les MAC diffèrent légèrement, c'est la logique qui compte).

## Partie A (ping PC1 → PC2)
MAC src PC1, MAC dst PC2 ; type 0x0800 ; IP 192.168.10.11 → 192.168.10.12 ; TTL 128 ; protocole ICMP (1) ; ICMP type 8.
Pourquoi MAC dst = PC2 : même réseau, pas de passerelle.

## Partie B (ARP)
1) PC1 → Broadcast : « Who has 192.168.10.12? Tell 192.168.10.11 » ; 2) PC2 → PC1 : « 192.168.10.12 is at … ». `arp -a` : ligne 192.168.10.12 ajoutée. La 1re en diffusion car la MAC est inconnue.

## Partie C
| Champ | Segment 1 | Segment 2 | Change |
|---|---|---|---|
| MAC source | PC1 | R1 Gi0/1 | oui |
| MAC destination | R1 Gi0/0 | SRV2 | oui |
| IP source | 192.168.10.11 | 192.168.10.11 | non |
| IP destination | 192.168.20.100 | 192.168.20.100 | non |
| TTL | 128 | 127 | oui (−1 par R1) |

## Partie D
FF:FF… = ARP (couche 2/3, ARP lié à Ethernet) ; TTL 64 = Linux (ou équipement) ; oui, le switch lit la MAC ; ARP : liaison (couche 2) ; ICMP : réseau (couche 3). Routeur HS : A fonctionne (même réseau), C échoue.

## QCM : 1 b · 2 c · 3 b · 4 c · 5 b · 6 b · 7 c · 8 b
