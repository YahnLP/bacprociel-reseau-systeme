const L=require('../lib');
let sim=L.reload('docs/premiere/S10-serveur-linux-ssh/tp/p10-serveur.json');sim.runFor(3000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
console.log(L.shell(sim,g('SRV1'),'ping -c 2 192.168.10.11'));
console.log(L.shell(sim,g('PC1'),'ping 192.168.20.100').split('\n').slice(0,3).join('\n'));
console.log(L.shell(sim,g('PC1'),'tracert 192.168.20.100').split('\n').slice(0,8).join('\n'));
console.log(L.shell(sim,g('SRV1'),'ip route add default via 192.168.20.1'));
console.log(L.shell(sim,g('SRV1'),'ping -c 2 192.168.10.11'));
L.save(sim,'/tmp/x10.json'); 
