/* Terminale – TP S06 et suivants (suite). Chargé par terminale.js. */
module.exports = function (TPS, env) {
  const { L, D, K, hostIp, hostDhcp, hostIpWifi, cliRun, shell, IP, ip4, m24, dv, ios, cfg, scfg, PW, C } = env;

  /* ---------- S06 : Wi-Fi d'entreprise (Cabinet Garcia) ---------- */
  function wfBuild(h) {
    const { dev, link, get } = h;
    dev('sw-2960', 'SW1', 330, 200, 'Switch'); dev('r-2911', 'R1', 330, 40, 'Routeur'); dev('pc-win', 'PC-GES', 80, 200, 'Poste gestion');
    dev('srv-linux', 'SRV', 80, 340, 'Serveur interne'); dev('ap-u6', 'AP-INT', 600, 120, 'Borne personnel'); dev('ap-u6', 'AP-INV', 600, 300, 'Borne invités');
    dev('laptop', 'LAP-PERS', 820, 120, 'Portable du personnel'); dev('laptop', 'LAP-INV', 820, 300, 'Portable invité');
    link('PC-GES', 'eth0', 'SW1', 'Fa0/1'); link('SRV', 'ens33', 'SW1', 'Fa0/2'); link('R1', 'gi0/0', 'SW1', 'Fa0/24');
    hostIp(get('PC-GES'), '192.168.10.11', '24', '192.168.10.1'); hostIp(get('SRV'), '192.168.10.10', '24', '192.168.10.1');
    hostDhcp(get('LAP-PERS')); hostIpWifi(get('LAP-PERS')); hostDhcp(get('LAP-INV')); hostIpWifi(get('LAP-INV'));
  }
  const WF_SW = 'enable\nconfigure terminal\nhostname SW1\nvlan 10\nname GESTION\nvlan 20\nname WIFI-PERSONNEL\nvlan 30\nname WIFI-INVITES\nexit\ninterface range fa0/1 - 2\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface fa0/10\nswitchport mode access\nswitchport access vlan 20\nexit\ninterface fa0/11\nswitchport mode access\nswitchport access vlan 30\nexit\ninterface fa0/24\nswitchport mode trunk\nend\nwrite memory';
  const WF_R = 'enable\nconfigure terminal\nhostname R1\ninterface gi0/0\nno shutdown\nexit\ninterface gi0/0.10\nencapsulation dot1Q 10\nip address 192.168.10.1 255.255.255.0\nexit\ninterface gi0/0.20\nencapsulation dot1Q 20\nip address 192.168.20.1 255.255.255.0\nexit\ninterface gi0/0.30\nencapsulation dot1Q 30\nip address 192.168.30.1 255.255.255.0\nexit\nip dhcp excluded-address 192.168.20.1 192.168.20.9\nip dhcp excluded-address 192.168.30.1 192.168.30.9\nip dhcp pool PERSONNEL\nnetwork 192.168.20.0 255.255.255.0\ndefault-router 192.168.20.1\nexit\nip dhcp pool INVITES\nnetwork 192.168.30.0 255.255.255.0\ndefault-router 192.168.30.1\nexit\nip access-list extended INVITES-IN\ndeny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255\ndeny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255\npermit ip any any\nexit\ninterface gi0/0.30\nip access-group INVITES-IN in\nend\nwrite memory';
  function wfWifi(sim, h) {
    const a = h.get('AP-INT'); a.ssid = 'GARCIA-PERSONNEL'; a.key = 'Perso#Garcia27'; a.security = 'WPA2';
    const b = h.get('AP-INV'); b.ssid = 'GARCIA-INVITES'; b.key = 'Invites2027'; b.security = 'WPA2';
    const p = h.get('LAP-PERS'); p.wifi = { ssid: 'GARCIA-PERSONNEL', key: 'Perso#Garcia27' };
    const v = h.get('LAP-INV'); v.wifi = { ssid: 'GARCIA-INVITES', key: 'Invites2027' }; L.NS.wifiRefresh(sim);
  }
  function wfSolve(sim, h) {
    const { link, get } = h;
    link('AP-INT', 'eth0', 'SW1', 'Fa0/10'); link('AP-INV', 'eth0', 'SW1', 'Fa0/11');
    cliRun(get('SW1'), WF_SW); cliRun(get('R1'), WF_R); wfWifi(sim, h);
  }
  const wfChecks = [
    { label: 'LAP-PERS reçoit une adresse du Wi-Fi personnel (192.168.20.x)', run: c => { c.wait(10000); return /^192\.168\.20\.\d+$/.test(c.ipOf('LAP-PERS')); } },
    { label: 'LAP-INV reçoit une adresse du Wi-Fi invités (192.168.30.x)', run: c => /^192\.168\.30\.\d+$/.test(c.ipOf('LAP-INV')) },
    { label: 'Le personnel joint le serveur interne', run: c => c.ping('LAP-PERS', '192.168.10.10') },
    { label: 'Les invités ne joignent PAS le serveur interne', run: c => !c.ping('LAP-INV', '192.168.10.10') },
    { label: 'Les invités ne joignent PAS le Wi-Fi du personnel', run: c => !c.ping('LAP-INV', c.ipOf('LAP-PERS')) },
    { label: 'Les invités joignent leur passerelle', run: c => c.ping('LAP-INV', '192.168.30.1') },
  ];
  TPS.push({
    id: 't06-wifi', start: D + 'S06-wifi-entreprise/tp/t06-wifi.json', solution: K + 'T06-wifi-corrige.json',
    notes: 'Terminale S06 – Cabinet Garcia : deux bornes (une par SSID, donc une par VLAN). Matériel posé, bornes non branchées, switch et routeur vierges. À faire : câbler les bornes, VLAN 10/20/30, sous-interfaces, DHCP par VLAN, ACL invités, SSID et clés.',
    build(sim, h) { h.sim = sim; wfBuild(h); }, solve: wfSolve, checks: wfChecks, startShould: wfChecks.map(x => x.label).filter(x => !/ne joignent PAS/.test(x)),
  });
  /* panne : mauvais mot de passe sur le portable, borne invités dans le mauvais VLAN, ACL absente */
  TPS.push({
    id: 't06-panne', start: D + 'S06-wifi-entreprise/tp/t06-panne.json', solution: K + 'T06-panne-corrige.json',
    notes: 'Terminale S06 – Le Wi-Fi du cabinet Garcia est installé mais : le portable du personnel n\'a pas la bonne clé, la borne invités est branchée dans le VLAN du personnel, et l\'ACL des invités a été retirée. À dépanner.',
    build(sim, h) {
      h.sim = sim; wfBuild(h); const { link } = h; link('AP-INT', 'eth0', 'SW1', 'Fa0/10'); link('AP-INV', 'eth0', 'SW1', 'Fa0/11');
      cliRun(h.get('SW1'), WF_SW.replace('interface fa0/11\nswitchport mode access\nswitchport access vlan 30', 'interface fa0/11\nswitchport mode access\nswitchport access vlan 20'));
      cliRun(h.get('R1'), WF_R.replace('interface gi0/0.30\nip access-group INVITES-IN in\n', ''));
      wfWifi(sim, h); h.get('LAP-PERS').wifi = { ssid: 'GARCIA-PERSONNEL', key: 'Perso#Garcia26' }; L.NS.wifiRefresh(sim);
    },
    solve(sim, h) {
      cliRun(h.get('SW1'), 'enable\nconf t\ninterface fa0/11\nswitchport access vlan 30\nend\nwrite memory');
      cliRun(h.get('R1'), 'enable\nconf t\ninterface gi0/0.30\nip access-group INVITES-IN in\nend\nwrite memory');
      h.get('LAP-PERS').wifi = { ssid: 'GARCIA-PERSONNEL', key: 'Perso#Garcia27' }; L.NS.wifiRefresh(sim);
      h.get('LAP-PERS').applyIp(h.get('LAP-PERS').ifaceList().find(i => i.port && i.port.media === 'wifi').name, { dhcp: true });
    },
    checks: wfChecks, startShould: wfChecks.map(x => x.label).filter(x => /LAP-PERS|Le personnel|serveur interne|LAP-INV reçoit/.test(x)),
  });

  /* ---------- S07 : mises à jour et sauvegardes (atelier Bonnet) ---------- */
  const SV_CFG = 'enable\nconfigure terminal\nhostname SW-ATELIER\nenable secret Pme#2027\nbanner motd #Atelier Bonnet - acces reserve#\nvlan 10\nname BUREAU\nvlan 20\nname ATELIER\nexit\ninterface range fa0/1 - 2\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface range fa0/3 - 4\nswitchport mode access\nswitchport access vlan 20\nend';
  function svBuild(h) {
    const { dev, link, get } = h;
    dev('sw-2960', 'SW1', 330, 180, 'Switch de l\'atelier'); dev('pc-win', 'PC-A', 80, 60, 'Bureau'); dev('pc-win', 'PC-B', 80, 300, 'Atelier');
    link('PC-A', 'eth0', 'SW1', 'Fa0/1'); link('PC-B', 'eth0', 'SW1', 'Fa0/3');
    hostIp(get('PC-A'), '192.168.1.11', '24'); hostIp(get('PC-B'), '192.168.1.12', '24');
  }
  TPS.push({
    id: 't07-sauvegarde', start: D + 'S07-maj-sauvegardes/tp/t07-sauvegarde.json', solution: K + 'T07-sauvegarde-corrige.json',
    notes: 'Terminale S07 – Le switch de l\'atelier Bonnet est configuré et fonctionne… mais la configuration n\'a JAMAIS été sauvegardée (running-config seulement). À faire : le constater (show startup-config), sauvegarder, vérifier.',
    build(sim, h) { svBuild(h); cliRun(h.get('SW1'), SV_CFG); },
    solve(sim, h) { cliRun(dv({ sim }, 'SW1'), 'enable\nPme#2027\nwrite memory'); },
    checks: [
      { label: 'Les postes de VLAN différents ne se joignent pas (VLAN actifs)', run: c => !c.ping('PC-A', '192.168.1.12') },
      { label: 'La configuration est sauvegardée (hostname dans la startup-config)', run: c => /hostname SW-ATELIER/.test(scfg(c, 'SW1')) },
      { label: 'Le mot de passe enable est dans la startup-config', run: c => /enable secret/.test(scfg(c, 'SW1')) },
      { label: 'Les deux VLAN sont dans la startup-config', run: c => /vlan 20/i.test(scfg(c, 'SW1')) && /switchport access vlan 20/.test(scfg(c, 'SW1')) },
    ],
    startShould: ['La configuration est sauvegardée (hostname dans la startup-config)', 'Le mot de passe enable est dans la startup-config', 'Les deux VLAN sont dans la startup-config'],
  });
  TPS.push({
    id: 't07-restauration', start: D + 'S07-maj-sauvegardes/tp/t07-restauration.json', solution: K + 'T07-restauration-corrige.json',
    notes: 'Terminale S07 – Le switch de l\'atelier Bonnet est mort ; voici son remplaçant, VIERGE. À faire : restaurer la configuration à partir de la sauvegarde fournie dans le TP (copier-coller), vérifier, sauvegarder.',
    build(sim, h) { svBuild(h); },
    solve(sim, h) { cliRun(dv({ sim }, 'SW1'), SV_CFG + '\nwrite memory'); },
    checks: [
      { label: 'Les postes de VLAN différents ne se joignent pas (VLAN actifs)', run: c => !c.ping('PC-A', '192.168.1.12') },
      { label: 'Le switch porte son nom SW-ATELIER', run: c => /hostname SW-ATELIER/.test(cfg(c, 'SW1')) },
      { label: 'La configuration restaurée est sauvegardée', run: c => /hostname SW-ATELIER/.test(scfg(c, 'SW1')) && /switchport access vlan 20/.test(scfg(c, 'SW1')) },
    ],
    startShould: ['Les postes de VLAN différents ne se joignent pas (VLAN actifs)', 'Le switch porte son nom SW-ATELIER', 'La configuration restaurée est sauvegardée'],
  });

  /* ---------- S08 : intégrer des équipements (cabinet d'architectes Lemoine) ---------- */
  function inBuild(h) {
    const { dev, get } = h;
    dev('sw-3560', 'CORE', 330, 180, 'Switch cœur'); dev('pc-win', 'PC-1', 80, 60, 'Poste bureau'); dev('pc-win', 'PC-2', 80, 300, 'Poste bureau 2');
    dev('printer', 'IMP', 600, 60, 'Imprimante réseau'); dev('nas', 'NAS', 600, 300, 'NAS sauvegarde');
    hostDhcp(get('PC-1')); hostDhcp(get('PC-2'));
  }
  const IN_CORE = 'enable\nconfigure terminal\nhostname CORE\nip routing\nvlan 10\nname POSTES\nvlan 40\nname OBJETS\nexit\ninterface range fa0/1 - 2\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface range fa0/3 - 4\nswitchport mode access\nswitchport access vlan 40\nexit\ninterface vlan 10\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface vlan 40\nip address 192.168.40.1 255.255.255.0\nno shutdown\nexit\nip dhcp excluded-address 192.168.10.1 192.168.10.49\nip dhcp pool POSTES\nnetwork 192.168.10.0 255.255.255.0\ndefault-router 192.168.10.1\nexit\nend\nwrite memory';
  function inSolve(sim, h) {
    const { link, get } = h;
    link('PC-1', 'eth0', 'CORE', 'Fa0/1'); link('PC-2', 'eth0', 'CORE', 'Fa0/2');
    link('IMP', get('IMP').ifaceList()[0].port.name, 'CORE', 'Fa0/3'); link('NAS', get('NAS').ifaceList()[0].port.name, 'CORE', 'Fa0/4');
    cliRun(get('CORE'), IN_CORE);
    hostIp(get('IMP'), '192.168.40.20', '24', '192.168.40.1'); hostIp(get('NAS'), '192.168.40.30', '24', '192.168.40.1');
  }
  const inChecks = [
    { label: 'PC-1 reçoit une adresse du VLAN postes (192.168.10.50 et +)', run: c => { c.wait(10000); return /^192\.168\.10\.(5\d|[6-9]\d|\d{3})$/.test(c.ipOf('PC-1')); } },
    { label: 'PC-1 joint l\'imprimante (192.168.40.20)', run: c => c.ping('PC-1', '192.168.40.20') },
    { label: 'PC-2 joint le NAS (192.168.40.30)', run: c => c.ping('PC-2', '192.168.40.30') },
    { label: 'L\'imprimante et le NAS sont hors de la plage DHCP (adresses réservées)', run: c => /excluded-address 192\.168\.10\.1 192\.168\.10\.49/.test(cfg(c, 'CORE')) && /192\.168\.40\.20/.test(c.ipOf('IMP')) },
    { label: 'Configuration du switch sauvegardée', run: c => /hostname CORE/.test(scfg(c, 'CORE')) && /vlan 40/i.test(scfg(c, 'CORE')) },
  ];
  TPS.push({
    id: 't08-integration', start: D + 'S08-integrer-equipements/tp/t08-integration.json', solution: K + 'T08-integration-corrige.json',
    notes: 'Terminale S08 – Cabinet Lemoine : deux postes, une imprimante réseau et un NAS posés sur le plan, aucun câble, switch cœur (niveau 3) vierge. À faire : câbler, créer le VLAN OBJETS (40), adresser l\'imprimante et le NAS en statique hors plage DHCP, tester, documenter.',
    build(sim, h) { inBuild(h); }, solve: inSolve, checks: inChecks, startShould: inChecks.map(x => x.label),
  });

  /* ---------- S09 : accès à distance sécurisé (garage Dupuy) ---------- */
  function adBuild(h) {
    const { dev, link, get } = h;
    C.internet(h.sim, h, 900, 200);
    dev('pc-win', 'DISTANT', 1100, 380, 'Technicien à distance'); dev('sw-8p', 'SW-FAI2', 1100, 300); 
    dev('r-2911', 'R1', 600, 200, 'Routeur de l\'entreprise'); dev('sw-2960', 'SW1', 400, 200); dev('pc-win', 'PC-ADM', 150, 100, 'Poste admin'); dev('srv-linux', 'SRV', 150, 300, 'Serveur web interne');
    link('R1', 'gi0/0', 'FAI', 'gi0/2'); link('R1', 'gi0/1', 'SW1', 'Fa0/24'); link('PC-ADM', 'eth0', 'SW1', 'Fa0/1'); link('SRV', 'ens33', 'SW1', 'Fa0/2');
    link('SW-FAI2', 'port1', 'SW-FAI', 'port4'); link('DISTANT', 'eth0', 'SW-FAI2', 'port2');
    hostIp(get('PC-ADM'), '192.168.1.50', '24', '192.168.1.1', '198.51.100.53'); hostIp(get('SRV'), '192.168.1.10', '24', '192.168.1.1');
    hostIp(get('DISTANT'), '198.51.100.100', '24', '198.51.100.1');
    get('SRV').httpd.pages['/'] = { type: 'text/html; charset=utf-8', body: '<html><body><h1>Intranet du garage Dupuy</h1></body></html>', _custom: true }; get('SRV').httpd.start();
    cliRun(get('FAI'), 'enable\nconf t\ninterface gi0/2\nip address 203.0.113.2 255.255.255.248\nno shutdown\nend');
  }
  const AD_R_BASE = 'enable\nconfigure terminal\nhostname R1\ninterface gi0/0\nip address 203.0.113.3 255.255.255.248\nip nat outside\nno shutdown\nexit\ninterface gi0/1\nip address 192.168.1.1 255.255.255.0\nip nat inside\nno shutdown\nexit\nip route 0.0.0.0 0.0.0.0 203.0.113.2\naccess-list 1 permit 192.168.1.0 0.0.0.255\nip nat inside source list 1 interface gi0/0 overload\n';
  const AD_R_SSH = 'ip domain-name garage.local\nusername tech privilege 15 secret Tech#2027\ncrypto key generate rsa modulus 1024\nip ssh version 2\nline vty 0 4\ntransport input ssh\nlogin local\nexit\n';
  const AD_R_FWD = 'ip nat inside source static tcp 192.168.1.10 80 203.0.113.3 8080\n';
  TPS.push({
    id: 't09-acces', start: D + 'S09-acces-distance/tp/t09-acces.json', solution: K + 'T09-acces-corrige.json',
    notes: 'Terminale S09 – Garage Dupuy : le routeur est en place (accès Internet par NAT) mais l\'administration se fait en telnet (sans chiffrement) et le serveur web interne n\'est pas joignable de l\'extérieur. À faire : passer en SSH, désactiver telnet, publier le site par une redirection de port 8080 → 80, tester depuis « Technicien à distance ».',
    build(sim, h) { h.sim = sim; adBuild(h); cliRun(h.get('R1'), AD_R_BASE + 'line vty 0 4\npassword Telnet123\nlogin\nend\nwrite memory'); },
    solve(sim, h) { cliRun(dv({ sim }, 'R1'), 'enable\nconfigure terminal\n' + AD_R_SSH + AD_R_FWD + 'end\nwrite memory'); },
    checks: [
      { label: 'Le réseau interne accède à Internet (NAT)', run: c => { c.wait(8000); const r = c.http('PC-ADM', 'http://www.exemple.fr'); return !!r && r.status === 200; } },
      { label: 'Le routeur n\'accepte que SSH (transport input ssh)', run: c => /transport input ssh/.test(cfg(c, 'R1')) },
      { label: 'Un compte nominatif existe sur le routeur (username tech)', run: c => /username tech/.test(cfg(c, 'R1')) },
      { label: 'Le technicien à distance ouvre le site interne par le port 8080', run: c => { const r = c.http('DISTANT', 'http://203.0.113.3:8080'); return !!r && r.status === 200; } },
      { label: 'Le technicien à distance n\'atteint PAS le serveur par le port 80', run: c => { const r = c.http('DISTANT', 'http://203.0.113.3'); return !r || r.status !== 200; } },
      { label: 'Configuration sauvegardée', run: c => /transport input ssh/.test(scfg(c, 'R1')) },
    ],
    startShould: ['Le routeur n\'accepte que SSH (transport input ssh)', 'Un compte nominatif existe sur le routeur (username tech)', 'Le technicien à distance ouvre le site interne par le port 8080', 'Configuration sauvegardée'],
  });

  /* ---------- S10 : supervision (imprimerie Laporte) ---------- */
  function suBuild(h) {
    const { dev, link, get } = h;
    dev('sw-2960', 'SW1', 330, 180, 'Switch'); dev('srv-linux', 'SUP', 80, 60, 'Poste de supervision'); dev('pc-win', 'PC-1', 80, 300, 'Poste'); dev('printer', 'IMP', 600, 300, 'Imprimante');
    link('SUP', 'ens33', 'SW1', 'Fa0/1'); link('PC-1', 'eth0', 'SW1', 'Fa0/2'); link('IMP', get('IMP').ifaceList()[0].port.name, 'SW1', 'Fa0/3');
    hostIp(get('SUP'), '192.168.1.5', '24', '192.168.1.1'); hostIp(get('PC-1'), '192.168.1.50', '24', '192.168.1.1'); hostIp(get('IMP'), '192.168.1.20', '24', '192.168.1.1');
    cliRun(get('SW1'), 'enable\nconfigure terminal\nhostname SW-IMPRIMERIE\ninterface vlan 1\nip address 192.168.1.2 255.255.255.0\nno shutdown\nend\nwrite memory');
  }
  const SU_CFG = 'enable\nconfigure terminal\nsnmp-server community supervision RO\nsnmp-server location Atelier - baie 1\nsnmp-server contact support@laporte-imprimerie.fr\nsnmp-server host 192.168.1.5 version 2c supervision\nsnmp-server enable traps\nlogging host 192.168.1.5\nlogging trap informational\nservice sequence-numbers\nend\nwrite memory';
  const suSh = (c, dst, cmd) => shell(c.sim, dv(c, dst), cmd);
  TPS.push({
    id: 't10-supervision', start: D + 'S10-supervision-tickets/tp/t10-supervision.json', solution: K + 'T10-supervision-corrige.json',
    notes: 'Terminale S10 – Imprimerie Laporte : switch administrable (192.168.1.2) et poste de supervision SUP (192.168.1.5). À faire : activer SNMP (communauté de lecture), envoyer les journaux vers SUP, interroger le switch depuis SUP (snmpget/snmpwalk), observer une alerte quand un câble est débranché, sauvegarder.',
    build(sim, h) { suBuild(h); },
    solve(sim, h) { cliRun(dv({ sim }, 'SW1'), SU_CFG); },
    checks: [
      { label: 'SUP interroge le switch en SNMP (snmpget sysName)', run: c => /SW-IMPRIMERIE/.test(suSh(c, 'SUP', 'snmpget -v2c -c supervision 192.168.1.2 1.3.6.1.2.1.1.5.0')) },
      { label: 'SUP lit l\'emplacement du switch (snmpget sysLocation)', run: c => /baie 1/.test(suSh(c, 'SUP', 'snmpget -v2c -c supervision 192.168.1.2 1.3.6.1.2.1.1.6.0')) },
      { label: 'Le switch envoie ses journaux vers SUP (logging host)', run: c => /logging host 192\.168\.1\.5/.test(cfg(c, 'SW1')) },
      { label: 'Les alertes (traps SNMP) sont envoyées vers SUP', run: c => /snmp-server host 192\.168\.1\.5/.test(cfg(c, 'SW1')) },
      { label: 'Configuration sauvegardée', run: c => /snmp-server community supervision/.test(scfg(c, 'SW1')) },
    ],
    startShould: ['SUP interroge le switch en SNMP (snmpget sysName)', 'SUP lit l\'emplacement du switch (snmpget sysLocation)', 'Le switch envoie ses journaux vers SUP (logging host)', 'Les alertes (traps SNMP) sont envoyées vers SUP', 'Configuration sauvegardée'],
  });

  /* ---------- S11 : dépanner (1) – PME Delmas, trois ateliers de pannes ---------- */
  function dpBuild(h, f) {
    f = f || {};
    const { dev, link, get } = h;
    dev('sw-2960', 'SW1', 330, 180, 'Switch'); dev('r-2911', 'R1', 330, 20, 'Routeur'); dev('pc-win', 'PC-CPT', 80, 60, 'Bureau'); dev('pc-win', 'PC-COM', 80, 300, 'Atelier'); dev('srv-linux', 'SRV', 600, 180, 'Serveur intranet');
    link('PC-CPT', 'eth0', 'SW1', 'Fa0/1'); link('SRV', 'ens33', 'SW1', 'Fa0/2'); link('PC-COM', 'eth0', 'SW1', 'Fa0/3'); link('R1', 'gi0/0', 'SW1', 'Fa0/24');
    hostDhcp(get('PC-CPT'));
    hostIp(get('PC-COM'), '192.168.20.11', '24', f.gw || '192.168.20.1', '192.168.30.10'); hostIp(get('SRV'), '192.168.30.10', '24', '192.168.30.1', '192.168.30.10');
    const s = get('SRV'); s.dnsd.records = [{ name: 'intranet.delmas.local', type: 'A', data: f.dnsIp || '192.168.30.10' }]; s.dnsd.start();
    s.httpd.pages['/'] = { type: 'text/html; charset=utf-8', body: '<html><body><h1>Intranet Delmas</h1></body></html>', _custom: true }; s.httpd.start();
    if (!f.noSw) cliRun(get('SW1'), 'enable\nconfigure terminal\nhostname SW1\nvlan 10\nname BUREAU\nvlan 20\nname ATELIER\nvlan 30\nname SERVEURS\nexit\ninterface fa0/1\nswitchport mode access\nswitchport access vlan ' + (f.vlanCpt || 10) + '\nexit\ninterface fa0/2\nswitchport mode access\nswitchport access vlan 30\nexit\ninterface fa0/3\nswitchport mode access\nswitchport access vlan 20\n' + (f.shutCom ? 'shutdown\n' : '') + 'exit\ninterface fa0/24\nswitchport mode trunk\nend\nwrite memory');
    cliRun(get('R1'), 'enable\nconfigure terminal\nhostname R1\ninterface gi0/0\nno shutdown\nexit\ninterface gi0/0.10\nencapsulation dot1Q 10\nip address 192.168.10.1 255.255.255.0\nexit\ninterface gi0/0.20\nencapsulation dot1Q 20\nip address 192.168.20.1 255.255.255.0\n' + (f.shutSub ? 'shutdown\n' : '') + 'exit\ninterface gi0/0.30\nencapsulation dot1Q 30\nip address 192.168.30.1 255.255.255.0\nexit\nip dhcp excluded-address 192.168.10.1 192.168.10.49\nip dhcp pool BUREAU\nnetwork 192.168.10.0 255.255.255.0\ndefault-router 192.168.10.1\n' + (f.noDns ? '' : 'dns-server 192.168.30.10\n') + 'exit\nend\nwrite memory');
  }
  const dpChecks = [
    { label: 'PC-CPT obtient une adresse du réseau Bureau (192.168.10.x)', run: c => { c.wait(10000); return /^192\.168\.10\.\d+$/.test(c.ipOf('PC-CPT')); } },
    { label: 'PC-CPT ouvre http://intranet.delmas.local', run: c => { const r = c.http('PC-CPT', 'http://intranet.delmas.local'); return !!r && r.status === 200; } },
    { label: 'PC-COM ouvre http://intranet.delmas.local', run: c => { const r = c.http('PC-COM', 'http://intranet.delmas.local'); return !!r && r.status === 200; } },
    { label: 'PC-COM joint le serveur (192.168.30.10)', run: c => c.ping('PC-COM', '192.168.30.10') },
  ];
  const dpFix = {
    a: 'enable\nconf t\ninterface fa0/3\nno shutdown\nend\nwrite memory',
    b: 'enable\nconf t\ninterface fa0/1\nswitchport access vlan 10\nend\nwrite memory',
    c: 'enable\nconf t\ninterface gi0/0.20\nno shutdown\nexit\nip dhcp pool BUREAU\ndns-server 192.168.30.10\nend\nwrite memory',
  };
  [['a', 'Atelier A : le poste de l\'atelier n\'a plus rien (port coupé et mauvaise passerelle)', { shutCom: 1, gw: '192.168.20.254' }, 'PC-COM : passerelle erronée (192.168.20.254) et port Fa0/3 désactivé.'],
   ['b', 'Atelier B : le poste du bureau n\'a plus d\'adresse et le nom intranet ne marche pas', { vlanCpt: 30, dnsIp: '192.168.30.11' }, 'PC-CPT : port Fa0/1 dans le VLAN 30 (au lieu de 10) ; DNS : la fiche intranet pointe vers 192.168.30.11.'],
   ['c', 'Atelier C : l\'atelier ne joint plus le serveur et le bureau n\'ouvre l\'intranet que par adresse', { shutSub: 1, noDns: 1 }, 'R1 : sous-interface gi0/0.20 arrêtée ; pool DHCP BUREAU sans dns-server.']].forEach(([k, titre, f, cause]) => {
    TPS.push({
      id: 't11-' + k, start: D + 'S11-depanner-1/tp/t11-panne-' + k + '.json', solution: K + 'T11-panne-' + k + '-corrige.json',
      notes: 'Terminale S11 – PME Delmas, ' + titre + '. Deux défauts sont cachés : à toi de les trouver avec la démarche du cours (les quatre tests de la fiche doivent être verts).',
      build(sim, h) { h.sim = sim; dpBuild(h, f); },
      solve(sim, h) {
        if (k === 'a') { cliRun(dv({ sim }, 'SW1'), dpFix.a); h.get('PC-COM').setGateway('192.168.20.1'); }
        if (k === 'b') { cliRun(dv({ sim }, 'SW1'), dpFix.b); const s = h.get('SRV'); s.dnsd.records = [{ name: 'intranet.delmas.local', type: 'A', data: '192.168.30.10' }]; const p = h.get('PC-CPT'); p.applyIp(p.ifaceList()[0].name, { dhcp: true }); }
        if (k === 'c') { cliRun(dv({ sim }, 'R1'), dpFix.c); const p = h.get('PC-CPT'); p.applyIp(p.ifaceList()[0].name, { dhcp: true }); }
      },
      checks: dpChecks, startShould: k === 'a' ? [dpChecks[2].label, dpChecks[3].label] : k === 'b' ? [dpChecks[0].label, dpChecks[1].label, dpChecks[2].label] : [dpChecks[1].label, dpChecks[2].label, dpChecks[3].label],
    });
  });

  /* ---------- S12 : remplacer un switch et restaurer (PME Delmas) ---------- */
  const DP_SW_BACKUP = 'enable\nconfigure terminal\nhostname SW1\nvlan 10\nname BUREAU\nvlan 20\nname ATELIER\nvlan 30\nname SERVEURS\nexit\ninterface fa0/1\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface fa0/2\nswitchport mode access\nswitchport access vlan 30\nexit\ninterface fa0/3\nswitchport mode access\nswitchport access vlan 20\nexit\ninterface fa0/24\nswitchport mode trunk\nend\nwrite memory';
  TPS.push({
    id: 't12-remplacement', start: D + 'S12-depanner-2/tp/t12-remplacement.json', solution: K + 'T12-remplacement-corrige.json',
    notes: 'Terminale S12 – Le switch de la PME Delmas a grillé. Son remplaçant, identique, est déjà câblé aux mêmes ports mais VIERGE. À faire : restaurer la configuration à partir de la sauvegarde fournie dans le TP, vérifier que tout est revenu à la normale (4 tests), sauvegarder, rédiger le compte rendu.',
    build(sim, h) { h.sim = sim; dpBuild(h, { noSw: 1 }); },
    solve(sim, h) { cliRun(dv({ sim }, 'SW1'), DP_SW_BACKUP); const p = h.get('PC-CPT'); p.applyIp(p.ifaceList()[0].name, { dhcp: true }); },
    checks: dpChecks.concat([{ label: 'Le switch de remplacement est sauvegardé (startup-config)', run: c => /hostname SW1/.test(scfg(c, 'SW1')) && /switchport trunk|mode trunk/.test(scfg(c, 'SW1')) }]),
    startShould: dpChecks.map(x => x.label).concat(['Le switch de remplacement est sauvegardé (startup-config)']),
  });
};
