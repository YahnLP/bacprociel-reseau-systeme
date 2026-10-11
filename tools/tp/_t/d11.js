const L=require('../lib');
let sim=L.reload('docs/premiere/S11-dhcp-dns-serveur/tp/p11-dhcp-dns.json');sim.runFor(5000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
console.log(L.shell(sim,g('PC1'),'ipconfig'));
console.log(L.shell(sim,g('PC1'),'ping 192.168.10.1').split('\n').slice(0,3).join('\n'));
sim=L.reload('corriges/premiere/P11-dhcp-dns-corrige.json');sim.runFor(12000);
console.log(L.shell(sim,g('PC1'),'ipconfig /all'));
console.log(L.shell(sim,g('PC1'),'nslookup intranet.mecapro.local'));
console.log(L.shell(sim,g('PC3'),'ip -br a; ip r'));
console.log(L.shell(sim,g('PC1'),'ping imprimante.mecapro.local').split('\n').slice(0,3).join('\n'));
