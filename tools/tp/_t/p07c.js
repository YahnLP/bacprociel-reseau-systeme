const L=require('../lib');
const sim=L.reload('corriges/premiere/P07-routage-corrige.json');sim.runFor(3000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
L.cliRun(g('R1'),'enable\nconf t\nno ip route 192.168.20.0 255.255.255.0 10.0.0.2\nip route 0.0.0.0 0.0.0.0 10.0.0.2\nend');
const d=g('R1');const s=d.newSession();let out='',done=false;const io={print:t=>out+=t,done:()=>done=true,clear(){}};
['enable','show ip route','show running-config'].forEach(c=>{done=false;out='';s.exec(c,io);sim.runUntil(()=>done,60000);console.log('>',c);console.log(out)});
console.log(L.shell(sim,g('PC1'),'ping 192.168.20.100'));
