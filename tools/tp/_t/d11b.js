const L=require('../lib');
let sim=L.reload('docs/premiere/S11-dhcp-dns-serveur/tp/p11-dhcp-dns-panne.json');sim.runFor(12000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
console.log(L.shell(sim,g('PC1'),'ipconfig /all').split('\n').filter(l=>/IPv4|DNS|Serveur/.test(l)).join('\n'));
console.log(L.shell(sim,g('PC1'),'nslookup intranet.mecapro.local'));
const s=g('SRV1');s.dhcpd.pools[0].dns=[L.IP.parse('192.168.10.2')];
console.log(L.shell(sim,g('PC1'),'ipconfig /renew').slice(0,300));sim.runFor(5000);
console.log(L.shell(sim,g('PC1'),'ipconfig /all').split('\n').filter(l=>/IPv4|DNS|Serveur/.test(l)).join('\n'));
console.log(L.shell(sim,g('PC1'),'nslookup intranet.mecapro.local'));
