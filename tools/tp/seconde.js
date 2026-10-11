/* TP du simulateur – Seconde. Lancer : node tools/tp/seconde.js [id ...]
   Chaque TP : fichier de départ (docs/…/tp/*.json), corrigé (corriges/…), vérifications par le moteur. */
const L = require('./lib');
const C = require('./common');
const { hostIp, hostDhcp, hostIpWifi, IP } = L;
const D = 'docs/seconde/', K = 'corriges/seconde/';
const TPS = [];

/* ---------- S06 : le terminal réseau ---------- */
TPS.push({
  id: 's06-terminal', start: D + 'S06-terminal/tp/s06-terminal-reseau.json', solution: K + 'S06-terminal-reseau-corrige.json',
  notes: 'S06 – Premières commandes réseau : hostname, ipconfig / ip a, ping.',
  build(sim, { dev, link, get }) {
    dev('sw-8p', 'SW1', 400, 130); dev('pc-win', 'PC-WIN', 220, 320); dev('pc-linux', 'PC-LINUX', 580, 320);
    link('PC-WIN', 'eth0', 'SW1', 'port1'); link('PC-LINUX', 'ens33', 'SW1', 'port2');
    hostIp(get('PC-WIN'), '192.168.10.11'); hostIp(get('PC-LINUX'), '192.168.10.12');
  },
  checks: [{ label: 'PC-WIN joint PC-LINUX', run: c => c.ping('PC-WIN', '192.168.10.12') }, { label: 'PC-LINUX joint PC-WIN', run: c => c.ping('PC-LINUX', '192.168.10.11') }],
});

/* ---------- S08 : le réseau de la salle (tout fonctionne, on observe) ---------- */
TPS.push({
  id: 's08-reseau-salle', start: D + 'S08-quest-ce-qu-un-reseau/tp/s08-reseau-salle.json', solution: null,
  notes: 'S08 – Le réseau de la salle : on observe, on suit les câbles, on dessine le schéma.',
  build(sim, h) {
    const { dev, link, get } = h;
    C.internet(sim, h, 900, 200); C.box(sim, h, 'BOX', 680, 200);
    dev('sw-8p', 'SW1', 480, 200); link('SW1', 'port1', 'BOX', 'lan1');
    dev('pc-win', 'PC1', 330, 80); dev('pc-win', 'PC2', 330, 320); dev('laptop', 'PC3', 480, 340); dev('printer', 'IMP1', 480, 60);
    link('PC1', 'eth0', 'SW1', 'port2'); link('PC2', 'eth0', 'SW1', 'port3'); link('PC3', 'ethernet0', 'SW1', 'port4'); link('IMP1', 'lan', 'SW1', 'port5');
    ['PC1', 'PC2', 'PC3', 'IMP1'].forEach(n => hostDhcp(get(n)));
  },
  checks: [
    { label: 'PC1 a une adresse (DHCP de la box)', run: c => { c.wait(8000); return /^192\.168\.1\./.test(c.ipOf('PC1')); } },
    { label: 'PC1 joint Internet (FAI)', run: c => c.ping('PC1', '203.0.113.1') },
    { label: 'PC3 ouvre le site www.exemple.fr', run: c => { const r = c.http('PC3', 'http://www.exemple.fr'); return !!r && r.status === 200; } },
  ],
});

/* ---------- S10 : deux PC sur un switch, rien de configuré ---------- */
TPS.push({
  id: 's10-deux-pc', start: D + 'S10-raccorder-brasser/tp/s10-deux-pc-switch.json', solution: K + 'S10-deux-pc-switch-corrige.json',
  notes: 'S10 – Deux PC reliés à un switch non administrable : voyants OK, mais se voient-ils ? (réponse en S11)',
  build(sim, { dev, link }) {
    dev('sw-8p', 'SW1', 400, 130); dev('pc-win', 'PC1', 230, 300); dev('pc-win', 'PC2', 570, 300);
    link('PC1', 'eth0', 'SW1', 'port1'); link('PC2', 'eth0', 'SW1', 'port2');
  },
  solve(sim, { get }) { hostIp(get('PC1'), '192.168.1.11'); hostIp(get('PC2'), '192.168.1.12'); },
  checks: [{ label: 'PC1 joint PC2', run: c => c.ping('PC1', '192.168.1.12') }],
  startShould: ['PC1 joint PC2'],
});

/* ---------- S11 : adressage IP statique ---------- */
TPS.push({
  id: 's11-adressage', start: D + 'S11-adresse-ip/tp/s11-adressage-vierge.json', solution: K + 'S11-adressage-corrige.json',
  notes: 'S11 – Trois postes sur un switch, aucune adresse : plan d\'adressage 192.168.1.0/24 à configurer et à tester.',
  build(sim, { dev, link }) {
    dev('sw-8p', 'SW1', 400, 130); dev('pc-win', 'PC1', 200, 310); dev('pc-linux', 'PC2', 400, 330); dev('laptop', 'PC3', 600, 310);
    link('PC1', 'eth0', 'SW1', 'port1'); link('PC2', 'ens33', 'SW1', 'port2'); link('PC3', 'ethernet0', 'SW1', 'port3');
  },
  solve(sim, { get }) { hostIp(get('PC1'), '192.168.1.11'); hostIp(get('PC2'), '192.168.1.12'); hostIp(get('PC3'), '192.168.1.13'); },
  checks: [{ label: 'PC1 joint PC2', run: c => c.ping('PC1', '192.168.1.12') }, { label: 'PC1 joint PC3', run: c => c.ping('PC1', '192.168.1.13') }, { label: 'PC3 joint PC2', run: c => c.ping('PC3', '192.168.1.12') }],
  startShould: ['PC1 joint PC2', 'PC1 joint PC3', 'PC3 joint PC2'],
});
TPS.push({
  id: 's11-erreurs', start: D + 'S11-adresse-ip/tp/s11-erreurs.json', solution: K + 'S11-erreurs-corrige.json',
  notes: 'S11 – Quatre postes configurés, trois erreurs d\'adressage à trouver : adresse hors réseau, mauvais masque, doublon.',
  build(sim, { dev, link, get }) {
    dev('sw-8p', 'SW1', 400, 130); dev('pc-win', 'PC1', 130, 320); dev('pc-win', 'PC2', 330, 340); dev('pc-win', 'PC3', 530, 340); dev('pc-win', 'PC4', 730, 320);
    ['PC1', 'PC2', 'PC3', 'PC4'].forEach((n, i) => link(n, 'eth0', 'SW1', 'port' + (i + 1)));
    hostIp(get('PC1'), '192.168.1.11');           // référence : correct
    hostIp(get('PC2'), '192.168.11.12');          // erreur 1 : faute de frappe, autre réseau
    hostIp(get('PC3'), '192.168.1.200', '25');    // erreur 2 : masque trop long
    hostIp(get('PC4'), '192.168.1.11');           // erreur 3 : même adresse que PC1
  },
  solve(sim, { get }) { hostIp(get('PC2'), '192.168.1.12'); hostIp(get('PC3'), '192.168.1.13'); hostIp(get('PC4'), '192.168.1.14'); },
  checks: [{ label: 'PC1 joint PC2', run: c => c.ping('PC1', '192.168.1.12') }, { label: 'PC1 joint PC3', run: c => c.ping('PC1', '192.168.1.13') }, { label: 'PC1 joint PC4', run: c => c.ping('PC1', '192.168.1.14') }, { label: 'PC4 joint PC2', run: c => c.ping('PC4', '192.168.1.12') }],
  startShould: ['PC1 joint PC2'],
});

/* ---------- S12 : DHCP, box et passerelle ---------- */
TPS.push({
  id: 's12-dhcp-box', start: D + 'S12-dhcp-box/tp/s12-dhcp-box.json', solution: K + 'S12-dhcp-box-corrige.json',
  notes: 'S12 – Un petit réseau derrière une box : PC1, PC3 et PC4 en DHCP ; PC2 configuré à la main sans passerelle (il ne sort pas sur Internet).',
  build(sim, h) {
    const { dev, link, get } = h;
    C.internet(sim, h, 900, 200); C.box(sim, h, 'BOX', 680, 200);
    dev('sw-8p', 'SW1', 480, 200); link('SW1', 'port1', 'BOX', 'lan1');
    dev('pc-win', 'PC1', 300, 70); dev('pc-win', 'PC2', 300, 200); dev('pc-linux', 'PC3', 300, 330); dev('laptop', 'PC4', 480, 360);
    link('PC1', 'eth0', 'SW1', 'port2'); link('PC2', 'eth0', 'SW1', 'port3'); link('PC3', 'ens33', 'SW1', 'port4'); link('PC4', 'ethernet0', 'SW1', 'port5');
    hostDhcp(get('PC1')); hostIp(get('PC2'), '192.168.1.50'); hostDhcp(get('PC3')); hostDhcp(get('PC4'));
  },
  solve(sim, { get }) { hostIp(get('PC2'), '192.168.1.50', '24', '192.168.1.1', '192.168.1.1'); },
  checks: [
    { label: 'PC1 a une adresse (DHCP de la box)', run: c => { c.wait(8000); return /^192\.168\.1\./.test(c.ipOf('PC1')); } },
    { label: 'PC1 joint Internet (FAI)', run: c => c.ping('PC1', '203.0.113.1') },
    { label: 'PC2 joint PC1 (même réseau)', run: c => c.ping('PC2', c.ipOf('PC1')) },
    { label: 'PC2 joint Internet (FAI)', run: c => c.ping('PC2', '203.0.113.1') },
  ],
  startShould: ['PC2 joint Internet (FAI)'],
});

/* ---------- S13 : DNS, NAT, panne DNS ---------- */
TPS.push({
  id: 's13-dns', start: D + 'S13-dns-internet/tp/s13-dns.json', solution: K + 'S13-dns-corrige.json',
  notes: 'S13 – Du nom à l\'adresse : PC1 et PC3 en DHCP, PC2 a un DNS erroné (il joint Internet par adresse, mais pas les sites par nom).',
  build(sim, h) {
    const { dev, link, get } = h;
    C.internet(sim, h, 900, 200); C.box(sim, h, 'BOX', 680, 200);
    dev('sw-8p', 'SW1', 480, 200); link('SW1', 'port1', 'BOX', 'lan1');
    dev('pc-win', 'PC1', 300, 70); dev('pc-win', 'PC2', 300, 200); dev('pc-linux', 'PC3', 300, 330);
    link('PC1', 'eth0', 'SW1', 'port2'); link('PC2', 'eth0', 'SW1', 'port3'); link('PC3', 'ens33', 'SW1', 'port4');
    hostDhcp(get('PC1')); hostIp(get('PC2'), '192.168.1.50', '24', '192.168.1.1', '198.51.100.99'); hostDhcp(get('PC3'));
  },
  solve(sim, { get }) { hostIp(get('PC2'), '192.168.1.50', '24', '192.168.1.1', '192.168.1.1'); },
  checks: [
    { label: 'PC1 ouvre www.exemple.fr', run: c => { c.wait(8000); const r = c.http('PC1', 'http://www.exemple.fr'); return !!r && r.status === 200; } },
    { label: 'PC3 ouvre www.exemple.fr', run: c => { const r = c.http('PC3', 'http://www.exemple.fr'); return !!r && r.status === 200; } },
    { label: 'PC2 joint le site par son adresse', run: c => c.ping('PC2', '198.51.100.80') },
    { label: 'PC2 ouvre www.exemple.fr (par le nom)', run: c => { const r = c.http('PC2', 'http://www.exemple.fr'); return !!r && r.status === 200; } },
  ],
  startShould: ['PC2 ouvre www.exemple.fr (par le nom)'],
});

/* ---------- S14 : Wi-Fi ---------- */
TPS.push({
  id: 's14-wifi', start: D + 'S14-wifi/tp/s14-wifi.json', solution: K + 'S14-wifi-corrige.json',
  notes: 'S14 – Une borne Wi-Fi neuve (SSID et sécurité d\'usine) derrière une box : à renommer, sécuriser, puis connecter deux portables. LAP3 a une mauvaise clé.',
  build(sim, h) {
    const { dev, link, get } = h;
    C.internet(sim, h, 900, 200); C.box(sim, h, 'BOX', 680, 200);
    dev('ap-u6', 'AP1', 480, 160); link('AP1', 'eth0', 'BOX', 'lan1');
    dev('pc-win', 'PC1', 560, 360); link('PC1', 'eth0', 'BOX', 'lan2'); hostDhcp(get('PC1'));
    dev('laptop', 'LAP1', 250, 330); dev('laptop', 'LAP2', 400, 380); dev('laptop', 'LAP3', 120, 220);
    const a = get('AP1'); a.ssid = 'AP-USINE'; a.key = ''; a.security = 'Ouvert';
  },
  solve(sim, { get }) {
    const a = get('AP1'); a.ssid = 'ATELIER-CIEL'; a.key = 'Atelier-Ciel#2027'; a.security = 'WPA2';
    ['LAP1', 'LAP2'].forEach(n => { const l = get(n); l.wifi = { ssid: 'ATELIER-CIEL', key: 'Atelier-Ciel#2027' }; hostDhcp(l); hostIpWifi(l); });
    const l3 = get('LAP3'); l3.wifi = { ssid: 'ATELIER-CIEL', key: 'mauvaiseCle' }; hostDhcp(l3); hostIpWifi(l3);
    L.NS.wifiRefresh(sim);
  },
  checks: [
    { label: 'La borne est en WPA2 avec le SSID ATELIER-CIEL', run: c => { const a = c.get('AP1'); return a.security === 'WPA2' && a.ssid === 'ATELIER-CIEL'; } },
    { label: 'LAP1 est associé et obtient une adresse', run: c => { c.wait(8000); return /^192\.168\.1\./.test(c.ipOf('LAP1')); } },
    { label: 'LAP1 joint Internet (FAI)', run: c => c.ping('LAP1', '203.0.113.1') },
    { label: 'LAP2 joint PC1 (filaire)', run: c => c.ping('LAP2', c.ipOf('PC1')) },
  ],
  startShould: ['La borne est en WPA2 avec le SSID ATELIER-CIEL', 'LAP1 est associé et obtient une adresse'],
});

/* ---------- S15 : cinq pannes à diagnostiquer (rotation) ---------- */
function reseauPanne(h, sansLiaison) {
  const { dev, link, get } = h;
  C.internet(null, h, 900, 200); C.box(null, h, 'BOX', 680, 200);
  dev('sw-8p', 'SW1', 480, 200); if (!sansLiaison) link('SW1', 'port1', 'BOX', 'lan1');
  dev('pc-win', 'PC-REF', 300, 90, 'PC de référence');
  link('PC-REF', 'eth0', 'SW1', 'port2');
}
const PANNE_CHECKS = [
  { label: 'PC-CLIENT joint la box', run: c => { c.wait(8000); return c.ping('PC-CLIENT', '192.168.1.1'); } },
  { label: 'PC-CLIENT joint Internet (FAI)', run: c => c.ping('PC-CLIENT', '203.0.113.1') },
  { label: 'PC-CLIENT ouvre www.exemple.fr', run: c => { const r = c.http('PC-CLIENT', 'http://www.exemple.fr'); return !!r && r.status === 200; } },
];
const PANNES = [
  { n: 1, nom: 'cable', txt: 'panne 1 : PC du client non relié au switch',
    build(h) { reseauPanne(h); hostDhcp(h.get('PC-REF')); hostDhcp(h.dev('pc-win', 'PC-CLIENT', 300, 330, 'PC du client')); },
    solve(sim, h) { h.link('PC-CLIENT', 'eth0', 'SW1', 'port3'); hostDhcp(h.get('PC-CLIENT')); } },
  { n: 2, nom: 'adresse', txt: 'panne 2 : adresse IP fixe fausse (autre réseau)',
    build(h) { reseauPanne(h); hostDhcp(h.get('PC-REF')); const c = h.dev('pc-win', 'PC-CLIENT', 300, 330, 'PC du client'); h.link('PC-CLIENT', 'eth0', 'SW1', 'port3'); hostIp(c, '192.168.10.30', '24', '192.168.1.1', '192.168.1.1'); },
    solve(sim, h) { hostIp(h.get('PC-CLIENT'), '192.168.1.30', '24', '192.168.1.1', '192.168.1.1'); } },
  { n: 3, nom: 'passerelle', txt: 'panne 3 : passerelle fausse',
    build(h) { reseauPanne(h); hostDhcp(h.get('PC-REF')); const c = h.dev('pc-win', 'PC-CLIENT', 300, 330, 'PC du client'); h.link('PC-CLIENT', 'eth0', 'SW1', 'port3'); hostIp(c, '192.168.1.30', '24', '192.168.1.2', '192.168.1.1'); },
    solve(sim, h) { hostIp(h.get('PC-CLIENT'), '192.168.1.30', '24', '192.168.1.1', '192.168.1.1'); } },
  { n: 4, nom: 'dns', txt: 'panne 4 : serveur DNS faux',
    build(h) { reseauPanne(h); hostDhcp(h.get('PC-REF')); const c = h.dev('pc-win', 'PC-CLIENT', 300, 330, 'PC du client'); h.link('PC-CLIENT', 'eth0', 'SW1', 'port3'); hostIp(c, '192.168.1.30', '24', '192.168.1.1', '192.168.1.5'); },
    solve(sim, h) { hostIp(h.get('PC-CLIENT'), '192.168.1.30', '24', '192.168.1.1', '192.168.1.1'); } },
  { n: 5, nom: 'liaison', txt: 'panne 5 : câble entre le switch et la box débranché',
    build(h) { reseauPanne(h, true); hostDhcp(h.get('PC-REF')); const c = h.dev('pc-win', 'PC-CLIENT', 300, 330, 'PC du client'); h.link('PC-CLIENT', 'eth0', 'SW1', 'port3'); hostDhcp(c); },
    solve(sim, h) { h.link('SW1', 'port1', 'BOX', 'lan1'); } },
].forEach(P => {
  TPS.push({
    id: 's15-panne-' + P.n, start: D + 'S15-depannage-n1/tp/s15-panne-' + P.n + '.json', solution: K + 'S15-panne-' + P.n + '-corrige.json',
    notes: 'S15 – ' + P.txt + '. Réseau : box, FAI, DNS, site www.exemple.fr. Poste de référence PC-REF, poste du client PC-CLIENT.',
    build(sim, h) { P.build(h); }, solve: P.solve, checks: PANNE_CHECKS, startShould: P.n === 1 || P.n === 2 || P.n === 5 ? PANNE_CHECKS.map(c => c.label) : P.n === 3 ? [PANNE_CHECKS[1].label, PANNE_CHECKS[2].label] : [PANNE_CHECKS[2].label],
  });
});


/* ---------- S16–S17 : projet A1, l'atelier de 4 postes ---------- */
function atelier(h) {
  const { dev } = h;
  C.internet(null, h, 900, 200); C.box(null, h, 'BOX', 680, 200);
  dev('sw-8p', 'SW1', 480, 200, 'Switch de l\'atelier');
  dev('pc-win', 'PC1', 260, 40, 'Poste 1'); dev('pc-win', 'PC2', 260, 140, 'Poste 2'); dev('pc-win', 'PC3', 260, 260, 'Poste 3'); dev('pc-win', 'PC4', 260, 360, 'Poste 4');
  dev('printer', 'IMP1', 480, 380, 'Imprimante'); dev('ap-u6', 'AP1', 680, 380, 'Borne Wi-Fi'); dev('laptop', 'LAP-INV', 680, 500, 'Portable invité');
}
function atelierCables(h) {
  const { link } = h;
  link('SW1', 'port1', 'BOX', 'lan1');
  ['PC1', 'PC2', 'PC3', 'PC4'].forEach((n, k) => link(n, 'eth0', 'SW1', 'port' + (2 + k)));
  link('IMP1', 'lan', 'SW1', 'port6'); link('AP1', 'eth0', 'BOX', 'lan2');
}
function atelierConfig(sim, h, ipImp) {
  const { get } = h;
  ['PC1', 'PC2', 'PC3', 'PC4'].forEach(n => hostDhcp(get(n)));
  hostIp(get('IMP1'), ipImp, '24', '192.168.1.1');
  const a = get('AP1'); a.ssid = 'ATELIER-INVITES'; a.key = 'Invites#2027'; a.security = 'WPA2';
  const l = get('LAP-INV'); l.wifi = { ssid: 'ATELIER-INVITES', key: 'Invites#2027' }; hostDhcp(l); hostIpWifi(l); L.NS.wifiRefresh(sim);
}
const A1_CHECKS = [
  { label: 'Les 4 postes ont une adresse 192.168.1.x (DHCP)', run: c => { c.wait(8000); return ['PC1', 'PC2', 'PC3', 'PC4'].every(n => /^192\.168\.1\./.test(c.ipOf(n))); } },
  { label: 'L\'imprimante est en 192.168.1.150 (hors plage DHCP)', run: c => c.ipOf('IMP1') === '192.168.1.150' },
  { label: 'PC1 joint l\'imprimante', run: c => c.ping('PC1', '192.168.1.150') },
  { label: 'PC4 joint l\'imprimante', run: c => c.ping('PC4', '192.168.1.150') },
  { label: 'PC3 ouvre www.exemple.fr', run: c => { const r = c.http('PC3', 'http://www.exemple.fr'); return !!r && r.status === 200; } },
  { label: 'Le portable invité obtient une adresse en Wi-Fi', run: c => /^192\.168\.1\./.test(c.ipOf('LAP-INV')) },
  { label: 'Le portable invité ouvre www.exemple.fr', run: c => { const r = c.http('LAP-INV', 'http://www.exemple.fr'); return !!r && r.status === 200; } },
];
TPS.push({
  id: 's16-atelier', start: D + 'S16-projet-a1-1/tp/projet-a1-depart.json', solution: K + 'S16-projet-a1-corrige.json',
  notes: 'Projet A1 – L\'atelier : box, switch, 4 postes, imprimante, borne Wi-Fi invité. Équipements placés mais non câblés ni configurés : à câbler, adresser, tester.',
  build(sim, h) { atelier(h); },
  solve(sim, h) { atelierCables(h); atelierConfig(sim, h, '192.168.1.150'); },
  checks: A1_CHECKS, startShould: A1_CHECKS.map(c => c.label),
});


TPS.push({
  id: 's17-panne-imprimante', start: D + 'S17-projet-a1-2/tp/projet-a1-panne-imprimante.json', solution: K + 'S17-panne-imprimante-corrige.json',
  notes: 'Projet A1, jalon de recette – panne introduite : l\'imprimante a une adresse fixe dans un autre réseau (192.168.10.150).',
  build(sim, h) { atelier(h); atelierCables(h); atelierConfig(sim, h, '192.168.10.150'); },
  solve(sim, h) { hostIp(h.get('IMP1'), '192.168.1.150', '24', '192.168.1.1'); },
  checks: A1_CHECKS, startShould: ['L\'imprimante est en 192.168.1.150 (hors plage DHCP)', 'PC1 joint l\'imprimante', 'PC4 joint l\'imprimante'],
});
TPS.push({
  id: 's17-panne-poste', start: D + 'S17-projet-a1-2/tp/projet-a1-panne-poste.json', solution: K + 'S17-panne-poste-corrige.json',
  notes: 'Projet A1, jalon de recette – panne introduite : le poste 4 n\'est pas relié au switch.',
  build(sim, h) { atelier(h); const { link } = h; link('SW1', 'port1', 'BOX', 'lan1'); ['PC1', 'PC2', 'PC3'].forEach((n, k) => link(n, 'eth0', 'SW1', 'port' + (2 + k))); link('IMP1', 'lan', 'SW1', 'port6'); link('AP1', 'eth0', 'BOX', 'lan2'); atelierConfig(sim, h, '192.168.1.150'); },
  solve(sim, h) { h.link('PC4', 'eth0', 'SW1', 'port5'); },
  checks: A1_CHECKS, startShould: ['Les 4 postes ont une adresse 192.168.1.x (DHCP)', 'PC4 joint l\'imprimante'],
});
const want = process.argv.slice(2);
let all = true;
TPS.filter(t => !want.length || want.includes(t.id)).forEach(t => { all = L.run(t) && all; });
process.exit(all ? 0 : 1);
