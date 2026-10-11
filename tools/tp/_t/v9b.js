const L=require('../lib');const {Sim,mk,cliRun,hostIp,shell}=L;
const sim=new Sim();const h=mk(sim);const {dev,link,get}=h;
dev('sw-2960','SW1',300,180);dev('sw-2960','SW2',600,180);
dev('pc-win','PC1',100,80);dev('pc-win','PC2',100,280);dev('pc-win','PC3',800,80);dev('pc-win','PC4',800,280);
link('PC1','eth0','SW1','Fa0/1');link('PC2','eth0','SW1','Fa0/2');link('PC3','eth0','SW2','Fa0/1');link('PC4','eth0','SW2','Fa0/2');link('SW1','Gi0/1','SW2','Gi0/1');
['PC1','PC3'].forEach((n,k)=>hostIp(get(n),'192.168.10.'+(11+k),'24'));['PC2','PC4'].forEach((n,k)=>hostIp(get(n),'192.168.20.'+(12+k),'24'));
const V='enable\nconf t\nvlan 10\nname DIRECTION\nvlan 20\nname ATELIER\ninterface fa0/1\nswitchport mode access\nswitchport access vlan 10\ninterface fa0/2\nswitchport mode access\nswitchport access vlan 20\nend';
cliRun(get('SW1'),V);cliRun(get('SW2'),V);sim.runFor(8000);
console.log(shell(sim,get('PC1'),'ping 192.168.10.12'));
