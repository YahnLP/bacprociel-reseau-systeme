/* TP du simulateur – Première. Lancer : node tools/tp/premiere.js [id ...]
   Même principe que seconde.js : départ (docs/premiere/…/tp/*.json), corrigé (corriges/premiere/…), vérifications par le moteur. */
const L = require('./lib');
const C = require('./common');
const { hostIp, hostDhcp, hostIpWifi, cliRun, shell, IP } = L;
const D = 'docs/premiere/', K = 'corriges/premiere/';
const TPS = [];

/* ---------- S02 : découverte du simulateur ---------- */
TPS.push({
  id: 'p02-decouverte', start: D + 'S02-remise-a-niveau-simulateur/tp/p02-decouverte.json', solution: K + 'P02-decouverte-corrige.json',
  notes: 'Première S02 – Découverte du simulateur : un petit réseau 192.168.10.0/24 ; PC2 n\'est ni câblé ni configuré.',
  build(sim, { dev, link, get }) {
    dev('sw-8p', 'SW1', 420, 150); dev('pc-win', 'PC1', 220, 70); dev('pc-win', 'PC2', 220, 270); dev('srv-linux', 'SRV1', 620, 150);
    link('PC1', 'eth0', 'SW1', 'port1'); link('SRV1', 'ens33', 'SW1', 'port2');
    hostIp(get('PC1'), '192.168.10.11'); hostIp(get('SRV1'), '192.168.10.100');
  },
  solve(sim, { link, get }) { link('PC2', 'eth0', 'SW1', 'port3'); hostIp(get('PC2'), '192.168.10.12'); },
  checks: [
    { label: 'PC1 joint SRV1', run: c => c.ping('PC1', '192.168.10.100') },
    { label: 'PC2 joint SRV1', run: c => c.ping('PC2', '192.168.10.100') },
    { label: 'PC2 joint PC1', run: c => c.ping('PC2', '192.168.10.11') },
  ],
  startShould: ['PC2 joint SRV1', 'PC2 joint PC1'],
});


/* ---------- S03 : les couches (réseau observé à la loupe) ---------- */
function r1941(h, name, x, y, cfg) { const r = h.dev('r-1941', name, x, y); cliRun(r, 'enable\nconf t\n' + cfg + '\nend'); return r; }
TPS.push({
  id: 'p03-couches', start: D + 'S03-couches-wireshark/tp/p03-couches.json', solution: null,
  notes: 'Première S03 – Deux réseaux reliés par un routeur : LAN 192.168.10.0/24 (PC1, PC2, SW1) et réseau serveur 192.168.20.0/24 (SRV2). On observe les trames avec l\'analyseur.',
  build(sim, h) {
    const { dev, link, get } = h;
    dev('sw-8p', 'SW1', 380, 170); dev('pc-win', 'PC1', 190, 80); dev('pc-win', 'PC2', 190, 260);
    r1941(h, 'R1', 580, 170, 'interface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 192.168.20.1 255.255.255.0\nno shutdown');
    dev('srv-linux', 'SRV2', 780, 170);
    link('PC1', 'eth0', 'SW1', 'port1'); link('PC2', 'eth0', 'SW1', 'port2'); link('SW1', 'port3', 'R1', 'gi0/0'); link('SRV2', 'ens33', 'R1', 'gi0/1');
    hostIp(get('PC1'), '192.168.10.11', '24', '192.168.10.1'); hostIp(get('PC2'), '192.168.10.12', '24', '192.168.10.1'); hostIp(get('SRV2'), '192.168.20.100', '24', '192.168.20.1');
  },
  checks: [
    { label: 'PC1 joint PC2 (même réseau)', run: c => c.ping('PC1', '192.168.10.12') },
    { label: 'PC1 joint SRV2 (à travers le routeur)', run: c => c.ping('PC1', '192.168.20.100') },
  ],
});

/* ---------- S04 : protocoles usuels (DHCP, DNS, HTTP/TCP) ---------- */
TPS.push({
  id: 'p04-protocoles', start: D + 'S04-protocoles-usuels/tp/p04-protocoles.json', solution: null,
  notes: 'Première S04 – PC1 branché directement sur la box : on observe DHCP, DNS, TCP et HTTP avec l\'analyseur (www.exemple.fr).',
  build(sim, h) {
    const { dev, link, get } = h;
    C.internet(sim, h, 800, 170); C.box(sim, h, 'BOX', 560, 170);
    dev('pc-win', 'PC1', 330, 170); link('PC1', 'eth0', 'BOX', 'lan1'); hostDhcp(get('PC1'));
    dev('pc-linux', 'PC2', 330, 330); link('PC2', 'ens33', 'BOX', 'lan2'); hostDhcp(get('PC2'));
  },
  checks: [
    { label: 'PC1 ouvre www.exemple.fr', run: c => { c.wait(8000); const r = c.http('PC1', 'http://www.exemple.fr'); return !!r && r.status === 200; } },
    { label: 'PC1 a une adresse DHCP', run: c => /^192\.168\.1\./.test(c.ipOf('PC1')) },
  ],
});

/* ---------- S05 : switch administrable (Catalyst 2960) ---------- */
const show = (c, dev, cmd) => {
  const s = dev.newSession(); let out = '', done = false; const io = { print: t => { out += t; }, done: () => { done = true; }, clear() { } };
  const go = l => { done = false; out = ''; s.exec(l, io); c.sim.runUntil(() => done, 60000); };
  go('enable'); go('Cisco123');
  go(cmd); return out;
};
const swdev = c => Array.from(c.sim.devices.values()).find(d => d.model === 'sw-2960');
const SW_CFG = 'enable\nconfigure terminal\n';
TPS.push({
  id: 'p05-switch', start: D + 'S05-switch-administrable/tp/p05-switch.json', solution: K + 'P05-switch-corrige.json',
  notes: 'Première S05 – Un switch Cisco 2960 neuf (configuration d\'usine) relie 3 PC et un serveur : à nommer, sécuriser, documenter et administrer à distance.',
  build(sim, h) {
    const { dev, link, get } = h;
    dev('sw-2960', 'SW1', 420, 180, 'Switch de l\'atelier');
    dev('pc-win', 'PC1', 200, 60, 'Compta'); dev('pc-win', 'PC2', 200, 180, 'Atelier'); dev('pc-win', 'PC3', 200, 300, 'Accueil'); dev('srv-linux', 'SRV1', 650, 180, 'Serveur');
    link('PC1', 'eth0', 'SW1', 'Fa0/1'); link('PC2', 'eth0', 'SW1', 'Fa0/2'); link('PC3', 'eth0', 'SW1', 'Fa0/3'); link('SRV1', 'ens33', 'SW1', 'Gi0/1');
    hostIp(get('PC1'), '192.168.10.11', '24', '192.168.10.1'); hostIp(get('PC2'), '192.168.10.12', '24', '192.168.10.1'); hostIp(get('PC3'), '192.168.10.13', '24', '192.168.10.1'); hostIp(get('SRV1'), '192.168.10.100', '24', '192.168.10.1');
  },
  solve(sim, h) {
    cliRun(h.get('SW1'), SW_CFG + 'hostname SW-ATELIER\nenable secret Cisco123\nbanner motd #Acces reserve au personnel#\n' +
      'interface vlan 1\nip address 192.168.10.2 255.255.255.0\nno shutdown\nexit\nip default-gateway 192.168.10.1\n' +
      'interface fa0/1\ndescription PC-COMPTA\nexit\ninterface fa0/2\ndescription PC-ATELIER\nexit\ninterface fa0/3\ndescription PC-ACCUEIL\nexit\ninterface gi0/1\ndescription SERVEUR\nexit\n' +
      'interface range fa0/4 - 24\nshutdown\nexit\n' +
      'ip domain-name atelier.local\nusername admin privilege 15 secret Adm1n!\ncrypto key generate rsa modulus 1024\nip ssh version 2\n' +
      'line vty 0 4\ntransport input ssh\nlogin local\nexit\nend\nwrite memory');
  },
  checks: [
    { label: 'Le switch s\'appelle SW-ATELIER', run: c => /hostname SW-ATELIER/.test(show(c, swdev(c), 'show running-config')) },
    { label: 'Mot de passe enable chiffré (enable secret)', run: c => /enable secret/.test(show(c, swdev(c), 'show running-config')) },
    { label: 'Les ports utilisés ont une description', run: c => { const r = show(c, swdev(c), 'show running-config'); return /description PC-COMPTA/.test(r) && /description SERVEUR/.test(r); } },
    { label: 'Les ports libres Fa0/4 à Fa0/24 sont désactivés', run: c => /FastEthernet0\/24\n shutdown/.test(show(c, swdev(c), 'show running-config')) },
    { label: 'PC1 joint le switch (192.168.10.2)', run: c => { c.wait(3000); return c.ping('PC1', '192.168.10.2'); } },
    { label: 'PC1 joint toujours le serveur', run: c => c.ping('PC1', '192.168.10.100') },
  ],
  startShould: ['Le switch s\'appelle SW-ATELIER', 'Mot de passe enable chiffré (enable secret)', 'Les ports utilisés ont une description', 'Les ports libres Fa0/4 à Fa0/24 sont désactivés', 'PC1 joint le switch (192.168.10.2)'],
});

/* ---------- S06 : sous-réseaux ---------- */
TPS.push({
  id: 'p06-sousreseaux', start: D + 'S06-sous-reseaux/tp/p06-sousreseaux.json', solution: K + 'P06-sousreseaux-corrige.json',
  notes: 'Première S06 – Le réseau 192.168.1.0/24 est découpé en /26 : PC1 et PC2 dans le sous-réseau A (192.168.1.0/26), PC3 et PC4 dans le B (192.168.1.64/26). Deux erreurs : PC2 a une adresse du sous-réseau B ; PC4 a un mauvais masque (/24).',
  build(sim, h) {
    const { dev, link, get } = h;
    dev('sw-8p', 'SW1', 420, 180, 'Switch');
    dev('pc-win', 'PC1', 200, 60, 'PC1 (A)'); dev('pc-win', 'PC2', 200, 180, 'PC2 (A)'); dev('pc-win', 'PC3', 200, 300, 'PC3 (B)'); dev('pc-win', 'PC4', 640, 180, 'PC4 (B)');
    ['PC1', 'PC2', 'PC3', 'PC4'].forEach((n, k) => link(n, 'eth0', 'SW1', 'port' + (k + 1)));
    hostIp(get('PC1'), '192.168.1.10', '26'); hostIp(get('PC2'), '192.168.1.70', '26'); hostIp(get('PC3'), '192.168.1.71', '26'); hostIp(get('PC4'), '192.168.1.80', '24');
  },
  solve(sim, h) { hostIp(h.get('PC2'), '192.168.1.20', '26'); hostIp(h.get('PC4'), '192.168.1.80', '26'); },
  checks: [
    { label: 'PC1 joint PC2 (sous-réseau A)', run: c => c.ping('PC1', c.ipOf('PC2')) },
    { label: 'PC2 joint PC1 (sous-réseau A)', run: c => c.ping('PC2', c.ipOf('PC1')) },
    { label: 'PC3 joint PC4 (sous-réseau B)', run: c => c.ping('PC3', c.ipOf('PC4')) },
    { label: 'PC4 joint PC3 (sous-réseau B)', run: c => c.ping('PC4', c.ipOf('PC3')) },
    { label: 'PC1 ne joint PAS PC3 (sous-réseaux séparés, pas de routeur)', run: c => !c.ping('PC1', '192.168.1.71') },
  ],
  startShould: ['PC1 joint PC2 (sous-réseau A)', 'PC2 joint PC1 (sous-réseau A)'],
});

/* ---------- S07 : routeur et routage statique ---------- */
const R_CFG = 'enable\nconfigure terminal\n';
const rshow = (c, name, cmd) => { const d = c.sim.devices.values ? Array.from(c.sim.devices.values()).find(x => x.name === name) : null; const s = d.newSession(); let out = '', done = false; const io = { print: t => { out += t; }, done: () => { done = true; }, clear() { } }; const go = l => { done = false; out = ''; s.exec(l, io); c.sim.runUntil(() => done, 60000); }; go('enable'); go(cmd); return out; };
TPS.push({
  id: 'p07-routage', start: D + 'S07-routeur-routage-statique/tp/p07-routage.json', solution: K + 'P07-routage-corrige.json',
  notes: 'Première S07 – Deux agences reliées par deux routeurs : LAN A 192.168.10.0/24 (R1), LAN B 192.168.20.0/24 (R2), lien 10.0.0.0/30. Les routeurs sont neufs : interfaces éteintes, pas de route.',
  build(sim, h) {
    const { dev, link, get } = h;
    dev('pc-win', 'PC1', 100, 80, 'PC1'); dev('pc-win', 'PC2', 100, 260, 'PC2'); dev('sw-8p', 'SW-A', 280, 170, 'Switch A');
    dev('r-1941', 'R1', 450, 170, 'R1 (agence)'); dev('r-1941', 'R2', 700, 170, 'R2 (siège)'); dev('sw-8p', 'SW-B', 880, 170, 'Switch B'); dev('srv-linux', 'SRV1', 1050, 170, 'Serveur');
    link('PC1', 'eth0', 'SW-A', 'port1'); link('PC2', 'eth0', 'SW-A', 'port2'); link('SW-A', 'port3', 'R1', 'gi0/0');
    link('R1', 'gi0/1', 'R2', 'gi0/1'); link('R2', 'gi0/0', 'SW-B', 'port1'); link('SRV1', 'ens33', 'SW-B', 'port2');
    hostIp(get('PC1'), '192.168.10.11', '24', '192.168.10.1'); hostIp(get('PC2'), '192.168.10.12', '24', '192.168.10.1'); hostIp(get('SRV1'), '192.168.20.100', '24', '192.168.20.1');
  },
  solve(sim, h) {
    cliRun(h.get('R1'), R_CFG + 'hostname R1\ninterface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 10.0.0.1 255.255.255.252\nno shutdown\nexit\nip route 192.168.20.0 255.255.255.0 10.0.0.2\nend\nwrite memory');
    cliRun(h.get('R2'), R_CFG + 'hostname R2\ninterface gi0/0\nip address 192.168.20.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 10.0.0.2 255.255.255.252\nno shutdown\nexit\nip route 192.168.10.0 255.255.255.0 10.0.0.1\nend\nwrite memory');
  },
  checks: [
    { label: 'PC1 joint sa passerelle R1', run: c => c.ping('PC1', '192.168.10.1') },
    { label: 'R1 joint R2 (10.0.0.2)', run: c => /!!|Success rate is [1-9]/.test(rshow(c, 'R1', 'ping 10.0.0.2')) },
    { label: 'PC1 joint SRV1', run: c => c.ping('PC1', '192.168.20.100') },
    { label: 'SRV1 joint PC2', run: c => c.ping('SRV1', '192.168.10.12') },
    { label: 'R1 a une route statique vers 192.168.20.0', run: c => /^S\s+192\.168\.20\.0/m.test(rshow(c, 'R1', 'show ip route')) },
  ],
  startShould: ['PC1 joint sa passerelle R1', 'R1 joint R2 (10.0.0.2)', 'PC1 joint SRV1', 'SRV1 joint PC2', 'R1 a une route statique vers 192.168.20.0'],
});

/* ---------- S08 : VLAN (1) ---------- */
const VLAN_OK = 'enable\nconfigure terminal\nvlan 10\nname DIRECTION\nvlan 20\nname ATELIER\ninterface range fa0/1 - 2\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface range fa0/3 - 4\nswitchport mode access\nswitchport access vlan 20\nend\nwrite memory';
function vlanBuild(h, ips) {
  const { dev, link, get } = h;
  dev('sw-2960', 'SW1', 440, 190, 'Switch (atelier)');
  const noms = [['PC1', 'Direction 1'], ['PC2', 'Direction 2'], ['PC3', 'Atelier 1'], ['PC4', 'Atelier 2']];
  noms.forEach(([n, l], k) => { dev('pc-win', n, 180, 40 + k * 100, l); link(n, 'eth0', 'SW1', 'Fa0/' + (k + 1)); hostIp(get(n), ips[k], '24'); });
}
const vsh = (c, cmd) => show(c, swdev(c), cmd);
TPS.push({
  id: 'p08-vlan', start: D + 'S08-vlan-1/tp/p08-vlan.json', solution: K + 'P08-vlan-corrige.json',
  notes: 'Première S08 – Quatre PC sur un switch 2960 d\'usine : tout le monde est dans le VLAN 1 et se voit. À séparer : Direction (PC1, PC2) et Atelier (PC3, PC4).',
  build(sim, h) { vlanBuild(h, ['192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14']); },
  solve(sim, h) { cliRun(h.get('SW1'), VLAN_OK); },
  checks: [
    { label: 'PC1 joint PC2 (Direction)', run: c => c.ping('PC1', '192.168.1.12') },
    { label: 'PC3 joint PC4 (Atelier)', run: c => c.ping('PC3', '192.168.1.14') },
    { label: 'PC1 ne joint PAS PC3 (VLAN différents)', run: c => !c.ping('PC1', '192.168.1.13') },
    { label: 'VLAN 10 DIRECTION et VLAN 20 ATELIER existent', run: c => { const r = vsh(c, 'show vlan brief'); return /10\s+DIRECTION\s+active\s+Fa0\/1, Fa0\/2/.test(r) && /20\s+ATELIER\s+active\s+Fa0\/3, Fa0\/4/.test(r); } },
  ],
  startShould: ['PC1 ne joint PAS PC3 (VLAN différents)', 'VLAN 10 DIRECTION et VLAN 20 ATELIER existent'],
});
TPS.push({
  id: 'p08-vlan-panne', start: D + 'S08-vlan-1/tp/p08-vlan-panne.json', solution: K + 'P08-vlan-panne-corrige.json',
  notes: 'Première S08 – Dépannage : VLAN 10 et 20 créés, mais deux ports sont mal affectés (Fa0/2 est dans le VLAN 20 ; Fa0/4 est resté dans le VLAN 1).',
  build(sim, h) {
    vlanBuild(h, ['192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14']);
    cliRun(h.get('SW1'), 'enable\nconfigure terminal\nvlan 10\nname DIRECTION\nvlan 20\nname ATELIER\ninterface fa0/1\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface fa0/2\nswitchport mode access\nswitchport access vlan 20\nexit\ninterface fa0/3\nswitchport mode access\nswitchport access vlan 20\nend');
  },
  solve(sim, h) { cliRun(h.get('SW1'), 'enable\nconfigure terminal\ninterface fa0/2\nswitchport access vlan 10\nexit\ninterface fa0/4\nswitchport mode access\nswitchport access vlan 20\nend\nwrite memory'); },
  checks: [
    { label: 'PC1 joint PC2 (Direction)', run: c => c.ping('PC1', '192.168.1.12') },
    { label: 'PC3 joint PC4 (Atelier)', run: c => c.ping('PC3', '192.168.1.14') },
    { label: 'PC1 ne joint PAS PC3', run: c => !c.ping('PC1', '192.168.1.13') },
  ],
  startShould: ['PC1 joint PC2 (Direction)', 'PC3 joint PC4 (Atelier)'],
});

/* ---------- S09 : VLAN (2) – deux switchs et trunk ---------- */
const VL_CFG = 'enable\nconfigure terminal\nvlan 10\nname DIRECTION\nvlan 20\nname ATELIER\ninterface fa0/1\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface fa0/2\nswitchport mode access\nswitchport access vlan 20\nend';
function trunkBuild(h) {
  const { dev, link, get } = h;
  dev('sw-2960', 'SW1', 330, 190, 'SW1 (bâtiment A)'); dev('sw-2960', 'SW2', 620, 190, 'SW2 (bâtiment B)');
  dev('pc-win', 'PC1', 120, 70, 'Direction A'); dev('pc-win', 'PC2', 120, 310, 'Atelier A'); dev('pc-win', 'PC3', 840, 70, 'Direction B'); dev('pc-win', 'PC4', 840, 310, 'Atelier B');
  link('PC1', 'eth0', 'SW1', 'Fa0/1'); link('PC2', 'eth0', 'SW1', 'Fa0/2'); link('PC3', 'eth0', 'SW2', 'Fa0/1'); link('PC4', 'eth0', 'SW2', 'Fa0/2'); link('SW1', 'Gi0/1', 'SW2', 'Gi0/1');
  hostIp(get('PC1'), '192.168.10.11', '24'); hostIp(get('PC3'), '192.168.10.12', '24'); hostIp(get('PC2'), '192.168.20.11', '24'); hostIp(get('PC4'), '192.168.20.12', '24');
  cliRun(get('SW1'), VL_CFG); cliRun(get('SW2'), VL_CFG);
}
const swn = (c, n) => Array.from(c.sim.devices.values()).find(d => d.name === n);
const TRK = 'enable\nconfigure terminal\ninterface gi0/1\nswitchport mode trunk\nend\nwrite memory';
const trunkChecks = [
  { label: 'PC1 joint PC3 (Direction, à travers le trunk)', run: c => c.ping('PC1', '192.168.10.12') },
  { label: 'PC2 joint PC4 (Atelier, à travers le trunk)', run: c => c.ping('PC2', '192.168.20.12') },
  { label: 'PC1 ne joint PAS PC2 (VLAN séparés)', run: c => !c.ping('PC1', '192.168.20.11') },
];
TPS.push({
  id: 'p09-trunk', start: D + 'S09-vlan-2-trunk/tp/p09-trunk.json', solution: K + 'P09-trunk-corrige.json',
  notes: 'Première S09 – Deux switchs 2960 (bâtiments A et B), VLAN 10 et 20 déjà créés et ports affectés sur chacun. Il reste à relier les deux switchs par un trunk pour que les VLAN traversent.',
  build(sim, h) { trunkBuild(h); },
  solve(sim, h) { cliRun(h.get('SW1'), TRK); cliRun(h.get('SW2'), TRK); },
  checks: trunkChecks.concat([{ label: 'Gi0/1 est un trunk sur SW1', run: c => /Gi0\/1\s+on\s+802\.1q\s+trunking/.test(show(c, swn(c, 'SW1'), 'show interfaces trunk')) }]),
  startShould: ['PC1 joint PC3 (Direction, à travers le trunk)', 'PC2 joint PC4 (Atelier, à travers le trunk)', 'Gi0/1 est un trunk sur SW1'],
});
TPS.push({
  id: 'p09-trunk-panne', start: D + 'S09-vlan-2-trunk/tp/p09-trunk-panne.json', solution: K + 'P09-trunk-panne-corrige.json',
  notes: 'Première S09 – Dépannage : le trunk est configuré sur SW1 seulement (SW2 est resté en access) et SW1 n\'autorise que le VLAN 10 sur son trunk.',
  build(sim, h) { trunkBuild(h); cliRun(h.get('SW1'), 'enable\nconfigure terminal\ninterface gi0/1\nswitchport mode trunk\nswitchport trunk allowed vlan 10\nend'); },
  solve(sim, h) { cliRun(h.get('SW2'), TRK); cliRun(h.get('SW1'), 'enable\nconfigure terminal\ninterface gi0/1\nswitchport trunk allowed vlan 10,20\nend\nwrite memory'); },
  checks: trunkChecks,
  startShould: ['PC1 joint PC3 (Direction, à travers le trunk)', 'PC2 joint PC4 (Atelier, à travers le trunk)'],
});

/* ---------- S10 : serveur Linux (partie réseau) ---------- */
function srvBuild(h, gw) {
  const { dev, link, get } = h;
  dev('pc-win', 'PC1', 120, 100, 'Poste admin'); dev('sw-8p', 'SW-A', 280, 100); dev('r-1941', 'R1', 450, 170, 'Routeur'); dev('sw-8p', 'SW-B', 620, 170); dev('srv-linux', 'SRV1', 800, 170, 'Serveur Linux');
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\ninterface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 192.168.20.1 255.255.255.0\nno shutdown\nend');
  link('PC1', 'eth0', 'SW-A', 'port1'); link('SW-A', 'port2', 'R1', 'gi0/0'); link('R1', 'gi0/1', 'SW-B', 'port1'); link('SRV1', 'ens33', 'SW-B', 'port2');
  hostIp(get('PC1'), '192.168.10.11', '24', '192.168.10.1'); hostIp(get('SRV1'), '192.168.20.100', '24', gw);
}
TPS.push({
  id: 'p10-serveur', start: D + 'S10-serveur-linux-ssh/tp/p10-serveur.json', solution: K + 'P10-serveur-corrige.json',
  notes: 'Première S10 – Le serveur Linux SRV1 (192.168.20.100/24) vient d\'être installé : on le joint depuis le poste admin PC1 (192.168.10.0/24) à travers le routeur R1. Il n\'a pas de passerelle : la réponse ne revient pas.',
  build(sim, h) { srvBuild(h, null); },
  solve(sim, h) { h.get('SRV1').setGateway('192.168.20.1'); },
  checks: [
    { label: 'PC1 joint SRV1', run: c => c.ping('PC1', '192.168.20.100') },
    { label: 'SRV1 joint PC1', run: c => c.ping('SRV1', '192.168.10.11') },
  ],
  startShould: ['PC1 joint SRV1', 'SRV1 joint PC1'],
});

/* ---------- S11 : DHCP et DNS sur un serveur ---------- */
const ip4 = x => IP.parse(x), mk24 = IP.parseMask('24');
function dhcpBuild(h) {
  const { dev, link, get } = h;
  dev('sw-8p', 'SW1', 420, 180); dev('r-1941', 'R1', 420, 40, 'Routeur'); dev('srv-linux', 'SRV1', 700, 180, 'Serveur DHCP/DNS');
  dev('pc-win', 'PC1', 180, 90, 'Poste 1'); dev('pc-win', 'PC2', 180, 270, 'Poste 2'); dev('pc-linux', 'PC3', 700, 330, 'Poste 3 (Linux)');
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\ninterface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nend');
  link('R1', 'gi0/0', 'SW1', 'port1'); link('SRV1', 'ens33', 'SW1', 'port2'); link('PC1', 'eth0', 'SW1', 'port3'); link('PC2', 'eth0', 'SW1', 'port4'); link('PC3', 'ens33', 'SW1', 'port5');
  dev('printer', 'IMP', 180, 180, 'Imprimante'); link('IMP', get('IMP').ifaceList()[0].port.name, 'SW1', 'port6'); hostIp(get('IMP'), '192.168.10.30', '24', '192.168.10.1');
  hostIp(get('SRV1'), '192.168.10.2', '24', '192.168.10.1', '192.168.10.2');
  ['PC1', 'PC2', 'PC3'].forEach(n => hostDhcp(get(n)));
}
function dhcpSolve(srv, opts = {}) {
  const d = srv.dhcpd; d.excluded = [[ip4('192.168.10.1'), ip4('192.168.10.49')]];
  d.addPool({ name: 'LAN', net: ip4('192.168.10.0'), mask: mk24, router: ip4('192.168.10.1'), dns: [ip4(opts.dns || '192.168.10.2')], domain: 'mecapro.local', lease: 28800, start: ip4('192.168.10.50'), end: ip4('192.168.10.150') });
  d.enabled = true;
  srv.dnsd.records = [{ name: 'srv.mecapro.local', type: 'A', data: '192.168.10.2' }, { name: 'intranet.mecapro.local', type: 'A', data: opts.intra || '192.168.10.2' }, { name: 'imprimante.mecapro.local', type: 'A', data: '192.168.10.30' }];
  srv.dnsd.start();
}
const dhcpChecks = [
  { label: 'PC1 reçoit une adresse du pool (192.168.10.50 à 150)', run: c => { c.wait(8000); const a = c.ipOf('PC1'); return /^192\.168\.10\.(5\d|[6-9]\d|1[0-4]\d|150)$/.test(a); } },
  { label: 'PC2 reçoit une adresse du pool', run: c => /^192\.168\.10\.(5\d|[6-9]\d|1[0-4]\d|150)$/.test(c.ipOf('PC2')) },
  { label: 'PC1 et PC2 ont des adresses différentes', run: c => c.ipOf('PC1') !== c.ipOf('PC2') },
  { label: 'PC1 résout intranet.mecapro.local en 192.168.10.2', run: c => /192\.168\.10\.2\b/.test(L.shell(c.sim, Array.from(c.sim.devices.values()).find(d => d.name === 'PC1'), 'nslookup intranet.mecapro.local')) && !/\.20\b/.test(L.shell(c.sim, Array.from(c.sim.devices.values()).find(d => d.name === 'PC1'), 'nslookup intranet.mecapro.local')) },
  { label: 'PC1 joint le serveur par son nom', run: c => /octets=/.test(L.shell(c.sim, Array.from(c.sim.devices.values()).find(d => d.name === 'PC1'), 'ping srv.mecapro.local')) },
];
TPS.push({
  id: 'p11-dhcp-dns', start: D + 'S11-dhcp-dns-serveur/tp/p11-dhcp-dns.json', solution: K + 'P11-dhcp-dns-corrige.json',
  notes: 'Première S11 – Le serveur SRV1 (192.168.10.2) n\'a encore aucun service : les postes en DHCP n\'ont pas d\'adresse. À configurer : DHCP (pool 192.168.10.50-150, passerelle .1, DNS .2) et DNS (srv, intranet, imprimante).',
  build(sim, h) { dhcpBuild(h); },
  solve(sim, h) { dhcpSolve(h.get('SRV1')); },
  checks: dhcpChecks,
  startShould: dhcpChecks.filter(x => !/différentes/.test(x.label)).map(x => x.label),
});
TPS.push({
  id: 'p11-dhcp-dns-panne', start: D + 'S11-dhcp-dns-serveur/tp/p11-dhcp-dns-panne.json', solution: K + 'P11-dhcp-dns-panne-corrige.json',
  notes: 'Première S11 – Dépannage : le DHCP et le DNS tournent, mais le pool distribue un mauvais serveur DNS (192.168.10.3) et l\'enregistrement intranet.mecapro.local pointe sur 192.168.10.20 au lieu de .2.',
  build(sim, h) { dhcpBuild(h); dhcpSolve(h.get('SRV1'), { dns: '192.168.10.3', intra: '192.168.10.20' }); },
  solve(sim, h) {
    const s = h.get('SRV1'); const p = s.dhcpd.pools[0]; p.dns = [ip4('192.168.10.2')];
    s.dnsd.records.find(r => r.name === 'intranet.mecapro.local').data = '192.168.10.2';
    ['PC1', 'PC2', 'PC3'].forEach(n => { const pc = h.get(n); const i = pc.ifaceList()[0]; pc.dhcpDns = true; pc.dnsServers = [ip4('192.168.10.2')]; });
  },
  checks: dhcpChecks.slice(3),
  startShould: [dhcpChecks[3].label],
});

/* ---------- S12 : serveur web ---------- */
function webBuild(h) {
  const { dev, link, get } = h;
  dev('sw-8p', 'SW1', 420, 180); dev('srv-linux', 'SRV1', 700, 180, 'Serveur web'); dev('pc-win', 'PC1', 180, 90, 'Poste 1'); dev('pc-win', 'PC2', 180, 270, 'Poste 2');
  link('SRV1', 'ens33', 'SW1', 'port1'); link('PC1', 'eth0', 'SW1', 'port2'); link('PC2', 'eth0', 'SW1', 'port3');
  hostIp(get('SRV1'), '192.168.10.2', '24', '192.168.10.1', '192.168.10.2'); hostIp(get('PC1'), '192.168.10.51', '24', '192.168.10.1', '192.168.10.2'); hostIp(get('PC2'), '192.168.10.52', '24', '192.168.10.1', '192.168.10.2');
  const s = get('SRV1'); s.dnsd.records = [{ name: 'intranet.mecapro.local', type: 'A', data: '192.168.10.2' }]; s.dnsd.start();
}
const INTRA = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Intranet MécaPro</title></head><body><h1>Intranet MécaPro</h1><p>Bienvenue sur l\'intranet de l\'atelier.</p><ul><li><a href="/direction.html">Espace Direction</a></li></ul></body></html>';
const DIR = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Espace Direction</title></head><body><h1>Espace Direction</h1><p>Documents de la Direction.</p></body></html>';
const webGet = (c, url) => { c.wait(3000); const r = c.http('PC1', url); return r; };
const webChecks = [
  { label: 'PC1 ouvre http://intranet.mecapro.local (200)', run: c => { const r = webGet(c, 'http://intranet.mecapro.local'); return !!r && r.status === 200 && /Intranet MécaPro/.test(r.body); } },
  { label: 'La page /direction.html existe', run: c => { const r = webGet(c, 'http://intranet.mecapro.local/direction.html'); return !!r && r.status === 200 && /Espace Direction/.test(r.body); } },
  { label: 'HTTPS (443) fonctionne', run: c => { const r = webGet(c, 'https://intranet.mecapro.local'); return !!r && r.status === 200; } },
];
TPS.push({
  id: 'p12-web', start: D + 'S12-web-partage/tp/p12-web.json', solution: K + 'P12-web-corrige.json',
  notes: 'Première S12 – Le serveur SRV1 (192.168.10.2) a un nom (intranet.mecapro.local) mais son service web est arrêté : à démarrer, à personnaliser (page d\'accueil + page Direction) et à passer en HTTPS.',
  build(sim, h) { webBuild(h); },
  solve(sim, h) { const w = h.get('SRV1').httpd; w.pages['/'] = { type: 'text/html; charset=utf-8', body: INTRA, _custom: true }; w.pages['/direction.html'] = { type: 'text/html; charset=utf-8', body: DIR, _custom: true }; w.https = true; w.start(); },
  checks: webChecks,
  startShould: webChecks.map(x => x.label),
});

/* ---------- S13 : câblage (types de câbles, mode « câbles stricts ») ---------- */
function cablesBuild(sim, h, wrong) {
  const { dev, link, get } = h;
  sim.opts.strictCables = true;
  dev('sw-8p', 'SW1', 330, 180, 'Switch bât. A'); dev('sw-8p', 'SW2', 640, 180, 'Switch bât. B');
  dev('pc-win', 'PC1', 120, 70, 'PC1'); dev('pc-win', 'PC2', 120, 290, 'PC2'); dev('pc-win', 'PC3', 850, 70, 'PC3'); dev('pc-win', 'PC4', 850, 290, 'PC4');
  link('PC1', 'eth0', 'SW1', 'port1', wrong ? 'cross' : 'straight'); link('PC2', 'eth0', 'SW1', 'port2', 'straight');
  link('SW1', 'port8', 'SW2', 'port8', wrong ? 'straight' : 'cross');
  link('PC3', 'eth0', 'SW2', 'port1', wrong ? 'fiber' : 'straight'); link('PC4', 'eth0', 'SW2', 'port2', 'straight');
  [['PC1', '11'], ['PC2', '12'], ['PC3', '13'], ['PC4', '14']].forEach(([n, k]) => hostIp(get(n), '192.168.10.' + k, '24'));
}
const cabChecks = [
  { label: 'PC1 joint PC2 (même switch)', run: c => c.ping('PC1', '192.168.10.12') },
  { label: 'PC3 joint PC4 (même switch)', run: c => c.ping('PC3', '192.168.10.14') },
  { label: 'PC1 joint PC3 (à travers le lien entre switchs)', run: c => c.ping('PC1', '192.168.10.13') },
  { label: 'PC2 joint PC4 (à travers le lien entre switchs)', run: c => c.ping('PC2', '192.168.10.14') },
];
TPS.push({
  id: 'p13-cables', start: D + 'S13-cuivre-fibre-securite/tp/p13-cables.json', solution: K + 'P13-cables-corrige.json',
  notes: 'Première S13 – Câblage : mode « câbles stricts ». Trois câbles sont du mauvais type : PC1–SW1 (croisé au lieu de droit), SW1–SW2 (droit au lieu de croisé) et PC3–SW2 (fibre sur un port cuivre).',
  build(sim, h) { cablesBuild(sim, h, true); },
  solve(sim, h) {
    sim.links.slice().forEach(l => { if (!l.ok) sim.disconnect(l); });
    const { link } = h; link('PC1', 'eth0', 'SW1', 'port1', 'straight'); link('SW1', 'port8', 'SW2', 'port8', 'cross'); link('PC3', 'eth0', 'SW2', 'port1', 'straight');
  },
  checks: cabChecks,
  startShould: ['PC1 joint PC2 (même switch)', 'PC3 joint PC4 (même switch)', 'PC1 joint PC3 (à travers le lien entre switchs)', 'PC2 joint PC4 (à travers le lien entre switchs)'],
});

/* ---------- S14 : sécurité de base ---------- */
function secBuild(h) {
  const { dev, link, get } = h;
  dev('pc-win', 'PC1', 100, 80, 'Poste atelier'); dev('pc-win', 'PC2', 100, 270, 'Poste compta'); dev('sw-2960', 'SW1', 270, 170, 'Switch');
  dev('r-1941', 'R1', 450, 170, 'Routeur'); dev('sw-8p', 'SWB', 620, 170); dev('srv-linux', 'SRV1', 790, 170, 'Serveur web');
  link('PC1', 'eth0', 'SW1', 'Fa0/1'); link('PC2', 'eth0', 'SW1', 'Fa0/2'); link('SW1', 'Gi0/1', 'R1', 'gi0/0'); link('R1', 'gi0/1', 'SWB', 'port1'); link('SRV1', 'ens33', 'SWB', 'port2');
  cliRun(get('R1'), 'enable\nconf t\nhostname R1\ninterface gi0/0\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface gi0/1\nip address 192.168.20.1 255.255.255.0\nno shutdown\nend');
  cliRun(get('SW1'), 'enable\nconf t\nhostname SW1\ninterface vlan 1\nip address 192.168.10.2 255.255.255.0\nno shutdown\nexit\nip default-gateway 192.168.10.1\nline vty 0 4\npassword cisco\nlogin\ntransport input all\nend');
  hostIp(get('PC1'), '192.168.10.11', '24', '192.168.10.1'); hostIp(get('PC2'), '192.168.10.12', '24', '192.168.10.1'); hostIp(get('SRV1'), '192.168.20.100', '24', '192.168.20.1');
  get('SRV1').httpd.start();
}
const rcfg = (c, n) => rshow(c, n, 'show running-config');
const showPw = (c, dev, cmd, extra) => { for (const pw of (extra || []).concat(['Cisco123', 'cisco'])) { const s = dev.newSession(); let out = '', done = false; const io = { print: t => { out += t; }, done: () => { done = true; }, clear() { } }; const go = l => { done = false; out = ''; s.exec(l, io); c.sim.runUntil(() => done, 60000); }; go('enable'); go(pw); go(cmd); if (out.trim() && !/Invalid|Access denied|Bad secrets/.test(out)) return out; } return ''; };
const swcfg = c => showPw(c, swn(c, 'SW1'), 'show running-config');
const SEC_SW = 'enable\nconfigure terminal\nenable secret Cisco123\nbanner motd #Acces reserve au personnel autorise#\nip domain-name mecapro.local\nusername admin privilege 15 secret Adm1n!\ncrypto key generate rsa modulus 1024\nip ssh version 2\nline vty 0 4\ntransport input ssh\nlogin local\nexit\ninterface range fa0/3 - 24\nshutdown\nend\nwrite memory';
const SEC_R = 'enable\nconfigure terminal\nip access-list extended WEB-ONLY\npermit tcp 192.168.10.0 0.0.0.255 host 192.168.20.100 eq 80\npermit tcp 192.168.10.0 0.0.0.255 host 192.168.20.100 eq 443\ndeny ip any any log\nexit\ninterface gi0/0\nip access-group WEB-ONLY in\nend\nwrite memory';
const secChecks = [
  { label: 'Switch : mot de passe enable chiffré (enable secret)', run: c => /enable secret/.test(swcfg(c)) },
  { label: 'Switch : SSH seulement sur les lignes distantes', run: c => /transport input ssh/.test(swcfg(c)) },
  { label: 'Switch : bannière d\'avertissement', run: c => /banner motd/.test(swcfg(c)) },
  { label: 'Switch : ports Fa0/3 à Fa0/24 désactivés', run: c => /FastEthernet0\/24\n shutdown/.test(swcfg(c)) },
  { label: 'Switch : configuration sauvegardée', run: c => /hostname SW1/.test(showPw(c, swn(c, 'SW1'), 'show startup-config')) && /transport input ssh/.test(showPw(c, swn(c, 'SW1'), 'show startup-config')) },
  { label: 'PC1 ouvre le site web du serveur', run: c => { const r = c.http('PC1', 'http://192.168.20.100'); return !!r && r.status === 200; } },
  { label: 'PC1 ne peut PAS faire un ping vers le serveur (filtré)', run: c => !c.ping('PC1', '192.168.20.100') },
];
TPS.push({
  id: 'p14-securite', start: D + 'S14-securite-base/tp/p14-securite.json', solution: K + 'P14-securite-corrige.json',
  notes: 'Première S14 – Un mini-réseau « à auditer » : le switch n\'a pas de mot de passe enable, Telnet est autorisé avec un mot de passe en clair, tous ses ports actifs, pas de bannière ; le routeur laisse tout passer vers le serveur web. À durcir (switch + ACL) puis à sauvegarder.',
  build(sim, h) { secBuild(h); },
  solve(sim, h) { cliRun(h.get('SW1'), SEC_SW); cliRun(h.get('R1'), SEC_R); },
  checks: secChecks,
  startShould: secChecks.filter(x => !/ouvre le site/.test(x.label)).map(x => x.label),
});
require('./premiere_proj')(TPS, { L, D, K, hostIp, hostDhcp, hostIpWifi, cliRun, shell, IP, rshow, showPw, swn });
const want = process.argv.slice(2);
let all = true;
TPS.filter(t => !want.length || want.includes(t.id)).forEach(t => { all = L.run(t) && all; });
process.exit(all ? 0 : 1);
