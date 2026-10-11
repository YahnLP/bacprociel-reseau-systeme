/* Projet A2 de Première (S16 à S19) – agence ArchiPlus : 3 services (Direction, Atelier, Invités), un serveur, du Wi-Fi invité.
   Chargé par premiere.js : module.exports(TPS, env). */
module.exports = function (TPS, env) {
  const { L, D, K, hostIp, hostDhcp, hostIpWifi, cliRun, shell, IP, rshow, showPw, swn } = env;
  const ip4 = x => IP.parse(x), m27 = IP.parseMask('27'), m26 = IP.parseMask('26');
  const SW_BASE = 'enable\nconfigure terminal\nhostname SW1\nvlan 10\nname DIRECTION\nvlan 20\nname ATELIER\nvlan 30\nname INVITES\nexit\n';
  const SW_VLAN = 'interface range fa0/1 - 8\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface range fa0/9 - 16\nswitchport mode access\nswitchport access vlan 20\nexit\ninterface range fa0/17 - 24\nswitchport mode access\nswitchport access vlan 30\nexit\n';
  const SW_SEC = 'enable secret Archi#2027\nbanner motd #Acces reserve - ArchiPlus#\nend\nwrite memory';
  const R_BASE = 'enable\nconfigure terminal\nhostname R1\ninterface gi0/0\nip address 192.168.50.1 255.255.255.224\nip helper-address 192.168.50.34\nno shutdown\nexit\ninterface gi0/1\nip address 192.168.50.33 255.255.255.224\nno shutdown\nexit\ninterface gi0/2\nip address 192.168.50.65 255.255.255.192\nip helper-address 192.168.50.34\nno shutdown\nexit\n';
  const R_ACL = 'ip access-list extended INVITES-IN\npermit udp any eq 68 any eq 67\npermit udp 192.168.50.64 0.0.0.63 host 192.168.50.34 eq 53\npermit tcp 192.168.50.64 0.0.0.63 host 192.168.50.34 eq 80\ndeny ip any any\nexit\ninterface gi0/2\nip access-group INVITES-IN in\nend\nwrite memory';
  function build(h, mode) {
    const { dev, link, get } = h;
    dev('pc-win', 'PC-DIR', 80, 60, 'Direction'); dev('pc-win', 'PC-AT1', 80, 200, 'Atelier 1'); dev('pc-win', 'PC-AT2', 80, 340, 'Atelier 2');
    dev('printer', 'IMP', 250, 400, 'Imprimante'); dev('srv-linux', 'SRV', 560, 400, 'Serveur'); dev('sw-2960', 'SW1', 330, 220, 'Switch');
    dev('r-2911', 'R1', 560, 60, 'Routeur'); dev('ap-u6', 'AP1', 560, 250, 'Borne Wi-Fi'); dev('laptop', 'LAP-INV', 760, 250, 'Portable invité');
    ['PC-DIR', 'PC-AT1', 'PC-AT2'].forEach(n => hostDhcp(get(n)));
    const l = get('LAP-INV'); hostDhcp(l); hostIpWifi(l);
  }
  function wifi(sim, h) {
    const a = h.get('AP1'); a.ssid = 'ARCHI-INVITES'; a.key = 'Invites#2027'; a.security = 'WPA2';
    const l = h.get('LAP-INV'); l.wifi = { ssid: 'ARCHI-INVITES', key: 'Invites#2027' }; hostDhcp(l); hostIpWifi(l); L.NS.wifiRefresh(sim);
  }
  function solve(sim, h, f) {
    f = f || {};
    const { link, get } = h;
    link('PC-DIR', 'eth0', 'SW1', 'Fa0/1'); link('R1', 'gi0/0', 'SW1', 'Fa0/8');
    link('PC-AT1', 'eth0', 'SW1', 'Fa0/9'); link('PC-AT2', 'eth0', 'SW1', 'Fa0/10');
    link('IMP', get('IMP').ifaceList()[0].port.name, 'SW1', 'Fa0/11'); link('SRV', 'ens33', 'SW1', 'Fa0/12'); link('R1', 'gi0/1', 'SW1', 'Fa0/16');
    link('AP1', 'eth0', 'SW1', 'Fa0/17'); link('R1', 'gi0/2', 'SW1', 'Fa0/24');
    cliRun(get('SW1'), SW_BASE + SW_VLAN + (f.vlan ? 'interface fa0/10\nswitchport access vlan 30\nexit\n' : '') + SW_SEC);
    cliRun(get('R1'), (f.helper ? R_BASE.replace('ip address 192.168.50.1 255.255.255.224\nip helper-address 192.168.50.34', 'ip address 192.168.50.1 255.255.255.224') : R_BASE) + (f.acl ? R_ACL.replace('permit udp 192.168.50.64 0.0.0.63 host 192.168.50.34 eq 53\n', '') : R_ACL));
    hostIp(get('IMP'), '192.168.50.35', '27', '192.168.50.33'); hostIp(get('SRV'), '192.168.50.34', '27', '192.168.50.33', '192.168.50.34');
    const s = get('SRV'); const d = s.dhcpd;
    d.excluded = [[ip4('192.168.50.1'), ip4('192.168.50.9')], [ip4('192.168.50.33'), ip4('192.168.50.39')], [ip4('192.168.50.65'), ip4('192.168.50.69')]];
    d.addPool({ name: 'DIRECTION', net: ip4('192.168.50.0'), mask: m27, router: ip4('192.168.50.1'), dns: [ip4('192.168.50.34')], domain: 'archiplus.local', lease: 28800, start: ip4('192.168.50.10'), end: ip4('192.168.50.30') });
    d.addPool({ name: 'ATELIER', net: ip4('192.168.50.32'), mask: m27, router: ip4('192.168.50.33'), dns: [ip4('192.168.50.34')], domain: 'archiplus.local', lease: 28800, start: ip4('192.168.50.40'), end: ip4('192.168.50.62') });
    d.addPool({ name: 'INVITES', net: ip4('192.168.50.64'), mask: m26, router: ip4('192.168.50.65'), dns: [ip4('192.168.50.34')], domain: 'archiplus.local', lease: 3600, start: ip4('192.168.50.70'), end: ip4('192.168.50.120') });
    d.enabled = true;
    s.dnsd.records = [{ name: 'intranet.archiplus.local', type: 'A', data: '192.168.50.34' }, { name: 'imprimante.archiplus.local', type: 'A', data: '192.168.50.35' }]; s.dnsd.start();
    s.httpd.start();
    wifi(sim, h);
  }
  const sh = (c, n, cmd) => shell(c.sim, swn(c, n), cmd);
  const checks = [
    { label: 'PC-DIR obtient une adresse Direction (192.168.50.10-30)', run: c => { c.wait(10000); return /^192\.168\.50\.(1\d|2\d|30)$/.test(c.ipOf('PC-DIR')); } },
    { label: 'PC-AT1 obtient une adresse Atelier (192.168.50.40-62)', run: c => /^192\.168\.50\.(4\d|5\d|6[0-2])$/.test(c.ipOf('PC-AT1')) },
    { label: 'LAP-INV obtient une adresse Invités (192.168.50.70-120)', run: c => /^192\.168\.50\.(7\d|8\d|9\d|1[01]\d|120)$/.test(c.ipOf('LAP-INV')) },
    { label: 'Direction joint l\'Atelier (PC-DIR → PC-AT1)', run: c => c.ping('PC-DIR', c.ipOf('PC-AT1')) },
    { label: 'Direction ouvre le site du serveur par son nom', run: c => { const r = c.http('PC-DIR', 'http://intranet.archiplus.local'); return !!r && r.status === 200; } },
    { label: 'Les invités ouvrent le site du serveur', run: c => { const r = c.http('LAP-INV', 'http://192.168.50.34'); return !!r && r.status === 200; } },
    { label: 'Les invités ne joignent PAS le poste de la Direction', run: c => !c.ping('LAP-INV', c.ipOf('PC-DIR')) },
    { label: 'Les invités ne joignent PAS l\'imprimante', run: c => !c.ping('LAP-INV', '192.168.50.35') },
    { label: 'Switch : mot de passe enable chiffré et config sauvegardée', run: c => /enable secret/.test(showPw(c, swn(c, 'SW1'), 'show startup-config', ['Archi#2027'])) },
  ];
  TPS.push({
    id: 'p16-projet', start: D + 'S16-projet-1-etude/tp/p16-projet-depart.json', solution: K + 'P16-projet-corrige.json',
    notes: 'Première S16 à S19 – Projet A2 ArchiPlus : matériel posé sur le schéma, aucun câble, aucune configuration. À câbler et configurer : VLAN 10/20/30, routeur à 3 pattes, DHCP/DNS/web sur SRV, Wi-Fi invité filtré.',
    build(sim, h) { h.sim = sim; build(h); }, solve, checks, startShould: checks.map(x => x.label).filter(x => !/ne joignent PAS/.test(x)),
  });
  const PANNE = { vlan: 1, helper: 1, acl: 1 };
  const pchecks = checks.concat([
    { label: 'PC-AT2 obtient une adresse Atelier (192.168.50.40-62)', run: c => /^192\.168\.50\.(4\d|5\d|6[0-2])$/.test(c.ipOf('PC-AT2')) },
    { label: 'Les invités ouvrent le site par son nom', run: c => { c.wait(3000); const r = c.http('LAP-INV', 'http://intranet.archiplus.local'); return !!r && r.status === 200; } },
  ]);
  TPS.push({
    id: 'p18-panne', start: D + 'S18-projet-3-recette/tp/p18-panne.json', solution: K + 'P18-panne-corrige.json',
    notes: 'Première S18 – Le projet ArchiPlus est installé mais 3 pannes ont été glissées : un port du switch dans le mauvais VLAN, le relais DHCP manquant côté Direction, une règle DNS oubliée dans l\'ACL des invités.',
    build(sim, h) { h.sim = sim; build(h); solve(sim, h, PANNE); },
    solve(sim, h) {
      cliRun(h.get('SW1'), 'enable\nArchi#2027\nconf t\ninterface fa0/10\nswitchport access vlan 20\nend\nwrite memory');
      cliRun(h.get('R1'), 'enable\nconf t\ninterface gi0/0\nip helper-address 192.168.50.34\nexit\nip access-list extended INVITES-IN\n25 permit udp 192.168.50.64 0.0.0.63 host 192.168.50.34 eq 53\nend\nwrite memory');
      sim.runFor(3000); ['PC-DIR', 'PC-AT2'].forEach(n => L.shell(sim, h.get(n), 'ipconfig /renew'));
    },
    checks: pchecks, startShould: ['PC-AT2 obtient une adresse Atelier (192.168.50.40-62)', 'Les invités ouvrent le site par son nom', 'PC-DIR obtient une adresse Direction (192.168.50.10-30)'],
  });
};
