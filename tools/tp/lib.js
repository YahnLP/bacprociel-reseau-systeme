/* Bibliothèque pour fabriquer et vérifier les TP du simulateur réseau (hors ligne).
   Le moteur du simulateur (EUPL 1.2) est lu dans le dossier indiqué par SIM_DIR
   (par défaut : ../../../yahnlp/simulateur-reseau). */
const fs = require('fs'), path = require('path');
const SIM = process.env.SIM_DIR || path.resolve(__dirname, '../../../yahnlp/simulateur-reseau');
const NS = require(path.join(SIM, 'tests', 'load.js'))();
const { Sim, createDevice, IP } = NS;
const REPO = path.resolve(__dirname, '../..');

function mk(sim) {
  const dev = (model, name, x, y, label) => { const d = createDevice(sim, model, { name, x, y }); if (label) d.label = label; return d; };
  const get = n => Array.from(sim.devices.values()).find(d => d.name === n);
  const link = (a, pa, b, pb, type) => {
    const A = typeof a === 'string' ? get(a) : a, B = typeof b === 'string' ? get(b) : b;
    const l = sim.connect(A.findPort(pa), B.findPort(pb), type || 'auto');
    if (!l) throw new Error('câble impossible ' + A.name + ':' + pa + ' – ' + B.name + ':' + pb);
    return l;
  };
  return { dev, get, link };
}
function cliRun(dev, text) {
  const s = dev.newSession(); const io = { print() { }, done() { }, clear() { } };
  text.split('\n').map(l => l.trim()).filter(Boolean).forEach(l => s.exec(l, io));
}
function hostIp(h, ip, mask, gw, dns) {
  h.applyIp(h.ifaceList()[0].name, { ip, mask: mask || '24' });
  if (gw !== undefined && gw !== null) h.setGateway(gw);
  if (dns) { h.dnsServers = [].concat(dns).map(IP.parse); h.dhcpDns = false; }
}
function hostDhcp(h) { const i = h.ifaceList()[0]; h.enableDhcp(i, false); h.applyIp(i.name, { dhcp: true }); }
function hostIpWifi(l) { const w = l.ifaceList().find(i => i.port && i.port.media === 'wifi'); if (w) { l.enableDhcp(w, false); l.applyIp(w.name, { dhcp: true }); } }
/* exécute une commande dans le terminal d'un hôte et rend la sortie */
function shell(sim, dev, line) {
  const s = dev.newSession(); let out = '', done = false;
  s.exec(line, { print: t => { out += t; }, done: () => { done = true; }, clear() { } });
  sim.runUntil(() => done, 60000); return out;
}

function save(sim, file, extra) {
  // La box apprend son DNS amont par DHCP WAN : on le fige (ip name-server) pour qu'il survive à l'enregistrement.
  sim.devices.forEach(d => { if (d.model === 'box' && d.dnsServers && d.dnsServers.length) d.dhcpDns = false; if (d.model === 'box') d.statics.forEach(r => { delete r.dhcp; }); });
  const full = path.join(REPO, file);
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, JSON.stringify(NS.saveTopology(sim, extra), null, 1) + '\n');
}
function reload(file) {
  const sim = new Sim();
  NS.loadTopology(sim, JSON.parse(fs.readFileSync(path.join(REPO, file), 'utf8')));
  return sim;
}

/* Un TP : { id, start:'chemin.json', solution:'chemin.json', build(sim,h), solve(sim,h), checks:[{label,run}],
   startShould:[labels des checks qui DOIVENT échouer au départ] } */
function run(tp) {
  let ok = true; const say = (m) => console.log(m);
  say('— ' + tp.id);
  // 1. départ
  const sim = new Sim(); const h = mk(sim); tp.build(sim, h);
  sim.runFor(8000);
  save(sim, tp.start, { notes: tp.notes || '' });
  const c0 = NS.checker(sim);
  (tp.checks || []).forEach(ch => {
    let r; try { r = !!ch.run(c0); } catch (e) { r = 'ERR ' + e.message; }
    const should = (tp.startShould || []).includes(ch.label);
    const good = should ? r === false : true;
    if (!good) ok = false;
    say('   départ  ' + (good ? 'ok  ' : 'KO  ') + (r === true ? 'vrai ' : 'faux ') + ch.label);
  });
  // 2. solution
  if (tp.solve) {
    const sim2 = reload(tp.start); const h2 = mk(sim2); tp.solve(sim2, h2);
    sim2.runFor(8000);
    save(sim2, tp.solution, { notes: 'CORRIGÉ – ' + (tp.notes || '') });
    const sim3 = reload(tp.solution); sim3.runFor(8000); const c3 = NS.checker(sim3);
    (tp.checks || []).forEach(ch => {
      let r; try { r = !!ch.run(c3); } catch (e) { r = 'ERR ' + e.message; }
      if (r !== true) ok = false;
      say('   corrigé ' + (r === true ? 'ok  ' : 'KO  ') + ch.label);
    });
  }
  say(ok ? '   => VALIDE' : '   => À CORRIGER');
  return ok;
}
module.exports = { NS, Sim, IP, createDevice, mk, cliRun, hostIp, hostDhcp, hostIpWifi, shell, save, reload, run, REPO };
