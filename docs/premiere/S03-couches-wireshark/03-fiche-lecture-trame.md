# 📝 Fiche de lecture d'une trame + QCM

## Aide-mémoire (à garder)

| Je cherche… | Je regarde… | Dans l'analyseur |
|---|---|---|
| Qui parle à qui, **sur le câble** ? | **MAC** source / destination | *Ethernet II* |
| Qui parle à qui, **de bout en bout** ? | **IP** source / destination | *Internet Protocol* |
| Combien de routeurs restent ? | **TTL** | *Internet Protocol* |
| Quel protocole du dessus ? | **Type** (Ethernet) ou **Protocol** (IP) | `0x0800` = IPv4 · `0x0806` = ARP · `1` = ICMP · `6` = TCP · `17` = UDP |
| Une demande ou une réponse de ping ? | **Type ICMP** | `8` = demande · `0` = réponse |
| Une question « qui a… ? » | ARP en **diffusion** | `ff:ff:ff:ff:ff:ff` |

## QCM final (8 questions)

**1.** Quelle couche utilise les adresses **MAC** ? a) physique · b) **liaison** · c) réseau

**2.** Quel équipement lit **l'adresse IP** pour choisir un chemin ? a) hub · b) switch · c) **routeur**

**3.** ARP sert à… a) donner une IP · b) **trouver une MAC à partir d'une IP** · c) traduire un nom

**4.** Au passage d'un routeur, quelle information **ne change pas** ? a) MAC source · b) MAC destination · c) **IP source**

**5.** Un paquet a un TTL de 1 quand il arrive sur un routeur. Que se passe-t-il ? a) il passe avec TTL 0 · b) **il est détruit** · c) il est doublé

**6.** Une trame est en **diffusion** quand sa MAC destination est… a) `00:00:00:00:00:00` · b) `ff:ff:ff:ff:ff:ff` · c) celle du routeur

**7.** Un `ping` utilise… a) TCP · b) UDP · c) **ICMP**

**8.** Une trame Ethernet contient un paquet IPv4 si le champ *Type* vaut… a) `0x0806` · b) **`0x0800`** · c) `0x86dd`

<details markdown="1"><summary>Correction</summary>

1 b · 2 c · 3 b · 4 c · 5 b · 6 b · 7 c · 8 b

</details>
