const L=require('../lib');
const sim=L.reload('docs/premiere/S07-routeur-routage-statique/tp/p07-routage.json');const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
const R='enable\nconfigure terminal\n';
L.cliRun(g('R1'),R+'interface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 10.0.0.1 255.255.255.252\nno shutdown\nend');
L.cliRun(g('R2'),R+'interface gi0/0\nip address 192.168.20.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 10.0.0.2 255.255.255.252\nno shutdown\nend');
sim.runFor(5000);
console.log('--- sans route'); console.log(L.shell(sim,g('PC1'),'ping 192.168.20.100'));
L.cliRun(g('R1'),R+'ip route 192.168.20.0 255.255.255.0 10.0.0.2\nend');
console.log('--- route aller seule'); console.log(L.shell(sim,g('PC1'),'ping 192.168.20.100'));console.log(L.shell(sim,g('PC1'),'tracert 192.168.20.100'));
