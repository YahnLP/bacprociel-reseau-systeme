const L=require('../lib');
let sim=L.reload('docs/premiere/S14-securite-base/tp/p14-securite.json');sim.runFor(4000);const g=n=>Array.from(sim.devices.values()).find(d=>d.name===n);
const s=g('SW1').newSession();let out='',done=false;const io={print:t=>out+=t,done:()=>done=true,clear(){}};
['enable','cisco','show running-config','show startup-config'].forEach(l=>{done=false;out='';s.exec(l,io);sim.runUntil(()=>done,60000);console.log('>',l,'\n'+out)});
