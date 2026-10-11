const L=require('../lib');
let sim=L.reload('docs/premiere/S12-web-partage/tp/p12-web.json');sim.runFor(4000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
g('SRV1').httpd.start();console.log(L.shell(sim,g('PC1'),'curl http://intranet.mecapro.local').slice(0,300));console.log(Object.keys(g('SRV1').httpd.pages));
