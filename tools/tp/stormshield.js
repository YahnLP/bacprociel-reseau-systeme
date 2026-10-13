/* TP du simulateur – parcours Stormshield. Lancer : SIM_DIR=… node tools/tp/stormshield.js [id ...]
   Départ : docs/stormshield/<module>/tp/*.json ; corrigé : corriges/stormshield/*.json (local). */
const L = require('./lib'); const C = require('./common');
const { hostIp, cliRun, IP } = L;
const D = 'docs/stormshield/', K = 'corriges/stormshield/';
const TPS = []; const lab = TPS.push.bind(TPS);
const dv = (c, n) => Array.from(c.sim.devices.values()).find(d => d.name === n);
const NA = (c, n, ip) => c.ping(n, ip, 2);
const page = (c, from, url) => { const r = c.http(from, url); return !!r && r.status === 200; };

/* Site d'entreprise : LAN (SW1), DMZ (SRVWEB), Internet (FAI). opts.ifaces = false : pare-feu non configuré */
function site(sim, h, o = {}) {
  const { dev, link, get } = h;
  dev('fw-sn210', 'FW1', 380, 200, 'Pare-feu'); dev('sw-8p', 'SW1', 160, 200); dev('pc-win', 'PC-ADMIN', 60, 330, 'Admin'); dev('pc-win', 'PC-STAGIAIRE', 200, 330, 'Stagiaire');
  dev('srv-linux', 'SRVWEB', 380, 380, 'Serveur web (DMZ)');
  C.internet(sim, h, 640, 200); dev('pc-linux', 'CLIENT', 980, 330, 'Client Internet'); link('CLIENT', 'ens33', 'SW-FAI', 'port4');
  link('SW1', 'port1', 'FW1', 'in'); link('PC-ADMIN', 'eth0', 'SW1', 'port2'); link('PC-STAGIAIRE', 'eth0', 'SW1', 'port3'); link('SRVWEB', 'ens33', 'FW1', 'dmz1'); link('FW1', 'out', 'FAI', 'gi0/0');
  hostIp(get('CLIENT'), '198.51.100.20', '24', '198.51.100.1');
  hostIp(get('PC-ADMIN'), '192.168.1.10', '24', '192.168.1.254'); hostIp(get('PC-STAGIAIRE'), '192.168.1.50', '24', '192.168.1.254');
  const s = get('SRVWEB'); hostIp(s, '172.16.0.10', '24', '172.16.0.254'); s.httpd.start();
  s.httpd.pages['/'] = { type: 'text/html; charset=utf-8', body: '<html><body><h1>Site de l\'entreprise (DMZ)</h1></body></html>', _custom: true };
  const f = get('FW1'); const out = f.ifaceByName('out');
  if (o.ifaces === false) { ['out', 'in', 'dmz1'].forEach(n => { const i = f.ifaceByName(n); f.enableDhcp(i, false); i.ip = 0; i.mask = 0; }); f.statics = f.statics.filter(x => !(x.net === 0 && x.mask === 0)); }
  else { f.enableDhcp(out, false); out.ip = IP.parse('203.0.113.2'); out.mask = IP.parseMask('29'); f.statics = f.statics.filter(x => !(x.net === 0 && x.mask === 0)); f.statics.push({ net: 0, mask: 0, nh: IP.parse('203.0.113.1'), iface: null, ad: 1 }); }
}
const setIfaces = f => {
  [['in', '192.168.1.254', '24'], ['dmz1', '172.16.0.254', '24'], ['out', '203.0.113.2', '29']].forEach(([n, ip, m]) => { const i = f.ifaceByName(n); f.enableDhcp(i, false); i.ip = IP.parse(ip); i.mask = IP.parseMask(m); });
  f.statics = f.statics.filter(x => !(x.net === 0 && x.mask === 0)); f.statics.push({ net: 0, mask: 0, nh: IP.parse('203.0.113.1'), iface: null, ad: 1 }); f.rebuildNat();
};
const R = (action, from, to, proto, src, dst, dport, comment) => ({ on: true, action, from, to, proto, src, dst, dport, comment });

/* ---------- S02 : lire le journal ---------- */
const s02 = [
  { label: 'PC-ADMIN fait un ping vers le serveur de la DMZ', run: c => NA(c, 'PC-ADMIN', '172.16.0.10') },
  { label: 'PC-STAGIAIRE ne peut PAS faire de ping vers le serveur de la DMZ', run: c => !NA(c, 'PC-STAGIAIRE', '172.16.0.10') },
  { label: 'PC-STAGIAIRE ouvre toujours le site web de la DMZ', run: c => page(c, 'PC-STAGIAIRE', 'http://172.16.0.10') },
];
lab({ id: 's02-journaux', start: D + 's02-journaux-supervision/tp/s02-journaux.json', solution: K + 'S02-journaux-corrige.json',
  notes: 'Stormshield S02 – Journaux : le LAN peut seulement ouvrir le site web de la DMZ. PC-ADMIN doit pouvoir faire un ping vers le serveur (supervision), pas PC-STAGIAIRE.',
  build: (sim, h) => { site(sim, h); const f = h.get('FW1'); f.rules = [R('pass', 'LAN', 'WAN', 'tcp', 'any', 'any', '80,443', 'Navigation web'), R('pass', 'LAN', 'DMZ', 'tcp', 'any', 'any', '80', 'Site de la DMZ')]; f.natMasq = [{ from: 'LAN', to: 'WAN' }]; f.rebuildNat(); },
  solve: (sim, h) => { const f = h.get('FW1'); f.rules.splice(1, 0, R('pass', 'LAN', 'DMZ', 'icmp', '192.168.1.10/32', 'any', 'any', 'Ping de supervision depuis PC-ADMIN')); },
  checks: s02, startShould: [s02[0].label] });

/* ---------- S04 : configuration réseau ---------- */
const s04 = [
  { label: 'FW1 : interface IN en 192.168.1.254/24', run: c => { const i = dv(c, 'FW1').ifaceByName('in'); return IP.str(i.ip) === '192.168.1.254' && IP.prefixFromMask(i.mask) === 24; } },
  { label: 'FW1 : interface DMZ1 en 172.16.0.254/24', run: c => { const i = dv(c, 'FW1').ifaceByName('dmz1'); return IP.str(i.ip) === '172.16.0.254' && IP.prefixFromMask(i.mask) === 24; } },
  { label: 'FW1 : interface OUT en 203.0.113.2/29 avec passerelle 203.0.113.1', run: c => { const f = dv(c, 'FW1'), i = f.ifaceByName('out'); return !!i.ip && IP.str(i.ip) === '203.0.113.2' && f.statics.some(x => x.net === 0 && x.mask === 0 && IP.str(x.nh) === '203.0.113.1'); } },
  { label: 'PC-ADMIN ouvre le site de la DMZ', run: c => page(c, 'PC-ADMIN', 'http://172.16.0.10') },
  { label: 'PC-ADMIN ouvre le site web d\'Internet (198.51.100.80)', run: c => page(c, 'PC-ADMIN', 'http://198.51.100.80') },
];
lab({ id: 's04-reseau', start: D + 's04-configuration-reseau/tp/s04-reseau.json', solution: K + 'S04-reseau-corrige.json',
  notes: 'Stormshield S04 – Configuration réseau : un pare-feu SN210 sorti de sa boîte, câblé, sans adresse. Plan : LAN 192.168.1.0/24, DMZ 172.16.0.0/24, WAN 203.0.113.0/29 (FAI : 203.0.113.1).',
  build: (sim, h) => site(sim, h, { ifaces: false }), solve: (sim, h) => setIfaces(h.get('FW1')), checks: s04, startShould: s04.map(x => x.label) });

/* ---------- S05 : NAT ---------- */
const s05 = [
  { label: 'PC-ADMIN accède à Internet (masquerade LAN → WAN)', run: c => page(c, 'PC-ADMIN', 'http://198.51.100.80') },
  { label: 'Le client Internet ouvre le site de la DMZ sur http://203.0.113.2', run: c => page(c, 'CLIENT', 'http://203.0.113.2') },
  { label: 'La redirection 80 → 172.16.0.10:80 existe', run: c => dv(c, 'FW1').forwards.some(f => f.port === 80 && f.toIp === '172.16.0.10' && (f.toPort || f.port) === 80) },
];
lab({ id: 's05-nat', start: D + 's05-nat/tp/s05-nat.json', solution: K + 'S05-nat-corrige.json',
  notes: 'Stormshield S05 – NAT : le pare-feu est configuré mais sans aucune règle de NAT. À faire : masquerade du LAN vers Internet, et publication du site web de la DMZ via l’adresse publique du pare-feu (port 80).',
  build: (sim, h) => { site(sim, h); const f = h.get('FW1'); f.rules = [R('pass', 'LAN', 'WAN', 'any', 'any', 'any', 'any', 'LAN vers Internet'), R('pass', 'LAN', 'DMZ', 'tcp', 'any', 'any', '80', 'Site de la DMZ'), R('pass', 'WAN', 'DMZ', 'tcp', 'any', 'any', '80', 'Publication du site')]; f.natMasq = []; f.forwards = []; f.rebuildNat(); },
  solve: (sim, h) => { const f = h.get('FW1'); f.natMasq = [{ from: 'LAN', to: 'WAN' }]; f.forwards = [{ proto: 'tcp', port: 80, toIp: '172.16.0.10', toPort: 80 }]; f.rebuildNat(); f.ifaceByName('dmz1').nat = 'inside'; },
  checks: s05, startShould: [s05[0].label, s05[1].label, s05[2].label] });

/* ---------- S06 : filtrage ---------- */
const s06 = [
  { label: 'PC-ADMIN ouvre le site web d\'Internet', run: c => page(c, 'PC-ADMIN', 'http://198.51.100.80') },
  { label: 'PC-STAGIAIRE ne peut PAS ouvrir le site web d\'Internet', run: c => !page(c, 'PC-STAGIAIRE', 'http://198.51.100.80') },
  { label: 'PC-ADMIN ne peut PAS faire de ping vers Internet (seul le web est autorisé)', run: c => !NA(c, 'PC-ADMIN', '198.51.100.80') },
  { label: 'PC-ADMIN ouvre le site de la DMZ', run: c => page(c, 'PC-ADMIN', 'http://172.16.0.10') },
];
lab({ id: 's06-filtrage', start: D + 's06-filtrage/tp/s06-filtrage.json', solution: K + 'S06-filtrage-corrige.json',
  notes: 'Stormshield S06 – Filtrage : politique permissive et mal ordonnée. À faire : bloquer PC-STAGIAIRE (192.168.1.50) vers Internet, ne laisser sortir que le web (80, 443) et le DNS, garder l\'accès à la DMZ en HTTP.',
  build: (sim, h) => { site(sim, h); const f = h.get('FW1'); f.rules = [R('pass', 'LAN', 'WAN', 'any', 'any', 'any', 'any', 'LAN vers Internet (trop large)'), R('block', 'LAN', 'WAN', 'any', '192.168.1.50/32', 'any', 'any', 'Stagiaire bloqué'), R('pass', 'LAN', 'DMZ', 'tcp', 'any', 'any', '80', 'Site de la DMZ')]; f.natMasq = [{ from: 'LAN', to: 'WAN' }]; f.rebuildNat(); },
  solve: (sim, h) => { const f = h.get('FW1'); f.rules = [R('block', 'LAN', 'WAN', 'any', '192.168.1.50/32', 'any', 'any', 'Stagiaire bloqué'), R('pass', 'LAN', 'WAN', 'tcp', 'any', 'any', '80,443', 'Navigation web'), R('pass', 'LAN', 'WAN', 'udp', 'any', 'any', '53', 'DNS'), R('pass', 'LAN', 'DMZ', 'tcp', 'any', 'any', '80', 'Site de la DMZ')]; },
  checks: s06, startShould: [s06[1].label, s06[2].label] });

/* ---------- S11 : site en panne (trois pannes à diagnostiquer) ---------- */
const s11 = [
  { label: 'PC-ADMIN ouvre le site web d\'Internet', run: c => page(c, 'PC-ADMIN', 'http://198.51.100.80') },
  { label: 'PC-STAGIAIRE ne peut PAS ouvrir le site web d\'Internet', run: c => !page(c, 'PC-STAGIAIRE', 'http://198.51.100.80') },
  { label: 'Le client Internet ouvre le site de la DMZ sur http://203.0.113.2', run: c => page(c, 'CLIENT', 'http://203.0.113.2') },
  { label: 'PC-ADMIN ouvre le site de la DMZ', run: c => page(c, 'PC-ADMIN', 'http://172.16.0.10') },
];
lab({ id: 's11-site-en-panne', start: D + 's11-depannage/tp/s11-site-en-panne.json', solution: K + 'S11-site-en-panne-corrige.json',
  notes: 'Stormshield S11 – Site en panne : un pare-feu configuré par un collègue ne fait pas ce qui est demandé (accès Internet pour le LAN sauf PC-STAGIAIRE ; site de la DMZ publié sur 203.0.113.2). Trois pannes indépendantes à trouver avec le journal.',
  build: (sim, h) => { site(sim, h); const f = h.get('FW1');
    f.rules = [R('pass', 'LAN', 'WAN', 'tcp', 'any', 'any', '80,443', 'Navigation web'), R('block', 'LAN', 'WAN', 'any', '192.168.1.50/32', 'any', 'any', 'Stagiaire bloqué'), R('pass', 'LAN', 'WAN', 'udp', 'any', 'any', '53', 'DNS'), R('pass', 'LAN', 'DMZ', 'tcp', 'any', 'any', '80', 'Site de la DMZ'), R('pass', 'WAN', 'DMZ', 'tcp', 'any', 'any', '80', 'Publication du site')];
    f.rules[4].on = false; f.natMasq = []; f.forwards = [{ proto: 'tcp', port: 80, toIp: '172.16.0.10', toPort: 80 }]; f.rebuildNat(); f.ifaceByName('dmz1').nat = 'inside'; },
  solve: (sim, h) => { const f = h.get('FW1'); const r = f.rules.splice(1, 1)[0]; f.rules.unshift(r); f.rules.forEach(x => { x.on = true; }); f.natMasq = [{ from: 'LAN', to: 'WAN' }]; f.rebuildNat(); f.ifaceByName('dmz1').nat = 'inside'; },
  checks: s11, startShould: [s11[0].label, s11[2].label] });

const want = process.argv.slice(2); let all = true;
TPS.filter(t => !want.length || want.includes(t.id)).forEach(t => { all = L.run(t) && all; });
process.exit(all ? 0 : 1);
