const S = require('./pannes_ss'); const { dv, load, web, png, rules, logs, IP } = S;
const N5 = 'corriges/stormshield/S05-nat-corrige.json', N6 = 'corriges/stormshield/S06-filtrage-corrige.json';
const tail = (f, n) => logs(f, n).split('\n').map(l => { try { const e = JSON.parse(l); return e.action.toUpperCase() + ' ' + e.src + ':' + e.sport + ' → ' + e.dst + ':' + e.dport + ' ' + e.proto + ' [' + e.zin + '→' + e.zout + '] ' + e.why; } catch (x) { return l; } }).join('\n');
const F = {
 'masq': { file: N5, desc: 'NAT sortant (masquerade) absent', inject: (s, f) => { f.natMasq = []; f.rebuildNat(); }, fix: (s, f) => { f.natMasq = [{ from: 'LAN', to: 'WAN' }]; f.rebuildNat(); },
   probe: s => ['PC-ADMIN → web Internet : ' + web(s, 'PC-ADMIN', 'http://198.51.100.80'), 'PC-ADMIN → web DMZ : ' + web(s, 'PC-ADMIN', 'http://172.16.0.10')] },
 'forward': { file: N5, desc: 'redirection de port absente', inject: (s, f) => { f.forwards = []; f.rebuildNat(); }, fix: (s, f) => { f.forwards = [{ proto: 'tcp', port: 80, toIp: '172.16.0.10', toPort: 80 }]; f.rebuildNat(); f.ifaceByName('dmz1').nat = 'inside'; },
   probe: s => ['CLIENT → http://203.0.113.2 : ' + web(s, 'CLIENT', 'http://203.0.113.2')] },
 'rule-wan-dmz': { file: N5, desc: 'redirection présente mais règle de filtrage WAN→DMZ absente', inject: (s, f) => { f.rules = f.rules.filter(r => r.from !== 'WAN'); }, fix: (s, f) => { f.rules.push({ on: true, action: 'pass', from: 'WAN', to: 'DMZ', proto: 'tcp', src: 'any', dst: 'any', dport: '80', comment: 'Publication du site' }); },
   probe: s => ['CLIENT → http://203.0.113.2 : ' + web(s, 'CLIENT', 'http://203.0.113.2')] },
 'rule-off': { file: N5, desc: 'règle de filtrage désactivée par erreur', inject: (s, f) => { f.rules[2].on = false; }, fix: (s, f) => { f.rules[2].on = true; },
   probe: s => ['CLIENT → http://203.0.113.2 : ' + web(s, 'CLIENT', 'http://203.0.113.2')] },
 'zone': { file: N5, desc: 'règle LAN→DMZ écrite avec la mauvaise zone source', inject: (s, f) => { f.rules[1].from = 'WAN'; }, fix: (s, f) => { f.rules[1].from = 'LAN'; },
   probe: s => ['PC-ADMIN → web DMZ : ' + web(s, 'PC-ADMIN', 'http://172.16.0.10')] },
 'order': { file: N6, desc: 'règle de blocage placée après la règle générale', inject: (s, f) => { const r = f.rules.shift(); f.rules.splice(1, 0, r); }, fix: (s, f) => { const r = f.rules.splice(1, 1)[0]; f.rules.unshift(r); },
   probe: s => ['PC-STAGIAIRE → web Internet : ' + web(s, 'PC-STAGIAIRE', 'http://198.51.100.80')] },
 'route': { file: N5, desc: 'route par défaut absente', inject: (s, f) => { f.statics = f.statics.filter(x => !(x.net === 0 && x.mask === 0)); }, fix: (s, f) => { f.statics.push({ net: 0, mask: 0, nh: IP.parse('203.0.113.1'), iface: null, ad: 1 }); },
   probe: s => ['PC-ADMIN → web Internet : ' + web(s, 'PC-ADMIN', 'http://198.51.100.80'), 'PC-ADMIN → web DMZ : ' + web(s, 'PC-ADMIN', 'http://172.16.0.10')] },
 'gw-srv': { file: N5, desc: 'serveur DMZ avec une mauvaise passerelle', inject: (s, f) => { L_hostGw(s, '172.16.0.99'); }, fix: (s, f) => { L_hostGw(s, '172.16.0.254'); },
   probe: s => ['PC-ADMIN → web DMZ : ' + web(s, 'PC-ADMIN', 'http://172.16.0.10'), 'CLIENT → http://203.0.113.2 : ' + web(s, 'CLIENT', 'http://203.0.113.2')] },
};
const L = S.L; function L_hostGw(s, gw) { L.hostIp(dv(s, 'SRVWEB'), '172.16.0.10', '24', gw); }
const want = process.argv.slice(2); Object.keys(F).filter(k => !want.length || want.includes(k)).forEach(k => {
  const d = F[k]; const s = load(d.file); const f = dv(s, 'FW1'); console.log('\n######## ' + k + ' — ' + d.desc);
  const step = tag => { f.fwlog.length = 0; const p = d.probe(s); s.runFor(3000); console.log('--- [' + tag + ']\n' + p.join('\n') + '\n  journal :\n' + tail(f, 4).split('\n').map(x => '    ' + x).join('\n')); };
  step('AVANT'); d.inject(s, f); s.runFor(3000); step('PANNE'); d.fix(s, f); s.runFor(12000); step('APRÈS');
});
