/* Terminale – TP S05 et suivants. Chargé par terminale.js. */
module.exports = function (TPS, env) {
  const { L, D, K, hostIp, hostDhcp, hostIpWifi, cliRun, shell, IP, ip4, m24, dv, ios, cfg, scfg, PW, C } = env;

  /* ---------- S05 : inter-VLAN (PME Rivière) ---------- */
  function ivBuild(h) {
    const { dev, link, get } = h;
    dev('pc-win', 'PC-CPT', 80, 80, 'Comptabilité'); dev('srv-linux', 'SRV', 80, 260, 'Serveur'); dev('sw-2960', 'SW1', 300, 170, 'Switch 1');
    dev('r-2911', 'R1', 300, 20, 'Routeur'); dev('sw-2960', 'SW2', 560, 170, 'Switch 2'); dev('pc-win', 'PC-COM', 780, 170, 'Commercial');
    link('PC-CPT', 'eth0', 'SW1', 'Fa0/1'); link('SRV', 'ens33', 'SW1', 'Fa0/2'); link('R1', 'gi0/0', 'SW1', 'Fa0/24'); link('SW1', 'Gi0/1', 'SW2', 'Gi0/1'); link('PC-COM', 'eth0', 'SW2', 'Fa0/1');
    hostIp(get('PC-CPT'), '192.168.10.11', '24', '192.168.10.1'); hostIp(get('PC-COM'), '192.168.20.11', '24', '192.168.20.1'); hostIp(get('SRV'), '192.168.30.10', '24', '192.168.30.1');
  }
  const IV_SW1 = 'enable\nconfigure terminal\nhostname SW1\nvlan 10\nname COMPTA\nvlan 20\nname COMMERCIAL\nvlan 30\nname SERVEURS\nexit\ninterface fa0/1\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface fa0/2\nswitchport mode access\nswitchport access vlan 30\nexit\ninterface fa0/24\nswitchport mode trunk\nexit\ninterface gi0/1\nswitchport mode trunk\nend\nwrite memory';
  const IV_SW2 = 'enable\nconfigure terminal\nhostname SW2\nvlan 10\nname COMPTA\nvlan 20\nname COMMERCIAL\nvlan 30\nname SERVEURS\nexit\ninterface fa0/1\nswitchport mode access\nswitchport access vlan 20\nexit\ninterface gi0/1\nswitchport mode trunk\nend\nwrite memory';
  const IV_R1 = 'enable\nconfigure terminal\nhostname R1\ninterface gi0/0\nno shutdown\nexit\ninterface gi0/0.10\nencapsulation dot1Q 10\nip address 192.168.10.1 255.255.255.0\nexit\ninterface gi0/0.20\nencapsulation dot1Q 20\nip address 192.168.20.1 255.255.255.0\nexit\ninterface gi0/0.30\nencapsulation dot1Q 30\nip address 192.168.30.1 255.255.255.0\nexit\nip access-list extended COMMERCIAL-IN\ndeny ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255\npermit ip any any\nexit\ninterface gi0/0.20\nip access-group COMMERCIAL-IN in\nend\nwrite memory';
  const ivChecks = [
    { label: 'VLAN : PC-CPT et SRV sont dans des VLAN différents (VLAN 10 et 30)', run: c => /10\s+COMPTA[^\n]*Fa0\/1\b/.test(ios(c, 'SW1', 'show vlan brief', PW)) && /30\s+SERVEURS[^\n]*Fa0\/2\b/.test(ios(c, 'SW1', 'show vlan brief', PW)) },
    { label: 'Trunk SW1–SW2 actif', run: c => /Gi0\/1\s+on/.test(ios(c, 'SW2', 'show interfaces trunk', PW)) },
    { label: 'Inter-VLAN : PC-CPT joint le serveur', run: c => { c.wait(8000); return c.ping('PC-CPT', '192.168.30.10'); } },
    { label: 'Inter-VLAN : PC-COM joint le serveur', run: c => c.ping('PC-COM', '192.168.30.10') },
    { label: 'PC-CPT joint PC-COM', run: c => c.ping('PC-CPT', '192.168.20.11') ? true : true },
    { label: 'Filtrage : PC-COM ne joint PAS la comptabilité', run: c => !c.ping('PC-COM', '192.168.10.11') },
  ];
  ivChecks[4] = { label: 'Filtrage : PC-CPT ne joint PAS PC-COM (aucun échange compta ↔ commercial)', run: c => !c.ping('PC-CPT', '192.168.20.11') };
  TPS.push({
    id: 't05-intervlan', start: D + 'S05-inter-vlan/tp/t05-intervlan.json', solution: K + 'T05-intervlan-corrige.json',
    notes: 'Terminale S05 – PME Rivière : 3 VLAN (Compta 10, Commercial 20, Serveurs 30), deux switches, un routeur (« router on a stick »). Les postes sont adressés ; switches et routeur sont vierges. À faire : VLAN, trunks, sous-interfaces, ACL (le commercial ne doit pas joindre la compta).',
    build(sim, h) { ivBuild(h); }, solve(sim, h) { cliRun(h.get('SW1'), IV_SW1); cliRun(h.get('SW2'), IV_SW2); cliRun(h.get('R1'), IV_R1); },
    checks: ivChecks, startShould: ivChecks.filter(x => !/ne joint PAS/.test(x.label)).map(x => x.label),
  });
  TPS.push({
    id: 't05-panne', start: D + 'S05-inter-vlan/tp/t05-panne.json', solution: K + 'T05-panne-corrige.json',
    notes: 'Terminale S05 – La PME Rivière marchait, puis un collègue a modifié trois choses : le trunk de SW2 n\'autorise plus le VLAN 20, la sous-interface Gi0/0.30 a une mauvaise encapsulation, le serveur a une mauvaise passerelle. À dépanner.',
    build(sim, h) {
      ivBuild(h); cliRun(h.get('SW1'), IV_SW1); cliRun(h.get('SW2'), IV_SW2); cliRun(h.get('R1'), IV_R1);
      cliRun(dv({ sim }, 'SW2'), 'enable\nconf t\ninterface gi0/1\nswitchport trunk allowed vlan 10,30\nend\nwrite memory');
      cliRun(h.get('R1'), 'enable\nconf t\ninterface gi0/0.30\nencapsulation dot1Q 3\nend\nwrite memory');
      h.get('SRV').setGateway('192.168.30.254');
    },
    solve(sim, h) {
      cliRun(h.get('SW2'), 'enable\nconf t\ninterface gi0/1\nswitchport trunk allowed vlan add 20\nend\nwrite memory');
      cliRun(h.get('R1'), 'enable\nconf t\ninterface gi0/0.30\nencapsulation dot1Q 30\nend\nwrite memory');
      h.get('SRV').setGateway('192.168.30.1');
    },
    checks: ivChecks.filter(x => !/VLAN : PC-CPT/.test(x.label)), startShould: ivChecks.filter(x => /PC-COM joint le serveur|PC-CPT joint le serveur/.test(x.label)).map(x => x.label),
  });

  /* extension S05 : le même réseau avec un switch de niveau 3 (SVI) */
  function l3Build(h) {
    const { dev, link, get } = h;
    dev('sw-3560', 'CORE', 300, 150, 'Switch cœur (niveau 3)'); dev('sw-2960', 'SW-ETAGE', 560, 150, 'Switch étage'); dev('pc-win', 'PC-CPT', 80, 60, 'Comptabilité'); dev('srv-linux', 'SRV', 80, 240, 'Serveur'); dev('pc-win', 'PC-COM', 780, 150, 'Commercial');
    link('PC-CPT', 'eth0', 'CORE', 'Fa0/1'); link('SRV', 'ens33', 'CORE', 'Fa0/2'); link('CORE', 'Gi0/1', 'SW-ETAGE', 'Gi0/1'); link('PC-COM', 'eth0', 'SW-ETAGE', 'Fa0/1');
    hostIp(get('PC-CPT'), '192.168.10.11', '24', '192.168.10.1'); hostIp(get('PC-COM'), '192.168.20.11', '24', '192.168.20.1'); hostIp(get('SRV'), '192.168.30.10', '24', '192.168.30.1');
  }
  const L3_CORE = 'enable\nconfigure terminal\nhostname CORE\nip routing\nvlan 10\nname COMPTA\nvlan 20\nname COMMERCIAL\nvlan 30\nname SERVEURS\nexit\ninterface fa0/1\nswitchport mode access\nswitchport access vlan 10\nexit\ninterface fa0/2\nswitchport mode access\nswitchport access vlan 30\nexit\ninterface gi0/1\nswitchport trunk encapsulation dot1q\nswitchport mode trunk\nexit\ninterface vlan 10\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface vlan 20\nip address 192.168.20.1 255.255.255.0\nno shutdown\nexit\ninterface vlan 30\nip address 192.168.30.1 255.255.255.0\nno shutdown\nend\nwrite memory';
  const L3_ET = 'enable\nconfigure terminal\nhostname SW-ETAGE\nvlan 20\nname COMMERCIAL\nexit\ninterface fa0/1\nswitchport mode access\nswitchport access vlan 20\nexit\ninterface gi0/1\nswitchport mode trunk\nend\nwrite memory';
  const l3Checks = [
    { label: 'Le switch cœur route (ip routing, 3 interfaces VLAN)', run: c => { const o = ios(c, 'CORE', 'show ip interface brief', PW); return /Vlan10/.test(o) && /Vlan20/.test(o) && /Vlan30/.test(o); } },
    { label: 'PC-CPT joint le serveur', run: c => { c.wait(8000); return c.ping('PC-CPT', '192.168.30.10'); } },
    { label: 'PC-COM joint le serveur (à travers le trunk)', run: c => c.ping('PC-COM', '192.168.30.10') },
    { label: 'PC-COM joint PC-CPT', run: c => c.ping('PC-COM', '192.168.10.11') },
  ];
  TPS.push({
    id: 't05-l3', start: D + 'S05-inter-vlan/tp/t05-switch-niveau3.json', solution: K + 'T05-switch-niveau3-corrige.json',
    notes: 'Terminale S05 – Extension : la même PME avec un switch de niveau 3 (Catalyst 3560) à la place du routeur : routage activé (ip routing) et interfaces VLAN (SVI).',
    build(sim, h) { l3Build(h); }, solve(sim, h) { cliRun(h.get('CORE'), L3_CORE); cliRun(h.get('SW-ETAGE'), L3_ET); },
    checks: l3Checks, startShould: l3Checks.map(x => x.label),
  });
};
