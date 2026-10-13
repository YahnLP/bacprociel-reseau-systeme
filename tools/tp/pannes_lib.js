/* Banc d'essai des pannes : charge un corrigé, injecte une panne, relève les symptômes et les sorties de diagnostic. */
const L = require('./lib');
const { cliRun, shell, mk } = L;
const PWS = ['', 'Cisco#2027', 'cisco', 'Cisco123', 'class'];
const dv = (sim, n) => Array.from(sim.devices.values()).find(d => d.name === n);
function ios(sim, n, cmd) { const d = dv(sim, n);
  for (const pw of PWS) { const s = d.newSession(); let out = '', done = false; const io = { print: t => { out += t; }, done: () => { done = true; }, clear() { } };
    const go = l => { done = false; out = ''; s.exec(l, io); sim.runUntil(() => done, 60000); };
    go('enable'); if (pw) go(pw); go(cmd); if (out.trim() && !/Invalid|Access denied|Bad secrets|Password/.test(out)) return out.trim(); }
  return ''; }
const sh = (sim, n, cmd) => shell(sim, dv(sim, n), cmd).trim();
const cfg = (sim, n, cmds) => cliRun(dv(sim, n), 'enable\nconf t\n' + cmds + '\nend');
function load(file) { const sim = L.reload(file); sim.runFor(8000); return sim; }
/* faults: [{id, file, inject(sim), probes:[[label, fn(sim)]], fix(sim), settle?}] */
function runFaults(faults, only) {
  faults.filter(f => !only.length || only.includes(f.id)).forEach(f => {
    const sim = load(f.file);
    console.log('\n######## ' + f.id + ' — ' + f.desc);
    const run = tag => f.probes.forEach(([lab, fn]) => { let o; try { o = fn(sim); } catch (e) { o = 'ERR ' + e.message; } o = String(o).split('\n').filter(l => !/^(Flags:|\s+[A-Za-z]{1,2} - |\s*$|Building|Current conf)/.test(l)).slice(0, 16).join('\n'); console.log('--- [' + tag + '] ' + lab + '\n' + o); });
    run('AVANT');
    f.inject(sim); sim.runFor(f.settle || 8000);
    run('PANNE');
    f.fix(sim); sim.runFor(f.settle || 8000);
    run('APRÈS');
  });
}
module.exports = { L, ios, sh, cfg, dv, runFaults, load };
