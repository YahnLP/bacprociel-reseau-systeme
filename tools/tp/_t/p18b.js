const L=require('../lib');const sim=L.reload('corriges/premiere/P18-panne-corrige.json');const NS=L.NS;
sim.runFor(8000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
for (const cmd of ['dhclient -r','dhclient','ip a']) {console.log('>',cmd);console.log(L.shell(sim,g('PC-AT2'),cmd).split('\n').filter(l=>/inet 1|dhcp|DHCP/i.test(l)).join('\n'));sim.runFor(5000)}
console.log(L.shell(sim,g('R1'),'enable\nconfigure terminal\nip access-list extended INVITES-IN\nno 40\nno 50\nend'));
L.cliRun(g('R1'),'enable\nconf t\nip access-list extended INVITES-IN\nno 50\nno 40\n25 permit udp 192.168.50.64 0.0.0.63 host 192.168.50.34 eq 53\nend');
console.log(L.shell(sim,g('R1'),'show access-lists'));
