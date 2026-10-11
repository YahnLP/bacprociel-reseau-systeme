const L=require('../lib');
let sim=L.reload('corriges/premiere/P14-securite-corrige.json');sim.runFor(4000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
const s=g('SW1').newSession();let out='',done=false;const io={print:t=>out+=t,done:()=>done=true,clear(){}};
['enable','Cisco123','show running-config | begin line'].forEach(l=>{done=false;out='';s.exec(l,io);sim.runUntil(()=>done,60000);if(l.includes('show'))console.log(out.split('\n').filter(x=>/line|password|login|transport|service|secret|username/.test(x)).join('\n'))});
