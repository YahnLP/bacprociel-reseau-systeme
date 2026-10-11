const L=require('../lib');const {Sim,mk,cliRun,hostIp,shell}=L;
const sim=new Sim();const h=mk(sim);const {dev,link,get}=h;
dev('sw-8p','SW1',300,100);dev('pc-win','PC1',100,100);dev('srv-linux','SRV1',500,100);
link('PC1','eth0','SW1','port1');link('SRV1','ens33','SW1','port2');
hostIp(get('PC1'),'192.168.10.11','24','192.168.10.1');hostIp(get('SRV1'),'192.168.10.100','24');sim.runFor(3000);
const s=get('SRV1').newSession();let out='',done=false;const io={print:t=>out+=t,done:()=>done=true,clear(){}};
const go=l=>{done=false;out='';const r=s.exec(l,io);sim.runUntil(()=>done||r!=='async',30000);console.log('>',l);console.log(out)};
['ip r','ping -c 2 8.8.8.8','ip route add default via 192.168.10.1','ip r','ip route add 10.0.0.0/8 via 192.168.10.1','ip r','ip route del default','ip r','ss -tln','ip -br a','ip link show'].forEach(go);
