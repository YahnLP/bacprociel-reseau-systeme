/* TP du simulateur – parcours CCNA. Lancer : SIM_DIR=… node tools/tp/ccna.js [id ...]
   Départ : docs/ccna/<module>/tp/*.json ; corrigé : corriges/ccna/*.json (local). */
const L = require('./lib');
const { hostIp, cliRun, shell, IP } = L;
const D = 'docs/ccna/', K = 'corriges/ccna/';
const TPS = [];
const dv = (c, n) => Array.from(c.sim.devices.values()).find(d => d.name === n);
const PWS = ['', 'Cisco#2027', 'cisco', 'Cisco123', 'class'];
const ios = (c, n, cmd) => { const d = dv(c, n);
  for (const pw of PWS) { const s = d.newSession(); let out = '', done = false; const io = { print: t => { out += t; }, done: () => { done = true; }, clear() { } };
    const go = l => { done = false; out = ''; s.exec(l, io); c.sim.runUntil(() => done, 60000); };
    go('enable'); if (pw) go(pw); go(cmd); if (out.trim() && !/Invalid|Access denied|Bad secrets|Password/.test(out)) return out; }
  return ''; };
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


/* ---------- Topologie triangle de routeurs (3-01, 3-02, 3-03) ---------- */
function triBuild(h, withStatic) {
  const { dev, link, get } = h;
  dev('r-2911', 'R1', 150, 120); dev('r-2911', 'R2', 450, 20); dev('r-2911', 'R3', 750, 120);
  dev('sw-2960', 'SW1', 60, 260); dev('sw-2960', 'SW3', 840, 260); pc(h, 'PC1', 60, 360); pc(h, 'PC3', 840, 360);
  link('R1', 'gi0/1', 'R2', 'gi0/1'); link('R2', 'gi0/2', 'R3', 'gi0/1'); link('R1', 'gi0/2', 'R3', 'gi0/2');
  link('SW1', 'Fa0/24', 'R1', 'gi0/0'); link('SW3', 'Fa0/24', 'R3', 'gi0/0'); link('PC1', PCIF, 'SW1', 'Fa0/1'); link('PC3', PCIF, 'SW3', 'Fa0/1');
  const i = (n, g0, g1, g2) => cliRun(get(n), 'enable\nconf t\nhostname ' + n + '\n' + [['gi0/0', g0], ['gi0/1', g1], ['gi0/2', g2]].filter(x => x[1]).map(x => 'interface ' + x[0] + '\nip address ' + x[1] + ' 255.255.255.' + (x[0] === 'gi0/0' ? '0' : '252') + '\nno shutdown\nexit').join('\n').replace(/255\.255\.255\.0\n/g, '255.255.255.0\n') + '\nend\nwrite memory');
  i('R1', '192.168.1.1', '10.0.12.1', '10.0.13.1'); i('R2', null, '10.0.12.2', '10.0.23.1'); i('R3', '192.168.3.1', '10.0.23.2', '10.0.13.2');
  hostIp(get('PC1'), '192.168.1.10', '24', '192.168.1.1'); hostIp(get('PC3'), '192.168.3.10', '24', '192.168.3.1');
}
const R1_ST = 'enable\nconf t\nip route 192.168.3.0 255.255.255.0 10.0.12.2\nip route 10.0.23.0 255.255.255.252 10.0.12.2\nend\nwrite memory';
const R2_ST = 'enable\nconf t\nip route 192.168.1.0 255.255.255.0 10.0.12.1\nip route 192.168.3.0 255.255.255.0 10.0.23.2\nip route 10.0.13.0 255.255.255.252 10.0.12.1\nend\nwrite memory';
const R3_ST = 'enable\nconf t\nip route 192.168.1.0 255.255.255.0 10.0.13.1\nip route 10.0.12.0 255.255.255.252 10.0.13.1\nend\nwrite memory';
lab({ id: 'c301-table-routage', start: D + '3-01-table-routage/tp/c301-table-routage.json',
  notes: 'CCNA 3-01 – Trois routeurs en triangle, routes statiques déjà en place. Lire les tables de routage : codes, préfixe, next hop, distance administrative, métrique, plus long préfixe.',
  build: (sim, h) => { triBuild(h); cliRun(h.get('R1'), R1_ST); cliRun(h.get('R2'), R2_ST); cliRun(h.get('R3'), R3_ST); cliRun(h.get('R1'), 'enable\nconf t\nip route 192.168.0.0 255.255.0.0 10.0.13.2\nip route 0.0.0.0 0.0.0.0 10.0.13.2\nend\nwrite memory'); }, checks: [], startShould: [] });

const stChecks = [
  { label: 'PC1 joint PC3 (routes statiques)', run: c => /bytes from/.test(sh(c, 'PC1', 'ping -c 2 192.168.3.10')) },
  { label: 'PC3 joint PC1 (retour)', run: c => /bytes from/.test(sh(c, 'PC3', 'ping -c 2 192.168.1.10')) },
  { label: 'R1 a une route par défaut vers R2 (10.0.12.2)', run: c => /ip route 0\.0\.0\.0 0\.0\.0\.0 10\.0\.12\.2\n/.test(cfg(c, 'R1')) },
  { label: 'R1 a une route flottante (distance 200) via R3', run: c => /ip route 0\.0\.0\.0 0\.0\.0\.0 10\.0\.13\.2 200/.test(cfg(c, 'R1')) },
  { label: 'La route flottante prend le relais quand le lien R1–R2 tombe', run: c => { cliRun(dv(c, 'R1'), 'enable\nconf t\ninterface gi0/1\nshutdown\nend'); c.wait(8000); return /bytes from/.test(sh(c, 'PC1', 'ping -c 2 192.168.3.10')); } },
];
function stSolve(sim, h) {
  cliRun(h.get('R1'), 'enable\nconf t\nip route 192.168.3.0 255.255.255.0 10.0.12.2\nip route 10.0.23.0 255.255.255.252 10.0.12.2\nip route 0.0.0.0 0.0.0.0 10.0.12.2\nip route 0.0.0.0 0.0.0.0 10.0.13.2 200\nip route 192.168.3.0 255.255.255.0 10.0.13.2 200\nend\nwrite memory');
  cliRun(h.get('R2'), R2_ST);
  cliRun(h.get('R3'), 'enable\nconf t\nip route 192.168.1.0 255.255.255.0 10.0.13.1\nip route 10.0.12.0 255.255.255.252 10.0.13.1\nend\nwrite memory');
}
lab({ id: 'c302-routage-statique', start: D + '3-02-routage-statique/tp/c302-routage-statique.json', solution: K + 'C302-routage-statique-corrige.json',
  notes: 'CCNA 3-02 – Triangle R1/R2/R3, interfaces configurées, aucune route. À faire : routes statiques (réseau), route par défaut, route flottante de secours via le lien R1–R3.',
  build: (sim, h) => triBuild(h), solve: stSolve, checks: stChecks, startShould: stChecks.map(x => x.label) });

const ospfChecks = [
  { label: 'R1 a une adjacence OSPF FULL avec R2', run: c => { c.wait(45000); return /FULL/.test(ios(c, 'R1', 'show ip ospf neighbor')) && /10\.0\.12\.2/.test(ios(c, 'R1', 'show ip ospf neighbor')); } },
  { label: 'R3 a deux adjacences FULL (R1 et R2)', run: c => (ios(c, 'R3', 'show ip ospf neighbor').match(/FULL/g) || []).length >= 2 },
  { label: 'Les routeurs ont un router-id fixé (1.1.1.1, 2.2.2.2, 3.3.3.3)', run: c => [['R1', '1.1.1.1'], ['R2', '2.2.2.2'], ['R3', '3.3.3.3']].every(([n, r]) => new RegExp('router-id ' + r.replace(/\./g, '\\.')).test(cfg(c, n))) },
  { label: 'Le LAN de R1 est en passive-interface', run: c => /passive-interface GigabitEthernet0\/0/.test(cfg(c, 'R1')) },
  { label: 'R1 apprend 192.168.3.0/24 par OSPF (code O)', run: c => /O\s+192\.168\.3\.0\/24/.test(ios(c, 'R1', 'show ip route')) },
  { label: 'PC1 joint PC3', run: c => /bytes from/.test(sh(c, 'PC1', 'ping -c 2 192.168.3.10')) },
];
function ospfSolve(sim, h) {
  const rid = { R1: '1.1.1.1', R2: '2.2.2.2', R3: '3.3.3.3' };
  const nets = { R1: ['192.168.1.0 0.0.0.255', '10.0.12.0 0.0.0.3', '10.0.13.0 0.0.0.3'], R2: ['10.0.12.0 0.0.0.3', '10.0.23.0 0.0.0.3'], R3: ['192.168.3.0 0.0.0.255', '10.0.23.0 0.0.0.3', '10.0.13.0 0.0.0.3'] };
  ['R1', 'R2', 'R3'].forEach(n => cliRun(h.get(n), 'enable\nconf t\nrouter ospf 1\nrouter-id ' + rid[n] + '\n' + nets[n].map(x => 'network ' + x + ' area 0').join('\n') + '\n' + (n === 'R2' ? '' : 'passive-interface gi0/0\n') + 'end\nwrite memory'));
}
lab({ id: 'c303-ospf', start: D + '3-03-ospf/tp/c303-ospf.json', solution: K + 'C303-ospf-corrige.json',
  notes: 'CCNA 3-03 – Triangle R1/R2/R3, interfaces configurées, aucun routage. À faire : OSPFv2 mono-zone (aire 0), router-id, passive-interface sur les LAN.',
  build: (sim, h) => triBuild(h), solve: ospfSolve, checks: ospfChecks, startShould: ospfChecks.map(x => x.label) });

/* ---------- 4-01 : PAT ---------- */
const C = require('./common');
function natBuild(sim, h) {
  const { dev, link, get } = h;
  C.internet(sim, h, 650, 150);
  dev('r-2911', 'R1', 450, 150, 'Routeur de bordure'); dev('sw-2960', 'SW1', 250, 150);
  pc(h, 'PC1', 80, 80); pc(h, 'PC2', 80, 220);
  link('R1', 'gi0/1', 'FAI', 'gi0/0'); link('R1', 'gi0/0', 'SW1', 'Fa0/24'); link('PC1', PCIF, 'SW1', 'Fa0/1'); link('PC2', PCIF, 'SW1', 'Fa0/2');
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\ninterface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 203.0.113.2 255.255.255.248\nno shutdown\nexit\nip route 0.0.0.0 0.0.0.0 203.0.113.1\nend\nwrite memory');
  hostIp(get('PC1'), '192.168.10.11', '24', '192.168.10.1', '198.51.100.53'); hostIp(get('PC2'), '192.168.10.12', '24', '192.168.10.1', '198.51.100.53');
}
const natChecks = [
  { label: 'PC1 joint le serveur web (198.51.100.80)', run: c => /bytes from/.test(sh(c, 'PC1', 'ping -c 2 198.51.100.80')) },
  { label: 'R1 a une interface inside et une interface outside', run: c => /ip nat inside/.test(cfg(c, 'R1')) && /ip nat outside/.test(cfg(c, 'R1')) },
  { label: 'La table NAT contient des traductions vers 203.0.113.2', run: c => { sh(c, 'PC2', 'ping -c 2 198.51.100.80'); return /203\.0\.113\.2/.test(ios(c, 'R1', 'show ip nat translations')); } },
];
function natSolve(sim, h) {
  cliRun(h.get('R1'), 'enable\nconf t\naccess-list 1 permit 192.168.10.0 0.0.0.255\ninterface gi0/0\nip nat inside\nexit\ninterface gi0/1\nip nat outside\nexit\nip nat inside source list 1 interface gi0/1 overload\nend\nwrite memory');
}
lab({ id: 'c401-nat', start: D + '4-01-nat/tp/c401-nat.json', solution: K + 'C401-nat-corrige.json',
  notes: 'CCNA 4-01 – PAT : un routeur de bordure, deux postes en adresses privées, un FAI avec un serveur web. À faire : traduire les adresses privées vers l\'adresse publique 203.0.113.2.',
  build: natBuild, solve: natSolve, checks: natChecks, startShould: natChecks.map(x => x.label) });

/* ---------- 4-02 : DHCP et relais ---------- */
function dhBuild(h) {
  const { dev, link, get } = h;
  dev('r-2911', 'R1', 350, 120, 'Passerelle des postes'); dev('r-2911', 'R2', 650, 120, 'Serveur DHCP'); dev('sw-2960', 'SW1', 150, 120); pc(h, 'PC1', 50, 40); pc(h, 'PC2', 50, 200);
  link('SW1', 'Fa0/24', 'R1', 'gi0/0'); link('R1', 'gi0/1', 'R2', 'gi0/1'); link('PC1', PCIF, 'SW1', 'Fa0/1'); link('PC2', PCIF, 'SW1', 'Fa0/2');
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\ninterface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 10.0.0.1 255.255.255.252\nno shutdown\nexit\nip route 0.0.0.0 0.0.0.0 10.0.0.2\nend\nwrite memory');
  cliRun(get('R2'), 'enable\nconf t\nhostname R2\ninterface gi0/1\nip address 10.0.0.2 255.255.255.252\nno shutdown\nexit\nip route 192.168.10.0 255.255.255.0 10.0.0.1\nend\nwrite memory');
  ['PC1', 'PC2'].forEach(n => L.hostDhcp(get(n)));
}
const dhChecks = [
  { label: 'R2 a un pool DHCP pour 192.168.10.0/24', run: c => /ip dhcp pool/.test(cfg(c, 'R2')) && /network 192\.168\.10\.0 255\.255\.255\.0/.test(cfg(c, 'R2')) },
  { label: 'R1 relaie les requêtes DHCP vers 10.0.0.2 (ip helper-address)', run: c => /ip helper-address 10\.0\.0\.2/.test(cfg(c, 'R1')) },
  { label: 'PC1 reçoit une adresse 192.168.10.x', run: c => { c.wait(8000); return /192\.168\.10\.\d+/.test(sh(c, 'PC1', 'ip -4 addr')); } },
  { label: 'PC2 reçoit une adresse différente de PC1', run: c => { const a = (sh(c, 'PC1', 'ip -4 addr').match(/inet (192\.168\.10\.\d+)/) || [])[1], b = (sh(c, 'PC2', 'ip -4 addr').match(/inet (192\.168\.10\.\d+)/) || [])[1]; return !!a && !!b && a !== b; } },
];
function dhSolve(sim, h) {
  cliRun(h.get('R2'), 'enable\nconf t\nip dhcp excluded-address 192.168.10.1 192.168.10.9\nip dhcp pool LAN10\nnetwork 192.168.10.0 255.255.255.0\ndefault-router 192.168.10.1\ndns-server 8.8.8.8\nend\nwrite memory');
  cliRun(h.get('R1'), 'enable\nconf t\ninterface gi0/0\nip helper-address 10.0.0.2\nend\nwrite memory');
  ['PC1', 'PC2'].forEach(n => { L.hostDhcp(h.get(n)); });
}
lab({ id: 'c402-dhcp-relais', start: D + '4-02-dhcp-dns/tp/c402-dhcp-relais.json', solution: K + 'C402-dhcp-relais-corrige.json',
  notes: 'CCNA 4-02 – DHCP et relais : les postes sont sur 192.168.10.0/24 (R1), le serveur DHCP est R2 sur un autre réseau. À faire : pool sur R2, ip helper-address sur R1.',
  build: (sim, h) => dhBuild(h), solve: dhSolve, checks: dhChecks, startShould: dhChecks.map(x => x.label) });

/* ---------- 4-03 : syslog et SNMP ---------- */
function slBuild(h) {
  const { dev, link, get } = h;
  dev('r-2911', 'R1', 350, 120); dev('sw-2960', 'SW1', 150, 120); dev('srv-linux', 'SRV-SUP', 550, 120, 'Serveur de supervision'); pc(h, 'PC1', 50, 120);
  link('SW1', 'Fa0/24', 'R1', 'gi0/0'); link('R1', 'gi0/1', 'SRV-SUP', PCIF); link('PC1', PCIF, 'SW1', 'Fa0/1');
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\ninterface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 10.9.0.1 255.255.255.0\nno shutdown\nend\nwrite memory');
  hostIp(get('SRV-SUP'), '10.9.0.10', '24', '10.9.0.1'); hostIp(get('PC1'), '192.168.10.11', '24', '192.168.10.1');
}
const slChecks = [
  { label: 'R1 envoie ses journaux (syslog) à 10.9.0.10', run: c => /logging host 10\.9\.0\.10/.test(cfg(c, 'R1')) },
  { label: 'Seuls les messages de niveau 4 (warnings) et plus graves sont envoyés', run: c => /logging trap warnings/.test(cfg(c, 'R1')) },
  { label: 'Une communauté SNMP en lecture seule « CIEL-RO » existe', run: c => /snmp-server community CIEL-RO RO/i.test(cfg(c, 'R1')) },
  { label: 'La localisation SNMP est renseignée', run: c => /snmp-server location \S+/.test(cfg(c, 'R1')) },
];
function slSolve(sim, h) { cliRun(h.get('R1'), 'enable\nconf t\nlogging host 10.9.0.10\nlogging trap warnings\nsnmp-server community CIEL-RO RO\nsnmp-server location SalleServeurs\nend\nwrite memory'); }
lab({ id: 'c403-syslog-snmp', start: D + '4-03-ntp-snmp-syslog/tp/c403-syslog-snmp.json', solution: K + 'C403-syslog-snmp-corrige.json',
  notes: 'CCNA 4-03 – Un routeur doit envoyer ses journaux à un serveur de supervision (syslog) et répondre en SNMP. NTP n\'est pas simulé : à connaître pour l\'examen.',
  build: (sim, h) => slBuild(h), solve: slSolve, checks: slChecks, startShould: slChecks.map(x => x.label) });

/* ---------- 4-04 : QoS ---------- */
function qsBuild(h) {
  const { dev, link, get } = h;
  dev('r-2911', 'R1', 350, 120); dev('sw-2960', 'SW1', 150, 120); pc(h, 'PC1', 50, 120); dev('r-2911', 'R2', 600, 120);
  link('SW1', 'Fa0/24', 'R1', 'gi0/0'); link('R1', 'gi0/1', 'R2', 'gi0/1'); link('PC1', PCIF, 'SW1', 'Fa0/1');
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\ninterface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 10.0.0.1 255.255.255.252\nno shutdown\nend\nwrite memory');
  cliRun(get('R2'), 'enable\nconf t\nhostname R2\ninterface gi0/1\nip address 10.0.0.2 255.255.255.252\nno shutdown\nexit\nip route 192.168.10.0 255.255.255.0 10.0.0.1\nend\nwrite memory');
  hostIp(get('PC1'), '192.168.10.11', '24', '192.168.10.1');
}
const qsChecks = [
  { label: 'Une class-map reconnaît la voix (DSCP EF)', run: c => /class-map match-any VOIX/.test(cfg(c, 'R1')) && /match (ip )?dscp ef/.test(cfg(c, 'R1')) },
  { label: 'La policy-map donne une priorité de 256 kb/s à la voix', run: c => /class VOIX\n\s+priority 256/.test(cfg(c, 'R1')) },
  { label: 'La policy-map est appliquée en sortie sur gi0/1', run: c => /service-policy output/.test(cfg(c, 'R1')) },
  { label: 'Le réseau fonctionne toujours (PC1 joint R2)', run: c => /bytes from/.test(sh(c, 'PC1', 'ping -c 2 10.0.0.2')) },
];
function qsSolve(sim, h) { cliRun(h.get('R1'), 'enable\nconf t\nclass-map match-any VOIX\nmatch dscp ef\nexit\npolicy-map SORTIE\nclass VOIX\npriority 256\nclass class-default\nfair-queue\nexit\nexit\ninterface gi0/1\nservice-policy output SORTIE\nend\nwrite memory'); }
lab({ id: 'c404-qos', start: D + '4-04-qos/tp/c404-qos.json', solution: K + 'C404-qos-corrige.json',
  notes: 'CCNA 4-04 – QoS : le lien R1–R2 est le goulot. À faire : classer la voix (DSCP EF), lui donner une file prioritaire de 256 kb/s, appliquer en sortie.',
  build: (sim, h) => qsBuild(h), solve: qsSolve, checks: qsChecks, startShould: qsChecks.slice(0, 3).map(x => x.label) });

/* ---------- 4-05 : SSH ---------- */
function sshBuild(h) {
  const { dev, link, get } = h;
  dev('sw-2960', 'SW1', 300, 120); pc(h, 'PC-ADMIN', 100, 120);
  link('PC-ADMIN', PCIF, 'SW1', 'Fa0/1');
  hostIp(get('PC-ADMIN'), '10.0.0.2', '24'); cliRun(get('SW1'), 'enable\nconf t\ninterface vlan 1\nip address 10.0.0.1 255.255.255.0\nno shutdown\nend\nwrite memory');
}
const sshChecks = [
  { label: 'Un nom de domaine est configuré (ip domain-name)', run: c => /ip domain-name \S+/.test(cfg(c, 'SW1')) },
  { label: 'Un utilisateur local « admin » existe', run: c => /username admin/.test(cfg(c, 'SW1')) },
  { label: 'Les lignes vty utilisent l\'authentification locale', run: c => /line vty 0 4[^!]*login local/.test(cfg(c, 'SW1')) },
  { label: 'Les lignes vty n\'acceptent que SSH (transport input ssh)', run: c => /transport input ssh/.test(cfg(c, 'SW1')) },
];
function sshSolve(sim, h) { cliRun(h.get('SW1'), 'enable\nconf t\nhostname SW1\nip domain-name ciel.local\nusername admin secret Pa55w0rd!\ncrypto key generate rsa modulus 2048\nip ssh version 2\nline vty 0 4\nlogin local\ntransport input ssh\nend\nwrite memory'); }
lab({ id: 'c405-ssh', start: D + '4-05-ssh-tftp/tp/c405-ssh.json', solution: K + 'C405-ssh-corrige.json',
  notes: 'CCNA 4-05 – Sécuriser l\'accès distant : un switch, un poste d\'administration. À faire : nom de domaine, utilisateur local, clés RSA, SSH 2, lignes vty en SSH seul.',
  build: (sim, h) => sshBuild(h), solve: sshSolve, checks: sshChecks, startShould: sshChecks.map(x => x.label) });


/* ---------- 5-02 : durcir l'accès aux équipements ---------- */
function hdBuild(h) {
  const { dev, link, get } = h;
  dev('sw-2960', 'SW1', 300, 120); pc(h, 'PC-ADMIN', 100, 120); link('PC-ADMIN', PCIF, 'SW1', 'Fa0/1'); hostIp(get('PC-ADMIN'), '10.0.0.2', '24');
  cliRun(get('SW1'), 'enable\nconf t\nhostname SW1\ninterface vlan 1\nip address 10.0.0.1 255.255.255.0\nno shutdown\nend\nwrite memory');
}
const hdChecks = [
  { label: 'Mot de passe enable chiffré (enable secret)', run: c => /enable secret/.test(cfg(c, 'SW1')) },
  { label: 'Bannière d\'avertissement (banner motd)', run: c => /banner motd/.test(cfg(c, 'SW1')) },
  { label: 'Un compte local « admin » avec mot de passe chiffré (secret)', run: c => /username admin .*secret/.test(cfg(c, 'SW1')) },
  { label: 'Authentification AAA locale activée', run: c => /aaa new-model/.test(cfg(c, 'SW1')) && /aaa authentication login default local/.test(cfg(c, 'SW1')) },
  { label: 'Les lignes vty exigent une connexion (login local)', run: c => /line vty 0 4[^!]*login local/.test(cfg(c, 'SW1')) },
];
function hdSolve(sim, h) { cliRun(h.get('SW1'), 'enable\nconf t\nenable secret Cisco#2027\nusername admin secret Pa55w0rd!\nbanner motd #Acces reserve aux personnes autorisees#\naaa new-model\naaa authentication login default local\nline vty 0 4\nlogin local\nend\nwrite memory'); }
lab({ id: 'c502-durcissement', start: D + '5-02-acces-equipements-aaa/tp/c502-durcissement.json', solution: K + 'C502-durcissement-corrige.json',
  notes: 'CCNA 5-02 – Un switch neuf, sans protection. À faire : enable secret, compte local, bannière, AAA locale, lignes vty. (Chiffrement des mots de passe, console et délai de déconnexion : voir Packet Tracer.)',
  build: (sim, h) => hdBuild(h), solve: hdSolve, checks: hdChecks, startShould: hdChecks.map(x => x.label) });

/* ---------- 5-03 : ACL étendue ---------- */
function aclBuild(h) {
  const { dev, link, get } = h;
  dev('r-2911', 'R1', 350, 140); dev('sw-2960', 'SW1', 150, 140); pc(h, 'PC-COMPTA', 40, 60); pc(h, 'PC-STAGIAIRE', 40, 220);
  dev('srv-linux', 'SRV', 600, 140, 'Serveur interne (web)');
  link('SW1', 'Fa0/24', 'R1', 'gi0/0'); link('PC-COMPTA', PCIF, 'SW1', 'Fa0/1'); link('PC-STAGIAIRE', PCIF, 'SW1', 'Fa0/2'); link('R1', 'gi0/1', 'SRV', PCIF);
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\ninterface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 192.168.20.1 255.255.255.0\nno shutdown\nend\nwrite memory');
  hostIp(get('PC-COMPTA'), '192.168.10.11', '24', '192.168.10.1'); hostIp(get('PC-STAGIAIRE'), '192.168.10.12', '24', '192.168.10.1'); hostIp(get('SRV'), '192.168.20.10', '24', '192.168.20.1');
  const w = get('SRV'); w.httpd.pages['/'] = { type: 'text/html; charset=utf-8', body: '<html><body><h1>Intranet</h1></body></html>' }; if (w.httpd.start) w.httpd.start();
}
const web = (c, n) => /Intranet|200|<h1>/.test(sh(c, n, 'curl http://192.168.20.10'));
const aclChecks = [
  { label: 'PC-COMPTA ouvre le site web du serveur (HTTP)', run: c => web(c, 'PC-COMPTA') },
  { label: 'PC-STAGIAIRE ne peut PAS ouvrir le site web', run: c => !web(c, 'PC-STAGIAIRE') },
  { label: 'PC-COMPTA ne peut PAS faire de ping vers le serveur (seul le web est autorisé)', run: c => !/bytes from/.test(sh(c, 'PC-COMPTA', 'ping -c 2 192.168.20.10')) },
  { label: 'Une ACL étendue nommée est appliquée en entrée sur gi0/0', run: c => /ip access-list extended \S+/.test(cfg(c, 'R1')) && /ip access-group \S+ in/.test(cfg(c, 'R1')) },
];
function aclSolve(sim, h) { cliRun(h.get('R1'), 'enable\nconf t\nip access-list extended VERS-SERVEUR\ndeny ip host 192.168.10.12 any\npermit tcp host 192.168.10.11 host 192.168.20.10 eq 80\ndeny ip any any\nexit\ninterface gi0/0\nip access-group VERS-SERVEUR in\nend\nwrite memory'); }
lab({ id: 'c503-acl', start: D + '5-03-acl/tp/c503-acl.json', solution: K + 'C503-acl-corrige.json',
  notes: 'CCNA 5-03 – ACL étendue : le serveur interne ne doit être joignable en web que depuis PC-COMPTA ; PC-STAGIAIRE ne doit rien joindre ; tout le reste est refusé.',
  build: (sim, h) => aclBuild(h), solve: aclSolve, checks: aclChecks, startShould: [aclChecks[1].label, aclChecks[2].label, aclChecks[3].label] });

/* ---------- 5-04 : port security ---------- */
function psBuild(h) {
  const { dev, link, get } = h;
  dev('sw-2960', 'SW1', 300, 120); pc(h, 'PC1', 100, 60); pc(h, 'PC2', 100, 200); link('PC1', PCIF, 'SW1', 'Fa0/1'); link('PC2', PCIF, 'SW1', 'Fa0/2');
  hostIp(get('PC1'), '10.5.0.11', '24'); hostIp(get('PC2'), '10.5.0.12', '24');
}
const psChecks = [
  { label: 'Fa0/1 : port-security activé', run: c => /interface FastEthernet0\/1\n[^!]*switchport port-security/.test(cfg(c, 'SW1')) },
  { label: 'Fa0/1 : adresse MAC apprise (sticky)', run: c => /interface FastEthernet0\/1\n[^!]*switchport port-security mac-address sticky/.test(cfg(c, 'SW1')) },
  { label: 'show port-security : Fa0/1 limité à 1 adresse, action Shutdown', run: c => /Fa0\/1\s+1\s+\d+\s+\d+\s+Shutdown/.test(ios(c, 'SW1', 'show port-security')) },
  { label: 'Ports inutilisés Fa0/10 à Fa0/24 désactivés', run: c => /interface FastEthernet0\/24\n shutdown/.test(cfg(c, 'SW1')) },
];
function psSolve(sim, h) { cliRun(h.get('SW1'), 'enable\nconf t\nhostname SW1\ninterface range fa0/1 - 2\nswitchport mode access\nswitchport port-security\nswitchport port-security maximum 1\nswitchport port-security mac-address sticky\nswitchport port-security violation shutdown\nexit\ninterface range fa0/10 - 24\nshutdown\nend\nwrite memory'); }
lab({ id: 'c504-port-security', start: D + '5-04-securite-couche2/tp/c504-port-security.json', solution: K + 'C504-port-security-corrige.json',
  notes: 'CCNA 5-04 – Sécurité de couche 2 : un switch d\'accès, deux postes. À faire : port-security (1 adresse, sticky, shutdown) sur Fa0/1 et Fa0/2, ports inutilisés coupés.',
  build: (sim, h) => psBuild(h), solve: psSolve, checks: psChecks, startShould: psChecks.map(x => x.label) });

/* ---------- 5-05 : VPN IPsec site à site ---------- */
function vpnBuild(h) {
  const { dev, link, get } = h;
  dev('r-2911', 'R1', 200, 150, 'Site A'); dev('r-2911', 'ISP', 450, 150, 'Internet'); dev('r-2911', 'R2', 700, 150, 'Site B');
  dev('sw-2960', 'SW-A', 80, 150); dev('sw-2960', 'SW-B', 820, 150); pc(h, 'PC1', 20, 240, 'Site A'); pc(h, 'PC2', 880, 240, 'Site B');
  link('SW-A', 'Fa0/24', 'R1', 'gi0/0'); link('R1', 'gi0/1', 'ISP', 'gi0/0'); link('ISP', 'gi0/1', 'R2', 'gi0/1'); link('R2', 'gi0/0', 'SW-B', 'Fa0/24');
  link('PC1', PCIF, 'SW-A', 'Fa0/1'); link('PC2', PCIF, 'SW-B', 'Fa0/1');
  const ifc = (n, lines) => cliRun(get(n), 'enable\nconf t\nhostname ' + n + '\n' + lines + '\nend\nwrite memory');
  ifc('R1', 'interface gi0/0\nip address 192.168.1.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 198.51.100.1 255.255.255.252\nno shutdown\nexit\nip route 0.0.0.0 0.0.0.0 198.51.100.2');
  ifc('ISP', 'interface gi0/0\nip address 198.51.100.2 255.255.255.252\nno shutdown\nexit\ninterface gi0/1\nip address 198.51.100.5 255.255.255.252\nno shutdown');
  ifc('R2', 'interface gi0/0\nip address 192.168.2.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 198.51.100.6 255.255.255.252\nno shutdown\nexit\nip route 0.0.0.0 0.0.0.0 198.51.100.5');
  hostIp(get('PC1'), '192.168.1.10', '24', '192.168.1.1'); hostIp(get('PC2'), '192.168.2.10', '24', '192.168.2.1');
}
const vpnCfg = (loc, rem, peer) => 'enable\nconf t\naccess-list 101 permit ip ' + loc + ' 0.0.0.255 ' + rem + ' 0.0.0.255\ncrypto isakmp policy 10\nencryption aes 256\nhash sha256\nauthentication pre-share\ngroup 14\nexit\ncrypto isakmp key Cle#VPN2027 address ' + peer + '\ncrypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac\ncrypto map CMAP 10 ipsec-isakmp\nset peer ' + peer + '\nset transform-set TS\nmatch address 101\nexit\ninterface gi0/1\ncrypto map CMAP\nend\nwrite memory';
const vpnChecks = [
  { label: 'PC1 joint PC2 à travers le tunnel', run: c => /bytes from/.test(sh(c, 'PC1', 'ping -c 3 192.168.2.10')) },
  { label: 'R1 : la crypto map est appliquée sur gi0/1', run: c => /crypto map CMAP/.test(cfg(c, 'R1')) && /interface GigabitEthernet0\/1[^!]*crypto map/.test(cfg(c, 'R1')) },
  { label: 'R1 : une association de sécurité IKE existe (show crypto isakmp sa)', run: c => { sh(c, 'PC1', 'ping -c 3 192.168.2.10'); return /198\.51\.100\.(2|6)|QM_IDLE|ACTIVE/.test(ios(c, 'R1', 'show crypto isakmp sa')); } },
  { label: 'L\'ACL 101 décrit le trafic à chiffrer (192.168.1.0/24 ↔ 192.168.2.0/24)', run: c => /access-list 101 permit ip 192\.168\.1\.0 0\.0\.0\.255 192\.168\.2\.0 0\.0\.0\.255/.test(cfg(c, 'R1')) },
];
function vpnSolve(sim, h) { cliRun(h.get('R1'), vpnCfg('192.168.1.0', '192.168.2.0', '198.51.100.6')); cliRun(h.get('R2'), vpnCfg('192.168.2.0', '192.168.1.0', '198.51.100.1')); }
lab({ id: 'c505-vpn-ipsec', start: D + '5-05-vpn-ipsec/tp/c505-vpn-ipsec.json', solution: K + 'C505-vpn-ipsec-corrige.json',
  notes: 'CCNA 5-05 – VPN IPsec site à site : deux sites (R1, R2) reliés par Internet (ISP) qui ne route pas les adresses privées. À faire : ACL du trafic à chiffrer, politique IKE, clé partagée, transform-set, crypto map.',
  build: (sim, h) => vpnBuild(h), solve: vpnSolve, checks: vpnChecks, startShould: [vpnChecks[0].label, vpnChecks[1].label, vpnChecks[2].label, vpnChecks[3].label] });

/* ---------- 7-01 : réseau en panne (trois pannes à diagnostiquer) ---------- */
function repBuild(h) {
  const { dev, link, get } = h;
  dev('r-2911', 'R1', 300, 40, 'Routeur d\'étage'); dev('r-2911', 'R2', 600, 40, 'Routeur serveurs'); dev('sw-2960', 'SW1', 150, 160);
  pc(h, 'PC10', 40, 300, 'COMPTA'); pc(h, 'PC20', 260, 300, 'ATELIER'); pc(h, 'SRV', 760, 160, 'Serveur');
  link('PC10', PCIF, 'SW1', 'Fa0/1'); link('PC20', PCIF, 'SW1', 'Fa0/2'); link('SW1', 'Fa0/24', 'R1', 'gi0/0'); link('R1', 'gi0/1', 'R2', 'gi0/1'); link('R2', 'gi0/0', 'SRV', PCIF);
  hostIp(get('PC10'), '192.168.10.10', '24', '192.168.10.1'); hostIp(get('PC20'), '192.168.20.10', '24', '192.168.20.1'); hostIp(get('SRV'), '172.16.0.10', '24', '172.16.0.1');
  const k = (n, l) => cliRun(get(n), 'enable\nconf t\nhostname ' + n + '\n' + l + '\nend\nwrite memory');
  k('SW1', 'vlan 10\nname COMPTA\nvlan 20\nname ATELIER\nexit\ninterface fa0/1\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface fa0/2\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface fa0/24\nswitchport mode trunk\nswitchport trunk allowed vlan 10,20');
  k('R1', 'interface gi0/0\nno shutdown\nexit\ninterface gi0/0.10\nencapsulation dot1Q 10\nip address 192.168.10.1 255.255.255.0\nexit\ninterface gi0/0.20\nencapsulation dot1Q 20\nip address 192.168.20.1 255.255.255.0\nexit\ninterface gi0/1\nip address 10.0.0.1 255.255.255.252\nshutdown\nexit\nip route 172.16.0.0 255.255.255.0 10.0.0.2');
  k('R2', 'interface gi0/0\nip address 172.16.0.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 10.0.0.2 255.255.255.252\nno shutdown\nexit\nip route 192.168.10.0 255.255.255.0 10.0.0.1');
}
const repChecks = [
  { label: 'PC10 (COMPTA) joint le serveur 172.16.0.10', run: c => /bytes from/.test(sh(c, 'PC10', 'ping -c 2 172.16.0.10')) },
  { label: 'PC20 (ATELIER) joint sa passerelle 192.168.20.1', run: c => /bytes from/.test(sh(c, 'PC20', 'ping -c 2 192.168.20.1')) },
  { label: 'PC20 (ATELIER) joint le serveur 172.16.0.10', run: c => /bytes from/.test(sh(c, 'PC20', 'ping -c 2 172.16.0.10')) },
  { label: 'Le lien R1–R2 est up/up (show ip interface brief)', run: c => /GigabitEthernet0\/1\s+10\.0\.0\.1\s+YES\s+\w+\s+up\s+up/.test(ios(c, 'R1', 'show ip interface brief')) },
];
function repSolve(sim, h) {
  cliRun(h.get('R1'), 'enable\nconf t\ninterface gi0/1\nno shutdown\nend\nwrite memory');
  cliRun(h.get('SW1'), 'enable\nconf t\ninterface fa0/2\nswitchport access vlan 20\nend\nwrite memory');
  cliRun(h.get('R2'), 'enable\nconf t\nip route 192.168.20.0 255.255.255.0 10.0.0.1\nend\nwrite memory');
}
lab({ id: 'c701-reseau-en-panne', start: D + '7-01-depannage-reseau/tp/c701-reseau-en-panne.json', solution: K + 'C701-reseau-en-panne-corrige.json',
  notes: 'CCNA 7-01 – Réseau en panne : deux VLAN, un routeur sur un bras (R1), une liaison vers R2 et un serveur. Trois pannes indépendantes à trouver méthodiquement (couche 1/2, couche 2, couche 3).',
  build: (sim, h) => repBuild(h), solve: repSolve, checks: repChecks, startShould: [repChecks[0].label, repChecks[1].label, repChecks[2].label, repChecks[3].label] });

const want = process.argv.slice(2); let all = true;
TPS.filter(t => !want.length || want.includes(t.id)).forEach(t => { all = L.run(t) && all; });
process.exit(all ? 0 : 1);
