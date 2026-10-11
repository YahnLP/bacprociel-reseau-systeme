const L=require('../lib');
let sim=L.reload('corriges/premiere/P11-dhcp-dns-corrige.json');sim.runFor(12000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
console.log(L.shell(sim,g('PC1'),'ping inconnu.mecapro.local'));console.log(L.shell(sim,g('PC1'),'nslookup inconnu.mecapro.local'));
console.log(L.shell(sim,g('PC1'),'ipconfig /renew').slice(0,200));
