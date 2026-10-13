const { ios, sh, cfg, runFaults } = require('./pannes_lib');
const K = 'corriges/ccna/';
const ping = (n, ip) => sim => sh(sim, n, 'ping -c 2 ' + ip).split('\n').slice(-3).join('\n');
const F = [
 { id: 'c202-natif', desc: 'VLAN natif différent entre les deux bouts du trunk', file: K + 'C202-trunk-corrige.json',
   inject: s => cfg(s, 'SW2', 'interface fa0/24\nswitchport trunk native vlan 1'),
   fix: s => cfg(s, 'SW2', 'interface fa0/24\nswitchport trunk native vlan 99'),
   probes: [['ping PC10A→PC10B', ping('PC10A', '192.168.10.11')], ['SW1 show interfaces trunk', s => ios(s, 'SW1', 'show interfaces trunk')], ['SW2 show interfaces trunk', s => ios(s, 'SW2', 'show interfaces trunk')]] },
 { id: 'c202-allowed', desc: 'VLAN 20 retiré de la liste autorisée du trunk (SW1)', file: K + 'C202-trunk-corrige.json',
   inject: s => cfg(s, 'SW1', 'interface fa0/24\nswitchport trunk allowed vlan 10,99'),
   fix: s => cfg(s, 'SW1', 'interface fa0/24\nswitchport trunk allowed vlan 10,20,99'),
   probes: [['ping PC20A→PC20B', ping('PC20A', '192.168.20.11')], ['ping PC10A→PC10B', ping('PC10A', '192.168.10.11')], ['SW1 show interfaces trunk', s => ios(s, 'SW1', 'show interfaces trunk')]] },
 { id: 'c202-encap', desc: 'sous-interface du routeur avec la mauvaise encapsulation', file: K + 'C202-trunk-corrige.json',
   inject: s => cfg(s, 'R1', 'interface gi0/0.20\nencapsulation dot1Q 30'),
   fix: s => cfg(s, 'R1', 'interface gi0/0.20\nencapsulation dot1Q 20'),
   probes: [['ping PC10A→PC20B', ping('PC10A', '192.168.20.11')], ['ping PC20A→PC20B (même VLAN)', ping('PC20A', '192.168.20.11')], ['R1 show ip interface brief', s => ios(s, 'R1', 'show ip interface brief')], ['R1 show running-config interface gi0/0.20', s => ios(s, 'R1', 'show running-config interface gi0/0.20')]] },
 { id: 'c202-shut', desc: 'interface physique du routeur coupée', file: K + 'C202-trunk-corrige.json',
   inject: s => cfg(s, 'R1', 'interface gi0/0\nshutdown'),
   fix: s => cfg(s, 'R1', 'interface gi0/0\nno shutdown'),
   probes: [['ping PC10A→PC20B', ping('PC10A', '192.168.20.11')], ['R1 show ip interface brief', s => ios(s, 'R1', 'show ip interface brief')]] },
 { id: 'c202-vlan', desc: 'un poste dans le mauvais VLAN', file: K + 'C202-trunk-corrige.json',
   inject: s => cfg(s, 'SW1', 'interface fa0/1\nswitchport access vlan 20'),
   fix: s => cfg(s, 'SW1', 'interface fa0/1\nswitchport access vlan 10'),
   probes: [['ping PC10A→PC10B', ping('PC10A', '192.168.10.11')], ['SW1 show vlan brief', s => ios(s, 'SW1', 'show vlan brief')]] },
];
runFaults(F, process.argv.slice(2));
