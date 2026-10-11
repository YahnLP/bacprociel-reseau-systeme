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
const want = process.argv.slice(2);
let all = true;
TPS.filter(t => !want.length || want.includes(t.id)).forEach(t => { all = L.run(t) && all; });
process.exit(all ? 0 : 1);
