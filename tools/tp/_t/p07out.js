const L=require('../lib');const path='corriges/premiere/P07-routage-corrige.json';
const sim=L.reload(path);sim.runFor(5000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
const rs=(n,cmds)=>{const d=g(n);const s=d.newSession();let out='',done=false;const io={print:t=>out+=t,done:()=>done=true,clear(){}};cmds.forEach(c=>{done=false;out='';s.exec(c,io);sim.runUntil(()=>done,60000);console.log('>',c);console.log(out)})};
rs('R1',['enable','show ip interface brief','show ip route','ping 10.0.0.2']);
console.log(L.shell(sim,g('PC1'),'tracert 192.168.20.100'));
console.log(L.shell(sim,g('PC1'),'ping 192.168.20.100'));
console.log(L.shell(sim,g('PC1'),'route print'));
