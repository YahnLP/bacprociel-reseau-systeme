/* Banc d'essai des pannes Stormshield (pare-feu simulé) */
const L = require('./lib'); const { NS, IP } = L;
const dv = (sim, n) => Array.from(sim.devices.values()).find(d => d.name === n);
const load = f => { const s = L.reload(f); s.runFor(8000); return s; };
const web = (sim, from, url) => { const c = NS.checker(sim); const r = c.http(from, url); return r ? 'HTTP ' + r.status : 'aucune réponse (délai dépassé)'; };
const png = (sim, from, ip) => NS.checker(sim).ping(from, ip, 2) ? 'ping OK' : 'ping sans réponse';
const rules = f => f.rules.map((r, i) => (i + 1) + ' ' + (r.on ? '' : '[off] ') + r.action.toUpperCase() + ' ' + r.from + '→' + r.to + ' ' + r.proto + ' src=' + r.src + ' dst=' + r.dst + ' port=' + r.dport + '  # ' + r.comment).join('\n');
const logs = (f, n) => (f.fwlog || []).slice(-n).map(e => typeof e === 'string' ? e : JSON.stringify(e)).join('\n');
module.exports = { L, NS, IP, dv, load, web, png, rules, logs };
if (require.main === module) {
  const sim = load(process.argv[2]); const f = dv(sim, 'FW1');
  console.log(rules(f)); console.log('natMasq', JSON.stringify(f.natMasq), 'forwards', JSON.stringify(f.forwards), 'statics', f.statics.length);
  console.log(web(sim, 'PC-ADMIN', 'http://198.51.100.80'), '|', web(sim, 'PC-STAGIAIRE', 'http://198.51.100.80'), '|', web(sim, 'CLIENT', 'http://203.0.113.2'));
  console.log('LOG:\n' + logs(f, 8)); console.log(Object.keys(f).filter(k => /log|nat|fwd|forw/i.test(k)).join(','));
}
