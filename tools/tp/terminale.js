/* TP du simulateur – Terminale. Lancer : node tools/tp/terminale.js [id ...]
   Même principe que premiere.js : départ (docs/terminale/…/tp/*.json), corrigé (corriges/terminale/…), vérifications par le moteur. */
const L = require('./lib');
const C = require('./common');
const { hostIp, hostDhcp, hostIpWifi, cliRun, shell, IP } = L;
const D = 'docs/terminale/', K = 'corriges/terminale/';
const TPS = [];
const ip4 = x => IP.parse(x), m24 = IP.parseMask('24');
const dv = (c, n) => { const a = Array.from(c.sim.devices.values()); return a.find(d => d.name === n) || a.find(d => (d.label || '') === n || (d.origName || '') === n) || (n === 'SW1' ? a.find(d => d.model === 'sw-2960') : n === 'R1' ? a.find(d => d.model === 'r-2911') : null); };
/* exécute une commande sur un équipement Cisco en essayant des mots de passe enable */
const ios = (c, name, cmd, pws) => {
  const d = dv(c, name);
  for (const pw of (pws || []).concat([''])) {
    const s = d.newSession(); let out = '', done = false; const io = { print: t => { out += t; }, done: () => { done = true; }, clear() { } };
    const go = l => { done = false; out = ''; s.exec(l, io); c.sim.runUntil(() => done, 60000); };
    go('enable'); if (pw) go(pw); go(cmd);
    if (out.trim() && !/Invalid|Access denied|Bad secrets|Password/.test(out)) return out;
  }
  return '';
};
const PW = ['Cabinet#2026', 'Archi#2027', 'Cisco123', 'cisco', 'Pme#2027', 'Vidal#2027', 'Marchand#2027', 'Pasquier#2027'];
const cfg = (c, n) => ios(c, n, 'show running-config', PW);
const scfg = (c, n) => ios(c, n, 'show startup-config', PW);

/* ---------- S01 : mini-chantier de positionnement (cabinet médical) ---------- */
function cabBuild(h) {
  const { dev } = h;
  dev('pc-win', 'PC1', 100, 80, 'Secrétariat'); dev('pc-win', 'PC2', 100, 250, 'Médecin'); dev('printer', 'IMP', 250, 380, 'Imprimante');
  dev('sw-2960', 'SW1', 330, 180, 'Switch'); dev('srv-linux', 'SRV', 560, 180, 'Serveur du cabinet');
  hostDhcp(h.get('PC1')); hostDhcp(h.get('PC2'));
}
const CAB_SW = 'enable\nconfigure terminal\nhostname SW-CABINET\nenable secret Cabinet#2026\nbanner motd #Acces reserve au cabinet#\ninterface range fa0/5 - 24\nshutdown\nexit\ninterface range fa0/1 - 4\ndescription poste\nexit\nend\nwrite memory';
function cabSolve(sim, h) {
  const { link, get } = h;
  link('PC1', 'eth0', 'SW1', 'Fa0/1'); link('PC2', 'eth0', 'SW1', 'Fa0/2'); link('IMP', get('IMP').ifaceList()[0].port.name, 'SW1', 'Fa0/3'); link('SRV', 'ens33', 'SW1', 'Fa0/4');
  cliRun(get('SW1'), CAB_SW);
  hostIp(get('IMP'), '192.168.1.20', '24'); hostIp(get('SRV'), '192.168.1.2', '24', null, '192.168.1.2');
  const s = get('SRV'), d = s.dhcpd; d.excluded = [[ip4('192.168.1.1'), ip4('192.168.1.49')]];
  d.addPool({ name: 'CABINET', net: ip4('192.168.1.0'), mask: m24, router: ip4('192.168.1.1'), dns: [ip4('192.168.1.2')], domain: 'martin.local', lease: 28800, start: ip4('192.168.1.50'), end: ip4('192.168.1.100') });
  d.enabled = true;
  s.dnsd.records = [{ name: 'cabinet.martin.local', type: 'A', data: '192.168.1.2' }, { name: 'imprimante.martin.local', type: 'A', data: '192.168.1.20' }]; s.dnsd.start(); s.httpd.start();
}
const cabChecks = [
  { label: 'PC1 reçoit une adresse du pool (192.168.1.50 à 100)', run: c => { c.wait(10000); return /^192\.168\.1\.(5\d|[6-9]\d|100)$/.test(c.ipOf('PC1')); } },
  { label: 'PC2 reçoit une adresse du pool', run: c => /^192\.168\.1\.(5\d|[6-9]\d|100)$/.test(c.ipOf('PC2')) },
  { label: 'PC1 ouvre http://cabinet.martin.local', run: c => { const r = c.http('PC1', 'http://cabinet.martin.local'); return !!r && r.status === 200; } },
  { label: 'PC1 joint l\'imprimante (192.168.1.20)', run: c => c.ping('PC1', '192.168.1.20') },
  { label: 'Switch : enable secret et bannière', run: c => /enable secret/.test(cfg(c, 'SW1')) && /banner motd/.test(cfg(c, 'SW1')) },
  { label: 'Switch : ports Fa0/5 à Fa0/24 désactivés', run: c => /FastEthernet0\/24\n shutdown/.test(cfg(c, 'SW1')) },
  { label: 'Switch : configuration sauvegardée', run: c => /hostname SW-CABINET/.test(scfg(c, 'SW1')) && /enable secret/.test(scfg(c, 'SW1')) },
];
TPS.push({
  id: 't01-diagnostic', start: D + 'S01-diagnostic-retour/tp/t01-mini-chantier.json', solution: K + 'T01-mini-chantier-corrige.json',
  notes: 'Terminale S01 – Mini-chantier de positionnement : cabinet médical. Matériel posé, aucun câble, aucune configuration. À faire : câbler (4 câbles), configurer switch, serveur (DHCP, DNS, web), imprimante fixe ; tester ; sauvegarder.',
  build(sim, h) { cabBuild(h); }, solve: cabSolve, checks: cabChecks, startShould: cabChecks.map(x => x.label),
});

require('./terminale_b')(TPS, { L, D, K, hostIp, hostDhcp, hostIpWifi, cliRun, shell, IP, ip4, m24, dv, ios, cfg, scfg, PW, C });
require('./terminale_c')(TPS, { L, D, K, hostIp, hostDhcp, hostIpWifi, cliRun, shell, IP, ip4, m24, dv, ios, cfg, scfg, PW, C });
const want = process.argv.slice(2);
let all = true;
TPS.filter(t => !want.length || want.includes(t.id)).forEach(t => { all = L.run(t) && all; });
process.exit(all ? 0 : 1);
