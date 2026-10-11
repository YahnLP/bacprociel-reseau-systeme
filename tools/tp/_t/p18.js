const L=require('../lib');const sim=L.reload('corriges/premiere/P18-panne-corrige.json');const NS=L.NS;
sim.runFor(8000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
for (const n of ['PC-AT2','LAP-INV','PC-DIR']) console.log(n, NS.checker(sim).ipOf(n));
console.log(L.shell(sim,g('PC-AT2'),'dhclient'));console.log(L.shell(sim,g('PC-AT2'),'ip a'));
console.log(L.shell(sim,g('LAP-INV'),'nslookup intranet.archiplus.local'));
console.log(L.shell(sim,g('R1'),'show access-lists'));
