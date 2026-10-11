const L=require('../lib');const sim=L.reload('docs/premiere/S18-projet-3-recette/tp/p18-panne.json');const NS=L.NS;
sim.runFor(8000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
console.log(NS.checker(sim).ipOf('PC-AT2'));
L.cliRun(g('SW1'),'enable\nconf t\ninterface fa0/10\nswitchport access vlan 20\nend');
for (const c of ['ipconfig /release','ipconfig /renew']) {console.log(L.shell(sim,g('PC-AT2'),c));sim.runFor(5000);}
console.log(NS.checker(sim).ipOf('PC-AT2'));
console.log(L.shell(sim,g('SW1'),'show vlan brief').split('\n').filter(l=>/^(10|20|30)/.test(l)).join('\n'));
console.log(L.shell(sim,g('SW1'),'show mac address-table').split('\n').slice(0,14).join('\n'));
console.log(L.shell(sim,g('SRV'),'cat /var/lib/dhcp/dhcpd.leases'));
