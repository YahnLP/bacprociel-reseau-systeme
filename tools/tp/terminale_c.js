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
};
