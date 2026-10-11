# 📝 Aide-mémoire – Supervision et tickets

## Switch

```text
snmp-server community supervision RO
snmp-server location Atelier - baie 1
snmp-server contact support@laporte-imprimerie.fr
snmp-server host 192.168.1.5 version 2c supervision
snmp-server enable traps
logging host 192.168.1.5
logging trap informational
```

Vérifier : `show snmp community` · `show logging`.

## Poste de supervision (Linux)

```text
snmpget  -v2c -c supervision <ip> 1.3.6.1.2.1.1.5.0     (nom)
snmpget  -v2c -c supervision <ip> 1.3.6.1.2.1.1.6.0     (emplacement)
snmpwalk -v2c -c supervision <ip> 1.3.6.1.2.1.2.2.1.8   (état des ports : 1 = up, 2 = down)
```

## Gravité des messages

0 urgence · 1 alerte · 2 critique · 3 erreur · 4 avertissement · 5 notification · 6 information · 7 débogage.

## Ticket

Symptôme · Cause · Action · Résultat · Durée.
