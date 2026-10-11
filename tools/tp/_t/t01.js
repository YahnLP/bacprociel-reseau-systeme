const L=require('../lib');const sim=L.reload('corriges/terminale/T01-mini-chantier-corrige.json');sim.runFor(5000);
const sw=Array.from(sim.devices.values()).find(d=>d.name==='SW1');
for (const pw of ['Cabinet#2026','Cabinet']) {const s=sw.newSession();let out='',done=false;const io={print:t=>{out+=t},done:()=>{done=true},clear(){}};
const go=l=>{done=false;out='';s.exec(l,io);sim.runUntil(()=>done,60000)};go('enable');console.log('after enable:',JSON.stringify(out));go(pw);console.log('after pw:',JSON.stringify(out));go('show running-config');console.log(out.slice(0,300));}
