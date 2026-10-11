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
const want = process.argv.slice(2);
let all = true;
TPS.filter(t => !want.length || want.includes(t.id)).forEach(t => { all = L.run(t) && all; });
process.exit(all ? 0 : 1);
