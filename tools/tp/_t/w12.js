const L=require('../lib');
let sim=L.reload('docs/premiere/S12-web-partage/tp/p12-web.json');sim.runFor(4000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
console.log(L.shell(sim,g('PC1'),'curl http://intranet.mecapro.local'));
console.log(L.shell(sim,g('PC1'),'ping intranet.mecapro.local').split('\n').slice(0,3).join('\n'));
sim=L.reload('corriges/premiere/P12-web-corrige.json');sim.runFor(4000);
console.log(L.shell(sim,g('PC1'),'curl http://intranet.mecapro.local'));
console.log(L.shell(sim,g('PC1'),'curl https://intranet.mecapro.local'));
console.log(L.shell(sim,g('PC1'),'curl http://intranet.mecapro.local/absente.html'));
