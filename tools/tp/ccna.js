/* TP du simulateur – parcours CCNA. Lancer : SIM_DIR=… node tools/tp/ccna.js [id ...]
   Départ : docs/ccna/<module>/tp/*.json ; corrigé : corriges/ccna/*.json (local). */
const L = require('./lib');
const { hostIp, cliRun, shell, IP } = L;
const D = 'docs/ccna/', K = 'corriges/ccna/';
const TPS = [];
const dv = (c, n) => Array.from(c.sim.devices.values()).find(d => d.name === n);
const ios = (c, n, cmd) => { const d = dv(c, n); const s = d.newSession(); let out = '', done = false; const io = { print: t => { out += t; }, done: () => { done = true; }, clear() { } };
  const go = l => { done = false; s.exec(l, io); c.sim.runUntil(() => done, 60000); }; go('enable'); out = ''; go(cmd); return out; };
const sh = (c, n, cmd) => shell(c.sim, dv(c, n), cmd);
const cfg = (c, n) => ios(c, n, 'show running-config');
const pc = (h, name, x, y, label, model) => h.dev(model || 'pc-linux', name, x, y, label);
const PCIF = 'ens33';
const lab = TPS.push.bind(TPS);

/* ---------- 1-01 : explorer une architecture à 3 niveaux (lecture seule) ---------- */
function t101Build(sim, h) {
  const { dev, link, get } = h;
  dev('r-2911', 'ROUTEUR-EDGE', 400, 20, 'Sortie vers le FAI'); dev('sw-3560', 'CORE1', 250, 120, 'Coeur 1'); dev('sw-3560', 'CORE2', 550, 120, 'Coeur 2');
  dev('sw-2960', 'DIST1', 120, 240, 'Distribution 1'); dev('sw-2960', 'DIST2', 680, 240, 'Distribution 2');
  dev('sw-2960', 'ACC-A', 40, 360, 'Accès bât. A'); dev('sw-2960', 'ACC-B', 220, 360, 'Accès bât. A'); dev('sw-2960', 'ACC-C', 580, 360, 'Accès bât. B'); dev('sw-2960', 'ACC-D', 760, 360, 'Accès bât. B');
  pc(h, 'PC-A1', 40, 470); pc(h, 'PC-B1', 220, 470); pc(h, 'PC-C1', 580, 470); pc(h, 'PC-D1', 760, 470);
  link('ROUTEUR-EDGE', 'gi0/0', 'CORE1', 'Gi0/1'); link('ROUTEUR-EDGE', 'gi0/1', 'CORE2', 'Gi0/1'); link('CORE1', 'Gi0/2', 'CORE2', 'Gi0/2');
  link('CORE1', 'Fa0/1', 'DIST1', 'Gi0/1'); link('CORE2', 'Fa0/1', 'DIST2', 'Gi0/1'); link('CORE1', 'Fa0/2', 'DIST2', 'Gi0/2'); link('CORE2', 'Fa0/2', 'DIST1', 'Gi0/2');
  link('DIST1', 'Fa0/1', 'ACC-A', 'Fa0/24'); link('DIST1', 'Fa0/2', 'ACC-B', 'Fa0/24'); link('DIST2', 'Fa0/1', 'ACC-C', 'Fa0/24'); link('DIST2', 'Fa0/2', 'ACC-D', 'Fa0/24');
  link('PC-A1', PCIF, 'ACC-A', 'Fa0/1'); link('PC-B1', PCIF, 'ACC-B', 'Fa0/1'); link('PC-C1', PCIF, 'ACC-C', 'Fa0/1'); link('PC-D1', PCIF, 'ACC-D', 'Fa0/1');
  ['CORE1', 'CORE2', 'DIST1', 'DIST2', 'ACC-A', 'ACC-B', 'ACC-C', 'ACC-D'].forEach(n => cliRun(get(n), 'enable\nconf t\nhostname ' + n + '\nend'));
  ['ROUTEUR-EDGE'].forEach(n => cliRun(get(n), 'enable\nconf t\nhostname ' + n + '\nend'));
}
lab({ id: 'c101-architecture', start: D + '1-01-equipements-architectures/tp/c101-architecture.json',
  notes: 'CCNA 1-01 – Réseau d\'entreprise à trois niveaux (accès, distribution, cœur). Exploration en lecture seule : show cdp neighbors, show interfaces status.',
  build: (sim, h) => t101Build(sim, h), checks: [], startShould: [] });

/* ---------- 1-04 : VLSM (192.168.50.0/24) ---------- */
function vlsmBuild(h) {
  const { dev, link } = h;
  dev('r-2911', 'R1', 300, 120); dev('r-2911', 'R2', 600, 120); dev('sw-2960', 'SW-A', 150, 220); dev('sw-2960', 'SW-B', 750, 220);
  pc(h, 'PC-A', 60, 330, 'Service A (≈ 50 postes)'); pc(h, 'PC-B', 840, 330, 'Service B (≈ 25 postes)');
  link('PC-A', PCIF, 'SW-A', 'Fa0/1'); link('SW-A', 'Fa0/24', 'R1', 'gi0/0'); link('R1', 'gi0/1', 'R2', 'gi0/1'); link('R2', 'gi0/0', 'SW-B', 'Fa0/24'); link('PC-B', PCIF, 'SW-B', 'Fa0/1');
}
const vlsmChecks = [
  { label: 'PC-A a une adresse du réseau 192.168.50.0/26', run: c => /192\.168\.50\.(?:[1-9]|[1-5]\d|6[0-2])\b/.test(sh(c, 'PC-A', 'ip -4 addr')) && /\/26/.test(sh(c, 'PC-A', 'ip -4 addr')) },
  { label: 'PC-B a une adresse du réseau 192.168.50.64/27', run: c => /192\.168\.50\.(?:6[5-9]|[7-8]\d|9[0-4])\/27/.test(sh(c, 'PC-B', 'ip -4 addr')) },
  { label: 'R1 joint R2 sur le lien /30 (192.168.50.194)', run: c => /!!!|Success rate is [1-9]/.test(ios(c, 'R1', 'ping 192.168.50.194')) },
  { label: 'PC-A joint PC-B', run: c => { const ip = (sh(c, 'PC-B', 'ip -4 addr').match(/inet (192\.168\.50\.\d+)/) || [])[1]; return !!ip && /bytes from/.test(sh(c, 'PC-A', 'ping -c 2 ' + ip)); } },
];
function vlsmSolve(sim, h) {
  const { get } = h;
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\ninterface gi0/0\nip address 192.168.50.1 255.255.255.192\nno shutdown\nexit\ninterface gi0/1\nip address 192.168.50.193 255.255.255.252\nno shutdown\nexit\nip route 192.168.50.64 255.255.255.224 192.168.50.194\nend\nwrite memory');
  cliRun(get('R2'), 'enable\nconf t\nhostname R2\ninterface gi0/0\nip address 192.168.50.65 255.255.255.224\nno shutdown\nexit\ninterface gi0/1\nip address 192.168.50.194 255.255.255.252\nno shutdown\nexit\nip route 192.168.50.0 255.255.255.192 192.168.50.193\nend\nwrite memory');
  hostIp(get('PC-A'), '192.168.50.10', '26', '192.168.50.1'); hostIp(get('PC-B'), '192.168.50.70', '27', '192.168.50.65');
}
lab({ id: 'c104-vlsm', start: D + '1-04-ipv4-vlsm/tp/c104-vlsm.json', solution: K + 'C104-vlsm-corrige.json',
  notes: 'CCNA 1-04 – VLSM : 192.168.50.0/24 à découper pour un service de 50 postes, un service de 25 postes et un lien routeur à routeur. Matériel câblé, rien n\'est configuré.',
  build: (sim, h) => vlsmBuild(h), solve: vlsmSolve, checks: vlsmChecks, startShould: vlsmChecks.map(x => x.label) });

/* ---------- 1-05 : IPv6 ---------- */
function v6Build(h) {
  const { dev, link } = h;
  dev('r-2911', 'R1', 300, 120); dev('r-2911', 'R2', 600, 120); pc(h, 'PC1', 100, 220); pc(h, 'PC2', 800, 220);
  link('PC1', PCIF, 'R1', 'gi0/0'); link('R1', 'gi0/1', 'R2', 'gi0/1'); link('R2', 'gi0/0', 'PC2', PCIF);
}
const v6Checks = [
  { label: 'R1 a l\'adresse 2001:db8:acad:1::1 sur gi0/0', run: c => /2001:DB8:ACAD:1::1/i.test(ios(c, 'R1', 'show ipv6 interface brief')) },
  { label: 'R1 joint R2 en IPv6 (2001:db8:acad:12::2)', run: c => /!!|Success rate is [1-9]/.test(ios(c, 'R1', 'ping 2001:db8:acad:12::2')) },
  { label: 'R1 possède une route statique IPv6 vers le réseau de PC2', run: c => /ipv6 route 2001:DB8:ACAD:2::\/64/i.test(cfg(c, 'R1')) },
  { label: 'PC1 joint PC2 en IPv6', run: c => /bytes from|64 bytes/.test(sh(c, 'PC1', 'ping -6 -c 2 2001:db8:acad:2::10')) },
];
function v6Solve(sim, h) {
  const { get } = h;
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\nipv6 unicast-routing\ninterface gi0/0\nipv6 address 2001:db8:acad:1::1/64\nno shutdown\nexit\ninterface gi0/1\nipv6 address 2001:db8:acad:12::1/64\nno shutdown\nexit\nipv6 route 2001:db8:acad:2::/64 2001:db8:acad:12::2\nend\nwrite memory');
  cliRun(get('R2'), 'enable\nconf t\nhostname R2\nipv6 unicast-routing\ninterface gi0/0\nipv6 address 2001:db8:acad:2::1/64\nno shutdown\nexit\ninterface gi0/1\nipv6 address 2001:db8:acad:12::2/64\nno shutdown\nexit\nipv6 route 2001:db8:acad:1::/64 2001:db8:acad:12::1\nend\nwrite memory');
  shell(sim, get('PC1'), 'ip -6 addr add 2001:db8:acad:1::10/64 dev ens33'); shell(sim, get('PC1'), 'ip -6 route add default via 2001:db8:acad:1::1');
  shell(sim, get('PC2'), 'ip -6 addr add 2001:db8:acad:2::10/64 dev ens33'); shell(sim, get('PC2'), 'ip -6 route add default via 2001:db8:acad:2::1');
}
lab({ id: 'c105-ipv6', start: D + '1-05-ipv6/tp/c105-ipv6.json', solution: K + 'C105-ipv6-corrige.json',
  notes: 'CCNA 1-05 – IPv6 : deux routeurs, deux postes Linux. Plan : 2001:db8:acad:1::/64 (PC1), 2001:db8:acad:12::/64 (lien), 2001:db8:acad:2::/64 (PC2).',
  build: (sim, h) => v6Build(h), solve: v6Solve, checks: v6Checks, startShould: v6Checks.map(x => x.label) });

/* ---------- 2-01 : commutation, table MAC, VLAN ---------- */
function mac1Build(h) {
  const { dev, link, get } = h;
  dev('sw-2960', 'SW1', 400, 120);
  [['PC1', 100, 260, '10'], ['PC2', 300, 260, '11'], ['PC3', 500, 260, '12'], ['PC4', 700, 260, '13']].forEach(([n, x, y, ip], i) => { pc(h, n, x, y); link(n, PCIF, 'SW1', 'Fa0/' + (i + 1)); hostIp(get(n), '192.168.20.' + ip, '24'); });
}
const mac1Checks = [
  { label: 'Les VLAN 10 (COMPTA) et 20 (ATELIER) existent', run: c => /10\s+COMPTA/.test(ios(c, 'SW1', 'show vlan brief')) && /20\s+ATELIER/.test(ios(c, 'SW1', 'show vlan brief')) },
  { label: 'PC1 et PC2 (VLAN 10) se joignent', run: c => /bytes from/.test(sh(c, 'PC1', 'ping -c 2 192.168.20.11')) },
  { label: 'PC3 et PC4 (VLAN 20) se joignent', run: c => /bytes from/.test(sh(c, 'PC3', 'ping -c 2 192.168.20.13')) },
  { label: 'PC1 ne joint PAS PC3', run: c => !/bytes from/.test(sh(c, 'PC1', 'ping -c 2 192.168.20.12')) },
  { label: 'La table MAC contient des adresses dans le VLAN 10', run: c => /\s10\s+[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}\s+DYNAMIC/i.test(ios(c, 'SW1', 'show mac address-table')) },
];
function mac1Solve(sim, h) {
  cliRun(h.get('SW1'), 'enable\nconf t\nvlan 10\nname COMPTA\nvlan 20\nname ATELIER\nexit\ninterface range fa0/1 - 2\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface range fa0/3 - 4\nswitchport mode access\nswitchport access vlan 20\nend\nwrite memory');
  ['PC1', 'PC2', 'PC3', 'PC4'].forEach(n => shell(sim, h.get(n), 'ping -c 1 192.168.20.' + ({ PC1: 11, PC2: 10, PC3: 13, PC4: 12 })[n]));
}
lab({ id: 'c201-vlan-mac', start: D + '2-01-commutation-vlan/tp/c201-vlan-mac.json', solution: K + 'C201-vlan-mac-corrige.json',
  notes: 'CCNA 2-01 – Table MAC et VLAN : un switch neuf, quatre postes dans le même réseau 192.168.20.0/24. Observer la table MAC, puis séparer COMPTA (VLAN 10) et ATELIER (VLAN 20).',
  build: (sim, h) => mac1Build(h), solve: mac1Solve, checks: mac1Checks, startShould: ['Les VLAN 10 (COMPTA) et 20 (ATELIER) existent', 'PC1 ne joint PAS PC3', 'La table MAC contient des adresses dans le VLAN 10'] });

/* ---------- 2-02 : trunk, VLAN natif, routeur sur un bras ---------- */
function trBuild(h) {
  const { dev, link, get } = h;
  dev('r-2911', 'R1', 400, 20); dev('sw-2960', 'SW1', 200, 150); dev('sw-2960', 'SW2', 600, 150);
  [['PC10A', 60, 300, '10', 10, 'SW1', 1], ['PC20A', 260, 300, '10', 20, 'SW1', 2], ['PC10B', 540, 300, '11', 10, 'SW2', 1], ['PC20B', 740, 300, '11', 20, 'SW2', 2]].forEach(([n, x, y, host, v, sw, p]) => {
    pc(h, n, x, y); link(n, PCIF, sw, 'Fa0/' + p); hostIp(get(n), '192.168.' + v + '.' + host, '24', '192.168.' + v + '.1'); });
  link('SW1', 'Fa0/24', 'SW2', 'Fa0/24'); link('R1', 'gi0/0', 'SW1', 'Fa0/23');
}
const SW_VL = 'vlan 10\nname COMPTA\nvlan 20\nname ATELIER\nvlan 99\nname NATIF\nexit\n';
const trChecks = [
  { label: 'Trunk SW1–SW2 actif avec VLAN natif 99', run: c => /Fa0\/24\s+on\s+802\.1q\s+trunking\s+99/.test(ios(c, 'SW1', 'show interfaces trunk')) && /Fa0\/24\s+on\s+802\.1q\s+trunking\s+99/.test(ios(c, 'SW2', 'show interfaces trunk')) },
  { label: 'PC10A joint PC10B (même VLAN, autre switch)', run: c => /bytes from/.test(sh(c, 'PC10A', 'ping -c 2 192.168.10.11')) },
  { label: 'PC20A joint PC20B (même VLAN, autre switch)', run: c => /bytes from/.test(sh(c, 'PC20A', 'ping -c 2 192.168.20.11')) },
  { label: 'PC10A joint PC20B (routage inter-VLAN)', run: c => /bytes from/.test(sh(c, 'PC10A', 'ping -c 2 192.168.20.11')) },
];
function trSolve(sim, h) {
  const { get } = h;
  cliRun(get('SW1'), 'enable\nconf t\nhostname SW1\n' + SW_VL + 'interface fa0/1\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface fa0/2\nswitchport mode access\nswitchport access vlan 20\nexit\ninterface range fa0/23 - 24\nswitchport mode trunk\nswitchport trunk native vlan 99\nswitchport trunk allowed vlan 10,20,99\nend\nwrite memory');
  cliRun(get('SW2'), 'enable\nconf t\nhostname SW2\n' + SW_VL + 'interface fa0/1\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface fa0/2\nswitchport mode access\nswitchport access vlan 20\nexit\ninterface fa0/24\nswitchport mode trunk\nswitchport trunk native vlan 99\nswitchport trunk allowed vlan 10,20,99\nend\nwrite memory');
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\ninterface gi0/0\nno shutdown\nexit\ninterface gi0/0.10\nencapsulation dot1Q 10\nip address 192.168.10.1 255.255.255.0\nexit\ninterface gi0/0.20\nencapsulation dot1Q 20\nip address 192.168.20.1 255.255.255.0\nexit\ninterface gi0/0.99\nencapsulation dot1Q 99 native\nip address 192.168.99.1 255.255.255.0\nend\nwrite memory');
}
lab({ id: 'c202-trunk', start: D + '2-02-trunk-inter-vlan/tp/c202-trunk.json', solution: K + 'C202-trunk-corrige.json',
  notes: 'CCNA 2-02 – Deux switchs, deux VLAN (10 COMPTA, 20 ATELIER), un lien trunk avec VLAN natif 99, routage inter-VLAN par un routeur « sur un bras ». Postes déjà adressés, switchs et routeur vierges.',
  build: (sim, h) => trBuild(h), solve: trSolve, checks: trChecks, startShould: [trChecks[0].label, trChecks[3].label] });

/* ---------- 2-03 : CDP et EtherChannel ---------- */
function ecBuild(h) {
  const { dev, link, get } = h;
  dev('sw-2960', 'SW1', 250, 120); dev('sw-2960', 'SW2', 550, 120); pc(h, 'PC1', 100, 260); pc(h, 'PC2', 700, 260);
  link('SW1', 'Fa0/23', 'SW2', 'Fa0/23'); link('SW1', 'Fa0/24', 'SW2', 'Fa0/24'); link('PC1', PCIF, 'SW1', 'Fa0/1'); link('PC2', PCIF, 'SW2', 'Fa0/1');
  hostIp(get('PC1'), '10.1.1.1', '24'); hostIp(get('PC2'), '10.1.1.2', '24');
}
const ecChecks = [
  { label: 'CDP : SW1 voit SW2 comme voisin', run: c => /SW2/.test(ios(c, 'SW1', 'show cdp neighbors')) },
  { label: 'Etherchannel 1 (LACP) actif sur SW1 : Po1(SU) avec Fa0/23(P) et Fa0/24(P)', run: c => /Po1\(SU\)\s+LACP\s+Fa0\/23\(P\)\s+Fa0\/24\(P\)/.test(ios(c, 'SW1', 'show etherchannel summary')) },
  { label: 'Etherchannel 1 (LACP) actif sur SW2', run: c => /Po1\(SU\)\s+LACP/.test(ios(c, 'SW2', 'show etherchannel summary')) },
  { label: 'PC1 joint PC2', run: c => /bytes from/.test(sh(c, 'PC1', 'ping -c 2 10.1.1.2')) },
];
function ecSolve(sim, h) {
  ['SW1', 'SW2'].forEach(n => cliRun(h.get(n), 'enable\nconf t\nhostname ' + n + '\ninterface range fa0/23 - 24\nchannel-group 1 mode active\nexit\ninterface port-channel 1\nswitchport mode trunk\nend\nwrite memory'));
}
lab({ id: 'c203-etherchannel', start: D + '2-03-lldp-etherchannel/tp/c203-etherchannel.json', solution: K + 'C203-etherchannel-corrige.json',
  notes: 'CCNA 2-03 – Deux switchs reliés par deux câbles (Fa0/23 et Fa0/24). Observer CDP, puis regrouper les deux liens en un EtherChannel LACP.',
  build: (sim, h) => ecBuild(h), solve: ecSolve, checks: ecChecks, startShould: ecChecks.slice(1, 3).map(x => x.label) });

/* ---------- 2-04 : STP ---------- */
function stpBuild(h) {
  const { dev, link, get } = h;
  dev('sw-2960', 'SW1', 400, 60); dev('sw-2960', 'SW2', 200, 220); dev('sw-2960', 'SW3', 600, 220); pc(h, 'PC-SRV', 80, 340); pc(h, 'PC-CLI', 720, 340);
  link('SW1', 'Fa0/23', 'SW2', 'Fa0/23'); link('SW1', 'Fa0/24', 'SW3', 'Fa0/24'); link('SW2', 'Fa0/24', 'SW3', 'Fa0/23');
  link('PC-SRV', PCIF, 'SW2', 'Fa0/1'); link('PC-CLI', PCIF, 'SW3', 'Fa0/1'); hostIp(get('PC-SRV'), '10.2.2.10', '24'); hostIp(get('PC-CLI'), '10.2.2.20', '24');
}
const stpChecks = [
  { label: 'SW2 est le pont racine (priorité 4096 + n° de VLAN)', run: c => /This bridge is the root/.test(ios(c, 'SW2', 'show spanning-tree vlan 1')) },
  { label: 'Les trois switchs utilisent Rapid PVST+', run: c => ['SW1', 'SW2', 'SW3'].every(n => /spanning-tree mode rapid-pvst/.test(cfg(c, n))) },
  { label: 'PortFast et BPDU guard sur les ports des postes (SW2 et SW3, Fa0/1)', run: c => ['SW2', 'SW3'].every(n => /interface FastEthernet0\/1\n[^!]*spanning-tree portfast/.test(cfg(c, n)) && /spanning-tree bpduguard enable/.test(cfg(c, n))) },
  { label: 'PC-SRV joint PC-CLI', run: c => /bytes from/.test(sh(c, 'PC-SRV', 'ping -c 2 10.2.2.20')) },
];
function stpSolve(sim, h) {
  ['SW1', 'SW2', 'SW3'].forEach(n => cliRun(h.get(n), 'enable\nconf t\nhostname ' + n + '\nspanning-tree mode rapid-pvst\nend'));
  cliRun(h.get('SW2'), 'enable\nconf t\nspanning-tree vlan 1 priority 4096\nend\nwrite memory');
  cliRun(h.get('SW1'), 'enable\nconf t\nspanning-tree vlan 1 priority 8192\nend\nwrite memory');
  ['SW2', 'SW3'].forEach(n => cliRun(h.get(n), 'enable\nconf t\ninterface fa0/1\nspanning-tree portfast\nspanning-tree bpduguard enable\nend\nwrite memory'));
}
lab({ id: 'c204-stp', start: D + '2-04-stp/tp/c204-stp.json', solution: K + 'C204-stp-corrige.json',
  notes: 'CCNA 2-04 – STP : trois switchs en triangle. Faire de SW2 le pont racine (SW1 en secours), passer en Rapid PVST+, protéger les ports des postes avec PortFast et BPDU guard.',
  build: (sim, h) => stpBuild(h), solve: stpSolve, checks: stpChecks, startShould: stpChecks.slice(0, 3).map(x => x.label) });

const want = process.argv.slice(2); let all = true;
TPS.filter(t => !want.length || want.includes(t.id)).forEach(t => { all = L.run(t) && all; });
process.exit(all ? 0 : 1);
