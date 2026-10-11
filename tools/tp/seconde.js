/* TP du simulateur – Seconde. Lancer : node tools/tp/seconde.js [id ...] */
const L = require('./lib');
const { hostIp, hostDhcp } = L;
const D = 'docs/seconde/', C = 'corriges/seconde/';
const TPS = [];

/* S06 – le terminal réseau : deux postes déjà configurés, à interroger */
TPS.push({
  id: 's06-terminal', start: D + 'S06-terminal/tp/s06-terminal-reseau.json', solution: C + 'S06-terminal-reseau-corrige.json',
  notes: 'S06 – Premières commandes réseau : hostname, ipconfig / ip a, ping.',
  build(sim, { dev, link, get }) {
    dev('sw-8p', 'SW1', 400, 130); dev('pc-win', 'PC-WIN', 220, 320); dev('pc-linux', 'PC-LINUX', 580, 320);
    link('PC-WIN', 'eth0', 'SW1', 'port1'); link('PC-LINUX', 'ens33', 'SW1', 'port2');
    hostIp(get('PC-WIN'), '192.168.10.11'); hostIp(get('PC-LINUX'), '192.168.10.12');
  },
  checks: [{ label: 'PC-WIN joint PC-LINUX', run: c => c.ping('PC-WIN', '192.168.10.12') }, { label: 'PC-LINUX joint PC-WIN', run: c => c.ping('PC-LINUX', '192.168.10.11') }],
});

const want = process.argv.slice(2);
let all = true;
TPS.filter(t => !want.length || want.includes(t.id)).forEach(t => { all = L.run(t) && all; });
process.exit(all ? 0 : 1);
