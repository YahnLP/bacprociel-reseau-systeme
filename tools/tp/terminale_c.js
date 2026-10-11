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
};
